# CtlFetchRule59 — FETCH-59 and focused counter mutations

Axes: fetch-rule conformance; detector sensitivity; no-reader resistance; exact restoration/isolation.

Declaration: `1b80ee41f544d17c0410733a47a3eecac01bf25e`; claim base: `39c9ce8a6be5e5625d8befb54df53d621a3a7929`. All execution was in `/fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/clone`. No source or counter was changed in the lane. No tools were installed or updated.

Results: **one direct, unchanged-counter no-reader control MEETS-COUNTER; all five assigned mutants are KILLED by this wave's focused fixtures; no surviving mutant within that detector.** Concurrent cache and HTTP-501 docstring probes fail already on pristine bytes and are reported separately, not counted as mutant kills.

## Reproduction and fixture boundary

```sh
timeout 60 mkdir -p /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59
timeout 180 env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE git clone --quiet /home/vgpnk/Projects/shokunin/kotodama-shokunin /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/clone
timeout 60 git -C /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/clone checkout --quiet 1b80ee41f544d17c0410733a47a3eecac01bf25e
```

Fixture/evidence copies: `.ufo/waves/round-59/control/CtlFetchRule59/` (197662 bytes total, below 200 KB). Copy the seven Python files beside the scratch `clone/`; launch from that clone root. Every harness starts its `http.server` child under `timeout 850` and kills/waits it in `finally`. Counters are invoked under `timeout 900`.

There are two deliberately separate mechanisms:
- **Direct controls:** 20 real loopback listeners, one physical host/process, ordinary urllib GETs; the exact `reports/round-59/accept-c.py` CLI runs with no monkeypatch, no import driver, no transport shim, and original instrument hashes.
- **Deterministic FETCH/mutation fixtures:** the source URLs are synthetic `*.fixture.test` live URLs and correctly shaped `web.archive.org` capture URLs. A shim at `urllib.request.urlopen` maps only these synthetic requests to loopback `http.server`, preserving/logging the canonical URL in a request header. Cache, locator, retries, root derivation, TOPIC and SUPPORT execute their frozen code. These synthetic captures are NOT claimed to exist on the public Wayback service. Public probes below have no shim.

Synthetic corpus/README/SOURCES/support payloads are temporary. Fixture setup generates matching planted/key hash files; these are explicitly fixture-controlled, not real pre-dispatch commitments. This exposes the distinction between the counter's actual file checks and the declared trusted-dispatch/commit-time prerequisites.

## Direct frozen-counter controls

The no-reader payload is 20 variations of one invented sentence and one teaches sentence, served locally, not sourced learning. Two invented registry members have role `reviewer` and nonempty agentIds `synthetic-not-an-agent-FixtureA59`/`...FixtureB59`. No reviewer was dispatched. Their reports explicitly say they are synthetic/no-reader. They support P01–P20 and reject the known P21 plant. The two packet/key SHA files are self-generated fixture inputs.

Each source is `http://127.0.0.1:<different-port>/leaf`; therefore DISTINCT reports 20 “hosts” even though every request goes to the same IP. Each direct run logged exactly 40 URLs (20 leaves, 20 roots), each with one GET.

Harness command (actual invocation):

```sh
timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/direct_controls59.py --phase pristine
```

CONTROL local-no-reader-MEETS-COUNTER | claim C | exit 0 | ACCEPT-C-59: PASS | failing legs: []

Command from clone root, with the harness's `positive` fixture prepared:

```sh
timeout 900 /usr/bin/python3 -B reports/round-59/accept-c.py
```

```text
SET PASS count=235 required=235 added=['corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'] removed=[]
SWEEP PASS exit=0 rows 235 files 235 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE PASS passing=20 cited=20 at=2026-10-23T02:54Z failing=[]
BOILER PASS passing=20 cited=20 at=2026-10-23T02:54Z failing=[]
RELEVANCE PASS passing=20 cited=20 at=2026-10-23T02:54Z failing=[]
TOPIC PASS passing=20 cited=20 at=2026-10-23T02:54Z failing=[]
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT PASS shared=[] hosts=20 need=10
SUPPORT PASS unsupported=[] qualified_seats=['FixtureA59', 'FixtureB59'] need_seats=2 planted=['FixtureA59:Q1', 'FixtureB59:Q1']
ACCEPT-C-59: PASS
```

CONTROL rubber-stamp-MEETS-MECHANICAL | claim C | exit 1 | ACCEPT-C-59: FAIL | failing legs: [SUPPORT]

Command from clone root, with the harness's `rubber-stamp` fixture prepared:

```sh
timeout 900 /usr/bin/python3 -B reports/round-59/accept-c.py
```

```text
SET PASS count=235 required=235 added=['corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'] removed=[]
SWEEP PASS exit=0 rows 235 files 235 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE PASS passing=20 cited=20 at=2026-10-23T02:54Z failing=[]
BOILER PASS passing=20 cited=20 at=2026-10-23T02:54Z failing=[]
RELEVANCE PASS passing=20 cited=20 at=2026-10-23T02:54Z failing=[]
TOPIC PASS passing=20 cited=20 at=2026-10-23T02:54Z failing=[]
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT PASS shared=[] hosts=20 need=10
SUPPORT FAIL unsupported=['S600:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S601:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S602:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S603:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S604:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S605:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S606:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S607:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S608:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S609:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S610:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S611:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S612:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S613:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S614:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S615:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S616:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S617:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S618:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59', 'S619:SUPPORTED/FixtureA59,SUPPORTED/FixtureB59'] qualified_seats=[] need_seats=2 planted=['FixtureA59:X1', 'FixtureB59:X1']
ACCEPT-C-59: FAIL
```

MEETS-MECHANICAL. SUPPORT did **not** fail merely for a missing registry/key: both files and both matching hashes were supplied; both seats support P21, so neither is qualified.

CONTROL wrong-quote-MEETS-MECHANICAL | claim C | exit 1 | ACCEPT-C-59: FAIL | failing legs: [SUPPORT]

Command from clone root, with the harness's `wrong-quote` fixture prepared:

```sh
timeout 900 /usr/bin/python3 -B reports/round-59/accept-c.py
```

```text
SET PASS count=235 required=235 added=['corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'] removed=[]
SWEEP PASS exit=0 rows 235 files 235 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE PASS passing=20 cited=20 at=2026-10-23T02:54Z failing=[]
BOILER PASS passing=20 cited=20 at=2026-10-23T02:54Z failing=[]
RELEVANCE PASS passing=20 cited=20 at=2026-10-23T02:54Z failing=[]
TOPIC PASS passing=20 cited=20 at=2026-10-23T02:54Z failing=[]
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT PASS shared=[] hosts=20 need=10
SUPPORT FAIL unsupported=['S600:no verdict', 'S601:no verdict', 'S602:no verdict', 'S603:no verdict', 'S604:no verdict', 'S605:no verdict', 'S606:no verdict', 'S607:no verdict', 'S608:no verdict', 'S609:no verdict', 'S610:no verdict', 'S611:no verdict', 'S612:no verdict', 'S613:no verdict', 'S614:no verdict', 'S615:no verdict', 'S616:no verdict', 'S617:no verdict', 'S618:no verdict', 'S619:no verdict'] qualified_seats=[] need_seats=2 planted=['FixtureA59:Q1', 'FixtureB59:Q1']
ACCEPT-C-59: FAIL
```

MEETS-MECHANICAL. SUPPORT did **not** fail merely for a missing registry/key: both files and both matching hashes were supplied; packet quotes differ from landed anchors, so no verdict counts.

CONTROL all-false-MEETS-MECHANICAL | claim C | exit 1 | ACCEPT-C-59: FAIL | failing legs: [SUPPORT]

Command from clone root, with the harness's `all-false` fixture prepared:

```sh
timeout 900 /usr/bin/python3 -B reports/round-59/accept-c.py
```

```text
SET PASS count=235 required=235 added=['corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'] removed=[]
SWEEP PASS exit=0 rows 235 files 235 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE PASS passing=20 cited=20 at=2026-10-23T02:54Z failing=[]
BOILER PASS passing=20 cited=20 at=2026-10-23T02:54Z failing=[]
RELEVANCE PASS passing=20 cited=20 at=2026-10-23T02:54Z failing=[]
TOPIC PASS passing=20 cited=20 at=2026-10-23T02:54Z failing=[]
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT PASS shared=[] hosts=20 need=10
SUPPORT FAIL unsupported=['S600:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S601:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S602:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S603:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S604:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S605:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S606:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S607:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S608:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S609:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S610:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S611:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S612:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S613:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S614:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S615:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S616:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S617:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S618:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59', 'S619:NOT-SUPPORTED/FixtureA59,NOT-SUPPORTED/FixtureB59'] qualified_seats=['FixtureA59', 'FixtureB59'] need_seats=2 planted=['FixtureA59:Q1', 'FixtureB59:Q1']
ACCEPT-C-59: FAIL
```

MEETS-MECHANICAL. SUPPORT did **not** fail merely for a missing registry/key: both files and both matching hashes were supplied; both seats explicitly reject every real row.

These receipts show actual counter acceptance, not genuine research or authenticated reviewers. The positive control also depends on the counter accepting self-written hash commitments; it does not establish that a control could replace an independently protected, already-frozen commitment.

## Deterministic FETCH-59 probes

```sh
timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/fetch59_probe.py --phase pristine
```

```text
PROBE live-403-listed-capture detector=PASS legs={"BOILER": true, "LOCATE": true, "RELEVANCE": true, "TOPIC": true} GET_counts={"http://deny403.fixture.test/leaf": 1, "https://web.archive.org/web/20240102030405/http://deny403.fixture.test/": 1, "https://web.archive.org/web/20240102030405id_/http://deny403.fixture.test/leaf": 1}
PROBE live-404-listed-capture detector=PASS legs={"BOILER": true, "LOCATE": true, "RELEVANCE": true, "TOPIC": true} GET_counts={"http://deny404.fixture.test/leaf": 1, "https://web.archive.org/web/20240102030405/http://deny404.fixture.test/": 1, "https://web.archive.org/web/20240102030405id_/http://deny404.fixture.test/leaf": 1}
PROBE live-403-no-capture detector=PASS legs={"BOILER": false, "LOCATE": false, "RELEVANCE": true, "TOPIC": false} GET_counts={"http://deny403.fixture.test/leaf": 1}
PROBE root-403-page-200-default-capture detector=PASS legs={"BOILER": true, "LOCATE": true, "RELEVANCE": true, "TOPIC": true} GET_counts={"http://root403.fixture.test/": 1, "http://root403.fixture.test/leaf": 1, "https://web.archive.org/web/2026id_/http://root403.fixture.test/": 1}
PROBE root-403-page-200-listed-timestamp detector=PASS legs={"BOILER": true, "LOCATE": true, "RELEVANCE": true, "TOPIC": true} GET_counts={"http://root403.fixture.test/": 1, "http://root403.fixture.test/leaf": 1, "https://web.archive.org/web/20240102030405id_/http://root403.fixture.test/": 1}
PROBE both-roots-fail detector=PASS legs={"BOILER": false, "LOCATE": true, "RELEVANCE": true, "TOPIC": true} GET_counts={"http://rootsfail.fixture.test/": 1, "http://rootsfail.fixture.test/leaf": 1, "https://web.archive.org/web/2026id_/http://rootsfail.fixture.test/": 1}
PROBE one-fetch-reused-across-legs-and-rows detector=PASS legs={"BOILER": true, "LOCATE": true, "RELEVANCE": true, "TOPIC": true} GET_counts={"http://reuse.fixture.test/": 1, "http://reuse.fixture.test/leaf": 1}
PROBE transient-429-then-200 detector=PASS legs={"BOILER": true, "LOCATE": true, "RELEVANCE": true, "TOPIC": true} GET_counts={"http://transient429.fixture.test/": 1, "http://transient429.fixture.test/leaf": 2}
PROBE persistent-429-error-reused detector=PASS legs={"BOILER": false, "LOCATE": false, "RELEVANCE": true, "TOPIC": false} GET_counts={"http://always429.fixture.test/leaf": 3}
PROBE topic-window-negative detector=PASS legs={"BOILER": true, "LOCATE": true, "RELEVANCE": true, "TOPIC": false} GET_counts={"http://topicgap.fixture.test/": 1, "http://topicgap.fixture.test/leaf": 1}
PROBE concurrent-one-fetch-contract detector=FAIL legs={"BOILER": true, "LOCATE": true, "RELEVANCE": true, "TOPIC": true} GET_counts={"http://race.fixture.test/": 2, "http://race.fixture.test/leaf": 2}
PROBE transient-501-docstring-contract detector=FAIL legs={"BOILER": false, "LOCATE": false, "RELEVANCE": true, "TOPIC": false} GET_counts={"http://transient501.fixture.test/leaf": 1}
FETCH59-DETECTOR: PASS
```

Interpretation:
- Live 403 plus the listed capture: LOCATE/BOILER/RELEVANCE/TOPIC PASS via that capture. Live and capture each receive one GET; BOILER fetches its derived archive root once.
- Live 403 without a capture: LOCATE/BOILER/TOPIC FAIL, including the second attempted row check; the failed URL is fetched only once.
- Live 404 plus the listed capture: all four legs PASS via the capture; 404 is not treated as a pass itself.
- Page 200/root 403: BOILER PASS using the capture root. Both the default `2026id_` path and the row's listed 14-digit timestamp are exercised. The listed article capture is not unnecessarily fetched when live LOCATE already succeeds.
- Both live root and capture root fail: BOILER FAIL; LOCATE and TOPIC remain PASS.
- Reuse: two full checks, including LOCATE/BOILER/TOPIC, yield one leaf GET and one root GET for the whole run.
- Transient 429 then 200: PASS with two leaf GET attempts, one root GET, and no new GET on the repeated check. FETCH-59 permits retries within one logical fetch; “one fetch” cannot mean literally one physical GET for this case.
- Persistent 429: FAIL after exactly three attempts; the repeated check reuses the cached error.
- TOPIC distance-negative: quote has a CHARM/stone and GUARD/protective separated by ten word positions; normal WINDOW=3 rejects it, despite an otherwise on-topic page.

Actual server log (the required fetch cases plus the two contract failures; full logs are copied with the fixtures):

```jsonl
{"run": "live-403-listed-capture", "method": "GET", "url": "http://deny403.fixture.test/leaf", "status": 403, "attempt": 1, "archive_timestamp": null}
{"run": "live-403-listed-capture", "method": "GET", "url": "https://web.archive.org/web/20240102030405id_/http://deny403.fixture.test/leaf", "status": 200, "attempt": 1, "archive_timestamp": "20240102030405"}
{"run": "live-403-listed-capture", "method": "GET", "url": "https://web.archive.org/web/20240102030405/http://deny403.fixture.test/", "status": 200, "attempt": 1, "archive_timestamp": "20240102030405"}
{"run": "live-404-listed-capture", "method": "GET", "url": "http://deny404.fixture.test/leaf", "status": 404, "attempt": 1, "archive_timestamp": null}
{"run": "live-404-listed-capture", "method": "GET", "url": "https://web.archive.org/web/20240102030405id_/http://deny404.fixture.test/leaf", "status": 200, "attempt": 1, "archive_timestamp": "20240102030405"}
{"run": "live-404-listed-capture", "method": "GET", "url": "https://web.archive.org/web/20240102030405/http://deny404.fixture.test/", "status": 200, "attempt": 1, "archive_timestamp": "20240102030405"}
{"run": "live-403-no-capture", "method": "GET", "url": "http://deny403.fixture.test/leaf", "status": 403, "attempt": 1, "archive_timestamp": null}
{"run": "root-403-page-200-default-capture", "method": "GET", "url": "http://root403.fixture.test/leaf", "status": 200, "attempt": 1, "archive_timestamp": null}
{"run": "root-403-page-200-default-capture", "method": "GET", "url": "http://root403.fixture.test/", "status": 403, "attempt": 1, "archive_timestamp": null}
{"run": "root-403-page-200-default-capture", "method": "GET", "url": "https://web.archive.org/web/2026id_/http://root403.fixture.test/", "status": 200, "attempt": 1, "archive_timestamp": "2026"}
{"run": "root-403-page-200-listed-timestamp", "method": "GET", "url": "http://root403.fixture.test/leaf", "status": 200, "attempt": 1, "archive_timestamp": null}
{"run": "root-403-page-200-listed-timestamp", "method": "GET", "url": "http://root403.fixture.test/", "status": 403, "attempt": 1, "archive_timestamp": null}
{"run": "root-403-page-200-listed-timestamp", "method": "GET", "url": "https://web.archive.org/web/20240102030405id_/http://root403.fixture.test/", "status": 200, "attempt": 1, "archive_timestamp": "20240102030405"}
{"run": "both-roots-fail", "method": "GET", "url": "http://rootsfail.fixture.test/leaf", "status": 200, "attempt": 1, "archive_timestamp": null}
{"run": "both-roots-fail", "method": "GET", "url": "http://rootsfail.fixture.test/", "status": 403, "attempt": 1, "archive_timestamp": null}
{"run": "both-roots-fail", "method": "GET", "url": "https://web.archive.org/web/2026id_/http://rootsfail.fixture.test/", "status": 403, "attempt": 1, "archive_timestamp": "2026"}
{"run": "one-fetch-reused-across-legs-and-rows", "method": "GET", "url": "http://reuse.fixture.test/leaf", "status": 200, "attempt": 1, "archive_timestamp": null}
{"run": "one-fetch-reused-across-legs-and-rows", "method": "GET", "url": "http://reuse.fixture.test/", "status": 200, "attempt": 1, "archive_timestamp": null}
{"run": "transient-429-then-200", "method": "GET", "url": "http://transient429.fixture.test/leaf", "status": 429, "attempt": 1, "archive_timestamp": null}
{"run": "transient-429-then-200", "method": "GET", "url": "http://transient429.fixture.test/leaf", "status": 200, "attempt": 2, "archive_timestamp": null}
{"run": "transient-429-then-200", "method": "GET", "url": "http://transient429.fixture.test/", "status": 200, "attempt": 1, "archive_timestamp": null}
{"run": "persistent-429-error-reused", "method": "GET", "url": "http://always429.fixture.test/leaf", "status": 429, "attempt": 1, "archive_timestamp": null}
{"run": "persistent-429-error-reused", "method": "GET", "url": "http://always429.fixture.test/leaf", "status": 429, "attempt": 2, "archive_timestamp": null}
{"run": "persistent-429-error-reused", "method": "GET", "url": "http://always429.fixture.test/leaf", "status": 429, "attempt": 3, "archive_timestamp": null}
{"run": "concurrent-one-fetch-contract", "method": "GET", "url": "http://race.fixture.test/leaf", "status": 200, "attempt": 1, "archive_timestamp": null}
{"run": "concurrent-one-fetch-contract", "method": "GET", "url": "http://race.fixture.test/leaf", "status": 200, "attempt": 2, "archive_timestamp": null}
{"run": "concurrent-one-fetch-contract", "method": "GET", "url": "http://race.fixture.test/", "status": 200, "attempt": 1, "archive_timestamp": null}
{"run": "concurrent-one-fetch-contract", "method": "GET", "url": "http://race.fixture.test/", "status": 200, "attempt": 2, "archive_timestamp": null}
{"run": "transient-501-docstring-contract", "method": "GET", "url": "http://transient501.fixture.test/leaf", "status": 501, "attempt": 1, "archive_timestamp": null}
```

### Two observed pristine contract failures (not killed mutants)

```json
{
  "probe": "concurrent-one-fetch-contract",
  "expected_counts": {
    "http://race.fixture.test/leaf": 1,
    "http://race.fixture.test/": 1
  },
  "actual_counts": {
    "http://race.fixture.test/leaf": 2,
    "http://race.fixture.test/": 2
  },
  "details": {
    "LOCATE": [
      true,
      "http://race.fixture.test/leaf"
    ],
    "BOILER": [
      true,
      "root-clear http://race.fixture.test/; not a title, h1 or meta label"
    ],
    "RELEVANCE": [
      true,
      "shared=['amule', 'cerem', 'charm', 'house', 'prote']"
    ],
    "TOPIC": [
      true,
      "quote_hits=2 function_words=5 page_hits=6 page_terms=5 need=1/2/3/2"
    ]
  }
}
```

```json
{
  "probe": "transient-501-docstring-contract",
  "expected_counts": {
    "http://transient501.fixture.test/leaf": 2,
    "http://transient501.fixture.test/": 1
  },
  "actual_counts": {
    "http://transient501.fixture.test/leaf": 1
  },
  "details": {
    "LOCATE": [
      false,
      "http://transient501.fixture.test/leaf HTTPError"
    ],
    "BOILER": [
      false,
      "not-located"
    ],
    "RELEVANCE": [
      true,
      "shared=['amule', 'cerem', 'charm', 'house', 'prote']"
    ],
    "TOPIC": [
      false,
      "quote_hits=2 not-located"
    ]
  }
}
```

The concurrent fixture launches two simultaneous checks with a barrier and delays server responses 250 ms. It records **2 leaf GETs and 2 root GETs**; all four legs still PASS. `_CACHE_LOCK` protects dictionary access but not the fetch-in-progress interval.

The 501 fixture serves 501 on the first request and 200 on the next request if made. The locator makes only one GET, caches HTTPError, and both checks fail. The docstring says 429/5xx/508; the retry tuple omits 501 (and other 5xx statuses).

These two observations are excluded from the mutation detector's pass/fail aggregate precisely because their pristine baseline already fails. They are pre-existing conformance findings, not evidence of a killed mutant. Every targeted mutation assertion below passes pristine and restored bytes.

## Ordinary public URLs (no local transport substitution)

Commands and observed GET output:

```sh
timeout 880 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/public_fetch59.py
timeout 880 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/public_fetch59.py --only teara
```

```jsonl
{"case": "real-met-listed", "urls": ["https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu", "https://web.archive.org/web/20171121161933id_/https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu"], "quote": "Amulets with images of his full body or, more often, just his head, were common in the early first millennium B.C.", "LOCATE": [true, "https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu"], "BOILER": [true, "root-clear https://www.metmuseum.org/; not a title, h1 or meta label"], "repeat_LOCATE": [true, "https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu"], "cache_entries": 2, "GETs": [{"case": "real-met-listed", "url": "https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu", "status": 200, "content_type": "text/html; charset=utf-8"}, {"case": "real-met-listed", "url": "https://www.metmuseum.org/", "status": 200, "content_type": "text/html; charset=utf-8"}]}
{"case": "real-met-unlisted", "urls": ["https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu"], "quote": "Amulets with images of his full body or, more often, just his head, were common in the early first millennium B.C.", "LOCATE": [true, "https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu"], "BOILER": [true, "root-clear https://www.metmuseum.org/; not a title, h1 or meta label"], "repeat_LOCATE": [true, "https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu"], "cache_entries": 2, "GETs": [{"case": "real-met-unlisted", "url": "https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu", "status": 200, "content_type": "text/html; charset=utf-8"}, {"case": "real-met-unlisted", "url": "https://www.metmuseum.org/", "status": 200, "content_type": "text/html; charset=utf-8"}]}
{"case": "real-met-object-listed", "urls": ["https://www.metmuseum.org/art/collection/search/312342", "https://web.archive.org/web/20230529091312id_/https://www.metmuseum.org/art/collection/search/312342"], "quote": "may relate to a wide spectrum of physical receptacles, including cloth packets, filled vessels", "LOCATE": [true, "https://www.metmuseum.org/art/collection/search/312342"], "BOILER": [true, "root-clear https://www.metmuseum.org/; not a title, h1 or meta label"], "repeat_LOCATE": [true, "https://www.metmuseum.org/art/collection/search/312342"], "cache_entries": 2, "GETs": [{"case": "real-met-object-listed", "url": "https://www.metmuseum.org/art/collection/search/312342", "status": 200, "content_type": "text/html; charset=utf-8"}, {"case": "real-met-object-listed", "url": "https://www.metmuseum.org/", "status": 200, "content_type": "text/html; charset=utf-8"}]}
{"case": "real-nt-page-root", "urls": ["https://environment.nt.gov.au/boards-committees/place-names-committee/guidelines"], "quote": "Aboriginal names for geographic or topographic features are preferred", "LOCATE": [true, "https://environment.nt.gov.au/boards-committees/place-names-committee/guidelines"], "BOILER": [true, "root-clear https://environment.nt.gov.au/; not a title, h1 or meta label"], "repeat_LOCATE": [true, "https://environment.nt.gov.au/boards-committees/place-names-committee/guidelines"], "cache_entries": 2, "GETs": [{"case": "real-nt-page-root", "url": "https://environment.nt.gov.au/boards-committees/place-names-committee/guidelines", "status": 200, "content_type": "text/html; charset=utf-8"}, {"case": "real-nt-page-root", "url": "https://environment.nt.gov.au/", "status": 200, "content_type": "text/html; charset=utf-8"}]}
{"case": "real-public-404", "urls": ["https://example.com/fetch59-missing-immutable-control"], "quote": "The amulet was carried by the household as a protective charm during ceremony number 0.", "LOCATE": [false, "https://example.com/fetch59-missing-immutable-control HTTPError"], "BOILER": [false, "not-located"], "repeat_LOCATE": [false, "https://example.com/fetch59-missing-immutable-control HTTPError"], "cache_entries": 1, "GETs": [{"case": "real-public-404", "url": "https://example.com/fetch59-missing-immutable-control", "status": 404, "error": "HTTPError"}]}
PUBLIC-FETCH-59: OBSERVED

{"case": "real-teara-403-listed", "urls": ["https://teara.govt.nz/en/taniwha/print", "https://web.archive.org/web/20260208222348id_/https://teara.govt.nz/en/taniwha/print"], "quote": "They hid in lairs known as rua taniwha, which could be deep pools, caves, or dangerous waterways – areas that people avoided.", "LOCATE": [true, "https://web.archive.org/web/20260208222348id_/https://teara.govt.nz/en/taniwha/print"], "BOILER": [false, "root-unfetchable https://web.archive.org/web/20260208222348/https://teara.govt.nz/ URLError"], "repeat_LOCATE": [true, "https://web.archive.org/web/20260208222348id_/https://teara.govt.nz/en/taniwha/print"], "cache_entries": 3, "GETs": [{"case": "real-teara-403-listed", "url": "https://teara.govt.nz/en/taniwha/print", "status": 403, "error": "HTTPError"}, {"case": "real-teara-403-listed", "url": "https://web.archive.org/web/20260208222348id_/https://teara.govt.nz/en/taniwha/print", "status": 200, "content_type": "text/html; charset=UTF-8"}, {"case": "real-teara-403-listed", "url": "https://web.archive.org/web/20260208222348/https://teara.govt.nz/", "status": 429, "error": "HTTPError"}, {"case": "real-teara-403-listed", "url": "https://web.archive.org/web/20260208222348/https://teara.govt.nz/", "status": 429, "error": "HTTPError"}, {"case": "real-teara-403-listed", "url": "https://web.archive.org/web/20260208222348/https://teara.govt.nz/", "status": null, "error": "URLError"}]}
{"case": "real-teara-403-unlisted", "urls": ["https://teara.govt.nz/en/taniwha/print"], "quote": "They hid in lairs known as rua taniwha, which could be deep pools, caves, or dangerous waterways – areas that people avoided.", "LOCATE": [false, "https://teara.govt.nz/en/taniwha/print HTTPError"], "BOILER": [false, "not-located"], "repeat_LOCATE": [false, "https://teara.govt.nz/en/taniwha/print HTTPError"], "cache_entries": 1, "GETs": [{"case": "real-teara-403-unlisted", "url": "https://teara.govt.nz/en/taniwha/print", "status": 403, "error": "HTTPError"}]}
PUBLIC-FETCH-59: OBSERVED
```

The Met and NT pages/roots currently returned 200; their historical 403/429 markers were not assumed to remain true. Their repeated LOCATE calls made no additional GETs. The real missing example.com page returned 404 and failed, with its error reused.

The real Te Ara live page returned **403**. With its listed ordinary capture (`20260208222348id_`) it returned 200 and **LOCATE PASS**; without the capture it was **LOCATE FAIL**. The archived root then returned 429 twice and raised URLError on the final attempt, so **BOILER FAIL** for that real captured row. Thus a locating article capture does not by itself guarantee row acceptance; the root rule still applies. This public quote is a FETCH diagnostic, not a proposed amulet source.

Additional ordinary curl GETs:

```sh
timeout 140 curl --location --max-time 130 --silent --show-error --dump-header /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/real-archive-met.headers --output /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/real-archive-met.html --write-out 'ARCHIVE-MET HTTP %{http_code} bytes %{size_download}\n' https://web.archive.org/web/20171121161933id_/https://www.metmuseum.org/exhibitions/listings/2014/assyria-to-iberia/blog/posts/pazuzu
# stdout: ARCHIVE-MET HTTP 200 bytes 90034
timeout 140 curl --location --max-time 130 --silent --show-error --dump-header /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/real-teara.headers --output /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/real-teara.html --write-out 'LIVE-TEARA HTTP %{http_code} bytes %{size_download}\n' https://teara.govt.nz/en/taniwha/print
# stdout: LIVE-TEARA HTTP 403 bytes 5462
timeout 140 curl --location --max-time 130 --silent --show-error --dump-header /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/real-teara-capture.headers --output /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/real-teara-capture.html --write-out 'CAPTURE-TEARA HTTP %{http_code} bytes %{size_download}\n' https://web.archive.org/web/20260208222348id_/https://teara.govt.nz/en/taniwha/print
# stdout: CAPTURE-TEARA HTTP 200 bytes 44005
```

No challenge, captcha, login or paywall was passed. No failing public request was rerun merely to confirm its failure; listed captures are separate ordinary URLs.

## Five isolated one-point mutants

Each mutant was applied only to the scratch counter and reversed before the next. The detector file/behavior is the same across pristine, mutated and restored runs; `--phase` only selects artifact names. Initial pristine exited 0; each mutant exited 1; each exact restoration exited 0. The negative controls are expected rejections, so their baseline ACCEPT-C failure is a successful detector assertion, not an inconclusive baseline. The positive full-corpus fixture passes before/after.

### M-CACHE — KILLED

Mutant: `reports/round-59/rowcheck.py:90` changes `hit = _CACHE.get(url)` → `hit = None`.

Expected detector: Request-count detector: two full checks must produce leaf=1/root=1; mutant produces leaf=6/root=2. The persistent-error fixture also changes from three attempts total to six.

```sh
timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/fetch59_probe.py --phase mutant-cache
timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/fetch59_probe.py --phase restored-cache
```

```text
PROBE one-fetch-reused-across-legs-and-rows detector=FAIL legs={"BOILER": true, "LOCATE": true, "RELEVANCE": true, "TOPIC": true} GET_counts={"http://reuse.fixture.test/": 2, "http://reuse.fixture.test/leaf": 6}
FETCH59-DETECTOR: FAIL live-403-listed-capture,live-404-listed-capture,live-403-no-capture,root-403-page-200-default-capture,root-403-page-200-listed-timestamp,both-roots-fail,one-fetch-reused-across-legs-and-rows,transient-429-then-200,persistent-429-error-reused
```

Captured rowcheck return: ```json
{
  "LOCATE": [
    true,
    "http://reuse.fixture.test/leaf"
  ],
  "BOILER": [
    true,
    "root-clear http://reuse.fixture.test/; not a title, h1 or meta label"
  ],
  "RELEVANCE": [
    true,
    "shared=['amule', 'cerem', 'charm', 'house', 'prote']"
  ],
  "TOPIC": [
    true,
    "quote_hits=2 function_words=5 page_hits=6 page_terms=5 need=1/2/3/2"
  ]
}
```

Hashes (SHA-256, before → mutated → exact restored):
```text
d4d0b703167de4432b0fabc7188a0fbf12c7bf9b40fab1ba7838a281438d8b1e
47d31225086da39a1f06a87d659c0255d8a65615d12eb33c638ff61be849d654
d4d0b703167de4432b0fabc7188a0fbf12c7bf9b40fab1ba7838a281438d8b1e
```

Restored detector: exit 0, `FETCH59-DETECTOR: PASS`; temporary corpus bytes restored exactly, no mismatches. This named fixture/control catches the mutant within this wave's scope.

### M-ROOT — KILLED

Mutant: `reports/round-59/rowcheck.py:189` changes `if "web.archive.org" in loc_url:` → `if True:`.

Expected detector: Root-fallback fixture must PASS BOILER and fetch the capture root. Mutant fails BOILER immediately and never fetches that fallback; listed-timestamp variant also catches it.

```sh
timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/fetch59_probe.py --phase mutant-capture-root
timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/fetch59_probe.py --phase restored-capture-root
```

```text
PROBE root-403-page-200-default-capture detector=FAIL legs={"BOILER": false, "LOCATE": true, "RELEVANCE": true, "TOPIC": true} GET_counts={"http://root403.fixture.test/": 1, "http://root403.fixture.test/leaf": 1}
FETCH59-DETECTOR: FAIL root-403-page-200-default-capture,root-403-page-200-listed-timestamp,both-roots-fail
```

Captured rowcheck return: ```json
{
  "LOCATE": [
    true,
    "http://root403.fixture.test/leaf"
  ],
  "BOILER": [
    false,
    "root-unfetchable http://root403.fixture.test/ HTTPError"
  ],
  "RELEVANCE": [
    true,
    "shared=['amule', 'cerem', 'charm', 'house', 'prote']"
  ],
  "TOPIC": [
    true,
    "quote_hits=2 function_words=5 page_hits=6 page_terms=5 need=1/2/3/2"
  ]
}
```

Hashes (SHA-256, before → mutated → exact restored):
```text
d4d0b703167de4432b0fabc7188a0fbf12c7bf9b40fab1ba7838a281438d8b1e
1c8c32e416f00860a09f82919a7ec6fddc71f348e8de6ecbd9954c3981abab66
d4d0b703167de4432b0fabc7188a0fbf12c7bf9b40fab1ba7838a281438d8b1e
```

Restored detector: exit 0, `FETCH59-DETECTOR: PASS`; temporary corpus bytes restored exactly, no mismatches. This named fixture/control catches the mutant within this wave's scope.

### M-WINDOW — KILLED

Mutant: `reports/round-59/rowcheck.py:107` changes `WINDOW = 3` → `WINDOW = 1000000`.

Expected detector: Distance-negative fixture must FAIL TOPIC. Mutant locates the distant CHARM/GUARD pair and changes TOPIC to PASS.

```sh
timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/fetch59_probe.py --phase mutant-topic-window
timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/fetch59_probe.py --phase restored-topic-window
```

```text
PROBE topic-window-negative detector=FAIL legs={"BOILER": true, "LOCATE": true, "RELEVANCE": true, "TOPIC": true} GET_counts={"http://topicgap.fixture.test/": 1, "http://topicgap.fixture.test/leaf": 1}
FETCH59-DETECTOR: FAIL topic-window-negative
```

Captured rowcheck return: ```json
{
  "LOCATE": [
    true,
    "http://topicgap.fixture.test/leaf"
  ],
  "BOILER": [
    true,
    "root-clear http://topicgap.fixture.test/; not a title, h1 or meta label"
  ],
  "RELEVANCE": [
    true,
    "shared=['catal', 'histo', 'museu', 'prote', 'reade', 'stone']"
  ],
  "TOPIC": [
    true,
    "quote_hits=1 function_words=4 page_hits=5 page_terms=3 need=1/2/3/2"
  ]
}
```

Hashes (SHA-256, before → mutated → exact restored):
```text
d4d0b703167de4432b0fabc7188a0fbf12c7bf9b40fab1ba7838a281438d8b1e
245c0c9bdfd8fec05c4788f67b5dcfceccd5029e164e2c1d5e357e4bcd40fa1a
d4d0b703167de4432b0fabc7188a0fbf12c7bf9b40fab1ba7838a281438d8b1e
```

Restored detector: exit 0, `FETCH59-DETECTOR: PASS`; temporary corpus bytes restored exactly, no mismatches. This named fixture/control catches the mutant within this wave's scope.

### M-QUAL — KILLED

Mutant: `reports/round-59/accept-c.py:259` changes `if planted and all((p, "NOT-SUPPORTED") in found and (p, "SUPPORTED") not in found for p in planted):` → `if True:`.

Expected detector: Rubber stamp must fail SUPPORT because it supports the plant. Mutant qualifies both seats and changes the full counter to ACCEPT-C-59: PASS, exit 0.

```sh
timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/fetch59_probe.py --phase mutant-support-qualification
timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/fetch59_probe.py --phase restored-support-qualification
```

```text
FETCH59-DETECTOR: FAIL support-rubber-stamp
```

Mutant-only diagnostic control (not a frozen-counter receipt):

CONTROL m-qual-support-rubber-stamp-MEETS-COUNTER | claim C | exit 0 | ACCEPT-C-59: PASS | failing legs: []

```sh
timeout 900 /usr/bin/python3 -B /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/counter_driver.py
```

```text
SET PASS count=235 required=235 added=['corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'] removed=[]
SWEEP PASS exit=0 rows 235 files 235 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE PASS passing=20 cited=20 at=2026-10-23T02:51Z failing=[]
BOILER PASS passing=20 cited=20 at=2026-10-23T02:51Z failing=[]
RELEVANCE PASS passing=20 cited=20 at=2026-10-23T02:51Z failing=[]
TOPIC PASS passing=20 cited=20 at=2026-10-23T02:51Z failing=[]
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT PASS shared=[] hosts=20 need=10
SUPPORT PASS unsupported=[] qualified_seats=['FixtureA59', 'FixtureB59'] need_seats=2 planted=['FixtureA59:Q1', 'FixtureB59:Q1']
ACCEPT-C-59: PASS
```

Hashes (SHA-256, before → mutated → exact restored):
```text
2d42deb5b84a06db06ec13cef49e4209f219e66b02cf4b21caa7d61a8197ea5e
a74cebc18c1fed16b4ec415b23c08b20e50f3d3f374075f496ea97f6d9616123
2d42deb5b84a06db06ec13cef49e4209f219e66b02cf4b21caa7d61a8197ea5e
```

Restored detector: exit 0, `FETCH59-DETECTOR: PASS`; temporary corpus bytes restored exactly, no mismatches. This named fixture/control catches the mutant within this wave's scope.

### M-EQUALITY — KILLED

Mutant: `reports/round-59/accept-c.py:264` changes `if sid and sid != "PLANTED" and shown.get(label) and shown.get(label) == anchor.get(sid):` → `if sid and sid != "PLANTED" and shown.get(label):`.

Expected detector: Mismatched packet quotes must fail SUPPORT. Mutant counts them anyway and changes the full counter to ACCEPT-C-59: PASS, exit 0.

```sh
timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/fetch59_probe.py --phase mutant-packet-quote-equality
timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/fetch59_probe.py --phase restored-packet-quote-equality
```

```text
FETCH59-DETECTOR: FAIL support-wrong-quote
```

Mutant-only diagnostic control (not a frozen-counter receipt):

CONTROL m-equality-support-wrong-quote-MEETS-COUNTER | claim C | exit 0 | ACCEPT-C-59: PASS | failing legs: []

```sh
timeout 900 /usr/bin/python3 -B /fast/scratch/hyaku/kotodama-r59/CtlFetchRule59/counter_driver.py
```

```text
SET PASS count=235 required=235 added=['corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'] removed=[]
SWEEP PASS exit=0 rows 235 files 235 missing_from_index 0 []
FLOOR PASS cited=20 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE PASS passing=20 cited=20 at=2026-10-23T02:52Z failing=[]
BOILER PASS passing=20 cited=20 at=2026-10-23T02:52Z failing=[]
RELEVANCE PASS passing=20 cited=20 at=2026-10-23T02:52Z failing=[]
TOPIC PASS passing=20 cited=20 at=2026-10-23T02:52Z failing=[]
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT PASS shared=[] hosts=20 need=10
SUPPORT PASS unsupported=[] qualified_seats=['FixtureA59', 'FixtureB59'] need_seats=2 planted=['FixtureA59:Q1', 'FixtureB59:Q1']
ACCEPT-C-59: PASS
```

Hashes (SHA-256, before → mutated → exact restored):
```text
2d42deb5b84a06db06ec13cef49e4209f219e66b02cf4b21caa7d61a8197ea5e
467af20ab54042b3d98b1bd5646271bb7c3a9e395f629378a694847ef8672446
2d42deb5b84a06db06ec13cef49e4209f219e66b02cf4b21caa7d61a8197ea5e
```

Restored detector: exit 0, `FETCH59-DETECTOR: PASS`; temporary corpus bytes restored exactly, no mismatches. This named fixture/control catches the mutant within this wave's scope.

### Surviving-mutant accounting

With the full scoped behavioral detector: **0/5 survived; 5/5 killed; 0 inconclusive targeted probes.** The pre-existing concurrent-cache and 501 failures above are not mutant kills.

If only the four full-corpus acceptance controls are retained, **M-CACHE, M-ROOT and M-WINDOW survive that narrower set**: their ACCEPT/leg truth patterns are unchanged there. They are caught by the dedicated request-count, capture-root and distance-negative fixtures, respectively. M-QUAL is caught by rubber-stamp rejection; M-EQUALITY by packet-quote rejection. Keep those focused fixtures rather than relying on a final ACCEPT line alone.

## Restoration and process evidence

Final `timeout 30 sha256sum` output equals the initial output for all six frozen instrument inputs:

```text
d4d0b703167de4432b0fabc7188a0fbf12c7bf9b40fab1ba7838a281438d8b1e  reports/round-59/rowcheck.py
2d42deb5b84a06db06ec13cef49e4209f219e66b02cf4b21caa7d61a8197ea5e  reports/round-59/accept-c.py
64e78c749b4dc334217499d7411671dbcb904f793b168bfae85dc69b68ab16f8  reports/round-59/reopen-quote.py
8194bc579c6459a064d734633f7e258ab5da7ab5df80993d8421a31221578814  reports/round-59/accept-d.py
46a3daec145a32dccb46c45c6e9d07146721dc363872a5c10c30cb177ca9e350  reports/round-59/d-fixes.json
96744ac5bd40d0f245d01178d028fd66f08348f7b6a7fc6fd91f1dffef628e0a  reports/round-59/claims.json
```

Each harness restores the exact pre-fixture bytes of every existing payload file and removes every fixture-created file; byte comparisons reported no mismatches. Every started server was killed and waited before that harness returned:

```text
pristine SERVER_STOP {"alive": false, "returncode": -15, "timeout_pid": 3967348} FIXTURE_RESTORE exact=True mismatches=[]
mutant-cache SERVER_STOP {"alive": false, "returncode": -15, "timeout_pid": 4019678} FIXTURE_RESTORE exact=True mismatches=[]
restored-cache SERVER_STOP {"alive": false, "returncode": -15, "timeout_pid": 4053828} FIXTURE_RESTORE exact=True mismatches=[]
mutant-capture-root SERVER_STOP {"alive": false, "returncode": -15, "timeout_pid": 4060721} FIXTURE_RESTORE exact=True mismatches=[]
restored-capture-root SERVER_STOP {"alive": false, "returncode": -15, "timeout_pid": 4082700} FIXTURE_RESTORE exact=True mismatches=[]
mutant-topic-window SERVER_STOP {"alive": false, "returncode": -15, "timeout_pid": 4104171} FIXTURE_RESTORE exact=True mismatches=[]
restored-topic-window SERVER_STOP {"alive": false, "returncode": -15, "timeout_pid": 4128338} FIXTURE_RESTORE exact=True mismatches=[]
mutant-support-qualification SERVER_STOP {"alive": false, "returncode": -15, "timeout_pid": 4167407} FIXTURE_RESTORE exact=True mismatches=[]
restored-support-qualification SERVER_STOP {"alive": false, "returncode": -15, "timeout_pid": 4169341} FIXTURE_RESTORE exact=True mismatches=[]
mutant-packet-quote-equality SERVER_STOP {"alive": false, "returncode": -15, "timeout_pid": 4170993} FIXTURE_RESTORE exact=True mismatches=[]
restored-packet-quote-equality SERVER_STOP {"alive": false, "returncode": -15, "timeout_pid": 4172796} FIXTURE_RESTORE exact=True mismatches=[]
direct-pristine SERVER_STOP {"alive": false, "returncode": -15, "timeout_pid": 459154} FIXTURE_RESTORE exact=True mismatches=[]
```

All public subprocesses/curl calls returned; all counter subprocesses completed. No server or background job remains. No lane changes beyond this report and its permitted small fixture/evidence directory were made. No counter fixes were integrated.

counter weaknesses:
- **Observed no-reader MEETS-COUNTER:** the unchanged CLI accepts invented reviewer agentIds and fixture-owned matching hash inputs without checking a real dispatch receipt or that the commitments existed at the declared revision/time. The scripted report knows the planted label and supports everything else. Fix before data: authenticate registry membership against an independently protected dispatch receipt; anchor planted/key commitments to the designated frozen revision and keep the blind key out of report-author control. Self-consistent author-written files are not independent qualification.
- **Observed host-diversity bypass:** 20 ports on `127.0.0.1` count as 20 hosts. Fix DISTINCT to canonicalize `urlsplit(first_url).hostname` (not netloc/port); reject nonpublic/local fixture endpoints in production if external sources are required. Preserve an explicit test-only allowance only outside the frozen predicate.
- **Observed one-fetch violation under concurrency:** two simultaneous checks fetch the same page/root twice while all row legs PASS. Fix `_fetch_once` with a per-URL in-flight result/exception shared by waiters; keep the barrier/count fixture. The serial cache test alone misses this.
- **Observed docstring/retry mismatch:** transient 501 is not retried although FETCH-59 says 5xx; the single error is cached. Fix the retry condition to the declared 500–599 rule, or explicitly narrow the declaration before freeze; do not silently reinterpret it after data.
- **Acceptance-only mutation blind spots:** final ACCEPT truth alone misses cache/fallback/window regressions on stable positive pages. Preserve the three dedicated count/fallback/distance fixtures. None of the five assigned mutants survives the full scoped detector; this is not permission to change the contract.
