# ScoutCaCount — round 50 falsify: claim Ca counting commands @ `1c779e4`

Seat: `KotodamaR50-2.ScoutCaCount-21` (scout, leaf). Judged on: calibration.
Landed `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`; base `4ad26836552462d28a946ca3b067cab0b5ce3532`.
Method: private clone `/tmp/scoutca-5iiM/repo` (`git clone -q --shared`, checkout `1c779e4`,
`GIT_CEILING_DIRECTORIES=/tmp`), Python 3.14.8. Mutations for counterexamples were made only inside
that `/tmp` clone and restored; lane files, index and jj state were not touched. No installs.
Author-lane advice, not admission.

## Verdict: **PARTIAL**

Split verdict, because the artifact and the claim record disagree:

- **Counting item — HOLDS.** All four commanded measurements reproduce exactly: `--selftest` 56/56
  (exit 0), r49 fixture exit 1 with **six** findings, r50 manifest exit 0, and `grep -ci separab`
  on `corpus/QUALITY.md` 0 at base → 1 at landed.
- **Ca claim record — PARTIAL.** One declared acceptance clause is false as written:
  `reports/round-50/claims.json:50` says "run on `reports/round-50/claims.json` exits 0"; that
  command exits **2** (input error). The wave's own critic caught this
  (`.ufo/waves/round-50/build/CriticMeasurement.md:28-32`, and its Ca7 at `:242` says "Never run on
  raw `claims.json` (contract rc=2)"), and the receipt measures
  `reports/round-50/separability/r50-manifest.json` instead, but the correction is not carried in
  the landed lesson's Mistakes table (R50-M2/M3 at `corpus/lessons/round-50.md:69-70` cover other
  declaration defects). The checker is not vacuous (plants fire), so the zero itself is real
  under the tool's declared semantics.

## Measurements, verbatim

### 1. `--selftest`

```
$ python3 tools/check-claim-separability.py --selftest
PASS positive: disjoint units are separable
PASS positive: self-citation and empty exports are not dependencies
PASS positive: a path that only shares a prefix or suffix is not named
PASS positive: citations already in base are not claim bytes
PASS positive: a base-existing path mention is not a dependency
PASS positive: only added lines are scanned
PASS positive: a record unit is never scanned as a depender
PASS positive: acceptance passes on base plus the unit's own lands
PASS positive: the counterfactual leaves other units at base bytes
PASS positive: a needs_git acceptance runs in a clone checked out at base
PASS positive: a WORKTREE unit reads its lands from --root
PASS negative: C cites an identifier S exports (round-49 shape)
PASS negative: an inline-URL-only citation of another unit's export is a dependency
PASS negative: a back-reference to a unit's new file is a dependency
PASS negative: C names a land path that S lands, absent at base
PASS negative: acceptance fails only without S's lands
PASS negative: acceptance that no declared unit repairs names <base>
PASS negative: acceptance is attributed to the one unit that repairs it
PASS negative: an acceptance run that times out is a failure
PASS negative: a needs_git acceptance is attributed inside its clone
PASS negative: dependency direction is ordered (S cites C, C cites nothing)
PASS negative: a claim citing a record's export is a finding
PASS negative: a claim naming a record's new path is a finding
PASS negative: one path landed by two units is an overlap finding
PASS negative: findings are printed sorted, then the summary
PASS negative: a WORKTREE unit's uncommitted bytes are scanned
PASS malformed: not JSON
PASS malformed: duplicate JSON key
PASS malformed: manifest without schema
PASS malformed: wrong schema
PASS malformed: misspelled unit key is refused, not skipped
PASS malformed: unknown top-level key
PASS malformed: base does not name a commit
PASS malformed: unit tree is a blob
PASS malformed: unit key missing
PASS malformed: empty lands
PASS malformed: land path absent at its tree
PASS malformed: absolute land path
PASS malformed: non-canonical land path
PASS malformed: land path names .git metadata
PASS malformed: lands nest across units
PASS malformed: unknown role
PASS malformed: record carries acceptance
PASS malformed: needs_git without acceptance
PASS malformed: export is not a regex
PASS malformed: export matches the empty string
PASS malformed: empty export string
PASS malformed: empty acceptance argv
PASS malformed: acceptance program cannot start
PASS malformed: unit id declared twice
PASS malformed: no units
PASS malformed: an export matching base bytes of its own lands is not novel
PASS malformed: a WORKTREE land absent from --root is refused
PASS malformed: a needs_git leg with an unusable --root is unevaluated
PASS malformed: lane is not a git repository
PASS malformed: manifest file absent
selftest: 56/56 checks passed - negative controls (export, inline URL, back-reference, land path, acceptance attribution in git-free and needs_git trees, timeout, direction, record citation, overlap, sorted output, WORKTREE), positive controls (disjoint, self-citation, name boundary, base-existing path, added-lines only, record unit, acceptance on base plus own lands, other units at base bytes, needs_git clone, WORKTREE reads) and malformed or unevaluable input (exit 2)
EXIT=0
```

### 2. Frozen r49 fixture

```
$ python3 tools/check-claim-separability.py reports/round-50/separability/r49-fixture.json
SEPARABILITY_DEPENDENCY C->Ca via land path 'tools/check-readme-revisions.py' named at corpus/README.md:18
SEPARABILITY_DEPENDENCY C->S via export '\\bS0(3[1-9]|4[0-7])\\b' matched corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18
SEPARABILITY_DEPENDENCY C->S via land path 'corpus/SOURCES.md' named at corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18
SEPARABILITY_DEPENDENCY S->C via land path 'corpus/knowledge/culture-material/hunting-foraging-subsistence.md' named at corpus/SOURCES.md:60
SEPARABILITY_DEPENDENCY S->Ca via land path 'tools/check-readme-revisions.py' named at corpus/lessons/round-49.md:12
SEPARABILITY_OVERLAP C/Ca corpus/README.md
SEPARABILITY: 6 findings
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=3
EXIT=1
```

Five dependency lines plus one overlap = six. The C→S export leg (the r49 REJECTED-HONEST-STOP
shape) is detected.

### 3. r50 manifest

```
$ python3 tools/check-claim-separability.py reports/round-50/separability/r50-manifest.json
SEPARABILITY: 0 findings
SEPARABILITY_NOTE units=4 ordered_pairs=12 acceptance_runs=3
EXIT=0
```

`acceptance_runs=3` and ~6.6 s wall time show the three acceptance legs actually ran (C and Ca in
a git-free base copy, O in a `git clone --shared` at base), not that they were skipped.

### 4. QUALITY.md separability count

```
$ git show 4ad2683:corpus/QUALITY.md > /tmp/.../Q-base.md; grep -ci separab /tmp/.../Q-base.md
0
base_rc=1
$ grep -ci separab corpus/QUALITY.md
1
landed_rc=0
```

`corpus/QUALITY.md:31` is criterion 7. The base→landed diff is a pure addition
(`@@ -27,3 +27,5 @@`): criterion 6 at line 29 is untouched. Criterion 7's grounding anchor exists:
`corpus/lessons/round-49-verifier-spotcheck.md:15` is `## Adjudication`.

## What holds

- **Fixture is frozen.** `r49-fixture.json` sha256 `3a6e39bce756c1777b910e82f20a0f2879679980546378849e2dd620237f0c67`;
  its base `c42d675…` and both unit trees (`8c78e6b…`, `d91c632…`) resolve in the landed clone.
  `r49-expected-independent.txt` sha256 `cab4c754…`; manifest sha256 `ab3c7658…`; checker
  `5764ea27…`.
- **The prediction is accurate at its own granularity.** It is not byte-identical to tool output
  (it says `x1`, `x2`, `x12`, `x9` and lists matched ids; the tool prints the first `PATH:LINE`
  per edge, `tools/check-claim-separability.py:607` `_first_line_hit`, `:616` `_static_findings`,
  `:629` `name_paths`). The edge set is 6/6. I checked every count against the pinned trees:
  `tools/check-readme-revisions.py` occurs 9× in `corpus/lessons/round-49.md`;
  `corpus/knowledge/…/hunting-foraging-subsistence.md` occurs 12× in `corpus/SOURCES.md`;
  `corpus/SOURCES.md` occurs 2× in the entry; `tools/check-readme-revisions.py` occurs 1× on
  `corpus/README.md:18`; the export line carries S031–S042 (12 distinct ids). So the prediction
  was not generated by the tool's printer, and it is factually right.
- **Equivalence is edge-level by design.** `reports/round-50/run-validation.py:387-405`
  (`_norm_finding`, `r49_matches`) deliberately normalizes the two spellings and drops location
  and multiplicity; the comment says so. Ca's claim only promises "1/1 detected", which is met.
- **Zero is non-vacuous.** In the clone I planted citations in Ca's added bytes of
  `corpus/QUALITY.md` and re-ran the r50 manifest:
  - `reports/round-50/jj-colocation-probe.py` (O's new land) → `Ca->O via land path … EXIT=1`;
  - `corpus/knowledge/…/pastoralism-animal-husbandry.md` (C's new land) → `Ca->C via land path … EXIT=1`;
  - `tools/check-readme-revisions.py` (exists at base) → 0 findings (correct exemption);
  - restore → `SEPARABILITY: 0 findings`, exit 0, clean `git status`.

## Findings

### F1 (calibration) — Ca's declared command is false; rc 2, not 0 — **PARTIAL**

`reports/round-50/claims.json:50` (Ca `after_required`) ends "…run on
`reports/round-50/claims.json` exits 0…". Measured at landed bytes:

```
$ python3 -B tools/check-claim-separability.py reports/round-50/claims.json
SEPARABILITY_INPUT_ERROR manifest is missing base, schema
EXIT=2
```

`claims.json` has no `schema`/`base`/`claims[].tree`; exit 2 is the tool's correct contract for
that input (`tools/check-claim-separability.py` docstring; selftest control "malformed: manifest
without schema"). The receipt and lesson already point at `r50-manifest.json`
(`reports/round-50/run-validation.py:62` and `corpus/lessons/round-50.md:70`), so the artifact is
measured correctly, but the claim as filed cannot pass as written and the defect is not in the
landed Mistakes table.

**Smallest fix:** amend the clause to
`python3 -B tools/check-claim-separability.py reports/round-50/separability/r50-manifest.json exits 0`;
if the filed declaration is frozen by policy (cf. R50-M2), add an M4 row recording "Ca
after_required named `claims.json`; contract rc=2; measured on `r50-manifest.json`". One sentence,
no artifact change.

### F2 (calibration) — C's export names 30 identifiers C never introduces — **PARTIAL**

`reports/round-50/separability/r50-manifest.json:14` exports `\\bS0(4[89]|[5-9]\\d)\\b`, i.e.
S048–S099. C lands exactly 22 new rows, S048–S069 (SOURCES row count 47 → 69; `diff` of the
preamble+rows adds only S048–S069; `grep -rnoE '\bS0(7|8|9)[0-9]\b'` over `corpus`, `tools` and
`reports` → no hits). The export is therefore not "identifiers C introduces" per the tool's own docstring, and
the over-breadth is live, not theoretical:

```
$ printf '\nplant: S077 row\n' >> corpus/QUALITY.md
$ python3 tools/check-claim-separability.py reports/round-50/separability/r50-manifest.json
SEPARABILITY_DEPENDENCY Ca->C via export '\\bS0(4[89]|[5-9]\\d)\\b' matched corpus/QUALITY.md:33
SEPARABILITY: 1 findings
EXIT=1
```

S077 is not a row C lands, yet the citation is attributed to C. Today the zero is unaffected only
because no landed token matches S070–S099. (Sibling `CriticR50Manifest.md` F2 reaches the same
over-breadth from the `S048`→`S998` rename; this is an independent confirmation via a planted
token.)

**Smallest fix:** `"\\bS0(4[89]|5\\d|6\\d)\\b"` (= S048–S069) in the manifest; rerun → still
`SEPARABILITY: 0 findings`.

### F3 (calibration) — the zero depends on whole-path spelling; C's own `SOURCES.md:8` uses the bare form — **tradeoff, disclosed nowhere in the landed docs**

Measured on the clone, with only Ca's `corpus/QUALITY.md` changed:

```
plant `lessons/round-50.md`          -> SEPARABILITY: 0 findings
plant `corpus/lessons/round-50.md`   -> SEPARABILITY_DEPENDENCY Ca->REC via land path 'corpus/lessons/round-50.md' named at corpus/QUALITY.md:33
                                        SEPARABILITY: 1 findings  EXIT=1
```

C's landed bytes do contain the bare form: `corpus/SOURCES.md:8` now reads "…(`lessons/round-49.md`
for S001–S047, `lessons/round-50.md` for S048–S069) holds each row's URL…", and
`corpus/lessons/round-50.md` is REC's land. The tool's whole-path rule (`_name_re`,
`tools/check-claim-separability.py:602-604`) makes that mention invisible, which is what keeps the
manifest at 0. This is self-consistent with the docstring ("A path is named as a whole path") but
the convention is not stated in QUALITY criterion 7, and `corpus/lessons/round-50.md:61` itself
uses the bare spelling. Sibling `CriticR50Manifest.md` F1 reaches the same dependency by two other
routes (full-path reword, Gate acceptance) and proposes folding the lesson into C or accepting
`C->REC`. My measurement adds: the *spelling* alone flips the verdict, so the zero is not
spelling-independent.

**Smallest fix:** add one sentence to criterion 7 or the tool docstring — "paths are matched
repo-relative; a bare `lessons/x.md` does not name `corpus/lessons/x.md`" — or adopt the sibling's
fold/accept route. Do not leave the convention implicit.

### F4 (record, adjacent — likely another seat's item) — the receipt is not landed

`reports/round-50/validation.json` is absent at `1c779e4` (`git ls-tree -r --name-only
1c779e4:reports/round-50` lists claims.json, jj-colocation-probe.py, run-validation.py,
separability/*, telemetry/* only). In the lane it is untracked
(`git status --porcelain` → `?? reports/round-50/validation.json`) and it is not in REC's lands
(`r50-manifest.json:60-68`). The landed lesson header cites it as "the acceptance receipt"
(`corpus/lessons/round-50.md:3`). Its own `tree`/`base_tree` fields are temp paths
(`/tmp/kr50-landed`, `/tmp/kr50-base`), not commits, so it is not self-pinning either.

The receipt's Ca values do match my independent measurements exactly (`r49_fixture_rc=1`,
`r50_manifest_rc=0`, `quality_separab_lines=1`, `checker_selftest_rc=0`,
`r49_matches_independent_prediction=true`, dependencies = the five pairs + overlap). The numbers
are sound; the record is not in the landed tree.

**Smallest fix:** add `reports/round-50/validation.json` to REC's lands and land it (record lane),
or drop the lesson's citation of it.

## Residual unknowns

- Authorship order of `r49-expected-independent.txt` vs the checker cannot be proven from the
  single squashed landed commit. Evidence it was derived independently of the printer: different
  vocabulary, occurrence counts (`xN`) the tool never emits, and all four counts verified correct
  above. Treated as inference, not proof.
- Whether C→REC should be a finding at all is a criterion-semantics decision (pointer to the
  record's Gate vs verification circularity); this seat reports the spelling sensitivity, not the
  adjudication.

## Cleanup

Clone `/tmp/scoutca-5iiM` and all temp files deleted; no tools installed; the only lane write is
this report.
