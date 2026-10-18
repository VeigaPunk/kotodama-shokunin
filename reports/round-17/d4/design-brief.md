# R17-D01 — D4 culture design brief: the weigh-court quote register (trader argot)

- **Seat:** R17-D01 (brief designer), round 17, operator loop 2 of 3, build round 1 of 4.
- **Claim:** D (depth) `culture-d4-assembly` — `reports/round-17/claims.json:9-16`.
- **Date:** 2026-10-18. Baseline revision `f30b6f8188937632bbedd0e7b29aeefff6f8b07b`
  (`reports/round-17/claims.json:5`); working-tree HEAD at write time
  `9b49a4a0fca6ceeab917d401945358fdedeb7e11` (R2).
- **Write scope:** this file only (`reports/round-17/d4/design-brief.md`). No commit, no
  push, no filed round 8–16 byte touched. Scratch writes under `.scratch/r17-d01/` only
  (`TMPDIR=$PWD/.scratch` exported; R11–R13).
- **Canon:** NON-CANON engineering design. This is not a canon record, not a lore
  handoff, not accepted by lore-shokunin, and not a culture proposal for any real
  community. No real-language clearance, cultural permission, community consultation,
  or ancient authenticity is claimed, performed, or granted anywhere in it. No
  real-world community, language, or source is named as D4's basis. Era coordinates are
  fixture-relative, not BCE/CE.

This file is the **D4 culture brief, the 12-component registry, the typed-pipeline
exercise spec, and the candidate hold set, all named before any D4 byte exists**. It is
design intent for the other round-17 D4 seats; it implements no component and runs no D4
tool (none exists yet — R12/R13).

---

## 0. Authority, scope, and what this file does not decide

What it is:

1. the culture brief in the Stage-0 sense — `corpus/knowledge/linguistics/conlang-methodology.md:24-36`
   ("the culture brief is a spec, not flavor"), the seven rows of that table filled for D4;
2. the **component registry** (12 components, D2's `01-brief.yml` pattern: a registry that
   fixes the shared contract and writes no component content of its own);
3. the **typed-pipeline exercise spec** — what D4 must exercise that D2 did not (claim D's
   reason to exist: `claims.json:11` "the typed pipeline (rounds 8-16) is exercised only on
   the legacy D2 example");
4. the **candidate hold set**, named pre-implementation, for the freeze authority to
   confirm (claim D: "hold set named pre-implementation in design docs").

What it is not:

- not the D4 packet, not a component file, not an assembler, not a gate;
- not a claim about any real culture, language, register, or script;
- not an absorption of any contested scope. Where a design question belongs to a sibling
  seat or to the parent, it is named as a requirement or an open item (§10), never decided
  here (`AGENTS.md` "reports contested scope instead of absorbing it").

Sibling round-17 seats this file feeds (targets: `reports/round-17/targets.json`
`D-design: 4`, `D-typed: 4`, `D-tests: 8`, `D-neg: 3`, `O-assembler: 4`; the exact
assignment of the other three D-design seats is not visible to this seat, so their
roles below are named by function, not by seat number):

| consumer | what it takes from this file | what it must not take |
|---|---|---|
| D-components (12 seats) | the registry rows §5: component name, packet keys, pipeline duty, spine obligation | the freedom to write component content that contradicts §3–§4 boundary rules |
| D-typed seats | the delta list §6 (routing-row shape, §6 Δ1) and the gate contract §7.3 | the freedom to edit D2's schema, gate, or expected-holds file |
| hold-set seat | the candidate set §7.1 and its freeze rules §7.2 | authority to add a hold class the gate cannot prove (each row names its proving leg) |
| D-neg seats | the required control battery §8 | the right to weaken a control after seeing results |
| O-assembler seats | the artifact contract §9 | the right to change emitted paths silently; §9.1 is the recommended interface |

---

## 1. Inputs read (pinned), and how claims below are evidenced

Every count below carries a command receipt (R-numbers, §11) with its date; every quote
names its file and line; every negative claim carries its sweep. Pins are as-read at
2026-10-18T09:2xZ–06:2x-03:00 on HEAD `9b49a4a` (R2); sibling round-17 workers were
writing concurrently (R14), so a pin that no longer matches is a re-read event.

| path | sha256 (R10) | role here |
|---|---|---|
| `reports/round-17/claims.json` | `3ac1586a6860f5fee18a234ba799cee555d211a1e810f72ec570b2146d7df854` | the D claim D4 must satisfy |
| `reports/round-17/targets.json` | `28ee64378b762de86f6fd7d80d816fe8be78103b11e8193660555cd32c7bf904` | seat arithmetic |
| `examples/culture-d2/components/01-brief.yml` | `ea0d67d0179aba4b118016f32f6cbf0d5e0dde92b1e8468ee6535e5026f2ea19` | the brief pattern, spine, D1 boundary list |
| `examples/culture-d2/expected-holds.json` | `a5dc26d5b495a90e05ce42d4d8b6d08f047359c377e458f9190b1d310d6dde3a` | the hold-set schema D4 reuses |
| `tools/gates/typed-pipeline-gate.py` | `d102fd1dd1bae3cc4c9d0ea33844b2f706a2098707938c82c75ce9fb6368e27d` | the gate whose D4 shape §7.3/§9.4 specifies |
| `tools/assemble-d2-typed.py` | `c7e5a7493601d3312f2eb55185ac4d081139cdaa0e11f67dd69f67250b037071` | the adapter whose routing rows D4 extends |
| `reports/round-8/depth/design-spec.md` | `84e4b4c19b0310f138b5bb53f3e4b3672cdc493fc83b555d912a9630984cc751` | typed-label schema, routing, borrow, rank adapter |
| `SKILL.md` | `e8d238a6377bc4135027c06b4320e3ab7b6937c1276164be986cf670db6d23f8` | lane decision tables §Label typing, §D3 |

Live state of the pipeline D4 must join (all read-only runs, 2026-10-18):

- D2 assembler `--check` exit 0 (R5); D3 assembler `--check` exit 0 (R6);
- D2 typed-pipeline gate default run exit 0, `summary: 16/16 legs passed` (R7);
  `--selftest` exit 0, `selftest: 12/12 checks passed` (R8);
- D2 naming gate over the legacy packet: exit 1 with exactly 10 `PHON-INVENTORY` lines
  (R9) — the representation-artifact class D2's routing removes;
- D2's typed packet carries exactly 10 `typed_channel` routing rows (R4), all one kind.

---

## 2. The culture: D4, the weigh-court quote register

**One line:** a settled grain-and-orchard plain culture whose towns run **weigh-courts**;
brokers there bind prices in a taught **quote register** (the argot) and keep the record
in a **notched-rod ledger**. Working descriptor: "the weigh-court brokers". The packet's
own name ledger will carry constructed names; this brief fixes no name.

Stage-0 rows (the seven obligations of `conlang-methodology.md:26-34`), filled for D4:

| brief row | D4 design obligation (spec, not flavor) |
|---|---|
| habitat/climate | dry inland plain with orchard belts; **no** river/bank/tide/flood setting (D1B-01), **no** highland/vertical transhumance (D2 SEED-01) — the landscape vocabulary is plain, road-less, and season-neutral; direction deixis is toward the weigh-court, not up/down |
| subsistence | grain and orchard produce plus the **weigh-service itself** (storage, tolls, credit-by-tally); measure and goods lexicon density, numeral/classifier morphology; **no** herd economy, **no** salt/dried-meat road (D2 SEED-04) |
| social ranking | court ranks (apprentice → rod-holder → broker → court-master) with **rod-rights**, not pasture rights; rank vocabulary and address forms are the register law's subjects (§3) |
| religion / oath law | no pantheon component: the culture's binding force is the **witnessed quote and the rod-mark**, with attributed sayings kept attributed; oath formulas are **plain-register-only** speech acts; who may attest what is the evidential law of the register contract |
| neighbors / trade history | two declared partner stages — the **western grain towns** (measures lexicon, the E1 script donor) and the **southern broker network** (credit and numeral terms, the carrier of the chained loan); loans are confined to declared layers and domains (`language-contact.md:56-62` band noted, never overriding D4's own history) |
| literacy / writing era | E0 notched rods only; a **ledger script** arrives at the E0/E1 seam adapted from the western towns, its sign values derived from D4's own phonology (**no** alphabet-first premise, D1B-04); the script freezes spellings at E2 |
| era and history | four strata E0–E3 (§5 `09-eras-calendar`); E3 is the **register split** — the quote register becomes a taught, distinct register and the plain doublets start being owed |

Distinctness is a design obligation, not a hope. The contrast table and D4's own
no-import list are §4.

### 2.1 What D4 refuses to be (one line each)

- not D1 ("Retied Houses"): no water setting, no tying/binding/knot-as-obligation imagery
  (D2's own D1B-01/02 boundary rows, `01-brief.yml:95-96`, are adopted by D4 as NB-01/NB-02);
- not D2: no verticality/wind spine, no herds, no pasture rights, no storm law, no felt/wool
  chain, no caravan/fair-court institutions, no tally-*knot* geometry (`01-brief.yml:67-68`,
  `:199` RG-01);
- not D3: not a source-bounded ancient model, no closed source bindings, no hall/temple
  pledge model, no real-language sweep pretense (`examples/culture-d3/README.md:1-14`,
  `SKILL.md:323-346`);
- not a real institution: no historical guild, market, script, or argot is described,
  cited, or approximated; the corpus comparators below are craft questions only.

---

## 3. Spine: COUNT × QUOTE

D2's spine was two axes with a tagging rule (`01-brief.yml:71-74`: SP-01 verticality,
SP-02 wind, SP-03 test). D4's spine is two axes and the same tagging discipline:

- **SP-01 COUNT** — quantity is the culture's public fact: standard measures, weight
  classes, tolls, classifier morphology, the notched-rod ledger, the counting register of
  numerals. Required evidence: measure/goods lexicon fields, numeral-classifier morphology,
  the rod-ledger records, the tariff rules.
- **SP-02 QUOTE** — binding speech is the culture's private fact: the quote register is
  where a price becomes an obligation; a quote is witnessed, rod-marked, and enforceable
  by court record. Required evidence: the register contract (component 06), the quote
  lexicon stratum, oath/saying formulas (component 07), rank rules whose property is a
  speech act (component 12).
- **SP-03 test** — every design record in every component carries `axis:` with one of
  `count | quote | both | neutral-with-rationale`; every component file declares
  `spine_coupling:` naming its two strongest couplings and their record IDs. A record that
  only makes sense through D1 or D2 imagery is a violation, not a neutral record.

Aesthetic stance (what D4 feels like, stated so components can be judged against it):

- **AS-01 "the price is spoken once"** — a quote given in the register is not repeated;
  re-quoting is a new act with a new rod-mark.
- **AS-02 "the record is a rod, not a memory"** — obligations live on notched rods in the
  court; there is no witness formula, no oath-cloth, no public witnessing institution.
- **AS-03 "plain is what is recorded, quote is what is bound"** — the register split is
  inverted against the slang intuition: the plain register is the record/ritual register,
  the argot is the *legal* register of binding speech.
- **AS-04 "measures are the town's face"** — the court's standard weights are public
  monuments; a town is judged by its weights, not its walls.
- **AS-05 "guests quote, hosts record"** — guest-law: a foreign broker may quote (in the
  register, rod-marked) but not keep the court's ledger; that asymmetry is the culture's
  central institution and the source of its rank rules.

---

## 4. Distinctness: the contrast table, D4's no-import list, and the rejected axes

### 4.1 Contrast (each row names its evidence)

| domain | D1 fixture | D2 | D3 | **D4** |
|---|---|---|---|---|
| medium of life | river terrace, bank work | winter valley / summer pasture | hall + market speech, ritual hall | **weigh-court, ledger rod, standard weights** |
| obligation | public witnesses, oath-cloth | lineage pasture rights | spoken pledge, hall invocation | **witnessed quote + rod-mark + court record** |
| record geometry | — (alphabet-first) | tally-knots on a hanging line (`:199`) | record line, boundary token | **notched rod (no knots, no cords, no tokens)** |
| literacy | E1 alphabet with letter IDs | E0 knots; script from lowland partner at E0/E1 seam (`:67`, `:89`) | written/read distinction, script binding | **E0 notched rods; ledger script at E0/E1 seam, sign values from D4 phonology** |
| economy | flax/bast/reed craft | herds: wool, milk, meat; salt trade | model economy (pledges, objects) | **grain/orchard + weigh-service (tolls, storage, credit-by-tally)** |
| prosody/register | penultimate stress; no tone | pitch accent isolate | ordinary vs ritual hall speech (SC1) | **fixed initial stress; no tone; plain vs quote register with a register law** |
| evidence posture | lane fixture | design drill, NON-CANON | source-bounded, closed bindings | **design drill, NON-CANON, zero real-source bindings, comparators in-repo only** |

### 4.2 D4's no-import list (NB-01..NB-08)

Adopted from D2's D1B rows where the ban is a lane-wide hygiene rule, extended for D2/D3:

| id | ban | check |
|---|---|---|
| NB-01 | river/bank/tide/flood as setting, staple, or metaphor (D1B-01) | term lists and record texts of components 05/06/07/10 scanned at review |
| NB-02 | tying/binding/knot-as-obligation imagery; **any** knot/cord record geometry (D1B-02 + D2 RG-01) | components 05/08/09 term lists; D4's geometry is the notch, never the knot |
| NB-03 | bast/flax/reed fiber chain (D1B-03) | component 11 materials and routes |
| NB-04 | alphabet-first literacy; D1 letter IDs (D1B-04) | component 04 script block vs the D1 letter list |
| NB-05 | D1 sound law (/p/→/f/) and penultimate stress; D2 pitch accent (D1B-05 + SEED-05) | components 02 and 09 rule lists |
| NB-06 | D1/D2 fixture forms and names (D1B-06) | collision run at the naming gate, D1/D2 form ledgers as inputs |
| NB-07 | D2 spine vocabulary: verticality/ascent/descent deixis, wind/breath/soul, storm law, herd/pasture terms | components 03/05/06/07 term lists; violations are findings, not resolved by the writer |
| NB-08 | D3 material: hall/temple pledge model, avoidance-register phonology, nights-based prescription, closed source bindings, any real-source URL | components 06/07/09 records; D4 declares zero source bindings |

### 4.3 The three underused axes, and why trader argot is the one

The assignment offered three: seasonal dual-site, trader argot, highland terrace polity.
Rejected, with evidence:

- **Seasonal dual-site — rejected (weakest delta).** D2's spine already carries seasonal
  poles and site-scoped jurisdiction: `01-brief.yml:68` (SEED-07 "seasonal poles") and D2's
  rank rules scope by `jurisdiction.places` = fairgrounds / valley-road / high pasture
  (`reports/round-8/depth/design-spec.md:388-399`, worked case `:488-502`). A dual-site D4
  would re-exercise a jurisdiction dimension the pipeline already carries, adding no new
  typed-routing surface.
- **Highland terrace polity — rejected (adjacency).** It collides with D2's highland spine
  and with a comparator D2 already flagged: `01-brief.yml:130-132` records "Andean
  terrace-agriculture material for a vertical-economy comparison is not yet located as a
  corpus entry in this repo and stays (to-verify)". Building D4 on that axis would walk
  into D2's own deferred comparator and the verticality spine D4 must not import (NB-07).
- **Trader argot — chosen (only axis that adds a new pipeline dimension).** It is the only
  one of the three that forces the typed pipeline into a dimension it has never graded:
  **register as a scope on a supplied, inventory-clean form** — a form that must stay on
  the sound channel while its *slot* is held (§6 Δ1). D2 graded one routing class
  (`translated-label`, R4) and one hold id; the register axis gives D4 a second routing
  class and a second hold id without touching D2's schema or artifacts.

---

## 5. Component registry (12 components)

D2 has 15 component files (R3); D4 declares 12 (claim D: "brief -> 12 components"). D4
drops D2's pantheon, myths-motifs, kin-address, and pragmatics as separate files, adds the
register contract, and merges naming into 12. Each component is written by its own worker
and writes no sibling's content (`01-brief.yml:11-20` scope note, adopted).

| # | file (under `examples/culture-d4/components/`) | packet keys | pipeline duty |
|---|---|---|---|
| 01 | `01-brief.yml` | `assembly`, registry, contract, hold-set declaration | the registry and contract; declares the hold set §7.1 pre-implementation; spine tagging rule SP-03 |
| 02 | `02-phonology.yml` | `phonology` | inventory, syllable profile, fixed initial stress; **law: no register owns a private segment** (a register that adds a segment is a `D4L-NATIVE` finding, never a license); declares the length/diacritic mark §7.1 row 8 rides on |
| 03 | `03-morphosyntax.yml` | `morphology` | agglutinative; numeral classifier + measure-noun morphology; **declares the two argot derivations** `head2` and `reverse` with their exact algorithms (Δ3) |
| 04 | `04-ledger-script.yml` | `script` | E0 notched rods → E1 ledger script (donor stage `west-stage-1`, sign values from 02); the **abbreviation convention** for written quotes (a convention, not a third register with forms); no alphabet-first premise (NB-04) |
| 05 | `05-lexicon.yml` | `lexicon`, `layers` | plain-register base lexicon (goods, measures, ranks, tally operations, sayings anchors); the **quote stratum** and the **argot loans** AL-01..06 with three-field donors (§6 Δ4); each lexeme carries `register: plain|quote` and `era_ids` |
| 06 | `06-register-contract.yml` | `registers`, `doublets` | the register law: registers `plain` and `quote`; slot admissibility; the plain-register-only oath law; the **owed plain doublets** list (Δ1/Δ2); the written-quote convention |
| 07 | `07-oaths-sayings.yml` | `sayings`, `oaths` | attributed sayings (kept attributed — D3's `D3-MYTH` discipline re-exercised); oath formulas (plain-only speech acts); no pantheon, no narrator-certified truth |
| 08 | `08-symbols-tokens.yml` | `symbols` | court marks, rod notches as symbol geometry, stamp shapes; audience-scoped symbols (court-internal vs public) |
| 09 | `09-eras-calendar.yml` | `eras`, `era_records` | E0–E3; the **E3 register split** as a dated event; per-form register-emergence clocks (Δ5); no CE dates synthesized |
| 10 | `10-measures-materials.yml` | `materials`, `measures` | the court's standard weights and sealed measures; goods classes; material routes for costume (local leather, imported plain cloth); the SM-03 unresolved route (§7.1 row 6) |
| 11 | `11-costumes.yml` | `costumes`, `constructions`, `cloth_sources` | trade-sash (imported cloth), court-apron (local leather), guest-robe (guest-law wear), rod-belt; **one declared violation kept visible** (CS-03) |
| 12 | `12-ranks-names.yml` | `rank_rules`, `names` | court ranks; register-law rules whose property kind is `register` or `speech-act` (Δ6); the name ledger (form-bearing; naming-gate input) |

Packet shape: D4's assembler emits one gate-facing packet whose top-level keys are D2's
set (R15: `phonology, morphology, lexicon, layers, names, costumes, materials, eras,
era_records, symbols, motifs→sayings, roles, cloth_sources, constructions, source_era_dates,
assembly, canon`) plus D4's `registers`, `doublets`, `measures`, `oaths`. The typed packet
adds `schema`, `typed_assembly`, `typed_channel`, `pipeline_findings`, `pipeline_counts`
(D2's typed keys, R16).

---

## 6. What D4 must exercise that D2 did not (Δ1–Δ8)

Each delta states the D2 state (with evidence), the D4 requirement, the **measurable
signature** the gate/tests must observe, and the control that proves the mechanism.

### Δ1 — a second routing class: register-scoped slots (the core delta)

- **D2 state:** exactly one routing class. The adapter moves the gloss field of
  `translated-label` records with no native form (`garment` → `garment_gloss`) and writes
  one `typed_channel` row per record with `channel: off-sound-and-identity` and
  `hold: D2L-FORM-UNRESOLVED` (`tools/assemble-d2-typed.py:1-30`; live shape, first row,
  `examples/culture-d2/packet.d2.typed.yml:3324-3334`); exactly 10 such rows exist (R4).
- **D4 requirement:** two routing classes in one packet. Class 1 is D2's (gloss rows,
  `D4L-FORM-UNRESOLVED`). Class 2 is **register rows**: a supplied, inventory-clean quote
  form that is *admissible only in a quote slot*; it **stays on the sound and identity
  channel** (`off_channel_field: null`, `channel: on-sound-and-identity`) while the *plain
  slot it must also fill* stays owed — `hold: D4L-REGISTER-UNRESOLVED`, `owed_slot:
  <slot>#plain`. The new state is **on-channel but slot-inadmissible**: D2 had no such
  state, and the round-8 rule it re-proves is T1's "adding typing fields cannot exempt a
  string" (`SKILL.md:42-47`, `reports/round-8/depth/design-spec.md:146-181` R1/R3/R6) —
  read in the new direction: **a `register` field cannot move a form off the sound channel
  either**.
- **Signature:** in the typed run, every quote form appears in the sound gate's inventory
  exactly as a native form does (same finding class, same field read), while the plain
  slots produce `D4L-REGISTER-UNRESOLVED` hold lines — one per owed slot, never a pass and
  never a note.
- **Controls:** (a) a fixture that sets `off_channel_field` on a quote form (exempting it)
  must FAIL the gate; (b) a fixture that fills a plain slot with the quote form must FAIL
  (`D4L-REGISTER`); (c) a fixture that deletes the routing row while the hold is owed must
  FAIL (the D2 "dropped-row" control class, mirrored by the gate's own selftest, R8).
  Sibling pipeline-level negatives already landed: `reports/round-17/tests/neg-1.md`
  (gloss smuggled onto the sound channel), `neg-2.md` (owed form silently dropped) — D4's
  (a)/(c) are the same mechanisms at the register class.

### Δ2 — slot cardinality: one checked form per (owner, slot)

- **D2 state:** L2 = "a record may carry at most one `status: supplied` form of kind
  `native-form`/`borrowed-strata`" (`reports/round-8/depth/design-spec.md:130-134`).
- **D4 requirement:** a record has a **register pair of slots** (`<id>#plain`,
  `<id>#quote`); each slot is its own label record; the invariant generalizes to **exactly
  one supplied checked form per (owner, slot_ref)**, and the pair relation is carried as a
  packet fact (`doublet_of`). Two supplied forms in one slot remain `D4L-DATA` exit 2.
- **Signature:** the typed projection's coverage block counts slots, not records, and the
  pair count is declared; a pair with one side owed yields exactly one hold, not two.
- **Control:** a fixture with two supplied forms in one slot → exit 2, `D4L-DATA`,
  no traceback (D2's L2 control re-run under the D4 schema).

### Δ3 — derivation-checked forms (a third derivation relation)

- **D2 state:** the only cross-record derivation was the borrow substitution
  `apply(substitutions, donor_form) == text` (B3, `reports/round-8/depth/design-spec.md:205-209`).
- **D4 requirement:** quote forms are **derived** from their plain base by one of two
  declared, fully specified operations — `head2` (first two syllables of the base) for
  measure words, `reverse` (string reversal) for the numeral series — and the derivation is
  checked (`derived_from` + `derivation` fields). This is a relation between two records of
  the same packet, which D2 never graded.
- **Signature:** every derived quote form's check passes in the delivered packet
  (zero fails); the coverage block reports `derived_forms` and `derived_ok` counts that
  agree.
- **Control:** a fixture whose quote form ≠ `apply(op, base)` → FAIL, id `D4L-ARGOT-DERIV`
  (new id, control-only; the delivered packet carries no such row).

### Δ4 — three-field donor separation exercised with a live carrier

- **D2 state:** both live loans have `ultimate: null, carrier: null` — one reserved
  immediate donor (`reports/round-8/depth/design-spec.md:184-194` field shape; the live
  fixtures L-26 `gas→kas`, L-27 `bher→per` at `:206-209`). B2's full three-field separation
  was never exercised.
- **D4 requirement:** at least one loan (AL-02) declares `ultimate`, `immediate`, and
  `carrier` as three distinct non-null facts (ultimate = an old far-side etymon, immediate
  = `west-stage-1`, carrier = the southern broker network), and at least one loan (AL-03)
  is declared with `ultimate: null` — **held**, not failed (B2's hold branch).
- **Signature:** the borrow-ledger leg reports three-field rows as checked, and AL-03's
  hold line names the missing field.
- **Controls:** an unseparated donor record (carrier merged into immediate) → `D4L-BORROW`
  HOLD (not a pass); a loan whose `layer_ref` names no declared layer → `D4L-BORROW` FAIL
  (B1; sibling pipeline-level negative `reports/round-17/tests/neg-3.md` territory); a
  loan with `entry_stage` earlier than `referent_available_from` → FAIL (B4).

### Δ5 — register history as a dated fact (the fourth clock)

- **D2 state:** two clocks existed for loans (`entry_stage` vs `referent_available_from`,
  B4) and era tags on labels with alias discipline (E5, `design-spec.md:248-273`); no
  register ever had an emergence date.
- **D4 requirement:** the quote register emerges at E3; every quote form carries
  `available_from: E3` and the record history keeps form / sense / object / **register**
  histories separate (`cultural-translation-protocol.md:111`; `era-language-staging.md:139`).
- **Signature:** a quote form claimed in a pre-E3 slot FAILS (`D4L-ERA`), and a register
  whose emergence is declared as a prose span yields `adapt_status: partial` with the raw
  string retained — the delivered hold RG-02 (§7.1 row 4).
- **Controls:** quote form dated E2 → FAIL; prose-only span → HOLD with the raw text in
  `unresolved[]`; a CE date synthesized anywhere → malformed (E7, no CE dates).

### Δ6 — a rank-rule property of kind `register` / `speech-act`

- **D2 state:** the adapter's declared property table maps `sign_axis` prefixes to kinds
  grade / material / trim / badge / rite-state / occasion-exemption / wearer-category / act
  (`design-spec.md:441-459`), and an unmapped row becomes `cannot-evaluate`, never a guess.
- **D4 requirement:** the table gains rows for `register` (a rule regulating which register
  a speech act must use: "a plain oath is binding; an oath in the quote register is void")
  and `speech-act` ("a guest's quote binds only with a rod-mark"). A rule whose register
  binding does not resolve is `cannot-evaluate` (A4), never a pass.
- **Signature:** two register-law priority gaps surface as `D4L-RANK` holds (RG-05/RG-07,
  RG-06/RG-09 — §7.1 rows 5), and the one band-keyed pair as a note (RG-08#a|RG-08#b).
- **Controls:** a lawful claim against a register rule out of jurisdiction → FAIL (A5); a
  declared violation kept visible is never repaired into a lawful case (A5, D3's C03
  precedent).

### Δ7 — costume/rank coupling on a different material base

- **D2 state:** costume = herd-fiber chain, felt/weave, rank rights over pasture
  institutions; one declared violation kept visible (R-01 note).
- **D4 requirement:** costume = imported plain cloth + local leather + the rod-belt; rank
  rights over **court ranks and guest-law**, not wealth; one declared violation (CS-03: the
  court-apron worn below the charter's rank floor at E2) kept visible as exactly one R-01
  note; material routes are import/local, with one unresolved route (SM-03) held.
- **Signature:** costume-era gate exits 1 with exactly one R-01 note and no other finding;
  material coverage reports the SM-03 route unresolved as a hold.

### Δ8 — the "no exemption" re-proof in both directions, plus the naming-gate red line

- **D2 state:** typing proved two things: a gloss never enters the sound test (R3) and an
  untyped legacy record's form is still checked (R6).
- **D4 requirement:** the same two proofs hold under the D4 schema, and a third: **register
  is never `compare_only`** — a register-scoped record setting `compare_only` while its
  plain slot is owed is `D4L-SCOPE` misuse, not a skip (`design-spec.md:160-169` R3
  discipline, re-read for register).
- **Signature:** the naming gate over the typed D4 packet shows the CROSS-HOLD row
  unresolved-real-language-sweep ×1 (a red line that must stay visible; `no` clearance is
  claimed anywhere) plus recall-oriented NAME-NEAR rows; zero PHON-INVENTORY lines name a
  gloss-routed record; zero line exempts a quote form.

---

## 7. The hold set, named pre-implementation

### 7.1 Candidate hold set (D01 proposal; freeze by the hold-set seat)

Schema: `kotodama-typed-pipeline-holds-v1` (D2's, `examples/culture-d2/expected-holds.json:2`),
filed as `examples/culture-d4/expected-holds.json`, pinning D4's packet/projection/projector/
adapter digests (D2 pins three; D4 adds the adapter — §9.2). Counts target: **18 holds,
1 note, 0 fails** (D2: 15/1/0, R1).

| # | id | severity | count | where-key shape | trigger (proving leg) |
|---|---|---|---|---|---|
| 1 | `D4L-FORM-UNRESOLVED` | hold | 6 | `GD-01`..`GD-06` | gloss-routed goods/measure slots with no supplied sound form (Δ1 class 1; R3) |
| 2 | `D4L-REGISTER-UNRESOLVED` | hold | 6 | `AL-01#plain`..`AL-06#plain` | argot loans supplied and checked in the quote slot; the plain doublet is owed (Δ1 class 2; the new id) |
| 3 | `D4L-BORROW` | hold | 1 | `AL-03` | donor separation incomplete: `ultimate: null` (B2 hold branch, Δ4) |
| 4 | `D4L-ERA` | hold | 1 | `RG-02` | register-emergence declared as a prose span → partial, raw retained (E5/A2 discipline, Δ5) |
| 5 | `D4L-RANK` | hold | 2 | `RG-05#a\|RG-07#a`; `RG-06#a\|RG-09#a` | register-law genuine-priority-gaps (A5/act-collision class, Δ6) |
| 6 | `D4L-MATERIAL` | hold | 1 | `SM-03` | sealed-measure slot with no resolved route (`maps_to` absent) (Δ7) |
| 7 | `D4L-RANK` | note | 1 | `RG-08#a\|RG-08#b` | band-keyed pair, reported not held (D2's `SR-01#a\|SR-01#b` shape) |
| 8 | `D4L-NATIVE` | hold | 1 | `QN-01` | a quote form carrying the length/diacritic mark declared by 02-phonology's own minimal pair; held for the form's owner, never failed (D2's `L-15`/`L-16` class) |

Row 8 is conditional by construction: it requires 02-phonology to declare a length or
diacritic mark with its own minimal pair. The design intent is that it does — re-exercising
the D2 `D2L-NATIVE` hold class is part of the claim's coverage — and the hold-set seat may
drop the row only by recording the phonology's decision that makes it impossible.

Holds 1–2 are the D4 signature: the packet is red in exactly the two ways the two routing
classes prescribe, and nowhere else. Holds 3–6 are designed open items (owed work), and
hold/note 5/7 mirror D2's rank-hold shape on the new register-law property.

### 7.2 Freeze rules (binding on the hold-set seat)

1. The set is **named here, before implementation** (this file's date). Any later change is
   a recorded amendment naming the component decision that forced it, never a silent edit
   after seeing the gate output.
2. Every row must be provable by a named leg: rows 1–2 by the channel leg (L2), rows 3–6/8
   by their respective projector checks, row 7 by the rank adapter. A row the gate cannot
   prove does not enter the file.
3. Severity is not negotiable downward: a hold is never laundered into a note to make a
   count green (the gate's own L3 discipline, `tools/gates/typed-pipeline-gate.py:24-37`,
   and its "laundered-hold" selftest control, R8).
4. The delivered packet carries **zero fails**: every FAIL class of §6 lives in controls,
   not in the shipped bytes. Exit 0 from the D4 gate is a *structural* pass with 18 open
   holds printed verbatim — never a clearance (D2's banner discipline).

### 7.3 The gate contract for D4 (recommended interface, §9.4 owns the mechanism)

- **L1 build** — assembler identity: the packet's bytes equal `tools/assemble-culture-d4.py`'s
  deterministic assembly (the assembler's own build path is called, never re-implemented);
  projector and adapter run into a temp mirror, never into `examples/`.
- **L2 channel** — the two-class differential: typed findings equal legacy findings minus
  **exactly** the 6 lines naming gloss-routed records; **zero** typed-run line names a
  gloss-routed record; **every** quote form still appears in the sound gate's inventory
  (register routing removes no form); a fixture that routes a quote form off-channel FAILS.
- **L3 holds** — the emitted finding set equals §7.1 exactly, keyed `(id, severity, where)`
  as a set with details pinned; 18/1/0.
- **L4 pins** — the typed packet's embedded digests re-verify against the bytes read
  (packet, projection, adapter, assembler).
- Exit codes: 0 all legs pass / 1 leg mismatch (channel, hold set, note set, determinism) /
  2 could-not-evaluate (stale pin, malformed packet, traceback, pin mismatch).

---

## 8. Required controls (negatives seat battery)

Design-level, to be executed by the D-neg seats; the pipeline-level negatives already
landed (D30–D32 per `reports/round-17/tests/neg-1.md:1-5`, `neg-2.md:1-5`: gloss smuggled
onto the sound channel, owed form silently dropped, loan without layer ref — the third
fixture was not on disk at this file's write time, sweep R20) cover the D2-mechanism
analogs. D4-specific required controls:

| # | control | expected |
|---|---|---|
| C-01 | quote form given a private segment (a segment outside 02's inventory) | FAIL `D4L-NATIVE`-class; a register never licenses an inventory |
| C-02 | quote form ≠ `apply(op, base)` | FAIL `D4L-ARGOT-DERIV` |
| C-03 | plain slot filled with the quote form | FAIL `D4L-REGISTER` |
| C-04 | routing row deleted while a plain doublet is owed | FAIL (dropped-row class) |
| C-05 | quote form claimed at E2 (before the E3 split) | FAIL `D4L-ERA` |
| C-06 | register-scoped record with `compare_only: true` | FAIL `D4L-SCOPE` |
| C-07 | two supplied forms in one slot | exit 2 `D4L-DATA`, no traceback |
| C-08 | unparsable component; unknown register enum; missing `slot_ref`; `doublet_of` pointing at a nonexistent slot | exit 2 `D4L-DATA` each |
| C-09 | gloss re-typed as native (the D2 artifact class restored) | the gloss re-enters the sound channel and FAILS — proving routing, not deletion, is the fix (D2's C1/C1b discipline) |
| C-10 | untyped legacy record whose form field is still checked | form still checked (R6 carry-over) |

Controls run in isolated scratch (`TMPDIR=$PWD/.scratch`), never against the delivered tree.

---

## 9. Artifact contract (recommended interface; the named seats own internals)

### 9.1 Paths and derived outputs

- `examples/culture-d4/components/01-brief.yml` … `12-ranks-names.yml` — 12 inputs.
- `tools/assemble-culture-d4.py` — the durable assembler (claim O), D3 naming convention
  (`tools/assemble-culture-d3.py`), emitting **exactly** `examples/culture-d4/packet.d4.yml`
  (gate-facing) on a default build; `--check` read-only byte comparison (exit 0 equal / 1
  drift / 2 error); `--selftest` with positive, tamper, malformed, and missing fixtures in
  scratch. If any gate needs a projection, it is a second derived output of the same
  assembler — never hand-edited.
- `tools/d4-typed-labels.py` — the projector (D2's `d2-typed-labels.py` pattern), emitting
  `examples/culture-d4/typed-labels.d4.yml`.
- `tools/assemble-d4-typed.py` — the adapter, emitting
  `examples/culture-d4/packet.d4.typed.yml` with `typed_channel`, `typed_assembly`,
  `pipeline_findings`, `pipeline_counts`.
- `examples/culture-d4/expected-holds.json` — §7.1, schema `kotodama-typed-pipeline-holds-v1`.

### 9.2 Pins

- `packet.d4.yml` `assembly` block pins component digests + the assembler's own digest
  (D3's `serializer_sha256` precedent, self-pin accepted there).
- `typed-labels.d4.yml` `assembly` pins `packet_sha256` + the projector's own digest.
- `packet.d4.typed.yml` pins packet, projection, adapter, assembler.
- `expected-holds.json` pins packet, projection, projector, adapter (D2 pins three; the
  adapter is D4's addition so the hold file transitively pins the routing code).

### 9.3 Determinism, freeze, replay

- Assembly is byte-deterministic: two builds into scratch produce identical sha256 (claim
  D: "twice byte-identical"), `--check` green on the delivered tree; no timestamps, no host
  paths, LF endings, sorted keys.
- Replay: a **new** frozen revision for the D4 run (the round-11 lesson: never re-point an
  old manifest; old manifests stay exactly as filed, the divergence reported).
- Regressions that must stay green and untouched: `tools/assemble-d2.py --check` (R5),
  `tools/assemble-culture-d3.py --check` (R6), `tools/gates/typed-pipeline-gate.py` default
  run 16/16 (R7) and `--selftest` 12/12 (R8), D2's `expected-holds.json` bytes, D2/D3
  packets and projections.

### 9.4 Gate placement

Recommendation: a **D4 entry point** that reuses the D2 gate's leg logic read-only
(`runpy.run_path`) if the legs are importable, otherwise a thin D4 gate implementing §7.3;
the D2 gate's bytes and behavior must not change (its hash is pinned by frozen rows and its
default run is a standing regression, R7/R8). Extending `typed-pipeline-gate.py` with a D4
mode is the acceptable alternative **only** with a new frozen revision and the old
manifests left filed; the typed-schema seats choose between the two and record the reason.

### 9.5 NON-CANON refusals (carried in every D4 artifact)

`canon_status: NON-CANON`; `handoff_status: prepared-not-accepted`; zero real-source
bindings; comparators are in-repo corpus entries cited by path and section, each with its
own cautions, never imported as packages (`01-brief.yml:122-129` comparator discipline);
no real-language sweep performed and none claimed (the naming gate's CROSS-HOLD row stays);
no rights, clearance, or attribution ruling; invented forms unscreened; era coordinates
fixture-relative.

---

## 10. Risks and open items (reported, not absorbed)

1. **The 12-component budget is tight.** Merging naming into `12-ranks-names` gives the
   naming gate its ledger but leaves D4 without D2's pragmatics/kin-address files; the
   register contract (06) is the declared replacement. If a component seat finds the merge
   unworkable, the change is a registry amendment in `01-brief.yml` naming the packet key
   that moved — not a 13th component (claim D's count is 12).
2. **Row 8 conditionality** (§7.1) depends on 02-phonology's mark decision; the hold-set
   seat records either outcome.
3. **Gate placement** (§9.4) is genuinely open between a new entry point and a mode; both
   are compatible with the claim, and the choice must not change D2's bytes.
4. **Rejected-axis evidence ages.** The dual-site and terrace rejections (§4.3) cite D2
   lines pinned at HEAD `9b49a4a`; if D2 is ever revised, re-read before reuse.
5. **No D4 tool exists yet** (R12/R13), so every §6 signature is a *requirement*, not an
   observation. Nothing in this file claims a D4 run.
6. **The D4 design fork is the round's top integration risk** — six seats, four culture
   concepts, three hold sets (§13, sweep R21). The parent must pick one culture and one
   delivered hold set before the component tree hardens further.

---

## 11. Receipts (all read-only; commands and observed results, 2026-10-18)

Scratch: `TMPDIR=$PWD/.scratch` exported, `.scratch/r17-d01/` created (R11–R13). No D4
artifact written, no filed round 8–16 byte touched (R14 shows only this file's directory
and this file).

| id | command | observed |
|---|---|---|
| R1 | `python3 -c "import json;d=json.load(open('examples/culture-d2/expected-holds.json'));print(d['counts'],len(d['holds']),len(d['notes']))"` | `{'hold': 15, 'note': 1, 'fail': 0} 15 1` |
| R2 | `git rev-parse HEAD` | `9b49a4a0fca6ceeab917d401945358fdedeb7e11` |
| R3 | `ls examples/culture-d2/components/ \| wc -l`; `ls examples/culture-d3/components/ \| wc -l` | `15`; `4` |
| R4 | `grep -c off_channel_field examples/culture-d2/packet.d2.typed.yml` | `10` |
| R5 | `python3 tools/assemble-d2.py --check` | exit 0 |
| R6 | `python3 tools/assemble-culture-d3.py --check` | exit 0 |
| R7 | `python3 tools/gates/typed-pipeline-gate.py` | exit 0, `summary: 16/16 legs passed` |
| R8 | `python3 tools/gates/typed-pipeline-gate.py --selftest` | exit 0, `selftest: 12/12 checks passed` |
| R9 | `python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml 2>/dev/null \| grep -c PHON-INVENTORY` → `10`; separately `… >/dev/null 2>&1; echo $?` → `1` | `10`; gate exit 1 |
| R10 | `sha256sum` over the §1 input set | digests as listed in §1 |
| R11 | `export TMPDIR=$PWD/.scratch; mkdir -p .scratch/r17-d01` | scratch prepared before any scratch write |
| R12 | `ls examples/culture-d4` | `No such file or directory` |
| R13 | `find . -iname '*d4*' -not -path './.git/*' -not -path './.scratch/*'` | exactly two matches: `reports/round-8/operability/neg-controls/neg-08/neg-08-d4-control.py` (unrelated: a round-8 supplement-review defect index "D4", a YAML boolean-coercion control — head read 2026-10-18) and `reports/round-17/d4/` (this brief's directory, empty before this file) |
| R14 | `git status --porcelain=v1` | concurrent round-17 worker changes only: claim-C civ files (`corpus/knowledge/civilizations/{inuit,maya-classic,mesoamerica-primary-sources,mongol,rapa-nui,siam-thai}.md`), `corpus/lessons/round-17.md`, `reports/round-17/{civ/,scope.md,scribe-1.md,scribe-2.md,tests/}` — no D4 artifact; `reports/round-17/d4/` was empty then and invisible to git (empty directories are not listed) |
| R15 | `python3 -c "import re;print(sorted(set(re.findall(r'^([a-z_]+):',open('examples/culture-d2/packet.d2.yml').read(),re.M))))"` | D2 packet keys (listed §5) |
| R16 | same over `examples/culture-d2/packet.d2.typed.yml` | adds `schema, typed_assembly, typed_channel, pipeline_findings, pipeline_counts` |
| R17 | `date -u +%Y-%m-%dT%H:%MZ`; `date +%Y-%m-%dT%H:%M%z` | `2026-10-18T09:21Z`; `2026-10-18T06:21-0300` |
| R18 | `python3 -c` over `examples/culture-d2/typed-labels.d2.yml` coverage block | `labels_by_kind {native-form: 46, translated-label: 10, borrowed-strata: 2}`, `typed_labels: 58` |
| R19 | post-write scope check: `git status --porcelain=v1` (concurrent entries filtered out) | this seat's only path is `?? reports/round-17/d4/`; also untracked and not this seat's: `reports/round-17/run-validation.py`, `reports/round-17/validation.json` (validation/parent seats) |
| R20 | `ls reports/round-17/tests/` | `neg-1.md  neg-2.md` (the third negative fixture had not landed at write time) |

---

## 12. Compliance self-attestation

- Wrote only `reports/round-17/d4/design-brief.md`. No commit, no push, no filed round 8–16
  byte touched, no component, packet, tool, or corpus file written (R14).
- All scratch under `.scratch/r17-d01/` with `TMPDIR=$PWD/.scratch` (R11).
- Every count carries a command and date (R1–R18); every quote names file and line; the two
  negative claims (no D4 artifact exists; no D4 run is claimed) carry their sweeps (R12/R13)
  and §10.5.
- NON-CANON throughout; no canon, handoff acceptance, real-language clearance, cultural
  permission, or rights/attribution ruling claimed, performed, or absorbed; contested scope
  routed to §0/§10.

---

## 13. Cross-seat reconciliation — the D4 design fork (reported, not absorbed; parent decision required)

**Status.** At this stamp (2026-10-18T09:30Z, sweep R21) `reports/round-17/d4/` carries
eight files from eight seats (R17-D01–D06, D18, D19), and they do **not** agree on the D4
culture, the component registry, or the hold set. This seat reports the divergence with
evidence; it does not edit another seat's file, does not re-base its own design silently,
and does not decide which culture the round ships.

Observed positions (all read 2026-10-18):

| record | culture / spine | registry | named hold set |
|---|---|---|---|
| `design-brief.md` (this file, R17-D01) | weigh-court brokerage; **COUNT × QUOTE** (§2–§3) | 12: `01-brief`…`12-ranks-names` (§5) | 18 holds / 1 note / 0 fails (§7.1), where-keys `GD-01..06`, `AL-01..06#plain`, `AL-03`, `RG-02`, `RG-05#a\|RG-07#a`, `RG-06#a\|RG-09#a`, `SM-03`, `RG-08#a\|RG-08#b`, `QN-01` |
| `components/01-brief.yml` (R17-D05, component seat 1) | furnace-league; **FIRE × MARK** — `:79` SEED-01 "towns of smiths on a forested upland basin, working bog-ore with charcoal; terraced valley grain and a small wool flock", `:85` SEED-07 | 12: `02-phonology`, `03-orthography`, `04-lexicon`, `05-naming`, `06-myth`, `07-symbolism`, `08-eras`, `09-costumes`, `10-ritual-calendar`, `11-contact-history`, `12-provenance` (`:228-240`) | 6 holds / 0 / 0: `D4L-FORM-UNRESOLVED` at `GAR-01..GAR-06`, `counts: {hold: 6, note: 0, fail: 0}` (`:195-205`) |
| `components/02-phonology.yml` (R17-D06) | fragment written to the D05 registry (`:1-8`) | — | — |
| `design-language.md` (R17-D02, language designer) | **TIDE + LEDGER** — `:61` "Institution/spine (assumption, the load-bearing one): **TIDE + LEDGER**"; tide-post `:281`, ledger `:322`, tide-mark `:353` | not stated as a registry | not stated as a hold set |
| `design-myth-era.md` (R17-D03, myth designer) | declares its **own** seed — `:45-57` "No D4 seed existed anywhere in the repo at write time (sweep …)", "the brief wins for the seed and this doc is superseded by a [new file]"; `SEED-D4-01` = "a salt-flat caravan confederation" | scopes `06-pantheon, 07-myths-motifs, 08-symbols, 09-eras-calendar` (D2-stem names) | not stated as a hold set |
| `design-costume.md` (R17-D04, costume designer) | "the tide-work wardrobe" (`:1`); GAR-07 "fair coat (imported oiled broadcloth)", GAR-08 "storm-assembly ensemble … raw bast cloth" (`:138-139`) | costume/material slice only | 3 holds / 0 / 0: `GAR-08..GAR-10`, **`D2L-` lettering**, with an explicit re-lettering note (`:217-231`) |
| `typed-support-1/2.md` (R17-D18/D19) | contract only; instance "pending the D4 design" (`typed-support-2.md:98-116`) | — | fragment path `reports/round-17/d4/expected-holds.fragment.json`, to be filled when the design names the records |

**Consequences (stated, not resolved).**

1. The delivered tree must follow **one** culture and **one** hold set. The claim's gate leg
   compares the delivered `examples/culture-d4/expected-holds.json` against the delivered
   typed packet's findings in both directions, keyed `(id, severity, where)` with details
   pinned (`reports/round-17/run-validation.py`: `def compare_holds` `:435`, selftest
   `holds-equality-pins-details` `:1243` — as-read digest `3fece609a635f58e5dde082419431cbca6e4f764b8fc3b19887403d194d64dd6`
   at 2026-10-18T09:32Z; the file was being edited concurrently, so cite the digest, not
   the lines); a mixed tree cannot satisfy it.
2. The **component tree is already being built to the D05 registry**: `components/01-brief.yml`
   `:228-240` fixes the extraction stems and packet keys, `components/02-phonology.yml` is
   written to it, and the costume slice has allocated `GAR-07..GAR-10` against the D05
   registry's `>= 6 garments` requirement (`components/01-brief.yml:219-222` A-04).
3. **The D04 costume slice reads against the D05 brief's own no-import list:** `:138-139`
   GAR-07 "imported oiled broadcloth" / GAR-08 "storm-assembly ensemble … raw bast cloth"
   vs `components/01-brief.yml:115` D1B-03 "bast/flax/reed fiber chain as the native textile
   story" and `:118` D2B-02 "wind as institution (storm law …)". Reported; not repaired here.
4. **The runner is tolerant of design-doc divergence but strict on the delivered set:**
   `run-validation.py`'s `# hold set pre-declared in design docs` block `:706-733` (same
   digest as item 1) requires every id and where named in the delivered expected file to
   appear *somewhere* in the union of the round-17 D4 design docs' text (boundary match),
   and does not compare design docs to each other. Divergence alone does not fail the
   runner; the tree/set choice does.
5. **D03's own protocol defers to the brief seat** (`design-myth-era.md:52`): "the brief
   wins for the seed and this doc is superseded by a [new file]". This file is that brief
   seat's artifact; whether it outranks the D05 "round-17 dispatch seed" claim
   (`components/01-brief.yml:78` "restated from the round-17 dispatch seed") is the parent's
   call, not this seat's.

**What is portable from this file under any culture choice.** §6 Δ1–Δ8 (register-scoped
routing, slot cardinality, derivation-checked forms, three-field donor separation,
register-era clock, register-property rank rules, the no-exemption re-proofs), §7.2 freeze
rules, §7.3 gate contract, §8 control battery, and §9 artifact contract are
culture-independent mechanisms. The furnace-league's own spine offers a natural host for
Δ1/Δ6 ("the mold-mark is the truth-mark", `components/01-brief.yml:80`: an attestation
register distinct from plain speech). **Not portable:** §2–§5 (culture, spine, registry,
where-keys).

**Reconciliation paths (parent's decision; this seat implements none).**

- **A — keep the landed furnace-league tree** (D05 registry + fragments), take its 6-GAR
  base hold set as rows 1–6, and port this brief's Δ1–Δ8 and register-axis hold classes
  onto it by re-lettering the where-keys. Cheapest against landed bytes; D02/D04's
  tide-work slices would then need superseding or re-causing (their material reading is
  item 3 above).
- **B — adopt TIDE + LEDGER** (D02/D04's convergence): D05's landed fragments, D03's seed,
  and this brief's culture are all superseded; the deltas still port.
- **C — adopt this brief's weigh-court** (D03's protocol gives the brief the seed): D05's
  and D06's fragments must be re-stemmed to §5's registry, and D02/D04/D03 re-keyed.

Sweep R21: `ls reports/round-17/d4/` → `components/{01-brief.yml, 02-phonology.yml}`,
`design-brief.md`, `design-costume.md`, `design-language.md`, `design-myth-era.md`,
`typed-support-1.md`, `typed-support-2.md` (2026-10-18T09:30Z).
