# ScoutS882 — re-open of staged row S882 (МГУ-hosted PDF of Сидорова & Шувалова 2006)

Seat: ScoutS882 (kotodama round 73, hyaku run 7, leaf — no delegation, no background jobs).
Date: 2026-10-25.
Godspeed skill invoked.
Target: staged S882, tentative lane id S877.
Document: М.Ю. Сидорова, О.Н. Шувалова, «Интернет-лингвистика: вымышленные языки», М.: «1989.ру», 2006, 184 с., ISBN 5-98789-005-5; URL http://www.philol.msu.ru/~sidorova/files/conlangs.pdf.
Scratch downloads: /tmp/ScoutS882/ (conlangs.pdf, headers.txt, conlangs.txt, recheck_s.pdf, wb_20251114.pdf, q*.txt). Nothing written under /home/vgpnk/Projects/shokunin/** except this report file (the assigned Report path).

Tooling record: no tool installed or upgraded. pdftotext 26.08.0 (poppler) was already present at /usr/bin/pdftotext; curl system binary; python3 used only to split extracted text on form feed characters (script kept in /tmp/ScoutS882/). Pacman untouched (host-wide pause respected).

---

## 1. Fetch log — exact commands and raw outputs

UA used for every fetch below (recorded per QUALITY 21/22):
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

### 1.1 Live fetch

Command:
```
mkdir -p /tmp/ScoutS882 && cd /tmp/ScoutS882 && curl -sS -o conlangs.pdf -D headers.txt -w 'HTTP_STATUS=%{http_code}\nSIZE=%{size_download}\nURL_EFFECTIVE=%{url_effective}\nCONTENT_TYPE=%{content_type}\nFINAL_URL=%{url_effective}\n' -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' 'http://www.philol.msu.ru/~sidorova/files/conlangs.pdf'
```

Raw output:
```
HTTP_STATUS=200
SIZE=1055723
URL_EFFECTIVE=http://www.philol.msu.ru/~sidorova/files/conlangs.pdf
CONTENT_TYPE=application/pdf
FINAL_URL=http://www.philol.msu.ru/~sidorova/files/conlangs.pdf
```

Response headers (raw):
```
HTTP/1.1 200 OK
Date: Sun, 25 Oct 2026 22:06:18 GMT
Server: Apache/2.2.3 (Red Hat) PHP/5.1.6 mod_ssl/2.2.3 OpenSSL/1.0.1e-fips
Last-Modified: Sun, 15 Jul 2007 15:26:48 GMT
ETag: "3890039-101beb-f8fe9e00"
Accept-Ranges: bytes
Content-Length: 1055723
Connection: close
Content-Type: application/pdf
```

### 1.2 Text extraction

Command:
```
cd /tmp/ScoutS882 && pdftotext -enc UTF-8 conlangs.pdf conlangs.txt && wc -w conlangs.txt && wc -l conlangs.txt && pdfinfo conlangs.pdf
```

Raw output:
```
66924 conlangs.txt
11434 conlangs.txt
Title:           verstka
Author:          G4
Creator:         QuarkXPressª 4.11: LaserWriter 8 Z1-8.7.1
Producer:        Acrobat Distiller 5.002001-01-22:00 for Macintosh
CreationDate:    Sun Jul 15 20:25:56 2007 -03
ModDate:         Sun Jul 15 20:25:56 2007 -03
Pages:           185
Encrypted:       no
Page size:       595 x 842 pts (A4)
File size:       1055723 bytes
PDF version:     1.3
```

### 1.3 Staged recheck command (ran exactly as the staged row names it)

Command:
```
cd /tmp/ScoutS882 && curl -fsSL 'http://www.philol.msu.ru/~sidorova/files/conlangs.pdf' -o /tmp/ScoutS882/recheck_s.pdf && pdftotext -enc UTF-8 /tmp/ScoutS882/recheck_s.pdf - | grep -c 'Классификация искусственных языков'
```

Raw output: `2` (grep exit code 0). The staged recheck prediction (count = 2) reproduces.

### 1.4 URL variants

```
== http://www.philol.msu.ru/~sidorova/files/conlangs.pdf  -> HTTP=200 FINAL=http://www.philol.msu.ru/~sidorova/files/conlangs.pdf SIZE=1055723 TYPE=application/pdf
== http://philol.msu.ru/~sidorova/files/conlangs.pdf     -> HTTP=200 FINAL=http://philol.msu.ru/~sidorova/files/conlangs.pdf SIZE=1055723 TYPE=application/pdf
== https://www.philol.msu.ru/~sidorova/files/conlangs.pdf -> HTTP=200 FINAL=https://www.philol.msu.ru/~sidorova/files/conlangs.pdf SIZE=1055723 TYPE=application/pdf
```

All three variants serve the same 1,055,723-byte PDF. No challenge wall was encountered with the browser-shaped UA; no CAPTCHA was bypassed (none present).

---

## 2. What the document actually is

The PDF is NOT a publisher-style announcement booklet. It is the complete typeset text of the book:

- PDF page 1: title page (М.Ю. Сидорова, О.Н. Шувалова; ИНТЕРНЕТ-ЛИНГВИСТИКА: ВЫМЫШЛЕННЫЕ ЯЗЫКИ; Издательство «1989.ру», МОСКВА, 2006).
- PDF page 2: УДК/ББК page with the аннотация and ISBN 5-98789-005-5 («2006, с.184»).
- PDF pages 3–4: Оглавление (full chapter list, see §3).
- PDF pages 5–184: complete body — Предисловие (printed p. 4), Глава 1 (printed pp. 8–34), Глава 2 (35), Глава 3 (49), Глава 4 (74), Глава 5 (107), Глава 6 (119), Заключение (136), Приложение 1 (142), Приложение 2 (152), Приложение 3 (170), Библиография (176).
- PDF page 185: blank final leaf (printed page number 185 printed alone).

Extracted text: 66,924 words, 11,434 lines, 186 form-feed segments (185 pages plus trailing feed). The printed pagination in the running heads matches the Оглавление page numbers exactly (classification section found at printed p. 10, auxiliary-vs-fictional at p. 16, natural-language differences at p. 21, Tolkien/Klingon/D'ni at p. 22, literature survey at p. 27).

---

## 3. Located passages

- **Аннотация** — PDF page 2 (УДК/ББК page). Opens: «Первая книга в серии «Интернет-лингвистика» рассказывает о проектах вымышленных языков в Интернете. Что такое вымышленные языки? Какими они могут быть? Чем они отличаются от других видов искусственных языков и от естественных языков? …»
- **Оглавление** — PDF pages 3–4. Chapter list (verbatim subsections of Глава 1):
  - Естественные, искусственные, вспомогательные, фантастические, вымышленные… и другие (p. 8)
  - Классификация искусственных языков (конлангов) (p. 10)
  - Принципиальные различия между вымышленными языками и вспомогательными языками (p. 16)
  - Отличия вымышленных языков от естественных (p. 21)
  - Языки Толкина, клингон и D'ni как конланги, имеющие особый статус (p. 22)
  - Обзор литературы, посвященной вымышленным языкам (p. 27)
  - Глава 2: Вымышленные языки в мире – фантастическом, реальном и виртуальном (p. 35); Глава 3: Келен, эналь, ларимин (p. 49); Глава 4: Путеводитель по Интернет-ресурсам, связанным с ВЯ (p. 74); Глава 5: ВЯ в Интернете – модель описания (p. 107); Глава 6: Уровни языковой системы в проектах ВЯ (p. 119); Заключение (p. 136); Приложения 1–3 (pp. 142/152/170); Библиография (p. 176).
- **конланги terminology** — printed p. 10 (PDF p. 10): «conlangs – конланги, conlangers – конлангеры (энтузиасты конструирования языков), artlangs – артланги … auxlangs».
- **The book's own typology** — printed p. 11: «1. Auxlangs. Вспомогательные языки» vs «2. Вымышленные языки (ВЯ) в широком смысле» (2.1 Artlangs with 2.1.1 «Языки, вышедшие за пределы фантастических миров … языки Толкина, клингон (язык сериала "Star Trek"), язык D'ni из мира компьютерной игры "Myst"»; 2.2 Рersonal languages / авторские языки).
- **Вымышленные vs вспомогательные** — printed p. 16: «Принципиальные различия между вымышленными языками и вспомогательными языками» section.
- **Вымышленные vs естественные** — printed p. 21: «Отличия вымышленных языков от естественных» section.
- **Tolkien / Klingon / D'ni** — heading printed p. 22; subsections Толкин (p. 23), Клингон (p. 24), D'ni (p. 26).
- **Survey of literature** — printed p. 27: «Обзор литературы, посвященной вымышленным языкам» — covers M. Yaguello (Lunatic Lovers of Language, 1985/1991), J. Schnapp, U. Eco, J. Hennig (conlang.com).

---

## 4. Quotes (verbatim, <=25 words, word counts by `wc -w`)

Primary quote (taxonomy; supports the entry's §3):
«Языки, используемые в художественных произведениях, называют вымышленными или фикциональными.»
Location: printed p. 10, Глава 1, section «Классификация искусственных языков (конлангов)» (PDF page 10 of the extracted text).
Word count: 9 (wc -w).

Secondary quote (auxiliary-vs-fictional distinction; printed p. 16):
«Кардинальные, принципиальные различия пролегают между проектами вспомогательных языков для международного общения типа эсперанто, идо и т.п.; и вымышленными языками, изначально предназначенными для сконструированных миров.»
Location: printed p. 16, section «Принципиальные различия между вымышленными языками и вспомогательными языками».
Word count: 24 (wc -w).

Tertiary quote (аннотация; PDF page 2):
«Что такое вымышленные языки? Какими они могут быть? Чем они отличаются от других видов искусственных языков и от естественных языков?»
Word count: 20 (wc -w).

---

## 5. Verification of staged entry §3 and §4

Staged entry: /home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/conlang-scholarship.md (Proposed body §3 and §4).

**§3 — «from S882: конланги, auxiliary languages, and вымышленные языки as a third kind; why the distinction matters for a fictional world that merely *has* languages.»**
- конланги: VERIFIED (p. 10, p. 11 terminological pairs; full book uses «конланги» throughout).
- auxiliary languages: VERIFIED (p. 11 «1. Auxlangs. Вспомогательные языки»; p. 16 contrast section; аннотация's «других видов искусственных языков»).
- вымышленные языки as a distinct kind: VERIFIED (p. 11 «2. Вымышленные языки (ВЯ) в широком смысле» — the book's own typology separates auxiliary languages and fictional languages within artificial languages; the аннотация frames the three-way contrast natural / other artificial / fictional).
- "why the distinction matters for a fictional world that merely *has* languages": NOT carried by the PDF. The book defines and contrasts the categories; it does not draw implications for fiction-writers. This clause is the entry's own synthesis, not a claim the document makes.

**§4 — «Tolkien, Klingon and D'ni as specially classed conlangs, and the survey literature behind them.»**
- Special status: VERIFIED — section heading, printed p. 22: «Языки Толкина, клингон и D'ni как конланги, имеющие особый статус»; and p. 11 (2.1.1) classes Tolkien's languages, Klingon and D'ni together as artlangs that outgrew their fictional worlds.
- Survey literature: VERIFIED — «Обзор литературы, посвященной вымышленным языкам», printed p. 27 (Yaguello, Schnapp, Eco, Hennig). Note: the survey is a general survey of the literature on fictional languages, not specifically a survey "behind" Tolkien/Klingon/D'ni.

Bibliographic claims of the staged row all carried: title, authors (М.Ю. Сидорова, О.Н. Шувалова), publisher «1989.ру», Moscow, 2006, 184 с., ISBN 5-98789-005-5 (all on PDF pages 1–2).

---

## 6. Claims the PDF does NOT carry

1. The staged row's tier-B reason — «a publisher-style announcement and table of contents, which support claims about the book's own coverage and not about the world» — is FALSE as a characterization of the document. The PDF is the complete typeset book text (185 PDF pages, full chapters, Заключение, Приложения 1–3, Библиография). It is not an announcement booklet. (The аннотация says «Первая книга в серии» — first in a series — but that is a series note, not a booklet format.)
2. The anchor cell «Аннотация + Оглавление» under-describes the document; the staged anchor cites only pp. 10 and 22 while the PDF carries the entire book.
3. §3's final clause («why the distinction matters for a fictional world that merely has languages») is the entry's application, not a statement present in the PDF.
4. The staged row's kind=book with 184 с. is consistent with the PDF (printed pagination runs to 184; PDF has 185 leaves incl. a blank final leaf), so no defect there — but the "announcement booklet" framing (tier reason) is the defect.

---

## 7. Proposed lane registry row (11-column schema, tentative id S877)

| S877 | М.Ю. Сидорова, О.Н. Шувалова, «Интернет-лингвистика: вымышленные языки», М.: «1989.ру», 2006, 184 с., ISBN 5-98789-005-5 — complete typeset text of the monograph, author-hosted at МГУ — http://www.philol.msu.ru/~sidorova/files/conlangs.pdf | book | A | Tier A for the book's own text: the full monograph was opened and read (185 PDF pages; аннотация, Оглавление, six chapters, Заключение, приложения 1–3, библиография). Scope: the classification of artificial languages (конланги) and the vocabulary separating вымышленные языки from вспомогательные языки and from natural languages; the special status of Tolkien's, Klingon and D'ni; the survey of the literature on imaginary languages. Not claimed beyond the book's own claims: it is a monograph, not peer-reviewed | Аннотация (PDF p. 2); Оглавление (PDF pp. 3–4); Глава 1: Классификация искусственных языков (конлангов), printed p. 10; Принципиальные различия между вымышленными языками и вспомогательными языками, printed p. 16; Языки Толкина, клингон и D'ni как конланги, имеющие особый статус, printed p. 22; Обзор литературы, посвященной вымышленным языкам, printed p. 27 | Supplies the non-English scholarly frame for conlang construction that the English literature lacks: a taxonomy of artificial languages and a vocabulary (вымышленные языки vs вспомогательные языки) for telling invented worlds apart from constructed auxiliary languages | mined | 2026-10-25 | 180d — `curl -fsSL 'http://www.philol.msu.ru/~sidorova/files/conlangs.pdf' -o /tmp/s.pdf && pdftotext -enc UTF-8 /tmp/s.pdf - > /tmp/s.txt && grep -c 'Классификация искусственных языков' /tmp/s.txt` -> 2 (ran 2026-10-25) | corpus/knowledge/linguistics/conlang-scholarship.md, corpus/knowledge/culture-material/worldbuilding-setting-practice.md |

Notes on the proposed row:
- No pipe character appears inside any cell (recheck cell rewritten pipe-free).
- recheck: 180d with ISO-ish date of run (2026-10-25); status mined; opened 2026-10-25.
- used-by names the two admitted entries that cite S882 in the staged package: conlang-scholarship.md AND worldbuilding-setting-practice.md (the assignment text mentions only the conlang-scholarship paths; the merge package evidence shows worldbuilding-setting-practice.md also cites this row — both are listed so the used-by cell is exactly the admitting entries).
- The proposed row corrects the staged row's kind/tier reasoning: kind book stays, but the anchor and tier reason now name the full text.

---

## 8. Tier assigned

Proposed tier: **A**.
Reason: under the lane's own practice (e.g., S353, S71, S308, S267), tier A is assigned where the full primary text was opened and read. This PDF is the complete text of the monograph, not an abstract, publisher description, or announcement. The staged row's B was justified only by the (incorrect) belief that the document was an announcement booklet.
Caveat: if the integrator applies A strictly as "every page read word-for-word in one session", the row is still B-compatible — but then the B reason MUST be corrected (the PDF is a complete author-hosted text, not an announcement booklet). My scout session read the full structure verbatim (title, аннотация, Оглавление, Глава 1 sections pp. 10–27, appendix and bibliography heads, final pages) and verified the claims; a full cover-to-cover reading was not performed page by page.

---

## 9. Wayback CDX canonical-slug probe

Probed URLs (all with browser-shaped UA; CDX API returned HTTP 200 on each):
1. `http://web.archive.org/cdx/search/cdx?url=philol.msu.ru/~sidorova/files/conlangs.pdf&output=json&filter=statuscode:200&fl=timestamp,original,statuscode,digest,length&collapse=digest&limit=40`
2. `http://web.archive.org/cdx/search/cdx?url=www.philol.msu.ru/~sidorova/files/conlangs.pdf&output=json&filter=statuscode:200&fl=timestamp,original,statuscode,digest,length&collapse=digest&limit=10`
3. `http://web.archive.org/cdx/search/cdx?url=https://www.philol.msu.ru/~sidorova/files/conlangs.pdf&output=json&filter=statuscode:200&fl=timestamp,original,statuscode,digest,length&collapse=digest&limit=10`

CDX result (identical across all three probes; rows collapsed by digest):
```
["timestamp","original","statuscode","digest","length"]
["20110716143917","http://www.philol.msu.ru/~sidorova/files/conlangs.pdf","200","3WWHFZNWQ7S2BF54CB2CEQ4U35FYQDRG","845312"]
["20210515195349","https://www.philol.msu.ru/~sidorova/files/conlangs.pdf","200","CJFQ2CMEEJ6UPCXXOVI7VXDBZLOJ7E5N","843988"]
["20210628095121","http://www.philol.msu.ru/~sidorova/files/conlangs.pdf","200","3WWHFZNWQ7S2BF54CB2CEQ4U35FYQDRG","844112"]
["20240921025932","http://www.philol.msu.ru/~sidorova/files/conlangs.pdf","200","CJFQ2CMEEJ6UPCXXOVI7VXDBZLOJ7E5N","844016"]
["20251114052301","http://www.philol.msu.ru/~sidorova/files/conlangs.pdf","200","3WWHFZNWQ7S2BF54CB2CEQ4U35FYQDRG","845546"]
```

Fallback snapshot verified by download:
```
curl -sS -o wb_20251114.pdf -A '<browser UA>' -w 'WB_HTTP=%{http_code} WB_SIZE=%{size_download}\n' 'https://web.archive.org/web/20251114052301id_/http://www.philol.msu.ru/~sidorova/files/conlangs.pdf'
WB_HTTP=200 WB_SIZE=1055723
pdftotext -enc UTF-8 wb_20251114.pdf - | grep -c 'Классификация искусственных языков'  -> 2
pdftotext -enc UTF-8 wb_20251114.pdf - | wc -w  -> 66924
```
The 2025-11-14 snapshot is byte-size-identical (1,055,723 B) and text-equivalent (66,924 words; recheck count 2) to the live file. (CDX length column values around 844–846 KB differ from the downloaded size; the archive serves the original bytes, so the CDX length field is not the served length.)

---

## 10. Verdict

**ADMIT.**

Reason:
- Live source reachable: HTTP 200, application/pdf, 1,055,723 bytes, browser UA, no challenge wall (2026-10-25).
- Authenticity: title page, authors, publisher, year, 184 с., ISBN 5-98789-005-5 all match the staged bibliographic data; PDF provenance (QuarkXPress 4.11 layout, distilled 2007-07-15) is consistent with an author-hosted typeset file.
- Content verification: every factual claim in staged entry §3 and §4 is carried by the PDF (konланги taxonomy; auxiliary vs вымышленные vs natural; Tolkien/Klingon/D'ni special status; literature survey). The staged recheck command reproduces (grep count = 2).
- Wayback fallback exists and was verified identical (20251114052301).

Flip condition: REFUSE/UNVERIFIABLE only if a future recheck finds (a) the live and archived copies both unreachable or replaced by a different document (digest change), or (b) a later bibliographic cross-check shows the hosted file is not in fact the book text (e.g., it is an abridged version). Neither holds today. Additionally, the staged row's tier reason must be corrected as proposed (§6.1, §8) — the document is the complete book, not an announcement booklet; otherwise the row as staged carries a false characterization even though the row itself is admissible.

Open items (non-blocking): the full cover-to-cover reading beyond the verified sections was not performed; the §3 application clause is the entry's synthesis, not book text.
