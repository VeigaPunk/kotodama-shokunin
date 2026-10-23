# ExecRowS740 — row S740 (claim C, mined row; topic: honorifics and keigo acquisition, entry section ## 8)

Axes named: **coverage (C)**, **operability (O)**, **calibration (Ca)**. This seat executed only the assigned row contribution for S740. No counter was edited, no entry integrated, no registry row appended, no sibling row touched, no commit, no jj/git index mutation, no tool installed.

## Verdict

S740 row is **written and self-checked**: `.ufo/waves/round-64/rows/ScribeRowS740/row.txt` (3280 bytes, 5 labelled lines, LF only) — the directory the inherited attempt-1 left MISSING. `python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows` prints `S740 OK` and the wave is now `CHECK-ROWS: 32/32 clean`.

The inherited recon lead survived re-verification with one material correction recorded below: the UC Press live URL is Cloudflare-403 to plain clients, so the row's evidence lives in the same-page Wayback capture, and that capture is fetched intermittently (429) from this network.

## Steps executed (commands and outputs)

### (1) Live URL, plain curl

```sh
curl -sSL -o live.html -w "status=%{http_code} url=%{url_effective} size=%{size_download} ctype=%{content_type}\n" \
  -A "Mozilla/5.0 (X11; Linux x86_64; rv:131.0) Gecko/20100101 Firefox/131.0" \
  "https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early"
```

```text
status=403 size=5787 ctype=text/html; charset=UTF-8
```

Body is a Cloudflare "Just a moment..." interstitial (`<title>Just a moment...</title>`, `challenges.cloudflare.com`). Repeated 5× (Firefox UA and a full Chrome UA with `Accept-Language`/`Sec-Fetch-*` headers): `403` every time, 5787 bytes every time. The two publisher PDF paths (`/collabra/article-pdf/doi/10.1525/collabra.18989/835053/collabra_2021_7_1_18989.pdf`, from the Crossref `link` field, and `/collabra/article-pdf/7/1/18989/404018/...`) also returned `403` with a Cloudflare body. Python `urllib` with the same UA: `HTTPError HTTP Error 403: Forbidden`.

The article itself is real, open access and correctly identified: Crossref `10.1525/collabra.18989` → "The Role of Parental Input in the Early Acquisition of Japanese Politeness Distinctions", Chang / Tatsumi / Hayakawa / Yoshizaki / Oka, `Collabra: Psychology`, 2021, 67 references; Unpaywall `is_oa: true`, licence `cc-by`; OpenAlex `is_oa: true`, journal `Collabra Psychology`. So the block is bot protection, not a paywall — which is why the archived copy of the same page is admissible.

### (2) Same-page archived capture

```sh
curl -sS "https://archive.org/wayback/available?url=https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early"
```

```json
{"url": "https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early",
 "archived_snapshots": {"closest": {"status": "200", "available": true,
  "url": "http://web.archive.org/web/20231203082010/https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early",
  "timestamp": "20231203082010"}}}
```

The `closest` snapshot 20231203082010 is **not** usable: fetching it returns the IA "loading" JS challenge (874 bytes, no article text). The CDX listing for the same URL shows four status-200 `text/html` captures with full bodies:

```text
edu,ucpress,online)/collabra/article/7/1/18989/116377/the-role-of-parental-input-in-the-early 20210303000525 ... text/html 200 ... 46542
edu,ucpress,online)/collabra/article/7/1/18989/116377/the-role-of-parental-input-in-the-early 20210414114152 ... text/html 200 ... 53447
edu,ucpress,online)/collabra/article/7/1/18989/116377/the-role-of-parental-input-in-the-early 20210418002427 ... text/html 200 ... 53445
edu,ucpress,online)/collabra/article/7/1/18989/116377/the-role-of-parental-input-in-the-early 20210420051508 ... text/html 200 ... 53443
```

`https://web.archive.org/web/20210414114152id_/<live URL>` fetched with HTTP 200, 243294 bytes of body, `<title>The Role of Parental Input in the Early Acquisition of Japanese Politeness Distinctions | Collabra: Psychology | University of California Press</title>`. The availability API re-queried with `&timestamp=20210414114152` returns that same capture with `status: 200`, confirming it is the archived copy of the cited URL and not of a different page.

### (3) Quote — 22 words, contiguous body text

The capture's full text was extracted (script/style stripped, tags removed, entities unescaped) and the section **"The Role of Honorific and Diminutive Titles in the Development of Politeness Distinctions"** read. The quote is a body paragraph of that section, contiguous in the raw HTML (verified by direct substring test `q in h → True`):

> These overgeneralizations suggest that children are not just memorizing the forms in their input, but also generating novel forms from a rule.

It is exactly on the assigned topic: children's acquisition of the honorific/diminutive title system (san vs chan/kun) from family input, with the paper's own examples of children producing *yuubinyachan* for adult *yuubinyasan* and *Puuchan* for adult *Puusan*. Under the lane's `norm_words` the quote is **22 words**, inside the frozen 8–25 band.

### (4) Lane locator from the lane root

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py \
  'https://web.archive.org/web/20210414114152id_/https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early' \
  'These overgeneralizations suggest that children are not just memorizing the forms in their input, but also generating novel forms from a rule.'
```

```text
LOCATED https://web.archive.org/web/20210414114152id_/https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early
```

Tally over the session (the locator, unmodified, run from the lane root): **8 LOCATED**, **13 NOT_LOCATED** with `HTTPError` / `URLError` (the final three runs, after the archive had rate-limited this network, were all `HTTPError`). Direct diagnosis of the failures: `urllib` against the same capture URL returned `HTTPError 429 Too Many Requests` on 6/6 attempts in one batch and `URLError` (connection refused) on others, while `curl` with the same URL succeeded. The failures are archive-side rate limiting on this network, not a missing quote: the same capture body (243294 bytes) contains the quote verbatim, and every LOCATED run found it. The live URL never located (403).

Run in `--row` mode against a scratch registry containing only the S740 row (i.e. exactly what `accept-c.py`'s LIVE leg will do after integration):

```text
LOCATED https://web.archive.org/web/20210414114152id_/https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early
EXIT=0
```

and on a later attempt under load:

```text
NOT_LOCATED https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early HTTPError; https://web.archive.org/web/20210414114152id_/https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early HTTPError
```

### (5) Row file written

`.ufo/waves/round-64/rows/ScribeRowS740/row.txt`, lines labelled `ROW` / `BULLET` / `VERIFY` / `CAPTURE` / `ACCESS` (model: `ScribeRowS739/row.txt`). The `ROW` line is one pipe row with **11 cells**:

| cell | value |
|---|---|
| 1 | `S740` |
| 2 | source: Chang, Tatsumi, Hayakawa, Yoshizaki & Oka (2021), "The Role of Parental Input in the Early Acquisition of Japanese Politeness Distinctions", *Collabra: Psychology*, 7(1):18989 — live URL `; capture` archived URL |
| 3 | `paper` |
| 4 | `A` (peer-reviewed open-access research article; the primary record for this scope) |
| 5 | scope: acquisition of honorific (san) and diminutive (chan, kun) noun titles by Japanese children, in recorded Japanese CHILDES child speech and a Kyoto kindergarten video-production task |
| 6 | anchor: section "The Role of Honorific and Diminutive Titles in the Development of Politeness Distinctions", paragraph on overgeneralization, with the quoted sentence |
| 7 | teaches: children overgeneralize noun titles rather than copying input verbatim, and parental use of san for parent names does not grow with the child's age, so a designed address system can be rule-governed and still be mislearned |
| 8 | `mined` |
| 9 | `2026-10-23` |
| 10 | `180d` |
| 11 | `corpus/knowledge/linguistics/language-socialization-and-acquisition.md` |

`kind` is `paper`, matching the lane's registry vocabulary (used by sibling rows S718, S720, S733 for journal articles). `VERIFY` names the archive URL because that is the URL the locator actually located; `CAPTURE` records `timestamp=20210414114152` and the identical original URL.

### (6) Self-check

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows
```

```text
S740 OK
CHECK-ROWS: 32/32 clean
```

## Cross-checks against the frozen instruments (read-only)

- `check-rows.py` — `S740 OK`: 11 cells, tier A, status `mined`, opened `2026-10-23`, recheck `180d`, used-by exact, quote 22 words (8–25), live URL present and unique, capture present with matching original, bullet shape `- … (S740)`, ≥5 content words, ≥3 quote words in quote order, a novel content word present, longest verbatim copy run ≤12, `VERIFY` starting with `LOCATED`.
- `reports/round-64/accept-c.py` — its `ROWS`/`LINK` logic was replicated against a scratch registry (`corpus/SOURCES.md` + the S740 row) without touching the real registry: cells 11 ✓, tier A ✓, status mined ✓, opened/recheck ✓, used-by contains the entry path ✓, quote band ✓, live URL present ✓, capture present and `norm_url(capture original) == norm_url(live url)` ✓, registry lines containing the live URL = **1** ✓, live URL absent from the entry file ✓.
- `reports/round-61/reopen-quote.py` — `--row S740` on a scratch registry printed `LOCATED` (see above).
- `tools/reopen-row.py` — run against a scratch registry holding only the S740 row: `ROW S740 LOCATED attempts=3 url=https://web.archive.org/web/20210414114152id_/…` and `REOPEN: 1/1 located`. The tool's own bytes were not edited.
- `.ufo/waves/round-64/integrate-w2.py` — `parse_contribution(path, "S740", rejected=False)` accepted the file: 11 cells, status `mined`, used-by exactly `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`, bullet one line ending with exactly `(S740)`, all five required labels present. `BULLET_MAP[8]` is `("S739", "S740", "S741")`, so this row lands in entry section ## 8 "Names, address and honorifics" as the assignment states.
- The RESTATE-leg arithmetic was computed independently: bullet content words 13, quote words matched in quote order 5 (≥3), novel content words `{diminutive, honorific, only, overgeneralize, rather, than, titles}`, longest verbatim copy run from the quote 6 (≤12).

## Named defects

1. **Live URL is unreadable by a plain client (material, recorded in the row's ACCESS line).** `https://online.ucpress.edu/collabra/article/7/1/18989/116377/The-Role-of-Parental-Input-in-the-Early` returns HTTP 403 with a Cloudflare interstitial on every plain request (5/5 attempts, two user agents, plus Python `urllib`). The paper is open access (CC-BY per Unpaywall/OpenAlex), so this is bot protection rather than a paywall, and the row's evidence is the same-page archived copy, whose body carries the quote verbatim. This mirrors sibling S724 (live 403, archive-carrying row) and S741's neighbourhood; the lane's own tool accepts it (`tools/reopen-row.py` → LOCATED via the archive URL). Flagged for the reviewer because a reader clicking the live link in a plain client will not see the article.
2. **The archived capture is fetched intermittently from this network (material, recorded in the row's ACCESS line).** The lane locator printed LOCATED 8 times and NOT_LOCATED 13 times; every failure was `HTTPError`/`URLError` from `web.archive.org` (429 Too Many Requests observed 6/6 in one direct batch, connection refused in others), while the same body is verifiably quote-bearing. `accept-c.py`'s LIVE leg retries three times 20 s apart for its frozen subset, which is why that leg exists; **S740 is not in `LIVE_IDS`** (`accept-c.py:45`: `(n - 717) % 5 == 1` → S718, S723, S728, S733, S738, S743), so the frozen LIVE leg will not exercise this row, but a reviewer re-running the locator on S740 may see intermittent red. Not a counter defect; recorded so the reviewer interprets it correctly. No counter was weakened and no counter was edited.
3. **The availability API's `closest` snapshot for this URL is unusable.** `available?url=<live URL>` returns 20231203082010, which replays as a JS challenge page with no article text; the usable same-page captures had to be enumerated from CDX, and the API re-queried with `&timestamp=20210414114152` confirms the chosen capture. This is a property of the archive, not of the row; recorded in ACCESS so the next reader does not re-walk it.
4. **The named fallback was tried and is unusable here (recorded).** The brief's fallback is Nakamura's "The acquisition of linguistic politeness in Japanese" (Cambridge handbook chapter). `www.cambridge.org` returned HTTP 429 to every plain request (3/3, including the Crossref `link` PDF endpoint `…/content/view/3B85FB0ADC3E17860078EE9756A6AF81` and the chapter landing page), and its 20180613065848 same-page capture carries only the Cambridge landing page (4876 characters of navigation chrome, no chapter body), so it offers no quotable body text either. The Collabra lead is therefore the only viable source of the assigned topic, and it is open access and peer-reviewed.
5. **Scope wording corrected during the write.** The first draft of the scope cell called the study "a Kyoto kindergarten picture-naming task"; the article describes a video-based production task (children produce what a child in a shop-errand video would have said, with formal/informal blocks). The cell now says "video-production task". The quoted sentence is unaffected.
6. **No defect found in the assigned source choice.** The recon lead is a peer-reviewed, CC-BY, open-access research article whose full text is available under a stable same-page archive URL, and whose §"The Role of Honorific and Diminutive Titles in the Development of Politeness Distinctions" is exactly the assigned topic (honorifics and keigo acquisition by children).

## Affected axes

- **Coverage (C) — improved, none harmed.** One of the 26 claimed mined rows now exists in the exact form `check-rows.py` and `accept-c.py` demand, with a topic-faithful anchor quote, and the wave's row check is now 32/32 clean. The row was validated against the frozen `reports/round-61/reopen-quote.py` bytes and against `tools/reopen-row.py`, not merely asserted.
- **Operability (O) — not harmed.** `tools/reopen-row.py` and `accept-o.py` bytes were not edited; the tool was only executed read-only against a scratch registry and located the row.
- **Calibration (Ca) — not harmed.** No bookkeeping file was touched (`LOG.md`, `SCORECARD.md`, `corpus/LOG.md`, `reports/round-63/telemetry/revisions.txt` are as the working tree had them; `git status` shows those as pre-existing modifications, not mine). The row records what the cited page says at its scope, including the honest note that parental san use for parent names did not increase with the child's age.

## Risks and blockers

- **Not verified here:** the whole-predicate `ACCEPT-C-64` run. `accept-c.py` needs the assembled entry, the appended registry rows and the README index row; none of that exists yet, so an unrun check has not passed. The L1 must run `python3 -B reports/round-64/accept-c.py` after integration.
- **No integration performed.** `corpus/SOURCES.md`, `corpus/knowledge/linguistics/language-socialization-and-acquisition.md` and `corpus/README.md` are untouched by this seat, as assigned; `NOHARM` is unaffected by me.
- **Locator flakiness on this row** (defect 2) is the main residual risk for any reviewer who re-checks S740 by hand; the mitigation already built into the frozen counter (three attempts, 20 s apart) applies to `LIVE_IDS` and does not include S740.
- **Live-link usability** (defect 1): a plain-client click on the live URL shows a Cloudflare interstitial; the archive URL in the same cell is the working copy.
- **Host clock.** The row's `opened` date 2026-10-23 is the local (UTC-3) calendar date, the same convention every sibling row in this wave uses.

## Files changed

- `.ufo/waves/round-64/rows/ScribeRowS740/row.txt` (created — the assigned deliverable)
- `.ufo/waves/round-64/w1/ExecRowS740.md` (this report)

No other file was written, edited, moved or deleted. Scratch (fetched copies, the scratch registry, the IA challenge solver) lives only in `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ExecRowS740/`. No tool was installed or updated (no pacman, no uv/npx, no binary fetch) — the task needed only `curl`, `node` (already present, used only to evaluate the archive's own JS challenge) and the lane's Python.

Report: .ufo/waves/round-64/w1/ExecRowS740.md
