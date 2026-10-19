- Seat: R08 | reviewer | cross | date 2026-10-19 | baseline 57c8409

# F-C13-1 conformance review

## Result

**No in-tree runner execution is recorded in the round-37 artifacts inspected; round-wide compliance remains to-verify.** The shared rule prohibits running any `reports/round-*/run-validation.py` in-tree and permits isolated git-archive copies only (`reports/round-37/targets.json:3-8`). The three declared counting-command fields name `python3 reports/round-37/run-validation.py`, but are a required command declaration, not evidence it was run (`reports/round-37/claims.json:17,23,29`). Ca10 labels the acceptance runner pending and not run (`reports/round-37/calib/Ca10-receipt.md:19`); S05 reports that observed-dispatch and validation artifacts were absent at its inspection, so no process-level dispatch/runner record is available (`reports/round-37/scribe/S05-telemetry-draft.md:3,90,94-95`).

I inspected all 24 seat output paths present in the round-37 target inventory at this cut. The round-wide text scan surfaced runner commands as filed-history inventory, required-command declarations, or plans/hazard descriptions; it did not find an execution transcript or a claim that a round runner was run in-tree. Multiple fragments explicitly say no round runner was executed: K01, Ca10, Ca11, Ca13, Ca15, Ca16, O05, O08, O10, O11, O12, P01, R02, X00, X04, and A05 (see citations below). These are artifact attestations, not independent process telemetry. Accordingly this is a **provisional no-recorded-breach finding**, not a verified global absence.

## Isolation hazard for future recounts

P01 correctly warns that an archive extraction alone is not safe for the filed r34/r35 runners: they hard-code the live repository root and `chdir` there, and P01 says not to execute them if path audit cannot prove containment (`reports/round-37/plan/P01-ca-plan.md:21-24`). O08 and O12 independently describe this as a carried runner-design hazard and say those seats did not execute a runner (`reports/round-37/op/O08-gap-fill.md:5-13`; `reports/round-37/op/O12-gap-fill.md:5-12`). X01 likewise warns against running a known absolute-root runner from a merely extracted copy (`reports/round-37/cross/X01-trades.md:9-14`). This is a material safety precondition, not evidence of an r37 breach. Do not count a plain archive replay of those runners as isolated without a demonstrated containment mechanism; if it cannot be proven safe, preserve the command as could-not-reproduce with owner and reason, as P01 specifies (`P01-ca-plan.md:22-24,28-31`).

## Scope limitation and owed work

The target-path census command, run from the repository root after setting the required environment, returned `assigned=64 present=24 missing=40`. This review accounts for the present 24 outputs but cannot verify statements or actions in the remaining seat fragments. The assigned R08 path was among the 40 absent paths at census time; this report now fills that path. Re-run the conformance review after the other target outputs land. Process-level proof also remains owed: `reports/round-37/telemetry/observed-dispatch.json` and `reports/round-37/validation.json` were absent at S05's inspection (`S05-telemetry-draft.md:3,105`).

## Owed

- `reports/round-37/scout/K02-defect-census.md`, `K03-freeze-drift.md`, `K04-entries-scout.md`.
- `reports/round-37/calib/Ca01-r33.md`, `Ca02-r34.md`, `Ca03-r35.md`, `Ca04-r36.md`, `Ca05-cross-cutting.md`, `Ca07-verify.md`, `Ca08-verify.md`, `Ca12-gap-fill.md`, `Ca14-gap-fill.md`.
- `reports/round-37/op/O01-queue-draft.md`, `O02-fix-verify.md`, `O03-carry-verify.md`, `O04-receipt.md`, `O07-scribe.md`, `O09-routing.md`.
- `reports/round-37/adj/A01-freeze-adjudication.md`, `A02-entries-bleed.md`, `A03-scope.md`, `A06-verify.md`, `A07-gap-fill.md`, `A08-verify.md`, `A09-gap-fill.md`, `A10-scribe.md`, `A11-audit-draft.md`, `A12-gap-fill.md`.
- `reports/round-37/review/R01-ca-review.md`, `R03-o-review.md`, `R04-o-review.md`, `R05-a-review.md`, `R06-a-review.md`, `R07-cross-review.md`.
- `reports/round-37/cross/X02-honesty.md`, `X03-protocol.md`; `reports/round-37/scribe/S02-o-receipt.md`, `S03-a-receipt.md`, `S04-integration-draft.md`.
- After artifacts land, re-scan the full target set and any observed execution/validation evidence; do not upgrade this provisional finding without evidence.

## Citations

- `reports/round-37/targets.json:3-8,69` — absolute no-in-tree-runner rule, evidence rules, and R08 assignment.
- `reports/round-37/claims.json:17,23,29,32-34` — declared validation command and explicit no-in-tree-execution non-goal.
- `reports/round-37/calib/Ca10-receipt.md:19`; `Ca11-scribe.md:9`; `Ca13-audit.md:9`; `Ca15-final.md:7`; `Ca16-final-verify.md:3` — pending or explicit no-runner statements.
- `reports/round-37/op/O05-verify.md:22`; `O08-gap-fill.md:13`; `O10-gap-fill.md:25`; `O11-final.md:23,42`; `O12-gap-fill.md:12`; `reports/round-37/plan/P01-ca-plan.md:35`; `reports/round-37/review/R02-ca-review.md:5`; `reports/round-37/cross/X00-connector.md:39`; `X04-sentinel.md:13`; `reports/round-37/adj/A05-receipt.md:12,40` — per-seat non-execution attestations.
- `reports/round-37/plan/P01-ca-plan.md:21-24`; `reports/round-37/op/O08-gap-fill.md:5-13`; `O12-gap-fill.md:5-12`; `reports/round-37/cross/X01-trades.md:9-14` — archive isolation hazard and required pre-execution controls.
- `reports/round-37/telemetry/dispatch-declared.json:2-16`; `reports/round-37/scribe/S05-telemetry-draft.md:3,90,94-95` — declared allocation only; observed dispatch and validation evidence were absent at S05's cut.
- Command output (2026-10-19): `Glob reports/round-37/**/*` enumerated the current tree; after `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, a read-only `python3` target-path check reported `assigned=64 present=24 missing=40` and the missing paths listed under Owed (including R08 before this file was created).
- Command output: `Grep` over `reports/round-37` with `(?i)run-validation\.py|in[- ]tree|runner|execut(e|ed|ion)` found declarations, historical command citations, plans, hazard discussion, and no execution transcript or in-tree-run claim in the inspected files.
