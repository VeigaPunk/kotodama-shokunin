# Claim C: do-nothing, junk, all-false, copied-registry controls

Axes: skipped-work rejection; metadata discipline; source freshness; isolation and exact restoration; low-cost bounded probes.

Declaration: `1b80ee41f544d17c0410733a47a3eecac01bf25e`. Claim base: `39c9ce8a6be5e5625d8befb54df53d621a3a7929`.
Scratch parent: `/fast/scratch/hyaku/kotodama-r59/CtlDoNothingJunk59/`.
`clone/` is the unchanged declaration; `junk/`, `all-false/`, and `copied-registry/` are independent shared-object clones of that checkout. Only the three declared data files were changed in each mutation state. No counter, support registry/key, or reviewer artifact was changed.

Expected detector for every control: from its sandbox root, `timeout 900 python3 -B reports/round-59/accept-c.py`; reject skipped work with exit 1 and `ACCEPT-C-59: FAIL`.

Result: four controls rejected; **0 MEETS-COUNTER**, **0 MEETS-MECHANICAL**. SUPPORT reports missing registry and planted key for all four; SUPPORT is never the only failing leg. These are negative-control rejections, **not credited mutant kills**: the pristine declaration already fails. Mutation-test verdict for each altered fixture is **INCONCLUSIVE (baseline failure)**; no surviving mutant is asserted.

## Do-nothing

Mutant: none; declaration bytes unchanged. This is the required negative baseline.
CONTROL do-nothing | claim C | exit 1 | ACCEPT-C-59: FAIL | failing legs: [SET, SWEEP, FLOOR, LOCATE, BOILER, RELEVANCE, TOPIC, DISTINCT, SUPPORT]

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDoNothingJunk59/clone`

```sh
timeout 900 python3 -B reports/round-59/accept-c.py
```

Actual stdout:

```text
SET FAIL count=234 required=235 added=[] removed=[]
SWEEP FAIL exit=0 rows 234 files 234 missing_from_index 0 []
FLOOR FAIL cited=0 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE FAIL passing=0 cited=0 at=2026-10-23T02:44Z failing=[]
BOILER FAIL passing=0 cited=0 at=2026-10-23T02:44Z failing=[]
RELEVANCE FAIL passing=0 cited=0 at=2026-10-23T02:44Z failing=[]
TOPIC FAIL passing=0 cited=0 at=2026-10-23T02:44Z failing=[]
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT FAIL shared=[] hosts=0 need=10
SUPPORT FAIL unsupported=[] qualified_seats=[] need_seats=2 planted=[] no registry: FileNotFoundError no planted key: FileNotFoundError
ACCEPT-C-59: FAIL
```

Stderr: empty.

## Junk

Mutant: add the requested entry with 22 lorem-ipsum citation lines, add 22 well-formed 11-cell rows S600 through S621, and make the README index/header/total/footer internally consistent. Each row is mined/tier A, names the entry in used-by, has a unique URL `https://r59-junk-NN.invalid/article` (22 hosts), and quotes the 10 words `Lorem ipsum dolor sit amet consectetur adipiscing elit fixture markerNN.`. The teaches sentence is `Junk metadata has no evidentiary relationship to an invented statement.` No source was read to create these rows.
CONTROL junk | claim C | exit 1 | ACCEPT-C-59: FAIL | failing legs: [LOCATE, BOILER, RELEVANCE, TOPIC, SUPPORT]

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDoNothingJunk59/junk`

```sh
timeout 900 python3 -B reports/round-59/accept-c.py
```

Actual stdout:

```text
SET PASS count=235 required=235 added=['corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'] removed=[]
SWEEP PASS exit=0 rows 235 files 235 missing_from_index 0 []
FLOOR PASS cited=22 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE FAIL passing=0 cited=22 at=2026-10-23T02:48Z failing=['S600: https://r59-junk-00.invalid/article URLError', 'S601: https://r59-junk-01.invalid/article URLError', 'S602: https://r59-junk-02.invalid/article URLError', 'S603: https://r59-junk-03.invalid/article URLError', 'S604: https://r59-junk-04.invalid/article URLError', 'S605: https://r59-junk-05.invalid/article URLError', 'S606: https://r59-junk-06.invalid/article URLError', 'S607: https://r59-junk-07.invalid/article URLError', 'S608: https://r59-junk-08.invalid/article URLError', 'S609: https://r59-junk-09.invalid/article URLError', 'S610: https://r59-junk-10.invalid/article URLError', 'S611: https://r59-junk-11.invalid/article URLError', 'S612: https://r59-junk-12.invalid/article URLError', 'S613: https://r59-junk-13.invalid/article URLError', 'S614: https://r59-junk-14.invalid/article URLError', 'S615: https://r59-junk-15.invalid/article URLError', 'S616: https://r59-junk-16.invalid/article URLError', 'S617: https://r59-junk-17.invalid/article URLError', 'S618: https://r59-junk-18.invalid/article URLError', 'S619: https://r59-junk-19.invalid/article URLError', 'S620: https://r59-junk-20.invalid/article URLError', 'S621: https://r59-junk-21.invalid/article URLError']
BOILER FAIL passing=0 cited=22 at=2026-10-23T02:48Z failing=['S600: not-located', 'S601: not-located', 'S602: not-located', 'S603: not-located', 'S604: not-located', 'S605: not-located', 'S606: not-located', 'S607: not-located', 'S608: not-located', 'S609: not-located', 'S610: not-located', 'S611: not-located', 'S612: not-located', 'S613: not-located', 'S614: not-located', 'S615: not-located', 'S616: not-located', 'S617: not-located', 'S618: not-located', 'S619: not-located', 'S620: not-located', 'S621: not-located']
RELEVANCE FAIL passing=0 cited=22 at=2026-10-23T02:48Z failing=['S600: quote-teaches shared=[]; teaches-entry shared=[]', 'S601: quote-teaches shared=[]; teaches-entry shared=[]', 'S602: quote-teaches shared=[]; teaches-entry shared=[]', 'S603: quote-teaches shared=[]; teaches-entry shared=[]', 'S604: quote-teaches shared=[]; teaches-entry shared=[]', 'S605: quote-teaches shared=[]; teaches-entry shared=[]', 'S606: quote-teaches shared=[]; teaches-entry shared=[]', 'S607: quote-teaches shared=[]; teaches-entry shared=[]', 'S608: quote-teaches shared=[]; teaches-entry shared=[]', 'S609: quote-teaches shared=[]; teaches-entry shared=[]', 'S610: quote-teaches shared=[]; teaches-entry shared=[]', 'S611: quote-teaches shared=[]; teaches-entry shared=[]', 'S612: quote-teaches shared=[]; teaches-entry shared=[]', 'S613: quote-teaches shared=[]; teaches-entry shared=[]', 'S614: quote-teaches shared=[]; teaches-entry shared=[]', 'S615: quote-teaches shared=[]; teaches-entry shared=[]', 'S616: quote-teaches shared=[]; teaches-entry shared=[]', 'S617: quote-teaches shared=[]; teaches-entry shared=[]', 'S618: quote-teaches shared=[]; teaches-entry shared=[]', 'S619: quote-teaches shared=[]; teaches-entry shared=[]', 'S620: quote-teaches shared=[]; teaches-entry shared=[]', 'S621: quote-teaches shared=[]; teaches-entry shared=[]']
TOPIC FAIL passing=0 cited=22 at=2026-10-23T02:48Z failing=['S600: quote_hits=0 not-located', 'S601: quote_hits=0 not-located', 'S602: quote_hits=0 not-located', 'S603: quote_hits=0 not-located', 'S604: quote_hits=0 not-located', 'S605: quote_hits=0 not-located', 'S606: quote_hits=0 not-located', 'S607: quote_hits=0 not-located', 'S608: quote_hits=0 not-located', 'S609: quote_hits=0 not-located', 'S610: quote_hits=0 not-located', 'S611: quote_hits=0 not-located', 'S612: quote_hits=0 not-located', 'S613: quote_hits=0 not-located', 'S614: quote_hits=0 not-located', 'S615: quote_hits=0 not-located', 'S616: quote_hits=0 not-located', 'S617: quote_hits=0 not-located', 'S618: quote_hits=0 not-located', 'S619: quote_hits=0 not-located', 'S620: quote_hits=0 not-located', 'S621: quote_hits=0 not-located']
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT PASS shared=[] hosts=22 need=10
SUPPORT FAIL unsupported=['S600:no verdict', 'S601:no verdict', 'S602:no verdict', 'S603:no verdict', 'S604:no verdict', 'S605:no verdict', 'S606:no verdict', 'S607:no verdict', 'S608:no verdict', 'S609:no verdict', 'S610:no verdict', 'S611:no verdict', 'S612:no verdict', 'S613:no verdict', 'S614:no verdict', 'S615:no verdict', 'S616:no verdict', 'S617:no verdict', 'S618:no verdict', 'S619:no verdict', 'S620:no verdict', 'S621:no verdict'] qualified_seats=[] need_seats=2 planted=[] no registry: FileNotFoundError no planted key: FileNotFoundError
ACCEPT-C-59: FAIL
```

Stderr: empty.

## All-false

Mutant: independently recreate the junk state, but every new row is rejected/tier C, used-by is the wrong existing entry `corpus/knowledge/myth-symbol/animal-symbolism.md`, and its quote is only `fake markerNN` (2 words). The same 22 distinct junk URLs and lorem-ipsum entry are retained.
CONTROL all-false | claim C | exit 1 | ACCEPT-C-59: FAIL | failing legs: [STATUS, TIER, USEDBY, LOCATE, BOILER, RELEVANCE, TOPIC, SUPPORT]

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDoNothingJunk59/all-false`

```sh
timeout 900 python3 -B reports/round-59/accept-c.py
```

Actual stdout:

```text
SET PASS count=235 required=235 added=['corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'] removed=[]
SWEEP PASS exit=0 rows 235 files 235 missing_from_index 0 []
FLOOR PASS cited=22 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS FAIL bad=['S600:rejected', 'S601:rejected', 'S602:rejected', 'S603:rejected', 'S604:rejected', 'S605:rejected', 'S606:rejected', 'S607:rejected', 'S608:rejected', 'S609:rejected', 'S610:rejected', 'S611:rejected', 'S612:rejected', 'S613:rejected', 'S614:rejected', 'S615:rejected', 'S616:rejected', 'S617:rejected', 'S618:rejected', 'S619:rejected', 'S620:rejected', 'S621:rejected']
TIER FAIL bad=['S600:C', 'S601:C', 'S602:C', 'S603:C', 'S604:C', 'S605:C', 'S606:C', 'S607:C', 'S608:C', 'S609:C', 'S610:C', 'S611:C', 'S612:C', 'S613:C', 'S614:C', 'S615:C', 'S616:C', 'S617:C', 'S618:C', 'S619:C', 'S620:C', 'S621:C']
USEDBY FAIL bad=['S600', 'S601', 'S602', 'S603', 'S604', 'S605', 'S606', 'S607', 'S608', 'S609', 'S610', 'S611', 'S612', 'S613', 'S614', 'S615', 'S616', 'S617', 'S618', 'S619', 'S620', 'S621']
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE FAIL passing=0 cited=22 at=2026-10-23T02:48Z failing=['S600: quote under 8 words', 'S601: quote under 8 words', 'S602: quote under 8 words', 'S603: quote under 8 words', 'S604: quote under 8 words', 'S605: quote under 8 words', 'S606: quote under 8 words', 'S607: quote under 8 words', 'S608: quote under 8 words', 'S609: quote under 8 words', 'S610: quote under 8 words', 'S611: quote under 8 words', 'S612: quote under 8 words', 'S613: quote under 8 words', 'S614: quote under 8 words', 'S615: quote under 8 words', 'S616: quote under 8 words', 'S617: quote under 8 words', 'S618: quote under 8 words', 'S619: quote under 8 words', 'S620: quote under 8 words', 'S621: quote under 8 words']
BOILER FAIL passing=0 cited=22 at=2026-10-23T02:48Z failing=['S600: not-located', 'S601: not-located', 'S602: not-located', 'S603: not-located', 'S604: not-located', 'S605: not-located', 'S606: not-located', 'S607: not-located', 'S608: not-located', 'S609: not-located', 'S610: not-located', 'S611: not-located', 'S612: not-located', 'S613: not-located', 'S614: not-located', 'S615: not-located', 'S616: not-located', 'S617: not-located', 'S618: not-located', 'S619: not-located', 'S620: not-located', 'S621: not-located']
RELEVANCE FAIL passing=0 cited=22 at=2026-10-23T02:48Z failing=["S600: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S601: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S602: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S603: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S604: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S605: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S606: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S607: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S608: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S609: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S610: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S611: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S612: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S613: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S614: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S615: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S616: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S617: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S618: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S619: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S620: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']", "S621: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['marke']"]
TOPIC FAIL passing=0 cited=22 at=2026-10-23T02:48Z failing=['S600: quote_hits=0 not-located', 'S601: quote_hits=0 not-located', 'S602: quote_hits=0 not-located', 'S603: quote_hits=0 not-located', 'S604: quote_hits=0 not-located', 'S605: quote_hits=0 not-located', 'S606: quote_hits=0 not-located', 'S607: quote_hits=0 not-located', 'S608: quote_hits=0 not-located', 'S609: quote_hits=0 not-located', 'S610: quote_hits=0 not-located', 'S611: quote_hits=0 not-located', 'S612: quote_hits=0 not-located', 'S613: quote_hits=0 not-located', 'S614: quote_hits=0 not-located', 'S615: quote_hits=0 not-located', 'S616: quote_hits=0 not-located', 'S617: quote_hits=0 not-located', 'S618: quote_hits=0 not-located', 'S619: quote_hits=0 not-located', 'S620: quote_hits=0 not-located', 'S621: quote_hits=0 not-located']
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT PASS shared=[] hosts=22 need=10
SUPPORT FAIL unsupported=['S600:no verdict', 'S601:no verdict', 'S602:no verdict', 'S603:no verdict', 'S604:no verdict', 'S605:no verdict', 'S606:no verdict', 'S607:no verdict', 'S608:no verdict', 'S609:no verdict', 'S610:no verdict', 'S611:no verdict', 'S612:no verdict', 'S613:no verdict', 'S614:no verdict', 'S615:no verdict', 'S616:no verdict', 'S617:no verdict', 'S618:no verdict', 'S619:no verdict', 'S620:no verdict', 'S621:no verdict'] qualified_seats=[] need_seats=2 planted=[] no registry: FileNotFoundError no planted key: FileNotFoundError
ACCEPT-C-59: FAIL
```

Stderr: empty.

## Copied-registry

Mutant: independently create the lorem-ipsum entry and matching README, but reuse the exact existing URLs and first anchor quotes under new ids. S600 through S621 map, in order, to old rows S504, S505, S506, S507, S508, S509, S510, S511, S512, S513, S514, S515, S518, S519, S521, S522, S524, S525, S526, S527, S533, S534. New rows are mined/tier A with the right used-by and the same junk teaches sentence; their URLs span 15 hosts. This skips new sourcing and topic knowledge while preserving locatable old quotations.
CONTROL copied-registry | claim C | exit 1 | ACCEPT-C-59: FAIL | failing legs: [RELEVANCE, TOPIC, FRESH, SUPPORT]

Working directory: `/fast/scratch/hyaku/kotodama-r59/CtlDoNothingJunk59/copied-registry`

```sh
timeout 900 python3 -B reports/round-59/accept-c.py
```

Actual stdout:

```text
SET PASS count=235 required=235 added=['corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md'] removed=[]
SWEEP PASS exit=0 rows 235 files 235 missing_from_index 0 []
FLOOR PASS cited=22 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE PASS passing=22 cited=22 at=2026-10-23T02:48Z failing=[]
BOILER PASS passing=22 cited=22 at=2026-10-23T02:48Z failing=[]
RELEVANCE FAIL passing=0 cited=22 at=2026-10-23T02:48Z failing=['S600: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', 'S601: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', 'S602: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', 'S603: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', 'S604: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', "S605: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=['conse']", 'S606: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', 'S607: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', 'S608: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', 'S609: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', 'S610: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', 'S611: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', 'S612: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', 'S613: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', 'S614: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', 'S615: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', 'S616: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', 'S617: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', 'S618: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', "S619: quote-teaches shared=['evide']; teaches-entry shared=[]; quote-entry shared=[]", 'S620: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]', 'S621: quote-teaches shared=[]; teaches-entry shared=[]; quote-entry shared=[]']
TOPIC FAIL passing=0 cited=22 at=2026-10-23T02:48Z failing=['S600: quote_hits=0 function_words=5 page_hits=0 page_terms=0 need=1/2/3/2', 'S601: quote_hits=0 function_words=6 page_hits=0 page_terms=0 need=1/2/3/2', 'S602: quote_hits=0 function_words=5 page_hits=0 page_terms=0 need=1/2/3/2', 'S603: quote_hits=0 function_words=3 page_hits=0 page_terms=0 need=1/2/3/2', 'S604: quote_hits=0 function_words=3 page_hits=0 page_terms=0 need=1/2/3/2', 'S605: quote_hits=0 function_words=6 page_hits=0 page_terms=0 need=1/2/3/2', 'S606: quote_hits=0 function_words=6 page_hits=0 page_terms=0 need=1/2/3/2', 'S607: quote_hits=0 function_words=5 page_hits=0 page_terms=0 need=1/2/3/2', 'S608: quote_hits=0 function_words=5 page_hits=0 page_terms=0 need=1/2/3/2', 'S609: quote_hits=0 function_words=6 page_hits=0 page_terms=0 need=1/2/3/2', 'S610: quote_hits=0 function_words=3 page_hits=0 page_terms=0 need=1/2/3/2', 'S611: quote_hits=0 function_words=4 page_hits=0 page_terms=0 need=1/2/3/2', 'S612: quote_hits=0 function_words=4 page_hits=0 page_terms=0 need=1/2/3/2', 'S613: quote_hits=0 function_words=4 page_hits=0 page_terms=0 need=1/2/3/2', 'S614: quote_hits=0 function_words=6 page_hits=0 page_terms=0 need=1/2/3/2', 'S615: quote_hits=0 function_words=8 page_hits=0 page_terms=0 need=1/2/3/2', 'S616: quote_hits=0 function_words=7 page_hits=0 page_terms=0 need=1/2/3/2', 'S617: quote_hits=0 function_words=7 page_hits=0 page_terms=0 need=1/2/3/2', 'S618: quote_hits=0 function_words=5 page_hits=0 page_terms=0 need=1/2/3/2', 'S619: quote_hits=0 function_words=4 page_hits=0 page_terms=0 need=1/2/3/2', 'S620: quote_hits=0 function_words=8 page_hits=0 page_terms=0 need=1/2/3/2', 'S621: quote_hits=0 function_words=7 page_hits=0 page_terms=0 need=1/2/3/2']
FRESH FAIL rows_reusing_registry_urls=['S600', 'S601', 'S602', 'S603', 'S604', 'S605', 'S606', 'S607', 'S608', 'S609', 'S610', 'S611', 'S612', 'S613', 'S614', 'S615', 'S616', 'S617', 'S618', 'S619', 'S620', 'S621']
DISTINCT PASS shared=[] hosts=15 need=10
SUPPORT FAIL unsupported=['S600:no verdict', 'S601:no verdict', 'S602:no verdict', 'S603:no verdict', 'S604:no verdict', 'S605:no verdict', 'S606:no verdict', 'S607:no verdict', 'S608:no verdict', 'S609:no verdict', 'S610:no verdict', 'S611:no verdict', 'S612:no verdict', 'S613:no verdict', 'S614:no verdict', 'S615:no verdict', 'S616:no verdict', 'S617:no verdict', 'S618:no verdict', 'S619:no verdict', 'S620:no verdict', 'S621:no verdict'] qualified_seats=[] need_seats=2 planted=[] no registry: FileNotFoundError no planted key: FileNotFoundError
ACCEPT-C-59: FAIL
```

Stderr: empty.

## Pristine and restored detector receipts

Each mutation sandbox was scored once pristine before edits (02:45 UTC), once mutated (02:48 UTC), and once after exact restoration (02:49 UTC). The separate do-nothing run was at 02:44 UTC. Ten bounded counter runs total; every one exited 1. The three pristine runs printed the following identical stdout (pasted once, shared by all three runs):

Working directories: `junk/`, `all-false/`, `copied-registry/` under the scratch parent. Command in each root:

```sh
timeout 900 python3 -B reports/round-59/accept-c.py
```

```text
SET FAIL count=234 required=235 added=[] removed=[]
SWEEP FAIL exit=0 rows 234 files 234 missing_from_index 0 []
FLOOR FAIL cited=0 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE FAIL passing=0 cited=0 at=2026-10-23T02:45Z failing=[]
BOILER FAIL passing=0 cited=0 at=2026-10-23T02:45Z failing=[]
RELEVANCE FAIL passing=0 cited=0 at=2026-10-23T02:45Z failing=[]
TOPIC FAIL passing=0 cited=0 at=2026-10-23T02:45Z failing=[]
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT FAIL shared=[] hosts=0 need=10
SUPPORT FAIL unsupported=[] qualified_seats=[] need_seats=2 planted=[] no registry: FileNotFoundError no planted key: FileNotFoundError
ACCEPT-C-59: FAIL
```

Restored `junk/`; exit 1. Same command from that root:

```sh
timeout 900 python3 -B reports/round-59/accept-c.py
```

Actual stdout:

```text
SET FAIL count=234 required=235 added=[] removed=[]
SWEEP FAIL exit=0 rows 234 files 234 missing_from_index 0 []
FLOOR FAIL cited=0 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE FAIL passing=0 cited=0 at=2026-10-23T02:49Z failing=[]
BOILER FAIL passing=0 cited=0 at=2026-10-23T02:49Z failing=[]
RELEVANCE FAIL passing=0 cited=0 at=2026-10-23T02:49Z failing=[]
TOPIC FAIL passing=0 cited=0 at=2026-10-23T02:49Z failing=[]
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT FAIL shared=[] hosts=0 need=10
SUPPORT FAIL unsupported=[] qualified_seats=[] need_seats=2 planted=[] no registry: FileNotFoundError no planted key: FileNotFoundError
ACCEPT-C-59: FAIL
```

Restored `all-false/`; exit 1. Same command from that root:

```sh
timeout 900 python3 -B reports/round-59/accept-c.py
```

Actual stdout:

```text
SET FAIL count=234 required=235 added=[] removed=[]
SWEEP FAIL exit=0 rows 234 files 234 missing_from_index 0 []
FLOOR FAIL cited=0 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE FAIL passing=0 cited=0 at=2026-10-23T02:49Z failing=[]
BOILER FAIL passing=0 cited=0 at=2026-10-23T02:49Z failing=[]
RELEVANCE FAIL passing=0 cited=0 at=2026-10-23T02:49Z failing=[]
TOPIC FAIL passing=0 cited=0 at=2026-10-23T02:49Z failing=[]
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT FAIL shared=[] hosts=0 need=10
SUPPORT FAIL unsupported=[] qualified_seats=[] need_seats=2 planted=[] no registry: FileNotFoundError no planted key: FileNotFoundError
ACCEPT-C-59: FAIL
```

Restored `copied-registry/`; exit 1. Same command from that root:

```sh
timeout 900 python3 -B reports/round-59/accept-c.py
```

Actual stdout:

```text
SET FAIL count=234 required=235 added=[] removed=[]
SWEEP FAIL exit=0 rows 234 files 234 missing_from_index 0 []
FLOOR FAIL cited=0 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
TIER PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE FAIL passing=0 cited=0 at=2026-10-23T02:49Z failing=[]
BOILER FAIL passing=0 cited=0 at=2026-10-23T02:49Z failing=[]
RELEVANCE FAIL passing=0 cited=0 at=2026-10-23T02:49Z failing=[]
TOPIC FAIL passing=0 cited=0 at=2026-10-23T02:49Z failing=[]
FRESH PASS rows_reusing_registry_urls=[]
DISTINCT FAIL shared=[] hosts=0 need=10
SUPPORT FAIL unsupported=[] qualified_seats=[] need_seats=2 planted=[] no registry: FileNotFoundError no planted key: FileNotFoundError
ACCEPT-C-59: FAIL
```

## Restoration evidence (SHA-256)

The added entry was absent before each probe and was removed after it. The inserted 22-row blocks were cut out and the README's four changes were reverted. Hashes below were observed with bounded `sha256sum` commands, before mutation, during mutation, and after restoration. All three restored README/source pairs match their pristine bytes exactly; `clone/` stayed unchanged. Bounded `test ! -e` checks reported `RESTORED_ENTRY_ABSENT all four sandbox states`.

Common hashes (same in all applicable sandboxes):

| File/state | SHA-256 |
|---|---|
| README pristine and restored | `5906ec6b7f2c81e19350cffc9118158192285605baa891810d5b64fe35ec93ce` |
| SOURCES pristine and restored | `d8857dcb0d3c4afcac53d13425878d101f9ef9e231a49d986101baabd207516e` |
| README mutated | `b6f027ae838cec4197221c0b5260d89c6037d9f879ce5e62ff7dfa10cf103aff` |
| Entry mutated (all three) | `5d69cfbc50794822716e595b86db0b89c95b322d380a79d99e2ea5a3ab0f8b1c` |
| Entry pristine/restored | absent |

| Mutated SOURCES | SHA-256 |
|---|---|
| junk | `ea03f47bbef1aaf9dab368270ce1dd35a8f8ee9c1fb8935f7d7931e1c092d93b` |
| all-false | `db8b1e173d3b1e54fc1dfb90a026eb7e8b99887d88f65cc5d0d2a85712326481` |
| copied-registry | `46ff664e0ed9389bc29e2d84b19f8d7f96acc851d067a61dcc5d9b0e0608b8cf` |

Frozen behavior bytes were never edited. Initial declaration hashes and final hashes in all four sandboxes:

| Instrument | SHA-256 before = after |
|---|---|
| accept-c.py | `2d42deb5b84a06db06ec13cef49e4209f219e66b02cf4b21caa7d61a8197ea5e` |
| rowcheck.py | `d4d0b703167de4432b0fabc7188a0fbf12c7bf9b40fab1ba7838a281438d8b1e` |
| reopen-quote.py | `64e78c749b4dc334217499d7411671dbcb904f793b168bfae85dc69b68ab16f8` |

The same frozen counter rejected the restored trees with exactly the pristine failing-leg set; only the printed run time changed. All foreground detector processes completed and the synchronous worker pools joined. No background jobs or subagents were created. Tools installed/updated: none.

counter weaknesses: none found by the four assigned controls (unchanged declaration, well-formed lorem-ipsum rows, rejected/tier-C/wrong-owner/short-quote rows, and registry URL/quote recycling). Junk metadata passes structural legs and ACCESS but fails five other legs; copied-registry passes LOCATE and BOILER for all 22 rows but FRESH rejects every reused URL, with RELEVANCE, TOPIC and SUPPORT also failing. No counter redesign is triggered by these receipts. A positive-baseline kill assessment remains inconclusive because the declared pre-data tree is intentionally non-accepting.
