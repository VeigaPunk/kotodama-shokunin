# ExecAdaptScripts — round 76, wave 1 (build, stage only)

Verdict: **DONE**. The four round-75 orchestration tools are adapted to round 76 under
`.ufo/waves/round-76/w1/stage/ExecAdaptScripts/`, with a fifth tool (`selftest.sh`) that reruns the
data-free checks, and a data-driven landing skeleton (`apply-landing.py`) that takes
`--drafts <dir>` + `--claim ca|c` and refuses an incomplete draft set with exit 3 and no writes.
Nothing outside this seat's stage directory and its report was written; the lane's worktree, index
and git state are untouched (`git -C … status --porcelain` prints only the two pre-existing untracked
wave directories — see §6).

## 1. Staged files

| file | sha256 | lines | role |
|---|---|---|---|
| `freeze-set.sh` | `f4520d87e21ca22fae0e519f6ed417944c9f02bf251a8587a537c6b43e54e649` | 195 | prints the freeze set; `--check` names every missing mandated input |
| `run-controls.sh` | `797e9116fe22dd0a8e78f4910fdb285b205b1ce9570c16db0308973e8107ac01` | 194 | the two do-nothing controls per claim, at the freeze |
| `rehearse.sh` | `40151ae621d79421651d03981a1dfbeee686aac25e1ee30262381c4ee14aa7a8` | 225 | base → freeze → Ca → C in a scratch clone, then both counters |
| `apply-landing.py` | `20fcc1a6168432cde0d826c380d0f6fd21b0298cd84f5352ea96ab4e62014f0a` | 488 | manifest-driven draft-landing applier, two-phase |
| `selftest.sh` | `964c95535ae6d9e881fe34e2096e0852091f3e89428cc5bb005424be059939bc` | 147 | the seven data-free checks, `SELFTEST: 7/7` |
| `manifest.example.json` | `3e64a1be942ff5f1fd6db4eb9950d888585784295f543d0b8c4ccb26203b6504` | — | the schema example (also `apply-landing.py --print-example`) |

Command: `sha256sum freeze-set.sh run-controls.sh rehearse.sh apply-landing.py selftest.sh manifest.example.json`
in `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-76/w1/stage/ExecAdaptScripts`.

Receipts, copied from the scratch dir before it was deleted, live in `receipts/` beside the tools:
`static.out`, `selftest.out`, `rehearse-empty.out`, `rehearse-positive.out`, `apply-positive.out`,
`apply-negative.out`, `freeze.list`, `freeze-check.txt`.

## 2. What each tool does (round-76 changes vs round 75)

Round-75 originals read, never edited: `.ufo/waves/round-75/{freeze-set.sh,run-controls.sh,rehearse.sh,apply-landing.py}`.

`freeze-set.sh`
- Mandated core per the seat spec: `reports/round-76/{claims.json,ledger.json,accept-c.py,accept-ca.py,fixtures/*.json,telemetry/{selftest-c,selftest-ca,census-start,gap-sweep}.txt}`.
- Plus the by-document map `.ufo/waves/round-76/assimilation/id-renumber-map.json`, the collision-guard inputs
  (`reg-ids`, `staged-ids`, `collisions`, `build-map.py`, `substitution-table.txt`, `collision-documents.txt`),
  the guard proof (`assimilation/guard-proof/*`), `CLAIMS-DRAFT.md`, the orchestration scripts, the counters
  (`counters/**`), the wave markers (`w1.ready*`, `w2.ready*`) and the w1/w2/w3 evidence trees.
- New `--check`: prints `CHECK ok|MISSING <item>` to stderr and exits 1 when a mandated input is absent;
  stdout stays a pure, sorted, unique copy list. New `--root` (default: the git toplevel of the script's dir).
- `find` sweeps exclude `*.pyc` and `__pycache__`; the tool is read-only.

`run-controls.sh`
- Round tokens moved to 76: `T=reports/round-76/telemetry`, `WA=.ufo/waves/round-76`, base
  `98c486bdb4650ba5b8e651d332910e8ee60ad121`, counter fallback `.ufo/waves/round-76/counters/`.
- Both counters now get `--fleet-root` and `--work` (`${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotodama-r76}/controls`),
  so the routed `/tmp` defect cannot reappear through the driver.
- New `--combined REV` (passed to `accept-ca.py`; without it the Ca COMBINED leg is red by construction — the
  round-75 control shape), `--base`, `--junk REV` (round-76 `junk-fixtures.py`, split into `junk-c.txt`/`junk-ca.txt`).
- Each control receipt now carries an `# expected: exit=…` line naming the frozen do-nothing shape.
- Guards: freeze/base must be 40-hex commits in the lane; counters must exist before any receipt is opened.

`rehearse.sh`
- Scratch: `${HYAKU_SCRATCH:-/fast/scratch/hyaku/kotodama-r76}/L1-rehearse` (`--scratch` overrides); clone is
  `git clone -q --shared` of the lane, checked out at `--base` (default `98c486b…`).
- Asserts `git -C "$D" rev-parse --show-toplevel` == `$D` before the first commit; every later git call names
  `-C "$D"`; the identity is `-c user.name=rehearsal -c user.email=r@r.invalid -c commit.gpgsign=false` per
  command, never written to config.
- Freeze: `freeze-set.sh` list copied, `--check` consulted (refuses on missing mandated input unless
  `--allow-missing-freeze`), one commit → `F`.
- Landings: `apply-landing.py --root "$D" --claim ca|c --drafts <dir> [--manifest <file>]`; a refusal stops the
  run with `REFUSED: claim <x> landing — apply-landing.py exit 3 …` and exit 3.
- Measurement: both counters from the clone with `HYAKU_SCRATCH` and `TMPDIR` pointing into the scratch dir and
  `--work` inside it; Ca gets `--combined` (default: the C rev this run produced). Prints `F= CA= C= D=`.
- Exit codes: 0 both counters ran, 2 setup error (clone/freeze set/counter missing), 3 draft refusal.
- New: tools are located via the script's own directory (`REHEARSE_TOOLS` overrides), so the staged set is
  rehearsable before installation; drafts default to the installed `w2/stage`.

`apply-landing.py` (skeleton, data-driven)
- CLI: `--root`, `--claim ca|c`, `--drafts`, `--manifest`, `--check`, `--allow-lane`, `--print-example`.
- Manifest (`<drafts>/manifest.json`): `{"round":76,"claims":{"ca":{"ops":[…]},"c":{"ops":[…]}}}`; each op is
  `copy`, `copy_glob`, `append`, `insert_block`, `replace`, `assert`. The example manifest carries exactly the
  round-76 landing shapes: SOURCES rows block, entry files, README rows + heading count + footer, SKILL rows +
  line repair, QUALITY/SCORECARD appends, the round-75 lesson corrections append, evidence `copy_glob`.
- Two phases: every op is planned against an in-memory copy of the target tree (sources exist and are
  non-empty, anchors match the declared count, `replace` hits its declared occurrence count, destinations do not
  already exist unless `overwrite`, `append` guards absent, path traversal rejected); only a clean plan writes.
  A failure prints one `REFUSED: claim <c> op <n> (<op>): …` line and exits 3 with nothing written.
- Root guards: `--root` must be a git worktree toplevel (`git -C <root> rev-parse --show-toplevel` == root) and
  may not be the live lane without `--allow-lane`.
- Anchors are Python `re` patterns (no POSIX `[[:space:]]`); documented in the docstring and exercised by the
  selftest. Round-75's `LINE-REPLACE` record shape is accepted by `replace {"from": …, "to": …}` with a lone
  `==>` separator line.

`selftest.sh` — `sh -n` (4 scripts), `shellcheck -S warning` (4), `py_compile` (apply-landing), no literal
`/tmp` scratch root in the five tools, example-manifest JSON/regex validity, traversal refusal (exit 3),
empty-drafts rehearsal (`freeze: F=…` then `REFUSED`, exit 3). Scratch: `<scratch>/selftest`, deleted on exit.

## 3. Static evidence

Command and raw output (`receipts/static.out`):

```
$ sh -n freeze-set.sh run-controls.sh rehearse.sh selftest.sh
sh -n ok: freeze-set.sh
sh -n ok: run-controls.sh
sh -n ok: rehearse.sh
sh -n ok: selftest.sh
exit=0

$ shellcheck -S warning freeze-set.sh run-controls.sh rehearse.sh selftest.sh
shellcheck exit=0

$ PYTHONPYCACHEPREFIX=$S/pyc python3 -m py_compile apply-landing.py
py_compile exit=0

$ grep -nE '"/tmp|/tmp/' freeze-set.sh run-controls.sh rehearse.sh apply-landing.py
grep exit=1 (1 = no match, the required result)
```

The fourth check is the prompt §7.4 check verbatim, run on the four tools; it prints nothing, exit 1.
`selftest.sh` was reworded so its own pattern does not self-match (`grep -nE '"/tmp|/tmp/' selftest.sh` →
exit 1 as well).

`sh selftest.sh --scratch /fast/scratch/hyaku/kotodama-r76/ExecAdaptScripts/selftest` (`receipts/selftest.out`):

```
SELFTEST ok   syntax (sh -n on four scripts)
SELFTEST ok   shellcheck -S warning (clean)
SELFTEST ok   py_compile apply-landing.py
SELFTEST ok   no literal /tmp scratch root
SELFTEST ok   manifest.example.json parses, round 76, anchors compile
SELFTEST ok   traversal draft refused (exit 3)
SELFTEST ok   empty drafts: freeze committed, landing refused (exit 3)
SELFTEST: 7/7
```

(shellcheck first reported SC1007 on `CDPATH= cd`; changed to `CDPATH='' cd` and the warning is gone —
`shellcheck exit=0` above is the post-fix run.)

## 4. Freeze set

`sh freeze-set.sh | wc -l` → 293 lines at the time of writing (the wave-1 stage trees are still growing, so the
count moves with sibling seats; the mandated inputs do not). Head/tail of the list and the `--check` result
(`receipts/freeze.list`, `receipts/freeze-check.txt`):

```
$ sh freeze-set.sh --check >/dev/null
CHECK MISSING reports/round-76/claims.json
CHECK MISSING reports/round-76/ledger.json
CHECK MISSING reports/round-76/accept-c.py
CHECK MISSING reports/round-76/accept-ca.py
CHECK MISSING reports/round-76/fixtures/*.json (no match)
CHECK MISSING reports/round-76/telemetry/selftest-c.txt
CHECK MISSING reports/round-76/telemetry/selftest-ca.txt
CHECK ok      reports/round-76/telemetry/census-start.txt
CHECK MISSING reports/round-76/telemetry/gap-sweep.txt
CHECK MISSING .ufo/waves/round-76/assimilation/id-renumber-map.json
CHECK ok      .ufo/waves/round-76/assimilation/guard-proof/* (9)
CHECK ok      .ufo/waves/round-76/w1/spec.json
CHECK ok      .ufo/waves/round-76/w1/dispatch.json
CHECK ok      .ufo/waves/round-76/w1/swarm-registry.json
freeze-set: mandated inputs missing (see CHECK MISSING)
exit=1
```

This is the correct pre-freeze state: the round-76 claims/ledger/counters/fixtures/selftests/by-document map
do not exist yet, and `--check` names each one instead of letting a short freeze pass silently.

## 5. Rehearsal and landing evidence

### 5.1 Empty draft set refuses cleanly (the requested demo)

`sh rehearse.sh --drafts <empty dir> --allow-missing-freeze --scratch …` → **exit 3**
(`receipts/rehearse-empty.out`):

```
freeze: F=3ce4389ded68d67c910f60287f00ea6f79f98c14 base=98c486bdb4650ba5b8e651d332910e8ee60ad121 files=293
--- apply-landing --claim ca --drafts /fast/scratch/hyaku/kotodama-r76/ExecAdaptScripts/empty-drafts
REFUSED: manifest not found: …/empty-drafts/manifest.json (the draft set is incomplete)
REFUSED: claim ca landing — apply-landing.py exit 3 (drafts=…; freeze 3ce4389d… already committed on base 98c486b…)
rehearse: stopping after the freeze (no Ca landing); scratch kept at …
```

The freeze commit is built first (`F=3ce4389d…`, from the lane's base plus the current freeze list), then the
landing is refused before any byte is written.

### 5.2 Positive path: freeze → Ca → C in the clone

`sh rehearse.sh --drafts drafts-positive --manifest manifest-copy.json --allow-missing-freeze --scratch …` →
**exit 2** at the missing counter, after both landings (`receipts/rehearse-positive.out`):

```
APPLIED claim=ca ops=2 wrote=2 root=…/lane
APPLIED claim=c ops=8 wrote=4 root=…/lane
F=6b6399ddfa8b68f42800fe8d125d62107e57b5dd CA=fd3ec637e4805432b5ca44a12f81a7e0163bb32b C=ee64118afe3c7e0184bec1d2e604f6d26a3d65ba D=…/lane
rehearse: no freeze-installed counter at reports/round-76/accept-c.py in the clone; stopping before measurement
```

Exit 2 is the documented setup-error code for a counter that is not yet installed; the counters do not exist in
this wave (ExecAdaptC / ExecAdaptCa are still building them).

### 5.3 `apply-landing.py` mechanics, against a base fixture

Fixture: `git clone -q --shared <lane> $FIX && git -C $FIX checkout -q -B main 98c486bdb4650ba5b8e651d332910e8ee60ad121`;
`git -C $FIX rev-parse --show-toplevel` == `$FIX`, head == base (asserted in the transcript header).
`receipts/apply-positive.out`, abridged:

```
$ python3 -B apply-landing.py --root $FIX --claim c --drafts drafts --check
PLAN assert       corpus/SOURCES.md
PLAN copy         corpus/knowledge/culture-material/test-entry.md
PLAN insert_block corpus/SOURCES.md
PLAN insert_block corpus/README.md
PLAN replace      corpus/README.md
PLAN append       corpus/README.md
PLAN copy_glob    reports/round-76/evidence/S894.txt
PLAN assert       corpus/README.md
PLAN claim=c ops=8 would-write=4 root=… (nothing written)

$ python3 -B apply-landing.py --root $FIX --claim c --drafts drafts
…
APPLIED claim=c ops=8 wrote=4 root=…
exit=0

$ python3 -B apply-landing.py --root $FIX --claim ca --drafts drafts
…
APPLIED claim=ca ops=2 wrote=2 root=…
exit=0

$ git -C $FIX status --porcelain; git -C $FIX diff --stat
 M SKILL.md
 M corpus/QUALITY.md
 M corpus/README.md
 M corpus/SOURCES.md
?? corpus/knowledge/culture-material/test-entry.md
?? reports/round-76/
 SKILL.md          | 1 +
 corpus/QUALITY.md | 2 ++
 corpus/README.md  | 5 ++++-
 corpus/SOURCES.md | 1 +
 4 files changed, 8 insertions(+), 1 deletion(-)
```

The diff shows the row landed after `| S893 |` in `corpus/SOURCES.md`, the index row at the end of the
`culture-material` section (anchor `^## synthesis/ \(`, `where: before` — the correct round-76 anchor: the
`culture-material` heading itself is the *start* of the section), the heading count `(40) → (41)`, the footer
appended, `SKILL.md` gate row after `| accept-ca-75 |`, and the QUALITY append.

### 5.4 Refusals (every one exit 3, nothing written)

`receipts/apply-negative.out`:

```
N1 --root is the live lane …            REFUSED: --root is the live lane …; pass --allow-lane …
N2 --check against the live lane        before/after status digest identical: 21e031894795b9650a69a650e294b20cc26d2b5a6ad1d417b68b4bb07be8cde5
N3 apply twice                          REFUSED: claim ca op 1 (append): append guard already present in corpus/QUALITY.md: '…'
N4.traversal                            REFUSED: claim c op 1 (copy): copy.from escapes its base directory: '../escape.md'
N4.replace-count                        REFUSED: … the old text occurs 0 times, manifest expects 7: '## culture-material/ (41)'
N4.anchor-ambiguous                     REFUSED: … anchor matched 9 lines in corpus/README.md (want 1): [343, 375, 409, 451, 483, 509, 607, 787, 800]
N4.missing-draft                        REFUSED: … draft missing: corpus/nope.md (looked at …)
N4.empty-ops                            REFUSED: claim 'c' has no ops (drafts incomplete): …/manifest.json
N4.wrong-round                          REFUSED: manifest is for round 75, this applier is round 76
N4.unknown-op                           REFUSED: claim c op 1 is not a known op: {'op': 'frobnicate', 'to': 'x'} …
N5 empty drafts directory               REFUSED: manifest not found: … (the draft set is incomplete)
N6 root is not a git worktree           REFUSED: --root is not a git worktree: …
```

All 11 `^exit=` lines in that file are `exit=3`, and the fixture the refusals ran against ends with an empty
`git status --porcelain` (`## FIXA is still clean` in the receipt). `--check` is proven write-free both by the
digest above and by the plan-only line `(nothing written)`.

## 6. Lane state (nothing mutated)

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin status --porcelain
?? .ufo/waves/round-76/
?? reports/round-76/
```

Both entries pre-date this seat (round-76 wave directories were already untracked). No lane file, index, ref or
identity was touched; no commit, add, checkout, stash, reset or switch was run in the lane. The counters were
never edited (ExecAdaptC / ExecAdaptCa own them). No packages were installed.

## 7. Not run, and why

- The counters themselves: `reports/round-76/accept-c.py` and `reports/round-76/accept-ca.py` do not exist yet.
  `run-controls.sh` was exercised up to its counter-presence guard only:
  `HYAKU_SCRATCH=… sh run-controls.sh 98c486b…` → `ERROR: no round-76 counter found … exit=2`, and
  `reports/round-76/telemetry/` was byte-identical before and after (only `census-start.txt`, 3776 B,
  mtime 18:27).
- A real freeze rehearsal: the mandated freeze inputs (§4) are still missing, so the empty-draft run uses
  `--allow-missing-freeze`; without it `rehearse.sh` refuses at the freeze-set check, exit 2.
- `--junk`: needs `junk-fixtures.py` (ExecAdaptJunk) and a landing revision.

## 8. Handoff notes for the L1

1. The counters must accept `--root`, `--lands`, `--freeze`, `--fleet-root`, `--work`; `accept-ca.py` must also
   accept `--combined` and must not require it for a do-nothing control (control 1 runs without it and the
   COMBINED leg is expected red there).
2. The freeze must carry `reports/round-76/fixtures/*.json` (the freeze-set `--check` treats the glob as
   mandated) and `reports/round-76/telemetry/{selftest-c,selftest-ca,census-start,gap-sweep}.txt`.
3. The landing drafts (`w2/stage`, or any `--drafts`) need a `manifest.json`; the ops are the only place paths
   live. `manifest.example.json` is the worked shape; `apply-landing.py --print-example` reproduces it.
4. Anchor regexes are Python `re`; for the README index use `^## synthesis/ \(` (`where: before`) for
   culture-material rows, `^## culture-material/ \(` for myth-symbol-style rows, `match: last` for the
   `corpus/SOURCES.md` id anchor.
5. `--allow-lane` is required for the real landing into the lane worktree; rehearsal clones never need it.
6. `selftest.sh` is the pre-freeze gate: `SELFTEST: 7/7` and exit 0.

## 9. Scratch

All scratch lived in `/fast/scratch/hyaku/kotodama-r76/ExecAdaptScripts/` (clones, fixtures, draft sets,
transcripts) and was deleted after `receipts/` was copied; the shared
`/fast/scratch/hyaku/kotodama-r76` parent was left in place. No `/tmp` path is cited anywhere.
