# MutCounterD — frozen depth-counter robustness

Axes: **depth** (predicate fidelity), **calibration** (distinguish a leg-level defect from an all-leg control), **operability** (bounded completion). Scope: one actual byte mutation in my isolated PROBE clone; offline diagnostics of the other assigned suspects. No lane source, counter, locator, sibling file, git history, or tool installation was changed.

## Result

**Confirmed SET false verdict:** `accept-d.py:148` reads ENTRY with universal-newline translation, unlike the decoded `git show` bytes at lines 144–145. Consequently lines 167–169 miss an unrelated LF→CRLF edit. With precisely four intended text differences, adding CR at the end of unrelated line 1 still prints `SET PASS ... differ=[63, 74, 75, 93]`; the byte oracle instead finds `[1, 63, 74, 75, 93]`. This contradicts SET's explicit “every other line byte-identical” clause at lines 11–12. `reg_text` at line 149 has the same newline-normalization exposure for APPEND.

**Verdict:** the mutation **survives frozen SET**; the independent byte oracle detects it (exit sequence 0→1→0). The **full frozen D mutation result is INCONCLUSIVE**, not a killed mutant: the intentionally unrepaired prepared baseline already fails other legs. No cheap fixture achieved the full frozen predicate.

Smallest counter change stopping this particular false verdict: retain line terminators when reading the current files, e.g. `open(..., newline="")` at lines 148–149, keeping the same LF split as BASE. No counter revision was made here.

**Confirmed timing mismatch, offline model:** the original LOCATE AST block, lines 265–285, consumes **2,622 virtual seconds and 18 requests for one row with two URLs**, on three successive 503 results per URL, each arriving after 119 seconds and carrying `Retry-After: 30`. The model executes the original locator retry code and original counter loop with only network I/O and time replaced. There were **zero real network requests**. Thus an attempt-count bound does not fit the prescribed 900-second receipt budget. [INFERENCE] Under the modeled timings, an ordinary 900-second receipt would time out before printing the final predicate, rather than finishing the declared three passes. This is not an observed live timeout. The source permits still longer runs: four URL slots, up to seven new rows, DNS without an explicit deadline, and response reads without an overall wall deadline.

## Mutation, fixtures and restoration

Scratch root: `/fast/scratch/hyaku/kotodama-r62/MutCounterD/`.

- `clone/`: made using the prescribed clone/checkout command, with GIT_DIR, GIT_WORK_TREE and GIT_INDEX_FILE unset; checked out `f0173481047a93c46798f90b68d71d4f169d2642`.
- `original-entry.bytes`: exact frozen entry.
- `baseline-entry.bytes`: positive SET calibration fixture, differing from original only by one trailing ASCII space on each of lines 63, 74, 75 and 93. It deliberately does **not** perform the claimed semantic repairs.
- `mutant-entry.bytes`: baseline plus **one inserted CR immediately before the first LF**, changing unrelated line 1 to CRLF. No other byte changes.
- `PROBE-counter-robustness.py`: read-only Python detector and offline diagnostics. It imports the untouched frozen counter/locator, compares SET against a byte oracle, and executes the original LOCATE AST block with a virtual clock. It does not write files or fetch pages.

Escaped mutation diff:

```text
ENTRY line 1 terminator only:
- ... worldbuilding surface\n
+ ... worldbuilding surface\r\n
```

Counter diff: **none**. Every frozen run used SHA-256 `3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4`.

| Bytes | SHA-256 |
|---|---|
| Original entry, before and final restoration | `eff2160a6b60dfe5a6fdc5128bcf10f65a963bef8636a0080584ff48466f8c72` |
| Prepared baseline, before and restored after mutation | `ea7b9f053d7dee70ad4d0b3013bdeb4f5744bed47b3362aeb0f72aa4ed9f7aa0` |
| One-byte mutant | `ebfc9b2efb7719f3abbf0e129313239fa9e77f0d70f94245dae9749d8b4b505f` |
| SOURCES, before and final; never modified | `eac31268b2fc29f1c978a3895800f66045b644da6287798dae3759a02449e9f2` |
| Frozen locator, final; never modified | `39d5bccc9a7676ab00ede2825ddfd453a1dd4fbf3c8df88f9f9db917b5721390` |
| PROBE detector | `bff4854f0d1d5a85ad03573e44a44e870d0d670c3e75a785db71c76d6b5d0922` |

The prepared baseline was restored and scored, then all preparation was removed and the exact original entry was restored and scored. Final `sha256sum` output matched original entry, SOURCES and counter hashes. All subprocesses were foreground and timeout-capped (30/60/120/180/900 seconds); all finished. No background service/process tree remains. Fixtures are retained only in the scratch root. Python 3.14.8 and git 2.56.0 were already available; installs/updates: **none**.

A CR-ending `edit` body was rejected as byte-identical; after re-reading, exact whole-file `write` calls applied/restored the fixture instead. The raw reader also omitted the final LF, caught by a hash guard before any write; restoring that LF matched the recorded baseline hash. Both tool inconsistencies were submitted through `xd://report_issue`.

## Other assigned suspects

These are code-inspection findings unless an observed PROBE output is named; they are not additional full-predicate mutation claims.

- **APPEND subsequence, lines 228–245:** the greedy scan implements the stated *subsequence* property. A deleted occurrence can be represented by an identical later occurrence only if the entire remaining BASE sequence still matches; this is not a counterexample to subsequence preservation. [INFERENCE] For non-row text, deleting an occurrence and replaying enough of its suffix can preserve the subsequence while changing where that text appears; inserted non-row lines are unchecked. For example BASE non-row tail `[x,a,x]`, changed tail `[a,x,a,x]` (delete first x; append a,x) still contains BASE in order. This exposes the difference between the informal “no base line deleted or edited” gloss and the actual frozen subsequence predicate, not an observed full PASS. Inserted old S-row ids are separately rejected at lines 240–244.
- **S687 used-by exception, lines 236–237:** observed 13 split cells, with prefix cells 0–10 compared and final cell 12 compared; only index 11 (used-by) is exempt. There is no apparent ordinary-cell loophole allowing tier, quote, status or source edits. No separate S687 mutation was scored.
- **`cells()` and embedded pipes, lines 188–197 and 209–212:** observed an escaped pipe turn 13 split cells into 14. New rows then fail ROWS (and SOLE when used at line 93). The canonical SOURCES v1 shape explicitly forbids `|` inside any cell, so this is not a valid-row false rejection under that contract. Old cited rows with a shifted quote cell also lose LINK; APPEND protects their original bytes apart from the newline issue above.
- **`cited_ids`, lines 77–78, 91–93, 171–173:** observed repeated `(S665) (S665)` and spaced `(S 665)` each produce `['S665']`. Occurrences are collapsed because the frozen docstring expressly says “one distinct S-id” at line 13. If “one S-id” is intended to prohibit repeated occurrences or to require canonical spelling, this is a specification gap; I do not silently reinterpret the frozen predicate.
- **LINK/COPY and digits, lines 253–261:** observed `10th-century` normalize to `10th`, `century`, and `10th` is counted as content despite having only two letters. The frozen docstring says **4+ characters**, agreeing with the implementation; the task's entry rule says **4+ letters**, which differs. COPY uses the same normalized tokenization on quote and line, consistent with the frozen normalized-word definition. Numerical factual fidelity beyond the matched words remains in the declared review-only scope; no full false verdict is claimed here.
- **LOCATE wall time, lines 273–278:** original loop has no wall deadline around `locator.locate`. Locator lines 81–96 use three attempts, 120-second request timeout, and up to two 30-second retry gaps **per URL**. The virtual-time witness above uses only two of four possible URLs. There is no evidence here of a live 900-second completion guarantee. A change in deadline/retry semantics would require an explicit pre-data contract decision, not a silent timeout waiver.
- **`git show BASE`, lines 63, 144–147:** BASE is intentionally round base `d42ffb890a54c8431fa891380b6c38bb608b8362`, not the later frozen-counter revision. `git -C root show BASE:path` is read-only and missing BASE is caught as an input error. Both subprocess calls lack a timeout (observed by AST inspection); inherited git environment is not sanitized by the counter itself. All my receipt processes explicitly unset the three named git variables. Alternate git-environment/history behavior was not experimentally tested and is not reported as a demonstrated false verdict.

## Frozen-counter receipts — complete stdout

Each command ran from the scratch clone:

```sh
timeout 900 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE python3 -B reports/round-62/accept-d.py; echo exit=$?
```

### 1. Original frozen bytes

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:56Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT MutCounterD/original counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### 2. Prepared pristine SET fixture

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T10:59Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT MutCounterD/prepared-pristine counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### 3. One-byte CRLF mutant

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T11:00Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT MutCounterD/crlf-mutant counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### 4. Exact restored prepared fixture

```text
SET PASS lines=108 base=108 differ=[63, 74, 75, 93]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T11:01Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT MutCounterD/prepared-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

### 5. Final exact original restoration

```text
SET FAIL lines=108 base=108 differ=[]
ONEID PASS 63:['S692'] 74:['S665'] 75:['S666'] 93:['S687']
NOMARK PASS marked=[]
OPEN FAIL ids=['S692']
HEDGE FAIL ids=['S666']
CAPTION FAIL ids=['S665']
SOLE FAIL id=S687 tier=C
ROWS FAIL cited=[] registry=[] bad=[]
APPEND PASS base_lines=746 matched=746 missing=[] inserted_rows=[]
LINK PASS bad=[]
COPY PASS bad=[]
LOCATE FAIL located=0 cited=0 at=2026-10-23T11:01Z not_located=[]
ACCESS PASS exit=0
LINT PASS exit=0 CITED-LINES: 0 finding(s) in 1 file(s)
ACCEPT-D-62: FAIL
exit=1
```

RECEIPT MutCounterD/original-restored counter-sha256=3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=SET,OPEN,HEDGE,CAPTION,SOLE,ROWS,LOCATE

NONE-MET MutCounterD/crlf-mutant — `/fast/scratch/hyaku/kotodama-r62/MutCounterD/mutant-entry.bytes` did not meet the full frozen counter. It did expose SET's false PASS; retaining original newlines at accept-d.py:148 is the smallest change stopping that leg-level defect. No claim admission or integration judgment is made.

## Same bounded PROBE on pristine, mutated and restored bytes

Command, identically each time:

```sh
timeout 60 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE python3 -B /fast/scratch/hyaku/kotodama-r62/MutCounterD/PROBE-counter-robustness.py; echo exit=$?
```

### Prepared pristine

```text
PROBE_COUNTER_SHA256 3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4
PROBE_ENTRY_SHA256 ea7b9f053d7dee70ad4d0b3013bdeb4f5744bed47b3362aeb0f72aa4ed9f7aa0
PROBE_SET text=PASS text_differ=[63, 74, 75, 93] byte=PASS byte_differ=[63, 74, 75, 93] crlf=0
PROBE_GIT_SHOW line=144 timeout_keyword=False
PROBE_GIT_SHOW line=146 timeout_keyword=False
PROBE_NUMERIC words=['the', 'earliest', 'evidence', 'we', 'have', 'is', 'from', 'a', '10th', 'century', 'persian', 'bowl'] content=['earliest', 'evidence', '10th', 'century', 'persian', 'bowl']
PROBE_IDS repeated=['S665'] spaced=['S665']
PROBE_S687 cells=13 compared_prefix_cells=11 exempt_index=11 exempt_value='corpus/knowledge/culture-material/footwear-codes-terminology.md' final=''
PROBE_PIPE ordinary_cells=13 escaped_pipe_cells=14
PROBE_SLOW_HOST virtual_seconds=2622 requests=18 receipt_cap=900 over_cap=True
PROBE_LOCATE FAIL located=0 cited=1 at=2026-10-23T10:59Z not_located=['S693: https://example.org/article HTTPError; https://web.archive.org/web/20261023000000id_/https://example.org/article HTTPError (passes=3)']
PROBE_NETWORK actual_requests=0
PROBE_SET_ORACLE: PASS
exit=0
```

### Mutated

```text
PROBE_COUNTER_SHA256 3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4
PROBE_ENTRY_SHA256 ebfc9b2efb7719f3abbf0e129313239fa9e77f0d70f94245dae9749d8b4b505f
PROBE_SET text=PASS text_differ=[63, 74, 75, 93] byte=FAIL byte_differ=[1, 63, 74, 75, 93] crlf=1
PROBE_GIT_SHOW line=144 timeout_keyword=False
PROBE_GIT_SHOW line=146 timeout_keyword=False
PROBE_NUMERIC words=['the', 'earliest', 'evidence', 'we', 'have', 'is', 'from', 'a', '10th', 'century', 'persian', 'bowl'] content=['earliest', 'evidence', '10th', 'century', 'persian', 'bowl']
PROBE_IDS repeated=['S665'] spaced=['S665']
PROBE_S687 cells=13 compared_prefix_cells=11 exempt_index=11 exempt_value='corpus/knowledge/culture-material/footwear-codes-terminology.md' final=''
PROBE_PIPE ordinary_cells=13 escaped_pipe_cells=14
PROBE_SLOW_HOST virtual_seconds=2622 requests=18 receipt_cap=900 over_cap=True
PROBE_LOCATE FAIL located=0 cited=1 at=2026-10-23T11:00Z not_located=['S693: https://example.org/article HTTPError; https://web.archive.org/web/20261023000000id_/https://example.org/article HTTPError (passes=3)']
PROBE_NETWORK actual_requests=0
PROBE_SET_ORACLE: FAIL
exit=1
```

### Restored

```text
PROBE_COUNTER_SHA256 3efb3bc6286a2b9e1d4b12cb5fb9bd64fd663ce6692214bee373f71fa12063f4
PROBE_ENTRY_SHA256 ea7b9f053d7dee70ad4d0b3013bdeb4f5744bed47b3362aeb0f72aa4ed9f7aa0
PROBE_SET text=PASS text_differ=[63, 74, 75, 93] byte=PASS byte_differ=[63, 74, 75, 93] crlf=0
PROBE_GIT_SHOW line=144 timeout_keyword=False
PROBE_GIT_SHOW line=146 timeout_keyword=False
PROBE_NUMERIC words=['the', 'earliest', 'evidence', 'we', 'have', 'is', 'from', 'a', '10th', 'century', 'persian', 'bowl'] content=['earliest', 'evidence', '10th', 'century', 'persian', 'bowl']
PROBE_IDS repeated=['S665'] spaced=['S665']
PROBE_S687 cells=13 compared_prefix_cells=11 exempt_index=11 exempt_value='corpus/knowledge/culture-material/footwear-codes-terminology.md' final=''
PROBE_PIPE ordinary_cells=13 escaped_pipe_cells=14
PROBE_SLOW_HOST virtual_seconds=2622 requests=18 receipt_cap=900 over_cap=True
PROBE_LOCATE FAIL located=0 cited=1 at=2026-10-23T11:01Z not_located=['S693: https://example.org/article HTTPError; https://web.archive.org/web/20261023000000id_/https://example.org/article HTTPError (passes=3)']
PROBE_NETWORK actual_requests=0
PROBE_SET_ORACLE: PASS
exit=0
```

No full-pass baseline, live-source result, or claim-O result is asserted. The assigned mutation probe is complete and exact bytes are restored.
