# kotodama-shokunin — round 6 development checkpoint (2026-10-17)

**Not admitted.** The operator requested all existing development be pushed
before starting a new session. This report preserves real executed work and
its unfinished acceptance queue; its existence is not a passed-round,
promotion or fleet-closure signal.

## Work performed

Declared claim: **F / freshness**, historically the lowest non-retired axis,
with unchanged thresholds in `reports/round-6/claims.json`.

- Executed one native sixteen-worker Z.ai GLM-5.3 Flash MAX batch; all
  sixteen completed. Three actual-output review continuations retained the
  same identities and also completed. Evidence: `dispatch.json`,
  `native-request-binding.json`, `LOG.md` round-6 checkpoint entry.
- Added twelve source ledgers, two fixed question IDs per entry, covering
  early language/myth/symbol/era/material reference surfaces. Evidence:
  `corpus/lessons/round-6-sources/02.json` through `13.json`, `targets.json`.
- Preserved initial concurrent-output limitations and appended the later
  actual reviews rather than manufacturing an earlier pass. Evidence:
  `14-linguistic-review.md`, `15-material-review.md`, `16-calibration-critic.md`.
- Added a mechanical checkpoint/preservation runner, measured it on the
  delivered staged tree, and recorded the remaining integration queue.
  Evidence: `check-checkpoint.py`, `checkpoint-validation.json`,
  `checkpoint.json`, `corpus/lessons/round-6.md`.

## Landed changes

Work HEAD at filing: **`19c5a867c64b502a8aa4192ae7562b90d7d14d9f`**.
The report was written only after this lane-identity work commit existed.
Its tree is `2e581a8fa887326c3e3b00415df2368d79095dc0`, the exact staged
checkpoint tree that passed the clean-export check.

All source fragments, review appendices, native dispatch/claim/baseline
records, checker/receipt, SCORECARD pending section, append-only LOG entries
and the round-6 lesson are carried by that work hash. Each is tied to the
LOG declaration headed "round 6 declaration: early-reference source checks,
Flash MAX" or the appended "round 6 development checkpoint before session
handoff — not admitted" entry. No old gate/example or knowledge entry was
changed. This report lands separately, last, under the same lane identity.

## Before → after measurements

Baseline: `030c3928de74ed514853bc1f7490e0f8bb4d451f`.
Work measured: `19c5a867c64b502a8aa4192ae7562b90d7d14d9f`.

- Round-6 source rows: **0 → 24 fixed question rows across twelve entries**.
- Actual worker returns: **16/16**, one batch, plus three existing-identity
  review continuations. Native reported runtime: **1224.021 seconds**.
- Raw main-passage keys: **24 distinct**. Excluding tertiary/catalogue/
  unavailable kinds leaves **20 candidates across eleven entries**.
  These are mechanical candidates, not parent-confirmed relevant passages.
- Raw worker labels: **24 supported**, scoped by workers as **18 whole /
  six partial**. Reviews identify additional whole-to-partial candidates;
  do not publish this as twenty-four resolved historical facts.
- **468 baseline historical files** are byte-identical. Previous round-5
  acceptance passes in a disposable copy, preserving the original receipt.

Re-run: `python3 reports/round-6/check-checkpoint.py`.
Observed exit **0**, checkpoint_checks_passed=true,
previous_acceptance_passed=true, **round6_admission=pending**.
`git diff --check` and staged whitespace checks passed. The same checker
passed on a clean `git checkout-index` export without ignored raw downloads
or experiment trees; the disposable export was removed.

The original admission command is still
`python3 reports/round-6/run-validation.py`, **not yet implemented**.
Its F thresholds are not replaced by the easier checkpoint check. Parent
re-fetch receipts and conservative reconciliation remain unfinished, so no
F pass or completed-round credit is claimed.

## Every-axis status

No final round-6 axis verdict is asserted at this partial checkpoint:

- **Depth:** pending; no new end-to-end culture task or newly admitted
  source-to-system rule is claimed.
- **Coverage:** pending; the twelve reviewed reference surfaces are existing
  entries, not twelve newly verified civilizations.
- **Operability:** no new capability claimed; existing gates/examples are
  unchanged and prior acceptance passes.
- **Freshness:** F remains pending its original parent-evidence threshold
  and acceptance instrument.
- **Calibration:** review debts and raw-versus-parent distinctions are
  recorded, not asserted as a final axis admission.
- **Adjacency:** no lore receipt, permission, canon or scope ruling.

The last admitted six-axis table remains round 5. D2 still has twenty
findings; the fifteen round-5 residual questions remain unresolved.

## SHONEN

- [~] Decision-table/source evidence remains in SKILL and the existing corpus; the new source readings are provisional, with review limits in fragments 14–16 and the pending Gate lesson.
- [~] Existing domain tasks were rerun through the isolated previous-acceptance suite in checkpoint-validation.json; no new round-6 whole-culture success or lore receipt is claimed.
- [~] The checkpoint command runs from the clean export at the work hash above; the distinct original F acceptance command remains unfinished.
- [~] Province boundaries and deviations are disclosed below; author-side assertions only, no non-author verifier, promotion or canon decision.

## Start here in a new session

Read **`reports/round-6/checkpoint.json`** first. Do not re-dispatch round 6:
its sole batch already executed. A brand-new session should consume the
committed files rather than assume old runtime agent handles can be resumed.

Finish this shrinking queue before advancing:

1. Persist at least three parent non-bibliographic source re-fetches.
   Parent's earlier Wisdomlib fetch was not durably recorded; two native
   PDF fetches failed extraction, so those are not completed checks.
2. Reconcile R6-04-A, 05-A, 06-A, 08-A, 08-B, 09-A and 10-A whole-claim
   scope; preserve the raw worker ledgers and record parent decisions apart.
3. Pin 13-A's wildcard archive capture; retain textual school, translation,
   emendation and exact timing options. Correct mediator/source-kind labels
   for university teaching and BMCR reviews. Crossref abstract prose is
   content, not its surrounding metadata, and not unseen full text.
4. Implement the original run-validation.py, run it on the actual/staged
   deliverable, integrate only warranted append-only errata and decision
   rows, judge every axis, and append a final outcome/report erratum in a
   new commit. Never rewrite this checkpoint as if it was a prior pass.
5. Then run **round 7 Flash MAX/16 → rounds 8–9 OpenCode Go DeepSeek v4.1
   Flash/32–64 each → round 10 exact Grok 4.7 xhigh fast/128 AFTER DeepSeek**.
   The operator's later model/provider/order amendments override the older
   stored goal draft. Do not silently substitute a different Grok route.

## Limits and session error

Workers 09 and 11 reported temporary fleet-root writes followed by cleanup;
no such files are shipped, but zero outside writes ever is not independently
established. Raw downloads and duplicate experiments remain ignored rather
than redistributed. No fleet roster/ledger, sibling, world-bible, credential
or provider-configuration changes are committed. No live child task remains.

The separate empty-assistant provider-400 problem was investigated only:
**no CLI source/configuration/binary fix was made or pushed**. The operator
requested Kimi K2.8 Preview as main session model via `/model`; a successful
switch was not performed or verified by this lane. Do not describe a new
session, a model selection or this corpus checkpoint as that bug's fix.

Historical round-2/round-4 rejections and round-4 dispatch-provenance debt
remain. This checkpoint plus its report are not additional training rounds,
and the ten-round goal is not complete. Push equality and clean nonignored
Git state are checked after publication, not assumed by this report.

---

## Final-outcome erratum — round 6 admitted by the author (2026-10-17)

This addendum supersedes the **pending admission/unfinished queue** status
in the checkpoint above, not its historical measurements or source bytes.
The first 142 lines remain unchanged. The checkpoint really was pending at
`104aa54c737d79c5df1382f65d578b61cbf831f2`; its unmodified checker still
reproduces that state in a disposable export of that exact commit.

### Work performed

Finished the original F contract without another swarm: persisted five
parent source re-fetches, reconciled all 24 questions with one main-source
scope rule, pinned the Gobhila capture, corrected the ARTA locator apart
from its raw ledger, and implemented the originally declared acceptance
command. Evidence: `parent-source-spotchecks.json`,
`parent-reconciliation.json`, `run-validation.py`, `validation.json` and
`outcome.json` under `reports/round-6/`.

The original sole batch remains sixteen completed Z.ai GLM-5.3 Flash MAX
workers. There were three actual-output reviewer continuations in the
checkpoint, then one further read-only counting-instrument review by the
same critic identity `agent-487`. That review independently reproduced the
bounded counts and returned **no blocking findings**. It is author-side,
not an independent promotion verifier or another AgentSwarm. Its limits
and nonblocking notes are retained in `outcome.json`.

### Landed changes and work-hash binding

Actual work HEAD at this addendum's writing:
**`b815bf400120c90f422dbe8d15f8ce028078bfd0`**.
Its tree is **`9352a8f7af50446d37a658985bfb3d1a7e9c5324`**, the clean staged
export that passed full acceptance before commit. Author and committer are
`kotodama-shokunin <kotodama@shokunin.local>`.

That commit lands the parent receipts/reconciliation, counting runner and
receipt, outcome record, five SKILL decision rows, two append-only Vedic
and Persian entry errata, README frontier update, six-axis SCORECARD and
appended lesson/LOG evidence. All are tied to LOG entries headed
“round 6 final integration: bounded freshness admitted” and
“Round 6 final instrument review and historical replay”. Historical
ledgers, reviews, old reports, gates and examples are not rewritten.

The critic-reviewed and committed acceptance instrument SHA256 is
`c53f100927b8723bea25eeaa06048ace68fdfa3e763811a64e1104323e535c6e`,
confirmed by hashing the actual Git blob at the work hash. This report
addendum is written after that commit, then committed last without amending
or rebinding any earlier report hash.

### Before → after and actual verification

`python3 reports/round-6/run-validation.py` exits **0**, F=true and
acceptance_checks_passed=true on the work tree and a clean
`git checkout-index` export of the staged deliverable. Exported and live
receipt JSON are equal; no ignored downloads or duplicate experiment trees
are required. Staged and unstaged whitespace checks passed.

- Zero round-6 rows/checks → **24 fixed questions across twelve entries**.
- **Twenty distinct eligible main passages / twenty main URLs across eleven
  entries**; threshold remains at least six passages across four entries.
- **Five parent passage re-fetches / five URLs across four entries**;
  threshold remains at least three parent non-bibliographic checks.
- Raw worker labels remain **24 supported / 18 whole / six partial**.
  Parent dispositions are **nine scoped-support / eleven partial-support /
  four unresolved**, not 24 independent whole-claim confirmations.
- Four tertiary mains and every optional corroboration are excluded from
  F's passage threshold. Museum technical fields are labelled field content;
  the Crossref record contributes actual deposited abstract prose, not
  bibliographic fields or unread full text.
- Nine in-memory count-boundary negative controls pass. They do not certify
  quotation truth or provide a universal scholarship gate.
- **497 checkpoint files byte-identical, six named append-only prefixes
  preserved, two explicitly editable bookkeeping files**. This final model
  is not the checkpoint's earlier 468-file whole-byte-equality measurement.
- Previous round-5 acceptance passes only in a disposable copy: seven gate
  selftests, both round-3 manifests 7/7, craft 10/10 domain and 18/18 CLI
  controls, with **twenty expected D2 findings unchanged**. Original receipts
  are untouched; old craft/battery code hashes still match their pins.
- Inventory remains **179 entries / six partitions 16/16/16/24/13/94**, with
  592 raw marker-bearing lines / 598 raw occurrences, 600 case-insensitive
  and 568 parenthesized occurrences. This is inventory, not a quality score.

### Every-axis verdict

- **Freshness: improved (declared F).** Original 24/≥6/≥4/≥3 contract passes
  by the exact declared command and saved normalized passage-key list.
- **Calibration: improved (unclaimed).** Strict 9/11/4 reconciliation,
  truthful mediators, pinned capture and page-9 locator preserve uncertainty
  and raw records rather than inflate support.
- **Depth: unchanged.** Five bounded source-to-system rows are useful
  constraints, not a new end-to-end miniature-culture demonstration.
- **Coverage: unchanged.** Existing entries rechecked within twelve fixed
  reference surfaces; no all-civilization or all-earlier-history claim.
- **Operability: unchanged.** Prior executable domain behavior is preserved;
  the new round-local receipt instrument is not a new general culture gate.
- **Adjacency: unchanged.** Same province/handoff checks; no lore receipt,
  cultural clearance, canon ruling or promotion.

**Author-side admission: F verifies and no tested axis is harmed.**
No scalar, rank promotion or fleet closure is inferred.

### SHONEN

- [~] Decision tables, error patterns and checklists remain source-linked in SKILL/corpus; five new bounded decision rows cite actual parent readings, with scope in reconciliation.
- [~] Existing domain demonstrations rerun through isolated prior acceptance; no new whole-culture or lore-receipt success, and D2's twenty findings remain visible.
- [~] The declared acceptance command passes on the clean staged work tree without ignored downloads; the committed instrument hash and work HEAD are bound above.
- [~] Province and cross-domain boundaries remain; author-side review only, no non-author promotion verifier and no canon decision.

### Remaining frontier and next round

The fifteen round-5 residuals remain unresolved; round 6 still has eleven
partial and four unresolved questions. Unread monographs, Sanskrit/Kāṇva
witnesses, original title/garment terms and source-specific disputed legs
remain explicitly bounded. Public text does not grant cultural permission.
The worker outside-write deviations, historical round-4 dispatch debt and
the unfixed CLI/provider-400 investigation remain disclosed above.

Next: **round 7 Flash MAX/16 → rounds 8–9 OpenCode Go DeepSeek v4.1
Flash/32–64 each → round 10 exact Grok 4.7 xhigh fast/128 after DeepSeek**.
The later operator amendments override the stored goal draft's old routes
and order. Do not silently substitute a Grok model. The ten-round goal is
still incomplete; integration/report commits do not add round credit.
This addendum must land in its own lane-identity commit before the normal
push; verify remote equality and a clean nonignored tree afterward.
