# ScribeR66Scorecard — round-67 stage draft of the missing SCORECARD round-66 table

Seat: ScribeR66Scorecard (scribe, round 67). Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin
(base `ad5b52b0`). Read-only against the lane: no product code, SCORECARD.md, LOG.md, counters,
judge, `.git`/`.jj` or index was written; the only writes are the two artifacts named below.
No tools installed or upgraded.

## Behavior (what was produced)

`## Axes — round 66 (2026-10-24, hyaku run 5, L1 KotodamaR66)` written in the round-65 house
shape: heading with date/label, baseline→lands→records intro with the wave shape and the dead
seat, the four-row `| axis | verdict | before → after / observation | re-run command | measured
evidence |` table, an admission paragraph, a round-66 receipt-correction block, and the
`Stale-lane:` line.

Axis verdicts, taken from the non-author spot-check §6 (`corpus/lessons/round-66-verifier-spotcheck.md`):
coverage improved, operability improved, calibration unprovable, depth/freshness/adjacency unchanged.
Admission: **not admitted** (`admitted = false`, verdict `rejected-honest-stop`), not the filed
report's self-assessment.

## Gates (what the draft asserts, and the exact bytes behind each)

- C: `ACCEPT-C-66: PASS` (13 receipt lines = 12 declared legs + REVISION pre-leg) —
  `reports/round-66/telemetry/final-measures-c.txt`; `dry-run-c.txt` FAIL at base; `controls-c.txt`.
- O: `ACCEPT-O-66: PASS` (10 receipt lines = 9 declared legs + REVISION) —
  `reports/round-66/telemetry/final-measures-o.txt`; separator `SEPARABILITY: 8 findings`,
  `acceptance_runs=9 skipped=0` — `telemetry/separability-real.txt`.
- Ca: `ACCEPT-CA-66: FAIL`, `D2 FAIL bad=[…:no_carrier]` ×3 —
  `reports/round-66/telemetry/final-measures-ca.txt`. D1/D3/D4/CRITERION/QUOTES PASS in the same
  receipt.
- Counts re-derived read-only with `git show <rev>:corpus/SOURCES.md | grep -cE '^\| S[0-9]{3} '`
  and `git ls-tree -r --name-only <rev> -- corpus/knowledge`: rows 701 (`94209e8f`) → 724
  (`65fe8572` and `4589ebdd`); entries 239 → 240; culture-material 32 → 33.
- Post-records re-derivation of the Ca D2 failure (cheap read-only facts, no counter re-run):
  carrier `git log -1 main -- final-measures-ca.txt` = `4589ebdd`, its parent = `65fe8572` = the
  receipt's stamped measured revision, `git rev-parse 65fe8572^{tree}` = `f0681e6e…` = the
  receipt's tree line, and each receipt's counter-sha line equals `sha256` of the counter blob at
  lands (c `987c4bbc…`, o `b366c25b…`, ca `f206095b…`).

## Touched surfaces

- `.ufo/waves/round-67/stage/scorecard-r66.md` (new draft; not integrated into SCORECARD.md).
- `.ufo/waves/round-67/w1/ScribeR66Scorecard.md` (this report).

## Out of scope / limits

- No frozen counter was executed (no re-run to decorate the report); every number above is read
  from committed receipts or from read-only `git show`/`ls-tree`/`sha256sum`.
- The draft is stage-only: insertion order and section placement are the L1's.
- No review of whether the entry's lore handoff is semantically adequate (claim C `review_only`).
- Freshness: no scoring attempted; the round-11 L0 pause is recorded, not re-litigated.

## Findings

1. **HIGH — the filed report contradicts the committed Ca receipt.** `.ufo/reports/round-66/kotodama.md`
   says "Verdict: ACCEPT-CA-66 PASS (`final-measures-ca.txt`, stamped revision = lands rev per
   criterion 17)" and "D2 PASS (receipts parented on the lands commit)", while the receipt prints
   `D2 FAIL bad=['reports/round-66/telemetry/final-measures-c.txt:no_carrier',
   '…-o.txt:no_carrier', '…-ca.txt:no_carrier']` and `ACCEPT-CA-66: FAIL`. Cause is R66-D3
   sequencing (receipts stamped at lands `65fe8572`, run before the records commit `4589ebdd`
   existed, so `git log -1 main -- <receipt>` at `accept-ca.py:113-125` found no carrier). The
   draft grades calibration unprovable and quotes both strings; the canonical Rust judge should
   see the conflict, not a resolution.
2. **MEDIUM — the assignment's coverage arithmetic does not add up.** "+22 rows 701->724" implies
   701+22=723; the re-derived net is +23 (22 new rows S779-S800 plus the S776 supersession repair
   row), 724 at `65fe8572`. Draft uses +23 and records the discrepancy in the correction block.
3. **MEDIUM — O's do-nothing control is not a base-tree FAIL.** `reports/round-66/telemetry/dry-run-o.txt`
   is stamped `measured revision (lane main): 94209e8f…` and prints all nine declared legs PASS plus
   `ACCEPT-O-66: PASS`, because the DIFF leg reads the already-modified worktree tool. The actual
   base-bytes control is a different probe (`controls-o.txt`: extracted base tool sha `5764ea27…`
   refuses `--jobs/--budget/--max-runs/--static-only`). Under the frozen-predicate rule ("a counter
   a do-nothing control passes is revised before data") this is an unmet control shape for O, not
   a false hardening; the spot-check scored operability improved without noting it. Draft discloses
   it in the O row.
4. **MEDIUM — separability expectations vs output.** `claims.json` declares 2 expected findings
   (`Ca->REC` class) but `separability-real.txt` prints 8, including `Ca->C`, `Ca->O`, `Ca->R`×4,
   `Ca-><base>`, `O-><base>`. The claims' own note says undeclared `Ca->C`/`Ca->O`-class findings
   would be "a real defect"; the filed report calls them by design. Not adjudicated; the draft
   states the counts and both readings.
5. **LOW — counter leg labels.** `ROWS PASS bad=[] n=0` in both C receipts means 0 bad rows (n is
   the bad list length), not zero rows checked; a reader can misread this as an empty scan.
6. **LOW — R66-D4 is still open at the lane tip.** `grep -n 'round 66' SCORECARD.md` and
   `LOG.md` return no round-66 section/entry; this draft is the SCORECARD half and is unintegrated.
   The SHONEN box-2 pointer remains unchecked until the L1 lands both halves.

## Addendum (same seat, post-report)

L1 resolved the r67 claim-C APPEND vs claim-Ca D4/D5 id conflict by per-claim lands separation
(A_r < A_c < A_ca), not by counter/claims revision: at A_c the appended set is S805-S828 plus
S801-S804 (= NEW_IDS ∪ EXTRA_IDS, registry 724 → 752 per claim C's own statement), while the S829+
reject rows exist only at A_ca, whose D5 then sees >=6 today-dated rejects (S801-S804 + >=2 new).
The code bounds this resolves were read (accept-c.py:70 `EXTRA_IDS`, :357 `allowed_new`;
accept-ca.py:235 `rej_opened_today < len(R66_REJECTS) + 2`), but the sequencing itself is L1's
decision, not seat-verified here. This does not alter the round-66 draft or findings 1-6; finding
4's declared-vs-printed mismatch was reconciled by prose in r66 and the spot-check rejected that,
which is the precedent for choosing pre-data sequencing over post-hoc reconciliation.

Report: .ufo/waves/round-67/w1/ScribeR66Scorecard.md
