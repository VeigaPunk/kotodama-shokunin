# round-77 do-nothing + gap harness — `run-controls.sh`

Owner seat: `ExecGapSweep` (wave 1). Deliverable installed by the L1 at the
freeze as `.ufo/waves/round-77/run-controls.sh` (the path `freeze-set.sh`
emits, exactly where round 76 kept `run-controls.sh`). Parent:
`.ufo/waves/round-76/run-controls.sh` + `rehearse.sh` (read, never edited).

The harness materializes one clone of the lane under scratch
(`git clone --shared`, toplevel asserted equal to the clone before any git
call, `main` pinned to the freeze = the do-nothing measured revision), hands
that clone to both round-77 counters as `--root`, and records — per control —
the exact argv, the counter's stdout+stderr, its exit status and a verdict.
The lane worktree is only read (validation) and cloned from; the counters'
own materializations live under the same scratch, and `HYAKU_SCRATCH`,
`SHOKUNIN_SCRATCH` and `TMPDIR` are pointed into it for every graded run.

## Controls

| # | invocation shape | expectation (hard) |
|---|---|---|
| 1 | `--lands <freeze>` | exit **1**, `ACCEPT-*-77: FAIL`, ≥1 `LEG` line, `LEG FAIL ENTRIES`, `LEG FAIL ROWS`, `LEG PASS FROZENCFG` for C (add `LEG PASS STAMP` with `--require-green-c 'FROZENCFG STAMP'`) and `LEG FAIL REPAIR`, `LEG FAIL ANNOTATE`, `LEG PASS FROZENCFG`, `LEG PASS STAMP`, `LEG PASS LEDGER` for Ca |
| 2 | `--lands <base>` | exit **2**, **zero** `LEG` lines, refusal names the base (`/base/`) |
| 3 | no `--work`, no `$HYAKU_SCRATCH`/`$SHOKUNIN_SCRATCH`/`$TMPDIR` (Ca by default; `--scratch-refusal both` adds claim C) | exit **2**, **zero** `LEG` lines, refusal names the missing scratch (`/scratch\|--work\|HYAKU_SCRATCH/`), and the fallback dir `/fast/scratch/hyaku/kotodama-r77` is stat'ed before/after so an invented scratch root is visible |
| 4 | Ca without `--combined` (scratch given) | exit **2**, **zero** `LEG` lines, refusal names `combined` |

Control 1 also fires on a refusal summary (`ACCEPT-*-77: FAIL legs=0/…`) at the
freeze: an unusable frozen config is not a do-nothing pass.

Control 3 is scope-controlled: `--scratch-refusal both|ca|none`, **default
`ca`**. The draft claim text that names this refusal names it for claim Ca only
("missing `--combined`/`--work` refused exit 2 printing no leg line"); claim C's
do-nothing control names only `lands == freeze`, `lands == base` and the junk
landings, and the round-76 C counter (freeze-proven) resolves `--work` →
`$HYAKU_SCRATCH/kotodama-r76/counter` → `$TMPDIR/…` → the operator default and
refuses only the system temp dir. Asserting the refusal for C by default would
manufacture a violation against a clause C does not freeze, so the default is
`ca`; pass `--scratch-refusal both` when the frozen C claim does name it (C
denominator 3), and `none` to drop the control. See `../../ExecGapSweep.md`
finding F1 for the measured C behaviour either way.

Receipts (default `--out <lane>/reports/round-77/telemetry`, the two names the
round-77 freeze manifest lists):

```
reports/round-77/telemetry/controls-c.txt    # ends CONTROLS-C-77:  PASS controls=2/2 | 3/3 (scope both) | FAIL controls=<n>/<m>
reports/round-77/telemetry/controls-ca.txt   # ends CONTROLS-CA-77: PASS controls=4/4 | FAIL controls=<n>/4
```

The skipped/short form is recorded in the receipt
(`## control 3: skipped (--scratch-refusal=ca: …)`), never silently dropped.

Exit: 0 every control met its expectation · 1 ≥1 deviation (receipts still
written, each named on its `# control verdict:` line) · 2 setup error (bad
revision, missing counter, clone failure) — nothing graded, no receipt written.

## Exact invocations

Production run at/after the freeze, from any directory (all paths absolute;
`--out` defaults to the lane telemetry dir):

```sh
sh /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-77/run-controls.sh \
   --freeze <FREEZE40> \
   --base <FROZEN-CLAIM-BASE40> \
   --lands <ROUND-77-LANDS40> \
   --fleet-root /home/vgpnk/Projects/shokunin \
   --scratch /fast/scratch/hyaku/kotodama-r77/controls
```

`--base` may be omitted (derived from `<freeze>:reports/round-77/claims.json`);
a `--base` that disagrees with the frozen one is refused unless
`--allow-base-mismatch`. `--lands` may be omitted (defaults to the freeze);
`--combined` defaults to `--lands` when it differs from the freeze, else the
freeze.

Do-nothing-only run (before any landing exists), scratch cleaned afterwards:

```sh
sh .../.ufo/waves/round-77/run-controls.sh \
   --freeze <FREEZE40> --lands <FREEZE40> \
   --scratch /fast/scratch/hyaku/kotodama-r77/controls --rm
```

Rehearsal on the wave-1 stage drafts (no `--counter-dir`: the default search
finds `reports/round-77/accept-c.py` in the clone first, then the lane's
installed copy, then `.ufo/waves/round-77/counters/`, then
`.ufo/waves/round-77/w1/stage/ExecAdaptC/` and `…/ExecAdaptCa/`; the receipt
records which path and sha256 was executed):

```sh
sh /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-77/w1/stage/ExecGapSweep/run-controls.sh \
   --freeze <FREEZE40> --base <BASE40> \
   --scratch /fast/scratch/hyaku/kotodama-r77/<seat> \
   --out /fast/scratch/hyaku/kotodama-r77/<seat>/out
```

Explicit counter pair (both names must be in one directory):

```sh
sh .../run-controls.sh --freeze <F> --base <B> \
   --counter-dir /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-77/counters
```

Leg-expectation overrides, when the frozen leg table differs from the defaults
(the defaults are claim C `ENTRIES ROWS` red / `FROZENCFG` green — the 22:33
draft's C list has no `STAMP`, the counter's table does; claim Ca
`REPAIR ANNOTATE` red / `FROZENCFG STAMP LEDGER` green):

```sh
sh .../run-controls.sh --freeze <F> --base <B> \
   --require-red-c 'ENTRIES ROWS COLLCHECK' --require-green-c 'FROZENCFG STAMP' \
   --require-red-ca 'REPAIR ANNOTATE' --require-green-ca 'FROZENCFG STAMP LEDGER'
```

Plan (materializes the clone, resolves the counters, prints the invocations,
executes no counter, writes no receipt):

```sh
sh .../run-controls.sh --freeze <F> --base <B> --plan --scratch /fast/scratch/hyaku/kotodama-r77/<seat>
```

Self-check (fixture repo + good/bad stub counters under `--scratch`; touches
no lane path; proves 2+4 green controls under the default `--scratch-refusal=ca`,
3+4 under `--scratch-refusal both`, and that all six bad controls are caught):

```sh
sh .../run-controls.sh --selftest --scratch /fast/scratch/hyaku/kotodama-r77/<seat>
```

## Notes / limits

* The counters must carry round-77 byte-for-byte at `<freeze>` for the graded
  path (the clone's committed copy is preferred); a missing counter is a setup
  error (exit 2), never a silent pass.
* `controls-c.txt` / `controls-ca.txt` name the freeze they measured, so they
  cannot be committed *in* the freeze commit they describe. Round 76's freeze
  tree carries no `controls-c.txt` (`git show
  98c486b…:reports/round-76/telemetry/controls-c.txt` → *exists on disk, but
  not in …*); the receipts are produced post-freeze. The freeze manifest must
  read those two names that way.
* No path in this script is a literal `/tmp`; every materialization is
  `--scratch`-rooted and removed on `--rm`.
