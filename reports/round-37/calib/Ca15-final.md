- Seat: Ca15 | scribe | Ca | date 2026-10-19 | baseline 57c8409

# Calibration receipt fold — blocked on inputs

## Status

No post-review receipt can be folded from the available artifacts. At inspection, `ls -la reports/round-37` listed only `claims.json`, `targets.json`, and `telemetry/`; no calibration or review fragments were present (command output cited below). Ca15's assigned mission is a receipt fold post-review (`targets.json:33`), but the Ca claim requires a complete recount ledger and two independent verifier samples covering at least 25% (`claims.json:12-18`). Without those inputs, coverage, observed outcomes, dispositions, mismatches, and review resolution are unverified. This fragment records a dependency gap only; it is not a receipt or acceptance claim. No round runner was executed.

## Owed

- Calibration source and fold inputs: `reports/round-37/calib/Ca01-r33.md` through `Ca05-cross-cutting.md`, `Ca06-ledger-draft.md`, `Ca07-verify.md`, `Ca08-verify.md`, `Ca09-coverage.md`, `Ca10-receipt.md`, `Ca11-scribe.md`, `Ca12-gap-fill.md`, `Ca13-audit.md`, `Ca14-gap-fill.md`, and `Ca16-final-verify.md` (`targets.json:19-34`).
- Post-review inputs: `reports/round-37/review/R01-ca-review.md` and `R02-ca-review.md` (`targets.json:62-63`).
- Owner: Ca15. Next touch: fold the receipt after the listed inputs land; record any unresolved evidence as `to-verify` rather than infer results.

## Citations

- `reports/round-37/claims.json:12-18` — calibration claim, required recount coverage and verifier sample threshold.
- `reports/round-37/targets.json:19-34` — calibration source, verification, and receipt tasks; `targets.json:33` assigns this seat's post-review fold.
- `reports/round-37/targets.json:62-63` — Ca review tasks.
- Command output: `ls -la reports/round-37` at inspection listed `claims.json`, `targets.json`, and `telemetry/` only.
