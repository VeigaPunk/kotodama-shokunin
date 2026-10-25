# CritFactAmend1 — attack on `conlang-scholarship.amend-2026-10-23.md` §1 (S878, Novikov 2022)

Seat: CritFactAmend1 (round 73, wave 2, FALSIFY). Leaf: no delegation, no background jobs.
Lane revision attacked: `0316b8883b4f8d44b8efd720140e7f52f734a102` (`git rev-parse HEAD` = that sha; the amend file's blob at HEAD is `da9f3c9d…`, worktree sha256 `089d41b9…`, unmodified — the untracked entries in `git status --porcelain` are wave-harness artifacts only (`build-w2.py`, `w2.ready`, `w2.ready.dispatched`, `w2/`)).
Target bytes: `corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md` lines 3, 18–32 (§1) and, for completeness, lines 76 and 78 (§4's two S878 sentences).
Source attacked: `https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955`.
Nothing under the fleet root was written; the only lane write is this file. No tool installed.

## 0. Fetch provenance (mine, not the lane's)

```
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
curl -sS -L -A "$UA" -o /tmp/CritFactAmend1/novikov-browser.pdf \
  -w 'status=%{http_code} bytes=%{size_download} type=%{content_type}\n' \
  'https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955'
```
→ `status=200 bytes=959171 type=application/pdf`
→ `sha256sum` = `9f745ddaccdbccbf254c5d890cd5b621ab241ea6d6de0219287c2e0c075ed07c`
→ byte-identical to the lane capture: `reports/round-73/evidence/S878.txt` carries the same 959171 B / `9f745ddaccdbccbf…` / browser UA / 2026-10-25. **Provenance holds.**

Second UA (hygiene 21/22), plain client:
```
curl -sS -L -A 'curl/8.7.1' -o /tmp/CritFactAmend1/novikov-curl.pdf -w 'status=%{http_code} bytes=%{size_download}\n' <same URL>
sha256sum /tmp/CritFactAmend1/novikov-curl.pdf ; cmp novikov-curl.pdf novikov-browser.pdf && echo IDENTICAL
```
→ `status=200 bytes=959171`, same sha256, `IDENTICAL`. Not UA-gated; no wall, no CDX probe needed.

Pagination used below: 13 PDF pages, printed 455–467, **printed page = PDF page + 454**, proved by the running footers (`pdftotext -f N -l N -layout … - | tail -1` prints the printed page number).

## 1. Per-sentence table — every (S878) sentence in §1

Verdicts: SUPPORTED / MISLOCATED / MISATTRIBUTED / OVERSTATED. Source spans were located by whitespace-normalized substring match on `pdftotext -layout` output.

| # | line | sentence (abridged) | claim's locator | source span (printed p.) | verdict |
|---|---|---|---|---|---|
| S1 | 18 | abstract states the method; 24-word quote | Abstract, p. 455 | **p. 455** — "In order to achieve this goal, the author examines … linguistic features **on various levels**." | SUPPORTED; quote verbatim, `wc -w` = 24; truncated mid-sentence without ellipsis (F7) |
| S2 | 20 | "calls it one of the most important classifications …, then argues it apart" | — | **p. 458** — "One of the most important classifications of constructed languages includes the definitions of a priori and a posteriori languages." | OVERSTATED (F5b): the superlative attaches to *a classification that includes the definitions*, not to the dichotomy |
| S3 | 22 | "His ruling on it: 'this division should be seen as a scale rather than a binary system'"; Balaibalan / SolReSol / aUI | — | **p. 458** — "However, **it may be argued that** this division should be seen as a scale rather than a binary system since all a priori languages are bound to be influenced by their creator's linguistic worldview. Thus … Balaibalan … higher degree of reliance on natural languages than SolReSol … position different from the one of aUI" | quote verbatim SUPPORTED; framing OVERSTATED (F5a) |
| S4 | 24 | Halley's interlang/artlang split; zonal (Križanić's Common Slavonic); CNLs (Basic English, Globish, E-Prime) | — | **p. 459** — "M. Halley defines these two categories as interlangs and artlangs." / "This category will also include zonal languages, one of the earliest examples of which is the Common Slavonic language created in the 17th century by J. Križanić" / "The highest degree of a posteriority is demonstrated by a special subcategory described as controlled natural languages: Simple English, Basic English, Special English, Globish, etc." / "such thinking devices as E-Prime" | SUPPORTED |
| S5 | 26 | "The artlang side is not a class but a range"; Star Wars 68 languages; Klingon on Wikipedia | — | **p. 459** — "M. Halley defines these two categories as interlangs and artlangs." + "These languages range from those that do not possess any developed semantic systems … (e.g., the **Star Wars universe** features 68 languages, yet none of them have any formal description or consistency) to … Klingon which was used as one of the official languages of Wikipedia before its abolishment" | "not a class" MISATTRIBUTED (F3); "films" MINOR drift (F4); Klingon/68 SUPPORTED |
| S6 | 28 | conclusion; 18-word quote | **Conclusion, p. 464** | **p. 465** — "The research results also reveal the lack of a uniform constructed language taxonomy and challenge the integrity of the seemingly well-established dichotomies of a priori and a posteriori, auxiliary and artistic languages." | **MISLOCATED** (F1); quote verbatim, `wc -w` = 18 |
| S7 | 30 | Calibration: contested refinement, one author's position | — | **p. 458** (same spans as S2/S3) | SUPPORTED |
| S8 | 32 | Eurocentrism "is the article's own hypothesis-test, not a survey result"; SAE features even in a priori languages; worldview cannot be escaped | — | **p. 455** ("both a priori and a posteriori … inevitably reveal a certain percentage of Standard Average European features"), **p. 464** ("eurocentrism is not limited to a posteriori languages"), **p. 465** ("the bias caused by the creator's linguistic worldview cannot be completely avoided"), **p. 466** ("thus proving the hypothesis of linguistic relativity") | content SUPPORTED; the "hypothesis-test / not a survey result" framing MISATTRIBUTED (F6) |
| S9 | 76 | §4: "the scale is that article's operative claim" | — | p. 458 | OVERSTATED, same hedge defect as F5a (folded there) |
| S10 | 78 | §4: Eurocentrism as default, not accident | — | p. 465 | SUPPORTED |

Word counts exercised: `printf '%s' '<24-word span>' | wc -w` → `24`; `printf '%s' '<18-word span>' | wc -w` → `18`. Both exact.

## 2. Findings

### F1 — BLOCKER — line 28 cites p. 464 for a quote that is on p. 465

```
$ pdftotext -f 10 -l 10 -layout novikov-browser.pdf - | grep -c 'challenge the integrity'
0
$ pdftotext -f 11 -l 11 -layout novikov-browser.pdf - | grep -n 'challenge the integrity'
42:taxonomy and challenge the integrity of the seemingly well-established
43:dichotomies of a priori and a posteriori, auxiliary and artistic languages.
$ pdftotext -f 11 -l 11 -layout novikov-browser.pdf - | tail -1
КОГНИТИВНЫЕ ИССЛЕДОВАНИЯ                                                                         465
$ pdftotext -f 10 -l 10 -layout novikov-browser.pdf - | grep -c 'Conclusion'
0
$ pdftotext -f 11 -l 11 -layout novikov-browser.pdf - | grep -n '^ *Conclusion'
28:                                         Conclusion
```

The cited page (464) carries the Eurocentrism/Fig. 3 material and **no part** of the quoted sentence; the `Conclusion` heading and the quote are on 465. The amendment asserts a location that does not contain its own quote, so a reviewer who follows the citation finds nothing.

Severity note for the judge: no claim leg fires — GATE and EVIDENCE test the *registry row* quote ("Abstract, p. 455"), which is correct, and the C kill rule does not enumerate per-sentence locators. Under a literal reading of "an admitted statement is wrong" this is a BLOCKER; under a content-only reading it is MAJOR. Smallest safe correction: `Conclusion, p. 464` → `Conclusion, p. 465`.

### F2 — MAJOR — header line 3 gives two page ranges that are each one page early

```
$ pdftotext -f 3 -l 3 -layout novikov-browser.pdf - | grep -c 'Correlation between types'   # claimed start p.457
0
$ pdftotext -f 4 -l 4 -layout novikov-browser.pdf - | grep -n 'Correlation between types'    # actual start
3:         Correlation between types of constructed languages,
$ pdftotext -f 4 -l 4 -layout novikov-browser.pdf - | tail -1
458                                                                               COGNITIVE STUDIES
$ pdftotext -f 5 -l 5 -layout novikov-browser.pdf - | grep -c 'Semiotic specificity'        # claimed end p.459
0
$ pdftotext -f 6 -l 6 -layout novikov-browser.pdf - | grep -n 'Semiotic specificity'         # actual end
33:              Semiotic specificity of constructed languages
$ pdftotext -f 6 -l 6 -layout novikov-browser.pdf - | tail -1
460                                                                               COGNITIVE STUDIES
```

- `§"Correlation between types…", pp. 457–459` → the section runs **458–460** (heading on 458, next heading on 460). Both bounds wrong.
- `Conclusion, pp. 464–465` → the Conclusion runs **465–466** (heading 465, references begin 466). Both bounds wrong.
- `Abstract, p. 455` is correct (`pdftotext -f 1 -l 1 … | grep -c 'the author examines the existing classifications'` → 1).

Three of the four S878 locators in this file are off by +1, so this is not a typo in one place but an unverified page mapping (the article is 455–467 over 13 PDF pages; 455 + (pdf−1) = the footer). No §1 quote falls outside the stated ranges except the Eurocentrism support on 465–466, which the header's Conclusion range excludes at its top end.

### F3 — MAJOR — line 26: "The artlang side is not a class but a range" misstates the source's taxonomy

```
$ pdftotext -f 5 -l 5 -layout novikov-browser.pdf - | grep -n \
  'defines these two categories as interlangs and artlangs\|These languages range from\|Artlangs are not necessarily'
11:     M. Halley defines these two categories as interlangs and artlangs. While the
31:pursue the goal of becoming a lingua franca. These languages range from those
38:     Artlangs are not necessarily incorporated into works of fiction since their
```

The article makes artlangs **one of Halley's two categories** (a class) and then says its members *range* from undeveloped to well-developed. "Not a class but a range" negates the first half and inverts the relation: the range is internal to the class. The paragraph's substance survives; the topic sentence is false as written.

### F4 — MINOR — line 26: "the Star Wars films use 68 languages"; the source says "universe"

```
$ grep -c 'Star Wars films' novikov.txt
0
$ pdftotext -f 5 -l 5 -layout novikov-browser.pdf - | tr '\n' ' ' | grep -o 'the Star Wars universe features 68 languages'
the Star Wars universe features 68 languages
```
`Star Wars` occurs on printed p. 459 only. "Films" narrows the source's claim (the count is the franchise/universe's, not the films').

### F5 — MINOR — lines 20 and 22 (and 76) strip the source's hedge and shift the superlative's referent

```
$ pdftotext -f 4 -l 4 -layout novikov-browser.pdf - | grep -n 'it may be argued that this division'
35:it may be argued that this division should be seen as a scale rather than a binary
$ pdftotext -f 4 -l 4 -layout novikov-browser.pdf - | grep -n -A2 'One of the most important classifications'
30:taxonomy of constructed languages. One of the most important classifications
31-of constructed languages includes the definitions of a priori and a posteriori
32-languages. This dichotomy allows the linguists to separate constructed languages
```

(a) "**His ruling on it:**" presents "this division should be seen as a scale" as a ruling; the source's operative clause is "**However, it may be argued that** this division should be seen as a scale…". The modal is the author's own hedge, and the entry's own Calibration (line 30: "a contested refinement, not a replacement") contradicts the strength of "ruling". Same defect recurs at line 76 ("the scale is that article's **operative claim**").

(b) "the same article **calls it** one of the most important classifications" — the article calls *a classification that includes the a priori/a posteriori definitions* one of the most important; the split is the classification's content, not the classification. "Then argues it apart" also overshoots, given the article keeps the dichotomy and moves it to a scale (which the entry itself says is "not a replacement").

### F6 — MINOR — line 32: "the article's own hypothesis-test, not a survey result" misattributes the article's hypothesis

```
$ pdftotext -f 1 -l 1 -layout novikov-browser.pdf - | grep -n 'The author argues that\|This hypothesis is confirmed by'
27:distribution. The author argues that the recent development in technology provides constructed
29:unavailable and thus facilitates communication. This hypothesis is confirmed by several case studies,
$ pdftotext -f 12 -l 12 -layout novikov-browser.pdf - | grep -n 'proving the hypothesis'
8:be found in their semantic and semiotic systems, thus proving the hypothesis
$ python3 -c "
import re
t=open('novikov.txt',encoding='utf-8').read()
pg=[(454+i,re.sub(r'\s+',' ',p)) for i,p in enumerate(t.split(chr(12)),1)]
for term in ['Lojban is seen as a language','Lidepla (Lingwa de Planeta)','Toki Pona,','Dovahzul','Interslavic']:
    print(term,'->',[n for n,p in pg if term.lower() in p.lower()])"
Lojban is seen as a language -> [464]
Lidepla (Lingwa de Planeta) -> [464]
Toki Pona, -> [465]
Dovahzul -> [461, 465]
Interslavic -> [465]
```

The hypothesis the article says is "confirmed by several case studies" is the **technology / non-verbal-expression** one (p. 455); the Eurocentrism finding is offered as "proving the hypothesis of **linguistic relativity**" (p. 466), which is a different hypothesis and is not framed anywhere as a test of a Eurocentrism hypothesis. And the finding is drawn from the article's own case survey (Lojban, Lidepla, Toki Pona, Dovahzul, Interslavic, pp. 464–465), so "not a survey result" is contradicted on its face. The sentence's content (SAE features even in a priori languages; the creator's worldview cannot be fully escaped) is supported at 455/464/465 — the defect is the framing, not the facts.

### F7 — MINOR — line 18: the 24-word abstract quote is cut mid-sentence with no ellipsis, and the cut span is also the registry Gate quote

```
$ pdftotext -f 1 -l 1 -layout novikov-browser.pdf - | grep -n -A2 'In order to achieve this goal'
22:features. In order to achieve this goal, the author examines the existing classifications of constructed
23-languages and attempts to establish a connection between purposes of their creation and their
24:linguistic features on various levels. The research topic relevance is determined by a substantial
```
The source sentence continues "**on various levels.**"; the amendment closes the quotation at "linguistic features" and presents it as the complete clause. Verbatim and word-count compliance both hold (24 ≤ 25 cap), and extending the span would break the cap (28 words), so the fix is an ellipsis. The same 24-word span is the S878 quote in `corpus/lessons/round-73.md:20`, so the truncation is carried into the Gate record (it does not break the GATE leg — quote and locator there are correct).

### Out-of-slice note (not claimed as my finding)

The registry row `corpus/SOURCES.md:833` calls S878 a "peer-reviewed **Russian-language** treatment"; the article body is English (Russian title page/abstract only, p. 456) and the amendment's own header says "(English, Russian, English)". Already filed by sibling `ScoutReopenS878` (its line 69); I confirm it independently but it is that seat's finding, not mine.

## 3. What I could NOT check

- **The article's own factual assertions about the world** — that the Star Wars universe "features 68 languages", that Klingon was "one of the official languages of Wikipedia" and that the status was "abolish[ed] … as a measure of preventing the copyright disputes". I verified only that the article states them (p. 459); no independent source was opened, so I neither confirm nor refute them.
- **Halley's original definition** — the article attributes the interlang/artlang split to "M. Halley" with no reference entry (`grep -ci halley novikov.txt` → 1, the body sentence only; the 13-item reference list has no Halley). The amendment's "Halley's split" is therefore exactly as strong as the source and no stronger; I did not chase Halley.
- **The publisher's landing page, erratum/retraction status** — the PDF was served directly; no HTML page was fetched, so I cannot say whether the article carries a correction notice.
- **S879 and S880** — other seats' slices; I did not open cyberleninka or the Sanders PDF.
- **The base entry's own S878 citations** (`corpus/knowledge/linguistics/conlang-scholarship.md`) — outside my slice; not audited, so I cannot say whether the base repeats the same page offset.
- **The Wayback duplicate** named in the registry row — I did not compare archived bytes; I re-verified the live capture only (sha matches the lane evidence exactly).
- Whether `p. 464`/`pp. 457–459` were intended as PDF-page indices: disproved rather than assumed — PDF p. 10 carries the printed footer 464 and no conclusion text, PDF p. 3 carries footer 457 and no section heading.

## 4. Smallest safe corrections (one line each)

1. Line 28: `Conclusion, p. 464` → `Conclusion, p. 465`. (F1)
2. Line 3: `pp. 457–459` → `pp. 458–460`; `pp. 464–465` → `pp. 465–466`. (F2)
3. Line 26: "The artlang side is not a class but a range" → "The artlang side is one category whose members range from …" (keep the sentence's second half). (F3)
4. Line 26: "the Star Wars films" → "the Star Wars universe". (F4)
5. Line 22: "His ruling on it:" → "He argues:"; line 76: "operative claim" → "own argument". (F5a)
6. Line 20: "calls it one of the most important classifications" → "calls the classification that carries it one of the most important". (F5b)
7. Line 32: drop "hypothesis-test, not a survey result" → "is the article's own reading of its case survey, offered as proof of the linguistic-relativity hypothesis". (F6)
8. Line 18 (and the mirrored Gate quote at `corpus/lessons/round-73.md:20`): close with "…linguistic features…" — an ellipsis, since extending to "on various levels" makes 28 words and breaks the 25-word cap. (F7)

No BLOCKER was found in the content of §1: every quoted string is verbatim in the fetched PDF, both word counts are exact, and every content claim except the three framed ones (F3, F5, F6) is carried by a located span. The one BLOCKER-grade defect is the locator at line 28 (F1), whose repair is a single page number.
