- Seat: A03 | executor | claim A | date 2026-10-19 | baseline 57c8409

# Scope watch — rounds 33–37 Git census

## Verdict

**PASS for the Git-visible scope census.** The inspected HEAD is the declared baseline (`57c8409ba16d9f9e692297198d95e8f2ce5a1937`); `git diff --name-status 57c8409` and `git diff --stat 57c8409` were empty. At the pre-output working-tree sample, every untracked path was under `reports/round-37/` (20 paths); no tracked change was present. This seat writes only the assigned `reports/round-37/adj/A03-scope.md` path.

The round-33 through round-36 commit path census found no `.ufo/`, earlier-round report, or `tools/gates/frozen/` path. All round report paths were under the respective round's own `reports/round-N/` tree; the remaining paths are listed below. Thus no out-of-lane path is evidenced by this Git census. Git does not observe arbitrary filesystem writes outside the repository, so this is not a claim about untracked external side effects.

## Commit census

Read-only census of the four round commits between the round-32 close and the declared round-37 baseline (counts from `git diff-tree --no-commit-id --name-status -r --no-renames`):

- **Round 33 — `da68a6d`:** 90 paths (80 added, 10 modified); 79 under `reports/round-33/`. The 11 other paths: `AGENTS.md`, `LOG.md`, `REGIMEN.md`, `SCORECARD.md`, `SKILL.md`, `corpus/knowledge/linguistics/register-lexicon-ceilings.md`, `corpus/lessons/README.md`, `examples/culture-d3/README.md`, `examples/culture-d3/handoff.md`, `examples/handoff-packet.sample.md`, `examples/handoff-packet.sample.yml`.
- **Round 34 — `4a7aede`:** 83 paths (80 added, 3 modified); 79 under `reports/round-34/`. Other paths: `LOG.md`, `SCORECARD.md`, `tools/exercise-handoff-e2e.py`, `tools/harness/receipt_guard_adoption.py`.
- **Round 35 — `ce103bf`:** 92 paths (88 added, 4 modified); 78 under `reports/round-35/`. Other paths: `LOG.md`, `SCORECARD.md`, `corpus/README.md`, six `corpus/knowledge/culture-material/` additions (`agrarian-field-system-lexicon.md`, `bathing-and-body-hygiene.md`, `fire-fuel-light.md`, `funerary-material-culture.md`, `furniture-interior-lexicon.md`, `writing-media-surface-economy.md`), four `corpus/knowledge/myth-symbol/` additions (`binding-speech-complex.md`, `death-afterlife-eschatology.md`, `eschatology-world-end-systems.md`, `sacred-kingship-mythic-charter.md`), and `tools/exercise-handoff-e2e.py`.
- **Round 36 — `57c8409`:** 47 paths (44 added, 3 modified); 43 under `reports/round-36/`. Other paths: `LOG.md`, `SCORECARD.md`, `corpus/README.md`, `corpus/knowledge/culture-material/timekeeping-instruments.md`.

The non-report paths above remain within the lane repository. Corpus knowledge additions are in PROVINCE-owned partitions; examples and the lane's records/tools are also within the lane's stated ownership. One path merits explicit context: round 33 modified `corpus/lessons/README.md`; its own `targets.json` expressly allowed the lessons README and SKILL changes to be drafted by seats and applied by the integrator. This historical exception does not authorize this seat to edit any protected lessons file.

## Round-37 worktree sample

`git status --short --untracked-files=all` before this fragment listed 20 untracked paths, all rooted at `reports/round-37/`, and no modified tracked path. After writing this fragment, the same status command listed 40 untracked paths, all under `reports/round-37/`; the accompanying `PATH-ROOTS` check emitted no `OUTSIDE` row, `git diff --name-status 57c8409` remained empty, and the assigned path appeared as `?? reports/round-37/adj/A03-scope.md`. The assigned path is the declared output (`reports/round-37/targets.json:51`); the round-37 shared rule limits this seat to its assigned output under that directory (`reports/round-37/targets.json:3-8`).

## Owed

None for the Git-path census. External filesystem side effects are not observable by the Git-only method and are not asserted absent.

## Citations

- Scope and hard boundaries: `reports/round-37/claims.json:7-8,25-30`; `reports/round-37/targets.json:3-8,51`; `REGIMEN.md:60-69`; `PROVINCE.md:9-14,27-31`.
- Round-33 exception for integrator-applied README/SKILL changes: `reports/round-33/targets.json:7`; commit path evidence: `git show --format='COMMIT %h %s' --name-status --no-renames da68a6d`.
- Baseline and clean tracked tree: command output from `git rev-parse HEAD` (57c8409ba16d9f9e692297198d95e8f2ce5a1937), `git diff --name-status 57c8409` (empty), and `git diff --stat 57c8409` (empty).
- Round commit counts and non-report paths: read-only output from `python3` aggregation of `git log --format=%H%x09%s cdd66d7..HEAD` and each selected r33-r36 commit's `git diff-tree --no-commit-id --name-status -r --no-renames`; per-commit path lists independently visible via `git show --format='COMMIT %h %s' --name-status --no-renames <commit>`.
- Round-37 worktree samples: pre-output `git status --short --untracked-files=all` (20 rows; all under `reports/round-37/`); post-output status (40 rows; all under `reports/round-37/`), `PATH-ROOTS` emitted no outside row, tracked diff empty, and assigned path present. No `reports/round-*/run-validation.py` was executed by this seat.
