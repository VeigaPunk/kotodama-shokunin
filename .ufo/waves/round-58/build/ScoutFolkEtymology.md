# ScoutFolkEtymology — round 58, claim C source item (folk etymology of place names)

Seat: KotodamaR58A2.ScoutFolkEtymology. S-ids: S542, S543 (both used). Accessed 2026-10-23.
Neither host is already in `corpus/SOURCES.md`: `grep -cF` returned 0 for `snsbi.org.uk`, `onomasticafelecan.ro`, `30816` and `iconn`.

Worldbuilder design decisions these rows serve:
- S542: how outsiders mangle a name. A pre-English river name is re-heard by the next language as familiar words ("cock wood"), and later scribes add a French-looking spelling.
- S543: how often reshaping happens. Folk etymology is reputed to be common in place names, but counted corpora put it under 1%. A setting should keep reshaped names as rare exceptions, most likely where an old generic word has gone out of use.

## (1) Registry rows

| S542 | Diana Whaley / Society for Name Studies in Britain and Ireland (SNSBI), 2024, River Coquet (Exploring names: place-name stories) — https://www.snsbi.org.uk/exploring-names/place-names/coquet-river/ (direct, HTTP 200) | web | B | a pre-English river name reshaped by folk etymology into English-looking words | section River turned wood, para. 1: "The History of St Cuthbert (Historia de Sancto Cuthberto) of the late eleventh century shows the river-name transformed into a very English-looking Cocwudu ‘cock wood’" | A late eleventh-century Cuthbert history recasts the pre-English river-name Coquet as Cocwudu, an English-seeming cock wood, by folk etymology. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |
| S543 | Katalin Reszegi (University of Debrecen), 2023, Folk etymology from a cognitive perspective, in O. Felecan and A. Bugheşiu (eds.), Proceedings of ICONN 6, pp. 889–899, doi:10.30816/ICONN6/2023/66 — https://onomasticafelecan.ro/iconn6/proceedings/4_13_Katalin_Reszegi_ICONN_6.pdf (direct, HTTP 200) | paper | A | how rare folk-etymological reshaping is in counted place-name corpora | §2.2 The frequency of folk etymology, p. 896: "The examination of the toponym corpus of different regions shows that less than 1% of the corpus was created in this way." | Examining Hungarian toponym corpus data region by region, folk etymology accounts for under one percent of recorded place names. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/toponymy-place-names.md |

Notes for the L1:
- Do not put a double quote in the locator part of either anchor cell. `row_target` takes the first double-quoted span in the anchor cell, so a quoted section title would replace the real quote. My first draft did this and failed LOCATE with "quote under 8 words".
- Quote length for S542: 25 words counted as written, but 27 after normalisation, because "river-name" and "English-looking" each split into two words. It is one full main clause, cut before the participle phrase ", referring to male birds, perhaps woodcock". If the L1 counts normalised words against the 8–25 rule, S542 is over by 2. No shorter clause on the page that carries this point holds a NAMING-PLACE window.
- S543 resolves through `https://doi.org/10.30816/iconn6/2023/66`, which answers HTTP 302 to the PDF URL above. The row cites the direct PDF.
- Tier choices: S542 is B because it is a learned-society explainer page with a named scholarly author (© Diana Whaley 2024) and a source list. S543 is A because it is a scholarly conference-proceedings paper with a DOI, from the ICONN 6 proceedings.

## (2) Gate lines

- S542 — https://www.snsbi.org.uk/exploring-names/place-names/coquet-river/ — accessed 2026-10-23 — section River turned wood, para. 1: “The History of St Cuthbert (Historia de Sancto Cuthberto) of the late eleventh century shows the river-name transformed into a very English-looking Cocwudu ‘cock wood’”. Grounds: A late eleventh-century Cuthbert history recasts the pre-English river-name Coquet as Cocwudu, an English-seeming cock wood, by folk etymology. Seat: KotodamaR58A2.ScoutFolkEtymology.
- S543 — https://onomasticafelecan.ro/iconn6/proceedings/4_13_Katalin_Reszegi_ICONN_6.pdf — accessed 2026-10-23 — §2.2 The frequency of folk etymology, p. 896: “The examination of the toponym corpus of different regions shows that less than 1% of the corpus was created in this way.” Grounds: Examining Hungarian toponym corpus data region by region, folk etymology accounts for under one percent of recorded place names. Seat: KotodamaR58A2.ScoutFolkEtymology.

## (3) rowcheck output

`cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && timeout 900 python3 -B reports/round-58/rowcheck.py --draft /fast/scratch/hyaku/kotodama-r58/ScoutFolkEtymology/rows.md` (exit 0):

```
S542 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://www.snsbi.org.uk/exploring-names/place-names/coquet-river/ | BOILER: root-clear https://www.snsbi.org.uk/; not a title, h1 or meta label | RELEVANCE: shared=['centu', 'cock', 'cocwu', 'cuthb', 'eleve', 'engli'] | TOPIC: quote_hits=1 function_words=3 page_hits=27 page_terms=12 need=1/2/3/2
S543 LOCATE PASS BOILER PASS RELEVANCE PASS TOPIC PASS | LOCATE: https://onomasticafelecan.ro/iconn6/proceedings/4_13_Katalin_Reszegi_ICONN_6.pdf | BOILER: root-clear https://onomasticafelecan.ro/; not a title, h1 or meta label | RELEVANCE: shared=['corpu', 'exami', 'regio', 'topon'] | TOPIC: quote_hits=1 function_words=6 page_hits=35 page_terms=27 need=1/2/3/2
```

I also ran the same command with `--entry` pointing at a scratch file holding the draft sentences below. The output was the same: all four legs PASS for both rows, so RELEVANCE (c) and (d) bind. Separately, I checked each draft sentence by itself with `rowcheck.stems`. Every sentence shares at least 2 stems with its row's quote and at least 2 with its teaches cell.

## (4) draft sentences

S542 (opened page: SNSBI, River Coquet):
- Folk etymology reshapes an opaque name toward familiar words: a late eleventh-century history of St Cuthbert shows the pre-English river-name Coquet transformed into English-looking Cocwudu, ‘cock wood’ (S542).
- The reshaped river-name can still suit its land: the same page calls ‘cock wood’ curiously appropriate because central Northumberland was historically quite heavily wooded (S542).
- Later spellings add a further layer to the river-name after the eleventh-century Cocwudu: Coket dominates late medieval documents, perhaps under French-trained scribes, and the French-looking Coquet became the standard modern form (S542).

S543 (opened paper: Reszegi, ICONN 6, pp. 896–897):
- Folk etymology is rarer than its reputation: examining the Hungarian toponym corpus of different regions, Reszegi finds that less than one percent of recorded place names were created that way (S543).
- Within that toponym corpus, the more than 5,500 place names of two Hajdú districts held only ten folk-etymological variants, and only one, Hat-ház ‘six houses’ to Hadház ‘war + house’, pushed out the earlier form (S543).
- In the historical toponym corpus of Abaúj and Bars counties, only one of 1,430 names was reshaped this way: the castle name Bódvakő, built on the river name Bódva, became Boldogkő ‘happy rock’ (S543).
- The paper partly blames lost generic words: when geographical common nouns such as jó ‘watercourse’ fell out of Hungarian, place names turned opaque and some were reshaped, yet such cases remain a very low share of any regional toponym corpus (S543).

Attack to pre-empt at SUPPORT, S543: the quote's "in this way" refers back to folk etymology. The paper's §2.2 heading, "The frequency of folk etymology", and the sentences before the quote on p. 896 make that reference plain. The paper's own figures for each district (0.52%, 0.01%, 0.18%) carry the "under one percent" in the teaches cell.

## (5) rejected

- https://www.snsbi.org.uk/exploring-names/interpreting-place-names/ (SNSBI, Interpreting place-names, opened 2026-10-23). It has a good general definition: "Another kind of non-standard change is folk etymology or popular etymology, where users of a name modify its form in a more familiar direction", with Rosedale and Leatherhead as examples. Rejected for two reasons. First, the full sentence runs past 25 words, and the clause that fits holds no place word near "name", by my reading of the NAMING and PLACE stem sets. I did not run rowcheck on it. Second, the seat cap of 2 rows was already filled by stronger, place-specific rows.
- https://ans-names.pitt.edu/ans/article/download/1140/1139/2282 (Thomas E. Murray, 1986, "Folk Etymology in the Streets of St. Louis", Names 34.4, CC BY 4.0; opened 2026-10-23, fetched as PDF, 3751 words). It is relevant to street names, for example Bellefontaine to Bell Fountain and Gnaw Bone from Narbonne. Rejected for two reasons. First, its candidate sentences break across hyphenated PDF lines ("corrup-/tion"), which risks LOCATE, and the Gnaw Bone sentence has no NAMING-PLACE window, by my reading; I did not run rowcheck on it. Second, the seat cap of 2 rows. It is a usable lead for a street-names seat.

I opened 4 sources against a guide of 1 to 3. The two rejected pages were opened to compare before choosing.

Scratch files: /fast/scratch/hyaku/kotodama-r58/ScoutFolkEtymology/ (rows.md, drafts.md, dump.py, page text dumps). I started no background processes; every process I ran has exited.

installs: none.
