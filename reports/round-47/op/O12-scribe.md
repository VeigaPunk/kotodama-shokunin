# O12 — O-claim scribe: the freshness-gate evidence chain, integration-ready

- Seat: `O12` | role scribe | claim **O** | round 47, loop 2
- Out path: `reports/round-47/op/O12-scribe.md` (the only file this seat writes)
- Baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`); declared `6e9a30d` (`reports/round-47/claims.json:7`); both baselines under test are ancestors of HEAD (`7ceff59`, `c9f4eaa`; `git merge-base --is-ancestor` → yes)
- Observation cut: **2026-10-19T18:10Z** (UTC); first cut 18:03Z. O01 and O03 landed at 18:06–18:07Z and are folded into §0/§5/§8; the wave was in flight. §8 records the final snapshot.
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root.
- Boundary: no filed byte edited; no corpus staging or write; no `reports/round-*/run-validation.py`; no git commit/push/install/network. The evaluator in Appendix A lives only in `.scratch/o12/`.

## 0. Bottom line

**The evidence chain is assembled but not closed.** The method is proven and the expected verdicts are measured independently; the deliverable — a durable `tools/harness/claims-freshness.py` with a green selftest and a filed `calib/` demonstration — does not exist at this cut.

| link the O claim requires | evidence at cut | status |
|---|---|---|
| defect statement (R01-43-12) | `reports/round-43/review/R01-review.md:400`; `reports/round-46/loop-1-retrospective.md:43-54` | **solid** |
| method proof | r44 prototype `dd88d9e1…`; seat reference evaluators O05 `008e0365…`, O06 `4209154c…` | **solid as method, partial as delivery** |
| baseline facts | §2 (this seat) + `op/O05-r43-demo.md` §2 + `calib/Ca05-verify.md` §1.1, measured independently | **solid** |
| durable tool `tools/harness/claims-freshness.py` | absent (`ls` → no such file) | **absent** |
| green selftest | prototype `--selftest` 17/19 FAIL, exit 1; no O04 artifact | **absent** |
| r43 positive regression | reference evaluators flag O STALE and C STALE, leave Ca FRESH; expected exit 1 (O05 §4); prototype exit 2 | **partial** — not the durable path |
| negative control | 3/3 claims, 9/9 clauses fresh, exit 0; fixture sha `38857b08…` (O06 §3); discriminates at HEAD | **partial** — not the durable path |
| anti-theater mutation | `op/O07-anti-theater.md` absent; this seat's independent mutation still flags (§4.3) | **absent as an artifact** |
| trap handling T1–T3 | prototype FAILS all three families (`op/O09-traps.md:23-31`); durable handling unmeasured | **absent** |
| verifier set | O09/O10/O13 filed; O08/O11/O14/O15 absent | **partial** |
| landing spec | `op/W01-landing-spec.md` absent; this seat supplies the apply contract (§6) | **absent** |
| filed demonstration under `calib/` | absent | **absent** |
| Ca handoff | `calib/Ca06-queue-successor.md` rows `r43-stale-premises` routed to this tool, reclass gates G1–G8 | **solid** |

**Candidate axis verdict: `unprovable-but-better`, not `improved`.** The defect is confirmed, the method is proven, the fixtures and expected outputs are ready, and no axis is harmed. The O claim's thresholds (`reports/round-47/claims.json:47`) require a durable tool with a green selftest, the four demonstrations, and `could-not-evaluate != green`; none of those can be certified from the artifacts that exist at this cut.

**The r47 O claim's own `before` is fresh.** At `6e9a30d` there is no `tools/harness/claims-freshness.py`; the only gate bytes are the untracked `.scratch/ca01/claims-freshness.py` (`git ls-files` → not tracked), whose selftest is red at 17/19. The round does not repeat the stale-premise defect it is fixing.

## 1. What claim O requires

From `reports/round-47/claims.json:37-47`:

- **claim**: land a durable pre-dispatch gate that, given a `claims.json` + `baseline_commit`, re-derives each claim's `before` at that commit (via `git show`/`ls-tree`, never the worktree) using typed per-clause probes with declared polarity; flags STALE if any declared clause contradicts the asserted `before`; exits non-zero on stale.
- **after_required** (`:41`): `tools/harness/claims-freshness.py` durable with a green selftest; flags r43 O and C stale + Ca fresh; does not flag a fresh claim; still flags under an anti-theater mutation; a filed demonstration at `reports/round-47/calib/`; exit non-zero on stale.
- **thresholds** (`:47`): selftest green; correct r43 flags; negative control not flagged; mutation still flags; durable not `.scratch`; `could-not-evaluate != green` (non-zero when no checks are declared).
- **defect**: `R01-43-12` — "The claim texts were not re-measured at `7ceff59` before dispatch" (`reports/round-43/review/R01-review.md:400`); carried in `reports/round-46/loop-1-retrospective.md:45-48`.
- **contract**: `reports/round-44/review/R01-review.md:243-250` (six-part minimum), exit codes at `:246`.
- **calibration handoff**: `reports/round-47/calib/Ca06-queue-successor.md` row `r43-stale-premises`, class `routed-with-owner`, owner "r47 O claim (freshness-gate author) + integrator"; reclass only when gates G1–G8 pass.

## 2. Measured anchors (this seat's own commands)

Every value below was read from committed bytes, not from another seat's summary.

### A1 — HEAD and partition

```
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ find corpus/knowledge -name '*.md' | wc -l
223
$ for p in civilizations culture-material linguistics myth-symbol synthesis verification; do
    printf '%-16s %s\n' "$p" "$(ls corpus/knowledge/$p/*.md | wc -l)"; done
civilizations    94
culture-material 25
linguistics      25
myth-symbol      26
synthesis        29
verification     24
```

`reports/round-47/claims.json` sha256 `7eb16979…`; `targets.json` sha256 `d60e5572…` — both match `reports/round-47/telemetry/dispatch-declared.json`.

### A2 — r43 baseline `7ceff59` (the regression)

```
$ git ls-tree -r --name-only 7ceff59 -- corpus/knowledge | grep -c '\.md$'
223
$ git ls-tree -r --name-only 7ceff59 -- corpus/knowledge/myth-symbol | grep -c '\.md$'
26
$ git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1  -
$ git cat-file -e 7ceff59:tools/harness/basename-couples-resolver.py; echo $?
fatal: path 'tools/harness/basename-couples-resolver.py' exists on disk, but not in '7ceff59'
128
$ sha256sum reports/round-43/claims.json
9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b
```

`corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` exists at `7ceff59`; its H1 names "the lithic register" and its `- topic:` line at `:5` owns the register. So r43 O's `before` (`claims.json:27`) is false (a tracked couples resolver exists; it reads the wrapped field 4/4), and r43 C's `before` (`:40`) is false in its ownership conjunct while its counts 26/223 are true.

**Constraint discovered by O05 and confirmed here:** `reports/round-43/` does not exist at `7ceff59` at all. The gate cannot read the claims file via `git show <baseline>:reports/round-43/claims.json`; it must read the claims/annotation file from the worktree and use the baseline commit only as the measurement tree (`op/O05-r43-demo.md` §2).

### A3 — r44 baseline `c9f4eaa` (the negative control)

```
$ git ls-tree -r --name-only c9f4eaa -- corpus/knowledge | grep -c '\.md$'
223
$ git show c9f4eaa:tools/harness/couples-reference-extractor.py | sha256sum
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1
$ git grep -l -E 'four_class|four-class census|four-class authority' c9f4eaa -- tools/
(no output)
$ sha256sum reports/round-44/claims.json
5bd54b714bd5238c2f8494e1c17b3126de000bdc1d3bbbdd9333f8e8bb5c06e8
```

No four-class census authority exists at `c9f4eaa`; the witness is the only couples resolver. r44 O's `before` (`claims.json:27`) is true, C's `before` (`:40`) is true, Ca's `before` (`:52`) is true.

### A4 — no filed claims file declares probes

```
$ grep -rl 'freshness_probes\|before_checks' reports/round-*/claims.json
(no output)
```

No round's `claims.json` has a probe field. The r43/r44 demonstrations therefore require an **annotation copy or sidecar**, never an edit of the filed claims. O05's annotated copy and O06's fixture are the two filed examples.

### A5 — the only extant implementation

```
$ sha256sum .scratch/ca01/claims-freshness.py
dd88d9e12bda5ade6b4f93864db138e0a5ce54b0ef5cbcf6e4f5050783121434
$ python3 -B .scratch/ca01/claims-freshness.py --selftest; echo exit=$?
FAIL  grep_absent hit fails
FAIL  seventeen checks collected (18)
selftest 17/19 FAIL
exit=1
$ python3 -B .scratch/ca01/claims-freshness.py --claims reports/round-43/claims.json; echo exit=$?
[O] operability -- STALE (0/2 premises hold)
[C] coverage -- STALE (2/3 premises hold)
[Ca] calibration -- FRESH (1/1 premises hold)
summary: 1 fresh, 2 stale, 0 unverifiable, 2 ungrounded clause(s)
REFUSE: claims O, C have a `before` already false at 7ceff59…; do not dispatch.
exit=2
```

The flags are correct; the selftest and exit codes are not the contract. The prototype is untracked (not durable).

### A6 — capability at HEAD (context, not baseline)

```
$ python3 -B tools/harness/basename-couples-resolver.py --selftest
SELFTEST OK: 27/27 controls
exit=0
$ grep -n 'four_class_totals' tools/harness/basename-couples-resolver.py | head -1
260:        "four_class_totals": four,
```

At HEAD the four-class capability exists; at `c9f4eaa` it does not. A gate that measures HEAD instead of `baseline_commit` turns the r44 negative control into a false STALE — measured in §4.5.

### A7 — cartography is still unowned at HEAD (cross-claim context)

```
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr)' corpus/knowledge/ | wc -l
0
$ grep -rliE 'cartograph|mapmaking' reports/round-*/scout/ | sort
reports/round-44/scout/K02-gap-scout.md
```

The only prior-round cartography proposal is the r44 K02 seed; it is not a carried topic in the R42-R2 sense. This is C's concern, recorded here only because the O demo must not accidentally evaluate a 224 tree.

## 3. Contract synthesis

This is the contract the durable tool must implement; it reconciles the claim, the r44 six-part minimum, and the filed fragments O05/O06/O09/O10/O13.

### 3.1 Inputs and baseline semantics

- Input: a claims file (worktree path) with `baseline_commit` and per-claim `before_checks` (inline) or an attached checks sidecar keyed by claim id.
- `baseline_commit` may be a full sha, short sha, or tag. Resolve `git rev-parse <rev>^{commit}`; record both the declared string and the resolved 40-hex commit. A tag-to-blob, tree, missing rev, or ambiguous rev is **malformed**, exit 2 — never a worktree fallback (O09 T3).
- Measure with `git ls-tree`/`git show` at the resolved commit only. Never read corpus or tool bytes from the worktree. The one worktree read is the claims/annotation file itself (A2 constraint).
- Read-only: no writes to the repo; stdout/JSON only.

### 3.2 Check schema

Each check is `{clause, probe_kind, target, expect, evidence_command}` (the schema used by O05 §3, O06 §3, and `reports/round-44/review/R01-review.md:245`).

- `clause` quotes the premise span being tested.
- `probe_kind` is from the closed set in §3.3.
- `target` is the measured object: a path, a glob, `<partition>:<topic>`, a named capability, or `path::regex` for a capability scoped to one blob.
- `expect` is the **asserted measured value of the predicate**, with explicit polarity:
  - boolean probes: `true` = predicate holds, `false` = its negation is the premise (e.g. `path_absent` + `expect:true` means "the path is absent"; `capability_present` + `expect:false` means "the capability is absent");
  - `count_eq`: integer;
  - `sha256_eq`: lowercase hex string.
- A missing `expect`, `expect:null`, a contradictory encoding, or an unknown `probe_kind` is **malformed** (exit 2), never a verdict.

### 3.3 Probe registry (eight contract kinds)

| probe_kind | measured value | example |
|---|---|---|
| `path_absent` | boolean: path absent at baseline | `tools/harness/basename-couples-resolver.py` at `7ceff59` → true |
| `path_present` | boolean: path present | witness `tools/harness/couples-reference-extractor.py` at `7ceff59` → true |
| `grep_absent` | integer hits over a scope | 0 hits for a named sentence |
| `grep_present` | integer hits over a scope | ≥1 hit |
| `count_eq` | integer matched by a shell-style glob (no `**`; `*` does not cross `/`) | `corpus/knowledge/*/*.md` → 223 |
| `sha256_eq` | blob digest at baseline | witness → `d8d23a26…` |
| `topic_owner_absent` | boolean: no entry in the partition owns the topic (H1 + `- topic:` scan only) | `myth-symbol:lithic` at `7ceff59` → false (owned) |
| `capability_present` | boolean: a declared capability is present (named registry or `path::regex`) | `couples-policy-durable` at `7ceff59` → true |

The r47 claim names seven kinds (omits `grep_present`); the r44 contract names eight. **Implement all eight** — the claim's seven are a subset, and O13's coverage check (`op/O13-probe-coverage.md` §2.3) recommends the eight-kind reading. Accept legacy aliases (`topic_unowned` → `topic_owner_absent`, `tool_family_absent` → `capability_present` with `expect:false`) for the prototype-era fixtures, but emit the contract names.

### 3.4 Verdict and exit contract

- A claim is `FRESH` iff every declared check holds; `STALE` if any check mismatches (report each failing clause with measured vs expected); `COULD-NOT-EVALUATE` if no checks are declared.
- Exit: **0** all fresh; **1** any stale; **2** malformed input; **3** any could-not-evaluate (and no stale). `could-not-evaluate` is never 0, including under any `--allow-unverifiable` flag (remove the flag or make it still exit non-zero; O09 T2e, `op/O10-exit-codes.md` §1).
- The prototype's numbering is inverted (stale→2, usage→1, C-N-E→0 under a flag). Do not copy it.
- JSON output must include per-check `{claim, clause, probe_kind, target, expect, measured, holds, evidence_command}` and the resolved baseline commit; the verdict must be reproducible from that object (O14 determinism).

### 3.5 Prose miner (fallback for unannotated claims)

The bare counting command `python3 tools/harness/claims-freshness.py --claims reports/round-43/claims.json` must work without a sidecar. That requires a conservative fallback miner over `before` prose, with these rules:

- A mined premise is authoritative only when the topic is a distinctive multi-token phrase or a known register term. A generic token (`register`, `slot`, `system`) yields **could-not-evaluate**, never a false ownership fact (O09 T1: "llama-herding register slot" must not become `register` → 51 owners → STALE).
- Capability extraction must measure a tool family, not a literal tool name (so the anti-theater mutation survives).
- Ungrounded clauses are reported with the claim id as owner and never treated as fresh.
- The miner must reproduce r43 O STALE, C STALE, Ca FRESH; if it cannot, it must return could-not-evaluate for that claim rather than a guessed verdict.

### 3.6 Capability registry and anchored signatures

A registry-wide capability scan must use anchored signatures. Two measured false positives from a loose scan (this seat, §4.5):

- `four[ _-]class` + `census` matched `tools/harness/receipt_guard_adoption.py:1192` (`"live-declared-hazard-four-classified"`), which is a runner census, not a couples four-class census. At `c9f4eaa` this wrongly makes the r44 negative control STALE.
- The fix: require `four[_-]class[ _-]+(totals|census|authority)` (the successor uses `four_class_totals`, `tools/harness/basename-couples-resolver.py:260`) and exclude `tools/gates/frozen/**`. At `c9f4eaa` the anchored scan returns 0 candidates; at HEAD it returns the successor.

Named capabilities in the O05 fixture: `couples-policy-durable` (a tracked `tools/harness/*.py` defines `couples_block(`, `field_refs(`, `classify(` and reads the baseline wrapped field 4/4) and `couples-wrapped-field-whole` (the same measurement reported as 4/4, not 0/4). Implement them as declared, auditable registry entries — not as substring searches over claim prose.

### 3.7 Topic-ownership probe

Scan only the entry's H1 and `- topic:` line at the baseline; use word-boundary matching. Measured false positives without boundaries:

- `gem` matches inside "Judgment Machines" (`myth-symbol/death-afterlife-eschatology.md:1`);
- `stone` matches "Deucalion's stones" (`myth-symbol/flood-traditions.md:3`).

With `\b(?:lithic|lapidary|mineral|gem|stone|metal)\b`, both disappear; only `mineral-stone-symbolism.md` owns the lithic register. The probe may accept a curated synonym set, but a generic token must be rejected as non-measuring (could-not-evaluate), not turned into an owner fact.

### 3.8 Read-only guarantee

The tool must not write under `reports/`, `corpus/`, `tools/`, or `.scratch`; the demonstration artifact is written by the integrator, not the gate. It must not mutate refs or run a round runner.

## 4. Demonstration set and expected results

### 4.1 r43 positive regression (O05, authoritative fixture)

Byte source: `reports/round-47/op/O05-r43-demo.md` §3, fenced annotated copy of `reports/round-43/claims.json` with `before_checks` added. Proposed extraction target: `reports/round-47/calib/r43-claims-annotated.json`.

Expected (O05 §4, reference evaluator `008e0365…`):

| claim | verdict | mismatching clauses | exit |
|---|---|---|---|
| O | **STALE** (2/3) | durable couples capability present; wrapped field reads 4/4 | — |
| C | **STALE** (2/4) | `mineral-stone-symbolism.md` present; lithic topic owned | — |
| Ca | **FRESH** (0/1) | — | — |
| all | **NOT GREEN** | — | **1** |

A literal-path gate passes O (the successor path is absent at baseline); the capability probe is what flags it. That is the anti-theater property in miniature (O05 §5.1).

### 4.2 Negative control (O06, authoritative fixture)

Byte source: `reports/round-47/op/O06-negative-control.md` §3, canonical fixture sha256 `38857b08543964cf2fd4a0154412279803043997d86fdcab1b2ce20499d4df1c` (5031 bytes). Proposed extraction target: `reports/round-47/calib/negative-control.claims.json`.

Expected (O06 §1, reference evaluator `4209154c…`): **3/3 claims fresh, 9/9 clauses hold, exit 0**. At HEAD the same fixture must turn claim O STALE because `basename-couples-resolver.py` landed — the discriminator that proves baseline scoping.

### 4.3 Anti-theater mutation (O07, owed)

No `op/O07-anti-theater.md` at this cut. This seat's independent mutation (§4.5) removes the literal successor path from O's checks and paraphrases C's ownership terms (`lithic` → `stone|gem|metal`); both claims still flag STALE from capability/ownership. The durable tool's acceptance condition: after replacing every literal tool name in the claim prose and annotation with a non-existent name, the verdict is unchanged; the flag must come from a measured capability or a scanned corpus header, not from a string comparison with the claim.

### 4.4 Trap matrix (O09, acceptance-ready)

`op/O09-traps.md:350-370` supplies the fixtures and expected outcomes. The durable tool must satisfy:

| trap | required outcome | forbidden |
|---|---|---|
| T1 novel phrasing "llama-herding register slot is unbuilt", no checks | could-not-evaluate (exit 3), or FRESH if the full phrase measures unowned | false STALE from the generic token `register` |
| T1 checked `topic_owner_absent` target `llama-herding register` | FRESH, exit 0 | — |
| T2 unknown `probe_kind`, missing `expect`, `expect:null`, contradictory polarity | malformed, exit 2 | FRESH by inferring polarity; traceback |
| T2 `freshness_probes: []` / no checks | could-not-evaluate, non-zero | FRESH via mining |
| T3 annotated tag | resolved commit reported; FRESH/STALE per checks | tag-object sha reported as baseline |
| T3 tag→blob, tree rev, missing rev | malformed, exit 2 | exit 1; FRESH; worktree fallback |

The prototype fails every family (`op/O09-traps.md:23-31`), so its body cannot be shipped unmodified.

### 4.5 This seat's independent cross-check

Scratch evaluator: `.scratch/o12/probe-check.py`, sha256 `0f540f2e1e18acb46cfd1b8dea09d1f295101a5a140d9dee323c7caeb40b19e1` (not a deliverable; it checks the annotation semantics, not the durable tool).

Five runs, all against committed bytes:

| run | baseline | expected | measured |
|---|---|---|---|
| r43 annotations | `7ceff59` | O STALE, C STALE, Ca FRESH | 2 stale claims; O 2/3, C 2/3, Ca 1/1 |
| r44 control | `c9f4eaa` | all fresh | 0 stale; O 3/3, C 2/2, Ca 2/2 |
| r43 mutation (no literal tool path; paraphrased terms) | `7ceff59` | O and C still stale | 2 stale |
| r43 annotations evaluated at HEAD | `6e9a30d` | must NOT be used; Ca flips | 3 stale (Ca false positive) |
| r44 control evaluated at HEAD | `6e9a30d` | must NOT be used; O flips | 1 stale (O false positive) |

The last two rows are the empirical reason for the baseline-only rule: a worktree-reading gate produces a false STALE on Ca (the r43 disposition artifact exists now) and on r44 O (the four-class successor exists now). The first three rows prove the annotation design reaches the required verdicts independently of O05/O06.

False positives found while building the cross-check (all fixed by anchoring):

- `four-class` registry scan matched `receipt_guard_adoption.py:1192` ("four-classified") at `c9f4eaa` → negative control false STALE; anchored signature removes it.
- `gem` matched inside "Judgment Machines" in `death-afterlife-eschatology.md:1`; `stone` matched "Deucalion's stones" in `flood-traditions.md:3`; word boundaries remove both.

These are the same class of defect O09 hunts (generic-token over-match), found independently in the capability and ownership legs.

## 5. Filed-fragment reconciliation

| artifact | what it proves | status / divergence the integrator must resolve |
|---|---|---|
| `op/O05-r43-demo.md` | annotated r43 copy; O STALE 2/3, C STALE 2/4, Ca FRESH; exit 1; baseline-vs-HEAD flip on Ca | authoritative r43 fixture. Uses inline `before_checks`; the r43 claims file does not exist at `7ceff59`, so the annotated copy is read from the worktree. |
| `op/O06-negative-control.md` | r44 fixture, 9/9 clauses fresh, exit 0; discriminators at HEAD | authoritative negative-control fixture, sha `38857b08…`. Uses `capability_present` with `path::regex` scoped to the witness; the durable registry must also support named capabilities (O05). |
| `op/O09-traps.md` | T1–T3 trap matrix and acceptance fixtures; prototype fails all three | trap outcomes are binding on the durable tool. Its cut missed O05/O06 by minutes; the schema is the same (`before_checks`/`probe_kind`). |
| `op/O10-exit-codes.md` | 0/1/2/3 contract; 14/14 suite vs a compliant double; 11/15 failures vs the prototype | exit codes are 0 fresh, 1 stale, 2 malformed, 3 could-not-evaluate. The prototype's 2-for-stale is nonconforming. |
| `op/O13-probe-coverage.md` | prototype: 6 of 13 kinds uncontrolled, 2 contract kinds missing, unknown kinds → STALE; recommends eight contract kinds | the durable selftest must compute its control count from the registry, not a hard-coded literal (the prototype's `seventeen checks collected (18)` failure). |
| `calib/Ca06-queue-successor.md` | row `r43-stale-premises` routed to the r47 O tool; parent queue pinned `dfc9265d…`; reclass gates G1–G8 | the O landing closes the Ca row only when G1–G8 pass; do not reclass on tool existence alone. |

Clause-count divergence: O05's C has four checks (path-absent on the lithic entry + topic-owner) and reports 2/4; this seat's independent C subset has three and reports 2/3. Both are correct; the contract requires every declared clause to hold, not a fixed count. The integrator should cite O05's fixture as the demo and not hardcode "2/3" or "2/4" in acceptance prose.

Schema divergence: O05/O06 use inline `before_checks`; P01/O09 describe a sidecar. **Support both**: inline checks are the demo form; a `--checks <sidecar>` path is the forward form for future rounds (filed claims stay immutable). The bare command still relies on the conservative miner (§3.5) to satisfy the claim's counting command.

## 6. Integration apply spec

### 6.1 Durable tool

- Target: `tools/harness/claims-freshness.py`.
- Byte source: the assembled fenced body from O01–O03, as pinned by `op/W01-landing-spec.md` when it lands. **At this cut neither the body nor W01 exists.** Do not substitute the r44 prototype wholesale: it fails O09's traps, inverts the exit codes, and its selftest is red.
- Preserve exactly one trailing LF; record the applied file's sha256 in the demo artifact and `validation.json`.
- Stdlib only; read-only.

### 6.2 Demo inputs to extract under `reports/round-47/calib/`

| target | source | digest to verify |
|---|---|---|
| `r43-claims-annotated.json` | O05 §3 fenced block | record after extraction (O05 does not publish a digest for this file) |
| `negative-control.claims.json` | O06 §3 fenced block | `38857b08543964cf2fd4a0154412279803043997d86fdcab1b2ce20499d4df1c` |
| `claims-freshness-demo.json` | authored by the integrator from the runs below | includes `tool_sha256`, baseline, per-run verdicts/exits, fixture digests |

### 6.3 Commands and expected results

```
# 1. selftest — controls computed from the registry
python3 tools/harness/claims-freshness.py --selftest
# exit 0; every control PASS; count == registry count

# 2. bare regression (miner fallback; the claim's own counting command)
python3 tools/harness/claims-freshness.py --claims reports/round-43/claims.json
# O STALE, C STALE, Ca FRESH; exit 1

# 3. typed-probe regression (authoritative clause-level run)
python3 tools/harness/claims-freshness.py --claims reports/round-47/calib/r43-claims-annotated.json
# O STALE, C STALE, Ca FRESH; exit 1; every clause reports measured vs expect

# 4. negative control
python3 tools/harness/claims-freshness.py --claims reports/round-47/calib/negative-control.claims.json
# 3 fresh, 0 stale; exit 0

# 5. traps (O09 §6), malformed and could-not-evaluate vectors
# exit 2 for malformed, 3 for no checks; never 0

# 6. anti-theater mutation
# same verdicts as (3) after literal tool names in the claim are replaced
```

### 6.4 Ca06 reclass gates

`reports/round-47/calib/Ca06-queue-successor.md` row `r43-stale-premises` does not reclass on tool existence. Its gates G1–G8 require, in outline: a durable path with a recorded sha; a green selftest whose asserted count equals the controls run; the r43 O/C stale + Ca fresh demonstration with clause evidence; the negative control fresh; the anti-theater mutation still flagging; the exit contract; and a filed demonstration. Until then the row stays `routed-with-owner`. The O claim's completion and the Ca row's reclass are the same event.

## 7. Acceptance matrix (for O08/V02)

| id | check | expected | source |
|---|---|---|---|
| A-01 | `--selftest` | exit 0; controls = registry count; includes T1/T2/T3 controls | O04/O13 |
| A-02 | bare r43 run | O STALE, C STALE, Ca FRESH; exit 1 | claim :41; prototype |
| A-03 | annotated r43 run | same verdicts; clause-level measured values; exit 1 | O05 |
| A-04 | negative control | 3 fresh, 9/9 clauses; exit 0 | O06 |
| A-05 | negative control at HEAD override | O flips STALE (discriminator) | O06 §1 |
| A-06 | anti-theater mutation | O and C still STALE | claim :41; O07 |
| A-07 | T1 novel phrasing | not a false STALE; could-not-evaluate or FRESH | O09 T1 |
| A-08 | T2 polarity/unknown kind/empty checks | malformed exit 2; no checks exit 3 | O09 T2 |
| A-09 | T3 tags/tree/blob | resolved commit; malformed for non-commit; exit 2 | O09 T3 |
| A-10 | determinism | two runs, identical verdict and exit | O14 |
| A-11 | malformed inputs | no crash; named error; exit 2 | O15 |
| A-12 | baseline-only | no worktree read of corpus/tools; Ca and r44-O flips absent at baseline | O11 |
| A-13 | read-only | `git status --porcelain` unchanged except the artifact | O08 |
| A-14 | post-landing | run from the durable path, not `.scratch` | V02 |

## 8. Gap register at cut (18:03Z)

| artifact | seat | consequence if absent at integration |
|---|---|---|
| `op/O01-tool-core.md` | O01 | no durable tool body; O cannot be applied |
| `op/O02-probe-registry.md` | O02 | probe vocabulary/aliases undefined |
| `op/O03-verdict-contract.md` | O03 | verdict/exit implementation undefined |
| `op/O04-selftest.md` | O04 | no green control set; O08/O13 cannot pass |
| `op/O07-anti-theater.md` | O07 | the mutation demonstration is owed (this seat's §4.3 is design evidence only) |
| `op/O08-verify.md` | O08 | no independent gate verification |
| `op/O11-baseline-eval.md` | O11 | baseline-vs-worktree requirement unverified by its owner (this seat's §4.5 covers it) |
| `op/O14-determinism.md` | O14 | determinism unverified |
| `op/O15-malformed.md` | O15 | malformed-input behavior unverified |
| `op/W01-landing-spec.md` | W01 | no pinned apply target; §6 is the scribe's substitute |
| `op/V02-gate-verify.md` | V02 | post-landing verification owed |
| `reports/round-47/calib/claims-freshness-demo.json` | integrator | the claim's "filed demonstration" is unmet |
| `tools/harness/claims-freshness.py` | integrator | the claim's durable deliverable is unmet |

Any of these absent at integration makes the corresponding link `could-not-evaluate`, not green.

## 9. Risks and limits

1. **The deliverable is absent.** Every "expected" result in §4 comes from a reference evaluator or the prototype, not from `tools/harness/claims-freshness.py`. O05/O06 say so in their own limits; this summary repeats it so no downstream reader treats a reference run as a durable one.
2. **The prototype cannot be shipped as-is.** Red selftest (17/19), inverted exit codes, two contract probe kinds missing, unknown kinds downgraded to STALE, generic-token false STALE (O09 T1), tag-object misreporting (T3). The O01–O04 authors must fix these, not copy the body.
3. **Two annotation routes.** Inline `before_checks` (O05/O06) vs sidecar (P01/O09). Supporting both is cheap; choosing neither leaves the bare counting command and the typed-probe demonstration in conflict.
4. **Capability false positives.** Registry-wide scans must be anchored; `four-class` matched `four-classified` and `gem` matched `judgment` in a loose scan. These are measured, not hypothetical.
5. **Trap T1 is a design constraint, not a test detail.** A miner that extracts one token before "slot" will refuse fresh claims. The conservative rule (generic token → could-not-evaluate) must be in the tool, not just the fixtures.
6. **Cut-time.** O05/O06/O09 landed within the last few minutes of this cut; O01–O04, O07, O08, O11, O14, O15, W01 and V02 had not. The integrator must re-snapshot before deciding; this document's §8 is the exact cut.
7. **No axis harm found.** The method improves operability if applied; the absent tool harms nothing live. The risk is process: declaring O improved from reference-evaluator runs.

## 10. Handoff

**For the integrator.** Apply O01–O03's assembled body to `tools/harness/claims-freshness.py` only when it exists and W01 pins it. Extract O05's and O06's fenced fixtures to the two `calib/` paths in §6.2. Run the six commands in §6.3 and file `claims-freshness-demo.json` with the tool digest and every measured verdict/exit. Reclass Ca06's `r43-stale-premises` row only when G1–G8 pass. If any of §8's artifacts is still absent, record O as `could-not-evaluate` for that link — the reference evaluators do not satisfy the claim's "durable" threshold.

**For O08/V02.** Use the §7 matrix; the two strongest independent checks are (a) the negative control at `c9f4eaa` exits 0 while the same fixture at HEAD turns O STALE, and (b) the r43 annotated run exits 1 with every failing clause naming the measured capability/owner. If the durable tool cannot reproduce both, the baseline-only or anti-theater property is not implemented.

**For the parent.** The O claim is not delivered at this cut. The chain's strongest assets are O05's annotated r43 fixture, O06's negative-control fixture (`38857b08…`), O09's trap matrix, and O10's exit suite. The missing piece is the tool body plus its selftest; without it, every O verdict in this round is `unprovable-but-better`.

## Appendix A — this seat's evaluator output (verbatim, abridged)

`python3 -B .scratch/o12/probe-check.py` → exit 0; full output `.scratch/o12/probe-check.out`.

```
== r43 regression at 7ceff59a0216 ==
  [O] capability_present  basename-couples-policy  measured=1 candidate(s) expect=False -> MISMATCH
        candidate tools/harness/couples-reference-extractor.py
  [O] VERDICT STALE (2/3 clauses hold)
  [C] count_eq            corpus/knowledge/myth-symbol/*.md measured=26 expect=26 -> holds
  [C] count_eq            corpus/knowledge/*/*.md          measured=223 expect=223 -> holds
  [C] topic_owner_absent  corpus/knowledge/myth-symbol     measured=1 owner file(s) expect=[] -> MISMATCH
        owner corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
  [C] VERDICT STALE (2/3 clauses hold)
  [Ca] path_absent        reports/round-43/calib/dispositions-r38-r39.json measured=absent expect=False -> holds
  [Ca] VERDICT FRESH (1/1 clauses hold)

== r44 negative control at c9f4eaa707b6 ==
  [O] VERDICT FRESH (3/3 clauses hold)
  [C] VERDICT FRESH (2/2 clauses hold)
  [Ca] VERDICT FRESH (2/2 clauses hold)

== r43 anti-theater mutation ==
  [O] capability_present  measured=1 candidate(s) expect=False -> MISMATCH
  [C] topic_owner_absent  measured=1 owner file(s) expect=[] -> MISMATCH
  both STALE

== COUNTERFACTUAL r43 at HEAD ==  Ca STALE (path now present) -> 3 stale claims
== COUNTERFACTUAL r44 at HEAD ==  O STALE (four-class now present) -> 1 stale claim
summary: r43 stale=2 (want 2), r44 stale=0 (want 0), mutation stale=2 (want 2),
         r43@HEAD stale=3 (want 3), r44@HEAD stale=1 (want 1) -> PASS
```

Semantics note: this evaluator encodes `path_absent` as "measured presence vs `expect`"; O05/O06 encode `expect` as the predicate's asserted value. The verdicts are identical; this seat's scratch output uses its own internal form and is not a byte source for the durable tool.

## Appendix B — evidence read at this cut

Read in full or in the cited sections: `reports/round-47/claims.json`, `targets.json`, `telemetry/dispatch-declared.json`; `reports/round-47/op/O05-r43-demo.md`, `O06-negative-control.md`, `O09-traps.md`, `O10-exit-codes.md`, `O13-probe-coverage.md`; `reports/round-47/calib/Ca05-verify.md`, `Ca06-queue-successor.md`; `reports/round-43/claims.json`, `review/R01-review.md:396-406`; `reports/round-44/claims.json`, `review/R01-review.md:212-260`; `reports/round-46/loop-1-retrospective.md:43-54`; `.scratch/ca01/claims-freshness.py` (read-only, run); `tools/harness/couples-reference-extractor.py`, `tools/harness/basename-couples-resolver.py` (selftests run read-only); `corpus/README.md` (partition context only).

Commands run: `git rev-parse`, `git status --porcelain`, `git ls-tree`, `git show`, `git cat-file -e`, `git grep`, `git merge-base --is-ancestor`, `sha256sum`, `find`, `grep`, `wc`, `python3 -B` on the prototype, the two harness tools, and this seat's scratch evaluator. No filed byte edited; no corpus write; no `run-validation.py`; no git mutation, network, or install.
