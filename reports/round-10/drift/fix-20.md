# R10-F20 — stale fix: round-8 runner's isolated replay assumed HEAD still carried the pins

- seat: freshness stale-fixer (R10-F16..F19). This file is the seat's write; the
  one in-place code repair it records is in `reports/round-8/run-validation.py`
  (a runner, not filed report prose).
- date: 2026-10-17 · lane: `kotodama-shokunin` · baseline `9dc18ec1…`
- live HEAD at work: `e3a1ec9` (+ worktree edits)

## Item taken from the ledger

| ledger row (0-based) | locator | shard | verdict in ledger |
|---|---|---|---|
| 115 | `SCORECARD.md:104` → `python3 reports/round-8/run-validation.py` | R10-F15-battery | `stale-documented` ("claim D FAIL — D2 frozen replay 7/7 could_not_evaluate … identical failure at a7bb205") |

shard-14 §3.4/§3.5 and shard-09 §DR-09-01 name the same root cause from the
tool side (round-8 gate repairs drifted the round-3 pins).

## Evidence

- Live-tree re-run today: `claim F: PASS / claim O: PASS / claim D: FAIL` with
  `{"rows": 7, "reproduced": 0, "mismatch": 0, "could_not_evaluate": 7, "exit": 2}`
  (measured in a clean mirror, exit 1 overall).
- The filed receipt was **current at its own commit**:
  `reports/round-8/validation.json` `runner_sha256`
  `7eaa36789b4d71ce94ffadc93d2f5e10d6e0ca353df1c233d0ba94f29bff8369` equals
  `git show HEAD:reports/round-8/run-validation.py | sha256sum`, and its
  `acceptance_checks_passed` is `true` (mtime 17:40:23 — before the round-8
  admission commit `e1694ba` at 17:44:17 that revised the gate bytes).
- Root cause in code: `replay_isolated()` restored each gate with
  `git show HEAD:tools/gates/<gate>.py` — i.e. it assumed HEAD still held the
  pinned revisions. After `e1694ba` committed the repaired gates, HEAD no longer
  matches the round-3 pins, so the replay refuses every row
  (`gate_digest_mismatch`) by design.

## Fix applied (in place, `reports/round-8/run-validation.py`)

1. New helper `gate_blob_for_pin(relative, pins)` — walks
   `git log --format=%H -- <path>` and returns the bytes plus revision of the
   first committed blob whose sha256 equals a manifest pin.
2. `replay_isolated()` now parses the manifest's `gate_sha256` column into a
   `pins` map, restores each gate from the matching revision, and falls back to
   HEAD (then the live file) only when no revision matches. New receipt fields:
   `gates_restored_from_history`, `gates_restored_from_pin`, `gate_revisions`.
3. Docstring corrected: it now states that the pinned revisions are resolved by
   digest, and why (the HEAD assumption read 0 of 7 rows after `e1694ba`).

Runner sha256: `7eaa36789b4d71ce94ffadc93d2f5e10d6e0ca353df1c233d0ba94f29bff8369`
(before) → `d78da29fdacc75d425e21c21fa2d299deff487f17724e8fa7bd73f5b4fc14735`
(after).

## Control (re-runnable)

In a clean mirror at HEAD with only the patched runner copied in
(`git show HEAD:<path> > <path>` restored every other dirty receipt first):

```
python3 reports/round-8/run-validation.py
→ exit 0
  claim F: PASS
  claim O: PASS
  claim D: PASS
  acceptance_checks_passed: True
```

The regenerated receipt records
`claims.D.measurement.replay_frozen.accepted = "isolated-pinned-revisions"`,
`isolated.exit = 0`, `gates_restored_from_pin = 6`,
`gates_restored_from_history = 7`, and `gate_revisions` naming
`291c714144f239db9d4efe14627b6cf07e5cffb8` for all six gates; the same receipt
still records the honest live-tree reference
`{"exit": 2, "summary": {"could_not_evaluate": 7, "reproduced": 0, "rows": 7}}`.

## Limits and side effect

- **Side effect, recorded**: the filed `reports/round-8/validation.json` still
  carries `runner_sha256 7eaa3678…`, which no longer matches the patched script.
  This seat did not regenerate the filed receipt (write scope: this fragment and
  the fix itself); the integrator/X04 should decide whether to re-file it. Until
  then the receipt is superseded by this fragment and by the mirror receipt.
- The repair changes **how** the pinned revisions are located, not what is
  checked: the replay still refuses edited gate bytes, and the live tree still
  reads exit 2 by design.
- No gate, fixture, packet, pin or corpus byte was touched; the mirror is
  disposable in-lane scratch.

## Ledger delta (for the F14 scribe / integrator)

```json
[{"id": "R10-F20-01", "command": "python3 reports/round-8/run-validation.py", "source_locator": "SCORECARD.md:104", "round10_verdict": "stale-fixed", "output_sha256": "9d0d40f1e27d9c18d60be1dfc2d963451230616ec5ee5953daae06cef59dcf5f", "exit": 1, "fix_evidence": "reports/round-10/drift/fix-20.md", "note": "replay_isolated() now resolves each manifest gate pin by digest over git history instead of assuming HEAD; control in a clean mirror: exit 0, F/O/D all PASS, accepted=isolated-pinned-revisions, gates_restored_from_pin 6 at 291c714; filed round-8 receipt now superseded (runner_sha256 7eaa3678 -> d78da29f)"}]
```
