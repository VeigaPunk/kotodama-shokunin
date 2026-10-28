# ExecTmpAudit2 — round 77 (hyaku run 10), wave 2 attack

Scope (as assigned): the round-77 **adapted capture tools and counters** — every
code path that resolves a scratch root or writes a file — attacked on two axes
only: (a) hardcoded or silently inherited `/tmp` scratch paths, (b) symlink
following. Code **and** selftests scanned. No edit was made to any file
(`sha256sum -c` of the 37 staged code files: every line `OK`). Lane git state
before and after: `?? .ufo/waves/round-77/`, `?? reports/round-77/` only.

`reports/round-77/` still holds only `telemetry/` at the time of writing, so the
graded copies the L1 installs at the freeze are exactly the stage files measured
here.

## Graded snapshot (line numbers and hashes below are pinned to these bytes)

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-77/w1/stage
$ sha256sum ExecAdaptC/accept-c.py ExecAdaptCa/accept-ca.py \
            ExecAdaptCapture/capture-evidence.py ExecAdaptJunk/junk-fixtures.py \
            ExecAdaptJunk/redbefore.py ExecAdaptC/scratchmirror-real.py \
            ExecFreezeChecklist/manifest-check.py ExecFreezeChecklist/controls.sh
5ac63e0d6630e8711aca7cceb159ee2b13c94b5a1bec4997afbdb3806826dca4  ExecAdaptC/accept-c.py
ac2bc93d02932464f9ee43222ffe1d06dd5bf1a0e68fd38bd94e10a991489b2e  ExecAdaptCa/accept-ca.py
bab5ca44f78540059b07f22c1ee2254ae310075c865355841b24c0d49030f8b5  ExecAdaptCapture/capture-evidence.py
1325ca504b717e2b09b9448b90e387af7ffa81ba501603800b9a245d7d296e3c  ExecAdaptJunk/junk-fixtures.py
a352d6dcbb603792ae1fa06023073ba33d0893172bbdae3bcdd272bb56fdf99a  ExecAdaptJunk/redbefore.py
bcc6745f24c98b528e583be6078d97b00927ac9ecf372524b4aa77935f595fab  ExecAdaptC/scratchmirror-real.py
aa96c58e241fc3ec9fdb803dbf5699d640d6ab9c138d0c9701c28765d4040aa9  ExecFreezeChecklist/manifest-check.py
473648d524863adfb1f09583bb7faf51a9a238b7067d62ec46e0dbe062fd8360  ExecFreezeChecklist/controls.sh
```

Two files moved after wave 1's audit: `accept-c.py` (`3006d7c2`/`de5dafd2` →
`5ac63e0d`) and `capture-evidence.py` (`41e79fe8` → `bab5ca44`). Both were
re-measured here; the wave-1 findings in them are **still open**.

## Verdict

The adapted tools contain **no hardcoded `/tmp` write target**, but every guard
against the system temp root compares `os.path.abspath`, never `os.path.realpath`,
and **no tool has an `islink` / `O_NOFOLLOW` / `lstat` check anywhere**
(`grep` below returns nothing). Consequences measured, not inferred: all four
scratch resolvers accept a *symlink to `/tmp`* as an operator scratch root and
write through it, a real capture run writes its evidence file through a
symlinked `--out` directory, and the C counter reads committed symlink entries
from a materialized tree straight out of the graded tree.

| # | class | site | severity |
|---|---|---|---|
| N1 | `--work`/`$HYAKU_SCRATCH` symlink to `/tmp` accepted by all four scratch resolvers | `accept-c.py:2481-2506,3103-3119`, `accept-ca.py:456-471`, `capture-evidence.py:590-603`, `junk-fixtures.py:426-477` | **fatal** |
| N2 | `capture-evidence.py --out` follows a symlinked output directory; evidence bytes land outside the lane | `capture-evidence.py:2083-2089` | **fatal** |
| N3 | materialized tree recreates committed absolute symlinks; `read_tree`/`tree_files`/`_grep_tree` read *through* them, so a committed `120000` entry under `corpus/knowledge` is graded from outside the tree | `accept-c.py:253-273,294-306,1125-1143` (+ `scratchmirror-real.py:41`) | **high** |
| N4 | `accept-ca.py` accepts a literal `/tmp` root (wave-1 F1, still open) — no banned-root check in `scratch_dir` at all | `accept-ca.py:456-471` | **fatal (carried)** |
| N5 | `capture-evidence.py` no-root fallback is `mkdtemp(dir=None)` → `/tmp` (wave-1 F2, still open) | `capture-evidence.py:590-603,2391` | **fatal (carried)** |
| N6 | zero symlink coverage in any selftest; one selftest (`junk-fixtures`) asserts the *buggy* ban and therefore cannot see F3 | selftests of all five files | **high (process)** |
| N7 | `scratchmirror-real.py` copies the assimilation dir with `shutil.copytree` default (`symlinks=False`) — a symlink in assimilation is copied as its target's bytes | `scratchmirror-real.py:41` | medium (0 symlinks in assimilation today) |
| N8 | `accept-ca.py` appends to `SCORECARD.md`/ledger/claims with plain `open(..., "a")`; a symlinked file in the graded clone is appended through | `accept-ca.py:3279,3595,3603,3672` | medium (latent) |
| I1 | `capture-evidence.py` local (`file://`) fetch follows a symlink and copies the target's bytes into the receipt | `capture-evidence.py:623-632,645` | info |
| I2 | `verify-scratch-discipline.sh` derives `$ROOT` from `$TMPDIR` with no banned check (auditor tool, not adapted) | `ExecTmpAudit/verify-scratch-discipline.sh:38-48` | info |
| P1 | positive: `manifest-check.py:195` is the one realpath-escape guard in the wave — the idiom the scratch resolvers lack | `ExecFreezeChecklist/manifest-check.py:195` | — |

## N1 — symlinked scratch root defeats every banned-root guard (fatal)

All guards compare `abspath`; a symlink under the operator tree that points at
`/tmp` is therefore *not* "inside the system temporary directory":

```
$ grep -n 'p = os.path.abspath(path)' ExecAdaptC/accept-c.py ExecAdaptJunk/junk-fixtures.py
ExecAdaptC/accept-c.py:2504:    p = os.path.abspath(path)
ExecAdaptJunk/junk-fixtures.py:434:    p = os.path.abspath(path)

$ grep -n 'islink\|O_NOFOLLOW\|follow_symlinks\|lstat\|readlink' \
       ExecAdaptC/accept-c.py ExecAdaptCa/accept-ca.py ExecAdaptCapture/capture-evidence.py \
       ExecAdaptJunk/junk-fixtures.py ExecAdaptJunk/redbefore.py ExecFreezeChecklist/manifest-check.py
$ echo "exit=$?"
exit=1                      # zero matches: no symlink refusal exists in the wave
```

Measured with the tools' **own resolvers** (`sym -> /tmp/et2-sym-target`):

```
accept-c._forbidden_scratch('/tmp')              -> True
accept-c._forbidden_scratch('/tmp/et2-x')        -> True
accept-c._forbidden_scratch(sym->/tmp)           -> False
accept-c._scratch_root(--work /tmp/et2-x)        -> /tmp/et2-x
accept-c._scratch_root(--work sym)               -> /fast/scratch/hyaku/kotodama-r77/ExecTmpAudit2/sym
accept-c._st_scratch() under HYAKU_SCRATCH=sym   -> /fast/scratch/hyaku/kotodama-r77/ExecTmpAudit2/sym/kotodama-r77/selftest
junk._forbidden_scratch(sym->/tmp)               -> False
junk.resolve_workroot(explicit=sym)              -> /fast/scratch/hyaku/kotodama-r77/ExecTmpAudit2/sym
accept-ca.scratch_dir(sym->/tmp)                 -> /fast/scratch/hyaku/kotodama-r77/ExecTmpAudit2/sym | exists: True
capture.make_work_dir(sym->/tmp)                 -> /fast/scratch/hyaku/kotodama-r77/ExecTmpAudit2/sym/capture-evidence-lx4yo3rx | exists: True
```

Note the asymmetry in `accept-c.py`: the `$TMPDIR` branch *is* guarded
(`accept-c.py:2496`), the `--work` branch is not (`2489-2491`); the only thing
that stops a literal `--work /tmp/...` is the later `_forbidden_scratch(scratch)`
at `3262`, which the symlink defeats:

```
--work /tmp/et2-c-real                -> /tmp/et2-c-real                    guard_refuses=True
--work <W>/sym                        -> <W>/sym                            guard_refuses=False
```

Real runs, not resolver calls — each wrote through the symlink into `/tmp`:

```
$ env HYAKU_SCRATCH=<W>/sym python3 -B ExecAdaptC/accept-c.py --selftest
SELFTEST: 37/37                                                   exit 0, 3.1 s
$ find /tmp/et2-sym-target -maxdepth 3
/tmp/et2-sym-target/kotodama-r77
/tmp/et2-sym-target/kotodama-r77/selftest

$ env HYAKU_SCRATCH=<W>/sym python3 -B ExecAdaptCa/accept-ca.py --selftest
SELFTEST: 199/199                                                 exit 0, 14.0 s
$ env -u HYAKU_SCRATCH TMPDIR=/tmp/et2-ca-t python3 -B ExecAdaptCa/accept-ca.py --selftest
SELFTEST: 199/199                                                 exit 0, 13.7 s

$ python3 -B ExecAdaptCapture/capture-evidence.py --selftest --work <W>/sym/ce
SELFTEST OK: 36 scenarios                                         exit 0, 4.9 s
$ find /tmp/et2-sym-target/ce
/tmp/et2-sym-target/ce
```

Retained byte proof for accept-ca's selftest scratch expression
(`accept-ca.py:3312`), executed with the tool's own resolver:

```
scratch_dir(sym) -> /fast/scratch/hyaku/kotodama-r77/ExecTmpAudit2/sym
mkdtemp(dir=scratch_dir()) -> .../sym/r77-ca-selftest-_qg97m23 | realpath: /tmp/et2-sym-target/r77-ca-selftest-_qg97m23
proof.txt exists: True
```

Required fix: resolve once, before the guard — `root = os.path.realpath(root)`
— and refuse when the realpath is `/tmp` or below (reuse the C counter's
`_forbidden_scratch`) **and** refuse when `os.path.islink(root)` for a root the
operator named explicitly. `junk-fixtures.py` must stop defining the banned root
as `tempfile.gettempdir()`.

## N2 — the capture tool writes evidence through a symlinked `--out` (fatal)

```
$ sed -n '2083,2089p' ExecAdaptCapture/capture-evidence.py
        out_dir = os.path.dirname(os.path.abspath(args.out))
        if out_dir:
            os.makedirs(out_dir, exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as fh:
            fh.write(document)
```

`os.makedirs` and `open` both follow symlinks; there is no check that `--out`
resolves inside the repo/`cfg.evidence_dir` (`evidence_dir` is resolved into the
config but never used to validate `--out`). Real CLI run against the tool's own
fixture page/memento server, `--out` a file inside `evlink -> /tmp/et2-out`:

```
$ python3 -B out-symlink-probe.py <stage> <W>
cmd: .../capture-evidence.py --claims-file <W>/claims-probe.json \
     --url http://127.0.0.1:45067/fixture.html \
     --wayback-url http://127.0.0.1:45067/web/20240111092427id_/http://127.0.0.1:45067/fixture.html \
     --quote 世界観の作り方は、一つの場所に集めることです。 --anchor-quote 同 --id S999 \
     --out <W>/evlink/S999.txt --work <W>/cework
exit: 0
stdout tail: EVIDENCE S999: quote-found=yes ... | VERIFY OK: <W>/evlink/S999.txt window-sha256=bf8ef735... | ACCEPT-C-77: CAPTURE OK
--out is a symlinked dir; islink(evlink): True
realpath(out): /tmp/et2-out/S999.txt
file exists at /tmp target: True
written bytes: 18323
first line: # evidence S999 — claim C GATE (round 77)
```

So a green `CAPTURE OK` receipt can be produced while the evidence file lives
outside the lane. Required fix: `real = os.path.realpath(args.out)`; refuse when
`real` is not under `realpath(repo)` (or, at minimum, not under
`realpath(dirname(repo)/cfg.evidence_dir)`), and refuse when the final component
is a symlink.

## N3 — committed symlinks are followed into the graded tree (high)

`materialize()` (`accept-c.py:294-306`) is `git archive | tar -x`; absolute
symlink blobs become absolute symlinks in the scratch tree. The lane **already
commits 19 of them at base** (all under `.ufo/waves/…/guard-proof/…`, all
absolute into this lane):

```
$ git -C <lane> ls-tree -r 211f9526… | awk '$1=="120000"' | wc -l
19
$ git -C <lane> show 211f9526…:.ufo/waves/round-73/assimilation/guard-proof/mirror/SKILL.md
/home/vgpnk/Projects/shokunin/kotodama-shokunin/SKILL.md
```

`read_tree` (`253-259`) is `open()`; `tree_files`/`_md_count`/`_grep_tree`
(`262-273`, `1088-1143`) use `os.walk` (which does **not** descend directory
symlinks — measured below) but they do hand file symlinks to `open()`. Measured
on a materialized base:

```
materialized symlink exists: True
target: /home/vgpnk/Projects/shokunin/kotodama-shokunin/SKILL.md
resolves INSIDE materialized tree: False
_grep_tree(dest,'.ufo','Shokunin|shokunin') hits: 1736   # reads the LIVE lane's SKILL.md
```

End-to-end with a committed fixture symlink (fixture repo under
`/fast/scratch/hyaku/kotodama-r77/ExecTmpAudit2/fixture-git`,
`git rev-parse --show-toplevel` asserted before and after the commit):

```
mode: 120000 corpus/knowledge/linked.md
git show HEAD:corpus/knowledge/linked.md -> /tmp/et2-out/payload.md
materialized is a symlink: True -> /tmp/et2-out/payload.md
tree_files: ['corpus/knowledge/linked.md']
read_tree -> 'OUTSIDE_SYMLINK_PAYLOAD\n'
_md_count: 1
```

Directory symlinks are **not** followed (default `followlinks=False`), which is
the only reason the frozen GROUND scope `corpus/knowledge` is safe today
(`claims-C.skeleton.json` sweeps use `"scope": "corpus/knowledge"`, and base has
no `120000` entry there):

```
tree_files -> []
_grep_tree UNIQUE_DIRLINK_PATTERN -> []
_md_count -> 0
```

Risk for the freeze: a lands tree may commit
`corpus/knowledge/<entry>.md` as mode `120000` whose blob is any path — including
`/tmp/...`. `ENTRIES`, `COLLCHECK`, `GROUND` (`_grep_tree`, `2192`) and the
`FROZENCFG` file-set comparison (`tree_files(mat, ".")`, `1234`) would then grade
content that is not committed. No leg rejects mode `120000`. Required fix:
`read_tree`/`_grep_tree`/`tree_files` must `os.path.islink`-reject (or
`realpath`-confine to the materialized tree), and at least one leg must assert no
`120000` entry inside the entry/corpus scopes.

`scratchmirror-real.py:41` `shutil.copytree(LANE/.ufo/waves/round-77/assimilation, assim)`
uses the default `symlinks=False`; measured on the same call shape:

```
copied path is a symlink: False
copied bytes: external bytes
```

Today safe only because `find .ufo/waves/round-77/assimilation -type l | wc -l`
is `0`; one symlink added to the staging dir is copied as target content.

## N4/N5 — wave-1 `/tmp` findings still open (carried, re-measured)

- **N4** `accept-ca.py:456-471` has no banned-root branch at all:

```
accept-ca.scratch_dir('/tmp/et2-ca-direct')      -> /tmp/et2-ca-direct | exists: True
$ python3 -B ExecAdaptCa/accept-ca.py --root <lane> --ledger-check <W>/empty-ledger.json \
      --base 211f9526800906e0c585d878d265c37e5e090c15 --work /tmp/et2-ca-run
     round=None != 77
     claim=None
     pairs=0 < the 10-pair floor
exit=1                                   # a ledger verdict, not a scratch refusal
$ find /tmp/et2-ca-run -maxdepth 2
/tmp/et2-ca-run                          # the counter created its root under /tmp
```

- **N5** `capture-evidence.py:590-603` still returns `None` with no root named:

```
work_base(None) -> None
make_work_dir(None) -> /tmp/capture-evidence-6ytzhy3c | realpath: /tmp/capture-evidence-6ytzhy3c
proof.txt exists: True
$ env -u TMPDIR -u HYAKU_SCRATCH -u SHOKUNIN_SCRATCH python3 -B ExecAdaptCapture/capture-evidence.py --selftest
SELFTEST OK: 36 scenarios                exit 0        # green while writing under /tmp
```

The tool's own selftest check `no-tmp-literal` only greps its own source for the
string `"/tmp` / `/tmp/`; it says nothing about `dir=None`.

## N6 — selftests cannot see any of this (process finding)

```
$ grep -rn 'os\.symlink\|symlink(' ExecAdaptC ExecAdaptCa ExecAdaptCapture ExecAdaptJunk ExecFreezeChecklist
$ echo "exit=$?"
exit=1                                    # no selftest creates a symlink
$ grep -rn 'check(".*\(link\|sym\|real\)' <the four tools>
    (no output)
```

The only scratch assertions in the wave's selftests are
`junk-fixtures.py:2289-2301` (`scratch tmp refused`, `scratch explicit`,
`scratch env`), `accept-ca.py:3356-3361` (`scratch-noroot`, refusal when nothing
is named), and `capture-evidence.py`'s `no-tmp-literal`. `junk-fixtures.py:2289`
is worse than useless: it asserts
`_forbidden_scratch(gettempdir() + "/r77")` is true, i.e. **the selftest
enshrines the F3 defect** (banning the operator's own `$TMPDIR`) and passes
either way, because a non-existent `$TMPDIR` makes `gettempdir()` fall back to
`/tmp`:

```
$TMPDIR=<W>/tmp-ok-dir -> REFUSED: FixtureError scratch root <W>/tmp-ok-dir/kotodama-r77-junk-fixtures is inside the system temporary directory...
$TMPDIR=/tmp          -> REFUSED: FixtureError scratch root /tmp/kotodama-r77-junk-fixtures is inside the system temporary directory...
```

Wave-1 carry-overs re-measured on the current bytes:

| W1 item | state now |
|---|---|
| F1 `accept-ca` accepts `--work /tmp` | **open** (N4) |
| F2 `capture-evidence work_base(None) -> None` | **open** (N5) |
| F3 junk-fixtures `$TMPDIR` branch dead / selftest codifies it | **open** (N6) |
| F4 `ExecFreezeChecklist/controls.sh:32 SCRATCH_BASE=${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotodama-r77}` drops the round segment when `HYAKU_SCRATCH` is the parent | **open** (`--scratch` exists at `38-39`; neither `--work` nor `$TMPDIR` is honoured) |
| F5 `ExecAdaptJunk/redbefore.py:19 WORK = "/fast/scratch/.../redbefore-work"` | **open** (unchanged hash) |
| I2 accept-ca `$HYAKU_SCRATCH` appends no round segment | **open**: `scratch_dir()` with `HYAKU_SCRATCH=/fast/scratch/hyaku` -> `/fast/scratch/hyaku` |

## Negative results (exact commands; empty output = clean)

```
$ grep -rnE '/tmp|os\.sep, ?"tmp"|gettempdir' <the five adapted tools>
    all hits are documentation, the C seat's refusal probe (scratch-probe.py:7,35,69),
    accept-c.py:2505 (the guard literal), junk-fixtures.py:431/435 (the gettempdir guard),
    junk-fixtures.py:150 SCRATCH_PARENT = "/fast/scratch/hyaku" (not /tmp), and the
    selftests' own probes. No hit is a write target.
$ grep -rn 'islink\|O_NOFOLLOW\|follow_symlinks\|lstat\|readlink' <the five tools + manifest-check>
    (no output, exit 1)
$ grep -rn 'os\.symlink\|symlink(' <.ufo/waves/round-77/w1/stage> --include='*.py' --include='*.sh'
    (no output, exit 1)
$ grep -rn '/fast/scratch' --include='*.py' --include='*.sh' . | grep -v ExecTmpAudit
    controls.sh:26,32; accept-c.py:134,2486,3194; accept-ca.py:30,271; capture-evidence.py:198;
    junk-fixtures.py:61,150,444,2293,2294,2345; redbefore.py:19; run-controls.sh:21,46,185,192;
    mutate_driver.py:34   -- all on /fast, none under /tmp
$ git -C <lane> ls-tree -r 211f9526… | awk '$1=="120000"' | grep corpus/knowledge
    (no output, exit 1: base has no symlink inside a graded corpus scope)
$ find .ufo/waves/round-77/assimilation -type l | wc -l
0
```

Positive model already in the wave (should be copied, not reinvented):

```
$ sed -n '193,197p' ExecFreezeChecklist/manifest-check.py
            if os.path.realpath(path) != os.path.realpath(os.path.join(root, rel)):
                rows.append((rel, "ESCAPES", "resolves outside the lane", None))
                continue
```

Scalers re-run over the current tree (unchanged verdicts):

```
$ python3 -B ExecTmpAudit/check-scratch-root.py --root . --paths '**/*.py' --paths '**/*.sh' --allow ExecTmpAudit/allow.txt
HIT       ExecTmpAudit/check-scratch-chain.py:422: env TMPDIR='/tmp'
checked=23 HIT(allowlisted)=1                       exit=0
$ python3 -B ExecTmpAudit/check-scratch-chain.py --root . --paths '**/*.py' --paths '**/*.sh' --allow ExecTmpAudit/allow.txt
checked=23 fatal=0                                  exit=0
```

## Selftest receipts collected this wave (green, on the snapshot above)

```
accept-c.py  --selftest                    SELFTEST: 37/37           exit 0
accept-ca.py --selftest (HYAKU_SCRATCH=sym) SELFTEST: 199/199          exit 0
accept-ca.py --selftest (TMPDIR=/tmp/et2-ca-t) SELFTEST: 199/199       exit 0
capture-evidence.py --selftest (--work sym/ce) SELFTEST OK: 36 scenarios exit 0
capture-evidence.py --selftest (no roots)  SELFTEST OK: 36 scenarios  exit 0
junk-fixtures.py --selftest                SELFTEST: PASS            exit 0
check-scratch-root.py --selftest           exit 0 (PASS hidden segment walked under **; PASS scanner writes nothing under a literal /tmp)
check-scratch-chain.py --selftest          selftest: 0 failure(s)     exit 0
```

Every one of these is green **and every one coexists with the defects above** —
the tests do not exercise symlinks, `--out` confinement, or `dir=None`.

## Implication for the freeze (no edit made here)

If the L1 installs these files as `reports/round-77/accept-c.py`,
`reports/round-77/accept-ca.py` and `reports/round-77/counters/capture-evidence.py`
unchanged, the frozen instruments admit: a symlinked scratch root onto `/tmp`
(N1), an evidence file written outside the lane through a symlinked `--out` (N2),
and a graded tree whose corpus content is read through committed symlinks (N3) —
while all six selftest suites print green. Minimum fix before freeze: realpath
the resolved root before the banned check (N1/N4), refuse `dir=None` and a
symlinked/non-confined `--out` (N2/N5), and make `read_tree`/`_grep_tree`
refuse or confine symlinks (N3); add one selftest per item that fails on the
current bytes.

## Bounds, scratch, cleanup

Read-only over the lane; no file edited (all 37 staged code hashes re-verified
`OK`). All probes ran from `/fast/scratch/hyaku/kotodama-r77/ExecTmpAudit2`
(symlink, fixture repo, claims JSON, selftest logs, probe harness) and the one
fixture git repo is `/fast/scratch/hyaku/kotodama-r77/ExecTmpAudit2/fixture-git`
(`git rev-parse --show-toplevel` asserted before and after its single commit).
Every `/tmp` probe target (`/tmp/et2-sym-target`, `/tmp/et2-out`,
`/tmp/et2-ca-direct`, `/tmp/et2-ca-t`, `/tmp/et2-ca-run`, `/tmp/et2-dirtarget`,
`/tmp/capture-evidence-6ytzhy3c`) was created by these probes only and is
removed before this report is yielded; the scratch tree is deleted too. No
pacman, no installs, no background jobs, no delegation.
