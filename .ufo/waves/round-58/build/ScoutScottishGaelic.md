# ScoutScottishGaelic — round 58, claim C source item (S520, S521)

Seat: KotodamaR58A2.ScoutScottishGaelic. Accessed 2026-10-23. Both rows pass LOCATE, BOILER, RELEVANCE and TOPIC (rowcheck output below). Neither URL is in corpus/SOURCES.md (`grep -c -F 'ainmean-aite.scot' corpus/SOURCES.md` → 0).

Host note: the brief named `gaelicplacenames.scot`; that host does not resolve (see rejected). Ainmean-Àite na h-Alba (AÀA) publishes at `www.ainmean-aite.scot`, which is linked as its own site (database, policy, research). Both rows come from that official site.

## Rows

| S520 | Ainmean-Àite na h-Alba (AÀA), 2020, Gaelic Place-Names Policy (last updated March 2020) — https://www.ainmean-aite.scot/wp-content/uploads/2020/05/A%C3%80A-Gaelic-Place-names-Policy_FINAL_EN.pdf (direct, HTTP 200) | docs | A | how Scotland's national Gaelic place-name partnership defines and standardises Gaelic place-names, including names of Norse origin | §1.6 What is a Gaelic Place-name?, p. 3: "A Gaelic place-name for the purposes of this document is a place-name used by Gaelic speakers when speaking Gaelic, whatever its linguistic origin" | Scotland's Gaelic naming partnership counts any name that Gaelic speakers use in Gaelic as a Gaelic place-name, even one inherited from another language. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |
| S521 | Ainmean-Àite na h-Alba (AÀA), About Ainmean-Àite na h-Alba — https://www.ainmean-aite.scot/about-ainmean-aite-na-h-alba/ (direct, HTTP 200) | docs | A | the origin and remit of Scotland's national advisory partnership for Gaelic place-names, as stated by the partnership | section The origins of Ainmean-Àite na h-Alba, first sentence: "In 2000 the Ordnance Survey (OS) recognised that some Gaelic place-names on their maps were incorrect" | Even a national mapping agency can print wrong minority-language place-names, as the Ordnance Survey admitted for Gaelic names on its Scottish maps. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

Tier A: both are the naming partnership's own statements about its own policy and history, used only within that scope. The S521 quote is a clause. The full sentence continues ", and in some instances, inconsistent across their scales of mapping." and runs to 26 words, so it was cut to stay within 25.

## Gate lines

- S520 — https://www.ainmean-aite.scot/wp-content/uploads/2020/05/A%C3%80A-Gaelic-Place-names-Policy_FINAL_EN.pdf — accessed 2026-10-23 — §1.6 What is a Gaelic Place-name?, p. 3: “A Gaelic place-name for the purposes of this document is a place-name used by Gaelic speakers when speaking Gaelic, whatever its linguistic origin”. Grounds: Scotland's Gaelic naming partnership counts any name that Gaelic speakers use in Gaelic as a Gaelic place-name, even one inherited from another language. Seat: KotodamaR58A2.ScoutScottishGaelic.
- S521 — https://www.ainmean-aite.scot/about-ainmean-aite-na-h-alba/ — accessed 2026-10-23 — section The origins of Ainmean-Àite na h-Alba, first sentence: “In 2000 the Ordnance Survey (OS) recognised that some Gaelic place-names on their maps were incorrect”. Grounds: Even a national mapping agency can print wrong minority-language place-names, as the Ordnance Survey admitted for Gaelic names on its Scottish maps. Seat: KotodamaR58A2.ScoutScottishGaelic.

## rowcheck output

Command: `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutScottishGaelic/rows.md` (draft file holds exactly the two rows above).

```
S520 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.ainmean-aite.scot/wp-content/uploads/2020/05/A%C3%80A-Gaelic-Place-names-Policy_FINAL_EN.pdf | BOILER: root-clear https://www.ainmean-aite.scot/; not a title, h1 or meta label | RELEVANCE: shared=['gaeli', 'name', 'place', 'speak'] | TOPIC: quote_hits=2 function_words=8 page_hits=74 page_terms=63 need=1/2/3/2
S521 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.ainmean-aite.scot/about-ainmean-aite-na-h-alba/ | BOILER: root-clear https://www.ainmean-aite.scot/; not a title, h1 or meta label | RELEVANCE: shared=['gaeli', 'maps', 'name', 'ordna', 'place', 'surve'] | TOPIC: quote_hits=1 function_words=6 page_hits=27 page_terms=27 need=1/2/3/2
exit 0
```

An earlier run failed S521 on all four legs (`LOCATE ... url-reflects-quote`) because the locator wrapped the section title in double quotes, so the checker read the title as the quote. The section title is now unquoted and the quote and teaches cell are unchanged; the run above is the passing re-run. Run without `--entry` (the entry does not exist yet), so RELEVANCE legs (c) and (d) are still unchecked.

## draft sentences

S520. Each sentence below reuses words from the S520 quote ("Gaelic", "place-name", "speakers", "origin") and from its teaches cell ("Gaelic", "name", "speakers"). Every fact is on the opened PDF: §1.6, §2, §3.4, §6.2 glossary, §6.3.1.1, and footnotes 1, 2, 24 and 43.
- In Scotland the national Gaelic naming partnership treats a Gaelic place-name as any name that Gaelic speakers use when speaking Gaelic, whatever its linguistic origin, so an inherited name from an older language layer still counts (S520).
- The policy keeps the Norse layer visible inside Gaelic names: in names of Norse origin, Old Norse dalr 'valley' is spelled -dal and Norse -ey 'island' is spelled -aigh or -eigh, so Armadale is given in Gaelic as Armadal, from Old Norse Ormadalr 'snake valley' (S520).
- Its glossary calls an element a building-block of a place-name, a generic element the part naming the type of place and a specific element the part that qualifies it. Its Gaelic examples are built on ceann and baile, such as Kincraig ~ Ceann na Creige and Tain ~ Baile Dhubhthaich (S520).
- The partnership gives a Gaelic form to a name of Gaelic origin, a name with an established Gaelic form, a non-Gaelic name among Gaelic-derived names, or a requested name. Its research ranks the local pronunciation of speakers with long contact with local traditions above that of recent incomers (S520).

S521. Each sentence below reuses words from the S521 quote ("Ordnance Survey", "Gaelic", "place-names", "maps", "recognised") and from its teaches cell ("Ordnance Survey", "Gaelic", "names", "maps"). Every fact is on the opened About page.
- Mapmakers can get names wrong too. In 2000 the Ordnance Survey recognised that some Gaelic place-names on its maps were incorrect, because most names of natural features had been collected in the 19th century (S521).
- The correction became an institution: experts advised the Ordnance Survey to set up a Gaelic Names Liaison Committee. In 2006 that committee became Ainmean-Àite na h-Alba, the national advisory partnership that recommends forms of Gaelic place-names for signage and maps (S521).
- Signs drove the demand. A 2003 Scottish Government policy of bilingual road signs in the West Highlands brought requests for Gaelic place-name research, and so did council Gaelic Language Plans covering street, building and path signs (S521).

The policy PDF shows baile, ceann and inbhir only in its example name pairs. It names no achadh-based example, and no opened page explains these elements in prose. The policy points to Taylor 2005, an Ordnance Survey guide with a glossary of Gaelic place-name elements (https://getoutside.ordnancesurvey.co.uk/guides/the-gaelic-origins-of-place-names-in-britain/). I did not open it, so it is only a lead for another seat. Do not cite S520 for a prose account of what those elements mean.

## rejected

- https://www.gaelicplacenames.scot/ (also `/about-gaelic-place-names/` and `/resources/`) and https://gaelicplacenames.scot/: the host does not resolve. curl output: `curl: (6) Could not resolve host: www.gaelicplacenames.scot` / `000 https://www.gaelicplacenames.scot/`; `curl: (6) Could not resolve host: gaelicplacenames.scot` / `000 https://gaelicplacenames.scot/ 0`.
- https://www.ainmean-aite.scot/placename-elements/ and https://www.ainmean-aite.scot/about-us/: guessed paths, both returned HTTP 404 (curl: `404 https://www.ainmean-aite.scot/placename-elements/ 67370`, `404 https://www.ainmean-aite.scot/about-us/ 67370`).
- https://www.ainmean-aite.scot/ (home page): this is the site root, which the BOILER leg compares quotes against. It holds navigation and news, not teaching body text.
- https://www.ainmean-aite.scot/gaelic-place-name-policy/: a short HTML summary that only points to the policy PDF. The PDF, the primary text, is offered as S520 instead.
- https://www.ainmean-aite.scot/research/: the only language-layer sentence ("focuses on Gaelic, though names from Scots, English, Old Norse and British are also included") has no place word near "names". The woodland-dataset sentence is off the assignment's design decisions.
- https://www.ainmean-aite.scot/placename-lists/ and https://www.ainmean-aite.scot/policies/: a list of PDF downloads and the organisation's workplace policies. Neither has teachable body text on place names.
- https://www.ainmean-aite.scot/wp-content/uploads/2024/07/AAA-Gaelic-Place-name-Policy-Appendices_Recommended-Terms_Jul-2024.pdf: a glossary for translating English street terms into Gaelic. Its content is mostly table cells, and it adds less to the entry than the policy itself; I kept to two rows.

## installs:

None. The PDF text was extracted with the same `uv run --with pypdf==5.4.0` call that reopen-quote.py uses; nothing was installed persistently.
