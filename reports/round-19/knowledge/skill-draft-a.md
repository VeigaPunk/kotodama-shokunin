> 2026-10-18 integrator erratum: the reviews' red measurements (L2-channel fail; adapter selftest 1/4) were pre-repair states — the integrator's L2-family patch and the adapter bytes fix landed after the review seats measured. Re-verified at close: typed gate 19/19 exit 0; adapter selftest green. Defect A correction: greens cited from runs over the untyped packet now name the typed run explicitly. Defect B (two wrong leg names in skill-draft-b) corrected to the legs the gate actually emits.

# R19-D04 — SKILL.md draft A: the slot-label routing model and register-scoped routing

- round: 19 (operator loop 2 of 3, build 3 of 4; `reports/round-19/claims.json`,
  claim **D** `depth`; provider `hyper/deepseek-v4.1-flash` per the operator's
  round-19 substitution). Lane: `kotodama-shokunin`.
- shard **D04** (table drafters ×2, first). Assignment (verbatim): "draft the
  exact SKILL.md subsection text (D4-derived decision tables + error-pattern
  rows), every row cited; reports/round-19/knowledge/skill-draft-a.md,
  skill-draft-b.md."
- date: 2026-10-18 (stamps UTC). Baseline revision
  `e5718945a1ab0a0c3db955338d2cae77d68fd348` (round-18 admit,
  `reports/round-19/claims.json:6`); declare `169c616`.
- canon: **NON-CANON engineering draft.** This file is paste-ready *draft text*
  for `SKILL.md`; it edits no byte of `SKILL.md`, `corpus/**`, `tools/**`, or any
  filed round-8..18 artifact. The parent owns placement, wording and admission.
  Nothing here is a canon record, a lore handoff, a clearance, or a rights
  statement.
- writes: **this file only**, plus gitignored scratch under `.scratch/r19d04/`
  (`export TMPDIR=$PWD/.scratch` preceded every scratch-writing command). No
  commit, no push.
- companion: `reports/round-19/knowledge/skill-draft-b.md` (R19-D05, the
  derivation-replay subsection). The two drafts are disjoint: A owns the routing
  shape, B owns the replay/derivation discipline.

## 0. Verdict

**The D4 typed pipeline is green end-to-end and its routing shape is fully
measurable from committed bytes, so the routing model can be codified as SKILL
craft text with every row cited.** Measured 2026-10-18T11:32:22Z at gate revision
`04ad4bb479562c419b48d750a8f9303c4a5a717ca7f2fe3b3658cc1bb9578a48`:
`python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml  # typed pipeline: gate builds the typed packet via the adapter`
exits **0**, `summary: 19/19 legs passed`, printing `15 holds + 1 note + 0 fails`
and `channel: 6 PHON artifact(s) retired, 0 added, retained lines identical`.

Three readings carry the whole subsection:

1. `examples/culture-d4/packet.d4.typed.yml` `typed_channel:` holds **exactly 12
   rows** — `record` = `GAR-01..GAR-06` and `LEX-GAR-01..LEX-GAR-06`, all 12 with
   `source_field: garment`, `off_channel_field: garment_gloss`,
   `hold: D2L-FORM-UNRESOLVED`, `channel: off-sound-and-identity`; `owed_slot` is
   `null` on the six garment rows and `LEX-GAR-0n` on the six slot rows (parsed
   2026-10-18T11:32Z).
2. `examples/culture-d4/expected-holds.json` carries `counts {hold 15, note 1,
   fail 0}`, and its 12 `D2L-FORM-UNRESOLVED` holds have `where` exactly
   `GAR-01..06` + `LEX-GAR-01..06` — the same 12 record ids (parsed
   2026-10-18T11:32Z).
3. The gate's routing cross-check asserts that equality directly
   (`tools/gates/typed-pipeline-gate.py:736-753`, `check("L3-routing-consistency",
   hold_records == moved_records and hold_slots == routed_slots, …)`).

The **register** dimension is drafted as a *boundary*, not as a delivered hold
class: the delivered tree carries no register-class hold and the shared engine
emits no register-class id (`grep -c "REGISTER" tools/d2-typed-labels.py` → **0**;
`grep -c "D4L-" tools/d2-typed-labels.py` → **0**, 2026-10-18T11:32Z). A
subsection that asserted a register hold class would be drafting a capability the
bytes do not have; the honest craft rule is the one the bytes *do* support — a
`register` field is declarative and never moves a form off the checked channel.

## 1. What the subsection must say (the two rules, stated before the table)

- **Rule 1 — the routing set is the hold set.** For a typed pipeline, the set of
  records named by a `typed_channel` row equals the set of records named by the
  `FORM-UNRESOLVED` holds, and the set of `owed_slot` values equals the set of
  slot ids those holds name in their `detail`. One row per translated label; an
  owed slot is named **once**, on its own row, and the obligation is one
  obligation seen from two sides, not two obligations.
- **Rule 2 — routing is triggered by kind, never by register.** The routing
  predicate is the label's *kind* (`translated-label`), not any social or
  stylistic field. A `register` value is a declarative property of an on-channel
  record; it may not be promoted into an `off_channel_field`. This is the
  round-8 T1 discipline (`SKILL.md:47`: "adding typing fields cannot exempt a
  string") read on the register axis.

## 2. Draft SKILL.md subsection text (paste-ready)

Suggested placement: a round-19 subsection under *Decision table*, after the
existing "Claim uncertainty typing" subsection (`SKILL.md:77-128`), before
`## Error patterns` (`SKILL.md:131`).

```markdown
### Slot-label routing — one row per moved record, the owed slot named once

A typed pipeline protects the checked channel by **moving** a form, never by
flagging it: a record the projector types `translated-label` with no supplied
native/borrowed form has its checked field renamed (moved off the sound-and-identity
channel), one routing row is written for it, and one hold names it. The routing
row set and the `FORM-UNRESOLVED` hold set are the same set — an equality the gate
asserts, not an intention. Executable authority
`tools/gates/typed-pipeline-gate.py` (`L3-routing-consistency`, `:736-753`; the
`L1-routing`/`L2-channel` legs) and `tools/assemble-d4-typed.py` (`ROUTED_KINDS`,
`:65`); design authority `reports/round-17/d4/typed-support-1.md` §5.2-§5.3 and
`reports/round-17/d4/typed-support-2.md` §3 ("One hold per owed slot"); worked
instance `examples/culture-d4/packet.d4.typed.yml` (`typed_channel:`) with
`examples/culture-d4/expected-holds.json`.

| Condition on the record | Routing row | Hold it carries | Never | Wrong-shape consequence |
|---|---|---|---|---|
| A checked field holds a reader-facing gloss (kind `translated-label`) and no native/borrowed form is supplied | **exactly one** row naming the record: `source_field` → the moved field, `off_channel_field` → its `_gloss` rename, `channel: off-sound-and-identity` | one `FORM-UNRESOLVED` hold whose `where` is the record id | delete the gloss to "clean" the gate — the gloss is moved and still rides in the typed packet; a row without its hold; a hold without its row | the gate's `L3-routing-consistency` fails, naming `holds … vs routed …`; a deleted hold is caught by `L3-holds`/`L3-counts`/`L3-baseline-set` naming the record (`reports/round-18/d4/neg-1.md` §3.1-§3.2) |
| The owed slot is itself a projected record (the packet's `form_slots` block) | a **second** row naming the slot record, with `owed_slot` set to that slot id and the same `source_field`/`off_channel_field` | a second `FORM-UNRESOLVED` hold whose `where` is the slot id, with the **identical** `detail` | count the two rows as two obligations — they are one obligation seen from the slot side (`reports/round-18/d4/review-1.md` §0-§1 derives six obligations from six costumes) | an under- or over-counted set; the gate's slot comparison (`hold_slots == routed_slots`) fails |
| The record carries a `register` (or any social/stylistic) field but its form is on-channel | **no** row: the record keeps its checked form | none from this field | promote the register value into `off_channel_field`; let a register label remove a string from the checked channel | a register-scoped exemption is the round-8 T1 violation at a new address — `adding typing fields cannot exempt a string` (`SKILL.md:47`) |
| A hold is laundered (downgraded to a note, or deleted) while the artifact still assembles | unchanged | the hold must still be present at `hold` severity | accept a shorter/quieter hold set as clean | four legs fail naming the record: `L3-holds`, `L3-notes`, `L3-counts`, `L3-baseline-set` (`reports/round-18/d4/neg-1.md` §3.1) |
| The family's design names a register hold class the engine cannot prove | no row; the class is reported, not written | the **emitted** vocabulary governs the expectation file | assume a `D4L-REGISTER-UNRESOLVED` (or any) id the delivered projector never emits | an expectation naming an unprovable class cannot equal the emitted set; the freeze rule excludes a row the gate cannot prove (`reports/round-17/d4/typed-support-2.md` §4 freeze rule 2; `reports/round-18/d4/holds.md` §3) |
| A label is retyped from `translated-label` to `native-form` to make the row disappear | the row must disappear **only** when a supplied native form exists | the hold clears only on a supplied form | retype a gloss as native to drop its routing row | the sound channel then grades translated text as a surface form; the naming kernel reads it as a `PHON-INVENTORY` artifact and the channel differential names the record (`reports/round-18/d4/neg-2.md` §3.1) |
```

Thresholds and cautions that are part of the rule:

- **T1 — the routing predicate is the label kind, not the field name.** The
  delivered adapter routes `ROUTED_KINDS = ("translated-label",)`
  (`tools/assemble-d4-typed.py:65`); a record of another kind that happens to sit
  in a costume block is not routed, and a `translated-label` anywhere is. Field
  names (`garment`, `garment_gloss`) are the *consequence* of the move, not its
  trigger.
- **T2 — the move is a rename, never a delete.** `text_payload` rewrites
  `^(\s*)garment:` → `garment_gloss:` in place (`tools/assemble-d4-typed.py:296-310`);
  the gloss stays in the document under its new key. A pipeline that deletes the
  gloss has removed evidence, not protected a channel.
- **T3 — one obligation, two record names.** The delivered instance keys the same
  six owed forms twice (`GAR-0n` and `LEX-GAR-0n`) because the projector projects
  every `form_slots` entry as a label and each owed slot then emits its own hold
  (`tools/d2-typed-labels.py:622`, `:793`; `reports/round-18/d4/holds.md` §4.2).
  The hand re-derivation counts **six** obligations for six costumes
  (`reports/round-18/d4/review-1.md` §0-§1). Both readings are correct; the
  craft statement is that the *count of obligations* is a property of the
  design, and the *count of rows* is a property of the projection.
- **T4 — a register field is a claim about who says a form, not whether it is a
  form.** Real registers are chosen, not inherited (`corpus/knowledge/linguistics/sociolinguistics-registers.md:58`),
  and professional registers resist paraphrase by design
  (`sociolinguistics-registers.md:83`). A register-scoped *slot* is therefore a
  design statement about a form's social distribution; it never licenses moving
  that form off the identity channel.
- Cautions that are part of the rule: a register label is not a channel
  (`SKILL.md:47`, `corpus/knowledge/synthesis/era-language-staging.md:114`
  "type every label"); the routing set is not the obligation set (T3); a green
  routing leg is not a clearance — exit 0 means "the emitted findings equal the
  frozen expected set", and every hold is still open design debt
  (`reports/round-18/d4/manifest.md` §6; `tools/gates/typed-pipeline-gate.py` banner).

## 3. Draft error-pattern rows (paste-ready — append to `## Error patterns`)

```markdown
| A `typed_channel` row exists but no hold names its record | half a routing: the row moved the field, the hold that records the debt is missing — `L3-routing-consistency` fails naming `holds … vs routed …` (`tools/gates/typed-pipeline-gate.py:736-753`; `reports/round-18/d4/neg-1.md` §3.2) |
| A hold names a record with no routing row | the debt is claimed but the field was never moved; `L3-routing-consistency` fails the same way (`tools/gates/typed-pipeline-gate.py:736-753`), and the aggregate is not clean |
| A `register` value promoted into `off_channel_field` | the round-8 T1 violation on the register axis: a typing/social field cannot exempt a string from the checked channel (`SKILL.md:47`); route by label kind only (`tools/assemble-d4-typed.py:65`) |
| One owed form counted as two obligations (garment id + slot id) | the projection names the slot separately (`tools/d2-typed-labels.py:622,:793`), so the rows are 12 while the obligations are 6 — do not report the row count as the design debt (`reports/round-18/d4/review-1.md` §0-§1; `reports/round-18/d4/holds.md` §4.2) |
| A gloss deleted rather than moved off the channel | evidence removed, not a channel protected: the move is a rename, `garment` → `garment_gloss` in place (`tools/assemble-d4-typed.py:296-310`) |
| An expectation carrying a register hold class no delivered projector emits | drafting a capability the bytes lack: `grep -c "REGISTER" tools/d2-typed-labels.py` → 0 (2026-10-18); the emitted vocabulary governs, and a row the gate cannot prove does not enter the file (`reports/round-18/d4/holds.md` §3; `reports/round-17/d4/typed-support-2.md` §4 freeze rule 2) |
| A label retyped `translated-label` → `native-form` to drop its routing row | the gloss then sits on the sound channel and the naming kernel reads it as a `PHON-INVENTORY` artifact; the channel leg names the record (`reports/round-18/d4/neg-2.md` §3.1) |
```

## 4. Measured basis (so the parent can paste with citations)

Every reading below was taken by this seat, read-only, from the lane root, with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, on **2026-10-18**; the
gate revision is named where it matters.

| command | observed |
|---|---|
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml  # typed pipeline: gate builds the typed packet via the adapter` | exit **0**, `summary: 19/19 legs passed`; 15 holds + 1 note + 0 fails printed; `channel: 6 PHON artifact(s) retired, 0 added, retained lines identical`; gate sha `04ad4bb4…` (11:32:22Z) |
| `python3` parse of `examples/culture-d4/packet.d4.typed.yml` `typed_channel:` | **12** rows; `record` = `GAR-01..06` + `LEX-GAR-01..06`; `source_field: "garment"` ×12; `off_channel_field: "garment_gloss"` ×12; `owed_slot` `null` ×6 + `LEX-GAR-01..06`; `hold` `{D2L-FORM-UNRESOLVED}`; `channel` `{off-sound-and-identity}` |
| `python3` parse of `examples/culture-d4/expected-holds.json` | `counts {hold:15, note:1, fail:0}`; 15 holds / 1 note; by id `D2L-FORM-UNRESOLVED` ×12, `D2L-RANK` ×3; FORM `where` = `GAR-01..06` + `LEX-GAR-01..06`; keys `counts, holds, notes, packet_sha256, projection_sha256, projector_sha256, schema` |
| `grep -c "REGISTER" tools/d2-typed-labels.py` | **0** — no register-class hold id in the engine |
| `grep -c "D4L-" tools/d2-typed-labels.py` | **0** — the emitted vocabulary is `D2L-*` |
| `grep -c "AL-01#plain" examples/culture-d4/packet.d4.yml` | **0** — the round-17 union's register rows have no delivered trigger |
| `grep -c "register" examples/culture-d4/packet.d4.yml` | **18** — declarative `register:` fields on lexicon/symbol records that stay on-channel; none appears in `typed_channel` |
| `grep -n "L3-routing-consistency" tools/gates/typed-pipeline-gate.py` | `:750`, inside the routing block `:736-753` |

## 5. Limits and what the parent must decide

1. **The register subsection is a boundary, not a class.** The delivered D4 tree
   carries no register-scoped hold; `reports/round-18/d4/holds.md` §3 dispositions
   the six union `D4L-REGISTER-UNRESOLVED` rows as "unprovable, not in the file".
   If the parent wants a register *hold class* in SKILL.md, that is a design claim
   for a future round with an engine path, not a codification of D4.
2. **Row counts are revision-pinned.** Every count here names the gate revision
   and the date; a later revision or a re-derived expectation moves them. The
   draft text avoids embedding counts in the craft statements themselves and puts
   them in the cited tables, so a re-pin changes a citation, not the rule.
3. **`SKILL.md` is not edited by this seat.** This file is draft text; placement
   and wording are the parent's. If the parent lands it, the `SKILL.md` line
   numbers cited above (`:47`, `:77-128`, `:131`) shift and must be re-read at
   landing time.
4. **NON-CANON throughout.** Hold counts are design debt, never a clearance;
   canon standing is lore-shokunin's (`AGENTS.md`, `PROVINCE.md`).
