#!/usr/bin/env python3
"""Round-100 forgery/feasibility controls for claim O, run by the L1 before any seat.

Builds candidate checkers that skip the claimed work in scratch, runs battery100 and the counter's
O3 historical replay over each, and writes one receipt per candidate under
reports/round-100/controls/forgery/. Usage:
  python3 -B forgery-controls.py --root <lane> --work <scratch dir, not /tmp>
"""
import argparse
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REF = os.path.join(HERE, 'feasibility', 'table_support_ref.py')

ALLCLEAN = '''import json, sys
print(json.dumps({"findings": [], "scoped_tables": 0}))
print("TABLE-SUPPORT: 0 finding(s) in 0 scoped table(s)", file=sys.stderr)
'''


def variants():
    ref = open(REF, encoding='utf-8').read()
    v = {'F-O-ALLCLEAN': ALLCLEAN}

    def sub(name, old, new):
        assert ref.count(old) == 1, (name, ref.count(old))
        v[name] = ref.replace(old, new)

    # no cell-support check: binding and capture checks only (an id-presence checker)
    sub('F-O-NOWORD', '                if best * 4 < len(stems) * 3:', '                if False:')
    # word presence anywhere in the row's support instead of co-location in one window
    sub('F-O-ANYWHERE', '                best = max((window_best(stems, t) for t in support), default=0)',
        '                best = sum(1 for s in stems if s in allstems)')
    # support pooled over every binding line of the table (row isolation lost)
    sub('F-O-UNION', '            bound = [(t, cited) for tokset, t, cited in texts_for_line if lw & tokset]',
        '            bound = [(t, cited) for tokset, t, cited in texts_for_line] if any(lw & ts for ts, _, _ in texts_for_line) else []')
    # caption scope widened to any "recorded" (over-refusal surface)
    sub('F-O-WIDE', "if not re.search(r'\\brecorded cases?\\b', cap, re.I):", "if not re.search(r'recorded', cap, re.I):")
    v['P-O-FEAS'] = ref
    return v


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True)
    ap.add_argument('--work', required=True)
    a = ap.parse_args()
    root, work = os.path.abspath(a.root), os.path.abspath(a.work)
    out = os.path.join(root, 'reports/round-100/controls/forgery')
    os.makedirs(out, exist_ok=True)
    bat = os.path.join(root, 'reports/round-100/controls/battery100.py')
    summary = []
    for name, code in variants().items():
        d = os.path.join(work, name)
        os.makedirs(d, exist_ok=True)
        tp = os.path.join(d, 'check-table-support.py')
        open(tp, 'w', encoding='utf-8').write(code)
        p = subprocess.run([sys.executable, '-B', bat, '--tool', tp, '--work', os.path.join(d, 'bat')],
                           capture_output=True, text=True)
        m = re.search(r'BATTERY-SUMMARY .*', p.stdout)
        fails = [l.split()[1] for l in p.stdout.splitlines() if l.startswith('CASE ') and ' FAIL ' in l]
        rec = p.stdout + f'BATTERY-RC {p.returncode}\n'
        open(os.path.join(out, name + '.txt'), 'w', encoding='utf-8').write(rec)
        summary.append(f'{name}: {m.group(0) if m else "no summary"} rc={p.returncode} failing={fails}')
    open(os.path.join(out, 'summary.txt'), 'w', encoding='utf-8').write('\n'.join(summary) + '\n')
    print('\n'.join(summary))


if __name__ == '__main__':
    sys.exit(main())
