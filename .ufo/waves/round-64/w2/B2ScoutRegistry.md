# Round-64 registry row rules (for row seats)

Seat B2ScoutRegistry. Read-only against the lane. No tool installed.

Axes: exactness (symptom strings copied from the counter), coverage (every cell and every bad-list append), applicability (a seat can file without re-reading the counter).

Sources, all read this session:

- Contract v1: `/home/vgpnk/Projects/shokunin/CORPUS.md` lines 64-148, section "SOURCES.md — where a shokunin learns" (frozen). The lane has no CORPUS.md. The lane restatement is `corpus/SOURCES.md` lines 1-22 and the header at line 28.
- Counter: `reports/round-64/accept-c.py`. ROWS at 180-222, REJECTS at 223-245, RESTATE at 268-314, HOSTS at 316-328, LINK at 330-340, LIVE at 385-426. A leg prints `LEG PASS detail` or `LEG FAIL detail`.
- Quality: `corpus/QUALITY.md` criterion 6 (line 29), 10 (line 37), 12 (line 41), 13 (line 43), 16 (line 49).
- Exemplars: `corpus/SOURCES.md` lines 649-672 (S694-S717).
- Locator the LIVE leg runs: `reports/round-61/reopen-quote.py` (`normalise` line 77, `locate` 195-216, `row_target` 226-231).

Confidence: high on every symptom string and on the three tier cases (quoted from those files). The order of the ten failures is likelihood for a seat copying S694-S717, marked [INFERENCE] at item (d).

Mined ids: S718-S743 (26). Disposition ids: S744-S749 (6). The mined used-by cell must contain this path: `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`.

## (a) The 11 cells

A data row is one line, column 0, starting and ending with a pipe. `cells()` is `line.split("|")[1:-1]`, each piece stripped. The counter requires exactly 11. The contract census says the same thing as awk `NF==13` (the two empty end fields). No pipe inside a cell: one extra pipe yields `cells=12` and the counter `continue`s, so later faults on that row are not reported. A leading space makes `ROW_RE` (`^\|\s*(S\d+)\s*\|`) miss the line, which then looks like a missing id.

Round template, tighter than contract v1:

`S###` / citation, then ` - `, then the live URL, then ` ; capture `, then the archive URL / kind / tier / scope / locator then `: "quote"` / teaches / `mined` / `2026-10-23` / `180d` / `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`

Normalisation for the 8-25 count (`norm_words`, lines 89-91): NFKC, casefold, every run of characters that are not letters or digits, and `_`, becomes one space. Hyphens and apostrophes split tokens. `flaminica's` and `flaminica’s` are `flaminica` plus `s`, and that `s` counts. `cone-shaped` is two words. `in-laws` is `in` plus `laws`. S717's quote is 25 words only because `cone-shaped` splits. S701's is 25 only because `in-laws` splits. S706's is exactly 8. Counts were run this session against the file text.

The quote the counter and the locator both use is the first quoted span in the anchor cell only. The regex accepts straight double quotes or curly quotes. A quoted word in the locator steals the quote.

1. `id`. Rule: `S` plus digits, one row, never reused. This round only S718-S743 (mined) or S744-S749 (disposition). Good: `S718`. Bad: a second S718 prints `S718:rows=2`. A missing id, or a line that does not start at column 0 with a pipe, prints `S718:rows=0`.

2. `source`. Rule: citation, then ` - `, then one live http(s) URL, then ` ; capture `, then `https://web.archive.org/web/` plus exactly 14 digits plus `id_/` plus the original, and that archive URL ends the cell. The first URL in the cell is the live URL. The capture original must `norm_url`-match that first URL. Good: S694's source cell, quoted below. Bad: an archive URL with no `id_/`, or any text after the capture, prints `no_capture`. A DOI placed before the page URL prints `capture_original_mismatch`.

3. `kind`. Rule: one of `spec` `docs` `paper` `code` `tool` `dataset` `talk` `book` `community` `own-work`. The counter does not read this cell. The contract census awk does. Good: `docs` (S694, a library's own page). Bad: `article` still passes ROWS; the census prints `kind S718 article`.

4. `tier`. Rule: `A` or `B` for a mined row, scoped to this row's scope. See (b). `C` fails the counter. Good: `B`. Bad: `C` prints `S718:tier=C`. `b` prints `S718:tier=b`.

5. `scope`. Rule: the claim the tier applies to, not a global topic. The counter only checks that the cell is present. Good: `lexical definition of crown as sovereign headgear and its materials` (S698). Bad: `headgear` as the scope of an A row. No counter symptom; it is a criterion-6 miss. A pipe inside the scope prints `cells=12`.

6. `anchor`. Rule: a locator (section, heading, page, or sense; never a bare homepage) then colon and a verbatim quote in double quotes. Body text. 8-25 normalised words. Good: `did-you-know body text: "A typical Roman helmet was called a galea."` (S706, 8 words). Bad: `sense "galea": "A typical Roman helmet was called a galea."` takes `galea` as the quote and prints `quote_words=1`. Seven words prints `quote_words=7`. A quote that lives only in teaches prints `quote_words=0`.

7. `teaches`. Rule for a mined row: one learner benefit in the seat's words. Rule for a disposition row: the shape in (c), not a prose benefit. Good: `the museum calls a typical Roman helmet a galea` (S706). Bad: a disposition cell `rejected: 403; flip: a 200` prints `S744:teaches=rejected: 403; flip: a 200` (lowercase fails `startswith`).

8. `status`. Rule: mined rows are exactly `mined`. Disposition rows are exactly `rejected` or `queued`. Good: `mined`. Bad: `queued` on S718 prints `S718:status=queued`. `mined` on S744 prints `S744:shape_or_status`.

9. `opened`. Rule: mined rows are exactly `2026-10-23`. Not checked on S744-S749. Good: `2026-10-23`. Bad: `2026-10-22` prints `S718:opened=2026-10-22`.

10. `recheck`. Rule: mined rows are exactly `180d`. Contract v1 also allows `90d`, `on-release`, and an ISO date. This counter does not. Good: `180d`. Bad: `365d` prints `S718:recheck=365d`.

11. `used-by`. Rule: the cell must contain `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`. Extra comma-separated paths are fine. An em dash is not. Good: that path alone. Bad: the S694-S717 tail `corpus/knowledge/culture-material/headgear-head-covering-codes.md` prints `S718:usedby=corpus/knowledge/culture-material/headg` (first 40 characters).

`norm_url` (lines 115-132) is used only for the capture comparison. Scheme and host are lowercased, a leading `www.` is removed, port 80 or 443 is dropped, the query and the fragment are ignored, and a trailing slash is stripped except on `/`. `http` versus `https` does not match. A different path does not match.

## (b) Tier, three registry cases

Tier is scoped to the row's scope, never global (`CORPUS.md` lines 93-97; `SOURCES.md` lines 14-19; QUALITY criterion 6, line 29). A means primary or authoritative for that scope. B means strong secondary: an expert write-up, a survey, a textbook, an encyclopedia overview, a publisher abstract. C means a lead only, never sole support for an admitted claim. `community` is never A. A publisher description or abstract is B for any substantive claim about the work, even when the abstract is accurate. A wrong tier is corrected by a new row whose teaches opens `supersedes S0NN —`, never by editing the old tier cell.

1. A, because the source is the authority for the scope named. S698 (`corpus/SOURCES.md` line 653), kind `docs`, tier A, scope `lexical definition of crown as sovereign headgear and its materials`. The anchor is Collins's own British noun sense 1 on that page. The page is the definition, so A attaches to the scope, not to HarperCollins. Contrast S009 (line 39): kind `community`, tier C. Filing `community` with tier A passes ROWS, because `tier=A` is allowed, and fails only the census awk, which prints `tier-inflation`.

2. B, encyclopedia summary, scope kept narrow. S717 (line 672), kind `docs`, tier B, scope `the fez's brimless cylindrical form, red felt and tassel (bounded summary support)`. Britannica's quick summary is a secondary overview of the object, not a primary source for Ottoman or Maghrebi practice. S697 (line 652) is the same choice for the Phrygian cap's material and shape.

3. B by correction: a publisher abstract is not A. S034 (line 63) filed Kelly 2013, *The Lifeways of Hunter-Gatherers*, as tier A for `the book's stated programme (publisher abstract)`. S044 (line 73) is the same book and the same Crossref abstract, retiered B, status `queued`, and teaches opens `supersedes S034 — a publisher abstract is useful orientation, not primary authority for substantive claims about the book`. S045 and S046 do the same for S038 and S039. Criterion 6 forbids fixing S034's tier cell in place.

## (c) REJECTED shape

Contract (`CORPUS.md` lines 101-102), exact text:

`REJECTED: <reason>; flip: <what would change the verdict>`

The counter (`accept-c.py` lines 239-244) accepts a disposition row when all three hold:

- 11 cells, and status is `rejected` or `queued`. Otherwise the symptom is `S744:shape_or_status`, one string for both faults.
- teaches starts with `REJECTED:` or `QUEUED-CANDIDATE:` (case-sensitive; `cells()` has already stripped ends).
- the cell contains the substring `; flip:` — semicolon, space, the word flip, colon.

`QUEUED-CANDIDATE:` is not in contract v1. The counter comment (lines 224-231) uses it when a retest contradicted the rejection ground, with status `queued`. The code does not pair the prefix with the status: either prefix with either status passes. The code also does not check tier, quote, capture, opened, recheck, used-by, or a live URL on S744-S749. The docstring says "and a live URL". The code never looks. Put the URL in anyway (criteria 12 and 13). The counter will not notice if you leave it out.

Worked, from the registry (S028, line 57):

`REJECTED: login-gated third-party aggregation of the Berezkin-Duvakin catalogue, ATU and Thompson that expressly reserves all rights in text and data mining, scraping and AI use; flip: permissive bulk/licence terms plus primary-source provenance per record`

These fail, symptom `S744:teaches=` plus the first 40 characters:

- `REJECTED: reason;flip: x` (no space after the semicolon)
- `rejected: reason; flip: x` (lowercase)
- `REJECTED: reason flip: x` (no semicolon)
- `supersedes S034 — ...` on a disposition id

The comment's routing is not enforced. It names S744, S745, and S747 as still HTTP 403 (keep `rejected`) and S748 and S749 as re-opened 200 plus LOCATED (use `queued` and `QUEUED-CANDIDATE:`). S746 is not classified there.

QUALITY criterion 12: a reason that names a tool, a word count, a locator failure, an HTTP status, or any source property a tool can check must name the re-test tool and carry its verbatim output in the round-64 lesson Gate. The counter does not open the lesson.

## (d) Ten ways a row fails the counter

[INFERENCE] on the order only. Each token is one element of the `bad=[...]` list. At most eight ROWS tokens are printed (`row_bad[:8]`). Python's list repr uses single quotes. A cells fault skips the rest of that row.

1. Quote length, or the wrong span. Leg line: `ROWS FAIL bad=['S718:quote_words=1', ...] checked=26`. N is 0 when the anchor has no straight or curly quote. Causes: under 8 or over 25 after the split in (a); the locator's own quoted label is the first span; the quote was put in teaches. S706 is the floor (8). S717 and S701 are the ceiling (25), and both depend on a hyphen split. Counting English words instead of normalised tokens will file a 26.

2. used-by copied from the exemplar block. Symptom: `S718:usedby=corpus/knowledge/culture-material/headg`. Every S694-S717 row ends with the headgear entry. The cell must contain the linguistics path. The check is a substring, so a longer comma-separated list that includes the right path passes.

3. Capture shape. Symptom: `S718:no_capture`. The source cell must end with `web.archive.org/web/` plus exactly 14 digits plus `id_/` plus the original, optional trailing period or semicolon. Fails: a timestamp shorter than 14 digits, `/web/TIMESTAMP/` without `id_/`, a parenthetical after the capture, a space inside the archive URL. Confirmed against the regex this session.

4. Capture of a different URL than the first URL in the cell. Symptom: `S718:capture_original_mismatch`. The archive original is compared with `urls[0]`, not with whichever URL you think is canonical. A DOI before the page URL mismatches. `http` versus `https` mismatches. A leading `www.`, a trailing slash, and a query string do not mismatch, because `norm_url` drops them. Confirmed this session.

5. A pipe inside a cell. Symptom: `S718:cells=12` (or whatever `split` produced). Titles, quotes, and flip clauses are the usual source. Nothing else on that row is checked.

6. Live URL string reused. Leg line: `LINK FAIL bad=['S718:registry_hits=2']`. The counter counts registry lines that contain the raw live-URL string (`url in line`, not `norm_url`). The capture on the same line embeds that string and still counts as one line. A second row fails it. So does a longer URL of which this one is a prefix: `.../topic/fez` is inside `.../topic/fez-hat`. `www.` versus a bare host does not collide. Sibling symptom, same leg: `S718:url_in_entry` if the knowledge entry contains the live URL. Cite by S-id only.

7. Citing bullet out of quote order. Leg line: `RESTATE FAIL bad=['line12:S718:in_order=1', ...]`. The entry line must match `^\s*-\s+(.*?)\s*\(S718\)\s*$`: a dash bullet, the id in parentheses, end of line. A period after `(S718)` is `line12:shape`. Content words are normalised tokens of length at least 4, alphabetic, and not in the stop list: a an and are as at be been but by for from has have he her his i if in into is it its of on or she so that the their them they this to was we were with you your not no nor. At least 5 of them, or the symptom is `line12:S718:content=4`. At least 3 must occur in order in the quote's full token list. The clause "galea was the name of a typical roman helmet according to the museum label" against S706's quote scores `in_order=1`, because galea is the last quote token and the earlier words are then behind the cursor. Checked this session.

8. Paraphrase uses only the quote's words. Symptom: `line12:S718:no_novel_content_word`. The clause "typical roman helmet called galea" has 5 content words and 5 in-order hits, and still fails: every content word is already in the quote. The bullet needs one content word the quote does not contain, such as museum or states. Checked this session.

9. Verbatim run longer than 12. Symptom: `line12:S718:copy_run=13`. The run is consecutive normalised tokens of the bullet, stopwords included, found as a contiguous span of the quote. S701's 25-token quote pasted whole fails. A bullet may repeat a short span: a restatement of S706 that includes "a typical roman helmet was called a galea" has `copy_run=8` and passes. Checked this session.

10. LIVE subset not located. Leg line: `LIVE FAIL subset=['S718', 'S723', 'S728', 'S733', 'S738', 'S743'] bad=['S718:NOT_LOCATED ...']`. Only those six ids are fetched, from `(n - 717) % 5 == 1`. The counter runs `python3 -B reports/round-61/reopen-quote.py --row S###` up to 3 times, 20 seconds apart. The locator tries at most the first 4 URLs in the source cell, in order, so a live 403 still passes if the archive URL's body contains the quote. A miss looks like `NOT_LOCATED` plus the url and `quote-absent`, or `denied-host`, or `quote under 8 words`, or `HTTPError`. The 60-character cut is on the locator's first line, then the counter prefixes `S718:`. HTML alt, title, and aria-label text is invisible to the locator (it keeps text nodes outside script and style only), so an attribute-only quote is `quote-absent`. A figcaption text node does locate. Criterion 16 still forbids a caption quote, and this counter never prints `CAPTION_ONLY`.

### Same counter, not in the ten

- `S718:rows=0` or `S718:rows=2` — id missing, or the line is not at column 0; or the id is duplicated.
- `S718:tier=C` — tier is not exactly A or B.
- `S718:status=queued` — a mined row whose status is not exactly `mined`.
- `S718:opened=...` and `S718:recheck=...` — not `2026-10-23`, or not `180d`.
- `S718:no_live_url` — no http(s) URL in the source cell.
- `S718:example.com` — HOSTS. The host equals, or is a subdomain of, `example.com` `example.org` `example.net` `example.io` `example.edu` `httpbin.org` `httpbingo.org` `reqres.in` `postman-echo.com` `jsonplaceholder.typicode.com`.
- `extra_new_rows=[...]` — an id that is not in the base registry and not in S718-S749. The list is cut at six.
- `S744:shape_or_status` — a disposition row that is not 11 cells, or whose status is not `rejected` or `queued`.
- `S744:teaches=` plus 40 characters — prefix or `; flip:` missing. See (c).
- `line12:shape` — the citing line is not `- clause (S###)` at end of line.
- `line12:S718:content=N` — the citing clause has fewer than 5 content words.
- `lineN:ids=[...]` and `marks=['lineN']` — ONEID. Two S-ids on one entry line, or a parenthetical to-verify, unverified, todo, fixme, tbd, or draft on a line that cites.
- `missing_base_lines=N` — APPEND. Any base row line changed. The only tolerated edit is S687's status from `mined` to `queued`, and that is not a row seat's job. Do not touch S001-S717.
- `locator_sha=DIGEST!=PIN` — someone edited `reports/round-61/reopen-quote.py`. Not a row fault.

## What the counter does not check

- Kind, scope wording, and tier inflation (community filed as A, or a publisher abstract filed as A). A caption quote also passes LIVE when the caption is a text node.
- That every S718-S743 id is actually cited in the entry. RESTATE only inspects lines that do cite one.
- A live URL on S744-S749, and which of those six are `rejected` versus `queued`.
- QUALITY criterion 10. `tools/check-source-access.py` is a different tool. It flags a mined row whose source, anchor, or teaches matches its bypass regex, printing `ACCESS_FINDING status S718 mined`. Clean, tested against that regex this session: `challenge met, not passed`, and `HTTP 403 on the live page; archive capture used`. Flagged: `headless`, `paywall bypassed`, `solved a captcha`, `VPN`, `got past the paywall`, `passed the cloudflare challenge`.
- Third-party scans (a JSTOR cover, an unnamed university PDF). Criterion 10 makes that a review reject. The counter cannot see it. Accept a scan only when the host page states a licence, or the file is the publisher's, the author's institutional repository, or the digitising library's own scan.
- The lesson Gate (URL, access date, a quote of at most 25 words). Contract rule 1 and criterion 12 require it. `accept-c.py` does not open the lesson.

## (e) Pre-filing checklist

1. The id is in S718-S743 or S744-S749, the line starts at column 0 with a pipe, and the line has exactly 11 cells. No pipe anywhere inside a cell.
2. Mined row: status `mined`, opened `2026-10-23`, recheck `180d`, tier A or B, kind from the contract list, and used-by contains `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`. Not the headgear path.
3. The scope is the claim you are actually supporting. A publisher abstract or an encyclopedia overview is B, and the scope says so (S717, S044). `community` is never A.
4. The anchor locator names a body location. The first straight or curly quote in that cell opens the quote. Count with `norm_words`, not a word processor: 8-25, hyphens and apostrophes split, and the leftover `s` counts.
5. The source cell ends with ` - `, the live URL, ` ; capture `, then `https://web.archive.org/web/` plus 14 digits plus `id_/` plus that same page. No earlier URL, so no DOI in front. The scheme matches. Take the timestamp from `curl -s "https://archive.org/wayback/available?url=URL"`.
6. From the lane root, `python3 -B reports/round-61/reopen-quote.py URL "QUOTE"` prints `LOCATED` and the url. If the live page is a challenge or a 403, repeat against the `id_/` capture and write `challenge met, not passed`. Do not write a bypass verb. Do not run `tools/reopen-row.py` for this. The counter's LIVE leg uses the round-61 locator.
7. The entry bullet, when you hand the quote on, is a dash, the clause, then ` (S###)` with no trailing period. At least 5 content words, at least 3 of them in quote order, one content word the quote does not have, and no 13-token copied run.
8. The live URL string is new. It is not a prefix of another row's URL, and it is not present in the entry.
9. Disposition only: teaches is `REJECTED: reason; flip: what would change it` or `QUEUED-CANDIDATE: reason; flip: ...`, status is `rejected` or `queued`, and a tool-checkable reason has its verbatim re-test output reserved for the lesson Gate.
10. You did not edit any line S001-S717. The cells do not say headless, captcha, VPN, paywall bypass, or logged-in.

## Three verbatim exemplars (S694-S717)

S694, line 649. The shape to copy: citation, ` - `, URL, ` ; capture `, `id_/` URL, a straight-quoted anchor, 12 words. Do not copy the used-by path.

`| S694 | “Liberty’s Cap: The Origins of a Numismatic Symbol,” Princeton University Library, n.d. - https://static-prod.lib.princeton.edu/capping-liberty/case/6/index.html ; capture https://web.archive.org/web/20251206173833id_/https://static-prod.lib.princeton.edu/capping-liberty/case/6/index.html | docs | A | the pileus in the Roman manumission rite and its later liberty imagery | opening explanatory paragraph: "given a pileus to wear as a public sign of his freedom" | Princeton describes the pileus given at Roman enfranchisement as a public sign of freedom | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |`

S698, line 653. Tier A because the scope is the dictionary's own sense. 13 words.

`| S698 | Collins English Dictionary, HarperCollins, 2012 Digital Edition (served by Dictionary.com; British noun sense 1) - https://www.dictionary.com/browse/crown ; capture https://web.archive.org/web/20260412094355id_/https://www.dictionary.com/browse/crown | docs | A | lexical definition of crown as sovereign headgear and its materials | British noun sense 1: "an ornamental headdress denoting sovereignty, usually made of gold embedded with precious stones" | Collins defines a crown as sovereign ornamental headwear made of gold and precious stones | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |`

S706, line 661. The 8-word floor. Do not copy its used-by.

`| S706 | “Roman soldier’s helmet,” National Museum of Australia, modified 2025-09-25 - https://www.nma.gov.au/learn/diy/roman-soldier-helmet ; capture https://web.archive.org/web/20260218211148id_/https://www.nma.gov.au/learn/diy/roman-soldier-helmet | docs | A | the museum's identification of the Roman helmet as galea | did-you-know body text: "A typical Roman helmet was called a galea." | the museum calls a typical Roman helmet a galea | mined | 2026-10-23 | 180d | corpus/knowledge/culture-material/headgear-head-covering-codes.md |`

## Unknowns

- The counter comment names S744, S745, and S747 as still-403, and S748 and S749 as re-opened. It does not classify S746, and the code enforces none of the six.
- Whether the integrator requires every mined id to appear in the entry. `accept-c.py` does not.
- No install. This seat edited nothing in the lane except the report path the item named.
