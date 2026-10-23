# ScoutRomanizationSystems — round 58, claim C source item (S534, S535)

Seat: KotodamaR58A2.ScoutRomanizationSystems. Accessed 2026-10-23. Both rows come from the UNGEGN Working Group on Romanization Systems (WGRS) site, an official UN working group site hosted by the Institute of the Estonian Language (EKI; the long-serving convenor Peeter Päll is from EKI). The site carries a banner saying that since May 2023 it is an archive that stays online but is no longer updated. The live successor page, https://unstats.un.org/UNSDWebsite/ungegn/wg/romanization, returns HTTP 200 but only as a 2611-byte JavaScript shell with no body text that a plain request can read, so it can carry no quote. `grep -F 'eki.ee'`, `grep -i ungegn` and `grep -i unstats` against corpus/SOURCES.md return nothing, so neither URL is already registered.

## (1) Registry rows

| S534 | UNGEGN Working Group on Romanization Systems (archive site hosted by the Institute of the Estonian Language, EKI), updated 2023-12-21, UNGEGN Working Group on Romanization Systems: main page, Terms of reference — https://arhiiv.eki.ee/wgrs/ (direct, HTTP 200) | docs | A | how a romanization system for a country's geographic names becomes the UN standard | Terms of reference ¶1: "The basic mandate of the Working Group consists of considering and reaching agreement on a romanization system for geographic names proposed by a (donor) country." | Under the UN process a country proposes the romanization system for its own geographic names, and the expert working group must reach agreement before adoption. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |
| S535 | UNGEGN Working Group on Romanization Systems, 2016, Report on the Current Status of United Nations Romanization Systems for Geographical Names, Version 4.0: Russian — https://arhiiv.eki.ee/wgrs/rom1_ru.htm (direct, HTTP 200) | docs | A | reversibility limits of romanized geographical names (UN Russian system) | Russian, ¶2: "For example, a geographical name Bajuba is reconstituted as Байуба in the Cyrillic source script, not Баюба as might be expected." | Even the reversible UN Russian romanization has rare ambiguities: the romanized geographical name Bajuba converts back to Байуба rather than the expected Баюба. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

Page context a reviewer will see, which supports the teaches cells and draft sentences:
- S534 (https://arhiiv.eki.ee/wgrs/): in the same Terms of reference, the group "considers whether the romanization system is based on sound scientific principles, the system's degree of reversibility, and the extent of its implementation on cartographic products (maps and charts) by the proposing country", and "When the resolution is adopted, the subject romanization system becomes the United Nations standard." The status table on the page lists 30 languages or scripts with UN-recommended systems and 15 "Other languages/scripts" (among them Japanese, Korean, Armenian and Kazakh).
- S535 (https://arhiiv.eki.ee/wgrs/rom1_ru.htm): "The United Nations recommended system was approved in 1987 (V/18), based on the official system of the Main Administration of Geodesy and Cartography of the former Soviet Union"; "The system is reversible, although rarely there can be ambiguities." The page also sets the competing BGN/PCGN 1947 and ISO 9:1995 renderings beside the UN one (ж is ž under the UN system and zh under BGN/PCGN; я is ja under the UN system, ya under BGN/PCGN and â under ISO 9).

## (2) Gate lines

- S534 — https://arhiiv.eki.ee/wgrs/ — accessed 2026-10-23 — Terms of reference ¶1: “The basic mandate of the Working Group consists of considering and reaching agreement on a romanization system for geographic names proposed by a (donor) country.” Grounds: Under the UN process a country proposes the romanization system for its own geographic names, and the expert working group must reach agreement before adoption. Seat: ScoutRomanizationSystems.
- S535 — https://arhiiv.eki.ee/wgrs/rom1_ru.htm — accessed 2026-10-23 — Russian, ¶2: “For example, a geographical name Bajuba is reconstituted as Байуба in the Cyrillic source script, not Баюба as might be expected.” Grounds: Even the reversible UN Russian romanization has rare ambiguities: the romanized geographical name Bajuba converts back to Байуба rather than the expected Баюба. Seat: ScoutRomanizationSystems.

## (3) rowcheck output (rows at /fast/scratch/hyaku/kotodama-r58/ScoutRomanizationSystems/rows.md)

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutRomanizationSystems/rows.md` (exit 0):

```
S534 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://arhiiv.eki.ee/wgrs/ | BOILER: root-clear https://arhiiv.eki.ee/; not a title, h1 or meta label | RELEVANCE: shared=['agree', 'count', 'geogr', 'group', 'name', 'propo'] | TOPIC: quote_hits=1 function_words=7 page_hits=24 page_terms=23 need=1/2/3/2
S535 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://arhiiv.eki.ee/wgrs/rom1_ru.htm | BOILER: root-clear https://arhiiv.eki.ee/; not a title, h1 or meta label | RELEVANCE: shared=['bajub', 'expec', 'geogr', 'name', 'байуб', 'баюба'] | TOPIC: quote_hits=1 function_words=7 page_hits=4 page_terms=4 need=1/2/3/2
```

The checks above ran without `--entry`. Once the entry exists, legs (c) and (d) need each citing line to share at least 2 stems with the teaches cell and with the quote. The draft sentences below were written for that: S534 sentences reuse agreement, country, geographic, names, romanization and proposes; S535 sentences reuse geographical, name, Bajuba, expected and Байуба.

## (4) draft sentences

S534:
- Who romanizes a place name is itself a naming decision: the UN does not invent romanization systems for geographic names; a (donor) country proposes one for its own language and the UNGEGN Working Group on Romanization Systems considers it until it reaches agreement (S534).
- The working group asks whether a proposed romanization system for geographic names rests on sound scientific principles, how reversible it is, and how far the proposing country already uses it on its own maps and charts (S534).
- Agreement is not the last step: the system goes to a UN Conference on the Standardization of Geographical Names as a resolution, and once that is adopted the country's proposal becomes the United Nations standard for romanizing its geographic names (S534).

S535:
- Romanization loses information even in a system built to be reversible: under the UN Russian system the geographical name Bajuba is reconstituted as Байуба, not the Баюба a reader might have expected (S535).
- For a worldbuilder, this kind of ambiguity is how outsiders mangle a name: a geographical name written in a foreign script can come back from its romanized form with an unexpected spelling (S535).
- Rival systems give one place name different Latin spellings: the UN Russian romanization that turns the geographical name Bajuba back into Байуба writes ж as ž, the BGN/PCGN 1947 system writes zh, and ISO 9:1995 writes я as â where the UN system writes ja (S535).

## (5) rejected

- https://unstats.un.org/unsd/ungegn/wg/romanization/: HTTP 404 (curl `404 https://unstats.un.org/unsd/ungegn/wg/romanization/ 1245`).
- https://unstats.un.org/UNSDWebsite/ungegn/wg/romanization: HTTP 200, but it is a 2611-byte JavaScript shell (`<!doctype html>…googletagmanager…`) with no body text, so there is no quotable sentence.
- https://unstats.un.org/unsd/ungegn/pubs/: fetched (HTTP 200, 90997 bytes) only to probe the site; not mined. It is an index of publications, and other seats cover UNGEGN glossary and manual material.
- https://arhiiv.eki.ee/wgrs/rom1_status.htm (reached through the www.eki.ee redirect) and https://arhiiv.eki.ee/wgrs/rom1_ja.htm: both HTTP 404 (curl `404 https://arhiiv.eki.ee/wgrs/rom1_status.htm 297`; `rom1_ja 404 293`).
- https://arhiiv.eki.ee/wgrs/status.htm: opened. Its only prose is about version numbering (V4 becoming V5), and the language statuses are table cells, so it has no anchor that meets the row rules. The same status table is on the main page (S534).
- https://arhiiv.eki.ee/wgrs/resolutions.htm: opened. The single-romanization principle appears only as list items ("I/9. A single romanization system"; "III/25. Single romanization system for each non-Roman writing system"), and list items are barred as anchors.
- https://arhiiv.eki.ee/wgrs/wg.htm: opened. Its single-romanization sentence ("The working group was established at the 2nd session of UNGEGN in 1970, originally it was called the Working Group on a Single Romanization System.") is 25 normalised words, but its only name-like token is the acronym UNGEGN, so it holds no NAMING-PLACE window. The 1972 rename sentence runs past 25 words, and so does the "no mandate to review any other systems" sentence. Both fail by word count and were not run through the checker.
- https://arhiiv.eki.ee/wgrs/rom1_zh.htm: fetched (HTTP 200) and not mined, because KotodamaR58A2.ScoutPinyinUN covers the Chinese system.

Gap: none of the pages I opened carries the single-romanization principle (one UN system per non-Roman script) in a sentence that meets the row rules. In these sources it survives only as resolution titles and the working group's former names.

installs: none.
