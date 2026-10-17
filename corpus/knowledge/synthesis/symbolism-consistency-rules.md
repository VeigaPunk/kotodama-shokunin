# Symbolism Consistency Rules — A Closed Grammar with Regional and Historical Variation
- topic: assigning one primary domain per scoped symbol; licensing secondary readings, regional variants, era drift, and compounds; auditing the resulting method package without deciding world-bible canon
- sources:
  - Charles S. Peirce (1931–1958), *Collected Papers*, vols. 1–8, Harvard University Press, especially CP 2.247–249; [Stanford Encyclopedia of Philosophy, interpretive guide](https://plato.stanford.edu/entries/peirce-semiotics/).
  - Victor Turner (1967), *The Forest of Symbols: Aspects of Ndembu Ritual*, Cornell University Press; [edition record and description, ISBN 9780801491016](https://books.google.com/books?vid=ISBN9780801491016).
  - Umberto Eco (1976), *A Theory of Semiotics*, Indiana University Press; [publisher record and description](https://iupress.org/9780253202178/a-theory-of-semiotics/).
  - Elizabeth Closs Traugott and Richard B. Dasher (2002), *Regularity in Semantic Change*, Cambridge University Press; [DOI and edition metadata](https://doi.org/10.1017/CBO9780511486500). Standard citation uses 2002; Crossref's print-publication metadata records 20 December 2001.
  - Jo B. Paoletti (2012), *Pink and Blue: Telling the Boys from the Girls in America*, Indiana University Press; [edition record and description, ISBN 9780253001177](https://books.google.com/books?vid=ISBN9780253001177).
- couples: language — ../linguistics/semantics-pragmatics.md, historical-linguistics.md, language-contact.md, writing-systems.md, naming-systems.md; myth/symbol — ../myth-symbol/symbolism-synthesis-method.md, comparative-frameworks.md, ritual-liminality.md, color-symbolism.md; era/costume — ../culture-material/era-periodization-models.md, costume-semiotics.md, textile-technology.md, sumptuary-law-rank-display.md; sibling boundary — lore-shokunin owns canon and world-bible consistency verification, while this entry supplies local design constraints and reference cautions only

## 1. Calibration: what closure does and does not claim

- **Design policy:** a closed grammar has a declared inventory, admissible transformations, and explicit exceptions; closure means that a new interpretation requires a recorded derivation or revision, not an improvised dictionary entry.
- **Not an ethnographic law:** one-symbol/one-primary-domain is a retrieval constraint for fictional design. Turner's Ndembu studies demonstrate contextual, multiple readings; they do not establish a universal single-meaning code (Turner 1967).
- **Primary is not exclusive, oldest, sacredest, or unanimous:** it is the registered default within a stated interpretation context. A participant's contrary reading may itself be designed and documented.
- **Evidence labels:** `ATTESTED` = source supports this dated occurrence; `INFERRED` = analyst reconstruction; `PROPOSED` = fictional design option; `UNKNOWN (to-verify)` = unresolved empirical claim. Do not substitute any of these for lore's canon-adoption status.
- Source checks on 2026-10-17 established bibliographic records, available descriptions, the Peirce guide, and Traugott–Dasher's publisher abstract through DOI metadata; they were not a page-by-page verification of every book.
- Recheck when transferring a claim to a new tradition, changing edition, or asserting a precise historical date. Exact quotations and detailed historical assignments need their own passage/object references.

## 2. Frameworks translated into limited craft operations

| Framework | Usable distinction | Operation in a fictional grammar | Calibration |
|---|---|---|---|
| Peircean sign relation | sign-vehicle, object, interpretant | distinguish visible mark, what it refers to, and a reader's interpretation | interpretant is not simply another name for the reader; this table simplifies a larger theory |
| Icon / index / symbol, CP 2.247–249 | resemblance / factual connection / conventional rule | record why a carrier supports a reading | one artifact can work in several ways; a painted flame is not physical evidence of a fire |
| Turner's ritual-symbol analysis (1967) | multiple meanings in situated ritual use | register exegesis, use context, and competing readings | Ndembu fieldwork is not a universal African or human symbol dictionary |
| Eco's signification / communication distinction (1976) | a signifying relation versus its use in a communicative process | separate available code from a particular act of display | the finite ledger below is this lane's tooling, not Eco's prescribed schema |
| Historical pragmatics (Traugott & Dasher 2002) | contextual inference can become conventional meaning | model repeated bridge uses before a default reading changes | evidence concerns linguistic change; applying it to badges and costume is a stated analogy |
| Historical dress study (Paoletti 2012) | color associations change with clothing practice and media | date a costume reading rather than projecting it backward | study concerns American children's dress, not every gender system or every society |

## 3. Define the lookup key before assigning a meaning

- Use `family_id` for a recognizable motif lineage; use `symbol_id` for a registered sign within that family. Track relationships rather than silently allocating new IDs to hide contradictions.
- Define context `c = {region, language/lect, era, institution/tradition, occasion, medium, reader_group}`. Write `ANY` for an intentional wildcard and `UNKNOWN` for missing information; never silently treat absence as a wildcard.
- For a fully resolved active symbol/context, `primary(symbol_id, c)` returns exactly one domain. An uncovered context returns `UNSPECIFIED`; incomplete context may return alternatives; unresolved rival assignments return `CONTESTED`, never an invented universal default.
- Define domains by **inclusions, exclusions, and contrasts**. `SWORN-OBLIGATION` can include witnessed vows and exclude ordinary promises; `power/life/goodness` is several domains masquerading as one.
- Scope defaults from general to specific only where the inheritance relation is declared. A temple tradition crossing political borders need not inherit the capital's court code.
- If two applicable overrides disagree, require an explicit resolution or mark `CONTESTED`; specificity alone cannot settle intersecting region and institution scopes.
- Keep `denotation`, `evaluation`, and `authority` separate: death need not mean evil; an emblem associated with justice need not prove that its wearer holds judicial office.

| Required record | Minimum content | Audit failure |
|---|---|---|
| Identity and carrier | family/symbol IDs; shape, orientation, color/material distinctions; word or script form if relevant | the same description unintentionally identifies different signs |
| Context and time | region/lect, tradition, medium, readers, occasion; valid interval and calendar basis | an unqualified statement claims a whole civilization or all eras |
| Primary domain | controlled ID, definition, default interpretation | multiple roots in the same resolved scope |
| Secondary readings | operator, source reading, target reading, activation context | an association has no derivation or limiting context |
| Ground and agency | resemblance, material link, convention, teaching/enforcement agent | an analyst's plausible story is presented as participants' knowledge |
| Provenance and status | source locator or `PROPOSED`; confidence; rival accounts | a museum label, legal prescription, or outsider gloss becomes universal practice |

## 4. Invariants for a closed symbolic grammar

1. **One scoped sign, one primary domain.** Recurrent independent roots require a scoped branch, a recognized homonym, or an unresolved dispute—not an ever-longer gloss.
2. **No unlicensed satellites.** Every secondary reading has a typed edge back to a registered root, with a stated occasion and reader group.
3. **No unmarked synonymy.** Different signs may share a domain, but record the contrast: elite/common, public/restricted, local/imported, spoken/written, or historically competing.
4. **Alignment is not identity.** A color associated with an animal does not inherit every story, taboo, or costume use of that animal. Mark links as `associated-with`, `substitutes-in`, or `equivalent-in`, with scopes.
5. **No automatic transitivity.** `color → animal → deity` does not license `every colored object → deity`; supply a composition or metonymy rule.
6. **No obligatory total cosmology.** The seed method's color/animal/number/celestial/direction matrix may contain reasoned `UNALIGNED` cells; absence of a documented link is not a mandate to invent one.
7. **No automatic symbolic promotion.** Not every animal, pigment, stitch count, or person's name must enter the code. Distinguish marked use from practical or incidental occurrence.
8. **No silent updates.** A changed primary domain, carrier contrast, reading context, or transformation creates a dated revision and an impact review.
9. **Separate recognition from legitimacy.** A counterfeit may be readable but unauthorized; a foreigner may see the mark without knowing the code; a ritual specialist may dispute a ruler's interpretation.
10. **Preserve intentional uncertainty.** Closed designer documentation can specify several in-world interpretations without deciding which is metaphysically true.

- When adopting ../myth-symbol/symbolism-synthesis-method.md §5's strict profile, retain its satellite cap of three, indexical-grounding quota, and three-compound productivity check as declared project settings. These are craft limits, not scholarly findings or universal cultural requirements.
- A claimed index needs its actual connection specified: expensive pigment can index access to supply; the same hue reproduced cheaply does not automatically retain that evidential force.

## 5. Licensed transformations: derivation, not free association

| Operator | Required bridge | What must remain explicit | Typical rejection |
|---|---|---|---|
| Metonymy / synecdoche | a practice-based relation, such as instrument → office | who recognizes the relation and in which setting | resemblance alone passed off as institutional authority |
| Metaphor | a named comparison and mapped property | which properties transfer and which do not | a predator emblem imports every predator trait |
| Ritual inversion | a documented reversed relation during a bounded rite | trigger, participants, ending, and ordinary reading restored afterward | arbitrary negative meaning assigned whenever convenient |
| Event-index | an event links carrier and memory | event date, commemorating group, media of transmission | the later emblem is projected into the event itself |
| Borrowing / reinterpretation | an adoption channel or explicitly proposed contact history | donor reading, recipient reading, adoption interval | identical shapes treated as proof of diffusion |
| Homophone / graphic rebus | relevant sound or graphic relation | lect, pronunciation stage, script, literacy, and register | modern pronunciation used to explain an earlier written motif |
| Taboo substitution | an avoidance relation and replacement practice | who avoids what, before whom, and whether the replacement later becomes taboo | every unexplained synonym labeled a euphemism |

- Link derived readings to the relevant source root; record each edge in a chain. Do not allow repeated loose metaphors to make any symbol mean anything.
- If a satellite becomes the unmarked reading in a scoped community, propose a primary-domain revision; do not preserve an obsolete default merely to keep the table tidy.
- Operators are permissions, not predictions: a culture need not exploit every available homophone, ecological analogy, or category anomaly.

## 6. Regional variance and reader-relative meaning

| Variation type | Keep invariant | Register the difference | Resolution rule |
|---|---|---|---|
| Allography | sign identity and primary domain | permitted stroke, weaving, carving, or print variants | test whether trained readers treat the difference as contrastive |
| Material substitution | domain, only if locally recognized | unavailable dye/fiber, substitute appearance, cost and durability | a replacement material is not automatically an equivalent ritual object |
| Ecological substitution | declared ritual function | replacement animal/plant and local explanatory bridge | retain a scoped substitution edge, not a global synonym |
| Sense specialization | parent domain | narrower local application | verify that the specialization remains inside the parent's definition |
| Divergent primary reading | family resemblance only | region/tradition branch and domain change | resolve by context; if context is unknown, return alternatives |
| Rival claim / appropriation | the observable carrier | who asserts continuity, who contests it, and since when | preserve disagreement rather than selecting a single culture-wide voice |
| Diaspora / revival | documented or proposed lineage | transmission gaps, reinterpretation, selective archaism | neither freeze the group in the donor's era nor assume total assimilation |

- Distinguish production region, wearer's affiliation, intended audience, and place of encounter. A traded garment may be made in one code and read in another.
- Record a cross-border misreading as a pair: `intended under code A` / `inferred under code B`. Such a mismatch can be an internally consistent result.
- Similar shapes or domains in unrelated cultures need not imply contact: conventional form, practical constraints, coincidence, or independent invention remain alternatives unless evidence decides.

## 7. Era drift: mechanisms and minimum causal records

| Mechanism | What may change | Minimum transition evidence or proposed design bridge | Coupled review |
|---|---|---|---|
| M1 Material / economic | affordability, authenticity cues, preferred carrier | supply or production change plus actual uptake | dye/fiber lexicon, costume access, sumptuary practice |
| M2 Political / religious overwrite | legitimacy, official interpretation, permitted wearers | authority's intervention and uneven acceptance/resistance | pantheon titles, oath formulae, insignia, naming taboos |
| M3 Media standardization | form, reproducibility, distribution, reader training | coin/print/textile convention and its reach | script, reproduction constraints, teaching and literacy |
| M4 Linguistic change | rebus, epithet, pun, lexical valuation | dated form/meaning relation and a plausible transmission chain | sound change, lect split, name formation, ritual archaisms |
| M5 Contact / borrowing | imported sign, domain, or composite | contact channel, donor attribution where supportable, recipient reinterpretation | loanwords, script use, textile routes, translated myths |
| M6 Event-index | commemorative or stigmatized reading | event, interpreting group, and later commemorative practice | chronicle wording, festivals, mourning dress, personal names |

- These are the seed method's mechanism labels, not an exhaustive scholarly taxonomy. Several may act together; record causal roles rather than assigning a single magic cause.
- Use a transition record: `{family_id, scope, old_primary, bridge_uses, new_primary, trigger, adoption_interval, agents, dissent, residues, evidence_status}`.
- Historical-pragmatic analogy: occasion-bound inference → repeated bridge use → conventional secondary reading → possible new default (Traugott & Dasher 2002). It is not a mandatory sequence for every visual sign.
- A decree supplies a prescription date, not proof of instant population-wide uptake. Permit overlapping old/new codes in different institutions, age groups, regions, and media.
- Retain non-adoption and reversal as outcomes. A campaign may fail; a displaced reading may survive in an enclave; a revival may reconstruct rather than restore it.

## 8. Era staging without an evolutionary ladder

| Optional stage | Record | Language / myth / costume coupling |
|---|---|---|
| Local usage | bounded occurrence and reader community | vernacular term, situated rite, locally available carrier |
| Institutional selection | a body teaches or privileges a reading | title/epithet, authorized story, garment or badge rule |
| Wider circulation | new media/users encounter the sign | loans, translated exegesis, standardized motif production |
| Contest / re-keying | competing interpretations and adoption intervals | rival names, doctrinal accounts, prohibited or reworked dress |
| Residue / revival | where an older reading survives or is reconstructed | fossil idiom, liturgical spelling, heirloom, antiquarian costume |

- Stages may overlap, repeat, or never occur. They are not labels for primitive → civilized progress, and a region is not “behind” simply because its code differs.
- Track separate dates for artifact manufacture, inscription/reworking, source composition/copying, and the event described. A later chronicle can tell an older event in the chronicler's code.
- First surviving attestation establishes presence by that date, not invention on that date; distinguish document survival from origin and flag uncertain dating or retrospective testimony.
- If dates are uncertain, use interval bounds plus the uncertainty basis. Do not make a precise primary-domain switch from a broad stylistic period alone.

## 9. Cross-system checks and productive composition

| Interface | Question to resolve | Prevented error |
|---|---|---|
| Language / symbol | do the relevant lect, sound stage, and script permit the claimed wordplay? | a rebus that works only in a modern translation |
| Myth / symbol | is this story an asserted origin, a later explanation, or the designer's causal proposal? | a myth treated as transparent historical evidence |
| Era / symbol | which version would this reader know at this date? | a modern interpretation assigned to an ancestral speaker |
| Costume / symbol | can the carrier be made, worn, seen, and recognized in this setting? | a tiny woven motif read like an enlarged modern illustration |
| Rank / symbol | who is allowed to display it, and what practice supports that permission? | symbolic association mistaken for legal entitlement |
| Naming / symbol | is the emblem-name actually productive in this naming system and era? | every person renamed after a later official emblem |

- Declare compound syntax: head versus modifier, ordering, orientation, enclosure, repetition, and which combinations are inadmissible. Adjacency alone need not produce a composite meaning.
- Separate `DECODED` (a licensed conventional reading), `INFERRED` (a reader's contextual guess), and `UNINTERPRETABLE` (no licensed composition). Productivity must not become permission to decode arbitrary imagery.
- For each new compound, record component versions, applicable composition rule, expected reading, reader group, and a plausible competing reading. Test positive and negative cases.

## 10. The symbol-audit procedure

1. **Freeze the proposal scope:** name packet revision, era intervals, regions, traditions, media, and intended readers. This is a local method audit, not a world-bible canon verdict.
2. **Inventory occurrences:** include glossary claims, myth passages, names, calendars, badges, costume descriptions, and historical notes; assign family/symbol IDs and source locators.
3. **Resolve context:** apply only declared inheritance/override rules; list uncovered contexts and overlapping incompatible definitions. Do not “fix” them by guessing author intent.
4. **Check roots and edges:** one resolved primary domain; satellites licensed; shared-domain signs contrasted; inversions bounded; `UNALIGNED` cells explained; project profile limits satisfied.
5. **Check carriers and access:** rendering distinctions survive actual media; production is feasible; wearer authorization, counterfeit recognition, and reader knowledge remain separate.
6. **Check chronology:** every changed assignment has a transition record; each scene/claim uses an available reading; old objects and new annotations are distinguished; prescribed and practiced codes are not conflated.
7. **Trace impact:** follow typed links into language, myth, names, era staging, and costume. Re-audit only implicated meanings; do not automatically propagate every change across the cosmology.
8. **Run probes:** ordinary use, regional encounter, ritual inversion, unfamiliar compound, inherited object, and changed pronunciation. Write expected and actual interpretations, including an expected refusal to decode.
9. **Triage findings:** `CONTRADICTION` = incompatible unqualified commitments; `UNDERDOCUMENTED` = missing scope/derivation/evidence; `INTENTIONAL-DISPUTE` = incompatible voices whose disagreement is modeled. The last is acceptable only when its limits are explicit.
10. **Hand off:** symbol ledger, scoped variant map, era transitions, compound rules, occurrence/probe results, collision log, and unresolved evidence questions. Lore-shokunin alone chooses adoption and performs world-bible verification.

- Audit result: `READY-FOR-REVIEW` when the declared packet has no unresolved contradictions or missing required fields; `BLOCKED` when it does. Deliberate unknowns remain visible and cannot support definitive historical claims.
- Collision log fields: finding ID, occurrence locators, affected contexts, violated rule, proposed repair, impacted dependencies, retest result. Preserve the superseded proposal's identity.
- Repairs in preference order: restore missing context; correct a mistaken occurrence; license a justified derivation; split a genuine homonym/branch; propose an actual grammar revision. Do not invent a historical explanation just to silence a warning.

## 11. Synthetic audit fixture — method demonstration, not proposed canon

- All IDs, regions, eras, events, and assignments below are disposable test variables with status `PROPOSED`; none names an existing fictional-world entity or a historical tradition.
- Let family `K` use a closed-knot motif. In region `A`, era `E0`, symbol `K17` has primary `SWORN-OBLIGATION`; its registered carrier variants are carved and embroidered depictions of the same motif.
- The test defines an authorized oath-officer's sleeve display as a metonymic satellite in an official ceremony, not a general permission for any wearer to claim office.
- In region `A/E1`, a stipulated institutional seizure re-keys the public code to `OFFICIAL-FORFEITURE` through M2; region `B/E1` retains the E0 primary. The changed branch and its adoption interval are explicit.

| Probe | Expected result | Reason |
|---|---|---|
| K17 carved rather than embroidered, A/E0 | same primary | carrier variation is licensed |
| K17 on a stranger's sleeve, A/E0 | obligation association; office authorization unproven | recognition does not establish entitlement |
| Same motif, B/E1 | sworn obligation | A's political revision is not B's default |
| Same motif, A/E1 public official code | official forfeiture | the scoped transition changes the default |
| E0 heirloom displayed in A/E1 | current public reading differs from its documented old use | artifact age does not force a contemporary viewer's interpretation |
| A/E0 passage glossed “forfeiture” without framing | contradiction | later branch projected backward |
| Unregistered knot-plus-bird compound | uninterpretable by this grammar | no composition rule is supplied |

- A claimed sound-based pun for K17 remains `UNKNOWN (to-verify)` until the relevant lexical forms, sound stage, and audience are supplied; no token etymology is invented to complete the fixture.

## 12. Reference uptake: complete civilization context, not emblem shopping

| Dossier field | Minimum context before borrowing a real tradition's symbolic mechanism |
|---|---|
| Language family and writing | actual language/lect and affiliation; script and orthographic period; spoken versus literate access |
| Mythic / pantheon core | named tradition, attested sources, ritual setting, internal alternatives; do not require a pantheon where none fits |
| Symbolic system | carrier, domain, exegesis, user/reader community, rival interpretation, provenance |
| Era model | local chronology and region; distinguish ancient use, later commentary, reconstruction, and modern revival |
| Costume / material signature | fiber, cut, dye, production/trade, class/rite constraints; surviving objects versus normative images |
| Naming practices | personal/place/title formation, transmission, taboo, register, and dated emblem-name relations |

- Paoletti (2012) is a bounded control case: American children's clothing and changing gender distinctions, examined through advertising, catalogs, baby books, and other media. It supports historical contingency, not a universal date on which all pink/blue meanings reversed.
- Turner (1967) is a bounded ritual-symbol case: Ndembu fieldwork in Zambia. Do not promote its account into a whole continent's cosmology or fill absent language, naming, and costume information from neighboring peoples.
- For thinly documented traditions, chronicle evidence may be late, elite, adversarial, or absent; that is a limit on the dossier, not evidence of cultural simplicity. Keep unresolved fields `UNKNOWN (to-verify)`.

## What a worldbuilder can take

- A small, learnable inventory with scoped defaults; typed secondary meanings; regional branches; uneven dated transitions; and productive rules that can also refuse an interpretation.
- Coherence without unanimity: a symbol may remain stable while laws, reader groups, costume carriers, and valuations diverge. An internally consistent misreading is usable design, not automatically an error.
- A reviewable packet of alternative mechanisms and their consequences for language, myth, era, naming, and costume. No assignment here establishes canon or writes to lore-shokunin's bible.

## Provenance cautions

- **Well-supported distinctions, limited transfer:** Peircean sign relations, context-sensitive ritual interpretation, and documented semantic/dress change are useful analytical resources; the closed inventory, primary-domain rule, caps, ledger, and audit verdicts are authored craft policy.
- **Contested interpretation:** a participant's gloss, a scholar's reconstruction, and a designer's analogy answer different questions. Multiple testimonies need not collapse into one concealed “true meaning.”
- **Colonial and institutional bias:** do not treat an outsider ethnographer, missionary chronicle, court decree, or collector's label as an unmediated community voice. Record translator, collection setting, access restrictions, and whose testimony is missing; assess each source rather than presuming equal reliability.
- **Unsupported pop frameworks:** timeless color/personality tables, universal dream-symbol dictionaries, and fixed Jungian-style decoding are not established cross-cultural lookup systems. Use them, if desired, as explicitly invented ideology or idea prompts, not evidence about a living tradition.
- **Thin coverage:** this entry does not establish specialist coverage of every tradition, verify a full civilization dossier, or settle restricted/sacred meanings. Missing chronicle or material evidence stays missing; mark the particular proposed historical claim `(to-verify)` rather than inventing a source or a continuous lineage.
