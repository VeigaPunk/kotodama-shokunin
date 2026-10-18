---
name: kotodama-shokunin
description: "Linguistic-cultural worldbuilding (言霊) — conlang craft, myth & symbol systems, era staging, costume/material-culture lexicon, and the coupling between them, feeding the world bible. Triggers: 'design a language', 'conlang', 'culture for this world', 'mythology of', 'symbolism of', 'naming system', 'costume/dress terms', 'era language stages', 'word for this concept'. Anti-trigger: NOT world-bible canon recording or consistency verification (lore-shokunin), NOT prompt/skill craft (kotoba-shokunin), NOT general source-research method (chousa-shokunin), NOT real-world rights/attribution rulings. Rank: shonen."
---

# kotodama-shokunin — linguistic-cultural systems (言霊)

Domain: the generative craft that connects languages, cultures, myths,
symbolisms, and eras to their linguistics and costumes for a fictional
world — and hands the resulting systems to the world bible. 言霊
(kotodama, "word-spirit") names the core premise: a culture's language is
not decoration on its world; it is evidence of it. Myth shapes vocabulary,
era shapes register, costume carries a lexicon, and symbols fossilize into
words.

This repo is the craft's home. The world bible itself — entities, relations,
timeline, canon consistency — belongs to lore-shokunin; this lane supplies
languages and cultural systems to it, never edits it.

## Decision table

| Intent | Correct surface | Never | Expected output |
|---|---|---|---|
| Design a language for a culture | conlang-methodology → phonology/typology → lexicon by semantic field → pragmatics | starting from a cipher of English with no culture brief | a language sketch tied to the culture brief |
| Give a culture a mythology | comparative frameworks → creation/hero/trickster taxonomies → symbolism synthesis | pasting a real-world pantheon with renamed gods | a mythic system with internal logic, tied to language |
| Name entities (people, places, gods, items) | naming-systems → phonotactics + morphology of the naming language | unpronounceable or collision-prone names with no derivational logic | names with etymologies and a derivation pipeline |
| Stage language across eras | era-language-staging → historical-linguistics (sound change, grammaticalization) | one static language across millennia | period registers / daughter languages with change laws |
| Dress a culture | dress-through-eras + costume-semiotics → garment lexicon (crosslinguistic) | costume with no rank/rite/era semantics | costume system + its terminology + signaling table |
| Check a world hangs together | consistency-verification-checklist (synthesis) | silently resolving contradictions into canon | a findings list; canon rulings go to lore |

### Label typing — translated labels, native forms, borrowed strata

Type every form-bearing record before any gate reads it. The checked channel
holds one form per record; a gloss is never that form, and a loan is never
typed by its look. Executable authority `tools/d2-typed-labels.py`
(`--selftest`); design authority `reports/round-8/depth/design-spec.md` §1;
full receipts `reports/round-8/depth/skill-table-draft.md`. Grounding:
`corpus/knowledge/synthesis/era-language-staging.md:108-124`.

| Condition on the record | Kind and status | Checked channel | Required companions | Wrong-typing consequence |
|---|---|---|---|---|
| Text is a reader-facing gloss (declared gloss field, whitespace/gloss syntax, or a segment outside the declared inventory) | `translated-label` | **never** — not on the sound or identity channel | `label_id` + `owner`; when the native form is still owed, the form slot stays held | grading a gloss against native phonotactics manufactures representation artifacts — 10/10 of the frozen round-4 `PHON-INVENTORY` class are this |
| A supplied native form exists | `native-form`, `status: supplied` | sound + identity; exactly one checked form per record | script/representation/scheme, `era_ids`, evidence | a translation claim cannot waive it: native bytes govern, still FAIL |
| Sound kind declared, no bytes supplied | `native-form` / `borrowed-strata`, `status: absent` or `to-verify` | nothing checked | owner + form slot + reason | silent pass forbidden — `D2L-FORM-UNRESOLVED` HOLD, never clean |
| Supplied form passes the declared inventory **and** ≥2 borrowed-strata discriminators hold | `borrowed-strata`, `status: supplied` | the recipient-adapted form against the recipient inventory, **plus** borrow-ledger checks: layer resolves, donor separated, substitutions reproduce the form, clocks ordered, domain/register declared | layer ref, donor {immediate / ultimate / carrier}, donor form + substitutions, entry stage, referent availability, channel, register/domain | mistyping a loan as native erases the contact clock; mistyping a native word as a loan invents a contact history |
| Exactly 1 discriminator holds | kind not asserted; `status: to-verify` with the one discriminator named | nothing | the discriminator that holds, stated | do not default to either kind |
| Untyped legacy record | no kind | unchanged channel — its legacy form field is still checked | — | adding typing fields cannot exempt a string from checking |

Thresholds (T1–T4 hard; T5 calibration): T1 native-eligibility = every segment
in the declared inventory **and** tokenizable under the declared syllable
profile; a label signature (whitespace, gloss punctuation, out-of-inventory
segment, declared gloss provenance) is sufficient to route off the sound
channel. T2 identity = exactly one checked form per record; a contradiction
between a translation claim and native bytes ⇒ native bytes govern; a declared
sound kind with no bytes ⇒ HOLD. T3 borrowed-strata discriminators — house
rule, ≥2 of 5: recurring correspondences with a named donor stage, donor-side
chronology, channel separation (etymon/donor/carrier as separate facts),
field/register clustering, dated witness + usage status (`corpus/knowledge/synthesis/loanword-material-dating.md:43-57`); exactly 1 → `to-verify`; 0 → native default, which is not a native finding. T4 clock separation:
typing `borrowed-strata` opens a second clock — word-entry interval ≠
referent-arrival interval; never intersect them to manufacture a date
(executable B4: `entry_stage` earlier than `referent_available_from` ⇒
`D2L-BORROW` FAIL). T5: WOLD 1,460-meaning / 41-language sample means ~24%
borrowing, none loan-free (`language-contact.md:56-62`) — a fully loan-free
declared lexicon needs a stated contact story; the band never overrides a
packet's own declared history.

Three cautions that are part of the rule: inventory-legal is not native (the
inventory test routes strings *away* from the native channel; it never proves
nativeness — provenance decides); a label is not a gap-filler (removing a
gloss from the sound channel removes an artifact, it does not clear the name —
the aggregate stays red with owed forms held); a label is not history (a
translated or curatorial label never becomes an attested historical native
word by repetition, `costume-language-coupling-table.md:43`).



### Claim uncertainty typing — supported / partial / unresolved

Every handoff claim-ledger row carries `uncertainty: {status: supported|
partial|unresolved, basis}` plus claim-to-record links that resolve: contract
§4 requires per-claim "uncertainty, and relation to other records"
(`corpus/knowledge/synthesis/worldbible-integration-contract.md:63`), and the
round-12 audit rejected the v1 packet because the ledger had neither the
uncertainty dimension nor claim-to-record keys, while D2 coupling was one
aggregate edge (`reports/round-12/adjacency/contract.md:27-28`). Status says
how completely this packet's pinned records and checks ground the claim
**exactly as worded**; claim kind and evidence status stay independent
dimensions, never merged with it (`worldbible-integration-contract.md:92-106`).
Executable authority `tools/harness/packet_uncertainty.py` (`--selftest`);
design authority `reports/round-15/handoff/v2-design.md` §2; knowledge draft
`reports/round-15/knowledge/uncertainty-table-draft.md` §3; vocabulary
`reports/round-15/claims.json:14`. Basis grammar: one `grounding:` witness per
claim (a manifest artifact id, a repo path, or a named validation check);
`restriction:` iff `partial`; `open:` + `owner:` iff `unresolved`
(v2-design §2.2).

| Status | Assign when (necessary condition) | Required basis | Never |
|---|---|---|---|
| `supported` | every element of the claim-as-worded is grounded by a named record in the packet's manifest or a named check with an observed result; nothing open narrows the wording | the resolving `grounding:` witness; residual limits are named even here — scoped-supported is "bounded and revisable, not certainty" (`corpus/knowledge/verification/to-verify-triage-protocol.md:18`) | upgrade a node's support onto its coupling edge (`to-verify-triage-protocol.md:97`); cite a shape-gate pass or digest match as the basis of a semantics claim (`reports/round-12/adjacency/contract.md:9-10,23`) |
| `partial` | the claim holds only under a stated restriction — scope limit, translation/mediation, projection-of-records, caveat-carrying source | `grounding:` + `restriction:` naming the exact bound, as BR05 did: "the Behistun cross-version leg … remain[s] unverified" (`reports/round-11/handoff/packet.md:108`) | widen the evidence instead of narrowing the wording (`to-verify-triage-protocol.md:70,76`); drop the `(to-verify)` from the downgraded remainder (`:182`) |
| `unresolved` | a named open question blocks the claim as worded: unperformed work, an external authority still pending, or contested alternatives that must coexist | `grounding:` + `open:` question + `owner:` lane — "a naked marker without a research question is not a usable queue item" (`to-verify-triage-protocol.md:32`) | let a deadline or failed search force closure (`:80`); present open as a fourth verdict — it is a queue state (`:80,181`); read absence as disproof ("silence is not proof of absence", `worldbible-integration-contract.md:179`) |

Partition crosswalk (`corpus/knowledge/verification/`): triage §1 evidence
states route to statuses — `Located` alone never rises above `partial`
(`to-verify-triage-protocol.md:16`); `Inspected` with unqualified wording
grounds `supported` (`:17`); `Scoped-supported` and `Contested` map to
`partial`, the restriction preserving the disagreement (`:18-19`); `Unknown`
maps to `unresolved`, and unknown is not false (`:21`). The corpus's
framework statuses S/C/H/R/U/V (`source-discipline-calibration.md:67`) stay
framework-level: they calibrate a source or framework, never substitute for a
claim's basis. Provenance-audit wording governs: `supported` does not mean
`improved`, and neither means canon
(`corpus/knowledge/verification/provenance-audit-ledger-format.md:12`).
Legacy `HARD/SOFT/DOCTRINE/DESIGN` labels are advisory and do not map onto
these statuses without lore's explicit mapping
(`worldbible-integration-contract.md:104`; `to-verify-triage-protocol.md:100`).

Cautions that are part of the rule: `supported` is not true and not canon —
evidence strength and fictional truth are orthogonal
(`worldbible-integration-contract.md:102`) and canon standing is lore's alone
(`:100`); `unresolved` is not false; `partial` describes the evidence, not a
demotion of the design. Status never inherits downward: an edge derived from
a `partial` or `unresolved` claim carries at least that status ("A confirmed
node does not upgrade an uncertain relationship",
`to-verify-triage-protocol.md:97`; severity `supported` < `partial` <
`unresolved`, v2-design §2.2). Basis is never boilerplate: unique per claim,
its witness must resolve, and a basis that restates the status word is
rejected (`worldbible-integration-contract.md:183`; v2-design §2.3).
````

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

### Derivation replay — replay the family's own build, by text transform

A typed derivation is replayable only when three things are true at once: the
identity leg calls the *family's* own assembler, the derived artifact is built by
a text transform of the source bytes (never by re-serializing foreign content),
and the replay names every input. The D4 chain is the worked instance.
Executable authorities `tools/assemble-d4-typed.py` (`SERIALIZER`, `:62`;
`text_payload`, `:296-310`) and `tools/gates/typed-pipeline-gate.py`
(`L1-profile`/`L1-assembler`/`L1-projection_freshness`/`L1-coverage`/`L1-build`,
`L2-channel`, `L3-*`, `L4-pins`); flagless resolution
`tools/gates/typed-pipelines.json`; design authority
`reports/round-18/gate/design.md` §0/§1.3/§11 and
`reports/round-17/d4/typed-support-1.md` §4-§5; measured instance
`reports/round-18/d4/determinism.md` §3, `reports/round-18/d4/manifest.md` §2,
`reports/round-18/d4/interop-1.md` §0.

| Replay requirement | Correct shape | Never | Consequence if violated | Citation |
|---|---|---|---|---|
| Assembler identity | the adapter's identity leg calls the family's own assembler build path (`assemble()` on `tools/assemble-culture-d4.py`), and the identity message names the assembler it actually checked | hard-bind the leg to another family's serializer, or re-implement the build inside the adapter | a correct foreign packet is refused (exit 2) and the default family's bytes move | `tools/assemble-d4-typed.py:62`; `reports/round-17/d4/typed-support-1.md` §4 B4 (receipt P3); `reports/round-18/gate/design.md` §1.3 |
| Named inputs | every input is named on the command line (`--packet` **and** the artifact), so the comparison is the pair the caller meant | run `--check <artifact>` alone against a multi-family tool | a false difference: exit 1 "differs" where the named pair exits 0 — measured 2026-10-18T11:32Z | `tools/d2-typed-labels.py --check` measured control (§4) |
| Machine-readable pattern/output pairs | the committed expectation is a machine-readable document: schema, `counts`, the row list, and the digests it is pinned to | a prose or hand-typed expectation; a pinned count with no row list; a row list with no pins | the equality leg cannot be re-run by a stranger, and a re-pin cannot be distinguished from a re-bless | `examples/culture-d4/expected-holds.json` keys `counts, holds, notes, packet_sha256, projection_sha256, projector_sha256, schema`; `reports/round-17/d4/typed-support-2.md` §2 (comparison key `(id, severity, where)` as a set, `detail` strings pinned); `tools/gates/typed-pipeline-gate.py:696-734` |
| Round-trip corruption class | derive by **text transform**: rewrite the one moved key in place, append adapter-owned blocks serialized from adapter-generated data alone | re-serialize the whole foreign document through a round-trip serializer | regex backslashes, booleans and nulls are mangled; the derived artifact stops matching its source's semantics while still assembling | `tools/assemble-d4-typed.py:296-310`; `SCORECARD.md:176-177,185`; `LOG.md:3252-3253` |
| Text-transform rule | the transform touches exactly the declared key set (`garment` → `garment_gloss`) and nothing else; the moved value stays in the document | a general "normalizer" that rewrites unrelated lines | the transform becomes an unreviewable second assembler; a byte diff cannot localize a change | `tools/assemble-d4-typed.py:296-310` (the loop renames only `^(\s*)garment:` inside `costumes:`) |
| Flagless resolution | a frozen replay row cannot carry flags (`tools/replay-frozen.py` launches `[python3, <gate>, <input>]`), so the family must resolve flaglessly from a sha-pinned profile matched on the packet's declared `assembly.generator` | a family that can only be graded with CLI flags | the row cannot be frozen; a flag-only path is un-replayable by design | `reports/round-18/d4/manifest.md` §2; `tools/gates/typed-pipelines.json` (`schema kotodama-typed-pipelines-v1`, profile `d4`, every field digest-pinned); `tools/gates/typed-pipeline-gate.py:481-485` (a stale pin refuses, exit 2, `L1-profile`) |
| Determinism | two consecutive builds are byte-identical, and `--check` compares bytes without writing | a build whose output embeds a path, a timestamp, or a host name | the artifact is not replayable; a frozen pin moves under an unrelated edit | `tools/assemble-d4-typed.py:369` (`two consecutive builds are not byte-identical`); `reports/round-18/d4/determinism.md` §3 |
| Pre-registration | the expected set is decided elsewhere **before** the tool runs (design table, design-doc union, or a declared acceptance criterion) and any delta is dispositioned in a filed reconciliation | write the expectation from the tool's own printed output | the equality leg has drift teeth but no content teeth — it cannot distinguish "the set is right" from "the set is a copy of the producer" | `reports/round-18/d4/review-2.md` §0/§2 (the landed D4 file equals the projector's live output verbatim); `reports/round-18/d4/holds.md` §3-§4; `corpus/knowledge/verification/verification-independence-anti-circularity.md` §2 (the circularity catalog) |
| Passenger rows | a row emitted by a shared engine for any packet is attributed **per packet** in the expectation, or excluded | let a packet-independent block silently enter a new family's debt set | the equality leg is described as verifying the new family's design debt while the row names records that occur zero times in its packet | measured: the D4 expected file carries 3 `D2L-RANK` holds + 1 note naming `TR-04#a\|TR-06#a`, `WR-02#g\|WR-09#g`, `WR-08#g\|WR-09#g`, `SR-01#a\|SR-01#b`, each **0** hits in `examples/culture-d4/packet.d4.yml` (2026-10-18T11:32Z); `reports/round-18/d4/review-4.md` §2; `reports/round-18/d4/holds.md` §5 |
| Freeze-artifact naming | a freeze receipt that is not a battery baseline is not named `expected.json` under a battery root | land a `freeze-receipt.json` under a name the battery discovers as a baseline | the standing battery fails closed on a gate outside its name constant | `reports/round-18/d4/manifest.md` §6 |
```

Thresholds and cautions that are part of the rule:

- **T1 — identity is checked against the declared assembler, and the message
  names it.** An identity leg that still says "assemble-d2.py" while grading a D4
  packet is the round-17 rejection reproduced at a new address
  (`reports/round-18/gate/design.md` §1.1, §11 item 4).
- **T2 — a skipped leg is not an implementation.** A packet declaring no assembler
  must resolve to the documented default, not to "identity not checked"; a
  `return True` branch for non-default input is a laundering channel of the same
  class as a laundered hold (`reports/round-18/gate/design.md` §1.3).
- **T3 — the round-trip class is about *content*, not about determinism.** A
  serializer can be perfectly deterministic and still corrupt a regex backslash;
  determinism (two runs equal) and fidelity (the derived artifact preserves the
  source's content) are separate checks and neither implies the other.
- **T4 — a projection embeds its packet path.** The D2 projection differs from a
  scratch-path emission in exactly two lines (`assembly.packet`, `canon`), so a
  family's projection must be emitted from its canonical path
  (`reports/round-17/d4/typed-support-1.md` §3 P1, F-D18-5).
- Cautions that are part of the rule: exit 0 is not a clearance — it means "the
  emitted findings equal the frozen expected set" and every hold stays open
  (`reports/round-18/d4/manifest.md` §6); a re-pin that changes the hold set is a
  finding, not a pass (`corpus/knowledge/verification/verification-independence-anti-circularity.md`
  §2, §6); a green self-test is capability, not measurement
  (`corpus/knowledge/verification/gate-frozen-run-standard.md` §1).

## Error patterns

| Observation | Reading |
|---|---|
| language is a relex of the author's native language | the culture brief never reached the lexicon; rebuild from semantic fields |
| every culture shares one symbolic color code | cross-cultural variance ignored; check color-symbolism variance table |
| static language across deep time | missing diachronic staging; apply sound-change and grammaticalization paths |
| costume described with modern garment words | era/register lexicon mismatch; derive terms from textile technology and cut |
| names with no derivational morphology | naming-systems pipeline skipped; names should carry etymology |
| myth that explains nothing in daily life | myth is detached from ritual, calendar, and taboo; re-couple via ritual-liminality |
| An English garment label fails the native inventory | representation-channel artifact, not a name violation; type the record or hold the owed form — never rename the garment to "fix" the gate (frozen round-4 output 10/10 `GAR-*`; `reports/supplement-opencode-1/22-label-representation.md` §1) |
| A label-only record passes silently | forbidden: label-only → off the sound channel **and** a hold, so the aggregate stays red (`22-label-representation.md:126-128`; executable `TL-01`) |
| A translation claim made over a violating native form | cannot waive: native bytes govern, still FAIL (`22-label-representation.md:129-130`) |
| A sound kind declared with no bytes supplied | HOLD, not clean (`22-label-representation.md:131-132`; executable `TL-01`) |
| An untyped legacy label | still checked; typing fields cannot exempt a string (`22-label-representation.md:133-134`) |
| A record with no declared kind at all | hold with a stable reason — the kind is never guessed from the text's language (`tools/d2-typed-labels.py` `TL-02`) |
| `compare_only` set while the typed label is unresolved | misuse, not a pass — the unresolved hold stands (design spec R3) |
| A borrowed form judged only against the native stratum | misfile: loans pass through the recipient's phonotactic filter and carry donor provenance (`language-contact.md:78-79`) |
| A loan's oldest form used to date the referent's arrival | clock conflation; keep word-entry and object-arrival intervals separate (`loanword-material-dating.md:26,60`; executable B4) |
| A loanword that switched referent in transit | keep both coexisting names; date the sense–referent pairing (`garment-lexicon-crosslinguistic.md:26`) |
| Imported prestige terminology for locally made goods read as evidence of import | dictionary/selection bias; check local manufacture under imported labels (`loanword-material-dating.md:57`) |
| A modern/curatorial label promoted to an attested historical native word | reject or split: the label is typed as a label; the term keeps its own record (`costume-language-coupling-table.md:43`) |
| A translation, exonym, or official replacement run through the inherited-form sound laws | track separately: sound laws apply to the inherited spoken label, not its translation or replacement (`era-language-staging.md:124`) |
| Era tags or slot glosses graded on the name/sound channel | type them `fictional-coordinate` / `descriptive-gloss`; neither enters the sound channel (tool `FIELD_DEFAULTS`) |
| A transliteration collision read as native-script identity | compare per declared scheme; a collision in that output channel is not native identity (`naming-collision-gate.md:69-70`) |
| A shared garment label across cultures read as identical cut or status | labels are neither cut nor status (`naming-collision-gate.md:52`) |

| Status | Assign when (necessary condition) | Required basis | Never |
| `supported` | every element of the claim-as-worded is grounded by a named record in the packet's manifest or a named check with an observed result; nothing open narrows the wording | the resolving `grounding:` witness; residual limits are named even here — scoped-supported is "bounded and revisable, not certainty" (`corpus/knowledge/verification/to-verify-triage-protocol.md:18`) | upgrade a node's support onto its coupling edge (`to-verify-triage-protocol.md:97`); cite a shape-gate pass or digest match as the basis of a semantics claim (`reports/round-12/adjacency/contract.md:9-10,23`) |
| `partial` | the claim holds only under a stated restriction — scope limit, translation/mediation, projection-of-records, caveat-carrying source | `grounding:` + `restriction:` naming the exact bound, as BR05 did: "the Behistun cross-version leg … remain[s] unverified" (`reports/round-11/handoff/packet.md:108`) | widen the evidence instead of narrowing the wording (`to-verify-triage-protocol.md:70,76`); drop the `(to-verify)` from the downgraded remainder (`:182`) |
| `unresolved` | a named open question blocks the claim as worded: unperformed work, an external authority still pending, or contested alternatives that must coexist | `grounding:` + `open:` question + `owner:` lane — "a naked marker without a research question is not a usable queue item" (`to-verify-triage-protocol.md:32`) | let a deadline or failed search force closure (`:80`); present open as a fourth verdict — it is a queue state (`:80,181`); read absence as disproof ("silence is not proof of absence", `worldbible-integration-contract.md:179`) |
| A claim's status rides as prose inside `evidence_status` or `kind` | no per-claim uncertainty carrier — the round-12 reject (`reports/round-12/adjacency/contract.md:27`; v1 rows `reports/round-11/handoff/packet.md:82,88,95`); fill the dedicated `uncertainty` field, don't decorate another column |
| The packet passes `16/16 + 20/20` with no uncertainty column anywhere | shape-clean is not uncertainty-populated: the gate has zero uncertainty checks (`grep -ci uncertainty tools/gates/handoff-packet-check.py` → 0, 2026-10-17) and its fixture ledger has five columns, none of them uncertainty (`tools/gates/handoff-packet-check.py:651`) |
| Two claims share one basis sentence, or a basis restates the status word | boilerplate basis: basis is per-claim evidence whose witness resolves (`reports/round-15/claims.json:14`; `worldbible-integration-contract.md:183`) |
| A digest match or gate exit 0 offered as a claim's basis | byte identity is not meaning: the audit matched 21/21 digests and still declined the count-semantics claim (`reports/round-12/adjacency/contract.md:11,23`) |
| A claim-to-record link present but not resolving | same defect class as an absent basis (`reports/round-15/claims.json:14`); existence-check every link at freeze and digest-pin the bytes |
| An edge or record inherits its source node's `supported` | nodes do not upgrade arrows: each source→target row is typed with its own status, applicability and justification (`to-verify-triage-protocol.md:97`; `worldbible-integration-contract.md:64`) |
| A date, count, or bound invented to avoid writing `unresolved` | retain uncertain bounds rather than invent precision (`worldbible-integration-contract.md:120`); an unverified conversion stays `(to-verify)` (`to-verify-triage-protocol.md:112`) |
| An open item closed because the round ended | a deadline never forces confirmation; unresolved rows carry owner + reopen condition, not a closure date (`to-verify-triage-protocol.md:80,181`) |
| A landed packet whose uncertainty markers disappeared | a disappearing uncertainty marker is not a verified claim (see *Using the evidence*); recheck every reused reference and unresolved id before each handoff (`to-verify-triage-protocol.md:139`) |

## Boundaries (hard)

- **Refuses canon authority.** Recording what IS true in the world, and
  consistency verification of the world bible, is lore-shokunin. This lane
  generates systems and hands them off; it never edits the world bible or
  a sibling repo.
- **Refuses real-world rights/attribution rulings** on reference works
  (attribution, rights, training permission stay distinct questions).
- **Refuses game mechanics** (game-dev-2d/3d) and **publishing** (kake).
- **Refuses general research method** — that is chousa-shokunin; this lane
  consumes cited sources, it does not own the method.
- Out-of-province evidence → report, never absorb.

## Checklist (executable where a tool exists)

- [ ] Every language system cites its typological basis (which real
      language family it draws on and why). No lane executable reads this
      item — prose gap, recorded in `reports/round-10/drift/shard-06.md` §06-G.
- [ ] Every mythic/symbolic claim names its framework and its calibration
      status (per-claim set S/C/H/R/U/V — see
      synthesis/source-discipline-calibration.md:67; `provenance-audit`'s
      `missing-calibration` family checks the declared shape only).
- [ ] Every costume/era claim couples to a term, a material, and a rule of
      who may wear it.
- [ ] Every handoff to the world bible names the recipient (lore) and the
      open questions; canon decisions are never made here.

## Corpus map

- `corpus/knowledge/linguistics/` — the language side: phonology through
  pragmatics, historical linguistics, writing, naming, contact, registers.
- `corpus/knowledge/myth-symbol/` — the mythic side: comparative frameworks,
  creation/hero/trickster taxonomies, cosmology, color/animal/number/celestial
  symbolism, ritual, folktale indexing.
- `corpus/knowledge/culture-material/` — the material side: dress through
  eras, costume semiotics, textiles, food, architecture, trade, calendars,
  craft, music, adornment.
- `corpus/knowledge/synthesis/` — the coupling (THE NICHE): decision
  tables, matrices, pipelines, the lore handoff contract, the worked
  example, source discipline.
- `corpus/knowledge/verification/` — the honesty layer: gate
  specifications, citation/provenance formats, the calibration registry,
  to-verify triage, real-world-inspiration boundaries.
- `corpus/knowledge/civilizations/` — 94 entries: 92 earlier-civilization
  bases plus two source maps (`africa-primary-sources.md`,
  `mesoamerica-primary-sources.md`), each
  coupling that tradition's language, writing, myth, symbols, era model,
  costume, and naming, with provenance cautions.

## Using the evidence

Read each entry's appended errata before using earlier tables. Source rechecks
are claim-specific: `corpus/lessons/supplement-opencode-1/sources/` records
supported, contradicted and unresolved claims with passage and access limits.
A catalogue record establishes catalogue metadata, not the unread book's
contents. A disappearing uncertainty marker is not a verified claim.

| Finding or observation | Response | Evidence |
|---|---|---|
| `A-NEUTRAL` REVIEW | Keep the contextual reanalysis and witnesses; do not call a typological warning a linguistic impossibility | `reports/supplement-opencode-1/21-phonology-review.md` |
| English garment labels fail the D2 phoneme inventory | Separate translated labels from native forms; missing native forms remain a gap, not cleared names | `reports/supplement-opencode-1/22-label-representation.md` |
| A name violates the declared coda rule | Repair the derivation in the owner ledger and propagate actual references, preserving the rejected form as historical evidence | `reports/supplement-opencode-1/04-name-correction.md` |
| A clean myth/costume verdict with omitted ledgers | Report unexercised checks; a clean supplied subset does not establish coverage or authenticity | `reports/supplement-opencode-1/23-myth-coverage.md`, `24-costume-coverage.md` |
| `CROSS-HOLD` or missing lore receipt | Retain the hold; author-side tests do not supply cultural clearance or canon authority | `reports/supplement-opencode-1/25-handoff-boundary.md` |
| Frozen replay exits 0 with recorded findings | The red verdict reproduced; the culture did not become clean | pinned-revision replay: restore each gate from the commit whose bytes match the manifest pin (the round-3 pins are the gate bytes at `291c714`), then run `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv --repo-root <isolated-tree>`; the live tree now reads exit 2, 7/7 `gate_digest_mismatch` (`reports/round-10/drift/fix-18.md`) |

## Gates and probes

Normal gate runs map 0 to clean, 1 to findings and 2 to could-not-evaluate.
`provenance-audit` reads corpus entries; `handoff-packet-check` reads the
Markdown handoff envelope; the other five read culture packets. The seven
legacy selftests pass, and five of them write only inside their own fixture
directories: a present fixture is verified byte-for-byte, a divergent one is
refused and left untouched, and only a missing one is regenerated atomically
(phonology, lexicon, myth, costume, provenance). Run that battery in an
isolated repo export; byte equality after a run does not prove no writes.
See `reports/supplement-opencode-1/29-local-boundaries.md` §F1 for the
finding that motivated the repair, and
`reports/round-8/operability/neg-controls/neg-13/neg-13-report.md` for the
current contract and its controls.

The replay tool validates SHA-256 pins and executes snapshots, never the
manifest command string. Its exit 0 means reproduction, including expected
red verdicts; 1 means mismatch and 2 means could-not-evaluate, including
`snapshot_tampered`. The round-3 TSV recording is replayable only in an
isolated tree holding the pinned gate revisions: measured 2026-10-17, the
live tree reads exit 2 with 7/7 `gate_digest_mismatch` because the round-8
admission commit (`e1694ba`) revised every gate file the pins name — restore
those files from `291c714` and the same manifest reproduces 7/7, exit 0
(`reports/round-10/drift/fix-18.md`). This does not
retrofit the protocol's separate per-gate `expected.json` layout. Round-4
output files alone remain unpinned legacy evidence.

| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |
|---|---|---|---|---|---|---|---|
| phonology-sanity-gate | gate | `python3 tools/gates/phonology-sanity-gate.py <packet.yml>` | 0 clean / 1 findings / 2 could-not-evaluate | `--selftest` (isolated export) | tools/gates/fixtures/phonology-sanity-gate.{yml,expected} | selftest verifies present fixtures; regenerates only an absent one | kotodama-shokunin |
| lexicon-coverage-audit | gate | `python3 tools/gates/lexicon-coverage-audit.py <packet.yml>` | 0 clean / 1 findings / 2 could-not-evaluate | `--selftest` (isolated export) | tools/gates/fixtures/lexicon-coverage-audit.{yml,expected} | selftest verifies present fixtures; regenerates only an absent one | kotodama-shokunin |
| myth-consistency-gate | gate | `python3 tools/gates/myth-consistency-gate.py <packet.yml>` | 0 clean / 1 findings / 2 could-not-evaluate | `--selftest` (isolated export) | tools/gates/fixtures/myth-consistency-gate.{yml,expected} | selftest verifies present fixtures; regenerates only an absent one | kotodama-shokunin |
| costume-era-consistency-gate | gate | `python3 tools/gates/costume-era-consistency-gate.py <packet.yml>` | 0 clean / 1 findings / 2 could-not-evaluate | `--selftest` (isolated export) | tools/gates/fixtures/costume-era-consistency-gate.{yml,expected} | selftest verifies present fixtures; regenerates only an absent one | kotodama-shokunin |
| naming-collision-gate | gate | `python3 tools/gates/naming-collision-gate.py <packet.yml>` | 0 clean / 1 findings / 2 could-not-evaluate | `--selftest` | tools/gates/fixtures/naming-collision-gate.{yml,expected} | read-only | kotodama-shokunin |
| provenance-audit | gate | `python3 tools/gates/provenance-audit.py <corpus-paths>` | 0 clean / 1 findings / 2 could-not-evaluate | `--selftest` (isolated export) | tools/gates/fixtures/provenance/ | selftest verifies present fixtures; regenerates only an absent one | kotodama-shokunin |
| handoff-packet-check | gate | `python3 tools/gates/handoff-packet-check.py <packet.md>` | 0 clean / 1 findings / 2 could-not-evaluate | `--selftest` | tools/gates/fixtures/handoff-packet-check.{md,expected} | read-only | kotodama-shokunin |
| frozen-replay | gate | `python3 tools/replay-frozen.py <MANIFEST.tsv>` | 0 recorded verdict reproduced / 1 mismatch / 2 could-not-evaluate | `--selftest` | manifest gate/input/output SHA-256 pins; selftest constants in script | auto-cleaned scratch only | kotodama-shokunin |
| uncertainty-inventory | probe | `python3 tools/source-audit-inventory.py --json` | 0 inventory produced, not scholarship verified / 2 could-not-evaluate | `--selftest` | exact-count fixture constants in script | read-only; selftest scratch | kotodama-shokunin |
| D2 assembly drift | gate | `python3 tools/assemble-d2.py --check` | 0 byte-identical / 1 drift / 2 could-not-evaluate | `--selftest` | committed packet, component hashes and synthetic controls in script | default mode regenerates packet; check read-only; selftest scratch | kotodama-shokunin |
| contrastive craft example | gate (bounded example) | `python3 tools/check-craft-exercise.py examples/supplement-opencode-1/sound-change-vs-taboo.json` | 0 checks pass / 1 findings / 2 could-not-evaluate for declared input errors | `--selftest` (committed example plus isolated subprocess controls; foreign cwd supported) | committed exercise and tamper/CLI expectations in script | read-only, including optional `--report <existing-report.md>` | kotodama-shokunin |
| isolated legacy selftest battery | gate | `python3 tools/check-gate-battery.py` | duty 1 (selftests): 0 seven selftests pass / 1 recognized selftest failure / 2 could-not-evaluate; duty 2 (baselines): 0 every discovered pin verifies / 2 tampered, revised or uncovered gate — exit is the worse of the two, and the committed default currently exits 2 with `BASELINE-GATE-UNCOVERED` for myth and naming, whose pins live under `reports/round-9/baselines/`; add that root via `--baselines-root` to reach 0 (`reports/round-9/baselines/registry.md` §5 item 6; `reports/round-10/drift/fix-21.md`) | `--selftest` (isolated synthetic children) | fixed seven-gate list and control expectations in script | disposable copied scripts/fixtures; optional retained mirror only when requested | kotodama-shokunin |

The contrastive checker is example-specific, not a general culture validator.
Its subprocess controls complement the ten domain mutations and a real positive
example run; they do not prove arbitrary nested schemas correct. `--counts`
returns the exercise's declared audit-count block after checks, not a new
independent source inventory. Its embedded historical counting-command string
points to ignored scratch and is not an executable instruction; use the public
entry command above. The LAW-ORDER early-return coverage limitation remains
recorded in `reports/round-5/15-cli-review.md`.

The battery runs trusted repo scripts in a copied working directory; it is not
an operating-system sandbox. Byte preservation does not prove no writes took
place. Copying contains the five fixture-writing legacy selftests but does not
repair their independent-expected-value or parser-coverage conformance debts.
Round-scoped acceptance is re-runnable with
`python3 reports/round-5/run-validation.py`; it records the two declared claims
and writes its own validation receipt. It is an orchestration check, not a new
general culture or scholarship-certification gate.

## Source-to-system constraints — round 5

| Retrieved evidence | Worldbuilding decision | Scope and pointer |
|---|---|---|
| Radiocarbon ranges change with bark-paper cleaning protocol | Separate support manufacture, painting, later use and depicted dress before assigning an era | Publisher abstract for meso-13; `corpus/lessons/round-5-sources/08.json`, `reports/round-5/parent-source-spotchecks.json` |
| Lowie gives borrowed kin terms not tied to a social institution | Borrowed relationship words alone do not establish marriage law, descent or a dowry-transfer mechanism | Lowie Chapter V passage re-fetched in parent spotchecks; combined KIN-A07/A08 residuals stay unresolved |
| A smaller avoidance vocabulary can express the same content | Model many-to-one paraphrase and register-triggered use, not one native synonym for every ordinary word | Haviland's Dixon quotation, SR-REG-07; parent spotchecks distinguish secondary quotation from unread primary pages |
| An earlier thesis supports parts of a later-book attribution | Carry version and passage scope into the design source ledger; do not merge editions into one verified claim | TIB-A12/A16 in `reports/round-5/parent-reconciliation.json` |
| A venue record corrects a phonetics citation | Repair the bibliography without treating that correction as support for an era-to-anatomy causal rule | PHON-A11 and appended erratum in `corpus/knowledge/linguistics/phonetics-phonology.md` |

## Source-to-system constraints — round 6

| Retrieved evidence | Worldbuilding decision | Scope and pointer |
|---|---|---|
| UT Lesson 2 spells IṢ-BAT as an Akkadogram but gives the Hittite reading ēpta | Store written form, reading language, copy horizon and cult provenance separately; a borrowed sign does not determine spoken language or deity genealogy | R6-05-A, parent P04; `reports/round-6/parent-reconciliation.json` keeps Hattic affiliation legs partial |
| Louvre E 12026 is catalogued as pleated linen before the New Kingdom | Reject an exclusively New Kingdom pleating date-marker for this object; require a separate pattern/technique witness before reconstructing its cut | R6-03-B, parent P02; museum technical fields and excavation-context attribution, not independent re-dating |
| Gobhila II.8.8 names ten nights, a hundred nights or one year; §14 has a translator's emendation | Model discrete school-specific timing options and keep grammatical labels edition-bound; do not implement an arbitrary “any time after ten nights” rule | R6-13-A, parent P03; exact capture and appended `india-vedic.md` erratum; Sanskrit and parallel schools unread |
| Śatapatha III.2.1 spreads skins on the ground but attaches a horn to a garment | Give ritual surfaces and worn attachments separate slots; attach school variants to their reported witnesses instead of merging a universal cloak | R6-13-B, parent P01; Kāṇva detail is Eggeling's footnote report, not an independently read recension |
| ARTA 2007.001 p. 9 describes a practical Old Persian administrative isolate and limits generalization | Allow an attested exception to a display-only register rule without turning it into general everyday usage; distinguish royal display, transaction and household language | R6-09-A, parent P05; appended `persia-achaemenid.md` erratum; Behistun cross-version and Hallock legs remain partial |

Re-run this round's receipt/count/preservation checks with
`python3 reports/round-6/run-validation.py`. The five parent readings are
separate from the twenty qualifying worker main passages; neither count
certifies whole cultures, ancient pronunciation or cultural permission.

## Source-bounded culture drill — D3 (round 7)

D3 is a small constructed model, not a recovered ancient culture and not a
repair of D2. Its four components separate language, attributed ritual,
era/material cases and evidence bridges. Read the exact bounded interface in
`reports/round-7/d3-contract.json` before editing; regenerate the packet
rather than hand-editing its derived outputs. Native forms are unscreened;
translated display labels do not enter a phonotactic test.

| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |
|---|---|---|---|---|---|---|---|
| D3 assembly drift | gate, bounded profile | `python3 tools/assemble-culture-d3.py --check` | 0 byte-identical / 1 drift / 2 could-not-evaluate | `--selftest`, isolated actual CLI | four component hashes and committed packet/projection | default rebuilds only two derived outputs; check read-only; selftest scratch | kotodama-shokunin |
| D3 evidence coupling | gate, bounded profile | `python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json` | 0 consistent supplied model / 1 profile contradiction / 2 could-not-evaluate | `--selftest`, independent committed controls and isolated subprocesses | closed source tuples/digests; optional `--frozen examples/culture-d3/expected.json` | normal run read-only; selftest disposable scratch | kotodama-shokunin |

| Condition | Decision / executable error | Evidence and limit |
|---|---|---|
| The same written L01 is read in ordinary E1 market speech and ritual E1 hall speech | Replay SC1 for ordinary speech (`fina`), but use AV1's `suma` only in its exact ritual/hall context; preserve written `pina`. Other places and L03 do not inherit the avoidance | D3 U01–U07 and `D3-UTTERANCE`; S01/BR01 transfer a written/read distinction, not a reconstructed Hittite taboo |
| A native name's displayed expected value agrees but its bases do not derive it | Recompute concat from the two E1 base forms; reject disagreement with `D3-DERIVATION`, not a hand-approved spelling | D3 N01–N06 and independent derivation control; no general morphology or historical genealogy proved |
| An English label contains spaces or sounds outside the native inventory | Keep it as `display_label`; project the constructed `native_form` only. A forbidden native spelling still receives `D3-NATIVE` | D3 label-positive/native-negative controls; separate representation is not real-language clearance |
| A source has a partial effective scope but the packet advertises scoped whole support | Use the committed parent reconciliation tuple, not the raw worker label; return `D3-SCOPE`. Check the actual ledger digest independently | S01/S05 remain partial; S03 keeps the exact archive capture. BR01–BR05 stay design-only |
| A naming institution offers discrete dates | Validate membership in the declared integer set, rejecting booleans and arbitrary later dates (`D3-TIMING`) | NR1 uses fictional [2,8,20] nights. S03's Gobhila 10/100 nights/one year is a methodological analogy, not this invented prescription |
| A ground surface is made into a garment or a worn item's material changes silently | Keep O01 unworn and verify object/material identity (`D3-OBJECT`); distinguish unavailable import routes (`D3-ERA`) | S04/BR04 transfer separate object roles; no copied sacred rite, immutable colour key or first-hand Kanva reading |
| A visitor wears prohibited imported cloth at the E1 hall assembly | Record C03 as a declared violation; reject only the false lawful entitlement (`D3-RANK`). Legacy R-01 must remain visible | RR1 is fictional. A clean new guard does not erase an honest scene violation or supply a historical dress law |
| A belief is promoted to narrator-certified truth, or screening is claimed without work | `D3-MYTH` protects attributed B01/B02; `D3-SCOPE` protects unresolved/unperformed real-language screening | Source analogy does not confer canon or community permission. The handoff stays prepared-not-accepted |

### D3 replay checklist

1. Run assembler `--check` and its isolated `--selftest`; drift or malformed
   components are not a passed culture task.
2. Run the positive guard, independent control selftest and frozen command.
   Snapshot mode verifies every listed input digest before the verdict;
   boolean exit labels and unsafe manifest paths are rejected. The committed
   manifest is deliberately comprehensive; the generic reader requires only
   packet coverage and does not infer artifact roles for the caller.
3. Run legacy naming and costume checks on `packet.gates.yml`. Keep naming's
   CROSS-HOLD (and E0/E1 similarity review) and C03's costume R-01 finding;
   neither is a green clearance gate. Verify the native coda adapter, not
   merely a permissive synthetic fixture.
4. Compare the handoff's glossary, names, source bridges and digest rows
   against actual packet bytes, then run its structural envelope check.
   Sixteen fields and twenty glossary rows alone cannot prove content agrees.
5. Run `python3 reports/round-7/run-validation.py` for the original F/O
   thresholds, input preservation and old-surface regressions. It writes its
   own receipt, not historical receipts. Fresh source access and invented
   model consistency are causally separate checks.

The frozen reader ignores extra metadata keys, compares finding IDs as a set
and allows symlinks whose resolved target remains inside the repo. These are
limits of this bounded interface, not a claim of universal schema/security
validation. Legacy parsers and D2's twenty expected findings remain unchanged.
Read `reports/round-7/integration-attempts.json` for corrected failures and
`native-request-binding.json` for the actual prompt's non-verbatim step-6
defect; passing example checks do not erase protocol-conformance debt.
