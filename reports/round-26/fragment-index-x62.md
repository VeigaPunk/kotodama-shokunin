# R26-X62 — fragment index + conformance

Seat **R26-X62** (scribe: fragment index + conformance) for round 26 (operator:
loop 3 of 3, build round 2 of 4; 64 workers on
`devin/deepseek-v4-1-flash-high`). Axes watched: **D / depth** (the register
stratum landing in D4), **O / operability** (the three round-25 remainders),
**C / coverage** (the open-question queue dispositioned). Declaration:
`reports/round-26/claims.json` (baseline
`fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`); seat allocation:
`reports/round-26/targets.json` (D-register 28, O-remainders 12, C-openq 14,
X 10 = 64). Lane HEAD at this index's census: `1ad491a`.

This is the assigned X62 index — an availability read plus a presence/conformance
census. It is **not** a round-admission receipt, not a verdict replay, and not an
independent promotion review. The round's own counting command is
`python3 reports/round-26/run-validation.py`; the round's verdict is
`reports/round-26/validation.json`, which is indexed here, not adjudicated here.
No round validator was executed by this seat; no filed rounds 8–25 artifact was
read as writable, and none was modified.

**Filing note.** This index files at the seat-named path
`reports/round-26/fragment-index-x62.md`. Seat **R26-C54** files
`reports/round-26/fragment-index-x54.md` (36,684 B), a second index of the same
subtree at its own stamp; seat **R26-X56** files
`reports/round-26/scribe/fragment-ledger.{json,md}`, a read-time census that
calls itself the integration ledger. The three paths do not collide, but the
roles overlap. All are indexed here; none settles the others, and a divergence
between the tables is a parent reconciliation item, not a verdict.

## Reading this index

- **Indexed** means the named artifact existed at the census and its size and
  sha256 were read. It does not mean the claim passed, a draft was integrated,
  or a control was executed.
- **Attributed** results belong to their source fragment; a row is an X62
  execution only where it says so.
- **Draft / declared / in-flight** are deliberate distinctions: a landed draft is
  not a landing; a declared threshold is not an achieved outcome; a runner on
  disk is not a green acceptance.
- Owner inference is directory/name based (stated in the table); `unassigned` is
  never guessed — at this census **no row is `unassigned`**. Seat attribution
  beyond the declaration files is not a launch or completion trace.
- Counts carry their command and date; quotations name their location; a missing
  required artifact is named, never inferred.

## Availability (at the census stamp)

- Census: **2026-10-18T18:43:57Z** (command: `python3 -B .scratch/x62/gen-index.py`;
  `__pycache__/`, `*.pyc`, `*.log` excluded; this index file is the self row,
  written after the census, never self-measured). Census count: **93**
  artifacts plus this index.
- **Counting command** `python3 reports/round-26/run-validation.py` — **present**
  at census (99,165 B, sha256 `4d79d0488f895fc455f0cb3f8db98e8e929920b92f0bd953a718648c1b2723ee`).
- **Runner receipt** `reports/round-26/validation.json` — **present** at census
  (150,611 B, sha256 `d251d37c…`), `measured_at_utc: 2026-10-18T18:38:16+00:00`,
  **`acceptance_checks_passed: False`**, claims
  `passed: {'C': True, 'D': True, 'O': False}`, three O failures (below).
- Marker line for the control: `runner_present_at_census=Y` and
  `binding_ok_at_census=Y`.
- **Binding check (the round-20 lesson).** The receipt's `runner_sha256` is
  `4d79d0488f895fc455f0cb3f8db98e8e929920b92f0bd953a718648c1b2723ee`; the live
  `reports/round-26/run-validation.py` hashes the same at the census — **the
  receipt binds to the live runner bytes**, so it is not a superseded receipt.
  A runner edit after this census invalidates the binding and requires a dated
  refresh.
- **Wave shape.** The wave was live across the census window (first artifact
  `claims.json` 17:59:43Z; the census stamp above; the last write before the
  stamp was `validation.json` at 18:38:16Z). A quiescence probe (30 s poll, 5
  consecutive no-change polls) read **QUIESCENT at 18:42:59Z**; the census was
  taken at 18:43:57Z and re-taken at the same count. A file arriving after it
  needs a dated refresh, not an inferred worker failure.
- **Protected surface** (rounds 8–25, `git status --porcelain=v1` over
  `reports/round-{8..25}` at the census): **clean** — no modified protected
  artifact. The runner's own protected-path leg agrees: **1,328 paths,
  `differences: []`**.
- **In-flight transients (named, not verdicts).** The receipt was red at earlier
  stamps and its failure set moved during the wave — 12 failures at 18:19Z
  (including a `D4L-ARGOT-DERV` control miss and eight regression commands), 2 at
  18:22Z, 3 at 18:38Z. The census-state reading above supersedes them all; the
  earlier readings are recorded here so they cannot be mistaken for the close
  state. This is the receipt-guard discipline the lane's round-20 lesson
  prescribes: **a moving receipt is a dated reading, not a verdict**.

## Census

Read-time census of `reports/round-26/**` at **2026-10-18T18:43:57Z** (command:
`python3 -B .scratch/x62/gen-index.py`, sha8 digests via `hashlib.sha256`; the
table below is that command's stdout verbatim; see **Index verification** for the
reproducible coverage control). Files under `__pycache__/` and `*.log` are
excluded. Counts are artifact counts, not worker counts.

| artifact | bytes | sha8 | mtime UTC | inferred owner | conformance state / limit |
|---|---:|---|---|---|---|
| `reports/round-26/adjacency.md` | 24353 | `b3da3afa` | 18:10:32 | X (scribe seats) | X scribe fragment (adjacency survey); attributed evidence. |
| `reports/round-26/argot/D21-adversarial-replay.md` | 14903 | `77fa1e8f` | 18:08:41 | D (register-stratum seats) | D fragment (register-stratum argot replay/forecast closure); attributed evidence, not independently re-executed here. |
| `reports/round-26/argot/D22-label-typing-crosscheck.md` | 12308 | `1328ba0a` | 18:08:56 | D (register-stratum seats) | D fragment (register-stratum argot replay/forecast closure); attributed evidence, not independently re-executed here. |
| `reports/round-26/argot/D23-overmatch.md` | 11191 | `7d31da7d` | 18:07:23 | D (register-stratum seats) | D fragment (register-stratum argot replay/forecast closure); attributed evidence, not independently re-executed here. |
| `reports/round-26/argot/D24-forecast-closure.md` | 12849 | `28cfa555` | 18:09:00 | D (register-stratum seats) | D fragment (register-stratum argot replay/forecast closure); attributed evidence, not independently re-executed here. |
| `reports/round-26/audit/o39-o40-remainder-fixes-adversarial.md` | 24767 | `149bbd3c` | 18:38:36 | auditors (X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-26/audit/x60-register-derivation-spotcheck.md` | 27096 | `71745325` | 18:11:48 | auditors (X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-26/audit/x60-register-derivation-spotcheck.py` | 24203 | `db22fb13` | 18:10:47 | auditors (X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-26/audit/x63-lessons-audit.md` | 16876 | `ed933058` | 18:07:04 | auditors (X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-26/audit/x63-lessons-audit.py` | 22851 | `33e27e78` | 18:05:27 | auditors (X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-26/audit/x63-lessons-receipt.json` | 4912 | `d90aebc2` | 18:06:53 | auditors (X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-26/availability.json` | 23057 | `7e23f33d` | 18:26:02 | X (availability seat) | Availability record; a route/liveness measurement, not round acceptance. |
| `reports/round-26/claims.json` | 2383 | `363498ed` | 17:59:43 | declaration (parent) | Declared thresholds and seat allocation, not achieved outcomes. |
| `reports/round-26/fragment-index-x54.md` | 36684 | `7a9342a5` | 18:35:08 | X (scribe seats) | X scribe fragment (round-root index by a second seat); attributed evidence; the two indexes do not settle each other. |
| `reports/round-26/gate-tests/D17-D20-teeth.md` | 3563 | `b92b8081` | 18:22:59 | D (register-stratum gate-test seats) | D fragment (register gate fixtures/receipt/freeze); attributed evidence, not independently re-executed here. |
| `reports/round-26/gate-tests/D17-typed-gate.md` | 6640 | `3c835aa3` | 18:25:24 | D (register-stratum gate-test seats) | D fragment (register gate fixtures/receipt/freeze); attributed evidence, not independently re-executed here. |
| `reports/round-26/gate-tests/D18-negatives.md` | 6505 | `d2bbe8da` | 18:22:57 | D (register-stratum gate-test seats) | D fragment (register gate fixtures/receipt/freeze); attributed evidence, not independently re-executed here. |
| `reports/round-26/gate-tests/D19-determinism.md` | 3770 | `5b462bef` | 18:22:53 | D (register-stratum gate-test seats) | D fragment (register gate fixtures/receipt/freeze); attributed evidence, not independently re-executed here. |
| `reports/round-26/gate-tests/D20-replay-frozen.md` | 7212 | `50f219e7` | 18:22:49 | D (register-stratum gate-test seats) | D fragment (register gate fixtures/receipt/freeze); attributed evidence, not independently re-executed here. |
| `reports/round-26/gate-tests/fixtures/n1-maximal-coda.yml` | 539 | `460cae84` | 18:05:57 | D (register-stratum gate-test seats) | D fragment (register gate fixtures/receipt/freeze); attributed evidence, not independently re-executed here. |
| `reports/round-26/gate-tests/fixtures/n2-rule-mismatch.yml` | 485 | `ef2ad71b` | 18:05:57 | D (register-stratum gate-test seats) | D fragment (register gate fixtures/receipt/freeze); attributed evidence, not independently re-executed here. |
| `reports/round-26/gate-tests/fixtures/n3-positive-control.yml` | 553 | `92e14150` | 18:05:57 | D (register-stratum gate-test seats) | D fragment (register gate fixtures/receipt/freeze); attributed evidence, not independently re-executed here. |
| `reports/round-26/gate-tests/fixtures/n4-unknown-rule.yml` | 350 | `77b31d15` | 18:05:57 | D (register-stratum gate-test seats) | D fragment (register gate fixtures/receipt/freeze); attributed evidence, not independently re-executed here. |
| `reports/round-26/gate-tests/fixtures/n5-borrow-mismatch.yml` | 339 | `04f54be6` | 18:05:57 | D (register-stratum gate-test seats) | D fragment (register gate fixtures/receipt/freeze); attributed evidence, not independently re-executed here. |
| `reports/round-26/gate-tests/fixtures/n6-coverage-hold.yml` | 408 | `5b455472` | 18:05:57 | D (register-stratum gate-test seats) | D fragment (register gate fixtures/receipt/freeze); attributed evidence, not independently re-executed here. |
| `reports/round-26/gate-tests/fixtures/n7-malformed.yml` | 46 | `c19d69c0` | 18:05:57 | D (register-stratum gate-test seats) | D fragment (register gate fixtures/receipt/freeze); attributed evidence, not independently re-executed here. |
| `reports/round-26/gate-tests/fixtures/n8-lengthen-mismatch.yml` | 771 | `d5a0f128` | 18:12:10 | D (register-stratum gate-test seats) | D fragment (register gate fixtures/receipt/freeze); attributed evidence, not independently re-executed here. |
| `reports/round-26/gate-tests/freeze.py` | 10446 | `3614fa51` | 18:23:49 | D (register-stratum gate-test seats) | D fragment (register gate fixtures/receipt/freeze); attributed evidence, not independently re-executed here. |
| `reports/round-26/gate-tests/receipt.json` | 56267 | `1e630436` | 18:25:57 | D (register-stratum gate-test seats) | D fragment (register gate fixtures/receipt/freeze); attributed evidence, not independently re-executed here. |
| `reports/round-26/gate-tests/run-gate-tests.py` | 31393 | `112181d9` | 18:23:59 | D (register-stratum gate-test seats) | D fragment (register gate fixtures/receipt/freeze); attributed evidence, not independently re-executed here. |
| `reports/round-26/lessons/C51-C52.md` | 13179 | `fb916d39` | 18:24:19 | C (lessons-entry / index seats) | C fragment (lessons-entry / index census); attributed evidence; the landed index is outside this subtree. |
| `reports/round-26/lessons/C53.md` | 24626 | `2f46520a` | 18:34:57 | C (lessons-entry / index seats) | C fragment (lessons-entry / index census); attributed evidence; the landed index is outside this subtree. |
| `reports/round-26/lessons/c51-revision-audit.py` | 15080 | `d0b6d1b3` | 18:22:10 | C (lessons-entry / index seats) | C fragment (lessons-entry / index census); attributed evidence; the landed index is outside this subtree. |
| `reports/round-26/lessons/c51-revision-receipt.json` | 1874 | `1eaab903` | 18:24:06 | C (lessons-entry / index seats) | C fragment (lessons-entry / index census); attributed evidence; the landed index is outside this subtree. |
| `reports/round-26/lessons/c51-revision-selftest.json` | 1685 | `82292aa3` | 18:24:06 | C (lessons-entry / index seats) | C fragment (lessons-entry / index census); attributed evidence; the landed index is outside this subtree. |
| `reports/round-26/lessons/r26-census.py` | 8670 | `cd64a81e` | 18:30:24 | C (lessons-entry / index seats) | C fragment (lessons-entry / index census); attributed evidence; the landed index is outside this subtree. |
| `reports/round-26/open-questions/C41.md` | 13930 | `70c80d11` | 18:11:01 | C (open-question seats) | C fragment (open-question disposition); attributed evidence; the lessons README revision lands outside this subtree. |
| `reports/round-26/open-questions/C42.md` | 6417 | `2cbbfc89` | 18:09:03 | C (open-question seats) | C fragment (open-question disposition); attributed evidence; the lessons README revision lands outside this subtree. |
| `reports/round-26/open-questions/C43.md` | 9349 | `ad598518` | 18:09:03 | C (open-question seats) | C fragment (open-question disposition); attributed evidence; the lessons README revision lands outside this subtree. |
| `reports/round-26/open-questions/C44.md` | 8363 | `33c4e3db` | 18:11:37 | C (open-question seats) | C fragment (open-question disposition); attributed evidence; the lessons README revision lands outside this subtree. |
| `reports/round-26/open-questions/C45.md` | 16785 | `72f60533` | 18:11:09 | C (open-question seats) | C fragment (open-question disposition); attributed evidence; the lessons README revision lands outside this subtree. |
| `reports/round-26/open-questions/C46.md` | 7472 | `eb1adc51` | 18:10:47 | C (open-question seats) | C fragment (open-question disposition); attributed evidence; the lessons README revision lands outside this subtree. |
| `reports/round-26/open-questions/audit-dispositions.py` | 24660 | `1fdd6607` | 18:21:22 | C (open-question seats) | C fragment (open-question disposition); attributed evidence; the lessons README revision lands outside this subtree. |
| `reports/round-26/open-questions/audit.json` | 45017 | `558a5b67` | 18:23:42 | C (open-question seats) | C fragment (open-question disposition); attributed evidence; the lessons README revision lands outside this subtree. |
| `reports/round-26/open-questions/audit.md` | 3780 | `c1e0eea5` | 18:23:42 | C (open-question seats) | C fragment (open-question disposition); attributed evidence; the lessons README revision lands outside this subtree. |
| `reports/round-26/open-questions/build-dispositions.py` | 45530 | `f833cedd` | 18:17:51 | C (open-question seats) | C fragment (open-question disposition); attributed evidence; the lessons README revision lands outside this subtree. |
| `reports/round-26/open-questions/dispositions.json` | 95421 | `4071dbf9` | 18:23:43 | C (open-question seats) | C fragment (open-question disposition); attributed evidence; the lessons README revision lands outside this subtree. |
| `reports/round-26/open-questions/dispositions.md` | 9468 | `5af233b9` | 18:23:43 | C (open-question seats) | C fragment (open-question disposition); attributed evidence; the lessons README revision lands outside this subtree. |
| `reports/round-26/open-questions/verify-dispositions.py` | 7179 | `2ea881b3` | 18:07:54 | C (open-question seats) | C fragment (open-question disposition); attributed evidence; the lessons README revision lands outside this subtree. |
| `reports/round-26/open-questions/verify.json` | 765 | `9a7c76de` | 18:21:25 | C (open-question seats) | C fragment (open-question disposition); attributed evidence; the lessons README revision lands outside this subtree. |
| `reports/round-26/register/design.md` | 14454 | `27d23fa6` | 18:10:37 | D (register-stratum seats) | D fragment (register-stratum analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/execution-1.md` | 10155 | `42aaa818` | 18:16:08 | D (register-stratum seats) | D fragment (register-stratum analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/execution-2.md` | 6726 | `87bc9d94` | 18:13:41 | D (register-stratum seats) | D fragment (register-stratum analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/execution-3.md` | 8368 | `4ccbb4ab` | 18:13:51 | D (register-stratum seats) | D fragment (register-stratum analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/execution-4.md` | 8801 | `cf361a8b` | 18:14:04 | D (register-stratum seats) | D fragment (register-stratum analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/forms.md` | 10031 | `06635a1c` | 18:10:37 | D (register-stratum seats) | D fragment (register-stratum analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/impl.md` | 16553 | `180a60b2` | 18:27:21 | D (register-stratum seats) | D fragment (register-stratum analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/repin.json` | 6986 | `45156429` | 18:30:00 | D (register-stratum seats) | D fragment (register-stratum analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/review.md` | 13537 | `0082f08b` | 18:10:29 | D (register-stratum seats) | D fragment (register-stratum analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/rules.md` | 9350 | `535cf7a9` | 18:10:29 | D (register-stratum seats) | D fragment (register-stratum analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/v3-baseline-r26/expected.json` | 10856 | `581f1a8d` | 18:26:36 | D (register-stratum seats) | D fragment (register-stratum analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/v3-baseline-r26/freeze.txt` | 521 | `7060579e` | 18:26:36 | D (register-stratum seats) | D fragment (register-stratum analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/v3-baseline-r26/packet.md` | 105582 | `69ce3877` | 18:26:36 | D (register-stratum seats) | D fragment (register-stratum analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/v3-baseline-r26/twin.json` | 103370 | `b849e2f9` | 18:26:36 | D (register-stratum seats) | D fragment (register-stratum analysis/impl); attributed evidence, not independently re-executed here. |
| `reports/round-26/remainders/pin-repoint-check.py` | 12165 | `5674a6b3` | 18:06:54 | O (remainder-disposition seats) | O fragment (round-25 remainder disposition); attributed evidence; the source edit is outside this subtree. |
| `reports/round-26/remainders/pin-repoint-receipt.json` | 4722 | `406b764e` | 18:08:57 | O (remainder-disposition seats) | O fragment (round-25 remainder disposition); attributed evidence; the source edit is outside this subtree. |
| `reports/round-26/remainders/pins.json` | 6887 | `cae128ab` | 18:08:34 | O (remainder-disposition seats) | O fragment (round-25 remainder disposition); attributed evidence; the source edit is outside this subtree. |
| `reports/round-26/remainders/pins.md` | 8109 | `fcb6e1fc` | 18:08:45 | O (remainder-disposition seats) | O fragment (round-25 remainder disposition); attributed evidence; the source edit is outside this subtree. |
| `reports/round-26/remainders/r4-twin/build-twin.py` | 18739 | `20a670e2` | 18:26:06 | O (remainder-disposition seats) | O fragment (round-25 remainder disposition); attributed evidence; the source edit is outside this subtree. |
| `reports/round-26/remainders/r4-twin/expected.json` | 1912 | `d02a9f2c` | 18:14:27 | O (remainder-disposition seats) | O fragment (round-25 remainder disposition); attributed evidence; the source edit is outside this subtree. |
| `reports/round-26/remainders/r4-twin/freeze.txt` | 4439 | `df772339` | 18:36:48 | O (remainder-disposition seats) | O fragment (round-25 remainder disposition); attributed evidence; the source edit is outside this subtree. |
| `reports/round-26/remainders/r4-twin/twin.json` | 103975 | `1874efbc` | 18:26:44 | O (remainder-disposition seats) | O fragment (round-25 remainder disposition); attributed evidence; the source edit is outside this subtree. |
| `reports/round-26/remainders/r4-twin/verify-twin.py` | 20274 | `10cfa07d` | 18:29:57 | O (remainder-disposition seats) | O fragment (round-25 remainder disposition); attributed evidence; the source edit is outside this subtree. |
| `reports/round-26/remainders/r4-twin.md` | 10685 | `466d5fe3` | 18:37:00 | O (remainder-disposition seats) | O fragment (round-25 remainder disposition); attributed evidence; the source edit is outside this subtree. |
| `reports/round-26/remainders/v2-successor-r26/expected.json` | 4435 | `f695b910` | 18:04:35 | O (remainder-disposition seats) | O fragment (round-25 remainder disposition); attributed evidence; the source edit is outside this subtree. |
| `reports/round-26/remainders/v3-baseline-r26/expected.json` | 10856 | `4879e760` | 18:04:39 | O (remainder-disposition seats) | O fragment (round-25 remainder disposition); attributed evidence; the source edit is outside this subtree. |
| `reports/round-26/remainders/v3-baseline-r26/freeze.txt` | 521 | `adad86ab` | 18:04:39 | O (remainder-disposition seats) | O fragment (round-25 remainder disposition); attributed evidence; the source edit is outside this subtree. |
| `reports/round-26/remainders/v3-baseline-r26/packet.md` | 105582 | `a97a0f0a` | 18:04:39 | O (remainder-disposition seats) | O fragment (round-25 remainder disposition); attributed evidence; the source edit is outside this subtree. |
| `reports/round-26/remainders/v3-baseline-r26/twin.json` | 103155 | `d3de56a8` | 18:04:39 | O (remainder-disposition seats) | O fragment (round-25 remainder disposition); attributed evidence; the source edit is outside this subtree. |
| `reports/round-26/report-draft.md` | 13760 | `1fa48a55` | 18:30:59 | X (scribe seats) | Scribe draft/evidence record, not authorized final filing. |
| `reports/round-26/rerun.json` | 40765 | `d049dd0a` | 18:31:39 | X (scribe seats) | Scribe draft/evidence record, not authorized final filing. |
| `reports/round-26/run-validation.py` | 99165 | `4d79d048` | 18:30:11 | acceptance runner/receipt | Executable runner; existence is not a green end-to-end acceptance (the receipt is the verdict). |
| `reports/round-26/scope.md` | 13386 | `12681452` | 18:04:50 | X (scribe seats) | X scribe fragment (scope watch); attributed evidence. |
| `reports/round-26/scribe/capability-row.md` | 22370 | `9ab00ee1` | 18:12:10 | X (scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-26/scribe/fragment-ledger.json` | 18886 | `f4fe5fd5` | 18:12:28 | X (scribe seats) | NON-CANON read-time census ledger; admits nothing. |
| `reports/round-26/scribe/fragment-ledger.md` | 20611 | `05a4efc2` | 18:12:25 | X (scribe seats) | NON-CANON read-time census ledger; admits nothing. |
| `reports/round-26/scribe/frozen-rows.md` | 30627 | `2f5bd3b6` | 18:09:45 | X (scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-26/scribe/skill-rule-row.md` | 18337 | `15e4b2a9` | 18:06:33 | X (scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-26/scribe/x64-d4-chain-cold-rerun.md` | 20558 | `df7bd441` | 18:16:36 | X (scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-26/targets.json` | 192 | `50a30752` | 17:59:43 | declaration (parent) | Declared thresholds and seat allocation, not achieved outcomes. |
| `reports/round-26/validation.json` | 150611 | `d251d37c` | 18:38:16 | acceptance runner/receipt | Primary receipt; written by the runner. Binding checked in the observations below. |
| `reports/round-26/zzz-lessons-index-revision-3.md` | 23411 | `eb6cde79` | 18:16:50 | C (lessons-index revision seats) | C lessons-index revision (NEW file; revision 1/2 of corpus/lessons/README.md are filed bytes and stay unedited). |
| `reports/round-26/zzz-lessons-index-revision-4.md` | 30178 | `1c4623ec` | 18:23:14 | C (lessons-index revision seats) | C lessons-index revision (NEW file; revision 1/2 of corpus/lessons/README.md are filed bytes and stay unedited). |

**Census:** 93 artifacts indexed (this index file is the 94th, self-indexed
without size/sha). Excluded: `__pycache__/` (one file,
`reports/round-26/__pycache__/run-validation.cpython-314.pyc`) and `*.log`
(two files, `reports/round-26/remainders/v3-baseline-r26/run.log` and
`reports/round-26/register/v3-baseline-r26/run.log`, excluded by suffix as the
round-25 index also excludes `*.log`).

## Conformance observations

1. **Declared, not achieved.** Both `claims.json` and `targets.json` are the
   parent's declaration (`state: declared-before-dispatch`); nothing in this
   index converts a declaration into an achieved outcome. The achieved outcome
   lives in `validation.json`, which is the runner's artifact, not this seat's.

2. **D / depth — the register stratum landed, and this seat measured it.** Three
   entries re-run by this seat at the census (read-only, in-lane, no clone):
   `tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` →
   **exit 0**, `records=170 register_scoped=14 derived_pairs=8 claimed_chains=8
   borrow_pairs=6 violations=0 rule_holds=0`; its `--selftest` → **21/21**, exit
   0; `tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` →
   **20/20** legs exit 0, `…packet.d4.typed.yml` → **17/17** legs exit 0 with no
   `DERIV-REPLAY` FAIL line, and its `--selftest` → **19/19** exit 0. **The
   round-25 emptiness is gone:** the round-25 argot leg read
   `register_scoped=6 derived_pairs=0` over the same packet (X44 index,
   observation 3); the census reads `14 / 8`. The runner's own D measurement
   agrees (`argot_gate.coverage` = the same six numbers; `d4_typed_gate` exit 0 /
   20 legs; `typed_labels.classifying_delivered_pairs` = `L-55..L-62`). This is
   attributed evidence plus this seat's own re-run; the runner's `claims.D.passed
   = True` is the formal measurement.

3. **D / depth — the forecast closure is *named*, and its own reviewer says the
   delta is not zero.** `reports/round-26/argot/D24-forecast-closure.md` states
   its verdict in one line: the *checking leg* is delivered, the *relation* is
   not, so the correct closure is **"delta named"**, and it defines a **false
   closure** (§5) to forbid closing on the leg's existence alone. The runner
   nevertheless reads `claims.D.passed = True` with `names_forecast_closed:
   true` and `typed_gate_carries_the_leg: true`. This index does **not** resolve
   that tension; it records that (a) the D deliverable landed, (b) the D seat's
   own reviewer disputes the "closed" reading, and (c) the runner and the
   reviewer describe the same bytes at different stamps. The parent should read
   the two together, not either alone.

4. **O / operability — all three round-25 remainders are dispositioned as NEW
   rows, and the receipt is nonetheless red on O.** The three remainders named by
   `reports/round-25/audit/x48-v3-supersession.md:148-158`:
   - **r4 twin gap** → `reports/round-26/remainders/r4-twin/` (build-twin.py,
     verify-twin.py, twin.json 103,975 B, expected.json, freeze.txt) plus the
     `r4-twin.md` disposition; the twin is **generated from the packet**, not
     authored, and reproduces two filed twins byte-for-byte.
   - **stale v2 successor pin** (`reports/round-20/wart/expected-v2-07-r20.json`)
     → new row `reports/round-26/remainders/v2-successor-r26/expected.json`.
   - **stale v3 packet-baseline pin** (`reports/round-20/handoff/expected.json`)
     → new row `reports/round-26/remainders/v3-baseline-r26/`.
   No filed round-8..25 byte was edited; the new-row convention holds (the
   round-20 lesson). **But the census-state receipt still reads `O: False`**, with
   three failures: the re-pointed rows do not satisfy
   `pin-repoint-check.py --check`'s control set (`new-v3-row-replays-green`,
   measured by this seat as **16/17, exit 1**), the r4 checker is not green
   (51/52), and `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` exits
   1. The adversarial audit `reports/round-26/audit/o39-o40-remainder-fixes-adversarial.md`
   names the root cause: **the re-pointed v3 row went stale within ~3 minutes of
   landing** because the D seat's register-stratum write to `examples/culture-d4/`
   moved the read set, and the r4 checker's red is produced by the new
   `L3b-argot` gate leg, not by the tails it names. **This is a moving-target
   interaction between claims D and O, not a silent failure** — and it is the
   one place where the round's `after_required` ("the r4 checker green;
   regressions green") is **not met at this stamp**. Reported, not adjudicated.

5. **C / coverage — the open-question queue is 100% dispositioned, with a
   verifier independent of the ledger.** `reports/round-26/open-questions/`
   carries six disposer fragments (`C41..C46.md`), a builder
   (`build-dispositions.py`), the ledger (`dispositions.{json,md}`: 78 surface
   rows, `undispositioned: []`, classes carried 51 / fixed-with-evidence 15 /
   routed 7 / standing-rule 4 / closed-by-supersession 1), an independent
   verifier (`verify-dispositions.py`, `verify.json` → six checks V1..V6 all
   `ok: true`, `findings: []`), and a second auditor
   (`audit-dispositions.py`, `audit.json` → checks A1..A8 all `True`,
   `findings: []`, 49 queue rows / 0 undispositioned). The lessons-index
   revision landed as a **NEW file** —
   `reports/round-26/zzz-lessons-index-revision-{3,4}.md` — and the filed
   `corpus/lessons/README.md` bytes are **unchanged** (the C51/C52 receipt
   records `filed.blob_sha1 == declared_baseline`, `unchanged: true`). The
   runner's C leg agrees: `queue_rows 49 / dispositioned 49 / percent 100.0 /
   undispositioned 0`, `claims.C.passed = True`.

6. **Cross-round coexistence (disclosed).** Three read-time censuses of this
   subtree coexist: this one (X62, stamp 18:43:57Z), `fragment-index-x54.md`
   (C54, mtime 18:35:08Z) and `scribe/fragment-ledger.{json,md}` (X56, mtime
   18:12Z). They were taken at different stamps and will differ in count; that
   is the expected dated-refresh delta, not a contradiction. None is the round's
   verdict; the verdict is `validation.json`.

7. **The parent integrates.** `reports/round-26/report-draft.md` and
   `rerun.json` are drafts; there is no `reports/round-26/integration/` or
   `rule/` directory at this census, so no integration draft or rule draft is
   indexed. Filing, scope, integration into `LOG.md`/`SCORECARD.md`, the
   `corpus/lessons/round-26.md` lesson (present, untracked) and any final
   promotion verification remain parent responsibilities; in-lane attestations
   do not prove a fresh external inspection.

## Index verification

X62 writes only this file. This stdout-only control re-derives the index
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
"""R26-X62 index verification — stdout-only, read-only, in-memory negatives."""
import datetime, hashlib, re
from pathlib import Path

INDEX = Path('reports/round-26/fragment-index-x62.md')
BASE = Path('reports/round-26')
text = INDEX.read_text()
rows = re.findall(r'^\| `(reports/round-26/[^`]+)` \| (\d+) \| `([0-9a-f]{8})`', text, re.M)

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
assert not conforms(pairs + [('reports/round-26/__X62_nonexistent__.md', 1, '0' * 8)]), 'missing-path negative missed'
tampered = [(p, s, ('00000000' if h != '00000000' else '11111111')) for p, s, h in pairs]
assert not conforms(tampered), 'tampered-sha negative missed'
# shape
assert text.endswith('\n') and '\0' not in text
assert all(line == line.rstrip() for line in text.splitlines()), 'trailing whitespace'
assert len(re.findall(r'^```[^\n]*$', text, re.M)) % 2 == 0, 'unbalanced fences'
print('INDEX_CONTROL=PASS; duplicate/drop/missing/tampered negatives rejected; digests and availability current')
PY
```

Control run **2026-10-18T18:44:20Z** (command: the fenced block above, extracted
verbatim and executed): `indexed=93 observed=93`, `unindexed=[]`,
`unavailable=[]`, `runner_indexed=Y`, `receipt_binds_live_runner=True`,
`INDEX_CONTROL=PASS`, exit 0. A later arrival, a further receipt refresh, or a
runner edit invalidates this reading and needs a dated refresh.

## Boundary record

- **Writes:** this file only. No `reports/round-{8..25}` byte was touched, no
  tool or gate was edited, no shared bookkeeping (`LOG.md`, `SCORECARD.md`) was
  appended. Scratch under `.scratch/x62/` (gitignored) with
  `export TMPDIR=$PWD/.scratch` before every scratch-writing command. No commit,
  no push.
- **Independence:** this index was re-derived from the live bytes by
  `.scratch/x62/gen-index.py`, not transcribed from the C54 index or the X56
  ledger. Where the three agree on a digest, the agreement is a cross-check, not
  inheritance.
- **Canon:** NON-CANON engineering evidence. This index admits nothing,
  certifies no round and adjudicates no claim.
