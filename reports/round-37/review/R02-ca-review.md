- Seat: R02 | reviewer | Ca | date 2026-10-19 | baseline 57c8409

# Second calibration review

Axis under review: calibration. **Disposition: could-not-review the r37 recount block; this is not a pass.** At this inspection the assigned K01 inventory, Ca01–Ca08 recount/ledger/verifier artifacts, and R01 review were absent. The round-37 directory had Ca09, Ca10, Ca15, and Ca16, but without K01's inventory and Ca06's ledger the coverage, observed command results, and R01 findings cannot be checked. I did not run any round-validation runner.

## Adversarial checks and risks

- **Denominator needs an explicit convention.** The r36 recount ledger distinguishes a `table_rows` count of 21 from 17 distinct-command entries; its alternative `claims.json` convention is 20 entries / 15 distinct commands (`reports/round-36/calib/recount-ledger.json:11-49`). Its `rows` array has 17 elements (`reports/round-36/calib/recount-ledger.json:65-209`). R36's validator only checks that array length is at least 15, that rows have dispositions, and counts disposition strings containing `mismatch`; it does not establish source-command coverage (`reports/round-36/run-validation.py:123-134`). For r37, define whether a row means each command occurrence filed per claim or each distinct shell command, then reconcile to K01 exactly once; do not inherit 17 as the complete r33–r36 denominator.
- **Keep round-36 claim status separate from round status.** The r36 receipt reports Ca passed with 17 rows and two named mismatches, while global `acceptance_checks_passed` is false because D failed; the receipt explicitly says the round is rejected on D (`reports/round-36/validation.json:2,31-47,49-79,144-167`). R37 must recount the Ca evidence, preserve both mismatches, and not turn this into a whole-round acceptance or repair the rejected D evidence (`SCORECARD.md:651-664`).
- **Runner identity requires a deliberate check.** R36 `validation.json` has `runner_sha256: null` but also a per-input digest for `reports/round-36/run-validation.py` (`reports/round-36/validation.json:149-167`). When replaying in an isolated archive, compare the archived runner to that per-input digest; do not infer the runner is unpinned from the null alone, or silently omit the identity check.

The declared threshold remains 100% command coverage plus two independent verifier samples each covering at least 25% (`reports/round-37/claims.json:13-18`). Those conditions are unverified until the missing inventory, ledger, samples, and first review land.

## Owed

- `reports/round-37/scout/K01-command-inventory.md` and `reports/round-37/calib/Ca01-r33.md` through `Ca08-verify.md` (including `Ca06-ledger-draft.md`): needed for command-by-command review and verifier-sample assessment.
- `reports/round-37/review/R01-ca-review.md`: needed to review and resolve the first review's findings.
- After those land, rerun the review against the source inventory and ledger; keep any unreproducible result `could-not-reproduce` with an owner, as required by `reports/round-37/claims.json:14-18`.

## Citations

- `reports/round-37/targets.json:11,19-27,62-63` — K01, Ca01–Ca09 and R01/R02 assignments.
- `reports/round-37/claims.json:13-18` — calibration coverage and independent-sample thresholds.
- `reports/round-36/calib/recount-ledger.json:11-49,65-209` — competing census conventions and distinct-command rows.
- `reports/round-36/run-validation.py:123-134` — r36 validator's row-count/disposition checks.
- `reports/round-36/validation.json:2,31-47,49-79,144-167`; `SCORECARD.md:651-664` — r36 Ca result versus rejected round status and runner digest fields.
- Command output: `ls -la reports/round-37/calib reports/round-37/scout reports/round-37/review; ...` showed Ca09/Ca10/Ca15/Ca16 in `calib`, while `scout/` and `review/` did not exist. The subsequent required-input existence check listed K01, Ca01–Ca08, Ca06, and R01 as `ABSENT`.
