# ScoutReopenS876 — wave 2 FALSIFY, row S876 (Enguehard 2022, ojs.unito.it article 7099)

Landed revision attacked: 0316b8883b4f8d44b8efd720140e7f52f734a102 (read-only `git show`; no lane writes except this file). Downloads: /tmp/ScoutReopenS876/ (live-{browser,curl}.html, doi-*.html, wb-*.html, j-about.html, j-sub.html, cdx.json). No tool installs. Local curl is 8.23.0; the "curl/8.7.1" UA was sent with `-A curl/8.7.1`.

## VERDICT: ADMIT-STANDS
No failing field in the admitted statement (access date, quote, locator, evidence sha/bytes/status, tier, recheck, used-by). Two MINOR findings below (scope-cell paraphrase; unrecorded peer-review provenance). Neither changes the admitted quote or the tier.

## Fetches (every request, UA / status / bytes / sha256)
UA-B = `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`; UA-C = `curl/8.7.1`.

| URL | UA | status | bytes | sha256 |
|---|---|---|---|---|
| https://ojs.unito.it/index.php/ricognizioni/article/view/7099 | UA-B | 200 | 30289 | e7260b49370e9a1e715d92b2102eabf8c2c8846f00a94caf3d80138dd019369c |
| same | UA-C | 200 | 30289 | e7260b49370e9a1e715d92b2102eabf8c2c8846f00a94caf3d80138dd019369c |
| https://doi.org/10.13135/2384-8987/7099 (-L) | UA-B | 302 → www.ojs… 301 → ojs.unito.it/…/view/7099 200 | 30289 | e7260b49…369c (same) |
| same | UA-C | same chain, 200 | 30289 | e7260b49…369c (same) |
| https://web.archive.org/web/20260413133830id_/https://ojs.unito.it/…/view/7099 | UA-B | 200 | 30289 | 575e6ee968fbd46cc20961291a6d222fd4a9cdea21772beedb99cf8bb69300e3 |
| same | UA-C | 200 | 30289 | 575e6ee9…00e3 (same) |
| https://web.archive.org/cdx/search/cdx?url=ojs.unito.it/index.php/ricognizioni/article/view/7099&output=json&limit=20 | UA-C | 200 | 2304 | (not hashed) |
| https://ojs.unito.it/index.php/ricognizioni/about | UA-B | 200 | 26501 | |
| https://ojs.unito.it/index.php/ricognizioni/about/submissions | UA-B | 200 | 19752 | |
| https://ojs.unito.it/index.php/ricognizioni/about/editorialPolicies | UA-B | 404 | 22 | (path guess; irrelevant) |

No UA gating in either direction (browser and curl UAs byte-identical).

## Checks
1. **sha256 vs evidence line: EQUAL.** Fresh live body sha256 = `e7260b49370e9a1e715d92b2102eabf8c2c8846f00a94caf3d80138dd019369c` = evidence file `sha256:` line; bytes 30289 = evidence `bytes: 30289`; status 200 = evidence. No drift (hours later, same day).
2. **Quote in fresh body:** python3 (strip tags, `html.unescape`, collapse whitespace) `q in txt` → found at collapsed-text index 801 in live-browser, live-curl and the Wayback capture. Source-line location: `live-browser.html` lines 21 (meta description) and **267** (`<p>` under the Abstract heading) — matches the row's "page-source line 267". Quote: "the construction of languages by students allows them to better grasp the reality of linguistic analysis" — `echo -n … | wc -w` → **16** (≤25; matches evidence `quote-words: 16` and the lesson's "S876 16").
3. **Row parse:** `git show 0316b88:corpus/SOURCES.md | sed -n 831p | awk -F'|' '{print NF}'` → **13** (= 11 cells). Row sits at SOURCES.md:831; all rows `^| S[0-9]+ |` in the file have NF=13 (no BAD NF printed); header is `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |`.
4. **Anchor contains the evidence quote:** yes — the anchor cell holds the identical 16-word string, plus "page as served 2026-10-25 (HTTP 200, 30289 bytes) and capture 20260413133830, both carrying the span" — both legs re-verified true (live: item 2; capture: item 5).
5. **Source-cell URLs:** the live URL resolves (200). The Wayback URL resolves (200, `memento-datetime: Mon, 13 Apr 2026 13:38:30 GMT`, `x-archive-orig-date` same) and **contains the quote** (idx 801, source line 267). The capture exists in the CDX: `…,"20260413133830","https://ojs.unito.it/…/view/7099","text/html","200","2JTTXV2YVPDEBYHGEBZCKBGF52NTOSSG","6748"`. The capture body differs from live only by the order of the "related articles" `<li>` blocks (diff lines 539-556), nothing in the abstract. Not drift of the claimed span.
6. **DOI 10.13135/2384-8987/7099:** resolves (302→301→200) to the same URL; body sha256 identical to the direct fetch. Page `citation_doi` = 10.13135/2384-8987/7099.
7. **Bibliographic cells vs page metadata:** `citation_title` "Teaching linguistic methods with conlangs"; `citation_author` Guillaume Enguehard; `citation_journal_title` "RiCOGNIZIONI. Rivista di Lingue e Letterature straniere e Culture moderne"; `citation_volume` 9, `citation_issue` 18; "Vol. 9 No. 18 (2022)"; DC.Date.created / Published 2022-12-31. All match the row's "9(18)", 2022.
8. **recheck/used-by:** recheck `180d`, opened `2026-10-25`, status `mined` (the 180d value is the modal one: 71 of the S8xx rows; 6×365d, 3×90d). used-by = `corpus/knowledge/linguistics/conlang-scholarship.md`, which exists at 0316b88 and cites S876 on lines 3, 30-33 (quote, second claim, keywords, "abstract is the whole opened artefact"). The row is `mined` and has a real citer → consistent. The Gate row (round-73.md:18) agrees with the evidence file on date, quote, locator, bytes, sha prefix, UA.
9. **Tier/scope overclaim:** SOURCES.md contract: A = primary/authoritative for scope incl. "original paper"; B = strong secondary. Row says Tier B and states "one author's argument in one article (the opened artefact is the abstract), not a venue-wide consensus"; the knowledge file line 33 repeats that it is a position, not a measured outcome. This is a self-limiting scope; no overclaim found. (Debatable that an original paper could be A, but B is the conservative direction.)

## Findings
- **MINOR-1 (scope cell paraphrase drifts from the abstract).** Row cell 5 says "the reasons linguists marginalize natural languages in teaching are the reasons they marginalize conlangs in research". The abstract (page line 267) says: "the reasons that lead **me** to marginalize natural languages from teaching are the same ones that lead **most** linguists to marginalize constructed languages from research." The row attributes the teaching-side marginalization to "linguists" generally rather than to the author, and drops "most". Likewise "lets students grasp" drops "better … than does the repetition of exercises based on data from natural languages". The knowledge file's own wording (conlang-scholarship.md:30-31) is faithful ("him", "most linguists", "than repeated exercises"), so only the registry scope cell is loose; the anchor quote and tier are unaffected. Proof: compare `sed -n 267p /tmp/ScoutReopenS876/live-browser.html` with `git show 0316b88:corpus/SOURCES.md | sed -n 831p`.
- **MINOR-2 (the word "peer-reviewed" has no recorded evidence).** The row and Gate row call this a "peer-reviewed statement"; `grep -c peer` on `reports/round-73/evidence/S876.txt` → **0**, and the article page itself has no peer-review statement (it only shows Section "CrOCEVIA"). I found support on the journal pages I fetched now: about page — "RiCOGNIZIONI is an open-access, peer-reviewed journal" and "uses a double blind peer review"; "Every proposal submitted … is sent to two reviewers". But the submissions page also says "Se si sta facendo la submission a una sezione peer-reviewed" (OJS boilerplate implying some sections may not be reviewed), and the about page does not say which sections are reviewed. So journal-level peer review is verified true live; that this article (section CrOCEVIA, described as "features papers…") was reviewed is inferred, not shown, and the claim's provenance is not in the committed evidence. Doesn't affect the admitted quote.

## Not checked / limits
- Whether the article's PDF (the "Downloads PDF" link) carries more than the abstract — not opened; the row correctly says the opened artefact is the abstract.
- Whether the lane's craft manuals "never mention" teaching/research asymmetry beyond `corpus/knowledge/**` at 0316b88 — git grep for marginali*/conlang-teach terms outside the new files, lessons and registry returned only the README line listing conlang-scholarship.md; manuals outside this lane's corpus not examined.
- Whether the round-73 gate tools (`tools/check-gate-quotes.py`, accept-c.py) pass — not run (not in scope; no counter runs).
- Sections' per-article peer-review status (see MINOR-2).
- The article was fetched once per UA per URL; no repeated-fetch stability test beyond live == evidence hash.
