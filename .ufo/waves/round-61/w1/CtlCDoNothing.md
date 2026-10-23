# CtlCDoNothing — round 61 wave 1 pre-data control

## Scope, axes and detector

- Target axis: **coverage**, claim C. Detector discrimination and exact restoration are guardrails; this report does not judge or admit the round or claim O.
- Read `reports/round-61/claims.json` first. All scratch clones checked out revision `78ad4b176695e9fcd490ab607cb8218e2ce62738`, with `GIT_DIR`, `GIT_WORK_TREE` and `GIT_INDEX_FILE` unset for clone/checkout.
- Scratch root: `/fast/scratch/hyaku/kotodama-r61/CtlCDoNothing/`.
- Exact reconstructible fixture contents: `/fast/scratch/hyaku/kotodama-r61/CtlCDoNothing/fixtures.json`. Clones were restored after measurement rather than left mutated.
- Every scored run used its own clone's frozen counter: `timeout 900 python3 -B reports/round-61/accept-c.py`, cwd the fixture root below.
- Counter SHA-256 throughout: `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.
- Frozen predicate: **ACCEPT-C-61: every leg above prints PASS.** No probe was made: FLOOR stayed 20, TOTAL stayed 236, the base list and all counter code stayed unchanged.
- Defect challenged: records, an index promise, or an empty file substitute for the required sourced footwear knowledge. Expected detector result: FAIL, not a coverage gain.

## Fixtures and results

All fixture roots below are under the scratch root.

| Case | Fixture root | Deliberate change | Observed stopping legs | Result |
|---|---|---|---|---|
| a-unchanged | `clone/` | None | SET, SWEEP, FLOOR, LINES, TOPIC, LINK, COPY, LOCATE | FAIL, exit 1 |
| b-records | `records/clone/` | Append a synthetic coverage SCORECARD row and LOG entry; create `corpus/lessons/round-61.md`; no entry, index or source changes | SET, SWEEP, FLOOR, LINES, TOPIC, LINK, COPY, LOCATE | FAIL, exit 1 |
| c-index-only | `index-only/clone/` | Case b plus a culture-material README row naming the absent entry; no count bumps | SET, SWEEP, FLOOR, LINES, TOPIC, LINK, COPY, LOCATE | FAIL, exit 1 |
| d-empty-entry | `empty-entry/clone/` | Exactly zero-byte entry, its README row, culture-material header 29→30, totals 235→236 and footer vector 29/29/29/29/24/95→29/29/30/29/24/95; records left pristine | SWEEP, FLOOR, LINES, TOPIC, LINK, COPY, LOCATE | FAIL, exit 1 |
| d-plus-records (supplementary) | `empty-entry/clone/` | The empty-entry fixture plus case b's records; scored first, then restored before exact case d | SWEEP, FLOOR, LINES, TOPIC, LINK, COPY, LOCATE | FAIL, exit 1 |

The empty file satisfies SET but not SWEEP: its sweep subprocess exits 1 even with 236 rows and 236 files. Every fixture has zero cited ids. RANGE, STATUS, OPENED, USEDBY and FRESH passing on zero rows is not evidence of sourced coverage. ACCESS reports the existing `2 flagged rows, 0 findings` and passes. LOCATE has no cited target to fetch.

**Mutation verdict: INCONCLUSIVE**, not killed or survived, because all pristine baselines already fail. Separately, the requested negative-control result is **NONE-MET**: no cheap fixture obtains frozen PASS. The extra cumulative empty variant is disclosed and retained in the recipe; it is not a counter revision or a narrowed predicate.

## Control receipts

```text
RECEIPT CtlCDoNothing/a-unchanged counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SWEEP,FLOOR,LINES,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCDoNothing/b-pristine counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SWEEP,FLOOR,LINES,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCDoNothing/c-pristine counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SWEEP,FLOOR,LINES,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCDoNothing/d-pristine counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SWEEP,FLOOR,LINES,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCDoNothing/b-records counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SWEEP,FLOOR,LINES,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCDoNothing/c-index-only counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SWEEP,FLOOR,LINES,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCDoNothing/d-plus-records counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=SWEEP,FLOOR,LINES,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCDoNothing/b-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SWEEP,FLOOR,LINES,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCDoNothing/c-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SWEEP,FLOOR,LINES,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCDoNothing/d-plus-records-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SWEEP,FLOOR,LINES,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCDoNothing/d-empty-entry counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=SWEEP,FLOOR,LINES,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCDoNothing/d-restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SWEEP,FLOOR,LINES,TOPIC,LINK,COPY,LOCATE
NONE-MET CtlCDoNothing/a-unchanged fixture=/fast/scratch/hyaku/kotodama-r61/CtlCDoNothing/fixtures.json#a-unchanged
NONE-MET CtlCDoNothing/b-records fixture=/fast/scratch/hyaku/kotodama-r61/CtlCDoNothing/fixtures.json#b-records
NONE-MET CtlCDoNothing/c-index-only fixture=/fast/scratch/hyaku/kotodama-r61/CtlCDoNothing/fixtures.json#c-index-only
NONE-MET CtlCDoNothing/d-empty-entry fixture=/fast/scratch/hyaku/kotodama-r61/CtlCDoNothing/fixtures.json#d-empty-entry
NONE-MET CtlCDoNothing/d-plus-records fixture=/fast/scratch/hyaku/kotodama-r61/CtlCDoNothing/fixtures.json#d-plus-records
```

## Full stdout and observed exit codes

These are all 12 counter runs, without filtering or omitted legs. Exit codes are the process exit statuses reported by the tool, not verdicts inferred from the last line.

### a-unchanged — cwd `clone/`

```text
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
LOCATE FAIL located=0 cited=0 need=0 at=2026-10-23T09:42Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
```
exit=1

### b-pristine — cwd `records/clone/`

```text
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
LOCATE FAIL located=0 cited=0 need=0 at=2026-10-23T09:42Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
```
exit=1

### c-pristine — cwd `index-only/clone/`

```text
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
LOCATE FAIL located=0 cited=0 need=0 at=2026-10-23T09:42Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
```
exit=1

### d-pristine — cwd `empty-entry/clone/`

```text
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
LOCATE FAIL located=0 cited=0 need=0 at=2026-10-23T09:42Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
```
exit=1

### b-records — cwd `records/clone/`

```text
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
LOCATE FAIL located=0 cited=0 need=0 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
```
exit=1

### c-index-only — cwd `index-only/clone/`

```text
SET FAIL count=235 required=236 added=[] removed=[]
SWEEP FAIL exit=1 rows 236 files 235 missing_from_index 0 []
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
LOCATE FAIL located=0 cited=0 need=0 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
```
exit=1

### d-plus-records — cwd `empty-entry/clone/`

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP FAIL exit=1 rows 236 files 236 missing_from_index 0 []
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
LOCATE FAIL located=0 cited=0 need=0 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
```
exit=1

### b-restored — cwd `records/clone/`

```text
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
LOCATE FAIL located=0 cited=0 need=0 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
```
exit=1

### c-restored — cwd `index-only/clone/`

```text
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
LOCATE FAIL located=0 cited=0 need=0 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
```
exit=1

### d-plus-records-restored — cwd `empty-entry/clone/`

This also supplies the immediately preceding pristine state for exact case d.

```text
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
LOCATE FAIL located=0 cited=0 need=0 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
```
exit=1

### d-empty-entry — cwd `empty-entry/clone/`

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP FAIL exit=1 rows 236 files 236 missing_from_index 0 []
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
LOCATE FAIL located=0 cited=0 need=0 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
```
exit=1

### d-restored — cwd `empty-entry/clone/`

```text
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
LOCATE FAIL located=0 cited=0 need=0 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
```
exit=1

## Before / mutated / restored hashes

The following pristine hashes were measured before mutation and re-measured equal after restoration in every affected clone. The untouched `clone/` also retained its original counter, SCORECARD, LOG and README digests.

```text
0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10  reports/round-61/accept-c.py
d581797e07f505b6c17f53c8e5b122e70608fb97153ef69c97feed927af7ca9e  SCORECARD.md
f449e878dfbbc848f20c55beb74df0a1cfeb7468fe8cac5cdeb920b212f6f695  LOG.md
a7fc403cf0f2908581926515d70c5b358afb504ac132bde3e1a0987e5870352c  corpus/README.md
641115af3777359d9b42cce28a249f7ce6807df601e543b4f5a867c74d7af485  corpus/SOURCES.md
```

Mutated hashes measured before restoration:

| Cases | File | SHA-256 while mutated |
|---|---|---|
| b, c, d-plus-records | SCORECARD.md | `f6ee20b8cfb1500912812ae3f882be4702f1bd68b1475e30fb078ca5bf5503e8` |
| b, c, d-plus-records | LOG.md | `f65f882405322bf20e5b15c07dd2e1ef9af196caa2b45950e5f12f09152bc795` |
| b, c, d-plus-records | corpus/lessons/round-61.md | `ae9f2e1c47e08b83a55404d8b2571b640d4691bcabe374c095313259358dd917` |
| b | corpus/README.md (unchanged) | `a7fc403cf0f2908581926515d70c5b358afb504ac132bde3e1a0987e5870352c` |
| c | corpus/README.md | `3ba04e6a1598058794c92af17ccf8a3051f06b92b2aa4f9c0fe3e6d12a4d842b` |
| d, d-plus-records | corpus/README.md | `915b8efb73e00f9757db79f1a67f565d048efd723b995529cdbb41109f2b769a` |
| d, d-plus-records | corpus/knowledge/culture-material/footwear-codes-terminology.md | `e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855` |
| exact d | SCORECARD.md (unchanged) | `d581797e07f505b6c17f53c8e5b122e70608fb97153ef69c97feed927af7ca9e` |
| exact d | LOG.md (unchanged) | `f449e878dfbbc848f20c55beb74df0a1cfeb7468fe8cac5cdeb920b212f6f695` |

The lesson and entry paths were absent initially. The new lessons were removed in all three mutated clones; the empty entry was removed after both empty-entry variants. The edit tool recorded all removals, and a subsequent exact-path glob returned those additions not found. The final exact-d restoration also recorded entry deletion and the restored hashes above. `wc -c` measured the supplementary empty entry as exactly `0` bytes; both variants used empty-content writes and had the empty-file SHA-256.

The frozen counter and source registry retained the hashes above while mutated and restored. No new source rows, fetched source material or counter/probe edits were introduced.

## Bounds and handoff

No installs or tool updates. No delegation, background jobs, services, git/jj writes in the lane/fleet, commits, integration or other runtime invocation. All processes launched here were bounded by explicit timeout (maximum 900 seconds) and completed; no running job/tree remains from this probe. All scratch-written files were below 5 MB and stayed under the assigned scratch root. The only lane write by this seat is this report, filed once. No claim-C build or claim-O measurement was performed.
