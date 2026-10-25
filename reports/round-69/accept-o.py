#!/usr/bin/env python3
r"""Round-69 operability acceptance counter — claim O2 (NEW counter, revision 1).

Revision history (both revisions are committed; the revision is recorded in
reports/round-69/claims.json with its forcing receipt):
  revision 0 — declared pre-data. It judged the new fixture harness by the
    harness's own printed lines. The wave's attack seat CritO1
    (.ufo/waves/round-69/w1/CritO1.md, probe C) showed that a no-op harness
    that only prints the expected strings reaches ACCEPT-O-69: PASS 7/7
    without running a single fixture: a do-nothing control could reach the
    target. No data had landed when the attack landed, so the instrument was
    revised before any data seat scored it (the r59/r63 pre-data control-wave
    pattern; the kumitate r42 rule bites on a rule changed after DATA, not on
    a falsifier forcing an instrument before data).
  revision 1 — the predicate sentence, the seven leg names and the 7/7 target
    are UNCHANGED. What changed is the anchoring: no leg now trusts the
    harness's self-report. The counter builds its own lane-shaped fixtures and
    runs the BASE checker (tools/check-supersession-settlement.py) on them
    itself, scans the lane root itself, and uses the harness only as a
    cross-check on a fixture the counter built (NEGPROBE). The spoof that
    killed revision 0 now fails NEGPROBE.

The round-68 counters are not edited; leg R68FROZEN proves that by
re-deriving the three round-68 counters' sha256 against the sha256 each
round-68 receipt recorded.

Usage:
  --root DIR     evaluate claim O2 against the lane tree at DIR (default ".")
  --selftest     run three controls and require each to behave as declared:
                 GREEN FIXTURE (a tree satisfying the claim) must PASS;
                 DO-NOTHING FIXTURE (the harness deleted) must FAIL; and
                 SPOOF FIXTURE (a no-op harness printing the expected strings)
                 must FAIL.

Exit codes: 0 pass · 1 fail · 2 usage/env.
Reads only. No network. No mutation of the lane tree.
"""

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(HERE))
SELF = os.path.basename(__file__)

# The counter's own lane-shaped registry fixture (independent of the harness).
FIXTURE_REGISTRY = """# SOURCES — counter fixture lane

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | Counter base source — https://example.invalid/base | docs | B | the base row's scope | §1 | the base claim | {s001} | 2026-10-24 | 90d | — |
| S002 | Counter successor source — https://example.invalid/next | docs | A | the successor row's scope | §1 | supersedes S001 — the counter's own correction | mined | 2026-10-24 | 90d | corpus/knowledge/a.md |

## Paths

- counter fixture — S001 -> S002: the correction replaces the base claim.

## Search log

- 2026-10-24 — counter fixture lane; no network; the two rows are synthetic.
"""

SUMMARY_RE = re.compile(
    r"SETTLEMENT:\s*pending=(\d+)\s+chains=(\d+)\s+usedby_paths=(\d+)\s+"
    r"missing_paths=(\d+)")

R68_COUNTERS = (
    ("accept-o.py", "final-measures-o.txt"),
    ("accept-ca.py", "final-measures-ca.txt"),
    ("accept-c.py", "final-measures-c.txt"),
)

SPOOF_HARNESS = '''#!/usr/bin/env python3
import sys
print("PASS fixture-green rc=0 pending=0 missing_paths=0")
print("PASS fixture-negative rc=1 pending=0 missing_paths=1")
print("PASS fixture-pending rc=1 pending=1 missing_paths=0")
print("FIXTURE: 3/3")
if "--root" in sys.argv:
    print("LANE: pending=0 missing_paths=0")
sys.exit(0)
'''


def sha256_file(path):
    h = hashlib.sha256()
    try:
        with open(path, "rb") as fh:
            for chunk in iter(lambda: fh.read(65536), b""):
                h.update(chunk)
    except OSError:
        return None
    return h.hexdigest()


def recorded_sha(path):
    try:
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
    except OSError:
        return None
    m = re.search(r"^# counter sha256 \(self\):\s*([0-9a-f]{64})\s*$",
                  text, re.M)
    return m.group(1) if m else None


def write_fixture(root, *, create_usedby, unsettled):
    reg = os.path.join(root, "corpus", "SOURCES.md")
    os.makedirs(os.path.dirname(reg), exist_ok=True)
    with open(reg, "w", encoding="utf-8") as fh:
        fh.write(FIXTURE_REGISTRY.format(s001="mined" if unsettled else "queued"))
    if create_usedby:
        kb = os.path.join(root, "corpus", "knowledge", "a.md")
        os.makedirs(os.path.dirname(kb), exist_ok=True)
        with open(kb, "w", encoding="utf-8") as fh:
            fh.write("cites S002 now\n")


def run_checker(checker, root):
    proc = subprocess.run(
        [sys.executable, "-B", checker, "--scan", "--root", root],
        capture_output=True, text=True, check=False)
    return proc.returncode, proc.stdout


def summary(out):
    m = SUMMARY_RE.search(out)
    if not m:
        return None
    return {"pending": int(m.group(1)), "chains": int(m.group(2)),
            "usedby_paths": int(m.group(3)),
            "missing_paths": int(m.group(4))}


def run_tool(root, tool, args):
    proc = subprocess.run(
        [sys.executable, "-B", os.path.join(root, tool)] + args,
        capture_output=True, text=True, check=False)
    return proc.returncode, proc.stdout + proc.stderr


class Result(object):
    def __init__(self, quiet=False):
        self.legs = []
        self.quiet = quiet

    def add(self, name, ok, detail=""):
        self.legs.append((name, bool(ok), detail))
        if not self.quiet:
            print("LEG %s %s %s" % ("PASS" if ok else "FAIL", name, detail))

    @property
    def ok(self):
        return all(ok for _, ok, _ in self.legs)


def evaluate(root, res):
    root = os.path.abspath(root)

    # STAMP — the counter under test is the committed one.
    mine = sha256_file(os.path.join(HERE, SELF))
    committed = sha256_file(os.path.join(root, "reports", "round-69", SELF))
    res.add("STAMP", bool(mine) and mine == committed,
            "self=%s committed=%s" % ((mine or "none")[:12],
                                      (committed or "none")[:12]))

    tool_rel = "tools/check-settlement-fixture.py"
    checker_rel = "tools/check-supersession-settlement.py"
    tool_path = os.path.join(root, tool_rel)
    checker_path = os.path.join(root, checker_rel)

    # TOOL — the new fixture harness is present.
    res.add("TOOL", os.path.exists(tool_path), tool_rel)

    # FIXTURE — the counter's OWN lane-shaped green fixture: the base checker
    # must settle it (pending=0, missing_paths=0, exit 0).
    if os.path.exists(checker_path):
        with tempfile.TemporaryDirectory(prefix="o69-green-") as td:
            fx = os.path.join(td, "green")
            write_fixture(fx, create_usedby=True, unsettled=False)
            rc, out = run_checker(checker_path, fx)
            s = summary(out)
            ok = rc == 0 and s is not None and s["pending"] == 0 \
                and s["missing_paths"] == 0
            res.add("FIXTURE", ok, "rc=%d pending=%s missing_paths=%s" % (
                rc, s["pending"] if s else "?",
                s["missing_paths"] if s else "?"))
        # NEGCASE — the counter's OWN negative fixture (the used-by file is
        # absent): the base checker must report missing_paths=1. This is the
        # round-68 defect class, detected by the counter, not by the harness.
        with tempfile.TemporaryDirectory(prefix="o69-neg-") as td:
            fx = os.path.join(td, "negative")
            write_fixture(fx, create_usedby=False, unsettled=False)
            rc, out = run_checker(checker_path, fx)
            s = summary(out)
            ok = s is not None and s["pending"] == 0 and s["missing_paths"] == 1
            res.add("NEGCASE", ok, "rc=%d pending=%s missing_paths=%s" % (
                rc, s["pending"] if s else "?",
                s["missing_paths"] if s else "?"))
        # LANE — the counter scans the lane root itself.
        rc, out = run_checker(checker_path, root)
        s = summary(out)
        ok = rc == 0 and s is not None and s["pending"] == 0 \
            and s["missing_paths"] == 0
        res.add("LANE", ok, "rc=%d pending=%s missing_paths=%s" % (
            rc, s["pending"] if s else "?",
            s["missing_paths"] if s else "?"))
        # NEGPROBE — the HARNESS must report missing_paths=1 on the
        # counter's OWN negative fixture: the harness's behaviour is judged
        # against evidence the counter built, never against its self-report.
        with tempfile.TemporaryDirectory(prefix="o69-probe-") as td:
            fx = os.path.join(td, "negative")
            write_fixture(fx, create_usedby=False, unsettled=False)
            if os.path.exists(tool_path):
                rc, out = run_tool(root, tool_rel, ["--root", fx])
                lane_lines = [l for l in out.splitlines()
                              if l.startswith("LANE:")]
                caught = any("missing_paths=1" in l for l in lane_lines)
                res.add("NEGPROBE", bool(lane_lines) and caught,
                        "harness_on_counter_fixture rc=%d lane_lines=%s" % (
                            rc, lane_lines or "none"))
            else:
                res.add("NEGPROBE", False, "harness absent")
    else:
        res.add("FIXTURE", False, "checker absent")
        res.add("NEGCASE", False, "checker absent")
        res.add("LANE", False, "checker absent")
        res.add("NEGPROBE", False, "checker absent")

    # R68FROZEN — the three round-68 counters are byte-identical to the
    # sha256 their own receipts recorded (no post-data amendment).
    bad = []
    for counter, receipt in R68_COUNTERS:
        live = sha256_file(os.path.join(root, "reports", "round-68", counter))
        rec = recorded_sha(os.path.join(root, "reports", "round-68", "telemetry",
                                         receipt))
        if not live or not rec or live != rec:
            bad.append("%s live=%s recorded=%s" % (
                counter, (live or "none")[:12], (rec or "none")[:12]))
    res.add("R68FROZEN", not bad, "mismatched=%s" % (bad or "none"))

    return res


def build_fixture_root(fx, *, harness):
    os.makedirs(os.path.join(fx, "tools"), exist_ok=True)
    for rel in ("tools/check-supersession-settlement.py",):
        src = os.path.join(LANE, rel)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(fx, rel))
    if harness == "real":
        src = os.path.join(LANE, "tools", "check-settlement-fixture.py")
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(fx, "tools",
                                            "check-settlement-fixture.py"))
    elif harness == "spoof":
        with open(os.path.join(fx, "tools", "check-settlement-fixture.py"), "w",
                  encoding="utf-8") as fh:
            fh.write(SPOOF_HARNESS)
    for rel in ("reports/round-68/accept-c.py", "reports/round-68/accept-o.py",
                "reports/round-68/accept-ca.py",
                "reports/round-68/telemetry/final-measures-c.txt",
                "reports/round-68/telemetry/final-measures-o.txt",
                "reports/round-68/telemetry/final-measures-ca.txt",
                "reports/round-69/accept-o.py"):
        src = os.path.join(LANE, rel)
        if os.path.exists(src):
            dst = os.path.join(fx, rel)
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            shutil.copy2(src, dst)
    reg = os.path.join(fx, "corpus", "SOURCES.md")
    os.makedirs(os.path.dirname(reg), exist_ok=True)
    write_fixture(fx, create_usedby=True, unsettled=False)


def selftest():
    results = []
    with tempfile.TemporaryDirectory(prefix="o69-selftest-") as td:
        for label, harness, want_pass in (("GREEN FIXTURE", "real", True),
                                          ("DO-NOTHING FIXTURE", None, False),
                                          ("SPOOF FIXTURE", "spoof", False)):
            fx = os.path.join(td, label.split()[0].lower())
            build_fixture_root(fx, harness=harness)
            r = Result(quiet=True)
            evaluate(fx, r)
            passed = r.ok
            behaved = (passed == want_pass)
            print("%s: %s (legs %d/%d) — %s" % (
                label,
                "PASS" if passed else "FAIL",
                sum(1 for _, ok, _ in r.legs if ok), len(r.legs),
                "as required" if behaved else "UNEXPECTED"))
            results.append(behaved)
    print("SELFTEST: %d/%d" % (sum(results), len(results)))
    return 0 if all(results) else 1


def main():
    ap = argparse.ArgumentParser(description="round-69 operability counter")
    ap.add_argument("--root", default=".")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if args.selftest:
        return selftest()
    res = Result()
    evaluate(args.root, res)
    passed = sum(1 for _, ok, _ in res.legs if ok)
    print("ACCEPT-O-69: %s legs=%d/%d" % (
        "PASS" if res.ok else "FAIL", passed, len(res.legs)))
    return 0 if res.ok else 1


if __name__ == "__main__":
    sys.exit(main())
