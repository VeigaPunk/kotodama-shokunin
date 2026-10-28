# ExecGapSweep — round-77 do-nothing + gap harness (wave 1)

Seat: `ExecGapSweep` (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Lane base for this round: `211f9526800906e0c585d878d265c37e5e090c15`.
Target: build the do-nothing + gap verification harness against the DRAFT claims
(`.ufo/waves/round-77/CLAIMS-DRAFT.md`, read-only). No lane file was drafted.

## Deliverables

| path (lane-relative) | bytes | sha256 |
|---|---|---|
| `.ufo/waves/round-77/w1/stage/ExecGapSweep/run-controls.sh` | 32 787 | `42beb47bec2d42d5fb63e2a214a4c120beae97a5ec8b67c0f7d5a67b1ac29c68` |
| `.ufo/waves/round-77/w1/stage/ExecGapSweep/README.md` | 7 198 | `ca124873434827fce1923846c1edfa626c6082de85befcd05912bcc2ed5d1333` |
| `.ufo/waves/round-77/w1/stage/ExecGapSweep/selfcheck/` | 6 receipts + 1 stdout | fixture evidence for the run below |

`sha256sum run-controls.sh README.md` (cwd = the stage dir) prints those two
digests; `wc -c` gives the byte counts.

The L1 installs the script as `.ufo/waves/round-77/run-controls.sh` — the path
round 76's `freeze-set.sh` emits (`grep -n 'run-controls' .ufo/waves/round-76/freeze-set.sh`
→ `140:  _emit "$W/run-controls.sh"`).

## What the harness does

Given `--freeze/--base/--lands` (40 hex each; `--base` is derived from
`<freeze>:reports/round-77/claims.json` when omitted and a disagreeing
`--base` is refused), it:

1. validates the lane worktree (`git rev-parse --show-toplevel` == the lane),
   every revision, and `merge-base --is-ancestor <freeze> <lands>`;
2. materializes **one clone** under scratch — `git clone -q --shared <lane>
   <scratch>/clone-<tag>`, asserts `git -C <clone> rev-parse --show-toplevel`
   equals the clone *before* any git call on it, then pins `main` to the freeze
   (`checkout -q -B main <freeze>`) so the clone is the do-nothing *measured*
   revision whatever day the controls are re-run;
3. resolves each counter (clone's committed copy → lane `reports/round-77/` →
   `.ufo/waves/round-77/counters/` → the two wave-1 stage drafts), recording
   path + sha256 in the receipt;
4. runs the four controls (both counters) with `--root <clone>` and
   `HYAKU_SCRATCH=$SCRATCH SHOKUNIN_SCRATCH=$SCRATCH TMPDIR=$SCRATCH/tmp
   --work $SCRATCH/work/…`, and records argv, stdout+stderr, exit and verdict;
5. writes `controls-c.txt` / `controls-ca.txt` (default
   `<lane>/reports/round-77/telemetry`, the two names the round-77 freeze
   manifest lists) ending in `CONTROLS-C-77: PASS|FAIL controls=n/m` (m = 2 by
   default, 3 with `--scratch-refusal both`) and
   `CONTROLS-CA-77: PASS|FAIL controls=n/4`;
6. exits 0 (all expectations met) / 1 (≥1 deviation, receipts still written) /
   2 (setup error, nothing graded, no receipt).

Control expectations (all hard):

| # | shape | asserted |
|---|---|---|
| 1 | `--lands <freeze>` | exit 1, `^ACCEPT-*-77: FAIL`, ≥1 `LEG` line, `LEG FAIL ENTRIES` + `LEG FAIL ROWS` (C) / `LEG FAIL REPAIR` + `LEG FAIL ANNOTATE` (Ca), `LEG PASS FROZENCFG` + `LEG PASS STAMP` (+ `LEG PASS LEDGER` for Ca); a refusal summary (`legs=0/…`) at the freeze is a violation |
| 2 | `--lands <base>` | exit 2, 0 leg-shaped lines, output matches `/base/` |
| 3 | no `--work`, env stripped of `HYAKU_SCRATCH`/`SHOKUNIN_SCRATCH`/`TMPDIR` (bound to claim **Ca** by default; `--scratch-refusal both` adds claim C) | exit 2, 0 leg-shaped lines, output matches `/scratch\|--work\|HYAKU_SCRATCH/`, fallback dir stat'ed before/after |
| 4 | Ca without `--combined`, scratch given | exit 2, 0 leg-shaped lines, output matches `/combined/` |

Leg-shaped line = `^LEG (PASS|FAIL) [A-Z][A-Z0-9_]*$` — round 76's exact grammar
(`grep -n 'print("LEG' reports/round-76/accept-c.py` → `415: print("LEG %s %s" % …)`).
Reason matching makes an exit 2 for the *wrong* reason fail (proved below).

## Verification performed (exact commands, raw output)

1. Syntax:

```
$ sh -n run-controls.sh && echo 'syntax: ok'
syntax: ok
```

2. `shellcheck -s sh run-controls.sh` → 4 blocks, `3 SC2094` (info: read/write
   the same file in one pipeline) and `3 SC2129` (style: group redirects).
   No error or warning class:

```
$ shellcheck -s sh run-controls.sh 2>&1 | grep -c '^In '
4
$ shellcheck -s sh run-controls.sh 2>&1 | grep -o 'SC[0-9]*' | sort | uniq -c
      3 SC2094
      3 SC2129
```

3. Self-check (fixture repo + good/bad/scope stub counter pairs, entirely under
   `$SCRATCH`, no lane path touched):

```
$ TMPDIR=/fast/scratch/hyaku/kotodama-r77/ExecGapSweep/tmp sh ./run-controls.sh \
    --selftest --scratch /fast/scratch/hyaku/kotodama-r77/ExecGapSweep/sc
selfcheck fixture: base=a3ac63ba2dc8a8f673d3824a6211d5783ad3ed09 freeze=04af6b994a91111e40ef50b8cfdf9c9ae0d28a0f lands=7501b282737170a6793958c8b1e833dacba92bfb
SELFCHECK-77: PASS good=2+4 controls green (default --scratch-refusal=ca), scope=3+4 with C control 3 asserted, bad=6 violations caught (/fast/scratch/hyaku/kotodama-r77/ExecGapSweep/sc/selfcheck)
exit=0
```

   The six verdict lines, one per receipt
   (`grep -h '^CONTROLS-' selfcheck/*/*.txt`):

```
CONTROLS-C-77: PASS controls=2/2        # good stubs, default (Ca-scoped) control 3
CONTROLS-CA-77: PASS controls=4/4       # good stubs
CONTROLS-C-77: PASS controls=3/3        # good stubs, --scratch-refusal=both
CONTROLS-CA-77: PASS controls=4/4       # good stubs, --scratch-refusal=both
CONTROLS-C-77: FAIL controls=0/2        # bad stubs (constant PASS printer)
CONTROLS-CA-77: FAIL controls=0/4       # bad stubs
```

   `6` — bad-run violations = 2 (C) + 4 (Ca). Each is attributed, e.g.
   `selfcheck/out-bad/controls-c.txt:20`:

```
# control verdict: FAIL — exit=0(want 1); no-'ACCEPT-C-77: FAIL'-summary; red legs absent: ENTRIES ROWS ;
# control verdict: FAIL — exit=0(want 2); 4 LEG line(s) printed(want 0);
```

   So the harness neither passes a constant printer (control 1) nor a counter
   that answers leg lines to a refusal (controls 2–4), and the default run
   records `## control 3: skipped (--scratch-refusal=ca: …)` rather than
   silently dropping the control.

4. Setup-error paths (no receipt written):

```
$ sh ./run-controls.sh >/dev/null 2>&1; echo "no-args exit=$?"
no-args exit=2
$ sh ./run-controls.sh --freeze zzz --base 211f9526… 2>&1
run-controls.sh: --freeze must be 40 hex, got 'zzz'
exit=2
```

5. Real-lane materialization and reason attribution, against the **wave-1 stage
   drafts** (bogus freeze = the lane base, so claim 1 is *supposed* to be red;
   receipts were written to scratch only):

```
$ sh ./run-controls.sh --freeze 211f9526800906e0c585d878d265c37e5e090c15 \
    --base 21ef98c131dae5cc7a6b6b3387a4a2d56cc74962 \
    --scratch /fast/scratch/hyaku/kotodama-r77/ExecGapSweep/probe2 \
    --out /fast/scratch/hyaku/kotodama-r77/ExecGapSweep/probe2/out
exit=1
$ grep -n '^# control verdict\|^CONTROLS-' probe2/out/controls-ca.txt
32:# control verdict: FAIL — exit=1(want 2); refusal not attributed to /base/;
47:# control verdict: FAIL — exit=1(want 2); refusal not attributed to /scratch|--work|HYAKU_SCRATCH/;
59:# control verdict: FAIL — exit=1(want 2); refusal not attributed to /combined/;
61:CONTROLS-CA-77: FAIL controls=0/4
```

   That run is a *shape* check, not a verdict on the drafts: at that moment the
   Ca draft was mid-write (finding F2). It does prove the clone materialization
   path, the lane validation, the receipt grammar and the reason attribution
   work on the real repository.

6. Scratch hygiene: `grep -n '/tmp' run-controls.sh` returns 5 lines — two
   comments and three `$SCRATCH/tmp` suffixes
   (`TMPDIR="$SCRATCH/tmp"`, `mkdir -p … "$SCRATCH/tmp"`) — **no literal `/tmp`
   path**. Mutating git verbs appear only inside the fixture repo
   (`gc_at … init/add/commit`) and the harness's own clone
   (`git -C <clone> checkout -q -B main`); the lane gets `cat-file`,
   `merge-base`, `rev-parse`, `show`, `fetch` and is the clone *source* only.

## Findings against the DRAFT claims

### F1 (resolved: contract asymmetry, default `--scratch-refusal=ca`) — the two counters' missing-scratch contract differs

The claim-C draft counter **intentionally** keeps the round-76 (freeze-proven)
operator default; the claim-C claim text never binds a missing-scratch refusal.
Measured, and confirmed with the counter's owner (`ExecAdaptC-2`, in-wave IRC).
The stable anchors are the function names — **the line numbers below are from
the 22:35 probe of a file that the owner is realigning with the 13-leg claim
list, so they will move**:

* `_scratch_root` in `.ufo/waves/round-77/w1/stage/ExecAdaptC/accept-c.py`
  (`--work` → `$HYAKU_SCRATCH/kotodama-r77/counter` → operator
  `$TMPDIR/kotodama-r77/counter` → **`return os.path.join(os.sep, "fast",
  "scratch", "hyaku", "kotodama-r77", "counter")`**, at probe lines 2172-2191);
  `main` refuses only a *system* temp dir root (probe lines 2790-2794).
* `scratch_dir` in `.ufo/waves/round-77/w1/stage/ExecAdaptCa/accept-ca.py`
  (probe lines 465-478) raises `ScratchRefused("no scratch root: pass --work,
  or set $HYAKU_SCRATCH (preferred) or $TMPDIR; this counter never invents the
  system temp dir")`, and its self-test asserts `"scratch-noroot refusal"`
  (probe line 3531).

Runtime observation (module import + the function; both env cases, no
claims.json needed, nothing written):

```
$ TMPDIR=<scratch>/tmp env -u HYAKU_SCRATCH -u SHOKUNIN_SCRATCH … m._scratch_root(work=None)
C _scratch_root(work=None, no env) -> <scratch>/tmp/kotodama-r77/counter
C _forbidden_scratch(default) -> False
$ env -u HYAKU_SCRATCH -u SHOKUNIN_SCRATCH -u TMPDIR … same call
C _scratch_root(work=None, no env at all) -> /fast/scratch/hyaku/kotodama-r77/counter
```

The claim text matches the owner's reading: the refusal clause ("missing
`--combined`/`--work` refused exit 2 printing no leg line") sits in claim
**Ca**; claim C's do-nothing control names only `lands == freeze`,
`lands == base` and the junk landings. (The draft was reshaped at 22:33 while
this seat was working — the pre-22:33 version carried explicit
`Do-nothing control:` bullets, the 22:33 version folds them into the kill
rules; neither version binds the refusal to C.)

**Resolution:** control 3 defaults to the Ca-scoped shape
(`--scratch-refusal ca`), so the harness never asserts a clause a claim does
not freeze; `--scratch-refusal both` is the one-flag opt-in if the frozen C
claim names the refusal (C denominator becomes 3), and `none` drops the
control. If the L1 wants C strict, `ExecAdaptC-2` states it is a 6-line change
in `_scratch_root` (refuse instead of returning the operator default) plus the
frozen C control text; the harness already supports the graded shape.

### F2 (informational, transient) — the Ca draft was mid-write during the probe

At 22:35 the stage Ca draft raised
`NameError: name 'LANE_ROW_ID' is not defined` at `accept-ca.py:3823` (module
level), so the counter exited 1 with no leg line. The harness reported it as a
**violation of control 1** (`legs=0(nothing graded); no-'ACCEPT-CA-77: FAIL'-summary;`)
rather than passing it — the desired direction. No conclusion about the Ca
draft's behaviour is drawn from that run; wave-1 drafts are still being edited
by their own seats.

### F3 (freeze-planning) — `controls-c.txt` / `controls-ca.txt` cannot be committed *in* the freeze they name

Both receipts name the freeze revision in their first line, and their content is
a function of it. Round 76's freeze tree confirms the consequence:

```
$ git show df0f0309d61e5485bb17035d3f8791b1e6a11d40:reports/round-76/telemetry/controls-c.txt
fatal: path 'reports/round-76/telemetry/controls-c.txt' exists on disk, but not in 'df0f0309…'
$ git ls-tree --name-only df0f0309… reports/round-76/telemetry/
reports/round-76/telemetry/accept-ca-75-at-lands.txt
reports/round-76/telemetry/census-start.txt
reports/round-76/telemetry/gap-sweep.txt
reports/round-76/telemetry/selftest-c.txt
reports/round-76/telemetry/selftest-ca.txt
```

The round-77 freeze manifest lists `telemetry/{controls-c.txt,controls-ca.txt}`.
Those two names must be read as *produced immediately after the freeze* (a
post-freeze commit), not as bytes the freeze commit can carry; the `selftest-*`,
`census-start*` and `gap-sweep` receipts are the ones that genuinely pre-date it.

### F4 — the control-1 leg defaults are the legs the drafts actually print

* C red: `ENTRIES`, `ROWS` are in both the reshaped draft's 13-leg list and the
  wave-1 C counter's docstring/table (`sed -n '33,44p' …/ExecAdaptC/accept-c.py`).
* C green: default **`FROZENCFG` only**. The reshaped draft's claim-C
  after-state says "Counter must preserve the lineage legs ENTRIES, ROWS,
  REPOINTED, GATE, EVIDENCE, REJECTS, GROUND, CITEDLINES, CENSUS, SCRATCHMIRROR,
  COLLCHECK, FROZENCFG, INDEX (13 unique); exactly one INDEX" — **no `STAMP`**,
  while the wave-1 C counter's own table prints `15` legs
  (`ACCEPT-C-77: FAIL legs=0/15` in the probe) and its docstring lists `STAMP`
  and `LEDGELIST`. Asserting `STAMP` by default would therefore fail a
  legitimate freeze of the 13-leg shape; `--require-green-c 'FROZENCFG STAMP'`
  is the one-flag form for the 15-leg table.
* Ca: `REPAIR`, `ANNOTATE` red and `FROZENCFG`, `STAMP`, `LEDGER` green are all
  inside the reshaped draft's 12-leg set ("Preserve the 12-leg lineage set
  LEDGER, BASEMISMATCH, REPAIR, ANNOTATE, APPENDONLY, R1EXEMPT, NOSTUB,
  SEPARABLE, RECEIPTS, COMBINED, FROZENCFG, STAMP").

`grep -n 'Counter must preserve\|Preserve the 12-leg lineage set'
.ufo/waves/round-77/CLAIMS-DRAFT.md` → lines **21** and **29** of the 22:33 draft.

### F5 — the frozen leg list and the counters' own tables disagree in the drafts

The reshaped draft freezes 13 legs for C and 12 for Ca; the wave-1 draft
counters print 15 (C, `legs=0/15`) and carry their own tables. The counters'
LEGCOUNT rule refuses (exit 2) when the frozen `legs[]` differs from the
counter's table (round-76 contract, `accept-c.py` docstring "the counter
refuses (exit 2) when its own leg table length or ordered names differ").

**Owner response (`ExecAdaptC-2`, in-wave IRC):** the C table is being
realigned to exactly the draft's 13 names in that order (one `INDEX`, no
`STAMP`, no `LEDGELIST`/`COUNTS`/`APPENDONLY`/`RECEIPTS` as separate names —
their content folds into `FROZENCFG`, `EVIDENCE`, `ROWS`/`ENTRIES`, `GROUND`);
after that, a frozen `legs[]` that differs is a **refusal** (exit 2, no leg
line, `ACCEPT-C-77: FAIL legs=0/13`), not a graded leg. Consequences for this
harness, both already satisfied without a code change:

* `--require-green-c FROZENCFG` is the correct frozen shape (the default), and
  `STAMP` becomes an *unknown* name rather than a missing one;
* a legs[]-mismatch refusal at the freeze trips control 1 through the explicit
  `^ACCEPT-C-77: FAIL legs=0/` check (`refusal-summary-at-the-freeze`), so an
  unusable frozen config can never read as a do-nothing pass.

The wave-1 C counter file is mid-edit; no line number from it should be cited
as frozen state (see F1's caveat).

## Lane-write disclosure (corrected within the turn)

Running the harness at 22:34 without `--out` used its production default and
wrote `reports/round-77/telemetry/controls-c.txt` and `controls-ca.txt` into the
lane — outside this seat's write scope. Both were mine (their argv names
`…/ExecGapSweep/probe/clone-round77` and the harness sha256) and were deleted
immediately; the directory is back to its pre-run state:

```
$ for f in reports/round-77/telemetry/controls-c.txt reports/round-77/telemetry/controls-ca.txt; do
    grep -q 'ExecGapSweep/probe/clone-round77' "$f" && rm -f "$f" && echo "removed (mine): $f"; done
removed (mine): reports/round-77/telemetry/controls-c.txt
removed (mine): reports/round-77/telemetry/controls-ca.txt
$ ls reports/round-77/telemetry/
census-start.txt
```

Every later harness run passed `--out` into scratch. No other lane file was
written: this seat's writes are the stage dir and this report only.

## Risks / not run

* **Control 1 against a real round-77 freeze: unrun** — no round-77 freeze
  exists at wave 1 (no `reports/round-77/claims.json` anywhere). The harness's
  control 1 has been exercised only against stub counters; the real counters
  cannot be graded until the freeze carries claims.json, accept-c.py and
  accept-ca.py.
* **Controls 3/4 against the real counters: unrun** for the same reason (the
  drafts refuse earlier on the missing frozen config, so the refusal is not
  attributable to the named gap; the reason assertion is what prevents that
  from reading as a pass).
* Leg-name defaults are the frozen claims' names, not proof; see F4.
* `--lands` is recorded for the receipt and used as the Ca `--combined` default
  only. The controls themselves grade `lands == freeze` (control 1) and
  `lands == base` (control 2) per the claims' do-nothing sentences; there is no
  "real landing PASS" control in this harness — that is the acceptance
  measurement the counters themselves perform.
* Scratch used for this seat
  (`/fast/scratch/hyaku/kotodama-r77/ExecGapSweep`) was deleted after the
  receipts above were copied into
  `.ufo/waves/round-77/w1/stage/ExecGapSweep/selfcheck/`.
