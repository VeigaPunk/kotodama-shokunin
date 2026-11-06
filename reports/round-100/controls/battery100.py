#!/usr/bin/env python3
"""battery100 — frozen case battery for claim O (round 100): the table-cell support checker
tools/check-table-support.py. Committed in the freeze commit before any seat runs; never edited
afterwards (counter leg O2 binds its sha256 to reports/round-100/controls/battery100.sha256 and to
the BATTERY-SHA256 line of every control receipt).

Usage: python3 -B battery100.py --tool <path> --work <existing dir, not under /tmp>

Each case builds a fixture (entry markdown, evidence dir of S-id captures, optional --root tree)
under --work, runs the tool with --json (or text mode for T-cases), and compares rc plus the EXACT
set of finding keys: (id, row|sid|path, col|''). Selected cases also compare `words`, `best`,
`total` or `scoped_tables`. Prints one CASE line per case and
`BATTERY-SUMMARY cases=<n> pass=<p> fail=<f> traceback=<t>`; rc 0 iff fail == 0 and traceback == 0.
"""
import argparse
import hashlib
import json
import os
import shutil
import subprocess
import sys

CAP = '| tradition | singer | limit |'
SEP3 = '|---|---|---|'

EVID = {
    'S9001': ('In the court the singer receives gifts from the chief and rewards from passers-by. '
              'Drummers recite titles of the king. Criticism of the chief is licensed in the song.'),
    'S9002': ('The leader calls each line and the rowing crew answers in chorus, keeping time with the '
              'oars.'),
    'S9003': 'chief ' + ' '.join(['lorem'] * 200) + ' bounty',
    'S9004': 'Each rally sang near the church and the box of drums held the oriki of the town.',
    'S9005': 'chief ' + ' '.join(['lorem'] * 30) + ' bounty',
}
REF_MD = '# Ref\nWeavers sing a slow song at the loom.\n'


def entry(caption, header, sep, rows, bind, tail='## 2. Next\n\nText.\n'):
    out = ['# T', '', '## 1. Section', '', caption, '', header, sep] + rows + ['']
    if bind:
        out += bind + ['']
    return '\n'.join(out) + '\n' + tail


REC = 'The columns are filled from the recorded cases this entry cites.'
COURT = '| Court | singer receives gifts | criticism of the chief is licensed |'


def cases():
    C = []
    # benign controls (rc 0, no findings)
    C.append(dict(id='B1', text=entry(REC, CAP, SEP3, [COURT],
                                      ['The Court row reports the court singer (S9001).']),
                  rc=0, keys=[]))
    C.append(dict(id='B2', text=entry(REC, '| tradition | place | object |', SEP3,
                                      ['| Town | rallies near churches | boxes of oriki |'],
                                      ['The Town row reports the town (S9004).']), rc=0, keys=[]))
    C.append(dict(id='B3', text=entry('A summary of design choices.', CAP, SEP3,
                                      ['| Court | zebra xylophone quantum | nebula |'], []),
                  rc=0, keys=[], scoped=0))
    C.append(dict(id='B4', text=entry(REC, '| tradition | practice | setting |', SEP3,
                                      ['| Loom | weavers sing slow | song at the loom |'],
                                      ['The Loom row restates `x/ref.md:2`.']), rc=0, keys=[], root=True))
    C.append(dict(id='B5', text=entry(REC, '| tradition | form |', '|---|---|',
                                      ['| Town | oríkì drums |'],
                                      ['The Town row reports the town (S9004).']), rc=0, keys=[]))
    C.append(dict(id='B6', text=entry(REC, CAP, SEP3,
                                      ['| Court | with the chief, also from them | singer |'],
                                      ['The Court row reports the court (S9001).']), rc=0, keys=[]))
    C.append(dict(id='B7', text=entry('Built from unrecorded cases only.', CAP, SEP3,
                                      ['| Court | zebra xylophone quantum | nebula |'], []),
                  rc=0, keys=[], scoped=0))
    C.append(dict(id='B8', text=entry(REC, '| tradition | reward |', '|---|---|',
                                      ['| Hall | chief bounty |'],
                                      ['The Hall row reports the hall (S9005).']), rc=0, keys=[]))
    C.append(dict(id='B9', text=entry(REC, '| tradition | reward |', '|---|---|',
                                      ['| Court | singer receives gifts zebra |'],
                                      ['The Court row reports the court (S9001).']), rc=0, keys=[]))
    # refusal cases
    C.append(dict(id='F1', text=entry(REC, CAP, SEP3, [
        COURT,
        '| Yoruba | drummers recite titles | titles are public property, so any drummer who knows them '
        'can assemble the praise |'],
        ['The Court and Yoruba rows report the court cases (S9001).']), rc=1,
        keys=[('UNSUPPORTED-CELL', 'Yoruba', 'limit')],
        words={('UNSUPPORTED-CELL', 'Yoruba', 'limit'): ['assemble', 'knows', 'praise', 'property', 'public']},
        best={('UNSUPPORTED-CELL', 'Yoruba', 'limit'): (2, 7)}))
    C.append(dict(id='F2', text=entry(REC, CAP, SEP3, [COURT, '| Hausa | singer receives gifts | chief |'],
                                      ['The Court row reports the court (S9001).']), rc=1,
                  keys=[('UNBOUND-ROW', 'Hausa', '')]))
    C.append(dict(id='F3', text=entry(REC, CAP, SEP3, [COURT],
                                      ['The Court row reports the court (S9001).',
                                       'The Court row also reports the court (S9999).']), rc=1,
                  keys=[('NO-CAPTURE', 'S9999', '')]))
    C.append(dict(id='F4', text=entry(REC, CAP, SEP3, [COURT],
                                      ['The Court row reports the court (S9001).',
                                       'The Court row restates `x/missing.md:3`.']), rc=1,
                  keys=[('NO-PATH', 'x/missing.md', '')], root=True))
    C.append(dict(id='F5', text=entry(REC, CAP, SEP3, [COURT, '| Town | rallies near churches | drums |'], []),
                  rc=1, keys=[('UNBOUND-ROW', 'Court', ''), ('UNBOUND-ROW', 'Town', '')]))
    C.append(dict(id='F6', text=entry(REC, '| tradition | practice |', '|---|---|',
                                      ['| Court | singer receives gifts |', '| River | leader calls crew |'],
                                      ['The Court row reports the court (S9002).',
                                       'The River row reports the river (S9001).']), rc=1,
                  keys=[('UNSUPPORTED-CELL', 'Court', 'practice'), ('UNSUPPORTED-CELL', 'River', 'practice')]))
    C.append(dict(id='F7', text=entry('Recorded Cases fill this table.', '| tradition | practice |', '|---|---|',
                                      ['| Court | zebra quantum xylophone |'],
                                      ['The Court row reports the court (S9001).']), rc=1,
                  keys=[('UNSUPPORTED-CELL', 'Court', 'practice')],
                  words={('UNSUPPORTED-CELL', 'Court', 'practice'): ['quantum', 'xylophone', 'zebra']}))
    C.append(dict(id='F8', text=entry(REC, CAP, SEP3, [COURT], ['Notes without ids.', '',
                                                                'The Court row reports the court (S9001).']),
                  rc=1, keys=[('UNBOUND-ROW', 'Court', '')]))
    two = entry(REC, CAP, SEP3, [COURT], ['The Court row reports the court (S9001).'],
                tail='## 2. Next\n\nThese rows come from recorded cases too.\n\n| tradition | practice |\n|---|---|\n'
                     '| River | zebra quantum xylophone |\n\nThe River row reports the river (S9002).\n')
    C.append(dict(id='F9', text=two, rc=1, keys=[('UNSUPPORTED-CELL', 'River', 'practice')], scoped=2))
    C.append(dict(id='F10', text=entry(REC, CAP, SEP3, ['| Ewe | singer receives gifts | chief |'],
                                       ['The jewel row reports the court (S9001).']), rc=1,
                  keys=[('UNBOUND-ROW', 'Ewe', '')]))
    C.append(dict(id='F11', text=entry(REC, '| tradition | reward |', '|---|---|', ['| Hall | chief bounty |'],
                                       ['The Hall row reports the hall (S9003).']), rc=1,
                  keys=[('UNSUPPORTED-CELL', 'Hall', 'reward')],
                  words={('UNSUPPORTED-CELL', 'Hall', 'reward'): []},
                  best={('UNSUPPORTED-CELL', 'Hall', 'reward'): (1, 2)}))
    C.append(dict(id='F12', text=entry(REC, CAP, SEP3, [COURT], ['The Court row reports the court singer.']),
                  rc=1, keys=[('UNBOUND-ROW', 'Court', '')]))
    C.append(dict(id='F13', text=entry(REC, '| tradition | reward |', '|---|---|',
                                       ['| Court | singer receives zebra quantum |'],
                                       ['The Court row reports the court (S9001).']), rc=1,
                  keys=[('UNSUPPORTED-CELL', 'Court', 'reward')],
                  words={('UNSUPPORTED-CELL', 'Court', 'reward'): ['quantum', 'zebra']},
                  best={('UNSUPPORTED-CELL', 'Court', 'reward'): (2, 4)}))
    # error cases (rc 2, TABLE_SUPPORT_ERROR, no traceback)
    C.append(dict(id='E1', err='missing-entry', rc=2))
    C.append(dict(id='E2', err='bad-utf8', rc=2))
    C.append(dict(id='E3', err='missing-evidence', rc=2))
    C.append(dict(id='E4', err='no-evidence-arg', rc=2))
    # text mode summary
    C.append(dict(id='T1', text=entry(REC, CAP, SEP3, [COURT], ['The Court row reports the court singer (S9001).']),
                  rc=0, textmode='TABLE-SUPPORT: 0 finding(s) in 1 scoped table(s)'))
    C.append(dict(id='T2', text=entry(REC, '| tradition | practice |', '|---|---|', ['| Court | zebra quantum xylophone |'],
                                      ['The Court row reports the court (S9001).']),
                  rc=1, textmode='TABLE-SUPPORT: 1 finding(s) in 1 scoped table(s)'))
    return C


def key(f):
    i = f.get('id')
    if i in ('UNSUPPORTED-CELL', 'UNBOUND-ROW'):
        return (i, f.get('row'), f.get('col', '') if i == 'UNSUPPORTED-CELL' else '')
    if i == 'NO-CAPTURE':
        return (i, f.get('sid'), '')
    if i == 'NO-PATH':
        return (i, f.get('path'), '')
    return (str(i), '?', '?')


def run_case(tool, work, c):
    d = os.path.join(work, c['id'])
    shutil.rmtree(d, ignore_errors=True)
    os.makedirs(os.path.join(d, 'ev'))
    for k, v in EVID.items():
        open(os.path.join(d, 'ev', k + '.txt'), 'w', encoding='utf-8').write(v)
    root = os.path.join(d, 'root')
    os.makedirs(os.path.join(root, 'corpus/knowledge/x'))
    open(os.path.join(root, 'corpus/knowledge/x/ref.md'), 'w', encoding='utf-8').write(REF_MD)
    ent = os.path.join(d, 'entry.md')
    args = [sys.executable, '-B', tool, '--entry', ent, '--evidence', os.path.join(d, 'ev')]
    err = c.get('err')
    if err == 'missing-entry':
        args[args.index(ent)] = os.path.join(d, 'absent.md')
    elif err == 'bad-utf8':
        open(ent, 'wb').write(b'\xff\xfe# T\n| a | b |\n')
    elif err == 'missing-evidence':
        open(ent, 'w', encoding='utf-8').write('# T\n')
        args[-1] = os.path.join(d, 'no-such-dir')
    elif err == 'no-evidence-arg':
        open(ent, 'w', encoding='utf-8').write('# T\n')
        args = args[:-2]
    else:
        open(ent, 'w', encoding='utf-8').write(c['text'])
    if c.get('root'):
        args += ['--root', root]
    if not c.get('textmode') and not err:
        args.append('--json')
    try:
        p = subprocess.run(args, capture_output=True, text=True, timeout=60)
    except subprocess.TimeoutExpired:
        return False, False, 'timeout'
    tb = 'Traceback (most recent call last)' in (p.stdout + p.stderr)
    if err:
        ok = p.returncode == 2 and 'TABLE_SUPPORT_ERROR' in (p.stdout + p.stderr) and not tb
        return ok, tb, f'rc={p.returncode} error-line={"TABLE_SUPPORT_ERROR" in (p.stdout + p.stderr)}'
    if c.get('textmode'):
        lines = [l.strip() for l in p.stdout.splitlines()]
        ok = p.returncode == c['rc'] and c['textmode'] in lines and not tb
        return ok, tb, f'rc={p.returncode} summary-present={c["textmode"] in lines}'
    try:
        js = json.loads(p.stdout)
        fs = js['findings']
        got = sorted({key(f) for f in fs})
    except Exception as e:  # malformed output fails the case
        return False, tb, f'rc={p.returncode} json-unparseable ({type(e).__name__})'
    want = sorted(set(c['keys']))
    ok = p.returncode == c['rc'] and got == want and not tb and len(fs) == len(got)
    detail = f'rc={p.returncode} got={got}'
    for k, w in (c.get('words') or {}).items():
        f = next((f for f in fs if key(f) == k), None)
        gw = sorted(f.get('words', [])) if f else None
        ok = ok and gw == sorted(w)
        detail += f' words={gw}'
    for k, (b, t) in (c.get('best') or {}).items():
        f = next((f for f in fs if key(f) == k), None)
        ok = ok and f is not None and f.get('best') == b and f.get('total') == t
        detail += f' best/total={f.get("best") if f else None}/{f.get("total") if f else None}'
    if 'scoped' in c:
        ok = ok and js.get('scoped_tables') == c['scoped']
        detail += f' scoped={js.get("scoped_tables")}'
    return ok, tb, detail


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tool', required=True)
    ap.add_argument('--work', required=True)
    a = ap.parse_args()
    work = os.path.abspath(a.work)
    if os.path.realpath(work).startswith('/tmp'):
        print('REFUSED --work must not live under /tmp')
        return 2
    os.makedirs(work, exist_ok=True)
    me = hashlib.sha256(open(os.path.abspath(__file__), 'rb').read()).hexdigest()
    print(f'BATTERY-SHA256 {me}')
    if not os.path.isfile(a.tool):
        print(f'TOOL-MISSING {a.tool}')
        print('BATTERY-SUMMARY cases=0 pass=0 fail=1 traceback=0')
        return 1
    print(f'TOOL-SHA256 {hashlib.sha256(open(a.tool, "rb").read()).hexdigest()}')
    n = npass = ntb = 0
    for c in cases():
        n += 1
        ok, tb, detail = run_case(os.path.abspath(a.tool), work, c)
        npass += ok
        ntb += tb
        print(f'CASE {c["id"]} {"PASS" if ok else "FAIL"} {detail}')
    print(f'BATTERY-SUMMARY cases={n} pass={npass} fail={n - npass} traceback={ntb}')
    return 0 if npass == n and ntb == 0 else 1


if __name__ == '__main__':
    sys.exit(main())
