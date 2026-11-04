# MutationTester — receipts, round 84 wave 1

Everything here was produced by grading *stub* claim artifacts (never the round's
real ones) with the frozen counters at `3ca2cf28` and with one-line mutants of
those counters. No byte of the lane repo was mutated to produce any of it.

| file | what it is |
|---|---|
| `matrix.json` | one row per graded stub: expected leg, verdict, failing legs, whether the counter still rejected the commit |
| `legs/<name>.txt` | the counter's full stdout for that stub (every `LEG …` line verbatim) |
| `stub-commits.json` | the fixture commit sha for each stub, in the scratch clone only |
| `counter-mutants.diff` | the three one-line counter mutations as unified diffs against the frozen blobs |
| `junk-battery.txt` | `accept-o84.py --junk` on the same lands with the unmutated and the DEMO-mutated counter, plus what the battery's `no-trace` trial actually rewrites |
| `audit-unrowed.txt` | `tools/check-gate-registry.py --root <tree>` over a lands carrying one extra unrowed tool: exit code and both summary lines |
| `integrity.txt` | sha256 of the four frozen round-84 blobs and the lane worktree status at the end of the seat |
| `build/mk.py`, `build/run.py` | the fixture drivers, portable: they take the scratch root from `SEAT_SCRATCH` (or the cwd) and expect `rep/` to be a clone of the lane at the freeze |

## Re-running

1. Clone the lane read-only into a scratch root: `git clone --shared --no-hardlinks <lane> <scratch>/rep`, set `user.email`/`user.name` **in the clone only**, `git checkout 3ca2cf28…` detached.
2. `SEAT_SCRATCH=<scratch> python3 build/mk.py` — writes the stubs as sibling commits of the freeze and `commits.json`.
3. `SEAT_SCRATCH=<scratch> python3 build/run.py` — copies the counter blobs out of the freeze, grades every stub, builds the three counter mutants in `mut/`, and re-audits the unrowed cap.

The drivers assert `git -C <scratch>/rep rev-parse --show-toplevel` equals the clone
before any git call, and they move `refs/heads/main` in the clone to the graded
lands so the counters' branch-tip guard is satisfied without touching the lane.
