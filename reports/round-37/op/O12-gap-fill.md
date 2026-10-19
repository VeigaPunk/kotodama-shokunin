- Seat: O12 | executor | claim O | date 2026-10-19 | baseline 57c8409

# O12 — Operability queue gap-fill: absolute-root isolation defect

## Candidate queue row

- **Finding:** The round-34 and round-35 filed runners defeat plain clone/archive isolation: each sets `ROOT` to the live repository and calls `os.chdir(ROOT)` (`reports/round-34/run-validation.py:10,26`; `reports/round-35/run-validation.py:9,36`). Their default publish paths then open the relative `reports/round-N/validation.json` for writing (`reports/round-34/run-validation.py:532-535`; `reports/round-35/run-validation.py:502-505`).
- **Disposition:** carried; this is an extant runner-design hazard, not fixed by restoring a receipt. The r36 conformance report independently calls it a real isolation-protocol defect and recommends a successor runner generation rather than editing filed runners (`reports/round-36/calib/Ca05-receipt.md:166-174`; `reports/round-36/cross/X02-conformance.md:196-223`).
- **Owner:** round-37 integrator for queue routing; round-38+ operability/runner maintainer for resolution (`reports/round-36/cross/X02-conformance.md:196-223`).
- **Reason carried:** the source runners are filed bytes and their hard-coded root makes a plain copied-tree invocation unsafe; no replacement runner or control proving publish-mode isolation is evidenced here. `--check` returns before publishing, but does not repair the default publish path (`reports/round-34/run-validation.py:527-535`; `reports/round-35/run-validation.py:497-505`; `reports/round-36/calib/Ca05-receipt.md:35-45`).
- **Next touch:** round 38+ operability routing, before any publish-mode recount/replay of r34/r35: use an isolation mechanism that contains the absolute-root `chdir`, or route to a new runner generation with a copy-relative root. Preserve the filed r34/r35 runners; do not treat an isolated `cd`/`git archive` copy alone as containment (`reports/round-36/cross/X02-conformance.md:212-223`).
- **Evidence status:** mechanism is corroborated by the runner source and two independent r36 reports; per-write actor attribution remains `to-verify` (`reports/round-36/cross/X02-conformance.md:227-234`; `reports/round-36/calib/Ca05-receipt.md:152-160`). This fragment did not execute any round runner.

## Owed

- Integrator: reconcile this candidate against the O01 queue and retain it as a distinct carried row if not already represented; no r37 queue exists in the tree at this fragment's write time.
- Round-38+ operability owner: supply evidence for a safe replacement/isolation control before changing disposition to fixed.

## Citations

- `reports/round-34/run-validation.py:10,26,527-535` — absolute root, chdir, `--check` branch, and receipt write.
- `reports/round-35/run-validation.py:9,36,497-505` — same mechanism in r35.
- `reports/round-36/calib/Ca05-receipt.md:28-45,166-174` — clone-isolation limitation and mechanism diagnosis.
- `reports/round-36/cross/X02-conformance.md:187-223,227-234,687-690` — F-C13-1 violation, successor-runner recommendation, actor attribution limit, and separately file the hardcoded-root defect.
- `SCORECARD.md:664-668` — r36 rejection and conformance incident recorded; restoration is not a fix to this structural issue.
