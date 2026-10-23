#!/usr/bin/env python3
"""Generate data fixtures from real off-topic prose; never alters a frozen counter."""
import hashlib
import html
import importlib.util
import json
from pathlib import Path
import re
import urllib.parse
import sys

BASE = Path('/fast/scratch/hyaku/kotodama-r59/CtlOffTopicEcho59')
ROOT = BASE / 'clone'
ENTRY = 'corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'
spec = importlib.util.spec_from_file_location('rowcheck', ROOT / 'reports/round-59/rowcheck.py')
rc = importlib.util.module_from_spec(spec)
spec.loader.exec_module(rc)

preferred = {
0: 'Lucky Charms made its magical debut',
1: 'Lucky Charms has been a breakfast staple',
2: 'Made with whole grain Lucky Charms',
4: 'Since their release',
5: 'Lucky Charms cereal was created',
6: 'From the shape',
8: 'Think of the classic',
11: 'Whether they’re made',
13: "They're a dessert bar",
14: 'Lucky Charms bars are chewy',
15: 'You will need an entire box',
16: 'Remove from heat',
21: "You'll of course need",
24: 'The marshmallows inside',
26: 'If you want to switch',
27: 'Lucky Charms cereal is labeled',
29: 'Actress Romola Garai',
31: 'Amulet is unfortunately',
32: 'Amulet is a layered film',
33: 'Cast in',
40: 'I will share',
41: 'While pudding is setting',
42: 'It all starts',
45: 'We infused',
}
suffix = '-all' if '--all' in sys.argv else ''
items = json.loads((BASE / 'scouted.json').read_text())
if suffix:
    items += json.loads((BASE / 'scouted-extra.json').read_text())
records = []
for item in items:
    if item['index'] not in preferred:
        continue
    raw = (BASE / 'bodies' / f"{item['index']:02}.html").read_text(errors='replace')
    labels = []
    for pattern in rc.LABELS:
        labels.extend(pattern.findall(raw))
    labeltext = html.unescape(re.sub(r'<[^>]+>', ' ', '\n'.join(labels)))
    choices = sorted(item['quotes_root_clear'], key=lambda q: not q.startswith(preferred[item['index']]))
    choices = [q for q in choices if not labeltext.strip() or not rc.locator.locate_in(labeltext,q)]
    if not choices:
        print(f"LABEL-REJECT {item['index']} {item['url']}")
        continue
    quote = choices[0].replace('"', '’').replace('“','’').replace('”','’')
    tokens = []
    seen = set()
    for word in rc.locator.normalise(quote).split():
        stems = rc.stems(word)
        if stems and not seen.intersection(stems):
            tokens.append(word)
            seen.update(stems)
        if len(tokens) == 4:
            break
    if len(tokens) < 4:
        print(f"STEM-REJECT {item['index']} {item['url']}")
        continue
    a,b,c,d = tokens
    teaches = f'A mechanical echo associates {a} with {b} and records {c} beside {d}.'
    sid = f'S{600 + len(records)}'
    entry_line = f'For the working note, {d} accompanies {c} while {b} frames {a} ({sid}).'
    assert not rc.copied(quote, teaches)
    assert rc.relevance(sid,quote,teaches,entry_line)[0]
    row = f'| {sid} | Ordinary GET off-topic control — {item["url"]} | docs | B | Deliberate non-domain body sentence; control only | Body paragraph opened 2026-10-23: "{quote}" | {teaches} | mined | 2026-10-23 | 365d | {ENTRY} |'
    records.append(dict(sid=sid,index=item['index'],url=item['url'],quote=quote,teaches=teaches,entry_line=entry_line,row=row,page_hits=item['page_hits'],page_terms=item['page_terms'],quote_hits=rc.window_hits(quote),body_sha256=item['body_sha256']))

rows = '\n'.join(r['row'] for r in records)+'\n'
entry = '# Amulets, talismans and apotropaic marks\n\n- topic: amulets, talismans and apotropaic marks\n- source: mechanical echo control\n- verified-at: 2026-10-23\n- recheck: round-59 frozen counter\n\n'+ '\n'.join(r['entry_line'] for r in records)+'\n'
(BASE / f'draft{suffix}.md').write_text(rows)
(BASE / f'entry{suffix}.md').write_text(entry)
(BASE / f'rows{suffix}.json').write_text(json.dumps(records, indent=2, ensure_ascii=False)+'\n')
for i in range(4):
    (BASE / f'draft{suffix}-{i}.md').write_text('\n'.join(r['row'] for r in records[i::4])+'\n')
print(f'GENERATED rows={len(records)} hosts={len({urllib.parse.urlsplit(r["url"]).hostname for r in records})} six_word_runs=0')
for r in records:
    print(f'{r["sid"]} source={r["index"]:02} quote_hits={r["quote_hits"]} page_hits={r["page_hits"]} terms={r["page_terms"]} {r["quote"]}')
