# Review: carried rows S359 and S360 (round-56 spot-check §5 item 5)

Seat: `KotodamaR57.ReviewCarriedS359S360` (leaf reviewer, read-only lane; no subagents).
Scope: the two carried findings — S359 (the pp. 469/470 locators) and S360 (the provincial-title sentence).
Original findings file: `.ufo/waves/round-56/falsify/ReviewRowsS359toS361.md` (findings 1–2 for S359, finding 3 for S360).
Carried list: `corpus/lessons/round-56-verifier-spotcheck.md` §5 item 5.

## Method (all ordinary means)

- Re-opened S359: `https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt` — plain GET, HTTP 200, 896,693 bytes, text/plain; sha256 `2459b0db…`. Item page `https://archive.org/details/monumentamissionariaafricana` — plain GET, HTTP 200.
- Re-opened S360: `https://www2.historia.uff.br/tempo/wp-content/uploads/2024/11/artg6-7.pdf` — plain GET, HTTP 200, 67,503 bytes, application/pdf; sha256 `d1e42387…`.
- Page mapping: fetched `MonumentaMissionáriaAfricana-01.001_scandata.xml` (HTTP 200) and the per-page word layout from `…_djvu.xml` (HTTP 200) to identify the scanned leaf carrying each quoted span and its printed page footer. No challenge, login, or capture was met or bypassed.
- Locator: `python3 -B reports/round-57/reopen-quote.py '<url>' '<quote>'` run for every quote used below; output pasted verbatim.

## Finding 1 — S359: wrong printed-page locators (pp. 469/470 and 489/490)

Verdict: **AGREE** with `ReviewRowsS359toS361.md` findings 1–2. The quoted text is verbatim, but the printed pages are 470 (doc. 142, both anchors and the Gate span) and 490 (doc. 147, both anchors), not 469 and 489.

Evidence:

- Leaf mapping (scanned leaf → printed page footer read from the leaf's bottom word rows):
  - leaf 530 (footer `4 *9` = 469) holds the paragraph *preceding* `os ditos mercadores…`;
  - leaf 531 (footers between 469 and 473; doc. 142 text) holds both doc. 142 anchor spans: `os ditos mercadores leuam cada dia nossos naturaes, filhos da terra e filhos de nossos fidallgos e vassallos` and `nosa terra se despouoa toda` — i.e. printed p. 470;
  - leaf 551 (footer `49°` = 490) holds both doc. 147 anchor spans: `se sam catiuos, se forros` and `e as poderam leuar e embarquar` — i.e. printed p. 490 (leaf 550 = p. 489 holds the preceding text, per the same footer map).
- Served text verbatim (OCR of `MonumentaMissionáriaAfricana-01.001_djvu.txt`, lines 19497–19536 for doc. 142; 20292–20296 for doc. 147): the two July quotes sit inside the 6 July 1526 letter (doc. 142, dated `yulho`), and the two October quotes sit inside the 18 October 1526 letter (doc. 147, after the `49°` footer of p. 490).

Locator lines (round-57):

```
LOCATED https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt
LOCATED https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt
LOCATED https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt
LOCATED https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt
```

(four spans: July `os ditos mercadores…`, July `nosa terra se despouoa toda`, October `se sam catiuos, se forros`, October `e as poderam leuar e embarquar`; each run printed `LOCATED`.)

### Fix (registry cell wrong → superseding row; SOURCES is append-only)

The wrong cell is the row's `anchor` (four locator labels). Draft superseding row, id left as `S4xx` for the L1 (records rows S481–S499), teaches opening `supersedes S359 — `, otherwise mirrors S359's citation, URL, kind, tier, scope, status/date/expiry and used-by:

```
| S4xx | Brásio, António (ed.), *Monumenta Missionaria Africana. África Ocidental (1471–1531)*, vol. I, Lisbon: Agência Geral do Ultramar, 1952 (the scan's title page prints the editor as Padre Antonio Brasio); Internet Archive item `monumentamissionariaafricana`, file `MonumentaMissionáriaAfricana-01.001_djvu.txt`. — https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt (direct download, HTTP 200, 896,693 bytes, no login or lending; item page https://archive.org/details/monumentamissionariaafricana. Text is the scan's OCR, so some letters are garbled and editorial footnote numbers appear inline; quotes below are exactly as that file prints them. accessed: 2026-10-22) | book | A | Afonso I's letters to João III of 6 July 1526 (doc. 142, pp. 468–471) and 18 October 1526 (doc. 147, pp. 488–491), and the receipt of 18 January 1526 for Portuguese garments sent to the king (doc. 139, pp. 455–457): naming of persons and offices, the royal verification rule for captives, the letter's account of kidnapping and depopulation, and the itemised clothing. The 6 July letter is an archive copy (ATT, CC-I-33-121), not an autograph. (tier note: A — a scholarly edition of the primary documents, authoritative for this exact correspondence.) | doc. 142, p. 470: "os ditos mercadores leuam cada dia nossos naturaes, filhos da terra e filhos de nossos fidallgos e vassallos"; doc. 142, p. 470: "nosa terra se despouoa toda"; doc. 147, p. 490: "se sam catiuos, se forros"; doc. 147, p. 490: "e as poderam leuar e embarquar" | supersedes S359 — Brásio's first volume prints Afonso I's 1526 letters and receipt, giving the court's own wording on kidnapped nobles, a royal verification commission and Portuguese garments. | mined | 2026-10-22 | 365d | corpus/knowledge/civilizations/kongo-kingdom.md |
```

Gate line (≤25 words, no character reference):

```
- S4xx — https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt — accessed 2026-10-22 — doc. 142, p. 470: “os ditos mercadores leuam cada dia nossos naturaes, filhos da terra e filhos de nossos fidallgos e vassallos”. Grounds: supersedes S359 — Brásio's first volume prints Afonso I's 1526 letters and receipt, giving the court's own wording on kidnapped nobles, a royal verification commission and Portuguese garments. Seat: ReviewCarriedS359S360.
```

Locator line for the Gate span:

```
python3 -B reports/round-57/reopen-quote.py 'https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt' 'os ditos mercadores leuam cada dia nossos naturaes, filhos da terra e filhos de nossos fidallgos e vassallos'
LOCATED https://archive.org/download/monumentamissionariaafricana/MonumentaMission%C3%A1riaAfricana-01.001_djvu.txt
```

### Same-fix, entry side (locator labels, not wording)

The entry sentences are not over-reads; they cite the wrong page. Recommended updates (draft; for the L1 to apply with the superseding row):

- `corpus/knowledge/civilizations/kongo-kingdom.md:18` — old: `(S359, doc. 142, p. 469)` → new: `(S359, doc. 142, p. 470)`
- `corpus/knowledge/civilizations/kongo-kingdom.md:110` — old: `S359 (doc. 147, p. 489)` → new: `S359 (doc. 147, p. 490)`
- `corpus/knowledge/civilizations/kongo-kingdom.md:140` — old: `(S359, doc. 142, p. 469)` → new: `(S359, doc. 142, p. 470)`; old: `(S359, doc. 147, p. 489)` → new: `(S359, doc. 147, p. 490)`
- `corpus/knowledge/civilizations/kongo-kingdom.md:146` — old: `(S374, title page; S359, doc. 142, p. 469)` → new: `(S374, title page; S359, doc. 142, p. 470)`

## Finding 2 — S360: provincial-title sentence overgeneralizes

Verdict: **AGREE** with `ReviewRowsS359toS361.md` finding 3. S360's served text (p. 100 of the PDF text layer) says only that the *old lineage heads of the provinces* began styling themselves as counts, marquises and dukes after the 1512 Regimento; the entry's `provincial chiefs` drops the lineage-head qualifier.

Evidence (served text, S360 PDF, section “Conversão e catolização”, paragraph beginning “Mas não foi apenas o cristianismo”):

```
…a justiça do Estado passou a se guiar pela normas portuguesas, a partir da embaixada de Simão da Silva, portador do Regimento de
1512, e os antigos chefes de linhagem das províncias passaram a intitular-de de condes, marqueses, duques.
```

Locator line:

```
python3 -B reports/round-57/reopen-quote.py 'https://www2.historia.uff.br/tempo/wp-content/uploads/2024/11/artg6-7.pdf' 'os antigos chefes de linhagem das províncias passaram a intitular-de de condes, marqueses, duques'
LOCATED https://www2.historia.uff.br/tempo/wp-content/uploads/2024/11/artg6-7.pdf
```

### Fix (entry over-read → entry-sentence change)

`corpus/knowledge/civilizations/kongo-kingdom.md:65`:

- old: `After the 1512 Regimento provincial chiefs carried the Portuguese titles count, marquis and duke (S360, section "Conversão e catolização").`
- new: `After the 1512 Regimento, the old lineage heads of the provinces began styling themselves as counts, marquises and dukes (S360, section "Conversão e catolização").`

No registry change is warranted for S360: its anchors remain verbatim at the stated section/paragraph locators (checked against the served PDF: `Quando o comércio de pessoas fugiu do controle do rei` → `…Afonso I escreveu ao rei português`; `O comércio de escravos era antigo…`; `até mesmo nobres congoleses…`; `São Salvador, nome atribuído a mbanza Kongo após a conversão dos reis` at section “Congo descoberto”).

## Other checks (no finding)

- S359 row car citation/URL/kind/tier/scope/teaches verify; the July-letter will clause (`nossa vontade hé que nestes Reynos nam aja trato de esprauos nem sayda pera elles`) is on printed p. 470 (leaf 531), consistent with the corrected locators.
- The round-56 Gate lessons file (`corpus/lessons/round-56.md:24`) is filed bytes; no in-place edit proposed (the superseding row carries the corrected Gate).

## Summary

| item | verdict | remedy |
|---|---|---|
| S359 locators (pp. 469/470; 489/490) | agree | superseding row S4xx (draft above) + entry-line locator updates at kongo-kingdom.md:18,110,140,146 |
| S360 provincial-title over-read | agree | entry-sentence change at kongo-kingdom.md:65 (old → new above) |

No tools installed; no lane file edited; no git/jj state touched. All work ran in `/fast/scratch/hyaku/kotodama-r57/ReviewCarriedS359S360/`.
