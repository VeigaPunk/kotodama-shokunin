# ScoutGermanPlaceNames — round 58, claim C source item (S526, S527)

Seat: KotodamaR58A2.ScoutGermanPlaceNames. Accessed 2026-10-23. Both rows pass every check below; both come from the Swiss National Museum's English history blog (the federal museum, written by dialectologist and historian André Perler). They cover German-language settlement-name endings and clearing names in German-speaking Switzerland. The Germany-only institutional source with the best suffix-dating text (Leibniz-Institut für Länderkunde, nationalatlas.de) is German-language and fails TOPIC (see `rejected:`).

Worldbuilder decisions the rows serve:
- **S526:** what a settlement name is built from (a specific element plus a period ending such as -ingen, -ikon, -dorf or -wil), and which language layer it belongs to (Celtic, then Latin, then Alemannic; the newcomers also re-shape older names).
- **S527:** clearing names (Rüti, then Schwand) date when land was opened. Field and locality names record land use, ownership and bans.

URL novelty: `grep -cF` on corpus/SOURCES.md returned 0 for both URLs and for the host `blog.nationalmuseum.ch`.

## (1) Registry rows

| S526 | André Perler (Swiss National Museum, Swiss history blog), 2023, From ‘Uitoduro’ to ‘Winti’: how place names change — https://blog.nationalmuseum.ch/en/2023/05/from-uitoduro-to-winti-how-place-names-change/ (direct, HTTP 200) | web | B | Alemannic settlement-name endings (-ingen, -ikon, -dorf, -wil) as the Germanic layer over Celtic and Latin names in German-speaking Switzerland | § Yet another change of language, ¶ 1: "they founded a large number of new settlements (with place names ending in -ingen, ‑ikon, -dorf and -wil)" | Alemannic settlers gave many of the new settlements they founded names ending in -wil, -dorf, -ikon or -ingen. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |
| S527 | André Perler (Swiss National Museum, Swiss history blog), 2022, “Rüti” and “Schwand” indicate historical clear-felling of forests — https://blog.nationalmuseum.ch/en/2022/07/rueti-and-schwand-indicate-historical-clear-felling-of-forests/ (direct, HTTP 200) | web | B | clearing names (Rüti from Middle High German riuten, later Schwand) as dated evidence of land expansion in German-speaking Switzerland | ¶ 3 (riuten, Rüti, Rütli): "These Rüti toponyms are considered evidence of the first phase of land expansion and large-scale cultivation" | Place names of the Rüti type record cleared land and are read as evidence of the earliest wave of expansion and cultivation. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

Notes for the L1:
- **S526 quote:** this is the main clause of a 34-word sentence; the full sentence is over the 25-word cap. The source text reads "‑ikon" with a non-breaking hyphen (U+2011), and the quote keeps it verbatim. The page sentence just before it names the subject: "The migration of the Alemanni to the territory of what is now German-speaking Switzerland from the 6th century onwards brought another change of language."
- **S527 quote:** this is the first clause of a 37-word sentence. Its antecedent, two sentences earlier, says the names "can be traced back to Middle High German riuten, “to clear”" and that there are "more than 10,000 such toponyms in the German-speaking part of Switzerland".
- **Tier B rationale:** the publisher is a federal institution (Schweizerisches Nationalmuseum), the posts are signed, and each page states "André Perler is a dialectologist and historian and works at SRF as a dialect editor."
- **Shared site:** both rows come from one site but use different URLs. That meets the one-URL-per-row rule. If the L1 wants host diversity, drop one row.

## (2) Gate lines

- S526 — https://blog.nationalmuseum.ch/en/2023/05/from-uitoduro-to-winti-how-place-names-change/ — accessed 2026-10-23 — § Yet another change of language, ¶ 1: “they founded a large number of new settlements (with place names ending in -ingen, ‑ikon, -dorf and -wil)”. Grounds: Alemannic settlers gave many of the new settlements they founded names ending in -wil, -dorf, -ikon or -ingen. Seat: KotodamaR58A2.ScoutGermanPlaceNames.
- S527 — https://blog.nationalmuseum.ch/en/2022/07/rueti-and-schwand-indicate-historical-clear-felling-of-forests/ — accessed 2026-10-23 — ¶ 3 (riuten, Rüti, Rütli): “These Rüti toponyms are considered evidence of the first phase of land expansion and large-scale cultivation”. Grounds: Place names of the Rüti type record cleared land and are read as evidence of the earliest wave of expansion and cultivation. Seat: KotodamaR58A2.ScoutGermanPlaceNames.

## (3) Rowcheck output

Command: `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutGermanPlaceNames/rows.md` (exit 0)

```
S526 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://blog.nationalmuseum.ch/en/2023/05/from-uitoduro-to-winti-how-place-names-change/ | BOILER: root-clear https://blog.nationalmuseum.ch/; not a title, h1 or meta label | RELEVANCE: shared=['dorf', 'endin', 'found', 'ikon', 'ingen', 'name'] | TOPIC: quote_hits=1 function_words=5 page_hits=22 page_terms=22 need=1/2/3/2
S527 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://blog.nationalmuseum.ch/en/2022/07/rueti-and-schwand-indicate-historical-clear-felling-of-forests/ | BOILER: root-clear https://blog.nationalmuseum.ch/; not a title, h1 or meta label | RELEVANCE: shared=['culti', 'evide', 'expan', 'land', 'rüti'] | TOPIC: quote_hits=1 function_words=4 page_hits=19 page_terms=15 need=1/2/3/2
exit=0
```

## (4) Draft sentences

S526:
- In German-speaking Switzerland the Alemanni, arriving from the 6th century, founded a large number of new settlements whose place names end in -ingen, -ikon, -dorf and -wil (S526).
- The same settlers also took over many existing settlements and adapted their older names to their Germanic language, which is how today's Swiss German settlement names evolved (S526).
- Beneath that Germanic layer, Celtic place names such as Thun and Yverdon were Romanised, and Celtic-Latin hybrids ending in -ach(t), such as Bettlach and Küsnacht, are more common than purely Latin names (S526).
- In the Romance-speaking parts of Switzerland no such change of language happened, and local place names developed within the Romance dialects instead of taking Germanic endings (S526).

S527:
- More than 10,000 toponyms in German-speaking Switzerland, such as Rüti, Rüttene and Grüt, go back to Middle High German riuten, "to clear", and Rüti names are taken as evidence of the first phase of land expansion and cultivation (S527).
- Schwand and Schwendi names come from a clearance method that killed trees by peeling off a strip of bark. They lie mainly in the Alpine area and its foothills, farther from the main settlements than Rüti names, and so mark a later phase of land expansion (S527).
- Locality names such as Brand and Stocke record slash-and-burn clearance, and the name Bannwald records an official ban on use. A district's toponyms therefore keep evidence of cultivation and land management that document collections often lack (S527).

## (5) rejected:

- **https://www.econstor.eu/bitstream/10419/279184/1/cesifo1_wp10435.pdf** (Nguyen, Brakman, Garretsen and Kohl, CESifo WP 10435, an English paper on German toponym suffixes). The repository serves a bot challenge to plain requests, and bypassing it is forbidden (QUALITY criterion 10). The fetch (reopen-quote `fetch`/`to_text`) returned `text/html; charset=utf-8 1756` with body: `Making sure you're not a bot! ... You are seeing this because EconStor has set up Anubis to protect the server ... Sadly, you must enable JavaScript to get past this challenge.`
- **https://www.ifo.de/DocDL/cesifo1_wp10435.pdf** and **https://www.ifo.de/en/cesifo/publications/2023/working-paper/whats-name-initial-geography-and-german-urban-development** (other copies of the same paper). Both serve a JavaScript client challenge to plain requests. Fetch output: `ifopdf text/html; charset=utf-8 481`, `ifopage text/html; charset=utf-8 481`, body: `Client Challenge ... JavaScript is disabled in your browser. Please enable JavaScript to proceed.`
- **https://nationalatlas.de/wp-content/uploads/23_05_Ortsnamen.pdf** (Brogiato and Hanewinkel, Leibniz-Institut für Länderkunde, 2023). This has the best suffix-dating text: -heim, -ingen, -stedt and -stetten from the first Landnahme after the 4th century; -dorf, -hausen and -weiler from the Merovingian early expansion; -roth, -reut and -schwand clearing names from the 10th century. It is in German, though: the quote has no NAMING-PLACE window and no English function words, so TOPIC fails. Rowcheck output: `S526 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC FAIL | ... | TOPIC: quote_hits=0 function_words=0 page_hits=12 page_terms=35 need=1/2/3/2`. It is usable as a lead for the L1's own understanding, not as a row.
- **https://germanistik.uni-greifswald.de/en/department/further-organisational-units/pomeranian-dictionary/dfg-project-digital-book-of-vorpommern-field-names/** (University of Greifswald, Vorpommern field names). The page does not use the field's terms enough to pass TOPIC. Rowcheck output: `S527 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC FAIL | ... | TOPIC: quote_hits=1 function_words=6 page_hits=1 page_terms=1 need=1/2/3/2`.
- **https://www.akademienunion.de/en/research/project-database/toponymies-between-rhine-and-elbe-onomastics-in-the-european-area** (Union of German Academies, Göttingen place-name project). Not offered: the 2-row cap is filled, and its only usable sentence ("Because toponyms are partly of old age, they extend far into the preliterate time.") is about the age of names, not suffixes or field names. My draft teaches cell also failed RELEVANCE; that is a wording problem, not a source defect. Rowcheck output: `S528 LOCATE PASS BOILER PASS RELEVANCE FAIL TOPIC PASS | ... | RELEVANCE: quote-teaches shared=['preli'] | TOPIC: quote_hits=1 function_words=3 page_hits=6 page_terms=12`. A strata or oldest-layer seat could still use it.
- **https://adw-goe.de/en/research/research-projects-within-the-academies-programme/place-names-between-rhine-and-elbe/** (Göttingen Academy project page). Not offered: it has no suffix or field-name content, and its window sentences run past 25 words. Probe output (probe.py uses rowcheck's own `window_hits`/`DISCIPLINE`): `page_hits 9 terms 14`; window sentences of 35 and 27 words.
- **https://ul.qucosa.de/landing-page/https%3A%2F%2Ful.qucosa.de%2Fapi%2Fqucosa%253A16338%2Fmets%2F/** (Peter Ernst 2016, English abstract on Old High German -ing names). Not offered: the cap is filled. Its window sentence ("The place names ending with -ing are a special phenomenum in Old High German.") teaches less than S526, and its settlement-history sentence has no window. Probe output: `page_hits 3 terms 3` (the bare minimum).
- **https://ul.qucosa.de/id/qucosa%3A80452** (Aehnlich 2021, Thuringian field-name portal). Not offered: the only sentence with a window is 34 words, over the 25-word cap. Probe output: `page_hits 3 terms 9`; window sentence of 34 words, "The article is a report on work in progress and presents the Thuringian approach ... field name research based on citizen science."
- **https://www.namenkundliche-informationen.de/ni/article/view/735** (Blaßnigg, Salzburg settlement history in Namenkundliche Informationen). Not offered: it is outside my scope (Austrian language strata, not German suffixes), and every window sentence is 34–38 words. Probe output: `page_hits 7 terms 5`. Lead for a strata seat: the clause "evidenced by the presence of Indo-European names associated with ancient European hydronymy, as well as Celtic, Romance, Slavic, and Bavarian names" is 22 words; I have not rowchecked it.

Scratch: /fast/scratch/hyaku/kotodama-r58/ScoutGermanPlaceNames/ (rows.md, rejected-rows.md, probe.py, fetched texts). No background processes were left running.

installs: none.
