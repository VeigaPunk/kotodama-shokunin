# ScoutUnescoMbanzaKongo — the UNESCO inscription of Mbanza Kongo and the ICOMOS evaluation

- seat: `KotodamaR56.ScoutUnescoMbanzaKongo` (scout, claim C ground: Kingdom of Kongo civilization entry)
- round: kotodama 56 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, declaration `b4b7db91a38447bb2c07b0ef436fc9654dcec89c`, claim base `052f145cbcff6996c153d460d81ce346ce74bfbc`
- assignment: one or two opened sources on the UNESCO listing of Mbanza Kongo (property 1511): the official list page and its Statement of Outstanding Universal Value, plus the ICOMOS evaluation; quote what the inscription says about the capital, its Christian buildings and the kingship
- draft ids used below: `NEW-ScoutUnescoMbanzaKongo-1` and `-2`; the L1 assigns the final `S` ids from the reserved block S359–S418 at integration

## Route summary

Access date for every file below: 2026-10-22. All reading was done with plain `curl` and local text
extraction (`pdftotext`), no browser automation, no archive needed.

| file | URL | status | bytes |
|---|---|---|---|
| list page, property 1511 (carries the full OUV inline) | `https://whc.unesco.org/en/list/1511/` | direct GET with a standard desktop User-Agent string, HTTP 200, `text/html;charset=UTF-8` | 142656 |
| documents tab for 1511 (document ids) | `https://whc.unesco.org/en/list/1511/documents/` | direct GET, HTTP 200 | 126497 |
| decision 41COM 8B.10 (same OUV text as annex) | `https://whc.unesco.org/en/decisions/6882` | direct GET, HTTP 200 | 130687 |
| ICOMOS evaluation, document 159705 | `https://whc.unesco.org/document/159705` | direct GET, HTTP 200, `application/pdf` | 3492278 |

Disclosure on the list page: the first plain `curl` request without a User-Agent returned an HTTP 403
Cloudflare interstitial page (title "Just a moment…"). The identical ordinary GET with a standard desktop
User-Agent header returned HTTP 200 and the public page. No browser automation and no challenge solver was
used; challenge met, not passed. The PDF and decision pages answered the same ordinary GET directly.

Page shape of the ICOMOS PDF: 15 pages, printed pp. 33–47, two columns per page. Quotations below were
checked by exact substring against the PDF text layer extracted per page; two passages that straddle a
column or page break are quoted only in their contiguous part, and that is noted where it happens.

---

### NEW-ScoutUnescoMbanzaKongo-1

citation: UNESCO World Heritage Centre, 2017. "Mbanza Kongo, Vestiges of the Capital of the former Kingdom of Kongo" (Angola), World Heritage List, property/dossier 1511, inscribed 2017 on criteria (iii)(iv), with the property's Statement of Outstanding Universal Value published on the list page. The same OUV text is the annex to decision 41COM 8B.10 (41st session, Krakow).

url: https://whc.unesco.org/en/list/1511/

route: direct GET with a standard desktop User-Agent string, HTTP 200, `text/html`, 142656 bytes, page and its OUV section read in full this session, 2026-10-22; the first request without a User-Agent met a Cloudflare interstitial (HTTP 403) and was not pursued further, and the same OUV paragraphs were confirmed against `https://whc.unesco.org/en/decisions/6882` (HTTP 200).

kind: record

tier: A — UNESCO is the author of the inscription and of this OUV wording, so it is authoritative for exactly this scope; it is not a primary source for Kongo history.

scope: what the 2017 inscription states the property is and means — the capital's political and spiritual role, the two building fabrics, the wording of criteria (iii) and (iv), the authenticity and continuity statements, and the property facts on the page (89.29 ha, buffer zone 622.16 ha, criteria (iii)(iv), 2017). Says nothing about the kingdom's internal offices, titles, economy, kinship or language beyond the phrases quoted, and gives no Kikongo gloss.

quotes:
- Brief synthesis, sentence 1: "one of the largest constituted states of Southern Africa, which was active from the 14th to the 19th century"
- Brief synthesis, sentence 3: "the Portuguese added and substituted stone buildings constructed in accordance with European construction methods, including several churches"
- Criterion (iii), sentence 2: "Its capital has retained the ritual and symbolic powers embodied in the brotherhood of the Leopard Ngo."
- Criterion (iii), sentence 3: "After the arrival of the Portuguese, the Kingdom adopted Christianity, while however retaining elements of pre-existing Kongo customs."

teaches: The inscription's own wording on the Kongo capital: its scale among Southern African states, Christian adoption with retained custom, and ritual power held by the Leopard Ngo brotherhood.

draft sentences:
- Choose your century before furnishing the capital, because the inscription dates the kingdom's active life from the 14th to the 19th century, so one scene cannot show both an uncontacted court and a cathedral chapter as if they were the same moment (NEW-ScoutUnescoMbanzaKongo-1, Brief synthesis, sentence 1).
- Build the capital in two fabrics and say who built which: the inscription has the Portuguese adding and substituting stone buildings on a large town already built in local materials, so stone marks the newcomer quarter rather than the whole city (NEW-ScoutUnescoMbanzaKongo-1, Brief synthesis, sentence 3).
- Put some ritual authority in a corporate body beside the king, since the inscription credits the capital's retained ritual and symbolic powers to the brotherhood of the Leopard Ngo rather than to the throne alone (NEW-ScoutUnescoMbanzaKongo-1, Criterion (iii), sentence 2).
- Treat Kongo Christianity as an adoption that kept its own customs, not as a veneer or a clean rupture, because the inscription says the kingdom adopted Christianity while retaining elements of pre-existing Kongo custom (NEW-ScoutUnescoMbanzaKongo-1, Criterion (iii), sentence 3).
- Carry one office across the colonial rupture: the inscription records a customary court reinstated after four decades of war and a royal space still free of encroachment, which lets a modern scene keep a precolonial institution alive (NEW-ScoutUnescoMbanzaKongo-1, Authenticity, sentence 2).
- Do not put the slave trade on stage at the capital on this evidence: the same OUV says no material vestige attesting to it has been found at the property, so trade is a fact of the kingdom's coasts and documents, not of this plateau (NEW-ScoutUnescoMbanzaKongo-1, Brief synthesis, sentence 7).

---

### NEW-ScoutUnescoMbanzaKongo-2

citation: ICOMOS, 2017. "Mbanza Kongo, vestiges of the capital of the former Kingdom of Kongo" (Angola), No 1511, advisory body evaluation, approved 10 March 2017, published by the UNESCO World Heritage Centre as document 159705 for the 41st session of the World Heritage Committee (Krakow, 2017). Author not named on the cover; the report is ICOMOS's institutional text.

url: https://whc.unesco.org/document/159705

route: direct GET (plain request, PDF 3492278 bytes, HTTP 200, `application/pdf`), text layer extracted with `pdftotext`, pp. 33–43 read this session, 2026-10-22

kind: record

tier: A — the advisory body's own evaluation of this property, authoritative for what the property contains and for which claims ICOMOS accepted and rejected; its historical summary is a synthesis, so it is B-level for Kongo history in general.

scope: ICOMOS's account of the property and its assessment of the nomination — the Kikongo place-name glosses, the layout of the royal core, the nzimbu shell currency, provincial governors, the dated sequence 1482–1957, the Jesuit college, the criteria ICOMOS accepted and rejected, and the evaluation's own cautions about evidence. Not a chronicle and not a source for kings' succession rules, titles at court or kinship.

quotes:
- p. 34, History and development: "at this time it was already known as Kulumbimbi, from Nkulu"
- p. 35, History and development (continuation of the same gloss from p. 34): "“dangerous place”"
- p. 35, History and development: "the royal house was located within a fence with a circumference of 1000 metres"
- p. 35, History and development: "a public square (Mbazi) where justice was delivered, ceremonies were held and troops were reviewed"

teaches: The evaluation's reading of the royal core: a fenced royal house ringed by dignitaries' dwellings around a judicial and ceremonial square, in a town whose name glosses ancestor and danger.

draft sentences:
- Gloss your capital's names rather than translating them flatly: the evaluation derives Kulumbimbi from Nkulu, ancestor, and Mbimbi, dangerous place, so one toponym can carry both a burial claim and a warning (NEW-ScoutUnescoMbanzaKongo-2, p. 34, History and development).
- Draw the royal core as a fenced enclosure with the dignitaries' houses ranked around it and one public square, Mbazi, where justice, ceremony and troop review happen in the same open ground (NEW-ScoutUnescoMbanzaKongo-2, p. 35, History and development).
- Give the treasury a single shell unit, the nzimbu, and let a power structure control it, since the evaluation grounds the kingdom's prosperity in that stable monetary system and names no coin (NEW-ScoutUnescoMbanzaKongo-2, p. 35, History and development).
- Staff the provinces with named governors, because the evaluation says the territory was divided into provinces each with a governor, which supplies a rank between the king and a district chief (NEW-ScoutUnescoMbanzaKongo-2, p. 35, History and development).
- Track two names for each sovereign: the king Nzinga Nkuwu took the name Joao I at his 1491 conversion while keeping traditional practices, so a baptismal name is a title event layered on the Kikongo name, not a replacement (NEW-ScoutUnescoMbanzaKongo-2, p. 35, History and development).
- Keep the capital off the slave market: ICOMOS writes that it is not even known whether enslaved people were brought to Mbanza Kongo rather than collected elsewhere in the kingdom, so a slave yard at the palace is an invention (NEW-ScoutUnescoMbanzaKongo-2, p. 36, Justification of Outstanding Universal Value).

---

## Further quotations, verified and opened, not placed in the two rows

These are exact substrings of the same opened files, offered so the L1 can swap a quote into either row
without reopening anything. Locators as in the rows above.

UNESCO list page (same URL as row 1):
- Brief synthesis, sentence 1: "the political and spiritual capital of the Kingdom of Kongo"
- Brief synthesis, sentence 4: "The town then experienced the expansion of Christianity with the Westernisation of the local elites, without however renouncing its culture."
- Brief synthesis, sentence 7: "No material vestige attesting to the slave trade has been found up to now."
- Criterion (iv), sentence 2: "The Cathedral was standing when in 1608, the Pope accredited in Rome the first ambassador of a sub-Saharan African state to the Vatican."
- Criterion (iv), sentence 3: "the place where in 1624 the first catechism was written in the Kikongo language"
- Criterion (iv), sentence 3: "The Jesuit College reflects the status given to Mbanza Kongo as a seat of learning"
- Authenticity, sentence 2: "the customary court, which manages conflicts, has been reinstated after four decades of war"
- Authenticity, sentence 5: "it is quite remarkable that the passing of centuries has not led to any encroachment on the royal space"
- Protection and management requirements, sentence 7: "Conservation and restoration measures, particularly for the former cathedral (Kulumbimbi)"

ICOMOS evaluation (same URL as row 2):
- p. 34, Description: "Nearby are the House of the king’s secretary and the Precinct of the Sacred Tree (Yala Nkuwu), in whose shade the sovereigns delivered justice."
- p. 34, Description: "Sungilu and Mpindi a Tadi (“stone signal”) are places linked to the funeral ceremonies of the kings."
- p. 34, Description: "the typical 19th-20th century Kongo house (Nzo)"
- p. 34, Description: "the cemetery of the sovereigns is located within its bounds"
- p. 34, Description: "the first episcopal seat in Africa south of the Equator"
- p. 34, History and development: "Mbanza Kongo is believed to have been founded in the 13th century"
- p. 34, History and development: "On the plateau, a sacred wood was the space used for traditional ritual ceremonies and the site of the royal cemetery"
- p. 35, History and development: "The site was defended by a palisade."
- p. 35, History and development: "In the south of the area marked out by the twelve springs"
- p. 35, History and development: "divided into provinces, each of which had a governor"
- p. 35, History and development: "the unit of currency was a shell, the nzimbu"
- p. 35, History and development: "between the 16th and 17th centuries, twelve churches"
- p. 35, History and development: "The Cathedral of the Holy Saviour was consecrated in 1596"
- p. 35, History and development: "In 1518, Pope Leo X appointed Don Enrique, son of the king Afonso I, bishop of Utica"
- p. 35, History and development: "Weakened, Mbanza Kongo was invaded in 1568 by the Jagas, a neighbouring people"
- p. 35, History and development: "Several texts were enacted by sovereigns from the early 16th century onwards to prevent the rise of the slave trade"
- p. 35, History and development: "the Kongo king, Antonio I (Nvita Nkanga), was defeated and killed by them at the Battle of Ambuila in 1665"
- p. 35, History and development: "a symbolic authority that was perpetuated right up to the death of the last sovereign, Antonio III, in 1957"
- p. 36, Justification of Outstanding Universal Value: "its main structures (royal palaces, churches, tombs, sacred tree, excavated shelters)"
- p. 38, Criterion (iv): "A Jesuit college with a library was founded in 1621 and operated until 1678"
- p. 38, Criterion (iv): "This criterion was not put forward by the State Party but was considered by ICOMOS to be appropriate."
- p. 38, Criterion (v): "the drawing of Mbanza Kongo made by the Dutch traveller Olfert Dapper, in his Description of Africa (1668)"
- p. 38, Criterion (v): "what is being nominated is only the core of the city and not the overall urban settlement on its promontory"
- p. 38, Criterion (vi): "no vestiges attesting to the slave trade have been found within the bounds of the nominated property"

## Map of names the two sources carry

Only what these two files say; the gloss column quotes the source's own gloss.

| term | what it names | source and locator | design use |
|---|---|---|---|
| Mbanza Kongo | the town, political and spiritual capital | row 1, Brief synthesis | the capital's plain name; neither source glosses the word itself |
| Kulumbimbi | the site/name of the royal cemetery area, later the first cathedral | row 2, p. 34, History and development; row 1, Protection and management requirements | a name that migrates from burial ground to cathedral |
| Nkulu | glossed "ancestor" | row 2, p. 34, History and development | naming element for ancestry |
| Mbimbi | glossed "dangerous place" | row 2, p. 35, History and development | naming element for danger |
| Lumbu ("residence") | area of the old royal palace, still the political and spiritual area | row 2, p. 34, Description | palace quarter |
| Yala Nkuwu, Precinct of the Sacred Tree | tree whose shade is where sovereigns delivered justice | row 2, p. 34, Description | a court of law under a tree, near the king's secretary's house |
| Mbazi | public square for justice, ceremonies and troop review | row 2, p. 35, History and development | one square, three functions |
| Mbanzi a Nkanu | the present-day customary court | row 2, p. 34, Description | continuity office, not a re-enactment |
| Nzo | the 19th-20th century Kongo house type | row 2, p. 34, Description | ordinary dwelling, long house with two main rooms |
| Sungilu; Mpindi a Tadi ("stone signal") | places of the kings' funeral rites — washing of the body, embalming | row 2, p. 34, Description | funerary topography, two named stations |
| Tadi dya Bukikwa | "inverted stone" or "that which has not yet revealed its contents"; probably the Jesuit college | row 2, p. 34, Description | a place name that also encodes an unexcavated secret |
| nzimbu | the shell unit of currency | row 2, p. 35, History and development | money as shells under political control |
| Leopard Ngo | the brotherhood in which the capital's ritual and symbolic powers are embodied | row 1, Criterion (iii) | ritual authority as a body, with no grades or offices given by either source |
| Jagas | a neighbouring people who invaded in 1568 | row 2, p. 35, History and development | the external shock between the first Christian kings and the rebuilt town |
| São Salvador | the town's name after 1596 | row 2, p. 35, History and development | the Portuguese name a worldbuilder may need for later scenes |

## Period sequence as the two sources date it

- 13th century, "believed" (row 2, p. 34): founding on a defensible plateau; a sacred wood for ritual and the royal cemetery; the place already called Kulumbimbi.
- 14th–19th century: the kingdom's active life (row 1, Brief synthesis).
- 1482: the Portuguese reach the mouth of the Congo and compare the town with Evora (row 2, p. 35).
- 1491: Nzinga Nkuwu converts and takes the name Joao I, keeping traditional practices (row 2, p. 35).
- 1518: Dom Enrique, son of Afonso I, made bishop of Utica and apostolic vicar (row 2, p. 35).
- 1568–1571: the Jagas take and ruin the town (row 2, p. 34, Description, and p. 35).
- 1596: the Cathedral of the Holy Saviour consecrated; the town renamed São Salvador (row 2, p. 35).
- 1608: the first ambassador of a sub-Saharan African state accredited at Rome (row 1, Criterion (iv)).
- 1621–1678: the Jesuit college with its library operates (row 2, p. 38, Criterion (iv)).
- 1624: the first Kikongo catechism written, at the college (row 1, Criterion (iv); row 2, p. 35).
- 1645–1648: the Capuchins arrive (row 2, p. 34, Description).
- 1665: António I (Nvita Nkanga) defeated and killed at Ambuila (row 2, p. 35).
- 1668: Olfert Dapper's printed drawing of the town (row 2, p. 38, Criterion (v)).
- 1889, 1901, 1933 onward: Baptist sanctuary, new cathedral and new Royal Palace, Franciscan complex (row 2, p. 34, Description).
- 1957: death of the last sovereign, António III (row 2, p. 35).
- 2017: inscription on criteria (iii)(iv) (row 1, page facts).

## Findings, attacks and limits for the L1

1. **The capital-as-slave-port reading is contradicted by both files.** The OUV says the kingdom sat on the main route and then that no material vestige of the trade has been found on the property; ICOMOS adds that it is not even known whether enslaved people were brought to the town. Any entry sentence that places a slave market on the plateau must be dropped or attributed as the nomination's rhetoric that ICOMOS itself doubted.
2. **Criteria drift.** The State Party nominated on (iii), (v) and (vi); ICOMOS rejected (v) and (vi) and introduced (iv) itself. So the OUV's Criterion (iv) paragraphs are the advisory body's draft, later adopted, not the nominating state's argument; an entry that says "Kongo claimed X under criterion (vi)" would misattribute.
3. **The brotherhood is named, never described.** Row 1 gives the Leopard Ngo brotherhood the capital's retained ritual powers; row 2 repeats the claim as the State Party's, and separately mentions "the presence of the spirit Ngo" in a Kasubi comparison at p. 35. Neither file gives membership, grades, initiation or office names. Those must come from another seat's source or stay out of the entry.
4. **The property is a core, not the city.** ICOMOS states that only the city core is nominated, not the whole settlement on the promontory. A map built from the 89.29 ha boundary would under-draw the capital; use the described twelve springs, palisade and ring of dignitaries' houses as the settlement logic instead.
5. **Two dates for contact.** Row 1 dates the documentation "from 1483 to the present day" (five centuries) while row 2 narrates the Portuguese at the river mouth in 1482. Keep both, attributed, or write "1482–1483" for first contact and 1483 for the documentary series.
6. **Episcopal precision.** Kulumbimbi is called the first episcopal seat in Africa south of the Equator, while Dom Enrique in 1518 is bishop of Utica (a titular see) and apostolic vicar of Mbanza Kongo. Do not merge a titular appointment with a residential see; the entry can say the town held a vicariate and a cathedral without claiming a resident bishop in 1518.
7. **Spelling.** The PDF's text layer prints Portuguese names without diacritics ("Joao I", "Antonio I") and renders the new cathedral's name as "Conçeicão". Quote as printed; a worldbuilder's spelling of Kikongo names should come from a Kikongo source, not from this dossier.
8. **Overlap to avoid double counting.** `ScoutNzimbuMoney`, `ScoutMpuRegalia`, `ScoutKongoChristianity`, `ScoutKongoKingArchaeology`, `ScoutKongoEmbassies`, `ScoutMbwilaEras`, `ScoutDiogoCaoContact`, `ScoutDoutrinaCatechism` and `ScoutBrusciottoGrammar` seat the same facts from other sources. These two rows are the inscription's and the advisory body's framing, useful as the entry's period spine and as the official property facts, not as the depth source for money, regalia, liturgy or archaeology.
9. **Kikongo glosses reach only six terms here** (Nkulu, Mbimbi, Lumbu, Mbazi, Nzo, Tadi dya Bukikwa). Neither file glosses "mbanza" itself, "mani", "nkisi" or any court title. Do not derive those from the toponyms.

Tooling: no installs. `curl` and `pdftotext` (poppler) were already present; nothing in the lane was changed beyond this report.

unopened:
- Nomination text, `https://whc.unesco.org/document/159684` — listed on the documents tab, not opened: the ICOMOS evaluation and the OUV carried the assigned question, and the dossier is a large state-party PDF whose content is screened by the evaluation.
- Executive Summary, `https://whc.unesco.org/document/159688`, and Annexes, `https://whc.unesco.org/document/159689` — listed, not opened, same reason.
- Advisory Body Interim Report, `https://whc.unesco.org/document/159687` — listed, not opened; the final evaluation supersedes it.
- `https://whc.unesco.org/document/190295` — opened by GET (HTTP 200) and found to be an `image/jpeg`, a photograph, not a text document; not read as a source.
- "Official website page (in Portuguese only)", linked from the list page — link target not resolved or opened this session.
- The "Periodic Report Cycle 3" and state-of-conservation documents linked on the documents tab — not opened; outside the assigned question.

Tooling: no installs. `curl` and `pdftotext` (poppler) were already present; reports are plain files, no change to the lane beyond this report.
