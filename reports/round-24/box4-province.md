# Box 4 sub-review — PROVINCE.md accuracy (kotodama-shokunin)

- **Round:** 24 · **Date:** 2026-10-18 · **Baseline revision:** `b5d9844615b32b145fc263e3bd37062dce703b3b`
- **Seat:** non-author C-box reviewer (PROVINCE-accuracy sub-claim of box 4: "no cross-domain bleed; PROVINCE accurate"). This reviewer authored none of the lane's artifacts. Scope of this file is the PROVINCE-accuracy half only; the repo-wide cross-domain-bleed half belongs to the other box-4 seat(s).
- **Method:** every surface PROVINCE.md names was re-resolved against the filesystem on 2026-10-18 (`ls`, `find … -type f | wc -l`, `test -f`), and PROVINCE.md was diffed against the round baseline (`git diff b5d9844… -- PROVINCE.md` → empty; `git status --porcelain PROVINCE.md` → clean).

## Verdict (this sub-claim): **verified**

Every path PROVINCE.md writes resolves; the partition list matches the real tree exactly (six named, six present, no unnamed partition); the refused-sibling names all exist; the document is byte-identical to the round-24 baseline. No stale name, no missing surface, no fix needed.

## Surface-by-surface evidence

| PROVINCE.md claim | Evidence (run 2026-10-18) | Verdict |
|---|---|---|
| Six partitions `corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis,verification,civilizations}` (`PROVINCE.md:10`) | `ls corpus/knowledge/` → exactly those six entries, nothing else; file counts: linguistics 19, myth-symbol 19, culture-material 18, synthesis 29, verification 20, civilizations 94 | accurate |
| "this lane's own gates" (`PROVINCE.md:10-11`) | `tools/gates/` exists — 286 files (gate scripts, `expected/`, `fixtures/`, `frozen/`) | accurate (named without a path; surface real) |
| "source-check records" (`PROVINCE.md:11`) | `corpus/knowledge/verification/` holds `citation-format-and-source-registry.md`, `calibration-registry.md`, `provenance-audit-ledger-format.md`, `gate-battery-surface-verification.md` | accurate |
| "non-canon examples" (`PROVINCE.md:11`) | `examples/culture-d2` (35 files), `examples/culture-d3` (10), `examples/culture-d4` (19), `examples/handoff-packet.sample.{md,yml}` | accurate |
| "reports" (`PROVINCE.md:11,28`) | `reports/` = rounds 5–24 + `supplement-opencode-1` (1,927 files) | accurate |
| Handoff contract path `corpus/knowledge/synthesis/worldbible-integration-contract.md` (`PROVINCE.md:24`) | file resolves; its header states the same adjacency PROVINCE claims: lore owns canon, kotodama hands off (`worldbible-integration-contract.md:1-3`, verified-at 2026-10-17) | accurate |
| Refused siblings: lore, game-dev-2d/3d, chousa, kake, kotoba (`PROVINCE.md:16-20`) | all six exist at fleet root: `lore-shokunin/`, `game-dev-2d-shokunin/`, `game-dev-3d-shokunin/`, `chousa-shokunin/`, `kake-shokunin/`, `kotoba-shokunin/` | accurate (shorthand names, resolvable) |
| "allowed append-only L0 questions" (`PROVINCE.md:28`) | fleet surface `.ufo/l0-questions.md` exists (47 lines) with kotodama entries from rounds 8/9/11; lane behavior matches: round-8 contract-digest drift "escalated to L0, not absorbed" (`SCORECARD.md:302`, `reports/round-8/adjacency.md:36`) | accurate |

## Drift check

- `git diff b5d9844615b32b145fc263e3bd37062dce703b3b -- PROVINCE.md` → empty; `git status --porcelain PROVINCE.md` → clean. PROVINCE.md is byte-identical to the round-24 baseline.
- Last content change was `c53782a` (2026-10-17, supplement-opencode-1), which expanded the partition list from four to six and added the verification/civilizations scope fence (`PROVINCE.md:12-14`). That expansion is exactly what makes the current list match the tree, so the document has been kept current as surfaces grew.

## Observations (non-blocking, no conditions raised)

1. `tools/` is never named by path in PROVINCE.md. The gates are named ("this lane's own gates", `PROVINCE.md:10`) and resolve to `tools/gates/`; the assembler/harness scripts (`tools/assemble-d2.py`, `tools/check-gate-battery.py`, `tools/harness/`, …) fall under "the generative/coupling craft and its records in this repo" (`PROVINCE.md:9-10`). Implicit-but-real coverage; no named path is wrong, so this is not an accuracy failure. If a future round adds a tools inventory to PROVINCE.md, that is an improvement, not a repair.
2. Cross-check with the lane's own records: `SKILL.md` and `corpus/README.md` cite the same partition paths (`SKILL.md:38,99,103,177`; `corpus/README.md:11-22`) — consistent with PROVINCE's surface naming; no internal contradiction found from this seat's probes.

## Sub-claim boundary

This file verifies PROVINCE.md accuracy only. It does not render the full box-4 verdict (which also covers repo-wide cross-domain bleed) and does not touch the promotion DECISION, which stays operator-owned per `reports/round-24/claims.json` (claim C).
