#!/usr/bin/env python3
r"""Round-64 claim Ca acceptance, revision 2 (pre-data).

Claim Ca (calibration): resolve the round-63 closure's routed bookkeeping
defects (corpus/lessons/round-63-verifier-spotcheck.md section 6) in the lane
repo, each verified by one counting leg over committed bytes:

  CANONLOG  defect 1 - the canonical root LOG.md carries a Round-64 entry
            before any corpus/LOG.md content; corpus/LOG.md is the stray
            round-63 file, now pointed at from the canonical file.
  PTRS     defect 2 - SCORECARD.md's round-63 correction rows and
            corpus/LOG.md no longer cite reports/round-63/telemetry/
            final-measures.txt (the receipts are final-measures-o.txt and
            final-measures-c.txt).
  HISTOGRAM defect 3 - the SCORECARD round-63 correction rows recompute the
            headgear tier split as A=13 B=11 over the committed registry
            (S694-S717 at the round base), matching the census command.
  DISPO    defect 4 - the round-64 LOG entry records explicit dispositions of
            the round-62 routed items 5, 6 and 7 (the r62 lesson is left
            byte-unchanged; item 7's S693 kind decision and the S687 status
            flip are named).
  REVNAMES defect 8 - reports/round-63/telemetry/revisions.txt names the
            measured revision of every r63 receipt that lacked one: 8d2041fa
            for final-measures-c.txt, 38ec1316 for final-measures-o.txt and
            rev-separability.txt, 0c892ce for census-end.txt, and 80ff34c
            as the commit that carried the final-measures record.
  NITS     defect 9 - the SCORECARD round-63 correction row and the round-64
            LOG entry correct the three numeric nits (45 vs 47 seat reports,
            W04 rows named as S650/S651 vs 27 duplicate-URL rows, 6 vs 9
            dry-run FAIL legs).
  R63SEP   defect 10 - the round-64 LOG entry records the round-63
            separability re-run result (SEPARABILITY: 2 findings, exit 1)
            and names the dependency class (counters are REC lands, read by
            the acceptance runs; not an inter-claim dependency).

Run from the lane root:

  python3 -B reports/round-64/accept-ca.py [--root DIR]

Revision history (pre-data):
- revision 2: NITS requires the affirmative Round-63 numeric-corrections
  record with the correct old-to-new values; forcing controls:
  `.ufo/waves/round-64/w1/CriticCa.md`,
  `.ufo/waves/round-64/w2/CriticRevCa.md`, and
  `.ufo/waves/round-64/w2/RevVerifyCa.md`.
Frozen predicate (the same sentence in reports/round-64/claims.json and in
every receipt): ACCEPT-CA-64: every leg of reports/round-64/accept-ca.py
prints PASS.
Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input.
"""
import argparse
import os
import re
import subprocess
import sys

BASE = "ff30a205c8d23b35f1ac533740121a955a9fda96"
CANON = "LOG.md"
STRAY = "corpus/LOG.md"
SCORE = "SCORECARD.md"
REV = "reports/round-63/telemetry/revisions.txt"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    legs = []

    def leg(name, ok, detail):
        legs.append(ok)
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")

    def read(rel):
        with open(os.path.join(root, rel), encoding="utf-8") as fh:
            return fh.read()

    # ---------- CANONLOG ----------
    try:
        canon = read(CANON)
        stray = read(STRAY)
    except (OSError, UnicodeDecodeError) as error:
        print(f"ACCEPT_CA_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    r64_idx = canon.find("## Round 64")
    stray_idx = stray.find("## Round 63")
    has_r63 = stray_idx != -1
    canon_point = "corpus/LOG.md" in canon[max(0, r64_idx):r64_idx + 800]
    # revision 1 (pre-data, forced by telemetry/dry-run-ca.txt): the canonical
    # LOG.md writes its entries as `## <date> — Round N`, so a `## Round` count
    # can never exceed 6; the proof counts round-bearing headings instead.
    proof = len(re.findall(r"^## .*Round", canon[:max(0, r64_idx)], re.MULTILINE))
    leg("CANONLOG", r64_idx != -1 and has_r63 and canon_point and proof > 50,
        f"r64_at={r64_idx} stray_has_r63={has_r63} points_at_stray={canon_point} prior_rounds={proof}")

    # ---------- PTRS ----------
    # revision 1 (pre-data, forced by telemetry/dry-run-ca.txt): the dead
    # pointer is a round-63 receipt, while rounds 51-58 legitimately cite their
    # own final-measures.txt; the leg reads the round-63 SCORECARD block only.
    score = read(SCORE)
    block = score.split("## Axes — round 63", 1)
    r63_block = block[1].split("\n## ", 1)[0] if len(block) == 2 else ""
    dead = "final-measures.txt" in r63_block
    stray_dead = "final-measures.txt" in stray
    fixed_o = "final-measures-o.txt" in r63_block and "final-measures-o.txt" in stray
    fixed_c = "final-measures-c.txt" in r63_block and "final-measures-c.txt" in stray
    leg("PTRS", not dead and not stray_dead and fixed_o and fixed_c,
        f"score_dead={dead} stray_dead={stray_dead} o_fixed={fixed_o} c_fixed={fixed_c}")

    # ---------- HISTOGRAM (over committed base registry) ----------
    proc = subprocess.run(["git", "-C", root, "show", f"{BASE}:corpus/SOURCES.md"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    base_reg = proc.stdout.decode("utf-8", "strict")
    tiers = {}
    for line in base_reg.splitlines():
        m = re.match(r"^\|\s*S(69[4-9]|7[01][0-9])\s*\|", line)
        if m:
            cells = [c.strip() for c in line.split("|")[1:-1]]
            if len(cells) >= 10:
                tiers[cells[3]] = tiers.get(cells[3], 0) + 1
    corr = "A 13 / B 11" in score or "A=13 B=11" in score or "13 / 11" in score
    leg("HISTOGRAM", tiers == {"A": 13, "B": 11} and corr,
        f"tiers={tiers} correction_present={corr}")

    # ---------- DISPO ----------
    dispo = "item 5" in canon and "item 6" in canon and "item 7" in canon
    s687 = "S687" in canon and "queued" in canon
    s693 = "S693" in canon and "docs" in canon
    leg("DISPO", dispo and s687 and s693,
        f"items5_7={dispo} s687_flip={s687} s693_kind={s693}")

    # ---------- REVNAMES ----------
    try:
        rev = read(REV)
    except (OSError, UnicodeDecodeError):
        rev = ""
    need = ["8d2041fa", "38ec1316", "0c892ce", "80ff34c",
            "final-measures-c.txt", "final-measures-o.txt",
            "rev-separability.txt", "census-end.txt"]
    if all(n in rev for n in need):
        rev_ok = True
    else:
        rev_ok = False
    # revision 1 (pre-data): the docstring declared REVNAMES but the rev-0 code
    # computed rev_ok and never printed or counted it (dry-run receipt shows 6
    # legs against 7 declared in reports/round-64/claims.json).
    leg("REVNAMES", rev_ok, f"missing={[n for n in need if n not in rev]}")

    # ---------- NITS ----------
    # revision 2 (pre-data; forcing controls:
    # .ufo/waves/round-64/w1/CriticCa.md,
    # .ufo/waves/round-64/w2/CriticRevCa.md, and
    # .ufo/waves/round-64/w2/RevVerifyCa.md): bind values to the positive
    # Round-63 correction record and its old-to-new numeric associations.
    r64_heading = re.search(r"^## Round 64\b", canon, re.MULTILINE)
    if r64_heading:
        after_heading = canon[r64_heading.end():]
        next_heading = re.search(r"^## (?!#)", after_heading, re.MULTILINE)
        r64_end = r64_heading.end() + next_heading.start() if next_heading else len(canon)
        r64_log = canon[r64_heading.start():r64_end]
    else:
        r64_log = ""
    nits_record = re.search(
        r"(?im)^[ \t]*(?:-[ \t]*)?(?:\*\*)?Round-63 numeric corrections(?::\*\*|\*\*:|:)[ \t]*(.*?)[ \t]*$",
        r64_log)
    nits_text = nits_record.group(1) if nits_record else ""
    seat_reports_nit = bool(re.search(
        r"\b47 seat reports landed,[ \t]*not 45\b", nits_text, re.IGNORECASE))
    duplicate_url_nit = bool(re.search(
        r"\bW04 covers 27 duplicate-URL rows,[ \t]*not (?:just )?S650/S651\b",
        nits_text, re.IGNORECASE))
    fail_legs_nit = bool(re.search(
        r"\bACCEPT-O-63 dry run had 9 FAIL legs\b[^.\n]*\bnot 6\b",
        nits_text, re.IGNORECASE))
    record_exact = bool(re.fullmatch(
        r"47 seat reports landed, not 45; W04 covers 27 duplicate-URL rows, "
        r"not (?:just )?S650/S651; the ACCEPT-O-63 dry run had 9 FAIL legs"
        r"(?: \([^)]*\))?, not 6\.",
        nits_text, re.IGNORECASE))
    nits = (nits_record is not None and record_exact and seat_reports_nit
            and duplicate_url_nit and fail_legs_nit)
    leg("NITS", nits,
        f"correction_record={nits_record is not None} record_exact={record_exact} "
        f"seat_reports_nit={seat_reports_nit} duplicate_url_nit={duplicate_url_nit} "
        f"fail_legs_nit={fail_legs_nit}")

    # ---------- R63SEP ----------
    sep = "SEPARABILITY: 2 findings" in canon and "exit=1" in canon
    dep_class = "REC" in canon and "record dependency" in canon
    leg("R63SEP", sep and dep_class, f"result_cited={sep} dep_class_named={dep_class}")

    verdict = all(legs)
    print(f"ACCEPT-CA-64: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
