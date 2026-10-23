# ScoutCanadaIndigenousNames — round 58, claim C source item (S512, S513)

Seat: KotodamaR58A2.ScoutCanadaIndigenousNames. Accessed 2026-10-23 by plain `curl` GET (no browser, no access control met). I checked both URLs against `corpus/SOURCES.md` with `grep -cF '<host/path>'` and got 0 matches each. Both pages are official Government of Canada (Natural Resources Canada / Geographical Names Board of Canada) pages, and both quotes are body `<p>` text, not a `<title>`, `<h1>` or `<meta>` label.

Design decisions these rows serve: **who may change a name and under what rule** (S512: Indigenous names get priority whenever a feature is named or renamed), and **which language layer a name belongs to and how outsiders mangle it** (S513: settler names that are Indigenous words respelled into English or French).

## (1) Registry rows

| S512 | Geographical Names Board of Canada, 2025 (adopted 21 October 2025; page modified 2026-01-07), "Best Practices for Indigenous Place Naming", Natural Resources Canada, ISBN 978-0-660-79927-8 — https://natural-resources.canada.ca/maps-tools-publications/maps/geographical-names-board-canada/best-practices-indigenous-place-naming (direct, HTTP 200) | docs | A | the Canadian naming board's rule that Indigenous names take priority when features are named or renamed | §3.2 Prioritization of Indigenous Names ¶1: "The GNBC recognizes the need to prioritize the identification and the adoption of Indigenous names when naming or renaming geographical features." | Canada's national naming board tells its member authorities to put Indigenous names first whenever a geographical feature is named or renamed. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |
| S513 | Natural Resources Canada, 2017 (issued 2017-06-09; page modified 2026-07-27), "Indigenous Place Names", Geographical names in Canada — https://natural-resources.canada.ca/maps-tools-publications/maps/geographical-names-canada/indigenous-place-names (direct, HTTP 200) | docs | A | settler respellings of Indigenous words surviving inside official Canadian place names | intro ¶2: "Indigenous heritage is reflected in many place names where European settlers tried to transpose the words they were hearing into either English or French." | Many Canadian place names keep an Indigenous word only as European settlers heard it, respelled into English or French. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

## (2) Gate lines

- S512 — https://natural-resources.canada.ca/maps-tools-publications/maps/geographical-names-board-canada/best-practices-indigenous-place-naming — accessed 2026-10-23 — §3.2 Prioritization of Indigenous Names ¶1: “The GNBC recognizes the need to prioritize the identification and the adoption of Indigenous names when naming or renaming geographical features.” Grounds: Canada's national naming board tells its member authorities to put Indigenous names first whenever a geographical feature is named or renamed. Seat: ScoutCanadaIndigenousNames.
- S513 — https://natural-resources.canada.ca/maps-tools-publications/maps/geographical-names-canada/indigenous-place-names — accessed 2026-10-23 — intro ¶2: “Indigenous heritage is reflected in many place names where European settlers tried to transpose the words they were hearing into either English or French.” Grounds: Many Canadian place names keep an Indigenous word only as European settlers heard it, respelled into English or French. Seat: ScoutCanadaIndigenousNames.

## (3) rowcheck output

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutCanadaIndigenousNames/rows.md`

```
S512 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://natural-resources.canada.ca/maps-tools-publications/maps/geographical-names-board-canada/best-practices-indigenous-place-naming | BOILER: root-clear https://natural-resources.canada.ca/; not a title, h1 or meta label | RELEVANCE: shared=['featu', 'geogr', 'indig', 'name', 'namin', 'renam'] | TOPIC: quote_hits=2 function_words=5 page_hits=63 page_terms=34 need=1/2/3/2
S513 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://natural-resources.canada.ca/maps-tools-publications/maps/geographical-names-canada/indigenous-place-names | BOILER: root-clear https://natural-resources.canada.ca/; not a title, h1 or meta label | RELEVANCE: shared=['engli', 'europ', 'frenc', 'indig', 'name', 'place'] | TOPIC: quote_hits=1 function_words=6 page_hits=35 page_terms=24 need=1/2/3/2
exit 0
```

The run was without `--entry`, so RELEVANCE legs (c) and (d) still have to be checked once the entry cites the rows. Each draft sentence below reuses at least 2 content words of both the quote and the teaches cell.

## (4) Draft sentences

S512:
- Canada's Geographical Names Board asks its naming authorities to prioritize Indigenous names whenever they are naming or renaming geographical features (S512).
- For a worldbuilder this is a naming rule with a direction: before a feature is named or renamed, the authority first looks for an Indigenous name and adopts it (S512).
- A setting's naming board can hold the same rule, so the identification and adoption of older Indigenous names comes ahead of any new coinage for a geographical feature (S512).

S513:
- Many Canadian place names carry Indigenous heritage only in the form European settlers heard the words and transposed them into English or French (S513).
- For a conquest or settlement layer, a settler place name need not be a new coinage: it can be an Indigenous word that European settlers respelled into English or French (S513).
- A worldbuilder can show that layer by giving a town or river an English- or French-looking name whose roots are Indigenous words the settlers were hearing (S513).

The S513 page also lists official restorations, but those are not carried by the S513 quote, so the entry SHOULD NOT cite them to S513 unless another row anchors them. Examples: Yukon changed Mount Higgins to Jùuk'an (2020); Nunavut changed Hall Beach and Cape Dorset to Sanirajak and Kinngait; Saskatchewan replaced a derogatory name with kikiskitotawânawak iskwêwak Lakes (2018); the Northwest Territories approved five names for the Mackenzie River (2015).

## (5) Rejected

- https://iqaluit.ca/visitors/explore-iqaluit/history (City of Iqaluit, HTTP 200). It is the Frobisher Bay to Iqaluit (1987) restoration example, but the page fails the TOPIC page thresholds (needs at least 3 windows and at least 2 field terms). Output of `rowcheck.window_hits(text)` and `len(rowcheck.DISCIPLINE.findall(normalise(text)))` on the tag-stripped page: `iq.html.txt 1 0`. For comparison, the two offered pages gave `bp.html.txt 63 34` and `ipn.html.txt 35 24`.
- Alternate S513 anchor on the same NRCan "Indigenous Place Names" page: "In 2020, Yukon changed the name of Mount Higgins to the traditional Tetlit Gwich'in name of Jùuk'an." (the official-restoration example). It is not offered because the checker failed it. Output of `rowcheck.py --draft rows-alt.md`:
  ```
  S513 LOCATE FAIL BOILER FAIL RELEVANCE PASS TOPIC FAIL | LOCATE: https://natural-resources.canada.ca/maps-tools-publications/maps/geographical-names-canada/indigenous-place-names url-reflects-quote | BOILER: not-located | RELEVANCE: shared=['name', 'tradi'] | TOPIC: quote_hits=1 not-located
  exit 1
  ```
  A page can only give one row, so offering it would mean dropping the S513 row above.
- Guessed NRCan paths, opened and returned HTTP 404 (not sources): `natural-resources.canada.ca/earth-sciences/geography/geographical-names-board-canada/principles-procedures-for-geographical-naming/9238`, `natural-resources.canada.ca/maps-tools-and-publications/maps/geographical-names-canada/principles-procedures-geographical-naming`, `www.nrcan.gc.ca/earth-sciences/geography/geographical-names-board-canada/indigenous-geographical-names/19777` (redirected, then 404), `natural-resources.canada.ca/maps-tools-publications/maps/geographical-names-canada/indigenous-geographical-names`.
- https://geonames.nrcan.gc.ca/ — not opened: `curl: (35) Recv failure: Connection reset by peer`, HTTP 000.
- Seen only as web-search leads and not opened (not counted as sources): the NRCan "Guiding principles for geographical naming" page (its 14 principles are list items, so not quotable under the row rules), "Propose a geographical name", the GNBC 2011 Principles and Procedures PDF on publications.gc.ca, the CGNDB record on geogratis.gc.ca (table cells only), and the Government of Nunavut Iqaluit history PDF.

## Remaining unknowns

- Haida Gwaii (Haida Gwaii Reconciliation Act) was not opened. If L1 wants that example, another seat would have to source it.

installs: none.
