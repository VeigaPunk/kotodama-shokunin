# Lexicon Coverage Audit — Seven-Field Release Gate

- topic: a reproducible manual gate for semantic-field coverage against the seven field briefs, derivational consistency, frequency discipline, and coherent loanword layers; release means a usable design proposal, never established canon
- sources: Haspelmath & Sims (2010), *Understanding Morphology*, 2nd ed., Hodder Education; List, Cysouw & Forkel (2016), “Concepticon: A Resource for the Linking of Concept Lists,” *LREC 2016*, 2393–2400; Rzymski et al. (2020), “The Database of Cross-Linguistic Colexifications, reproducible analysis of cross-linguistic polysemies,” *Scientific Data* 7:13; Haspelmath & Tadmor, eds. (2009), *Loanwords in the World's Languages: A Comparative Handbook*, De Gruyter Mouton, and *World Loanword Database*; Haspelmath (2009), “Lexical borrowing: Concepts and issues,” therein, 35–54; Gries (2008), “Dispersions and adjusted frequencies in corpora,” *International Journal of Corpus Linguistics* 13(4):403–437; Campbell (2013), *Historical Linguistics: An Introduction*, 3rd ed., Edinburgh University Press
- couples: language — `corpus/knowledge/linguistics/{semantic-fields-lexicon-building,morphological-typology,phonetics-phonology,historical-linguistics,language-contact,naming-systems,writing-systems,sociolinguistics-registers,semantics-pragmatics}.md`; myth/symbol — `corpus/knowledge/myth-symbol/{symbolism-synthesis-method,ritual-liminality,color-symbolism}.md`; era/costume — `corpus/knowledge/culture-material/{era-periodization-models,textile-technology,ritual-garments,garment-lexicon-crosslinguistic}.md`; sibling — lore-shokunin receives proposals and findings, owns the world bible and canon decisions
- verified-at: 2026-10-17 — round-8 metadata pass: header fields and cross-reference resolution checked; 6 linked locators re-checked for resolution (5 reachable, 1 blocked by remote server); sources not re-inspected.
- recheck: when the field briefs, the source lists (Concepticon/CLICS/WOLD), or the declared language stage, dialect, or register set change.

## 1. Scope, evidence, and verdict contract

- Audit the proposed lexicon for one declared language-stage, dialect, and register set; do not collapse a language family's entire history into one dictionary.
- The seven fields are **body, kinship, weather, landscape, subsistence, war, religion**, from `semantic-fields-lexicon-building.md` §4; costume and trade are cross-field extensions, not replacements.
- This document specifies a manual domain gate, not an implemented validator or a registered fleet runtime gate. An auditor must execute the checks and preserve the evidence before claiming a result.
- Four independent verdicts: **C** coverage, **D** derivation, **F** frequency discipline, **L** loan layers. One strength cannot compensate for another failure.
- Overall: any known blocking defect → `failed`; otherwise any required evidence missing → `could-not-evaluate`; only all four clean → `clean`. Advisory findings remain visible.
- `clean` certifies consistency with the declared design and tested uses, not naturalness, historical truth, or permission to record canon.
- All numerical floors, sampling rules, and blocking conditions below are **project acceptance policies**, not cross-linguistic universals or thresholds supplied by the cited scholars.
- Freeze input identifiers and content digests, audit date, reviewer, rule version, exclusions, and expected outcomes; changing inputs invalidates the old verdict.

## 2. Required inputs and counting units

| Input | Minimum usable record | Stop condition |
|---|---|---|
| Culture brief | Ecology, institutions, social groups, required scenes, intended depth by field | No context for deciding whether a gap matters |
| Coupling brief | Family/design ancestry and writing; mythic agents or explicit non-theistic model; symbols; era model; costume/material signature; naming practices | A label such as “ancient culture” stands in for these decisions |
| Lexicon snapshot | Lexeme ID, sense ID, forms, pronunciation, definition, usage example, stage, dialect, register, route, evidence status | Gloss-only word list cannot resolve meaning or usage |
| Grammar snapshot | Word-building constructions, restrictions, phonotactics, inflection, orthography/transliteration policy | Auditor has to invent rules to explain the entries |
| Era/contact ledger | Relative event order, donor and recipient stages, channels, speakers, technological availability | Loan history supplied only as “foreign, long ago” |
| Requirement/sample manifest | Predeclared semantic needs and sample tasks; text IDs, provenance, lengths, tokenization and annotation policy | Denominators or testing criteria change to rescue a result |

- Count **roots**, **lexemes**, **senses**, **surface forms**, and **running tokens** separately. Ten inflected forms do not demonstrate ten lexical contrasts (Haspelmath & Sims 2010).
- A compound can be a lexeme; a productive phrase can satisfy a communicative need without becoming a dictionary headword. Record which is being counted.
- Record polysemy as linked senses of a lexeme; homophones need distinct lexeme IDs. Spelling variants and transliterations must not inflate either inventory.
- Use Concepticon mappings as comparison aids, with dataset version and concept definition; use local IDs for culture-specific concepts. English gloss identity is not semantic equivalence (List et al. 2016).
- Record real-world reference claims separately from fictional proposals: `attested`, `reconstructed`, `contested`, `design-choice`, or `(to-verify)`; a believable invented etymology is still a design choice.

## 3. C — Seven-field coverage matrix

Read from intended **meaning to expression** (onomasiology), then back from expression to licensed senses (semasiology). The second pass catches an attractive word reused for incompatible jobs.

| Field | Needs to test, adapted to the brief | Coupling probe | Typical false coverage |
|---|---|---|---|
| Body | Parts and boundaries; injury/state; sensation; possession and spatial expressions | Distinguish a proposed soul-organ doctrine from the ordinary anatomical sense; test a garment's body location | A list of organs with no way to say “my hand hurts” |
| Kinship | Address/reference; generation; affinity; sibling/cousin contrasts actually required; adoption or household relations if relevant | Test inheritance, mourning dress, and ancestor address without equating every relation with biological descent | English kin labels merely respelled; social rules inferred from one term |
| Weather | Conditions and events; duration/intensity; seasonal or travel-relevant distinctions | Translate a weather warning and a festival/weather association; keep literal and ritual readings distinguishable | Counting every productive snow compound as a basic root |
| Landscape | Terrain/water categories; routes; orientation; resources and inhabited places | Derive or interpret a place-name and give usable directions; separate sacred geography from physical description | Decorative toponyms but no way to locate a ford |
| Subsistence | Obtain, grow, process, preserve, distribute, eat; locally important organisms/materials | Connect labor and food to seasons, offerings, textile fibers, and exchange where the brief requires them | Many crop nouns but no verbs for preparing or sharing food |
| War | Threat, force, defense, negotiation, peace; equipment/organization appropriate to the stage | Test a command, surrender or refusal, and the names of armor/rank insignia if present | Imported officer titles in a brief with no such institution |
| Religion | Ritual acts/roles; sacred or non-theistic concepts; taboo/replacement; reported belief and disagreement | Connect a rite, epithet, emblem, and garment to speaker/occasion; distinguish a deity's name from a title | A pantheon list with no language for prayer, doubt, prohibition, or practice |

- Every field gets a review row, including low-salience fields. Do not require equal field sizes, a pantheon, a standing army, or any particular kinship typology.
- For each field, predeclare needs spanning referents, actions/states, and relations/context where applicable; nouns alone do not prove practical coverage.
- Assign `critical` to needs required by the requested scenes, naming pipeline, or load-bearing cultural coupling; assign other needs `supporting` before inspecting the inventory.
- A culture lacking a technology can mark its specific terms not applicable; that does not exempt vocabulary for encountering, rejecting, or describing it if a required scene needs that ability.
- For each need record `need ID → field → context → expression IDs/construction → example → back-translation → reviewer finding`.
- Accepted realizations: simplex, compound, derivation, contextual colexification, conventional multiword expression, or grammatical periphrasis; no dedicated root is compulsory.
- A periphrasis passes only if its components and construction exist, preserve the needed contrast, and fit the stated speaker/register; “can explain it somehow” is not evidence.
- Colexification is a design option, not a permission slip from a database: inspect definitions and actual contexts. CLICS shows comparative patterns, not mandatory synonymy or every language's full inventory (Rzymski et al. 2020).
- Mark a need `covered`, `gap`, `unevaluated`, or `excluded-with-reason`; exclusions require reviewer acceptance and cannot remove critical obligations.
- Per-field coverage: `C_f = covered applicable needs / all applicable needs`; gaps and unevaluated needs remain in the denominator. Report counts beside fractions.
- If no needs apply, report `N/A` with the brief-based reason, never 100%; an omitted field is unevaluated, not N/A.
- **C clean:** all applicable declared needs covered, every critical task demonstrated, every field reviewed, and every exclusion justified. Report imbalance as advice, not automatic failure.
- A named core list can supply additional checks, but pin its exact edition/mapping; passing that list does not replace these fields or establish a universal vocabulary size.

## 4. D — Derivational consistency and licensed irregularity

Basis: distinguish inflection, derivation, compounding, lexicalization, and analogy rather than forcing all words into affix chains (Haspelmath & Sims 2010; Campbell 2013).

| Check | Evidence to inspect | Blocking finding ID |
|---|---|---|
| Route completeness | Each lexeme is marked inherited, underived design root, derived, compound, borrowed, calqued, or explicitly unresolved | `D-route-missing` |
| Construction signature | Base class/meaning → output class/meaning; argument structure, order, stress/tone, allomorphy, restrictions and productivity | `D-rule-underspecified` |
| Reproduction | Rebuild each claimed transparent derivative from its recorded bases and ordered operations | `D-form-mismatch` |
| Meaning composition | Demonstrate the intended reading; any noncompositional residue has a lexicalized sense/history note | `D-meaning-mismatch` |
| Stage eligibility | Bases and construction exist at the claimed formation stage; subsequent changes applied in order | `D-stage-mismatch` |
| Exception accountability | Analogy, suppletion, taboo replacement, fossilization, or dialect mixture explains an exception within its recorded scope | `D-exception-unlicensed` |

- Do not require every word to be synchronically analyzable. An opaque inherited root is not defective for lacking a recoverable real-world etymology.
- A historical derivation and a modern speaker's analysis are different records; folk etymology may be an in-world belief, not the designer's proven history.
- Tag constructions `productive`, `restricted`, or `fossilized`; give the eligible base set or restriction. Productivity is not simply the number of listed derivatives.
- Project diagnostic: for each claimed productive construction, test a held-out eligible base plus a declared boundary condition (base class, interpretation, or ordering); preserve expected outcomes before derivation. If unrestricted within its domain, record that scope rather than inventing an excluded base.
- A restricted construction needs an eligible context and a demonstrated boundary; a fossilized construction requires its inventory, not a promise of unlimited new formations.
- “Synthetic” does not license arbitrary long strings; “analytic” does not prohibit compounding, derivation, or productive phrases. Audit the particular construction, not a typological stereotype.
- Homophony and synonymy are not automatic errors. Check ambiguity in the required context; document register/domain differences where a contrast is claimed.
- Run the same process over personal, place, divine, and garment names; opaque or preserved name-forms need their own stage/register explanation, not exemption by prestige.
- **D clean:** all recorded formation claims reproduce within their scope; exceptions are explicit; held-out tests agree with the declared productivity limits. Record checks over the whole snapshot separately from diagnostic samples.

## 5. F — Frequency discipline, not frequency theatre

Gries (2008) supplies the central distinction: an item's aggregate frequency and its distribution across corpus parts are different evidence. A ritual refrain is not a sample of everyone's everyday speech.

| Frequency claim | Required evidence | Prohibited shortcut |
|---|---|---|
| “Common in ordinary speech” | Declared speech contexts, independent text/speaker units, token count and distribution | Rank in an alphabetic glossary or a prayer anthology |
| “Specialist/ritual” | Register label and usage contexts; note whether speakers know it but seldom say it | Treating rarity in conversation as lexical absence |
| “This construction is productive” | Type diversity and held-out rule tests, distinct from repetitions | One very frequent derivative treated as unrestricted productivity |
| “This era uses the loan more” | Comparable stage/register sampling and a stable counting unit | Comparing one early inscription with a later dictionary |

- Store `frequency_status = projected | observed-in-authored-sample | attested-reference | unknown`; never relabel generated text as independent linguistic attestation.
- Before texts exist, projected common/specialist/archaic bands with a rationale are acceptable design inputs; numeric frequency and dispersion remain `not measured`, not zero.
- Such a lexicon may pass **frequency discipline**, but not an empirical usage claim. If measured usage is an explicit delivery requirement, missing samples yield `could-not-evaluate`.
- Keep core/function expressions and ordinary actions in the sampling plan; cultural salience is not identical to token frequency. A rarely uttered divine name may be culturally central.
- Project scene suite: for each field, include an ordinary communicative task and a relevant marked context; where no marked register is designed, use a different interlocutor or situation.
- Add an integrated task: identify a garment/material, who wears it and when, its name/epithet, and a relevant symbolic or ritual reading. Keep mundane description available.
- Translate without adding vocabulary mid-run; log every forced coinage, circumlocution failure, or register repair as a new coverage finding and rerun after revision.
- An authored suite tests usability; it cannot independently prove the language's natural distribution. Record author/prompt provenance and duplicated templates or refrains.
- Publish the token boundary policy for clitics, incorporated forms, compounds, punctuation, and multiword units; map surface forms to lexeme IDs while preserving ambiguities.
- Report raw `n(w)` and denominator `N`; a normalized display such as `1000 × n(w)/N` is a rescaling, not more evidence. Define any overlapping multiword counts separately.
- For nonoverlapping corpus partitions, also report range `parts containing w / all parts`, with partition sizes and labels; one occurrence in every tiny part is not robust generality.
- Optional dispersion diagnostic: `DP(w) = 0.5 × Σ_i |n_i(w)/n(w) − N_i/N|`, for `n(w) > 0` and positive-size partitions; lower means occurrence shares track corpus-size shares more closely (Gries 2008).
- If `n(w)=0`, DP is undefined; with only one partition it is uninformative. Always show the underlying counts; partition choice and small samples limit interpretation.
- Do not impose one DP cutoff, an exact rank-frequency slope, a minimum number of synonyms, or an English frequency ranking as a natural-language pass rule.
- Suspected oversupply: many near-synonymous prestige terms with no contrasting use while required everyday tasks fail. Flag the missing uses, not an invented universal noun/verb ratio.
- **F clean:** projected and measured claims remain distinct, counting policies and sample provenance are explicit, every asserted measurement reproduces, and no frequency claim exceeds its evidence.

## 6. L — Loanword-layer coherence

Haspelmath (2009) separates borrowing concepts and mechanisms; WOLD records expert judgments and uncertainty. Neither supplies a compulsory borrowing percentage for a fictional culture.

- Each proposed layer records donor language **and stage**, recipient stage, intermediary if any, channel, social carriers, affected fields/registers, and a relative chronological window.
- Each borrowed lexeme links to that layer and records donor form/sense, adaptation route, semantic change, grammatical integration, later recipient changes, and confidence/evidence status.
- Separate material borrowing, loan translation/calque, semantic extension, hybrid formation, quotation/code-switching, and established lexical borrowing; not every foreign-looking token belongs in the loan inventory.
- Unknown donors can be explicitly unresolved; a required layer whose coherence depends on that missing information is unevaluated, not silently assigned to a convenient neighbor.

| Layer test | Pass evidence | Failure/advice distinction |
|---|---|---|
| Contact opportunity | Speakers/texts and a route linking the relevant stages | Declared history rules out the required route → `L-contact-unsupported`; unknown route → unevaluated; a garment name alone does not prove conquest |
| Phonological integration | Consistent substitutions, repairs, prosody, or licensed retained foreign contrasts by subgroup/channel | Inconsistent with declared adaptation → `L-adaptation-mismatch`; unadapted forms alone are not failure |
| Relative chronology | Entry follows donor availability and precedes only changes it actually undergoes | Impossible event order → `L-chronology-conflict`; insufficient dating → unevaluated |
| Morphological integration | Loan class and behavior under native/borrowed constructions specified | Borrowed base forced through an ineligible rule → `L-integration-mismatch` |
| Semantic/register layering | Literal and specialized senses, carriers, and competing native forms recorded | Doublets need not divide neatly into humble/prestige; unexplained use restrictions are a gap |
| Cultural/material availability | Name, imported referent, local manufacture, and later reinterpretation staged separately | Contemporary referent used before its declared availability → `L-material-anachronism`; unfamiliar known object can still be named |

- Use the chronological pipeline: **donor at entry → transmission/adaptation → recipient at entry → later recipient changes → present form** (Campbell 2013).
- Early loans can undergo later recipient sound changes; later loans can escape changes already completed. Modern donor pronunciation must not be substituted for the donor's borrowing-stage form.
- Reborrowing, spelling pronunciation, learned restoration, analogy, and dialect mixture can disrupt a simple signature; require evidence or an explicit design mechanism before using one as a rescue.
- First surviving written occurrence is an attestation bound, not automatically a coinage date; oral circulation, scribal conventions, and source survival constrain any chronology.
- Borrowability rankings are comparative tendencies, not prohibition lists. Pronoun or basic-vocabulary borrowing deserves sociohistorical review, not automatic rejection or a mandated conquest narrative.
- Report loan **lexeme share** separately from loan **token share**, by field/stage/register and known versus uncertain status; calques and hybrids need separately stated counting rules.
- Clothing loans can travel with trade, imitation, texts, migrants, or prestige; a borrowed robe word proves neither local textile technology nor the wearer's ethnicity.
- Ritual loans can label dissent, scholarship, or quotation rather than conversion; test the usage before attributing a borrowed pantheon.
- **L clean:** no contradiction in the declared contact/adaptation chronology, every formation claim has a reproducible route, and unresolved etymologies remain visibly unresolved without supporting required claims.

## 7. Era-staging and coupling checks

The stages below are audit coordinates, **not** a universal civilization sequence; registers can coexist and technologies need not arrive in this order.

| Coordinate | Lexical audit move | Material/myth/symbol/name check |
|---|---|---|
| Earlier inherited layer | Keep the earlier lexicon distinct from reconstructed designer forms | A surviving place-name is not proof that later religion/costume already existed |
| Contact/innovation window | Identify loans, native coinages, calques, and newly specialized senses | A new cloth, emblem, institution, or rite can have different adoption and naming dates |
| Codified or liturgical selection | Record chosen spellings, recitation, restricted senses and competing everyday variants | Sacred garment/deity titles may preserve older forms; claim preservation only where specified |
| Later vernacular/reform/revival | Apply changes, replacement, purism or reborrowing with social scope | An archaizing name or costume is a later selection, not uninterrupted survival by default |

- Trace one required coupling chain in both directions: **term/sense ↔ material or social practice ↔ symbolic/mythic interpretation ↔ era/register ↔ naming use**; retain explicit “not applicable” nodes.
- Do not force literal color words to equal symbolic color categories, a garment counter to prove an ontology, or a deity epithet to describe ordinary belief unanimously.
- Disagreement across groups, rival myths, and regional senses may be designed variation; contradiction exists only when incompatible claims occupy the same declared scope without explanation.
- Audit proposals against their own briefs; conflicts with accepted world-bible material are findings for lore-shokunin, not authorization to edit or reconcile canon here.

## 8. Run procedure and adversarial review cases

1. Freeze the inputs and expected task outcomes; pin source editions, database versions and item IDs. Mark absent evidence before judging content.
2. Build the seven requirement rows and exclusions; perform C meaning→expression→meaning checks, then D reproduction and productivity-boundary tests.
3. Execute the predeclared scene suite on the frozen snapshot; retain failed translations. Calculate only the F measurements the evidence permits.
4. Rebuild loan routes and order constraints for L; run the era/costume/myth/name coupling checks, including retained or archaizing forms.
5. Record finding ID, input/item ID, check, expected/observed result, severity, source pointer, repair option and retest scope; preserve disagreement rather than averaging verdicts.
6. After repairs, freeze a new snapshot and rerun affected checks plus the integrated task. Release four verdicts, overall result, unresolved questions and reviewer identity to lore.

These are constructed review cases with expected findings, **not a claim that a tool or a real lexicon has passed them**.

| Deliberate perturbation | Expected result | Protection against false failure |
|---|---|---|
| Duplicate spelling variants and inflected forms to inflate a field | Counts remain separate; missing critical need gives `C-required-gap` | Legitimate distinct lexicalized senses remain countable |
| Replace every kin term with one vague expression that loses a required distinction | `C-contrast-lost` | A genuinely licensed contextual expression retaining the distinction can pass |
| Apply an agent-forming rule to a base excluded by its declared restrictions | `D-rule-violation` | A separately recorded lexicalized exception is tested on its own terms |
| Treat repetitions of one hymn as broadly distributed ordinary speech | `F-provenance-overreach` | Repetition can support a frequency statement about that hymn corpus only |
| Describe invented frequency bands as corpus measurements | `F-measurement-missing` | Explicit projections with rationale remain acceptable where measurements are not required |
| Put a post-change borrowing through a completed earlier sound change without a mechanism | `L-chronology-conflict` | A documented reborrowing, analogy or alternative ordering can change the expected result |
| Leave out an indispensable donor-stage/adaptation record | `could-not-evaluate` for the affected claim | Known contradictions elsewhere still make the overall verdict `failed` |
| License an opaque inherited word and a regular productive periphrasis | No defect merely for opacity or lack of a dedicated root | Verify their actual meanings, usage and stage anyway |

## 9. Provenance, calibration, and known limits

- Checkable access points: [Haspelmath & Sims, publisher](https://www.routledge.com/Understanding-Morphology/Haspelmath-Sims/p/book/9780340950012); [Concepticon documentation](https://concepticon.clld.org/about); [Rzymski et al. 2020](https://doi.org/10.1038/s41597-019-0341-x); [WOLD](https://wold.clld.org/); [Haspelmath 2009](https://doi.org/10.1515/9783110218442.35); [Gries 2008](https://doi.org/10.1075/ijcl.13.4.02gri).
- Campbell (2013), 3rd ed., is the reference for sound change, borrowing, analogy and relative chronology; do not silently substitute exercises or chapter numbering from a different edition.
- When importing a WOLD example, cite the vocabulary contributor and individual record, not only the editors; preserve uncertain borrowing judgments. Database samples are not all-language laws.
- Concepticon comparison sets and CLICS colexifications are analytical resources, not culture-free semantic atoms; inspect source glosses, coverage and language-specific descriptions before extrapolation.
- **Rejected as a gate:** “no word means no thought,” vocabulary counts as civilization rankings, universal symbol dictionaries, and inflated “words for snow” competitions. Derivational/sense-count differences defeat such shortcuts.
- **Contested:** productivity diagnostics, morphological boundaries, semantic category alignment, etymological direction and dispersion interpretations can depend on analysis. Record alternative analyses where they affect a verdict.
- **Colonial-source bias:** a missionary glossary, administrator's list, outsider chronicle, or elite dictionary samples its collectors' interests and access; mark those limits rather than treating missing everyday terms as cultural absence.
- **Thin tradition coverage:** this entry does not verify individual sacred vocabularies, historical costume etymologies, or any civilization's complete lexical history. Verify each proposed real-world example locally; otherwise mark it `(to-verify)` inline.
- **Scarce chronicle evidence:** do not fill undocumented donor stages, oral histories, speakers' beliefs or domestic practices with confident reconstructions. Separate attestation, inference, and fictional invention explicitly.
- An archaeological object without a secure name and a surviving word without a secure referent are different evidential gaps; neither automatically supplies the missing half of the costume/era link.

## 10. What a worldbuilder can take

- A lexicon becomes usable when the culture's required distinctions can be expressed and understood, not when its headword count reaches an impressive round number.
- Reuse derivational constructions, contextual senses, contact channels and relative chronology as generators; let unequal field depth reflect the brief without claiming it proves a people's mind.
- Hand off the frozen design inputs, seven-field matrix, derivation routes, sample tasks/results, projected/measured frequency ledger, loan layers and unresolved findings; label all proposed forms and histories as proposals.
- Final provenance caution: this gate tests the **method and reference package**. Lore-shokunin decides what enters the world bible; no audit verdict here establishes fictional canon or real-world ethnographic fact.
