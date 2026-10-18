# R21-O10 — R19 scribe-seat failure fallback

- **Disposition:** bounded close-time fallback is documented; route recurrence prevention to R22.
- **Finding and control:** `reports/round-19/validation.json` is dated 2026-10-18 and records `integrator-authored harness (scribe seat failed); all measurements re-run at close`. It records both `counting_command` and `rerun_at_close` as `python3 reports/round-19/run-validation.py`, with `acceptance_checks_passed: true` and `failures: []`. These are attributed R19 receipt claims, not a re-run by this worker.
- **Bounded action:** use that close receipt as the disposition pointer; do not regenerate or overwrite the filed receipt or infer why the scribe seat failed.
- **R22 route / owner:** operator or integrator to define a named scribe-failure trigger, fallback owner, and retained handoff receipt so the close is reproducible without silently replacing the assigned seat. The cause of the R19 seat failure remains `to-verify`.
