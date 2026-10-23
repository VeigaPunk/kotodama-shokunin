# Round 61 W1 — CtlCSourceless

## Scope and result

- Seat: `KotodamaR61.CtlCSourceless`; assigned claim C sourceless-stub control and its two variants.
- Axes: coverage (detect false acceptance without source work), evidence fidelity, scratch isolation/restoration. No predicate or contract changed.
- Frozen revision: `78ad4b176695e9fcd490ab607cb8218e2ce62738`.
- Scratch checkout: `/fast/scratch/hyaku/kotodama-r61/CtlCSourceless/clone`.
- Detector: that checkout's `reports/round-61/accept-c.py`, SHA-256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10` (matches the assigned frozen digest).
- **NONE-MET: all three assigned fixtures returned `ACCEPT-C-61: FAIL`, exit 1.** The URL-free fixture passed all other 13 legs and failed only LOCATE, with all 22 rows reported `no-url`.
- Mutation-test classification: **INCONCLUSIVE, not killed** for each variant because the pristine pre-data baseline already fails. These are observed negative-control rejections, not a passing-baseline mutation kill.
- Pristine and restored runs both fail on the same eight legs. README and SOURCES were restored byte-for-byte; ENTRY was removed to its original absent state. Counter and detector dependencies retain their before hashes.

## Mutants, expected detector, and retained fixtures

ENTRY is `corpus/knowledge/culture-material/footwear-codes-terminology.md`.

All three fixtures add exactly that knowledge file, a matching README index row, the culture-material section count 29 → 30, the total 235 → 236, and the current footer 235/29/29/29/29/24/95 → 236/29/29/30/29/24/95. Each entry contains 22 plausible footwear bullet clauses, exactly one cited S-id on each clause; its topic field matches the index row.

| Case | Mutation | Expected rejecting leg | Observed failing legs |
|---|---|---|---|
| sourceless-stub | ENTRY cites S652–S673; SOURCES is completely unchanged | RANGE: cited rows absent | RANGE, TOPIC, LINK, COPY, LOCATE |
| source-cell-no-url | Same entry; add 22 correctly shaped S652–S673 rows with matching footwear anchors, mined status, correct opened date and used-by path, but no URL in any source cell | LOCATE: `no-url` | LOCATE only |
| outside-block-ids | Renumber both the entry citations and those 22 URL-free rows to S600–S621 | RANGE: ids outside the reserved block | RANGE, TOPIC, LINK, COPY, LOCATE |

The outside-block variant appends its synthetic rows without overwriting the existing registry rows S600–S621. Thus those ids are also duplicated; this is not an isolated test separating the two RANGE conditions. The range predicate excludes all 22 rows from its downstream targets, and LOCATE still requires 22 located rows.

Fixture inputs, all retained below `/fast/scratch/hyaku/kotodama-r61/CtlCSourceless/fixtures/`:

- `entry-in-block.md` — 1,564 bytes; SHA-256 `a31c041f172ed1e3fec9e41100315bfb1ae56de05b7b8f444742b568547cac09`.
- `entry-outside-block.md` — 1,564 bytes; SHA-256 `ce20deda2cc9367362f098f3ebf668fcc4a186bc6868fa421642419d498a0ad5`.
- `rows-no-url.md` — 7,180 bytes; SHA-256 `34c7826c567fe06571fd72b5ba49b3dfcd84ce7160e0e4bc982e59dada65ed65`.
- `rows-outside-block.md` — 7,180 bytes; SHA-256 `f2067619197b2196b66864f11245c99d182aa1259af302f77213f44874edeb90`.
- `readme.patch` — exact index/count edit recipe and fixture assembly instructions. Insert the chosen row fixture immediately before the original blank line 607 in SOURCES; never add both sets together.

No PROBE was created or run: every assigned fixture already cites 22 distinct ids against frozen FLOOR=20. Probe result and diff are therefore `n/a`; FLOOR, TOTAL, base list, counter code and detector dependencies were unchanged.

## Control receipts

Every run used this command, with cwd `/fast/scratch/hyaku/kotodama-r61/CtlCSourceless/clone`:

```sh
timeout 900 python3 -B reports/round-61/accept-c.py; echo exit=$?
```

The `exit=` value records the detector's status, not the subsequent echo's status. Full stdout for every run follows below; no output was trimmed.

```text
RECEIPT CtlCSourceless/pristine counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SWEEP,FLOOR,LINES,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCSourceless/sourceless-stub counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=RANGE,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCSourceless/source-cell-no-url counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=LOCATE
RECEIPT CtlCSourceless/outside-block-ids counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=RANGE,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCSourceless/restored counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SWEEP,FLOOR,LINES,TOPIC,LINK,COPY,LOCATE
NONE-MET CtlCSourceless/sourceless-stub fixture=entry-in-block.md+readme.patch; no SOURCES changes; no passing fixture
NONE-MET CtlCSourceless/source-cell-no-url fixture=entry-in-block.md+rows-no-url.md+readme.patch; no passing fixture
NONE-MET CtlCSourceless/outside-block-ids fixture=entry-outside-block.md+rows-outside-block.md+readme.patch; no passing fixture
```

## Full detector stdout

### Pristine — 2026-10-23 09:41 UTC

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
LOCATE FAIL located=0 cited=0 need=0 at=2026-10-23T09:41Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Sourceless stub — 2026-10-23 09:43 UTC

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=22 floor=20
RANGE FAIL bad=['S652', 'S653', 'S654', 'S655', 'S656', 'S657', 'S658', 'S659', 'S660', 'S661', 'S662', 'S663', 'S664', 'S665', 'S666', 'S667', 'S668', 'S669', 'S670', 'S671', 'S672', 'S673'] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=22 bad=[]
TOPIC FAIL rows=0 bad=[]
LINK FAIL min=3 bad=['6:no-row', '7:no-row', '8:no-row', '9:no-row', '10:no-row', '11:no-row', '12:no-row', '13:no-row', '14:no-row', '15:no-row', '16:no-row', '17:no-row', '18:no-row', '19:no-row', '20:no-row', '21:no-row', '22:no-row', '23:no-row', '24:no-row', '25:no-row', '26:no-row', '27:no-row']
COPY FAIL max=12 bad=['6:no-row', '7:no-row', '8:no-row', '9:no-row', '10:no-row', '11:no-row', '12:no-row', '13:no-row', '14:no-row', '15:no-row', '16:no-row', '17:no-row', '18:no-row', '19:no-row', '20:no-row', '21:no-row', '22:no-row', '23:no-row', '24:no-row', '25:no-row', '26:no-row', '27:no-row']
LOCATE FAIL located=0 cited=22 need=22 at=2026-10-23T09:43Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### URL-free source cells — 2026-10-23 09:44 UTC

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=22 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=22 bad=[]
TOPIC PASS rows=22 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE FAIL located=0 cited=22 need=22 at=2026-10-23T09:44Z not_located=['S652: no-url', 'S653: no-url', 'S654: no-url', 'S655: no-url', 'S656: no-url', 'S657: no-url', 'S658: no-url', 'S659: no-url', 'S660: no-url', 'S661: no-url', 'S662: no-url', 'S663: no-url', 'S664: no-url', 'S665: no-url', 'S666: no-url', 'S667: no-url', 'S668: no-url', 'S669: no-url', 'S670: no-url', 'S671: no-url', 'S672: no-url', 'S673: no-url']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Outside-block ids — 2026-10-23 09:45 UTC

```text
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=22 floor=20
RANGE FAIL bad=['S600', 'S601', 'S602', 'S603', 'S604', 'S605', 'S606', 'S607', 'S608', 'S609', 'S610', 'S611', 'S612', 'S613', 'S614', 'S615', 'S616', 'S617', 'S618', 'S619', 'S620', 'S621'] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=22 bad=[]
TOPIC FAIL rows=0 bad=[]
LINK FAIL min=3 bad=['6:no-row', '7:no-row', '8:no-row', '9:no-row', '10:no-row', '11:no-row', '12:no-row', '13:no-row', '14:no-row', '15:no-row', '16:no-row', '17:no-row', '18:no-row', '19:no-row', '20:no-row', '21:no-row', '22:no-row', '23:no-row', '24:no-row', '25:no-row', '26:no-row', '27:no-row']
COPY FAIL max=12 bad=['6:no-row', '7:no-row', '8:no-row', '9:no-row', '10:no-row', '11:no-row', '12:no-row', '13:no-row', '14:no-row', '15:no-row', '16:no-row', '17:no-row', '18:no-row', '19:no-row', '20:no-row', '21:no-row', '22:no-row', '23:no-row', '24:no-row', '25:no-row', '26:no-row', '27:no-row']
LOCATE FAIL located=0 cited=22 need=22 at=2026-10-23T09:45Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### Restored — 2026-10-23 09:46 UTC

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
exit=1
```

## Byte hashes and restoration evidence

Actual `timeout 30 sha256sum ...` readings of the mutated paths:

| State | corpus/README.md | corpus/SOURCES.md | ENTRY |
|---|---|---|---|
| pristine | `a7fc403cf0f2908581926515d70c5b358afb504ac132bde3e1a0987e5870352c` | `641115af3777359d9b42cce28a249f7ce6807df601e543b4f5a867c74d7af485` | absent |
| sourceless-stub | `1daa6be8713cca28556083e16edb895767ccaed7ef1a7a5508edecac6b369c92` | `641115af3777359d9b42cce28a249f7ce6807df601e543b4f5a867c74d7af485` | `a31c041f172ed1e3fec9e41100315bfb1ae56de05b7b8f444742b568547cac09` |
| source-cell-no-url | `1daa6be8713cca28556083e16edb895767ccaed7ef1a7a5508edecac6b369c92` | `53f744d72b5cd21fcca4fadfa09c757214faa1fa5aa0f0e8b14bba71b8a00c38` | `a31c041f172ed1e3fec9e41100315bfb1ae56de05b7b8f444742b568547cac09` |
| outside-block-ids | `1daa6be8713cca28556083e16edb895767ccaed7ef1a7a5508edecac6b369c92` | `68ce6ba66bf1f08bf201c65a3e4856d688de75ec702ce6dc68d25eda60e5d2e9` | `ce20deda2cc9367362f098f3ebf668fcc4a186bc6868fa421642419d498a0ad5` |
| restored | `a7fc403cf0f2908581926515d70c5b358afb504ac132bde3e1a0987e5870352c` | `641115af3777359d9b42cce28a249f7ce6807df601e543b4f5a867c74d7af485` | absent |

Restoration used surgical inverse edits: remove only the 22 synthetic registry rows, remove the one index row, reverse the three count edits, and delete the newly created ENTRY. The edit tool returned original snapshot tags `FA0C` (SOURCES) and `2389` (README). The explicit post-restoration hash readings above match pristine. An exact-path glob after restoration returned `Path not found` for ENTRY; the restored detector independently reported count=235, added=[], removed=[].

The following hashes were measured both before mutation and after restoration and were identical in both readings:

```text
0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10  reports/round-61/accept-c.py
cdf71cb38155712fe3fdaeefae828622761837a7ba2a12d0d00dd931ad98f53d  reports/round-61/reopen-quote.py
c98a8841f73632e09bf04c61d8dac1c37ae60a076a2f82dfe9bb90cb6b2f6f76  reports/round-61/base-knowledge-files.txt
9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3  reports/round-28/readme/sweep.py
fb915386a781b332ae4d73e6d81b2e441ad0d9cd264d8c10421b0c01cd973bd5  tools/check-source-access.py
a7fc403cf0f2908581926515d70c5b358afb504ac132bde3e1a0987e5870352c  corpus/README.md
641115af3777359d9b42cce28a249f7ce6807df601e543b4f5a867c74d7af485  corpus/SOURCES.md
```

## Bounds

- Read claims.json first, then godspeed skill, operator RULES, and relevant frozen counter/dependency sections.
- No delegation, background jobs, services, integrations, counter revisions, or other runtime invocation.
- Clone and checkout ran only in the assigned scratch namespace with GIT_DIR, GIT_WORK_TREE and GIT_INDEX_FILE unset. Every shell process was bounded by timeout (clone/checkout and detector: 900 s; hash commands: 30 s). All completed synchronously; no launched process tree remained running.
- Only this requested report was written in the lane; all mutations and retained fixtures were confined to the assigned scratch directory. No sibling or fleet source was modified.
- No external reading/fetching was needed: the in-range fixture had no source URLs, and the other fixtures had no eligible target rows. No challenge, captcha, paywall or login was encountered or passed.
- Installs/updates: none. No PDF extraction, build, lint suite, or unrelated verification was run; only the assigned bounded acceptance detector and hash/restoration evidence.
