# CritRegistrySweep — round 71 wave 1

Seat: `L1Kotodama71.CritRegistrySweep` (critic, leaf; no subagents).
Assignment: sweep `corpus/SOURCES.md` for rows a do-nothing control would count
(missing/blank used-by on mined rows; duplicate ids; malformed 11-column rows;
missing used-by paths), running the frozen census commands from `CORPUS.md`
§SOURCES.md. Read-only. Measured at lane HEAD `b694afd6c91c6d86fa98cbb66dd22c02998678b3`
(working tree), 2026-10-25. No tools installed.

## Frozen census commands (CORPUS.md §SOURCES.md `## Census`, run from lane root)

| # | command | stdout | exit |
|---|---|---|---|
| 1 | `grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|' corpus/SOURCES.md` | `784` | 0 |
| 2 | `awk -F'|' '/^\|[[:space:]]*S[0-9][0-9][0-9]+[[:space:]]*\|/ && NF!=13 {n++} END{print n+0}' corpus/SOURCES.md` | `0` | 0 |
| 3 | tier histogram | `A=474 B=298 C=12 ` | 0 |
| 4 | status histogram | `mined=689 queued=58 rejected=37 ` | 0 |
| 5 | duplicate ids (`… | sort | uniq -d`) | *(empty)* | 0 |
| 6 | enum violations + tier-inflation | *(empty)* | 0 |
| 7 | mined rows' used-by paths missing (`… | while read -r p; do [ -e "$p" ] || echo "missing: $p"; done`) | *(empty)* | 0 |

## Sweep results (the four control-counted categories)

1. **Missing/blank used-by on mined rows — must print nothing.** PASS.
   All 689 `mined` rows carry ≥1 non-empty used-by path (token count distribution:
   682×1, 4×2, 1×3, 1×9, 1×11 tokens; zero rows with empty or `—` used-by).
2. **Duplicate ids — must print nothing.** PASS. Command 5 prints nothing; no id
   repeats in the 784-row registry.
3. **Malformed 11-column rows — must be 0.** PASS. Command 2 prints `0`.
4. **Mined rows whose used-by path does not exist — must print nothing.** PASS.
   Command 7 prints nothing: every used-by path exists relative to the lane root.

A do-nothing control run at this measurement would print nothing / zero for all
four invariants. No counterexample found; no rows would be counted by the control.
The registry invariant surface claim C relies on (`every row's used-by path exists`)
holds at measurement.

## Note: round-49 runner (for completeness)

`python3 reports/round-49/run-validation.py` (the runner SOURCES.md points at for the
seven commands) exits **1** with `acceptance_checks_passed: False`,
`verdict: rejected-honest-stop`. Its seven `CENSUS` legs are the verbatim commands
above and are all clean; the non-zero exit comes from round-49-era extra checks that
no longer hold at this measurement: uniform `opened` == 2026-10-19 (histogram:
2026-10-19 ×47, -21 ×23, -22 ×395, -23 ×210, -24 ×108, -25 ×1), round-49 lesson
Gate covering every current registry id (784 vs round 49's rows), and corpus totals
vs the round-49 targets. This is expected drift, not a registry invariant defect.
The runner writes `reports/round-49/validation.json` as a side effect; since this
seat is read-only, the file was restored from HEAD immediately after the run
(`git restore --source=HEAD --worktree reports/round-49/validation.json`; verified
clean, exit 0).

Evidence: exact command outputs captured above from fresh runs of the frozen commands
on the current registry; no mutations performed.
