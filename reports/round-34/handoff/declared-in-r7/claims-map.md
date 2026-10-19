# Handoff v3 — the D4 claim rows (`D4-CL01`…`D4-CL12`)

- topic: The exact D4 claim rows the v3 packet's `claim_ledger` must carry:
  statement, contract §6 claim kind, evidence status, `uncertainty
  {status, basis}` in the v2 clause grammar, and the link specs that resolve
  into `examples/culture-d4/` records and the round-18 receipts. This file is
  the packet seat's copy surface; the status rationale is `uncertainty-plan.md`,
  the envelope design is `design.md`.
- sources: `examples/culture-d4/{brief.md,packet.d4.yml,typed-labels.d4.yml,
  packet.d4.typed.yml,expected-holds.json}`; `examples/culture-d4/components/
  01-brief.yml` (`contract.hold_set_declaration`, `registry`),
  `08-eras.yml`, `09-costumes.yml`, `12-provenance.yml`;
  `reports/round-18/d4/{holds.md,determinism.md,manifest.md,replay.md}`;
  `reports/round-19/validation.json`; `tools/assemble-d4-typed.py`;
  `tools/harness/packet_links.py` (resolver whose rules the specs obey).
- couples: `design.md` §2/§4 (rules 1–4 and the D4-CL08 flip rule);
  `uncertainty-plan.md` (census, grammar, owner routing); the packet seat
  renders these rows into `packet-v3-*.{md,yml}`; the audit seat re-resolves
  every spec.
- taken-from: the delivered D4 bytes and receipts, read on 2026-10-18; no D4
  fact is asserted that `design.md` §8 did not measure, and no real-world
  referent, date, clearance or canon standing is claimed by any row.
- verified-at: 2026-10-18 — the twelve rows as written in this file were
  re-extracted from the markdown and run through
  `tools/harness/packet_uncertainty.py --claims-json … --json`: exit 0,
  `claims=12 findings=[]`; the union of the link lines below (46 unique specs,
  re-extracted from this file) resolved by `tools/harness/packet_links.py
  --links "<46 specs>"`: exit 0, `links=46 resolved=46 findings=0`, and the
  coverage map's 18 cited record ids resolved too (`18/18`); the earlier
  48-spec draft list also resolved `48/48` (`review.md` §2–§3 record the
  commands and the five negative controls that fired their codes).
- **post-filing update (2026-10-18, later stamp):** the O seat's per-family
  alias work landed in the working tree while this file was being written, so
  the `D4-CL08` row below is typed in its **landed** form (`supported`) and the
  census moves to **16 supported / 7 partial / 4 unresolved** (v2's 8/5/2 plus
  D4's 8/2/2). The pre-flip form and the measured evidence are recorded in the
  row's flip record and in `review.md` §4; the rule is symmetric — a revert of
  the O bytes re-flips the row to `unresolved` with `OQ-V3-04` re-opened in a
  new build.
- recheck: whenever an `examples/culture-d4/**` byte, a D4 tool or gate, or a
  round-18 D4 receipt cited here changes; before the v3 packet is frozen;
  whenever the O seat's alias bytes move (the status is evidence-keyed and
  symmetric — a reverted O byte re-flips the row, never a silent edit).

## 1. The rows

Notation: `u.status` is the `uncertainty.status`; `u.basis` is quoted in full
because the clause grammar (`grounding:` always, `restriction:` iff `partial`,
`open:` + `owner:` iff `unresolved`) is what the validator parses. Every link
spec is written **fully qualified** (`path#token`) — no shorthand — because the
resolver and the packet seat both consume the specs literally; every token
below was measured present in its file (2026-10-18).

### D4-CL01 — designer interpretation — invented — `supported`

- **statement:** The D4 furnace-league drill is a fourth non-canon example
  culture assembled through the typed pipeline: thirteen authored components, a fictional basin league with furnace-right rank, an isolate speech with one
  unmodelled sister variety, and no real-world community, language, craft
  tradition or rights question described anywhere in its records; the drill is
  a design record only, and canon standing is not its to give.
- **u.basis:** `grounding: examples/culture-d4/brief.md canon-boundary block and examples/culture-d4/packet.d4.yml#canon, both worded "not canonized (D4 NON-CANON design drill)", with the thirteen authored inputs listed by the component registry examples/culture-d4/components/01-brief.yml#C-01; the drill's own records carry the design-only scope and refuse any canon standing, and no real-language clearance or rights ruling is claimed anywhere`
- **links:** `examples/culture-d4/brief.md`, `examples/culture-d4/packet.d4.yml#canon`, `examples/culture-d4/components/01-brief.yml#C-01`

### D4-CL02 — generative rule — invented — `supported`

- **statement:** D4 stages its own history in four fixture-relative era tags
  E0–E3: ER-01 "the stamp era" (E0, pre-script), ER-02 "the mark hand" (E1,
  the script seam), ER-03 "the league" (E2, the literate anchor) and ER-04
  "the cold fire" (E3, reserved and unoccupied); each era record declares its
  institution seam, language stage, record stage and costume seam, and no
  absolute date is claimed for any of them.
- **u.basis:** `grounding: examples/culture-d4/packet.d4.yml#era_records, four records ER-01..ER-04 on tags E0..E3 whose ER-04 note reads "reserved and unoccupied", with examples/culture-d4/packet.d4.yml#named_eras and the contract era_tags block; examples/culture-d4/brief.md declares the tags fixture-relative rather than BCE/CE, and no delivered record dates an era`
- **links:** `examples/culture-d4/packet.d4.yml#era_records`, `examples/culture-d4/packet.d4.yml#ER-01`, `examples/culture-d4/packet.d4.yml#ER-04`, `examples/culture-d4/packet.d4.yml#era_tags`, `examples/culture-d4/packet.d4.yml#named_eras`, `examples/culture-d4/components/08-eras.yml`

### D4-CL03 — generative rule — invented — `supported`

- **statement:** Rank in D4 is furnace right, not wealth: RK-01…RK-04 declare
  authority, jurisdiction, era set, rite, the property a rule governs (kind and
  value) and the effect, and the permitted wearer ranks are the same rank names
  the garment records carry — the drill's seed text states the rule and the
  delivered records implement it.
- **u.basis:** `grounding: examples/culture-d4/packet.d4.yml#rank_rules, RK-01..RK-04 each declaring authority, jurisdiction, era set, rite, property and wearer ranks, plus the garment records' own wearer_ranks values in examples/culture-d4/packet.d4.yml#costumes; the brief's seed text states rank is furnace right, not wealth alone, and every delivered record carries evidence "design-choice"`
- **links:** `examples/culture-d4/packet.d4.yml#rank_rules`, `examples/culture-d4/packet.d4.yml#RK-01`, `examples/culture-d4/packet.d4.yml#RK-04`, `examples/culture-d4/packet.d4.yml#GAR-01`, `examples/culture-d4/components/09-costumes.yml`

### D4-CL04 — generative rule — invented — `partial`

- **statement:** Every delivered D4 garment record (GAR-01…GAR-06) owes its
  term through a form slot LEX-GAR-01…LEX-GAR-06 whose status is `unfilled`:
  the garment's own string is an English gloss riding as a translated label off
  the sound channel, no garment term is delivered, five slots owe a
  native-form, and LEX-GAR-06 — the imported-cloth coat — owes a
  borrowed-strata term whose delivery route is left to a lexicon decision.
- **u.basis:** `grounding: examples/culture-d4/packet.d4.yml#form_slots, six slots LEX-GAR-01..LEX-GAR-06 each owned by a garment record and each status "unfilled", with the gloss riding as a translated label per examples/culture-d4/typed-labels.d4.yml#labels_by_kind; restriction: five slots owe a native-form and LEX-GAR-06 owes a borrowed-strata term whose delivery route the slot's own note leaves to a lexicon decision, so the debt is certain while the sixth slot's owed kind is conditional`
- **links:** `examples/culture-d4/packet.d4.yml#form_slots`, `examples/culture-d4/packet.d4.yml#LEX-GAR-01`, `examples/culture-d4/packet.d4.yml#LEX-GAR-06`, `examples/culture-d4/typed-labels.d4.yml#labels_by_kind`

### D4-CL05 — designer interpretation — derived projection (author-side) — `supported`

- **statement:** The D4 typed channel types 82 labels — 64 native-form, 12 translated-label, 6 borrowed-strata — and carries 12 findings, all of them holds (12 label holds, 0 label fails); the committed projection is the
  projector's own deterministic output, and its check leg reports byte-identity
  rather than a re-derivation.
- **u.basis:** `grounding: examples/culture-d4/typed-labels.d4.yml#coverage (typed_labels 82, labels_by_kind native-form 64 / translated-label 12 / borrowed-strata 6, findings_total 12, findings_hold_or_fail 12, label_findings_fail 0) and examples/culture-d4/typed-labels.d4.yml#stats (fail 0, hold 12, labels 82), re-read from the delivered bytes; the projection is the projector's own output and the check leg reports byte-identical determinism`
- **links:** `examples/culture-d4/typed-labels.d4.yml#coverage`, `examples/culture-d4/typed-labels.d4.yml#labels_by_kind`, `examples/culture-d4/typed-labels.d4.yml#stats`, `examples/culture-d4/typed-labels.d4.yml#typed_labels`, `tools/gates/d4-typed-labels-check-gate.py`

### D4-CL06 — designer interpretation — derived projection (author-side) — `supported`

- **statement:** The committed D4 hold set is 12 holds, 0 notes and 0 fails, pinned to the delivered bytes: twelve `D2L-FORM-UNRESOLVED` holds keyed to each garment twice (record id and slot id — `GAR-01..GAR-06` and `LEX-GAR-01..LEX-GAR-06`); the emitted set equals the committed file, and the round-17 brief's six-row declaration is reconciled by a documented +6 hold / +0 note delta rather than absorbed or silently re-declared.
- **u.basis:** `grounding: examples/culture-d4/expected-holds.json#counts (hold 12, note 0, fail 0) with the row list, whose holds are twelve D2L-FORM-UNRESOLVED rows keyed to each garment twice (GAR-01..GAR-06 and LEX-GAR-01..LEX-GAR-06); the emitted set equals the committed file, its own revision_note records that the hold set is unchanged at 12 holds / 0 notes / 0 fails since the round-28 law-replay build, and reports/round-18/d4/holds.md's reading of 15 holds / 1 note stands filed as a superseded measurement rather than absorbed`
- **links:** `examples/culture-d4/expected-holds.json#counts`, `examples/culture-d4/expected-holds.json#holds`, `examples/culture-d4/components/01-brief.yml#hold_set_declaration`, `reports/round-18/d4/holds.md`

### D4-CL07 — designer interpretation — derived projection (author-side) — `supported`

- **statement:** The D4 projection's era and material reconciliation resolves
  all six garment records by declared row and slot identity — each record's era
  block tagged in scope, each material block resolved to a `CMAT` record — with
  zero findings, while the reconciliation carries six reconciliation records and the file's coverage block counts zero conflicts and zero quarantine handles — carried as measured counts rather than asserted away.
- **u.basis:** `grounding: examples/culture-d4/typed-labels.d4.yml#era_material_reconciliation, six records GAR-01..GAR-06 each carrying an era block tagged E0 or E1 and a material block resolved by slot identity to a CMAT record, summary claims 6 findings 0; the same file's examples/culture-d4/typed-labels.d4.yml#reconciliation_records and examples/culture-d4/typed-labels.d4.yml#conflicts counts carry six reconciliation records and zero conflicts, taken as measured rather than collapsed`
- **links:** `examples/culture-d4/typed-labels.d4.yml#era_material_reconciliation`, `examples/culture-d4/typed-labels.d4.yml#R-MAT-RESOLVED`, `examples/culture-d4/typed-labels.d4.yml#reconciliation_records`, `examples/culture-d4/typed-labels.d4.yml#conflicts`, `examples/culture-d4/packet.d4.yml#materials`

### D4-CL08 — designer interpretation — derived projection (author-side) — `supported`

- **statement:** The D4 packet declares no legacy era-alias handles of its own:
  every delivered era value is already a canonical E0–E3 tag from the packet's
  own era space, and the projection's alias leg now resolves **family-local** —
  it reads the D4 packet's own era records and declares an explicit documented
  skip instead of reading another family's component, so the cross-family read
  the round-19 routing note recorded is closed on the live bytes.
- **u.basis:** `grounding: examples/culture-d4/typed-labels.d4.yml#era_reconciliation, whose basis now names examples/culture-d4/packet.d4.yml named_eras (A1) and the explicit skip "the packet declares no reconciliation rows (the D2 leg's examples/culture-d2/components/11-costumes.yml is not read for family d4)", with alias_rows 4 and examples/culture-d4/packet.d4.yml#era_tags carrying the canonical E0-E3 tags; the run evidence is tools/assemble-d4-typed.py --selftest exit 0 with 12/12 checks in a mirror that copies only examples/culture-d4, and the unchanged-foreign-path control is tools/d2-typed-labels.py --selftest exit 0 163/163 plus tools/gates/typed-pipeline-gate.py over examples/culture-d2/packet.d2.typed.yml exit 0 13/13 legs with stdout sha256 9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606 equal to the round-18 pre-generalization baseline`
- **links:** `examples/culture-d4/typed-labels.d4.yml#era_reconciliation`, `examples/culture-d4/packet.d4.yml#era_tags`, `examples/culture-d4/packet.d4.yml#named_eras`, `tools/assemble-d4-typed.py`, `tools/d2-typed-labels.py`, `reports/round-18/d4/determinism.md`, `reports/round-19/validation.json`
- **flip record** (`design.md` §4): the **pre-flip form** (filed earlier the
  same day, superseded) was status `unresolved`, grounding the projection's
  then-D2-naming `era_reconciliation.basis` and the adapter's selftest copy of
  the D2 tree, with `open:` the missing per-family resolution and `owner:` the
  kotodama O seat. The landed form above was adopted on measured evidence
  (2026-10-18; the O bytes were uncommitted working-tree edits at measurement
  time, so the packet seat re-runs these legs on the pinned revision before
  freezing). The flip is symmetric: a revert of the O bytes re-flips this row
  to the pre-flip form and re-opens `OQ-V3-04` in a new build.

### D4-CL09 — designer interpretation — derived projection (author-side), holds open — `unresolved`

- **statement:** The D4 projection carries no rank residual of its own: its `rank_rules` block's `act_rules`, `unresolved` and `quarantine` lists are empty and the coverage block counts 0 unresolved rank items, 0 quarantine handles and 0 conflicts, so the D2 normalization residuals (13 unresolved rank items, 3 quarantine handles, 4 conflicts) stay D2's own and are counted on the D2 row rather than restated here; what stays open for D4 is the six garment terms the twelve `D2L-FORM-UNRESOLVED` holds key (claim D4-CL04), and no residual is promoted, resolved or hidden by this packet.
- **u.basis:** `grounding: examples/culture-d4/typed-labels.d4.yml#rank_rules, whose act_rules, unresolved and quarantine lists are empty at the delivered bytes, with examples/culture-d4/typed-labels.d4.yml#rank_rules_unresolved_items 0 and examples/culture-d4/typed-labels.d4.yml#rank_quarantine_handles 0 and examples/culture-d4/typed-labels.d4.yml#conflicts 0 in the same file's coverage block; the D2 normalization residuals (13 unresolved rank items, 3 quarantine handles, 4 conflicts) are counted on the D2 channel in this packet's own D2 fact row rather than restated as D4 debt; open: the six garment terms stay owed through twelve D2L-FORM-UNRESOLVED holds (claim D4-CL04), and no rank or form residual is promoted or hidden by this packet; owner: kotodama, blocking for the affected D2 rank records and the six garment terms, not for this envelope`
- **links:** `examples/culture-d4/typed-labels.d4.yml#rank_rules`, `examples/culture-d4/typed-labels.d4.yml#rank_rules_unresolved_items`, `examples/culture-d4/typed-labels.d4.yml#rank_quarantine_handles`, `examples/culture-d4/typed-labels.d4.yml#conflicts`

### D4-CL10 — designer interpretation — invented — `partial`

- **statement:** D4's loan and contact material is declared unmodelled where
  unmeasured: the borrowed-strata labels carry the full borrow ledger (layer,
  donor, donor form, substitutions, entry stage, referent-available-from),
  while the donor's own stage, the imported cloth's fibre and the salt-road
  towns' speech are marked unmodelled or `(to-verify)`; no real-world donor
  language is named, and no contact history is dated.
- **u.basis:** `grounding: examples/culture-d4/packet.d4.yml#provenance PR-01..PR-09 declaring every comparator a repo corpus entry by path and section, with the loan ledger's donor_stage and unmodelled markers carried in the packet's own lexicon and contact lines; restriction: the supported remainder is the ledger's declared completeness (layer, donor, donor_form, substitutions, entry_stage, referent_available_from) while the donor stage, the fibre and the donor speech stay unmodelled or (to-verify), so no contact history is dated`
- **links:** `examples/culture-d4/packet.d4.yml#provenance`, `examples/culture-d4/packet.d4.yml#donor_stage`, `examples/culture-d4/packet.d4.yml#unmodelled`, `examples/culture-d4/packet.d4.yml#CT-01`, `examples/culture-d4/packet.d4.yml#LY-01`, `examples/culture-d4/components/12-provenance.yml`

### D4-CL11 — screening statement — invented — `supported`

- **statement:** No real-language sweep, novelty check, community consultation
  or rights ruling has been performed or claimed for any D4 spelling: the
  provenance rows declare every comparator a repo corpus entry cited by path
  and section, the naming component records that the cross-culture review is a
  self-check only, and no clearance may be inferred from this packet.
- **u.basis:** `grounding: examples/culture-d4/packet.d4.yml#PR-04 recording that no real-language collision sweep was performed and the cross-culture review is a self-check only, with the packet's provenance rows stating that no real-world source, community or rights question is described or decided; the absence as worded is supported and the clearance question itself is routed to the packet's open questions, not carried by this status`
- **links:** `examples/culture-d4/packet.d4.yml#PR-04`, `examples/culture-d4/packet.d4.yml#provenance`, `examples/culture-d4/components/05-naming.yml`

### D4-CL12 — candidate world-fact — candidate world-fact — `unresolved`

- **statement:** The D4 culture is carried as namespaced candidates only: the
  drill names lore-shokunin as the recipient of a design record, its questions
  stay undecided in its own provenance rows, and no lore entity key, baseline
  bible revision or receipt surface exists — so its names cannot be imported as
  canon without a lore baseline and a new reviewed handoff.
- **u.basis:** `grounding: examples/culture-d4/brief.md and examples/culture-d4/components/01-brief.yml#handoff_recipient naming lore-shokunin as the recipient of a design record, with examples/culture-d4/packet.d4.yml#provenance declaring the drill's questions undecided; open: no lore baseline revision, entity key or receipt surface exists for the D4 culture, so its namespaced candidates cannot be imported as canon without a lore baseline and a new reviewed handoff; owner: lore-shokunin, non-blocking for this envelope`
- **links:** `examples/culture-d4/brief.md`, `examples/culture-d4/components/01-brief.yml#handoff_recipient`, `examples/culture-d4/packet.d4.yml#provenance`

## 2. Record coverage map

The v2 coverage rule (every delivered record id appears in ≥1 claim link or
edge target) is kept, with the v2 mechanism for the remainder: the
`artifact_manifest` `record_ids` index. Measured D4 inventory (2026-10-18,
`design.md` §8.1): **153 distinct namespaced record ids** over 22 families plus
14 contract rules.

| family | delivered | carried by a claim link or edge family in this file |
|---|---|---|
| lexicon `L-01..L-54` | 54 | edge family `costume→slot`/`loan→layer`; `examples/culture-d4/packet.d4.yml#L-49` (the loan ledger row) is the named witness for D4-CL10 |
| names `NM-01..NM-08` | 8 | edge family `name→formation/bases` |
| pantheon `PAN-01..PAN-06` | 6 | manifest `record_ids` index |
| symbols `SYM-01..SYM-08` | 8 | edge family `symbol→era/register` |
| costumes `GAR-01..GAR-06` | 6 | D4-CL04 links (`#GAR-01`, `#GAR-06`), D4-CL07 (all six via the reconciliation block) |
| materials `CMAT-01..CMAT-05` | 5 | D4-CL07 (`#materials`, `#R-MAT-RESOLVED`) |
| rank rules `RK-01..RK-04` | 4 | D4-CL03 links |
| eras `ER-01..ER-04` (+ tags E0–E3) | 4 + 4 | D4-CL02 links |
| form slots `LEX-GAR-01..06` | 6 | D4-CL04 links |
| provenance `PR-01..PR-09` | 9 | D4-CL10/D4-CL11 links |
| festivals / rites / motifs / narratives / roles / calendar | 6/4/4/3/6/1 | edge family `festival|rite→calendar`; manifest `record_ids` index |
| contact / routes / layers / cloth sources / constructions | 2/3/2/2/3 | D4-CL10 links (`#CT-01`, `#LY-01`); manifest `record_ids` index |
| cross-culture review `CC-01..CC-03` | 3 | D4-CL11 (the self-check statement) via `components/05-naming.yml`; manifest index |
| contract rules `RG-01..RG-14` | 14 | manifest `record_ids` index |

The packet's `validation` must carry the measured coverage row (declared vs
carried, with the manifest-index remainder named) exactly as v2 does — a count,
not a claim.

## 3. D4 coupling-edge families (atomic rows; counts re-measured at build time)

One atomic edge per live relation, each with `source`, `relation`,
`mechanism`, `limits`, `applicability`, concrete `target_ids` and a `claims`
back-link (the v2 shape; no aggregate rows):

| family | live count measured 2026-10-18 | example targets | back-link |
|---|---|---|---|
| costume → its form slot | 6 (each costume carries `form_slot`) | `GAR-01` → `LEX-GAR-01` | D4-CL04 |
| costume → its material record | 6 (`material_ref`) | `GAR-01` → `CMAT-01` | D4-CL07 |
| rank rule → permitted wearer ranks | 4 (`wearer_ranks`) | `RK-01` → smith/furnace-master | D4-CL03 |
| era record → costume seam requirement | 4 (`costume_seam`) | `ER-02` → the league cloak's seam | D4-CL02 |
| borrowed-strata label → its layer/entry stage | 6 label rows | `L-49` → Salt-road trade layer, E1 | D4-CL10 |
| name → formation/bases | 8 name records | `NM-01` → its base lexeme | manifest index + D4-CL01 scope |
| symbol → era/register | 8 symbol records | `SYM-01` → its era and register | manifest index |
| festival/rite → calendar unit | 10 records | `FES-01`/`RIT-01` → `CAL-01` | manifest index |
| contact layer → route | 2 layers, 3 routes | `CT-01` → `RT-01` | D4-CL10 |

Edges inherit status severity per the v2 rule: an edge derived from a
`partial`/`unresolved` claim carries at least that status (D4-CL10's edges are
`partial`; the loan edges under D4-CL09's residuals stay `unresolved`).

## 4. Open-question rows for the unresolved D4 claims (`--require-oq`)

Each `unresolved` claim must be referenced by an `open_questions` row (the
harness leg runs with `--require-oq`; zero findings required):

| id | question | unresolved_claims | lane / blocking |
|---|---|---|---|
| `OQ-V3-04` *(closed)* | the projector's era-alias leg read a foreign family's component for D4 packets (round-19 routed wart); **closed** by the O seat's landed per-family resolution, measured and controlled in `review.md` §4 — the id is retained only as the re-open id if the O bytes are reverted | `D4-CL08` is now `supported`, so `--require-oq` no longer requires this row | kotodama O seat |
| `OQ-V3-05` | D4's own holds stay open: 12 form holds, 0 notes, 0 fails; the projection carries 0 unresolved rank items, 0 quarantine handles and 0 conflicts (the 13/3/4 residuals are D2's, counted on the D2 row) | `D4-CL09` | kotodama; blocking for the affected D2 rank records and the six garment terms, not for this envelope |
| `OQ-V3-06` | no lore baseline revision, entity key or receipt surface exists for the D4 culture | `D4-CL12` | lore-shokunin; non-blocking |

The v2 rows `OQ-V2-01..07` carry forward unchanged (D2/D3 screening, the
bilateral read, D2 residuals, the belief truth question, the bridge supports,
the separate-fixtures note, and the builder/freeze process row — the last of
which v3 supersedes in kind, since the v3 exercise now *is* the builder; the
packet seat should say so in that row's text rather than delete it).

## 5. Measured controls (see `review.md` for commands and raw output)

- `packet_uncertainty.py --claims-json <the twelve rows re-extracted from this
  file> --json` → exit 0, `claims=12 findings=[]` (pre-flip census 7 supported /
  2 partial / 3 unresolved; the post-flip re-extraction is recorded in
  `review.md` §2 row 19).
- `packet_links.py --links "<the union of the link lines above>"` → exit 0,
  every spec resolved (`46/46` on the pre-flip link set; the post-flip set is
  re-measured in the same `review.md` row), and the coverage map's 18 cited
  record ids resolved too (`18/18`).
- Negative controls: duplicate basis → `U-BASIS-DUPLICATE`; `partial` without
  `restriction:` → `U-BASIS-NO-RESTRICTION`; `unresolved` without `owner:` →
  `U-BASIS-NO-OWNER`; status `tentative` → `U-STATUS-VOCAB`; basis
  `grounding: unknown` → `U-BASIS-SHORT`; dangling selectors `#ER-99` and
  `#no_such_block` → `L-TOKEN-MISSING` (exit 1). Every claim above carries a
  control that fires when its witness is absent.
