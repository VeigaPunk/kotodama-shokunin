# ReviewSepSemantics — Ca: the r49 separability counterfactual

Seat: ReviewSepSemantics-4 (reviewer, leaf). Scope: Ca only.
Lane: `kotodama-shokunin`, round-50 base `4ad2683`. r49 landing: `d91c632`. Entry blob `ae2226c` (identical at `8c78e6b`, `8cee755`, `d91c632`, `4ad2683`). Registry `corpus/SOURCES.md` blob `34e27f6` at `d91c632` and `4ad2683`. Lesson blob `f03d4c7` at `d91c632`. The worktree equals `d91c632` for these four files (`git hash-object`, no `-w`).
Method: read-only git only (`cat-file`, `show`, `log`, `rev-parse`, `hash-object` without `-w`, `archive` into `/tmp`). Replays ran on git blobs in `/tmp` and were deleted. No lane writes. No tools installed.

## Verdict

1. **The verifier's counterfactual is C-without-S.** Build a tree of base plus C's lands only. In that tree, C's registry-dependent citations must resolve. In that tree, the 12 ids C cites (S031–S042) resolve to nothing. Result: C→S.
2. **`c_without_s` (run-validation.py:264–274) is not that counterfactual.** It checks whether C's own `- source:` line carries an inline URL for each id C cites. Those bytes survive any removal of S, so the predicate cannot fail for an entry that inlines URLs. It passed (validation.json:256–257).
3. **`s_without_c` (run-validation.py:276–305) is not a counterfactual either, and the verifier did not name it.** It rewrote S's own bytes (12 used-by cells removed, 12 rows mined→queued) before testing. Under the same definition applied to S's landed bytes, census 7 prints 12 `missing:` findings for C's path. Result: S→C. The pair is inseparable in both directions.
4. **The receipt's `admitted` is not a separability result.** Admission is C∧Ca∧S, and the separability legs are labelled informational (:264, :342–343). The runner has no path to a separability rejection.
5. **The new checker must flag the r49 pair in both directions.** It must also flag an inline-URL-only C, which is the case the r49 leg passed. And it must not let census-style output pass on exit status: census 5–7 exit 0 with findings (probed).

## 1. The counterfactual the verifier required

Adjudication, `corpus/lessons/round-49-verifier-spotcheck.md:17`: "C cites the registry S creates; the c_without_s runner leg retained inline URLs rather than the required registry rows and therefore did not verify the required counterfactual."

Stated precisely, using the manifest contract's own definition (base + X.lands only, others at base bytes):

- T(C∖S) = `c42d675` + {hunting-foraging entry `ae2226c`, `corpus/README.md` `de7ed40`}. S's paths, `corpus/SOURCES.md` and `corpus/lessons/round-49.md`, are at base, so they are absent.
- C is separable from S iff each S-dependent reference in C resolves in T(C∖S). Every cited id needs a SOURCES row whose used-by names C. The `## Gate` and `corpus/SOURCES.md` pointers must resolve.
- Replay: 0 of 12 cited ids resolve. SOURCES is absent. The Gate lesson is absent. Result: C→S.

C's own text makes these references:
- entry:18 — "registered in `corpus/SOURCES.md` rows S031–S042 … full locators and quotes in the round lesson's `## Gate`"
- entry:201 — "re-check its row id in `corpus/SOURCES.md`"
- entry:20 — "plus the external rows opened this round"

Inline URLs are C's own bytes. They are present in every tree, so they cannot stand in for S's rows.

## 2. Why the r49 `c_without_s` leg failed

- **Wrong object.** run-validation.py:265–268 build `url_ids` and `cited` from C's own text. No tree is built, and SOURCES and the Gate are never read. A predicate over bytes that survive the counterfactual is invariant under it.
- **It tests the declared premise, not the counterfactual.** `reports/round-49/claims-addendum-kaika.json:24`: "C verifies without SOURCES.md because the entry's `- source:` line carries each load-bearing URL and anchor inline." The leg checked that sentence against the entry, and the entry satisfies it. Replay: `url_ids = cited = S031…S042`, `no_inline = []`, `passed = True`. This matches validation.json:241–257.
- **The premise is contradicted by C's own text** (entry:18 and :201 above). Per-row tier, status, used-by, and the access date and quote that the S contract requires (claims-addendum-kaika.json:18) live in SOURCES.md and the Gate. The entry has zero occurrences of "accessed".
- **Non-gating.** :264 says "these legs never gate admission". :342–343 compute `admitted = C and Ca and S`. The receipt records `acceptance_checks_passed: true` (validation.json:2) and `verdict: admitted` (:352).
- **Known to the lane, not fixed.** LOG.md:4001–4003 (commit `d91c632`): "`c_without_s.passed` only tests inline URLs; it does not test the required `S###` registry rows and is an incomplete counterfactual." The only C-side change, `8c78e6b`, narrowed the shelf note from "S031–S043" to "S031–S042". The dependency is unchanged.

## 3. The S side: same definition, opposite leg

- **The rewrite removes the evidence first.** run-validation.py:276–292 rewrites S's rows before the census. It removes the entry path from every used-by cell and sets mined→queued where no citer remains. The census-7 patch at :303–305 would flag the entry path, but the rewrite has already removed every occurrence, so the patch never fires.
- **Replay, rewritten bytes.** 12 used-by cells deleted and 12 rows changed mined→queued (status histogram mined=20→8, queued=22→34). Zero entry references remain. Census 1–7 are clean (validation.json:321–323, `passed: true`).
- **Replay, landed bytes** (base + S.lands, entry absent, census unmodified). Census 1–6 are clean: 47 rows, malformed 0, no duplicate ids, no enum violations. Census 7 prints 12 lines, `missing: corpus/knowledge/culture-material/hunting-foraging-subsistence.md`, for SOURCES.md:60–71 (rows S031–S042, status mined). Exit code 0.
- **Why the lane's premise does not hold on landed bytes.** Census 7 checks only rows with status mined (`if (s=="mined")`). The premise "rows citing the hunting entry would read queued with used-by — and the census would still run" (claims-addendum-kaika.json:24) holds only for a registry where those rows are queued. S's landed bytes are not that registry. "Runs" is not "passes": S's after_required includes "no missing used-by paths" (claims-addendum-kaika.json:18).
- The back-reference set equals C's cited set exactly: S031–S042.

Under the contract rule "X depends on Y if X's landed bytes name any Y land path", the SOURCES used-by cells name C's land path, so S→C holds. It also fails S's own acceptance in T(S∖C). The verifier named only C→S. The checker must report both. Exempting used-by back-references would be a contract change, not a checker default.

## 4. Test cases the new checker must flag

### 4.1 Primary: frozen r49 fixture (`reports/round-50/separability/r49-fixture.json`)

- **base:** `c42d675`
- **C:** tree `8c78e6b`. Lands `[corpus/knowledge/culture-material/hunting-foraging-subsistence.md, corpus/README.md]`. Exports `[]`. Acceptance (inline argv, run in base+C.lands): every cited id matches a SOURCES row whose used-by names the entry, and `corpus/SOURCES.md` and the `## Gate` lesson exist. Otherwise exit 1. The README contributes no edge: it names no SOURCES path and no S ids (checked).
- **S:** tree `d91c632`, the final registry at 47 rows (43 at `8c78e6b`). Lands `[corpus/SOURCES.md, corpus/lessons/round-49.md]`. Exports `["\\bS0(0[1-9]|[1-3]\\d|4[0-7])\\b"]`, verified to match S001–S047 and not S000 or S048. Acceptance (inline argv, run in base+S.lands): census 2 prints `0`, and census 5, 6 and 7 each print nothing. Census 1–4 are counts and histograms, not failures.

Expected: exit 1, with at least these findings:

```
SEPARABILITY_DEPENDENCY C->S via static: entry:18 names corpus/SOURCES.md and '## Gate'; entry lines carry S031-S042 (match S exports)
SEPARABILITY_DEPENDENCY C->S via acceptance: base+C.lands resolves 0/12 cited ids
SEPARABILITY_DEPENDENCY S->C via static: SOURCES.md:60-71 used-by names corpus/knowledge/culture-material/hunting-foraging-subsistence.md (12 rows)
SEPARABILITY_DEPENDENCY S->C via acceptance: base+S.lands census7 prints 12 'missing:' lines
```

A path-only static rule misses the lesson leg, because entry:18 says "the round lesson's `## Gate`" and does not name the path. The S-id exports catch it.

### 4.2 Controls (synthetic git repo in a temp dir)

| id | construction | required result |
|---|---|---|
| SYN-INLINE (the case r49 passed) | S lands `reg.md` with row `S900`, used-by `—`, exports `\bS900\b`. C lands `a.md` containing `- source: **S900** (https://example.org/x — Abstract)` and a body that cites S900. C acceptance: the row must be present in base+C.lands. | exit 1; `C->S` static and acceptance. The r49 predicate returns passed=True on this text (replayed). |
| SYN-ACCEPT-ONLY | C bytes contain no S token and no `reg.md`. C acceptance: `python3 -c "import os,sys; sys.exit(0 if os.path.exists('reg.md') else 1)"`. | exit 1; `C->S via acceptance`. This proves the dynamic leg actually runs in base+C.lands. |
| SYN-BACKREF | S row used-by names `a.md` (C's land) with status mined. C has no S reference. S acceptance: every mined used-by path exists in the tree. | exit 1; `S->C` static and acceptance. The checker must not edit S's bytes to pass. |
| SYN-UNDECLARED | C cites `S900`. No declared claim exports it. Base lacks `reg.md`. Manifest closed-world pattern `\bS\d{3}\b`. | exit 1; `C->UNDECLARED`. This is the r50 frontier case. |
| SYN-CLEAN | C has no S token and no registry path. S row used-by `—`. Both acceptances exit 0. | exit 0. |
| GUARD-INPUT | Manifest entries without tree, exports or acceptance (`reports/round-50/claims.json` as-is). | exit 2, never 0. |
| GUARD-WORKTREE | Pinned trees. A worktree edit adds `S900` to `a.md`. | verdict unchanged; the checker reads `git show <tree>:<path>` only. |

## 5. Defects the r50 design would inherit

1. **Frontier contradiction (claims.json:10, :17).** The contract says C "verifies against base 4ad2683 plus only its own paths" and that C's entry "cites SOURCES rows opened by the frontier step (not a claim)". The base SOURCES (`34e27f6`) has exactly S001–S047. C's S048+ citations cannot resolve in base+C.lands. An undeclared frontier is invisible to the manifest, so the checker would exit 0: the r49 mistake again. L1 has to choose. Either declare the frontier as an item (lands SOURCES.md and the round-50 lesson; exports S048+), or land it in an earlier commit and declare that commit as base. Either way the closed-world rule (SYN-UNDECLARED) is required.
2. **Closed-world scanning will hit Ca's own fixture.** [INFERENCE: the fixture must contain S ids to test, so it will match.] Scope closed-world patterns per claim, or declare fixture exclusions in the manifest. Do not add exemptions ad hoc.
3. **"run on reports/round-50/claims.json exits 0" (claims.json:50).** claims.json has no `schema`, `tree`, `exports` or `acceptance`. The checker must exit 2 on it. The acceptance should point at a pinned manifest written after landing.
4. **Exit-status semantics.** The contract judges acceptance by exit code, and census commands exit 0 even with findings. Probe on a mutated registry: census 5 printed `S031` (duplicate id) with rc 0; census 6 printed `tier S042 Z` with rc 0; census 7 printed twelve `missing:` lines with rc 0. Fixture acceptance must convert findings into nonzero exits.
5. **Dynamic-leg blind spot.** The counting commands copied from r49 (`reports/round-49/claims.json:32–37`: find, ls, sweep, run-validation) never touch the registry. A dynamic leg built from them passes in T(C∖S). Citation resolution belongs in C's acceptance. Without it, only the static leg can flag C→S.
6. **Receipt staleness.** validation.json was measured at `8c78e6b`. Its SOURCES sha256 `933013…` matches that commit's content, which shows 43 rows, 4 rejected, tier B=3 C=6, queued 19 (validation.json:214–218). The landed registry at `d91c632` is `662f96…`, with 47 rows (S044–S047 added by `8cee755`), and round-49.md also changed. The adjudication's "47 rows; census exit 0" describes a state the receipt never measured. Calibration requires pinning trees and re-measuring at the landing commit.
7. **Shared-file attribution.** `corpus/README.md` is in C's lands, and in r49 the same commit (`c6a174d`) also carried Ca's README change (claims.json, r49 Ca). Whole-file attribution would assign other claims' bytes to C. Disjoint lands must be enforced by the manifest, not assumed.
8. **Wording.** "exits 1 naming the C->S dependency (1/1 detected)" (claims.json:50) should read "1 unordered pair, 2 directed edges (C->S and S->C)".

## 6. Proposed QUALITY criterion 7 (for Ca)

> 7. **Separability** — a claim's landed bytes may cite another claim's bytes (registry ids, land paths, anchors) only where the citation resolves in base plus the claim's own lands. An inline copy inside the citing claim does not count as resolution. A counterfactual must not edit the bytes under test. References count in both directions. Grounded in `corpus/lessons/round-49-verifier-spotcheck.md` (REJECTED-HONEST-STOP: C cited the registry S creates).

## 7. Unrun checks and limits

- `tools/check-claim-separability.py` and `reports/round-50/separability/` do not exist yet. Nothing was run against the new checker.
- I did not execute `reports/round-49/run-validation.py` in the lane, because it writes `.scratch/` and `validation.json` there. Its predicates were replayed on git blobs extracted to `/tmp`, since removed. The census commands were taken verbatim from the runner via `ast`.
- Not reviewed: `JjAuditKotodama.md` (operability), and `corpus/QUALITY.md` beyond criterion 6 (`:29`).
- Installs: none.
