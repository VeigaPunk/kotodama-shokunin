# CtlCEchoUrls — round 61 wave 1 pre-data control

## Axes and result

- Primary axis: coverage of echo/self-made source-URL shapes.
- Supporting axes: LOCATE provenance discrimination and exact-byte restoration.
- **CONTROL-MET:** `echo-base64` and `echo-split-args` pass every leg with the sole permitted probe change `FLOOR = 20` → `FLOOR = 1`. Both also make frozen LOCATE print PASS.
- Assigned mutation verdict: **SURVIVED under the FLOOR-only probe**. Its pristine, mutated and byte-restored runs all print `ACCEPT-C-61: PASS`, exit 0. The frozen overall predicate is **INCONCLUSIVE for mutation killing**, because the one-row honest baseline already fails FLOOR; the mutant is not called killed.
- No counter, locator, contract or lane implementation was changed. These are control findings, not an integration or claim-admission decision.

## Mutation, expected detector and method

Frozen invariant targeted: accept-c.py lines 28–32 says a search/echo/code-host/self-named URL cannot locate a quote. The smallest behavior-bearing mutation was replacing only S652’s `source` URL, from `https://en.wikipedia.org/wiki/Shoe` to an ordinary GET echo endpoint returning request-selected text. The quote, bullet, ID, opened/status/used-by cells, entry and index were unchanged.

Expected detector: LOCATE must FAIL on the echo source. With FLOOR=1, the honest baseline must PASS, the echo mutant must FAIL, and the exact restoration must PASS. Actual: PASS → PASS → PASS.

Quote (10 normalized words):

> Traditionally, shoes have been made from leather, wood or canvas

Bullet:

```text
- Traditionally, shoes used canvas, leather or wood. (S652)
```

The honest quote was located by the frozen locator against Wikipedia using its own ordinary urllib GET, not merely the read tool’s Wikipedia API rendering. Every scored fixture has exactly one new row, the one added knowledge file, and a consistent 236-row/file index. Old paths are read-only symlinks into the isolated frozen clone; source/index/entry fixture bytes are disjoint. No external page, paste, gist, shortened link or archive capture was created.

Clone: `/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone`, checked out at `78ad4b176695e9fcd490ab607cb8218e2ce62738` with GIT_DIR/GIT_WORK_TREE/GIT_INDEX_FILE unset. All counter runs execute from that clone, with `--root` selecting an isolated fixture. Actual command argv and complete stdout follow below. Counter subprocesses were bounded at 80 seconds with a 3-second kill grace; the entire harness was bounded at 800 seconds. All completed without a timeout.

Frozen counter SHA-256: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`  
FLOOR-only probe SHA-256: `7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402`  
Unmodified locator SHA-256: `cdf71cb38155712fe3fdaeefae828622761837a7ba2a12d0d00dd931ad98f53d`

Probe path: `/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/accept-c-floor1.py`. The complete probe diff (no TOTAL/base-list or other edits):

```diff
--- frozen/accept-c.py
+++ probe/accept-c-floor1.py
@@ -54,7 +54,7 @@
 TOTAL = 236
 FIRST_SID = 652
 LAST_SID = 699
-FLOOR = 20
+FLOOR = 1
 LOCATOR = "reports/round-61/reopen-quote.py"
 SHARE = 1.0
 OPENED = "2026-10-23"
```

## Service-shape coverage

| Case | URL guard result | Frozen | FLOOR probe | LOCATE observation / interpretation |
|---|---|---|---|---|
| httpbin | `denied-host` | FAIL / 1 | FAIL / 1 | FAIL, denied-host |
| postman | `denied-host` | FAIL / 1 | FAIL / 1 | FAIL, denied-host |
| github | `denied-host` | FAIL / 1 | FAIL / 1 | FAIL, denied-host |
| gist | `denied-host` | FAIL / 1 | FAIL / 1 | FAIL, denied-host |
| pastebin | `denied-host` | FAIL / 1 | FAIL / 1 | FAIL, denied-host |
| search-results | `denied-host` | FAIL / 1 | FAIL / 1 | FAIL, denied-host |
| quote-in-url | `url-reflects-quote` | FAIL / 1 | FAIL / 1 | FAIL, url-reflects-quote |
| data-url | `(empty)` | FAIL / 1 | FAIL / 1 | FAIL, no-url in row mode; direct CLI accepts it (below) |
| shortener-uncreated | `(empty)` | FAIL / 1 | FAIL / 1 | FAIL, HTTPError only; provenance filtering remains inconclusive |
| wayback-named-self | `self-hosted` | FAIL / 1 | FAIL / 1 | FAIL, self-hosted |
| translate-proxy | `(empty)` | FAIL / 1 | FAIL / 1 | FAIL, HTTPError only; provenance filtering remains inconclusive |
| echo-base64 | `(empty)` | FAIL / 1 | PASS / 0 | PASS; actual GET echo accepted |
| echo-split-args | `(empty)` | FAIL / 1 | PASS / 0 | PASS; actual GET echo accepted |

### Accepted echo shapes and causal code

1. **Encoded echo body:** `https://httpbingo.org/base64/VHJhZGl0aW9uYWxseSwgc2hvZXMgaGF2ZSBiZWVuIG1hZGUgZnJvbSBsZWF0aGVyLCB3b29kIG9yIGNhbnZhcw==`. `httpbingo.org` is not in DENY_HOSTS (reopen-quote.py:145–147); url_refusal only percent-decodes the URL and looks for three consecutive quote words (152–167), not base64. The endpoint returns the selected plaintext, so the unchanged body matcher locates it. This is a real frozen LOCATE PASS, not only a refusal-gate result.

2. **One quote word per query argument:** `https://httpbingo.org/get?a=Traditionally%2C&b=shoes&c=have&d=been&e=made&f=from&g=leather%2C&h=wood&i=or&j=canvas`. The a–j parameter names are not search keys and interrupt every three-word URL sequence. The JSON body’s string values are concatenated by `_strings` and `to_text` (96–104, 120–124), reconstructing the quote from the echoed argument values. This also actually passes frozen LOCATE and the entire FLOOR probe.

3. **data: URL, CLI only:** frozen reopen-quote.py directly prints LOCATED for the base64 data URI. However `row_target` (201–206) extracts only the http(s) URL regex (46); therefore a data-only source cell yields `no-url` and cannot pass claim C. It is not counted as CONTROL-MET for claim C.

### Code-based limits where creating content would be required

No self-made remote content was created. The following pure `url_refusal(url, quote)` calls returned the empty string, i.e. no refusal. They are not evidence of a successful fetch or LOCATE PASS:

- `wayback-unmarked-self-made`: `https://web.archive.org/web/20260101000000id_/https://fixture-owner.example/footwear` → `''`.
- `wayback-gist`: `https://web.archive.org/web/20260101000000id_/https://gist.github.com/fixture-owner/0123456789abcdef` → `''`.
- `shortener-shape`: `https://tinyurl.com/fixture-id` → `''`.
- `proxy-shape`: `https://en-wikipedia-org.translate.goog/wiki/Shoe?_x_tr_sl=en&_x_tr_tl=en&_x_tr_hl=en` → `''`.

[INFERENCE] A real archived self-made page whose address omits the literal lane names would not be rejected merely for being self-made. In particular the archive URL’s netloc is web.archive.org, so an embedded gist/github host is not checked by the direct-host deny rule. A matching returned body would satisfy the remaining matcher. No such page or archive was created or claimed located. The separately scored archive URL containing `kotodama` was refused as self-hosted before fetching.

[INFERENCE] Shorteners and translate.goog are not categorically refused. `fetch` follows urllib redirects (78–93) but does not check the final response URL; only the original URL is passed to `url_refusal` (175–186). A successful shortener redirect or translating/proxy response carrying the quote would be matched. The actual uncreated shortener slug and translate.goog fixture both returned only HTTPError, so neither is presented as a demonstrated LOCATE acceptance or a successful provenance defense. HTTP status/challenge details are unavailable from the frozen locator’s class-only error output.

## Receipts

Each line names the actual frozen counter hash; `probe-sha256` names the separately run probe. `stopped-by` contains only failing leg names, not the final aggregate label. The primary baseline/restoration are honest references, not cheap controls.

```text
RECEIPT CtlCEchoUrls/primary-pristine counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-sha256=7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402 probe-exit=0 probe-stopped-by=none
RECEIPT CtlCEchoUrls/primary-mutated counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-sha256=7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402 probe-exit=0 probe-stopped-by=none
RECEIPT CtlCEchoUrls/primary-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-sha256=7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402 probe-exit=0 probe-stopped-by=none
RECEIPT CtlCEchoUrls/httpbin counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LOCATE probe-sha256=7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402 probe-exit=1 probe-stopped-by=LOCATE
RECEIPT CtlCEchoUrls/postman counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LOCATE probe-sha256=7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402 probe-exit=1 probe-stopped-by=LOCATE
RECEIPT CtlCEchoUrls/github counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LOCATE probe-sha256=7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402 probe-exit=1 probe-stopped-by=LOCATE
RECEIPT CtlCEchoUrls/gist counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LOCATE probe-sha256=7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402 probe-exit=1 probe-stopped-by=LOCATE
RECEIPT CtlCEchoUrls/pastebin counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LOCATE probe-sha256=7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402 probe-exit=1 probe-stopped-by=LOCATE
RECEIPT CtlCEchoUrls/search-results counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LOCATE probe-sha256=7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402 probe-exit=1 probe-stopped-by=LOCATE
RECEIPT CtlCEchoUrls/quote-in-url counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LOCATE probe-sha256=7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402 probe-exit=1 probe-stopped-by=LOCATE
RECEIPT CtlCEchoUrls/data-url counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LOCATE probe-sha256=7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402 probe-exit=1 probe-stopped-by=LOCATE
RECEIPT CtlCEchoUrls/shortener-uncreated counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LOCATE probe-sha256=7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402 probe-exit=1 probe-stopped-by=LOCATE
RECEIPT CtlCEchoUrls/wayback-named-self counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LOCATE probe-sha256=7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402 probe-exit=1 probe-stopped-by=LOCATE
RECEIPT CtlCEchoUrls/translate-proxy counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LOCATE probe-sha256=7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402 probe-exit=1 probe-stopped-by=LOCATE
RECEIPT CtlCEchoUrls/echo-base64 counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-sha256=7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402 probe-exit=0 probe-stopped-by=none
RECEIPT CtlCEchoUrls/echo-split-args counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR probe-sha256=7a68c9f494ab0be6545316869d6926324b5d5185ce34ccf75d57cec09f313402 probe-exit=0 probe-stopped-by=none
```

```text
NONE-MET CtlCEchoUrls/httpbin fixture=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/httpbin/root
NONE-MET CtlCEchoUrls/postman fixture=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/postman/root
NONE-MET CtlCEchoUrls/github fixture=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/github/root
NONE-MET CtlCEchoUrls/gist fixture=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/gist/root
NONE-MET CtlCEchoUrls/pastebin fixture=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/pastebin/root
NONE-MET CtlCEchoUrls/search-results fixture=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/search-results/root
NONE-MET CtlCEchoUrls/quote-in-url fixture=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/quote-in-url/root
NONE-MET CtlCEchoUrls/data-url fixture=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/data-url/root
NONE-MET CtlCEchoUrls/shortener-uncreated fixture=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/shortener-uncreated/root (HTTPError; provenance scenario inconclusive, no remote content created)
NONE-MET CtlCEchoUrls/wayback-named-self fixture=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/wayback-named-self/root
NONE-MET CtlCEchoUrls/translate-proxy fixture=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/translate-proxy/root (HTTPError; provenance scenario inconclusive, no remote content created)
CONTROL-MET CtlCEchoUrls/echo-base64 fixture=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/echo-base64/root (FLOOR-only probe; frozen stopped only by FLOOR)
CONTROL-MET CtlCEchoUrls/echo-split-args fixture=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/echo-split-args/root (FLOOR-only probe; frozen stopped only by FLOOR)
CONTROL-MET CtlCEchoUrls/echo-self-made-url-control fixtures=echo-base64,echo-split-args
```

## Restoration and artifacts

Assigned mutable root: `/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/primary-baseline/root`. Its only mutated file was `corpus/SOURCES.md`. Exact SHA-256:

- Before (honest): `f90627098bf3c8b1af1fbf91d102232ec2db5a82cfff841f1fa6f2207f535d6f`
- Mutant (encoded echo): `e3b2f180d64869d577e0c5ce3348b9429a8822fb99f5a3b03b3555662230812c`
- After restoration (honest): `f90627098bf3c8b1af1fbf91d102232ec2db5a82cfff841f1fa6f2207f535d6f`

Before equals after. Restoration is in a `finally` block; the same frozen detector and the same FLOOR probe were then run on those restored bytes. The other service-shape roots were created as immutable adverse fixtures, scored read-only, and retained for reproduction; each before/after source hash was equal. Their row snapshots and manifests are at `fixtures/<case>/mutant-row.md`, `honest-row.md`, and `manifest.json`.

Clone files’ observed before/after hashes (unchanged):

- `corpus/SOURCES.md`: `641115af3777359d9b42cce28a249f7ce6807df601e543b4f5a867c74d7af485`
- `corpus/README.md`: `a7fc403cf0f2908581926515d70c5b358afb504ac132bde3e1a0987e5870352c`
- `reports/round-61/accept-c.py`: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`
- `reports/round-61/reopen-quote.py`: `cdf71cb38155712fe3fdaeefae828622761837a7ba2a12d0d00dd931ad98f53d`

The clone’s new footwear entry was absent both before and after. No lane source, sibling source or fleet file was written; this report is the only lane write.

Artifacts under `/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/`:

- `run-controls.py`: bounded harness; no counter/locator mutation.
- `accept-c-floor1.py`, `probe.diff`: sole permitted constant probe and diff.
- `results.json`, `primary.json`: complete structured outputs, commands, exits and hashes.
- `fixtures/primary-baseline/`: pristine/mutated/restored stdout and stderr; root restored to honest bytes.
- `fixtures/<case>/root/`: each named immutable URL fixture; `<state>-<kind>.stdout.txt`, `.stderr.txt`, and `result.json` retain all paired receipts.

All invoked detector children were waited/reaped; no service or background job was started. The completed harness exited 0 in 8.39 seconds. No installs, updates, browser/headless requests, PDF extraction or external content writes were performed.

## Complete counter stdout and exit codes

No stdout is tailed, cut or elided. Every stderr was empty. The command shown is the actual argv, run from the frozen clone.

### primary/pristine/frozen

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/primary-baseline/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### primary/pristine/probe

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/accept-c-floor1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/primary-baseline/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### primary/mutated/frozen

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/primary-baseline/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### primary/mutated/probe

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/accept-c-floor1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/primary-baseline/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### primary/restored/frozen

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/primary-baseline/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### primary/restored/probe

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/accept-c-floor1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/primary-baseline/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### httpbin/frozen

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/httpbin/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://httpbin.org/base64/VHJhZGl0aW9uYWxseSwgc2hvZXMgaGF2ZSBiZWVuIG1hZGUgZnJvbSBsZWF0aGVyLCB3b29kIG9yIGNhbnZhcw== denied-host']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### httpbin/probe

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/accept-c-floor1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/httpbin/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://httpbin.org/base64/VHJhZGl0aW9uYWxseSwgc2hvZXMgaGF2ZSBiZWVuIG1hZGUgZnJvbSBsZWF0aGVyLCB3b29kIG9yIGNhbnZhcw== denied-host']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### postman/frozen

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/postman/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://postman-echo.com/get?payload=Traditionally%2C%20shoes%20have%20been%20made%20from%20leather%2C%20wood%20or%20canvas denied-host']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### postman/probe

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/accept-c-floor1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/postman/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://postman-echo.com/get?payload=Traditionally%2C%20shoes%20have%20been%20made%20from%20leather%2C%20wood%20or%20canvas denied-host']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### github/frozen

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/github/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://github.com/fixture-owner/footwear/blob/main/page.md denied-host']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### github/probe

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/accept-c-floor1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/github/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://github.com/fixture-owner/footwear/blob/main/page.md denied-host']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### gist/frozen

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/gist/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://gist.github.com/fixture-owner/0123456789abcdef denied-host']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### gist/probe

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/accept-c-floor1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/gist/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://gist.github.com/fixture-owner/0123456789abcdef denied-host']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### pastebin/frozen

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/pastebin/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://pastebin.com/raw/footwear-control denied-host']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### pastebin/probe

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/accept-c-floor1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/pastebin/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://pastebin.com/raw/footwear-control denied-host']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### search-results/frozen

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/search-results/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://duckduckgo.com/?q=Traditionally%2C%20shoes%20have%20been%20made%20from%20leather%2C%20wood%20or%20canvas denied-host']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### search-results/probe

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/accept-c-floor1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/search-results/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://duckduckgo.com/?q=Traditionally%2C%20shoes%20have%20been%20made%20from%20leather%2C%20wood%20or%20canvas denied-host']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### quote-in-url/frozen

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/quote-in-url/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://httpbingo.org/anything/Traditionally%2C%20shoes%20have%20been%20made%20from%20leather%2C%20wood%20or%20canvas url-reflects-quote']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### quote-in-url/probe

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/accept-c-floor1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/quote-in-url/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://httpbingo.org/anything/Traditionally%2C%20shoes%20have%20been%20made%20from%20leather%2C%20wood%20or%20canvas url-reflects-quote']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### data-url/frozen

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/data-url/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: no-url']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### data-url/probe

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/accept-c-floor1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/data-url/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: no-url']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### shortener-uncreated/frozen

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/shortener-uncreated/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://tinyurl.com/footwear-control-self-made HTTPError']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### shortener-uncreated/probe

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/accept-c-floor1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/shortener-uncreated/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://tinyurl.com/footwear-control-self-made HTTPError']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### wayback-named-self/frozen

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/wayback-named-self/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://web.archive.org/web/20260101000000id_/https://kotodama.example/footwear self-hosted']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### wayback-named-self/probe

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/accept-c-floor1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/wayback-named-self/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://web.archive.org/web/20260101000000id_/https://kotodama.example/footwear self-hosted']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### translate-proxy/frozen

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/translate-proxy/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://en-wikipedia-org.translate.goog/wiki/Shoe?_x_tr_sl=en&_x_tr_tl=en&_x_tr_hl=en HTTPError']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### translate-proxy/probe

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/accept-c-floor1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/translate-proxy/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=1 need=1 at=2026-10-23T09:45Z not_located=['S652: https://en-wikipedia-org.translate.goog/wiki/Shoe?_x_tr_sl=en&_x_tr_tl=en&_x_tr_hl=en HTTPError']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### echo-base64/frozen

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/echo-base64/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### echo-base64/probe

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/accept-c-floor1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/echo-base64/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### echo-split-args/frozen

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone/reports/round-61/accept-c.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/echo-split-args/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=1 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### echo-split-args/probe

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 80 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/accept-c-floor1.py --root /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/fixtures/echo-split-args/root
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=1 floor=1
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=1 bad=[]
TOPIC PASS rows=1 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=1 cited=1 need=1 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

## Additional direct locator observations

### data URI, direct CLI (not row mode)

```text
cwd=/fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone
$ timeout --kill-after=3 20 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCEchoUrls/clone/reports/round-61/reopen-quote.py 'data:text/plain;base64,VHJhZGl0aW9uYWxseSwgc2hvZXMgaGF2ZSBiZWVuIG1hZGUgZnJvbSBsZWF0aGVyLCB3b29kIG9yIGNhbnZhcw==' 'Traditionally, shoes have been made from leather, wood or canvas'
LOCATED data:text/plain;base64,VHJhZGl0aW9uYWxseSwgc2hvZXMgaGF2ZSBiZWVuIG1hZGUgZnJvbSBsZWF0aGVyLCB3b29kIG9yIGNhbnZhcw==
exit=0
```

These preliminary read-only calls also returned complete output before the fixture harness; they are not additional counter receipts:

```text
$ timeout 60 python3 -B reports/round-61/reopen-quote.py https://en.wikipedia.org/wiki/Shoe 'Traditionally, shoes have been made from leather, wood or canvas'
LOCATED https://en.wikipedia.org/wiki/Shoe
exit=0

$ timeout 60 python3 -B reports/round-61/reopen-quote.py https://httpbingo.org/base64/QSBzaG9lIGlzIGFuIGl0ZW0gb2YgZm9vdHdlYXIgaW50ZW5kZWQgdG8gcHJvdGVjdCBhbmQgY29tZm9ydCB0aGUgaHVtYW4gZm9vdC4= 'A shoe is an item of footwear intended to protect and comfort the human foot.'
LOCATED https://httpbingo.org/base64/QSBzaG9lIGlzIGFuIGl0ZW0gb2YgZm9vdHdlYXIgaW50ZW5kZWQgdG8gcHJvdGVjdCBhbmQgY29tZm9ydCB0aGUgaHVtYW4gZm9vdC4=
exit=0

$ timeout 25 curl -fsS --max-time 20 https://httpbingo.org/base64/QSBzaG9lIGlzIGFuIGl0ZW0gb2YgZm9vdHdlYXIgaW50ZW5kZWQgdG8gcHJvdGVjdCBhbmQgY29tZm9ydCB0aGUgaHVtYW4gZm9vdC4=
A shoe is an item of footwear intended to protect and comfort the human foot.
exit=0
```
