# O07 — Anti-theater mutation: the r43 verdict is invariant under prose rewrites because capability and ownership are measured, not matched

- Seat: `O07` | role executor | claim `O` | round 47, loop 2
- Out path: `reports/round-47/op/O07-anti-theater.md` (the only file this seat writes under `reports/`)
- Mission: `reports/round-47/targets.json:39` — "mutate the r43 O tool name to the existing witness (couples-reference-extractor.py) and C's literals to live values; show the gate still flags via capability/ownership not literal text. Fenced demo."
- Contract: `reports/round-47/claims.json:39` (tool), `:41` (`after_required`, the anti-theater mutation clause), `:47` (thresholds); K03 §5 (`reports/round-47/scout/K03-gate-spec.md:317-331`) and §7.3 mutants (`:529-540`).
- Baseline under test: `7ceff59` (`reports/round-43/claims.json:7`); HEAD at this seat: `6e9a30d`.
- Boundary: no filed byte edited (`reports/round-43/claims.json` sha256 `9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b` before and after, matching the overlay pin); no corpus/tools staging; no git mutation; no `run-validation.py`; `git status --porcelain` for `corpus`, `tools`, `reports/round-43` → empty.

## 1. Result

Twelve runs against the r43 claims file, using the K03-conformant reference evaluator (`reports/round-47/op/O05-r43-demo.md`; digest pinned in §8), each run in its own mutant fixture:

| Run | Claim mutated | Prose mutation | Probes | O / C / Ca | exit |
|---|---|---|---|---|---|
| **M0** | — | none (filed bytes) | O05 overlay | STALE / STALE / FRESH | 1 |
| **M1** | O | names the live witness `tools/harness/couples-reference-extractor.py` as a hollow extractor | capability held fixed | **STALE** / STALE / FRESH | 1 |
| **M1-L** | O | same bytes as M1 (`claims_sha256 6cd02779…`) | **name/path + counts only** (the theater gate) | **FRESH / FRESH / FRESH** | **0** |
| **M2** | O | names only `tools/harness/basename-couples-resolver.py`, absent at baseline | capability held fixed | **STALE** / STALE / FRESH | 1 |
| **M2-L** | O | same bytes as M2 | name/path + counts only | **FRESH / FRESH / FRESH** | **0** |
| **M3** | C | removes the literal `lithic`; says "the stone, gem and metal slot"; counts left at live 26/223 | ownership (aliases) + counts | STALE / **STALE** / FRESH | 1 |
| **M3-L** | C | same bytes as M3 | ownership (single token `lithic`) + counts | STALE / **STALE** / FRESH | 1 |
| **M4** | C | counts mutated to post-landing 27/224 | counts follow the mutation | STALE / **STALE** / FRESH | 1 |
| **M5** | O | M1 bytes | capability target carries a `tool` key | malformed | **2** |
| **M6** | — | exact repeat of M1's command | identical | identical byte-for-byte | 1 |
| **M7** | O | M1 bytes | capability scope narrowed to `tools/harness/p*.py` | **FRESH / FRESH / FRESH** | **0** |
| **M8** | C | M3 bytes | ownership partition narrowed to `linguistics` | STALE / **FRESH** / FRESH | 1 |

The contract sentence this seat exists to prove is `reports/round-47/claims.json:41`: *"still flags under an anti-theater mutation (rename the tool/live values — flags from capability/ownership not literal text)"*.

- **O** stays STALE in both naming directions: naming the real witness (M1) and naming a nonexistent successor (M2). The capability probe measures `main` + `classify` + `resolve_entry` + `--census` + `--selftest` in `tools/**.py` and finds the witness under whatever name the harness holds.
- **C** stays STALE after the claim's prose no longer contains the word `lithic` and after both counts match (M3/M3-L). The only mismatching clause is the ownership probe. The word "lithic" occurs **14 times across 4** myth-symbol files but owns a header in exactly **one** entry (`mineral-stone-symbolism.md:1,3,5`) — literal occurrence and ownership are different measurements, and the probe measures the latter.
- The **theater gate** is not hypothetical: the same mutant bytes run through path/name + count checks return `fresh=3 stale=0`, exit **0** (M1-L, M2-L). That is the false negative the capability/ownership legs close.

Two honest limits are measured in §7: the gate is only as honest as its declared **scope** (M7) and **partition** (M8). Neither is a defect unique to this tool — both are author-declared inputs — but they are recorded here so X03/O09 do not have to discover them later.

## 2. What counts as "theater" here

A theater gate is one whose verdict is a function of the claim's **words or paths** rather than of the state the claim asserts. The r43 defect (R01-43-12) was exactly this shape: the O claim said "no durable instrument implements the r39 basename-couples policy" while `tools/harness/couples-reference-extractor.py` was tracked at the baseline and passed its own 8/8 selftest (`reports/round-43/review/R01-review.md:389`). A gate that reads the claim's named path, or greps the claim's prose, cannot see that.

The mutation method is therefore:

1. Take the filed r43 claims bytes as a **read-only input**; copy and mutate only in memory / scratch.
2. Rewrite the `before` prose so the *words* collide with what a literal gate would find true — name the live witness, name a nonexistent tool, quote the owner's own H1 wording, change the numeric literals to post-landing values.
3. Re-sync each check's `clause` to a substring of the mutated `before` (the schema refuses silent decoupling — measured in §6), and re-pin `claims_sha256` to the mutant bytes (the evaluator refuses a stale pin — measured in §6).
4. Hold the **measurement targets fixed** for the capability/ownership runs. Only the labeled `-L` runs swap in a literal gate.
5. Compare verdicts. If the verdict changes when only the prose changes, the gate is theater. If it holds, the verdict came from state.

The filed file is never written: every mutant is a new file under `.scratch/o07/out/`, and the original sha is asserted before and after the harness (`filed claims sha256 unchanged: True`).

## 3. Measured baseline facts at `7ceff59`

Every value below is read from committed bytes, not the worktree.

**The witness is tracked and has the capability** (`reports/round-47/op/O05-r43-demo.md:31-34` independently re-measured here):

```
$ git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1  -

$ python3 -B - <<'PY'   # ast facts from the baseline blob
...
top-level functions: ['basename_index', 'census', 'classify', 'couples_block',
                      'couples_field', 'expand_braces', 'field_refs', 'join_parts',
                      'main', 'resolve_entry', 'selftest']
argparse flags: ['--selftest', '--census']
couples_census facts: True
PY
```

**The successor path is absent at baseline and present at HEAD** — the live-value drift between the r43 baseline and this seat:

```
$ for c in 7ceff59 HEAD; do
    printf "%s extractor: " "$c"; git cat-file -e $c:tools/harness/couples-reference-extractor.py && echo present || echo ABSENT
    printf "%s successor: " "$c"; git cat-file -e $c:tools/harness/basename-couples-resolver.py && echo present || echo ABSENT
  done
7ceff59 extractor: present
7ceff59 successor: ABSENT
HEAD extractor: present
HEAD successor: present
```

**The count literals are the same at baseline and at HEAD** — an important correction to the seat mission's phrasing "C's literals to live values":

```
$ git ls-tree -r --name-only HEAD -- corpus/knowledge | grep -c '\.md$'        # 223
$ git ls-tree -r --name-only HEAD -- corpus/knowledge/myth-symbol | grep -c '\.md$'  # 26
$ git ls-tree -r --name-only 7ceff59 -- corpus/knowledge | grep -c '\.md$'     # 223
$ git ls-tree -r --name-only 7ceff59 -- corpus/knowledge/myth-symbol | grep -c '\.md$'  # 26
```

So the *live* values for C's two numeric literals are identical to the declared ones. There is no live-value mutation of 26/223 that carries signal; §5.4 states this and runs the opposite direction (post-landing 27/224) as a sensitivity control. The live-value signal in C is the **owner's own wording** (the H1 "Stone, gem and metal symbolism — the lithic register"), used in M3.

**Literal occurrence ≠ ownership**:

```
$ git grep -n -i lithic HEAD -- 'corpus/knowledge/myth-symbol/*.md' | awk -F: '{print $1}' | sort | uniq -c
     14 HEAD                    # 14 matching lines in 4 files
$ git grep -n -i lithic HEAD -- 'corpus/knowledge/myth-symbol/*.md' | grep -E ':[0-9]+:(# |- topic:|- gap filled:)'
HEAD:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:1:# Stone, gem and metal symbolism — the lithic register: ...
HEAD:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:3:- gap filled: the lithic/mineral register is absent ...
HEAD:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:5:- topic: the lithic register of a fictional culture's ...
```

Four files mention the word; one file owns it in a header field. A grep-based gate has to choose between under- and over-counting; `topic_owner_absent` scans only `H1` / `- topic:` / `- gap filled:` (O02 §3, `reports/round-47/op/O02-probe-registry.md:64`), which is the measurement that matches "owned".

**Ca's premise is baseline-scoped** (used only as the control that must not flip):

```
$ git cat-file -e 7ceff59:reports/round-43/calib/dispositions-r38-r39.json  → absent
$ ls reports/round-43/calib/dispositions-r38-r39.json                        → present at HEAD
```

## 4. The mutants

Mutant `before` strings, verbatim. Only `before` changes; every other claim field, all `after_required` text and the round metadata stay byte-identical to the filed file.

**M1 — O names the live witness as hollow.**

```
tools/harness/couples-reference-extractor.py is tracked but is a hollow reference extractor that implements no r39 basename-couples policy; its named successor path tools/harness/basename-couples-resolver.py is absent at baseline; the only resolver that ever ran (r39 I-C05) lives in ephemeral .scratch (r39-ic05-resolver-durability); the verbatim policy landing lacks block extraction + a disposition leg (r39-basename-successor-instrument, Ca04 D1 reproduced live by R01); the single wrapped couples field reads 0/4 tokens
```

The first clause now contains the witness's exact path and asserts it is hollow. A path/name gate sees the file present and stops. The capability probe reads the baseline blob's AST: `main`, `classify`, `resolve_entry` present and `--census`, `--selftest` registered → measured `true` against `expect:false` → **MISMATCH → STALE**.

**M2 — O names a tool that does not exist at baseline.**

```
the only durable instrument would be tools/harness/basename-couples-resolver.py, which is absent at baseline, so no durable instrument implements the r39 basename-couples policy; the only resolver that ever ran (r39 I-C05) lives in ephemeral .scratch (r39-ic05-resolver-durability); the verbatim policy landing lacks block extraction + a disposition leg (r39-basename-successor-instrument, Ca04 D1 reproduced live by R01); the single wrapped couples field reads 0/4 tokens
```

This is the inverse mutation: the claim's named path genuinely is absent, so `path_absent expect:true` **matches** (M2-L goes green). The capability probe still finds the capable file under a name the claim never mentions → **STALE**.

**M3 — C drops the literal `lithic`, keeps the live counts.**

```
myth-symbol 26 (the stone, gem and metal slot is named but unbuilt since r42's C01/C04 collision routed this draft to spare); total 223
```

The wording is the owner entry's own H1 vocabulary ("Stone, gem and metal"). No token `lithic` remains in the claim. Counts are unchanged because 26/223 are the live values (§3). The ownership probe still finds the owner → **STALE** in both the alias form (M3, `topics:["lithic","stone","gem","metal"]`) and the original single-token form (M3-L, `topics:["lithic"]`). The second result is the load-bearing one: the probe never reads the claim, so removing the claim's word cannot change the measurement.

**M4 — C's count literals moved to post-landing values.**

```
myth-symbol 27 (the stone, gem and metal slot is named but unbuilt since r42's C01/C04 collision routed this draft to spare); total 224
```

The checks follow the prose (`count_eq` 27 and 224). Measured 26 and 223 → both mismatch, plus ownership mismatch → STALE. This shows the count legs are live, not decorative: M3's count matches were not vacuous.

**M1-L / M2-L — the theater gate.** Same mutant bytes as M1/M2 (`claims_sha256 6cd02779…` and `c4bd3d05…` respectively), but the O checks are replaced with two name/path checks (`path_present` on the witness, `path_absent` on the successor) and C's checks are the two counts with the ownership check removed. This is a valid overlay under the same schema — no malformed input, no missing `before`, no unevaluated clause. It returns **FRESH on all three, exit 0**, on a claims file that is stale in two claims. That is the exact false negative the r47 O tool must not reproduce.

## 5. Verbatim runs

Full stdout for every run is in `.scratch/o07/out/run-*.out`; the decisive lines are quoted here. The evaluator is not the durable tool (see §8).

### 5.1 M0 — control on the filed bytes

```
$ python3 -B .scratch/o05/claims-freshness-k03.py \
    --claims reports/round-43/claims.json --checks .scratch/o05/r43-checks.json
...
== claim O ==
  [MISMATCH] no durable instrument implements the r39 basename-couples policy | capability_present expect=False measured=True
             tools/harness/couples-reference-extractor.py: main+classify+resolve_entry, --census+--selftest
  [MISMATCH] the only resolver that ever ran (r39 I-C05) lives in ephemeral .scratch | capability_present expect=False measured=True
  VERDICT: STALE
== claim C ==
  [MATCH] myth-symbol 26 | count_eq expect=True measured=True
  [MISMATCH] lithic slot named but unbuilt | topic_owner_absent expect=True measured=False
             corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:1 (H1) ... ; :3 (gap filled) ... ; :5 (topic) ...
  [MATCH] total 223 | count_eq expect=True measured=True
  VERDICT: STALE
== claim Ca ==
  [MATCH] have no per-finding disposition on record | path_absent expect=True measured=True
  VERDICT: FRESH
summary: fresh=1 stale=2 could-not-evaluate=0
exit 1
REFUSE: stale claim(s) O, C at 7ceff59a0216a8ea21ee43262d9fc72abf770cee
```

### 5.2 M1 — witness named, capability measured

```
== claim O ==
  [MISMATCH] is a hollow reference extractor that implements no r39 basename-couples policy | capability_present expect=False measured=True
             tools/harness/couples-reference-extractor.py: main+classify+resolve_entry, --census+--selftest
  [MISMATCH] the only resolver that ever ran (r39 I-C05) lives in ephemeral .scratch | capability_present expect=False measured=True
  VERDICT: STALE
...
summary: fresh=1 stale=2 could-not-evaluate=0
exit 1
REFUSE: stale claim(s) O, C at 7ceff59a0216a8ea21ee43262d9fc72abf770cee
```

### 5.3 M2 — nonexistent name, capability still found

```
== claim O ==
  [MISMATCH] so no durable instrument implements the r39 basename-couples policy | capability_present expect=False measured=True
             tools/harness/couples-reference-extractor.py: main+classify+resolve_entry, --census+--selftest
  VERDICT: STALE
...
exit 1
```

### 5.4 M1-L — the same M1 bytes through a name/path gate

```
== claim O ==
  [MATCH] tools/harness/couples-reference-extractor.py is tracked | path_present expect=True measured=True
  [MATCH] its named successor path tools/harness/basename-couples-resolver.py is absent at baseline | path_absent expect=True measured=True
  VERDICT: FRESH
== claim C ==
  [MATCH] myth-symbol 26 | count_eq expect=True measured=True
  [MATCH] total 223 | count_eq expect=True measured=True
  VERDICT: FRESH
== claim Ca ==
  [MATCH] have no per-finding disposition on record | path_absent expect=True measured=True
  VERDICT: FRESH
summary: fresh=3 stale=0 could-not-evaluate=0
exit 0
```

M1 and M1-L read **the same claims bytes** (`claims_sha256 6cd0277922ea771f550e88e85f568d5d32453af04e6cdf8ec39bc245ef1faad8`). The only difference is the probe set. M1 exits 1; M1-L exits 0. The verdict is a function of the probes.

### 5.5 M3 — C reworded, counts live, ownership mismatches

```
== claim C ==
  [MATCH] myth-symbol 26 | count_eq expect=True measured=True
             corpus/knowledge/myth-symbol/*.md -> 26 (want eq 26)
  [MATCH] total 223 | count_eq expect=True measured=True
             corpus/knowledge/*/*.md -> 223 (want eq 223)
  [MISMATCH] the stone, gem and metal slot is named but unbuilt | topic_owner_absent expect=True measured=False
             corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:1 (H1) ... ; :3 (gap filled) ... ; :5 (topic) ...
  VERDICT: STALE
```

M3-L is the same row with `topics:["lithic"]` — identical verdict and identical owner list. The ownership measurement is independent of the claim's vocabulary.

### 5.6 M4 — count literals moved to 27/224

```
  [MISMATCH] myth-symbol 27 | count_eq expect=True measured=False
             corpus/knowledge/myth-symbol/*.md -> 26 (want eq 27)
  [MISMATCH] total 224 | count_eq expect=True measured=False
             corpus/knowledge/*/*.md -> 223 (want eq 224)
  [MISMATCH] the stone, gem and metal slot is named but unbuilt | topic_owner_absent expect=True measured=False
  VERDICT: STALE
```

### 5.7 M5 — a capability probe cannot be bound to a tool name

```
$ python3 -B .scratch/o05/claims-freshness-k03.py --claims .../claims-M5.json --checks .../checks-M5.json
MALFORMED: capability_present target has unknown keys ['tool']
exit 2
```

The overlay added `"tool": "couples-reference-extractor.py"` to the capability target. The schema rejects the key rather than ignoring it, so a name binding cannot be smuggled into the behavioral probe (K03 `:322`; O02 `:65`).

### 5.8 M6 — determinism

The exact M1 command was run twice; stdout and exit code are byte-identical (`run-M1.out` and `run-M6.out` both sha256 `6100dd7a83c3fcdf00126a098ca69d115e47c2172684aea193323c77667947c4`). No timestamp or random value enters the decision surface.

### 5.9 State-flip control (K03 §7.4)

A reduced, premise-only overlay (O capability; C ownership; Ca path) run at two baselines with the same claims bytes:

```
$ python3 -B .scratch/o05/claims-freshness-k03.py --claims reports/round-43/claims.json \
    --checks .scratch/o07/out/checks-stateflip.json --at 7ceff59
== claim O ==  [MISMATCH] capability_present expect=False measured=True     VERDICT: STALE
== claim C ==  [MISMATCH] topic_owner_absent expect=True measured=False    VERDICT: STALE
== claim Ca == [MATCH] path_absent expect=True measured=True              VERDICT: FRESH
summary: fresh=1 stale=2 could-not-evaluate=0 ; exit 1

$ ... --at ac47c78
== claim O ==  [MATCH] capability_present expect=False measured=False      VERDICT: FRESH
== claim C ==  [MATCH] topic_owner_absent expect=True measured=True        VERDICT: FRESH
== claim Ca == [MATCH] path_absent expect=True measured=True               VERDICT: FRESH
summary: fresh=3 stale=0 could-not-evaluate=0 ; exit 0
```

Same tool, same checks, earlier baseline, flipped verdict. This is the strongest anti-hardcoding control: a gate keyed on round id or claim id cannot produce it. Note that the **reduced** overlay is required: the full O05 overlay carries the count clauses, and at `ac47c78` the corpus is 220/23, so C would stay STALE on counts and the flip would be confounded. State-flip controls must isolate premise probes from era-bound counts.

## 6. Controls that fired on the harness itself

- **Clause binding is enforced.** The first M2 attempt reused M1's clause string; the evaluator refused it: `MALFORMED: clause is not a substring of 'before': 'is a hollow reference extractor...'`, exit 2. A mutant cannot silently keep a stale quote.
- **The overlay pin is enforced.** M0 was first attempted through a re-serialized copy of the claims file; the evaluator refused it (`overlay claims_sha256 does not match the claims file bytes`, exit 2). Mutants must carry their own pin; there is no free ride on the filed digest.
- **The filed file is untouched.** The harness asserts the filed sha before and after every run (`filed claims sha256 unchanged: True`); `git status --porcelain -- corpus tools reports/round-43` is empty.
- **Unknown probe kinds and missing `expect`/`target` are malformed, not false** (O03's table; exercised by O05 §5.3 and O04). Not re-run here beyond M5 to avoid duplicating those seats.

## 7. Limits — theater surfaces this tool cannot close (measured)

These are not failures of the r43 regression; they are properties of any declared-probe gate, and they matter for the r47 acceptance review.

**7.1 Scope narrowing defeats the capability probe (M7).** The M1 claim's capability check was narrowed to `tools/harness/p*.py`:

```
== claim O ==
  [MATCH] is a hollow reference extractor that implements no r39 basename-couples policy | capability_present expect=False measured=False
             no in-scope file satisfies couples_census (2 scanned)
  VERDICT: FRESH
...
summary: fresh=3 stale=0   exit 0
```

The witness is not in scope, so the probe honestly reports "no capable file among 2 scanned" and the stale claim passes. The report **does** print the scope's candidate count, which is the only defense: the review must diff the declared scope, not just the verdict. K03's selftest has no scope-dodge control; O04/O09 should add one (`K07` in the O04 numbering): same witness, scope that excludes it, expect `could-not-evaluate` or a named warning, not silent fresh.

**7.2 Partition narrowing defeats the ownership probe (M8).** The M3 claim's ownership check was narrowed to `partition: "linguistics"`:

```
== claim C ==
  [MATCH] the stone, gem and metal slot is named but unbuilt | topic_owner_absent expect=True measured=True
             no owner in 25 entries
  VERDICT: FRESH
```

The owner sits in `myth-symbol`; 25 linguistics entries legitimately do not own it. A claim author who declares the wrong partition gets a green C. The mitigation is the same: the partition is printed, and the round's claim (not the check author) should pin the partition under test. The r43 C `before` names `myth-symbol`, so the correct partition is textually available — a durable tool could *require* the partition to appear in `before` before accepting the probe.

**7.3 Clause binding is prose-dependent by design.** `clause` must be a whitespace-normalized substring of `before` (`scout/K03-gate-spec.md:60` (D9), `:407` (V10); measured refusal in §6). That is the one place the claim text is an input. It is a *binding* check, not a measurement: changing the prose requires re-quoting the clause, which is visible in the overlay diff, and the re-quoted check still measures the same target. An author can under-declare checks — an undeclared clause is not verdict-bearing (K03 §7.2) — so the review should compare the number of declared checks against the number of premise clauses in `before`, as O05 §7 already does by naming its ungrounded clauses.

**7.4 Probe targets are author-declared.** The anti-theater property is *invariance under prose mutation given fixed probes*, not immunity to a dishonest probe declaration. M7/M8 are the two dishonest declarations that stay schema-valid. A gate detects contradictions; it cannot detect intent. This is why the round contract pairs it with the two-verifier rule and with O09's false-positive traps.

**7.5 Capability facts are single-file.** `couples_census` requires `main`, `classify`, `resolve_entry` and the two flags in one parsed baseline file. A future instrument that splits the capability across modules would measure `false` even if the capability exists in aggregate. The r43 witness is single-file (measured §3), so the regression is unaffected; the registry's contract should say this explicitly (K03 §5 implies it; O02's `capability_present` table should state it).

## 8. Provenance and reproducibility

The evaluator used for every run is O05's K03-conformant reference evaluator, **not** the durable tool:

```
f35eab201910f42c4184391c24de63a721fed859ad419575599f4ff02412b910  .scratch/o05/claims-freshness-k03.py
0f43e90746ed99a1cae06e6887db87f9ca648aaeeebd3b7101a652bd82d8b25d  .scratch/o05/r43-checks.json
9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b  reports/round-43/claims.json
14af445b5dc03a1c3f733ce8175849e984c84b8e290cd3208f132bfc610fa9e7  .scratch/o07/mutate.py (before this report)
e499ebaa75162171fc015381e519909394076677bb2067bd878a2df39e7193df  .scratch/o07/out/checks-stateflip.json
```

Mutant fixtures (all under `.scratch/o07/out/`, scratch-only; the fenced spec in Appendix B makes them durable):

| Fixture | sha256 (first 12) |
|---|---|
| M1/M1-L claims | `6cd0277922ea` |
| M2/M2-L claims | `c4bd3d05b4c4` |
| M3/M3-L/M8 claims | `3a09364f6c6b` |
| M4 claims | `888d999d1d65` |
| M1 overlay | `cb6df6a3f133` |
| M1-L overlay | `311a6deb0505` |
| M3 overlay | `be5b8b097a0d` |
| M3-L overlay | `60095c4ea2d2` |
| M5 overlay | `fdfccc52fd25` |
| M7 overlay | `89bd3ef6c4c6` |
| M8 overlay | `0d6fdfb37732` |

Commands to reproduce (requires O05's evaluator and overlay to exist; if scratch is cleaned, extract them from `reports/round-47/op/O05-r43-demo.md` and its digest pin):

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B .scratch/o07/mutate.py
```

Expected tail:

```
### M0 -> exit 1 ... ### M1 -> exit 1 ... ### M1-L -> exit 0 ... ### M2 -> exit 1 ...
### M2-L -> exit 0 ... ### M3 -> exit 1 ... ### M3-L -> exit 1 ... ### M4 -> exit 1 ...
### M7 -> exit 0 ... ### M8 -> exit 1 ... ### M5 -> exit 2 ... ### M6 -> exit 1
M1 vs M6 identical stdout+exit: True
filed claims sha256 unchanged: True
```

## 9. Handoff

1. **O08 / V02 acceptance tests.** Reproduce AT-1 through AT-7 from the **durable** path once `tools/harness/claims-freshness.py` lands. Expected verdicts are fixed by this report:

   | ID | Input | Expected |
   |---|---|---|
   | AT-1 | filed r43 claims + O05 overlay | O STALE, C STALE, Ca FRESH; exit 1 |
   | AT-2 | M1 claims + capability overlay | O **STALE** (2/2 capability mismatch) |
   | AT-3 | M1 claims + literal overlay | O **FRESH** (this is the theater gate; it must be *documented as insufficient*, never adopted) |
   | AT-4 | M2 claims + capability overlay | O **STALE** despite the named path being absent |
   | AT-5 | M3 claims + ownership overlay (single-token `lithic`) | C **STALE** with both counts matching |
   | AT-6 | M5 overlay | exit 2, unknown target key |
   | AT-7 | state-flip reduced overlay at `7ceff59` and `ac47c78` | stale/exit 1 then fresh/exit 0 |

   AT-3 is a *negative* acceptance test: a gate that returns FRESH there is the theater gate and fails the r47 contract (`reports/round-47/claims.json:41`).

2. **Integrator.** Nothing from this seat is applied to `corpus/` or `tools/`. If the round wants the anti-theater cases as a filed calibration artifact, the fenced `AT-SPEC` in Appendix B is the byte source; suggested path `reports/round-47/calib/o07-anti-theater-cases.json`. It contains no filed bytes, only mutant fixtures.

3. **Schema conflict to reconcile before the durable run.** O02's registry table specifies `topic_owner_absent` target `{"topic": [...], "partitions": [...]}` (`reports/round-47/op/O02-probe-registry.md:55`), while O05's evaluator and overlay use `{"topics": [...], "partition": ...}` (`reports/round-47/op/O05-r43-demo.md:135`; evaluator `_target_fields("topic_owner_absent", target, ("topics",), ("partition", "fields"))`, `.scratch/o05/claims-freshness-k03.py:191`). The two forms are not interchangeable: a durable tool accepting only one will return exit 2 on the other's fixtures. My mutants follow the **evaluator/O05** shape because that is what produced the measured outputs above. If the durable tool adopts O02's shape, the transform is mechanical (`topics`→`topic`, `partition`→`partitions`) but every fixture pin must be recomputed. **to-verify — owner: O12/integrator.**

4. **X03 / O09.** The scope (M7) and partition (M8) dodges are the two theater surfaces that survive a schema-valid overlay. They are measured here so the critics can start from evidence rather than a hypothesis; the constructive fix is a report-level warning when a capability/ownership probe's declared scope does not contain the claim's own noun (witness name in O's `before`; partition in C's `before`).

5. **R01-43-12 closure.** This artifact is the anti-theater leg only. It does not replace the durable tool, the r43 positive regression (O05), the negative control (O06) or the selftest (O04). The r47 O claim is not satisfied by this seat alone.

## 10. Unresolved / to-verify

- **The durable tool does not exist at this cut.** Every verdict above comes from O05's scratch reference evaluator, sha `f35eab20…`. If the durable tool differs in probe semantics, the verdicts must be re-measured, not assumed.
- **Live-value premise of the mission is partly a no-op.** C's count literals at HEAD equal the baseline values (223/26, measured §3). The only live-value mutation with signal is the owner wording; the report says so rather than manufacturing a numeric change.
- **M7/M8 are limits, not passes.** They are recorded as theater surfaces. Whether the durable tool should reject a scope/partition that omits the claim's named object is an open design question; K03 does not require it, and I did not implement it (this seat writes no tool).
- **Capability single-file limit** (§7.5) is stated but not exercised by a fixture; a split-module instrument is out of scope for r43 and would need a registry change.
- **`topic_owner_absent` first-200-lines limit** (`reports/round-47/op/O02-probe-registry.md:243`) is not exercised: the owner's fields are at lines 1, 3 and 5. A future entry with a late header would under-count owners; the probe's detail list makes that visible, but no control covers it here.

---

## Appendix A — the mutation harness (fenced, runnable)

This is the exact script that produced §5 (`sha256 14af445b5dc03a1c3f733ce8175849e984c84b8e290cd3208f132bfc610fa9e7`). It writes only under `.scratch/o07/out/` and asserts the filed claims sha before and after.

```python
#!/usr/bin/env python3
"""O07 anti-theater mutation harness (round 47).

Mutates only the *prose* of the r43 claims' `before` strings (never the filed
file), resyncs each overlay's `clause` binding, and runs the K03-conformant
reference evaluator. The probes' measurement targets are held fixed unless a
variant is explicitly labelled as a literal-gate contrast.

Writes mutated claims/overlays + captured outputs under .scratch/o07/out/.
Never touches reports/round-43/**.
"""
from __future__ import annotations

import copy
import hashlib
import json
import os
import subprocess
import sys

sys.dont_write_bytecode = True

LANE = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
EVAL = os.path.join(LANE, ".scratch/o05/claims-freshness-k03.py")
BASE_CLAIMS = os.path.join(LANE, "reports/round-43/claims.json")
BASE_OVERLAY = os.path.join(LANE, ".scratch/o05/r43-checks.json")
OUT = os.path.join(LANE, ".scratch/o07/out")

O_M1 = (
    "tools/harness/couples-reference-extractor.py is tracked but is a hollow "
    "reference extractor that implements no r39 basename-couples policy; its named "
    "successor path tools/harness/basename-couples-resolver.py is absent at "
    "baseline; the only resolver that ever ran (r39 I-C05) lives in ephemeral "
    ".scratch (r39-ic05-resolver-durability); the verbatim policy landing lacks "
    "block extraction + a disposition leg (r39-basename-successor-instrument, Ca04 "
    "D1 reproduced live by R01); the single wrapped couples field reads 0/4 tokens"
)

O_M2 = (
    "the only durable instrument would be tools/harness/basename-couples-resolver.py, "
    "which is absent at baseline, so no durable instrument implements the r39 "
    "basename-couples policy; the only resolver that ever ran (r39 I-C05) lives in "
    "ephemeral .scratch (r39-ic05-resolver-durability); the verbatim policy landing "
    "lacks block extraction + a disposition leg (r39-basename-successor-instrument, "
    "Ca04 D1 reproduced live by R01); the single wrapped couples field reads 0/4 tokens"
)

C_M3 = (
    "myth-symbol 26 (the stone, gem and metal slot is named but unbuilt since r42's "
    "C01/C04 collision routed this draft to spare); total 223"
)

C_M4 = (
    "myth-symbol 27 (the stone, gem and metal slot is named but unbuilt since r42's "
    "C01/C04 collision routed this draft to spare); total 224"
)

CAP_O = [
    {
        "clause": "is a hollow reference extractor that implements no r39 basename-couples policy",
        "probe_kind": "capability_present",
        "target": {"capability": "couples_census", "scope": "tools/**.py"},
        "expect": False,
        "evidence_command": "git ls-tree -r -z --name-only 7ceff59 -- tools/",
    },
    {
        "clause": "the only resolver that ever ran (r39 I-C05) lives in ephemeral .scratch",
        "probe_kind": "capability_present",
        "target": {"capability": "couples_census", "scope": "tools/**.py"},
        "expect": False,
        "evidence_command": "git show 7ceff59:tools/harness/couples-reference-extractor.py | grep -n add_argument",
    },
]

# A gate that binds on the *name/path* a claim happens to mention.
LIT_O = [
    {
        "clause": "tools/harness/couples-reference-extractor.py is tracked",
        "probe_kind": "path_present",
        "target": {"path": "tools/harness/couples-reference-extractor.py"},
        "expect": True,
        "evidence_command": "git ls-tree 7ceff59 tools/harness/couples-reference-extractor.py",
    },
    {
        "clause": "its named successor path tools/harness/basename-couples-resolver.py is absent at baseline",
        "probe_kind": "path_absent",
        "target": {"path": "tools/harness/basename-couples-resolver.py"},
        "expect": True,
        "evidence_command": "git cat-file -e 7ceff59:tools/harness/basename-couples-resolver.py",
    },
]

# A gate that binds on the *name* the M2 claim invents.
LIT_M2 = [
    {
        "clause": "which is absent at baseline",
        "probe_kind": "path_absent",
        "target": {"path": "tools/harness/basename-couples-resolver.py"},
        "expect": True,
        "evidence_command": "git cat-file -e 7ceff59:tools/harness/basename-couples-resolver.py",
    }
]

COUNT_C = [
    {
        "clause": "myth-symbol 26",
        "probe_kind": "count_eq",
        "target": {"glob": "corpus/knowledge/myth-symbol/*.md", "value": 26},
        "expect": True,
        "evidence_command": "git ls-tree -r --name-only 7ceff59 -- corpus/knowledge/myth-symbol | wc -l",
    },
    {
        "clause": "total 223",
        "probe_kind": "count_eq",
        "target": {"glob": "corpus/knowledge/*/*.md", "value": 223},
        "expect": True,
        "evidence_command": "git ls-tree -r --name-only 7ceff59 -- corpus/knowledge | wc -l",
    },
]

OWN_C_LITHIC = {
    "clause": "the stone, gem and metal slot is named but unbuilt",
    "probe_kind": "topic_owner_absent",
    "target": {"topics": ["lithic"], "partition": "myth-symbol",
               "fields": ["H1", "topic", "gap filled"]},
    "expect": True,
    "evidence_command": "git grep -n -i lithic 7ceff59 -- 'corpus/knowledge/myth-symbol/*.md'",
}

OWN_C_ALIAS = {
    "clause": "the stone, gem and metal slot is named but unbuilt",
    "probe_kind": "topic_owner_absent",
    "target": {"topics": ["lithic", "stone", "gem", "metal"], "partition": "myth-symbol",
               "fields": ["H1", "topic", "gap filled"]},
    "expect": True,
    "evidence_command": "git grep -n -i -E 'lithic|stone|gem|metal' 7ceff59 -- 'corpus/knowledge/myth-symbol/*.md'",
}


def load(path):
    with open(path, "rb") as handle:
        raw = handle.read()
    return raw, json.loads(raw.decode("utf-8"))


def dump(obj, path):
    data = json.dumps(obj, indent=2, ensure_ascii=False) + "\n"
    with open(path, "w", encoding="utf-8") as handle:
        handle.write(data)
    return hashlib.sha256(data.encode("utf-8")).hexdigest()


def claims_with(before_map):
    raw, claims = load(BASE_CLAIMS)
    mutated = copy.deepcopy(claims)
    for claim in mutated["claims"]:
        if claim["id"] in before_map:
            claim["before"] = before_map[claim["id"]]
    return raw, mutated


def overlay_for(checks, claims_sha, baseline="7ceff59", round_no=43):
    return {
        "schema": "kotodama-claims-freshness-checks-v1",
        "round": round_no,
        "baseline_commit": baseline,
        "claims_sha256": claims_sha,
        "checks": checks,
    }


def run_cmd(name, claims_path, overlay_path):
    env = dict(os.environ, TMPDIR=os.path.join(LANE, ".scratch"), PYTHONDONTWRITEBYTECODE="1")
    proc = subprocess.run(
        [sys.executable, "-B", EVAL, "--claims", claims_path, "--checks", overlay_path],
        cwd=LANE, env=env, capture_output=True, text=True,
    )
    with open(os.path.join(OUT, "run-%s.out" % name), "w", encoding="utf-8") as handle:
        handle.write(proc.stdout)
        if proc.stderr:
            handle.write("STDERR:\n" + proc.stderr)
    print("### %s -> exit %d" % (name, proc.returncode))
    print(proc.stdout.rstrip())
    if proc.stderr.strip():
        print("STDERR:", proc.stderr.rstrip())
    print()
    return {
        "name": name,
        "claims_path": claims_path,
        "overlay_path": overlay_path,
        "claims_sha256": hashlib.sha256(open(claims_path, "rb").read()).hexdigest(),
        "overlay_sha256": hashlib.sha256(open(overlay_path, "rb").read()).hexdigest(),
        "exit": proc.returncode,
        "stdout": proc.stdout,
        "stderr": proc.stderr,
    }


def run(name, claims_obj, overlay_obj):
    claims_path = os.path.join(OUT, "claims-%s.json" % name)
    overlay_path = os.path.join(OUT, "checks-%s.json" % name)
    dump(claims_obj, claims_path)
    dump(overlay_obj, overlay_path)
    return run_cmd(name, claims_path, overlay_path)


def main():
    os.makedirs(OUT, exist_ok=True)
    raw, base_claims = load(BASE_CLAIMS)
    _, base_overlay = load(BASE_OVERLAY)
    assert hashlib.sha256(raw).hexdigest() == base_overlay["claims_sha256"], "filed claims changed"

    results = []

    # M0 — control: filed claims bytes + O05 overlay, unmutated.
    results.append(run_cmd("M0", BASE_CLAIMS, BASE_OVERLAY))

    # M1 — O prose names the live witness; capability probes held fixed.
    _, c1 = claims_with({"O": O_M1})
    s1 = dump(c1, os.path.join(OUT, "claims-M1.json"))
    results.append(run("M1", c1, overlay_for({"O": copy.deepcopy(CAP_O),
                                              "C": copy.deepcopy(base_overlay["checks"]["C"]),
                                              "Ca": copy.deepcopy(base_overlay["checks"]["Ca"])}, s1)))

    # M1-L — same mutated claim, literal name/path probes only (the theater gate).
    results.append(run("M1-L", c1, overlay_for({"O": copy.deepcopy(LIT_O),
                                                "C": copy.deepcopy(COUNT_C),
                                                "Ca": copy.deepcopy(base_overlay["checks"]["Ca"])}, s1)))

    # M2 — O prose names a tool that does not exist at baseline; capability probe held.
    _, c2 = claims_with({"O": O_M2})
    s2 = dump(c2, os.path.join(OUT, "claims-M2.json"))
    m2_cap = copy.deepcopy(CAP_O)
    m2_cap[0]["clause"] = "so no durable instrument implements the r39 basename-couples policy"
    results.append(run("M2", c2, overlay_for({"O": m2_cap,
                                              "C": copy.deepcopy(base_overlay["checks"]["C"]),
                                              "Ca": copy.deepcopy(base_overlay["checks"]["Ca"])}, s2)))

    # M2-L — the same claim through a name-only gate.
    results.append(run("M2-L", c2, overlay_for({"O": copy.deepcopy(LIT_M2),
                                                "C": copy.deepcopy(COUNT_C),
                                                "Ca": copy.deepcopy(base_overlay["checks"]["Ca"])}, s2)))

    # M3 — C prose stops saying "lithic"; counts unchanged (they are the live values).
    _, c3 = claims_with({"C": C_M3})
    s3 = dump(c3, os.path.join(OUT, "claims-M3.json"))
    results.append(run("M3", c3, overlay_for({"O": copy.deepcopy(base_overlay["checks"]["O"]),
                                              "C": copy.deepcopy(COUNT_C) + [copy.deepcopy(OWN_C_ALIAS)],
                                              "Ca": copy.deepcopy(base_overlay["checks"]["Ca"])}, s3)))

    # M3-L — same mutated prose, original single-token "lithic" ownership probe.
    results.append(run("M3-L", c3, overlay_for({"O": copy.deepcopy(base_overlay["checks"]["O"]),
                                                "C": copy.deepcopy(COUNT_C) + [copy.deepcopy(OWN_C_LITHIC)],
                                                "Ca": copy.deepcopy(base_overlay["checks"]["Ca"])}, s3)))

    # M4 — C count literals mutated to post-landing values 27/224; probes follow.
    _, c4 = claims_with({"C": C_M4})
    s4 = dump(c4, os.path.join(OUT, "claims-M4.json"))
    m4_counts = copy.deepcopy(COUNT_C)
    m4_counts[0]["target"]["value"] = 27
    m4_counts[0]["clause"] = "myth-symbol 27"
    m4_counts[1]["target"]["value"] = 224
    m4_counts[1]["clause"] = "total 224"
    results.append(run("M4", c4, overlay_for({"O": copy.deepcopy(base_overlay["checks"]["O"]),
                                              "C": m4_counts + [copy.deepcopy(OWN_C_LITHIC)],
                                              "Ca": copy.deepcopy(base_overlay["checks"]["Ca"])}, s4)))

    # M7 — theater surface: narrowing the capability scope dodges the witness.
    m7 = [copy.deepcopy(CAP_O[0])]
    m7[0]["target"]["scope"] = "tools/harness/p*.py"
    m7[0]["clause"] = "is a hollow reference extractor that implements no r39 basename-couples policy"
    results.append(run("M7", c1, overlay_for({"O": m7,
                                              "C": copy.deepcopy(COUNT_C),
                                              "Ca": copy.deepcopy(base_overlay["checks"]["Ca"])}, s1)))

    # M8 — theater surface: narrowing the ownership partition dodges the owner.
    m8 = copy.deepcopy(OWN_C_LITHIC)
    m8["target"]["partition"] = "linguistics"
    results.append(run("M8", c3, overlay_for({"O": copy.deepcopy(base_overlay["checks"]["O"]),
                                              "C": copy.deepcopy(COUNT_C) + [m8],
                                              "Ca": copy.deepcopy(base_overlay["checks"]["Ca"])}, s3)))

    # M5 — schema refusal: a capability target carrying a `tool` name is malformed.
    bad = copy.deepcopy(CAP_O)
    bad[0]["target"]["tool"] = "couples-reference-extractor.py"
    results.append(run("M5", c1, overlay_for({"O": bad,
                                              "C": copy.deepcopy(base_overlay["checks"]["C"]),
                                              "Ca": copy.deepcopy(base_overlay["checks"]["Ca"])}, s1)))

    # M6 — determinism: the exact M1 command repeated, byte-compare stdout+exit.
    results.append(run_cmd("M6", results[1]["claims_path"], results[1]["overlay_path"]))

    with open(os.path.join(OUT, "results.json"), "w", encoding="utf-8") as handle:
        json.dump(results, handle, indent=2, ensure_ascii=False)
        handle.write("\n")

    same = results[1]["stdout"] == results[-1]["stdout"] and results[1]["exit"] == results[-1]["exit"]
    print("M1 vs M6 identical stdout+exit: %s" % same)
    print("filed claims sha256 unchanged: %s" % (hashlib.sha256(
        open(BASE_CLAIMS, "rb").read()).hexdigest() == base_overlay["claims_sha256"]))


if __name__ == "__main__":
    main()
```

## Appendix B — AT-SPEC (machine-readable acceptance cases)

If the integrator files this as `reports/round-47/calib/o07-anti-theater-cases.json`, it is a fixture specification, not an overlay: each case names the mutant `before` substitutions, the probe set as a *delta* from the O05 overlay, and the expected per-claim verdict/exit. It contains no filed bytes.

```json
{
  "schema": "kotodama-anti-theater-cases-v1",
  "round": 47,
  "seat": "O07",
  "baseline_commit": "7ceff59",
  "claims_input": "reports/round-43/claims.json",
  "claims_input_sha256": "9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b",
  "cases": [
    {
      "id": "AT-1",
      "purpose": "positive regression control",
      "before_substitutions": {},
      "probes": "o05-overlay",
      "expect": {"O": "STALE", "C": "STALE", "Ca": "FRESH", "exit": 1}
    },
    {
      "id": "AT-2",
      "purpose": "witness named as hollow; capability must still flag",
      "before_substitutions": {"O": "M1"},
      "probes": "M1 CAP_O (capability checks; clauses resynced to the M1 prose)",
      "expect": {"O": "STALE", "C": "STALE", "Ca": "FRESH", "exit": 1}
    },
    {
      "id": "AT-3",
      "purpose": "theater gate: name/path + counts only; must NOT be adopted",
      "before_substitutions": {"O": "M1"},
      "probes": "literal-only (M1 LIT_O + counts 26/223, no capability/ownership)",
      "expect": {"O": "FRESH", "C": "FRESH", "Ca": "FRESH", "exit": 0},
      "note": "A durable gate that returns this is the theater gate and fails reports/round-47/claims.json:41."
    },
    {
      "id": "AT-4",
      "purpose": "nonexistent tool named; capability must still flag",
      "before_substitutions": {"O": "M2"},
      "probes": "M1 CAP_O with the first clause resynced to 'so no durable instrument implements...'",
      "expect": {"O": "STALE", "C": "STALE", "Ca": "FRESH", "exit": 1}
    },
    {
      "id": "AT-5",
      "purpose": "C reworded without the literal 'lithic'; ownership must still flag",
      "before_substitutions": {"C": "M3"},
      "probes": "counts 26/223 + ownership topics=['lithic']; clauses resynced to the M3 prose",
      "expect": {"O": "STALE", "C": "STALE", "Ca": "FRESH", "exit": 1}
    },
    {
      "id": "AT-6",
      "purpose": "capability target cannot carry a tool name",
      "before_substitutions": {"O": "M1"},
      "probes": "M1 CAP_O with target.tool added",
      "expect": {"exit": 2, "stderr_contains": "unknown keys"}
    },
    {
      "id": "AT-7",
      "purpose": "state flip on a reduced premise-only overlay",
      "before_substitutions": {},
      "probes": "reduced overlay (O capability, C ownership, Ca path)",
      "expect": {
        "at_7ceff59": {"O": "STALE", "C": "STALE", "Ca": "FRESH", "exit": 1},
        "at_ac47c78": {"O": "FRESH", "C": "FRESH", "Ca": "FRESH", "exit": 0}
      },
      "note": "Do not include count clauses; at ac47c78 the corpus is 220/23 and the flip would be confounded."
    }
  ],
  "measured_limits": [
    {"id": "M7", "surface": "capability scope narrowing", "observation": "O FRESH, all fresh, exit 0", "owner": "O04/O09"},
    {"id": "M8", "surface": "ownership partition narrowing", "observation": "C FRESH ('no owner in 25 entries')", "owner": "O09/X03"}
  ]
}
```

## Appendix C — state-flip overlay (fenced)

The reduced premise-only overlay used in §5.9; sha256 `e499ebaa75162171fc015381e519909394076677bb2067bd878a2df39e7193df`.

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
        "expect": false
      }
    ],
    "C": [
      {
        "clause": "lithic slot named but unbuilt",
        "probe_kind": "topic_owner_absent",
        "target": {"topics": ["lithic"], "partition": "myth-symbol",
                   "fields": ["H1", "topic", "gap filled"]},
        "expect": true
      }
    ],
    "Ca": [
      {
        "clause": "have no per-finding disposition on record",
        "probe_kind": "path_absent",
        "target": {"path": "reports/round-43/calib/dispositions-r38-r39.json"},
        "expect": true
      }
    ]
  }
}
```
