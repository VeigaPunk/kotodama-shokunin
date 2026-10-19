# O08 — gate verifier 1: the behaviors are right; the assembled tool does not exist

- Seat: `O08` | role verifier | claim **O** (operability) | round 47, loop 2 | refire seat
- Out path: `reports/round-47/op/O08-verify.md` (the only durable write by this seat)
- Mission: `reports/round-47/targets.json` seat O08 — "given the assembled tool, run its `--selftest` + the r43 demo + negative control + anti-theater in a clean `.scratch`; confirm green + correct flags."
- Baseline at seat start: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`); r43 measurements at `7ceff59a0216a8ea21ee43262d9fc72abf770cee`; negative control at `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d`.
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root, Python 3.14.7.
- Boundary: wrote only this out path under `reports/round-47/`; all scaffolding under `.scratch/o08/`; no filed byte edited, nothing staged under `corpus/`, no `run-validation.py`, no git mutation, install, or network. `git status --porcelain` before filing showed only pre-existing untracked round dirs.

## 1. Verdict

**BLOCKED — the four required behaviors reproduce exactly, but there is no assembled tool to which they belong.** The three filed drafts are each sound in isolation and mutually incompatible at every seam that matters. A plain concatenation does not run; a ~100-line verifier adapter makes it run and produces the required r43 verdicts. The O claim's `after_required` is therefore **not met by the filed bytes alone**, and the integrator (W01) must resolve the nine defects in §7 before the claim can be admitted. Marking O complete on the present evidence would be an over-claim.

| required demonstration | result through the adapter | status |
|---|---|---|
| `--selftest` green | part2 registry `43/43`, exit 0 | **PASS**, but only 43 controls; O04's filed control set is not integrated (§7 D8/D9) |
| r43 demo: O stale, C stale, Ca fresh, exit 1 | exactly that | **PASS** |
| negative control not flagged, exit 0 | 8/8 clauses hold at `c9f4eaa`, exit 0 | **PASS** |
| anti-theater still flags from capability/ownership | 4/4 mutations | **PASS** |
| exit 0 only all-fresh; 1 stale; 2 malformed; CNE non-zero | 0 / 1 / 2 / 3 observed | **PASS** |
| durable path `tools/harness/claims-freshness.py` exists | `ls` → no such file (pre-integration, expected) | not yet applicable |
| plain concatenation of the filed fences runs | `SyntaxError`, then no `main` | **FAIL** |
| filed demo artifacts replay on the assembled tool | O05 5/6 checks rejected; O06 fixture rejected | **FAIL** |

**Verifier judgment: conditional PASS on behavior, FAIL on artifact.** The O claim may be admitted only after the integrator applies an assembly that resolves D1–D9 and re-runs the four demonstrations from the durable path (V02).

## 2. What the filed bytes are, proved

Each draft is a fenced Python block. Extracted with the fence-boundary rule and a trailing newline, they reproduce the digests their authors declared:

```
part1 (O01) 24754 bytes sha256 72c294f2c49dc53f3f7e7e65b0dc646e238a56b19473f84b63f1cb5bbf13b876  (declared: O01 §1)
part2 (O02) 38874 bytes sha256 a60b0a22df2d73c1...                                                (no digest declared)
part3 (O03) 16491 bytes sha256 097a31987cc334d93eaa117e60d7112cddeb7fbf9a356d10ca4dc178721cfcef  (declared: O03 §6)
```

Commands: `.scratch/o08/build_assembly.py` (reads `reports/round-47/op/O01-tool-core.md:160-794`, `O02-probe-registry.md:254-1222`, `O03-verdict-contract.md:86-574`; prints `MATCH`/`MISMATCH` per part). The digests match only with the final newline; without it the hashes are `0617cad…` and `52ab888…`. This is a byte-level confirmation that the filed fragments are the tested bodies, not retyped approximations.

Isolated suites, run from the fragments (scratch drivers that predate this seat, cited as corroboration not as my own control):

```
$ python3 -B .scratch/o01-r47/check_core.py   -> PASS 70 / 70, exit 0
$ python3 -B .scratch/o08/part2.py --selftest -> PROBE-REGISTRY SELFTEST: 43/43, exit 0   (extracted from the filed fence)
$ python3 -B .scratch/o03/drive_o03.py        -> selftest 33/33 PASS, exit 0
```

One divergence worth recording: `.scratch/o02/probe_registry.py` — the author's scratch module, 48/48 when run — is a later variant than the filed fence (43/43). The filed fence is the artifact under review; the 48-control scratch is not filed, and O02 declared no digest to settle which body it tested (§7 D9).

Each part is internally coherent. The failures below are all at the joins.

## 3. Positive regression — r43 O and C stale, Ca fresh

Overlay (verifier-authored, O02 registry schema; §3.4 K03 overlay shape, pinned to the filed claims sha):

```
claims  reports/round-43/claims.json  sha256 9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b
overlay .scratch/o08/r43-overlay.json sha256 1408eca802c5802a83f8ec7368f19e192dea4da55e192802da8da1989b70f5b4
```

```
$ python3 -B .scratch/o08/claims-freshness.assembled.py \
    --claims reports/round-43/claims.json --checks .scratch/o08/r43-overlay.json
claims-freshness: round 43 baseline 7ceff59 (7ceff59a0216a8ea21ee43262d9fc72abf770cee)
  [O] STALE             2/2 clauses contradict
      clause 0 (capability_present): measured=True expected=False -- no durable instrument implements the r39 basename-couples policy
      clause 1 (capability_present): measured=True expected=False -- the single wrapped couples field reads 0/4 tokens
  [C] STALE             1/3 clauses contradict
      clause 1 (topic_owner_absent): measured=False expected=True -- lithic slot named but unbuilt since r42's C01/C04 collision routed this draft to spare
  [Ca] FRESH            1/1 clauses hold
summary: 1 fresh, 2 stale, 0 could-not-evaluate, 0 malformed; clauses 6 (3 hold, 3 contradict, 0 not evaluated)
REFUSE: claim(s) O, C have a `before` already false at 7ceff59; do not dispatch.
exit 1
```

Independent measurement of the premises, from committed bytes only:

```
$ git ls-tree -r --name-only 7ceff59 corpus/knowledge/myth-symbol | grep -c '\.md$'   -> 26
$ git ls-tree -r --name-only 7ceff59 corpus/knowledge | grep -c '\.md$'              -> 223
$ git ls-tree -r --name-only 7ceff59 tools/harness/basename-couples-resolver.py | wc -l -> 0
$ git ls-tree -r --name-only 6e9a30d tools/harness/basename-couples-resolver.py | wc -l -> 1
$ git show 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md | head -1
# Stone, gem and metal symbolism — the lithic register: ...
$ git ls-tree -r --name-only 7ceff59 reports/round-43/calib/ | wc -l      -> 0
```

C is stale **only** on ownership: both counts hold, exactly the r43 shape R01 recorded (`reports/round-44/review/R01-review.md:228-231`). The capability probe is behavioral: it materializes the wrapped `- couples:` fixture and runs each baseline `tools/harness/*.py` candidate with `--census`; the witness at `7ceff59` prints `refs=4`, so the measured value is `True` against declared `expect=false` (`reports/round-47/op/O02-probe-registry.md:65`).

## 4. Negative control — not flagged, exit 0

A claims file at `c9f4eaa` (round 44's baseline) whose `before` premises are true there, converted from O06's filed fixture to the O02 object-target schema (the conversion itself is a defect finding, §7 D7):

```
$ python3 -B .scratch/o08/claims-freshness.assembled.py \
    --claims .scratch/o08/neg-control.claims.json --checks .scratch/o08/neg-control.overlay.json
claims-freshness: round 47 baseline c9f4eaa (c9f4eaa707b6e977ff6e1616463e91f4b8afea5d)
  [O] FRESH             4/4 clauses hold
  [C] FRESH             2/2 clauses hold
  [Ca] FRESH             2/2 clauses hold
summary: 3 fresh, 0 stale, 0 could-not-evaluate, 0 malformed; clauses 8 (8 hold, 0 contradict, 0 not evaluated)
exit 0
```

The discriminator is real: the same `path_absent` clause measures `True` at `c9f4eaa` and `False` at `6e9a30d`, because the successor resolver landed in between:

```
c9f4eaa path_absent measured True  status holds
6e9a30d path_absent measured False status mismatch
```

A worktree-measuring gate would flag the control; this one does not. The control's own `before_checks` could not be declared in-file (§7 D4/D5) — the overlay is the only path that works today.

## 5. Anti-theater — mutations do not move the verdict

`.scratch/o08/anti_theater.py`, 4/4:

```
PASS A1 renamed carrier still measures the capability  [1/1 candidate(s) pass the declared behavior: tools/harness/zzz-renamed.py]
PASS A2 clause remains a verbatim fragment of the mutated prose  [substring]
PASS A2 phantom tool name in prose does not change the measurement  [1/1 candidate(s) pass the declared behavior: tools/harness/couples-reference-extractor.py]
PASS A3 renamed owner file still yields an ownership hit  [1 owner(s): corpus/knowledge/myth-symbol/zzz-renamed.md]
PASS A4 unowned topic measures True and holds (live value drives the verdict)  [0 owner(s): none]
ANTI-THEATER OK: 4/4
exit 0
```

- **A1** — the capability witness blob (`git show 7ceff59:tools/harness/couples-reference-extractor.py`) re-pathed to `tools/harness/zzz-renamed.py` still passes the behavioral test. The `capability_present` target has no name/tool field (`O02-probe-registry.md:445-554`), so renaming cannot launder a stale premise.
- **A2** — appending "the phantom zzz-nonexistent.py is the only candidate" to the claim prose leaves the measured value and verdict identical. The check carries no tool name to rewrite.
- **A3** — the owner entry renamed to `zzz-renamed.md`, header bytes unchanged, still produces an ownership hit; `topic_owner_absent` scans H1 / `- topic:` / `- gap filled:`, not filenames.
- **A4** — pointing the same probe at `cartography` (unowned at `7ceff59`) flips the measurement to `True`, so the verdict is a function of measured state, not of constant text.

## 6. Exit contract and determinism

| input | exit | evidence |
|---|---|---|
| r43 overlay, stale | 1 | §3 |
| negative control, all hold | 0 | §4 |
| `reports/round-47/claims.json`, no `before_checks` | **3** (could-not-evaluate), refusal printed | `.scratch/o08/cne.out` |
| non-JSON claims file | **2** (malformed) | `.scratch/o08/malformed.out` |
| two identical r43 runs | identical `decision_sha256` `8360914d08619511fb5f5f17474988a1eb6689b8a18586b262b53af2272331fd`, exit 1 both | `.scratch/o08/r43-run-{1,2}.json` |

This satisfies "could-not-evaluate != green" and "exits non-zero on stale" (`reports/round-47/claims.json:47`). Note that exit 3 is the adapter's pass-through of part 3's `EXIT_NOT_EVALUATED`; part 3 documents why 3, not 2, is correct (`O03-verdict-contract.md:50-60`).

## 7. Integration defects — the reason the claim cannot be admitted yet

All are reproducible from the filed fences. None is a probe-logic error; every one is a seam.

**D1 — plain concatenation is a syntax error.** Part 2 carries its own `from __future__ import annotations` (`O02-probe-registry.md:315`; part 3 at `O03-verdict-contract.md:108`); concatenated after part 1, `py_compile` fails:

```
SyntaxError: from __future__ imports must occur at the beginning of the file
```

**D2 — part 2 terminates the program.** Its last lines are `if __name__ == "__main__": sys.exit(selftest_registry())` (`O02-probe-registry.md:1220-1221`). In a concatenated tool this runs before any CLI parse.

**D3 — no part defines `main()`.** Part 1 declares none; part 3 states it "does not define a `main`" and that "the full tool does not exist yet … The seam in §8 is a proposal until their fragments land" (`O03-verdict-contract.md:744`). The adapter's `main` is verifier scaffolding, not a filed deliverable.

**D4 — no in-file check can survive the join.** Part 1's `Check.as_dict()` emits `expect_source` (`O01-tool-core.md:416-424`); part 2's `validate_check` allows only `id, clause, probe_kind, target, expect, evidence_command, note` and rejects the rest (`O02-probe-registry.md:566-590`). Reproduction:

```
claims[0]: before_checks[0] expect_source -> "check has unknown key(s): expect_source" (exit 2)
```

I had to strip `expect_source` in the adapter before any in-file `before_checks` would run. Every claim declaring checks in-file is malformed today.

**D5 — the two parts disagree on `expect`'s type.** Part 1 requires boolean (`O01-tool-core.md:474`); part 2 requires `int` for `count_eq` and a 64-hex `str` for `sha256_eq` (`O02-probe-registry.md:555-563`, `O02-probe-registry.md:597-611`). A `count_eq` check cannot pass both. Reproduction:

```
{"probe_kind":"count_eq","expect":223} -> "count_eq expect must be a JSON integer, got True" (part 2)
                                        "expect is not boolean" (part 1, before part 2 is reached)
```

Consequence: the count and digest probes — the legs that carry r43 C's true counts and O06's witness pin — are reachable only through the overlay path.

**D6 — the overlay is specified but implemented nowhere.** K03 §3.4 defines `--checks` (`reports/round-47/scout/K03-gate-spec.md:111-129`), and O05's demo depends on it, but no filed part parses an overlay; part 1's `open_claims` has no checks argument (`O01-tool-core.md:747-769`). The adapter's `_overlay_checks` (schema, round, baseline, `claims_sha256`, unknown-id checks) is new logic, not a bridge.

**D7 — the filed demonstrations use incompatible schemas.**
- O05's overlay (`O05-r43-demo.md:101-158`) passes 6 checks to part 2. **5 are rejected**: two `capability_present` targets `{"capability","scope"}` → "unknown key(s): capability, scope"; two `count_eq` with boolean `expect` → "expect must be a JSON integer"; one `topic_owner_absent` target `{"partition","topics"}` → "unknown key(s): partition, topics". Only Ca's `path_absent` is accepted. The filed r43 demo cannot be replayed on the O02 registry.
- O06's fixture (`O06-negative-control.md:78-179`) has **9/9 string targets** where the registry requires objects ("target is not an object", exit 2), and **3/9 clauses are not substrings of their own `before`** (O `sha256_eq`, O `capability_present`, O second `count_eq`) — rejected by the clause-binding rule.
- Cross-check: O06's own evaluator greens its fixture (`3 fresh, 0 stale`, exit 0) while the assembled gate rejects it (exit 2). Both artifacts are internally consistent with their own authors; they are not consistent with each other.

**D8 — O04's filed control set targets a fourth API.** Its fence defines `selftest()` around `evaluate_claim(...)` and `FixtureBaseline(...)` (7 and 12 call sites) and check entries keyed `"kind"` with string targets (37 occurrences) — none of which exist in the assembled parts (`evaluate_claim` 0 definitions, `FixtureBaseline` 0). The round's own required controls (synthetic stale, synthetic fresh, CNE, malformed) therefore cannot run as filed. Additionally, the fence contains 36 named `check("…")` controls plus loop-driven calls, while O04 §2 claims 46 controls — `to-verify` the exact denominator; it cannot be settled without running the suite, which cannot run.

**D9 — the selftest surface is partial and the draft/scratch bodies diverge.** The assembled `--selftest` runs part 2's 43 registry controls only. Part 3's 33 decision controls live in an external scratch driver; O04's 46-control suite is not integrated. The author's scratch `probe_registry.py` runs **48/48**, while the filed fence runs **43/43**; O02 declared no digest, so the filed body cannot be shown to be the one tested. The claim's threshold says "selftest green", which 43/43 technically satisfies, but the filed control set the round names is not what runs.

Severity for dispatch: D1–D3 block execution; D4–D6 block declared-input evaluation; D7 makes the filed demonstrations non-replayable; D8–D9 understate the test surface. All are W01/integrator work; none requires changing probe semantics.

**Concurrent corroboration (read at filing time).** Two refire seats filed independent findings on the same fences: W01 (`op/W01-landing-spec.md:19-40`) pins a 105,526-byte assembly (`sha256 d4e4d60e…`) and names the same seam defects (S1–S6), and V02 (`op/V02-gate-verify.md:11-25`) independently reaches "could-not-evaluate, not green" because the durable path is absent. Neither applies bytes; the durable path remains absent. The integrator should prefer W01's pinned assembly and its 19-control seam over my verifier adapter, which exists only to measure behavior under `.scratch/o08/`.

## 8. What this verifier did and did not establish

Established:
- The filed bytes are the tested bytes (digest match).
- With a seam adapter that adds no probe or verdict logic, all four required demonstrations pass and the exit contract holds.
- The r43 positive regression matches R01's independent findings and my own `git` reads.
- The gate is not literal theater: four mutations leave the measured state in charge.

Not established (mark `to-verify`, do not read as green):
- That `tools/harness/claims-freshness.py` exists and runs as a single file — it does not yet.
- That the filed O05/O06 artifacts replay — they do not.
- That O04's 46 controls pass — they cannot run against these parts.
- That the integrator can apply the adapter as-is — it is verifier scaffolding under `.scratch/o08/`, explicitly not a deliverable, and it omits the `--at` exit cap O03 requires (`O03-verdict-contract.md:64`).

## 9. Reproduction

Scratch (not durable; regenerate with these commands):

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B .scratch/o08/build_assembly.py                 # digest-checks the three fences, writes the assembly
python3 -B .scratch/o08/claims-freshness.assembled.py --selftest
python3 -B .scratch/o08/claims-freshness.assembled.py --claims reports/round-43/claims.json --checks .scratch/o08/r43-overlay.json
python3 -B .scratch/o08/claims-freshness.assembled.py --claims .scratch/o08/neg-control.claims.json --checks .scratch/o08/neg-control.overlay.json
python3 -B .scratch/o08/anti_theater.py
```

Artifacts: `.scratch/o08/claims-freshness.assembled.py` (2193 lines, sha256 `56470610ada295e72b8ac4408e26d61c9dc9335bac3ead37ff767bcb1952da4a`), `r43-overlay.json` (sha256 `1408eca8…`), `neg-control.claims.json`, `neg-control.overlay.json`, `anti_theater.py`, and the `.out`/`.json` transcripts named above. The assembly embeds part1 + part2 + part3 byte-for-byte except the two module-boundary lines (D1/D2) and appends the adapter.

## 10. Evidence register

| evidence | location |
|---|---|
| O claim text, thresholds, required flags | `reports/round-47/claims.json:37-48` |
| O08 mission | `reports/round-47/targets.json` seat O08 |
| fence bodies and declared digests | `reports/round-47/op/O01-tool-core.md:160-794`, `O02-probe-registry.md:254-1222`, `O03-verdict-contract.md:86-574` |
| part 1 boolean-only `expect` | `reports/round-47/op/O01-tool-core.md:474` |
| part 1 `expect_source` in `as_dict` | `reports/round-47/op/O01-tool-core.md:416-424` |
| part 2 closed target schemas | `reports/round-47/op/O02-probe-registry.md:445-554` |
| part 2 `__main__` guard | `reports/round-47/op/O02-probe-registry.md:1220-1221` |
| part 3 status vocabulary + exit 3 rationale | `reports/round-47/op/O03-verdict-contract.md:172-250`, `:50-60` |
| "the full tool does not exist yet" | `reports/round-47/op/O03-verdict-contract.md:744` |
| O05 overlay | `reports/round-47/op/O05-r43-demo.md:101-158` |
| O06 fixture | `reports/round-47/op/O06-negative-control.md:78-179` |
| O04 control set | `reports/round-47/op/O04-selftest.md:202-488` |
| r43 `before` lines | `reports/round-43/claims.json:27,40,53` |
| R01-43-12 defect | `reports/round-43/review/R01-review.md:400` |
| r43 measured premises | `reports/round-44/review/R01-review.md:222-235` |

## 11. Seat self-audit

- Wrote only `reports/round-47/op/O08-verify.md`; scratch stayed under `.scratch/o08/`.
- Edited no filed byte; staged nothing under `corpus/`; changed no `tools/` file; ran no `run-validation.py`; no git commit/push, install, or network.
- Every number above is from a command in this session, not from a sibling's prose; sibling claims I did not re-run are labelled as corroboration.
- The adapter is explicitly **not** the deliverable and must not be applied as the durable tool without W01's review of D1–D9.
