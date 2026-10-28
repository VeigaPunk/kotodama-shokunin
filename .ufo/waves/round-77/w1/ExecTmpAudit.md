# ExecTmpAudit — round 77 (hyaku run 10), wave 1

Routed defect under audit: a hardcoded or silently-inherited `/tmp` scratch root
(prompt §7.4 / seat ATTACK). Scope: the adapted counters and tools under
`.ufo/waves/round-77/w1/stage/*/`, plus the wave's own control scripts.

**Verdict.** No committed tool in the stage tree writes a *literal* `/tmp` path —
the routed grep returns zero non-probe hits and the strict scanner is clean. Five
scratch-routing defects remain (two fatal, three warn), all reachable when the
operator supplies the root the wave prompt itself tells seats to supply
(`TMPDIR=… --work …`):

| # | file:line (graded snapshot) | class | one line |
|---|---|---|---|
| F1 | `ExecAdaptCa/accept-ca.py:456-471` (`scratch_dir`) | **fatal** | accepts `--work /tmp/<x>` and `$TMPDIR=/tmp` verbatim and creates the dir — the sibling C counter refuses both |
| F2 | `ExecAdaptCapture/capture-evidence.py:588-601` (`work_base`/`make_work_dir`) | **fatal** | with no root named it returns `None`, so `mkdtemp(dir=None)` writes under `/tmp` |
| F3 | `ExecAdaptJunk/junk-fixtures.py:426-439`, `452-457` | warn | the advertised `$TMPDIR/…` branch is unreachable: `_forbidden_scratch` bans `gettempdir()`, which *is* `$TMPDIR` |
| F4 | `ExecFreezeChecklist/controls.sh:26,32` | warn | `${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotodama-r77}` drops the round segment when `HYAKU_SCRATCH` is the parent; honours neither `--work` nor `$TMPDIR` |
| F5 | `ExecAdaptJunk/redbefore.py:19` | warn | `WORK` hardcoded to an absolute scratch path; ignores `--work`/`$HYAKU_SCRATCH`/`$TMPDIR` |

Graded snapshot (line numbers and hashes below are pinned to it; every row is
reproducible with `stage/ExecTmpAudit/verify-scratch-discipline.sh --snapshot`):

```
$ S=/fast/scratch/hyaku/kotodama-r77/ExecTmpAudit/verify-scratch-audit/snap-3656155
$ (cd "$S" && sha256sum ExecAdaptC/accept-c.py ExecAdaptCa/accept-ca.py \
      ExecAdaptJunk/junk-fixtures.py ExecAdaptCapture/capture-evidence.py \
      ExecGapSweep/run-controls.sh ExecFreezeChecklist/controls.sh)
3006d7c248fa545dffee8162dababb02f6efac3e0bdac48f46d95a1fdff21df0  ExecAdaptC/accept-c.py
ac2bc93d02932464f9ee43222ffe1d06dd5bf1a0e68fd38bd94e10a991489b2e  ExecAdaptCa/accept-ca.py
1325ca504b717e2b09b9448b90e387af7ffa81ba501603800b9a245d7d296e3c  ExecAdaptJunk/junk-fixtures.py
41e79fe8ce1245a16c476a96258ecafdb897d08d96c189765f0df92ad86c635b  ExecAdaptCapture/capture-evidence.py
42beb47bec2d42d5fb63e2a214a4c120beae97a5ec8b67c0f7d5a67b1ac29c68  ExecGapSweep/run-controls.sh
473648d524863adfb1f09583bb7faf51a9a238b7067d62ec46e0dbe062fd8360  ExecFreezeChecklist/controls.sh
```

The builders were still writing while this report was produced (four of the six
files above changed again between 22:37 and 22:43). Every finding below was
re-measured against the *live* tree immediately before this report was written;
the L1 MUST re-run `verify-scratch-discipline.sh --snapshot` after wave 1 lands
and before the freeze commit.

## F1 — `accept-ca.py`: a system-temp root is accepted (fatal)

`scratch_dir` walks `--work` → `$HYAKU_SCRATCH` → `$TMPDIR` and returns the first
non-empty value after `makedirs(root)`, with **no** banned-root check:

```
$ python3 -B - <<'PY'   # import the counter, call its own resolver
    spec…; m.scratch_dir("/tmp/r77-ca-probe")  and  m.scratch_dir("/tmp")
PY
--work /tmp/r77-ca-probe -> /tmp/r77-ca-probe (exists now: True )
--work under system tmp -> /tmp (exists now: True )
```

`(exists now: True)` is the tool's own `os.makedirs` creating it. The probe
directory was empty and was removed immediately (`rmdir /tmp/r77-ca-probe` →
gone); no other byte was written under `/tmp` by this seat.

The sibling C counter already implements the guard, at the *work* level as well
(`accept-c.py` lines moved while this report was written: graded snapshot 2207-2210,
live 2333-2336):

```
$ grep -n 'def _forbidden_scratch\|banned = os.path.abspath(os.sep' ExecAdaptC/accept-c.py
2333:def _forbidden_scratch(path):
2336:    banned = os.path.abspath(os.sep + "tmp")

$ cat stage/ExecAdaptC/scratch-probe.txt      # the C seat's own probe receipt
  verdict: ACCEPT-C-77: FAIL legs=0/15 (refused: scratch root /tmp/r77-scratch-probe
           is the system temporary directory (pass --work or set $HYAKU_SCRATCH; QUALITY 14))
```

Required fix: in `scratch_dir` (`accept-ca.py:456`), refuse — do not accept — a
root that `os.path.abspath` resolves to `/tmp` or below, e.g. reuse
`accept-c.py`'s `_forbidden_scratch` (ban `os.path.abspath(os.sep + "tmp")`) and
`raise ScratchRefused(...)` when the only named roots are banned. Measured
current divergence: `$TMPDIR=/tmp` → `accept-c.py` → `/fast/scratch/hyaku/kotodama-r77/counter` (off `/tmp`);
`accept-ca.py` → `/tmp`.

## F2 — `capture-evidence.py`: silent fallback to the interpreter temp dir (fatal)

```
$ sed -n '588,601p' ExecAdaptCapture/capture-evidence.py
def work_base(explicit):
    """The scratch root: --work, else $HYAKU_SCRATCH, else $TMPDIR, else the
    interpreter's temporary directory (tempfile honours TMPDIR itself)."""
    …
    return None

def make_work_dir(explicit, prefix="capture-evidence-"):
    return tempfile.mkdtemp(prefix=prefix, dir=work_base(explicit))
```

Measured (`--work`, `$HYAKU_SCRATCH`, `$TMPDIR`, `$SHOKUNIN_SCRATCH` all cleared):

```
$ env -u TMPDIR -u HYAKU_SCRATCH -u SHOKUNIN_SCRATCH python3 -B - … <<< work_base(None)
work_base(None) with no --work/$HYAKU_SCRATCH/$TMPDIR -> None | mkdtemp(dir=None) would use /tmp
$ env -u TMPDIR -u HYAKU_SCRATCH -u SHOKUNIN_SCRATCH python3 -c 'import tempfile; print(tempfile.gettempdir())'
/tmp
```

`dir=None` is `mkdtemp()` with no `dir=` — round 76's own scanner class `UNROUTED`;
round 76's `accept-ca.py` refuses in exactly this situation. This is inherited
verbatim from `reports/round-76/counters/capture-evidence.py` (same function, same
docstring), so the r77 adaptation did not touch it.

Required fix: `work_base` must raise/exit 2 when none of the three roots is named
(message: `no scratch root: pass --work, or set $HYAKU_SCRATCH or $TMPDIR`), and
`make_work_dir` must never be called with `dir=None`. The `--work` help text at
line 1785 ("else the interpreter's temporary directory") must change with it.

## F3 — `junk-fixtures.py`: the `$TMPDIR` branch cannot be used (warn)

Docstring (line 58-60) advertises `$TMPDIR/kotodama-r77-junk-fixtures`; the guard
bans it:

```
$ sed -n '426,439p;452,457p' ExecAdaptJunk/junk-fixtures.py
def _forbidden_scratch(path):
    """True when `path` is (inside) the system temporary directory.
    … The banned root is whatever `tempfile.gettempdir()` resolves
    (which honours `$TMPDIR`), so no temp path is spelled here."""
    p = os.path.abspath(path)
    b = os.path.abspath(tempfile.gettempdir())
    return p == b or p.startswith(b + os.sep)
        elif tmp:
            root = os.path.join(os.path.abspath(tmp), "kotodama-r%d-junk-fixtures" % r)
```

Measured with `TMPDIR` set to an operator scratch dir (and `tempfile.tempdir`
reset between cases — `gettempdir()` caches, which is how a naive probe misses
this):

```
junk-fixtures.py  $TMPDIR      -> REFUSED: FixtureError: scratch root
   /fast/scratch/hyaku/kotodama-r77/ExecTmpAudit/verify-scratch-audit/t/kotodama-r77-junk-fixtures
   is inside the system temporary directory; pass --work under the operator scratch tree instead
junk-fixtures.py  $TMPDIR=/tmp -> REFUSED: FixtureError: scratch root /tmp/kotodama-r77-junk-fixtures …
junk-fixtures.py  $HYAKU_SCRATCH -> …/h/kotodama-r77/junk-fixtures      (works)
junk-fixtures.py  none           -> /fast/scratch/hyaku/kotodama-r77/junk-fixtures
```

Consequence: a seat following the wave instruction `TMPDIR=<scratch> --work <scratch>/x`
gets a refusal (any `--work` under `$TMPDIR` is refused by the same guard), and
the documented TMPDIR tier is dead code.

Required fix: ban only the literal system root, as `accept-c.py:2210` does
(`banned = os.path.abspath(os.sep + "tmp")`), so an operator-chosen `$TMPDIR`
elsewhere stays usable — this is the reasoning round 76 already wrote into
`accept-c.py`'s docstring ("banning gettempdir() would ban the operator's own choice").

## F4 — `ExecFreezeChecklist/controls.sh`: the round segment disappears (warn)

```
$ grep -n 'SCRATCH_BASE=' ExecFreezeChecklist/controls.sh
26:#   ${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotodama-r77}/ExecFreezeChecklist-controls.$$
32:SCRATCH_BASE=${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotodama-r77}

$ HYAKU_SCRATCH=/fast/scratch/hyaku bash -c 'SCRATCH_BASE=${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotodama-r77}; echo "resolved: $SCRATCH_BASE"'
resolved: /fast/scratch/hyaku
$ HYAKU_SCRATCH= bash -c 'SCRATCH_BASE=${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotodama-r77}; echo "unset-resolved: $SCRATCH_BASE"'
unset-resolved: /fast/scratch/hyaku/kotodama-r77
```

With the fleet's parent value `HYAKU_SCRATCH=/fast/scratch/hyaku` the script
writes `/fast/scratch/hyaku/ExecFreezeChecklist-controls.<pid>` — outside the
round tree, so two rounds (or two seats) share one flat namespace. The sibling
control script gets this right:

```
$ grep -n 'kotodama-r77/controls' ExecGapSweep/run-controls.sh
185:[ -n "$SCRATCH" ] || SCRATCH=${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotodama-r77/controls
```

Required fix: line 32 → `${HYAKU_SCRATCH:-/fast/scratch/hyaku}/kotodama-r77`;
and add `--work`/`$TMPDIR` to the resolution chain (measured chain: `hyaku` only —
`check-scratch-chain.py` `CHAIN ExecFreezeChecklist/controls.sh: hyaku`), or state
in the header that only `--scratch`/`$HYAKU_SCRATCH` are honoured.

## F5 — `ExecAdaptJunk/redbefore.py:19`: hardcoded scratch root (warn)

```
$ grep -n '^WORK =' ExecAdaptJunk/redbefore.py
19:WORK = "/fast/scratch/hyaku/kotodama-r77/ExecAdaptJunk/redbefore-work"
$ grep -n 'SCRATCH\|TMPDIR\|gettempdir' ExecAdaptJunk/redbefore.py   # (no --work/$… branches)
```

A committed tool must honour `--work` / `$HYAKU_SCRATCH` / `$TMPDIR`; this one is
frozen to the author's own seat directory and would collide if two seats run it.
Required fix: take `--work` (default `$HYAKU_SCRATCH/kotodama-r77/redbefore`) and
refuse when none is named. `os.makedirs(WORK)` at line 141 is the write site.

## Live re-check (immediately before this report was finalised)

```
$ sha256sum stage/ExecAdaptCa/accept-ca.py stage/ExecAdaptCapture/capture-evidence.py \
            stage/ExecAdaptJunk/junk-fixtures.py stage/ExecAdaptC/accept-c.py
ac2bc93d…  ExecAdaptCa/accept-ca.py          (= graded snapshot: F1 open)
41e79fe8…  ExecAdaptCapture/capture-evidence.py (= graded snapshot: F2 open)
1325ca50…  ExecAdaptJunk/junk-fixtures.py    (= graded snapshot: F3 open)
de5dafd2…  ExecAdaptC/accept-c.py            (newer than graded 3006d7c2: no /tmp target)

$ # accept-ca.py, its own resolver, five environments
accept-ca  $TMPDIR=/tmp -> /tmp                      F1 open
accept-ca  --work /tmp  -> /tmp                      F1 open
capture    work_base(None) -> None | gettempdir -> /tmp   F2 open
junk       $TMPDIR (existing dir) REFUSED: FixtureError … inside the system temporary directory   F3 open
junk       --work under $TMPDIR REFUSED: FixtureError                                            F3 open
ExecFreezeChecklist/controls.sh:32:SCRATCH_BASE=${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotodama-r77}  F4 open
ExecAdaptJunk/redbefore.py:19:WORK = "/fast/scratch/hyaku/kotodama-r77/ExecAdaptJunk/redbefore-work"  F5 open
```

Measurement caveat for F3: `tempfile.gettempdir()` verifies a candidate by writing
into it, so a **non-existent** `$TMPDIR` is skipped and `gettempdir()` silently
falls back to `/tmp` — the refusal then does not fire and the tool happily returns
`$TMPDIR/kotodama-r77-junk-fixtures` (observed). Probes must `mkdir -p "$TMPDIR"`
first, and the tool's guard should not depend on `gettempdir()` at all.

## Informational (no `/tmp` write; decide at the freeze, do not silently accept)

- **I1** `ExecAdaptC/accept-c.py:2312` (`_scratch_root`): with nothing named it
  *invents* `/fast/scratch/hyaku/kotodama-r77/counter` (measured `none -> …/kotodama-r77/counter`);
  `accept-ca.py` refuses instead. Both behaviours are on `/fast` — pick one policy
  and state it in the claims, because a frozen counter that invents a root cannot
  be used to prove "no scratch bytes nobody named".
- **I2** `accept-ca.py`'s `$HYAKU_SCRATCH` branch appends no round segment
  (measured `-> …/verify-scratch-audit/h`), while `accept-c.py` appends
  `kotodama-r77/counter`. With a bare operator `HYAKU_SCRATCH` this counter writes
  straight into the shared root.
- **I3** `ExecAdaptCapture/dry-run.py:37` (`OUTDIR = HERE/"dryrun"`) and
  `ExecFreezeChecklist/manifest-check.py:154` (`--manifest` default
  `HERE/manifest.json`) write next to the script. Correct for a wave-local tool;
  they must not be installed into `reports/round-77/` as-is.
- **I4** `ScribeQuality30/exec-limb.py:8`, `exec-limb2.py:6` read
  `reports/round-76/ledger.json` — a previous round's path inside a round-77 stage
  tool. Deliberate cross-check or stale copy: route to the author.
- **I5** Transient states seen during the wave and *gone* at the graded snapshot
  (recorded so nobody re-reports them): `accept-ca.py:3942 NameError: LANE_ROW_ID`
  (22:37, 22:41); `junk-fixtures.py:1935 NameError: j10_candidates` (22:32);
  `junk-fixtures.py:2211` selftest expectation "must-pass green" red (22:36);
  `r76-ca-` mkdtemp prefixes (now `r77-ca-`/`r77-ledgercheck-`).

## Negative results (the sweep, not an assumption)

```
$ cd .ufo/waves/round-77/w1
$ grep -rnE 'mkdtemp\(dir="/tmp|"/tmp/|/tmp/' stage/ | grep -v '^stage/ExecTmpAudit/'
stage/ExecAdaptC/scratch-probe.py:7:  1. --work /tmp/<probe>   -> refused exit 2, FAIL verdict, no LEG line, no dir
stage/ExecAdaptC/scratch-probe.txt:5:  verdict: ACCEPT-C-77: FAIL legs=0/15 (refused: scratch root /tmp/r77-scratch-probe …
stage/ExecAdaptC/scratch-probe.txt:6:  stderr: REFUSED: scratch root /tmp/r77-scratch-probe is the system temporary directory …
```

All three hits are the C seat's *refusal* probe (documentation plus the refusal it
provoked) — no write target. Stage-wide, with the two auditors' own pattern
strings allowlisted:

```
$ python3 -B check-scratch-root.py --root stage --paths '**/*.py' --paths '**/*.sh' --strict --allow allow.txt
checked=20 HIT(allowlisted)=1            # exit 0; the one HIT is this seat's own probe case
$ python3 -B check-scratch-chain.py --root stage --paths '**/*.py' --paths '**/*.sh' --allow allow.txt
checked=20 fatal=0
```

- Base sweep, active tooling only: `git grep -n -E '("/tmp["/]|dir=.?/tmp|/tmp/)' 211f952… -- 'tools/*.py' 'tools/*.sh' 'reports/round-76/*.py' 'reports/round-76/counters/*.py'` → **0 hits**, so no round-77 hit is inherited from a committed active tool.
- The lane's own `reports/round-77/` is empty at the time of writing (the L1
  installs at the freeze) and `.ufo/waves/round-77/w1/drafts/` holds no code:
  `find drafts -type f` → `drafts/corpus/knowledge/…/naming-systems.amend-2026-10-23.md`,
  `drafts/corpus/lessons/round-77.md`, `drafts/quality-30.md`,
  `drafts/reports/round-77/telemetry/census-start-counts.txt`,
  `drafts/scorecard-section.md`; `grep -rn '/tmp' drafts/` → no output.
- Every `mkdtemp()` in the four counters carries `dir=` (`accept-c.py` 2/2,
  `accept-ca.py` 3/3, `junk-fixtures.py` 1/1, `capture-evidence.py` 1/1).
- Selftests at the graded snapshot: `accept-c.py --selftest` exit 0 (`SELFTEST: 29/29`),
  `accept-ca.py --selftest` exit 0 (`SELFTEST: 199/199`), `junk-fixtures.py --selftest`
  exit 0 (`SELFTEST: PASS`) — receipts in `stage/ExecTmpAudit/receipts/*.selftest.txt`.
- No tool writes into the real lane during a run: every fixture write site
  (`_st_write`, `_st_census_stub`, the selftest lane appends in `accept-ca.py`
  ~3218-3657) resolves under a `case_dir` inside the named scratch root.

## Delivered tooling (stage only; the L1 installs)

- `stage/ExecTmpAudit/check-scratch-root.py` — round-76 scanner, extended:
  `os.sep` folding (catches `os.path.join(os.sep, "tmp")`), python code embedded
  in `*_BOOTSTRAP`/`*_SCRIPT`-named constants (catches `python -c` payloads),
  attribute assignment targets (`module.R74_TMPDIR = …`) and env keys containing
  `TMPDIR`. Selftest: 13/13 cases (last block prints `PASS … []`).
- `stage/ExecTmpAudit/check-scratch-chain.py` — resolution-chain checker:
  static `CHAIN` per file, `NOCHAIN`/`HARDROUND`/`INVENTED`/`BARE` classes, and a
  `--dynamic` probe that imports the tool's own resolver and measures five
  environments (`gettempdir()` cache reset between cases). Selftest: 4/4.
- `stage/ExecTmpAudit/allow.txt` — the auditors' own pattern strings only.
- `stage/ExecTmpAudit/verify-scratch-discipline.sh` — one command re-running all
  six sections above; honours `--work`/`$HYAKU_SCRATCH`/`$TMPDIR` and refuses when
  none is set; `--snapshot` freezes the tree first.

## Bounds and scratch discipline

Read-only over the lane: `LOG.md`, `SCORECARD.md`, `SKILL.md`, `SHONEN.md`,
`corpus/**`, `reports/round-76/**`, `reports/round-77/**` (empty at the time of
writing), `.ufo/state`, the fleet repo and `shokuknow` were not written. No git
mutation, no jj, no background service. All scratch lived in
`/fast/scratch/hyaku/kotodama-r77/ExecTmpAudit/`; the one directory this seat's
probe caused under `/tmp` (`/tmp/r77-ca-probe`, created by the tool under test)
was removed. No tool was installed or upgraded — python3 stdlib and coreutils only,
so there is no install to record. Scratch is deleted before yielding; the graded
snapshot hashes above are cited from the transcript, not from scratch paths.
