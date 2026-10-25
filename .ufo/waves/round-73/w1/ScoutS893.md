# Seat ScoutS893 — staged row S893 (Kostyukhin 2023, Vestnik MGLU) scout report

Seat: ScoutS893 (leaf, no delegation, no task spawns). Item: re-open staged row S893; tentative lane id S879.
Verdict: **ADMIT** (with two wording/location corrections the adopted text should carry, listed in §9).

---

## 1. Assignment and source

Staged row S893 (SOURCES.append.md row 41):
Костюхин, А. А. (2023), «Классификации конлангов в современной интерлингвистике», *Вестник Московского государственного лингвистического университета. Гуманитарные науки*, 2023, Вып. 2 (870), С. 28–34, DOI 10.52070/2542-2197_2023_2_870_28 — https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike | paper | B, mined, opened 2026-10-23, recheck 180d, used-by conlang-scholarship.amend-2026-10-23.md.

Amendment claims citing S893 (conlang-scholarship.amend-2026-10-23.md, third amendment §N+1): "from S893: Auxlangs, then вымышленные языки in the broad sense, then personal or автоконланги for individual enthusiasts' projects, with Tolkien's languages, Klingon and the language of Myst as instances; and how that classification compares with Peterson's, which is finer-grained." Also the source line claims the passage is in "§1". Verified against the live page as served and the publisher PDF.

---

## 2. Fetch commands and raw outputs

UA used for live fetch (browser-shaped; recorded per QUALITY 21/22):
`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

Command 1 (article HTML page):
```
mkdir -p /tmp/ScoutS893 && cd /tmp/ScoutS893 && UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' && curl -sS -o page.html -w 'HTTP %{http_code} bytes %{size_download} url %{url_effective}\n' -A "$UA" -L 'https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike' && wc -c page.html
```
Raw output:
```
HTTP 200 bytes 97656 url https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike
97656 page.html
```

Command 2 (article PDF):
```
cd /tmp/ScoutS893 && UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' && curl -sS -o article.pdf -w 'HTTP %{http_code} bytes %{size_download} type %{content_type}\n' -A "$UA" -L 'https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike/pdf' && file article.pdf
```
Raw output:
```
HTTP 200 bytes 630227 type application/pdf
article.pdf: PDF document, version 1.7 (zip deflate encoded)
```

Command 3 (PDF text extraction):
```
cd /tmp/ScoutS893 && pdfinfo article.pdf | head -12 && pdftotext -layout article.pdf article_pdf.txt
```
Raw output (relevant lines):
```
Creator:         Adobe InDesign CS6 (Windows)
Producer:        CyberLeninka
Pages:           7
```

Checksums (fetched artifacts):
```
sha256sum page.html article.pdf
331062f8a4dcb9f51234727040cd673035ca4c308267ee84c36e45cbd2e382d9  page.html
cc9a91c5149ada2868fc94f93c39e61c62812466c8414ddff5643dd254c0643f  article.pdf
```

No challenge wall encountered; the browser-shaped UA got HTTP 200 on first attempt (no retry needed).

---

## 3. Bibliographic verification (live page via CyberLeninka metadata + PDF)

| Field | Claimed | Verified | Match |
|---|---|---|---|
| Title (RU) | «Классификации конлангов в современной интерлингвистике» | `<meta name="citation_title" content="КЛАССИФИКАЦИИ КОНЛАНГОВ В СОВРЕМЕННОЙ ИНТЕРЛИНГВИСТИКЕ"/>`; PDF first page `Классификации конлангов / в современной интерлингвистике` | ✓ |
| Author | Костюхин, А. А. | `<meta name="citation_author" content="Костюхин А. А."/>`; PDF `А. А. Костюхин, Московский государственный лингвистический университет` | ✓ |
| Year | 2023 | `<meta name="citation_publication_date" content="2023"/>`; PDF `2023` | ✓ |
| Journal | Вестник МГЛУ. Гуманитарные науки | `<meta name="citation_journal_title" content="Вестник Московского государственного лингвистического университета. Гуманитарные науки"/>`; PDF header `Языкознание` + `Vestnik of MSLU. Humanities. Issue 2 (870) / 2023` | ✓ |
| Issue | Вып. 2 (870) | `<meta name="citation_issue" content="2 (870)"/>`; PDF `Вып. 2 (870)` | ✓ |
| Pages | С. 28–34 | PDF: printed folios 29,30,31,32,33,34 appear on PDF pages 2–7 (title page = printed p. 28); citation block `С. 28–34` | ✓ |
| DOI | 10.52070/2542-2197_2023_2_870_28 | PDF first page `DOI 10.52070/2542-2197_2023_2_870_28`; DOI string appears 3× in live HTML | ✓ |
| eISSN | 2542-2197 (DOI prefix) | `<meta name="citation_eissn" content="2542-2197"/>` | ✓ |
| Publisher | ФГБОУ ВО «Московский государственный лингвистический университет» | `<meta name="citation_publisher" content="...Московский государственный лингвистический университет"/>` | ✓ |

---

## 4. Located quotes (≤25 words, verbatim, from the live page as served; PDF spelling noted)

All quotes are verbatim spans from the live HTML page (`article.txt`, lines 104–118) and are confirmed in the publisher PDF (PDF page 5 = printed p. 32). Word counts by `wc -w` (Cyrillic, whitespace tokens).

Q1 (4 words): `1. Auxlangs. Вспомогательные языки`
- Location: comparison section (heading `Сопоставление классификации Д. Питерсона с типологиями современных отечественных лингвистов`), PDF p. 5 = printed p. 32; live-page extraction line 104.

Q2 (7 words): `2. Вымышленные языки (ВЯ) в широком смысле`
- Location: same section, live-page extraction lines 106–107 (PDF p. 5 = printed p. 32).

Q3 (16 words): `2.2. Personal languages Это личные, или персональные, языки, т. е. вымышленные языки, проектируемые отдельными энтузиастами лингвоконструирования`
- Location: same section, live-page extraction lines 117–118 (PDF p. 5 = printed p. 32). This is the passage the amendment renders as "personal or автоконланги for individual enthusiasts' projects" — the concept is verbatim; the lexeme автоконланги is NOT in the source (see §5).

Q4 (11 words): `Шувалова и М. Ю. Сидорова приводят языки Дж. Р. Р. Толкина`
- Location: same section, live-page extraction line 113 (PDF p. 5 = printed p. 32).

Q5 (15 words): `клингонский язык из сериала «Звездный путь», а также язык Э'П из мира компьютерной игры «Myst»`
- Location: same section, live-page extraction line 113 (PDF p. 5 = printed p. 32). Note: the live page renders the game's language as `Э'П` (raw HTML has `Э&#39;П`); the publisher PDF renders it `D'ni`. Quoted above as served on the live page.

The claimed "finer-grained" comparison is verbatim on the live page (line 127): `Наиболее детализированной классификацией, по всей видимости, является типология Д. Питерсона, поскольку она содержит категории, явно не представленные в двух других классификациях.` (32 words — reported as evidence, not used as the located quote.)

Recheck command (the staged row's own recheck, run by me on 2026-10-25):
```
curl -fsSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' 'https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike' | grep -c 'Шувалова и М. Ю. Сидорова предлагают следующую классификацию'
```
Output: `1` — reproduces the row's recheck expectation.

---

## 5. Amendment claim verification (conlang-scholarship.amend-2026-10-23.md)

| Amendment claim | Verified | Status |
|---|---|---|
| "Auxlangs" | Q1 verbatim, with definition sentence `К этой группе следует относить языки, которые, по замыслу их создателей, предназначены функционировать в качестве международных искусственных языков` (examples эсперанто, идо, ложбан) | ✓ |
| "вымышленные языки in the broad sense" | Q2 verbatim, with sub-items 2.1 Artlangs (2.1.1 languages that outgrew their fiction; 2.1.2 languages functioning only within the work) | ✓ |
| "personal or автоконланги for individual enthusiasts' projects" | Concept verbatim (Q3: `Personal languages ... личные, или персональные ... проектируемые отдельными энтузиастами лингвоконструирования`; the article adds `Их исследователи предлагают также обозначать «авторскими языками»`). The lexeme **автоконланги is absent from the source** — 0 occurrences in the full HTML page and in the PDF. Source's own terms: Personal languages / личные, или персональные / авторские языки. | ✓ (concept) / ✗ (lexeme not verbatim) |
| "Tolkien's languages, Klingon and the language of Myst as instances" | Q4+Q5 verbatim (Толкина; клингонский язык из сериала «Звездный путь»; язык Э'П / D'ni из мира игры «Myst») | ✓ |
| "how that classification compares with Peterson's, which is finer-grained" | `Наиболее детализированной классификацией, по всей видимости, является типология Д. Питерсона...` (comparison section; also: `классификация Шуваловой и Сидоровой более детально рассматривает категорию вымышленных языков`) | ✓ |
| Location "§1, the classification passage" | The passage sits under the heading `Сопоставление классификации Д. Питерсона с типологиями современных отечественных лингвистов` — the fourth body section (after Введение, Происхождение и дефиниции термина «конланг», Классификация конлангов Д. Питерсона). Section headings are unnumbered in both the HTML and the PDF, so "§1" is an inaccurate label; by ordinal count the passage is in the 3rd numbered body section (the comparison section), not §1. | ✗ (mislocated) |

No misquote of the classification content found. Two non-content defects to carry into the adopted text: (1) the location label "§1" is wrong; (2) "автоконланги" is not the article's wording.

---

## 6. Wayback CDX canonical-slug probe

Probed URLs (both returned HTTP 200 with an empty array — no captures of this slug):

1. Exact canonical slug: `https://web.archive.org/cdx/search/cdx?url=cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike&output=json&limit=10&filter=statuscode:200`
   - Result: `[]` (no snapshot).
2. Prefix (any path under the slug): `https://web.archive.org/cdx/search/cdx?url=cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike*&output=json&limit=20`
   - Result: `[]` (no snapshot).

The live page is reachable (HTTP 200), so no 'no capture' ruling is needed, but the CDX result means the URL has no Wayback fallback — a flip-relevant fact if the live page ever moves (see §9).

---

## 7. Proposed lane registry row (11-column schema, tentative id S879)

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S879 | Костюхин, А. А. (2023), «Классификации конлангов в современной интерлингвистике», *Вестник Московского государственного лингвистического университета. Гуманитарные науки*, 2023, Вып. 2 (870), С. 28–34, DOI 10.52070/2542-2197_2023_2_870_28 — https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike | paper | B | Tier B for the content of the Шувалова/Сидорова classification of artificial languages as a later peer-reviewed article states and assesses it: Auxlangs (вспомогательные языки), then вымышленные языки (ВЯ) in the broad sense (2.1 Artlangs, incl. 2.1.1 languages that outgrew their fiction), then 2.2 Personal languages for individual enthusiasts' projects, with Tolkien's languages, Klingon and the language of Myst as instances; and for the comparison against Peterson's finer-grained typology. Tier B: one review article reporting another author's classification | The section headed «Сопоставление классификации Д. Питерсона с типологиями современных отечественных лингвистов» (comparison section), the passage presenting the Шувалова/Сидорова classification, and the same section's comparison with Peterson's typology — PDF p. 5 = printed p. 32; article page as served 2026-10-25 | Closes the gap round 2 could not: the actual categories the Russian conlang-scholarship book proposed — Auxlangs, вымышленные языки (ВЯ) в широком смысле (Artlangs incl. languages that outgrew their fiction), and Personal languages for individual enthusiasts — quoted from a peer-reviewed article that also compares them with Peterson's finer-grained typology and says which categories are under-specified | mined | 2026-10-25 | 180d — `curl -fsSL 'https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike' | grep -c 'Шувалова и М. Ю. Сидорова предлагают следующую классификацию'` -> 1 (ran 2026-10-25) | corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md |

Notes:
- No pipe character inside any cell; no escaped pipes; recheck in 180d form with the working command (output 1 reproduced on 2026-10-25).
- status mined; opened 2026-10-25 (this verification date, per the wave instruction; the staged row had opened 2026-10-23).
- used-by: exactly the admitted entry that cites S893 — conlang-scholarship.amend-2026-10-23.md (the base conlang-scholarship.md does not cite S893; grep of the whole knowledge tree found S893 only in that one file).
- Anchor cell intentionally corrects the staged row's "§1" label to the true location (comparison section, printed p. 32).
- Source cell is the staged biblio unchanged (verified in full in §3).

---

## 8. Tier assignment

**Tier B**, matching the staged row and the amendment's own tier note.

Reason: the tier rubric (corpus/SOURCES.md) reads "B — strong secondary (expert write-up with reproducible detail, survey, textbook)". This is one peer-reviewed research article (Vestnik MGLU Humanities, open access) that presents and assesses another author's classification — a strong secondary source for the conlang-scholarship entry, read in the original language (Russian) with full text opened. Not tier A: the row's payload is a second-hand presentation of the Shuvalova/Sidorova book's classification (the book itself is not the fetched artifact), and for the article's own comparative method it is primary but the entry uses the reported classification content. Not tier C: it is real, reachable, and peer-reviewed. Flip condition: if the fleet's tier rubric were read so that "original paper" (the A-list mention) covers this article for its own comparative analysis, an A argument could be made; the amendment text uses it as a source for another work's classification, which is the B use.

---

## 9. Verdict

**ADMIT.**

Reason: live FET HTTP 200 (97 656 bytes HTML, 630 227 bytes PDF), full text obtained both as the CyberLeninka page and as the publisher-produced PDF; bibliographic data verified in full against the page (title, author, year, journal, issue 2 (870), pages 28–34, DOI, eISSN); the classification passage located verbatim with five ≤25-word quotes (4/7/16/11/15 words); every substantive amendment claim verified — Auxlangs, вымышленные языки (ВЯ) в широком смысле, Personal languages for individual enthusiasts, instances Tolkien/Klingon/Myst, and the finer-grained Peterson comparison; the staged row's recheck grep reproduced (output 1).

Two non-content corrections to carry into the adopted row and entry text (they affect wording/location only, not the row's substance):
1. Location: the classification passage is NOT in "§1" — it sits in the comparison section headed «Сопоставление классификации Д. Питерсона с типологиями современных отечественных лингвистов» (3rd numbered body section), PDF p. 5 = printed p. 32. Section headings are unnumbered in the source.
2. Lexeme: "автоконланги" appears nowhere in the source (0 occurrences in HTML and PDF). The source's own terms are Personal languages / личные, или персональные / авторские языки. The adopted text should use the source's wording.

Flip condition: REFUSE/UNVERIFIABLE if (a) the wave requires the drafted wording and "§1" location to be adopted verbatim without these corrections (then the row as staged would be factually mislocated and the entry would carry a non-source lexeme); or (b) the live page or PDF becomes unreachable later — the Wayback CDX probe found zero captures of the canonical slug, so there is no archive fallback; or (c) a later check shows the fetched PDF is not the final published version (no evidence of that; folios 28–34 and DOI match).

---

## 10. Hygiene records

- Tool installs: none (curl, pdftotext, pdfinfo, grep all preinstalled system tools; no pacman — paused host-wide; no installs of any kind; RULES.md read before any install consideration).
- Downloads (all under /tmp/ScoutS893/): page.html (97 656 bytes, sha256 331062f8a4dcb9f51234727040cd673035ca4c308267ee84c36e45cbd2e382d9), article.pdf (630 227 bytes, sha256 cc9a91c5149ada2868fc94f93c39e61c62812466c8414ddff5643dd254c0643f); extracted texts article.txt / article_pdf.txt (scratch).
- UA recorded in §2. No challenge walls encountered (browser-shaped UA succeeded on first attempt).
- Nothing written to the fleet repo, lane repo, shokuknow source tree, or registry; only this report file under .ufo/waves/round-73/w1/.
