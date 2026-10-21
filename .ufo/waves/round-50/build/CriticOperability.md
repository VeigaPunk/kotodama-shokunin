# CriticOperability — round 50, claim O (jj-safe gates)

Seat: `ChousaR27R2.CriticOperability-4` (critic, leaf). The review covers the proposed O approach
(`reports/round-50/claims.json:31-44`) against base `4ad26836552462d28a946ca3b067cab0b5ce3532`.
When this review ran, no O patch, clone or probe existed (`.ufo/waves/round-50/patches` and `work/`
were absent, and `reports/round-50/` held only `claims.json` and `telemetry/`). Every finding below
targets the claim text and base tool bytes. This is author-lane advice, not admission.

## Verdict

- **Not bookkeeping for R2.** The false negative is reachable through a command the lane permits
  (the helper's own `jj git fetch`), not only through a forbidden `jj new`. This is a real
  operability move (E2).
- **R1 is real, but the claim states the wrong invariant.** The phrase "landed (branch/remote) sha
  distinct from the local HEAD" would certify false provenance in the push-failed state, and it is
  false in the steady state (E3).
- **R3 is a real fail-open defect, but jj did not cause it.** Labelling it a "jj-colocation false
  negative" inflates the jj count. The base fail-open has two triggers that do not involve jj at
  all (E4, E5).
- **The probe is circular as declared.** The before and after numbers (3/3 and 0/3) were fixed in
  `claims.json` before the probe existed. Without positive controls and mutants, a tool that always
  refuses and a selftest that always fails would both reach 0/3. R1 is also not a false negative
  (the guard does refuse); it is a provenance defect. Counting it as one of "3 false negatives"
  miscalibrates the metric.

## Counterexamples and evidence

| id | counterexample | evidence (observed this session) |
|---|---|---|
| E1 | R2 still reproduces on the base guard in the preserved real-jj sandbox | `/fast/scratch/jj-wave/JjAuditKotodama-2/case6/lane`: HEAD `20c3eec0…` is detached (`symbolic-ref` rc 1), while `refs/heads/main` and `origin/main` are both `8020198f…`. `cat-file -e origin/main:reports/validation.json` returns rc 0, but the HEAD lookup fails with rc 128. The case6 guard is byte-identical to the lane guard (`cmp`). Running `receipt_guard.py reports/validation.json --repo-root case6/lane` exits **0**. |
| E2 | **R2 needs no forbidden command.** `lane-addendum.md:215-218` forbids seats from running `jj new`/`edit`, which is the audit's trigger. However, the same file allows `jj git fetch` through the helper (`jj-lane.sh:285-288`, the push-recovery fetch). A fetch after another writer pushes leaves HEAD below the tip. | In a temp sandbox (jj 0.45.1, git, bare origin, a second clone pushes a receipt commit, then `jj git fetch` in the colocated lane): HEAD stays at `a9779314…`, while `refs/heads/main` and `origin/main` move to `60fdfe03…`. `origin/main` holds the receipt, the working copy lacks the file, and the base guard exits **0**. The base commit itself was written by an outside writer ("round-49 verifier spot-check (integrator, kaika)"), so other writers do push to this lane. |
| E3 | **"Branch/remote sha distinct from HEAD" is the wrong invariant.** After helper exit 3 ("committed but push failed (commit kept)", `jj-lane.sh:9,60`), `refs/heads/main` equals HEAD and both point at an unpushed commit. | Same sandbox, using a local `jj commit` and `bookmark set main`: HEAD = `refs/heads/main` = `af9ecd1a…`, while `origin/main` = `60fdfe03…`. `merge-base --is-ancestor HEAD origin/main` returns rc 1 and `origin/main` lacks the receipt (rc 128). The base guard refuses with `committed_sha=af9ecd1a…`, which is unlanded. A fix that cites `refs/heads/main` as "landed" repeats R1 under a new label. A probe that asserts "landed != HEAD" is wrong in the steady state, where HEAD equals `origin/main` (audit `JjAuditKotodama.md:97-99`). `lane-addendum.md:209-210` says to cite a hash only after remote verification. |
| E4 | R3 is not jj-caused: pin `c42d675` is reachable history | `git cat-file -t c42d675…` returns `commit`, `merge-base --is-ancestor c42d675 refs/heads/main` returns rc 0, and `is-shallow-repository` is `false`. jj does not garbage-collect reachable objects, so in a full clone this pin cannot vanish through jj. |
| E5 | R3 fail-open triggers that the claim does not name | (a) In the live lane with `GIT_DIR=/nonexistent`, `check-readme-revisions.py --selftest` prints `SKIP control: base c42d675 … (base object unreachable)`, `selftest skips: 1`, `all checks passed`, and exits **0**. The tool does not scrub `GIT_*` (`check-readme-revisions.py:305-309`), whereas `receipt_guard._git` does (`receipt_guard.py:49-51`; the same leak against the guard was still refused). (b) A git-free copy of the tool gives the same SKIP and exit 0. (c) A secondary workspace made with `jj workspace add` contains only `.jj` and `tools` (no `.git`), and the selftest gives the same SKIP and exit 0. In that temp repo the pin was absent anyway; the structural fact is that the workspace has no `.git`. |
| E6 | **The round's own Ca design manufactures R3.** The Ca dynamic leg "materializes base + X.lands … in a temp git-free dir and runs X.acceptance there". | Before O lands, `check-readme-revisions --selftest` in a git-free directory skips and passes (E5b), so the Ca leg is the R3 environment. After a correct O fix, the same acceptance turns nonzero. If O's acceptance includes the readme-rev selftest, Ca reports `SEPARABILITY_DEPENDENCY`/acceptance failure for O, or someone weakens the fix to keep it green. |
| E7 | Selftest pressure to weaken a control | `receipt_guard.py:234-235` asserts `committed_sha={head}` on every COMMITTED/REFRESH stderr. The fixture HEAD is `refs/heads/control` (`:174`) and it has no `main` or `origin` refs. If the fix redefines `committed_sha`, it breaks this control, and the tempting repair is to edit the control. Also, if the fix requires `refs/remotes/origin/main` to exist, it breaks the `unborn-receipt-allowed` (`:289-291`) and `untracked-receipt-allowed` controls. |

## Impacted axes

- **operability.** R2 is a real false negative (E1, E2). R3 is a real fail-open (E5). R1 risks
  turning into false provenance (E3).
- **calibration.** R1 is miscounted as a false negative. R3 is mislabelled as caused by jj (E4).
  The probe targets were fixed before the probe existed. The separability statement "O's probe
  builds synthetic git sandboxes from the tool bytes only" is either false or vacuous: a positive
  R3 control needs the real `c42d675` object from lane history, because a commit with that hash
  cannot be fabricated.
- **coverage.** No impact.

## Evidence that would falsify O

O is false if any of the following holds on the landed bytes:

1. **Real-jj R2.** The landed guard exits 0 on `case6/lane` (E1), or on the fetch-behind sandbox
   (E2), for a receipt present in `origin/main`.
2. **Provenance.** In the push-failed state (E3), the landed guard prints any sha labelled as
   landed or citable that is not an ancestor of `refs/remotes/origin/main`, or whose
   `origin/main` tree lacks the reported blob. The correct output is an explicit statement that
   the receipt is not landed.
3. **Label-only mutant.** Take the base guard and add only a print of `landed_sha=<HEAD>`. If the
   probe still scores R1 as fixed, the probe checks for the field's presence rather than git
   ancestry, which makes it circular.
4. **Vacuity mutants.** The probe scores 0/3 for either of these:
   - a guard that always exits 3, which must instead fail the probe's allow-path positive control
     (a new or untracked receipt is allowed);
   - a readme-rev selftest that always returns nonzero, or one with control 9 deleted. Either must
     fail a positive control: with the pin reachable, the selftest exits 0 and control 9 prints
     PASS.
5. **Non-jj R3.** The landed `check-readme-revisions --selftest` exits 0 with `GIT_DIR=/nonexistent`
   (E5a).
6. **Control loss.** The landed `receipt_guard --selftest` has fewer than 45 controls, or any base
   control name is missing or its assertion is weakened, including `:234-235`. The same applies if
   any of the 11 readme-rev check names is missing.
7. **Base bytes.** The probe does not report 3/3 on the base bytes for the stated reasons. In
   particular, its R1 base finding must come from an ancestry failure (E3), not from the absence
   of a new output field.

## Smallest safe corrections

1. **Guard semantics.** Keep `committed_sha` as the commit where the receipt was found (HEAD
   first), so control `:234-235` stays as written. Probe HEAD, `refs/heads/main` and
   `refs/remotes/origin/main`. Pass the resolved oids to `ls-tree` and refuse if any of them
   contains the path. Skip a missing ref with `rev-parse --verify --quiet` rc 1; do not fail
   closed on it, because that would keep the unborn and fixture controls green. Add a separate
   `landed_sha=<origin/main oid>` only when `origin/main`'s tree contains the receipt, and print
   `landed_sha=none` otherwise. Never treat `refs/heads/main` as landed.
2. **Guard controls.** Add fixture controls using the existing hand-rolled object store
   (`_fixture_repo`) for three states: fetch-behind (HEAD = C1, while `main` and `origin` = C2
   hold the receipt), push-failed (HEAD = `main` = C2 holds it, `origin` = C1 lacks it, so
   `landed_sha=none`), and steady state (all three equal, so landed = HEAD).
3. **Readme-rev.** Run git through a `GIT_*`-scrubbed environment, using the same pattern as
   `receipt_guard._git`. Check `cat-file -e <pin>^{commit}` first. When the pin is unreachable,
   report it as a failure and exit **2** from `--selftest`, following the tool's own contract
   (could-not-evaluate = 2, `:34-35`), rather than 1, which means a finding. The skip machinery
   can stay for the record, but a skip must not leave `ok` true.
4. **Probe.** Fix the R1 oracle to git ancestry plus a blob check against `origin/main`. Include
   the positive controls and the label-only, always-refuse, always-fail and deleted-control
   mutants from item 4 of the falsification list, and report each mutant's result. Rename the
   metric from "3 false negatives" to "3 defects (1 false negative, 1 false provenance, 1 fail-open
   skip)". Mark R3 as not jj-specific, and add the `GIT_DIR` leak and the git-free/jj-workspace
   triggers.
5. **Separability.** Either leave the readme-rev `--selftest` out of O's Ca `acceptance` argv, or
   have Ca treat exit 2 as could-not-evaluate rather than a dependency. The O and Ca owners must
   agree on one of these before Ca runs on the round-50 manifest (E6).

## Peer follow-up (CriticCalibration, 15:29Z)

CriticCalibration has independently verified E6: the base selftest prints SKIP and exits 0 in a
directory with no git repo. It has folded this into its own controls:

- **Control 12** runs a git-backed counterfactual, with the lane's objects attached read-only
  through `clone --shared`. If it cannot do that, it returns COULD_NOT_EVALUATE with exit 2,
  never 0 or 1.
- **Control 10** requires acceptance to fail on a base-only tree, so a vacuous SKIP pass is
  flagged.
- **Interim:** keep the readme-rev selftest out of O.acceptance.

I agree with all three. Two caveats:

- **Control 10 must match a selftest skip count of zero, not just exit 0.** Base
  `check-readme-revisions` exits 0 even when a control skips. Control 10 has to require the line
  `selftest skips: 0` (or, after O, exit 2 when the pin is missing).
- **The `clone --shared` command must run with `GIT_*` variables cleared.** E5a showed that a
  leaked `GIT_DIR` silently retargets git.

## Unrun checks

- No O patch or probe existed to run, so none of the falsifiers above was executed against landed
  bytes.
- Whether jj's push-recovery path leaves HEAD below the tip in the real helper (rather than in my
  plain `jj git fetch` reproduction) is [INFERENCE] from `jj-lane.sh:285-288`. I did not run the
  helper.
- I sent the E6 coupling to `ChousaR27R2.CriticCalibration-4` as a one-line peer note.

Sandboxes: `/tmp/critop-*`, temp dirs only, all removed. I ran no command that writes to the lane,
the fleet repo or case6. No tools were installed or updated.
