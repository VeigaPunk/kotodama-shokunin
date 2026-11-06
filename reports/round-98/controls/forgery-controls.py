#!/usr/bin/env python3
"""Round-98 pre-freeze forgery and positive controls for the frozen counter
reports/round-98/predispatch.py (built and run by the L1 before any seat ran).

Each fixture is `git archive <rev>` of the lane into <work>/<name>/ (a plain tree; the counter's
C3 reads the base registry through --base-registry because a plain tree is not a git work tree),
plus the round-98 control files, plus the fixture's forgery. Then the counter runs once per
fixture and its full stdout is written to <out>/<name>.txt.

Fixtures (expected verdicts are declared here, before the runs):
  F-O-SHA     v9 + one comment line (sha differs, no new refusal).
              expect O0 PASS, O1 FAIL, O2 FAIL, O5 FAIL.
  F-C-JUNK    padded junk entry (frozen topic line, six phrase-bearing h2, a 5x3 table, >= 12000 B),
              four junk registry rows S994-S997 (tier A, mined, opened 2026-11-05, used-by the entry,
              anchor carrying a quote), a manifest whose captures exist with matching sha256 but do
              not contain the quote, and an in-place tier edit of S992 (A -> B).
              expect C1 PASS, C2 PASS, C6 PASS, C3 FAIL (illegal in-place tier edit), C7 FAIL
              (quote-count=0 for every id).
  F-C-DUP     as F-C-JUNK without the tier edit, captures containing the quote twice.
              expect C3 PASS, C7 FAIL (quote-count=2).
  P-C-BOUND   positive control: as F-C-DUP but each capture contains the quote exactly once and
              S992 changes only its status cell in place (mined -> queued, allowed by rule 2).
              expect C3 PASS (in-place=1 illegal=0), C7 PASS. (C5 and C4 may fail; the fixture
              does not update the index. A PASS here shows C7 and C3 are not blanket refusals;
              it also shows fabricated captures pass C7, which is why C9 exists.) expect C9 FAIL.
  F-C-REOPEN  P-C-BOUND plus a reopen.json whose urls miss the row (2 ids) or count 2 (2 ids).
              expect C9 FAIL.
  P-C-REOPEN  P-C-BOUND plus a well-formed reopen.json for all four ids. expect C9 PASS:
              C9 is a non-author attestation leg; its bytes are only as good as the seat that
              writes them, and the closure re-opens a sample itself.
Usage: python3 -B forgery-controls.py --root <lane> --rev <base rev> --work <scratch> --out <dir>
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

ENTRY = 'corpus/knowledge/linguistics/toast-drinking-speech-formulae.md'
TOPIC = ('- topic: toasts and drinking-speech formulae: the toast as a speech act over a shared cup — '
         "health-drinking, libation and the pledge; the toastmaster's office and the order of a "
         'toast sequence; the drinking oath and the boast-cup; refusal, reciprocity and the '
         'penalty cup; and the design procedure for a fictional drinking rite whose words stay '
         'tied to its hosts, guests, cups and occasions')
CONTROL_FILES = ['reports/round-98/predispatch.py', 'reports/round-98/controls/battery98.py',
                 'reports/round-98/controls/battery98.sha256',
                 'reports/round-98/controls/battery98-control-v9.txt']
IDS = ['S994', 'S995', 'S996', 'S997']


def sh(cmd, **kw):
    return subprocess.run(cmd, capture_output=True, **kw)


def export(root, rev, dst):
    os.makedirs(dst, exist_ok=True)
    a = sh(['git', '-C', root, 'archive', rev])
    sh(['tar', '-x', '-C', dst], input=a.stdout, check=True)
    for f in CONTROL_FILES:
        p = os.path.join(dst, f)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(os.path.join(root, f), 'rb') as s, open(p, 'wb') as d:
            d.write(s.read())


def junk_entry():
    heads = ['## Toast formula', '## Health-drinking', '## The toastmaster', '## Libation',
             '## Toast sequence', '## Drinking oath']
    filler = ('Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor '
              'incididunt ut labore et dolore magna aliqua. ') * 22
    parts = ['# Toasts', '', TOPIC, '']
    for h in heads:
        parts += [h, '', filler + ' ' + ' '.join(IDS), '']
    parts += ['| a | b | c |', '|---|---|---|'] + [f'| {i} | x | y |' for i in range(5)] + ['']
    return '\n'.join(parts)


def quote_of(i):
    return f'the cup passes to the left and the host names the guest {i}'


def write_reopen(d, mode):
    # bad: url not in the row's source cell for two ids, quote_count 2 for the other two.
    out = []
    for n, i in enumerate(IDS):
        url = f'https://junk.example.org/{i}'
        cnt = 1
        if mode == 'bad':
            if n < 2:
                url = 'https://elsewhere.example.org/x'
            else:
                cnt = 2
        out.append(dict(id=i, url=url, http=200, fresh_sha256='0' * 64, quote_count=cnt))
    p = os.path.join(d, '.ufo/waves/round-98/w1/stage/ReviewerC98')
    os.makedirs(p, exist_ok=True)
    json.dump(out, open(os.path.join(p, 'reopen.json'), 'w', encoding='utf-8'), indent=1)


def write_fixture(d, cap_mode, s992_mode):
    with open(os.path.join(d, ENTRY), 'w', encoding='utf-8') as f:
        f.write(junk_entry())
    reg = os.path.join(d, 'corpus/SOURCES.md')
    text = open(reg, encoding='utf-8').read()
    lines = text.split('\n')
    if s992_mode != 'none':
        for n, l in enumerate(lines):
            if re.match(r'^\| S992 \|', l):
                c = l.split('|')
                if s992_mode == 'tier':
                    c[4] = ' B '
                elif s992_mode == 'status':
                    c[8] = ' queued '
                lines[n] = '|'.join(c)
    last = max(n for n, l in enumerate(lines) if re.match(r'^ {0,3}\| *S[0-9]{3,} *\|', l))
    rows = [f'| {i} | Junk source {i} — https://junk.example.org/{i} | paper | A | toast | body text; '
            f'exact locator: "{quote_of(i)}" | junk teaches cell | mined | 2026-11-05 | 180d | {ENTRY} |'
            for i in IDS]
    lines[last + 1:last + 1] = rows
    open(reg, 'w', encoding='utf-8').write('\n'.join(lines))
    ev = os.path.join(d, 'reports/round-98/evidence')
    os.makedirs(ev, exist_ok=True)
    man = []
    for i in IDS:
        body = 'unrelated capture text about something else entirely. '
        if cap_mode == 'once':
            body += quote_of(i) + '.'
        elif cap_mode == 'twice':
            body += quote_of(i) + '. again: ' + quote_of(i) + '.'
        fn = f'{i}.txt'
        open(os.path.join(ev, fn), 'w', encoding='utf-8').write(body)
        h = hashlib.sha256(body.encode('utf-8')).hexdigest()
        man.append(dict(id=i, quote=quote_of(i), quote_capture=fn,
                        captures=[dict(file=fn, sha256=h)]))
    json.dump(man, open(os.path.join(ev, 'manifest.json'), 'w', encoding='utf-8'), indent=1)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True)
    ap.add_argument('--rev', required=True)
    ap.add_argument('--work', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    root, work, out = map(os.path.abspath, (a.root, a.work, a.out))
    if work.startswith('/tmp'):
        print('refused: --work under /tmp')
        return 2
    os.makedirs(out, exist_ok=True)
    os.makedirs(work, exist_ok=True)
    base_reg = os.path.join(work, 'base-SOURCES.md')
    open(base_reg, 'wb').write(sh(['git', '-C', root, 'show', f'{a.rev}:corpus/SOURCES.md'], check=True).stdout)
    fixtures = [('F-O-SHA', None), ('F-C-JUNK', ('none', 'tier')), ('F-C-DUP', ('twice', 'none')),
                ('P-C-BOUND', ('once', 'status')), ('F-C-REOPEN', ('once', 'status', 'bad')),
                ('P-C-REOPEN', ('once', 'status', 'good'))]
    for name, spec in fixtures:
        d = os.path.join(work, name)
        export(root, a.rev, d)
        if name == 'F-O-SHA':
            t = os.path.join(d, 'tools/check-advance-evidence.py')
            open(t, 'a', encoding='utf-8').write('# round-98 forgery control: comment only\n')
        else:
            write_fixture(d, *spec[:2])
            if len(spec) > 2:
                write_reopen(d, spec[2])
        cw = os.path.join(work, name + '-counter')
        os.makedirs(cw, exist_ok=True)
        p = sh([sys.executable, '-B', os.path.join(d, 'reports/round-98/predispatch.py'), '--root', d,
                '--work', cw, '--base-rev', a.rev, '--base-registry', base_reg], text=True)
        txt = f'FIXTURE {name} rev={a.rev} rc={p.returncode}\n' + p.stdout + p.stderr
        open(os.path.join(out, name + '.txt'), 'w', encoding='utf-8').write(txt)
        legs = ' '.join(re.findall(r'^LEG (\S+ \S+)', p.stdout, re.M))
        print(f'{name} rc={p.returncode} {legs}')
    return 0


if __name__ == '__main__':
    sys.exit(main())
