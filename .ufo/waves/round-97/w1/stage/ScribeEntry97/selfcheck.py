#!/usr/bin/env python3
"""ScribeEntry97 self-check: measures the round-97 claim-C entry against the frozen counter's
own C1 predicate and the seat's own extra checks (cited ids vs rows.md, C8 ownership sweep).

Usage: python3 -B selfcheck.py --entry <path> --rows <rows.md> [--root <lane root>]
Prints one `CHECK <name> <PASS|FAIL> <detail>` line per check and exits 0 iff all pass.
"""
import argparse
import os
import re
import sys

ENTRY_REL = 'corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md'
FROZEN_TOPIC = ('verbal duelling and ritual insult: contests fought in words — flyting, senna, '
                'song duels and boasting matches; the formula grammar of boast, taunt and riposte; '
                'the audience that adjudicates; the rules that keep an insult ritual rather than '
                'real; and the design procedure for a fictional word-contest whose stakes stay tied '
                'to its contestants, judges and occasions')
PHRASES = ['verbal duel', 'ritual insult', 'flyting', 'song duel', 'boast formula',
           'audience adjudication']
MIN_BYTES = 12000
MIN_H2 = 6
ROW_MIN, ROWS_MIN = 3, 5

RES = []


def check(name, ok, detail):
    RES.append(bool(ok))
    print(f'CHECK {name} {"PASS" if ok else "FAIL"} {detail}')
    return ok


def norm(s):
    return re.sub(r'[^a-z0-9]+', ' ', s.lower()).strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--entry', required=True)
    ap.add_argument('--rows', default=None)
    ap.add_argument('--root', default=None)
    a = ap.parse_args()
    raw = open(a.entry, encoding='utf-8').read()

    size = len(raw.encode('utf-8'))
    check('BYTES', size >= MIN_BYTES, f'bytes={size} floor={MIN_BYTES}')

    heads = [l for l in raw.splitlines() if l.startswith('## ')]
    check('H2', len(heads) >= MIN_H2, f'h2={len(heads)} floor={MIN_H2}')

    rows = cols = 0
    sep = False
    table_rows = []
    best = (0, 0)
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
    check('TABLE', r >= ROWS_MIN and c >= ROW_MIN, f'best-table={r}x{c} floor={ROWS_MIN}x{ROW_MIN}')

    anchor = ' '.join(norm(h) for h in heads)
    hits = [p for p in PHRASES if norm(p) in anchor or any(norm(p) in t for t in table_rows)]
    check('PHRASES', len(hits) >= 4, f'phrases={len(hits)}/{len(PHRASES)} hits={hits}')

    tline = next((l for l in raw.splitlines() if l.strip().startswith('- topic:')), '')
    check('TOPIC', tline == '- topic: ' + FROZEN_TOPIC,
          'topic-line=byte-equal' if tline == '- topic: ' + FROZEN_TOPIC
          else f'topic-line differs (len={len(tline)})')

    if a.rows and os.path.isfile(a.rows):
        ids = sorted(set(re.findall(r'\bS\d{3,}\b', raw)))
        rowtext = open(a.rows, encoding='utf-8').read()
        # rows.md groups the landed rows under a section heading that names the
        # used-by path; a row belongs to the group whose section it sits under.
        section = None
        groups = {}
        for line in rowtext.splitlines():
            if line.startswith('## '):
                section = line
            m = re.match(r'### (S\d{3,})', line)
            if m:
                groups.setdefault(section, []).append(m.group(1))
        entry_rel = 'corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md'
        used_by_entry = sorted(
            sid for head, sids in groups.items()
            if head and entry_rel in head for sid in sids)
        rowids = sorted({sid for sids in groups.values() for sid in sids})
        check('IDS_CITED', bool(used_by_entry) and all(i in ids for i in used_by_entry),
              f'cited={ids} rows.md ids={rowids} '
              f'used-by-entry={used_by_entry} '
              f'missing={[i for i in used_by_entry if i not in ids]}')
    else:
        check('IDS_CITED', False, 'rows.md not available')

    if a.root:
        sys.path.insert(0, os.path.join(a.root, 'reports/round-97'))
        import importlib.util
        spec = importlib.util.spec_from_file_location(
            'pd97', os.path.join(a.root, 'reports/round-97/predispatch.py'))
        pd = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(pd)
        kf = pd.tree_knowledge(a.root)
        owners = pd.sweep_owners(kf, PHRASES, exclude=(ENTRY_REL,))
        check('C8_SWEEP', not owners, f'files={len(kf)} other owners={owners}')

    npass = sum(1 for x in RES if x)
    print(f'SELFCHECK: {"PASS" if npass == len(RES) else "FAIL"} checks={npass}/{len(RES)}')
    return 0 if npass == len(RES) else 1


if __name__ == '__main__':
    sys.exit(main())
