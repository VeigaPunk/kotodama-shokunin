# ReviewKongoA58 — carried kongo-kingdom sentence fixes, lines 18, 65, 82, 84, 85, 89

Seat: `KotodamaR58A2.ReviewKongoA58` (leaf reviewer, read-only lane except this file).
Scope: round-57 spotcheck §5 item 6, carried a second round — entry lines 18, 65, 82, 84, 85, 89 of `corpus/knowledge/civilizations/kongo-kingdom.md`, fixes drafted in `.ufo/waves/round-57/build/ReviewCarried*.md`.
Method: each cited source re-opened this session by ordinary means (plain `curl` GETs, no challenge met or passed); text checked against the served bytes; anchors re-located with `python3 -B reports/round-58/reopen-quote.py '<url>' '<quote>'` (byte copy of the round-57 instrument). Scratch: `/fast/scratch/hyaku/kotodama-r58/ReviewKongoA58/` (served copies kept). LSP unavailable (no `xd://lsp` device); verdicts rest on the served text.

## Re-opened sources (this session)

| row | URL | result |
|---|---|---|
| S359 | `https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt` (+ `_scandata.xml`) | HTTP 200, 896,693 B — byte-equal to the row's recorded size |
| S360 | `https://www2.historia.uff.br/tempo/wp-content/uploads/2024/11/artg6-7.pdf` | HTTP 200, 67,503 B — byte-equal |
| S383 | `https://web.archive.org/web/20260203111247/…cambridge.org…2FB5AD22282AF36704DE49E593623693` | HTTP 200, 1,158,760 B |
| S384 | `https://www.redalyc.org/jatsRepo/273/27353124003/27353124003.pdf` | HTTP 200, 1,291,427 B — byte-equal |
| S392 | `https://revistas.usp.br/sankofa/article/download/187402/173183/497395` | HTTP 200, 985,805 B — byte-equal |
| S396 | `https://web.archive.org/web/20230529091312id_/https://www.metmuseum.org/art/collection/search/312342` | HTTP 200, 204,151 B |
| S399 | `https://web.archive.org/web/20260314181520id_/https://www.metmuseum.org/art/collection/search/318318` | HTTP 200, 232,310 B |

## Per-line verdicts and exact fixes

### Line 18 — S359 printed-page locators (AGREE)

Served OCR text (`_djvu.txt`, concatenated leaves, hyphen-breaks joined): the doc. 142 quotes `os ditos mercadores leuam cada dia nossos naturaes, filhos da terra e filhos de nossos fidallgos e vassallos` and `nosa terra se despouoa toda` sit between printed-page footers `4 *9` (469) and `* 7 °` (470) → **printed p. 470**, not 469. The doc. 147 quotes `se sam catiuos, se forros` and `e as poderam leuar e embarquar` sit between `489`'s leaf and footer `49°` (490) → **printed p. 490**, not 489. The letter dates read `escryta aos bj djas de yulho` (6 July) and `xbiij 0 dia de oytobro` (18 October), matching docs. 142/147. The entry's `(S359, doc. 142, p. 469)` cites the wrong page.

Fix (`kongo-kingdom.md:18`):
- old: `Afonso I's letters are a royal voice (S359, doc. 142, p. 469).`
- new: `Afonso I's letters are a royal voice (S359, doc. 142, p. 470).`

Registry companion: the wrong cells are S359's anchor locators → superseding row S5xx-1 below (append-only).

Locator:
```
python3 -B reports/round-58/reopen-quote.py 'https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt' 'os ditos mercadores leuam cada dia nossos naturaes, filhos da terra e filhos de nossos fidallgos e vassallos'
LOCATED https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt
```

### Line 65 — S360 "provincial chiefs" drops the lineage-head qualifier (AGREE)

Served PDF text (`pdftotext -layout`, section "Conversão e catolização", p. 100): `…a partir da embaixada de Simão da Silva, portador do Regimento de 1512, e os antigos chefes de linhagem das províncias passaram a intitular-de de condes, marqueses, duques.` — *antigos chefes de linhagem das províncias* (old lineage heads of the provinces), not unqualified "provincial chiefs".

Fix (`kongo-kingdom.md:65`, replacing only the last clause of the line):
- old: `After the 1512 Regimento provincial chiefs carried the Portuguese titles count, marquis and duke (S360, section "Conversão e catolização").`
- new: `After the 1512 Regimento, the old lineage heads of the provinces began styling themselves as counts, marquises and dukes (S360, section "Conversão e catolização").`

No registry change for S360: the four anchors verify verbatim in the served PDF.

Locator:
```
python3 -B reports/round-58/reopen-quote.py 'https://www2.historia.uff.br/tempo/wp-content/uploads/2024/11/artg6-7.pdf' 'os antigos chefes de linhagem das províncias passaram a intitular-de de condes, marqueses, duques'
LOCATED https://www2.historia.uff.br/tempo/wp-content/uploads/2024/11/artg6-7.pdf
```

### Line 82 — S383 "royal control" over-read (AGREE)

Served capture text (Extract, para. 2): `Kongo's control over the theological content allowed the religion to gain mass acceptance while its control over the Church organization and finance allowed it never to be an instrument for foreign domination, in spite of Portuguese attempts to use it as a 'fifth column'.` The subject is Kongo; "royal" does not occur in the Extract (`royal control` → absent). The seat's replacement "Kongo's control" is the page's own attribution ("its" = Kongo's).

Fix (`kongo-kingdom.md:82`, mid-sentence replacement only):
- old: `with royal control of church organization and finance (S383, Extract, paras. 1–2).`
- new: `with Kongo's control of church organization and finance (S383, Extract, paras. 1–2).`

Registry companion: S383's teaches cell (`royal control of organization and finance`) AND its scope cell (`royal control of church organization and finance`) both carry the same over-read — the round-57 seat caught only teaches → superseding row S5xx-2 below corrects both.

Locator:
```
python3 -B reports/round-58/reopen-quote.py 'https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693' 'its control over the Church organization and finance allowed it never to be an instrument for foreign domination'
LOCATED https://web.archive.org/web/20260203111247/…
```

### Line 84 — two findings (BOTH AGREE)

(a) S384 *mestres* generalization. Served p. 12 (pdftotext of the PDF): `Behind him, two mestres, interpreters and leaders of the Church, wear their uniform composed of a white cloth draped over one shoulder.` — a caption for two figures in one watercolor (`Figure 1 − Bernardino d'Asti. Reception of a capuchin missionary by a local ruler. Italy, ca. 1740.`), not a general office rule. The seat's fix restores the depicted scope:

- old: `*Mestres* were interpreters and leaders of the Church, marked by a white shoulder cloth (S384, p. 12).`
- new: `In the ca. 1740 watercolor, Fromont identifies two *mestres* as Church interpreters and leaders, wearing a white cloth over one shoulder (S384, p. 12).`

Locator:
```
python3 -B reports/round-58/reopen-quote.py 'https://www.redalyc.org/jatsRepo/273/27353124003/27353124003.pdf' 'two mestres, interpreters and leaders of the Church, wear their uniform composed of a white cloth draped over one shoulder'
LOCATED https://www.redalyc.org/jatsRepo/273/27353124003/27353124003.pdf
```

(b) S399 locator "object 318318". Served capture: `Object Number: 1999.295.2`; `318318` is the collection-search record id (it appears only in the URL, not in the record body). Fix:

- old: `(S399, Overview label, object 318318)`
- new: `(S399, Overview label, record 318318)`

Registry companion: S399's citation cell (`object number 318318`) and both anchor locators → superseding row S5xx-5 below.

Locator:
```
python3 -B reports/round-58/reopen-quote.py 'https://web.archive.org/web/20260314181520id_/https://www.metmuseum.org/art/collection/search/318318' 'Uniting symbols of Kongo religious and secular power, this prestige staff was used as an insignia of office by a Kongo chief'
LOCATED https://web.archive.org/web/20260314181520id_/https://www.metmuseum.org/art/collection/search/318318
```

### Line 85 — S392 authorship/location conflation (AGREE)

Served PDF (30 leaves, printed pp. 7–36): Batsîkama's own narrative on printed **p. 27** reads `…condenaram a profetisa angolana a morrer queimada viva. Isso aconteceu no dia 2 de julho de 1706, numa sexta-feira.` — Kimbangu is absent from that sentence (it appears in the preceding Thornton block quote, `o rei sedeado em Kimbângu, Pedro IV, mandou prendê-la`). On printed **p. 32**, inside a block quotation introduced `William Graham Lister Randels conclui, em relação ao movimento antoniano, que:`, the text reads `No dia 2 de julho de 1706, em Kimbangu, aos olhos dos missionários, eles foram entregues juntos às chamas.` So the 2-July date is Batsîkama's own; "at Kimbangu" is the quoted Randels block's, not Batsîkama's. The seat's fix is exact:

- old: `Batsîkama gives 2 July at Kimbangu (S392, p. 32), and Farias places the execution in Mbanza Kongo (S381, p. 210): date and place stay contested (to-verify).`
- new: `Batsîkama's own account gives 2 July 1706 (S392, p. 27), while the block quotation he credits to Randels places the execution at Kimbangu (S392, p. 32); Farias places it in Mbanza Kongo (S381, p. 210): date and place stay contested (to-verify).`

Registry companion: S392's scope cell carries the related conflation `the Antonian ending in 1706` — Batsîkama's own p. 27 says the movement `só cessou depois de 1719` and the Randels block ends it `em 1712` → superseding row S5xx-3 below corrects the scope. (The matching entry heading defect is already resolved: line 85 heads "The Antonian movement (from 1704)".)

Locators:
```
python3 -B reports/round-58/reopen-quote.py 'https://revistas.usp.br/sankofa/article/download/187402/173183/497395' 'condenaram a profetisa angolana a morrer queimada viva. Isso aconteceu no dia 2 de julho de 1706, numa sexta-feira'
LOCATED https://revistas.usp.br/sankofa/article/download/187402/173183/497395
python3 -B reports/round-58/reopen-quote.py 'https://revistas.usp.br/sankofa/article/download/187402/173183/497395' 'No dia 2 de julho de 1706, em Kimbangu, aos olhos dos missionários'
LOCATED https://revistas.usp.br/sankofa/article/download/187402/173183/497395
```

### Line 89 — S396 hedge stripped (AGREE)

Served capture (intro `<p>` with `<br/><br/>` block separators), first block: `The term "nkisi" may relate to a wide spectrum of physical receptacles, including cloth packets, filled vessels, as well as the carved wood sculptures studied by art historians.` The entry's "the term covers" drops the "may relate to" hedge and narrows "carved wood sculptures" to "carved wood". The seat's fix restores the page's strength:

- old: `The Met says the term covers cloth packets and filled vessels as well as carved wood (S396, essay, first paragraph).`
- new: `The Met says the term nkisi may relate to a wide spectrum of physical receptacles, including cloth packets, filled vessels, as well as carved wood sculptures (S396, essay, first paragraph).`

Registry companion: S396's fourth anchor is labelled `essay, fourth paragraph` but the quote sits in the **third** `<br/>`-separated block (block order verified: collaboration+receptacles → amulets/cross → cloth-and-knots) → superseding row S5xx-4 below (anchor label corrected to third paragraph; teaches keeps the same substantive claim).

Locator:
```
python3 -B reports/round-58/reopen-quote.py 'https://www.metmuseum.org/art/collection/search/312342' 'may relate to a wide spectrum of physical receptacles, including cloth packets, filled vessels'
LOCATED https://www.metmuseum.org/art/collection/search/312342
```

## Drafted superseding rows (records rows, ids S560–S599 assigned by the L1)

11 cells each; teaches opens `supersedes S### — `; every superseded row is cited by `kongo-kingdom.md`, so status `mined` with the same used-by; opened 2026-10-23, recheck 2027-10-23. Anchor quotes unchanged except where the locator label itself is the defect. All locator lines pasted above.

```
| S5xx-1 | Brásio, António (ed.), *Monumenta Missionaria Africana. África Ocidental (1471–1531)*, vol. I, Lisbon: Agência Geral do Ultramar, 1952 (the scan's title page prints the editor as Padre Antonio Brasio); Internet Archive item `monumentamissionariaafricana`, file `MonumentaMissionáriaAfricana-01.001_djvu.txt`. — https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt (direct download, HTTP 200, 896,693 bytes, no login or lending; item page https://archive.org/details/monumentamissionariaafricana. Text is the scan's OCR, so some letters are garbled and editorial footnote numbers appear inline; quotes below are exactly as that file prints them. accessed: 2026-10-23; supersedes S359 — re-opened 2026-10-23: both doc. 142 anchors sit between printed-page footers 469 and 470 → p. 470, both doc. 147 anchors between 489 and `49°` → p. 490; the old row's locators read 469/489.) | book | A | Afonso I's letters to João III of 6 July 1526 (doc. 142, pp. 468–471) and 18 October 1526 (doc. 147, pp. 488–491), and the receipt of 18 January 1526 for Portuguese garments sent to the king (doc. 139, pp. 455–457): naming of persons and offices, the royal verification rule for captives, the letter's account of kidnapping and depopulation, and the itemised clothing. The 6 July letter is an archive copy (ATT, CC-I-33-121), not an autograph. (tier note: A — a scholarly edition of the primary documents, authoritative for this exact correspondence.) | doc. 142, p. 470: "os ditos mercadores leuam cada dia nossos naturaes, filhos da terra e filhos de nossos fidallgos e vassallos"; doc. 142, p. 470: "nosa terra se despouoa toda"; doc. 147, p. 490: "se sam catiuos, se forros"; doc. 147, p. 490: "e as poderam leuar e embarquar" | supersedes S359 — Brásio's first volume prints Afonso I's 1526 letters and receipt, giving the court's own wording on kidnapped nobles, a royal verification commission and Portuguese garments. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/civilizations/kongo-kingdom.md |
| S5xx-2 | Thornton, John. 1984. "The Development of an African Catholic Church in the Kingdom of Kongo, 1491–1750." *The Journal of African History* 25(2): 147–167. DOI 10.1017/S0021853700022830. Cambridge Core article page, published online 22 January 2009; author affiliation on the page: Allegheny College, Pennsylvania. — https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693 (Wayback capture 20260203111247 of the Cambridge Core article page, HTTP 200, `text/html`, 1158760 bytes, re-read 2026-10-23; supersedes S383 — the Extract attributes the church-organization-and-finance clause to "its" (Kongo's) control, not royal control; the old row's teaches and scope said "royal".) | paper | B | the article's stated argument — that Christianity in Kongo became a distinctly African form widely accepted as the country's religion, that a voluntary conversion gave the kingdom leeway over its rite, that Kongo's control of church organization and finance kept it out of foreign hands, and that nineteenth-century missionaries rejected that local form. Not: the article's evidence, its named offices, its dates beyond the abstract's own, the Antonian movement, or anything on Kikongo vocabulary. (tier note: B — the article is a peer-reviewed original study, but the row rests on the publisher's extract only, so it is a strong secondary summary for the argument and not authority for the article's evidence, names or dates.) | Extract, para. 1: "This article argues that although Christianity in Kongo took a distinctly African form it was widely accepted both in Kongo and in Europe"; Extract, para. 2: "This was possible because Kongo, as a voluntary convert, had considerable leeway to contribute to its particular form of Christianity."; Extract, para. 2: "its control over the Church organization and finance allowed it never to be an instrument for foreign domination"; Extract, para. 2: "When European priests arrived in Kongo during the Portuguese colonial occupation at the end of the nineteenth century, they rejected the local form of Christianity" | supersedes S383 — Kongo's church was African-controlled: a voluntary conversion, local theological leeway and Kongo's control of organization and finance kept it from becoming a foreign instrument until nineteenth-century missionaries rejected it. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/civilizations/kongo-kingdom.md |
| S5xx-3 | Batsîkama, Patrício. 2021. "Evangelização, guerra civil no Kôngo e Ñsîmba Vita (Kimpa Vita)". *Sankofa: Revista de História da África e de Estudos da Diáspora Africana* 14(25): 7-36. ISSN 1983-6023; no DOI printed on the article or landing page. Stable ids: article https://revistas.usp.br/sankofa/article/view/187402 and the PDF at https://revistas.usp.br/sankofa/article/download/187402/173183 — https://revistas.usp.br/sankofa/article/download/187402/173183/497395 (direct plain request, HTTP 200, application/pdf, 985,805 bytes, 30 pages, re-read 2026-10-23; no challenge; supersedes S392 — the old scope cell read "the Antonian ending in 1706", conflating the execution with the movement's end: Batsîkama's own p. 27 has it cease only after 1719, the p. 32 Randels block in 1712.) | paper | B | the 1665 campaign from the Kongo side (two days, field offices, the king's death), the post-1667 proclamation and election of kings at Bula and Kibangu, Daniel I's 1678 entry into Mbanza Kongo, Kimpa Vita's execution in 1706 and the later, disputed end of the Antonian movement (after 1719 in Batsîkama's own account, 1712 in the Randels block he quotes), and the 1709-versus-1712 dispute over the final conquest. Not demography, trade volumes or material culture. (tier note: B — peer-reviewed article by a professor of Angolan history (ISPT, Luanda), arguing from Cadornega, Cuvelier and Randles; strong on Kongo-side names and sequence, partly reconstructive.) | p. 19: "É importante salientar que foi logo de manhã, por volta das 9 horas de 27 de Outubro de 1665, que aconteceu o primeiro confronto."; p. 22: "A sua ida a Mbânz’a Kôngo em 1678 como monarca foi acompanhada pelos militares Makela (Makaba)"; p. 24: "Visto que Mbânz’a Kôngo estava sem governo desde 1667, os reis eram proclamados ou eleitos pelos seus apoiantes em Kôngo dya Lemba (Bula) ou Kimbângu."; p. 32, in a block quotation credited to Randels 2002: "Já antes do assalto final que em 1709 D. Pedro IV lançou contra São Salvador, ainda ocupado por hereges rebeldes (antonianos)" | supersedes S392 — Gives the Kongo-side sequence and names: a first clash on 27 October 1665, elected kings at Bula and Kibangu, Daniel I's 1678 entry, and a 1709 or 1712 final conquest. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/civilizations/kongo-kingdom.md |
| S5xx-4 | The Metropolitan Museum of Art. *Male Power Figure (Nkisi)*, late 19th–mid-20th century, Kongo peoples, Democratic Republic of the Congo; artist credited as Kongo artist and nganga. Object record 312342, accession 1979.206.127. — https://www.metmuseum.org/art/collection/search/312342 (Wayback capture 20230529091312 (HTTP 200, 204,151 bytes, re-read 2026-10-23), object essay and detail fields read; supersedes S396 — the "Knots and the act of tying" anchor sits in the third `<br/><br/>`-separated essay block, not the fourth.) | docs | A | what the word nkisi may cover, the nganga's role, the crossroads cross and its double reading, and binding and cloth as technique and payment. (tier note: A — the holding museum's record and essay for this exact object; authoritative for the Met's description.) | essay, first paragraph: "This work was the product of an intense collaboration between a sculptor and the initiated priest"; essay, first paragraph: "may relate to a wide spectrum of physical receptacles, including cloth packets, filled vessels"; essay, second paragraph: "The cross alludes to the division between the land of the living and the land of the dead"; essay, third paragraph: "Knots and the act of tying are associated with the binding and capturing of a spirit." | supersedes S396 — The Met describes nkisi as a class of receptacles activated by an nganga, with binding knots, cloth offerings and a crossroads cross carrying spirit and transaction. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/civilizations/kongo-kingdom.md |
| S5xx-5 | The Metropolitan Museum of Art. No date printed. "Staff with Saint Anthony of Padua," object record 318318, object number 1999.295.2, Kongo artist, 19th century, brass, wood and iron; Gift of Ernst Anspach, 1999. Collection record. — https://www.metmuseum.org/art/collection/search/318318 (live page returned HTTP 429 behind a Vercel Security Checkpoint (challenge met, not passed); record re-read 2026-10-23 from Wayback capture 20260314181520id_ of the same URL, HTTP 200, 232,310 bytes; supersedes S399 — 318318 is the collection-search record id, the served Object Number is 1999.295.2.) | docs | A | the prestige staff as an insignia of office held by a Kongo chief, its brass Saint Anthony pendant and the saint's attributes, and the museum's identification of Saint Anthony as one of the most loved saints in Kongo Christianity. (tier note: A — the holding museum's own record and gallery label for the object it holds.) | Overview label, record 318318: "Uniting symbols of Kongo religious and secular power, this prestige staff was used as an insignia of office by a Kongo chief."; Overview label, record 318318: "At its summit is a brass pendant of St. Anthony of Padua, one of the most beloved saints in Kongo Christianity." | supersedes S399 — A Kongo prestige staff is an insignia of office topped with a brass Saint Anthony, joining religious and secular authority in one carried object. | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/civilizations/kongo-kingdom.md |
```

## Gate lines (round-58 format)

```
- S5xx-1 — https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt — accessed 2026-10-23 — doc. 142, p. 470: “os ditos mercadores leuam cada dia nossos naturaes, filhos da terra e filhos de nossos fidallgos e vassallos”. Grounds: supersedes S359 — Brásio's first volume prints Afonso I's 1526 letters and receipt, giving the court's own wording on kidnapped nobles, a royal verification commission and Portuguese garments. Seat: ReviewKongoA58.
- S5xx-2 — https://web.archive.org/web/20260203111247/https://www.cambridge.org/core/journals/journal-of-african-history/article/abs/development-of-an-african-catholic-church-in-the-kingdom-of-kongo-149117501/2FB5AD22282AF36704DE49E593623693 — accessed 2026-10-23 — Extract, para. 1: “This article argues that although Christianity in Kongo took a distinctly African form it was widely accepted both in Kongo and in Europe”. Grounds: supersedes S383 — Kongo's church was African-controlled: a voluntary conversion, local theological leeway and Kongo's control of organization and finance kept it from becoming a foreign instrument until nineteenth-century missionaries rejected it. Seat: ReviewKongoA58.
- S5xx-3 — https://revistas.usp.br/sankofa/article/download/187402/173183/497395 — accessed 2026-10-23 — p. 19: “É importante salientar que foi logo de manhã, por volta das 9 horas de 27 de Outubro de 1665, que aconteceu o primeiro confronto.”. Grounds: supersedes S392 — Gives the Kongo-side sequence and names: a first clash on 27 October 1665, elected kings at Bula and Kibangu, Daniel I's 1678 entry, and a 1709 or 1712 final conquest. Seat: ReviewKongoA58.
- S5xx-4 — https://www.metmuseum.org/art/collection/search/312342 — accessed 2026-10-23 — essay, first paragraph: “This work was the product of an intense collaboration between a sculptor and the initiated priest”. Grounds: supersedes S396 — The Met describes nkisi as a class of receptacles activated by an nganga, with binding knots, cloth offerings and a crossroads cross carrying spirit and transaction. Seat: ReviewKongoA58.
- S5xx-5 — https://www.metmuseum.org/art/collection/search/318318 — accessed 2026-10-23 — Overview label, record 318318: “Uniting symbols of Kongo religious and secular power, this prestige staff was used as an insignia of office by a Kongo chief.”. Grounds: supersedes S399 — A Kongo prestige staff is an insignia of office topped with a brass Saint Anthony, joining religious and secular authority in one carried object. Seat: ReviewKongoA58.
```

## Residual risk and verification gaps

- The S359 page mapping was read from the OCR's own printed-page footers (469 → `4 *9`, 470 → `* 7 °`, 490 → `49°`, 491 → `49 1`), not from the scandata leaf map; the round-57 seat's leaf mapping (leaf 531 → p. 470, leaf 551 → p. 490) agrees. If the L1 wants a belt-and-suspenders check, `MonumentaMissionáriaAfricana-01.001_scandata.xml` is saved in my scratch dir.
- S383's teaches fix writes "Kongo's control" (the page's subject attribution), not the literal "its control"; the verbatim span `its control over the Church organization and finance` stays the anchor. The scope cell fix was added by me — the round-57 seat corrected only teaches.
- S396's paragraph count rests on the capture's `<br/><br/>` separators; the live page serves identical text (locator LOCATED on the live URL this session). The round-57 seat's optional teaches hedge ("may cover" in scope) is included in S5xx-4's scope cell.
- The S392 fix cites `S392, p. 27` (a page not in the row's anchor list); if the L1 prefers every cited page to be anchored, the p. 27 quote above is locator-verified and can be appended to S5xx-3's anchor cell.
- If the L1 wants the entry to cite the new S5xx ids instead of the superseded ones, the used-by convention applied to round-56 supersessions (`supersedes` rows taking over used-by) should be checked at integration; every fix above keeps the S3xx citation, matching the round-57 drafts.

installs: none (curl, pdftotext 26.08, python3 stdlib already present; the locator's `uv run --with pypdf` ran under the existing uv).
