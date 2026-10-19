# O05 — r43 regression demonstration: the freshness gate flags O and C STALE, leaves Ca FRESH

- Seat: `O05` | role executor | claim `O` | round 47, loop 2
- Out path: `reports/round-47/op/O05-r43-demo.md` (the only file this seat writes)
- Baseline under test: `7ceff59` (`reports/round-43/claims.json:7`); HEAD at this seat: `6e9a30d`
- Contract: `reports/round-47/claims.json:39` (tool), `:41` (after_required), `:47` (thresholds); K03's normative schema `reports/round-47/scout/K03-gate-spec.md:9,111-148,245-324,432-490`; defect `reports/round-43/review/R01-review.md:400` (R01-43-12)
- Boundary: no filed byte edited, no corpus staging, no git mutation, no `run-validation.py` execution. `reports/round-43/claims.json` is byte-identical before and after (sha256 `9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b`, matching the overlay pin and `git show HEAD:...`); `git status --porcelain -- reports/round-43 corpus tools` → empty.

## 1. Result

The r43 claims file, evaluated at its own `baseline_commit` with the overlay in §3, produces:

| claim | verdict | matching clauses | mismatching clauses |
|---|---|---|---|
| **O** operability | **STALE** | — | durable `couples_census` capability present (both capability clauses) |
| **C** coverage | **STALE** | myth-symbol 26; total 223 | topic `lithic` owned by `mineral-stone-symbolism.md` |
| **Ca** calibration | **FRESH** | disposition artifact absent at baseline | — |

Reference-evaluator exit: **1**, with `REFUSE: stale claim(s) O, C at 7ceff59a0…`. This is the positive regression the r47 O claim requires: *"it flags r43 O and C stale + Ca fresh"* (`reports/round-47/claims.json:41`).

The verdicts independently reproduce R01-43-1 and R01-43-6:

- `reports/round-43/review/R01-review.md:389` — "`claims.json:27` false: `tools/harness/couples-reference-extractor.py` is tracked in `7ceff59`, selftest 8/8, census 223/2730".
- `reports/round-43/review/R01-review.md:394` — "Lithic slot owned (26/223; `mineral-stone-symbolism.md`, sha `c99f44ca…`, r42 C04)".

## 2. Measured baseline facts

Every value below was read from committed bytes at `7ceff59` with `git ls-tree` / `git show`, not from the worktree.

```
$ git ls-tree 7ceff59 tools/harness/couples-reference-extractor.py
100644 blob 1ded489bbb2bb90b3ad883ec0cd052822d870225	tools/harness/couples-reference-extractor.py
$ git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1  -
```

The baseline extractor's own selftest, run read-only from a scratch extraction of the baseline blob:

```
$ git show 7ceff59:tools/harness/couples-reference-extractor.py > .scratch/o05/extractor-7ceff59.py
$ python3 -B .scratch/o05/extractor-7ceff59.py --selftest
PASS wrapped positive 4/4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
PASS wrapped positive heals soft wrap
PASS unwrapped regression
PASS over-capture trap (prose excluded) ['sound-symbolism.md']
PASS phantom negative: absent wrapped targets are visible, not zeroed {'sound-change.md': 'prospective', 'sound-symbolism.md': 'fallback', 'tone-prosody.md': 'prospective', 'writing-systems.md': 'fallback'}
PASS N6 regression guard: single-line capture still yields 0 tokens
PASS N6 regression guard: block read yields 4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
PASS glob fragment classified
exit=0
```

The live wrapped field at the baseline (`corpus/knowledge/linguistics/phonetics-phonology.md:72-77`), parsed by the baseline extractor's `field_refs`:

```
tokens: ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md'] count: 4
wrapped: True
```

The successor path the r43 claim names is genuinely absent at baseline — a literal-path gate would pass the claim:

```
$ git cat-file -e 7ceff59:tools/harness/basename-couples-resolver.py || echo ABSENT
fatal: path 'tools/harness/basename-couples-resolver.py' exists on disk, but not in '7ceff59'
ABSENT
```

Counts and ownership for C:

```
$ git ls-tree -r --name-only 7ceff59 -- corpus/knowledge | grep -c '\.md$'
223
$ git ls-tree -r --name-only 7ceff59 -- corpus/knowledge/myth-symbol | grep -c '\.md$'
26
$ git show 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | sed -n '1p;3p;5p'
# Stone, gem and metal symbolism — the lithic register: the lapidary code, material prestige, and the quarry-to-regalia chain
- gap filled: the lithic/mineral register is absent from the partition and this entry fills it — ...
- topic: the lithic register of a fictional culture's symbolic grammar — ...
$ git show 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | sha256sum
c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f  -
```

Ca's premise is true at baseline and false at HEAD — the fact that makes baseline scoping observable:

```
$ git cat-file -e 7ceff59:reports/round-43/calib/dispositions-r38-r39.json || echo ABSENT
fatal: path 'reports/round-43/calib/dispositions-r38-r39.json' exists on disk, but not in '7ceff59'
ABSENT
$ ls reports/round-43/calib/dispositions-r38-r39.json
reports/round-43/calib/dispositions-r38-r39.json        # present at HEAD 6e9a30d
```

Also important: `reports/round-43/` does not exist at `7ceff59` at all. The gate **cannot** read the claims file with `git show <baseline>:reports/round-43/claims.json`; it must read the worktree claims file as input and use the baseline commit only for measurement (K03 §3.3, `scout/K03-gate-spec.md:109`).

## 3. Demo artifact — the r43 checks overlay

This is the `before_checks` annotation in the form K03 makes normative: an overlay keyed by claim id and pinned to the sha256 of the filed claims file, so no filed byte is copied or edited (K03 §3.4/§7.1). The integrator's file name is `reports/round-47/calib/r43-checks.json`; the byte source is the fence below. It matches K03 §7.1 (`scout/K03-gate-spec.md:438-482`), with the evidence commands filled in.

Schema: `{schema, round, baseline_commit, claims_sha256, checks}`; each check is `{clause, probe_kind, target, expect, evidence_command}`. `target` is a kind-specific object, `expect` is a JSON boolean, and `clause` must be a whitespace-normalized substring of the claim's `before` (K03 §3.5). Kinds used here: `capability_present` (AST facts at the baseline), `count_eq`, `topic_owner_absent`, `path_absent`.

```json
{
  "schema": "kotodama-claims-freshness-checks-v1",
  "round": 43,
  "baseline_commit": "7ceff59",
  "claims_sha256": "9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b",
  "checks": {
    "O": [
      {
        "clause": "no durable instrument implements the r39 basename-couples policy",
        "probe_kind": "capability_present",
        "target": {"capability": "couples_census", "scope": "tools/**.py"},
        "expect": false,
        "evidence_command": "git ls-tree -r -z --name-only 7ceff59 -- tools/"
      },
      {
        "clause": "the only resolver that ever ran (r39 I-C05) lives in ephemeral .scratch",
        "probe_kind": "capability_present",
        "target": {"capability": "couples_census", "scope": "tools/**.py"},
        "expect": false,
        "evidence_command": "git show 7ceff59:tools/harness/couples-reference-extractor.py | grep -n add_argument"
      }
    ],
    "C": [
      {
        "clause": "myth-symbol 26",
        "probe_kind": "count_eq",
        "target": {"glob": "corpus/knowledge/myth-symbol/*.md", "value": 26},
        "expect": true,
        "evidence_command": "git ls-tree -r --name-only 7ceff59 -- corpus/knowledge/myth-symbol | wc -l"
      },
      {
        "clause": "lithic slot named but unbuilt",
        "probe_kind": "topic_owner_absent",
        "target": {"topics": ["lithic"], "partition": "myth-symbol", "fields": ["H1", "topic", "gap filled"]},
        "expect": true,
        "evidence_command": "git grep -n -i lithic 7ceff59 -- 'corpus/knowledge/myth-symbol/*.md'"
      },
      {
        "clause": "total 223",
        "probe_kind": "count_eq",
        "target": {"glob": "corpus/knowledge/*/*.md", "value": 223},
        "expect": true,
        "evidence_command": "git ls-tree -r --name-only 7ceff59 -- corpus/knowledge | wc -l"
      }
    ],
    "Ca": [
      {
        "clause": "have no per-finding disposition on record",
        "probe_kind": "path_absent",
        "target": {"path": "reports/round-43/calib/dispositions-r38-r39.json"},
        "expect": true,
        "evidence_command": "git ls-tree -r --name-only 7ceff59 -- reports/round-43/calib/"
      }
    ]
  }
}
```

Why these probes:

- **O.** `couples_census` is true at `7ceff59` by AST facts: the tracked `tools/harness/couples-reference-extractor.py` parses, defines top-level `main`, `classify`, `resolve_entry`, and registers `--census` and `--selftest` (K03 §5, `scout/K03-gate-spec.md:346`). Both O clauses assert absence/capability absence, so `expect:false` is the declared polarity; the measured `true` contradicts them. The wrapped-field fact is corroborated in §2 but not separately encoded: K03's closed capability registry has no behavioral probe for it, and the verdict does not need it.
- **C.** The two counts are true; the ownership leg is false. `topic_owner_absent` scans `H1`, `- topic:` and `- gap filled:` in `corpus/knowledge/myth-symbol/*.md` and finds the owner at `mineral-stone-symbolism.md:1`, `:3` and `:5`. Counts alone would pass — exactly the defect the ownership leg exists to catch (`reports/round-44/review/R01-review.md:243-247`; K03 §4.4).
- **Ca.** The disposition artifact named by Ca's `after_required` is absent at baseline; the premise is true at the moment the claim was declared.

## 4. Demonstration run at `7ceff59`

```
$ export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
$ python3 -B .scratch/o05/claims-freshness-k03.py \
    --claims reports/round-43/claims.json \
    --checks .scratch/o05/r43-checks.json
```

```
claims-freshness reference evaluator (K03 overlay; r47 O05 demo; NOT the durable tool)
claims:   reports/round-43/claims.json
checks:   .scratch/o05/r43-checks.json
baseline: declared=7ceff59 resolved=7ceff59a0216a8ea21ee43262d9fc72abf770cee (git plumbing, never the worktree)

== claim O ==
  [MISMATCH] no durable instrument implements the r39 basename-couples policy | capability_present expect=False measured=True
             tools/harness/couples-reference-extractor.py: main+classify+resolve_entry, --census+--selftest
  [MISMATCH] the only resolver that ever ran (r39 I-C05) lives in ephemeral .scratch | capability_present expect=False measured=True
             tools/harness/couples-reference-extractor.py: main+classify+resolve_entry, --census+--selftest
  VERDICT: STALE

== claim C ==
  [MATCH] myth-symbol 26 | count_eq expect=True measured=True
             corpus/knowledge/myth-symbol/*.md -> 26 (want eq 26)
  [MISMATCH] lithic slot named but unbuilt | topic_owner_absent expect=True measured=False
             corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:1 (H1) # Stone, gem and metal symbolism — the lithic register: the lapidary code, material prestige, and the quarry-to-regalia ; corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:3 (gap filled) - gap filled: the lithic/mineral register is absent from the partition and this entry fills it — the register family is ; corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:5 (topic) - topic: the lithic register of a fictional culture's symbolic grammar — the mineral slot the register family lacks, and
  [MATCH] total 223 | count_eq expect=True measured=True
             corpus/knowledge/*/*.md -> 223 (want eq 223)
  VERDICT: STALE

== claim Ca ==
  [MATCH] have no per-finding disposition on record | path_absent expect=True measured=True
             reports/round-43/calib/dispositions-r38-r39.json: absent
  VERDICT: FRESH

summary: fresh=1 stale=2 could-not-evaluate=0
exit 1
REFUSE: stale claim(s) O, C at 7ceff59a0216a8ea21ee43262d9fc72abf770cee
```

The reference evaluator is scratch-only and is not a deliverable; it exists because `tools/harness/claims-freshness.py` has not landed at this cut. Its digest is `f35eab201910f42c4184391c24de63a721fed859ad419575599f4ff02412b910` (provenance only). O08/V02 must reproduce this table from the durable path.

## 5. Controls

**5.1 A literal-path gate would pass claim O.** The exact successor path named by the r43 claim's `after_required` is absent at baseline (`git cat-file -e 7ceff59:tools/harness/basename-couples-resolver.py` → absent, §2). The claim is still STALE because `couples_census` measures a structural capability in the tracked harness. The verdict is not produced by the claim's own path name, nor by literal prose matching; the `clause` field is a human binding only (K03 §3.5). O07 owns the mutation test that renames the tool; this seat supplies the baseline datum that a literal-path check is insufficient.

**5.2 The verdict is baseline-scoped, not HEAD-scoped.** Re-running with `--at HEAD` flips Ca to STALE, because the r43 disposition artifact exists now but did not at `7ceff59`:

```
$ python3 -B .scratch/o05/claims-freshness-k03.py --claims reports/round-43/claims.json \
    --checks .scratch/o05/r43-checks.json --at HEAD
baseline: declared=7ceff59 resolved=6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe ...
...
== claim Ca ==
  [MISMATCH] have no per-finding disposition on record | path_absent expect=True measured=False
             reports/round-43/calib/dispositions-r38-r39.json: present
  VERDICT: STALE

summary: fresh=0 stale=3 could-not-evaluate=0
exit 1
```

Under the HEAD override the O capability detail switches to `tools/harness/basename-couples-resolver.py` (sha256 `43ce341f…`) because the r44 successor is tracked now — still a real capability, still STALE. A worktree-reading gate would produce the Ca false positive; the correct baseline evaluation does not. O11 should use this pair as its witness.

**5.3 Malformed and could-not-evaluate are not green.** Synthetic controls against the same evaluator:

```
overlay claims_sha256 mismatch   -> exit 2 (MALFORMED)
unknown probe_kind               -> exit 2 (MALFORMED)
clause not a substring of before -> exit 2 (MALFORMED)
missing expect                   -> exit 2 (MALFORMED)
claim with no overlay entry      -> exit 3 (could-not-evaluate)
claim with before_checks: []     -> exit 3 (could-not-evaluate)
```

This is consistent with `could-not-evaluate != green` (`reports/round-47/claims.json:47`) and K03's exit table (`scout/K03-gate-spec.md:188-199`). Exit-code ownership belongs to O10; this seat only confirms the reference evaluator does not conflate the states.

## 6. Handoff

1. **Integrator:** extract the fenced JSON to `reports/round-47/calib/r43-checks.json`; do not write it under `reports/round-43/` and do not edit `reports/round-43/claims.json`. Then run the durable tool:
   ```
   python3 tools/harness/claims-freshness.py \
     --claims reports/round-43/claims.json \
     --checks reports/round-47/calib/r43-checks.json
   ```
   Expected: `O` STALE (2/2 checks mismatch), `C` STALE (ownership mismatch; both counts match), `Ca` FRESH; summary `fresh=1 stale=2`; exit 1; a REFUSE line naming O and C.
2. **O01–O03 authors:** the overlay follows K03 §3.4–§7.1 exactly: `target` objects, `expect` boolean, `claims_sha256` pin, closed seven-kind vocabulary, `couples_census` AST facts. The `--checks` overlay path is required for this demo because r43 has no in-file `before_checks`; in-file `before_checks` remain the forward form for r48+.
   - **Schema conflict to reconcile:** `reports/round-47/plan/P03-o-plan.md:45-68` proposes a separate `polarity` field plus complementary kinds; K03 §4.1 says the set is closed at seven and encodes polarity in `expect`. This overlay follows K03. If the tool adopts P03's shape, the transform is mechanical (`expect:false` → `polarity:"absent"`), but the tool must accept one schema or the integrator's run is malformed. Flag this in the O scribe's receipt.
3. **O08 and V02:** re-run independently from the durable path and compare clause-for-clause with §4. The `couples_census` measurement must come from AST facts, not from running the baseline tool; the wrapped-field 4/4 is corroboration, not the flag.
4. **O06/O07:** the r44 negative control and the anti-theater mutation remain theirs. This artifact supplies the r43 positive regression and one anti-literal datum (§5.1).
5. **R01-43-12 closure:** this is the check r43 lacked. It does not edit r43 and is not a re-adjudication; it is evidence for the r47 O claim's `after_required`.

## 7. Unresolved / to-verify

- **The durable tool does not exist yet.** All runs in §4–§5 are a K03-conformant reference evaluator, not `tools/harness/claims-freshness.py`. The O claim is not satisfied by this seat alone; O08/V02 must reproduce from the durable path.
- **O's clauses 3–4 are ungrounded in this overlay.** No landed r39 policy artifact exists at `7ceff59` to measure the disposition leg, and the wrapped-field clause has no closed-registry probe. The claim is stale on the two capability legs, so the verdict does not depend on them; the ungrounded clauses are named here rather than silently dropped.
- **`grep_absent`, `path_present` and `sha256_eq` are not exercised by this demo.** They remain in the closed vocabulary; the tool's selftest (O04) and probe-coverage seat (O13) own their controls.
- **No claim is made about post-landing state.** This is a pre-dispatch regression at `7ceff59`, not a re-check of r43's acceptance or of the current corpus (223 at HEAD).
