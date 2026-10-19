# O06 — negative control: a fresh-claim claims.json the gate must NOT flag

- Seat: `O06` | executor | claim `O` | round 47, loop 2 | date 2026-10-19
- Out path: `reports/round-47/op/O06-negative-control.md` (the only write by this seat)
- Mission (`reports/round-47/targets.json`, id `O06`): "a fresh-claim claims.json whose
  `before` is TRUE at its baseline (e.g. r44 O 'no four-class authority' at c9f4eaa);
  show the gate does NOT flag it. Fenced demo."
- Baseline under test: `c9f4eaa` — the `baseline_commit` declared by
  `reports/round-44/claims.json:7` (`c9f4eaa707b6e977ff6e1616463e91f4b8afea5d`).
- Discriminator commit: `6e9a30d` (`6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe`), lane HEAD at this cut.
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root.
- Boundary: no filed byte edited (`reports/round-1..46/**` untouched); no corpus byte staged or
  written; no `run-validation.py` executed; no git-mutating / network / install command. Scratch is
  under `.scratch/o06/`. The two fixture bytes are drafted here for the integrator to file; this
  seat writes only its out path.

## 1. Verdict

**The negative control is FRESH at its own baseline and is not flagged: 3/3 claims, 9/9 clauses,
exit 0.** The result holds under three runners — the seat-local contract evaluator and two
independent implementations:

| runner | vocabulary | baseline `c9f4eaa` | HEAD `6e9a30d` (expected stale) |
|---|---|---|---|
| seat-local reference evaluator (`§6`) | r47 `before_checks` | **3 fresh, 0 stale, exit 0** | O stale (2 clauses), C+Ca fresh, exit 1 |
| r44 scratch prototype (`§7.1-§7.2`) | `freshness_probes` | **3 fresh, 0 stale, exit 0** | O stale (2 premises), C+Ca fresh, exit 2 |
| O08 reference oracle (`§7.3`) | `probe` + kind fields | **3 fresh, 0 stale, exit 0** | O stale (2 clauses), C+Ca fresh, exit 1 |

The HEAD column is the reason this is a control rather than a tautology. Two of claim O's clauses —
the claim-named resolver path is **absent** and the couples-tool family count is **1** — are false at
HEAD because the resolver landed at r44 integration (`tools/harness/basename-couples-resolver.py`,
sha256 `43ce341f…`). A gate that measures the worktree instead of `baseline_commit` will therefore
wrongly flag this control STALE. The control is fresh **only if** the gate evaluates at the baseline,
which is the contract's first requirement (`reports/round-44/review/R01-review.md:245`).

Artefact digests (read from the scratch files at this cut):

| artifact | bytes | sha256 |
|---|---|---|
| canonical fixture `negative-control.claims.json` | 5031 | `38857b08543964cf2fd4a0154412279803043997d86fdcab1b2ce20499d4df1c` |
| prototype-compatible fixture `negative-control.compat.json` | 1528 | `ccb0638a9e9876ab0e9c3e1dd669f64c837194f3288de0667283e59b1a5fc491` |
| oracle-compatible fixture `negative-control.o08.json` | 3064 | `d3c38e95574acfeb0b0fd493d75598fad60587d45fd9d983352e946786732eeb` |
| seat-local reference evaluator `ref-eval.py` | 11256 | `4209154c51958173daedafe30d55645af4613ff9597644bfca67290108659047` |

**Honest scope:** the durable tool `tools/harness/claims-freshness.py` does not exist at this cut
(`git cat-file -e HEAD:tools/harness/claims-freshness.py` → rc 128). "The gate does not flag it" is
proved here against the seat-local contract evaluator, the r44 prototype (`--selftest` 17/19, red),
and O08's independent reference oracle (`.scratch/o08/claims-freshness.py`, sha256
`36104b0cef65b64986ecf9fd74fc359d140a6fda548d5414eacacd39c8245ece`, `--selftest` 15/15, green).
The durable-path verdict is owed by O08/V02; this artifact supplies the fixtures and the expected
result, not the durable run.

## 2. Why this is a negative control, not a passing string

1. **The `before` strings are byte-identical to the filed r44 claims.** A read-only comparison
   (`§5.1`) reports `O: True (419/419)`, `C: True (140/140)`, `Ca: True (169/169)` and
   `baseline_commit match: True c9f4eaa`. No premise was paraphrased to make a probe pass.
2. **The clauses are measured, not pattern-matched out of the prose.** They use six probe kinds:
   `path_absent`, `path_present`, `count_eq`, `sha256_eq`, `capability_present`, and
   `topic_owner_absent`. Both boolean polarities are exercised: `capability_present expect=false`
   (the four-class census is absent) and `topic_owner_absent expect=false` (the lithic topic *is*
   owned).
3. **It discriminates.** Clauses O1/O2 flip at HEAD; a worktree-reading gate cannot pass this
   control. That is the r44 defect class inverted into a test.
4. **It does not depend on the r43 prose.** The anti-theater mutation (`O07`) rewrites r43's literal
   tool names; this control instead asserts existence, family count, digest, capability absence and
   ownership — the same measured properties the anti-theater test requires the gate to use.
5. **It is not a claim that r44 was a good round.** r44 C was later blocked and Ca unprovable; the
   control asserts only that the *declared `before` state* was true at `c9f4eaa`. That is exactly
   what a pre-dispatch freshness gate is asked to check.

## 3. Canonical fixture — `before_checks` (r47 contract)

Fenced byte source for `reports/round-47/calib/negative-control.claims.json` (integrator applies;
this seat does not write under `calib/`). Preserve the final newline; verify sha256
`38857b08…` after extraction.

```json
{
  "round": 44,
  "regimen": "REGIMEN.md",
  "baseline_commit": "c9f4eaa",
  "control": {
    "kind": "negative-control",
    "owner_seat": "O06",
    "round": 47,
    "source_claims": "reports/round-44/claims.json",
    "purpose": "A claims file whose declared `before` clauses are TRUE at its own baseline_commit. The freshness gate must report FRESH and exit 0; it must not flag any claim.",
    "discriminator": "Clauses O1 and O2 are FALSE in the r47 worktree (tools/harness/basename-couples-resolver.py landed at r44 integration). A gate that measures the worktree instead of baseline_commit will wrongly flag this control STALE.",
    "expect_semantics": "`expect` is the asserted measured value of the predicate named by probe_kind. Boolean predicates: true = the predicate holds, false = its negation is the premise. count_eq/sha256_eq: the value itself."
  },
  "claims": [
    {
      "id": "O",
      "axis": "operability",
      "before": "no four-class census authority exists; the r42 six-class extractor is the only tool (223/2730 -> 2556/166/2/5/1), it over-captures blank-line-separated indented prose (couples-reference-extractor.py:64-65 continue), lacks an ambiguous control and an indented-prose control, lists no fallback mappings and names no per-token reason; the r43 O claim to mint this was rejected as fork-risk because the re-scope was missing",
      "before_checks": [
        {
          "clause": "no four-class census authority exists",
          "probe_kind": "path_absent",
          "target": "tools/harness/basename-couples-resolver.py",
          "expect": true,
          "evidence_command": "git cat-file -e c9f4eaa:tools/harness/basename-couples-resolver.py; test $? -ne 0"
        },
        {
          "clause": "the r42 six-class extractor is the only tool",
          "probe_kind": "count_eq",
          "target": "tools/harness/*couples*.py",
          "expect": 1,
          "evidence_command": "git ls-tree -r --name-only c9f4eaa tools/harness/ | grep -c 'couples.*\\.py$'"
        },
        {
          "clause": "the r42 six-class extractor (the witness bytes are the baseline bytes)",
          "probe_kind": "sha256_eq",
          "target": "tools/harness/couples-reference-extractor.py",
          "expect": "d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1",
          "evidence_command": "git show c9f4eaa:tools/harness/couples-reference-extractor.py | sha256sum"
        },
        {
          "clause": "lacks a four-class census",
          "probe_kind": "capability_present",
          "target": "tools/harness/couples-reference-extractor.py::four[ _-]class|four_class",
          "expect": false,
          "evidence_command": "git show c9f4eaa:tools/harness/couples-reference-extractor.py | grep -cE 'four[ _-]class|four_class'  # 0"
        },
        {
          "clause": "223 entries at baseline (the census denominator in 223/2730)",
          "probe_kind": "count_eq",
          "target": "corpus/knowledge/*/*.md",
          "expect": 223,
          "evidence_command": "git ls-tree -r --name-only c9f4eaa corpus/knowledge/ | grep -c '\\.md$'"
        }
      ]
    },
    {
      "id": "C",
      "axis": "coverage",
      "before": "total 223; the r43 lithic claim was blocked because its topic was already owned — the correct coverage move is a fresh, verified-unowned gap",
      "before_checks": [
        {
          "clause": "total 223",
          "probe_kind": "count_eq",
          "target": "corpus/knowledge/*/*.md",
          "expect": 223,
          "evidence_command": "git ls-tree -r --name-only c9f4eaa corpus/knowledge/ | grep -c '\\.md$'"
        },
        {
          "clause": "the r43 lithic claim was blocked because its topic was already owned",
          "probe_kind": "topic_owner_absent",
          "target": "myth-symbol:lithic",
          "expect": false,
          "evidence_command": "git show c9f4eaa:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | head -8 | grep -in 'lithic'  # H1 line 1"
        }
      ]
    },
    {
      "id": "Ca",
      "axis": "calibration",
      "before": "r43 declared O and C on stale premises (a green resolver existed; the lithic slot was owned); no mechanical pre-dispatch freshness check exists — the defect is R01-43-12",
      "before_checks": [
        {
          "clause": "no mechanical pre-dispatch freshness check exists",
          "probe_kind": "path_absent",
          "target": "tools/harness/claims-freshness.py",
          "expect": true,
          "evidence_command": "git cat-file -e c9f4eaa:tools/harness/claims-freshness.py; test $? -ne 0"
        },
        {
          "clause": "a green resolver existed",
          "probe_kind": "path_present",
          "target": "tools/harness/couples-reference-extractor.py",
          "expect": true,
          "evidence_command": "git cat-file -e c9f4eaa:tools/harness/couples-reference-extractor.py; echo $?  # 0; greenness measured separately: --selftest exit 0, 8/8"
        }
      ]
    }
  ]
}
```

## 4. Clause-by-clause result at `c9f4eaa`

All nine clauses hold. "Measured" is the probe's return; "Expect" is the asserted `before` value.

| # | claim | clause | probe kind | target | expect | measured | holds |
|---|---|---|---|---|---|---|---|
| O1 | O | no four-class census authority exists | `path_absent` | `tools/harness/basename-couples-resolver.py` | true | **true** (absent) | yes |
| O2 | O | the r42 six-class extractor is the only tool | `count_eq` | `tools/harness/*couples*.py` | 1 | **1** | yes |
| O3 | O | the r42 six-class extractor bytes are the baseline bytes | `sha256_eq` | `tools/harness/couples-reference-extractor.py` | `d8d23a26…cf1` | **`d8d23a26…cf1`** | yes |
| O4 | O | lacks a four-class census | `capability_present` | `…couples-reference-extractor.py::four[ _-]class\|four_class` | false | **false** (no hit) | yes |
| O5 | O | 223 entries at baseline | `count_eq` | `corpus/knowledge/*/*.md` | 223 | **223** | yes |
| C1 | C | total 223 | `count_eq` | `corpus/knowledge/*/*.md` | 223 | **223** | yes |
| C2 | C | the lithic topic was already owned | `topic_owner_absent` | `myth-symbol:lithic` | false | **false** (3 header hits) | yes |
| Ca1 | Ca | no mechanical pre-dispatch freshness check exists | `path_absent` | `tools/harness/claims-freshness.py` | true | **true** (absent) | yes |
| Ca2 | Ca | a green resolver existed | `path_present` | `tools/harness/couples-reference-extractor.py` | true | **true** (present) | yes |

C2's three hits are `mineral-stone-symbolism.md:1` (H1), `:3` (`- gap filled:`), `:5` (`- topic:`);
the body count is irrelevant to the ownership probe. This is the same reading the r44 prototype
reports (`§7`).

## 5. Raw measurements

### 5.1 Premise fidelity (read-only comparison)

```
$ python3 -B - <<'PY'
import json
src = json.load(open('reports/round-44/claims.json'))
ctl = json.load(open('.scratch/o06/negative-control.claims.json'))
src_by = {c['id']: c['before'] for c in src['claims']}
for c in ctl['claims']:
    print(c['id'], 'before_identical=', c['before'] == src_by[c['id']], 'len=', len(c['before']))
print('baseline_commit match:', ctl['baseline_commit'] == src['baseline_commit'], src['baseline_commit'])
PY
O before_identical= True len= 419
C before_identical= True len= 140
Ca before_identical= True len= 169
baseline_commit match: True c9f4eaa
```

Source lines: `reports/round-44/claims.json:7` (`baseline_commit`), `:27` (O `before`),
`:40` (C `before`), `:52` (Ca `before`).

### 5.2 Probe measurements at the baseline

```
$ git cat-file -e c9f4eaa:tools/harness/basename-couples-resolver.py; echo rc=$?
fatal: path 'tools/harness/basename-couples-resolver.py' exists on disk, but not in 'c9f4eaa'
rc=128
$ git ls-tree -r --name-only c9f4eaa tools/harness/ | grep -c "couples.*\.py$"
1
$ git show c9f4eaa:tools/harness/couples-reference-extractor.py | sha256sum
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1  -
$ git show c9f4eaa:tools/harness/couples-reference-extractor.py | grep -cE "four[ _-]class|four_class"
0
$ git ls-tree -r --name-only c9f4eaa corpus/knowledge/ | grep -c "\.md$"
223
$ git show c9f4eaa:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | head -5 | grep -in lithic | cut -c1-118
1:# Stone, gem and metal symbolism — the lithic register: the lapidary code, material prestige, and the quarry-to-rega
3:- gap filled: the lithic/mineral register is absent from the partition and this entry fills it — the register family
5:- topic: the lithic register of a fictional culture's symbolic grammar — the mineral slot the register family lacks,
$ git cat-file -e c9f4eaa:tools/harness/claims-freshness.py; echo rc=$?
fatal: path 'tools/harness/claims-freshness.py' does not exist in 'c9f4eaa'
rc=128
$ git cat-file -e c9f4eaa:tools/harness/couples-reference-extractor.py; echo rc=$?
rc=0
$ python3 -B .scratch/o06/extractor-at-c9f4eaa.py --selftest | grep -c '^PASS'
8
selftest rc=0
```

"Green resolver" in Ca's `before` is therefore true at baseline as a runtime fact: the extractor
was extracted from `c9f4eaa:tools/harness/couples-reference-extractor.py` and its own selftest exits
0 with 8/8 PASS controls. A static probe can only pin presence; the clause carries `path_present`
and the runtime result is recorded here rather than overclaimed by the gate.

### 5.3 HEAD discriminator

```
$ git cat-file -e 6e9a30d:tools/harness/basename-couples-resolver.py; echo rc=$?
rc=0
$ git ls-tree -r --name-only 6e9a30d tools/harness/ | grep -c "couples.*\.py$"
2
```

So O1 (`path_absent`) and O2 (`count_eq 1`) are false at HEAD while every C/Ca clause remains true.
That asymmetry is the control's teeth.

## 6. Executable demo 1 — canonical `before_checks` schema

Runner: the seat-local reference evaluator in Appendix A (not a deliverable, not a competing gate).
Its only purpose is to measure this fixture independently of the not-yet-assembled durable tool.

```
$ python3 -B .scratch/o06/ref-eval.py --claims .scratch/o06/negative-control.claims.json
baseline: c9f4eaa707b6e977ff6e1616463e91f4b8afea5d
[O] FRESH (5/5 clauses hold)
  ok   path_absent          tools/harness/basename-couples-resolver.py              measured=true       expect=true
  ok   count_eq             tools/harness/*couples*.py                              measured=1          expect=1
  ok   sha256_eq            tools/harness/couples-reference-extractor.py            measured=d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1 expect=d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1
  ok   capability_present   tools/harness/couples-reference-extractor.py::four[ _-] measured=false      expect=false
  ok   count_eq             corpus/knowledge/*/*.md                                 measured=223        expect=223
[C] FRESH (2/2 clauses hold)
  ok   count_eq             corpus/knowledge/*/*.md                                 measured=223        expect=223
  ok   topic_owner_absent   myth-symbol:lithic                                      measured=false      expect=false
[Ca] FRESH (2/2 clauses hold)
  ok   path_absent          tools/harness/claims-freshness.py                       measured=true       expect=true
  ok   path_present        tools/harness/couples-reference-extractor.py            measured=true       expect=true
summary: 3 fresh, 0 stale, 0 could-not-evaluate
VERDICT: FRESH (exit 0)
$ echo $?
0
```

The same fixture at HEAD — **expected not green**, because the `before` belongs to `c9f4eaa`:

```
$ python3 -B .scratch/o06/ref-eval.py --claims .scratch/o06/negative-control.claims.json --at 6e9a30d
baseline: 6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
[O] STALE (3/5 clauses hold)
  FAIL path_absent          tools/harness/basename-couples-resolver.py              measured=false      expect=true
  FAIL count_eq             tools/harness/*couples*.py                              measured=2          expect=1
  ok   sha256_eq            tools/harness/couples-reference-extractor.py            measured=d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1 expect=d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1
  ok   capability_present   tools/harness/couples-reference-extractor.py::four[ _-] measured=false      expect=false
  ok   count_eq             corpus/knowledge/*/*.md                                 measured=223        expect=223
[C] FRESH (2/2 clauses hold)
  ok   count_eq             corpus/knowledge/*/*.md                                 measured=223        expect=223
  ok   topic_owner_absent   myth-symbol:lithic                                      measured=false      expect=false
[Ca] FRESH (2/2 clauses hold)
  ok   path_absent          tools/harness/claims-freshness.py                       measured=true       expect=true
  ok   path_present        tools/harness/couples-reference-extractor.py            measured=true       expect=true
summary: 2 fresh, 1 stale, 0 could-not-evaluate
VERDICT: NOT GREEN (exit 1)
$ echo $?
1
```

The HEAD run is a discriminator, not the control verdict. It is evidence for O11's baseline-eval
check: the same bytes produce opposite verdicts under baseline vs worktree measurement.

## 7. Executable demo 2 — the existing r44 prototype (compat vocabulary)

Because the durable tool is not on disk, two executable gate implementations exist today: the r44
scratch prototype `.scratch/ca01/claims-freshness.py` (34 038 bytes, mtime 2026-10-19 14:23) and
O08's independent reference oracle (`.scratch/o08/claims-freshness.py`, 20 922 bytes, mtime
2026-10-19 15:04, `--selftest` 15/15 green). Neither reads the canonical fixture's r47 vocabulary, so
this section renders the identical premises in each one's own schema. Both are **compatibility
harnesses**, not additional deliverables.

Fenced byte source for `reports/round-47/calib/negative-control.compat.json` (optional; sha256
`ccb0638a…`):

```json
{
  "round": 44,
  "baseline_commit": "c9f4eaa",
  "control": {
    "kind": "negative-control-compat",
    "owner_seat": "O06",
    "note": "Same premises rendered in the r44 scratch prototype's `freshness_probes` vocabulary, so the only existing gate implementation can be run today. The canonical artifact is negative-control.claims.json (`before_checks`)."
  },
  "claims": [
    {
      "id": "O",
      "axis": "operability",
      "freshness_probes": [
        {"kind": "path_absent", "path": "tools/harness/basename-couples-resolver.py"},
        {"kind": "count_eq", "glob": "tools/harness/*couples*.py", "value": 1},
        {"kind": "sha256_eq", "path": "tools/harness/couples-reference-extractor.py", "value": "d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1"},
        {"kind": "grep_absent", "glob": "tools/harness/couples-reference-extractor.py", "regex": "four[ _-]class|four_class"},
        {"kind": "count_eq", "glob": "corpus/knowledge/*/*.md", "value": 223}
      ]
    },
    {
      "id": "C",
      "axis": "coverage",
      "freshness_probes": [
        {"kind": "count_eq", "glob": "corpus/knowledge/*/*.md", "value": 223},
        {"kind": "topic_owned", "partition": "myth-symbol", "topic": "lithic"}
      ]
    },
    {
      "id": "Ca",
      "axis": "calibration",
      "freshness_probes": [
        {"kind": "path_absent", "path": "tools/harness/claims-freshness.py"},
        {"kind": "path_present", "path": "tools/harness/couples-reference-extractor.py"}
      ]
    }
  ]
}
```

Baseline — not flagged:

```
$ python3 -B .scratch/ca01/claims-freshness.py --claims .scratch/o06/negative-control.compat.json
[O] operability -- FRESH (5/5 premises hold)
[C] coverage -- FRESH (2/2 premises hold)
[Ca] calibration -- FRESH (2/2 premises hold)
summary: 3 fresh, 0 stale, 0 unverifiable, 0 ungrounded clause(s)
exit 0
$ echo $?
0
```

HEAD discriminator — the same file is correctly refused:

```
$ python3 -B .scratch/ca01/claims-freshness.py --claims .scratch/o06/negative-control.compat.json --at 6e9a30d
[O] operability -- STALE (3/5 premises hold)
[C] coverage -- FRESH (2/2 premises hold)
[Ca] calibration -- FRESH (2/2 premises hold)
summary: 2 fresh, 1 stale, 0 unverifiable, 0 ungrounded clause(s)
REFUSE: claims O have a `before` already false at 6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe; do not dispatch.
exit 2
$ echo $?
2
```

**Prototype caveats, on the record.** Its own selftest is red — the known r44 defect:

```
$ python3 -B .scratch/ca01/claims-freshness.py --selftest
FAIL  seventeen checks collected (18)
selftest 17/19 FAIL
exit 1
```

and its exit-code contract is **not** the r47 contract: it uses 0 fresh / 1 usage / 2 stale /
3 unverifiable, while r47 requires 0 fresh / 1 stale / 2 malformed (`reports/round-47/claims.json`,
O `after_required`). My compat demo therefore claims only `exit 0` at the baseline; it does not
endorse the prototype's 2/3 codes. The durable tool must implement 0/1/2 (O03/O10).

### 7.3 O08 reference oracle — `probe` + kind-field vocabulary (15/15 green)

O08's oracle is the only green gate implementation on disk. Its schema is
`{"clause", "probe", <kind fields>, "expect", "evidence_command"}`: `expect` is the asserted
boolean condition (default true) and `value` carries the count/digest. The same nine premises in
that schema (fenced byte source for `reports/round-47/calib/negative-control.o08.json`, sha256
`d3c38e95…`):

```json
{
  "round": 44,
  "baseline_commit": "c9f4eaa",
  "control": {
    "kind": "negative-control-o08-rendering",
    "owner_seat": "O06",
    "note": "Identical premises to negative-control.claims.json, rendered in the O08 reference oracle's schema (`probe` + kind-specific fields; `expect` is the asserted condition, default true). Filed only because the r47 contract leaves the JSON key names to O02; see the artifact's integration note."
  },
  "claims": [
    {
      "id": "O",
      "axis": "operability",
      "before": "no four-class census authority exists; the r42 six-class extractor is the only tool (223/2730 -> 2556/166/2/5/1), it over-captures blank-line-separated indented prose (couples-reference-extractor.py:64-65 continue), lacks an ambiguous control and an indented-prose control, lists no fallback mappings and names no per-token reason; the r43 O claim to mint this was rejected as fork-risk because the re-scope was missing",
      "before_checks": [
        {"clause": "no four-class census authority exists", "probe": "path_absent",
         "path": "tools/harness/basename-couples-resolver.py"},
        {"clause": "the r42 six-class extractor is the only tool", "probe": "count_eq",
         "glob": "tools/harness/*couples*.py", "value": 1},
        {"clause": "the r42 six-class extractor (the witness bytes are the baseline bytes)",
         "probe": "sha256_eq", "path": "tools/harness/couples-reference-extractor.py",
         "value": "d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1"},
        {"clause": "lacks a four-class census", "probe": "capability_present",
         "glob": "tools/harness/couples-reference-extractor.py",
         "markers": ["four_class_totals"], "expect": false},
        {"clause": "223 entries at baseline (the census denominator in 223/2730)",
         "probe": "count_eq", "glob": "corpus/knowledge/*/*.md", "value": 223}
      ]
    },
    {
      "id": "C",
      "axis": "coverage",
      "before": "total 223; the r43 lithic claim was blocked because its topic was already owned — the correct coverage move is a fresh, verified-unowned gap",
      "before_checks": [
        {"clause": "total 223", "probe": "count_eq",
         "glob": "corpus/knowledge/*/*.md", "value": 223},
        {"clause": "the r43 lithic claim was blocked because its topic was already owned",
         "probe": "topic_owner_absent", "partition": "myth-symbol",
         "terms": ["lithic"], "expect": false}
      ]
    },
    {
      "id": "Ca",
      "axis": "calibration",
      "before": "r43 declared O and C on stale premises (a green resolver existed; the lithic slot was owned); no mechanical pre-dispatch freshness check exists — the defect is R01-43-12",
      "before_checks": [
        {"clause": "no mechanical pre-dispatch freshness check exists", "probe": "path_absent",
         "path": "tools/harness/claims-freshness.py"},
        {"clause": "a green resolver existed", "probe": "path_present",
         "path": "tools/harness/couples-reference-extractor.py"}
      ]
    }
  ]
}
```

Baseline — not flagged:

```
$ python3 -B .scratch/o08/claims-freshness.py --claims .scratch/o06/negative-control.o08.json | grep -E '^\[|^  - [a-z0-9_]+:|^summary:'
[O] FRESH
  - path_absent: MATCH
  - count_eq: MATCH
  - sha256_eq: MATCH
  - capability_present: MATCH
  - count_eq: MATCH
[C] FRESH
  - count_eq: MATCH
  - topic_owner_absent: MATCH
[Ca] FRESH
  - path_absent: MATCH
  - path_present: MATCH
summary: FRESH (exit 0)
$ echo $?
0
```

HEAD discriminator — expected stale:

```
$ python3 -B .scratch/o08/claims-freshness.py --claims .scratch/o06/negative-control.o08.json --at 6e9a30d | grep -E '^\[|^  - [a-z0-9_]+:|^summary:'
[O] STALE
  - path_absent: MISMATCH
  - count_eq: MISMATCH
  - sha256_eq: MATCH
  - capability_present: MATCH
  - count_eq: MATCH
[C] FRESH
  - count_eq: MATCH
  - topic_owner_absent: MATCH
[Ca] FRESH
  - path_absent: MATCH
  - path_present: MATCH
summary: STALE (exit 1)
$ echo $?
1
```

The oracle reports the same nine measurements as §6, including C2's three owner hits
(`mineral-stone-symbolism.md:1,3,5`). Its `--selftest` is green at 15/15.

## 8. Integration notes (for W01, O02, O03, O08, O10, O11, V02)

1. **File name and owner.** The canonical fixture belongs at
   `reports/round-47/calib/negative-control.claims.json`, applied from §3, sha256
   `38857b08…`. Two compatibility renderings are optional: `negative-control.compat.json`
   (`§7.2`, sha256 `ccb0638a…`) for the r44 prototype, and `negative-control.o08.json` (`§7.3`,
   sha256 `d3c38e95…`) for O08's oracle. All are new records; nothing is edited in place.
2. **Expected durable result.** `[O] FRESH`, `[C] FRESH`, `[Ca] FRESH`; 9/9 clauses; exit 0 —
   whichever lawful rendering the tool reads. Any STALE verdict is a gate defect or a schema
   mismatch, not a stale fixture.
3. **Schema divergence — the one open decision for O02/W01.** The r47 contract fixes the seven
   probe kinds but not the JSON key names, and three lawful shapes are now in play: the canonical
   `{"probe_kind", "target"}`; O08's `{"probe", <kind fields>}`; and the r44 prototype's
   `{"kind", "path"/"glob"}` under `freshness_probes`. All three render the same nine premises and
   all three return FRESH at `c9f4eaa` (canonical: §6; O08: §7.3; prototype: §7.2). The integrator
   must file the rendering the durable tool actually reads and name that one the acceptance
   fixture; filing both is safe (each is independently evaluated and asserts the same state), but
   a fixture the tool cannot parse yields could-not-evaluate, not a pass. If the durable tool
   defines `expect` as "the premise holds, always true" rather than "the asserted measured value",
   then O4 must be re-rendered as `grep_absent … expect=true`; C2 needs an ownership-positive kind
   (not in the closed set) or must be recorded as ungrounded. **Do not silently invert the
   fixture**; record the schema adopted and re-pin the digest.
4. **Target encodings used.** `grep_*`/`capability_present`: `<path>::<regex>`;
   `topic_owner_absent`: `<partition>:<topic>`; `count_eq`: a repo-relative glob with `*` not
   crossing `/`; `sha256_eq`/`path_*`: a repo-relative path. These are proposals to O02; the
   `evidence_command` on every clause reproduces the measurement without the tool.
5. **Exit codes.** 0 fresh / 1 stale-or-could-not-evaluate / 2 malformed. This fixture declares
   checks, so it is FRESH, not could-not-evaluate; the no-checks case is O04/O10's control.
6. **Baseline evaluation (O11).** §6/§7 at HEAD are the ready-made discriminator: a worktree-reading
   gate reports O stale; a baseline-reading gate reports the control fresh. Use them as the O11
   fixture if useful.
7. **Anti-theater (O07).** This control is the complement of O07's mutation: O07 proves the gate
   still flags when literals are renamed; O06 proves it does not flag a true premise measured by
   existence/count/digest/capability/ownership rather than prose.

## 9. What was not encoded, and why

The `before` strings contain narrative clauses a static gate cannot measure. They are listed here
rather than silently dropped:

| claim | clause | disposition |
|---|---|---|
| O | "the r43 O claim to mint this was rejected as fork-risk because the re-scope was missing" | historical/process; verified by `reports/round-43/validation.json` (O `failed-as-declared`) and r44's re-scope, not by a baseline probe |
| O | "it over-captures blank-line-separated indented prose (…:64-65 continue)" | static property of the pinned bytes; subsumed by O3's sha256. Live incidence was 0 (R01 §2.3), and a runtime probe is outside the static vocabulary |
| O | "lacks an ambiguous control and an indented-prose control" / "lists no fallback mappings and names no per-token reason" | static properties of the pinned bytes; O3 pins them by identity and O4 samples the four-class capability |
| O | "223/2730 -> 2556/166/2/5/1" | only the 223 denominator is a static count (O5); 2730 and the class split are the extractor's runtime output, verified in `reports/round-44/review/R01-review.md:46-56`, not re-derived here |
| C | "the correct coverage move is a fresh, verified-unowned gap" | normative, not a state premise |
| Ca | "r43 declared O and C on stale premises" | historical about `7ceff59`; verified by `reports/round-43/validation.json` and `reports/round-43/review/R01-review.md:400` (R01-43-12), not by a `c9f4eaa` probe |

## 10. Limits / to-verify

- **`to-verify`: durable-path verdict.** `tools/harness/claims-freshness.py` is absent at this cut.
  The canonical FRESH result is against the contract-shaped reference evaluator; O08/V02 must
  re-run the fixture against the assembled tool. Until then the durable claim is unproved.
- **`to-verify`: schema adoption.** The `expect`/target encodings in §8 are recommendations. If O02
  adopts a different schema, this fixture must be adapted and its digest re-pinned; the premises
  and the expected verdict do not change.
- **Static vs runtime.** "A green resolver existed" is pinned as presence plus a separately recorded
  8/8 selftest run; the probe vocabulary has no runtime kind. If the durable tool gains one, Ca2
  should be upgraded.
- **Control scope.** This fixture is not evidence that r44 O/C/Ca were well-scoped claims. It
  asserts only that their declared `before` state was true at `c9f4eaa` — precisely the check that
  would have prevented r43's stale dispatch.

## Appendix A — seat-local reference evaluator (evidence harness, not a deliverable)

Fenced byte source of `.scratch/o06/ref-eval.py`, sha256 `4209154c…`. It implements the seven probe
kinds, baseline evaluation via `git ls-tree`/`git show`, the `before_checks` schema, and the 0/1/2
exit contract. It is filed here only so §6 is reproducible after scratch cleanup; the durable tool
supersedes it.

```python
#!/usr/bin/env python3
"""Seat-local reference evaluator for the r47 claims-freshness contract.

NOT a deliverable and NOT a competing gate: the durable tool is authored by
O01-O03 and assembled by the integrator.  This script exists only so the O06
negative-control fixture can be measured independently of that tool, at its
own baseline_commit, before the durable path exists.

Implements the r47 `before_checks` clause schema:

    {clause, probe_kind, target, expect, evidence_command}

Closed probe set: path_absent, path_present, grep_absent, count_eq,
sha256_eq, topic_owner_absent, capability_present.

`expect` is the asserted measured value of the predicate named by the kind.
For boolean kinds, true means the predicate holds and false means its
negation is the premise (e.g. capability_present expect=false asserts the
capability is absent).  count_eq/sha256_eq carry the value itself.

Measurement is against `baseline_commit` via git plumbing, never the
worktree; `--at worktree` is a deliberate override used only by the O06
discriminator demonstration.

Exit: 0 every claim fresh; 1 any stale or could-not-evaluate; 2 malformed.
Read-only; stdlib only.
"""
from __future__ import annotations

import argparse
import hashlib
import json
import pathlib
import re
import subprocess
import sys

sys.dont_write_bytecode = True

KINDS = {
    "path_absent",
    "path_present",
    "grep_absent",
    "count_eq",
    "sha256_eq",
    "topic_owner_absent",
    "capability_present",
}


class Malformed(Exception):
    pass


class Tree:
    def __init__(self, root, commit):
        self.root = pathlib.Path(root).resolve()
        self.commit = commit
        self._files = None
        self._text = {}

    def _git(self, *args, text=True):
        proc = subprocess.run(
            ["git", "-C", str(self.root), *args],
            capture_output=True,
            text=text,
        )
        if proc.returncode != 0:
            err = proc.stderr if text else proc.stderr.decode("utf-8", "replace")
            raise Malformed("git %s failed: %s" % (" ".join(args), err.strip()))
        return proc.stdout

    def files(self):
        if self._files is None:
            if self.commit:
                out = self._git("ls-tree", "-r", "--name-only", self.commit)
                self._files = [line for line in out.splitlines() if line]
            else:
                found = []
                for path in self.root.rglob("*"):
                    if not path.is_file():
                        continue
                    rel = path.relative_to(self.root).as_posix()
                    parts = rel.split("/")
                    if parts[0] in (".git", ".scratch", "__pycache__"):
                        continue
                    if "__pycache__" in parts:
                        continue
                    found.append(rel)
                self._files = sorted(found)
        return self._files

    def exists(self, path):
        return path in set(self.files())

    def read(self, path):
        if path not in self._text:
            if self.commit:
                self._text[path] = self._git("show", "%s:%s" % (self.commit, path))
            else:
                self._text[path] = (self.root / path).read_text(
                    encoding="utf-8", errors="replace"
                )
        return self._text[path]

    def sha256(self, path):
        if self.commit:
            data = self._git("show", "%s:%s" % (self.commit, path), text=False)
        else:
            data = (self.root / path).read_bytes()
        return hashlib.sha256(data).hexdigest()

    def match(self, pattern):
        regex = _glob_regex(pattern)
        return [path for path in self.files() if regex.fullmatch(path)]


def _glob_regex(pattern):
    out = []
    index = 0
    while index < len(pattern):
        char = pattern[index]
        if char == "*":
            if index + 1 < len(pattern) and pattern[index + 1] == "*":
                out.append(".*")
                index += 2
                continue
            out.append("[^/]*")
        elif char == "?":
            out.append("[^/]")
        else:
            out.append(re.escape(char))
        index += 1
    return re.compile("".join(out))


def _topic_hits(tree, partition, topic):
    hits = []
    for path in tree.match("corpus/knowledge/%s/*.md" % partition):
        for number, line in enumerate(tree.read(path).splitlines()[:200], 1):
            field = None
            if number == 1 and line.startswith("# "):
                field = "H1"
            else:
                match = re.match(r"^- (topic|gap filled):", line)
                if match:
                    field = match.group(1)
            if field and re.search(r"\b%s\b" % re.escape(topic), line, re.I):
                hits.append((path, number, field, line.strip()))
    return hits


def evaluate(check, tree):
    kind = check.get("probe_kind") or check.get("kind")
    if kind not in KINDS:
        raise Malformed("unknown probe_kind: %r" % (kind,))
    target = check.get("target") or check.get("path") or check.get("glob")
    if not target:
        raise Malformed("probe %r has no target" % (kind,))
    expect = check.get("expect", check.get("value"))
    if expect is None:
        raise Malformed("probe %r has no expect value" % (kind,))

    if kind in ("path_absent", "path_present"):
        present = tree.exists(target)
        measured = (not present) if kind == "path_absent" else present
        detail = "%s: %s" % (target, "present" if present else "absent")
    elif kind == "count_eq":
        count = len(tree.match(target))
        measured = count
        detail = "%s -> %d" % (target, count)
    elif kind == "sha256_eq":
        measured = tree.sha256(target)
        detail = "sha256 %s" % measured
    elif kind in ("grep_absent", "capability_present"):
        path, sep, regex = target.partition("::")
        if not sep:
            raise Malformed("probe %r target needs <path>::<regex>" % (kind,))
        try:
            pattern = re.compile(regex)
        except re.error as exc:
            raise Malformed("bad regex %r: %s" % (regex, exc))
        found = pattern.search(tree.read(path)) is not None
        measured = (not found) if kind == "grep_absent" else found
        detail = "%s /%s/ -> %s" % (path, regex, "hit" if found else "no hit")
    else:  # topic_owner_absent
        partition, sep, topic = target.partition(":")
        if not sep:
            raise Malformed("probe %r target needs <partition>:<topic>" % (kind,))
        hits = _topic_hits(tree, partition, topic)
        measured = not hits
        detail = "%d owner hit(s) for %s" % (len(hits), topic)
        if hits:
            path, number, field, line = hits[0]
            detail += " [%s:%d %s]" % (path, number, field)

    if kind == "count_eq":
        try:
            expected = int(expect)
        except (TypeError, ValueError):
            raise Malformed("count_eq expect must be an integer: %r" % (expect,))
    elif kind in (
        "path_absent",
        "path_present",
        "grep_absent",
        "capability_present",
        "topic_owner_absent",
    ):
        expected = bool(expect)
    else:
        expected = str(expect)

    return measured, expected, detail, measured == expected


def evaluate_claim(claim, tree):
    checks = claim.get("before_checks")
    if checks is None:
        checks = claim.get("freshness_probes")
    if not checks:
        return {
            "id": claim.get("id"),
            "verdict": "could-not-evaluate",
            "rows": [],
            "detail": "no checks declared",
        }
    rows = []
    for index, check in enumerate(checks):
        measured, expected, detail, ok = evaluate(check, tree)
        rows.append(
            {
                "index": index,
                "clause": check.get("clause", "probe[%d]" % index),
                "kind": check.get("probe_kind") or check.get("kind"),
                "target": check.get("target") or check.get("path") or check.get("glob"),
                "measured": measured,
                "expected": expected,
                "detail": detail,
                "ok": ok,
            }
        )
    verdict = "fresh" if all(row["ok"] for row in rows) else "stale"
    return {
        "id": claim.get("id"),
        "verdict": verdict,
        "rows": rows,
        "detail": "%d/%d clauses hold" % (sum(row["ok"] for row in rows), len(rows)),
    }


def fmt(value):
    if isinstance(value, bool):
        return "true" if value else "false"
    return str(value)


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--claims", required=True)
    parser.add_argument("--root", default=".")
    parser.add_argument("--at", default=None, help="override; 'worktree' for the live tree")
    parser.add_argument("--json", action="store_true")
    args = parser.parse_args(argv)

    try:
        with open(args.claims, "r", encoding="utf-8") as handle:
            data = json.load(handle)
        if not isinstance(data, dict):
            raise Malformed("claims file is not a JSON object")
        claims = data.get("claims")
        if not isinstance(claims, list) or not claims:
            raise Malformed("claims file has no non-empty claims list")
        commit = args.at or data.get("baseline_commit")
        if not commit:
            raise Malformed("no baseline_commit and no --at override")
        tree = Tree(args.root, None if commit == "worktree" else commit)
        tree.files()
        resolved = "worktree" if commit == "worktree" else tree._git(
            "rev-parse", commit
        ).strip()
        report = [evaluate_claim(claim, tree) for claim in claims]
    except (OSError, json.JSONDecodeError, Malformed) as exc:
        print("MALFORMED: %s" % exc, file=sys.stderr)
        return 2

    if args.json:
        print(json.dumps({"baseline": resolved, "claims": report}, indent=1, sort_keys=True))
    else:
        print("baseline: %s" % resolved)
        for claim in report:
            print("[%s] %s (%s)" % (claim["id"], claim["verdict"].upper(), claim["detail"]))
            for row in claim["rows"]:
                print(
                    "  %-4s %-20s %-55s measured=%-10s expect=%s"
                    % (
                        "ok" if row["ok"] else "FAIL",
                        row["kind"],
                        (row["target"] or "")[:55],
                        fmt(row["measured"]),
                        fmt(row["expected"]),
                    )
                )
        counts = {}
        for claim in report:
            counts[claim["verdict"]] = counts.get(claim["verdict"], 0) + 1
        print(
            "summary: %d fresh, %d stale, %d could-not-evaluate"
            % (
                counts.get("fresh", 0),
                counts.get("stale", 0),
                counts.get("could-not-evaluate", 0),
            )
        )

    verdicts = {claim["verdict"] for claim in report}
    if verdicts == {"fresh"}:
        print("VERDICT: FRESH (exit 0)")
        return 0
    print("VERDICT: NOT GREEN (exit 1)")
    return 1


if __name__ == "__main__":
    sys.exit(main())
```
