# D4 myth-symbol system and era model — pre-implementation design (R17-D03)

- **Seat:** R17-D03 (myth designer), round 17, loop 2 build 1 of 4.
- **Component scope this doc designs:** `07-oaths-sayings`, `08-symbols-tokens`,
  `09-eras-calendar` of the twelve-component D4 tree (`design-brief.md` §5).
- **Culture:** D4 — the weigh-court quote register (trader argot); seed and
  spine adopted from `reports/round-17/d4/design-brief.md` §2–§3 (§1 below).
- **Canon status:** **NON-CANON.** Every saying, oath, mark, era name, and
  coordinate below is invented design for a fictional culture. Nothing here is
  canon, nothing is a lore decision (lore-shokunin owns canon), and nothing
  here is a real-world rights, attribution, or clearance ruling — such
  questions are *reported* (§13), never absorbed.
- **Status:** pre-implementation design record, 2026-10-18; revision r2
  (reconciliation to the brief; see §14). Supersede-by-new-file only for any
  frozen version.
- **Write scope:** this file only. No component, packet, tool, or filed round
  8–16 artifact was edited by this seat.

## 0. What this doc fixes, what it does not, and authority order

**Authority order (binding for this file):** `design-brief.md` (R17-D01) is
authoritative for the culture, the spine, the component registry, the artifact
contract, and the union hold-set proposal (§7.1). `typed-support-1.md` /
`typed-support-2.md` own the typed-derivation contract and the hold-set
freeze. This doc owns the internals of components 07, 08, 09 and the
myth/era channel's named contribution to the hold set. Where this doc and the
brief differ, the brief wins and this doc is superseded by a new file.

It fixes: the myth/era-channel read of the seed (§1); the register cosmology
(§4); the oaths/sayings system and role ledger (§5–§6); the symbol/token
system (§7); the era model incl. the register-emergence clocks (§8); the
typed-label interface for my records (§9); **the myth/era contribution to the
pre-implementation hold set (§10)**; coupling edges (§11); acceptance checks
(§12).

It does **not** write: phonology, morphosyntax, lexicon, ledger script
(language seats); the register contract and its doublets (06 seat);
materials/measures, costumes, ranks/names (their seats); the brief; any
component file, packet, tool, or expected-holds file; any canon decision.

**Pre-implementation proof.** This doc's r1 was written when no D4 design doc
had landed (`ls reports/round-17/d4/` → empty, 2026-10-18T09:16Z;
`ls examples/culture-d4/` → exit 2, same timestamp). While r1 was in flight
the sibling design docs landed (09:26–09:28Z); r2 reconciles to them (§14).
The hold-set block (§10) remains a pre-implementation record: no D4 packet,
component, projection, or expected-holds file exists at write time
(`ls examples/culture-d4/` → exit 2, re-checked 2026-10-18T09:28Z).

## 1. Seed adopted (from the brief), and my channel's obligations

Adopted verbatim in substance from `design-brief.md` §2–§3, §4.2, §5:

- **One line (brief §2):** a settled grain-and-orchard plain culture whose
  towns run **weigh-courts**; brokers there bind prices in a taught **quote
  register** (the argot) and keep the record in a **notched-rod ledger**.
- **Spine (brief §3):** **SP-01 COUNT** (quantity as the public fact: standard
  measures, weight classes, tolls, classifier morphology, the rod ledger,
  numerals) × **SP-02 QUOTE** (binding speech as the private fact: a quote is
  witnessed, rod-marked, and enforceable by court record); **SP-03 test**:
  every record carries `axis: count | quote | both | neutral-with-rationale`.
- **Stage-0 rows (brief §2):** dry inland plain with orchard belts (no
  river/bank/tide/flood setting, no highland transhumance); grain and orchard
  produce plus the weigh-service; court ranks with rod-rights; **religion/oath
  law: no pantheon component — the binding force is the witnessed quote and
  the rod-mark, attributed sayings kept attributed, oath formulas
  plain-register-only**; two partner stages (western grain towns = the E1
  script donor; southern broker network = the chained loan carrier);
  E0 notched rods only, ledger script at the E0/E1 seam, spellings freeze at
  E2; **four strata E0–E3, E3 = the register split**.
- **No-import list (brief §4.2, NB-01..NB-08):** my components are scanned for
  NB-01 (river/tide setting or metaphor), NB-02 (**any knot/cord geometry** —
  D4's geometry is the notch, never the knot), NB-05 (D1 sound law, D2 pitch
  accent), NB-06 (D1/D2 fixture forms and names), NB-07 (D2 spine vocabulary),
  NB-08 (D3 material: hall/temple pledge, avoidance register, closed source
  bindings, any real-source URL). Violations are findings, not quietly fixed.
- **My three components (brief §5):**
  - `07-oaths-sayings.yml` → packet keys `sayings`, `oaths`: attributed
    sayings (kept attributed), oath formulas (plain-only speech acts), no
    pantheon, no narrator-certified truth.
  - `08-symbols-tokens.yml` → packet key `symbols`: court marks, rod notches
    as symbol geometry, stamp shapes; audience-scoped symbols
    (court-internal vs public).
  - `09-eras-calendar.yml` → packet keys `eras`, `era_records`: E0–E3, the E3
    register split as a dated event, per-form register-emergence clocks (brief
    §6 Δ5), no CE dates synthesized.
- **Packet-shape mapping (brief §5):** the packet's `motifs` key carries my
  sayings; `roles` carries the role ledger of §5; `symbols` carries §7;
  `eras`/`era_records` carry §8. `pantheon` is the marker `NOT-APPLICABLE`
  with a `pantheon_note` (the myth gate's own allowance for non-pantheonic
  systems, `myth-consistency-gate.md` §3).

## 2. Follows (corpus decision tables this doc is built on)

Paths repo-relative; section numbers are the ones actually used.

- `corpus/knowledge/verification/myth-consistency-gate.md` §2 (minimum review
  packet: role, narrative, index, symbol, evidence ledgers), §3 (bipartite
  role–agent map; the five status marks; `NOT-APPLICABLE` for non-pantheonic
  systems; MC-P00/P01/P02), §4 (motif ledger: local id, law with
  trigger/effect, variant records; MC-M00/M01/M02), §5 (era alignment: five
  clocks; MC-E01..E03), §6 (symbol keys form+medium+era+register+audience;
  MC-S00/S01/S02).
- `corpus/knowledge/myth-symbol/ritual-liminality.md` §5 (calendrical rites;
  inversion licence and aftermath), §6 (ritual grammar → narrative grammar:
  performative speech and felicity conditions).
- `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md` §3 steps 0–8
  (material substrate first; polarity axes; partition n from real enumeration;
  registers over the same n slots; UNALIGNED cells kept), §5 (one primary
  domain per sign; satellites licensed), §6 (drift laws M1–M6; date-stamp
  every meaning; no retro-projection; fossils), §7 (symbol audit).
- `corpus/knowledge/synthesis/symbolism-consistency-rules.md` §3 (define the
  lookup key before assigning a meaning), §4 (invariants), §5 (licensed
  transformations), §7–§8 (era drift; no evolutionary ladder), §10 (audit).
- `corpus/knowledge/synthesis/era-language-staging.md` §4 (stage packets, not
  filters), §5 (register stratification inside an era — the row grammar this
  design's register clocks follow), §7 (type every period label; era-name
  formation recipe; date-formula recipe), §8 (synchronize without
  determinism).
- `corpus/knowledge/synthesis/era-myth-language-costume-matrix.md` §1 (an era
  is an address, not an explanation; emic vs etic), §3 (cell grammar
  `state; users/place; authority; carrier; exception; evidence/status`; A/R/
  F/U labels), §8 (coupling ledger: explain links without synchronizing
  everything).
- `corpus/knowledge/culture-material/era-periodization-models.md` §1
  (periodization is a legitimacy technology), §3 (era-name craft), §4 (seam
  logistics: reveal object, broken artifact), §5 (calendar as loyalty; rival
  counts), §13 (build order for a fictional culture), §14 (canon boundary).
- `corpus/knowledge/culture-material/calendar-festival-systems.md` §1 (three
  clocks and the lie), §8 (new-year placement; era as statute), §11
  (application protocol).
- `corpus/knowledge/synthesis/cultural-translation-protocol.md` §(the
  form/sense/object/register histories kept separate — the brief §6 Δ5 cites
  it at `:111`).
- `corpus/knowledge/verification/calibration-registry.md` §10 (era staging:
  replace ladders with separate clocks), §11 (coupling audit).
- `corpus/knowledge/verification/real-world-inspiration-boundaries.md` §3
  (name the relationship before borrowing), §5 (transformation checklist).
- `examples/culture-d2/` — the working precedent: `ASSEMBLY.md`,
  `expected-holds.json` (hold-set schema), `typed-labels.d2.yml` (projection
  shape), `components/08-symbols.yml`, `09-eras-calendar.yml`,
  `11-costumes.yml` `era_reconciliation` (the era-alias row pattern).

Comparator discipline: every comparator above is an in-repo corpus entry with
its own provenance cautions; no outside scholarship is asserted; no real
culture is described, renamed, or approximated.

## 3. Spine read for the myth/era channel

| Axis | Definition (D4) | Required evidence in components 07/08/09 |
|---|---|---|
| **COUNT** | quantity as the public fact: the rod, the notch, the sealed weight, the toll, the classifier | rod-notch geometry as symbol geometry (08); era records dated by rod-notch groups (09); sayings whose law is a count rule (07) |
| **QUOTE** | binding speech as the private fact: the taught register, the witnessed quote, the rod-mark | oath formulas as plain-only speech acts (07); the quote register's emergence clock (09, RG-02); audience-scoped court marks that mark *who may quote* (08) |
| **both** | the rod: the object that carries the count and receives the quote's mark | the rod as the one carrier in both axes; the stamp as the mark that makes a quote a record |

Aesthetic stance (brief §3 AS-01..AS-05, read into my channel): **the price is
spoken once** (a saying's law, not a proverb); **the record is a rod, not a
memory** (no witness formula, no oath-cloth, no public witnessing
institution); **plain is what is recorded, quote is what is bound** (the
inversion: the plain register is the record/ritual register, the argot is the
legal register); **measures are the town's face** (the court's standard
weights are public monuments); **guests quote, hosts record** (the asymmetry
that generates the rank rules).

## 4. Register cosmology (a culture with no pantheon)

There is no pantheon and no cosmic-origin account in D4 by design (brief §2).
What functions as the mythic substrate is the **court's world-model**, and it
is kept as *attributed, dated, institution-bound* material, never as
narrator-certified truth (the D3 `D3-MYTH` discipline re-exercised, brief §5
row 07):

- **COS-01 — the world is a counted plain.** The plain is what the courts can
  weigh; what cannot be weighed is not part of the account. The emic model
  has no upper/lower worlds, no axis mundi, no directions by compass: direction
  deixis is **toward the court / away from the court / the goods side / the
  ledger side** (brief §2: "direction deixis is toward the weigh-court").
- **COS-02 — the rod is the one carrier.** The notched rod carries the count;
  the stamp marks the quote. The rod is the culture's world-axis substitute
  (cosmology §2's "axis needs a built expression and a ritual that uses it"):
  its built expression is the court's standard rod; its ritual use is the
  **rod-marking** of a witnessed quote (RIT-01, §5).
- **COS-03 — the weights are monuments.** The court's sealed weights are the
  town's public face (AS-04); a town is judged by its weights. No weights, no
  court, no record.
- **COS-04 — the refusal of origins.** "Where the plain came from" is
  **EXPLICITLY-UNEXPLAINED** (a role-ledger status, §5): the plain register
  refuses the question, and the refusal is recorded as a design blank with
  its reason — never filled by an invented cosmogony. (This is the
  non-pantheonic counterpart of the myth gate §3 "legitimate non-slot
  answer".)
- **COS-05 — the register inversion is doctrine.** Plain is the record and
  ritual register; quote is the legal register of binding speech (AS-03).
  The doctrine is attributed to the court charters (dated at E3, §8), not to
  a narrator.

## 5. Oaths, sayings, and the role ledger (component 07)

### 5.1 Oath formulas (plain-only speech acts)

- **OAT-01 — the binding oath** (the oath that makes a quote a record): a
  plain-register formula; felicity conditions: (a) spoken in the plain
  register, (b) before a rod-holder, (c) followed by the rod-mark; failure of
  any condition voids the act. An oath in the quote register is **void by
  law** (brief §6 Δ6: "a plain oath is binding; an oath in the quote register
  is void").
- **OAT-02 — the guest oath** (guest-law): a foreign broker may quote and be
  rod-marked, but the oath's recording is the host court's act; a guest's oath
  binds only with a rod-mark (brief §6 Δ6: "a guest's quote binds only with a
  rod-mark").
- **OAT-03 — the refusal formula**: the plain-register formula that ends a
  negotiation without a record; it leaves no rod-mark and no obligation.
- Each formula is a record: `{id, register: plain, felicity_conditions,
  rod_mark: required|none, authority, era_ids, evidence}`. Formulas are
  **speech acts, not spells**: their force is institutional, stated as such,
  and no supernatural sanction is claimed anywhere (calibration: the
  binding force is the court, not a power).

### 5.2 Attributed sayings (no narrator-certified truth)

Sayings are the culture's mythic material — kept **attributed**: every saying
names its speaker or institution, its register, its occasion, and its date
(era tag or rod-notch group). A saying with no attribution is not admitted;
the packet's `sayings` block never asserts a narrator's truth.

- **SAY-01 — "the price is spoken once"** (AS-01): law = *when* a price is
  quoted in the register, *then* it is not repeated; re-quoting is a new act
  with a new rod-mark. Attributed to the court charters (E3); a rival
  attribution to the southern broker network is kept as a variant.
- **SAY-02 — "the record is a rod"** (AS-02): law = *when* an obligation is
  contested, *then* the rod decides, not a memory. Attributed: court-masters'
  assembly.
- **SAY-03 — "plain is what is recorded"** (AS-03): law = *when* a speech act
  must bind, *then* it is spoken plain; *when* it must be remembered, *then*
  it is written. Attributed: the first ledger-keeper (E1).
- **SAY-04 — "measures are the town's face"** (AS-04): law = *when* a court's
  weights are found light, *then* its records are read again. Attributed: the
  western towns' envoy (a *foreign* attribution kept as such).
- **SAY-05 — "guests quote, hosts record"** (AS-05): law = *when* a guest
  quotes, *then* the host's court keeps the rod. Attributed: the guest-law
  charter.

### 5.3 Role ledger (ROLE-01..ROLE-10) — institutional coverage, no gods

The myth gate's role ledger applies to non-pantheonic systems with
`NON-DIVINE` and `EXPLICITLY-UNEXPLAINED` statuses; agents here are
institutions and objects (myth gate §3, statuses as given).

| id | dependency | status | agent / mechanism | basis (record ids) |
|---|---|---|---|---|
| ROLE-01 | subsistence (grain, orchard, weigh-service) | NON-DIVINE | the courts' sealed measures; no provider claimed | COS-03, SM-* (10's records) |
| ROLE-02 | authority and oath | NON-DIVINE | the court; OAT-01's formula + the rod-mark (exclusive for binding quotes) | OAT-01, RIT-01 |
| ROLE-03 | conflict settlement | NON-DIVINE | the court's re-reading of the rod (SAY-02) | SAY-02 |
| ROLE-04 | mortality, inheritance | NON-DIVINE | the court's inheritance records (rod transfers); no death agent | ROLE-10, SAY-02 |
| ROLE-05 | reproduction, household continuity | EXPLICITLY-UNEXPLAINED | the packet records no household-continuity mechanism; the register's domain is trade | reason recorded, never filled |
| ROLE-06 | craft and goods knowledge | NON-DIVINE | the apprentice-to-master ladder (rod-rights) | rank ids (12's records) |
| ROLE-07 | exchange and travel | NON-DIVINE | the guest-law asymmetry (SAY-05) and the two partner stages | SAY-05, OAT-02 |
| ROLE-08 | cosmic origins and boundaries | EXPLICITLY-UNEXPLAINED | COS-04: the plain register refuses the question | COS-04 |
| ROLE-09 | weather and season (orchard timing) | EXPLICITLY-UNEXPLAINED | no weather agent; the calendar records the seasons without a provider | ER-* records (§8) |
| ROLE-10 | the dead | EXPLICITLY-UNEXPLAINED | no destination doctrine; the rod transfer is the only trace | ROLE-04 |

No row is `ASSIGNED` (there are no gods), no row is `UNKNOWN` without a
reason, and the four `EXPLICITLY-UNEXPLAINED` rows each carry their reason
inline — the blanks are doctrine (COS-04) and scope (ROLE-05), not omissions.

### 5.4 The gate-facing blocks

- `pantheon: NOT-APPLICABLE` with `pantheon_note` naming the brief's
  religion/oath-law row and COS-04 (myth gate §3's non-pantheonic allowance).
- `oaths`: OAT-01..OAT-03. `sayings`: SAY-01..SAY-05. `roles`: ROLE-01..ROLE-10.
- The packet's `motifs` key carries the sayings, each with its law
  `{rule, when, then}` and variants (§6) so MC-M00/M01/M02 cannot fire.

## 6. Saying ledger — laws and variants (the packet's `motifs` block)

Each saying record carries: `id`, `tier`, `title`, `code` (a local handle, not
an index code), `index_checked: none`, `law {rule, when, then}`, `variants[]`
with `{id, teller, register, asserts_law, exception, events[]}`.

| id | law (rule / when / then) | variants |
|---|---|---|
| SAY-01 | a quote is spoken once / when a price is quoted in the register / then it is not repeated; re-quoting is a new act with a new rod-mark | V1 court charters (E3, plain, asserts law); V2 southern brokers' version (quote register; asserts law; **exception recorded**: the fair's re-quote licence, dated E1) |
| SAY-02 | the rod decides / when an obligation is contested / then the court reads the rod, not a memory | V1 court-masters (E1); V2 the guests' version (host court's rod only; asserts law; exception: none) |
| SAY-03 | plain binds, written remembers / when a speech act must bind, it is plain; when it must be remembered, it is written | V1 first ledger-keeper (E1); V2 the abbreviation convention's users (E1+, a *reduction*, marked as a later teller) |
| SAY-04 | a light weight is a re-read / when a court's weights are found light / then its records are read again | V1 western envoy (foreign attribution); V2 the local counter-saying (asserts the weights' immunity, exception: the found-light case itself — the contradiction is recorded as an exception, never smoothed) |
| SAY-05 | guests quote, hosts record / when a guest quotes / then the host's court keeps the rod | V1 guest-law charter (E1); V2 the southern network's variant (a *claimed* guest court; asserts law; exception: the charter's named refusal) |

**Index concordance policy:** D4 makes **no ATU/motif-index claims**; every
saying carries `index_checked: none` and a note. A `cf.` comparison may be
added later only with a checked entry, edition, and witness (myth gate §4,
MC-M02). This is a deliberate refusal, not an oversight — the drill has no
checked index witnesses in-repo.

**Teller classes / registers:** the plain register (record and ritual
tellings: charters, court-masters, the ledger-keeper) and the quote register
(the brokers' tellings, which are *legal speech*, not literature). A saying
told in the wrong register is a register violation, not a variant (brief §3
AS-03).

## 7. Symbols and tokens (component 08)

**Material substrate first (method §3 step 0):** available media are the rod
(scored wood, notch geometry), the stamp (cut stone or cast metal, court
seals), the sealed weights (stone/brass faces), the ledger (script on cloth
or leaf from E1), cloth bands (trade-sash, imported plain cloth), and the
court's floor. No dyes are needed for the marks themselves; colour enters
only through costume (11's records).

- **Partition (n = 4, from real enumeration):** the four court ranks
  (apprentice → rod-holder → broker → court-master; brief §2). Recurrence:
  four ranks, four notch-classes on the rod, four columns of the ledger
  (goods / measures / ranks / sayings anchors — brief §5 row 05). The
  partition is the culture's own ladder, not an aesthetic (method §3 step 2).
- **Polarity axes:** AX-1 public / court-internal (the audience axis; the
  brief's own scoping); AX-2 counted / quoted (the notch vs the stamp: the
  count is public, the quote's mark is kept); AX-3 bound / unbound (a mark
  with a rod vs a mark that leaves nothing).
- **Registers over the same four slots:** mark geometry (notch classes),
  stamp shape, cloth band, licence (who may mark). The **mark geometry** is
  the notch — **never the knot** (NB-02): no cord, no loop, no tie occurs in
  any symbol record.
- **Registered signs (SYM-01..SYM-08).** Each carries the gate's full key —
  **form, medium, era, register, audience** — plus one primary domain,
  satellites capped at 3 with a licensed transformation each, poles, and a
  change history (drift law 1). Emic names are term requests (§9).

| id | sign (gloss) | register | medium | era | register/occasion | audience |
|---|---|---|---|---|---|---|
| SYM-01 | the single notch | mark geometry | rod, scored | E0–E3 | a recorded act | the court (rod-holders and above) |
| SYM-02 | the group of four | mark geometry | rod, scored | E0–E3 | a settled account | the court |
| SYM-03 | the court stamp | stamp shape | cut stone / cast metal seal | E0–E3 | sealing a weight, marking a quote | court-internal (stamp-holders) |
| SYM-04 | the guest's half-stamp | stamp shape | a stamp cut in halves; the host keeps one | E1–E3 | the guest-law record | host court and guest broker |
| SYM-05 | the plain band | cloth band | undyed local cloth | E0–E3 | the record occasion | public (worn where visible) |
| SYM-06 | the sash | cloth band | imported plain cloth | E1–E3 | fair and assembly | public |
| SYM-07 | the light-weight mark | stamp shape | a chiselled face-mark on the weight | E2–E3 | the re-read of a court's weights | public (the monument's face) |
| SYM-08 | the frozen spelling | written form | ledger script on cloth/leaf | E2–E3 | the written record | court-internal (ledger-keepers) |

**Alignment matrix** (rows = the four rank slots; columns = the other three
registers; one UNALIGNED cell kept with its reason and its consequence,
method §3 step 4):

| rank slot | mark geometry | stamp shape | cloth band |
|---|---|---|---|
| apprentice | single notch (may count, may not mark) | **UNALIGNED** — "the stamp is not earned by the unmarked hand"; no stamp exists for this slot | plain band only |
| rod-holder | group of four | the court stamp (held, not cut) | plain band |
| broker | group of four + the broker's extra score | the broker's stamp | sash (E1+) |
| court-master | the full rod | the master's stamp (the court's own) | sash, and the master's band |

Two consequences are declared, not decorative: the apprentice's missing stamp
is the rank ladder's own signal (a promotion is a stamp, so the ladder is
legible in the tokens), and the plain band's public wear vs the sash's fair
wear is the audience scope made visible (AX-1).

**Drift table (era-versioned meanings; drift laws 1–4):**

| sign | E0 | E1 | E2–E3 | mechanism | fossil kept |
|---|---|---|---|---|---|
| SYM-03 court stamp | the weight's seal only | the quote's mark (the rod gets stamped) | the record's authority (the stamp outranks the notch) | M2 institutional overwrite | old weight-faces still carry only the seal; the double meaning survives in the formula "the stone's word" |
| SYM-06 sash | — (absent) | the fair-goer's cloth (foreignness marked) | the assembly's own cloth (foreignness forgotten) | M5 contact → M2 | the plain band is still required *under* the sash at court (the fossil is structural) |
| SYM-08 frozen spelling | — | — | the ledger's authority (E2 freeze) | M3 media standardization | rod-notch groups survive beside the ledger (the rod is never retired) |
| SYM-07 light-weight mark | — | — | the re-read's mark | M6 event-index (a datable found-light case at E2) | the chisel mark is kept on repaired weights |

No retro-projection: every later meaning is dated at its seam and no present
meaning explains an earlier row (drift law 2).

## 8. Era model (component 09)

### 8.1 Tag space and named eras

`eras: [E0, E1, E2, E3]` (contract tags). `era_records: ER-01..ER-05`, each
with `name` (emic gloss), `tag`, `seam`, `language_stage`, `record_stage`,
`register_state`, `axis`, `evidence`.

| id | name (emic gloss) | tag | seam | record stage | register state |
|---|---|---|---|---|---|
| ER-01 | First Weights | E0 | the first sealed weights; the courts are founded | notched rods only | plain only |
| ER-02 | The Rod Years | E0 | the rod ledger spreads; the rank ladder fixes | notched rods | plain only |
| ER-03 | The Written Ledger | E1 | the ledger script arrives (donor stage `west-stage-1`; sign values from 02's phonology; no alphabet-first premise, NB-04) | rods + ledger | plain + the ledger's written convention |
| ER-04 | The Frozen Hand | E2 | spellings freeze | rods + ledger (frozen spellings) | plain + written convention |
| ER-05 | The Taught Quote | E3 | **the register split**: the quote register becomes a taught, distinct register; the plain doublets start being owed | rods + ledger | plain + quote (taught) |

### 8.2 Register-emergence clocks (RG-01..RG-04) — the brief's Δ5

Per-form register histories are kept separate from form, sense, and object
histories (brief §6 Δ5; `cultural-translation-protocol.md:111`). The era
component carries the emergence clocks:

| id | clock | declared value | adapter state |
|---|---|---|---|
| RG-01 | the plain register | `available_from: E0` (tag) | confirmed |
| RG-02 | the quote register | **declared as a prose span** — "around the time the third court raised its weights, before the frozen hand" — with no tag | **`adapt_status: partial`, raw string retained in `unresolved[]`; emits the `D4L-ERA` hold (§10)** |
| RG-03 | the ledger's written convention | `available_from: E1` (tag) | confirmed |
| RG-04 | the abbreviation convention | `available_from: E1` (tag; a convention, not a third register — brief §5 row 04) | confirmed |

- Every quote form carries `available_from: E3` (brief §6 Δ5); a quote form
  claimed in a pre-E3 slot is a **`D4L-ERA` FAIL**, so the design dates every
  quote form at E3 and no earlier. Exactly one row (RG-02) is a prose span by
  design — the hold, not an accident.
- RG-02's raw span is kept verbatim in `unresolved[]`; the adapter never
  promotes it to a tag (the E5/A2 discipline: a partial is never a pass).
- No CE date is synthesized anywhere (brief §6 Δ5, E7): the era component
  emits no numeric `era_dates`.

### 8.3 Date formula, coordinates, and rival counts

- Count unit: the **court year** (from a court's weight-sealing); dates on
  rods are notch groups, written dates (E1+) are ledger entries.
- No year zero; a succession does not reset the count (the count is the
  court's, not a person's); the ledger keeps the western towns' own era names
  in a second column and never converts them (era-periodization §5, rival
  counts).
- `source_era_dates`: in-world coordinates (rod-notch groups) keyed by named
  era; the numeric gate key `era_dates` is **omitted** because no defensible
  conversion exists — the D2 precedent and its reason restated
  (`examples/culture-d2/ASSEMBLY.md`, "Parse/assembly fix and verification":
  strings such as D1 would be the wrong type; inventing a CE chronology was
  refused). The D4 assembler must reproduce the omission.
- Era-name formation recipe: authority = the court-masters' assembly at a
  weight-sealing; permitted morphology = two-base compounds (a measure or
  ledger base + a hand/court base); semantic pool = weights, rods, hands,
  ledgers — **never a person's name**; reuse taboo: a name may not be reused
  while a rod bearing it is still kept; announcement medium = the weight's
  face (E0+) and the ledger's first line (E1+).

### 8.4 Seams, rites, calendar

- **Seam records (SEAM-01..SEAM-03):** the E0/E1 script seam (the ledger
  arrives; the rod is not retired), the E1/E2 freeze seam (the spelling
  freeze), the E2/E3 register split (the taught quote; the owed doublets).
  Each seam names its reveal object (the new ledger / the frozen page / the
  taught slot) and its kept artifact (the rod; the old spelling; the plain
  doublet list) — era-periodization §4's seam pattern, transformed.
- **Rites (RIT-01..RIT-02):** RIT-01 the rod-marking (COS-02's built
  expression + ritual use; register: plain; office: rod-holder; failure
  condition: no mark, no record); RIT-02 the weight-sealing (COS-03; the
  court's public act; failure: a light weight re-reads the records, SAY-04).
- **Calendar (CAL-01..CAL-02):** CAL-01 the court year (weight-sealing to
  weight-sealing; no festival calendar claimed beyond the court's acts);
  CAL-02 the fair (E1+, the partner stages' occasion; the re-quote licence,
  SAY-01 V2's exception). No astronomical anchor is claimed (unlike D2's sky
  calendar): D4's calendar is institutional, and inventing a sky anchor would
  import a cosmology the brief refuses.
- **Five clocks kept separate (myth gate §5):** narrated time (the sayings'
  own "before the courts"), formation hypothesis (kept as design note),
  surviving witness (rod, ledger — both constructed), performance (the teller
  classes of §6), reception (the abbreviation convention's later reduction of
  SAY-03). No clock is equated with another.

### 8.5 Stage interfaces

- **Language stage interface:** stage tags E0–E2 with the language seat's
  declared sound changes (SC-*); the E0/E1 seam is where the ledger script
  and the western loan layer enter; the E2 freeze is a *spelling* event, not
  a sound event (era-language-staging §4: script reform and sound change are
  different processes).
- **Register interface (06):** the register law (registers `plain` and
  `quote`; slot admissibility; the plain-only oath law; the owed plain
  doublets) is the 06 seat's; my era component supplies the **dated
  emergence** (RG-01..RG-04) and the E3 split as an event. The plain doublet
  list is the 06 seat's; its dates come from RG-02/RG-04.
- **Measures/materials interface (10):** the era-side obligations: E0 local
  materials only; E1 the imported plain cloth route opens; E2+ the stamp's
  metal and the ledger's leaf stock; E3 cites the taught register, not new
  materials. The 10 seat owns routes and the SM-03 unresolved route.
- **Rank interface (12):** the rank ladder's eras (when each rank appears) are
  era-side facts supplied here for the 12 seat's rules to cite; the
  register-law rules (RG-05..RG-09) and their property kinds are the 12
  seat's.

## 9. Typed-label interface (my records)

The typed pipeline types every label into exactly three kinds (D2 precedent:
`tools/d2-typed-labels.py`; D2's projection = 58 labels, 46 native-form / 10
translated-label / 2 borrowed-strata, measured 2026-10-18). From my
components:

- **native-form** (sound-tested): emic era names (ER-01..ER-05's spoken
  forms), the sayings' operative words, the oath formulas' operative words,
  the mark names (SYM-01..SYM-08's emic forms), the rank names' era forms.
  All are **term requests** to the lexicon seat (TRQ-01..TRQ-16 below); this
  doc coins no spelling.
- **translated-label** (never sound-tested): every English gloss here (era
  glosses, saying titles, mark glosses, rank names' glosses).
- **borrowed-strata**: **none owned here.** The D4 loan ledger (AL-01..AL-06,
  `LAY-*` layers, the three-field donors, AL-03's held `ultimate: null`) is
  the 05/06 seats' records (brief §5 row 05, §6 Δ4). My components cite loan
  ids; they do not carry borrow blocks.
- **Form slots:** my components open **no form slots** (a form slot is the
  costume/goods device, `form_slot` + gloss). The sayings/oaths/marks are
  form-bearing records owned by the lexicon seat; an unfilled slot here would
  manufacture a hold by design, so the design does not create one.
- **Term requests (TRQ-01..TRQ-16, lexicon-owned ids):** TRQ-01 rod; TRQ-02
  notch; TRQ-03 stamp; TRQ-04 weight; TRQ-05 plain register (the register's
  own name); TRQ-06 quote register (its emic name — **note: this name's form
  is a quote-register form and carries `available_from: E3`**); TRQ-07 oath;
  TRQ-08 rod-mark; TRQ-09 court; TRQ-10 court-master; TRQ-11 broker; TRQ-12
  rod-holder; TRQ-13 apprentice; TRQ-14 ledger; TRQ-15 the guest's
  half-stamp; TRQ-16 the saying "spoken once" (its operative word). Each
  request names its record ids, its register (plain|quote), and its axis.
- **Quote/plain slot mechanics from my side:** where a saying's or oath's
  operative word is a quote-register form, the record cites its plain doublet
  slot (`<id>#plain`) so the 06 seat's owed-doublet machinery applies; my
  records never claim the doublet is supplied (that would be the 05 seat's
  form and the `D4L-REGISTER-UNRESOLVED` rows are the brief §7.1 row 2's).

## 10. Named hold set — pre-implementation (binding)

**Named before implementation.** No D4 packet, component, projection, or
expected-holds file exists at write time (`ls examples/culture-d4/` → exit 2,
2026-10-18T09:28Z; `reports/round-17/d4/components/` holds design drafts
only). The union hold set was proposed by `design-brief.md` §7.1 (candidate
18 holds / 1 note / 0 fails) and is **frozen as 17 holds / 1 note / 0 fails**
by the hold-set seat: `typed-support-2.md` §4 + the freeze record
`reports/round-17/d4/expected-holds.fragment.json` (schema
`kotodama-typed-pipeline-holds-v1`), whose amendment **A-19-1** drops the
brief's row 8 (`D4L-NATIVE` @ `QN-01`) because 02-phonology records no
delivered length minimal pair and 03-orthography declares no diacritics —
counts move 18/1/0 → 17/1/0. This section adopts the frozen fragment and
binds the **myth/era channel's slice** of it. Key form:
`(id, severity, where)`.

**10.1 My channel's holds (in the hold set):**

| id | severity | where | detail (design state) |
|---|---|---|---|
| `D4L-ERA` | hold | `RG-02` | the quote register's emergence is declared as a prose span (no tag) → `adapt_status: partial`, the raw string retained in `unresolved[]`; the adapter emits the hold and never promotes the span to a tag. Deliberate: the E3 split's exact boundary is a design question the culture's own records leave open (the "third court raised its weights, before the frozen hand" wording is the raw evidence). |

Count from my channel: **1 hold, 0 notes, 0 fails.** `RG-02` is bound by this
doc as an era-component record (component 09's register-emergence clocks,
brief §5 row 09 duty "per-form register-emergence clocks (Δ5)"). If the 06
seat carries the row instead, the row id moves to the 06 record and the delta
is recorded in the round's assembly doc — the *key* `(D4L-ERA, hold, 1 at
RG-02)` is what the brief §7.1 and the expected file compare.

**10.2 My channel's declared zeros (absent from the hold set, with the check
that enforces each):**

| class | declared count | enforcement check |
|---|---|---|
| `MC-*` (myth gate) | **0 findings** | `pantheon: NOT-APPLICABLE` + `pantheon_note` (§5.4); every ROLE-* carries a status and a basis (§5.3); every SAY-* carries a law with trigger/effect and variant records (§6); every SYM-* carries form+medium+era+register+audience (§7); no index claim without a checked witness (§6). Run: `python3 tools/gates/myth-consistency-gate.py examples/culture-d4/packet.d4.yml` → exit 0, zero `FINDING` lines. |
| `G-ERA` (costume gate) | **0 findings from my records** | every era my records cite is a contract tag (`E0..E3`) or a named era with its tag declared (§8.1); no record cites a prose span as an era value (RG-02's span is an `unresolved[]` raw string, never an `era` field). |
| `D4L-ERA` FAIL | **0** | every quote form is dated `available_from: E3` and no earlier (§8.2); the only prose-span row is RG-02, whose branch is the hold, not the fail. |
| `D4L-NATIVE` from my channel | **0** | no spelling is coined here; all emic forms are lexicon-owned term requests (§9). (The brief §7.1 row 8's `D4L-NATIVE` hold at `QN-01` was dropped by freeze amendment A-19-1 — 02-phonology delivers no length minimal pair — so this class is absent from the frozen set entirely.) |
| `D4L-FORM-UNRESOLVED` from my channel | **0** | no form slot is opened by components 07/08/09 (§9). |
| `D4L-BORROW` from my channel | **0** | no borrow block is owned here; the loan ledger is 05/06's (AL-01..AL-06; brief §7.1 rows 2–3). |
| `D4L-RANK` from my channel | **0** | no rank rule is written here; the register-law rules (RG-05..RG-09) are the 12 seat's (brief §7.1 rows 5, 7). |
| `D4L-SCOPE` from my channel | **0** | no `compare_only` exemption is requested; no untyped promotion. |

**10.3 The union as frozen (adopted from
`reports/round-17/d4/expected-holds.fragment.json`, 2026-10-18 — not re-bound
here):** `D4L-FORM-UNRESOLVED` ×6 (GD-01..GD-06);
`D4L-REGISTER-UNRESOLVED` ×6 (AL-01#plain..AL-06#plain); `D4L-BORROW` ×1
(AL-03); **`D4L-ERA` ×1 (RG-02 — this doc's row)**; `D4L-RANK` ×2
(RG-05#a|RG-07#a; RG-06#a|RG-09#a); `D4L-MATERIAL` ×1 (SM-03); `D4L-RANK`
note ×1 (RG-08#a|RG-08#b). Totals **17 holds / 1 note / 0 fails** — the
brief §7.1 candidate was 18/1/0 and freeze amendment **A-19-1** drops its row
8 (`D4L-NATIVE` @ `QN-01`; 02-phonology records no delivered length minimal
pair, 03-orthography declares no diacritics, so the D2 `L-15`/`L-16` class has
no D4 trigger). Zero fails in the delivered packet (every FAIL class lives in
controls, per brief §7.2 rule 4). Freeze rules: brief §7.2 (named before
implementation; every row provable by a named leg; severity never laundered
downward; a change is a recorded amendment naming the component decision that
forced it). The fragment's `detail` fields are null placeholders; the
delivered `examples/culture-d4/expected-holds.json` derives them from the
delivered typed run (the fragment's own `derivation` note).

**10.4 Reconciliation note (reported, not absorbed).** `design-costume.md`
was drafted before the brief landed and has since reconciled itself (its
revision note, `design-costume.md:20–22`, records the earlier littoral draft
and adopts the brief's NB-01); its §6 hold rows now match the brief's
`GD-01..GD-06` + `SM-03`. **Still open at this stamp:** `design-language.md`
(06:30) was drafted on an assumed maritime archipelago — islets, channels,
tide, boats, palm/mangrove bark — and its era note says "E3 reserved and
untouched", while the brief (authoritative) says inland plain, COUNT × QUOTE,
and **E3 = the register split**. My components follow the brief; the seed
reconciliation for the language slice is the integrator's to route. This doc
does not decide it and does not absorb it.

## 11. Coupling and dependency edges

Typed `F` (hard limit), `I` (interderive constraint), `T` (term), `R`
(reference) per `corpus/knowledge/synthesis/coupling-model.md` §3.

- `01-brief` — **F**: spine COUNT × QUOTE, the no-import list NB-01..NB-08,
  the registry, the artifact contract. The brief wins on any conflict (§0).
- `02-phonology` — **F**: the declared inventory bounds every emic form; the
  length/diacritic mark's existence is 02's decision; freeze amendment A-19-1
  records 02's decision that no delivered length minimal pair exists, so the
  brief §7.1 row 8 hold (`QN-01`) is dropped — my records carry no spelling
  regardless.
- `03-morphosyntax` — **T**: the classifier/measure morphology my era and
  mark records cite; the two argot derivations (`head2`, `reverse`) are 03's
  algorithms (brief §6 Δ3).
- `04-ledger-script` — **I**: the script seam (E0/E1) and the abbreviation
  convention (RG-04); sign values come from 02; the freeze (E2) is a spelling
  event my era record dates.
- `05-lexicon` — **T**: TRQ-01..TRQ-16; the quote stratum and AL-01..AL-06
  loan ids my records cite; each lexeme's `register` and `era_ids`.
- `06-register-contract` — **I**: registers `plain`/`quote`, slot
  admissibility, the owed plain doublets (my records cite `<id>#plain`
  slots; the doublet list is 06's), the plain-only oath law (OAT-01 is its
  speech-act instance).
- `10-measures-materials` — **I**: the era-side material obligations (§8.5);
  the SM-03 unresolved route is 10's.
- `11-costumes` — **I**: the sash/plain band and the rod-belt are costume
  records citing my marks by id (SYM-05/SYM-06); no garment content is
  asserted here.
- `12-ranks-names` — **I**: the rank ladder's eras (§8.5) and the
  register-law rules (RG-05..RG-09) that cite my register clocks (RG-01..RG-04)
  and OAT-01's speech-act property.

## 12. Acceptance checks

Declared now so implementation can be graded against them (repo-relative
commands, run from the lane root; all read-only).

1. **Components exist (12 + brief):** `ls examples/culture-d4/components/` →
   12 files; `07-oaths-sayings.yml`, `08-symbols-tokens.yml`,
   `09-eras-calendar.yml` are this doc's three.
2. **Myth gate clean:** `python3 tools/gates/myth-consistency-gate.py
   examples/culture-d4/packet.d4.yml` → exit 0, zero `FINDING` lines (§10.2).
3. **No G-ERA from my records:** the costume gate's output on the D4 packet
   contains no `G-ERA` line naming a record of components 07/08/09 (§10.2).
4. **Hold-set equality:** the typed packet's emitted finding set, keyed
   `(id, severity, where)`, equals the frozen expected file in both
   directions; the myth/era slice is exactly `D4L-ERA` ×1 at `RG-02` (§10.1);
   totals 17/1/0 as frozen (§10.3).
5. **The partial stays visible:** the projection's era section carries RG-02
   as `partial` with the raw span retained in `unresolved[]` and never
   promotes it (§8.2).
6. **No CE dates:** the D4 packet carries `source_era_dates` only; no numeric
   `era_dates` key and no CE-comparable value anywhere (§8.3).
7. **Determinism and replay:** the D4 assembler `--check` regenerates
   byte-identically twice; a new round-17 frozen manifest replays green
   (scope.md §5 D3/D4; brief §9.3).
8. **D2/D3 untouched:** `examples/culture-d2/` and `examples/culture-d3/`
   bytes equal the round-16 baseline; the D2 typed gate, D2 assembler /
   adapter / projector `--check`, and the D3 assembler `--check` stay green
   (scope.md §5 D6; brief §9.3).
9. **NON-CANON:** the D4 tree declares `canon_status: NON-CANON`,
   `handoff_status: prepared-not-accepted`, zero real-source bindings, and
   carries no real-world clearance, rights, or canon-acceptance assertion
   (brief §9.5; scope.md §5 D7).
10. **No fabricated provenance:** every comparator is an in-repo corpus entry
    cited by path and section; every unchecked claim is marked `(to-verify)`;
    the one deliberate open provenance state is the named hold (§10.1), not a
    silent guess.

## 13. Open questions (to-verify) and boundary notes

- **RG-02's raw span** (§8.2): the quote register's exact emergence boundary
  stays a prose statement by design; the hold is the record of that state.
- **The seed reconciliation** (§10.4): `design-language.md`'s assumed
  maritime archipelago and `design-costume.md`'s assumed littoral biome
  diverge from the brief's inland plain; the brief is authoritative here and
  the routing is the integrator's. Reported, not absorbed.
- **Freeze amendment A-19-1** (`expected-holds.fragment.json`): the brief's
  row 8 (`D4L-NATIVE` @ `QN-01`) is dropped from the frozen set; the brief's
  §7.1 table still carries it as the candidate row — the fragment is the
  freeze, and the delivered expected file follows the fragment.
- **The rank ladder's era dates** (§8.5): when each rank appears is supplied
  as era-side facts for the 12 seat; if the 12 seat's rules need finer
  intervals, the delta is an amendment, not a silent edit.
- **Boundary note (reported, never absorbed):** weigh-courts, broker argots,
  rod tallies, and guild-like rank ladders exist in the real world; every
  element above is constructed for the drill and screened by the
  transformation checklist (`real-world-inspiration-boundaries.md` §5). No
  real institution, guild, market, script, or argot is described, cited, or
  approximated; no rights, attribution, or clearance question is ruled on
  here. Any such question routes to the operator/lore as a report (PROVINCE).

## 14. Provenance, calibration, and revision log

- **Author:** R17-D03 (myth designer seat), 2026-10-18. All content is
  lane-authored design; no outside scholarship is asserted; comparators are
  in-repo corpus entries (§2).
- **Evidence status:** every record is a *design stipulation* (the F label of
  the matrix cell grammar) unless it cites a corpus entry; corpus entries'
  own provenance cautions are inherited and none is upgraded.
- **Counts used in this doc (all measured 2026-10-18, commands shown):**
  `ls corpus/knowledge/myth-symbol/*.md | wc -l` → 19; `python3 -c
  'import json;print(json.load(open("examples/culture-d2/expected-holds.json"))
  ["counts"])'` → `{'hold': 15, 'note': 1, 'fail': 0}`; `python3 -c 'import
  json;d=json.load(open("examples/culture-d2/typed-labels.d2.yml"));
  print(d["coverage"]["typed_labels"], d["coverage"]["labels_by_kind"])'` →
  `58 {'borrowed-strata': 2, 'native-form': 46, 'translated-label': 10}`;
  `ls examples/culture-d4/` → exit 2 (twice: 09:16Z, 09:28Z).
- **Negative sweeps:** "no D4 seed existed at r1" — swept `reports/round-13`,
  `reports/round-14`, `reports/round-16`, `LOG.md`, `SCORECARD.md`,
  `examples/`, and the fleet `.ufo/prompts/` directory for `culture-d4`/`D4`
  seed text (2026-10-18); only round-13's skipped claim, round-14/16
  retrospectives, and unrelated sibling-lane hits. "No D4 tree exists" —
  `ls examples/culture-d4/` → exit 2 at 09:16Z and 09:28Z.
- **Limits:** a design record, not an implementation, not a gate run, not a
  clearance, not canon. §12's checks are declared, not executed.
- **Revision log (append-only):**
  - **r1, 2026-10-18 ~09:2xZ, R17-D03:** initial pre-implementation design.
    The D4 seed was *declared by this doc* (a salt-flat caravan
    confederation, spine SALT × SHADE) because no brief existed in-repo at
    write time (proof: §0). Hold-set slice: `D4L-BORROW` ×1 at `L-24`.
  - **r2, 2026-10-18 09:3xZ, R17-D03:** reconciliation. The sibling
    `design-brief.md` (R17-D01) landed at 06:28 local while r1 was in flight
    and is authoritative: D4 is the **weigh-court quote register** culture,
    spine **COUNT × QUOTE**, with components 07-oaths-sayings /
    08-symbols-tokens / 09-eras-calendar (no pantheon component). r1's
    declared seed, its cosmology/pantheon/symbol/era content, and its
    `D4L-BORROW` at `L-24` are **withdrawn**; the brief's seed, the
    brief §7.1 union hold set (18/1/0), and the myth/era slice
    `D4L-ERA` ×1 at `RG-02` are adopted. Sibling docs read for this revision:
    `design-brief.md`, `typed-support-1.md`, `typed-support-2.md`,
    `design-costume.md` (the last is reported, not adopted — see §10.4).
    No filed round 8–16 artifact was touched.
  - **r3, 2026-10-18 ~09:3xZ, R17-D03:** hold-set alignment to the freeze
    record. `reports/round-17/d4/expected-holds.fragment.json` (typed-support-2,
    06:33 local) freezes the union at **17 holds / 1 note / 0 fails** via
    amendment **A-19-1** (brief §7.1 row 8, `D4L-NATIVE` @ `QN-01`, dropped:
    02-phonology delivers no length minimal pair, 03-orthography declares no
    diacritics). §10 now adopts the fragment as the frozen instance; the
    myth/era slice is unchanged: **`D4L-ERA` ×1 at `RG-02`**. §12's totals and
    §13's open items updated; `design-costume.md` §6 has meanwhile reconciled
    its slice to the brief's `GD-01..GD-06` + `SM-03`, so only the seed
    divergence (§10.4) remains open for the integrator. No filed round 8–16
    artifact was touched.
