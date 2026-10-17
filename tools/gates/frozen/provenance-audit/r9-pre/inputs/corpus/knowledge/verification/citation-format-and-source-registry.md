# Citation formats, source registry, and provenance ledger for coupled worldbuilding

- topic: A lane-local citation profile connecting each linguistic-cultural claim to its exact source version, supported scope, mediations, and design transformations; bibliography accuracy never substitutes for evidence or canon approval.
- sources:
  - KTD-S-0001 — University of Chicago Press. 2024. *The Chicago Manual of Style*. 18th ed. University of Chicago Press. [Publisher record](https://press.uchicago.edu/ucp/books/book/chicago/C/bo213648716.html). Edition identity only; citation rules below were checked through the public companions, not a full-text inspection of this book.
  - KTD-S-0002 — Lebo, Timothy, Satya Sahoo, and Deborah McGuinness, eds. 2013. *PROV-O: The PROV Ontology*. W3C Recommendation, April 30. [Dated specification](https://www.w3.org/TR/2013/REC-prov-o-20130430/), especially §3.1, “Starting Point Terms.” Supports entity/activity/agent and derivation relations, not historical truth assessment.
  - KTD-S-0003 — Dublin Core Metadata Initiative. 2020. *DCMI Metadata Terms*. January 20 version. [Dated specification](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/2020-01-20/). Supports descriptive fields and distinctions among source, provenance, coverage, language, and rights.
  - KTD-S-0004 — Carroll, Stephanie Russo, Ibrahim Garba, Oscar L. Figueroa-Rodríguez, et al. 2020. “The CARE Principles for Indigenous Data Governance.” *Data Science Journal* 19: article 43. [DOI](https://doi.org/10.5334/dsj-2020-043). Supports Collective Benefit, Authority to Control, Responsibility, and Ethics; not blanket permission to adapt traditions.
  - KTD-S-0005 — University of Chicago Press. n.d.-a. “Author-Date: Sample Citations.” Accessed October 17, 2026. [Public guide](https://www.chicagomanualofstyle.org/tools_citationguide/citation-guide-2.html). Supports author-date forms, electronic locators, translated works, and undated pages.
  - KTD-S-0006 — University of Chicago Press. n.d.-b. “What’s New in the 18th Edition.” Accessed October 17, 2026. [Public change list](https://www.chicagomanualofstyle.org/help-tools/what-s-new.html). Supports edition-specific changes, including author lists, chapter ranges, and accession numbers.
- couples: language — linguistics/historical-linguistics.md, writing-systems.md, naming-systems.md; myth/symbol — myth-symbol/motif-index-usage.md, comparative-frameworks.md, symbolism-synthesis-method.md; era/costume — culture-material/era-periodization-models.md, dress-through-eras.md, material-culture-inference-method.md; siblings — chousa-shokunin for source investigation, lore-shokunin for world-bible acceptance; no sibling or canon writes.

## 1. Contract and named frameworks

- source: The works above ground this local profile; its mandatory fields and acceptance rules are kotodama working conventions, not requirements imposed by Chicago, DCMI, or W3C.
- verified-at: 2026-10-17 — public Chicago companions, PROV-O §3.1, DCMI term definitions, CARE article text, and its [Crossref metadata](https://api.crossref.org/works/10.5334/dsj-2020-043) inspected; no tradition-specific evidence survey performed here.
- recheck: On a source-version change, broken locator, correction/retraction, changed community restriction, or before a contested reference enters a lore handoff.
- **Chicago author-date** answers “which work, which passage?”; **DCMI** answers “what resource and coverage?”; **PROV-O** answers “who transformed what into what?”; **CARE** asks whose authority and interests govern reuse.
- Keep bibliographic provenance, artifact ownership/custody provenance, and the lane’s transformation history distinct; a museum accession number is not a complete acquisition history (DCMI 2020, terms `identifier`, `provenance`).
- This is the citation interface for language–myth–symbol–era–costume coupling, not a general research service; unresolved source discovery or authentication goes to chousa, canon decisions to lore.
- A reference claim, a scholar’s interpretation, and a fictional design option are different records. Citation confidence must not silently become a canon tag or an assertion about the fictional world.

## 2. Required in-entry citation syntax

- Use `Claim text (Author year, locator; source: KTD-S-NNNN).` Source IDs supplement rather than replace readable author/year citations; every ID resolves to an entry-local registry record or an explicitly linked shared record.
- Cite a quotation at the quotation, a numerical claim at the number, and an inference at the inference; a bibliography at the top does not support every sentence below it.
- Use both names for two authors and first author + `et al.` for three or more in text; list up to six authors in references, or the first three + `et al.` for more than six (Chicago 2024, §13.23, checked via KTD-S-0006).
- Preserve a creator’s published name order and diacritics; do not mechanically invert every East Asian name. Distinguish author, editor, narrator, translator, collector, illustrator, and custodian.
- Same author/year: assign `2020a`, `2020b` consistently by title order; use `n.d.-a`, `n.d.-b` for undated collisions. Keep stable source IDs if a later discovery changes a year suffix.
- Prefer printed page, paragraph, example, tablet line, tale number, folio side, object number, figure/plate, or timestamp. For ebooks without fixed pagination use named chapter/section, not a fabricated page.
- Separate printed pagination from PDF-viewer index: `printed p. <n>; PDF image <m>` when both are necessary. Never transfer page numbers from another edition or a search snippet.
- Primary texts: `Author/attributed author, Work, conventional division; consulted editor/translator year, locator; source ID`. Unknown authorship remains unknown, not reassigned to a translator.
- Secondary access: `Original author year, cited in Consulted author year, locator; original not consulted (to-verify)`. The consulted source supports its report; do not pretend the original was checked.
- Undated resources use `n.d.` plus access date; inferred dates use an explicit qualifier and its evidence. Copyright year, edition year, collection date, and ancient composition date are not interchangeable.
- An unresolved reference or untested factual claim carries `(to-verify)` beside that specific reference/claim, plus the missing check. Do not hide uncertainty in a distant “further reading” list.
- Quotations retain original wording with omissions/additions marked; identify published translation versus own translation versus machine-assisted draft. Unreviewed linguistic translations carry `(to-verify)`.
- Example: `PROV-O distinguishes entities, activities, and agents (Lebo et al. 2013, §3.1; source: KTD-S-0002).` This supports a recording method, not a theory of cultural development.

## 3. Bibliographic entry types: minimum reference forms

Angle-bracketed values below are placeholders, not citations to invented publications. Publisher/location details follow the consulted edition; local additions preserve auditability beyond Chicago’s minimum (KTD-S-0005–0006).

| Entry type | Required reference form | Required pinpoint or qualification |
|---|---|---|
| Monograph / edited collection | `<Author/editor>. <Year>. <Title>. <Edition>. <Publisher>. <DOI/URL if consulted online>.` | Page/section for each supported claim; edition other than first explicit; publisher record alone verifies identity only |
| Chapter in collection | `<Chapter author>. <Year>. “<Chapter>.” In <Book>, edited by <Names>, <chapter range if available>. <Publisher>. <DOI/URL>.` | Specific passage required; retain chapter range locally when known, although Chicago 18 no longer requires it |
| Journal article | `<Authors>. <Year>. “<Title>.” <Journal> <volume> (<issue if supplied>): <range or article ID>. <DOI URL>.` | Page/section/figure; article ID is not a page; identify preprint versus version of record |
| Dictionary / grammar / name corpus | `<Author/editor>. <Year/version>. <Title>. <Edition/release>. <Publisher/repository>. <Persistent URL>.` | Headword + sense/subentry, grammar section/example, or corpus record ID; preserve form, language, and transcription scheme |
| Ancient / medieval text in modern edition | `<Author or traditional attribution>. <Edition year>. <Work>. Edited/translated by <Names>. <Edition/volume>. <Publisher>.` | Conventional book/hymn/verse plus consulted edition locator; separately qualify composition and manuscript dates |
| Inscription / manuscript / archive | `<Creator if known>. <Document date or n.d.>. <Title/description>. <Corpus/archive>, <shelfmark/accession>, <edition/catalogue>. <URL>.` | Inscription line, recto/verso folio, item/file; distinguish physical witness, published reading, and restored text |
| Museum object / costume image | `<Maker if known>. <Object date/range as catalogued>. <Title/description>. <Material>. <Collection>, <accession>. <Record URL>, accessed <date>.` | Separate image creator/date/license and catalogue update from object dating; pinpoint view/plate; identify reconstruction or restoration |
| Oral account / performance | `<Named narrator or authorized attribution>. <Recording date>. <Title/description>, in <language>. Recorded by <collector>; translated by <name>. <Archive/item>, <URL if authorized>.` | Timestamp/transcript line, locality and performance context; attribution and circulation follow recorded consent, not collector convenience |
| Web page / digital standard | `<Author/institution>. <Publication/update year or n.d.>. “<Title>.” <Version/date>. <URL>. Accessed <date>.` | Heading/paragraph and dated version/archive where available; homepage, search result, and underlying work are different sources |
| Dataset / typology / motif index | `<Creators>. <Year>. <Title>. <Release>. <Repository/publisher>. <DOI/permalink>.` | Feature/code/record ID, query and filters, access date for mutable data; classification code does not replace the classified witness |
| Private communication / restricted testimony | `<Authorized attribution>, <date>, <medium>; <permitted locator>.` | Cite in text or controlled note, not a public registry by default; do not expose identities, content, or access routes without authority |
| Software / generated aid / internal note | `<Creator/tool>. <Version/date>. <Artifact or operation>. <Stable record if retained>.` | Method/output identifier and reviewer; generative output or an internal note is not independent evidence for a historical claim |

## 4. Knowledge-entry types: what the citation must support

| Lane entry type | Required support packet | Invalid shortcut |
|---|---|---|
| Linguistic attestation | Language/variety, source form + gloss, grammatical or lexical locator, date/register, orthographic/transliteration conventions | Deriving pronunciation from spelling without a phonological source |
| Reconstruction / etymology | Reconstructing scholar and edition, starred form, compared forms, proposed changes and alternatives | Treating a reconstructed form as an attested inscription or folk etymology as accepted derivation |
| Myth / pantheon reference | Particular text, narrator, recension, cult/locality, collection date and textual strata; translation named | Citing a modern retelling as the unqualified belief of an entire people |
| Motif / comparative framework | Index edition + type/motif ID, actual narrative witness, and separately cited interpretive framework | A matching index number proves neither diffusion nor common origin; a design framework proves no universal mythic sequence |
| Symbol / color / regalia code | Carrier object/text, actor/audience, setting, era, and passage supporting the proposed meaning | A symbol dictionary proves one meaning across all periods, classes, or neighboring languages |
| Civilization / regional profile | Separate evidence for language family + writing, mythic/pantheon core or its inapplicability, symbolic practices, era model, costume/material signature, and naming practices | One civilization handbook citation silently covers every system and every century |
| Era / periodization | Who defined the period, geographic coverage, date bounds and uncertainty, evidence for each staged transition | An archaeological period boundary automatically dates a sound change, cult reform, and garment change together |
| Costume / material inference | Object/site/catalogue ID or statute clause; dated setting; fiber, technique, cut, depiction, or function distinguished | A law proves compliance; a painted hue proves a dye; an elite grave proves everyday dress |
| Naming / script practice | Dated attested forms and naming slots, reading/edition, endonym/exonym and official/everyday register distinguished | A name website proves antiquity, a script fixes language family, or modern standardized spelling proves ancient usage |
| Coupling hypothesis / design method | Claim IDs for each factual premise + explicit inference bridge + counterexample/alternative + `design-only` where invented | Adjacent true claims establish causation, or a novel fictional option becomes evidence about the source culture |

## 5. Source registry: fields and version identity

Use entry-local `## Source registry` blocks unless a shared registry is already designated; this specification does not require creating another file. Resolve records by `(registry location, source_id, registry_revision)`; IDs in this entry are local, not fleet-wide allocations. One source ID denotes one consulted edition/version/witness, not an entire author’s output. New editions/translations/witnesses receive new IDs linked by `related_sources`.

| Field | Requirement / recording rule |
|---|---|
| `source_id`, `registry_revision` | Stable `KTD-S-NNNN` plus revision number; identifiers never recycled; a correction records the previous revision it supersedes |
| `entry_type` | One bibliographic type from §3; add conditional fields appropriate to that type |
| `author`, `roles` | Full credited names or institutional creator; preserve narrator/community attribution separately from collector, translator, editor, custodian; write `unknown` where unknown |
| `year` | Publication year of this edition, recording year for a performance, or `n.d.`; preserve uncertainty rather than supplying a convenient date |
| `title`, `container`, `publisher` | Full identifiable title; journal/book/archive and publisher/repository when applicable; `not-applicable` must be explicit rather than guessed |
| `edition` | Edition/release/recension, volume, editor, translator, and dated version as applicable; `edition not stated` if that is all the inspected resource provides |
| `identifiers`, `access` | DOI/ISBN/accession/shelfmark as applicable; consulted URL or physical holding, access date, availability; optional authorized snapshot and computed checksum, never an invented hash |
| `language_mediation` | Source language/script, variety where known, transliteration scheme and translation history; note if only a translation was read |
| `coverage` | Region/community, social group, era/date range, genre and institutional context the source actually covers; `not-applicable` for a metadata standard |
| `what_it_supports` | List of `{claim_id, proposition, locator, relation}`; relation = `supports`, `qualifies`, `contradicts`, or `reports`; locator belongs to this exact version |
| `what_it_does_not_support` | Explicit limits: e.g. chronology but not phonology; pictured cut but not fiber; official norm but not actual compliance |
| `dependencies` | Sources/witnesses cited or copied; identify shared collector/archive/text behind apparently separate accounts; multiple URLs are not automatically independent evidence |
| `verification` | Who checked, when, against what version/holding; `metadata_status` = `checked` / `partial` / `to-verify`, and `support_status` = `checked` / `partial` / `not-consulted`, kept separate |
| `calibration` | Claim-level qualifications: `scoped`, `contested`, `source-biased`, `thin-evidence`, `design-only`, or `(to-verify)`; these local labels are not a universal scholarship score |
| `permissions` | Record supplied rights/access/community restrictions and their source; `not-assessed` is not permission; no legal clearance or community endorsement inferred |
| `related_sources`, `supersedes` | Links to other editions, translations, reviews/corrections and earlier registry revisions; retain old identifiers and the reason for replacement |

DCMI mappings are aids, not claims of exact equivalence: author → `creator`/`contributor`; year → `issued`; coverage → `spatial`/`temporal`; source relationship → `source`; restrictions → `rights`/`accessRights`. DCMI `provenance` specifically concerns significant custody/ownership changes; use PROV relations for derivation (DCMI 2020; Lebo et al. 2013).

## 6. Filled registry example: a reference-method claim

This record documents only the PROV-O passage used here; `checked` does not certify all of the specification or constitute an independent review. Other cited works need their own records when reused in a claim packet.

```yaml
source_id: KTD-S-0002
registry_revision: 1
entry_type: digital-standard
author: [Timothy Lebo, Satya Sahoo, Deborah McGuinness]
roles: editors
year: 2013
title: "PROV-O: The PROV Ontology"
container: W3C Recommendations
publisher: W3C
edition: "Recommendation, 30 April 2013"
identifiers: ["https://www.w3.org/TR/2013/REC-prov-o-20130430/"]
access: {url: "https://www.w3.org/TR/2013/REC-prov-o-20130430/", date: 2026-10-17, availability: public}
language_mediation: "English; no translation used"
coverage: "Provenance ontology; historical-cultural coverage not-applicable"
what_it_supports:
  - {claim_id: KTD-C-0001, proposition: "PROV-O distinguishes Entity, Activity, and Agent", locator: "3.1 Starting Point Terms", relation: supports}
what_it_does_not_support: "Truth of historical claims, a culture's beliefs, or authorization to adapt them"
dependencies: "PROV-DM is referenced by PROV-O; not independently audited here"
verification: {by: entry-author, date: 2026-10-17, version: "30 April 2013 Recommendation", metadata_status: checked, support_status: checked}
calibration: scoped
permissions: "Publicly readable; reuse conditions not-assessed"
related_sources: []
supersedes: null
```

## 7. Provenance ledger: transformations, not a second bibliography

Use an append-only sequence of events, each with a unique `KTD-E-NNNN`. Source records identify resources; claim records identify propositions; events connect inspected inputs to resulting reference notes, comparisons, or design options. This is a lightweight PROV-inspired profile, not a claim of RDF/OWL conformance (Lebo et al. 2013, §3.1).

| PROV term / relation | Lane use | Preserve explicitly |
|---|---|---|
| `Entity` | Edition, recording, source excerpt, claim packet, design-option revision | Identity and version; original object and its photograph are separate entities |
| `Activity` | Consultation, transcription, translation, comparison, inference, revision | Action, date/time at known precision, input/output IDs, transformation description |
| `Agent` | Narrator, scholar, translator, lane author, named reviewer | Actual responsibility; tool assistance is not a human review |
| `used` / `wasGeneratedBy` | Activity used a passage and generated a note | Source ID + locator → event ID → output claim/version |
| `wasDerivedFrom` | A new note or option derives from an earlier entity | Direct source chain and mediations; derivation alone says nothing about correctness |
| `wasAttributedTo` | Responsibility for an entity | Attribution distinct from ownership, approval, or agreement |

Every ledger event requires: `event_id`, `date`, `agent`, `action`, `inputs` with source/claim IDs + versions + locators, `output` with claim ID + revision + destination, `transformation`, `verification` with outcome/evidence, `calibration`, `canon_status`, and `supersedes` (null for an initial event). A correction adds an event naming the replaced event and reason; it never erases the earlier record.

```yaml
event_id: KTD-E-0001
date: 2026-10-17
agent: entry-author
action: paraphrase
inputs:
  - {source_id: KTD-S-0002, registry_revision: 1, version: "30 April 2013 Recommendation", locator: "3.1 Starting Point Terms"}
output: {claim_id: KTD-C-0001, revision: 1, destination: "this entry, section 2 example"}
transformation: "Restated the Entity/Activity/Agent distinction; no historical inference"
verification: {outcome: supporting-section-read, evidence: "https://www.w3.org/TR/2013/REC-prov-o-20130430/", reviewer: not-independently-reviewed}
calibration: scoped
canon_status: not-submitted
supersedes: null
```

- For a coupling inference, list every premise ID in `inputs`; keep separate output IDs for “attested,” “inferred,” and “invented.” Never cite an invented intermediate as a historical premise downstream.
- For translation, record input language, translator/tool/version, output revision and review status; unresolved lexical decisions remain `(to-verify)` even if the transcription was checked.
- For correction/retraction, preserve the old event, append its replacement, and enumerate affected downstream claim IDs and handoff IDs; notify their owner rather than silently updating someone else’s canon.
- For unavailable/restricted evidence, retain only authorized metadata and the permitted verification route. Do not copy sensitive content, personal access details, or restricted names into the ledger.

## 8. Era staging and cross-system claim boundaries

Maintain distinct chronology fields rather than one misleading “date.” The arrangement below is local craft practice; DCMI’s separate `created`, `issued`, `modified`, and `temporal` terms help prevent conflation.

| Clock / scope | Record | Coupling consequence |
|---|---|---|
| Represented practice / event | Date/range the source claims to describe; speaker and uncertainty | A later story about an early era is evidence of representation, not automatically of early practice |
| Composition / redaction | Proposed textual strata and the scholarship assigning them | Do not stage a full pantheon or name taboo from one undated composite text |
| Physical witness / collection | Manuscript copying, inscription, object manufacture, or performance recording date | The surviving witness and the supposed origin of a tradition may be far apart |
| Edition / translation | Consulted publication/release and editorial decisions | A modern translation’s familiar garment term does not establish an ancient garment construction |
| Access / registry event | Inspection date and source/claim revision | Records what the lane actually saw, not when the cultural practice existed |
| Geographic / social scope | Locality, dialect, audience, class, gender/role if evidenced | Court dress, rural speech, and temple ritual cannot be fused into one timeless national norm |

- For each proposed era transition, ask separately what changed in language, script, myth authority, symbol use, material production, dress, and naming; attach evidence or mark the proposed change `design-only`.
- A proposed chain such as “new ritual title → court emblem → garment restriction” needs distinct attestations plus evidence for transmission/causation; otherwise label it an analogy or invented mechanism, not a sourced historical sequence.
- A civilization reference closes with “what a worldbuilder can take” and “provenance cautions”; keep any unsupported profile slot visible as `(to-verify)` rather than filling it from a neighboring culture.

## 9. Calibration and provenance failure patterns

| Failure / condition | Required status and repair |
|---|---|
| Real title, unread passage | Metadata may be `checked`; support remains `not-consulted`; mark the dependent claim `(to-verify)` and identify the needed passage |
| Search snippet or retailer blurb | Discovery/identity evidence only; inspect the work before attributing its detailed argument |
| Colonial collector, missionary translation, imperial chronicle | Record commission, audience, translator, access conditions and omissions where known; `source-biased` is scoped to the relevant claim, not a blanket dismissal |
| Community-authored account | Preserve particular author/community/era and authority conditions; no individual speaks for all communities or all generations |
| Single late chronicle or sparse surviving evidence | `thin-evidence`; describe what survives and what was searched, not an invented complete pantheon, continuous chronology, or universal dress rule |
| Living or restricted tradition | Record applicable community protocols; public access and attribution do not establish permission to adapt; CARE is governance guidance, not a license (Carroll et al. 2020) |
| Rival scholarly readings | `contested`; cite each reading at its own locator and state the precise disagreement; do not average incompatible claims into a false consensus |
| Pop “universal symbol” / totalizing myth template | Designer heuristic only unless a bounded empirical claim is supported; a framework rejected for a particular claim stays rejected even if creatively useful |
| Many sources copying one witness | Record dependency chain; count witnesses, not websites, before claiming independent corroboration |
| Artifact/image/translation conflated | Split entities and record mediations; missing custody or restoration history stays unknown, not backfilled with an attractive story |

- Tradition-specific expertise here is deliberately thin: this entry verifies documentation frameworks, not the oral histories, chronicle transmission, local ritual authority, or dress practices of any particular people. Those checks remain `(to-verify)` for a future specific application.
- Do not claim a framework is “discredited” without the named critique and rejected proposition. Do not use “contested” to imply every reading is equally supported; record what evidence favors each.
- “No evidence” requires a bounded search description: collections/languages/editions checked, date range, terms, and inaccessible material. Otherwise write “not established by the consulted sources.”

## 10. Apply to a fictional-culture brief

1. Atomize the request into language/script, myth, symbol, era, costume/material, and naming claims; assign claim IDs before assembling a coupled narrative.
2. Attach readable citations and source-version IDs to every reference premise; populate the relevant §3 and §5 fields, including what the source does not support.
3. Check the actual passage/object record; separate metadata status, support status, calibration and reuse restrictions. Send unresolved source investigation to chousa rather than inventing a citation.
4. Build the chronology/scope grid in §8; mark missing slots and mismatched eras. Do not harmonize contradictions solely to make the design convenient.
5. Record each transformation as an event: preserve the borrowed structural relationship, identify changed assumptions, and label fictional mechanisms `design-only`.
6. Handoff to lore with proposed system/options, premise IDs, source registry and event IDs, unresolved alternatives, and `canon_status: not-submitted`; only lore’s own acceptance process can change its world bible.
7. Before reuse, resolve every cited ID and locator, inspect edition correspondence, test whether each citation supports the attached proposition, and enumerate downstream effects of corrections. Unchecked items remain `(to-verify)`.

## 11. What a worldbuilder can take; provenance cautions

- **Take:** a reproducible trail from attested word, text, object, or practice → scoped interpretation → explicit coupled design choice. The useful borrowing is a mechanism with changed assumptions, not an asserted identity between a fictional people and a real one.
- **Keep separate:** bibliographic accuracy, historical support, ethical/rights conditions, and fictional coherence; success on one does not certify the others.
- **Caution:** surviving chronicles, translated texts and curated costume collections are selective witnesses, not transparent cultural wholes. Unknowns stay unknown; access does not erase community authority; a checked citation never writes canon.
