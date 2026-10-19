- Seat: Ca14 | executor | Ca | date 2026-10-19 | baseline 57c8409

# Ca14 — r33 nested-command gap fill

Supplemental recount of seven nested r33 command records in K01's inventory. This is not a complete r33 recount: Ca01 owns all r33 command/result rows, including the claim-scoped runner commands and the two C31 audit commands. No `reports/round-*/run-validation.py` was run.

| K01 source | Command | Filed result | Observed result | Disposition |
|---|---|---|---|---|
| 33 / A / A7 | `python3 -B tools/assemble-d4-typed.py --selftest` | exit 0; 12/12 | exit 0; `selftest: 12/12 checks passed` | match |
| 33 / A / A7 | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | exit 0; 20/20 legs | exit 0; `summary: 20/20 legs passed` | match; the emitted D2L hold findings are part of the expected hold set |
| 33 / O / O7 | Embedded `python3 -B -c` O06 controls command | exit 0; controls 11/11 | exit 0; `CONTROLS OK: 11/11 controls behaved as specified`. Extracted the filed source from the receipt and ran it with the same Python arguments in a disposable local clone under `.scratch`, using `O06_REPO` to keep its scratch mutations in the clone. | match |
| 33 / O / O8 | `python3 -B tools/check-gate-battery.py` | exit 0; 7 pass, 0 fail, 0 unevaluable; coverage 10/10 | exit 0; battery_exit 0, pass 7, fail 0, unevaluable 0; baselines 20, coverage 10/10, pinned 20; findings empty | match |
| 33 / O / O8 | `python3 -B tools/check-gate-battery.py --selftest` | exit 0; 44/44 | exit 0; `SELFTEST OK 44/44 controls behaved as expected` | match |
| 33 / O / O8 | `python3 -B tools/check-craft-exercise.py --selftest` | exit 0; tamper 10/10 and CLI 18/18 | exit 0; `SELFTEST OK 10/10 tamper cases detected`; `CLI-SELFTEST OK 18/18 cases passed` | match |
| 33 / O / O8 | `python3 -B tools/assemble-culture-d4.py --selftest` | exit 0; 81/81 | exit 0; `selftest: 81/81 checks passed` | match |

All observed outputs above are from read-only command executions dated 2026-10-19; the battery and selftests used the prescribed `.scratch` TMPDIR. The O06 harness was executed from a local clone and removed after completion; its output reported 11/11 controls passing.

## Owed

- `reports/round-37/calib/Ca01-r33.md` — Ca01's complete r33 recount remains required, including claim-scoped runner rows and K01's C31 audit/selftest rows; this supplement does not claim those rows.

## Citations

- `reports/round-37/targets.json:19-34` — Ca01's r33 assignment and Ca14's spare gap-fill output assignment.
- `reports/round-37/plan/P01-ca-plan.md:7-17` — per-round row ownership; spare seats fill only uncovered rows.
- `reports/round-37/scout/K01-command-inventory.md:28-40` — nested command inventory, filed results, and source pointers.
- `reports/round-33/validation.json:583-620` — filed typed-adapter selftest and typed-pipeline results.
- `reports/round-33/validation.json:802-813` — filed embedded O06 control command and result.
- `reports/round-33/validation.json:903-920,925-950,965-990,992-1016` — filed gate-battery, craft, and D4 selftest results (including repeated command occurrences).
- Command outputs (this seat, 2026-10-19): the six listed tool invocations returned the stated exit codes and summaries; the extracted O06 script returned exit 0 and `CONTROLS OK: 11/11` in an isolated local clone.
