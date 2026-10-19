- Seat: Ca09 | scribe | Ca | date 2026-10-19 | baseline 456674d

## Landed-changes material

At this inspection, no round-41 calibration delta or verification artifact was present: `reports/round-41/` contained only `claims.json`, `targets.json`, and `telemetry/`; no `calib/` fragments existed before this file. No edits were visible in `SKILL.md`, `SCORECARD.md`, `corpus/README.md`, `AGENTS.md`, or the argot gate.

The checked-in argot gate currently hashes to `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75` (`sha256sum tools/gates/argot-derivation-gate.py`). `SCORECARD.md:755` cites the round-38 gate at `10c88433…`. The stale-prefix search across the four live surfaces returned one hit: `SKILL.md:383` cites reader `b5406bcd…` in a dated worked-ceiling measurement over a pre-integration packet; the same passage says it supersedes the pre-fix reading without rewriting it (`SKILL.md:382-389`). This is an explicitly historical measurement reference, not evidence of the gate's current digest. The search found no stale-prefix hits in `SCORECARD.md`, `corpus/README.md`, or `AGENTS.md`.

Accordingly, this snapshot records the currently visible historical quote and current gate pin; it does not establish that the requested supersession cascade is complete. The claim also requires a census of live claims/validation cross-references and two independent verifiers.

## Owed

- Recheck after calibration executors/verifiers produce their fragments; the full live claims/validation cross-reference census and any supersession record remain to-verify.
- Confirm whether the integrator wants the dated SKILL measurement retained as a historical quote or included in the supersession record's filed-readings list.

## Citations

- `reports/round-41/claims.json:20-24` — required pin cascade, thresholds, and verification commands.
- `reports/round-41/targets.json:181-186` — Ca09 assignment and output path.
- `SKILL.md:382-389` — dated historical reader pin and supersession wording.
- `SCORECARD.md:755` — round-38 gate pin.
- `sha256sum tools/gates/argot-derivation-gate.py` output — full current digest above.
- Grep of `8c7dd098|b5406bcd|15f8b232|10c884337fbb` across `SKILL.md`, `SCORECARD.md`, `corpus/README.md`, and `AGENTS.md` — only hit was `SKILL.md:383`; the other three files had no matches.
- `git status --short -- SKILL.md SCORECARD.md corpus/README.md AGENTS.md tools/gates/argot-derivation-gate.py` — no output (no visible modifications to those surfaces).
