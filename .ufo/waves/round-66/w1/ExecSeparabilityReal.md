# ExecSeparabilityReal — real separability probe (judged axis: operability)

**Verdict: PROBE BLOCKED, no round-66 verdict produced** — `reports/round-66/separability-manifest.json`
is absent and two declared lands are still missing, which is the assignment's explicit exit
condition. The probe harness itself was proven live on a read-only copy of the lane, and the
pre-flight against the declared design surfaced two integration-breaking defects in the
manifest the L1 is about to write.

Evidence written: `.ufo/waves/round-66/stage/separability-real-probe.txt` (job's declared path).
Lane files not edited. No commit, no jj/git write. No tool installed or upgraded (pacman untouched).

## Measured state at probe time

| input | state |
|---|---|
| `reports/round-66/separability-manifest.json` | **ABSENT** |
| `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md` (C land) | **ABSENT** |
| `corpus/lessons/round-66.md` (Ca land) | **ABSENT** |
| `reports/round-66/telemetry/separability-real.txt` (Ca land) | **ABSENT** |
| `tools/check-claim-separability.py` | present, 69554 B, executable |
| lane `main` ref | `94209e8f…` == base |

`find . -iname '*separab*manifest*'` shows only rounds 51–63 plus
`.ufo/waves/round-65/stage/separability-manifest.json`; no round-66 draft exists anywhere.

## What I ran (copy-safe; lane's `.jj` excluded, lane git index/jj never touched)

Copy: `tar -C <lane> -cf - --exclude=./.jj . | tar -C /tmp/r66-probe-copy -xf -` (1019M, 2.1s).

### A. Declared command, manifest absent → exit 2, honest
```
cd /tmp/r66-probe-copy && python3 -B tools/check-claim-separability.py \
  reports/round-66/separability-manifest.json --jobs 4 --timeout 120 --budget 300 \
  --root /tmp/r66-probe-copy --lane /tmp/r66-probe-copy
exit=2
stdout: (empty)
stderr: SEPARABILITY_INPUT_ERROR cannot read manifest 'reports/round-66/separability-manifest.json': No such file or directory
```
Empty stdout is the important part: an absent input cannot be misread as `SEPARABILITY: 0 findings`.
The declared flags all parse, so `--jobs/--timeout/--budget` (O leg OPTIONS) hold at the entry point.

### B. Plumbing positive control (one WORKTREE unit, same flags) → exit 0, live
```
SEPARABILITY: 0 findings
SEPARABILITY_NOTE units=1 ordered_pairs=0 acceptance_runs=0 skipped=0
```
Manifest load, `--root`/`--lane` on a foreign copy, static leg and report line all work. Only the
round-66 manifest and the build lands are missing — the harness is not the blocker.

## Findings

**F1 (BLOCKER, dependency).** Manifest and two lands absent — probe impossible today. Any
`stage/separability-real-probe.txt` claiming a verdict before those land is fabricated.

**F2 (DEFECT, will break integration).** `claims.json` → `separability.manifest_units` is a keyed
dict, and the tool requires the top-level key `claims` as a **list** (`MANIFEST_KEYS =
frozenset(("schema","base","claims"))`, line 111; parse at line 404). Copying the declared block
verbatim yields `SEPARABILITY_INPUT_ERROR manifest is missing claims`, exit 2. The manifest must be
authored as `{"schema": "...", "base": "...", "claims": [ {id, tree, lands, exports, …}, … ]}`.

**F3 (DEFECT, will break integration, two occurrences).** Land paths are canonicalized and any
trailing slash is rejected (`_repo_path`: "empty, '.' or '..' component"). Both occurrences are in
the frozen `claims.json`:
- O: `.ufo/waves/round-66/stage/mut-o/` → `SEPARABILITY_INPUT_ERROR claims[1].lands[1] is not canonical …`
- REC: `.ufo/waves/round-66/w1/` → same error (isolated reproduction, exit 2).
Fix: drop the trailing slash (`…/stage/mut-o`, `…/w1`) in the manifest. `.ufo/` paths themselves are
accepted once canonical. Note the same slash appears in O's `lands` inside `claims.json` — the O
counter's own land list is unaffected (that is a different instrument), but the manifest copy needs
the fix.

**F4 (TRAP, decisive for probe semantics).** `main` at the lane tip still equals the base
(`git rev-parse --verify main` → `94209e8f…`). With `tree: "main"`, every land new this round is
`absent at its tree` → `SEPARABILITY_INPUT_ERROR`, even after the drafts are on disk. Units carrying
new lands must declare `"tree": "WORKTREE"` (or the L1 must advance `main` before the probe). This is
also why a probe of a *draft* tree can only work with WORKTREE units.

**F5 (positive control on the honest failure path).** On a correctly shaped manifest whose C land is
absent, the tool fails closed with exit 2 and a message naming the missing path — both with the full
dynamic flags and with `--static-only`. No fabricated `<base>` line, no partial verdict emitted, no
`SEPARABILITY:` line: the "never fabricate" property of O holds at the real entry point.

## Ready-to-run at integration (unchanged command shape)

```
tar -C <lane> -cf - --exclude=./.jj . | tar -C /tmp/r66-real -xf -
cd /tmp/r66-real && python3 -B tools/check-claim-separability.py \
  reports/round-66/separability-manifest.json --jobs 4 --timeout 120 --budget 300 \
  --root /tmp/r66-real --lane /tmp/r66-real
```
Pass `--lane` explicitly at the copy: the default is the repo holding the script, which is the lane
if the probe is launched with the lane's script path. Acceptance: a `SEPARABILITY:` line with exit 0
or 1 and exactly the declared Ca→REC class, or exit 2 with `SEPARABILITY_PARTIAL` +
`SEPARABILITY_UNRESOLVED` (an honest partial, never a fabricated `<base>`).

## Risks / blockers
- The probe cannot be closed in this wave seat: F1 is a hard dependency on the C/Ca build seats and
  the REC scribe. Do not treat `stage/separability-real-probe.txt` as the round-66 receipt.
- Timing is unmeasured for the integrated run (no real manifest existed to measure against). The
  fixture-level 180s bound is `accept-o.py`'s leg, not this probe's; nothing here contradicts O.
- Scratch copy `/tmp/r66-probe-copy` and `/tmp/preflight-*.json`, `/tmp/*slash*.json`,
  `/tmp/worktree-pos.json` are disposable probe inputs, outside the lane and outside the wave tree;
  none is a land of any claim.
