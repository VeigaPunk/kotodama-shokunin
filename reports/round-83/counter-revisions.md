# Round-83 counter revisions

The round-83 counters freeze before any claim artifact lands. A revision after
that point is a repair with a red-before receipt, never a silent edit; the
claim's predicate, kill rule and target do not move (r79/r80/r81/r82
precedent).

- **r1 — `240d76b76bb8d3d054f63c28d2423bd5ed692ad5`** (first freeze: claims.json,
  `counterlib.py`, the three counters, census start). Red-before, measured at
  this revision before any claim data existed:
  - `reports/round-83/telemetry/controls-*.txt`: all three counters refused the
    do-nothing control with the *wrong* reason, `freeze is not an ancestor of
    lands`, because the ancestor check ran before the `lands == base` check — a
    control receipt that names the wrong rule is not a control.
  - `reports/round-83/telemetry/smoke-d.txt`: the D counter raised an uncaught
    `FileNotFoundError` for the absent entry instead of grading the ENTRY leg,
    so a missing artifact could have crashed the counter rather than failing it.
- **r2 — this commit.** Fixes, each visible in the diff: (1) every counter checks
  `lands == base` before the ancestor relation, so the do-nothing control is
  refused with that named reason; (2) the D counter reads a missing file as
  empty text, so an absent entry fails `ENTRY` instead of raising; (3)
  `counterlib.load_config` reads the frozen config from `--freeze` only — the
  `lands` bytes stay a graded `FROZENCFG` leg, so a control run at the base
  revision is refused by rule rather than by an unreadable file. No predicate,
  target, leg name or leg order changes; constants unchanged.
- **r3 — this commit.** Red-before: the freeze-r2 smoke grade
  (`reports/round-83/telemetry/smoke-o.txt`) printed `LEG BEFORE FAIL
  instruments=58 missing=11/11` — the counter's own `missing_of` iterated the
  `(cells, line)` tuple as if it were the cell list, so every instrument looked
  uncovered and the before-state could never pass. Two further legs
  (`ROWS`) carried the same unpacking bug, and the `DEAD`/`REGISTRY` legs
  materialised only the accept-* scripts, so every `tools/*.py` row read as a
  dead token (13 dead at a tree that had no `tools/` blobs). Fix: unpack
  `(cells, _)` in `missing_of` and `ROWS`; materialise every `tools/**/*.py`
  blob at lands into the graded tree; treat a fixture mutation that changes no
  committed bytes as a `NoOp` rather than a commit failure (so a dry run of the
  junk battery is honest about what it did not test). No predicate, constant,
  target or leg name changes; the r2 counters are the red-before.
- **r4 — this commit.** r3's no-op-fixture fix reached the O and C counters and the
  shared library but not the D counter (`git diff` at r3 showed the D file clean
  while the worktree carried the uncommitted hunk). Red-before: at r3 the D
  counter's junk battery would have raised `CalledProcessError` on a mutation
  that changes no bytes instead of reporting it. The hunk committed here is the
  identical `NoOp` handling; no predicate or constant changes.
- **r5 — this commit.** Red-before: the L1's dry parse of the claim-D entry
  showed `- couples:`/`- source:`/`- verified-at:`/`- recheck:`/`- scope:`
  reported missing while all eight header fields were present at lines 3-10 —
  the `ENTRY` leg split the document on the *substring* `"## "`, and the header's
  own `the anchor list in `## 3`` cut the split before the later fields. Fix:
  split on `^## ` at line starts. No constant or predicate changes; the header
  requirement is unchanged and the entry was never graded by the broken leg.
