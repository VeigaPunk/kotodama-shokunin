# ScoutReopenS878 — wave 2 FALSIFY, row S878 (lane rev 0316b8883b4f8d44b8efd720140e7f52f734a102)

## Verdict: ADMIT-STANDS

No BLOCKER and no MAJOR finding. Two MINOR findings. Neither touches a gate leg (bytes, quote, locator, word count, URLs, row shape).

Work dir: /tmp/ScoutReopenS878/ (live-browser.pdf, live-curl.pdf, wb-browser.pdf, wb-curl.pdf, row.txt, cdx.txt, journal pages). Nothing was written under the fleet root or lane tree except this report. No tools were installed.

## 1. Fetch matrix (access date 2026-10-25)

Browser UA = `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`. Curl UA = `curl/8.7.1`.

```
live browser    code=200 size=959171 https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955
live curl       code=200 size=959171 (same URL)
wayback browser code=200 size=959171 https://web.archive.org/web/20240415141632id_/https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955
wayback curl    code=200 size=959171 (same URL)
sha256 all four: 9f745ddaccdbccbf254c5d890cd5b621ab241ea6d6de0219287c2e0c075ed07c
```
- The evidence file S878.txt records sha256 `9f745ddaccdbccbf254c5d890cd5b621ab241ea6d6de0219287c2e0c075ed07c`, bytes 959171, HTTP 200, UA browser. **Equal on all four fetches: no drift.**
- Both UAs are served; there is no UA gate in either direction. The live host answers via `server: ddos-guard` (cookies set), but there is no challenge.
- The Wayback `id_` capture is `content-type: application/pdf`, `content-length: 959171`, `x-archive-orig-content-length: 959171`. It carries the same bytes as the live fetch (sha equal), which backs the row's "same bytes".
- Wayback CDX for the canonical slug (`cdx/search/cdx?url=journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955`, curl/8.7.1, HTTP 200, 75 B): the only capture is `20240415141632 200 application/pdf DFBD4NO3SA2CSNANACJS2KGKU23VYWWM 861874`. The CDX length is the compressed WARC record, so it is not comparable to 959171. The named timestamp exists and is a 200 PDF.

## 2. Quote
```
Q='the author examines the existing classifications of constructed languages and attempts to establish a connection between purposes of their creation and their linguistic features'
echo -n "$Q" | wc -w        -> 24   (<= 25 OK; evidence quote-words: 24 matches)
pdftotext -enc UTF-8 | whitespace-collapse | grep -o -F "$Q" | wc -l
   live-browser.pdf -> 1 ; wb-browser.pdf -> 1 ; page 1 only (-f 1 -l 1) -> 1
```
- Location: PDF p.1 = journal p.455, in the English Abstract ("Abstract. The research aims … In order to achieve this goal, the author examines the existing classifications …").
- It is verbatim (whitespace-collapsed) in both the fresh live body and the capture body.
- The evidence file's locator "Abstract, p. 455" is correct.

## 3. Bibliographic fields
- `pdfinfo`: Pages 13. Page 1 header: "2022 Vol. 13 No. 2 455–467", "DOI: 10.22363/2313-2299-2022-13-2-455-467", and the English title "Constructed Languages as Semantic and Semiotic Systems".
- The DOI string appears 3 times and `455–467` or `455—467` 15 times in the text. Vol. 13(2), 2022 is confirmed.
- The Russian title «Искусственные языки как семантические и семиотические системы» appears on PDF p.2 (the Russian title page and abstract). The journal's Russian series name «Теория языка. Семиотика. Семантика» appears in the p.13 citation line. The row's cells are correct.

## 4. Registry row shape
```
awk -F'|' '{print NF}'  on SOURCES.md line 833 -> 13
```
- 13 fields means 11 cells, matching the header `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |` (line 28).
- Cell contents: `S878 | source | paper | B | scope | anchor | teaches | mined | 2026-10-25 | 180d | corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md`.
- The sibling rows S876..S880 all have NF=13, status mined, opened 2026-10-25, recheck 180d. Used-by is the main entry for S876 and S877, and the amend file for S878..S880. That is consistent with S878 being cited only in the amend file.
- Used-by check: the amend file cites S878 at lines 3, 18, 20, 22, 24, 26, 28, 30, 32, 76 and 78. The main entry file has no S878 hit. Used-by is right.
- Recheck: 180d is a value already used by 226 other rows, so it is a valid convention.
- Status: the registry says `mined`, and the Gate row in lessons/round-73.md says `admitted`. These are two different vocabularies for two different tables. I count this as no defect.

## 5. Anchor cell
- The anchor cell contains the evidence quote verbatim (24 words), plus "Abstract, p. 455 (13-page PDF)", the HTTP 200 and 959171-byte statement, and "capture 20240415141632 (same bytes), both carrying the span". All of it is verified above.
- The Gate row in lessons/round-73.md line 20 carries the same quote, locator "Abstract, p. 455", HTTP 200, 959171 B, sha prefix `9f745ddaccdbccbf…` (a prefix of the true sha), and the browser UA. It matches the fresh measurement.

## 6. Source-cell URLs
- Live URL: 200 (both UAs), 959171 B.
- Wayback `20240415141632id_` URL: 200 (both UAs), 959171 B, and the quote is found in the capture body.

## 7. Scope and tier text
- The "lexical, syntactic and morphological features" wording matches the Abstract ("lexical, syntactic, morphological and other features").
- The teaches cell is supported by the body text:
  - "scale rather than a binary system": found.
  - "a priori / a posteriori" dichotomy: found.
  - Eurocentrism "even in a priori languages": found. The Abstract says both a priori and a posteriori languages by European-language speakers show it.

### MINOR-1 — "Russian-language treatment" in the scope cell is imprecise
- The article body is English. The PDF is bilingual only in apparatus: Russian title page, abstract and keywords on p.2, author note on p.13. Cyrillic lines per page: p4=0, p6=0, and 1–6 elsewhere.
- The cell calls it a "peer-reviewed Russian-language treatment". Accurate wording would be "English-language article in a Russian journal, with a Russian title page and abstract".
- Reproduce: `pdftotext -f 4 -l 4 live-browser.pdf - | grep -c '[а-яА-Я]'` → 0; the body quotes are English.
- It does not change the tier, the quote or the claim.

### MINOR-2 — "peer-reviewed" is not evidenced in the capture
- The PDF has no article-level peer-review statement. It carries only "Article history: Received: 01.06.2021 Accepted: 1.03.2022"; a grep for peer or reviewer finds only an unrelated "peer-to-peer".
- Journal-level evidence exists but is not in S878.txt. `/about/editorialPolicies` returned 200 for curl/8.7.1 and says "A double-blind peer review method is mandatory for processing of all scientific manuscripts".
- So the claim is true at journal level. The evidence capture and anchor do not carry it, so it is a policy claim, not an article-level one.

### Tier B and "not a field consensus"
- Neither is overclaimed. The row labels the article as one author's framework.

## 8. Could not check
- The archive capture's response headers, beyond content-type and lengths, were not examined. Its WARC digest was not compared, only the sha256 of the delivered bytes.
- I did not verify the amend file's other section and page citations (§ pp. 457–459, Conclusion p. 464). I confirmed only that the Correlation heading is on PDF p.4 and that the Abstract is on p.1. The conclusion quote and "68 languages" claims in the amend file are outside this seat's scope (the S878 row, evidence and Gate row).
- I did not check for a retraction or erratum on the DOI landing page.
- The Wayback CDX probe was single-slug. Only one capture exists, so I did not probe URL variants such as http or no-www.
