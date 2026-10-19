- Seat: O11 | executor | O | date 2026-10-19 | baseline 456674d

## Gap-fill: test guard dominance, not token presence

The checker selftest should distinguish an actually dominating `guard_receipt()` call from a mere textual occurrence. For every publishing path, require the guard to execute before the receipt write; a guard inside an unreachable branch, after the write, or in an uncalled helper must not satisfy the contract. Include a positive control for the reference runner's early-return `--check` / `--selftest` paths: those do not publish and return before the guard, while the normal path calls the guard before opening `validation.json` for writing. This narrows a likely false-green in shallow AST/text checks without incorrectly rejecting the reference's non-publishing modes.

Suggested selftest cases: accept (1) guard then receipt write and (2) early-return non-publishing mode plus guarded publishing mode; reject (3) no guard, (4) guard only after write, (5) guard only in a dead branch or uncalled function, and (6) one publishing branch that bypasses the guard. This supplements rather than replaces a fake conformant/non-conformant runner pair.

## Owed

None. This is an evidence-backed checker test recommendation; O11 did not execute or modify a runner/checker.

## Citations

- `reports/round-41/claims.json:13-18` — O claim specifies guard dominance among the runner contract points and requires checker selftest.
- `reports/round-41/targets.json:111-115` — O11 spare gap-fill assignment and output path.
- `reports/round-40/run-validation.py:233-247` — reference `main`: `--check` and `--selftest` return before the normal-path guard; normal publication calls `guard_receipt()` before opening `validation.json` for writing.
