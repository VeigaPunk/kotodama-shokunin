- Seat: O08 | executor | claim O | date 2026-10-19 | baseline 57c8409

# O08 — supplemental operability defect evidence

## Gap found: r34/r35 runner isolation is not clone-safe

The round-34 and round-35 validation runners hardcode the live repository root and immediately `chdir` to it (`reports/round-34/run-validation.py:10,26`; `reports/round-35/run-validation.py:9,36`). Their publish paths then open `reports/round-34/validation.json` and `reports/round-35/validation.json` for writing (`reports/round-34/run-validation.py:532-535`; `reports/round-35/run-validation.py:502-505`). A plain `git archive` or clone therefore does not isolate a publishing run of either runner: execution redirects to the original worktree before the relative receipt path is resolved. The r35 runner's `--check` branch returns before publication (`reports/round-35/run-validation.py:496-505`), but that is not a remedy for the publishing path.

This is a distinct mechanism-level queue item, not merely a repeat of the earlier unguarded-runner finding: the round-34 adoption inventory's `guarded-refresh` protocol routes refreshes to an isolated clone (`reports/round-34/op/adoption-inventory.json:102-107`), while r34/r35's absolute root defeats that isolation. The r36 conformance audit explicitly documents repeated r34/r35 receipt rewrites, identifies the hardcoded-root defect as its cause, and requests it be recorded as its own finding (`reports/round-36/cross/X02-conformance.md:187-223`). Ca05 independently records the same root/chdir mechanism and calls plain clone execution unsafe for these runners (`reports/round-36/calib/Ca05-receipt.md:28-45,166-174`).

**Disposition proposed for O01:** `carried-with-owner+reason+next-touch`; do not classify as fixed. Owner: integrator to assign the implementation seat. Reason: r34/r35 are filed bytes and may not be edited; only a successor runner generation can replace the unsafe root behavior. Next touch: O09 routes the item to round 38 or a later operability/build round; the assigned owner drafts a successor runner that resolves its root from the copied checkout, then verifies a publishing invocation in an isolated copy writes only there. The round-36 evidence documents runner-filed-byte restoration but does not establish that this isolation defect was repaired (`reports/round-36/cross/X02-conformance.md:198-223`; `reports/round-36/calib/Ca05-receipt.md:161-174`).

This seat did not execute any round runner and makes no claim that a fix has been implemented or independently verified.

## Owed

- O01: add this as a distinct, unnumbered-until-integrated carried defect; preserve the mechanism and citations above rather than folding it into F-C13-1's original unguarded-writer class.
- O09: assign a round-38+ next-touch and named implementation owner; `reports/round-37/targets.json:44` assigns O09 the routing table.
- Integrator: confirm the final route and queue row after O01/O09 land; this fragment alone does not establish census-to-queue completeness.

## Citations

- `reports/round-34/run-validation.py:10-11,26,532-535` — absolute live root, `chdir`, and receipt write path.
- `reports/round-35/run-validation.py:9-10,36,496-505` — absolute live root, `chdir`, check-only early return, and receipt write path.
- `reports/round-34/op/adoption-inventory.json:102-107` — `guarded-refresh` route prescribes isolated clone refresh.
- `reports/round-36/cross/X02-conformance.md:187-223,227-234` — repeated breach, hardcoded-root finding, carried correction, and attribution limits.
- `reports/round-36/calib/Ca05-receipt.md:28-45,145-174` — independent mechanism observation and clone-safety finding.
- `reports/round-37/targets.json:43-44`; `REGIMEN.md:15-16` — O08 out scope / O09 routing mission and round-38 build position.
