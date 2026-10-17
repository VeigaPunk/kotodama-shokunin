# 02 CONNECTOR — D2 language / myth / material / era interface map

- wave: `supplement-opencode-1` (not a numbered GLM round)
- baseline revision: `fe34faaafbe0add59ff68827a0df6c5782a72404`
- role: connector, read-only. No canon decided, no symbol equated with a god, no
  component or gate edited. Evidence only.
- companion record: `corpus/lessons/supplement-opencode-1/sources/02-connector.json`
  (seven source-recheck audits for `corpus/knowledge/synthesis/era-myth-language-costume-matrix.md`).
- scratch (not required for reproduction): `reports/supplement-opencode-1/scratch/02-connector/`.

Pinned artifacts used, all at baseline bytes:

| artifact | identity |
|---|---|
| `examples/culture-d2/packet.d2.yml` | sha256 `d5fb408871dcb985c2f9b134a26c6d64e8640a6f1f17ba1c6bb3c5db1d6dbd96` (= `claims.json` baseline) |
| `tools/assemble-d2.py` | baseline via `git show fe34faa:tools/assemble-d2.py` |
| frozen round-4 gate outputs | `tools/gates/frozen/round-4/*.out` |
| round-4 material review | `examples/culture-d2/reviews/10-materials.md` M10-R01 |

Commands actually run and observed results:

- `python3 tools/assemble-d2.py --check` at 12:33 local → `packet.d2.yml: byte-identical
  deterministic assembly`, exit 0. Re-run at 12:44 → `packet.d2.yml differs from
  deterministic assembly`, exit 1: in-flight sibling edits landed in
  `examples/culture-d2/components/06-pantheon.yml` (PAN-03 `Humweha` → `Humaweha` + `NE-01`
  erratum, mtime 12:38) and `tools/assemble-d2.py` after my first run. Packet regeneration
  is the parent's step; this report therefore analyses baseline bytes.
- `python3 tools/gates/naming-collision-gate.py examples/culture-d2/packet.d2.yml`
  (baseline packet) → exit 1, exactly 18 findings, byte-identical to
  `tools/gates/frozen/round-4/naming-collision-gate.out`:
  10 `PHON-INVENTORY`, 6 `NAME-NEAR`, 1 `PHON-CODA`, 1 `CROSS-HOLD`.
- `git show fe34faa:examples/culture-d2/packet.d2.yml | sha256sum` → matches the digest above;
  the committed packet contains `Humweha` ×10 and `Humaweha` ×0.
- Structured extracts below were computed with the gates' own `parse_packet` reader over
  component blocks (script paths are listed in the JSON record's `basis` fields).

## 1. What the assembler consumes — the gate-facing interface surface

`assemble()` sources the packet from nine component files (exactly the nine pinned in
`packet.assembly.source_sha256`):

| packet key | source component | assembler treatment |
|---|---|---|
| `phonology` | 02 | copied, then **overwritten**: `coda=[n,l,r,s]`, `onset_clusters=false` |
| `morphology` | 03 | copied |
| `lexicon`, `constructions`, `layers` | 05 | copied (40 lexicon records) |
| `pantheon` | 06 | copied (7 records) |
| `motifs`, `roles` | 06 **then 07** | concatenated, no aliasing or deduplication |
| `symbols` | 08 | copied (10 records) |
| `eras`, `source_era_dates`, `era_records` | 09 | `eras` = tag list `E0..E3`; `era_dates` renamed to `source_era_dates` (D-coordinates) |
| `costumes`, `materials`, `cloth_sources` | 11 | copied (10 / 9 / 3 records) |
| `names` | 13 | copied (8 records) |

Not read by the assembler at all: `01-brief` (contract), `04-orthography`, **`10-materials`**,
`12-rank-rules`, `14-kin-address`, `15-pragmatics`. Three consequences matter for integration:

1. **10-materials is outside the assembly path.** The packet's `materials` block is 11's
   nine local `CMAT-*` records, not 10's 22 `MAT-*` inventory; 10's `era_slots`,
   `grade_ladder`, `writing_media` (`WM-*`), `measures` (`ME-*`) and `gates_interface` never
   reach the packet — even though 08's symbol `medium` strings cite 9 distinct `MAT-*` ids
   and 3 `WM-*` ids, and 11's `maps_to` notes cite `MAT-01/02/05/06/07/10/20/22`.
2. **12-rank-rules is outside the path.** The packet carries no `rank_rules`, so 12's
   `rule_edges` (GAR ids) and its G1–G3 felt-grade ladder (11 `OQ-6`) cannot be evaluated by
   any gate from the packet alone.
3. **04/14/15** are declared out of the base merge both by the assembler's `unresolved` list
   and by their own scope notes.

The assembler's baseline `unresolved` list is the current integration ledger; two entries
were re-checked against bytes:

- "08 symbol domains are structured records and lack explicit medium fields" — **inexact as
  written**: all 10 symbol records carry a top-level `medium:` string (the packet contains 10
  `medium:` keys); it is `domain:` that is the structured sub-record (each carries its own
  `id`, e.g. `STORM-LAW`). The media information exists; only its *form* is heterogeneous.
- "09 era names differ from 05/11 E0-E2 tags and 08 E1-E4 local labels" — confirmed and
  sharpened in §4; note 05 declares four tags (`E0..E3`), not three.

## 2. English labels vs native forms (emic / etic)

| class | field(s) | form | gate treatment |
|---|---|---|---|
| lexicon | `05.lexicon[].term` | native citation form (`ir`, `nel`, `mirken`; 40 records) | `NAME-LEXEME` only; not tested for collisions with names |
| theonyms | `06.pantheon[].name` | native (`Halatu`, `Kahatu`, `Humweha` at baseline) | gate A entity + gate B phonotactics |
| personal/clan names | `13.names[].name` | native (`sunel`, `banwal`) | gate A + gate B |
| era tags | `09.eras` = `E0..E3` | **etic analyst labels**; the in-world names are `09.named_eras` (`Open Grazing`, …, `Still Air (reserved)`, ER-01…ER-09) | gate A treats each tag as a name entity → 6 `NAME-NEAR` "collisions" (`E0` vs `E1` …) |
| garments | `11.costumes[].garment` | **English descriptive strings** ("winter valley coat (heavy felted wool; uncombed finish optional)") | gate B tokenizes them as names → **all 10 `PHON-INVENTORY` failures** (`/v/`, `/c/`, `-`, `(`, `'`) are this class, not language defects |
| symbols | `08.symbols[].sign` | English descriptive labels ("storm-slate (blue-black wool; the storm cloak's dye)") | gate A indexes them; gate B skips symbols (class filter excludes `symbol`) |
| materials | `11.materials[].material` (values), `10.materials[].material` | English slot strings; 10 declares `costume_interface.material_names_to_use` as the exact vocabulary | costume-era gate matches on these strings |

The one genuine native-form phonology failure is `PAN-03 'Humweha'`: `/m/` cannot close a
syllable under the declared coda set `{l,n,r,s}` (frozen `PHON-CODA`). The repair is already
owner-drafted twice at baseline: `05.naming_support.compound` registers `huma` + `weha` →
`humaweha`, and `13-naming.cross_component_repairs` proposes `humaweha` for PAN-03 plus
native citation names for GAR-01..10, explicitly noting that "tools/assemble-d2.py copies
06.name and 11.garment unchanged and does not apply this repair ledger". `05.naming_support
.integration_gap` says the same. 13 also states the English descriptions must move to
`gloss`/`note`, not be deleted, and that "adding name alone does not repair this gate, which
reads garment".

**Do not "fix" the era labels.** `NAME-NEAR` on `E0`/`E1`/… is an artifact of feeding etic
labels into a name-collision gate; renaming eras to clear it would falsify the analyst
vocabulary. The correct disposition is a declared exclusion/whitelist for tag labels.

## 3. Cross-component reference namespaces (counts from baseline bytes)

| namespace | owner | canonical form | references from other components | hazard found |
|---|---|---|---|---|
| `L-01..L-40` | 05 | hyphenated | 11 (16 distinct), 13 (19), 15 (23), 03 (15), 01 (3), 10 (1) | refs are written **unhyphenated** (`L34`, `L35`, `L08`); `L0` in 01 is the lane's L0 surface; `L3-L6` in 12 is a legibility dial — neither is a lexicon id |
| `PAN-01..PAN-07` | 06 | `PAN-` | 13 (3), 01 (1), 07 (7, as its own view) | 07 repeats the theonyms without ids; 13's repair ledger keys them by PAN id |
| `S1..S10` | 08 | bare `S` | 11 cites `S1,S3,S4` (colour readings) | `14` uses `S01..S08` as **its own** avoidance-register row labels, and `MC-S00` is a myth-gate finding code; none of these are 08 symbols. 06's registry note still says the symbols file numbers "S1-S9" although 10 records ship |
| `GAR-01..GAR-10` | 11 | `GAR-` | 12 (10 ids but `garment_refs_note` limits consumption to GAR-01..08), 13 (10, repair ledger), 01 (1) | GAR-09/GAR-10 are unclaimed by rank rules by design — do not treat "no rule references them" as missing data |
| `LEX-GAR-01..10` | 11 (`form_slots`) | `LEX-GAR-` | 13's repair ledger supplies candidate names | every form is `(to-verify)`; 05 owns the lexicon and has not coined them |
| `MAT-01..MAT-22` | 10 | `MAT-` | 08 (9 distinct in `medium` strings), 11 (12 across records/notes) | 10 is not in the packet; ids in the packet resolve only by reading 10 (or 11's `maps_to`) |
| `CMAT-01..CMAT-09` | 11 | `CMAT-` | — | deliberately re-lettered to dodge 10's `MAT-*` space; `CMAT-03` (pack-ox down) and `CMAT-08` (silk) are `maps_to: null` |
| `ER-01..ER-09` | 09 | `ER-` | 11 (5 seams), 12 (5 labels), 06 (`to-verify against ER- records`) | 06's evidence lines stay `to-verify`; 11's ERX-0 says the 09 `costume_seam` fields point at GAR ids and matched "at write time" |
| `WM-*`, `ME-*`, `SKY-*`, `DEG-*`, `WI-*`, `CS-*`, `RT-*`, `BULK-*` | 10 / 12 / 09 / 11 | component-local | `SKY-*` only inside 09; `RT-*` only inside 10 (39 distinct); `WI-*`, `CS-*`, `DEG-*` only inside 11 | none of these reach the packet; any gate or reviewer needing them must read the component |

Registry-vs-dispatch stems are also unresolved: 06's registry notes expect `06-symbols` and
`04-lexicon` while the delivered files are `08-symbols` and `05-lexicon`, and expect a `SYM-`
prefix (`06` OQ-P03); the delivered ids are `S1..S10`.

## 4. Era taxonomy — the load-bearing seam

| component | declared tags | occupied | semantics as written |
|---|---|---|---|
| 01 brief (contract) | `E0–E3` (`contract.era_tags.fixed`) | — | pre-script / script-arrival seam / literate anchor / reserved, plus `alias_rule`: a pre-contract component "may use their own era-tag prefix (e.g. ES0–ES3); each such component declares a one-line mapping to the fixed space in its header, and assembly records the mapping. No mapping is assumed silently." |
| 05 lexicon | `E0–E3` | E0 ×36, E1 ×3, E2 ×1 | knot era / script-arrival seam / literate anchor; E3 reserved |
| 09 eras-calendar | `E0–E3` | 9 named eras | `E0` = 6 named eras (Open Grazing…Bitter Smoke), E1 = Marked Count, E2 = Two Counts, E3 = Still Air (reserved, undated); `era_dates` in non-CE D-coordinates |
| 11 costumes | `E0–E2` | E0 ×7, E1 ×2, E2 ×1 | tags defined by 09; E3 unoccupied |
| 12 rank-rules | `E0–E2` (+ legacy `era-1..3`) | — | E0 = ER-01..06, E1 = ER-07, E2 = ER-08, E3 unoccupied |
| 08 symbols | **`E1–E4`** with local labels shelter/road/assembly/script | — | "Labels are local handles — reconcile with the era component's `eras[]` at integration (PENDING interface)" |
| 10 materials | **`E1–E4`** (shelter/road/assembly/script) | — | E0 appears only in the mythic layer (per `reviews/10-materials.md` M10-R01) |

Owner-declared mapping anchors, quoted from baseline bytes (11 is unmodified in the worktree):

- `11.materials[].CMAT-06.maps_to_note`: 10's record "is excluded in its E1 (shelter) slot and
  this one in E0, **which are the same slot under the era mapping**" → `10-E1 = 11-E0`.
- `11.materials[].CMAT-08.maps_to_note`: 10's anchor-era luxury is `MAT-07 lowland-broadcloth`
  "arriving in its E4 slot = **brief E2**" → `10-E4 = brief E2`.
- Byte-level corroboration: `10 MAT-05` is `excluded_eras: [E1]` with routes `E2–E4`, while
  `11 CMAT-06` (same material slot) is `excluded_eras: [E0]` with routes `E1–E2`.

Those two anchors cannot be reconciled to a uniform shift: a global "−1" would place
`10-E4` at brief `E3` (the reserved, undated slot) and would misdate the anchor-era luxury
import; a global identity would misdate the lowland-cloth exclusion. Four material slots are
compressed onto three occupied contract tags, and the interior (`10-E2`, `10-E3` → `E1`/`E2`)
is undeclared. The frozen round-4 review says the same in its own words: `reviews/10-materials.md`
**M10-R01** — "era slots are not an executable shared chronology … In particular, that proposal
puts script arrival at the target's E2 road seam, earlier than WM-01..03's E4-only media … Do
not merely subtract one from every E-number or move all systems together."

Related unresolved seam: 10 dates writing surfaces `WM-01..WM-03` to its E4 only, while 09 puts
script arrival at its E1 and literacy at E2; the packet carries neither, so no gate can date the
script against 09's tags.

**The contract's own alias rule is unmet.** `01.contract.era_tags.alias_rule` requires any
pre-contract component using its own era-tag prefix to declare "a one-line mapping to the fixed
space in its header", with "no mapping … assumed silently". 08 declares the gap (`era_records[0]`
"reconcile with the era component's `eras[]` at integration (PENDING interface)"; `to_verify`
"Era labels E1-E4 … pending the era component") but provides no mapping line; 10 declares none at
all, and both reuse the letters `E1..E4` without a distinguishing prefix, so the rule's suggested
disambiguator (e.g. `ES0–ES3`) is unavailable as written. The assembler records the conflict
rather than guessing, which is correct — but the packet cannot be called reconciled until the two
mapping lines exist.

Packet-level consequence: `packet.eras` is 09's four tags, while `packet.symbols[].era` strings
stay in 08's local numbering — e.g. `S1` ships as `"E1 bog-dark (…); E2+ storm-slate after
traded indigo arrives"`. A consumer that aligns that string to `packet.eras` will read 08's
shelter era as 09's script-arrival era. The assembler copies both verbatim; nothing in the
packet declares the offset.

## 5. Material ↔ language ↔ era couplings (what is asserted, what is only requested)

- **Two REPORT-don't-merge materials** (owner-declared): `CMAT-03 pack-ox down` and
  `CMAT-08 silk`, both `maps_to: null`. 10 supplies the pack-ox's hair as `MAT-03 ox-hair
  cordage` but no down record; 10's anchor-era luxury is `MAT-07 lowland-broadcloth`, not silk.
  11 `OQ-3` requires the integrator to "either extend the inventory or re-letter GAR-06 to
  broadcloth"; `GAR-06.material = "silk"` and `GAR-09.material = "pack-ox down"` therefore do
  **not** appear in 10's `costume_interface.material_names_to_use` — a mechanical consumer
  validating costume materials against 10's list would flag exactly these two records.
- **Garment terms are English, not lexicon entries.** `GAR-01..GAR-10` `form_slot` values are
  all `(to-verify)` against 05 (`LEX-GAR-01..10`). 13's repair ledger builds native citation
  names from owned lexicon ids — e.g. `tolmirken` = `tol` (L-14) + `mirken` (L-35),
  `taskor` = `tas` (L-21) + `kor` (L-25) — verified against 05: L-14 `tol` "the low ground",
  L-35 `mirken` "wool cloak", L-21 `tas` "dried meat", L-25 `kor` "tally-cord". These are
  proposals; 05 has not coined them (its `naming_support` block is marked NON-CANON repair
  support and leaves the 40-record lexicon unchanged).
- **Loan/era coupling is already staged in 05**: `L-27 per` ("the script-mark") is the one
  loan-stage `E2` record; the two remaining `E1` records carry the script-arrival seam. No
  component dates a garment term as a loan; the imported-cloth naming stratum stays an open
  lexical task (13's `garment_scope`, 11's `form_slots_note`).
- **Symbols carry colour/media readings, not gods**: 08's `medium` strings bind each sign to
  material ids and eras; 11's costume records consume `S1`, `S3`, `S4` for hue readings and say
  "hue meaning stays theirs".

## 6. Symbols and gods — no equation exists in the packet (checked)

`08-symbols.yml` contains **zero** `PAN-` ids and **zero** occurrences of any of the seven
baseline pantheon names (`Halatu`, `Kahatu`, `Humweha`, `Kalweha`, `Seratu`, `Suweha`, `Ula`).
Couplings run 08 → `MAT-*`/`WM-*` and 11 → `S1/S3/S4`; 06 references "the symbols component"
without ids (and with a stale id-range note). So the delivered packet asserts no
symbol-equals-god identity and no symbol→deity pointer. Any future mapping of a sign to a
theonym must be declared by the owners as a new edge, not inferred from colour or domain
wording — this is a report about the current state, not a licence to add one.

## 7. Smallest safe integration path (proposal, no canon, no gate changes)

1. **Approve an explicit era mapping table before any merge.** Columns: 09/05/11/12 tags,
   08 labels, 10 slots; constraints = the two owner anchors above; mark `10-E2/E3` and
   `10-E4 ↔ 09-E3` explicitly unresolved, and record that `WM-01..03` dating is E4-only.
   This is what `contract.era_tags.alias_rule` already requires of pre-contract components
   ("a one-line mapping … No mapping is assumed silently"), so the cheapest compliant form is
   one declared mapping line in 08's and 10's headers, recorded by assembly. Exit criterion: no
   consumer applies an assumed shift; the mapping is data, not prose. Do **not** rewrite 08/10
   restoration details or dates to force a fit.
2. **Let the owners apply the drafted label repairs, then regenerate the packet.** PAN-03
   spelling (already in flight in `06`) and `GAR-01..10` citation names with the English
   descriptions preserved in `gloss`/`note` (11). Only after regeneration can the 11 phonology
   failures clear; they must not be suppressed, waivered, or hidden by an assembler-side
   rewrite.
3. **Decide the CMAT↔MAT material join with the two REPORT-don't-merge records.** Either
   extend 10's inventory (down, silk) or re-letter `GAR-06`/`GAR-09`; do not silently union
   10's 22 records with 11's 9 and do not let a label-matching union create a third luxury
   import.
4. **Add a reference normalizer before any mechanical closure check**: `L34`↔`L-34`,
   `S01..S08` (14) and `MC-S*` excluded from the 08 symbol space, `06-symbols`↔`08-symbols`
   stem aliasing, `04-lexicon`↔`05-lexicon`.
5. **Keep 04/12/14/15 out of the packet** until their owners hand off (the assembler's
   `unresolved` list already records this); if rank rules must become machine-checkable,
   12 must publish an executable block rather than have a consumer re-derive it from prose.
6. **Correct the assembler metadata note about symbol media** at the next generator touch
   (it is a description defect in `assembly.unresolved`, not a data defect); parent owns the
   file.

## 8. Reconciliation notes for the parent (calibration)

- Frozen round-4 finding census, counted from the committed files: naming gate 18
  (10 `PHON-INVENTORY`, 6 `NAME-NEAR`, 1 `PHON-CODA`, 1 `CROSS-HOLD`; the round-3 file had 20
  = 10 + 8 `DERIV-HOLD` + 1 + 1, so `DERIV-HOLD` retired and `NAME-NEAR` is new) and phonology
  gate 3 (`A-NEUTRAL`, unchanged from round 3). The round-4 `costume-era`, `lexicon-coverage`
  and `myth` outputs are **0 bytes**, so the commit message's "34->24 findings, 2 classes
  eliminated" is not reconstructible from the frozen gate bytes alone (34→21 if the empty
  files mean zero findings). Flagged for the calibration axis; no correction asserted here.
- The round-4 review's pinned digests for 09/11 (`540a9339…`, `b6e2c5c2…`) are **identical** to
  the digests the baseline packet pins in `assembly.source_sha256` for the same files — the
  review and the packet were built from the same component revisions.
- No erratum was appended to `corpus/knowledge/synthesis/era-myth-language-costume-matrix.md`:
  all five rechecked claim classes came back supported (see the JSON record), so there is
  nothing to correct in that entry.

Limits: the Met's human-facing page returned HTTP 429 from this environment (the official
collection API JSON was used instead); WebSearch was quota-blocked, so every recheck used a
direct fetch of an institutional or open scholarly source. I ran no gate that writes files and
edited no component, gate, packet, or bookkeeping file.
