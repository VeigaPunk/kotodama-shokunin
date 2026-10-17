# kotodama — supplement-opencode-1 — 2026-10-17

## Work performed

- Rechecked historical/linguistic evidence through one native 32-item
  `AgentSwarm` requesting `opencode-go/deepseek-v4.1-flash`; all 32 workers
  returned completed. `dispatch.json` retains assignments, agent IDs and the
  result digest. Actual simultaneous concurrency and upstream model identity
  were not independently instrumented. One existing replay worker was resumed
  for a bounded security correction; no second swarm batch was launched.
- Recorded 148 distinct checks across 13 assigned source ledgers: 118
  worker-classified supported, 10 contradicted, 20 unresolved. Five parent
  passage re-fetches are recorded in `parent-source-spotchecks.json`.
  Nine corpus entries received dated errata; every baseline entry remains an
  exact byte prefix. The two additional connector/inventory JSON files are
  not included in those acceptance counts. See `validation.json` and
  `corpus/lessons/supplement-opencode-1/sources/`.
- Added assembler controls, digest-verifying frozen replay, a read-only
  uncertainty inventory and an example-specific craft checker. Ran the real
  D2, handoff and craft surfaces, not just imports. Exact argv, outputs and
  tested-file digests are committed in `validation.json`.
- Repaired D2 PAN-03 to `Humaweha`, the full stated `huma + weha` compound;
  propagated owner-ledger references and regenerated the packet. The rejected
  spelling remains in dated errata and historical evidence. No phoneme
  inventory or gate was weakened (`04-name-correction.md`).
- Appended historical corrections rather than rewriting prior verdicts;
  corrected the index's omitted African primary-source map and documented
  actual source-use/tool limits in SKILL.md. Author-side reviews identify
  omitted myth/costume checks, parser defects and handoff limits; they are
  evidence, not independent promotion approval.

## Landed changes

At report filing, child-repo HEAD is
`335d02729d0f19cd3d58a62927fde7fc8a1d3188`. The work commits below are
ancestors of that revision:

- `c53782ab875e88d7311c8b9b1db310357b944685`: source ledgers and append-only
  corpus errata, D2 repair/packet, tools and controls, scoped operating rules,
  province/index/skill/scorecard updates, dispatch and acceptance records,
  and the supplemental lesson. Logged in `LOG.md:2017` (historical corrections)
  and `LOG.md:2062` (three-claim admission and every-axis judgment).
- `f7c0ac6a6fa47aa12decc6b0f4eca596c2fd7724`: normal merge of remote
  `848417c2d366cae2eb07e48fba53f19cafcb6388`. The remote README is retained
  byte-for-byte, both LOG append sequences are preserved, and the merged-tree
  acceptance receipt is included. Logged in `LOG.md:2150`. No force-push,
  rebase, reset or amended cited commit was used.
- `335d02729d0f19cd3d58a62927fde7fc8a1d3188`: actual-interface registry
  correction and refreshed acceptance receipt. The assembler's `--check` is
  classified as a drift gate; the bounded craft checker has a registry row
  and a named input-error limitation. Logged in `LOG.md:2162`.

This report lands after the work commits. It stays inside the child repo
under the operator's narrower write scope: the fleet report location and
MANIFEST ledger were not written, and fleet closure is not claimed.

## Before → after measurements

Baseline: `fe34faaafbe0add59ff68827a0df6c5782a72404`.
Delivered revision: `335d02729d0f19cd3d58a62927fde7fc8a1d3188`.
The final acceptance run preceded that commit with identical tool/packet
bytes; its complete receipt is `validation.json` in the same revision.

1. **Freshness — improved, claim admitted.** The declared requirement was
   at least 10 distinct source checks and at least five retrieved supporting
   or contradicting passages. This wave's source rows went from 0 to 148;
   the five parent re-fetches meet the direct-passage threshold. Worker
   classifications are not 148 independent confirmations, and the 20
   unresolved rows remain unresolved.
   Counting command: `python3 reports/supplement-opencode-1/run-validation.py`
   reports `source_audits: 148`, `supported: 118`, `contradicted: 10`,
   `unresolved: 20`. SCORECARD.md:27 carries the direct ledger-count command.
   The runner checks ledger schema, unique per-entry IDs, baseline hashes,
   short excerpt limits and append-only entry bytes; it does not turn a
   catalogue citation into evidence of an unread book's contents.
2. **Operability — improved, claim admitted.** Assembler selftest absent →
   42/42 controls; replay command absent → both historical seven-row
   manifests reproduced byte-for-byte, plus 79/79 selftest controls.
   Commands: `python3 tools/assemble-d2.py --selftest`,
   `python3 tools/assemble-d2.py --check`,
   `python3 tools/replay-frozen.py --selftest`, and
   `python3 tools/replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv`.
   The attempt-1 manifest also reproduces 7/7. Tampered snapshots, gate/output
   digest changes, traversal and option-like input paths are rejected before
   gate launch. Seven legacy gate selftests remain passing, executed in an
   isolated export because five rewrite fixtures. All actual worktree
   fixture bytes stayed unchanged. The positive craft CLI passes and
   `python3 tools/check-craft-exercise.py --selftest` detects 10/10 mutations.
3. **Calibration — improved, claim admitted.** Historical round-4 finding
   total 24 → corrected 21; audit reports 17 → corrected 16. Historical
   dispatch details without a durable original receipt stay unresolved.
   `python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge`
   now reports 179 entries, 592 raw marker-bearing lines and 598 raw
   occurrences. Baseline raw lines were 590; the increase is discussion
   added by errata, not a quality regression or an excuse to erase flags.
   The exact historical counting commands are in SCORECARD.md:28 and
   `07-historical-corrections.md`. Numeric quality scores were not raised.

`python3 reports/supplement-opencode-1/run-validation.py` exited 0 with
`acceptance_checks_passed: true` on the merged deliverable, including
`git diff --check`. No package/build manifest exists; the standard runnable
checks here are the stdlib CLI selftests and real domain calls above.

Every-axis judgments:

- **depth: improved** as an unclaimed observation. Current D2 findings are
  20 versus corrected baseline 21; one real coda defect disappeared. The
  separate non-canon exercise runs nine derivations and distinguishes sound
  law from register/name-avoidance and borrowed garment strata.
- **coverage: unchanged.** There are 179 existing entries in six partitions,
  including 94 civilization-partition entries (92 bases plus two source
  maps), not 94 independently verified civilizations.
- **operability: improved.** The declared controls and real replay pass.
- **freshness: improved.** The bounded checks/errata and five parent
  passage re-fetches meet the declared observable.
- **calibration: improved.** Units, historical corrections and limits are
  explicit and reproducible; absence of markers is not factual validation.
- **adjacency: unchanged.** The Markdown handoff still passes 16/16 fields
  with 20 glossary entries. It does not prove lore receipt, consent,
  cultural screening or canon acceptance.

All three declared claims verify and no tested axis was harmed; this
supplemental wave is **admitted** on per-axis judgments. Prior numbered
round-2/round-4 rejections are not relabelled. Untested behavior is not
certified harmless.

## SHONEN

- [~] Real decision tables/error patterns/checklists with cited sources:
  `SKILL.md:20`, `SKILL.md:31`, `SKILL.md:55`, `SKILL.md:87`; claim-specific
  source ledgers and their access limits are retained. Author assertion only.
- [~] End-to-end domain task executed and logged: `LOG.md:2062`, current
  D2 gate calls in `validation.json`, and the non-canon contrast exercise.
  Negative D2 outcomes are preserved, not called cleared design.
- [~] Written instructions runnable without oral context: SKILL.md's tool
  registry, the acceptance runner and passing real CLI controls provide
  bounded author evidence. Legacy parser, fixture and malformed-input
  limitations prevent a claim of universal operability.
- [~] No cross-domain bleed: PROVINCE.md retains lore/canon, research-method,
  rights and sibling boundaries. Source review is claim-specific; no
  world-bible, sibling or provider-configuration edits are part of this wave.

No named non-author promotion review ran. The canonical SHONEN.md remains
unchecked; no rank, roster or canon decision is made here.

## Remaining limits and continuation

- D2 still has three phonology REVIEWs and 17 naming findings: six era-ID
  similarity reviews, ten English-label inventory failures, one cultural
  screening hold. Missing native/translated-label typing, executable rank
  rules and full material/era reconciliation remain work, not suppressed
  failures. Clean myth/costume results cover only supplied ledgers.
- Parser/regex negative controls, five fixture-rewriting selftests, legacy
  corpus headers, the separate per-gate expected.json layout, the bounded
  craft checker's input-error handling and a calibrated numeric-axis rubric
  remain explicit conformance debts. A green acceptance assertion does not
  erase these debts. See reviews 23–31 and the supplemental lesson.
- Raw downloaded works and duplicated experiment trees are ignored scratch,
  not redistributed evidence. Durable ledgers retain URLs, short excerpts,
  locators and commands. No provider config or credential material is a
  publication artifact.
- Four numbered rounds are recorded, but old round-4 dispatch provenance
  does not retrospectively certify its advertised batch size: 31 returned
  workers are documented and the original durable dispatch receipt is
  missing. Commit counts cannot repair schedule or evidence defects.
- This OpenCode Go wave is additional work while Z.ai cooled down. The three
  requested 16-worker **non-flash** `zai-coding-plan/glm-5.3` rounds remain
  reserved, followed by the requested 128-worker Grok 4.7 xhigh fast wave,
  then rounds 9–10 on Alibaba DeepSeek. Exact native routing must be observed;
  no custom client or silent model substitution is authorized.
- Publication is not preclaimed by this report. Push to the lane's own
  origin/main, then verify remote HEAD equals local HEAD. The full ten-round
  goal remains active and incomplete after this supplemental closure.
