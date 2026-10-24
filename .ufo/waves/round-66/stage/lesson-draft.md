# Round 66 lesson (kotodama, hyaku run 5) — DRAFT body

> **DRAFT — seat ScribeLessonDraft (`.ufo/waves/round-66/stage/lesson-draft.md`).**
> Not a claim record, not a receipt, not an integration. Nothing in this draft
> asserts that a routed defect is fixed: every repair statement is written as
> *"to be dispositioned by <evidence>"* and names the artifact that must carry
> the evidence at closure. Every observation below was read from disk at draft
> time (2026-10-24) at lane base `94209e8f80969dbac48d56c5d0e2e623635b8616`
> plus the untracked pre-data worktree; nothing was re-executed to decorate it.
>
> **Integration notes for the L1 (delete this block before commit):**
> 1. `## Gate` here carries only the preamble and the S776 supersession note.
>    The `- S### | live URL (capture) | date | "<quote>"` row lines are owned by
>    sibling stage drafts `stage/gate-rows.md` (S777-S800) and
>    `stage/s776-gate.md` (S776) — do not copy quotes from this file.
> 2. `ACCEPT-CA-66` leg `QUOTES` requires `corpus/lessons/round-66.md` to name
>    at least 25 distinct ids in S776-S800 and to pass `tools/check-gate-quotes.py`
>    with `0 finding`. That count must come from the real Gate rows; a bare id
>    list added to satisfy the regex would be a false stamp and is out of scope
>    for this draft.
> 3. Add the attempt history, census and counts at integration (this draft does
>    not carry them: it is a skeleton, and inventing counts would be worse than
>    the gap).

## Round summary

Kotodama round 66, base `94209e8f80969dbac48d56c5d0e2e623635b8616`, three
frozen claims (`reports/round-66/claims.json`, revision 0, written pre-wave):

- **C (coverage, sourced):** the scent / perfume / aromatics / incense register
  is unowned at base (word-bounded filename census prints 0) -> one new
  culture-material entry `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md`
  supported by exactly 24 mined registry rows S777-S800, each tier A or B,
  opened 2026-10-24, used-by the entry, cited exactly once by it.
  Predicate `ACCEPT-C-66`: every leg of `reports/round-66/accept-c.py` prints PASS.
- **O (operability):** `tools/check-claim-separability.py` returns a verdict
  inside a round's budget (`--timeout/--jobs/--budget/--max-runs/--static-only`;
  skipped runs are honest partial verdicts, exit 2, never a fabricated `<base>`).
  Predicate `ACCEPT-O-66`: every leg of `reports/round-66/accept-o.py` prints PASS.
- **Ca (calibration, records):** the round-65 closure's routed defects
  R65-D1..D4 are dispositioned in this round's records.
  Predicate `ACCEPT-CA-66`: every leg of `reports/round-66/accept-ca.py` prints PASS.

Attempt history, final counts and the census block are to be filled at
integration from the receipts, not from this draft.

## Gate

Rows opened this round: **S777-S800** (24 rows, one anchor quote per row, taken
from that row's own `row-<SID>.txt` fragment, opened 2026-10-24). Each row's
anchor quote is at most 25 words; a row whose live URL answers a bot challenge
keeps its located status through the same-page Wayback capture named in its
source cell and names the challenge in its VERIFY cell (QUALITY criteria 10 and
16 — the challenge is recorded, never bypassed). Capture cells carry a full
`https://` scheme so the frozen locator tries them (round-65 R65-M3 class), and
the `- verified-at:` head line names the rows per free text, never as a range
token such as `S777-S800` (round-65 R65-M4 class).

**S776 supersession (the round-65 R65-D1 durability repair).** S776 is a new
registry row for the Penn Museum *Expedition* 58(1) mancala article
("Sowing the Seeds of Competitive Play") that **supersedes S753** as the
games entry's mancala anchor. S753's live URL answered an HTML shell at
round-65 closure and its committed capture `20250926172224` replays 404 today
(the round-65 spot-check, §3, "disagree on durability"); S776 carries the live
PDF plus a fresh capture `20261024111013` as its durability evidence. S776's
anchor quote is the round-65 S753 anchor quote copied verbatim from
`corpus/lessons/round-65.md`'s S753 Gate line — it is not re-typed here, and
the row line itself is drafted in `stage/s776-gate.md`. At draft time the
supersession is **designed, not evidenced**: `reports/round-66/telemetry/s753-recapture.txt`
(worktree, untracked) records live `status=200 content-type=application/pdf`
and a PDF 1.6 fetch, but its CDX section is empty, it records the old capture
replaying `status=000`, and it carries no quote-verbatim line, no
`20261024111013` and no S776 mention. The supersession is therefore *to be
dispositioned by* the completed `s753-recapture.txt` receipt (quote located
verbatim + fresh capture replay), the S776 registry row, and the games entry's
mancala bullet citing `(S776)` exactly once and `(S753)` zero times —
`accept-ca.py` leg `D1` is the instrument that decides it.

Rows S777-S800 and S776's row line are integrated from the sibling stage drafts;
none of the 24 new anchoring rows is claimed located by this preamble. Each
row's locatability is to be dispositioned by the `ACCEPT-C-66` legs `ROWS`,
`RESTATE`, `CAPTURE` and the locator reopens, and by the round's blind
per-row support review.

## Mistakes

Shape (`R66-Mn`): class -> evidence pointer -> captured-by -> fix, with the fix
always phrased as *to be dispositioned by <evidence>*. Entries seeded from the
round-65 lesson's `## Mistakes` and from the round-65 closure's routed defects
R65-D1..D4; each names this round's exposure, not a claimed outcome.

- **R66-M1 (class: anchor-provenance).** Round-65 R65-M1: a seat fragment
  anchored on wording absent from the cited article while its VERIFY claimed a
  page location. This round's 24 row fragments are the same attack surface; at
  draft time `.ufo/waves/round-66/rows/` holds no fragment files at all, so no
  anchor has yet been re-opened against its source.
  **Evidence:** `.ufo/waves/round-66/rows/` (empty at draft time; `ScoutRow03/`
  is a directory with no files) and the absence of any `row-S###.txt` in the
  wave tree. **Captured-by:** `ACCEPT-C-66` leg `RESTATE` plus
  `tools/check-gate-quotes.py` (`truncated-grounds`, `doubled-locator`) at
  integration. **Fix:** to be dispositioned by the L1's preflight re-open of
  every fragment's anchor, with the re-test output recorded in that row's
  VERIFY-L1 cell and in `stage/gate-rows.md` (no Gate quote may be typed from a
  fragment's prose summary).
- **R66-M2 (class: locator-url-shape).** Round-65 R65-M3: a capture written as
  bare `web.archive.org/web/<ts>id_/...` was never tried by the frozen locator,
  which extracts only scheme-bearing URLs, so two rows read NOT_LOCATED while
  the capture itself carried the quote. **Evidence:** `corpus/lessons/round-65.md`
  R65-M3 entry; at draft time no round-66 row line exists yet to audit, and the
  fresh S776 capture id is recorded in the frozen D1 leg and claim Ca but not in
  any receipt on disk. **Captured-by:** `ACCEPT-C-66` leg `CAPTURE` (scheme and
  capture presence) and the locator's LIVE leg. **Fix:** to be dispositioned by
  the integrated registry source cells, every capture carrying `https://`, and
  by one locator smoke run over the new rows.
- **R66-M3 (class: capture-encoding).** Round-65 R65-M6 and the round-65
  spot-check both found captures stored gzip-compressed, which a raw-byte
  locator measures as quote-absent (S765's Britannica capture; S771's admitted
  capture read only after decompression). The S753 replacement is exposed to the
  same class: the fresh capture's replay is asserted by the frozen claim, not
  yet observed. **Evidence:** `corpus/lessons/round-65.md` R65-M6;
  `corpus/lessons/round-65-verifier-spotcheck.md` §3 (S771 row) and §5 item 1;
  `reports/round-66/telemetry/s753-recapture.txt` (no replay line yet).
  **Captured-by:** the `RevD1Anchor` attack seat and `accept-ca.py` leg `D1`.
  **Fix:** to be dispositioned by a `s753-recapture.txt` that records the fresh
  capture replaying 200 `application/pdf` **and** the anchor quote located after
  decoding, plus the games-entry re-point.
- **R66-M4 (class: oneid-shape).** Round-65 R65-M4: a `- verified-at:` line
  carrying the range token `S750-S775` was read by the ONEID leg as one line
  holding two S-ids. Round 66 freezes the same 24-id block as S777-S800, so the
  entry head must not repeat that token. **Evidence:** entry
  `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md` does not
  exist at draft time (checked on disk); the class is carried from
  `corpus/lessons/round-65.md` R65-M4. **Captured-by:** `ACCEPT-C-66` legs
  `ONEID` and `NOHARM`. **Fix:** to be dispositioned by the integrated entry's
  head block and the `ONEID` leg's per-id citation counts.
- **R66-M5 (class: claim-calibration).** Round-65 R65-M7: the frozen coverage
  claim's before-state was re-derived only by a pre-data attack, and the counter
  never re-derives semantic ownership; the two partial-scope hits had to be
  disclosed in the entry. Round 66's claim C has the same shape (filename census
  0, topic-line sweep finds partial mentions). **Evidence:**
  `reports/round-66/claims.json` claim C `statement` (the frozen census command
  and the "partial-scope mentions" clause) and its `review_only` list; the
  partial-owner scout artifact `w1/ScoutPartialOwners.md` (landed at draft
  time). **Captured-by:** the `RevClaimC` / `RevBaseCensus` seats and
  `AXES.md`'s falsifiable before->after rule. **Fix:** to be dispositioned by a
  pre-data re-derivation recorded against the frozen claim text — the claim is
  not to be rewritten after data, and the entry's one-way pointers to partial
  owners are to be checked, not asserted.
- **R66-M6 (class: receipt-honesty).** Round-65 R65-M8: a red full run and a
  green filtered run coexisted; only the unchanged full command could settle
  the claim, and both receipts had to be kept. Round 66 already has red pre-data
  output that must survive integration. **Evidence:**
  `reports/round-66/telemetry/dry-run-ca.txt` (all six Ca legs FAIL at base,
  `ACCEPT-CA-66: FAIL`), `dry-run-c.txt` (FILE/SET/ONEID FAIL), `dry-run-o.txt`
  (SELFTEST PASS 63/63, DIFF PASS 428 lines, OPTIONS PASS, BOUND PASS), and the three
  `controls-*.txt` do-nothing controls. **Captured-by:** the frozen predicates
  themselves (`ACCEPT-C-66/O-66/CA-66`) and the `RevReceipts` seat. **Fix:** to
  be dispositioned by the three `final-measures-*.txt` receipts produced by the
  unchanged full commands; the red dry-runs stay preserved below any re-stamp
  (QUALITY criterion 17).
- **R66-M7 (class: receipt-parent sequencing — R65-D2).** Round-65 R65-M9: the
  records commit was not a direct child of the lands commit it receipted, so the
  post-record `RECEIPTS` leg failed all three receipts. Round 66 must place the
  records commit directly on the lands commit. **Evidence:** at draft time none
  of `reports/round-66/telemetry/final-measures-{c,o,ca}.txt` exists
  (dry-run-ca leg `D2 FAIL ...:absent`), so the sequence has not yet been
  exercised. **Captured-by:** `accept-ca.py` leg `D2` (carrier commit's parent
  == stamped `measured revision`, tree + counter sha256). **Fix:** to be
  dispositioned by the three final receipts committed under the unchanged
  counters, with no interposed evidence commit between lands and records.
- **R66-M8 (class: source-durability — R65-D1).** S753's evidence pointer does
  not resolve: live URL answered an HTML shell at round-65 closure, committed
  capture `20250926172224` replays 404 while CDX lists 200 pdf. Round 66's
  declared repair is the live 200 PDF + fresh capture `20261024111013` + the
  S776 supersession row. **Evidence:** `reports/round-66/telemetry/s753-recapture.txt`
  (live `status=200 content-type=application/pdf`; empty CDX section; old
  capture `status=000`; no quote line), `dry-run-ca.txt` leg `D1 FAIL
  bad=['live_status','quote','capture_ts','s776','s776_citations=0','s753_citations=1']`
  (base bytes, receipt absent there), and
  `corpus/knowledge/culture-material/games-play-sport-contests.md:23` still
  citing `(S753)`. **Captured-by:** `accept-ca.py` leg `D1` and the
  `RevD1Anchor` / `RevengerIntent` seats. **Fix:** to be dispositioned by the
  completed recapture receipt, the S776 row with its used-by pointing at the
  games entry, and the one-for-one bullet re-point; durability is the closure's
  call, not this lesson's.
- **R66-M9 (class: dispatch-evidence — R65-D3).** Round-65 dispatched 0 L2 seats
  against the >=8 batched-seat floor and kept no per-seat last-error text. Round
  66 seeds the receipt but has not yet filled it. **Evidence:**
  `reports/round-66/telemetry/seat-evidence.txt` (header names the 64-seat
  `spec-v2.json` and the >=8 floor, then lists 64 *expected* report paths, with
  status lines deferred to integration), while `.ufo/waves/round-66/w1/` holds
  only `swarm-registry.json`, `ScoutPartialOwners.md` and two scratch trees at
  draft time; `dry-run-ca.txt` leg `D3 FAIL named=0 existing=0 min=8` (base
  bytes, receipt absent there). **Captured-by:** `accept-ca.py` leg `D3` and the
  `RevD3Evidence` / `RevWaveEvidence` seats. **Fix:** to be dispositioned by a
  `seat-evidence.txt` whose named seat reports exist on disk, each with a status
  line, and whose dead seats carry their last-error text — a prepared taskcall
  or a list of expected paths does not satisfy the floor.
- **R66-M10 (class: separability bound — R65-D4).** Round-65's
  `check-claim-separability.py` timed out at its 600 s per-run cap, leaving
  separability permanently unverified. Round 66's tool upgrade is present in
  the worktree, but no complete bounded verdict is on disk. **Evidence:** tool
  bytes at draft time expose `--jobs/--budget/--max-runs/--static-only`
  (`--help` lines 63-65; docstring 38-47); `dry-run-o.txt` prints `SELFTEST
  PASS 63/63`, `DIFF PASS diff_lines=428`, `OPTIONS PASS`, `BOUND PASS exit=2
  partial=True unresolved=True`; `controls-o.txt` extracts the base tool
  `5764ea27e8bba0c92801e2b95e58c52c349852e64729dfdd434459bd35532cc5` whose
  option surface lacks the new flags; `stage/mut-o/` holds four mutants;
  `reports/round-66/telemetry/separability-real.txt` does not exist
  (`dry-run-ca.txt` leg `D4 FAIL`). **Captured-by:** `ACCEPT-O-66` legs
  `SELFTEST/DIFF/OPTIONS/BOUND/STATIC/MAXRUNS/JOBS/MUT/FIXTURES` and
  `accept-ca.py` leg `D4`. **Fix:** to be dispositioned by
  `separability-real.txt` carrying a complete `SEPARABILITY: N findings` verdict
  and an `acceptance_runs=` count with no `PARTIAL`, produced by the bounded run
  on the round-66 manifest — a skipped run may only ever print the partial
  verdict and exit 2.

## Routed defects (round-65 closure, §5) — disposition paragraphs

One paragraph per routed defect. Each names the closure's own words, the
declared round-66 instrument, and the evidence state read at draft time. None
of the four is claimed dispositioned here.

**R65-D1 (S753 source-cell durability).** The closure asked for a repair of
S753's source cell: "re-capture the Penn Museum PDF (or cite a live-resolving
mirror/DOI); today neither the live URL nor the committed capture returns the
quoted bytes." Round 66's declared disposition is three-part: the live URL now
answers `200 application/pdf` (observed in the untracked probe
`reports/round-66/telemetry/s753-recapture.txt`, which also fetched a PDF 1.6
object), a fresh capture `20261024111013` is the new archive anchor, and a new
row **S776** supersedes S753 for the games entry's mancala bullet, which must
cite `(S776)` once and `(S753)` zero times. At draft time the probe carries no
verbatim-quote line, its CDX section is empty and it records the old capture
replaying `status=000`; the S776 row and the entry re-point are not on disk;
`corpus/QUALITY.md` still ends at criterion 17, so the durability criterion the
claim promises (18) is also absent. The defect is therefore **to be
dispositioned by** the completed `s753-recapture.txt` (quote located verbatim +
fresh capture replay), the S776 registry row, the one-for-one games-entry
re-point, and QUALITY criterion 18 — with `accept-ca.py` leg `D1` as the
deciding instrument, and the non-author `RevD1Anchor` judgment carrying the
resolvability question the leg cannot settle.

**R65-D2 (receipt sequencing).** The closure's words: records commits must be
direct children of the lands commit they receipt, and it suggested making the
receipt leg's expected lands hash the actual parent at run time. Round 66 keeps
the rule (no post-data retargeting) and declares leg `D2`: for each
`final-measures-{c,o,ca}.txt`, the commit that carries the receipt on `main`
must have the receipt's stamped `measured revision (lane main)` as its parent,
and the stamped tree and the counter's sha256 must resolve. At draft time the
three receipts do not exist (`telemetry/` holds only `dry-run-*` and
`controls-*`, all untracked), so the sequence has not been exercised;
`dry-run-ca.txt` leg `D2` records `absent` for all three. The defect is
**to be dispositioned by** the three final receipts committed directly on the
lands commit under the unchanged counters — an interposed evidence commit
between lands and records is exactly the round-65 failure this leg measures.

**R65-D3 (dispatch registry + seat-evidence receipt).** The closure required
dispatching the L2 wave or recording the refused/errored dispatch evidence, and
keeping per-seat last-error text for dead seats: a prepared taskcall does not
satisfy the >=8 batched-seat floor. Round 66 seeds
`reports/round-66/telemetry/seat-evidence.txt`, which names the 64-item
`spec-v2.json`, the 64-member `w1/swarm-registry.json` and the >=8 floor, then
lists 64 expected report paths with status lines deferred to integration; only
a handful of those files exist at draft time, so the receipt is a seed, not
evidence. The defect is **to be dispositioned by** the integrated
`seat-evidence.txt`: >=8 named seat reports that exist on disk, one status line
each, and explicit last-error lines for every dead seat — with
`accept-ca.py` leg `D3` counting named-vs-existing paths and the
`RevD3Evidence` seat reading the status lines for honesty.

**R65-D4 (bounded separability run).** The closure's words: bound
`check-claim-separability.py` so it returns a verdict inside a round, or replace
it — a 600 s timeout leaves separability permanently unverified. Round 66
declares the bounded upgrade (`--timeout` unchanged per-run, `--jobs`,
`--budget` on the whole dynamic leg, `--max-runs` per unit, `--static-only`;
every skipped run counted and printed as `SEPARABILITY_PARTIAL` with exit 2; a
skipped repair names `SEPARABILITY_UNRESOLVED`, never a fabricated `<base>`).
The worktree tool already exposes that option surface (428 diff lines against
base; `--selftest` 63/63; the `BOUND` fixture exits 2 with `partial=True
unresolved=True`; four mutants sit under `stage/mut-o/`), and the base tool's
`5764ea27…` bytes are preserved as the negative control. What does not exist is
the measurement: no `separability-real.txt` carrying a complete
`SEPARABILITY: N findings` verdict with `acceptance_runs=`. The defect is
**to be dispositioned by** that receipt, produced by the bounded run on the
round-66 manifest with no `PARTIAL` line, and by `accept-ca.py` leg `D4` — a
partial run, however fast, dispositions nothing.
