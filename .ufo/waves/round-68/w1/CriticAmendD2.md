# CriticAmendD2 — attack on the claim Ca D2 pre-data revision (round 68, w1)

Seat: critic (resumed after provider error, same identity). Date: 2026-10-24.
Scratch: `/tmp/amendd2/` (mutants `mut-*.md`, scratch lanes `lanes/`, clone fixtures `fx/F*`,
harness `harness.py`, raw outputs `mut-results2.txt`, `harness-rev1.out`).
Installs/updates: none (python3, gawk, git already present).

## Verdict (TL;DR)

1. **The revision's conclusion holds, but one step of the proof is false.** Under every
   *honest* transform, W04 = distinct_scopes − 1 per URL group, and that count does not depend
   on statuses or row order. However, the proof's §2 bullet 3 ("indented rows … vanish from
   accept-c SET/ROWS legs … not a lands state") is **wrong for base rows**. Indenting the flagged
   rows 4 spaces gives a census exit of 0, no E-lines, **0 W04**, and accept-c APPEND **passes**
   (APPEND matches `line.strip()`). SET/ROWS only cover S833–S856. So rev 0 *was* reachable,
   by blinding the census. The rev-0 counter committed at T0 scores that state **D2 PASS**
   (fixture F8, first run). Rev 1 closes this hole: F8 fails with `w04_set_delta=-[all 28]`.
   The proof text should be corrected to say "reachable only by census blinding (4-space
   indentation), which rev 1's exact-set check refuses". As written it reads "unreachable".
2. **W04_BASE is exactly correct:** the live census flags 28 ids, which equals W04_BASE.
   claims.json `W04_FLAGGED` is wrong: it lists 29 ids under the label "28" (S200 extra). S200's URL
   (kensycooperrider.com/…pdf) appears once in the registry. Frozen-set drift is confirmed, and the
   label/count error is still in the committed and working-tree claims.json.
3. **The amended D2 can fail, and it discriminates on the registry axis.** It catches a new
   cross-scope duplicate (F2), a missing ledger row (F3), an invalid ruling (F3b), census
   blinding of one or all W04 rows (F4, F8), and a benign reorder (F5, a false fail: see 6).
   **It does not discriminate settlement from no settlement:** a paper ledger with zero registry
   change passes D2 (F1). A well-formed all-`keep-split` paper ledger also passes the
   settlement tool's `--ledger` with `findings=0`.
4. **The do-nothing control fails Ca overall** (F0: D2, D3, D4, R68, QUOTES; F0b at BASE also
   D1 and SEQ). What stops a do-nothing-plus-paper-ledger lane is only R68's S833–S856 count
   (claim C's rows), D3, D4 and QUOTES. Within Ca, nothing checks that a pending chain was
   actually settled.
5. **NEW DEFECT (outside D2, same claim): R68's pending-row consistency check is dead code.**
   `c = m.group(0).split("|")[1:-1]` parses only the matched prefix `| S044 |`, which gives 1
   cell, so `len(c) != 11` and the row is skipped. All **34/34** PENDING_S rows are skipped, so
   the claim-statement clause "every pending-chain s row lands consistent with its ruling
   (activate->mined, retire->rejected, none left queued)" is **never measured**. F7 (`activate` on a
   row left `queued`) scores R68-pending clean. Fix: take the full line
   (`reg[m.start():reg.find("\n", m.start())]`) and add a mutant fixture. Also add a ledger/status
   consistency check to D2, or rely on accept-o `--ledger` plus scan `pending=0`, but then say so
   in the separability note.
6. **Robustness gaps in D2 (fail-closed, but worth fixing before data):**
   - The exact-set comparison is **order-sensitive**. Swapping S079 and S127 (both rows
     intact, still 28 W04) gives `w04_set_delta=+['S079']-['S127']` → FAIL. accept-c APPEND
     ignores order, so this is a *permitted* transform that falsely fails Ca. Compare URL
     groups/pairs (url → set of scopes, or the set of {id, sibling} pairs) instead of the id the
     census happens to print second.
   - The filter `"W04" in l` is a substring match. A W01 line whose used-by path contains `W04`
     injects that id (false FAIL). Use `ln.split("\t")[1] == "W04"`.
   - A `W04` line with an empty third field raises IndexError, which `main()` does not catch
     (traceback, exit 1). The census never emits one. Cosmetic.
7. **The revision is not committed.** `git status` shows ` M reports/round-68/accept-ca.py`,
   ` M reports/round-68/claims.json`, and `?? telemetry/w04-impossibility.txt`. The T0 commit
   c1adbdf carries rev 0 (sha256 `103fc42d…`). The working tree has rev 1 (`4ff82c5f…`). Any
   `git clone --no-local` evaluation, which is the declared protocol, measures **rev 0** until the
   revision lands as its own pre-data commit. The pre-data claim needs that commit timestamped
   before any A_r data.

**Overall: the revision is sound in direction and the amended D2 can fail (verified on 7 mutants).
Ship it after:** (a) committing it pre-data, (b) correcting proof §2/§4 (indentation reachability;
the "28" label on a 29-id W04_FLAGGED), (c) making the W04 comparison order-insensitive and the
code match exact, (d) fixing the R68 dead-code parse. Without (d), Ca's settlement-consistency
clause is unmeasured. Without (c), a benign reorder can kill a true Ca.

---

## (a) Verify the proof — registry transforms vs census validate

Mutants were built from live `corpus/SOURCES.md` (884 lines; `## Registry` at L26, `## Paths` at L788).
URL grouping (census normalization re-implemented): **28 groups, each exactly 2 rows, 2 distinct
scopes.** The W04-flagged id is always the later row of each group.

First run (mutants loose in /tmp): every mutant exited 1. This was **an artifact**: 6120 E11 lines,
because `--file` resolves the lane as `dirname(file)/..`, so used-by paths were missing. The run
was redone in scratch lanes (`/tmp/amendd2/lanes/<name>/corpus/SOURCES.md`, every other entry
symlinked to the real lane):

```
=== control === exit=0
file	ok	/tmp/amendd2/lanes/control/corpus/SOURCES.md
W04 ids: S127 S128 S129 S130 S131 S132 S133 S185 S186 S358 S482 S483 S485 S490 S561 S564 S565 S566 S569 S570 S571 S572 S573 S648 S649 S650 S651 S830
W04 count: 28
=== mut-A-flip-rejected === exit=0            # all 56 group rows -> status rejected
file	ok	/tmp/amendd2/lanes/mut-A-flip-rejected/corpus/SOURCES.md
W04 ids: S127 … S830   (identical 28)
W04 count: 28
=== mut-B-reorder === exit=0                  # each pair's two rows swapped
file	ok	/tmp/amendd2/lanes/mut-B-reorder/corpus/SOURCES.md
W04 ids: S079 S086 S094 S097 S117 S119 S122 S135 S141 S145 S147 S151 S157 S252 S256 S367 S379 S383 S392 S417 S433 S438 S440 S453 S602 S616 S623 S643
W04 count: 28
=== mut-C-indent-flagged === exit=0           # the 28 flagged rows indented 4 spaces
file	ok	/tmp/amendd2/lanes/mut-C-indent-flagged/corpus/SOURCES.md
W04 ids:
W04 count: 0
=== mut-C2-indent-sibling === exit=0          # the 28 unflagged siblings indented 4 spaces
file	ok	/tmp/amendd2/lanes/mut-C2-indent-sibling/corpus/SOURCES.md
W04 ids:
W04 count: 0
=== mut-D-append-diffscope === exit=0         # S833 = S127's URL, new scope
file	W03	S833 mined but unused
file	ok	/tmp/amendd2/lanes/mut-D-append-diffscope/corpus/SOURCES.md
W04 ids: S127 … S830 S833
W04 count: 29
=== mut-E-append-samescope === exit=1         # S833 = S127's URL + S127's scope, mined
file	E04	S833 duplicate url voices.uchicago.edu/goldinmeadowlab/people/susan-goldin-meadow/research-statement within scope the author's own summary of her homesign and gesture research
file	W03	S833 mined but unused
W04 count: 28
=== mut-E2-append-samescope-rejected === exit=0   # same, but S833 rejected
file	ok	/tmp/amendd2/lanes/mut-E2-append-samescope-rejected/corpus/SOURCES.md
W04 count: 28
=== mut-F-subsection === exit=0               # S127 moved under "### Ad-hoc subsection" inside ## Registry
file	ok	/tmp/amendd2/lanes/mut-F-subsection/corpus/SOURCES.md
W04 count: 28
=== mut-G-leaves-registry === exit=1          # S127 moved under ## Paths
file	E12	S127 row outside Registry section
W04 count: 27
```

Findings:
- Status (A), order (B), `###` subsection (F, since `###` matches neither heading regex in the census
  and stays in-registry) and same-scope appends (E/E2) do not reduce W04. Leaving the registry (G) is
  E12, exit 1. **The proof's semantics are confirmed** for every transform that keeps rows visible.
- **Indentation (C, C2) clears ALL W04 at exit 0, with no E-lines, and every base row byte-present.**
  The proof dismisses this via accept-c SET/ROWS, but those legs check only S833–S856. Base rows are
  checked by APPEND, which strips. Evidence (accept-c `append_check` on the clone fixtures,
  BASE registry as base):

```
F8: R68-pending bad=[] | R68 skipped(no col-0 match)=34 […] | accept-c APPEND ok=True bad=[]
F6: R68-pending bad=[] | R68 skipped(no col-0 match)=34 ['S044', 'S045', …] | accept-c APPEND ok=True bad=[]
```

  (F8 = all 28 W04 rows indented. F6 = S044/S045 indented.) The rev-0 counter at T0 scored F8 as
  **`D2 PASS bad=[] w04=0 census_exit=0`**, so rev 0 was gameable, not unreachable. Rev 1 kills it
  (see (c), F8).
- Proof §3 witness S094/S132: confirmed in a single group, `ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls`,
  rows S094 and S132. It is airtight only under "rows stay visible to the census".

## (b) W04_BASE accuracy

```
$ sources-census.sh validate --file corpus/SOURCES.md     # live, lane main = c1adbdf
file	W04	S127 duplicate url voices.uchicago.edu/goldinmeadowlab/people/susan-goldin-meadow/research-statement across scopes
… (28 W04 lines; full output /tmp/amendd2/live-census.out) …
file	W04	S830 duplicate url collection.sciencemuseumgroup.org.uk/objects/co122693/disease-mask-for-healing-rituals across scopes
file	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md
exit=0
--- E-line count:
0

live == W04_BASE: True
live-W04_BASE : []
W04_BASE-live : []
live == W04_FLAGGED: False
W04_FLAGGED-live: ['S200']
live-W04_FLAGGED: []
```

W04_BASE is exact. claims.json `W04_FLAGGED` says "28 census-flagged ids" but lists **29** (S200 extra).
S200's row (L229) carries a URL that occurs nowhere else. The drift is real. The counter correctly
keys on the empirical 28, but claims.json's frozen text is now internally inconsistent and should
carry an erratum in revision_note.

## (c) Do-nothing reachability and D2 discrimination

Harness: `git clone --no-local` of the lane at T0 c1adbdf, then the **working-tree rev-1** accept-ca.py and
claims.json copied in, fixture mutation, commit on `main`, run
`accept-ca.py --root <clone> --lands <HEAD>`. (In the first harness run the clones carried the
*committed* counter, which is rev 0. That run is how finding 7 surfaced.)

```
=== F0 do-nothing: T0 + rev-1 instruments commit only (no settlement, no ledger) exit=1
STAMP PASS  D1 PASS bad=[] paths=26
D2 FAIL bad=['S034:no_ledger_row', 'S038:no_ledger_row', 'S039:no_ledger_row', 'S044:no_ledger_row', 'S045:no_ledger_row', 'S046:no_ledger_row'] w04=28 census_exit=0
D3 FAIL bad=['log:no_round68_heading', 'scorecard:no_axes68', …]
D4 FAIL bad=["nonunique=['S857', 'S858']", 'r68_rejects=0'] r68_band=0
SEQ PASS  R68 FAIL bad=['S833:count', …]  CRITERION PASS  QUOTES FAIL exit=2 gate_ids=0  FIXTURES PASS
ACCEPT-CA-68: FAIL

=== F0b do-nothing at BASE (rev-1 counter, --lands BASE) exit=1
D1 FAIL bad=['path_list_absent'] paths=0
D2 FAIL bad=['S034:no_ledger_row', …] w04=28 census_exit=0
D3 FAIL …  D4 FAIL …  SEQ FAIL bad=['reports/round-68/accept-c.py:no_required_lands', …]  R68 FAIL …  QUOTES FAIL …
ACCEPT-CA-68: FAIL

=== F1 T0 + paper ledger (all keep-split), zero registry change exit=1
D1 PASS bad=[] paths=26
D2 PASS bad=[] w04=28 census_exit=0                 <-- D2 passes with no settlement
D3 FAIL …  D4 FAIL …  R68 FAIL bad=['S833:count', …]  QUOTES FAIL …
ACCEPT-CA-68: FAIL

=== F2 F1 + extra cross-scope duplicate row S833
D2 FAIL bad=["w04_set_delta=+['S833']-[]"] w04=29 census_exit=0
=== F3 F1 minus ledger row S132
D2 FAIL bad=['S132:no_ledger_row'] w04=28 census_exit=0
=== F3b F1 with S132 ruling 'pending'
D2 FAIL bad=["S132:ruling='pending'"] w04=28 census_exit=0
=== F4 F1 + S127 indented 4 spaces
D2 FAIL bad=["w04_set_delta=+[]-['S127']"] w04=27 census_exit=0
=== F5 F1 + benign reorder of pair S079/S127
D2 FAIL bad=["w04_set_delta=+['S079']-['S127']"] w04=28 census_exit=0      <-- false fail
=== F6 F1, ledger 'activate' S044/S045, rows left queued + indented
D2 PASS bad=[] w04=28 census_exit=0
=== F7 F1, ledger 'activate' S044, row left queued
D2 PASS bad=[] w04=28 census_exit=0
=== F8 F1 + all 28 W04 rows indented (rev-0 "W04-free" via blinding)
D2 FAIL bad=["w04_set_delta=+[]-['S127', 'S128', … 'S830']"] w04=0 census_exit=0
```

Rev-0 counter (committed at T0) on the same F8 state: `D2 PASS bad=[] w04=0 census_exit=0`.

The R68 leg in F6/F7 shows only `S833:count…` (the first 6 bad entries). I isolated its pending-row
half with the counter's exact logic:

```
F1: R68-pending bad=[] | R68 skipped(no col-0 match)=34 ['S044(cells=1)', 'S045(cells=1)', 'S046(cells=1)', 'S070(cells=1)'] | accept-c APPEND ok=True bad=[]
F7: R68-pending bad=[] | R68 skipped(no col-0 match)=34 ['S044(cells=1)', 'S045(cells=1)', 'S046(cells=1)', 'S070(cells=1)'] | accept-c APPEND ok=True bad=[]
```

`cells=1` on every row: accept-ca.py L288–293 parses `m.group(0)` (the regex prefix only). **Dead
check, 34/34 skipped** (finding 5).

Does the settlement tool stop a paper ledger?

```
=== tool --ledger on F1   (related='-')
LEDGER-FINDING L76:related='-'  … exit=1
=== tool --scan on F1
SETTLEMENT: pending=34 chains=47 usedby_paths=686 missing_paths=0
=== well-formed keep-split paper ledger (real partner ids + urls), zero registry change
      1 LEDGER: rows=78 findings=0
exit=0
```

Answers:
- A pure do-nothing lane fails D2 on missing ledger rows, and fails D3, D4, R68 (S833–S856 count)
  and QUOTES. At BASE it also fails D1 and SEQ. **Ca stops the do-nothing control.**
- D2 itself discriminates on the registry axis (F2, F3, F3b, F4, F8 all FAIL).
- D2 does **not** discriminate settlement: a do-nothing lane plus a 78-row `keep-split`
  ledger passes D2. In isolation that is D2's stated scope ("ruling coverage"), but nothing in Ca
  then catches it. R68's consistency half is dead, and `keep-split` exempts `queued` even when it
  is alive. The tool's `--ledger` passes the well-formed paper ledger (`findings=0`). The only stop
  is accept-o's scan `pending=0` (still 34), which is claim O's leg, not Ca's.

## (d) Smuggling and parsing

- A new cross-scope pair in S833–S858 against a base URL: caught (F2, `+['S833']`). A new pair between
  two new rows: the later row is flagged, so it is caught by the `+` delta. A new same-scope duplicate:
  E04 (exit 1) if mined, caught via `census_exit`. If rejected (mut-E2): silent, but that is not a
  cross-scope duplicate. For S833–S856 it is caught anyway by accept-c LINK.
- **Displacement smuggling:** inserting a row *above* a base pair, or reordering, changes *which* id
  the census flags. D2 then fails, so the comparison fails closed. But it is the wrong invariant
  (finding 6). A honest reorder fails Ca, and the error message names ids that did nothing wrong.
- Indentation hides rows from the census. Rev 1 catches it only when a hidden row belongs to a
  W04 group (F4/F8). Hiding a non-W04 pending s-row (F6) is invisible to D2 and to R68.
- `w04_ids` parser (verbatim logic, synthetic census lines):

```
real W04 line (lane prefix 'file')                 -> ['S127']
ok line, registry path contains W04                -> []
W01 line, used-by path contains W04                -> ['S859']     <-- substring false-positive
W03 line (no W04)                                  -> []
E11 line, path contains W04 (exit would be 1)      -> ['S860']
W04 line, lane name with spaces                    -> ['S500']
empty-third-field W04 line -> EXC IndexError('list index out of range')   (uncaught by main())
```

  The lane prefix `file` is handled correctly (the field index is tab-based). The substring filter
  gives false FAILs only, never false PASSes. Fix: `ln.split("\t")[1] == "W04"`.

## (e) Commit state of the revision

```
$ git status --short reports/round-68
 M reports/round-68/accept-ca.py
 M reports/round-68/claims.json
?? reports/round-68/telemetry/w04-impossibility.txt
$ git log --oneline -1   ->  c1adbdf round-68: declaration + instruments …
$ git show HEAD:reports/round-68/claims.json | grep -c revision_note  ->  0
sha256 working tree accept-ca.py  4ff82c5f98742ddd15310181282498447737a817f54ab94ae57cb1424c63e7f2
sha256 HEAD        accept-ca.py  103fc42dc0bc9901ee811672788b193f9022a8628b42e25d4eee1a81f68543d0
```

The pre-data status of the revision rests on an uncommitted edit. Commit it as its own commit
before any A_r settlement lands, so the round-58 precedent is git-evidenced.

## Required fixes before data (ranked)

1. Commit the revision (accept-ca.py, claims.json, w04-impossibility.txt) pre-data.
2. R68 pending check: parse the full matched line; add a mutant (`activate` + `queued` must FAIL).
3. D2: compare URL groups/pairs (order-insensitive), not the census's second-row id. Use an exact
   `W04` code match.
4. Proof: correct §2 bullet 3 (indentation reaches zero W04 under every committed leg; rev 1
   refuses it). Fix claims.json W04_FLAGGED ("28" label vs 29 ids, S200 erratum).
5. Optional: Ca should either check ledger↔status consistency in D2, or state in separability_note
   that settlement adequacy is carried only by accept-o's scan `pending=0`.
