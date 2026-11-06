#!/usr/bin/env python3
"""CriticC97 claim-C leg checks (read-only):
1. manifest.json: for each id, re-count the quote in the lane evidence capture
   (bytes.count == 1) and recompute capture sha256 == manifest sha256.
2. SOURCES.md S985+ rows: ids, used-by exactly the entry path, opened 2026-11-05,
   tier A|B, status mined; row ids == manifest ids.
3. entry: cited ids (S98x tokens) vs row ids.
4. append-only: removed lines base->worktree SOURCES.md == 0.
5. census: caller runs sources-census.sh separately; this prints row stats only.
Usage: verify_c.py <root>"""
import hashlib, json, os, re, subprocess, sys

ROOT = sys.argv[1] if len(sys.argv) > 1 else '/home/vgpnk/Projects/shokunin/kotodama-shokunin'
BASE = '1ffc5a83d2c70e3bc581594efbcf32c562ba2569'
ENTRY = os.path.join(ROOT, 'corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md')
EV = os.path.join(ROOT, 'reports/round-97/evidence')

fails = []
def check(name, ok, detail):
    print(f'CHECK {name} {"PASS" if ok else "FAIL"} {detail}')
    if not ok:
        fails.append(name)

man = json.load(open(os.path.join(EV, 'manifest.json')))
rows = man if isinstance(man, list) else man.get('rows', man.get('captures', []))
if isinstance(rows, dict):
    rows = list(rows.values())
print(f'manifest rows: {len(rows)}')
for r in rows:
    rid = r.get('id', '')
    q = r.get('quote', '')
    qc_name = r.get('quote_capture', '')
    p = os.path.join(EV, qc_name) if qc_name else ''
    if not p or not os.path.isfile(p):
        check(f'{rid}:quote-capture-exists', False, f'missing {qc_name!r}')
        continue
    data = open(p, 'rb').read()
    cnt = data.count(q.encode('utf-8')) if q else -1
    check(f'{rid}:quote-count==1', cnt == 1, f'count={cnt} capture={qc_name} bytes={len(data)}')
    tsha = hashlib.sha256(data).hexdigest()
    check(f'{rid}:text-sha==manifest', tsha == (r.get('text_extraction', {}).get('sha256') or r.get('sha256', '')),
          f'{tsha[:12]}')
    check(f'{rid}:manifest-quote-count', r.get('quote_count') == cnt, f'manifest={r.get("quote_count")} recomputed={cnt}')

src = open(os.path.join(ROOT, 'corpus/SOURCES.md'), encoding='utf-8').read()
row_ids = re.findall(r'^ {0,3}\| ?(S9[89]\d) ?\|', src, re.M)
new_ids = sorted(set(row_ids))
print(f'SOURCES.md S985+ row ids: {new_ids}')
man_ids = sorted(r.get('id', '') for r in rows)
check('rows==manifest-ids', new_ids == man_ids, f'{new_ids} vs {man_ids}')

used_by_bad = []
opened_bad, tier_bad, status_bad = [], [], []
for line in src.splitlines():
    m = re.match(r'^ {0,3}\| ?(S9[89]\d) ?\|', line)
    if not m:
        continue
    cells = [c.strip() for c in line.strip().strip('|').split('|')]
    if len(cells) >= 11:
        if cells[10] != 'corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md' and m.group(1) in new_ids:
            used_by_bad.append((m.group(1), cells[10][:60]))
        if cells[8] != '2026-11-05':
            opened_bad.append((m.group(1), cells[8]))
        if cells[3] not in ('A', 'B'):
            tier_bad.append((m.group(1), cells[3]))
        if cells[7] != 'mined':
            status_bad.append((m.group(1), cells[7]))
check('used-by==entry', not used_by_bad, str(used_by_bad))
check('opened==2026-11-05', not opened_bad, str(opened_bad))
check('tier A|B', not tier_bad, str(tier_bad))
check('status mined', not status_bad, str(status_bad))

etext = open(ENTRY, encoding='utf-8').read() if os.path.exists(ENTRY) else ''
cited = sorted(set(re.findall(r'S9[89]\d', etext)))
check('entry-cited==rows', cited == new_ids, f'entry {cited} vs rows {new_ids}')

base_src = subprocess.run(['git', 'show', f'{BASE}:corpus/SOURCES.md'], capture_output=True,
                          text=True, check=True).stdout
import difflib
rem = sum(1 for l in difflib.unified_diff(base_src.splitlines(), src.splitlines(), lineterm='', n=0)
          if l.startswith('-') and not l.startswith('---'))
check('append-only removed==0', rem == 0, f'removed={rem}')

print(f'FAILURES: {len(fails)} {fails}')
sys.exit(0 if not fails else 1)
