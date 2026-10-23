# ScoutSlavicGermanContact — claim C source item (S528, S529)

Seat: KotodamaR58A2.ScoutSlavicGermanContact (scout, leaf). Access date 2026-10-23. All reading by plain GET (curl, and the frozen locator's urllib fetch); no browser, no access control met on either offered source. Neither offered URL appears in corpus/SOURCES.md (`grep -cF -e 'journals.uni-lj.si' -e 'stagn' corpus/SOURCES.md` → `0`).

Design decisions served: who may set and print the official form of a minority-language name and how two names share a map (S528); which language layer a name belongs to and what contact does to it — parallel names, name changes, translation, doublets, hybrids such as German personal name + Slavic suffix -ici > -itz (S529).

## (1) Registry rows

| S528 | Ständiger Ausschuss für geographische Namen (StAGN), 2016, Toponymic Guidelines for map and other editors for international use: Federal Republic of Germany, sixth revised edition, bilingual German and English (Frankfurt am Main: StAGN office at the Bundesamt für Kartographie und Geodäsie) — https://stagn.bkg.bund.de/fileadmin/user_upload/02_StAGN/04_StAGN_Was_wir_ver%C3%B6ffentlichen/161018_TopR06.pdf (direct, HTTP 200, application/pdf, 3,388,709 bytes, plain GET, accessed 2026-10-23) | docs | A | the official German rule for showing Sorbian geographical names beside the German names on maps of the Sorbian settlement area, with its slash, parenthesis and diacritic conventions | §1.2.1.4 Sorbian languages, English column, pp. 20–21: "Sorbian geographical names have to be used alongside the German names" | Germany's official toponymic guidelines require Sorbian geographical names to stand next to the German names on maps, especially maps made for schools. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |
| S529 | Bily, Inge, 2015, "Deutsch-slawischer Siedlungs- und Sprachkontakt im Gebiet zwischen Saale und Neiße – vorgestellt an ausgewählten Ortsnamen (Siedlungsnamen)" [German-Slavic settlement and language contact in the region between the rivers Saale and Neisse – presented on the basis of selected place names], Linguistica 55(1): 131–147, doi 10.4312/linguistica.55.1.131-147, CC BY-SA — https://journals.uni-lj.si/linguistica/article/download/6302/6030 (direct, HTTP 200, application/pdf, 809,712 bytes, 17 pages, plain GET, accessed 2026-10-23; journal record https://journals.uni-lj.si/linguistica/article/view/6302 HTTP 200 supplied volume, pages and DOI) | paper | A | Old Sorbian settlement names between Saale and Neisse as a record of German-Slavic contact: parallel names, renaming, translation, assimilation to German words, name doublets and hybrid names | p. 146, English abstract: "the processes of historical settlement are reflected in the historical documentation of place names" | Bily treats the recorded historical forms of place names as evidence for how Slavic and German settlement unfolded between Saale and Neisse. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

Notes for the L1:
- S528 quote is the main clause of the English sentence "In cartographic products designed in particular for educational purposes in schools, Sorbian geographical names have to be used alongside the German names." The PDF is two-column (German left, English right) and a page break plus the German column fall between "educational" and "purposes", so only the clause is locatable; the clause is complete. Same page, same section: names "usually written next to each other and separated by a forward slash, or below each other", Sorbian name "in parentheses and/or in a smaller font" in particular cases, example "Weißwasser/Běła Woda", "The Sorbian names are represented with all diacritical marks of the Upper and Lower Sorbian alphabets". Collision risk: another UNGEGN/BGN seat could also pick a national toponymic-guidelines PDF; this one is Germany's (StAGN), host stagn.bkg.bund.de.
- S529 quote is the "since" clause of the abstract's third sentence (full sentence is 39 words, over the 25-word cap). The abstract (p. 146) goes on to list the nine contact features (list items, so not quotable): "Parallel name giving with the result of temporary parallel names for the same place", "Name changes in the historical documentation", "Translation of place names", "Secondary assimilation of an Old Sorbian place name to an element of the superstrate language (German)", "German-Slavic place name doublets", "German-Slavic and Slavic-German hybrid names". The German body §9.2 gives the -itz case: "Strukturtyp: deutscher Personenname + slawisches ortsnamenbildendes Suffix -ici bzw. -ovici (= Typ Arnoltici) / Beispiel: ON Arntitz, w. Lommatzsch: 1296 Arnolticz, PN Arnolt als Ableitungsbasis des Ortsnamens". Tier A: peer-reviewed university journal (Ljubljana), author is a Leipzig onomast; L1 may set B by lane convention, both pass TIER.
- The S529 journal record page carries the abstract in `<meta name="DC.Description">`, so keep the PDF as the first (locating) URL; a quote located on the record page would fail BOILER.

## (2) Gate lines

- S528 — https://stagn.bkg.bund.de/fileadmin/user_upload/02_StAGN/04_StAGN_Was_wir_ver%C3%B6ffentlichen/161018_TopR06.pdf — accessed 2026-10-23 — §1.2.1.4 Sorbian languages, English column, pp. 20–21: “Sorbian geographical names have to be used alongside the German names”. Grounds: Germany's official toponymic guidelines require Sorbian geographical names to stand next to the German names on maps, especially maps made for schools. Seat: ScoutSlavicGermanContact.
- S529 — https://journals.uni-lj.si/linguistica/article/download/6302/6030 — accessed 2026-10-23 — p. 146, English abstract: “the processes of historical settlement are reflected in the historical documentation of place names”. Grounds: Bily treats the recorded historical forms of place names as evidence for how Slavic and German settlement unfolded between Saale and Neisse. Seat: ScoutSlavicGermanContact.

## (3) rowcheck output

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutSlavicGermanContact/rows.md` (exit 0):

```
S528 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://stagn.bkg.bund.de/fileadmin/user_upload/02_StAGN/04_StAGN_Was_wir_ver%C3%B6ffentlichen/161018_TopR06.pdf | BOILER: root-clear https://stagn.bkg.bund.de/; not a title, h1 or meta label | RELEVANCE: shared=['geogr', 'germa', 'name', 'sorbi'] | TOPIC: quote_hits=1 function_words=3 page_hits=220 page_terms=113 need=1/2/3/2
S529 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://journals.uni-lj.si/linguistica/article/download/6302/6030 | BOILER: root-clear https://journals.uni-lj.si/; not a title, h1 or meta label | RELEVANCE: shared=['histo', 'name', 'place', 'settl'] | TOPIC: quote_hits=1 function_words=4 page_hits=24 page_terms=88 need=1/2/3/2
exit=0
```

Same command with `--entry /fast/scratch/hyaku/kotodama-r58/ScoutSlavicGermanContact/draft-entry.md` (the six draft sentences below), exit 0, RELEVANCE (c) and (d) included:

```
S528 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | RELEVANCE: shared=['geogr', 'germa', 'name', 'sorbi']
S529 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | RELEVANCE: shared=['histo', 'name', 'place', 'settl']
exit=0
```

Each sentence on its own shares at least 2 stems with both the quote and the teaches cell. The weakest are S529 sentences 2 and 3, which share only `name` and `place` with the quote.

## (4) draft sentences

S528:
- Who sets the official form is a design decision too: Germany's toponymic guidelines say that on maps, in particular those made for schools, Sorbian geographical names have to be used alongside the German names (S528).
- The same guidelines fix the layout: the German and Sorbian names stand next to each other split by a slash, as in Weißwasser/Běła Woda, or the Sorbian name goes in parentheses or a smaller font (S528).
- In those guidelines the Sorbian names keep every diacritic of the Upper or Lower Sorbian alphabet, so the official maps show the minority spelling beside the German one (S528).

S529:
- Language contact leaves a readable layer: between Saale and Neisse, the processes of historical settlement are reflected in the recorded forms of place names, which Bily reads as evidence of Slavic and German settlement (S529).
- Bily lists what German-Slavic contact did to place names there: parallel names for the same place, name changes, translation, German-Slavic place name doublets and hybrid names (S529).
- Hybrids run both ways: a German personal name could take the Slavic place-name suffix -ici, so the place recorded in 1296 as Arnolticz, from the personal name Arnolt, is today's Arntitz (S529).

## (5) rejected

- https://www.ceeol.com/search/article-detail?id=752104 — Zschieschang 2019, "Place names among three languages: the Sorbian, German and Polish toponymy of eastern Lusatia", Acta Onomastica 60(1). The topic is the best fit (Sorbian names Germanized, German names Sorabized, Polish names after 1945), but this is an aggregator abstract page whose served text drops spaces at line joins. Python text extraction of the fetched HTML printed `Originally,it was an Old Sorbian settlement area, but after the conquest by the Ottonian rulersin the High Medieval Era ... Sorbian name…` and the abstract has `nameswere Germanized`, so no clean quote. The full text is not reachable by plain GET: `https://actaonomastica.ujc.cas.cz/` gave `curl: (6) Could not resolve host: actaonomastica.ujc.cas.cz`, and `https://asjournals.lib.cas.cz/actaonomastica/` and its search URLs each returned `200 text/html; charset=utf-8 3530` (a JavaScript shell with no article text).
- https://onomastica.ijppan.pl/index.php/ONOM/article/view/406 (and PDF galley `/download/406/521`, HTTP 200 application/pdf 618743) — Szczepańska 2022, the Lower Sorbian name portal. The body is German. Its English abstract talks about "proper names" and "Sorbian and German variants of a proper name" with no place word next to a naming word, so no quote holds a NAMING-PLACE window. The English part of the PDF is only the abstract and keywords (`grep` hits: `Keywords: Lower Sorbian, German, bilingualism, toponyms, anthroponyms`).
- https://apples.journal.fi/article/view/97953 (via doi 10.17011/apples/urn.201909124143) — Bautzen linguistic-landscape paper (bilingual place-name signs). A plain GET served a bot-check page, `<title>Making sure you&#39;re not a bot!</title>` with an `anubis_challenge` script. I did not go past it, so the source is unopened.
- https://reference-global.com/article/10.2478/lccc-2022-0002 — Bleakly 2022, Upper Sorbian street names in Bautzen. Page screen using rowcheck's own `window_hits` and `DISCIPLINE`: `words 1059 page_hits 2 terms 0`, which would fail the TOPIC page test (needs 3 and 2).
- https://www.namenkundliche-informationen.de/ni/article/view/388 — Müller 2006, Polabian plant words in Brandenburg settlement names (Buckow/beech, Preußnitz/cranberry, Löcknitz/water-lily). The English abstract is also the page's own label, `<meta name="DC.Description" xml:lang="en" content="The article deals with the explanation of toponyms in the territory of Brandenburg, ...`, so a quote from it fails BOILER. The PDF galley (`/download/388/377`, HTTP 200 application/pdf 3219921) has no text layer; screen gave `words 12 page_hits 0 terms 0`.
- http://onomastics.ru/en/content/2015-%E2%84%961-18-0 and http://onomastics.ru/content/2015-%E2%84%962-19-4 (Holzer 2015, Austrian Slavic-German hybrid names; the 2015 East German hybrid-names article) — `500 text/html; charset=utf-8` on both.
- https://journals.rcsi.science/2587-6953/article/view/302426 — Belyaev 2021, "German-Slavic toponymic contacts in East Germany". I probed it once (`200 text/html; charset=utf-8 64669`) and did not read it further. It is an aggregator mirror of a Russian-language article with only an English abstract, and the two offered rows already cover the ground within the 2-row cap.

Scratch (my own, under /fast/scratch/hyaku/kotodama-r58/ScoutSlavicGermanContact/): rows.md, draft-entry.md, screen.py (it imports rowcheck.py read-only and prints page window and term counts), plus fetched copies. No process is left running.

installs: none.
