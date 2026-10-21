# Falsify — SimplifySepTool (Kotodama R50 attempt1)

**Seat:** `KotodamaR50-2.SimplifySepTool-21`  
**Target:** `tools/check-claim-separability.py` @ `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (1230 lines)  
**Axes:** coverage (Ca tool weight), operability (`--selftest`), calibration (r49 fixture + independent prediction)  
**Tools installed:** none (stdlib + existing `python3` only)

## Item attacked

Ca calibration deliverable: separability checker dead code / duplicate logic — whether meaningful deletions exist without breaking `56/56` selftest or the frozen r49 fixture normalization used by `reports/round-50/run-validation.py`.

## Verdict

| Claim | Verdict | Evidence |
|-------|---------|----------|
| Material dead code beyond one constant | **HOLDS** (no bulk dead code) | Module-level AST/name ref scan: every `def`/`class` reachable from `main`, `report`, `evaluate`, or `selftest`. No unused imports (`io`, `math`, `dataclasses`, `contextlib` all used). |
| Safe deletion candidate | **PARTIAL** | One line provably dead; larger DRY/inlining either fails tests or saves ~1 line at clarity cost. |
| `--selftest 56/56` after proposed deletion | **HOLDS** | Private clone after removing `BASE_NAME`: `selftest: 56/56 checks passed`. |
| r49 fixture + independent prediction | **HOLDS** | `rc=1`, 6 findings; `_norm_finding` set equality vs `reports/round-50/separability/r49-expected-independent.txt` → `match True`. |

**Overall simplification attack:** **PARTIAL** — landed tool is already tight; only `BASE_NAME` is falsifiable dead weight. Duplicate-shaped blocks are dual-authority (git-free vs `needs_git`, export vs land-path legs), not redundant paths.

## Dead code (confirmed)

```74:74:tools/check-claim-separability.py
BASE_NAME = "<base>"
```

- **References:** definition only (`grep BASE_NAME` on landed tree → this line; finding strings use literal `"<base>"` in `_acceptance_findings`, not the constant).
- **Verified deletion:** in `/tmp/k50-simplify-4180537` (shared clone, checkout `1c779e4a…`), delete line → **1229 lines**, `python3 tools/check-claim-separability.py --selftest` → 56/56; r49 fixture unchanged (including `C->S` export + land-path deps).

**Smallest fix (author lane):** remove `BASE_NAME = "<base>"` at `tools/check-claim-separability.py:74`.

## Duplicate logic reviewed (not deletion-safe)

| Pair | Lines (landed) | Why retained |
|------|----------------|--------------|
| `_counterfactual` / `_git_counterfactual` | ~553–596 | Different scratch setup; **`InputError` vs `Unevaluated`** on `CannotStart` (malformed vs needs_git leg). Extracted `_acceptance_in_tree` in clone: **1229→1228 lines**, selftest still 56/56 — net ~1 line, adds indirection. |
| Export loop / land-path loop in `_static_findings` | ~624–633 | Same helper `_first_line_hit`, different match semantics (`pattern.search` vs `_name_re(rel).search`). Merging would not remove a leg. |
| `evaluate` / `report` | ~672–721 | `evaluate` single caller (`report`); inlining attempted in clone → **IndentationError**, selftest broken. Separation is structural, not duplicate authority. |
| Selftest `_write_files` vs prod `_place` | ~740–746 / ~505–524 | Fixture git repos vs counterfactual overlay safety (symlink guard). Different contracts. |

## Operability / calibration commands (clone evidence)

```text
$ git clone -q --shared …/kotodama-shokunin /tmp/k50-simplify-4180537
$ git -C /tmp/k50-simplify-4180537 checkout -q 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0
$ python3 tools/check-claim-separability.py --selftest
selftest: 56/56 checks passed - …
$ python3 tools/check-claim-separability.py reports/round-50/separability/r49-fixture.json --lane .
… SEPARABILITY: 6 findings …
$ echo $?
1
```

Independent prediction check (same logic as `run-validation.py:r49_matches`):

```text
match True
want/got: 6 normalized tuples (C->S export + land path, S->C, C->Ca, S->Ca, overlap C/Ca README)
```

## Preserved contract

- Exit codes: 0 clean, 1 findings, 2 input/unevaluated (`tools/check-claim-separability.py:78`, `main` handlers).
- r49 acceptance: exit 1, `FINDING_RE` includes `C->S`, normalized finding set equals `r49-expected-independent.txt` (`run-validation.py:387–404`, `EXPECT["Ca"]["after"]`).
- Selftest roster: 56 named checks unchanged by `BASE_NAME` removal.

## Tradeoff

Deleting only `BASE_NAME` improves maintainability axis trivially with **zero** operability/calibration harm. Aggressive DRY on counterfactual runners or inlining `evaluate` trades test stability and error-type clarity for negligible line count — **stop** per UFO simplifier rule (next deletion would harm an axis).

## Milestone (Ca)

Checker + fixture **HOLD** under falsify; simplification opportunity is **1 line**, not structural redundancy in the 1230-line landed artifact.
