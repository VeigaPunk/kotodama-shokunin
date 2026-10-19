- Seat: Ca09 | verifier | Ca | date 2026-10-19 | baseline 57c8409

Calibration coverage check: **could-not-evaluate**. The required comparison is every command in K01's inventory occurring exactly once in Ca06's recount ledger. At inspection, neither input artifact was present: `reports/round-37` contained only `claims.json`, `targets.json`, and `telemetry/`; `reports/round-37/scout` and `reports/round-37/calib` did not exist. Therefore the inventory size, ledger size, omissions, and duplicates are unknown; no zero-count or coverage pass is inferred. The assigned coverage rule and input artifact paths are in `reports/round-37/targets.json:24-27`.

## Owed
- `reports/round-37/scout/K01-command-inventory.md` (K01) and `reports/round-37/calib/Ca06-ledger-draft.md` (Ca06): produce/land the inputs; Ca09 must then rerun exact-once coverage and name any gaps. Assignments are `reports/round-37/targets.json:11,24,27`.

## Citations
- `reports/round-37/targets.json:24-27` — Ca06 ledger schema and Ca09's coverage mission.
- Command output: `ls -la reports/round-37` listed only `claims.json`, `targets.json`, and `telemetry/`.
- Command output: `ls -la reports/round-37/scout reports/round-37/calib` reported both paths `No such file or directory` (exit 2).
