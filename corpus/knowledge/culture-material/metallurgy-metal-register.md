- source: S919 in corpus/SOURCES.md; Encyclopaedia Britannica, 11th edition (1911), Wikisource transcription of Metallurgy; General Sequence of Operations and Fluxes body paragraphs.
  S920 in corpus/SOURCES.md; Iron, opening article-scope and commercial-variety paragraphs (1911).
  S921 in corpus/SOURCES.md; Bronze, first and second body paragraphs (1911).
  S922 in corpus/SOURCES.md; Alloys, opening definition, brass example and manufacturing-method body paragraphs (1911).
- verified-at: 2026-11-04; ordinary HTTP source reads preserved in reports/round-85/evidence/ and independent ReviewerEntry evidence under .ufo/waves/round-85/w1/stage/ReviewerEntry/evidence/.
- recheck: 180d; re-open the four named article bodies, re-locate the quoted spans, and check that the entry attributes technical/historical descriptions to their 1911 witness rather than presenting them as current scientific consensus.

# Metallurgy and the metal register: words for an ore-to-market chain

- topic: ore-to-metal vocabulary as a linguistic-cultural worldbuilding register — distinguish feedstock, preparation, extraction, refining, alloy family, product grade and market name; couple naming to institutions and era changes without treating a metal word as an assay, an etymology as a production date, or a technological label as a universal social stage.
- gap filled: no knowledge basename at the round-85 base owns metallurgy, smelting, smithing, foundry or alloy as a whole naming-chain surface; craft-artisan-lexicon already owns workshop tool words and material grading, while trade-economy-lexicon owns money and market language. The missing craft is a record connecting those narrower owners through ore, intermediate product, named metal, grade and traded object. The absence claim is bounded to the filename sweep in reports/round-85/baseline.json, not absence of metal-related knowledge everywhere.
- sources: the four cited 1911 articles are tier B for their dated technical vocabulary and the distinctions they themselves make. Their ancient-history reconstructions, racial classifications, etymological proposals and industrial examples are not modern archaeological or linguistic authority. This entry does not adjudicate current chemistry or etymology.
- couples: culture-material/craft-artisan-lexicon.md; culture-material/trade-economy-lexicon.md; culture-material/era-periodization-models.md; culture-material/material-culture-inference-method.md; linguistics/semantic-fields-lexicon-building.md; synthesis/loanword-material-dating.md; synthesis/era-language-staging.md; synthesis/worldbible-integration-contract.md.
- scope: reference-grounded generative method for fictional words and institutions; NOT an engineering recipe, furnace construction guide, historical reconstruction, universal metallurgy chronology, real-language-name clearance or world-bible canon. Native forms in an eventual conlang still require the lane's own phonology, morphology, borrowing and naming checks.

## 1. Partial owners and the new surface

The workshop entry remains the owner of tools, apprenticeships, craft speech and the existing material-grading examples. Read `corpus/knowledge/culture-material/craft-artisan-lexicon.md` before inventing a tool synonym or reusing its Japanese swordsmithing vocabulary. A new label such as “heart metal” is not licensed as a historical form merely because that neighbour discusses an attested Japanese distinction. This entry supplies a place for the record in a process chain; it does not duplicate that record's source authority.

The market entry remains the owner of weighing, money, contracts, measures and exchange institutions. Read `corpus/knowledge/culture-material/trade-economy-lexicon.md` when a metal word becomes a unit of account or a coin name survives a change of substance. “Silver” in a transaction may be an accounting expression inside the fictional brief; whether it denotes metal, currency, a value unit or a class of goods must be written, not guessed from spelling.

Periodization belongs to `corpus/knowledge/culture-material/era-periodization-models.md`. An invented E1/E2 distinction here is a pair of local design horizons, not a universal Copper→Bronze→Iron ladder. Word borrowing, artifact import, ore extraction, furnace operation and administrative standardization can occupy different intervals. When those intervals disagree, record the disagreement rather than averaging them into one date.

The source article defines metallurgy as extracting metals from ores and customarily distinguishes commercial from laboratory methods. That is a named 1911 usage boundary, not a timeless claim about every community's word for a metalworker. S919.

The Iron article explicitly confines itself to chemistry and points manufacture, properties and uses to a separate Iron and Steel article. Its title is not evidence that the English word's etymology has been verified. S920.

The Bronze article discusses variable compositions and ambiguous ancient metal words. This licenses a caution about translation and classification, not a declaration that every ancient bronze object has the same ingredients or that Homeric terminology transparently identifies an archaeological alloy. S921.

The Alloys article makes nonuniformity and variable proportion explicit. It supplies a reason to separate a commercial or functional alloy name from an analyzed composition; the name is not the analysis. S922.

**New craft output:** one compact metal-register ledger. Every row has a sense, a process or product referent, the speaker institution that recognizes it, an era interval, the form's language channel, and an evidence status. A fictional metal vocabulary is usable when a writer can decide which row a character means without silently filling the composition field from a familiar English gloss.

## 2. Six design decisions

These are design thresholds, not historical universal laws. The defaults are deliberately conservative: if a needed field is unknown, leave it unknown or hold the derivation rather than producing a false native form.

| decision | options | default and threshold | failure if unset |
|---|---|---|---|
| What kind of referent does the word name? | ore, prepared charge, intermediate metal, refined lot, alloy family, finished object, unit of account | Give each lexeme one explicit primary category; allow a second sense only as a separately indexed row with its own use context. | “Iron” changes from rock to blade to tax unit mid-scene and the reader cannot reconstruct the transaction. |
| Which transformation does a process verb assert? | dressing, roasting, extraction, refining, casting, working, repair | Before adding a verb, specify its input and output categories; do not let one English translation silently merge every transformation. | A culture that only remelts imported feedstock is credited with ore extraction. |
| Does the named material have a fixed recipe? | analyzed composition, allowed range, commercial family, function/appearance name, unknown | Store a composition assertion only with a stated fictional assay or independently sourced historical analysis; otherwise default to family/unknown. | A bell-metal label is treated as a unique chemical formula across centuries and workshops. |
| Who guarantees a grade or name? | maker, guild, merchant, household, ruler's office, assayer, nobody | Name at least one issuing or recognizing institution before the grade can support a legal or rank decision; personal praise defaults to nonbinding description. | A traveller's adjective becomes a legally enforceable quality standard without an institution. |
| What changed between eras? | word form, word sense, supply route, local process, office, object use | Record at least one explicit change and one retained feature; keep word-arrival and referent-arrival intervals in separate fields. | A borrowed word is used to date an invented furnace or an imported artifact proves local production. |
| What may pass to the world bible? | proposed sense record, attributed belief, unresolved evidence, tested derivation | Hand off only typed records with source/design status and unresolved fields; canon status remains not canonized until lore supplies acceptance. | A vocabulary generator turns a proposed technical system or an attributed smith myth into narrator-certified canon. |

A practical minimum is enough: start with an ore term, a prepared-feedstock term, an extraction verb, a refining term, an intermediate-product term and a finished-product term. That six-slot starting inventory is a **craft proposal**, not a report that any real language must lexicalize exactly six stages. One language may use broad verbs plus complements; another may use several inherited technical verbs; a third may borrow a whole occupational register. Preserve the difference between designing such an inventory and asserting an attested one.

When a brief demands “one word for bronze,” ask what its speakers need to distinguish. A merchant may group by sale category, a founder by casting behaviour, a musician by an object's sound, a clerk by accepted payment class. Those are fictional functional choices unless attested for a named historical institution. They may share a form without sharing a material definition. Write a `sense_id` even when the displayed gloss repeats.

## 3. Attested anchors

Each bullet below carries exactly one registered source id and a short body quotation. Locations identify the article paragraph or section, not a plate caption. Interpretive follow-through stays within the dated text's scope. Quotations are whitespace-folded when the served HTML wraps a line; a folded location does not establish modern truth.

- S919: Metallurgy, opening definition: 「the art of extracting metals from their ores」 — the source's technical boundary is extraction, not every act involving a metal object.
- S919: Metallurgy, General Sequence of Operations, first paragraph: 「ore proper and gangue」 — record named material and accompanying matter separately instead of making one undifferentiated “rock” slot.
- S919: Metallurgy, General Sequence of Operations, washing paragraph: 「purify the ore before the liberation of the metal is attempted」 — preparation and extraction need not be the same predicate in a lexical record.
- S919: Metallurgy, paragraph after Wet Processes: 「Few methods of metal extraction at once yield a pure product.」 — an extraction word does not on its own license a purity claim.
- S919: Metallurgy, same refining paragraph: 「requires to be “refined” to become fit for the market」 — the article distinguishes an intermediate product from a market-ready state.
- S919: Metallurgy, Fluxes section: 「Slags are not a necessary evil」 — even waste/product valuations require scope; do not define slag only as accidental dirt when this witness names another function.
- S920: Iron, opening discussion of article scope: 「the present article being confined to its chemistry」 — chemical description is not an etymological or social-institutional source.
- S920: Iron, following carbon paragraph: 「the proportion and condition regulate the properties of the metal」 — do not reduce the source's grade distinctions to a mere percentage label.
- S920: Iron, same paragraph: 「cast iron, steel, wrought iron」 — a broad iron gloss can conceal several explicitly distinguished technical categories in this witness.
- S920: Iron, physical-properties paragraph: 「In bulk, the metal has a silvery white lustre」 — material appearance vocabulary can differ from an everyday inherited colour category; no universal colour taxonomy follows.
- S921: Bronze, opening sentence: 「in variable proportions」 — an alloy family is not automatically a single recipe.
- S921: Bronze, opening paragraph, processing comparison: 「more fusible than copper and thus better suited for casting」 — the article connects a material distinction with a use/process distinction; this is not a furnace operating instruction.
- S921: Bronze, named engineering alloys, aluminium-bronze sentence: 「though often nearly or completely destitute of tin」 — the displayed family word does not guarantee tin membership in every use covered by this 1911 terminology.
- S921: Bronze, ancient metal names, Homer discussion: 「copper pure or alloyed」 — record translation uncertainty rather than treating the gloss as an assay.
- S921: Bronze, opening etymology sentence: 「The word has been etymologically connected」 — this is an attributed proposal; the same sentence introduces a competing place-name proposal, not a settled derivation.
- S922: Alloys, opening definition: 「or even uniformity throughout the material」 — the term does not guarantee a uniform interior.
- S922: Alloys, introductory brass example: 「for we can largely alter its percentage composition」 — a named family may persist across composition changes.
- S922: Alloys, continuation of brass example: 「the properties change more or less continuously」 — avoid an invented discrete naming threshold unless the fictional institution actually defines one.
- S922: Alloys, after the plate, manufacturing-method paragraph: 「but it is not the only method possible」 — fusion is the article's general method, not a universally necessary condition for every alloy.
- S922: Alloys, microscopic structure discussion before the plate: 「the uniformity of brass and bell-metal is only superficial」 — a surface-description word is not sufficient evidence of microscopic homogeneity.

The anchors were selected for lexical and record-design consequences, not to teach extraction practice. The four source titles are independent documents in one dated reference work, not four independent modern corroborations. Their publication date, shared editorial context and the age of their archaeological interpretations remain part of the evidence record.

## 4. A lexicon interface for metal words

Use this schema as a ledger interface, not as a claim that natural languages encode scientific taxonomies. Fields may be unknown; the point is to make uncertainty visible before a label reaches narrative or canon.

| field | what goes here | what does not follow |
|---|---|---|
| `sense_id` | stable identifier for one use of a form | the same written form in two eras is not automatically the same sense |
| `display_gloss` | reader-facing translation such as red metal or ring metal | English words are not native phonological inputs |
| `form_kind` | native-form, borrowed-strata, translated-label, unresolved | familiar-looking letters do not decide whether a word is borrowed |
| `referent_category` | feedstock, process, intermediate, material family, grade, object, value unit | a named object does not prove local production of its material |
| `composition_status` | analyzed, declared fictional range, unknown, not applicable | an opaque family name does not supply a chemical formula |
| `process_context` | named operation and input/output relation | process similarity does not establish shared etymology |
| `institution` | speakers, users and any guarantor of the term | a craft occupation is not automatically a caste or ritual monopoly |
| `era_word` | first/last use interval of this form or sense | word arrival is not referent arrival |
| `era_referent` | independently stated supply/production interval | one imported specimen is not a local industrial system |
| `source_or_design` | located historical witness or explicitly invented brief | design coherence is not historical attestation |
| `uncertainty` | supported, partial, unresolved, with exact basis | a structural gate pass does not mean an assertion is historically true |

For a generated conlang, create the semantic records before generating forms. Feed only the records actually typed `native-form` into phonotactic checking. The display label “washed ore” remains a translation until a native form, morphology and representation scheme exist. A borrowing history must identify its immediate donor and adaptation rather than merely resembling a historical metal name in Latin, Greek or English.

Do not convert a real source's lexical ambiguity into a fictional grammatical ambiguity by accident. If the brief wants one broad term for copper and some copper alloys, that is a **new fictional decision**. Store its rationale and distinguish it from a historical claim about the meanings of a particular Greek or Latin term. The resemblance can motivate a design question without becoming evidence of shared history.

A useful record may contain an ordinary-language label and a restricted workshop label for the same item. Keep their institutions distinct. An apprentice can recognize an ordinary category without being authorized to certify a grade. A merchant can quote a grade without possessing its recipe. A ruler can impose a stamped sale category without making every workshop use that category in its internal speech. These are possible fictional arrangements, not a universal account of historical guild organization.

## 5. Era staging: four clocks instead of one metal age

Start with four independently writable clocks:

1. **Form clock:** when this word or form is used in the fictional language.
2. **Sense clock:** when that form acquires the relevant technical or market sense.
3. **Object clock:** when the material or finished object is available, perhaps by import.
4. **Process/institution clock:** when local production or certification is present.

A coherent brief can place imported cast objects before local smelting, a borrowed process name before widespread household use, or an old trade-family name after an administrative composition standard changes. Each ordering needs a reason. None is inferred merely from the presence of a metal word in a lexicon.

This prevents two common false histories. In the first, a borrowed metal word is assigned to E1 and the worldbuilder dates a whole furnace industry to E1 because the word exists. The proper outcome is a word-entry date plus an unresolved production field. In the second, an E2 alloy object is observed and every occurrence of the older family word is back-translated into that object's composition. The proper outcome is a sense-specific translation with an unknown or broader E1 material range.

The rejected periodization candidate is not used to fill these clocks. Its universal diffusion and racial-stage narrative cannot turn a local invented process sequence into the history of all societies. An age label can be a convenient authorial index if the brief defines exactly what it indexes; it is not a license to collapse language, political institutions, burial custom and workshop technology into one developmental rank.

Keep authorial eras separate from characters' own period names. “Before the Port Seal” might be the world's internal era boundary; “E1 imported feedstock horizon” is the designer's analytical label. The internal phrase can persist for political reasons even when workshop practice changes gradually. Decide which system a scene uses before treating disagreement between the labels as a contradiction.

## 6. Worked NON-CANON two-era register

**Trigger:** a fictional river port needs words for incoming copper-rich material, casting households and a later hillworks industry. The task is to produce a usable semantic inventory, not to reconstruct a real ancient language. The machine-readable companion is `reports/round-85/metallurgy-craft.json`; its status is prepared handoff, not accepted canon.

**E1 brief:** the port imports feedstock and finished objects. Local households cast and repair objects, but the brief supplies no evidence of local ore extraction. “Red metal” is an ordinary trade-family gloss with unknown exact composition. “Ring metal” is a functional family used when ordering bells; its name does not fix a recipe. “Cast blank” denotes a product stage. “Casting house” denotes a place/institution, not proof that it mines or smelts.

**E2 change:** a named hillworks institution now prepares ore and extracts metal; the port creates an assay office. These are explicit additions to the invented brief, not conclusions drawn from E1 vocabulary. Add “ore stone,” “washed charge,” “roast charge,” “furnace burden,” “slag” and “refined lot” as separate semantic records. This is an illustrative inventory; a real conlang could express some of them compositionally instead of coining six simple roots.

Retain E1 “red metal” as a broad market family in E2. Add “white-hard grade” as an office-recognized grade, with the fictional record requiring a separate assay field. Do not claim that its English adjective determines a modern material specification. The institution defines what counts in the fictional transaction; historical facts about actual assays would require their own sources.

**Action:** type all twelve entries as translated labels; give each its semantic category, supply/process context and composition status. Add the four source-to-design bridges: extraction need not yield purity; iron grades are explicitly differentiated by the dated witness; copper/alloy translation can be ambiguous; alloy name does not enforce fixed proportions. These bridges motivate decisions without importing the source's historical society into the invented world.

**Checks:** an E1 caster never acquires mining authority merely from “casting house”; “ore stone” never denotes extracted metal; “ring metal” never supplies a recipe; “refined lot” never means chemically pure by default. The era change is the newly declared institution and process chain, not a universal developmental step. The companion's `craft-check.txt` records the bounded semantic/source-location checks; those checks are not a general culture validator.

**Outcome:** twelve semantic records across two eras and four located source bridges, with no native forms or etymologies asserted. A writer can now describe an argument between the port merchant and the hillworks clerk without assuming they use the same grade system. The clerk can refuse a market-family name as insufficient for certification, while the merchant can legitimately continue using that family name in ordinary trade. That scene conflict is a product of the invented institution, not a claim about a real historical people.

## 7. Error patterns and repair decisions

| signature in a draft | likely error | repair |
|---|---|---|
| Every “bronze” object has one recipe regardless of era | name–composition collapse | separate name/sense from composition evidence and its date |
| Imported metal word proves a local furnace | word clock substituted for process clock | leave production unresolved until the fictional brief or an actual dated source supplies it |
| Ore, molten metal and finished sword share an undocumented category | referent category drift | write separate sense rows or an explicit broad category with context restrictions |
| A process verb means melting whenever metal changes | extraction confused with working/remelting | specify input, output and operation; route engineering details out of scope |
| Slag means nothing but unwanted dirt | source distinction erased | keep product/function/valuation as separate fields; do not invent a modern chemical claim |
| A smith is automatically hereditary, secret or ritually marginal | unsupported social universal | mark the institution as a fictional choice or obtain a claim-scoped historical source |
| “Iron” receives an English etymology from a chemistry article | title used as authority beyond scope | remove the etymology or hold it for a real etymological witness |
| A caption supplies a broad statement about every alloy | figure-specific observation generalized | locate a body statement or retain the explicit caption scope |
| Alloys must always have been melted together | typical route made necessary | preserve the source's not-only-method qualification |
| A coherent generated lexicon is marked accepted canon | submission mistaken for acceptance | revert canon status to not canonized and request lore's separate receipt |

An error pattern is a diagnostic question, not a claim to detect every instance mechanically. Source-body review is still required when a sentence moves from a technical distinction to an explanation of historical social organization. The structural entry counter detects missing records, identifier errors and citation shape; it cannot settle whether a paragraph faithfully represents a source's argument.

## 8. Craft checklist

1. Read the partial owners before drafting another tool bank or market-money glossary.
2. Define the source scope: dated terminology, not modern engineering or archaeological consensus.
3. Give each lexeme a sense identifier and a referent category.
4. Keep composition separate from family name, grade, appearance and intended use.
5. Name the institution that recognizes a restricted grade; leave ordinary adjectives ordinary.
6. Record the word, sense, object and process clocks independently.
7. Put every borrowed form through the donor/adaptation record; do not infer borrowing from looks.
8. Keep display glosses out of the native sound channel until native forms are supplied.
9. Locate body quotations on the actual cited page, not a neighbouring article or plate caption.
10. Verify that the source's qualification survived the design bridge: variable proportions, ambiguous names, not-only-method.
11. Keep universal stage-law and unsupported caste/taboo claims out of the comparative model.
12. Prepare the lore handoff with evidence statuses, open questions and explicit non-canon standing.

## 9. Limits and remaining questions

This entry deliberately uses a small, dated technical reading set. It provides no verified language-family etymology for iron, copper or bronze; no global adoption chronology; no account of every smelting tradition; and no general theory of a smith's social status. A request for a historical community's exact metal vocabulary needs that community's linguistic and archaeological sources, not a larger set of English glosses from this reference work.

The lexical interface can represent differing knowledge between speakers but cannot infer it. A character's ability to recognize ore, judge a bell, certify a grade or repair a tool must come from the fictional brief. A job title alone is insufficient. Likewise, a garment or badge associated with a workshop is a costume record requiring its own era/rank semantics; this article supplies no attested costume rule.

The sources' shared editorial environment limits corroboration. Agreement among four article titles in one 1911 encyclopedia is not equivalent to independent modern verification. Every adoption here is scoped to what its source actually says. The refused periodization narrative remains a documented reject; selecting technical vocabulary from neighbouring articles does not rehabilitate that narrative.

## 10. Lore handoff

Send sense records, era intervals, institutions, declared material ranges, source bridges, unresolved fields and check receipts. Label native forms absent when they are absent. Label the whole worked example NON-CANON. Preserve the distinction between an attested source statement and a proposed worldbuilding consequence so lore can accept, revise, defer or reject each independently.

Kotodama proposes the register and prepares its evidence; lore records the world bible and owns canon acceptance and consistency decisions. No source quote, local script output, reviewer comment or generated example in this entry constitutes that acceptance.
