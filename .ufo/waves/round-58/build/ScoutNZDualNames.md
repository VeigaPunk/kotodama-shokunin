# ScoutNZDualNames — claim C source item (S508, S509)

Seat: KotodamaR58A2.ScoutNZDualNames. Sources: official pages of the New Zealand Geographic Board Ngā Pou Taunaha o Aotearoa on linz.govt.nz, fetched with plain `curl` on 2026-10-23. Neither URL is in `corpus/SOURCES.md` (`grep -cF` returned 0 for both paths). Both rows pass LOCATE, BOILER, RELEVANCE and TOPIC.

What the rows give a worldbuilder:
- **S508** covers who may change a name and by what rule. Restoring a Māori mountain name was tested against written naming criteria (original Māori name first, no duplicate place names). The page also shows the outsider layer: Cook's honorific "Mount Egmont" stayed on maps after confiscation and settlement, and in the end both names were made official.
- **S509** also covers who may change a name. A place name made official through a Treaty settlement can be changed only with the written consent of the settlement group's trustees.

## Rows

| S508 | New Zealand Geographic Board Ngā Pou Taunaha o Aotearoa / Toitū Te Whenua LINZ, 2019 (updated 2024), Mount Taranaki or Mount Egmont — https://www.linz.govt.nz/our-work/new-zealand-geographic-board/place-name-stories/place-names-cooks-voyages/mount-taranaki-or-mount-egmont (direct, HTTP 200) | web | A | how the NZ naming authority restored a Māori mountain name under its naming criteria | para. on the 1983 approach to the NZGB: "the NZGB considered whether the name change met the naming criteria, including prioritising the original Māori name and avoiding duplications of place names" | Restoring a mountain's Māori name required the Board to test the change against criteria favouring original Māori names and avoiding duplicate names. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |
| S509 | New Zealand Geographic Board Ngā Pou Taunaha o Aotearoa / Toitū Te Whenua LINZ, n.d. (live 2026), Treaty of Waitangi claims settlement place names — https://www.linz.govt.nz/our-work/new-zealand-geographic-board/treaty-waitangi-claims-settlement-place-names (direct, HTTP 200) | web | A | how Treaty settlement place names are restored and then protected from change in New Zealand | section on the Board's role in Treaty settlements, para. 4: "Once official a Treaty settlement place name can only be changed with written consent from the trustees of the relevant Treaty settlement group." | A place name made official through a Treaty settlement is locked against change unless the settlement group's trustees consent in writing. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

Note: the S508 quote is a clause. The full sentence on the page begins "As required by legislation, " and is 27 words, which is over the 25-word cap.

## Gate lines

- S508 — https://www.linz.govt.nz/our-work/new-zealand-geographic-board/place-name-stories/place-names-cooks-voyages/mount-taranaki-or-mount-egmont — accessed 2026-10-23 — para. on the 1983 approach to the NZGB: “the NZGB considered whether the name change met the naming criteria, including prioritising the original Māori name and avoiding duplications of place names”. Grounds: Restoring a mountain's Māori name required the Board to test the change against criteria favouring original Māori names and avoiding duplicate names. Seat: ScoutNZDualNames.
- S509 — https://www.linz.govt.nz/our-work/new-zealand-geographic-board/treaty-waitangi-claims-settlement-place-names — accessed 2026-10-23 — section on the Board's role in Treaty settlements, para. 4: “Once official a Treaty settlement place name can only be changed with written consent from the trustees of the relevant Treaty settlement group.” Grounds: A place name made official through a Treaty settlement is locked against change unless the settlement group's trustees consent in writing. Seat: ScoutNZDualNames.

## rowcheck output

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutNZDualNames/rows.md` (exit 0):

```
S508 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.linz.govt.nz/our-work/new-zealand-geographic-board/place-name-stories/place-names-cooks-voyages/mount-taranaki-or-mount-egmont | BOILER: root-clear https://www.linz.govt.nz/; not a title, h1 or meta label | RELEVANCE: shared=['avoid', 'chang', 'crite', 'dupli', 'māori', 'name'] | TOPIC: quote_hits=1 function_words=3 page_hits=31 page_terms=21 need=1/2/3/2
S509 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.linz.govt.nz/our-work/new-zealand-geographic-board/treaty-waitangi-claims-settlement-place-names | BOILER: root-clear https://www.linz.govt.nz/; not a title, h1 or meta label | RELEVANCE: shared=['chang', 'conse', 'group', 'name', 'offic', 'place'] | TOPIC: quote_hits=1 function_words=6 page_hits=36 page_terms=28 need=1/2/3/2
```

Attack for the L1: the first draft of S509 put the section heading in double quotes inside the locator. rowcheck takes the FIRST double-quoted span of the anchor as QUOTE, so it tested the heading instead, and the heading shares a three-word run with the URL. The result was `LOCATE FAIL ... url-reflects-quote`. When writing locators in `corpus/SOURCES.md`, never put a heading or other text in double quotes before the anchor quote.

## draft sentences

S508 (page facts used: Cook named it "Mount Egmont" in January 1770 to honour the Earl of Egmont, who "had no direct connection with" the voyage; "The name ‘Egmont’ persisted on maps while the land was settled"; the 1985 NZGB resolution restored Taranaki with Egmont as a secondary name; 10,746 objections followed; the Minister "decided that both names – Mount Taranaki and Mount Egmont – would become official"; "Taranaki is now in widespread use"):
- When a mountain's original Māori name is restored, New Zealand's naming Board tests the name change against written naming criteria that put the original Māori name first and avoid duplications of place names (S508).
- Mount Taranaki shows the layers in one mountain: an original Māori name, then an outsider's honorific (Cook's 1770 "Mount Egmont", for an earl with no connection to the voyage) that stayed on maps after confiscation and settlement, then a 1985 Board decision to restore the original name under its criteria (S508).
- Restoring a name does not have to erase the outsider layer: after the Board's restoration drew 10,746 objections, the Minister made both names official, Mount Taranaki and Mount Egmont, and the original Māori name is now in widespread use (S508).

S509 (page facts used: names are part of cultural redress; the Board checks proposals against its "naming standards, policies and guidelines"; "The Minister makes the final decisions"; "The public aren’t consulted"; names are "published in the New Zealand Gazetteer, along with their histories"; renaming a town, city, suburb or locality needs a full proposal outside the Treaty process, with public consultation):
- In New Zealand, restoring original Māori place names is part of Treaty of Waitangi settlement redress, and once official, a Treaty settlement place name can be changed only with written consent from the settlement group's trustees (S509).
- The Board checks each proposed settlement name against its naming standards, the Minister makes the final decision without public consultation, and every settled name is published with its history in the New Zealand Gazetteer (S509).
- A settled name is therefore locked against later change unless the group's trustees consent, but changing the name of a town or city still needs a full public proposal outside the Treaty process (S509).

## rejected

- https://www.linz.govt.nz/our-work/new-zealand-geographic-board/place-name-stories/te-ika-maui-north-island-and-te-waipounamu-south-island (HTTP 200) passed rowcheck as a backup row, but I did not offer it because of the two-row cap. It is the better source for the **alternative-name** pattern (in 2013 the North and South Islands got Te Ika-a-Māui and Te Waipounamu as official alternative names, and the Minister said people "would not have to use the English and Māori names together"). If the L1 wants that pattern instead of S509, this is the tested row (from `/fast/scratch/hyaku/kotodama-r58/ScoutNZDualNames/rows-alt.md`; id S509 only for the test):
  `| S509 | New Zealand Geographic Board Ngā Pou Taunaha o Aotearoa / Toitū Te Whenua LINZ, n.d. (live 2026), Te Ika-a-Māui North Island and Te Waipounamu South Island — https://www.linz.govt.nz/our-work/new-zealand-geographic-board/place-name-stories/te-ika-maui-north-island-and-te-waipounamu-south-island (direct, HTTP 200) | web | A | how New Zealand made Māori and English island names official alternatives in 2013 | first para.: "Prior to this, the English names of the islands were not official and the Māori names had stopped being used on official maps." | Before 2013 neither English island name was official in New Zealand, and official maps had dropped the Māori names entirely. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |`
  rowcheck output: `S509 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.linz.govt.nz/our-work/new-zealand-geographic-board/place-name-stories/te-ika-maui-north-island-and-te-waipounamu-south-island | BOILER: root-clear https://www.linz.govt.nz/; not a title, h1 or meta label | RELEVANCE: shared=['engli', 'islan', 'maps', 'māori', 'name', 'offic'] | TOPIC: quote_hits=1 function_words=7 page_hits=28 page_terms=18 need=1/2/3/2`
- https://www.linz.govt.nz/our-work/new-zealand-geographic-board/place-name-stories/north-island-and-south-island-nzgb-decisions-17-october-2013 (HTTP 200): this is the legal Gazette notice behind the alternative-names page above. It adds nothing a worldbuilder needs beyond that page.
- https://www.linz.govt.nz/our-work/new-zealand-geographic-board/about-new-zealand-geographic-board (HTTP 200): a general remit page (give, approve and change names; maintain the Gazetteer). It is less specific than S509, and the two-row cap applies.
- https://www.linz.govt.nz/guidance/place-naming (HTTP 200): a landing page of about 846 characters of body text, mostly navigation, with no anchorable sentence.
- https://www.linz.govt.nz/resources/guide/restoring-original-maori-place-names and https://www.linz.govt.nz/resources/guide/survey-pegs-past-understanding-maori-place-names: both served HTTP 202 with an empty body (curl `-w "%{http_code} ..."` printed `202 resources/guide/restoring-original-maori-place-names` and `202 resources/guide/survey-pegs-past-understanding-maori-place-names`; the extracted text length was `0`). I made no further attempt, so no access control was bypassed.
- Guessed paths that returned HTTP 404 (none were sources): https://www.linz.govt.nz/guidance/place-names/dual-and-alternative-place-names, https://www.linz.govt.nz/guidance/place-names/maori-place-names, https://www.linz.govt.nz/our-work/place-naming, https://www.linz.govt.nz/guidance/place-names (curl printed `404 ...` for each).
- https://www.linz.govt.nz/ and https://www.linz.govt.nz/sitemap.xml: used only to find URLs, never offered as sources.

I found no LINZ page that is specifically about Aoraki / Mount Cook as a dual name. The sitemap lists only an oral-history story (`.../maori-oral-history-atlas/rakaihautu-naming-great-lakes-canoe-aoraki`) and First World War pages that mention the mountain. I did not open them.

## installs:

none.
