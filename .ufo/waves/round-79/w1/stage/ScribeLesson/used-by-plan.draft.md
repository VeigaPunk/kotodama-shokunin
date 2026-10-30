# Planned used-by and tool registry map (round 79, DRAFT for L1)

Nothing below exists on disk yet except the round-78 and round-77 sources it cites. Paths marked TBD are not named in `CLAIMS-DRAFT.md` and must be chosen by L1; this seat does not invent them.

| artifact | planned path | state now | lands with | used-by / registry cell |
|---|---|---|---|---|
| round-79 lesson (Gate, Mistakes, Trends, Routed) | `corpus/lessons/round-79.md` | missing `[OBSERVED]` (`ls` at base) | L1 integration commit | S897 used-by flips `—` → this path, status `queued` → `mined` in the same commit |
| S897 own-work row (`corpus/SOURCES.md`, registry after S896) | registry row | not present at base (`grep -c "^| S897 "` = 0) | L1 integration commit | row text in `s897-row.draft.md` |
| O ledger-token guard tool | TBD by L1 | not present | after red/green fixtures, controls and selftest pass | SKILL.md gate table row (format at `SKILL.md:681-715`), and S897 used-by once landed `[PENDING-TOOL-PROOF]` |
| Ca census correction record (append-only) | TBD by L1 (must not edit `reports/round-78/telemetry/census-end.txt`) | not present | separable from O and S897 | no registry row; cited from lesson R79-M1 |
| R78-M1 pointer correction record | inside the round-79 lesson (append-only; round-78.md untouched) | not present | with the lesson | none |
| frozen counter for Ca (mismatch 1 → 0) | TBD by L1 | not present | at freeze, after do-nothing and junk controls | `[PENDING-TOOL-PROOF]` |

Census rules that bind this map (`scripts/sources-census.sh`): E11 fails any used-by path missing on disk at validation; W03 flags `mined` with used-by `—`; E05 enum includes `own-work`; E09 accepts `on-change` as a symbolic cadence.

Tool-registry row template for SKILL.md (to be filled only after a passing run; do not land before proof):

```
| <gate-id> | gate | python3 -B <path> --root . --lands <40-hex> --freeze <40-hex> | Output ends `<ID>: PASS` or `: FAIL legs=<n>/<m>`; 0 pass / 1 fail / 2 usage | <selftest command> | — | <notes> |
```
