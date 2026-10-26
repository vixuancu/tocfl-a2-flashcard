# -*- coding: utf-8 -*-
import json

with open('a2_vocab.json', 'r', encoding='utf-8') as f:
    vocab_js = f.read().strip()

CSS = """
:root {
  --bg-page: #f5f5f0;
  --bg-card: #ffffff;
  --bg-sidebar: #ffffff;
  --bg-unit-btn-hover: #e5e5df;
  --bg-unit-btn-active: #1a1a1a;
  --fg-primary: #1a1a1a;
  --fg-secondary: #6b6b60;
  --fg-muted: #9b9b90;
  --fg-on-dark: #ffffff;
  --fg-pinyin: #5a7a5a;
  --fg-meaning: #3a3a35;
  --color-pass: #2d8a4e;
  --color-fail: #c93c37;
  --color-pass-tag-bg: #d4edda;
  --color-fail-tag-bg: #f8d7da;
  --color-reset: #8b6914;
  --color-reset-bg: #fff8e1;
  --color-hard: #b83227;
  --color-hard-bg: #fdf0ed;
  --color-bookmark: #d97706;
  --color-bookmark-bg: #fffbeb;
  --color-bookmark-border: #fde68a;
  --color-bookmark-filled: #f59e0b;
  --color-border: #e0e0d8;
  --color-border-light: #ececec;
  --color-progress-bg: #e8e8e2;
  --color-progress-fill: #1a1a1a;
  --shadow-card: 0 1px 3px rgba(0,0,0,0.06), 0 1px 2px rgba(0,0,0,0.04);
  --shadow-card-hover: 0 4px 12px rgba(0,0,0,0.08);
  --shadow-btn: 0 1px 2px rgba(0,0,0,0.05);
  --font-ui: 'Inter', 'Segoe UI', system-ui, sans-serif;
  --font-chinese: 'Noto Sans TC', 'PingFang TC', 'Microsoft JhengHei', sans-serif;
  --sp-1: 4px; --sp-2: 8px; --sp-3: 12px; --sp-4: 16px; --sp-5: 20px;
  --sp-6: 24px; --sp-8: 32px; --sp-10: 40px; --sp-12: 48px;
  --radius-sm: 6px; --radius-md: 10px; --radius-lg: 14px; --radius-xl: 20px;
}
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }
body {
  font-family: var(--font-ui); background: var(--bg-page);
  color: var(--fg-primary); min-height: 100vh;
  -webkit-font-smoothing: antialiased;
}

/* ===== DESKTOP LAYOUT ===== */
.app { display: flex; min-height: 100vh; }

/* SIDEBAR */
.sidebar {
  width: 280px; min-width: 280px; background: var(--bg-sidebar);
  border-right: 1px solid var(--color-border); padding: var(--sp-6);
  overflow-y: auto; height: 100vh; position: sticky; top: 0;
}
.sidebar-title {
  font-size: 15px; font-weight: 700; letter-spacing: 0.02em;
  color: var(--fg-primary); margin-bottom: var(--sp-6);
  padding-bottom: var(--sp-3); border-bottom: 2px solid var(--fg-primary);
}
.sidebar-group { margin-bottom: var(--sp-5); }
.sidebar-group-label {
  font-size: 11px; font-weight: 700; text-transform: uppercase;
  letter-spacing: 0.1em; color: var(--fg-muted);
  margin-bottom: var(--sp-2); padding-left: var(--sp-1);
}
.sidebar-group-special .sidebar-group-label {
  color: var(--color-hard);
}
.unit-list { display: flex; flex-direction: column; gap: var(--sp-1); }
.unit-btn {
  display: flex; align-items: center; justify-content: space-between;
  padding: var(--sp-2) var(--sp-3); border: none; background: transparent;
  border-radius: var(--radius-sm); cursor: pointer;
  font-family: var(--font-ui); font-size: 14px; font-weight: 500;
  color: var(--fg-primary); transition: background 0.15s, color 0.15s; text-align: left;
  min-height: 44px;
}
.unit-btn:hover { background: var(--bg-unit-btn-hover); }
.unit-btn.active { background: var(--bg-unit-btn-active); color: var(--fg-on-dark); }
.unit-btn .count { font-size: 12px; font-weight: 400; color: var(--fg-muted); min-width: 28px; text-align: right; }
.unit-btn.active .count { color: rgba(255,255,255,0.6); }
.unit-btn-hard {
  border: 1px solid #ffd8d2;
  background: var(--color-hard-bg);
  color: var(--color-hard);
  font-weight: 600;
}
.unit-btn-hard:hover { background: #ffe4df; }
.unit-btn-hard.active {
  background: var(--color-hard);
  color: #fff;
  border-color: var(--color-hard);
}
.unit-btn-hard .count { color: var(--color-hard); font-weight: 700; }
.unit-btn-hard.active .count { color: #fff; }
.unit-btn-bookmark {
  border: 1px solid var(--color-bookmark-border);
  background: var(--color-bookmark-bg);
  color: var(--color-bookmark);
  font-weight: 600;
}
.unit-btn-bookmark:hover { background: #fef3c7; }
.unit-btn-bookmark.active {
  background: var(--color-bookmark);
  color: #fff;
  border-color: var(--color-bookmark);
}
.unit-btn-bookmark .count { color: var(--color-bookmark); font-weight: 700; }
.unit-btn-bookmark.active .count { color: #fff; }

.progress-dot { width: 8px; height: 8px; border-radius: 50%; margin-right: var(--sp-2); flex-shrink: 0; }
.progress-dot.none { background: var(--color-border); }
.progress-dot.partial { background: #e6a817; }
.progress-dot.done { background: var(--color-pass); }
.progress-dot.hard { background: var(--color-hard); }
.progress-dot.bookmark { background: var(--color-bookmark-filled); }

.sidebar-reset {
  margin-top: var(--sp-6); padding-top: var(--sp-4);
  border-top: 1px solid var(--color-border);
}
.reset-btn {
  display: flex; align-items: center; gap: var(--sp-2);
  padding: var(--sp-2) var(--sp-3); border: 1px solid var(--color-border);
  background: var(--bg-card); border-radius: var(--radius-sm); cursor: pointer;
  font-family: var(--font-ui); font-size: 13px; font-weight: 500;
  color: var(--color-reset); transition: all 0.15s; width: 100%;
}
.reset-btn:hover { background: var(--color-reset-bg); border-color: var(--color-reset); }

/* MOBILE TOPBAR (hidden on desktop) */
.mobile-topbar {
  display: none;
  position: sticky; top: 0; z-index: 50;
  background: var(--bg-sidebar);
  border-bottom: 1px solid var(--color-border);
  padding: var(--sp-3) var(--sp-4);
  align-items: center; justify-content: space-between;
}
.mobile-topbar-title {
  font-size: 15px; font-weight: 700; color: var(--fg-primary);
}
.mobile-menu-btn {
  display: flex; align-items: center; gap: var(--sp-2);
  padding: var(--sp-2) var(--sp-3); border: 1px solid var(--color-border);
  background: var(--bg-card); border-radius: var(--radius-sm); cursor: pointer;
  font-family: var(--font-ui); font-size: 13px; font-weight: 600;
  color: var(--fg-primary);
}
.mobile-menu-btn:hover { background: var(--bg-unit-btn-hover); }
.mobile-current-unit {
  font-size: 13px; font-weight: 600; color: var(--fg-secondary);
}

/* Mobile drawer overlay */
.drawer-overlay {
  display: none; position: fixed; inset: 0;
  background: rgba(0,0,0,0.3); z-index: 200;
}
.drawer-overlay.active { display: block; }
.drawer {
  position: fixed; top: 0; left: 0; bottom: 0;
  width: 300px; max-width: 85vw; background: var(--bg-sidebar);
  z-index: 201; overflow-y: auto; padding: var(--sp-6);
  transform: translateX(-100%); transition: transform 0.25s ease;
}
.drawer-overlay.active .drawer { transform: translateX(0); }
.drawer-close {
  position: absolute; top: var(--sp-3); right: var(--sp-3);
  width: 36px; height: 36px; border: none; background: transparent;
  cursor: pointer; font-size: 20px; color: var(--fg-muted);
  border-radius: var(--radius-sm); display: flex; align-items: center;
  justify-content: center;
}
.drawer-close:hover { background: var(--bg-unit-btn-hover); }

/* MAIN */
.main {
  flex: 1; display: flex; flex-direction: column; align-items: center;
  padding: var(--sp-10) var(--sp-8); min-height: 100vh;
}
.welcome {
  display: flex; flex-direction: column; align-items: center;
  justify-content: center; flex: 1; text-align: center; max-width: 480px;
}
.welcome h1 { font-size: 28px; font-weight: 700; margin-bottom: var(--sp-3); letter-spacing: -0.01em; }
.welcome p { font-size: 16px; color: var(--fg-secondary); line-height: 1.6; }
.welcome .stat-row { display: flex; gap: var(--sp-6); margin-top: var(--sp-8); }
.welcome .stat-box { text-align: center; }
.welcome .stat-num { font-size: 32px; font-weight: 700; color: var(--fg-primary); }
.welcome .stat-label { font-size: 13px; color: var(--fg-muted); margin-top: var(--sp-1); }
.study-view {
  width: 100%; max-width: 680px; display: none;
  flex-direction: column; align-items: center;
}
.study-view.active { display: flex; }
.study-header {
  width: 100%; display: flex; align-items: center;
  justify-content: space-between; margin-bottom: var(--sp-8);
}
.study-unit-name { font-size: 18px; font-weight: 700; color: var(--fg-primary); }
.study-progress-text {
  font-size: 14px; color: var(--fg-secondary); font-weight: 500; font-variant-numeric: tabular-nums;
}
.progress-bar {
  width: 100%; height: 4px; background: var(--color-progress-bg);
  border-radius: 2px; margin-bottom: var(--sp-10); overflow: hidden;
}
.progress-fill {
  height: 100%; background: var(--color-progress-fill);
  border-radius: 2px; transition: width 0.3s ease;
}

/* FLASHCARD */
.flashcard {
  width: 100%; min-height: 340px;
  background: var(--bg-card); border-radius: var(--radius-xl);
  box-shadow: var(--shadow-card); display: flex; flex-direction: column;
  align-items: center; justify-content: center;
  padding: var(--sp-12) var(--sp-8); position: relative;
  transition: box-shadow 0.2s; border: 1px solid var(--color-border-light);
  margin-bottom: var(--sp-8);
}
.flashcard:hover { box-shadow: var(--shadow-card-hover); }
.flashcard .word-index {
  position: absolute; top: var(--sp-5); left: var(--sp-6);
  font-size: 13px; font-weight: 600; color: var(--fg-muted); font-variant-numeric: tabular-nums;
  display: flex; align-items: center; gap: 6px;
}
.flashcard .unit-badge {
  background: #f0f0eb; color: var(--fg-secondary);
  padding: 2px 6px; border-radius: 4px; font-size: 11px; font-weight: 700;
}
.flashcard .hanzi {
  font-family: var(--font-chinese); font-size: 80px; font-weight: 400;
  color: var(--fg-primary); line-height: 1.2; text-align: center;
  letter-spacing: 0.04em; user-select: none; overflow-wrap: anywhere; max-width: 100%;
}
.flashcard .reveal-area {
  display: none; flex-direction: column; align-items: center;
  gap: var(--sp-3); margin-top: var(--sp-6); padding-top: var(--sp-6);
  border-top: 1px solid var(--color-border-light); width: 100%;
}
.flashcard.revealed .reveal-area { display: flex; }
.flashcard .pinyin { font-size: 26px; font-weight: 500; color: var(--fg-pinyin); letter-spacing: 0.02em; }
.flashcard .meaning { font-size: 24px; font-weight: 600; color: var(--fg-meaning); text-align: center; line-height: 1.4; overflow-wrap: anywhere; max-width: 100%; }
.flashcard .history-tags {
  position: static; margin-top: var(--sp-5); width: 100%;
  display: flex; flex-wrap: wrap; gap: 3px; justify-content: center;
}
.tag {
  display: inline-flex; align-items: center; justify-content: center;
  width: 24px; height: 24px; border-radius: 4px;
  font-size: 12px; font-weight: 700; font-family: var(--font-ui); line-height: 1;
}
.tag-t { background: var(--color-pass-tag-bg); color: var(--color-pass); }
.tag-f { background: var(--color-fail-tag-bg); color: var(--color-fail); }

/* BOOKMARK BUTTON on Flashcard */
.bookmark-btn {
  position: absolute; top: var(--sp-5); right: var(--sp-6);
  width: 44px; height: 44px;
  display: flex; align-items: center; justify-content: center;
  border: none; background: transparent; cursor: pointer;
  border-radius: var(--radius-sm);
  color: var(--fg-muted);
  transition: color 0.2s, transform 0.15s, background 0.15s;
}
.bookmark-btn:hover { background: var(--color-bookmark-bg); color: var(--color-bookmark); transform: scale(1.1); }
.bookmark-btn.bookmarked { color: var(--color-bookmark-filled); }
.bookmark-btn.bookmarked svg path { fill: var(--color-bookmark-filled); stroke: var(--color-bookmark-filled); }
.bookmark-btn.bookmarked:hover { color: var(--color-bookmark); }
.bookmark-btn:active { transform: scale(0.9); }
.bookmark-btn:focus-visible { outline: 2px solid var(--color-bookmark); outline-offset: 2px; }

/* BUTTONS */
.actions { display: flex; gap: var(--sp-4); width: 100%; max-width: 480px; }
.actions.hidden { display: none; }
.btn {
  flex: 1; padding: var(--sp-4) var(--sp-6); border: none;
  border-radius: var(--radius-md); font-family: var(--font-ui);
  font-size: 18px; font-weight: 600; cursor: pointer;
  transition: all 0.15s; box-shadow: var(--shadow-btn); letter-spacing: 0.01em;
}
.btn:active { transform: scale(0.97); }
.btn-pass { background: var(--color-pass); color: white; }
.btn-pass:hover { background: #248b42; }
.btn-flip { background: var(--bg-card); color: var(--fg-primary); border: 1px solid var(--color-border); }
.btn-flip:hover { background: var(--bg-unit-btn-hover); }
.btn-fail-next { background: var(--color-fail); color: white; }
.btn-fail-next:hover { background: #b33530; }
.kb-hint { margin-top: var(--sp-4); font-size: 13px; color: var(--fg-muted); text-align: center; }
.kb-hint kbd {
  display: inline-block; padding: 2px 7px; background: #eee;
  border: 1px solid var(--color-border); border-radius: 4px;
  font-family: var(--font-ui); font-size: 12px; font-weight: 600; color: var(--fg-secondary);
}

/* SESSION COMPLETE */
.session-complete {
  display: none; flex-direction: column; align-items: center; text-align: center;
  padding: var(--sp-12) var(--sp-8); background: var(--bg-card);
  border-radius: var(--radius-xl); box-shadow: var(--shadow-card);
  border: 1px solid var(--color-border-light); width: 100%; max-width: 480px;
}
.session-complete.active { display: flex; }
.session-complete h2 { font-size: 24px; font-weight: 700; margin-bottom: var(--sp-6); }
.session-stats { display: flex; gap: var(--sp-8); margin-bottom: var(--sp-6); }
.session-stat { text-align: center; }
.session-stat .num { font-size: 36px; font-weight: 700; }
.session-stat .num.pass { color: var(--color-pass); }
.session-stat .num.fail { color: var(--color-fail); }
.session-stat .label { font-size: 13px; color: var(--fg-muted); margin-top: var(--sp-1); }
.btn-restart {
  margin-top: var(--sp-6); padding: var(--sp-3) var(--sp-8);
  background: var(--fg-primary); color: var(--fg-on-dark); border: none;
  border-radius: var(--radius-md); font-family: var(--font-ui);
  font-size: 15px; font-weight: 600; cursor: pointer; transition: opacity 0.15s;
}
.btn-restart:hover { opacity: 0.85; }

/* EMPTY HARD WORDS VIEW */
.empty-state {
  display: none; flex-direction: column; align-items: center; text-align: center;
  padding: var(--sp-12) var(--sp-8); background: var(--bg-card);
  border-radius: var(--radius-xl); box-shadow: var(--shadow-card);
  border: 1px solid var(--color-border-light); width: 100%; max-width: 480px;
}
.empty-state.active { display: flex; }
.empty-state h2 { font-size: 22px; font-weight: 700; margin-bottom: var(--sp-3); color: var(--color-pass); }
.empty-state p { font-size: 15px; color: var(--fg-secondary); line-height: 1.6; margin-bottom: var(--sp-6); }

/* MODAL */
.modal-overlay {
  display: none; position: fixed; inset: 0;
  background: rgba(0,0,0,0.35); z-index: 100;
  align-items: center; justify-content: center;
}
.modal-overlay.active { display: flex; }
.modal {
  background: var(--bg-card); border-radius: var(--radius-lg);
  padding: var(--sp-8); max-width: 400px; width: 90%;
  box-shadow: 0 20px 60px rgba(0,0,0,0.15);
}
.modal h3 { font-size: 18px; font-weight: 700; margin-bottom: var(--sp-4); }
.modal p { font-size: 14px; color: var(--fg-secondary); margin-bottom: var(--sp-6); line-height: 1.5; }
.modal-actions { display: flex; gap: var(--sp-3); justify-content: flex-end; }
.modal-btn {
  padding: var(--sp-2) var(--sp-5); border: 1px solid var(--color-border);
  background: var(--bg-card); border-radius: var(--radius-sm);
  font-family: var(--font-ui); font-size: 14px; font-weight: 500; cursor: pointer; transition: all 0.15s;
}
.modal-btn:hover { background: var(--bg-unit-btn-hover); }
.modal-btn.danger { background: var(--color-fail); color: white; border-color: var(--color-fail); }
.modal-btn.danger:hover { background: #b33530; }

/* ===== RESPONSIVE: TABLET ===== */
@media (max-width: 900px) {
  .sidebar { width: 240px; min-width: 240px; padding: var(--sp-4); }
}

/* ===== RESPONSIVE: MOBILE ===== */
@media (max-width: 700px) {
  .sidebar { display: none; }
  .mobile-topbar { display: flex; }
  .app { flex-direction: column; }
  .main {
    padding: var(--sp-5) var(--sp-4);
    min-height: calc(100vh - 52px);
  }
  .study-header { margin-bottom: var(--sp-4); }
  .progress-bar { margin-bottom: var(--sp-5); }
  .flashcard {
    min-height: 280px;
    padding: var(--sp-10) var(--sp-5);
    border-radius: var(--radius-lg);
    margin-bottom: var(--sp-5);
  }
  .flashcard .hanzi { font-size: 60px; }
  .flashcard .pinyin { font-size: 22px; }
  .flashcard .meaning { font-size: 20px; }
  .btn { font-size: 17px; padding: 14px var(--sp-5); }
  .kb-hint { display: none; }
  .welcome h1 { font-size: 24px; }
  .welcome p { font-size: 14px; }
  .welcome .stat-num { font-size: 28px; }
  .session-complete { padding: var(--sp-8) var(--sp-5); }
  .bookmark-btn { width: 48px; height: 48px; top: var(--sp-3); right: var(--sp-3); }
}

button:focus-visible { outline: 2px solid var(--fg-primary); outline-offset: 2px; }
.sidebar::-webkit-scrollbar { width: 6px; }
.sidebar::-webkit-scrollbar-track { background: transparent; }
.sidebar::-webkit-scrollbar-thumb { background: var(--color-border); border-radius: 3px; }
"""

JS = """
const VOCAB = __VOCAB_DATA__;
const unitOrder = [];
const unitMap = {};
VOCAB.forEach(v => {
  if (!unitMap[v.unit]) { unitMap[v.unit] = []; unitOrder.push(v.unit); }
  unitMap[v.unit].push(v);
});
function categorize(unit) {
  if (/^U\\d/.test(unit)) return 'Unit';
  if (unit.includes('HB')) return 'Hanban';
  if (unit.includes('XL')) return 'Luy\\u1ec7n \\u0111\\u1ec1';
  return 'Kh\\u00e1c';
}
const categories = {};
unitOrder.forEach(u => {
  const cat = categorize(u);
  if (!categories[cat]) categories[cat] = [];
  categories[cat].push(u);
});
function naturalSort(a, b) {
  const na = parseInt(a.replace(/\\D/g, '')) || 0;
  const nb = parseInt(b.replace(/\\D/g, '')) || 0;
  return na - nb;
}
Object.values(categories).forEach(arr => arr.sort(naturalSort));

const SK = 'tocfl_a2_fc_hist';
const HARD_UNIT_KEY = '__HARD_WORDS__';
const BM_KEY = 'tocfl_a2_fc_bookmarks';
const BOOKMARK_UNIT_KEY = '__BOOKMARKED__';

function loadH() { try { return JSON.parse(localStorage.getItem(SK)) || {}; } catch { return {}; } }
function saveH(h) { localStorage.setItem(SK, JSON.stringify(h)); }
function wk(v) { return v.id; }
function getWH(v) { return loadH()[wk(v)] || []; }
function addR(v, r) { const h = loadH(); const k = wk(v); if (!h[k]) h[k] = []; h[k].push(r); saveH(h); }

// Bookmark helpers
function loadBM() { try { return JSON.parse(localStorage.getItem(BM_KEY)) || {}; } catch { return {}; } }
function saveBM(bm) { localStorage.setItem(BM_KEY, JSON.stringify(bm)); }
function isBM(v) { return !!loadBM()[wk(v)]; }
function toggleBM(v) { const bm = loadBM(); if (bm[wk(v)]) delete bm[wk(v)]; else bm[wk(v)] = true; saveBM(bm); }
function getBookmarkedWords() { const bm = loadBM(); return VOCAB.filter(v => bm[wk(v)]); }
function updateBookmarkBtn(v) {
  const btn = document.getElementById('btnBookmark');
  if (!btn || !v) return;
  const marked = isBM(v);
  btn.classList.toggle('bookmarked', marked);
  btn.setAttribute('aria-pressed', String(marked));
  btn.setAttribute('title', marked ? '\\u0110\\u00e3 \\u0111\\u00e1nh d\\u1ea5u (B \\u0111\\u1ec3 b\\u1ecf)' : '\\u0110\\u00e1nh d\\u1ea5u t\\u1eeb n\\u00e0y (B)');
}

function resetU(unit) {
  if (unit === BOOKMARK_UNIT_KEY) {
    // Reset chỉ xóa bookmark flags, KHÔNG xóa lịch sử T/F
    saveBM({});
  } else {
    const h = loadH();
    if (unit === HARD_UNIT_KEY) {
      getHardWords().forEach(v => { delete h[wk(v)]; });
    } else {
      (unitMap[unit] || []).forEach(v => { delete h[wk(v)]; });
    }
    saveH(h);
  }
}

// Calculate Hard Words (F >= 5 from historical data)
function getHardWords() {
  const h = loadH();
  const hardList = [];
  VOCAB.forEach(v => {
    const hist = h[wk(v)] || [];
    const fCount = hist.filter(r => r === 'F').length;
    if (fCount >= 5) {
      hardList.push(v);
    }
  });
  return hardList;
}

let curUnit = null, curWords = [], curIdx = 0, sPass = 0, sFail = 0, revealed = false;

// Build sidebar content into a container
function buildUnitList(container) {
  container.innerHTML = '';

  // 1. Special Group: TỪ CỨNG ĐẦU (F >= 5)
  const specGroup = document.createElement('div');
  specGroup.className = 'sidebar-group sidebar-group-special';
  const specLabel = document.createElement('div');
  specLabel.className = 'sidebar-group-label';
  specLabel.textContent = '\\u0110\\u1eb7c bi\\u1ec7t';
  specGroup.appendChild(specLabel);

  const specList = document.createElement('div');
  specList.className = 'unit-list';

  const hardBtn = document.createElement('button');
  hardBtn.className = 'unit-btn unit-btn-hard';
  hardBtn.dataset.unit = HARD_UNIT_KEY;

  const hardDot = document.createElement('span');
  hardDot.className = 'progress-dot hard';

  const hardNm = document.createElement('span');
  hardNm.textContent = '\\ud83d\\udd25 T\\u1eeb c\\u1ee9ng \\u0111\\u1ea7u (F \\u2265 5)';
  hardNm.style.flex = '1';

  const hardCnt = document.createElement('span');
  hardCnt.className = 'count hard-count-badge';
  hardCnt.textContent = getHardWords().length;

  hardBtn.appendChild(hardDot);
  hardBtn.appendChild(hardNm);
  hardBtn.appendChild(hardCnt);
  hardBtn.addEventListener('click', () => {
    selectHardWords();
    document.getElementById('drawerOverlay').classList.remove('active');
  });
  specList.appendChild(hardBtn);

  // Nút ⭐ Đã đánh dấu (Bookmark)
  const bmBtn = document.createElement('button');
  bmBtn.className = 'unit-btn unit-btn-bookmark';
  bmBtn.dataset.unit = BOOKMARK_UNIT_KEY;

  const bmDot = document.createElement('span');
  bmDot.className = 'progress-dot bookmark';

  const bmNm = document.createElement('span');
  bmNm.textContent = '\\u2b50 \\u0110\\u00e3 \\u0111\\u00e1nh d\\u1ea5u';
  bmNm.style.flex = '1';

  const bmCnt = document.createElement('span');
  bmCnt.className = 'count bookmark-count-badge';
  bmCnt.textContent = getBookmarkedWords().length;

  bmBtn.appendChild(bmDot);
  bmBtn.appendChild(bmNm);
  bmBtn.appendChild(bmCnt);
  bmBtn.addEventListener('click', () => {
    selectBookmarkWords();
    document.getElementById('drawerOverlay').classList.remove('active');
  });
  specList.appendChild(bmBtn);

  specGroup.appendChild(specList);
  container.appendChild(specGroup);

  // 2. Regular Categories: Unit, Hanban, Đề luyện, Khác
  const catOrder = ['Unit', 'Hanban', 'Luy\\u1ec7n \\u0111\\u1ec1', 'Kh\\u00e1c'];
  catOrder.forEach(cat => {
    const units = categories[cat];
    if (!units || !units.length) return;
    const g = document.createElement('div');
    g.className = 'sidebar-group';
    const l = document.createElement('div');
    l.className = 'sidebar-group-label';
    l.textContent = cat;
    g.appendChild(l);
    const list = document.createElement('div');
    list.className = 'unit-list';
    units.forEach(u => {
      const btn = document.createElement('button');
      btn.className = 'unit-btn';
      btn.dataset.unit = u;
      const dot = document.createElement('span');
      dot.className = 'progress-dot';
      const p = unitProg(u);
      dot.classList.add(p === 0 ? 'none' : p < 1 ? 'partial' : 'done');
      const nm = document.createElement('span');
      nm.textContent = u;
      nm.style.flex = '1';
      const cnt = document.createElement('span');
      cnt.className = 'count';
      cnt.textContent = unitMap[u].length;
      btn.appendChild(dot);
      btn.appendChild(nm);
      btn.appendChild(cnt);
      btn.addEventListener('click', () => {
        selectUnit(u);
        document.getElementById('drawerOverlay').classList.remove('active');
      });
      list.appendChild(btn);
    });
    g.appendChild(list);
    container.appendChild(g);
  });
}

function unitProg(unit) {
  const ws = unitMap[unit] || [];
  if (!ws.length) return 0;
  const h = loadH();
  let r = 0;
  ws.forEach(v => { if ((h[wk(v)] || []).length > 0) r++; });
  return r / ws.length;
}

function updAllActive() {
  document.querySelectorAll('.unit-btn').forEach(btn => {
    btn.classList.toggle('active', btn.dataset.unit === curUnit);
    if (btn.dataset.unit !== HARD_UNIT_KEY && btn.dataset.unit !== BOOKMARK_UNIT_KEY) {
      const dot = btn.querySelector('.progress-dot');
      const p = unitProg(btn.dataset.unit);
      dot.className = 'progress-dot ' + (p === 0 ? 'none' : p < 1 ? 'partial' : 'done');
    }
  });

  // Update hard words count badge
  const hardCount = getHardWords().length;
  document.querySelectorAll('.hard-count-badge').forEach(badge => {
    badge.textContent = hardCount;
  });

  // Update bookmark count badge
  const bmCount = getBookmarkedWords().length;
  document.querySelectorAll('.bookmark-count-badge').forEach(badge => {
    badge.textContent = bmCount;
  });

  // Update mobile topbar
  const mcu = document.getElementById('mobileCurrentUnit');
  if (mcu) {
    if (curUnit === HARD_UNIT_KEY) mcu.textContent = '\\ud83d\\udd25 C\\u1ee9ng \\u0111\\u1ea7u (' + hardCount + ')';
    else if (curUnit === BOOKMARK_UNIT_KEY) mcu.textContent = '\\u2b50 \\u0110\\u00e3 \\u0111\\u00e1nh d\\u1ea5u (' + bmCount + ')';
    else mcu.textContent = curUnit || '';
  }
}

function selectHardWords() {
  curUnit = HARD_UNIT_KEY;
  curWords = getHardWords();
  curIdx = 0; sPass = 0; sFail = 0; revealed = false;
  updAllActive();

  document.getElementById('welcomeView').style.display = 'none';
  document.getElementById('sessionComplete').classList.remove('active');
  document.getElementById('emptyBookmarkState').classList.remove('active');

  if (curWords.length === 0) {
    document.getElementById('studyView').classList.remove('active');
    document.getElementById('emptyHardState').classList.add('active');
  } else {
    document.getElementById('emptyHardState').classList.remove('active');
    document.getElementById('studyView').classList.add('active');
    document.getElementById('studyUnitName').textContent = '\\ud83d\\udd25 T\\u1eeb c\\u1ee9ng \\u0111\\u1ea7u (F \\u2265 5)';
    showCard();
  }
}

function selectBookmarkWords() {
  curUnit = BOOKMARK_UNIT_KEY;
  curWords = getBookmarkedWords();
  curIdx = 0; sPass = 0; sFail = 0; revealed = false;
  updAllActive();

  document.getElementById('welcomeView').style.display = 'none';
  document.getElementById('sessionComplete').classList.remove('active');
  document.getElementById('emptyHardState').classList.remove('active');

  if (curWords.length === 0) {
    document.getElementById('studyView').classList.remove('active');
    document.getElementById('emptyBookmarkState').classList.add('active');
  } else {
    document.getElementById('emptyBookmarkState').classList.remove('active');
    document.getElementById('studyView').classList.add('active');
    document.getElementById('studyUnitName').textContent = '\\u2b50 \\u0110\\u00e3 \\u0111\\u00e1nh d\\u1ea5u';
    showCard();
  }
}

function selectUnit(unit) {
  curUnit = unit; curWords = unitMap[unit] || [];
  curIdx = 0; sPass = 0; sFail = 0; revealed = false;
  updAllActive();
  document.getElementById('welcomeView').style.display = 'none';
  document.getElementById('emptyHardState').classList.remove('active');
  document.getElementById('emptyBookmarkState').classList.remove('active');
  document.getElementById('studyView').classList.add('active');
  document.getElementById('sessionComplete').classList.remove('active');
  document.getElementById('studyUnitName').textContent = curUnit;
  showCard();
}

function showCard() {
  if (curIdx >= curWords.length) { showDone(); return; }
  const v = curWords[curIdx];
  revealed = false;
  document.getElementById('flashcard').classList.remove('revealed');
  document.getElementById('hanzi').textContent = v.word;
  document.getElementById('pinyin').textContent = v.pinyin;
  document.getElementById('meaning').textContent = v.meaning;

  // Show unit badge if inside Hard Words or Bookmark mode
  const indexEl = document.getElementById('wordIndex');
  if (curUnit === HARD_UNIT_KEY || curUnit === BOOKMARK_UNIT_KEY) {
    indexEl.innerHTML = '<span class="unit-badge">' + v.unit + '</span> ' + (curIdx + 1) + ' / ' + curWords.length;
  } else {
    indexEl.textContent = (curIdx + 1) + ' / ' + curWords.length;
  }

  const pct = (curIdx / curWords.length) * 100;
  document.getElementById('progressFill').style.width = pct + '%';
  document.getElementById('studyProgressText').textContent = curIdx + ' / ' + curWords.length;
  renderTags(v);
  updateBookmarkBtn(v);
  document.getElementById('actionsDefault').classList.remove('hidden');
  document.getElementById('actionsRevealed').classList.add('hidden');
}

function renderTags(v) {
  const c = document.getElementById('historyTags');
  c.innerHTML = '';
  getWH(v).forEach(r => {
    const t = document.createElement('span');
    t.className = 'tag ' + (r === 'T' ? 'tag-t' : 'tag-f');
    t.textContent = r;
    c.appendChild(t);
  });
}

function doPass() {
  if (revealed || curIdx >= curWords.length) return;
  addR(curWords[curIdx], 'T'); sPass++; curIdx++;
  updAllActive();
  showCard();
}
function doFlip() {
  if (revealed || curIdx >= curWords.length) return;
  revealed = true;
  document.getElementById('flashcard').classList.add('revealed');
  document.getElementById('actionsDefault').classList.add('hidden');
  document.getElementById('actionsRevealed').classList.remove('hidden');
  addR(curWords[curIdx], 'F'); sFail++;
  renderTags(curWords[curIdx]);
  updAllActive();
}
function doNext() { if (!revealed || curIdx >= curWords.length) return; curIdx++; showCard(); }

function showDone() {
  document.getElementById('studyView').classList.remove('active');
  document.getElementById('sessionComplete').classList.add('active');
  document.getElementById('sessionPass').textContent = sPass;
  document.getElementById('sessionFail').textContent = sFail;
  const total = sPass + sFail;
  const pct = total > 0 ? Math.round((sPass / total) * 100) : 0;
  let msg = pct >= 90 ? 'Tuy\\u1ec7t v\\u1eddi! G\\u1ea7n nh\\u1edb h\\u1ebft r\\u1ed3i.' :
            pct >= 70 ? 'Kh\\u00e1 t\\u1ed1t! C\\u1ed1 th\\u00eam ch\\u00fat n\\u1eefa.' :
            pct >= 50 ? 'C\\u1ea7n \\u00f4n l\\u1ea1i nhi\\u1ec1u h\\u01a1n.' : 'H\\u00e3y h\\u1ecdc r\\u1ed3i review l\\u1ea1i nh\\u00e9.';
  document.getElementById('sessionMsg').textContent = msg + ' (' + pct + '% nh\\u1edb)';
  document.getElementById('progressFill').style.width = '100%';
  document.getElementById('studyProgressText').textContent = curWords.length + ' / ' + curWords.length;
  updAllActive(); updStats();
}

// Reset
function openReset() {
  if (!curUnit) { alert('Chọn một mục trước.'); return; }
  document.getElementById('drawerOverlay').classList.remove('active');
  document.getElementById('resetModalText').textContent = curUnit === BOOKMARK_UNIT_KEY
    ? 'Bỏ toàn bộ dấu sao. Lịch sử T/F được giữ lại. Không thể hoàn tác.'
    : 'Xóa toàn bộ lịch sử T/F của ' + (curUnit === HARD_UNIT_KEY ? 'các từ cứng đầu' : curUnit) + '. Không thể hoàn tác.';
  document.getElementById('resetModal').classList.add('active');
}
document.getElementById('resetBtn').addEventListener('click', openReset);
document.getElementById('resetCancel').addEventListener('click', () => {
  document.getElementById('resetModal').classList.remove('active');
});
document.getElementById('resetConfirm').addEventListener('click', () => {
  resetU(curUnit);
  document.getElementById('resetModal').classList.remove('active');
  if (curUnit === HARD_UNIT_KEY) {
    selectHardWords();
  } else if (curUnit === BOOKMARK_UNIT_KEY) {
    selectBookmarkWords();
  } else {
    selectUnit(curUnit);
  }
  updStats();
});
document.getElementById('resetModal').addEventListener('click', e => {
  if (e.target === e.currentTarget) document.getElementById('resetModal').classList.remove('active');
});

document.getElementById('btnRestart').addEventListener('click', () => {
  if (curUnit === HARD_UNIT_KEY) selectHardWords();
  else if (curUnit === BOOKMARK_UNIT_KEY) selectBookmarkWords();
  else selectUnit(curUnit);
});
document.getElementById('btnPass').addEventListener('click', doPass);
document.getElementById('btnFlip').addEventListener('click', doFlip);
document.getElementById('btnFailNext').addEventListener('click', doNext);
document.getElementById('btnBookmark').addEventListener('click', () => {
  if (curIdx >= curWords.length) return;
  const v = curWords[curIdx];
  toggleBM(v);
  updateBookmarkBtn(v);
  updAllActive();
});

// Mobile drawer
document.getElementById('mobileMenuBtn').addEventListener('click', () => {
  document.getElementById('drawerOverlay').classList.add('active');
});
document.getElementById('drawerOverlay').addEventListener('click', e => {
  if (e.target === e.currentTarget) e.currentTarget.classList.remove('active');
});
document.getElementById('drawerClose').addEventListener('click', () => {
  document.getElementById('drawerOverlay').classList.remove('active');
});
// Reset from drawer
document.getElementById('drawerResetBtn').addEventListener('click', openReset);

// Keyboard
document.addEventListener('keydown', e => {
  if (e.repeat || document.getElementById('resetModal').classList.contains('active') || document.getElementById('drawerOverlay').classList.contains('active')) return;
  if (!document.getElementById('studyView').classList.contains('active')) return;
  if (curIdx >= curWords.length) return;
  if (e.key === 'ArrowRight' && !revealed) { e.preventDefault(); doPass(); }
  else if (e.key === ' ' && !revealed) { e.preventDefault(); doFlip(); }
  else if ((e.key === 'ArrowLeft' || e.key === ' ' || e.key === 'Enter') && revealed) { e.preventDefault(); doNext(); }
  else if (e.key === 'b' || e.key === 'B') {
    e.preventDefault();
    const v = curWords[curIdx];
    toggleBM(v);
    updateBookmarkBtn(v);
    updAllActive();
  }
});

function updStats() {
  const h = loadH();
  let reviewed = 0, tp = 0, ta = 0;
  Object.values(h).forEach(hist => {
    if (hist.length > 0) reviewed++;
    hist.forEach(r => { ta++; if (r === 'T') tp++; });
  });
  document.getElementById('totalWords').textContent = VOCAB.length;
  document.getElementById('totalReviewed').textContent = reviewed;
  document.getElementById('totalPassRate').textContent = ta > 0 ? Math.round((tp / ta) * 100) + '%' : '\\u2014';
}

// Init
buildUnitList(document.getElementById('sidebarContent'));
buildUnitList(document.getElementById('drawerContent'));
updStats();
""".replace('__VOCAB_DATA__', vocab_js)

HTML_BODY = """
<!-- Mobile top bar -->
<div class="mobile-topbar" id="mobileTopbar">
  <span class="mobile-topbar-title">TOCFL A2 Flashcard</span>
  <span class="mobile-current-unit" id="mobileCurrentUnit"></span>
  <button class="mobile-menu-btn" id="mobileMenuBtn">
    <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    M\u1ee5c
  </button>
</div>

<!-- Mobile drawer -->
<div class="drawer-overlay" id="drawerOverlay">
  <div class="drawer">
    <button class="drawer-close" id="drawerClose">\u00d7</button>
    <div class="sidebar-title" style="margin-top:var(--sp-2)">Ch\u1ecdn m\u1ee5c</div>
    <div id="drawerContent"></div>
    <div class="sidebar-reset">
      <button class="reset-btn" id="drawerResetBtn" title="Reset">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M2.5 2.5v4h4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M2.82 10a5.5 5.5 0 1 0 .52-5.5L2.5 6.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        Reset m\u1ee5c \u0111ang ch\u1ecdn
      </button>
    </div>
  </div>
</div>

<div class="app">
  <!-- Desktop sidebar -->
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-title">TOCFL A2 Flashcard</div>
    <div id="sidebarContent"></div>
    <div class="sidebar-reset">
      <button class="reset-btn" id="resetBtn" title="Reset">
        <svg width="16" height="16" viewBox="0 0 16 16" fill="none"><path d="M2.5 2.5v4h4" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/><path d="M2.82 10a5.5 5.5 0 1 0 .52-5.5L2.5 6.5" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></svg>
        Reset m\u1ee5c \u0111ang ch\u1ecdn
      </button>
    </div>
  </aside>

  <main class="main" id="mainArea">
    <div class="welcome" id="welcomeView">
      <h1>TOCFL A2 Flashcard</h1>
      <p>Ch\u1ecdn m\u1ed9t m\u1ee5c \u0111\u1ec3 b\u1eaft \u0111\u1ea7u \u00f4n t\u1eeb v\u1ef1ng.<br>Nh\u00ecn ch\u1eef Trung \u2014 t\u1ef1 nh\u1edb ngh\u0129a \u2014 \u0111\u00e1nh gi\u00e1 PASS hay FAIL.</p>
      <div class="stat-row">
        <div class="stat-box"><div class="stat-num" id="totalWords">500</div><div class="stat-label">T\u1ed5ng t\u1eeb</div></div>
        <div class="stat-box"><div class="stat-num" id="totalReviewed">0</div><div class="stat-label">\u0110\u00e3 review</div></div>
        <div class="stat-box"><div class="stat-num" id="totalPassRate">\u2014</div><div class="stat-label">T\u1ef7 l\u1ec7 nh\u1edb</div></div>
      </div>
    </div>

    <!-- Empty state for Hard words -->
    <div class="empty-state" id="emptyHardState">
      <h2>\u2728 Ch\u01b0a c\u00f3 t\u1eeb c\u1ee9ng \u0111\u1ea7u!</h2>
      <p>Hi\u1ec7n t\u1ea1i ch\u01b0a c\u00f3 t\u1eeb n\u00e0o b\u1ecb qu\u00ean t\u1eeb 5 l\u1ea7n tr\u1edf l\u00ean (F \u2265 5).<br>B\u1ea1n \u0111ang h\u1ecdc v\u00e0 ghi nh\u1edb r\u1ea5t t\u1ed1t!</p>
      <button class="btn-restart" onclick="document.getElementById('emptyHardState').classList.remove('active'); document.getElementById('welcomeView').style.display='flex';">Quay l\u1ea1i trang ch\u1ee7</button>
    </div>

    <!-- Empty state for Bookmark words -->
    <div class="empty-state" id="emptyBookmarkState">
      <h2>\u2b50 Ch\u01b0a c\u00f3 t\u1eeb \u0111\u00e3 \u0111\u00e1nh d\u1ea5u!</h2>
      <p>Trong khi h\u1ecdc, h\u00e3y b\u1ea5m bi\u1ec3u t\u01b0\u1ee3ng \u2b50 \u1edf g\u00f3c ph\u1ea3i th\u1ebb t\u1eeb<br>ho\u1eb7c ph\u00edm t\u1eaft <kbd style="background:#eee;border:1px solid #ccc;border-radius:3px;padding:1px 5px;font-size:13px;">B</kbd> \u0111\u1ec3 l\u01b0u t\u1eeb v\u00e0o \u0111\u00e2y.</p>
      <button class="btn-restart" onclick="document.getElementById('emptyBookmarkState').classList.remove('active'); document.getElementById('welcomeView').style.display='flex';">Quay l\u1ea1i trang ch\u1ee7</button>
    </div>

    <div class="study-view" id="studyView">
      <div class="study-header">
        <span class="study-unit-name" id="studyUnitName"></span>
        <span class="study-progress-text" id="studyProgressText"></span>
      </div>
      <div class="progress-bar"><div class="progress-fill" id="progressFill"></div></div>
      <div class="flashcard" id="flashcard">
        <div class="word-index" id="wordIndex"></div>
        <button class="bookmark-btn" id="btnBookmark" aria-pressed="false" title="\u0110\u00e1nh d\u1ea5u t\u1eeb n\u00e0y (B)" aria-label="\u0110\u00e1nh d\u1ea5u t\u1eeb n\u00e0y">
          <svg width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
            <path class="star-outline" d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"/>
          </svg>
        </button>
        <div class="hanzi" id="hanzi"></div>
        <div class="reveal-area">
          <div class="pinyin" id="pinyin"></div>
          <div class="meaning" id="meaning"></div>
        </div>
        <div class="history-tags" id="historyTags"></div>
      </div>
      <div class="actions" id="actionsDefault">
        <button class="btn btn-pass" id="btnPass">\u2713 Nh\u1edb</button>
        <button class="btn btn-flip" id="btnFlip">L\u1eadt xem</button>
      </div>
      <div class="actions hidden" id="actionsRevealed">
        <button class="btn btn-fail-next" id="btnFailNext">\u2717 Kh\u00f4ng nh\u1edb \u2014 Ti\u1ebfp</button>
      </div>
      <div class="kb-hint">
        <kbd>\u2192</kbd> Nh\u1edb &nbsp;&nbsp; <kbd>Space</kbd> L\u1eadt &nbsp;&nbsp; <kbd>\u2190</kbd> Ti\u1ebfp (sau khi l\u1eadt) &nbsp;&nbsp; <kbd>B</kbd> \u0110\u00e1nh d\u1ea5u
      </div>
    </div>

    <div class="session-complete" id="sessionComplete">
      <h2>Ho\u00e0n th\u00e0nh!</h2>
      <div class="session-stats">
        <div class="session-stat"><div class="num pass" id="sessionPass">0</div><div class="label">Nh\u1edb</div></div>
        <div class="session-stat"><div class="num fail" id="sessionFail">0</div><div class="label">Qu\u00ean</div></div>
      </div>
      <p style="font-size:14px;color:var(--fg-secondary);margin-bottom:var(--sp-4);" id="sessionMsg"></p>
      <button class="btn-restart" id="btnRestart">H\u1ecdc l\u1ea1i m\u1ee5c n\u00e0y</button>
    </div>
  </main>
</div>

<div class="modal-overlay" id="resetModal">
  <div class="modal">
    <h3>Reset l\u1ecbch s\u1eed?</h3>
    <p id="resetModalText">X\u00f3a to\u00e0n b\u1ed9 l\u1ecbch s\u1eed T/F c\u1ee7a m\u1ee5c n\u00e0y.</p>
    <div class="modal-actions">
      <button class="modal-btn" id="resetCancel">H\u1ee7y</button>
      <button class="modal-btn danger" id="resetConfirm">Reset</button>
    </div>
  </div>
</div>
"""

full_html = f"""<!DOCTYPE html>
<html lang="vi">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=yes">
<title>TOCFL A2 Flashcard</title>
<link rel="preconnect" href="https://fonts.googleapis.com">
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700&family=Noto+Sans+TC:wght@400;500;600;700&display=swap" rel="stylesheet">
<style>{CSS}</style>
</head>
<body>
{HTML_BODY}
<script>{JS}</script>
</body>
</html>"""

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(full_html)

print(f"Generated index.html ({len(full_html):,} bytes)")
print("Done!")
