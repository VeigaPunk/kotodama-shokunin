# O14 — determinism verification: the assembled draft is byte-stable, the durable tool is absent

- Seat `O14` | role verifier | claim **O** (operability) | round 47, loop 2
- Out path: `reports/round-47/op/O14-determinism.md` — the only path this seat writes under `reports/round-47/`
- Mission: `reports/round-47/targets.json` seat `O14` — "run the gate twice on the same inputs — identical verdict + identical exit code (no timestamp/random nondeterminism in the flag decision)"
- Round baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`); declared `6e9a30d` (`reports/round-47/claims.json:7`)
- Measurement cut: **2026-10-19T19:22Z** (UTC), first measurements 18:10Z. All commands run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; Python 3.14.7, git 2.55.0.
- Boundary: no filed byte edited; nothing staged under `corpus/`; no `reports/round-*/run-validation.py`; no git commit/push/install/network; no ref mutation. Scratch work is under `.scratch/o14/`; the durable artifacts cited below are the sibling fragments plus this file.

## 0. Verdict at this cut

| subject | status | basis |
|---|---|---|
| Durable `tools/harness/claims-freshness.py` | **ABSENT → could-not-evaluate** | `ls` → no such file; `git cat-file -e 6e9a30d:tools/harness/claims-freshness.py` → rc 128 |
| Assembled draft (O01+O02+O03) — full probe→verdict path | **deterministic** | 11-run matrix, 7 orthogonal perturbations, 4 parallel runs, in-process repeat: one stdout sha256, one `decision_sha256`, one exit code |
| Assembled draft **as filed** (no adapter) | **deterministic but semantically broken** | every genuine mismatch becomes `NOT_EVALUATED`; r43 run exits 3, never 1 (§5 F-O14-2) |
| Verdict classes tested | **deterministic** | fresh → 0, stale → 1, no-checks → 3, malformed → 2; each run twice, byte-identical |
| `decision_sha256` scope | **hazard** | any `observed_at`/`generated_at` field changes the digest, though not verdict/exit (§5 F-O14-5) |
| Durable-path proof of claim O | **could-not-evaluate** | the tool does not exist; this seat proves determinism of the drafted decision path, not of a landed tool |

**Bottom line.** Determinism itself passes, and it passes in the strong form: the drafted report is byte-identical, not merely verdict- and exit-identical. The qualification is the deliverable: the assembled draft cannot currently produce the claim's required r43 result without a vocabulary adapter, and the filed demonstration schema (K03/O05) is not the schema O01/O02 parse. Those are join defects, not nondeterminism, and they are listed in §5 for the integrator.

## 1. Subject: what was actually run

### 1.1 The durable target does not exist

```
$ ls tools/harness/claims-freshness.py
ls: cannot access 'tools/harness/claims-freshness.py': No such file or directory
$ git cat-file -e 6e9a30d:tools/harness/claims-freshness.py; echo rc=$?
fatal: path 'tools/harness/claims-freshness.py' does not exist in '6e9a30d'
rc=128
$ git ls-tree -r --name-only HEAD tools/harness/ | grep -c claims-freshness
0
```

The only executable gate bytes in the tree are the three fenced drafts landed by O01–O03 at `reports/round-47/op/`. This seat assembled them without editing either fragment.

### 1.2 Assembly provenance

| part | source fenced block | extracted lines | sha256 | corroboration |
|---|---|---|---|---|
| 1/3 core + baseline | `reports/round-47/op/O01-tool-core.md:161-793` | 633 | `72c294f2c49dc53f3f7e7e65b0dc646e238a56b19473f84b63f1cb5bbf13b876` | matches O01 §1's declared digest |
| 2/3 probe registry | `reports/round-47/op/O02-probe-registry.md:255-1221` | 967 | `a60b0a22df2d73c1a4075662d76a1d5c25a5caa8f6f35b72ffdf0c2ed772c191` | — |
| 3/3 verdict contract | `reports/round-47/op/O03-verdict-contract.md:87-573` | 487 | `097a31987cc334d93eaa117e60d7112cddeb7fbf9a356d10ca4dc178721cfcef` | matches O03 §11's declared digest |
| assembled module | `.scratch/o14/gate_draft.py` | 2,006 | `6a521e92948215884f6f96abfa12588401b413d30d308796ec69acd112ee7aa7` | 75,882 bytes; reproduced by the recipe below |

Two non-semantic assembly edits were required and are declared here:

1. `part2.py` and `part3.py` each carry their own `from __future__ import annotations` and module docstring. Only the first occurrence is legal in one module, so the later headers were dropped; no statement was changed.
2. `part2.py` ends with `if __name__ == "__main__": sys.exit(selftest_registry())`. It was removed from the assembly so the module could be imported; the selftest itself was run separately (§3.5).

Assembly recipe (reproduces the 2,006-line module from the filed fragments only):

```python
import pathlib
def block(path, start, end):
    return "".join(pathlib.Path(path).read_text().splitlines(keepends=True)[start-1:end])
def after_future(text):
    lines = text.splitlines(keepends=True)
    i = next(i for i, line in enumerate(lines)
             if line.startswith("from __future__ import annotations"))
    return "".join(lines[i+1:])

p1 = block("reports/round-47/op/O01-tool-core.md", 161, 793)
p2 = after_future(block("reports/round-47/op/O02-probe-registry.md", 255, 1221))
p2 = p2.replace('\nif __name__ == "__main__":\n    sys.exit(selftest_registry())\n', '\n')
p3 = after_future(block("reports/round-47/op/O03-verdict-contract.md", 87, 573))
pathlib.Path(".scratch/o14/gate_draft.py").write_text(
    p1 + "\n# ---- part 2 (O02): probe registry ----\n" + p2
       + "\n# ---- part 3 (O03): verdict contract ----\n" + p3)
```

The driver that calls the assembled API is `.scratch/o14/run_gate.py`, 85 lines, sha256 `0234b4f9bcdb92b0f83adc26116de3797db9d0ed321a31e80c4a4e41bfa34ab7` (Appendix A). It opens the declared baseline, reads `baseline_commit` from the raw JSON (bypassing O01's parser for the F-O14-1 reason), validates each `before_checks` entry through O02's `validate_claim_checks`, evaluates each probe against the baseline, judges each claim with O03, aggregates, and exits with the report's own code. Its `--adapt-seams` switch is a **scratch-only vocabulary bridge** (F-O14-2/F-O14-3); it never alters a measured value.

## 2. Inputs

### 2.1 The r43 fixture was re-expressed into the durable schema

The r43 claims file has no in-file `before_checks` (`reports/round-43/claims.json:27,40,53`), so a demonstration must supply them. K03's normative overlay uses one schema; O01/O02's parser uses another:

| field | K03 §7.1 / O05 overlay | O01/O02 durable schema |
|---|---|---|
| container | top-level `checks` map + `claims_sha256` (`reports/round-47/scout/K03-gate-spec.md:442-481`; `reports/round-47/op/O05-r43-demo.md:97`) | per-claim `before_checks` list (`O01-tool-core.md:562-580`) |
| `capability_present` target | `{"capability": "couples_census", "scope": "tools/**.py"}` (`K03:452-453`; `O05:112,119`) | behavioral `globs/exclude_globs/argv/fixture/success_regex/timeout_s/max_candidates` (`O02-probe-registry.md:445-543`) |
| `count_eq` | `target.value` integer + boolean `expect` (`K03:463-464`) | integer `expect`, target `{"glob"}` (`O02-probe-registry.md:460-463`) |
| `topic_owner_absent` | `{"topics", "partition"}` + header field `"H1"` (`K03:467-469`) | `{"topic", "partitions", "mode"}` + field `h1` (`O02-probe-registry.md:468-500,337-339`) |

The K03/O05 overlay therefore cannot be fed to the current parser: O01 accepts only `before_checks` or `legacy freshness_probes` (`O01-tool-core.md:562-580`), and O02 rejects the K03 target keys. To measure determinism of the actual drafted probe code rather than of a rejected input, this seat rebuilt the same r43 premises in the O02 schema:

- `before` strings are **byte-identical** to `reports/round-43/claims.json` (verified: `O True, C True, Ca True`), so no premise was paraphrased to fit a probe.
- Every clause is a verbatim substring of its `before` (verified: `[True,True,True]`, `[True,True,True]`, `[True]`).
- The measured facts reproduce K03 §7.1 exactly: myth-symbol 26, total 223, lithic owned by `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`, resolver absent at `7ceff59`, extractor present and passing `entries=1 refs=4`.

The fixture is `.scratch/o14/r43-durable.json`, 46,450 bytes, sha256 `23454a391b57d3462f0050961ffb72f00a759f038331ca73624b1b3230487b9d`; its builder is Appendix B.

### 2.2 Other fixtures

| fixture | purpose | expected | measured |
|---|---|---|---|
| `fresh.json` | a premise true at its baseline (absent sentinel path) | FRESH, 0 | FRESH, 0 |
| `no-checks.json` | `before_checks: []` | could-not-evaluate, non-zero | could-not-evaluate, 3 |
| `malformed.json` | non-JSON input | malformed, 2 | malformed, 2 |

## 3. Measurements

### 3.1 Determinism matrix — 11 runs, one result

Each row is a full process run over the same claims bytes, baseline tree, and tool bytes. `stdout sha` is the sha256 of the canonical JSON report; `digest` is the report's own `decision_sha256`.

| run | perturbation | exit | stdout sha256 | `decision_sha256` |
|---|---|---|---|---|
| base | `PYTHONHASHSEED=0` | 1 | `18f685e9…299e7` | `819360383b6461904e20eb5027379e575f133850726c7e97256bd2e057ea051c` |
| repeat1 | identical rerun | 1 | `18f685e9…299e7` | identical |
| hashseed1 | `PYTHONHASHSEED=1` | 1 | `18f685e9…299e7` | identical |
| hashseed42 | `PYTHONHASHSEED=42` | 1 | `18f685e9…299e7` | identical |
| hashseed_rand | `PYTHONHASHSEED=random` | 1 | `18f685e9…299e7` | identical |
| tz_tokyo | `TZ=Asia/Tokyo` | 1 | `18f685e9…299e7` | identical |
| tz_ny | `TZ=America/New_York` | 1 | `18f685e9…299e7` | identical |
| lc_c | `LC_ALL=C` | 1 | `18f685e9…299e7` | identical |
| lc_cutf8 | `LC_ALL=C.UTF-8` | 1 | `18f685e9…299e7` | identical |
| sde_1 | `SOURCE_DATE_EPOCH=1` | 1 | `18f685e9…299e7` | identical |
| sde_2 | `SOURCE_DATE_EPOCH=2000000000` | 1 | `18f685e9…299e7` | identical |

Unique stdout shas: **1**. Unique exit codes: **1**. Unique digests: **1**.

### 3.2 Orthogonal perturbations — still one result

| perturbation | comparison | result |
|---|---|---|
| 3-second time separation (two runs) | `cmp` | IDENTICAL |
| `TMPDIR` changed between runs (`tmpA` vs `tmpB`), which changes every `tempfile.mkdtemp` used by the capability probe | `cmp` | IDENTICAL |
| cwd = repo root vs cwd = `.scratch` (absolute tool/claims/root paths) | `cmp` | IDENTICAL |
| 4 concurrent runs (`&` + `wait`) | stdout shas | **1** unique |
| hostile `HOME` with a user `.gitconfig` (`core.abbrev`, `log.showSignature`) | `cmp` | IDENTICAL |
| claims file copied to a different path | `cmp` | IDENTICAL |
| same process, same `Baseline` (warm blob cache), two `one_pass()` evaluations | byte comparison | equal; both `decision_sha256 = 81936038…051c`, both exit 1 |

The `TMPDIR` row is the one that matters for the capability probe: the probe creates a randomized temporary directory per candidate (`O02-probe-registry.md:845-847`), but neither the directory name nor its path reaches the report.

### 3.3 Verdict-class determinism

Each fixture was run twice; stdout was compared byte-for-byte.

| fixture | run 1 | run 2 | `decision_sha256` |
|---|---|---|---|
| fresh | exit 0 | exit 0 | `1adc4706a2c61fd1e8b21a17c76c8a786969c392bd7b15740f9e0f5be7756c5a` |
| stale (r43) | exit 1 | exit 1 | `819360383b6461904e20eb5027379e575f133850726c7e97256bd2e057ea051c` |
| no-checks | exit 3 | exit 3 | `aff388bc0f005520ca4b291479c16eb1c04f8c77f9d61c7813273fff3ab85958` |
| malformed (non-JSON) | exit 2 | exit 2 | `339becccffaf16e81524a8da1d9b7a0e5845456a7aae8d659a529f7755db7912` |

The four digests are distinct, so `decision_sha256` is not a constant: determinism is not purchased by discarding the decision.

### 3.4 The r43 regression under the seam adapter

With the vocabulary bridge only (no measurement changed), the assembled probe path produces exactly the claim's required result:

| claim | verdict | clauses |
|---|---|---|
| **O** | **stale** | 2 contradicted (both capability checks: the baseline extractor satisfies `entries=1 refs=4`), 1 holds (resolver path absent) |
| **C** | **stale** | 2 hold (myth-symbol 26, total 223), 1 contradicted (topic `lithic` has 1 owner: `mineral-stone-symbolism.md`) |
| **Ca** | **fresh** | 1 holds (no disposition artifact at `7ceff59`) |

`summary {claims:3, clauses:7, fresh:1, stale:2, could_not_evaluate:0, malformed:0}`; run verdict `stale`; exit **1**; `decision_sha256 = 81936038…051c`; resolved baseline `7ceff59a0216a8ea21ee43262d9fc72abf770cee`. This is the same shape O05 and O12 predicted, measured through O02's probes and O03's verdict layer.

### 3.5 The layers' own selftests are deterministic

```
$ for i in 1 2 3; do PYTHONHASHSEED=$((i*17)) python3 -B .scratch/o14/part2.py --selftest; done
PROBE-REGISTRY SELFTEST: 43/43      (all three runs, exit 0)
sha256 of the three outputs: 6b1c50952abaebca0218ef648a08d0201b08a58c7b3d7502781be7a41897e70d (identical)

$ for i in 1 2; do PYTHONHASHSEED=$((i*23)) python3 -B .scratch/o03/drive_o03.py; done
selftest 33/33 PASS                 (both runs, exit 0, output identical)
```

## 4. Static determinism audit

| hazard | source | measurement |
|---|---|---|
| wall clock | no `time`, `datetime`, `monotonic`, `perf_counter` anywhere in the assembled module | `grep -nE '\b(time\|datetime\|random\|uuid\|secrets\|urandom\|perf_counter\|monotonic)\b'` → no hits |
| RNG / UUIDs | no `random`, `uuid`, `secrets`, `os.urandom` | same grep → no hits |
| hash randomization | no builtin `hash()`; set/dict output goes through `json_safe`, which sorts sets and dict keys (`O03-verdict-contract.md:152-170`) | `grep -nE '\bhash\('` → no hits |
| set iteration order | capability candidates are `sorted(...)` (`O02-probe-registry.md:816-818`); registry membership is a frozen set used only for lookup; error text uses `sorted(PROBE_KINDS)` (`O01-tool-core.md:460-462`) | 4 `PYTHONHASHSEED` values → identical stdout |
| ambient git config | `_git_env` drops every `GIT_*` variable and pins `GIT_NO_REPLACE_OBJECTS=1`, `GIT_OPTIONAL_LOCKS=0`, `LC_ALL=C` (`O01-tool-core.md:278-281`) | hostile user `.gitconfig` → identical stdout |
| replace refs / locale | same pin; baseline blob bytes come from `git cat-file --batch` (`O01-tool-core.md:663-690`) | `TZ`/`LC_ALL` matrix → identical |
| temp paths | capability probe's randomized work dir is not in the report (part 3 reads `check["evidence"]`, and validated checks carry only `evidence_command`) | `TMPDIR` A/B → identical; output scan finds no `/tmp`, `claims-freshness-cap`, or absolute path |
| timestamps in output | the report has no timestamp field; top-level keys are `baseline_commit, baseline_sha, claims, decision_sha256, errors, exit_code, refusal, refuse, round, run_verdict, schema, summary` | scan for ISO dates / epoch digits → no hits |

## 5. Findings

These are integration findings surfaced by the determinism work. None is a nondeterminism source; all block the claim's end-to-end acceptance if left.

### F-O14-1 — `expect` is boolean-only in the parser; two probe kinds cannot be declared (blocking)

`O01-tool-core.md:473-474` rejects any non-`bool` `expect`:

```
if not isinstance(expect, bool):
    raise GateInputError(... "expect is not boolean")
```

But the registry types `expect` per kind: `int` for `count_eq`, 64-hex `str` for `sha256_eq` (`O02-probe-registry.md:555-570`). Reproduction with a schema-conformant r43 fixture (direct parser call, since the driver bypasses this parser for the reason below):

```
$ python3 -B -c "import sys; sys.path.insert(0,'.scratch/o14'); import gate_draft as g; g.load_claims('.scratch/o14/r43-durable.json')" 2>&1 | tail -1
gate_draft.GateInputError: .scratch/o14/r43-durable.json: claims[1]: before_checks[0] expect is not boolean
```

The driver used for the determinism matrix reads `baseline_commit` from the raw JSON and validates each `before_checks` entry through O02's `validate_claim_checks`, because `load_claims` cannot parse a `count_eq` clause at all. That bypass is the workaround for this finding, not a second schema.

Consequence: a claims file using `count_eq` or `sha256_eq` is rejected as malformed before any probe runs. Fix belongs at the O01/O02 seam: delegate type validation to `PROBE_VALUE_TYPES` rather than requiring `bool`.

### F-O14-2 — probe status vocabulary does not meet the verdict vocabulary; the gate can never say STALE (blocking)

O02's `_result` emits `"holds"` / `"mismatch"` (`O02-probe-registry.md:679-693`). O03 accepts only `HOLDS` / `CONTRADICTED` / `NOT_EVALUATED` and turns anything else into `NOT_EVALUATED` (`O03-verdict-contract.md:138,172-190`). On the assembled module, every genuine mismatch becomes an evaluator-contract violation:

```
[O] could-not-evaluate   clauses: NOT_EVALUATED, NOT_EVALUATED, HOLDS
    reason: evaluator-contract-violation: status 'MISMATCH' is not one of HOLDS/CONTRADICTED/NOT_EVALUATED
[C] could-not-evaluate   clauses: HOLDS, HOLDS, NOT_EVALUATED
[Ca] fresh
exit=3
```

This is the failure the r47 O claim exists to prevent, inverted: the assembled gate exits 3 (could-not-evaluate) on r43 where the contract requires exit 1 with O and C stale. Fix: one of the two layers owns the mapping (`mismatch → CONTRADICTED`, `could-not-evaluate → NOT_EVALUATED`), or both share one status enum.

### F-O14-3 — result key `expect` vs report key `expected` (non-blocking, report quality)

O02 returns `"expect"`, O03 reads `"expected"` (`O03-verdict-contract.md:172-190,202-225`). Consequence under the adapter: the verdict is right, but every clause row renders `"expected": null` until the key is unified. Determinism is unaffected.

### F-O14-4 — the filed demonstration schema is not the schema the parser accepts (blocking for the demo, not for the tool)

K03 §7.1 and O05's overlay use top-level `checks`, `claims_sha256`, string-named capabilities (`{"capability": "couples_census", "scope": ...}`), `target.value`, `target.topics`, `target.partition`, and header field `"H1"` (`K03-gate-spec.md:442-481`; `O05-r43-demo.md:97,112,119`). O01 accepts only in-claim `before_checks` or `freshness_probes` (`O01-tool-core.md:562-580`); O02 requires the behavioral capability target (`O02-probe-registry.md:445-543`) and the lowercase `h1` regex (`O02-probe-registry.md:337-339`). An integrator who files O05's overlay verbatim will get `malformed` (exit 2), not the r43 regression. Either add the overlay path the demo names, or re-express the demo in the durable schema as done here (Appendix B).

### F-O14-5 — `decision_sha256` includes any observation field, so adding `observed_at` breaks digest stability (must decide before landing)

K03 §3.11 requires a digest that "excludes `observed_at`, evidence strings, and the tool digest", and allows `--json` output to differ only in `observed_at` (`K03-gate-spec.md:243`). P03 likewise says `generated_at` is the only non-deterministic field (`reports/round-47/plan/P03-o-plan.md:310`). O03's digest hashes **every** report field except itself:

```
body = {key: value for key, value in report.items() if key != "decision_sha256"}
```

Measured: injecting an observation field into the report changes the digest while leaving verdict and exit untouched:

```
observed_at  digest_changes=True  new=ebe9c561536f4340
generated_at digest_changes=True  new=52a2a577c64fc28d
base digest 819360383b646190  verdict stale  exit 1
```

As drafted (no observation field), stdout is byte-identical across runs — the stronger result. If the landing adds `observed_at`/`generated_at` per K03/P03, the digest must exclude those fields or be replaced by K03's claim-level `verdict_digest`; otherwise O14's assertion "identical digest" fails on correct runs.

## 6. Claim-O threshold disposition

| O threshold (`reports/round-47/claims.json:41,47`) | status |
|---|---|
| durable tool, not `.scratch` | **FAIL at cut** — path absent; only scratch/dev artifacts exist |
| green selftest | **partial** — part 2 `43/43`, part 3 `33/33`, both deterministic; no assembled-tool selftest exists |
| flags r43 O and C stale, Ca fresh | **FAIL as filed** (exit 3, F-O14-2); **PASS** under the vocabulary adapter (exit 1, §3.4) |
| does not flag a fresh claim | **PASS** at the decision layer (fresh fixture exit 0); durable-path proof still absent |
| anti-theater mutation still flags | not this seat (O07/O08); unverified here — `to-verify` |
| `could-not-evaluate != green` | **PASS** — no-checks fixture exits 3, deterministically |
| identical verdict + exit on identical inputs | **PASS** at the drafted decision layer (§3.1-§3.3); **could-not-evaluate** for the durable path |

Determinism is satisfied; operability is not yet delivered. The distinction matters for the round: no live behavior depends on the absent tool, so no axis is harmed, but the O claim cannot be marked improved on this evidence.

## 7. Reproduction

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1

# 1. run the assembly recipe in §1.2 (writes .scratch/o14/gate_draft.py)
# 2. write Appendix A to .scratch/o14/run_gate.py and Appendix B to .scratch/o14/build_fixtures.py
python3 -B .scratch/o14/build_fixtures.py

# two runs, same input
python3 -B .scratch/o14/run_gate.py .scratch/o14/r43-durable.json "$PWD" --adapt-seams > .scratch/o14/r1.json; echo $?
python3 -B .scratch/o14/run_gate.py .scratch/o14/r43-durable.json "$PWD" --adapt-seams > .scratch/o14/r2.json; echo $?
cmp .scratch/o14/r1.json .scratch/o14/r2.json && sha256sum .scratch/o14/r1.json
python3 -c 'import json;print(json.load(open(".scratch/o14/r1.json"))["decision_sha256"])'

# unadapted draft: deterministic but never stale (F-O14-2)
python3 -B .scratch/o14/run_gate.py .scratch/o14/r43-durable.json "$PWD"; echo $?

# verdict classes
for f in fresh no-checks malformed; do python3 -B .scratch/o14/run_gate.py .scratch/o14/$f.json "$PWD" --adapt-seams; echo "$f exit=$?"; done
```

## 8. Ledger

Writes:

- `reports/round-47/op/O14-determinism.md` — this file (durable deliverable).
- `.scratch/o14/` — `part1.py`, `part2.py`, `part3.py`, `gate_draft.py`, `run_gate.py`, `build_fixtures.py`, fixtures, matrix outputs (scratch only; the scripts are reproduced in the appendices so the evidence survives scratch cleanup).

Reads: `reports/round-43/claims.json`; `reports/round-47/{targets.json,claims.json}`; `reports/round-47/op/{O01,O02,O03,O05,O06,O09,O10,O12,O13}.md`; `reports/round-47/scout/K03-gate-spec.md`; `reports/round-47/plan/P03-o-plan.md`; `reports/round-44/review/R01-review.md`; `.scratch/o03/drive_o03.py`; `.scratch/o05/r43-checks.json`.

Provenance at cut:

```
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-47/
```

No tracked file changed; `git status` shows only the pre-existing untracked round trees. No filed byte was edited; nothing was staged under `corpus/`; no round runner was executed; `declared-in-r7` was not touched.

## Appendix A — driver (`.scratch/o14/run_gate.py`)

```python
#!/usr/bin/env python3
"""O14 driver: run the assembled r47 draft end-to-end on one claims file.

The durable CLI does not exist at this cut; this is the seat-local driver over
the three fenced draft parts (O01+O02+O03).  It prints the part-3 report as
canonical JSON and exits with the report's own exit_code.
"""
import json
import pathlib
import sys

HERE = pathlib.Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import gate_draft as g  # noqa: E402

claims_path = pathlib.Path(sys.argv[1])
root = pathlib.Path(sys.argv[2]).resolve() if len(sys.argv) > 2 else pathlib.Path.cwd().resolve()
ADAPT = "--adapt-seams" in sys.argv[3:]


def adapt(result):
    """Scratch only: bridge O02's result vocabulary to O03's verdict vocabulary.

    O02 emits status holds|mismatch|could-not-evaluate and key `expect`; O03
    accepts HOLDS|CONTRADICTED|NOT_EVALUATED and reads `expected`.  This shim
    exists so determinism of the real probe->verdict path can be measured
    without editing the drafted bytes.  It never changes a measurement.
    """
    if not ADAPT:
        return result
    out = dict(result)
    status = str(out.get("status", "")).strip().lower()
    out["status"] = {
        "holds": "HOLDS",
        "mismatch": "CONTRADICTED",
        "could-not-evaluate": "NOT_EVALUATED",
    }.get(status, out.get("status"))
    if "expected" not in out and "expect" in out:
        out["expected"] = out["expect"]
    if "reason" not in out:
        out["reason"] = out.get("detail", "")
    return out

raw = {}
try:
    raw = json.loads(claims_path.read_text())
    baseline_input = raw.get("baseline_commit")
    if not isinstance(baseline_input, str) or not baseline_input.strip():
        raise ValueError("claims file has no non-empty baseline_commit")
    baseline = g.open_baseline(root, baseline_input)
except Exception as exc:
    report = g.malformed_report(str(exc), round_id=raw.get("round") if isinstance(raw, dict) else None,
                                baseline_commit=raw.get("baseline_commit") if isinstance(raw, dict) else None)
    sys.stderr.write("malformed: %s\n" % exc)
    sys.stdout.write(json.dumps(report, indent=2, sort_keys=True) + "\n")
    sys.exit(report["exit_code"])

rows = []
for claim in raw.get("claims", []):
    cid = claim.get("id")
    axis = claim.get("axis")
    before = claim.get("before", "")
    try:
        checks = g.validate_claim_checks(claim)
    except g.CheckError as exc:
        rows.append(g.judge_claim(cid, [], axis=axis, before=before,
                                  schema_errors=[str(exc)]))
        continue
    results = []
    for check in checks:
        try:
            results.append(adapt(g.evaluate_check(check, baseline, allow_exec=True)))
        except Exception as exc:  # probe contract: never green on error
            results.append({"status": "NOT_EVALUATED", "measured": None,
                            "expected": check.get("expect"), "reason": str(exc)})
    rows.append(g.judge_claim(cid, checks, results=results, axis=axis, before=before))

report = g.build_report(
    rows,
    round_id=raw.get("round"),
    baseline_commit=raw.get("baseline_commit"),
    baseline_sha=baseline.commit,
)
sys.stdout.write(json.dumps(report, indent=2, sort_keys=True) + "\n")
sys.exit(report["exit_code"])
```

## Appendix B — r43 fixture builder (`.scratch/o14/build_fixtures.py`)

```python
#!/usr/bin/env python3
"""Build the O14 fixtures: r43 (durable schema), fresh, no-checks, malformed."""
import json
import pathlib
import subprocess

here = pathlib.Path(__file__).resolve().parent
repo = here.parent.parent

r43 = json.loads((repo / "reports/round-43/claims.json").read_text())
texts = {c["id"]: c for c in r43["claims"]}

field = subprocess.run(
    ["git", "show", "7ceff59:corpus/knowledge/linguistics/phonetics-phonology.md"],
    cwd=repo, capture_output=True, text=True, check=True,
).stdout

cap_target = {
    "globs": ["tools/harness/*.py"],
    "exclude_globs": [],
    "argv": ["--census"],
    "fixture": {"corpus/knowledge/linguistics/phonetics-phonology.md": field},
    "success_regex": "entries=1 refs=4",
    "timeout_s": 30,
    "max_candidates": 32,
}

doc = {
    "round": 43,
    "baseline_commit": "7ceff59",
    "claims": [
        {
            "id": "O",
            "axis": "operability",
            "before": texts["O"]["before"],
            "before_checks": [
                {
                    "clause": "no durable instrument implements the r39 basename-couples policy",
                    "probe_kind": "capability_present",
                    "target": cap_target,
                    "expect": False,
                    "evidence_command": "git ls-tree -r --name-only 7ceff59 -- tools/harness",
                },
                {
                    "clause": "the single wrapped couples field reads 0/4 tokens",
                    "probe_kind": "capability_present",
                    "target": cap_target,
                    "expect": False,
                    "evidence_command": "git show 7ceff59:corpus/knowledge/linguistics/phonetics-phonology.md | sed -n '72,77p'",
                },
                {
                    "clause": "no durable instrument implements the r39 basename-couples policy",
                    "probe_kind": "path_absent",
                    "target": {"path": "tools/harness/basename-couples-resolver.py"},
                    "expect": True,
                    "evidence_command": "git cat-file -e 7ceff59:tools/harness/basename-couples-resolver.py || echo ABSENT",
                },
            ],
        },
        {
            "id": "C",
            "axis": "coverage",
            "before": texts["C"]["before"],
            "before_checks": [
                {
                    "clause": "myth-symbol 26",
                    "probe_kind": "count_eq",
                    "target": {"glob": "corpus/knowledge/myth-symbol/*.md"},
                    "expect": 26,
                    "evidence_command": "git ls-tree -r --name-only 7ceff59 -- corpus/knowledge/myth-symbol | wc -l",
                },
                {
                    "clause": "total 223",
                    "probe_kind": "count_eq",
                    "target": {"glob": "corpus/knowledge/*/*.md"},
                    "expect": 223,
                    "evidence_command": "git ls-tree -r --name-only 7ceff59 -- corpus/knowledge | wc -l",
                },
                {
                    "clause": "lithic slot named but unbuilt",
                    "probe_kind": "topic_owner_absent",
                    "target": {"topic": ["lithic"], "partitions": ["myth-symbol"],
                               "fields": ["h1", "topic", "gap filled"], "mode": "word"},
                    "expect": True,
                    "evidence_command": "git grep -n -i lithic 7ceff59 -- 'corpus/knowledge/myth-symbol/*.md'",
                },
            ],
        },
        {
            "id": "Ca",
            "axis": "calibration",
            "before": texts["Ca"]["before"],
            "before_checks": [
                {
                    "clause": "have no per-finding disposition on record",
                    "probe_kind": "path_absent",
                    "target": {"path": "reports/round-43/calib/dispositions-r38-r39.json"},
                    "expect": True,
                    "evidence_command": "git ls-tree -r --name-only 7ceff59 -- reports/round-43/calib/",
                },
            ],
        },
    ],
}
(here / "r43-durable.json").write_text(json.dumps(doc, indent=1) + "\n")

fresh = {
    "round": 47,
    "baseline_commit": "6e9a30d",
    "claims": [{
        "id": "neg", "axis": "operability",
        "before": "a sentinel path that does not exist at the baseline",
        "before_checks": [{
            "clause": "a sentinel path that does not exist at the baseline",
            "probe_kind": "path_absent",
            "target": {"path": "corpus/knowledge/__o14_no_such_entry__.md"},
            "expect": True,
            "evidence_command": "git cat-file -e 6e9a30d:corpus/knowledge/__o14_no_such_entry__.md || echo ABSENT",
        }],
    }],
}
(here / "fresh.json").write_text(json.dumps(fresh, indent=1) + "\n")

cne = {
    "round": 47,
    "baseline_commit": "6e9a30d",
    "claims": [{
        "id": "cne", "axis": "operability",
        "before": "a premise with no declared checks",
        "before_checks": [],
    }],
}
(here / "no-checks.json").write_text(json.dumps(cne, indent=1) + "\n")
(here / "malformed.json").write_text("{not json\n")
print("wrote", [p.name for p in sorted(here.glob('*.json'))])
```
