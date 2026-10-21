# CriticR50Manifest — round 50 falsify: `reports/round-50/separability/r50-manifest.json` @ `1c779e4`

Seat: KotodamaR50-2.CriticR50Manifest-21 (critic, leaf). Judged on: calibration.
Landed `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`, base `4ad26836552462d28a946ca3b067cab0b5ce3532`.
Method: `git show`/`git diff` of landed bytes, plus a private clone `/tmp/critman-KapO` (`git clone --shared`, checkout `1c779e4`, `GIT_CEILING_DIRECTORIES=/tmp`). The clone was mutated only inside `/tmp` for the counterexamples and deleted afterwards. Lane files, index and jj state were not touched. No installs. Author-lane advice, not admission.

## Verdict: **PARTIAL**

The reported `SEPARABILITY: 0 findings` reproduces byte-for-byte, but it does not show real separability. Two dependencies the build wave predicted were removed by rewording, not by separating the claims:

1. **The C→lesson dependency is real and hidden by wording (BROKEN).** C's landed bytes name the round lesson only in a corpus-relative form (`SOURCES.md:8`) or in prose (entry line 9). The checker matches only exact full paths, so it misses both. Naming the lesson by its full path, or adding the registry's own Gate rule to C's acceptance, each yields `C->REC`.
2. **The selftest literals were renamed from `S048` to `S998` (a false positive suppressed, not disclosed).** The build-patch checker bytes yield one finding on this manifest; the landed bytes yield zero. The finding was spurious (a synthetic selftest literal, not a real citation), so the rename is not a hidden dependency. But it was never recorded, and it shows that C's export regex is purely lexical and wider than C's rows.

O holds. Ca's own unit holds apart from the rename. Folding `corpus/SOURCES.md` into C is honest on substance, but it disagrees with `claims.json`.

## Reproduction

```
$ python3 -B tools/check-claim-separability.py reports/round-50/separability/r50-manifest.json --lane .
SEPARABILITY: 0 findings
SEPARABILITY_NOTE units=4 ordered_pairs=12 acceptance_runs=3      EXIT=0
```

This matches the live receipt `reports/round-50/validation.json` (`claims.Ca.acceptance.after.r50_manifest_rc.actual = 0`, tail `SEPARABILITY: 0 findings`).

## Findings

### F1 (calibration, coverage) — C depends on the REC lesson; the zero comes from wording — **BROKEN**

- **The landed dependency.** The registry contract states that every row's URL, date and verbatim quote live in the round lesson's `## Gate`. C lands that contract line at `corpus/SOURCES.md:8`: `` (`lessons/round-49.md` for S001–S047, `lessons/round-50.md` for S048–S069) holds each row's URL, access date and verbatim quote ``. The Gate bullets themselves are `corpus/lessons/round-50.md:33-54` (22 bullets, S048–S069), which the manifest files under REC (`r50-manifest.json:61`).
- **The entry asserts it too, in prose.** Entry `pastoralism-animal-husbandry.md:9` reads "…each with URL, access date 2026-10-21, tier scope and the round lesson's located quote." The entry contains no lesson path (`rg lessons/round-50` → 0 hits).
- **The rewording was foreseen.** `.ufo/waves/round-50/build/ExecSepFixture.md:79-81`: "entry line 7 names the full `corpus/lessons/round-50.md` → would fire `C->REC` at landing; the r49 precedent (SOURCES line 8) uses the bare form … which stays clean. Bare form, or accept the finding." The same file at `:86-87`: "bare `lessons/round-50.md` does NOT match land `corpus/lessons/round-50.md`". Landed entry line 7 now reads "…each row carrying its URL, access date, tier scope and anchor", with no path. The "bare form" route was taken.
- **The build reviewers said to fold the lesson into C.** `ReviewEntryContract.md:245` (D3): "If the entry cites the lesson's `## Gate`, add `corpus/lessons/round-50.md` too." `ReviewSourcesContract.md:205` (M1) said to fold SOURCES, the lesson and the lessons-index row. `CriticMeasurement.md:48` said the same. The integrator folded only `SOURCES.md`.
- **Not disclosed.** `corpus/lessons/round-50.md` R50-M3 (`:70`) says only that the manifest lists `corpus/SOURCES.md` among C's lands. Searching the lesson, runner and QUALITY for bare/REC/exempt/instrument wording turns up nothing on this point.

**Counterexample V1** (clone only; `SOURCES.md:8` names the lesson by its repo path, nothing else changed):
```
SEPARABILITY_DEPENDENCY C->REC via land path 'corpus/lessons/round-50.md' named at corpus/SOURCES.md:8
SEPARABILITY: 1 findings      EXIT=1
```

**Counterexample V2** (unchanged bytes; C's acceptance adds the SOURCES contract's own check that S048–S069 each have a `- S0nn — ` Gate bullet in `corpus/lessons/round-50.md`):
```
SEPARABILITY_DEPENDENCY C->REC via acceptance [...] fails on base+C.lands (rc=1) and passes on base+C.lands+REC.lands
SEPARABILITY: 1 findings      EXIT=1      acceptance_runs=6
```

C's declared acceptance (`r50-manifest.json:16-21`) checks only README sweep plus "S-id resolves to a SOURCES row whose used-by names the entry". It omits the Gate requirement that the r49 validator enforced (`reports/round-49/run-validation.py:212-221`, cited at `ReviewR50Separability.md` H1). That omission is why the dynamic leg is green.

**Checker blind spot.** The path leg has no resolution of relative links against the citing file's directory (corpus/SOURCES.md → `lessons/round-50.md` = `corpus/lessons/round-50.md`), and no prose detection. Under the checker's own controls, a claim citing a record is a finding (`tools/check-claim-separability.py:1012-1027`). So the zero relies on one specific spelling of the path.

**Smallest safe fix:** do one of the following, and record it either way:
- (a) move `corpus/lessons/round-50.md` into C's lands, as D3 and M1 recommended; or
- (b) keep it in REC, add V2's Gate check to C's acceptance, and accept and record `C->REC` as an ordered, disclosed dependency (expected finding 1, not 0).

Separately, the path leg should resolve `` `relative/path` `` mentions against the citing land's directory.

### F2 (calibration) — `S048`→`S998` selftest rename turned 1 finding into 0; undisclosed — **PARTIAL (benign rename, honesty gap)**

- The only diff between the build-wave patch (`.ufo/waves/round-50/patches/ExecSepTool.patch`, applied alone in a scratch repo) and the landed checker is eight literal swaps `S048`→`S998`, at `tools/check-claim-separability.py:838,865,874,936,953,1006,1056` (and the patch's corresponding lines).
- Running the build-patch checker bytes on this manifest at `1c779e4` gives:
  ```
  SEPARABILITY_DEPENDENCY Ca->C via export '\\bS0(4[89]|[5-9]\\d)\\b' matched tools/check-claim-separability.py:838
  SEPARABILITY: 1 findings      EXIT=1
  ```
- The finding is a false positive. The literal is a synthetic selftest row, and the selftest range is `s_range = r"\bS0(3[1-9]|4[0-3])\b"` (`:778`), so `S998` still sits "outside the exported range". The control's meaning is unchanged.
- The rename was foreseen: `ExecSepFixture.md:82-84` ("Anything citing 'S048–S069' as tokens in Ca/O/REC bytes will fire `->C`").
- It is recorded nowhere: no hit for S998 or the rename in `corpus/lessons/round-50.md`, `reports/round-50/`, or the build reports.
- Calibration impact: the export is purely lexical, and C's export `\bS0(4[89]|[5-9]\d)\b` (`r50-manifest.json:14`) also claims S070–S099, which C never lands. The zero partly depends on editing the instrument's bytes until the tool stays quiet.

**Smallest fix:** narrow C's export to its real rows, `\bS0(4[89]|5\d|6\d)\b`. Record the rename and the triaged false positive in the lesson's Mistakes or Frontier section. Better still, keep `S048` and record `Ca->C (spurious, synthetic literal)` as an expected and triaged finding.

### F3 (calibration) — the manifest re-scopes declared lands relative to `claims.json` — **tradeoff to rule on**

- `claims.json:18`: C lands = entry + `corpus/README.md`; the manifest adds `corpus/SOURCES.md` (`:11`).
- `claims.json:51`: Ca lands omit `r49-expected-independent.txt`; the manifest adds it.
- The SOURCES fold is honest on substance. Rows S048–S069 all have `used-by` = only the entry, and QUALITY criterion 7 (landed by Ca) now states "Sources a claim cites are that claim's lands." However:
  - Ca writes the rule that makes C separable, in the same round.
  - The declared claim and the checked unit differ.
  - `ReviewSourcesContract.md:205` warned "Ca can no longer report the C↔registry coupling. State that in the verdict." Lesson R50-M3 states the fold but not that consequence.
- Ca's `after_required` (`claims.json:50`) says the checker run "on `reports/round-50/claims.json` exits 0". Measured: `SEPARABILITY_INPUT_ERROR manifest is missing base, schema`, EXIT=2. The receipt substitutes `r50-manifest.json` without the claim text being amended.

**Fix:** amend or annotate the `claims.json` lands and `after_required` to match the manifest (or record the substitution as a deviation), and state that the fold removes the C↔registry edge from Ca's view.

### F4 (calibration, operability) — REC declares lands the commit does not land; undeclared new paths exist — **minor**

- `LOG.md`, `SCORECARD.md` and `corpus/lessons/README.md` (`r50-manifest.json:62-64`) are byte-identical to base at `1c779e4` (`git diff --quiet` succeeds for all three). The REC unit declares records that were not written at landing. [INFERENCE: they may come in a later close commit.] The checker accepts lands with zero added lines and never says so.
- New in the commit but in no unit: `reports/round-50/telemetry/{census-before.txt,declaration-freshness.json,jj-probe-v1.txt,jj-probe-v2.txt}` and 89 `.ufo/` files. O's probe names one by a relative path (`reports/round-50/jj-colocation-probe.py:241`, `telemetry/jj-probe-v1.txt`, provenance comment only). Nothing functional depends on them.
- The checker has no completeness check: it never compares the union of lands with `git diff --name-only base..tree`. With `tree: WORKTREE` it cannot, so a path omitted from every unit is invisible to the static leg.
- `validation.json` is correctly absent from the commit and the manifest. It exists only in the live worktree (30003 bytes), as a receipt should.

**Fix:**
- Drop unchanged paths from REC, or have the checker print `SEPARABILITY_NOTE <unit> land <path> adds 0 lines`.
- Add a land-coverage note listing the non-`.ufo` paths changed in the commit that no unit declares.

### F5 — O holds under its stronger stated acceptance — **HOLDS**

- The manifest's O acceptance is selftests only (`:33-37`). In a base + O-lands-only tree I ran:
  - `jj-colocation-probe.py --tools-root .` → `JJ_COLOCATION_FALSE_NEGATIVES=0/3`, `FALSE_POSITIVES=0/4`, EXIT=0;
  - `tools/check-readme-revisions.py` (default run) → `findings 0`, `warnings 1` (the carried `REVISION-ORPHAN`), EXIT=0. The same result holds on the landed tree, where the orphan shifts from lines [90,101] to [101,112] because C's rev-2.7 paragraph was inserted above it.
- O does not need C's bytes.

### F6 — r49 fixture still red — **HOLDS (for this question)**

`check-claim-separability.py reports/round-50/separability/r49-fixture.json` → 6 findings including `C->S via export … hunting-foraging-subsistence.md:18`, EXIT=1. The fixture's fidelity belongs to the fixture reviewers' seat and was not re-judged here.

## Is "0 findings" real separability?

No, not as stated. O is separable, and Ca stands as its own unit. C is separable from the SOURCES rows only because the manifest declares them as C's own lands, and C still depends on the REC lesson's Gate. That dependency is hidden by the corpus-relative path at `SOURCES.md:8`, by the path removed from the entry, and by a C acceptance that omits the Gate rule. An honest manifest reports either 1 finding (`C->REC`, ordered and disclosed) or 0 with the lesson folded into C. Either way, the `S048`→`S998` rename belongs in the record.

## Impacted axes

calibration (primary: the instrument's zero is wording-sensitive), coverage (C's acceptance is weaker than the SOURCES contract), operability (land coverage is unchecked).

## Commands run

- `git diff --stat`, `git show <L>:<path>`, `git diff --quiet 4ad2683 HEAD -- <path>` (lane read-only, then in the clone)
- the checker on the r50 manifest, the r49 fixture and `claims.json` (clone)
- the build-patch checker on the r50 manifest (clone; restored with clone-local `git checkout`)
- V1 (`SOURCES.md:8` with full path) and V2 (Gate acceptance manifest in `/tmp`) (clone)
- in a base + O-only clone: the probe and the readme-revisions default run
- a read-only `json.load` of the live `reports/round-50/validation.json`

Temp dirs `/tmp/critman-KapO` were deleted.

## Installs

None.
