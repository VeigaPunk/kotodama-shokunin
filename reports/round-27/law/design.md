# R27-D01 — the register law: the speech-act component the stamp register is missing

- **Seat:** R27-D01 (D axis, law design 1 of 4), round 27, loop 3 build 3 of 4,
  claim **D** `register-law` (`reports/round-27/claims.json`).
- **Date:** 2026-10-18 (measurements 19:0x–19:16Z). Baseline revision
  `4f09c990d4c17f23b5e2cda0871f81db875635fc` (round-26 admit); lane HEAD
  `b95fca1` ("round-27: declare claims D/O/C").
- **Reads first, as the assignment directs:** `reports/round-26/register/design.md`
  (`27d23fa6…`), and its siblings `forms.md` (`06635a1c…`), `rules.md`
  (`535cf7a9…`), `review.md` (`0082f08b…`), `impl.md` (the landing).
- **Write scope:** `reports/round-27/law/{design,rules,review}.md`, plus
  gitignored scratch under `.scratch/r27-law/`. `export TMPDIR=$PWD/.scratch`
  preceded every scratch-writing command. No component, packet, tool, gate,
  fixture, pin file, or filed rounds 8–26 byte was written; no commit, no push.
  No file of the sibling R27 seats (`pinsweep/`, `readme/`, `audit/`, `scribe/`)
  was read for content or touched.
- **Canon:** NON-CANON engineering design. No real language, institution, script
  or argot is described, cited or approximated. No clearance is claimed.

## 0. The gap this seat closes, restated in the round-26 review's own words

Round 26 landed the register stratum's **arithmetic** and named, as its own
finding **RD-5c**, the thing this seat owns:

> "The delivered tree has **no component that owns a register law**. … The five
> law rows in `reports/round-26/register/forms.md` §5 (RGL-01..RGL-05) are design
> statements with no home.
> `packet_keys` admits `registers` and `doublets`, so the landing is additive —
> but **someone must own it**" — `reports/round-26/register/review.md` §6.3

The round-26 `design.md` §6 assigned the law to "`06-myth.yml` / `07-symbolism.yml`'s
contract rows, or a new register-contract component", and
`reports/round-26/register/rules.md` §4 recorded
the same as `RL-6`. Round 26's landing put a *description* of the law in the
packet — `QREG-02` carries a `law:` string that mentions stamp-act slots — but a
description is not a law: it names no speaker, no force, and no consequence, and
nothing can replay it.

**This design closes RD-5c / RL-6.** It specifies the register law as a
speech-act component and names the exact bytes, the exact owner, and the exact
cost of landing it.

## 1. What the law is, and what it refuses to be

**The law is the admissibility-and-consequence rule set of the `stamp`
register.** It answers three questions per speech act, and nothing else:

| question | field | why it is the law's, not the lexicon's |
|---|---|---|
| **who may speak** | `speaker` | a register is a social variety; the lexicon cannot say who holds it |
| **with what force** | `force` | illocutionary force is what makes a spoken word bind; it is not a lexical property |
| **with what record consequence** | `consequence` | the delivered tree is a *record* culture (`SEED-06`, `AS-05`): an act that leaves no record is not an act here |

**It refuses to be three other things**, each of which a reader could mistake it
for:

1. **Not a second phonology.** 02's own law holds and the round-26 design adopted
   it: *no register owns a private segment* (`02-phonology.yml` `strata_note`;
   `reports/round-26/register/design.md` §2). The law adds no segment, no
   syllable, no form. Every `stamp`
   form is checked on the sound channel exactly as a plain form, and the law
   never touches a form.
2. **Not a canon statement.** The law says what the *system* permits. Whether any
   town observed it is lore-shokunin's (`PROVINCE.md`: kotodama hands off
   systems).
3. **Not a rank rule by another name.** §4 draws that boundary precisely, because
   it is the boundary the forecast itself got wrong.

## 2. The host: why the `registers` block, measured rather than assumed

Two landing routes exist. Both were built as probes against the delivered bytes
and **both were measured**, because the difference is not a matter of taste — one
costs holds and one does not.

**Route A — the law rows live in the `registers` block** (`QREG-05..`, new fields
on a block that already exists). The block is declared by `04-lexicon.yml` and
admitted by `tools/assemble-culture-d4.py:81`; `RECORD_FIELDS["registers"] =
("id",)` (`:118`) so a new field is additive and needs **no assembler edit**.

**Route B — the law rows are `rank_rules` with `property.kind: register` /
`speech-act`** — the shape the round-17 forecast's **Δ6** asked for
(`design-brief.md:342-355`).

Measured, both probes = the delivered packet plus the law rows, built by a text
transform of the delivered bytes (never a re-serialization):

| route | probe | `d2-typed-labels.py --packet …` | new holds |
|---|---|---|---|
| **A** | `.scratch/r27-law/A/culture-d4/packet.d4.yml` (`2c177d47…`) | `findings_total=12`, `rank_rules_unresolved_items=0` | **0** |
| **B** | `.scratch/r27-law/B/culture-d4/packet.d4.yml` (`8cde9a71…`) | `findings_total=16`, `rank_rules_unresolved_items=4` | **4** |

Route B's four holds are exactly one per law row, and they are the forecast's own
declared behaviour:

```
$ python3 tools/d2-typed-labels.py --packet .scratch/r27-law/B/culture-d4/packet.d4.yml
FINDING D2L-RANK: [hold] RK-05 — property kind 'register' is outside the gate model
FINDING D2L-RANK: [hold] RK-06 — property kind 'speech-act' is outside the gate model
FINDING D2L-RANK: [hold] RK-07 — property kind 'speech-act' is outside the gate model
FINDING D2L-RANK: [hold] RK-08 — property kind 'register' is outside the gate model
coverage: … rank_rules_component=8, rank_rules_gate_projected=4, rank_rules_normalized=8, rank_rules_unresolved_items=4 …
```

**This design takes Route A, and the reason is a constraint, not a preference.**
Δ6's shape is unreachable without a projector amendment, and the amendment is
larger than it looks — §5 measures that. Route A is the *cheapest* landing
against the delivered bytes: the same mechanism, zero new holds, no tool edit.

**Route A is not a compromise on the law's content.** Everything Δ6 wanted — a
rule that says which register a speech act must use, and what a mis-registered
act costs — is expressible as a `registers` row. What Δ6 wanted that Route A
cannot give is *gate enforcement* of it. §5 names that, and names what enforcing
it would actually cost, so the choice can be re-made on evidence.

## 3. The law rows: four acts, stated exactly

Four acts, chosen because they are the four the delivered tree already supplies
the *institutions* for, and because each carries a different force. This is a
filter, not a list of favourites.

| id | act | speaker (who may speak) | force | record consequence |
|---|---|---|---|---|
| `QREG-05` | **the charge** | `stamp-holder` (and `furnace-master` by `RK-03`) | `directive-binding` | a count-stamp row in the furnace roll; the lot's count is binding |
| `QREG-06` | **the attested oath** | `stamp-holder` **only** — no master, no delegate | `commissive-binding` | the oath's term entered against the swearer's lineage bar |
| `QREG-07` | **the naming of a lot** | `stamp-holder`, `mold-keeper` | `declarative-naming` | the lot's name is written on the ingot's tally face |
| `QREG-08` | **the guest's charge** | `broker`, `market-goer` — **in-register, but asymmetrically** | `directive-binding`, `not-rollable` | the charge binds the goods at the gate; it may **not** write the furnace roll |

The asymmetry in `QREG-08` is the delivered tree's own: `RK-04` permits the
`broker` and `market-goer` at `market days`, and the packet's own era record
`ER-03` says "the furnace roll and the league council" — so a guest speaks and is
bound but keeps no record. That is the round-26 `RGL-03` ("a guest broker may
speak `stamp` under a stamp-name but may not keep the furnace roll"), now with a
speaker, a force and a consequence attached.

`QREG-06`'s speaker restriction is the round-26 `RGL-02` ("an oath spoken in
`stamp` is **void**; the binding oath is plain") resolved in the only direction
the arithmetic permits — §3.2.

**One speaker in the table above is component-only, and the table says so.**
`mold-keeper` occurs in `03-orthography.yml` (`OR-02` institutions, `LI-02`) and
in `05-naming.yml` (`craft_office`), but **`03-orthography.yml` declares no
`packet_keys`**, so its `records` and `literacy_institutions` blocks are recorded
under `assembly.skipped_keys` and **do not reach the packet**
(`assembly.skipped_keys['records'] = ['…/03-orthography.yml']`, measured). The
packet's `orthography` block is the summary scalar set only (`case`, `direction`,
`type`, `signs`, `scheme`, `notes`).

**Consequence, and it is a defect this design reports rather than papers over:**
`QREG-07`'s `speaker: mold-keeper` names an office that **no packet record
carries**. It is legal in the component, legal in `05-naming`'s prose, and
invisible to every gate that reads the packet. This is finding **RL-4** in
`review.md` §5 — the same class as round 26's RD-1 (cited where-keys that do not
exist in the delivered tree), and it is why `QREG-07` is marked `to-verify` in
`reports/round-26/register/rules.md` §2 rather than landed as a confident row.

### 3.1 The law binds the delivered rank rules and the council, and says how

The law is not free-standing. Each row names the institution that authorises it,
so a reader can trace the act to its licence. **The column that matters is the
third: whether that institution is actually in the packet** — because a licence
the gates cannot see is not a licence.

| law row | authorising row | in the packet? | what the row already says |
|---|---|---|---|
| `QREG-05` | `RK-03` `the stamp-house` | ✅ **yes** (`rank_rules`) | permits `stamp-holder`/`furnace-master` the `maker's stamp` at `attesting work` |
| `QREG-06` | `RK-03` + `RIT-03` `the stamp-taking` | ✅ **yes** (`rank_rules`, `rites`) | the holder's first mark is on the holder's own work; marking another's voids the taking |
| `QREG-07` | `RK-03` + `OR-02` | ⚠️ `RK-03` yes; **`OR-02` no** | `OR-02` is component-only; `mold-keeper` is absent from the packet (above) |
| `QREG-08` | `RK-04` `the league charter` | ✅ **yes** (`rank_rules`) | permits `broker`/`market-goer` at `market days`, `E1–E2` |

Measured:

```
$ python3 - <<'PY'   # packet record presence, over the packet's own blocks
   RK-03   block=rank_rules   present_as_record=True
   RK-04   block=rank_rules   present_as_record=True
   RIT-03  block=rites        present_as_record=True
   OR-02   block=(skipped)    present_as_record=False
   LI-02   block=(skipped)    present_as_record=False
   EN-01   block=(skipped)    present_as_record=False
```

**Three of the four law rows stand on in-packet institutions.** The fourth
(`QREG-07`) stands on a component-only office, and that is declared.

**The council's role is the consequence channel, not the speaker.** The council's
presence in the packet is real but thinner than the components suggest: `OR-03`'s
"the league council keeps the furnace roll" is component-only, and what the
packet actually carries is `ER-03` ("the literate anchor; the furnace roll and
the league council", `era_records`) and `ER-02`'s seam text. `EN-01`/`EN-02` —
the two enforcement mechanisms — are **component-only** as well
(`09-costumes.yml`'s `enforcement` key is not in its `packet_keys`). So the law
reads: *the speaker makes the act; the council makes the act a record* — and the
council's mechanism is cited from the component while its **existence** is
grounded in the packet's era records. `QREG-08`'s `not-rollable` is precisely the
statement that the council does not enter a guest's charge.

### 3.2 The arithmetic the law inherits, and the one act it cannot licence

The law sits on top of the round-26 operation rule (`mark → reverse`,
`fire → lengthen`, `reports/round-26/register/rules.md` §2) and therefore
inherits its partiality. Measured
this round over the delivered 62-record lexicon:

```
mark-axis plain words: 27   reverse-legal: 18   reverse-ILLEGAL: 9
```

The nine refusals are not random, and **the law's own vocabulary is in them**:

| class | count | members |
|---|---|---|
| material presence (fire/nature/craft nouns) | 8 legal, **2 illegal** | `L-08 wak`, `L-17 bek`, `L-24 wat`, `L-26 gim` legal; `L-30 gis→sig`, `L-51 gul→lug` illegal |
| **legal / institutional abstraction** | **0 legal, 5 illegal** | `L-15 wer→rew` (road's right-of-way), `L-30 gis→sig` (**oath**), `L-44 wad→daw` (price), `L-45 tikmes→semkit` (the script), `L-51 gul→lug` (weight) |

```
$ python3 - <<'PY'   # classification by gloss over the delivered packet
mark-axis plain words by class x reverse-legality:
   material  reverse-legal= 8  reverse-ILLEGAL= 2
   abstract  reverse-legal= 0  reverse-ILLEGAL= 5
   other     reverse-legal=10  reverse-ILLEGAL= 2
```

**This is the design's most important finding, and it is a design constraint the
law must be written around.** Every one of the eight landed register forms
(`L-55..L-62`) descends from a **material-presence** base — `tik` (mark), `mol`
(mold), `tum` (breath), `nes` (water), `hum` (smoke), `mes` (metal), `rek` (ore),
`sam` (charcoal). **Not one descends from an abstraction.** The register, as
landed, is the vocabulary of *things at the weigh-stone*, not of *obligations*.

The oath is the sharp case: `L-30 gis` ("oath, sworn word; the mark that attests
it") is `axis: mark`, so the rule sends it to `reverse`, and `sig` is not a legal
D4 syllable — **the register cannot say the word "oath" in itself.** The law
therefore cannot be built on a `stamp` form for the oath. `QREG-06` states the
act in terms the register *can* carry (`tuum`, the breath sworn by) and names the
consequence on the council's side, which is where the delivered tree puts the
record anyway.

**This is a design choice, and it is labelled as one.** The alternative — adding
an escape hatch to the operation rule so abstractions can enter — is a rule
change, and round 26 already recorded its cost (`reports/round-26/register/review.md`
§3: "a later round
that wants a larger stratum must either accept the rule's partiality … or add an
escape hatch, which would be a rule change requiring a recorded amendment").
This design does **not** amend it. It reports the constraint and writes the law
inside it.

## 4. The boundary against the delivered rank rules (the Δ6 confusion, resolved)

The forecast folded the register law into `rank_rules` as a `property.kind`.
**That is the wrong home, and the delivered bytes show why.** The two systems
regulate different things and are enforced by different mechanisms:

| | `rank_rules` (delivered, RK-01..04) | the register law (this design, QREG-05..08) |
|---|---|---|
| regulates | **what may be worn** — a `material` or a `badge` | **what may be said, and what it makes true** |
| property | `property: {kind, value}` over a physical thing | `speech_act` + `speaker` + `force` + `consequence` |
| enforcement | `EN-01` the council's fine; `EN-02` the stamp-holder's refusal to **mark** | the act is **void** (`not-rollable`) — nothing enters the roll |
| evidence field | `wearer_ranks`, `rites`, `eras` | `speaker`, `force`, `consequence` |
| the projector's leg | `family_rank_payload` → `gate_rank_rules` → `R-RANK-CONFLICT` | **none exists** (§5) |

The forecast's own Δ6 text confirms the split: its example rule is *"a plain oath
is binding; an oath in the quote register is void"* — a rule about **speech
validity**, which its own adapter then forced into a costume-rank ledger whose
`verdict_for` resolves `property.value` against a **costume row's** `material` or
`badge` field. A speech act has no costume row to resolve against. The Δ6 shape
was a category error that the delivered pipeline's failure mode (`cannot-evaluate`,
"never a pass" — `d2-typed-labels.py:2737`) has been hiding rather than exposing.

**The rank rules are not bypassed by this design.** `QREG-05..08` name RK-03/RK-04
as their authorising rows (§3.1), so the two systems are *linked* rather than
merged: the rank rule says who holds the stamp; the law says what holding it lets
you say and what the saying costs.

## 5. What enforcing the law would cost, measured (Route B's real price)

Route A is cheap. This section measures what Route B would need, so the choice is
recorded on evidence rather than on the forecast's assertion.

Widening the gate's kind set is **not sufficient**, and this is measurable:

```
$ python3 - <<'PY'   # tools/d2-typed-labels.py with "register","speech-act" added to GATE_PROPERTY_KINDS
WIDENED frozenset -> verdict_for(kind=register): 'not-applies'
```

`GATE_PROPERTY_KINDS` (`tools/d2-typed-labels.py:970`) is a **membership guard**,
not a dispatch table. `verdict_for` (`:1315-1345`) branches on `material`/`fiber`/
`cloth`, `garment`, `badge`, `trim`/`closure`, and then falls through to
`return "not-applies"`. Adding the two kinds to the frozenset moves the failure
from an exception (`Malformed: property kind 'register' is outside the gate's
modelled set`) to a **silent `not-applies`** — a law that is never evaluated and
never reported. That is strictly worse than the current honest hold.

A real enforcement leg would need, at minimum:

| # | change | site |
|---|---|---|
| E-1 | two new kinds in the guard | `GATE_PROPERTY_KINDS`, `tools/d2-typed-labels.py:970` |
| E-2 | a **dispatch branch** that resolves a speech act against a **speech** row, not a costume row | `verdict_for`, `:1315-1345` |
| E-3 | a non-costume target: today `verdict_for` reads `row["material"]`, `row["garment"]`, `row["badge_office"]` — none exist on a speech act | same |
| E-4 | `GATE_KIND_MAP` / `GATE_VALUE_MAP` entries, or the kinds route to `cannot-evaluate` forever | `:975-984` |
| E-5 | a hold id for the new leg — the forecast's `D4L-RANK` has **0 producers**; the live id the projector emits is `D2L-RANK`/`R-RANK-UNSUPPORTED` (`tools/d2-typed-labels.py:2273,2862`), and it already fires for exactly this case | `:2246,2273` |
| E-6 | the freeze rule: a new hold id must not be invented for an id the projector never emits (`SKILL.md:149`) | policy |
| E-7 | re-pin `tools/d2-typed-labels.py` in the three places the lane byte-pins it (`expected-holds.json` `projector_sha256`, `typed-pipelines.json`, the frozen round-22 row) | pins |

**E-2 and E-3 are the load-bearing items**: they are a semantic amendment to the
family projector, not a table extension. That is why this design lands the law in
`registers` (Route A) and reports the enforcement leg as an **unowned, declared
gap** with its full price — rather than opening a projector amendment inside a
design seat. §5 of `review.md` records the gap and its owner.

## 6. Owners

| artifact | owner | what they owe |
|---|---|---|
| the four law rows (`QREG-05..08`) as packet records | **`04-lexicon.yml`** (it already declares `packet_keys: […, registers]` and carries `QREG-01..04`) | add the rows with `speech_act`, `speaker`, `force`, `consequence`, `era_rule`, `law`; **no assembler edit** — `RECORD_FIELDS["registers"] = ("id",)` |
| the `registers` record-field declaration | **`01-brief.yml`** `contract.record_fields.registers` | currently `[id, title, register, class, law, axis, evidence, follows]`; add the five new fields, or the schema does not declare what the rows carry |
| the law's replay leg | **unowned — declared gap** | §5's E-1..E-7. Until it exists, the law is a *declaration*, and `QREG-05..08` are exactly as enforceable as `QREG-02`'s prose today |
| the speech-act **vocabulary** (which acts exist) | **`10-ritual-calendar.yml`'s `rites` block** or a successor | `RIT-03` already names `attesting work`; the acts in §3 are `rites`-adjacent and should be declared beside them if a later round wants the acts themselves machine-readable |
| the enforcement ids | **the O/typed seats** | `EN-01`/`EN-02` are costume-side; a speech-act enforcement row has no home yet. Named, not invented |
| the holds | **the O/typed seats** | Route A adds **zero** holds (measured, §2). Route B adds one per row. `D4L-ARGOT-DERIV` stays control-only |

## 7. Named limits (declared, not silently skipped)

| id | limit | measured |
|---|---|---|
| **LL-1** | the law **cannot licence an act whose vocabulary the register cannot spell**: all 5 legal/institutional abstractions refuse `reverse`, including `L-30 gis` (the oath itself) | §3.2 |
| **LL-2** | the landed register's forms are **100 % material-presence bases** (8 of 8); the law is written inside that ceiling, not against it | §3.2 |
| **LL-3** | the law has **no replay leg**; a tampered law row (`force: "no-such-force"`) produces **the same 12 findings** as a clean one | §5, `review.md` §2 |
| **LL-4** | `registers` rows carry `id` as their only required field (`assemble-culture-d4.py:118`), so a **malformed law row passes the assembler** | §2 |
| **LL-5** | the law is a **design choice**; no informant, corpus or frequency evidence exists for any speaker, force or consequence | `design.md` §7, `review.md` §7 |
| **LL-6** | the four acts are **selected**, not derived: the delivered tree supplies institutions for them, but no rule generates the act set | §3, `review.md` §7 |
| **LL-7** | the law does **not** bind `RK-01`/`RK-02` (forge work, the league assembly) — those are non-attesting contexts; a reader may reasonably expect a fuller coupling | §3.1 |
| **LL-8** | one law row's authorising office (`mold-keeper`, `QREG-07`) is **component-only**: `03-orthography.yml` declares no `packet_keys`, so its `records`/`literacy_institutions` blocks never reach the packet | §3, `review.md` §5 |
| **LL-9** | the law's `consequence` strings are **free prose**, like `law:` today; nothing parses them | `rules.md` §6 RU-L3 |

## 8. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
sha256sum reports/round-26/register/{design,forms,rules,review}.md
python3 tools/d2-typed-labels.py --packet .scratch/r27-law/A/culture-d4/packet.d4.yml   # Route A: 12 findings
python3 tools/d2-typed-labels.py --packet .scratch/r27-law/B/culture-d4/packet.d4.yml   # Route B: 16 findings
python3 tools/gates/argot-derivation-gate.py .scratch/r27-law/A/culture-d4/packet.d4.yml # violations=0
python3 tools/d2-typed-labels.py --packet .scratch/r27-law/A/culture-d4/packet.tamper.yml | grep -c FINDING   # 12 — no law leg
python3 -c "import runpy;m=runpy.run_path('tools/d2-typed-labels.py');print(sorted(m['GATE_PROPERTY_KINDS']))"
grep -rn "D4L-RANK" tools/ examples/ | wc -l     # 0 producers
```
