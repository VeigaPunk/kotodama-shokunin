# ReviewR50Separability — round-50 declared separability (C, O, Ca)

Seat: ChousaR27R2.ReviewR50Separability-4 (reviewer, leaf). Base `4ad2683` (= `main`).
Method: read-only git plumbing only (`cat-file`, `show`, `ls-tree`, `grep`, `merge-base`, `rev-parse`, `git grep`) and one `/tmp` probe (deleted). No lane writes, no installs. Author-lane advice, not admission.

## Verdicts

| pair | verdict | reason |
|---|---|---|
| C ↔ frontier (non-claim; `corpus/SOURCES.md`, `corpus/lessons/round-50.md`) | **NOT SEPARABLE — r49 defect repeats** | C needs S048+ rows and `used-by` edits it does not land. Either the frontier writes `mined` rows naming C (census cycle) or `queued` rows that C must flip (shared writer of `SOURCES.md`). The manifest omits the frontier, so neither edge is checked. |
| C ↔ O | **CONDITIONAL** — not separable under the declared whole-file path rule; separable on acceptance under a delta-scoped rule | Two base-era literals name each other's paths (C→O `corpus/README.md:18`; O→C `tools/check-readme-revisions.py:2,306`). Neither is in either delta. Live edge: O's default run reads the live `corpus/README.md`. |
| C ↔ Ca | **CONDITIONAL** — separable under full-path matching; flagged under basename matching | `corpus/README.md:207` names `QUALITY.md` by basename only. Criterion 7 will govern C's admission, so C's verdict changes when Ca lands. |
| O ↔ Ca | **Path-disjoint; identifier-coupled; NOT SEPARABLE under the stated dynamic protocol** | No shared file. Shared label `Ca`. A routed residual owned by "r50 Ca" is emitted by O's file. O's fail-closed selftest needs a git object that Ca's git-free leg does not provide. |

Ca's own acceptance, "`reports/round-50/claims.json` exits 0", is **unsatisfiable as declared**. `claims.json` has no `schema`, `base`, `tree`, `exports` or `acceptance` keys (0 matches; it has `baseline_commit` at :6), and it is not committed at base (`git cat-file -e 4ad2683:reports/round-50/claims.json` fails). Per the contract it exits 2. Leniently parsed it exits 0 vacuously. With the whole-file path leg it exits 1 on C↔O (H3).

## Q1 — Does C's citation of frontier rows repeat the r49 defect?

**Yes**, in shape and in blind spot.

- **r49 (the defect):** C (hunting entry) cited S rows created in the same commit `c6a174d`. The `c_without_s` leg passed because it tested inline URLs (`reports/round-49/run-validation.py:269-273`, "never gate admission" at :264), not whether S rows were absent.
- **r50 declares the same coupling in prose:** `reports/round-50/claims.json:10` ("C's entry cites SOURCES rows opened by the frontier step (not a claim)"). C's `lands` omit `corpus/SOURCES.md` (:18). C's `after_required` (:17) requires every cited S-id to resolve to a row whose `used-by` names the entry. Base `SOURCES.md` ends at S047 (:76). `used-by` is changed in place (`corpus/SOURCES.md:10`).
- **The only executable check named for C** (`sweep.py rows 226 files 226 …`, :17) has zero references to `SOURCES.md` (`git grep -c` = 0). It cannot fail on an unresolved S-id. A dynamic leg would pass C in base + C.lands, which is the r49 vacuity reproduced.
- **New in r50 — a reverse edge.** `ScoutCensus.md` §7 items 4–5 (:215–221) require mined rows' `used-by` to name the entry and the entry to exist in the same tree. The r49 validator enforces the same check (`run-validation.py:62`). [INFERENCE: r50 validator not written yet.] So frontier→C and C→frontier form a cycle. No existing check verifies citation↔`used-by` in either direction (`ScoutCensus.md` F4, :157).
- **Grounding adds a third undeclared path.** The registry requires each row's URL, date and quote in the round lesson's `## Gate` (`corpus/SOURCES.md:7-9`; `run-validation.py:212-221`). `corpus/lessons/round-50.md` does not exist yet.

The label "(not a claim)" removes the edge from the checker's universe; it does not remove the coupling. This corroborates the sibling `CriticFrontier.md` F5 and adds the census reverse edge, the sweep's blindness and the lesson path.

## Q2 — Do O and Ca share any path or identifier?

- **Path:** no shared land. O: `tools/harness/receipt_guard.py`, `tools/check-readme-revisions.py`, `reports/round-50/jj-colocation-probe.py` (`claims.json:37`). Ca: `tools/check-claim-separability.py`, `reports/round-50/separability/r49-fixture.json`, `corpus/QUALITY.md` (:51). Shared directories only: `tools/`, `reports/round-50/`.
- **Identifier — label `Ca`:** `tools/check-readme-revisions.py:2` reads "(round 49, claim Ca)". O lands that file, which was authored by r49's Ca. A label-based scan reads historical Ca as r50 Ca.
- **Identifier — routed residual:** `corpus/lessons/round-49.md:160` and `:206` route the REVISION-ORPHAN residual to `next_touch: r49 close / r50 Ca`. O's gate emits that warning. The lines it names (README 90–101) are C's bytes. Neither Ca's lands (:51) nor `non_goals` (:60) disposition it.
- **Historical overlap:** `c6a174d` (r49) touched `tools/check-readme-revisions.py` and `corpus/README.md`, plus SOURCES, QUALITY, the hunting entry and `round-49.md`. A frozen r49 fixture that lists those lands shares paths with O and C.
- **Object dependency:** O's pinned `BASE_COMMIT` `c42d675` (`check-readme-revisions.py:67`) is reachable from base (`merge-base --is-ancestor` = yes). It is needed by O's selftest and absent from a git-free tree (H4).

## Findings

Axis tags: coverage / operability / calibration.

### High

**H1 (coverage, calibration) — C is not separable from the frontier.** See Q1. Smallest fix: move `corpus/SOURCES.md` rows, `used-by`/status flips and the `corpus/lessons/round-50.md` `## Gate` lines into C.lands. Add an S-resolution acceptance (every `\bS\d{3}\b` cited in the entry maps to a row whose `used-by` names the entry and a `## Gate` bullet). Red = base + C.lands; green = with the rows. Alternatively drop "citing SOURCES rows opened this round" and keep inline URLs, as r49 did. A "not a claim" unit with C→F edges is inseparable by construction.

**H2 (calibration) — Ca's acceptance on `claims.json` is unsatisfiable or vacuous.** `claims.json` lacks the contract's keys and is untracked at base. Fix: keep `claims.json` as prose. Derive `reports/round-50/separability/r50-manifest.json` with pinned claim trees, mechanically derived exports and acceptance argv. Pin "`claims.json` input → exit 2" in the fixture.

**H3 (calibration, operability) — the whole-file path leg flags pre-existing base literals in both directions.**
- C→O: `corpus/README.md:18` names `tools/check-readme-revisions.py`. The "(exit 1)" beside it describes the pre-r49 stub; the live gate exits 0 on base (verified, H4 probe), so it is stale prose that C's README edit would carry.
- O→C: `tools/check-readme-revisions.py:2` and `:306` (control 9's `git show` pin) name `corpus/README.md`. Line :50 names it only by path component (`"corpus", "README.md"`); the sibling critic's `:50` hit needs component-aware matching.

Neither edge is in either delta. Fix: scan only lines a claim adds (`git diff base..X.tree -- <lands>`). Pin `expect_findings: []` for r50 and triage any real hit in the record.

**H4 (operability, calibration) — O's post-fix acceptance cannot run in Ca's git-free dynamic leg, and "git-free" is not guaranteed.**
- Base selftest in a git-free temp copy: exit 0, "selftest skips: 1", "all checks passed". Control 9 (`check-readme-revisions.py:302-311`) SKIPs. That is a vacuous green. O's fail-closed fix (`claims.json:34`; `JjAuditKotodama.md:57, :129`) turns it into a failure, so O cannot pass a git-free counterfactual.
- Upward discovery leaks: `git -C .ufo rev-parse --show-toplevel` returns the lane root. A temp dir under the lane (the `.scratch` convention, `round-49.md:299`) is silently git-enabled.
- Fix: set `GIT_CEILING_DIRECTORIES` for the dynamic leg. Either run O's selftest in a git-enabled sandbox that declares `c42d675` as an object dependency, or exempt that control explicitly.

**H5 (coverage, operability) — the REVISION-ORPHAN residual has no owner.** It is routed to "r50 Ca" (`round-49.md:206`), emitted by O's file, and located in C's README bytes (lines 90–101). Fix: re-route explicitly (C for the README bytes, O keeps the advisory leg). Record the disposition and a new `next_touch` in `round-50.md`.

### Medium

**M1 (calibration) — C's before-check evidence command misfires.** `grep -rniE '^- topic:.*(pastoral|herd|…)'` returns one line, `writing-media-surface-economy.md:3` (matching "sherd"). PCRE `\b` returns zero. The declared `mode: word` is not what the command does. Fix: `git grep -P -n -i '^- topic:.*\b(pastoral|herd|husbandr|transhuman|livestock)\b'` (expect 0).

**M2 (shared path) — `corpus/lessons/round-50.md` is written by undeclared units.** The frontier's `## Gate` rows (`SOURCES.md:7-9`), Ca's M1 row (`ScribeLesson.md:66`, "captured-by pending") and the residual disposition all write it. If C.lands adds it (H1 fix), C and Ca share it. Fix: one owner, or make the lesson an integrator artifact outside every acceptance.

**M3 (policy coupling) — QUALITY criterion 7 changes C's verdict.** C's entry is judged against the admission bar in `corpus/QUALITY.md`. Base + C.lands is judged under six criteria; the combined tree under seven. Criterion 7's text is not written yet. Basename matching flags `README:207`. Fix: pin full-path matching and scope criterion 7 so it does not change the verdict on entries whose lands do not include Ca.

**M4 (operability) — the manifest is unpinned.** `claims.json` is untracked at base, so tree/commit pins cannot be checked against history. Fix: commit the manifest at the wave base, or pin its sha256 in the fixture.

### Low

**L1 (calibration) — Ca's contract contradicts itself.** `claims.json:10` says Ca verifies on the fixture "not on C or O". `:50` says run on `claims.json`. Keep the fixture-only form; it is the one that cannot be gamed.

## Recommended order (smallest first)

1. H2 + M4: derive the r50 manifest; pin `claims.json` → exit 2.
2. H1: move registry bytes into C.lands; add the S-resolution argv; red/green pair.
3. H3: delta-scope the path leg; pin `expect_findings`.
4. H4: `GIT_CEILING_DIRECTORIES`; declare O's object dependency.
5. H5, M1, M2, M3, L1: re-route, fix the probe, assign owners, scope criterion 7.

## Residual risk and verification gaps

- Not in the lane yet: the Ca checker, the fixture, O's probe, QUALITY criterion 7, C's entry, `round-50.md`, and the r50 census validator. Every C/Ca/O verdict above rests on contract text plus base-byte proxies, not executed results.
- Dynamic legs not run: no argv in `claims.json`; C's entry absent; O's fix not landed. The git-free failure of O's post-fix selftest comes from claim text (`claims.json:34`; `JjAuditKotodama.md:57, :129`), not an executed run.
- The r50 census behaviour is inferred from the r49 validator (`run-validation.py:62`, `:212-221`) and `ScoutCensus.md` §7.
- Not verified: O's R1–R3 correctness (outside separability); any external source.

## Checks run (read-only, /tmp only)

- `git cat-file -t`, `rev-parse`, `log -3`, `merge-base --is-ancestor c42d675`, `ls-tree`, `show`, `show --stat c6a174d`, `grep`, `git grep` (plain, `-P`, `-c`, `-w -o`), `git -C .ufo rev-parse --show-toplevel`, `git cat-file -e` on `claims.json`.
- Temp: a git-free copy of `tools/check-readme-revisions.py` and `corpus/README.md` under `/tmp`; ran `--selftest` (exit 0, skips 1) and the default run (exit 0, findings 0, warnings 1 `REVISION-ORPHAN [90,101]`); the directory was then removed.

Main agent should re-run after the fixes: the r49 fixture red/green (exact `expect_findings`); `claims.json` input → exit 2; `git diff base..X.tree` scoped path leg; the PCRE before-check; the O selftest in a git-enabled sandbox with `c42d675` present.

## Installs

None.
