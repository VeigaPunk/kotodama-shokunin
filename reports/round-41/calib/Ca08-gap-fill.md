- Seat: Ca08 | executor | Ca | date 2026-10-19 | baseline 456674d

## Gap-fill: distinguish a historical reading from a live pin

The only old argot-digest match among the scanned live surfaces is `SKILL.md:383`: the ceiling entry explicitly records a measurement at `2026-10-18T21:53:04Z` and labels `b5406bcd…` as the reader used for that historical result (`SKILL.md:382-395`). Preserve this digest as measurement provenance; do not substitute the current gate digest into the historical result. If the supersession record treats every live-file occurrence, classify this row as a retained historical reading and add any clarification as a separate dated note, not an in-place rewrite.

The current gate digest was independently observed as `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75` by `sha256sum tools/gates/argot-derivation-gate.py`; the filed r38 validation records that digest at `reports/round-38/validation.json:17`. `SCORECARD.md:755` cites the current digest prefix. The `8c7dd098…` declaration at `reports/round-40/run-validation.py:11` is inside a filed r40 runner and must remain untouched under the no-filed-bytes rule.

Surface sweep result: Grep for `8c7dd098|b5406bcd|15f8b232|10c884337fbb` found only the `SKILL.md:383` hit among `SKILL.md`, `SCORECARD.md`, `corpus/README.md`, and root `AGENTS.md`; the latter three returned no matches. In `reports/round-41`, the old-prefix hits are task-definition text at `claims.json:20,23` and `targets.json:23`, not digest pins to a live artifact. The round-41 file inventory currently contains no `validation.json`, so no validation cross-reference audit can yet be completed.

## Owed

- `reports/round-41/validation.json` — absent at this audit; classify any eventual digest mentions as historical measurement context versus current pin when available. Do not run an in-tree round validation runner.

## Citations

- `SKILL.md:382-395` — dated ceiling measurement and reader digest context.
- `SCORECARD.md:755` — current argot-gate digest prefix.
- `reports/round-38/validation.json:17-18` — full current digest and transition note.
- `reports/round-40/run-validation.py:11` — filed old `ARGOT_SHA_UNUSED` declaration.
- `reports/round-41/claims.json:20,23`; `reports/round-41/targets.json:23` — task-definition mentions.
- Command output: `sha256sum tools/gates/argot-derivation-gate.py` → `10c884337fbb2b8f5cc64bedb70e2ddbc34b84c17aaa29fb9be15d049b324a75`.
- Command output: Grep with the four-digest pattern over the four live surfaces above → one hit (`SKILL.md:383`); SCORECARD, corpus README, and root AGENTS returned no matches. Grep over `reports/round-41` → only claims/targets task-definition hits; `Glob reports/round-41/**/*` showed no validation file.
