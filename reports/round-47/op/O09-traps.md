# O09 — false-positive traps for the claims-freshness gate

- Seat: `O09` | role verifier | claim **O** | round 47, loop 2
- Out path: `reports/round-47/op/O09-traps.md` (the only write this seat makes under `reports/round-47/`)
- Baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`); declared `6e9a30d` (`reports/round-47/claims.json:7`)
- Review cut: **2026-10-19T18:06Z** (UTC); first measurements at 18:00Z, O05/O06 landed during the review and are cited for schema only
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root.

**Mission.** Hunt the three false-positive trap families named in `targets.json`:
(1) a novel-phrasing "unbuilt" claim (the R02 llama-herding trap);
(2) a clause with no declared polarity; (3) a `baseline_commit` that is a tag, not a sha.
Confirm the gate handles each per contract.

**Subject at cut.** The durable deliverable `tools/harness/claims-freshness.py` **does not exist**
(`ls` → no such file, exit 2). The only gate bytes are the r44 scratch prototype
`.scratch/ca01/claims-freshness.py`, sha256
`dd88d9e12bda5ade6b4f93864db138e0a5ce54b0ef5cbcf6e4f5050783121434`. All "measured" rows below are
**prototype** runs, labelled as such; the "required" rows are the contract (`R01-review.md:245-246`,
`P01-plan.md:243,268-269`, `X00-connector.md:108-119`, and the operational sidecars
`O05-r43-demo.md:99-101,134-136,173-175`, `O06-negative-control.md:85`). No row claims the durable
tool was run.

---

## 0. Verdict at cut

| trap | prototype measured | contract requirement | durable status |
|---|---|---|---|
| **T1 novel phrasing** | **FAIL — false STALE**: "the llama-herding register slot is unbuilt" → `topic_unowned(topic="register")` → 51 owner hits → STALE, exit 2 | never assert STALE from a generic token; a fresh claim either grounds on the full phrase (FRESH) or is `COULD-NOT-EVALUATE`; never a false ownership fact | **could-not-evaluate** (tool absent) |
| **T2 no declared polarity** | **FAIL, plus a blocking schema ambiguity**: unknown/untyped probe and missing `value` → STALE; **no `expect`, `expect:null`, and a wrong-typed `expect` all → silently FRESH**; `freshness_probes: []` → prose-mined FRESH, exit 0; and the round states `expect` two incompatible ways (P01 vs O05/O06) | malformed input (unknown `probe_kind`, missing/typed-wrong `expect`, no clause span) → `MALFORMED`, exit 2, no verdict; zero premise checks → `COULD-NOT-EVALUATE`, non-zero; **one polarity semantics pinned** | **could-not-evaluate** |
| **T3 tag baseline** | **PARTIAL**: lightweight tag correct; annotated tag evaluates the right tree but reports the **tag-object** sha as `baseline_resolved`; blob/missing/tree revs mishandled (exit 1 or silently accepted); ambiguous tag/branch resolved with the warning discarded | resolve to a commit (`^{commit}`), report declared + resolved 40-hex commit, reject non-commit/ambiguous/missing as `MALFORMED` exit 2, no worktree fallback | **could-not-evaluate** |

**Bottom line for claim O.** The r43 positive regression reproduces on the prototype (O STALE 0/2,
C STALE 2/3, Ca FRESH 1/1, exit 2), but the prototype **fails every one of the three trap families**
in a specific, reproducible way. The O claim's threshold "does not flag a fresh claim" is therefore
**not met by the only extant implementation**, and the durable tool's handling is **could-not-evaluate**
until it lands. §3.0 adds a blocking finding independent of the prototype: the round's own artifacts
define `expect` polarity two incompatible ways, and a tool built from P01's literal wording would
invert every absence check in O05's r43 sidecar. This is delivery debt, not harm to the operability
axis: no live behavior depends on the absent tool, and I found no corpus, ledger, or authority
damage. The acceptance matrix in §6 is ready for O08/V02 to run against the landed path.

---

## 1. Method and limits

**Read:** `reports/round-47/claims.json`, `targets.json`; `reports/round-43/claims.json`;
`reports/round-44/review/R01-review.md:212-258` (the six-part contract);
`reports/round-47/plan/P01-plan.md:225-269` (sidecar schema, probe registry, exit table);
`reports/round-47/cross/X00-connector.md:108-119` (encoding rule);
`reports/round-47/op/O05-r43-demo.md` and `O06-negative-control.md` (the operational `expect` values,
read for schema only — their demo runners were not run); `O10-exit-codes.md` and
`O13-probe-coverage.md` (independent corroboration, not relied on for my measurements);
`.scratch/ca01/claims-freshness.py` in full.

**Ran:** the prototype read-only against synthetic fixtures in `.scratch/o09/fixtures/` (all
recreated in §6/Appendix), the real r43 and r47 claims files, and an isolated scratch clone for tag
refs. No filed byte edited, no corpus staging, no `reports/round-*/run-validation.py`, no git
commit/push/network, no ref mutation in the lane repo.

**Limits.**
- No durable tool existed at the cut, and no O01–O04 tool fragments had landed, so I could not run
  the contract-shaped sidecar through the deliverable. O05/O06 landed during the review; their
  sidecars are read for the `expect` semantics, but their demo runners are not the durable tool and
  were not executed. The exact sidecar wiring (inline `before_checks` vs P01's sidecar file) and the
  `topic_owner_absent` target syntax are **to-verify** against O02/O05's landed schema; the trap
  acceptance below is stated behaviourally so it survives either.
- The tag tests run in `git clone --shared --no-checkout . .scratch/o09/tagrepo`; tags exist only in
  that scratch repository. The lane repo has **no tags** (`git tag -l` → empty), so mutating it was
  neither necessary nor done.
- r47 was declared before any gate landed; running the gate on its own `claims.json` is a diagnostic,
  not a retroactive pre-dispatch refusal.

---

## 2. Trap T1 — novel-phrasing "unbuilt" (the R02 llama-herding trap)

### 2.1 Measured

Fixture `.scratch/o09/fixtures/t1-llama-novel.json` (prototype schema):

```json
{"round": 999, "baseline_commit": "6e9a30d", "claims": [{
  "id": "T1", "axis": "coverage",
  "before": "the llama-herding register slot is unbuilt and has no owner",
  "after_required": "corpus/knowledge/culture-material/llama-herding.md lands",
  "counting_commands": []}]}
```

```
$ python3 -B .scratch/ca01/claims-freshness.py --claims .scratch/o09/fixtures/t1-llama-novel.json
[T1] coverage -- STALE (0/1 premises hold)
      probe {"kind": "topic_unowned", "topic": "register"} -> 51 owner hit(s) for register
summary: 0 fresh, 1 stale, 0 unverifiable, 0 ungrounded clause(s)
REFUSE: claims T1 have a `before` already false at 6e9a30d…; do not dispatch.
exit 2
```

The 51 hits are the generic English word "register", across **36 distinct entries**, in linguistics
(`sociolinguistics-registers.md`, `register-strata-attestation.md`, `register-lexicon-ceilings.md`,
`dialect-register-consistency.md`), craft (`craft-artisan-lexicon.md`), law
(`sumptuary-law-rank-display.md`), etc. The claim's actual topic phrase ("llama-herding register")
has **0** owner hits. Measured directly with the prototype's own `topic_owners()` at `6e9a30d`:

```
rows 51 distinct_files 36
llama hits: 0
```

Control: the hyphenated variant `t1b-hyphenated.json` — "the llama-herding-register slot is
unbuilt" — is **FRESH**, 0 hits. That is phrasing luck, not a fix: the extractor happens to capture
the whole hyphenated token. The space-separated form is the trap, and it is the ordinary English
form.

### 2.2 Root cause

`E3a` captures exactly one lowercase/hyphen token immediately before `slot|topic`
(`.scratch/ca01/claims-freshness.py:472`):

```python
r"\b(?P<topic>[a-z][a-z-]*)\s+(?:slot|topic)\b[^.;]*\b(?:unbuilt|unowned|empty|unfilled)\b"
```

For "llama-herding register slot", the token before `slot` is `register`; the modifier is dropped.
`topic_owners()` then does a word-boundary header scan for `register` (`:247-272`), which is
semantically unrelated to the claim. The gate asserts a **false ownership fact** and refuses a fresh
claim. This is precisely the failure R02 reproduced at r44 (`reports/round-44/review/R02-review.md`
§1.3) and the fragility X02/S01 named.

Adjacent, same root cause (measured): `.scratch/o09/fixtures/t1c-negation-scope.json` —
`before: "no change to the couples resolver was required at this baseline"` is **not** an absence
premise, but `E1a` mines it as one and `_family_from_phrase` (`:242`) yields
`stem_tokens: ["the", "couples"]`; the stopword `"the"` matches **42** unrelated tools → STALE, exit 2.
A gate that can "flag" on the word "the" is theater-prone in the anti-theater direction too: a
mutation test that only changes a tool name can pass while the mechanism remains unsound.

### 2.3 Required behaviour per contract

The contract does not require prose inference at all: `R01-review.md:245` requires *declared,
machine-readable* per-claim checks; `P01-plan.md:260` forbids mining. The r43 regression that needs
prose today is solved by O05's **explicit probe overlay** for the filed r43 claims. Given that, T1's
required outcomes are:

1. **With a declared check** on the full topic phrase, using the operational `expect` semantics
   (§3.0) — `{"probe_kind":"topic_owner_absent","target":"culture-material:llama-herding register",
   "expect":true}` — measured at `6e9a30d`, 0 owners → predicate holds → **FRESH, exit 0**. This is
   the canonical negative control for the trap: a genuinely fresh claim must not be flagged.
2. **With no checks** — `COULD-NOT-EVALUATE`, exit 3 (P01 pins 3), **never STALE** and never green.
   A refusal that says "add a check" is honest; a refusal that says "your premise is false" is not.
3. **Never** a STALE verdict whose evidence is a generic structural token
   (`register`, `slot`, `topic`, `entry`, `practice`, `system`, `tradition`, `complex`). If a mining
   fallback is retained, the generic-token case must be `COULD-NOT-EVALUATE` with the token named,
   not a verdict.
4. Multi-word topics must be matched as a **phrase/sequence**, not as OR-ed tokens; otherwise
   "llama-herding register" still matches every "register".

### 2.4 Regression guards (must not break while fixing T1)

| guard | required | why |
|---|---|---|
| r43 C | `topic_owner_absent` target `myth-symbol:lithic`, expect `true` → measured owner present → predicate false → **STALE** | `lithic` is specific; mineral-stone-symbolism.md owns it at `7ceff59` (`Ca01-stale-premises.md` §2.2; O05's sidecar at `O05-r43-demo.md:173-175`) |
| r43 Ca | `path_absent reports/round-43/calib/dispositions-r38-r39.json`, expect `true` → absent → **FRESH** | in-file negative control (`O05-r43-demo.md:184-190`) |
| T1 hyphenated | **FRESH**, 0 owners | the phrase is genuinely unowned |
| T1 declared | **FRESH**, 0 owners | forward path for a fresh claim |

A fix that suppresses all `topic_owner_absent` verdicts, or that turns every mined topic into
`COULD-NOT-EVALUATE` including r43 C, fails the positive regression.

---

## 3. Trap T2 — a clause with no declared polarity

### 3.0 Blocking prerequisite: the round states `expect` two incompatible ways

Before any per-clause test, the semantics must be pinned. The r47 artifacts disagree:

| source | wording | consequence for `path_absent` |
|---|---|---|
| `P01-plan.md:243` | "`expect` is the **asserted state** — `false` for 'absent', `true` for 'present/equal'" | `path_absent` + `expect:true` looks **contradictory** |
| `O05-r43-demo.md:99-101,134-136` | boolean types; JSON encodes the r43 Ca absence claim as `path_absent … expect: true`, and r43 C ownership as `topic_owner_absent … expect: true` | `path_absent` + `expect:true` is the **correct** encoding of "the path is absent" |
| `O06-negative-control.md:85` | "`expect` is the asserted measured value of the predicate named by `probe_kind`. Boolean predicates: `true` = the predicate holds, `false` = its negation is the premise." | predicate-truth; resolves the conflict in O05's favour |

This is not a wording quibble: a durable tool built from P01's literal wording would invert every
absence check in O05's sidecar — r43 Ca (`path_absent … expect:true`) would be marked STALE and the
r43 regression would fail in the opposite direction, and C's `topic_owner_absent … expect:true`
would flip to FRESH. `P01-plan.md:269` also makes "missing `expect`" malformed, so the tool cannot
"just infer" the polarity from the kind.

**Rule to pin (operational, matches the authoritative sidecars):** `expect` is the truth value of
the predicate named by `probe_kind`. For `path_absent`, `grep_absent`, `topic_owner_absent`:
`true` = the absence holds. For `path_present`, `grep_present`, `capability_present`: `true` = the
presence holds. For `count_eq`, `sha256_eq`: `expect` is the value itself. Missing `expect`, a null
`expect`, or a value outside the predicate's type is `MALFORMED`.

This also means my first-pass "contradictory polarity" vector (`path_absent` + `expect:true`) is
**not** a contradiction under the operational schema; I withdrew it and replaced it with the
no-expect / null-expect / wrong-type vectors below. Recording the withdrawal matters: a reviewer
following P01's wording would otherwise encode the same mistake.

### 3.1 Measured vectors

The durable schema declares polarity explicitly: `{clause, probe_kind, target, expect,
evidence_command}` — `X00-connector.md:112-119`; `P01-plan.md:243`. A clause without a valid
`expect`, with an unknown `probe_kind`, or with no clause span is **malformed**
(`P01-plan.md:243`; verdict table `:268-269`). The prototype has no such validation. Measured at
`6e9a30d`:

| vector | fixture (`freshness_probes` / prose) | prototype | correct per contract |
|---|---|---|---|
| T2a unknown kind, no polarity | `{"kind":"grep","glob":"…","regex":"llama-herding"}` | **STALE** — `probe error: unknown probe kind: 'grep'`, exit 2 | `MALFORMED`, exit 2, claim `T2a` named; **no verdict** |
| T2b typed kind, no value | `{"kind":"count_eq","glob":"corpus/knowledge/*/*.md"}` | **STALE** — `probe error: 'value'`, exit 2 | `MALFORMED`, exit 2 |
| T2c **no `expect`** | `{"kind":"path_absent","path":"tools/harness/claims-freshness.py"}` | **FRESH** — predicate holds; polarity never consulted, exit 0 | `MALFORMED` — `expect` is mandatory (`P01-plan.md:243,269`) |
| T2d **`expect: null`** | same kind/path, `"expect": null` | **FRESH** — null ignored, exit 0 | `MALFORMED` — null is not a declared polarity |
| T2f **wrong-typed `expect`** | same kind/path, `"expect": "absent"` (string on a boolean predicate) | **FRESH** — string ignored, exit 0 | `MALFORMED` — type is boolean for this predicate (`O05-r43-demo.md:99-101`) |
| T2e explicit empty list | `"freshness_probes": []`, prose `before: "total 223"` | **FRESH** — empty list is falsy, falls back to mining, `count_eq 223` holds, exit 0 | `COULD-NOT-EVALUATE`, non-zero (3); an explicit empty list is a declaration of **no checks**, not permission to mine |

T2e is the direct violation of the round's own threshold: "could-not-evaluate != green (exits
non-zero when no checks declared)" (`reports/round-47/claims.json:47`). The prototype turns an
explicit no-checks claim green. T2c/T2d/T2f are the "no declared polarity" defect in its purest
form: the probe passes because the gate never asked what the clause asserted.

### 3.2 Root cause

1. `declared = claim.get("freshness_probes")` treats `[]` as absent (`:555`), so the empty-list
   declaration silently switches to prose mining.
2. Probe evaluation errors are converted to a failed premise, not a schema rejection
   (`:573-574`):

   ```python
   except (KeyError, ValueError) as exc:
       passed, evidence, detail = False, [], "probe error: %s" % exc
   ```

   A typo in `probe_kind` therefore becomes `STALE` — a false accusation — instead of
   `MALFORMED`.
3. The prototype schema has **no `expect` field at all**; `expect`/`polarity` are inert extra keys.
   T2c/T2d/T2f show the consequence: an undeclared, null, or wrong-typed polarity is not rejected —
   the probe predicate is evaluated on its own and the clause is declared to hold. The gate never
   asked what the clause asserted.

### 3.3 Required behaviour per contract

- Validate the whole claims document **before** evaluating any claim: closed `probe_kind` set
  (`path_absent|path_present|grep_absent|grep_present|count_eq|sha256_eq|topic_owner_absent|
  capability_present`), `expect` present and type-correct under §3.0, `clause_span`/`clause_text`
  matching the claim's `before` bytes, and `evidence_command` present. Any failure → `MALFORMED`
  exit 2, naming the claim id, check id/index and the missing/wrong-typed field. No claim in a
  malformed file receives a FRESH/STALE verdict (`P01-plan.md:269`).
- A missing, null, or wrong-typed `expect` is a schema error, not a verdict. The one behaviour that
  is definitely wrong is the prototype's: evaluate the predicate and return FRESH without ever
  checking the declaration. An undeclared polarity can never make a clause hold.
- Zero premise checks (key absent, empty list, or all clauses marked `context`) →
  `COULD-NOT-EVALUATE`, exit 3, with coverage printed (`premise clauses matched/total`,
  `uncovered`) per `P01-plan.md:245,268`.
- Exit contract: `0` only all-fresh; `1` any stale; `2` malformed; `3` could-not-evaluate
  (`P01-plan.md:266-269`). The prototype uses `1` usage, `2` stale, `3` unverifiable and a flag that
  can make CNE exit 0 — do not inherit any of that numbering. (O10 measured the same inversion
  independently; my T2a/T2b runs confirm the stale-on-malformed half.)

### 3.4 Acceptance

| vector | expected verdict | expected exit | forbidden outcome |
|---|---|---|---|
| unknown `probe_kind` | `MALFORMED` | 2 | STALE; crash/traceback |
| missing `expect` | `MALFORMED` | 2 | FRESH by inferring polarity from the kind |
| `expect:null` | `MALFORMED` | 2 | FRESH |
| wrong-typed `expect` (string for boolean, string for `count_eq`) | `MALFORMED` | 2 | FRESH |
| `freshness_probes: []` / no `before_checks` | `COULD-NOT-EVALUATE` | 3 | FRESH, including via `--allow-unverifiable` |
| valid check, all predicates hold §3.0 | `FRESH` | 0 | — |
| valid check, one mismatch | `STALE` | 1 | 2 |

---

## 4. Trap T3 — `baseline_commit` is a tag, not a sha

### 4.1 Setup (isolated, no lane-repo mutation)

The lane repo has no tags (`git tag -l` → empty), so the test lives in a scratch clone:

```
$ git clone --shared --no-checkout -q . .scratch/o09/tagrepo
$ cd .scratch/o09/tagrepo
$ git tag base-lw 6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe      # lightweight
$ git tag -a base-ann -m 'annotated baseline tag' 6e9a30d…      # annotated
$ git tag base-blob "$(git rev-parse 6e9a30d:corpus/README.md)" # blob
refs/tags/base-ann  tag     43fe2a8cb3cf20bc6964f7c72637034db904a395
refs/tags/base-blob blob    a0fd64c5600ede3668038ba97340fff9192b7af2
refs/tags/base-lw   commit  6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
```

Key resolution fact:

```
$ git rev-parse base-ann            → 43fe2a8cb3cf20bc6964f7c72637034db904a395   (the TAG object)
$ git rev-parse --verify base-ann^{commit}
                                    → 6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe   (the COMMIT)
$ git rev-parse base-lw             → 6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe   (commit; lightweight)
$ git rev-parse --verify base-blob^{commit}
                                    → fatal: … object dereferences to blob type (exit 128)
```

`git ls-tree`/`git show` do peel an annotated tag to its tree, so **measurement** at a tag is
usually correct; the defect is the **identifier reported and pinned**.

### 4.2 Measured (prototype, `--root .scratch/o09/tagrepo`)

Each fixture declares `count_eq corpus/knowledge/*/*.md = 223` plus a `grep_present` read, so the
tag's tree must be both listed and read.

| baseline | prototype output | exit | defect |
|---|---|---|---|
| `base-lw` (lightweight → commit) | `round 999 baseline 6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe (git)`; FRESH 2/2 | 0 | none; correct |
| `base-ann` (annotated tag) | `round 999 baseline 43fe2a8cb3cf20bc6964f7c72637034db904a395 (git)`; FRESH 2/2 | 0 | **reports the tag object as the baseline**, not the commit; the pin is not a commit sha. Measurement happened to be right because git peels for `ls-tree`/`show` |
| `base-blob` (tag → blob) | `claims-freshness: git ls-tree -r --name-only base-blob failed: fatal: not a tree object` | **1** | unresolvable/non-commit baseline is a usage error, not `MALFORMED` (2); no claim verdict, but wrong class |
| `deadbeef00` (missing rev) | `… failed: fatal: Not a valid object name deadbeef00` | **1** | as above |
| `HEAD:corpus/README.md` (blob object expression) | `… failed: fatal: not a tree object` | **1** | as above |
| `6e9a30d^{tree}` (tree, not commit) | `round 999 baseline 765306d294a2f0d6634cfbb15380bcdfd30144cf (git)`; FRESH | **0** | **silently accepts a tree as the baseline** and pins a tree sha; a provenance hole |
| `base-lw` with a branch of the same name pointing at `c9f4eaa` | `git rev-parse` warns `refname 'base-lw' is ambiguous`; resolves the **tag** (6e9a30d) and exits 0 | 0 | ambiguity is discarded; the evaluated commit depends on git's tag-over-head precedence, not on an unambiguous declaration |

`resolve_tree` is the source (`:612-618`): `git rev-parse <commit>` with no `^{commit}` and no
object-type check; errors surface as `RuntimeError` → exit 1 in `main`, while the prototype's `2` is
already taken by STALE.

### 4.3 Required behaviour per contract

`R01-review.md:245` requires evaluation "at the claim's own `baseline_commit` via `git
ls-tree`/`git show`, never against the worktree". For a tag, the only reproducible reading is:

1. Resolve the declared rev to a **commit**: `git rev-parse --verify --quiet "<rev>^{commit}"`.
2. Accept a tag **iff** it resolves unambiguously to exactly one commit; evaluate at that commit's
   tree.
3. Report **both** `baseline_declared` (the tag/text as written) and `baseline_resolved` (the 40-hex
   **commit**). `baseline_resolved` must never be a tag, tree, or blob object sha.
4. Reject as `MALFORMED` exit 2, with a named reason and no claim verdict: missing rev, non-commit
   rev (blob/tree), and **ambiguous** rev (tag and branch with the same name) — do not rely on git's
   precedence. An ambiguity warning on stderr is not a resolution policy.
5. No fallback to the worktree (`None`/empty/`worktree` must not be a silent baseline); missing
   `baseline_commit` is malformed (`P01-plan.md:269`).
6. A tag that moves between runs changes `baseline_resolved`; because both values are printed, a
   re-run can detect the drift. (Optional hardening: pin `baseline_resolved_sha256` in the report.)

Acceptable alternative policy: reject **all** tag/rev inputs as non-sha (`MALFORMED` exit 2). That is
stricter than the contract but not dishonest. What is not acceptable is the prototype's middle:
evaluate the tree, print a non-commit identifier, and call it green.

### 4.4 Acceptance

| vector | expected | forbidden |
|---|---|---|
| lightweight tag → commit | FRESH/STALE per checks, `baseline_resolved` = `6e9a30d…`, exit 0/1 | tag/other sha reported |
| annotated tag → commit | same; `baseline_resolved` = `6e9a30d…` (peeled), `baseline_declared` = `base-ann`, exit 0/1 | `43fe2a8…` as the resolved baseline |
| tag → blob | `MALFORMED`, exit 2, named object type | exit 1; FRESH; worktree fallback |
| missing rev | `MALFORMED`, exit 2 | exit 1; worktree fallback |
| `6e9a30d^{tree}` | `MALFORMED`, exit 2 (not a commit) | FRESH with a tree sha |
| ambiguous tag+branch | `MALFORMED`, exit 2, ambiguity named | silent precedence |
| tag with all checks holding | exit 0 only if every claim is fresh and has ≥1 premise check | CNE made green |

---

## 5. Cross-cutting findings

1. **Exit numbering is inverted relative to the contract** (independently measured by O10; confirmed
   by my runs). Prototype: `1` usage, `2` stale, `3` unverifiable, and `--allow-unverifiable` can make
   CNE exit 0. Contract: `0` fresh, `1` stale, `2` malformed, `3` CNE (`P01-plan.md:266-269`). Every
   trap test must assert the contract codes, not the prototype's.
2. **`expect` polarity is stated two incompatible ways** (§3.0). P01:243 says `false` = absent;
   O05's sidecar encodes `path_absent … expect:true` for absence; O06:85 says `true` = the predicate
   holds. This is the highest-risk finding in this seat's remit because it is a **global inversion**,
   not a per-clause typo: a tool built from P01's literal wording would flag r43 Ca (a true premise)
   as STALE and flip O05's C ownership check, while still passing its own selftest. The durable tool
   must pin predicate-truth semantics in its docstring and its schema, and O05/O06's fixtures are the
   tie-breaker because they are the executable sidecars.
3. **The r47 claims file has no `before_checks`.** Run on `6e9a30d`:
   `[C] FRESH (1/1)` (only the literal "total 223" is mined; the cartography clause is `ungrounded`),
   `[O] UNVERIFIABLE (0/0)`, `[Ca] UNVERIFIABLE (0/0)`, exit 3. The gate never checks the round's
   actual coverage premise — evidence that prose mining cannot bind a coverage claim. For r48+,
   claims must carry the sidecar checks the gate consumes; for r47 the declaration predates the tool,
   so this is a forward requirement, not a retroactive failure.
4. **Prototype selftest is red 17/19**, exit 1: `FAIL grep_absent hit fails` uses a nonexistent
   `corpus/knowledge/beta/*.md` fixture (`:791`), and `FAIL seventeen checks collected (18)` is a
   stale count assertion (`:876`). The durable tool must ship green; a red selftest plus the T1/T2
   failures is not a shippable gate.
5. **Anti-theater warning.** T1c shows a token-based mechanism can "flag" on the stopword "the" and
   find 42 candidates. O07's mutation test should include a **non-claim generic word** in the family
   phrase, not only a renamed tool, or a two-string lookup can pass it. The contract's anti-theater
   intent (`capability_present` resolved through a registry, `P01-plan.md:260`) is the right fix;
   mining cannot supply it.
6. **Measurement vs provenance.** The annotated-tag run is the cleanest example: the verdict is
   correct, the pin is wrong. A gate can pass its verdict tests and still lose the r43 baseline-drift
   property if `baseline_resolved` is not a commit. Trap T3 must be judged on the **reported
   identifier**, not only on the verdict.

---

## 6. Acceptance matrix for the durable tool (ready to run)

Run from the lane root with the landed tool. `$TOOL=tools/harness/claims-freshness.py`.

| id | fixture semantics | command | expected verdict | expected exit |
|---|---|---|---|---|
| T1a | prose "llama-herding register slot is unbuilt", **no checks** | `python3 -B $TOOL --claims <t1-prose>.json` | `COULD-NOT-EVALUATE` (not STALE) | 3 |
| T1b | same claim, `topic_owner_absent` target **`culture-material:llama-herding register`**, expect **true** | `python3 -B $TOOL --claims <t1-checked>.json` | `FRESH` | 0 |
| T1c | same claim, target **`culture-material:register`** (the false-positive vector) | `python3 -B $TOOL --claims <t1-generic>.json` | must **not** be FRESH; `STALE` only if the tool explains the generic-token match — the contract-compliant outcome for a generic-only target is `MALFORMED`/`COULD-NOT-EVALUATE` | not 0 |
| T1d | r43 C sidecar: `myth-symbol:lithic`, expect **true** | `python3 -B $TOOL --claims reports/round-43/claims.json --checks <r43-sidecar>` | `STALE` | 1 |
| T1e | r43 Ca sidecar: dispositions path absent, expect **true** | same file | `FRESH` | — |
| T2a | unknown `probe_kind` | `python3 -B $TOOL --claims <t2-unknown>.json` | `MALFORMED` | 2 |
| T2b | `count_eq` missing `expect`/value | same | `MALFORMED` | 2 |
| T2c | `path_absent` with **no `expect`** | same | `MALFORMED` | 2 |
| T2d | `expect: null` | same | `MALFORMED` | 2 |
| T2f | `expect: "absent"` on a boolean predicate | same | `MALFORMED` | 2 |
| T2e | explicit empty checks / no `before_checks` | same | `COULD-NOT-EVALUATE` | 3 |
| T3a | `baseline_commit: base-lw` (lightweight) | `python3 -B $TOOL --claims <t3-lw>.json --root <tagrepo>` | FRESH, resolved commit | 0 |
| T3b | `baseline_commit: base-ann` (annotated) | same | FRESH, resolved **commit** `6e9a30d…` | 0 |
| T3c | `baseline_commit: base-blob` | same | `MALFORMED` | 2 |
| T3d | missing rev / `HEAD:path` | same | `MALFORMED` | 2 |
| T3e | `6e9a30d^{tree}` | same | `MALFORMED` | 2 |
| T3f | ambiguous tag+branch | same | `MALFORMED` | 2 |

The prototype-schema fixture files used for the measured rows are in `.scratch/o09/fixtures/`
(ephemeral); the exact JSON for the load-bearing ones is reproduced in Appendix A. The tag repo can
be recreated by the commands in §4.1. If the round wants durable fixtures, the integrator should
copy the Appendix JSON into `reports/round-47/calib/fixtures/` — this seat does not write outside
its out path.

**Contract-shaped example (T1b), operational sidecar semantics.** `before` must contain the clause;
the sidecar check is `{clause_id, clause_span, clause_text, probe_kind: "topic_owner_absent",
target: "culture-material:llama-herding register", expect: true, evidence_command: "git grep … at
6e9a30d"}`. Measured at `6e9a30d`: 0 owner hits → the predicate holds → FRESH. Replace `target`
with `culture-material:register` and the same probe measures 51 hits → predicate false → mismatch;
that is the vector a naive tool turns into STALE, and the vector a correct tool either rejects
(generic target) or reports with a named generic-token reason. The exact `target` syntax
(`partition:topic`, as in O05) is **to-verify** against O02's landed schema.

---

## 7. Per-clause disposition for claim O (this seat's remit)

The O claim's `after_required` (`reports/round-47/claims.json:41`) and thresholds (`:47`) name five
testable properties. My judgment on each at this cut:

| property | status | basis |
|---|---|---|
| durable `tools/harness/claims-freshness.py` | **could-not-evaluate** | absent at cut; prototype is `.scratch` only |
| green selftest | **could-not-evaluate** for the deliverable; prototype **FAIL** 17/19 | §5.4 |
| flags r43 O and C stale + Ca fresh | **reproduced on the prototype** (O 0/2, C 2/3, Ca 1/1, exit 2); durable run **could-not-evaluate** | §0, §1 |
| does not flag a fresh claim (negative control) | **prototype FAIL on the novel-phrasing fresh claim** (T1 STALE); groundable count control passes | §2 |
| anti-theater mutation still flags | **not testable at cut** (O07 absent); T1c shows the mining path is theater-prone | §5.5 |
| exit non-zero on stale; CNE ≠ green | prototype exits 2 on stale (non-zero, but wrong code); **CNE can be made green** via `--allow-unverifiable`; empty declared list → green | §3.1, §5.1 |
| polarity semantics unambiguous | **FAIL at the artifact level** — P01 vs O05/O06 (§3.0); prototype has no `expect` at all | §3.0 |

**Named-verifier judgment.** No axis is **harmed**: the durable artifact is absent, not wrong on
disk, and nothing in the corpus/ledgers changed. The trap-handling clause is **unproven** at cut;
the only extant implementation is **nonconforming** on all three trap families in the ways measured
above, and the schema itself is ambiguous on polarity. The fix is mechanical and already specified
by P01 plus §3.0: declared checks, schema validation before evaluation, `^{commit}` resolution with
both identifiers reported, and the 0/1/2/3 exit table. The acceptance matrix in §6 is the bar for
O08/V02.

---

## 8. Evidence ledger

**Subject**
- `.scratch/ca01/claims-freshness.py` — sha256 `dd88d9e12bda5ade6b4f93864db138e0a5ce54b0ef5cbcf6e4f5050783121434`
- Prototype selftest: `selftest 17/19 FAIL`, exit 1 (failures at `:791`, `:876`)
- Prototype r43 run: `1 fresh, 2 stale, 0 unverifiable, 2 ungrounded`, exit 2
- Prototype r47-claims run: `1 fresh, 0 stale, 2 unverifiable, 5 ungrounded`, exit 3
- Prototype CNE escape hatch: `--allow-unverifiable` on the r47 claims → exit 0

**Fixtures run** (all under `.scratch/o09/fixtures/`, prototype schema; sha256 recorded in the run log):
`t1-llama-novel`, `t1b-hyphenated`, `t1c-negation-scope`, `t2a-unknown-kind`, `t2b-count-no-value`,
`t2c-no-expect`, `t2d-null-expect`, `t2f-wrong-type-expect`, `t4-empty-declared`, `control-count223`,
`t3-lw`, `t3-ann`, `t3-blob`, `t3-missing`, `t3-blobpath`, `t3-treerev`.

**Tag refs (scratch clone only)**
- lightweight `base-lw` → `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe`
- annotated `base-ann` → tag object `43fe2a8cb3cf20bc6964f7c72637034db904a395`, peeled commit `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe`
- blob `base-blob` → `a0fd64c5600ede3668038ba97340fff9192b7af2`
- tree rev `6e9a30d^{tree}` → `765306d294a2f0d6634cfbb15380bcdfd30144cf`

**Contract citations**
- `reports/round-44/review/R01-review.md:245-246` — closed probe set, baseline evaluation, exit codes
- `reports/round-47/plan/P01-plan.md:243` — `expect` declared, unknown kind/missing expect/no clause span = malformed
- `reports/round-47/plan/P01-plan.md:245,266-269` — coverage, verdict and exit table (0/1/2/3)
- `reports/round-47/cross/X00-connector.md:108-119` — encoding rule; `expect` is the measured state
- `reports/round-47/op/O05-r43-demo.md:99-101,134-136,173-175` — operational `expect` encoding (`path_absent … expect:true`; `topic_owner_absent … expect:true`)
- `reports/round-47/op/O06-negative-control.md:85` — predicate-truth semantics ("true = the predicate holds")
- `reports/round-47/claims.json:41,47` — the O claim's thresholds, including "could-not-evaluate != green"
- `reports/round-47/op/O10-exit-codes.md` (independent exit-code verification) and `O13-probe-coverage.md` (independent unknown-kind/probe-coverage verification) — corroboration, not relied on for my numbers

**Write surface.** This file is the only write outside `.scratch/o09/`. No filed byte edited; no
corpus staging; no ref/commit/push/network operation; no in-tree `run-validation.py`. The scratch
clone's refs live only under `.scratch/o09/tagrepo`.

---

## Appendix A — load-bearing fixtures (exact bytes)

**A1. T1 novel phrasing (no checks) — `t1-llama-novel.json`**

```json
{"round": 999, "baseline_commit": "6e9a30d", "claims": [{
  "id": "T1", "axis": "coverage",
  "before": "the llama-herding register slot is unbuilt and has no owner",
  "after_required": "corpus/knowledge/culture-material/llama-herding.md lands",
  "counting_commands": []}]}
```

**A2. T2c no declared polarity — `t2c-no-expect.json`**

```json
{"round": 999, "baseline_commit": "6e9a30d", "claims": [{
  "id": "t2c-no-expect", "axis": "coverage", "before": "probe declared",
  "after_required": "x",
  "freshness_probes": [{"kind": "path_absent",
    "path": "tools/harness/claims-freshness.py"}]}]}
```

The null and wrong-type variants are the same file with `"expect": null` and `"expect": "absent"`;
the prototype returns FRESH for all three.

**A3. T2e explicit empty checks — `t4-empty-declared.json`**

```json
{"round": 999, "baseline_commit": "6e9a30d", "claims": [{
  "id": "T4", "axis": "calibration", "before": "total 223",
  "after_required": "x", "freshness_probes": []}]}
```

**A4. T3 annotated tag — `t3-ann.json`**

```json
{"round": 999, "baseline_commit": "base-ann", "claims": [{
  "id": "t3-ann", "axis": "coverage", "before": "tag baseline holds 223 entries",
  "after_required": "x",
  "freshness_probes": [
    {"kind": "count_eq", "glob": "corpus/knowledge/*/*.md", "value": 223},
    {"kind": "grep_present", "glob": "corpus/README.md", "regex": "^# "}]}]}
```

The other fixtures differ only in the fields named in §3.1 and §4.2; all are one-claim files with
the same shape.
