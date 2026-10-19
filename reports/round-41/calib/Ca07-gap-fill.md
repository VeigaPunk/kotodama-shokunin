- Seat: Ca07 | executor | Ca | date 2026-10-19 | baseline 456674d

## Additional live-surface boundary check

- `SKILL.md:382-389` still quotes the old `b5406bcd…` reader at line 383. Its surrounding text calls this a worked measurement from 2026-10-18 against a pre-integration packet and describes the reading that it supersedes, so this is historical evidence, not the current gate pin. Preserve the measured value; however, the row does not explicitly say “historical.” For the strict stale-hit threshold in `reports/round-41/claims.json:22-24`, Ca02’s SKILL delta should explicitly classify it as a historical reading and add a separately dated supersession, rather than replacing the old measured digest.
- The broad digest scan also finds historical measurements in `corpus/knowledge/linguistics/register-lexicon-ceilings.md:18-20,137` and `corpus/knowledge/linguistics/register-strata-attestation.md:345-369,422`. These passages anchor 2026-10-18 readings to the then-delivered gate; they are not current-pin claims. They are outside the named SKILL/SCORECARD/README/AGENTS surfaces, and `reports/round-41/targets.json:8,26` prohibits corpus changes this round. Do not rewrite them here; if “every LIVE-file row” is meant to include corpus knowledge, record that extension as owed work with a separate permitted scope.
- The same scan finds the current argot digest in `SCORECARD.md:755`; `sha256sum tools/gates/argot-derivation-gate.py` returned `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75`. The requested prefixes were absent from `corpus/README.md` and `AGENTS.md` in the targeted search.

## Owed

- Integrator: decide and record whether corpus/knowledge is excluded from this claim’s live-surface census (round-41 corpus-change prohibition) or requires a future, separately authorized supersession. Until then, do not claim the broader repository-wide stale-pin sweep is complete. `reports/round-41/claims.json:20-24`; `reports/round-41/targets.json:8,26`.

## Citations

- `SKILL.md:382-389`; `SCORECARD.md:755`.
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:18-20,137`; `corpus/knowledge/linguistics/register-strata-attestation.md:345-369,422`.
- Search output: pattern `8c7dd098|b5406bcd|5b5abe78|d7a3ad1a|10c88433` returned the SKILL hit at line 383; SCORECARD’s line 755 current digest; corpus/knowledge hits listed above; no matches in `corpus/README.md` or `AGENTS.md`.
- Command output: `sha256sum tools/gates/argot-derivation-gate.py` → `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75`.
