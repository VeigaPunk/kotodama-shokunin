# R9-D11 — D3 packet × d3-contract.json field-by-field cross-check

- date: 2026-10-17
- shard: R9-D11 (D3 acceptance, round 9)
- contract: `reports/round-7/d3-contract.json` (profile `kotodama-d3-evidence-coupling/1`)
- object under test: `examples/culture-d3/packet.json` (sha256 `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829`) plus its contracted sibling outputs
- tree revision at check time: `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` (round-9 claims commit; D3 artifacts last committed at `57c3ce6`)
- method: mechanical re-derivation of every contract field from the delivered bytes (scratch checker, 138 assertions; command in §Reproduce), plus the shipped tools run as independent oracles

## Verdict

**Packet: contract-consistent.** 138/138 packet-side contract checks pass. `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json` → exit 0, `findings: []`; `python3 tools/assemble-culture-d3.py --check` → "packet.json: byte-identical deterministic assembly; packet.gates.yml: byte-identical deterministic assembly", exit 0; `python3 tools/check-evidence-coupling.py --selftest` → `selftest_passed: true` (5 positive / 16 domain / 4 malformed / 5 frozen, all passed), exit 0.

**One contract-level finding (F-1), not a packet defect:** the contracted frozen snapshot `examples/culture-d3/expected.json` is stale for 3 of its 24 manifest entries, so the exact frozen replay now refuses:

```
$ python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json
{"counts": {"D3-SNAPSHOT": 3, "total": 3}, "exit": 2, "findings": [ ... 3× D3-SNAPSHOT ... ]}
```

The D claim's acceptance wording ("D3 replays frozen without digest drift") is therefore **not met as delivered** until the pin is refreshed. Cause is legitimate, documented round-8 input edits (F-1 detail below); this shard's disposition recommendation is refresh, never weakening the check.

## F-1 — frozen expected.json pin drifted (finding)

Contract text it violates, verbatim:

- `d3-contract.json` §`guard_cli`: "Snapshot mode verifies every persisted input digest BEFORE verdict and returns exit2 D3-SNAPSHOT on tamper."
- `examples/culture-d3/expected.json` §`limits` (its own declaration): "later input edits invalidate this snapshot before verdict."

Measured mismatches (declared in `expected.json` manifest vs actual bytes, `sha256sum`/hashlib, 2026-10-17):

| manifest entry | declared (expected.json) | actual (tree) |
|---|---|---|
| `corpus/knowledge/synthesis/worldbible-integration-contract.md` | `50c4c2f2…7268c1` | `5f4c02bf…f79069` |
| `tools/gates/costume-era-consistency-gate.py` | `29a9361c…a43f03` | `e6bffd70…c478f` |
| `tools/gates/naming-collision-gate.py` | `8c5afb0a…9aa526` | `d9e4e8f4…630a1d` |

Provenance (git, 2026-10-17):

- `expected.json` is unchanged since `57c3ce6` ("checkpoint: preserve unfinished round-7 D3 integration"); its declared digests equal the file bytes at `57c3ce6` (verified with `git show 57c3ce6:<path>` hashing). So the pin was correct when authored — this is drift, not an authoring error.
- All three files were modified by `e1694ba` ("round-8: admit F/O/D — freshness receipts, harness+gate repairs, d2-typed-labels"), i.e. after the pin.
- The two gate changes are documented in round 8 with reasons and new digests: `reports/round-8/operability/audit.md:23,25` records exactly `d9e4e8f4…` and `e6bffd70…` as the post-repair live hashes; the repairs themselves are recorded in `reports/round-8/operability/o02-fix.md` and `reports/round-8/operability/neg-controls/neg-09/neg-09-report.md` (and the same class of pin staleness is explicitly handled there for the round-3 manifest: `…/neg-09/evidence-replay-gate-digest.txt` — "the replay tool correctly refuses (exit 2) instead of replaying unpinned code").
- The worldbible-contract change is the round-8 metadata pass (`git diff 57c3ce6 e1694ba` = +3 lines: `source:` / `verified-at:` / `recheck:` frontmatter), documented under `reports/round-8/metadata/` (e.g. `m07-synth-13-24.md`).
- Cross-shard corroboration (landed in parallel in this round): R9-D01 `reports/round-9/d3/check-diagnosis.md` §1–§2 independently reproduces the same 3-file drift, same declared/actual digests, same `exit 2, 3 × D3-SNAPSHOT`; R9-D04 `reports/round-9/d3/replay.md` leg D records the committed freeze as RED for the same three pins and leg E exercises a scratch refresh updating exactly those three digest lines → `exit 0, findings: []` (demonstrated remediation path, not committed). No shard contradicts this finding.

Consequences and notes:

- The failure mode is the designed one (fail-closed, exit 2, no silent pass); the guard's behaviour is correct. What is unmet is the D-claim leg "frozen replay clean", because the pin was never refreshed after round 8.
- Not a fabrication and not a packet contradiction: `packet.json`'s own digests (`assembly.source_sha256`, `references[].file_sha256`) all match actual bytes (see §Evidence below); only the parent-owned snapshot manifest is stale.
- Recommended disposition (parent's call): refresh `expected.json`'s manifest for the three entries as round-9 work and re-run `--frozen`; alternatively keep the refusal and record the D claim's frozen leg as unmet-with-diagnosis. Do not re-scope the frozen check to skip entries.
- The 21 remaining manifest entries match actual bytes, including `examples/culture-d3/packet.json`, `packet.gates.yml`, `controls.json`, the four components, the four round-6 ledgers, `tools/check-evidence-coupling.py`, `tools/assemble-culture-d3.py`, `tools/assemble-d2.py` and `tools/gates/handoff-packet-check.py`. There is no self-digest in the manifest (contract: "not a printed self-blessing checksum"), and `handoff.md`/`README.md` are deliberately absent (contract §`expected.json.coverage`: external presentation evidence checked separately).

## Packet field-by-field results

All rows below: PASS, checked 2026-10-17 by the scratch checker over the delivered bytes. Grouped by contract section; each row names the contract field and the measured value.

### `components` / `assembly` (33 checks)

- Component files are exactly the four contracted paths; each holds exactly its assigned top-level key set (`components/04-language.json` → phonology/lexicon/names/sound_changes/utterances; `05-ritual.json` → beliefs/speech_rules/symbols/naming_rule; `06-material.json` → eras/materials/objects/costumes/rank_rules; `07-evidence.json` → references/bridges/canon_status/handoff_status/scope_notes/screening).
- Packet top level is exactly the union of those 20 keys plus `profile`/`name`/`assembly` (23 keys, no extras, none missing); every merged value equals its component value (no override, no collision).
- `profile` = `kotodama-d3-evidence-coupling/1`; `name` = `D3 source-bounded culture drill (NON-CANON)`.
- `assembly.generator` = `tools/assemble-culture-d3.py` (file exists); `assembly.source_sha256` covers exactly the four components and every digest equals the actual component bytes.
- Deterministic bytes: packet bytes == `json.dumps(doc, sort_keys=True, indent=2)` + final LF (byte-identical under both ensure_ascii variants); final byte is `\n`.
- No absolute filesystem paths: sweep `(?:^|["\s(])/(?:home|Users|tmp|var|opt)/[^\s"]*` over the packet bytes → 0 hits. No ISO timestamps: sweep `\d{4}-\d{2}-\d{2}T\d{2}:\d{2}` → 0 hits. Date-like digit runs audited: all are source locators (e.g. Wayback capture id `20231003011254`, SBE 30/1892 and 1885 in reference `limits`), not generation timestamps.
- Observation (no violation): `assembly` carries `serializer` = `tools/assemble-d2.py (yaml_lines loaded read-only)` and `serializer_sha256` = `8ea6bdde…` (matches actual bytes) in addition to the contracted `{generator, source_sha256}`; the contract's "exactly" wording binds component key sets, and it separately requires the projection trace/limits to live under `assembly`, so the extra informative keys are additive, not contradictory.

### `minimum_counts` (1 check)

- eras 2 ≥ 2; lexicon 20 ≥ 20; names 6 ≥ 6; beliefs 2 ≥ 2; costumes 4 ≥ 4; references 5 ≥ 5; bridges 5 ≥ 5.

### `interface_anchors` (4 checks)

- `native_lexeme_E0`: L01 `pina`, L02 `suma`, L03 `talu`, L17 `nara`, L18 `salu`, L19 `mila`, L20 `kuru` — all exact.
- `material_gate_names`: M01 `felt`, M02 `plant-cloth`, M03 `horn` — all exact.
- `costume_lexemes`: C01→L17, C02→L18, C03→L19, C04→L20 — all exact; and each costume's `native_form` equals that lexeme's form **for the costume's era** (nara/salu/mila/kuru).

### `language` (34 checks)

- phonology: `phonotactics` `(C)V(C)`; `coda_subset` `[n,l,r,s]`; `onset_clusters` false; `p` and `f` both in consonants (union-stage projection); coda subset ⊆ consonants; vowels `[a,i,u]` ASCII lowercase.
- lexicon: exactly L01..L20 in order; fields exactly `{id,native_form,gloss,status,available_from,forms}`; every `status` `constructed`; every `available_from` in {E0,E1}; `forms` keys exactly {E0,E1}; `native_form` == `forms.E0` for all 20; initial-p forms L01/L04/L05/L06 = 4 ≥ 3; unchanged forms (E0==E1) = 16 ≥ 3 (L02,L03,L07–L20); all 40 forms match `^[a-z]+$` and syllabify under the declared profile (faithful re-implementation of `tools/check-evidence-coupling.py:573-599`, verified by probes `suma/puka/ami/kalti/falulura/masin` accept, `tana!/pkla/str` reject); every E1 form == SC1(E0) with SC1 = initial p→f applied once (L01 pina→fina, L04 palu→falu, L05 pira→fira, L06 puka→fuka, all others unchanged).
- sound_changes: exactly one rule, and it is exactly `{id:SC1, from:p, to:f, environment:initial, from_era:E0, to_era:E1, register:ordinary}`.
- names: exactly N01..N06; fields exactly `{id,native_form,display_label,type,era,formation{bases,operation,expected}}`; all era E1; bases are exactly two existing lexeme ids with `operation` `concat`; concat of the **E1** base forms equals `native_form` for all six (N01 sumatalu, N02 kilanisu, N03 falulura, N04 rumafira, N05 amikuru, N06 fukasina); `expected` == `native_form`; all six syllabify and are ASCII lowercase; mutually distinct; none equals any lexeme form; display labels are English explanatory strings, never native-name claims.
- utterances: 7 ≥ 4; fields exact; all era E1; U01 ordinary/market/L01, U02 ritual/hall/L01, U03 ordinary/L03, U04 ritual/L03 as contracted; every `written_form` == the lexeme's E0 form; every `spoken_form` follows the declared law (ordinary → E1 form; ritual → E0 form; only the exactly matching AV1 case L01+hall+ritual substitutes L02's E0 form `suma`); no generalized taboo — U07 (L01, hall, **ordinary**) reads `fina`, the E1 form.

### `ritual` (12 checks)

- speech_rules: exactly AV1 and exactly the contracted field values (`L01`/`E1`/`ritual`/`hall`/`L02`/`constructed-rule`).
- beliefs: exactly B01/B02; fields exact; both `claim_kind` `attributed-belief`, `truth_status` `unresolved`, era E1, distinct propositions, nonempty attributed speakers — two disagreeing fictional accounts, no narrator-certified supernatural fact.
- symbols: exactly SY01/SY02; fields exact; audience nonempty; both readings explicitly deny meaning outside the hall/era and assign no colour or universal meaning key; era E1; `claim_kind` `constructed-rule`.
- naming_rule: NR1 exactly `{allowed_offsets:[2,8,20], unit:fictional-nights, chosen_offset:8, status:constructed-not-historical, source_id:S03}`; chosen offset is in the unique integer set and is not a bool; no claim that Gobhila prescribed these numbers (BR03 `limits`/`mechanism` state the deliberate difference).

### `material` (19 checks)

- eras: exactly E0 (ordinal 0) and E1 (ordinal 1), both with display labels that declare fictional relative coordinates, not CE/BCE.
- materials: M01 `felt`, local-production, available E0; M02 `plant-cloth`, import, available E1 and **no E0 route** (its only route is `kind:import, stage:cloth, eras:[E1]`); M03 `horn`, local-production, available E0, route local/trim/[E0,E1]; fields and route shapes exact; compositions declare invented materials with no species claim.
- objects: exactly O01..O04 with display labels; O01 is `ground-surface`/M01/`worn:false`; O02 `garment`/M01/true; O03 `garment`/M02/true; O04 `worn-attachment`/M03/true.
- costumes: exactly C01..C04 with all 11 contract fields; matrix verified cell by cell — C01 O02/M01/E0/worker/work/workshop/lawful/local-production/nara; C02 O02/M01/E1/worker/work/workshop/lawful/local-production/salu; C03 O03/M02/E1/visitor/assembly/hall/**violation**/import/mila; C04 O04/M03/E1/appointed/assembly/hall/lawful/local-production/kuru; every costume's `material_id` equals its object's material; no ground-surface object is a costume target; availability agrees with the material's declared route eras; display labels are translated.
- rank_rules: RR1 exactly as contracted — invented hall authority, jurisdiction `hall`, eras `[E1]`, rites `[assembly]`, effect `prohibit`, `property {kind:material, value:plant-cloth}` == M02 `gate_name`, `wearer_ranks [visitor]`, `exempt_ranks []`; C03 keeps its declared violation (not repaired lawful).

### `evidence` (23 checks)

- references: exactly S01..S05; fields exact; `ledger_path`/`audit_id`/`support_scope` equal the closed `source_bindings` for all five; every `file_sha256` equals the actual closed-path bytes and the round-7 `baseline.json` reference hashes (05 `a00a5dc4…`, 03 `adb22c9a…`, 13 `69504356…`, 09 `0dd2820d…`); `support_scope` and `source_kind` equal the **effective** round-6 reconciliation row, not the raw worker label — notably S01 uses `secondary-scholarly` (raw ledger `05.json` had `repository-scholarship`; effective row `R6-05-A` is `secondary-scholarly`), and S03's `source_url` is the parent-pinned capture `https://web.archive.org/web/20231003011254/https://sacred-texts.com/hin/sbe30/sbe30020.htm` (raw ledger URL was the unpinned `/web/2023/` form; `R6-13-A.effective_source_url` and spotcheck P03 pin the exact capture); S02/S04/S05 URLs equal spotchecks P02/P01/P05 respectively; all `limits` nonempty; S01/S05 stay `partial-support`.
- bridges: exactly BR01..BR05; fields exact; all `asserted_scope` `design-only`, `claim_kind` `constructed-rule`, relations in {method-transfer, analogy}; pairings exactly BR01 S01→U01,U02; BR02 S02→C01,C02; BR03 S03→NR1; BR04 S04→O01,O04; BR05 S05→SY01,B01; every target id exists as a D3 record.
- no duplicate record ids across all sections (sweep over all 63 record ids: 20 lexicon + 6 names + 7 utterances + 2 beliefs + 2 symbols + 4 objects + 4 costumes + 3 materials + 2 eras + 5 references + 5 bridges + AV1 + NR1 + RR1, all distinct).
- canon_status `NON-CANON`; handoff_status `prepared-not-accepted`; screening `{status:unresolved, real_language_sweep_performed:false, limits:nonempty}`; scope_notes (5 entries) cover invented genealogy, cultural-permission limit, no lore receipt, and unresolved historical/corpus residuals (including open rows R6-05-B, R6-09-B).

### Contract fields outside the packet (bounded surface check; deep checks owned by other round-9 shards)

- `outputs`: all five contracted outputs exist (`packet.json`, `packet.gates.yml`, `controls.json`, `expected.json`, `handoff.md`).
- `controls_format`: `controls.json` has exactly `{profile, positive:3, domain:16, malformed:4}`; all 14 non-DATA diagnostics have at least one domain negative (D3-SCOPE and D3-TIMING twice each); malformed kinds are exactly the four contracted kinds; every entry carries `name`/`patches`/`expected_exit`/`expected_ids` with `replace` JSON-pointer patches; the three positive controls are the contracted clean classes (translated costume label, ordinary unaffected context, attributed-belief reword). All 30 selftest cases pass (see §Reproduce).
- `guard_cli`: JSON stdout shape `{profile, exit, findings:[{id,record_id,message}], counts}` observed on the real run; exits 0/1/2 semantics exercised by the selftest (5 frozen cases include tampered digest → exit 2). Static sweep of `tools/check-evidence-coupling.py` found no network client and no `eval`/`os.system`/shell interpolation; the only `subprocess` use is the selftest's own re-invocation (`run_subprocess`, line 1663), and all `open(...,'w')` calls are inside the selftest scratch path (lines 1728–1915) — consistent with "no input/report writes at normal run".
- `legacy_projection`: surface-verified only (deep projection validation is R9-D01/D08 work) — `assemble-culture-d3.py --check` reports byte-identical `packet.gates.yml`; the file carries `derivation_rules` (six per-name concat replays per its own limits note), `cross_culture_review.languages` empty with the unresolved real-language sweep note and the CROSS-HOLD expectation, and the explicit C03 violation-retention note.
- `handoff_requirements`: surface-verified only (deep acceptance is R9-D12) — `handoff.md` declares NON-CANON / not canonized / `prepared-not-accepted` and no lore receipt.
- `assembly --check` exit codes: the equal case verified (exit 0, byte-identical). Drift (exit 1) and error (exit 2) cases were **not** exercised by this shard (assigned to R9-D01/D02/D05); no claim is made about them here.

## Observations (no contract violation found)

- OBS-1 (F-1 alternative reading): if the parent judges that the D3 frozen expectation should track the post-round-8 tree, refreshing the three manifest digests is the only change needed; the guard needs no change and none was made by this shard.
- OBS-2: `expected.json` deliberately excludes its own digest, `handoff.md` and `README.md` from the manifest; this matches the contract's own coverage note, so it is not a gap.
- OBS-3: the packet contains no "screening passed" or clearance language; `screening.status` is `unresolved` everywhere and no real-language/community permission is claimed.

## Limits of this cross-check

- This shard checked the delivered bytes against the contract; it did not re-verify the underlying sources, the historical claims in the reference `limits`, or the round-6 reconciliation rows themselves (those are round-6/round-8 records, read only as the contract's declared bindings).
- The scratch checker re-implements the contract's rules; where its semantics could diverge from the shipped guard (syllabification), the shipped guard was treated as the oracle and the re-implementation was aligned to `tools/check-evidence-coupling.py:573-599` and probe-tested. No finding rests on the scratch checker alone: F-1 is reproduced by the shipped tool.
- The working tree at check time contained in-flight round-9 metadata edits under `corpus/knowledge/civilizations/` (other shards); none of the D3 or round-6 ledger files were modified (`git status` clean for them; ledger hashes still match their pins).

## Reproduce

```
# 1. packet field-by-field sweep (138 checks) — scratch checker, not committed
python3 /dev/shm/d3_crosscheck.py            # TOTAL=138 PASS=138 FAIL=0

# 2. shipped oracles
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json      # exit 0, findings []
python3 tools/assemble-culture-d3.py --check                                  # exit 0, byte-identical
python3 tools/check-evidence-coupling.py --selftest                           # exit 0, selftest_passed true

# 3. the finding
python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json
# exit 2, counts {D3-SNAPSHOT: 3}

# 4. count/hash spot commands used above
python3 -c "import json;p=json.load(open('examples/culture-d3/packet.json'));print({k:len(p[k]) for k in ['eras','lexicon','names','beliefs','costumes','references','bridges']})"
sha256sum corpus/lessons/round-6-sources/{03,05,09,13}.json
git show 57c3ce6:examples/culture-d3/expected.json | python3 -c "import sys,json;print(json.load(sys.stdin)['manifest']['tools/gates/naming-collision-gate.py'])"
```
