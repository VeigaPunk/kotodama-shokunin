# Internal Consistency Audit — Coupling Graphs, Terminology Sweeps, and Contradiction Triage

- topic: audit the cross-file coherence of linguistic-cultural design methods and candidate handoff packets; expose missing couplings, misaligned terms, incompatible assertions, and unsupported repairs without deciding world-bible canon.
- sources: Thomas R. Gruber (1993); Alistair Miles and Sean Bechhofer, eds. (2009); Luc Moreau and Paolo Missier, eds. (2013); Holger Knublauch and Dimitris Kontokostas, eds. (2017); triage round-2 additions (2026-10-17; web-verified): David Hackett Fischer (1970), Steven A. Greenberg (2009), David-Antoine Williams (2023/24), TEI P5 ch. 22 (TEI Consortium, release version consulted), the Leiden/EpiDoc editorial conventions (Brill TEI–EpiDoc documentation), Bradley Dowden, “Fallacies” (*Internet Encyclopedia of Philosophy*), John Kausch (2023), Sami Honkasalo (2011); full references and limits below.
- couples: language (`../linguistics/`) / myth and symbol (`../myth-symbol/`) / era and costume (`../culture-material/`); especially naming, historical linguistics, writing, symbolic synthesis, periodization, textiles, ritual dress, and material inference; siblings: lore-shokunin receives findings and owns canon verification; chousa-shokunin receives unresolved source-research questions, neither sibling is edited here.
- verified-at: 2026-10-17 — round-8 metadata pass: header fields and cross-reference resolution checked (couples targets are directory-level references and all resolve); 13 linked locators re-checked for resolution (11 reachable, 2 blocked by remote servers); sources not re-inspected.
- recheck: when a coupled entry is renamed or re-scoped, a new contradiction class is added, or before a finding is promoted into a repair.

## Scope, authority, and calibration

- **Object of audit:** this lane's reference methods, design constraints, and proposed cultural-system packets, not the sibling world bible. A finding is a question or proposed repair, never a canon ruling; see `../../../PROVINCE.md`.
- **Consistency is not truth.** An internally coherent etymology can be historically false; an inconsistent chronicle can accurately preserve disagreement. Run provenance checks independently of coherence checks.
- **Consistency is not uniformity.** Polysemy, competing cosmogonies, divergent ritual practice, multilingual names, and changing costume codes are not defects merely because a table prefers one value.
- The couples graph, obligations matrix, severity levels, and release conditions below are **local craft conventions**, not published anthropological laws or a validated measure of cultural complexity.
- Keep three assertion layers separate: `reference-evidence` about real sources; `design-rule` selected for a fictional system; `candidate-in-world` statements awaiting lore's disposition. Add `reported-belief` or `prescription` where appropriate.
- A source's existence does not verify every claim attributed to it. Cite edition plus page, section, inscription/catalogue number, or stable passage when promoting a reference claim; an unresolved locator is `(to-verify)`.

## Source basis and limits

- **Gruber, Thomas R. (1993).** “A Translation Approach to Portable Ontology Specifications.” *Knowledge Acquisition* 5(2): 199–220. [Author's bibliographic page and abstract](https://tomgruber.org/writing/ontolingua-kaj-1993/). Basis: explicit shared vocabulary and relations; not evidence that cultures possess one closed ontology.
- **Miles, Alistair, and Sean Bechhofer, eds. (2009).** *SKOS Simple Knowledge Organization System Reference*. W3C Recommendation, 18 August 2009. [Dated standard](https://www.w3.org/TR/2009/REC-skos-reference-20090818/), §§5, 8, 10. Basis: lexical labels, notes, and concept mappings; concept equivalence is not cognacy or identical spelling.
- **Moreau, Luc, and Paolo Missier, eds. (2013).** *PROV-DM: The PROV Data Model*. W3C Recommendation, 30 April 2013. [Dated standard](https://www.w3.org/TR/2013/REC-prov-dm-20130430/), §§2, 5. Basis: entities, activities, agents, and derivations; provenance records responsibility and dependence, not reliability by itself.
- **Knublauch, Holger, and Dimitris Kontokostas, eds. (2017).** *Shapes Constraint Language (SHACL)*. W3C Recommendation, 20 July 2017. [Dated standard](https://www.w3.org/TR/2017/REC-shacl-20170720/), §§3–4. Basis: validation against explicit graph conditions and diagnostic results; no RDF implementation or SHACL conformance is claimed here.
- **Fischer, David Hackett (1970).** *Historians' Fallacies: Toward a Logic of Historical Thought*. Harper & Row, p. 47. Basis: the fallacy of the negative proof — “there is no evidence that X is the case” cannot license the conclusion “not-X”; consulted as quoted verbatim at p. 92 of Vermette, “Rejecting the Standard Discourse on the Dispossession of Métis Lands in Manitoba,” *aboriginal policy studies* 6(2) (2017): 87–119 ([open access](https://journals.library.ualberta.ca/aps/index.php/aps/article/download/28227/pdf/77588)), not as an inspection of Fischer's book. Supports “a missing chronicle is not proof of absence.”
- **Greenberg, Steven A. (2009).** “How citation distortions create unfounded authority: analysis of a citation network.” *BMJ* 339: b2680, [DOI](https://doi.org/10.1136/bmj.b2680); abstract and figure captions read via [PubMed 19622839](https://pubmed.ncbi.nlm.nih.gov/19622839/) on 2026-10-17. Basis: in a 242-paper, 675-citation network, citation bias, amplification, and “conversion of hypothesis to fact through citation alone” produced unfounded authority; a source's existence and citation count therefore do not verify what is attributed to it.
- **Williams, David-Antoine (2023/24).** “Antedating (in) the Oxford English Dictionary.” *Notes and Queries*, advance access 30 November 2023, [DOI](https://doi.org/10.1093/notesj/gjad106) (open access; author-hosted PDF read 2026-10-17). Basis: OED3 revised earliest dates downwards for 38–44 per cent of revised entries in the early 2000s; a first attestation records the earliest evidence found so far, not an origin event.
- **TEI Consortium (release version consulted 2026-10-17).** *Guidelines for Electronic Text Encoding and Interchange (TEI P5)*, ch. 22, “Certainty, Precision, and Responsibility.” [Release documentation](https://www.tei-c.org/release/doc/tei-p5-doc/en/html/CE.html). Basis: graded `certainty` (`locus`, `degree`), numerical `precision`, and per-element `respons` are distinct encodings — responsibility for a judgment is not the degree of confidence in it; the chapter likewise separates certainty about markup from confidence in a factual assertion.
- **Leiden conventions / EpiDoc (Brill TEI–EpiDoc documentation, read 2026-10-17).** [Page](https://brillpublishers.gitlab.io/documentation-tei-xml/epidoc.html). Basis: epigraphic and papyrological editions mark uncertainty at the smallest unit — ambiguous letters with underdots, restorations in square brackets, tentative restorations with a question mark (`cert="low"`). Caveat carried from the same page: “There is, it seems, not one Leiden system, but many,” so no single canonical mark set is asserted here.
- **Dowden, Bradley (n.d.).** “Fallacies.” *Internet Encyclopedia of Philosophy*, s.v. “Appeal to Authority” ([entry read 2026-10-17](https://iep.utm.edu/fallacy/)), quoting Schwartz (1981). Basis: an appeal to authority is fallacious whenever the cited authority lacks standing in that subject, is misquoted, or authorities disagree — a famous name is not a calibration status. The entry's bibliography records Walton (1997), *Appeal to Expert Opinion* (not inspected in this pass).
- **Kausch, John (2023).** “The ‘Universal’ Rebus Principle and Phonosemantic Compounding.” *Journal of Universal Language* 24(2): 91– ([article read 2026-10-17](https://www.sejongjul.org/archive/view_article?pid=jul-24-2-91)). Basis: the rebus principle is the mechanism by which signs acquire phonological content, and it “obscures the meaning of an image in a code accessible only to those who speak the language it is written in” — a rebus claim is therefore a claim about that language's sounds.
- **Honkasalo, Sami (2011).** “A Cognitive Approach to Character Formation in the Oracle Bone Script.” *Tokyo University Linguistic Papers (TULIP)* 31: 67–77 ([PDF read 2026-10-17](https://repository.dl.itc.u-tokyo.ac.jp/record/27548/files/ggr031005.pdf)). Basis: the rebus principle borrows an existing symbol “to write a homophonous or near homophonous word,” and its examples rest on pronunciation reconstructed for that stage (the preposition ‘from’ sharing the word for ‘nose’ in Shang Chinese); modern homophony cannot justify a rebus in an earlier stage.
- The knowledge-representation sources above are **not ethnographic verification**, and neither are the round-2 verification-method additions. No tradition-specific chronicle or costume corpus was examined for this method; contextual source work remains necessary before using a real civilization as reference.
- **Verification boundary (round-2 triage, 2026-10-17).** The five to-verify tokens in this entry are use-mention definitions of the lane's own mark and of the audit actions that place it, not reference claims; all five are retained and no mark was removed, since the triage outcomes apply to claims. This pass verified the method basis behind them, listed above; ledger at `../../lessons/round-2-triage/V04.md`.

## Establish the audit unit and assertion record

1. Freeze the authorized input inventory: relative paths, content digests or immutable revision, included sections, excluded material with reasons, and audit date. A moving tree cannot support a reproducible “all files checked” claim.
2. Read every included `- topic:`, `- sources:`, and `- couples:` field, then inspect the body: front matter declares obligations but cannot establish that the promised coupling actually works.
3. Register **concept IDs separately from words**, and assertion IDs separately from concepts. One concept can have several names; one written form can identify several senses.
4. Record each load-bearing assertion in the following shape; `unknown` is a value requiring review, not a wildcard proving compatibility.

`assertion-id | concept-id | predicate | value/sense | polarity/quantifier | culture/region | valid-time | dialect/register | speaker/context | assertion-layer | file:section | source-locator | evidence-status`

- `valid-time` concerns the claimed state; also record composition, witness/copy, and modern publication dates when relevant. Do not collapse these clocks.
- `evidence-status`: `located`, `inferred` with reasoning, `contested` with competing references, or `unverified (to-verify)`. Keep confidence separate from graph coverage and from lore's approval.
- For sampled rather than exhaustive review, name the sample and selection rule; never report a sampled sweep as a corpus-wide absence result.

## Couples-graph completeness: two layers, not a link count

- **File graph F:** a node is an inventoried file; a directed edge records a declared coupling or substantive body cross-reference. Classify it as `semantic-dependency`, `shared-input`, or `editorial-reference`.
- Resolve explicit file paths and section references. A directory-level coupling requires an enumerated target set in the audit worksheet; a broad category label alone is not a verified edge.
- **Claim graph G:** nodes identify concepts/assertions in language `L`, myth `M`, symbol `S`, era `E`, and costume/material practice `C`; multiple edges may connect the same nodes with different predicates and scopes.
- Each semantic edge records `edge-id | from | relation | to | scope | evidence/assertion IDs | required? | status | finding-id`. Relations must say something testable: `names`, `depicts`, `requires-material`, `restricted-to`, `borrowed-from`, `valid-during`, or a defined alternative.
- A bibliographic reference is not a causal link. A `- couples:` mention is not proof of semantic alignment. Reciprocal file links are useful navigation, not independent corroboration.
- Build obligations from the brief and declared dependencies **before** counting checked edges. Do not invent links merely to make the graph dense.

| Domain pair | Obligation to test when applicable | Existing method surfaces, relative to this file |
|---|---|---|
| L–M | ritual names, taboos, and mythic speech have a derivation and a speaking context | `../linguistics/naming-systems.md`; `../linguistics/politeness-taboo-euphemism.md` |
| L–S | a rebus uses the right sounds/script; color vocabulary is not silently equated with symbolic meaning | `../linguistics/color-terminology.md`; `../myth-symbol/symbolism-synthesis-method.md` |
| L–E | sound change, borrowing, orthography, and register refer to compatible stages | `../linguistics/historical-linguistics.md`; `../linguistics/writing-systems.md` |
| L–C | garment terms distinguish the intended cut, material, wearer, and loan stratum | `../culture-material/garment-lexicon-crosslinguistic.md`; `../linguistics/language-contact.md` |
| M–S | a mythic association names its version/community; motif resemblance is not identity | `../myth-symbol/comparative-frameworks.md`; `../myth-symbol/motif-index-usage.md` |
| M–E | narrative time is distinguished from composition, reception, and retrospective legitimation | `../myth-symbol/myth-folktale-genres.md`; `../culture-material/era-periodization-models.md` |
| M–C | ritual dress has a rite, wearer, occasion, and source of authorization | `../culture-material/ritual-garments.md`; `../myth-symbol/ritual-liminality.md` |
| S–E | symbolic meanings and inversions are versioned rather than projected backward | `../myth-symbol/symbolism-synthesis-method.md`; `../culture-material/calendar-festival-systems.md` |
| S–C | material color, lexical category, emblem meaning, and legal privilege remain distinct | `../culture-material/costume-semiotics.md`; `../culture-material/sumptuary-law-rank-display.md` |
| E–C | local manufacture, import, heirloom survival, and revival fit the stated period | `../culture-material/dress-through-eras.md`; `../culture-material/textile-technology.md` |

- **Path test:** each load-bearing item must reach the domains the brief declares relevant through tested relations, not merely through a bibliography hub. Not every item needs every domain or a complete clique.
- **Orphan test:** isolate terms with no defining sense, symbols with no scoped reading, eras with no boundaries, and costumes with no material or use-context; flag missing support rather than filling it creatively.
- **Cycle test:** mutual dependency can be legitimate; mutual citation cannot bootstrap evidence. Trace every factual support chain to an identified source or explicitly labeled design assumption.
- **Higher-order test:** inspect a language → symbol → costume → era → language path as a whole. A wordplay valid in one language stage may cease to motivate an emblem later; a documented fossil is an option, not an automatic repair.

## Coverage accounting and stop conditions

- Give every expected obligation one state: `checked`, `open`, `blocked`, or `justified-N/A`. `checked` requires a recorded test and result, including a negative result if it raises a finding.
- `justified-N/A` means the obligation does not apply, with an explicit scope reason. Missing evidence, an absent target file, and unfamiliar scholarship are **not** N/A.
- Report disposition coverage as `(checked + justified-N/A) / all obligations`; report checked coverage as `checked / applicable obligations`, where applicable excludes justified N/A. An empty denominator is `N/A`, not a perfect score.
- Show raw state counts and the obligation list alongside either fraction; a checked contradiction must remain visible in the findings tally. Coverage cannot certify correctness.
- Separate `broken-reference`, `missing-coupling`, `unsupported-claim`, and `incompatible-assertions`; fixing a link closes only the first kind.
- Release conditions for an **audit-complete** packet: declared scope reproducible; every obligation disposed; no open/blocked required obligation; no unresolved blocking finding; advisory gaps listed with owners. This is not “canon approved.”
- Record `incomplete` if required inputs were inaccessible or the review stopped early. Do not infer coherence from a search returning no matches.

## Terminology alignment sweep: concepts before replacements

Use SKOS-style preferred/alternative labels and scope notes as an editorial model, not a demand that each language have one universal word per concept.

| Sweep | Compare | Preserve rather than flatten |
|---|---|---|
| Exact forms | spelling, diacritics, capitalization, segmentation, script, and search-normalized variants | phonemic contrasts; raw spelling; intentional scribal variants |
| Concept identity | defining features, referent, sense IDs, and relationship type | homonyms and polysemous senses with separate scoped definitions |
| Naming practices | personal name, epithet, title, patronymic, clan name, endonym/exonym | a divine title shared by several beings; observer labels versus self-names |
| Language family + writing | genealogical classification, contact claims, language stage, script, transliteration | script sharing without common ancestry; a liturgical script versus everyday speech |
| Mythic/pantheon core | deity/ancestor IDs, versions, narrative role, cult/community, reported speaker | incompatible origin narratives as attributed accounts; traditions without a pantheon |
| Symbolic system | sign, meaning, context, allowed transformation, source framework | multivocal symbols; local inversion; emic readings versus analyst categories |
| Era model | period names, interval boundaries, event order, regional chronology | overlapping periodizations and uncertain dates; no universal civilization ladder |
| Costume/material signature | fiber, dye, weave, cut, fastener, access, wearer, occasion | imported cloth versus local manufacture; prescriptive costume versus actual wear |
| Gloss and translation | literal analysis, idiomatic meaning, translator's gloss, technical sense | two terms sharing an English gloss without being interchangeable |
| Source vocabulary | historical spelling, obsolete analytic labels, modern preferred terminology | quoted historical categories clearly attributed, not normalized into present endorsement |

1. Build the label sheet: `concept-id | preferred label by language/stage | alternative labels | definition | scope note | forbidden conflations | occurrences`.
2. Search exact labels across every inventoried file, then curated aliases, transliterations, and morphological variants. Record search strings, file set, tool/version, and results, including inspected zero-hit queries.
3. Use case-folding or Unicode normalization only in a separate search view; preserve originals. Never strip accents or glottal markers and then merge entities automatically.
4. Inspect each candidate in context. Fuzzy matching nominates review candidates; it cannot establish common etymology, semantic identity, or mythic diffusion.
5. Compare both directions: every used term has a definition; every declared alias has occurrences or an explicit reserved status. Reject circular definitions that supply no distinguishing features.
6. Record equivalence as `same-concept`, `near-equivalent`, `broader/narrower`, `related`, or `unresolved`. SKOS `exactMatch` is a strong concept mapping, not a convenient “looks similar” label.
7. Propose scoped repairs and an occurrence list; rerun all affected aliases and neighboring definitions after an authorized change. Do not perform blind global replacement of names or ritual vocabulary.

## Era staging: align the clocks before alleging anachronism

| Clock or stage | Required distinction | Audit question |
|---|---|---|
| Claimed event | when a narrative says something happened | is this mythic time, an interval, or a dated event? |
| Language stage | spoken forms, ritual archaisms, orthography, borrowing | does the proposed derivation operate in this stage, not just the modern one? |
| Composition/redaction | when an account was formulated or revised | is a later ideology being projected into the narrated past? |
| Witness/material survival | surviving copy, artifact manufacture, reuse, deposition | does the object date the practice, or only this instance of it? |
| Reception/translation | later interpretation, revival, editorial naming | is the present label an explanatory gloss rather than an ancient term? |

- Keep relative order if absolute dates are unknown. Record interval bounds and uncertainty explicitly; unknown overlap yields an indeterminate finding, not a proven contradiction or clean bill.
- Check region-specific adoption, continued old usage, loans, ceremonial archaism, and reuse before declaring an error. Each explanation needs evidence or a proposed design decision, not a retrofit asserted as fact.
- Earliest surviving attestation is not automatically invention; a missing chronicle is not proof of absence. Where written evidence is scarce or knowledge of a tradition is thin, mark the inference `(to-verify)` and name the missing evidence.
- Do not infer a society's “era” from a single garment, writing system, or language family. Use the periodization brief and keep technological, political, and linguistic stages distinct.

## Contradiction detection and resolution protocol

A contradiction candidate requires overlapping scopes and incompatible assertions, not merely different strings. Compare subject/sense, predicate, polarity, quantifier, time, region, dialect/register, context/speaker, and assertion layer.

- Positive and negative assertions about the same scoped state conflict; differing values conflict only where the predicate is declared exclusive. Color meaning, deity epithet, and language use are not intrinsically single-valued.
- A universal claim and an in-scope counterexample can conflict; a rule prohibiting an act and evidence that someone performed it need not. Distinguish normative from observed claims.
- Unknown scope blocks adjudication. Different witnesses may disagree without the audit being entitled to decide which account is true.

| Finding class | First diagnostic | Permitted proposal, not automatic canon repair |
|---|---|---|
| Editorial mismatch | same concept and scope, variant caused by transcription or stale reference | normalize a documented label; retain original readings in provenance |
| Sense collision | identical gloss hides different concepts or referents | split sense IDs and clarify definitions |
| Scope collision | region, speaker, rite, social group, or register omitted | narrow only to a scope actually supported; otherwise leave unresolved |
| Diachronic collision | valid-time confused with witness/reception time | version states; identify the change mechanism or flag the gap |
| Framework collision | one file's chosen constraint treated as universal scholarship | label the local rule; present alternatives without silently overriding it |
| Source disagreement | independent evidence supports incompatible readings | preserve attributed alternatives and confidence; request specialist review |
| Genuine design conflict | incompatible candidate requirements occupy the same scope | offer repair options and dependency effects to lore-shokunin |
| Unsupported reconciliation | proposed “secret cult,” borrowing, or revival has no basis | reject the patch as established explanation; submit as a new candidate only |

1. **Open:** assign finding ID; quote the smallest sufficient conflicting passages with file/section and source locators. Preserve originals; collect a minimal conflict set, which can involve more than two assertions.
2. **Normalize:** compare senses and scopes without changing inputs. State the incompatibility rule and whether it is sourced, logical, or a local design choice.
3. **Trace:** follow citations and derivations. Repeated secondary summaries may share one source; count evidence lineages, not repetitions. Separate absence of evidence from evidence against a claim.
4. **Classify:** choose a class above; mark `confirmed`, `candidate`, or `indeterminate`. A hypothesis explaining variation is not confirmation that the variation had that cause.
5. **Evaluate options:** correction of a sourced factual error, explicit scope/version split, retained disagreement, withdrawal of an unsupported claim, or a lore decision. For each, list affected terms, paths, and unresolved dependencies.
6. **Route:** kotodama proposes repairs to its methods/candidate systems; lore owns canon choices and world-bible verification. Unresolved historical sourcing goes to chousa; rights/attribution rulings remain outside this lane.
7. **Record:** finding, evidence, proposed action, owner, disposition, rationale, and any decision pointer. Use `superseded-by` links rather than erasing inconvenient readings; “newest file wins” and source prestige are not adjudication rules.
8. **Re-audit:** after an authorized repair, revisit all dependent graph paths, aliases, era states, and examples. Close only with rerun evidence or an explicit recorded disposition; a pending canon decision stays pending.

## Severity, provenance debt, and evidence scarcity

| Severity | Examples | Required disposition |
|---|---|---|
| Blocking | fabricated/untraceable load-bearing citation; incompatible required design constraints; undecidable required dependency; canon authority claimed | stop the affected handoff; correct, supply evidence, or obtain an owner decision |
| Advisory | nonessential coupling incomplete; bounded translation uncertainty; optional naming variant unresolved | retain finding, impact, owner, and next check; no unqualified completeness claim |
| Informational | supported register difference, documented reuse, deliberate and scoped narrative disagreement | retain the explanation so a later sweep does not “fix” it away |

- Severity follows impact and obligation status, not exoticness or age. A well-cited interpretation may remain contested; a beautiful design is not external evidence.
- Colonial/missionary/administrative descriptions require observer, purpose, translation chain, access, and local counter-evidence fields where obtainable. Do not treat observer vocabulary as the community's own taxonomy or discard a source solely by category.
- Survival is uneven: official texts, elite regalia, and durable media may dominate the record. Flag whose speech, domestic dress, nonelite practice, and oral transmission are missing; do not invent their content to balance the table.
- Do not turn universal symbol dictionaries, a single hero template, or a unilinear “primitive → civilized” ladder into validation rules. Such universalizing premises require independent support; discredited racial/evolutionist rankings are inadmissible as evidence.
- Mark a framework `local design convention`, `supported within stated scope`, `contested`, `discredited claim`, or `unverified (to-verify)` **at claim level**. A famous author's name is not a calibration status.
- Seeded synthesis quotas and single-primary-meaning rules are inspectable design choices, not discovery claims. If chosen constraints clash across files, report the clash; do not rewrite seeded entries or falsely universalize them.

## Abstract audit fixtures: how to apply without creating canon

These are diagnostic inputs, not a fictional civilization, historical claims, or additions to any world bible.

| Input fixture | Expected audit result |
|---|---|
| Same symbol, opposite meanings, different documented ritual contexts | scoped variation; preserve contexts, not an automatic contradiction |
| Garment color forbidden by law; evidence of an unauthorized wearer | prescription and practice can coexist; inspect enforcement/context |
| Rebus justified only by modern homophones in a proposed earlier stage | missing L–S–E support; require historical sound evidence or leave `(to-verify)` |
| Era packet says local production absent; costume packet says imported cloth available | not logically incompatible; check route, period, and intended availability claim |
| Two exclusive material requirements for the same object, region, and interval | conflict set; blocking if required, with alternative repairs for the owner |
| File lists a coupling, but the target contains no relevant definition or test | unresolved semantic obligation even if the path exists |
| A source cannot be located and its claim is essential to a ritual rule | blocked provenance obligation, not justified-N/A or a license to invent |

- For a fictional culture brief, begin with language family/contact basis + writing, mythic/pantheon or non-pantheon core, symbolic repertoire, era model, costume/material signature, and naming practices. Explicitly mark each dimension's applicability and evidence state.
- Trace a load-bearing term through its derivation, mythic use, symbolic reading, wearable/material realization, and period scope; then try a context or era change to see which dependencies fail.
- Counter-test the audit: remove an essential definition, introduce a scoped incompatible assertion, and add a legitimate dialect variant in isolated practice inputs. Expected findings must distinguish missing support, conflict, and harmless difference.

## Handoff checklist and what a worldbuilder can take

- [ ] Scope/inventory fixed; all actual checks named; exclusions and sampling visible.
- [ ] File references resolved; semantic obligations tested; open/blocked/N/A states distinguished.
- [ ] Terminology sheet separates concepts, senses, labels, scripts, translations, and names.
- [ ] Language, myth, symbol, era, costume, and naming dependencies inspected where relevant.
- [ ] Contradictions carry minimal witnesses, incompatibility rules, provenance, and scoped repair options.
- [ ] Thin tradition knowledge, scarce chronicles, contested interpretations, and unverified locators flagged inline.
- [ ] Dependency reruns recorded; blocking findings resolved or affected handoff withheld.
- [ ] Recipient and authority explicit: findings/options to lore-shokunin; no canon writes or silent rulings.

**Take:** a reproducible way to distinguish missing connections from real incompatibility, preserve meaningful cultural variation, and price the consequences of a design change before handoff. **Provenance caution:** graph completeness and tidy terminology certify only the declared audit work; neither establishes historical truth, exhaustiveness of cultural evidence, or acceptance into canon.
