# Round-20 gap refresh — the README frontier surveyed against rounds 17–20 (R20-C05..C08)

- round: 20 (operator: loop 2 of 3, build round 4 of 4;
  `reports/round-20/claims.json` claim C). Seat: R20-C05..C08, the C gap-refresh
  seat — four seats share this one path; this file is the seat's single
  deliverable and carries no per-seat fragments.
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  declared baseline revision `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d`, HEAD
  `122086b` ("round-20: declare claims D/O/C"). All commands below ran from the
  repo root on 2026-10-18 (UTC stamps inline); scratch under
  `.scratch/r20-c-gaps/` with `TMPDIR=$PWD/.scratch` exported.
- canon: NON-CANON engineering evidence. This file admits nothing, certifies no
  round, verifies no historical claim, and is not a lore receipt. It closes no
  gate.
- writes: **this file only**. No `corpus/` byte is edited by this seat (the
  in-flight README revision 1.5 belongs to the C01..C04 seat); no commit, no
  push. One honest exception, controlled: running the historical round-5/7/9
  runners rewrote their filed `reports/round-N/validation.json` in place; the
  committed bytes were restored with `git checkout --` and verified clean —
  see §1.5.
- purpose: the C claim asks for a *gap refresh* — survey the still-open gaps the
  README's `## Known gaps (frontier)` names, compare them against what rounds
  17–20 actually landed, close the rows the new content filled (with pointers),
  and hand the README owner a reconciled row set. The README itself is written
  by the C01..C04 seat; §5 below is the merge-ready text for that seat and the
  integrator, not a competing revision.

## 0. Verdict at a glance

Row ids `F1..F11` number the frontier bullets in README order (HEAD `122086b`
version, before the in-flight 1.5 edits).

| row | subject | status at 2026-10-18 | pointer |
|---|---|---|---|
| F1 | round-5 carried-entry residuals (15 unresolved) | **open**; reproduction command stale at HEAD | `reports/round-5/parent-reconciliation.json`, §2.1 |
| F2 | round-6 24 questions (9/11/4) | **open**; reproduction command stale at HEAD | `reports/round-6/parent-reconciliation.json`, §2.2 |
| F3 | per-gate `expected.json` layout pending | **filled** (layout shipped; 17 pins, 9/9 coverage); residue: three baseline roots | §2.3 |
| F4 | header trio missing on most entries | **open** under reading A; now measurable under three named readings | `corpus/knowledge/verification/header-conformance-readings.md`, §2.4 |
| F5 | D2 typed handling / rank rules / scoped reconciliation / parser controls / isolated export | **filled** by rounds 11–20 | `tools/d2-typed-labels.py`, §2.5 |
| F6 | "Round7 acceptance remains pending" | **stale** — closed as failed (ledger closure), D3 surface re-verified in round 9 | `LOG.md` 2026-10-17 ledger closure; `reports/round-9/validation.json`, §2.6 |
| F7 | five round-7 live constraint rechecks (3 scoped / 2 partial) | **open**, counts confirmed | `reports/round-7/parent-reconciliation.json`, §2.7 |
| F8 | round-10 paragraph + round-9 open items | **partial** — items 1/3/4/5 disposed, item 2 open, item 6 environmental | `reports/round-9/report-draft.md` §Open items, §2.8 |
| F9 | strict historical path whitelists in old runners | **open** as a standing rule; now measured four times at HEAD | §2.9 |
| F10 | cultural permission, name screening, lore receipt, independent promotion review | **open** — rounds 17–20 still disclaim all four | §2.10 |
| F11 | round-19's two limits | **partial** — battery limit superseded (9 registered, 9/9 coverage); D4 assembly selftest still absent (exit 2) | §2.11 |
| — | round-20's own content (handoff v3, era-alias wart, README reconcile) | **in flight**; proposed row in §5 | `reports/round-20/claims.json` |

Two claim-vs-tree discrepancies found while refreshing, both carried to the
integrator rather than repaired here:

1. **`reports/round-20/claims.json` claim C states "linguistics 20".** The tree
   measures **19** (`tools/source-audit-inventory.py`, §1.2); the stated vector
   94/20/19/18/29/20 sums to 200, not to the 199 files the same sentence names.
   The in-flight README 1.5 note already records this; the claim text itself
   still carries the un-reproducible number.
2. **The README's own reproduction commands for F1/F2 are stale at HEAD** — see
   §2.1/§2.2. The rows' counts remain filed and correct; what no longer works is
   the instruction to re-derive them with the round-local runner.

## 1. Method and counting commands

All artifacts of this refresh are under `.scratch/r20-c-gaps/` (git-ignored);
digests are sha256 of the captured stdout.

### 1.1 Header readings (F4)

Inline script: opening block = text before the first `## `; reading A = singular
`- source:`; B = `- source:` or `- sources:`; C = either, anywhere in the file;
`verified-at:` and `recheck:` required in the same scope. Run 2026-10-18
12:56:49Z.

```text
reading A: files=199 missing_any=70 parts=[('civilizations',19),('culture-material',18),('linguistics',18),('verification',15)]
reading B: files=199 missing_any=3  parts=[('verification',3)]
reading C: files=199 missing_any=0  parts=[]
```

digest `cf53c5f03cd8aa16ed642d02e978e0b98a18bf68a9fac7f3124e1a6eceffbaa1`
(`.scratch/header-readings3.txt`). The B remainder is exactly the three
digest-pinned placement stragglers —
`verification/{citation-format-and-source-registry,myth-consistency-gate,provenance-audit-ledger-format}.md`
— each pinned once inside
`tools/gates/frozen/provenance-audit/r9-pre/expected.json` (grep count 1 each,
2026-10-18), which is why they stay unrepaired.

### 1.2 Partition counts

```sh
python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge
```

total 199 files; partition counts civilizations 94, culture-material 18,
linguistics 19, myth-symbol 19, synthesis 29, verification 20
(digest `7aab9ca31406be798460a54978dd0b66248cf7932876a08710a01695fe525ad1`).

### 1.3 Gate battery and baselines (F3, F11)

```sh
python3 tools/check-gate-battery.py
```

exit 0; duty 1 `pass 7 / fail 0 / unevaluable 0`, originals preserved
(30 files hashed before/after, 0 modified); duty 2 `baselines_found 17`,
`pinned 17`, `coverage "9/9"`, `gates_uncovered []`. Default roots and their
pin counts: `tools/gates/expected` (4), `tools/gates/frozen` (10),
`reports/round-9/baselines` (3) — the **three roots are all still live**
(round-9 open item 2). digest
`c36ce7b72cfba75f7bcb80998012d92f051255a6dfe8c783a8ecd801e7ecd147`.

### 1.4 Index rows (context for the C01..C04 seat)

```sh
python3 reports/round-19/audit/coverage-audit.py
```

`TOTAL rows=199 disk=199 clean=6/6` — measured while `corpus/README.md` was
already modified in the working tree by the C01..C04 seat (`git diff --stat
corpus/README.md` → 27 insertions, 2 deletions; mtime 2026-10-18 09:59:21
-03:00), so this reading covers the in-flight revision 1.5. digest
`2a5ff83d9458b86f96e2a8ec37f5c729c0eead9c76fc3585d7d98ed3cc4fdf92`.

### 1.5 Historical runners at HEAD (F1, F2, F6, F8, F9)

```sh
python3 reports/round-{5,6,7}/run-validation.py
python3 reports/round-9/run-validation.py
```

| runner | exit | reading at HEAD 2026-10-18 | digest |
|---|---|---|---|
| round 5 | 1 | acceptance false — F: `non-append corpus edit: ('corpus/lessons/supplement-opencode-1/sources/ottoman.json', 'OTT-06')`; O: replay of `tools/gates/frozen/round-3/MANIFEST.tsv` → 7 `could-not-evaluate` rows, all `gate_digest_mismatch` | `c8dc79ec…` |
| round 6 | 1 | acceptance false — `error: "historical file changed: .gitignore"` | `ef767ba7…` |
| round 7 | 1 | acceptance false — `F_passed false` (same filed error, below), `O_passed true`; preservation failures `historical file changed vs BASE: .gitignore` and `historical knowledge totals changed {'files': 199, ...}` | `e7914edd…` |
| round 9 | 1 | `claim F: PASS`, `claim D: PASS`, `claim O: FAIL` — `tools/gates/typed-pipeline-gate.py: no expected.json baseline found under tools/gates/frozen, tools/gates/expected, reports/round-9/baselines` | `f55a6437…` |

None of these reds is a defect of the filed rounds; each is the F9 pattern
(historical runner + later tree). They are reported, not repaired.

**Write hazard (measured, then controlled).** Running the round-5, round-7 and
round-9 runners rewrites their own filed receipt
`reports/round-N/validation.json` **in place**. This seat's runs did so
(`git diff --stat` after the runs: round-5 4 lines, round-7 2 lines, round-9 597
insertions / 67 deletions). The committed bytes were restored immediately with
`git checkout -- reports/round-5/validation.json reports/round-7/validation.json
reports/round-9/validation.json`; the control is `git diff --stat` on those
three paths → empty, and `git status --porcelain` shows no modification on them
(2026-10-18, after restoration). The stdout captures under `.scratch/r20-c-gaps/`
are unaffected by the restore. Readers: run these three runners only inside an
isolated copy, never from the repo root.

## 2. Row-by-row survey

### 2.1 F1 — round-5 residuals

Filed counts confirmed from `reports/round-5/parent-reconciliation.json`
(read 2026-10-18): `parent_counts {"supported": 5, "unresolved": 15,
"contradicted": 0}`, `expected_worker_raw_counts {"rows": 22, "supported": 13,
"unresolved": 8, "contradicted": 1}`, limits "Five scoped support dispositions
are not five universally verified cultural facts". The row stays **open**; what
changes is the reproduction sentence: at HEAD
`python3 reports/round-5/run-validation.py` exits 1 with the two errors in §1.5,
so the counts must be read from the filed receipt and the reconciliation file,
with the drift named. The residual set is untouched by rounds 17–20 (grep of
round-17..19 receipts for the round-5 ids returns nothing; e.g.
`reports/round-19/report-draft.md` §Limits).

### 2.2 F2 — round-6 questions

Filed counts confirmed from `reports/round-6/parent-reconciliation.json`:
`rows: 24` → `{'partial-support': 11, 'scoped-support': 9, 'unresolved': 4}`,
with `older_residuals` = "The fifteen original round-5 residual questions stay
unresolved; this round covers different fixed earlier-reference questions and
does not close them." Row stays **open**; same reproduction caveat (round-6
runner exits 1 with `historical file changed: .gitignore`).

### 2.3 F3 — per-gate `expected.json` layout: **filled**

The layout exists now. `tools/gates/frozen/<gate>/<baseline-id>/expected.json`
is present for all seven legacy gate names (r9-pre and/or r18-post), and
`tools/gates/expected/<gate>/<baseline-id>/expected.json` for four
(`costume-era-consistency-gate` r9-pre, `phonology-sanity-gate` r9-pre, and the
two D4 adapters r19-pre). The battery verifies every pin (§1.3). The in-flight
README 1.5 revision already carries this correction.

Two residues must travel with the closure, not be lost in it:

- **three roots remain live** (`tools/gates/expected`, `tools/gates/frozen`,
  `reports/round-9/baselines`) — round-9 open item 2 is *not* closed; the lane
  standard names a single `tools/gates/frozen/<gate>/<baseline-id>/` home.
- **round-4 outputs still have no frozen manifest** and remain unpinned legacy
  evidence — unchanged by rounds 17–20.

### 2.4 F4 — header trio: **open, but now measurable**

The row's sentence ("Most historical entries lack the fleet's complete
`source`, `verified-at`, `recheck` header") is a reading-A statement. The
round-10 verification entry `header-conformance-readings.md` supplies the
measurement contract (three readings, a count-statement schema, and the
digest-pin constraint that keeps the three B-remainder stragglers deliberately
unrepaired); §1.1 re-measures it on the 199-file tree. The row should cite the
entry and quote a reading id instead of the bare sentence. Nothing in rounds
17–20 changes the underlying placement state: the ten round-19 entries landed
with their trio in the opening block, so B did not grow (3 → 3), while A grew
64 → 70 with the round-10 and round-19 additions.

### 2.5 F5 — D2 typed handling and its companions: **filled**

Every clause of the bullet is now answered, each with a runnable control:

| clause | shipped surface | control (2026-10-18) |
|---|---|---|
| typed native-form / translated-label handling | `examples/culture-d2/typed-labels.d2.yml`, `examples/culture-d2/packet.d2.typed.yml`, `tools/d2-typed-labels.py`, `tools/assemble-d2-typed.py` (r18) | `python3 tools/d2-typed-labels.py --selftest` → `39/39`, exit 0 |
| rank-rule translation | rank adapter inside the same projection (`rank_rules_component 21`, `rank_rules_gate_projected 5`, `rank_rules_normalized 9`, `rank_rules_unresolved_items 13`; `typed-labels.d2.yml:41-44`) | same selftest (`rank adapter block: its own controls pass`) |
| scoped material/era reconciliation | `reconcile_scoped` in `tools/d2-typed-labels.py` (`declared_era_aliases()` at :2319), method entry `corpus/knowledge/synthesis/era-material-scoped-reconciliation.md` (r19) | selftest rows `era: a contract tag is identity`, `era: the declared legacy handle is mapped-confirmed`, `era: a (to-verify) ERX row is mapped-unconfirmed, never promoted` |
| parser/regex negative controls | loader/parser refusals + substitution/template screens in the same tool | selftest rows `loader: P-{UNTERMINATED-FLOW,DUPLICATE-KEY,ANCHOR-TAG,TAB-INDENT,EMPTY,DEPTH-CAP} refused`, `parser: apply_substitutions is one pass, longest key first`, `parser: screen_pattern flags a catastrophic pattern`, `parser: check_template refuses an attribute path` |
| legacy selftests in an isolated export | the gate battery's disposable mirror (`tools/check-gate-battery.py`) | §1.3: originals preserved, 30 files hashed before/after, 0 modified |

The in-flight README 1.5 revision already supersedes this bullet; the row should
survive only as historical record. One honest residue belongs with it: the D2
surface is *NON-CANON design drill* and its green selftest proves routing
mechanics, not any cultural fact (`label-channel-routing-verification.md` §the
four things routing never proves).

### 2.6 F6 — "Round7 acceptance remains pending": **stale, closed as failed**

`reports/round-7/validation.json` exists and reads `acceptance_checks_passed:
false`, `claims.F.passed: false` (`wrong rejection for
duplicate-parent-receipt-does-not-inflate: parent check identity collision`),
`claims.O.passed: true`. The ledger closure of 2026-10-17 (`LOG.md`,
"Operator training regimen + round-7 ledger closure") appended a `closure` row
for round 7 with status `failed` — "terminated at operator session wrap,
acceptance receipt failing per `reports/round-7/validation.json`, no landed
report, never re-dispatched per the round-7 declaration". So acceptance is not
*pending*; it is closed as failed, and the D3 drill itself was later
re-verified independently: `reports/round-9/validation.json` has
`acceptance_checks_passed: true` with `claims.D.passed: true`
(`assembler_check` exit 0 twice, stdout sha identical; `coupling_selftest`
16/16 + 5/5 + 4/4; `frozen_replay.drift_paths []`, `expected_sha256
562b76cb48f14bdb7bcf6362f78d8b5c5506934a10d9f912f6c4a0a554bf90fc`). The row
should be rewritten as history plus those two pointers; the D3 lesson
(`lessons/round-7.md`) is unaffected.

### 2.7 F7 — five round-7 rechecks: **open**

Confirmed from `reports/round-7/parent-reconciliation.json`: `rows: 5` →
`{'scoped-support': 3, 'partial-support': 2}`, and `older_residuals` = "Round5
retains fifteen unresolved original questions; round6 retains eleven partial and
four unresolved questions. New round7 rechecks do not close them." No rounds
17–20 artifact touches these rows; the README wording is accurate as filed.

### 2.8 F8 — round-10 paragraph and the round-9 open items: **partial**

The round-10 paragraph's own statements hold (ten entries, receipts under
`reports/round-10/coverage/`, index re-measured). Its pointer to the round-9
open items is now resolvable item by item (read 2026-10-18,
`reports/round-9/report-draft.md` §Open items):

| item | state |
|---|---|
| 1. D decision (re-freeze `examples/culture-d3/expected.json`) | **closed** — round-9 receipt acceptance true, D passed, replay `drift_paths []` (§2.6) |
| 2. baseline root (three roots → one) | **open** — battery default roots still show all three (§1.3) |
| 3. metadata v09 import | **closed** — the stray `v09-myth.md` was relocated in-lane (`reports/round-10/adjacency.md:147-149`: the parent-dir stray is "gone"; fragment present) and round-12 recorded it as a legitimate later arrival (`reports/round-12/recount/dispositions.md` row 12) |
| 4. commit hygiene | **closed** — `.gitignore` now carries `.scratch/`, `*.log`, `__pycache__/`; `find` for `.scratch-r9f04c`, `freshness/.scratch-v03`, `*.tmp` → empty (2026-10-18) |
| 5. re-run the round-9 runner on the settled tree | **filed then, stale now** — receipt exists; at HEAD the runner reads F PASS / D PASS / O FAIL (§1.5) |
| 6. `/tmp` inode exhaustion | **environment** — carried to the operator, not lane-closable |

The paragraph's sentence "the verifier-independence record rules do not by
themselves dispose of the round-9 open items" can now be replaced by this table
plus the two still-open residues (items 2 and 6). The other sentence — the
header measurement contract "reports an integrator question it does not absorb"
— remains true (`header-conformance-readings.md` §the open integrator question),
and rounds 17–20 add no ruling on it.

### 2.9 F9 — strict historical whitelists: **open, standing rule, now measured**

The row's guidance ("do not edit old scripts or rewrite historical receipts")
is unchanged. This refresh supplies four concrete instances at HEAD: round-5
(non-append corpus edit + 7 digest mismatches), round-6 (`.gitignore`), round-7
(same plus inventory totals), round-9 (O leg: missing `typed-pipeline-gate`
baseline under the three roots). All four are the expected old-runner/later-tree
collision; none is repaired here. The row could carry one sentence naming that
the collision now has four measured instances, so a reader does not mistake a
red old runner for a regression.

### 2.10 F10 — outside-evidence items: **open**

Cultural permission, real-language name screening, a lore receipt and
independent promotion review remain outside the evidence. Rounds 17–20 disclaim
all four in their receipts rather than supply them (e.g.
`reports/round-17/report-draft.md:13`; `reports/round-17/reviews/review-1..5.md`
each "NON-CANON engineering review … not … a lore receipt";
`reports/round-19/report-draft.md` §Limits). Unchanged wording is correct.

### 2.11 F11 — round-19's two limits: **one superseded, one open**

- "the D4 family is outside the battery's seven-name constant" — **superseded
  for coverage**. `tools/check-gate-battery.py` now defines `GATE_NAMES` (7) +
  `D4_GATE_NAMES` (2) = `REGISTERED_GATE_NAMES` (9) and the default run reads
  `coverage "9/9"`, `gates_uncovered []` (§1.3). The precise surviving residue:
  the two D4 adapters are "registered for duty-2 coverage only"
  (`tools/check-gate-battery.py:125-134`) — the battery verifies their
  baselines and pins, it does **not** run their selftests.
- "`tools/gates/d4-assembly-check-gate.py` ships no `--selftest`" — **still
  open**, re-measured 2026-10-18: `python3 tools/gates/d4-assembly-check-gate.py
  --selftest` → exit 2, `assembly error: [Errno 2] No such file or directory:
  '--selftest'`. Its sibling `d4-typed-labels-check-gate.py --selftest` → 39/39,
  exit 0.

## 3. Gaps the rounds-17–20 content actually filled (the close list)

1. **Per-gate `expected.json` layout (F3)** — filled by the round-18 freeze
   work and the round-19 baselines; pointer: `tools/gates/frozen/`,
   `tools/gates/expected/`, and the battery run in §1.3.
2. **D2 typed native-form/translated-label handling (F5)** — filled by rounds
   11/18; pointers: `examples/culture-d2/typed-labels.d2.yml`,
   `examples/culture-d2/packet.d2.typed.yml`, `tools/d2-typed-labels.py`,
   `tools/assemble-d2-typed.py`.
3. **Rank-rule translation (F5)** — filled; pointer: the rank counters and
   adapter controls in `typed-labels.d2.yml` / the tool's selftest.
4. **Scoped material/era reconciliation (F5)** — filled; pointers:
   `reconcile_scoped` in `tools/d2-typed-labels.py`, method entry
   `corpus/knowledge/synthesis/era-material-scoped-reconciliation.md`, routing
   entries `typed-label-routing-workflow.md` and
   `label-channel-routing-verification.md` (both r19).
5. **Parser/regex negative controls (F5)** — filled; pointer: the loader/parser
   selftest rows (§2.5).
6. **Legacy selftests in an isolated export (F5)** — filled; pointer: the
   battery's disposable mirror with the originals-preserved measurement (§1.3).
7. **Gate coverage (F5/F11)** — filled for coverage; pointer: nine registered
   gates, 9/9 default coverage (§1.3), with the duty-2-only caveat.
8. **Round-7 acceptance "pending" (F6)** — closed as failed; pointers:
   `reports/round-7/validation.json`, `LOG.md` 2026-10-17 ledger closure, and
   the round-9 D re-verification.
9. **Round-9 open items 1, 3, 4 (F8)** — disposed with pointers; item 5 is
   filed-but-stale at HEAD.
10. **Round-19's battery-constant limit (F11)** — superseded; pointer: §1.3.

## 4. Still-open rows (the refreshed frontier, stated once)

- Rounds 5/6/7 residual questions (F1, F2, F7) — counts as filed; reproduction
  commands stale at HEAD (§1.5).
- Header trio under reading A (F4) — 70/199; B 3/199 (digest-pinned); C 0/199.
- Three baseline roots and the unpinned round-4 outputs (F3 residue).
- Round-9 open items 2 (single baseline root) and 6 (environment) (F8).
- Strict historical whitelists as a standing rule (F9), four measured instances.
- Cultural permission, name screening, lore receipt, independent promotion
  review (F10).
- `d4-assembly-check-gate.py` has no `--selftest`; the battery runs no D4
  selftest (F11).
- The fleet header-text ruling (the integrator question
  `header-conformance-readings.md` reports and does not absorb).
- Round-20's own claims (D handoff v3, O era-alias wart) — not yet landed at
  this measurement; the frontier must not claim them closed before their
  receipts exist.

## 5. Merge-ready frontier text for the README owner (C01..C04 / integrator)

The in-flight revision 1.5 has already corrected F3 and F5; the block below is
what remains, written to merge into that revision (not to replace it). It
carries this file as the pointer for every refreshed count.

```text
- Round 5's fifteen whole-claim residuals and round 6's nine scoped / eleven
  partial / four unresolved dispositions and round 7's three scoped / two
  partial rechecks remain open. The filed receipts stay authoritative
  (`reports/round-{5,6,7}/parent-reconciliation.json`); the round-local
  reproduction commands no longer run clean on later trees — measured
  2026-10-18 at HEAD: round-5 runner exit 1 (non-append corpus edit;
  seven `gate_digest_mismatch` rows in the round-3 manifest replay), round-6
  runner exit 1 (`historical file changed: .gitignore`), round-7 runner exit 1
  (same, plus inventory-total drift). Read counts from the receipts and name
  the drift; do not edit the old runners. Survey and digests:
  `reports/round-20/readme/gaps.md` §1.5.
- The header trio remains open under the strict reading: re-measured
  2026-10-18 over 199 entries, reading A = 70 missing, reading B = 3 (the three
  digest-pinned placement stragglers in
  `tools/gates/frozen/provenance-audit/r9-pre/expected.json`), reading C = 0.
  Quote a reading id from
  `corpus/knowledge/verification/header-conformance-readings.md` with any
  count; the fleet-text ruling stays with the integrator.
- The per-gate `expected.json` layout has shipped (seventeen pins across
  `tools/gates/expected/`, `tools/gates/frozen/`,
  `reports/round-9/baselines/`; battery coverage 9/9, exit 0). Two residues
  remain: three baseline roots are still in use (round-9 open item 2, lane
  standard names one), and the round-4 outputs still have no frozen manifest.
- Round 7 is closed as failed in the ledger (2026-10-17 closure row; receipt
  `reports/round-7/validation.json` failing), not pending; the D3 drill was
  re-verified independently in round 9 (`reports/round-9/validation.json`,
  D passed, replay `drift_paths []`).
- Round 9's open items are disposed except two: item 2 (single baseline root)
  stays open, item 6 (`/tmp` inode exhaustion) is environmental. Items 1, 3 and
  4 are closed with pointers in `reports/round-20/readme/gaps.md` §2.8; item 5's
  runner is filed but stale at HEAD.
- The battery registers nine gates and reads coverage 9/9 by default, so the
  D4 family is no longer outside its surface for coverage — only for selftest
  execution: the two D4 adapters are registered for duty-2 (baseline/pin)
  coverage, and `tools/gates/d4-assembly-check-gate.py` still ships no
  `--selftest` (measured `--selftest` → exit 2, 2026-10-18).
- Round 20 lands the handoff e2e v3 exercise (D4 artifacts + uncertainty
  claims in the packet path), the per-family era-alias resolution closing the
  round-19 projector wart, and this README reconciliation; receipts in
  `reports/round-20/`. Non-canon examples and passing structural gates do not
  certify historical truth.
```

## 6. Limits

- This file measures; it admits nothing and certifies no round, no gate, no
  entry and no source. Every reading is bound to the tree revision and stamp
  named with it; the in-flight README revision 1.5 means the working tree is
  dirty by construction and every index reading covers that dirty state.
- The round-20 D and O claims are **not** assessed here beyond noting they are
  in flight; their closure belongs to their own receipts and the round's
  acceptance runner (`python3 reports/round-20/run-validation.py`).
- The claim-C partition vector in `reports/round-20/claims.json` (linguistics
  20) is not reproducible from the tree (19); the discrepancy is reported to
  the integrator, not absorbed.
- `.scratch/r20-c-gaps/` artifacts are git-ignored scratch; the digests quoted
  here are of captured stdout at the stamps given, and re-running later on a
  moved tree will not reproduce them.
- Operational caveat for the integrator: the round-5/7/9 runners write their
  filed `reports/round-N/validation.json` in place. This seat ran them from the
  repo root, detected the modification, and restored the committed bytes with
  `git checkout --` (control in §1.5); a later seat running them again should
  work in an isolated copy.
- Two in-flight working-tree edits are **not** this seat's and were left
  untouched (observed at the final check 2026-10-18: `corpus/README.md` for the
  C01..C04 seat; `tools/d2-typed-labels.py` and
  `examples/culture-d4/typed-labels.d4.yml` for the O-claim seat).
