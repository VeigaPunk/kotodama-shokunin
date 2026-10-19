# X03 — gate-theater critique: the method survives its attacks; the artifact is a false green

- Seat `X03` | role critic | claim **O** (operability) | round 47, loop 2
- Out path: `reports/round-47/cross/X03-gate-theater.md` (the only file this seat writes)
- Mission (`reports/round-47/targets.json`, id `X03`): "prove the freshness gate isn't a
  two-string lookup — it must flag stale from measured capability/ownership, not literal prose;
  challenge it with novel phrasings."
- Cut: **2026-10-19T19:13Z**, revised **19:25Z**; HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe`;
  baselines under test `7ceff59` (r43) and `c9f4eaa` (r44).
- Revision note: Q01 gated the 19:16Z draft of this path (sha `52220e2622684b08f913c8add6094cfab2139e449e839fd74b4eec2c280ef239`).
  This revision adds §2.7 (the llama-herding refusal) and D4's third splice, and fixes wording;
  its digest differs and is recorded by the parent's close census, not self-referentially here.
  Q01's X03 citation is to the earlier draft; re-read at close.
- Citation convention: bare paths such as `op/O02-probe-registry.md:224`, `cross/X01-trades.md:50`,
  and `review/R02-review.md:250` are relative to `reports/round-47/`; `reports/round-*` and
  `.scratch/*` paths are from the lane root.
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from
  the lane root.
- Boundary: no filed byte edited (`reports/round-1..46/**` untouched; `reports/round-43/claims.json`
  sha256 `9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b` before and after); no
  corpus write or staging; no `run-validation.py`; no git mutation, install, or network. All attacks
  ran from `.scratch/x03/`. This seat writes only its out path.

## 0. Bottom line

**The method is not theater. The deliverable is.** These are separate findings and the round must
not conflate them.

| layer | verdict | evidence |
|---|---|---|
| **Probe method** (O02 registry, evaluated directly) | **PASS** — measured behavior and ownership, not prose | §2: novel prose, renamed witness, real-name decoy, polarity flip, baseline scope |
| **Durable artifact** (`tools/harness/claims-freshness.py`) | **ABSENT** at this cut | `git cat-file -e HEAD:tools/harness/claims-freshness.py` → absent |
| **The one executable concatenation** (O01+O02 fences) | **FALSE GREEN** — every argv prints `43/43` and exits 0 | §3 D1 |
| **r43 demo overlay** (O05, the claimed positive regression) | **REJECTED by the registry's own validator**: 5 of 6 clauses malformed | §3 D3 |
| **O claim** (`reports/round-47/claims.json:37-47`) | **NOT SATISFIED** — `could-not-evaluate` on the durable link | §6 |

The O claim's own threshold is explicit: "durable not `.scratch` ... could-not-evaluate != green"
(`reports/round-47/claims.json:47`). At this cut the round has a green-looking computation whose
only executable artifact exits 0 for a malformed file, a nonexistent file, an unknown flag, and the
r43 claims file alike. If an integrator accepts `--selftest` as the gate, the round lands the exact
theater the claim exists to prevent.

**Candidate axis verdict: `unprovable-but-better`, not `improved`** — the same conclusion O12
reached (`op/O12-scribe.md:30`), with three new blocking defects not visible from the filed reports
alone (D1–D3) and two policy-layer theater vectors the tool cannot close by itself (P1–P2).

## 1. What was attacked, and how

Three byte-sources were used, each with a pinned digest:

| artifact | path | sha256 | role |
|---|---|---|---|
| assembled registry (O01+O02 fences) | `.scratch/r04/assembled/claims-freshness.py` | `5a5635dfc0ea33639ad29b7e625e5b0095ecc9263e63941edec4b47f5fc0e9f0` | the tool an integrator gets from O02's splice instruction (`op/O02-probe-registry.md:224`) |
| O08 reference oracle | `.scratch/o08/claims-freshness.py` | `3bcbeb67fb1111d31a6960c9a9a3c22740c925b512ab46a2a731677a85357919` | independent second implementation, `--selftest` 15/15, exit 0 |
| O05/K03 reference evaluator | `.scratch/o05/claims-freshness-k03.py` | `f35eab201910f42c4184391c24de63a721fed859ad419575599f4ff02412b910` | the runner used for O05's r43 demo |

The registry was imported as a module and driven directly through `validate_claim_checks` /
`evaluate_check` / `claim_status`; every measurement below is from committed bytes at the named
baseline (`Baseline(root, rev)` uses `git ls-tree`/`git show`, never the worktree). The attack
harness is `.scratch/x03/attack.py`; its output is `.scratch/x03/attack.out`. The O08 oracle was
run as a CLI for the cross-check. No attack used the durable path because the durable path does not
exist.

The mission's question decomposes into four tests: does the verdict follow (1) new prose, (2) a
renamed carrier, (3) a real name with the wrong behavior, and (4) declared polarity/ownership rather
than a sentence? §2 answers each with a measured result.

## 2. The method survives the attacks

### 2.1 Novel phrasing: new sentences, same measured premise → same verdicts

The r43 `before` strings were replaced with prose that shares no long substring with them
(`.scratch/x03/attack.py`, `NOVEL_O`/`NOVEL_C`/`NOVEL_CA`), and the check clauses were re-bound to
the new text. The probes were unchanged.

| claim | novel clause | measured | declared | verdict |
|---|---|---|---|---|
| O | "ships no program that consumes the couples field" | capability `true` (`couples-reference-extractor.py`) | `false` | **STALE** |
| C | "the lapidary register is unbuilt" | owner found (`mineral-stone-symbolism.md`) | `true` | **STALE** |
| C | "totals stand at twenty-six" | 26 | 26 | holds |
| C | "corpus overall at two hundred twenty-three" | 223 | 223 | holds |
| Ca | "no per-finding disposition exists" | path absent | `true` | **FRESH** |

```
{"scenario": "S2-novel-O", "status": "stale", ... "detail": "1/7 candidate(s) pass the declared behavior: tools/harness/couples-reference-extractor.py"}
{"scenario": "S2-novel-C", "status": "stale", ... "detail": "1 owner(s): corpus/knowledge/myth-symbol/mineral-stone-symbolism.md"}
{"scenario": "S2-novel-Ca", "status": "fresh", ... "detail": "reports/round-43/calib/dispositions-r38-r39.json is absent"}
```

The O08 oracle independently produced the same three verdicts on the same novel fixture
(`.scratch/x03/novel-o08.json`): `[O] STALE`, `[C] STALE`, `[Ca] FRESH`, `summary: STALE (exit 1)`.
The flag does not come from r43's wording.

### 2.2 Renamed carrier: same behavior, different filename → still STALE

The baseline witness was read from `7ceff59:tools/harness/couples-reference-extractor.py` and placed
in an in-memory tree under `tools/harness/zzz-renamed.py`; the check still declared absence.

```
{"scenario": "S3-renamed-witness-asserts-absent", "status": "stale",
 "detail": "1/1 candidate(s) pass the declared behavior: tools/harness/zzz-renamed.py"}
```

A name lookup would have passed the claim; the behavioral probe did not. This is the unit-level
property O04's K13 and O02's S7 also assert, reproduced here against the real witness bytes.

### 2.3 Real name, wrong behavior → FRESH (the decoy)

The inverse control: a file at the real path `tools/harness/couples-reference-extractor.py`
containing only `print('hello world')`; the check still declares the `refs=4` behavior absent.

```
{"scenario": "S4-decoy-real-name-wrong-behavior", "status": "fresh",
 "detail": "0/1 candidate(s) pass the declared behavior"}
```

The verdict follows behavior, not the presence of the name in the tree. A two-string lookup that
searched for the tool's name would have flagged this claim STALE; the gate did not.

### 2.4 Polarity is declared, not inferred

Same measurement (`capability_present measured=true`), opposite `expect`:

```
{"scenario": "S5-polarity-flip-expect-true", "status": "holds", ...}
```

The registry has no `kind -> expected polarity` table; the r44 defect (asserting `true` for an
absence claim) is structurally impossible to inherit silently because `expect` is typed and
required (`op/O02-probe-registry.md:24-44`; selftest S8/S8b/S8c).

### 2.5 Baseline, not worktree

The Ca premise is true at `7ceff59` and false at HEAD — the disposition file exists now. The same
check evaluated against the two commits flips:

```
{"rev": "7ceff59", "measured": true,  "status": "holds"}      # absent at baseline
{"rev": "HEAD",    "measured": false, "status": "mismatch"}   # present at HEAD
```

This is the r43 false-positive class inverted: a worktree-reading gate would flag Ca stale.

### 2.6 Determinism and the candidate cap

Three evaluations of the same check produced one digest (`74eaf4c207e8d714…`), and the safety valve
works rather than truncating to a false absence:

```
{"cap_cap2": {"measured": null, "status": "could-not-evaluate",
              "detail": "7 candidates exceed max_candidates=2; refusing a partial scan"}}
```

`--no-exec` likewise yields `could-not-evaluate`, not green (`S8-no-exec`), and a claim with no
checks yields `could-not-evaluate` (`S9-no-checks`), matching the r47 threshold.

### 2.7 The other direction: the llama-herding false-positive trap is refused, not guessed

A gate that flags on any token is theater too. The R02 llama-herding trap is the canonical
false-positive control (`review/R02-review.md:207-227`; `op/O09-traps.md:76-134`). Against the O02
registry at HEAD:

```
{"case": "llama-generic", "status": "REJECTED",
 "error": "topic_owner_absent refuses a generic topic (register); name the register, not a category word"}
{"case": "llama-specific", "status": "holds", "measured": true, "detail": "0 owner(s): none"}
{"case": "cartography-specific", "status": "holds", "measured": true, "detail": "0 owner(s): none"}
```

The generic category word is a **malformed check**, not 51 owners and not a false STALE. A specific
unowned topic measures fresh. The registry refuses to guess a topic from a category phrase, which is
the behavior the r44 prototype lacked. (The cartography result is a side observation for the C
claim, not this seat's verdict.)

**Conclusion for §2.** The method answers the mission's question affirmatively: stale flags are
produced by executed behavior, scanned header ownership, and baseline-scoped path/count facts; a
generic topic is refused rather than over-matched. On this evidence the gate is not a two-string
lookup.

## 3. Blocking artifact defects

The method's survival does not make the O claim deliverable. Four defects are measured.

### D1 (critical) — the concatenation is a false green

`tools/harness/claims-freshness.py` does not exist, so the only executable assembled artifact is the
fence splice. That splice still contains O02's own module guard, and there is no `main` anywhere in
the file:

```
$ grep -n '^if __name__' .scratch/r04/assembled/claims-freshness.py
1599:if __name__ == "__main__":
$ grep -c '^def main' .scratch/r04/assembled/claims-freshness.py
0
```

The guard calls `selftest_registry()` and exits 0 **before** any CLI exists to parse an argument.
Measured:

```
$ cd .scratch/r04/assembled
$ python3 claims-freshness.py --claims ../../../reports/round-43/claims.json
...
PROBE-REGISTRY SELFTEST: 43/43
exit=0
$ python3 claims-freshness.py --claims ../../../.scratch/x03/malformed.json   # not JSON
exit=0
$ python3 claims-freshness.py --claims /nonexistent/xyz
exit=0
$ python3 claims-freshness.py --no-such-flag
exit=0
```

This is the purest form of gate theater: a green control count with no evaluation, on every input,
including malformed ones. The cause is O02's fence ending with the guard at
`op/O02-probe-registry.md:1220-1221` while O02's splice instruction says to append the body
(`:224`). The integrator who follows the instruction literally reproduces this file; the scratch copies under
`.scratch/r01/` and `.scratch/r04/` did (the r01 copy differs only by an assembly comment and a
header line, and has the same guard at `:1598`).

**Required fix.** Remove the part-2 `if __name__` guard (turn `selftest_registry` into a callable
control, not a script entry), add one `main()`, and make `--selftest` run the whole tool. A
post-landing `--selftest` must never be satisfiable by a tool that ignores `--claims`.

### D2 (critical) — no fence contains the CLI

O01 says it does not implement one (`op/O01-tool-core.md:9`, `:798`); O02 ends in a selftest guard
(`:1220`); O03's fence contains no `def main` and no `argparse` (grep returns nothing), only the
verdict algebra. P03's architecture lists `def main(argv=None) -> int`
(`plan/P03-o-plan.md:480`), but a plan is not a byte source. W01 (the landing spec) is absent, and
O12 says so (`op/O12-scribe.md:26`, `:319-320`).

Therefore O01+O02+O03, as fenced, **cannot be assembled into a runnable tool**. The `main` that the
P03 architecture promises was never written by the seat that owns it. This is not a splice detail;
it is a missing deliverable. O12's instruction to apply "O01–O03's assembled body" (`:413`) has no
body to apply.

### D3 (critical) — three schemas, no common runner; the r43 demo is not runnable by the registry

The r43 demo overlay is the claim's positive regression. Its fenced bytes are identical to
`.scratch/o05/r43-checks.json` (sha256 `0f43e90746ed99a1cae06e6887db87f9ca648aaeeebd3b7101a652bd82d8b25d`).
It uses a schema that the O02 registry rejects. The rejection is per clause:

```
$ python3 -B .scratch/x03/attack.py   # S10, feeding .scratch/o05/r43-checks.json's checks to validate_claim_checks
{"claim": "O",  "clause": "no durable instrument implements the r39 base", "verdict": "REJECTED",
 "error": "capability_present target has unknown key(s): capability, scope"}
{"claim": "C",  "clause": "myth-symbol 26", "verdict": "REJECTED",
 "error": "count_eq expect must be a JSON integer, got True"}
{"claim": "C",  "clause": "lithic slot named but unbuilt", "verdict": "REJECTED",
 "error": "topic_owner_absent target has unknown key(s): partition, topics"}
{"claim": "C",  "clause": "total 223", "verdict": "REJECTED",
 "error": "count_eq expect must be a JSON integer, got True"}
{"claim": "Ca", "clause": "have no per-finding disposition on record", "verdict": "ACCEPTED"}
```

The only accepted clause is Ca — the trivial baseline control, which is already fresh. **Every
clause that produces the claimed stale verdicts is malformed under the registry being landed.**
The inverse also holds: the O02 canonical overlay, fed to the O05 evaluator, exits 2 with
`capability_present target has unknown keys ['argv', 'exclude_globs', 'fixture', 'globs',
'max_candidates', 'success_regex', 'timeout_s']`; the O08 oracle, fed the canonical object target,
returns `could-not-evaluate` / exit 2 with `capability_present requires a glob`.

| runner | accepts | rejects |
|---|---|---|
| O02 registry (`validate_claim_checks`) | `target` objects: `globs/argv/fixture/success_regex`, `topic/partitions/fields/mode`, int `expect` for counts | O05's `{capability,scope}`, `{topics,partition}`, bool `expect` on counts |
| O05/K03 evaluator | O05's `{capability,scope}`, `{topics,partition}`, `value` + bool `expect` | O02's object targets |
| O08 oracle | string `target` (capability name, glob, `path::regex`, `partition:term`) | O02's object targets |

The r43 demonstration in `op/O05-r43-demo.md` §4 was produced by the O05 evaluator, not by the
registry in `op/O02-probe-registry.md` and not by the spliced tool. O08's oracle is another
implementation with its own schema (the r44 prototype is a fourth). **No artifact in the round
accepts the overlay and produces the verdict the claim requires.** This is the strongest theater risk in the chain: the green numbers and
the stale flags come from different tools, so the positive regression has never been end-to-end.

### D4 (high) — the second splice does not parse

The second assembly (`.scratch/o08/claims-freshness.assembled.py`, sha
`5aa0f8cd500023b7a0da02b4e7dd8f0a492ccb66047431bf090b5b41710d58a9`; mtime 16:10 local, provenance
`to-verify`) fails at import:

```
$ python3 claims-freshness.assembled.py --selftest
  File "....scratch/o08/claims-freshness.assembled.py", line 696
    from __future__ import annotations
SyntaxError: from __future__ imports must occur at the beginning of the file
exit=1
```

Every scratch concatenation failed in one of two ways: the r04/r01 splice is silently green, while
`.scratch/o08/claims-freshness.assembled.py:696` and the prior X03 assembly
`.scratch/x03/assembled.py:694` (sha `4c7af22048fa08fe303a29dff7bd87c33651e11a6683a4497cba32f716eb6a1e`,
provenance `to-verify`) both die on the same misplaced `from __future__ import annotations`.
Assembly is not a solved step; it is an unowned one.

## 4. Policy-layer theater the tool cannot close by itself

Even a correct CLI only measures the clauses it is given. The following are measured holes in the
*policy*, not bugs in the probe code. They matter because the O claim's purpose is to stop stale
dispatches, and each of these lets a stale claim pass.

### P1 (high) — check-set adequacy: a stale claim can be made FRESH by omitting the false premise

The gate's rule is "STALE if any **declared** clause mismatches" (`op/O02-probe-registry.md:2-24`;
`op/O03-verdict-contract.md:20-35`). It has no notion of a premise that was not declared. Demonstrated
on the real r43 claims:

```
{"case": "C-counts-only", "status": "fresh",
 "clauses": [{"probe": "count_eq", "measured": 26,  "expect": 26,  "status": "holds"},
             {"probe": "count_eq", "measured": 223, "expect": 223, "status": "holds"}]}
{"case": "O-literal-path-only", "status": "fresh",
 "clauses": [{"probe": "path_absent", "measured": true, "expect": true, "status": "holds"}]}
```

r43 C is stale **only** on ownership; drop that clause and the gate says FRESH. r43 O is stale on
the executed capability; replace it with the literal successor path (`basename-couples-resolver.py`,
absent at baseline) and the gate says FRESH. O05 itself notes that a literal-path gate would pass
claim O (`op/O05-r43-demo.md` §5.1). X02 reached the same count-only result (`cross/X02-honesty.md:219`).

**Required fix at the contract layer.** A claim's material premises must be covered: every atomic
premise in `before` is either checked or explicitly marked `ungrounded` with a reason; any
ungrounded premise makes the claim `could-not-evaluate`, never FRESH. At minimum, the integrator
must reject a check set that does not ground the clause that motivated the claim and the
`after_required` state. A count-only overlay on C must not be admissible evidence for the C
verdict.

### P2 (high) — probe-choice laundering: `grep_absent` can stand in for a capability

r43 O asserts "no durable instrument implements the r39 basename-couples policy". If the check
author chooses `grep_absent` for a token the implementer does not use, the measurement is true and
the claim is FRESH while the behavior exists:

```
$ git show 7ceff59:tools/harness/couples-reference-extractor.py | grep -c 'couples_census'
0
{"status": "holds", "measured": true, "expect": true,
 "detail": "tools/harness/*.py /couples_census/ -> 0 hit(s)"}
```

The document's own anti-theater requirement says the flag must come "from capability/ownership, not
literal text" (`reports/round-47/claims.json:41`). The registry permits a text probe to ground an
absence-of-instrument clause; that is the loophole. **Required fix:** absence-of-instrument clauses
must use `capability_present` (behavioral) or a `path_absent`+`count_eq` pair scoped to the named
artifact; `grep_absent` may not be the sole grounding. A lint in the validator or the review
checklist is enough to enforce it.

### P3 (medium) — a non-discriminative `success_regex` is accepted

The validator rejects regexes that match the empty string, but accepts `.` and `\b`:

```
{"regex": "refs=4\\b", "verdict": "ACCEPTED"}
{"regex": ".",        "verdict": "ACCEPTED"}
{"regex": "PASS",     "verdict": "ACCEPTED"}
{"regex": ".*",       "verdict": "REJECTED: success_regex matches the empty string"}
{"regex": "\\b",      "verdict": "ACCEPTED"}
```

With `success_regex: "."`, a one-line `print('x')` satisfies the declared capability:

```
{"scenario": "S6b-weak-regex-trivial-tool", "status": "mismatch",
 "detail": "1/1 candidate(s) pass the declared behavior: tools/harness/trivial.py"}
```

This is not a two-string lookup — the tool still executes — but it is a weak contract: any
executable can be made the "capability". **Recommendation:** require the regex to contain a literal
run of at least three characters derived from the fixture, or require a declared negative-control
candidate that must fail the same regex. The O07 mutation test covers renames, not degenerate
behavioral specs.

### P4 (medium) — `topic_owner_absent` is alias-bounded; a synonym can false-green

Header ownership is measured correctly when the alias covers the owner's vocabulary. The r43 owner
(`corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:1,3,5`) contains lithic, lapidary, mineral,
stone, gem, gemstone and quarry, so every alias I tested from that family catches it. Synonyms
absent from the header do not:

| alias | measured | verdict with `expect=true` |
|---|---|---|
| `lithic` + `lapidary` | owner found | **STALE** |
| `gemstone`, `stone`, `mineral`, `gem` | owner found | **STALE** |
| `petrology` | 0 owners | **FRESH** (false) |
| `masonry` | 0 owners | **FRESH** (false) |
| `jewellery` | 0 owners | **FRESH** (false) |
| `stonework` | 0 owners | **FRESH** (false) |
| `mineralogy` | 0 owners | **FRESH** (false) |

So "the petrology register is unbuilt" is a novel phrasing that passes while the register is owned.
The probe is honest about its scope (`op/O02-probe-registry.md` §7.3: header fields only, first 200
lines), and it cannot do semantics. **Recommendation:** the `evidence_command` for an ownership
clause must include a synonym sweep over the corpus (the owner's own gap statement shows the form:
`grep -rli 'gemstone' corpus/knowledge/myth-symbol/`), and the reviewer must verify the alias family
against the proposed entry's slug and title stem. Do not claim "novel phrasings are caught" without
this qualification — only phrasings whose aliases are declared are caught.

### P5 (medium, declared) — capability execution is not sandboxed

O02 declares it: a candidate can walk above the fixture root and read the worktree
(`op/O02-probe-registry.md` §3, §7.2). I did not exploit it. It matters only if baseline blobs are
treated as hostile; the current in-repo corpus is not. Record as a limit, not a settlement, and do
not extend the probe to untrusted repositories without a sandbox.

## 5. What I could not test, and what would change the verdict

- **The durable tool is absent**, so every run here is a scratch import or a reference oracle. The
  O claim's "durable not `.scratch`" threshold is not met by construction.
- `reports/round-47/run-validation.py` does not exist, so the O claim's own counting command
  (`reports/round-47/claims.json:43-45`) cannot run at this cut. Its absence is not evidence of
  failure; it is evidence of an unfinished round.
- The O08 assembled file has mtime 16:10 local (after the filed fragments; provenance `to-verify`)
  and may be superseded; the digest is pinned above. The r04 splice (15:09) was stable across every
  run in this critique.
- No hostile execution, no network, no external source. The Ca FRESH result is a **trivial** control
  (the disposition path), as X01 notes (`cross/X01-trades.md:50`); O06's r44 fixture is the
  substantive negative control, and I did not re-derive all nine of its clauses (O08's oracle
  reports 9/9 fresh at `c9f4eaa`, exit 0; `.scratch/o08/o06-fixture.out`).
- My attacks test the O02 registry. They do not prove the O05/K03 evaluator or the O08 oracle are
  equivalent; §3 D3 shows they are not schema-compatible.

**What would change the verdict to PASS for the artifact:** a single durable file with one `main`,
one schema, the part-2 guard removed, the r43 overlay validating in that schema and exiting 1, O06's
negative control exiting 0, the rename/prose mutations still stale, and malformed/no-check inputs
exiting 2/3. §6 lists the exact commands.

## 6. Integrator acceptance gates (must pass before O is admitted)

Run from the lane root after applying the tool; record tool sha, control count and rc, and every
exit code in `reports/round-47/calib/claims-freshness-demo.json`.

1. **One entry point, one schema.**
   ```
   grep -c '^def main' tools/harness/claims-freshness.py        # >= 1
   grep -n '^if __name__' tools/harness/claims-freshness.py     # the only guard must call main()
   python3 tools/harness/claims-freshness.py --help              # exit 0, no controls run
   ```
2. **Whole-tool selftest**, count computed from the registry, not a literal:
   ```
   python3 tools/harness/claims-freshness.py --selftest          # green, exit 0
   ```
   It must include parser/baseline/verdict/exit controls (O04's 46/46 set or equivalent), not only
   O02's 43 probe controls.
3. **r43 positive regression, in the landed schema:**
   ```
   python3 tools/harness/claims-freshness.py \
     --claims reports/round-43/claims.json \
     --checks reports/round-47/calib/r43-checks.json
   # O STALE, C STALE, Ca FRESH; summary fresh=1 stale=2; exit 1; REFUSE names O and C
   ```
   Every check in the overlay must validate under the landed schema. If the tool is in-file-only,
   use the annotated copy at `reports/round-47/calib/r43-claims-annotated.json` (`op/O12-scribe.md`
   §6.3), once filed, instead of `--checks`; the requirement is the verdict, not the flag spelling.
   If the overlay is rewritten, the rewrite is a new artifact with its own digest and the O05 demo
   must be re-run.
4. **Negative control:** O06's fixture at `c9f4eaa` → FRESH, exit 0; the same fixture at HEAD must
   turn O STALE (baseline-vs-worktree discriminator).
5. **Anti-theater:** rename the witness in a synthetic baseline and mutate the r43 prose/targets;
   the verdict must remain O/C STALE. My S3/S4/S5 are the minimal controls.
6. **Exit contract:** malformed claims → exit 2; no checks → exit 3 (or another non-zero per the
   landed contract); malformed JSON → exit 2; unknown flag → exit 2. None may be 0. The current
   splice fails all four (D1).
7. **Policy lint:** reject a check set whose material premises are ungrounded (P1), and reject
   `grep_absent` as sole grounding for an absence-of-instrument clause (P2). Require a
   non-discriminative-`success_regex` check (P3) and a synonym sweep for ownership clauses (P4).

Until gates 1–6 pass, the O claim is `could-not-evaluate`, not improved. This is the same
instruction O12 gives the integrator (`op/O12-scribe.md:413-417`); this critique adds the exact
failure modes that make a superficially green run unacceptable.

## 7. Reconciliation with the other critics and reviewers

- **O12** (`op/O12-scribe.md:12-30`): agrees the durable tool is absent and the verdict is
  `unprovable-but-better`. This fragment adds D1 (the splice is a false green), D2 (no `main` in any
  fence), and D3 (the r43 overlay is rejected by the registry), none of which are visible from the
  seat reports alone.
- **X01** (`cross/X01-trades.md:155-175`): T6 says the *prototype* fails all three trap families and
  the durable tool is absent. I agree on the prototype; the distinction I add is that the **O02
  registry method** passes the behavioral attacks in §2. The prototype's failures (O09 T1–T3) are a
  reason to build the new tool, not evidence that the method is theater.
- **X01 T5** (`:50`): "the gate's r43 Ca FRESH is theater" — correct as a warning about the trivial
  control; my novel Ca repeats that triviality deliberately, and O06 is the substantive control.
- **X02** (`cross/X02-honesty.md:173-235`): agrees the durable tool is absent and that a count-only
  gate flags 0 of 2 stale claims; my P1 reproduces that result on the O clause as well.
- **R02** (`review/R02-review.md:250`): "could-not-evaluate on the deliverable; no axis harm" —
  agrees. The method is demonstrated; the artifact is not.
- **Prior X03 scratch (unfiled, `to-verify`)**: `.scratch/x03/attack-run.txt` (mtime 15:04) scores
  12/29 against the **r44 prototype** (`ref-eval.py`), not against the O02 registry. Its failures —
  renamed tool hides the capability (A6), path dependence (A7), llama false STALE (B1), irrelevant
  probe passes (D1) — are prototype defects consistent with O09/O10/O13. A6/A7 are precisely the
  behaviors my S3/S4 show the O02 registry handles; D1 is the policy hole I record as P1. Do not
  read the 12/29 as a result for the registry under test.

## 8. Evidence appendix

### 8.1 Commands

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B .scratch/x03/attack.py > .scratch/x03/attack.out 2>&1    # exit 0
python3 .scratch/r04/assembled/claims-freshness.py --claims reports/round-43/claims.json
python3 .scratch/r04/assembled/claims-freshness.py --claims .scratch/x03/malformed.json
python3 .scratch/o08/claims-freshness.py --selftest
python3 .scratch/o08/claims-freshness.py --claims .scratch/x03/novel-o08.json
python3 .scratch/o05/claims-freshness-k03.py --claims reports/round-43/claims.json \
  --checks .scratch/x03/o02-canonical-overlay.json
```

### 8.2 Key digests

| item | sha256 |
|---|---|
| `reports/round-43/claims.json` | `9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b` |
| `reports/round-47/claims.json` | `7eb16979ba88bb43a61553c6b62168854f6fe2e2f98852dc14affe45f9e1fa34` |
| `.scratch/r04/assembled/claims-freshness.py` | `5a5635dfc0ea33639ad29b7e625e5b0095ecc9263e63941edec4b47f5fc0e9f0` |
| `.scratch/o08/claims-freshness.py` | `3bcbeb67fb1111d31a6960c9a9a3c22740c925b512ab46a2a731677a85357919` |
| `.scratch/o05/claims-freshness-k03.py` | `f35eab201910f42c4184391c24de63a721fed859ad419575599f4ff02412b910` |
| `.scratch/o08/claims-freshness.assembled.py` | `5aa0f8cd500023b7a0da02b4e7dd8f0a492ccb66047431bf090b5b41710d58a9` |

### 8.3 Minimal reproduction of the two decisive checks

The decisive policy-layer result (P1) and the anti-theater result (S3) can be reproduced without
the full harness:

```python
import importlib.util, sys
spec = importlib.util.spec_from_file_location("cf", ".scratch/r04/assembled/claims-freshness.py")
cf = importlib.util.module_from_spec(spec); sys.modules["cf"] = cf; spec.loader.exec_module(cf)

tree = cf.Baseline(".", "7ceff59")
# P1: r43 C with only its two true count clauses -> FRESH
chk = lambda cid, clause, target, expect: {
    "id": cid, "clause": clause, "probe_kind": "count_eq",
    "target": target, "expect": expect, "evidence_command": "git ls-tree 7ceff59"}
claim = {"id": "C",
  "before": "myth-symbol 26 (lithic slot named but unbuilt); total 223",
  "before_checks": [chk("C-2", "myth-symbol 26", {"glob": "corpus/knowledge/myth-symbol/*.md"}, 26),
                    chk("C-3", "total 223", {"glob": "corpus/knowledge/*/*.md"}, 223)]}
checks = cf.validate_claim_checks(claim)
print(cf.claim_status([cf.evaluate_check(c, tree) for c in checks]))   # fresh
```

The rename/decoy controls need an in-memory tree implementing `files/exists/read/sha256`; the full
harness in `.scratch/x03/attack.py` is the authoritative version (S3/S4 in its output).

### 8.4 What I did not write

No `corpus/` file, no `tools/` file, no `reports/round-1..46/**` byte, no queue or manifest edit.
This fragment drafts no landing; the integrator applies the O tool and the C entry. The only
artifacts this seat produced are this file and `.scratch/x03/*` (scratch, not a deliverable).
