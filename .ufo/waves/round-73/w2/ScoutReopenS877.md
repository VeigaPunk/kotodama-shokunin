# ScoutReopenS877 — wave 2 FALSIFY: registry row S877 / evidence S877.txt / Gate row

Lane revision attacked: 0316b8883b4f8d44b8efd720140e7f52f734a102 (read via `git show` and a throwaway clone `/tmp/tmp.UEq46X0I41/lane`; lane tree not mutated). Downloads: `/tmp/ScoutReopenS877/` (conlangs.pdf x5 + Wayback x2 + CDX text). Tools installed: none.

## VERDICT: ADMIT-STANDS

No failing field. The registry row's 11 cells parse, the anchor quote is verbatim in the freshly fetched body at printed p. 10, the sha256 and size are equal to the evidence file, both URLs resolve, and the Wayback capture holds the same bytes. Four MINOR defects (below) leave the admitted statement true. No BLOCKER and no MAJOR.

## 1. Fresh re-open — status, bytes, sha256 (all per request)

Evidence file S877.txt records: HTTP 200, 1055723 B, sha256 `e512a20dd3eef097ed403bd4191545dea1147279d82b7cced32aaa6037ca595a9`, UA Mozilla/5.0 (X11; Linux x86_64) … Chrome/130.0 Safari/537.36.

| request | UA | status | bytes | sha256 |
|---|---|---|---|---|
| GET http://www.philol.msu.ru/~sidorova/files/conlangs.pdf | browser-shaped Chrome/130.0 | 200 | 1055723 | e512a20d…ca595a9 |
| same | curl/8.7.1 | 200 | 1055723 | e512a20d…ca595a9 |
| GET https://www.philol.msu.ru/~sidorova/files/conlangs.pdf | browser-shaped | 200 | 1055723 | e512a20d…ca595a9 |
| same | curl/8.7.1 | 200 | 1055723 | e512a20d…ca595a9 |
| GET https://web.archive.org/web/20260208005339id_/https://www.philol.msu.ru/~sidorova/files/conlangs.pdf (the row's named capture) | browser-shaped | 200 (HTTP/2, memento-datetime Sun, 08 Feb 2026 00:53:39 GMT) | 1055723 | e512a20d…ca595a9 |
| same | curl/8.7.1 | 200 after one retry; the first try returned `curl: (7) Failed to connect to web.archive.org:443` (transient, status 000) | 1055723 | e512a20d…ca595a9 |

- **Drift:** none. Fresh sha256 equals the evidence line, byte for byte, in all six legs; `cmp live_browser.bin wb_browser.bin` printed `identical-live-wb`.
- **UA gating:** none either way for this host or for Wayback. The server is Apache/2.2.3, `Last-Modified: Sun, 15 Jul 2007 15:26:48 GMT`, `Content-Type: application/pdf`.
- The row's "capture 20260208005339 (same bytes)" claim is TRUE.
- **CDX probe** (`web.archive.org/cdx/search/cdx?url=philol.msu.ru/~sidorova/files/conlangs.pdf&matchType=exact`, both UAs, 200, 7875 B each, identical output): the row `20260208005339 https://www.philol.msu.ru/~sidorova/files/conlangs.pdf 200 3WWHFZNWQ7S2BF54CB2CEQ4U35FYQDRG` exists. The slug has many other captures from 2011 to 2026; some have status `-` (revisit records, 507–696 B). The named capture is a real 200 record.

## 2. Quote located verbatim in the fresh body

Quote: `Языки, используемые в художественных произведениях, называют вымышленными или фикциональными.`

- `printf '%s' <quote> | wc -w` → **9** (cap 25: pass). This matches the lesson's "S877 9".
- Whitespace-collapsed search in `pdftotext -enc UTF-8` output (the evidence file's method): **1 hit**, on PDF page 10. The context is "…Искусственные языки, сконструированные для конкретных целей, также получают ряд терминологических обозначений. Языки, используемые … фикциональными. Те, которые сконструированы для обеспечения международной коммуникации…"
- The text of the live PDF and the text of the Wayback PDF are identical (`cmp full.txt wb.txt` → `text-identical`).
- `pdftotext -layout -f 10 -l 10`: the page header reads "Page 10" and the printed folio at the bottom is `10`. PDF page = printed page for the body (printed p. 12 is PDF page 12; the last PDF page is 185, a blank numbered 185). **Printed p. 10 holds the quote: confirmed.** The quoted sentence sits in the block paragraph that opens "«Искусственный язык – это язык, который намеренно сконструирован…»".

## 3. Registry row S877 (SOURCES.md line 832 at 0316b88…)

- `awk -F'|' 'NR==832{print NF}'` → **13** (empty lead + 11 cells + empty tail): PASS. Cells in order: id, source, kind=book, tier=B, scope, anchor, teaches, status=mined, opened=2026-10-25, recheck=180d, used-by=`corpus/knowledge/linguistics/conlang-scholarship.md`.
- Anchor cell contains the evidence quote verbatim (Python `Q in cell` → True).
- Source cell URLs: `http://www.philol.msu.ru/~sidorova/files/conlangs.pdf` (live, 200) and the Wayback `id_` URL (200, quote present: PDF text identical). Both resolve.
- recheck 180d is the same value as the neighbouring rows 829, 831, 833–835 (830 is 90d). used-by: the file exists, and it is the only file that cites S877 (the amend file cites S879, not S877). status `mined` is consistent with that use.
- Imprint: the book's own copyright page says "2006, с.184" and ISBN 5-98789-005-5, matching the source cell. Publisher «1989.ру», Moscow, matches.

## 4. Tier/scope text against the opened document

- "Full typeset text … not an announcement booklet": TRUE. It is a 185-page PDF (pdfinfo `Pages: 185`), with a title page, annotation, TOC, preface, chapters 1–6, a conclusion, three appendices and a bibliography.
- The scope contents all exist in the book:
  - the class typology (printed p. 11, "мы принимаем следующую типологию");
  - the вымышленные-vs-вспомогательные section (printed p. 16);
  - "Языки Толкина, клингон и D'ni как конланги, имеющие особый статус" (printed p. 22);
  - the literature survey "Обзор литературы, посвященной вымышленным языкам" (printed p. 27);
  - "taxonomy is one classification among several it surveys": TRUE. pp. 12–15 survey Rosenfelder, Henning, Kuznetsov, Harrison and Capuzzo;
  - the "volume rule": Henning's volume classification (printed pp. 12–13).
- "Monograph, not peer-reviewed": the front matter gives no peer-review statement and the PDF has `Title: verstka`, `Producer: Acrobat Distiller` (a typeset layout). I cannot prove a negative, but it is not contradicted.
- I found nothing in the scope cell that the book does not say.

## 5. Findings

**F1 — MINOR. The Gate quote is not the authors' own words, but the row frames it as the book's own framing.** The quoted sentence is part of a block quote the authors give in Russian translation: `«Искусственный язык – это язык, который намеренно сконструирован…»1 (http://www.rickharrison.com/language/faq.txt)`. Footnote 1 on printed p. 10 gives the English original (verified in `pdftotext -layout -f 10 -l 10`): "Those used in works of fiction are called imaginary languages or fictional languages." The tier-B reason opens "Tier B for the book's own framing: the classification of artificial languages…". The book's own typology starts at printed p. 11 (1 Auxlangs / 2 ВЯ / 2.1 Artlangs / 2.2 Personal languages). The quote proves the sentence is printed on p. 10, which is true, but the row and the Gate do not tell a reader that the sentence is a translated citation of Rick Harrison's FAQ. A reader who takes it as Sidorova & Shuvalova's definition would misattribute it. Nothing in conlang-scholarship.md quotes this sentence (grep of `фикциональн` in the knowledge files → no hits), so the misattribution has no downstream carrier today. Suggested fix: add "(quoting Harrison's FAQ, fn. 1)" to the anchor, or pick an authors'-own sentence from p. 11.

**F2 — MINOR. The locator names the wrong heading level.** The Gate row and the anchor cell say "Глава 1 «Классификация искусственных языков (конлангов)»". Per the TOC (PDF p. 3), Глава 1 is «Естественные, искусственные, вспомогательные, фантастические, вымышленные… и другие». «Классификация искусственных языков (конлангов)» is the first section heading inside it (printed p. 10). Reads as if it were the chapter title. The page number is right.

**F3 — MINOR. The recheck procedure does not reproduce under `-layout` as literally written.** conlang-scholarship.md line 6 says: "for S877, re-run `pdftotext -layout` and re-find the quote on the printed page number given" (line 4 also says "text read with `pdftotext -layout`"), but S877.txt records `extract: pdftotext -enc UTF-8` (no `-layout`). Reproducing command (the quote is split across a hyphenated line break, "на-/зывают"):

```
python3 - <<'E'   # whitespace-collapsed exact-quote search, per pdftotext mode
plain  collapsed-hit 1 pages [10] dehyph-hit 1
layout collapsed-hit 0 pages []   dehyph-hit 1
raw    collapsed-hit 0 pages []   dehyph-hit 0
E
```

So with `-layout` the whitespace-collapsed search finds 0 hits; it needs hyphen-joining (`re.sub(r'-\s*\n\s*','',t)`). A future rechecker following the knowledge file verbatim would conclude the quote is missing. The evidence file's own method (plain mode) does find it. Fix: say "plain `pdftotext`, or `-layout` with end-of-line hyphens joined".

**F4 — MINOR. Page-count wording is inconsistent across the landed bytes.** The row's scope cell says "The full 185-page typeset text was opened" (true as the PDF page count: pdfinfo `Pages: 185`, with a blank final page numbered 185). The Gate row's source label, the lesson (line 33–35: "full 184-page text") and conlang-scholarship.md line 4 ("whole 184-page book") say 184 (the imprint's "с.184"). Both numbers are defensible, but the same artefact carries both and no cell explains the difference. The imprint figure is 184 pages and the PDF has 185.

Not a defect: the Gate row truncates the sha256 to `e512a20dd3eef97e…` (16 hex) while S877.txt carries all 64; both agree on the prefix. The access date 2026-10-25 is the day of both captures.

## 6. What I did NOT check

- The other four rows (S876, S878–S880) and the knowledge-file body's claims beyond grepping which S877 sentences it makes. I did not re-verify every S877-cited claim in conlang-scholarship.md against the book, only the scope-cell items and the p. 10–16 spans I read.
- `accept-c.py` was not run (it is a counter, outside this item's scope).
- "Not peer-reviewed" is checked only as not contradicted by the front matter; I did not search for an editorial or review record.
- I did not independently confirm that the 2006 print edition equals this 2007-dated PDF (`CreationDate` Jul 2007); the PDF itself carries the 2006 imprint and the ISBN.
- No browser automation or challenge-solving was used; none was needed.
- Wayback `curl/8.7.1` first attempt failed at TCP connect (`curl: (7)`), the retry succeeded. I treated it as transient network noise, not a UA wall.
