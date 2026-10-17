# Naming-Collision Gate — Identity, Pronunciation, Derivation, and Cultural Overlap
- topic: A pre-handoff gate for name uniqueness across a supplied canon snapshot, phonotactic pronounceability, derivational validity, and bounded cross-cultural collision review; method and reference knowledge only, never canon approval.
- sources:
  - [N] Hough, Carole (ed.) (2016), *The Oxford Handbook of Names and Naming*, Oxford University Press, ISBN 9780199656431; [publisher DOI](https://doi.org/10.1093/oxfordhb/9780199656431.001.0001). Onomastic reference, not a universal naming template.
  - [P] International Phonetic Association (1999), *Handbook of the International Phonetic Association: A Guide to the Use of the International Phonetic Alphabet*, Cambridge University Press; [DOI](https://doi.org/10.1017/9780511807954). Phonemic versus phonetic representation.
  - [S] Maddieson, Ian (2013), “Syllable Structure,” in Dryer, Matthew S. and Martin Haspelmath (eds.), *The World Atlas of Language Structures Online*, chapter 12; [chapter](https://wals.info/chapter/12). Sequencing restrictions and the limitations of broad syllable types.
  - [M] Haspelmath, Martin, and Andrea D. Sims (2010), *Understanding Morphology*, 2nd ed., Hodder Education; [current Routledge catalogue](https://www.routledge.com/Understanding-Morphology/Haspelmath-Sims/p/book/9780340950012), ISBN 9780340950012. Derivation, inflection, allomorphy, and morphology–phonology interfaces.
  - [U15] Unicode Consortium; Whistler, Ken (ed.) (2026), *Unicode Standard Annex #15: Unicode Normalization Forms*, Unicode 18.0.0, revision 58, 12 August; [versioned text](https://www.unicode.org/reports/tr15/tr15-58.html), especially §§1.1–1.2.
  - [U39] Unicode Consortium; Hadley, Josh, and Roozbeh Pournader (eds.) (2026), *Unicode Technical Standard #39: Unicode Security Mechanisms*, version 18.0.0, revision 34, 27 August; [versioned text](https://www.unicode.org/reports/tr39/tr39-34.html), especially §4, Confusable Detection.
  - [E] Wagner, Robert A., and Michael J. Fischer (1974), “The String-to-String Correction Problem,” *Journal of the ACM* 21(1): 168–173; [DOI](https://doi.org/10.1145/321796.321811). Edit-distance machinery, not a model of reader confusion.
  - [C] UNESCO Intergovernmental Committee (2015), *Ethical Principles for Safeguarding Intangible Cultural Heritage*, endorsed by Decision 10.COM 15.a; [principles](https://ich.unesco.org/en/ethics-and-ich-00866), especially 1, 4–5, 7–10. Ethical reference adapted here, not a fiction-naming law.
- couples: language — `linguistics/naming-systems.md`, `phonetics-phonology.md`, `morphological-typology.md`, `historical-linguistics.md`, `writing-systems.md`, `language-contact.md`, `politeness-taboo-euphemism.md`; myth/symbol — `myth-symbol/symbolism-synthesis-method.md`, `pantheon-archetypes.md`; era/costume — `culture-material/era-periodization-models.md`, `costume-semiotics.md`, `garment-lexicon-crosslinguistic.md`; sibling — lore-shokunin owns entity identity, canon exceptions, and world-bible admission. Abbreviated filenames belong to the preceding directory; all paths are relative to `corpus/knowledge/`.

## 1. Contract and calibration
- This is a review specification, not a shipped executable gate or evidence that a live canon was searched. Its findings concern only the supplied snapshot and declared review scope.
- Verification date: 2026-10-17. Book identities were checked against publisher/Crossref metadata; [S], [U15], [U39], and [C] were inspected as accessible texts. No uninspected passage is quoted or given invented page numbers.
- All thresholds and verdict rules below are **craft policy**, not conclusions established by the cited scholarship.
- **Unique identifiers are mandatory; unique human-readable names are not.** Namesakes, reused place names, theophoric names, and shared titles need explicit relationships rather than automatic renaming [N].
- Compare every proposed name against all entity classes, not just its own: persons, places, peoples, languages, deities, cults, eras, offices, artifacts, garments, and named symbols.
- “All canon” means lore's supplied inventory plus its declared coverage: historical names, aliases, translations, obsolete spellings, and unpublished reservations. An incomplete inventory cannot prove global uniqueness.
- Each individual check returns PASS, FAIL, or HOLD. REVIEW means a retrieved hit still needs examination; it cannot count as PASS. The aggregate success state is PASS-TO-HANDOFF.

| Verdict | Meaning | Required action |
|---|---|---|
| FAIL | A demonstrated identity ambiguity, rule violation, or unresolved prohibited use | Repair or request a specific owner decision; rerun affected checks |
| HOLD | Missing inventory, pronunciation, derivation, relevant expertise, or required cultural review | Record the missing evidence; do not relabel uncertainty as a pass |
| PASS-TO-HANDOFF | Each check has evidence, with any exception approved by its owner | Send the package to lore; this is not canon status or legal clearance |

## 2. Required input records
- Freeze the inventory revision/digest, proposed-name batch, language-profile revision, and review date. Include proposals in pairwise comparisons with one another.
- Preserve the original written form; generate comparison keys beside it, never instead of it.

| Record | Minimum fields | Missing-field consequence |
|---|---|---|
| Entity | stable `entity_id`, class, culture, locale, era interval, canon/proposal status | HOLD: cannot decide whether a match means identity or coincidence |
| Name use | `name_id`, entity link, native script, display form, language stage, dialect, register, use interval | HOLD: apparent duplicates may be stage or register variants |
| Alias relation | endonym/exonym, translation, abbreviation, epithet, former name, namesake, disputed identification | Do not merge entities merely because their labels match |
| Sound | phonemic form `/…/`, syllabification, stress/tone/length where contrastive, orthographic reading rules | HOLD phonology; a romanization is not a pronunciation [P] |
| Formation | lexeme IDs, morpheme boundaries, rule IDs/order, gloss, borrowing history or explicit opacity | HOLD derivation if evidence is needed but absent |
| Social license | naming authority, lifecycle slot, who may utter/write it, taboo conditions, title versus personal name | HOLD when the proposed use crosses an unreviewed restriction |
| Review scope | relevant real languages/communities, source editions, consulted reviewers, accessible versus restricted evidence | No unbounded “cross-culture clear” claim |

## 3. Historical-reference card: keep the coupled culture visible
- For any civilization used as a reference, complete this card for a **region, social group, and dated period**, not a timeless civilizational essence. This entry does not supply civilization digests.

| Coupled system | What the reviewer needs | Collision or provenance trap |
|---|---|---|
| Language family + writing | supported family/branch, historical stage, script, transliteration, literacy context | Shared script is not shared language; unattested sounds are `(to-verify)` |
| Mythic/pantheon core | local divine names/epithets, cult setting, variant traditions; non-pantheonic systems if applicable | A translated epithet need not identify the same deity |
| Symbolic system | local emblem/rebus readings, permitted users, competing interpretations | Similar emblem or gloss is not evidence of cultural identity |
| Era model | dated attestations, emic era labels, modern periodization, renaming/reform events | A late chronicle can retroject names into an earlier age |
| Costume/material signature | dated garment terms, fibers, manufacture, rank/ritual uses, inscription medium | A shared garment label need not mean identical cut or status |
| Naming practices | name slots/order, assignment authority, life-stage changes, namesake/avoidance rules | Do not impose hereditary surnames, binary gender slots, or one lifetime name |

## 4. Gate A — uniqueness across the inventory
1. Index every active and historical name use by entity ID; retain era, language, and relation labels in the index.
2. Run exact comparisons first, then broader candidate-retrieval keys below. Search retired/reserved labels too; they are findings, not automatically permanent bans.
3. Compare across classes and within the proposed batch. A deity, city, and cloth can share a word intentionally; the reader-facing reference must still be resolvable.
4. Classify each hit: same entity/alias, intentional reuse, accidental duplication, unresolved identity, or harmless surface resemblance.
5. Record how references will disambiguate a permitted reuse: qualifier, map label, title, glossary cross-link, scene introduction, or locale-specific usage.

| Comparison layer | Procedure | What a match establishes |
|---|---|---|
| Exact | Original code-point sequence | Same written sequence only |
| Canonical Unicode | NFC under pinned Unicode data [U15] | Canonically equivalent sequences, not the same referent |
| Case policy | Apply the declared language/display casing rules to NFC keys | Possible case-only ambiguity; no universal English lowercasing rule |
| Spacing/punctuation | Retrieve variants with declared separator substitutions | Review candidates; an apostrophe may encode a phoneme or boundary |
| Compatibility | Separate NFKC retrieval key [U15] | Compatibility overlap; never silently replace the stored name |
| Diacritic reduction | Optional broad retrieval key, labeled lossy | Possible rendering collision; tone/length distinctions remain real |
| Transliteration | Compare each declared scheme and common localized display form | A collision in that output channel, not native-script identity |
| Confusable skeleton | UTS #39 procedure/data version [U39] | Potential visual confusion; not linguistic equivalence |
| Spoken form | Compare phonemic keys within stage/dialect; compare approved adaptations across languages | Homophony or near-homophony under stated reading rules |

- Preserve meaningful joiners, combining marks, and script distinctions. Flag unexpected controls, mixed scripts, and missing glyphs for inspection; do not delete them indiscriminately.
- Different entity IDs with the same unqualified display/reference key: FAIL until a disambiguation or intentional-reuse decision is recorded. Multiple aliases of one entity are not duplicate entities.
- Shared roots, rhyming endings, and inherited name elements are not failures by themselves; coherence would disappear if every resemblance were banned.

## 5. Similarity triage: retrieval is not a verdict
- Use Wagner–Fischer insertion/deletion/substitution distance [E] on declared units: graphemes for display, phoneme tokens for sound. Never count UTF-8 bytes as letters.
- Craft default: review exact phonemic matches, edit distance ≤1, and shared distinctive beginnings/endings among prominent names. For longer names, optionally retrieve distance ≤2; pin the chosen threshold before review.
- These are recall-oriented heuristics, not validated confusion cutoffs. Single-letter names, tone-only contrasts, and transliteration mergers need separate attention regardless of threshold.
- An English-specific phonetic code is not a multilingual pronunciation model. A visual confusables skeleton is not a transliterator [U39].
- Run channel tests: two names on a map; a roll call without spelling; a conversation using short forms; and names embroidered/carved in the actual display style.
- Record the tested audience and channel. A native-language contrast can be valid while the localization needs qualifiers; do not simplify the language to conceal a translation problem.

## 6. Gate B — pronounceability under the named phonotactics
- **Question:** can the declared stage/register generate this sound form? Not “can an English reader say it?” Inventory, syllable template, and distribution restrictions are separate inputs [P, S].

| Check | Evidence to inspect | Failure signature |
|---|---|---|
| Segment inventory | Phoneme sequence and grapheme-to-sound mapping | A decorative letter introduces an unlicensed sound |
| Syllable structure | Legal onset/nucleus/coda, cluster restrictions, word-edge conditions | A template permits CVC, but this particular coda is illegal |
| Distribution | Harmony, co-occurrence bans, hiatus, boundary-sensitive processes | Individually legal syllables form an illegal word |
| Prosody | Stress assignment, tone melody, vowel/consonant length, weight rules | Written variants accidentally erase a contrast or break a name-class rule |
| Connected use | Address, possessive/case forms, clitics, titles, ritual formulae | Citation form passes but an obligatory inflection cannot be formed |
| Variant stratum | Dialect, loan, archaic/liturgical register, or deliberate foreign form | “Ancient” becomes a blanket excuse without its own profile |

- Syllabify sound tokens, not spelling. Test the entire word after morphological and loan-adaptation rules, including cross-boundary clusters.
- A loan may retain exceptional phonotactics or adapt to the recipient language; require the selected pathway and comparable examples, not universal assimilation.
- Reading trials measure discoverability of the spelling, not phonological legality. Record mistaken readings and revise the guide or localization where needed.
- No automatic link from consonant clusters to aggression, simple syllables to innocence, or morphology to civilizational advancement is admitted by this gate.

## 7. Gate C — derivational validity
- Use the **derivation/inflection distinction**, productivity, compounding, and allomorphy [M]. A name may be an opaque lexical item; it need not transparently translate into a desired English slogan.
- Audit chain: `lexeme IDs → licensed construction → morphophonology → dated transmission/adaptation → surface sound → script`.
- Keep historical derivation, current speaker analysis, and folk etymology in separate fields. A plausible folk explanation is not a verified historical etymology.

| Formation route | Required witness | Reject this shortcut |
|---|---|---|
| Productive affixation | Stem category/class, affix meaning, selection restrictions, allomorph rule | Attaching a convenient suffix to every root |
| Compound or naming phrase | Head/modifier order, linker/case syntax, special name construction if any | Translating English words individually and preserving English order |
| Non-concatenative formation | Licensed pattern, mutation, reduplication, tone, or stem alternation | Calling arbitrary vowel replacement “root-and-pattern morphology” |
| Inherited/fossil name | Earliest proposed/attested stage, ordered changes, retained irregularity | Reconstructing whatever ancestors are needed to justify a typo |
| Loan/exonym/calque | Donor form, contact era/route, recipient rules; semantic mapping for calques | Borrowing sounds from one language and suffix behavior from another silently |
| Opaque or unanalyzed lexeme | Explicit opacity; provenance/attestation or intentional fictional stipulation | Inventing a confident etymology to fill an empty ledger cell |

- Replay the rule chain independently. If the stated inputs/rules do not yield the candidate, FAIL; do not repair the derivation invisibly.
- Distinct roots may converge through sound change. Log the resulting collision at Gate A rather than reversing the change for one inconvenient name.
- Real-language etymologies without adequate attestations remain `(to-verify)`; sparse evidence can justify HOLD, not certainty manufactured from resemblance.

## 8. Era staging and myth–symbol–costume stress tests
- These are optional design situations, **not a mandatory historical sequence**. Each change needs dates and relevant region/register boundaries.

| Situation | Naming check | Coupled stress test |
|---|---|---|
| Older oral stratum | Separate reconstructed, remembered, and written forms | Is a mythic name preserved in a chant but absent from ordinary address? |
| Contact/conquest | Stage donor and recipient forms; distinguish imposed labels from local use | Does a borrowed garment term or cult epithet reveal the contact route? |
| Script/state reform | Retain former spellings and new official names as linked uses | Can an old seal or embroidered name still be read without merging entities? |
| Religious/rank transition | Record taboo, consecration, office, initiation, or posthumous naming rules | Is a restricted name displayed on clothing to an audience barred from speaking it? |
| Revival/diaspora | Distinguish revived, inherited, reconstructed, and newly coined forms | Is a “traditional” costume label a recent revival rather than evidence of ancient continuity? |

- Match language stage to the inscription's production date, not just the depicted event. A later copy may modernize spelling; a costume can be an heirloom or revival.
- Shared deity epithets, emblem words, clan names, and textile terms require relation notes; do not infer shared ancestry, identical religion, or legal ownership from a match.
- Name-magic is an **in-world proposition**: record who believes pronunciation binds an entity. Whether it actually works is lore's canon decision.

## 9. Gate D — bounded cross-cultural collision review
1. Declare priority languages and communities: direct reference cultures, intended publication/localization audiences, contact neighbors, and any source tradition whose distinctive forms were borrowed.
2. Search native-script and transliterated forms; include pronunciation variants, segmentation, acronyms, abbreviations, and plausible localized readings. Record which searches were actually possible.
3. Check reliable dictionaries and onomastic/reference works; verify serious findings with a relevant speaker/specialist where available. Search-engine snippets and name-generator glosses are leads, not etymological proof.
4. Separate accidental resemblance, attested borrowing, shared origin, translation coincidence, and reader association. Similarity alone establishes none of their historical causes.
5. For living or restricted traditions, use appropriate consultation and respect access conditions [C, principles 1, 4–5, 7–10]. Do not demand protected names as evidence for an audit.
6. Record reviewed languages, dialects, editions/URLs, query variants, date, reviewer remit, findings, and gaps. “No material hit in this bounded sweep” is permitted; “unique in every culture” is not.

| Finding class | Default disposition | Evidence needed for resolution |
|---|---|---|
| Ordinary word/common personal-name resemblance | REVIEW, not automatic rejection | Meaning, pronunciation, frequency/context, audience relevance |
| Slur, obscenity, dehumanizing label, or extremist association | HOLD public-facing use | Reliable usage evidence and qualified contextual review, not an unsourced blacklist |
| Sacred/restricted name, title, ceremonial garment term | HOLD proposed borrowing | Access/usage conditions and appropriate community guidance; public availability is not permission |
| Distinctive historical or living person's name | HOLD implied identification/endorsement | Identity/context check; route rights questions to the responsible owner |
| Recognizable fictional franchise, organization, product, or mark | HOLD unresolved publication risk | Bounded overlap evidence; legal clearance is outside this lane |
| Unknown language, inaccessible evidence, or unsupported gloss | HOLD the relevant claim | Mark `(to-verify)` and name the missing source/expertise |

- The gate does not impose a worldwide veto on ordinary shared syllables. Escalate culturally consequential resemblance, not every dictionary coincidence.
- Reviewers speak to a defined language/community/context, not for an entire civilization; record disagreement rather than fabricating consensus.
- Colonial administrative spellings and missionary transcriptions require source-position notes: who recorded them, when, for whom, and what voices are missing. Do not treat them as an uncontested native standard.

## 10. Constructed regression fixtures — not setting canon
- Toy profile F, invented solely for checking this method: consonants `/p t k m n s l r/`, vowels `/a i u/`; syllables `(C)V(C)` with codas only `/n s/`; no onset clusters; penultimate stress, initial stress in monosyllables.
- Toy morphology: noun `tala` “reed” + productive agent suffix `-in`; delete stem-final `/a/` immediately before this suffix; output `talin`, `/ˈta.lin/`. No other agent suffix is licensed.
- Toy orthography writes phonemes with their shown Latin letters; case is display-only. Fixture records are supplied inputs, not statements about any real language.

| Input/test | Expected finding | Why |
|---|---|---|
| `talin` with the complete stated derivation | B/C PASS | Legal syllables and replayable formation; A/D remain separate |
| `tlina` claimed native to F | `PHON-ONSET`, FAIL | Initial `/tl/` cannot be parsed under the template |
| `talasi` claimed to mean the same agent via `-si` | `DERIV-AFFIX`, FAIL | Pronounceable form, unlicensed formation rule |
| New entity F02 `Talin`; existing F01 `talin` | `NAME-REUSE`, FAIL pending resolution | Same case-policy key, different referents, no qualifier decision |
| F01 also has alias `Talin` | No duplicate-entity failure | Two name uses point to one ID |
| `é` versus `e` + combining acute, comparison-unit fixture | Same NFC key | Canonical equivalence [U15]; no claim about F's inventory |
| Latin `a` versus Cyrillic `а`, visual fixture | `NAME-VISUAL`, REVIEW | Visually confusable glyphs remain different script characters [U39] |
| All toy names lack a real-language sweep | D HOLD | Constructing a string does not establish cross-cultural clearance |

## 11. Handoff and rerun rule
- Deliver a **proposal report** containing snapshot/profile/batch identifiers, coverage declaration, all Gate A–D outcomes, stable finding IDs, evidence pointers, and proposed repairs.
- Each finding records `{finding_id, name_ids, entity_ids, stage, channel, rule_or_source, verdict, resolution_owner, resolution, reviewer, date}`; restrict circulation of culturally protected material.
- Reuse exceptions require lore's recorded identity/disambiguation decision; phonological exceptions require a defined language stratum; cultural restrictions need appropriate evidence, not an author-only waiver.
- PASS-TO-HANDOFF requires resolved FAILs and required HOLDs, evidence for each check, and an explicit bounded cross-cultural result. A broader missing review cannot be hidden as “out of scope” after the fact.
- Rerun on new aliases, entity merges/splits, sound changes, script/transliteration reform, revised costume/cult terms, localization changes, or new relevant cultural evidence. Recheck old hits against the new snapshot.
- Kotodama hands off systems, findings, and options. Lore alone records accepted names and canon identity; nothing in this entry reserves or assigns a name in a fictional world.

## What a worldbuilder can take
- A reusable name-use ledger, replayable formation trace, script/sound collision index, era-aware coupling card, and bounded cultural-review record.
- Deliberate namesakes and historical ambiguity with explicit reader-facing controls, instead of either accidental confusion or implausible universal uniqueness.

## Provenance cautions
- [N, P, M] are scholarly reference anchors, not endorsements of these craft thresholds. Bibliographic verification does not pretend that every chapter was inspected.
- [U15, U39] solve text-equivalence/security problems, not cultural identity; [E] supplies a distance algorithm, not psychological validation. Pin actual implementation/data versions before claiming reproducible results.
- No tradition-specific expertise is claimed here. Where chronicle evidence is scarce, recording is colonial-source-biased, or access is restricted, mark the particular reconstruction `(to-verify)` and retain HOLD on dependent claims.
- Universal symbol dictionaries, sound-to-morality recipes, and “ancient naming law” claims without dated evidence are inadmissible shortcuts, not substitutes for local scholarship. This file makes no new civilization-specific historical claims.
