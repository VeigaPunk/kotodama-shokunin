# CtlCJunkLines — claim C "junk lines citing real rows" control (round 61, wave 1)

Lane revision: `78ad4b176695e9fcd490ab607cb8218e2ce62738`.
Instrument: `reports/round-61/accept-c.py`, sha256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10` (matches the
frozen counter named in the assignment/claims.json). Probe: the same file with **only** `FLOOR` changed 20 → 3
(sha256 `71f91748f4e69664038d0dfbf9f80c77875c1cf652a498fea2bf8d3cf7402749`). Diff:

```
--- clone/reports/round-61/accept-c.py
+++ accept-c-probe-FLOOR3.py
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

Sandbox: `/fast/scratch/hyaku/kotodama-r61/CtlCJunkLines/` (`clone/` at the pinned rev; `fixtureA`–`fixtureD`;
`accept-c-probe-FLOOR3.py`; `build.py`). Nothing was written into the lane except this report.

## What was built

Three REAL footwear pages were opened by ordinary GET with the frozen locator
(`python3 -B reports/round-61/reopen-quote.py URL "QUOTE"`), each `LOCATED`, exit 0, at 2026-10-23T09:43Z:

| row | URL | quote (first quoted span of the anchor cell) |
|---|---|---|
| S652 | https://en.wikipedia.org/wiki/Chopine | "Chopines were originally used as a patten , clog , or overshoe to protect shoes and dresses from mud and street soil." |
| S653 | https://en.wikipedia.org/wiki/Clog | "Welsh traditional clog maker Trefor Owen identified three main varieties of clogs: wooden upper, wooden soled and overshoes." |
| S654 | https://en.wikipedia.org/wiki/Caligae | "Caligae would have been cooler on the march than enclosed boots." |

Rows are 13 cells, `mined`, opened `2026-10-23`, used-by
`corpus/knowledge/culture-material/footwear-codes-terminology.md`; no URL of the registry below S652 is reused.
The fixture entry
`corpus/knowledge/culture-material/footwear-codes-terminology.md` carries `- topic: footwear control fixture rows for round 61`;
`corpus/README.md` gets the matching index row, `## culture-material/ (30)`, `Total knowledge entries: 236.` and the
footer `(total 236 files; directory totals 29/29/30/29/24/95)`; 235 base files + 1 entry = 236. `SWEEP` prints
`rows 236 files 236` and `missing_from_index 0 []`.

Entry lines per case (lines 5–7 of each entry; each line is a bullet with exactly one S-id):

- **A honest**: restatements of the three quotes.
- **B junk**: three identical lorem-ipsum lines, one per S-id (0 shared words).
- **C three quote words + junk**: `- lorem ipsum <word1> dolor sit amet <word2> consectetur adipiscing <word3> elit S6NN`.
- **D stop-ish**: `- shoes their made were from S652` (line 5) and `- would have been than S654` (line 7); S653 honest.

Per-line measurement with the counter's own `normalise`, `STOP`, `TOPIC_WORDS` and `longest_run`:

```
== fixtureA
 5: - Venetian women wore chopines as an overshoe, a patten over shoes to keep dresses off mud and street soil. S652
    shared=['chopines', 'dresses', 'overshoe', 'patten', 'shoes', 'soil', 'street'] n=7 longest=4 quote_topic=['chopines', 'clog', 'patten', 'shoes']
 6: - Trefor Owen sorted Welsh clogs into wooden upper, wooden soled and overshoe varieties. S653
    shared=['clogs', 'owen', 'soled', 'trefor', 'upper', 'varieties', 'welsh', 'wooden'] n=8 longest=5 quote_topic=['clog', 'clogs']
 7: - Caligae stayed cooler on the march than enclosed boots for Roman soldiers. S654
    shared=['boots', 'caligae', 'cooler', 'enclosed', 'march'] n=5 longest=7 quote_topic=['boots', 'caligae']
== fixtureB
 5: - lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor S652
    shared=[] n=0 longest=0 quote_topic=['chopines', 'clog', 'patten', 'shoes']
 6: - lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor S653
    shared=[] n=0 longest=0 quote_topic=['clog', 'clogs']
 7: - lorem ipsum dolor sit amet consectetur adipiscing elit sed do eiusmod tempor S654
    shared=[] n=0 longest=0 quote_topic=['boots', 'caligae']
== fixtureC
 5: - lorem ipsum chopines dolor sit amet patten consectetur adipiscing shoes elit S652
    shared=['chopines', 'patten', 'shoes'] n=3 longest=1 quote_topic=['chopines', 'clog', 'patten', 'shoes']
 6: - lorem ipsum trefor dolor sit amet owen consectetur clogs adipiscing elit S653
    shared=['clogs', 'owen', 'trefor'] n=3 longest=1 quote_topic=['clog', 'clogs']
 7: - lorem ipsum caligae dolor sit amet cooler consectetur boots adipiscing elit S654
    shared=['boots', 'caligae', 'cooler'] n=3 longest=1 quote_topic=['boots', 'caligae']
== fixtureD
 5: - shoes their made were from S652
    shared=['shoes'] n=1 longest=1 quote_topic=['chopines', 'clog', 'patten', 'shoes']
 6: - Trefor Owen sorted Welsh clogs into wooden upper, wooden soled and overshoe varieties. S653
    shared=['clogs', 'owen', 'soled', 'trefor', 'upper', 'varieties', 'welsh', 'wooden'] n=8 longest=5 quote_topic=['clog', 'clogs']
 7: - would have been than S654
    shared=[] n=0 longest=3 quote_topic=['boots', 'caligae']
```

## Runs — full stdout and exit codes

### base: do-nothing, `clone/` (no entry, no rows) — frozen counter

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
LOCATE FAIL located=0 cited=0 need=0 at=2026-10-23T09:41Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### fixtureA — honest lines — frozen

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
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:43Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### fixtureA — honest lines — probe (FLOOR 3)

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
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:43Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### fixtureB — lorem-ipsum lines, 0 shared words — frozen

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
LINK FAIL min=3 bad=['5:0', '6:0', '7:0']
COPY PASS max=12 bad=[]
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:43Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### fixtureB — lorem-ipsum lines — probe (FLOOR 3)

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
LINK FAIL min=3 bad=['5:0', '6:0', '7:0']
COPY PASS max=12 bad=[]
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:43Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### fixtureC — three quote words + lorem junk — frozen

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
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:43Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### fixtureC — three quote words + lorem junk — probe (FLOOR 3)

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
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:43Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### fixtureD — stop-ish words only — frozen

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
LINK FAIL min=3 bad=['5:1', '7:0']
COPY PASS max=12 bad=[]
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:43Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### fixtureD — stop-ish words only — probe (FLOOR 3)

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
LINK FAIL min=3 bad=['5:1', '7:0']
COPY PASS max=12 bad=[]
LOCATE PASS located=3 cited=3 need=3 at=2026-10-23T09:43Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

## Receipts

```
RECEIPT CtlCJunkLines/base-do-nothing counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=SET,SWEEP,FLOOR,LINES,TOPIC,LINK,COPY,LOCATE
RECEIPT CtlCJunkLines/A-honest counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR
RECEIPT CtlCJunkLines/B-lorem-0-shared counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LINK
RECEIPT CtlCJunkLines/C-three-quote-words-plus-junk counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR
RECEIPT CtlCJunkLines/D-stop-ish-only counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,LINK
```

Probe runs used `fixture?/reports/round-61/accept-c-probe.py`, sha256
`71f91748f4e69664038d0dfbf9f80c77875c1cf652a498fea2bf8d3cf7402749`; each fixture's frozen copy is
`0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`.

## Verdicts

```
VERDICT CtlCJunkLines/junk-lines-citing-real-rows CONTROL-MET fixture=/fast/scratch/hyaku/kotodama-r61/CtlCJunkLines/fixtureC
VERDICT CtlCJunkLines/lorem-only-lines NONE-MET fixture=/fast/scratch/hyaku/kotodama-r61/CtlCJunkLines/fixtureB
VERDICT CtlCJunkLines/three-stop-ish-words-only NONE-MET fixture=/fast/scratch/hyaku/kotodama-r61/CtlCJunkLines/fixtureD
VERDICT CtlCJunkLines/base-do-nothing NONE-MET fixture=/fast/scratch/hyaku/kotodama-r61/CtlCJunkLines/clone
```

Cheapest junk that still passes LINK: **three distinct quote content words of ≥4 characters, scattered in
lorem ipsum so no two are adjacent** (fixture C). LINK counts `{chopines, patten, shoes}`, `{clogs, owen, trefor}`,
`{caligae, cooler, boots}` — exactly 3 each — and COPY sees a longest run of 1, so both LINK and COPY PASS. Under
the probe (FLOOR 20 → 3, the only change) the whole frozen counter prints `ACCEPT-C-61: PASS`, exit 0. The
frozen counter itself is not met by any 3-row fixture because FLOOR=20; reaching frozen PASS would require the
20-row sourced payload, which is claim C's own work, not a cheap fixture.

The stop-ish line does **not** pass: `- shoes their made were from S652` shares only `shoes` after STOP
(`their`/`made` are not in the quote; `were`/`from` are STOP) → LINK 1; `- would have been than S654` shares
four quote words that are all STOP → LINK 0 (longest run 3, COPY passes). Zero-shared lorem lines fail LINK 0.
So the filter is exactly: ≥3 distinct content words, with STOP and the 4-character floor applied.

## Risks and notes

- LINK is a lexical floor, not a restatement test. Fixture C shows an entry whose every line is lorem ipsum plus
  three quote words passes LINES/LINK/COPY and, with FLOOR met, the whole frozen counter. claims.json already
  puts "whether each line's wording beyond the shared words is carried by its cited page" in review-only; the
  reviewer must read the real entry's lines against their quotes, because the counter cannot reject this shape.
- The frozen counter's only guard against fixture C is FLOOR=20, i.e. quantity, not clause quality. Raising
  LINK_MIN/COPY after the counter's first run on the claimed object would violate the frozen-predicate rule;
  this seat recommends no counter change, only the review read.
- The fixture rows are tier-C Wikipedia pages used as control data only; they are not acceptable as claim-C
  source rows. Real rows must be judged on their own tier/scope.
- LOCATE was live at 2026-10-23T09:43Z; all three quotes located on their own URLs. Fixture entry/rows/README
  edits exist only in the sandbox copies under `/fast/scratch/hyaku/kotodama-r61/CtlCJunkLines/`.
- No tools were installed or updated. No process trees were left running (all runs bounded by `timeout`).
