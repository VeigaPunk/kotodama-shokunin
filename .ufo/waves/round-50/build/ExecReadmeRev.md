# ExecReadmeRev: claim O, R3 (pinned readme-revision base fails closed), revision 2

## Assignment
`tools/check-readme-revisions.py`: the pinned `BASE_COMMIT` control must not SKIP when the base
object is unreachable (JjAuditKotodama R3; base `skip()` at `:233`, skip sites `:311` and `:321`,
unguarded `git -C LANE show` at `:306`). Revision 2 (L1 refinement, IRC from ChousaR27R2): scrub
`GIT_*` from the probe environment; an unreachable pin in a repository, or with no repository, is
an ERROR line and exit 2 (could-not-evaluate, the tool's own contract) and never a skip; keep
`BASE_COMMIT` and control 9's name; append controls for unreachable-pin errors and for GIT_DIR
masking; default and `--readme` modes unchanged; regenerate the patch.

## Artifacts
- Patch: `.ufo/waves/round-50/patches/ExecReadmeRev.patch`, sha256 `3ace2b523ddeb976eb1fce1148d9d7ae4d2e7fbb7338de81def0184addd70bf4`, one file, +222 / -40.
- Tool (clone `.ufo/waves/round-50/work/ExecReadmeRev`, base `4ad26836`): sha256 `54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4`.

## What changed in revision 2 (vs revision 1)
- Base-pin outcome is three-way: `PASS` (base README still carries REVISION-DUP and REVISION-STUB), `FAIL` (it no longer does), `ERROR` (the pin cannot be evaluated). The loader returns `(name, status, detail)`.
- `ERROR` prints `ERROR control: ...` and makes the selftest exit 2. `FAIL` exits 1. Any `ERROR` takes precedence (exit 2).
- No SKIP path remains. `grep -n 'SKIP\|skip(\|skips:'` on the tool returns no matches.
- `GIT_*` scrub (`_git_env`, `:236`) applies to every probe. It was already present in revision 1; the base `GIT_DIR=/nonexistent` SKIP is observed on base bytes and is gone.
- Controls 14 (shallow clone, pin beyond depth 1) and 15 (GIT_DIR naming a foreign repo that holds the pin, against a non-repository lane) are appended. Controls 12 and 13 keep their names and now expect `ERROR`.
- `BASE_COMMIT`, control 9's name, and controls 1-8 and 10-11 are byte-identical to revision 1.
- `main()` maps the selftest result to `{0: all checks passed, 1: FAILED, 2: could not evaluate (ERROR)}`. Default and `--readme` paths are unchanged.

## Ordered control list (15)
1. control: clean revision list passes
2. control: duplicate label flagged at [1, 4]
3. control: truncated stub flagged
4. control: EOF stub flagged
5. control: increasing order flagged
6. control: fenced 'revision:' ignored
7. control: absent revision lines passes
8. control: missing file exits 2
9. control: base c42d675 README flagged (r49 defect)
10. control: orphan paragraph warned at [4, 5], verdict clean
11. control: minor gap warned
12. control: unreachable base pin fails closed (never skips)
13. control: git-free tree fails closed (never skips)
14. control: shallow clone with unreachable pin fails closed (never skips) [new]
15. control: GIT_DIR override cannot mask an unreachable pin [new]

## Verification (exercised; final landed bytes)

| run | rc | observed |
|---|---|---|
| full clone `--selftest` | 0 | 15 PASS, `selftest: all checks passed` |
| full clone `GIT_DIR=/nonexistent --selftest` | 0 | 15 PASS (GIT_* scrubbed; the pin resolves in the lane's store) |
| shallow copy (`git clone --depth 1 file://`) carrying the landed tool | 2 | 14 PASS; `ERROR control: base c42d675 ... unreachable in /tmp/r50-shallow/lane: fatal: Not a valid object name c42d675...^{commit}`; `selftest: could not evaluate (ERROR)` |
| no-repository copy (tool alone under `/tmp`) | 2 | 14 PASS; `ERROR control: base c42d675 ... unreachable in /tmp/r50-norepo: fatal: not a git repository`; `selftest: could not evaluate (ERROR)` |
| full clone `--selftest --base-commit 000...0` | 2 | ERROR control 9; controls 12-15 PASS |
| mutant: scrub removed (`if key}`), scratch copy only | 2 | `FAIL control: GIT_DIR override cannot mask an unreachable pin []`. Control 15 detects the masking when the scrub is absent. |
| full clone normal mode | 0 | `findings 0`, `warnings 1` (REVISION-ORPHAN [90,101]), identical to revision 1 |
| `--readme` on pre-fix `c42d675:corpus/README.md` | 1 | `REVISION-DUP lines=[55, 57]`, `REVISION-STUB lines=[55]` (defect path unchanged) |
| base bytes (`4ad2683`) under `GIT_DIR=/nonexistent`, git-free tree | 0 | `SKIP control: base c42d675 ... (base object unreachable)`, `selftest skips: 1` (base behaviour, for comparison) |

Scratch trees under `/tmp/r50-*` were removed after the runs.

## Behavior change to review (deliberate)
- A poisoned inherited `GIT_DIR` no longer changes the outcome. In a healthy lane control 9 PASSes. Where the pin really is missing, the result is ERROR.
- The unreachable cases are proven by controls 12-15 and the shallow and no-repository runs. They do not depend on the environment.
- The selftest exit code is now 2 for "could not evaluate". The round-49 runner (`reports/round-49/run-validation.py`) requires `rc_rs == 0`, so 2 still counts as failure there.

## Risks and cross-seat advice
1. **Ca acceptance.** A counterfactual leg that runs `check-readme-revisions.py --selftest` in a git-free temp tree exits 2 by design (ERROR, control 9). Do not weaken the control. Either pass `--lane <absolute path to a git repo holding c42d675>` or drop the selftest from the acceptance.
2. **TMPDIR precondition.** Controls 13-15 build temp directories or repositories. A TMPDIR nested inside a git work tree that holds the pin would break control 13 (the pin would resolve). This holds here (`/tmp`, "not a git repository ... mount point /").
3. **Reviewed, not run.** A pin that resolves while `corpus/README.md` is absent at that commit (returns ERROR), and the `OSError`/`ValueError` path when the git binary is missing (returns ERROR).
4. **R3 is not jj-caused** (CriticOperability E4). The change is git-only. The jj counting probe belongs to another seat; it should measure R3 as base bytes exit 0 with SKIP, landed bytes exit 2 with ERROR, both in a git-free tree.

## Unrun checks (main agent to run after integration)
- In the landed tree: `python3 -B tools/check-readme-revisions.py --selftest`, expect rc 0 and 15 PASS.
- Same with `--lane <non-repository dir>`, expect rc 2 with control 9 ERROR.
- Not run by me: anything in the lane itself (lane bounds), `receipt_guard`, the jj probe, lint or formatters.

## Installs
None. Only the system `git` and `python3` were used. Nothing was installed or upgraded.

## Hygiene
- Lane production files untouched. No git or jj mutation in the lane.
- Written under `.ufo/waves/round-50/`: the clone, the patch, and this report in `build/`.
