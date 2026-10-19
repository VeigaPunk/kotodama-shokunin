- Seat: Ca07 | verifier | Ca | date 2026-10-19 | baseline 57c8409

## Independent sample

K01's command inventory contains 25 records: 16 claim-level runner records and 9 distinct nested command records (`reports/round-37/scout/K01-command-inventory.md:7-8,28-45`). I independently re-ran 8 of those 25 records (32%), sampling the eight directly executable nested records from round 33. Each observed result matched its filed result. No round runner was executed; these were nested tools only. The exact re-run commands, values and filed-result citations follow.

| K01 inventory record | Filed result | Ca07 observed | Disposition |
|---|---|---|---|
| r33 O/O1 `python3 -B -B reports/round-25/audit/c31-lessons-index-audit.py` | exit 0; findings 0 (`K01:34`; `reports/round-33/validation.json:701-727`) | exit 0; 33 lesson files / 33 index rows / 78 queue rows; formats 21/5/7; findings 0 (command output, Ca07) | match |
| r33 O/O2+O8 `python3 -B -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` | exit 0; 28/28 (`K01:35`; `reports/round-33/validation.json:729-745,952-963`) | exit 0; `SELFTEST OK: 28/28 checks passed` (command output, Ca07) | match |
| r33 A/A7 `python3 -B tools/assemble-d4-typed.py --selftest` | exit 0; 12/12 (`K01:32`; `reports/round-33/validation.json:583-598`) | exit 0; 12/12 checks passed (command output, Ca07) | match |
| r33 A/A7 `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | exit 0; 20/20 legs (`K01:33`; `reports/round-33/validation.json:600-611`) | exit 0; summary `20/20 legs passed` (command output, Ca07) | match |
| r33 O/O8 `python3 -B tools/check-gate-battery.py` | exit 0; 7 pass, 0 fail, 0 unevaluable; coverage 10/10 (`K01:37`; `reports/round-33/validation.json:903-907,925-937`) | exit 0; battery exit 0, 7 pass, 0 fail, 0 unevaluable; coverage 10/10, 20 baselines pinned (command output, Ca07) | match |
| r33 O/O8 `python3 -B tools/check-gate-battery.py --selftest` | exit 0; 44/44 (`K01:38`; `reports/round-33/validation.json:909-920,939-950`) | exit 0; `SELFTEST OK 44/44 controls behaved as expected` (command output, Ca07) | match |
| r33 O/O8 `python3 -B tools/check-craft-exercise.py --selftest` | exit 0; tamper 10/10 and CLI 18/18 (`K01:39`; `reports/round-33/validation.json:965-976,992-1003`) | exit 0; tamper 10/10 and CLI 18/18 (command output, Ca07) | match |
| r33 O/O8 `python3 -B tools/assemble-culture-d4.py --selftest` | exit 0; 81/81 (`K01:40`; `reports/round-33/validation.json:977-990,1004-1016`) | exit 0; `selftest: 81/81 checks passed` (command output, Ca07) | match |

No disagreement on the eight sampled records. This is a threshold sample, not a re-run of all 25 records or a round-runner sample. The two C31 commands were run with the inventory's exact `-B -B` argv. `TMPDIR=$PWD/.scratch` and `PYTHONDONTWRITEBYTECODE=1` were set for every Python invocation.

## Supplementary checks (not counted toward 8/25)

- Current r34 adoption inventory reports 31 runner files and classes 20 guarded-refresh / 11 unguarded-in-place (`receipt_guard_adoption.py --selftest` / `--json`, plus `ls reports/round-*/run-validation.py | wc -l`; command outputs, Ca07). The r34 filed receipt is 29 / 18 / 11 (`reports/round-34/validation.json:53-65`); the prior r36 recount records 30 / 19 / 11 at its observation point and attributes the change from r34 to later runner growth (`reports/round-36/calib/recount-ledger.json:138-143`). Current values are later-tree readings, not a new finding against r34's filed-time result.
- The r35 inventory and sweep now report 212 files/rows and the updated README digest `c3b872c4…`, versus r35's filed 211 (`reports/round-35/validation.json:46-61`). This matches r36's declared corpus move to 212 total / 25 culture-material (`reports/round-36/claims.json:22-27`); treat it as later-tree growth, not a mismatch in the 8-record sample.
- Filed receipt integrity after these checks: r33 `93b28f36…`, r34 `ba2fa4dc…`, r35 `328e97b3…`, r36 `0744b095…`, each equals the recorded SHA-256 captured after sampling (command output, Ca07). No `reports/round-*/run-validation.py` was executed in-tree or from an archive.

## Owed

- `reports/round-37/calib/Ca01-r33.md`, `Ca02-r34.md`, `Ca03-r35.md`, `Ca04-r36.md`, and `Ca05-cross-cutting.md`: these recount fragments were absent at the final inspection, so I could compare my sample with the source receipts and K01 inventory but not reconcile it against their separately filed observed rows.
- `reports/round-37/calib/Ca06-ledger-draft.md`: present but explicitly `could-not-assemble` because Ca01-Ca05 were absent (`:5-15`). Reconcile the 8 sampled rows against a populated ledger when those inputs land; record any discrepancy there. The K01 inventory denominator is present and the 8/25 threshold is met.

## Citations

- `reports/round-37/targets.json:25` — Ca07 mission and output path.
- `reports/round-37/claims.json:13-18` — Ca coverage and independent-sample threshold.
- `reports/round-37/scout/K01-command-inventory.md:7-8,28-47` — denominator, sampled command records, filed results and the explicit rule not to infer a runner's exit code from `passed`.
- `reports/round-33/validation.json:583-611,701-745,903-1016` — nested command receipts used for the sampled filed results.
- `reports/round-34/validation.json:53-65`; `reports/round-35/validation.json:46-61`; `reports/round-36/claims.json:22-27`; `reports/round-36/calib/recount-ledger.json:138-143` — supplementary time-shift cross-checks.
- Command outputs: the eight commands in the sample table and the supplementary commands recorded above, run by Ca07 on 2026-10-19 at baseline `57c8409`, with the stated TMPDIR and bytecode environment.
