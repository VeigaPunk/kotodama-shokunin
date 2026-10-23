# ScoutRiverNames — round 58, claim C source item (river names / hydronymy)

Seat: KotodamaR58A2.ScoutRiverNames. S-ids: S518, S519. Sources opened 2026-10-23 UTC by plain GET (reports/round-58/reopen-quote.py `fetch`, curl). Both URLs grep-checked absent from corpus/SOURCES.md (`grep -c -F snsbi.org.uk corpus/SOURCES.md` → 0).

## Rows

| S518 | Eleanor Rye and Diana Whaley (Society for Name Studies in Britain and Ireland), 2023, Languages in the Place-Names of Britain and Ireland — https://www.snsbi.org.uk/exploring-names/languages/ (direct, HTTP 200) | web | B | Old European stratum of British river-names | section Old European, paragraph 1: "‘Old European’ origins are postulated for names, above all river-names, which recur widely within the Indo-European world" | Name scholars assign Old European origins chiefly to river-names that recur widely across the Indo-European language world. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |
| S519 | Carole Hough (Society for Name Studies in Britain and Ireland), 2024, Introducing the place-names of Scotland — https://www.snsbi.org.uk/exploring-names/place-names-of-scotland/ (direct, HTTP 200) | web | B | river-names embedded in Scottish city names | section City names, paragraph 1: "Aberdeen and Inverness both contain early Celtic river-names, Don and Ness, combined with words for a river-mouth" | The city names Aberdeen and Inverness each pair an early Celtic river-name with a word meaning the mouth of a river. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

Authorship: the pages' own footers read `© Eleanor Rye and Diana Whaley 2023` and `© Carole Hough 2024`. Both sit under the SNSBI statement that the materials are "produced by individual members of the Society". Tier B means a learned-society explainer by named scholars. It is not a peer-reviewed paper.

## Gate lines

- S518 — https://www.snsbi.org.uk/exploring-names/languages/ — accessed 2026-10-23 — section Old European, paragraph 1: “‘Old European’ origins are postulated for names, above all river-names, which recur widely within the Indo-European world”. Grounds: Name scholars assign Old European origins chiefly to river-names that recur widely across the Indo-European language world. Seat: ScoutRiverNames.
- S519 — https://www.snsbi.org.uk/exploring-names/place-names-of-scotland/ — accessed 2026-10-23 — section City names, paragraph 1: “Aberdeen and Inverness both contain early Celtic river-names, Don and Ness, combined with words for a river-mouth”. Grounds: The city names Aberdeen and Inverness each pair an early Celtic river-name with a word meaning the mouth of a river. Seat: ScoutRiverNames.

## rowcheck output

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutRiverNames/rows.md`

```
S518 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.snsbi.org.uk/exploring-names/languages/ | BOILER: root-clear https://www.snsbi.org.uk/; not a title, h1 or meta label | RELEVANCE: shared=['europ', 'indo', 'name', 'origi', 'recur', 'river'] | TOPIC: quote_hits=2 function_words=4 page_hits=43 page_terms=30 need=1/2/3/2
S519 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.snsbi.org.uk/exploring-names/place-names-of-scotland/ | BOILER: root-clear https://www.snsbi.org.uk/; not a title, h1 or meta label | RELEVANCE: shared=['aberd', 'celti', 'early', 'inver', 'mouth', 'name'] | TOPIC: quote_hits=1 function_words=4 page_hits=66 page_terms=48 need=1/2/3/2
exit 0
```

(RELEVANCE legs (c) and (d) will only run once the entry exists. The L1 should rerun with `--entry`.)

## draft sentences

S518 (the page's Old European section, which opens with “The earliest stratum of place-names in Britain whose linguistic affiliation is identifiable are those termed ‘Old European’” and lists Adder/Oder, Allan/Ellen/Alauna, Don/Danube/Don, and Wear/Wyre/Weser, and adds “There is naturally a good deal of uncertainty about this ancient stratum.”):
- Name scholars postulate Old European origins above all for river-names that recur widely across the Indo-European world (S518).
- The same page calls Old European the earliest stratum of place-names in Britain whose linguistic affiliation is identifiable. Its river-names include the Don, compared with the Danube, and the Wear and Wyre, compared with the Weser (S518).
- The page also says there is a good deal of uncertainty about this ancient stratum. Old European origins for these river-names are postulated, not proven (S518).

S519 (the page's City names section, and its settlement paragraph: “others consist solely of a river-name … Ayr, Cullen, Leith and Nairn have historical spellings with Gaelic inbhir, showing that, like Inverness, they originally described a river-mouth”):
- The city names Aberdeen and Inverness each contain an early Celtic river-name, the Don and the Ness. Each river-name is combined with a word for a river-mouth: Pictish aber in Aberdeen and Gaelic inbhir in Inverness (S519).
- Dundee probably also contains a river-name, the Tay, which the page dates to the even earlier Old European stratum, so one city name can hold two layers of names (S519).
- Some Scottish settlement-names, such as Ayr, Girvan, Irvine and Nairn, consist solely of a river-name. Historical spellings of Ayr, Cullen, Leith and Nairn with Gaelic inbhir show that these names once described a river-mouth (S519).

Worldbuilder framing for the L1 (my inference, not carried by either page, so it must not be cited to S518 or S519): the river-name is the element a settlement name inherits from the oldest layer. Later languages wrap it in their own generic for "river-mouth" or "fort".

## rejected

- https://www.snsbi.org.uk/Nomina_articles/Nomina_35_Coates.pdf (Richard Coates, A toponomastic contribution to the linguistic prehistory of the British Isles, Nomina 35; HTTP 200, application/pdf, opened). The paper is mainly about island names. Its one river sentence, “Most scholars accept that the ancient river-nomenclature of the islands includes a strong Indo-European component which Nicolaisen (2001), following Krahe (1963), calls ‘Old European’”, runs over 25 words. It also has no NAMING-stem word: `nomenclature` is not in the rowcheck NAMING set. A cut-down quote would fail TOPIC quote_hits.
- https://www.nottingham.ac.uk/english/documents/innervate/22-23/engl3002-kathryn-hardy.pdf (Kathryn Hardy, A linguistic analysis of the river-names of two English counties, Innervate 2022-23; HTTP 200, application/pdf, opened). It is an undergraduate dissertation, which is weaker than the SNSBI pages written by established scholars. I left it out because of the 2-row cap. Usable lead: “In English river-names, this earliest stratum is an ancient, possibly pre-Celtic language.”
- https://openjournals.library.sydney.edu.au/JSSSH/article/download/7186/7650 (Scottish Place-Names and Their Sources, Journal of the Sydney Society for Scottish History). The server refused a plain GET, and I made no bypass attempt. Tool output: `urllib.error.HTTPError: HTTP Error 403: Forbidden` (reopen-quote.py `fetch`), and `curl` printed `403 text/html; charset=UTF-8` with an HTML block page. The reopen-quote locator could not re-open it either.
- Search-result leads I did not open, so they are not offered: doi.org/10.1111/j.1467-968x.2005.00155.x (Coates, Four pre-English river names, Wiley), doi.org/10.1111/j.1467-968x.1996.tb01178.x (Kitson 1996, Wiley), journals.lki.lt Bichlmeier (German), and spns.org.uk Watson transcriptions.

installs: none.
