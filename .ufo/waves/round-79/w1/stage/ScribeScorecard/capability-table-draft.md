# Capability table draft — round 79 (ScribeScorecard, W1; draft only, nothing entered)

Rule applied: `AXES.md` §Capabilities — "Rows enter only through a round that demonstrates the capability running; a
capability without a passing demonstration in the round report is pre-claiming and does not enter the table."
Therefore **no row is added in W1**. The O row below is a pre-entry draft for L1 to hold until a round report
carries a passing run.

## A. Pending O row (NOT to enter until a passing run is in the round report)

| name | demonstrated behavior | command / evidence | first working |
|---|---|---|---|
| ledger-token guard (pending) | Re-runs approved read-only observations against committed bytes at a pinned revision, rejects mutable revisions, `observed_at_base` mismatches and stated==observed tokens | `python3 -B tools/ledger-token-guard.py --selftest` and the frozen acceptance command, both with output preserved in the round telemetry | pending — round 79 not yet demonstrated |

Placeholder rule: the "demonstrated behavior" cell is written only from observed passing output. Until then the
row is absent from the table, not present with "pending". (The draft text above is for L1's review; it is not a
table entry.)

Notes for L1 when O lands:
- The name must describe what the guard can now do, not the claim letter.
- The O guard reads committed bytes at the lands revision; the evidence pointer must name `--lands` and `--freeze`
  values, per QUALITY 19/25.
- Scope words: "ledger-token guard for this lane's calibration records" only. No "security", "coverage" or
  "general verifier" wording; the claims draft already rejects those.

## B. Proposed append-only correction for the existing `sources registry` row (NOT applied; draft for L1/ScribeCorrection)

Do not edit the row in place. Append under a new heading in SCORECARD.md (lane convention: `## Corrections — round N`):

```
## Corrections — round 79 (append-only; the capability row at line 54 is left as filed)

| row | old figure (as filed) | new figure (observed) | re-derivation command |
|---|---|---|---|
| capabilities: sources registry | 43 rows: A 34 / B 3 / C 6; mined 20 / queued 19 / rejected 4 (measured at 8c78e6b) | 820 rows: A 493 / B 311 / C 16; mined 725 / queued 58 / rejected 37 (measured at 4b255745dea45a45d88b17e3c3fea4cdb6700cf7; same bytes at HEAD 44f76d4) | git show 4b255745dea45a45d88b17e3c3fea4cdb6700cf7:corpus/SOURCES.md \| awk -F'\|' '/^\| *S[0-9][0-9][0-9]+ *\|/{gsub(/ /,"",$9); print $9}' \| sort \| uniq -c |
```

Notes:
- The new figure is from committed bytes (probe P1 in `probe-raw.txt`). The corrected statement is a count, not a
  score; no axis verdict moves from it.
- The `rows(...)` count in the probe uses `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'`
  (820 at 4b255745 and HEAD). The `awk` in the table above counts status cells and gives 725+58+37 = 820.
- Whether this row needs a *calibration* record at all, or only an appended correction under no claim, is L1's
  decision; per QUALITY 20 a records-only repair declares both trends `unchanged`.

## C. Non-row observations (not capability evidence)

- The capability table has no column for "as-of" date. Adding one would be a structural change to SCORECARD and is
  not proposed here; the correction in §B carries the date in its own cell instead.
- No other capability row was checked in W1; other rows cite historical round commands and were not re-run.
