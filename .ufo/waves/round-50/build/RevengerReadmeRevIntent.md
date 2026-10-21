# RevengerReadmeRevIntent: Claim O, BASE_COMMIT pin, skip() intent, fail-closed impact

Seat: RevengerReadmeRevIntent (revenger, leaf, no delegation). Milestone: Round 50 (C, O, Ca).
Judged on: coverage, operability, calibration.
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, `main` = `4ad26836` (round-50 base).

Method: lane reads only; git read-only (`rev-parse`, `cat-file`, `merge-base`, `for-each-ref`,
`log`, `show --stat`, `symbolic-ref`). Experiments only in `/tmp/r50-revenger` (clones and
exports, with fail-closed mutants copied from the base tool bytes). No jj command. No installs
or upgrades. The only lane write is this file.

## 1. Answer

1. **Why c42d675.** It is the parent of `c6a174d`, the round-49 commit that added
   `tools/check-readme-revisions.py` (388 lines) and removed the dangling `revision: 2.0` stub from
   `corpus/README.md` (`git show --stat c6a174d`). It is the last README carrying the r49 defect, and
   it is the round-49 frozen baseline (`reports/round-49/run-validation.py:46`, `BASELINE = "c42d675"`;
   LOG.md:3952-3954; SCORECARD.md:957-958). Only selftest control 9 reads it (tool:302-321).
2. **What skip() tolerates.** It has two call sites, both inside control 9: `git show` returning
   non-zero (tool:310-311) and `OSError`/`SubprocessError` (tool:320-321). It tolerates a tree that
   cannot resolve the pinned object: a shallow clone, a `git archive` or copy export, or no repository.
   The recorded intent is "SKIP not FAIL if object unreachable" (Ca-evidence.md:106-108; tool:64-66).
   The other ten controls use synthetic inputs and still gate.
3. **Does fail-closed break a documented workflow?** No documented admitted workflow breaks.
   - Full-clone round-49 replay (SCORECARD.md:959-961, "replayed in a fresh clone"): `verdict: admitted`
     at `4ad2683`, unchanged (the object resolves).
   - Default mode and `--readme` never read `BASE_COMMIT` (tool:360-369): unchanged in every tree.
   - Wave executor clones (`git clone -q <lane> <work>`): keep `c42d675` (checked on
     `.ufo/waves/round-50/work/ExecGuard`: `cat-file` rc 0, not shallow, HEAD `4ad2683`).
   - What does break: standalone `--selftest` in a shallow clone or git-less export goes rc 0 to rc 1.
     The round-49 runner in a git-less export was already `rejected-honest-stop`, because its C leg
     needs `git diff BASELINE` to exit 0 (run-validation.py:125-128, 136-139). Fail-closed also turns
     its Ca leg from a false `improved` (the SKIP exits 0) into `unprovable`. The verdict does not change.
   - The lane's own standard already excludes this use: SKILL.md:585-588 requires "a history-retaining
     copy (clone or worktree ...)", because "a plain tree export lacks" the pinned history. SKILL.md:419
     requires "could-not-evaluate" to stay distinct from pass.

## 2. Evidence chain

| Element | Evidence |
|---|---|
| Pin constant and intent | tool:64-67: `BASE_COMMIT = "c42d675be96b6b3957e6e5c00ab192080cb70083"`, comment "committed fixture (SKIP, not FAIL, when the object is unreachable)" |
| Introduced at | `git log -- tools/check-readme-revisions.py` lists only `c6a174d` (never edited since); `c6a174d` parent = `c42d675` |
| The defect the pin preserves | round-49.md:159-160 (`c42d675:corpus/README.md:55,57`); measured: `--readme` on `git show c42d675:corpus/README.md` gives rc 1, REVISION-DUP [55,57], REVISION-STUB [55] |
| Reachability today | `git merge-base --is-ancestor c42d675 4ad2683` rc 0; `for-each-ref --contains` lists `refs/heads/main`, `refs/remotes/origin/main`, `refs/jj/keep/4ad2683…`, `refs/jj/keep/13ae139…`; no keep ref names `c42d675` itself; lane not shallow |
| Control 9 | tool:302-321: `git -C LANE show c42d675:corpus/README.md`, timeout 30; assertion REVISION-DUP and REVISION-STUB |
| skip() and sites | tool:233-235 (appends name, prints SKIP, never touches `ok`); sites tool:310-311 and tool:320-321 |
| Verdict semantics | tool:344 prints `selftest skips: N`; tool:355-358 returns `0 if passed`; skips never enter the verdict |
| Exit-code contract | tool:34-36: 0 clean, 1 finding, 2 could-not-evaluate (the pin skip does not use 2) |
| Round-49 intent | Ca-evidence.md:88-111 (base run exit 1; `--selftest` 11/11; "SKIP not FAIL if object unreachable" at :106-108) |
| LOG entries | LOG.md:3940-3943 (r48 "runner reproduced in isolated git-archive replay (`.scratch/r48-replay`)", the archive precedent); :3944-3945 (X01 flags the duplicate `revision: 2.0`, "recorded for a later Ca round"); :3947-3954 (r49 framing; base `c42d675`; "declared premises transfer"); :3968-3971 (Ca landed; "selftest 11/11 ... exits 1 on the base README") |
| SCORECARD | :957-961 (baseline; fresh-clone replay; `verdict: admitted`); :970 (calibration row, "selftest 11/11") |
| Round-49 runner | run-validation.py:22-24 (acceptance "its --selftest exits 0"); :46 BASELINE; :125-128 `git diff --name-only BASELINE` and `no_overwrite`; :136-139 C verdict; :152-156 `rev_tool_ok` requires `rc_rs == 0`; :357-366 pins are written, not checked |
| Receipt pin | reports/round-49/validation.json:347 `d49fdf1c…` = sha256 of the tool bytes at `4ad2683` (verified) |
| Lane standard | SKILL.md:585-588 (history-retaining copy); :419 (keep could-not-evaluate distinct from pass); :579 (normal gates: 2 = could-not-evaluate) |
| Fleet R3 | `.ufo/waves/hyaku/jj-w1/reports/JjAuditKotodama.md`: :129-139 (silent SKIP, exit 0), :57 (CR:306 row), :188 (selftest row), :227-228 (recommendation 3) |
| Planned round-50 consumers | `.ufo/waves/round-50/build/ScribeLesson.md:97` (`--selftest` as a gate); `reports/round-50/claims.json:41-42` (text-grep acceptance) |

## 3. Documented invocations (inventory)

| Invocation | Where documented | Needs `c42d675`? |
|---|---|---|
| `python3 -B tools/check-readme-revisions.py` | corpus/README.md:17-21; round-49.md:293 | no |
| `… --readme <path> [--json]` | round-49.md:299; Ca-evidence.md:88-96 | no |
| `… --selftest` | round-49.md:292; SCORECARD.md:970; Ca-evidence.md:101; run-validation.py:152-156 (acceptance) | yes (control 9) |
| `python3 reports/round-49/run-validation.py` in a fresh clone | SCORECARD.md:959-961; run-validation.py:45 | yes (C leg, :125-128) |
| isolated git-archive replay (r48 precedent, pre-dates this tool) | LOG.md:3942-3943 | r48: no; r49 runner: already fails C |
| wave executor clone (`git clone -q <lane>`, non-shallow) | round-50 contract, Ownership and bounds | keeps it (verified) |

## 4. Experiment matrix

Trees (all in `/tmp/r50-revenger`, lane at `4ad2683`):
- `full`: `git clone --no-local` (object reachable)
- `shallow`: `git clone --depth 1 file://…` (`git cat-file -e c42d675^{commit}` rc 128)
- `archive`: `git archive 4ad2683 tools corpus | tar -x` (no `.git`)
- `bogus-full`: copy of `full` with `BASE_COMMIT = 0123456…` (pin absent from a repo with history)
- `mut-*`: copies whose two skip() sites are replaced by `check(name, False, …)` (fail-closed mutant)

`--selftest`:

| Tree | Tool | rc | Output summary |
|---|---|---|---|
| full | base | 0 | 11 PASS; `selftest skips: 0`; `selftest: all checks passed` |
| full | mutant | 0 | 11 PASS |
| shallow | base | 0 | `SKIP control: base c42d675 README flagged (r49 defect) (base object unreachable)`; `skips: 1`; `all checks passed` |
| shallow | mutant | 1 | `FAIL control: base c42d675 …`; `selftest: FAILED` |
| archive (no .git) | base | 0 | same SKIP; `skips: 1`; `all checks passed` |
| archive | mutant | 1 | FAIL; `selftest: FAILED` |
| bogus-full | base | 0 | `SKIP control: base 0123456 …`; `skips: 1`; `all checks passed` |
| bogus-full | mutant (bogus pin) | 1 | `FAIL control: base 0123456 …`; `selftest: FAILED` |

Default mode (`python3 -B tools/check-readme-revisions.py`), every tree: rc 0; findings 0; warnings 1
(REVISION-ORPHAN [90,101]); the mutant in `archive` also rc 0.

Base README: `--readme` on `c42d675:corpus/README.md` gives rc 1, REVISION-DUP [55,57],
REVISION-STUB [55], warning REVISION-ORPHAN [71,82].

Round-49 runner (`reports/round-49/run-validation.py --out /tmp/…`, run in the tree):

| Tree | Tool | Verdict | C | Ca | S |
|---|---|---|---|---|---|
| full | base | `admitted` (acceptance true) | improved | improved | improved |
| archive | base | `rejected-honest-stop` | unchanged-blocked (`no_existing_entry_modified` false; `knowledge_changed_vs_baseline` []) | improved (selftest SKIP) | improved |
| archive | mutant | `rejected-honest-stop` | unchanged-blocked | unprovable | improved |

Tool sha256 (base bytes at `4ad2683`): `d49fdf1c9524c457c2a5fb9c647442e682c6a3de98030d3c778b5f33740cdeb7`,
equal to validation.json:347.

Reproduce (paths in `/tmp/r50-revenger`):
```
git clone -q --no-local <lane> /tmp/r50-revenger/full
git clone -q --depth 1 file://<lane> /tmp/r50-revenger/shallow
git -C /tmp/r50-revenger/full archive --format=tar 4ad2683 tools corpus | tar -x -C /tmp/r50-revenger/archive
python3 -B <tree>/tools/check-readme-revisions.py --selftest      # exit codes as the table
cd <tree> && python3 -B reports/round-49/run-validation.py --out /tmp/r50-revenger/r49-<tree>.json
```

## 5. Divergences

- **D1. The verdict hides skips.** A shallow or archive run prints `selftest: all checks passed` with
  `selftest skips: 1` and exits 0 (tool:344, 357-358). The documented "11/11" (LOG.md:3970;
  SCORECARD.md:970; round-49.md:159; Ca-evidence.md:101) holds only where `c42d675` resolves, and the
  documentation does not say so.
- **D2. The round-49 acceptance accepts a SKIP.** run-validation.py:156 requires only `rc_rs == 0`. In an
  archive the Ca leg reports `improved` without control 9 running (archive base row). That is the R3
  failure inside the receipt, not only inside the selftest.
- **D3. Exit-code convention.** tool:34-36 defines 2 as could-not-evaluate, and SKILL.md:419 requires that
  state to stay distinct from pass. The pin skip returns 0, which is a pass.
- **D4. Fleet R3 durability note is partly off.** JjAuditKotodama.md:131-134 says the pin is durable
  because jj writes `refs/jj/keep/<sha>` for local commits. No keep ref names `c42d675`. Its durability
  is ancestry: `c42d675` is an ancestor of `4ad2683`, which is kept by `refs/jj/keep/4ad2683…` and
  `refs/heads/main`. [INFERENCE] If main's chain were rewritten and those keep refs dropped, the pin would
  vanish silently. Not reproduced.
- **D5. Lane state moved since the audit.** JjAuditKotodama.md:6 says the lane is "not yet colocated
  (`test -d .jj` → absent)". Now `.jj` exists, `git symbolic-ref -q HEAD` gives `refs/heads/main`
  (attached), and 11 `refs/jj/keep/*` refs exist. R1 and R2 premises need re-measurement before reuse.
  No jj command was run.
- **D6. Cited worktree is gone.** round-49.md:119 cites
  `/home/vgpnk/Projects/shokunin/.tower/worktrees/kaika/kotodama-shokunin`; it no longer exists. The
  commit is still in the lane's object store, so the pin still resolves.
- **D7. Filed receipt pins tool bytes.** validation.json:347 pins the current bytes. Any O edit makes that
  pin describe old bytes. The runner writes pins without checking them (run-validation.py:357-366), so
  nothing fails. Leave the r49 receipt untouched (round-50 non-goal); the r50 receipt records the new hash.

## 6. Design constraints for O (for the integrator; not implemented here)

1. Keep `BASE_COMMIT` and control 9's name. The name embeds `BASE_COMMIT[:7]` (tool:303), and the same
   constant is r49's baseline (run-validation.py:46).
2. Split the unresolvable pin into two states:
   - (a) repository present, `git -C LANE cat-file -e <sha>^{commit}` fails (jj or gc rewrite, or a bogus
     pin): FAIL, exit 1, explicit message. This is the R3 case; the bogus-pin mutant reproduces it.
   - (b) no repository (`git rev-parse --git-dir` fails; export): could-not-evaluate, exit 2 with an
     explicit message, per tool:34-36 and SKILL.md:419. Exit 0 with a printed NOT-EVALUATED line keeps the
     silent-pass shape; I do not recommend it.
3. Remove the silent path. `skip()` must not leave the verdict green, and the verdict line must never say
   "all checks passed" while a control was not evaluated.
4. Update the docstring (tool:29-36) to say `--selftest` needs a history-retaining copy (lane or clone).
   Default README mode is unchanged and still works in an export.
5. Make the acceptance behavioural, not textual. claims.json:41-42 greps for the literal
   "base object unreachable"; rewording would satisfy it without changing behaviour. Use instead: a
   shallow-clone `--selftest` must exit non-zero; a full-clone run must print 11 PASS and exit 0; default
   mode unchanged.

## 7. Operability hazards for other round-50 seats

- ExecProbe's `reports/round-50/jj-colocation-probe.py --tools-root <tree>`: a tools tree taken from an
  export (no `c42d675`) makes `--selftest` exit 1 after the fix. The landed-tool case must run in a
  repository that contains `c42d675` (the lane, or a `git clone` of it). The R3 case must use an explicit
  bogus pin in a repo with history. Otherwise the 0/3 count is an artefact of the probe's tree.
- The planned round-50 gate (`build/ScribeLesson.md:97`) must run in the lane or a full clone.
- The executor clone recipe keeps the pin (verified above).

## 8. Ordered control list (11; keep names and order)

1. control: clean revision list passes (tool:242)
2. control: duplicate label flagged at [1, 4] (tool:250)
3. control: truncated stub flagged (tool:259)
4. control: EOF stub flagged (tool:267)
5. control: increasing order flagged (tool:275)
6. control: fenced 'revision:' ignored (tool:283)
7. control: absent revision lines passes (tool:291)
8. control: missing file exits 2 (tool:300)
9. control: base c42d675 README flagged (r49 defect) (tool:303; name uses `BASE_COMMIT[:7]`)
10. control: orphan paragraph warned at [4, 5], verdict clean (tool:331)
11. control: minor gap warned (tool:339)

## 9. Confidence and unrun checks

- Pin provenance and reachability: high (git facts plus experiments).
- Skip intent: high for the recorded wording (Ca-evidence.md:106-108; tool:64-66). The portability motive
  is inferred from that wording and the r48 archive precedent. [INFERENCE]
- Break set: high for every workflow executed. The inventory is grep-based over lane docs and round-49
  artefacts (fleet `.ufo` copies excluded). Medium-high.
- Not run: no in-lane selftest or runner (the runner writes `validation.json` by default, so it was run
  only with `--out` into `/tmp`). No jj command, so jj gc and keep behaviour is inferred from git refs
  only. The receipt_guard half of O was not examined.
- Installs or updates: none. System `git`, `python3` and `tar` only.
