- Seat: Ca03 | executor | Ca | date 2026-10-19 | baseline 456674d

## SCORECARD.md delta draft

No change is proposed. The stale pre-r38 digests `8c7dd098`, `b5406bcd`, and `15f8b232` do not occur in SCORECARD.md. Its round-38 argot-gate reference already carries the current digest prefix `10c88433…`; the current full SHA-256 begins with that prefix. Rewriting that historical observation or adding a supersession row would imply a stale SCORECARD pin that the census does not show.

Exact before/after disposition:

- Before (`SCORECARD.md:755`): `tools/gates/argot-derivation-gate.py` (sha `10c88433…`); round-38 depth fragments.
- After: unchanged; retain the historical round-38 observation.

## Owed

None.

## Citations

- `SCORECARD.md:755` — round-38 argot-gate digest reference.
- Search `8c7dd098|b5406bcd|15f8b232|10c884337fbb` in `SCORECARD.md` — no matches.
- Search `argot|10c88433|8c7dd098|b5406bcd|15f8b232` in `SCORECARD.md` — the digest-bearing reference is at line 755; other hits are argot-domain text without digest pins.
- Command output: `sha256sum tools/gates/argot-derivation-gate.py` → `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75`.
