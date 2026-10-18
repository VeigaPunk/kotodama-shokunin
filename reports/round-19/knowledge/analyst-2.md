> 2026-10-18 integrator erratum: the reviews' red measurements (L2-channel fail; adapter selftest 1/4) were pre-repair states — the integrator's L2-family patch and the adapter bytes fix landed after the review seats measured. Re-verified at close: typed gate 19/19 exit 0; adapter selftest green. Defect A correction: greens cited from runs over the untyped packet now name the typed run explicitly. Defect B (two wrong leg names in skill-draft-b) corrected to the legs the gate actually emits.

# R19-D02 — craft analysis 2/3: the slot-label routing model (two carriers per garment)

- round: 19 (operator loop 2 of 3, build round 3 of 4; `reports/round-19/claims.json`,
  claim **D**, shard **D02**). Lane: `kotodama-shokunin`.
- assignment (verbatim): "D R19-D01..D03 (craft analysts x3): mine rounds 17-18 D4
  artifacts … for codifiable craft rules: register-scoped slot routing; derivation replay
  requirements; **the slot-label routing model**; the text-transform rule.
  reports/round-19/knowledge/analyst-{1..3}.md."
- this file: **the slot-label routing model** — how a D4 costume is keyed twice (record id
  and slot-label id), why both are first-class routing carriers, and how the landed gate
  reconciles them. Siblings: `analyst-1.md` (register class), `analyst-3.md` (derivation
  replay + text-transform).
- date: 2026-10-18; readings 11:3xZ. Baseline revision
  `e5718945a1ab0a0c3db955338d2cae77d68fd348`.
- canon: NON-CANON engineering evidence.
- writes: **this file only**. Rounds 8–18 read-only; no tool/packet/baseline byte edited.
  No commit, no push.
- status: **analysis complete; the model is delivered and gate-verified** (12 routing rows,
  6 field moves, `L3-routing-consistency` green).

## 0. The rule in one sentence

**A form-bearing costume is keyed twice — once by its record id and once by its
slot-label id — and both keys are first-class routing carriers**: each produces its own
`typed_channel` row and its own hold, while the owed slot is named **once**, on the slot's
own row (`tools/assemble-d4-typed.py:168-249`).

## 1. The model, stated from the adapter (executable authority)

`tools/assemble-d4-typed.py` (sha256
`087846719041db0ba32c005a34a6075c452e122a1f7b7bc4527ae4e0bfc4d798`, 11:32Z),
`build_typed_packet` (`:161-272`):

1. **Two indices over the same costume.** The adapter builds `costume_ids` (record ids) and
   `slot_owner` (the `form_slot` string → owning record id) from `doc["costumes"]`
   (`:177-186`). For each costume it collects `entries = by_record.get(rid)` **and**
   `slot_labels = by_record.get(slot)` (`:196-201`) — the projector has typed the
   `form_slot` as its own `translated-label` whose `source.record` is the owed-slot id
   (`:170-175`).
2. **Both keys enter the typed set.** `typed_ids.add(rid)` and, when a `form_slot` exists,
   `typed_ids.add(slot)` (`:210-212`).
3. **One routing row per routed label.** For every label in `all_labels` whose kind is in
   `ROUTED_KINDS = ("translated-label",)` (`:65`, `:213-241`) a routing row is appended,
   keyed `record_key = label.source.record or rid`. Both the garment-field label and the
   slot label are lawful carriers — the adapter comment says so explicitly (`:170-175`):
   "Both labels are first-class routing carriers … Slot-keyed records are lawful carriers,
   not coverage gaps."
4. **The owed slot is named once.** `owed_slot` is set **only** on the row whose
   `record_key == slot` (`:236-240`); the record-keyed row carries `owed_slot: null`. The
   comment: "the owed slot is named once per costume — on the slot's own routing row; the
   gate compares slot sets."
5. **Fail-closed coverage.** An untyped garment record is a problem, not an exemption
   (`:205-209`); a routing row naming a record absent from the costume ledger and not a
   slot owner is a problem (`:242-249`); any problem exits **2** (`:31-38`, `:359-365`).

## 2. What the delivered tree carries (measured, 2026-10-18)

| subject | command | observed |
|---|---|---|
| routing rows | `sed -n '2678,2800p' examples/culture-d4/packet.d4.typed.yml` | **12 rows**: 6 keyed `GAR-01..06` (`owed_slot: null`) + 6 keyed `LEX-GAR-01..06` (`owed_slot: "LEX-GAR-01..06"`) |
| field moves | same region | all 12 rows `off_channel_field: "garment_gloss"`; **6 costumes, 6 moves** |
| emitted holds | `python3 -c` read of `examples/culture-d4/expected-holds.json` (`09490a27…`) | `{hold: 15, note: 1, fail: 0}`; 12 × `D2L-FORM-UNRESOLVED` at `GAR-0n` + `LEX-GAR-0n`, 3 × `D2L-RANK` |
| the reconciliation statement | `reports/round-18/d4/scribe-7.md:85-89` | "the projector keys the same six slots twice (record id and slot-label id)" |

So the "2-labels-per-garment typed shape" the claim names is a **delivered fact**: 6 garments
→ 12 routing rows → 12 holds, while the sound-channel differential removes exactly **6**
artifacts (`reports/round-18/` D verdict: "routing consistency (12 rows: 6 garment + 6 slot,
owed slots named once); channel differential exactly the 6 PHON-INVENTORY artifacts
removed").

## 3. The gate's reconciliation (executable authority)

`tools/gates/typed-pipeline-gate.py` (sha256 `04ad4bb4…`):

1. **Row count ≠ move count.** `L2-channel` compares removed artifacts against the moved
   records that are **costume records** (`:656-673`), precisely because two rows share one
   field move. The comment (`:660-663`): "D4 family: two routing rows per costume
   (garment-field row + owed-slot row) but exactly one field move per costume."
2. **`L3-routing-consistency`** (`:736-753`) is the model's own leg: it reads the hold id
   **off the routing rows** (`routing_hold_ids`, `:741-742`), collects the finding `where`s
   (`hold_records`) and the finding `label_id`s (`hold_slots`, `:744-747`), collects the
   routing rows' `owed_slot`s (`routed_slots`, `:748-749`), and requires
   `hold_records == moved_records and hold_slots == routed_slots` (`:750-753`). A dropped
   routing row, or a hold without its routing row, is a defect.
3. **`owed_slot` extraction** — `OWED_SLOT_RE = re.compile(r"\s*([A-Za-z][A-Za-z0-9]*(?:-[A-Za-z0-9]+)*-\d+)")`
   (`tools/assemble-d4-typed.py:68`), applied by `owed_slot()` (`:100-104`) to the
   `form_slot` string, which may carry a trailing qualifier (`"LEX-GAR-99, (to-verify)"` —
   see the adapter selftest `:467-477`). The slot id, not the raw `form_slot` text, is the
   routing key.

## 4. Codifiable craft rules (for the D-axis SKILL.md decision-table row)

| # | rule | citation | control |
|---|---|---|---|
| R6 | Key a form-bearing record by **both** its record id and its slot-label id; both are lawful routing carriers. | `assemble-d4-typed.py:170-175`, `:196-201`, `:210-212` | delivered packet: 12 rows (`packet.d4.typed.yml:2678-2800`) |
| R7 | Name the owed slot **once**, on the slot's own row; the record-keyed row carries `owed_slot: null`. | `assemble-d4-typed.py:236-240` | gate `L3-routing-consistency` compares slot sets (`:748-753`) |
| R8 | Count sound-channel moves against **costume records**, never against routing rows. | `typed-pipeline-gate.py:656-673` | delivered run: 12 rows, 6 moves, 6 removals |
| R9 | Every moved routing record carries exactly one off-channel hold, and every such hold names a moved routing record. | `typed-pipeline-gate.py:736-753` | dropped-row control `:975` (deletes `owed_slot` ⇒ red) |
| R10 | A garment record the projector did not type is a **coverage problem** (exit 2), never a silent exemption; a routing row naming an unknown record is likewise exit 2. | `assemble-d4-typed.py:205-209`, `:242-249` | adapter selftest unit controls `:454-466` |
| R11 | Slot cardinality generalizes to **exactly one supplied checked form per (owner, slot_ref)**, with the register pair carried as a packet fact (`doublet_of`); two supplied forms in one slot ⇒ exit 2 `D4L-DATA`. | `design-brief.md:283-295` (Δ2) | design control C-07 `design-brief.md:461` |

## 5. Forecast vs delivered

- **Delivered**: R6–R10 on the D4 packet (class-1 gloss rows), with the gate's
  `L3-routing-consistency` and `L2-channel` legs green.
- **Forecast (mark `(to-verify)`)**: R11's `doublet_of` pair relation and the `<id>#plain` /
  `<id>#quote` slot pair are design-brief Δ2 — the delivered packet carries **no** `doublet`
  token at all (`grep -c "doublet" examples/culture-d4/packet.d4.yml` → **0**, 2026-10-18);
  the register class that would populate `#plain`/`#quote` slots is unbuilt (see
  `analyst-1.md` §5).

## 6. Destination

- **D-axis SKILL.md**: extend the label-typing decision table (`SKILL.md:31-60`) with the
  dual-key carrier row and the "moves, not rows" counting rule; the executable authority is
  the adapter (`assemble-d4-typed.py:161-272`) plus the gate's `L2-channel` /
  `L3-routing-consistency` legs.
- **Corpus lesson**: the D4 lesson entry records the 12-row / 6-move / 6-removal arithmetic
  with the counting command, and R6–R10.

## 7. Limits

- Readings bind to the shas/stamps above; a later edit to the adapter, packet or gate is a
  re-read event.
- R11's pair relation is design-forecast, not delivered; the codification must not present
  `doublet_of` as a live packet fact.
- The reconciliation of the round-17 forecast ids to the emitted `D2L-*` vocabulary is
  `reports/round-18/d4/holds.md` / `scribe-7.md`; this file cites it, does not re-decide it.
