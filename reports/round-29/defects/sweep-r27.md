# Round-27 conformance defect sweep — R29-O05..O06

- **Audit date:** 2026-10-18.
- **Scope:** round-27 sweep inventory coverage and the frozen/v3 rows measured during the register-law landing.
- **Mode:** read-only review of `reports/round-27/audit/o39-o40-sweep-adversarial.md`, the sweep receipt, and the later validation receipt. No round validator was run for this sweep; all measurements below are archived, dated snapshots.
- **Round state:** the snapshots moved materially during the round. This sweep preserves the audit readings and the later receipt separately; it does not label the earlier red as the final round verdict.

## Findings

### O05 — The round-27 inventory tools did not cover the full D4 pin surface (tool-scope defect)

The audit's recorded **2026-10-18 19:26Z** run of `python3 reports/round-27/audit/o37-sweep-inventory-audit.py` exited 1: its census found **26** D4-pinning surfaces, of which **9** were swept and **17** missed. The paired `python3 reports/round-27/audit/x61-pin-sweep.py` measurement at **19:26Z** exited 2 and reported only its A/B families. The same `python3 reports/round-27/audit/o37-sweep-inventory-audit.py` is recorded in the dated review's later receipt read as **29** surfaces and **24** missed (`o39-o40-sweep-adversarial.md`, §2). Preserve both inventory snapshots; they are not one stable denominator.

This is a confirmed **instrument-scope** gap against the round-27 O requirement to sweep frozen manifests, batteries, holds, and replay surfaces. It does not establish that every individual surface was bad, nor does it make a claim about the current round-28 sweep implementation.

### O06 — Frozen replay and v3 handoff were red after the O rows were frozen, then the later runner receipt turned green (snapshot-dependent)

At **2026-10-18 19:26Z**, `python3 tools/replay-frozen.py reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv` returned `2 mismatch, 0 reproduced` (exit 1); the same-stamp `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` was exit 1 (`reports/round-27/audit/o39-o40-sweep-adversarial.md`, §3.2). The audit's `stat` timeline (§3.1; **2026-10-18**) places subsequent D-seat packet writes at **16:23:21Z** and **16:24:45Z**, after the O seat froze the generations.

The later recorded `reports/round-27/validation.json` is measured at **2026-10-18 20:08:49Z** and instead has `acceptance_checks_passed: true`, `unrepinned_surfaces: []`, and `handoff-v3: 0`; the archived runner command is `python3 reports/round-27/run-validation.py`. `reports/round-27/pinsweep/sweep-receipt.json` still preserves its own `summary.exit: 1`. These readings are intentionally not collapsed: O06 is the dated failure of the frozen generation under a moving D4 target, not a claim that the later acceptance receipt is red or that the later runner proved every manifest replay green.

## Preservation boundary

These are historical, time-bound findings; the review itself says the D4 packet moved during its observation window. Keep the scope gap separate from the snapshot failure. No round-8–28 file was edited by this sweep.

FILES: reports/round-29/defects/sweep-r27.md | SUMMARY: the R27 inventory missed part of its D4 pin surface, and its frozen/v3 rows changed status across dated snapshots.
