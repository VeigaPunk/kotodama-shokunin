# ScoutDecommunization — claim C rows S538, S539 (Ukraine decommunization renaming)

Seat: ScoutDecommunization. Accessed 2026-10-23. Two sources opened by plain GET (curl, then the round's `rowcheck.py` urllib fetch); both PDFs, both HTTP 200, `application/pdf`. Neither URL nor host path is in `corpus/SOURCES.md` (`grep -cF` for `E_Conf.105_82_CRP.82_5_Report_Ukraine`, `unstats.un.org/UNSD/geoinfo/UNGEGN/docs/11th`, `karolinum.cz`, `Geogr_53_2_0119`, `23361980.2018.13`, `Gnatiuk`: all 0).

Design decisions served: who may change a place name and under what rule (state law fixes which names must go; local bodies choose replacements), and which language/history layer a name belongs to (renaming can restore an older layer, including minority and indigenous names).

## 1. Registry rows

| S538 | State Service of Ukraine for Geodesy, Cartography and Cadastre (submitted by Ukraine), 2017, "Report of Ukraine: Standardization of the geographical names in Ukraine from 2012 till 2017", 11th UN Conference on the Standardization of Geographical Names, E/CONF.105/82/CRP.82 — https://unstats.un.org/UNSD/geoinfo/UNGEGN/docs/11th-uncsgn-docs/E_Conf.105_82_CRP.82_5_Report_Ukraine_11_ENG.pdf (direct, HTTP 200) | docs | A | official national report on Ukraine's 2015-2016 decommunization renaming of settlements and the restoration of historical names | PDF p. 2, section Status of Legislative and Regulatory Base in the Sphere of Geographical Names: "As a result of the renaming of settlements, more than 300 historical names have been restored" | Ukraine's decommunization renaming of settlements did not only coin new names but restored over three hundred historical ones. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |
| S539 | Gnatiuk, Oleksiy, 2018, "The renaming of streets in post-revolutionary Ukraine: regional strategies to construct a new national identity", AUC Geographica 53(2): 119-136, DOI 10.14712/23361980.2018.13, CC BY 4.0 — https://karolinum.cz/data/clanek/6421/Geogr_53_2_0119.pdf (direct, HTTP 200) | paper | A | peer-reviewed open-access study of who chose replacement street and place names under Ukraine's decommunization law | p. 120, §1 Introduction: "However, the official legislation provides no strict instructions about new place-names which should appear instead." | Ukrainian decommunization legislation set no strict rules on which new place names should replace the removed ones. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

Notes for the L1:
- S538's locator deliberately carries the section title WITHOUT double quotes: with quotes, `row_target` takes the title as QUOTE (first run failed RELEVANCE on exactly that; see §3).
- S538's quote is the main clause of a longer sentence; the sentence continues ", of which about 70 belong to the cultural heritage of the indigenous population and national minorities of Ukraine - Crimean Tatars, Bulgarians, Greeks, Jews, etc." (kept out of the quote to stay within 25 words; draft sentence 2 uses it as page text).
- S539's PDF is ~10 MB (under the locator's 120 MiB cap); pypdf extraction located it.

## 2. Gate lines

- S538 — https://unstats.un.org/UNSD/geoinfo/UNGEGN/docs/11th-uncsgn-docs/E_Conf.105_82_CRP.82_5_Report_Ukraine_11_ENG.pdf — accessed 2026-10-23 — PDF p. 2, section Status of Legislative and Regulatory Base in the Sphere of Geographical Names: “As a result of the renaming of settlements, more than 300 historical names have been restored”. Grounds: Ukraine's decommunization renaming of settlements did not only coin new names but restored over three hundred historical ones. Seat: ScoutDecommunization.
- S539 — https://karolinum.cz/data/clanek/6421/Geogr_53_2_0119.pdf — accessed 2026-10-23 — p. 120, §1 Introduction: “However, the official legislation provides no strict instructions about new place-names which should appear instead.” Grounds: Ukrainian decommunization legislation set no strict rules on which new place names should replace the removed ones. Seat: ScoutDecommunization.

## 3. rowcheck output

Command: `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutDecommunization/rows.md` (exit 0). The kind cell of S538 was changed from `record` to `docs` after this run; rowcheck reads no kind cell.

```
S538 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://unstats.un.org/UNSD/geoinfo/UNGEGN/docs/11th-uncsgn-docs/E_Conf.105_82_CRP.82_5_Report_Ukraine_11_ENG.pdf | BOILER: root-clear https://unstats.un.org/; not a title, h1 or meta label | RELEVANCE: shared=['histo', 'name', 'renam', 'resto', 'settl'] | TOPIC: quote_hits=1 function_words=5 page_hits=64 page_terms=49 need=1/2/3/2
S539 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://karolinum.cz/data/clanek/6421/Geogr_53_2_0119.pdf | BOILER: root-clear https://karolinum.cz/; not a title, h1 or meta label | RELEVANCE: shared=['legis', 'name', 'place', 'stric'] | TOPIC: quote_hits=1 function_words=2 page_hits=263 page_terms=155 need=1/2/3/2
EXIT 0
```

On the first run, before the locator fix, S538 printed `RELEVANCE FAIL ... quote-teaches shared=['name']` because the locator's quoted section title was read as the quote.

## 4. Draft sentences

draft sentences:

S538
- When Ukraine carried out the decommunization renaming of its settlements in 2015-2016, more than 300 historical names were restored rather than newly coined (S538).
- Ukraine's report to the UN conference on geographical names counts about 70 of those restored historical names as heritage of the indigenous population and national minorities, such as Crimean Tatars, Bulgarians, Greeks and Jews (S538).
- The same renaming of settlements under the 2015 law reached more than 900 settlements and administrative-territorial units, among them the regional centres Dnipropetrovsk and Kirovograd, and about 50,000 streets, squares and other toponymic objects (S538).

S539
- Ukraine's decommunization legislation obliged every city to remove a clearly identified list of Soviet place names, yet it gave no strict instructions about which new place names should appear instead (S539).
- Because the legislation set no strict rules for the new names, local authorities had a large range of discretion and chose renaming strategies from local cultural traditions and the electoral and political situation (S539).
- Gnatiuk found that south-eastern cities used that freedom to replace removed names with topographical or poetic street names or by restoring historical place names, while new names in western and central Ukraine commemorate the twentieth-century national liberation movements (S539).

Page support for the context sentences: S538 p. 2 ("more than 900 settlements and administrative-territorial units (including the regional centers of Dnipropetrovsk and Kirovograd), about 50,000 streets, squares and other toponymic objects ... have been renamed"; "about 70 belong to the cultural heritage of the indigenous population and national minorities of Ukraine - Crimean Tatars, Bulgarians, Greeks, Jews, etc."). S539 p. 120 ("all cities are legally obliged to go through decommunization. Clearly identified list of urban toponymy must perish from the maps"; "local communities have a large range of discretion. Local authorities can choose different renaming strategies, based on local cultural traditions together with electoral and political situation"), and p. 119 abstract ("using non-commemorative categories of street names, like topographical or poetic ones, or restoring the historical toponyms"; "new toponyms in western and central Ukraine reflect the legacy of the national liberation movements of the 20th century").

## 5. rejected

rejected:
- No other source was opened. These search-result leads were seen only as snippets and were NOT opened, so they are not offered: Verkhovna Rada news pages https://www.rada.gov.ua/en/news/News/132159.html and https://www.rada.gov.ua/en/print/131134.html (official, about the Dnipropetrovsk-to-Dnipro resolution; not opened because the two rows above already cover the assignment, and these press pages have few discipline terms [INFERENCE, unchecked]); Kudriavtseva 2020 https://www.ideopol.org/wp-content/uploads/2020/05/Eng.-04.-01.-2020.-Kudriavtseva-Full.pdf (not opened); Gnatiuk & Glybovets 2020, Geographia Polonica https://rcin.org.pl/igipz/Content/129235/WA51_160302_r2020-t93-no2_G-Polonica-Gnatiuk.pdf (not opened; a second Gnatiuk article would duplicate S539's angle); Wikipedia list of decommunized Ukrainian toponyms (tier C, not opened).
- No Kropyvnytskyi-specific official source was opened. S538 names Kirovograd among the renamed regional centres but does not give the new name, so the draft sentences do not say "Kropyvnytskyi".

## Remaining gaps

- No post-colonial African renaming source was opened; this seat covered the Ukrainian option of its brief only.

installs: none.
