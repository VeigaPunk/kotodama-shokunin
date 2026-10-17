# Naming-to-Canon Workflow: Derivation, Etymology Ledger, Collision Review, and Handoff
- topic: An auditable pipeline for proposing names for persons, places, gods, individual items, and ships; couples linguistic derivation to cultural use without granting canon authority.
- sources:
  - Hough, Carole (ed.) (2016), *The Oxford Handbook of Names and Naming*, first ed., Oxford University Press; especially Nyström, “Names and Meaning”; Taylor, “Methodologies in Place-name Research”; Lawson, “Personal Naming Systems”; Coates, “Names and Historical Linguistics”; Sandnes, “Names and Language Contact”; Jones, “Ship Names.” [Publisher preview, including contents and Hough's introduction](https://api.pageplace.de/preview/DT0400.9780191630415_A29774794/preview-9780191630415_A29774794.pdf).
  - Campbell, Lyle (2013), *Historical Linguistics: An Introduction*, 3rd ed., Edinburgh University Press; North American edition, MIT Press, ISBN 9780262518499. [Edition record](https://mitpress.mit.edu/9780262518499/historical-linguistics/).
  - Burkert, Walter (1985), *Greek Religion*, translated by John Raffan, Harvard University Press; English translation of the 1977 German work. [Publisher description and scope](https://www.hup.harvard.edu/books/9780674362819).
  - Cleland, Liza, Glenys Davies, and Lloyd Llewellyn-Jones (2007), *Greek and Roman Dress from A to Z*, first ed., Routledge, ISBN 9780415226615; especially preface pp. viii–x on evidence and contextual variation. [Publisher preview](https://api.pageplace.de/preview/DT0400.9781134589166_A24932461/preview-9781134589166_A24932461.pdf).
  - Lexicon of Greek Personal Names project (n.d.; consulted 2026-10-17), *LGPN*, University of Oxford, live database and project introduction. [Evidence coverage and bearer-based organization](https://www.lgpn.ox.ac.uk/). The webpage has no publication year; consultation date is not a publication date.
  - Whistler, Ken (ed.) (2026), *Unicode Standard Annex #15: Unicode Normalization Forms*, revision 58, Unicode 18.0.0. [Pinned specification](https://www.unicode.org/reports/tr15/tr15-58.html).
  - Hadley, Josh, and Roozbeh Pournader (eds.) (2026), *Unicode Technical Standard #39: Unicode Security Mechanisms*, revision 34, version 18.0.0; §4, confusable detection. [Pinned specification](https://www.unicode.org/reports/tr39/tr39-34.html).
- couples: language — `../linguistics/naming-systems.md`, `../linguistics/historical-linguistics.md`, `../linguistics/language-contact.md`, `../linguistics/writing-systems.md`, `../linguistics/phonetics-phonology.md`, `../linguistics/morphological-typology.md`, `../linguistics/semantics-pragmatics.md`; myth/symbol — `../myth-symbol/pantheon-archetypes.md`, `../myth-symbol/symbolism-synthesis-method.md`; era/costume — `../culture-material/era-periodization-models.md`, `../culture-material/costume-semiotics.md`, `../culture-material/material-culture-inference-method.md`; sibling — lore-shokunin receives proposals and owns the world bible, acceptance, and consistency adjudication.

## 1. Authority, identity, and evidence are separate
- This is method/reference knowledge. Every fictional form below is a disposable demonstration, not a proposed addition to any actual world's canon.
- **Entity identity** answers which person, place, cult figure, object, or hull is meant; **name identity** answers which linguistic form is used, by whom, and when. Never use spelling alone as an entity identifier.
- One entity may have many names; one name may belong to many entities. LGPN's separation of name and bearer is a useful real reference, not a requirement to imitate Greek naming.
- Distinguish the creator's derivation, an in-world speaker's explanation, and a scholar's historical hypothesis. A folk etymology can be culturally important while linguistically wrong (Campbell 2013; Hough 2016).
- Working states: `candidate`, `held`, `ready-for-review`, `withdrawn`. Only lore-shokunin can return an acceptance decision; this lane never turns `ready-for-review` into canon.
- The ledgers, thresholds, IDs, and packet below are **workflow conventions**, not historical universals or a replacement for the receiving lane's integration contract.

## 2. Frameworks to use, and limits to preserve
| Framework | Operational question | Calibration |
|---|---|---|
| Onomastics: formation versus reference (Nyström in Hough 2016) | What formed the name, and what does it identify now? | A name's current reference is not exhausted by a dictionary gloss. |
| Socio-onomastics (Ainiala in Hough 2016) | Who uses this variant, in which interaction? | No single “native name” need exhaust a multilingual community's usage. |
| Comparative method and relative chronology (Campbell 2013) | Can the form follow the recorded language history? | Similarity alone establishes neither cognacy nor ancestry. |
| Contact onomastics (Sandnes in Hough 2016) | Was this inherited, borrowed, translated, or reinterpreted? | Each transfer needs a direction, receiving variety, and period. |
| Material-context comparison (Cleland et al. 2007) | Where is the name displayed, worn, or recited? | An image, a prescribed outfit, and ordinary practice are different evidence. |
| Unicode equivalence/confusables (UAX #15; UTS #39) | Are different stored strings equivalent or visually misleading? | Text-processing equivalence does not establish linguistic or entity identity. |

## 3. Establish the naming brief before generating strings
- Obtain a read-only snapshot/version of lore's entity list and constraints; record missing inputs rather than filling their gaps with invented history.
- Specify entity type, stable `entity_id`, culture/community, language variety, era of naming, era of use, location, register, and intended medium/audience.
- Request the minimum language profile: phonemes and phonotactics, stress/tone, productive name morphology, compound order, inflection, script, transliteration, and reader-facing spelling policy.
- Request a **name-slot schedule**: assigner, given/lineage/byname/title slots, address versus reference, and any change at initiation, marriage, office, conversion, or death. None is mandatory everywhere.
- Request a **coupling brief**: relevant cult or story, symbol meaning in that community/era, naming authority, material carrier, and costume display. Record `none` where no connection is intended.
- Specify editorial needs separately: pronunciation accessibility, dialogue distinguishability, localization, map-label length, and searchability. These are production constraints, not facts about a fictional people.
- Deliverable of intake: unresolved questions plus a bounded naming profile; return conflicts over an entity's history or identity to lore rather than deciding them through a convenient name.

## 4. Select formation rules by entity type
| Entity | Candidate formation mechanisms | Required distinctions | Coupling check |
|---|---|---|---|
| Person | inherited name pool, compound, relational name, byname, chosen name | individual versus house; title versus personal name; changes over a lifetime | A cult-derived name need not prove personal devotion; a badge may mark office, not descent. |
| Place | descriptive formation, association, commemoration, transfer, borrowed substrate name | feature versus settlement; naming date versus settlement date; competing local/official forms | A sacred cape may retain its name after the shrine disappears; record both dates. |
| God/cult figure | inherited theonym, epithet, euphemistic substitute, local title | deity claim versus cult manifestation; epithet versus separate entity; speaker's identification | An equation between gods is a proposed theological position, not an automatic entity merge. |
| Individual item | maker/owner transfer, deed-name, dedicatory title, metaphor | unique artifact versus product/type; name versus inventory number; copy versus original | Match inscription technique and ritual use to era; a generic “sword” is not yet a proper name. |
| Ship | transferred person/place/god name, virtue, emblem, administrative series | hull versus class, fleet prefix, registry number, successive names, reused name | Record sponsor, dedication, ensign/figurehead, and renaming event separately (Jones in Hough 2016). |
- Do not impose human gender categories on ship names or assume every culture assigns vessels personal names. State the fictional institution's rule.
- Preserve productive repetition when the brief warrants it: namesakes, commemorative fleets, and repeated place names are plausible; reader confusion still needs mitigation.

## 5. Derive candidates as a reproducible chain
1. **Select source lexemes**, not an English phrase plus arbitrary syllables. Give each root a language-stage ID, pronunciation, semantic range, and evidence/design status.
2. **Choose a named construction**: compound, genitive phrase, patronymic, derivation, clipping, epithet, loan, calque, or transfer. Record head/dependent order and any linking morphology.
3. **Form the historical input** with required inflection, agreement, and morphophonology. A bound stem is not automatically interchangeable with its dictionary citation form.
4. **Apply ordered changes** to the relevant variety and period. Show intermediate forms and environments; track morphology, analogy, borrowing, and semantic change as distinct operations.
5. **License exceptions explicitly**: liturgical preservation, spelling conservatism, a later loan, analogical remodeling, or deliberate revival. “It sounds better” is an editorial choice, not a sound law.
6. **Derive each contact form separately** from the form actually encountered at that date. Label phonological adaptation, translation, partial translation, or new naming; an outsider's form is not merely a respelling by default.
7. **Render layers separately**: pronunciation → native spelling → transliteration → optional reader spelling. Log information loss; transliteration need not reproduce historical pronunciation.
8. **Attach use conditions**: speaker, addressee, register, taboo scope, territorial authority, and validity interval. A secret name is not automatically a more ancient name.
9. **Attach cultural/material links** with their causal direction: emblem → name, name → badge, or shared source. A rebus requires a homophony/graphic relation in the specified variety and era.
10. **Back-check the chain** against the profile and neighboring examples; keep alternative derivations when evidence cannot choose. Never invent an attestation to make the chain look complete.
- Give literal compositional gloss, current referential use, and poetic/folk explanation separate fields. Opacity is a legitimate outcome, not a defect to repair with a false translation.

## 6. Era staging: date the operation, not just the finished name
| Stage/event | Linguistic action | Myth/symbol and material action | Ledger obligation |
|---|---|---|---|
| Initial coinage | use the contemporary construction and variety | select assigner and occasion; state whether a cult/emblem participates | distinguish coinage date, first surviving attestation, and unknown origin |
| Language change | apply ordered changes or document a retained register | spoken name may change while carved lettering stays old | separate pronunciation interval from inscription date |
| Contact/conquest | borrow, translate, reinterpret, or replace | official seals and uniforms may change before household usage does | parallel names with users, locations, and contested authority |
| Religious reform | preserve, taboo, substitute, or reinterpret a theonym | insignia can be removed while the name survives, or vice versa | proposed event dependency; no invented reform date |
| Bureaucratic standardization | prescribe spelling, slots, or registry labels | name appears on certificates, ship registers, badges | policy date is not proof of universal compliance |
| Antiquarian revival | reuse an older form or reconstruct one | “ancestral” dress and emblems may be newly selected | distinguish revival claim from demonstrable continuity |
- These are optional mechanisms, not a universal civilization ladder; oral societies can regulate names closely and literate states can tolerate variation.
- Use relative stages when dates are unavailable. A new textile term need not prove a new naming system; a surviving old name need not prove an unchanged costume.

## 7. Etymology ledger: minimum record contract
| Field group | Minimum contents |
|---|---|
| Identity | `entity_id`, `name_id`, `entity_type`, `proposal_id`, revision, naming-profile version |
| Scope | culture/community, language/variety/stage, register, users, place of use, naming authority |
| Time | coinage interval, attestation date/source, use interval; mark unknowns and proposed event dependencies |
| Form | original string/code points, pronunciation and notation, script, native spelling, transliteration scheme/version, reader form |
| Construction | root IDs and senses, segmentation, construction ID, input, ordered operations, intermediate outputs, exceptions |
| Meaning | compositional gloss, present function/reference, attributed folk explanation with its speaker/source |
| Relations | aliases, former/successor names, namesakes, transfers, epithets, disputed identifications; each relation typed |
| Coupling | myth/cult, symbol, era-event, garment/insignia and material-carrier IDs; relation/direction and provenance for each |
| Evidence | source key, author/year/edition, page/entry/inscription ID, attested form and context, confidence and limitations |
| Review | collisions checked and coverage, query/method, findings/dispositions, reviewer, unresolved `(to-verify)` items |
| Decision | proposal state, reason, superseded revision; lore's returned decision/reference kept distinct from author recommendation |
- Use evidence labels per claim: `attested`, `scholarly-reconstruction`, `contested`, `design-invention`, `unknown`. Do not collapse these into one confidence score for the entire name.
- In historical scholarship, `*` conventionally marks reconstruction/unattested status; label fictional design stages explicitly rather than letting an asterisk imply real comparative evidence.
- An etymology citation must support the etymology, not merely prove the name exists. Preserve competing analyses and ambiguous segmentation instead of silently selecting the prettiest gloss.
- Keep the original form as supplied; normalization produces comparison keys, not permission to overwrite source transcription. Corrections create a traceable revision and retain the old reference.

## 8. Collision review: compare broadly, adjudicate locally
- Input set: proposed forms plus all names/aliases supplied by lore, including withdrawn and former names where relevant; declare snapshot, languages, eras, scripts, and any unavailable records.
- Search across entity types as well as within them; then classify whether a hit is aliasing, deliberate transfer, permitted homonymy, accidental duplication, or unresolved identity.
| Pass | Method | Required response |
|---|---|---|
| Exact/raw | compare original strings and IDs | same string/different entity is a finding, not proof of mistaken identity |
| Canonical equivalence | compare NFC keys; retain raw inputs (UAX #15) | merge equivalent encodings of a form only after checking record identity |
| Editorial retrieval | separately compare case-folded, spacing/punctuation, optional accentless and transliteration keys | flag lossy matches; do not delete meaningful case, tone marks, or script distinctions |
| Graphic confusables | inspect font/medium; optionally UTS #39 skeletons and mixed-script warnings | human review; a security skeleton is not an etymology or a native reader's judgment |
| Phonological | compare pronunciation in each relevant variety; listen/read aloud | flag homophones and near-neighbors; spelling distance and English Soundex are not universal phonology |
| Semantic/cultural | compare literal glosses, cult titles, insults, sacred restrictions, historical associations | meaning overlap is not automatically a collision; identify affected users and evidence |
| Reader-facing | test names appearing together in a scene, map, roster, or audio sequence | mitigate confusing similarity by contextual labels or different candidates, not fake historical rules |
| External | search exact variants/transliterations in relevant languages and major reference sources | record queries, date, hits, and unsearched coverage; route rights judgments outside this lane |
- Suggested **editorial trigger**, not a scholarly threshold: Levenshtein edit distance ≤1 between co-occurring reader forms after the chosen text-normalization pass prompts review; short names need special care and distant spellings can still be homophones.
- Each finding records both IDs/forms, affected context/interval, method, severity, and disposition: `revise`, `retain-intentional`, `disambiguate`, or `hold`; retain a reason and reviewer.
- A repeat name may be intentional across eras but confusing in a flashback. Resolve presentation without pretending historical homonymy never existed.
- Report “no hits in snapshot X using passes Y” only after performing them. An unavailable lexicon, unrun language check, or inaccessible script is `not checked`, never a clean result.

## 9. Bounded reference comparison: Classical Greek naming ecology
- **Scope:** Greek-speaking communities of the fifth–fourth centuries BCE; not one uniform Greek culture and not a complete account of the Mediterranean.
| Coupled system | Reference observation | Naming-workflow consequence |
|---|---|---|
| Language/family + writing | Greek is Indo-European; alphabetic texts coexist with regional/dialect variation (Campbell 2013; LGPN). | Record variety and inscription convention; do not project a modern pronunciation onto every ancient spelling. |
| Myth/pantheon core | Zeus, Athena, Apollo and other gods belong to locally differentiated cult practice, not a single administrative pantheon (Burkert 1985). | Keep divine names, cult epithets, and local identifications distinct; a theophoric personal name does not identify its bearer's exact theology. |
| Symbolic system | Divine attributes, sanctuary contexts, festivals, and dedications supply situated associations (Burkert 1985). | Verify a claimed attribute against a dated object/text; do not treat “owl = wisdom everywhere” as evidence. |
| Era model | “Classical” is an external period label, not a universal local dating system; community history remains necessary. | Attach names to local attestation/use intervals rather than deriving all chronology from the period label. |
| Costume/material signature | Chiton, peplos, and himation belong to a varied dress repertoire; literary terms, images, and actual garments are different evidence (Cleland et al. 2007). | An inscribed dedication or garment depiction needs its own context; no automatic family-name-to-outfit mapping. |
| Naming practices | LGPN records individual bearers from literary, epigraphic, papyrological, numismatic, and artifact evidence; names may refer to gods, ideals, or origins. | Separate name entry from bearer, allow repetition, and cite the actual record before interpreting an individual. |
- **What a worldbuilder can take:** bearer/name separation, local cult-specific epithet inventories, register/medium fields, and era-bounded naming pools; borrow relationships and institutions, not an undifferentiated “Greek” syllable costume.
- **Provenance cautions:** the handbook and database are entry points, not complete social coverage. Monumental/literary survival privileges some groups and genres; chronicle evidence for everyday naming ceremonies can be scarce.
- This entry's knowledge is thin for exact community-, status-, and gender-specific naming formulas and garment-name associations: those applications remain `(to-verify)` until checked in a specialist corpus. Do not infer absence from silence.

## 10. Disposable end-to-end fixture: one profile, five entity types
- **Invented input only:** language T, roots `/asa/` “reed,” `/tal/` “haven,” `/mun/` “keeper,” `/kar/` “rod”; modifier–head compounding, initial stress, letters corresponding to the displayed phonemes. No real-language etymologies are claimed.
- **Proposed cultural coupling:** a reed-associated local cult, woven reed badge, and dedication rite. The badge has no specified color; no external color symbolism is imported. All three institutions require lore's decision if ever adapted.
- **Chronology:** S0 coinages precede S1 changes; S1-L1 `/t/ > /d/` between vowels, including across compound boundaries; then S1-L2 `/s/ > /h/` between vowels. Roots and ordinary compounds share these rules; the cult register preserves S0 forms by explicit design.
| Fixture entity/name IDs | Formation and trace | S1 proposal | Cultural/identity note |
|---|---|---|---|
| E-PER / N-PER | `/asa+mun/ → /asamun/ → /ahamun/` | Ahamun, `/ˈa.ha.mun/` | reed-keeper formation; an individual's name, not proof of office |
| E-PLC / N-PLC | `/asa+tal/ → /asatal/ → /asadal/ → /ahadal/` | Ahadal, `/ˈa.ha.dal/` | place label; old carved Asatal remains a distinct dated form |
| E-GOD / N-GOD | S0 `/asa/`; conservative cult register blocks S1-L2 | Asa, `/ˈa.sa/` | ordinary S1 Aha is an alias candidate, not a second god |
| E-ITM / N-ITM | `/asa+kar/ → /asakar/ → /ahakar/` | Ahakar, `/ˈa.ha.kar/` | individual rod's dedication name; not the generic term for every rod |
| E-SHP / N-SHP | transfer the S1 place name `/ahadal/` | Ahadal, `/ˈa.ha.dal/` | separate hull identity; optional reed-badge ensign is a proposal |
- **Contact branch:** neighbor U encounters S1 `/ahadal/`, deletes unavailable `/h/`, then contracts `/aa/` to `/a/`: `/ahadal/ → /aadal/ → /adal/`, reader form Adal. These invented repair rules belong to U, not to T's earlier sound laws.
- **Ledger sample:** N-PLC has literal gloss “reed-haven,” S0 formation, S1 current form, place reference E-PLC, derivation profile T-v1; Adal is a linked U-language name record for E-PLC, not an alternate entity.
- **Expected collision findings:** N-PLC/N-SHP match exactly and phonologically; retain as intentional transfer, disambiguate map/registry references with type and hull ID. Ahadal/Ahakar have edit distance 2, outside the ≤1 trigger, but merit qualitative review for their shared opening and rhythm; use context or another item-name candidate if they co-occur confusingly.
- **Encoding fixture:** `\u00C9la` and `E\u0301la` are canonically equivalent strings after NFC; this says nothing about whether two people sharing that spelling are one person. These strings are encoding tests, not names assigned to the fixture culture.
- **Review result scope:** the table demonstrates intended dispositions, not a completed fleet-wide or real-language collision clearance. External associations, lore compatibility, and cultural reception remain `not checked`.

## 11. Handoff envelope and receiving decision
- Example envelope only; field mapping must be agreed with lore's world-bible integration contract. All referenced collections below travel inside the proposal packet, not as edits to the bible.
```yaml
schema: naming-proposal/v1
proposal_id: DEMO-NAMING-01
revision: 1
authority: proposal-only
recipient: lore-shokunin
base_bible_snapshot: null
state: held
profiles: [T-v1, U-v1]
entity_ids: [E-PER, E-PLC, E-GOD, E-ITM, E-SHP]
name_ledger: embedded-records
attachments: [lexeme-ledger, ordered-rules, era-table, alias-relations, collision-report]
evidence_policy: claim-level-status-and-source-locator
unresolved: [external-checks-unrun, bible-snapshot-missing, institutions-unapproved]
requested_decisions: [entity-relations, name-selection, cult-register-exception, transfer-policy]
lore_decision: null
```
- A real packet embeds the complete §7 records and named attachments or supplies durable resolvable locations/digests; these symbolic attachment labels are not evidence that artifacts already exist.
- Include rejected candidates and reasons, pronunciation guide, localization/typographic exceptions, competing derivations, source limitations, and the exact checks performed. Do not substitute a shortlist for its derivation ledger.
- Receiver checks entity identity, era dependencies, established usage, and conflicts with canon; returns accept/reject/revise/defer for each proposal, canonical IDs if assigned, decision version, and reason.
- On revision, preserve stable IDs unless identity itself changes; distinguish a corrected derivation from a new in-world renaming event. Provide impacted aliases, inscriptions, regalia labels, maps, and dialogue references as a change list.
- No response means pending, not accepted. The lane stores or hands back the receipt; lore alone updates the world bible and its authoritative name index.

## 12. Release checks, usable takeaways, and provenance cautions
- [ ] All requested entity types are represented or explicitly out of scope; entity IDs and name IDs are distinct; aliases and intentional duplicates are typed.
- [ ] Every proposed form can be reproduced from source lexemes, construction, ordered operations, and orthographic policy; exceptions and unknown etymologies remain visible.
- [ ] Myth/symbol associations specify community and era; costume/material links specify carrier and use; absent couplings are explicit rather than invented.
- [ ] Collision coverage, queries/methods, findings, dispositions, and unrun checks travel with the packet; no unexecuted clearance is described as passed.
- [ ] Real-world claims cite author/year/edition plus a recoverable passage/entry when used for a specific derivation; unsupported particulars carry `(to-verify)` and cannot silently become evidence.
- [ ] Lore-facing packet declares proposal-only authority, baseline, unresolved decisions, and a receipt mechanism; it makes no canon writes.
- **What a worldbuilder can take:** a reusable generator plus an exception ledger, not a pile of attractive strings; institutions, naming events, and material display make the five systems causally meet.
- **Calibration:** universal “true-name magic,” pan-cultural symbol dictionaries, and consonant-to-ethnic-character stereotypes are not accepted derivation evidence. They may be labeled fictional ideologies, never scholarly explanations of a real people.
- **Provenance cautions:** distinguish an Indigenous/self-designation from an imposed administrative or colonial label, without assuming either community is unanimous; record collector, translator, date, speaker, and archive context. Colonial documentation can be both indispensable and coercively selective.
- Oral testimony is evidence with attribution and context, not an inferior substitute for a chronicle. Missing chronicles, damaged texts, inaccessible corpora, and restricted sacred knowledge create limits; leave `unknown` or `(to-verify)` instead of fabricating the missing ceremony, pronunciation, or etymology.
