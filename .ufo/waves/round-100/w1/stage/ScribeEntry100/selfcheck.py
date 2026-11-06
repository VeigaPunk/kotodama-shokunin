#!/usr/bin/env python3
"""ScribeEntry100 self-check for corpus/knowledge/linguistics/work-song-labour-chant.md.
Read-only. Prints one line per check with its measured number; exit 1 on any failure.
"""
import json
import os
import re
import sys
import unicodedata

ROOT = '/home/vgpnk/Projects/shokunin/kotodama-shokunin'
ENTRY = os.path.join(ROOT, 'corpus/knowledge/linguistics/work-song-labour-chant.md')
REL = 'corpus/knowledge/linguistics/work-song-labour-chant.md'
FROZEN_TOPIC = ('work song and labour chant: song that times and coordinates shared labour \u2014 the song '
                "leader's call and the crew's response; hauling, rowing, pounding, field and craft songs and "
                'how their rhythm fits the task; the shanty and other occupational repertories; improvised '
                'verses, complaint and satire licensed by the work; and the design procedure for a fictional '
                'work-song tradition whose songs stay tied to their task, crew, leader and setting')
PHRASES = ['work song', 'call and response', 'song leader', 'shanty', 'hauling song', 'work rhythm']
ADJACENT = ['orality-formulaic-language.md', 'lullaby-child-song-formulae.md',
            'speech-surrogates-whistled-drummed.md', 'verbal-duelling-ritual-insult.md',
            'funerary-lament-dirge-formulae.md', 'toast-drinking-speech-formulae.md',
            'linguistic-anthropology.md', 'sociolinguistics-registers.md',
            'praise-poetry-panegyric.md']


def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()


def main():
    fails = []
    if not os.path.isfile(ENTRY):
        print('ENTRY absent')
        return 1
    raw = open(ENTRY, encoding='utf-8').read()
    size = len(raw.encode('utf-8'))
    print(f'BYTES {size} (>=12000: {size >= 12000})')
    if size < 12000:
        fails.append('bytes')

    heads = [l for l in raw.splitlines() if l.startswith('## ')]
    print(f'H2 {len(heads)} (>=6: {len(heads) >= 6})')
    if len(heads) < 6:
        fails.append('h2')

    # table shape exactly as predispatch C1 measures it
    best = (0, 0)
    rows, cols, sep = 0, 0, False
    table_rows = []
    for l in raw.splitlines():
        s = l.strip()
        if not s.startswith('|'):
            sep = False
            rows = 0
            continue
        if re.match(r'^\|[\s:\-|]+\|$', s):
            sep = True
            rows = 0
            continue
        c = len(s.strip('|').split('|'))
        if sep:
            rows += 1
            cols = c
            best = max(best, (rows, cols))
            table_rows.append(norm(l))
    r, c = best
    print(f'TABLE {r}x{c} (>=5x3: {r >= 5 and c >= 3})')
    if not (r >= 5 and c >= 3):
        fails.append('table')

    anchor_heads = ' '.join(norm(h) for h in heads)
    hits = [p for p in PHRASES if norm(p) in anchor_heads or any(norm(p) in t for t in table_rows)]
    print(f'PHRASES {len(hits)}/{len(PHRASES)} {hits}')
    if len(hits) < 4:
        fails.append('phrases')

    tline = next((l for l in raw.splitlines() if l.strip().startswith('- topic:')), '')
    tok = tline == ('- topic: ' + FROZEN_TOPIC)
    print(f'TOPIC-LINE {"equal" if tok else "differ"}')
    if not tok:
        fails.append('topic')
        print('  got: ' + tline[:160])

    # cited ids vs rows.md qualifying rows
    rows_md = os.path.join(ROOT, '.ufo/waves/round-100/w1/stage/ExecRegistry100/rows.md')
    ids = []
    if os.path.isfile(rows_md):
        rows_text = [l for l in open(rows_md, encoding='utf-8') if l.startswith('| S')]
        ids = sorted(set(re.findall(r'\bS\d{3,}\b', '\n'.join(rows_text))),
                     key=lambda x: int(x[1:]))
    cited = sorted(set(re.findall(r'\bS\d{3,}\b', raw)), key=lambda x: int(x[1:]))
    uncited = [i for i in ids if i not in cited]
    print(f'CITED ids={len(cited)} {cited} rows.md={len(ids)} uncited={uncited}')
    if ids and uncited:
        fails.append('c6')
    if not ids:
        print('  WARN rows.md absent: C6 not evaluable here')

    # multi-id lines (QUALITY 15 lint shape)
    multi = [(n, l.strip()[:80]) for n, l in enumerate(raw.splitlines(), 1)
             if len(set(re.findall(r'\bS\d{3,}\b', l))) >= 2]
    tableid = [(n, l.strip()[:60]) for n, l in enumerate(raw.splitlines(), 1)
               if l.lstrip().startswith('|') and re.search(r'\bS\d{3,}\b', l)]
    print(f'CITED-LINES multi-id={len(multi)} table-id={len(tableid)} {multi[:3]} {tableid[:3]}')
    if multi or tableid:
        fails.append('cited-lines')

    # 8-gram overlap against adjacent owners
    def grams(text):
        toks = re.findall(r'[a-z0-9]+', text.lower())
        return {' '.join(toks[i:i + 8]) for i in range(len(toks) - 7)}

    # The lane's standard header block (source/verified-at/recheck lines) is shared by every
    # entry; it is a format convention, not prose copied from a neighbour, so it is exempt.
    body = '\n'.join(l for l in raw.splitlines()
                     if not l.startswith(('- source:', '- verified-at:', '- recheck:')))
    mine = grams(body)
    worst = []
    for name in ADJACENT:
        p = os.path.join(ROOT, 'corpus/knowledge/linguistics', name)
        if not os.path.isfile(p):
            continue
        other = grams(open(p, encoding='utf-8').read())
        shared = mine & other
        worst.append((len(shared), name, sorted(shared)[:3]))
    worst.sort(reverse=True)
    print('OVERLAP-8GRAM ' + '; '.join(f'{n}={c}' for c, n, _ in worst))
    for c, n, sample in worst[:3]:
        if c:
            print(f'  {n}: {sample}')
    if worst and worst[0][0] > 0:
        fails.append('overlap')

    print('SELFCHECK ' + ('PASS' if not fails else 'FAIL ' + ','.join(fails)))
    return 0 if not fails else 1


if __name__ == '__main__':
    sys.exit(main())
