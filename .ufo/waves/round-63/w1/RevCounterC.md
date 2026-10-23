# RevCounterC — frozen ACCEPT-C-63 counter review

Reviewed the pinned `80d53ffde7788299b69dbb0bd0436b2b7ddddb95` clone, not a later mutable lane copy. Frozen `accept-o.py` and `accept-c.py` hashes match the assignment (`a751efecccf623fcd4d2f348994933e34da892cf08132fa55b77f28c5fd8a5de` and `3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca`). Read both frozen counter docstrings, `claims.json`, and round-62 spotcheck §5. No tools installed. `read xd://lsp` reported no such device (only `ast_edit`/`debug` are mounted), so there was no LSP server for references/definition/diagnostics; findings below use pinned source and targeted scratch probes, not grep-as-semantic-proof.

## Findings

### HIGH — ROWS can accept fictitious captures; LIVE does not require archive evidence for every row

`accept-c.py:69,177-186` only regex-matches a Wayback-looking string and compares its embedded original URL after stripping `. , ; ) '`. The `[a-z]+` timestamp alternative accepts `fakeid_`; it does not establish that the capture exists or that its page contains the quote. The `rstrip` also equates distinct URLs: `https://example.com/path.` and `https://example.com/path` both become the latter, although a terminal dot can be part of the URL. The direct helper probe returned `rstrip mismatch=True` for that pair.

The only locator leg is `LIVE_IDS` (six rows, `accept-c.py:65,299-314`). The frozen locator tries URLs in order and returns at the first located URL (`reopen-quote.py:195-212`), so a successful live URL prevents the listed archive URL from being fetched. Thus the rows outside the six are never opened, and even the six can pass on live-only evidence. This is a concrete false PASS against the row rule requiring each quote on both the live page and its same-page capture.

**PROBE evidence:** in a separate scratch clone, I supplied 24 unique `example.com/?id=S694`…`S717` live URLs; all quote the generic Example Domain body text, `"This domain is for use in documentation examples without needing permission."`, and all rows use `web.archive.org/web/fakeid_/` plus the matching original URL. The entry clauses claim unsupported headgear facts. The base locator located the live quote for all six frozen rows; it never needed the archive. The unchanged frozen counter returned `ACCEPT-C-63: PASS` (full run below). The archive paths remain unverified; the result shows the counter accepts their syntax alone.

Smallest change that rejects this fixture’s alphabetic timestamp is `([0m\d+|[a-z]+)` → `(\d+)` in `CAPTURE_RE` (preserving numeric partial timestamps such as `2024id_`); that alone is not sufficient provenance validation. To meet the row rule, verify the exact original URL without punctuation stripping and independently locate each quote on both live and capture URLs for all 24 rows.

### HIGH — LIVE executes an unpinned locator from the measured root

`LOCATOR` is a relative path (`accept-c.py:61`) and `LIVE` executes `[sys.executable, LOCATOR, "--row", sid]` with `cwd=root` (`:306-307`). It neither verifies a frozen locator hash nor reads the locator from `BASE`. `NOHARM` only compares `corpus/knowledge` (`:274-279`), so replacing `reports/round-61/reopen-quote.py` is invisible to that leg. `LIVE` accepts any first stdout line beginning `LOCATED` (`:308-311`).

**PROBE evidence:** in the scratch fixture I replaced only its locator path with a stub that prints `LOCATED PROBE_NO_FETCH` for `--row`. The frozen counter still returned `ACCEPT-C-63: PASS`; no URL was reopened by that stub. Pin/verify the base locator bytes or execute a copy obtained from the frozen base commit, and require the expected locator result format.

### MEDIUM — RESTATE admits ordered token coincidences, not source support

`accept-c.py:208-250` counts any three `content_words` found in quote order; it does not require them to support the rest of the clause. The fixture clause `Domain documentation examples thereby rank ceremonial helmets as hereditary investiture` has nine content words, with only `domain`, `documentation`, `examples` matching the quote in order; its longest contiguous copied run is two words. The clause is unsupported by Example Domain, yet the frozen run reports `RESTATE PASS` for all 24 lines.

This matches the counter’s literal three-word predicate, and the docstring explicitly reserves SUPPORT judgment for blind review (`:47-49`); it is therefore a disclosed limit, not a mismatch in the frozen lexical implementation. It does mean `ACCEPT-C-63: PASS` alone cannot certify sourced coverage: the independent per-row support review must remain an actual admission gate.

### LOW — raw pipe splitting rejects valid escaped text and accepts extra columns

`cells()` uses `line.split("|")` (`accept-c.py:91-92`), while ROWS rejects only fewer than 11 cells (`:156-159`). A pipe inside a quoted body-text span (even Markdown-escaped as `\|`) is split as a delimiter; the targeted helper probe yielded `12` cells and `anchor_quote=None`, so a valid quoted row fails. Conversely, a row with 12 or more cells is accepted if the first 11 look valid, although the specified registry shape has exactly 11 columns. Use a pipe-escape-aware splitter and require exactly 11 cells.

## Explicit checks with no finding

- **APPEND:** `accept-c.py:265-272` preserves multiplicity: for each base line it requires the measured count to be at least `base_lines.count(line)`, then enforces the +24 total. Legitimately repeated base rows are not lost. The repeated `list.count` is quadratic, but 619 base rows are not a material cost here.
- **NOHARM:** `:274-279` names `main`, not `HEAD`/`--root`. Under the frozen receipt model, the measured revision is the lane’s `main` tip at receipt time, so comparing BASE..main is correct and catches every committed knowledge change at that measurement. If someone intends to measure an earlier claim commit after main has advanced, they must pin that commit; that is a different measured revision, not a counter defect at the receipt tip. The fixture’s NOHARM output was exactly the new entry.
- **SWEEP:** the local `topic_text in row_line` test (`:289-297`) is only substring-based, but SWEEP also requires `sweep.py` success. Its comparison at `reports/round-28/readme/sweep.py:136-141` checks the complete README row topic against the entry topic (with entry wrapping joined); a shortened/wrapped README row cannot pass the leg. No false PASS found here.
- **Copy-run scan:** for valid rows the quote is capped at 25 normalized words (`:172-175`), and the window search stops when a longer prefix ceases to be a quote substring (`:238-250`). It is correct for the stated contiguous-run metric and bounded by the short quote size per clause token; no complexity defect found on valid inputs.

## LIVE budget / retry gap

The 1500-second timeout is per locator subprocess, and the six selected rows run sequentially (`accept-c.py:301-307`), not under one 1500-second leg deadline. The frozen locator uses a 120-second `urlopen` timeout and three attempts with up to two 30-second waits for retryable HTTP errors (`reopen-quote.py:81-96`): the advertised worst-case request schedule is up to 420 seconds per URL, or 840 seconds per row / 5040 seconds across six rows. Therefore 1500 seconds is adequate for one row’s ordinary retry schedule, but not a whole six-row run under the assigned outer `timeout 900` command; a slow full run can be killed before emitting `ACCEPT-C-63`. A slow-trickle body can also outlive the socket timeout until the per-child 1500-second cap.

Separately, `fetch()` retries only `HTTPError` (`reopen-quote.py:89-93`); timeout/connection exceptions escape to `locate()`’s broad catch (`:214-216`) and move on without the promised three attempts. This contradicts the claims.json LIVE treatment for timeout/connection errors and can turn a transient event into an early NOT_LOCATED. No slow-host case was exercised here; the six local-example lookups completed quickly.

## Control receipts and PROBE

Frozen counter SHA-256 for every unchanged-counter run: `3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca`.

`RECEIPT kotodama-r63-w1-RevCounterC/freeze-empty counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=FAIL exit=1 stopped-by=FILE ROWS ONEID APPEND NOHARM SWEEP LIVE`

```text
FILE FAIL unreadable: [Errno 2] No such file or directory: '/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-RevCounterC/clone/corpus/knowledge/culture-material/headgear-head-covering-codes.md'
ROWS FAIL bad=['S694:rows=0', 'S695:rows=0', 'S696:rows=0', 'S697:rows=0', 'S698:rows=0', 'S699:rows=0', 'S700:rows=0', 'S701:rows=0'] checked=24
ONEID FAIL bad=[] cited_lines=0 cited_lines_tool=exit2 clean=False
RESTATE PASS bad=[] lines=0
LINK PASS bad=[]
APPEND FAIL missing_base_lines=0 base=619 measured=619 +24=False
NOHARM FAIL diff=[]
SWEEP FAIL exit=0 topic_row=False
LIVE FAIL subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=['S694:no_row', 'S698:no_row', 'S702:no_row', 'S706:no_row', 'S710:no_row', 'S714:no_row']
ACCEPT-C-63: FAIL
exit=1
```

`RECEIPT kotodama-r63-w1-RevCounterC/fake-capture counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=none`

```text
FILE PASS exists lines=28 h1=1 h2=0 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: PASS
exit=0
```

The clearly labeled scratch-only PROBE wrapper (`/fast/scratch/hyaku/kotodama-r63/kotodama-r63-w1-RevCounterC/PROBE/accept-c.PROBE.py`, SHA-256 `f79aeb6a1db7bc3e6852f842441a1fa6d43439cd8ca77208fc521f8f6ca1ccab`) imported the untouched frozen counter and changed only this regex at runtime:

```diff
-CAPTURE_RE = re.compile(r"web\.archive\.org/web/(\d+|[a-z]+)id_/(.+?)\s*(?:;|\||$)", re.IGNORECASE)
+CAPTURE_RE = re.compile(r"web\.archive\.org/web/(\d+)id_/(.+?)\s*(?:;|\||$)", re.IGNORECASE)
```

Its full result on the same synthetic fixture was:

```text
FILE PASS exists lines=28 h1=1 h2=0 h3=0 topic=True
ROWS FAIL bad=['S694:no_capture', 'S695:no_capture', 'S696:no_capture', 'S697:no_capture', 'S698:no_capture', 'S699:no_capture', 'S700:no_capture', 'S701:no_capture'] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: FAIL
exit=1
```

`PROBE-RECEIPT counter-sha256=f79aeb6a1db7bc3e6852f842441a1fa6d43439cd8ca77208fc521f8f6ca1ccab rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 delta=CAPTURE_RE digits-only exit=1`.

`RECEIPT kotodama-r63-w1-RevCounterC/fake-locator counter-sha256=3a5310342c9e17567964e8b20ea24126d0f31b9316cadccc0d2c41a80fe499ca rev=80d53ffde7788299b69dbb0bd0436b2b7ddddb95 frozen=PASS exit=0 stopped-by=none`

```text
FILE PASS exists lines=28 h1=1 h2=0 h3=0 topic=True
ROWS PASS bad=[] checked=24
ONEID PASS bad=[] cited_lines=24 cited_lines_tool=exit0 clean=True
RESTATE PASS bad=[] lines=24
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 base=619 measured=643 +24=True
NOHARM PASS diff=['corpus/knowledge/culture-material/headgear-head-covering-codes.md']
SWEEP PASS exit=0 topic_row=True
LIVE PASS subset=['S694', 'S698', 'S702', 'S706', 'S710', 'S714'] bad=[]
ACCEPT-C-63: PASS
exit=0
```

**CONTROL-MET** — the `fake-capture` and `fake-locator` scratch fixtures both get full frozen ACCEPT-C PASS while skipping archive verification; the smallest per-fixture guards are numeric-only timestamps and pinning the locator to frozen base bytes. Full 24-row live-and-capture checks remain necessary for the actual row contract.

## Verification gaps / residual risk

No claimed C data existed in the frozen tree; no actual S694–S717 source-support judgments were attempted. The full PASS runs above are explicitly synthetic controls, not evidence for the round’s real entry. The per-row SUPPORT reviewer artifacts remain necessary. No build, lint, or unrelated runtime checks were run.
