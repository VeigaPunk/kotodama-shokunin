# CtlCHonestHtml — R61 W1 pre-data control: claim C honest positive (HTML pages)

**Item:** honest positive calibration for `ACCEPT-C-61` on a small, real, hand-built fixture — 3 real footwear pages on 3 different hosts, 3 honest SOURCES rows, 3 honest one-clause cited bullets, README index row and footer bump (TOTAL 236). Scored with the frozen counter and with a probe that changes only `FLOOR` (20 → 3).

**Revision:** `78ad4b176695e9fcd490ab607cb8218e2ce62738` (sandbox clones; no git/jj write in the lane or fleet repo).
**Frozen counter sha256:** `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10` (matches the assigned sha).
**Probe sha256:** `71f91748f4e69664038d0dfbf9f80c77875c1cf652a498fea2bf8d3cf7402749`.

## Fixture paths (all under /fast/scratch/hyaku/kotodama-r61/CtlCHonestHtml/)

- `clone/` — pinned-revision clone carrying the honest fixture (only 3 paths differ: `M corpus/README.md`, `M corpus/SOURCES.md`, `?? corpus/knowledge/culture-material/footwear-codes-terminology.md`).
- `accept-c-probe.py` — copy of the frozen counter, one-line change: `FLOOR = 20` → `FLOOR = 3`.
- `clone-stub/` — cheap fixture: same entry + README, `corpus/SOURCES.md` reverted (the three cited ids have no rows) = "sourceless stub citing ids with no rows".
- `clone-base/` — cheap fixture: do-nothing base (corpus reverted, entry removed, 235 files).

Fixture file hashes in `clone/`:

```
c054e00fee36db5fc3bb3a5cd9df2d109391e5c1f75655bc4b94648d2c567118  corpus/knowledge/culture-material/footwear-codes-terminology.md
0ad7e4e45d2bb6386f82ea7eccaf6536fad38c913631bd8bd1282cc43c05bcfc  corpus/README.md
3ada93f25c07e25b9f82e7f3934fb77064b3ef88b7ebcc3f4b923d2ef75cc6ef  corpus/SOURCES.md
0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10  reports/round-61/accept-c.py
```

## What the fixture contains

Three rows appended to `corpus/SOURCES.md` (lines 706–708), 11 cells each, one S-id per row, block S652–S699, `status=mined`, `opened=2026-10-23`, `recheck=2027-04-21` (+180 d), `used-by` exactly `corpus/knowledge/culture-material/footwear-codes-terminology.md`:

- **S652** — V&A object record "Pair of Chopines", T.48&A-1914, Venice ca. 1600, `https://collections.vam.ac.uk/item/O74447/` (live plain GET HTTP 200, 53,550 bytes). Anchor (10 words): "Chopines were based on the shoes worn at Turkish baths." Tier A, docs.
- **S653** — Wikipedia "Clog" (tertiary encyclopedia article), `https://en.wikipedia.org/wiki/Clog` (live plain GET HTTP 200, 238,245 bytes). Anchor (19 words): "Welsh traditional clog maker Trefor Owen identified three main varieties of clogs: wooden upper, wooden soled and overshoes." Tier B, docs.
- **S654** — The Met object record "Chopines", 82448 (1973.114.4a, b), live `https://www.metmuseum.org/art/collection/search/82448` (plain GET via curl: HTTP 429, 34,223 bytes, 2026-10-23) **and the Wayback `id_` capture as the second URL**: `https://web.archive.org/web/20260421020550id_/https://www.metmuseum.org/art/collection/search/82448` (HTTP 200, 169,090 bytes). Anchor (17 words): "The high platform shoes known as chopines came into fashion in Venice in the sixteenth century." Tier A, docs.

New entry `corpus/knowledge/culture-material/footwear-codes-terminology.md` (head block with `- topic:` text byte-identical to the README row, `- sources:`, `- verified-at:`, `- recheck:`), then three bullet lines, exactly one S-id each, no S-id in any heading or table:

```
- Chopines took the shoe worn at Turkish baths as their base [S652].
- Trefor Owen, a Welsh clog maker, identified three main varieties: wooden upper, wooden soled and overshoes [S653].
- The high platform shoes called chopines came into fashion in Venice in the sixteenth century [S654].
```

README: `## culture-material/ (29)` → `(30)`; one index row inserted alphabetically (after `fire-fuel-light.md`) whose text equals the entry's `- topic:` text; `Total knowledge entries: 235.` → `236.`; counts footer `(total 235 files; directory totals 29/29/29/29/24/95)` → `(total 236 files; directory totals 29/29/30/29/24/95)`.

## Independent locator evidence (same locator the counter imports)

```
$ python3 -B reports/round-61/reopen-quote.py 'https://collections.vam.ac.uk/item/O74447/' "Chopines were based on the shoes worn at Turkish baths."
LOCATED https://collections.vam.ac.uk/item/O74447/            exit=0

$ python3 -B reports/round-61/reopen-quote.py 'https://en.wikipedia.org/wiki/Clog' "Welsh traditional clog maker Trefor Owen identified three main varieties of clogs: wooden upper, wooden soled and overshoes."
LOCATED https://en.wikipedia.org/wiki/Clog                    exit=0

$ python3 -B reports/round-61/reopen-quote.py 'https://web.archive.org/web/20260421020550id_/https://www.metmuseum.org/art/collection/search/82448' "The high platform shoes known as chopines came into fashion in Venice in the sixteenth century."
LOCATED https://web.archive.org/web/20260421020550id_/https://www.metmuseum.org/art/collection/search/82448   exit=0

Fabricated-quote negative control on the same V&A URL:
NOT_LOCATED https://collections.vam.ac.uk/item/O74447/ quote-absent   exit=1

Row mode after filing:
$ python3 -B reports/round-61/reopen-quote.py --row S654
LOCATED https://www.metmuseum.org/art/collection/search/82448       exit=0
```

Met-live nuance (recorded because it is the Wayback-row evidence): the live Met object URL answered **HTTP 429 (34,219–34,223 bytes) to curl on every attempt**, while the locator's own urllib GET received **HTTP 200 (194,399 bytes)** and located the quote. The `id_` capture is listed second in the cell and independently LOCATED the same quote (HTTP 200, 169,090 bytes). So the row's access note ("live plain GET, HTTP 429, 34223 bytes") is the measured curl result at opening; the capture is a verified second route, and the frozen LOCATE leg used the live URL under urllib. This is a fetch-path difference (client stack), not a relaxed rule.

No cited URL is reused from below S652 (`FRESH PASS`; a case-insensitive grep for `O74447`, `search/82448`, `wiki/Clog` in SOURCES.md found nothing).

## Probe diff (only constant changed)

```
--- reports/round-61/accept-c.py
+++ /fast/scratch/hyaku/kotodama-r61/CtlCHonestHtml/accept-c-probe.py
@@ -54,7 +54,7 @@
 TOTAL = 236
 FIRST_SID = 652
 LAST_SID = 699
-FLOOR = 20
+FLOOR = 3
 LOCATOR = "reports/round-61/reopen-quote.py"
 SHARE = 1.0
 OPENED = "2026-10-23"
```

`TOTAL`/`BASE_LIST` unchanged: the fixture adds the entry, it does not replace it.

## Run receipts — full stdout

### Honest fixture — frozen counter (`cd clone && python3 -B reports/round-61/accept-c.py`)

```
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=3 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=3 bad=[]
TOPIC PASS rows=3 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

Only `FLOOR` fails (3 < 20). Every other leg passes, including LOCATE share 1.0 on live URLs. **No false FAIL on honest work.**

### Honest fixture — FLOOR=3 probe (`cd clone && python3 -B .../accept-c-probe.py`)

```
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=3 floor=3
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=3 bad=[]
TOPIC PASS rows=3 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

**The probe PASSes on all 14 legs.** Calibration is green; no counter repair is owed before data on this evidence.

### Cheap fixture: sourceless stub (`clone-stub`, entry + README present, the three cited rows absent)

Frozen:

```
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=3 floor=20
RANGE FAIL bad=['S652', 'S653', 'S654'] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=3 bad=[]
TOPIC FAIL rows=0 bad=[]
LINK FAIL min=3 bad=['10:no-row', '11:no-row', '12:no-row']
COPY FAIL max=12 bad=['10:no-row', '11:no-row', '12:no-row']
LOCATE FAIL located=0 cited=3 need=3 at=2026-10-23T09:48Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

Probe:

```
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=3 floor=3
RANGE FAIL bad=['S652', 'S653', 'S654'] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=3 bad=[]
TOPIC FAIL rows=0 bad=[]
LINK FAIL min=3 bad=['10:no-row', '11:no-row', '12:no-row']
COPY FAIL max=12 bad=['10:no-row', '11:no-row', '12:no-row']
LOCATE FAIL located=0 cited=3 need=3 at=2026-10-23T09:47Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Cheap fixture: do-nothing base (`clone-base`, 235 files, corpus reverted)

Frozen:

```
SET FAIL count=235 required=236 added=[] removed=[]
SWEEP FAIL exit=0 rows 235 files 235 missing_from_index 0 []
FLOOR FAIL cited=0 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=0 bad=[]
TOPIC FAIL rows=0 bad=[]
LINK FAIL min=3 bad=[]
COPY FAIL max=12 bad=[]
LOCATE FAIL located=0 cited=0 need=0 at=2026-10-23T09:48Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

Probe:

```
SET FAIL count=235 required=236 added=[] removed=[]
SWEEP FAIL exit=0 rows 235 files 235 missing_from_index 0 []
FLOOR FAIL cited=0 floor=3
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=0 bad=[]
TOPIC FAIL rows=0 bad=[]
LINK FAIL min=3 bad=[]
COPY FAIL max=12 bad=[]
LOCATE FAIL located=0 cited=0 need=0 at=2026-10-23T09:47Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

## Receipt lines

```
RECEIPT CtlCHonestHtml/honest counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS probe-sha256=71f91748f4e69664038d0dfbf9f80c77875c1cf652a498fea2bf8d3cf7402749 stopped-by=frozen:FLOOR;probe:none
RECEIPT CtlCHonestHtml/stub counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL probe-sha256=71f91748f4e69664038d0dfbf9f80c77875c1cf652a498fea2bf8d3cf7402749 stopped-by=frozen:FLOOR,RANGE,TOPIC,LINK,COPY,LOCATE;probe:RANGE,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCHonestHtml/base counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL probe-sha256=71f91748f4e69664038d0dfbf9f80c77875c1cf652a498fea2bf8d3cf7402749 stopped-by=frozen:SET,SWEEP,FLOOR,LINES,TOPIC,LINK,COPY,LOCATE;probe:SET,SWEEP,FLOOR,LINES,TOPIC,LINK,COPY,LOCATE
```

## Verdict

**NONE-MET** — no cheap fixture that skips the claimed work gets PASS under the frozen counter or under the FLOOR-only probe.

- `CtlCHonestHtml/clone-stub` (ids with no rows) fails RANGE/TOPIC/LINK/COPY/LOCATE under both counters.
- `CtlCHonestHtml/clone-base` (do nothing) fails SET/SWEEP/FLOOR/LINES/TOPIC/LINK/COPY/LOCATE under both counters.
- The only PASS is the honest fixture under the declared probe (`FLOOR` lowered to its own 3 rows). That fixture does not skip any mechanical leg: three real rows of 13 cells, three real live-located quotes, one S-id per bullet, mined/opened/used-by satisfied, README sweep exact, FRESH clean. The probe result is the calibration signal, not a gaming path.

## Risks / notes

- **Met live 429 vs locator 200 (fetch-path split).** The cell records the curl-measured 429; the counter's urllib client gets 200 on the same URL and located the quote live. The capture is listed second and independently LOCATED, so the Wayback-row requirement holds, but a future run that hardens the Met edge could flip LOCATE onto the capture — no leg depends on which of the two URLs wins.
- `ACCESS: 2 flagged rows, 0 findings` — the two BYPASS-regex matches are pre-existing registry rows whose status is `rejected`; none of S652–S654 trips the access pattern.
- LOCATE ran fast (~1.3 s for the whole counter) because the three fetches are concurrent and the hosts answered promptly; verified independently by row-mode and by the fabricated-quote negative control (NOT_LOCATED), so the PASS is not a stale/cached result.
- This is a **calibration fixture only**, not the real C entry: 3 rows vs the frozen FLOOR 20. The real wave must satisfy the frozen counter with ≥20 rows, the full 14 legs, and a real (non-fixture) entry body. The `FLOOR=20` constant in the lane counter was not touched; only the scratch copy carries `FLOOR=3`.
- No tool installs or updates were made. Nothing was written in the lane repo or the fleet repo except this report; all fixture bytes live under `/fast/scratch/hyaku/kotodama-r61/CtlCHonestHtml/`.
