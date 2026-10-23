# ScoutStreetNaming — round 58, claim C source item (street naming / odonymy)

Seat: KotodamaR58A2.ScoutStreetNaming. S-ids: S540, S541. Two rows offered; both pass all four rowcheck legs, both bare and against a mock entry made of the draft sentences below.

Note on scope: the brief said to open 1 to 3 sources. I opened 5 (one more returned HTTP 403) because the first municipal policy, Toronto's, fails TOPIC. The extra sources are listed under `rejected:`.

## S540 — London Borough of Harrow, Street Naming and Numbering Policy (May 2025)

(1) Registry row

| S540 | London Borough of Harrow (Digital Services), May 2025, *Street Naming and Numbering (SNN) Policy* — https://www.harrow.gov.uk/downloads/file/32247/Street_naming_and_numbering_document.pdf (direct, HTTP 200) | docs | A | a municipal street-naming authority's rules: no duplicate names, commemorative conditions, renaming consent | Appendix B - Street and Building name suffixes, p. 18: "New street or building names should not duplicate any similar name already in use in a postcode area." | Under Harrow's policy a proposed street name should not repeat a similar name already used within the same postcode area. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

(2) Gate line

- S540 — https://www.harrow.gov.uk/downloads/file/32247/Street_naming_and_numbering_document.pdf — accessed 2026-10-23 — Appendix B - Street and Building name suffixes, p. 18: “New street or building names should not duplicate any similar name already in use in a postcode area.” Grounds: Under Harrow's policy a proposed street name should not repeat a similar name already used within the same postcode area. Seat: ScoutStreetNaming.

Other text on the same page that the draft sentences use. The first two are bullet items and the third is a numbered rule, so none was offered as the anchor:
- §5.9 bullet: "New street names, wherever possible, should be relevant to the area in question and be based on historical events, natural features or landmarks."
- §9.5 bullets: "The person must be deceased." / "The name will not be considered if the person has been deceased for less than 40 years."
- §9.3: "At least a two thirds majority of residents and property owner consent will be required before any renaming proposals are considered."
- §5.9 bullet: "Names with different suffixes are not acceptable i.e. Dylan Court, Dylan Drive etc." (in the reviewer's words: changing only the suffix does not make a name new).

(4) draft sentences:
- A street-naming authority such as the London Borough of Harrow says a new street name should not duplicate a similar name already in use in the same postcode area (S540).
- Harrow also asks that new street names be relevant to the area, based on historical events, natural features or landmarks, and a street named after a person must honour someone deceased for at least 40 years (S540).
- Harrow considers a proposal to change an existing street name only after at least a two-thirds majority of residents and property owners consent (S540).

## S541 — Azaryahu 2011, "The Critical Turn and Beyond: The Case of Commemorative Street Naming" (ACME, CC BY-NC-ND)

(1) Registry row

| S541 | Azaryahu, Maoz, 2011, "The Critical Turn and Beyond: The Case of Commemorative Street Naming", *ACME: An International E-Journal for Critical Geographies* 10 (1), 28-33 (CC BY-NC-ND) — https://acme-journal.org/index.php/acme/article/download/883/739/2716 (direct, HTTP 200) | paper | A | scholarship on commemorative street naming: renaming after regime change, decolonisation of street names | p. 29: "The retributive and politicized nature of street renaming has been particularly evident in South African cities." | After a change of regime, renaming streets can serve as political retribution against the old order, as South African cities show. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

(2) Gate line

- S541 — https://acme-journal.org/index.php/acme/article/download/883/739/2716 — accessed 2026-10-23 — p. 29: “The retributive and politicized nature of street renaming has been particularly evident in South African cities.” Grounds: After a change of regime, renaming streets can serve as political retribution against the old order, as South African cities show. Seat: ScoutStreetNaming.

Context on the same page, used by the draft sentences: the preceding sentence "Of much interest in this respect is the function of renaming as a measure of symbolic retribution" sits in the paragraph on large-scale "toponymic cleansing" after a regime change. The following sentence reads: "Violent protests have taken place over the removal of road names from the country's colonial and apartheid past and the establishment of new names that glorify the ruling African National Congress and supposedly slight the party's political rivals (Wines, 2007)." On p. 31 the article sets out three decolonisation strategies: "erase all 'colonial' street names", "leave colonial commemorations in their place", and "a selective de-commemoration of the colonial past".

(4) draft sentences:
- Street renaming after a regime change can be politicized retribution against the old order: in South African cities violent protests met the removal of road names from the colonial and apartheid past (S541).
- In those South African cities the new names glorify the ruling African National Congress and supposedly slight its political rivals, so street renaming both removes the old names and establishes new ones (S541).
- After independence a former colony may, Azaryahu surmises, erase all colonial street names, leave them in place, or de-commemorate the colonial past selectively; these are three strategies of street renaming (S541).

## (3) rowcheck output

Run: `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutStreetNaming/rows.md` (exit 0):

```
S540 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.harrow.gov.uk/downloads/file/32247/Street_naming_and_numbering_document.pdf | BOILER: root-clear https://www.harrow.gov.uk/; not a title, h1 or meta label | RELEVANCE: shared=['alrea', 'area', 'name', 'postc', 'simil', 'stree'] | TOPIC: quote_hits=1 function_words=3 page_hits=80 page_terms=10 need=1/2/3/2
S541 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://acme-journal.org/index.php/acme/article/download/883/739/2716 | BOILER: root-clear https://acme-journal.org/; not a title, h1 or meta label | RELEVANCE: shared=['afric', 'citie', 'polit', 'renam', 'retri', 'south'] | TOPIC: quote_hits=1 function_words=5 page_hits=75 page_terms=29 need=1/2/3/2
```

The same command with `--entry /fast/scratch/hyaku/kotodama-r58/ScoutStreetNaming/mock-entry.md` (the six draft sentences above) printed the identical four PASS legs per row and exited 0. Per sentence, each draft sentence shares at least 2 stems with both the quote and the teaches cell; the smallest overlaps are S540 sentence 3, which shares quote stems name and street, and S541 sentence 3, which shares quote stems renaming and street.

None of the URLs is in corpus/SOURCES.md. `grep -cF` returned 0 for each of `harrow.gov.uk/downloads/file/32247`, `acme-journal.org/index.php/acme/article/download/883`, `thurrock.gov.uk` and `toronto.ca/legdocs/mmis/2022/ex/bgrd/backgroundfile-228155`.

## (5) rejected:

- https://www.toronto.ca/legdocs/mmis/2022/ex/bgrd/backgroundfile-228155.pdf (City of Toronto Street Naming Policy, 2022, HTTP 200). Rejected because it fails TOPIC: the page has no field terms (toponym, place name, gazetteer and so on). Output from the seat's probe, which uses rowcheck's `page_text`, `window_hits` and `DISCIPLINE`: `https://www.toronto.ca/legdocs/mmis/2022/ex/bgrd/backgroundfile-228155.pdf words 2406 hits 69 terms 0 []`. Its rules are a good design lead, but no row can carry them: a 10-year bar on renaming a street named or reviewed recently, a 2-year wait after death or event on the official street-naming page, Indigenous consultation, and duplicates defined as identical names ignoring the suffix.
- https://www.toronto.ca/city-government/planning-development/street-naming/ (City of Toronto, Street Naming page). Rejected for the same TOPIC failure: `https://www.toronto.ca/city-government/planning-development/street-naming/ words 2690 hits 69 terms 0 []`.
- https://barnet.moderngov.co.uk/documents/s55370/Street%20Naming%20and%20Numbering%20Policy.pdf (London Borough of Barnet). Not opened: the server refuses an ordinary GET. Probe: `ERR HTTP Error 403: Forbidden`; curl on the site root: `403 root barnet`. I did not try to get past the refusal (QUALITY criterion 10).
- https://www.thurrock.gov.uk/sites/default/files/assets/documents/naming-numbering-streets-highway-assets-202105-v01.pdf (Thurrock Council, May 2021, HTTP 200). Not offered only because of the 2-row cap; Harrow is a London borough and also covers the duplicate, commemoration and consent rules. It is a valid spare if the L1 wants a third source. Its draft row was B.2: "Proposed street names should, where possible have some connection to the development site or in keeping with the area, whether historical or geographical." Rowcheck on that draft (with the id S540 used only for the test): `S540 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | ... TOPIC: quote_hits=1 function_words=5 page_hits=60 page_terms=3 need=1/2/3/2`. Its prose sentence "The presumption will be therefore that a street or premises will not be named after a living person unless there are exceptional circumstances." fails the window rule: "named" is 6 words from "street".
- Search leads only, not opened: https://doi.org/10.1068/d140311 (Azaryahu 1996, *Environment and Planning D*; restricted access) and https://www.jbe-platform.com/content/journals/10.1075/ll.21016.buc (Buchstaller et al. 2022; access status not checked).

## Scratch

The draft rows, the spare row, the mock entry, the probe script and the cached page texts are under /fast/scratch/hyaku/kotodama-r58/ScoutStreetNaming/. No process was left running.

installs: none.
