# R19-D01 — craft analysis 1/3: register-scoped slot routing (the on-channel-but-slot-inadmissible class)

- round: 19 (operator loop 2 of 3, build round 3 of 4; `reports/round-19/claims.json`,
  claim **D**, shard **D01**). Lane: `kotodama-shokunin`.
- assignment (verbatim): "D R19-D01..D03 (craft analysts x3): mine rounds 17-18 D4
  artifacts (design docs, gate design §11, adapter code, SCORECARD sections) for
  codifiable craft rules: register-scoped slot routing; derivation replay requirements;
  the slot-label routing model; the text-transform rule.
  reports/round-19/knowledge/analyst-{1..3}.md."
- this file: **register-scoped slot routing** — the second routing class the D4 exercise
  named, what state it creates, how the landed gate classifies it, and what a craft rule
  must say. Siblings: `analyst-2.md` (slot-label routing model), `analyst-3.md`
  (derivation replay + text-transform).
- date: 2026-10-18; readings 11:2x–11:3xZ. Baseline revision
  `e5718945a1ab0a0c3db955338d2cae77d68fd348` (`reports/round-19/claims.json`).
- canon: NON-CANON engineering evidence. Nothing here is a canon record, a lore handoff,
  a clearance, or a rights/attribution ruling.
- writes: **this file only**. No tool, gate, packet, projection, component, baseline,
  receipt or earlier-round byte is edited by this seat; rounds 8–18 are read-only here.
  No commit, no push.
- status: **analysis complete; the rule is codifiable from a delivered gate plus a design
  forecast, and the forecast half is labelled as such** (see §3, §5).

## 0. The rule in one sentence

**A routing class may hold a form's *slot* while leaving the form itself on the sound and
identity channel** — the same "a typing field cannot exempt a string" law the round-8 T1
discipline states, read in the new direction: **a `register` field cannot move a form off
the sound channel either** (`reports/round-17/d4/design-brief.md:254-281`, Δ1).

## 1. What the D4 exercise named (design authority, read-only)

`reports/round-17/d4/design-brief.md` §6 Δ1 (`:254-281`) declares **two routing classes in
one packet**:

| class | record set | checked field | channel | hold | anchor |
|---|---|---|---|---|---|
| 1 — gloss rows | goods/measure glosses with owed slots | moved off-channel (`off_channel_field: <field>_gloss`) | `off-sound-and-identity` | `D4L-FORM-UNRESOLVED` | `:255-262` |
| 2 — register rows | argot loans supplied and checked in the quote slot; plain doublet owed | **stays on channel** (`off_channel_field: null`) | `on-sound-and-identity` | `D4L-REGISTER-UNRESOLVED`, `owed_slot: <slot>#plain` | `:263-273` |

The D4 signature the brief names (`:271-273`): "every quote form appears in the sound
gate's inventory exactly as a native form does … while the plain slots produce
`D4L-REGISTER-UNRESOLVED` hold lines — one per owed slot, never a pass and never a note."

`typed-support-1.md:230-262` restates the same two-class table and fixes the vocabulary
(`D4L-REGISTER-UNRESOLVED` at `<slot>#plain`); `:272-292` §6.4 records that the D2 engine
carries **no register leg** — the class was forecast, not built.

## 2. What actually landed (measured, 2026-10-18)

| subject | command | observed |
|---|---|---|
| delivered D4 typed packet routing rows | `sed -n '2678,2800p' examples/culture-d4/packet.d4.typed.yml` | **12 rows**, every row `off_channel_field: "garment_gloss"`, `channel: "off-sound-and-identity"`, `hold: "D2L-FORM-UNRESOLVED"` — **all moved; zero class-2 register rows** |
| delivered projector's register support | `grep -c "REGISTER" tools/d2-typed-labels.py` | **0** |
| delivered projector's slot regex | `grep -n "_SLOT_RE" tools/d2-typed-labels.py` | `:449 _SLOT_RE = re.compile(r"LEX-GAR-[0-9]{2}")`, used `:498` |
| gate's class-2 classifier | `sed -n '186,199p' tools/gates/typed-pipeline-gate.py` | `moved_field(row)`: a missing key **or a null-ish value** (`null`, `none`, `~`, empty — the lane reader keeps an unquoted `null` as the string `"null"`) means the row **stays on channel** |

So the delivered tree carries **class 1 only**; class 2 exists as (a) the round-17 design
forecast, (b) the **generalized gate's classification and retention leg** built to grade it,
and (c) the gate's own selftest fixture. The craft rule is therefore codifiable, but its
evidence is a gate mechanism + a control fixture, **not** delivered D4 packet data — stated
plainly here so the D-axis codification does not over-claim.

## 3. The landed gate mechanism (executable authority)

`tools/gates/typed-pipeline-gate.py` (sha256
`04ad4bb479562c419b48d750a8f9303c4a5a717ca7f2fe3b3658cc1bb9578a48`, 11:32Z):

1. **Classification** — `moved_field(row)` (`:186-199`) splits the routing table into
   `moved_records` and `retained_records` (`:572-576`). A row whose `off_channel_field` is
   null-ish is *retained*: it names an owed slot but removes nothing from the sound channel.
   The docstring states the reason verbatim: "the D4 register class the round-17 brief
   declares."
2. **`L2-channel` counts moves, not rows** (`:656-673`). For a generalized (non-D2) family
   the removed-artifact count is compared against `field_moved` — the moved records that are
   **costume records** — not against the routing-row count, because D4 has "two routing rows
   per costume (garment-field row + owed-slot row) but exactly one field move per costume"
   (`:660-667`).
3. **`L2-retention`** (`:677-682`) is the class-2 leg: a record kept on the sound channel
   may **not** lose its inventory line — "routing, not deletion". This is the leg that makes
   the register class observable: if a register row silently retired a sound line, the run
   goes red.
4. **Fixture control** — the generalized selftest builds a `d9` fixture whose routing row is
   `off_channel_field: null`, `channel: "on-sound-and-identity"`,
   `hold: "D9L-REGISTER-UNRESOLVED"`, `owed_slot: "LEX-RF-01"` (`:1130-1146`) and grades it
   green against an expected set carrying that hold (`:1210-1211`). The class-2 shape is thus
   exercised on every `--selftest`, independent of the delivered D4 packet.

## 4. Codifiable craft rules (for the D-axis SKILL.md decision-table row)

Each row carries its citation and its control, so the codification is falsifiable.

| # | rule | citation | control |
|---|---|---|---|
| R1 | A routing row has two independent axes: **whether a checked field is moved** (`off_channel_field`) and **what slot remains owed** (`owed_slot`). Null-ish `off_channel_field` = form stays on channel. | `typed-pipeline-gate.py:186-199`; `design-brief.md:263-273` | gate selftest fixture `:1130-1146` (green) |
| R2 | The sound channel is governed by **field moves, not routing rows**: count removed artifacts against moved costume records, never against row count. | `typed-pipeline-gate.py:656-673` | delivered D4 run: 12 rows, 6 field moves, 6 `PHON-` artifacts removed (`reports/round-18/d4/` verdict) |
| R3 | A retained (on-channel) routing row may never delete the record's inventory line. | `typed-pipeline-gate.py:677-682` (`L2-retention`) | the leg itself is the control: `lost` non-empty ⇒ red |
| R4 | Neither direction of the T1 law is waivable: a typing field cannot exempt a string (round-8), **and** a `register` field cannot move a string off the sound channel (D4 Δ1/Δ8). | `design-brief.md:254-281`, `:368-381` (Δ8); `SKILL.md:42-47` | design controls C-01 (private segment ⇒ FAIL), C-03 (plain slot filled with quote form ⇒ FAIL), C-09 (gloss re-typed native re-enters and FAILS), `design-brief.md:455-463` |
| R5 | A register-scoped record is never `compare_only`: an owed plain slot cannot be skipped by a comparison flag. | `design-brief.md:373`, `:460` (C-06) | C-06 fixture ⇒ FAIL `D4L-SCOPE` |

## 5. Forecast vs delivered — the honesty ledger

- **Delivered**: class-1 gloss routing (12 moved rows), the generalized classifier that can
  *recognize* class-2 rows, and the `L2-retention` leg that would grade them.
- **Not delivered**: any class-2 row in `examples/culture-d4/packet.d4.typed.yml`; the
  projector emits `grep -c "REGISTER" → 0`; `D4L-REGISTER-UNRESOLVED` appears in no delivered
  D4 byte (the emitted set is `12 × D2L-FORM-UNRESOLVED + 3 × D2L-RANK`,
  `examples/culture-d4/expected-holds.json` `09490a27…`, counts `{hold 15, note 1, fail 0}`).
- Consequence for the D-axis: the SKILL.md row must cite the **gate mechanism + fixture** as
  its executable authority and the **design brief §6 Δ1 / §7.1 row 2** as its design
  authority, and must mark the class-2 *instance* `(to-verify)` — no delivered packet carries
  it (AGENTS.md: "claims you cannot verify are marked `to-verify`").

## 6. Destination

- **D-axis SKILL.md**: a new row under the label-typing decision table (§"Label typing",
  `SKILL.md:31-60`), condition = "a supplied form is admissible only in a register-scoped
  slot", routing = on-channel + `owed_slot`, hold = the register class, consequence = a
  register never licenses an inventory and never exempts a form.
- **Corpus lesson**: the D4 lesson entry (`corpus/lessons/round-19.md` or the round-19
  entry the C axis lands) carries R1–R5 with the `moved_field` citation and the delivered
  counts above.

## 7. Limits

- All readings are of NON-CANON engineering bytes at the shas/stamps above; a later edit to
  the gate or the packet is a re-read event, not a contradiction.
- The gate digest `04ad4bb4…` and packet digest `e7ecd204…` bind this file to those bytes
  only; the D4 exercise remains an exercise, and holds remain open design debt.
- Class-2 evidence is a fixture + a design forecast, not delivered culture data (see §5);
  the codification must say so.
