#!/usr/bin/env python3
"""Round-88 pre-dispatch controls, run and committed BEFORE the claim freeze.

1. The inherited frozen r87 counter (membership semantics) is scored against the
   honest auditor and every committed counterfeit: red-before evidence that the
   inherited battery accepts a label shotgun, an extra-id report and a
   filename-only oracle at 12/12.
2. The new 13-case exact-set battery is scored at the base revision, where the
   comparator tools/check-finding-sets.py does not exist.
3. The depth claim's no-work control is measured at the base revision.
Writes reports/round-88/pre-dispatch.json.
"""
import json
import os
import pathlib
import subprocess
import sys

ROOT = pathlib.Path(__file__).resolve().parents[2]
BASE = '4956282281dac1306cfbe59523e46dde99749d75'
WORK = pathlib.Path(os.environ.get('HYAKU_WORK') or '/fast/scratch/hyaku/kotodama-r88/L1')
CONTROLS = ['constant-pass', 'shotgun-all-labels', 'extra-id', 'filename-only']


def run(args):
    p = subprocess.run([sys.executable, '-B'] + args, capture_output=True, text=True, cwd=str(ROOT),
                       env=dict(os.environ, KOTODAMA_ROOT=str(ROOT)))
    try:
        body = json.loads(p.stdout)
    except ValueError:
        body = None
    return dict(command=['python3', '-B'] + args, rc=p.returncode, stdout=p.stdout, stderr=p.stderr, body=body)


def main():
    if not WORK.is_dir():
        print('PRE_DISPATCH_ERROR work must exist', file=sys.stderr)
        return 2
    out = dict(round=88, base=BASE, work=str(WORK), inherited_r87_counter={}, exact_set_counter={}, depth_control={})
    out['inherited_r87_counter']['honest'] = run(['reports/round-87/measure87.py', '--root', '.',
                                                  '--revision', BASE, '--work', str(WORK)])
    for name in CONTROLS:
        out['inherited_r87_counter'][name] = run(['reports/round-87/measure87.py', '--root', '.', '--revision', BASE,
                                                  '--candidate', f'reports/round-88/controls/{name}.py',
                                                  '--work', str(WORK)])
    for name, rec in out['inherited_r87_counter'].items():
        rec['score'] = f"{rec['body']['passed']}/{rec['body']['total']}" if rec['body'] else 'no-json'
    out['exact_set_counter']['at-base'] = run(['reports/round-88/measure88.py', '--root', '.', '--base', BASE,
                                               '--lands', BASE, '--claim', 'O', '--work', str(WORK)])
    out['depth_control']['at-base'] = run(['reports/round-88/measure88.py', '--root', '.', '--base', BASE,
                                           '--lands', BASE, '--claim', 'D', '--work', str(WORK)])
    target = ROOT / 'reports' / 'round-88' / 'pre-dispatch.json'
    target.write_text(json.dumps(out, indent=2, sort_keys=True) + '\n')
    summary = {k: (v.get('score') if 'score' in v else v['rc']) for k, v in out['inherited_r87_counter'].items()}
    print(json.dumps(dict(written=str(target), inherited=summary,
                          exact_o_rc=out['exact_set_counter']['at-base']['rc'],
                          depth_rc=out['depth_control']['at-base']['rc']), indent=2))
    return 0


if __name__ == '__main__':
    sys.exit(main())
