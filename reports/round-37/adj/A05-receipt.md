- Seat: A05 | executor | claim A | date 2026-10-19 | baseline 57c8409

# A05 — adjacency receipt draft

**Status: dependency-limited draft; no adjacency verdict.** Assignment: draft the adjacency receipt (`reports/round-37/targets.json:53`). Claim A requires a cross-cutting audit of rounds 33–37, including a re-render comparison for the r7 freeze/read-set asymmetry, re-verification of eleven r35/r36 corpus entries, verdicts for every surface, and contested items kept routed (`reports/round-37/claims.json:25-30`). This draft records the available scope and open evidence only; it does not claim those requirements are met or make an axis/acceptance decision (`reports/round-37/claims.json:32-34`).

## Evidence available at this cut

- The checkout reported `git rev-parse --short HEAD` → `57c8409`, matching the declared baseline (`reports/round-37/claims.json:6-7`). The protected-path status query for `reports/round-1..36`, `corpus/lessons`, and `tools/gates/frozen` returned no rows at this sample; this is a point-in-time observation, not a continuous-write guarantee (command output, 2026-10-19).
- `Glob reports/round-37/adj/*` returned **No matches found** at this cut, and reads of all four named A-block outputs returned “does not exist.” Thus A01–A04 have no filed evidence available to fold in this draft (command/tool outputs, 2026-10-19).
- A prior-round scout identified the specific freeze-drift question: the r7 packet declares 13 D4 component digests while `D4_COMPONENTS` / the frozen read set contain 12, omitting `13-register-law.yml`; it also notes that `v3_verify_component_digests` checks packet-declared digests, so the component is checked transitively although absent from the frozen `inputs` map (`reports/round-36/scout/K01-register-scout.md:145-181`). That is a lead from round 36, **not** this round's required re-render comparison or adjudication.
- No validation runner, renderer, bleed scan, or corpus-entry check was run by this seat. In particular, no `reports/round-*/run-validation.py` was executed, as prohibited by the shared rules (`reports/round-37/targets.json:4-8`).

## Claim-A checklist at this cut

| Required surface / decision | Status | Evidence / limitation |
|---|---|---|
| Re-render current tree and compare the r7 pair against frozen bytes; adjudicate whether the 13-component asymmetry is a defect or a documented skip | **to-verify** | A01 output absent. The round-36 scout's recorded 13-vs-12 asymmetry is cited above; it cannot substitute for the specified re-render and adjudication (`targets.json:49`, `claims.json:25-28`). |
| Re-scan eleven r35/r36 corpus entries for cross-domain language and dangling couples | **to-verify** | A02 output absent. “Eleven” is the claim declaration; this seat did not census or re-scan the entries (`targets.json:50`, `claims.json:27-28`). |
| Cross-cutting scope/bleed audit of rounds 33–37 artifacts | **to-verify** | A03 output absent; no independent git-based census was run by this seat (`targets.json:51`, `claims.json:26-28`). |
| Re-verify contested scope: bilateral read, contract digest, and freshness pause remain routed rather than absorbed | **to-verify** | A04 output absent; no re-verification by this seat (`targets.json:52`, `claims.json:32-34`). |
| Per-surface verdicts and zero unfiled bleed | **not established** | The required source fragments and consolidated audit are not available at this cut; no finding of “zero” is inferred from missing evidence (`claims.json:28-30`). |

This is a partial receipt only. It does not repair, re-freeze, or otherwise alter `declared-in-r7`; it does not convert the prior scout's signal into a finding or a documented skip. The required verdict remains open pending the specified evidence and independent verification (`reports/round-37/claims.json:25-34`; `reports/round-37/targets.json:7-8,49-54`).

## Owed

- `reports/round-37/adj/A01-freeze-adjudication.md` — isolated-copy current-tree re-render, comparison against r7 freeze bytes, and evidence-backed disposition of the 13-component asymmetry.
- `reports/round-37/adj/A02-entries-bleed.md` — eleven-entry cross-domain language and couples-resolution scan.
- `reports/round-37/adj/A03-scope.md` — git-based census of rounds 33–37 writes and scope evidence.
- `reports/round-37/adj/A04-contested.md` — bilateral-read, contract-digest, and freshness-pause routing re-verification.
- After these land, reconcile them with verifier results and the final adjacency audit; do not call claim A verified from this draft alone (`reports/round-37/targets.json:54,56,59`; `reports/round-37/claims.json:28-30`).

## Citations

- `reports/round-37/claims.json:6-7,25-34` — baseline, adjacency claim, required state, and non-goals.
- `reports/round-37/targets.json:4-8,49-54,56,59` — shared rules and A01–A06/A11 assignments.
- `reports/round-36/scout/K01-register-scout.md:145-181` — prior-round description of the 13-component / 12-member read-set asymmetry and verifier behavior; not a round-37 adjudication.
- Command/tool outputs at this cut (2026-10-19): `git rev-parse --short HEAD` → `57c8409`; protected-path `git status --porcelain` query → empty; `Glob reports/round-37/adj/*` → `No matches found`; reads of A01–A04 output paths → each “does not exist.”
- No `reports/round-*/run-validation.py` was run (required prohibition: `reports/round-37/targets.json:7`).
