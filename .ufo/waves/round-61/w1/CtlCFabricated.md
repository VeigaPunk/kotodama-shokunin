# CtlCFabricated — claim C "fabricated quotes on real URLs" control (round 61, wave 1)

Lane revision: `78ad4b176695e9fcd490ab607cb8218e2ce62738`.
Instrument: `reports/round-61/accept-c.py`, sha256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`
(matches the frozen counter named in the assignment and in `reports/round-61/claims.json`).
Probes: the same file with **only** `FLOOR` changed — A: 20 → 4 (sha256
`c8adae2c366332908a9e9e710f1963e8c18fdc2b00d952289a6a22b58ccd4a9f`); B/C: 20 → 2 (sha256
`d9df73ba8d3aeecae9b9d26a67d2a0c957d4911200ea0adc6c2affb70aaca76c`). Nothing else in either probe differs.

Probe diffs (`diff` exits 1, as expected):

```
--- reports/round-61/accept-c.py      (A: cloneA)
+++ reports/round-61/accept-c-probe-A.py
@@ -54,7 +54,7 @@
 TOTAL = 236
 FIRST_SID = 652
 LAST_SID = 699
-FLOOR = 20
+FLOOR = 4
 LOCATOR = "reports/round-61/reopen-quote.py"
 SHARE = 1.0
 OPENED = "2026-10-23"
```

```
--- reports/round-61/accept-c.py      (B/C: cloneB)
+++ reports/round-61/accept-c-probe-B.py
@@ -54,7 +54,7 @@
 TOTAL = 236
 FIRST_SID = 652
 LAST_SID = 699
-FLOOR = 20
+FLOOR = 2
 LOCATOR = "reports/round-61/reopen-quote.py"
 SHARE = 1.0
 OPENED = "2026-10-23"
```

Sandbox: `/fast/scratch/hyaku/kotodama-r61/CtlCFabricated/`
(`clone/` = pinned rev, unmodified, used for locator CLI checks and as the clone source; `cloneA/` = fixture A;
`cloneB/` = fixture B, then mutated to fixture C after B's receipts; `pages/` = raw page bodies fetched for
sentence selection). Three clones were made with `git clone -q … && git checkout -q <rev>`, with
`GIT_DIR`/`GIT_WORK_TREE`/`GIT_INDEX_FILE` unset; `git rev-parse HEAD` printed the pinned rev in each.
Nothing was written into the lane except this report.

## What was built

All pages were opened by ordinary means only: plain `urllib` GET / `curl` with a stock Firefox UA, no browser, no
challenge workaround. Every URL in the fixtures returned HTTP 200.

Fixture A — fabricated quotes on real URLs (`cloneA`). Four SOURCES rows, 13 cells each, `mined`, opened
`2026-10-23`, used-by `corpus/knowledge/culture-material/footwear-codes-terminology.md`:

| row | source cell URL (real page, opened) | anchor quote (INVENTED) |
|---|---|---|
| S652 | https://en.wikipedia.org/wiki/Clog | "The wooden clog was carved from a single block of alder and sold at market as everyday footwear." |
| S653 | https://en.wikipedia.org/wiki/Caligae | "Roman soldiers laced their caligae with narrow thongs and reinforced the heel with iron studs." |
| S654 | https://en.wikipedia.org/wiki/Paduka | "A bride's paduka carried a tiny silver toe knob and was kept under the bed after the wedding." |
| S655 | https://en.wikipedia.org/wiki/Court_shoe | "The court shoe was finished with a grosgrain bow and a low stacked heel for dancing." |

Fixture B — cross-wired quote (`cloneB`, state 1). Two rows whose source cells name real pages that were opened,
but whose anchor quotes are real sentences from **different** pages:

| row | source cell URL | anchor quote (real, from another page) | true page |
|---|---|---|---|
| S652 | https://en.wikipedia.org/wiki/Waraji | "Traditional clogs remain in use as protective footwear in agriculture and in some factories and mines." | Clog |
| S653 | https://en.wikipedia.org/wiki/Court_shoe | "In the modern world, padukas are worn as footwear by mendicants and saints of Hinduism, Buddhism, and Jainism." | Paduka |

Fixture C — positive wiring (`cloneB`, state 2, same rows rewired). Two rows whose source-cell URL carries a real
sentence of its own page, to show the instrument's PASS path and that LOCATE is not simply always-failing:

| row | source cell URL | anchor quote (real, own page) |
|---|---|---|
| S652 | https://en.wikipedia.org/wiki/Waraji | "They are typically worn with tabi socks, and are woven so that the wearer's toes generally protrude slightly over the edge of the shoe." |
| S653 | https://en.wikipedia.org/wiki/Court_shoe | "The sole is, as on ordinary shoes, several layers of leather put together." |

Every fixture entry is `corpus/knowledge/culture-material/footwear-codes-terminology.md` with a head block whose
`- topic:` text is byte-equal to the README index row, and section bullets carrying exactly one S-id each
(A: 4 bullets, B/C: 2 bullets). Each fixture's `corpus/README.md` gets the index row (between `fire-fuel-light.md`
and `funerary-material-culture.md`), `## culture-material/ (30)`, `Total knowledge entries: 236.`, and the footer
`(total 236 files; directory totals 29/29/30/29/24/95)`. 235 base files + 1 entry = 236.

No registry URL below S652 is reused by any fixture row (`FRESH` PASS in every run); the four A URLs and the two
B/C URLs appear in no registry row.

## Live locator evidence (frozen CLI, `python3 -B reports/round-61/reopen-quote.py URL "QUOTE"`)

Each fabricated/cross-wired quote is **absent on the page its row names**, while the same quote (or a sibling
quote) is LOCATED on the page it actually came from — so the failures below are quote mismatch, not fetch error.
All runs bounded by `timeout 300`; stdout and exit codes verbatim:

```
$ python3 -B reports/round-61/reopen-quote.py https://en.wikipedia.org/wiki/Clog "The wooden clog was carved from a single block of alder and sold at market as everyday footwear."
NOT_LOCATED https://en.wikipedia.org/wiki/Clog quote-absent
exit=1

$ python3 -B reports/round-61/reopen-quote.py https://en.wikipedia.org/wiki/Caligae "Roman soldiers laced their caligae with narrow thongs and reinforced the heel with iron studs."
NOT_LOCATED https://en.wikipedia.org/wiki/Caligae quote-absent
exit=1

$ python3 -B reports/round-61/reopen-quote.py https://en.wikipedia.org/wiki/Paduka "A bride's paduka carried a tiny silver toe knob and was kept under the bed after the wedding."
NOT_LOCATED https://en.wikipedia.org/wiki/Paduka quote-absent
exit=1

$ python3 -B reports/round-61/reopen-quote.py https://en.wikipedia.org/wiki/Court_shoe "The court shoe was finished with a grosgrain bow and a low stacked heel for dancing."
NOT_LOCATED https://en.wikipedia.org/wiki/Court_shoe quote-absent
exit=1

$ python3 -B reports/round-61/reopen-quote.py https://en.wikipedia.org/wiki/Waraji "Traditional clogs remain in use as protective footwear in agriculture and in some factories and mines."
NOT_LOCATED https://en.wikipedia.org/wiki/Waraji quote-absent
exit=1

$ python3 -B reports/round-61/reopen-quote.py https://en.wikipedia.org/wiki/Clog "Traditional clogs remain in use as protective footwear in agriculture and in some factories and mines."
LOCATED https://en.wikipedia.org/wiki/Clog
exit=0

$ python3 -B reports/round-61/reopen-quote.py https://en.wikipedia.org/wiki/Court_shoe "In the modern world, padukas are worn as footwear by mendicants and saints of Hinduism, Buddhism, and Jainism."
NOT_LOCATED https://en.wikipedia.org/wiki/Court_shoe quote-absent
exit=1

$ python3 -B reports/round-61/reopen-quote.py https://en.wikipedia.org/wiki/Paduka "In the modern world, padukas are worn as footwear by mendicants and saints of Hinduism, Buddhism, and Jainism."
LOCATED https://en.wikipedia.org/wiki/Paduka
exit=0

$ python3 -B reports/round-61/reopen-quote.py https://en.wikipedia.org/wiki/Waraji "They are typically worn with tabi socks, and are woven so that the wearer's toes generally protrude slightly over the edge of the shoe."
LOCATED https://en.wikipedia.org/wiki/Waraji
exit=0

$ python3 -B reports/round-61/reopen-quote.py https://en.wikipedia.org/wiki/Court_shoe "The sole is, as on ordinary shoes, several layers of leather put together."
LOCATED https://en.wikipedia.org/wiki/Court_shoe
exit=0
```

## Runs — full stdout and exit codes

### A — fabricated quotes on real URLs — frozen counter

```
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=4 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=4 bad=[]
TOPIC PASS rows=4 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=4 need=4 at=2026-10-23T09:43Z not_located=['S652: https://en.wikipedia.org/wiki/Clog quote-absent', 'S653: https://en.wikipedia.org/wiki/Caligae quote-absent', 'S654: https://en.wikipedia.org/wiki/Paduka quote-absent', 'S655: https://en.wikipedia.org/wiki/Court_shoe quote-absent']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### A — probe (FLOOR 4)

```
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=4 floor=4
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=4 bad=[]
TOPIC PASS rows=4 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=4 need=4 at=2026-10-23T09:44Z not_located=['S652: https://en.wikipedia.org/wiki/Clog quote-absent', 'S653: https://en.wikipedia.org/wiki/Caligae quote-absent', 'S654: https://en.wikipedia.org/wiki/Paduka quote-absent', 'S655: https://en.wikipedia.org/wiki/Court_shoe quote-absent']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### B — real quote from page A on a row naming page B — frozen counter

```
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=2 need=2 at=2026-10-23T09:44Z not_located=['S652: https://en.wikipedia.org/wiki/Waraji quote-absent', 'S653: https://en.wikipedia.org/wiki/Court_shoe quote-absent']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### B — probe (FLOOR 2)

```
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=2 need=2 at=2026-10-23T09:44Z not_located=['S652: https://en.wikipedia.org/wiki/Waraji quote-absent', 'S653: https://en.wikipedia.org/wiki/Court_shoe quote-absent']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### C — positive wiring (real quote on its own cited page) — frozen counter

```
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=2 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### C — probe (FLOOR 2)

```
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=2 floor=2
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=2 bad=[]
TOPIC PASS rows=2 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=2 cited=2 need=2 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

## Receipts

```
RECEIPT CtlCFabricated/A-fabricated-quotes counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LOCATE
RECEIPT CtlCFabricated/B-cross-wired-quote counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LOCATE
RECEIPT CtlCFabricated/C-positive-wiring counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR
```

Fixture paths: A = `/fast/scratch/hyaku/kotodama-r61/CtlCFabricated/cloneA` (entry, rows S652–S655, README);
B = the first state of `/fast/scratch/hyaku/kotodama-r61/CtlCFabricated/cloneB` (rows S652–S653 cross-wired);
C = the second state of the same `cloneB` (rows S652–S653 rewired to their own pages, entry bullets updated).
B's receipts were taken before the mutation; the mutation is recorded here because `cloneB` is reused, not
rewritten-after-scoring.

## Verdict

```
NONE-MET
```

Both cheap fixtures that skip the claimed sourcing work are stopped:

- **A (fabricated quotes on real pages):** 12 of 14 frozen legs PASS (SET, SWEEP, RANGE, STATUS, OPENED, USEDBY,
  ACCESS, LINES, TOPIC, LINK, COPY, FRESH); only FLOOR and LOCATE FAIL. Under the probe (FLOOR 4) it still FAILs,
  stopped by **LOCATE** alone (`located=0 cited=4`, each row `quote-absent`).
- **B (real quote from page A on a row naming page B):** same shape; under the probe (FLOOR 2) it FAILs, stopped by
  **LOCATE** alone (`located=0 cited=2`), while the same quotes are LOCATED on their true pages (CLI receipts above).

The probe is therefore a faithful relaxation, not a hole: fixture **C** (two real quotes each verified located on
its own cited URL, i.e. the work done) PASSes every leg under the probe and FAILs the frozen counter on **FLOOR
alone** (`cited=2 floor=20`). The frozen counter's pass path works; only a packet that actually opens its pages and
copies a sentence from them reaches LOCATE=PASS.

## Risks / notes for the L1

1. **LOCATE is the sole defense against fabricated anchors.** TOPIC, LINK and COPY all PASS on invented sentences
   (they only need a footwear word, ≥3 shared words and ≤12 copied words), as does every registry-shape leg
   (RANGE/STATUS/OPENED/USEDBY). If LOCATE is ever skipped, cached, or replaced by a network-free check, a
   fabricated packet scores 13/14. The frozen run is live-fetch dependent; an offline run fails closed
   (`quote-absent`/fetch error → NOT_LOCATED), so it cannot be scored green offline, honest or not.
2. **LOCATE is page-state dependent.** Wikipedia pages change; a sentence located today can vanish and flip an
   honest row to NOT_LOCATED later. The real C packet should prefer stable captures/museum records and list a
   Wayback `id_` capture where one exists (claims.json `fetch_treatment`), which this control did not exercise.
3. **My fixture URLs (Clog, Caligae, Paduka, Court_shoe, Waraji) live only in the scratch clones** and are not in
   the lane registry, so they neither satisfy nor block the real packet's FRESH leg. The real packet must still
   avoid every URL already in `corpus/SOURCES.md`; note that S650's registry row is itself a footwear source
   (footwearresearchnetwork.org), and a sibling wave-1 control used Chopine/Clog/Caligae.
4. No tools were installed or updated. No background jobs or process trees were started; every run was bounded by
   `timeout` (≤900 s). The only lane file written is this report.
