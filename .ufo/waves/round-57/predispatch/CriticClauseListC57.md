# Round 57 pre-dispatch critic — claim C (CriticClauseListC57)

Measured revision: lane `main` declaration commit `51726fa6e0fc6ee028b54c74509a8fec1bc06186` (claim base `6f08c494`; `git diff --stat 6f08c494 51726fa6 -- reports/round-57/{accept-c,reopen-quote,controls-c}.py` is empty, so the instrument bytes are the claim base's). sha256 of the measured files:

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/accept-c.py` `fd378e1b9eb38a95d1eb8cec70a16008e26733aaa59501c96a6f6a2858db3631`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/reopen-quote.py` `29ffa41772fdd1a137643c2e60ea6bede13fbc47f93b3265c47ca053d6500714`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/controls-c.py` `0a468dcb95de9755976ff77e3647e66011aa25b9317fd075db43242cc56f058c`

Scratch: `/fast/scratch/hyaku/kotodama-r57/CriticClauseListC57/` (`cheats.py`, `legcontrols.py`, clones under `clones/`, outputs `echo.txt`, `short.txt`, `legs.txt`). No lane file other than this report was written. Installs: none.

## Verdict

**BLOCKING.** The LOCATE leg is the only leg that separates real sourcing from the round-56-style stub, and it can be met with no sourcing. On the frozen `accept-c.py`, three fixtures with no real sourcing print `ACCEPT-C-57: PASS` and exit 0: the controls-c stub with an invented quote behind an archive.org search URL that echoes it, and the same stub with the anchor quote `"a"` or `"of the"`. Criterion 11 / addendum §9 is therefore not met: the cheapest shortcut reaches the target. The inherited legs are correct for S413–S480 and the total of 233; each one fails under its own mutation at this revision.

## (1) Clause list against the statement and predicate words

| clause | words found in statement/predicate | leg | red control at this revision (cite) | verdict |
|---|---|---|---|---|
| C-count | statement "232 to 233", "no file is removed", plus the entry path | SET, SWEEP | `controls-c.txt` lines 3–4 (`SET FAIL count=232`, `SWEEP FAIL ... rows 232 files 232`) | ok for the count. The clause words drop the path ("..."), and no control adds a 233rd file at another path; see `set-extra-file` below |
| C-floor | predicate "at least 20 distinct cited S-ids" | FLOOR | `controls-c.txt` line 5 (`FLOOR FAIL cited=0`) | ok. 19 is first tested here (`floor-19`) |
| C-range | predicate RANGE | RANGE | **none at this revision**: the clause cites the round-56 receipt, which ran on other bytes (bounds 359/418). The new constants 413/480 have no receipt | gap (minor). Supplied below: low, high, duplicate and notation each fail |
| C-status | "mined" | STATUS | none at this revision (round-56 receipt) | gap (minor). Supplied below |
| C-usedby | predicate USEDBY | USEDBY | none at this revision (round-56 receipt) | gap (minor). Supplied below |
| C-access | "tools/check-source-access.py exits 0" | ACCESS | none at this revision (round-56 receipt) | gap (minor). Supplied below |
| C-locate | "for at least ceil(0.8 x cited) cited rows the quote is located live in the source" | LOCATE | `controls-c.txt` lines 20, 30 (`LOCATE FAIL located=0 cited=20 need=16`) | **fails criterion 11**: the leg *can* fail, but its red controls only test invented quotes on dead or unrelated URLs. The words "located live in the source" overclaim: the leg shows only that the response body of some URL in the source cell contains the quote's word sequence. That URL may be an echo, a search page, or the lane's own published files, and the quote may be one word long. The predicate's "at least one id cited" and the code's "at most four URLs" are not in the clause words or the predicate |

The predicate, the code and the receipt agree on the label `ACCEPT-C-57: PASS|FAIL` and on the eight legs (`accept-c.py` lines 143–147; receipt lines 11, 21, 31).

### Per-leg red controls I ran at 51726fa6 (inherited legs, isolated)

Command: `cd /fast/scratch/hyaku/kotodama-r57/CriticClauseListC57 && python3 -B legcontrols.py` (exit 0). Each fixture starts from the controls-c stub with 20 rows on real Wikipedia URLs and anchor quote `"a"`. That stub passes every leg on its own, so each mutation isolates one leg. Each fixture's `accept-c.py` was run in its own clone.

```
## pass-base       exit 0 failed_legs []          ACCEPT-C-57: PASS
## set-extra-file  exit 1 failed_legs ['SET']     SET FAIL count=234 required=233 added=[...heraldry-emblems-identity-marks.md', '...myth-symbol/notes.txt'] removed=[]
## floor-19        exit 1 failed_legs ['FLOOR']   FLOOR FAIL cited=19 floor=20
## range-low-S412  exit 1 failed_legs ['RANGE']   RANGE FAIL bad=['S412'] range_notation=[]
## range-high-S481 exit 1 failed_legs ['RANGE']   RANGE FAIL bad=['S481'] range_notation=[]
## range-dup-S414  exit 1 failed_legs ['RANGE']   RANGE FAIL bad=['S414'] range_notation=[]
## range-notation  exit 1 failed_legs ['RANGE']   RANGE FAIL bad=[] range_notation=['S413–S415']
## status-S415     exit 1 failed_legs ['STATUS']  STATUS FAIL bad=['S415:candidate']
## usedby-S416     exit 1 failed_legs ['USEDBY']  USEDBY FAIL bad=['S416']
## access-S417     exit 1 failed_legs ['ACCESS']  ACCESS FAIL exit=1 ACCESS: 3 flagged rows, 2 findings
```

`pass-base` is itself a sixth no-work pass (quote `"a"`).

## (2) Shortcut hunt

### 2a. The locator alone: `python3 -B reports/round-57/reopen-quote.py URL QUOTE`

Q = `the banner of the ninth river house shows a silver heron on a field of 7 stars`. This is controls-c's invented text, so it is on no real page. QE is Q percent-encoded. Run from `/home/vgpnk/Projects/shokunin/kotodama-shokunin`:

| URL | QUOTE | output | exit |
|---|---|---|---|
| `https://en.wikipedia.org/wiki/Heraldry` | `the` | LOCATED | 0 |
| `https://en.wikipedia.org/wiki/Heraldry` | `of the` | LOCATED | 0 |
| `https://www.metmuseum.org/art/collection/search/318324` (a round-56 URL) | `of the` | LOCATED | 0 |
| `https://archive.org/advancedsearch.php?q=QE&fl%5B%5D=identifier&rows=1&output=json` | Q (invented) | LOCATED | 0 |
| `https://api.crossref.org/works?query=QE&rows=0` | Q | LOCATED | 0 |
| `https://en.wikipedia.org/w/index.php?search=QE&fulltext=1&ns0=1` | Q | LOCATED | 0 |
| `https://www.bing.com/search?q=QE` | Q | LOCATED | 0 |
| `https://httpbin.org/anything?q=QE` | Q | LOCATED | 0 |
| `https://httpbin.org/anything?a=the%20banner%20of&b=the%20ninth...stars` (quote split over two parameters) | Q | LOCATED | 0 |
| `https://httpbin.org/base64/<base64 of Q>` (quote not readable in the URL) | Q | LOCATED | 0 |
| `https://postman-echo.com/get?q=QE` | Q | LOCATED | 0 |
| `https://html.duckduckgo.com/html/?q=QE` | Q | NOT_LOCATED quote-absent | 1 |
| `https://raw.githubusercontent.com/VeigaPunk/kotodama-shokunin/main/corpus/SOURCES.md` (the lane's own public remote) | `Dom Miguel de Castro, Ambassadør for herren af Sonho` (S386's anchor) | LOCATED | 0 |
| same raw URL | Q (not yet in that file) | NOT_LOCATED quote-absent | 1 |
| `https://github.com/VeigaPunk/kotodama-shokunin/blob/main/corpus/SOURCES.md` | S386 anchor | NOT_LOCATED quote-absent | 1 |

The self-hosted route works because the lane remote (`origin https://github.com/VeigaPunk/kotodama-shokunin.git`) is public. Once a row lands and is pushed, a row whose source is the lane's raw `SOURCES.md`, or the entry file itself, locates its own invented anchor.

### 2b. Full shortcut fixtures scored by the frozen instrument

These use the controls-c stub verbatim: the entry with a `- topic:` line and 20 cited ids S413–S432, the README row, section count, totals and footer moved, and 20 mined rows used-by the entry. Only the anchor quote and URL change. Command: `cd /fast/scratch/hyaku/kotodama-r57/CriticClauseListC57 && python3 -B cheats.py ...`, which runs `python3 -B reports/round-57/accept-c.py` in each clone (checked out at `51726fa6e0fc6ee028b54c74509a8fec1bc06186`).

```
## fixture echo-archive  (20 invented quotes; source = archive.org advancedsearch?q=<quote>&output=json)  exit 0
   SET PASS count=233 ... SWEEP PASS ... FLOOR PASS cited=20 ... RANGE/STATUS/USEDBY PASS
   ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
   LOCATE PASS located=20 cited=20 need=16 at=2026-10-22T23:11Z not_located=[]
   ACCEPT-C-57: PASS
## fixture shortquote-a  (round-56 URLs S359-S378, anchor "a")  exit 0
   LOCATE PASS located=20 cited=20 need=16 at=2026-10-22T23:12Z not_located=[]
   ACCEPT-C-57: PASS
## fixture shortquote-ofthe  (round-56 URLs S359-S378, anchor "of the")  exit 0
   LOCATE PASS located=16 cited=20 need=16 at=2026-10-22T23:12Z not_located=[S413 ..., S421 ..., S426 ..., S428 ...]
   ACCEPT-C-57: PASS
## fixture echo-crossref  (as echo-archive via api.crossref.org)  exit 1
   LOCATE FAIL located=9 cited=20 need=16 ... 11 rows HTTPError (Crossref rate-limited the 8 parallel fetches)
   ACCEPT-C-57: FAIL
```

Crossref failed only because of rate limiting; on its own the URL is LOCATED (table 2a). The archive.org echo is the most damaging case: the host is the same one round-56 rows legitimately cite (S359, S361, S371, S404), so it does not stand out in review.

## (3) Findings

### F1 — BLOCKING: LOCATE passes on one- and two-word quotes from any page

Evidence: `shortquote-a` and `pass-base` locate 20 of 20, `shortquote-ofthe` 16 of 20; all three print ACCEPT-C-57: PASS with exit 0. Across 20 English Wikipedia heraldry articles, the share of pages each phrase locates on is: `of the` 20/20, `one of the` 11/20, `as well as the` 5/20, and for five-word phrases `at the end of the` 0/20, `in the form of a` 3/20, `is one of the most` 0/20, `in the middle of the` 2/20. Below five words a phrase is found on many arbitrary pages; at five words it no longer reaches 16 of 20.

Fix: in `reopen-quote.py` `locate`, return `(False, "short-quote")` when `len(normalise(quote).split()) < 5`. State the rule in the docstring and in the C-locate clause words.

Cost to honest round-56 rows: of the 43 located in the calibration, this drops S360 (3 words), S365, S369 and S372 (2 words each); S379 (1 word) was already not located. That leaves 39/54 = 0.722. Five words is the cheapest bar: four words drops the same rows, and six also drops S376. New rows are written to the rule, so this does not block honest round-57 work. Re-run the calibration with the fixed locator and disclose 39/54.

### F2 — BLOCKING: echo, search and transform endpoints locate invented quotes

Evidence: the `echo-archive` fixture passes with exit 0. Table 2a shows archive.org advanced search, Crossref, Wikipedia search, Bing, httpbin (query, split parameters, base64) and postman-echo all locate Q.

Smallest fix, in three parts:

1. **Reflection guard.** For each URL, return not located (`reflected`) when every word of `normalise(quote)` occurs among the words of `normalise(urllib.parse.unquote_plus(url))`. Across all quoted rows in `corpus/SOURCES.md` this fires only on S160, whose 3-word quote "The Banda-Linda" F1 already rejects. It never fires on S386, whose search-API URL carries "Miguel de Castro" but whose quote also has "Dom", "Ambassadør", "herren", "Sonho". It catches the archive.org, Crossref, Wikipedia-search, Bing, httpbin query and split-parameter cases.
2. **Host deny-list.** The guard cannot catch encoded echoes (`httpbin.org/base64/…` gives `reflection guard would fire: False` and still LOCATED). Deny `httpbin.org`, `postman-echo.com`, and the lane owner's own publication hosts (`github.com/VeigaPunk/`, `raw.githubusercontent.com/VeigaPunk/`, `veigapunk.github.io`, `gist.github.com`, `gist.githubusercontent.com`). None of the 54 round-56 calibration URLs is on this list.
3. **Review-only clause.** A host list is not a closure, so add to `review_only`: "each located URL is an independent publication, not an author-controlled page and not an echo, search or transform endpoint that rebuilds the quote from the URL".

### F3 — BLOCKING, procedural: controls-c lacks the shortcut red controls

Under criterion 11 / §9, the controls must include the cheapest shortcut, and only the two invented-quote-on-dead-or-unrelated-URL stubs exist.

Fix: add `stub-shortquote` (anchor `"a"` on the S359–S378 URLs), `stub-echo` (archive.org advanced-search URL plus invented quote) and `stub-selfhost` (lane raw `SOURCES.md`) to `/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-57/controls-c.py`, each expecting `LOCATE` only. Re-commit `telemetry/controls-c.txt` after the F1 and F2 fixes; all three print PASS today. Add the per-leg controls from §1 (low, high, duplicate, notation, status, used-by, access, floor-19, extra file) so that C-range, C-status, C-usedby and C-access carry a receipt at this revision instead of round 56's.

### F4 — minor (risk to honest work): LOCATE results are non-deterministic, and Wayback dominates the flips

Evidence: a sequential retry of the four calibration HTTPError rows gave S408 and S409 located, S400 `HTTPError 429`, and S391 loaded but quote-absent. A full re-run of the 54 calibration rows with the leg's own `ThreadPoolExecutor(8)` located 43 of 54 in 32 s, but 6 rows changed result: S365, S383 and S384 lost; S400, S408 and S409 gained. That is about 11% per row in ten minutes. At p ≈ 0.1 per row, an honest pre-checked 20-citation entry has about a 4% chance of falling below 16 on any single re-run, and the falsifier counts a live re-run.

Fix: in `fetch`, honour `Retry-After` and retry 429/5xx up to three times (8, 30 and 60 s). Fetch at most one request at a time per host for `web.archive.org`. Declare that a verifier who sees a LOCATE miss re-runs once before falsifying.

### F5 — minor (honest false negative): `row_target` strips a closing `)` that belongs to the URL

`row_target` applies `.rstrip(").,;:'")`, so `…/wiki/Tincture_(heraldry)` becomes `…/Tincture_(heraldry` and returns HTTP 404. URL mode (the scouts' pre-check) reports `LOCATED https://en.wikipedia.org/wiki/Tincture_(heraldry)` with exit 0, while row mode (the leg) gives `(['https://en.wikipedia.org/wiki/Tincture_(heraldry'], 'tincture')`. The two modes disagree on the same source, and Wikipedia and Wayback URLs often end in `)`.

Fix: strip a trailing `)` only when the URL has more `)` than `(`.

### F6 — minor: the 0.8 share is honest only for pre-checked rows; say so

The calibration gives 43/54 = 0.796. Under its own rule that is a FAIL on honest round-56 data (ceil(0.8 × 54) = 44). Under F1 it becomes 39/54 = 0.722. So the share is not free: a seat that does not pre-check fails. A seat that runs each row through the locator (row mode, after F5) and replaces misses clears it with four misses of slack at 20 citations, subject to F4.

Fix: state in the claim that seats MUST pre-check every row in row mode and SHOULD cite at least 22 so that flake does not decide the claim. The share itself is not inflated and need not change.

### F7 — minor wording

- The C-count clause words should name the path, since SET checks `added == [ENTRY]`.
- C-locate should say "located in the response body of a URL in the row's source cell (at most four), quote of at least five words" rather than "located live in the source".
- The predicate's LOCATE text omits "at most four URLs".
- ACCESS reads the whole registry, so a defect in a round-57 records row (S481–S499) fails C's ACCESS. Disclose this coupling between claim C and the records rows in `two_claim_note` or the separability note.

### Question (b): inherited legs for S413–S480 and a total of 233

They are correct:

- `base-knowledge-files.txt` equals `git ls-tree -r --name-only 6f08c494 corpus/knowledge` as sets (`True 232`).
- The surface grep returns 0 at base.
- The highest existing row is S412, so S413–S480 are free. S413–S418 overlap round 56's closed reserved block S359–S418 but carry no rows.
- The column indices match the header `id|source|kind|tier|scope|anchor|teaches|status|opened|recheck|used-by` (source = cell 2, anchor = 6, status = 8, used-by = 11).
- Each leg fails in isolation (§1). Only the receipts are missing (F3).

## Smallest safe correction (summary)

1. Apply the `reopen-quote.py` changes: five-word minimum (F1), reflection guard and deny-list (F2), balanced-parenthesis strip (F5), retry and per-host serialisation (F4).
2. Add the shortcut and per-leg controls to `controls-c.py` and re-commit the controls and calibration receipts (F3, F1).
3. Add the review-only independence clause and the clause-wording fixes (F2, F7).
4. Re-declare from the new instrument revision before any seat builds.
