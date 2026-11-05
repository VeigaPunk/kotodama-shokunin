# Round 93 — grader v4 and a greeting-formulae entry

Claims O (operability) and C (coverage) are exactly as frozen at freeze commit `174fd5a8e05b3919a7854a4495c2fe0f28080775` (revision 2; base `8b2ce60a7bbf015f42a6c9e5c45e994e4c2f7742`).

## Gate

Candidates considered: the DOAJ article API result page for each of the five query strings named in the search log below, deduplicated by DOI, or by the full-text URL where the record carries no DOI (one article appears twice in the API, as a journal page and as a download stub for the same text). That set holds 38 distinct records, measured 2026-11-05 by deduplicating the five API responses from `curl -sS "https://doaj.org/api/search/articles/<query>?pageSize=10"` over the five query strings below. Four articles in the set were opened and are the admitted rows below; two were unreachable and are recorded as not rows; the remaining 31 candidates are listed below with one reason each for not being opened.

- S961 admit A/mined. https://bop.unibe.ch/linguistik-online/article/view/1426 — accessed 2026-11-05 — body: “the speech acts of greeting and leave-taking denoted by the German verb”
- S962 admit A/mined. https://pressto.amu.edu.pl/index.php/srp/article/view/21548 — accessed 2026-11-05 — body: “despite their apparent formal resemblance, came to codify totally opposite”
- S963 admit A/mined. https://bop.unibe.ch/linguistik-online/article/view/3847 — accessed 2026-11-05 — body: “greetings tend to be brief today”
- S964 admit A/mined. https://oaj.fupress.net/index.php/ss/article/view/17732 — accessed 2026-11-05 — body: “compiled a pool of words, expressions, and sayings”

Search method: the DOAJ article API, `https://doaj.org/api/search/articles/<query>`, queried on 2026-11-05 with five query strings — `greeting formulas`, `greetings ritual`, `farewell formulas`, `fórmulas de saludo`, `politeness formulae greeting` — returning 14, 10, 10, 10 and 10 results per query as the API returned them at search time. Those figures are the round's screen-time counts: the DOAJ index is live, and a re-run of the same five strings on the same day returns different totals, so the numbers are not a re-runnable invariant and only the screened set below is reproducible. The first result page of each query was screened, and that is what produced the candidate set. Four articles were opened by ordinary HTTP on 2026-11-05 and are the admitted rows above; every other candidate in the screened set was left unopened or was unreachable, as recorded below. Raw response bodies, sha256 digests and access instants for the four opened articles are in `reports/round-93/evidence/manifest.json`, with the captures beside it. Each candidate in the screened set was probed once on 2026-11-05 with a plain `curl` request (default user agent, no browser, no challenge passing, no verification disabled) while this search log was written, and the access outcomes quoted in the bullets below come from that run.

Unreachable candidates, recorded as not rows. The MDPI article "Pragmatic Variation in Greeting and Farewell Formulae in Rural Austria" (https://www.mdpi.com/2226-471X/11/9/179) returned HTTP 403 to the plain request and was not passed; the body served is an access-denied notice, not the article. The Esan and àlago article "Greeting Others: Hermeneutics Of The Greeting Ritual In The Esan And àlago Communities In Nigeria" (https://univ-bejaia.dz/revue/jslcs/article/view/394) failed TLS certificate verification on the plain request and was not retried with verification disabled. Neither candidate is a registry row.

DOAJ-listed candidates not opened, one reason each (reasons are about the record, not about the article's findings):

- "De l'essentialisation à la désincarnation des formules de salutations en Algérie" (Langues & Cultures, 2025) — on-topic (salutation formulae in Algeria), not opened this round, so unassessed and not a row.
- "DALLA PRAGMATICA ALLA SEMANTICA: USI METAFORICI DEI SALUTI DI CONGEDO IN ITALIANO" (Italiano LinguaDue, 2023) — on-topic (figurative use of Italian leave-taking formulae), not opened this round, so unassessed and not a row.
- "Fórmulas de saludo y de despedida como relacionemas" (Studia Iberystyczne, 2017) — on-topic (greeting and farewell formulae as relationemes), not opened this round, so unassessed and not a row.
- "Komunikační funkce věty a modalita v Česko-německé srovnávací gramatice Františka Štíchy" (Časopis pro Moderní Filologii, 2017) — greeting formulae appear as one item inside a contrastive grammar of sentence function and modality, so marginal to this entry's topic; not opened.
- "Politeness Speech Acts in the Speech of Children: Pragmatic Mistakes and Acquisition" (Taikomoji kalbotyra, 2019) — on-topic (greeting and farewell among the politeness speech acts), but the study's subject is child acquisition, not formulae; not opened this round.
- "Etiquette Formulas as Ethnolinguistic Components of Original and Translated 18th Century Kalmyk Official Texts" (Oriental Studies, 2021) — on-topic (etiquette formulae in historical letters), not opened this round, so unassessed and not a row.
- "The Concept of \"Greeting\" in the Russian and English Blogosphere" (Язык и текст, 2020) — on-topic (greeting in network communication), but the record's page returned HTTP 404 to the plain re-open; not opened, not a row.
- "\"Bow\" (\"Poklon\") in Komi Speech Etiquette Formulas" (Polylinguality and Transcultural Practices, 2026) — on-topic but restricted to one etiquette lexeme; not opened this round, so unassessed and not a row.
- "Orality in the cultural area of Bosnia and Herzegovina" (CM. Communication and Media, 2024) — off-topic: the record's subject is orality and literacy in social communication, not greeting formulae.
- "Views of childhood and knowledge of children" (South African Journal of Childhood Education, 2014) — off-topic: the record's subject is early-childhood schooling, not greeting formulae.
- "Easter Egg Symbolism in Lithuania Minor" (Acta Humanitarica Academiae Saulensis, 2025) — off-topic: the record's subject is ceremonial egg painting and holiday custom.
- "Символіка Зодіакального Кола в єврейському мистецтві Східної Галичини" (Studia Żydowskie, 2016) — off-topic: the record's subject is zodiac symbolism in art.
- "Celebrating the New Year in Byzantium" (Вестник Волгоградского государственного университета, 2023) — off-topic: the record's subject is Byzantine New Year custom.
- "The language of giving: Eid rituals and gift-giving practices among Saudi Gen Z" (Cogent Arts & Humanities, 2026) — off-topic: the record's subject is gift-giving; the plain re-open returned HTTP 403.
- "Singing on the Village Patron's Feast and New Year's Carols: The Case of the Village of Ugovizza" (Traditiones, 2023) — off-topic: the record's subject is caroling and village custom.
- "Classroom Greetings: More than a Simple Hello" (Iranian Journal of Language Teaching Research, 2020) — on-topic (greeting rituals in a classroom), but the record's scope is one teacher's practice; not opened this round.
- "Formulaicity and pragmatics of contact-terminating means in cinematic vs. artistic discourse: A corpus study" (Russian Journal of Linguistics, 2025) — on-topic (contact-terminating means), but the corpus is fictional dialogue; not opened this round.
- "\"Do Not Blame Anyone...\" The Suicide Note as a Trait of the Character's Image" (Достоевский и мировая культура, 2022) — off-topic: the record's subject is a literary suicide note and character image.
- "The Farewell Sermon: An Analytical Rhetorical Study" (آداب الرافدين, 1981) — off-topic: the record's subject is the rhetoric of a religious sermon; the plain re-open failed to resolve the host.
- "Means of Implementing Phatic Communication in English-Language Film Dialogue: a Diachronic Aspect" (Дискурс, 2026) — on-topic (phatic markers including greetings) but restricted to film dialogue; not opened this round.
- "Toponyms in the Context of the Winter Farewell Rite on the Belarusian-Ukrainian" (Вопросы ономастики, 2023) — off-topic: the record's subject is toponymy in a seasonal rite; the plain re-open returned HTTP 500.
- "Etykieta językowa w Listach na wyczerpanym papierze Agnieszki Osieckiej i Jeremi Przybory" (Annales Universitatis Paedagogicae Cracoviensis, 2018) — greeting and farewell acts are one item among several speech acts in a letter corpus; marginal to this entry's topic; the plain re-open returned HTTP 403.
- "'Lleva marca, lleva calidad': el discurso comercial ambulante en el transporte público de Buenos Aires" (Oralia, 2021) — off-topic: the record's subject is street-vending commercial discourse.
- "Bendecir para saludar en Plauto. Redistribución de la función pragmática" (Emerita, 2017) — on-topic (Latin blessing formulae reinterpreted as greetings), not opened this round; the plain re-open failed TLS verification.
- "La dinámica del saludo en interacciones institucionales en español porteño" (Oralia, 2021) — on-topic (greetings in institutional interaction), not opened this round, so unassessed and not a row.
- "Andrzej Zieliński (ed.): Las fórmulas de saludo y de despedida en las lenguas románicas" (Anuario de Estudios Filológicos, 2022) — the record is a book review ("Reseña de libro"), so it reports another work rather than holding findings of its own; the plain re-open returned HTTP 403.
- "Las fórmulas de saludo en la era de los descubrimientos" (Estudios Hispánicos, 2024) — on-topic (greeting formulae in a historical period), not opened this round, so unassessed and not a row.
- "\"A las niñas no toca sino obedecer\". Comportamiento verbal y no verbal en las \"Reglas sencillas de cortesía para las niñas\" (1848)" (Boletín de la Sociedad Española de Historiografía Lingüística, 2024) — off-topic: the record's subject is a nineteenth-century conduct manual for girls.
- "La construcción discursiva en WhatsApp: relaciones demarcativas desde una perspectiva de género" (Círculo de Lingüística Aplicada a la Comunicación, 2024) — off-topic: the record's subject is demarcation in messaging, not greeting formulae.
- "Good morning, China! – czyli o dzień dobry po chińsku oraz o niektórych formach adresatywnych" (Postscriptum Polonistyczne, 2020) — on-topic (greeting formulae and address forms in Chinese), not opened this round; the plain re-open failed TLS verification.
- "Some Remarks on Language Usage in Late Babylonian Letters" (Open Linguistics, 2017) — on-topic (greeting formulae and terms of address in ancient letters), not opened this round; the plain re-open returned an empty 202 response from the publisher front door.

## Mistakes

| id | class | evidence | captured-by | fix |
|---|---|---|---|---|
| R93-M1 | survivor | the first v4 mutation run scored 80/83 with survivors dispo-anchor-revert, gap-lesson-graded-off and head-qualify-off: the negatives passed through another leg, so each fixture named a leg it did not isolate | none | each v4 negative now pins the exact failing leg (chk_leg), and the fixtures were isolated; red-before 80/83, after 83/83, receipt reports/round-93/mutation-score.txt |
| R93-M2 | vacuous | the round-92 search log excluded sixteen candidates by title only, with no per-candidate reason, per the round-92 spot-check §4 at corpus/lessons/round-92-verifier-spotcheck.md | none | QUALITY criterion 37 below, and this round's search log gives a reason per exclusion |
| R93-M3 | stale-premise | the round-92 claim C before-description says sound-symbolism.md has no ideophone-class entry, but §6 holds one | none | corrected below as an append-only erratum, not by editing the frozen round-92 text |

Proposed QUALITY criterion 37, for the integrator to land in corpus/QUALITY.md: a rejected candidate carries a topic or access reason on record; title-only triage is not an exclusion, and a candidate that could not be fetched is recorded as unassessed for access rather than rejected.

## Corrections

Append-only. The round-92 bytes are not edited; the round-92 sentences named here stand as filed, with the following errata.

1. The round-92 Gate sentence beginning "Excluded (16), as read from the DOAJ records:" calls the Signifiances item "a French study of vocalic alternation in ideophones". The article is French-language and concerns Turkish ideophones.
2. The round-92 claim C surface sentence beginning "The nearest owners are corpus/knowledge/linguistics/sound-symbolism.md" describes that file as holding "no ideophone-class entry". Sound-symbolism.md §6 already holds an ideophone word-class definition, grammar profile, reduplication and a register procedure, as the round-92 spot-check §2 records; the round-92 claim is a dedicated-entry gap and the counter measures that gap, so the verdict does not move.

## Quarantine

The round-91 register verdicts stand: 21 rows, LOCATED 3, PARTIAL 3, ABSENT 10, UNREACHABLE 3, UNVERIFIABLE 2. Nothing was adopted this round. The id-collision guard was not run this round, because there was no package adoption.

## Assimilation

None: this round adopted no package, so there was nothing to assimilate. The lane directory `considerthese/` does not exist (`ls -d /home/vgpnk/Projects/shokunin/kotodama-shokunin/considerthese` returned rc 2, no such file or directory, 2026-11-05).

## Understanding

The four opened sources support four separable readings and do not support a fifth.
S961 supports the speech-act reading: greeting and leave-taking are one act family denoted by one German verb, Swiss speakers hold that greeting formulae are especially important among their politeness rituals, and the study reports erosion of those conventions over time in the English-speaking world.
S962 supports the divergence reading: two formulae built on the same Spanish predicate came to codify opposite social values, so formal resemblance fixes neither meaning nor politeness.
S963 supports the contact reading: under pervasive contact with Swahili, Ngoni greetings tend to be brief today and code-switching is widespread, and older community members read the preference for Swahili as a lack of respect.
S964 supports the situated-inventory reading: a pilot questionnaire elicited situationally bound responses and compiled a pool of words, expressions and sayings that speakers reported using when saying goodbye to acquaintances and strangers, and the study reports that parting interactions are context-sensitive rather than fixed; it is a pilot study, not a population sample.
The design rules of the fictional greeting register go beyond what these four sources carry and are the author's design (design, not sourced): a register separating an access ritual from a courtesy token, a leave-taking slot with a negotiated closing, a contact-driven shortening rule with a politeness cost, and a step-by-step procedure for building a greeting repertoire for an invented culture; no claim about canon, lore acceptance, real-world rights or cultural permission is made or implied, the entry is NON-CANON and lore alone decides canon.

## Spot-check

Pending non-author spot-check (LEARNING.md). No box is marked here.
