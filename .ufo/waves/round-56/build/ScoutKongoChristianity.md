# ScoutKongoChristianity — claim C source report (Kongo Christianity as a Kongo institution)

- seat: `KotodamaR56.ScoutKongoChristianity` (scout, claim C ground: Kingdom of Kongo civilization entry)
- round: kotodama 56 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, declaration `b4b7db91a38447bb2c07b0ef436fc9654dcec89c`, claim base `052f145cbcff6996c153d460d81ce346ce74bfbc`
- assignment: one or two opened sources on Kongo Christianity as a Kongo institution — Thornton's 1984 article and Fromont's *The Art of Conversion* — quoting the thesis statements, aimed at worldbuilder decisions (what people, offices, objects and places were called; who held which title; what was worn, carried, paid or made; what changed between periods; where an outsider's record over-reads)
- draft ids used below: `NEW-ScoutKongoChristianity-1`, `-2`, `-3`; the L1 assigns final `S` ids from the reserved block S359–S418 at integration

## Result

Three rows were opened this session, covering two works:

1. Thornton 1984, *The Journal of African History* — only the publisher's article page and its extract (the free summary) were readable; the article body is closed access. This supports the argument and its sequence, not the article's evidence, names or dates.
2. Fromont 2017, *Anais do Museu Paulista* — full open-access article, 21 PDF pages, extracted in full with the argument, regalia and coronation sections read closely. This is the strongest row here: it names the regalia, the church office and the 1665–1696 succession problem.
3. Fromont 2014, *The Art of Conversion* — the UNC Press publisher page only (description and award lines). Tier B for the book's thesis; the book itself is not open.

No row here carries the Antonian movement, Kikongo grammar, minkisi, nzimbu currency or kinship terms. The entry needs other seats' rows for those. None of the three rows supports a claim about Dona Beatriz or Kimpa Vita: the Thornton extract does not mention her and I did not read the article body, so take that material from another row.

## Route summary

Access date for every file below: 2026-10-22. Reading was done with plain `curl` and local text extraction (`pdftotext`); no browser automation, no challenge solver, no login.

| file | URL actually read | status | bytes |
|---|---|---|---|
| Thornton extract, Cambridge Core article page | `https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693` | Wayback capture, HTTP 200, `text/html` | 1158765 |
| Fromont 2017, SciELO PDF | `https://www.scielo.br/j/anaismp/a/q5xByvmxMJwkQWQFw3qJkGM/?format=pdf&lang=en` | direct GET, HTTP 200, `application/pdf`, 21 pages | 6082597 |
| Fromont 2014, UNC Press book page | `https://web.archive.org/web/20240424143548/https://uncpress.org/book/9781469641249/the-art-of-conversion/` | Wayback capture, HTTP 200, `text/html` | 69581 |

Disclosure on the two publisher pages: both were met by a block on a plain desktop request and were then read through Wayback captures, which is an ordinary copy and not a bypass.

- `https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo--149117501/2FB5AD22282AF36704DE49E593623693` answered HTTP 429, "Too many automated requests from this network", on two attempts. Challenge met, not passed; the capture above (2026-02-03) was read instead.
- `https://uncpress.org/book/9781469641249/the-art-of-conversion/` answered HTTP 403 (`text/html`, 6180 bytes). Challenge met, not passed; the capture above (2024-04-24) was read instead.

Extracted text and HTML were cached at `/fast/scratch/hyaku/kotodama-r56/ScoutKongoChristianity/src/`. Every quote below was checked by exact substring against the normalized extracted text; page numbers for the Fromont article come from `pdftotext` per-page extraction (PDF page 1 = journal page 11).

---

### NEW-ScoutKongoChristianity-1

citation: Thornton, John. 1984. "The Development of an African Catholic Church in the Kingdom of Kongo, 1491–1750." *The Journal of African History* 25(2): 147–167. DOI 10.1017/S0021853700022830. Cambridge Core article page, published online 22 January 2009; author affiliation on the page: Allegheny College, Pennsylvania.
url: https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693
route: Wayback capture 20260203111247 of the Cambridge Core article page, HTTP 200, `text/html`, 1158765 bytes, read 2026-10-22; the live page answered HTTP 429 (rate limit) and was not retried through any other tool.
kind: paper
tier: B — the article is a peer-reviewed original study, but the row rests on the publisher's extract only, so it is a strong secondary summary for the argument and not authority for the article's evidence, names or dates.
scope: the article's stated argument — that Christianity in Kongo became a distinctly African form widely accepted as the country's religion, that a voluntary conversion gave the kingdom leeway over its rite, that royal control of church organization and finance kept it out of foreign hands, and that nineteenth-century missionaries rejected that local form. Not: the article's evidence, its named offices, its dates beyond the abstract's own, the Antonian movement, or anything on Kikongo vocabulary.
quotes:
- Extract, para. 1: "This article argues that although Christianity in Kongo took a distinctly African form it was widely accepted both in Kongo and in Europe"
- Extract, para. 2: "This was possible because Kongo, as a voluntary convert, had considerable leeway to contribute to its particular form of Christianity."
- Extract, para. 2: "its control over the Church organization and finance allowed it never to be an instrument for foreign domination"
- Extract, para. 2: "When European priests arrived in Kongo during the Portuguese colonial occupation at the end of the nineteenth century, they rejected the local form of Christianity"
teaches: Kongo's church was African-controlled: a voluntary conversion, local theological leeway and royal control of organization and finance kept it from becoming a foreign instrument until nineteenth-century missionaries rejected it.
draft sentences:
- Build the Kongo church as the kingdom's own institution rather than a mission field: Thornton argues that Christianity there took a distinctly African form and was widely accepted in Kongo and in Europe as the country's religion (NEW-ScoutKongoChristianity-1, Extract, para. 1).
- Give the kingdom bargaining room over its own rite: Thornton explains the leeway as the consequence of Kongo being a voluntary convert (NEW-ScoutKongoChristianity-1, Extract, para. 2).
- Keep church property and revenues under royal control if the clergy is to stay politically dependent; Thornton says control of the Church's organization and finance kept it from becoming an instrument of foreign domination (NEW-ScoutKongoChristianity-1, Extract, para. 2).
- Put the rupture late: Thornton dates the rejection of the local form of Christianity to European priests arriving under the Portuguese colonial occupation at the end of the nineteenth century (NEW-ScoutKongoChristianity-1, Extract, para. 2).

### NEW-ScoutKongoChristianity-2

citation: Fromont, Cécile. 2017. "Foreign Cloth, Local Habits: Clothing, Regalia, and the Art of Conversion in the Early Modern Kingdom of Kongo." *Anais do Museu Paulista: História e Cultura Material* 25(2): 11–31, May–August 2017. DOI 10.1590/1982-02672017v25n02d01-2. Open access.
url: https://www.scielo.br/j/anaismp/a/q5xByvmxMJwkQWQFw3qJkGM/?format=pdf&lang=en
route: direct plain GET on the SciELO PDF endpoint, HTTP 200, `application/pdf`, 6082597 bytes, 21 pages, text extracted in full and key sections read on 2026-10-22; page numbers taken from per-page extraction, PDF page 1 is journal page 11.
kind: paper
tier: B — open-access peer-reviewed expert article with object-level evidence and reproductions; it interprets images and documents rather than printing them, so it is strong secondary for the material vocabulary, not authority for the underlying records.
scope: named Kongo Christian dress and regalia and what they combined — the mpu cap, the nkutu shoulder net, the red coat with the insignia of the Order of Christ, the mestres' white shoulder cloth, raffia and brocade wrappers, coral beads, the king's rule through governors sent to provincial capitals, and Pedro IV's 1696 makeshift crown with the five-sword royal coat of arms after the 1665 loss at Mbwila. Not: Kikongo grammar, kinship, minkisi, nzimbu money, the Antonian movement, or rural practice beyond the elite the images show.
quotes:
- p. 12, description of the 1750s watercolor: "He wears an mpu cap on the head, an nkutu net over the shoulders"
- p. 12, same description: "two mestres, interpreters and leaders of the Church, wear their uniform composed of a white cloth draped over one shoulder"
- p. 13, opening of the historical sketch: "ruled with absolute power from his capital city over large territories through the governors he sent"
- p. 23, "Of Hats, Power, and History": "Pedro was coronated instead with a makeshift crown on which featured the royal coat of arms of the Kongo"
teaches: Kongo Christian regalia combined central African and European pieces into one visual language, so mpu caps, nkutu nets, mestres' white cloth and heraldic swords marked rank and faith.
draft sentences:
- Dress a Christian noble in named pieces a reader can picture: an mpu cap on the head, an nkutu net over the shoulders, a wooden staff, and a red coat carrying the insignia of the Order of Christ (NEW-ScoutKongoChristianity-2, p. 12).
- Make church leadership a named Kongo office: mestres are described as interpreters and leaders of the Church, marked by a white cloth draped over one shoulder (NEW-ScoutKongoChristianity-2, p. 12).
- Seat authority in a capital and send it outward: the king ruled from his capital city over large territories through governors he sent to the provincial capitals (NEW-ScoutKongoChristianity-2, p. 13).
- Stage a succession under material constraint: with the European-style crown lost to the Portuguese at Mbwila in 1665, Pedro IV was crowned at the abandoned capital São Salvador in 1696 with a makeshift crown carrying the royal coat of arms (NEW-ScoutKongoChristianity-2, p. 23).
- Treat regalia as an argument rather than costume: the article reads sartorial practice as displaying the realm's conversion under its monarchs and aristocrats (NEW-ScoutKongoChristianity-2, p. 11).

### NEW-ScoutKongoChristianity-3

citation: Fromont, Cécile. 2014. *The Art of Conversion: Christian Visual Culture in the Kingdom of Kongo*. Chapel Hill: University of North Carolina Press, published for the Omohundro Institute of Early American History and Culture. 328 pp.; paperback 2017, ISBN 978-1-4696-4124-9.
url: https://web.archive.org/web/20240424143548/https://uncpress.org/book/9781469641249/the-art-of-conversion/
route: Wayback capture 20240424143548 of the UNC Press book page, HTTP 200, `text/html`, 69581 bytes, read 2026-10-22; the live page answered HTTP 403.
kind: book
tier: B — publisher description of a scholarly monograph: accurate for how the press states the book's thesis and span, not a substitute for the book's evidence (QUALITY criterion 6).
scope: the book's framing as the publisher states it — an independent Kongo practicing Christianity across the sixteenth to nineteenth centuries, the conversion as a centuries-long dynamic process, and the elite independently combining old and new religious thought, political concepts and visual forms. Not: any quotation from the book, its object names, its documents, dates, or Kikongo terms.
quotes:
- publisher's description, para. 1: "the west central African kingdom of Kongo practiced Christianity and actively participated in the Atlantic world as an independent, cosmopolitan realm"
- publisher's description, para. 2: "The African kingdom’s elite independently and gradually intertwined old and new, local and foreign religious thought, political concepts, and visual forms"
teaches: Fromont reads Kongo's conversion as a centuries-long process in which the kingdom's elite independently intertwined local and foreign religious thought, politics and visual forms.
draft sentences:
- Keep the kingdom independent in the frame: the publisher describes Kongo as practicing Christianity while taking part in the Atlantic world as an independent, cosmopolitan realm (NEW-ScoutKongoChristianity-3, publisher's description, para. 1).
- Plan the conversion as a process with phases rather than a single decree, since the book spans the sixteenth to the nineteenth centuries under war, the slave trade and finally European colonialism (NEW-ScoutKongoChristianity-3, publisher's description, para. 1).
- Make the elite the agents: the description has them independently intertwining old and new religious thought, political concepts and visual forms into a changing Kongo Christian worldview (NEW-ScoutKongoChristianity-3, publisher's description, para. 2).

---

## Notes for the L1

- Sentence strength. The Thornton row is extract-only: use it for the thesis and for the sequence (voluntary conversion, royal control, late rupture), never for a date, a title or a number beyond the extract's own words. The two Fromont rows can carry object names and the 1665/1696 sequence; the 2017 article cites its own sources for them (Lopes/Pigafetta 1591, Eeckhout 1642, Bernardino d'Asti ca. 1750, Marcellino d'Atri on the 1696 coronation), which the entry should not upgrade into primary testimony.
- Overlap with sibling seats. The UNESCO and KongoKing rows already carry mbanza, the capital's church buildings and elite grave goods; my rows carry the church as an institution (mestres, royal finance, the late rejection) and the regalia vocabulary (mpu, nkutu, Order of Christ, coat of arms). Keep the entry from attributing architecture or archaeology to these three rows.
- Gaps I did not fill: the Antonian movement (Dona Beatriz Kimpa Vita), Kikongo catechisms and early grammars, nzimbu shell money, minkisi and the cosmogram dispute, raffia-cloth production and the title vocabulary of provinces other than the governors line. Other seats' rows must carry these.
- No installs or upgrades were made in this seat.

## unopened

- Cambridge Core live article page (`https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo--149117501/2FB5AD22282AF36704DE49E593623693`): HTTP 429 "Too many automated requests from this network" on two attempts; challenge met, not passed. Read through the Wayback capture instead.
- Cambridge Core PDF of the article body: no lawful open copy found. Search results offered Scribd, sci-hub and Academia.edu copies; the first two are shadow-library/pirate copies and the third needs a login, so none was opened.
- UNC Press live book page (`https://uncpress.org/9781469641249/the-art-of-conversion/`): HTTP 403; challenge met, not passed. Read through the Wayback capture instead.
- Fromont 2014 book text or introduction: the Project MUSE record (`https://muse.jhu.edu/book/35580`, plain GET, HTTP 200, read 2026-10-22) states "Open Access No" and gives 328 pages; no ordinary open copy of the introduction was found, so the publisher description is the row.
- Fromont's Harvard dissertation *Under the Sign of the Cross in the Kingdom of Kongo* (2008): only bibliographic records (Penn State art-history dissertations list, Smithsonian Libraries) surfaced, no open full text; a related 2011 *RES* article exists but was not needed once the 2017 open article was in hand.
- `https://chsc.uc.pt/wp-content/uploads/2021/10/pdf-final_compressed-2.pdf`: fetched, HTTP 200, 414556 bytes, 3 pages, an image-only scan with no text layer; content unverified and unused.
- Semantic Scholar API for the Thornton DOI: HTTP 429. OpenAlex was queried instead and reports `oa_status: closed`, `any_repository_has_fulltext: false`; that metadata is not a source row.
- John Thornton, "Afro-Christian Syncretism in the Kingdom of Kongo" (2013): a PDF is hosted on an unaffiliated squarespace site and Scribd copies exist; provenance of the squarespace copy is unclear, so it was not used, and it is a different article from the one this seat was asked for.
