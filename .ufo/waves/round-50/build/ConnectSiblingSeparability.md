# ConnectSiblingSeparability — round 50, item Ca (sibling sweep)

Seat `ChousaR27R2.ConnectSiblingSeparability-4` (connector, leaf). Author-lane advice, never
admission. Assigned item: sweep sibling lanes' `tools/` and lessons (read-only) for existing
claim-separability checkers or counterfactual runners; report reusable patterns and any lane
whose rounds were rejected on separability. Lane writes: this report only. No installs. No
production file touched. All lane reads were `git show` / `cat-file` / `grep`; scratch model ran
under `/tmp/sepsweep/` only, outside the lane and outside any work tree.

Axes named: **calibration** (the tool's verdicts must have a measured false-positive AND
false-negative side), **operability** (durable `tools/` control, house exit contract),
**coverage** (the round's real dependency on frontier rows must be visible, not renamed away).

## Result 1 — fleet inventory: exactly one automated per-claim runner, zero durable controls

- The only automated claim-separability runner in any lane is wave scratch, not a lane control:
  `kagi-shokunin/.ufo/waves/round-24/tools/claim-separability.py`. kagi has **no `tools/` dir at
  all** (`ls kagi-shokunin` → `AGENTS.md LOG.md PROVINCE.md README.md SCORECARD.md SHONEN.md
  SKILL.md considerthese corpus plans`).
- Its decisive defect: only the `c2-only` leg materializes a counterfactual tree
  (`claim-separability.py:27-32`: clone `--no-hardlinks`, checkout `manifest['base']`, copy claim
  inputs). The `c1-only` and `c3-only` legs run **against the live lane** —
  `claim-separability.py:33-36` sets `root = lane` and invokes the wave tool in place. The
  recorded "All three processes exit 0" therefore measured command success, not separability.
  Named independently by kagi's own reviewers:
  `kagi-shokunin/.ufo/waves/round-25/build/CritSeparability.md:30` ("None is a like-for-like
  overlay ledger run") and `kagi-shokunin/.ufo/waves/round-27/build/CritSeparability.md:17,105`
  ("The plan's separation mechanism ('executed claim-only overlays') has no artifact").
- No lane ships a semantics-equivalent under another name: `find */tools -iname '*separab*'`
  returns nothing; a `git show|cat-file` sweep of `*/tools/*.py|*.sh` finds gates and censuses,
  not per-claim tree assembly. **Kotodama's Ca would be the fleet's first durable lane-owned
  separability control.** That raises the bar: it is the precedent, so it must carry what kagi's
  scratch runner lacked (negative controls, like-for-like legs, exit discipline).

## Result 2 — reusable patterns (each proven somewhere, with the cost it paid)

1. **Frozen overlay + digest tamper check.** `claim-separability.py:18-21` reads
   `separability/<label>/expected.json` `{base, inputs:{path: sha256}}` and refuses with
   `snapshot_tampered: <path>` before running. Cheap; catches fixture edits. Ca's fixture should
   pin its trees the same way (but pin *commit ids*, which are already immutable).
2. **Counterfactual tree from committed blobs only.** kagi r25 used
   `git archive BASE` + `git archive CAND -- <paths>`
   (`kagi-shokunin/.ufo/waves/round-25/falsify/FSeparability.md:1-6`); tameshi's runner
   materializes cases with `git show <rev>:<path>` "immune to working-tree drift"
   (`tameshi-shokunin/tools/mutate-and-run.sh:10-13`). Ca's contract already restricts it to
   `git show`/`cat-file` — keep that; it is the jj-safe form (fixed shas, no HEAD, no index).
3. **Sandboxed environment + per-leg receipt.** `claim-separability.py:22-27` runs with
   `env -i`-style `{PATH, HOME=<tmp>, LANG}`; `:39` records `{manifest, command, exit, stdout,
   stderr}` per leg to JSON. Adopt both; add the house exit codes 0/1/2 (below).
4. **Negative control per claim — the discriminating leg.** kumitate's
   `ReviewSeparability.md:15`: the claim's *cases-only* patch on base code must fail its selftest
   (`t/c1n` → 103/107, "FAILs are exactly the 3 new distinct cases ... not vacuous"). A positive
   leg alone cannot distinguish "the claim works" from "the runner is inert".
5. **Byte-exact recomposition sanity.** `ReviewSeparability.md:30` (E1): applying both claim
   patches must reproduce the integrated file byte-exact, else the claim split is wrong. For Ca's
   fixture this is the check that a claim's `lands` really are the paths that changed at its tree.
6. **Removal matrix, not a single verdict.** tabi r18 `corpus/lessons/round-18.md:148-152`:
   baseline 51/6/5; remove C1 inputs → 0/6/5; remove C2 scripts → 51/0/5; remove C3 repairs →
   51/6/0. A per-claim metric vector under each removal is stronger and more falsifiable than
   pairwise "dependent/separable".
7. **Label every ordered pair, report TP/FP/FN/TN, and mutate the checker.** The r49 fixture as
   specified has 1 labelled positive and 0 negatives, so an always-dependent tool scores "1/1".
   Use r48 as a real-history mixed fixture with per-direction labels (Ca→C positive, C→Ca
   negative, C/Ca README overlap) **and** add a synthetic negative (base plus a claim that lands
   an unreferenced new file; a temp git repo in `--selftest`), so the FP rate is not measured
   only on author-built inputs. Run two mutants (always-dependent, always-separable); both must
   fail the fixture. This is the calibration axis in one line.
8. **Forgery probe / opaque fixtures.** `mori-shokunin/corpus/lessons/2026-10-15-forgeable-oracle-visible-fixtures.md:19-24,82,95-108`:
   a checker whose case identity leaks can be answered by identity; the hardened oracle drops the
   cheat from 27/27 to 1/28 and keeps a forgery probe in its repertoire. Applied here: the fixture
   must not encode the expected finding in the claim id or in a filename the checker can special-
   case, and `--selftest` should contain a stub "checker" that reads the expected label.
9. **"Measurement-separable" vs "landing-separable".** `souji-shokunin/.ufo/waves/round-17/w1/ConnClaimSeparability.md:1-10`:
   a claim can pass the static/measurement leg and still fail to land alone (its own frozen pin
   moves). Ca's static leg is measurement; the optional acceptance leg is landing. Say which one
   the verdict reports.
10. **Export novelty from a base freeze.** `kengaku-shokunin/corpus/lessons/round-25.md:18` (M27):
    round 24's C1 created the registry row C2 counted — the exact r49 class. The fix there was to
    freeze the population at base and scope the census to base-defined ids. This converts directly
    into an export rule: an export regex must match **0 times at base** or it is not that claim's
    export (see Result 4).
11. **Judge independence + hermetic selftest.** `tsukuroi-shokunin/tools/check-revision-binding.py:10`
    ("it grades the tools and must not share what it grades") and `:43` ("`--selftest` is
    hermetic: stub tools in mktemp fixtures, never the real lane"). Ca's checker must not import
    the lane's git helpers, and its selftest must build temp repos, never read the live lane.
12. **House exit contract, already in the lane.** `tools/check-readme-revisions.py:33-36`
    (0 clean / 1 finding / 2 could-not-evaluate, exceptions → JSON `ok:null` + exit 2) and
    `tools/replay-frozen.py` `repo_path()` (refuses traversal/symlinks, mirrors before running).
    Ca's `--selftest` should follow these, not kagi's argv-slot shape.

## Result 3 — lanes rejected (or falsified) on separability

| lane | outcome | evidence |
|---|---|---|
| kotodama r49 | REJECTED-HONEST-STOP, C cites the registry S created; the `c_without_s` leg measured "no inline URL", not counterfactual resolvability | `corpus/lessons/round-49-verifier-spotcheck.md:17`; `reports/round-49/run-validation.py:264-273` |
| game-dev-2d r105 | REJECT AS DECLARED / HONEST STOP: C2's QUALITY creation was C3's admission prerequisite | `corpus/lessons/round-105-verifier-spotcheck.md:17`; `round-105.md:188` |
| kengaku r25 | round not rejected, but M27 records the same class (C1 created the row C2 counted) and its fix is the base freeze | `corpus/lessons/round-25.md:18` |
| kagi r27 | overclaim rejected: claims not file-disjoint, a shared hunk (`SKILL.md @@ -46,3`, `README.md` one section) mixes both, and the separation mechanism had no artifact | `.ufo/waves/round-27/build/CritSeparability.md:105-120` |
| souji r12 | C2 separability *falsified* by a critic; K1 had been admitted through C3's gate | `corpus/lessons/round-12.md:155` |
| souji r17 | not rejected; C1 "measurement yes, landing no" — the frozen r15 pin moves with C1's own bytes | `.ufo/waves/round-17/w1/ConnClaimSeparability.md:1-10` |
| kumitate r35, tabi r18, tsukuroi r18 | held, via per-claim trees + negative controls (kumitate), removal matrix (tabi), three rollback experiments (tsukuroi) | `ReviewSeparability.md:15,30`; `round-18.md:148-152`; `tsukuroi/corpus/lessons/round-18.md:127` |

No other lane in `*/corpus/lessons` carries a round rejected on separability. The class is
unanimously treated as a **claim-declaration** defect, not a landing defect — which is why a
durable control belongs in `tools/`, not in a wave report.

## Result 4 — the contradiction, measured, and one resolution

The contract-literal rule ("X's landed bytes match any Y export regex or name any Y land path")
is false in both directions on real committed bytes. I re-ran it with a ~60-line reference model
(`/tmp/sepsweep/model.py`, read-only `git show`; rebuilt from the rule in the shared contract):

| input | literal rule | truth |
|---|---|---|
| r49 (`base c42d675`, trees `c6a174d`; S export `\bS0(0[1-9]\|[1-3][0-9]\|4[0-3])\b`) | rc=1, 4 pairs: C→Ca, C→S, S→C, S→Ca | spot-check names C→S only; critic adds S→C and C↔Ca |
| r48 (`base a01405d`, tree `78f77a6`, admitted) | rc=1, C→Ca | C→Ca is a false hit (README pre-exists), but r48 is genuinely coupled in the other direction: Ca→C via `reports/round-48/calib/queue-successor-r48.json:134,144` (G1 requires the entry landed). The literal rule was right for the wrong reason. |
| r50 base bytes (`4ad2683`) | rc=1, C→O **and** O→C | no r50 bytes exist; `after_required` unattainable |

Root cause, in one sentence: **a reference that already resolves in the base tree is not a
dependency on Y, because X's counterfactual tree (base + X.lands) still resolves it.** Concretely
`tools/check-readme-revisions.py:306` (`git show <BASE_COMMIT>:corpus/README.md`) works at base, so
O does not need C's README row; `corpus/SOURCES.md` does **not** exist at `c42d675`
(`git cat-file -e c42d675:corpus/SOURCES.md` → absent), so C's entry cannot resolve its citations
without S. Path-mention classification (prose vs backtick vs executable reference) cannot make
this distinction — only base-resolvability can. The test is per *referent*, not per file: a path
can pre-exist at base while the cited rows inside it are new (round 50: `corpus/SOURCES.md`
exists with S001–S047, C cites S048+), so gate 1 and gate 2 answer different questions and both
are required.

Four gates, applied per claim X and land path L. They are necessary, not sufficient: F5 (a
negated new path), F2 (novel-but-incomplete export), F7 (dead regex) and F8–F12 stay open and
must be carried by the other controls in Result 2 (reference-vs-mention, mechanically derived
exports, liveness, exit discipline, acceptance discrimination, hermeticity).

1. **Base-absence gate (paths).** A path hit counts only when `git cat-file -e <base>:<path>`
   fails. Pre-existing paths (README, QUALITY, `LOG.md`) are ambient in every round.
2. **Export novelty gate (ids).** Each export regex must match 0 times at base (`git grep -P
   <rx> <base>`); otherwise exit 2 — a declared export that base already contains is not Y's
   contribution (kengaku M27's freeze, made mechanical). At `4ad2683` the plausible round-50
   export `\bS0(4[8-9]|5[0-9])\b` matches 0 files, while `\bS\d+\b` matches hundreds (stage labels
   S0–S5), so novelty is cheap and decisive.
3. **Shared-land exclusion.** Bytes of a path in `X.lands ∩ Y.lands` are reported as
   `SEPARABILITY_OVERLAP` (exit 1; the contract already says lands are disjoint) and are not used
   for directed dependency. r49's `corpus/README.md` is one `revision: 2.6` paragraph edited by
   both C and Ca, so per-path lands cannot attribute its bytes to either.
4. **Ledger exclusion by line class, with a warning net.** In `corpus/lessons/round-N.md`, scan
   table rows **and bullet lines** under headings matching `^## (Gate|Registry changes)` — the
   registry evidence (URL/date/quote rows, and the integrator's normalization bullets at
   `round-49.md:77`, which re-scope rows and name the entry by basename). `LOG.md`,
   `SCORECARD.md` and `SHONEN.md` are integration-owned and are not scanned as dependent
   sources. Every *excluded* section is still matched: a hit there prints
   `SEPARABILITY_LEDGER_MENTION <file>:<section>` as an advisory line and never changes the exit
   code, so a hand list of evidence sections cannot silently drop a dependency. This is more
   precise than both alternatives on real bytes: r49's `round-49.md:12` (prose) and `:152` (a
   `## Mistakes` table row) name `tools/check-readme-revisions.py`, so whole-file exclusion would
   drop a possible Gate-row dependency while an all-tables scan would fire on narration.

Measured effect of the four gates (`/tmp/sepsweep/model4.py`, Gate + Registry-changes scan):

| input | result |
|---|---|
| r49 | **2 deps + 1 overlap**: C→S (id S031–S042 *and* path `corpus/SOURCES.md` in the entry), S→C (`SOURCES.md` used-by names the entry path, 12 occurrences), OVERLAP C/Ca `corpus/README.md`; Ca↔S clean |
| r48 | **Mixed, per direction**: Ca→C TRUE; C→Ca NEGATIVE; OVERLAP C/Ca `corpus/README.md` (detail below) |
| r50 base bytes | 0 deps, 0 overlap — honest green *because nothing has landed*, not because the scan was narrowed |

r48 detail (base `a01405d`, tree `78f77a6`): **Ca→C is TRUE** —
`reports/round-48/calib/queue-successor-r48.json:134,144` makes the entry's landed presence a G1
closure condition, and the file is added at base. **C→Ca is a NEGATIVE** — C's entry names
`corpus/README.md` and Ca owns README, but the path exists at base, so the entry does not need
Ca's bytes. **OVERLAP C/Ca `corpus/README.md`** — both claims edited it (C's row plus the rev-2.4
prose vector per `reports/round-48/claims.json` C; the duplicate-heading removal per Ca). r48 is
a three-way labelled fixture, not a whole-round negative, and it is the real-history negative the
critic asked to keep alongside the synthetic one. My earlier "r48 → 0" held only because I had
hand-picked Ca's lands and dropped the calib artifact.

Adding `## Registry changes before landing` to the scanned set changes no r49 verdict (measured):
its bullets name S028–S030/S043, which S itself owns, and the entry by basename only, so the
directed set stays at C→S and S→C. The warning net does fire as designed — the excluded
`## Mistakes` section names `corpus/README.md` and `tools/check-readme-revisions.py`, printed as
`SEPARABILITY_LEDGER_MENTION` advisories with the exit code unchanged. Basename resolution for
unique land basenames was also tried and adds nothing on these fixtures; keep it advisory.

The r48 correction is the general lesson: **hand-picked lands hide dependencies.** Lands must be
`git diff --name-only base <tree>` partitioned by declaration, and any changed path not assigned
to a claim or to an explicit `non_claim` entry is itself a finding (control 1). The synthetic
negative (base + a claim that lands an unreferenced new file) stays in `--selftest` so the false-
positive rate is not measured only on author-built inputs.

The remaining contradictions are semantic, not lexical. First, with control 1 (a `FRONTIER`
non-claim pseudo-owner) the r50 manifest at **tip** reports `C->FRONTIER` — C's pastoralism entry
cites S048+ rows that no claim lands. Labelling those edges `SEPARABILITY_PREREQUISITE`
(printed, exit 0) while claim-to-claim edges are `SEPARABILITY_DEPENDENCY` (exit 1) lets both
`claims.json`/manifest exit 0 and the frontier dependency stay visible — but **only when the
manifest declares the prerequisite in `non_claim` with its own evidence**; an undeclared producer
stays a dependency (exit 1) and an unowned changed path is itself a finding. Second, the path leg
is **blind where the file pre-exists**: `corpus/SOURCES.md` exists at `4ad2683` (S001–S047), so
`C->FRONTIER` is invisible to gate 1 no matter how it is cited; only exports **mechanically
derived from the added `| Snnn |` rows** at C's tree, novelty-checked at base, can catch it. A
hand-declared export range is one stale range away from a false separable (F2). Third, the
prerequisite label **renames the r49 defect by declaration** — the judge must rule on that
(game-dev-2d r105 rejected precisely a declared prerequisite standing between two claims). My
recommendation is to keep the prerequisite edge in the printed output and the exit-0/1 split, and
to change Ca's `after_required` from "claims.json exits 0" to "the derived r50 manifest reports
exactly the judged set (expected `C->FRONTIER` plus no other pair)", because that is the only
wording that can be true both before and after landing.

## Proposed move (one, bounded)

Adopt the four-gate reference rule as the semantic core of `tools/check-claim-separability.py`
and label the r49 fixture with the measured set above (C→S, S→C, OVERLAP C/Ca, Ca↔S clean),
reusing patterns 2, 3, 4, 7, 11, 12; add **two** negatives — the real-history r48 mixed pair
(Ca→C labelled positive, C→Ca labelled negative, C/Ca README overlap) and a synthetic
unreferenced-new-file case inside `--selftest` — plus the two checker mutants of pattern 7. Affected axes: calibration (a measured FP side and a real negative instead of an
admitted round retro-labelled), operability (the tool follows the lane's 0/1/2 +
hermetic-selftest house form instead of kagi's argv-slot script), coverage (the frontier edge
stays printed and separately counted). No axis is harmed: the r49 detection is preserved by
measurement, not asserted.

## Risks

- **Prerequisite label as an escape hatch.** Any round can re-declare a claim as "non-claim" and
  go green (the critic's F1). Mitigation: prerequisites are listed per manifest, each path must
  be absent from every claim's lands, and the printed prerequisite edges are part of the
  calibration record the next outside spot-check reads.
- **Hand-picked lands hide dependencies.** My own first r48 measurement missed Ca→C because I
  assigned Ca only README. Mitigation: derive lands from `git diff --name-only base <tree>` and
  treat any unassigned changed path as a finding; never let a manifest author choose a convenient
  subset silently.
- **Ledger exclusion.** Lessons narrate every claim (r49 `round-49.md:12` prose and `:152`
  Mistakes row name Ca's tool; `:77` Registry bullets name the entry). Gate 4 scans Gate and
  Registry-changes rows/bullets and prints excluded-section hits as advisory
  `SEPARABILITY_LEDGER_MENTION`, so neither a whole-file exclusion nor a section whitelist can
  silently hide a dependency; the dynamic leg catches an acceptance that actually reads a ledger.
- **Shared-land exclusion can hide real coupling.** r49's README paragraph really does couple C
  and Ca; the rule demotes that from dependency to overlap. It is still exit 1 and still printed.
- **Dynamic leg cannot run O.** O's gates read git and jj; in the contract's git-free temp dir
  they fail 128 and would read as a false dependency. O needs a `needs_git` leg (materialize base,
  commit, then apply X) or no acceptance leg at all this round — `claims.json` declares none.
- **Git-object survival.** The fixture reads `c42d675`, `c6a174d`, `a01405d`, `78f77a6`; under jj
  colocation these are ordinary git objects, but a future `git gc` without them breaks the
  fixture. Record them in the fixture header (control from `tools/replay-frozen.py`'s manifest).

## Verification (read-only; main should run)

```sh
git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin cat-file -e c42d675:corpus/SOURCES.md; echo $?   # 1 = absent
git -C ... cat-file -e a01405d:corpus/README.md; echo $?                                                # 0 = present
git -C ... show c6a174d:corpus/SOURCES.md | grep -c 'culture-material/hunting-foraging-subsistence.md'  # 12
git -C ... show c6a174d:corpus/knowledge/culture-material/hunting-foraging-subsistence.md | grep -oE '\bS0[0-9]{2}\b' | sort -u | wc -l  # 13 ids cited
git -C ... show 4ad2683:tools/check-readme-revisions.py | grep -n 'corpus/README.md'                    # :2 and :306
git -C ... show c6a174d:corpus/lessons/round-49.md | sed -n '12p;152p' | grep -c 'check-readme-revisions'  # 2 (prose + Mistakes row; neither scanned)
git -C ... show c6a174d:corpus/lessons/round-49.md | sed -n '77,107p' | grep -c 'hunting-foraging-subsistence.md'  # 1 at :100 (Registry bullets, basename only)
git -C ... show 78f77a6:reports/round-48/calib/queue-successor-r48.json | grep -n 'cartography'          # :134 G1, :144 landed_path
git -C ... show 4ad2683:corpus/SOURCES.md | grep -cE '^\| *S[0-9]{3} *\|'                                 # 47 -> path leg blind to new rows
```
Then, after the executor patch exists: r49 fixture exits 1 with C→S and S→C named and OVERLAP
C/Ca printed, Ca↔S absent, and the excluded-section mentions printed as
`SEPARABILITY_LEDGER_MENTION` without changing the verdict; the r48 mixed fixture labels Ca→C
positive, C→Ca negative and prints the README overlap; the synthetic negative exits 0; the r50
manifest exits 0 with `C->FRONTIER` printed as a declared prerequisite (undeclared → exit 1);
both checker mutants (always-dependent, always-separable) fail the fixture; `--selftest` passes
with the new controls; an unassigned changed path exits 1.

## Unrun

- No `tools/check-claim-separability.py` patch existed to test (`.ufo/waves/round-50/patches/` is
  empty); the four-gate rule was measured against my own reference model, not the executor's.
- F5/F2/F7/F8–F12 were not measured under any implementation; they are assigned to controls in
  Result 2, not claimed closed by the four gates.
- Lands for the r48 re-measurement come from `git diff --name-only a01405d 78f77a6`; I did not
  re-derive r49's full partition from the diff, so a further pair may exist under a complete
  ownership map.
- The `FRONTIER` pseudo-owner was reasoned from `claims.json` `separability_contract`, not run.
- I did not read the pastoralism entry or the round-50 SOURCES rows (neither had landed).
- I did not measure O's dynamic leg against a git-backed counterfactual.
- Sibling sweep covered `*/tools`, `*/corpus/lessons`, `*/corpus/QUALITY.md` and wave `build/`,
  `falsify/` reports under `*/\.ufo/waves`; I did not read every `w1/` report in every lane.

Report: `.ufo/waves/round-50/build/ConnectSiblingSeparability.md`
