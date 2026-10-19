- Seat: A04 | executor | claim A | date 2026-10-19 | baseline 57c8409

# A04 — contested-scope re-verification

At the round-37 baseline (`git rev-parse --short=7 HEAD` → `57c8409`), the live contract SHA-256 is `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` (`sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md`). This matches the kotodama-side §1 read record at `reports/round-33/adj/contract-read-record.md:5`, which explicitly limits its scope to the kotodama read and excludes Lore's read or acknowledgement (`:6-9`).

The bilateral gate is **not verified** for the live digest. Lore's round-93 connector record names SHA `50c4c2f25a728e69260b76d42f0d838a398cc4683a6149f74cceeec8fb7268c1` and labels that record informational, not a lane ratification (`/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-93/K1.md:4-5`). Lore's current L0 row says it has no acknowledgement record, that a changed digest requires both lanes to re-read, and requests a ruling about the `50c4…` rev-1.0.0 copy versus a revision bump/re-issue (`/home/vgpnk/Projects/shokunin/lore-shokunin/l0-questions.md:6`). A current read-only `git grep -n -e 'kotodama-lore-adjacency' HEAD -- corpus` in `lore-shokunin` returned no matches (exit 1; tracked corpus only). The current digest and the Lore-side recorded digest differ; this seat does not decide which version to ratify or rewrite either record.

The freshness pause remains active, not absorbed as an axis move: round-37 declares `freshness_pause_in_force: true`, omits freshness from `axes_in_play`, and lists “no freshness axis-move” as a non-goal (`reports/round-37/claims.json:9-11,32-34`). The same pause flag is filed in claims for rounds 33-36 (`reports/round-33/claims.json:16-18`; `reports/round-34/claims.json:17-19`; `reports/round-35/claims.json:17-19`; `reports/round-36/claims.json:12-14`), consistent with the regimen's pause pending operator ruling (`REGIMEN.md:27-33`).

**Disposition:** contested scope remains routed, not absorbed. The prior adjacency audit records the bilateral-read and digest question as unanswered (`reports/round-35/adj/audit-assembled.md:347-355`). `PROVINCE.md:22-25` and the contract's escalation procedure (`corpus/knowledge/synthesis/worldbible-integration-contract.md:159-172`) reserve contested scope for the integrator; no Lore acknowledgement, operator freshness ruling, canon decision, clearance or version ruling is claimed here.

## Owed

- Integrator/operator: adjudicate the live `5f4c…` versus Lore-recorded `50c4…` contract digest and route any required same-revision Lore read/record or revision re-issue. Do not treat the round-93 informational read as an acknowledgement of the current bytes.
- Operator: freshness-threshold ruling remains pending; freshness stays paused and unclaimed.

## Citations

- `reports/round-37/claims.json:9-11,32-34`; `REGIMEN.md:27-33`.
- `reports/round-33/claims.json:16-18`; `reports/round-34/claims.json:17-19`; `reports/round-35/claims.json:17-19`; `reports/round-36/claims.json:12-14`.
- `reports/round-33/adj/contract-read-record.md:1-9`; command output: `git rev-parse --short=7 HEAD` → `57c8409`; `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` → `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`.
- `/home/vgpnk/Projects/shokunin/lore-shokunin/.ufo/waves/round-93/K1.md:4-5`; `/home/vgpnk/Projects/shokunin/lore-shokunin/l0-questions.md:6`; command output: `git -C /home/vgpnk/Projects/shokunin/lore-shokunin grep -n -e 'kotodama-lore-adjacency' HEAD -- corpus` → no matches, exit 1.
- `reports/round-35/adj/audit-assembled.md:347-355`; `PROVINCE.md:22-25`; `corpus/knowledge/synthesis/worldbible-integration-contract.md:9-16,159-172`.
