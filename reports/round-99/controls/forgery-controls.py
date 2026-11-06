#!/usr/bin/env python3
"""Round-99 claim-O forgery and feasibility controls (L1 KotodamaR99, run before any seat).

Each fixture is the lane tree at --rev (git archive) plus the uncommitted reports/round-99/
directory, with tools/check-advance-evidence.py replaced by a patched copy of v10. The frozen
counter reports/round-99/predispatch.py then runs over the fixture; only its O-leg lines and the
verdict line are kept (C legs are not under test here).

  F-O-SHA    v10 + one comment line: identity changes, behaviour does not.
             Expected: O0 PASS; O1, O2, O4 FAIL.
  F-O-LOOSE  blanket loosening: v10 with the h2 combining-mark refusal disabled and the
             HEADING-NUMBER refusal disabled (over-refusals go away by deleting protection).
             Expected: O2 FAIL (CM1/CMW2 survive), even though the six round-99 controls are CLEAN.
  P-O-FEAS   feasibility (not a candidate): v10 with the heading mark check narrowed to Mn/Me
             marks whose base character is ASCII and the HEADING-NUMBER refusal disabled.
             Shows the O2 target is reachable without loosening; selftest and mutation legs are
             expected to fail (no pins, no driver).

Usage: python3 -B forgery-controls.py --lane <lane> --rev <40hex> --work <scratch> --out <dir>
"""
import argparse
import os
import shutil
import subprocess
import sys

COMB_V10 = "if any(unicodedata.category(_c)[0] == 'M' for _c in _h):"
NUM_V10 = "problems.append('h2 heading numbering token is non-ASCII numerals or full stop (HEADING-NUMBER)')"


def patched(src, kind):
    t = src
    if kind == 'F-O-SHA':
        return t + '\n# round-99 forgery control: identity-only change\n'
    assert t.count(COMB_V10) == 1 and t.count(NUM_V10) == 1
    if kind == 'F-O-LOOSE':
        t = t.replace(COMB_V10, 'if False:')
    elif kind == 'P-O-FEAS':
        t = t.replace(COMB_V10, "if any(unicodedata.category(_c) in ('Mn', 'Me') and _i > 0 and ord(_h[_i - 1]) < 128 "
                                "for _i, _c in enumerate(_h)):")
    t = t.replace(NUM_V10, 'pass')
    return t


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--lane', required=True)
    ap.add_argument('--rev', required=True)
    ap.add_argument('--work', required=True)
    ap.add_argument('--out', required=True)
    a = ap.parse_args()
    lane, work, out = map(os.path.abspath, (a.lane, a.work, a.out))
    if work.startswith('/tmp'):
        print('refused: --work under /tmp')
        return 2
    os.makedirs(out, exist_ok=True)
    src = open(os.path.join(lane, 'tools/check-advance-evidence.py'), encoding='utf-8').read()
    summary = []
    for kind in ('F-O-SHA', 'F-O-LOOSE', 'P-O-FEAS'):
        root = os.path.join(work, kind, 'tree')
        shutil.rmtree(os.path.join(work, kind), ignore_errors=True)
        os.makedirs(root)
        arc = subprocess.run(['git', '-C', lane, 'archive', a.rev], capture_output=True, check=True).stdout
        subprocess.run(['tar', '-x', '-C', root], input=arc, check=True)
        shutil.rmtree(os.path.join(root, 'reports/round-99'), ignore_errors=True)
        shutil.copytree(os.path.join(lane, 'reports/round-99'), os.path.join(root, 'reports/round-99'),
                        ignore=shutil.ignore_patterns('__pycache__'))
        with open(os.path.join(root, 'tools/check-advance-evidence.py'), 'w', encoding='utf-8') as f:
            f.write(patched(src, kind))
        cw = os.path.join(work, kind, 'counter')
        os.makedirs(cw)
        p = subprocess.run([sys.executable, '-B', os.path.join(lane, 'reports/round-99/predispatch.py'),
                            '--root', root, '--work', cw, '--base-rev', a.rev],
                           capture_output=True, text=True)
        keep = [l for l in p.stdout.splitlines() if l.startswith('LEG O') or l.startswith('PREDISPATCH-99')]
        body = f'FIXTURE {kind} rev={a.rev} counter-rc={p.returncode}\n' + '\n'.join(keep) + '\n'
        with open(os.path.join(out, kind + '.txt'), 'w', encoding='utf-8') as f:
            f.write(body)
        legs = ' '.join(l.split()[1] + '=' + l.split()[2] for l in keep if l.startswith('LEG O'))
        summary.append(f'{kind}: {legs}')
        shutil.rmtree(os.path.join(work, kind), ignore_errors=True)
    with open(os.path.join(out, 'summary.txt'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(summary) + '\n')
    print('\n'.join(summary))
    return 0


if __name__ == '__main__':
    sys.exit(main())
