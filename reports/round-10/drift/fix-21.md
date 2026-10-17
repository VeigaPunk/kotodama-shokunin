# R10-F21 — stale fix: battery row's verdict map omitted duty 2 (committed default exits 2)

- seat: freshness stale-fixer (R10-F16..F19). This file is the seat's write; the
  `SKILL.md` row correction below is the in-place fix.
- date: 2026-10-17 · lane: `kotodama-shokunin` · baseline `9dc18ec1…`
- live HEAD at work: `e3a1ec9` (+ worktree edits)

## Items taken from the ledger

| ledger row (0-based) | locator | shard | verdict in ledger |
|---|---|---|---|
| 92 | `SKILL.md:194` (`python3 tools/check-gate-battery.py`) | shard-10 | `stale-documented` (DR-10-02) |
| 97 | invoked by `reports/round-5/run-validation.py:120` | shard-11 | `stale-documented` |
| 112 | `SCORECARD.md:52` | R10-F15-battery | `stale-documented` (with reason + three-root control) |

shard-10 §DR-10-02 states the remaining obligation exactly: "a SKILL row that
says '0 seven selftests pass' while the committed command exits 2 remains
misleading until either the pins are relocated or the row documents duty 2."
This fix takes the second branch; relocating pins is the orchestrator's call
(`reports/round-9/baselines/registry.md` §5 items 1, 6, 7).

## Evidence

- Committed default (this seat, 2026-10-17, lane root): exit **2**;
  duty 1 `pass 7 / fail 0 / unevaluable 0`,
  `originals {preserved: true, modified 0, added 0, deleted 0,
  files_hashed_before 28, files_hashed_after 28}`;
  duty 2 `baselines_found 5, pinned 5, readings {pinned: 5}`,
  `gates_uncovered [myth-consistency-gate.py, naming-collision-gate.py]`,
  two `BASELINE-GATE-UNCOVERED` findings; `verdict_replay: "not-run: …"`.
- Three-root control: `python3 tools/check-gate-battery.py --baselines-root
  tools/gates/expected --baselines-root tools/gates/frozen --baselines-root
  reports/round-9/baselines` → exit **0**, `baselines_found 8, pinned 8,
  readings {pinned: 8}, gates_uncovered []`.
- The two pins are present and valid; the gap is discovery
  (`BASELINE_ROOTS = (tools/gates/expected, tools/gates/frozen)`), which is why
  the battery's own help text refuses to read `--baselines-root` as a way to
  silence a committed defect.

## Disposition

1. `stale-fixed` — the `SKILL.md` battery row's verdict map now documents both
   duties, names the committed default's exit 2 and the uncovered gates, and
   points at the three-root remedy. Replacement cell:

```
duty 1 (selftests): 0 seven selftests pass / 1 recognized selftest failure /
2 could-not-evaluate; duty 2 (baselines): 0 every discovered pin verifies /
2 tampered, revised or uncovered gate — exit is the worse of the two, and the
committed default currently exits 2 with `BASELINE-GATE-UNCOVERED` for myth and
naming, whose pins live under `reports/round-9/baselines/`; add that root via
`--baselines-root` to reach 0 (`reports/round-9/baselines/registry.md` §5 item 6;
`reports/round-10/drift/fix-21.md`)
```

2. `stale-documented` (unchanged, still open for the orchestrator) — the pin
   **layout** decision: copy the myth/naming pins under a committed root, or
   adopt the third root durably. This seat does not relocate pins: the registry
   records the choice as the orchestrator's, and copying the naming pin would
   interact with the duplicate-id question (§5 item 7).

## Control (re-runnable)

- `grep -n "duty 2 (baselines)" SKILL.md` → the corrected row (exit 0).
- `grep -c "0 seven selftests pass / 1 recognized selftest failure / 2 could-not-evaluate" SKILL.md`
  → `0` (the bare, misleading map is gone).
- `python3 tools/check-gate-battery.py --selftest` → exit 0, 28/28 controls.
- The corrected row's new cited tokens introduce no new ledger key: the
  `--baselines-root` token is written outside any backtick span containing
  `python3` (validator's extraction rule), and the two `python3` keys on that
  line (`check-gate-battery.py` bare and `--selftest`) already exist in the
  ledger.

## Limits

- Documenting duty 2 does not make the committed default green; the exit-2
  reading stands until the layout question is decided.
- The battery never re-executes a baseline (`verdict_replay: not-run`) — pin
  verification is not a verdict comparison.

## Ledger delta (for the F14 scribe / integrator)

```json
[{"id": "R10-F21-01", "command": "python3 tools/check-gate-battery.py", "source_locator": "SKILL.md:194", "round10_verdict": "stale-fixed", "output_sha256": "6fd828d32bfbde7724cfc8baea845206d8aef0a5c3a7e1b6ab9a1685286abc6e", "exit": 2, "fix_evidence": "reports/round-10/drift/fix-21.md", "note": "row's verdict map now documents duty 2 and the committed default's exit 2 + uncovered gates + three-root remedy; pin relocation itself stays the orchestrator's decision (registry §5 items 1/6/7)"},
 {"id": "R10-F21-02", "command": "python3 tools/check-gate-battery.py --baselines-root tools/gates/expected --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines", "source_locator": "SKILL.md:194 (documented remedy)", "round10_verdict": "current", "output_sha256": "c164b1e2c386c9b24f4054076964713d25934478b6e6fbb7eab2be0792a52fee", "exit": 0, "note": "green control re-run by this seat: baselines_found 8, pinned 8, gates_uncovered []"}]
```
