# R28-C47/C48 verify — independent re-measurement of the README reconciliation and the entry audit

- **seat:** R28-C47..C48 verify leg. **lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- **date:** 2026-10-18. **HEAD:** `69cecbc7dcf575a29f29660ecac470e05260fd86`.
  **stamps:** 20:13:39Z (revision 1.8, 200 entries) and **20:20:50Z (final,
  binding, revision 1.9, 201 entries)**.
- **canon:** NON-CANON engineering evidence; admits nothing, certifies no round.
- **what this file is:** the reconciliation's and the audit's measurements re-run
  from fresh processes, with before/after and negative controls. It is
  **same-seat** verification — a re-measurement with controls, not
  independent-seat review — and that limit is restated in §5 rather than hidden.

## V1 — the sweep re-run (fresh process)

```sh
export TMPDIR=$PWD/.scratch
python3 -B reports/round-28/readme/sweep.py            # exit 0
# parts {"civilizations": 94, "culture-material": 18, "linguistics": 21,
#        "myth-symbol": 19, "synthesis": 29, "verification": 20}
# rows 201 files 201
# missing_from_index 0 []   topic_mismatch 0 []
# orphan_rows 0 []          header_drift {}
# totals_line 201 totals_ok True
# footer {"total": 201, "dir_totals": [21, 19, 18, 29, 20, 94]}
# footer_findings [] footer_ok True
# readme_sha256 053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c
python3 -B reports/round-28/readme/sweep.py --json     # same result as JSON
python3 -B reports/round-28/readme/sweep.py --selftest # exit 0, 12/12
```

The pre-landing reading (20:13:39Z) was 200 rows / 200 files with the same zero
mismatches; the only delta is the round-28 ceiling row and the counts that
follow it.

## V2 — the before/after control (the repair's own claim, tested)

The repair asserts two things: the footer was stale, and round 27's instrument
could not have caught it. Both were tested by replaying both instruments over
the committed `HEAD` bytes:

```sh
git show HEAD:corpus/README.md > .scratch/r28-readme-before.md
python3 -B reports/round-28/readme/sweep.py --readme .scratch/r28-readme-before.md
#   footer_findings: FOOTER_TOTAL 199 vs 200;
#                    FOOTER_DIR_TOTALS [19,19,18,29,20,94] vs [20,19,18,29,20,94]
#   exit 1
python3 -B reports/round-27/readme/sweep.py --readme .scratch/r28-readme-before.md
#   rows 200 files 200; 0 missing; 0 topic mismatches; totals_ok True; exit 0
python3 -B reports/round-28/readme/sweep.py            # exit 0 (working tree, fixed)
```

Round 27's sweep is **green on the defective bytes**; round 28's is red on them
and green after the fix. The blind spot is measured, not asserted.

## V3 — counts re-derived by a second, independent method

```sh
python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge
# totals.files 201; per-dir 94/18/21/19/29/20
for d in linguistics myth-symbol culture-material synthesis verification civilizations; do
  find corpus/knowledge/$d -maxdepth 1 -name '*.md' -type f | wc -l; done
# 21 19 18 29 20 94
find corpus/knowledge -maxdepth 2 -name '*.md' -type f | wc -l   # 201
```

Both agree with the footer revision 1.9 carries and with the `Total knowledge
entries: 201.` line.

## V4 — the audit re-run (fresh process)

```sh
python3 -B reports/round-28/audit/entry-audit.py --selftest   # 11/11, exit 0
python3 -B reports/round-28/audit/entry-audit.py --all        # exit 0
# audited 201; bar clear 17; bar failing 184
# indexed 201; index clear 201; index failing 0
python3 -B reports/round-28/audit/entry-audit.py --all --strict-bar   # exit 1 (the legacy bar)
python3 -B reports/round-28/audit/entry-audit.py \
    --new corpus/knowledge/linguistics/register-lexicon-ceilings.md   # exit 0
# new .../register-lexicon-ceilings.md bar=True filler=False src=11/11 index=[]
```

The index leg is the hard check and is clean for all 201 entries. The bar leg's
184 is reported and interpreted, not laundered: the gap discipline postdates
most of the corpus, and `--strict-bar` exists so a caller that wants the strict
reading gets a failing exit rather than a footnote. The round-28 ceiling entry
clears the full bar, so the round's own admission claim is measured.

## V5 — the preservation control and the final claim-C reading (the runner, read back)

The README change must not disturb any protected round-8..27 byte. The round-28
runner measures exactly that:

```sh
python3 reports/round-28/run-validation.py --check
# at 20:13Z: C failures: 2 — both the peer ceiling seats' deliverables
#   "no new section was added to .../register-strata-attestation.md"
#   "no new entry landed under corpus/knowledge/linguistics"
# at 20:20Z: C failures: []  <-- the entry landed; the README indexes it
#   corpus_readme: revision_head "1.9", partition_headers
#     {"civilizations": 94, "culture-material": 18, "linguistics": 21,
#      "myth-symbol": 19, "synthesis": 29, "verification": 20}, mismatches {}
# protected_filed_artifacts: no differences reported for the README edit
```

The README edit fails neither the preservation check nor any claim-C leg; at the
final stamp claim C reports `failures: []`, with the runner's own `corpus_readme`
measurement reading `mismatches {}` and partition headers reproducing the tree.

## V6 — limits of this verification

- **Same-seat.** The instruments, the receipts and this file are one seat's
  work. The controls are planted, not an independent reader. Independent
  corroboration is the round-28 runner's `measure_ceiling_entry`, which reads
  the delivered bytes itself and reports `failures: []`.
- **Point-in-time.** The final reading is at 20:20:50Z, revision 1.9, 201
  entries. The tree moves under the round; re-run before quoting any count.
- **Non-canon.** A reconciled index and a green structural sweep do not certify
  historical truth, and neither seat admits anything into the corpus.
