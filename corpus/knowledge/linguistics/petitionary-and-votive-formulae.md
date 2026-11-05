# Petitionary and votive formulae: vocative address, petition mood, the conditional vow, votive inscription grammar, prayer-register archaism and litanic parallelism

- topic: petitionary address and votive formulae: vocative address to deities, petition mood (imperative, optative, precative), the conditional vow, votive inscription grammar, prayer-register archaism and parallelism, design procedure and failure modes
- sources: S942 S943 S944 S945 S946 S947 S948
- verified-at: 2026-11-04 — seven sources opened live this round; bodies and sha256 in `reports/round-90/evidence/` with `manifest.json`; WALS value counts read from the map value tables themselves, not from the prose summary.
- recheck: 180d — re-open the three WALS chapter pages plus the two catalogues. Chapter numbers move on that site: the Prohibitive is chapter 71, and chapter 74 now holds Situational Possibility, so a row that inherits a chapter number from a reading list rather than from the page is already wrong.
- couples: linguistics/semantics-pragmatics (wish, obligation, commitment), linguistics/syntax-typology (mood as inflection versus periphrasis), linguistics/politeness-taboo-euphemism (address rank and the flattery of epithets), linguistics/orality-formulaic-language (parallelism and fixed diction), linguistics/historical-linguistics (frozen archaic morphs in prayer), myth-symbol (deity inventories and their epithets), culture-material (votive objects actually offered), synthesis/worldbible-integration-contract (handing the register to lore as a system, never as canon).

## 1. What the register is, and what it is not

Petitionary language is the speech act of asking a power for something; votive language is the speech act of binding oneself to give something in return. They share an addressee and a future state of affairs, and they differ exactly in who is obliged. A petition asks the god to act; a vow obliges the speaker to act if the god acts first. Worlds that conflate the two lose the single most useful social lever the register provides, because a vow is a debt the culture can collect on and a petition is not.

Three components are separable in every attested tradition and should be designed separately:

1. **Address** — how the addressee is named and ranked (vocative morphology, epithet stacks, circumlocution).
2. **Petition** — the mood or periphrasis that carries the wish (imperative, hortative, optative, prohibitive, precative particle).
3. **Obligation** — the form of the promised return, from a named object through a named sacrifice to a named text (the inscription itself).

A prayer register is not "religious vocabulary". It is a small set of formal devices — address form, mood choice, fixed epithet, parallelism, archaism — reused across content. A culture can have an enormous religious lexicon and no prayer register at all, which is the commonest failure in invented worlds: priests who speak ordinary prose about extraordinary things.

## 2. Vocative address: the grammar of being addressed

A vocative is not a decorative prefix to a sentence; it is a case whose whole function is to mark the referent as the addressee. The SIL glossary definition is the minimal one: vocative case marks "a noun whose referent is being addressed", with the canonical Latin example *Et tu, Brute* (S945). Two consequences follow for design.

First, the vocative is syntactically outside the clause's argument structure in most languages that have one, so it can carry material that would be ungrammatical elsewhere: a bare title, a genealogy, a list of cult places. That is why address formulae grow: the slot accepts apposition without limit.

Second, address rank is encoded by *which* name is chosen, not by morphology. A culture distinguishes, in its address system, between:

- **name** — the deity's proper name, the default in private dedications;
- **epithet** — a functional title (*Hypsistos*, "the Highest"; *Soter*, "Saviour") that locates the god in a cult, not in a pantheon;
- **periphrasis** — a relative clause or participle ("the one who hears"), used where the name is dangerous, unknown, or plural.

Design rule: give the vocative a distinct form only if the language already has case; otherwise give it a distinct *particle* or a distinct *prosody*, and say which. A conlang whose vocative is identical to the nominative but whose address formulae are elaborate is perfectly plausible — Greek and Latin did exactly this with foreign divine names, which is why the epigraphic corpus is full of indeclinable barbarian theonyms sitting in a vocative slot.

Warning from the sources: a general glossary will not carry the terms a prayer register needs. The SIL glossary has `vocative-case` but returns 404 for `/term/vocative` and has no entry at all for *prayer*, *invocation*, *supplication*, *votive*, *vow*, or *blessing* (checked 2026-11-04). A designer who needs a term that a lexicon does not define is looking at a concept the tradition under study did not lexicalise as a category.

## 3. Petition mood: four paradigms and what their counts mean

WALS documents the petition paradigms that are grammaticalised across its samples. The counts below are the map value tables, with the total each chapter prints; they are sample-bounded frequencies, never world frequencies, and they should be quoted with the chapter number because the site has renumbered chapters.

| feature (WALS chapter) | values distinguished | sample counts | design consequence |
|---|---|---|---|
| Imperative-hortative systems (72) | maximal only / minimal only / both / neither | 133 / 20 / 21 / 201, total 375 | the "maximal" system is the marked one; most sample languages grammaticalise a minimal imperative only |
| The optative (73) | inflectional optative present / absent | 48 / 271, total 319 | a dedicated wish inflection is a minority option; periphrasis is the unmarked choice |
| The prohibitive (71) | second-singular imperative + declarative negation / + non-declarative negation / other verb + declarative negation / other verb + non-declarative negation | 113 / 182 / 55 / 146, total 496 | the negative of a command is a separate paradigm, not the imperative plus "not" |
| Vocative case (SIL glossary) | case marking an addressed noun | not a frequency claim | address is a slot, not a mood; keep it out of the mood system |
| Votive terminology (epigraphic corpus) | explicit *euche/euchomai* wording present / absent | increase over time, corpus of about 11,000 inscriptions | votive wording is a diachronic variable a culture can be placed on |

Chapter 72's central claim is homogeneity: the imperative and the hortative form one paradigm whose members differ by person, and the chapter counts how far that paradigm is filled out. A **minimal** system is one where the second-singular imperative is not formally homogeneous with any other form; a **maximal** one is where it is homogeneous with the other second persons, the third persons and at least an inclusive first-person plural. The chapter also fixes the boundary that matters for design: imperatives and hortatives express the speaker's wish about a future state and *appeal to the addressee to help make it true*, which is precisely what separates them from the optative (S942).

Chapter 73 defines the optative narrowly — an inflected verb form dedicated to the expression of the speaker's wish — and reports 48 sample languages with one against 271 without (S943). It also records the distribution: none in Australia or Africa, two in Europe (Albanian, Karaim), one in New Guinea. For a designer this is the strongest available argument that an optative should be *earned*: it is a minority inflection concentrated in a few families and areas, so a world in which every language has one is a world that has not thought about areal diffusion.

Chapter 71 is the one that repays the most care. The prohibitive is defined as the grammaticalisation of a prohibition addressed to a single addressee, and the four values cross the verb's shape against the negation strategy. Only 113 of 496 sample languages use the plain second-singular imperative with the same negation as declaratives; the largest single class (182) uses the imperative with a *different* negative strategy; 146 use a different verb entirely (S944). The design lesson is exact: "do not" is not the negation of "do" in most languages of the sample, and a conlang that forms its prohibitive by adding the ordinary negator to the imperative has chosen the minority pattern — legitimate, but it should be a choice, not an oversight.

A fourth option deserves a row of its own in any design document: the **precative**, a dedicated non-inflectional petition particle (often a clitic) that carries the wish without mood morphology. WALS chapters 72 and 73 explicitly set non-inflectional expressions of the wish aside, so the sample counts say nothing about particles; absence from the counts is not absence from the languages. When a world's petition is particle-based, the design burden moves from morphology to particle placement and to the particle's interaction with negation.

## 4. The conditional vow and votive inscription grammar

A votive inscription is a small genre with a stable grammar, and its stability is what makes it usable as a worldbuilding device: the reader of a fictional dedication recognises the shape before parsing the content.

The Greek shape, as the Attic catalogues present it (S946), runs: dedicant in the nominative, a verb of dedicating, the object, and the deity in the dative, optionally with the maker named in a second clause. IG I³ 646, a columnar base from the Acropolis dated ca. 510–500 BC, reads in translation as *Smikros dedicated (me), the tanner, Euthykles made me* — a speaking object, an occupational self-identification, and a craftsman's signature in eleven words. The commentary on that page shows the other half of the genre's value: the letter forms and the occupational term carry social history (specialist tanning before the fifth century), which is to say a dedication is a dateable, attributable, socially located document rather than a pious decoration.

The vow proper adds conditionality. Two formulaic patterns cover most of the evidence:

- **Vow before the fact** — "if the god does X, I will give Y": the inscription records an obligation, and its fulfilment is often recorded later, either on the same stone or by a second monument.
- **Dedication after the fact** — "having vowed, I dedicated": the object is the receipt. The Latin tag *ex voto suscepto* names exactly this bookkeeping.

The large-scale study of Greek votive epigraphy (S947) is the best evidence that these formulae are variables rather than constants. Blidstein's distant reading of about 11,000 Greek dedicatory inscriptions from the sixth century BCE to the seventh century CE, drawn mainly from the GIST/I.PHI corpus, tags each text for votive terminology, deity, motive and gender, and controls for the "epigraphic habit" — the changing propensity of a society to inscribe at all, which otherwise masquerades as religious change. Its findings, as stated in the abstract:

- explicit votive terminology (forms of *euche*/*euchomai*) increases in relative frequency over time, especially in the Roman Imperial period and Late Antiquity;
- the practice is regionally uneven, markedly more prevalent in Asia Minor and the East than in mainland Greece before the fourth century CE;
- votive formulae correlate positively with particular deities (Men, Meter, Hypsistos, Hosios kai Dikaios) and negatively with others (emperors, Athena);
- votive terminology correlates negatively with naming other motives (dreams, commands) and with standard consecration terms.

Those four findings translate directly into a design procedure. If a world's dedications all use one formula, the world has no religious history; if the formula is uniform across regions, it has no religious geography; if every deity accepts the same wording, the pantheon has no cult differentiation. The correlations are the cheapest available generator of plausible variation.

The conditional vow also needs a stated failure mode, because a vow is a contract and contracts have breach: what happens when the god does not deliver, or the dedicator does not pay. Attested solutions include re-dedication, erasure, legal fiction (the vow was conditional on a condition never met), and transfer of the debt to heirs. A world that has vows but no breach procedure has designed a form without a society.

## 5. Prayer-register archaism, parallelism and litanic generation

Two formal devices distinguish prayer from prose in nearly every tradition, and both are cheap to design.

**Archaism.** Prayer conserves forms the colloquial has lost: an older case ending, an obsolete pronoun, a conservative cluster. The mechanism is conservative performance, not magic: a fixed text is repeated by rote and resists sound change. Design it by staging the register against the language's own chronology — the morphology of the prayer register should look like the language two or three centuries earlier. This gives a conlang a datable layer without inventing a second language.

**Parallelism.** The line is built as a pair whose second member restates the first with a variation (synonym, antonym, specification). It is the cheapest way to make a text sound liturgical, and it is generative: a pair can be expanded to a triplet, and a triplet to a litany. Lowth's description of Hebrew parallelism is the classic account; the lane's orality entry holds the general theory.

The computational study of litanies (S948) shows that the litanic form is rule-governed enough to be generated. Galofaro and Kubas study the Litany of the Saints and the Litany of Loreto in their most ancient attested forms, build a narrative grammar that generates their structure, and propose **n-selection**: a narrative rule which "can't be reduced to syntax or semantics" because it depends on culture. They then test the grammar by generating the twentieth-century Litany to the Divine Mercy, written by Faustina Kowalska, and identify the genre rules that let the form reproduce in later versions.

For design, n-selection is the important term. A litany is not a list with a refrain; it is a *culturally ordered* list, where the order and the set of admissible members are decisions of the tradition, not of the grammar. A world's litany therefore encodes its hierarchy: which saints, in which order, with which epithets, and which categories are expandable. If the order is arbitrary, the litany is decoration; if the order is a ranking, the litany is a political document that can be quoted in a dispute.

Practical composition rules that follow from the two sources:

1. Fix the couplet: invocation (vocative + epithet) plus petition (mood or particle). Everything else is expansion.
2. Let the refrain be invariant while the invocation varies; the invariant part is what a congregation can join.
3. Keep one archaic layer, and keep it consistent: an archaism that appears in one line and not its parallel is a scribal error, and a reader will treat it as one.
4. Order the invocations by a cultural principle the world can state (rank, chronology, cult place, function), because that principle is what a later schism will fight over.

## 6. Design procedure for a fictional culture

A working sequence, each step producing a file the world bible can hold:

1. **Choose the mood strategy** and record it as a decision: inflectional optative (minority pattern, S943), imperative-hortative paradigm with a distinct prohibitive (majority pattern, S942/S944), or particle-based precative (not counted by the WALS chapters). One strategy per language, with an areal reason for its distribution across a family.
2. **Separate the prohibitive.** Decide whether the negative command shares the imperative's negation, and if it does not, name the negative strategy. This single cell is the most reliable typological fingerprint a reader can check.
3. **Build the address system**: vocative form or particle; epithet inventory; circumlocution rules for dangerous or unknown names; the rank order the culture uses.
4. **Write the vow formula** in three slots (condition, deity, promised object) and then write the fulfilment formula as its receipt. Name who may vow, who may witness, and what happens on breach.
5. **Design the votive object inventory** against the culture's material record, and give each deity a preferred object class: the correlation finding (S947) predicts that cults differ in what they are given, not only in who is asked.
6. **Stage the register diachronically**: list the archaisms, and give each a colloquial counterpart in the modern stage of the language.
7. **Generate the litany** from the rank order with a fixed refrain and a culturally principled member set (S948's n-selection). Write the principle down; it is the thing that makes the form reproducible.
8. **Write the failure cases** before the good examples: an unanswered petition, a breach of vow, a prayer in the wrong register, a litany with one invocation out of order. The failure cases are what let a reader test the system.

## 7. Failure modes and checks

- **Petition without addressee.** A prayer that never names or ranks its addressee reads as narration, not address. Check: does every prayer text contain a vocative slot, even an empty one?
- **Vow without receipt.** Obligations that are never recorded as fulfilled leave the culture without a bookkeeping habit, and the register loses its documentary function. Check: is there at least one fulfilment formula in the corpus?
- **Prohibitive as imperative plus negation**, when the design claims a distinct paradigm. Check: the negation in the prohibition is or is not the declarative negator — one cell, and it must match the decision file.
- **Optative everywhere.** A dedicated wish inflection in every language of the world contradicts the areal skew the sample shows. Check: which families have it, and what is the contact story?
- **Chrome piety.** Fixed epithets attached indiscriminately to every deity flatten the pantheon; the correlation evidence says cults differ. Check: two deities with the same epithet stack must be justified by a shared cult.
- **Archaism without a modern stage.** An archaic layer that is not contrastable with a colloquial form is just unusual spelling. Check: each archaism has a listed modern counterpart.
- **Litany as unordered list.** Check: state the ordering principle and one admissible expansion; if the principle cannot be stated, the form is decorative.
- **Sample counts quoted as world frequencies.** WALS counts are sample-bounded (375, 319, 496 languages respectively). Check: every quotation carries chapter number and total.

## 8. Scope and calibration

The evidence here is deliberately narrow and it is stated as narrow. Three WALS chapters give typological counts over their own samples; one glossary gives a definition; two catalogues give one dated inscription and one distant-reading study of Greek dedicatory practice; one computational paper gives a generative account of two Catholic litanies. Nothing here establishes frequency in the world's languages, the theology of any tradition, or the truth of any reconstruction.

The votive evidence is Greek and Mediterranean; the litanic evidence is Christian and Latin; the mood typology is worldwide but sampled. A world that borrows the Greek vow formula and the Catholic litany while claiming a non-Mediterranean, non-Christian religion should be able to say what it changed and why — that statement, not the borrowing, is the design work.

This entry is NON-CANON by construction: it describes a design surface and its checks. It does not record, ratify or verify any world's canon, and the handoff to lore remains a handoff (`synthesis/worldbible-integration-contract.md`), never an import.
