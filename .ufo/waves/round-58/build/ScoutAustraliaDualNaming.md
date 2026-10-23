# ScoutAustraliaDualNaming — round 58, claim C source item (S510, S511)

Seat: KotodamaR58A2.ScoutAustraliaDualNaming. Both pages were opened 2026-10-23 with plain curl and urllib GETs. Neither URL is in corpus/SOURCES.md: `grep -F` for `environment.nt.gov.au` and `land.vic.gov.au` returned nothing.

Two rows are offered. Both pass all four rowcheck legs.

## S510 — Northern Territory Place Names Committee guidelines

(1) Registry row:

| S510 | Northern Territory Government, Department of Lands, Planning and Environment, Place Names Committee, 2026 (page modified 2026-05-13), Guidelines for NT place naming — https://environment.nt.gov.au/boards-committees/place-names-committee/guidelines (direct, HTTP 200) | docs | A | Northern Territory committee preference for Aboriginal names on features with no registered name | section Aboriginal and dual names, first paragraph: "Aboriginal names for geographic or topographic features are preferred where a place does not have a name that has previously been registered." | Where a Northern Territory geographic feature has no registered name yet, the committee prefers to give it an Aboriginal name. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

(2) Gate line:
- S510 — https://environment.nt.gov.au/boards-committees/place-names-committee/guidelines — accessed 2026-10-23 — section Aboriginal and dual names, first paragraph: “Aboriginal names for geographic or topographic features are preferred where a place does not have a name that has previously been registered.” Grounds: Where a Northern Territory geographic feature has no registered name yet, the committee prefers to give it an Aboriginal name. Seat: ScoutAustraliaDualNaming.

draft sentences:
- In the Northern Territory, Aboriginal names are preferred for geographic or topographic features that have no previously registered name (S510).
- So in the Northern Territory, which language the first registered name comes from is set by the naming committee's rule, not by whoever happens to name the place first (S510).
- A worldbuilder can copy this order: a geographic feature with no registered name is a gap, and the naming committee prefers to fill it with an Aboriginal name (S510).

## S511 — Geographic Names Victoria, Aboriginal place naming: how to get started

(1) Registry row:

| S511 | State of Victoria, Department of Transport and Planning, Geographic Names Victoria, 2020 (page last updated 2021-10-28), How to get started (Aboriginal place naming) — https://www.land.vic.gov.au/place-naming/aboriginal-place-naming/how-to-get-started (direct, HTTP 200) | docs | A | Victorian naming authority's stance that Aboriginal feature names are preserved although they rest on a non-western concept of place | page body, opening paragraph: "While these features are defined differently to western concepts of place, their Aboriginal names are just as important to preserve." | Victoria's naming office says Aboriginal names for features deserve preservation even though Aboriginal definitions of a feature differ from western ideas of place. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

(2) Gate line:
- S511 — https://www.land.vic.gov.au/place-naming/aboriginal-place-naming/how-to-get-started — accessed 2026-10-23 — page body, opening paragraph: “While these features are defined differently to western concepts of place, their Aboriginal names are just as important to preserve.” Grounds: Victoria's naming office says Aboriginal names for features deserve preservation even though Aboriginal definitions of a feature differ from western ideas of place. Seat: ScoutAustraliaDualNaming.

draft sentences:
- Geographic Names Victoria says Aboriginal names for features are just as important to preserve, even though those features are defined differently from western concepts of place (S511).
- For a worldbuilder, this means an older people's name need not match a newcomer's feature one to one: what counts as the named place can differ between the two traditions (S511).
- A settler state that wants to preserve indigenous names therefore has to accept the names together with their own definition of the feature, not only as new labels on its own map divisions (S511).

## (3) rowcheck output

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutAustraliaDualNaming/rows.md` printed:

```
S510 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://environment.nt.gov.au/boards-committees/place-names-committee/guidelines | BOILER: root-clear https://environment.nt.gov.au/; not a title, h1 or meta label | RELEVANCE: shared=['abori', 'featu', 'geogr', 'name', 'prefe', 'regis'] | TOPIC: quote_hits=1 function_words=6 page_hits=25 page_terms=10 need=1/2/3/2
S511 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.land.vic.gov.au/place-naming/aboriginal-place-naming/how-to-get-started | BOILER: root-clear https://www.land.vic.gov.au/; not a title, h1 or meta label | RELEVANCE: shared=['abori', 'defin', 'diffe', 'featu', 'name', 'place'] | TOPIC: quote_hits=1 function_words=5 page_hits=53 page_terms=7 need=1/2/3/2
exit 0
```

Both rows have 11 cells. The teaches cells are 20 words (S510) and 23 words (S511).

## Note for L1: the dual-naming rule itself cannot be a row

The same NT section's fourth paragraph states the dual-naming rule: "Dual names are preferred for geographic or topographic features where a place has a previously registered non-Aboriginal name and there is an Aboriginal name (or names) for the place." The full sentence is 30 normalised words, which is over the 25-word cap. Cut down to 25 words, it fails TOPIC: "names" is four words from "geographic", and the window allows three. Observed rowcheck output for that cut-down quote:

`S510 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC FAIL | ... TOPIC: quote_hits=0 function_words=4 page_hits=25 page_terms=10 need=1/2/3/2`

The section's other dual-name sentences have no PLACE-stem word near a naming word, so they fail too. Because of that, no entry sentence cited to S510 should claim the dual-name rule. The rule is real page text; the row rules just cannot carry it.

## rejected:

- https://www.anzlic.gov.au/ICSM — this is where every icsm.gov.au URL now 301-redirects, including the Principles for geographical naming, place-names and Dual Naming Guidelines PDF paths. Not offered because plain requests never got the page: curl over HTTP/2 exited 92 (`https://www.anzlic.gov.au/ICSM 000`), curl `--http1.1` timed out at 40 s with no body, and two sub-paths also returned `000`.
- https://www.icsm.gov.au/publications/principles-geographical-naming, https://www.icsm.gov.au/place-names, https://www.icsm.gov.au/sites/default/files/2018-05/Dual%20Naming%20Guidelines.pdf — not offered: each returns `301 https://www.anzlic.gov.au/ICSM`, which is unreachable (above).
- https://nt.gov.au/property/land-planning-and-development/place-names/dual-naming and .../place-names — not offered: HTTP 404.
- https://www.qld.gov.au/environment/land/title/addressing/placenames — not offered: HTTP 403, and I did not try to get past it (QUALITY criterion 10).
- https://www.sa.gov.au/topics/planning-and-property/land-and-property-information/geographical-names and .../planning-and-land-management/place-names — not offered: HTTP 404.
- https://www.sa.gov.au/topics/housing/planning-and-property/suburb-road-and-place-names — not offered: HTTP 200, but the served HTML has no body text. Lines over 50 characters, outside script/style/nav: only `SA.GOV.AU is licensed under a Creative Commons Attribution 4.0 Licence. © Copyright 2026`.
- https://uluru.gov.au/discover/culture/ (redirected from parksaustralia.gov.au/uluru/discover/culture/) — not offered: HTTP 200, but the only line matching name or Ayers is `Ayers Rock Resort & Yulara` (navigation). There is no Uluru / Ayers Rock dual-naming text.
- https://environment.nt.gov.au/boards-committees/place-names-committee/how-places-are-named — not offered. Its generic/specific sentence ("Generally a place name will have 2 parts, a unique identifying name (sometimes called a specific term) and a generic term that describes the type of place.") is 28 words, over the cap, and the clause that keeps the generic term has no NAMING word within 3 words of "place". There is a usable fallback on this page: "Once the minister approves a name and it is included in the Place Names Register, it is known as a 'registered' name." (22 words, Place Names window). I did not file it so as to stay within two rows.
- https://www.land.vic.gov.au/place-naming/aboriginal-place-naming/develop-an-aboriginal-naming-proposal — not offered. Its consent sentence (a naming authority "must consult the relevant Traditional Owner group(s) to determine an appropriate name and receive consent") is 35 words, and its clauses have no PLACE stem. The Registered/Dual recording line is a list item.
- https://www.land.vic.gov.au/place-naming (also .../aboriginal-place-naming, .../what-we-do, .../the-naming-rules, .../first-time-here/frequently-asked-questions, .../diversity-and-inclusion-in-naming) — opened to find the S511 page; not offered because the URL is one-row-per-page and S511 carries the stronger point. The Victorian naming-rules documents are .docx files, which the locator does not parse (only PDF, HTML and JSON), so I did not offer them.

## installs:

None.
