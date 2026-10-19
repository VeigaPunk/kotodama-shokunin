- Seat: K03 | scout | claim A | date 2026-10-19 | baseline 57c8409

# K03 — r7 D4 component/read-set evidence

Axis: adjacency. This is evidence for the round-37 freeze-drift adjudication; it is not the adjudication or an instruction to edit the r7 freeze.

## Findings

1. **The path-set mismatch is real.** The live D4 packet's `assembly.source_sha256` lists 13 components, ending with `13-register-law.yml` ( `examples/culture-d4/packet.d4.yml:2875-2888`); its recorded digest `c0d771…f50b7` equals the component's live SHA-256 (`sha256sum` output below; file is `examples/culture-d4/components/13-register-law.yml`). By contrast, `D4_COMPONENTS` is a 12-item tuple ending at `12-provenance.yml` (`tools/exercise-handoff-e2e.py:157-170`), and `V3_READ_SET` spreads that tuple (`:1939-1959`). The frozen r7 `inputs` contains D4 components 01–12 and omits 13 (`reports/round-34/handoff/declared-in-r7/expected.json:146-161`).

2. **The 13th component is nevertheless digest-checked transitively.** `v3_mine_d4` parses component hashes from the packet's own `assembly` block (`tools/exercise-handoff-e2e.py:2045-2056`); `v3_verify_component_digests` measures every component in the D2/D3/D4 packet manifests and raises `E2E-DIGEST` on mismatch (`:2208-2222`). `V3Assembly` invokes that verifier (`:3502-3510`), and the v3 receipt reports its component totals separately from the read-set file count (`:3861-3862`). The pinned read-set does include `packet.d4.yml` itself (`expected.json:160`), so its component-digest map is pinned as part of that packet's bytes. The recorded live hash for component 13 matches that embedded map.

3. **The filed record documents the two counts, but not the exclusion rationale.** The r7 packet calls the artifact manifest “58 read-set files” and reports D4 packet A-28 has 13 component digests (`reports/round-34/handoff/declared-in-r7/packet.md:35,66`); its validation distinguishes 58 read-set files from 26 component digests (9 D2 + 4 D3 + 13 D4) (`:278-281`), and `freeze.txt:7` records `26/26`. This supports a transitive-integrity interpretation, not a missing-digest finding. However, the runner docstring still calls them “the twelve D4 components” (`tools/exercise-handoff-e2e.py:51-55`), and neither the input map nor the cited prose explicitly says why component 13 is omitted from the direct read-set roster. Thus the evidence establishes a roster asymmetry with transitive digest coverage; whether this is an accepted/documented skip or a defect in the meaning of “read set” remains for the adjudicator.

## Adjudication checklist for A01

- In an isolated `git archive 57c8409` copy, run the v3 **verification** path (for example, `python3 -B tools/exercise-handoff-e2e.py --profile v3 --root <copy> --json`) without `--freeze`. Compare the generated handoff packet and twin checks to the frozen `packet_sha256` / `twin_sha256` in `expected.json`; the verification path compares both (`tools/exercise-handoff-e2e.py:3951-3966`) and runs the D4 assembler `--check` (`:3547-3555`). This seat did not run that comparison; it remains `to-verify` here.
- State whether “read set” requires every file path directly in `expected.json.inputs`, or permits components to be represented by a digest manifest inside a pinned packet. If direct membership is required, record the missing direct row as the defect. If transitive coverage is permitted, cite the 13-component/26-component checks and explicitly document the omission rationale; do not infer intent merely from a green count.
- Keep the r7 freeze immutable. The CLI's `--freeze` branch writes a baseline, while the non-freeze v3 path calls `v3_exercise` (`tools/exercise-handoff-e2e.py:4646-4659`). Do not use `--freeze`, and do not execute any in-tree `reports/round-*/run-validation.py`.

## Owed

- `reports/round-37/adj/A01-freeze-adjudication.md` — isolated r7 packet/twin re-render comparison and the explicit roster-vs-transitive-scope verdict (assigned to A01; not claimed by this scout).

## Citations

- `tools/exercise-handoff-e2e.py:51-55,157-170,1939-1959,2045-2056,2208-2222,2480-2482,2577-2589,3502-3510,3547-3555,3861-3862,3951-3966,4646-4659`
- `examples/culture-d4/packet.d4.yml:2875-2888`
- `examples/culture-d4/components/13-register-law.yml:1-18`
- `reports/round-34/handoff/declared-in-r7/expected.json:124-161,184`
- `reports/round-34/handoff/declared-in-r7/packet.md:33-35,65-66,274-281`
- `reports/round-34/handoff/declared-in-r7/freeze.txt:7`
- Read-only command snapshot (workspace root, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`): `git rev-parse HEAD` → `57c8409ba16d9f9e692297198d95e8f2ce5a1937`; `sha256sum` → packet `aac91246…6eee3`, component 13 `c0d77181…f50b7`, r7 expected `bbe15887…9d55`, freeze `3969954b…1223`.
- Read-only Python comparison of `packet.d4.yml` `assembly.source_sha256` to r7 `expected.json.inputs` (after exporting the required environment): `packet_manifest_component_count=13`; `r7_inputs_d4_component_count=12`; `manifest_not_readset=['examples/culture-d4/components/13-register-law.yml']`; `readset_not_manifest_count=0`; `component_13_manifest_digest=c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7`; `component_13_live_digest=c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7`; `r7_input_count=58`.
