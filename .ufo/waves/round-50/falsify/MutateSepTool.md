# Round 50 falsify — claim-separability mutation probe
**Item attacked:** claim Ca, `tools/check-claim-separability.py`, landed commit `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`.
**Verdict: HOLDS within this bounded mutation set.** All **11/11** one-point mutants were killed by the landed `--selftest`; no combined-detector survivor and no inconclusive baseline. The r49 fixture alone has **PARTIAL** sensitivity: **5/11** kills using the landed receipt’s independent-prediction comparator, versus **1/11** if checked only for exit 1 and any C→S dependency. This is a fixture-coverage finding, not a demonstrated defect in pristine checker behavior. No production changes are proposed or made.
**Axes:** mutation sensitivity; detector specificity; exact-byte restoration; bounded resource use.
## Scope and provenance
- Read the entire 1,230-line landed checker, not only its added lines. One private shared clone: `/tmp/r50-mutate-sep-pfg6u9vg`, checked out at the exact landed commit. Compared the pristine checker bytes with `git show 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0:tools/check-claim-separability.py`; they were identical.
- Modified only one behavior-bearing line of the scratch checker per mutant. Every mutant started from the original bytes, then was restored before the next mutant. No lane source, index, refs, jj state, sibling files, or validation receipts were mutated. The only persistent write is this report.
- The two detector commands ran concurrently for each stable version of the file; mutations themselves were serialized to prevent cross-contamination. No subagents, background jobs, external services, credentials, or live-process probes.
- Existing tools: Python 3.14.8; git 2.56.0. Tool installs/updates: **none**.
- The attempted landed read of `reports/round-50/validation.json` returned git exit 128 (`fatal: path ... exists on disk, but not in ...`); no working-tree receipt was used. The fixture oracle is grounded in the landed prediction and runner below.
### Landed input SHA-256

| Path | SHA-256 |
|---|---|
| `tools/check-claim-separability.py` | `5764ea27e8bba0c92801e2b95e58c52c349852e64729dfdd434459bd35532cc5` |
| `reports/round-50/separability/r49-fixture.json` | `3a6e39bce756c1777b910e82f20a0f2879679980546378849e2dd620237f0c67` |
| `reports/round-50/separability/r49-expected-independent.txt` | `cab4c75476cb9f7ac19ce0c10f332e9b0d422a0de8737aff353f97a56e0bfa71` |
| `reports/round-50/run-validation.py` | `2b7d4cd74c14711825dbe5d8e810966d3d59ff34fe3d15f74b558834212f1cff` |
| `reports/round-50/claims.json` | `fd3d6346c4f1b0db518fafece5acb96601460683d675114f11c22b7b57af599b` |

## Bounded detectors and pristine results
Environment for the clone and every detector invocation: `GIT_CEILING_DIRECTORIES=/tmp`. Working directory: the private clone. Outer wall-clock timeout: **45 seconds per detector**. Fixture acceptance timeout: **10 seconds per leg**. No outer timeout occurred.
```sh
git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/r50-mutate-sep-pfg6u9vg
git -C /tmp/r50-mutate-sep-pfg6u9vg checkout -q 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0
python3 -B tools/check-claim-separability.py --selftest
python3 -B tools/check-claim-separability.py reports/round-50/separability/r49-fixture.json --lane /tmp/r50-mutate-sep-pfg6u9vg --root /tmp/r50-mutate-sep-pfg6u9vg --timeout 10
```
Expected detectors:
1. **ST:** `--selftest` exits 0 with all 56 controls passing on pristine/restored bytes. A mutant is killed when this success predicate fails.
2. **R49 receipt:** fixture exits 1, names C→S, and its normalized finding set equals the independent prediction. This mirrors `reports/round-50/run-validation.py:387–404, 415–421` and the Ca expectations at `:130–135`; normalization ignores first-hit locations and wording differences, not missing/extra finding identities. Applied the landed normalization logic to the captured outputs; did **not** invoke the full validation runner.
3. **R49 minimum:** fixture exits 1 and names **any** C→S dependency, matching the weaker manifest wording. Reported separately to avoid crediting a kill just because the output changed.
4. **R49 export-specific:** exit 1 and specifically a C→S export finding. This stronger-than-minimum predicate kills 2/11 (M08, M11); it is not substituted for the minimum claim.
Also compared complete fixture stdout/stderr/exit status against pristine: the same five mutants differ as are killed by the receipt oracle.
### Pristine ST

Exit **0**; stderr empty. Actual final line:

```text
selftest: 56/56 checks passed - negative controls (export, inline URL, back-reference, land path, acceptance attribution in git-free and needs_git trees, timeout, direction, record citation, overlap, sorted output, WORKTREE), positive controls (disjoint, self-citation, name boundary, base-existing path, added-lines only, record unit, acceptance on base plus own lands, other units at base bytes, needs_git clone, WORKTREE reads) and malformed or unevaluable input (exit 2)
```
### Pristine r49

Exit **1** (expected dependency detection, not baseline failure). Actual stdout:

```text
SEPARABILITY_DEPENDENCY C->Ca via land path 'tools/check-readme-revisions.py' named at corpus/README.md:18
SEPARABILITY_DEPENDENCY C->S via export '\\bS0(3[1-9]|4[0-7])\\b' matched corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18
SEPARABILITY_DEPENDENCY C->S via land path 'corpus/SOURCES.md' named at corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18
SEPARABILITY_DEPENDENCY S->C via land path 'corpus/knowledge/culture-material/hunting-foraging-subsistence.md' named at corpus/SOURCES.md:60
SEPARABILITY_DEPENDENCY S->Ca via land path 'tools/check-readme-revisions.py' named at corpus/lessons/round-49.md:12
SEPARABILITY_OVERLAP C/Ca corpus/README.md
SEPARABILITY: 6 findings
```
Actual stderr:

```text
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=3
```
The six normalized finding identities exactly match `reports/round-50/separability/r49-expected-independent.txt:1–6`. The fixture’s three acceptance legs all pass independently; its findings here are static/overlap findings.
## Mutation matrix

`K` = killed; `S` = survived that detector. Every mutant is a one-line, syntax-valid change; none was killed by a syntax error or an unrelated baseline failure. `R49` uses the independent-prediction receipt oracle, not merely a nonzero process status.

| Mutant | Landed file:line | Defect | ST result (exit; controls passed) | R49 (exit; findings) | ST | R49 | Minimum |
|---|---|---|---|---|---|---|---|
| M01 | `tools/check-claim-separability.py:488` | Scan whole files instead of added lines | 1; 55/56 | 1; 6 | K | S | S |
| M02 | `tools/check-claim-separability.py:368` | Drop base-absence path qualification | 1; 55/56 | 1; 10 | K | K | S |
| M03 | `tools/check-claim-separability.py:680` | Drop export-novelty validation | 1; 55/56 | 1; 6 | K | S | S |
| M04 | `tools/check-claim-separability.py:621` | Scan only forward pairs, skipping back-references | 1; 51/56 | 1; 5 | K | K | S |
| M05 | `tools/check-claim-separability.py:619` | Treat record units as dependers | 1; 55/56 | 1; 6 | K | S | S |
| M06 | `tools/check-claim-separability.py:1220` | Exit zero on UNEVALUATED | 1; 55/56 | 1; 6 | K | S | S |
| M07 | `tools/check-claim-separability.py:681` | Omit overlap findings | 1; 55/56 | 1; 5 | K | K | S |
| M08 | `tools/check-claim-separability.py:625` | Ignore identifier-export citations | 1; 50/56 | 1; 5 | K | K | S |
| M09 | `tools/check-claim-separability.py:604` | Treat path substrings as whole-path references | 1; 55/56 | 1; 6 | K | S | S |
| M10 | `tools/check-claim-separability.py:650` | Treat failed counterfactual acceptance as passing | 1; 51/56 | 1; 6 | K | S | S |
| M11 | `tools/check-claim-separability.py:721` | Exit zero despite dependency or overlap findings | 1; 41/56 | 0; 6 | K | K | K |

Totals: **ST 11/11 killed**; **R49 receipt 5/11 killed** (M02, M04, M07, M08, M11); **R49 minimum 1/11 killed** (M11); combined ST + R49 **11/11 killed**. **0 inconclusive**. These are mutation scores for this deliberately selected set, not a completeness or probability estimate.
## Exact mutations and observed failure output
The ST excerpts below contain **every `FAIL` line and the final summary** for each mutant; repetitive successful `PASS` lines are omitted. Top-level ST stderr was empty for every mutant. Per-control stderr appears inside the actual failure diagnostic when applicable.

### M01 — Scan whole files instead of added lines

- Point: `tools/check-claim-separability.py:488`. Mutation: `if line not in seen -> if True`.
- Expected ST control(s): `tools/check-claim-separability.py:872–878 (only added lines)`.
- Observed ST exit 1:

```text
FAIL positive: only added lines are scanned: rc=1 want 0; stdout="SEPARABILITY_DEPENDENCY C->S via export '\\\\bS0(3[1-9]|4[0-3])\\\\b' matched corpus/knowledge/c.md:1\nSEPARABILITY: 1 findings\n" stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
selftest: 55/56 checks passed - FAILED
```
- Observed r49: exit 1; stdout and stderr **byte-for-byte identical to the pristine r49 block above**; independent prediction matches; survives both receipt and minimum detectors.

### M02 — Drop base-absence path qualification

- Point: `tools/check-claim-separability.py:368`. Mutation: `return [rel for rel in self.lands if self.base_absent[rel]] -> return list(self.lands)`.
- Expected ST control(s): `tools/check-claim-separability.py:864–870 (base-existing path)`.
- Observed ST exit 1:

```text
FAIL positive: a base-existing path mention is not a dependency: rc=1 want 0; stdout="SEPARABILITY_DEPENDENCY C->S via land path 'corpus/SOURCES.md' named at corpus/knowledge/c.md:1\nSEPARABILITY: 1 findings\n" stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
selftest: 55/56 checks passed - FAILED
```
- Observed r49 exit 1; independent prediction matches: `false`; receipt verdict **KILLED**, minimum verdict **SURVIVED**. Actual stdout:

```text
SEPARABILITY_DEPENDENCY C->Ca via land path 'corpus/README.md' named at corpus/knowledge/culture-material/hunting-foraging-subsistence.md:21
SEPARABILITY_DEPENDENCY C->Ca via land path 'tools/check-readme-revisions.py' named at corpus/README.md:18
SEPARABILITY_DEPENDENCY C->S via export '\\bS0(3[1-9]|4[0-7])\\b' matched corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18
SEPARABILITY_DEPENDENCY C->S via land path 'corpus/SOURCES.md' named at corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18
SEPARABILITY_DEPENDENCY Ca->C via land path 'corpus/README.md' named at tools/check-readme-revisions.py:2
SEPARABILITY_DEPENDENCY S->C via land path 'corpus/README.md' named at corpus/lessons/round-49.md:127
SEPARABILITY_DEPENDENCY S->C via land path 'corpus/knowledge/culture-material/hunting-foraging-subsistence.md' named at corpus/SOURCES.md:60
SEPARABILITY_DEPENDENCY S->Ca via land path 'corpus/README.md' named at corpus/lessons/round-49.md:127
SEPARABILITY_DEPENDENCY S->Ca via land path 'tools/check-readme-revisions.py' named at corpus/lessons/round-49.md:12
SEPARABILITY_OVERLAP C/Ca corpus/README.md
SEPARABILITY: 10 findings
```
Actual stderr:

```text
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=3
```

### M03 — Drop export-novelty validation

- Point: `tools/check-claim-separability.py:680`. Mutation: `_check_novelty(units) -> pass`.
- Expected ST control(s): `tools/check-claim-separability.py:1145–1149 (non-novel export)`.
- Observed ST exit 1:

```text
FAIL malformed: an export matching base bytes of its own lands is not novel: rc=0 want 2; stdout='SEPARABILITY: 0 findings\n' stderr='SEPARABILITY_NOTE units=1 ordered_pairs=0 acceptance_runs=0\n'
selftest: 55/56 checks passed - FAILED
```
- Observed r49: exit 1; stdout and stderr **byte-for-byte identical to the pristine r49 block above**; independent prediction matches; survives both receipt and minimum detectors.

### M04 — Scan only forward pairs, skipping back-references

- Point: `tools/check-claim-separability.py:621`. Mutation: `for y in units -> for y in units[units.index(x) + 1:]`.
- Expected ST control(s): `tools/check-claim-separability.py:943–949, 1005–1010 (back-reference/direction)`.
- Observed ST exit 1:

```text
FAIL negative: a back-reference to a unit's new file is a dependency: rc=0 want 1; stdout='SEPARABILITY: 0 findings\n' stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: dependency direction is ordered (S cites C, C cites nothing): rc=0 want 1; stdout='SEPARABILITY: 0 findings\n' stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: a claim citing a record's export is a finding: rc=0 want 1; stdout='SEPARABILITY: 0 findings\n' stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: a claim naming a record's new path is a finding: rc=0 want 1; stdout='SEPARABILITY: 0 findings\n' stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: findings are printed sorted, then the summary: rc=1 want 1; stdout="SEPARABILITY_DEPENDENCY C->S via export '\\\\bS0(3[1-9]|4[0-3])\\\\b' matched corpus/knowledge/c.md:1\nSEPARABILITY: 1 findings\n" stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
selftest: 51/56 checks passed - FAILED
```
- Observed r49 exit 1; independent prediction matches: `false`; receipt verdict **KILLED**, minimum verdict **SURVIVED**. Actual stdout:

```text
SEPARABILITY_DEPENDENCY C->Ca via land path 'tools/check-readme-revisions.py' named at corpus/README.md:18
SEPARABILITY_DEPENDENCY C->S via export '\\bS0(3[1-9]|4[0-7])\\b' matched corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18
SEPARABILITY_DEPENDENCY C->S via land path 'corpus/SOURCES.md' named at corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18
SEPARABILITY_DEPENDENCY S->Ca via land path 'tools/check-readme-revisions.py' named at corpus/lessons/round-49.md:12
SEPARABILITY_OVERLAP C/Ca corpus/README.md
SEPARABILITY: 5 findings
```
Actual stderr:

```text
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=3
```

### M05 — Treat record units as dependers

- Point: `tools/check-claim-separability.py:619`. Mutation: `if x.role == "record" -> if False`.
- Expected ST control(s): `tools/check-claim-separability.py:880–887 (record is not a depender)`.
- Observed ST exit 1:

```text
FAIL positive: a record unit is never scanned as a depender: rc=1 want 0; stdout="SEPARABILITY_DEPENDENCY R->C via export '\\\\bCQ\\\\b' matched LOG.md:1\nSEPARABILITY_DEPENDENCY R->S via export '\\\\bS0(3[1-9]|4[0-3])\\\\b' matched LOG.md:1\nSEPARABILITY: 2 findings\n" stderr='SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=0\n'
selftest: 55/56 checks passed - FAILED
```
- Observed r49: exit 1; stdout and stderr **byte-for-byte identical to the pristine r49 block above**; independent prediction matches; survives both receipt and minimum detectors.

### M06 — Exit zero on UNEVALUATED

- Point: `tools/check-claim-separability.py:1220`. Mutation: `return EXIT_INPUT -> return EXIT_OK in Unevaluated handler`.
- Expected ST control(s): `tools/check-claim-separability.py:1159–1163 (unusable needs_git root)`.
- Observed ST exit 1:

```text
FAIL malformed: a needs_git leg with an unusable --root is unevaluated: rc=0 want 2; stdout="SEPARABILITY_UNEVALUATED git clone failed (rc=128): fatal: repository '/tmp/claim-separability-selftest-zm6t9gol/not-a-repo' does not exist\n" stderr=''
selftest: 55/56 checks passed - FAILED
```
- Observed r49: exit 1; stdout and stderr **byte-for-byte identical to the pristine r49 block above**; independent prediction matches; survives both receipt and minimum detectors.

### M07 — Omit overlap findings

- Point: `tools/check-claim-separability.py:681`. Mutation: `_overlap_findings(units) + _static_findings(units) -> _static_findings(units)`.
- Expected ST control(s): `tools/check-claim-separability.py:1029–1034 (overlap)`.
- Observed ST exit 1:

```text
FAIL negative: one path landed by two units is an overlap finding: rc=0 want 1; stdout='SEPARABILITY: 0 findings\n' stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
selftest: 55/56 checks passed - FAILED
```
- Observed r49 exit 1; independent prediction matches: `false`; receipt verdict **KILLED**, minimum verdict **SURVIVED**. Actual stdout:

```text
SEPARABILITY_DEPENDENCY C->Ca via land path 'tools/check-readme-revisions.py' named at corpus/README.md:18
SEPARABILITY_DEPENDENCY C->S via export '\\bS0(3[1-9]|4[0-7])\\b' matched corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18
SEPARABILITY_DEPENDENCY C->S via land path 'corpus/SOURCES.md' named at corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18
SEPARABILITY_DEPENDENCY S->C via land path 'corpus/knowledge/culture-material/hunting-foraging-subsistence.md' named at corpus/SOURCES.md:60
SEPARABILITY_DEPENDENCY S->Ca via land path 'tools/check-readme-revisions.py' named at corpus/lessons/round-49.md:12
SEPARABILITY: 5 findings
```
Actual stderr:

```text
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=3
```

### M08 — Ignore identifier-export citations

- Point: `tools/check-claim-separability.py:625`. Mutation: `hit = _first_line_hit(x, pattern.search) -> hit = None`.
- Expected ST control(s): `tools/check-claim-separability.py:926–941, 1005–1018, 1045–1050 (exports)`.
- Observed ST exit 1:

```text
FAIL negative: C cites an identifier S exports (round-49 shape): rc=0 want 1; stdout='SEPARABILITY: 0 findings\n' stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: an inline-URL-only citation of another unit's export is a dependency: rc=0 want 1; stdout='SEPARABILITY: 0 findings\n' stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: dependency direction is ordered (S cites C, C cites nothing): rc=0 want 1; stdout='SEPARABILITY: 0 findings\n' stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: a claim citing a record's export is a finding: rc=0 want 1; stdout='SEPARABILITY: 0 findings\n' stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: findings are printed sorted, then the summary: rc=1 want 1; stdout="SEPARABILITY_DEPENDENCY S->C via land path 'corpus/knowledge/c.md' named at corpus/SOURCES.md:1\nSEPARABILITY: 1 findings\n" stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: a WORKTREE unit's uncommitted bytes are scanned: rc=0 want 1; stdout='SEPARABILITY: 0 findings\n' stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
selftest: 50/56 checks passed - FAILED
```
- Observed r49 exit 1; independent prediction matches: `false`; receipt verdict **KILLED**, minimum verdict **SURVIVED**. Actual stdout:

```text
SEPARABILITY_DEPENDENCY C->Ca via land path 'tools/check-readme-revisions.py' named at corpus/README.md:18
SEPARABILITY_DEPENDENCY C->S via land path 'corpus/SOURCES.md' named at corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18
SEPARABILITY_DEPENDENCY S->C via land path 'corpus/knowledge/culture-material/hunting-foraging-subsistence.md' named at corpus/SOURCES.md:60
SEPARABILITY_DEPENDENCY S->Ca via land path 'tools/check-readme-revisions.py' named at corpus/lessons/round-49.md:12
SEPARABILITY_OVERLAP C/Ca corpus/README.md
SEPARABILITY: 5 findings
```
Actual stderr:

```text
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=3
```

### M09 — Treat path substrings as whole-path references

- Point: `tools/check-claim-separability.py:604`. Mutation: `re.compile(lookbehind + re.escape(rel) + lookahead) -> re.compile(re.escape(rel))`.
- Expected ST control(s): `tools/check-claim-separability.py:850–855 (whole-path boundaries)`.
- Observed ST exit 1:

```text
FAIL positive: a path that only shares a prefix or suffix is not named: rc=1 want 0; stdout="SEPARABILITY_DEPENDENCY C->S via land path 'tools/check.py' named at corpus/knowledge/c.md:1\nSEPARABILITY: 1 findings\n" stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
selftest: 55/56 checks passed - FAILED
```
- Observed r49: exit 1; stdout and stderr **byte-for-byte identical to the pristine r49 block above**; independent prediction matches; survives both receipt and minimum detectors.

### M10 — Treat failed counterfactual acceptance as passing

- Point: `tools/check-claim-separability.py:650`. Mutation: `if passed -> if True`.
- Expected ST control(s): `tools/check-claim-separability.py:959–1003 (acceptance failure/repair/timeout)`.
- Observed ST exit 1:

```text
FAIL negative: acceptance fails only without S's lands: rc=0 want 1; stdout='SEPARABILITY: 0 findings\n' stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=1\n'
FAIL negative: acceptance that no declared unit repairs names <base>: rc=0 want 1; stdout='SEPARABILITY: 0 findings\n' stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=1\n'
FAIL negative: acceptance is attributed to the one unit that repairs it: rc=0 want 1; stdout='SEPARABILITY: 0 findings\n' stderr='SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=1\n'
FAIL negative: an acceptance run that times out is a failure: rc=0 want 1; stdout='SEPARABILITY: 0 findings\n' stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=1\n'
FAIL negative: a needs_git acceptance is attributed inside its clone: rc=0 want 1; stdout='SEPARABILITY: 0 findings\n' stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=1\n'
selftest: 51/56 checks passed - FAILED
```
- Observed r49: exit 1; stdout and stderr **byte-for-byte identical to the pristine r49 block above**; independent prediction matches; survives both receipt and minimum detectors.

### M11 — Exit zero despite dependency or overlap findings

- Point: `tools/check-claim-separability.py:721`. Mutation: `return EXIT_DEPENDENT if lines else EXIT_OK -> return EXIT_OK`.
- Expected ST control(s): `tools/check-claim-separability.py:925–1050 (finding exit status)`.
- Observed ST exit 1:

```text
FAIL negative: C cites an identifier S exports (round-49 shape): rc=0 want 1; stdout="SEPARABILITY_DEPENDENCY C->S via export '\\\\bS0(3[1-9]|4[0-3])\\\\b' matched corpus/knowledge/c.md:1\nSEPARABILITY: 1 findings\n" stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: an inline-URL-only citation of another unit's export is a dependency: rc=0 want 1; stdout="SEPARABILITY_DEPENDENCY C->S via export '\\\\bS0(3[1-9]|4[0-3])\\\\b' matched corpus/knowledge/c.md:1\nSEPARABILITY: 1 findings\n" stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: a back-reference to a unit's new file is a dependency: rc=0 want 1; stdout="SEPARABILITY_DEPENDENCY S->C via land path 'corpus/knowledge/c.md' named at corpus/SOURCES.md:1\nSEPARABILITY: 1 findings\n" stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: C names a land path that S lands, absent at base: rc=0 want 1; stdout="SEPARABILITY_DEPENDENCY C->S via land path 'corpus/SOURCES.md' named at corpus/knowledge/c.md:1\nSEPARABILITY: 1 findings\n" stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: acceptance fails only without S's lands: rc=0 want 1; stdout='SEPARABILITY_DEPENDENCY C->S via acceptance [\'/usr/bin/python3\', \'-c\', "import os, sys; sys.exit(0 if os.path.isfile(\'corpus/SOURCES.md\') else 1)"] fails on base+C.lands (rc=1) and passes on base+C.lands+S.lands\nSEPARABILITY: 1 findings\n' stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=2\n'
FAIL negative: acceptance that no declared unit repairs names <base>: rc=0 want 1; stdout="SEPARABILITY_DEPENDENCY C-><base> via acceptance ['/usr/bin/python3', '-c', 'import sys; sys.exit(3)'] fails on base+C.lands (rc=3) and no declared unit's lands repairs it\nSEPARABILITY: 1 findings\n" stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=2\n'
FAIL negative: acceptance is attributed to the one unit that repairs it: rc=0 want 1; stdout='SEPARABILITY_DEPENDENCY C->T via acceptance [\'/usr/bin/python3\', \'-c\', "import os, sys; sys.exit(0 if os.path.isfile(\'tools/t.txt\') else 1)"] fails on base+C.lands (rc=1) and passes on base+C.lands+T.lands\nSEPARABILITY: 1 findings\n' stderr='SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=3\n'
FAIL negative: an acceptance run that times out is a failure: rc=0 want 1; stdout="SEPARABILITY_DEPENDENCY C-><base> via acceptance ['/usr/bin/python3', '-c', 'import time; time.sleep(30)'] fails on base+C.lands (timeout after 1s) and no declared unit's lands repairs it\nSEPARABILITY: 1 findings\n" stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=2\n'
FAIL negative: a needs_git acceptance is attributed inside its clone: rc=0 want 1; stdout='SEPARABILITY_DEPENDENCY C->S via acceptance [\'/usr/bin/python3\', \'-c\', "import os, sys; sys.exit(0 if os.path.isfile(\'corpus/SOURCES.md\') else 1)"] fails on base+C.lands (rc=1) and passes on base+C.lands+S.lands\nSEPARABILITY: 1 findings\n' stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=2\n'
FAIL negative: dependency direction is ordered (S cites C, C cites nothing): rc=0 want 1; stdout="SEPARABILITY_DEPENDENCY S->C via export '\\\\bCQ\\\\b' matched corpus/SOURCES.md:1\nSEPARABILITY: 1 findings\n" stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: a claim citing a record's export is a finding: rc=0 want 1; stdout="SEPARABILITY_DEPENDENCY C->R via export '\\\\bRLOG-\\\\d+\\\\b' matched corpus/knowledge/c.md:1\nSEPARABILITY: 1 findings\n" stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: a claim naming a record's new path is a finding: rc=0 want 1; stdout="SEPARABILITY_DEPENDENCY C->R via land path 'LOG-round-50.md' named at corpus/knowledge/c.md:1\nSEPARABILITY: 1 findings\n" stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: one path landed by two units is an overlap finding: rc=0 want 1; stdout='SEPARABILITY_OVERLAP C/S corpus/knowledge/c.md\nSEPARABILITY: 1 findings\n' stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: findings are printed sorted, then the summary: rc=0 want 1; stdout="SEPARABILITY_DEPENDENCY C->S via export '\\\\bS0(3[1-9]|4[0-3])\\\\b' matched corpus/knowledge/c.md:1\nSEPARABILITY_DEPENDENCY S->C via land path 'corpus/knowledge/c.md' named at corpus/SOURCES.md:1\nSEPARABILITY: 2 findings\n" stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
FAIL negative: a WORKTREE unit's uncommitted bytes are scanned: rc=0 want 1; stdout="SEPARABILITY_DEPENDENCY C->S via export '\\\\bS0(3[1-9]|4[0-3])\\\\b' matched corpus/knowledge/c.md:1\nSEPARABILITY: 1 findings\n" stderr='SEPARABILITY_NOTE units=2 ordered_pairs=2 acceptance_runs=0\n'
selftest: 41/56 checks passed - FAILED
```
- Observed r49 exit 0; independent prediction matches: `true`; receipt verdict **KILLED**, minimum verdict **KILLED**. Actual stdout:

```text
SEPARABILITY_DEPENDENCY C->Ca via land path 'tools/check-readme-revisions.py' named at corpus/README.md:18
SEPARABILITY_DEPENDENCY C->S via export '\\bS0(3[1-9]|4[0-7])\\b' matched corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18
SEPARABILITY_DEPENDENCY C->S via land path 'corpus/SOURCES.md' named at corpus/knowledge/culture-material/hunting-foraging-subsistence.md:18
SEPARABILITY_DEPENDENCY S->C via land path 'corpus/knowledge/culture-material/hunting-foraging-subsistence.md' named at corpus/SOURCES.md:60
SEPARABILITY_DEPENDENCY S->Ca via land path 'tools/check-readme-revisions.py' named at corpus/lessons/round-49.md:12
SEPARABILITY_OVERLAP C/Ca corpus/README.md
SEPARABILITY: 6 findings
```
Actual stderr:

```text
SEPARABILITY_NOTE units=3 ordered_pairs=6 acceptance_runs=3
```

## Restoration evidence
Original and final checker SHA-256: **`5764ea27e8bba0c92801e2b95e58c52c349852e64729dfdd434459bd35532cc5`**.
After **each** mutation, restored the exact original line, asserted equality of the **entire byte sequence** with the initial landed bytes, and reran **both identical bounded commands**. All 11 restoration cycles returned ST exit 0 with **56/56**, and r49 exit 1 with **6 findings**, matching both the independent prediction and the complete pristine fixture output. There was one pristine pair, 11 mutant pairs, and 11 restored pairs: **46 top-level detector executions**.

| Mutant | Mutated checker SHA-256 | Restored checker SHA-256 | Restored ST / r49 |
|---|---|---|---|
| M01 | `59d831b4de1140ddbf4496dde3ea2060d04003786674cac9f99066c6385c26ca` | `5764ea27e8bba0c92801e2b95e58c52c349852e64729dfdd434459bd35532cc5` | 0 (56/56) / 1 (6 findings; identical) |
| M02 | `ed6a32d70742f8d922196e818f43b9331c6ca3f43d1ee855068961ecc7784fdd` | `5764ea27e8bba0c92801e2b95e58c52c349852e64729dfdd434459bd35532cc5` | 0 (56/56) / 1 (6 findings; identical) |
| M03 | `2e68865fedec4dbbb44584de3a3c3e434817370853cc0783709c0101b0d14634` | `5764ea27e8bba0c92801e2b95e58c52c349852e64729dfdd434459bd35532cc5` | 0 (56/56) / 1 (6 findings; identical) |
| M04 | `743074f47da5e113bef522def2089cbd222e4447677bb2b557b318c17dc272c4` | `5764ea27e8bba0c92801e2b95e58c52c349852e64729dfdd434459bd35532cc5` | 0 (56/56) / 1 (6 findings; identical) |
| M05 | `f2f9fb40879dc248677123d847e01ddec50c3b992c96b8de0ebe26c9a0fb7151` | `5764ea27e8bba0c92801e2b95e58c52c349852e64729dfdd434459bd35532cc5` | 0 (56/56) / 1 (6 findings; identical) |
| M06 | `464752eee88507a39a84b1a1e3ac10015c379522c7386ff43e3f830007f5d8eb` | `5764ea27e8bba0c92801e2b95e58c52c349852e64729dfdd434459bd35532cc5` | 0 (56/56) / 1 (6 findings; identical) |
| M07 | `25f4de3e743be19f1d1015ee1a8c532655842c6caa18466cc4b244e4c693752c` | `5764ea27e8bba0c92801e2b95e58c52c349852e64729dfdd434459bd35532cc5` | 0 (56/56) / 1 (6 findings; identical) |
| M08 | `28d06aa202a2c07029b31125022c2b10da960bbe4cf4fc157a71af76fa2b89d6` | `5764ea27e8bba0c92801e2b95e58c52c349852e64729dfdd434459bd35532cc5` | 0 (56/56) / 1 (6 findings; identical) |
| M09 | `6fd6278562d17e8a1893ce5712d0a8a7f66e5665b1cb7588bdf6479022f2540d` | `5764ea27e8bba0c92801e2b95e58c52c349852e64729dfdd434459bd35532cc5` | 0 (56/56) / 1 (6 findings; identical) |
| M10 | `4bec5ea0efac0829652a360325b6c750166914aa0ebf3b4e564c56c3764c163f` | `5764ea27e8bba0c92801e2b95e58c52c349852e64729dfdd434459bd35532cc5` | 0 (56/56) / 1 (6 findings; identical) |
| M11 | `3e36c4ec269e165df5d7106729f94aee236f456ff12fe8382d49387c90ee7976` | `5764ea27e8bba0c92801e2b95e58c52c349852e64729dfdd434459bd35532cc5` | 0 (56/56) / 1 (6 findings; identical) |

## Calibration finding and smallest author-lane advice
- The **combined** claimed controls held against this probe. No mutant survived ST; no checker fix is established by these experiments. Do not weaken the contract on the basis of fixture survivors.
- Fixture-alone blind spots are concrete: whole-file scanning (M01), missing novelty validation (M03), records treated as dependers (M05), exit-zero UNEVALUATED (M06), path-boundary loss (M09), and swallowed dynamic acceptance failures (M10) all preserve the complete six-finding r49 result. The fixture contains no `record` or `needs_git` unit (`r49-fixture.json:4–54`), and its passing acceptance legs cannot expose M10. The ST controls cited above do expose each defect.
- The weaker “exit 1 naming C→S” check also misses M02/M04/M07/M08. In particular, M08 removes **identifier** detection but still names C→S through the new registry path; counting only an inseparable pair would falsely credit that mutant. Preserve `r49_matches_independent_prediction` and ST as independent requirements; the landed runner already does so (`run-validation.py:130–135, 417–421`).
- Smallest advice: **retain both detectors** and describe the evidence as 11/11 ST kills and 5/11 fixture kills, rather than treating the historical fixture as a substitute for the 56-control suite. No production code, fixture, or acceptance criterion was changed here.
- Not exercised: the r50 manifest run, other claims, the full validation runner, source URLs, or general correctness beyond these 11 mutants. This report is author-lane evidence, not an admission/integration decision.

**Cleanup:** exact bytes restored first; private clone `/tmp/r50-mutate-sep-pfg6u9vg` then deleted; removal observed `true`. No scratch scripts or clones retained.
