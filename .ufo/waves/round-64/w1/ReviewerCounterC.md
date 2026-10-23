# ReviewerCounterC — claim C counter attack (accept-c.py rev1, working tree)

Scope: attack `reports/round-64/accept-c.py` in a scratch copy of the lane tree.
Scratch: `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ReviewerCounterC/` (`tree*` =
`cp -a` of the lane; lane untouched). Counter under test: working-tree rev1
(REJECTS accepts `queued`/`QUEUED-CANDIDATE:`), identical to HEAD except that leg.
Tools installed: none (git, python3, curl already present; pacman untouched).

## Verdict summary

The counter blocks the assigned do-nothing and stub controls and catches
committed harm — but it has **two demonstrated soundness/completeness defects**
(citation vacuity lets a zero-citation entry print `ACCEPT-C-64: PASS`; the
S687 APPEND exception tolerates any single-row rewrite), **one demonstrated
false-negative/soundness pair** (NOHARM diffs committed refs, not the measured
tree), plus doc/code drift on REJECTS and LIVE scope. Do-nothing also shows
RESTATE/HOSTS/LINK pass vacuously, which is expected but worth recording.

## Control 1 — do-nothing (scratch `tree`, dirty state, no round-64 lands)

Command: `cd $SCRATCH/tree && python3 -B reports/round-64/accept-c.py --root .`

```
FILE FAIL unreadable: ... No such file or directory
ROWS FAIL bad=['S718:rows=0', ...] checked=26
REJECTS FAIL bad=['S744:rows=0', ...] checked=6
ONEID FAIL bad=[] marks=[] cited_lines=0 cited_lines_tool=exit2 clean=False
RESTATE PASS bad=[] lines=0
HOSTS PASS bad=[]
LINK PASS bad=[]
APPEND FAIL missing_base_lines=0 s687_queued=False base=643 measured=643 +32=False
NOHARM FAIL diff=[]
SWEEP FAIL exit=0 topic_row=False
LIVE FAIL ... bad=['S718:no_row', ...]
ACCEPT-C-64: FAIL  (exit 1)
```

FILE/ROWS/APPEND (and REJECTS/ONEID/NOHARM/SWEEP/LIVE) correctly FAIL.
Observation: **RESTATE, HOSTS, LINK PASS vacuously on a tree with no lands** —
no leg requires a single citation or URL to exist (see D1).

## Control 2 — stub (sourceless-shaped entry + tampered copied rows)

Built in `tree`: 26 bullets `- Orbital tundra flux calibration maintains vector
lattice resonance. (S###)`; 26 rows copied from staged artifacts then tampered
(tier→`Z`, status→`copied`, LIVE-subset anchors→`"Two words only"`); 6 real
rejected rows; S687 flipped mined→queued; README row + counts bumped 237→238 /
29→30; entry committed. `main` left at `097c21d` (lane HEAD is detached, so a
plain commit never moves it — this is itself the D2(b) demonstration).

```
FILE PASS exists lines=35 h1=1 h2=1 h3=0 topic=True
ROWS FAIL bad=['S718:tier=Z','S718:status=copied','S718:quote_words=3',...]
REJECTS PASS bad=[] checked=6
ONEID PASS bad=[] marks=[] cited_lines=26 cited_lines_tool=exit0 clean=True
RESTATE FAIL bad=['line10:S718:in_order=0', ... ] lines=26
HOSTS PASS bad=[]
LINK PASS bad=[]
APPEND PASS missing_base_lines=0 s687_queued=True base=643 measured=675 +32=True
NOHARM FAIL diff=[]
SWEEP PASS exit=0 topic_row=True
LIVE FAIL bad=['S718:NOT_LOCATED quote under 8 words', ...]   (all six, instant)
ACCEPT-C-64: FAIL  (exit 1)
```

Assigned predicate holds: FILE/ONEID-shaped legs PASS; ROWS and RESTATE FAIL.
Bonus coverage: REJECTS/APPEND/SWEEP pass honestly (real reject rows, real
append, real README land); LIVE fails fast on `quote under 8 words`
(locator MIN_WORDS refusal, no network). NOHARM FAIL here is the D2 false
negative — lands existed but `main` did not point at them.

## Control 3 — NOHARM leg (`accept-c.py:360-364`)

Leg: `git -C root diff --name-only BASE main -- corpus/knowledge`,
PASS iff `diff == [ENTRY]`. Three scratch runs, same stub land:

| variant | mutation | NOHARM |
|---|---|---|
| `tree` | entry committed on detached HEAD; `main`=097c21d | **FAIL `diff=[]`** |
| `tree-harmc` | + committed harm to `language-contact.md`; `main`=harm commit | **FAIL** `diff=['…language-contact.md','…acquisition.md']` |
| `tree-harmu` | `main`=stub commit; harm appended to `language-contact.md` **uncommitted** | **PASS** `diff=['…acquisition.md']` |

So NOHARM *does* catch committed harm, but it compares refs `BASE..main`, while
FILE/ROWS/APPEND/SWEEP/LIVE all read the working tree. Consequences:

- **D2(a) uncommitted harm is invisible** — `tree-harmu` PASSes NOHARM while a
  sibling entry is corrupted on disk (soundness hole).
- **D2(b) lands not reachable from `main` produce `diff=[]` → FAIL** on a
  correct land (false negative). Lane HEAD is detached
  (`git rev-parse --abbrev-ref HEAD` → `HEAD`), so integrator commits that do
  not move `main` fail NOHARM spuriously. (CriticClaims observed the same
  'clone main' FAIL.) Fix direction for a pre-data revision: measure the
  working tree, e.g. `git diff --name-only BASE -- corpus/knowledge` plus
  `git ls-files --others --exclude-standard corpus/knowledge` — never edit the
  counter myself; recorded for the owner.

## Control 4 — SWEEP/LIVE audit

- **SWEEP** (`accept-c.py:367-383`): executes `python3 -B
  reports/round-28/readme/sweep.py` under `--root` and ANDs exit 0 with a
  substring `topic_text in row_line` check against the FIRST matching README
  row. `sweep.py` itself is a real comparator: exact topic equality per row
  (`REWRITE`/`NO_TOPIC_FIELD` mismatch classes), missing/ghost/duplicate rows,
  per-section count drift, totals line, and the dated counts footer
  (regex-verified, `sweep.py:59-116,191-194`). The counter's own
  `topic_text in row_line` check is a weaker substring test and only looks at
  `next(...)` — the first README row — but any second/false row still makes
  `sweep.py` exit nonzero, so the composite is not exploitable through that
  route (LOW residual). Verified empirically: `SWEEP PASS exit=0 topic_row=True`
  only after a complete README land (row + section count + totals + footer).
- **LIVE** (`accept-c.py:385-426`): pinned locator bytes
  (`sha256(open(LOCATOR).read())` must equal `sha256(git show BASE:LOCATOR)` —
  verified by code; the pin is resolved from `BASE` once per run since
  `LOCATOR_SHA256` is `None` in-file); subset = `S718,S723,S728,S733,S738,S743`
  (6/26, declared); per row, up to 3 locator invocations 20 s apart;
  `LOCATED` = `returncode==0` **and first stdout line startswith "LOCATED"**.
  Scope honesty caveat (MEDIUM): `reopen-quote.py:226-231` collects **all**
  URLs in the row's source cell — live URL *and* the web.archive.org capture —
  and `locate()` tries them in order, so `LOCATED` can be satisfied by the
  archived copy when the live endpoint is dead. The leg's name "LIVE"
  overstates: it proves "the recorded URL set still locates the quote," not
  "the live URL serves it." The docstring's own wording ("archived same-page
  captures remain inside each row") is arguably consistent, but the frozen
  claims predicate advertises nothing narrower — flagging for honesty, not
  claiming exploitability.
- LIVE flake observed: identical real rows passed all six LOCATED in
  `tree-vac` (~120 s), while `tree-s687` saw
  `S718/S733 NOT_LOCATED https://pmc.ncbi.nlm.nih.gov/...` — a >40 s outage
  window survived the 3×20 s retry budget on PMC hosts (the known flake the
  rev-4 comment budgets against; retry does not always rescue it).

## Control 5 (found while building) — citation vacuity, demonstrated end-to-end

`tree-vac`: **all real lands** — 26 rows (24 staged-verbatim + S740 fabricated
by me, both LOCATED-verified; S723 came from the staged artifact that landed
mid-run), 6 reject rows, S687→queued, README row/counts/footer, committed
vacuity entry that cites **zero** S-ids. Result:

```
FILE PASS ... ONEID PASS cited_lines=0 clean=True
RESTATE PASS bad=[] lines=0   HOSTS/LINK/APPEND/NOHARM/SWEEP PASS
LIVE PASS bad=[]              ACCEPT-C-64: PASS  (exit 0)
```

**D1 (HIGH):** `ONEID PASS cited_lines=0` and `RESTATE PASS lines=0` — no leg
requires the entry to cite any of S718-S743, let alone each once. The claim
statement says rows "opened this round and cited by it"; the predicate passes
with `cited_lines=0`. Fix direction: a pre-data revision requiring
`len(cited) >= 26` (or per-id coverage of NEW_IDS in `cited`), with my
`tree-vac` receipt as the forcing control.

## Control 6 — S687 APPEND exception breadth

`tree-s687`: same as `tree-vac` plus S687's anchor cell rewritten to a quote
absent from the base row (status still flipped to `queued`).
`accept-c.py:347-353` tolerates *any* single missing base line starting
`| S687 ` and separately requires *some* S687 row with `cs[7]=='queued'` —
the two are never cell-compared. Observed: **`APPEND PASS`** with the row's
anchor silently rewritten. Only the `+32` row count and the existence of a
queued S687 are enforced (MEDIUM). Fix: diff the S687 row cells, permitting
only cs[7] (and usedby if intended) to change.

## Additional findings

- **D4 (MEDIUM, doc drift):** REJECTS docstring promises "a live URL" for
  S744-S749; the leg checks only 11-cell shape, `rejected|queued` status, and
  `REJECTED:|QUEUED-CANDIDATE: ... ; flip:` in the teaches cell. A URL-less
  disposition row passes the leg.
- **D7 (LOW):** APPEND's multiset/count compare only `ROW_RE` lines
  (`^\|\s*S\d+\s*\|`); deletion or insertion of non-row lines in SOURCES.md
  (headers, comments, prose) is invisible to every leg.
- **D8 (LOW, static):** HOSTS blacklists placeholder hosts but nothing denies
  loopback/private hosts in *non*-LIVE-subset rows (the locator's
  `private-host` refusal only protects the six re-opened rows).
- **D10 (LOW, hypothetical):** LIVE executes the pinned locator by path with
  `cwd=root`; `sys.path[0]` is `reports/round-61/`, so a landed same-directory
  module could shadow its stdlib imports. Nothing in the counter forbids new
  files there (NOHARM only scopes `corpus/knowledge`).
- **Positive verifications:** FILE shape enforced; ONEID couples in-line scan
  with `tools/check-cited-lines.py` exit+`0 finding`; ROWS checks 11 cells,
  tier, status, opened, recheck, used-by, quote length, live URL and
  same-page-capture URL normalization; LINK enforces per-URL uniqueness and
  absence from the entry; APPEND enforces base multiset + exact count.

## Severity rollup

1. **HIGH D1** citation vacuity — `ACCEPT-C-64: PASS` with `cited_lines=0`
   (receipt above). The coverage claim's "cited by it" is unenforced.
2. **MEDIUM D2** NOHARM ref-vs-worktree mixing — misses uncommitted harm;
   false-fails correct lands not on `main` (both reproduced).
3. **MEDIUM D3** S687 exception tolerates any single-row rewrite (`APPEND
   PASS` with anchor cell changed).
4. **MEDIUM D4/D5** doc drift: REJECTS "live URL" unenforced; LIVE = locatable
   via live-or-archive, subset 6/26, first-line LOCATED only.
5. **LOW D7-D10** non-row registry content unprotected; private hosts in
   non-subset rows; SWEEP substring topic check (moot under sweep exit 0);
   locator path-shadowing surface.

## Residual risk / verification gaps

- LIVE flakiness is real on this network (PMC transient NOT_LOCATED observed
  while an identical tree passed 6/6); the 3×20 s retry budget did not rescue
  the window. A genuine land may need a re-run; that is operational, not a
  counter defect.
- S740 row in my green trees is fabricated-by-me (verified LOCATED twice);
  S723 came from the staged row that landed during the run. My green results
  are evidence about the *counter*, not about the seat corpus.
- No subagent dispatch (leaf member). Peers: CriticClaims ran complementary
  controls (verbatim-teaches escape → RESTATE false negative; LINK/NOHARM the
  only blocks) — corroborates D1-adjacent weakness and D2(b).

Report: `.ufo/waves/round-64/w1/ReviewerCounterC.md`
