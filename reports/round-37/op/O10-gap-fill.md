- Seat: O10 | executor | claim O | date 2026-10-19 | baseline 57c8409

# O10 — independent defect-census gap candidate

## Finding

**Receipt provenance defect candidate — round 36 runner digest is null.** The filed receipt names `reports/round-36/run-validation.py` at `reports/round-36/validation.json:166`, but its top-level `runner_sha256` is `null` at line 167. In the runner, `rec(p)` computes a digest and inserts it into `inputs` but has no `return` (`reports/round-36/run-validation.py:63-67`); the receipt assigns `runner_sha256` from that helper call (`:210`), which evaluates to `None`. The receipt does contain the runner's digest in `input_sha256` (`validation.json:152`), so the computed value exists but is omitted from the dedicated field. Independent command output confirms the digest: `sha256sum reports/round-36/run-validation.py` → `dd52c5806f5cfd88bb10816b98c4559dd7bf72873d13bdf2836427010a85a4d3`.

The neighboring receipts use a non-null digest in the same field: round 33 (`reports/round-33/validation.json:1283`), round 34 (`reports/round-34/validation.json:196`), and round 35 (`reports/round-35/validation.json:222`). Round-36's filed summary names the stale D premise, coverage findings, route deviation, in-tree-runner incident and README nuance, but not this receipt inconsistency (`SCORECARD.md:651-666`; `LOG.md:3676-3701`). Greps of `SCORECARD.md` and `LOG.md` for `runner_sha256` return no matches.

## Census status and proposed disposition

At this inspection, `reports/round-37/scout/K02-defect-census.md` and `reports/round-37/op/O01-queue-draft.md` did not exist (direct reads returned “does not exist”). Therefore this is a **candidate gap for K02/O01 to account for**, not proof that a completed census or queue omitted it; no census-to-ledger equality or defect count is inferred.

Proposed class: **carried**. The filed round-36 receipt and runner are protected from in-place edits by `reports/round-37/targets.json:4-8`. Proposed owner: round integrator / future runner maintainer. Next touch: add a regression/schema check requiring the top-level runner digest to equal the measured file SHA-256, then record an append-only correction if the r36 receipt needs a corrected reading. Do not rewrite the filed receipt or runner. O01/O02/O03 should determine and verify the final class, owner and routing.

## Sources

- `reports/round-36/validation.json:152,166-168` — input digest exists; dedicated runner field is null.
- `reports/round-36/run-validation.py:63-67,210` — helper has no return; its result populates `runner_sha256`.
- `reports/round-{33,34,35}/validation.json:1283,196,222` — neighboring non-null receipt fields.
- `SCORECARD.md:651-666`; `LOG.md:3676-3701` — round-36 defect summary omits this finding.
- `reports/round-37/targets.json:4-8,12,36-45` — filed-byte rule and K02/O01/O10 assignments.
- Command: `sha256sum reports/round-36/run-validation.py` → `dd52c5806f5cfd88bb10816b98c4559dd7bf72873d13bdf2836427010a85a4d3`.
- No round runner was executed.
