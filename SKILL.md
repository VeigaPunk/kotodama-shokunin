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
rejected (`tools/harness/packet_uncertainty.py:205,209`; v2-design §2.3 = `reports/round-15/handoff/v2-design.md:126,131-139`; erratum 2026-10-19: contract `:183` carries the delivered-record checklist item, not basis hygiene).

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
`examples/culture-d4/expected-holds.json`. Gate input is the source packet (`packet.d4.yml`), never the typed packet — feeding it back reads a false red (exit 1, 14/16 legs, measured 2026-10-18 round-24 cold run).

| Condition on the record | Routing row | Hold it carries | Never | Wrong-shape consequence |
|---|---|---|---|---|
| A checked field holds a reader-facing gloss (kind `translated-label`) and no native/borrowed form is supplied | **exactly one** row naming the record: `source_field` → the moved field, `off_channel_field` → its `_gloss` rename, `channel: off-sound-and-identity` | one `FORM-UNRESOLVED` hold whose `where` is the record id | delete the gloss to "clean" the gate — the gloss is moved and still rides in the typed packet; a row without its hold; a hold without its row | the gate's `L3-routing-consistency` fails, naming `holds … vs routed …`; a deleted hold is caught by `L3-holds`/`L3-counts`/`L3-baseline-set` naming the record (`reports/round-18/d4/neg-1.md` §3.1-§3.2) |
| The owed slot is itself a projected record (the packet's `form_slots` block) | a **second** row naming the slot record, with `owed_slot` set to that slot id and the same `source_field`/`off_channel_field` | a second `FORM-UNRESOLVED` hold whose `where` is the slot id, with the **identical** `detail` | count the two rows as two obligations — they are one obligation seen from the slot side (`reports/round-18/d4/review-1.md` §0-§1 derives six obligations from six costumes) | an under- or over-counted set; the gate's slot comparison (`hold_slots == routed_slots`) fails |
| The record carries a `register` (or any social/stylistic) field but its form is on-channel | **no** row: the record keeps its checked form | none from this field | promote the register value into `off_channel_field`; let a register label remove a string from the checked channel | a register-scoped exemption is the round-8 T1 violation at a new address — `adding typing fields cannot exempt a string` (`SKILL.md:47`) |
| A hold is laundered (downgraded to a note, or deleted) while the artifact still assembles | unchanged | the hold must still be present at `hold` severity | accept a shorter/quieter hold set as clean | four legs fail naming the record: `L3-holds`, `L3-notes`, `L3-counts`, `L3-baseline-set` (`reports/round-18/d4/neg-1.md` §3.1) |
| The family's design names a register hold class the engine cannot prove | no row; the class is reported, not written | the **emitted** vocabulary governs the expectation file | assume a `D4L-REGISTER-UNRESOLVED` (or any) id the delivered projector never emits | an expectation naming an unprovable class cannot equal the emitted set; the freeze rule excludes a row the gate cannot prove (`reports/round-17/d4/typed-support-2.md` §4 freeze rule 2; `reports/round-18/d4/holds.md` §3) |
| A label is retyped from `translated-label` to `native-form` to make the row disappear | the row must disappear **only** when a supplied native form exists | the hold clears only on a supplied form | retype a gloss as native to drop its routing row | the sound channel then grades translated text as a surface form; the naming kernel reads it as a `PHON-INVENTORY` artifact and the channel differential names the record (`reports/round-18/d4/neg-2.md` §3.1) |

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
  (`tools/d2-typed-labels.py:639`, `:808-814` at the round-24 baseline `8fbcee9`;
  cited `:622`, `:793` at the round-18 bytes `e571894` — the round-22 family-dispatch
  edits shifted both blocks down; `reports/round-18/d4/holds.md` §4).
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
  (`SKILL.md:47`, `corpus/knowledge/synthesis/era-language-staging.md:111`
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
| Determinism | two consecutive builds are byte-identical, and `--check` compares bytes without writing | a build whose output embeds a path, a timestamp, or a host name | the artifact is not replayable; a frozen pin moves under an unrelated edit | `tools/assemble-d4-typed.py:387` (`two consecutive builds are not byte-identical`; cited `:369` before the round-22 `carry_findings` block landed above it); `reports/round-18/d4/determinism.md` §3 |
| Pre-registration | the expected set is decided elsewhere **before** the tool runs (design table, design-doc union, or a declared acceptance criterion) and any delta is dispositioned in a filed reconciliation | write the expectation from the tool's own printed output | the equality leg has drift teeth but no content teeth — it cannot distinguish "the set is right" from "the set is a copy of the producer" | `reports/round-18/d4/review-2.md` §0/§2 (the landed D4 file equals the projector's live output verbatim); `reports/round-18/d4/holds.md` §3-§4; `corpus/knowledge/verification/verification-independence-anti-circularity.md` §2 (the circularity catalog) |
| Passenger rows | a row emitted by a shared engine for any packet is attributed **per packet** in the expectation, or excluded | let a packet-independent block silently enter a new family's debt set | the equality leg is described as verifying the new family's design debt while the row names records that occur zero times in its packet | measured: the D4 expected file carries 3 `D2L-RANK` holds + 1 note naming `TR-04#a\|TR-06#a`, `WR-02#g\|WR-09#g`, `WR-08#g\|WR-09#g`, `SR-01#a\|SR-01#b`, each **0** hits in `examples/culture-d4/packet.d4.yml` (2026-10-18T11:32Z; **erratum 2026-10-18, round-24 audit:** the committed `expected-holds.json` post-repin carries counts hold:12 / note:0 / fail:0 with zero `D2L-RANK` rows and zero notes — the 3+1 passenger set is the superseded pre-fix expectation, preserved at `reports/round-22/bleed/analysis.md:101` and in the file's `revision_note`/`supersedes_pins`, see T4 below); `reports/round-18/d4/review-4.md` §2; `reports/round-18/d4/holds.md` §5 |
| Freeze-artifact naming | a freeze receipt that is not a battery baseline is not named `expected.json` under a battery root | land a `freeze-receipt.json` under a name the battery discovers as a baseline | the standing battery fails closed on a gate outside its name constant | `reports/round-18/d4/manifest.md` §6 |

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

### Family-clean projection — a family's owned fields cite that family's own records

A multi-family projector selects data and provenance by the input packet's
declared family **before** constructing labels, rank ledgers, coverage, or
findings. Shared parser/gate code, tool paths, and diagnostic vocabulary may be
reused; another family's fixture records, bare component citations, owner
labels, romanization schemes, residuals, or conflict findings may not appear in
family-owned fields. Identity is at least `(family, source block/component,
record id)` — `GAR-01`, `WR-01`, or `E0` alone is not an identity, and a
same-ID foreign record is never reinterpreted as a local one. A declared
linguistic borrow ledger is not permission to borrow fixture data. Determinism
is not isolation: the pre-fix D4 projection passed its canonical gate 19/19
while carrying D2's 21-component rank fixture
(`reports/round-22/bleed/repin.md:15,18`; the rejected reading "deterministic
means family-clean", `corpus/lessons/round-22.md:63`). Executable authority
`tools/d2-typed-labels.py` (family dispatch `:2837-2838`; boundary checks
`P-FAMILY-SOURCE`/`P-FAMILY-RANK` `:2636-2732`; family-boundary controls
`_selftest_family` `:2980`; selftest 163/163,
`reports/round-22/bleed/impl.md:54,70`); design authority
`reports/round-22/bleed/design.md` (R22-D03); measured defect basis
`reports/round-22/bleed/analysis.md` §C1-C3; normative boundary
`examples/culture-d4/components/01-brief.yml:55-75,111-121`; worked instance
`examples/culture-d4/typed-labels.d4.yml` with
`examples/culture-d4/expected-holds.json` (counts hold:12 / note:0 / fail:0,
`supersedes_pins` naming the pre-fix projection/projector digests).

**Injection-point warning — an embedded-fixture builder invoked before family
dispatch injects the default family into every family.** At the round-21
baseline `46a03257…`, `run_pipeline` called `build_payload()`
**unconditionally** (`tools/d2-typed-labels.py:2613` at that revision),
packaging the embedded D2 constants (`:925-1197`) through a helper with **no
packet/family argument** (`:1235-1258`); the family alias leg invoked
afterward (`:2614`) annotated the foreign ledger without making it local. An
embedded fixture needs no disk read: with `load_packet_file` replaced by a
raising sentinel, `build_payload()` still returned the exact D2 ledger,
byte-equal to the filed D4 `rank_rules` (2/2 helper probes,
2026-10-18T14:42:15Z, `reports/round-22/bleed/analysis.md` §C3). A
foreign-tree-free rebuild therefore proves dependency isolation, not data
isolation. The landed dispatch (`tools/d2-typed-labels.py:2837-2838`:
`build_payload()` only when `family == DEFAULT_FAMILY` (`:2471`), else the
packet's own `family_rank_payload`) is the shape to preserve; add every new
family leg on the family side of that line.

| Paired control (design §Required paired controls) | Positive must show | Defect it defeats — Never | Landed control | Citation |
|---|---|---|---|---|
| D2 compatibility | the baseline D2 serialized projection keeps digest `a3aa452c…`; D2 `--check`/selftests pass; a D2 rank mutation still moves D2 | achieving compatibility by disabling rank projection globally | `boundary compatibility: D2 projection keeps its exact baseline digest`; `boundary D2 control: D2 rank projection remains enabled and responds to D2 mutation` | `tools/d2-typed-labels.py:3114,:3119`; digest at `reports/round-22/bleed/analysis.md:18` |
| D4 independence | a D4 packet-only mirror is byte-identical with no `examples/culture-d2/` tree **and** poisoning the embedded D2 fixture hooks (raising sentinels) leaves D4 output identical; the pre-fix artifact is refused semantically | reading filesystem absence as data isolation (the C3 result) | `boundary: packet-only D4 mirror is byte-identical without a foreign tree`; `boundary poison control: D4 never calls embedded D2 fixture machinery`; pre-fix bytes refused `P-FAMILY-SOURCE … GAR-01.owner: foreign owner '11-costumes'` | `tools/d2-typed-labels.py:3045,:3053-3054`; `reports/round-22/bleed/analysis.md:103-110`; `reports/round-22/bleed/impl.md:64` |
| Not empty-by-default | mutating declared `RK-01` authority/property/rank moves only the corresponding D4 projection; add/remove of one valid RK row moves coverage exactly once; malformed or duplicate declared records fail closed | replacing the foreign ledger with empty arrays and calling the family clean | `boundary local control: RK-01 authority/property/rank follow the local packet only`; `boundary coverage control: … counted exactly once`; `boundary malformed local rank set … fails closed` | `tools/d2-typed-labels.py:3063,:3073,:3099`; shape checks `P-FAMILY-RANK` `:2694-2732` |
| Owner-qualified citations | an absolute foreign citation, a short component citation, or a foreign owner/scheme injected into a family-owned field is rejected, while genuine `WR-*` orthography IDs and shared tool/schema references pass | a whole-document substring ban on the family token (it would reject method provenance and the packet's own contrast declarations) and any unqualified foreign citation passing | `boundary control: deterministic D2-owned label metadata is rejected`; `boundary control: foreign label … rejected`; `boundary: D4 WR writing ids and shared engine references are not substring-banned` | `tools/d2-typed-labels.py:3011,:3024,:3032`; `WR-*` are D4's own rules, `examples/culture-d4/components/03-orthography.yml:83-90` |
| No ID-based reinterpretation | same-ID foreign records fail ownership checks while the six local owed slots still route to their garments; ordinary era tags never import foreign eras | treating a shared ID or era tag as ownership evidence (D4 `GAR-01`/`GAR-06` keep D4 ranks/text, never a foreign `RANK_RESOLUTIONS`) | `boundary explicit same-id foreign label: emit refuses and preserves … output` | `tools/d2-typed-labels.py:3109`; identity definition `reports/round-22/bleed/design.md` §Decision |
| Honest borrowed language | the six `borrowed-strata` labels keep packet-declared donors, layer refs and adaptation rules; an undeclared donor in an owned source field stays a failure | legalizing an embedded fixture block by relabeling the ledger borrowed | `boundary: label texts, kinds, owed slots and all six borrow ledgers unchanged`; D4 no-import rows `D2B-01..04` | `tools/d2-typed-labels.py:2989`; `examples/culture-d4/components/01-brief.yml:111-121` |
| Propagation/tamper | a stale projection pin, a stale expected-hold set, or one changed typed routing byte fails the gate/adapter checks; a clean regeneration passes with new rows | re-blessing pins in place, freezing while upstream moves, or letting inherited findings ride into consumers | consumers copy the projector's own finding set (`carry_findings`); frozen generation `tools/gates/frozen/round-22/d4-repin/MANIFEST.tsv` (3 rows, exit 0 — requires TMPDIR outside the repo, `mirror_unsafe` exit 2 otherwise, measured 2026-10-18 round-24 cold run; deployed replay 33 peer pairs, 2026-10-18T14:56:01Z); profile row `$.profiles[0]` with `repin_history[2]` binding projector+expected; stale pins refuse exit 2 `L1-profile` | `tools/assemble-d4-typed.py:276-288`; `reports/round-22/bleed/evidence/deployed-replay.json`; `tools/gates/typed-pipelines.json`; `reports/round-22/bleed/impl.md:60` |

Thresholds and cautions that are part of the rule:

- **T1 — check owned fields structurally; substring bans are not ownership
  checks.** Explanatory negative provenance ("the foreign component was not
  read"), shared engine paths, and the receiving family's own reused ID space
  are legitimate; the structural checks above are the boundary
  (`reports/round-22/bleed/design.md` §Reusable machinery;
  `reports/round-22/bleed/analysis.md:60`; control
  `tools/d2-typed-labels.py:3032`).
- **T2 — equality and isolation are independent.** A deterministic projection
  can deterministically reproduce the wrong family; a byte-equality pass never
  grounds a family-ownership claim (`reports/round-22/bleed/repin.md:15,18`;
  poison control `tools/d2-typed-labels.py:3053-3054`).
- **T3 — both halves of every pair, or the fix is cosmetic.** The mirror
  control without the poison control proves dependency isolation only; the
  poison control without a local-packet mutation control cannot distinguish
  real selection from empty-by-default (`reports/round-22/bleed/analysis.md`
  §C3; `corpus/lessons/round-22.md:53`;
  `reports/round-22/bleed/design.md` §Required paired controls).
- **T4 — obligations and history survive a data cleanup.** Removing inherited
  findings removes misattribution, not debt: the six owed garment forms remain
  held (12 holds), and the removal is recorded as new rows with before/after
  digests (`examples/culture-d4/expected-holds.json` `revision_note` +
  `supersedes_pins` → pre-fix projection `cbcf997f…`, projector `76536a92…`;
  append-only discipline
  `corpus/knowledge/verification/gate-frozen-run-standard.md:50-78,102-142`;
  keep historical verdict / current reproduction / supersession distinct,
  `corpus/lessons/round-22.md:19`).
- Cautions that are part of the rule: this is an engineering boundary, not a
  canon, lore-acceptance, or real-world rights decision — handoffs stay
  prepared-not-accepted (`reports/round-22/bleed/design.md` §Decision final
  sentence; `reports/round-22/bleed/analysis.md` §Handoff limitation). A
  family-local leg the packet does not declare is reported as an explicit
  skip, never counted as evaluated (`tools/d2-typed-labels.py:3343`;
  `reports/round-22/bleed/design.md` "Source-level change contract" item 3, :17 —
  cited §3 before the round-24 audit; the file has no numbered sections).

**Round-25 implementation commitment.** Round 22 closed REJECTED on D and
routed the remaining integration to round 25 with the full recipe
(`LOG.md:3298-3309`; `reports/round-22/routed-resolution.json`
R21-ALIAS-COERCION, R21-MTIME-TIE-BREAK). Landed at the round-23 baseline
`0e81d9d`: the family-clean projector (`2819f687…`), the regenerated D4
projection/typed packet/expected holds, the combined-source profile row
(`repin_history[2]`), and the frozen `d4-repin` generation. Committed to
round 25: (1) a superseding handoff v3 claim map/baseline — D4-CL05/06/07/09
and OQ-V3-05 still describe the removed rank passengers
(`reports/round-22/bleed/repin.md:26-37`); (2) the PLACEHOLDER_RE
validator-wording disposition, so the full historical check runs without
weakening any placeholder rule (`reports/round-22/routed-resolution.json`
R21-MTIME-TIE-BREAK); (3) any combined-source successor row (D2 live/frozen
pins, v2) not landed under round 23's O claim
(`reports/round-23/claims.json` O). Until each lands, this rule's per-row
verification status is stated as landed or pending — never retroactively
green — and filed historical wording is not rewritten
(`corpus/lessons/round-22.md:19`).

<!-- END R23-D SKILL SUBSECTION -->

### Register craft

Build a register as three linked objects: a **typed stratum of forms**, a
**law over speech acts**, and a **replayable delivery**. A register value says
who uses a form and in which situation; it does not decide whether the bytes
are native, borrowed, or a translated label. A derivation pass proves neither
the law nor the register's semantic coverage. This subsection composes, rather
than replaces, *Label typing*, *Claim uncertainty typing*, *Slot-label routing*,
*Derivation replay*, and *Family-clean projection* above. Design authorities:
`reports/round-26/register/design.md` §§2–6,
`corpus/knowledge/linguistics/register-strata-attestation.md` §§1,4,7–8 and §13,
and `corpus/knowledge/linguistics/register-lexicon-ceilings.md` §§3–5,10.
The D4 furnace-league is a NON-CANON worked case, not a real-language model or
an accepted world-bible record (`reports/round-29/adjacency/register-law.md`
§Verdict).

#### Stratum discipline — select an operation, then test its domain

| Condition | Do | Never / boundary | Evidence |
|---|---|---|---|
| A form carries a marked register | Type its form channel first; keep supplied native and recipient-adapted borrowed forms on the sound-and-identity channel. Only a translated label without a supplied form is moved, with its owed-form hold | Give `stamp`, `ritual`, or `trade` a private inventory, or use register as an exemption flag | `reports/round-26/register/impl.md` §5; `examples/culture-d4/components/04-lexicon.yml` `registers` / `QREG-02`; `corpus/knowledge/synthesis/era-language-staging.md` §7 |
| A stratum is derived from the delivered lexicon | Resolve the base in the same family's packet; name the base record, `derived_from`, `doublet_of`, operation and candidate. In D4 `QREG-03` selects `mark → reverse`, `fire → lengthen` from the **base's** axis | Choose the operation from the desired spelling, borrow an absent forecast record, or mistake replay of an arbitrary declared operation for enforcement of the axis selector | `reports/round-26/register/rules.md` §2; `reports/round-26/register/impl.md` §§1,3; `tools/gates/argot-derivation-gate.py` `declared_derivation` / `evaluate_packet`; `reports/round-29/defects/routed.md` §`R26-ARGOT-DERIVATION-IDENTITY-AND-PAIR-SCOPE` |
| The selected operation must replay | Use the declared computed operation or a machine-readable `morphology.derivation_rules` pattern/output pair. `reverse` reverses characters; the landed `lengthen` rule doubles the first vowel and its id is lowercase `lengthen`, exactly matching `derivation.op` | Treat the design's uppercase `LENGTHEN` as the landed id; confuse character reversal with syllable reversal; claim that first-vowel doubling handles every stress pattern or diphthong | `examples/culture-d4/components/04-lexicon.yml` `morphology.derivation_rules` / `derivation_spelling_note`; `reports/round-26/register/rules.md` §§3.1,4 RU-1/RU-2; `reports/round-26/register/impl.md` §4.2; `tools/gates/argot-derivation-gate.py` `OP_FUNCTIONS` / `replay_rule` |
| An operation yields the stated bytes | Check recipient inventory, syllables, collisions and identity separately; report missing bases, malformed pairs and unresolved rules as debt. Arithmetic equality is not that entire check set | Read an argot exit 0 as proof of base ownership, phonotactic legality, non-identity, label typing, era legality or complete coverage | `tools/gates/argot-derivation-gate.py` §Calibration / `evaluate_packet`; `reports/round-29/defects/routed.md` §§`R26-ARGOT-DERIVATION-IDENTITY-AND-PAIR-SCOPE`, `R26-ARGOT-LABEL-TYPING-AND-REGISTER-SCOPE`; `reports/round-26/register/impl.md` §3 |
| The institution needs a semantic field | List its required acts, offices, obligations and measures **before** selecting the operation. Measure `semantic class × operation-legality` over named delivered bases, with the exact legality call, reader digest, packet digest, command and date | Call an operation total because it selects an operation for each axis; apply a one-syllable predicate to a whole word; assume a legal identity truncation makes a useful marked form | `corpus/knowledge/linguistics/register-lexicon-ceilings.md` §§3–5,10; `reports/round-28/argot/D20-ceiling-wording.md` §§1–4; `reports/round-26/register/rules.md` §§2,3.2 |
| The operation cannot supply a needed form | Choose and record the price: hand-pick/replace the bases, choose or amend the operation, or accept the ceiling and declare the paraphrase/substitution/other record channel that carries the missing term | Coin more instances under an unchanged illegal transformation, relax the inventory to legalize one desired word, or infer that a missing derived word makes its concept inexpressible | `corpus/knowledge/linguistics/register-lexicon-ceilings.md` §§2,5,10; `corpus/knowledge/linguistics/register-strata-attestation.md` §6 and §13 |
| A register has an institutional era | Carry its availability window with the forms and law. D4's `stamp` is available from E1; E3 is reserved, not a substitute historical attestation | Present an era declaration as an executed era check: the argot arithmetic leg does not implement that institution-date test | `reports/round-26/register/design.md` §5; `reports/round-26/register/rules.md` §5; `examples/culture-d4/components/04-lexicon.yml` `QREG-04`; `examples/culture-d4/components/13-register-law.yml` `RGL-05` |

Worked ceiling, measured **2026-10-18T21:53:04Z** with
`python3 -B reports/round-28/ceiling/measure-ceiling.py`: reader `b5406bcd…`
over the pre-integration packet `543d68a8…` finds **19 legal / 8 illegal**
among **27** mark-axis plain words; the named institutional abstraction set
has **1 legal / 4 illegal**. `L-45 tikmes → sem.kit` is the surviving
abstraction; `L-30 gis → sig` is not legal. This supersedes the pre-fix
reader's 18/9 and 0/5 readings, without rewriting them. Test legality
**per syllable**: `all(is_legal_syllable(s) for s in syllabify(form))`.
The base-initial-coda predicate agrees on that measured population, not on
every possible language or arbitrarily shaped input. The transferable result
is the check over the **operation + base list + phonotactics + reader**, not
this fixture's ratio (`corpus/knowledge/linguistics/register-strata-attestation.md`
§13; `corpus/knowledge/linguistics/register-lexicon-ceilings.md` §§4,10;
`reports/round-28/argot/D20-ceiling-wording.md` §§3–4). Read the ceiling entry's
phrase-absence evidence with the separate qualification
`reports/round-30/fixes/x63-f2.md` §Applied amendment: that evidence correction
changes neither the measured arithmetic nor the declared ceiling.

#### Law discipline — speech acts are not lexical or costume properties

| Condition | Do | Never / boundary | Evidence |
|---|---|---|---|
| A register is meant to make speech bind | State each act as a row: speaker/authority, venue/slot, procedure, force, record consequence and penalty shape. Use the speech-act classes as a design checklist; declarations need an authorizing institution | Treat a register identity row, vocabulary list or prose claim that “the word binds” as a replayable law; assert that the delivered checker evaluates every felicity condition | `corpus/knowledge/linguistics/register-strata-attestation.md` §§1–4,8; `reports/round-27/law/design.md` §§1,3; `reports/round-28/law/design.md` §§1,3.5 |
| An act fails its conditions | Distinguish **misfire** (act void/not performed) from **abuse** (act performed, speaker sanctionable); state the record effect separately from the penalty | Infer that every wrong act merely incurs a fine, or that every sanction erases the record | `corpus/knowledge/linguistics/register-strata-attestation.md` §§2–3,10 RSA-3 |
| A speaker's rank authorizes an act | Link the law row to the delivered authorizing rank/rite/institution record. Keep law over speech in `register_law`; keep costume/material permits in their own ledger | Add `register` to a costume-rule membership guard and call it enforcement: the costume resolver can fall through to `not-applies` without a speech target | `reports/round-27/law/design.md` §§3.1,4–5; `corpus/knowledge/linguistics/register-strata-attestation.md` §7; `reports/round-28/law/impl-1.md` §§1–3 |
| The design and delivered law disagree | Name both row sets and scope the claim to the delivered wording. D4 `RGL-02` refuses a binding stamp oath; do not substitute the historical round-27 positive `QREG-06` proposal for it. `RGL-03` enters the guest act under a stamp-name while restricting the guest's furnace-roll access | Equate `not-rollable` with no record of any kind, silently resolve competing oath scopes, or turn a proposed QREG id into a delivered record by citation alone | `examples/culture-d4/components/13-register-law.yml` `RGL-01` / `RGL-02` / `RGL-03`; `reports/round-27/law/design.md` §3; `reports/round-28/law/design.md` §3.1 |
| Law rows reach a packet | Name their component owner, packet key, declared fields, assembler validation and delivered record links. Recheck the assembled **record** set, not a substring in a component | Read “present in source”, “read by the auditor”, “validated by assembly” and “enforced” as synonyms; let `design_row` point to nonexistent QREG records | `corpus/knowledge/linguistics/register-strata-attestation.md` §4.1 and §10 RSA-9; `reports/round-28/law/impl-1.md` §§2–3; `reports/round-29/defects/routed.md` §§`R28-LAW-REGISTER-ROW-ASSEMBLY-VALIDATION`, `R28-LAW-DANGLING-DESIGN-ROW-REFERENCES` |
| The law is replayed | Invoke `tools/gates/register-law-gate.py` on the source packet. Its `evaluate_packet` checks delivered references, declared register names/ids, force vocabulary, consequence machinery, axes/kinds and expected row presence within its stated scope; retain each emitted finding's severity | Copy an early design's all-HOLD severity onto the executable's FAIL findings; call string/record resolution a simulation of authority, polarity, delegation, uptake or record transactions | `tools/gates/register-law-gate.py` §Finding ids / §Calibration / `evaluate_packet`; `reports/round-28/law/design.md` §§3.2,3.5,5; `reports/round-29/defects/routed.md` §§`R28-LAW-FORCE-OVERMATCH`, `R28-LAW-CONSEQUENCE-AND-SPEAKER-BLINDNESS` |
| A law checker or cited row changes | Pair the clean input with named negative controls for force, speaker, consequence and missing/dangling rows; compare finding identities and messages, not only their count. Include the tokenless speaker shape as distinct from `Name (ZZ-99)` | Call a token-bearing tamper proof of tokenless-speaker coverage; call equal finding counts identical findings; bless a broken clean baseline from the producer's output | `tools/gates/register-law-gate.py` `selftest`; `reports/round-29/defects/routed.md` §`R28-LAW-CONSEQUENCE-AND-SPEAKER-BLINDNESS`; `corpus/knowledge/verification/verification-independence-anti-circularity.md` §2 |

#### Composition and delivery — preserve every type and every obligation

| Pipeline boundary | Required invariant | Wrong reading to reject | Evidence |
|---|---|---|---|
| Family → label type → register scope | Select family-local records first; keep provenance-based `native-form` / `borrowed-strata` / `translated-label` independent of register. Loans retain donor/adaptation and separate entry/referent clocks | A legal register form proves native provenance; a declared linguistic loan licenses foreign fixture data | `reports/round-22/bleed/design.md` §§Decision,Required paired controls; `reports/round-26/register/impl.md` §5; `corpus/knowledge/synthesis/loanword-material-dating.md` §§2–3 |
| Typed labels → adapter → routing/holds | The family's own assembler is the identity authority; move gloss fields by text transform, never delete or re-serialize the foreign packet. The routed record set equals the owed-form hold set; distinguish obligations from record/slot rows | A register label moves supplied sound bytes off-channel; removing inherited fixture findings or adding supplied register forms discharges the unrelated garment obligations | `reports/round-17/d4/typed-support-1.md` §§4–5; `reports/round-18/d4/holds.md` §4; `reports/round-22/bleed/design.md` §Integration obligations; `reports/round-26/register/impl.md` §5 |
| Form replay + law replay → gate result | Run both legs. The generalized typed gate has `L3b-argot`; that leg admits argot HOLDs while rejecting FAILs/input refusals. Run the separate law gate even when typed routing is green | A typed-pipeline pass implies a clean law, or `L3b-argot` means no argot debt. Gate exit 0 is scope-specific, not clearance | `tools/gates/typed-pipeline-gate.py` `evaluate`, `L3b-argot`; `tools/gates/register-law-gate.py` §Calibration / `main`; `reports/round-28/law/impl-1.md` §§5–6 |
| Read-set pins → frozen replay | Name every input; keep commands flagless where the replay interface requires it; record re-pins as new rows and verify the pinned dependency closure. Keep reproduction, mismatch and could-not-evaluate distinct | Overwrite a filed manifest, equate a pin match with a fresh verdict, or claim isolated snapshot replay while a ROOT-relative peer reads the live tree | `reports/round-18/d4/manifest.md` §§2,6; `corpus/knowledge/verification/gate-frozen-run-standard.md` §§4,6; `reports/round-29/defects/fix-14.md` §§Instrument limitation found later,Route |
| Checks → claim ledger → lore handoff | Give each claim its own resolving basis and `supported` / `partial` / `unresolved` status; preserve restrictions and owner/reopen questions on unresolved law, era, ceiling and source legs | Promote arithmetic support onto an untested institutional edge, digest equality onto semantics, or a prepared packet onto lore acceptance/canon | `reports/round-15/handoff/v2-design.md` §2; `corpus/knowledge/verification/to-verify-triage-protocol.md` §2; `corpus/knowledge/synthesis/worldbible-integration-contract.md` §§4,8; `reports/round-29/adjacency/province-entries.md` §§Province and contract boundary,Deliverables reviewed |

#### Executable entry points and supporting helpers

Use the **source** packet, not the derived typed packet, for the normal entry
commands:

```sh
export TMPDIR=$PWD/.scratch
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
```

Argot and law use 0 = no reported findings, 1 = findings, 2 =
could-not-evaluate; `--selftest` is a capability check, not a measurement of
every packet. The typed gate's 0 instead means equality with its pinned
expected findings. All three interfaces are documented in their module
docstrings (`tools/gates/argot-derivation-gate.py`,
`tools/gates/register-law-gate.py`, `tools/gates/typed-pipeline-gate.py`).

These previously implicit supporting surfaces are named so the craft index is
not mistaken for a smaller executable inventory. Helpers are not independent
culture-clearance gates, and a historical baseline must not be silently
replaced by the latest bytes.

| Surface | Role / entry contract | Evidence |
|---|---|---|
| `tools/exercise-handoff-e2e.py` | v1/v2/v3 handoff exerciser; `--profile v3 --baseline <authorized-successor>/expected.json` selects the intended generation instead of silently blessing stale prose/pins | module docstring §§Profiles,Assertions; `reports/round-29/defects/routed.md` §Fresh v3 renderer claim drift |
| `tools/assemble-d2-typed.py` | D2 typed adapter; `--check` compares the typed packet without regenerating it; D4 uses its own adapter rather than borrowing D2's build | module docstring §§Interface,Fail-closed rules; `reports/round-17/d4/typed-support-1.md` §4 |
| `tools/gates/d4-assembly-check-gate.py` | flagless frozen-row adapter: `<source-packet>` must equal the D4 assembler's own build; 0 identity / 1 drift / 2 could-not-evaluate | module docstring and `main`; `reports/round-18/d4/manifest.md` §2 |
| `tools/gates/d4-typed-labels-check-gate.py` | flagless frozen-row adapter: `<projection>` is checked against the D4 **source** packet; forwards the projector's `--check` byte-identity verdict: 0 identical / 1 drift / 2 could-not-evaluate, not the label-findings verdict | module docstring and `main`; `reports/round-18/d4/manifest.md` §2 |
| `tools/harness/packet_links.py` | claim/edge link resolver, `--packet <machine-twin> --json`; path/token/line links must resolve against the manifest and live bytes | module docstring §§Inputs,CLI; `reports/round-15/handoff/v2-design.md` §3 |
| `tools/harness/receipt_guard.py` | receipt-write preflight; rejects committed-receipt writes by default, not a sandbox or permission to refresh historical evidence | module docstring, `guard_receipt` / `round_runner_main` |
| `tools/harness/r8_checks.py` | internal round-8 parent-receipt identity/deduplication module; `--measure` reads the old inputs without rewriting their filed receipt | module docstring §§Corrected semantics,Modes |

Run scratch-writing tools only after `export TMPDIR=$PWD/.scratch`; a
mirror-safety leg that rejects an in-repo temporary directory requires its own
external temporary directory (for example `/var/tmp`) and an explicitly
pinned input/dependency set. A refusal is not a failed linguistic judgment.
The historical replay-isolation caveat remains routed until its own paired
control closes it (`reports/round-29/defects/fix-14.md` §§Instrument limitation
found later,Route; `reports/round-29/defects/routed.md`
§`R28-FROZEN-REPLAY-USES-LIVE-TREE`). All register choices here remain
NON-CANON, with no real-language resemblance, cultural-permission, rights or
lore-acceptance claim (`corpus/knowledge/linguistics/register-strata-attestation.md`
§§11–12; `corpus/knowledge/linguistics/register-lexicon-ceilings.md` §§10–11).

### Registry correction chains

The registry's correction mechanism is append-only: a defective row keeps its
cells and a new row whose `teaches` opens `supersedes S### —` carries the fix.
A chain is *settled* only when exactly one of the five states below holds;
otherwise it is correction debt. The taxonomy is not prose: it is the lane's
own re-runnable check (`python3 -B tools/check-supersession-settlement.py
--selftest`, registry row S859), and the counter that gates it is
`python3 -B reports/round-69/accept-o.py` (7/7). Disposition authority
`reports/round-68/dispositions/dedup-ledger.tsv` (82 ruling rows; header
`:1-6`); round-68 ruling record `LOG.md:4214`. The table is opened as registry
row S859 (own-work, tier A).

| State | Row shape | Writer's next action | Error signature | Evidence |
|---|---|---|---|---|
| pending | successor opened (`supersedes S### —` in its teaches), neither side `rejected`, and no settled shape holds — e.g. successor `queued`, or `mined` with no `used-by`, or both `mined` without the limiter | rule the chain: apply the cell change first (repoint + deactivate, reject the successor, or write the limiter), then record the ruling in the disposition ledger — the validator refuses `activate` while the row still reads `queued` (`:207-208`) and refuses `retire` / `keep-reject` unless the row reads `rejected` (`:209-212`), so the data comes before the ruling | chain-left-pending | S859 — tools/check-supersession-settlement.py:132 (scan gate `:167`); the 34 chains ruled at settlement: reports/round-68/dispositions/dedup-ledger.tsv:1-6; LOG.md:4214 |
| settled-active | successor `mined` with a non-`—` `used-by` cell (path existence is reported as `missing_paths`, not gated, `:162-164`); target `queued` (deactivated: `used-by` cell reads `—`) | repoint the entries: inline citations move to the successor's id; the target's deactivation lands in the same settlement, not before (ledger mechanisms `repoint`, then `deactivate`) | entry-not-repointed | S859 — tools/check-supersession-settlement.py:127; ruling S044>S034 `activate` reports/round-68/dispositions/dedup-ledger.tsv:7, target row `:41` |
| settled-retired | successor `rejected` — the correction was audited and refused; the target keeps its own status and `used-by` (typically still `mined`) | keep the target: record the refusal (ruling `retire`); if a mutation already touched target cells, flip them back (`cell-flip`, S186); when the frozen ruling vocabulary lacks a target-retained class, note the true disposition in the ledger | retired-row-mined | S859 — tools/check-supersession-settlement.py:125; `cell-flip` S186>S157 reports/round-68/dispositions/dedup-ledger.tsv:19; forced retire S490>S379 `:30` (R68-M2, corpus/lessons/round-68.md:92) |
| settled-closed | the superseded **target** is `rejected`; the successor's own status is free — `mined` over a rejected target is the common case (10 of the 12 live closed chains), `rejected` over `rejected` the rarer one (S047>S029) | keep the successor as it stands: rule `keep-successor` when it is `mined` (S570>S135, ledger `:78`), `keep-reject` when it is itself `rejected` (S047>S029, `:75`) — the ruling attaches to the row the validator checks, and `keep-reject` is refused unless that row reads `rejected` (`:211-212`); nothing flips | closed-chain-kept | S859 — tools/check-supersession-settlement.py:123; S047>S029 `keep-reject` reports/round-68/dispositions/dedup-ledger.tsv:75; kept-reject fingerprint S830 `:88` |
| settled-split | both rows `mined`, successor has `used-by`, and its teaches carries the limiter `for entry/line/row/cell/clause … only` (regex window 40 chars, `:54`) | narrow the scope: the supersession covers only the named slice; keep both rows and both scopes (ruling `keep-split`) | scope-limiter-missing | S859 — tools/check-supersession-settlement.py:129; S575>S420 `keep-split` reports/round-68/dispositions/dedup-ledger.tsv:83, live row corpus/SOURCES.md:553 |

Cautions that are part of the rule: branch order decides overlaps — the
closed test runs first, so a pair with **both** rows `rejected` reads
settled-closed, never settled-retired (`:123-131`; live pair S047>S029).
`same_url` is diagnostic only: `classify()` records it (`:136`) and no state
depends on it. An existing `used-by` path is not a reading `used-by`: the
scan checks path existence only (`:162-164`); whether the entry actually
contains the row id is review work — the docstring's `STALE-USED-BY` class
(`:21-22`) names a containment check no committed code path implements. A row
that does not split into exactly 11 cells never reaches `classify()`: a malformed
*successor* drops out of the chain list (`chains=0`, exit 0) and a malformed
*target* raises `KeyError: 'status'` (`:121`, exit 1 — the same exit code as
pending), so repair the row shape before reading any state (R69-M4). The five
error signatures are review-only labels: no committed code path detects them,
and each Evidence cell names the branch that *assigns* the state (`:123-132`),
not a detector.

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
| A label-only record passes silently | forbidden: label-only → off the sound channel **and** a hold, so the aggregate stays red (`22-label-representation.md:126-128`; live hold `D2L-FORM-UNRESOLVED`, `tools/d2-typed-labels.py:422,:810-814`; erratum 2026-10-19: retired anchor `TL-01`) |
| A translation claim made over a violating native form | cannot waive: native bytes govern, still FAIL (`22-label-representation.md:129-130`) |
| A sound kind declared with no bytes supplied | not clean: a `supplied` sound kind with no text is a `D2L-DATA` FAIL (exit 2, `tools/d2-typed-labels.py:694-695,:774-775`); carried `to-verify` with its owed slot, the `D2L-FORM-UNRESOLVED` hold stands (`:810-814`) (`22-label-representation.md:131-132`; erratum 2026-10-19: retired anchor `TL-01`) |
| An untyped legacy label | still checked; typing fields cannot exempt a string (`22-label-representation.md:133-134`) |
| A record with no declared kind at all | refused with a stable reason: `D2L-DATA` FAIL, exit 2 — the kind is never guessed from the text's language; it is assigned by declaration/component or refused (`tools/d2-typed-labels.py:768-769`; projection `:500,:549,:565`; erratum 2026-10-19: retired anchor `TL-02`) |
| `compare_only` set while the typed label is unresolved | misuse, not a pass — the unresolved hold stands (design spec R3) |
| A borrowed form judged only against the native stratum | misfile: loans pass through the recipient's phonotactic filter and carry donor provenance (`language-contact.md:78-79`) |
| A loan's oldest form used to date the referent's arrival | clock conflation; keep word-entry and object-arrival intervals separate (`loanword-material-dating.md:30-31,63`; executable B4) |
| A loanword that switched referent in transit | keep both coexisting names; date the sense–referent pairing (`corpus/knowledge/culture-material/garment-lexicon-crosslinguistic.md:28,30`) |
| Imported prestige terminology for locally made goods read as evidence of import | dictionary/selection bias; check local manufacture under imported labels (`loanword-material-dating.md:59,63`) |
| A modern/curatorial label promoted to an attested historical native word | reject or split: the label is typed as a label; the term keeps its own record (`costume-language-coupling-table.md:43`) |
| A translation, exonym, or official replacement run through the inherited-form sound laws | track separately: sound laws apply to the inherited spoken label, not its translation or replacement (`era-language-staging.md:127`) |
| Era tags or slot glosses graded on the name/sound channel | type them off the sound channel: costume labels project `translated-label` (`tools/d2-typed-labels.py:500`) and slot glosses ride as `gloss`/`representation`, never as a form (`:520,:529`), so neither enters the sound channel (retired anchor `FIELD_DEFAULTS`; the five-kind superset `fictional-coordinate`/`descriptive-gloss` remains proposed-only, `reports/round-11/depth/shard-gate-adapter.md:120-125`; selftest `no GAR label is graded on the sound channel`, `:3195`; erratum 2026-10-19) |
| A transliteration collision read as native-script identity | compare per declared scheme; a collision in that output channel is not native identity (`naming-collision-gate.md:72`) |
| A shared garment label across cultures read as identical cut or status | labels are neither cut nor status (`naming-collision-gate.md:54`) |
| chain-left-pending | an opened `supersedes` chain with no settled shape is correction debt: make the cell change first, then record the ruling in the disposition ledger (the validator refuses the reverse order, `tools/check-supersession-settlement.py:207-212`) — `--scan` exits 1 while any chain is pending (`:167`) |
| entry-not-repointed | the successor is `mined` but the entry still cites the deactivated target — repoint citations to the successor before the target's deactivation lands (classification branch `tools/check-supersession-settlement.py:127`; review-only signature, no committed detector) |
| retired-row-mined | a rejected correction still reads `mined` or is still cited — the audit refused it; the target keeps its status and citations (classification branch `tools/check-supersession-settlement.py:125`; review-only signature, no committed detector) |
| closed-chain-kept | the closed chain's successor was dropped or re-ruled — the target's `rejected` is the keep fingerprint; rule `keep-successor` for a `mined` successor and `keep-reject` for a `rejected` one (classification branch `tools/check-supersession-settlement.py:123`; review-only signature, no committed detector) |
| scope-limiter-missing | both rows are `mined` without the `for entry/line/row/cell/clause … only` limiter — the chain reads `pending`, not split; write the named slice into the successor's teaches (classification branch `tools/check-supersession-settlement.py:129`; review-only signature, no committed detector) |

| Status | Assign when (necessary condition) | Required basis | Never |
| `supported` | every element of the claim-as-worded is grounded by a named record in the packet's manifest or a named check with an observed result; nothing open narrows the wording | the resolving `grounding:` witness; residual limits are named even here — scoped-supported is "bounded and revisable, not certainty" (`corpus/knowledge/verification/to-verify-triage-protocol.md:18`) | upgrade a node's support onto its coupling edge (`to-verify-triage-protocol.md:97`); cite a shape-gate pass or digest match as the basis of a semantics claim (`reports/round-12/adjacency/contract.md:9-10,23`) |
| `partial` | the claim holds only under a stated restriction — scope limit, translation/mediation, projection-of-records, caveat-carrying source | `grounding:` + `restriction:` naming the exact bound, as BR05 did: "the Behistun cross-version leg … remain[s] unverified" (`reports/round-11/handoff/packet.md:108`) | widen the evidence instead of narrowing the wording (`to-verify-triage-protocol.md:70,76`); drop the `(to-verify)` from the downgraded remainder (`:182`) |
| `unresolved` | a named open question blocks the claim as worded: unperformed work, an external authority still pending, or contested alternatives that must coexist | `grounding:` + `open:` question + `owner:` lane — "a naked marker without a research question is not a usable queue item" (`to-verify-triage-protocol.md:32`) | let a deadline or failed search force closure (`:80`); present open as a fourth verdict — it is a queue state (`:80,181`); read absence as disproof ("silence is not proof of absence", `worldbible-integration-contract.md:179`) |
| A claim's status rides as prose inside `evidence_status` or `kind` | no per-claim uncertainty carrier — the round-12 reject (`reports/round-12/adjacency/contract.md:27`; v1 rows `reports/round-11/handoff/packet.md:82,88,95`); fill the dedicated `uncertainty` field, don't decorate another column |
| The packet passes `16/16 + 20/20` with no uncertainty column anywhere | shape-clean is not uncertainty-populated: the gate has zero uncertainty checks (`grep -ci uncertainty tools/gates/handoff-packet-check.py` → 0, 2026-10-17) and its fixture ledger has five columns, none of them uncertainty (`tools/gates/handoff-packet-check.py:651`) |
| Two claims share one basis sentence, or a basis restates the status word | boilerplate basis: basis is per-claim evidence whose witness resolves (`reports/round-15/claims.json:14`; `tools/harness/packet_uncertainty.py:205,209`; erratum 2026-10-19: contract `:183` carried the delivered-record checklist item) |
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
      synthesis/source-discipline-calibration.md:67; `provenance-audit
      corpus/knowledge`: `missing-calibration` checks declared shape only).
- [ ] Every costume/era claim couples to a term, a material, and a rule of
      who may wear it — prose gap (machinery: `costume-era-consistency-gate`).
- [ ] Every handoff to the world bible names the recipient (lore) and the
      open questions — `handoff-packet-check` enforces per packet; no canon here.

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
- `corpus/SOURCES.md` — where the lane learns: the opened, tier-scoped
  source registry with study paths, search log and unopened leads.

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
isolated repo export — a history-retaining copy (clone or worktree; the
round-3 restore-and-replay leg reads `291c714` from `.git`, which a plain tree
export lacks); byte equality after a run does not prove no writes.
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
| isolated legacy selftest battery | gate | `python3 tools/check-gate-battery.py` | duty 1 (selftests): 0 seven selftests pass / 1 recognized selftest failure / 2 could-not-evaluate; duty 2 (baselines): 0 every discovered pin verifies / 2 tampered, revised or uncovered gate — exit is the worse of the two; the committed default roots already include `reports/round-9/baselines/` (`tools/check-gate-battery.py:151`), so the default run exits 0 (measured 2026-10-18, round-24 audit: 7/7 selftests, 0 uncovered; supersedes the earlier "default exits 2 for myth and naming" wording once `--baselines-root` was folded into the defaults), and `--baselines-root` replaces the roots for one run (`tools/check-gate-battery.py:100`), so passing only `reports/round-9/baselines` now exits 2 with `BASELINE-GATE-UNCOVERED` for the frozen-root gates (`reports/round-9/baselines/registry.md` §5 item 6; `reports/round-10/drift/fix-21.md`; controls in `reports/round-24/audit-fixes.md`) | `--selftest` (isolated synthetic children) | fixed seven-gate list and control expectations in script | disposable copied scripts/fixtures; optional retained mirror only when requested | kotodama-shokunin |
| accept-c-53 | gate | `python3 -B reports/round-53/accept-c.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-c-54 | gate | `python3 -B reports/round-54/accept-c.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-c-55 | gate | `python3 -B reports/round-55/accept-c.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-o-55 | gate | `python3 -B reports/round-55/accept-o.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input, including a pinned | `python3 -B reports/round-55/accept-o.py --selftest` | — | read-only; selftest scratch | kotodama-shokunin |
| accept-c-56 | gate | `python3 -B reports/round-56/accept-c.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-o-56 | gate | `python3 -B reports/round-56/accept-o.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input, including a pinned | `python3 -B reports/round-56/accept-o.py --selftest` | — | read-only; selftest scratch | kotodama-shokunin |
| accept-c-57 | gate | `python3 -B reports/round-57/accept-c.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-o-57 | gate | `python3 -B reports/round-57/accept-o.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | `python3 -B reports/round-57/accept-o.py --selftest` | — | read-only; selftest scratch | kotodama-shokunin |
| accept-c-58 | gate | `python3 -B reports/round-58/accept-c.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-c-59 | gate | `python3 -B reports/round-59/accept-c.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-d-59 | gate | `python3 -B reports/round-59/accept-d.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-d-60 | gate | `python3 -B reports/round-60/accept-d.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-c-61 | gate | `python3 -B reports/round-61/accept-c.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-o-61 | gate | `python3 -B reports/round-61/accept-o.py --root .` | Exit 1 when k > 0, 0 when k = 0, 2 (with a diagnostic) on unusable input. | `python3 -B reports/round-61/accept-o.py --selftest` | — | read-only; selftest scratch | kotodama-shokunin |
| accept-d-62 | gate | `python3 -B reports/round-62/accept-d.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-o-62 | gate | `python3 -B reports/round-62/accept-o.py --root .` | Exit 0 when every row is REOPEN-verified, 1 findings, 2 on unusable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-c-63 | gate | `python3 -B reports/round-63/accept-c.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-o-63 | gate | `python3 -B reports/round-63/accept-o.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-c-64 | gate | `python3 -B reports/round-64/accept-c.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-ca-64 | gate | `python3 -B reports/round-64/accept-ca.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-o-64 | gate | `python3 -B reports/round-64/accept-o.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-c-65 | gate | `python3 -B reports/round-65/accept-c.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-ca-65 | gate | `python3 -B reports/round-65/accept-ca.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-o-65 | gate | `python3 -B reports/round-65/accept-o.py --root .` | Exit 0 only when every leg passes; 1 when any leg fails; 2 on unreadable input. | `python3 -B reports/round-65/accept-o.py --selftest` | — | read-only; selftest scratch | kotodama-shokunin |
| accept-c-66 | gate | `python3 -B reports/round-66/accept-c.py --root .` | Output ends `ACCEPT-C-66: PASS|FAIL`; exit 0/1, or 2 on unusable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-ca-66 | gate | `python3 -B reports/round-66/accept-ca.py --root .` | Output ends `ACCEPT-CA-66: PASS|FAIL`; exit 0/1, or 2 on unusable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-o-66 | gate | `python3 -B reports/round-66/accept-o.py --root .` | Output ends `ACCEPT-O-66: PASS|FAIL`; exit 0/1, or 2 on unusable input. | `python3 -B reports/round-66/accept-o.py --selftest` | — | read-only; selftest scratch | kotodama-shokunin |
| accept-c-67 | gate | `python3 -B reports/round-67/accept-c.py --root .` | Output ends `ACCEPT-C-67: PASS|FAIL`; exit 0/1, or 2 on unusable input. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-ca-67 | gate | `python3 -B reports/round-67/accept-ca.py --root .` | Output ends `ACCEPT-CA-67: PASS|FAIL`; exit 0/1, or 2 on unusable input. | `python3 -B reports/round-67/accept-ca.py --selftest` | — | read-only; selftest scratch | kotodama-shokunin |
| accept-o-67 | gate | `python3 -B reports/round-67/accept-o.py --root .` | Output ends `ACCEPT-O-67: PASS|FAIL`; exit 0/1, or 2 on unusable input. | `python3 -B reports/round-67/accept-o.py --selftest` | — | read-only; selftest scratch | kotodama-shokunin |
| accept-c-68 | gate | `python3 -B reports/round-68/accept-c.py --root .` | 0 pass / 1 fail / 2 usage-env. | — | — | read-only; selftest scratch | kotodama-shokunin |
| accept-ca-68 | gate | `python3 -B reports/round-68/accept-ca.py --root .` | 0 pass / 1 fail / 2 usage-env. | `python3 -B reports/round-68/accept-ca.py --selftest` | — | read-only; selftest scratch | kotodama-shokunin |
| accept-o-68 | gate | `python3 -B reports/round-68/accept-o.py --root .` | 0 pass / 1 fail / 2 usage-env. | `python3 -B reports/round-68/accept-o.py --selftest` | — | read-only; selftest scratch | kotodama-shokunin |
| accept-ca-69 | gate | `python3 -B reports/round-69/accept-ca.py --root .` | Exit codes: 0 pass · 1 fail · 2 usage/env. | `python3 -B reports/round-69/accept-ca.py --selftest` | — | read-only; selftest scratch | kotodama-shokunin |
| accept-d-69 | gate | `python3 -B reports/round-69/accept-d.py --root .` | Exit codes: 0 pass · 1 fail · 2 usage/env. | `python3 -B reports/round-69/accept-d.py --selftest` | — | read-only; selftest scratch | kotodama-shokunin |
| accept-o-69 | gate | `python3 -B reports/round-69/accept-o.py --root .` | Exit codes: 0 pass · 1 fail · 2 usage/env. | `python3 -B reports/round-69/accept-o.py --selftest` | — | read-only; selftest scratch | kotodama-shokunin |
| accept-c-71 | gate | `python3 -B reports/round-71/accept-c.py --root .` | Output ends `ACCEPT-C-71: PASS` or `: FAIL` (no legs= token); 0 pass / 1 fail / 2 input error. | — (no `--selftest`; passing it is an argparse error, exit 2) | entry path, partition/corpus counts 36 and 243, `>=12` cited ids pinned in script | read-only; no revision pin — grades whatever tree `--root` names | kotodama-shokunin |
| accept-ca-71 | gate | `python3 -B reports/round-71/accept-ca.py --root .` | Output ends `ACCEPT-CA-71: PASS` or `: FAIL` (no legs= token); 0 pass / 1 fail / 2 input error. | — (no `--selftest`; argparse error, exit 2) | 21-id quarantine slice, verdict set {PRESENT, REFUSED, UNVERIFIABLE}, unreachable ids S807/S812/S835, six round-70 receipt paths pinned in script | read-only; no revision pin — grades whatever tree `--root` names | kotodama-shokunin |
| accept-d-71 | gate | `python3 -B reports/round-71/accept-d.py --root .` | Delegates to the frozen round-69 counter, so output ends `ACCEPT-D-69: PASS` or `: FAIL legs=8/8` — a grep for `ACCEPT-D-71` finds nothing; 0/1 from the frozen counter, 2 on usage/env. | `python3 -B reports/round-71/accept-d.py --selftest` (prints the frozen `GREEN FIXTURE`, `DO-NOTHING FIXTURE`, `SELFTEST: n/2`) | frozen counter path `reports/round-69/accept-d.py` and the no-git marker string pinned in script | read-only; selftest scratch in `tempfile.TemporaryDirectory`; a tree without `.git` prints `SELFTEST: COULD-NOT-EVALUATE (no git)` and exits 2 | kotodama-shokunin |
| accept-c-72 | gate | `python3 -B reports/round-72/accept-c.py --root . --lands <40-hex>` | Output ends `ACCEPT-C-72: PASS` or `: FAIL legs=10/10` — the denominator is a literal, so a FAIL receipt still reads `legs=10/10`; 0 pass / 1 fail; 2 on missing or non-40-hex `--lands`, or when `--root` has no `.git`. | `python3 -B reports/round-72/accept-c.py --selftest` — measured `SELFTEST: 10/11`, exit 1 at HEAD (see §5) | base `b60c7b14…`, ids S874/S875, both entry paths, scratch-mirror receipt path, ten mutants pinned in script | read-only against `--lands` via `git show`; selftest builds `tempfile.mkdtemp` fixtures and leaves them behind | kotodama-shokunin |
| accept-ca-72 | gate | `python3 -B reports/round-72/accept-ca.py --root . --lands <40-hex> --fleet-root /home/vgpnk/Projects/shokunin` | Output ends `ACCEPT-CA-72: PASS` or `: FAIL legs=12/12` — literal denominator; 0 pass / 1 fail; 2 on missing or malformed `--lands`; a well-formed but absent revision grades as leg FAILs with exit 1. | — (no `--selftest`; argparse error, exit 2) | base `b60c7b14…`, fleet root, five known round-71 report commits, seven w2 file paths, CASTAMP path, authorized path prefixes pinned in script | read-only (`git show` plus absolute reads of the fleet report); corpus materialized only into temp dirs | kotodama-shokunin |
| accept-c-73 | gate | `python3 -B reports/round-73/accept-c.py --root . --lands <40-hex>` | Output ends `ACCEPT-C-73: PASS` or `: FAIL legs=11/11`; 0 pass / 1 fail; 2 on a missing or malformed `--lands`. | `python3 -B reports/round-73/accept-c.py --selftest` (prints `SELFTEST: 29/29`) | base `8841ad3b…`, the five adopted registry rows (set in claims.json), both entry paths, evidence dir, the refused staged ids and campaign ids pinned in the script and in claims.json | read-only against `--lands` (materialized `git archive`); selftest builds `tempfile.mkdtemp` fixtures | kotodama-shokunin |
| accept-ca-73 | gate | `python3 -B reports/round-73/accept-ca.py --root . --lands <40-hex> --fleet-root /home/vgpnk/Projects/shokunin` | Output ends `ACCEPT-CA-73: PASS` or `: FAIL legs=<n>/9`; 0 pass / 1 fail; 2 on input error. | `python3 -B reports/round-73/accept-ca.py --selftest` (prints `SELFTEST OK: 10 scenarios`) | base `8841ad3b…`, ledger `reports/round-73/ledger.json` (8 pairs, must_track list), fleet pin `80d8c9b5…`, observe allowlist | read-only (materialized clones; observe_cmd argv only); selftest builds `tempfile` repositories | kotodama-shokunin |

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

### D3 replay checklist (executable where a tool exists)

1. Run assembler `--check` and its isolated `--selftest`; drift or malformed
   components are not a passed culture task.
2. Run the positive guard, independent control selftest and frozen command.
   Snapshot mode verifies every listed input digest before the verdict;
   boolean exit labels and unsafe manifest paths are rejected. The committed
   manifest is deliberately comprehensive; the generic reader requires only
   packet coverage and does not infer artifact roles for the caller.
3. Run legacy naming and costume checks on
   `examples/culture-d3/packet.gates.yml`. Keep naming's CROSS-HOLD (and E0/E1
   similarity review) and C03's costume R-01 finding; neither is a green
   clearance gate. Verify the native coda adapter, not merely a permissive
   synthetic fixture.
4. Compare the handoff's glossary, names, source bridges and digest rows
   against actual packet bytes (`examples/culture-d3/handoff.md` against
   `examples/culture-d3/packet.gates.yml`), then run its structural envelope
   check. Sixteen fields and twenty glossary rows alone cannot prove content
   agrees.
5. Run `python3 reports/round-7/run-validation.py` for the original F/O
   thresholds, input preservation and old-surface regressions. It writes its
   own receipt, not historical receipts. Fresh source access and invented
   model consistency are causally separate checks. **Expected verdicts at HEAD
   (dated 2026-10-19; each exits 1 by design — a regression is a different
   output, not this), and run them in a disposable clone: round 5 and round 7
   rewrite their own filed `validation.json` in place (round 6 is byte-stable).**
   round-5 `run-validation.py` → `acceptance_checks_passed: false` with F =
   non-append corpus edit (`supplement-opencode-1/sources/ottoman.json`, OTT-06)
   and O = seven `gate_digest_mismatch` could-not-evaluate rows replaying
   `tools/gates/frozen/round-3/MANIFEST.tsv` against gates repaired after round 3;
   round-6 `run-validation.py` → `historical file changed: .gitignore` vs its
   BASE; round-7 `run-validation.py` → preservation (`.gitignore`), historical
   knowledge-inventory totals, one claim-F rejection, and the round-6 predecessor
   check, while its O leg passes (5/5, 16/16, 4/4, frozen 5/5).

The frozen reader ignores extra metadata keys, compares finding IDs as a set
and allows symlinks whose resolved target remains inside the repo. These are
limits of this bounded interface, not a claim of universal schema/security
validation. Legacy parsers and D2's twenty expected findings remain unchanged.
Read `reports/round-7/integration-attempts.json` for corrected failures and
`native-request-binding.json` for the actual prompt's non-verbatim step-6
defect; passing example checks do not erase protocol-conformance debt.
- [ ] Every availability/dispatch record filed `open-at-seat-close` whose round's
      validation.json has landed carries a closing snapshot in that round's telemetry/ whose
      `closes` names that record and whose `closes_sha256` matches the record's live bytes
      (audit: `python3 -c "import glob,hashlib,json,os; [print(f) for f in sorted(glob.glob('reports/round-*/availability*.json')) if json.load(open(f)).get('state')=='open-at-seat-close' and os.path.exists(os.path.join('reports',f.split('/')[1],'validation.json')) and not any((lambda d: isinstance(d,dict) and d.get('closes')==f and d.get('closes_sha256')==hashlib.sha256(open(f,'rb').read()).hexdigest())(json.load(open(s))) for s in glob.glob(os.path.join('reports',f.split('/')[1],'telemetry','availability-close-*.json')))]"` — must print nothing once the round's records are closed)
