# Round 61 lesson — footwear entry (claim C) and the cited-line lint (claim O)

Round 61, hyaku phase 4, attempt 1, L1 `KotodamaR61`. Lane base `942abdf4`. Instruments revision 0 `106df397` (dry-run receipt `78ad4b17`); revision 1 and freeze `2f4f8a40`, forced by the pre-data control wave; O landed `675d59af`; C landed `efbee29c` (measured revision). Receipt: `reports/round-61/telemetry/final-measures.txt` — **ACCEPT-C-61: FAIL** (LOCATE 40/41: S671), **ACCEPT-O-61: PASS**.

Anti-loop: rounds 58-60 failed on blind support of multi-row and lead-in packets in the amulets entry. This round did not re-enter that entry and ran no blind support leg as a predicate. C opened a new frontier area (footwear; 0 filename and 0 topic-line owners at base) under mechanical legs that read one row per line; O shipped the R60-M6 lint as a tool. The one-row one-clause support review of S652-S692 runs as review-only wave 2.

## Spot-check intake (round-60 outside verifier, `corpus/lessons/round-60-verifier-spotcheck.md` §5)

| item | route | status |
|---|---|---|
| 1 void breakdown | correction below and in LOG/SCORECARD: 5 `bash-cwd-outside-sandbox` (A, P, Q, R, V), 4 `deny:chr(` (D, F, L, W), 1 `kotodama` BLIND (S), 1 bare X2 with no verdicts (U; `grep -c '^VERDICT ' .ufo/waves/round-60/support/SupportU60.md` → 0) | done |
| 2 SupportX60 counted | correction below; X60 was qualified and its S646 NOT-SUPPORTED counted. Round 61 ran no blind-support counter, so no CONFINED-invisible breach rule was needed; the question carries to the next blind-support predicate | done (carried) |
| 3 pypdf record | correction below: seven seats disclosed `pypdf==5.4.0` via `uv run --with`, not two (and not the spot-check's five): RescoreMechA3:13, MutEvidenceA3:94, CtlNarrowA3:617, CtlGenericA3:583, CtlKeyedLabelA3:439, plus AuditA3R15:95 and CtlRubberStampA3:149 | done |
| 4 report structure | the round-61 report carries `## Gate`; erratum below for "five pre-data controls" and revision 5; mistake R61-M2 | done |
| 5 R60-M6 precision | correction below: the S612 packet joined entry lines 69, 95 and 120 (`reports/round-60/build-packets.py:50-52`; `packet-SupportD60.md` P05) | done |
| 6 registry teaches cells | S646 joins S601, S608, S614, S624, S636, S640, S641 as superseding-row candidates; the finding is SupportB60 **P01** (committed `planted-key.json` maps P01→S646 and P07→PLANTED), not P07 as the spot-check says. No superseding row was written this round | recorded, carried |
| 7 counter-input pinning | any re-run of round-60 `accept-d.py` must read the committed session copies; recorded here and in LOG | recorded |

## Corrections to the round-60 report (the filed report is not rewritten)

Drafted by ScribeR60Repairs (`.ufo/waves/round-61/w1/ScribeR60Repairs.md`), figures re-checked by the L1.

- The report has no `## Gate` heading; its line-55 discernment text and line-57 "Real rejects" paragraph sit under `## SHONEN`. The Gate content is in `corpus/lessons/round-60.md` `## Gate`.
- Line 46's "five pre-data controls" is superseded by line 55: three controls met earlier counters (CtlNarrowA3, CtlKeyedLabelA3, MutEvidenceA3) and RescoreConfineA3 found an evasion. Revision 5 was forced by the L1's own review (`reports/round-60/claims.json` `revision_note_5`), not by a control receipt; line 10 overstates it.
- The 11 unqualified seats: 5 `bash-cwd-outside-sandbox`, 4 `deny:chr(`, 1 `kotodama`, 1 bare X2 (SupportU60, no verdicts). "5 `deny:chr(`" and "11 voided by CONFINED" are wrong, and R60-M7's evidence cell repeats them. SupportX60 was qualified and counted, not voided, despite its self-reported `multi_tool_use.parallel` breach.
- pypdf 5.4.0 through `uv run --with`: seven seats (list above), not the two named on report line 66.
- R60-M6: the S612 packet joined lines 69, 95 and 120, not line 95 alone.
- S646 over-reach ("at their own altars" vs the page's "in their own temples") is SupportB60 P01.

## Pre-data control wave and revision 1

Wave 1 (36 seats, `.ufo/waves/round-61/w1/`, policy v1) scored revision 0 before any data. Each control that met revision 0 forced one change in revision 1 (`2f4f8a40`); the L1 re-scored the met fixtures on revision 1 (`reports/round-61/telemetry/controls-c-rescore.txt`, `controls-o-rescore.txt`):

- CtlCJunkLines (lorem lines with three scattered quote words) → LINK requires a restatement: ≥5 content words, ≥3 distinct quote words, ≥max(4, 0.4×content) in quote order. The 0.4 share was calibrated on honest control fixtures only (0.6 failed CtlCJunkLines fixture A line 5; 0.5 failed CtlCHonestPdf lines 18 and 20).
- CtlCOffTopic (homonyms: `sole` = only, `boot` = start-up and car trunk) → TOPIC splits strong and homonym-prone words; `clog(s)` moved to strong after it failed CtlCHonestPdf S664.
- CtlCMultiId (`S 653`, fullwidth `Ｓ653`) → ids read after NFKC, spaced ids counted.
- CtlCCopiedRows (`?ref=x`, `#fragment`) → FRESH ignores query, fragment, `m.`/`mobile.`.
- CtlCEchoUrls (httpbingo.org base64 and split-query echoes) and MutCounterC (a 127.0.0.1 document) → the locator denies more echo hosts, base64 or scattered quote words in the URL, and loopback/private hosts.
- CtlOSelftest, CtlOKeyed (a2, c), CtlOHonest (fake `selftest 10/10`; counter imported through a run-time path) → the selftest clause left O's statement; INDEP names `round-61` too and every leg runs a copy of the tool outside the lane.
- CtlOParsing (g) (boundary-blind regex) → lookalike lines carry a real id beside lookalikes of a second id.
- CtlODoNothing (no-args exit 0 survived) → ERR adds no arguments.
- NONE-MET on revision 0: CtlCDoNothing, CtlCSourceless, CtlCFabricated, CtlCHonestHtml (honest positive PASS under the FLOOR probe), CtlCHonestPdf (honest 24-row fixture PASS), MutCounterO (6/6 killed).
- Met and kept as declared residuals (`claims.json` `known_residuals_after_controls`): CtlCQuoteDump (compressed quotes), CtlCNoReader (in-order quote-word sampling) — both still had to open real on-topic sources; a heel homonym; a public self-made page. CtlOKeyed a2 and the fake-selftest fixture still pass revision 1 because their parsers are correct.

## Gate

New rows opened this round (accessed 2026-10-23 by the wave-1 scribes ScribeSrc01-10; each quote LOCATED live by `reports/round-61/reopen-quote.py` in the scribe report; three rows re-located by the L1 after its pre-landing edits: S652 (DOI URL replacing a query URL that FRESH's query strip collides with S005), S660 and S662 (quotes trimmed to ≤25 words, contiguous spans)):

- S652 | https://doi.org/10.1371/journal.pone.0010984 | 2026-10-23 | "The shoe was stuffed with loose, unfastened grass (Poaceae) without clear orientation."
- S653 | https://mnch.uoregon.edu/collections-galleries/great-basin-sandals | 2026-10-23 | "well-preserved sandals woven from sagebrush bark and other fibers"
- S654 | https://www.oregonencyclopedia.org/articles/fort_rock_sandals/ | 2026-10-23 | "The tie system involves a series of interlocking loops fixed to the edge of the sole near the heel."
- S655 | https://www.iceman.it/en/news/new-reconstruction-of-the-iceman-s-shoes-and-coat_440 | 2026-10-23 | "To keep his feet warm in the snow the Iceman also stuffed his shoes with hay."
- S656 | https://exarc.net/issue-2023-2/at/reconstructing-otzis-shoes | 2026-10-23 | "The shoes consist of a bearskin sole, deerskin upper leather attached to the sole with a thin cow hide strap."
- S657 | https://www.vindolanda.com/blog/the-curators-favourite-shoes | 2026-10-23 | "The iron studs on any Roman shoe are there as a way of holding the numerous layers of leather which make up the sole together"
- S658 | https://www.vindolanda.com/news/magna-shoes | 2026-10-23 | "The collection includes tiny baby booties, elaborate summer sandals and marching boots"
- S659 | https://collections.vam.ac.uk/item/O74164/ | 2026-10-23 | "This is part of a poulaine, a type of medieval man’s shoe with a long pointed toe"
- S660 | https://www.londonmuseum.org.uk/collections/london-stories/pointy-shoes-sexuality-medieval-london/ | 2026-10-23 | "sumptuary laws (laws governing dress and behaviour) which set out regulations for how long somebody's poulaines could be based on their station"
- S661 | https://collections.vam.ac.uk/item/O74447/pair-of-chopines-unknown/ | 2026-10-23 | "Chopines were completely hidden under skirts. The higher the footwear the more cloth was required for the dress, another indication of status."
- S662 | https://www.metmuseum.org/essays/the-chopine | 2026-10-23 | "especially popular among Venetian women, the high-platformed shoe called the chopine had both a practical and symbolic function."
- S663 | https://hue.fitnyc.edu/fit-museum/ | 2026-10-23 | "The red heels and soles of these latchet shoes are associated with Louis XIV and his court."
- S664 | https://tidsskrift.dk/atr/article/download/167035/208065 | 2026-10-23 | "King Louis XIV of France often wore shoes with red heels and soles, and by regulation made them the preserve of the nobility,"
- S665 | https://batashoemuseum.ca/standing-tall/ | 2026-10-23 | "The heel was not a European invention, instead it originated in Western Asia centuries ago for horseback riding"
- S666 | https://www.bbc.co.uk/programmes/articles/qsXBljJrnRm60Gdt2PR362/six-surprising-facts-about-the-history-of-high-heeled-shoes | 2026-10-23 | "The earliest evidence we have of someone wearing heels is from a 10th-century Persian bowl."
- S667 | https://jpsearch.go.jp/en/gallery/ndl-GZqzDNvVK0a | 2026-10-23 | "Traditional Japanese footwear can be roughly divided into two groups: zori sandals and geta wooden clogs."
- S668 | https://www.sfomuseum.org/exhibitions/stepping-out-shoes-world-cultures/gallery | 2026-10-23 | "Similar to the zori but elevated in height, geta became fashionable in urban areas during the Edo period (1615–1868)."
- S669 | https://www.nippon.com/en/guide-to-japan/gu020004/ | 2026-10-23 | "Japanese custom of removing footwear before entering a home. The same applies to ryokan inns, temples, and even restaurants with tatami-floored rooms"
- S670 | https://vmm.mcb.org.uk/visiting-a-mosque-guide | 2026-10-23 | "You'll be asked to remove your shoes before entering the prayer hall"
- S671 | https://americanindian.si.edu/collections-search/object/NMAI_26904 | 2026-10-23 | "Object Name Moccasins Media/Materials Elk hide/skin, hide thong/babiche, paint Techniques Sewn, painted"
- S672 | https://www.historymuseum.ca/cmc/exhibitions/aborig/mocasin/mocintre.html | 2026-10-23 | "The moccasin, the Aboriginal footwear of the Northern Plains, is no different: it is also both practical and stylish"
- S673 | https://www.musee-mccord-stewart.ca/en/collections/indigenous-cultures/ | 2026-10-23 | "Moccasins, Nêhiyawak, 1920. Gift of the Art Association of Montreal, ME928.8.1-2"
- S674 | https://www.nwttimeline.ca/stories/2500-year-old-kamik-boot/ | 2026-10-23 | "Made over 2,500 years ago, this child’s boot or kamik is one of the oldest examples of footwear found in the Canadian Arctic."
- S675 | https://collections.vam.ac.uk/item/O89378/pair-of-shoes-unknown/ | 2026-10-23 | "The shoes are made for bound feet. The shoes are embroidered with a peach blossom motif."
- S676 | https://batashoemuseum.ca/timeline/every-step-a-lotus/ | 2026-10-23 | "Shoes in the Lives of Women in Late Imperial China, curated by Dr. Dorothy Ko was one of our most popular exhibitions"
- S677 | https://collections.vam.ac.uk/item/O232311/sandal-unknown/ | 2026-10-23 | "The epitome of luxury, these ornately worked toe-knob sandals, known as paduka, were one of the many often extravagant presents a bride might receive."
- S678 | https://collections.vam.ac.uk/item/O482201/ritual-object/ | 2026-10-23 | "These also have the knobs of sandals (paduka) protruding between the toes."
- S679 | https://etnografskimuzej.rs/en/zbirka/crafts/ | 2026-10-23 | "an opančar workshop (for making opanci—traditional leather footwear)"
- S680 | https://cplorg.contentdm.oclc.org/digital/api/singleitem/collection/p4014coll10/id/836 | 2026-10-23 | "A pair of leather shoes, their soles are attached to the uppers with knotted leather thongs."
- S681 | http://news.bbc.co.uk/2/hi/middle_east/7783325.stm | 2026-10-23 | "In Arab culture it's considered rude even to display the sole of one's shoe to a fellow human being."
- S682 | https://aasjournal.spbu.ru/article/download/20521/12582/76573 | 2026-10-23 | "For instance, a deliberate demonstration of the soles of shoes is considered indecent in Arab society;"
- S683 | https://polotsk-local.museum.by/en/node/45054 | 2026-10-23 | "Traditional type of peasant shoes were bast shoes. They are woven from vine or linden bast (soft bark)."
- S684 | https://collections.readingmuseum.org.uk/index.asp?page=record&mwsquery=%7Btotopic%7D=%7BWorld%20Collection:%20Ornamentation%7D&filename=REDMG&hitsStart=156 | 2026-10-23 | "Shoes made from woven birch bark are found throughout Scandinavia, Siberia, and the Baltics. In Russia they are known as 'lapti' shoes."
- S685 | https://www.londonmuseum.org.uk/collections/v/object-731922/wood-worked-wood-patten/ | 2026-10-23 | "Wooden patten. This was a type of overshoe worn to raise the foot above ground during wet weather."
- S686 | https://www.museum.ie/collections/collection/antiquity-68544/ | 2026-10-23 | "This piece of footwear is a patten. It is one of a pair (1945:61.2). These were worn over a pair of normal shoes."
- S687 | https://www.theoi.com/Olympios/HermesTreasures.html | 2026-10-23 | "Hermes wore winged, short leather boots called by the Greeks pteroeis pedila and by the Romans talaria."
- S688 | https://penelope.uchicago.edu/Thayer/E/Roman/Texts/secondary/SMIGRA*/Talaria.html | 2026-10-23 | "commonly done by representing him with sandals, which have wings fastened to them on each side over the ancles."
- S689 | https://www.museum.nl/en/internationaal-klompenmuseum | 2026-10-23 | "Aside from the large collection of wooden shoes, discover the craft of clogmaking, for example through the specialized machinery dating from 1920."
- S690 | https://www.zaanseschans.com/en/wooden-shoe-workshop-de-zaanse-schans/ | 2026-10-23 | "such as beautiful bridal clogs, work clogs and the famous church clogs from Hindeloopen, dating all the way back to 1675"
- S691 | https://www.wordorigins.org/big-list-entries/sabotage | 2026-10-23 | "borrowing from French, and that borrowing occurred in the opening years of the twentieth century. The root, sabot, literally means a wooden shoe or clog."
- S692 | https://www.dictionary.com/browse/sabot | 2026-10-23 | "a shoe made of a single block of wood hollowed out, worn especially by farmers and workers in the Netherlands, France, Belgium, etc."

Rejected or not registered this round (real rejects with reasons):

- Bata Shoe Museum "Art & Innovation: Traditional Arctic Footwear" quote "Traditional designs are geometric but more contemporary boots feature highly curvilinear patterns." (ScribeSrc07 draft 2) — not registered: its only lexicon word is the homonym-prone `boots` with no second footwear or context word (TOPIC revision 1), and its clause had 4 content words (LINK minimum 5). Re-test: `build.py` self-check output `['TOPIC', 'LINK shared=4 content=4 ordered=4']`.
- Web Japan Nipponia page (ScribeSrc05): HTTP 403 on ordinary fetch; not used, no bypass.
- Smithsonian `si.edu/object/pair-shoes-bound-feet:nmnhanthropology_8428831` (ScribeSrc07): HTTP 403, no Wayback capture; not used.
- UBC Museum of Anthropology `kamiik` record (ScribeSrc07): the locator refused its query-bearing `/search/item` URL (`search-url`).
- Ancient Egyptian sandals (ScribeSrc02): no locatable source found in the box; none registered.

## Status and used-by change log

- S652-S692: new rows, status `mined`, opened 2026-10-23, used-by `corpus/knowledge/culture-material/footwear-codes-terminology.md` (no prior state).
- No existing row's status, recheck or used-by cell changed.

## Mistakes

| id | class | evidence | captured-by | fix (shown able to fail) |
|---|---|---|---|---|
| R61-M1 | report figures not re-derived from the committed receipt | `.ufo/reports/round-60/kotodama.md:14,46,61,66`; spot-check §1 | none | derive report counts from the receipt files before filing (the round-61 report quotes `final-measures.txt` lines verbatim); witness: ScribeMistakes W2-W4 fail on the round-60 report |
| R61-M2 | required report heading missing | `.ufo/reports/round-60/kotodama.md:48-59` | none | `grep -c '^## Gate' <report>` must print 1 before filing; prints 0 on the round-60 report |
| R61-M3 | cited clauses joined across ids and table cells (R60-M6) | `corpus/lessons/round-60.md:56` | none before this round | claim O: `tools/check-cited-lines.py`; QUALITY criterion 15; exit 1 on the amulets entry (line 95 S612,S613), exit 0 on the footwear entry |
| R61-M4 | a no-slack live leg turned one transient archive error into a claim miss (second time after R58) | `reports/round-61/telemetry/final-measures.txt` LOCATE: S671 live URL 403 (structural bot block) and its only capture erred at 09:58Z; the same capture LOCATED on a diagnostic `reopen-quote.py --row S671` run about two minutes later while the live URL still answered 403 (a locator run, not a counter run; verdict unchanged) | QUALITY 13 asks for a capture, not for a second independent working URL | before landing, replay the locator on every row and drop or re-source any row whose live URL is blocked and whose only fallback is one capture; next predicate with a live leg declares a bounded transient-error allowance with its own control (criterion 13's second option) |
| R61-M5 | seat misroot into the fleet root | ScribeSrc01 wrote `/home/vgpnk/Projects/shokunin/.ufo/waves/round-61/w1/ScribeSrc01.md`; moved byte-exact (`cmp` 0) to the lane path and the fleet copy deleted | the wave context's absolute-path rule (not followed by one seat) | keep the rule; the L1 misroot sweep caught it |
| R61-M6 | wave sized above the gate's free seats | wave 1 asked for 42 seats while `live_estimate` was 62 of cap 100: the acquire waited 3600 s and timed out; re-sized to 36 genuine items it was granted at 09:40Z | none | read `wave-slot.sh status` before sizing; size to the free seats, never pad |
| R61-M7 | registry vocabulary repeat (R58-M6) | census end run 1: `E05 S655 kind=news`, `E05 S658 kind=news`, `E05 S681 kind=news`, exit 1 (`reports/round-61/telemetry/census-end.txt`, run 1 kept) | the census E05 check (worked); R58-M6's fix (wave contexts name the kind enum) was not carried into the round-61 wave-1 context | the three kind cells of rows added this round, report not yet filed, corrected to `docs` (R58 precedent; no counter reads the kind cell: accept-c.py reads cells 1, 2, 6, 8, 9, 11); census run 2 exit 0; wave contexts name the enum `spec docs paper code tool dataset talk book community own-work` |

## Known defects routed to round 62

- S687 (Theoi, tier C) is the sole support of its entry line ("Hermes' talaria were winged leather boots"); QUALITY says a tier-C row is a lead, never sole support for an admitted claim (census `W01 S687 tierC mined`). The entry is not admitted (C missed); round 62 re-sources that line with an A/B row or removes it under its own claim.
- Separability (`reports/round-61/telemetry/separability.txt`): one finding, `O->C via export` — the regex of C's id block matches the literal `S652` in the tool's selftest case at `tools/check-cited-lines.py:152` (a fixture id, not a citation). O's acceptance needs no C land (the dynamic leg found no O dependency). The same check re-ran C's acceptance in a temporary copy at 10:02Z and produced no `C-><base>` finding, so LOCATE succeeded there; that later run is a dependency check, not the claim receipt, and the frozen kill rule keeps C MISSED on the first run.
- QUALITY criterion 13 gap shown by R61-M4: a capture is not a second independent source of availability; the next live-leg predicate declares a bounded transient-error allowance with its own control before data.

## Outcome

ACCEPT-C-61 FAIL on LOCATE alone (13 of 14 legs PASS; 41 cited rows, 40 located). Per the frozen kill rule claim C is **MISSED**: nothing is amended, no row is removed, and the counter is not re-run to look for a pass. ACCEPT-O-61 PASS (all six legs). The entry and its 41 rows stay as landed; the one-row one-clause support review (wave 2) is review-only.
