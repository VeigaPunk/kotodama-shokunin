# 15 — Implementation review: D3 code/data integration (round 7)

- Reviewer: worker 15 (author-side review; **no promotion authority**, not independent promotion verification).
- Date: 2026-10-17. Baseline: `30caac66a2a382f1c46ba31f0c3c93da62d0762c` (verified ancestor of HEAD via `git merge-base --is-ancestor`).
- Inputs read: `reports/round-7/claims.json`, `reports/round-7/d3-contract.json`, `reports/round-7/targets.json`, `reports/round-7/baseline.json`, `reports/round-7/dispatch-plan.json`, `AGENTS.md`, `PROVINCE.md`, `reports/round-6/parent-reconciliation.json`, `corpus/lessons/round-6-sources/{03,05,09,13}.json`, `corpus/knowledge/synthesis/worldbible-integration-contract.md`, `examples/handoff-packet.sample.md`, `tools/assemble-d2.py`, `tools/check-craft-exercise.py` (all read-only).
- Method: contract-vs-artifact static inspection of every file landed at review time, plus byte/hash verification of the closed source bindings. **No CLI execution evidence exists yet** — both D3 tools are absent — so every verdict below is static; runtime behavior is explicitly unreviewed.

## 1. Presence census at review time (2026-10-17, working tree, none committed yet)

`for p in <paths>; do [ -e "$p" ] && echo PRESENT || echo ABSENT; done` (all paths relative to repo root):

| Artifact | Owner | State |
|---|---|---|
| `tools/check-evidence-coupling.py` | 02 | **ABSENT — UNREVIEWED** |
| `tools/assemble-culture-d3.py` | 03 | **ABSENT — UNREVIEWED** |
| `examples/culture-d3/components/04-language.json` | 04 | PRESENT — reviewed §3.1 |
| `examples/culture-d3/components/05-ritual.json` | 05 | PRESENT — reviewed §3.2 |
| `examples/culture-d3/components/06-material.json` | 06 | PRESENT — reviewed §3.5 (landed mid-review) |
| `examples/culture-d3/components/07-evidence.json` | 07 | PRESENT — reviewed §3.3 |
| `examples/culture-d3/controls.json` | 13 | PRESENT — reviewed §3.4 |
| `examples/culture-d3/packet.json` / `packet.gates.yml` | 03 (generated) | **ABSENT — UNREVIEWED** |
| `examples/culture-d3/expected.json` | parent | **ABSENT — UNREVIEWED** |
| `examples/culture-d3/handoff.md` | 14 | PRESENT — reviewed §3.6 as declared draft (landed mid-review) |
| `examples/culture-d3/README.md` | 14 | PRESENT — reviewed §3.7 (landed mid-review) |
| `reports/round-7/run-validation.py` | parent | **ABSENT — UNREVIEWED** (claims.json `counting_command` target) |

Round-7 source ledgers `corpus/lessons/round-7-sources/` show `10.json`, `11.json`, `12.json` present at review time (`08`/`09` not observed in a listing cut to 3 entries; F-claim review is another worker's scope). Per assignment: **absent files are marked unreviewed, not predicted green.**

## 2. Pre-landing anchor verification (evidence, not predictions)

These are checks I ran against bytes that already exist; they bound what the future code must reproduce.

1. **Closed ledger hashes match `baseline.json` exactly.** `sha256sum` over the four bound ledgers: `05.json` → `a00a5dc4c872de14970899f6736007039c2cda10824f9731d2436bdd519afbdb`, `03.json` → `adb22c9a5f3acee621103c7b9dddeeb1eedba22d9e1d92081e37825b80560cea`, `13.json` → `695043562e7e0caeda6693384baca060009c9e3feb2c108f5e8ea6bfc282d71a`, `09.json` → `0dd2820d1e837b9ab5e503d21f1a891d367d873c9335f9dad80bef3c2da6ac94` — all equal to `reports/round-7/baseline.json:9-13`. Note S03/S04 share one file (13.json); a per-reference digest check on the file path is therefore correct for both.
2. **All five bound audit IDs exist** inside those ledgers: `R6-05-A`+`R6-05-B` in 05.json, `R6-03-A`+`R6-03-B` in 03.json, `R6-13-A`+`R6-13-B` in 13.json, `R6-09-A`+`R6-09-B` in 09.json (extracted via Python walk of each file's `audits` array).
3. **Pinned handoff contract digest verified**: `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` → `50c4c2f25a728e69260b76d42f0d838a398cc4683a6149f74cceeec8fb7268c1`, equal to `baseline.json:15` and to the digest quoted in `examples/handoff-packet.sample.md:21`. `reports/round-6/parent-reconciliation.json` → `1b9b16710ae128185b5f1cdb339e4afd3dd09063b59974128271d23287892162`, equal to `baseline.json:14`.
4. **Effective reconciliation values the packet references must carry** (from `reports/round-6/parent-reconciliation.json` rows, not raw worker labels). Two override traps confirmed in the raw ledgers:
   - **S01/R6-05-A kind trap:** raw audit `source_kind` is `repository-scholarly`; the effective row (line 26) is `secondary-scholarly` with the reasoning recorded in `corroboration_annotations_not_counted` (line 46). A guard that compares against the raw ledger kind will raise a false `D3-SCOPE` contradiction on a correct packet.
   - **S03/R6-13-A URL trap:** raw audit `source_url` is the wildcard `https://web.archive.org/web/2023/...`; the effective row (line 42) pins `https://web.archive.org/web/20231003011254/https://sacred-texts.com/hin/sbe30/sbe30020.htm` via parent spotcheck P03. S05/R6-09-A additionally carries an effective **locator** override (PDF/printed page 9, `parent-reconciliation.json:34`), relevant only to prose, not to the reference tuple.
   - Effective tuple for guard cross-check: S01 = partial-support / secondary-scholarly / UT hitol/20 URL; S02 = scoped-support / museum-object / Louvre ARK URL; S03 = scoped-support / primary-text / pinned-timestamp URL; S04 = scoped-support / primary-text / wisdomlib URL; S05 = partial-support / secondary-scholarly / http (not https) achemenet PDF URL.
5. **Reusable legacy interfaces confirmed**: `tools/assemble-d2.py:72` defines `yaml_lines(value, indent=0)` and `:167` wraps it with a trailing newline — the read-only serializer the assembler is allowed to reuse; local checker idiom (`main(argv)` → `print(json.dumps(...))` → `sys.exit`, `tools/check-craft-exercise.py:624-664`) matches the contract's JSON-stdout/exit-code CLI shape.
6. **The "16 required fields" of the handoff envelope** are enumerated at `worldbible-integration-contract.md:50-63`: packet_id, packet_version, contract_ref, producer, recipient, request_ref, baseline_bible_ref, artifact_manifest, subject_refs, scope, dependency_manifest, claim_ledger, coupling_edges, requested_decisions, validation, open_questions.

## 3. Static review of landed files

### 3.1 `examples/culture-d3/components/04-language.json` — clean on static inspection

- Top-level keys exactly the five assigned (`d3-contract.json` components.04): phonology, lexicon, names, sound_changes, utterances. Exactly 20 lexemes L01–L20, 6 names N01–N06, 1 sound change SC1, 7 utterances U01–U07 (contract minimum is 4).
- Anchors exact (`d3-contract.json` interface_anchors): L01 `pina`, L02 `suma`, L03 `talu`, L17 `nara`, L18 `salu`, L19 `mila`, L20 `kuru` (04-language.json:12,23,34,188,199,210,221).
- SC1 is the single declared law `p→f / initial, E0→E1, ordinary` (04-language.json:305-315). Initial-p forms transformed: L01, L04, L05, L06 (4 ≥ 3); unchanged forms: 16 ≥ 3. Recomputed E1 forms by hand match every `forms.E1` value (e.g. `palu→falu`, `pira→fira`, `puka→fuka`).
- Every lexeme/name/utterance native form tokenizes under `(C)V(C)` with coda ⊆ {n,l,r,s}, no onset clusters, ASCII lowercase only (incl. coda words `masin` ma-sin, `kalti` kal-ti; onsetless `ami` a-mi is licensed by (C)V(C)).
- Name concat recomputation against **E1** base forms all six match: sumatalu (suma+talu), kilanisu (kila+nisu), falulura (**falu**+lura), rumafira (ruma+**fira**), amikuru (ami+kuru), fukasina (**fuka**+sina) — i.e. the derivation uses post-SC1 forms where required, exactly the `D3-DERIVATION` hazard. Names ≠ base lexemes, mutually distinct, all syllabify.
- Utterance register law: U01 ordinary/market L01 spoken `fina` (E1) / written `pina` (E0); U02 ritual/hall L01 spoken `suma` = L02's E0 form via exactly matching AV1; U03/U04 L03 unaffected in both registers; U07 ordinary/**hall** L01 stays `fina` — a built-in positive proving AV1 does not generalize outside its register/place (`d3-contract.json`: "No generalized taboo outside its place/register"). Written forms are E0 spellings throughout.

### 3.2 `examples/culture-d3/components/05-ritual.json` — clean on static inspection

- Keys exactly beliefs/speech_rules/symbols/naming_rule; AV1 fixed record matches contract field-for-field (05-ritual.json:33-42); B01/B02 are attributed (`speaker` populated), disagreeing (cord-record decisive vs spoken-voice decisive), `truth_status:"unresolved"`, no narrator-certified supernatural fact; SY01/SY02 carry nonempty audience + era + explicit no-universal-meaning/no-colour scoping; NR1 = offsets [2,8,20] (unique ints, no bools), chosen 8 ∈ set, unit fictional-nights, status constructed-not-historical, source_id S03 (`d3-contract.json` ritual block).

### 3.3 `examples/culture-d3/components/07-evidence.json` — clean on static inspection; binding table verified byte-level

- Keys exactly the six assigned; references S01–S05 and bridges BR01–BR05 exactly; per-reference all eight contract fields present.
- **Every reference tuple matches the effective reconciliation table in §2.4**, including both override traps: S01 `source_kind:"secondary-scholarly"` (07-evidence.json:77, effective, not the raw repository-scholarly) and S03 pinned-timestamp URL (07-evidence.json:98, not the raw wildcard). All five `file_sha256` values equal the actual bytes I hashed in §2.1. Sibling unresolved audits (R6-05-B) are explicitly fenced out in S01's limits (07-evidence.json:76) — no whole-claim promotion.
- Bridge relations match the contract's fixed table (BR04 `analogy`, rest `method-transfer`); all `asserted_scope:"design-only"`, `claim_kind:"constructed-rule"`; target_ids exactly {U01,U02}/{C01,C02}/NR1/{O01,O04}/{SY01,B01}; each carries mechanism + limits; BR03 explicitly does not adopt Gobhila's 10/100/1-year numbers and BR04 explicitly does not copy the rite.
- canon_status NON-CANON, handoff_status prepared-not-accepted, screening {unresolved, sweep false, nonempty limits}, scope_notes cover invented genealogy / cultural permission / no lore receipt / name sweep / unresolved residuals (07-evidence.json:68-133).

### 3.4 `examples/culture-d3/controls.json` — strong static coverage; two handshake notes for the resume pass

- Coverage: 3 positive cases (translated costume label replace, ordinary utterance place change, belief proposition reword — all contract-required clean classes); **15 domain negatives covering all 14 non-DATA diagnostics** (D3-TIMING twice: offset 9 and bool `true`, matching the contract's reject-bools rule); 4 malformed kinds invalid-json/invalid-utf8/wrong-root/missing-file all expecting exit 2 + `D3-DATA`. Meets "≥12 domain / 4 malformed / ≥2 positive".
- Pointer arithmetic verified against the contract's merged layout: `/lexicon/3`=L04 (initial-p, so forms stay SC1-consistent while gaining the non-profile glyph `!` — isolates NATIVE from DERIVATION), `/names/0`=N01 (native_form and expected patched together to `funalu` — isolates DERIVATION), `/utterances/0`=U01 (spoken E0 in ordinary context), `/objects/0`=O01 (ground surface worn), `/costumes/2`=C03 (era→E0 breaks M02's no-E0-route; claimed_status→lawful trips RANK on the declared RR1 violation), `/references/0`, `/bridges/0`, `/symbols/0`, `/beliefs/0`, `/naming_rule`, `/canon_status` — all land on the intended records given component array order C01..C04 / O01..O04 / N01..N06 / L01..L20 / U01..U07 / BR01..BR05 / S01..S05. The assembler must preserve array order (sorted-key JSON reorders object keys, not arrays) or these indices silently retarget — **checksum this on the resume pass**.
- Handshake note 1 (match semantics): `expected_ids` lists one stable ID per negative, but the contract does not say whether the selftest requires the expected ID to be *the only* finding, *subset*, or *present*. E.g. the D3-NATIVE case could plausibly also surface a second finding in a strict implementation. The guard/selftest must define this deterministically; reviewer will verify whichever semantics worker 02 documents, and that it is not loosened after seeing results.
- Handshake note 2 (raw-vs-effective): the `D3-SCOPE` negative only flips `support_scope`; nothing in controls discriminates a guard that validates against **raw** ledger url/kind instead of the effective reconciliation rows. Such a guard would pass every control yet fail the true positive packet (false `D3-SCOPE` on S01/S03). The selftest drives the positive packet too, so a correct selftest harness catches this — but only if the positive case is actually run in the same selftest, not just asserted. Resume pass must confirm from CLI output, not from intent.

### 3.5 `examples/culture-d3/components/06-material.json` — clean on static inspection (landed mid-review)

- Keys exactly the five assigned: eras, materials, objects, costumes, rank_rules. Eras exactly `[{E0,0},{E1,1}]` with fictional-relative display labels (06-material.json:60-71).
- Materials: M01 `felt` local E0+/cloth route [E0,E1], M02 `plant-cloth` import **E1 only, no E0 route** (06-material.json:90-104), M03 `horn` local E0+/trim route — gate names match the contract anchors exactly; provenance↔route↔`available_from` all agree; no species authenticity claimed.
- Objects: O01 ground-surface `worn:false` (never worn), O02/O03 garments and O04 worn-attachment all `worn:true`, each carrying its matching material (06-material.json:124-153).
- Costumes C01–C04: field sets complete (11 contract fields each); lexeme mapping C01=L17/C02=L18/C03=L19/C04=L20; each `native_form` equals its lexeme's form for the costume era (nara, salu, mila, kuru — all SC1-unchanged, so E0/E1 forms coincide); costume forms distinct from all six names; era↔material route agreement holds in all four rows (C03 E1/M02 against the E1-only route). C03 is `claimed_status:"violation"` at hall/assembly as visitor in imported M02 — the RR1 violation stays declared, not laundered lawful.
- RR1 is exactly in the legacy-gate shape with fictional authority, `property:{kind:"material",value:"plant-cloth"}` (= M02.gate_name), visitor/prohibit/E1/assembly, empty exemptions (06-material.json:154-175).

### 3.6 `examples/culture-d3/handoff.md` — reviewed as a self-declared draft; three freeze obligations

The scribe's draft is honest by construction: it marks itself `0.1.0-draft (unfrozen)`, records **measured** digests only for bytes that existed (all seven verified by me: contract `50c4c2f2…`, four ledgers matching baseline.json, plus A-FORMAT `4e24bd3b…` which I re-hashed and confirmed), writes "**absent at scribe time**" for every D3 byte row, and its validation section states plainly that nothing was executed. All 16 required envelope fields are present (§2.6 list) plus the canon_standing/handoff_status bullets; no lore acceptance, no invented digests, expected holds (CROSS-HOLD, C03 R-01) named as *expected*, not observed. Three items must be reconciled before freeze (parent/worker-14 resume):

1. **Stale draft rows vs landed components** (self-declared, OQ-D3-06): the draft glossary L04–L16 (`naru`, `penu`, `sari`…) and names N01–N06 (`finatalu`, `sumanara`…) are scribe seeds that differ from the actual landed 04-language.json (`palu`, `pira`…; `sumatalu`, `kilanisu`…); scope also says "4 utterances" while the landed component has 7. Requires re-issue as a new packet version with actual rows before freeze.
2. **Bridge-relation mismatch vs the landed evidence component**: handoff bridge-ledger marks BR02/BR03/BR05 `analogy`, but landed 07-evidence.json uses `method-transfer` for BR01/BR02/BR03/BR05 and `analogy` only for BR04 (07-evidence.json:9,22,35,47,60). The contract does not pin per-bridge relations, but handoff and packet must agree at freeze; the component is the authoritative artifact.
3. **Actual digests/counts at freeze**: A-C01..C04, A-PACKET, A-GATES, A-CONTROLS, A-FROZEN rows must be filled from real bytes (and self/README digests recorded by the parent), with the validation section upgraded from "nothing executed" to actual command outputs and holds.

### 3.7 `examples/culture-d3/README.md` — clean on static inspection (landed mid-review)

- NON-CANON framing, no clearance/permission/authenticity claims; commands match the contract's five exactly, with exit semantics explicitly labeled "interface definitions, not observed results" (README.md:68-70) — no pre-announced success.
- Recorded digests (README.md:98-104) match my §2.1/§2.3 measurements byte-for-byte; the S01–S05 binding table carries **effective** scopes/kinds, including S01 `secondary-scholarly` and the S03 pinned-timestamp URL (README.md:112-118) — consistent with 07-evidence.json and the reconciliation rows.
- Expected-holds section states the contract's legacy requirements correctly (CROSS-HOLD exit 1 with no native FAIL, C03 R-01 note exit 1, structural-pass-not-canonized, similarity as recorded review, D3-RANK only on false lawful claims) (README.md:123-145).
- One staleness note for freeze: the "Assembly status" snapshot lists components 04–07 and controls.json under "Awaiting other owners" (README.md:33-48), but all five files have since landed; refresh the presence list when the packet/tools land and the manifest freezes.

## 4. Defect classes actively hunted, nothing found so far (static scope)

Schema handshake (exact key sets/IDs/anchors — verified for the three landed components), native/label separation (no display label reaches a phonotactic surface in 04/05; costumes absent so unreviewable), source binding (hashes/IDs effective-rows verified), era/role (utterance/AV1 law verified; material half absent), canonicalization (no bytes generated yet — determinism of packet/gates/`--check` unreviewable), path/symlink (guard absent; the hazard stands: `ledger_path` is input data, the guard must resolve only the closed binding paths and refuse traversal/symlink escape — I confirmed the closed targets exist and are regular files, `ls -f` style check implicit in `sha256sum` succeeding on the literal paths), malformed-input (guard absent; controls.json defines the four required kinds).

## 5. Explicitly unreviewed / open for the same-identity resume

1. `tools/check-evidence-coupling.py` — absent. Resume must cover: exit codes 0/1/2, JSON stdout shape `{profile,exit,findings,counts}`, digest-before-verdict ordering in `--frozen` mode (D3-SNAPSHOT exit 2 on tamper), no writes at normal run, no network/eval/shell interpolation, symlink/path-escape refusal, traceback-free exit 2 on all four malformed kinds, effective-row (not raw-row) scope/kind/URL comparison, selftest actually executing the CLI in isolated scratch incl. foreign-cwd call.
2. `tools/assemble-culture-d3.py` + `packet.json` + `packet.gates.yml` — absent. Resume must cover: exact-key component merge with fail-closed collision handling, deterministic sorted-key indent-2 UTF-8 + final newline, no timestamps/absolute paths, assembly.source_sha256 correctness, `--check` 0/1/2 semantics, native-only legacy projection (no English garment labels into phonology), six explicit replay rules, retained C03 violation + CROSS-HOLD (exit 1 expected, not cleared), trace mapping.
3. ~~`components/06-material.json`~~ — landed and reviewed (§3.5): no defect found statically; runtime confirmation still requires the assembled packet + guard.
4. `expected.json` (parent) and `run-validation.py` (parent) — absent; expected_exit/finding_ids must stay `0`/`[]` as predeclared, and must not be weakened to fit any observed bug.
5. `handoff.md` — reviewed as declared draft (§3.6); freeze obligations 1–3 there remain open. `README.md` — reviewed clean (§3.7); refresh its stale presence snapshot at freeze.
6. All runtime/CLI verdicts in §3 are **static**; none of the landed files has been executed, and none can be until worker 02's guard lands.

## 6. Verdict

- Landed and statically clean against the contract: 04-language.json, 05-ritual.json, 06-material.json, 07-evidence.json, controls.json (two runtime handshake notes in §3.4), README.md, plus handoff.md as an honest draft carrying three concrete freeze obligations (§3.6).
- Still **UNREVIEWED — absent at review time**: both tools (guard, assembler), packet.json, packet.gates.yml, expected.json, run-validation.py. No green predicted for any of them; every component/controls verdict above is static, none executed.
- No blocking defect found in what exists; the only concrete cross-file inconsistency is the handoff draft's bridge-relation mismatch (§3.6 item 2), which lives in the self-declared draft, not in the authoritative component. Parent can resume worker 15 (same identity) once guard/assembler/packet land, for the final diff/behavior review with actual CLI evidence.

## 7. Resume pass (same identity): actual implementation + CLI evidence, 2026-10-17 later same day

Scope: `tools/check-evidence-coupling.py` (1946 lines, read in full), `tools/assemble-culture-d3.py` (928 lines, read in full), landed `packet.json`/`packet.gates.yml`/updated `controls.json` (now 3 positive / 16 domain / 4 malformed). All CLI evidence gathered read-only or in tool-own temp dirs; my scratch fixtures live only at `reports/supplement-opencode-1/scratch/round7-15/` (results file: `adversarial-results.txt`, plus `out-guard-positive.json`, `out-guard-selftest.json`, `out-naming-real.txt`, `out-costume-real.txt`, `out-assembler-selftest.txt`). Nothing outside my owned review file and ignored scratch was written. Still absent and **UNREVIEWED**: `expected.json`, `reports/round-7/run-validation.py` (re-checked this pass).

### 7.1 Positive path — all real CLI runs

| Command (repo root) | Exit | Observed |
|---|---|---|
| `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json` | 0 | JSON `{"exit":0,"findings":[],"counts":{"total":0}}` — live positive verdict |
| `python3 tools/check-evidence-coupling.py --selftest` | **1** | selftest_passed **false**: positive 5/5, domain **15/16**, malformed 4/4, frozen 3/3 — sole failure is the control conflict in §7.2 |
| `python3 tools/assemble-culture-d3.py --check` | 0 | "byte-identical deterministic assembly" for both outputs; no writes |
| `python3 tools/assemble-culture-d3.py --selftest` | 0 | 84/84 checks passed (fixture CLI, determinism, tamper, 9 fail-closed negatives, collision branch, serializer-absent, real gates on fixture) |
| `python3 tools/gates/naming-collision-gate.py examples/culture-d3/packet.gates.yml` | 1 | CROSS-HOLD ×2 + NAME-NEAR ×1 (see §7.4); no PHON-/DERIV- FAIL |
| `python3 tools/gates/costume-era-consistency-gate.py examples/culture-d3/packet.gates.yml` | 1 | R-01 only — C03 declared violation retained, no false-lawful R-02 |

Packet spot-checks: top-level keys exactly the contract set; counts lexicon 20 / names 6 / utterances 7 / beliefs 2 / symbols 2 / eras 2 / materials 3 / objects 4 / costumes 4 / rank_rules 1 / SC1 1 / references 5 / bridges 5; costume native forms nara/salu/mila/kuru with lexeme anchors L17–L20; C03 `violation`; bytes are canonical (`sort_keys`, indent 2, final newline — recomputed and compared, equal); no `/tmp/`, `/home/` or ISO-timestamp leakage. `packet.gates.yml` carries exactly six `D3-N01..N06-CONCAT` rules, native-only garment/name slots, `cross_culture_review` unresolved sweep, C03 violation retained, and a native-vs-display trace.

### 7.2 P1 BLOCKER — screening fake-clearance control vs guard diagnostic (selftest currently failing)

- `examples/culture-d3/controls.json:103` `domain-D3-SCOPE-screening-sweep-flag-faked` patches `/screening/real_language_sweep_performed` → `true` and expects exit 1 with `D3-SCOPE` (the critic-directed refinement; not to be weakened).
- The guard emits **D3-MYTH** for this mutation: `tools/check-evidence-coupling.py:760-762` (`check_screening`: "real_language_sweep_performed must be exactly false…"), documented as "D3-MYTH … screening claiming clearance" in the module docstring at `:43-44`.
- Measured: `guard --selftest` → `domain:domain-D3-SCOPE-screening-sweep-flag-faked failed: expected diagnostic ids ['D3-SCOPE'] absent (got ['D3-MYTH'])`; direct CLI on my patched copy → `exit=1 ids=['D3-MYTH']`.
- Consequence: the O-claim selftest evidence is red as landed; any acceptance runner invoking the counting command chain will record a failing selftest until resolved.
- Minimum scoped fix (parent decides; author-side, no promotion): in `check_screening` emit `D3-SCOPE` for the two screening-clearance findings (`:756-762`; keep the limits-nonempty finding as-is or align it too) and update the docstring lines `:43-44`. One-function change; no control edit; then `--selftest` should report 16/16. The alternative (retargeting the control's `expected_ids` to D3-MYTH) would contradict the critic directive as relayed and is listed only for completeness. Semantic note for the record: the contract's D3-SCOPE text covers "unread whole-claim promotion", and the guard author deliberately classified clearance claims under D3-MYTH — the conflict is real and needs an owner ruling, but per instructions the control expectation stands and the guard is the repairable side.

### 7.3 P2 — legacy coda wiring: selftest fixture masks a real key mismatch

- The real naming gate reads `phonology.coda` only (`tools/gates/naming-collision-gate.py:733`, `source.get("coda")`; no `coda_subset` fallback — grep confirmed).
- The contract/D3 component schema uses `coda_subset`, the assembler projects "phonology direct" (`packet.gates.yml` carries `coda_subset`), so on the **real** projection the gate's coda-subset constraint `[n,l,r,s]` is silently inert (template `(C)V(C)` checking still runs — no PHON-PROFILE HOLD was emitted).
- The assembler's selftest fixture instead declares `"coda"` (`tools/assemble-culture-d3.py:427`), so its "real naming gate" integration check (84/84 green) is exercised with a phonology schema the real data never has — fixture-fidelity defect masking the integration gap.
- Impact today: none on exit codes (naming gate exits 1 via CROSS-HOLD as expected; no native FAIL either way). Risk: a future costume/name form with an illegal coda would pass the legacy gate while the new guard rejects it — divergent verdicts between old and new surfaces.
- Minimum scoped fix (author-side): change the fixture phonology key to `coda_subset` (one line, `:427`) so the selftest demonstrates the real schema — the naming-gate checks there only assert CROSS-HOLD/no-PHON-FAIL and would still pass. Whether to additionally map `coda` in `build_legacy` (would change committed legacy bytes → `--check` drift → parent-coordinated regeneration) is a parent decision; contract wording "phonology direct" makes the current projection itself compliant, so I do not flag the projection as a defect.

### 7.4 P3 observations (recorded, no action required for this round)

- Real naming-gate run emits `NAME-NEAR: REVIEW — entities era#1 and era#2 are 1 edit apart ('E0' vs 'E1')… recall-oriented retrieval, not a confusion verdict`: the pre-existing gate compares era ids as name-like entities. REVIEW-class, not FAIL; the README "Expected holds" section names CROSS-HOLD/R-01 but not NAME-NEAR — the parent's acceptance report should record it as a recorded similarity review so it is not mistaken for a regression.
- The guard tolerates unknown extra top-level packet keys (my `zz_unknown_extra` probe → exit 0). The contract's exact-key rule is an assembler-side rule (enforced there with fail-closed behavior); noting the leniency only.
- `spoken_form:"FINA"` yields both `D3-NATIVE` and `D3-UTTERANCE` — acceptable under the selftest's subset semantics.
- Handshake notes from §3.4 are now settled by behavior: `expected_ids` is enforced as a deterministic subset check (`check-evidence-coupling.py:1696-1701`), and the guard compares against the **effective** reconciliation values embedded at `:110-146` (S01 `secondary-scholarly`, S03 pinned-timestamp URL — both traps handled; `full-support` and valid-enum-but-wrong `scoped-support` both correctly raise `D3-SCOPE`).

### 7.5 Adversarial battery — 18/18 expected behaviors (my scratch, raw results in `adversarial-results.txt`)

| Probe | Observed |
|---|---|
| 50k-deep nested JSON packet (raw-text built) | exit 2 `D3-DATA`, no traceback (RecursionError caught at `:274`) |
| packet path is a directory | exit 2 `D3-DATA`, clean JSON |
| frozen manifest key = repo-internal **symlink** resolving outside root | exit 2 `D3-SNAPSHOT` (safe-path containment `:1443-1455` works) |
| frozen manifest key `../../etc/passwd` / absolute `/etc/passwd` | exit 2 `D3-SNAPSHOT` each |
| `--frozen` missing file / invalid JSON | exit 2 `D3-SNAPSHOT`, clean |
| frozen manifest with tampered packet digest | exit 2 `D3-SNAPSHOT` **before** any verdict (digest-first ordering verified) |
| frozen full good manifest (packet + 4 components + 4 ledgers, real digests) | exit 0, clean |
| packet `ledger_path` traversal string `../../../../etc/passwd` | `D3-SCOPE` only; the declared path is never opened — reads go exclusively to the embedded closed bindings (`:1333-1343`) |
| `lexicon[0].forms.E0 = 123` | exit 2 `D3-DATA` boundary rejection |
| costume `display_label` set to native-looking text | exit 0 — translated labels never phonotactically tested ✓ |
| `screening.real_language_sweep_performed=true` | `D3-MYTH` — the §7.2 conflict |
| S01 `support_scope` → `scoped-support` / `full-support` | `D3-SCOPE` both — critic refinement 1 satisfied by the guard |
| unknown extra top-level key | exit 0 (§7.4) |
| normal-run write check (mtime+digest of packet before/after) | unchanged — no writes at normal run proven |

### 7.6 Resume verdict

- Positive path, frozen-snapshot ordering, malformed/boundary handling, path/symlink containment, native-only projection and source binding all verified against the **actual implementation** with real CLI runs: no defect found there.
- Exactly one blocking item: the §7.2 controls/guard diagnostic conflict, which leaves `--selftest` red as landed. One P2 fixture-fidelity item (§7.3) and three P3 notes (§7.4).
- Still unreviewed (absent): `expected.json`, `reports/round-7/run-validation.py` — parent creates them; frozen-mode acceptance flow beyond my scratch manifest stays unreviewed until then.

## 8. Third pass (same identity): fixed guard 849494b0 / assembler ba8d19d5 / packet bdf635ce / projection 306bcac7, 2026-10-17

Exact hashes tested this pass (`sha256sum`, repo root): `tools/check-evidence-coupling.py` = `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e`, `tools/assemble-culture-d3.py` = `ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014`, `examples/culture-d3/packet.json` = `bdf635ceaed4eb2f43ed68418aea968dc930b572bfa61b709372efe89baf4829`, `examples/culture-d3/packet.gates.yml` = `306bcac7b920840ae26f544afcf39a1f09666d6a8c5e786a5089e89af4c70425`, plus `examples/culture-d3/expected.json` = `74496aa8aa7db2d7b2d69ecbd7a5a6acf3d4f565f600fd74bfeab5480adf5080` and `examples/culture-d3/controls.json` = `f00ccf7aac931fb23719e4c3715f0e987c924fc79d7f9881236567d260d2ae70` — the four stated values all match. Per instruction I did **not** review the in-progress `reports/round7/run-validation.py` (reserved for critic 503) or the volatile `handoff.md`/`README.md` prose (agent 501 finalizing); scope here is code/packet/manifest/controls only. Scratch results: `adversarial-results-r3.txt`.

### 8.1 Prior P1 resolution — screening fake-clearance now `D3-SCOPE` (verified)

`check_screening` now emits `D3-SCOPE` for all three screening findings (`tools/check-evidence-coupling.py:760,765,769`). Direct probe on my patched copy (`real_language_sweep_performed`→`true`): `exit=1 ids=['D3-SCOPE']` (was `D3-MYTH`). Selftest domain counter went 15/16 → **16/16**; the control `domain-D3-SCOPE-screening-sweep-flag-faked` passes unmodified. P1 closed.

### 8.2 Prior P2 resolution — fixture `coda_subset` + explicit legacy `coda` adapter (verified, with behavioral proof)

- Fixture phonology now uses the real component key `"coda_subset"` (`tools/assemble-culture-d3.py:436`), and the selftest asserts the projected `phonology.coda == ["n","l","r","s"]` (`:727`).
- `build_legacy` explicitly projects the component's `coda_subset` under the legacy gate key `coda` alongside the original (`:348-354`), with the adapter disclosed in `PROJECTION_LIMITS` (`:120-122`) and present in the real `packet.gates.yml` (keys `coda_subset` at :19 and `coda` at :25).
- Behavioral proof the gate now enforces codas on real-schema data: I copied the real projection to my scratch, mutated C01's `garment: "nara"` → `"pinat"` (coda /t/, illegal under the subset but legal under the bare `(C)V(C)` template), and ran the real naming gate read-only on the copy: **`PHON-CODA: FAIL — 'pinat' cannot be syllabified: /t/ cannot close the preceding syllable: declared coda set {l, n, r, s}`** (exit 1). On the untouched real projection the gate is silent on PHON (holds remain CROSS-HOLD ×2 + NAME-NEAR ×1, costume gate R-01 ×1). P2 closed; the §7.3 residual gap is eliminated.

### 8.3 New strict-bool frozen `expected_exit` (verified)

`load_expected` now requires `type(expected_exit) is not int` → reject (`:1440-1443`; docstring `:69` "strict integer; booleans rejected"). Direct probes with a full parent-derived manifest: `expected_exit: true` → exit 2 `D3-SNAPSHOT`; `false` → exit 2 `D3-SNAPSHOT`; `"0"` (string) → exit 2 `D3-SNAPSHOT`. Previously `true` would have compared equal to 1 and passed; the bool-typing hole is closed, and the selftest carries dedicated `frozen-bool-expected-exit-false` / `-true` cases.

### 8.4 Parent-owned `expected.json` — manifest coverage and digest verification (all pass)

All 24 declared digests recomputed against actual bytes: **24/24 match, zero mismatches**. Coverage as declared: packet + projection, four components, controls.json, both new tools, serializer `assemble-d2.py`, three legacy gates, four round-6 ledger files (five bindings), worldbible contract, reconciliation, round-7 declarations (baseline/claims/d3-contract/targets), handoff sample. The guard's own hash is in the manifest, so any post-freeze guard edit breaks the snapshot — good tamper coupling. Frozen CLI with the parent file measured by me: `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json` → **exit 0, findings []** (matches the parent's measurement). Disclosures, no scope expansion: (a) `expected.json` carries extra metadata keys (`coverage`, `declared_expectation`, `limits`) that `load_expected` does not validate — they are parent-declared prose, ignored by code, harmless; (b) `handoff.md`/`README.md` are deliberately not manifest-covered while volatile — the snapshot must be re-issued after the prose freeze, as its own `limits` field states; (c) `expected.json` does not self-digest (stated in its `coverage`).

### 8.5 Symlink/path semantics — corrected probes (two corrections to my own §7.5)

- **Correction 1 (my r2 claim was unproven):** my earlier "symlink-escape containment works" probe was flawed — its symlink target was actually *inside* my in-repo scratch, and its single-key manifest failed on packet-coverage, not containment. Containment is now genuinely proven: a repo-internal symlink key resolving to a real `/tmp` target, with the outside file's correct digest in a full 24-entry manifest, is rejected **before any read**: `D3-SNAPSHOT "manifest path … is not a safe repository-relative path"` (`safe_repo_path` realpath containment, `:1450-1462` region). Digest match does not smuggle an outside path in.
- **Correction 2 (r3 in-repo probe misread):** the rejected r3 in-repo-symlink case failed on packet-coverage (my single-key manifest), not symlink semantics. Corrected full-manifest probes establish the actual semantics: (a) a manifest key through an **in-repo symlink is accepted as an alias** — the digest binds the resolved **target's** bytes, and swapping the target after manifest creation flips frozen mode to `D3-SNAPSHOT` digest-mismatch (tamper evidence travels through the alias); (b) only keys resolving outside `REPO_ROOT` are refused. Two manifest keys aliasing one realpath collide benignly in the guard's resolution map (only packet coverage is asserted). These semantics are disclosed here; they are reasonable and I do not treat them as defects.

### 8.6 Counters and commands measured this pass (all repo-root)

| Command | Result |
|---|---|
| `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json` | exit 0, `findings: []` |
| `… packet.json --frozen examples/culture-d3/expected.json` | exit 0, `findings: []` |
| `python3 tools/check-evidence-coupling.py --selftest` | exit 0, `selftest_passed: true` — positive **5/5** (`positive-repo-cwd`, `positive-foreign-cwd`, + 3 controls), domain **16/16**, malformed **4/4**, frozen **5/5** (`frozen-good`, `frozen-tampered-digest`, `frozen-unknown-manifest-entry`, `frozen-bool-expected-exit-false`, `frozen-bool-expected-exit-true`) |
| `python3 tools/assemble-culture-d3.py --check` | exit 0, byte-identical both outputs (determinism holds over the new bytes) |
| `python3 tools/gates/naming-collision-gate.py examples/culture-d3/packet.gates.yml` | exit 1 — CROSS-HOLD ×2, NAME-NEAR ×1 (era-id REVIEW, §7.4), no PHON/DERIV |
| `python3 tools/gates/costume-era-consistency-gate.py examples/culture-d3/packet.gates.yml` | exit 1 — R-01 ×1 only |
| Regression battery (17 probes, `adversarial-results-r3.txt`) | deep-nesting, directory-as-packet, traversal/absolute manifest keys, missing/bad frozen file, tampered digest, `form-int`, `spoken-upper` → all unchanged correct; `screening-true` → `D3-SCOPE` (new); `label-nativeish` → clean; no-write re-proven (mtime+digest) |

### 8.7 Verdict of this pass

- Both prior findings (P1 screening diagnostic, P2 coda wiring) are **resolved and verified against the stated hashes**, with behavioral (not just static) evidence; the strict-bool frozen fix is verified; the parent manifest is byte-accurate with declared coverage.
- **No new blocker found** in code, packet, manifest, or controls within my tested scope. No universal malformed-input assurance is claimed — my probes are exactly the set listed in §7.5/§8.6 and nothing more.
- Corrections to my own earlier pass are recorded in §8.5 (r2 containment claim unproven-at-the-time, now proven; r3 in-repo symlink probe misread, semantics now correctly disclosed).
- Open items outside this pass by instruction: `run-validation.py` (agent 490, critic 503 to review), `handoff.md`/`README.md` prose freeze (agent 501; expected.json re-issue afterwards is the parent's stated plan), and all §3.6 freeze obligations. Author-side advice only; no admission or promotion decision made or implied.
