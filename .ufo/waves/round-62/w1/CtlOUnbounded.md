# Claim O over-retry controls — KotodamaR62.CtlOUnbounded

## Scope and axes

Operability controls only, and only the over-retry half of claim O's control list. No lane implementation was built, judged or integrated; the frozen counter and the lane repo were not modified. Every fixture below is a **scratch** stand-in for `tools/reopen-row.py`, authored only so that the frozen counter has something to score; it is not a candidate lane implementation and no part of it was written into the lane.

- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, branch `main` (jj-colocated), measured revision `f0173481047a93c46798f90b68d71d4f169d2642`.
- Frozen counter: `reports/round-62/accept-o.py`, SHA-256 `bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551`. Byte-identical in every run below (verified by `sha256sum` over all ten worktrees) and in the lane repo itself. It was never edited.
- Scratch root: `/fast/scratch/hyaku/kotodama-r62/CtlOUnbounded/`.
- `tools/reopen-row.py` is **absent** at `f0173481` (`git cat-file -e f0173481:tools/reopen-row.py` → `does not exist`), matching `claims.json`'s `unmoved_command` for claim O.
- Scratch clone: `git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin clone && git -C clone checkout -q f0173481047a93c46798f90b68d71d4f169d2642`; ten detached worktrees (`wt_<case>`) at the same revision carry one fixture each. No `git`/`jj` write command was run in the lane repo or the fleet repo. All files live under the scratch root; every file is far below 5 MB.
- Every counter invocation: `cd wt_<case> && timeout 900 python3 -B reports/round-62/accept-o.py`, cwd = the worktree, `-B` (no bytecode), each case in its own worktree, runs batched in parallel where the harness allowed it. Each run used the counter's own run-time random local fixture. All spawned processes completed; no background job of mine remains (`pgrep -af CtlOUnbounded` → empty).
- No installs were needed and none were performed.
- Only this report was written into the lane.

### Baseline used for the mutations

`variants/base/tools/reopen-row.py` (SHA-256 `321648bd2bf7bce428ef46cbadb0802dadd94dffb24f39921ca4791d3f8bfbfd`) is an honest independent implementation of the contract in the counter's docstring. It is the **positive calibration**: it passes every leg (`ACCEPT-O-62: PASS`, exit 0), so each mutant below differs from a known-good tool by exactly one minimal patch and any failure is attributable to that patch.

## Result

**Four of the five mandated over-retry classes are caught by the frozen counter; one is not.** The frozen counter kills an over-broad per-URL attempt bound, an extra pass after a LOCATED verdict, an extra pass after a non-transient ABSENT verdict, and retries on 4xx — each by `GEN` and `BOUND`. It does **not** see a tool that keeps fetching the row's remaining URLs after the first BODY match: the frozen fixture never places a BODY-matching URL before a second URL of the same row, so that over-fetch is invisible to every leg.

| Mandated over-retry class | Fixture | Frozen verdict | Stopped by | Result |
|---|---|---|---|---|
| 5 attempts per URL | `variants/c1_attempts5/tools/reopen-row.py` | `ACCEPT-O-62: FAIL` exit 1 | `GEN`, `BOUND`, `DEFAULT` | killed |
| passes continue after a LOCATED | `variants/c2_pass_after_located/tools/reopen-row.py` | `ACCEPT-O-62: FAIL` exit 1 | `GEN`, `BOUND` | killed |
| a new pass after an ABSENT (non-transient) pass | `variants/c3_pass_after_absent/tools/reopen-row.py` | `ACCEPT-O-62: FAIL` exit 1 | `GEN`, `BOUND` | killed |
| 4xx retried | `variants/c4_retry_4xx/tools/reopen-row.py` | `ACCEPT-O-62: FAIL` exit 1 | `GEN`, `BOUND` | killed |
| every URL fetched even after a BODY match | `variants/c5_fetch_all_urls/tools/reopen-row.py` | **`ACCEPT-O-62: PASS` exit 0** | none | **SURVIVED** |

Three further over-retry shapes were probed beyond the mandated five; two are killed, one survives:

| Extra over-retry class | Fixture | Frozen verdict | Stopped by | Result |
|---|---|---|---|---|
| 10 attempts per URL | `variants/c6_attempts10/tools/reopen-row.py` | `ACCEPT-O-62: FAIL` exit 1 | `GEN`, `BOUND`, `DEFAULT` | killed |
| same URL re-fetched after a BODY match | `variants/c7_refetch_after_match/tools/reopen-row.py` | `ACCEPT-O-62: FAIL` exit 1 | `GEN`, `BOUND` | killed |
| a further pass after a CAPTION_ONLY pass | `variants/c9_pass_after_caption/tools/reopen-row.py` | `ACCEPT-O-62: FAIL` exit 1 | `GEN`, `BOUND` | killed |
| a 200 whose body lacks the quote is re-requested | `variants/c8_retry_after_200_nomatch/tools/reopen-row.py` | `ACCEPT-O-62: FAIL` exit 1 | `GEN`, `BOUND` | killed |
| an extra request to a URL the row does not list, uncounted | `variants/c11_aux_url_fetch/tools/reopen-row.py` | **`ACCEPT-O-62: PASS` exit 0** | none | **SURVIVED** |
| the same extra request, counted in `attempts=` | `variants/c12_aux_url_counted/tools/reopen-row.py` | `ACCEPT-O-62: FAIL` exit 1 | `GEN`, `PRIV`, `DEFAULT` | killed |

### The surviving over-retry is real, not an artifact of my fixture

`probe_c5_blindspot.py` and `probe_c11_extra_request.py` (both clearly labelled PROBEs, not counters) drive the base and the surviving mutants against a local server that records every path it is asked for. Measured server-side hits:

```text
=== base (row lists 2 url(s)) ===
ROW S1 LOCATED attempts=1 url=http://127.0.0.1:39325/live
REOPEN: 1/1 located
server saw: {'/live': 1}
=== c5_fetch_all_urls (row lists 2 url(s)) ===
ROW S1 LOCATED attempts=2 url=http://127.0.0.1:41887/arch
REOPEN: 1/1 located
server saw: {'/live': 1, '/arch': 1}
=== c11_aux_url_fetch (row lists 1 url(s)) ===
ROW S1 LOCATED attempts=2 url=http://127.0.0.1:44535/live
REOPEN: 1/1 located
server saw: {'/live': 1, '/__aux_overfetch': 1}
```

The base stops at the first BODY match and asks for one URL. `c5` asks for the row's second URL even though the first already carried the quote in body text — the contract's "A pass tries the row's URLs in order and stops at the first BODY match" is violated, and the row's reported `url=` moves from the live URL to the archive. `c11` issues a request to a URL the registry row never lists.

Both matter for the lane's use of the tool: `corpus/SOURCES.md` has **618** registry rows, of which **101** list a `capture` URL. A tool with the `c5` shape will, on every such row whose live URL answers 200 with the quote in body text, request the archive as well — the exact traffic the contract's "stop at the first BODY match" rule exists to avoid, and it mis-attributes the located URL. [INFERENCE] This is the mechanism by which the round-61 S671 class (live 403, capture carries the quote) could be reached by an over-fetching tool that never needed the capture.

### Why the frozen counter cannot see it

`accept-o.py`'s `build()` gives a row two URLs (`live` + `arch`) only for the classes `DEAD_ARCHIVE`, `ARCHIVE_CAPTION` and `DEAD_THEN_BODY2` (lines 202–212). In all three, the `live` path answers a **non-200** (403 / 410 / 500) and the archive carries the quote. Every class whose `live` path answers 200 with the quote in body text (`BODY`, `BODY_SPLIT`, `PLAIN`, `TRANSIENT2`, `TRANSIENT_PASS`) has a **single** URL. There is therefore no fixture row in which a BODY-matching URL is followed by another URL of the same row, which is the only shape in which "stops at the first BODY match" and "fetches every URL" differ. `BOUND` compares `fx.hits` per path role against `CLASSES[cls][2]`, and `GEN` compares the row's printed verdict and attempt count against the same table — both tables are blind to the difference.

The `c11` shape survives for a second, independent reason: `BOUND` only inspects the paths the fixture registered (`live`, `arch`). A request to any other path is not counted anywhere, and `attempts=` is the tool's own report, so a tool that does not count it stays invisible. The counted twin (`c12`) is caught, confirming that the leak is specifically the uncounted extra request.

## Per-item control verdicts

CONTROL-MET KotodamaR62.CtlOUnbounded/c5_fetch_all_urls fixture=`/fast/scratch/hyaku/kotodama-r62/CtlOUnbounded/variants/c5_fetch_all_urls/tools/reopen-row.py`; frozen=PASS (exit 0); violates "a pass tries the row's URLs in order and stops at the first BODY match". Smallest frozen-counter change that would stop this observed fixture: add one fixture class in which the row's **first** URL answers 200 with the quote in body text and the row also lists a second URL, with expected hits `{live: 1, arch: 0}` — i.e. a class like `EARLY_BODY` in the PROBE counter below. Measured on the PROBE (not the frozen counter): base `ACCEPT-O-62: PASS` exit 0, c5 `ACCEPT-O-62: FAIL` exit 1 stopped by `GEN` (`EARLY_BODY: want=LOCATED/1: got=LOCATED/2`) and `BOUND` (`EARLY_BODY:arch: want=0: hits=1`). Proposed only; the frozen counter was not changed.

CONTROL-MET KotodamaR62.CtlOUnbounded/c11_aux_url_fetch fixture=`/fast/scratch/hyaku/kotodama-r62/CtlOUnbounded/variants/c11_aux_url_fetch/tools/reopen-row.py`; frozen=PASS (exit 0); issues an HTTP request to a URL the registry row does not list and does not report it in `attempts=`. Smallest frozen-counter change that would stop this observed fixture: sum the server's observed hits per row across **all** paths (not only the registered `live`/`arch` roles) and require the total to equal the row's reported `attempts=`; the counted twin `c12` shows the existing `attempts=` comparison already detects the same request once it is declared, so the missing half is the server-side total. Proposed only; not implemented.

NONE-MET KotodamaR62.CtlOUnbounded/c1_attempts5 fixture=`/fast/scratch/hyaku/kotodama-r62/CtlOUnbounded/variants/c1_attempts5/tools/reopen-row.py`; frozen=FAIL; stopped-by=GEN,BOUND,DEFAULT; no counter change needed to stop this fixture.

NONE-MET KotodamaR62.CtlOUnbounded/c2_pass_after_located fixture=`/fast/scratch/hyaku/kotodama-r62/CtlOUnbounded/variants/c2_pass_after_located/tools/reopen-row.py`; frozen=FAIL; stopped-by=GEN,BOUND; no counter change needed to stop this fixture.

NONE-MET KotodamaR62.CtlOUnbounded/c3_pass_after_absent fixture=`/fast/scratch/hyaku/kotodama-r62/CtlOUnbounded/variants/c3_pass_after_absent/tools/reopen-row.py`; frozen=FAIL; stopped-by=GEN,BOUND; no counter change needed to stop this fixture.

NONE-MET KotodamaR62.CtlOUnbounded/c4_retry_4xx fixture=`/fast/scratch/hyaku/kotodama-r62/CtlOUnbounded/variants/c4_retry_4xx/tools/reopen-row.py`; frozen=FAIL; stopped-by=GEN,BOUND; no counter change needed to stop this fixture.

NONE-MET KotodamaR62.CtlOUnbounded/c6_attempts10 fixture=`/fast/scratch/hyaku/kotodama-r62/CtlOUnbounded/variants/c6_attempts10/tools/reopen-row.py`; frozen=FAIL; stopped-by=GEN,BOUND,DEFAULT; no counter change needed to stop this fixture.

NONE-MET KotodamaR62.CtlOUnbounded/c7_refetch_after_match fixture=`/fast/scratch/hyaku/kotodama-r62/CtlOUnbounded/variants/c7_refetch_after_match/tools/reopen-row.py`; frozen=FAIL; stopped-by=GEN,BOUND; no counter change needed to stop this fixture.

NONE-MET KotodamaR62.CtlOUnbounded/c8_retry_after_200_nomatch fixture=`/fast/scratch/hyaku/kotodama-r62/CtlOUnbounded/variants/c8_retry_after_200_nomatch/tools/reopen-row.py`; frozen=FAIL; stopped-by=GEN,BOUND; no counter change needed to stop this fixture.

NONE-MET KotodamaR62.CtlOUnbounded/c9_pass_after_caption fixture=`/fast/scratch/hyaku/kotodama-r62/CtlOUnbounded/variants/c9_pass_after_caption/tools/reopen-row.py`; frozen=FAIL; stopped-by=GEN,BOUND; no counter change needed to stop this fixture.

NONE-MET KotodamaR62.CtlOUnbounded/c12_aux_url_counted fixture=`/fast/scratch/hyaku/kotodama-r62/CtlOUnbounded/variants/c12_aux_url_counted/tools/reopen-row.py`; frozen=FAIL; stopped-by=GEN,PRIV,DEFAULT; no counter change needed to stop this fixture.

## A third, adjacent gap in the same counter (found while probing, not a mandated over-retry)

The `url=` field of the `ROW` line is defined by the contract ("url = the URL that gave the verdict's match, else `-`") and is captured by the counter's `ROWLINE` regex as group 4, but `parse()` (accept-o.py:284–289) keeps only groups 1–3, so group 4 is never compared against anything. A tool that prints `url=-` for every LOCATED row passes every leg: `variants/c10_report_dash_url/tools/reopen-row.py` → `ACCEPT-O-62: PASS` exit 0.

CONTROL-MET KotodamaR62.CtlOUnbounded/c10_report_dash_url fixture=`/fast/scratch/hyaku/kotodama-r62/CtlOUnbounded/variants/c10_report_dash_url/tools/reopen-row.py`; frozen=PASS (exit 0); prints `url=-` for every LOCATED row although the contract requires the matching URL. Smallest frozen-counter change that would stop this observed fixture: compare `ROWLINE` group 4 against the expected value for the class — non-`-` for `LOCATED`/`CAPTION_ONLY`, `-` for the no-match verdicts. Measured on the PROBE (not the frozen counter): base `ACCEPT-O-62: PASS` exit 0 with `url_bad=[]`, c10 `ACCEPT-O-62: FAIL` exit 1 with `url_bad=['S9687', 'S6348', 'S3668', 'S4417', 'S9255', 'S9336']`. Proposed only; the frozen counter was not changed.

This gap compounds the `c5` survivor: an over-fetching tool that fetches the archive after a live BODY match reports the **archive** URL as the located URL, and no leg checks that field either.

## Full frozen-counter receipts

Every stdout below is complete and untrimmed; stderr was empty for every run. Each run used the counter's own run-time random local fixture. The trailing `exit=` is the captured process exit code.

### base (honest independent implementation — positive calibration)

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S5937', 'REFUSED', 0), ('S1891', 'REFUSED', 0), ('S4272', 'REFUSED', 0)]
DEFAULT PASS rows=[('S3592', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT KotodamaR62.CtlOUnbounded/base counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### c1_attempts5 (5 attempts per URL)

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=5 ["DEAD:S1658:want=UNREACHABLE/9:got=[('UNREACHABLE', 15)]", "DEAD_THEN_BODY2:S1456:want=LOCATED/4:got=[('LOCATED', 6)]", "DEAD_THEN_BODY2:S1388:want=LOCATED/4:got=[('LOCATED', 6)]", "DEAD:S1928:want=UNREACHABLE/9:got=[('UNREACHABLE', 15)]", "DEAD_PORT:S2433:want=UNREACHABLE/9:got=[('UNREACHABLE', 15)]"] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD:live:want=9:hits=15', 'DEAD_THEN_BODY2:live:want=3:hits=5', 'DEAD_THEN_BODY2:live:want=3:hits=5', 'DEAD:live:want=9:hits=15']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S1314', 'REFUSED', 0), ('S6711', 'REFUSED', 0), ('S7767', 'REFUSED', 0)]
DEFAULT FAIL rows=[('S4692', 'UNREACHABLE', 15)] wall=180s hits=15 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT KotodamaR62.CtlOUnbounded/c1_attempts5 counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND,DEFAULT

### c2_pass_after_located (a pass continues after a LOCATED verdict)

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=14 ["DEAD_THEN_BODY2:S1581:want=LOCATED/4:got=[('LOCATED', 12)]", "BODY:S2679:want=LOCATED/1:got=[('LOCATED', 3)]", "TRANSIENT2:S3873:want=LOCATED/3:got=[('LOCATED', 5)]", "TRANSIENT2:S9959:want=LOCATED/3:got=[('LOCATED', 5)]", "TRANSIENT_PASS:S9419:want=LOCATED/4:got=[('LOCATED', 5)]", "TRANSIENT_PASS:S2853:want=LOCATED/4:got=[('LOCATED', 5)]"] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=3', 'BODY:live:want=1:hits=3', 'TRANSIENT2:live:want=3:hits=5', 'TRANSIENT2:live:want=3:hits=5', 'TRANSIENT_PASS:live:want=4:hits=5', 'TRANSIENT_PASS:live:want=4:hits=5', 'BODY:live:want=1:hits=3']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S4043', 'REFUSED', 0), ('S4390', 'REFUSED', 0), ('S1722', 'REFUSED', 0)]
DEFAULT PASS rows=[('S8501', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT KotodamaR62.CtlOUnbounded/c2_pass_after_located counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND

### c3_pass_after_absent (a new pass after an ABSENT, non-transient pass)

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=8 ["TRANSIENT2:S8932:want=LOCATED/3:got=[('LOCATED', 4)]", "SCRIPT:S1664:want=ABSENT/1:got=[('ABSENT', 3)]", "DEAD_THEN_BODY2:S6946:want=LOCATED/4:got=[('LOCATED', 12)]", "TRANSIENT2:S2347:want=LOCATED/3:got=[('LOCATED', 4)]", "ABSENT:S8843:want=ABSENT/1:got=[('ABSENT', 3)]", "DEAD_THEN_BODY2:S8064:want=LOCATED/4:got=[('LOCATED', 12)]"] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['TRANSIENT2:live:want=3:hits=4', 'SCRIPT:live:want=1:hits=3', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=3', 'TRANSIENT2:live:want=3:hits=4', 'TRANSIENT2:live:want=3:hits=4', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=3']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S5442', 'REFUSED', 0), ('S5572', 'REFUSED', 0), ('S1200', 'REFUSED', 0)]
DEFAULT PASS rows=[('S1563', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT KotodamaR62.CtlOUnbounded/c3_pass_after_absent counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND

### c4_retry_4xx (4xx answers retried)

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=6 ["GONE:S9258:want=UNREACHABLE/1:got=[('UNREACHABLE', 9)]", "GONE:S6266:want=UNREACHABLE/1:got=[('UNREACHABLE', 9)]", "DEAD_ARCHIVE:S3341:want=LOCATED/2:got=[('LOCATED', 4)]", "ARCHIVE_CAPTION:S5088:want=CAPTION_ONLY/2:got=[('CAPTION_ONLY', 12)]", "ARCHIVE_CAPTION:S9800:want=CAPTION_ONLY/2:got=[('CAPTION_ONLY', 12)]", "DEAD_ARCHIVE:S9166:want=LOCATED/2:got=[('LOCATED', 4)]"] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['GONE:live:want=1:hits=9', 'GONE:live:want=1:hits=9', 'DEAD_ARCHIVE:live:want=1:hits=3', 'ARCHIVE_CAPTION:live:want=1:hits=9', 'ARCHIVE_CAPTION:arch:want=1:hits=3', 'ARCHIVE_CAPTION:live:want=1:hits=9', 'ARCHIVE_CAPTION:arch:want=1:hits=3', 'DEAD_ARCHIVE:live:want=1:hits=3']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S1576', 'REFUSED', 0), ('S2116', 'REFUSED', 0), ('S6527', 'REFUSED', 0)]
DEFAULT PASS rows=[('S1272', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT KotodamaR62.CtlOUnbounded/c4_retry_4xx counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND

### c5_fetch_all_urls (every URL fetched even after a BODY match) — SURVIVED

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S1198', 'REFUSED', 0), ('S7201', 'REFUSED', 0), ('S7221', 'REFUSED', 0)]
DEFAULT PASS rows=[('S6321', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT KotodamaR62.CtlOUnbounded/c5_fetch_all_urls counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### c6_attempts10 (10 attempts per URL)

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=5 ["DEAD_THEN_BODY2:S2511:want=LOCATED/4:got=[('LOCATED', 11)]", "DEAD_THEN_BODY2:S3064:want=LOCATED/4:got=[('LOCATED', 11)]", "DEAD:S1670:want=UNREACHABLE/9:got=[('UNREACHABLE', 30)]", "DEAD:S7210:want=UNREACHABLE/9:got=[('UNREACHABLE', 30)]", "DEAD_PORT:S3099:want=UNREACHABLE/9:got=[('UNREACHABLE', 30)]"] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD_THEN_BODY2:live:want=3:hits=10', 'DEAD_THEN_BODY2:live:want=3:hits=10', 'DEAD:live:want=9:hits=30', 'DEAD:live:want=9:hits=30']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S1107', 'REFUSED', 0), ('S2259', 'REFUSED', 0), ('S2596', 'REFUSED', 0)]
DEFAULT FAIL rows=[('S2492', 'UNREACHABLE', 30)] wall=255s hits=30 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT KotodamaR62.CtlOUnbounded/c6_attempts10 counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND,DEFAULT

### c7_refetch_after_match (same URL re-fetched after a BODY match)

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=12 ["PLAIN:S8824:want=LOCATED/1:got=[('LOCATED', 3)]", "DEAD_ARCHIVE:S3725:want=LOCATED/2:got=[('LOCATED', 4)]", "BODY:S2016:want=LOCATED/1:got=[('LOCATED', 3)]", "TRANSIENT_PASS:S2640:want=LOCATED/4:got=[('LOCATED', 6)]", "TRANSIENT_PASS:S1412:want=LOCATED/4:got=[('LOCATED', 6)]", "BODY_SPLIT:S9866:want=LOCATED/1:got=[('LOCATED', 3)]"] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['PLAIN:live:want=1:hits=3', 'DEAD_ARCHIVE:arch:want=1:hits=3', 'BODY:live:want=1:hits=3', 'TRANSIENT_PASS:live:want=4:hits=6', 'TRANSIENT_PASS:live:want=4:hits=6', 'BODY_SPLIT:live:want=1:hits=3', 'BODY:live:want=1:hits=3', 'PLAIN:live:want=1:hits=3']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S6553', 'REFUSED', 0), ('S1472', 'REFUSED', 0), ('S8183', 'REFUSED', 0)]
DEFAULT PASS rows=[('S9230', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT KotodamaR62.CtlOUnbounded/c7_refetch_after_match counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND

### c8_retry_after_200_nomatch (a 200 without the quote is re-requested)

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=12 ["ARCHIVE_CAPTION:S4440:want=CAPTION_ONLY/2:got=[('CAPTION_ONLY', 4)]", "CAP_CLASS:S7662:want=CAPTION_ONLY/1:got=[('CAPTION_ONLY', 3)]", "ABSENT:S9270:want=ABSENT/1:got=[('ABSENT', 3)]", "ARCHIVE_CAPTION:S2022:want=CAPTION_ONLY/2:got=[('CAPTION_ONLY', 4)]", "CAP_FIG:S8794:want=CAPTION_ONLY/1:got=[('CAPTION_ONLY', 3)]", "CAP_ATTR:S4621:want=CAPTION_ONLY/1:got=[('CAPTION_ONLY', 3)]"] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['ARCHIVE_CAPTION:arch:want=1:hits=3', 'CAP_CLASS:live:want=1:hits=3', 'ABSENT:live:want=1:hits=3', 'ARCHIVE_CAPTION:arch:want=1:hits=3', 'CAP_FIG:live:want=1:hits=3', 'CAP_ATTR:live:want=1:hits=3', 'SCRIPT:live:want=1:hits=3', 'CAP_CLASS:live:want=1:hits=3']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S7948', 'REFUSED', 0), ('S6258', 'REFUSED', 0), ('S8377', 'REFUSED', 0)]
DEFAULT PASS rows=[('S5111', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT KotodamaR62.CtlOUnbounded/c8_retry_after_200_nomatch counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND

### c9_pass_after_caption (a further pass after a CAPTION_ONLY pass)

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=12 ["DEAD_THEN_BODY2:S1084:want=LOCATED/4:got=[('LOCATED', 12)]", "CAP_CLASS:S7520:want=CAPTION_ONLY/1:got=[('CAPTION_ONLY', 3)]", "CAP_ATTR:S4266:want=CAPTION_ONLY/1:got=[('CAPTION_ONLY', 3)]", "DEAD_THEN_BODY2:S7233:want=LOCATED/4:got=[('LOCATED', 12)]", "TRANSIENT2:S3867:want=LOCATED/3:got=[('LOCATED', 4)]", "CAP_FIG:S8769:want=CAPTION_ONLY/1:got=[('CAPTION_ONLY', 3)]"] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND FAIL bad=['DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=3', 'CAP_CLASS:live:want=1:hits=3', 'CAP_ATTR:live:want=1:hits=3', 'DEAD_THEN_BODY2:live:want=3:hits=9', 'DEAD_THEN_BODY2:arch:want=1:hits=3', 'TRANSIENT2:live:want=3:hits=4', 'CAP_FIG:live:want=1:hits=3']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S2120', 'REFUSED', 0), ('S8860', 'REFUSED', 0), ('S4259', 'REFUSED', 0)]
DEFAULT PASS rows=[('S6114', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT KotodamaR62.CtlOUnbounded/c9_pass_after_caption counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,BOUND

### c10_report_dash_url (`url=-` printed for every LOCATED row) — SURVIVED

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S5261', 'REFUSED', 0), ('S5833', 'REFUSED', 0), ('S8079', 'REFUSED', 0)]
DEFAULT PASS rows=[('S9088', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT KotodamaR62.CtlOUnbounded/c10_report_dash_url counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### c11_aux_url_fetch (uncounted request to a URL the row does not list) — SURVIVED

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S2502', 'REFUSED', 0), ('S9879', 'REFUSED', 0), ('S6971', 'REFUSED', 0)]
DEFAULT PASS rows=[('S5181', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

RECEIPT KotodamaR62.CtlOUnbounded/c11_aux_url_fetch counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=PASS exit=0 stopped-by=none

### c12_aux_url_counted (the same extra request, counted in `attempts=`)

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=31 ["PLAIN:S9767:want=LOCATED/1:got=[('LOCATED', 2)]", "BODY_SPLIT:S4263:want=LOCATED/1:got=[('LOCATED', 2)]", "DEAD_ARCHIVE:S9304:want=LOCATED/2:got=[('LOCATED', 3)]", "PLAIN:S1465:want=LOCATED/1:got=[('LOCATED', 2)]", "CAP_ATTR:S9509:want=CAPTION_ONLY/1:got=[('CAPTION_ONLY', 2)]", "DEAD:S5305:want=UNREACHABLE/9:got=[('UNREACHABLE', 10)]"] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV FAIL exit=1 rows=[('S9090', 'REFUSED', 1), ('S6745', 'REFUSED', 1), ('S4369', 'REFUSED', 1)]
DEFAULT FAIL rows=[('S1601', 'UNREACHABLE', 10)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

RECEIPT KotodamaR62.CtlOUnbounded/c12_aux_url_counted counter-sha256=bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551 rev=f0173481047a93c46798f90b68d71d4f169d2642 frozen=FAIL exit=1 stopped-by=GEN,PRIV,DEFAULT

## PROBE-counter receipts (labelled PROBE, not the frozen counter)

These used `probe/accept-o-probe.py` and `probe/accept-o-probe2-url.py`, which are copies of the frozen counter with one added check each. They exist only to show that a *small* frozen-counter change would stop the survivors. The frozen counter was not modified and no receipt above depends on these PROBEs.

### PROBE 1 (`EARLY_BODY` class) on base — must PASS

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=39 wrong=0 [] summary_ok=True exit=1
ORDER PASS printed=39 expected=39
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S8549', 'REFUSED', 0), ('S2365', 'REFUSED', 0), ('S2453', 'REFUSED', 0)]
DEFAULT PASS rows=[('S8791', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

### PROBE 1 on c5_fetch_all_urls — killed

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=39 wrong=2 ["EARLY_BODY:S6350:want=LOCATED/1:got=[('LOCATED', 2)]", "EARLY_BODY:S6401:want=LOCATED/1:got=[('LOCATED', 2)]"] summary_ok=True exit=1
ORDER PASS printed=39 expected=39
BOUND FAIL bad=['EARLY_BODY:arch:want=0:hits=1', 'EARLY_BODY:arch:want=0:hits=1']
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S3118', 'REFUSED', 0), ('S3833', 'REFUSED', 0), ('S2615', 'REFUSED', 0)]
DEFAULT PASS rows=[('S7268', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

### PROBE 2 (`url=` field check) on base — must PASS

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN PASS rows=37 wrong=0 [] url_bad=[] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S4570', 'REFUSED', 0), ('S1237', 'REFUSED', 0), ('S2472', 'REFUSED', 0)]
DEFAULT PASS rows=[('S1621', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: PASS
exit=0
```

### PROBE 2 on c10_report_dash_url — killed

```text
TOOL PASS path=tools/reopen-row.py exists=True
INDEP PASS named=[]
GEN FAIL rows=37 wrong=0 [] url_bad=['S9687', 'S6348', 'S3668', 'S4417', 'S9255', 'S9336'] summary_ok=True exit=1
ORDER PASS printed=37 expected=37
BOUND PASS bad=[]
EXIT PASS gen_exit=1 body_exit=0
PRIV PASS exit=1 rows=[('S8249', 'REFUSED', 0), ('S3604', 'REFUSED', 0), ('S9222', 'REFUSED', 0)]
DEFAULT PASS rows=[('S2210', 'UNREACHABLE', 9)] wall=150s hits=9 exit=1
ERR PASS bad=[]
ACCEPT-O-62: FAIL
exit=1
```

## Exact fixture diffs (fixture diffs, not counter diffs)

```diff
--- base/tools/reopen-row.py
+++ c1_attempts5/tools/reopen-row.py
@@ -24,7 +24,7 @@
 import urllib.parse
 import urllib.request

-MAX_ATTEMPTS_PER_URL = 3
+MAX_ATTEMPTS_PER_URL = 5
 DEFAULT_PASSES = 3
 DEFAULT_GAP = 60.0
 REQUEST_TIMEOUT = 30

--- base/tools/reopen-row.py
+++ c2_pass_after_located/tools/reopen-row.py
@@ -320,7 +320,7 @@
             else:
                 pass_verdict = "UNREACHABLE"
         verdicts.append((pass_verdict, pass_url))
-        another = (pass_verdict != "LOCATED") and transient
+        another = transient or pass_verdict == "LOCATED"
         if not another:
             break

--- base/tools/reopen-row.py
+++ c3_pass_after_absent/tools/reopen-row.py
@@ -320,7 +320,7 @@
             else:
                 pass_verdict = "UNREACHABLE"
         verdicts.append((pass_verdict, pass_url))
-        another = (pass_verdict != "LOCATED") and transient
+        another = transient or pass_verdict == "ABSENT"
         if not another:
             break

--- base/tools/reopen-row.py
+++ c4_retry_4xx/tools/reopen-row.py
@@ -289,7 +289,7 @@
                     if attempt + 1 < MAX_ATTEMPTS_PER_URL:
                         time.sleep(min(gap, 5.0))
                     continue
-                if status == 429 or 500 <= status <= 599:
+                if status == 429 or 400 <= status <= 599:
                     transient = True
                     if attempt + 1 < MAX_ATTEMPTS_PER_URL:
                         time.sleep(min(gap, 5.0))

--- base/tools/reopen-row.py
+++ c5_fetch_all_urls/tools/reopen-row.py
@@ -310,8 +310,6 @@
                     pass_verdict = "CAPTION_ONLY"
                     pass_url = url
                 break
-            if pass_verdict == "LOCATED":
-                break
         if pass_verdict is None:
             if answered:
                 pass_verdict = "ABSENT"

--- base/tools/reopen-row.py
+++ c6_attempts10/tools/reopen-row.py
@@ -24,7 +24,7 @@
 import urllib.parse
 import urllib.request

-MAX_ATTEMPTS_PER_URL = 3
+MAX_ATTEMPTS_PER_URL = 10
 DEFAULT_PASSES = 3
 DEFAULT_GAP = 60.0
 REQUEST_TIMEOUT = 30

--- base/tools/reopen-row.py
+++ c7_refetch_after_match/tools/reopen-row.py
@@ -305,7 +305,7 @@
                 if has_run(words(body), quote_words):
                     pass_verdict = "LOCATED"
                     pass_url = url
-                    break
+                    continue
                 if pass_verdict is None and has_run(words(caption), quote_words):
                     pass_verdict = "CAPTION_ONLY"
                     pass_url = url

--- base/tools/reopen-row.py
+++ c8_retry_after_200_nomatch/tools/reopen-row.py
@@ -306,6 +306,8 @@
                     pass_verdict = "LOCATED"
                     pass_url = url
                     break
+                if attempt + 1 < MAX_ATTEMPTS_PER_URL:
+                    continue
                 if pass_verdict is None and has_run(words(caption), quote_words):
                     pass_verdict = "CAPTION_ONLY"
                     pass_url = url

--- base/tools/reopen-row.py
+++ c9_pass_after_caption/tools/reopen-row.py
@@ -320,7 +320,7 @@
             else:
                 pass_verdict = "UNREACHABLE"
         verdicts.append((pass_verdict, pass_url))
-        another = (pass_verdict != "LOCATED") and transient
+        another = transient or pass_verdict == "CAPTION_ONLY"
         if not another:
             break
```

The `c10`, `c11` and `c12` diffs are in `/fast/scratch/hyaku/kotodama-r62/CtlOUnbounded/variants_diffs.txt` family; the generated diff files are `variants_diffs.txt`, `variants_diffs2.txt`, `variants_diffs3.txt`, `probe_counter_diff.txt` and `probe_counter2_diff.txt`.

## Fixture hashes and exact locations

| Fixture | SHA-256 of `tools/reopen-row.py` | Frozen verdict |
|---|---|---|
| `variants/base` | `321648bd2bf7bce428ef46cbadb0802dadd94dffb24f39921ca4791d3f8bfbfd` | PASS |
| `variants/c1_attempts5` | `911ec7f44653c8111c5d2b6c60022e82bfa7f67b6f6f9207f925564bf04230b4` | FAIL |
| `variants/c2_pass_after_located` | `d0dc8b5b3cfbe684b03fe669948c6503c6a42c2ebcdcce85ff64577a62c1c7c7` | FAIL |
| `variants/c3_pass_after_absent` | `bfafa6ba62cdf64edefaac90e8bac6553eb271c07da478678a0855bfd9ca44a8` | FAIL |
| `variants/c4_retry_4xx` | `c642582d4f8b59bdd7203564b49ab7eaf6fc68a22ab77a41671d19c63833e749` | FAIL |
| `variants/c5_fetch_all_urls` | `1dbcc74a07032dadc2fe9d821d690ac8795fe56085b396024c4884d5a8c3da53` | **PASS** |
| `variants/c6_attempts10` | `248a465d701a9ed75cc4f9b2fa84969cd985f41beb916c389967a72868c533db` | FAIL |
| `variants/c7_refetch_after_match` | `db1a650c2aecf97da611c663fa7ad5243195cbbd83f76db67a85a59dafcc4cec` | FAIL |
| `variants/c8_retry_after_200_nomatch` | `03525730ed04dd36670974b1986bddd7231d415bba1401c9f45b5484670e78c1` | FAIL |
| `variants/c9_pass_after_caption` | `9cbf74f651eb5dc12f21e34dcb2c76c6b0eafa13c22a4ade4e3c9846add2aa4f` | FAIL |
| `variants/c10_report_dash_url` | `b5db6e53c4a446ce1fe9b56ab57c5570e0cbde2a4db94c768ec002e5ff7a559c` | **PASS** |
| `variants/c11_aux_url_fetch` | `b1faab53d7d2a974b3be6816e00a2ba354b3c1a327961a598076c54f4dd5ae85` | **PASS** |
| `variants/c12_aux_url_counted` | `145842b926eb44c680896f75ae15be7be948cc90b351ef0f7bffc0f4aebccd9c` | FAIL |

PROBE counters (never the frozen counter): `probe/accept-o-probe.py` `e3710fd35f7b602078ef7f09a903e180610509e910b2f8caace4ba979cf9bf1e`; `probe/accept-o-probe2-url.py` `3062479c388a856064bf8f2d44c4276f14e6c6906dfa82893eed71d475e62bbf`. Frozen counter, unchanged everywhere: `bfd17a300d1cbe523b269f8dc5ceeeb42824ac2ad1dca4ce70f0c7ae55c77551`.

## Risks and what this does not establish

- The over-retry survivors are **counter-coverage** findings, not findings against any lane implementation: `tools/reopen-row.py` does not exist in the lane at the measured revision, and this seat built none. A lane tool that implements the contract as written is unaffected; the risk is that a tool with the `c5` or `c11` shape would be **admitted** by the frozen predicate.
- [INFERENCE] The `c5` shape is the more likely one to arise in practice than the others, because a naive "try every URL in the source cell" loop is the natural implementation of "archived-copy fallback" and differs from the contract only in where it stops. 101 of the 618 registry rows list a capture, so the exposure is not hypothetical.
- The `url=` gap (`c10`) is independent of the retry gaps and would let a tool mis-attribute the located URL on every row regardless of its retry discipline. It also weakens the `c5` detection, because the over-fetching tool's reported `url=` moves to the archive and nothing checks it.
- Neither the frozen counter nor any PROBE was edited; every counter change proposed here is a recommendation, not an applied change. The lane's `claims.json` permits a counter revision only before the counter's first run on the claimed object, so these proposals are time-sensitive: if the L1 has already run `accept-o.py` on a candidate `tools/reopen-row.py`, the c5/c10/c11 coverage gap should be handled by the lane's own review (the claim's `review_only` items) rather than by a counter edit.
- No live network fetch was performed; every measurement is against a local fixture, as the claim requires. Nothing here says anything about the tool's behaviour on real pages (S665 caption, S671 capture) — those remain wave-2 review items.

## Artefact index (all under `/fast/scratch/hyaku/kotodama-r62/CtlOUnbounded/`)

- `base/reopen-row.py` — honest independent implementation used as the mutation baseline (positive calibration).
- `variants/<case>/tools/reopen-row.py` — the twelve fixtures actually scored.
- `make_variants.py`, `make_variants2.py`, `make_variants3.py` — fixture generators; `variants_diffs*.txt` — the exact diffs.
- `make_probe_counter.py`, `make_probe_counter2.py` — PROBE-counter generators; `probe_counter_diff.txt`, `probe_counter2_diff.txt` — the exact PROBE diffs.
- `probe_c5_blindspot.py`, `probe_c11_extra_request.py` — server-side hit probes (not counters).
- `runs/canon_*.out` — the twelve frozen-counter receipts quoted above (stdout + exit); `runs/probe_*.out` — the four PROBE receipts; `runs/probe_c11_extra_request.out` — the hit probe output.
- `clone/`, `wt_*/` — the scratch clone and the ten per-case worktrees at `f0173481`.
