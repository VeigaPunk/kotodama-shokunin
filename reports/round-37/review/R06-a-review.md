- Seat: R06 | reviewer | claim A | date 2026-10-19 | baseline 57c8409

# R06 — second adjacency review

Review scope: adversarial check of the available A-block evidence and the integration state. This is not a claim-A acceptance verdict. The working-tree sample during review contained only round-37 untracked paths; the review does not claim a continuous write audit (`git status --short --untracked-files=all` output, 2026-10-19).

## Findings

### 1. A01's freeze adjudication is supported, with the stated scope limit

I agree with A01's distinction: the r7 D4 read-set roster omits `13-register-law.yml` without a documented exclusion rationale, while the packet-manifest digest check does catch changed bytes for the current packet. This supports a read-set completeness/documentation defect, not a demonstrated integrity bypass.

Independent source cross-checks:

- `D4_COMPONENTS` ends at component 12 and `V3_READ_SET` expands that tuple (`tools/exercise-handoff-e2e.py:157-170,1939-1953`). A search of the filed r7 `expected.json` for `13-register-law.yml` returned no matches; A01/K03 report the corresponding 58-input census (`A01-freeze-adjudication.md:26`; `K03-freeze-drift.md:9`).
- The packet's `assembly.source_sha256` does contain component 13 and digest `c0d77181…f50b7` (`examples/culture-d4/packet.d4.yml:2875-2888`); the live component independently hashes to the same full digest (`sha256sum examples/culture-d4/components/13-register-law.yml` output, 2026-10-19).
- Existing explanatory text is inconsistent rather than a documented skip: the renderer inventory and `ASSEMBLY.md` describe 12 components (`tools/exercise-handoff-e2e.py:51-59`; `examples/culture-d4/ASSEMBLY.md:12-24`), while the r34 repin record explicitly changes packet scope wording from twelve to thirteen authored components (`reports/round-34/handoff/repin.json:32-40`). K03 also checks that the r27 omission predates r7 and finds no explicit skip for this path (`reports/round-37/adj/A07-gap-fill.md:7-13`).
- The verifier parses component hashes from the pinned packet and measures each listed path (`tools/exercise-handoff-e2e.py:2045-2056,2208-2222`). A01 records an isolated mutation control that changed component 13 and produced the named `E2E-DIGEST` mismatch (`reports/round-37/adj/A01-freeze-adjudication.md:29`).

A01 reports byte-identical isolated packet/twin/expected outputs and did not write or re-freeze `declared-in-r7` (`A01-freeze-adjudication.md:9-22,31`). I did not independently rerun that isolated rendering; the assigned A06 command verification remains necessary. A01 used `--freeze .scratch/render`, not the protected r7 destination; preserve the reported destination boundary when independently checking it.

### 2. A03 is a Git-visible census, not proof about arbitrary side effects

A03's boundary is correctly limited: it reports the r33–r36 commit-path census, then a point-in-time r37 untracked-path census, and explicitly excludes arbitrary external filesystem writes (`reports/round-37/adj/A03-scope.md:7-24,28-36`). My current `git status --short --untracked-files=all` likewise showed only untracked paths rooted at `reports/round-37/`, with no tracked modifications. This does not establish per-surface bleed verdicts and should not be used as a substitute for A02 or the full claim-A threshold.

### 3. A04 correctly keeps the contract question and freshness routed

The live contract hash is `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` (`sha256sum` output, 2026-10-19), matching the kotodama-side read record (`reports/round-33/adj/contract-read-record.md:1-9`). The contract checklist requires both-lane read records to agree on revision/digest (`corpus/knowledge/synthesis/worldbible-integration-contract.md:182-184`). A04 reports a different Lore-side digest and no acknowledgement for the current bytes, and leaves ratification/version choice with the integrator (`reports/round-37/adj/A04-contested.md:5-7,11,15`). Its routed disposition is supported; no bilateral acceptance is established. Freshness remains paused and unclaimed under the current claims/regimen (`reports/round-37/claims.json:9-11,32-34`; `REGIMEN.md:27-33`).

### 4. Carry A09's D3 snapshot finding separately from A01's D4 freeze finding

A09 re-ran the frozen D3 evidence-coupling check and reports exit 2 with one `D3-SNAPSHOT` digest mismatch, while the unfrozen check passes (`reports/round-37/adj/A09-gap-fill.md:9-22`). The report routes the existing round-35 F12 to the integrator and explicitly distinguishes it from A01's D4 question (`A09-gap-fill.md:26-35`). The assembled audit must not mark that D3 surface green without recording the invalidation and route.

### 5. Claim A remains unverified at this review cut

A02's eleven-entry bleed/couples scan, A06/A08 independent verifications, and R05's first A review were absent from the output paths when checked (`Glob reports/round-37/adj/*.md` and `Glob reports/round-37/review/*.md`, 2026-10-19). Therefore no “zero unfiled bleed” or complete per-surface verdict is established (`reports/round-37/claims.json:25-30`; `reports/round-37/targets.json:49-56,66-67`).

A05, A11, and S03 are explicitly cut-based drafts whose dependency tables still say A01/A03/A04 were absent; those outputs have since landed. Their historical observations are not false for their stated cuts, but their current owed/status sections need a post-review fold (`reports/round-37/adj/A05-receipt.md:10,18-24`; `A11-audit-draft.md:7,13-17,26-33`; `reports/round-37/scribe/S03-a-receipt.md:5,13,19-27,31-40`). A03 and A10 are scope/inventory evidence, not A02's entry-level scan (`A03-scope.md:9,22-28`; `reports/round-37/adj/A10-scribe.md:17-25`).

## Owed

- `reports/round-37/adj/A02-entries-bleed.md` and `reports/round-37/scout/K04-entries-scout.md` — roster and cross-domain/couples checks for all eleven entries.
- `reports/round-37/adj/A06-verify.md`, `reports/round-37/adj/A08-verify.md`, and `reports/round-37/review/R05-a-review.md` — independent command verification and first adversarial A review; reconcile any disagreement with A01.
- Integrator: refresh A05/A11/S03 after all A evidence lands; carry A09's D3 F12 separately; retain A04's digest-ratification and freshness routes. Do not mark claim A complete from this partial review.

## Citations

- `reports/round-37/claims.json:25-34`; `reports/round-37/targets.json:3-8,49-59,66-67` — claim-A threshold, boundaries, A-block and review assignments.
- `reports/round-37/adj/A01-freeze-adjudication.md:5-31,39-45`; `reports/round-37/scout/K03-freeze-drift.md:9-19`; `reports/round-37/adj/A07-gap-fill.md:7-13` — re-render, component asymmetry, verifier behavior, historical evidence.
- `tools/exercise-handoff-e2e.py:51-59,157-170,1939-1953,2045-2056,2208-2222`; `examples/culture-d4/packet.d4.yml:2875-2888`; `examples/culture-d4/ASSEMBLY.md:12-24`; `reports/round-34/handoff/repin.json:32-40` — independent source cross-check.
- `reports/round-37/adj/A03-scope.md:7-24,28-36` — Git-census scope and limits; command output: `git status --short --untracked-files=all` showed untracked paths only under `reports/round-37/`.
- `reports/round-37/adj/A04-contested.md:5-16`; `reports/round-33/adj/contract-read-record.md:1-9`; `corpus/knowledge/synthesis/worldbible-integration-contract.md:159-172,182-184`; command output: current contract SHA-256 `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069`.
- `reports/round-37/adj/A09-gap-fill.md:9-35`; `reports/round-35/adj/audit-assembled.md:280-293` — D3 snapshot result and carried F12 route.
- `reports/round-37/adj/A05-receipt.md:10,18-24`; `reports/round-37/adj/A11-audit-draft.md:7,13-17,26-33`; `reports/round-37/scribe/S03-a-receipt.md:5,13,19-27,31-40` — stale-at-cut dependency statuses; `reports/round-37/adj/A10-scribe.md:17-25` — descriptive inventory limit.
- Command/tool outputs (2026-10-19): `Grep` for `13-register-law.yml` in `reports/round-34/handoff/declared-in-r7/expected.json` → no matches; `sha256sum examples/culture-d4/components/13-register-law.yml` → `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7`; `Glob reports/round-37/adj/*.md` → A01/A03/A04/A05/A07/A09/A10/A11 present, A02/A06/A08 absent; `Glob reports/round-37/review/*.md` → R05/R06 absent before this fragment was written. No round-validation runner was executed.
