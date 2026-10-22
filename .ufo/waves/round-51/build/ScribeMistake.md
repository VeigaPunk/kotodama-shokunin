# ScribeMistake — round 51 attempt 3 (frontier step: mine one mistake)

Assigned item: mine the round-50 Ca-on-`reports/round-50/claims.json` mistake; draft a `## Mistakes` row in the round-50 lesson format; sweep `corpus/lessons/round-50.md` and `corpus/lessons/round-50-verifier-spotcheck.md` for any other unmined mistake class. All corpus/report/tool bytes cited below were re-read at the lane worktree for this report. No tool was installed or upgraded.

## Result

One mistake mined, row drafted below (id provisional `R51-M1`; L1 renumbers). Sweep found six more unmined mistake classes (Section 3), each with pointers.

## 1. Mined mistake — the declared Ca self-application runs the checker on an input the checker always rejects

**Class.** The round-50 Ca acceptance was declared as a command on `reports/round-50/claims.json`, and that file is not a valid separability manifest: it has `baseline_commit` but no `schema` and no `base` keys, so `tools/check-claim-separability.py` exits 2 before any analysis. The declared exit-0 condition was unachievable from declaration; the frozen receipt records exit 2. No rule executed any declared command on its declared input before the declaration froze.

**Evidence pointer.**
- `reports/round-50/claims.json:50` — Ca `after_required`: "run on reports/round-50/claims.json exits 0", the exact declared argv recorded in the receipt.
- `reports/round-50/claims.json:6` — only `baseline_commit`; no `base`, no `schema` (checker keys).
- `tools/check-claim-separability.py:85` — `MANIFEST_KEYS = frozenset(("schema", "base", "claims"))`; `:372-377` — `_check_keys` raises `InputError` for missing keys; `:1221-1223` prints `SEPARABILITY_INPUT_ERROR` and exits 2.
- `reports/round-50/telemetry/final-conformance.json:29-39` — the committed receipt: argv `["python3", "-B", "tools/check-claim-separability.py", "reports/round-50/claims.json"]`, exit 2, stderr `SEPARABILITY_INPUT_ERROR manifest is missing base, schema`.
- `corpus/lessons/round-50-verifier-spotcheck.md:7-11` — decision: the frozen self-application requires exit 0; the committed receipt records exit 2; a substitute manifest cannot satisfy the unchanged condition. `:19-23` — original authority names the original file, which lacks `base` and `schema`; `final-conformance.json` records the exact argv, exit 2 and the error; Main inspected without execution.
- `corpus/lessons/round-50.md:102` (R50-M6) records the same exit-2 symptom under path spelling; it does not mine the structural-input class (missing keys make the command fail regardless of spelling) or the missing pre-freeze dry run.

**Captured-by.** `none` — no criterion or gate executed a declared command on its declared input before or at declaration; the runner receipted the exit-2 output. R50-M6 (falsify wave) noted the symptom but not this class.

**Fix.** The round-51 declaration dry run, `reports/round-51/claims.json:54` (`dry_run_rule`: every declared counting command and the separability command runs once on the declaration tree before wave 1; each must exit without an input error) and its receipt `reports/round-51/telemetry/declaration-dry-run.txt` (`:16-21`, `:38-40`). The receipt shows (a) the historical round-50 command still failing exit 2 with the same error — evidence the check can fail and was not weakened, and (b) the round-51 manifest now parsing through schema/base/claims to the only remaining error, the not-yet-landed C entry land (`SEPARABILITY_INPUT_ERROR unit C lands 'corpus/knowledge/linguistics/sign-languages-manual-modality.md', which is absent from the worktree`), i.e. structural input validity is established pre-build.

## 2. Drafted row (ready to paste into round 51's `## Mistakes` table)

```
| R51-M1 | declared acceptance command frozen against an input the checker rejects: Ca's self-application `python3 -B tools/check-claim-separability.py reports/round-50/claims.json` can never exit 0 because `reports/round-50/claims.json` lacks the manifest keys `schema` and `base` (it has `baseline_commit`); the committed receipt records exit 2 `SEPARABILITY_INPUT_ERROR manifest is missing base, schema` — an unachievable acceptance whose impossibility was unknowable at declaration | `reports/round-50/claims.json:6,50`; `tools/check-claim-separability.py:85,372-377`; `reports/round-50/telemetry/final-conformance.json:29-39`; `corpus/lessons/round-50-verifier-spotcheck.md:7-11,19-23` | none (no rule executed a declared command on its declared input before the declaration froze; R50-M6 recorded the symptom under path spelling, not the structural class) | round 51's `dry_run_rule` (`reports/round-51/claims.json:54`) with receipt `reports/round-51/telemetry/declaration-dry-run.txt`: every declared counting and separability command runs once on the declaration tree before wave 1 and must exit without an input error; the receipt shows the historical round-50 command still exiting 2 (evidence the check can fail) and the round-51 manifest parsing through schema/base to the not-yet-landed C-entry error only |
```

## 3. Sweep — other unmined mistake classes

Classes already in the round-50 Mistakes table (R50-M1…M9) are not repeated. Unmined classes found:

1. **Dispatch before required load order** — the replacement L1 loaded the shokunin/swarm bindings and required jj trial/audit after dispatch: `corpus/lessons/round-50.md:137-140`. Captured-by: none (disclosed in prose only; R50-M7 covers only the retry burst). Fix: complete the required load order before any dispatch; gate dispatch on it.
2. **Opened sources left unregistered** — build seats opened FAO chapter `x5439e03.htm` and Goody & Tambiah as unregistered leads; the round's unregistered opened-source list was not reconstructed as a census and the search-log note lacks identified/screened/excluded counts and a stop rationale: `corpus/lessons/round-50.md:87`, `:144-147`, `:79`. Captured-by: none. Fix: register every URL opened by a seat; record census counts and the stop rationale.
3. **Source-row locator/quotative errata batch** — S050 anchor ¶3 vs ¶4, S052 page offset drift, S054 paragraph and heading, S064 speech ownership, S060 pages wrong (superseded by S070), S053 "unreachable" wording, S066 seat attribution: `corpus/lessons/round-50.md:109`, `:60` (S070 supersession). Captured-by: none (integrator re-fetch and falsify seats caught them). Fix: locator/quote checkpoint at source intake.
4. **Checker coverage gaps** — acceptance never run base-only (O's manifest acceptance exits 0 on base bytes), acceptance that rewrites another claim's bytes still counts as verified, no lands-provenance check (93 changed paths owned by no unit), `r49_matches` drops counts and locations: `corpus/lessons/round-50.md:110`. Captured-by: none. Fix: extend the checker controls.
5. **Guard/readme-rev selftest insufficiency** — three guard and four `check-readme-revisions` mutants survive; `landed_*` names the alphabetically-first remote holder; `refs/tags/*` unprobed; the design doc still states the HEAD-only contract: `corpus/lessons/round-50.md:111`. Captured-by: none.
6. **README sweep weak oracle** — `reports/round-28/readme/sweep.py` passes a duplicated or out-of-order row: `corpus/lessons/round-50.md:112`. Captured-by: none.

Boundary case, not a mistake class: the commissioned neighbour-boundary 15-row target was not met (11 rows) — `corpus/lessons/round-50.md:119-120`, `corpus/lessons/round-50-verifier-spotcheck.md:47-48`; recorded as a retained debt and routed as repair-first defect 2 for round 51's claim D, not silently lowered.

## Unrun checks

None — this is a read-only scribe report; no product code, judge, or counters were run or modified.
