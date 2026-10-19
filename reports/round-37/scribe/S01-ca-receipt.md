- Seat: S01 | scribe | Ca | date 2026-10-19 | baseline 57c8409

# Calibration receipt — post-review

## Outcome

**Could not evaluate; no pass is claimed.** The required recount ledger and independent-review evidence were unavailable in the round-37 artifact set at this inspection. Thus command coverage, filed-versus-observed dispositions, mismatch causes, and the two-verifier sampling threshold remain unverified. The required threshold is 100% of inventoried commands plus two independent verifiers sampling at least 25% (claims.json:13-18); no row counts or completion rates are inferred.

## Work performed

Checked the Ca claim and seat assignments, inspected the available round-37 fragments, and recorded the missing dependencies. The current `ls -R reports/round-37` output lists `calib/Ca09-coverage.md` and `calib/Ca16-final-verify.md`, but no K01 inventory, Ca06 ledger, recount fragments, or R01/R02 review fragments. Ca09 and Ca16 themselves report that the comparison/strict-parse checks could not be performed because the inventory and ledger inputs were absent at their inspections (reports/round-37/calib/Ca09-coverage.md:3-6; reports/round-37/calib/Ca16-final-verify.md:3-10). No round validation runner was executed; the shared rule explicitly forbids in-tree runner execution (targets.json:7).

## Claim disposition

- **Command census and recount:** could-not-evaluate. Without K01's per-command inventory and Ca01-Ca05 recounts, no filing-level command count or filed/observed results can be reproduced (targets.json:11,19-23).
- **Ledger coverage and consistency:** could-not-evaluate. Ca09 and Ca16 identify the missing K01 inventory and Ca06 ledger as blockers; exact-once coverage, strict parsing, row-count equality, and digest checks remain undone (targets.json:24-27; reports/round-37/calib/Ca09-coverage.md:3-6; reports/round-37/calib/Ca16-final-verify.md:3-10).
- **Independent sampling and mismatch audit:** could-not-evaluate. The assigned Ca07/Ca08 sample results and Ca13 mismatch audit are not present in the inspected artifact listing; no mismatch disposition or verifier agreement is asserted (targets.json:25,31).
- **Post-review fold:** incomplete. The Ca10 draft, Ca15 final fold, and R01/R02 reviews are not present in the inspected listing, so this receipt cannot attest that review comments were incorporated (targets.json:28,33,62-63).

This receipt does not establish the Ca claim's required after-state. Keep the claim unverified pending the owed artifacts and a complete post-review fold; no repaired or inherited evidence is substituted for a recount.

## Owed

- `reports/round-37/scout/K01-command-inventory.md` — K01: file the command census needed to establish the expected coverage denominator (targets.json:11).
- `reports/round-37/calib/Ca01-r33.md` through `Ca05-cross-cutting.md` — Ca01-Ca05: file observed-versus-filed recounts for their assigned scope (targets.json:19-23).
- `reports/round-37/calib/Ca06-ledger-draft.md` — Ca06: assemble one row per inventoried command; then rerun Ca09 coverage and Ca16 final consistency checks (targets.json:24,27,34).
- `reports/round-37/calib/Ca07-verify.md` and `Ca08-verify.md` — Ca07/Ca08: file independent samples meeting the >=25% requirement (targets.json:25-26; claims.json:18).
- `reports/round-37/calib/Ca10-receipt.md`, `Ca13-audit.md`, and `Ca15-final.md` — Ca10/Ca13/Ca15: supply the receipt draft, mismatch-cause audit, and post-review fold (targets.json:28,31,33).
- `reports/round-37/review/R01-ca-review.md` and `R02-ca-review.md` — R01/R02: file both assigned adversarial reviews before the final fold (targets.json:62-63).

## Citations

- `reports/round-37/claims.json:13-18` — Ca claim, after-state, counting command, and coverage/reviewer thresholds.
- `reports/round-37/targets.json:7,11,19-34,62-63` — shared runner restriction and relevant seat assignments.
- `reports/round-37/calib/Ca09-coverage.md:3-6` — coverage check could not be evaluated; inventory and ledger owed.
- `reports/round-37/calib/Ca16-final-verify.md:3-10` — strict parse, row count, and digest checks blocked; inventory and ledger owed.
- Command output: `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1 && ls -R reports/round-37` — at inspection, only Ca09 and Ca16 were present under `calib/`; no `scout/`, Ca06, recount, receipt, or review fragments were listed.
