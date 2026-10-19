- Seat: R01 | reviewer | claim Ca | date 2026-10-19 | baseline 57c8409

## Review

**Verdict: could-not-evaluate the round-37 recount results; partial adversarial review only.** Ca06 says it could not assemble a ledger because Ca01–Ca05 were absent at its check; it contains no r37 observed command results or dispositions to verify (`reports/round-37/calib/Ca06-ledger-draft.md:3-15`). K01's filed-result inventory is now present and reviewed below. No round-validation runner was executed.

### Findings and controls

1. **Keep the command unit explicit.** K01 records 16 claim-level receipt results plus 9 distinct nested command argv records (25 inventory entries total), and correctly preserves one row per round/claim even where the same runner string repeats (`reports/round-37/scout/K01-command-inventory.md:5-7,23-46`). Ca05 separately owns recurring cross-cutting commands; K01's 25 is not by itself proof that those rows are covered. Ca06 must reconcile Ca05's additions and any exact duplicates; Ca09's exact-once check against K01 alone cannot prove full Ca-claim coverage (`reports/round-37/targets.json:23-27`; `reports/round-37/claims.json:13-18`).

2. **Do not flatten round 36.** K01 correctly distinguishes C, Ca, D, and cross: D is `passed=false`, while Ca is `passed=true` with 17 measured rows and two named mismatches. The overall receipt is rejected on D, not on Ca (`reports/round-37/scout/K01-command-inventory.md:23-26`; `reports/round-36/validation.json:31-47,49-78,164-167`). Recount rows must preserve this per-claim result; neither a single runner argv nor the overall rejection substitutes for the claim-specific filed value.

3. **Guard inherited `17` and `21` counts.** The round-36 historical recount ledger distinguishes 21 table rows from 17 distinct-command entries, with separate per-round and disposition totals (`reports/round-36/calib/recount-ledger.json:11-28,51-58,65-74`). Round-36's validation also reports `rows: 17` for its Ca leg (`reports/round-36/validation.json:37-43`). These counts have different units and scopes; do not use the inherited 17 or 21 as the round-37 command denominator. Ca06 correctly labels that ledger historical-only (`reports/round-37/calib/Ca06-ledger-draft.md:7`).

4. **One inventory row needs an exact command reference.** K01's nested O7 command cell uses the placeholder `[embedded O06 controls harness; full command literal at cited line]`, not the literal argv (`reports/round-37/scout/K01-command-inventory.md:36`). The source receipt has the embedded command at `reports/round-33/validation.json:802`; Ca06's `command` field should use the exact command or an unambiguous source pointer, and the replay disposition must remain unverified until Ca05/Ca01 evidence supplies an observed result (`reports/round-37/targets.json:23-24`).

No row-level r37 observed/filed comparison was possible, so this review finds no basis to call the recount complete or to accept its dispositions. That is not a finding of zero mismatches.

## Owed

- `reports/round-37/calib/Ca01-r33.md` through `Ca05-cross-cutting.md`: provide observed recounts, including the exact O7 command reference and Ca05's cross-cutting rows.
- `reports/round-37/calib/Ca06-ledger-draft.md`: re-assemble the ledger from those inputs; preserve per-claim receipt results and distinguish table rows, distinct argv, and inventory entries.
- `reports/round-37/calib/Ca07-verify.md` and `Ca08-verify.md`: independent sample evidence and disagreements are required before a final review can be issued (`reports/round-37/claims.json:16-18`).

## Citations

- `reports/round-37/claims.json:13-18` — Ca coverage and independent-sample thresholds.
- `reports/round-37/targets.json:19-27,62-63` — Ca01–Ca06 inputs, Ca05 scope, and R01/R02 review assignments.
- `reports/round-37/scout/K01-command-inventory.md:5-7,23-46` — scope, per-claim results, 25-entry count, and O7 placeholder.
- `reports/round-37/calib/Ca06-ledger-draft.md:3-15` — blocked assembly and historical-only r36 ledger.
- `reports/round-36/calib/recount-ledger.json:11-28,51-58,65-74` — historical row-count conventions and dispositions.
- `reports/round-36/validation.json:31-47,49-78,164-167` — Ca passed, D failed, and r36 rejected status.
- `reports/round-33/validation.json:802-813` — embedded O7 command source.
- No round-37 runner command was executed; shared prohibition is `reports/round-37/targets.json:7`.
