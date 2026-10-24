#!/usr/bin/env python3
r"""Round-69 operability acceptance counter — claim O2 (NEW counter).

The round-68 operability counter failed as declared: its EXEC fixture lane
never created the used-by file, so the scan answered ``missing_paths=1`` in
every recorded run and the leg was structurally unreachable (R68-M1). This
counter is a NEW file; the round-68 counters are not edited. Leg
``R68FROZEN`` proves that by re-deriving the three round-68 counters'
sha256 against the sha256 each round-68 receipt recorded.

Claim O2 surface: the lane gains a runnable, lane-shaped settlement fixture
harness (``tools/check-settlement-fixture.py``) whose negative case is the
missing-used-by defect class the round-68 counter never exercised.

Usage:
  --root DIR     evaluate claim O2 against the lane tree at DIR (default ".")
  --selftest     run the GREEN control (a fixture tree that satisfies the
                 claim) and the DO-NOTHING control (the same tree with the
                 used-by file absent, which the claim's LANE leg must catch);
                 exit 0 iff the green fixture passes and the do-nothing
                 fixture fails.

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

NEG_REGISTRY = """# SOURCES — independent probe fixture

## Registry

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S001 | Probe base source — https://example.invalid/base | docs | B | probe scope | §1 | the base claim | queued | 2026-10-24 | 90d | — |
| S002 | Probe successor source — https://example.invalid/next | docs | A | probe scope | §1 | supersedes S001 — the probe correction | mined | 2026-10-24 | 90d | corpus/knowledge/a.md |
"""

LANE_REGISTRY = NEG_REGISTRY

R68_COUNTERS = (
    ("accept-o.py", "final-measures-o.txt"),
    ("accept-ca.py", "final-measures-ca.txt"),
    ("accept-c.py", "final-measures-c.txt"),
)


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


def run_tool(root, tool, args):
    proc = subprocess.run(
        [sys.executable, "-B", os.path.join(root, tool)] + args,
        capture_output=True, text=True, check=False)
    return proc.returncode, proc.stdout + proc.stderr


def evaluate(root, res):
    root = os.path.abspath(root)

    # STAMP — the counter under test is the committed one.
    mine = sha256_file(os.path.join(HERE, SELF))
    committed = sha256_file(os.path.join(root, "reports", "round-69", SELF))
    res.add("STAMP", mine and committed and mine == committed,
            "self=%s committed=%s" % ((mine or "none")[:12],
                                      (committed or "none")[:12]))

    # TOOL — the new fixture harness is present.
    tool_path = os.path.join(root, "tools", "check-settlement-fixture.py")
    res.add("TOOL", os.path.exists(tool_path),
            "tools/check-settlement-fixture.py")

    # FIXTURE — the harness's own three cases are green.
    if os.path.exists(tool_path):
        rc, out = run_tool(root, "tools/check-settlement-fixture.py",
                           ["--selftest"])
        res.add("FIXTURE", rc == 0 and "FIXTURE: 3/3" in out,
                "rc=%d %s" % (rc, "FIXTURE: 3/3" in out))
        # NEGCASE — the missing-used-by case is caught (the r68 defect class).
        neg_line = [l for l in out.splitlines()
                    if l.startswith("PASS fixture-negative")]
        res.add("NEGCASE", bool(neg_line) and "missing_paths=1" in neg_line[0],
                neg_line[0] if neg_line else "no fixture-negative line")
        # LANE — the real lane tree settles with no missing used-by path.
        rc, out = run_tool(root, "tools/check-settlement-fixture.py",
                           ["--root", root])
        res.add("LANE", rc == 0 and "LANE: pending=0 missing_paths=0" in out,
                "rc=%d %s" % (rc, "LANE: pending=0 missing_paths=0" in out))
    else:
        res.add("FIXTURE", False, "tool absent")
        res.add("NEGCASE", False, "tool absent")
        res.add("LANE", False, "tool absent")

    # NEGPROBE — independent reproduction: the base checker on a fixture whose
    # used-by file is absent must report missing_paths=1. Built here, not read
    # from the new tool, so a broken harness cannot hide the defect.
    checker = os.path.join(root, "tools", "check-supersession-settlement.py")
    if os.path.exists(checker):
        with tempfile.TemporaryDirectory(prefix="o69-negprobe-") as td:
            reg = os.path.join(td, "corpus", "SOURCES.md")
            os.makedirs(os.path.dirname(reg), exist_ok=True)
            with open(reg, "w", encoding="utf-8") as fh:
                fh.write(NEG_REGISTRY)
            proc = subprocess.run(
                [sys.executable, "-B", checker, "--scan", "--root", td],
                capture_output=True, text=True, check=False)
            res.add("NEGPROBE", "missing_paths=1" in proc.stdout,
                    "missing_paths=1 present=%s" %
                    ("missing_paths=1" in proc.stdout))
    else:
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


def build_fixture_root(fx, *, with_usedby):
    os.makedirs(os.path.join(fx, "tools"), exist_ok=True)
    for rel in ("tools/check-settlement-fixture.py",
                "tools/check-supersession-settlement.py"):
        src = os.path.join(LANE, rel)
        if os.path.exists(src):
            shutil.copy2(src, os.path.join(fx, rel))
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
    with open(reg, "w", encoding="utf-8") as fh:
        fh.write(LANE_REGISTRY)
    if with_usedby:
        kb = os.path.join(fx, "corpus", "knowledge", "a.md")
        os.makedirs(os.path.dirname(kb), exist_ok=True)
        with open(kb, "w", encoding="utf-8") as fh:
            fh.write("cites S002 now\n")


def selftest():
    with tempfile.TemporaryDirectory(prefix="o69-selftest-") as td:
        green = os.path.join(td, "green")
        build_fixture_root(green, with_usedby=True)
        r1 = Result(quiet=True)
        evaluate(green, r1)
        green_ok = r1.ok
        print("GREEN FIXTURE: %s (legs %d/%d)" % (
            "PASS" if green_ok else "FAIL",
            sum(1 for _, ok, _ in r1.legs if ok), len(r1.legs)))

        nothing = os.path.join(td, "donothing")
        build_fixture_root(nothing, with_usedby=False)
        r2 = Result(quiet=True)
        evaluate(nothing, r2)
        nothing_fails = not r2.ok
        print("DO-NOTHING FIXTURE: %s (legs %d/%d)" % (
            "FAIL (as required)" if nothing_fails else "PASS (unexpected)",
            sum(1 for _, ok, _ in r2.legs if ok), len(r2.legs)))
        print("SELFTEST: %d/2" % (sum([green_ok, nothing_fails])))
        return 0 if (green_ok and nothing_fails) else 1


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
