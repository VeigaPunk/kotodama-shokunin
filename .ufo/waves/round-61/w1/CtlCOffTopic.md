# CtlCOffTopic — pre-data control for claim C, leg TOPIC

Seat: KotodamaR61.CtlCOffTopic (leaf executor). Scope: off-topic rows control for ACCEPT-C-61,
target leg TOPIC. Lane revision measured: `78ad4b176695e9fcd490ab607cb8218e2ce62738` (my clone,
`sweep` baseline verified before building). No lane file was modified except this report; no git/jj
write ran in the lane or the fleet repo; no install or update was made (nothing needed).

## Files changed

- Lane: this report only (`/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-61/w1/CtlCOffTopic.md`).
- Scratch (all fixtures): `/fast/scratch/hyaku/kotodama-r61/CtlCOffTopic/`
  - `clone/` — `git clone` + `checkout 78ad4b176695e9fcd490ab607cb8218e2ce62738`
  - `mine.py` — candidate-quote miner (uses the locator's own `fetch`/`to_text`/`normalise`)
  - `build.py` — reproducible fixture generator (writes ENTRY, 4 SOURCES rows, README index/totals,
    probe copy)
  - `fixtureA/`, `fixtureB/` — one copy of the clone each, at the pinned rev, with the fixture
    applied; `fixtureA/frozen-rerun.txt`, `fixtureA/probe.txt`, `fixtureB/frozen-b.txt`,
    `fixtureB/probe-b.txt` hold the exact stdout pasted below

## What the control does

Two fixtures, each a 236-file tree (base 235 knowledge files + `ENTRY`) with the README index,
section count, totals line and counts footer bumped so legs SET/SWEEP can pass, and four new
`corpus/SOURCES.md` rows S652-S655 (`status=mined`, `opened=2026-10-23`, `used-by=ENTRY`, one live
URL each, 13 cells), cited by four bullet lines in
`corpus/knowledge/culture-material/footwear-codes-terminology.md`. The only counter change is the
sanctioned probe: `FLOOR 20 -> 4` (diff below, one hunk, nothing else).

- **fixtureA — off-topic, no footwear-lexicon word.** Real pages, real located quotes: Golden Gate
  Bridge (engineering leadership), American robin (daily activity), US income tax (taxable
  entities), Mount Vesuvius (79 AD eruption). Every quote verified LOCATED live; every anchor quote
  carries no word of TOPIC_WORDS.
- **fixtureB — off-topic with a footwear word in passing (the cheap defeat).** American robin
  ("…sexed on the **sole** basis of plumage" = only), Booting ("the term **boot** has been used in
  this sense since at least 1958" = computing startup), Sole proprietorship ("a **sole**
  proprietorship…" = business-law adjective), Trunk (car) ("front and **boot**…" = car trunk).
  Four different non-footwear senses of two lexicon words; all four located live.

Both fixtures' entry lines restate their quote (>=3 shared 4+ letter words, no run over 12 words),
so LINK/COPY/LOCATE measure real numbers rather than being vacuous.

## Receipts

Counter hashes: frozen = `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10`
(unchanged), probe = `c8adae2c366332908a9e9e710f1963e8c18fdc2b00d952289a6a22b58ccd4a9f`
(identical in both fixtures; `sha256sum` of both printed in the runs below).

Capture note: my first paste of the fixtureA frozen block dropped a `PASS ` token from the COPY
line. I re-captured all four runs to files listed above (same commands, same fixture bytes, only
the LOCATE timestamp moved from 09:44/09:45Z to 09:46Z) and paste those exact bytes. Every leg's
PASS/FAIL and both exit codes are identical to the first runs, including the frozen FAIL on both
fixtures; nothing was re-run to look for a pass.

Probe diff (`diff -u reports/round-61/accept-c.py reports/round-61/accept-c.probe.py`):

```
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

### fixtureA, frozen counter — `cd fixtureA && python3 -B reports/round-61/accept-c.py`

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
TOPIC FAIL rows=4 bad=['S652', 'S653', 'S654', 'S655']
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=4 cited=4 need=4 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
```

exit=1

### fixtureA, probe (FLOOR=4) — `python3 -B reports/round-61/accept-c.probe.py`

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
TOPIC FAIL rows=4 bad=['S652', 'S653', 'S654', 'S655']
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=4 cited=4 need=4 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
```

exit=1

### fixtureB, frozen counter — same command in `fixtureB`

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
LOCATE PASS located=4 cited=4 need=4 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
```

exit=1

### fixtureB, probe (FLOOR=4)

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
LOCATE PASS located=4 cited=4 need=4 at=2026-10-23T09:46Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
```

exit=0

RECEIPT CtlCOffTopic/offtopic-nofootwear counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=FAIL stopped-by=FLOOR,TOPIC (frozen); TOPIC (probe; probe counter-sha256=c8adae2c366332908a9e9e710f1963e8c18fdc2b00d952289a6a22b58ccd4a9f exit=1)
RECEIPT CtlCOffTopic/offtopic-passingfootwear counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=PASS stopped-by=FLOOR (frozen); none (probe; probe counter-sha256=c8adae2c366332908a9e9e710f1963e8c18fdc2b00d952289a6a22b58ccd4a9f exit=0)

VERDICT TOPIC on off-topic rows with no footwear word: NONE-MET — fixtureA is stopped by TOPIC
(and only by FLOOR+TOPIC under the frozen counter, TOPIC alone under the probe). The leg does the
work the claim names for this control.
VERDICT TOPIC on off-topic rows carrying a passing footwear word: CONTROL-MET — fixtureB passes
the whole counter under the probe with only FLOOR changed (13/13 legs PASS, exit 0), and under the
frozen counter fails only FLOOR (20 > 4).

## Mechanism (observed, not inferred)

TOPIC is `set(locator.normalise(anchor_quote).split()) & TOPIC_WORDS` on the first double-quoted
span of the row's anchor cell. It never reads the page body, the article title, the entry line, or
the `teaches` cell. Any token in the lexicon satisfies it, including homonyms and other senses.
fixtureB proves four of them at once: `sole` = "only", `sole` = the business-law adjective,
`boot` = computing startup, `boot` = the car trunk. The fixtureB entry line for S652 even replaces
`sole` with `only` ("…cannot be accurately sexed **only** on the basis of plumage") — the entry
text states the ordinary sense and TOPIC still passes.

## Build note (defect caught, honest record)

The first build of fixtureA put "control rows S652-S655" in the entry head block. The frozen
counter caught it immediately; the full stdout of that defective run was:

```
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR FAIL cited=4 floor=20
RANGE FAIL bad=[] range_notation=['S652-S655']
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES FAIL cited_lines=5 bad=['4:S652,S655']
TOPIC FAIL rows=4 bad=['S652', 'S653', 'S654', 'S655']
LINK FAIL min=3 bad=['4:no-row']
COPY FAIL max=12 bad=['4:no-row']
LOCATE PASS located=4 cited=4 need=4 at=2026-10-23T09:44Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
```

so RANGE and LINES fire on an S-id range in a non-cited line, and LINK/COPY cascade on the same
line because a range is not a row. I fixed the fixture (head block now carries no S-id) and
rebuilt; the receipts above are the cleaned fixtures. The defective run is not scored.

## Retained evidence (exact)

- Quote location, run in `clone/` with the frozen locator
  (`python3 -B reports/round-61/reopen-quote.py URL QUOTE`, exit 0 = LOCATED):
  - A: Golden Gate Bridge 0 LOCATED; American robin 0 LOCATED; Income tax in the United States 0
    LOCATED; Mount Vesuvius 0 LOCATED.
  - B: American robin ("sole basis") 0 LOCATED; Booting ("term boot") 0 LOCATED; Sole
    proprietorship 0 LOCATED; Trunk (car) ("front and boot") 0 LOCATED.
  - Refused alternative: the sentence beginning "the Golden Gate Bridge is described…" returned
    `NOT_LOCATED … url-reflects-quote` (three quote words appear in the article URL). Replaced with
    the Strauss sentence, which located.
- Base-tree baselines at the pinned rev (before fixtures): `reports/round-28/readme/sweep.py`
  prints `rows 235 files 235`, `missing_from_index 0 []`, `footer_ok True`, exit 0;
  `tools/check-source-access.py` prints `ACCESS: 2 flagged rows, 0 findings`, exit 0. The
  "2 flagged rows" line in every fixture run is therefore pre-existing registry state, not
  produced by these fixtures.
- Fixture diffs vs the clone: SOURCES.md gains exactly four rows after S651; README.md gains one
  index row, `## culture-material/ (29) -> (30)`, `Total knowledge entries: 235. -> 236.`,
  `(total 235 files; directory totals 29/29/29/29/24/95). -> (total 236 files; directory totals
  29/29/30/29/24/95).`; ENTRY is the single added knowledge file; accept-c.probe.py is the frozen
  counter with FLOOR only.
- Entry/SOURCES rows are in `build.py` (verbatim quotes, one per row); fixtures are reproducible
  by `python3 -B /fast/scratch/hyaku/kotodama-r61/CtlCOffTopic/build.py`.

## Risks and limits

- Both fixtures cite 4 rows, so under the frozen counter FLOOR (20) still fails; the CONTROL-MET
  verdict rests on the sanctioned probe with only FLOOR changed, as the receipt rules allow. A
  frozen-PASS off-topic fixture would need 20 rows. Not built inside the 25-minute box; the cheap
  route exists and is visible in the mined output: the Booting article alone yielded 50 candidate
  8-25-word sentences containing `boot`, so 20 distinct rows on one URL (distinct quotes; FRESH
  compares URLs against rows *below* S652 only) would very likely pass the frozen counter on a
  purely computing entry.
- LOCATE is live and time-stamped 2026-10-23T09:46Z; Wikipedia article text can change, so the
  fixture quotes are pinned to that run, not to a permanent capture.
- The fixtures are full copies of the clone (2 x 185 MB) under `/fast/scratch`; they are scratch
  and must not be merged. Nothing in them is proposed as lane content.
- For the real claim C, the practical reading: TOPIC is a cheap token filter, not a subject test.
  An entry built from genuine footwear sources will pass it trivially; the leg does not protect
  against a homonym-built packet, so the topical quality of S652-S699 remains a review-only
  judgement, exactly as `claims.json` separates it.
- No blockers. No process left running (all runs were `timeout`-capped and synchronous).
