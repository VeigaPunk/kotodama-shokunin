- Seat: A03 | executor (scope watch, claim A) | claim A (adjacency) | date 2026-10-19 | baseline 139e3b6

# A03 — Scope watch (round 33, regimen 2 opening)

Write scope: this file only. No scratch file was created by this seat; every
command below is read-only (`git status`, `git ls-files`, `git ls-tree`,
`git diff`, `stat`, `find`, `sha256sum`, `grep`). No install, no network, no
Git-mutating command, no commit or push. Commands ran with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

## Verdict

**PASS at the final reading (2026-10-19T03:57:47Z) with one named finding.**
The tracked surface is byte-clean against baseline `139e3b6`: **2655 tracked
paths** at HEAD and 2655 at the baseline commit, **zero** tracked-file delta
baseline→HEAD, and **zero** working-tree rows under the protected roots
(`reports/round-1..32`, `corpus/lessons`, `tools/gates/frozen`). The only
working-tree delta is the declared, in-lane one: the append-only `LOG.md`
entry, the new `REGIMEN.md` contract, and the untracked `reports/round-33/`
wave surface.

Named finding **A03-F1**: between 03:53:25Z and 03:55:27Z a writer re-ran the
historical validators **in-tree**, which rewrote filed receipts
`reports/round-5/validation.json` and `reports/round-7/validation.json` in
place; both were restored to their committed bytes at 03:55:27Z. The end state
is clean, but the write class is forbidden by `targets.json` `shared_rules[1]`
and is the same hazard already on record from rounds 20 and 28. Routed to the
integrator (restore is done; the record and the repeat-prevention are not).

## Baseline binding and census

`reports/round-33/claims.json` `baseline_commit` = `139e3b662900557afe54f632b468619593dc9fcb`;
`git rev-parse HEAD` = the same value, so the declaration-time and observed
revisions coincide and no baseline-to-HEAD drift is possible.

| count | command | value |
|---|---|---|
| tracked paths, worktree | `git ls-files \| wc -l` | **2655** |
| tracked paths, baseline tree | `git ls-tree -r --name-only 139e3b6 \| wc -l` | **2655** |
| tracked delta baseline→HEAD | `git diff --stat 139e3b6..HEAD` | **empty** |
| reports/round-1..32 tracked | `git ls-files reports/round-{1..32} \| wc -l` | **1830** |
| corpus/lessons tracked | `git ls-files corpus/lessons \| wc -l` | **179** |
| tools/gates/frozen tracked | `git ls-files tools/gates/frozen \| wc -l` | **237** |
| reports/round-33 tracked | `git ls-files reports/round-33 \| wc -l` | **0** (wave surface, untracked by design) |

The declared regimen-2 opening baseline of 2655 tracked paths
(`reports/round-33/claims.json` claim A `before.state`) is therefore confirmed
at HEAD, not merely asserted: 2655 = 2655, and the three protected roots above
account for 2246 of them.

## Working-tree inventory

Final reading, `git status --porcelain`, **2026-10-19T03:57:47Z** — 3 rows:

```
 M LOG.md
?? REGIMEN.md
?? reports/round-33/
```

- ` M LOG.md` is a **pure append**: `git diff --stat LOG.md` → `18 insertions(+)`,
  0 deletions; the added block is the dated `2026-10-19 — Regimen 2 contracted
  by operator directive (rounds 33–74)` entry. Append-only discipline holds.
- `?? REGIMEN.md` is the operator-approved round contract (mtime
  `2026-10-19 00:42:09 -0300`), explicitly inside claim A's own scope-delta
  allowance ("scope delta fully explained by `reports/round-33/` + REGIMEN.md/
  LOG.md append entries").
- `?? reports/round-33/` is the wave write surface (claims/targets/telemetry
  plus the seat fragments); 0 of its files are tracked at HEAD, so no filed
  byte is involved.
- `git status --porcelain -uall` restricted to `reports/round-1..32`,
  `corpus/lessons` and `tools/gates/frozen` at the final reading → **0 rows**.

## A03-F1 — filed receipts rewritten in place, then restored (named finding)

**Class:** in-tree re-run of historical validators. `reports/round-5/run-validation.py`
writes `HERE / "validation.json"` (`reports/round-5/run-validation.py:194`) and
`reports/round-7/run-validation.py` does the same
(`reports/round-7/run-validation.py:1171-1172`), so executing either in the
lane root rewrites the filed receipt as a side effect. This is a recurring
hazard, on record twice: `corpus/lessons/round-20.md:120` observes the *same
signature* (round-5 `claims.O.error` moving from a battery error string to a
`replay-frozen.py` could-not-evaluate string, with
`tested_file_sha256."tools/check-gate-battery.py"` `0a126b70…` → `cd8c0ec2…`),
and `reports/round-32/scope.md:171` restates it from
`reports/round-28/scope.md:12` ("a historical round-27 battery rewrote a filed
receipt even when invoked with `--check`") — the round-28 case was also a
rewrite-then-restore of a filed artifact (`reports/round-27/gate-tests/receipt.json`,
rewritten 20:13:21Z, restored 20:14:42Z).

Observed timeline (all times UTC; local `-0300` mtimes in parentheses):

| time | event | evidence |
|---|---|---|
| 03:52:20Z | clean: 3 status rows | `git status --porcelain` (this seat) |
| 03:53:25–28Z | in-tree r5/r6/r7 run #1; r5+r7 mutated | mtimes `00:53:25.196`/`00:53:28.557` |
| 03:54:15–18Z | in-tree run #2 | mtimes `00:54:15.802`/`00:54:18.608` (`reports/round-33/adj/A01-province.md:106-108`) |
| 03:54:32–35Z | in-tree run #3 | mtimes `00:54:32.592`/`00:54:35.490` (this seat, sample 1) |
| 03:54:37Z | isolated copy created | `.scratch/c05-iso/` dir mtime `00:54:37.367` |
| 03:54:39–42Z | isolated-leg runs (correct practice) | `.scratch/c05-tmp/r{5,6,7}.log` mtimes `00:54:39.695`/`00:54:39.725`/`00:54:42.679`, identical to the nanosecond with the iso receipts they captured |
| 03:55:27Z | **restored**: r5+r7 back to committed bytes | mtimes `00:55:27.940762254` both; `git status` clean at 03:55:39Z (`reports/round-33/adj/A16-shonen-material.md:209`) |
| 03:57:47Z | final reading: clean, 2655 tracked | this seat |

Digests at the mutated reading (03:55:25Z sample) versus the filed bytes:

| path | mutated (observed) | filed / final (restored) |
|---|---|---|
| `reports/round-5/validation.json` | `fe926984e8d15728c43c44b2fc4c0f60058f784aa4aa4b7c2e6aecc04a4dfeee` | `73a66f7464ead0d99318750422256ceafac3d8c2d283f94604eb258abc1bb794` |
| `reports/round-6/validation.json` | `32c621efaccca71db3b49a9151e3a37fd3663bcd97d9a6a71d745f6034158441` (unchanged throughout) | same |
| `reports/round-7/validation.json` | `af0cf4ed32d68c2b96284b49de97cfe75900c512299d4dd7423580e9573912a4` | `2f4c1e159b60d78250074c51f013d13aac3cf1b140a623d197a0883e5ecac6f3` |

Mutation shape (read-only diff inspection): round 5's `claims.O.error` changed
from a `tools/check-gate-battery.py` exit-2 baseline-coverage failure to a
`tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` exit-2
`gate_digest_mismatch` could-not-evaluate (7/7 rows), and
`tested_file_sha256."tools/check-gate-battery.py"` moved
`0a126b70afa6cbd5c2565b57399c318788540e10c4940d07c906718c8b9e1aa1` →
`455b595ad6d5b1be7844fc9b53a259a5b8a0efbd788b129dbfd2cc0d0ad173ce`; round 7's
`failures[1]` inventory totals moved `{files: 189, raw_lines: 688, …}` →
`{files: 201, raw_lines: 717, …}`. Both are live-re-measurement contamination
of historical receipts, not corrections — no seat declared a refresh, and
`acceptance_checks_passed` stayed `false` in both files. Round 6 came out
byte-identical (re-run, same bytes), so it carries no residual risk.

**Probable writer — `to-verify`:** the round-33 **C05** seat (calibration item
5). Basis: the only new scratch namespace matching this exact r5→r6→r7 chain is
`c05-*`; `.scratch/c05-tmp/r{5,6,7}.log` captures the chain's stdout, and
`.scratch/c05-iso/` is a clean committed-tree copy (`sha256sum
.scratch/c05-iso/LOG.md` = `3e786a819bc0fee6433222e6…` = `git show HEAD:LOG.md
| sha256sum`) holding the isolated leg. The in-tree leg's mtime spacing
(0.03 s between r5 and r6, ~2.9 s to r7) matches the isolated leg's spacing
(0.03 s, ~2.95 s) — one runner executed twice against two roots. No process
table or session log is readable by this seat, so the seat identity is
inference, not proof; the *class* (in-tree historical-validator run) is proven
by the diffs.

**Not an authorized refresh:** the round-23 precedent
(`c64b2b3 "refreshed validation receipt (close-time, receipt-guard
REFRESH_RECEIPTS=1)"`, cited at `reports/round-33/adj/A01-province.md:126`) is a
committed, guarded, integrator action. Here HEAD never moved
(`git rev-parse HEAD` = `139e3b6` at every sample), the guard env is absent from
every observed invocation, and the end state is the *pre-edit* revision — a
refresh would leave new bytes, not restore old ones.

**Disposition (integrator-owned):** the bytes are already restored, so no
repair is owed; what is owed is the record (LOG.md / telemetry note naming the
class, the two paths, the window and the restored digests) and the
repeat-prevention note. This seat did not write, and did not repair, any filed
byte. Corroborating independent observations exist at
`reports/round-33/op/O07-baseline-receipt.md:150-180` (routed to A03 + X02),
`reports/round-33/adj/A01-province.md:99-137` (A01-5) and
`reports/round-33/adj/A16-shonen-material.md:208-209`.

## Out-of-lane write scan

Nothing outside this repo was written by this lane during the round-33 window.

- `ls .ufo/reports/round-33` → **No such file or directory**; the fleet round
  report is not yet owed or filed, matching the mission's "none are owed this
  round".
- `find /home/vgpnk/Projects/shokunin/.ufo -type f -newermt "2026-10-19 00:00"`
  → exactly one path, `/home/vgpnk/Projects/shokunin/.ufo/reports/round-104/game-dev-2d.md`
  — another lane's own report, not kotodama.
- `.ufo/l0-questions.md` mtime `Oct 18 17:14` and
  `.ufo/scopes/kotodama-mint-20261017/` mtime `Oct 17 01:27`: untouched today.
- Fleet-root-wide scan, `find /home/vgpnk/Projects/shokunin -path '*/.git' -prune
  -o -type f -newermt "2026-10-19 00:40"` → 79 files, of which the kotodama-owned
  ones are **all inside this repo** (the LOG.md/REGIMEN.md/round-33 trio above,
  the r5/r6/r7 receipts, and `.scratch/` seat scratch); the remainder are
  `kotoba-shokunin/.ufo/round-21/**` and `kotoba-shokunin/verifiers/**` — that
  lane's own round-21 work.
- Non-scope observation, no owner, **not** a round-33 write: a stray directory
  `"/home/vgpnk/Projects/shokunin/bash: "` exists at the fleet root (mtime
  `Oct 18 14:01`, containing `home/vgpnk/Projects/shokunin/souji-shokunin/tests/tools/souji-verify.sh:
  No such file or directory` — a mis-quoted command's output captured as a
  path). It predates round 33 by ~11 h; flagged for fleet hygiene only.
- In-repo scratch: `.scratch/` is gitignored and explicitly the seat scratch
  area (`shared_rules[2]`); observed round-33 scratch namespaces (`o01-`, `o06-`,
  `o08-`, `r01-`, `r03-`, `c01-`, `c05-`, `k02-`) live there. Per AGENTS.md they
  are not durable artifacts; nothing in this fragment depends on scratch bytes
  except the c05 evidence cited above.

## Scope-watch counts and controls

- Detector: `git status --porcelain` + per-path `stat` mtime + `sha256sum`,
  sampled at 03:52:20Z, 03:55:25Z, 03:56:49Z, 03:57:47Z. The detector fired
  positively (A03-F1) and the end state was re-measured clean after the
  restore — a positive control from live data, not a fixture.
- `git ls-files | wc -l` was 2655 at every sample, so no path was added or
  removed under any root; the A03-F1 delta was content-only, in two tracked
  files.
- Nothing in the round-33 write surface left the repo: the only untracked
  directory outside the three declared rows is none.

## Limits

- mtime sampling cannot exclude a write-and-restore that falls entirely
  between two samples. Here the window *was* observed (two independent
  readings), which is the strongest form available to this seat, but the count
  of in-tree runs (three inferred from mtime spacing) is a lower bound.
- Attribution of A03-F1 to a specific seat is inference from scratch-namespace
  evidence and is marked `to-verify`; the mutation class is proven by the diffs
  alone.
- This is a scope verdict, not round acceptance, not a semantic review of peer
  fragments, and not a statement about fleet-root cleanliness beyond the
  scan surface named above (fleet root only; the wider host was not surveyed).
- No historical validator was executed by this seat, so no new side effect can
  originate here.

## Owed

- `reports/round-33/run-validation.py` — not present at 03:57:47Z
  (`ls reports/round-33/run-validation.py` → No such file or directory), so
  claim A's counting command (`python3 reports/round-33/run-validation.py`)
  cannot be run by any seat; the integrator writes it and must re-read this
  fragment's counts into it (A-legs: scope-watch counts, protected-root status
  rows, and A03-F1's routed finding).
- Re-read at round close: because a repeat in-tree validator run would recreate
  A03-F1's delta, the integrator should re-run `git status --porcelain -uall --
  reports/round-1..32 corpus/lessons tools/gates/frozen` (expect 0 rows) and
  compare the r5/r6/r7 digests against the filed values above before filing the
  round record.

## Citations

Paths and lines:
- `reports/round-33/claims.json` (baseline_commit, claim A `before.state`,
  thresholds, non_goals), `reports/round-33/targets.json` (`shared_rules`,
  A03 mission), `REGIMEN.md` (per-round contract, scope).
- `reports/round-5/run-validation.py:194` (writes `validation.json`),
  `reports/round-6/run-validation.py:283,336`,
  `reports/round-7/run-validation.py:8,1016,1171-1172`.
- `reports/round-32/scope.md:171` (historical-validator rewrite hazard, citing
  `reports/round-28/scope.md:12`), `corpus/lessons/round-20.md:120` (same
  signature observed in round 20).
- `reports/round-33/op/O07-baseline-receipt.md:150-205`,
  `reports/round-33/adj/A01-province.md:99-137,152`,
  `reports/round-33/adj/A16-shonen-material.md:208-209`,
  `reports/round-33/calib/P02-plan.md:20,31-33` (independent observations).
- `reports/round-33/telemetry/dispatch-declared.json` (declared dispatch,
  durable sources and digests).

Commands (all read-only, 2026-10-19, `TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`):
- `git rev-parse HEAD`; `git ls-files | wc -l`; `git ls-tree -r --name-only
  139e3b662900557afe54f632b468619593dc9fcb | wc -l`; `git diff --stat
  139e3b6..HEAD`; `git ls-files reports/round-{1..32} | wc -l`; `git ls-files
  corpus/lessons | wc -l`; `git ls-files tools/gates/frozen | wc -l`.
- `git status --porcelain` (03:52:20Z, 03:55:25Z, 03:56:49Z, 03:57:47Z);
  `git status --porcelain -uall -- reports/round-{1..32} corpus/lessons
  tools/gates/frozen` (0 rows); `git status --porcelain --ignored`.
- `git diff --stat LOG.md` (18 insertions, 0 deletions); `git diff
  reports/round-5/validation.json`; `git diff reports/round-7/validation.json`;
  `sha256sum reports/round-{5,6,7}/validation.json`; `git show
  HEAD:reports/round-{5,7}/validation.json | sha256sum`.
- `stat -c '%y %n'` on `LOG.md`, `REGIMEN.md`, `reports/round-33/**`,
  `reports/round-{5,6,7}/validation.json`, `.scratch/c05-tmp/*`,
  `.scratch/c05-iso/reports/round-{5,6,7}/validation.json`.
- `sha256sum .scratch/c05-iso/LOG.md` vs `git show HEAD:LOG.md | sha256sum`.
- `find . -path ./.git -prune -o -type f -newermt "2026-10-19 00:40" -print`;
  `find /home/vgpnk/Projects/shokunin/.ufo -type f -newermt "2026-10-19 00:00"`;
  `find /home/vgpnk/Projects/shokunin -path '*/.git' -prune -o -type f
  -newermt "2026-10-19 00:40" -print`; `ls -la /home/vgpnk/Projects/shokunin/.ufo/reports/round-33`.

FILES: reports/round-33/adj/A03-scope.md | SUMMARY: Scope watch PASS at 03:57:47Z — 2655/2655 tracked paths, zero protected-root rows, in-lane delta only (LOG.md append + REGIMEN.md + reports/round-33/), no out-of-lane kotodama write; named finding A03-F1 files the transient in-tree rewrite and restore of reports/round-5/validation.json and reports/round-7/validation.json (probable writer C05, to-verify), routed to the integrator with digests.
