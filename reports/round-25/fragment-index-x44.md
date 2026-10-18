# R25-X44 — fragment index + conformance

Seat **R25-X44** (scribe: fragment index + conformance) for round 25 (operator:
loop 3 of 3, build round 1 of 4; 64 workers on
`devin/deepseek-v4-1-flash-high` — operator provider test). Axes watched:
**O / operability** (the typed-pipeline gate-input false red; the handoff v3
claim-prose supersession), **D / depth** (the argot-derivation checking leg),
**C / coverage** (`corpus/lessons/README.md` reconciled). Declaration:
`reports/round-25/claims.json` (baseline `e06581b7fc2b50050a336f7f38a7e2baebcc6abc`);
seat allocation: `reports/round-25/targets.json` (O-gate-input 10,
O-v3-supersession 10, D-argot 24, C-lessons 12, X 8 = 64). Lane HEAD at this
index's census: `f74fc94`.

This is the assigned X44 index — an availability read plus a presence/conformance
census. It is **not** a round-admission receipt, not a verdict replay, and not an
independent promotion review. The round's own counting command is
`python3 reports/round-25/run-validation.py`; the round's verdict is
`reports/round-25/validation.json`, which is indexed here, not adjudicated here.
No round validator was executed by this seat; no filed rounds 8–24 artifact was
read as writable, and none was modified.

**Filing note.** This index files at the seat-named path
`reports/round-25/fragment-index-x44.md` (the round-19/round-20 collision lesson,
X28-1 / X24-L1). Seat **R25-D20** files
`reports/round-25/scribe/fragment-ledger.{json,md}`, a read-time census of the
same subtree that calls itself the integration ledger; the paths do not collide,
but the roles overlap. Both are indexed here; neither settles the other, and a
divergence between the two tables is a parent reconciliation item, not a verdict.

## Reading this index

- **Indexed** means the named artifact existed at the census and its size and
  sha256 were read. It does not mean the claim passed, a draft was integrated,
  or a control was executed.
- **Attributed** results belong to their source fragment; a row is an X44
  execution only where it says so.
- **Draft / declared / in-flight** are deliberate distinctions: a landed draft is
  not a landing; a declared threshold is not an achieved outcome; a runner on
  disk is not a green acceptance.
- Owner inference is directory/name based (stated in the table); `unassigned` is
  never guessed. Seat attribution beyond the declaration files is not a launch or
  completion trace.
- Counts carry their command and date; quotations name their location; a missing
  required artifact is named, never inferred.

## Availability (at the census stamp)

- Census: **2026-10-18T17:55:11Z** (command: `python3 -B .scratch/x44/gen-index.py`;
  `__pycache__/`, `*.pyc`, `*.log` excluded; this index file is the self row,
  written after the census, never self-measured). Census count: **66**
  artifacts plus this index.
- **Counting command** `python3 reports/round-25/run-validation.py` — **present**
  at census (60,048 B, sha256 `d19435251dccb738e456c01fe7fb94498c27bae7f70704a96f94ec9324ce35af`).
- **Runner receipt** `reports/round-25/validation.json` — **present** at census
  (107,893 B, sha256 `e887239cb81865dd38b7b19e24e1ae6db9320dad206686eb2459b1124c73b9fd`), `acceptance_checks_passed: True`,
  `failures: []`, claims O/D/C
  `passed: {'C': True, 'D': True, 'O': True}`.
- Marker line for the control: `runner_present_at_census=Y` and `binding_ok_at_census=Y`.
- **Binding check (the round-20 lesson).** The receipt's `runner_sha256` is
  `d19435251dccb738e456c01fe7fb94498c27bae7f70704a96f94ec9324ce35af`; the live `reports/round-25/run-validation.py` hashes
  `d19435251dccb738e456c01fe7fb94498c27bae7f70704a96f94ec9324ce35af` at the census — **the receipt binds to the live runner bytes**,
  so it is not a superseded receipt. (Round 20's receipt bound to a superseded
  revision; this round's does not.) A runner edit after this census invalidates
  the binding and requires a dated refresh.
- **Wave shape.** The wave was live across the census window (first artifact
  `claims.json` 17:23:25Z; the census stamp above). Arrivals by inferred owner
  group are visible in the table; the wave had gone quiescent (no write in the
  240 s before the stamp) when the census was taken. A file arriving after it
  needs a dated refresh, not an inferred worker failure.
- **Protected surface** (rounds 8–24, `git status --porcelain=v1` over
  `reports/round-{8..24}` at the census): **clean** — no modified protected
  artifact. Round 24 left no straggler this time (contrast round 23's
  `reports/round-22/fixes/regression.md`).
- **Fleet root** `/home/vgpnk/Projects/shokunin`: one untracked entry
  (`.scratch/`, gitignored); no tracked modification.
- **In-flight transients (named, not verdicts).** Two readings taken *during*
  the wave are recorded here so they cannot be mistaken for the close state:
  (a) at 17:25Z the derived-packet entry `typed-pipeline-gate.py
  examples/culture-d4/packet.d4.typed.yml` exited **1** with 14/16 legs, eight
  `DERIV-REPLAY` FAILs and six `null` owed slots — the round-24 hazard, live and
  reproduced; (b) at 17:35Z the untyped entry
  `typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` died with
  `NameError: name 'owed_slot' is not defined` (a mid-edit snapshot of the
  in-flight fix). Neither is the close state; the census-state readings below
  supersede both. (c) The receipt itself was **refreshed at the final
  revision**: an earlier reading at 17:48:52Z carried sha8 `f8375af6` / 106,957 B
  and the settled bytes carry sha8 `e887239c` / 107,893 B (mtime 17:50:38Z).
  The refreshed receipt still reads `acceptance_checks_passed: true`,
  `failures: []`, claims O/D/C `passed: true`, and still binds the live runner
  (`runner_sha256` = the live `run-validation.py` digest). This index's own
  control caught that drift before filing, which is the receipt-guard discipline
  the lane's round-20 lesson prescribes.

## Census

Read-time census of `reports/round-25/**` at **2026-10-18T17:55:11Z** (command:
`python3 -B .scratch/x44/gen-index.py`, sha8 digests via `hashlib.sha256`;
see **Index verification** for the reproducible coverage control). Files under
`__pycache__/` and `*.log` are excluded. The wave was in flight at the census;
a file arriving after it needs a dated refresh. Counts are artifact counts, not
worker counts.

| artifact | bytes | sha8 | mtime UTC | inferred owner | conformance state / limit |
|---|---:|---|---|---|---|
| `reports/round-25/adjacency.md` | 19095 | `0d46cc5c` | 17:29:15 | X (scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-25/argot/current-state.md` | 17885 | `6562f115` | 17:32:19 | D (argot-derivation seats) | D fragment (argot-derivation analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-25/argot/delta.md` | 29611 | `c4b6c47b` | 17:33:04 | D (argot-derivation seats) | D fragment (argot-derivation analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-25/argot/execution-1.md` | 5028 | `793400e5` | 17:30:30 | D (argot-derivation seats) | D fragment (argot-derivation analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-25/argot/execution-2.md` | 6458 | `53421b57` | 17:31:20 | D (argot-derivation seats) | D fragment (argot-derivation analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-25/argot/execution-3.md` | 9962 | `a187a3a2` | 17:32:26 | D (argot-derivation seats) | D fragment (argot-derivation analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-25/argot/execution-4.md` | 10776 | `8d6f0c21` | 17:32:21 | D (argot-derivation seats) | D fragment (argot-derivation analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-25/argot/forecast.md` | 9551 | `19b38555` | 17:27:58 | D (argot-derivation seats) | D fragment (argot-derivation analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-25/argot/impl-1.md` | 5164 | `2dc51536` | 17:48:48 | D (argot-derivation seats) | D fragment (argot-derivation analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-25/argot/impl-2.md` | 4217 | `d026172c` | 17:48:54 | D (argot-derivation seats) | D fragment (argot-derivation analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-25/argot/impl-3.md` | 4200 | `2639e010` | 17:48:59 | D (argot-derivation seats) | D fragment (argot-derivation analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-25/argot/impl-4.md` | 4953 | `a0dbd26e` | 17:49:04 | D (argot-derivation seats) | D fragment (argot-derivation analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-25/argot/impl-5.md` | 5631 | `32ed481a` | 17:49:10 | D (argot-derivation seats) | D fragment (argot-derivation analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-25/argot/impl-6.md` | 7361 | `595ebc38` | 17:49:17 | D (argot-derivation seats) | D fragment (argot-derivation analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-25/argot/review-1.md` | 26228 | `3ed7e98d` | 17:37:48 | D (argot-derivation seats) | D fragment (argot-derivation analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-25/argot/review-2.md` | 11836 | `0c115d18` | 17:36:24 | D (argot-derivation seats) | D fragment (argot-derivation analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-25/argot/review-3.md` | 15715 | `20576a05` | 17:37:45 | D (argot-derivation seats) | D fragment (argot-derivation analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-25/audit/c31-lessons-index-audit.md` | 21803 | `f049daa4` | 17:36:39 | auditors (X4x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-25/audit/c31-lessons-index-audit.py` | 19406 | `dc3ee4cc` | 17:34:12 | auditors (X4x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-25/audit/c31-lessons-receipt.json` | 7673 | `24749f3e` | 17:36:26 | auditors (X4x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-25/audit/o18-gate-input-adversarial.md` | 18109 | `d05cec84` | 17:47:31 | auditors (X4x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-25/audit/o18-probe-matrix.sh` | 4212 | `f20fa056` | 17:41:05 | auditors (X4x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-25/audit/o19-supersession-honesty.md` | 11652 | `4d7471fa` | 17:43:57 | auditors (X4x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-25/audit/o20-argot-leg-review.md` | 13469 | `b290eaa6` | 17:46:24 | auditors (X4x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-25/audit/x42-argot-execution-spotcheck.md` | 20515 | `b28074fd` | 17:41:17 | auditors (X4x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-25/audit/x45-lessons-audit.md` | 16848 | `e8162709` | 17:39:14 | auditors (X4x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-25/audit/x45-lessons-pointer-audit.py` | 10244 | `97c2a171` | 17:37:12 | auditors (X4x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-25/audit/x45-lessons-pointer-receipt.json` | 1477 | `6669c3bd` | 17:38:44 | auditors (X4x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-25/audit/x47-argot-negatives-audit.py` | 14478 | `2beaa81e` | 17:28:41 | auditors (X4x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-25/audit/x47-argot-negatives.md` | 15308 | `7c7acca1` | 17:36:38 | auditors (X4x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-25/audit/x48-v3-supersession-audit.py` | 15847 | `3cd3f3c9` | 17:31:33 | auditors (X4x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-25/audit/x48-v3-supersession.md` | 10740 | `5451a892` | 17:39:26 | auditors (X4x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-25/availability.json` | 17021 | `51d62532` | 17:45:15 | X (availability seat) | Availability record; a route/liveness measurement, not round acceptance. |
| `reports/round-25/claims.json` | 2979 | `bde84338` | 17:23:25 | declaration (parent) | Declared thresholds and seat allocation, not achieved outcomes. |
| `reports/round-25/docs/derivation-relation-docs.md` | 21821 | `681cb202` | 17:36:08 | D (argot-derivation seats) | Presence recorded; not independently re-executed here. |
| `reports/round-25/gate-input/design.md` | 21177 | `defa9cfc` | 17:34:38 | O (gate-input seats) | O fragment (gate-input diagnosis/design/impl/verify); attributed evidence; the source edit is outside this subtree. |
| `reports/round-25/gate-input/diagnosis.md` | 16449 | `4055f17b` | 17:34:50 | O (gate-input seats) | O fragment (gate-input diagnosis/design/impl/verify); attributed evidence; the source edit is outside this subtree. |
| `reports/round-25/gate-input/impl.md` | 14978 | `91573573` | 17:37:32 | O (gate-input seats) | O fragment (gate-input diagnosis/design/impl/verify); attributed evidence; the source edit is outside this subtree. |
| `reports/round-25/gate-input/verify.md` | 11167 | `7d3818ce` | 17:36:47 | O (gate-input seats) | O fragment (gate-input diagnosis/design/impl/verify); attributed evidence; the source edit is outside this subtree. |
| `reports/round-25/integration/log-draft.md` | 6546 | `7f01b86b` | 17:36:02 | integration (parent-owned) | NON-CANON integration draft (LOG/SCORECARD); parent-owned landing. |
| `reports/round-25/integration/scorecard-draft.md` | 6373 | `c47b8eb6` | 17:36:22 | integration (parent-owned) | NON-CANON integration draft (LOG/SCORECARD); parent-owned landing. |
| `reports/round-25/lessons/C25-C30.md` | 13685 | `8c5a9f28` | 17:30:11 | C (lessons-index seats) | C fragment (lessons-index census/tool/report); attributed evidence; the landed index is outside this subtree. |
| `reports/round-25/lessons/C35-C36.md` | 12688 | `dae71579` | 17:48:18 | C (lessons-index seats) | C fragment (lessons-index census/tool/report); attributed evidence; the landed index is outside this subtree. |
| `reports/round-25/lessons/census.json` | 33977 | `7e79f7c0` | 17:30:14 | C (lessons-index seats) | C fragment (lessons-index census/tool/report); attributed evidence; the landed index is outside this subtree. |
| `reports/round-25/lessons/lessons-index-census.py` | 20221 | `23723db8` | 17:28:54 | C (lessons-index seats) | C fragment (lessons-index census/tool/report); attributed evidence; the landed index is outside this subtree. |
| `reports/round-25/regression.md` | 18874 | `89df5e2e` | 17:42:16 | O (regression seat) | O regression receipt (clone-isolated sweep); attributed evidence, not independently re-executed here. |
| `reports/round-25/report-draft.md` | 11680 | `e4c7cad0` | 17:43:55 | X (scribe seats) | Scribe draft/evidence record, not authorized final filing. |
| `reports/round-25/rerun.json` | 33345 | `a8c7db58` | 17:43:34 | X (scribe seats) | Scribe draft/evidence record, not authorized final filing. |
| `reports/round-25/rule/skill-draft.md` | 21110 | `75a05a81` | 17:35:56 | rule draft (parent lands) | Rule draft for SKILL.md; landing is the orchestrator's, not this fragment's. |
| `reports/round-25/run-validation.py` | 60048 | `d1943525` | 17:48:00 | acceptance runner/receipt | Executable runner; existence is not a green end-to-end acceptance (the receipt is the verdict). |
| `reports/round-25/scope.md` | 10769 | `6cafe2c2` | 17:28:07 | X (scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-25/scribe/capability-row.md` | 20837 | `03b477e5` | 17:34:22 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-25/scribe/fragment-ledger.json` | 17415 | `10b277c7` | 17:40:52 | X (scribe seats) | NON-CANON read-time census ledger; admits nothing. |
| `reports/round-25/scribe/fragment-ledger.md` | 18883 | `44ab45d8` | 17:40:52 | X (scribe seats) | NON-CANON read-time census ledger; admits nothing. |
| `reports/round-25/scribe/frozen-rows.md` | 16517 | `5f2a9ffd` | 17:37:09 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-25/scribe/x46-gate-input-cold-rerun.md` | 17758 | `726615e0` | 17:38:48 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-25/targets.json` | 217 | `309d9bc1` | 17:23:25 | declaration (parent) | Declared thresholds and seat allocation, not achieved outcomes. |
| `reports/round-25/v3-supersession/build-revision.py` | 17560 | `f362d1f6` | 17:30:10 | O (v3-supersession seats) | O fragment (v3 claim-prose supersession, new revision); attributed evidence; filed rounds 8-24 untouched. |
| `reports/round-25/v3-supersession/declared-in-r4/expected.json` | 2715 | `c2d4eb7a` | 17:31:37 | O (v3-supersession seats) | O fragment (v3 claim-prose supersession, new revision); attributed evidence; filed rounds 8-24 untouched. |
| `reports/round-25/v3-supersession/declared-in-r4/freeze.txt` | 4724 | `6cc4fc2c` | 17:31:54 | O (v3-supersession seats) | O fragment (v3 claim-prose supersession, new revision); attributed evidence; filed rounds 8-24 untouched. |
| `reports/round-25/v3-supersession/declared-in-r4/packet.md` | 109817 | `5f58db4a` | 17:30:13 | O (v3-supersession seats) | O fragment (v3 claim-prose supersession, new revision); attributed evidence; filed rounds 8-24 untouched. |
| `reports/round-25/v3-supersession/evidence/check-receipt.json` | 12113 | `0bf2d586` | 17:38:40 | O (v3-supersession seats) | O fragment (v3 claim-prose supersession, new revision); attributed evidence; filed rounds 8-24 untouched. |
| `reports/round-25/v3-supersession/evidence/selftest-receipt.json` | 6069 | `c685d2c3` | 17:38:43 | O (v3-supersession seats) | O fragment (v3 claim-prose supersession, new revision); attributed evidence; filed rounds 8-24 untouched. |
| `reports/round-25/v3-supersession/evidence.md` | 10043 | `c74ee433` | 17:38:56 | O (v3-supersession seats) | O fragment (v3 claim-prose supersession, new revision); attributed evidence; filed rounds 8-24 untouched. |
| `reports/round-25/v3-supersession/v3-supersession-check.py` | 30104 | `2a20ddbb` | 17:37:02 | O (v3-supersession seats) | O fragment (v3 claim-prose supersession, new revision); attributed evidence; filed rounds 8-24 untouched. |
| `reports/round-25/validation.json` | 107893 | `e887239c` | 17:50:38 | acceptance runner/receipt | Primary receipt; written by the runner. Binding checked in the observations below. |

**Census:** 66 artifacts indexed (this index file is the 67th,
self-indexed without size/sha). Excluded: `__pycache__/` (one file,
`reports/round-25/__pycache__/run-validation.cpython-314.pyc`) and `*.log`
(none present).

## Conformance observations

1. **Declared, not achieved.** Both `claims.json` and `targets.json` are the
   parent's declaration (`state: declared-before-dispatch`); nothing in this
   index converts a declaration into an achieved outcome. The achieved outcome
   lives in `validation.json`, which is the runner's artifact, not this seat's.

2. **O / operability — the gate-input hazard is fixed at the census, measured by
   this seat.** Three entries re-run at the census stamp, all exit 0:
   `typed-pipeline-gate.py` (default source entry) → 16/16 legs;
   `typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → **20/20** legs;
   `typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` → **17/17**
   legs, **zero** `DERIV-REPLAY` lines and **no** `L3-routing-consistency` FAIL.
   The fix is the uncommitted edit to `tools/gates/typed-pipeline-gate.py`
   (`git diff --stat` → 264 insertions, 31 deletions), which adds a `nullish()`
   / `owed_slot()` null-normalizer and an `L2-legacy-source` leg that grades the
   typed packet against the source it *declares*, rather than against the gate's
   own non-byte-faithful rebuild. The leg counts grew because the argot leg
   (observation 3) was bound into the same gate. `--selftest` 19/19. This is
   attributed evidence plus this seat's own re-run; the runner's own
   `gate_input_honesty` block is the formal measurement, and it reads
   `derived_packet` exit 0 / 17 legs / 0 `deriv_replay_lines` / `nullish_routing
   false`, with the teeth controls: tampered expectation → exit 1, corrupted
   packet → exit 2.

3. **D / depth — the argot-derivation leg landed, and the delta is recorded.**
   New untracked files `tools/gates/argot-derivation-gate.py` (36,127 B),
   `tools/gates/fixtures/argot-derivation-gate.yml` + `.expected`, a binding leg
   inside `tools/gates/typed-pipeline-gate.py`, and a frozen generation
   `tools/gates/frozen/round-25/`. Measured by this seat:
   `argot-derivation-gate.py examples/culture-d4/packet.d4.yml` → exit 0,
   `register_scoped=6 derived_pairs=0 claimed_chains=8 borrow_pairs=6
   violations=0`; `--selftest` → **21/21**, exit 0. **The delivered-vs-forecast
   delta is named, not silently dropped** — and the naming is itself contested
   inside the wave: `reports/round-25/argot/delta.md` §1 marks F-1..F-8 and
   A-1..A-11 **NOT DELIVERED** element-by-element (root cause: the round-17 brief
   designed a weigh-court brokerage culture that never shipped), while its own §8
   addendum, re-measured after the leg landed, **narrows** the delta (F-2/F-2b/F-7
   now closed at the mechanism level; F-5 still vacuous because the delivered
   packet declares `derived_pairs=0`; F-6 still not delivered — the gate prints
   `derived_pairs`, not the forecast's `derived_forms`/`derived_ok`). The
   independent review `reports/round-25/audit/o20-argot-leg-review.md` calls the
   delta honest. The receipt marks claim D `passed: true`. This index does not
   resolve the wording; it records that the delta exists, is element-named, and
   that the receipt and the delta fragment describe the same delivered shape at
   different stamps.

4. **O / operability — the v3 supersession landed as a NEW revision.** A new
   directory `reports/round-25/v3-supersession/declared-in-r4/` carries the
   corrected claim prose (five declared line corrections plus a provenance note)
   with its own `expected.json`, `freeze.txt` and a 109,817 B `packet.md`; a
   dedicated checker `v3-supersession-check.py` (30,104 B) and two receipts
   under `v3-supersession/evidence/` verify it. **No filed round-20 or round-22
   byte is edited** — the supersession is a new row, which is the round-23
   disposition pattern. This seat records presence and the new-row shape; the
   prose-level verdict belongs to the checker and the runner.

5. **C / coverage — the lessons index landed outside this subtree.** The
   assigned deliverable `corpus/lessons/README.md` (29,059 B, sha256
   `ec7469dadf87df3e…`) and the round's own lesson `corpus/lessons/round-25.md`
   (38,520 B, sha256 `08f0337e66dbf0c4…`) both live **outside**
   `reports/round-25/` and are therefore **not** in this census, which walks only
   this round's subtree. The subtree carries the C seat's evidence instead:
   `lessons/lessons-index-census.py`, `lessons/census.json`, `lessons/C25-C30.md`,
   `lessons/C35-C36.md`, and the auditors' `audit/c31-lessons-index-audit.{md,py}`
   + receipt, `audit/x45-lessons-audit.md` + `x45-lessons-pointer-{audit.py,receipt.json}`.
   Measured partition at the census: **26 `*.md` files** in `corpus/lessons/`
   (24 `round-*.md` + `supplement-opencode-1.md` + the new `README.md`), plus
   **9** subdirectories. The receipt's claim C leg reads `measured_files: 26`,
   `measured_rows: 26`, formats documented = expected = {gate-keeper,
   fragment-index, plain}, open-question queue 51 rows / 33 owners. The parent
   should integrate the pair (index + evidence), not the receipt alone.

6. **Cross-round coexistence (disclosed).** Seat R25-D20's
   `scribe/fragment-ledger.json` (census `2026-10-18T17:30:50Z`, 17,415 B) and
   its `.md` sibling are a second read-time census of this subtree. They predate
   the last arrivals indexed here (the argot `impl-*.md` at 17:48–17:49Z and
   `validation.json` at 17:48:52Z), so the two tables will differ; that is the
   expected dated-refresh delta, not a contradiction. `scribe/` also carries
   `capability-row.md`, `frozen-rows.md` and `x46-gate-input-cold-rerun.md`.

7. **The parent integrates.** `reports/round-25/integration/log-draft.md` and
   `scorecard-draft.md` are drafts; `reports/round-25/rule/skill-draft.md` is a
   rule draft whose SKILL.md landing is the orchestrator's. Filing, scope,
   integration into `LOG.md`/`SCORECARD.md`, and any final promotion
   verification remain parent responsibilities; in-lane attestations do not
   prove a fresh external inspection.

## Index verification

X44 writes only this file. This stdout-only control re-derives the index
inventory against the live tree (this file excluded), re-hashes every indexed
file, re-checks the runner/receipt availability and binding markers, and runs
in-memory negatives (duplicate row, dropped row, nonexistent path, tampered
sha8) plus Markdown shape checks. No file is written; no validator is executed.
A later-arriving artifact, a drifted digest, or a runner edit after the census
invalidates the reading and requires a dated refresh.

```sh
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
#!/usr/bin/env python3
"""R25-X44 index verification — stdout-only, read-only, in-memory negatives."""
import datetime, hashlib, re
from pathlib import Path

INDEX = Path('reports/round-25/fragment-index-x44.md')
BASE = Path('reports/round-25')
text = INDEX.read_text()
rows = re.findall(r'^\| `(reports/round-25/[^`]+)` \| (\d+) \| `([0-9a-f]{8})`', text, re.M)

def observed():
    return sorted(
        str(p) for p in BASE.rglob('*')
        if p.is_file()
        and '__pycache__' not in p.parts
        and not p.name.endswith(('.pyc', '.log'))
        and p != INDEX
    )

actual = observed()
names = [r[0] for r in rows]

def conforms(pairs):
    ns = [p for p, _, _ in pairs]

    def ok_one(p, s, h):
        f = Path(p)
        if not f.is_file() or f.stat().st_size <= 0:
            return False
        data = f.read_bytes()
        return len(data) == int(s) and hashlib.sha256(data).hexdigest()[:8] == h

    return (len(ns) == len(set(ns)) and set(ns) == set(actual)
            and all(ok_one(*row) for row in pairs))

pairs = [(p, s, h) for p, s, h in rows]
print('observed_at=' + datetime.datetime.now(datetime.timezone.utc).isoformat())
print(f'indexed={len(rows)} observed={len(actual)}')
print('unindexed=' + repr(sorted(set(actual) - set(names))))
print('unavailable=' + repr(sorted(set(names) - set(actual))))
assert conforms(pairs), 'index inventory incomplete, stale, or invalid'

# runner / receipt availability + binding markers
runner = BASE / 'run-validation.py'
receipt = BASE / 'validation.json'
m_r = re.search(r'runner_present_at_census=(\w+)', text)
m_b = re.search(r'binding_ok_at_census=(\w+)', text)
assert m_r and m_b, 'availability/binding marker line missing'
print(f'runner_indexed={m_r.group(1)} runner_now={runner.is_file()}')
assert (m_r.group(1) == 'Y') == runner.is_file(), 'index stale: runner presence drifted'
assert (m_b.group(1) == 'Y') == receipt.is_file(), 'index stale: receipt presence drifted'
if receipt.is_file():
    import json
    rec = json.loads(receipt.read_text())
    live = hashlib.sha256(runner.read_bytes()).hexdigest()
    print(f'receipt_binds_live_runner={rec.get("runner_sha256") == live}')
    assert rec.get('runner_sha256') == live, 'receipt no longer binds the live runner'

# negative controls (in memory only)
assert not conforms(pairs + [pairs[0]]), 'duplicate negative missed'
assert not conforms(pairs[1:]), 'dropped-row negative missed'
assert not conforms(pairs + [('reports/round-25/__X44_nonexistent__.md', 1, '0' * 8)]), 'missing-path negative missed'
tampered = [(p, s, ('00000000' if h != '00000000' else '11111111')) for p, s, h in pairs]
assert not conforms(tampered), 'tampered-sha negative missed'
# shape
assert text.endswith('\n') and '\0' not in text
assert all(line == line.rstrip() for line in text.splitlines()), 'trailing whitespace'
assert len(re.findall(r'^```[^\n]*$', text, re.M)) % 2 == 0, 'unbalanced fences'
print('INDEX_CONTROL=PASS; duplicate/drop/missing/tampered negatives rejected; digests and availability current')
PY
```

Control run **2026-10-18T17:55:15Z** (command: the fenced block above, extracted
verbatim and executed): `indexed=66 observed=66`, `unindexed=[]`,
`unavailable=[]`, `runner_indexed=Y`, `receipt_binds_live_runner=True`,
`INDEX_CONTROL=PASS`, exit 0. An earlier run at 17:50:39Z failed on a drifted
`validation.json` row (the 17:50:38Z receipt refresh, observation 7c); the
census was regenerated at the settled stamp and this reading is the one that
binds the filed bytes. A later arrival, a further receipt refresh, or a runner
edit invalidates this reading and needs a dated refresh.
