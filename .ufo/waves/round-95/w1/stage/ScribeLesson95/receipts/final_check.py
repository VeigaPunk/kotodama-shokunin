#!/usr/bin/env python3
"""Final integrity check of stage/round-95.md.

For every quoted span in the Gate section that sits on an id-bearing line:
the id, the capture it must occur in, and the span's exact byte occurrence.
Also: no id-bearing line may carry a lowercase verdict token (the grader's
VERDICT-LOWERCASE channel), and the Gate section must contain one gate line
per new registry row.
"""
import os
import re
import sys

LESSON = ('/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-95/w1/stage/'
           'ScribeLesson95/round-95.md')
EV = ('/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-95/w1/stage/'
      'ExecRegistry95/evidence')
QUOTE = re.compile(r'"([^"]+)"|“([^”]+)”')
IDS = re.compile(r'\bS\d{3,}\b')
CAPTURE = {'S970': 'S970.txt', 'S971': 'S971.txt', 'S972': 'S972.txt',
           'S973': 'S973.txt', 'S974': 'S974.txt'}

text = open(LESSON, encoding='utf-8').read()
lines = text.splitlines()
start = next(i for i, l in enumerate(lines) if l.startswith('## Gate'))
end = next(i for i, l in enumerate(lines) if i > start and l.startswith('## '))
gate = lines[start:end]

bad = 0
checked = 0
gate_ids = []
for n, line in enumerate(gate, start + 1):
    ids = IDS.findall(line)
    if ids and re.search(r'(?i)not[\s_-]?located|\blocated\b', line):
        print('FAIL line %d: id-bearing line carries a lowercase verdict token' % n)
        bad += 1
    for m in QUOTE.finditer(line):
        q = m.group(1) or m.group(2)
        if not ids:
            continue
        # the quote must occur exactly once in each capture named by an id on this line
        for rid in ids:
            cap = os.path.join(EV, CAPTURE[rid])
            raw = open(cap, encoding='utf-8', errors='replace').read()
            cnt = raw.count(q)
            checked += 1
            if cnt != 1:
                print('FAIL line %d: %s quote count=%d %r' % (n, rid, cnt, q[:60]))
                bad += 1
    if line.startswith('- ') and ' admit A/mined.' in line:
        gate_ids.append(IDS.findall(line)[0])

print('gate lines:', gate_ids)
if sorted(gate_ids) != sorted(CAPTURE):
    print('FAIL: gate lines do not cover the five new rows')
    bad += 1
print('quote occurrences checked: %d | failures: %d' % (checked, bad))
sys.exit(1 if bad else 0)
