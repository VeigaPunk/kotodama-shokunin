# CtlCQuoteDump — pre-data quote-dump control

## Result

CONTROL-MET CtlCQuoteDump/quote-dump fixture=/fast/scratch/hyaku/kotodama-r61/CtlCQuoteDump/drop12.md under the permitted FLOOR-only probe.

The cheapest passing dump among the requested variants deletes every twelfth quote word: one deletion per line, three deleted words total, 485 → 469 entry bytes. It passes COPY and LINK under both counters, and every leg under the FLOOR=3 probe. The frozen counter still fails FLOOR (3 cited rows, required 20); it does **not** meet the full frozen predicate. Reordering each quote's two halves also passes the probe. A verbatim dump and a dump with `reportedly` appended fail COPY.

Axes: coverage/detection of quote dumping; honesty of live source anchors; mutation size; exact restoration. This is a detector coverage finding, not a change to the frozen contract. The word-deletion and half-reordering lines satisfy the counter's literal consecutive-copy bound without doing a genuine paraphrase.

## Isolation and procedure

- Read claims.json first, then the godspeed skill and /home/vgpnk/.omp/agent/RULES.md.
- Scratch root: `/fast/scratch/hyaku/kotodama-r61/CtlCQuoteDump/`.
- Cloned with GIT_DIR, GIT_WORK_TREE and GIT_INDEX_FILE unset and checked out `78ad4b176695e9fcd490ab607cb8218e2ce62738` using the prescribed local clone command. No lane or fleet git/jj write commands.
- Only this report was written in the lane. All fixtures, the probe, and fixture edits are in the isolated scratch root.
- Built a reference fixture with three honest rows S652–S654, the one new entry, and corresponding index/count changes. Only the entry's three cited bullet lines vary between probes; source rows, locator, index, and frozen counter remain unchanged throughout the mutation sequence.
- Frozen and probe runs were paired concurrently over identical, stable fixture bytes; mutation installation waited for both runs to finish. No subagents, background jobs, browsers, access-control circumvention, installs, or updates.
- Every invoked process was bounded with timeout (at most 900 seconds); all returned. No running process tree was left behind.

## Three real located footwear quotes

The three rows use two distinct new URLs, not three: S652 and S654 are separate real quotes from the same SFO Museum exhibition. The counter does not require distinct URLs among newly added rows. A grep of the frozen clone's SOURCES.md for both accepted URLs returned `No matches found` before insertion; all scored FRESH legs passed.

### S652 — SFO Museum, Stepping Out: Shoes in World Cultures (2017)

URL: https://www.sfomuseum.org/exhibitions/stepping-out-shoes-world-cultures

Body quote, 19 normalized words:

> In the most utilitarian sense, shoes and sandals simply protect feet; hence, practical concerns have long driven shoe design.

Command (timeout 300; lane locator, ordinary GET):

```sh
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py https://www.sfomuseum.org/exhibitions/stepping-out-shoes-world-cultures 'In the most utilitarian sense, shoes and sandals simply protect feet; hence, practical concerns have long driven shoe design.'; echo exit=$?
```

Full stdout:

```text
LOCATED https://www.sfomuseum.org/exhibitions/stepping-out-shoes-world-cultures
exit=0
```

### S653 — American University in Cairo, King Tut's Sandals Featured at Ancient Egyptian Footwear Exhibition (2015-10-11)

URL: https://www.aucegypt.edu/news/stories/king-tuts-sandals-featured-ancient-egyptian-footwear-exhibition

Body quote, 23 normalized words, attributed on the page to Veldmeijer:

> You can see the various steps used by the Egyptians to turn sandals into completely closed shoes — the evolution of a new form.

Command:

```sh
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py https://www.aucegypt.edu/news/stories/king-tuts-sandals-featured-ancient-egyptian-footwear-exhibition 'You can see the various steps used by the Egyptians to turn sandals into completely closed shoes — the evolution of a new form.'; echo exit=$?
```

Full stdout:

```text
LOCATED https://www.aucegypt.edu/news/stories/king-tuts-sandals-featured-ancient-egyptian-footwear-exhibition
exit=0
```

### S654 — SFO Museum, same exhibition

Body quote, 17 normalized words:

> During the 1870s, athletic footwear began to be offered for sports and leisure activities, such as tennis.

Command:

```sh
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py https://www.sfomuseum.org/exhibitions/stepping-out-shoes-world-cultures 'During the 1870s, athletic footwear began to be offered for sports and leisure activities, such as tennis.'; echo exit=$?
```

Full stdout:

```text
LOCATED https://www.sfomuseum.org/exhibitions/stepping-out-shoes-world-cultures
exit=0
```

### Rejected candidate, not used in any fixture

The read tool displayed the following sentence in Noel B. Salazar's Maasai sandals article, but the prescribed live locator did not locate it. It was discarded without a confirming rerun or a workaround:

```sh
timeout 300 python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-61/reopen-quote.py https://journals.openedition.org/etnografica/12724 'A shoemaker can produce seven or eight pairs from one single used tyre.'; echo exit=$?
```

Full stdout:

```text
NOT_LOCATED https://journals.openedition.org/etnografica/12724 quote-absent
exit=1
```

## Counter identity and permitted probe diff

Frozen counter: `/fast/scratch/hyaku/kotodama-r61/CtlCQuoteDump/clone/reports/round-61/accept-c.py`

SHA256 before and after: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.

Probe: `/fast/scratch/hyaku/kotodama-r61/CtlCQuoteDump/accept-c-floor3.py`

SHA256 before and after: `71f91748f4e69664038d0dfbf9f80c77875c1cf652a498fea2bf8d3cf7402749`.

The only probe difference is FLOOR=20 → FLOOR=3. TOTAL, BASE_LIST and all detector logic are unchanged. Full diff stdout:

```diff
--- /fast/scratch/hyaku/kotodama-r61/CtlCQuoteDump/clone/reports/round-61/accept-c.py	2026-10-23 06:41:10.540058466 -0300
+++ /fast/scratch/hyaku/kotodama-r61/CtlCQuoteDump/accept-c-floor3.py	2026-10-23 06:44:13.832102034 -0300
@@ -54,7 +54,7 @@
 TOTAL = 236
 FIRST_SID = 652
 LAST_SID = 699
-FLOOR = 20
+FLOOR = 3
 LOCATOR = "reports/round-61/reopen-quote.py"
 SHARE = 1.0
 OPENED = "2026-10-23"
diff_exit=1
```

Clone locator SHA256: `cdf71cb38155712fe3fdaeefae828622761837a7ba2a12d0d00dd931ad98f53d`.

## Mutants and expected detector

Pristine reference entry: `pristine.md` under the scratch root. Tested file: `clone/corpus/knowledge/culture-material/footwear-codes-terminology.md`.

| Case | Entry change | Expected detector | Observed probe verdict |
|---|---|---|---|
| pristine | honest paraphrases | PASS | PASS |
| verbatim | paste each complete anchor quote | COPY failure | KILLED: COPY fails with runs 19, 23, 17 |
| drop12 | delete quote words 12, 24, …; here only word 12 exists in each quote | target COPY; detect un-restated quote dumping | SURVIVED: COPY, LINK and all probe legs pass |
| halves | swap two contiguous halves of each quote | target COPY; detect un-restated quote dumping | SURVIVED: COPY, LINK and all probe legs pass |
| reportedly | append `reportedly` after each otherwise verbatim quote | COPY failure | KILLED: COPY fails with runs 19, 23, 17 |
| restored | restore pristine entry byte-for-byte | same result as pristine | PASS |

The frozen **whole-predicate** mutation verdict is INCONCLUSIVE for all four mutants because the pristine three-row fixture already fails FLOOR. Killed/survived above refers only to the valid pristine→mutant→restored sequence under the permitted FLOOR=3 probe, whose pristine and restored runs both pass.

Exact cheapest dump (`drop12.md`):

```markdown
- In the most utilitarian sense, shoes and sandals simply protect feet; practical concerns have long driven shoe design. (S652)
- You can see the various steps used by the Egyptians to sandals into completely closed shoes — the evolution of a new form. (S653)
- During the 1870s, athletic footwear began to be offered for sports leisure activities, such as tennis. (S654)
```

The deleted words are `hence`, `turn`, and `and`. The second line becomes malformed, but LINK and COPY still pass. The mutation does not alter the truthful anchor quote or live source.

## Receipts

Each line's counter-sha256 and exit refer to the frozen run. Probe identity is given above; full probe exits are included in the run transcripts below. `stopped-by` lists frozen failures, followed by probe failures where present.

```text
RECEIPT CtlCQuoteDump/pristine counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR
RECEIPT CtlCQuoteDump/verbatim counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,COPY;probe:COPY
RECEIPT CtlCQuoteDump/drop12 counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR
RECEIPT CtlCQuoteDump/halves counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR
RECEIPT CtlCQuoteDump/reportedly counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,COPY;probe:COPY
RECEIPT CtlCQuoteDump/restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR
```

## Full counter stdout and exits

Every frozen command was run from `/fast/scratch/hyaku/kotodama-r61/CtlCQuoteDump/clone`:

```sh
timeout 900 python3 -B reports/round-61/accept-c.py; echo exit=$?
```

Every probe command was run from that same clone:

```sh
timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCQuoteDump/accept-c-floor3.py; echo exit=$?
```

### Pristine / frozen

```text
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
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Pristine / probe

```text
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
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Verbatim / frozen

```text
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
COPY FAIL max=12 bad=['6:19', '7:23', '8:17']
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Verbatim / probe

```text
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
COPY FAIL max=12 bad=['6:19', '7:23', '8:17']
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Drop12 / frozen

```text
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
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Drop12 / probe

```text
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
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Halves / frozen

```text
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
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Halves / probe

```text
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
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### Reportedly / frozen

```text
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
COPY FAIL max=12 bad=['6:19', '7:23', '8:17']
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Reportedly / probe

```text
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
COPY FAIL max=12 bad=['6:19', '7:23', '8:17']
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Restored / frozen

```text
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

### Restored / probe

```text
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

## Fixture paths, hashes, restoration

All five fixture snapshots are direct children of `/fast/scratch/hyaku/kotodama-r61/CtlCQuoteDump/`; source rows and index changes are in that root's `clone/corpus/SOURCES.md` and `clone/corpus/README.md`.

| Fixture | Bytes | SHA256 |
|---|---:|---|
| pristine.md | 387 | 5ded5201c1b456550025999e4b1f1019aaf5af44d599a3600cba9203ffcb2d65 |
| verbatim.md | 485 | 3d3a4ef5ebd830e5ba815c25788f17f89948ed33899d922455602d43ada506e7 |
| drop12.md | 469 | ae79a2f12bb52028cfb32d90caf877bf2f19bfce23b878e6f751310b1e6e780c |
| halves.md | 485 | 821db79eb75f294bc192997981d3c63c08966eacf321dd7225798b4d3263f3a0 |
| reportedly.md | 518 | 8b96c1321e7540029ac9f86d61a4d0254aacb13929449c809c154582003499e8 |

The tested entry was restored to the exact **reference-fixture** bytes, not to the bare no-entry checkout. Test-support rows/index remain fixture assets; they were not mutant-dependent. A timeout-bounded `cmp pristine.md clone/corpus/knowledge/culture-material/footwear-codes-terminology.md` returned success, followed by SHA256 checks. Full restoration command stdout (cmp itself was silent):

```text
5ded5201c1b456550025999e4b1f1019aaf5af44d599a3600cba9203ffcb2d65  /fast/scratch/hyaku/kotodama-r61/CtlCQuoteDump/pristine.md
5ded5201c1b456550025999e4b1f1019aaf5af44d599a3600cba9203ffcb2d65  /fast/scratch/hyaku/kotodama-r61/CtlCQuoteDump/clone/corpus/knowledge/culture-material/footwear-codes-terminology.md
0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10  /fast/scratch/hyaku/kotodama-r61/CtlCQuoteDump/clone/reports/round-61/accept-c.py
71f91748f4e69664038d0dfbf9f80c77875c1cf652a498fea2bf8d3cf7402749  /fast/scratch/hyaku/kotodama-r61/CtlCQuoteDump/accept-c-floor3.py
a2a0275b3728444838e2b86be55af62bd2a7158b7f41770d928d98efd3fb7005  /fast/scratch/hyaku/kotodama-r61/CtlCQuoteDump/clone/corpus/SOURCES.md
34e0858a36159add1c666406fe207aef4891bc62ddc2f08080abece2d6ed3561  /fast/scratch/hyaku/kotodama-r61/CtlCQuoteDump/clone/corpus/README.md
exit=0
```

Before the mutant sequence, the entry SHA256 was also `5ded5201c1b456550025999e4b1f1019aaf5af44d599a3600cba9203ffcb2d65`; source/index hashes were the same values shown above. Before constructing the reference fixture, bare-clone SOURCES.md and README.md hashes were respectively `641115af3777359d9b42cce28a249f7ce6807df601e543b4f5a867c74d7af485` and `a7fc403cf0f2908581926515d70c5b358afb504ac132bde3e1a0987e5870352c`.

Installs/updates: none. No broader build, lint, or integration verification was performed; only the assigned live-location checks and bounded frozen/probe mutation detectors.
