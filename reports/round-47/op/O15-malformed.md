# O15 — malformed-input verifier: no `baseline_commit`, a claim without `before`, non-JSON

- Seat: `O15` | role `verifier` | claim **O** (operability) | round 47, loop 2 (refire)
- Out path: `reports/round-47/op/O15-malformed.md` — the only file this seat writes
- Mission: `reports/round-47/targets.json:74` — "feed the gate a claims.json with no baseline_commit, a claims[] missing `before`, and non-JSON — each yields exit 2 malformed, not a crash or a green"
- Baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`), declared `6e9a30d` (`reports/round-47/claims.json:7`)
- Observation cut: **2026-10-19T19:17Z**; Python 3.14.7; git 2.55.0
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root
- Boundary: no filed byte edited; no corpus write or staging; no round runner executed in-tree; no git commit/push/install/network. Fixtures and the assembled candidate live only under `.scratch/o15/` (gitignored: `.gitignore:6`) plus the fenced copies in this file.

---

## 1. Verdict

**The three named malformed inputs pass on the assembled draft: each exits exactly 2, with `run_verdict: "malformed"`, `refuse: true`, no traceback, and no green.** The pass is a property of the parse layer (O01) and the malformed-report layer (O03); the cases never reach the probe seam, so this result does **not** certify the probe layer or the durable tool.

| leg | measured | status |
|---|---|---|
| no `baseline_commit` | exit 2, `malformed`, `document_errors: 1`, no traceback | **PASS** |
| claim without `before` | exit 2, `malformed`, `document_errors: 1`, no traceback | **PASS** |
| non-JSON | exit 2, `malformed`, `document_errors: 1`, no traceback | **PASS** |
| controls are not forced to 2 | legal no-checks claim → exit **3**; true check → exit **0** | **PASS** |
| focused battery (named + `--at`, renamed key, worktree, missing file, empty/blank fields, null doc, empty claims) | **13/13** | **PASS** |
| broad battery (17 cases) | **16/17** — the failure is a non-UTF-8 file that crashes part 1 | see §7 |
| same battery with a one-line UTF-8 catch | **17/17** | patch verified |

**Deliverable status: `could-not-evaluate`, not improved.** `tools/harness/claims-freshness.py` is absent at this cut (`ls` → no such file), so the malformed leg is verified against an **assembled draft**, digest-pinned below, not against the durable path. The round's own threshold is "could-not-evaluate != green" (`reports/round-47/claims.json:47`); the durable link must be re-run by V02 after W01 lands the tool. This is the same disposition R01 and R04 reached for O overall (`reports/round-47/review/R01-review.md:236`; `review/R04-gate.md:25`).

**Three integration blockers were reproduced independently** (already filed by R01/R04/X03 — I confirm them with my own runs): the fenced parts do not concatenate (duplicate `from __future__` imports), part 2's `__main__` guard exits before any CLI, and the part-2 → part-3 status vocabulary does not match. **One new defect is filed here:** a non-UTF-8 claims file raises `UnicodeDecodeError` out of part 1 as a traceback/exit 1 instead of exit 2 (§7, O15-D1).

---

## 2. Contract under test

The exit contract is closed and stated in three places consistently:

| condition | required exit | source |
|---|---|---|
| every claim fresh | 0 | `reports/round-47/scout/K03-gate-spec.md:190-205` |
| any claim stale | 1 | same |
| **malformed input** (bad JSON, missing `baseline_commit`, claim missing `id`/`before`, wrong types, unknown probe kind, missing `expect`) | **2** | same; `reports/round-47/plan/P01-plan.md:344`; `op/O03-verdict-contract.md:739` |
| no stale, any could-not-evaluate | 3 | same |
| usage error (no `--claims`) | 2 | K03 §3.9 ("malformed input or usage error") |

Input rules specific to this seat (`reports/round-47/scout/K03-gate-spec.md:99-102`):
`baseline_commit` must be a non-empty string **even when `--at` is supplied**; a claim must carry a non-empty `before`; a missing/duplicate `id` is malformed. Exit 2 is decided **before** any verdict: "malformed is decided first (parse/validate, no verdicts)" (`K03:197`).

---

## 3. Verification target and assembly

The durable path is absent:

```
$ ls tools/harness/claims-freshness.py
ls: cannot access 'tools/harness/claims-freshness.py': No such file or directory
```

I extracted the three fenced bodies from the filed fragments and verified their digests against the fragments' own claims:

| part | source fence | bytes | sha256 | matches filed statement |
|---|---|---|---|---|
| p1 | `reports/round-47/op/O01-tool-core.md:160` | 24,754 | `72c294f2c49dc53f3f7e7e65b0dc646e238a56b19473f84b63f1cb5bbf13b876` | `O01:14` |
| p2 | `reports/round-47/op/O02-probe-registry.md:254` | 38,874 | `a60b0a22df2d73c1a4075662d76a1d5c25a5caa8f6f35b72ffdf0c2ed772c191` | `O02:1224` |
| p3 | `reports/round-47/op/O03-verdict-contract.md:86` | 16,491 | `097a31987cc334d93eaa117e60d7112cddeb7fbf9a356d10ca4dc178721cfcef` | `O03:84` |

**Plain concatenation does not run.** Three assembly-only repairs were required; none edits the semantic body of a part:

1. **Strip the repeated `from __future__ import annotations`** from p2 (`O02:315`) and p3 (`O03:108`). Kept at the head (p1), the duplicates land mid-file and are a `SyntaxError` at assembled line 695. O01's sentence "The assembly is plain concatenation; nothing in part 2/3 needs to edit these bytes" (`O01:23`) is false; R01 and R04 measured the same (`R01-review.md:204-209`; `R04-gate.md:190`).
2. **Strip p2's trailing module guard** `if __name__ == "__main__": sys.exit(selftest_registry())` (`O02:1220-1221`). Left in place it executes the registry selftest at import of the second part and exits 0 before the CLI — the "false green" X03 measured (`cross/X03-gate-theater.md:158-196`).
3. **Add the status adapter** at the p2 → p3 seam: p2 emits `holds | mismatch | could-not-evaluate` (`O02:679-689`), p3 accepts only `HOLDS | CONTRADICTED | NOT_EVALUATED` (`O03:138,172-175`). Without the map, `mismatch` uppercases to `MISMATCH`, is not in `_CLAUSE_STATUS`, and is downgraded to `NOT_EVALUATED` — a contradiction becomes exit 3, never stale. R04 filed this as D3 (`R04-gate.md:192`); my run reproduces it (`p3.normalise_clause_result({'status':'mismatch'}) → NOT_EVALUATED`).

Assembly result (tested glue in the Appendix; the adapter is confined to `_adapt_result`):

| artifact | bytes | sha256 |
|---|---|---|
| `.scratch/o15/claims-freshness-o15.py` (p1+p2+p3+seam) | 84,037 | `5d8983c436827e3af9e3032d8068f0e2065a5b2230a1cf0f75c369433800bca5` |
| `.scratch/o15/claims-freshness-o15-patched.py` (+ UTF-8 catch) | 84,059 | `4c8b07fb557b32fb49671040869d3a3414a689b05a1b1f74cee78f155362d779` |
| `.scratch/o15/assemble.py` | 8,131 | `5f55d820fba87386b6ec9f86ded1d5ad19796c6de3b09552d797bb050ccb226c` |
| `.scratch/o15/run-malformed.py` | 4,828 | `586a691fbd56e2fbc4760c2775975e65b76eca2b98001c63cdaf154a7b4b50f3` |
| `.scratch/o15/verify-named.py` | 6,456 | `b5e0bd09aca18ebe6d72294b919561f0f6e9025d95f4c911d1e7d0ce86c9211c` |
| `.scratch/o15/results/matrix.json` | — | `8fb981f3c2124b25a66cb75b62996c1c3671c9b6902977417a3b1d6a5c9f8b46` |
| `.scratch/o15/results-patched/matrix.json` | — | `b02dd7d4ff5b3755922714f088377f6b183fedd66b2d93feab8ea70da5c505df` |
| `.scratch/o15/results-focus/focus.json` | — | `38595e14b50e381e048ebfa42c07e92e87352310da8103f4ac6d5192711a94db` |

Part 2's own control set is green in the assembled file when invoked directly: `PROBE-REGISTRY SELFTEST: 43/43`. That is a probe-layer signal only; it is not the malformed acceptance.

---

## 4. The three named cases, measured

Fixtures (exact bytes in Appendix B):

| fixture | sha256 | defect |
|---|---|---|
| `.scratch/o15/fixtures/m1-no-baseline.json` | `976751efb47158ee57a182dc6c13c58efaa42ee7107198fec3edaac0457c0aa8` | no `baseline_commit` key |
| `.scratch/o15/fixtures/m2-missing-before.json` | `e406606af04de7fb0761c5530c52e3177c3a83e4eed6db6e9c5538a9910d2141` | `claims[0]` has no `before` |
| `.scratch/o15/fixtures/m3-not-json.json` | `c00050fa6a244e6a7d7dcbdf163ae88aff0aec493421ebcb98724cd366ffcaa1` | truncated JSON |

### 4.1 Exit and report fields

`python3 -B .scratch/o15/claims-freshness-o15.py --claims <fixture> --json`:

| case | exit | `run_verdict` | `exit_code` field | `refuse` | claim rows | `summary.document_errors` | traceback | `decision_sha256` |
|---|---|---|---|---|---|---|---|---|
| M1 no baseline | **2** | `malformed` | 2 | true | `[]` | 1 | none | `36d05606f806d17c441a92d70ae3646cb69c09cab1855125a9136f9c9ba3d6f7` |
| M2 missing `before` | **2** | `malformed` | 2 | true | `[]` | 1 | none | `c5c8fe4e4e7559265a21ffc5595b9d6bf58c5c4c80626393581e928c491c79c3` |
| M3 non-JSON | **2** | `malformed` | 2 | true | `[]` | 1 | none | `03daf95c877a1b52054d318771822b6706d5d77f32bb6c2b1ee8000480d24e7a` |

No case returns 0, 1 or 3; no case prints `Traceback`; all three `--json` reports parse as JSON. The `decision_sha256` is identical on a second run (determinism check in §6.2).

### 4.2 Verbatim human renders

M1 (no baseline):

```
claims-freshness: round None baseline unresolved (unresolved)
summary: 0 fresh, 0 stale, 0 could-not-evaluate, 0 malformed; clauses 0 (0 hold, 0 contradict, 0 not evaluated); 1 document error(s)
error: .scratch/o15/fixtures/m1-no-baseline.json: no baseline_commit; a claim premise cannot be evaluated without the commit it describes (worktree evaluation is forbidden)
REFUSE: input is malformed at unresolved baseline: .scratch/o15/fixtures/m1-no-baseline.json: no baseline_commit; a claim premise cannot be evaluated without the commit it describes (worktree evaluation is forbidden); exit 2 -- no freshness verdict is possible.
exit 2
```

M2 (missing `before`):

```
claims-freshness: round None baseline unresolved (unresolved)
summary: 0 fresh, 0 stale, 0 could-not-evaluate, 0 malformed; clauses 0 (0 hold, 0 contradict, 0 not evaluated); 1 document error(s)
error: .scratch/o15/fixtures/m2-missing-before.json: claims[0]: claim O has no non-empty `before`
REFUSE: input is malformed at unresolved baseline: .scratch/o15/fixtures/m2-missing-before.json: claims[0]: claim O has no non-empty `before`; exit 2 -- no freshness verdict is possible.
exit 2
```

M3 (non-JSON):

```
claims-freshness: round None baseline unresolved (unresolved)
summary: 0 fresh, 0 stale, 0 could-not-evaluate, 0 malformed; clauses 0 (0 hold, 0 contradict, 0 not evaluated); 1 document error(s)
error: .scratch/o15/fixtures/m3-not-json.json: invalid JSON at line 2 column 1: Expecting value
REFUSE: input is malformed at unresolved baseline: .scratch/o15/fixtures/m3-not-json.json: invalid JSON at line 2 column 1: Expecting value; exit 2 -- no freshness verdict is possible.
exit 2
```

The error strings come from `load_claims`: missing baseline at `O01:531`, missing `before` at `O01:557`, JSON decode at `O01:508-520`. The `exit 2` line and `REFUSE` sentence are p3's `render_human`/`_refusal`.

### 4.3 What "green leak" means here

A malformed input is a green leak if the process exits 0, or if the report says `run_verdict: fresh`, or if any claim row says `fresh`. All three were asserted false (`run-malformed.py` case fields `green_leak`, and `focus.json` claim-verdict lists). The reports carry zero claim rows by construction: a malformed document has no verdicts.

---

## 5. Controls: exit 2 is not hardcoded

| control | input | exit | expected | source |
|---|---|---|---|---|
| C1 legal, no checks | `v1-valid-no-checks.json` | **3** | 3 (could-not-evaluate is non-zero, never green) | `claims.json:47` |
| C2 legal, true check | `v2-valid-true.json` (`path_present corpus/README.md` at `6e9a30d`) | **0** | 0 | K03 §3.9 |
| C3 legal, one true check, `--json` | `valid-open.json` | **0** | 0 | K03 §3.9 |

C2/C3 prove the tool can return 0; C1 proves legal-but-unmeasured input returns 3, not 2 and not 0. Therefore the named-case exit 2 is a decision about those inputs, not a constant.

---

## 6. Adjacent malformed battery

### 6.1 Matrix

`python3 -B .scratch/o15/run-malformed.py` → **16/17** on the assembled draft; `O15_TOOL=<patched> python3 -B .scratch/o15/run-malformed.py` → **17/17**.

| case | input defect | exit | expected | result |
|---|---|---|---|---|
| M1/M2/M3 | the three named cases | 2/2/2 | 2 | PASS |
| M1j/M2j/M3j | same, `--json` | 2/2/2 | 2 | PASS |
| X1 empty file | 0 bytes | 2 | 2 | PASS |
| X2 top-level array | `[{"id":"O"}]` | 2 | 2 | PASS |
| X3 `--claims` is a directory | `IsADirectoryError` | 2 | 2 | PASS |
| X4 baseline is a tree sha | `765306d…` (the tree of `6e9a30d`) | 2 | 2 | PASS |
| X5 `expect` missing | check has no polarity | 2 | 2 | PASS |
| X6 non-UTF-8 bytes | `0xff` in a JSON string position | **1 + traceback** | 2 | **FAIL** → §7 |
| X7 `claims: null` | not a list | 2 | 2 | PASS |
| X8 duplicate claim id | two `O` rows | 2 | 2 | PASS |
| X9 `baseline_commit: 6` | integer, not string | 2 | 2 | PASS |
| C1 no checks | legal | 3 | 3 | PASS |
| C2 true check | legal | 0 | 0 | PASS |

Focused battery (`verify-named.py`) adds nine shape/`--at` variants, all exit 2:

| case | input | exit | why it matters |
|---|---|---|---|
| A1 no baseline + `--at 6e9a30d` | baseline absent, override supplied | **2** | K03 §3.3: absence is malformed **even with `--at`**; no override rescue |
| A2 key renamed to `baseline` | required key absent | **2** | structural key check, not substring matching |
| A3 `--at worktree` | valid claims, worktree override | **2** | `worktree` does not resolve to a commit; no worktree escape (`git rev-parse --verify worktree^{commit}` fails) |
| A4 nonexistent file | path not on disk | **2** | `OSError` → `GateInputError` (`O01:513`) |
| A5 malformed + otherwise-true check | no baseline, a check that would hold at `6e9a30d` | **2** | **anti-green-leak**: the rest of the file measuring true cannot rescue the document |
| A6 empty `before` | `"   "` | 2 | blank is not a premise |
| A7 blank `baseline_commit` | `"   "` | 2 | non-empty required |
| A8 top-level `null` | not an object | 2 | `O01:526` |
| A9 empty `claims` | `[]` | 2 | non-empty list required |

### 6.2 Determinism of the malformed decision

Each named case was run twice. Exit and `decision_sha256` were identical:

| case | exit run A/B | digest run A/B |
|---|---|---|
| M1 | 2 / 2 | `36d05606…` / `36d05606…` |
| M2 | 2 / 2 | `c5c8fe4e…` / `c5c8fe4e…` |
| M3 | 2 / 2 | `03daf95c…` / `03daf95c…` |

This is consistent with p3's report carrying no timestamp (`O03:76-78`). Note: O14 owns the full determinism claim; this is only the malformed subset.

### 6.3 Usage and unresolvable baseline

```
$ python3 -B .scratch/o15/claims-freshness-o15.py
claims-freshness: error: --claims FILE is required (or --selftest)
exit=2

$ python3 -B .scratch/o15/claims-freshness-o15.py --claims .scratch/o15/fixtures/m4-bad-commit.json --json
run_verdict= malformed exit= 2
err= baseline_commit '0000000000000000000000000000000000000000' does not resolve to a commit …
```

Argparse returns 2 for usage, which matches K03 §3.9. A syntactically valid file whose baseline is unresolvable is malformed, not stale/fresh.

---

## 7. Defects filed by this seat

### O15-D1 (new, high) — a non-UTF-8 claims file crashes part 1

Measured:

```
$ python3 -B .scratch/o15/claims-freshness-o15.py --claims .scratch/o15/fixtures/m9-nonutf8.json
Traceback (most recent call last):
  ...
  File ".scratch/o15/claims-freshness-o15.py", line 352, in load_claims
    text = source.read_text(encoding="utf-8")
UnicodeDecodeError: 'utf-8' codec can't decode byte 0xff in position 64: invalid start byte
exit=1
```

Root cause: `load_claims` catches only `OSError` (`reports/round-47/op/O01-tool-core.md:512-513`). `UnicodeDecodeError` is a `ValueError`, so it escapes the CLI's `except GateInputError` and Python exits 1. The contract is "malformed input … exit 2, not a crash" (`K03:190-205`; `P01:344`). This is a genuine crash class, not a cosmetic mismatch.

Verified fix (one line, fenced below): catch `(OSError, UnicodeDecodeError)`. With it, the broad battery is **17/17** including X6, and the three named cases are unchanged.

```diff
--- a/tools/harness/claims-freshness.py
+++ b/tools/harness/claims-freshness.py
@@
     try:
         text = source.read_text(encoding="utf-8")
-    except OSError as exc:
+    except (OSError, UnicodeDecodeError) as exc:
         raise GateInputError(f"cannot read claims file {source}: {exc}") from exc
```

### O15-D2 (new, low) — malformed reports lose declared provenance

M2's file declares `"baseline_commit": "6e9a30d"`, but the malformed report prints `"baseline_commit": null` and `round: null`, because `load_claims` raises before returning a header and the seam has nothing to pass to `malformed_report`. For unparseable JSON (M3) null is correct; for a parsed document with one bad claim, the declared round/baseline are knowable and useful for triage. K03's report schema expects them when available (`K03:207-238`). Non-blocking for the exit contract; recommend the seam pre-read the JSON **for provenance only** (never for verdicts) or have `load_claims` carry a partial provenance object on `GateInputError`.

### O15-D3 (new, medium) — the probe layer requires `check["id"]`; evaluate the normalized check

`evaluate_check` calls `_result`, which unconditionally reads `check["id"]` (`O02:679-681`), while `validate_check` allows `id` to be absent (`O02:566-639`) and returns a normalized dict that always carries the key. A seam that validates with `validate_check` but evaluates the **raw** input crashes:

```
KeyError: 'id'
  at _result (O02:681) ← _probe_path_present ← evaluate_check ← seam_main
```

My tested seam evaluates the object returned by `validate_check`; that is the contract O02's docstring implies. Record this as an assembly rule: **validate → keep the normalized return → evaluate that**, never the raw check. The crash is in the probe path, not in my malformed cases, but it would turn a legal fresh claim into exit 1 with a traceback (I hit it before fixing the seam; C2 then passed 0).

### Confirmations of already-filed blockers (not new)

| defect | my measured reproduction | filed by |
|---|---|---|
| duplicate `from __future__` mid-file | `SyntaxError: from __future__ imports must occur at the beginning of the file` at assembled line 695 | R01-47 (`review/R01-review.md:204-209`), R04 D1 (`review/R04-gate.md:190`), X03 D4 |
| p2 `__main__` guard runs the selftest before the CLI | `--version` and `--claims` both printed `PROBE-REGISTRY SELFTEST: 43/43` and exited 0 | X03 D1 (`cross/X03-gate-theater.md:158-196`), R04 D2 |
| status vocabulary break | `p3.normalise_clause_result({'status':'mismatch'}) → NOT_EVALUATED`; a contradiction would become exit 3 | R04 D3 (`R04-gate.md:192`) |
| check-schema incompatibility (O05 5/6, O06 9/9 rejected) | `seam_test.py` output reproduced at `.scratch/r04/seam_test.py` run | R04 D4; not this seat's scope |

---

## 8. What this proves and what it does not

**Proves (on the assembled draft, digest `5d8983c4…`):**
- The parse layer rejects the three named malformed shapes with exit 2, a typed error string, a valid `--json` report, and no traceback.
- The malformed path is not bypassable by `--at`, a renamed key, a renamed file, or an otherwise-true check.
- Legal input can still yield 3 (no checks) and 0 (true check), so exit 2 is not a constant.
- The malformed decision is deterministic (same digest and exit on repeat).
- A one-line UTF-8 catch makes every malformed shape in the battery exit 2.

**Does not prove:**
- That `tools/harness/claims-freshness.py` exists, lands, or passes — it does not exist at this cut. The malformed leg is `could-not-evaluate` for the durable link until V02 re-runs the protocol in §9.
- That the probe layer works: the named cases fail during parse, before any probe. The assembled probe layer is separately broken at the seam (status vocabulary) and its O05/O06 fixtures are schema-incompatible (R04 D4); a green malformed matrix must not be read as a green gate.
- That the selftest covers parser/exit controls: part 2's 43/43 is a probe-only control set. O04's parser/exit controls are not drop-in (`R04:144-157`), so the whole-tool selftest remains owed by the integrator (X03 gate 2).

---

## 9. Re-run protocol for V02 (after W01 lands the durable tool)

Run from the lane root with `PYTHONDONTWRITEBYTECODE=1`. Expected exits are the contract; the JSON assertions are the anti-green checks.

```bash
# 1. the three named cases
python3 tools/harness/claims-freshness.py --claims reports/round-47/calib/malformed/m1-no-baseline.json --json; echo "exit=$?"   # 2
python3 tools/harness/claims-freshness.py --claims reports/round-47/calib/malformed/m2-missing-before.json --json; echo "exit=$?" # 2
python3 tools/harness/claims-freshness.py --claims reports/round-47/calib/malformed/m3-not-json.json --json; echo "exit=$?"        # 2

# 2. no-green assertions (jq or python)
python3 tools/harness/claims-freshness.py --claims <m1> --json | python3 -c \
  'import json,sys; d=json.load(sys.stdin); assert d["exit_code"]==2 and d["run_verdict"]=="malformed" and d["refuse"] is True; print("OK")'

# 3. controls
python3 tools/harness/claims-freshness.py --claims <no-checks>; echo "exit=$?"   # 3, never 0
python3 tools/harness/claims-freshness.py --claims <true-check>; echo "exit=$?"  # 0

# 4. non-UTF-8 edge (after the O15-D1 fix)
python3 tools/harness/claims-freshness.py --claims <non-utf8>; echo "exit=$?"    # 2, no Traceback

# 5. usage
python3 tools/harness/claims-freshness.py; echo "exit=$?"                        # 2
```

The integrator should file the fixtures under `reports/round-47/calib/malformed/` (new artifacts, not edits of filed bytes) so V02 does not depend on `.scratch` surviving. Their exact bytes are Appendix B; expected digests are in §4.

**Acceptance:** 3/3 named exit 2; zero `Traceback`; zero `run_verdict: fresh` on malformed; controls 3 and 0; X6 exit 2 after the patch. If any named case returns 0 or prints a traceback, the malformed leg is **not** accepted regardless of the stale-claim demo.

---

## 10. Evidence register

| evidence | command / path | result |
|---|---|---|
| durable tool absent | `ls tools/harness/claims-freshness.py` | no such file |
| p1/p2/p3 digests | `.scratch/o15/assemble.py` extraction | match `O01:14`, `O02:1224`, `O03:84` |
| plain concat fails | first assembled run | `SyntaxError … line 695` |
| guard fires before CLI | first assembled run of `--version` | `PROBE-REGISTRY SELFTEST: 43/43`, exit 0 |
| status break | `p3.normalise_clause_result({'status':'mismatch'})` | `NOT_EVALUATED` |
| named matrix | `python3 -B .scratch/o15/run-malformed.py` | 16/17 (X6 fails) |
| patched matrix | `O15_TOOL=…-patched.py O15_OUT=…run-malformed.py` | 17/17 |
| focused matrix | `python3 -B .scratch/o15/verify-named.py` | 13/13 |
| determinism | `verify-named.py` D1 row | identical digests/exits |
| read-only | `git status --porcelain` | `?? reports/round-46/review/`, `?? reports/round-47/` only |
| tracked files untouched | `git ls-files -m`; `git diff --stat` | empty |
| contract | `claims.json:41,47`; `targets.json:74`; `P01:344`; `K03:99-102,190-205` | cited inline |
| prior art | `R01-review.md:204-220,332-333`; `R04-gate.md:190-195`; `X03:158-196` | cited inline |

---

## Appendix A — tested seam (assembly glue, not filed draft bytes)

This is the `main` O03 §8 delegates to the assembler, plus the status adapter R04 D3 requires. It is reproduced so the integrator can adopt or re-author it; the malformed decisions above come from p1/p3, not from this block.

```python
import argparse as _argparse

_STATUS_ADAPTER = {
    "HOLDS": "HOLDS",
    "MISMATCH": "CONTRADICTED",
    "COULD-NOT-EVALUATE": "NOT_EVALUATED",
    "NOT_EVALUATED": "NOT_EVALUATED",
    "CONTRADICTED": "CONTRADICTED",
}


def _adapt_result(result):
    """Part 2 status vocabulary -> part 3 vocabulary; measured stays verbatim."""
    if not isinstance(result, dict):
        return result
    out = dict(result)
    status = str(out.get("status", "")).upper()
    out["status"] = _STATUS_ADAPTER.get(status, status)
    out["expected"] = out.get("expect", out.get("expected"))
    out["reason"] = out.get("detail") or out.get("reason") or ""
    return out


def _check_dict(check):
    """O01 Check -> the exact key set O02.validate_check accepts."""
    data = check.as_dict()
    return {
        "clause": data["clause"],
        "probe_kind": data["probe_kind"],
        "target": dict(data["target"]),
        "expect": data["expect"],
        "evidence_command": data.get("evidence_command")
        or "git ls-tree -r --name-only BASELINE",
    }


def _emit(report, as_json):
    if as_json:
        print(json.dumps(report, indent=2, sort_keys=True, default=str))
    else:
        print(render_human(report))


def seam_main(argv=None):
    parser = _argparse.ArgumentParser(prog="claims-freshness")
    parser.add_argument("--claims", help="claims.json to evaluate")
    parser.add_argument("--at", help="measure at this commit instead of baseline_commit")
    parser.add_argument("--json", action="store_true", help="machine-readable report")
    parser.add_argument("--selftest", action="store_true", help="part-2 registry control set")
    parser.add_argument("--version", action="version", version=VERSION)
    args = parser.parse_args(argv)

    if args.selftest:
        return selftest_registry()
    if not args.claims:
        parser.error("--claims FILE is required (or --selftest)")

    try:
        doc, baseline, deviation = open_claims(args.claims, at=args.at)
    except GateInputError as exc:
        report = malformed_report(str(exc))
        _emit(report, args.json)
        return report["exit_code"]

    rows = []
    for claim in doc.claims:
        checks = [_check_dict(check) for check in claim.checks]
        errors, validated = [], []
        for index, check in enumerate(checks):
            try:
                validated.append(validate_check(check, claim.before))
            except CheckError as exc:
                errors.append("claims[%s].before_checks[%d]: %s" % (claim.id, index, exc))
        if errors:
            rows.append(judge_claim(claim.id, checks, axis=claim.axis,
                                    before=claim.before, schema_errors=errors))
            continue
        results = [_adapt_result(evaluate_check(check, baseline)) for check in validated]
        rows.append(judge_claim(claim.id, validated, results,
                                axis=claim.axis, before=claim.before))

    report = build_report(rows, round_id=doc.round,
                          baseline_commit=doc.baseline_input,
                          baseline_sha=baseline.commit)
    if deviation:
        report["deviation"] = deviation
    _emit(report, args.json)
    return report["exit_code"]


if __name__ == "__main__":
    sys.exit(seam_main())
```

Assembly recipe (three repairs, then concatenate p1 → p2 → p3 → seam):

```python
for name in ("p2", "p3"):
    body = body.replace("from __future__ import annotations\n", "", 1)
body_p2 = body_p2.replace(
    'if __name__ == "__main__":\n    sys.exit(selftest_registry())\n', "", 1)
```

## Appendix B — fixtures (exact bytes)

`m1-no-baseline.json`:

```json
{
 "round": 47,
 "claims": [
  {
   "id": "O",
   "axis": "operability",
   "before": "the gate is absent",
   "after_required": "the gate exists"
  }
 ]
}
```

`m2-missing-before.json`:

```json
{
 "round": 47,
 "baseline_commit": "6e9a30d",
 "claims": [
  {
   "id": "O",
   "axis": "operability",
   "after_required": "the gate exists"
  }
 ]
}
```

`m3-not-json.json` (truncated; no closing structure):

```text
{"round": 47, "baseline_commit": "6e9a30d", "claims": [
```

`m9-nonutf8.json` (Python bytes literal; `\xff` is a raw byte):

```python
b'{"round": 47, "baseline_commit": "6e9a30d", "claims": [], "x": "\xff\xfe"}\n'
```

`v1-valid-no-checks.json`:

```json
{
 "round": 47,
 "baseline_commit": "6e9a30d",
 "claims": [
  {"id": "O", "axis": "operability", "before": "a premise with no declared checks"}
 ]
}
```

`v2-valid-true.json`:

```json
{
 "round": 47,
 "baseline_commit": "6e9a30d",
 "claims": [
  {
   "id": "O",
   "axis": "operability",
   "before": "the corpus README exists at baseline",
   "before_checks": [
    {
     "clause": "the corpus README exists at baseline",
     "probe_kind": "path_present",
     "target": {"path": "corpus/README.md"},
     "expect": true,
     "evidence_command": "git ls-tree 6e9a30d -- corpus/README.md"
    }
   ]
  }
 ]
}
```

## Appendix C — limits and `to-verify`

1. **Durable path absent.** Everything above was measured on the assembled draft, not `tools/harness/claims-freshness.py`. Re-run §9 after W01/V02; until then the malformed leg is `could-not-evaluate` for the deliverable.
2. **Assembly decisions are mine.** The three repairs and the seam are test glue. If the integrator chooses a different CLI or a different status map, the exit behavior of the malformed path should be unchanged (it is decided in p1/p3), but the `decision_sha256` values will differ.
3. **X6's fix is proposed, not landed.** The patched variant is a demonstration (`4c8b07fb…`); whether to adopt the two-word catch is the integrator's call. The contract requires it.
4. **`round`/baseline provenance in malformed reports** (O15-D2) is a reporting-quality finding; if the integrator fixes it, re-capture the malformed digests.
5. **Not tested here:** symlinked claims paths, JSON with a BOM, enormous/deeply nested inputs, and a claims file whose baseline is a tag. They are outside the three named cases and outside this seat's budget; mark them `to-verify` for V02 if the runner admits them.
