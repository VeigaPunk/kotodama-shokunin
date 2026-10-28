# RevClaimsHonesty — round 76 W2

## Verdict

The round-76 SCORECARD's top-line trend verdicts are appropriately conservative: both C and Ca are marked failed as declared, no score delta is claimed, and the conclusion says neither frozen counter passes. I found no basis to recommend admission or an improved axis verdict. The failure measurements support those statements.

## Findings

### Medium — SCORECARD understates the breadth of the Ca acceptance failure

`SCORECARD.md:1543` summarizes the failed Ca measurement as “L76-13/19 ledger defects plus repair/annotate/fixture/combined failures remain.” The frozen counter output is more specific and exposes additional distinct blockers: `reports/round-76/telemetry/measures-ca.txt:4-11` records LEDGER failures on L76-13 and L76-19; REPAIR failure L76-16; three unannotated rows because L76-19/20/21 rederive commands are not executable; NOSTUB failures for all three; missing committed R1EXEMPT receipts; SEPARABLE failure for L76-13's forbidden knowledge-path read; and COMBINED failure for the C-owned README change and invalid `owned_inplace` line number. The scorecard's shorthand does not falsely claim success, but obscures important, independently actionable failure classes (especially SEPARABLE and the specific combined-tree ownership conflict). Recommend listing or linking the actual failed legs, rather than compressing them into “repair/annotate/fixture/combined.”

### Low — SCORECARD's C failure summary is accurate but omits the exact defect

`SCORECARD.md:1542` correctly says C fails 11/13 with ROWS and COLLCHECK red. The evidence gives the concrete cause: `reports/round-76/telemetry/measures-c.txt:26` ROWS rejects two added registry lines outside the frozen row set; `:38-39` COLLCHECK says map record S938→S895 names a document different from the row. The lesson does disclose these blockers at `corpus/lessons/round-76.md:85-89`, so this is not a missing overall disclosure, but the SCORECARD axis row would be more useful if it named the exact mismatch instead of only leg labels.

## Evidence supporting conservative verdict

- C is `FAIL legs=11/13`, exit 1 (`reports/round-76/telemetry/measures-c.txt:24-46`).
- Ca is `FAIL legs=5/12`, exit 1 (`reports/round-76/telemetry/measures-ca.txt:4-16`).
- The SCORECARD explicitly says “failed as declared; no score delta” for both axes and “Neither claim's frozen acceptance counter passes” (`SCORECARD.md:1542-1545`).
- Ca's corrections section expressly limits its table: it is “not an assertion that the frozen Ca counter accepts them” (`SCORECARD.md:1535`).

## Residual risk / verification gaps

This review used the committed lane telemetry and round-76 report wording available in the checkout; I did not rerun counters or tests. No installs, scratch files, or source/report edits outside this seat report.