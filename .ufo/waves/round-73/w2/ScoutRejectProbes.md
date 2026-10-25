# ScoutRejectProbes — falsify the Gate reject rows of corpus/lessons/round-73.md (landed 0316b88)

Seat: leaf scout, wave 2. Read-only against the lane (lesson read via `git show 0316b88:...`); no clone needed
(no byte-changing experiment). Downloads in `/tmp/ScoutRejectProbes/` only. No tools installed; pacman not run.
Fetch UAs: `UB` = `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`,
`UC` = `curl/8.7.1`; every request below names its UA. No browser automation, no challenge passed.

## Verdict in one line
One BLOCKER: the S894 reject ground "no Wayback capture of the same page" is FALSE. The canonical Cambridge article
page has two status-200 Wayback captures whose body carries the quoted abstract. Every other stated number and status
reproduced exactly. Two MINOR omissions and two MINOR wording defects.

## 1. Re-run table (all measured 2026-10-25 ~20:06 local / 23:07 UTC)

| probe | lesson says | measured | match |
|---|---|---|---|
| `https://doi.org/10.1017/cnj.2024.21` UC, `curl -sSL` | 429, 1302 B, "Too many automated requests" | 429, 1302 B, marker x3 (302 -> `cambridge.org/core/product/identifier/S0008413124000215/type/journal_article`, then 429) | yes |
| same, UB | 429, 1302 B, marker | 429, 1302 B, marker x3 | yes |
| Springer `https://link.springer.com/chapter/10.1007/978-3-032-03277-5_15` UC | 200, 325225 B, wall absent | 200, 325225 B, 0 "Client Challenge"; `<title>Conlangs in Theoretical Linguistics \| Springer Nature Link`; **3 redirects, final URL `...?error=cookies_not_supported&code=...`** (first hop is 303 to `idp.springer.com/authorize`) | yes (redirect chain unstated, MINOR) |
| same, UB | 200, 3038 B, "Client Challenge" | 200, 3038 B, `<title>Client Challenge`, 1 marker | yes |
| `https://doi.org/10.1007/978-3-032-03277-5_15` UC / UB | (S910 route) | UC 200 325225 B; UB 200 3038 B | yes |
| Crossref `/works/10.1017/cnj.2024.21` (UB) | reachable, abstract | 200, 6670 B, `abstract` 1112 chars, "project-based curriculum" x1 | yes |
| Crossref `/works/10.1007/978-3-032-03277-5_15` (UB) | reachable | 200, 14874 B; **no `abstract` field** (metadata only: title, container, pages 343-363) | yes; staged S910 span is metadata, so fine |
| MGIMO PDF `https://philnauki.mgimo.ru/jour/article/viewFile/520/524` UB and UC | 200, 5824942 B, nine-field span | 200, 5824942 B both UAs; `pdftotext` line 180 "The structure of each entry includes:" then fields 1-9 (lines 181-190) | yes |
| Luba PDF `linguistische-treffen.pl/articles/27/24_luba.pdf` UB and UC | 200, 168723 B; span2 on printed p. 390 | 200, 168723 B both; 12 pp; span1 "insbesondere drei Hauptgruppen unterscheiden" on PDF p.3 (printed 387); span2 "interpretativ, explorativ und konfigu-" on PDF p.6, page header `390  Katarzyna Luba` | yes |
| Schreyer Crossref `/works/10.1146/annurev-anthro-101819-110152` | 200 | 200, 22456 B; page `327-344`, container `Annual Review of Anthropology`, abstract opens "Constructed languages, also known as conlangs" | yes |
| Goodall Crossref (S923) | span present | 200, 12490 B; "four main types of these constructed languages" x1 | yes |
| `api.crossref.org/journals?query=constructed+language&rows=20` (S922) | negative | 200, 196 B, `"total-results":0`, `"items":[]` | yes |
| S915 Crossref query (corrected "Languages", UB) | relevance search not a filter | 200, 515859 B, `total-results` **822923** (scout recorded 730,163 in w1; not in lesson), 40 items, 19 of them container "The Palgrave Handbook of Constructed Languages", "Conlangs in Typological Research" x1 | yes (the lesson states no total) |
| `http://conlang.org/26c3.pdf` UB and UC, `-L` | live 200, 753374 B | 200, 753374 B **after 301 -> `https://conlang.org/26c3.pdf` -> 301 -> `https://conlang.org/cl101.pdf`** | number yes; "live HTTP 200" omits the two redirects (MINOR; round-68 lesson line 111 already says "26c3.pdf -> cl101.pdf") |
| `web.archive.org/web/20100107110431id_/http://conlang.org/26c3.pdf` UB/UC | capture | 200, 753374 B, `memento-datetime: Thu, 07 Jan 2010 11:04:31 GMT`, `x-archive-orig-content-length: 753374`; sha256 `19eb1dc1...e80` identical to live | yes |
| epigraph | "conlanging (n): the art and craft of making your very own language" | `pdftotext -layout 26c3.pdf` line 7: `conlanging (n): the art and craft of` (wraps; quote is spread over lines) | yes |
| S920 Wayback PDF `.../web/20260115005532id_/https://www.cambridge.org/core/services/aop-cambridge-core/content/view/649F8BEDBF579512088F614EB2794B59/S0008413124000215a.pdf/...` UB and UC | printed p. 310 §1.3 | 200, 638008 B both, sha256 identical `1acd085f...`; 26 pp; PDF p.4 header `310  Sara Sowers-Wills`; span at line 202, after heading `1.3 Institutional and course details` (line 183); `2.1.2 Petlang` heading line 325 on printed p. 313 | yes (p. 310, §1.3; staged "§2.1.2 p. 312" wrong as lesson says) |
| staged recheck S894 `api.semanticscholar.org/graph/v1/paper/DOI:10.1017/cnj.2024.21?fields=...` | n/a | first call (UB, grep piped) printed `0`; two later calls (UB, UC) 200, 3588 B, abstract present (grep -c 1 on UC). First `0` = transient, not absence | n/a |

Staged recheck commands from `SOURCES.append.md` also re-ran: S909 -> 1, S910 -> 1, S915 -> 1, S922 -> 1, S923 -> 1,
S929 -> 1, S930 -> 1 (staged S930 expected 3; measured `grep -c` over the file = 1 because the JSON is one line — see MINOR M3).

## 2. Findings

### F1 — BLOCKER: S894 Gate row ground "no Wayback capture of the same page" is false
The row (lesson line 47) says: "no Wayback capture of the same page (CDX 0 for the DOI, the cambridge identifier URL and
the slug prefix)". The canonical article page is the redirect target of the DOI/identifier URL, and it has status-200 captures.

Reproducing commands and output (UC `curl/8.7.1`, 2026-10-25):

```
# canonical target recorded in the DOI chain (wayback id_ replay of the 2024-11-01 captures)
$ curl -sI -A curl/8.7.1 'https://web.archive.org/web/20241101042851id_/https://doi.org/10.1017/cnj.2024.21'
HTTP/2 302  location: .../web/20241101042851id_/https://www.cambridge.org/core/product/identifier/S0008413124000215/type/journal_article
$ curl -sI -A curl/8.7.1 'https://web.archive.org/web/20241101042852id_/https://www.cambridge.org/core/product/identifier/S0008413124000215/type/journal_article'
HTTP/2 301  location: /web/20241101042852id_/https://www.cambridge.org/core/journals/canadian-journal-of-linguistics-revue-canadienne-de-linguistique/article/phonology-from-the-inside-out-constructed-language-as-a-pedagogical-tool/649F8BEDBF579512088F614EB2794B59

$ A=www.cambridge.org/core/journals/canadian-journal-of-linguistics-revue-canadienne-de-linguistique/article/phonology-from-the-inside-out-constructed-language-as-a-pedagogical-tool/649F8BEDBF579512088F614EB2794B59
$ curl -s -A curl/8.7.1 "https://web.archive.org/cdx/search/cdx?url=$A&output=txt&filter=statuscode:200"
org,cambridge)/core/journals/.../649f8bedbf579512088f614eb2794b59 20241106195515 https://www.cambridge.org/core/journals/.../649F8BEDBF579512088F614EB2794B59 text/html 200 PHYINBAF4UFJYGIVRKM4FAW772BN5X47 139256
org,cambridge)/core/journals/.../649f8bedbf579512088f614eb2794b59 20241107004043 https://www.cambridge.org/core/journals/.../649F8BEDBF579512088F614EB2794B59 text/html 200 QE7UHKBANTDZ55WDAIZUDZ5O5MYXESKH 139614

$ curl -s -A "$UB" -o cap1.html -w "%{http_code} %{size_download}\n" "https://web.archive.org/web/20241106195515id_/https://$A"   -> 200 1030239  (UC: 200 1030239, same sha256 dc061a30...)
$ curl -s -A "$UB" -o cap2.html ... 20241107004043 -> 200 1030236
$ grep -c 'project-based curriculum' cap1.html cap1c.html cap2.html  -> 5 / 5 / 5 lines; Python on text after <body>: 6 occurrences,
  first in `<h2>Abstract</h2> ... <div class="abstract" data-abstract-type="normal"><p>This paper reflects on a project-based curriculum employing constructed languages to teach linguistics`
  title: "Phonology from the Inside Out: Constructed Language as a Pedagogical Tool | Canadian Journal of Linguistics/Revue canadienne de linguistique | Cambridge Core"
  canonical link = the same article URL.
$ live canonical article page, UB and UC: 429, 1302 B, "Too many automated requests" (the capture is the only same-page reader)
```

Why the wave-1 probe returned nothing: `.ufo/waves/round-73/w1/RevSowersAccess.md:40` ran
`...article/phonology-from-the-inside-out-constructed-language-as-a-pedagogical-tool*&matchType=prefix` — a literal trailing `*`
combined with `matchType=prefix`. Reproduced: that exact query returns HTTP 200 with an empty body; the same query without the `*`
returns 3 rows (the two 200 captures plus `/core-reader` 302); the `*`-only form without `matchType` also returns them:

```
## seat's exact query (trailing *, matchType=prefix)
[status=200]            <- 0 rows
## same, no star
20241106195515 ...649F8BEDBF579512088F614EB2794B59 200 139256
20241107004043 ...649F8BEDBF579512088F614EB2794B59 200 139614
20241106195515 ...649F8BEDBF579512088F614EB2794B59/core-reader 302 1100
```

The DOI row's own CDX (`doi.org/10.1017/cnj.2024.21&filter=statuscode:200`) is genuinely 0 — but only because both DOI captures
are 302 stubs (`20241101042851`, `20241101082618`; unfiltered query shows them) — exactly the round-72 K71-8 pattern QUALITY 21 was
written for (probe the canonical/redirect target, not the front door). The identifier URL likewise has only 301 captures
(`20241101042852`, `20241101082618`).

Effect on the verdict: the row has three grounds — (a) 429 (true), (b) no same-page capture (false), (c) Crossref record is a
different page (true as far as it goes). The stated flip, "a same-page capture, or the publisher page serving", is already
satisfied by (b)'s negation. The refusal does not follow from what I measured. QUALITY 18's same-page leg is met: the live URL is
the canonical article page, the capture is of that same page, and the anchor ("This paper reflects on a project-based curriculum
employing constructed languages to teach linguistics") is in the capture's body text (inside `abstract-content`), not only in meta.
QUALITY 10: a plain archive capture is an ordinary means; no automation.

Also QUALITY 21 (4)/(5) are not met by the row: the cell "Probed URLs" files only `doi.org`, `api.crossref.org` and the DOI CDX
query; the identifier-URL and slug-prefix probes the reason cites are not filed with raw urlkey counts/earliest/latest.
(Round-73's own lesson, R73-M3, applies QUALITY 21/22 to this row and misses the canonical slug.)

Related admitted-bytes consequences (not mutated here):
- `corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md:12` (admitted): "The Sowers-Wills article that S880
  describes was not opened: its DOI resolved to a publisher page answering HTTP 429 on 2026-10-25, so no row here cites it". Literally
  true, but it implies the article was unopenable by ordinary means; a status-200 same-page capture and a Wayback PDF of the same
  article (S920's URL, 200, 638008 B, 26 pp.) were reachable. MAJOR to MINOR depending on whether the entry is read as a statement
  about this round's opening only.
- Lesson line 101 ("unverifiable at the publisher page, not fabrication; the row is not adopted") — "unverifiable" is wrong: the quote is
  verifiable in the capture body and in the Semantic Scholar/Crossref records.

### F2 — MINOR: S869 row "live HTTP 200, 753374 B" omits two redirects
`http://conlang.org/26c3.pdf` -> 301 `https://conlang.org/26c3.pdf` -> 301 `https://conlang.org/cl101.pdf` -> 200. Numbers (753374 B,
capture 20100107110431, memento date 2010-01-07T11:04:31Z) and the epigraph reproduce; sha256 of live equals the 2010 capture
(`19eb1dc140785018e8c07b8b418b5e53b69170e10b470e3163ec1c942d454e80`). QUALITY 21 (3) asks for the redirect target; the row names none.
CDX for the exact slug `conlang.org/26c3.pdf` shows ≥15 status-200 captures, 2010-01-07 to 2024-03-04, all digest `A5RJVGZFIP4JGDIFCLQW5C2MT3E6Q3TQ`.
The row is "refused" because no admitted entry cites it and the clause is cut — consistent with the evidence; the document is adoptable now.

### F3 — MINOR: S915 "query token 'Languistics' misspelled" is true of the amend file, not of the staged registry row
`conlang-scholarship.amend-2026-10-23c.md` contains `Constructed+Languistics`; `SOURCES.append.md` S915 row (and its recheck command)
contains `Constructed+Linguistics` (twice). Both are wrong (correct token "Languages"), the lesson cites "S915 ... as staged" without saying which file.
Not a verdict problem. The corrected query reproduces (above).

### F4 — MINOR: S930 staged recheck count
Staged S930 recheck expects `grep -c` -> 3; measured 1 on the one-line Crossref JSON (`grep -c` counts lines). Lesson does not cite the count; no verdict effect. (Staged-file defect only.)

### F5 — MINOR (unverifiable by me): "CORPUS rule 4"
The lesson rows for S909/S910/S869 rest on "CORPUS rule 4" ("no admitted entry cites it"). I could not find a rule 4 with that content in
the lane tree at 0316b88 (`git grep -i "corpus rule"` returns none), in `corpus/README.md`/`QUALITY.md`, or in `shokuknow/doctrine/corpus-requirements.md`
(read-only grep). Not checked further.

## 3. Do the other verdicts still follow?
- S909/S910 "not adopted": follows as a scope decision. S909 reachable and span-present under both UAs (5824942 B). S910: Springer page serves 325225 B under UC and a 3038 B Client Challenge under UB — numbers exact — so an "unreachable" ground would be void, as the lesson states. Crossref metadata (no abstract) and the plain-UA page are both adoptable by ordinary means today. The lesson says exactly this; I found no contradiction. S910's CDX is genuinely empty (re-run: `link.springer.com/chapter/...` exact + prefix, `link.springer.com/10.1007/...`, `doi.org/10.1007/...` exact+prefix all 200/empty).
- S869 "refused": follows (scope), document adoptable now (live via redirect + 2010 capture, body epigraph present).
- S915 "not adopted": follows (defective query; reproduces: relevance search, 822923 total).
- S929/S930, S920/S922/S923 "not adopted, reachable, span-present": all reproduce; p. 390 and §1.3 p. 310 corrections correct.
- S894 "refused": does NOT follow (F1). It is adoptable now by ordinary means as a row naming the canonical article URL + the 2024-11-06 (or 11-07) Wayback capture; separately S920 (Tier A, Wayback PDF of the publisher PDF) covers the same article.
- Staged rows the lesson calls reachable and I find adoptable by ordinary means now: S909, S910 (plain UA / Crossref), S915 (after restage), S920, S922, S923, S929, S930 — all confirmed; plus S894 and S869 (F1, F2). None is blocked by an access control I met; the only access refusals met were Cambridge 429 (rate limit, both UAs, `retry-after: 5`, still 429 after ~15 min of probing) and Springer Client Challenge under UB (left unpassed; plain-UA route exists).

## 4. Not checked
- CORPUS rule 4 text (F5). Whether adoption "outside the declared set" is policy-forbidden in this round — I only judged reachability/ground validity.
- Cambridge 429 with a delayed single retry under a cookie jar (did not try beyond the Retry-After wait that elapsed naturally across calls).
- `reports/round-73/telemetry/quality22-controls.txt` GROUND/SHAPE regex logic — read only; not re-run.
- Whether `tools/check-gate-quotes.py` or accept-c.py would catch F1 (not run; no clone made).
- The S915 total-results count drift (730,163 w1 vs 822,923 now) is Crossref growth; not in the lesson.
- Wayback 429s appeared late in the session (my CDX bursts); the Springer CDX results were re-run after cool-down (status 200, empty body for every probe), the earlier empty results before the rate limit agree.
