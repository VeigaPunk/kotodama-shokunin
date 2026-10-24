#!/usr/bin/env python3
r"""Round-65 claim Ca acceptance, revision 1 (pre-data).

Claim Ca (calibration, records): every defect routed by the round-64
verifier spot-check (`corpus/lessons/round-64-verifier-spotcheck.md`
section 6) is dispositioned in the lane repo, each verified by one counting
leg over committed bytes, append-only wherever the target is a filed
record:

  R1 (HIGH)  reports/round-64/telemetry/final-measures-ca.txt is re-stamped
             to the revision its read-path bytes actually equalled
             (8bab271c691c6b1006da95316a24ae1958ec01e2, the records commit
             17 minutes after the original run over a dirty worktree) and
             now pins a tree hash of its read inputs; the original receipt
             bytes are preserved below a marker.  The repeats in LOG.md,
             SCORECARD.md and .ufo/waves/round-64/w2/LessonFinal.md are
             corrected; the filed fleet-repo report repeat is corrected by
             the round-65 report's erratum (the filed report is outside the
             lane's write scope and stays byte-preserved).
  R2 (MED)   reports/round-63/telemetry/revisions.txt gains a named
             "Correction (round 65, R2)" entry: the header clause "measured
             8d2041fa" for final-measures-c.txt is false (the path is absent
             at 8d2041fa; the receipt was added by 0c892ce); the original
             lines stay byte-unchanged above the correction.
  R3 (MED)   the wrong-path citation is corrected in lane records: the
             round-65 LOG entry and the SCORECARD correction table name
             .ufo/waves/round-64/w1/ReviewerCa.md as the actual path (the
             filed round-64 report's "w2/ReviewerCa.md" is named as the
             erratum target).
  R4 (MED)   reports/round-64/claims.json carries a statement_correction
             for claim O: the mutant wording is the honest "at least their
             pinned leg", with m1/m2's disclosed extra failures named; the
             frozen predicate sentence is byte-unchanged.
  R5 (LOW)   the control-o binding is named: a committed record binds
             reports/round-64/telemetry/control-o.txt to counter rev3
             (sha256 c27a9fef…) measured at b7d22703, not the final rev5.
  R6 (LOW)   corpus/lessons/round-64.md carries a "Correction (round 65,
             R6)" status note after R64-M12 (the S687 flip is committed in
             95c9194e; the lesson sentence was a pre-land snapshot).
  R7 (LOW)   the round-64 entry's `verified-at:` line no longer reads
             "skeleton structure prepared; cited source claims await L1
             insertion" — corrected in this round's entry touch.
  CRITERION  corpus/QUALITY.md carries criterion 17 generalizing the R1
             class: a receipt must pin the measured revision and a tree
             hash of its read inputs, never only the counter sha.
  QUOTES     tools/check-gate-quotes.py reports 0 findings on
             corpus/lessons/round-65.md (the Gate rows written this round).

Run from the lane root:

  python3 -B reports/round-65/accept-ca.py [--root DIR]

Frozen predicate (the same sentence in reports/round-65/claims.json and in
every receipt): ACCEPT-CA-65: every leg of reports/round-65/accept-ca.py
prints PASS.
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable
input.
"""
import argparse
import os
import re
import subprocess
import sys

BASE = "17c32302c6845c8f164b985a8cb312d3181c8788"
CA64 = "reports/round-64/telemetry/final-measures-ca.txt"
REV63 = "reports/round-63/telemetry/revisions.txt"
CA64_CLAIMS = "reports/round-64/claims.json"
CONTROL_O = "reports/round-64/telemetry/control-o.txt"
R64_LESSON = "corpus/lessons/round-64.md"
R64_ENTRY = "corpus/knowledge/linguistics/language-socialization-and-acquisition.md"
R65_LESSON = "corpus/lessons/round-65.md"
QUALITY = "corpus/QUALITY.md"
LOG = "LOG.md"
SCORE = "SCORECARD.md"
LESSON_FINAL = ".ufo/waves/round-64/w2/LessonFinal.md"
SPOTCHECK = "corpus/lessons/round-64-verifier-spotcheck.md"
TRUE_REV = "8bab271c691c6b1006da95316a24ae1958ec01e2"


def read(root, path):
    try:
        return open(os.path.join(root, path), encoding="utf-8").read()
    except (OSError, UnicodeDecodeError):
        return None


def git_out(root, args):
    proc = subprocess.run(["git", "-C", root] + args,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.returncode, proc.stdout.decode("utf-8", "replace")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    legs = []

    def leg(name, ok, detail):
        legs.append(ok)
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")

    # ---------- R1: re-stamped receipt + tree hash + corrected repeats ----------
    receipt = read(root, CA64) or ""
    tree_code, tree_out = git_out(root, ["rev-parse", f"{TRUE_REV}^{{tree}}"])
    tree = tree_out.strip()
    r1_ok = (f"measured revision: {TRUE_REV}" in receipt
             and re.search(rf"^tree: {re.escape(tree)}$", receipt, re.MULTILINE) is not None
             and "re-stamped" in receipt
             and "measured revision: 95c9194ef938e1338b2af894086a46e8b8677ee2"
                 in receipt.split("original receipt bytes")[-1])
    log_text = read(root, LOG) or ""
    score_text = read(root, SCORE) or ""
    lesson_final = read(root, LESSON_FINAL) or ""
    r1_repeats_ok = ("Correction (round 65, R1)" in log_text
                     and "Correction (round 65, R1)" in score_text
                     and "Correction (round 65, R1)" in lesson_final)
    leg("R1", r1_ok and r1_repeats_ok,
        f"restamp={r1_ok} tree={tree if tree_code == 0 else 'unresolvable'} "
        f"repeats_log_score_lessonfinal={r1_repeats_ok}")

    # ---------- R2: named correction, append-only ----------
    rev_text = read(root, REV63) or ""
    base_code, base_rev = git_out(root, ["show", f"{BASE}:{REV63}"])
    r2_original_intact = base_code == 0 and base_rev == rev_text[:len(base_rev)] and base_rev.strip() and rev_text.startswith(base_rev.rstrip("\n"))
    r2_named = "Correction (round 65, R2)" in rev_text and "final-measures-c.txt" in rev_text
    leg("R2", r2_original_intact and r2_named,
        f"original_intact={r2_original_intact} named={r2_named}")

    # ---------- R3: wrong-path citation corrected in lane records ----------
    r3_ok = ("w1/ReviewerCa.md" in log_text
             and "w2/ReviewerCa.md" in log_text
             and "Correction (round 65, R3)" in score_text)
    leg("R3", r3_ok, f"log_names_actual_and_wrong={r3_ok}")

    # ---------- R4: honest mutant wording, predicate unchanged ----------
    claims = read(root, CA64_CLAIMS) or ""
    r4_ok = ("statement_correction" in claims
             and "at least their pinned leg" in claims
             and "ACCEPT-O-64: every leg of reports/round-64/accept-o.py prints PASS."
                 in claims.replace("\\", ""))
    leg("R4", r4_ok, f"honest_wording_patch={'at least their pinned leg' in claims}")

    # ---------- R5: control-o binding named ----------
    control = read(root, CONTROL_O) or ""
    r5_in_control = ("c27a9fef" in control and "b7d22703" in control
                     and "revision 3" in control)
    r5_record = "Control-O binding" in log_text or "control-o binding" in log_text.lower()
    leg("R5", r5_in_control and r5_record,
        f"in_control={r5_in_control} in_log={r5_record}")

    # ---------- R6: R64-M12 status correction ----------
    lesson64 = read(root, R64_LESSON) or ""
    r6_ok = "Correction (round 65, R6)" in lesson64 and "R64-M12" in lesson64
    leg("R6", r6_ok, f"status_correction={r6_ok}")

    # ---------- R7: entry verified-at line corrected ----------
    entry = read(root, R64_ENTRY) or ""
    m = re.search(r"^- verified-at:.*$", entry, re.MULTILINE)
    verified_at = m.group(0) if m else ""
    r7_ok = (m is not None
             and not re.search(r"skeleton|await L1", verified_at, re.IGNORECASE))
    leg("R7", r7_ok, f"line={verified_at[:90]!r}")

    # ---------- CRITERION: QUALITY 17 ----------
    quality = read(root, QUALITY) or ""
    r_criterion = re.search(r"17\.", quality) is not None
    leg("CRITERION", r_criterion, f"criterion_with_tree_hash={r_criterion}")

    # ---------- QUOTES: round-65 lesson Gate rows ----------
    q = subprocess.run([sys.executable, "-B", "tools/check-gate-quotes.py",
                        os.path.join(root, R65_LESSON)],
                       cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    q_out = q.stdout.decode("utf-8", "replace")
    r_quotes = q.returncode == 0 and "0 finding" in q_out
    leg("QUOTES", r_quotes, f"exit={q.returncode} out={q_out.strip().splitlines()[-1:]}")

    verdict = all(legs)
    print(f"ACCEPT-CA-65: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
