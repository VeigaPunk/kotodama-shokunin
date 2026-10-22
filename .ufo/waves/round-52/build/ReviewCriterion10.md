# ReviewCriterion10: QUALITY criterion 10 and tools/check-source-access.py

Reviewer report, read-only. Lane: `kotodama-shokunin` (main; claim base `147cfde`; D landed `dea5ece`). All access checks ran 2026-10-22. No lane file was edited and no SOURCES row was added. Nothing was installed. Sandbox (outside the lane): `/fast/scratch/hyaku/kotodama-r52/ReviewCriterion10/` (a `git archive` snapshot of `147cfde`, the downloaded Wayback pages, and the proposed checker).

## Verdict

1. **On today's registry the checker is right.** It flags exactly S094 and S132. Both record a bypass and both are `rejected`. I found no unflagged bypass and no wrongly flagged ordinary route in the 133 rows. The sign entry has 0 S094 lines, and it has no Battison 1974 mention without `(to-verify)`.
2. **The checker is weaker than criterion 10 says.** Each gap below exits 0 on a bad registry. None is triggered by a current row, so all are latent.
3. **Parts of the wording cannot be tested from committed bytes.** Other parts conflict with criterion 1, criterion 6, the SOURCES header and criterion 9's receipt.
4. **Round-52 grounding has two factual errors.** The "6 findings on the round-52 base" receipt comes from an older tree. The `#mistakes` anchor it cites does not exist.
5. **A tested replacement is drafted** (section 4): criterion text, grounding sentence, S132 follow-up and a checker patch. The patch exists only in the sandbox.

## 1. Findings by severity

**F1 · High · latent · bypass wording is a three-part denylist that misses common phrasings.**
- Evidence: `BYPASS` at `tools/check-source-access.py:32-35` matches `headless`, `bypass(ed|ing)`, and `solved (a|the) (bot) captcha|challenge`. I probed 16 bypass phrasings in memory against the real regex. It missed **16 of 16**: "solved the Cloudflare challenge", "solved CAPTCHAs", "bypasses the paywall", "got past the bot challenge", "passed the AWS WAF JS challenge", "solving a captcha", "solved hCaptcha", "stealth browser", "undetected-chromedriver session", "Playwright session", "logged in with a shared account", "via Sci-Hub", "circumvented the paywall", "user-agent spoofed", "by-passed the login", "clear the Turnstile".
- Current registry: no miss. Section 2 covers every row with an access term, plus a second sweep with about 40 further terms.
- Fix: the regex in section 4.4. The proposed regex catches all 16 probes.

**F2 · High · latent · "status rejected through a superseding row" is not tested.**
- Evidence: `check()` tests only the status text (`tools/check-source-access.py:63-65`). A temp registry with a headless-route row marked `rejected` and no superseding row exits 0 with 0 findings (demonstrated).
- Fix: flag a rejected row that has no row whose teaches opens `supersedes <id>` (section 4.4). The proposed patch also exempts superseding records, so S132 passes.

**F3 · Medium-high · latent · the citation leg counts S-ids only.**
- Evidence: `tools/check-source-access.py:70-81` matches S-ids only. Demonstrated exit 0 for "Battison 1974 reports X." and for a URL to the flagged host, both in `corpus/knowledge`.
- Real case on base `147cfde`: `sign-languages-manual-modality.md:92` reads "six shapes in Battison 1974 (S094)". The S-id leg catches this line only through "(S094)". The proposed author-year leg catches the same line from the author and year alone. At the lane head the author-year hits are 0.
- Fix: add author-year and URL legs. Author-year mentions are allowed only with an inline `(to-verify)`, which criterion 1 already requires (`QUALITY.md:5-8`).

**F4 · Medium · latent · malformed row ids disappear without an error.**
- Evidence: `ROW` at line 31 needs three digits. A line `| S94 | … headless … |` next to a valid row was dropped silently: `parse_rows` returned only `S095`, so the run exits 0 (demonstrated).
- Lane: 133 row-like lines and 133 strict parses, so there is no current effect.
- Fix: parse leniently, then raise if a row-like line does not parse strictly (section 4.4).

**F5 · Medium · latent · the route note is read from three cells, not four.**
- Evidence: `flagged()` reads source, anchor and teaches (lines 52-53). `scope` is not read. The proposed sweep found no scope hits in the lane.
- Fix: read `scope` too.

**F6 · Medium · known false positives, by design.**
- Evidence: a disclaimer such as "no headless browser was used", a negation such as "did not solve the captcha" in the proposed regex, and a mined superseding row whose history clause names the earlier route ("supersedes S000 — S000 was opened via headless browser; this copy is a plain request") all produce a finding (demonstrated).
- Lane: 0 current false positives. The two flagged rows describe real bypasses.
- Fix: keep the fail-closed behaviour and document it. Authors should not name a forbidden route in a disclaimer or history note.

**F7 · Medium · wording overclaims what the check tests.**
- Evidence: the `Check:` line presents exit 0 as the check for the criterion. It proves only that the route notes in the rows contain no listed vocabulary. "A fresh session can reach it the same way" cannot be tested from committed bytes. It is a live, time-varying fact. The IDA PDF, for example, was 403 on 2026-10-22 and may not be later.
- Undefined terms: "access note" (no such column), "plain request", "public copy", "library scan", "routed around", and "opened" for partial access.
- Fix: the replacement text in section 4.1.

**F8 · Medium · conflicts with other rules.**
- (a) Criterion 1 counts author and year as "checkable" (`QUALITY.md:5-8`). Criterion 10 says no entry cites an unopened source. Resolve it with `(to-verify)`, which criterion 1 already allows.
- (b) Criterion 6 treats abstracts as usable tier B (`QUALITY.md:29`). Criterion 10 is silent on partial access. Affected rows: S032, S035, S036, S101, S102 and S118. All are honest in their scope cells, but the criterion does not say how partial access counts.
- (c) SOURCES header lines 9-12 allow `status` to change in place. Criterion 10 requires a superseding row. The S094 change did both, which satisfies both rules, but the header does not say a superseding row is required.
- (d) Criterion 9 cannot see the access check. `tools/check-source-access.py` appears in neither `reports/round-52/claims.json` nor `reports/round-52/telemetry/declaration-dry-run.txt`. `claims.json` also names no acceptance command for C; its `after_required` says only "the acceptance command exiting 0".

**F9 · Medium · grounding errors in criterion 10 and the round-52 lesson.**
- (a) "shown able to fail on the round-52 base (…: 6 findings, exit 1)" (`QUALITY.md:37`; `corpus/lessons/round-52.md:16`). The receipt's first line says `tree=main 2b956d7c … before any registry change` (`reports/round-52/telemetry/prereq-access-check.txt:1`). That is the round-51 tip with the checker added, not the base. Re-run on `147cfde`: 2 flagged rows, **5** findings, exit 1 (section 3.1).
- (b) `corpus/lessons/round-52.md#mistakes`. No `Mistakes` heading and no R52-M1 entry exists at lane head. The sections are at lines 10, 25 and 37 (Spot-check intake, Gate, Status and used-by change log). Land the section before closure.

**F10 · Medium · calibration of S132.**
- S132 (`SOURCES.md:161`) says "no copy reachable by ordinary means". That holds for the routes it names and for the routes I tested (section 3.2). It overstates "no copy exists". The repository's own search snippet labels the same PDF open-access, and I did not test other repositories or library scans. Its flip list names publisher, Project MUSE and library scan, but not archive capture, which criterion 10 lists as ordinary.
- Fix: a superseding row with the routes and dates (section 4.3). Do not edit S132's anchor in place (`SOURCES.md:9-12`).

**F11 · Low · Wayback reliance needs an explicit statement.**
- S093 (`SOURCES.md:122`) and S062 (`:91`) imply that the challenge was met and not passed, but neither says so. The replacement text requires the row to say it.

## 2. Registry sweep (every access-related row)

| Row (line) | Route in its cells | Checker result | Verdict |
|---|---|---|---|
| S094 (123) | "Cloudflare-gated, opened via headless browser" | flagged; `rejected` | correct |
| S132 (161) | superseding record; history clause names the bypass | flagged; `rejected`; not cited | correct; harmless |
| S133 (162) | superseding anchor fix | not flagged | correct |
| S093 (122) | AWS WAF JS challenge; read via Wayback 20241210011800 | not flagged | ordinary (F11) |
| S062 (91) | live CAPTCHA; read via Wayback 20241219152138 | not flagged | ordinary (F11) |
| S064 (93) | host timed out; read via Wayback 20260605210113 | not flagged | ordinary; status checked only |
| S123 (152) | live HTTP 403; read via Wayback 20221222142436 | not flagged | ordinary; status checked only |
| S032 (61) | ScienceDirect body HTTP 403; arguments unread | not flagged | correct; metadata scope |
| S035, S036 (64, 65) | JSTOR paywalled or blocked; argument unread | not flagged | correct; metadata scope |
| S101 (130) | full text paywalled; abstract only | not flagged | correct; abstract scope |
| S102 (131) | JSTOR blocked; Cambridge Core 429 | not flagged | correct; abstract scope |
| S118 (147) | abstract only | not flagged | correct; abstract scope |
| S052 (81) | Duke-hosted copy of an Internet Archive scan | not flagged | ordinary public copy |
| S028, S029, S030, S043, S047 (57, 58, 59, 72, 76) | login-, member- or paywall-gated | `rejected` | correct; rejected for other reasons |

Knowledge tree: `sign-languages-manual-modality.md` lines 83, 87, 90, 92 and 93 carry Battison 1978 attributions (credited to S096 and S097) and no S094 or S132. Line 92 carries "an earlier, smaller 1974 set is not checked here (to-verify)". `awk '/S094/{n++} END{print n+0}'` returns 0. The D counter is therefore 5 → 0, as claimed.

Second sweep: about 40 more terms (scraping, mirror, token, user-agent, rate limit, interstitial, JS challenge and others). It matched only S028 (a scraping reservation, rejected) and S093 (its own JS-challenge note, read via Wayback). No unflagged bypass.

## 3. Evidence: outputs and routes

### 3.1 Checker runs (`python3 -B tools/check-source-access.py`)

- Lane head, `--selftest`: `SELFTEST: 10/10 pass`, exit 0.
- Lane head, real run: `ACCESS: 2 flagged rows, 0 findings`, exit 0.
- Base `147cfde` (snapshot in the sandbox): `ACCESS_FINDING cited S094` at sign-entry lines 83, 87, 90, 92 and 93, then `ACCESS: 2 flagged rows, 5 findings`, exit 1.
- Prerequisite receipt, tree `2b956d7`: 1 status finding plus 5 cited findings = 6, exit 1 (`reports/round-52/telemetry/prereq-access-check.txt:23`).
- Proposed patch (section 4.4), sandbox only: selftest 19/19; lane 2 flagged and 0 findings, exit 0; base `147cfde` 2 flagged and 6 findings, exit 1. The sixth finding is the author-year hit on line 92.

### 3.2 Routes tested for S094 and S132 (plain requests, default curl identity, 2026-10-22)

| Route | Result | Reading |
|---|---|---|
| Repository PDF, `https://ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls` | HTTP 403, `cf-mitigated: challenge` | blocked; the lane's 10:38Z request (with a browser-style user agent) got the same result |
| Repository landing page, `https://ida.gallaudet.edu/sls/5/` | HTTP 200 | reachable; the PDF link is the same challenged URL |
| Wayback exact-URL index (CDX) for the PDF URL | HTTP 200, body `[]` | no capture indexed for this URL |
| Wayback 2024 prefix for the PDF URL | HTTP 404 | not conclusive; the CDX result is the decisive one |
| Project MUSE, DOI `10.1353/sls.1974.0005` → `muse.jhu.edu/article/507140` | 302 to `/verify`: "Verification required!" with a challenge widget | gated |
| JSTOR, `https://www.jstor.org/stable/26203099` | HTTP 200, page title "Client Challenge" | gated |
| Web search index (snippet, not counted as a source) | labels the repository PDF "open-access" | consistent with the repository route |

S132's negative holds for these routes. It is unverified for other repositories and for library scans.

### 3.3 Wayback captures checked for content (ordinary route, not a bypass)

- `web.archive.org/web/20241210011800/https://www.hup.harvard.edu/books/9780674270411` (S093): HTTP 200. The page carries the title "Everyone Here Spoke Sign Language" and the Martha's Vineyard description. The direct page returned HTTP 202; I did not read its body, so the challenge reading is the row's, not mine.
- `web.archive.org/web/20241219152138/https://ich.unesco.org/en/RL/traditional-craftsmanship-of-the-mongol-ger-and-its-associated-customs-00872` (S062): HTTP 200. The description says the ger is "light enough for nomads to carry".
- S123 and S064 captures returned HTTP 200. I did not check their content.

## 4. Drafted text (ready to paste or adapt)

### 4.1 Criterion 10 (replaces `corpus/QUALITY.md:37`)

> **10. Sources are opened by ordinary means** — a source counts as opened only when a fresh session could reach it on its access date by an ordinary means: a plain request sent with the client's default identity (no added cookie, header or user-agent override); a public copy (the publisher's or author's own open copy, an open repository, or a scan in a public archive that any reader may open, not a lending copy); an archive capture; or a publicly reachable library scan. Institutional or personal logins, shadow libraries (Sci-Hub, LibGen, Z-Library), headless browsers, and solving a captcha or challenge are not ordinary means. A row whose source, scope, anchor or teaches cell records a route outside these counts as unopened: its status is `rejected`; a superseding row whose teaches opens `supersedes <id>` keeps the reason; and no knowledge entry cites it by S-id or URL, or by author and year unless that sentence carries an inline `(to-verify)` mark. A challenge that the lane met and did not pass, followed by a read of an ordinary copy (for example a Wayback capture), is not a bypass, and the row must say the challenge was not passed; a challenge that was solved, answered or passed is one. A source reached only in part (an abstract, a metadata record, a refused body) counts as opened for that part only; its scope cell names the part, and any claim beyond it carries `(to-verify)`. Check (self-declared route notes only): `python3 -B tools/check-source-access.py` exits 0 and `--selftest` passes. The check cannot test live reachability.

### 4.2 Grounding sentence (replaces the last clause of `QUALITY.md:37`)

> Grounded in the round-51 outside spot-check at `corpus/lessons/round-51-verifier-spotcheck.md#discernment-spot-check` (S094 disagree: HTTP 403, Cloudflare challenge, opened via headless browser) and in the round-52 lesson's R52-M1 (the section must land first). At `147cfde` the checker gives 2 flagged rows and 5 findings, exit 1; the prerequisite receipt `reports/round-52/telemetry/prereq-access-check.txt` records 6 findings at tree `2b956d7`, before the registry change.

### 4.3 S132 follow-up (a new superseding row; do not edit S132 in place)

The L1 assigns the next free id. Its teaches opens `supersedes S132 —` and records the routes in section 3.2 with the 2026-10-22 date, plus the Wayback result. Its flip adds an ordinary copy opened by plain request, a public archive capture, and a publicly reachable library scan.

### 4.4 Checker patch (sandbox only: `/fast/scratch/hyaku/kotodama-r52/ReviewCriterion10/patched/check-source-access-proposed.py`)

Changes against `tools/check-source-access.py`:
1. **Bypass vocabulary.** A verb (solved, answered, passed, cleared, got past, opened, read, accessed, downloaded and others) followed within 60 characters by an access noun (captcha, hCaptcha, Turnstile, paywall, login, sign-in, or a challenge with a qualifier such as bot, JS, Cloudflare, WAF or browser). Plus `headless`, bypass, circumvent, spoof, Sci-Hub, LibGen, Z-Library, stealth, undetected, Playwright, Puppeteer, Selenium and "log in with a shared account".
```
BYPASS = re.compile(
    r"\bheadless\b"
    r"|\bby-?pass(?:e[sd]|ing)?\b"
    r"|\b(?:circumvent|evad|spoof)(?:e[sd]|ing)?\b"
    r"|\b(?:sci-?hub|libgen|library genesis|z-?library|shadow librar(?:y|ies)|stealth|undetected|puppeteer|playwright|selenium|chromedriver|2captcha|anti-?captcha)\b"
    r"|\b(?:solv(?:e[sd]?|ing|er)|answer(?:ed|ing)|pass(?:ed|es|ing)|clear(?:ed|ing|s)?|beat|beaten|got\s+past|get\s+past|getting\s+past|gets\s+past|worked\s+around|opened|read|accessed|downloaded|retrieved)\b[^|;]{0,60}?\b(?:captchas?|hcaptcha|recaptcha|turnstile|paywalls?|logins?|sign-?ins?|(?:bot|js|javascript|cloudflare|waf|browser|managed|interstitial|anti-?bot|access)\s+challenges?)\b"
    r"|\b(?:logged[- ]in|log[- ]in)\s+(?:with|using|via)\s+(?:a\s+|an\s+)?(?:shared|someone|another|borrowed|stolen)\b",
    re.IGNORECASE,
)
```
2. **Cells.** Read source, scope, anchor and teaches.
3. **Superseding leg.** A flagged row marked `rejected` needs a row whose teaches opens `supersedes <id>`, unless its own teaches opens `supersedes` (a superseding record).
4. **Citation legs.** S-ids and URLs are never allowed in `corpus/knowledge`. Author and year are allowed only with `(to-verify)` on the same line.
5. **Strict parse.** A line starting `| S<digit>` must parse as an 11-cell row with a three-digit id, or the check exits 2.

Results: selftest 19/19 (the original 10, two of them extended with a superseding row, plus 9 new cases). Lane: 2 flagged rows, 0 findings, exit 0. Base `147cfde`: 2 flagged rows, 6 findings, exit 1.

Known residual false positives (documented, fail-closed): negations such as "did not solve the captcha", and history notes that name a forbidden route.

## 5. Residual risk and verification gaps

- A word list cannot read intent. A bypass described in new words will slip through, so the reviewer's reading of the route notes remains the real control.
- Reachability is a live, time-varying fact and is not testable from committed bytes. The checker can only test what the rows say.
- Not tested, and not attempted: institutional or library access (no credentials), and shadow libraries (not to be touched).
- Not run: the criterion 9 receipt regeneration and the separability checker. Both are outside this review.
- The Wayback 2024-prefix query returned 404 and was not conclusive. The archive.org availability API returned 429 once and I did not retry. Two early connection failures to `web.archive.org` were transient, and later calls succeeded.
- I did not solve any challenge or add any header, cookie or user-agent override. The lane's telemetry used `-A Mozilla/5.0` (receipt line 25). My requests used curl's default identity, and both got the same 403 challenge.
- Symlinked directories under `corpus/knowledge` are skipped silently by `os.walk`. I did not check whether any exist.

## 6. Coordination

I sent one message to `KotobaR50.SrcOpencodeDocs` (peer write, delivered). It said I claim no S-id and add no SOURCES rows. It also said that at this lane's head S024 and S025 are already taken (the registry runs S001–S133), and that the message may not apply if their registry belongs to another lane.
