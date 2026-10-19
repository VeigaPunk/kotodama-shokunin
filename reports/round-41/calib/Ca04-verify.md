- Seat: Ca04 | verifier | Ca | date 2026-10-19 | baseline 456674d

## Verification

- **Ca02 / SKILL.md:** Its exact `Before` block (`SKILL.md:382-398`) matches the current live text and the old `b5406bcd…` occurs once in the live-file census, at `SKILL.md:383`. The dated 2026-10-18 measurement is explicitly over the pre-integration packet (`SKILL.md:382-388`), so it is a historical reading rather than a current pin. Ca02's proposed replacement makes that classification explicit and adds a 2026-10-19 supersession naming the current full gate digest; the SHA-256 matches the independent command below (`reports/round-41/calib/Ca02-skill-delta.md:27-55`). Its remaining `b5406bcd…` references are explicitly qualified as historical. **Verified.**
- **Ca03 / SCORECARD.md:** No stale-prefix occurrence (`8c7dd098|b5406bcd|15f8b232`) exists in the live file. The draft's no-change decision is anchored at `SCORECARD.md:755`, which records `10c88433…`; the current gate digest begins with that prefix. It correctly preserves this round-38 measurement rather than inventing a stale-pin replacement (`reports/round-41/calib/Ca03-scorecard-delta.md:3-10`). **Verified.**
- **Other in-scope surfaces:** The read-only prefix scan found no stale hits in `corpus/README.md` or `AGENTS.md`. The old `8c7dd098…` and `15f8b232…` prefixes do not occur in the four in-scope files. The latter is the current register-law gate SHA, which was not touched.
- **Exactly-once / scope:** Live scan output: `SKILL.md:383` is the sole old-prefix hit; SCORECARD, corpus README, and AGENTS report no stale-prefix hits. The round-41 claims/targets mentions are task-scope text, not live gate measurements (`reports/round-41/claims.json:20,23`; `targets.json:23`). No live file was edited by this verifier.

## Owed

- `reports/round-41/calib/Ca01-supersession.md` was absent at the final check (Glob returned no match). Its row inventory/completeness cannot be cross-checked against the verified Ca02/Ca03 deltas; owner: Ca01/integrator. Ca02 and Ca03 were present and verified.

## Citations

- `SKILL.md:382-398` — source anchor; dated historical measurement and old reader digest.
- `SCORECARD.md:746-755` — round-38 record; current argot-gate digest prefix.
- `reports/round-41/calib/Ca02-skill-delta.md:5-55` — exact before block and proposed explicit historical label/supersession.
- `reports/round-41/calib/Ca03-scorecard-delta.md:3-10` — no-change delta and its live anchor.
- `reports/round-41/scout/K02-pin-scout.md:5-10` — independent in-scope census and historical classification.
- `reports/round-41/calib/Ca05-verify.md:3-5` — independent baseline scan; its scan predated the arrival of Ca02/Ca03.
- Command output after `cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`: `sha256sum tools/gates/argot-derivation-gate.py tools/gates/register-law-gate.py` → `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75` and `15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169`.
- Command output: read-only prefix scan of SKILL.md, SCORECARD.md, corpus/README.md, AGENTS.md → sole hit `SKILL.md:383`; remaining files report no stale-prefix hits.
- Command output: `Glob reports/round-41/calib/Ca01-supersession.md` → no match.
