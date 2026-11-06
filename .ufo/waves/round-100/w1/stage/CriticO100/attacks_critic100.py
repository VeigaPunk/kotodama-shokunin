#!/usr/bin/env python3
"""attacks_critic100.py — adversarial fixtures for tools/check-table-support.py (round 100, claim O).

Attack seat only: reads the tool, battery100 and the feasibility reference; never edits them, any
pin, any driver or claims.json. Every fixture is built under --work (scratch); the tool and the
pinned reference are invoked as subprocesses.

Contract source: reports/round-100/claims.json claims.O.contract (frozen). Each class's expected
verdict is decided from that text BEFORE the run; the feasibility reference (the L1's implementation,
pinned by battery100 28/28) is run alongside only as a second opinion. A tool/ref divergence is
reported separately from a contract mismatch.

Usage: python3 -B attacks_critic100.py [--work DIR] [--only ID,ID,...] [--sweep] [--no-ref]
Exit: 0 when no OVERREFUSAL / FALSE-GREEN / traceback; 1 otherwise (CONTRACT-GAP never fails).
"""
import argparse
import glob
import json
import os
import shutil
import subprocess
import sys

LANE = '/home/vgpnk/Projects/shokunin/kotodama-shokunin'
TOOL = os.path.join(LANE, 'tools/check-table-support.py')
REF = os.path.join(LANE, 'reports/round-100/controls/feasibility/table_support_ref.py')
DEFWORK = '/fast/scratch/hyaku/kotodama-r100/CriticO100/classes'

E1 = ('In the court the singer receives gifts from the chief and rewards from passers-by. '
      'Drummers recite titles of the king. Criticism of the chief is licensed in the song.')
E2 = ('The leader calls each line and the rowing crew answers in chorus, keeping time with the '
      'oars.')
E4 = ('Each rally sang near the church and the box of drums held the oriki of the town.')
E9101 = ('court ' + ' '.join(['lorem'] * 200) + ' singer ' + ' '.join(['ipsum'] * 200) +
         ' receives ' + ' '.join(['dolor'] * 200) + ' gifts')
REF_MD = '# Ref\nWeavers sing a slow song at the loom.\n'
REC = 'The columns are filled from the recorded cases this entry cites.'
CAP3 = '| tradition | singer | limit |'
SEP3 = '|---|:---|:--:|'
COURT = '| Court | singer receives gifts | criticism of the chief is licensed |'


def entry(caption, header, sep, rows, bind, tail='## 2. Next\n\nText.\n'):
    out = ['# T', '', '## 1. Section', '', caption, '', header, sep] + rows + ['']
    if bind:
        out += bind + ['']
    return '\n'.join(out) + '\n' + tail


def lead(text, n=2):
    return '\n'.join((' ' * n + l) if l.startswith('|') else l for l in text.split('\n'))


def trail(text):
    return text.replace('\n', '   \n')


CLASSES = []


def C(**kw):
    CLASSES.append(kw)


# ---------------------------------------------------------------- benign (contract: CLEAN)
C(id='B1', kind='benign', note='separator row with alignment colons',
  text=entry(REC, CAP3, '|---|:---|:--:|', [COURT],
             ['The Court row reports the court (S9001).']),
  evid={'S9001': E1}, expect=dict(rc=0, keys=[], scoped=1))

C(id='B2', kind='benign', note='emphasis, inline code, [link](x) and &amp; in a supported cell',
  text=entry(REC, CAP3, '|---|---|---|',
             ['| Court | **singer** receives [gifts](x) &amp; `rewards` | criticism of the chief is licensed |'],
             ['The Court row reports the court (S9001).']),
  evid={'S9001': E1}, expect=dict(rc=0, keys=[], scoped=1))

C(id='B3', kind='benign', note='CRLF line endings',
  raw=entry(REC, CAP3, '|---|---|---|', [COURT],
            ['The Court row reports the court (S9001).']).replace('\n', '\r\n').encode(),
  evid={'S9001': E1}, expect=dict(rc=0, keys=[], scoped=1))

C(id='B4', kind='benign', note='trailing spaces on every line',
  text=trail(entry(REC, CAP3, '|---|---|---|', [COURT],
                   ['The Court row reports the court (S9001).'])),
  evid={'S9001': E1}, expect=dict(rc=0, keys=[], scoped=1))

C(id='B5', kind='benign', note='two leading spaces before every table pipe',
  text=lead(entry(REC, CAP3, '|---|---|---|', [COURT],
                  ['The Court row reports the court (S9001).'])),
  evid={'S9001': E1}, expect=dict(rc=0, keys=[], scoped=1))

C(id='B6', kind='benign', note='one binding line carrying two S-ids',
  text=entry(REC, CAP3, '|---|---|---|', [COURT],
             ['The Court row reports the court (S9001) and the singer rewards (S9002).']),
  evid={'S9001': E1, 'S9002': E2}, expect=dict(rc=0, keys=[], scoped=1))

C(id='B7', kind='benign', note='diacritic label Oríkì bound by its folded form oriki',
  text=entry(REC, '| tradition | practice |', '|---|---|',
             ['| Oríkì | drums held in the box |'],
             ['The oriki row reports the drums (S9004).']),
  evid={'S9004': E4}, expect=dict(rc=0, keys=[], scoped=1))

C(id='B8', kind='benign', note="caption says 'recorded case' (singular)",
  text=entry('Each row is a recorded case.', CAP3, '|---|---|---|', [COURT],
             ['The Court row reports the court (S9001).']),
  evid={'S9001': E1}, expect=dict(rc=0, keys=[], scoped=1))

C(id='B9', kind='benign', note='a second unscoped table in the same file',
  text=entry(REC, CAP3, '|---|---|---|', [COURT],
             ['The Court row reports the court (S9001).'],
             tail=('## 2. Next\n\nA summary of design choices.\n\n'
                   '| tradition | practice |\n|---|---|\n| River | zebra quantum xylophone |\n\n'
                   'No binding here.\n')),
  evid={'S9001': E1}, expect=dict(rc=0, keys=[], scoped=1))

C(id='B10', kind='benign', note='entry with no tables at all',
  text='# T\n\n## 1. Section\n\nNo tables here at all.\n',
  evid={'S9001': E1}, expect=dict(rc=0, keys=[], scoped=0))

# ---------------------------------------------------------------- attack (contract: FLAGGED)
C(id='A1', kind='attack', note='cell words present in the capture but >80 tokens apart',
  text=entry(REC, '| tradition | singer |', '|---|---|',
             ['| Court | singer receives gifts |'],
             ['The Court row reports the court (S9101).']),
  evid={'S9101': E9101}, expect=dict(rc=1, keys=[('UNSUPPORTED-CELL', 'Court', 'singer')],
                                     scoped=1, best={('UNSUPPORTED-CELL', 'Court', 'singer'): (1, 3)}))

C(id='A2', kind='attack', note="Court cell's words exist only in the River row's capture",
  text=entry(REC, '| tradition | practice |', '|---|---|',
             ['| Court | leader calls each line |', '| River | rowing crew answers in chorus |'],
             ['The Court row reports the court (S9001).',
              'The River row reports the river (S9002).']),
  evid={'S9001': E1, 'S9002': E2},
  expect=dict(rc=1, keys=[('UNSUPPORTED-CELL', 'Court', 'practice')], scoped=1))

C(id='A3', kind='attack', note='row bound only by a line carrying no S-id and no path',
  text=entry(REC, CAP3, '|---|---|---|', [COURT], ['The Court row reports the court.']),
  evid={'S9001': E1}, expect=dict(rc=1, keys=[('UNBOUND-ROW', 'Court', '')], scoped=1))

C(id='A4', kind='attack', note='binding line placed after a second blank-separated paragraph',
  text=entry(REC, CAP3, '|---|---|---|', [COURT],
             ['Notes without ids.', '', 'The Court row reports the court (S9001).']),
  evid={'S9001': E1}, expect=dict(rc=1, keys=[('UNBOUND-ROW', 'Court', '')], scoped=1))

C(id='A5', kind='attack', note='binding cites an S-id with no capture file',
  text=entry(REC, CAP3, '|---|---|---|', [COURT],
             ['The Court row reports the court (S9001).',
              'The Court row also reports the court (S9999).']),
  evid={'S9001': E1}, expect=dict(rc=1, keys=[('NO-CAPTURE', 'S9999', '')], scoped=1))

C(id='A6', kind='attack', note='path cite 99-120 in a 2-line support file (outside range)',
  text=entry(REC, '| tradition | practice |', '|---|---|',
             ['| Loom | weavers sing slow |'],
             ['The Loom row restates `x/ref.md:99-120`.']),
  evid={}, root=True,
  expect=dict(rc=1, keys=[('UNSUPPORTED-CELL', 'Loom', 'practice')], scoped=1,
              best={('UNSUPPORTED-CELL', 'Loom', 'practice'): (0, 3)}))

C(id='A7', kind='attack', note='trailing spaces must not hide an unsupported cell',
  text=trail(entry(REC, '| tradition | reward |', '|---|---|',
                   ['| Court | singer receives zebra quantum |'],
                   ['The Court row reports the court (S9001).'])),
  evid={'S9001': E1},
  expect=dict(rc=1, keys=[('UNSUPPORTED-CELL', 'Court', 'reward')], scoped=1,
              words={('UNSUPPORTED-CELL', 'Court', 'reward'): ['quantum', 'zebra']}))

C(id='A8', kind='attack', note='leading spaces must not hide an unsupported cell',
  text=lead(entry(REC, '| tradition | reward |', '|---|---|',
                  ['| Court | singer receives zebra quantum |'],
                  ['The Court row reports the court (S9001).'])),
  evid={'S9001': E1},
  expect=dict(rc=1, keys=[('UNSUPPORTED-CELL', 'Court', 'reward')], scoped=1,
              words={('UNSUPPORTED-CELL', 'Court', 'reward'): ['quantum', 'zebra']}))

C(id='A9', kind='attack', note='CRLF must not hide an unsupported cell',
  raw=entry(REC, '| tradition | reward |', '|---|---|',
            ['| Court | singer receives zebra quantum |'],
            ['The Court row reports the court (S9001).']).replace('\n', '\r\n').encode(),
  evid={'S9001': E1},
  expect=dict(rc=1, keys=[('UNSUPPORTED-CELL', 'Court', 'reward')], scoped=1,
              words={('UNSUPPORTED-CELL', 'Court', 'reward'): ['quantum', 'zebra']}))

C(id='A10', kind='attack', note='capture path is a directory: contract says NO-CAPTURE (rc 1)',
  text=entry(REC, '| tradition | practice |', '|---|---|',
             ['| River | leader calls each line |'],
             ['The River row reports the river (S9001).',
              'The River row also reports the river (S9002).']),
  evid={'S9002': E2}, evdirs=['S9001.txt'],
  expect=dict(rc=1, keys=[('NO-CAPTURE', 'S9001', '')], scoped=1))

# ---------------------------------------------------------------- contract probes (residuals)
C(id='G1', kind='gap', note='table inside a ``` fence with a matching caption line inside it',
  text=('# T\n\n## 1. Section\n\n```\nThe columns are filled from the recorded cases this entry cites.\n'
        '| tradition | singer |\n|---|---|\n| Court | zebra quantum |\n```\n\nText.\n'),
  evid={'S9001': E1}, expect=dict(rc=None, keys=None, scoped=None))

C(id='G2', kind='gap', note='heading used as caption (### Recorded cases): scoped at all?',
  text=entry('### Recorded cases', CAP3, '|---|---|---|',
             ['| Court | zebra quantum xylophone | nebula |'], []),
  evid={'S9001': E1}, expect=dict(rc=0, keys=[], scoped=0))

C(id='G3', kind='gap', note='GFM table without outer pipes: scoped at all?',
  text=('# T\n\n## 1. Section\n\n' + REC + '\n\ntradition | singer | limit\n--- | --- | ---\n'
        'Court | zebra quantum xylophone | nebula\n\nThe Court row reports the court (S9001).\n'),
  evid={'S9001': E1}, expect=dict(rc=0, keys=[], scoped=0))

C(id='A11', kind='attack', note='supported cell carrying a real URL link (markup tokens counted)',
  text=entry(REC, CAP3, '|---|---|---|',
             ['| Court | [singer](https://example.org/wiki/Singer) receives gifts | '
              'criticism of the chief is licensed |'],
             ['The Court row reports the court (S9001).']),
  evid={'S9001': E1}, expect=dict(rc=1, keys=[('UNSUPPORTED-CELL', 'Court', 'singer')], scoped=1))

C(id='A12', kind='attack', note='two-token label bound by a source mentioning only one token',
  text=entry(REC, '| tradition | practice |', '|---|---|',
             ['| Court drums | oriki held in the box |'],
             ['The drums row reports the drums (S9004).']),
  evid={'S9004': E4}, expect=dict(rc=0, keys=[], scoped=1))


def key(f):
    i = f.get('id')
    if i in ('UNSUPPORTED-CELL', 'UNBOUND-ROW'):
        return (i, f.get('row'), f.get('col', '') if i == 'UNSUPPORTED-CELL' else '')
    if i == 'NO-CAPTURE':
        return (i, f.get('sid'), '')
    if i == 'NO-PATH':
        return (i, f.get('path'), '')
    return (str(i), '?', '?')


def build(cls, base):
    d = os.path.join(base, cls['id'])
    shutil.rmtree(d, ignore_errors=True)
    ev = os.path.join(d, 'ev')
    os.makedirs(ev)
    for k, v in cls.get('evid', {}).items():
        with open(os.path.join(ev, k + '.txt'), 'w', encoding='utf-8') as fh:
            fh.write(v)
    for name in cls.get('evdirs', []):
        os.makedirs(os.path.join(ev, name))
    rt = os.path.join(d, 'root')
    os.makedirs(os.path.join(rt, 'corpus/knowledge/x'))
    with open(os.path.join(rt, 'corpus/knowledge/x/ref.md'), 'w', encoding='utf-8') as fh:
        fh.write(REF_MD)
    ent = os.path.join(d, 'entry.md')
    if cls.get('raw') is not None:
        with open(ent, 'wb') as fh:
            fh.write(cls['raw'])
    else:
        with open(ent, 'w', encoding='utf-8') as fh:
            fh.write(cls['text'])
    args = ['--entry', ent, '--evidence', ev]
    if cls.get('root'):
        args += ['--root', rt]
    args.append('--json')
    return args


def run(prog, args):
    p = subprocess.run([sys.executable, '-B', prog] + args,
                       capture_output=True, text=True, timeout=120)
    tb = 'Traceback (most recent call last)' in (p.stdout + p.stderr)
    return p, tb


def parse(p):
    try:
        js = json.loads(p.stdout)
        fs = js['findings']
        return js, fs, sorted({key(f) for f in fs}), None
    except Exception as e:  # noqa: BLE001 - any malformed output is the finding
        return None, None, None, f'{type(e).__name__}: {e}'


def classify(cls, p, tb, js, fs, got):
    exp = cls['expect']
    if cls['kind'] == 'gap':
        return 'CONTRACT-GAP', 'contract silent/ambiguous'
    if tb:
        return ('FALSE-GREEN' if exp['rc'] == 1 else 'OVERREFUSAL'), 'traceback'
    if js is None:
        if p.returncode == 2:
            return 'OVERREFUSAL', 'rc=2 refusal instead of findings'
        return ('FALSE-GREEN' if exp['rc'] == 1 else 'OVERREFUSAL'), 'json-unparseable'
    if exp.get('scoped') is not None and js.get('scoped_tables') != exp['scoped']:
        if exp['scoped'] == 1 and js.get('scoped_tables') == 0:
            return 'FALSE-GREEN', 'table not scoped'
        return ('OVERREFUSAL' if exp['scoped'] == 0 else 'FALSE-GREEN'), 'scoped mismatch'
    want = sorted(set(exp['keys']))
    ok = p.returncode == exp['rc'] and got == want and len(fs) == len(got)
    detail = ''
    for k, w in exp.get('words', {}).items():
        f = next((f for f in fs if key(f) == k), None)
        gw = sorted(f.get('words', [])) if f else None
        ok = ok and gw == sorted(w)
        detail += f' words={gw}'
    for k, (b, t) in exp.get('best', {}).items():
        f = next((f for f in fs if key(f) == k), None)
        ok = ok and f is not None and f.get('best') == b and f.get('total') == t
        detail += f' best/total={f.get("best") if f else None}/{f.get("total") if f else None}'
    if ok:
        return 'OK', detail.strip()
    if p.returncode == 0 and not fs:
        return 'FALSE-GREEN', 'expected findings, got clean'
    if exp['rc'] == 0:
        return 'OVERREFUSAL', 'expected clean, got findings/rc'
    if p.returncode == 2:
        return 'OVERREFUSAL', 'rc=2 instead of a finding'
    return 'FALSE-GREEN', 'wrong finding set'


def sweep(tool, ref, lane):
    ev = sorted(glob.glob(os.path.join(lane, 'reports/round-*/evidence')))
    files = sorted(glob.glob(os.path.join(lane, 'corpus/knowledge/**/*.md'), recursive=True))
    bad = []
    n_rc = {0: 0, 1: 0, 2: 0, 'other': 0}
    n_tb = n_json = n_div = n_scoped = 0
    for f in files:
        args = ['--entry', f, '--json', '--root', lane]
        for d in ev:
            args += ['--evidence', d]
        p, tb = run(tool, args)
        n_tb += tb
        if p.returncode in n_rc:
            n_rc[p.returncode] += 1
        else:
            n_rc['other'] += 1
        js, fs, got, err = parse(p)
        if err:
            n_json += 1
            bad.append((f, f'json: {err} rc={p.returncode}'))
            continue
        n_scoped += js.get('scoped_tables', 0)
        if p.returncode == 2:
            bad.append((f, f'rc=2 {p.stdout.strip().splitlines()[:1]}'))
        if ref:
            q, qtb = run(ref, args)
            qjs, qfs, qgot, qerr = parse(q)
            if qerr or qtb:
                n_div += 1
                bad.append((f, f'ref-fail rc={q.returncode} tb={qtb} err={qerr}'))
            elif qgot != got or qjs.get('scoped_tables') != js.get('scoped_tables'):
                n_div += 1
                bad.append((f, f'DIVERGE tool={got} scoped={js.get("scoped_tables")} '
                               f'ref={qgot} scoped={qjs.get("scoped_tables")}'))
    print(f'SWEEP files={len(files)} evidence={len(ev)} rc0={n_rc[0]} rc1={n_rc[1]} '
          f'rc2={n_rc[2]} rcother={n_rc["other"]} traceback={n_tb} jsonbad={n_json} '
          f'diverge={n_div} scoped_total={n_scoped}')
    for f, why in bad[:20]:
        print(f'SWEEP-BAD {os.path.relpath(f, lane)} {why}')
    return len(bad)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--work', default=DEFWORK)
    ap.add_argument('--only')
    ap.add_argument('--sweep', action='store_true')
    ap.add_argument('--no-ref', action='store_true')
    a = ap.parse_args()
    if not os.path.isfile(TOOL):
        print(f'TOOL-MISSING {TOOL}')
        return 2
    import hashlib
    print(f'TOOL-SHA256 {hashlib.sha256(open(TOOL, "rb").read()).hexdigest()}')
    print(f'REF-SHA256 {hashlib.sha256(open(REF, "rb").read()).hexdigest()}')
    work = os.path.abspath(a.work)
    os.makedirs(work, exist_ok=True)
    only = set(a.only.split(',')) if a.only else None
    tally = {'OK': 0, 'OVERREFUSAL': 0, 'FALSE-GREEN': 0, 'CONTRACT-GAP': 0}
    ntb = 0
    n = 0
    for cls in CLASSES:
        if only and cls['id'] not in only:
            continue
        n += 1
        args = build(cls, work)
        p, tb = run(TOOL, args)
        ntb += tb
        js, fs, got, err = parse(p)
        verdict, detail = classify(cls, p, tb, js, fs, got)
        tally[verdict] += 1
        obs = f'rc={p.returncode} scoped={js.get("scoped_tables") if js else None} got={got}'
        if err:
            obs += f' err={err}'
        refobs = ''
        if not a.no_ref:
            q, qtb = run(REF, args)
            qjs, qfs, qgot, qerr = parse(q)
            refobs = (f' ref_rc={q.returncode} ref_scoped={qjs.get("scoped_tables") if qjs else None}'
                      f' ref_got={qgot}' + (f' ref_tb={qtb}' if qtb else '')
                      + (f' ref_err={qerr}' if qerr else ''))
            if qjs and js and (qgot != got or qjs.get('scoped_tables') != js.get('scoped_tables')):
                refobs += ' DIVERGE'
        print(f'CLASS {cls["id"]} {verdict} expect_rc={cls["expect"]["rc"]} {obs}{refobs} '
              f'| {cls["note"]} {detail}')
    print(f'CRITIC-O100 classes={n} ok={tally["OK"]} overrefusal={tally["OVERREFUSAL"]} '
          f'falsegreen={tally["FALSE-GREEN"]} gap={tally["CONTRACT-GAP"]} traceback={ntb}')
    bad = 0
    if a.sweep:
        bad = sweep(TOOL, None if a.no_ref else REF, LANE)
    return 0 if (tally['OVERREFUSAL'] == 0 and tally['FALSE-GREEN'] == 0 and ntb == 0 and bad == 0) else 1


if __name__ == '__main__':
    sys.exit(main())
