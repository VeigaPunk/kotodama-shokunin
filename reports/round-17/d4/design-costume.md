# R17-D04 — D4 costume/material design: the weigh-court wardrobe, goods classes, and their terminology strategy

- round: 17 (loop 2 of 3, build round 1 of 4) · date: 2026-10-18 · seat: **R17-D04**
  (costume designer) · status: **NON-CANON design record, pre-implementation**
- claim under specification: `reports/round-17/claims.json` D —
  `examples/culture-d4/` built end-to-end through the typed pipeline, gate
  findings exactly equal to the hold set named before implementation; counting
  command `python3 reports/round-17/run-validation.py`.
- this file designs the **costume/material slice**: component 11
  (`11-costumes.yml` — `costumes`, `constructions`, `cloth_sources`) and the
  goods/measure/material half of component 10 (`10-measures-materials.yml` —
  `materials`, `measures`, goods classes), with the terminology strategy and
  **this slice's contribution to the named hold set**. It writes no file under
  `examples/culture-d4/`; the component, assembler and typed seats land the
  tree, and the hold-set freeze is seat D19's (`reports/round-17/d4/typed-support-2.md`).
- at write time (2026-10-18 09:25–09:35Z) `examples/culture-d4/` and
  `tools/assemble-culture-d4.py` do not exist (`ls` sweeps: `No such file or
  directory`), and `reports/round-17/d4/` carried no component bytes — this is
  a genuine pre-implementation record.
- revision note: an earlier draft of this file assumed a littoral frame before
  the D01 brief landed (06:28Z). That frame is withdrawn: it violated the
  brief's NB-01 (no river/bank/tide/flood setting). The brief is now the fixed
  frame (§1), and the withdrawn draft's byte history stays in `.scratch`
  (`r17-d04-dryrun.py`); nothing of it survives into the record shapes below.

## 0. Read basis (read 2026-10-18; digests measured from the bytes on disk)

| path | sha256 | what it gave this design |
|---|---|---|
| `reports/round-17/d4/design-brief.md` (D01) | `a5fdc84d…8447e78f` | the fixed frame: §2 the weigh-court culture, §3 spine COUNT × QUOTE + AS-01..05, §4.2 the no-import list NB-01..08, §5 rows 10–11 (component duties), Δ1/Δ2 (routing classes, register pairs), Δ7 (costume/rank coupling, CS-03, SM-03), §7.1 the candidate hold set (18 holds / 1 note / 0 fails), §13 the cross-seat fork report |
| `reports/round-17/d4/typed-support-1.md` (D18) | `4ff0bf62…a070915f` | §5 the D4 derivation contract (artifact names §5.1, typed-packet shape §5.3, class vocabulary §5.5, determinism §5.6); F-D18-1: the live projector's slot regex is D2-literal and crashes on a foreign prefix |
| `reports/round-17/d4/typed-support-2.md` (D19) | `af69a6db…607c42e5` | §2–§3 the exactness contract and naming rules; "one hold per owed slot"; the fragment path `reports/round-17/d4/expected-holds.fragment.json` |
| `reports/round-17/claims.json` | `3ac1586a…d7df854` | claim D's required outcome and counting command |
| `reports/round-17/scope.md` | `7eb0d773…f429e6b` | §5: the runner's D-leg (hold-set equality keyed `(id, severity, where)`, counts and detail strings pinned; D8: hold set named in the design docs) |
| `tools/d2-typed-labels.py` | `0da0015f…fb89c802` | the live D2 projector used as the arithmetic model: `_SLOT_RE` `:449`, `_costume_label` `:493`, `project_labels` `:605`, FORM hold emission `:782–793`, `claims_from_packet` `:1615`, `_match_material` `:1740` |
| `tools/gates/typed-pipeline-gate.py` | `d102fd1d…68e27d` | the equality leg (`:295`) and key (`:134`); D2's frozen 15/1/0 (`:80–98`) |
| `examples/culture-d2/expected-holds.json` | `a5dc26d5…d6dde3a` | the D2 baseline the D4 file mirrors (`kotodama-typed-pipeline-holds-v1`) |
| `examples/culture-d2/components/11-costumes.yml` | `b6e2c5c2…483f22` | the precedent record shapes (`form_slot` `:217`, `form_slots` ledger `:404–418`, "this file coins no surface form") |
| `corpus/knowledge/synthesis/costume-language-coupling-table.md` | `dc7b723f…314cb9` | §2 the term/wearer/era field model and reject conditions; §5 the design decision table; §7 "version the relation, not just the silhouette" |
| `corpus/knowledge/culture-material/dress-through-eras.md` | `88872005…41b769` | §1 the three-slot grammar; §9 worn words; §10 enforcement mechanisms (two per culture); §11 the application protocol |
| `corpus/knowledge/synthesis/era-language-staging.md` | `621b7a33…4a91da8` | `:108–124` type every label; a period label is not the wearer's term |
| `corpus/knowledge/synthesis/glossary-registry-format.md` | `043a4e3b…7caeee3` | one lemma per record; script/representation/scheme separate; "unknown is not all eras" |
| `corpus/knowledge/culture-material/sumptuary-law-rank-display.md` | `c5def40e…5f7a6fdb` | rank-display rules encode anxiety and enforcement is selective — the CS-03 design principle |

Digests were measured at 2026-10-18 09:34Z; the wave was still writing
sibling files while this seat worked (measured changes: `design-brief.md`
43263→50273 bytes, `typed-support-2.md` 10367→16372 bytes), so every digest
here is a *measured-at* value, and drift in a sibling is reported by the
verifier rather than silently absorbed.

Counts below carry their command and date; quotes name their location; negative
claims carry their sweep. Nothing here is a real-world clearance or a canon
ruling.

## 1. Scope and authority

**Authority order.** D01's brief is the fixed frame: the culture (weigh-court
brokers, `design-brief.md:91`), the spine COUNT × QUOTE (`:128`), the
no-import list (`:178`), the component duties (`:236–237`), the deltas
(`:254`, `:283`, `:357`), and the candidate hold set (`:385`). This file
designs *inside* that frame and does not renegotiate it. Where the brief
leaves an identifier open (record ids beyond `CS-03`, the goods block name,
the slot prefix), this file proposes one and states the reconciliation rule.

**Owns:** the wardrobe grammar and record set (component 11), the goods
classes, measures and material routes (component 10's second half), the
terminology strategy per record, and this slice's named hold rows.

**Does not own:** the brief; phonology and the actual forms (language seat);
the register law, argot loans and doublets (component 06/05 seats); rank law
and the charter's rank floor (component 12 seat); the D4 projector/adapter and
the expected-holds file (D18/D19 seats); canon (lore-shokunin alone).

## 2. The frame, read into the costume/material slice

**The culture in one line** (`design-brief.md:93`): a settled grain-and-orchard
plain whose towns run weigh-courts; brokers bind prices in a taught **quote
register** and keep the record on **notched rods**.

**Spine, in dress terms** (`:128`, SP-03 tagging): **COUNT** is public —
measures, weight classes, the hem-line, the belt hardware, the rod itself;
**QUOTE** is binding speech — who may wear the recording apron, who may wear
the guest-robe to quote. Every record below carries
`axis: count | quote | both | neutral-with-rationale` and every component file
declares `spine_coupling:` naming its two strongest couplings.

**Boundary rows that bind the wardrobe** (`:178–190`):

- **NB-01** — no river/bank/tide/flood setting, staple or metaphor. The
  wardrobe has no water vocabulary, no oiled surfaces, no flood calendar.
- **NB-02** — no tying/binding/knot-as-obligation imagery (D1's boundary,
  adopted). The dress system therefore uses **folding, layering, pinning,
  belt-suspension, seams and stamping** — never knots, never cords that
  "bind". The rod-belt *suspends* the rod; it does not bind a person.
- **NB-07** — no D2 spine vocabulary (verticality/ascent/descent deixis,
  wind/breath, herd/pasture terms). The wardrobe has no felt/wool chain.
- **AS-05 "guests quote, hosts record"** (`:159`) — the central institution,
  and the source of the wardrobe's hardest line: the recording apron is a
  host garment; a guest wears the guest-robe and may quote, never record.

**Era strata** (`:108`, `:236`): E0 notched rods only; E1 the ledger script
and the first imports; E2 the script freezes spellings and the charter's rank
floor bites (CS-03); E3 the register split — the quote register becomes
taught and the plain doublets start being owed.

## 3. The dress grammar (three slots, `dress-through-eras.md` §1)

**Silhouette — layered flat panels, folded and pinned; no tailoring, no
knots.** A plain cloth robe or apron panel, folded to the body and pinned at
the shoulder or hip; a leather apron over it for recording work; a leather
belt that suspends the rod sheath. Status is not cut into the body line; it
is carried at three places: the **hem-line depth**, the **apron's leather
grade and stamp**, and the **belt hardware**. (Layered body technology:
opacity and who-shows-what, per §1's "layered cultures choreograph opacity".)

**Material — from the plain and its one road** (routes in §4):

| stratum | material | route | era |
|---|---|---|---|
| recording wear | local leather (apron, belt, rod sheath) | local | E0–E3 |
| everyday wear | local plain cloth (robe, guest-robe) | local | E0–E3 |
| trade-day wear | imported plain cloth (trade-sash, guest-robe cloth) | the western grain towns | E1–E3 |
| record hardware | rod-wood + court pigment (the rod-mark) | local | E0–E3 |
| the sixth material | coiled reed fiber (a good, not dress) | local | E0–E3 |

The material routes are import/local with **one unresolved route** (SM-03,
§4.4) held as `D4L-MATERIAL` — the brief's Δ7 signature (`:364`).

**Wearer rule — rank floor plus guest-law, enforced twice** (`dress-through-eras.md`
§10 requires at least two mechanisms):

1. **institutional rank floor** — the charter fixes which ranks may wear the
   recording apron and which hem-line depth each rank may show; the court
   reads it at a glance. Enforcement is selective, as rank display rules
   always are (`sumptuary-law-rank-display.md`) — that selectivity is what
   makes CS-03 a scene, not a footnote.
2. **guest-law asymmetry** — a guest may wear the guest-robe and quote; a
   guest may not wear the recording apron. The asymmetry is enforceable
   because the apron is *issued* by the court, not bought.

**Misread scene** (`dress-through-eras.md` §11 step 7): a guest in the
recording apron (claiming host standing at the weigh-court); an apprentice
showing a broker's hem-line depth; a trade-sash on a day the court is not
sitting.

**Time-lock** (§11 step 5): the **court-day schedule** — which layer is worn
and when the apron may appear is keyed to whether the court sits, not to
taste; and at E3 the register split re-keys the robe vocabulary (the plain
doublets start being owed).

**Era drift** (§11 step 8 — relations, not silhouettes): E0 rod-belt, apron,
local cloth only → E1 the script arrives and imported plain cloth enters
(trade-sash, guest-robe) → E2 the charter's rank floor is enforced and the
declared violation CS-03 occurs → E3 the register split; the old wear stays as
fossil while the quote register's vocabulary is taught.

## 4. Record set (design rows; ids are contract ids, glosses are labels)

### 4.1 Component 11 — costumes, constructions, cloth sources

| id | garment (gloss) | silhouette/status slot | material | era | wearer / context | axis | term status |
|---|---|---|---|---|---|---|---|
| CS-01 | trade-sash (imported plain cloth; folded, pinned at the shoulder) | trade-day layer; sash width by rank | imported plain cloth | E1–E3 | brokers and guests; court days | count | supplied (Class A) |
| CS-02 | court-apron (local leather; stamped at issue) | recording layer; leather grade + stamp | local leather | E0–E3 | host ranks only (charter floor) | both | supplied (Class A) |
| CS-03 | court-apron worn below the charter's rank floor — **declared violation, kept visible** | recording layer, rank floor violated | local leather | E2 | a wearer below the floor; the charter case | count | supplied (Class A) |
| CS-04 | guest-robe (local plain cloth; guest-law wear) | guest layer; hosts record | local plain cloth | E1–E3 | guests; quoting only | quote | supplied (Class A) |
| CS-05 | rod-belt (local leather; suspends the rod sheath) | record hardware; belt hardware | local leather | E0–E3 | rod-holders and above | count | supplied (Class A) |

Constructions `CT-01..CT-03`: CT-01 the folded panel (no cut, no knot);
CT-02 the apron seam and stamp placement; CT-03 the belt-and-sheath
suspension. Cloth sources `CL-01..CL-02`: CL-01 the local plain weave; CL-02
the western-towns import. (Ids beyond `CS-03` are this design's proposal; the
component seat may re-letter, and the reconciliation rule is *map by slot id*,
never by label.)

### 4.2 Component 10 — materials

| id | material (identity key) | slot | route | route eras |
|---|---|---|---|---|
| MAT-01 | local leather | apron-belt-leather | local | E0–E3 |
| MAT-02 | imported plain cloth | sash-robe-cloth | import (western grain towns) | E1–E3 |
| MAT-03 | local plain cloth | robe-cloth | local | E0–E3 |
| MAT-04 | rod-wood | ledger-rod | local | E0–E3 |
| MAT-05 | court pigment | rod-mark | local | E0–E3 |
| MAT-06 | coiled reed fiber | goods-fiber | local | E0–E3 |

### 4.3 Component 10 — goods classes (gloss-routed; slots owed)

| id | goods class (reader-facing gloss) | measure ref | era | axis | form slot (owed) |
|---|---|---|---|---|---|
| GD-01 | grain, by the sealed measure | SM-01 | E0–E3 | count | LEX-GD-01 |
| GD-02 | orchard produce, by the crate count | SM-02 | E0–E3 | count | LEX-GD-02 |
| GD-03 | pressed oil, by the jar | SM-04 | E1–E3 | count | LEX-GD-03 |
| GD-04 | coiled reed fiber, by the coil | SM-05 | E0–E3 | count | LEX-GD-04 |
| GD-05 | plain cloth, by the bolt (imported) | SM-05 | E1–E3 | both | LEX-GD-05 |
| GD-06 | hide and leather, by the piece | SM-02 | E0–E3 | both | LEX-GD-06 |

### 4.4 Component 10 — measures (the sealed measures; SM-03 unresolved)

| id | measure | status | route |
|---|---|---|---|
| SM-01 | the sealed grain measure | resolved | local (MAT-01 stock) |
| SM-02 | the weight-stone set (public monument) | resolved | local |
| SM-03 | **the guest measure** — what guests use to quote | **route unresolved by design** | none recorded |
| SM-04 | the oil-jar measure | resolved | local |
| SM-05 | the cloth bolt measure | resolved | import (MAT-02) |

**Why SM-03 stays unresolved** (the design decision, not an omission): by
AS-05 the court records *hosts'* obligations; a guest's own measure is outside
the court's ledger, so the court records no origin for it. The design keeps
that gap visible as exactly one `D4L-MATERIAL` hold (brief §7.1 row 6) rather
than inventing a route. This is the D2 material-seam discipline (an unresolved
reference is carried, never invented into the inventory) applied at the
measure layer.

### 4.5 The declared violation CS-03

CS-03 is a wearing record, not a repair: the court-apron worn below the
charter's rank floor at E2. It carries `declared_violation: true`, the
charter rule reference (rank seat's id), the era, and the basis. The
costume-era gate must emit **exactly one R-01 note** naming it and no other
finding (Δ7, `design-brief.md:362–366`); the D2 precedent is the R-01 note in
`examples/culture-d3/README.md`'s observed gate run. The violation is never
laundered into a clean row — the gate note is the visibility mechanism.

## 5. Terminology strategy — the native-form vs translated-label decisions

The decision rules are the lane's typing table (`SKILL.md` "Label typing")
read through `costume-language-coupling-table.md` §2 ("a modern curatorial
label becomes an attested historical native word" is a reject condition) and
`era-language-staging.md:108–124`. Three classes, assigned per record:

**Class A — supplied native forms (the five costume records).** The wearer
terms: what a broker, a guest or a rod-holder actually says. Each is supplied
through the labels channel (§7.5), owned by the lexicon seat, coined inside
02-phonology's inventory (brief §5 row 02: a register that adds a segment is a
`D4L-NATIVE` finding, never a license). These five records must emit **no
finding** — and by the design's arithmetic they are the only form-bearing
records in the slice that stay on the sound channel.

**Class B — gloss-routed goods slots (the six goods records).** The court's
goods classes carry reader-facing glosses; their **court terms are owed**. The
gloss is routed off the sound-and-identity channel (Δ1 class 1), the owed slot
is held as `D4L-FORM-UNRESOLVED`, one per record. The design rationale is
explicit: the goods/measure nomenclature is the measure seat's live work, and
the design refuses to coin court-instrument terms ahead of the sealed-measure
inventory — the same refusal that keeps SM-03's route unresolved. This is the
D4 exercise of D2's class-1 routing on the culture's *goods* instead of its
garments, and it is where "a gloss never enters the sound test, and an owed
form is held, never laundered" is proven under the D4 schema.

**Class C — register-scoped terms (the argot loans AL-01..06).** These are
component 05/06's, not this slice's (Δ1 class 2, brief §7.1 row 2): a quote
form stays on the sound channel while its plain doublet is owed. The
costume/material design contributes **no** register pair; if a costume term
ever needs a `#plain`/`#quote` pair (e.g. a robe term taught in the quote
register at E3), that is a recorded design amendment, not a silent addition.

Three cautions that are part of the strategy (`SKILL.md` typing cautions):
inventory-legal is not native; a label is not a gap-filler; a label is not
history. One structural rule carried from the D2 discipline: a category no
wearer names is not written as a costume record — the pipeline has no
permanent-label state, so such categories live in the component's prose
tables, not in the record set.

## 6. The named hold set (pre-implementation) — this slice's contribution

Consistent with the brief's candidate set (`design-brief.md:385–411`, rows 1
and 6), this slice contributes **exactly seven rows** to
`examples/culture-d4/expected-holds.json`:

| id | severity | where | trigger (proving leg) | detail |
|---|---|---|---|---|
| `D4L-FORM-UNRESOLVED` | `hold` | `GD-01` | gloss-routed goods slot with no supplied sound form (channel leg) | `label_id LEX-GD-01 has no supplied native/borrowed form` |
| `D4L-FORM-UNRESOLVED` | `hold` | `GD-02` | same | `label_id LEX-GD-02 has no supplied native/borrowed form` |
| `D4L-FORM-UNRESOLVED` | `hold` | `GD-03` | same | `label_id LEX-GD-03 has no supplied native/borrowed form` |
| `D4L-FORM-UNRESOLVED` | `hold` | `GD-04` | same | `label_id LEX-GD-04 has no supplied native/borrowed form` |
| `D4L-FORM-UNRESOLVED` | `hold` | `GD-05` | same | `label_id LEX-GD-05 has no supplied native/borrowed form` |
| `D4L-FORM-UNRESOLVED` | `hold` | `GD-06` | same | `label_id LEX-GD-06 has no supplied native/borrowed form` |
| `D4L-MATERIAL` | `hold` | `SM-03` | sealed-measure slot with no resolved route (`maps_to`/route absent) | `sealed-measure slot with no resolved route (maps_to absent)` |

**Slice counts: hold 7, note 0, fail 0.** The detail strings follow the D2
wording templates (measured live, §8); the delivered D4 projector's exact
strings are the ones the expected file must pin (typed-support-2 §2). The
union of all slices is the brief's candidate **18 holds / 1 note / 0 fails**;
the freeze authority is seat D19, and any later change is a recorded
amendment naming the component decision that forced it (brief §7.2 rule 1).

**Zero-fail conditions — design requirements, not observations** (each
demonstrated live in §8):

1. every supplied form (the five Class-A terms) is coined inside the declared
   inventory — an out-of-inventory form is a `D4L-NATIVE` **fail**, exit 2;
2. every costume, goods and measure record that claims a material carries one
   that resolves in the packet's material scope, with routes covering the
   claim era — a gap is a material-section finding (the D2 class
   `R-MAT-ERA-EXCLUDED` analogue), never a silent pass;
3. the six owed slots stay owed (no half-supplied pair), and the five
   supplied slots carry exactly one supplied form each (`(owner, slot)` is
   1:1 — Δ2's cardinality);
4. SM-03's route stays absent with its `route_note` (the design's reason),
   and no bridge is invented to clean it.

**Must not appear** (with the design condition that prevents each):
`D4L-NATIVE` (condition 1); `D4L-DATA` (field rules §7); `D4L-SCOPE` (era
ids are contract tags only); `D4L-BORROW` (no borrow block in this slice — the
one borrow row is AL-03, the lexicon seat's); `D4L-REGISTER`/
`D4L-REGISTER-UNRESOLVED` (no register pair in this slice — Class C boundary);
rank rows (`D4L-RANK`) are the rank seat's.

**Not part of the pipeline finding set:** the CS-03 declared violation is
surfaced by the **costume-era gate** as exactly one R-01 note (Δ7) — a
culture-gate reading, not a pipeline row. The D2 precedent is explicit: the
costume gate's R-01 note sat outside `expected-holds.json` while the pipeline
finding set carried only the label/rank rows. The runner's equality leg reads
the typed packet's `pipeline_findings`; the culture gates are graded by their
own exits in {0,1}.

## 7. Interface contract for the implementers

**7.1 Costume records (component 11).** Fields: `id` (`CS-NN`), `garment`
(reader-facing gloss), `form_slot` (`LEX-CS-NN …`), `material` (the
inventory's own material name — the identity key, §7.3), `era` (a contract
tag; ranges where the record spans strata), `axis` (SP-03), `wearer` (rank or
guest-law reference by id), `term_status: supplied` for all five records, and
for CS-03 additionally `declared_violation: true` + the charter rule
reference + `violation_basis`.

**7.2 Goods records (component 10).** Fields: `id` (`GD-NN`), `gloss`
(reader-facing), `form_slot` (`LEX-GD-NN`), `term_status: owed`, `measure_ref`
(§7.4), `era`, `axis`. The goods block's packet key is this design's proposal
(`goods`); if the packet shape is frozen to the brief's key list
(`design-brief.md:241–245`), the records may live under `materials` with a
`kind: good` marker — the reconciliation rule is *map by slot id*, and the
projector must find them by their owed `form_slot`, not by block name.

**7.3 Material and measure records (component 10).** Materials as §4.2
(`id`, `material` name, `slot`, `routes`). Measures as §4.4; SM-03 carries
`routes` absent/null plus `route_note` naming the design reason (AS-05: the
guest measure is outside the court's record) — that absence is what the
`D4L-MATERIAL` leg must read, exactly once, at `SM-03`.

**7.4 Slot prefixes and the generalized slot pattern.** This design uses
`LEX-CS-NN` (costume slots) and `LEX-GD-NN` (goods slots). The live D2
projector cannot parse them: its pattern is the D2-literal
`LEX-GAR-[0-9]{2}` (`tools/d2-typed-labels.py:449`) and `_costume_label`
crashes with a raw `AttributeError` on a non-matching slot (`:498`) —
measured twice in the dry run (§8, receipt P-crash), the same defect
typed-support-1 F-D18-1 reports. **Requirement on the D4 derivation:** the
slot pattern is generalized to `LEX-<REC>-NN` (or the design re-letters its
slots to the D2 convention), and an unmatched slot is refused with a stable
exit-2 `D4L-DATA` finding, never a traceback. If the typed seat prefers
adopting D2's `LEX-GAR-NN` convention, the slot ids in §4 are re-lettered 1:1;
the `where` set (`CS-*`, `GD-*`, `SM-03`) is invariant.

**7.5 The labels channel.** The five Class-A forms arrive as supplied
`native-form` label records (the D2 `typed_labels` channel is the precedent),
each `id` = `label_id` = `LEX-CS-NN`, `status: supplied`, with `text`,
`script`, `representation`, `scheme`, `era_ids`, `register: plain`, `evidence`,
`source`. The form text is the lexicon seat's; this design coins nothing. No
label record is created for the owed goods slots — their *absence* is the
hold.

**7.6 Costume-era gate inputs.** Every costume record carries `era` +
`material` (the D2 projector refuses otherwise: `claims_from_packet`,
`:1615`, measured in §8 control 3); CS-03's `declared_violation` fields are
what the gate reads to emit the single R-01 note. The gate must exit 1 with
that one note and no other finding (Δ7).

**7.7 Artifact names** (typed-support-1 §5.1, binding): `examples/culture-d4/packet.d4.yml`,
`packet.d4.typed.yml`, `typed-labels.d4.yml`, `expected-holds.json`; the
fragment `reports/round-17/d4/expected-holds.fragment.json` is D19's.

## 8. Design-time dry-run receipts (arithmetic measured, not asserted)

The D4-bound projector does not exist at this stamp (typed-support-1 §5.7),
so the slice's record shapes were run through the **live D2 projector's pure
functions** (`project_labels`, `validate_labels`, `reconcile_scoped`) in a
scratch harness, with the loaded module's slot pattern generalized to
`LEX-[A-Z]+-[0-9]{2}` (the §7.4 requirement) so the design's own slot names
parse. Placeholders, not proposals: the inventory `{a,b,p,t,k}` and the form
strings (`apa`, `baka`, …) are artificial; the language seat owns the real
inventory and forms.

- harness: `.scratch/r17-d04-dryrun2.py`, sha256
  `ef0b542a597486de40933502a33945665b4a452685a832c5c33dacbd91494998`
- output: `.scratch/r17-d04-dryrun2.out`, sha256
  `c9734891182855f371ddb4513f780d933cf52beeb1bf7290a0efcccf5f0aa3c9`
- command (2026-10-18): `export TMPDIR=$PWD/.scratch && python3 .scratch/r17-d04-dryrun2.py`
- projector revision read at run time: `tools/d2-typed-labels.py` sha256
  `0da0015f…fb89c802` (unchanged)

| run | observed |
|---|---|
| positive (design as named) | labels gate exit 1; findings = exactly the six FORM holds `GD-01..GD-06`; counts hold 6 / fail 0; 16 labels projected (5 native-form + 11 translated-label); material reconciliation `{claims: 11, findings: 0}` — the five costume and six goods records all resolve their material refs |
| control 1 — supply one owed goods slot (`LEX-GD-01`) | 5 holds (`GD-02..GD-06`): the hold set tracks the owed set 1:1 |
| control 2 — an out-of-inventory supplied form (`bakaz`) | `D2L-NATIVE` **fail** at `LEX-CS-02`, exit 2 — why condition 1 exists |
| control 3 — a costume record without a material ref | `ReconciliationError: CS-01: costume carries no material reference` — the refusal `claims_from_packet` performs |
| receipt P-crash — the same harness **without** the pattern generalization | `AttributeError: 'NoneType' object has no attribute 'group'` at `tools/d2-typed-labels.py:498` on the first `LEX-CS-01` slot — the D2-literal pattern defect (typed-support-1 F-D18-1), measured twice; why §7.4 is a requirement |

Limits of this receipt: the harness exercises the D2 projector's pure
functions over an in-memory D4-shaped packet, not the delivered D4 tree, the
D4 projector, the adapter or the gate; the `SM-03` `D4L-MATERIAL` row is
*designed* here (name, trigger, where) and its emission is the D4 projector's
leg, which does not exist yet. This is a design-time control, not the round's
verification; the equality leg runs in `python3 reports/round-17/run-validation.py`
once the tree lands.

## 9. Open handoffs and (to-verify) items

### 9.1 The cross-seat fork (observed 2026-10-18 09:30–09:34Z; reported, not absorbed)

The wave's design seats do **not** agree on the D4 culture; the parent must
decide which frame ships. Observed positions (digests measured 09:34Z):

| record | position |
|---|---|
| `design-brief.md` (D01, `a5fdc84d…`) | weigh-court brokerage; COUNT × QUOTE; hold set 18/1/0 with `GD-01..06` and `SM-03`; its §13 reports the fork itself |
| `components/01-brief.yml` (D05, `1a51b313…`) | **furnace-league**; FIRE × MARK (smith towns, forested upland basin, bog-ore, charcoal); 6 holds/0/0 at `GAR-01..GAR-06` — a different culture and registry from the brief |
| `design-language.md` (D02, `94713577…`) | TIDE + LEDGER (its own assumption, stated as such) |
| `design-myth-era.md` (D03, `66601b1a…`) | salt-flat caravan confederation (its own seed, with a supersede-by-new-file note) |
| `typed-support-1/2.md` (D18/D19) | contract only; the hold-set instance pending the design |
| **this file (D04)** | **follows the D01 brief** (§1); slice rows `GD-01..06` + `SM-03` |

**This seat's position, stated so the integrator can act:** the brief is the
design authority (its own §0/§1), so this file is written to it. If the parent
ships a different frame (the furnace-league registry, or another), this file's
*mechanics* survive — three-slot grammar, the supplied/owed/register class
split, the hold-arithmetic conditions (§6) — while the glosses and record ids
re-map by slot id, and the named rows are superseded only by a **recorded
amendment** naming the frame decision (brief §7.2 rule 1). No seat's file is
edited by this one; the fork is the parent's decision, not a repair this seat
may make.

### 9.2 Handoff items

- **(to-verify) the component seats**: record ids beyond `CS-03` (proposed
  here: `CS-01..05`, `CT-01..03`, `CL-01..02`, `MAT-01..06`, `SM-01..05`,
  `GD-01..06`) and the goods block key (§7.2) — reconcile by slot id.
- **(to-verify) the typed seat (D18/D19)**: the generalized slot pattern
  (§7.4), the goods routing leg, the `SM-03` material leg, and the exact
  detail strings; the fragment and the freeze are D19's.
- **(to-verify) the language seat**: the five Class-A forms inside 02's
  inventory; the plain register label; no register pair in this slice.
- **(to-verify) the rank seat**: the charter's rank floor and the rule
  reference CS-03's `declared_violation` cites.
- **(to-verify) the assembler seat**: `form_slot`/`material`/`era` extraction
  for costumes, goods and measures; the CS-03 violation fields.
- **Handoff target:** lore-shokunin receives this as a NON-CANON design
  proposal with its cautions attached; no entitlement, clearance or canon
  claim is made or implied.

### 9.3 Re-map under the landed component registry (furnace-league, D05)

The components landing in `reports/round-17/d4/components/` follow D05's
registry, not the D01 brief (observed: `01-brief.yml` `1a51b313…`,
`02-phonology.yml`, `03-orthography.yml`, `04-lexicon.yml`, `05-naming.yml`,
all read 09:34–09:35Z). If that frame ships, this is the costume slice
re-mapped to its contract — offered so the integrator can act without waiting
for a rewrite; it is **not** adopted here (the brief remains this file's
frame, §1), and adopting it is a recorded amendment.

**D05's costume contract** (`components/01-brief.yml:157`, `:174`, `:184–205`):
component `09-costumes` supplies `costumes`, `materials`, `cloth_sources`,
`rank_rules`; costume fields `[id, garment, form_slot, material, era,
wearer_ranks, rite, axis, evidence, follows]`; id prefixes `GAR-` garments,
`CMAT-` materials, `CS-` cloth sources, `RK-` rank rules; **≥6 garments**; all
forms lowercase ASCII, length spelled as double vowels, no diacritics
(`:194` RG-08); the named hold set is **6 × `D4L-FORM-UNRESOLVED` at
`GAR-01..GAR-06`, counts {hold: 6, note: 0, fail: 0}** (`:195–205`), with the
design note that the six garment slots are the deliberate debt and every other
checked surface is designed clean.

**Re-mapped record set** (design content for the smith-town frame: forested
upland basin, bog-ore and charcoal, terraced valley grain, a small wool flock;
spine FIRE × MARK; era E0 pre-script stamp era, E1 script seam, E2 literate
league anchor):

| id | garment (gloss, owed slot) | material | era | wearer / rite | axis |
|---|---|---|---|---|---|
| GAR-01 | forge apron (thick hide; spark and slag protection) | CMAT-01 local hide | E0–E3 | smiths by furnace right; forge work | fire |
| GAR-02 | quench smock (coarse wool, soaked at the quench) | CMAT-02 upland wool | E0–E3 | smiths; the quench | fire |
| GAR-03 | league cloak (fulled wool; town stamp at the shoulder) | CMAT-02 upland wool | E1–E3 | league delegates; the league assembly | mark |
| GAR-04 | stamp-belt (hide; carries the maker's stamp and charge tokens) | CMAT-01 local hide | E0–E3 | stamp-holders by furnace right | mark |
| GAR-05 | kiln hood (felted wool; charcoal burners, kiln tenders) | CMAT-03 felted wool | E0–E3 | charcoal burners; the burn | fire |
| GAR-06 | market-day coat (valley wool with salt-road cloth facing) | CMAT-04 salt-road cloth (import) | E1–E3 | market-goers; market days | both |

Materials `CMAT-01..05`: local hide; upland wool; felted wool; salt-road cloth
(import, E1–E3); charcoal pigment (the stamp mark). Cloth sources
`CS-01..02`: the valley weave; the salt-road import. Rank coupling: furnace
right (`RK-` records), never wealth alone (D05 `:191` RG-07); the no-import
row D1B-03 (`:115`) forbids a bast/flax/reed native textile story, so the
fiber chain is wool and hide with one declared import.

**Strategy delta under this frame:** the garment terms are owed *by design*
(all six are the named debt), so the terminology strategy's supplied-wearer-
term class (Class A) has no instances here, and this slice contributes **no**
material row (contrast the brief frame's `SM-03`). The mechanics of §5–§6
still apply: glosses are translated labels, off the sound channel; the six
owed slots are held, one per record; zero fails; the CS-03-style declared
violation mechanism (§4.5) is available to `09-costumes` if its rank coupling
needs a kept-visible case.

## 10. Non-canon boundary

NON-CANON. This file designs an invented wardrobe and goods system for the D4
drill and describes no real people, region, market, guild, script or living
practice. Every record is a proposal; nothing here decides what is true in any
world. Canon, entity identity, chronology and supernatural truth belong to
lore-shokunin alone (`corpus/knowledge/synthesis/worldbible-integration-contract.md`;
`PROVINCE.md`). No real-world rights, attribution or clearance ruling is made;
the corpus citations are design grounding, not evidence about any living
tradition.
