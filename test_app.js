// End-to-end regression tests against a real browser and persistent localStorage.
const { chromium } = require('playwright');
const assert = require('node:assert/strict');
const fs = require('node:fs');
const http = require('node:http');
const path = require('node:path');
const vocab = JSON.parse(fs.readFileSync('a2_vocab.json', 'utf8'));
const H = 'tocfl_a2_fc_hist', B = 'tocfl_a2_fc_bookmarks';
const results = [], errors = [];
const server = http.createServer((req,res) => {
  if (req.url === '/favicon.ico') { res.writeHead(204); return res.end(); }
  res.setHeader('Content-Type','text/html; charset=utf-8');
  res.end(fs.readFileSync('index.html'));
});
(async () => {
  await new Promise(r => server.listen(0,'127.0.0.1',r));
  const base = process.env.TEST_URL || `http://127.0.0.1:${server.address().port}`;
  const browser = await chromium.launch({headless:true, channel:process.env.TEST_BROWSER || 'chrome'});
  const context = await browser.newContext({viewport:{width:1280,height:900}});
  const page = await context.newPage();
  page.on('pageerror', e => errors.push(e.message));
  async function check(name, fn) {
    try { await fn(); results.push({name,status:'PASS'}); console.log('PASS '+name); }
    catch(e) { results.push({name,status:'FAIL',error:e.message}); console.log('FAIL '+name+': '+e.message); }
  }
  const select = async u => page.locator(`#sidebarContent [data-unit="${u}"]`).click();
  const text = id => page.locator('#'+id).textContent();
  const hist = () => page.evaluate(k=>JSON.parse(localStorage.getItem(k)||'{}'),H);
  const reset = async () => { await page.evaluate(()=>localStorage.clear()); await page.reload(); };
  const visible = async id => assert(await page.locator('#'+id).isVisible(),id+' visible');
  try {
    await page.goto(base);
    await check('500 entries, 20 ordered units, 25 per unit, unique stable IDs', async()=>{
      assert.equal(vocab.length,500); assert.equal(new Set(vocab.map(v=>v.id)).size,500);
      for(let u=1;u<=20;u++) {
        assert.equal(vocab.filter(v=>v.unit==='U'+u).length,25);
        await select('U'+u); assert.equal(await text('hanzi'),vocab[(u-1)*25].word);
      }
      assert.equal(await page.locator('#sidebarContent [data-unit^="U"]').count(),20);
    });
    await check('Initial statistics and hidden answer',async()=>{
      await reset(); assert.equal(await text('totalWords'),'500'); assert.equal(await text('totalReviewed'),'0');
      await select('U1'); assert.equal(await text('hanzi'),vocab[0].word);
      assert.equal(await page.locator('.reveal-area').isVisible(),false);
    });
    await check('All 500 rendered cards exactly match imported text',async()=>{
      const rendered=await page.evaluate(()=>VOCAB.map(v=>{
        selectUnit(v.unit);curIdx=curWords.indexOf(v);showCard();doFlip();
        return {id:v.id,word:document.getElementById('hanzi').textContent,pinyin:document.getElementById('pinyin').textContent,meaning:document.getElementById('meaning').textContent};
      }));
      assert.deepEqual(rendered,vocab.map(({id,word,pinyin,meaning})=>({id,word,pinyin,meaning})));
      await reset();await select('U1');
    });
    await check('Pass records T, flip records exactly one F, next advances',async()=>{
      await page.click('#btnPass'); assert.deepEqual((await hist())[vocab[0].id],['T']);
      await page.click('#btnFlip'); await visible('meaning');
      assert.equal(await text('pinyin'),vocab[1].pinyin); assert.equal(await text('meaning'),vocab[1].meaning);
      await page.evaluate(()=>doFlip()); assert.deepEqual((await hist())[vocab[1].id],['F']);
      await page.click('#btnFailNext'); assert.equal(await text('hanzi'),vocab[2].word);
    });
    await check('Keyboard right, Space, left, Enter, B and held-key guard',async()=>{
      await page.keyboard.press('ArrowRight'); await page.keyboard.press('Space');
      assert.deepEqual((await hist())[vocab[3].id],['F']);
      await page.keyboard.press('ArrowLeft'); assert.equal(await text('hanzi'),vocab[4].word);
      await page.keyboard.press('Space'); await page.keyboard.press('Enter');
      assert.equal(await text('hanzi'),vocab[5].word);
      await page.keyboard.press('b'); assert.equal(await page.locator('#btnBookmark').getAttribute('aria-pressed'),'true');
      await page.keyboard.press('B'); assert.equal(await page.locator('#btnBookmark').getAttribute('aria-pressed'),'false');
      const before=await hist(); await page.evaluate(()=>document.dispatchEvent(new KeyboardEvent('keydown',{key:'ArrowRight',repeat:true})));
      assert.deepEqual(await hist(),before);
    });
    await check('Bookmarks and history persist across reload and browser page',async()=>{
      await select('U1'); await page.click('#btnBookmark'); await page.reload(); await select('U1');
      assert.equal(await page.locator('#btnBookmark').getAttribute('aria-pressed'),'true');
      assert.deepEqual((await hist())[vocab[0].id],['T']);
      await select('__BOOKMARKED__'); assert.equal(await text('hanzi'),vocab[0].word);
      const other=await context.newPage(); await other.goto(base);
      assert.equal(await other.evaluate(k=>JSON.parse(localStorage.getItem(k))['a2-001'],B),true); await other.close();
    });
    await check('Full session totals, completion and restart',async()=>{
      await reset(); await select('U2');
      await page.click('#btnFlip'); await page.click('#btnFailNext');
      for(let i=1;i<25;i++) await page.click('#btnPass');
      await visible('sessionComplete'); assert.equal(await text('sessionPass'),'24'); assert.equal(await text('sessionFail'),'1');
      assert((await text('sessionMsg')).includes('96%'));
      await page.evaluate(()=>doPass()); assert.equal(Object.keys(await hist()).length,25);
      await page.click('#btnRestart'); assert.equal(await text('hanzi'),vocab[25].word);
    });
    await check('Hard words appear only after five historical F results',async()=>{
      await reset();
      for(let i=0;i<4;i++) {await select('U1'); await page.click('#btnFlip');}
      await select('__HARD_WORDS__'); await visible('emptyHardState');
      await select('U1'); await page.click('#btnFlip'); await select('__HARD_WORDS__');
      await visible('studyView'); assert.equal(await text('hanzi'),vocab[0].word);
      await page.click('#btnPass'); await visible('sessionComplete'); await page.click('#btnRestart'); await visible('studyView');
    });
    await check('Cancel reset and modal blocks study keyboard',async()=>{
      await select('U1'); const before=await hist(); await page.click('#resetBtn');
      await page.keyboard.press('ArrowRight'); await page.keyboard.press('Space'); assert.deepEqual(await hist(),before);
      await page.click('#resetCancel'); assert.deepEqual(await hist(),before);
    });
    await check('Unit reset preserves other units and bookmarks',async()=>{
      await select('U2'); await page.click('#btnPass'); await select('U1'); await page.click('#btnBookmark');
      await page.click('#resetBtn'); await page.click('#resetConfirm');
      assert.equal((await hist())[vocab[0].id],undefined); assert.deepEqual((await hist())[vocab[25].id],['T']);
      assert.equal(await page.locator('#btnBookmark').getAttribute('aria-pressed'),'true');
    });
    await check('Bookmark reset clears stars, retains history and shows empty state',async()=>{
      await select('__BOOKMARKED__'); await page.click('#btnPass'); await page.click('#btnRestart');
      const before=await hist(); await page.click('#resetBtn'); assert((await text('resetModalText')).includes('Lịch sử T/F được giữ lại'));
      await page.click('#resetConfirm'); await visible('emptyBookmarkState'); assert.deepEqual(await hist(),before);
      assert.equal(await page.locator('.bookmark-count-badge').first().textContent(),'0');
    });
    await check('Hard reset clears only hard histories',async()=>{
      await reset(); for(let i=0;i<5;i++){await select('U1');await page.click('#btnFlip');}
      await select('U2'); await page.click('#btnPass'); await select('__HARD_WORDS__');
      await page.click('#resetBtn'); await page.click('#resetConfirm'); await visible('emptyHardState');
      assert.deepEqual(await hist(),{[vocab[25].id]:['T']});
    });
    await check('Duplicate spellings have independent histories',async()=>{
      const group=vocab.filter(v=>v.word===vocab.find((v,i)=>vocab.findIndex(w=>w.word===v.word)!==i).word);
      await reset();
      await page.evaluate(ids=>{ids.forEach((id,i)=>addR(VOCAB.find(v=>v.id===id),i?'F':'T'));},group.map(v=>v.id));
      assert.deepEqual((await hist())[group[0].id],['T']); assert.deepEqual((await hist())[group[1].id],['F']);
    });
    await check('Invalid JSON storage recovers and HSK4 keys are untouched',async()=>{
      await page.evaluate(([h,b])=>{localStorage.setItem(h,'broken');localStorage.setItem(b,'broken');localStorage.setItem('hsk4_fc_hist','original');},[H,B]);
      await page.reload(); await select('U1'); await page.click('#btnPass');
      assert.deepEqual((await hist())[vocab[0].id],['T']);
      assert.equal(await page.evaluate(()=>localStorage.getItem('hsk4_fc_hist')),'original');
    });
    await check('Progress dots and welcome statistics reflect saved results',async()=>{
      await reset(); await select('U1'); await page.click('#btnPass');
      assert(await page.locator('#sidebarContent [data-unit="U1"] .progress-dot').evaluate(e=>e.classList.contains('partial')));
      for(let i=1;i<25;i++)await page.click('#btnPass');
      assert(await page.locator('#sidebarContent [data-unit="U1"] .progress-dot').evaluate(e=>e.classList.contains('done')));
      await page.reload(); assert.equal(await text('totalReviewed'),'25'); assert.equal(await text('totalPassRate'),'100%');
    });
    fs.mkdirSync('test-results',{recursive:true});
    await check('Desktop, tablet, mobile layouts and long vocabulary',async()=>{
      for(const [label,width,height] of [['desktop',1280,900],['tablet',820,1180],['mobile',390,844],['small-mobile',320,640]]){
        await page.setViewportSize({width,height});
        if(width<=700) {
          await page.click('#mobileMenuBtn'); await visible('drawerOverlay');
          await page.locator('#drawerContent [data-unit="U20"]').click();
          assert.equal(await page.locator('#drawerOverlay').isVisible(),false);
        }else await select('U20');
        await page.click('#btnFlip');
        assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
        await page.screenshot({path:`test-results/${label}.png`,fullPage:true});
      }
      await page.click('#mobileMenuBtn'); await page.click('#drawerResetBtn'); await visible('resetModal');
      await page.click('#resetCancel'); await page.click('#mobileMenuBtn'); await page.click('#drawerClose');
      assert.equal(await page.locator('#drawerOverlay').isVisible(),false);
    });
    await check('Longest text and 80 history markers do not overlap controls',async()=>{
      await page.setViewportSize({width:390,height:844});
      await page.evaluate(()=>{const v=VOCAB.reduce((a,b)=>a.word.length>b.word.length?a:b);selectUnit(v.unit);curIdx=curWords.indexOf(v);const h={};h[wk(v)]=Array(80).fill('F');saveH(h);showCard();doFlip();});
      assert(await page.evaluate(()=>document.documentElement.scrollWidth<=innerWidth));
      assert.equal(await page.locator('.history-tags .tag').count(),81);
      const tags=await page.locator('#historyTags').boundingBox(),actions=await page.locator('#actionsRevealed').boundingBox();
      assert(tags.y+tags.height<=actions.y);
      await page.screenshot({path:'test-results/long-word-history.png',fullPage:true});
    });
    await check('No JavaScript runtime errors',async()=>assert.deepEqual(errors,[]));
  } finally {
    fs.mkdirSync('test-results',{recursive:true});
    fs.writeFileSync('test-results/report.json',JSON.stringify({target:base,browser:process.env.TEST_BROWSER||'chrome',results,errors},null,2));
    await browser.close(); server.close();
  }
  console.log(`${results.filter(r=>r.status==='PASS').length}/${results.length} checks passed`);
  if(results.some(r=>r.status==='FAIL'))process.exitCode=1;
})().catch(e=>{console.error(e);server.close();process.exitCode=1;});
