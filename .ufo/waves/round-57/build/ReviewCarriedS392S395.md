# ReviewCarriedS392S395 — round-57 carry review (S392, S395)

Seat: `KotodamaR57.ReviewCarriedS392S395` (leaf). Task: re-open the carried round-56 falsify findings for S392 (two over-reads) and S395 (artist credit) by ordinary means, check each against the served text, and give a verdict plus exact fix (entry-sentence change, or a drafted superseding SOURCES row with its Gate line and locator line).

Finding sources (falsify wave, lane): `kotodama-shokunin/.ufo/waves/round-56/falsify/ReviewRowsS392toS394.md` (findings at lines 5–6) and `.../ReviewRowsS395toS397.md` (finding at line 12). Carried by `corpus/lessons/round-56-verifier-spotcheck.md` §5 item 5 and claims.json `records_not_claims` item 5. Note: the assignment's grep path `/home/vgpnk/Projects/shokunin/.ufo/waves/round-56/falsify/` does not exist; the falsify wave lives in the lane at `kotodama-shokunin/.ufo/waves/round-56/falsify/`.

Method: ordinary means only — plain GETs (curl / urllib with a browser UA), Wayback replay, and PDF text extraction (pdftotext 26.08.0 and pypdf 6.21.2 via `uv run --with`). The live Met host returns 429/bot challenge; that challenge was met and routed around by Wayback captures (reported per QUALITY criterion 10 as "challenge met, not passed"). No headless browser, no access-control bypass, no tool installs. LSP was unavailable (`read xd://lsp` → "No such tool"; only `ast_edit` and `debug` are mounted), so source and entry judgments come from the opened text.

---

## Findings (each with verdict)

### F1 — S392: "the Antonian ending in 1706" conflates the execution with the movement's end — AGREE (registry scope cell); entry-heading part already resolved in the current tree

Evidence re-opened in this session (S392 PDF, direct plain GET HTTP 200, 985,805 bytes, 30 pages; printed page = PDF page − 6, article printed pp. 7–36):

- Batsîkama's own narrative, printed p. 27 (PDF leaf 21): "… o movimento de Dona Beatriz – mais conhecido pelo nome de antonismo, por causa de Santo António – só cessou depois de 1719."
- The block quotation on printed p. 32 (PDF leaf 26), introduced "William Graham Lister Randels conclui, em relação ao movimento antoniano, que:", ends "… mas a heresia só terminaria três anos depois com a conquista final de São Salvador por D. Pedro IV87 (quer dizer, em 1712)."
- Both statements are separate from the 1706 execution (see F2). So "the Antonian ending in 1706" is not what the source says, and the 1706 date marks the execution, not the movement's end.

Where the problem lives today:
- `corpus/SOURCES.md:421` (S392 row), scope cell (column 4): "… the Antonian ending in 1706, and the 1709-versus-1712 dispute …" — **the conflating phrase sits in the scope cell**. It is a registry cell other than status/recheck/used-by → append-only ⇒ a superseding row is required.
- The finding also named an entry heading "The Antonian movement (1704–1706)". That heading existed at the first round-56 claim commit (`git show 767040e:corpus/knowledge/civilizations/kongo-kingdom.md` → "The Antonian movement (1704–1706)"), but the current tree heading is **"The Antonian movement (from 1704)"** (`kotodama-shokunin/corpus/knowledge/civilizations/kongo-kingdom.md:85`), changed by the round-56 records commit `c8af23f` ("entry falsify fixes"). The entry heading part is **already resolved**; no entry change needed for F1.
- The finding's "teaches phrase / matching Gate Grounds" half is also already moot: the S392 teaches cell (`SOURCES.md:421` col 6) reads "... and a 1709 or 1712 final conquest" (no "1706 ending"), and the lesson Gate line at `corpus/lessons/round-56.md:57` has the same wording. Neither carries the conflating phrase today.

Fix: superseding row for S392 (draft at the end), scope cell corrected to "Kimpa Vita's execution in 1706 and the later, disputed end of the Antonian movement (after 1719 in Batsîkama's account, 1712 in the Randels block he quotes)".

### F2 — S392: p. 32 locator does not make Kimbangu Batsîkama's own assertion — AGREE (entry over-read)

Evidence (same PDF, re-opened):

- Batsîkama's own p. 27 narrative: "… isso aconteceu no dia 2 de julho de 1706 numa sexta-feira …" — no Kimbangu in that sentence (the word Kimbângu appears elsewhere on the page, in a separate sentence about Pedro IV seated at Kimbângu ordering her burned).
- The p. 32 block is credited to Randels ("William Graham Lister Randels conclui, em relação ao movimento antoniano, que:") and it is inside that block that "… no dia 2 de julho de 1706 em kimbangu …" appears, together with the "quer dizer, em 1712" endpoint.

So the current entry sentence "Batsîkama gives 2 July at Kimbangu (S392, p. 32)" fuses Batsîkama's authorship with the Kimbangu location that belongs to the quoted Randels block. Exact entry-sentence fix (old → new) in `corpus/knowledge/civilizations/kongo-kingdom.md:85`:

- OLD: `Gallo dates the sentence to Sunday 1 July 1706 (S380, relatione para. 136); Batsîkama gives 2 July at Kimbangu (S392, p. 32), and Farias places the execution in Mbanza Kongo (S381, p. 210): date and place stay contested (to-verify).`
- NEW: `Gallo dates the sentence to Sunday 1 July 1706 (S380, relatione para. 136); Batsîkama's own account gives 2 July 1706 (S392, p. 27), while the block quotation he credits to Randels places the execution at Kimbangu (S392, p. 32); Farias places it in Mbanza Kongo (S381, p. 210), so date and place stay contested (to-verify).`

(OLD was verified to be a verbatim substring of the current line 85; everything after the changed clause — "Farias follows the devotion into Brazil (S381, p. 210)." — is untouched.)

### F3 — S395: recorded capture does not support the artist credit — AGREE (registry cells: citation and teaches)

Evidence re-opened in this session:

- The row's recorded capture `20210208082447` (ordinary Wayback replay, HTTP 200 after transient 429 blocks, 20,104 bytes raw / 97,412 bytes decoded): page title "Power Figure (Nkisi N'Kondi: Mangaaka) | **Kongo peoples, Yombe group** | The Metropolitan Museum of Art"; details block "19th century Kongo peoples, Yombe group"; "Culture: Kongo peoples, Yombe group". **No artist/nganga credit anywhere.**
- The later capture `20230308010409` (ordinary Wayback replay, HTTP 200, 209,131 bytes): page title "Mangaaka Power Figure (Nkisi N'Kondi) | **Kongo artist and nganga, Yombe group** | The Metropolitan Museum of Art"; details block "Kongo artist and nganga, Yombe group … Second half of the 19th century". All four anchor quotes are present in this capture (verified normalized): "collaborative creations of Kongo sculptors and ritual specialists", "identified with Mangaaka, the preeminent force of jurisprudence", "Its crowning element is the distinctive mpu headdress worn by chiefs or priests.", "They document vows sealed, treaties signed".
- The live Met URL answers 429/bot challenge under a plain GET (challenge met, not passed), so the effective ordinary route is the 2023 capture.

Registry cells that are wrong (other than status/recheck/used-by), both in `corpus/SOURCES.md:424`: the citation cell's "artist credited as Yombe-Kongo artist and nganga" and the teaches cell's "The Met credits a Yombe-Kongo artist with an nganga". Fix: superseding row for S395 (draft below) citing the 2023 capture URL with the artist credit as served ("Kongo artist and nganga, Yombe group") and teaches opening "supersedes S395 — ".

---

## Drafted superseding SOURCES rows (11 columns; id left as `S4xx` for the L1; append-only)

Both rows below follow the registry contract (`corpus/SOURCES.md:9-12`: corrections are new rows whose teaches opens `supersedes S0NN —`; only status/recheck/used-by ever change in place). Status cell drafted as `queued` (as the S127–S131 precedents); the L1 sets `mined` + used-by when the entry cites the new id. Record rows this round take ids S481–S499 (claims.json export rule).

### S392 superseding row (fixes F1 scope cell; anchors/locators unchanged and re-verified)

```
| S4xx | Batsîkama, Patrício. 2021. "Evangelização, guerra civil no Kôngo e Ñsîmba Vita (Kimpa Vita)". *Sankofa: Revista de História da África e de Estudos da Diáspora Africana* 14(25): 7-36. ISSN 1983-6023; no DOI printed on the article or landing page. Stable ids: article https://revistas.usp.br/sankofa/article/view/187402 and the PDF at https://revistas.usp.br/sankofa/article/download/187402/173183 — https://revistas.usp.br/sankofa/article/download/187402/173183/497395 (direct plain request, HTTP 200, application/pdf, 985,805 bytes, 30 pages, read 2026-10-22; no challenge.) | paper | B | the 1665 campaign from the Kongo side (two days, field offices, the king's death), the post-1667 proclamation and election of kings at Bula and Kibangu, Daniel I's 1678 entry into Mbanza Kongo, Kimpa Vita's execution in 1706 and the later, disputed end of the Antonian movement (after 1719 in Batsîkama's account, 1712 in the Randels block he quotes), and the 1709-versus-1712 dispute over the final conquest. Not demography, trade volumes or material culture. (tier note: B — peer-reviewed article by a professor of Angolan history (ISPT, Luanda), arguing from Cadornega, Cuvelier and Randles; strong on Kongo-side names and sequence, partly reconstructive.) | p. 19: "É importante salientar que foi logo de manhã, por volta das 9 horas de 27 de Outubro de 1665, que aconteceu o primeiro confronto."; p. 22: "A sua ida a Mbânz'a Kôngo em 1678 como monarca foi acompanhada pelos militares Makela (Makaba)"; p. 24: "Visto que Mbânz'a Kôngo estava sem governo desde 1667, os reis eram proclamados ou eleitos pelos seus apoiantes em Kôngo dya Lemba (Bula) ou Kimbângu."; p. 32, in a block quotation credited to Randels 2002: "Já antes do assalto final que em 1709 D. Pedro IV lançou contra São Salvador, ainda ocupado por hereges rebeldes (antonianos)" | supersedes S392 — Gives the Kongo-side sequence and names: a first clash on 27 October 1665, elected kings at Bula and Kibangu, Daniel I's 1678 entry, and a 1709 or 1712 final conquest. | queued | 2026-10-22 | 365d | corpus/knowledge/civilizations/kongo-kingdom.md |
```

Gate-line draft for the new row (round-56 lesson format):

```
- S4xx — https://revistas.usp.br/sankofa/article/download/187402/173183/497395 — accessed 2026-10-22 — p. 19: "É importante salientar que foi logo de manhã, por volta das 9 horas de 27 de Outubro de 1665, que aconteceu o primeiro confronto.". Grounds: supersedes S392 — Gives the Kongo-side sequence and names: a first clash on 27 October 1665, elected kings at Bula and Kibangu, Daniel I's 1678 entry, and a 1709 or 1712 final conquest; Kimpa Vita's execution in 1706 is not the movement's end. Seat: ReviewCarriedS392S395.
```

Locator line (pasted verbatim from the round-57 tool, this session):

```
$ python3 -B reports/round-57/reopen-quote.py 'https://revistas.usp.br/sankofa/article/download/187402/173183/497395' 'É importante salientar que foi logo de manhã, por volta das 9 horas de 27 de Outubro de 1665, que aconteceu o primeiro confronto.'
LOCATED https://revistas.usp.br/sankofa/article/download/187402/173183/497395
```

### S395 superseding row (fixes F3 citation + teaches cells; anchors unchanged)

```
| S4xx | The Metropolitan Museum of Art. *Power Figure (Nkisi N'Kondi: Mangaaka)*, second half of the 19th century, Chiloango River region, Republic of the Congo or Cabinda, Angola; Kongo peoples, Yombe group; artist credited as Kongo artist and nganga, Yombe group. Object record 320053, accession 2008.30. — https://web.archive.org/web/20230308010409id_/https://www.metmuseum.org/art/collection/search/320053 (ordinary Wayback replay, HTTP 200, ~209,131 bytes; object essay and detail fields read. The recorded 20210208082447 capture carries no artist credit; the live host answers 429/bot challenge: challenge met, not passed.) | docs | A | minkisi practice at the Met's strongest example — collaboration between sculptor and ritual specialist, Mangaaka as the force of jurisprudence, the mpu headdress as chiefly regalia, and embedded metal as a record of transactions. (tier note: A — the holding museum's record and essay for this exact object; authoritative for the Met's description and attribution.) | essay, first paragraph: "collaborative creations of Kongo sculptors and ritual specialists"; essay, first paragraph: "identified with Mangaaka, the preeminent force of jurisprudence"; essay, second paragraph: "Its crowning element is the distinctive mpu headdress worn by chiefs or priests."; essay, second paragraph: "They document vows sealed, treaties signed" | supersedes S395 — The Met credits a Kongo artist and nganga from the Yombe group, reads Mangaaka as the force of jurisprudence, and names the mpu headdress and embedded metals as chiefly regalia and records. | queued | 2026-10-22 | 365d | corpus/knowledge/civilizations/kongo-kingdom.md |
```

Gate-line draft for the new row:

```
- S4xx — https://web.archive.org/web/20230308010409id_/https://www.metmuseum.org/art/collection/search/320053 — accessed 2026-10-22 — essay, first paragraph: "collaborative creations of Kongo sculptors and ritual specialists". Grounds: supersedes S395 — The Met credits a Kongo artist and nganga from the Yombe group, reads Mangaaka as the force of jurisprudence, and names the mpu headdress and embedded metals as chiefly regalia and records. Seat: ReviewCarriedS392S395.
```

Locator line (pasted verbatim from the round-57 tool, this session):

```
$ python3 -B reports/round-57/reopen-quote.py 'https://web.archive.org/web/20230308010409id_/https://www.metmuseum.org/art/collection/search/320053' 'collaborative creations of Kongo sculptors and ritual specialists'
LOCATED https://web.archive.org/web/20230308010409id_/https://www.metmuseum.org/art/collection/search/320053
```

---

## Residual risk and verification gaps

- Wayback availability is flaky: during this session web.archive.org intermittently answered 429 ("suspected abusive bot traffic") to plain GETs, including to the locator's own fetches; spaced retries eventually succeeded (the two LOCATED lines above were reproduced). If the L1's integration-time LOCATE run hits the same blocks, a retry after a pause is expected to clear them; this is environmental, not a source-content defect.
- S395's four anchors were verified present normalized in the 2023 capture; the live Met page (the previous row URL) answers 429/bot challenge, so the new row's effective route is the Wayback capture URL (same pattern as S400's row).
- S392 p. 22 anchor: the served text reads "makela makaba" without parentheses; the row renders "(Makaba)". Under the lane's own normalization (reopen-quote.py `normalise` strips the parentheses) this locates and was carried by the round-56 falsify seat; flagged here as an observation only, not an actionable finding.
- The round-56 lesson's Gate lines for S392/S395 (round-56.md:57/60) carry the old teaches/grounds text; lessons are append-only history, so they are not edited — the superseding rows' Gate lines above are for the new rows' own lesson entry.
- No other row slices (S393/S394/S396/S397 etc.) were re-checked here; they were not in this seat's assignment. No O-tool runs, no LSP (unavailable as noted).
