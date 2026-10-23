# ScoutUNGEGNHeritage — claim C source item (S502, S503)

Seat: KotodamaR58A2.ScoutUNGEGNHeritage. Accessed 2026-10-23 UTC by plain curl (desktop User-Agent) and pypdf 5.4.0 text extraction (the locator's own PDF path). Neither URL is in `corpus/SOURCES.md` (`grep -c 'seriesm\|ungegn\|Media_Kit' corpus/SOURCES.md` → 0; `grep -n unstats.un.org` → no lines).

Design angle: S502 covers **which language layer a name belongs to**: geographical names outlive the languages that coined them, so they are a substrate layer. S503 covers **who rules on names and by what rule**: UN conference resolutions treat names as cultural heritage and set criteria for judging that status.

## S502

(1) Registry row

| S502 | United Nations Group of Experts on Geographical Names (UN DESA Statistics Division), 2006, Manual for the national standardization of geographical names (ST/ESA/STAT/SER.M/88), ch. V, The social and cultural values of geographical names — https://unstats.un.org/unsd/publication/seriesm/seriesm_88e.pdf (direct, HTTP 200) | docs | A | geographical names preserving otherwise extinct languages (substrate layer of place names) | p. 121 (PDF p. 132), ch. V §A, Place names: the memory of places: "In many cases, geographical names are the only surviving elements of extinct languages." | Place names often outlive the languages that coined them, so a toponym can be the last surviving trace of an extinct language. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

(2) Gate line

- S502 — https://unstats.un.org/unsd/publication/seriesm/seriesm_88e.pdf — accessed 2026-10-23 — p. 121 (PDF p. 132), ch. V §A: “In many cases, geographical names are the only surviving elements of extinct languages.” Grounds: Place names often outlive the languages that coined them, so a toponym can be the last surviving trace of an extinct language. Seat: ScoutUNGEGNHeritage.

Page context (same paragraph, PDF p. 132; this text is on the page but is not the anchor): "Geographical names, or place names, may be said to represent the oldest living part of human cultural heritage, in the sense that they have been handed down orally from generation to generation for hundreds or several thousands of years. In the continents overseas where Europeans introduced their languages and their names, many aboriginal names nevertheless survive as a testimony to the existence of earlier civilizations." The title page reads "New York, 2006", "Sales No. E.06.XVII.7", "Copyright © United Nations, 2006".

(4) draft sentences:
- In many cases geographical names are the only surviving elements of extinct languages, so a vanished substrate language can live on in a world's place names (S502).
- A toponym can be the last surviving trace of an extinct language: its speakers' place names outlive the language that coined them (S502).
- Even where incoming colonists brought their own languages and names, many earlier aboriginal names survive, so the older language layer outlasts the newer one in the geographical names of a land (S502).

## S503

(1) Registry row

| S503 | United Nations Group of Experts on Geographical Names, 2025, Media Kit 7: Resolutions and decisions of UNGEGN — https://unstats.un.org/unsd/ungegn/pubs/documents/Media_Kit%207_Resolutions_2025_final.pdf (direct, HTTP 200) | docs | A | UN naming-conference resolutions treating geographical names as cultural heritage | p. 2, paragraph on cultural heritage aspects of geographical names: "Resolution X/3 (2012) recommended a list of criteria to establish and evaluate the nature of geographical names as cultural heritage." | In 2012 a UN naming conference adopted criteria by which an authority can judge which geographical names qualify as cultural heritage. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

(2) Gate line

- S503 — https://unstats.un.org/unsd/ungegn/pubs/documents/Media_Kit%207_Resolutions_2025_final.pdf — accessed 2026-10-23 — p. 2: “Resolution X/3 (2012) recommended a list of criteria to establish and evaluate the nature of geographical names as cultural heritage.” Grounds: In 2012 a UN naming conference adopted criteria by which an authority can judge which geographical names qualify as cultural heritage. Seat: ScoutUNGEGNHeritage.

Page context (same paragraph, p. 2): "Resolution VIII/9 (2002) and resolution IX/4 (2007) recognized the significance of geographical names to a nation’s cultural heritage, urged promotion of a greater public understanding of names and identity, and made links to the conventions of UNESCO." Page 1 says the UN Conferences on the Standardization of Geographical Names "were held every five years between 1967 and 2017". The page also lists resolution topics as bullets (national names authorities, exonyms, romanization, commemorative naming, commercialization). These are list items, so none of them can serve as an anchor.

(4) draft sentences:
- UN naming conferences treat geographical names as cultural heritage: Resolution X/3 (2012) recommended a list of criteria to establish and evaluate which names qualify (S503).
- A worldbuilder can borrow this as a heritage list of geographical names judged against stated criteria, as Resolution X/3 recommended (S503).
- Earlier resolutions, VIII/9 (2002) and IX/4 (2007), recognized the significance of geographical names to a nation's cultural heritage, so the 2012 criteria built on a decade of heritage resolutions (S503).

## (3) rowcheck output

Draft rows are in `/fast/scratch/hyaku/kotodama-r58/ScoutUNGEGNHeritage/rows.md`.

Plain draft run: `timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutUNGEGNHeritage/rows.md` (exit 0):

```
S502 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://unstats.un.org/unsd/publication/seriesm/seriesm_88e.pdf | BOILER: root-clear https://unstats.un.org/; not a title, h1 or meta label | RELEVANCE: shared=['extin', 'langu', 'name', 'survi'] | TOPIC: quote_hits=1 function_words=4 page_hits=1443 page_terms=1172 need=1/2/3/2
S503 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://unstats.un.org/unsd/ungegn/pubs/documents/Media_Kit%207_Resolutions_2025_final.pdf | BOILER: root-clear https://unstats.un.org/; not a title, h1 or meta label | RELEVANCE: shared=['2012', 'crite', 'cultu', 'geogr', 'herit', 'name'] | TOPIC: quote_hits=1 function_words=6 page_hits=28 page_terms=22 need=1/2/3/2
```

Entry legs (c)/(d) were also run against a mock entry made from the draft sentences: `--entry /fast/scratch/hyaku/kotodama-r58/ScoutUNGEGNHeritage/mock-entry.md`. Exit 0, and the output for both rows was identical to the run above (all four legs PASS). The mock's first S502 sentence had a trailing "long after its last speakers"; I cut that from the draft above because the quote does not say it. Cutting it still leaves the shared stems that legs (c) and (d) need.

Attack note for the L1: the first draft of these rows had a locator containing a double-quoted heading (`ch. V §A "Place names: the memory of places"`). rowcheck takes the FIRST double-quoted span in the anchor cell as QUOTE. For S502 that made the row fail ("quote under 8 words"). For S503, an earlier quoted paragraph opener in the locator **passed** all four legs as if it were the anchor. Do not use double quotes in locators.

## rejected:
- https://unstats.un.org/unsd/publication/seriesm/seriesm_88e.pdf, other passages. Same page as S502, and one URL makes one row. Two passages would also fail: the generic-term sentence on p. 39 ("The generic term, often a separate word, is an integral part of most geographical names...") and the conservative name-change rule on p. 34. pypdf splits words in both ("ge ographical", "in cluded", "rega rd"), so LOCATE would fail. The name-change and derogatory-name policy sentences on p. 33 also have no NAMING-PLACE window ("rules covering name changes, treatment of derogatory names, names commemorating living persons" has no place word within 3 words).
- https://unstats.un.org/unsd/ungegn/pubs/documents/Media_Kit%202_GN_Values_2025_final.pdf (HTTP 200). On topic, but every substantive sentence is in a bullet list (list items are barred). It also repeats the Manual's heritage text ("In many cases, geographical names are the only surviving elements of extinct languages." appears in a bullet), so it adds no new evidence.
- https://unstats.un.org/unsd/ungegn/pubs/documents/UNCSGN%20Resolutions_eng.pdf. This was a guessed URL for the resolutions compendium; it returned HTTP 404.
- https://unstats.un.org/UNSD/ungegn/pubs/ and https://unstats.un.org/unsd/ungegn/ (HTTP 200). These are navigation and index pages, used only to find the media-kit PDFs, so they cannot be anchors.

## remaining unknowns
- The full official text of resolutions VIII/9, IX/4 and X/3 (the compendium at unstats.un.org/unsd/ungegn/resolutions) was not opened; I stopped at the 3-source cap. S503 cites UNGEGN's own 2025 summary of those resolutions, not the resolution texts.

installs: none.
