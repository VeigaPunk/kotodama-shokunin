- Seat: R05 | reviewer | A | date 2026-10-19 | baseline 57c8409

# R05 — adversarial review of A01 freeze adjudication

**Review verdict: A01's re-render conclusion is supported; its adjudication is appropriately scoped.** I independently re-rendered from an isolated `git archive HEAD` copy, compared the resulting r7 `packet.md` and `twin.json` byte-for-byte with the filed pair, and separately checked `expected.json`. All three comparisons passed. The 13th component is absent from the direct `V3_READ_SET`/frozen input roster, with no documented exclusion rationale in the cited inventory prose; however, it remains covered by the packet's pinned component manifest, and a mutation probe confirms the verifier rejects changed bytes. Therefore “roster/completeness defect, not a demonstrated integrity bypass” is a defensible distinction (`reports/round-37/adj/A01-freeze-adjudication.md:5-31`).

## Independent checks

- Re-rendered in `.scratch/r05-freeze-audit.zwWL6W/tree` from `git archive HEAD` (`57c8409ba16d9f9e692297198d95e8f2ce5a1937`); the `--freeze` target was the separate `.scratch/.../replayed-r7` directory, never the filed `declared-in-r7` path. `cmp` passed for the filed/replayed `packet.md` and `twin.json`; a second `cmp` passed for `expected.json`. The hashes match: packet `45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`, twin `0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599`, expected `bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55` (R05 command output; compare targets and hashes also filed at `reports/round-34/handoff/declared-in-r7/freeze.txt:1-10`).
- The roster distinction is real: `D4_COMPONENTS` has 12 paths (`tools/exercise-handoff-e2e.py:157-170`), and the pinned `expected.json` input map has 58 entries without component 13 (`reports/round-34/handoff/declared-in-r7/expected.json:124-183`). The packet itself records component 13's digest (`examples/culture-d4/packet.d4.yml:2875-2888`); `v3_mine_d4` extracts assembly-manifest entries and `v3_verify_component_digests` measures each (`tools/exercise-handoff-e2e.py:2045-2056,2208-2222`).
- In a second isolated archive, a comment-only edit to component 13 followed by `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` returned exit 1 with `E2E-DIGEST` (recorded digest `c0d77181ac56…`, measured changed digest `0b43132584da…`; R05 command output). This independently confirms transitive detection for that component; it does not make the direct-roster omission disappear.
- A01's summary is substantively corroborated. Minor traceability note: A01 reports `cmp` results but does not show the literal compare commands/exit statuses; the independent commands and results above supply that evidence (`reports/round-37/adj/A01-freeze-adjudication.md:11-22`).

## Process note

During an initial probe setup, I mistakenly appended the test comment to the workspace copy rather than the isolated archive. I removed that exact suffix immediately; the follow-up SHA-256 returned the original component digest `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7`, and `git status --short` showed no modified tracked paths. The corrected probe was then run inside the isolated archive only (command output; restored path: `examples/culture-d4/components/13-register-law.yml`). No filed r7 bytes or other tracked files remain changed.

## Owed

- Integrator: route the direct-read-set/documentation correction to a future baseline revision; keep r7 immutable. R05 has no remaining evidence dependency (`reports/round-37/adj/A01-freeze-adjudication.md:31-35`; `reports/round-37/targets.json:7`).

## Citations

- `reports/round-37/adj/A01-freeze-adjudication.md:5-31` — adjudication, render claim, component roster finding, and disposition.
- `reports/round-37/scout/K03-freeze-drift.md:9-19` — independent source map and verifier rationale.
- `tools/exercise-handoff-e2e.py:51-59,157-170,1939-1953,2045-2056,2208-2222,3480-3510` — documented roster, read-set construction, assembly-manifest parsing, and digest-check path.
- `examples/culture-d4/ASSEMBLY.md:12-24`; `reports/round-34/handoff/repin.json:32-38` — 12-input prose versus recorded correction to 13 authored components.
- `reports/round-34/handoff/declared-in-r7/expected.json:124-183`; `reports/round-34/handoff/declared-in-r7/freeze.txt:1-10`; `examples/culture-d4/packet.d4.yml:2875-2888`.
- R05 command outputs: isolated `git archive HEAD`; `python3 tools/exercise-handoff-e2e.py --profile v3 --freeze <separate scratch target>`; `cmp` of packet/twin/expected (all exit 0); isolated component-13 mutation `E2E-DIGEST`; restored component SHA-256 and `git status --short`. No `reports/round-*/run-validation.py` was executed.
