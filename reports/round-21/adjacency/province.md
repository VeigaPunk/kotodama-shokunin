# Round 21 — PROVINCE accuracy (R21-A09..A10)

- **Date:** 2026-10-18. **Lane:** `kotodama-shokunin`.
- **Assignment:** compare `PROVINCE.md` with loop-2 capability (D4 family, handoff v3, round-20 wart fix); draft a correction only if it drifted.
- **Verdict: ACCURATE; no correction draft.** The three capabilities remain lane-local linguistic-cultural design and verification craft. The handoff remains a non-canon, computational submission/check surface; neither it nor the family-specific alias fix claims lore authority, general research-method ownership, or historical-truth certification.

## Evidence

- **D4 family and wart fix fit `Owns`.** `PROVINCE.md` defines the domain as linguistic-cultural worldbuilding (§Domain, lines 3–7), owns the lane's knowledge partitions, gates, non-canon examples and reports (§Owns, lines 9–14), and refuses canon and general research method (§Refuses, lines 16–20). The live projector derives a family from `examples/culture-<family>/…` and defaults nonmatching paths to D2 (`tools/d2-typed-labels.py:2457–2466`); its D2 branch retains D2 inputs while other families use the packet's own declared aliases and expose undeclared legs as skips (`tools/d2-typed-labels.py:2512–2518`). The D4 adapter's self-test mirror copies the D4 tree but explicitly omits the foreign D2 tree (`tools/assemble-d4-typed.py:424–438`).

  Re-measured on **2026-10-18** with `export TMPDIR=$PWD/.scratch; python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` → byte-identical projection; `export TMPDIR=$PWD/.scratch; python3 tools/assemble-d4-typed.py --selftest` → 12/12 checks passed, including D4 emission from the D2-free mirror; `export TMPDIR=$PWD/.scratch; python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → 19/19 legs passed. These checks exercise the lane's own tooling/examples; they do not change its ownership boundary.

- **Handoff v3 stays within the adjacent contract.** `PROVINCE.md` assigns the world bible and consistency verification to lore, identifies the shared integration contract and routes contested scope outward (§Adjacent contract, lines 22–25). The contract says it is a method/reference interface, not a canon ruling or world-bible entry, keeps lore's canon and bible ownership, and denies kotodama world-bible write access (`corpus/knowledge/synthesis/worldbible-integration-contract.md:9–19`). It further limits kotodama to local generation and submission, not bible-wide consistency certification, and makes delivery distinct from acceptance/canon import (`…worldbible-integration-contract.md:124–136`).

  Re-measured on **2026-10-18** with `export TMPDIR=$PWD/.scratch; python3 tools/exercise-handoff-e2e.py --profile v3` → exit 0; 16/16 fields, 20 glossary entries, zero gate findings; uncertainty check over 27 claims with zero findings; census 27 claims (16/7/4 statuses); 105/105 links; 58 read-set files preserved. The profile's passing computational checks verify the packet envelope, not its claims as truth or canon.

- **PROVINCE pin/current-state check.** On **2026-10-18**, `git diff --quiet -- PROVINCE.md` exited 0 and `git rev-parse HEAD:PROVINCE.md` returned blob `313b182f251564b7997b06996b4f063370778f11` (command batch stamped by `date -u '+%Y-%m-%dT%H:%M:%SZ'` at `2026-10-18T13:50:03Z`). The declaration remains unchanged; the live capabilities map to its existing ownership and refusal clauses.

## Routed limitation, not Province drift

Round 20's wart review recorded a separate malformed-alias edge case: declared tag values are coerced with `str(...)` (`tools/d2-typed-labels.py:2477–2506`; `reports/round-20/wart/review.md`, §3 F5). The family-isolation fix and the re-measured valid D4 path do not establish fail-closed validation for malformed declarations. This is a tool-quality/conformance item for the operability queue, not evidence that the lane has absorbed another province or that `PROVINCE.md` needs a scope correction; no new test of malformed declarations was run for this province audit.

## Disposition

No change to `PROVINCE.md` is warranted. D4 family craft and its non-canon fixtures fall under the existing lane domain and tools/examples ownership; v3 implements the existing lore handoff boundary without taking canon or bible authority; the wart fix changes a lane-local tool, not the lane's remit. Out-of-province decisions continue to be reported rather than absorbed, as `PROVINCE.md:31` requires.
