# Register-lexicon ceilings — what a register's derivation operation cannot say

- topic: Why a marked register built by a **mechanical operation** (reversal, truncation, lengthening, reduplication) can only spell some of the semantic fields its own institution needs — and how to measure the ceiling before it is designed into a law. States the general craft rule (**a register's derivation operation constrains which semantic fields it can natively spell**), gives the measurement procedure over a syllable template, works the NON-CANON D4 stamp register as a measured case (four of five legal/institutional abstractions refuse `reverse`), and supplies the three dispositions (hand-pick the base list, choose an operation whose domain covers the needed fields, or accept the ceiling and write the law inside it) plus the calibration shelf for the real-world analogues (verlan, anti-languages, avoidance registers) and their limits. Reference knowledge and method only; canon decisions belong to lore-shokunin.
- gap filled: the partition teaches how to **build** a register's lexicon (`corpus/knowledge/linguistics/sociolinguistics-registers.md` §4 on register strata; `corpus/knowledge/linguistics/semantic-fields-lexicon-building.md` §3–§4 on semantic-field engineering; `corpus/knowledge/linguistics/linguistic-anthropology.md` §5 on special languages) and how to state a **register law** over it (`corpus/knowledge/linguistics/register-strata-attestation.md`), but **no entry measures what an operation-constrained register cannot say**, and none states the ceiling as a design constraint with a check. Absence sweep 2026-10-18 from the lane root, over `corpus/knowledge/`: `grep -rl -i "lexicon ceiling" corpus/knowledge/ | wc -l` → **0**; `grep -rl -i "register ceiling" corpus/knowledge/ | wc -l` → **0**; `grep -rl -i "derivational ceiling" corpus/knowledge/ | wc -l` → **0**; `grep -rl -i "operation-constrained" corpus/knowledge/ | wc -l` → **0**; `grep -rl -i "which semantic fields" corpus/knowledge/ | wc -l` → **0**. The word `ceiling` occurs in 14 files but never for a lexicon: in `syntax-typology.md`, `color-terminology.md`, `language-contact.md` it means an upper bound on a grammatical or lexical **category count**, not a semantic-field limit. The nearest neighbours are extended here, never restated: this entry adds the **ceiling as a measured object** (the domain of a derivation operation, over a syllable template) which the framework entries supply the vocabulary for and leave unbuilt.
- sources:
  - KTD-RLC-S-0001 — `reports/round-27/law/design.md` §3.2 and `reports/round-27/law/review.md` §4 (`RL-3`): the round-27 statement of the ceiling — the `mark-axis plain words: 27 reverse-legal: 18 reverse-ILLEGAL: 9` table, the five named legal/institutional abstractions (`L-15 wer`, `L-30 gis`, `L-44 wad`, `L-45 tikmes`, `L-51 gul`), and the eight landed register forms as material-presence bases. **Cited by revision, not by digest** (the file moved inside round 27 while the entry that cites it was being written; `reports/round-27/law/design.md` went `00f201b3…` → `9d5c1dd7…` during authoring, per `reports/round-27/entry/C43.md` §3). Read at lane HEAD `69cecbc`, 2026-10-18.
  - KTD-RLC-S-0002 — `reports/round-28/ceiling/measure-ceiling.py` (seat R28-C41..C46, this round) and its reading: the instrument that re-derives the ceiling from the delivered packet and gate, reproduces the filed count with a reconstructed pre-fix reader, and tests the mechanism (`reverse is legal <=> the base-initial consonant is a licensed coda`, 27/27). Command: `python3 reports/round-28/ceiling/measure-ceiling.py` (10/10 controls via `--selftest`).
  - KTD-RLC-S-0003 — `examples/culture-d4/components/02-phonology.yml` (`:61-75` the 14-consonant inventory, `:82` the template `(C)V(V)(C)`, `:92` `onset_clusters: false`, `:119` the eight codas): the phonology the ceiling is arithmetic over. **The NON-CANON drill.** Read at lane HEAD `69cecbc`, 2026-10-18.
  - KTD-RLC-S-0004 — `corpus/knowledge/linguistics/register-strata-attestation.md` §6 and §13 (the round-28 amendment section, added this round): the entry that carries the register law and now the ceiling as a design constraint, with the superseded and corrected readings tabulated. This entry is the general statement; that entry is the law-specific one.
  - KTD-RLC-S-0005 — `reports/round-26/register/rules.md` §2–§3 and `reports/round-26/register/review.md` §3: the operation rule (`axis mark → reverse; axis fire → lengthen`), the 13-of-54 unusable-form measurement, and the round-26 pricing of an escape hatch as "a rule change requiring a recorded amendment". The precedent for the third disposition (accept and record).
  - R. M. W. Dixon (1972), *The Dyirbal Language of North Queensland*, Cambridge University Press, esp. the **jalnguy** ("mother-in-law language") material at pp. 32–34, 292–296, 304–306; and Dixon (1980), *The Languages of Australia*, CUP. Jalnguy is a complete replacement lexicon used in the presence of taboo relatives, with the **same phonology and grammar** as everyday Guwal (Dixon 1972) and a **many-to-one** relation from everyday vocabulary into the avoidance lexicon. Framework status: **mainstream**, the standard reference for avoidance registers. Calibration: Dixon's later work (2020, *Dyirbal: A Language of Australia*, and the LINGUIST List review at `https://linguistlist.org/issues/32/1859/`) reframes jalnguy use as marking avoidance between cross-cousins in initiation contexts, not only in-law address; the entry uses jalnguy for the *structural* fact (grammar kept, lexicon swapped, correspondence many-to-one) and does not rest any claim on the social trigger. Already integrated in this partition at `corpus/knowledge/linguistics/sociolinguistics-registers.md:91` and `corpus/knowledge/linguistics/semantic-fields-lexicon-building.md:56`; cited here for the **substitution type**, which is the opposite of a derivation operation: jalnguy does not derive from Guwal at all.
  - M. A. K. Halliday (1976), "Anti-languages", *American Anthropologist* 78(3): 570–584; Halliday (1978), *Language as Social Semiotic*, Edward Arnold. The anti-language construct: an "anti-society" generates a variety by **relexicalization** — substituting new vocabulary for old — while **preserving the parent grammar**, with **overlexicalization** clustering around the group's central concerns. Framework status: **mainstream** in systemic functional linguistics and widely cited; calibration: Halliday's anti-language is a socially situated theoretical category, and `corpus/knowledge/synthesis/dialect-faction-map-workflow.md:122` records the caution that it is **not** a synonym for all slang or criminal speech. Already integrated at `corpus/knowledge/linguistics/sociolinguistics-registers.md:84` and `corpus/knowledge/linguistics/linguistic-anthropology.md:115`. What this entry takes from it: relexicalization is a **substitution** operation (the lexicon changes, the grammar does not), and Halliday's own list of mechanisms — "metaphor, metathesis, syllable addition and transposition, lexical borrowing, compounding and suffixation" — is precisely a list of operations with **different domains**, which is the entry's subject.
  - Megan Gotowski (2019), "La règle du jeu: Verlan as an example of anti-faithfulness", *Linguistica Atlantica* 38, https://journals.lib.unb.ca/index.php/la/article/download/29638/1882524823/1882525105 (accessed 2026-10-18). The primary source for **verlan's constrained inversion**: monosyllables invert segments, multisyllables invert syllables, and of the six logically possible three-syllable orders only **231, 321 and 312** are attested — 132 and 213 are never found. Gotowski's OT account (LOOP + MIRROR, after Raimy 1999; Alderete 2001 on anti-faithfulness) explains the constraint: the loop may start at a new point **or** reverse the successor relations, but **not both**. Framework status: **mainstream** phonology, a specific OT analysis of a well-documented language game; calibration: the analysis is one account of the constraint (competing prosodic-template and CV-skeleton accounts exist — Plénat 1995; Weinberger & Lefkowitz 1992), and the paper itself says written records of an informal game are not exhaustive. What this entry takes from it: **a reversal operation has a formally statable, non-obvious domain** — not every word can be verlan'd into every order, and the constraint is phonological, not stylistic.
  - Mark Aronoff (1976), *Word Formation in Generative Grammar*, MIT Press — **blocking**: "the nonoccurrence of one form due to the simple existence of another" (p. 43), the principle behind the nonapplication of otherwise productive derivational affixes (`glory` blocks `*gloriosity`; `went` blocks `*goed`). Framework status: **mainstream** morphology, the origin of blocking as a technical term. Calibration: Aronoff's blocking is a **lexical** constraint (a listed form pre-empts a rule-derived one); this entry's ceiling is **phonological** (a form the operation cannot produce at all) — the two are different mechanisms and are kept apart in §5, because conflating them produces a wrong diagnosis ("just coin it and the gap closes").
  - Laurie Bauer (1983), *English Word Formation*, CUP; Bauer (2001), *Morphological Productivity*, CUP. Productivity as **gradient**, not binary: an affix may be fully productive, semi-productive, or unproductive, and the ceiling on what a rule yields is measurable as the ratio of attested to possible forms. Framework status: **mainstream**; calibration: productivity judgements depend on the corpus measured, so a productivity figure is a reading of a corpus, not a property of the rule alone. Used here for the *shape* of the claim (measure the domain, do not assume totality), which is why the D4 operation rule is stated as "total over the two axis values and **not total in effect**".
  - William Labov (1972), *Sociolinguistic Patterns*, University of Pennsylvania Press; Judith T. Irvine & Susan Gal (2000), "Language ideology and linguistic differentiation", in Kroskrity (ed.), *Regimes of Language*, School of American Research Press — the register-formation side (a variety becomes readable as a register through metadiscourse). Framework status: **mainstream**. Cited by path through `corpus/knowledge/linguistics/sociolinguistics-registers.md`; not re-fetched this pass. Used only for the point that a register's *readability* and its *coverage* are different properties: a register can be unmistakably institutional and still unable to name its own institution.
- couples: linguistics — `corpus/knowledge/linguistics/register-strata-attestation.md` (the register law this entry measures the vocabulary ceiling of; its §13 is the case), `corpus/knowledge/linguistics/sociolinguistics-registers.md` (register strata, avoidance registers, anti-languages), `corpus/knowledge/linguistics/semantic-fields-lexicon-building.md` (field engineering — which fields exist to be spelled), `corpus/knowledge/linguistics/morphological-typology.md` (the derivation operations a language supplies: affixation, reduplication, ablaut, root-and-pattern — each with a different domain), `corpus/knowledge/linguistics/phonetics-phonology.md` (the syllable template the domain is computed over), `corpus/knowledge/linguistics/linguistic-anthropology.md` (special languages, ritual and avoidance registers), `corpus/knowledge/linguistics/naming-systems.md` (name magic and taboo strata as fields a register must cover), `corpus/knowledge/linguistics/writing-systems.md` (the script half of an attestation convention); culture-material — `corpus/knowledge/culture-material/trade-economy-lexicon.md` (the obligation and measure vocabulary a trade institution needs sayable); synthesis — `corpus/knowledge/synthesis/era-language-staging.md` (a form's era window, which bounds which bases exist to derive from), `corpus/knowledge/synthesis/worldbible-integration-contract.md` (the handoff a ceiling must travel with); verification — `corpus/knowledge/verification/lexicon-coverage-audit.md` (the instrument family that would measure coverage); artifacts — `reports/round-26/register/`, `reports/round-27/law/`, `reports/round-28/ceiling/`, `examples/culture-d4/`; siblings — lore-shokunin owns canon and world-bible consistency; this entry is design method and never canon.
- source: the measured authority is `reports/round-28/ceiling/measure-ceiling.py` run at lane HEAD `69cecbc` on 2026-10-18 against `examples/culture-d4/packet.d4.yml` (`543d68a8…`) and `tools/gates/argot-derivation-gate.py` (`b5406bcd…`); the design authority is `reports/round-26/register/{design,rules,review}.md` and `reports/round-27/law/{design,rules,review}.md`; the external framework is Dixon (1972/1980), Halliday (1976/1978), Gotowski (2019), Aronoff (1976), Bauer (1983/2001), Labov (1972), Irvine & Gal (2000). The measurement procedure is this lane's house method; the frameworks are cited, never blended into a claim about any real community.
- verified-at: 2026-10-18 — written this round against lane HEAD `69cecbc` (`reports/round-28/claims.json` baseline `6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`). Measured at write time with `export TMPDIR=$PWD/.scratch`. Readings: `python3 -B reports/round-28/ceiling/measure-ceiling.py` → `mark-axis plain words = 27`, delivered gate `b5406bcd…` **legal=19 illegal=8**, pre-fix reader **legal=18 illegal=9** (the filed round-27 count), delta `{L-45}`; `--selftest` → **10/10 checks passed**, exit 0; `--json` receipt written to `.scratch/r28-ceiling.json`. Mechanism: `reverse is legal <=> the base-initial consonant is a licensed coda` → **True (27/27)**, onsets 14 / codas 8 / never-coda `b g h j p w`. The delivered packet and gate digests are re-printed by every run, so a reader on a later tree can tell whether the numbers above still describe the bytes. The round-27 filing of `RL-3` was read in `reports/round-27/law/{design,rules,review}.md`; the pre-fix reader is a labelled reconstruction (the pre-fix gate declares no legality predicate), and it is labelled as one wherever it is used.
- recheck: before quoting any coverage figure for a register built by a mechanical operation; whenever `examples/culture-d4/components/02-phonology.yml` changes (the coda set is what the ceiling is computed from); whenever `examples/culture-d4/components/04-lexicon.yml` or `packet.d4.yml` changes (the base list the ceiling is measured over); whenever a round changes `tools/gates/argot-derivation-gate.py`'s `syllabify`/`is_legal_syllable` (the reader that decides legality — this entry's own correction exists because that reader moved); and whenever an external framework above is revised (corrections are new sections or a new entry, never rewrites of this one).

## 1. The ceiling, stated as one sentence

**A register's derivation operation constrains which semantic fields it can natively spell.**

A marked register is usually not a hand-built lexicon. It is the ordinary lexicon
run through an **operation** — reversed, truncated, lengthened, reduplicated,
substituted. An operation is a function, and every function has a **domain**: the
set of inputs it can turn into a legal output. The ceiling is the gap between the
fields the register's *institution* needs to talk about and the fields the
operation's domain reaches.

That gap is the design hazard this entry exists to catch, because it is
**invisible in the register's own success**. A reversal register looks like it
works: the words it does produce are legal, and the register reads as marked and
institutional. What fails is one level up — the law written over the register
tries to name an obligation, and the operation cannot produce the word.

## 2. Why it is a ceiling and not a gap that more coinage closes

Three distinct mechanisms get confused under the word "missing word", and only the
first is the subject here:

| mechanism | what is missing | how it closes | source |
|---|---|---|---|
| **operation ceiling** | the operation cannot produce a legal form for that input at all | only by changing the operation or the base list — never by coining more | this entry, §3 |
| **blocking** | a listed form pre-empts the rule-derived one (`glory` blocks `*gloriosity`) | by the listed form going away | Aronoff (1976) |
| **lexical accident** | nobody has needed the word yet | by someone coining it | Bauer (1983) |

The distinction matters because the remedies are incompatible. A designer who
diagnoses an **operation ceiling** as a **lexical accident** will coin forms that
the register's own gate refuses — or, worse, will adjust the gate until they pass,
which is how a legality check becomes a rubber stamp. The D4 drill hit exactly
this shape: the operation rule is "total over the two delivered axis values and is
**not total in effect**" (`reports/round-26/register/rules.md` §2), and 13 of 54
delivered lexicon records yield an unusable form.

## 3. Measuring the ceiling: the procedure

Five steps. Each produces a number, not an opinion.

1. **Write the operation's domain as a predicate over the input.** For a reversal
   over a syllable template, this is a statement about one segment position
   (§4.1). For truncation it is a minimum-length statement. For lengthening it is
   a statement about which segment may be lengthened.
2. **Take the base list** the register will actually draw on — the delivered
   lexicon, not an imagined one.
3. **Classify the base list by the fields the register must cover.** Name the
   members; do not keyword-guess. In the D4 case the five legal/institutional
   abstractions are named by ID (`L-15`, `L-30`, `L-44`, `L-45`, `L-51`) precisely
   so that the class is a list and not a vibe.
4. **Run the predicate and cross-tabulate.** The output is a table of
   `class × operation-legality`. This is the measurement, and it is cheap.
5. **Compare against the law's vocabulary.** Every act, office, obligation and
   consequence the law names must be spellable by the operation, or the law must
   be rewritten to say it another way. The comparison is the ceiling.

The check is worth running **before** the law is written, because the alternative
is a law that reads well and names words the register cannot produce.

## 4. The measurement, worked: the D4 stamp register

### 4.1 Worked case: the D4 stamp register, measured

The drill's register (`examples/culture-d4/`) is the ordinary lexicon carried into
the marked register by the operation its own axis selects — `mark → reverse`,
`fire → lengthen` (`reports/round-26/register/rules.md` §2). The template is
`(C)V(V)(C)` with `onset_clusters: false` (`02-phonology.yml:82,92`).

**The predicate.** The inventory has **14 onset consonants** but only **8 licensed
codas** (`:61-75`, `:119`). A reversal moves the base-initial consonant to final
position, where it must be a coda. So:

```
reverse is legal  <=>  the base's initial consonant is a licensed coda
```

Measured over the 27 delivered mark-axis plain words: **27/27, no
counterexample**. The six consonants that are onsets but never codas
(`b g h j p w`) are exactly the refusals. The ceiling is arithmetic over the
syllable template — it is not a property of the word list at all, which is why
adding coinages cannot move it.

**The cross-tab, at lane HEAD `69cecbc` (2026-10-18):**

| class | legal | illegal | members (illegal) |
|---|---|---|---|
| material / other | 18 | 4 | `L-08 wak→kaw`, `L-17 bek→keb`, `L-24 wat→taw`, `L-26 gim→mig` |
| **legal / institutional abstraction** | **1** | **4** | `L-15 wer→rew` (right-of-way), `L-30 gis→sig` (**oath**), `L-44 wad→daw` (price), `L-51 gul→lug` (weight) |

Population: 27 mark-axis plain words; **19 legal / 8 illegal**. The one abstract
member that survives is `L-45 tikmes` → `semkit`, and only because it is a
**compound** (`STACK-COMPOUND` over `tik` + `mes`) whose reversal happens to land
on a licensed coda (`sem.kit`, both syllables legal) — not because abstractions
are spellable in general.

**The eight landed register forms are material-presence bases, 8 of 8:**
`tik` (mark), `mol` (mold), `tum` (breath), `nes` (water), `hum` (smoke), `mes`
(metal), `rek` (ore), `sam` (charcoal). Zero abstractions. The register, as
landed, is the vocabulary of *things at the weigh-stone*, not of *obligations*.

**The sharp case, and why it matters.** `L-30 gis` — "oath, sworn word; the mark
that attests it" — is `axis: mark`, so the rule sends it to `reverse`, and `sig`
is not a legal D4 syllable. **The register cannot say the word "oath" in itself.**
An attestation register whose whole subject is binding speech cannot name the
binding act in its own marked variety.

### 4.2 The correction this entry carries

Round 27 filed the cross-tab as **18 legal / 9 illegal** with the abstract class
**0 legal / 5 illegal** (`reports/round-27/law/design.md` §3.2). Re-measured at
lane HEAD `69cecbc` with the delivered gate, the count is **19 legal / 8 illegal**
and the abstract class is **1 legal / 4 illegal**.

The filed 18/9 is the **pre-fix reader's** reading. It reproduces exactly with the
syllabification that never splits a consonant run — the scan round 27's D seat
replaced mid-round (`5b5abe78…` → `d7a3ad1a…` → `b5406bcd…`, selftest 21/21 →
27/27; `reports/round-27/law/impl-3.md` §3.2). The single row that moves is
`L-45 tikmes`: the pre-fix scan read `semkit` as `se.mki.t` (`mki` and the bare
`t` are not syllables), the delivered gate reads it `sem.kit`.

**The correction does not weaken the ceiling.** Four of the five abstractions
still refuse `reverse`, including the oath; the one that does not is a compound
that got lucky with its final consonant. But the correction is the entry's own
best evidence for its own rule: **the ceiling is only as trustworthy as the
legality reader it is measured with**, and a reader that mis-splits syllables
moves the count. `reports/round-28/ceiling/measure-ceiling.py` prints both
readers, both digests, and the delta, so a reader can see which one produced a
number before quoting it.

## 5. The three dispositions

There is no fourth. Pick one **before** writing the law.

| # | disposition | what it costs | when it is right |
|---|---|---|---|
| **A** | **Hand-pick the base list** — build the register from chosen bases rather than by a total operation | the register loses its mechanical derivability; every form is a design decision and must be justified individually | when the law's vocabulary is small and known, and the register's institution is the design's centre |
| **B** | **Choose an operation whose domain covers the needed fields** | you must measure the domain first (§3); a different operation may cost other properties (length, recoverability, markedness) | when the law's vocabulary is open-ended or will grow |
| **C** | **Accept the ceiling and write the law inside it** — state each act in words the register can carry, and put the un-spellable part on another institution's side | the law is weaker than it reads; the un-spellable term must be carried by a different channel, and that must be declared | when the operation is load-bearing (it *is* the register's identity) and the ceiling is narrow |

The D4 drill took **C**, and declared the price as two named limits: the law
cannot licence an act whose vocabulary the register cannot spell (`LL-1`), and all
eight landed forms are material-presence bases (`LL-2`). The oath is stated in
terms the register *can* carry (`tuum`, the breath sworn by) and the consequence
is put on the council's roll — which is written in the league hand, not in the
register (`reports/round-27/law/design.md` §3.2). The repair — an escape hatch in
the operation rule so abstractions can enter — was priced in round 26 as "a rule
change requiring a recorded amendment" and **not taken**; that refusal is a
recorded decision, not an oversight.

**What each disposition forbids.** A forbids claiming the register is
mechanically derived. B forbids quoting a domain you did not measure. C forbids
presenting the law as complete — a law written inside a ceiling must say where
the ceiling is, or the next reader will take the gap for a bug.

## 6. The real-world analogues, and what they do and do not show

| case | operation | constraint measured | what it supports | limit |
|---|---|---|---|---|
| **verlan** (French) | syllable/segment inversion | of six three-syllable orders only **231, 321, 312** occur; **132** and **213** are unattested (Gotowski 2019) | a reversal operation has a formally statable, non-obvious domain | one informal variety; written records are not exhaustive; competing OT analyses exist |
| **jalnguy** (Dyirbal) | **substitution**, not derivation | many-to-one from everyday Guwal into the avoidance lexicon; grammar and phonology kept (Dixon 1972) | a register can swap its whole lexicon without an operation — the ceiling is a property of *operations*, not of registers as such | the correspondence is many-to-one, so it *avoids* the ceiling rather than solving it; the social trigger is contested in later work (Dixon 2020) |
| **anti-languages** (Halliday 1976) | relexicalization + overlexicalization | the parent grammar is preserved; vocabulary is replaced, clustered on the group's obsessions | the *fields* a register covers are a design choice with a social cause | a theoretical category, not a synonym for slang (`dialect-faction-map-workflow.md:122`); no domain arithmetic is offered |
| **language games** (Tagalog *tadbaliks*, *baliktád*; Saramaccan; Zande; Chaga) | syllable movement, segment reversal, copying | different games in the same language allow different orders, and a game may allow only one (Gotowski 2019, §4) | the operation is a **design parameter**: choosing it chooses the domain | described for a handful of languages; the mechanism generalises further than the evidence |

**The transferable claim is the procedure, not the numbers.** No real-world case
above supplies a cross-tab of `semantic class × operation-legality` — that is this
entry's method. What the real cases supply is the warrant that the *shape* is real:
operations have domains, the domains are phonological, and a register built by an
operation inherits them.

## 7. Design procedure (build order)

1. **List the fields the register's institution must name** — the acts, offices,
   obligations, measures and consequences its law will use. Write the list before
   choosing anything else.
2. **Choose the operation** (§5, disposition B) or the base list (§5, A). If the
   register's identity is the operation, that choice is already made.
3. **Write the operation's domain predicate** (§3 step 1). For a reversal over
   `(C)V(V)(C)`, this is one consonant position: the base-initial segment must be
   a licensed coda.
4. **Measure**: run the predicate over the delivered base list, cross-tabulated by
   field class (§4.1). Keep the named members of each class in the record.
5. **Compare with the law's vocabulary** (§3 step 5). Every term the law names
   must be spellable, or the law changes.
6. **Pick the disposition and record its price** (§5). If the answer is C, name
   the ceiling and name where the un-spellable term is carried instead.
7. **Re-measure when the reader changes.** The legality predicate lives in an
   instrument; when that instrument moves, the count moves (§4.2). Re-run and
   record the new reading as a new row, never as a silent edit.

## 8. Decision record — the rules this entry adopts

| ID | decision | evidence | consequence if violated | recheck trigger |
|---|---|---|---|---|
| **RLC-1** | a register built by a mechanical operation must have its **domain measured** before its law is written | §3–§4; measured `19 legal / 8 illegal` and `4 of 5` abstractions refusing `reverse` | a law that names words the register cannot produce | any register built by an operation |
| **RLC-2** | the ceiling is stated as a **predicate over the input**, not as a word list | §4.1: `reverse is legal <=> the base-initial consonant is a coda`, 27/27 | a ceiling that moves when the lexicon grows, and so cannot be designed around | any ceiling claim |
| **RLC-3** | an operation ceiling, **blocking** (Aronoff 1976) and a **lexical accident** (Bauer 1983) are different diagnoses with incompatible remedies | §2 | coining words to fix a phonological ceiling, or editing the gate until they pass | any "the register just needs more words" reading |
| **RLC-4** | a legality count is only as good as the **reader** that produced it; a moved reader moves the count | §4.2: filed 18/9 is the pre-fix reader; delivered is 19/8; delta `L-45` | a superseded count quoted as current, or a correction read as a weakening | any change to `syllabify`/`is_legal_syllable` |
| **RLC-5** | the three dispositions (hand-pick / choose the operation / accept and declare) are **exhaustive**, and each forbids one claim | §5 | presenting a ceiling-limited law as complete, or claiming a mechanical derivation that was hand-picked | every register design |
| **RLC-6** | if the ceiling is accepted, its **price is declared with the law**, including where the un-spellable term is carried instead | §5 disposition C; the D4 `LL-1`/`LL-2` declaration, oath stated via `tuum`, consequence on the council's roll | a gap the next reader takes for a bug, or a law that reads stronger than it is | every law row that names an abstraction |
| **RLC-7** | a register's **readability** and its **coverage** are different properties; a register can be unmistakably institutional and unable to name its own institution | §1; the D4 register is marked, legible and material-only | grading a register by how marked it reads, which the ceiling never shows up in | any register-quality claim |

- **Append-only discipline.** A later round that re-measures the ceiling adds a
  new section or a new entry linked from `recheck`; it never rewrites a filed
  reading. The round-27 numbers stay as the round-27 reading at their stamp.

## 9. Calibration: what is mainstream, what is contested, what is this lane's

- **Mainstream.** Dixon's jalnguy material (avoidance registers exist, grammar kept,
  lexicon swapped, correspondence many-to-one); Halliday's anti-language construct
  (relexicalization with grammar preserved); Aronoff's blocking; Bauer's gradient
  productivity; the existence of constrained language games with statable domains
  (Gotowski 2019 and the literature it reviews).
- **Contested or moving.** The *account* of verlan's constraint (LOOP+MIRROR is one
  OT analysis among several — Plénat's prosodic templates, Weinberger &
  Lefkowitz's CV skeletons); jalnguy's **social trigger** (Dixon 2020 and the
  LINGUIST List review of it reframe it toward cross-cousin avoidance in
  initiation contexts, away from in-law address); whether anti-language is a
  category or a metaphor for marked in-group varieties
  (`dialect-faction-map-workflow.md:122`).
- **This lane's own, and NON-CANON.** The measurement procedure (§3), the
  `class × legality` cross-tab, the predicate form (§4.1), the three dispositions
  (§5), and every number taken over `examples/culture-d4/`. The D4 drill is an
  engineering fixture: its furnace-league, stamp-house and four acts are not canon
  for any world, and no real language's resemblance to its forms has been screened.
- **Not claimed.** No claim that any real register's ceiling has been measured this
  way; no claim that the D4 cross-tab predicts any real language; no claim that
  four-of-five is a typical ratio — it is this drill's ratio.

## 10. Limits of this entry

- **One measured case.** The procedure is stated generally; the only full
  application is the D4 stamp register. A reader who needs a lengthening or
  truncation ceiling must run §3 themselves — this entry gives the shape, not the
  number.
- **The mechanism is template-specific.** `reverse is legal iff the base-initial
  consonant is a coda` holds for `(C)V(V)(C)` with a single licensed coda and no
  onset clusters. A language with onset clusters or long codas has a different
  predicate; the **check** transfers, the consonant list does not.
- **The count is a reading of a reader.** §4.2 is the demonstration: the same
  lexicon yields 18/9 or 19/8 depending on the syllabifier. Every number here names
  its packet digest, gate digest and date, and must be re-taken before quoting.
- **No real-language resemblance screening.** The D4 forms have not been screened
  against any natural language; nothing here says they resemble one.
- **The dispositions are exhaustive as dispositions, not as designs.** A designer
  may combine them (hand-pick the law's vocabulary *and* run the operation for the
  rest), but each combination is still a choice among the three, and each still
  owes its price.
- **Thin knowledge, stated.** This entry contains no theory of register genesis, no
  position on the productivity debate beyond the measurement discipline, and no
  claim that a ceiling is a defect. A ceiling that is declared and designed around
  is a design; a ceiling that is discovered later is a bug.

## 11. Canon boundary and handoff

- Nothing here decides what is true in any world. Which register exists, which
  fields it must cover and which operation builds it are **systems this lane
  generates**; whether they are canon is lore-shokunin's decision (`PROVINCE.md`;
  `AGENTS.md`).
- **Handoff shape.** Ship the register with its **operation and domain predicate**,
  its **base list**, the **cross-tab** (`class × legality`, with named members),
  and the **declared ceiling** if disposition C was taken — including where each
  un-spellable term is carried instead. Never ship an operation-constrained
  register without its domain measurement, and never ship a law written inside a
  ceiling without the ceiling named.
- **Contested scope → report, never absorb.** If a receiving lane expects a green
  register gate to certify that the law is enforceable, that is reported to the
  integrator: a legality leg over forms does not check a law over acts, and the
  decision is not this lane's to make unilaterally.

## 12. Errata (round 33): the absence sweeps in the head block, re-measured

**Append-only.** Nothing above is rewritten. The `- gap filled:` cell states five
absence sweeps, each returning 0 over `corpus/knowledge/` at 2026-10-18. Re-run at
lane HEAD `139e3b6` on 2026-10-19, **all five now return ≥ 1**:

| pattern | hits at HEAD | files | class |
|---|---|---|---|
| `lexicon ceiling` | 2 | `register-strata-attestation.md` §13; this entry | sibling landing (r28 wave) |
| `register ceiling` | 1 | this entry | self-match after landing |
| `derivational ceiling` | 1 | this entry | self-match after landing |
| `operation-constrained` | 1 | this entry | self-match after landing |
| `which semantic fields` | 3 | `sound-symbolism.md:106`; `register-strata-attestation.md` §13; this entry | **one pre-existing hit** |

The last row is the finding. `sound-symbolism.md:106` ("assign **which semantic
fields** carry ideophones") existed at the round-28 baseline commit `6c0ac448`
(that file last moved in round 10), so that sweep was **false when written** —
reported as `X63-F2`, an authoring defect, in
`reports/round-28/audit/x63-entry-source-resolvability.md` §3.4 and routed, never
repaired. The other four rows are the wave's own landings (this entry and the
strata §13 amendment), the sibling-landing class of the same audit.

**Corrected reading, for any future consumer of the head block:** of the five
patterns, the phrase `which semantic fields` occurs once in the pre-existing
corpus, in `sound-symbolism.md`, in the ideophone sense — a different sense from
this entry's ceiling sense. The claim that survives is the narrower one: no entry
before this one measured what an operation-constrained register cannot say.
