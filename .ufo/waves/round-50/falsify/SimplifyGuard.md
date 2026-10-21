# Falsify — SimplifyGuard (Kotodama R50 attempt1)

**Seat:** `KotodamaR50-2.SimplifyGuard-21`  
**Target:** `tools/harness/receipt_guard.py` @ `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0` (vs base `4ad26836552462d28a946ca3b067cab0b5ce3532`: +378/−35, 716 lines landed)  
**Axes:** coverage (O claim + jj-colocation probe), operability (`--selftest` 69/69), calibration (probe 0/3 false negatives on landed bytes)  
**Tools installed:** none (stdlib + `python3` + system `git` only)

## Item attacked

Round-50 **O operability** change in `receipt_guard.py`: multi-ref committed probe (`for-each-ref` over `refs/heads` + `refs/remotes`), `landed_*` / `hit_refs` identity, and synthetic landing selftest harness (`_landing_fixture`, 21× `r50-*` controls). Question: what r50-added complexity is **unnecessary** if all **69** selftest controls and `jj-colocation-probe.py` must still pass?

## Verdict

| Axis | Verdict | Evidence |
|------|---------|----------|
| Coverage (multi-ref probe) | **HOLDS** — not deletable | Removing `_enumerate_refs` / ref loop reverts to HEAD-only; claim `reports/round-50/claims.json` requires remote-aware landed sha. |
| Operability (69 controls + probe) | **PARTIAL** | Baseline: `python3 tools/harness/receipt_guard.py --selftest` → 69/69; `python3 reports/round-50/jj-colocation-probe.py --tools-root <clone>` → `JJ_COLOCATION_FALSE_NEGATIVES=0/3`. Verified deletion stack (−21 lines) keeps both. |
| Calibration (diagnostics vs tests) | **PARTIAL** | Some identity fields and harness checks are test-agnostic; others are asserted by legacy controls and **cannot** be dropped. |

**Overall simplification attack:** **PARTIAL** — ~343 net new lines are mostly load-bearing (probe semantics + landing fixtures). **~21–23 lines** of r50-adjacent code are falsifiable as redundant without failing 69/69 or the colocation probe.

## Verified deletion candidates (private clone)

Clone: `git clone -q --shared …/kotodama-shokunin /tmp/sg-r50-sg2 && git checkout -q 1c779e4a…`. Each patch applied only in `/tmp`; lane tree untouched.

| ID | Proposal | Δ lines | 69/69 | `jj-colocation-probe` | Notes |
|----|----------|---------|-------|------------------------|-------|
| D1 | Drop `listed` set in `_enumerate_refs` **and** the `head is None and branch in listed` guard in `_check_receipt` (`tools/harness/receipt_guard.py:108–130`, `195–198`) | ~6 | pass | 0/3 FN | No control exercises the guard; synthetic git could not produce “symbolic branch listed but HEAD unborn with resolvable ref file” without `rev-parse` succeeding. |
| D2 | Omit `landed_blob=` from refusal/refresh identity string (`213–214`) | ~1 | pass | 0/3 FN | No `must=` token references `landed_blob`. |
| D3 | Remove `_digest_tree` and compare only receipt bytes in `_landing_controls` snapshot (`295–301`, `367–369`) | ~11 | pass | 0/3 FN | Guard does not mutate `.git` on success/failure paths covered by controls. |
| D4 | Trim the extra module doc paragraph (`10–16`) | ~7 | pass | (n/a) | Doc-only. |
| D5 | Drop `if symref: continue` in `_enumerate_refs` (`123–124`) | ~2 | pass | 0/3 FN | `r50-dangling-origin-head` still passes; symref lines do not change landed selection in fixtures. |
| **Stack** | D1+D2+D3+D4 | **−21** | pass | 0/3 FN | Single combined patch, `py_compile` clean. |
| **Stack+** | above + D5 | **−23** | pass | 0/3 FN | Marginal; slightly weaker symref isolation. |

**Smallest author-lane cut:** apply **D1–D4 stack** (−21 lines) first; add D5 only if willing to accept less explicit symref filtering.

## Rejected deletions (would break 69/69 or probe)

| ID | Proposal | Result | Evidence |
|----|----------|--------|----------|
| R1 | Stop failing closed on `for-each-ref` **stderr** (`106–107`) | **BROKEN** | 67/69 — fails `r50-corrupt-remote`, `r50-refresh-corrupt-remote`. Git emits stderr on corrupt remote ref even when behavior is correct. |
| R2 | Remove UTF-8 refname rejection (`117–121`) | **BROKEN** | fails `r50-nonutf8-refname`. |
| R3 | Remove `committed_blob=` from identity | **BROKEN** | fails 19 controls including legacy `committed-refused`, `r50-detached-below-remote`, `attached-head-holds-refused`. |
| R4 | Remove `hit_refs=` from identity | **BROKEN** | fails `r50-local-branch-not-landed`, `unborn-local-branch-refused`, `other-local-branch-refused`. |
| R5 | Inline/remove `_committed_entry`, `_head_state`, `_landing_fixture`, or r50 control block | **BROKEN** (by design) | Reverts multi-ref probe or drops the 21 r50 controls; violates claim “new controls added” and O milestone. |

## Preserved contract

- `guard_receipt` still refuses when any `refs/heads/*` or `refs/remotes/*` tip contains the receipt blob unless `REFRESH_RECEIPTS=1` exactly (`191–220`).
- `landed_ref` / `landed_sha` still come from the first `refs/remotes/*` hit in probe order, never from local branch names alone (`207–214`).
- Selftest roster stays **69** controls (48 legacy + 21 `r50-*`); deletion candidates do not remove controls.
- Landed probe strings may still contain literal `refs/remotes/origin/…` in **selftest** setup (`385+`); production logic uses generic `refs/remotes` prefixes — do not “simplify” by removing remote enumeration.

## Duplicate / dead shape reviewed

| Block | Lines (landed) | Why retained |
|-------|----------------|--------------|
| `_store_object` + `_store_tree` vs old inline `store()` in `_fixture_repo` | `267–293`, `255–256` | Shared by `_landing_fixture` nested trees; dedup is real, not a second convention. |
| `_set_head` vs `_write_ref` | `304–311` | One-liner wrappers; merging saves ~3 lines, adds noise at 15 call sites — below payoff threshold. |
| `r50-refresh-path-refused` vs legacy symlink controls | `494–499` vs `612–618` | Overlapping path guard under refresh=1; still a distinct control name in the 69 roster — delete only with claim amendment. |
| `listed` + branch guard | `108–122`, `195–198` | **Deletion-safe (D1)** — no observed test authority. |

## Operability commands (clone evidence)

```text
$ git clone -q --shared …/kotodama-shokunin /tmp/sg-r50-sg2
$ git -C /tmp/sg-r50-sg2 checkout -q 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0
$ python3 tools/harness/receipt_guard.py --selftest | python3 -c "import json,sys; r=json.load(sys.stdin); print(r['controls_passed'], r['controls_total'], r['selftest_passed'])"
69 69 True
$ python3 reports/round-50/jj-colocation-probe.py --tools-root /tmp/sg-r50-sg2
… JJ_COLOCATION_FALSE_NEGATIVES=0/3
… JJ_COLOCATION_FALSE_POSITIVES=0/4
```

After **D1–D4 stack** on the same clone: same 69/69 and probe `0/3` false negatives.

## Tradeoff

Aggressive cuts past **~23 lines** either break legacy diagnostics (`committed_blob`, `hit_refs`), corrupt-ref stderr handling, or the multi-ref probe itself. The r50 diff is **heavy but mostly honest** for jj colocation; the falsify win is tightening harness/diagnostic cruft, not collapsing `_landing_fixture` / `_enumerate_refs`.

## Milestone (O)

**HOLDS** on functional operability; **PARTIAL** on minimal implementation — landed work is simplifiable by a **small, evidenced stack**, not by removing the ref-scan architecture.
