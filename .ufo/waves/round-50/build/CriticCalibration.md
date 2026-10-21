# CriticCalibration — round 50, claim Ca (separability control)

Seat: `ChousaR27R2.CriticCalibration-4` (critic, leaf). Author-lane advice, not admission.
Assigned item: is a static citation scan with an optional acceptance rerun a genuine separability
control? Build inputs that give false-separable and false-dependent verdicts, and list the
required controls.

## Verdict

As specified, the tool (shared contract in the build spec; `claims.json` Ca `after_required`) is
not yet a genuine separability control. It detects lexical co-mentions, and that proxy fails in
both directions on **real lane history**:

- **False dependent on a round that was admitted as separable.** Round 48 (C cartography and Ca
  README/heading control) was admitted, yet the tool returns exit 1 whichever claim owns README.
- **False separable for the round-49 defect itself.** Round 50 repeats that defect under a new
  label: the source rows C cites are declared a "frontier step (not a claim)" (`claims.json`
  `separability_contract`). No claim exports them, so the tool exits 0 by construction.
- **Unattainable acceptance criterion.** "Run on `reports/round-50/claims.json` exits 0" fails on
  **base bytes**, before any round-50 byte lands.

Most of this is fixable inside Ca (see the controls list). One item is a tradeoff the canonical
judge must rule on: is a declared non-claim prerequisite (the frontier source rows) acceptable,
or must C own those rows?

## Method (reproducible, ephemeral)

I wrote a contract-literal reference model at `/tmp/sepcrit/model.py`. For each ordered pair X≠Y,
X depends on Y if X's landed bytes at X.tree match a Y export regex or contain a Y land path. An
optional dynamic leg runs X.acceptance in a git-free temp dir holding base plus X.lands.

I ran it on:

- real lane commits, via read-only `git show`;
- a synthetic temp repo at `/tmp/sepcrit/syn`, using `/tmp/sepcrit/cases.py`.

No lane file other than this report was written. No executor patch for
`tools/check-claim-separability.py` existed when I checked (`.ufo/waves/round-50/patches/` is
absent), so I critiqued the contract, not a patch. Any implementation that follows the contract
text literally inherits every result below.

## Evidence from real history

| input | contract-literal result | ground truth | class |
|---|---|---|---|
| r49 real (base `c42d675`; C, Ca and S all land in `c6a174d`; S export `\bS0(0[1-9]\|[1-3][0-9]\|4[0-3])\b`) | rc=1, 11 findings covering **all 6 ordered pairs** | spot-check labels only C→S dependent; Ca was "verified" | C→S is a true positive, but the fixture can't tell this tool apart from one that always says "dependent" |
| r48 real (base `a01405d`, tree `78f77a6`; admitted) | rc=1 with README owned by Ca (C→Ca, Ca→C) and rc=1 with README owned by C (Ca→C ×2) | separable (admitted) | **false dependent** |
| r50 shape on base bytes (`4ad2683`; C=`corpus/README.md`, O=both gates, Ca=`corpus/QUALITY.md`) | rc=1: `C->O` (README revision prose names `tools/check-readme-revisions.py`), `O->C` (`tools/check-readme-revisions.py:2,50,306` name `corpus/README.md`) | no round-50 bytes exist yet | **false dependent**; makes `after_required` unattainable without weakening the check |
| `reports/round-50/claims.json` fed directly | `KeyError: 'tree'`, rc=1 | input error (exit 2) | **exit-code collision**: an uncaught exception looks like a dependency verdict |

Supporting anchors:

- **r49 README edit is shared.** `c6a174d:corpus/README.md:3` opens one `revision: 2.6` paragraph
  that describes both C (the row, 224→225) and Ca (the dedupe plus the
  `tools/check-readme-revisions.py` control). Both claims edited one file and one paragraph, so
  per-path `lands` can't separate them.
- **Path mentions sit in the entry contract's own provenance lines.**
  `78f77a6:…/cartography-and-mapmaking.md:21` and `c6a174d:…/hunting-foraging-subsistence.md:21`
  carry `verified-at` lines naming `corpus/README.md`. Any C entry built to the contract will
  contain other claims' paths as provenance, not as dependencies.
- **The hunting entry names the S registry both ways.** `c6a174d:…/hunting-foraging-subsistence.md:18,201`
  name `corpus/SOURCES.md` and S031–S043. The pastoralism model inherits this, so C will name
  `corpus/SOURCES.md` and S048+. No round-50 claim lands either of those.
- **Generic ids are everywhere at base.** `\bS\d+\b` matches **660 files** at `4ad2683`, including
  stage labels S0–S5 (`historical-linguistics.md:244-248`, `taboo-strata-lifecycle.md:34`) and
  `S94` (`costume-language-coupling-table.md:18`). A plausible round-50 export
  `\bS0(4[8-9]|5[0-9])\b` matches 0 files at base, so a novelty check is cheap and decisive.
- **Round-49 runner precedent.** The runner put its counterfactual temp file inside the repo
  (`reports/round-49/run-validation.py:295-296`, `dir=scratch` under ROOT). Its C-without-S leg
  passed on "no inline URL" (`:273`). That is the leg the spot-check rejected.

## Synthetic counterexamples (`/tmp/sepcrit/cases.py`)

| case | contract result | truth | class |
|---|---|---|---|
| **F1 undeclared producer**: C cites S048/S049 rows added by a non-claim "frontier" step (the round-50 shape) | rc=0 | C depends on the rows | **false separable** (the r49 defect, renamed) |
| F1b: same, with a C acceptance that resolves cited ids | rc=1 via acceptance | dependent | caught **only if** acceptance argv exists; `claims.json` declares none, so the dynamic leg is inert this round |
| F2 stale export range (S exports `\bS04[4-7]\b`; C cites S048) | rc=0 | dependent | **false separable** (exports are hand-declared) |
| F3 relative link `../SOURCES.md` for land `corpus/SOURCES.md`, no exports | rc=0 | dependent | **false separable** (literal path match) |
| F4 broad export `\bS0\d*\b` vs stage labels S0–S5 and base-only S031 | rc=1 (`S0` matched) | separable | **false dependent** |
| F5 prose negation: "does not use tools/check-claim-separability.py" | rc=1 | separable | **false dependent** |
| F6 Ca's own tool or fixture strings name `corpus/README.md` (r50 C's land; the r49 fixture must list r49 C's `corpus/README.md`) | rc=1 Ca→C | separable | **false dependent** on the real round-50 run |
| F7 JSON over-escaped export `\\\\bS04[89]\\\\b` | rc=0, silent | dependent | **false separable** |
| F8 land deleted at its tree | traceback, rc=1 | input/deletion case | **exit-code collision** |
| F9 acceptance `["true"]` | rc=0; also passes on a base-only tree | uninformative | **vacuous dynamic leg** |
| F10 acceptance reads a live absolute path | rc=0; base-only also rc=0 | uninformative | **hermeticity escape** |
| F11 git-reading acceptance (like O's gates) in the git-free dir | rc=1 (git 128) | separable | **false dependent**; O can never pass the dynamic leg |
| F11b counterfactual dir created under a repo (r49 precedent) | `git rev-parse --show-toplevel` → enclosing repo | reads live lane | **false separable** risk |
| F12 C and Ca both land `corpus/README.md` at one tree; C's acceptance needs Ca's dedupe | rc=0 | true counterfactual (base README + C's hunk only) **FAILS** acceptance | **false separable** (file granularity) |

## Refinement tested: scan added lines only

I scanned only the added lines in `git diff base tree -- <land>`, and reported overlaps
separately. This removes the base-byte false positives (the r50 shape and F4's pre-existing text)
and keeps r49 C→S (`S031`, `corpus/SOURCES.md`). It still reports `SEPARABILITY_OVERLAP C<->Ca`
on README.

What remains are path mentions in narrative ledgers: r49 S lands `corpus/lessons/round-49.md`,
which narrates every claim. So path mentions must not be proof of dependency by themselves.

## Peer rule measured: count a reference only if it is unresolvable at base (ConnectSiblingSeparability)

The rule has three parts: a path hit counts only if `git cat-file -e <base>:<path>` fails, an
export must match 0 times at base, and shared-land bytes are reported as `OVERLAP`. I measured
it with lands taken from the actual commit diffs:

| input | result | assessment |
|---|---|---|
| r49 | C→S (export and path), S→C (`used-by`), OVERLAP C/Ca README, **plus S→Ca** (`corpus/lessons/round-49.md:12` narrates that `tools/check-readme-revisions.py` landed, and that file is absent at `c42d675`) | the S→Ca hit is a ledger mention, so still a false dependent. Ca↔S comes out clean only if the lesson leaves S's lands, but the r49 addendum names it as S's verification surface. Control 8 is still needed |
| r48 | Ca→C via `queue-successor-r48.json` (the closure gate's `landed_path`) | true positive (see the correction in control 14); "r48 → 0" holds only if that file is left out of Ca's lands |
| r50 base stand-in | separable | fixes the base-byte false dependent |
| F4, F6 | resolved | — |
| F5 (negation naming a *new* path) | still reported as a dependency | still needs control 7 |
| F3 / r50 shape (Y appends rows to a file that exists at base) | the path leg is silent by design | detection rests entirely on the exports |
| F2 novel but incomplete range, F7 over-escaped regex | separable | still needs controls 5 and 6 |
| F1, F8–F12 | untouched (ownership, exit codes, dynamic leg) | still needs controls 1 and 9–12 |

Adopted: the rule replaces control 3 for the path leg and satisfies control 4.

Consequence for round 50: `corpus/SOURCES.md` exists at base, so `C->FRONTIER` can be detected
only by control 1 (the frontier as a scanned pseudo-claim) together with control 6 (exports
derived mechanically from the added `| Snnn |` row ids). Hand-declared exports leave the round-49
defect undetectable.

Convergence with ConnectSiblingSeparability (Result 4 in their report). We agree on four points:

- lands are `git diff --name-only base <tree>` partitioned by declaration, and any unassigned
  path is a finding;
- ledger exclusion applies only to the dependent scan, never to dependency targets;
- round 50's C→FRONTIER is detectable only through derived exports plus novelty at base;
- F2, F5, F7 and F8–F12 stay assigned to the other controls.

Two points where I hold a different position:

- **Negatives.** A synthetic negative in `--selftest` is necessary but not enough on its own.
  Keep r48 C→Ca as a *real-history* negative, labelled per direction. Otherwise the tool's
  false-positive rate is measured only on inputs its author constructed.
- **Ledger scope.** Exclude by line class, not whole file. `corpus/lessons/round-N.md` `## Gate`
  rows are registry evidence (URL, access date, quote), not narrative. A Gate row quoting a
  source row that only another claim creates is a real dependency, and whole-file exclusion would
  hide it. Scan Gate and other table rows; exclude only narrative prose.
  - *Resolved with ConnectSiblingSeparability:* scanning every table row is too broad. In
    `c6a174d:corpus/lessons/round-49.md`, `tools/check-readme-revisions.py` appears at `:12`
    (prose before the first section) and at `:152`, a table row under `## Mistakes` (`:108`).
    Narrative tables would fire on that. The adopted rule is section-aware: scan only table rows
    under evidence sections, and skip LOG, SCORECARD and SHONEN entirely.
  - *Residual:* the section list is maintained by hand. `## Registry changes before landing
    (integrator normalization)` (`:77`) also records registry evidence and should be on the list.
    Any evidence section left off the list is unscanned. The tool should print a warning
    listing the unscanned sections that contain tables, rather than drop them silently.

Measured in their section-aware model (my reference model did not rerun these):

- r49: C→S, S→C, OVERLAP C/Ca, Ca↔S clean;
- r48: Ca→C, OVERLAP C/Ca (both claims own README per `reports/round-48/claims.json`), no C→Ca;
- r50 base: clean.

This matches the per-direction labels in control 14.

Final state agreed with ConnectSiblingSeparability (I spot-checked the line claims):

- **Scanned sections.** `^## (Gate|Registry changes)`, covering both table rows and bullet lines.
  The Registry section spans `round-49.md:77-107`.
- **Verdict unchanged.** Line `:100` names the entry by basename only
  (`hunting-foraging-subsistence.md`) alongside S-owned ids, so r49's directed set stays C→S and
  S→C.
- **Ledger warnings.** Excluded sections still produce a `SEPARABILITY_LEDGER_MENTION
  <file>:<section>` warning without changing the exit code. On r49 it fires on `## Mistakes`.
- **Basename resolution is advisory.** It adds nothing on these fixtures. Only full-path
  references and derived exports decide the verdict. A basename-only dependency is therefore a
  known blind spot, reported but not gated.

PREREQUISITE vs DEPENDENCY output class: I agree, under one condition. `PREREQUISITE` (exit 0) is
allowed only for a producer declared in the manifest's `non_claim` list with its own verification
evidence. An undeclared producer is a `DEPENDENCY` (exit 1). Whether a declared prerequisite counts
as "separable" remains the judge's call.

## Required controls (the selftest should cover each one with a fixture that fails without it)

1. **Ownership completeness (closes F1).** `git diff --name-only base tip` must be a subset of
   the union of claim `lands` plus an explicit `non_claim` list. Scan each non-claim entry as a
   pseudo-claim Y (for example `FRONTIER` exporting the new row ids). Any unowned changed path
   exits 1. In round 50 this must report `C->FRONTIER`.
2. **Disjoint lands (closes F12, r48, r49).** Shared paths across claims emit
   `SEPARABILITY_OVERLAP` and exit 1, unless the manifest assigns hunk-level ownership. Then the
   counterfactual applies only X's hunks to base, not X.tree's whole file.
3. **Delta scan.** Scan only added lines in base..X.tree for X.lands, not whole files.
4. **Export novelty (closes F4).** Every export regex must match 0 times in the base tree
   (`git grep -P <rx> <base>`), otherwise exit 2.
5. **Export liveness (closes F7).** Every export must match at least once in its own claim's added
   lines, otherwise exit 2.
6. **Export completeness (closes F2).** Derive exports mechanically from Y's added registry
   identifiers (new `| Snnn |` row ids, new headings and anchors). The declared exports must cover
   the derived ones, otherwise exit 2.
7. **Separate references from mentions (closes F3, F5, r48).** Resolve markdown link targets and
   relative paths against X's directory. Classify hits as `reference` (citation fields, `used-by`
   cells, imports, `open()`/`git show` targets, link targets) or `mention` (prose, `verified-at`
   provenance, negations). Mentions are advisory unless the dynamic leg confirms them.
8. **Ledgers are not claim lands.** `corpus/lessons/round-N.md`, `LOG.md`, `SCORECARD.md` and
   README revision paragraphs belong to an integration pseudo-owner that is never scanned as a
   dependent source.
9. **Exit-code discipline (closes F8, F14).** Wrap main so any exception exits 2. Selftest asserts:
   exit 1 if and only if at least one `SEPARABILITY_DEPENDENCY`/`OVERLAP` line is printed; exit 0
   if and only if none.
10. **Dynamic-leg discrimination (closes F9).** Acceptance must fail on the base-only tree and
    pass on base plus X.lands. Otherwise report `ACCEPTANCE_VACUOUS` with exit 2.
11. **Hermeticity (closes F10, F11b).** Create the temp dir outside any work tree. Set
    `GIT_CEILING_DIRECTORIES` and use a scrubbed `HOME`/`GIT_*` environment. Reject argv that
    contains the lane's absolute path or a `..` that escapes the temp dir, with exit 2.
12. **VCS-requiring acceptance (closes F11).** When an acceptance declares `needs_git`,
    materialize a fresh git repo (commit base, then commit X) instead of the git-free dir.
    Otherwise O's jj/git gates can't be checked. A fresh repo is not enough when the acceptance
    reads pinned historical objects: `check-readme-revisions` pins `c42d675`, and an object with
    that hash can't be fabricated. In that case, attach the lane's objects read-only (for example
    a `git clone --shared` of the lane into the temp dir), or emit `COULD_NOT_EVALUATE` and exit 2.
    It must never fold into exit 0 (separable) or exit 1 (dependent).

    Peer cross-check (CriticOperability E6, verified here): base
    `tools/check-readme-revisions.py --selftest` in a git-free dir prints
    `SKIP control: base c42d675 README flagged (r49 defect) (base object unreachable)` and exits 0.
    So the contract's git-free dynamic leg *is* the R3 fail-open environment. Before O lands, the
    leg passes vacuously; after a correct fail-closed O fix, it goes nonzero and Ca would report a
    false `O->*` dependency, which pressures someone to weaken O. Control 10 catches the vacuous
    base pass as `ACCEPTANCE_VACUOUS`. Until control 12 lands, O.acceptance must not include the
    readme-revisions selftest.

    Peer follow-up (CriticOperability, both verified here):
    - **A skipped control is not a pass (tightens control 10).** Exit 0 alone does not count as an
      acceptance pass. Base `check-readme-revisions.py` exits 0 while printing
      `selftest skips: N` (`4ad2683:tools/check-readme-revisions.py:344`). A pass requires exit 0
      *and* `selftest skips: 0` where the tool reports a skip count, otherwise no `^SKIP ` lines.
      Any skip counts as `COULD_NOT_EVALUATE` (exit 2).
    - **Clear inherited `GIT_*` variables.** Run the `clone --shared` counterfactual with every
      inherited `GIT_*` variable removed. I measured this: in a `--shared` clone of the lane,
      `git cat-file -e c42d675` succeeds in a clean environment and fails with rc=128 when
      `GIT_DIR` points elsewhere. The skip from a leaked `GIT_DIR` would then read as a pass.
13. **Manifest, not `claims.json` (closes F14).** `claims.json` has no `tree`/`exports`/`acceptance`
    fields. The round-50 run must target a derived
    `reports/round-50/separability/r50-manifest.json` (tip commit, lands, derived exports). No
    silent defaults (`exports=[]` would make the run vacuous).
14. **Labelled calibration with negatives.** The r49 fixture has 1 labelled positive and 0
    labelled negatives, so an always-dependent tool scores "1/1". Fix it this way:
    - label every ordered pair: C→S dependent (spot-check); S→C dependent (the `used-by` cells
      name the entry, and the addendum's separability text concedes it); C↔Ca overlap (shared
      `revision: 2.6` paragraph); Ca↔S expected separable once controls 7 and 8 apply;
    - add the r48 admitted pair (base `a01405d`, tip `78f77a6`) with **per-direction** labels:
      C→Ca separable (the labelled negative); Ca→C dependent. Ca lands
      `reports/round-48/calib/queue-successor-r48.json`, whose closure gate G1 (`:134`, `:144`
      `landed_path`) requires C's cartography entry to exist at the landing commit. So round 48
      is not a clean negative in both directions, and the earlier "r48 false dependent" row in
      the evidence table is a true positive for Ca→C;
    - report TP/FP/FN/TN counts;
    - add always-dependent and always-separable mutants that must fail the fixture.
15. **Frozen fixture integrity.** Fixture trees must be reachable lane commits (`c42d675`,
    `c6a174d`, `a01405d`, `78f77a6`), each claim's lands must sit inside `git diff --name-only`,
    and the fixture's sha256 is recorded at landing.

## Impacted axes

- **Calibration** (primary): verdicts lack a measured false-positive rate. The r48 false
  dependent and the F2/F3/F7 false separables mean "1/1 detected" overstates discernment.
- **Coverage:** round-50 C's real dependency on frontier rows S048+ is invisible (F1). The r49
  REJECTED-HONEST-STOP pattern can recur and get a green separability result.
- **Operability:** exit 1 is overloaded by tracebacks (F8, F14). The git-free dynamic leg can't
  run O-style gates (F11) and leaks to the enclosing repo if the temp dir sits inside one (F11b).

## Fixable defect vs judge-level tradeoff

- **Fixable inside Ca:** controls 1–15. The smallest set for this round is 1, 2, 3, 4, 5, 9, 13
  and 14. Without 3 and 13, Ca's own `after_required` ("claims.json exits 0") can't be met
  honestly. Without 14, "1/1" has no false-positive side.
- **Tradeoff for the canonical judge:** with control 1 in place, round 50 will report
  `C->FRONTIER`. The judge must decide whether a declared, non-claim, pre-verified prerequisite
  (the source rows) makes C separable, or whether C must land the rows itself. Calling the rows
  "not a claim" does not remove the dependency the r49 spot-check rejected.
- **Residual even after the fixes:** two kinds of semantic dependency leave no lexical trace.
  One is a policy change: Ca edits QUALITY tier rules that C's admission relies on. The other is
  a change of meaning in an id X already cites, such as a correction row superseding a cited row;
  the delta scan misses it. The dynamic leg catches these only through real, non-vacuous
  acceptance argv, and round 50 declares none.
- **Residual: tools that skip silently (raised by CriticOperability).** Some tools skip a check
  without printing a skip count or any `SKIP` line. The "no `^SKIP` lines" fallback lets those
  pass vacuously. Control 10 (the acceptance must fail on the base-only tree) catches this only
  when the silent skip also happens at base. A tool that skips only in the counterfactual still
  slips through. This does not affect round 50, because `check-readme-revisions` prints
  `selftest skips: N`. Durable fix: an acceptance qualifies for the dynamic leg only if it
  reports a skip count (or proves zero skips some other way). Otherwise the verdict is
  `COULD_NOT_EVALUATE`.

## Smallest safe correction

1. Implement controls 1–5, 9 and 13. Freeze r49 plus r48 as labelled fixtures with mutants
   (control 14).
2. Change Ca `after_required` from "run on `reports/round-50/claims.json` exits 0" to "run on
   the derived `r50-manifest.json` reports exactly the judged set (expected: `C->FRONTIER` unless
   the judge accepts declared non-claim prerequisites), with no other pair flagged".
3. Have QUALITY criterion 7 state that separability is decided by ownership, overlap and
   reference findings plus non-vacuous counterfactual acceptance. Lexical mention alone never
   proves dependency or independence.

## Unrun checks

- No `tools/check-claim-separability.py` patch existed to test. Rerun F1–F12 and the r48/r49/r50
  manifests against the executor's patch once it exists.
- I did not inspect the pastoralism entry or the frontier SOURCES rows; neither had landed yet.
  The F1 conclusion is about the declared round-50 shape (`claims.json` `separability_contract`).
- I didn't measure the dynamic leg against O's real gates in a git-backed counterfactual
  (control 12 is a design requirement, not a measured result).
- Tool installs: none.
