# R27-D04 — review of the register law: what it settles, what it cannot, and the two defects it exposes

- **Seat:** R27-D04 (D axis, law design 4 of 4), round 27, loop 3 build 3 of 4,
  claim **D** `register-law` (`reports/round-27/claims.json`).
- **Date:** 2026-10-18 (measurements 19:0x–19:16Z). Baseline revision
  `4f09c990d4c17f23b5e2cda0871f81db875635fc` (round-26 admit); lane HEAD
  `b95fca1`.
- **Reviews:** this round's `design.md` (R27-D01) and `rules.md` (R27-D02),
  against the delivered bytes, plus the round-26 findings they inherit.
- **Write scope:** this file only, plus gitignored scratch under
  `.scratch/r27-law/`. `export TMPDIR=$PWD/.scratch` preceded every scratch write.
  No component, packet, tool, gate, fixture, pin file, or filed rounds 8–26 byte
  was written; no commit, no push.
- **Canon:** NON-CANON engineering evidence. Findings are review evidence, never
  canon rulings.

**Verdict in one line.** The register law is now **specified and hosted**: four
speech-act rows with a speaker, a force and a record consequence, landing in the
`registers` block at **zero** new holds (measured against the Δ6 alternative's
four), on institutions three of which are verified present as packet records —
but the law has **no replay leg at all** (a tampered row is invisible), its
vocabulary is bounded by an arithmetic ceiling that excludes **every** legal and
institutional abstraction in the delivered lexicon, and the design's own
citation audit exposed **two real defects in the delivered tree** that round 26
did not name: the orthography record block never reaches the packet, and the
"syllabify disagreement" is reader-dependent to the point of dissolving.

## 1. What is settled, and measured

| # | claim | command | result |
|---|---|---|---|
| S-1 | the law's arithmetic leg is green and undisturbed by the law | `argot-derivation-gate.py` over the delivered packet | `derived_pairs=8 violations=0 rule_holds=0`, exit 0 |
| S-2 | Route A (law in `registers`) costs **zero** new holds | `d2-typed-labels.py --packet .scratch/r27-law/A/culture-d4/packet.d4.yml` | `findings_total=12`, `rank_rules_unresolved_items=0` |
| S-3 | Route B (Δ6's `property.kind`) costs **one hold per row** and drops the rows | `… B/culture-d4/packet.d4.yml` | `findings_total=16`, `rank_rules_gate_projected=4` of 8 |
| S-4 | the Δ6 shape cannot be repaired by widening the kind guard | §2.2 probe | `verdict_for(kind=register)` → `'not-applies'` (silent) |
| S-5 | the delivered rank rules are untouched and still resolve | delivered packet | `RK-01..04`, 4 distinct `(kind, value, rite)` triples, `conflicts=0` |
| S-6 | every speaker name but one is a delivered string | packet census | `stamp-holder`, `furnace-master`, `broker`, `market-goer`, `league delegate` present; `mold-keeper` **absent** |
| S-7 | the standing battery and the typed gate are green at this HEAD | `check-gate-battery.py`; `typed-pipeline-gate.py` | `battery_exit 0, pass 7, fail 0`; `20/20 legs passed` |

Artifact digests at measurement (`sha256sum`):

| artifact | sha256 |
|---|---|
| `examples/culture-d4/packet.d4.yml` | `dd25077bc01681bc17f4586b40cfdd6959d4f45fc63e4f33f13fdc9b2cc88e67` |
| `examples/culture-d4/components/04-lexicon.yml` | `d0d4e17cc3c43a11e598259271fe16f18539c8bce3c3a30a40b6d2554b6c7240` |
| `examples/culture-d4/components/09-costumes.yml` | `82fb92ad17848fff8fe40421e6f15858ca79b9e6c90ba9e60e262b4cb48b8c8f` |
| `examples/culture-d4/components/03-orthography.yml` | `de1820b0c115271f7f86fbad8f7e6d637a6155cb61ad9a92cd53e32fdc08783e` |
| `examples/culture-d4/components/10-ritual-calendar.yml` | `5a8d41b4bc58997a8181c8f5ae8f2c279b48c92b76f6728deec23713a1ab85a2` |
| `tools/gates/argot-derivation-gate.py` | `5b5abe7865ed906c23fba87fd0dae8b6187c8dfc1a80137adbd364d4d88b0211` (measurement window) |
| `tools/d2-typed-labels.py` | `2819f68769dfc0b57f46cdaeb4c9a96324c5711c46348f5a8308382dfd7053c3` |
| `reports/round-26/register/design.md` | `27d23fa67d0bb920d1841d25c82b09919419ef58ef3b2f75494d950f3b5bb55a` |
| `reports/round-26/register/review.md` | `0082f08b62986ab2091a07acee464888fd68fa5312f19ef1b3817111a05f96e1` |
| probe A (law in `registers`) | `2c177d471e2df379f9646c30d1dfef818ee88062116b7ad613a2ed7888f835f9` |
| probe B (law in `rank_rules`) | `8cde9a7174f53814456fb6c02a74dcc74533046af537035be578ffeccbd6557c` |
| probe A, tampered (`force: no-such-force`) | `6ab1a96969c5a45ce14ccb6f2339a473716fbd5bec63360ae247de8279ee8f75` |

**A sibling seat changed one artifact inside this measurement window, and this
review records it rather than hiding it.** At the start of measurement
`tools/gates/argot-derivation-gate.py` was `5b5abe78…` (840 lines, `--selftest`
21/21); by the end of measurement it was `d7a3ad1a…` (uncommitted working-tree
change, `--selftest` **27/27**), a sibling round-27 seat's **legality-aware
syllabify** fix — which is precisely the repair §6 below calls for. Everything in
this file that depends on the gate was re-measured against the new bytes and is
**unchanged**:

```
$ for p in examples/culture-d4/packet.d4.yml .scratch/r27-law/A/culture-d4/packet.d4.yml \
           .scratch/r27-law/B/culture-d4/packet.d4.yml; do
    python3 tools/gates/argot-derivation-gate.py $p; done
… violations=0 rule_holds=0     (all three, identical to the 5b5abe78… window)
$ python3 tools/gates/argot-derivation-gate.py --selftest | tail -1
selftest: 27/27 checks passed
```

The reason the A/B is unaffected is stated in the sibling's own diff: **no
delivered `derived_from`/`derivation` record names `head2`** — the register
stratum uses `reverse` and `lengthen` only — so `head2`'s algorithm is not on the
register's path. The law's cost was never in the argot leg (§2 measures it in the
projector's rank leg), so the fix moves neither route's count.

## 2. Finding RL-1 — the law has no replay leg, and this is the design's central honesty

A law row whose `force` is nonsense is **invisible**:

```
$ python3 tools/d2-typed-labels.py --packet .scratch/r27-law/A/culture-d4/packet.tamper.yml | grep -c FINDING
12
$ python3 tools/d2-typed-labels.py --packet .scratch/r27-law/A/culture-d4/packet.d4.yml | grep -c FINDING
12
```

Identical. `force: "no-such-force"` produces no finding anywhere in the pipeline.
**The law, as landable today, is a declaration with no teeth.**

This is not a defect of the chosen route. It is the state of the tree, and it is
the reason `design.md` lands the law at zero cost and reports the enforcement leg
as an **unowned gap** rather than claiming a green leg. Round 26 named the same
class of gap three times (`RL-6`, `RL-8`, and `reports/round-26/register/review.md`
§6.1's missing typing
leg); this review names it once more, for the law, with the tamper control that
proves it.

**Disposition:** reported, not repaired. The repair is `design.md` §5's E-1..E-7,
and E-2/E-3 are a semantic amendment to `verdict_for` — not a design seat's file.
Named owner: whoever grows the projector's rank leg.

## 3. Finding RL-2 — Δ6's shape is unreachable, and widening the guard is worse than the hold

The forecast's Δ6 asked for `rank_rules` rows with `property.kind: register` /
`speech-act`. Measured (probe B):

```
$ python3 tools/d2-typed-labels.py --packet .scratch/r27-law/B/culture-d4/packet.d4.yml
FINDING D2L-RANK: [hold] RK-05 — property kind 'register' is outside the gate model
FINDING D2L-RANK: [hold] RK-06 — property kind 'speech-act' is outside the gate model
FINDING D2L-RANK: [hold] RK-07 — property kind 'speech-act' is outside the gate model
FINDING D2L-RANK: [hold] RK-08 — property kind 'register' is outside the gate model
coverage: … rank_rules_component=8, rank_rules_gate_projected=4, rank_rules_normalized=8, rank_rules_unresolved_items=4 …
```

The forecast's own text claims this shape gives "`cannot-evaluate` (A4), never a
pass" (`design-brief.md:350`). **That claim is half right, and the half that is
wrong matters.** The rows are `cannot-evaluate` — but they are also **dropped from
`gate_rank_rules`** (`gate_projected=4` of `normalized=8`), so the law would never
be *evaluated against anything*. `cannot-evaluate` with no evaluator is a hold
that can never close.

Worse, the obvious repair fails:

```
$ python3 - <<'PY'   # GATE_PROPERTY_KINDS widened with "register","speech-act"
WIDENED frozenset -> verdict_for(kind=register): 'not-applies'
```

`verdict_for` (`tools/d2-typed-labels.py:1315-1345`) branches on `material`/
`fiber`/`cloth`, `garment`, `badge`, `trim`/`closure`, and **falls through to
`return "not-applies"`**. Widening the guard turns an honest hold into a **silent
pass-through**. The kind set is a membership guard, not a dispatch table.

**Disposition.** This design takes Route A and records the full price of Route B
(`design.md` §5). The forecast's Δ6 is **not adopted**, and the reason is
measured rather than stylistic: its home is a costume-rank ledger whose resolver
reads `row["material"]` / `row["garment"]` / `row["badge_office"]` — fields a
speech act does not have.

## 4. Finding RL-3 — the register cannot spell its own law's vocabulary

Measured over the delivered 62-record lexicon:

```
mark-axis plain words: 27   reverse-legal: 18   reverse-ILLEGAL: 9
mark-axis plain words by class x reverse-legality:
   material  reverse-legal= 8  reverse-ILLEGAL= 2
   abstract  reverse-legal= 0  reverse-ILLEGAL= 5
   other     reverse-legal=10  reverse-ILLEGAL= 2
```

The five legal/institutional abstractions in the delivered lexicon are
`L-15 wer` (road's right-of-way), `L-30 gis` (**oath, sworn word**), `L-44 wad`
(price), `L-45 tikmes` (the script), `L-51 gul` (weight). **All five refuse
`reverse`.** `gis → sig` is not a legal D4 syllable.

And every one of the eight landed register forms descends from a
**material-presence** base:

```
L-56 kit  <- tik   mark, stamp       L-55 tuum <- tum  breath
L-57 lom  <- mol   mold, cast form   L-58 nees <- nes  water
L-59 huum <- hum   smoke             L-60 mees <- mes  metal, ingot
L-61 reek <- rek   ore               L-62 saam <- sam  charcoal
```

**Zero abstractions.** The register, as landed, is the vocabulary of *things at
the weigh-stone*, not of *obligations*.

**Consequence for the law.** The oath — the one act whose *bindingness* is the
law's whole subject — cannot be named in the register. `QREG-06` is therefore
written to name the act by a form the register can carry (`tuum`, the breath
sworn by) and to put the consequence on the council's side, which is where the
delivered tree puts the record anyway.

**Disposition.** Declared as `LL-1`/`LL-2` and designed around, not repaired. The
repair would be an operation-rule amendment (an escape hatch for abstractions),
which round 26 already priced as "a rule change requiring a recorded amendment"
(`reports/round-26/register/review.md` §3). **This design does not amend it.**

## 5. Finding RL-4 — the orthography record block never reaches the packet

While auditing the law's citations, the design found that
**`03-orthography.yml` declares no top-level `packet_keys`**, so the assembler
falls back to the `PACKET_KEYS` allowlist (`tools/assemble-culture-d4.py:76-108`)
and records everything outside it under `assembly.skipped_keys`:

```
$ python3 - <<'PY'   # assembly.skipped_keys, filtered to 03-orthography
  skipped from 03: lexicon_requests, literacy_institutions, numeral_register,
                   orthography_rules, records, signs, …
```

**OR-01/OR-02/OR-03 (the `records` block) and LI-01..LI-03 (the
`literacy_institutions` block) are not packet records.** The packet's
`orthography` block is the summary scalar set only: `case`, `direction`, `type`,
`signs` (a count), `scheme`, `notes`. The `OR-` ids survive only as
**cross-references inside prose** — `ER-01`'s `record_stage` "…03's OR-01…",
`ER-02`'s "…03's OR-02…", `ER-03`'s "…03's OR-03…" — never as records, and the
`LI-` ids do not appear in the packet **at all**. Measured:

```
$ for id in OR-01 OR-02 OR-03 LI-01 LI-02 LI-03 EN-01 EN-02; do
    printf "%s: %s\n" "$id" "$(grep -c "$id" examples/culture-d4/packet.d4.yml)"; done
OR-01: 1   OR-02: 1   OR-03: 2
LI-01: 0   LI-02: 0   LI-03: 0
EN-01: 0   EN-02: 0
```

Measured:

```
$ python3 - <<'PY'   # packet record presence
   RK-03   block=rank_rules   present_as_record=True
   RK-04   block=rank_rules   present_as_record=True
   RIT-03  block=rites        present_as_record=True
   OR-02   block=(skipped)    present_as_record=False
   LI-02   block=(skipped)    present_as_record=False
   EN-01   block=(skipped)    present_as_record=False
```

**The same holds for `09-costumes.yml`'s `enforcement` block**: `EN-01` and
`EN-02` — the delivered tree's *only two enforcement mechanisms* — are
component-only, recorded under `assembly.skipped_keys['enforcement']`. The
`01-brief` registry row for C-03 claims `packet_keys: [orthography]`, which is
accurate about the *scalar* block and silent about the records.

**This is the same class as round 26's RD-1** (cited where-keys absent from the
delivered tree) and it is **new**: round 26's review did not name it. Its cost is
concrete — a design that cites OR-02 or EN-01 as a law's authority is citing a
byte the gates cannot see, and `mold-keeper` (the design's `QREG-07` speaker) is
the first casualty: it is legal in the component and **absent from the packet**.

**Disposition.** Reported, not repaired — `03-orthography.yml` is not this seat's
file, and adding a `packet_keys` line to it would change the packet and move
every pin in the lane (the O claim's surface). The design adapts: three of the
four law rows are anchored to verified in-packet institutions (`RK-03`, `RK-04`,
`RIT-03`), and `QREG-07` is marked `to-verify`.

## 6. Finding RL-5 — the "syllabify disagreement" is reader-dependent, and at the design's own reading it is 8 of 70, not 15 of 62

The claim's `before` carries round 26's measurement: "the gate's syllabify
disagrees with the design's maximal-onset algorithm on **15 of 62** forms". This
seat re-measured it, and the number is a property of the *reader*, not the gate.

| reader | disagreement vs the gate's `syllabify` |
|---|---|
| naive maximal-onset (consonants always join the next syllable) | **0 of 70** |
| legality-checking maximal onset (`design-language.md:191-196`, read literally) | **8 of 70** |
| round 26's reported figure (`reports/round-26/register/review.md` §5) | 15 of 62 |

```
$ python3 - <<'PY'   # legality-checking maximal onset vs the gate's syllabify
  disagreements: 8 of 70 delivered forms
    tikmes | gate= ['ti', 'kme', 's'] | design= ['tik', 'me', 's']
    tumhai | gate= ['tu', 'mha', 'i'] | design= ['tum', 'ha', 'i']
    kalker | gate= ['ka', 'lke', 'r'] | design= ['kal', 'ke', 'r']
    samren | gate= ['sa', 'mre', 'n'] | design= ['sam', 're', 'n']
    mestum | gate= ['me', 'stu', 'm'] | design= ['mes', 'tu', 'm']
    meslun | gate= ['me', 'slu', 'n'] | design= ['mes', 'lu', 'n']
    kalnes | gate= ['ka', 'lne', 's'] | design= ['kal', 'ne', 's']
    salwer | gate= ['sa', 'lwe', 'r'] | design= ['sal', 'we', 'r']
```

**The finding is that the disagreement is not a stable quantity.** The gate's
`syllabify` at `5b5abe78…` (`argot-derivation-gate.py:135-160`) implemented
"consonants always join the next syllable" — a maximal onset with no legality
test. The design's stated algorithm adds one clause: "*whenever that yields a
legal syllable*" (`design-language.md:191-196`). Whether those two differ
**depends entirely on what "legal" means to the reader**:

- if a reader treats any consonant string as a syllable onset, the two algorithms
  coincide and the disagreement is **zero**;
- if a reader applies D4's real onset constraint (`onset_clusters: false`,
  `02-phonology.yml`) plus the coda set, the disagreement is **8**;
- round 26's reader produced **15**, which is a third reading this seat could not
  reproduce from the delivered bytes.

### 6.1 The fix landed mid-round, by a sibling seat — and it resolves the ambiguity in the right direction

Late in this measurement window a sibling round-27 seat landed a
**legality-aware** `syllabify` in the working tree (`d7a3ad1a…`, uncommitted,
`--selftest` **27/27**). It makes the design's clause executable and states the
predicate explicitly (`CODAS`, `ONSET_CLUSTERS = False`, quoted from
`02-phonology.yml`), so "a legal syllable" is no longer reader-dependent. Its own
docstring records the consequence: `tikmes` is `tik.mes`, never `ti.kme.s`, and
`ker` is one syllable, never `ke.r`.

**This changes the direction of the disagreement, and the change is worth
recording.** Re-measured against the new bytes, the new gate now disagrees with
*this review's* legality-checking reader on **66 of 70** forms — because the two
readers differ on a **word-final consonant run**: this review's reader kept it as
a separate coda-only syllable (`ker` → `['ke','r']`), the new gate attaches it to
the preceding syllable (`ker` → `['ker']`).

```
$ python3 - <<'PY'   # the NEW gate (d7a3ad1a) vs this review's legality-checking reader
  disagreements: 66 of 70
    ker  | gate= ['ker'] | this reader= ['ke', 'r']
    tum  | gate= ['tum'] | this reader= ['tu', 'm']
    bak  | gate= ['bak'] | this reader= ['ba', 'k']
```

**The new gate's reading is the better one, and this review says so.** A
word-final consonant run belongs to the last syllable's coda: `ker` is a
monosyllable, and a `['ke','r']` analysis invents a syllable with no nucleus.
The 66-form divergence is therefore **this review's reader being wrong**, not the
new gate's — and it is exactly the kind of instability RL-5 was filed to name.
The correct statement of the algorithm is now the one in the new gate's
docstring, and it should be lifted into `design-language.md` so the design's
prose and the gate's implementation stop being two things a reader has to
reconcile.

**Consequence for the law.** None, directly — the law builds no form with `head2`
(round 26's `RL-2` already established `head2` is an identity over the delivered
tree). But the claim's `after_required` says "the syllabify disagreement **fixed**
(one algorithm, forms re-verified)", and this review's honest position is that
**the disagreement cannot be fixed by choosing an algorithm while the design's
own prose is ambiguous about what "legal syllable" means.** The fix is a
definition, not an implementation: state the legality predicate, then either the
gate's algorithm or the design's is provably wrong.

**Disposition.** Reported with all three pre-fix readings and the exact 8-row
witness list; §6.1 records the sibling seat's fix, the new gate's digest, and the
one place this review's own reader was wrong. **The remaining action is a
documentation one**: lift the new gate's legality predicate into
`design-language.md` so the design's prose and the gate's implementation state
one algorithm. The `head2` consumer is the only site affected, and it has none.

## 7. Finding RL-6 — the law's four acts are selected, and its speaker sets are enumerations

Nothing derives the act set. The four acts exist because the delivered tree
supplies institutions for them (`RK-03`, `RK-04`, `RIT-03`) and because each
carries a distinguishable force. A fifth act would be as arbitrary as these four
unless a later round names a derivation. Likewise `speaker` is an enumeration per
act, not a computed set. Declared as `LL-6`, `RU-L1`.

This is not a defect so much as a **scope statement**: the law is a *declaration*
in the same sense the delivered `RK-01..04` are declarations (`evidence:
design-choice` throughout). What the law adds over the round-26 prose is
structure — three named fields per act — and the structure is what makes the
enforcement leg *buildable* later.

## 8. Finding RL-7 — the `D4L-RANK` id in the forecast has zero producers

The forecast's Δ6 names `D4L-RANK` holds (`design-brief.md:351`). Census:

```
$ grep -rn "D4L-RANK" tools/ examples/ | wc -l
0
$ grep -n "D2L-RANK\|R-RANK-UNSUPPORTED" tools/d2-typed-labels.py
420:  "D2L-ERA", "D2L-MATERIAL", "D2L-RANK", "D2L-SCOPE")
2246:  "D2L-RANK": "D2L-RANK",
2273:  ("R-RANK-", "D2L-RANK"),
2862:  findings.append(normalize_finding("R-RANK-UNSUPPORTED", item["rule"], item["item"], "hold"))
```

The live ids are **`D2L-RANK`** and **`R-RANK-UNSUPPORTED`**, and they already
fire for exactly the case Δ6 describes — measured on probe B (§3). Same shape as
round 26's RD-6 (`D4L-ARGOT-DERV` has zero producers): a consumer matching the
forecast text literally finds nothing, while the mechanism it asks for is
delivered under a different name.

## 9. Summary table

| id | finding | severity | disposition |
|---|---|---|---|
| RL-1 | the law has no replay leg; a tampered row is invisible (12 = 12 findings) | **high** | reported; owner named; `design.md` §5 prices the repair |
| RL-2 | Δ6's shape costs 4 holds and drops the rows; widening the guard yields a silent `not-applies` | **high** | Δ6 not adopted; Route A taken; A/B measured |
| RL-3 | the register cannot spell any legal/institutional abstraction; all 8 forms are material bases | design constraint | declared `LL-1`/`LL-2`; law written inside the ceiling |
| RL-4 | `03-orthography.yml` declares no `packet_keys`, so OR-01..03 and LI-01..03 never reach the packet; `09-costumes.yml`'s `enforcement` (EN-01/02) likewise | **high, new** | reported; `QREG-07` marked `to-verify`; not repaired (not this seat's file) |
| RL-5 | the "15 of 62" syllabify disagreement is reader-dependent: 0, 8, or 15 by reading | medium, new | **fix landed mid-round by a sibling seat** (`d7a3ad1a…`, §6.1); remaining action is to lift the predicate into `design-language.md` |
| RL-6 | the act set and the speaker sets are enumerations | scope statement | declared `LL-6`, `RU-L1` |
| RL-7 | `D4L-RANK` has zero producers; the live ids are `D2L-RANK`/`R-RANK-UNSUPPORTED` | cosmetic | recorded |

## 9a. Closing note — a sibling seat landed the law while this review was being written

**The landing seat's own work confirms this design's central A/B, independently.**
Before this review was finalized, a sibling round-27 seat (`R27-D05..D12`, per
`examples/culture-d4/components/13-register-law.yml`'s header) landed the register
law as a **new component 13** with a **new packet block `register_law`**
(`packet_keys: [register_law]`, rows `RGL-01..RGL-05`). It took **Route A's
shape** — a new block beside `registers`, **not** `rank_rules` rows with
`property.kind` — which is the route this review's §2/§3 measured as the zero-cost
one. Measured on the landed packet:

```
$ python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml | grep -o 'findings_total=[0-9]*'
findings_total=12          # the delivered baseline count, unchanged
$ python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1
summary: 20/20 legs passed
$ python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml | grep -o 'violations=[0-9]* rule_holds=[0-9]*'
violations=0 rule_holds=0
```

**The law lands at zero new holds, exactly as this review predicted.** That is
the prediction confirmed by an independent implementer working from the same
evidence.

**Two observations from comparing the landed component against this design**, both
offered as review evidence rather than as defects:

1. **The landed rows carry no `force` field.** Measured, `RGL-01..05`'s key set is
   `{id, register, axis, kind, act, holder, consequence, evidence, follows, cite}`
   — `holder` does the work of this design's `speaker`, and `kind`
   (`admissibility` / `exclusion` / `asymmetry` / `no-segment` / `era`) does part
   of the work of `force` by classifying the *rule*. What has no counterpart is
   the **illocutionary** value on the *act* — this design's
   `directive-binding` / `commissive-binding` / `declarative-naming`. Whether that
   is a gap depends on whether a consumer needs to distinguish *binding a
   listener* from *committing a speaker* — §3 of `design.md` argues it
   does, because the guest asymmetry (`QREG-08` / the landed `RGL-03`) is exactly
   a force difference, not a holder difference.
2. **The new block is not declared in the schema.** `contract.record_fields` has
   no `register_law` key (measured: `None`), and `01-brief.yml`'s C-13 registry
   row is absent — so the block arrives in the packet **undeclared by the
   contract**, which is `LL-4`'s shape recurring at a new address. This is the
   same class of finding as `design.md` §6's note that the schema-side
   declaration belongs in `01-brief.yml`.

**This review does not revise its measurements to match the landing.** Everything
in §1–§9 was measured against the committed HEAD packet
(`dd25077bc01681bc17f4586b40cfdd6959d4f45fc63e4f33f13fdc9b2cc88e67`) and the
committed `argot-derivation-gate.py` (`5b5abe78…`); the landed packet is
`c5441e3d0b237f331cfabe8002ad3bf4db7694e2666c21ba8c723ac66bf21f6a` and the gate
is `d7a3ad1a…`. Both windows are recorded so a reader can tell which bytes any
number came from.

## 10. What this seat did not do

- Did not write any component, packet, tool, gate, fixture or pin file. The three
  probes live under `.scratch/r27-law/` and were **not promoted**.
- Did not land the law. This seat's assignment is the design (three files); the
  landing is a separate seat's, and `design.md` §6 names the exact bytes and the
  exact owner.
- Did not repair `tools/d2-typed-labels.py`, `tools/gates/argot-derivation-gate.py`,
  or `03-orthography.yml`. All three findings that have owners outside this seat
  are reported with their price.
- Did not amend the round-26 operation rule (`mark → reverse`, `fire → lengthen`)
  or propose an escape hatch for abstractions.
- Did not resolve the culture question, claim any form as attested, or perform a
  real-language resemblance screening (CAL-1).
- Did not read the sibling R27 seats' outputs (`pinsweep/`, `readme/`, `audit/`,
  `scribe/`) or touch their files.

## 11. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch
python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml        # S-1
python3 tools/d2-typed-labels.py --packet .scratch/r27-law/A/culture-d4/packet.d4.yml # S-2, 12 findings
python3 tools/d2-typed-labels.py --packet .scratch/r27-law/B/culture-d4/packet.d4.yml # S-3, 16 findings
python3 tools/d2-typed-labels.py --packet .scratch/r27-law/A/culture-d4/packet.tamper.yml | grep -c FINDING  # RL-1, 12
python3 tools/check-gate-battery.py | tail -6                                        # S-7
python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml | tail -1  # S-7
python3 -c "import runpy;m=runpy.run_path('tools/d2-typed-labels.py');print(sorted(m['GATE_PROPERTY_KINDS']))"  # RL-2 site
python3 -c "import runpy;n=runpy.run_path('tools/gates/naming-collision-gate.py');p=n['load_yaml'](open('examples/culture-d4/packet.d4.yml').read());print([k for k,v in p['assembly']['skipped_keys'].items() if any('03-orthography' in x for x in v)])"  # RL-4
grep -rn "D4L-RANK" tools/ examples/ | wc -l                                          # RL-7, 0
sha256sum reports/round-27/law/{design,rules}.md
```
