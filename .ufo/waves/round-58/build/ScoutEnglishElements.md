# ScoutEnglishElements — claim C source item (English place-name elements), round 58

Seat: KotodamaR58A2.ScoutEnglishElements. S-ids assigned: S514, S515. Both offered; both pass rowcheck on all four legs (LOCATE, BOILER, RELEVANCE, TOPIC).
Both URLs are new to corpus/SOURCES.md (`grep -cF` = 0 for `nottingham.ac.uk/research/groups/ins/resources/vocabulary.aspx` and `kepn.nottingham.ac.uk/about`). Both are reached by a plain GET (curl and the instrument's own fetch) that returns HTTP 200, with no challenge or login. The two rows sit on different hosts (`www.nottingham.ac.uk` and `kepn.nottingham.ac.uk`), so they count toward the DISTINCT 10-host floor as two hosts.

Worldbuilder design decisions these rows cover: what a name is built from (elements), which language layer an element belongs to (S514), and what English settlement names typically name (S515).

## S514 — Vocabulary of English Place-Names (INS, Nottingham)

Registry row:

| S514 | Institute for Name-Studies, University of Nottingham, n.d., "Vocabulary of English Place-Names" — https://www.nottingham.ac.uk/research/groups/ins/resources/vocabulary.aspx (direct, HTTP 200) | web | A | that English place-name elements derive from several languages and mirror England's linguistic history | body ¶2: "These words - or place-name elements - reflect the rich diversity of England's linguistic history" | Place-name elements, the words from which English names are built, mirror the varied linguistic history of England. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

Gate line:
- S514 — https://www.nottingham.ac.uk/research/groups/ins/resources/vocabulary.aspx — accessed 2026-10-23 — body ¶2: “These words - or place-name elements - reflect the rich diversity of England's linguistic history”. Grounds: Place-name elements, the words from which English names are built, mirror the varied linguistic history of England. Seat: ScoutEnglishElements.

Quote note: the quote is the full main clause of the sentence. The sentence continues "and derive from Norse, French, British Celtic, Irish, and Latin, as well as from English in its various stages of development" (37 words in all, over the 25-word cap). The page serves the hyphens in "place‑name" as U+2011; the locator's normalisation treats them as spaces, and LOCATE passed.

draft sentences:
- An English place-name is built from words called place-name elements, and the Vocabulary of English Place-Names aims to record every such word found in any place-name recorded before about 1750 (S514).
- These elements mirror the linguistic history of England: the Vocabulary traces English place-name elements to Norse, French, British Celtic, Irish and Latin as well as to English in its various stages (S514).
- The Vocabulary's element words come from both major names and 'minor' names such as field-names and street-names, so the name elements of England's linguistic history survive at every scale of place (S514).

## S515 — About KEPN (Key to English Place-Names, INS, Nottingham)

Registry row:

| S515 | Institute for Name-Studies, University of Nottingham, n.d., "About - KEPN" (Key to English Place-Names) — https://kepn.nottingham.ac.uk/about (direct, HTTP 200) | web | A | what English village and town names typically refer to and how old they are | About ¶2: "The names of villages and towns frequently refer to particular people(s), social and administrative activities, landscape, birds and animals, crops and vegetation" | English village and town names usually describe a person or group, local activities, the landscape, wildlife, or the crops grown there. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

Gate line:
- S515 — https://kepn.nottingham.ac.uk/about — accessed 2026-10-23 — About ¶2: “The names of villages and towns frequently refer to particular people(s), social and administrative activities, landscape, birds and animals, crops and vegetation”. Grounds: English village and town names usually describe a person or group, local activities, the landscape, wildlife, or the crops grown there. Seat: ScoutEnglishElements.

Quote note: the quote is the first main clause of the sentence (21 whitespace words). The sentence continues ", and most of them are well over a thousand years old." The KEPN home page (`https://kepn.nottingham.ac.uk/`) serves only a navigation shell and "Loading map...", so BOILER cleared it.

draft sentences:
- The names of English villages and towns most often refer to particular people or peoples, to social and administrative activities, to the landscape, to birds and animals, or to crops and vegetation (S515).
- Most of these village and town names are well over a thousand years old, so the people, activities and landscape they name record how those places were perceived when they were named (S515).
- The Key to English Place-Names gives, for village and town names, a meaning and a break-down of the name into its elements and the language of each element (S515).

## rowcheck output

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutEnglishElements/rows.md` (exit 0):

```
S514 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.nottingham.ac.uk/research/groups/ins/resources/vocabulary.aspx | BOILER: root-clear https://www.nottingham.ac.uk/; not a title, h1 or meta label | RELEVANCE: shared=['eleme', 'engla', 'histo', 'lingu', 'name', 'place'] | TOPIC: quote_hits=1 function_words=3 page_hits=27 page_terms=23 need=1/2/3/2
S515 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://kepn.nottingham.ac.uk/about | BOILER: root-clear https://kepn.nottingham.ac.uk/; not a title, h1 or meta label | RELEVANCE: shared=['activ', 'crop', 'lands', 'name', 'town', 'villa'] | TOPIC: quote_hits=1 function_words=4 page_hits=6 page_terms=5 need=1/2/3/2
```

(The --entry legs (c) and (d) were not run because the entry does not exist yet. Each draft sentence reuses at least 2 content words from both its row's quote and its teaches cell: S514 uses place, name, elements, linguistic, history, England; S515 uses names, villages, towns, landscape, activities.)

## Gap: no row names tūn, hām, lēah or burh

The brief's target was explanations of specific generic elements (-tūn, -hām, -lēah, -burh). No ordinary-access Nottingham page I opened explains them in body text:
- KEPN (`https://kepn.nottingham.ac.uk/`) is a Next.js app. The served HTML and its 16 JS chunks expose only the routes `/`, `/about` and `/panel`, plus auth routes. Per-place and per-element data loads behind the map, and plain GETs do not reach it.
- `https://epns.nottingham.ac.uk/` (Digital Survey) resolves to the INS "Digital Survey of English Place-Names" description page and has no element text.
- I scanned 12 INS/EPNS static pages for `tūn|tun|hām|ham|lēah|leah|burh|-by|thorp|wīc|ingas`. The few hits were names (Burghal Hidage, Hartlepool, "simplex burh" as a paper title), not element explanations.
Only one opened source glosses tūn, hām and bȳ: an undergraduate essay on nottingham.ac.uk (rejected below). If the entry needs element-level glosses, it needs a different scout source (for example a printed EPNS/Gelling text with an open copy).

## rejected

- https://www.nottingham.ac.uk/english/documents/innervate/23-24/engl3013-andrina-bettschen.pdf — student essay (Innervate, Nottingham's undergraduate journal). It glosses tūn "farmstead", bȳ (Old Norse) and hām "homestead", and links hām to early English settlement. Rejected because undergraduate coursework is not an expert source a SUPPORT reviewer would defend as tier A/B. Content seen only in the web-search snippet; I did not run rowcheck on it.
- https://www.nottingham.ac.uk/research/groups/ins/resources/kepn.aspx — opened, HTTP 200. It carries the same element/language sentence as S515's page ("It will provide you with a meaning of the place-name as well as a break-down of the different parts of the name (its 'elements') and the language(s) of those elements"). That sentence has no NAMING-PLACE window near "elements", and S515 is the stronger page on the same project. Not offered (one row per project).
- https://www.nottingham.ac.uk/research/groups/epns/survey.aspx — opened, HTTP 200. Its sentence on 'major' names versus minor, field and street names is real but is about survey coverage, not name design. Not offered (cap of 2 rows; weaker fit).
- https://www.nottingham.ac.uk/research/groups/epns/ — opened, HTTP 200. Its River Trent news blurb (river name "older than previously thought") is a news teaser that links to BBC News, not a stated principle. Not offered.
- https://www.nottingham.ac.uk/research/groups/ins/index.aspx, .../ins/resources/index.aspx, .../ins/projects/index.aspx, .../ins/projects/deep.aspx, .../ins/resources/digital-survey-of-english-place-names.aspx, .../ins/resources/finding-medieval-landscape-names/finding-medieval-landscape-names.aspx, .../ins/projects/past-projects/{perceptions-of-place, travel-and-communication, impact-of-diasporas, suffolk-place-names, landscapes-of-governance}.aspx, .../ins/projects/{the-place-names-of-shropshire, street-names-planning-and-public-policy, learning-through-language/home}.aspx — opened as navigation or for the element scan. These are project and institutional descriptions with no element-meaning or name-design sentence worth a row.
- https://www.nottingham.ac.uk/research/groups/ins/projects/survey-of-english-place-names.aspx — HTTP 404 (guessed path); not used.
- http://www.beeston-notts.co.uk/morrell5.shtml — seen only as a web-search result (a local-history glossary table of elements). Not opened as a source, and the glossary is table cells, which a quote cannot use. Not offered.

## installs

None.
