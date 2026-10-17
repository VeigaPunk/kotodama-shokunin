# kotodama-shokunin — round 5 (2026-10-17)

## Work performed

- Followed up the 20 original unresolved supplemental questions in ten
  assigned ledgers, retaining access failures, compound residuals and
  version limits. Raw rows total 22; parent reconciliation is five scoped
  supported and 15 unresolved, not 13 confirmed original claims.
  Evidence: `corpus/lessons/round-5-sources/`,
  `reports/round-5/parent-reconciliation.json`, `LOG.md:2309`.
- Independently re-fetched five bounded source records/passages and appended
  a bibliography-only phonetics erratum. The bark-support, kin-terminology,
  avoidance-register and unnamed-witness distinctions are not universal
  cultural conclusions. Evidence: `reports/round-5/parent-source-spotchecks.json`,
  `corpus/knowledge/linguistics/phonetics-phonology.md:312`, `SKILL.md:154`.
- Added a standalone copied-tree seven-gate selftest battery and repaired
  the craft CLI's six declared malformed inputs plus reviewed nested/mode
  counterexamples. Positive example, genuine finding, existing-report read,
  declared counts, frozen replays and older acceptance remain exercised.
  Evidence: `reports/round-5/validation.json`, `LOG.md:2348`.
- Retained intermediate failed acceptance, executor repair and bounded
  re-review evidence; tested a traceback-veto-removal mutant in scratch.
  Evidence: `reports/round-5/integration-attempts.json`, `15-cli-review.md`,
  `battery-mutation.json`, `LOG.md:2383`.

## Landed changes

Work HEAD at filing: **`9c5263523d3c978140ec886a22f254a224fcd604`**.
This report was written only after that commit. The work commit's author
and committer are `kotodama-shokunin <kotodama@shokunin.local>`; its tree is
`14c97212519b7a9190dcdc6abec3997fca3c8d9f`.

- Source ledgers, parent checks, conservative reconciliation and appended
  Science 363(6432):eaav3218 correction: carrying work hash above;
  `LOG.md:2309` and `corpus/lessons/round-5.md`.
- `tools/check-gate-battery.py` and typed bounded
  `tools/check-craft-exercise.py`, with actual call receipts and mutation
  evidence: same hash; `LOG.md:2348` and `LOG.md:2383`.
- SKILL gate registry/source-to-system decision rows, corpus frontier,
  rolling scorecard, lesson and actual dispatch binding: same hash;
  `LOG.md:2276` and `LOG.md:2419`.

No old gate, frozen manifest, toy law, exercise or D2 packet was changed.
The previous non-flash availability report remains historical. This
child-local report is intentional under the operator's child-only write
scope; it is not the canonical fleet report or a shared-ledger closure.

## Before → after measurements

Baseline: `1ccb2b7119039d8026ad1d004f20427623838b94`.
Delivered work: `9c5263523d3c978140ec886a22f254a224fcd604`.
Claims were declared before the authorized dispatch in `flash-claims.json`;
thresholds were not lowered. Freshness is historically the lowest axis;
no calibrated numeric rubric is claimed.

- **F / freshness:** zero new round-5 follow-ups → 20 original questions,
  22 raw rows, 17 retrieved rows, five parent checks. The required
  ≥10 original follow-ups / ≥3 new relevant passages / ≥3 parent re-fetches
  pass. Four parent checks concern non-bibliographic content; metadata is
  not counted as prose to reach that threshold. Parent dispositions remain
  five scoped supported / 15 unresolved; raw worker labels remain visible.
  Counting command: `python3 reports/round-5/run-validation.py`.
- **O / operability:** no standalone battery (prior parent-only isolation
  existed) → seven of seven actual copied-tree selftests pass. Six declared
  malformed craft inputs changed from traceback/exit 1 to stable diagnostic
  exit 2. Battery selftest is 10/10; craft selftest is ten domain mutations
  plus 18 real CLI subprocess controls. Both round-3 manifests reproduce
  seven of seven recorded verdicts; previous acceptance passes in a copy.
  Commands: `python3 tools/check-gate-battery.py`, its `--selftest`,
  `python3 tools/check-craft-exercise.py --selftest`, both manifest calls in
  `flash-claims.json`, and the combined acceptance command above.
- **Preservation observations:** 179 knowledge entries, six partitions,
  totals 16/16/16/24/13/94; civilization partition is 92 bases + two source
  maps. Inventory is 592 raw marker-bearing lines / 598 raw occurrences
  (600 case-insensitive; 568 parenthesized). Command:
  `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`.
  The handoff sample remains 16/16 fields and 20 glossary entries, exit 0:
  `python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md`.
  D2 still has 20 findings; expected red remains red.

`python3 reports/round-5/run-validation.py` was rerun successfully on the
final working deliverable and again on a clean staged export made by
`git checkout-index --all --prefix=<disposable child-scratch export>/`.
The export had no ignored source downloads or experiment trees; it used
the repo's Git object store only for historical baseline reads. Both runs
reported F=true, O=true, acceptance_checks_passed=true and errors={};
`git diff --check` and staged whitespace checks passed. The tested index
tree equals the work commit tree above. The temporary export was removed.

Exact tested code SHA256 values in `validation.json`:

- Craft: `b5b890b4b9c9953be5ed5f5453a2b60bc9c856616b0a5b28cb2b5bca6ffdf7b5`
- Battery: `077f68e488d56c633c98a0d95a24581389ed655b52e0fb553c3dec5f5ffe9b67`

Removing only the traceback veto in an isolated copy made
CTRL-MARKER-THEN-CRASH reject the mutant, exit 1; the original stayed green,
10/10, with unchanged bytes. One bounded mutation is not universal coverage.

## Dispatch and operator amendments

One actual native batch completed 16/16 distinct workers (agent-456 through
agent-471), explicit alias `zai-coding-plan/glm-5.3-flash-low`, profile
`sec-fast-zai-flash-low`, after the user explicitly authorized Flash.
The host documents the legacy alias at MAX thinking. This is not a
non-flash claim, an upstream wire echo or a measured simultaneous
concurrency assertion. `dispatch.json` records the 1789.607-second native
runtime and nine continuations of existing identities, not extra swarms.

There were two native request attempts: the earlier non-flash host-registry
refusal launched zero workers; the authorized Flash attempt ran one batch.
Both remain distinguishable. Saved request binding:
`reports/round-5/native-request-binding.json`, canonical argument SHA256
`119036a731d817d8df1a7e27c1933790d83a0fa7ea126e0632cf5ae33694b69b`.
No custom provider client, credential read, routing/configuration edit or
implicit model fallback was used. Public scholarly curl/PDF retrieval was
source research, not model-dispatch plumbing.

## Every-axis verdict and admission

- **Depth — unchanged:** same nine-derivation non-canon exercise/D2 packet;
  source-use guidance clarified, no new end-to-end culture task claimed.
- **Coverage — unchanged:** 179 entries in six partitions; no fabricated
  verified-civilization count.
- **Operability — improved:** claim O verifies on real commands and the
  standalone battery, including the declared malformed-input boundary.
- **Freshness — improved:** claim F verifies; 15 residual original questions
  remain explicit rather than being counted as resolved nearby facts.
- **Calibration — improved, unclaimed observation:** raw rows, logical IDs,
  partial support, edition boundaries and intermediate defects reconciled.
- **Adjacency — unchanged:** handoff envelope only; no lore receipt,
  cultural permission, authenticity certification or canon decision.

**Round 5 is admitted author-side:** both measurable claims verify and no
tested axis is harmed. This is not universal untested-behavior assurance,
independent promotion verification or full protocol-conformance closure.
Previous round-2/round-4 rejections are not relabelled.

## SHONEN

- [~] Real decision tables/error patterns/checklists with sources: `SKILL.md`, especially the gate registry and source-to-system rows; `corpus/lessons/round-5.md`. Author assertion, not non-author verification.
- [~] Executed domain-task evidence: existing D2 and non-canon contrastive exercise are rerun in `reports/round-5/validation.json`; D2's 20 findings and missing lore receipt remain explicit. No new whole-culture success is claimed.
- [~] Executable instructions: standalone battery, typed craft CLI and the combined acceptance command ran from the clean staged deliverable at the work hash above. Bounded checks, not arbitrary-schema certification.
- [~] No intended domain expansion: `PROVINCE.md:9`, source-use limits and the unchanged handoff boundary; actual intermediate temporary-file deviations are disclosed below. No non-author verifier, rank change or canon action.

## Remaining debts, scope deviations and next sequence

- The battery is not an OS sandbox; byte equality is not no-write proof.
  It trusts child exit 0 and does not repair old parsers, fixture-rewriting
  tests or self-derived expected values. Five assert-based gate failures
  may conservatively map to could-not-evaluate/2, not recognized-failure/1.
  Craft LAW-ORDER early-return coverage, declared count metadata and the
  frozen example's historical scratch command remain bounded limitations.
- The intermediate recursive-selftest mistake was repaired. Reviewer
  observed 428 historical /tmp craft-selftest directories (~24 MB), unchanged
  by final-byte runs; these were not swept outside the child-only cleanup
  scope. Attributing that residue to intermediate repairs is a timing-based
  inference, not independent forensic proof; read LOG/lesson shorthand with
  that limit. Parent's PID-only check observed no matching live selftest
  process. Worker 12 reported cleaning stray session-root temporary files.
  No such files are shipped, but zero outside writes ever is not independently
  established. See `15-cli-review.md` and LOG.
- Full corpus headers, independent expected.json layout and a calibrated
  numeric axis rubric remain conformance debts. No shared fleet files,
  sibling content, world bible, provider configuration or credentials were
  committed. Raw downloaded works and scratch experiments are not shipped.
- Historical round 4 still documents only 31 worker returns and lacks a
  durable original request; this round does not manufacture compliance.
  Five numbered round records and extra report commits do not complete the
  ten-round goal. No live child task remains from this batch; no fleet
  watchdog mission state was inferred from that observation.
- Pending: **rounds 6–7, Z.ai GLM-5.3 Flash, 16 workers each; rounds 8–9,
  OpenCode Go DeepSeek v4.1 Flash, 32–64 each; round 10, exact Grok 4.7 xhigh
  fast, 128 workers, AFTER DeepSeek**. Grok routing remains to be established
  when relevant; no substitute has been silently selected.

This report lands in a separate lane-identity commit after the work commit,
then both commits are pushed to the lane's origin. Push equality and clean
nonignored Git state must be checked after publication, not assumed here.
