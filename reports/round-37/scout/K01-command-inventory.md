- Seat: K01 | scout | Ca | date 2026-10-19 | baseline 57c8409

## Inventory

Scope: command records filed in `reports/round-33..36/validation.json`. The claim-level runner is recorded once per claim (the same runner argv is repeated across claims); nested command records are listed separately, deduplicated only where the exact argv and result repeat within round 33. Claim-level receipts file `passed` and `failures`, not a shell `exit_code`; do not infer a runner exit code from `passed`.

### Claim-level runner commands (16 records)

| Round / claim | Filed command | Filed result | Citation |
|---|---|---|---|
| 33 / A | `python3 reports/round-33/run-validation.py` | passed=true; failures=[]; round accepted | `reports/round-33/validation.json:2,6-8,622` |
| 33 / C | `python3 reports/round-33/run-validation.py` | passed=true; failures=[]; round accepted | `reports/round-33/validation.json:2,624-627,693` |
| 33 / O | `python3 reports/round-33/run-validation.py` | passed=true; failures=[]; round accepted | `reports/round-33/validation.json:2,695-698,1043` |
| 33 / cross | `python3 reports/round-33/run-validation.py` | passed=true; failures=[]; round accepted; CO6 is could-not-evaluate | `reports/round-33/validation.json:2,1045-1049,1095-1104,1176` |
| 34 / C | `python3 reports/round-34/run-validation.py` | passed=true; failures=[]; round accepted | `reports/round-34/validation.json:2,6-9,25` |
| 34 / D | `python3 reports/round-34/run-validation.py` | passed=true; failures=[]; round accepted | `reports/round-34/validation.json:27-30,45` |
| 34 / O | `python3 reports/round-34/run-validation.py` | passed=true; failures=[]; round accepted | `reports/round-34/validation.json:47-50,65` |
| 34 / cross | `python3 reports/round-34/run-validation.py` | passed=true; failures=[]; round accepted; CO6 is could-not-evaluate | `reports/round-34/validation.json:2,67-71,122-129,159` |
| 35 / A | `python3 reports/round-35/run-validation.py` | passed=true; failures=[]; round accepted | `reports/round-35/validation.json:2,6-9,21` |
| 35 / C | `python3 reports/round-35/run-validation.py` | passed=true; failures=[]; round accepted | `reports/round-35/validation.json:23-26,67` |
| 35 / O | `python3 reports/round-35/run-validation.py` | passed=true; failures=[]; round accepted | `reports/round-35/validation.json:69-72,92` |
| 35 / cross | `python3 reports/round-35/run-validation.py` | passed=true; failures=[]; round accepted; CO-godspeed is could-not-evaluate | `reports/round-35/validation.json:2,94-98,100-108,191` |
| 36 / C | `python3 reports/round-36/run-validation.py` | passed=true; failures=[] | `reports/round-36/validation.json:2,5-8,29` |
| 36 / Ca | `python3 reports/round-36/run-validation.py` | passed=true; failures=[]; Ca measurement: 17 rows, 2 named mismatches | `reports/round-36/validation.json:31-43,47` |
| 36 / D | `python3 reports/round-36/run-validation.py` | passed=false; one stale-premise failure; round rejected on D | `reports/round-36/validation.json:49-59,74,78,165` |
| 36 / cross | `python3 reports/round-36/run-validation.py` | passed=true; failures=[]; CO-godspeed is could-not-evaluate; round rejected because D failed | `reports/round-36/validation.json:80-105,136,165` |

### Additional nested command records (9 distinct argv)

| Round / claim-leg | Filed command | Filed result | Citation |
|---|---|---|---|
| 33 / A / A7 | `python3 -B tools/assemble-d4-typed.py --selftest` | exit_code=0; ok=true; selftest 12/12 | `reports/round-33/validation.json:583-598` |
| 33 / A / A7 | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | exit_code=0; ok=true; 20/20 legs passed | `reports/round-33/validation.json:600-611` |
| 33 / O / O1 | `python3 -B -B reports/round-25/audit/c31-lessons-index-audit.py` | exit_code=0; ok=true; findings=0 | `reports/round-33/validation.json:701-727` |
| 33 / O / O2 + O8 | `python3 -B -B reports/round-25/audit/c31-lessons-index-audit.py --selftest` | exit_code=0; ok=true; selftest 28/28; same argv/result also appears in O8 | `reports/round-33/validation.json:729-745,952-963` |
| 33 / O / O7 | `python3 -B -c '[embedded O06 controls harness; full command literal at cited line]'` | exit_code=0; ok=true; controls 11/11 | `reports/round-33/validation.json:802-813` |
| 33 / O / O8 | `python3 -B tools/check-gate-battery.py` | exit_code=0; ok=true; 7 pass, 0 fail, 0 unevaluable; coverage 10/10 | `reports/round-33/validation.json:903-907,925-937` |
| 33 / O / O8 | `python3 -B tools/check-gate-battery.py --selftest` | exit_code=0; ok=true; selftest 44/44; same argv/result also appears in O8 battery_selftest | `reports/round-33/validation.json:909-920,939-950` |
| 33 / O / O8 | `python3 -B tools/check-craft-exercise.py --selftest` | exit_code=0; ok=true; tamper 10/10 and CLI 18/18; same argv/result also appears in O8 | `reports/round-33/validation.json:965-976,992-1003` |
| 33 / O / O8 | `python3 -B tools/assemble-culture-d4.py --selftest` | exit_code=0; ok=true; selftest 81/81; same argv/result also appears in O8 | `reports/round-33/validation.json:977-990,1004-1016` |

## Reconciliation notes

- Claim-level runner argv is repeated for each claim; the top-level `counting_command` (where present) names the same runner: round 34 `validation.json:167`, round 35 `:199`, round 36 `:144` (round 33 runner and receipt header at `:1184,1282-1284`). These are not extra distinct invocations.
- Inventory count: 16 claim-level records + 9 distinct nested argv records = 25. The nested O8 selftests repeated under both `battery_selftest` / `commands` and top-level O8 fields are consolidated by exact argv, with every filed occurrence cited.
- Rounds 33–35 have `acceptance_checks_passed=true`; round 36 has `false` and is expressly `REJECTED on D`. The nested cross-claim `could-not-evaluate` legs did not change their claims' filed `passed=true` result. Round 34 also lists missing dependencies at `reports/round-34/validation.json:190-193`; round 36's runner has `runner_sha256=null` at `:166-168`.
- I read the receipts only; no `reports/round-*/run-validation.py` was executed in-tree.

## Owed

None for the assigned inventory. This is a filed-result inventory, not a replay/recount of the acceptance commands.

## Citations

- `reports/round-33/validation.json:2-1285`
- `reports/round-34/validation.json:2-201`
- `reports/round-35/validation.json:2-224`
- `reports/round-36/validation.json:2-169`
- `reports/round-37/claims.json:12-18` (Ca mission and coverage threshold)
- `reports/round-37/targets.json:3-11` (shared rules and K01 assignment)
- `REGIMEN.md:25-43,60-69` (round contract, scope, and stop rules)
