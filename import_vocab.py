"""Import the supplied workbook without changing its vocabulary text."""
import argparse
import collections
import json
from pathlib import Path
import openpyxl

parser = argparse.ArgumentParser()
parser.add_argument('workbook', type=Path)
args = parser.parse_args()
rows = openpyxl.load_workbook(args.workbook, read_only=True, data_only=True).worksheets[0].iter_rows(values_only=True)
vocab = []
for row in rows:
    if not row or not isinstance(row[0], (int, float)):
        continue
    number = int(row[0])
    assert row[0] == number, 'Noninteger STT'
    assert all(isinstance(x, str) and x.strip() for x in row[1:4]), f'Missing data at STT {number}'
    vocab.append(dict(id=f'a2-{number:03}', unit=f'U{(number-1)//25+1}', word=row[1], pinyin=row[2], meaning=row[3]))
assert [v['id'] for v in vocab] == [f'a2-{n:03}' for n in range(1, 501)], 'Expected STT 1..500 in order'
assert collections.Counter(v['unit'] for v in vocab) == {f'U{n}':25 for n in range(1,21)}
Path('a2_vocab.json').write_text(json.dumps(vocab, ensure_ascii=False, indent=2)+'\n', encoding='utf-8')
duplicates = [word for word, count in collections.Counter(v['word'] for v in vocab).items() if count > 1]
print(json.dumps(dict(words=len(vocab), units=20, missing=0, duplicate_words=duplicates), ensure_ascii=True))
