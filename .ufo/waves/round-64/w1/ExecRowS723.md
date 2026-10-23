# ExecRowS723 — row S723 (claim C, mined row)

Axes named: **coverage (C)**, **operability (O)**, **calibration (Ca)**. This seat executed only the assigned row contribution for S723 (overextension and underextension in early word meaning, entry section ## 3). No counter edited, no entry integrated, no registry mutated, no sibling row touched, no commit, no jj/git index mutation.

## Verdict

S723 row is **written and self-checked**: `.ufo/waves/round-64/rows/ScribeRowS723/row.txt` (1660 bytes, 5 lines, LF only) — the directory that the inherited attempt-1 left MISSING. `python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows` prints `S723 OK`. The whole check is now `31/32 clean` (only S740 remains MISSING; it is another seat's assignment, not this one).

The prior seat's source and quote were re-verified from scratch rather than trusted; every one of the four steps in the assignment was executed and observed.

## Steps executed (commands and outputs)

### (1) Live URL, plain curl

```sh
curl -sS -D /tmp/helm_headers.txt -o /dev/null -L "https://www.nottingham.ac.uk/helm/dev-test/ncc_work_in_progress/language_0-5/page_eleven.html"
```

```text
HTTP/2 200
date: Sat, 24 Oct 2026 01:57:30 GMT
last-modified: Mon, 25 Jul 2016 17:15:42 GMT
etag: "2547-53878ef164b80"
accept-ranges: bytes
content-length: 9543
content-type: text/html; charset=UTF-8
x-origin-server: rp_www_web_nottingham_ac_uk_www_nottingham_ac_uk_80
x-geoip-country-code: BR
```

HTTP 200 on the live URL. The host clock is UTC-3 (`date -u` → `Sat 24 Oct 2026 02:01:57 AM UTC`, local `Fri 23 Oct 2026 11:01:57 PM -03`), so the local calendar date is still 2026-10-23 — the date recorded in the row's `opened` cell and in the `ACCESS` line.

### (2) Quote is body text, 8–25 words

Body text was extracted from the fetched HTML (script/style stripped, tags removed, entities unescaped, whitespace collapsed). The quote appears in the "Early language acquisition" section, in the run of prose around the "Errors in early word use" paragraph:

```text
... Errors in early word use can help to explain the learning process. 2 errors are overextension and underextension. In overextension, children use a simple word to refer to many different things. For example, an 18 month old may use a word 'doggy' for all animals with 4 legs, or 'daddy' for all adult males. As children's vocabulary increases, their use of overextension decreases. In underextension, which is less common, children use a single word in a very restrictive way. ...
```

Programmatic containment check (same normalisation as the lane locator) printed `QUOTE_PRESENT: True`. Word count under the lane's `norm_words` is **13**, inside the frozen 8–25 band. Note: the assignment described the quote as "11 words"; the locale's tokenizer counts 13 (`in overextension children use a simple word to refer to many different things`). This is a counting difference in the brief, not a defect in the quote — the frozen band is 8–25 words and 13 satisfies it. The quote string itself is verbatim from the page.

### (3) Locator run from the lane root

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B reports/round-61/reopen-quote.py 'https://www.nottingham.ac.uk/helm/dev-test/ncc_work_in_progress/language_0-5/page_eleven.html' 'In overextension, children use a simple word to refer to many different things.'
```

```text
LOCATED https://www.nottingham.ac.uk/helm/dev-test/ncc_work_in_progress/language_0-5/page_eleven.html
EXIT=0
```

### (4) Row file written

`.ufo/waves/round-64/rows/ScribeRowS723/row.txt`, with exactly the labelled lines `ROW` / `BULLET` / `VERIFY` / `CAPTURE` / `ACCESS` (model: `ScribeRowS718/row.txt`).

The `ROW` line is one pipe table row with **11 cells**:

| cell | value |
|---|---|
| 1 | `S723` |
| 2 | source: University of Nottingham, School of Health Sciences, HELM RLO "Language from birth to 5 years old" (Early language acquisition module), n.d. — live URL `; capture` archived URL |
| 3 | `docs` |
| 4 | `B` (tier B, university teaching page) |
| 5 | scope: overextension and underextension as early word-meaning errors in children aged 0-5 |
| 6 | anchor: Early language acquisition section, paragraph on errors in early word use, with the quoted sentence |
| 7 | teaches: children of this age apply one simple word to many different referents, or hold one word to a single referent; both errors recede as vocabulary grows, so early word breadth is a design variable, not a fixed stage |
| 8 | `mined` |
| 9 | `2026-10-23` |
| 10 | `180d` |
| 11 | `corpus/knowledge/linguistics/language-socialization-and-acquisition.md` |

Capture cell carries `timestamp=20260324122540` and the original URL; the archived capture was fetched and confirmed to carry the quoted sentence (`WAYBACK_QUOTE_PRESENT: True`).

`kind` cell value `docs` follows the lane's existing registry vocabulary (`docs` 284, `paper` 202, `book` 108, `dataset` 25, `community` 16, `spec` 6, `tool` 2 measured over `corpus/SOURCES.md`); the source is a teaching module page, so `docs` is the closest existing kind and no new kind was invented.

### (5) Self-check

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows
```

```text
S723 OK
CHECK-ROWS: 31/32 clean
```

(The 32nd is S740, whose directory `ScribeRowS740` is absent — another seat's assignment.)

## Live-URL uniqueness (grep)

```sh
grep -rnE 'nottingham|page_eleven|language_0-5' .ufo/waves/round-64/rows   → No matches found (before write)
grep -nE 'language_0-5|page_eleven|helm/dev-test' corpus/SOURCES.md        → No matches found
```

Independent count over the registry at base: `sum(1 for l in corpus/SOURCES.md.splitlines() if live_url in l)` → **0**. The only other Nottingham URLs in the registry are the unrelated Institute for Name-Studies place-name rows (S514, S515) and a repository thesis (S517); none of them is this page. The live URL therefore appears in exactly one registry row after integration, which is what `accept-c.py`'s `LINK` leg counts.

## Cross-checks against the frozen counters (read-only)

The assignment's format rules were re-derived from the frozen instruments, not from the brief, and the row was validated against both implementations independently.

- `check-rows.py` — `S723 OK` (cells, tier, status, opened, recheck, used-by, quote band, live URL present, capture present and matching, bullet shape, content words, in-order quote words, novel content word, copy run, `VERIFY` starts with `LOCATED`).
- `reports/round-64/accept-c.py` — its `ROWS`/`RESTATE` logic was replicated against the row. Quote band 13 words (8–25 ✓). Bullet: 20 clause words, 14 content words (≥5 ✓), 5 quote words matched in quote order (≥3 ✓), novel content words present (`overextension` aside, the set difference is non-empty ✓), longest verbatim copy run from the quote = 3 (≤12 ✓).
- `reports/round-61/reopen-quote.py` — the `LIVE` leg resolves the row through `row_target` on the pipe-split `ROW` line. Simulated directly against the written row:

```text
URLS: ['https://www.nottingham.ac.uk/helm/dev-test/ncc_work_in_progress/language_0-5/page_eleven.html',
       'https://web.archive.org/web/20260324122540id_/https://www.nottingham.ac.uk/helm/dev-test/ncc_work_in_progress/language_0-5/page_eleven.html']
QUOTE: 'In overextension, children use a simple word to refer to many different things.'
LIVE-LEG RESULT: LOCATED https://www.nottingham.ac.uk/helm/dev-test/ncc_work_in_progress/language_0-5/page_eleven.html
```

  The live URL is tried first and wins; the archived capture is the second URL in the same source cell and also carries the quote.
- `.ufo/waves/round-64/integrate-w2.py` — `parse_contribution(path, "S723", rejected=False)` accepted the file: 11 cells, status `mined`, `used-by` exactly `corpus/knowledge/linguistics/language-socialization-and-acquisition.md`, bullet one line ending with exactly `(S723)`, and the required field set `ROW/BULLET/VERIFY/CAPTURE/ACCESS` all present. `BULLET_MAP[3]` maps section 3 to `("S720", "S721", "S722", "S723")`, so this row lands in entry section ## 3 as the assignment states.

## Named defects

1. **Inherited MISSING, now closed for this seat.** `ScribeRowS723/` did not exist at wave start; the inherited checker reported `MISSING mined ['ScribeRowS723', 'ScribeRowS740']`. This seat created and validated `ScribeRowS723`. `ScribeRowS740` is still missing and remains open on its own seat.
2. **Brief's word count differs from the lane's tokenizer.** The assignment calls the quote "11 words"; `norm_words` yields 13. The frozen band (8–25) is satisfied either way, so no counter leg is affected and no revision is proposed. Recorded because the brief's number could be misread as a frozen bound.
3. **Frozen counter stamp inconsistency (observed, not touched).** `reports/round-64/accept-c.py:2` still says "revision 0" while inline comments say revision 1 (`:224`), revision 3 (`:395`), revision 4 (`:405`). The frozen predicate in `claims.json` names no revision number, so this is a docstring-stamp defect only. Recorded, not edited, per the no-counter-edit rule. Proposed pre-data revision with forcing control, for the L1 to schedule: make the docstring stamp equal the highest inline `revision N`, with the current file pinned as the must-fail specimen (a synthetic file whose docstring reads "revision 0" while its body carries "revision 4" must FAIL). Not run here.
4. **No defect found in the S723 source choice.** The prior seat's selection (HELM `Early language acquisition`, tier B) survived re-verification: live 200, quote in body text, locator LOCATED, archived capture present and quote-bearing, URL unique in the registry.

## Affected axes

- **Coverage (C) — improved, none harmed.** One of the 26 claimed mined rows now exists in the exact form `check-rows.py` and `accept-c.py` demand, and it is one of the six ids in the `LIVE` frozen subset (`accept-c.py:45`), so its locator leg was exercised against the pinned `reports/round-61/reopen-quote.py` bytes, not merely asserted.
- **Operability (O) — not harmed.** `tools/reopen-row.py` and `accept-o.py` bytes were not read, edited, or invoked; the O axis is untouched by this seat.
- **Calibration (Ca) — not harmed.** No bookkeeping file was touched (`LOG.md`, `SCORECARD.md`, `corpus/LOG.md`, `reports/round-63/telemetry/revisions.txt` were left exactly as the working tree had them). The row records only what the cited page says, at the page's tier-B scope, with no claim beyond it.

## Risks and blockers

- **Not verified here:** the whole-predicate `ACCEPT-C-64` run. `accept-c.py` needs the assembled entry, the appended registry rows and the README index row; none of that exists yet (the inherited dry-run receipt `reports/round-64/telemetry/dry-run-c.txt` begins `FILE FAIL` / `ROWS FAIL`). An unrun check has not passed. The L1 must run `python3 -B reports/round-64/accept-c.py` after integration.
- **No integration performed.** `corpus/SOURCES.md`, `corpus/knowledge/linguistics/language-socialization-and-acquisition.md` and `corpus/README.md` are untouched by this seat, as assigned. `NOHARM` (the knowledge diff must list only the new entry) is therefore unaffected by me.
- **`ScribeRowS740` still missing.** It will keep `check-rows.py` and, once integrated, `accept-c.py`'s `ROWS` leg red until its seat lands. Named for the L1.
- **Tier-B sourcing.** The row supports a *scope-limited* claim (a teaching module's description of overextension/underextension in children aged 0–5). The bullet deliberately states the pattern as a design variable rather than a developmental law, and the `teaches` cell says so, to keep the tier-B evidence from being read as a universal sequence. A reviewer judging support must hold the claim to that scope.
- **Host clock.** The row's `opened` date 2026-10-23 is the local (UTC-3) calendar date; the live server's `date` header reads 2026-10-24T01:57:30Z. If the L1's canonical date convention is UTC, this cell would read 2026-10-24 and fail the frozen `opened=2026-10-23` check — but every sibling row in this wave also records 2026-10-23, so the wave convention is local date. Flagged, not changed.
- **`SOURCES.md` append-only discipline.** The row's registry line carries a `capture` URL inside the source cell (matching the S718–S722 model). `accept-c.py`'s `LINK` leg counts registry lines containing the *live* URL: because the capture URL embeds the live URL as a substring, the count is by line, not by substring, so one row yields exactly one hit. No duplicate-URL hazard was observed.

## Files changed

- `.ufo/waves/round-64/rows/ScribeRowS723/row.txt` (created — the assigned deliverable)
- `.ufo/waves/round-64/w1/ExecRowS723.md` (this report)

No other file was written, edited, moved or deleted. No tool was installed or updated (no pacman, no uv/npx, no binary fetch) — the task needed only `curl` and the lane's own Python.

Report: .ufo/waves/round-64/w1/ExecRowS723.md
