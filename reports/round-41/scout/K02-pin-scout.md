- Seat: K02 | scout | Ca | date 2026-10-19 | baseline 456674d

## Pin census

Scope searched: `SKILL.md`, `SCORECARD.md`, `corpus/README.md`, and `AGENTS.md`, for `8c7dd098`, `b5406bcd`, `15f8b232`, and `10c884337`.

- **SKILL.md:383** is the only hit for the old prefixes in scope: `b5406bcd…`. The adjacent lines date the measurement to 2026-10-18 and identify it as a reader run over the pre-integration packet (SKILL.md:382-388). Classify this as a historical measurement, not a current gate pin/claim; it documents the former reader and should not be rewritten as a present-day digest. Its historical status is established by the dated, pre-integration context; the row does not use a literal `historical` label.
- **SCORECARD.md** has no match for the old prefixes. Its round-38 evidence row records `tools/gates/argot-derivation-gate.py` as `10c88433…` (SCORECARD.md:746-755); this is the round-38 record, and its prefix matches the current file digest measured below, so it is not a stale pin.
- **corpus/README.md** and **AGENTS.md** have no match for any searched prefix. The README's ordinary argot mention at line 176 is descriptive prose, not a digest pin.
- No in-scope live-file occurrence of `8c7dd098…` or `15f8b232…` was found. `15f8b232…` is currently the prefix of `tools/gates/register-law-gate.py`'s exact SHA-256, so do not treat it as stale absent a changed gate digest.

## Owed

None.

## Citations

- Exact-prefix search results: Grep pattern `8c7dd098|b5406bcd|15f8b232|10c884337` separately over `SKILL.md`, `SCORECARD.md`, `corpus/README.md`, and `AGENTS.md`; only `SKILL.md:383` matched. Context search `argot|8c7dd098|b5406bcd|15f8b232|10c884337` surfaced `SCORECARD.md:755` as the current-digest row.
- `SKILL.md:382-388` — dated, pre-integration ceiling measurement; `SKILL.md:383` names the `b5406bcd…` reader.
- `SCORECARD.md:746-755` — admitted round-38 record and `10c88433…` argot-gate pin.
- `corpus/README.md:176` — descriptive argot mention; no digest.
- `AGENTS.md:1-40` — no digest references (source file read).
- Command output: `sha256sum tools/gates/argot-derivation-gate.py tools/gates/register-law-gate.py` returned `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75` and `15f8b23251ca2ad0a203bb1ed5fda2611dff9514e6a1af8120f520b1e7ec4169`, respectively.