# Round-19 battery integration — implementation record (R29-O01..O06)

- **Seat:** R29-O01..O06 (battery integration). **Date:** 2026-10-18.
- **Single file changed:** `tools/check-gate-battery.py`.
- **Before (declared baseline `e5718945a1ab0a0c3db955338d2cae77d68fd348`):**
  `sha256 7aa898d627fe361517d2942a0fe2b337f15d8cdc1fcb4061b394eee60f03d574`
  (`git show e571894:tools/check-gate-battery.py | sha256sum`, 2026-10-18T11:40Z).
- **After (working tree, uncommitted round-19 worker output):**
  `sha256 cd8c0ec291b6b986744ff132991abff717cbc085a86f095378189e15d6df13e5`
  (`sha256sum tools/check-gate-battery.py`, 2026-10-18T12:37Z). `git diff --stat` →
  `1 file changed, 231 insertions(+), 33 deletions(-)`.
- **Intermediate revision, withdrawn:** `sha256 83d9e3e5…` (the 9-leg variant, 11:38–12:35Z). See
  `design.md` §3 for why it was withdrawn; nothing of it survives except the widened preservation
  snapshot's gate-script coverage.
- **No gate script, fixture, baseline, or filed round-8..18 byte is touched by this seat.** The tool
  is not a gate surface: `reports/round-19/run-validation.py` §O4 hashes only
  `tools/gates/{LEGACY_GATES,D4_GATES}`, so this change needs no before/after gate ledger entry.

## 1. Constants (the registration change)

| Constant | Before | After |
|---|---|---|
| `GATE_NAMES` | 7 structural names | unchanged — the mirror selftest duty |
| `D4_GATE_NAMES` | absent | `d4-typed-labels-check-gate.py`, `d4-assembly-check-gate.py` |
| `REGISTERED_GATE_NAMES` | absent | `GATE_NAMES + D4_GATE_NAMES` (9) — the coverage duty's gate set |

## 2. Coverage duty: the registered set, and two new summary fields

- `inspect_baselines` now defaults `gate_names=REGISTERED_GATE_NAMES`, and `run_battery` passes it
  explicitly, so both duty sites name the same nine in one place each.
- `baselines.summary` gains `gates_registered` (the denominator) and `coverage`
  (`len(covered in registration order)/len(gate_names)`, e.g. `"9/9"`), beside the existing
  `gates_covered` / `gates_uncovered`. `covered_order` replaces the inline list comprehension so the
  two new fields and the list cannot drift apart.
- The `BASELINE-GATE-UNKNOWN` detail string lost the word "seven" ("is not one of the registered
  gates") because the constant it reports on is no longer seven. Finding id, state mapping and
  reading vocabulary are unchanged.

Effect on the default run: `coverage 9/9`, `gates_registered 9`, `gates_uncovered []`,
`baseline_exit 0` — where the pre-state read `7/7` with no denominator field at all.

## 3. Leg dispatch and the preservation snapshot

`leg_plan(mirror)` (new) returns the `(name, argv, cwd)` triples for the seven structural selftest
legs — the plan as data, so the selftest can assert its membership and rooting
(`CTRL-D4-SURFACE`) instead of a reader having to trace the loop. `run_battery` iterates it:

```python
for name, argv, cwd in leg_plan(mirror):
    results.append(run_child(name, argv, timeout=timeout, cwd=cwd))
```

`preservation_paths()` (new) keys every live path the battery reads: the seven structural scripts and
the fixture tree (relative to `tools/gates/`) plus the two D4 adapter scripts, which duty 2 hashes
against their baselines' `gate_sha256` pins. `preservation_snapshot()` (new) hashes each, recording
`unreadable: <err>` instead of raising if a path vanishes between listing and hashing — a vanished
path then reads as a modification, which is the finding a live-tree edit deserves. `run_battery` uses
it for both the `before` and the `after` snapshot; `diff_snapshots` and the `GATE-BYTES-CHANGED`
finding are unchanged.

Measured effect (2026-10-18T12:37Z): `files_hashed_before 30`, `files_hashed_after 30`,
`modified 0 added 0 deleted 0`, `preserved true`. The pre-change run reported 28
(`.scratch/bat.json`, 08:33 local); the 9-leg variant reported 32 and is recorded in `design.md` §3.

The mirror copy comparison (`hash_snapshot(battery_paths(mirror), mirror)`) deliberately still covers
only the seven scripts + fixtures: the mirror is not asked to hold what it cannot hold, and the copy
check keeps its old meaning.

## 4. Selftest additions (6 new controls, 29 → 35)

| Control | What it proves |
|---|---|
| `CTRL-D4-PRESTATE-7-GREEN` | the pre-state seven-name set over a seven-baseline fixture reads exit 0, `coverage 7/7`, `uncovered []` — the silent pass |
| `CTRL-D4-POSTSTATE-UNCOVERED` | the registered nine over the same fixture reads exit 2, `uncovered == D4_GATE_NAMES` exactly, `coverage 7/9` |
| `CTRL-D4-DEFAULT-9-OF-9` | the default registered set (no `gate_names` argument) over a nine-baseline fixture reads exit 0, `coverage 9/9`, every registered gate covered |
| `CTRL-D4-PRESTATE-REJECTS-D4` | the pre-state set over the nine-baseline fixture reads the D4 rows as `no baseline` / `BASELINE-GATE-UNKNOWN` — the pre-state cannot name them |
| `CTRL-D4-REGISTRY` | the registered set is nine distinct names, contains both D4 names, shares none with `GATE_NAMES`, and both D4 scripts exist under `tools/gates/` |
| `CTRL-D4-SURFACE` | the leg plan is exactly the seven structural names, every leg mirror-rooted; the mirror path set excludes both D4 names; the registered set is exactly `GATE_NAMES ∪ D4_GATE_NAMES`; the preservation snapshot covers all nine scripts |

All six are synthetic and isolated: the two nine-gate fixtures are built under the selftest's own
`TemporaryDirectory`, one synthetic script per registered gate name, so no live gate is executed by
the selftest and no live tree is read by the coverage controls. `CTRL-D4-REGISTRY` and
`CTRL-D4-SURFACE` do stat the live `tools/gates/` paths (existence only) — deliberate: a registration
that names a script which is not there must be red.

## 5. What was NOT changed

- No gate script, no fixture, no baseline, no `expected.json`, no frozen manifest. In particular the
  D4 adapters keep their graded behavior: `d4-assembly-check-gate.py` still has no `--selftest` mode,
  and the battery neither invents a leg for it nor substitutes another gate's check — the leg is
  simply not in the battery's surface, and the round's claim-O definition (runner, 12:33Z) places the
  nine-gate coverage in the baseline duty.
- The conservative exit-1 classifier, the stable-id rule, the mirror-copy check, the baseline reading
  order and the `combined_exit` mapping (`2 > 1 > 0`) are untouched.
- The seven structural legs run exactly as before: same mirror, same argv shape, same cwd, same
  capture and classification.
