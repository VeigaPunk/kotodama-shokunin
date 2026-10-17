#!/usr/bin/env python3
"""Negative control for round-8 defect R8-O12 (supplement review 26, defect D8).

Defect under control: `tools/gates/naming-collision-gate.py` compiled the
packet-authored `formation.pattern` with `re.fullmatch` and caught only
`re.error`, so a pattern that compiles but backtracks catastrophically ran
unbounded. Review 26 §3 D8 payload, re-confirmed on the pre-fix bytes at
cf338a7: rule `pattern: "^(?P<stem>(a+)+)$"` with stem 40*'a'+'b' — the
subprocess was still running at a 12 s wall bound and was killed (rc=124,
no output). Unbounded CPU from a packet another lane can author.

Repair (this shard): Gate C now matches under a wall-clock budget and refuses
the two canonical catastrophic shapes up front (see the gate's docstring
"Gate C matching budget" calibration note and MATCH_BUDGET_SECONDS).

Contract (one expectation set, both modes):
  * pointed at the LIVE (post-fix) gate -> every check passes, exit 0;
  * pointed at PRE-FIX bytes (`--gate <pre-fix copy>` or
    `--pre-fix-from-git [REV]`, default REV `cf338a7`) -> the unsafe-pattern
    checks observe the pre-fix pattern (the gate does not terminate inside
    the wall bound) and the control exits 1, naming the pattern.

Isolation: payloads are written only into a scratch directory — `$TMPDIR` when
set and writable, otherwise the system temp dir, otherwise a self-cleaning
`.scratch` beside this file (the round-8 wave observed /tmp inode exhaustion,
so the fallback matters). Gates run as subprocesses; no live repository path
is written.

Exit codes: 0 all controls pass · 1 any control fails · 2 usage/environment.

Usage:
    python3 reports/round-8/operability/neg-controls/neg-12/neg-12-control.py
    python3 .../neg-12-control.py --gate /tmp/neg12-prefix.py
    python3 .../neg-12-control.py --pre-fix-from-git cf338a7
"""

import argparse
import hashlib
import os
import shutil
import subprocess
import sys
import tempfile
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.abspath(os.path.join(HERE, "..", "..", "..", "..", ".."))
DEFAULT_GATE = os.path.join(REPO, "tools", "gates", "naming-collision-gate.py")

# Review 26 §0 pin for the pre-fix bytes (blob fe34faa / HEAD cf338a7, unchanged).
PREFIX_SHA256 = "8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526"

WALL_BOUND_SECONDS = 10.0

_PHON = ('phonology: {consonants: [p, t, k, m, n, s, l], vowels: [a, e, i, o, u], '
         'phonotactics: "(C)V(C)", tones: 0}\n')


def _packet(pattern, stem, name="pak", output="{stem}x"):
    return (
        "name: R\n"
        + _PHON
        + "morphology:\n"
        + "  derivation_rules:\n"
        + '    - {id: R1, kind: suffix, affix: -x, pattern: "%s", output: "%s"}\n'
        % (pattern, output)
        + "names:\n"
        + "  - {name: %s, id: N1, type: person, formation: {stem: %s, rule: R1}}\n"
        % (name, stem)
    )


# C1/C2 — the two canonical catastrophic shapes the static screen refuses.
NESTED_QUANTIFIER = _packet("^(?P<stem>(a+)+)$", "a" * 40 + "b")
QUANTIFIED_ALTERNATION = _packet("^(?P<stem>(a|aa)+)$", "a" * 40 + "b")
# C3 — a shape the screen deliberately leaves alone (no groups); only the
# wall-clock budget can stop it. Pre-fix this also ran unbounded.
BUDGET_ONLY = _packet("^a*a*a*a*a*a*a*a*a*a*b$", "a" * 40 + "c")
# C4 — legitimate fixture-shaped pattern with a real derivation: must replay
# exactly as before the repair (no DERIV finding at all).
LEGIT = _packet("^(?P<stem>.+)a$", "paka", name="pakin", output="{stem}in")
# C5 — a legal but non-matching pattern: still DERIV-REPLAY FAIL, not HOLD.
MISMATCH = _packet("^(?P<stem>.+)z$", "paka", name="pakin")


def _scratch_candidates():
    seen = []
    for cand in (os.environ.get("TMPDIR"), tempfile.gettempdir(), os.path.join(HERE, ".scratch")):
        if cand and cand not in seen:
            seen.append(cand)
    return seen


class Scratch(object):
    """TemporaryDirectory with a fallback chain (see module docstring)."""

    def __init__(self):
        self.path = None
        self.errors = []
        for cand in _scratch_candidates():
            try:
                os.makedirs(cand, exist_ok=True)
                self.path = tempfile.mkdtemp(prefix="neg12-", dir=cand)
                return
            except OSError as exc:
                self.errors.append("%s: %s" % (cand, exc))
        raise SystemExit("NEG-12 ERROR: no writable scratch directory (%s)"
                         % "; ".join(self.errors))

    def write(self, name, text):
        path = os.path.join(self.path, name)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(text)
        return path

    def close(self):
        if self.path:
            shutil.rmtree(self.path, ignore_errors=True)


def run_gate(gate, payload_path, timeout=WALL_BOUND_SECONDS):
    """Return (rc, output, elapsed); rc = 'TIMEOUT' when the bound kills it."""
    start = time.time()
    try:
        proc = subprocess.run(
            [sys.executable, gate, payload_path],
            capture_output=True, text=True, timeout=timeout)
        return proc.returncode, (proc.stdout or "") + (proc.stderr or ""), time.time() - start
    except subprocess.TimeoutExpired:
        return "TIMEOUT", "", time.time() - start


def finding_ids(output):
    ids = []
    for line in output.splitlines():
        if line.startswith("FINDING "):
            ids.append(line.split(":", 1)[0].split()[1])
    return ids


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--gate", default=DEFAULT_GATE,
                    help="gate file to test (default: the live lane gate)")
    ap.add_argument("--pre-fix-from-git", nargs="?", const="cf338a7", default=None,
                    metavar="REV",
                    help="extract the pre-fix gate bytes from git REV into scratch and test those")
    args = ap.parse_args()

    scratch = Scratch()
    try:
        gate = os.path.abspath(args.gate)
        if args.pre_fix_from_git:
            proc = subprocess.run(
                ["git", "-C", REPO, "show",
                 "%s:tools/gates/naming-collision-gate.py" % args.pre_fix_from_git],
                capture_output=True)
            if proc.returncode != 0:
                print("NEG-12 ERROR: git show failed: %s"
                      % (proc.stderr or b"").decode("utf-8", "replace").strip())
                return 2
            gate = scratch.write("prefix-naming.py", proc.stdout.decode("utf-8"))
        if not os.path.isfile(gate):
            print("NEG-12 ERROR: gate not found: %s" % gate)
            return 2
        with open(gate, "rb") as handle:
            digest = hashlib.sha256(handle.read()).hexdigest()
        print("NEG-12 gate under test: %s" % gate)
        print("NEG-12 gate sha256: %s" % digest)
        if digest == PREFIX_SHA256:
            print("NEG-12 note: this is the review-26 pinned PRE-FIX byte copy "
                  "(%s...); checks below are expected to FAIL." % PREFIX_SHA256[:8])

        payloads = {
            "nested-quantifier": NESTED_QUANTIFIER,
            "quantified-alternation": QUANTIFIED_ALTERNATION,
            "budget-only-shape": BUDGET_ONLY,
            "legit-pattern-twin": LEGIT,
            "legal-mismatch": MISMATCH,
        }
        paths = {key: scratch.write(key + ".yml", text) for key, text in payloads.items()}

        failures = []
        checks = 0

        def check(name, key, predicate, describe):
            nonlocal checks
            checks += 1
            rc, out, elapsed = run_gate(gate, paths[key])
            ids = finding_ids(out)
            ok = predicate(rc, ids, out, elapsed)
            print("NEG-12 %-24s rc=%-8s t=%5.2fs ids=%s %s"
                  % (name, rc, elapsed, ",".join(ids) or "-", "PASS" if ok else "FAIL"))
            if not ok:
                failures.append("%s: %s" % (name, describe(rc, ids, out, elapsed)))

        def refused(kind):
            def predicate(rc, ids, out, elapsed):
                return (rc == 1 and "DERIV-HOLD" in ids and kind in out
                        and elapsed < WALL_BOUND_SECONDS)
            return predicate

        def refused_desc(expect):
            def describe(rc, ids, out, elapsed):
                if rc == "TIMEOUT":
                    return ("PRE-FIX PATTERN OBSERVED: the gate did not terminate "
                            "inside the %.0fs wall bound (unbounded match); expected "
                            "%s within it." % (WALL_BOUND_SECONDS, expect))
                return ("PRE-FIX/regression PATTERN OBSERVED: rc=%s ids=%s t=%.2fs; "
                        "expected %s. output=%r"
                        % (rc, ids, elapsed, expect, out.strip().splitlines()[:3]))
            return describe

        # C1/C2: the two canonical shapes are refused as HOLD, fast.
        check("nested-quantifier", "nested-quantifier",
              refused("catastrophic backtracking shape"),
              refused_desc("rc=1 with DERIV-HOLD naming the catastrophic shape"))
        check("quantified-alternation", "quantified-alternation",
              refused("catastrophic backtracking shape"),
              refused_desc("rc=1 with DERIV-HOLD naming the catastrophic shape"))

        # C3: a screen-invisible shape is stopped by the wall-clock budget.
        check("budget-only-shape", "budget-only-shape",
              refused("matching budget"),
              refused_desc("rc=1 with DERIV-HOLD naming the matching budget"))

        # C4: the fixture-shaped legitimate pattern still replays (no DERIV finding).
        check("legit-pattern-twin", "legit-pattern-twin",
              lambda rc, ids, out, elapsed: rc == 1 and not any(
                  i.startswith("DERIV-") for i in ids),
              lambda rc, ids, out, elapsed: (
                  "regression: a legitimate pattern no longer replays: rc=%s ids=%s "
                  "output=%r" % (rc, ids, out.strip().splitlines()[:3])))

        # C5: a legal non-matching pattern is still a FAIL, not a HOLD.
        check("legal-mismatch", "legal-mismatch",
              lambda rc, ids, out, elapsed: rc == 1 and "DERIV-REPLAY" in ids
              and "DERIV-HOLD" not in ids,
              lambda rc, ids, out, elapsed: (
                  "regression: mismatch handling changed: rc=%s ids=%s output=%r"
                  % (rc, ids, out.strip().splitlines()[:3])))

        if failures:
            print("NEG-12 RESULT: FAIL (%d/%d checks)" % (len(failures), checks))
            for line in failures:
                print("NEG-12 FAILURE: %s" % line)
            return 1
        print("NEG-12 RESULT: PASS (%d/%d checks)" % (checks, checks))
        return 0
    finally:
        scratch.close()


if __name__ == "__main__":
    sys.exit(main())
