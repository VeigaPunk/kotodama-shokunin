# Glossary Registry Format — Forms, Senses, Histories, and Scoped Usage

- topic: Canonical local glossary-entry profile for this corpus and terminology handoff to the world bible: identity, required fields, evidential etymologies, register labels, diachronic scope, and versioned exchange; reference knowledge and method only.
- sources: TEI Consortium (2021), *TEI P5*, version 4.2.0, chapter 9, “Dictionaries”; Philip Durkin (2009), *The Oxford Guide to Etymology*, Oxford University Press, first edition; Asif Agha (2007), *Language and Social Relations*, Cambridge University Press, first edition; Addison Phillips and Mark Davis, eds. (2009), *Tags for Identifying Languages*, RFC 5646, BCP 47. Editions and links: §9.
- couples: language — `linguistics/semantic-fields-lexicon-building.md`, `linguistics/historical-linguistics.md`, `linguistics/writing-systems.md`, `linguistics/sociolinguistics-registers.md`, `linguistics/naming-systems.md`; myth/symbol — `myth-symbol/symbolism-synthesis-method.md`; era — `culture-material/era-periodization-models.md`; costume/material — `culture-material/garment-lexicon-crosslinguistic.md`, `culture-material/costume-semiotics.md`, `culture-material/material-culture-inference-method.md`; sibling — lore-shokunin receives proposals and owns world-bible decisions. Paths above are relative to `corpus/knowledge/`.
- source: Standards and scholarship identified in §9; schema rules below are this lane's explicit house profile, not an external standard's requirements.
- verified-at: 2026-10-17 — TEI and RFC text checked; Durkin and Agha publication details and contents checked against book previews/front matter.
- recheck: On schema migration, language-tag registry change, source correction, or adoption of a terminology packet; no claim that archived TEI 4.2.0 is the latest edition.

## 1. Unit of description and authority

**Profile version: 1.0.0.** “Canonical format” means the authoritative local representation, never approval of fictional facts. This document establishes a method, not a vocabulary or culture.
A record describes **one lexical sense of one lexeme in one linguistic variety/stage**. `entry_id` identifies that record; `lexeme_id` groups its senses; `concept_id` optionally links a carefully scoped concept, not an English gloss treated as universal.
The separation of form, grammar, sense, usage, and etymology follows TEI P5 chapter 9; the stricter unit and identifiers are local design decisions. This JSON profile is not itself TEI XML or a claim of TEI validation.

| Case | Registry treatment | Do not collapse |
|---|---|---|
| Spelling, transliteration, pronunciation, or inflected variant | Form data within the same scoped record, with representation and scheme labels | Script conversion with translation; inflection with a new sense |
| Polysemy | Separate `entry_id`s, shared `lexeme_id`; connect senses with a reason | A garment, office, and divine epithet merely because their spelling matches |
| Homonymy | Separate lexeme and entry IDs; record uncertainty if the analysis is disputed | Unrelated words into one invented etymology |
| Translation or near-synonym | Separate lexical records; relate them with stated equivalence limits | Matching glosses into identical social institutions |
| Later language stage | New scoped entry linked by `continuation_of`; retain earlier record | In-world language change with an editorial revision |

IDs are opaque, namespace-qualified strings, allocated once and never recycled; do not derive them from a changeable spelling, ruler, or dynasty name. The `demo:` namespace below is reserved for format examples and cannot enter a production packet.
`record_kind` is `reference`, `proposal`, or `template`; `workflow` is `draft`, `reviewed`, `exported`, or `deprecated`. None means canon, and `reviewed` means a named review of this record, not historical certainty.

## 2. Required fields and null semantics

The exchange body is UTF-8 JSON without comments or duplicate keys; Markdown is a human-facing view. All top-level keys in §3 are required. Nested fields shown there are required unless this section explicitly makes them conditional; extensions belong under an optional `extensions` object with producer-qualified keys.
`null` means unknown or inapplicable **only with a field-specific reason in `issues`**; distinguish those reasons. `[]` means no relationship/item asserted, never proof that none existed. A draft template may use one root-level issue to declare its unfilled state; export requires individual unresolved-field notes.

| Field group | Required content and constraints |
|---|---|
| `schema_version`, `entry_version` | Independent three-part version strings; schema compatibility and record revision are different questions (§6) |
| `entry_id`, `lexeme_id`, `concept_id` | Stable lexical-sense and lexeme IDs; concept ID may be null where equivalence is unestablished |
| `record_kind`, `workflow` | Controlled values from §1; every transition appears in `history` |
| `language` | Local language, variety, and stage IDs; `family_ref` and `writing_ref` point to scoped descriptions; registered BCP 47 tag where available, otherwise documented private use |
| `forms` | One editorial lemma object; native form, phonemic/phonetic IPA, and variants separately; each supplied form identifies script, representation, and applicable scheme |
| `grammar` | Part of speech in the language's own grammatical analysis; segmentation, morpheme gloss, and paradigm reference, or explicit unknown/inapplicable reasons |
| `meaning` | Definition, short translation gloss, exclusions, and viewpoint; `viewpoint` is `analyst` or `community-claim`, with `attributed_to` required for the latter |
| `scope` | Era IDs, calendar-qualified usage bounds and precision, regions, communities, institutions; unknown is not “all eras/all speakers” |
| `registers` | At least one scoped usage object, including `unspecified` where evidence is missing; labels do not substitute for speaker/addressee/setting data (§5) |
| `etymology` | Status, immediate/ultimate source references, link chain, folk accounts, first attestation; explicit unknowns are valid, unsupported derivations are not (§4) |
| `couplings` | Language, myth, symbol, era, and costume arrays; each asserted edge has `target`, `relation`, `mechanism`, `evidence_ids`; empty arrays do not force invented links |
| `names` | `kind`, naming-pattern reference, endonym/exonym attribution; null with reasons for a non-name; kinds may include personal, place, divine, title, or object-name |
| `relations` | Objects with `relation`, `target_id`, `target_version`, `evidence_ids`; distinguish lexical, conceptual, historical, and replacement relations |
| `evidence`, `sources` | Field-level support ledger and bibliographic records (§4); factual assertions must not rely on a naked source list |
| `restrictions`, `issues` | Access handling and its basis; unresolved questions with field path, status, reason, and, when available, resolver/next check |
| `history`, `handoff` | Append-only revision events; recipient, requested action, external bible/decision pointers; initially null external pointers confer no authority |

Use BCP 47 for language identification, not as a social-register taxonomy. RFC 5646 §§2.2.7 and 4.6 permit private-use tags by agreement; each private-use subtag contains 1–8 letters/digits. `x-ktd-demo` is a syntax example, not an IANA assignment or globally meaningful identifier.
Retain a shared mapping from private-use tags to local language IDs in the packet. Registered tags take precedence when suitable; an invented script or family gets a local reference, not a fabricated ISO code. A language family and a writing system are separate fields.
Lemma preference is editorial and scoped to variety/stage, not a claim that other speakers are incorrect. Preserve a diplomatic/source transcription separately from normalized display or search forms; do not erase diacritics or reinterpret a romanization as native spelling.

## 3. Copyable entry skeleton

This is syntactically JSON but intentionally **not export-ready**. Angle-bracket text is metasyntactic, not invented lexicon; empty evidence and the root issue prevent the skeleton from masquerading as a completed entry.

```json
{
  "schema_version": "1.0.0",
  "entry_id": "demo:entry:0001",
  "lexeme_id": "demo:lexeme:0001",
  "concept_id": null,
  "entry_version": "0.1.0",
  "record_kind": "template",
  "workflow": "draft",
  "language": {
    "language_id": "demo:language:01", "variety_id": "demo:variety:01",
    "stage_id": "demo:stage:01", "bcp47": "x-ktd-demo",
    "family_ref": null, "writing_ref": null
  },
  "forms": {
    "lemma": {"text": "<headword>", "script": "Latn", "representation": "editorial-romanization", "scheme": "<scheme>"},
    "native": null, "ipa_phonemic": null, "ipa_phonetic": null, "variants": []
  },
  "grammar": {"pos": null, "segmentation": null, "morpheme_gloss": null, "paradigm_ref": null},
  "meaning": {"definition": "<scoped definition>", "gloss": "<short gloss>", "excludes": [], "viewpoint": "analyst", "attributed_to": null},
  "scope": {
    "era_ids": [], "usage_dates": {"calendar_id": null, "from": null, "to": null, "precision": "unknown"},
    "region_ids": [], "community_ids": [], "institution_ids": []
  },
  "registers": [{
    "label": "unspecified", "domain": null, "speakers": [], "addressees": [],
    "setting": null, "medium": null, "relation": null, "stance": null,
    "era_ids": [], "observer": null
  }],
  "etymology": {
    "status": "unknown", "immediate_source_ref": null, "ultimate_source_ref": null,
    "links": [], "folk_accounts": [], "first_attestation": null
  },
  "couplings": {"language": [], "myth": [], "symbol": [], "era": [], "costume": []},
  "names": {"kind": null, "pattern_ref": null, "endonym_or_exonym": null},
  "relations": [],
  "evidence": [],
  "sources": [],
  "restrictions": {"access": "open", "basis": "Unfilled format template only; not clearance for cultural material."},
  "issues": [{"field": "", "status": "to-verify", "reason": "Unfilled template: replace placeholders and explain every null before export (to-verify)."}],
  "history": [{"version": "0.1.0", "date": "<YYYY-MM-DD>", "editor": "<editor-id>", "change": "Created template", "supersedes": null}],
  "handoff": {"recipient": "lore-shokunin", "requested_action": "review", "bible_ref": null, "decision_ref": null}
}
```

For non-null `native`, IPA, and variant forms, use objects with `text`, `script`, `representation`, `scheme`, plus scoped `era_ids` and `evidence_ids`; use null with a reason for inapplicable script/scheme. Add a local asset reference when a script cannot be represented in text; never substitute a decorative font for a documented script mapping.
`usage_dates.from` and `.to` use values interpreted by `calendar_id`; `precision` records exact, approximate, interval, relative-only, or unknown dating. A null bound must distinguish unknown, open-ended, and inapplicable; do not sort dates from different calendars without an explicit conversion reference.
Each history event identifies the prior entry version in `supersedes` or explains initial creation; use actual dates/editors, never this skeleton's placeholders. Reviews add reviewer identity and evidence pointers to their history event.

## 4. Etymology and provenance requirements

Durkin (2009), especially the chapters on word identity, formation, borrowing, form change, semantic change, and names, supplies the methodological distinctions. The following ledger makes them operational; it is not a demand that every term have a recoverable origin.

1. Give every etymological link an ID and explicit source/target forms, language/variety/stage, morphological analysis, gloss, relative/absolute chronology, mechanism, status, and evidence IDs. Order links oldest justified form → documented target; chronology may remain relative.
2. Distinguish inheritance, borrowing, calquing, derivation/compounding, analogical remodeling, and semantic extension. Name the relevant sound-change rule or correspondence set for inheritance; a lookalike alone cannot supply it.
3. A borrowing link identifies the proposed donor and recipient stages, contact route, and phonological/morphological adaptation. A transmitted form may pass through intermediaries; “ultimately from X” is not evidence of direct contact with X.
4. `immediate_source_ref` points into the supported chain; `ultimate_source_ref` points to its oldest justified source, explicitly not a claim to the unknowable first origin. Missing stages stay missing; do not generate unattested bridges to make the diagram attractive.
5. Separate the source form's lexical meaning, a compositional morpheme gloss, the sense at borrowing, and current usage. “Literally” is a segmentation claim, not an explanation of every modern use or a people's worldview.
6. Mark reconstructed forms explicitly, conventionally with `*`, and identify the reconstruction's author and method. Distinguish reconstruction from an attested spelling and from an intentionally constructed fictional ancestor. Do not confuse reconstruction `*` with an ungrammatical-example marker.
7. `first_attestation` records form, sense, usage date, witness/manuscript date, document/object locator, and dating uncertainty separately. Earliest surviving evidence is not a coinage date; a later copy or chronicle does not make its wording contemporary with the event described.
8. Keep rival analyses as rival link chains with supporting and adverse evidence. `etymology.status` is `attested`, `reconstructed`, `constructed`, `contested`, or `unknown`; each link also carries its own status. Attestation of a word does not attest every arrow in its proposed history.
9. Store folk accounts in `folk_accounts` with narrator/community, era, genre, explanation, historical-validity assessment, and evidence IDs. Evidence that an explanation circulates is not evidence that the derivation is historically correct.
10. For fictional proposals, cite the actual design rule/derivation record as constructed evidence. Scholarly references establish a reusable mechanism, not the existence of the fictional form, god, costume, or event.

**Evidence object:** `id`, `field` (JSON Pointer into this record), `claim`, `basis`, `source_ids`, `locator`, `checked`, `counterevidence_ids`. `basis` is `attested`, `reconstructed`, `constructed`, `contested`, `unknown`, or `refuted`; these are local calibration labels, not probabilities or canon ranks.
**Source object:** `id`, `author`, `year`, `title`, `edition`, `publisher_or_container`, `locator`, `url_or_identifier`, `checked`, `verification`, `bias_notes`. `verification` distinguishes inspected passage, metadata-only, and unverified `(to-verify)`; page/entry/tablet/line/record numbers must actually resolve in the named edition.
A source supports only its identified passage and claim. A secondary quotation identifies both the original work and the intermediary actually inspected; do not imply direct consultation. Contradictory evidence remains visible even when a preferred analysis is selected.

## 5. Register labels: scoped usage, not a prestige ladder

TEI's usage labeling distinguishes kinds of restriction; Agha (2007) treats registers as social phenomena, including models of conduct and enregistered styles. The labels below are **house search facets**, not a universal taxonomy, a prediction from class/gender, or a substitute for local analysis.
Every register object specifies the domain, speaker/addressee roles, setting, medium, social relation, stance, era, and observer. Observer distinguishes a community's label from an analyst's label; a claim that one group “sounds coarse” needs an attributed evaluator, not authorial endorsement.

| Label | Information it adds | Additional question before use |
|---|---|---|
| `unmarked` | No locally marked usage in the stated sample/context | Unmarked to which speakers and observer, in which era? |
| `ritual` | Tied to a named rite or liturgical practice | Who may say/hear it, at which ritual phase? Not automatically archaic or secret |
| `administrative` / `craft` | Institutional domain or technical practice | Is the term used by practitioners, customers, officials, or outsiders? |
| `courtly` | A locally recognized court-associated repertoire | Is its prestige asserted by etiquette, mocked in satire, or observed in use? |
| `formal` / `intimate` | Interactional relation/style | Which interlocutors and occasion license it? Formal need not mean honorific |
| `avoidance` / `euphemistic` | Substitution under a specified social or pragmatic condition | Which prohibited referent, audience, or relationship triggers substitution? |
| `slang` | Locally identified in-group vocabulary | Whose in-group, how dated, and with what evidence of circulation? |
| `derogatory` / `reclaimed` | Evaluative stance or situated reappropriation | Who uses it about whom? Reclamation does not grant outsider permission |
| `archaic` / `obsolete` | Temporal assessment relative to a reference stage | Still productive in liturgy, titles, quotations, or names? Record residual domains |
| `unspecified` | Evidence insufficient to characterize usage | Keep the unresolved field `(to-verify)`; never silently substitute `unmarked` |

Use separate objects for independent facets; slash-separated alternatives in the table are separate labels, not literal composite values. Multiple facets may coexist. Region/dialect belongs in language/scope, grammatical gender in grammar, and publication restriction in `restrictions`; none is intrinsically a register.
Do not derive speech from costume automatically: a robe may license an office without making its wearer fluent in its register. Record the institutional rule, training/access mechanism, and any exceptions as separate proposed coupling claims.

## 6. Versioning, replacement, and reproducible handoff

| Change | Version/identity action | Consumer obligation |
|---|---|---|
| Schema adds optional data with unchanged meaning | Increment schema minor component | Preserve unknown optional extensions; declare supported schema range |
| Schema changes required fields, field meanings, or controlled-value interpretation incompatibly | Increment schema major component; provide explicit migration mapping | Reject unsupported major versions; never silently drop usage/provenance scope |
| Same-sense record gains evidence, a variant, or an additional usage observation | Increment entry minor component | Retain prior snapshot; review whether dependent claims are affected |
| Typographic correction without semantic/evidential change | Increment entry patch component | Preserve change event; a corrected citation pointing to different evidence is not merely typography |
| Substantive reinterpretation while preserving the intended lexical-sense identity | Increment entry major component and explain continuity | Re-review all pinned dependencies; old exports remain identifiable |
| Analysis splits/merges senses, changes referent, or discovers a mistaken identity | Allocate new entry IDs; deprecate old IDs with typed replacement edges | Preserve tombstones and one-to-many/many-to-one mappings; never silently redirect a citation |

These are local three-part version rules, not a claim that historical meaning behaves like software APIs. Editorial time (`history`) and in-world time (`scope`, forms, attestations) are independent; publication of a new record never moves an event within the fictional chronology.
Keep prior exported bytes immutable. Deprecation is a status plus reason and replacement relation, not deletion; an obsolete word can still be a currently valid historical entry. Correct a faulty exported claim in a new revision with explicit supersession and affected-field pointers.
A handoff packet enumerates entry IDs/versions, schema version, local language/tag and chronology mappings, referenced dependency versions, unresolved issues, source/evidence records, and a checksum of the exact UTF-8 packet bytes. A checksum detects byte drift, not scholarly truth or cultural permission.
Lore-shokunin receives a review request, not an instruction to ingest canon. Only its external decision record may populate `decision_ref`; retain its bible pointer as a reference, never manufacture an acceptance. Format incompatibility is an adapter/migration question to report, not a license to rewrite sibling data.
Do not resolve a citation against mutable “latest”. Imported decisions must identify the precise entry version they considered; a later revision requires renewed review where meaning, scope, or evidence changes.

## 7. Era staging and application to a fictional culture

Treat the rows below as independent design probes, not a universal ladder from “primitive” to “advanced”. Chronology follows local institutions, contact, and material change, not a shared European costume calendar.

| Staging probe | Lexical question | Coupled record to request |
|---|---|---|
| Oral transmission alongside later written witnesses | Is the formula old, the transcription late, or both uncertain? | Recitation register, witness date, proposed mythic use; do not backdate wording automatically |
| Adoption of a new dye, fiber, weave, or garment cut | Does the name travel with the technique, or get applied to an older object? | Loan/adaptation chain, production constraints, garment form and availability |
| Script or administrative standardization | Did spelling change while speech/meaning persisted? | Script mapping, chancery form, literacy/access distribution |
| Ritual preservation amid everyday language change | Which pronunciation, morphology, or sense is retained, by whom? | Earlier-stage entry plus present ritual usage; not an entire timeless “sacred language” |
| Court/guild divergence or institutional suppression | Has the same word become technical, insulting, euphemistic, or a personal name? | Sense split, authority/evaluator, clothing/rank rule, affected communities and era bounds |

For each proposed term: start from a referent/practice and its material limits; define the sense and exclusions; derive or borrow a form using the language-stage rules; assign witnessed or deliberately designed usage; then add only coupling edges with a named mechanism.
For any civilization/comparative-culture profile linked from an entry, require the coverage below. A glossary entry may point to these descriptions rather than pretending that one word reconstructs a whole civilization.

| Profile dimension | Minimum scoped reference |
|---|---|
| Language family + writing | Family hypothesis/status separately from languages, scripts, literacy domains, and transliteration conventions |
| Mythic/pantheon core | Tradition/version, narrative or cult context, attributed claims; no forced pantheon where that model is inappropriate |
| Symbolic system | Sign/material, interpreters, occasion, competing readings; lexical meaning is not symbolic meaning |
| Era model | Local period criteria, relative order, date anchors and uncertainty; avoid synchronized culture-wide stages by default |
| Costume/material signature | Actual fibers, dyes, cuts, technologies, access, and survival limits; an object does not attest its lost name |
| Naming practices | Name structure, kinship/title rules, endonym/exonym perspective, name changes and era/register restrictions |

## 8. Export review and failure tests

- Check unique non-demo IDs, defined schema/version support, present required keys, parseable JSON, and no unresolved placeholders; a parse success alone is not a content pass.
- Resolve every entry, language, chronology, rule, source, and asset pointer in the actual packet/version being reviewed; verify every asserted field or coupling has evidence or explicitly constructed support.
- Check etymological-link direction, contact and sound-change chronology, morphological segmentation, and separation of witness date from usage date; keep competing analyses and uncertainties visible.
- Check register against an actual or explicitly proposed speaker/addressee/setting pair, then a contrasting pair. Verify that later-era costume availability has not silently licensed an earlier word or social role.
- Export `(to-verify)` material only as visibly unresolved review material, never as settled reference: keep the field issue inline in the human view and in the machine issue ledger. Hold restricted material whose handling basis remains unresolved.
- Obtain a named review event before changing `workflow` to `reviewed`; an `exported` state means transmitted bytes only. No state in this lane certifies lore-shokunin acceptance.

| Deliberate failure | Expected result |
|---|---|
| Same English gloss offered as proof of synonymy or shared deity | Reject equivalence; compare referents, institutions, scope, and source claims |
| Folk tale supplied as the sole proof of a sound change | Retain as attributed folk account; historical derivation remains unknown/contested |
| Chronicler's late garment term placed in a much earlier event | Separate event, witness, and lexical-use dates; mark back-projection `(to-verify)` |
| Private-use subtag exceeds eight alphanumeric characters | Reject tag syntax; document a compliant private mapping rather than invent an ISO assignment |
| Proposed “high” register equated with objectively superior language | Reject narrator endorsement; attribute prestige and document the institution/context |
| Draft skeleton parsed successfully, then submitted as finished terminology | Reject export-ready status: template/demo IDs, placeholders, missing evidence and field issues remain |

## 9. Checkable editions and verification limits

- **TEI Consortium (2021).** *TEI P5: Guidelines for Electronic Text Encoding and Interchange*, version 4.2.0, chapter 9, especially §§9.2–9.3 on entry structure and constituents. [Archived chapter](https://tei-c.org/Vault/P5/4.2.0/doc/tei-p5-doc/en/html/DI.html). Supports the separation of forms, senses, grammar, usage, and etymology; does not prescribe this lane's JSON keys or version policy.
- **Durkin, Philip (2009).** *The Oxford Guide to Etymology*. Oxford University Press, first edition, ISBN 9780199236510. Chapters 3–9 are relevant reading targets; publication details and contents checked in the [authorized preview](https://api.pageplace.de/preview/DT0400.9780191570452_A23535653/preview-9780191570452_A23535653.pdf). No claim of full chapter-by-chapter inspection or invented page citations.
- **Agha, Asif (2007).** *Language and Social Relations*. Cambridge University Press, first edition, ISBN 9780521571760; DOI [10.1017/CBO9780511618284](https://doi.org/10.1017/CBO9780511618284). [Publisher front matter](https://assets.cambridge.org/97805215/71760/frontmatter/9780521571760_frontmatter.pdf) verifies the 2007 imprint and contents, including enregisterment and honorific registers. Bibliographic services may show a 2006 release date; use the consulted edition's 2007 imprint, not the later digital-publication date.
- **Phillips, Addison, and Mark Davis, eds. (2009).** *Tags for Identifying Languages*. RFC 5646, BCP 47, September 2009. [RFC text](https://www.rfc-editor.org/rfc/rfc5646.html), §§2.2.7 and 4.6 for private use. A tag labels linguistic information; it does not validate a language-family hypothesis or encode cultural authority.

## 10. What a worldbuilder can take

Take the form/sense distinction, evidence-bearing derivation chains, role-and-era usage grids, and stable versioned IDs. They let a single garment term expose trade, craft technique, ritual preservation, title formation, or social exclusion without pretending those systems must move together.
Hand lore-shokunin a bounded set of alternatives: what each form would require, which coupling mechanisms it enables, what remains unknown, and which other records would need revision. Let the recipient decide whether any proposal belongs in its bible.

## 11. Provenance cautions

This format note does not establish tradition-specific expertise or verify any historical divine, garment, or personal-name etymology. For oral, fragmentarily attested, or undeciphered traditions, chronicle evidence may be scarce or absent; record that limit explicitly and mark an unsupported reading `(to-verify)` rather than inventing a citation or phonetic value.
Colonial dictionaries, missionary grammars, court chronicles, and museum labels may preserve important evidence while restricting whose language or clothing is represented. Record compiler, date, elicitation/translation conditions, institution, and missing voices in `bias_notes`; do not automatically discard evidence or treat its categories as indigenous consensus.
Similarity, universal-symbol dictionaries, and pop claims that a name's “secret root” reveals a people's essence are not etymological demonstrations. Contested comparative or symbolic interpretations require attributed alternatives and status labels; scholarly uncertainty and an institution's in-world certainty are different facts.
Do not reproduce restricted names, ritual speech, or sacred dress details merely because a source is online. Record the handling question without exposing the material; rights/permission rulings are outside this lane. An unresolved provenance, interpretation, or access question stays visible at handoff, and no bibliography or schema status turns it into canon.
