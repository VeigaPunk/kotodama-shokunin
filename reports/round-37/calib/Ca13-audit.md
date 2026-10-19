- Seat: Ca13 | verifier | calibration mismatch disposition audit | date 2026-10-19 | baseline 57c8409

# Ca13 — disposition audit

## Status

**Could-not-evaluate; no pass claimed.** The required round-37 recount inventory and ledger were not available at inspection. `Glob reports/round-37/calib/*.md` returned only `Ca09-coverage.md` and `Ca16-final-verify.md`. Ca09 reports that `reports/round-37/scout/K01-command-inventory.md` and `reports/round-37/calib/Ca06-ledger-draft.md` were absent and leaves exact-once coverage owed; Ca16 independently reports the same missing inputs and that parsing, row-count, and digest checks were not performed. Consequently I cannot enumerate r37 mismatch rows, verify their causes, or certify that none were smoothed. This is an explicit blocker, not an empty mismatch set. The assigned test requires every command to be covered and Ca13's mission is mismatch disposition auditing (claims.json:13-18; targets.json:24-34).

No round validation runner was executed.

## Disposition controls from the prior filed recount

These are precedent controls only, not r37 recount results:

- The round-36 ledger distinguishes `match`, `dispositioned-mismatch` with named cause/class, and `could-not-reproduce` with owner/reason (reports/round-36/calib/Ca03-ledger-draft.md:79-81). Its RC-34-3 runner row is mixed by leg: D/O/cross match, while C failed because the reconstruction retained the round-34 SCORECARD edit, which triggered the runner's C3 check; it is explicitly classified `reconstruction-artifact` (reports/round-36/calib/Ca03-ledger-draft.md:95,199). Do not flatten that scoped mismatch to an overall match.
- RC-34-5's observed 30/19/11 differs from the filed 29/18/11 because the r35 runner was added after the r34 census instant; the ledger names this as an environmental mismatch and explains how the r34-time value reproduces (reports/round-36/calib/Ca03-ledger-draft.md:97,201). Preserve that cause/class if this historical row is reused; do not present it as a filed-value defect or erase the live-tree difference.
- The round-36 validation receipt records two mismatches in its calibration leg and says they were dispositioned, not smoothed (reports/round-36/validation.json:37-45,159-160).

## Audit required when inputs land

1. Compare each filed and observed value row-by-row. Any difference must remain a named mismatch with a causal explanation and class; a command with mixed leg outcomes must retain its per-leg dispositions.
2. A `could-not-reproduce` row must name an owner and reason; it is not a match. Unknown causes remain `to-verify` rather than being inferred.
3. Reconcile the complete ledger against K01's command inventory and any independent Ca07/Ca08 verifier disagreements before issuing a verdict. The threshold is 100% command coverage with two independent samples of at least 25% (claims.json:16-18).

## Owed

- `reports/round-37/scout/K01-command-inventory.md` — command universe and filed results.
- `reports/round-37/calib/Ca01-r33.md`, `Ca02-r34.md`, `Ca03-r35.md`, `Ca04-r36.md`, `Ca05-cross-cutting.md` — recount evidence needed to identify every observed/filed difference.
- `reports/round-37/calib/Ca06-ledger-draft.md` — assembled row-level dispositions to audit.
- `reports/round-37/calib/Ca07-verify.md` and `Ca08-verify.md` — independent sample outcomes and disagreements.
- Re-run this disposition audit after those artifacts land; until then calibration mismatch-disposition coverage is to-verify.

## Citations

- `reports/round-37/claims.json:13-18` — recount requirement, coverage threshold, independent verifier sample threshold.
- `reports/round-37/targets.json:19-34` — Ca01-Ca16 assignments, including Ca06 ledger, Ca07/Ca08 verification, and this seat's mission/output.
- `reports/round-37/calib/Ca09-coverage.md:3-11` — missing K01/Ca06 inputs and un-evaluated exact-once check.
- `reports/round-37/calib/Ca16-final-verify.md:3-17` — missing K01/Ca06 inputs; parse/count/digest checks left to-verify.
- Command/tool output: `Glob reports/round-37/calib/*.md` listed only `Ca09-coverage.md` and `Ca16-final-verify.md` at inspection.
- `reports/round-36/calib/Ca03-ledger-draft.md:79-81,95,97,199,201` — prior disposition vocabulary and named mismatch examples.
- `reports/round-36/validation.json:37-45,159-160` — prior Ca mismatch count and explicit disposition-not-smoothed note.
