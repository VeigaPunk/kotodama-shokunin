# V02 — independent gate verification: the r43 regression reproduces, the instrument is not landable

- Seat: `V02` | role verifier (non-author of O01–O06) | claim **O** (operability) | round 47, loop 2
- Out path: `reports/round-47/op/V02-gate-verify.md` (this seat's only durable write)
- Mission (`reports/round-47/targets.json:65`): "Independent gate verifier: after the integrator applies the freshness tool, run --selftest + the r43 demo from the durable path; confirm green + correct flags."
- Contract: `reports/round-47/claims.json:36-48` (O claim; after_required `:41`; thresholds `:47`)
- Cut: 2026-10-19T19:17Z; HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe`; `git status --porcelain` → `?? reports/round-46/review/`, `?? reports/round-47/` only
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root
- Boundary: no filed byte edited, no corpus staging, no `reports/round-*/run-validation.py`, no git mutation, no network. The extracted parts, adapter, fixtures and transcripts live only under `.scratch/v02/`.

## 0. Verdict

**The mission's named check cannot be performed: the durable path does not exist. That is `could-not-evaluate`, not green.**

`tools/harness/claims-freshness.py` is absent both at HEAD and in the worktree. The claim's first two counting commands therefore fail, and no `--selftest` or r43 demonstration can be run "from the durable path" (`claims.json:42-46`).

I did not stop at the absence. I reconstructed the exact O01+O02+O03 assembly from the filed fenced bodies (all three digests match the authors' published SHA-256), and measured its semantics through a verifier-local adapter. **The measurement layer works and the r43 regression is correct.** But the fragments **cannot be landed as plain concatenation**, and the only executable concatenation is a false green. Table:

| check the claim requires | durable path | reconstructed assembly (verifier adapter) |
|---|---|---|
| `--selftest` green | **absent** — `python3: can't open file … No such file or directory`, exit 2 | **43/43**, exit 0 (O02 registry selftest) |
| r43 O and C STALE, Ca FRESH | not runnable | **O stale 2/2, C stale 1/3, Ca fresh 1/1; exit 1** |
| negative control not flagged | not runnable | **3 fresh, 9/9 clauses, exit 0** at `c9f4eaa` |
| anti-theater still flags | not runnable | **stale** from measured capability; the literal path check holds |
| `could-not-evaluate != green` | not runnable | **exit 3** |
| durable, not `.scratch` | **fails** — no file | n/a (draft only) |
| filed demonstration at `reports/round-47/calib/` | **absent** — no `r43-checks.json`, no negative-control file | n/a |

Two independent findings are decisive for the integrator:

1. **Plain concatenation does not parse.** O01 says "The assembly is plain concatenation" (`op/O01-tool-core.md:23`), but O02 and O03 each carry `from __future__ import annotations` inside their fenced body (`O02:315`, `O03:108`), so `cat part1 part2 part3` is a `SyntaxError`.
2. **The minimal syntax fix yields a false green.** O02 ends with `if __name__ == "__main__": sys.exit(selftest_registry())` (`O02:1220-1221`) and no part defines `main()` or `argparse` (O01 concedes "No CLI yet", `O01:798`; O03 offers a sketch, not an entry point, `O03:683`). After hoisting the future imports, **every** invocation — `--selftest`, `--claims <r43>`, `--help` — prints `PROBE-REGISTRY SELFTEST: 43/43` and exits **0** without reading the claims file. Landed as-is, the claim's own green check would pass while the gate evaluated nothing.

R04 independently reached the same verdict on the durable-path and false-green points (`review/R04-gate.md:13`, §3.2). This seat adds the measured reconstruction, the negative control, the anti-theater control and the exit-code checks, and names the schema work the integrator must do before a landing can be verified at all.

## 1. What exists at the cut

```
$ ls tools/harness/claims-freshness.py
ls: cannot access 'tools/harness/claims-freshness.py': No such file or directory
$ git cat-file -e 6e9a30d:tools/harness/claims-freshness.py
fatal: path 'tools/harness/claims-freshness.py' does not exist in '6e9a30d'
$ python3 tools/harness/claims-freshness.py --selftest
python3: can't open file '…/tools/harness/claims-freshness.py': [Errno 2] No such file or directory
exit=2
```

The two required `calib/` demonstration artifacts are also unfiled:

```
$ ls reports/round-47/calib/ | grep -E 'r43-checks|negative-control|claims-freshness'
(no output)
```

The O seat set is incomplete at this cut: `O07` (anti-theater), `O08` (independent verify), `O11` (baseline-eval), `O14` (determinism), `O15` (malformed) and `W01` (landing spec) are absent from `reports/round-47/op/`; `X03` (gate-theater critic) is absent from `cross/`. A complete 64-seat census puts 55 out paths filed at 19:17Z (54 before this file; R04 landed at 19:15Z). This seat's verdict is therefore also an evidence-chain statement, not only a tool statement: the O claim cannot be closed from the filed set as it stands.

## 2. Reconstruction — byte fidelity first

Extracted with a fence-aware reader (the first `python` fence in each file, trailing newline preserved), then verified against each author's published digest:

| part | source | lines | sha256 | matches author |
|---|---|---|---|---|
| O01 core | `op/O01-tool-core.md:160-794` | 633 | `72c294f2c49dc53f3f7e7e65b0dc646e238a56b19473f84b63f1cb5bbf13b876` | yes (`O01:13-14`) |
| O02 registry | `op/O02-probe-registry.md:254-1222` | 967 | `a60b0a22df2d73c1a4075662d76a1d5c25a5caa8f6f35b72ffdf0c2ed772c191` | yes (`O02:1224`) |
| O03 verdict | `op/O03-verdict-contract.md:86-574` | 487 | `097a31987cc334d93eaa117e60d7112cddeb7fbf9a356d10ca4dc178721cfcef` | yes (`O03:84`) |

So the defects below are in the filed bytes, not in extraction.

### 2.1 Assembly as documented

```
$ cat part1.py part2.py part3.py > assembled-draft.py
$ python3 -B assembled-draft.py --selftest
  File "assembled-draft.py", line 693
    from __future__ import annotations
SyntaxError: from __future__ imports must occur at the beginning of the file
exit=1
```

`grep -cE 'argparse|def main\(|--selftest|add_argument' assembled-draft.py` → **1**, and that one hit is a docstring mention. There is no entry point.

### 2.2 Minimal syntax fix — the false green

All three future imports hoisted to line 1 (nothing else changed):

```
$ python3 -B assembled-syntaxfixed.py --claims reports/round-43/claims.json
PASS S13 destructive evidence_command rejected
PROBE-REGISTRY SELFTEST: 43/43
exit=0
$ python3 -B assembled-syntaxfixed.py --selftest
PROBE-REGISTRY SELFTEST: 43/43
exit=0
$ python3 -B assembled-syntaxfixed.py --help
PROBE-REGISTRY SELFTEST: 43/43
exit=0
```

Cause: the `__main__` guard from part 2 executes before any argument parsing; part 3's functions are never called. The output is identical for every argv, so the mode is not observable from stdout but the exit-0 is. Transcript: `.scratch/v02/out/concat-syntaxfixed-{claims,selftest,help}.txt`.

### 2.3 The seam is declared, but not implemented

O03 §8 sketches the adapter (`O03:683-714`) and its names do not match the parts it says to call:

| O03 sketch | actual part | measured consequence |
|---|---|---|
| `header, claims = load_claims(path)` (`:686`) | `load_claims` returns a `ClaimsDoc` (`O01:348-446`) | unpacking a dataclass raises `TypeError` |
| `resolve_baseline(header["baseline_commit"])` (`:687`) | `open_baseline(root, commit_input)` / `Baseline` (`O01:583-601`) | `NameError` |
| `validate_check(check, claim["id"], index)` (`:693`) | `validate_check(check, before_text, seen_ids=None)` (`O02:312`) | claim id is passed where the `before` string is expected |
| `evaluate_check(check, baseline)` returning `ClauseResult` (`:696-697`) | returns a dict with `status` ∈ `holds/mismatch/could-not-evaluate` (`O02:687`, `:650-656`) | O03 normalises to `HOLDS/CONTRADICTED/NOT_EVALUATED` (`O03:138`) and downgrades `MISMATCH` to `NOT_EVALUATED` (`O03:172-184`) |

The status mismatch alone means a real contradiction would be reported `could-not-evaluate` / exit 3, not `stale` / exit 1, if the sketch were followed literally. R04 measured the same downgrade (`review/R04-gate.md:§3.3`).

## 3. Verifier-local adapter — what the fragments' semantics actually do

To measure the method rather than the missing file, I wrote `.scratch/v02/run_gate.py`: it imports the three parts as modules, maps O01 `Check` dataclasses to O02 dicts, maps O02 statuses (`holds`→`HOLDS`, `mismatch`→`CONTRADICTED`, `could-not-evaluate`→`NOT_EVALUATED`), maps `expect`/`detail` to `expected`/`reason`, and calls O03's `judge_claim` and `build_report`. **This adapter is verifier-local; it is not a proposed landing and is not filed.** Its purpose is to answer: if the integrator fixes the seams as described in §4, do the required verdicts follow?

### 3.1 Registry selftest

```
$ python3 -B part2.py
[… 43 PASS lines …]
PROBE-REGISTRY SELFTEST: 43/43
exit=0
```

All seven kinds are exercised by both polarities; S7 is the renamed-tool control (`O02:1066-1092`). Transcript: `.scratch/v02/out/selftest-registry.txt`, sha256 `0cd51f53…71ca0`.

### 3.2 r43 positive regression at `7ceff59`

Input: filed `reports/round-43/claims.json` (sha256 `9662e2bd…bc174b`, unchanged), plus `.scratch/v02/r43-checks-o02.json`, a verifier transformation of O05's K03 overlay into O02's target schema. The six premises are O05's; two clause strings were extended to the exact wording of the r43 `before` so they bind verbatim, and no premise was added or dropped.

```
claims-freshness: round 43 baseline 7ceff59 (7ceff59a0216a8ea21ee43262d9fc72abf770cee)
  [O] STALE             2/2 clauses contradict
      clause 0 (capability_present): measured=True expected=False -- no durable instrument implements the r39 basename-couples policy
      clause 1 (capability_present): measured=True expected=False -- the only resolver that ever ran (r39 I-C05) lives in ephemeral .scratch
  [C] STALE             1/3 clauses contradict
      clause 0 (topic_owner_absent): measured=False expected=True -- lithic slot named but unbuilt since r42's C01/C04 collision routed this draft to spare
  [Ca] FRESH             1/1 clauses hold
summary: 1 fresh, 2 stale, 0 could-not-evaluate, 0 malformed; clauses 6 (3 hold, 3 contradict, 0 not evaluated)
REFUSE: claim(s) O, C have a `before` already false at 7ceff59; do not dispatch.
exit 1
```

This is clause-for-clause the result O05 §1/§4 reported (`op/O05-r43-demo.md:13-19,181-205`): O's two capability clauses contradict; C's ownership clause contradicts while both counts hold (`myth-symbol 26`, `total 223`); Ca's artifact is absent at baseline. The flag is not a prose match — the two C counts holding while the ownership leg fails is the r43 defect shape (`reports/round-44/review/R01-review.md:228-231`).

**Baseline scope, not worktree.** Re-run with `--at HEAD` (override recorded as a deviation in the report; still a committed tree):

```
[O] STALE 2/2 … [C] STALE 1/3 … [Ca] STALE 1/1
summary: 0 fresh, 3 stale …
exit 1
```

Ca flips fresh→stale because `reports/round-43/calib/dispositions-r38-r39.json` exists at HEAD but not at `7ceff59`. A worktree-reading gate would have produced that false positive at the declared baseline; the reconstruction does not. Observation for the durable CLI: the refusal line still says "at 7ceff59" under `--at HEAD`, because `baseline_commit` is the declared value, not the evaluated one — the report should name the evaluated baseline alongside the deviation.

### 3.3 Negative control at `c9f4eaa`

Input: O06's clauses and target values (`op/O06-negative-control.md:78-179`), transformed to O02's object-target schema. Every clause is a verbatim substring of its claim's `before`.

```
claims-freshness: round 44 baseline c9f4eaa (c9f4eaa707b6e977ff6e1616463e91f4b8afea5d)
  [O] FRESH             5/5 clauses hold
  [C] FRESH             2/2 clauses hold
  [Ca] FRESH             2/2 clauses hold
summary: 3 fresh, 0 stale, 0 could-not-evaluate, 0 malformed; clauses 9 (9 hold, 0 contradict, 0 not evaluated)
exit 0
```

Discriminator: at HEAD the same control flips O stale (2/5 clauses: the resolver path is now present, and there are 2 `*couples*.py` files, not 1), while C and Ca stay fresh:

```
  [O] STALE             2/5 clauses contradict
      clause 0 (path_absent): measured=False expected=True -- no four-class census authority exists
      clause 1 (count_eq): measured=2 expected=1 -- the r42 six-class extractor is the only tool
summary: 2 fresh, 1 stale …
exit 1
```

So the control is a real baseline test, not a tautology: a gate that read the worktree would wrongly flag it, and the reconstruction does not.

### 3.4 Anti-theater — the flag comes from behavior, not the literal name

Synthetic claim at `7ceff59` whose `before` names the **absent successor path**:

- `MUT-1` capability: run every `tools/harness/*.py` with `--census` against the wrapped-couples fixture, success iff `refs=4`; `expect=false` (no capability).
- `MUT-2` literal: `path_absent tools/harness/basename-couples-resolver.py`, `expect=true`.

```
  [MUT] STALE             1/2 clauses contradict
      clause 0 (capability_present): measured=True expected=False -- no basename-couples capability exists
summary: 0 fresh, 1 stale …
exit 1
```

`MUT-2` holds (the named path is genuinely absent at `7ceff59`), yet the claim is stale because the capability is found in the differently named `couples-reference-extractor.py`. A two-string lookup keyed on the claim's own path would have called this fresh. This is the anti-theater property the claim requires, measured against the baseline bytes; O07 owns the stronger mutation battery, which is unfiled at this cut.

### 3.5 Exit contract

| input | verdict | exit | transcript |
|---|---|---|---|
| all clauses hold (`c9f4eaa` control) | fresh | **0** | `out/negative.txt` |
| any clause contradicts (r43; anti-theater) | stale | **1** | `out/r43.txt`, `out/anti-theater.txt` |
| missing `baseline_commit` | malformed | **2** | `out/missing-baseline.txt` |
| unknown probe kind (`capability_vibes`) | malformed | **2** | `out/unknown-kind.txt` |
| claim with no declared checks | could-not-evaluate | **3** | `out/no-checks.txt` |

`could-not-evaluate` is non-zero, satisfying `claims.json:47`. Determinism: two runs of the r43 demo produced the same `decision_sha256` (`69a2a0f53b1770eb…`) and the same exit 1 (`out/run1.json`, `out/run2.json`).

## 4. Blockers the integrator must clear before a landing can be verified

These are ordered by severity. Each is measured, not inferred.

**B1 — Durable path and demonstrations absent.** `tools/harness/claims-freshness.py` absent at HEAD and worktree; `reports/round-47/calib/` has no `r43-checks.json` or negative-control artifact. The O claim's `after_required` (`claims.json:41`) is unmet on every durable-artifact clause.

**B2 — The parts are not concatenable as documented.** `O01:23` says plain concatenation; the result is a `SyntaxError` at the second `from __future__` (assembled line 693). The assembly must import the parts as modules or hoist one future import and strip the others; that edits bytes O01 says need no edit.

**B3 — The only executable assembly false-greens.** After the minimal syntax fix, O02's `__main__` runs the registry selftest for every argv and exits 0, including `--claims <stale file>` and `--help`. Any landing that follows O01's assembly instruction inherits this. A CLI must be authored: `--claims`, `--checks`, `--at`, `--selftest`, `--json`, exit mapping from `build_report`.

**B4 — Status vocabulary mismatch at the O02→O03 seam.** O02 emits `holds|mismatch|could-not-evaluate` (`O02:687`); O03 accepts `HOLDS|CONTRADICTED|NOT_EVALUATED` and turns anything else into `NOT_EVALUATED` (`O03:138,172-184`). Unmapped, a contradiction becomes exit 3 (false acquittal). The adapter's three-line map is in `.scratch/v02/run_gate.py:30-34`; the same map belongs in the landed tool, with a selftest control that pins it.

**B5 — O01 rejects the typed probes O02 implements.** O01's in-file parser requires `expect` to be a JSON boolean (`O01:472-474`), but O02's value types are `count_eq:int` and `sha256_eq:str` (`O02:555-562`). Measured: an in-file `count_eq expect:1` is rejected `before_checks[1] expect is not boolean`, exit 2. The negative control only ran because its checks were moved to an overlay, bypassing O01's parser. A landed tool that accepts only in-file `before_checks` cannot express counts or digests.

**B6 — Four check dialects are in play.** (a) O02 in-file: object targets, `probe_kind`, typed `expect`; (b) O05/K03 overlay: object targets with different keys (`capability`+`scope`, `value` inside `target`, `topics`/`partition`), boolean `expect`; (c) O06: string targets and `path::regex`, key `kind`; (d) O04's selftest seam: `FixtureBaseline`, `evaluate_claim`, `CAPABILITIES`, `SchemaError`, "8 kinds" (`O04:189-194`). Measured by this seat against O02's validator: O05's overlay is **5/6 rejected** (`capability_present target has unknown key(s): capability, scope`; `count_eq expect must be a JSON integer, got True`; `topic_owner_absent target has unknown key(s): partition, topics`), and O06's fixture is **9/9 rejected** (`target must be an object`, plus three clause substrings that do not match). R04 reports the same counts (`review/R04-gate.md:§3.4`). The integrator must pick one input schema and either rewrite the demos or ship a documented transform; a tool cannot accept all four.

**B7 — O04's selftest is not a drop-in.** It calls `evaluate_claim`, `FixtureBaseline`, `CAPABILITIES` and `SchemaError`, none of which exist in O01–O03 (`grep` in the assembled parts: zero hits). The claim's `--selftest` green must therefore be demonstrated by a selftest authored against the landed API, not assembled from O04's body unchanged.

**B8 — O evidence chain incomplete.** O07, O08, O11, O14, O15, W01 and X03 are unfiled at this cut. Their subjects are exactly the controls this seat cannot replace: the mutation battery (O07), the second independent run (O08), the baseline-vs-worktree witness (O11), determinism (O14), malformed inputs (O15), and the apply instructions (W01). My §3 covers their *questions* on the reconstruction, but the round still owes independent, non-V02 evidence for them.

## 5. Required post-landing verification (exact re-run)

When the integrator lands a reconciled tool, this seat's check is satisfied only by the following, from the durable path. Expected values are the ones the reconstruction measured; a mismatch is a finding, not a threshold to reinterpret.

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1

# 1. Durable path exists and is a file
test -f tools/harness/claims-freshness.py || echo "ABSENT"

# 2. Selftest green, and the selftest actually exercises the gate
python3 tools/harness/claims-freshness.py --selftest
echo "exit=$?"                       # expect 0

# 3. r43 positive regression (filed overlay required under calib/)
python3 tools/harness/claims-freshness.py \
  --claims reports/round-43/claims.json \
  --checks reports/round-47/calib/r43-checks.json
echo "exit=$?"                       # expect 1

# 4. Negative control
python3 tools/harness/claims-freshness.py \
  --claims reports/round-47/calib/negative-control.claims.json
echo "exit=$?"                       # expect 0

# 5. Pinned machine-readable decision (two runs must match)
python3 tools/harness/claims-freshness.py --claims reports/round-43/claims.json \
  --checks reports/round-47/calib/r43-checks.json --json | sha256sum
```

Expected r43 verdict lines: `O` STALE (both capability clauses), `C` STALE (ownership only; `myth-symbol 26` and `total 223` hold), `Ca` FRESH, summary `fresh=1 stale=2`, refusal naming O and C. Whether the landed CLI emits O02's lowercase statuses or O03's uppercase ones is immaterial; the verdicts, clause counts and exit codes above are the contract.

The `calib/` artifacts do not exist yet; the integrator must file them from `op/O05-r43-demo.md:101-158` (K03 form) and `op/O06-negative-control.md:78-179` (in-file form), reconciled to the landed schema under B6. This seat cannot file them: `reports/round-47/calib/` is outside its out path.

## 6. Bounds and unknowns

- **No claim that the durable tool will behave like this reconstruction.** The semantics are the fragments'; the adapter, schema transformations and fixtures are mine. A landed tool that maps differently can differ. B4/B5 are precisely the places it can.
- **The r43 O check here is behavioral, not O05's `couples_census`.** O02's registry has no named-capability form; I encoded O05's capability clause as "run each baseline `tools/harness/*.py` with `--census` on the wrapped fixture, success iff `refs=4`", the same shape O02 used for its measured run (`O02:87-106`). The verdict is unchanged, but the durable tool must implement whichever form it declares, and O05's overlay as filed uses the other one.
- **Capability execution is not sandboxed** (declared in `O02:§7`): candidates run as `python3 -I -B` in a temp tree but can read above it. For an absence claim (`expect:false`), R04 measured that a candidate which executes and exits non-zero is treated as "no capability" (`review/R04-gate.md:§3.1`) — a present capability can be laundered as absent by an incomplete fixture. The r43 O checks are absence claims. This seat did not exploit that edge (its fixture is the live wrapped field and the witness exits 0), but the landed tool should treat a non-zero candidate as `could-not-evaluate` for absence claims, or state the limitation at the point of use.
- **`--at` report labelling.** Under an override the human refusal names the declared baseline (`at 7ceff59`) while measuring HEAD. The deviation is recorded, but the refusal text should name the evaluated commit; otherwise a reader can misattribute the verdict. `to-verify` against the landed CLI.
- **No post-landing check performed.** This file is the pre-landing ceiling. When the tool lands, V02's out path is already written; the integrator must re-run §5 and file the result as a new round-47 verification artifact (an append, not an edit of this file).
- **Seat census is a moving target.** 55/64 out paths exist at 19:17Z (this file included); R04's file landed at 19:15Z. B8's missing list was measured at 19:17Z and may shrink.

## 7. Reproduction ledger

Scratch artifacts (not durable deliverables; hashes pin the exact bytes used):

| path | sha256 |
|---|---|
| `.scratch/v02/part1.py` (+NL) | `72c294f2c49dc53f3f7e7e65b0dc646e238a56b19473f84b63f1cb5bbf13b876` |
| `.scratch/v02/part2.py` (+NL) | `a60b0a22df2d73c1a4075662d76a1d5c25a5caa8f6f35b72ffdf0c2ed772c191` |
| `.scratch/v02/part3.py` (+NL) | `097a31987cc334d93eaa117e60d7112cddeb7fbf9a356d10ca4dc178721cfcef` |
| `.scratch/v02/run_gate.py` | `dc783a72bacf94864268d5f6e31a72383a3888f5077a714a385be66106288a1c` |
| `.scratch/v02/r43-checks-o02.json` | `dc51dc783d27555c3635842d451d6febed9124e483f453f962e344728527d3b5` |
| `.scratch/v02/negative-control.claims.json` | `6dc288ac70cf7d5337315af1aed2db21cb8be763cd871061d045cfb6903ad754` |
| `.scratch/v02/negative-control.checks.json` | `43917401845ccfcd09645f3de437d553418e7c850e428a738dc62d2ae0a2246d` |
| `.scratch/v02/anti-theater.claims.json` | `c729253a584feb3b6489254369c0d0744b651fce07a3aa4831f6665b299b6389` |
| `.scratch/v02/run1.json` | `f4a15d21de78906e5035def7bc734e6fb7ae3c959cd8d77fdfd968b17b62e242` |

Transcripts under `.scratch/v02/out/`: `r43.txt` `94269fbe…92f2cf`, `r43-at-head.txt` `74d3c656…81649`, `negative.txt` `254fdc04…e288da`, `negative-at-head.txt` `e99e0586…99e56`, `anti-theater.txt` `02f3623a…26e341`, `no-checks.txt` `46bd62e6…875f`, `missing-baseline.txt` `a9a02aca…3fa4b`, `unknown-kind.txt` `75ce550e…5433`, `selftest-registry.txt` `0cd51f53…71ca0`, `concat-selftest.txt` `bace994d…24c7c`.

Commands, in order: `python3 -B part2.py`; `python3 -B run_gate.py --claims reports/round-43/claims.json --checks r43-checks-o02.json [--at HEAD]`; the same against the two negative-control files; the anti-theater pair; `no-checks`, `missing-baseline`, `unknown-kind`; `cat part1.py part2.py part3.py > assembled-draft.py && python3 -B assembled-draft.py --selftest`; the syntax fix and three invocations. Boundary re-check at close: `git status --porcelain` → only the two pre-existing untracked round paths; no file under `corpus/`, `tools/`, `reports/round-43/` or `reports/round-1..46/` was written.

## 8. Ledger

| item | value |
|---|---|
| seat | V02, verifier, claim O |
| durable writes | `reports/round-47/op/V02-gate-verify.md` only |
| durable path under test | absent → mission `could-not-evaluate` |
| reconstruction verdict | O stale / C stale / Ca fresh at `7ceff59`; exit 1 |
| negative control | fresh 9/9 at `c9f4eaa`; exit 0; HEAD discriminator stale |
| anti-theater | stale from capability while the literal path check holds |
| exit contract | 0 fresh / 1 stale / 2 malformed / 3 CNE, all measured |
| blockers filed to integrator | B1–B8 (§4) |
| next touch | integrator lands reconciled CLI + `calib/` overlays; re-run §5 from the durable path |
