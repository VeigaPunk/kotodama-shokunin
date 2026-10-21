# CriticMeasurementAll — round 50 falsify: the three before→after numbers in `reports/round-50/validation.json`

Seat: `KotodamaR50-2.CriticMeasurementAll-21` (critic, leaf). Item attacked: the before→after numbers for C (knowledge 225→226, culture-material 27→28), O (jj-colocation false negatives 3→0) and Ca (r49 fixture exit 1 naming C→S, matching the independent prediction; r50 manifest exit 0). I attacked each for circularity, base-run safety and four post-hoc changes: probe v2, the runner regex fix, the checker literal rename, and the entry wording change. This is author-lane advice, not admission.

Landed bytes were read with `git show 1c779e4:<path>`. Reproductions ran in a private shared clone, `/tmp/cma21-cu0R/{landed@1c779e4,base@4ad2683}`, with `GIT_CEILING_DIRECTORIES=/tmp`.

Axes: coverage (C), operability (O), calibration (Ca, and every number).

## Verdict summary

| number | verdict | one line |
|---|---|---|
| Receipt as a whole | **BROKEN (provenance)** | The landed runner exits **1** on the landed tree. The filed receipt (exit 0) came from an **uncommitted** runner edit made after landing. |
| C 225→226 / 27→28 | **HOLDS** (once the runner fix is committed) | git-object counts agree. The regex fix moves the runner onto the declared word mode, not onto the answer. |
| O false negatives 3→0 | **PARTIAL** | Reproduces 3/3→0/3. R1 was loosened after the v1 run scored landed 1/3, and v2's R1 is passed by a cosmetic base-guard mutant that never reads a remote ref. |
| Ca r49 rc=1 + prediction | **HOLDS** | The prediction is byte-identical to the expectation that existed before the checker ran. |
| Ca r50 manifest rc=0 | **PARTIAL** | rc=0 depends on wording. The same reference written as a full path gives rc=1 `C->REC`. |
| Checker literal rename S048→S998 | **HOLDS** | Semantics-preserving: both tokens are outside the selftest `s_range`. |
| Base-run safety | **HOLDS** | No tree writes. A hostile `GIT_DIR` and no ceiling change no judged value. |

## F1 (blocker, all axes): the receipt is not reproducible from landed bytes

- `reports/round-50/validation.json` is **untracked**, mtime 13:32:51 -03. The landing commit 1c779e4 is 13:03:10 -03.
- `reports/round-50/run-validation.py` is **modified** in the working tree (mtime 13:04:02, after landing). The working-tree sha256 is `de5b9c16…` and the landed sha256 is `2b7d4cd7…`.
- The diff is the R50-M2 fix: `TOPIC_OWNER_RE` gains `\b`, at landed `run-validation.py:69`.
- Reproduction on identical trees:
  - `python3 -B runner-landed.py --tree landed --base-tree base` → **rc=1**, `acceptance_passed: false`. It fails on `C.before.pastoral_topic_owner_lines` with actual 1, expected 0. The hit is "sherd" at `culture-material/writing-media-surface-economy.md:3`.
  - `python3 -B runner-wt.py --tree landed --base-tree base` → **rc=0**, `acceptance_passed: true`. Every other judged value is identical.
- The receipt records no tree sha, runner sha or probe sha. `"tree": "/tmp/kr50-landed"` and `"base_tree": "/tmp/kr50-base"` are bare paths at `validation.json:578,9`. `"probe"` points at the lane **working-tree** file (`validation.json:575`). That file currently hashes equal to landed (`d3fff001…`), but the receipt cannot prove it. `/tmp/kr50-landed` HEAD is 1c779e4 and `/tmp/kr50-base` is 4ad2683 (observed), so the trees were right. Only the instrument was off-commit.
- **Smallest fix:** commit the runner `\b` edit together with the receipt. Add `tree_sha`, `base_sha`, and sha256 values for `runner` and `probe` to the receipt, and re-run. Until then, the filed "acceptance_passed: true" is produced by bytes that no commit holds.

## C: 225→226, culture-material 27→28 — HOLDS (conditional on F1)

- Circularity: none found. `git ls-tree -r` gives `4ad2683 knowledge=225 culture=27` and `1c779e4 knowledge=226 culture=28`, matching the runner's working-tree `find` counts. That rules out the jj-untracked-file hazard for these trees.
- Runner regex fix: it is a correction toward the declared semantics, not toward the result. `claims.json:20` declares `"mode": "word"` for `pastoral-unowned`; only its `evidence_command` was a substring match. The left-only `\b(…|herd|…)` matches herd, herds and herder, which is broader than the declared target list, so the "absent at base" check is conservative.
  - At base: 0 lines.
  - After: exactly 1 line, the new entry at `pastoralism-animal-husbandry.md:3` (grep verified).
- The filed `claims.json` evidence command still returns 1 at base, as disclosed in R50-M2. A judge who runs it literally still sees a non-empty result.
- Base-run safety: holds (see the final section).

## O: probe false negatives 3→0 — PARTIAL

- Reproduced with the landed probe v2 (`d3fff001…`):
  - base tools: `JJ_COLOCATION_FALSE_NEGATIVES=3/3`, `FALSE_POSITIVES=0/4`
  - landed tools: `0/3`, `0/4`
- Post-hoc predicate change, reproduced with the v1 bytes (`work/ExecProbe-4`, `276eff71…`):
  - v1 on landed: `1/3`
  - v1 on base: `3/3`
  - v2 on landed: `0/3`
- So the after-number 0 exists only under v2. v2 was written after v1 had scored the landed tools 1/3 (`telemetry/jj-probe-v1.txt`; code comment at `jj-colocation-probe.py:241-246`).
- The amendment is disclosed, and it is defensible on intent. The claim text asks for "a landed (branch/remote) sha distinct from the local HEAD". 17 of the 45 retained controls and `design.md:128` require `committed_sha=<HEAD>`, so v1 asked for more than the claim.
- **Counterexample (R1 has no discriminating power).** I made a one-line mutant of the **base** guard. It prints `landed_sha=$(git rev-list --max-parents=0 HEAD)` beside `committed_sha` and never reads `refs/heads/*` or `refs/remotes/*`. It contains no detection logic at all.
  - Under v2, R1 is **not flagged** ("every landed-labelled sha is an ancestor of refs/remotes/origin/main"), and the total is `2/3`.
  - v1 flags the same mutant (`3/3`).
  - The cause: v2's predicate at `:247-252` is only "some `landed`-labelled sha exists and is an ancestor of origin/main". The R1 fixture at `:228-232` has a one-commit history, so every ancestor of origin/main is the tip and holds the receipt.
  - R2 still catches this mutant, and the landed guard does real ref work (`guard_remote_ref_lines` 0→24, R2 refuses with `landed_ref=refs/remotes/origin/main`). So the landed 0/3 is not fake, but R1 itself proves nothing beyond label presence.
- **Smallest fix:** put a receipt-less commit below C0 in the R1 fixture. Require `landed_sha == rev(landed_ref)`, with `landed_ref` in `refs/remotes/*`. Also require `landed_sha:<receipt>` to exist. Re-run v2 on base, landed and the root-commit mutant (expected: 3/3, 0/3, 3/3).

## Ca: r49 fixture rc=1 naming C→S, matching the independent prediction — HOLDS

- Reproduced: rc=1 with 6 findings (C→Ca, C→S ×2 vias, S→C, S→Ca, overlap C/Ca). `r49_matches_independent_prediction: true`.
- Not tuned on checker output. `r49-expected-independent.txt` is **byte-identical** to the `expected_findings` array in `work/ExecSepFixture-4/.../r49-fixture.json` (mtime 12:51). That seat reports it did not run ExecSepTool's checker ("in flight"; `ExecSepFixture.md:89-91`). The array was moved out of the fixture at integration without changing content (diff observed).
- The build-wave M2 concern ("exactly 1/1 means tuned") no longer applies: the expectation is an exact 6-finding set, not one pair.
- Residual weakness: the runner's `_norm_finding` drops multiplicity and location (`x12`, `matched S031,…,S042`, `named at …:18`). Equality is over (pair, via, target) only.
- The "before" side is not measured in this receipt. Ca.before is all-null because the checker is absent at base, and the declared "0/1 detected" lives in `4ad2683:reports/round-49/validation.json` (`separability.c_without_s.passed: true`, observed). Report it as the r49 receipt value, not as a receipt delta. The receipt's own Ca deltas (files 0→1, QUALITY lines 0→1) are text-presence counts.
- Checker literal rename (S048→S998 at `check-claim-separability.py:838,865,874,936,953,1006,1056`; ExecSepTool→landed diff): this **holds**.
  - The selftest's `s_range` is `\bS0(3[1-9]|4[0-3])\b` (`:778`), and both S048 and S998 fall outside it, so every scenario keeps its meaning.
  - The rename only stops the checker's own bytes, a Ca land, from matching C's export `\bS0(4[89]|[5-9]\d)\b`. That was a true false positive.
  - No residual S048+ token remains in any O or Ca land (grep: 0).

## Ca: r50 manifest rc=0 — PARTIAL (wording-contingent)

- Reproduced on the clean landed tree: `SEPARABILITY: 0 findings`, rc=0.
- Entry wording change: `ExecSepFixture.md:79-81` records that the WIP entry named `corpus/lessons/round-50.md`, which "would fire `C->REC` at landing. Bare form, or accept the finding". The landed bytes avoid the finding through wording:
  - The entry's `- source:` line (`pastoralism-animal-husbandry.md:9`) says "the round lesson's located quote".
  - C's **added** line at `corpus/SOURCES.md:8` (diff +10) names the new REC file in bare relative form, `` `lessons/round-50.md` for S048–S069 ``.
- Counterexample (private clone, working-tree edit, reverted):
  - Changing `SOURCES.md:8` to `corpus/lessons/round-50.md` gives rc=1 with `SEPARABILITY_DEPENDENCY C->REC via land path 'corpus/lessons/round-50.md' named at corpus/SOURCES.md:8`.
  - Putting the same path into the entry's `- source:` line gives rc=1 `C->REC … pastoralism-animal-husbandry.md:9`.
- The dependency is real either way. By the registry's own contract (`SOURCES.md:7-9`), the URL, access date and verbatim quote for S048–S069 live only in REC's new lesson. On base plus C's lands, the pointer dangles.
- The checker's own selftest calls this a finding ("negative: a claim naming a record's new path is a finding", `:1020-1027`). QUALITY criterion 7 says "a counterfactual leg that quietly keeps the dependency … does not count". The miss is the full-path-substring matcher (CriticCalibration F3, predicted in the build wave).
- **Smallest fix:** either declare `corpus/lessons/round-50.md` among C's lands, or accept and disclose `C->REC` (expected rc=1). Also teach the path leg to resolve relative mentions against the naming file's directory (`corpus/` + `lessons/round-50.md`). Do not report rc=0 as separability.

## Base-run safety — HOLDS

- After full runs of both runners, `git status --short` on both clones was empty.
- The probe uses `mkdtemp` under `/tmp`, drops `GIT_*`, and sets `GIT_CEILING_DIRECTORIES=/tmp` (`jj-colocation-probe.py:72-90`). No `/tmp/jj-colocation-probe.*` leftovers remained.
- Hostile environment: `GIT_DIR`/`GIT_WORK_TREE` pointed at an empty decoy repo, with `GIT_CEILING_DIRECTORIES` unset. The runner still gave rc=0, every before and after value was identical to the clean run, and the decoy stayed commit-less.

## Session record

- Commands: `git show`, `git ls-tree`, `git diff` (read-only on the lane), plus `git clone --shared` into `/tmp/cma21-cu0R`. The runners, probe v1 and v2, and the checker ran in the clone only. The base-guard mutant lived in `/tmp/cma21-cu0R/mut`. The clone working-tree edits were reverted (`git checkout -- .`).
- Lane: no edits, no git or jj mutation; the only write is this report. `/tmp/cma21-cu0R` was deleted after writing.
- Tool installs: none.
