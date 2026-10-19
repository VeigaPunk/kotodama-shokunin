- Seat: Ca05 | verifier | Ca | date 2026-10-19 | baseline 456674d

Independent baseline scan of the named live surfaces found one old argot-gate digest: `SKILL.md:383` cites `b5406bcd…` in the dated worked-ceiling measurement, and `SKILL.md:382-388` dates that measurement to 2026-10-18 and identifies it as the pre-integration reading. Treat as a historical measurement, not a current gate pin; preserve it and add an explicit dated supersession rather than silently rewriting the reading. `SCORECARD.md` has no `8c7dd098`/`b5406bcd` hits and already cites current `10c88433…` at line 755. `corpus/README.md` and `AGENTS.md` have no old digest hits (independent `Grep` scans, 2026-10-19).

The current argot gate hash is `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75`; law-gate hash remains `15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169` (`sha256sum tools/gates/argot-derivation-gate.py tools/gates/register-law-gate.py`). Round-38 validation already records the current argot digest and explains that its older `8c7dd098…` pin was superseded (`reports/round-38/validation.json:17-18`); round-30 audit/rerun records retain the earlier b5406 reading (`reports/round-30/audit/x38-law-gate-baseline.json:20`, `reports/round-30/rerun.json:110-118`) and are filed readings. Round-41 claims/targets mention stale prefixes only as task scope (`reports/round-41/claims.json:20,23`, `targets.json:23`), not as live measurement pins. The law-gate pin was not touched.

Post-draft check: Ca02's before block matches `SKILL.md:382-398`; its proposed after block labels the `b5406bcd…` reading historical, adds a separately dated supersession with the current full digest, and limits it to new measurements (`reports/round-41/calib/Ca02-skill-delta.md:30-55`). Ca03 correctly proposes no SCORECARD change because line 755 already cites current `10c88433…` (`reports/round-41/calib/Ca03-scorecard-delta.md:5-10`). No disagreements with these two drafts. I re-grepped the live surfaces after the drafts appeared: the only old-prefix hit remains `SKILL.md:383`; SCORECARD, corpus README and AGENTS return no old-prefix matches. `reports/round-41/validation.json` is not present, so a current-round validation cross-reference scan cannot yet be done.

## Owed
- `reports/round-41/calib/Ca01-supersession.md` and `Ca04-verify.md` were not present at final scan; review the supersession inventory and compare the first verifier's exact-anchor classifications when they land.
- `reports/round-41/validation.json` is not present; if filed, grep its cross-references only (do not execute the in-tree runner).

## Citations
- `SKILL.md:382-388`, `SCORECARD.md:755`
- `reports/round-38/validation.json:17-18`
- `reports/round-30/audit/x38-law-gate-baseline.json:20`, `reports/round-30/rerun.json:110-118`
- `reports/round-41/claims.json:20,23`, `reports/round-41/targets.json:23`
- Command output: `sha256sum tools/gates/argot-derivation-gate.py tools/gates/register-law-gate.py` (2026-10-19)
- Command output: independent `Grep` scans for `8c7dd098|b5406bcd|15f8b232|10c884337fbb` over `SKILL.md`, `SCORECARD.md`, `corpus/README.md`, and `AGENTS.md` (2026-10-19)
