# Round 22 — SCRIBE X04 report draft

**Axes:** O / operability, C / calibration, D / depth. **Date:** 2026-10-18. **Declared baseline:** `46a03257ee75dd8f685a105e47da3f45a0154172`; declaration HEAD observed by this seat: `cd9c8e4cb62896a8b5d0d642cd04966d41dd4d13`. The claim contract is [`claims.json`](claims.json); detailed command/date/output bindings belong in [`rerun.json`](rerun.json).

**Status: awaiting settled-tree validation, not an admission.** This seat writes only this report and `rerun.json`, plus ignored in-lane scratch used for isolation and receipts. The parent owns final admission, shared LOG/SCORECARD integration, and the final post-integration rerun. A green historical receipt, a draft rule, or a worker's preliminary control is not substituted for the round-22 acceptance command.

## O — routed resolutions

The declared operability worklist is: v3 `declared_in` loss; non-hermetic candidate tie-break; malformed alias coercion; the R17 clone-snapshot question; R18 replay supersession; baseline-binding drift. The canonical new disposition file is `reports/round-22/routed-resolution.json` once landed. These items must each carry a controlled fix or an evidence-backed documentation disposition; frozen re-pins must be new rows/files. The D4 bleed is the separate D claim, not a seventh O item or proof that the entire historical defect backlog was closed.

**Already supported, not source-fixed:** [`fixes/snapshot-r17.md`](fixes/snapshot-r17.md) demonstrates the absolute-ancestor `.scratch` scanner defect in a complete isolated clone. Its dated reproduction command (2026-10-18T14:40:46Z) finds all 16 evidence files byte-matched, while the unchanged absolute-root scanner reports 0 fragments; rebasing only enumeration to the clone's relative root restores 16 fragments, 7 fixed and 5 attempted. Restoring the absolute root returns 0. This resolves a sufficient mechanism, not the unknowable transient contents of the original recount clone. The filed R17 rejection and scanner are not rewritten.

Other O closures remain pending their final control artifacts and the new runner. No historical validator has been executed in the live lane by this seat.

## C — honest loop-2 checkpoint

The retrospective covers rounds 17–21, not completion of the amended loop 17–24. The independent read-only count command in [`retrospective-audit-C08.md`](retrospective-audit-C08.md) (2026-10-18) establishes four filed admissions (R18–R21), one rejection (R17), and stored claim flags 14 passed / 1 failed. These are archived harness outcomes, not a fresh recertification of every literal claim threshold.

The R17→R18 arc must remain bounded: R17 D failed for missing typed-chain/frozen evidence; the D2-bound gate was an architectural blocker. R18 generalized the gate and delivered a working D4 pipeline. Round 21 independently reproduced D4 19/19 and byte-identical default-D2 output at the before/after revisions (`reports/round-21/validation.json`, `claims.C.measurement.round18_repair_reproduction`; command/date recorded there, 2026-10-18). That does **not** establish equality to R17's competing pre-implementation hold declarations, adjudicate the design fork, erase D2 fixture carry, or retroactively admit R17.

Calibration populations stay separate. C08's dated read-only command counts R21's 23 defect rows as 13 open + 5 closed + 5 observation, with 18 non-closed routes; the six declared R22 O items are a scoped worklist. Its recount is 63 rows = 39 matches + 24 dispositions, not a 100% byte match or a freshness score. Two structural regimen amendments and one separately counted R19 provider substitution must not be collapsed into an unqualified amendment total. Reported attendance is not an independent dispatch trace; R19's local availability receipt leaves completion unknown.

The consolidated retrospective, pointer/number audits, new baseline corrections, freshness-threshold operator question and SCORECARD draft still require their final hash-bound review. No paused freshness threshold is changed here.

## D — source-level family isolation

The filed D2→D4 bleed (`A21-D4-XF-01`, `reports/round-21/adjacency/ledger.json`) must be fixed in the projector, not merely hidden by a D4-only filesystem mirror. [`bleed/impl.md`](bleed/impl.md) traces the pre-fix unconditional embedded D2 rank fixture; [`bleed/skill-rule-draft.md`](bleed/skill-rule-draft.md) proposes a family-owned-label rule for parent integration. Both source isolation and finding-set honesty need controls: reject the old projection, preserve canonical D2 bytes, bind D4 labels/rank rows to D4 sources, preserve native-form obligations, and issue new frozen generations with explicit rationale for any removed findings.

A deterministic gate pass alone cannot prove family isolation. Final source decision, verification and re-pin evidence are pending; D4 19/19, adapter 12/12 and handoff v3 105/105 must be measured after the fix before D can be reported green.

## Settled-tree rerun and preservation

This seat cloned the lane to `.scratch/r22-x04/checkpoint-a` and overlaid a hash-inventoried snapshot at **2026-10-18T14:50:00Z**, with source bytes stable during the copy. `python3 .scratch/r22-x04/capture.py run checkpoint-a .scratch/r22-x04/commands.json` (2026-10-18T14:50:07–14:50:44Z) executed **32/32 real regression commands successfully**, including D4 gate **19/19**, adapter **12/12**, combined projector **163/163**, D2 byte-identical projection, v2 **50/50** links and v3 **105/105** links, **27** claims, statuses **16/7/4**, fields **16/16**, glossary **20/20**, zero findings. The v3 selftest included complete carried-edge equality and field-deletion/truncation negatives. Commands and stream hashes are retained in `.scratch/r22-x04/checkpoint-a-regressions.json` for the final rerun record.

**The aggregate checkpoint is red, not an admission.** `python3 reports/round-22/run-validation.py --selftest` (2026-10-18T14:50:54Z) passed **21/21** controls. The actual counting command, `python3 reports/round-22/run-validation.py` (2026-10-18T14:50:54–14:51:33Z), exited **1**, acceptance false: O lacked the resolution ledger/new frozen generation; C lacked the landed SCORECARD summary and final audit PASS stamps; D's product/boundary legs passed but the draft failed the runner's then-current dated-command requirement. Its runner SHA was `470e503a508e38f850ccff35a1d50ba22f42e23ff798150fe4f4229030038064`. Its clone-only receipt is `.scratch/r22-x04/checkpoint-a/reports/round-22/validation.json`; no live receipt was written. The runner and combined source pins changed after the checkpoint, so this is retained as in-flight evidence, not represented as the final settled result. A later snapshot and rerun are still pending.

Initial preservation control: `export TMPDIR="$PWD/.scratch"; PYTHONDONTWRITEBYTECODE=1 python3 .scratch/r22-x04/capture.py protect` at **2026-10-18T14:41:48Z** compared all **1,018 tracked filed paths** under reports rounds 8–21 to the declared baseline, including mode identity: **0 mismatches**, protected status empty. Manifest SHA-256: `8eaa73b290eb0b85240b79d91d8f2cb5d41b77d2e009003be0072e699a896ff4`. This is a point-in-time check, not proof no transient write occurred between observations; ignored logs have no baseline identity.

## Limits and handoff

All artifacts are NON-CANON engineering evidence. No source-freshness certification, real-world rights clearance, lore acceptance or promotion is claimed. Parent integration must preserve the filed rounds, retain named historical mismatches and residual design/owner decisions, and remeasure if the delivered source or frozen baseline changes after this seat's snapshot. No commit or push was made and no shared bookkeeping file was edited by X04.
