- Seat: Ca12 | executor | Ca | date 2026-10-19 | baseline 57c8409

# Ca12 — round-33 nested command gap-fill

K01's inventory identifies nine distinct nested commands in the round-33 validation receipt (`reports/round-37/scout/K01-command-inventory.md:28-40`). I independently reran six of those commands as a partial gap-fill; these rows are supplemental evidence for Ca06, not additional inventory occurrences. Ca06 should include each K01 inventory row exactly once and deduplicate any matching Ca01 results.

| Round / claim-leg | Command | Filed result | Observed result (2026-10-19) | Disposition | Owner |
|---|---|---|---|---|---|
| 33 / A / A7 | `python3 -B tools/assemble-d4-typed.py --selftest` | exit 0; `selftest: 12/12 checks passed` (`reports/round-33/validation.json:583-598`) | exit 0; `selftest: 12/12 checks passed` (command output, this seat) | match | Ca12 |
| 33 / A / A7 | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | exit 0; summary `20/20 legs passed` (`reports/round-33/validation.json:600-611`) | exit 0; summary `20/20 legs passed` (command output, this seat) | match | Ca12 |
| 33 / O / O8 | `python3 -B tools/check-gate-battery.py` | exit 0; `pass: 7`, `fail: 0`, `unevaluable: 0`, coverage `10/10` (`reports/round-33/validation.json:925-937`) | exit 0; JSON summary `battery_exit: 0`, `pass: 7`, `fail: 0`, `unevaluable: 0`, coverage `10/10` (command output, this seat) | match | Ca12 |
| 33 / O / O8 | `python3 -B tools/check-gate-battery.py --selftest` | exit 0; `SELFTEST OK 44/44 controls behaved as expected` (`reports/round-33/validation.json:909-920,939-950`) | exit 0; `SELFTEST OK 44/44 controls behaved as expected` (command output, this seat) | match | Ca12 |
| 33 / O / O8 | `python3 -B tools/check-craft-exercise.py --selftest` | exit 0; tamper `10/10` and CLI `18/18` (`reports/round-33/validation.json:965-976,992-1003`) | exit 0; `SELFTEST OK 10/10 tamper cases detected`; `CLI-SELFTEST OK 18/18 cases passed` (command output, this seat) | match | Ca12 |
| 33 / O / O8 | `python3 -B tools/assemble-culture-d4.py --selftest` | exit 0; `selftest: 81/81 checks passed` (`reports/round-33/validation.json:977-990,1004-1016`) | exit 0; `selftest: 81/81 checks passed` (command output, this seat) | match | Ca12 |

The six commands above were run directly; none was a `reports/round-*/run-validation.py` runner. For each Python invocation, the environment was set first with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

## Owed

- `reports/round-37/calib/Ca01-r33.md` — assigned to Ca01: the remaining K01 round-33 command rows, including the c31 audit/selftest and embedded O06 controls command (`reports/round-37/scout/K01-command-inventory.md:34-36`). This supplement does not claim those rows were independently rerun.
- `reports/round-37/calib/Ca06-ledger-draft.md` — integrate these six results only once against K01's inventory; Ca01 may file overlapping evidence.

## Citations

- `reports/round-37/targets.json:30-34` — Ca12's spare gap-fill assignment and output path.
- `reports/round-37/scout/K01-command-inventory.md:28-40,45` — nested command records and deduplication convention.
- `reports/round-33/validation.json:583-611,909-920,925-990,992-1016` — filed command results and source locations.
- Command outputs, this seat, 2026-10-19 — the six observed results recorded in the table; commands were run with the required temporary-directory and no-bytecode environment.
