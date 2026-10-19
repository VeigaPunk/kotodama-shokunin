- Seat: A08 | verifier | claim A | date 2026-10-19 | baseline 57c8409

# A08 — independent verification of A01–A04

Baseline rechecked: `git rev-parse HEAD` → `57c8409ba16d9f9e692297198d95e8f2ce5a1937`. I did not execute an in-tree `reports/round-*/run-validation.py`, re-freeze the filed r7 target, or inspect external repositories. Findings below distinguish reproduced claims from limits on what the local evidence establishes.

## Findings

### A01 — r7 rerender and component roster

**Reproduced, with a roster-completeness finding.** In a temporary `git archive 57c8409` copy, `python3 -B tools/exercise-handoff-e2e.py --profile v3 --freeze .scratch/render` exited 0: gate 16/16, 20 glossary entries, no findings; uncertainty check 0; 105/105 links; read set 58 files; component digests 26/26; D4 pins 8/8. `cmp` found `packet.md`, `twin.json`, and `expected.json` byte-identical to the filed r7 files. Their SHA-256 values were respectively `45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19`, `0e22913850cd85bc393fe6d0d7a8bf448e9b253aa2884457d4c8999ac9096599`, and `bbe15887b710bb36def5e1c82fa5b1c1ef37df3cb5581c7c2982a0498e829d55`.

The direct `D4_COMPONENTS` roster and r7 frozen input map each contain 12 D4 components, while the packet manifest contains 13, including `13-register-law.yml`. A separate archive mutation appended a comment to that file; `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` exited 1 with `E2E-DIGEST` for the changed component. So A01 is right that this is not a documented skip: it is absent from the direct read-set roster, while its manifest digest is still checked transitively. The r7 pair reproduces faithfully; do not alter or re-freeze its filed bytes.

### A02 — couples and language scan

**Conditional, not an unconditional zero-unresolved result.** I independently scanned all 11 named entries: their per-entry deduplicated couples counts sum to 334, and all 11 filed SHA-256 prefixes match. The documented resolver in `reports/round-19/audit/entry-audit.py:74-96` resolves 319 and leaves 15 basename-only references in `sacred-kingship-mythic-charter.md:37` unresolved. A unique-basename search in `corpus/knowledge` finds one file for each of those 15, with no ambiguity. Therefore A02's 0 unresolved is accurate only if that additional fallback is adopted as an accepted resolver rule; K04's 15 unresolved is accurate under the documented resolver. A02's exact round-34 language predicate produced 127 token matches, 0 verdict-frame matches, and 0 affirmative hits. Its additional PROVINCE-family lexical screen gives categories but no exact patterns or runnable command, so its zero counts are not independently reproducible.

K04's coupling and scope interfaces remain routing findings, not evidence that ownership was breached. Keep both the resolver policy and those interfaces open rather than turning them into canon or admission decisions.

### A03 — Git scope census

**Reproduced within its four-round scope.** The round-33/34/35/36 commit path counts and report-tree counts reproduce as 90/79, 83/79, 92/78, and 47/43. The four commits show no `.ufo/`, earlier-round-report, or frozen-gate paths. Qualifier: `git log cdd66d7..57c8409` includes an additional non-round commit, `139e3b6`, deleting `.ufo/reports/round-32/kotodama.md`; A03's four-commit result must not be generalized to that full raw interval. Its historical 20/40-row worktree samples are time-specific. The post-write `git status --short --untracked-files=all` check showed 65 untracked paths, all under `reports/round-37/`, including this fragment; tracked and staged diffs from baseline were empty.

### A04 — contested scope and freshness pause

**Supported only by local evidence; bilateral status remains unverified here.** The live contract digest `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` matches the kotodama-side record, which expressly records only kotodama's read and excludes Lore's read or acknowledgement. Contract §1 requires same-digest records from both lanes. Accordingly, this seat confirms the local read record but neither asserts nor denies a Lore-side acknowledgement. In-repo boundaries keep the decision with the integrator: contested scope is routed, not absorbed. The round-37 claims keep the freshness pause true, omit freshness from axes in play, and make no freshness move; `REGIMEN.md:27-33` keeps the operator ruling pending.

## Owed

- Integrator: decide whether unique corpus-basename fallback is an accepted `couples:` rule; otherwise normalize the 15 references and rerun the documented resolver. Preserve the distinction between 334 per-entry references and a global set of targets.
- Integrator: route K04's funerary/afterlife, afterlife/world-end, bathing/fire, timekeeping/fire, and binding-speech/kingship interfaces; preserve their unresolved scope without assigning ownership.
- Integrator: route A01's direct read-set roster/documentation correction to a future baseline revision; preserve the filed r7 bytes.
- Integrator/operator: resolve the same-revision bilateral contract read/acknowledgement and the pending freshness ruling. This seat did not check external Lore records.

## Citations

- Assignment, baseline and constraints: `reports/round-37/targets.json:3-8,49-56`; claim and non-goals: `reports/round-37/claims.json:25-34`.
- A01: isolated archive command and output, byte comparisons, mutation control: `reports/round-37/adj/A01-freeze-adjudication.md:7-31`; direct roster: `tools/exercise-handoff-e2e.py:157-170,1939-1953,2208-2222`; frozen inputs: `reports/round-34/handoff/declared-in-r7/expected.json:124-183`; packet manifest: `examples/culture-d4/packet.d4.yml:2875-2888`.
- A02: entry table and language findings: `reports/round-37/adj/A02-entries-bleed.md:7-47`; K04 scan and owed interfaces: `reports/round-37/scout/K04-entries-scout.md:9-43,47-65`; documented resolver: `reports/round-19/audit/entry-audit.py:74-96`; round-34 predicate (read only): `reports/round-34/run-validation.py:283-308`.
- A03: four-commit census and its time-bounded worktree evidence: `reports/round-37/adj/A03-scope.md:5-36`; independent scope qualifier and extra commit: `reports/round-37/adj/A06-verify.md:33-37`; current status and diff command results recorded above.
- A04: local digest and read-record limits: `reports/round-37/adj/A04-contested.md:5-11`; local record: `reports/round-33/adj/contract-read-record.md:1-9`; bilateral gate: `corpus/knowledge/synthesis/worldbible-integration-contract.md:9-18`; local contested-scope boundary: `PROVINCE.md:22-25`; freshness pause: `reports/round-37/claims.json:9-11,32-34` and `REGIMEN.md:27-33`; prior routing: `reports/round-35/adj/audit-assembled.md:347-355`.
