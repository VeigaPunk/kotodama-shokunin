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

Revision history (pre-data):
- revision 3: MutRecords survivors closed - R4 requires the false wording
  absent from the whole claims.json (M3), R2's correction must assert the
  clause is false (M7), R3's correction must name w1/ReviewerCa.md as the
  actual path (M6), R5's binding must name revision 3 (M8), R6's window must
  name R64-M12 (M10), CRITERION's negation scan gains 'optional' (M11), R7
  gains the round-64 naming requirement and a wider stale-wording blocklist
  (M5, M12).  Forcing controls: .ufo/waves/round-65/w1/MutRecords.md.
- revision 2: R1 hardened (original-bytes sha256, per-path read-input
  manifest at 8bab271c, dirty-worktree line, repeats must name the corrected
  revision); R4 requires byte-exact predicate equality via JSON parse; R5
  requires the named binding record.  Forcing controls:
  .ufo/waves/round-65/w1/RevReceipts.md (HIGH-1 bypass keeps only a bare
  false-stamp line; HIGH-2 tree line alone is not a read-inputs hash;
  HIGH-3 dirtiness disclosure; MEDIUM-6 bare-marker repeats; LOW-7
  substring predicate match).

Run from the lane root:

  python3 -B reports/round-65/accept-ca.py [--root DIR]

Frozen predicate (the same sentence in reports/round-65/claims.json and in
every receipt): ACCEPT-CA-65: every leg of reports/round-65/accept-ca.py
prints PASS.
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable
input.
"""
import argparse
import hashlib
import json
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
# revision 2 (pre-data; forcing controls .ufo/waves/round-65/w1/RevReceipts.md
# HIGH-1/HIGH-2/HIGH-3): the receipt must pin the ORIGINAL bytes' sha256, a
# per-path read-input manifest at TRUE_REV, and a dirty-worktree disclosure.
READ_INPUTS = [
    "LOG.md",
    "SCORECARD.md",
    "corpus/LOG.md",
    "corpus/lessons/round-64.md",
    "reports/round-63/telemetry/revisions.txt",
]
ORIGINAL_RECEIPT = "reports/round-64/telemetry/final-measures-ca.txt"
FROZEN_O_PREDICATE = ("ACCEPT-O-64: every leg of reports/round-64/accept-o.py "
                      "prints PASS.")


def read(root, path):
    try:
        return open(os.path.join(root, path), encoding="utf-8").read()
    except (OSError, UnicodeDecodeError):
        return None


def git_out(root, args):
    proc = subprocess.run(["git", "-C", root] + args,
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    return proc.returncode, proc.stdout.decode("utf-8", "replace")


def _preserved_block_ok(receipt):
    """The block below the `--- original receipt bytes ---` marker must be the
    full original receipt, not one surviving line (RevCounterCaKeying F1/F2:
    the revision-1 split degenerated to the whole file when the marker was
    renamed, and one fabricated line satisfied preservation).  Requires the
    marker exactly once and the distinctive original lines all present below
    it, with exactly one `measured revision:` line above the marker."""
    marker = "--- original receipt bytes ---"
    if receipt.count(marker) != 1:
        return False
    above, below = receipt.split(marker, 1)
    if above.count("measured revision:") != 1:
        return False
    required = [
        "ACCEPT-CA-64 evidence (FINAL)",
        "counter sha256: d0787979",
        "CANONLOG PASS",
        "PTRS PASS",
        "HISTOGRAM PASS",
        "DISPO PASS",
        "REVNAMES PASS",
        "NITS PASS",
        "R63SEP PASS",
        "ACCEPT-CA-64: PASS",
        "exit=0",
        "measured revision: 95c9194ef938e1338b2af894086a46e8b8677ee2",
    ]
    return all(line in below for line in required)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    import hashlib as _hl
    _self = _hl.sha256(open(os.path.abspath(__file__), "rb").read()).hexdigest()
    _mv = subprocess.run(["git", "rev-parse", "main"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(f"# counter sha256 (self): {_self}")
    print(f"# measured revision (lane main): {_mv.stdout.decode().strip() or 'unresolvable'}")
    legs = []

    def leg(name, ok, detail):
        legs.append(ok)
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")

    # ---------- R1: re-stamped receipt + tree hash + read-input manifest +
    # original-bytes sha256 + dirty-worktree line + keyed repeats ----------
    receipt = read(root, CA64) or ""
    tree_code, tree_out = git_out(root, ["rev-parse", f"{TRUE_REV}^{{tree}}"])
    tree = tree_out.strip()
    orig_proc = subprocess.run(["git", "-C", root, "show", f"{BASE}:{ORIGINAL_RECEIPT}"],
                               stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    orig_sha = hashlib.sha256(orig_proc.stdout).hexdigest() if orig_proc.returncode == 0 else "unresolvable"
    _lines = receipt.splitlines()
    r1_checks = {
        "stamp_positional": (len(_lines) > 1
                             and _lines[1] == f"measured revision: {TRUE_REV}"),
        "stamp": f"measured revision: {TRUE_REV}" in receipt,
        "tree": re.search(rf"^tree: {re.escape(tree)}$", receipt, re.MULTILINE) is not None,
        "restamp_note": "re-stamped" in receipt,
        "dirty": (f"dirty-worktree: original run over a dirty worktree; records landed in {TRUE_REV}"
                  in receipt),
        "original_sha": f"original-sha256: {orig_sha}" in receipt,
        "tree_resolves": tree_code == 0,
        "preserved_original": _preserved_block_ok(receipt),
    }
    # RevClaimCa HIGH-1: a cosmetic re-stamp kept 95c9194e as the operative
    # line 2 and passed; the true stamp must be the receipt's line 2 (index 1).
    manifest_bad = []
    for path in READ_INPUTS:
        proc = subprocess.run(["git", "-C", root, "show", f"{TRUE_REV}:{path}"],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if proc.returncode != 0:
            manifest_bad.append(f"{path}:unresolvable")
            continue
        want = hashlib.sha256(proc.stdout).hexdigest()
        if not re.search(rf"^read-input: {re.escape(path)} {want}$", receipt, re.MULTILINE):
            manifest_bad.append(f"{path}:manifest_mismatch")
    log_text = read(root, LOG) or ""
    score_text = read(root, SCORE) or ""
    lesson_final = read(root, LESSON_FINAL) or ""
    # revision 2: the repeats must carry the corrected revision, not a bare
    # marker (RevReceipts MEDIUM-6: a bare 'Correction (round 65, R1)'
    # satisfied the revision-1 leg while LOG/SCORECARD still said 95c9194e).
    def _correction_names(text, marker):
        idx = text.find(marker)
        if idx == -1:
            return False
        window = text[idx:idx + 600]
        return TRUE_REV[:8] in window or TRUE_REV in window
    r1_repeats_ok = (_correction_names(log_text, "Correction (round 65, R1)")
                     and _correction_names(score_text, "Correction (round 65, R1)")
                     and _correction_names(lesson_final, "Correction (round 65, R1)"))
    r1_ok = all(r1_checks.values()) and not manifest_bad
    leg("R1", r1_ok and r1_repeats_ok,
        f"checks={r1_checks} manifest_bad={manifest_bad} "
        f"repeats_log_score_lessonfinal={r1_repeats_ok}")

    # ---------- R2: named correction, append-only ----------
    rev_text = read(root, REV63) or ""
    base_code, base_rev = git_out(root, ["show", f"{BASE}:{REV63}"])
    r2_original_intact = base_code == 0 and base_rev == rev_text[:len(base_rev)] and base_rev.strip() and rev_text.startswith(base_rev.rstrip("\n"))
    r2_named = "Correction (round 65, R2)" in rev_text and "final-measures-c.txt" in rev_text
    _r2_idx = rev_text.find("Correction (round 65, R2)")
    _r2_window = rev_text[_r2_idx:_r2_idx + 800] if _r2_idx != -1 else ""
    r2_asserts_false = ("is false" in _r2_window or "false clause" in _r2_window)
    # RevengerR2R3: substance must pin the true adder (0c892ce) and the
    # absent-at-8d2041fa fact, and the LOG repeat of the falsehood must be
    # corrected there too (LOG.md carried the same 8d2041fa claim).
    r2_substance = "0c892ce" in _r2_window and "8d2041fa" in _r2_window
    _r2l_idx = log_text.find("Correction (round 65, R2)")
    _r2l_window = log_text[_r2l_idx:_r2l_idx + 900] if _r2l_idx != -1 else ""
    r2_log_ok = _r2l_idx != -1 and "0c892ce" in _r2l_window and "8d2041fa" in _r2l_window
    r2_named = r2_named and r2_asserts_false and r2_substance and r2_log_ok
    leg("R2", r2_original_intact and r2_named,
        f"original_intact={r2_original_intact} named={r2_named} "
        f"substance={r2_substance} log_repeat={r2_log_ok}")

    # ---------- R3: wrong-path citation corrected in lane records ----------
    _r3_idx = score_text.find("Correction (round 65, R3)")
    _r3_window = score_text[_r3_idx:_r3_idx + 800] if _r3_idx != -1 else ""
    r3_ok = ("w1/ReviewerCa.md" in log_text
             and "w2/ReviewerCa.md" in log_text
             and "Correction (round 65, R3)" in score_text
             and "w1/ReviewerCa.md" in _r3_window
             and ("actual path" in _r3_window or "actual:" in _r3_window))
    leg("R3", r3_ok, f"log_names_actual_and_wrong={r3_ok}")

    # ---------- R4: honest mutant wording, predicate unchanged ----------
    claims = read(root, CA64_CLAIMS) or ""
    r4_ok = False
    r4_detail = "claims_unreadable"
    try:
        cj = json.loads(claims)
        oc = next(c for c in cj["claims"] if c["id"] == "O")
        pred_exact = oc.get("predicate") == FROZEN_O_PREDICATE
        corr = oc.get("statement_correction", {})
        corr_json = json.dumps(corr)
        corr_ok = ("at least their pinned leg" in corr_json
                   and "EDGE_USERINFO" in corr_json
                   and "EDGE_MALTARG" in corr_json)
        # MutRecords M3: the predicate field must be byte-exact (done above),
        # and the original statement must stay byte-equal to its base version
        # (append-only discipline - the historical wording persists with the
        # correction riding beside it).
        base_claims_proc = subprocess.run(
            ["git", "-C", root, "show", f"{BASE}:{CA64_CLAIMS}"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        statement_unchanged = False
        if base_claims_proc.returncode == 0:
            try:
                bcj = json.loads(base_claims_proc.stdout.decode("utf-8"))
                boc = next(c for c in bcj["claims"] if c["id"] == "O")
                statement_unchanged = oc.get("statement") == boc.get("statement")
            except (ValueError, KeyError, StopIteration):
                statement_unchanged = False
        r4_ok = pred_exact and corr_ok and statement_unchanged
        r4_detail = (f"pred_exact={pred_exact} correction={corr_ok} "
                     f"statement_unchanged={statement_unchanged}")
    except (ValueError, KeyError, StopIteration) as error:
        r4_detail = f"json_error={error}"
    leg("R4", r4_ok, r4_detail)

    # ---------- R5: control-o binding named ----------
    control = read(root, CONTROL_O) or ""
    r5_in_control = ("c27a9fef" in control and "b7d22703" in control
                     and "revision 3" in control)
    binding = read(root, "reports/round-64/telemetry/control-o-binding.txt") or ""
    r5_record = ("control-o binding" in log_text.lower()
                 or "Control-O binding" in log_text)
    r5_named = ("c27a9fef" in binding and "b7d22703" in binding
                and "revision 3" in binding)
    leg("R5", r5_in_control and r5_record and r5_named,
        f"in_control={r5_in_control} in_log={r5_record} named_binding={r5_named}")

    # ---------- R6: R64-M12 status correction ----------
    lesson64 = read(root, R64_LESSON) or ""
    _r6_idx = lesson64.find("Correction (round 65, R6)")
    _r6_window = lesson64[_r6_idx:_r6_idx + 800] if _r6_idx != -1 else ""
    r6_ok = ("Correction (round 65, R6)" in lesson64 and "R64-M12" in lesson64
             and "R64-M12" in _r6_window)
    leg("R6", r6_ok, f"status_correction={r6_ok}")

    # ---------- R7: entry verified-at line corrected ----------
    entry = read(root, R64_ENTRY) or ""
    m = re.search(r"^- verified-at:.*$", entry, re.MULTILINE)
    verified_at = m.group(0) if m else ""
    value = verified_at.split(":", 1)[1].strip() if m and ":" in verified_at else ""
    r7_ok = (m is not None
             and len(value) > 10
             and "2026" in value
             and "round-64" in value
             and not re.search(r"skeleton|await L1|pending insertion|to be inserted|re-opened",
                               verified_at, re.IGNORECASE))
    leg("R7", r7_ok, f"line={verified_at[:90]!r}")

    # ---------- CRITERION: QUALITY 17 ----------
    quality = read(root, QUALITY) or ""
    cand = [l for l in quality.splitlines() if re.match(r"^1[7-9]\.\s", l)]
    r_criterion = (any("tree hash" in l for l in cand)
                   and not any(re.search(r"need not|must not|optional", l, re.IGNORECASE) for l in cand))
    leg("CRITERION", r_criterion, f"candidates={len(cand)} negation_free={r_criterion}")

    # ---------- QUOTES: round-65 lesson Gate rows ----------
    lesson_path = os.path.join(root, R65_LESSON)
    q = subprocess.run([sys.executable, "-B", "tools/check-gate-quotes.py", lesson_path],
                       cwd=root, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    q_out = q.stdout.decode("utf-8", "replace")
    # revision 2 (pre-data; forcing control .ufo/waves/round-65/w1/RevLessonFinal.md
    # HIGH: a '(no rows yet)' body or a wrong heading prints the clean 0-findings
    # summary - exit 0 or 2 - so presence of all 26 Gate rows is required here).
    gate_ids = set()
    lesson_ok = os.path.isfile(lesson_path)
    if lesson_ok:
        ltext = open(lesson_path, encoding="utf-8").read()
        gate_section = ltext.split("## Gate", 1)[-1].split("\n## ", 1)[0] if "## Gate" in ltext else ""
        gate_ids = set(re.findall(r"\bS(75\d|76\d|77[0-5])\b", gate_section))
    r_quotes = (q.returncode == 0
                and re.search(r"(^|\s)0 finding", q_out) is not None
                and lesson_ok
                and len(open(lesson_path, encoding="utf-8").read().splitlines()) > 10
                and len(gate_ids) == 26)
    leg("QUOTES", r_quotes,
        f"exit={q.returncode} lesson_exists={lesson_ok} gate_rows={len(gate_ids)}/26 "
        f"clean={'0 finding' in q_out}")

    # ---------- RECEIPTS: the R1 class generalized to this round's own
    # receipts (MutReceipts M1-M4: wrong counter sha, stale sha, declaration-
    # commit stamp, missing tree line all survived at base).  Each round-65
    # final-measures receipt must name the LANDS commit (main^ while the
    # receipts themselves ride the records commit), its tree, and the sha256
    # of the counter that produced it. ----------
    receipt_reqs = [
        ("reports/round-65/telemetry/final-measures-c.txt", "reports/round-65/accept-c.py"),
        ("reports/round-65/telemetry/final-measures-o.txt", "reports/round-65/accept-o.py"),
        ("reports/round-65/telemetry/final-measures-ca.txt", "reports/round-65/accept-ca.py"),
    ]
    lands_code, lands_out = git_out(root, ["rev-parse", "main^"])
    lands = lands_out.strip()
    lands_tree_code, lands_tree_out = git_out(root, ["rev-parse", "main^^{tree}"])
    lands_tree = lands_tree_out.strip()
    rec_bad = []
    if lands_code != 0 or lands_tree_code != 0 or not lands:
        rec_bad.append("lands_unresolvable")
    else:
        for rpath, cpath in receipt_reqs:
            rtext = read(root, rpath)
            if rtext is None:
                rec_bad.append(f"{rpath}:absent")
                continue
            cblob = open(os.path.join(root, cpath), "rb").read()
            csha = hashlib.sha256(cblob).hexdigest()
            if f"measured revision: {lands}" not in rtext:
                rec_bad.append(f"{rpath}:lands_stamp")
            if not re.search(rf"^tree: {re.escape(lands_tree)}$", rtext, re.MULTILINE):
                rec_bad.append(f"{rpath}:tree")
            if f"counter sha256: {csha}" not in rtext:
                rec_bad.append(f"{rpath}:counter_sha")
    leg("RECEIPTS", not rec_bad, f"lands={lands[:8] if lands else None} bad={rec_bad}")

    verdict = all(legs)
    print(f"ACCEPT-CA-65: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
