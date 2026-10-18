# R26-D01 — the register stratum: design against the delivered furnace-league tree

- **Seat:** R26-D01 (D axis, register design 1 of 4), round 26, loop 3 build 2 of 4,
  claim **D** `register-stratum` (`reports/round-26/claims.json:14-23`).
- **Date:** 2026-10-18. Baseline `fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`
  (round-25 admit); worktree HEAD `1ad491a` (`git log --oneline -1`).
- **Sources:** `reports/round-17/d4/design-language.md`
  (`cfc2d698559ed552c85b527c3a34e32e4fe308cfd093137483f9d3c782b462cc`) and
  `reports/round-17/d4/design-brief.md`
  (`a5fdc84dfe3f98e92068e2737f6447c9adec82ff669914b3e22963ee8447e78f`).
- **Write scope:** `reports/round-26/register/{design,forms,rules,review}.md`, plus
  gitignored scratch under `.scratch/r26-d-reg/`. `export TMPDIR=$PWD/.scratch`
  preceded every scratch-writing command. No tool, gate, fixture, component,
  packet, pin file, or filed rounds 8–25 byte was written; no commit, no push.
- **Canon:** NON-CANON engineering design. No real language, institution, script,
  or argot is described, cited, or approximated. No clearance is claimed.

## 0. What this file fixes, and what it refuses to fix

It fixes the **register stratum's design**: the register's identity, its form
set, the operation each form is derived by, the era window, the owners, and the
reconciliation with the tree that actually shipped. `forms.md` carries the
forms, `rules.md` the machine-readable rules, `review.md` the verdict against
the delivered bytes.

It does **not** write the forms into `examples/culture-d4/`, does not edit the
argot gate, does not touch `expected-holds.json`, and does not decide the canon
question. Those are named as requirements with owners (§5).

## 1. The reconciliation that has to come first

Round 17 left **three cultures on file** and shipped a fourth-shaped tree. The
argot design was written against the one that did **not** ship.

| source | culture / spine | status |
|---|---|---|
| `design-brief.md:30-50` | weigh-court brokerage; **COUNT × QUOTE** | not shipped |
| `design-language.md:61` | **TIDE + LEDGER** (its own stated assumption) | not shipped |
| `design-myth-era.md` | salt-flat caravan confederation | superseded by the brief seat's own protocol |
| `components/01-brief.yml:78-91` | furnace-league; **FIRE × MARK** | **shipped** (path A, `reports/round-25/argot/delta.md:1.2`) |

The consequence for this design is not "the argot was forgotten". It is that
**the argot's where-keys name records that do not exist**: `AL-01..AL-06`,
`GD-01..GD-06`, `QN-01`, and the whole `D4-Xnn` measure/numeral series. Measured
this round:

```
$ grep -rl "AL-0" examples/ | wc -l          # 1 (inside "CAL-01", unrelated)
$ grep -rl "D4-X" examples/ tools/ | wc -l   # 0
$ grep -c "registers\|doublets" examples/culture-d4/packet.d4.yml   # 0 keys
```

So the register stratum cannot be "reconciled" by re-lettering a few rows. It
has to be **re-hosted**: the same culture-independent mechanism (§6 of the
brief, "what is portable") instantiated on the FIRE × MARK record set that is
on disk. The brief seat named the host itself:

> "the furnace-league's own spine offers a natural host for Δ1/Δ6 ('the
> mold-mark is the truth-mark', `components/01-brief.yml:80`: an attestation
> register distinct from plain speech)" — `design-brief.md:659-661`

This design takes that route. It is the only one that does not supersede a
shipped component (round-25 delta §4 Δ-step 7 route (i)).

## 2. The register: what it is

**The register is `stamp`.** In-world it is the **attestation register**: the
speech a stamp-holder uses when a spoken word is being made to bind, as against
the plain speech of the forge floor and the household.

- **Plain** is the unmarked register — the forge, the household, the road. It is
  the baseline, not a member of the stratum (`rules.md` §1 fixes the unmarked
  set).
- **`stamp`** is the marked register. A form in `stamp` is admissible only in a
  stamp-act slot: a charge spoken at the weigh-stone, an oath attested before
  the stamp-holder, a lot named as it is sealed.

This is coherent with the delivered spine rather than imported onto it:

| delivered record | how it carries the register |
|---|---|
| `01-brief.yml:80` SEED-02 "the mold-mark is the truth-mark" | the register is the *speech* half of the mark institution |
| `07-symbolism.yml:28` SYM-01 "the mold-mark", `register: "craft and law"` | the symbol surface already declares a `register`; the stratum's register is the same axis, made grammatical |
| `03-orthography.yml:57-58` OR-02/OR-03 | the script's written-charge convention is the written face of the same act |
| `09-costumes.yml:134-137` RK-01..RK-04 | rank rules are permits over `badge`/`material` — the register law is the *speech* permit beside them |
| `04-lexicon.yml:192-195` CX-01..CX-03 | the three delivered construction rules the register forms must not disturb |

**What it is not.** It is not D2's pitch accent, not D1's penultimate stress, not
a second phonology. 02's own law holds: *no register owns a private segment*
(`design-language.md:87-91`, adopted). Every `stamp` form in `forms.md` is
inventory-legal and syllable-legal under 02's PHON-01, and the gate grades it on
the sound channel exactly as a plain form.

## 3. Where the forms come from — the rule the delivered data already carries

The forecast fixed the operations (`head2` for measure words, `reverse` for the
numeral series) and the *bases* those operations ran on. The delivered tree has
neither: there is no numeral series and no measure ladder (`04-lexicon.yml`
`declared_gaps`). What the delivered tree **does** carry, on every lexicon and
name record, is an `axis` — and it carries exactly two values, distributed
almost evenly:

```
axis census (lexicon, 54 records): {mark: 27, fire: 27}
axis census (names, 8 records):    {fire: 6, mark: 2}
```

The spine (SP-01 fire, SP-02 mark, `01-brief.yml:89-90`) therefore supplies the
operation-selection rule the forecast supplied by hand:

| axis | operation | why, in the delivered terms |
|---|---|---|
| `mark` | `reverse` | the mark reverses the work: the stamp is the impression of the mold, the term is the form read back to front |
| `fire` | `lengthen` | the fire lengthens: the stressed root vowel is drawn out as the word is held over the mark |

This is a **design choice**, and it is labelled as one. Its virtue is that it is
*total over the delivered tree* and *machine-checkable*: `rules.md` §2 states it
as a rule the gate can replay, and `review.md` §3 measures what it costs (it is
not total — 13 of 54 lexicon forms and 2 of 8 names yield an unusable form).

## 4. The form set: 8 register forms

Eight, in the assignment's 6–10 band, chosen by a stated filter rather than by
taste. Each is a `mark`-axis or `fire`-axis root from the delivered lexicon,
carried into `stamp` by the §3 rule.

| id | base | axis | op | form | gloss |
|---|---|---|---|---|---|
| RF-01 | L-02 `tum` | fire | lengthen | `tuum` | the breath the smith swears by |
| RF-02 | L-42 `tik` | mark | reverse | `kit` | the mark itself, spoken |
| RF-03 | L-38 `mol` | mark | reverse | `lom` | the mold, named in the register |
| RF-04 | L-16 `nes` | fire | lengthen | `nees` | the quench water, named |
| RF-05 | L-09 `hum` | fire | lengthen | `huum` | the smoke that carries the word |
| RF-06 | L-43 `mes` | fire | lengthen | `mees` | the ingot as an attested lot |
| RF-07 | L-37 `rek` | fire | lengthen | `reek` | the ore as an attested lot |
| RF-08 | L-39 `sam` | fire | lengthen | `saam` | the charcoal as an attested lot |

The full arithmetic, the legality check of every form, and the collision sweep
against the delivered tree and the D2 fixture ledger are in `forms.md` §1.
**All 8 are inventory-legal, syllable-legal, and collision-free** — measured,
not asserted.

**A note on RF-01/RF-05.** `tum` (breath) and `hum` (smoke) both lengthen to a
`uu` form. `tum → tuum` and `hum → huum` are distinct, and the table above is
corrected: RF-01's form is **`tuum`**, not `huum` (that is RF-05). RF-03 was
likewise moved from `L-36 kal` to `L-38 mol` so that every form follows the §3
axis rule strictly: `kal` is a `fire`-axis record (`04-lexicon.yml:168`), so
under the rule it takes `lengthen` (`kaal`), not `reverse`. Both corrections are
left visible rather than silently folded, because a design table that disagrees
with its own receipt is exactly the class of defect this lane's gates exist to
catch. `forms.md` §1 carries the authoritative table and the receipt digests.

## 5. Era scoping

The register is dated to the seam the delivered eras already declare.

| register | available_from | evidence |
|---|---|---|
| `plain` | E0 | unmarked; the forge and household speech, present from `E0` (`08-eras.yml:28`) |
| `stamp` | **E1** | the register is the speech of the **stamp-house**, which `03-orthography.yml:57` dates to E1 (OR-02, "the extended stamp hand"; the stamp-house keeps the sign stamps and licenses a mold-keeper) |

E1, not E3. The forecast's `E3` came from the weigh-court's register split
(`design-brief.md:328-341`, Δ5); the furnace-league's `E3` is **reserved and
unoccupied** (`08-eras.yml:31`, "the cold fire (reserved)", `span: "undated"`).
Dating the register to E3 would put every `stamp` form in an era the delivered
packet explicitly leaves empty. E1 is the era the tree actually supplies for the
attesting institution.

**A form claimed in an earlier era is a finding.** A `stamp` form with
`stage: E0` is `D4L-ERA` — the mechanism the forecast asked for (Δ5), now with
a delivered trigger. `forms.md` §3 states the control.

## 6. Owners

| artifact | owner | what they owe |
|---|---|---|
| the 8 register forms as packet records | **`04-lexicon.yml`** (lexicon, `layers`, `constructions`, `morphology`) | add the records with `register: stamp`, `derived_from`, `derivation`, `stage: E1`; add the `LENGTHEN` rule to `morphology.derivation_rules` |
| the register declaration block | **a new `registers:` packet block** — declared by `04-lexicon.yml` or a re-cast `06-*` component | `packet_keys` already admits `registers` and `doublets` (`tools/assemble-culture-d4.py:81,118`) and `RECORD_FIELDS["registers"] = ("id",)`, so no assembler edit is needed; the block is additive |
| the register *law* (admissibility, oath-only-plain, the guest asymmetry) | **`06-myth.yml` / `07-symbolism.yml`'s contract rows**, or a new register-contract component | the law is prose-plus-rules; the delivered tree has no `06-register-contract.yml` (the forecast's registry was re-planned, delta A-8) |
| the machine-readable rules | **`04-lexicon.yml` `morphology.derivation_rules`** | the `LENGTHEN` pattern/output pair (`rules.md` §3) |
| the checking leg | **`tools/gates/argot-derivation-gate.py`** (already landed, `5b5abe78…`) | nothing to write; the gate already replays `derived_from`/`derivation` |
| the holds | **the O/typed seats** | `D4L-REGISTER-UNRESOLVED` per owed plain doublet; `D4L-ARGOT-DERIV` stays control-only |

**No new component is required.** The stratum is additive: 8 lexicon records, 1
derivation rule, 1 packet block. That is the cheapest landing against the
delivered bytes and the reason this route was taken.

## 7. What the delivered argot gate already does with these forms

The leg exists (`tools/gates/argot-derivation-gate.py`, 840 lines, `--selftest`
21/21) and it keys on exactly the shape this design supplies. Measured this
round over a probe packet = the delivered packet + the 8 records:

```
$ python3 tools/gates/argot-derivation-gate.py .scratch/r26-d-reg/probe.yml
coverage: .scratch/r26-d-reg/probe.yml records=164 register_scoped=14 \
          derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=6
exit 1
```

`derived_pairs=8`, `violations=0` — the eight `reverse`/`lengthen` rows that the
gate can replay **replay clean**. `rule_holds=6` is the six `lengthen` rows it
cannot: `lengthen` is not a declared operation. Declaring it as a
`pattern`/`output` pair (`rules.md` §3) turns the same probe to:

```
coverage: … derived_pairs=8 … violations=0 rule_holds=0
exit 0
```

And the control the forecast asked for (C-02, `design-brief.md:456`) fires: with
`kit` mutated to `kat`, the gate emits

```
FINDING D4L-ARGOT-DERIV: FAIL — register-scoped form RF-02 'kat' (register 'stamp'):
  declared chain 'reverse' applied to 'tik' yields 'kit'; the stated inputs and rules
  do not yield the candidate
```

So the mechanism is delivered and discriminating. What is missing is the **data**
— which is what this design supplies.

## 8. Named limits (declared, not silently skipped)

| id | limit | measured |
|---|---|---|
| **RL-1** | the §3 axis→operation rule is **not total**: 13 of 54 lexicon forms yield an unusable register form (illegal or colliding) | `review.md` §3 |
| **RL-2** | `head2` has an **empty proper domain**: 59 of 62 delivered forms are ≤2 syllables, so `head2(form) == form` is an identity, not a derivation | `review.md` §4 |
| **RL-3** | the delivered gate's `syllabify` disagrees with `design-language.md:191-196`'s stated maximal-onset algorithm on **15 of 62** delivered forms | `review.md` §5 |
| **RL-4** | `reverse` is **not expressible** as a `pattern`/`output` pair — the template subset refuses slicing — so it must stay a computed operation in the gate | `rules.md` §3 |
| **RL-5** | the register's forms are a **design choice**; no frequency, corpus, or informant evidence exists for any of them | CAL-1 in `forms.md` |
| **RL-6** | the register **law** (admissibility, oath-only-plain, guest asymmetry) is specified but not implemented anywhere; the delivered tree has no component that owns it | §6 |

## 9. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
sha256sum reports/round-17/d4/design-language.md reports/round-17/d4/design-brief.md
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml   # register_scoped=6 derived_pairs=0
python3 tools/gates/argot-derivation-gate.py .scratch/r26-d-reg/probe.yml       # derived_pairs=8 violations=0
python3 tools/gates/argot-derivation-gate.py .scratch/r26-d-reg/probe-rule2.yml # rule_holds=0, exit 0
python3 tools/gates/argot-derivation-gate.py .scratch/r26-d-reg/probe-bad.yml   # D4L-ARGOT-DERIV fires
grep -rl "AL-0" examples/ | wc -l ; grep -rl "D4-X" examples/ tools/ | wc -l
```
