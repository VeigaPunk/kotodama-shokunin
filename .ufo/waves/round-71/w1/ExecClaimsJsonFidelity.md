# ExecClaimsJsonFidelity — round-71 claims.json fidelity report

Seat: `L1Kotodama71.ExecClaimsJsonFidelity` (leaf executor, read-only verification wave 1)
Date: 2026-10-25
Scope: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-71/claims.json` (frozen)
Verification tooling: Python 3.14.8 (`json.loads` on raw UTF-8 bytes), GNU bash 5.3.20(1) (`bash -n`). No tools installed; nothing needed beyond system python/bash.

## Checks and results

| # | Check | Result |
|---|-------|--------|
| 1 | Parses as JSON (UTF-8, `json.loads`) | PASS — parse OK, no decode/syntax error |
| 2 | `claims` is an array of exactly 3 objects | PASS — ids `C`, `Ca`, `D` |
| 3 | Axes distinct and exactly coverage/calibration/depth | PASS — `C=coverage`, `Ca=calibration`, `D=depth` (3 distinct, set matches) |
| 4 | Each claim carries before/after/predicate/counting_command/target/kill_rule/do_nothing_control | PASS — all 7 fields present, non-empty strings on all 3 claims |
| 5 | Counting commands syntactically valid shell: `bash -n` | PASS — rc=0 for all three commands (C, Ca, D) |

### Detail — `bash -n` (syntax only, no execution)
- Claim C command: rc=0. Note: JSON-escaped `\\|` decodes to `\|` inside the single-quoted grep `-cE` pattern — quotes are balanced, no shell metacharacter leakage.
- Claim Ca command: rc=0. Includes brace expansions `{o,ca,d}`, single-quoted awk program, pipes; all balanced.
- Claim D command: rc=0. Includes `bash -c '...'` nested quote block with `$(mktemp -d)`, `git archive | tar -x -C $T`, `cd $T`, `echo EXIT=$?`; nested quoting balanced.

## Fidelity findings
- No fidelity defects found in the frozen claims file against the assigned criteria. All five checks pass.
- Sanity spot-checks (not required by brief, no defects found): `round=71`; `base_revision` present; claim Ca `surface` enumerates exactly V70-1..V70-5 plus item-10 score-consistent with its `before`/`after`/`predicate`; claim D `predicate`/`target`/`kill_rule`/`do_nothing_control` consistent on the no-git path (exit 2 vs 1).

## Tools installed
- None (no install/update performed; system python3 and bash sufficed — verified versions above).

## Risks / notes
- `bash -n` verifies syntax only, not runtime success; whether the commands' exit codes meet targets is a post-integration gate concern, outside this read-only seat.
- `wave.wave2_seats` holds the string `"TBD after wave 1"` (not a number) — intentional per wave policy, not in scope, not flagged as defect.
