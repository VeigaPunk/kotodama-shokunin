# CriticMistakes — round 50 falsify: `corpus/lessons/round-50.md` `## Mistakes`

Seat: KotodamaR50-2.CriticMistakes-21 (critic, leaf). Landed commit `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`, base `4ad2683`.
Method: read landed bytes with `git show 1c779e4:<path>`. I reproduced in a private clone `/tmp/cm-lzL5` (`clone --shared`, checkout `1c779e4`, `GIT_CEILING_DIRECTORIES=/tmp`), plus a second clone at `4ad2683` for `--base-tree`. Both were deleted afterwards. I made no lane writes except this report and no installs. This is author-lane advice, not admission.

Axes: coverage, operability, calibration.

## Verdict summary

| item | verdict | one line |
|---|---|---|
| R50-M1 (`round-50.md:68`) | **PARTIAL** | The checker does fail on the r49 bytes (reproduced). But the cited run, `reports/round-50/validation.json`, is not in the landed commit, and the row reports only 2 of the 6 findings. |
| R50-M2 (`round-50.md:69`) | **PARTIAL (not honest in scope)** | The class is mislabelled. The seat count is low (11 build reports name the hit, not six). "Not executed by the gate" hides that the round's own acceptance runner does execute the substring regex: the landed runner exits 1. |
| R50-M3 (`round-50.md:70`) | **PARTIAL** | The facts and captured-by hold. The fix is a second authority that disagrees with the filed `claims.json:18`. Its 0-findings verdict depends on how a path is spelled and on which role the manifest is filed under. |
| Missing mistakes | **BROKEN (omissions)** | (a) The probe's R1 predicate was changed after measurement, and the docstring is stale. (b) The runner regex was fixed only after landing, and the receipt was produced by uncommitted bytes. (c) Path-literal collisions are masked by spelling and role. The lesson also points verdicts at files with no round-50 content. |

## R50-M1 — is the fix "shown able to fail"? Cite the run.

**What holds (reproduced at `1c779e4`):**
- `python3 -B tools/check-claim-separability.py reports/round-50/separability/r49-fixture.json` exits **1** with `SEPARABILITY: 6 findings`, including `C->S via export '\bS0(3[1-9]|4[0-7])\b' matched …hunting-foraging-subsistence.md:18` and `S->C via land path '…hunting-foraging-subsistence.md' named at corpus/SOURCES.md:60`.
- `--selftest` exits **0** with `56/56 checks passed`. Line 13 of its output is `PASS negative: an inline-URL-only citation of another unit's export is a dependency`. The scenario (`tools/check-claim-separability.py:935-941`) asserts `EXIT_DEPENDENT` and `out_must=["SEPARABILITY_DEPENDENCY C->S via export"]`, so "the inline-URL control exits 1" is accurate.

**Counterexample 1: the cited run is not in the landed bytes.** The row says "(receipt in `reports/round-50/validation.json`)". `git ls-tree -r --name-only 1c779e4 reports/round-50/` lists claims.json, the probe, run-validation.py, the separability files and telemetry. It does **not** list validation.json. In the lane, `git status` shows `?? reports/round-50/validation.json`, mtime `13:32:51`, while commit `1c779e4` has committer date `13:03:10`. At the landed commit the evidence pointer is dangling. It points at an untracked file written 30 minutes after landing.

**Counterexample 2: the row misreports the output.** The row says the checker "exits 1 with the C→S and S→C findings". It actually emits 6 lines:
- `C->Ca via land path 'tools/check-readme-revisions.py' named at corpus/README.md:18`
- `S->Ca via land path 'tools/check-readme-revisions.py' named at corpus/lessons/round-49.md:12`
- `SEPARABILITY_OVERLAP C/Ca corpus/README.md`
- plus the three C/S lines.

The C→Ca line is drawn from `corpus/README.md`, which is in **both** C's and Ca's lands in the fixture. README:18 (at `8c78e6b`) is Ca's revision-2.6 note naming Ca's own tool, yet the checker credits it to C. `ConnectSiblingSeparability.md` "Shared-land exclusion" says such bytes "are not used for directed dependency". The "independent" prediction (`r49-expected-independent.txt:1`) encodes the same line, so it ratifies the semantics rather than testing them.

Axes: calibration.

Smallest fix:
- Land the receipt, or cite the committed telemetry plus the exact command and its output.
- Restate the row as "exits 1 with 6 findings, of which C→S and S→C are the adjudicated pair".
- Either exclude overlapped-path bytes from directed findings or disclose C→Ca as an overlap artifact.

## R50-M2 — honest?

- **Mislabelled class.** "Not reproducible" is false. The command reproduces deterministically, returning 1 line (`writing-media-surface-economy.md:3`, "sherd"). The defect is that it misfires and contradicts the declared `mode: "word"` / `expect: true` (`claims.json:20-22`).
- **Seat count is low.** `git grep -l -i sherd 1c779e4 -- .ufo/waves/round-50/build/*.md` returns **11** reports:
  - ConnectSiblingPastoral (cites CriticGapPremise rather than finding it itself)
  - CriticGapPremise, ReviewEntryContract, ReviewR50Separability, ReviewSourcesContract
  - ScoutCouplings, ScoutMistakeSweep
  - SrcAndeanCamelids, SrcBarfield, SrcFaoPastoralism, SrcPeku

  That is 10 independent finds, not "six".
- **Captured-by holds as far as it goes.** In `telemetry/declaration-freshness.json`, `pastoral-unowned` is `status: HOLDS`, `reason: "0 owner(s): none"`, so the word-mode freshness gate is correct.
- **Counterexample: the scope is not honest.** "The printed command is not executed by the gate" is true only of the freshness gate. The round's **acceptance runner** executes the same substring regex at `reports/round-50/run-validation.py:69` (landed: `^- topic:.*(pastoral|herd|…)`, no `\b`). Reproduced:
  - Landed runner, `--tree <1c779e4 clone> --base-tree <4ad2683 clone>`: **rc=1, `acceptance_passed: false`**. Claim C fails `before.pastoral_topic_owner_lines` with actual **1**, expected 0. Ca and O pass.
  - The lane's uncommitted runner (`git diff` adds `\b` and an "R50-M2" comment; mtime `13:04:02`, one minute after the commit), with `--probe`/`--manifest` pointed at the clone: **rc=0, `acceptance_passed: true`**, all three claims passing.

  The two runners differ only in that regex. M2's fix (the entry's `gap filled` line, `pastoralism-animal-husbandry.md:4`) does not touch the runner, so the landed bytes cannot reproduce the round's pass.

Axes: calibration, operability.

Smallest fix:
- Commit the runner's `\b` edit, or restore the landed runner and record the failure.
- Retitle the class "declaration evidence command misfires (substring)".
- Add `run-validation.py:69` to the evidence pointer, and correct "six".

## R50-M3 — honest?

- **The facts hold.** `claims.json:10` reads "C's entry cites SOURCES rows opened by the frontier step (not a claim)". CriticFrontier.md, ReviewR50Separability.md (H1) and ReviewSourcesContract.md (F1) capture it.
- **Counterexample 1: two authorities.** The filed declaration `claims.json:18` still gives C lands = [entry, `corpus/README.md`], with no `corpus/SOURCES.md`, and `:10` still says "not a claim". Only `r50-manifest.json` lists SOURCES among C's lands. M2 discloses that "the filed declaration is not rewritten". M3 does not, even though its fix contradicts the declaration.
- **Counterexample 2: the 0-findings verdict depends on spelling.** C's landed `corpus/SOURCES.md:8` says the round lesson's `## Gate` (`lessons/round-50.md` for S048–S069) holds each row's verbatim quote. That is a real C→REC dependency: C's rows are grounded only by REC's Gate. In the private clone I changed that one token to the full path `corpus/lessons/round-50.md`. The checker on `r50-manifest.json --root <clone>` then gave `SEPARABILITY_DEPENDENCY C->REC via land path 'corpus/lessons/round-50.md' named at corpus/SOURCES.md:8`, **rc=1**. As landed it gives `0 findings`, rc=0. Whether the edge is detected depends only on spelling. This is the "third undeclared path" that ReviewR50Separability H1 asked to be moved into C.lands.
- **Counterexample 3: the verdict depends on role filing.** `r50-manifest.json` sits in the REC unit (role `record`, never scanned). With the manifest moved into Ca's lands, the checker gives **rc=1, 5 findings**:
  - `Ca->C via land path '…pastoralism-animal-husbandry.md' named at r50-manifest.json:9`
  - `Ca->O via land path 'reports/round-50/jj-colocation-probe.py' named at r50-manifest.json:29`
  - `Ca->REC` ×3 (`round-50.md`, `claims.json`, `run-validation.py`)

  ExecSepFixture.md "Conditions" item 1 predicted this and asked for an instrument exemption in the checker. Instead the exemption is achieved by role assignment and is undisclosed.

Axes: calibration, coverage.

Smallest fix:
- Note in M3 that `claims.json` lands and the contract text are stale.
- Add the Gate lines, or `corpus/lessons/round-50.md`, to C's lands, or declare the C→REC edge.
- Record that the manifest is exempt only through role `record`.

## Missing mistakes

1. **The probe predicate was changed after measurement (operability, calibration).**
   - `telemetry/jj-probe-v1.txt`: probe v1 (sha `276eff71…`, which matches the `ExecProbe-4.patch` bytes; I recomputed it) on the **landed tools** gave `JJ_COLOCATION_FALSE_NEGATIVES=1/3`. R1 was still flagged: "guard presents committed_sha=5fb8… as landed, but it is not an ancestor of refs/remotes/origin/main".
   - v2 (`d3fff001…`, equal to the landed `jj-colocation-probe.py`) counts only `landed`-labelled shas and moves `committed_sha` to the informational `committed_local_only` field. The result became **0/3**, the declared `after_required`.
   - The amendment is defensible on substance. `reports/round-14/guard/design.md:131` requires `committed_sha` to be the HEAD snapshot, and claim O asks for a landed sha distinct from HEAD.
   - It is still a post-hoc predicate change that moved a gating count from 1 to 0.
   - The landed probe's own docstring (`reports/round-50/jj-colocation-probe.py:10-12`) still states the v1 rule: "Flagged when receipt_guard presents a sha as committed or landed that is not an ancestor". Under the documented rule, the landed result is 1/3.
   - `round-50.md` never mentions v1 or v2. Only the telemetry files and a code comment do.

   Fix: add a Mistakes row covering the v1 1/3 result, the reason for v2, and the probe sha pair. Update the docstring at :10-12 to the v2 rule.

2. **Runner regex / unlanded receipt (operability, calibration).** See R50-M2. The landed `run-validation.py:69` fails claim C (rc=1). The passing receipt comes from an uncommitted edit plus an untracked file written after the commit.

   Fix: a Mistakes row, then land the runner fix and the receipt in the same record commit.

3. **Tool/path literal collision (calibration).**
   - The r49 run's C→Ca line comes from a shared-land file (README:18 names Ca's tool).
   - The r50 0-findings verdict holds only because `SOURCES.md:8` spells the lesson path in its bare form and the manifest is filed as a record (both reproduced above).
   - In the checker itself, `tools/check-claim-separability.py:866` contains the C land literal `corpus/SOURCES.md`. It is muted only because that path exists at base, which is correct under the base-absence rule but is worth one sentence.

   Fix: a Mistakes row naming these masks, or checker changes (match by referent: path components or `lessons/…` suffixes; overlap-excluded attribution).

4. **Verdict pointer (calibration, lower severity).** `round-50.md:14-15` says "Verdicts live in `reports/round-50/validation.json`, `SCORECARD.md` and `LOG.md`". At `1c779e4`:
   - validation.json is absent.
   - `git diff --name-only 4ad2683 1c779e4 -- LOG.md SCORECARD.md` is empty.
   - `rg -c 'round 50|Round 50|round-50'` finds 0 matches in both files.

   [INFERENCE] These may be intended for a later close commit. If so, the lesson should say "will live".

## Commands run (all read-only on the lane; reproductions in /tmp)

- `git show 1c779e4:{corpus/lessons/round-50.md, reports/round-50/claims.json, telemetry/jj-probe-v1.txt, -v2.txt, separability/*, build/*.md}`; `git ls-tree`; `git diff --stat`; `git log -1 --format=%cd`; `git grep -l -i sherd`
- Lane: `git diff -- reports/round-50/run-validation.py`; `git status --short`; `stat` on validation.json and run-validation.py; JSON read of validation.json
- Clone: checker on r49-fixture (rc 1, 6 findings); `--selftest` (rc 0, 56/56); checker on r50-manifest as landed (rc 0); manifest moved into Ca (rc 1, 5 findings); SOURCES.md:8 full-path variant (rc 1, C->REC), then restored
- Clone: landed runner (rc 1, C before-check fails); uncommitted runner with explicit `--probe`/`--manifest` (rc 0). My first uncommitted-runner run gave O=None because a copied runner resolves `PROBE` relative to its own location. That was a harness artifact, rerun with `--probe`, and is not a finding.
- Probe v1 sha recomputed from `.ufo/waves/round-50/patches/ExecProbe-4.patch` and matched; v1/v2 diff read

## Installs

None.
