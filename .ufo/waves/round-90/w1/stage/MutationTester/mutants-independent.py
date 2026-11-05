#!/usr/bin/env python3
"""Independent round-90 mutation probe (MutationTester seat).

Mutants here deliberately avoid every pattern used by the committed
reports/round-90/mutants.py list. Each is one single-removal of a hardening
that the committed list does not touch. A mutant is KILLED when the tool's own
--selftest exits non-zero; the failing case names are captured so a kill can be
attributed to a real selftest case rather than to an unrelated crash.

The graded bytes are never edited: the source is copied to --work, and the
source sha256 is re-read at the end to prove the copy was the only thing that
changed. No network. Run:
  python3 -B mutants-independent.py --root <tree-with-tools/> --work <existing-dir>
"""

import argparse
import hashlib
import json
import os
import subprocess
import sys

TOOL = 'tools/check-advance-evidence.py'

# (name, old, new, behaviour removed, selftest case that ought to catch it)
MUTANTS = [
    ('capture-fetched-date-off',
     "if fm.group(1) != as_of:",
     "if False:",
     "the committed capture must be fetched on the round date, not merely carry a "
     "well-formed ISO instant with an offset",
     "no case: every fixture uses fetched_at 2026-11-04 (the as_of), only the "
     "malformed prefix is tested"),
    ('capture-traversal-off',
     "if rel.startswith('/') or '..' in rel.split('/'):",
     "if False:",
     "a capture path may not be absolute and may not climb out with '..'",
     "no case: the only path fixture is 'reports/round-90/elsewhere/', which the "
     "capture-dir confinement already refuses"),
    ('table-data-row-count-off',
     "data = max(0, len(rows) - 2)",
     "data = max(0, len(rows))",
     "the header row and the |---| separator are not data rows",
     "'entry table too small' / 'entry table too few columns' / 'positive entry'"),
    ('window-upper-bound-off',
     "if not (lo < d <= hi):",
     "if not (lo < d):",
     "a recheck beyond --max-days is not an advance",
     "no case: the only window fixture ('near.md' 2027-01-01) probes the floor"),
    ('newids-status-off',
     "if status != 'mined':",
     "if False:",
     "a cited new id must be status mined, not merely tier A/B",
     "no case: the only non-mined row ('lands_uncited' S013) is tier C and "
     "uncited, so it is out of scope for a different reason"),
    ('advanced-single-row-off',
     "if len(lands.get(rid, [])) != 1:",
     "if not lands.get(rid, []):",
     "a population id must resolve to exactly one lands row; two rows are a shadow",
     "'shadow duplicate id' (but SHADOW fails in the same run, so the assertion "
     "may not discriminate)"),
    ('sentence-min-words-off',
     "len(s.split()) >= 6",
     "len(s.split()) >= 1",
     "filler detection ignores fragments shorter than six words",
     "'repetition filler entry' / 'entry repeats a sentence three times'"),
    ('stem-min-length-off',
     "if len(w) >= 4]",
     "if len(w) >= 1]",
     "filename stem words shorter than four characters ('md', 's') are not evidence",
     "'filename stem absent from the entry'"),
    ('words-min-length-off',
     "if len(w) >= 4 and w not in STOP",
     "if w not in STOP",
     "content words shorter than four characters do not count toward overlap",
     "'topic overlap below the floor' (min_topic_overlap 40)"),
    ('dispo-first-wins-off',
     "if rid not in out:",
     "if True:",
     "the first disposition line for an id wins; a later LOCATED cannot overwrite it",
     "no case: no fixture carries two disposition lines for one id"),
    ('row-indent-bound-off',
     "ROW_RE = re.compile(r'^ {0,3}")[:-1] if False else "ROW_RE = re.compile(r'^ {0,3}\\|')",
     "ROW_RE = re.compile(r'^ *\\|')",
     "a registry row is indented at most three spaces (a deeper indent is code, "
     "not a row)",
     "no case: every fixture row starts at column 0"),
    ('population-required-off',
     "if args.advance and not (args.population or args.population_file):",
     "if False:",
     "advance mode requires a declared population",
     "'missing population file' (which still exits 2 through the unreadable read)"),
    ('capture-graded-normpath-off',
     "if rel == g or rel == os.path.normpath(g):",
     "if rel == g:",
     "a graded file named with a normalised path is still the graded file",
     "'capture inside the dir but graded' (same string, so it may not discriminate)"),
    ('norm-punct-space-off',
     "s = re.sub(r'\\s+([.,;:!?%\\)\\]])', r'\\1', s)",
     "s = s",
     "a space before punctuation is collapsed so a quote survives reflow in the capture",
     "no case: no fixture puts a space before punctuation"),
    ('capture-text-confinement-off',
     "    if not (rel == cap_dir or rel.startswith(cap_dir.rstrip('/') + '/')):\n        return ''",
     "    if False:\n        return ''",
     "capture_text() confines a manifest capture to the declared directory",
     "no case: capture_text() is never called (dead function)"),
]


def run_selftest(tool, work):
    d = os.path.join(work, 'st-' + hashlib.sha256(tool.encode()).hexdigest()[:10])
    os.makedirs(d, exist_ok=True)
    r = subprocess.run([sys.executable, '-B', tool, '--selftest', '--work', d],
                       capture_output=True, text=True, timeout=1800)
    out = (r.stdout or '') + (r.stderr or '')
    bad = [l.strip()[4:] for l in out.splitlines() if l.strip().startswith('BAD ')]
    head = next((l for l in out.splitlines() if l.startswith('SELFTEST ')), '')
    return r.returncode, head, bad


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', default='.')
    ap.add_argument('--work', required=True)
    ap.add_argument('--out', default=None)
    args = ap.parse_args()
    if not os.path.isdir(args.work):
        print('INDEPENDENT: FAIL --work must be an existing directory', file=sys.stderr)
        return 2
    src = os.path.join(args.root, TOOL)
    raw = open(src, 'rb').read()
    before = hashlib.sha256(raw).hexdigest()
    clean = os.path.join(args.work, 'clean.py')
    open(clean, 'wb').write(raw)
    rc, head, bad = run_selftest(clean, args.work)
    if rc != 0:
        print('INDEPENDENT: INCONCLUSIVE clean tool is not green: ' + head, file=sys.stderr)
        return 1
    text = raw.decode()
    rows = []
    for name, old, new, removed, ought in MUTANTS:
        if text.count(old) != 1:
            rows.append(dict(mutant=name, status='BROKEN-PATTERN',
                             detail=f'pattern count {text.count(old)}', removed=removed, ought=ought))
            continue
        path = os.path.join(args.work, 'i-' + name + '.py')
        open(path, 'w').write(text.replace(old, new, 1))
        mut_sha = hashlib.sha256(open(path, 'rb').read()).hexdigest()
        rc, head, bad = run_selftest(path, args.work)
        rows.append(dict(mutant=name, status='KILLED' if rc != 0 else 'SURVIVED',
                         rc=rc, selftest=head, failing_cases=bad, sha256=mut_sha,
                         removed=removed, ought=ought))
        os.unlink(path)
    after = hashlib.sha256(open(src, 'rb').read()).hexdigest()
    killed = sum(1 for r in rows if r['status'] == 'KILLED')
    survived = [r['mutant'] for r in rows if r['status'] == 'SURVIVED']
    broken = [r['mutant'] for r in rows if r['status'] == 'BROKEN-PATTERN']
    lines = [f'INDEPENDENT-SCORE: {killed}/{len(rows)} killed, {len(survived)} survived, '
             f'{len(broken)} broken-pattern',
             f'tool sha256 before {before}',
             f'tool sha256 after  {after}',
             f'restored: {"yes" if before == after else "NO"}']
    for r in rows:
        lines.append(f'  {r["status"]:14s} {r["mutant"]:<32s} '
                     f'{r.get("selftest", "")} bad={",".join(r.get("failing_cases", [])) or "-"}')
    out = '\n'.join(lines)
    print(out)
    if args.out:
        os.makedirs(os.path.dirname(args.out), exist_ok=True)
        open(args.out, 'w').write(out + '\n')
        json.dump(dict(tool_sha256_before=before, tool_sha256_after=after,
                       total=len(rows), killed=killed, rows=rows),
                  open(args.out.replace('.txt', '.json'), 'w'), indent=1)
    return 0


if __name__ == '__main__':
    sys.exit(main())
