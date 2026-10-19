- Seat: A07 | executor | claim A (adjacency) | date 2026-10-19 | baseline 57c8409

# A07 — gap-fill: chronology and scope of the r7 D4 omission

## Finding

The `13-register-law.yml` component is present in D4's packet manifest but absent from the r7 frozen `inputs` map. This was not a component added after the r7 freeze: the path was added by round 27 commit `6c0ac44` (command output below), while the r27 v3 baseline was frozen on 2026-10-18 (`reports/round-27/pinsweep/v3-baseline-r27/freeze.txt:1`) and r7 was frozen by round 34 on 2026-10-19 (`reports/round-34/handoff/declared-in-r7/freeze.txt:1`).

The r27 commit left the v3 runner's `D4_COMPONENTS` tuple unchanged at components 01–12: `git show 6c0ac44^:tools/exercise-handoff-e2e.py` and `git show 6c0ac44:tools/exercise-handoff-e2e.py` both print that same tuple; `git diff 6c0ac44^ 6c0ac44 -- tools/exercise-handoff-e2e.py` shows only the baseline/frozen-dir defaults changed. The current tuple still ends at `12-provenance.yml` (`tools/exercise-handoff-e2e.py:157-170`), and the r27 frozen input list also has only those twelve (`reports/round-27/pinsweep/v3-baseline-r27/expected.json:144-161`). The omission therefore predates r7 and persisted through it; it is not shown as a deliberate r34-only exclusion.

There is a separate, broader D4 assembly baseline in round 27: its `repin.py` discovers all component YAML files by glob (`reports/round-27/pinsweep/repin.py:58-66`), and the receipt says that baseline pins the packet plus all 13 components (`reports/round-27/pinsweep/sweep.md:192-200`). That is a different instrument and does not establish membership in the v3 handoff runner's read set.

The `explicit skip` wording in D4-CL08 concerns its family-local alias explanation: it skips reading D2 `11-costumes.yml` for D4 reconciliation (`reports/round-34/handoff/declared-in-r7/packet.md:151`; `twin.json:1139-1141`). That text does not document skipping `13-register-law.yml` from the v3 read set. The freeze line says `read set: 58 files; component digests 26/26` (`freeze.txt:7`), which is not a count of D4 components in the `inputs` map. A01's isolated-copy comparison independently adjudicates the latter as a roster/completeness defect, not a documented skip (`reports/round-37/adj/A01-freeze-adjudication.md:5,22,26-31`).

## Scope and limits

A read-only probe at the declared baseline measured: `expected.inputs` total 58; D4 component paths in `expected.inputs` 12; D4 component manifest rows in the live packet 13; manifest includes `13-register-law.yml: True`; r7 inputs include it: `False`. `sha256sum` reports component `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7` and packet `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3` (command outputs below; packet manifest row also appears at `examples/culture-d4/packet.d4.yml:2888`).

This is a direct-read-set omission, not evidence that the component digest is wholly unverified: `v3_verify_component_digests` iterates the component maps supplied by each packet and measures their live paths (`tools/exercise-handoff-e2e.py:2208-2222`). A01 now reports the isolated pair re-render byte-identical and the component mutation control detected (`reports/round-37/adj/A01-freeze-adjudication.md:5,22,29-31`). This fragment adds the historical chronology only; it does not independently validate A01 or close claim A.

## Owed

- Integrator: route the read-set roster/documentation correction to a future baseline revision without rewriting or re-freezing the filed r7 pair (`reports/round-37/adj/A01-freeze-adjudication.md:31-35`). A06/A08 independent verification remains a separate integration requirement (`reports/round-37/targets.json:54,56`).

## Citations

- `reports/round-37/claims.json:25-30`; `reports/round-37/targets.json:7-8,49` — required freeze adjudication and no-re-freeze / no-in-tree-runner boundary.
- `reports/round-27/adjacency.md:371-379` — `assembly.skipped_keys` pertains to component metadata keys and deterministic `packet_keys` wiring, not the v3 read-set.
- `reports/round-27/pinsweep/repin.py:58-66`; `reports/round-27/pinsweep/sweep.md:192-200` — separate adapter baseline uses all component YAML files and pins 13.
- `reports/round-27/pinsweep/v3-baseline-r27/freeze.txt:1,7`; `reports/round-27/pinsweep/v3-baseline-r27/expected.json:144-161` — round-27 v3 baseline date, count, and D4 input list.
- `reports/round-34/handoff/declared-in-r7/freeze.txt:1,7`; `reports/round-34/handoff/declared-in-r7/expected.json:144-157`; `reports/round-34/handoff/declared-in-r7/packet.md:151`; `reports/round-34/handoff/declared-in-r7/twin.json:1139-1141` — r7 freeze, component input list, and unrelated D2-family alias skip.
- `examples/culture-d4/packet.d4.yml:2888`; `tools/exercise-handoff-e2e.py:157-170,1939-1954,2208-2222` — current packet manifest, v3 read-set construction, and transitive component-digest verification.
- Command outputs, 2026-10-19, from repo root with `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:
  - `git log --follow --format='%h %ad %s' --date=iso-strict -- examples/culture-d4/components/13-register-law.yml` → `6c0ac44`, round 27, 2026-10-18.
  - `git show --format='commit %H%ncommit-date %cI%nsubject %s' --name-status 6c0ac44 -- ...` → component added and `tools/exercise-handoff-e2e.py` modified; `git show ...` before/after 6c0ac44 both show `D4_COMPONENTS` 01–12; `git diff 6c0ac44^ 6c0ac44 -- tools/exercise-handoff-e2e.py` shows only `V3_BASELINE_DEFAULT` / `V3_FROZEN_DIR_DEFAULT` path changes.
  - Read-only `python3 -B -c` probe of r7 JSON and packet manifest → `r7 expected.inputs total: 58`; `r7 D4 component input count: 12`; `packet assembly component manifest count: 13`; `manifest component 13: True`; `r7 includes 13-register-law: False`.
  - `sha256sum examples/culture-d4/components/13-register-law.yml examples/culture-d4/packet.d4.yml` → `c0d77181…f50b7`, `aac91246…c76eee3`.
  - No `reports/round-*/run-validation.py` and no freeze command was executed.