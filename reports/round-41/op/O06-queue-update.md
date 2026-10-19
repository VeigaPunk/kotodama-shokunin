- Seat: O06 | executor | O | date 2026-10-19 | baseline 456674d

## Queue-v2 delta draft

Apply these two row deltas to the round-41 successor queue only; do not edit the filed round-40 queue. The source rows are `N7-receipt-fidelity` and `r39-runner-root-regression` in `reports/round-40/op/defect-queue-v2.json`. This draft proposes `fixed-with-evidence` only after the integrator has the canonical template/checker and the required verifier evidence below. Historical r34-r39 runners and receipts remain filed readings, not repaired bytes.

### `N7-receipt-fidelity`

Before (round 40):
```json
{
  "class": "carried-with-owner",
  "owner": "integrator (the r40 runner is the first cure)",
  "reason": "four receipts carry runner_sha256:null (r37:148, r36, r38, r39) and r39's filed receipt duplicated r38's named_findings/CO route verbatim against r39's actual zai dispatch",
  "next_touch": "cured by the r40 runner (relative ROOT, non-null runner_sha256, round-specific findings)",
  "evidence": "reports/round-40/review/R01-review.md"
}
```

Proposed successor values (retain the row's `id` and `origin`):
```json
{
  "class": "fixed-with-evidence",
  "owner": "round-41 integrator (records the landing and verifier outputs)",
  "reason": "Receipt fidelity is fixed for forward runner generation: r40 supplies the corrected reference receipt, and the canonical template plus conformance checker make the required receipt fields a repeatable contract. This closes the forward-generation defect only; the four historical null-hash receipts and r39's stale findings/route remain unchanged and must appear as historical defects in the census.",
  "next_touch": "none for the round-41 fix; re-run the conformance checker on each successor runner, beginning in loop 2",
  "evidence": "reports/round-40/run-validation.py:197-209; reports/round-40/validation.json:135-144; templates/round-runner-template.py (landed); tools/harness/round_runner_conformance.py (landed); python3 tools/harness/round_runner_conformance.py --selftest (captured output); python3 tools/harness/round_runner_conformance.py --json (captured census output)",
  "verification": "Fill with the observed selftest result and census output after O04/O05 verification; do not mark fixed before those artifacts exist."
}
```

### `r39-runner-root-regression`

Before (round 40):
```json
{
  "class": "carried-with-owner",
  "owner": "round-40 runner author",
  "reason": "the r39 runner re-carried ROOT = \"/home/vgpnk/Projects/shokunin/kotodama-shokunin\" + os.chdir(ROOT) (:5,:13) — the exact O12 hazard shape its own dossier spec'd against ('the ROOT line is the load-bearing one', S01 §5; r38's ruling: 'copy the r33 relative-ROOT shape, never the r34/r35 absolute os.chdir shape') — plus a stale 'Round-38 acceptance runner' docstring (:2); the streak is six (r34-r39); the r39 record's own Ca claim ('the protocol addresses O12') must not be read as the runner being remediated",
  "next_touch": "r40's own runner is the first relative-ROOT cure; loops 2-3 runners must follow (S01 dossier)",
  "evidence": "reports/round-39/run-validation.py:2,5,12 (this seat's head -14, 2026-10-19); reports/round-39/scribe/S01-integration-draft.md:371-396; reports/round-38/cross/X01-trades.md:365-370",
  "verification": "HEAD read by this seat at fd55e1f"
}
```

Proposed successor values (retain the row's `id` and `origin`):
```json
{
  "class": "fixed-with-evidence",
  "owner": "round-41 integrator (records the landing and verifier outputs)",
  "reason": "The runner-root regression is fixed for forward runner generation: r40 is the relative-ROOT reference, and the canonical template/checker encode and audit that shape. The r39 filed runner itself remains an immutable historical defect; the checker census must continue to classify it as such.",
  "next_touch": "none for the round-41 fix; require the checker on successor runners, beginning in loop 2",
  "evidence": "reports/round-40/run-validation.py:1-7,227-248; templates/round-runner-template.py (landed); tools/harness/round_runner_conformance.py (landed); python3 tools/harness/round_runner_conformance.py --selftest (captured output); python3 tools/harness/round_runner_conformance.py --json (captured census output)",
  "verification": "Fill with the observed selftest and row-by-row census result after O04/O05 verification; include the r40 reference-shape result from O09."
}
```

## Owed

- `templates/round-runner-template.py`, `tools/harness/round_runner_conformance.py`, and captured `--selftest` / `--json` outputs were not present at draft time; the verifier/ integrator must attach the landed paths and actual outputs before applying either reclassification. The claim requires checker selftest and a seven-runner census (`reports/round-41/claims.json:14-18`).
- Census scope is internally inconsistent: the claim describes seven runners r34-r40, but its threshold glob `reports/round-3[3-9]/run-validation.py + round-40` covers r33-r39 plus r40 (eight paths). Resolve the roster/count in integration and ensure the checker covers the agreed complete set before claiming fixed (`reports/round-41/claims.json:14-18`).

## Citations

- `reports/round-41/targets.json:76-80` — O06 mission and assigned output.
- `reports/round-41/claims.json:14-18` — template/checker contract, r40 reference requirement, and census threshold.
- `reports/round-40/op/defect-queue-v2.json:312-319` — current r39 regression row.
- `reports/round-40/op/defect-queue-v2.json:370-377` — current N7 row.
- `reports/round-40/run-validation.py:1-12,197-209,227-248` — r40 runner's relative root, receipt hash/findings/limits, guard-before-write sequence.
- `reports/round-40/validation.json:135-144` — r40 named findings, runner path, and non-null runner SHA-256.
- `reports/round-40/op/defect-queue-v2.json:8,51-59` — queue class vocabulary and prior fixed-with-evidence row shape.
