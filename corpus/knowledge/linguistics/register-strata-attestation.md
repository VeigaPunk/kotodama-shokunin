# Register strata for attestation speech — the law that makes a spoken word bind

- topic: How to design the **attestation register** — the marked speech a culture uses when a spoken word is being made to bind, as against its unmarked everyday speech — and, separately, the **register law** that governs it: which acts may be spoken in-register, by whom, with what illocutionary force, and with what record consequence. Supplies the speech-act framework (Austin's felicity conditions and misfires, Searle's five classes and the declaration/status-function machinery, Searle's constitutive rules and deontic powers), the anthropological spine for ritually binding speech (Tambiah on the magical power of words; Rappaport on invariance as the engine of liturgical authority), the social conditions that authorise a speaker (Bourdieu's authorized language and delegation; Irvine's honorific ideology), the documentary-institution side that makes an oral act a record (Clanchy; Clanchy's "from memory to written record" transition), a register-law design procedure with worked rows, the boundary against costume/rank rules, and the calibration shelf for what is contested. Reference knowledge and method only; canon decisions belong to lore-shokunin.
- gap filled: the partition carries the pragmatic frameworks — Austin/Searle speech acts and the five-class table in `corpus/knowledge/linguistics/semantics-pragmatics.md:88-98`, politeness and honorific grammar in `corpus/knowledge/linguistics/politeness-taboo-euphemism.md`, register/diglossia strata in `corpus/knowledge/linguistics/sociolinguistics-registers.md`, ritual performative language in `corpus/knowledge/myth-symbol/ritual-liminality.md:112` — but **no entry covers the attestation register as a design object, and none states the register law** (admissibility, speaker, force, record consequence). Absence sweep 2026-10-18 from the lane root, over `corpus/knowledge/` minus this entry: `grep -rl -i "illocutionary" corpus/knowledge/ | wc -l` → **0**; `grep -rl -i "constitutive rule" corpus/knowledge/ | wc -l` → **0**; `grep -rl -i "deontic" corpus/knowledge/ | wc -l` → **0**; `grep -rl -i "attestation register\|attestation speech" corpus/knowledge/ | wc -l` → **0**; `grep -rl -i "register law\|register-law" corpus/knowledge/ | wc -l` → **0**. The word `felicity` occurs twice, both as a one-clause aside in a larger framework (`semantics-pragmatics.md:88`; `ritual-liminality.md:112`) and never as a designed rule set. The nearest neighbours are extended here, never restated: this entry adds the **law** (who may speak, with what force, with what consequence) that the frameworks above supply the vocabulary for and leave unbuilt.
- sources:
  - KTD-RSA-S-0001 — `reports/round-26/register/design.md` (sha256 `27d23fa67d0bb920d1841d25c82b09919419ef58ef3b2f75494d950f3b5bb55a`): the register's identity (`stamp`, the attestation register), the axis→operation rule, the era scoping, the owners. Read at lane HEAD `b95fca1`, 2026-10-18.
  - KTD-RSA-S-0002 — `reports/round-26/register/forms.md` (sha256 `06635a1c123e0908e1bf51796c04940caac7d4b29ddaa47169eaaa1a1b7fc71b`) §5: the five law rows `RGL-01..RGL-05` as design statements — the row set this entry generalises into a law component.
  - KTD-RSA-S-0003 — `reports/round-26/register/rules.md` (sha256 `535cf7a981c5cf7d8c824454cb46319745bf096342a203add998a34842b026ef`) §2–§5: `REGISTER-OP-01` (the operation-selection rule) and `REGISTER-ERA-01` (the era rule), both stated and both unowned.
  - KTD-RSA-S-0004 — `reports/round-26/register/review.md` (sha256 `0082f08b62986ab2091a07acee464888fd68fa5312f19ef1b3817111a05f96e1`) §6.3: the named finding that the delivered tree had **no component owning a register law** (`RD-5c`), and §5 the syllabify disagreement (`RD-4`, `RL-3`).
  - KTD-RSA-S-0005 — `reports/round-27/law/design.md` (seat R27-D01) §3–§4: the four acts (charge, attested oath, naming of a lot, guest's charge) with speaker/force/consequence, and the boundary that separates the register law from the delivered costume rank rules. §3.2 is the measured constraint this entry's §6 adopts. **Cited by revision, not by digest:** this file was still being written while this entry was authored (`sha256 00f201b3…` at 19:19Z, `9d5c1dd7…` at 19:20:37Z — measured twice, moving), so no digest is pinned here and the round-27 X63 audit's `pin-drift` rows against it are expected until the law seats close.
  - KTD-RSA-S-0006 — `reports/round-27/law/rules.md` (seat R27-D02) §1: the six-rule registry `RLAW-01..06` with the replayable/unowned column — the measured state of the law's enforceability. **Cited by revision, not by digest** (same reason as S-0005: `9b0d1415…` at 19:19Z, `c6935957…` at 19:20:12Z).
  - KTD-RSA-S-0007 — `reports/round-27/audit/x59-register-law-negatives.py` (seat R27-X59), law `L6`, and its receipt `reports/round-27/gate-tests/receipt.json`: the independent instrument emits `FINDING L6-HOLD` on the delivered packet, naming the missing law columns rather than reporting a vague gap. Two readings are quoted in §4.1 — `law_rows=0 register_rows=4 records=62` (before the law landed, packet `dd25077b…`), then `law_rows=0 speech_act_rows=0 register_rows=4 records=62` (after the five `RGL` rows landed in the separate `register_law:` key, packet `c5441e3d…`). **Cited by revision, not by digest** (the instrument's own bytes moved inside this round: `f5f5d46a…` → `7e3b3559…`); the earlier counters are the ones in the filed `receipt.json`, which is the stable artifact.
  - KTD-RSA-S-0008 — `reports/round-27/scribe/x54-syllabify-spotcheck.py` (seat R27-X54): the third witness that adjudicates the round-26 syllabify dispute — the packet's own author-declared `syllables:` field on the 8 name records agrees **8/8** with the design's maximal-onset algorithm and **0/8** with the gate's. **Cited by revision, not by digest** (the file moved inside this round: `1bfa9e3a…` → `ee370f78…`).
  - KTD-RSA-S-0009 — `examples/culture-d4/components/13-register-law.yml` (seat R27-D05..D12; the new component that landed mid-round) and its merged packet block `register_law:` in `examples/culture-d4/packet.d4.yml` (line 2617; rows at 2622/2634/2646/2658/2670). The five `RGL-01..05` law rows with `kind`/`act`/`holder`/`consequence`. The packet's `registers:` block still carries only the four identity rows `QREG-01..04` (line 1300ff). **Cited by revision, not by digest:** the packet moved twice inside this round (`dd25077b…` → `c5441e3d…`), and pinning a churning file is the defect `RSA-10` names. The NON-CANON drill packet this entry's worked example reads; not canon, not a real culture. The frozen round-26 copy at `tools/gates/frozen/round-26/post-register/inputs/examples/culture-d4/packet.d4.yml` still carries the pre-landing bytes `dd25077b…`.
  - KTD-RSA-S-0010 — `corpus/knowledge/linguistics/semantics-pragmatics.md` §5 (`:88-98`) and `corpus/knowledge/linguistics/sociolinguistics-registers.md` §4; `corpus/knowledge/myth-symbol/ritual-liminality.md:112`; `corpus/knowledge/culture-material/trade-economy-lexicon.md:119-124`. The neighbouring entries this one extends: they supply the speech-act vocabulary, the register strata, the ritual-performative frame and the documentary-instrument frame respectively, and none states the law.
  - John L. Austin (1962), *How to Do Things with Words*, Clarendon Press (the William James Lectures, 1955). Performatives; the locutionary/illocutionary/perlocutionary distinction; **felicity conditions** and the two failure classes — **misfires** (the act is not performed at all: I lack the authority, or the addressee withholds uptake) and **abuses** (the act is performed but insincere). Framework status: **mainstream**, the origin of the field. Read through the Stanford Encyclopedia entry [Speech Acts](https://plato.stanford.edu/entries/speech-acts/) §1–§2 (accessed 2026-10-18), which states the authority and uptake conditions and the misfire/abuse split at §"Felicity"; the book itself was not re-read this pass, so the locators below are the encyclopedia's, not the book's pagination.
  - John R. Searle (1976), "A Classification of Illocutionary Acts", *Language in Society* 5(1): 1–23 (the five classes: assertives, directives, commissives, expressives, declarations); Searle (1969), *Speech Acts: An Essay in the Philosophy of Language*, CUP; Searle (1995), *The Construction of Social Reality*, Free Press (constitutive rules of the form "X counts as Y in context C"; **deontic powers** — rights, duties, permissions — as what status-functions create); Searle (2018), "Status Functions" (the later statement of deontic powers). Framework status: **mainstream**, with the constitutive-rule account **contested in its details** — see §9. Consulted through the Stanford Encyclopedia entries [Social Institutions](https://plato.stanford.edu/entries/social-institutions/) §§"constitutive rules", "Declaration", "deontic powers" (accessed 2026-10-18), which also records Guala's and Hindriks's arguments that constitutive rules are less central than Searle holds.
  - Stanley J. Tambiah (1968), "The Magical Power of Words", *Man* n.s. 3(2): 175–208 — ritual formulae whose efficacy does not depend on comprehension or paraphrase. Framework status: **mainstream** in linguistic anthropology; the entry's ritual-language coupling. Cited by path through `corpus/knowledge/linguistics/linguistic-anthropology.md:99` and `corpus/knowledge/myth-symbol/ritual-liminality.md:112`, where it is already integrated; not re-fetched this pass.
  - Roy A. Rappaport (1999), *Ritual and Religion in the Making of Humanity*, Cambridge University Press. Chapter list verified at the Internet Archive catalogue record [ritualreligionin0000rapp](https://archive.org/details/ritualreligionin0000rapp) (accessed 2026-10-18), which lists ch. 2 "The ritual form", ch. 5 "Word and act, form and substance", ch. 6 "Time and liturgical order". Framework status: **mainstream** in ritual studies, and the standard authority for "frozen form carries the authority"; the limit is that it is an anthropological generalisation from a comparative base, not a tested universal (stated again in §9). The load-bearing claim this entry uses — that the **invariance** of liturgical form, not the speaker's will, is what makes a rite authoritative — is stated at `corpus/knowledge/myth-symbol/ritual-liminality.md:112` ("Rappaport 1999: the liturgy's very invariance is what makes it authoritative, because no individual's will can alter it"); the book's own wording was not retrieved, so the claim is attributed as the neighbouring entry states it.
  - Pierre Bourdieu (1991), *Language and Symbolic Power*, Polity Press / Harvard UP (trans. Gino Raymond & Matthew Adamson; ed. John B. Thompson). **Authorized language**, delegation, and the spokesperson: a speech act's authority is not the speaker's property but the institution's, lent to a delegate; the "linguistic market" prices ways of speaking. Framework status: **mainstream** in the sociology of language, **contested** as a general theory of linguistic exchange. Cited by path through `corpus/knowledge/linguistics/linguistic-anthropology.md:67` ("a linguistic market prices ways of speaking; linguistic capital converts to economic and political power"), where the same work is already integrated; not re-fetched this pass, and the `plato.stanford.edu/entries/bourdieu/` locator returns 404 (attempted 2026-10-18) so no encyclopedia locator is asserted.
  - Michael T. Clanchy (1979; 2nd ed. 1993), *From Memory to Written Record: England 1066–1307*, Blackwell. The transition from an oral/witness-based culture of proof to a documentary one; the seal, the chirograph and the tally as instruments that make a spoken act survive its speaker. Framework status: **mainstream** medieval social history, and the standard account of that transition. Cited by path through `corpus/knowledge/culture-material/trade-economy-lexicon.md:92,121` (the tally's stock-and-foil split; the chirograph and indenture as split-object authentication), where the work is already integrated; not re-fetched this pass.
  - Judith T. Irvine (1992), "Ideologies of honorific language", *Pragmatics* 2(3): 251–262, and Asif Agha (2007), *Language and Social Relations*, CUP — the **enregisterment** of honorific/register forms through metadiscourse, already integrated in `corpus/knowledge/linguistics/sociolinguistics-registers.md` §1 and `corpus/knowledge/linguistics/politeness-taboo-euphemism.md`. Framework status: **mainstream** in linguistic anthropology (both are the standard references for enregisterment); the limit is that enregisterment describes how a register comes to *read* as institutional, not how it becomes binding — the law is a separate object (§1). Cited by path; not re-fetched this pass.
  - William Labov (1972), *Sociolinguistic Patterns*, U Pennsylvania Press (marker/indicator/stereotype); John J. Gumperz (1982), *Discourse Strategies*, CUP (contextualisation cues and codeswitching). Framework status: **mainstream**; already integrated in `corpus/knowledge/linguistics/sociolinguistics-registers.md`; cited here only for the mechanism by which a register switch is *read* by hearers, and not relied on for any law row.
  - M. B. Parkes (1973), "The Literacy of the Laity", in Daiches & Thorlby (eds.), *The Mediaeval World*; and the general vernacular/legal-register literature behind `corpus/knowledge/linguistics/sociolinguistics-registers.md` (Tiersma 1999, *Legal Language*, U Chicago Press) — the legal register's resistance to paraphrase by design. Cited by path through that entry; not re-fetched this pass.
- couples: linguistics — `corpus/knowledge/linguistics/semantics-pragmatics.md` (the speech-act vocabulary this entry builds a law on), `corpus/knowledge/linguistics/sociolinguistics-registers.md` (register strata, diglossia, enregisterment), `corpus/knowledge/linguistics/politeness-taboo-euphemism.md` (honorific grammar, taboo and sanction — the penalty side of admissibility), `corpus/knowledge/linguistics/orality-formulaic-language.md` (frozen diction as the oral analogue of an in-register form), `corpus/knowledge/linguistics/naming-systems.md` (name magic and the naming act as a declaration), `corpus/knowledge/linguistics/writing-systems.md` (the script half of an attestation convention), `corpus/knowledge/linguistics/linguistic-anthropology.md` (ritual registers, Bourdieu's market); myth-symbol — `corpus/knowledge/myth-symbol/ritual-liminality.md` (performative ritual language, felicity codes), `corpus/knowledge/myth-symbol/divination-omen-systems.md` (licensed reader, prescription as output — the same speaker-authorisation logic); culture-material — `corpus/knowledge/culture-material/sumptuary-law-rank-display.md` (the rank/permit system the law must not be merged into), `corpus/knowledge/culture-material/trade-economy-lexicon.md` (contract vocabulary, the seal, the tally, the oath-scroll), `corpus/knowledge/culture-material/craft-artisan-lexicon.md` (guild marks and the stamp-house institution); synthesis — `corpus/knowledge/synthesis/worldbible-integration-contract.md` (the handoff the law rows ship through), `corpus/knowledge/synthesis/era-language-staging.md` (the era window an in-register form must respect), `corpus/knowledge/synthesis/religion-language-co-evolution.md` (liturgical register genesis); verification — `corpus/knowledge/verification/two-reader-interop-agreement.md` (two readers of one packet must agree about what a law row says); artifacts — `reports/round-26/register/`, `reports/round-27/law/`, `reports/round-27/audit/x59-register-law-negatives.py`, `examples/culture-d4/packet.d4.yml`; siblings — lore-shokunin owns canon and world-bible consistency; chousa-shokunin owns general source-research method; this entry is design method and never canon.
- source: the design authority is `reports/round-26/register/{design,forms,rules,review}.md` plus `reports/round-27/law/{design,rules}.md`; the measured authority is `reports/round-27/audit/x59-register-law-negatives.py` and `reports/round-27/scribe/x54-syllabify-spotcheck.py` run at lane HEAD `b95fca1` on 2026-10-18; the external framework is Austin (1962), Searle (1969/1976/1995/2018), Tambiah (1968), Rappaport (1999), Bourdieu (1991), Clanchy (1979/1993), Irvine (1992), Agha (2007). The register-law *design procedure* and its worked rows are this lane's house method; the frameworks are cited, never blended into a claim about any real community.
- verified-at: 2026-10-18 — written this round against lane HEAD `b95fca1` (`reports/round-27/claims.json` baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`). Measured at write time with `export TMPDIR=$PWD/.scratch`. **Three measurements, because the D seat landed the law mid-round and then closed two of the defects:**
  - **Reading 1** (packet `dd25077b…`, `sha256sum examples/culture-d4/packet.d4.yml`): the `registers:` block read for rows `QREG-01..QREG-04`; the law's absence measured by `python3 -B reports/round-27/audit/x59-register-law-negatives.py` → exit 1, `FINDING L6-HOLD`, `law_rows=0 register_rows=4 records=62`; the register leg green by `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` → exit 0, `records=170 register_scoped=14 derived_pairs=8 violations=0 rule_holds=0`.
  - **Reading 2** (packet `c5441e3d…`): the law found landed as a new top-level `register_law:` block from `examples/culture-d4/components/13-register-law.yml`; the auditor re-run → `FINDING L6-HOLD`, `law_rows=0 speech_act_rows=0 register_rows=4`; the argot leg → exit 0, `records=175 register_scoped=14 derived_pairs=8 violations=0 rule_holds=0`; `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → `FAIL L1-profile`, stale pins.
  - **Reading 3** (packet `86079a67…`, last stamp): `x59` → `law_rows=5 law_wiring_checked=5 register_law_block=5 register_rows=4 speech_act_rows=5`, `failures: 2`, the two being `L6b-HOLD` (no enforcement leg) and `L9-HOLD` (block unregistered in the assembler) — **`L6` closed**; `typed-pipeline-gate` → `summary: 20/20 legs passed`, exit 0 (the O seat re-pinned `tools/gates/typed-pipelines.json` profile `d4` to `86079a67…`).
  - Cross-checks at close: `python3 -B reports/round-27/audit/entry-audit.py corpus/knowledge/linguistics/register-strata-attestation.md` → exit 0, `bar=True filler=False src=19/19 refs_unres=0 digests_bad=0 couples_unres=0`; `python3 -B reports/round-27/audit/x63-entry-source-resolvability.py --offline` → exit 0, `locators=36 unresolved=0 exempt=0 pins=4 sweeps=0`, `findings=0`; `python3 -B reports/round-27/readme/sweep.py` → exit 0, `rows 200 files 200`, 0 missing, 0 topic mismatch, `totals_ok True`; `python3 reports/round-27/run-validation.py --check` → **claim C `passed: true`**. The three-witness syllabify reading was taken from `reports/round-27/scribe/x54-syllabify-spotcheck.py`. Digests in `sources` are pinned **only** where the file was stable; the churning round-27 peer files are cited by revision with the reason stated, so no stale pin is manufactured (see `RSA-9`/`RSA-10`). The external locators were fetched or attributed as stated; two fetches failed and are reported in §9 rather than dressed as successes.
- recheck: before quoting any law row (`RGL-*`, `RLAW-*`, `QREG-*`) into a handoff; whenever `examples/culture-d4/components/{04-lexicon,13-register-law}.yml` or `packet.d4.yml` changes (the `registers` and `register_law` blocks are the law's hosts); whenever `tools/assemble-culture-d4.py`'s `PACKET_KEYS` or `tools/d2-typed-labels.py`'s `GATE_PROPERTY_KINDS`/`verdict_for` changes (the address question, §4.1, and the enforcement leg's price, §7); whenever a round lands a speech-act replay leg (this entry's §7 gap would then be closed and must be re-read); and whenever an external framework above is revised (corrections are new sections or a new entry, never rewrites of this one).

## 1. What this entry is, and the two objects it separates

Two objects get confused constantly, and the confusion is expensive, so this entry keeps them apart from the first paragraph:

| object | what it is | where it lives | who owns it |
|---|---|---|---|
| the **attestation register** | a *speech variety* — the marked way of speaking used when a word is being made to bind | lexicon/derivation records + a register declaration | the language designer |
| the **register law** | a *rule set over speech acts* — who may speak, with what force, with what record consequence | a speech-act component, separate from the lexicon | the institution designer |

The register without the law is a vocabulary nobody is licensed to use. The law without the register is a statute with no words to enforce. Both are needed, and neither implies the other — which is exactly the defect the lane's own drill measured twice in one round: first the packet declared register identity rows and **zero** law rows (`x59` `L6-HOLD`, `law_rows=0 register_rows=4`), and then, when the law rows landed in a **new top-level key** (`register_law:`) rather than in the `registers:` block the auditor reads, the same instrument held again (`law_rows=0 speech_act_rows=0` on a packet that already contains five law rows). §4.1 carries both readings. The second is the sharper lesson: **the law's address is part of the law.**

**What this entry refuses to be.** It is not a second phonology (a register owns no private segment); it is not a rank rule (see §7); it is not canon (whether any town observed the law is lore-shokunin's); and it is not a claim about any real community's practice — every real case below is a *design exemplar*, cited, and never a template to port wholesale.

## 2. The speech-act framework, as a designer's toolkit

Austin (1962) is the floor. Three distinctions carry all the design weight:

- **Locution / illocution / perlocution.** What was said / what was *done in* saying it / what *resulted*. A worldbuilder designs at the illocutionary layer and writes consequences at the perlocutionary one; conflating them produces dialogue where characters narrate their own effects.
- **Felicity conditions.** An act is performed only if the conditions hold: the right **authority**, the right **venue**, the right **procedure**, the right **precedent**, and the addressee's **uptake**. Austin's own examples are institutional to the bone — christening a ship, pronouncing a couple married, appointing to a post, declaring proceedings open, rescinding an offer.
- **Misfires vs abuses** — the two failure classes, and the reason this entry's law has two different penalty shapes:

| class | what happens | in-world shape | design lever |
|---|---|---|---|
| **misfire** | the act is **not performed** — no authority, wrong venue, no uptake | the words were said and nothing is true | the *void* outcome; nothing enters the record |
| **abuse** | the act **is performed** but is insincere, or the speaker does not mean to be bound | the words bind, and the speaker is forsworn | the *sanction* outcome; the record stands and the swearer is answerable |

That asymmetry is the single most useful thing Austin gives a worldbuilder, because it makes two distinct institutions out of one scene: a court that voids acts, and a court that punishes speakers. A culture can have either, both, or neither — and each choice is legible to a reader.

Searle's five classes (1976) turn Austin's observations into a checklist a designer can walk:

| class | the act does | institution it needs | delivered-tree row (the drill, §8) |
|---|---|---|---|
| assertives | commits the speaker to something's being the case | a truth-standard and an audience that can check | testimony bound by evidentials |
| directives | tries to get the hearer to do something | a right to direct, and a sanction for refusal | `QREG-05` the charge (`directive-binding`) |
| commissives | commits the speaker to future action | a record that can outlive the speaker | `QREG-06` the attested oath (`commissive-binding`) |
| expressives | expresses a state of mind | etiquette; almost no institutional machinery | mourning formulas, thanks, curses |
| declarations | **makes** something the case by saying it | an extralinguistic institution that confers the power | `QREG-07` the naming of a lot (`declarative-naming`) |

The classes are not equally costly. Assertives and expressives need little; directives need a hierarchy; **declarations need an institution that already exists and already has the power to confer it** — which is why a declaration is the most expensive speech act a designer can put in a world, and why the delivered drill's naming act needs a `mold-keeper`'s licence behind it.

## 3. The two source models: binding by form, and binding by institution

Two very different real mechanisms produce "saying it makes it so", and a designer should pick one deliberately rather than blending them:

| model | what carries the binding force | real exemplar | design consequence |
|---|---|---|---|
| **binding by form** | the **invariance** of the formula — no individual's will can alter it, so the words are not the speaker's | Rappaport (1999) on liturgical order; Tambiah (1968) on mantra efficacy independent of comprehension | the register's power is *frozenness*; paraphrase is desecration; the language must have a fixed form set |
| **binding by institution** | the speaker's **delegated authority** — the words are the institution's, lent to a person | Bourdieu (1991) on authorized language and the spokesperson; Austin's christening | the register's power is *licensing*; the same words in an unauthorised mouth are a misfire |

These are not rivals; a culture usually has both, layered. But the *failure modes* differ and a designer must write the right one:

- Under **binding by form**, the failure is a **tampered formula** — the words said wrong, out of order, or paraphrased. The penalty is that the act did not happen, and the institution's reaction is to re-do it correctly.
- Under **binding by institution**, the failure is a **wrong speaker** — the formula said perfectly by someone with no standing. The penalty is the same (void), but the institution's reaction is *not* to re-do it; it is to punish the impersonation.

The drill's `QREG-06` (the attested oath, `speaker: stamp-holder` only, "no master and no delegate may speak it") is the institution model with a deliberately *narrow* delegation. The drill's `QREG-08` (the guest's charge: in-register, bound, but `not-rollable`) is the institution model with a **partial** delegation — the guest gets the force but not the record. That partial case is the interesting one and it is under-designed in most fiction: it is what makes a guest's word real and simultaneously second-class.

## 4. Felicity conditions, turned into a design procedure

The law is built by walking Austin's conditions in order and naming a value for each. The six columns below are the whole procedure; a culture's law is a table of such rows.

| condition | the question | example value (drill row `QREG-05`, the charge) |
|---|---|---|
| **speaker** | who holds the standing to speak this act? | `stamp-holder` (and `furnace-master` by the delivered `RK-03`) |
| **venue / slot** | where and when is the act admissible? | at the weigh-stone, over a lot the speaker has already stamped with the speaker's own stamp |
| **procedure** | what must already be true or done? | the lot is present and already carries the speaker's mark |
| **force** | what does the act do? | `directive-binding` — the lot's count is made binding |
| **consequence** | what record does it leave? | a count-stamp row in the furnace roll |
| **penalty shape** | misfire or abuse, and who enforces? | misfire: nothing enters the roll; the council's fine (`EN-01`) is the abuse-side sanction |

**The six-condition walk is the design procedure, and its output is a row set, not prose.** A law stated as prose ("the stamp-holder's word binds") cannot be replayed, cannot be tested, and cannot be handed to a tool; a law stated as rows can be checked for gaps (a row with no speaker, a force with no consequence) and handed off. This is the same reason the neighbouring verification partition insists a rule carry a locator and a failing case (`corpus/knowledge/verification/verification-method-overview.md` §2–§3).

### 4.1 The gap the procedure exposed in the drill — and the two shapes it was closed in

Walking the six conditions over the delivered packet gave a clean negative result, and the sequence matters more than either reading, because the lane's own round reproduced the entry's whole thesis twice in one day. **Both readings are recorded here** (a correction is a new measurement, never a rewrite of the old one).

**Reading 1 — before the law landed** (packet `dd25077b…`; the state this entry was first written against):

```
$ export TMPDIR=$PWD/.scratch
$ python3 -B reports/round-27/audit/x59-register-law-negatives.py
FINDING L6-HOLD: the register block declares the register IDENTITY (QREG-*) but no
  speech-act law rows (RGL-01..05): what may be said in-register, by whom, and with
  what record consequence is not on the delivered packet surface
counters: admissibility_checked=8 era_checked=8 law_rows=0 oath_checked=8
          plain_records=0 records=62 refs_checked=8 register_rows=4 rule_checked=8
          stamp_records=8
failures: 1
```

Four identity rows, **zero** law rows, and the instrument named the missing columns rather than reporting a vague gap. A designer reading only the packet would learn *that* a register exists and *what its forms are*, and nothing about who may use them.

**Reading 2 — after the law landed** (packet `c5441e3d…`; the D seat's new component `13-register-law.yml` landed mid-round). The law is now **on the packet surface**, as a new top-level `register_law:` block of five rows:

```
$ grep -n "register_law:" examples/culture-d4/packet.d4.yml      # → line 2617
$ grep -n 'id: "RGL-0' examples/culture-d4/packet.d4.yml          # → 2622 2634 2646 2658 2670
```

| row | kind | act | holder | consequence |
|---|---|---|---|---|
| `RGL-01` | admissibility | a charge at the weigh-stone, a lot named as it is sealed, an attested oath | a stamp-holder, or a speaker the holder attests | the form binds; the holder enters it on the stamp-roll |
| `RGL-02` | exclusion | an oath | **none** — no binding oath in-register | a stamp oath is void; the binding oath is plain |
| `RGL-03` | asymmetry | a guest broker's charge / lot-naming / attested oath | a guest broker under a stamp-name | binds and is entered, but the guest keeps no roll |
| `RGL-04` | no-segment | any form in the register | any admitted speaker | no phoneme or syllable is licensed by being in-register |
| `RGL-05` | era | any form in the register | any admitted speaker | every stamp form is `available_from E1` |

**But the independent auditor still emitted `L6-HOLD` at that stamp, and the reason is the entry's central lesson in miniature.** Re-measured on the landed packet (`c5441e3d…`, 2026-10-18):

```
$ python3 -B reports/round-27/audit/x59-register-law-negatives.py
FINDING L6-HOLD: … no speech-act law rows: neither `RGL-0n` nor a `QREG-05..` row
  carrying `speech_act`/`speaker`/`force`/`consequence`
counters: … law_rows=0 … register_rows=4 speech_act_rows=0 stamp_records=8
failures: 1
```

The auditor read `registers:` (where `QREG-01..04` live). The law landed in a **different top-level key**, `register_law:`, so the auditor's `register_rows` was still 4 and `speech_act_rows` was 0 — and it returned `HOLD`, not a silent pass. Three separate things were true at once, and a designer must hold all three:

1. **The law was stated in the packet** — five rows, with the six conditions populated (`kind`, `act`, `holder`, `consequence`, `cite`, `axis`).
2. **The auditor did not read the key it landed in** — so the law's *presence* was invisible to the instrument built to measure exactly this gap. The instrument is honest (it holds) but its scope is the `registers` block, and the D seat chose a new key.
3. **The law rows carried no `force` field** — `01-brief.yml:183` declares the field set as `register_law: [id, register, axis, kind, act, speaker, holder, force, consequence, design_row, evidence, follows]`, but the five rows at that stamp populated `holder` and `consequence` and omitted `speaker` and `force`.

**Reading 3 — the same round, later** (packet `86079a67…`). The D seat then closed both halves of reading 2: the auditor was taught the new key, and every `RGL` row gained a `force`:

```
$ python3 -B reports/round-27/audit/x59-register-law-negatives.py
counters: … law_rows=5 law_wiring_checked=5 register_law_block=5 register_rows=4
          speech_act_rows=5 stamp_records=8
failures: 2      # both L6b-HOLD and L9-HOLD, and neither is L6
```

`law_rows` 0 → **5** and `speech_act_rows` 0 → **5**: the law is now **read** as well as landed, and the `L6` finding is gone. What replaced it is more interesting, and it is the entry's thesis again in a third form:

| finding at reading 3 | what it says | whose surface |
|---|---|---|
| `L6b-HOLD` | "a tampered law value is not a finding in any delivered gate (measured: the tampered packet emits the same finding set as the clean one): the law is a declaration with no teeth — the enforcement leg is unowned" | the enforcement gap this entry's §7 and `RSA-7` declare |
| `L9-HOLD` | "the `register_law` block is landed and every row carries an `id`, but the assembler declares it in neither `PACKET_KEYS` nor `RECORD_FIELDS`… stripping an `id` from a `register_law` row assembles exit 0 and lands `id: None`; the same edit to a `lexicon` row refuses exit 2" | the **address/registration** defect `RSA-9` names |

So the three readings are a sequence, not a contradiction: **absent → present but unread → read but unenforced and unregistered.** Each step closed the previous finding and exposed the next, which is what a law actually being built looks like.

**A cross-check that moved the other way, recorded so the sequence is not one-sided.** At reading 2 the packet's three-artifact read-set had moved without its pins, and `typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` reported `FAIL L1-profile` (`packet: pins dd25077b, live c5441e3d`). By reading 3 the O seat had re-pinned the profile (`tools/gates/typed-pipelines.json`, profile `d4`, packet `86079a67…`), and the same command now returns `summary: 20/20 legs passed`, exit 0. **`RSA-10` was demonstrated and then discharged by its owner**, which is exactly the disposition the row asks for.

**The generalisable form of all of it** — and this is why the sequence is worth keeping in the entry rather than deleting once the law landed:

> **A law is only as visible as the key it lands in, as readable as the fields it populates, and only as real as the leg that enforces it.** Landing the rows is not landing the law: an instrument scoped to one block will report a hold on a packet that already contains the rule; a declared field set will not guarantee the fields are filled; a block the assembler does not register will accept a malformed row; and a law no gate reads cannot be tampered into a finding. When a designer says "the law is in the packet", the four questions to ask are: *which key*, *which fields*, *which validator*, and *which pins moved*.


## 5. The documentary turn: why a record culture needs an attestation register

An attestation register only exists where an oral act must **outlive its speaker**. Clanchy's transition — from proof by witnesses and memory to proof by document — is the historical hinge, and it is a design hinge too:

| proof regime | what settles a dispute | what the register must do | era anchor |
|---|---|---|---|
| **witness/memory** | living people who saw and heard | nothing durable; the register is the *recital* of the witnesses | pre-literate to early scribal |
| **documentary** | a written instrument, sealed or marked | make the spoken word **recoverable** after the speaker is gone | scribal to chancery |
| **both, in tension** | witnesses for the living, documents for the dead | the register must be *quotable* — its forms must survive being read aloud | the whole documentary transition |

Three consequences a designer should build in, each with a real analogue already integrated in the corpus:

- **The mark is not the speech.** A stamp, seal or tally attests that a formula was said; it does not carry the formula. The split-object authentication family — Greek *symbolon*, the English chirograph and indenture, the Exchequer tally's stock and foil (`corpus/knowledge/culture-material/trade-economy-lexicon.md:121`) — is the material half. The register is the *speech* half of the same institution, and the two must be designed together or the world reads as half-built.
- **The record-keeper is a power class.** If the roll is kept by one body, that body decides what counts as having happened. In the drill this is explicit: the league council keeps the furnace roll, and the guest's charge is `not-rollable` — the guest is bound and silent in the record at the same time.
- **Where the register and the record diverge, plot lives.** An act that binds but leaves no record (the guest's charge) is a debt with no ledger; an act that leaves a record but did not bind (a forged mark over an unspoken formula) is a fraud the register cannot detect. Both are stronger scenes than a straightforward oath.

## 6. Worked rows: the four acts, and the constraint that shaped them

The drill's four acts are chosen because the delivered tree supplies the institution for each, and because each carries a different force. Reproduced here as a *design exemplar*, not as canon:

| id | act | speaker | force | consequence | authorising institution |
|---|---|---|---|---|---|
| `QREG-05` | the charge | `stamp-holder` (+ `furnace-master`) | `directive-binding` | count-stamp row; the lot's count binds | `RK-03` the stamp-house |
| `QREG-06` | the attested oath | `stamp-holder` **only** | `commissive-binding` | the term entered against the swearer's lineage bar | `RK-03` + `RIT-03` |
| `QREG-07` | the naming of a lot | `stamp-holder`, `mold-keeper` | `declarative-naming` | the name written on the tally face | `RK-03` + `OR-02` |
| `QREG-08` | the guest's charge | `broker`, `market-goer` | `directive-binding`, `not-rollable` | binds at the gate; may not write the roll | `RK-04` the league charter |

**This is the *designed* shape. The shape that landed is different, and the difference is the lesson.** The landed law is the round-26 `RGL-01..05` row set (five rows keyed on `kind`, not on `speech_act`), so the table above is a **design target** and the landed rows are its partial realization — and the realization moved *during the round*, so the table below records the state at the **last measurement** (packet `86079a67…`):

| designed column | landed `RGL` row(s) | present? |
|---|---|---|
| act | `RGL-01` (admissibility), `RGL-02` (exclusion), `RGL-03` (asymmetry), `RGL-04` (no-segment), `RGL-05` (era) | **yes**, as `act` — but keyed by `kind`, and the four acts of the table are not four rows |
| holder | `holder` on every row | **yes** (the `speaker` field is declared but still empty at this stamp) |
| consequence | `consequence` on every row | **yes** |
| **force** | `force` on every row | **yes at the last stamp** — `RGL-01` `"directive-binding for the charge; declarative-naming for the lot's name"`, `RGL-02` `"commissive-binding refused"`, `RGL-03` `"directive-binding, not-rollable"`, `RGL-04`/`RGL-05` `"none — a sound-channel constraint, not a speech act"` / `"none — a dating constraint, not a speech act"`. This column was **absent at reading 2** and was filled before reading 3 |
| **venue / procedure** | — | **no** — `RGL-01` names the acts and the holder, not the slot |

The `force` column is the clearest single illustration of the entry's own rule: at reading 2 the field was declared in the schema and unpopulated, and the auditor's `speech_act_rows` was 0; at reading 3 it is populated and `speech_act_rows` is 5. **The row that changed was the one the schema declared and the data omitted.**

So the drill's worked example demonstrates the procedure and the landing demonstrates the *partial* realization of it — which is precisely why `RSA-2` (rows over six conditions) and `RSA-9` (address and fields are part of the law) are separate decisions. A designer who lands the act, the holder and the consequence but not the force has landed an institution with no illocutionary content, and the instrument that reads the block cannot say so.

**The constraint that shaped the act set, and the general lesson.** The drill's register was built by an operation rule that reverses one axis of its lexicon and lengthens the other, and the reversal is only legal on some bases. Measured over the drill's 62 delivered forms:

```
mark-axis plain words: 27   reverse-legal: 18   reverse-ILLEGAL: 9
  material-presence bases   8 legal  / 2 illegal
  legal-institutional bases 0 legal  / 5 illegal   <-- every abstraction refuses
```

Every landed in-register form descends from a **material-presence** base (mark, mold, breath, water, smoke, metal, ore, charcoal); **not one** descends from a legal or institutional abstraction. The sharp case: the word for *oath* is an abstraction, its in-register form is not spellable, and **the register therefore cannot say "oath" in itself**.

The generalisable lesson — and the reason this is in a knowledge entry and not only in a round report — is:

> **A register's derivational mechanism silently decides which *semantic classes* can enter the register.** If you generate in-register forms by a mechanical operation over an everyday lexicon, the operation's legality conditions, not your intentions, will pick the register's semantic profile. Choose the operation *after* deciding which classes must be sayable in-register, or accept that your register will be the vocabulary of *things* and never of *obligations*.

A designer who wants a register that can say "oath", "right-of-way", "price" and "weight" must either (a) build the register from a hand-picked base list, (b) choose an operation whose domain includes abstractions, or (c) accept the ceiling and write the law inside it — which is what the drill did, stating the oath in terms the register *can* carry and putting the consequence on the record-keeper's side.

## 7. The boundary: the register law is not a rank rule

This is the boundary the lane's own forecast got wrong, and it is worth stating as a table because the two systems look alike and are enforced by different machinery:

| | rank / sumptuary rules | the register law |
|---|---|---|
| regulates | **what may be worn** — a material, a badge | **what may be said, and what it makes true** |
| the property | a kind/value over a physical thing | speaker + force + consequence over an act |
| enforcement | a fine; a refusal to **mark** | the act is **void** — nothing enters the roll |
| evidence field | wearer ranks, rites, eras | speaker, force, consequence, slot |
| what it resolves against | a costume row's material or badge | a **speech** row — and no such leg exists by default |

**Why the merge fails, mechanically.** Folding a speech act into a costume-rank ledger makes the checker resolve a speech act against a *costume* row, and a speech act has no costume row — so the rule falls through to "cannot evaluate", which reads as "no problem found". The lane measured this shape and reported it (`reports/round-27/law/design.md` §4–§5); the general form is:

> **A rule that cannot find its target must fail loudly, never fall through.** If a validator's dispatch ends in a default `not-applies`, then adding a new rule *kind* to the guard converts an honest hold into a silent pass — which is strictly worse than the hold.

**The right coupling is a link, not a merge.** The rank rule says *who holds the stamp*; the register law says *what holding it lets you say and what the saying costs*. Each law row names the rank row that authorises it, so a reader can trace an act to its licence — and a checker can still see two systems, not one.

## 8. Design procedure (build order)

1. **Decide the proof regime** (§5): witness-based, documentary, or in tension. This determines whether an attestation register exists at all. No record-keeping institution, no register.
2. **Pick the source model** (§3): binding by form, by institution, or layered. Write the corresponding failure mode (tampered formula vs wrong speaker) before writing any law row.
3. **Choose the register's forms and their derivation, checking the semantic ceiling** (§6). List the classes that *must* be sayable in-register (obligations, measures, names) and verify the operation's domain covers them — or accept the ceiling and record it.
4. **Walk the six conditions** (§4) for each act: speaker, venue/slot, procedure, force, consequence, penalty shape. A row with a blank column is an unfinished institution, not a stylistic choice.
5. **Classify each act** (§2, Searle): assertives and expressives are cheap; directives need a hierarchy; declarations need a pre-existing institution with the power to confer. Budget accordingly — declarations are the expensive ones.
6. **Separate the two systems** (§7): keep the law out of the costume/rank ledger; link the rows by ID instead. Name the enforcement mechanism, and make the checker fail loudly where no mechanism exists.
7. **Write the metadiscourse** that enregisters the register: the formula's fixed wording, the etiquette of who may speak it, the proverbs mocking mis-users, the sanctioned cases. A register with no metadiscourse does not read as belonging to an institution (`corpus/knowledge/linguistics/sociolinguistics-registers.md` §1).
8. **Stress-test the scenes**: oath at a gate, a lot named as it is sealed, a guest's charge refused a roll entry, a formula said by the wrong speaker, a mark over a formula never spoken. Table speaker × act × venue; an empty cell is a missing institution.
9. **Declare the gap.** Where the law is a declaration with no replay leg, say so, and name the price of enforcement — do not let a green gate stand in for an unbuilt law.

## 9. Calibration: mainstream, contested, and commonly botched

- **Austin's framework** (performatives, illocutionary force, felicity, misfire/abuse): **mainstream**, foundational. Caveat: Austin's own programme of enumerating act types was never completed, so "the" felicity conditions for a given act are not a fixed list to be looked up — they are a design surface.
- **Searle's taxonomy** (1976): **mainstream** and widely used, with the usual complaint that the five classes leak into one another (a declaration is often also a directive). Use it as a checklist, not a partition.
- **Searle's constitutive rules and deontic powers** (1995, 2018): **contested in its details**. The constitutive-rule account is influential, but Guala and Hindriks (as recorded in the Stanford Encyclopedia's *Social Institutions* entry, §§"constitutive rules", "deontic powers") argue constitutive rules are not necessary to institutions and that the deontic reading needs more argument than Searle supplies. Use "X counts as Y in C" as a *generator*, not as a law of institutions.
- **Rappaport's invariance claim** (1999): **mainstream** in ritual studies and the standard authority for "frozen form carries the authority". Limit: it is an anthropological generalisation from a comparative base, not a tested universal, and it does not say a culture *cannot* have variant liturgy — only that variance costs authority.
- **Bourdieu's authorized language** (1991): **mainstream** in the sociology of language, **contested** as a general theory. Its strongest form — that a speech act's force is *entirely* delegated — is not falsifiable as stated; use the weaker, useful form: authority is *institutionally lent*, and the same words misfire in an unauthorised mouth.
- **Clanchy's documentary transition** (1979/1993): **mainstream** medieval social history. Limit: it is one country's record (England 1066–1307); do not read it as a universal sequence with dates.
- **"Some words are inherently performative"**: **botched framing.** Austin himself abandoned the performative/constative dichotomy in favour of illocutionary force. Any word can carry force given the right institution; no word carries it by nature. A designer who makes an in-world word magic *because of its sound* is writing a different (and legitimate) system — but should not label it speech-act theory.
- **"Binding speech is primitive/religious, and modern law is rational"**: **discredited framing** in this form. Documentary legal language is *more* formulaic and more register-locked than most ritual speech, not less (`corpus/knowledge/linguistics/sociolinguistics-registers.md` §4, Tiersma 1999: legal language resists paraphrase by design).
- **Conflating the register with politeness**: a polite register and an attestation register are different objects. Politeness indexes *relative standing* (honorifics, T/V); attestation indexes *whether the act binds*. They often co-occur and are separately designed.
- **Fetched and failed, reported rather than dressed:** the `plato.stanford.edu/entries/bourdieu/` locator returned **404** (2026-10-18), and the Cambridge Core page for Rappaport's book returned **429 Too Many Requests**; the Internet Archive catalogue record was used instead for the chapter list, and Bourdieu is cited by path through `linguistic-anthropology.md:67`. No locator above is asserted that was not either fetched or attributed to a named in-repo passage.

## 10. Decision record — the rules this entry adopts

| ID | decision | evidence | consequence if violated | recheck trigger |
|---|---|---|---|---|
| **RSA-1** | the register and the law are **two objects**; a register declaration without law rows is an unfinished institution | `x59` `L6-HOLD` at readings 1–2 (§4.1): `law_rows=0 register_rows=4`, then `law_rows=0 speech_act_rows=0` after the rows landed in a different key; **closed at reading 3** (`law_rows=5 speech_act_rows=5`, `L6` gone) | a vocabulary nobody is licensed to use; a law with no words | any packet that gains a `registers` or `register_law` block |
| **RSA-2** | the law is stated as **rows over six conditions** (speaker, venue, procedure, force, consequence, penalty shape), never as prose | §4; `reports/round-27/law/rules.md` §1's replayable/unowned column | prose law cannot be replayed, tested, or handed off | every law row set |
| **RSA-3** | **misfire and abuse are different institutions** and get different penalty shapes (void vs sanction) | §2 (Austin's two failure classes) | one institution doing both jobs, and a reader who cannot tell which happened | every law design |
| **RSA-4** | the **derivational operation picks the register's semantic profile**; verify the classes that must be sayable before choosing it | §6, measured `0 legal / 5 illegal` over the drill's institutional abstractions | a register of things that can never speak of obligations | any register built by a mechanical operation |
| **RSA-5** | the register law is **never merged into the rank/sumptuary ledger**; the two are linked by row ID | §7; `reports/round-27/law/design.md` §4 | the checker resolves a speech act against a costume row and silently passes | any attempt to add `kind: register`/`speech-act` to a costume rule set |
| **RSA-6** | a rule that cannot find its target must **fail loudly**; a default `not-applies` turns a hold into a silent pass | §7 (measured: widening the guard yields `not-applies`) | an unenforced law reads green | any widening of a validator's kind guard |
| **RSA-7** | the law's own **enforcement gap is declared, with its price**, rather than covered by a green gate | §7–§8 step 9; `reports/round-27/law/rules.md` §1; and `x59` `L6b-HOLD` at reading 3 — a tampered `force` emits the same finding set as a clean one | a declaration presented as a checked rule | every round that cites a register-leg green |
| **RSA-8** | no law row is quoted without its **era window**; an in-register form claimed before the register's institution exists is a defect | `reports/round-26/register/rules.md` §5 (`REGISTER-ERA-01`), `QREG-04`, and the landed `RGL-05` (`force: "none — a dating constraint, not a speech act"`) | anachronistic attestation speech in a world with no attestation institution | every era-staged packet |
| **RSA-9** | the law's **address, registration and fields are part of the law**: name the key it lands in, register the block with the assembler, and populate every declared field | §4.1 reading 2 (landed in `register_law:`, not `registers:`; `speaker`/`force` empty; `speech_act_rows=0`) and reading 3 (`x59` `L9-HOLD`: the block is in neither `PACKET_KEYS` nor `RECORD_FIELDS`, so a stripped `id` assembles exit 0 while the same edit to a `lexicon` row refuses exit 2) | a law present in the packet that no instrument finds; a block whose rows are unvalidated; a declared field set that is not filled | any law landing; any auditor scoped to one block; any component key not in the assembler's allowlist |
| **RSA-10** | a change to the register surface **moves the read-set pins with it**; a pin left behind is a stale-pin failure, not a cosmetic drift | §4.1 reading 2 — `typed-pipeline-gate` `FAIL L1-profile` on `packet pins dd25077b, live c5441e3d` (same class as `reports/round-26/register/repin.json`'s cascade); **discharged at reading 3** by the O seat's re-pin (`typed-pipelines.json` profile `d4` → `86079a67…`, `summary: 20/20 legs passed`, exit 0) | a green leg reading a superseded packet; a reader following the entry into a red tree | every landing that touches `examples/culture-d4/` |

- **Append-only discipline.** This entry never rewrites a filed round receipt. If a later round lands the law component or a replay leg, the correction is a new section here or a new entry linked from `recheck`; the round-26/27 artifacts cited keep their bytes.

## 11. Limits of this entry

- **No real community is described.** Every real case (Austin's christenings, Rappaport's liturgy, Bourdieu's market, Clanchy's England) is a cited design exemplar. Nothing here says what any actual culture does, and no real-language resemblance screening has been run on the drill's forms.
- **The drill is NON-CANON.** `examples/culture-d4/` is an engineering drill; its furnace-league, stamp-house and four acts are not canon for any world.
- **The law's content is a design choice.** No informant, corpus or frequency evidence exists for any speaker, force or consequence in §6.
- **The law's replay leg is unowned and unbuilt.** `RLAW-01..05` have no executable owner (`reports/round-27/law/rules.md` §1); only `RLAW-06` (the derivation rule) is green, and green there means the *arithmetic* replays, not that the law is enforced.
- **The landed law is incomplete, and the incompleteness moved during the round** (§4.1). At the last measurement: the law sits in a key the auditor now reads (`register_law:`, `law_rows=5`), but the assembler registers the block in **neither** `PACKET_KEYS` nor `RECORD_FIELDS` (`x59` `L9-HOLD`: a stripped `id` assembles exit 0 while the same edit to a `lexicon` row refuses exit 2); the `speaker` field its declared field set names is still empty; the law still has **no enforcement leg** (`L6b-HOLD`: a tampered `force` emits the same finding set as a clean one); and `venue`/`procedure` are not on the surface at all. This entry records all four and repairs none — they are the D and O seats' surfaces.
- **The entry's own measurements are point-in-time, and the point moved three times.** The packet went `dd25077b…` → `c5441e3d…` → `86079a67…` inside the round, and peer round-27 files moved while the entry was written. Every reading above names its packet digest or revision; re-measure before quoting. A reader who finds a fourth state should treat this entry as the *sequence* it records, not as a claim about the current tree.
- **Two external locators failed and are reported, not laundered** (§9). The Rappaport invariance claim is attributed to a neighbouring entry's statement of it, not to a retrieved page of the book.
- **Thin knowledge, stated.** This entry contains no general theory of institutions, no legal-philosophy position on the validity of norms, and no claim that its six-condition walk matches any other lane's practice. It is design method for one lane's craft.

## 12. Canon boundary and handoff

- Nothing here decides what is true in any world. The register, its law rows and its consequences are **systems this lane generates**; which of them exist in a given world, and which factions they bind, are lore-shokunin's decisions (`PROVINCE.md`; `AGENTS.md`).
- **Handoff shape.** Ship the law as a row set (six columns per act) with each row naming its authorising rank/rite row by ID, plus the declared enforcement gap and its price. Ship the register's forms with their derivation and era window. Never ship a law row without its era and its authorising row.
- **Contested scope → report, never absorb.** If the receiving lane expects the law inside the costume-rank ledger, or expects a green register gate to certify the law, that is reported to the integrator — this entry's §7 and `RSA-7` state why the merge fails mechanically, and the decision is not this lane's to make unilaterally.
