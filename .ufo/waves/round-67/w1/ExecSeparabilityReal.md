# ExecSeparabilityReal — round-67 separability manifest + measured verdict (w1)

Seat: executor, real (non-static) run of `tools/check-claim-separability.py` over a
round-67 manifest built from the frozen declarations in
`reports/round-67/claims.json` at base `ad5b52b0ab5691358cd38718ab75649dc9916f9a`
(lane tip at run time `b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21`, 0 tracked dirty files).

## Deliverables

- `.ufo/waves/round-67/stage/separability-manifest.json` — schema
  `kotodama-separability-manifest-v1`, base `ad5b52b0…`, 4 units (C, O, Ca claims +
  REC record), shape copied from `reports/round-66/telemetry/separability-manifest.json`.
- This report (complete verdict block below, ready to file verbatim at
  `reports/round-67/telemetry/separability-real.txt`; the lane write rule for this seat
  is `.ufo/waves/round-67/` only, so filing is L1's copy).

No tool installs or upgrades (python3 + git sufficed; pacman guard untouched).

## Command and verdict

The briefed command fails outright — the frozen tool takes the manifest as a
**positional** argument, not `--manifest`:

```
$ python3 -B tools/check-claim-separability.py --manifest <manifest> --jobs 4 --budget 240
check-claim-separability.py: error: unrecognized arguments: --manifest      (exit 2)
```

The equivalent positional invocation was run:

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
$ python3 -B tools/check-claim-separability.py \
    .ufo/waves/round-67/stage/separability-manifest.json --jobs 4 --budget 240
```

Complete stdout (verbatim), exit **1**, wall 2.26 s:

```
SEPARABILITY_DEPENDENCY C-><base> via acceptance ['python3', '-B', 'reports/round-67/accept-c.py', '--root', '.', '--lands', 'ad5b52b0ab5691358cd38718ab75649dc9916f9a'] fails on base+C.lands (rc=1) and no declared unit's lands repairs it
SEPARABILITY_DEPENDENCY Ca-><base> via acceptance ['python3', '-B', 'reports/round-67/accept-ca.py', '--root', '.', '--lands', 'ad5b52b0ab5691358cd38718ab75649dc9916f9a'] fails on base+Ca.lands (rc=1) and no declared unit's lands repairs it
SEPARABILITY_DEPENDENCY Ca->C via land path 'reports/round-67/accept-c.py' named at reports/round-67/accept-ca.py:63
SEPARABILITY_DEPENDENCY Ca->O via land path 'reports/round-67/accept-o.py' named at reports/round-67/accept-ca.py:64
SEPARABILITY_DEPENDENCY Ca->O via land path 'tools/check-receipt-seq.py' named at reports/round-67/accept-ca.py:37
SEPARABILITY_DEPENDENCY O-><base> via acceptance ['python3', '-B', 'reports/round-67/accept-o.py', '--root', '.', '--lands', 'ad5b52b0ab5691358cd38718ab75649dc9916f9a'] fails on base+O.lands (rc=1) and no declared unit's lands repairs it
SEPARABILITY_OVERLAP C/Ca corpus/SOURCES.md
SEPARABILITY: 7 findings
```

stderr: `SEPARABILITY_NOTE units=4 ordered_pairs=12 acceptance_runs=12 skipped=0`
(not partial: 0 skipped; all 12 runs executed — 3 initial + 9 repair attempts).

Determinism check: `--jobs 1` reproduces the same stdout and stderr byte-for-byte
(`diff` clean, both exit 1), so the verdict is order-parallel-invariant.

## Finding classes (expected vs unexpected)

Expected record-dependency class — **confirmed** (Ca reads the other claims' carriers):

| finding | carrier named at | class |
|---|---|---|
| `Ca->C` | `reports/round-67/accept-c.py:63` (`COUNTERS` list) | Ca's SEQ leg reads C's counter source |
| `Ca->O` | `reports/round-67/accept-o.py:64` (`COUNTERS` list) | Ca's SEQ leg reads O's counter source |
| `Ca->O` | `tools/check-receipt-seq.py:37` (`SEQ_TOOL`) | Ca's SEQ leg runs O's tool |

Expected class, not cross-claim coupling — 3 × `X-><base>` (C, O, Ca). Each counter
returns rc=1 at the base counterfactual with `--lands ad5b52b0` because STAMP finds
`evaluated=b78f8b8e != stamped=ad5b52b0`:

```
$ python3 -B reports/round-67/accept-c.py --root . --lands ad5b52b0…
STAMP FAIL stamped=ad5b52b0 evaluated=b78f8b8e equal=False tree=de353b04 dirty_tracked=False
ACCEPT-C-67: FAIL                                                              (rc=1)
```

No unit's lands repairs it, so `<base>` is the correct conclusion. This is the
frozen-predicate control semantics (counter must reject base bytes) expressed through
the dynamic leg; it is *not* evidence of undeclared coupling between claims. The
`<base>` head is also structurally unavoidable pre-integration: the receipt protocol
stamps a real lands commit and the checker's counterfactual tree is base+overlays with
no such commit, so STAMP can never pass by construction.

Unexpected coupling — **1 finding, declaration-level**:

- `SEPARABILITY_OVERLAP C/Ca corpus/SOURCES.md`. Both claims declare the same
  pre-existing registry file in their frozen `lands` arrays (`claims.json` C and Ca).
  The checker reports identical paths as overlap, never as a dependency, so this is not
  in the named expected class (`Ca->C/O counters`, `Ca->REC lands`) yet is real
  coupling: C appends S805-S828 rows to the registry that Ca's D2 leg reads through
  `sources-census.sh validate` and whose E12/E11 defects Ca repairs, and Ca's D4 leg
  reads the S801-S804 rows in the same table. Neither claim is independently landable
  against this file without the other's bytes, and (see below) a single merged tree
  cannot satisfy both at all.

### Sequencing coupling C↔Ca (design finding; L1-ruled satisfiable in order, never simultaneously)

The overlap is not only an ordering preference — the two frozen counters cap the same
registry id space in opposite directions:

- `reports/round-67/accept-c.py:67` `NEW_IDS = S805..S828`, `:70`
  `EXTRA_IDS = {S801..S804}`, and APPEND's `allowed_new` union (`:357`) makes any
  appended registry id outside those 28 print `extra=[...]` → `APPEND FAIL`.
- `reports/round-67/accept-ca.py:68` `R66_REJECTS = S801..S804` and `:230-231` require
  `rej_opened_today >= len(R66_REJECTS) + 2` (six today-dated `rejected` rows).

Base census (read-only, `git show ad5b52b0…:corpus/SOURCES.md`): **724** registry rows
and **0** rows with `status=rejected, opened=2026-10-24` (awk over the 11-cell rows
printed nothing). So no single tree satisfies both predicates: Ca needs two today-dated
rejects beyond S801-S804, and C's APPEND rejects exactly those ids. L1 resolved this
in-wave with **no counter/claims revision**, by per-claim lands commits:
A_r (S801-S804 + r66 dispositions) < A_c (S805-S828 only; C's receipt evaluated inside
a clone at A_c, evaluated==stamped==A_c) < A_ca (adds S829+ rejects + the round-67
lesson; Ca's receipt at A_ca). Joint satisfiability is therefore **sequence-dependent**
— a stronger coupling than the shared file, and the reason the SOURCES.md overlap is
load-bearing rather than cosmetic. (Also noted: `claims.json`'s C statement parenthetical
"728 + 24" disagrees with the measured base census of 724 rows; 724 + 28 = 752 matches
the stated 752 target, so the row arithmetic is right and only the parenthetical is off.)

Consequence for this instrument: the checker's dynamic leg materializes *one* tree per
run (base plus one or more units' overlays) and each acceptance argv carries a single
`--lands`, so the A_r < A_c < A_ca ordering is inexpressible. The dynamic leg is blind
to this class by construction — the static overlap is its only trace. The
post-integration re-run must evaluate C at A_c and Ca at A_ca in separate clones (two
manifest passes or per-unit `tree` revisions), never one merged tree: a merged tree
either STAMP-fails for both or evaluates bytes that neither receipt stamps.

Ca->REC — **declared but not evaluable at this snapshot** (record-dependency class,
absence-forced, not a miss). Ca's script names three record carriers that do not exist
yet:

```
reports/round-67/accept-ca.py:55  MANIFEST = "reports/round-67/dispositions/r66-wave-evidence-manifest.txt"
reports/round-67/accept-ca.py:60  LESSON   = "corpus/lessons/round-67.md"
reports/round-67/accept-ca.py:15  reports/round-67/telemetry/post-records.txt
```

Including any of them (or the declared directory lands) makes the run unverdictable, so
exclusion from the manifest was forced, not chosen. Demonstrated with throwaway
manifests via process substitution (no file written):

```
unit Ca lands 'corpus/lessons/round-67.md', which is absent from the worktree …   (exit 2)
unit Ca lands '.ufo/waves/round-66', which is not a regular file or symlink …     (exit 2)
```

The manifest therefore names a REC record unit carrying the seven round-67 records that
*do* exist (`claims.json` + the three control receipts + the three dry-run receipts);
the static leg cannot yield `Ca->REC` from those paths because accept-ca.py does not
name them. Post-integration the Ca->REC findings should appear for LESSON and MANIFEST
(both literals are in Ca's added lines), plus a second declared overlap
`C/Ca corpus/lessons/round-67.md`.

Static-leg semantics worth knowing when reading the verdict:
`Unit.name_paths()` counts only land paths **absent at base** (checker lines 388-392),
so a pre-existing shared file can only express coupling as `SEPARABILITY_OVERLAP`; the
counter-direction `C->Ca` (accept-c.py names `corpus/SOURCES.md` at its line 64) is
invisible by design, not a detector gap I can widen from this seat.

## Manifest fidelity table (declared lands → represented)

| unit | declared in `claims.json` | in manifest | excluded and why |
|---|---|---|---|
| C | entry, SOURCES.md, README.md, lessons/round-67.md, accept-c.py | SOURCES.md, README.md, accept-c.py | entry + lessons absent from the worktree (build drafts not integrated) |
| O | check-receipt-seq.py, `.ufo/waves/round-67/stage/mut-o/`, accept-o.py | tool + the 5 mutant sources (dir expanded) + accept-o.py | none; the declared dir is not representable as a lands entry |
| Ca | dispositions manifest, `.ufo/waves/round-66/`, SOURCES.md, QUALITY.md, lessons/round-67.md, LOG.md, SCORECARD.md, accept-ca.py | SOURCES.md, QUALITY.md, LOG.md, SCORECARD.md, accept-ca.py | manifest + lessons absent; `.ufo/waves/round-66/` is a directory |
| REC | (not in claims.json; record unit) | claims.json + 6 telemetry receipts | post-records carriers absent pre-integration |

Acceptance argv carries `--lands ad5b52b0…` because the checker runs each acceptance in
a `git clone --shared` checked out at base plus overlays; base is the only revision the
sandbox tree can honestly claim to measure.

## Attack finding (receipt protocol, reproduced)

The STAMP leg binds `git rev-parse main` — a ref — while every counter reads the
filesystem, and `dirty_tracked` uses `git status --porcelain --untracked-files=no`
(`accept-c.py:184,205`; `accept-o.py:139,157`; `accept-ca.py` has no dirty probe at
all). Consequence: **untracked bytes are evaluated and are invisible to the stamp.**
Reproduced in a scratch clone at `b78f8b8…` (no lane mutation):

```
$ git clone --shared … && git -C c checkout --detach b78f8b8…
$ printf '# Fabricated entry\n\n- topic: untracked bytes not in the lands tree\n' \
    > c/corpus/knowledge/culture-material/medicine-healing-codes.md
dirty_tracked_lines=0
fatal: path 'corpus/knowledge/culture-material/medicine-healing-codes.md' exists on disk,
       but not in 'b78f8b8…'                       # absent from the lands tree
STAMP PASS stamped=b78f8b8e evaluated=b78f8b8e equal=True tree=e5bf3a7e dirty_tracked=False
FILE PASS exists lines=3 h1=1 h2=0 h3=0 topic=True
```

So `STAMP PASS` + `FILE PASS` are both obtainable for an entry that does not exist in
the stamped tree. This is the same family as R66-D3 (a receipt whose truth depends on
something the receipt does not pin), not a separability defect: a `--root` that is not a
materialized lands clone passes STAMP. Advisory, not implemented (outside my write
scope): add a lands-tree membership leg for every filesystem-read path
(`git cat-file -e <lands>:<path>`) and fail STAMP on any non-empty
`git status --porcelain` including untracked files; add the missing dirty probe to
accept-ca.py. Note the frozen Ca SEQ leg only asserts headers + `stamped==evaluated`,
so this class is not currently caught by any r67 leg.

## Verdict summary

- `SEPARABILITY: 7 findings`, exit 1, `skipped=0` — complete (not partial), reproducible
  under `--jobs 1` and `--jobs 4`.
- 3 of 7 are the declared `Ca->C` / `Ca->O` counter/tool record-dependency (expected).
- 3 of 7 are `<base>` counter failures that are structurally expected pre-integration.
- 1 of 7 is a declaration-level overlap (`C/Ca corpus/SOURCES.md`) outside the named
  expected class — the only cross-claim coupling this snapshot actually measures. It is
  load-bearing: the same file carries an id-space conflict (C's APPEND cap vs Ca's D4
  count) that is satisfiable only by per-claim lands commits in the L1-ruled order
  A_r < A_c < A_ca, never by one merged tree.
- `Ca->REC` is a declared record dependency that cannot be evaluated until the lesson,
  dispositions manifest and post-records file exist; the checker refuses absent and
  directory lands with exit 2, so it is named here rather than faked into the manifest.
- Briefed invocation is stale: `--manifest` is not accepted by the frozen tool (exit 2);
  use the positional form above for any re-run.
- No unexpected claim-to-claim dependency beyond the declared SOURCES.md overlap was
  found, but that overlap is a sequenced coupling, not a cosmetic one (see the
  sequencing subsection). The dynamic leg cannot represent the A_r < A_c < A_ca
  ordering, so post-integration C must be evaluated at A_c and Ca at A_ca in separate
  clones (per-unit `tree` revisions or two manifest passes) with the full declared
  lands (entry, lesson, dispositions manifest, post-records, dir expansions), before
  filing `reports/round-67/telemetry/separability-real.txt`.

Files changed: `.ufo/waves/round-67/stage/separability-manifest.json` (new draft),
`.ufo/waves/round-67/w1/ExecSeparabilityReal.md` (this report). No lane jj/git writes,
no commits, no tool installs.

Report: .ufo/waves/round-67/w1/ExecSeparabilityReal.md
