# ExecCounterReplay — round-93 claim-C do-nothing control replay (2026-11-05)

Seat: ExecCounterReplay (w1, judged on operability). No frozen file edited. No tool installs (none needed). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.

## Commands and rc (all run 2026-11-05, `--work` under `/fast/scratch/hyaku/kotodama-r93/ExecCounterReplay/`)

1. `python3 -B reports/round-93/measure93.py --root <lane> --lands 8b2ce60a7bbf015f42a6c9e5c45e994e4c2f7742 --freeze 174fd5a8e05b3919a7854a4495c2fe0f28080775 --claim C --work <scratch>/run-a` → **rc 2**; stdout empty; stderr exactly `MEASURE93_ERROR: --lands equals the frozen base; a do-nothing landing cannot pass`. Expected rc 2 + MEASURE93_ERROR: **met**.
2. same, `--lands 174fd5a8e05b3919a7854a4495c2fe0f28080775 --claim C --work <scratch>/run-b` → **rc 1**; legs: `LEG PASS MATERIALIZE`, `LEG FAIL ENTRY`, `LEG PASS POSITIVE`, `LEG PASS INDEX`, `LEG PASS CENSUS`, `LEG FAIL APPENDONLY`; summary `MEASURE93-C: FAIL legs=4/6 failed=ENTRY,APPENDONLY`. Expected rc 1 with ENTRY and APPENDONLY failing and POSITIVE, INDEX (and MATERIALIZE) passing: **met**.
3. same, `--claim O --lands 8b2ce60a7bbf015f42a6c9e5c45e994e4c2f7742 --work <scratch>/run-c` → **rc 2**, stderr exactly as in run 1. Expected rc 2: **met**.
4. `python3 -c "import json;json.load(open('<lane>/reports/round-93/claims.json'))"` → **rc 0**.
5. `python3 -B <lane>/tools/check-advance-evidence.py --selftest --work <scratch>/selftest` → **rc 0**, output line `SELFTEST PASS 114/114`; count of lines starting `  ok ` = 114 (command: Python `sum(1 for l in stdout.splitlines() if l.startswith('  ok '))` over the captured output, 2026-11-05). Tool sha256 of the lane tool = `9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7`, equal to claims.json `O.tool_sha256`. Note: `/home/vgpnk/Projects/shokunin/tools/check-advance-evidence.py` does not exist; the referenced tool is the lane tool.

## refusal_cases cross-check

All **25/25** names in claims.json `O.refusal_cases` appear in the selftest output as ok lines of the form `` ``  ok  <name>: rc=1`` `` — note the tool's format is `  ok  ` (two spaces after `ok`), so a single-space pattern `  ok <name>:` finds none; with the tool's actual format every name matches exactly once (per-name substring count = 1 for all 25). **Missing list: none.**

## Receipt comparison (per seat spec: stamp lines `# stamped`/`# evaluated`/`# measured`/`# tree`/`# counter sha256`, materialized paths, and tool scratch paths in LEG lines excluded)

- (a) vs `reports/round-93/controls/C-base-refusal.txt`: receipt line 1 `# claim C, lands = frozen base 8b2ce60a: refused by design (a do-nothing landing cannot pass)` is a receipt annotation, not counter output (the counter emits only the stderr line on this path). Receipt line 2 is byte-identical to run-a stderr; run-a stdout is empty. **No difference.**
- (b) vs `reports/round-93/controls/C-freeze-rev2.txt`: after excluding the five stamp lines and the annotation header line 1, and normalizing the work paths (`/fast/scratch/hyaku/kotodama-r93/controls2/C-freeze2` in the receipt vs `/fast/scratch/hyaku/kotodama-r93/ExecCounterReplay/run-b` here) to `<WORK>`, the `# frozen legs` header, all six LEG lines and the `MEASURE93-C: FAIL legs=4/6 failed=ENTRY,APPENDONLY` summary are byte-identical (unified diff over normalized lines: only the excluded lines and the receipt file's trailing newline remain). Stamp values also coincide: tree `d51763c968c7a12583d0b1e9630a680073fcfc00`, counter self-sha `fb3ca1c20026f0f3dfeb60103396f6af166bf4bc1490d83c17e1fb34df6f84c3`, measured revision (lane main) `174fd5a8e05b3919a7854a4495c2fe0f28080775`. **No difference.**

## Committed mutation receipt header lines (`reports/round-93/mutation-score.txt`, lines 1–3)

```
# tool sha256 9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7
# clean selftest rc=0 ['SELFTEST PASS 114/114']
MUTATION-SCORE: 83/83 killed, 0 survived, 0 broken-pattern
```

## Result

Counter refusal behaviour confirmed on all three named legs; both committed C receipts replay clean under the exclusion rules; no discrepancy to report.
