#!/usr/bin/env python3
"""mutants100 — mutation driver for tools/check-table-support.py (kotodama round 100, claim O leg O4).

Each mutant is a (pattern, replacement, expected-match-count) triple applied to a scratch COPY of
the tool under test.  A pattern that matches a different number of times than declared is a
broken-pattern mutant (the driver could not express the defect); it is reported separately and
never counted as killed.

Kill oracle (either suffices, and the driver says which):
  * battery100 rc != 0 on the mutant  (python3 -B battery100.py --tool <mutant> --work <dir>)
  * the mutant's own selftest rc != 0 (python3 -B <mutant> --selftest --work <dir>), used only
    when the pristine tool's selftest passes (otherwise the selftest oracle is unavailable)

Usage: mutants100.py --tool <path> --work <dir>
First output line: DRIVER-SHA256 <sha256 of this file's bytes>
Summary line:      MUTATION-SCORE: <killed>/<total> killed, <survived> survived, <broken> broken-pattern
"""
import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys

LANE = '/home/vgpnk/Projects/shokunin/kotodama-shokunin'
BATTERY = os.path.join(LANE, 'reports/round-100/controls/battery100.py')

# (id, clause, pattern, replacement, expected matches)
MUTANTS = [
    # --- window size -------------------------------------------------------
    ('W1', 'window 80 -> 79', r'\bWINDOW = 80\b', 'WINDOW = 79', 1),
    ('W2', 'window 80 -> 81', r'\bWINDOW = 80\b', 'WINDOW = 81', 1),
    ('W3', 'window 80 -> 10000', r'\bWINDOW = 80\b', 'WINDOW = 10000', 1),
    # --- threshold arithmetic ---------------------------------------------
    ('A1', 'support 3/4 -> strict >', r'if best \* 4 < len\(stems\) \* 3:',
     'if best * 4 <= len(stems) * 3:', 1),
    ('A2', 'support 3/4 -> 2/3', r'if best \* 4 < len\(stems\) \* 3:',
     'if best * 3 < len(stems) * 2:', 1),
    ('A3', 'support 3/4 -> 1/2', r'if best \* 4 < len\(stems\) \* 3:',
     'if best * 2 < len(stems) * 1:', 1),
    # --- stem rules --------------------------------------------------------
    ('S1', 'stem ies->y rule removed', r"if len\(t\) > 4 and t\.endswith\('ies'\):", 'if False:', 1),
    ('S2', 'stem es-after-s/x/z/ch/sh rule removed',
     r"if len\(t\) > 4 and t\.endswith\('es'\) and \(t\[-3\] in 'sxz' or t\[-4:-2\] in \('ch', 'sh'\)\):",
     'if False:', 1),
    ('S3', 'stem trailing-s rule removed',
     r"if len\(t\) > 3 and t\.endswith\('s'\) and not t\.endswith\('ss'\):", 'if False:', 1),
    # --- stoplist ----------------------------------------------------------
    ('P1', 'STOP emptied', r"STOP = set\('''[\s\S]*?'''\.split\(\)\)", 'STOP = set()', 1),
    ('P2', "STOP loses 'them' (a battery case relies on it)", r'\bthem\b(?=\s+themselves)', '', 1),
    # --- label tokens / binding -------------------------------------------
    ('L1', 'label-token min length 3 -> 4',
     r"if len\(t\) >= 3 and t not in STOP and t != 'and'",
     "if len(t) >= 4 and t not in STOP and t != 'and'", 1),
    ('L2', 'label-token min length 3 -> 2',
     r"if len\(t\) >= 3 and t not in STOP and t != 'and'",
     "if len(t) >= 2 and t not in STOP and t != 'and'", 1),
    ('L3', 'label binding -> substring instead of token equality', r'if lw & tokset',
     'if any(t in x for t in lw for x in tokset)', 1),
    ('L4', "'and' exclusion removed from label tokens", r" and t != 'and'", '', 1),
    # --- caption scope -----------------------------------------------------
    ('C1', 'caption regex widened to any "recorded"',
     r"if not re\.search\(r'\\brecorded cases\?\\b', cap, re\.I\):",
     "if not re.search(r'recorded', cap, re.I):", 1),
    ('C2', 'caption regex narrowed to singular "recorded case"',
     r"if not re\.search\(r'\\brecorded cases\?\\b', cap, re\.I\):",
     "if not re.search(r'\\brecorded case\\b', cap, re.I):", 1),
    ('C3', 'caption match case-sensitive', r', cap, re\.I\)', ', cap)', 1),
    ('C4', 'caption paragraph extent: one line only',
     r"while k >= 0 and lines\[k\]\.strip\(\) and not HEAD\.match\(lines\[k\]\) and not lines\[k\]\.strip\(\)\.startswith\('\|'\):",
     "while k >= 0 and lines[k].strip() and not HEAD.match(lines[k]) and not lines[k].strip().startswith('|') and not cap:",
     1),
    ('C5', 'caption paragraph emptied (scope lost)', 
     r"while k >= 0 and lines\[k\]\.strip\(\) and not HEAD\.match\(lines\[k\]\) and not lines\[k\]\.strip\(\)\.startswith\('\|'\):",
     'while False:', 1),
    # --- binding extent / union -------------------------------------------
    ('B1', 'binding paragraph crosses blank lines',
     r"while m < n and lines\[m\]\.strip\(\) and not HEAD\.match\(lines\[m\]\) and not lines\[m\]\.strip\(\)\.startswith\('\|'\):",
     "while m < n and not HEAD.match(lines[m]) and not lines[m].strip().startswith('|'):", 1),
    ('B2', 'support pooled across rows (union)',
     r'support = \[t for ts, _ in bound for t in ts\]',
     'support = [t for ts, _ in bound for t in ts] + [t for _ts, _c in texts_for_line for t in _ts]',
     1),
    # --- NO-CAPTURE / NO-PATH ---------------------------------------------
    ('N1', 'NO-CAPTURE dedup removed', r'if sid not in seen_sid:', 'if True:', 1),
    ('N2', 'NO-PATH finding skipped',
     r"findings\.append\(\{'id': 'NO-PATH', 'line': h \+ 1, 'path': p\}\)", 'pass', 1),
    ('N3', 'path line range off by one', r'src\[a - 1:b\]', 'src[a:b]', 1),
    ('N4', 'UNBOUND only when no line binds (citation requirement dropped)',
     r'if not bound or not any\(cited for _, cited in bound\):', 'if not bound:', 1),
    # --- rc mapping / error paths -----------------------------------------
    ('R1', 'rc 1 <-> 0', r'return 1 if f else 0', 'return 0 if f else 1', 1),
    ('R2', 'rc 2 -> 1 on every error path', r'return 2', 'return 1', 7),
    ('R3', 'TABLE_SUPPORT_ERROR text changed', r'TABLE_SUPPORT_ERROR', 'TABLE-SUPPORT-ERROR', 13),
    ('R4', 'traceback on a refused input (ToolError re-raised)',
     r"    except ToolError as e:\n        print\(f'TABLE_SUPPORT_ERROR \{e\}'\)\n        return 2",
     '    except ToolError as e:\n        raise', 1),
    ('R5', 'bad UTF-8 entry accepted (error path returns 0)',
     r"print\('TABLE_SUPPORT_ERROR entry is not valid UTF-8'\)\n            return 2",
     "print('TABLE_SUPPORT_ERROR entry is not valid UTF-8')\n            return 0", 1),
    # --- output shape ------------------------------------------------------
    ('J1', 'JSON key findings renamed', r"'findings': f", "'finding': f", 1),
    ('J2', 'JSON key scoped_tables renamed', r"'scoped_tables': s", "'scoped_table': s", 1),
    ('J3', 'header column name off by one',
     r'col = header\[ci\] if ci < len\(header\) else str\(ci\)',
     'col = header[ci - 1] if ci - 1 < len(header) else str(ci)', 1),
    # --- extra contract points --------------------------------------------
    ('A4', 'content-word min length 4 -> 3',
     r'if len\(t\) >= 4 and t not in STOP and t not in out:',
     'if len(t) >= 3 and t not in STOP and t not in out:', 1),
    ('W4', 'UNSUPPORTED-CELL words compared as words, not stems',
     r'absent = sorted\(\{w for w in words if stem\(w\) not in allstems\}\)',
     'absent = sorted({w for w in words if w not in allstems})', 1),
]


def sha256_file(path):
    return hashlib.sha256(open(path, 'rb').read()).hexdigest()


def apply_mutant(src, pattern, repl, expected):
    new, n = re.subn(pattern, lambda m: repl, src)
    if n != expected:
        return None, n
    if new == src:
        return None, n
    return new, n


def run(cmd, timeout=300):
    try:
        p = subprocess.run(cmd, capture_output=True, text=True, timeout=timeout)
        return p.returncode, p.stdout + p.stderr
    except subprocess.TimeoutExpired:
        return 124, 'TIMEOUT'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--tool', required=True)
    ap.add_argument('--work', required=True)
    a = ap.parse_args()
    tool = os.path.abspath(a.tool)
    work = os.path.abspath(a.work)
    if os.path.realpath(work).startswith('/tmp'):
        print('REFUSED --work must not live under /tmp')
        return 2
    print(f'DRIVER-SHA256 {sha256_file(os.path.abspath(__file__))}')
    print(f'TOOL-SHA256 {sha256_file(tool)}')
    print(f'BATTERY-SHA256 {sha256_file(BATTERY)}')
    os.makedirs(work, exist_ok=True)
    src = open(tool, encoding='utf-8').read()
    rc_p, _ = run([sys.executable, '-B', tool, '--selftest', '--work', os.path.join(work, 'pristine-sw')])
    selftest_ok = rc_p == 0
    print(f'SELFTEST-ORACLE {"available" if selftest_ok else "unavailable"} (pristine rc={rc_p})')
    killed = survived = broken = 0
    total = len(MUTANTS)
    for mid, clause, pattern, repl, expected in MUTANTS:
        d = os.path.join(work, mid)
        shutil.rmtree(d, ignore_errors=True)
        os.makedirs(d)
        new, n = apply_mutant(src, pattern, repl, expected)
        if new is None:
            broken += 1
            print(f'MUTANT {mid} BROKEN-PATTERN matches={n} expected={expected} :: {clause}')
            continue
        mp = os.path.join(d, 'tool.py')
        open(mp, 'w', encoding='utf-8').write(new)
        rc_b, out_b = run([sys.executable, '-B', BATTERY, '--tool', mp, '--work', os.path.join(d, 'bw')])
        fails = [l.split()[1] for l in out_b.splitlines() if l.startswith('CASE ') and ' FAIL ' in l]
        if rc_b != 0:
            killed += 1
            print(f'MUTANT {mid} KILLED-BY-BATTERY rc={rc_b} failing={",".join(fails)} :: {clause}')
            continue
        rc_s, _ = run([sys.executable, '-B', mp, '--selftest', '--work', os.path.join(d, 'sw')]) if selftest_ok else (0, '')
        if rc_s != 0:
            killed += 1
            print(f'MUTANT {mid} KILLED-BY-SELFTEST rc={rc_s} :: {clause}')
            continue
        survived += 1
        print(f'MUTANT {mid} SURVIVED battery-rc=0 selftest-rc=0 :: {clause}')
    print(f'MUTATION-SCORE: {killed}/{total} killed, {survived} survived, {broken} broken-pattern')
    return 0 if (survived == 0 and broken == 0 and killed == total) else 1


if __name__ == '__main__':
    sys.exit(main())
