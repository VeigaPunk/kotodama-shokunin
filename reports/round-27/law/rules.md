# R27-D02 — the register law, machine-readable: rule registry, replay surface, and the laws that cannot be replayed

- **Seat:** R27-D02 (D axis, law design 2 of 4), round 27, loop 3 build 3 of 4,
  claim **D** `register-law`.
- **Date:** 2026-10-18 (measurements 19:0x–19:16Z). Baseline revision
  `4f09c990d4c17f23b5e2cda0871f81db875635fc`; lane HEAD `b95fca1`.
- **Design authority:** `reports/round-27/law/design.md` (this round, seat R27-D01).
- **Delivered authority:** `reports/round-26/register/rules.md` (`535cf7a9…`) for
  the operation rule; `examples/culture-d4/components/04-lexicon.yml`
  (`d0d4e17c…`) for the `registers` block; `tools/d2-typed-labels.py`
  (`2819f687…`) for the projector's rank leg.
- **Write scope:** this file only, plus gitignored scratch under
  `.scratch/r27-law/`. `export TMPDIR=$PWD/.scratch` preceded every scratch write.
  No component, packet, tool, gate, fixture, pin file or filed 8–26 byte written;
  no commit, no push.
- **Canon:** NON-CANON engineering rules.

## 1. The rule registry (what a consumer can replay, and what it cannot)

The register law is stated as **six rules**, of which **one** is replayable by a
delivered gate and **five** are declarations. The column that matters is the last
one, and it is measured, not asserted (§3).

| id | rule | kind | replayable? | site that would replay it |
|---|---|---|---|---|
| `RLAW-01` | a `stamp` form is admissible only in a stamp-act slot | admissibility | **no** — no gate reads a slot | — |
| `RLAW-02` | only the named `speaker` may speak a given act | speaker | **no** | — |
| `RLAW-03` | an act whose speaker is outside its `speaker` set is **void**; nothing enters the roll | force/consequence | **no** | — |
| `RLAW-04` | a `stamp` form is `available_from: E1`; an E0 claim is a defect | era | **no** — the argot gate has no era concept | `argot-derivation-gate.py` (unowned) |
| `RLAW-05` | the register owns no segment; a `stamp` form is inventory-checked as a plain form | typing | **no** — the argot gate has no inventory leg | `argot-derivation-gate.py` (unowned) |
| `RLAW-06` | a `stamp` form is the plain base carried in by the operation the base's own `axis` selects | derivation | **yes** | `argot-derivation-gate.py` + `morphology.derivation_rules` |

`RLAW-06` is round 26's `REGISTER-OP-01` (`reports/round-26/register/rules.md` §2), adopted unchanged. It is
the only rule with an executable owner, and it is green:

```
$ python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: examples/culture-d4/packet.d4.yml records=170 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
exit 0
```

**The other five are the law this seat designs, and none of them is enforceable
today.** That is the honest state of `RLAW-01..05`, and it is recorded as `LL-3`
rather than presented as a green leg.

## 2. The packet bytes to add (Route A, the measured-cheapest landing)

The registry the law reads is the packet's `registers` block
(`04-lexicon.yml:244-253`). Four rows are delivered (`QREG-01..04`); the law adds
four:

```yaml
  - {id: QREG-05, title: "the charge", register: stamp, class: marked,
     speech_act: charge, speaker: "stamp-holder", force: directive-binding,
     consequence: "a count-stamp row in the furnace roll; the lot's count is binding",
     era_rule: "E1", axis: mark, evidence: design-choice, follows: [F-2],
     law: "spoken at the weigh-stone over a lot the speaker has already stamped with the speaker's own stamp; the charge makes the lot's count binding and nothing else."}
  - {id: QREG-06, title: "the attested oath", register: stamp, class: marked,
     speech_act: oath, speaker: "stamp-holder", force: commissive-binding,
     consequence: "the oath's term entered against the swearer's lineage bar",
     era_rule: "E1", axis: mark, evidence: design-choice, follows: [F-2],
     law: "spoken before the stamp-holder and the lineage bar; the holder speaks and the council enters the term. No master and no delegate may speak it."}
  - {id: QREG-07, title: "the naming of a lot", register: stamp, class: marked,
     speech_act: name-lot, speaker: "stamp-holder, mold-keeper", force: declarative-naming,
     consequence: "the lot's name written on the ingot's tally face",
     era_rule: "E1", axis: mark, evidence: design-choice, follows: [F-2],
     law: "the lot is named as it is sealed; the name is the mold-keeper's, and the mold-keeper's license is the stamp-house's to grant."}
  - {id: QREG-08, title: "the guest's charge", register: stamp, class: marked,
     speech_act: guest-charge, speaker: "broker, market-goer", force: "directive-binding, not-rollable",
     consequence: "the charge binds the goods at the market gate; it may not write the furnace roll",
     era_rule: "E1", axis: mark, evidence: design-choice, follows: [F-2],
     law: "a guest speaks the register under a stamp-name and is bound by it, but the guest keeps no roll. The asymmetry is the culture's: the council's roll is furnace right, not speech."}
```

**Field set added:** `speech_act`, `speaker`, `force`, `consequence`, `era_rule`.
The block's delivered fields are `id, title, register, class, law, axis, evidence,
follows` (`contract.record_fields.registers`, measured from the packet), and
`QREG-04` already carries the `era_rule` field — so `era_rule` is **not** new;
only four fields are.

**No assembler edit is required.** `RECORD_FIELDS["registers"] = ("id",)`
(`tools/assemble-culture-d4.py:118`) means the assembler validates only `id` on a
`registers` row; a new field is additive. The schema-side declaration belongs in
`01-brief.yml` `contract.record_fields.registers`, which is the one edit that
makes the new fields *declared* rather than merely present.

### 2.1 Why the `rank_rules` route is not taken (the Δ6 shape, priced)

The round-17 forecast's Δ6 asked for `property.kind: register` / `speech-act`
rows. Measured as Route B (`.scratch/r27-law/B/culture-d4/packet.d4.yml`,
`8cde9a71…`): **four rows, four holds**, one per row, and the rows are dropped
from `gate_rank_rules` entirely.

```
$ python3 tools/d2-typed-labels.py --packet .scratch/r27-law/B/culture-d4/packet.d4.yml
FINDING D2L-RANK: [hold] RK-05 — property kind 'register' is outside the gate model
…
coverage: … rank_rules_component=8, rank_rules_gate_projected=4, rank_rules_normalized=8, rank_rules_unresolved_items=4 …
```

Route A (`.scratch/r27-law/A/culture-d4/packet.d4.yml`, `2c177d47…`) produces
`findings_total=12` and `rank_rules_unresolved_items=0` — the delivered baseline
counts, unchanged. The A/B is in `design.md` §2.

### 2.2 Why the two kinds cannot simply be added to the guard

`GATE_PROPERTY_KINDS` (`tools/d2-typed-labels.py:970`) is a **membership guard**.
`verdict_for` (`:1315-1345`) dispatches on the kind and **falls through to
`return "not-applies"`**. Measured with the two kinds added to the frozenset:

```
$ python3 - <<'PY'   # re-executes the projector with the guard widened
WIDENED frozenset -> verdict_for(kind=register): 'not-applies'
```

So widening the guard converts an **honest hold** into a **silent non-evaluation**.
`design.md` §5 lists the seven-item amendment a real leg would need (E-1..E-7);
E-2/E-3 are a semantic change to `verdict_for`, not a table extension.

## 3. The replay surface, measured three ways

The law's own claims are checked against three independent readers, because a
single reader agreeing with itself proves nothing.

### 3.1 A tampered law row is invisible (the negative control)

```
$ python3 - <<'PY'   # delivered packet + the law rows, then `force: directive-binding` -> `force: no-such-force`
$ python3 tools/d2-typed-labels.py --packet .scratch/r27-law/A/culture-d4/packet.tamper.yml | grep -c FINDING
12
```

**The tampered packet emits exactly the same 12 findings as the clean one.** A
nonsense `force` value is not a finding anywhere. This is `LL-3` and it is the
single most important measurement in this file: **the law, as landable today, is
a declaration with no teeth.** It is not a defect of Route A — it is the state of
the tree, and it is why the enforcement leg is reported as unowned rather than
claimed.

### 3.2 The law's arithmetic is already green, and the law does not disturb it

```
$ python3 tools/gates/argot-derivation-gate.py .scratch/r27-law/A/culture-d4/packet.d4.yml
coverage: … records=172 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
$ python3 tools/gates/argot-derivation-gate.py .scratch/r27-law/B/culture-d4/packet.d4.yml
coverage: … records=174 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0
```

Both routes leave the derivation leg green (`violations=0`, `rule_holds=0`). The
law's cost is entirely on the projector's rank leg, which is why the A/B is
measured there.

### 3.3 The law's vocabulary ceiling (the constraint the rules must respect)

```
$ python3 - <<'PY'   # gloss-classification over the delivered 62-record lexicon
mark-axis plain words: 27   reverse-legal: 18   reverse-ILLEGAL: 9
mark-axis plain words by class x reverse-legality:
   material  reverse-legal= 8  reverse-ILLEGAL= 2
   abstract  reverse-legal= 0  reverse-ILLEGAL= 5
   other     reverse-legal=10  reverse-ILLEGAL= 2
```

Every one of the eight landed register forms descends from a **material-presence**
base. **Zero** descend from a legal/institutional abstraction, and all five
abstractions refuse `reverse` — including `L-30 gis` ("oath, sworn word"), whose
`reverse` is `sig`, an illegal D4 syllable. `RLAW-02`/`RLAW-03` are therefore
written so that **no act's law requires a `stamp` form for an abstraction**: the
act is named by a form the register can spell, and the *consequence* is carried by
the council's roll, which is written in the E2 league hand (`OR-03`), not in the
register.

## 4. The era rule and its unowned control

```
rule RLAW-04:
  a row with register == "stamp" and a speech_act must carry era_rule >= E1
  a stamp-act claimed at E0  ->  a finding (id unassigned)
```

Round 26 specified the same mechanism as `REGISTER-ERA-01` and measured that it
has **no executable owner** (`reports/round-26/register/rules.md` §5,
`reports/round-26/register/review.md` §6.2). This design
inherits that gap unchanged and does **not** re-measure it as a pass:

| # | control | fixture | expected | measured |
|---|---|---|---|---|
| C-E1 | a `stamp` form dated E0 | round-26 `ctrl-early-era.yml` | era FAIL | ❌ **no finding** — the gate has no era concept (`reports/round-26/register/rules.md` §5) |
| C-INV | an out-of-inventory register form | round-26 reviewer probe | FAIL | ❌ **no finding** — the gate has no inventory leg (`reports/round-26/register/review.md` §6.1) |
| C-LAW | a law row with a nonsense `force` | `.scratch/r27-law/A/culture-d4/packet.tamper.yml` | FAIL or HOLD | ❌ **no finding** — `rules.md` §3.1 |

Three ❌ rows, all with the same cause: the law's *typing*, *era* and *force* legs
are declared and unimplemented. The law's *arithmetic* leg is delivered and green
(`RLAW-06`). The registry above is the complete statement of which is which.

**A note on the era value.** `E1` is the delivered anchor: `RIT-03` the
stamp-taking is `era: E1`, `OR-02` "the extended stamp hand" is `stage: E1`, and
`ER-02` "the mark hand" `tag: E1` notes "the stamp inventory extended into the
native hand; **the first written charges**". The last phrase is the law's own
institution named in the delivered bytes. `QREG-04` already fixes the same era
for forms; the law extends it to acts.

## 5. The speaker sets, and the delivered rows that authorise them

| act | `speaker` | authorising delivered row | the row's own text |
|---|---|---|---|
| charge | `stamp-holder` | `RK-03` | authority `the stamp-house`; jurisdiction `the market and the weigh-stone`; `wearer_ranks: [stamp-holder, furnace-master]` |
| attested oath | `stamp-holder` **only** | `RK-03` + `RIT-03` | `RIT-03` felicity: "the first mark must be on the holder's own work; marking another's work voids the taking" |
| naming of a lot | `stamp-holder, mold-keeper` | `RK-03` + `OR-02` | `OR-02` institutions: "the stamp-house keeps the sign stamps; a **mold-keeper's license** is required to cut a new sign stamp" |
| guest's charge | `broker, market-goer` | `RK-04` | authority `the league charter`; jurisdiction `market days`; `eras: [E1, E2]`; `wearer_ranks: [market-goer, broker, furnace-master]` |

**Every speaker name above is a delivered string.** No new rank, office, or
institution is coined by this design: `stamp-holder`, `furnace-master`,
`mold-keeper`, `broker`, `market-goer`, `league delegate` all occur in the
delivered `rank_rules`, `costumes` or `orthography` records. The law assigns
speech to existing holders; it does not invent holders.

## 6. Declared limits of the rules

| id | limit | statement |
|---|---|---|
| **RU-L1** | the speaker sets are **enumerations**, not derivations | nothing computes who may speak; the set is stated. A later round wanting it derived must name the derivation |
| **RU-L2** | `force` is a **closed four-value set** here (`directive-binding`, `commissive-binding`, `declarative-naming`, `not-rollable`) | a fifth force would be a rule change; the set is declared so a reader can tell an addition from a variant |
| **RU-L3** | `consequence` is **free prose** | like `law:` today, it is not parseable; making it machine-readable is the enforcement leg's job (§2.2) |
| **RU-L4** | the law is **additive**; no delivered `QREG` or `RK` row changes | `QREG-01..04` keep their bytes; `RK-01..04` are cited, never amended |
| **RU-L5** | `RLAW-04`'s era bound reads `era_rule`, which the contract does **not** list | `contract.record_fields.registers` has no `era_rule`; `QREG-04` carries the field anyway. A contract change would silently empty the rule's domain — the same shape as round 26's `RU-3` for `axis` |
| **RU-L6** | the law does not cover **written** acts | `OR-02`/`OR-03` give the script its own charge conventions; whether a written charge is a stamp-act is **not decided here** and is named as an open question |

## 7. Controls

| # | control | command | expected | measured |
|---|---|---|---|---|
| C-A1 | Route A lands the law with **no** new hold | `d2-typed-labels.py --packet .scratch/r27-law/A/culture-d4/packet.d4.yml` | `findings_total=12`, `unresolved_items=0` | ✅ 12 / 0 |
| C-A2 | Route B (the Δ6 shape) costs one hold per row | `… B/culture-d4/packet.d4.yml` | 4 new holds, rows dropped | ✅ 16 total, `gate_projected=4` of 8 |
| C-A3 | the derivation leg is undisturbed by either route | `argot-derivation-gate.py` over A and B | `violations=0 rule_holds=0` | ✅ both |
| C-A4 | a tampered law row is invisible | `… A/culture-d4/packet.tamper.yml \| grep -c FINDING` | — | ❌ **12 — same as clean** (the gap, §3.1) |
| C-A5 | widening the kind guard yields a **silent** `not-applies` | §2.2 probe | — | ❌ `not-applies` (worse than the hold) |
| C-A6 | the law's vocabulary ceiling is real | §3.3 probe | abstractions refuse `reverse` | ✅ 5 of 5 illegal |
| C-A7 | the law's authorising offices are packet records | §5 record-presence probe | all speakers present | ❌ **`mold-keeper` absent** (`03-orthography.yml` has no `packet_keys`) — `review.md` §5 |

C-A4 and C-A5 are the two ❌ rows that justify this design's central choice: land
the law where it costs nothing and **name** the enforcement gap, rather than
open a projector amendment whose first effect is to hide the failure. C-A7 is the
third: it is why `QREG-07` is marked `to-verify` rather than landed as a
confident row.

### 7.1 The row that should not be landed as written

`QREG-07`'s `speaker: "stamp-holder, mold-keeper"` cites `OR-02`'s institutions
text, which is **component-only** (`review.md` §5). Until `03-orthography.yml`
declares `packet_keys` (or the office is declared somewhere the packet carries),
the honest landing of that row is either:

- `speaker: "stamp-holder"` only — the delivered, in-packet holder — with the
  `mold-keeper` named in the `law:` prose as the round-26 `OR-02` condition; or
- the full set, with the row marked `to-verify` and the missing office recorded
  as a named dependency on the orthography component's packet contribution.

**This design recommends the second**, because it keeps the component's own
institution visible rather than silently dropping it — but the choice is the
landing seat's, and it is stated here so the choice is made knowingly.

## 8. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 tools/d2-typed-labels.py --packet .scratch/r27-law/A/culture-d4/packet.d4.yml   # C-A1
python3 tools/d2-typed-labels.py --packet .scratch/r27-law/B/culture-d4/packet.d4.yml   # C-A2
python3 tools/gates/argot-derivation-gate.py .scratch/r27-law/A/culture-d4/packet.d4.yml # C-A3
python3 tools/d2-typed-labels.py --packet .scratch/r27-law/A/culture-d4/packet.tamper.yml | grep -c FINDING  # C-A4
python3 -c "import runpy;m=runpy.run_path('tools/d2-typed-labels.py');print(sorted(m['GATE_PROPERTY_KINDS']))" # C-A5 site
python3 -c "import runpy;n=runpy.run_path('tools/gates/naming-collision-gate.py');p=n['load_yaml'](open('examples/culture-d4/packet.d4.yml').read());print('mold-keeper' in open('examples/culture-d4/packet.d4.yml').read())"  # C-A7
sha256sum .scratch/r27-law/A/culture-d4/packet.d4.yml .scratch/r27-law/B/culture-d4/packet.d4.yml
grep -n "RECORD_FIELDS\[.registers.\]" -A 2 tools/assemble-culture-d4.py
grep -n "registers:" -A 12 examples/culture-d4/components/04-lexicon.yml | head -20
```
