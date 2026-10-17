# R8-D01 design spec — `tools/d2-typed-labels.py`

- round: 8 (loop 1, build 1 of 4) · date: 2026-10-17 · shard: R8-D01
- status: NON-CANON design record. This file specifies the tool that shard R8-D02
  owns; it does not write the tool, edit gates, components or the packet, and
  claims no canon standing (`AGENTS.md`; `corpus/knowledge/synthesis/worldbible-integration-contract.md:97`).
- claim under specification: `reports/round-8/claims.json` D —
  "typed translated-label/native-form handling, scoped era/material
  reconciliation, and an executable rank-rule adapter"; counting commands
  `python3 reports/round-8/run-validation.py` and
  `python3 tools/d2-typed-labels.py --selftest`.
- every rule below carries a `path:line` citation. Line numbers were read from
  the working tree on 2026-10-17; the §9 receipt records the sha256 of each
  cited file at spec time, so drift is detectable.

## 0. Purpose, inputs, outputs, non-goals

**Purpose.** D2's round-3 packet is red for three interface reasons that are not
design findings:

1. Ten `PHON-INVENTORY` FAILs: the naming gate reads `costumes[].garment` as a
   sound form and phonotactically tests the English description
   (`tools/gates/naming-collision-gate.py:614-618`, `:1099`, `:1130`;
   `examples/culture-d2/ASSEMBLY.md:94` — "a real missing-native-form/interface
   limitation, not evidence that an English description itself needs D2
   phonology").
2. Ten `G-ERA` holds: costume stage tags E0/E1/E2 cannot be aligned with 09's
   named-era list (`examples/culture-d2/ASSEMBLY.md:85-89`; "E0 spans six named
   eras, so converting every E0 row to one guessed era would manufacture dating
   precision", `:89`).
3. No executable rank-rule consistency: 12's WR/SR/TR/LO records are
   prose-rich and were not translated (`examples/culture-d2/ASSEMBLY.md:123`;
   "There are no executable `rank_rules`; therefore this run **does not
   establish rank-rule consistency**", `:89`).

The tool makes those three seams **typed, scoped and executable** without
inventing native forms, era names, dates, material identities or rule values.

**Inputs (read-only).**

- `examples/culture-d2/components/11-costumes.yml` (costume + costume-facing
  material records; `examples/culture-d2/ASSEMBLY.md:28`)
- `examples/culture-d2/components/10-materials.yml` (material inventory and
  `maps_to` targets; `11-costumes.yml:92`)
- `examples/culture-d2/components/12-rank-rules.yml` (rule records;
  `11-costumes.yml:69-73`)
- `examples/culture-d2/components/09-eras-calendar.yml` (tag space, named eras,
  dates; `11-costumes.yml:56`)
- `examples/culture-d2/components/05-lexicon.yml` (`layers`, `roots`, lexicon
  records; `11-costumes.yml:74-78`)
- optionally the assembled `examples/culture-d2/packet.d2.yml` for `--check`
  cross-verification (its `assembly.source_sha256` map is written by
  `tools/assemble-d2.py:145-149`).

**Outputs.**

- default: one deterministic report to stdout (no file writes);
- `--emit PATH`: the typed-label projection, the reconciliation ledger and the
  adapted rule set as one document, byte-deterministic;
- `--check`: byte-compare against the committed projection without writing
  (`tools/assemble-d2.py:6` — "`--check` compares bytes without writing");
- `--selftest`: fixture tree in scratch, positive and malformed controls.

**Non-goals.** No gate edits (the round-3 gate behaviour and its 20 findings stay
frozen, `examples/culture-d2/ASSEMBLY.md:97`, `:143-145`); no component or
packet mutation; no CE date conversion (`ASSEMBLY.md:125` — "Numeric CE dates
are unavailable"); no canon decision (`AGENTS.md` — "Canon decisions are
lore-shokunin's"); no invented surface forms — the lexicon component owns forms
(`11-costumes.yml:405`, `:418`).

**Exit codes** follow the lane convention (`SKILL.md:132`, 0/1/2;
`examples/culture-d2/ASSEMBLY.md:105` G-DATA exit 2):

| code | meaning |
|---|---|
| 0 | every projected record consistent; no HOLD/FAIL |
| 1 | findings emitted (HOLD or FAIL), report still complete |
| 2 | could-not-evaluate: malformed input, unparsable record, undecidable schema (no traceback) |

## 1. Typed-label schema

### 1.1 Kinds (exactly three, per the round claim)

| `kind` | Meaning for D2 | Sound channel | Precedent |
|---|---|---|---|
| `native-form` | a constructed D2 surface form owned by 05-lexicon | **checked** (the only sound/identity form) | `reports/supplement-opencode-1/22-label-representation.md:118`; `SKILL.md:185` |
| `translated-label` | reader-facing English rendering (the designer's gloss) | never phonotactically tested | `22-label-representation.md:118`; `tools/check-evidence-coupling.py:941-943` ("display_label/gloss/proposition … deliberately never tested") |
| `borrowed-strata` | a surface form that entered D2 through a declared loan layer, adapted by declared substitutions | **checked** (the adapted recipient form is a D2 string) + borrow-ledger checks | `corpus/knowledge/synthesis/loanword-material-dating.md:40` ("Build loanword strata, not a list of exotic-looking words"); `05-lexicon.yml:168-186` |

Grounding for the three-way split: `corpus/knowledge/synthesis/era-language-staging.md:108`
("type every label") with its label-type table `:110-121` — a costume/style
period label "classifies a silhouette, construction, or fashion cluster" and "a
later museum label is not automatically the wearer's garment term" (`:121`);
`:124` requires that an inherited spoken label and "an unchanged written form,
learned rereading, translation, exonym, or official replacement" be tracked
separately. `corpus/knowledge/synthesis/cultural-translation-protocol.md:93`
adds "Keep script, transcription, reading, and proposed meaning distinct".
`corpus/knowledge/synthesis/glossary-registry-format.md:38` fixes the form
object: "native form, phonemic/phonetic IPA, and variants separately; each
supplied form identifies script, representation, and applicable scheme"; `:53`
requires a diplomatic/source transcription to be preserved separately from
normalized display forms.

### 1.2 Label record shape

```yaml
labels:
  - id: GAR-01                     # owning record id (required)
    owner: 11-costumes             # component that owns the referent record (required)
    label_id: LEX-GAR-01           # form slot / lexicon id this label resolves to, or null
    kind: translated-label         # translated-label | native-form | borrowed-strata (required)
    text: "winter valley coat (heavy felted wool; uncombed finish optional)"
    script: Latn                   # required when text is supplied
    representation: english-gloss  # english-gloss | editorial-romanization | native-spelling
    scheme: null                   # romanization scheme id when representation is a romanization
    status: supplied               # supplied | to-verify | absent
    era_ids: [E0]                  # contract tags; unknown is not "all eras" (glossary-registry-format.md:41)
    register: everyday             # scoped usage, not a prestige ladder (glossary-registry-format.md:42)
    evidence: design-choice        # design-choice | attested | invented | to-verify
    source: {component: 11-costumes.yml, field: garment, line: 216}
```

Rules:

- **L1** (required fields): `id, owner, kind, status`; `text` required when
  `status: supplied`; `label_id` required when the owner record carries a form
  slot (`11-costumes.yml:407-416` LEX-GAR-01..10). Missing/ill-typed fields are
  malformed input → exit 2, `D2L-DATA` (precedent: `tools/check-evidence-coupling.py:57`
  "malformed file/UTF-8/JSON/root or nested essential schema (exit 2, no traceback)").
- **L2** (one sound form per record): a record may carry at most one
  `status: supplied` form of kind `native-form`/`borrowed-strata`; two supplied
  sound forms are an identity collision → exit 2, `D2L-DATA`
  (`glossary-registry-format.md:38` — one editorial lemma object, variants
  separate; `22-label-representation.md` rule 3, `:129-130`).
- **L3** (`null` semantics): an absent value carries a field-specific reason in
  `issues`; `null` never means "no form exists in the world"
  (`glossary-registry-format.md:30`).
- **L4** (scope): `era_ids` must be contract tags (E0–E3) or aliased per §2;
  "unknown is not 'all eras/all speakers'" (`glossary-registry-format.md:41`).
- **L5** (form history separate from object history): `text` records the form;
  the referent's material/era history stays on the owning record — "Record
  **form history**, **sense history**, and **object history** separately"
  (`era-language-staging.md:139`); "Version a garment's referent and its social
  reading separately" (`cultural-translation-protocol.md:111`).

### 1.3 Routing rules (fail-closed)

Derived from `reports/supplement-opencode-1/22-label-representation.md:125-135`
(rules 1–5, with controls C0–C5 at `:138-146`) and the frozen-gate analysis in
`examples/culture-d2/ASSEMBLY.md:94`:

- **R1** `native-form` + `status: supplied` ⇒ this text is the only checked
  sound/identity form. (`22-label-representation.md:125`; `SKILL.md:185`
  "Native forms are unscreened; translated display labels do not enter a
  phonotactic test.")
- **R2** `borrowed-strata` + `status: supplied` ⇒ checked as a D2 string **and**
  must pass the borrow-ledger checks B1–B3 (§1.4). A loan is still a recipient
  surface form; its adaptation is a recipient change
  (`loanword-material-dating.md:50-53`).
- **R3** `translated-label` ⇒ never enters a sound test. If the owning record
  supplies no `status: supplied` native/borrowed form, emit
  `D2L-FORM-UNRESOLVED` **HOLD** — never a silent pass
  (`22-label-representation.md:126-128`, control C1/C1b: "the artifact is
  removed without clearing the real gap"; `ASSEMBLY.md:94`: the unresolved
  LEX-GAR slots "are not silently filled or bypassed with `compare_only`").
  `compare_only` is therefore **not** a licensed exemption channel for typed
  labels; a record setting it while unresolved is `D2L-SCOPE` (misuse), not a
  pass (the gate's own `compare_only` skip sits at
  `tools/gates/naming-collision-gate.py:1097-1098`).
- **R4** contradiction (`kind: translated-label` while a supplied
  `native-form`/`borrowed-strata` is present on the same record) ⇒ the native
  bytes govern and remain checked; labelling cannot waive the check
  (`22-label-representation.md:129-130`, control C2).
- **R5** declared sound kind with `status: absent`/`to-verify` ⇒
  `D2L-FORM-UNRESOLVED` HOLD ("a claim without bytes is not a pass",
  `22-label-representation.md:131-132`, control C3).
- **R6** untyped legacy record (no `kind`) ⇒ unchanged channel: its legacy form
  field is still checked; "dropping the typing fields cannot exempt a string"
  (`22-label-representation.md:133-134`, control C4). This keeps the frozen
  round-3/4/5 verdicts reproducible (`ASSEMBLY.md:143-144`).

### 1.4 Borrowed-strata extension

```yaml
    borrow:
      layer_ref: "Salt-road trade layer"      # must name a declared packet layer
      donor: {immediate: "lowland partner stage 1", ultimate: null, carrier: null}
      donor_form: gas
      substitutions: {g: k}                   # applied to donor_form to yield text
      entry_stage: E1
      referent_available_from: E1
      channel: "the salt and dried-meat road over the pass"
      alternative_checks: [loan-retains-donor-innovation]   # from the §3 diagnostic table
```

- **B1** `layer_ref` must resolve to a layer declared in the packet's `layers`
  block (`05-lexicon.yml:168-186`: "Salt-road trade layer", "Lowland script
  layer"); unknown layer ⇒ `D2L-BORROW` FAIL.
- **B2** `donor` must separate **ultimate etymon / immediate donor / carrier**
  (`loanword-material-dating.md:44`: "A Persian-derived word carried by
  Arabic-speaking traders does not establish a Persian-speaking colony").
  For D2 the immediate donor is the reserved lowland partner stage
  (`05-lexicon.yml:169-171`, `:178-180`); an unseparated donor record ⇒
  `D2L-BORROW` HOLD.
- **B3** when `substitutions` are declared, `apply(substitutions, donor_form)`
  must equal `text`; a failed derivation ⇒ `D2L-BORROW` FAIL. Live D2 fixtures:
  - L-26 `kas` ← donor `gas`, "devoiced g to k on entry" (`05-lexicon.yml:562-576`);
    layer substitutions `{bh: p, dh: t, sh: s, g: k}` (`:175`) ⇒ `g→k` yields `kas`.
  - L-27 `per` ← donor `bher`, "simplified bh to p" (`:577-591`; layer substitutions `:184`) ⇒ `bh→p` yields `per`.
- **B4** dating separation: `entry_stage` (when the word entered) and
  `referent_available_from` (when the thing was available) are different facts
  (`05-lexicon.yml:186`: "the script is adapted at the E0/E1 seam … while the
  D2 word for the borrowed mark is staged later, at E2 — naming date and arrival
  date are different facts"; `worldbible-integration-contract.md:118`
  prescribed introduction / first attestation / popular uptake / retrospective
  description need separate dates). `entry_stage` earlier than
  `referent_available_from` ⇒ `D2L-BORROW` FAIL ("Date the sense–referent
  pairing, not merely the word's oldest ancestor", `loanword-material-dating.md:60`).
- **B5** register/domain partition: the borrow record must carry the register
  and domain the layer declares (`loanword-material-dating.md:48`; `05-lexicon.yml:177`
  "trade and administration only — the loan is a record word, not a religion, a
  garment or a second culture"; `:186` "script only").
- **B6** the borrowed form must not be re-labelled as native: `route: loan` vs
  `layer: loan` are different fields and the gate "reads borrowed-ness from
  `layer`, not `route`" (`05-lexicon.yml:36`). The projection must preserve
  `layer` verbatim.

### 1.5 Worked mapping for the ten costume records

Input `11-costumes.yml:214-403`. Every GAR record carries an English `garment`
string, a `form_slot` (LEX-GAR-01..10), and no `native_form`
(`22-label-representation.md` §1 table). The tool must project:

| record | projected `kind` | `text` | `label_id` | `status` | resulting finding |
|---|---|---|---|---|---|
| GAR-01..GAR-10 | `translated-label` | the `garment` string verbatim | `LEX-GAR-0x` | `to-verify` | `D2L-FORM-UNRESOLVED` HOLD ×10 |

This reproduces the round-4 analysis exactly: the ten `PHON-INVENTORY` FAILs are
representation-channel artifacts, and the correct replacement is ten declared
holds (`22-label-representation.md:112-121`), not ten silent passes and not ten
renames (`ASSEMBLY.md:94`). The two costume-field lexemes already landed —
L-34 `mir` (`05-lexicon.yml:680-692`) and L-35 `mirken` (`:693-706`) — are the
only records in this class that can be projected as `native-form`
(`11-costumes.yml:77`).

## 2. Scoped era reconciliation semantics

### 2.1 Tag space and alias discipline

- **E1** the canonical space is E0–E3 (`01-brief.yml:113` CP-07: "Era tags are
  mandatory from the fixed space E0–E3 … Pre-contract components alias their own
  era prefixes in, never silently"; `01-brief.yml:183` alias rule: "each such
  component declares a one-line mapping to the fixed space in its header, and
  assembly records the mapping. No mapping is assumed silently.").
- **E2** tags are broad stages, not era names: E0 covers ER-01..ER-06, E1 is
  ER-07 Marked Count, E2 is ER-08 Two Counts, E3 is ER-09 Still Air (reserved)
  (`09-eras-calendar.yml:20-26`, `:122-125`; `12-rank-rules.yml:7`).
- **E3** mapping is **by slot, never by number**. 10-materials and 08-symbols
  use their own E-numbers whose values do not coincide with the contract's:
  "their E1 = shelter = contract E0. Merge by slot, never by number"
  (`11-costumes.yml:66`, ERX-W; the same warning at `10-materials.yml:21`:
  "the E1-E4 tags here are slot ids for staging only and must be mapped to 09's
  names at integration, never treated as era names in their own right").
- **E4** every non-identity mapping row carries an explicit `status`
  (`confirmed` | `to-verify`) and a `scope` (`slot` | `label`). ERX-1..ERX-4
  are `(to-verify)` and explicitly "slot-level, not label-level"
  (`11-costumes.yml:62-65`); only ERX-0 (identity with 09) and ERX-R
  (round-4 alignment) are confirmed (`:60-61`).
- **E5** a `to-verify` mapping row never silently promotes a claim: any
  availability verdict that depends on it is scoped HOLD, and the row id is
  cited in the finding (`worldbible-integration-contract.md:94` evidence status
  "no automatic promotion").

### 2.2 Reconciliation verdicts

`reconcile(record, era)` returns exactly one of:

| verdict | condition | downstream |
|---|---|---|
| `identity` | era is already a contract tag and the component declares the tag space directly (`11-costumes.yml:56`; `12-rank-rules.yml:7`) | proceed |
| `mapped-confirmed` | an alias row with `status: confirmed` maps the source label to the tag (ERX-0, ERX-R; `11-costumes.yml:60-61`) | proceed, record the row id |
| `mapped-unconfirmed` | a row with `status: to-verify` (ERX-1..4; `11-costumes.yml:62-65`) | scoped HOLD, `D2L-ERA`, row id cited |
| `unmapped` | no row exists for that source label | HOLD, `D2L-ERA` — never identity-by-number (E3) |
| `conflict` | two rows map the same source label to different tags | exit 2, `D2L-DATA` |

Additional rules:

- **E6** no invented granularity: a mapping to tag E0 must not be emitted as a
  named era; the tool may carry the named era only when the source record states
  it (`09-eras-calendar.yml:20-26`; `ASSEMBLY.md:89`, `:125` "Era names, stage
  tags, 08's E1-E4 local labels, and 12's era-1..3 are not treated as
  interchangeable").
- **E7** dates stay in 09's coordinates: half-open `[from, to)` in descent
  coordinates, "D1 = the covenant ascent; the in-world quarter is not
  convertible without convention" (`09-eras-calendar.yml:100-110`); machine
  interchange uses a declared half-open convention and retains uncertain bounds
  (`worldbible-integration-contract.md:117`). The tool emits no CE number and
  no synthesized `era_dates` field (`ASSEMBLY.md:105-107`, `:125`).
- **E8** institutions, language stages, records and costume seams are dated
  independently, not moved as one block (`01-brief.yml:113` CP-07;
  `loanword-material-dating.md:176` "Stage households and institutions
  separately"; `costume-era-consistency-gate.md:122` separate clocks).

### 2.3 Worked example — GAR-04's E1 arrival

GAR-04 (`11-costumes.yml:274-291`) declares `era: E1`, `provenance: import`,
`material: lowland plant-thread cloth`, and states its seam: "Arrives E1 (the
dated import route A-07 requires); forbidden in E0 by construction (CMAT-06
`excluded_eras`, converging with 10-materials' own exclusion in the same slot
under the era mapping)" (`:289`). Reconciliation must:

1. accept E1 as identity (contract tag, `11-costumes.yml:55-56`);
2. resolve the E0 prohibition through CMAT-06 `excluded_eras: ["E0"]`
   (`:171`) — a closed inventory (§3.4), not an unknown;
3. resolve the cross-component convergence via ERX-2 (`:63`), which is
   `(to-verify)` — so the *cross-component* alignment is reported as a scoped
   HOLD while the *within-component* E0 prohibition stays a hard contradiction
   check. This is exactly the split `ASSEMBLY.md:85-89` asks for (G-ERA is a
   dating/interface hold, not a fabricated date).

## 3. Scoped material reconciliation semantics

### 3.1 Slot identity

- **M1** match by slot, never by label: `11-costumes.yml:110-114` — "Mapping is
  by slot, per 10-materials' own instruction ('map by slot id rather than by
  label'), never by label merge. `maps_to` names the 10-materials record where
  one exists; a null map is a reported finding, not a merge."
- **M2** a `maps_to: null` with a `maps_to_note` is a **reported finding**, kept
  in the ledger (`11-costumes.yml:138-139` CMAT-03 pack-ox down;
  `:189-190` CMAT-08 silk). The round-3 packet leaves both open: "the
  integrator must either keep both luxury imports or re-letter GAR-06 to the
  broadcloth (OQ-3)" (`:190`), and `ASSEMBLY.md:123` records that the material
  inventory "is not unioned with 11's costume-facing subset".
- **M3** the union is allowed only on slot identity: `maps_to` values name the
  target record and slot (`:118`, `:128`, `:148`, `:157`, `:167`, `:178`, `:200`).

### 3.2 Route coverage

`coverage(record, era)` returns one of:

| verdict | condition | downstream |
|---|---|---|
| `available` | some route has the era in `routes[].eras` and a kind in `{local, import, reuse, alternative}` (`11-costumes.yml:122-124`, `:172-173`; `10-materials.yml: g ates_interface` splice contract) | proceed |
| `unavailable-by-closure` | the era is in `excluded_eras` (`11-costumes.yml:171`, `:183`) or the material's era map excludes it (`10-materials.yml:74` "closed inventory — every import route is explicitly excluded in this era (not unknown: excluded)") | contradiction if claimed: `D2L-MATERIAL` FAIL |
| `unresolved` | no route states the era | HOLD, `D2L-MATERIAL` — "an unspecified route is HOLD; a route explicitly ruled out is unavailable" (`costume-era-consistency-gate.md:71`) |

- **M4** the closed-inventory rule is a reject, not a missing datum: "If a
  costume from a later component claims the excluded good in that era, the
  finding is a real contradiction (reject), not a missing datum — repair it by
  moving the claim or by amending this file, and log which"
  (`10-materials.yml:591` closed_inventory_rule; same statement at
  `:107-109`).
- **M5** import stage honesty: "cloth arrives as cloth, dye as dye cake, iron as
  stock … D2 never claims the partner's production stages"
  (`10-materials.yml:488`, imported_stage_rule; `costume-era-consistency-gate.md:64`
  MAT-03). A costume claiming a stage its import route does not declare ⇒
  `D2L-MATERIAL`.
- **M6** route kinds/stages are closed enums: `{local, import, reuse,
  alternative, excluded}` × `{fiber, yarn, cloth, garment, dye, trim}`
  (`10-materials.yml:589` enum_conformance); an out-of-enum value is exit 2,
  `D2L-DATA`.
- **M7** dye vocabulary is closed: a costume `dye:` field must use exactly the
  strings of `dye_names_to_use` (`10-materials.yml:573`; "MAT-04 in the gate
  matches them").
- **M8** grade ladders are era-scoped: G3 "requires imported wool combs, so the
  grade is E2 onward" (`10-materials.yml:450-479`, `era_break_note`); a costume
  claiming a grade outside its era list ⇒ `D2L-MATERIAL`. The rank assignment of
  G1–G3 belongs to the rank-rules component, not to the material file
  (`10-materials.yml:473`; `costume_interface.rank_hooks_not_decided_here` `:581`).
- **M9** width bounds are per material/source (`10-materials.yml:574` width_cap;
  `11-costumes.yml:225` GAR-01 panel 1.7 m seamless bounded by CS-03), checked
  against the costume's `panels[].seamless` flag; a seamless panel above the
  declared source width ⇒ `D2L-MATERIAL` (`costume-era-consistency-gate.md:85`
  "Wide unseamed panel" row).

## 4. Rank-rule adapter interface

### 4.1 Normalized rule record

The adapter reads `12-rank-rules.yml` rule records (WR-01..WR-08 at `:199-300`,
TR-01..TR-06 at `:392-469`, plus DEG/AU/JU/EN/SA/LO/BM/SC blocks) and emits:

```yaml
rank_rules:
  - id: WR-02
    authority: "caravan treaty ratified at the winter moot"
    jurisdiction: {raw: "valley fairgrounds and valley road; void at transit and high pasture",
                   places: [fairgrounds, valley-road], bands: []}
    effect: prohibit                      # prohibit | permit | obligate | exempt
    property: {kind: material, value: lowland-plant-cloth,
               slot_ref: CMAT-06}         # resolved slot or null
    wearer_ranks: [registered herd-master]
    exempt_ranks: []
    eras: [E1, E2]                        # from era + era_history, alias-resolved
    era_history_raw: "E1 onward (the treaty is the script's first D2 use)"
    rites: [caravan-fair]
    garment_refs: [GAR-04, GAR-06]
    enforcement: {mechanism: fair-court-register, assay: "...", reality: "...", sanction: "..."}
    adapt_status: executable              # executable | partial | cannot-evaluate
    unresolved: []
    source: {component: 12-rank-rules.yml, record_id: WR-02, line: 212}
```

Grounding: the audit notation is fixed by
`costume-era-consistency-gate.md:97-99` — "Model a rule as **authority ×
jurisdiction × effective interval × wearer category × garment/material/placement
× occasion → obligation, permission, or prohibition**, followed by exemptions and
sanctions" — and the D3 executable precedent is
`tools/check-evidence-coupling.py:469-472` (`rank_rules: {id, authority,
jurisdiction, effect, property:{kind,value}}` + `eras/rites/wearer_ranks/exempt_ranks`
string lists) with its checker at `:1286-1320`.

**Field semantics (normative, resolves the `wearer_ranks` collision).** In this
spec's normalized record, `wearer_ranks` names the class the rule **licenses or
scopes to** (the class the rule is written about), and `exempt_ranks` names a
carve-out; this is the reading the §4.3 worked example depends on (WR-02
licenses a registered herd-master at the fairgrounds ⇒ `not-applies`, no
finding). The executable gate's field of the same name means the opposite: the
class the rule **bites** (`tools/gates/costume-era-consistency-gate.py:923-941`
applies the rule to `wearer_ranks` and skips `exempt_ranks`). A verbatim field
copy therefore **inverts the verdict**. The projection must translate by effect:
for a `prohibit` rule, spec `wearer_ranks` → gate `exempt_ranks`; for a
`permit` rule, spec `wearer_ranks` → gate `wearer_ranks`. This defect and its
fail-before/pass-after control are recorded by shard R8-D04 at
`reports/round-8/depth/shard-rank.md:44` and `:609`; the adapter must ship the
naive-projection control asserting naive = `applies` vs declared = `not-applies`
for GAR-04 while the treaty stranger still yields `applies`.

### 4.2 Adapter rules

- **A1** `era_aliases: {era-1: E0, era-2: E1, era-3: E2}` (`12-rank-rules.yml:5`)
  must be applied and recorded per rule; no silent aliasing (E1 in §2.1;
  `01-brief.yml:183`).
- **A2** `era` is the rule's **initial canonical stage**; `era_history` preserves
  its full interval, renewals and transitions and is carried verbatim
  (`12-rank-rules.yml:7`). `eras[]` is derived from both; a prose-only span
  (e.g. WR-01 "E0 (knot only) -> E1 (renewed in script) -> E2 (grade floors
  frozen, prices left to the fair)", `:206`) yields `adapt_status: partial` with
  the raw string retained, not a guessed interval.
- **A3** property extraction is a **declared table**, not prose inference. The
  table maps `sign_axis` prefixes to kinds and resolves the value to a slot:

  | sign_axis prefix (record) | kind | value source | slot_ref |
  |---|---|---|---|
  | `fiber/material` grade (WR-01 `:200-201`) | `grade` | G1–G3 ladder | `MAT-02` grade_ladder (`10-materials.yml:450-479`) |
  | `fiber/material` imported cloth (WR-02 `:213`) | `material` | `lowland-plant-cloth` | `CMAT-06`/`MAT-05` (`11-costumes.yml:164-174`) |
  | `fiber/material` fossil law (WR-08 `:291`) | `material` | `plant-thread` | `CMAT-06` |
  | `trim/embellishment` (WR-03 `:226`) | `trim` | `hem-cords` | `GAR-03` (`11-costumes.yml:255-273`) |
  | `garment-type/badge` (WR-04 `:239`) | `badge` | `mast-sash` | `GAR-05` (`:293-311`) |
  | `rite/lifecycle` (WR-05 `:252`) | `rite-state` | mourning finish | `GAR-07` |
  | `quantity/occasion` (WR-06 `:265`) | `occasion-exemption` | wedding day | — (exempt path) |
  | `regulated person` (WR-07 `:278`) | `wearer-category` | treaty stranger | `GAR-06` |
  | `claim` / `touch` (TR-02 `:406`, TR-06 `:457`) | `act` | hem-knot / handshake | `GAR-05`/`GAR-03` |

  A `sign_axis` row absent from the table ⇒ `adapt_status: cannot-evaluate`
  with the raw string in `unresolved[]`; the tool must **not** translate prose
  into new rule values (`ASSEMBLY.md:123`: "Rank rules in 12 are prose-rich
  WR/TR/LO records, not executable `rank_rules`; they were **not** translated").
- **A4** verdict semantics are three-valued: `applies` / `not-applies` /
  `cannot-evaluate`. A costume claim is checked only when every binding field of
  the rule resolves; any `cannot-evaluate` field downgrades the verdict rather
  than passing it (`costume-era-consistency-gate.md:114` — "High wealth, legal
  rank unknown | HOLD the permission claim").
- **A5** the guard rejects **only falsely claimed lawful entitlement**: a
  declared violation stays visible and is never repaired into a lawful case
  (`costume-era-consistency-gate.md:106`, `:110-111`; D3 precedent
  `tools/check-evidence-coupling.py:1261-1280`, D3-RANK docstring `:52-53`;
  `examples/culture-d3/packet.gates.yml:445` "C03's declared violation … is
  retained as a violation … never repaired into a lawful case").
- **A6** exemptions resolve before conflict: "Resolve exemptions before
  declaring a conflict: grant, livery, office, ritual role, wedding/festival,
  theatrical performance, foreign envoy, or other **documented** category"
  (`costume-era-consistency-gate.md:104`). WR-06's wedding-day exemption
  (`12-rank-rules.yml:264-276`) and TR-05's storm-lift necessity clause
  (`:443-455`) are the live D2 exemption fixtures.
- **A7** enforcement stays a separate field group (`costume-era-consistency-gate.md:105`;
  `12-rank-rules.yml` `enforcement_reality` on every WR record — e.g. WR-02's
  "the fair court prosecutes strangers and the visibly overdressed, and almost
  never a registered herd-master's spouse" `:220`; the wives problem,
  `11-costumes.yml:444`).
- **A8** unmapped wearer institutions quarantine: WI-2's `rule_ref:
  "(to-verify) DEG slot"` (`11-costumes.yml:102`) and WI-3..WI-7's
  `lexicon_ref: "(to-verify)"` (`:103-107`) must appear in the adapter's
  quarantine table as `cannot-evaluate` — the adapter reports the gap instead of
  filling it (`AGENTS.md` "claims you cannot verify are marked `to-verify`").

### 4.3 Worked example — WR-02 vs GAR-04

WR-02 (`12-rank-rules.yml:212-224`) prohibits lowland-woven cloth except for a
registered herd-master and never above the sell-line. GAR-04
(`11-costumes.yml:274-291`) is worn by "registered herd-master only (WI-3), and
lawful only within the fairgrounds and on the valley road". Adapter output:
`property.kind=material`, `value=lowland-plant-cloth`, `slot_ref=CMAT-06`
(resolved via `maps_to` `11-costumes.yml:167`), `eras=[E1,E2]`,
`jurisdiction.places=[fairgrounds, valley-road]`, `wearer_ranks=[registered
herd-master]`, `adapt_status=executable`. Verdict for GAR-04 at the fairgrounds
in E1: `not-applies` (registered, in jurisdiction) — i.e. no finding. The
counterfactual control (R8-D12/D13): the same coat claimed lawful one step up
the valley road is `applies` ⇒ `D2L-RANK` FAIL, matching the record's own
statute case (`11-costumes.yml:288`; `12-rank-rules.yml:217` "void at transit
and high pasture").

## 5. Determinism, frozen replay, selftest, and CLI

- **D1** the tool is read-only over components, packet and gates; `--check`
  writes nothing (`tools/assemble-d2.py:6`).
- **D2** output is byte-deterministic: sorted keys, LF endings, no timestamps,
  no host paths in the projection body (precedent: `--check` byte comparison,
  `tools/assemble-d2.py:344-347`; packet hash discipline `ASSEMBLY.md:16`).
- **D3** frozen replay must stay clean: `python3 tools/replay-frozen.py
  tools/gates/frozen/round-3/MANIFEST.tsv` replays all seven recorded verdicts
  with matching digests (`ASSEMBLY.md:143-144`; manifest schema
  `tools/replay-frozen.py:8`). The tool must not touch
  `tools/gates/frozen/**`, `examples/culture-d2/packet.d2.yml`, or any gate, so
  the frozen inputs keep their hashes.
- **D4** `--selftest` runs in a scratch tree (fixture CLI pattern,
  `tools/assemble-d2.py:297`, `:322-326`) and must include, at minimum:
  - positive: GAR-01..10 projected as ten `translated-label` HOLDs; L-26/L-27
    borrowed-strata derivations `gas→kas`, `bher→per` pass; WR-02/GAR-04
    fairgrounds case yields no finding; ERX-0 identity passes;
  - negative/malformed (exit 2, `D2L-DATA`): unparsable record, two supplied
    sound forms on one record (L2), out-of-enum route kind (M6), two alias rows
    conflicting (E5 `conflict`), missing required field (L1);
  - negative/finding (exit 1): a `translated-label` with no native form
    (R3 HOLD), a `borrowed-strata` whose substitutions do not derive `text`
    (B3 FAIL), a costume claiming CMAT-06 in E0 (M4 FAIL), a lawful claim
    against WR-02 out of jurisdiction (A5 FAIL), an untyped legacy record whose
    form is still checked (R6).
- **D5** exit 2 diagnostics are stable strings (no tracebacks), following
  `tools/check-evidence-coupling.py:57` and `ASSEMBLY.md:105`.

## 6. Finding ids

| id | class | trigger |
|---|---|---|
| `D2L-DATA` | malformed input / schema | §1.2 L1–L2, §2.2 conflict, §3.2 M6 |
| `D2L-FORM-UNRESOLVED` | typed label with no supplied sound form | §1.3 R3, R5 |
| `D2L-NATIVE` | supplied native form violates the declared profile | §1.3 R1 (delegated to the existing phonology contract; `tools/check-evidence-coupling.py:941-943` precedent) |
| `D2L-BORROW` | borrow ledger defect | §1.4 B1–B5 |
| `D2L-ERA` | era reconciliation HOLD/conflict | §2.2 |
| `D2L-MATERIAL` | coverage contradiction / unresolved route / grade or stage mismatch | §3.2 M4–M9 |
| `D2L-RANK` | falsely claimed lawful entitlement | §4.2 A5 |
| `D2L-SCOPE` | scope misuse (`compare_only` as exemption, untyped promotion, unstated scope) | §1.3 R3, §2.1 E5 |

## 7. Open items (report, do not absorb)

- **OQ-3 material identity** stays open by design: pack-ox down (CMAT-03) and
  silk (CMAT-08) have no `maps_to` target; the tool reports both as
  `D2L-MATERIAL` findings (`11-costumes.yml:138-139`, `:189-190`; `ASSEMBLY.md:123`).
- **ERX-1..ERX-4** remain `(to-verify)` slot-level mappings; the tool may not
  upgrade them (`11-costumes.yml:62-65`).
- **WI-2..WI-7** rule/lexicon slots remain `(to-verify)`
  (`11-costumes.yml:102-107`).
- The **era-seam tension** (12's era-2 register vs 08's E4 script) is a
  recorded handoff, not a tool decision (`10-materials.yml:18`, OH-03 `:657-659`).
- Canon, attribution and real-world rights questions are out of province
  (`PROVINCE.md`; `AGENTS.md`).

## 8. What D02–D05 must reuse verbatim

- The three kinds and their names (`translated-label`, `native-form`,
  `borrowed-strata`) — round claim D, `reports/round-8/claims.json`.
- Routing rules R1–R6 (parser shard R8-D03): §1.3.
- Reconciliation verdicts and slot rules (R8-D05): §2.2, §3.2.
- Adapter record shape, property table, verdict semantics (R8-D04): §4.1–§4.2.
- Finding ids and exit codes: §6, §0.
- Selftest control list (R8-D06..D13): §5 D4.

### 8.1 Landed-shard reconciliation (read at 2026-10-17T~20:20Z)

The shards below landed while this spec was being written; four deltas are
recorded here so integration is deterministic and nothing is silently dropped.
This section is a **note**, not a rewrite: the interfaces above remain the
design authority for the three kinds the round claim names
(`reports/round-8/claims.json` D).

| delta | landed value | spec value | required action |
|---|---|---|---|
| label kinds | `tools/d2-typed-labels.py:85` ships five (`fictional-coordinate`, `descriptive-gloss` added for the era-tag / slot-gloss class flagged at `reports/supplement-opencode-1/22-label-representation.md` §3) | three (round claim) | keep the five as a superset; the three named kinds keep their routing rules R1–R6 unchanged; the two extras must never enter the sound channel |
| finding ids | tool `TL-01`/`TL-02` (`tools/d2-typed-labels.py:342`, `:425`); parser shard `E-LABEL-*`/`W-LABEL-*` (`reports/round-8/depth/shard-parser.md:73-76`); era/material shard `R-MAT-ERA-*` (`reports/round-8/depth/shard-era-material.md:46-47`) | `D2L-*` (§6) | D02 declares one mapping table; ids are names, the classes in §6 are the contract |
| status vocabulary | tool `declared`/`unresolved` (`reports/round-8/depth/skill-table-draft.md:262`) | `supplied`/`to-verify`/`absent` (§1.2) | map by semantics (`supplied`→`declared`, `to-verify`/`absent`→`unresolved`); a `to-verify` form is never emitted as supplied |
| rank projection | shard R8-D04 found the `wearer_ranks` inversion (`reports/round-8/depth/shard-rank.md:44`, `:609`) and translates by effect | §4.1 field-semantics clause (added) | adopt the by-effect projection; ship the naive-vs-declared control |

Live tool state, re-read and re-run directly by this shard (2026-10-17):

- at 20:24Z, `tools/d2-typed-labels.py` sha256
  `623b5b1f2f9f50b3e306975b4107b5f70122e86e7d7b41aeca21bcb5a7979b03`: `by_id`
  is defined (`:1011`) and used (`:1073`), so the `NameError` reported by shard
  R8-D15 at 20:23Z (`reports/round-8/depth/skill-table-draft.md` §7) is not
  present in those bytes;
- at 20:25Z, sha256
  `56c0db1423f2aac154db4b48bc6a958d3e132001fc2a9df28782e834cd8e21fc`
  (mtime 17:25:40 −0300 — the file is being edited concurrently), the command
  `TMPDIR=$(mktemp -d) python3 tools/d2-typed-labels.py --selftest` **exits 1
  with `RecursionError: maximum recursion depth exceeded`** at
  `tools/d2-typed-labels.py:2130` (`rank_rc = selftest_rank_block()`), reproduced
  twice; the current bytes contain the call but no `def selftest_rank_block`
  (grep: only the call site). The D claim's counting command
  `python3 tools/d2-typed-labels.py --selftest` therefore **cannot pass on this
  sha** — an access/run failure receipt, not a design finding;
- at 20:28Z, sha256
  `5d87d34683d63fe56d0f3f214693d52e7affabd4a1f750761424cc509024686c`: the same
  `RecursionError` persists (call now at `:2286`). **Root cause located:**
  `tools/d2-typed-labels.py:2483` sets `selftest_rank_block = selftest`, so the
  call recurses into `selftest` itself. The fix is a real
  `def selftest_rank_block` (the rank shard's own control matrix, per
  `reports/round-8/depth/shard-rank.md`), not an alias to `selftest`.

The tool file is owned by shard R8-D02; this spec records the state and does not
repair it. Re-run `TMPDIR=$(mktemp -d) python3 tools/d2-typed-labels.py --selftest`
after D02's next edit and update this paragraph before the round's acceptance
run. (`/tmp` inode exhaustion is also live on this host: `mktemp -d` without an
explicit `TMPDIR` fails with "No space left on device" — use a TMPDIR outside
`/tmp`.)

## 9. Source ledger and receipts

All paths repository-relative to `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
sha256 read with `sha256sum` on 2026-10-17 (working tree, pre-integration):

| file | sha256 |
|---|---|
| `examples/culture-d2/components/11-costumes.yml` | `b6e2c5c29cc5d68900d6cde5a8487e64f27d85ecb3d2bd7f3f5beb1113483f22` |
| `examples/culture-d2/components/10-materials.yml` | `11a374d3a5b937a49ed10dc3026a1b681332e6081060ff5710e85a28d519865d` |
| `examples/culture-d2/components/12-rank-rules.yml` | `28696a5a70404984fbf1a453f66c9e7618e318ebf93f25bce461fdb7dfcd35a3` |
| `examples/culture-d2/components/09-eras-calendar.yml` | `540a9339627fdcb802a7f59915a3c72e8234fff37c4a771783382af9c863b030` |
| `examples/culture-d2/components/05-lexicon.yml` | `9bdcb8d895be0592047260361c4c12493569e7d38318b3508a5bde314d87abdf` |
| `corpus/knowledge/synthesis/era-language-staging.md` | `226e11049b7361d86c00e81e910a3d5982839e2e787faead0c9e9da4854152da` |
| `corpus/knowledge/synthesis/glossary-registry-format.md` | `043a4e3b9f525f4a9a7ed51e982c515e5ba3e861d4ffc0605987f1ad37caeee3` |
| `corpus/knowledge/synthesis/loanword-material-dating.md` | `bb08d4585033d856aaccb6b3548cfb8ce598ad226db4648d878109b9188e6fd8` |
| `corpus/knowledge/synthesis/costume-language-coupling-table.md` | `caaca840b9cefc1081a28c6424628467e657a6f34a64296e2c3d96d789a7ebde` |
| `corpus/knowledge/synthesis/cultural-translation-protocol.md` | `fb5d705b5f3542123e428626a591516b1d128ab79bad95a7b33a14286319f207` |
| `corpus/knowledge/synthesis/worldbible-integration-contract.md` | `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` |
| `corpus/knowledge/verification/costume-era-consistency-gate.md` | `9a5982cf2aee742ce702ccbffdec717889a3d6c987d9e32628ecd9c0aa761aef` |
| `tools/gates/naming-collision-gate.py` | `8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526` |
| `tools/gates/costume-era-consistency-gate.py` | `6be04578fc219949daf938838793c3413c152a7c4339ff867d32621ea228f8f7` |
| `examples/culture-d2/ASSEMBLY.md` | `531cafacb6a714c6e2ca74dd287a7fda88a8a2c9c7a7b8344edf291bb138a3d1` |
| `reports/supplement-opencode-1/22-label-representation.md` | `5493b3f7a4c8e1b056ca0cdc7112c84e9ce43b6cb89ef47926bc88bdeacb3364` |
| `tools/check-evidence-coupling.py` | `849494b0c4113885223f6d865110cd34ed6bb3aeec8b449d020f7b571eb2197e` |
| `tools/assemble-d2.py` | `8ea6bdde9514ee966fe58cf219d4d0228ecc3b041e30549c68073cc822c8655d` |
| `tools/d2-typed-labels.py` (landed; owned by R8-D02) | sha churned during this shard's run: `13e82857…` (D15's read) → `623b5b1f2f9f50b3e306975b4107b5f70122e86e7d7b41aeca21bcb5a7979b03` (20:24Z) → `56c0db1423f2aac154db4b48bc6a958d3e132001fc2a9df28782e834cd8e21fc` (20:25Z; `--selftest` crashes, see §8.1) |
| `reports/round-8/depth/shard-rank.md` | `e73ea71eae9a7b9a05a477916e0a0c83698fe447508d04d98f98598163fc4432` |
| `reports/round-8/depth/shard-parser.md` | `6d40b43f68ae9f97dea4ebf9d04eb92564c57b204dd13d4faeac388a1885460a` |
| `reports/round-8/depth/shard-era-material.md` | `da92ea83fce29c730c53dcc29f6e31875adcc217d66c78529315a3ebc3de6a60` |
| `reports/round-8/depth/skill-table-draft.md` | `0e9aca3a84ee4da360090ba921bdef9023f38c46dc47d7e7552fc8b0a1dbcac5` |

Reproduction commands used for this spec:

```sh
sha256sum examples/culture-d2/components/11-costumes.yml \
  examples/culture-d2/components/10-materials.yml \
  examples/culture-d2/components/12-rank-rules.yml \
  examples/culture-d2/components/09-eras-calendar.yml \
  examples/culture-d2/components/05-lexicon.yml \
  corpus/knowledge/synthesis/era-language-staging.md \
  corpus/knowledge/synthesis/glossary-registry-format.md \
  corpus/knowledge/synthesis/loanword-material-dating.md \
  corpus/knowledge/synthesis/costume-language-coupling-table.md \
  corpus/knowledge/synthesis/cultural-translation-protocol.md \
  corpus/knowledge/synthesis/worldbible-integration-contract.md \
  corpus/knowledge/verification/costume-era-consistency-gate.md \
  tools/gates/naming-collision-gate.py \
  tools/gates/costume-era-consistency-gate.py \
  tools/check-evidence-coupling.py tools/assemble-d2.py tools/d2-typed-labels.py \
  examples/culture-d2/ASSEMBLY.md \
  reports/supplement-opencode-1/22-label-representation.md
```

Line-reference audit (2026-10-17): every `path:line` in this spec was checked
against the working tree with a targeted `grep -n`/`sed -n` on the cited file;
the audit corrected twelve off-by-a-few references (WR/TR `sign_axis` lines,
`10-materials.yml` `gates_interface` keys, `05-lexicon.yml` layer lines, the
`22-label-representation.md` rule lines, the D3-DATA docstring line and the
D3-RANK guard range). Residual risk: component files may be edited by sibling
shards after this read; the sha256 column above makes any drift detectable.

No web retrieval was used in this shard; every citation is a local `path:line`
read on 2026-10-17. Claims that could not be verified locally are marked
`to-verify` (now only the tool's live selftest state, §8.1). This spec asserts
no canon and no real-world cultural claim; D2 is a declared non-canon design
drill (`examples/culture-d2/components/11-costumes.yml:8`; `ASSEMBLY.md:3`).
