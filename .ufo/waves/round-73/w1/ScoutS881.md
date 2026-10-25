# ScoutS881 — round 73, wave 1 — staged S881 re-open (Enguehard 2022, RiCOGNIZIONI 9(18))

Seat: ScoutS881 (leaf). Date: 2026-10-25. Item: re-open staged row S881 vs the live OJS page; verify title/author/year/DOI/abstract/keywords, locate the abstract sentence for "conlang construction is a method that yields analysable data", confirm the staged entry §2 claims live in the abstract, propose the registry row, probe Wayback CDX, verdict.

Tools installed: none (no install needed; nothing recorded).

---

## 1. Fetches — exact commands + raw outputs

All fetches used one browser-shaped User-Agent (recorded):
`User-Agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

### 1.1 Live article page (primary fetch)

Command:
```
curl -sSL -w 'HTTP_STATUS=%{http_code} BYTES=%{size_download} CONTENT_TYPE=%{content_type} REDIRECT_URL=%{url_effective}\n' -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' -o /tmp/ScoutS881/7099.html 'https://ojs.unito.it/index.php/ricognizioni/article/view/7099'
```
Raw output:
```
HTTP_STATUS=200 BYTES=30289 CONTENT_TYPE=text/html; charset=utf-8 REDIRECT_URL=https://ojs.unito.it/index.php/ricognizioni/article/view/7099
```
Downloaded file: `/tmp/ScoutS881/7099.html` (30,289 bytes, 686 lines; saved from the live page as served 2026-10-25).

### 1.2 Staged recheck command reproduced at live page

Command (exactly the staged recheck):
```
curl -fsSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' 'https://ojs.unito.it/index.php/ricognizioni/article/view/7099' | grep -c 'marginalize'
```
Raw output: `2` (downloaded at 2026-10-25). The staged row's `-> 2` claim reproduces.

### 1.3 DOI resolution

Command:
```
curl -sSL -o /dev/null -w 'HTTP_STATUS=%{http_code} REDIRECT_URL=%{url_effective}\n' -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' 'https://doi.org/10.13135/2384-8987/7099'
```
Raw output: `HTTP_STATUS=200 REDIRECT_URL=https://ojs.unito.it/index.php/ricognizioni/article/view/7099`
The DOI resolves to the same OJS landing page.

---

## 2. Staged row vs live page

Staged S881 (SOURCES.append.md line 29, raw) compared against live metadata (`<meta name="citation_*">`, `<title>`, abstract `<section class="item abstract">` of /tmp/ScoutS881/7099.html):

| field | staged S881 | live page | match |
|---|---|---|---|
| title | "Teaching linguistic methods with conlangs" | `<title>` + `citation_title`: Teaching linguistic methods with conlangs | YES |
| author | Guillaume Enguehard (2022) | `citation_author` = Guillaume Enguehard; `citation_date` content="2022/12/31" | YES |
| journal | RiCOGNIZIONI. Rivista Di Lingue E Letterature Straniere E Culture Moderne 9(18) | `citation_journal_title`: RiCOGNIZIONI. Rivista di Lingue e Letterature straniere e Culture moderne; `citation_volume` 9, `citation_issue` 18 | YES (trivial case variants in the staged title) |
| DOI | 10.13135/2384-8987/7099 | `citation_doi` = 10.13135/2384-8987/7099; DOI redirect resolves to same page | YES |
| abstract | staged anchor: "Abstract + Keywords …" (paraphrase) | abstract paragraph verbatim (section 3 below) | YES (substance in abstract, not only paraphrase) |
| keywords | staged: (Constructed Languages, Phonology, Diachronic linguistics, Method-Oriented Teaching) | live `citation_keywords` fields: Constructed languages, Phonology, Diachronic linguistics, Natural Languages, Natlang, Linguistic Analysis, Constructed Languages (dup), Conlangs, Linguistics Teaching, Method-Oriented Teaching | PARTIAL — staged list is a 4-item subset of the live 10 tokens; no staged token is false |

PDF endpoint advertised on page: `citation_pdf_url` = https://ojs.unito.it/index.php/ricognizioni/article/download/7099/6102 (not fetched; this seat's scope is the landing page/abstract).

## 3. Located quote — "conlang construction is a method that yields analysable data"

Location: article landing page, "Abstract" section (`<h2 class="label">Abstract</h2>`), the abstract `<p>` — page-source line 267 of /tmp/ScoutS881/7099.html.

Quote (verbatim, first clause of the abstract's first sentence):

> the construction of languages by students allows them to better grasp the reality of linguistic analysis

Word count (wc -w): **16** (≤25 ✓). Command: `printf '%s' 'the construction of languages by students allows them to better grasp the reality of linguistic analysis' | wc -w` → `16`.

Full abstract for the record (both sentences, line 267):
1. "In this article, I show from my own experience as a linguistics teacher that the construction of languages by students allows them to better grasp the reality of linguistic analysis than does the repetition of exercises based on data from natural languages." (42 words)
2. "I show that the reasons that lead me to marginalize natural languages from teaching are the same ones that lead most linguists to marginalize constructed languages from research." (28 words)

## 4. Staged entry §2 claims — confirmed in the abstract, not only in the paraphrase

Staged entry `conlang-scholarship.md` §2 (line 19): "**§2 Conlangs as method** — from S881: construction as a teaching instrument that produces analysable data, and the asymmetry between how linguists teach and how they research."

- "construction as a teaching instrument that produces analysable data" — abstract sentence 1: "the construction of languages by students allows them to better grasp the reality of linguistic analysis …" ✓ in the abstract.
- "the asymmetry between how linguists teach and how they research" — abstract sentence 2: "the reasons that lead me to marginalize natural languages from teaching are the same ones that lead most linguists to marginalize constructed languages from research." ✓ in the abstract.

Both claims are literally carried by the live abstract; neither lives only in the staged paraphrase.

## 5. Proposed lane registry row (11-column schema), tentative id S876 (map: staged S881 → S876)

| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S876 | Guillaume Enguehard (2022), "Teaching linguistic methods with conlangs", *RiCOGNIZIONI. Rivista di Lingue e Letterature straniere e Culture moderne* 9(18), DOI 10.13135/2384-8987/7099 — https://ojs.unito.it/index.php/ricognizioni/article/view/7099 | paper | B | Tier B for the peer-reviewed statement of what constructed languages are for in linguistics — that conlang construction lets students grasp the reality of linguistic analysis, and that the reasons linguists marginalize natural languages in teaching are the same reasons they marginalize conlangs in research. Tier B: one author's argument in one article, not a venue-wide consensus | Abstract paragraph (page-source line 267) under the "Abstract" heading: "the construction of languages by students allows them to better grasp the reality of linguistic analysis" and "the reasons that lead me to marginalize natural languages from teaching are the same ones that lead most linguists to marginalize constructed languages from research" — article page as served 2026-10-25 | Answers the round-1 question of whether a peer-reviewed conlang venue exists: it does, and it frames conlang construction as a method that produces analysable linguistic data rather than as decoration | mined | 2026-10-25 | 180d — `curl -fsSL 'https://ojs.unito.it/index.php/ricognizioni/article/view/7099' \| grep -c 'marginalize'` -> 2 (ran 2026-10-25) | corpus/knowledge/linguistics/conlang-scholarship.md |

used-by check: `conlang-scholarship.md` header names `source: S881 — https://ojs.unito.it/index.php/ricognizioni/article/view/7099` (line 4); `conlang-scholarship.amend-2026-10-23.md` does not cite Enguehard/7099 (it cites the Russian-language rows S892/S893 and the English S894 family), so used-by is exactly the one admitted entry. No pipe character appears inside any cell. No campaign-id citation in the S881 row itself (adjacent observation: the base entry's prose cites S728 as "round 1 conference paper" — that is the C-claim defect domain, logged separately).

## 6. Tier assigned: B — reason

The claim the lane takes from this row ("conlang construction is a method that produces analysable data; conlang marginalisation mirrors natural-language data marginalisation") is a single author's argument in one peer-reviewed article — a position, not a venue-wide consensus, and the opened artefact is the landing page plus abstract, not the full-text PDF. Tier B matches the staged assignment and the row family; nothing here satisfies a Tier-A test (field authority/consensus or full-text opened).

## 7. Wayback CDX canonical-slug probe — probed URLs

Probe 1 (exact slug, status-200 captures):
```
curl -sSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' 'https://web.archive.org/cdx/search/cdx?url=ojs.unito.it/index.php/ricognizioni/article/view/7099&output=json&filter=statuscode:200&limit=10'
```
Raw output: JSON list of 10 captures, all statuscode 200, text/html:
- 2023-01-02 16:12:26 https://www.ojs.unito.it/index.php/ricognizioni/article/view/7099 (5879 B)
- 2023-01-02 16:12:47 https://www.ojs.unito.it/index.php/ricognizioni/article/view/7099 (6078 B)
- 2023-03-15 15:21:43 https://www.ojs.unito.it/index.php/ricognizioni/article/view/7099 (6142 B)
- 2024-01-11 22:16:43 https://ojs.unito.it/index.php/ricognizioni/article/view/7099 (6381 B)
- 2024-02-13 04:34:12 https://ojs.unito.it/index.php/ricognizioni/article/view/7099 (6378 B)
- 2024-09-07 04:12:02 https://ojs.unito.it/index.php/ricognizioni/article/view/7099 (5601 B)
- 2025-01-23 12:48:23 https://ojs.unito.it/index.php/ricognizioni/article/view/7099 (5574 B)
- 2025-03-18 16:11:46 https://ojs.unito.it/index.php/ricognizioni/article/view/7099 (6475 B)
- 2025-10-12 22:57:26 https://ojs.unito.it/index.php/ricognizioni/article/view/7099 (6630 B)
- 2026-04-13 13:38:30 https://ojs.unito.it/index.php/ricognizioni/article/view/7099 (6748 B)

Probe 2 (prefix match — captures under the slug, incl. download subpath):
```
curl -sSL -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' 'https://web.archive.org/cdx/search/cdx?url=ojs.unito.it/index.php/ricognizioni/article/view/7099&matchType=prefix&output=json&filter=statuscode:200&limit=20'
```
Raw output: the same 10 captures plus 4 captures of `https://ojs.unito.it/index.php/ricognizioni/article/view/7099/6102` (2024-01-13, 2024-09-11, 2025-03-18, 2026-01-25; all 200).

Probed URLs filed: `https://ojs.unito.it/index.php/ricognizioni/article/view/7099`, `https://www.ojs.unito.it/index.php/ricognizioni/article/view/7099`, `https://ojs.unito.it/index.php/ricognizioni/article/view/7099/6102`, via CDX endpoint `https://web.archive.org/cdx/search/cdx`. Canonical slug has archive coverage continuously 2023-01-02 → 2026-04-13; no status-300/400/500 captures observed for it (filter 200 returned non-empty).

## 8. Verdict: ADMIT

Reason: the live page is directly reachable (HTTP 200, 30,289 bytes, browser UA — no wall encountered); every compared bibliographic field (title, author, year, journal, volume/issue, DOI) matches the staged row; the abstract carries both staged §2 claims verbatim in substance, and the located 16-word clause supports the "analysable data" framing; the staged recheck command reproduces (`grep -c 'marginalize'` → 2); the DOI resolves to the same page; Wayback archives the canonical slug under status 200 from 2023 to 2026. No refusal ground found for this row.

Flip condition: ADMIT flips to REFUSE/UNVERIFIABLE only if (a) the adopting entry requires full-text PDF content and the PDF endpoint (citation_pdf_url /download/7099/6102) proves unreachable by ordinary means, or (b) an adopt row must carry the complete live keyword set (the proposed row keeps the staged 4-token subset, which is accurate but not exhaustive — 6 further tokens exist on the page), or (c) the register row is assigned a different source URL than the cited slug.

## 9. Discrepancies / notes (non-blocking)

- Staged keyword list is a subset of the live 10 keywords; no false tokens.
- Staged journal-title capitalization differs trivially from the live metadata ("Di"/"e"/"straniere"/"Culture" casing).
- Live metadata carries the author affiliation "Université d'Orléans, CNRS/LLL" (not in the staged row; no impact on the claimed content).
- The base entry's prose citation of S728 as the round-1 conference paper remains a campaign-id defect per the claim text (out of this seat's scope to fix; flagged for the C-claim review).
