# R26-C54 — round-26 fragment index + conformance

Seat **R26-C54** (scribe: fragment index + conformance) for round 26 (operator:
loop 3 of 3, build round 2 of 4; 64 workers on
`devin/deepseek-v4-1-flash-high`). Axes watched: **D / depth** (the register
stratum landing in D4), **O / operability** (the three round-25 remainders),
**C / coverage** (the open-question queue dispositioned). Declaration:
`reports/round-26/claims.json` (baseline
`fc13cd27b9e78d5d7c4f70740fd26c9383a7447b`); seat allocation:
`reports/round-26/targets.json` (D-register 28, O-remainders 12, C-openq 14,
X 10 = 64). Lane HEAD at this index's census: `1ad491a`.

This is the assigned C54 index — an availability read plus a presence/conformance
census. It is **not** a round-admission receipt, not a verdict replay, and not an
independent promotion review. The round's own counting command is
`python3 reports/round-26/run-validation.py`; the round's verdict is
`reports/round-26/validation.json`, which is indexed here, not adjudicated here.
No round validator was executed by this seat; no filed rounds 8–25 artifact was
read as writable, and none was modified.

**Filing note.** This index files at the round root
`reports/round-26/fragment-index-x54.md`. Seat **R26-X56** files
`reports/round-26/scribe/fragment-ledger.{json,md}`, a read-time census of the
same subtree that calls itself the integration ledger; the paths do not collide,
but the roles overlap. Both are indexed here; neither settles the other, and a
divergence between the two tables is a parent reconciliation item, not a verdict.

**Seat split inside claim C (named so the parent sees the seam).** Claim C is
carried by four seat groups and they do **not** overlap:

| seat | deliverable | state at this census |
|---|---|---|
| `R26-C41..C46`, `C47..C50` | the open-question disposition ledger under `reports/round-26/open-questions/` | present: `dispositions.{json,md}`, `verify.json`, `audit.{json,md}`, six `C4x.md` seat notes, four tools |
| `R26-C51..C52` | the **lessons README revision as a new file** (the runner requires the filed `corpus/lessons/README.md` bytes to stay byte-unchanged) | present: `reports/round-26/zzz-lessons-index-revision-3.md` (23 411 B) and `-4.md` (30 178 B) + a revision auditor/receipt/selftest |
| `R26-C53` | the lessons entry `reports/round-26/lessons/C53.md` | present (19 950 B) |
| `R26-C54` (this seat) | this fragment index + the shared census tool `reports/round-26/lessons/r26-census.py` | this file |

This seat did **not** write the README revision and did **not** edit the filed
`corpus/lessons/README.md`; that revision is C51/C52's write, and it landed. The
C53 entry carries the same stale-reading corrections as **new rows in its own
file**, which is the non-colliding form.

## Reading this index

- **Indexed** means the named artifact existed at the census and its size and
  sha8 were read. It does not mean the claim passed, a draft was integrated, or a
  control was executed.
- **Attributed** results belong to their source fragment; a row is a C54
  execution only where it says so.
- **Draft / declared / in-flight** are deliberate distinctions: a landed draft is
  not a landing; a declared threshold is not an achieved outcome; a runner on
  disk is not a green acceptance.
- Owner inference is directory/name based (stated in the table); `unassigned` is
  never guessed — and at this census the classifier returns **zero** `unassigned`
  rows, which is itself a reading about the round's directory shape.
- Counts carry their command and date; quotations name their location; a missing
  required artifact is named, never inferred.

## Availability (at the census stamp)

- Census: **2026-10-18T18:35:04Z** (command: `python3 -B
  reports/round-26/lessons/r26-census.py`; `__pycache__/`, `*.pyc`, `*.log`
  excluded; this index file is the self row, written after the census, never
  self-measured). Census count: **91** artifacts plus this index.
- **Counting command** `reports/round-26/run-validation.py` — **present** at
  census (99 165 B, sha256 prefix `4d79d048`, mtime 18:30:11Z), **settled**. It
  moved three times inside this seat's own window — 44 891 B / `10fafb94` at
  18:07:38Z, 79 466 B / `635b91f3` at 18:10:09Z, 99 165 B / `4d79d048` at
  18:30:11Z — and has not changed since 18:30:11Z.
- **Runner receipt** `reports/round-26/validation.json` — **present** at census
  (150 611 B, sha256 prefix `0922a67e`, mtime 18:33Z). It reads
  `acceptance_checks_passed: **false**`, **3** failures, claims
  `{C: true, D: true, O: false}`, `missing_dependencies: []`. **The round is
  OPEN, not admitted**: the O claim is red and the receipt says so.
- Marker line for the control: `runner_present_at_census=Y` and
  `receipt_present_at_census=Y`.
- **Binding check (the round-20 lesson).** The receipt's `runner_sha256` is
  `4d79d0488f895fc4…`; the live `reports/round-26/run-validation.py` hashes
  `4d79d0488f895fc4…` at the census — **the receipt binds the live runner
  bytes**, so its `passed: false` verdict is a reading of the runner that is on
  disk now, not a superseded snapshot. **This reading took three samples to
  settle, and the drift is disclosed rather than hidden:** an earlier sample in
  this seat's window read the receipt at 149 716 B / `37b3670a` bound to runner
  `060310d092d70a28…`, i.e. **not** bound, because the runner was being rewritten
  while the receipt was written. The settled pair above is the one this index
  binds. A further runner edit or a re-run of the counting command invalidates it
  and needs a dated refresh.
- **Wave shape.** The wave was **live** across most of this seat's window and
  went **quiescent** before the stamp: the round-26 tree went 4 → 7 → 16 → 30 →
  38 → 50 → 55 → 91 → 94 files between 18:03Z and 18:34Z. The last write in the
  50 s before the census was **zero** (`find reports/round-26 -type f -newermt
  '-50 seconds'` → 0 at 18:33:57Z), after five samples that read 2, 5, 11, 1, 2
  recent writes between 18:25:36Z and 18:29:16Z. The earlier reading in this
  seat's own window — a 55-artifact census at 18:10:13Z — drifted on **18 of its
  55 rows** within ten minutes. **This is the round-25 X44 situation repeating**:
  that index also had to bind a live wave and say so. A file arriving after this
  stamp needs a dated refresh, not an inferred worker failure.
- **Protected surface** (rounds 8–25, `git status --porcelain=v1` over
  `reports/round-{8..25}` at the census): **clean** — no modified protected
  artifact. The round-26 scope seat (`reports/round-26/scope.md`) reports the
  same for its own window, with 1 225 tracked paths matching the declared
  baseline; the runner's own `protected_status_rows` reads 0.
- **Fleet root** `/home/vgpnk/Projects/shokunin`: one untracked entry
  (`.scratch/`, gitignored); no tracked modification. The round-26 scope seat
  additionally discloses two debris families at the fleet root (ten
  `.scratch/*.out` files and a stray `bash: ` directory) — both outside this
  lane, both disclosed rather than dispositioned, and neither is a kotodama
  filed artifact.

## Census

Read-time census of `reports/round-26/**` at **2026-10-18T18:35:04Z** (command:
`python3 -B reports/round-26/lessons/r26-census.py`, sha8 digests via
`hashlib.sha256`; see **Index verification** for the reproducible coverage
control). Files under `__pycache__/` and `*.log` are excluded. The wave was in
flight at the census; a file arriving after it needs a dated refresh. Counts are
artifact counts, not worker counts.

| artifact | bytes | sha8 | mtime UTC | inferred owner | conformance state / limit |
|---|---:|---|---|---|---|
| `reports/round-26/adjacency.md` | 24353 | `b3da3afa` | 18:10:32 | X (adjacency/scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-26/argot/D21-adversarial-replay.md` | 14903 | `77fa1e8f` | 18:08:41 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/argot/D22-label-typing-crosscheck.md` | 12308 | `1328ba0a` | 18:08:56 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/argot/D23-overmatch.md` | 11191 | `7d31da7d` | 18:07:23 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/argot/D24-forecast-closure.md` | 12849 | `28cfa555` | 18:09:00 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/audit/o39-o40-remainder-fixes-adversarial.md` | 21671 | `0c7a10d7` | 18:27:06 | auditors (X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-26/audit/x60-register-derivation-spotcheck.md` | 27096 | `71745325` | 18:11:48 | auditors (X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-26/audit/x60-register-derivation-spotcheck.py` | 24203 | `db22fb13` | 18:10:47 | auditors (X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-26/audit/x63-lessons-audit.md` | 16876 | `ed933058` | 18:07:04 | auditors (X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-26/audit/x63-lessons-audit.py` | 22851 | `33e27e78` | 18:05:27 | auditors (X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-26/audit/x63-lessons-receipt.json` | 4912 | `d90aebc2` | 18:06:53 | auditors (X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-26/availability.json` | 23057 | `7e23f33d` | 18:26:02 | X (availability seat) | Availability record; a route/liveness measurement, not acceptance. |
| `reports/round-26/claims.json` | 2383 | `363498ed` | 17:59:43 | declaration (parent) | Declared thresholds and seat allocation, not achieved outcomes. |
| `reports/round-26/gate-tests/D17-D20-teeth.md` | 3563 | `b92b8081` | 18:22:59 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-26/gate-tests/D17-typed-gate.md` | 6640 | `3c835aa3` | 18:25:24 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-26/gate-tests/D18-negatives.md` | 6505 | `d2bbe8da` | 18:22:57 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-26/gate-tests/D19-determinism.md` | 3770 | `5b462bef` | 18:22:53 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-26/gate-tests/D20-replay-frozen.md` | 7212 | `50f219e7` | 18:22:49 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-26/gate-tests/fixtures/n1-maximal-coda.yml` | 539 | `460cae84` | 18:05:57 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-26/gate-tests/fixtures/n2-rule-mismatch.yml` | 485 | `ef2ad71b` | 18:05:57 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-26/gate-tests/fixtures/n3-positive-control.yml` | 553 | `92e14150` | 18:05:57 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-26/gate-tests/fixtures/n4-unknown-rule.yml` | 350 | `77b31d15` | 18:05:57 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-26/gate-tests/fixtures/n5-borrow-mismatch.yml` | 339 | `04f54be6` | 18:05:57 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-26/gate-tests/fixtures/n6-coverage-hold.yml` | 408 | `5b455472` | 18:05:57 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-26/gate-tests/fixtures/n7-malformed.yml` | 46 | `c19d69c0` | 18:05:57 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-26/gate-tests/fixtures/n8-lengthen-mismatch.yml` | 771 | `d5a0f128` | 18:12:10 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-26/gate-tests/freeze.py` | 10446 | `3614fa51` | 18:23:49 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-26/gate-tests/receipt.json` | 56267 | `1e630436` | 18:25:57 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-26/gate-tests/run-gate-tests.py` | 31393 | `112181d9` | 18:23:59 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-26/lessons/C51-C52.md` | 13179 | `fb916d39` | 18:24:19 | C (lessons-entry / index seats) | C fragment (census/tool/report/revision draft); attributed evidence; the landed index is outside this subtree. |
| `reports/round-26/lessons/C53.md` | 24626 | `2f46520a` | 18:34:57 | C (lessons-entry / index seats) | C fragment (census/tool/report/revision draft); attributed evidence; the landed index is outside this subtree. |
| `reports/round-26/lessons/c51-revision-audit.py` | 15080 | `d0b6d1b3` | 18:22:10 | C (lessons-entry / index seats) | C fragment (census/tool/report/revision draft); attributed evidence; the landed index is outside this subtree. |
| `reports/round-26/lessons/c51-revision-receipt.json` | 1874 | `1eaab903` | 18:24:06 | C (lessons-entry / index seats) | C fragment (census/tool/report/revision draft); attributed evidence; the landed index is outside this subtree. |
| `reports/round-26/lessons/c51-revision-selftest.json` | 1685 | `82292aa3` | 18:24:06 | C (lessons-entry / index seats) | C fragment (census/tool/report/revision draft); attributed evidence; the landed index is outside this subtree. |
| `reports/round-26/lessons/r26-census.py` | 8670 | `cd64a81e` | 18:30:24 | C (lessons-entry / index seats) | C fragment (census/tool/report/revision draft); attributed evidence; the landed index is outside this subtree. |
| `reports/round-26/open-questions/C41.md` | 13930 | `70c80d11` | 18:11:01 | C (open-question disposition seats) | C disposition fragment; attributed evidence; the disposition is read here, not re-adjudicated. |
| `reports/round-26/open-questions/C42.md` | 6417 | `2cbbfc89` | 18:09:03 | C (open-question disposition seats) | C disposition fragment; attributed evidence; the disposition is read here, not re-adjudicated. |
| `reports/round-26/open-questions/C43.md` | 9349 | `ad598518` | 18:09:03 | C (open-question disposition seats) | C disposition fragment; attributed evidence; the disposition is read here, not re-adjudicated. |
| `reports/round-26/open-questions/C44.md` | 8363 | `33c4e3db` | 18:11:37 | C (open-question disposition seats) | C disposition fragment; attributed evidence; the disposition is read here, not re-adjudicated. |
| `reports/round-26/open-questions/C45.md` | 16785 | `72f60533` | 18:11:09 | C (open-question disposition seats) | C disposition fragment; attributed evidence; the disposition is read here, not re-adjudicated. |
| `reports/round-26/open-questions/C46.md` | 7472 | `eb1adc51` | 18:10:47 | C (open-question disposition seats) | C disposition fragment; attributed evidence; the disposition is read here, not re-adjudicated. |
| `reports/round-26/open-questions/audit-dispositions.py` | 24660 | `1fdd6607` | 18:21:22 | C (open-question disposition seats) | C disposition fragment; attributed evidence; the disposition is read here, not re-adjudicated. |
| `reports/round-26/open-questions/audit.json` | 45017 | `558a5b67` | 18:23:42 | C (open-question disposition seats) | C disposition fragment; attributed evidence; the disposition is read here, not re-adjudicated. |
| `reports/round-26/open-questions/audit.md` | 3780 | `c1e0eea5` | 18:23:42 | C (open-question disposition seats) | C disposition fragment; attributed evidence; the disposition is read here, not re-adjudicated. |
| `reports/round-26/open-questions/build-dispositions.py` | 45530 | `f833cedd` | 18:17:51 | C (open-question disposition seats) | C disposition fragment; attributed evidence; the disposition is read here, not re-adjudicated. |
| `reports/round-26/open-questions/dispositions.json` | 95421 | `4071dbf9` | 18:23:43 | C (open-question disposition seats) | C disposition fragment; attributed evidence; the disposition is read here, not re-adjudicated. |
| `reports/round-26/open-questions/dispositions.md` | 9468 | `5af233b9` | 18:23:43 | C (open-question disposition seats) | C disposition fragment; attributed evidence; the disposition is read here, not re-adjudicated. |
| `reports/round-26/open-questions/verify-dispositions.py` | 7179 | `2ea881b3` | 18:07:54 | C (open-question disposition seats) | C disposition fragment; attributed evidence; the disposition is read here, not re-adjudicated. |
| `reports/round-26/open-questions/verify.json` | 765 | `9a7c76de` | 18:21:25 | C (open-question disposition seats) | C disposition fragment; attributed evidence; the disposition is read here, not re-adjudicated. |
| `reports/round-26/register/design.md` | 14454 | `27d23fa6` | 18:10:37 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/execution-1.md` | 10155 | `42aaa818` | 18:16:08 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/execution-2.md` | 6726 | `87bc9d94` | 18:13:41 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/execution-3.md` | 8368 | `4ccbb4ab` | 18:13:51 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/execution-4.md` | 8801 | `cf361a8b` | 18:14:04 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/forms.md` | 10031 | `06635a1c` | 18:10:37 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/impl.md` | 16553 | `180a60b2` | 18:27:21 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/repin.json` | 6986 | `45156429` | 18:30:00 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/review.md` | 13537 | `0082f08b` | 18:10:29 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/rules.md` | 9350 | `535cf7a9` | 18:10:29 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/v3-baseline-r26/expected.json` | 10856 | `581f1a8d` | 18:26:36 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/v3-baseline-r26/freeze.txt` | 521 | `7060579e` | 18:26:36 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/v3-baseline-r26/packet.md` | 105582 | `69ce3877` | 18:26:36 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/register/v3-baseline-r26/twin.json` | 103370 | `b849e2f9` | 18:26:36 | D (register-stratum seats) | D fragment (register-stratum derivation); attributed evidence, not independently re-executed here. |
| `reports/round-26/remainders/pin-repoint-check.py` | 12165 | `5674a6b3` | 18:06:54 | O (remainder disposition seats) | O fragment (remainder disposition); attributed evidence. |
| `reports/round-26/remainders/pin-repoint-receipt.json` | 4722 | `406b764e` | 18:08:57 | O (remainder disposition seats) | O fragment (remainder disposition); attributed evidence. |
| `reports/round-26/remainders/pins.json` | 6887 | `cae128ab` | 18:08:34 | O (remainder disposition seats) | O fragment (remainder disposition); attributed evidence. |
| `reports/round-26/remainders/pins.md` | 8109 | `fcb6e1fc` | 18:08:45 | O (remainder disposition seats) | O fragment (remainder disposition); attributed evidence. |
| `reports/round-26/remainders/r4-twin/build-twin.py` | 18739 | `20a670e2` | 18:26:06 | O (remainder disposition seats) | O fragment (remainder disposition); attributed evidence. |
| `reports/round-26/remainders/r4-twin/expected.json` | 1912 | `d02a9f2c` | 18:14:27 | O (remainder disposition seats) | O fragment (remainder disposition); attributed evidence. |
| `reports/round-26/remainders/r4-twin/freeze.txt` | 2556 | `d3b0e2f1` | 18:17:26 | O (remainder disposition seats) | O fragment (remainder disposition); attributed evidence. |
| `reports/round-26/remainders/r4-twin/twin.json` | 103975 | `1874efbc` | 18:26:44 | O (remainder disposition seats) | O fragment (remainder disposition); attributed evidence. |
| `reports/round-26/remainders/r4-twin/verify-twin.py` | 20274 | `10cfa07d` | 18:29:57 | O (remainder disposition seats) | O fragment (remainder disposition); attributed evidence. |
| `reports/round-26/remainders/v2-successor-r26/expected.json` | 4435 | `f695b910` | 18:04:35 | O (remainder disposition seats) | O fragment (remainder disposition); attributed evidence. |
| `reports/round-26/remainders/v3-baseline-r26/expected.json` | 10856 | `4879e760` | 18:04:39 | O (remainder disposition seats) | O fragment (remainder disposition); attributed evidence. |
| `reports/round-26/remainders/v3-baseline-r26/freeze.txt` | 521 | `adad86ab` | 18:04:39 | O (remainder disposition seats) | O fragment (remainder disposition); attributed evidence. |
| `reports/round-26/remainders/v3-baseline-r26/packet.md` | 105582 | `a97a0f0a` | 18:04:39 | O (remainder disposition seats) | O fragment (remainder disposition); attributed evidence. |
| `reports/round-26/remainders/v3-baseline-r26/twin.json` | 103155 | `d3de56a8` | 18:04:39 | O (remainder disposition seats) | O fragment (remainder disposition); attributed evidence. |
| `reports/round-26/report-draft.md` | 13760 | `1fa48a55` | 18:30:59 | X (scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-26/rerun.json` | 40765 | `d049dd0a` | 18:31:39 | X (scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-26/run-validation.py` | 99165 | `4d79d048` | 18:30:11 | acceptance runner | Executable runner; existence is not a green end-to-end acceptance (the receipt is the verdict). |
| `reports/round-26/scope.md` | 13386 | `12681452` | 18:04:50 | X (scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-26/scribe/capability-row.md` | 22370 | `9ab00ee1` | 18:12:10 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-26/scribe/fragment-ledger.json` | 18886 | `f4fe5fd5` | 18:12:28 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-26/scribe/fragment-ledger.md` | 20611 | `05a4efc2` | 18:12:25 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-26/scribe/frozen-rows.md` | 30627 | `2f5bd3b6` | 18:09:45 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-26/scribe/skill-rule-row.md` | 18337 | `15e4b2a9` | 18:06:33 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-26/scribe/x64-d4-chain-cold-rerun.md` | 20558 | `df7bd441` | 18:16:36 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-26/targets.json` | 192 | `50a30752` | 17:59:43 | declaration (parent) | Declared thresholds and seat allocation, not achieved outcomes. |
| `reports/round-26/validation.json` | 150611 | `0922a67e` | 18:32:39 | acceptance runner/receipt | Primary receipt; written by the runner. Binding checked below. |
| `reports/round-26/zzz-lessons-index-revision-3.md` | 23411 | `eb6cde79` | 18:16:50 | C (lessons-index revision seats) | C lessons-index revision (new file, not an edit of the filed `corpus/lessons/README.md`); attributed evidence, read here. |
| `reports/round-26/zzz-lessons-index-revision-4.md` | 30178 | `1c4623ec` | 18:23:14 | C (lessons-index revision seats) | C lessons-index revision (new file, not an edit of the filed `corpus/lessons/README.md`); attributed evidence, read here. |
CENSUS_COUNT=91

**Census:** 91 artifacts indexed (this index file is the 92nd, self-indexed
without size/sha). Excluded: `__pycache__/` (two files under
`reports/round-26/audit/`) and `*.log` (three: the `v3-baseline-r26/run.log`
pair plus one under `remainders/`).

**Absent required artifacts, named:** `reports/round-26/integration/` — **no such
directory** at the census (no LOG/SCORECARD draft has landed under the round
root; the parent's `report-draft.md` and `rerun.json` sit at the root instead).
Nothing else the declaration requires is missing: the counting command, the
receipt, the C revision files and the O/D evidence directories all exist.

## Conformance observations

1. **Declared, not achieved — and the achieved outcome is RED.** Both
   `claims.json` and `targets.json` are the parent's declaration. The receipt
   landed and reads `acceptance_checks_passed: false` with claims
   `{C: true, D: true, O: false}`. So the round is **open on O**; this index
   reports that verdict, it does not produce or contest it.

2. **O / operability — the round's red, named.** All three failures are on
   claim O, quoted from the settled receipt (18:33Z):
   - `pin-repoint-checker is not green: the re-pointed rows do not satisfy its
     control set (['new-v3-row-replays-green'])` — the re-pointed pin rows exist
     (`remainders/pins.json`, `pin-repoint-receipt.json`) but one named control,
     `new-v3-row-replays-green`, does not hold.
   - `r4-checker is not green … (['claim D: v2 successor row not green:
     reports/round-20/wart/expected-v2-07-r20.json exit 2 — V2F-DIGEST: 1 pinned
     file(s) changed since the freeze: tools/d2-typed-labels.py', 'claim D: v3
     baseline reports/round-20/handoff/expected.json pins packet e92f5e6775b6…
     but the run assembled a97a0f0a0a49…'])` — the r4 checker's own control set
     names two successor-pin mismatches; the second is the same `a97a0f0a…`
     packet digest the round-26 `remainders/v3-baseline-r26/packet.md` carries.
   - `Regression failed: python3 tools/exercise-handoff-e2e.py --profile v3
     --quiet (exit 1)` — the fixed regression battery is not green.
   The O seat's own fragments and the adversarial audit
   (`audit/o39-o40-remainder-fixes-adversarial.md`) are indexed below; which of
   the three is a real defect versus a checker-convention mismatch is the O
   claim's and the parent's, not this index's. Note the **stamp sensitivity**:
   an earlier receipt sample (149 716 B / `37b3670a`) named a *different* first
   failure — the r4 twin's `packet_links.py` — so the O failure set moved with
   the runner revision. The settled set above is the one this index binds.

3. **D / depth — the register stratum landed, and this seat re-ran nothing.** The
   D fragments span `argot/` (four: `D21-adversarial-replay`,
   `D22-label-typing-crosscheck`, `D23-overmatch`, `D24-forecast-closure`) and
   `register/` (eleven: `design`, `forms`, `rules`, `review`, `impl`,
   `execution-1..4`, `repin.json`, plus the `v3-baseline-r26/` packet/twin set)
   and `gate-tests/` (five `D17..D20` notes + an eight-fixture negative set + a
   frozen receipt). The peer auditor
   `reports/round-26/audit/x60-register-derivation-spotcheck.py` is the
   independent instrument; this seat did **not** re-execute it, and the runner's
   own `Claim D` measurement is the formal reading — the receipt marks D
   `passed: true`.

4. **C / coverage — both halves landed.** (a) The disposition ledger:
   `open-questions/verify.json` reads six checks all `ok: true`,
   `surface_rows: 78`, `ledger_rows: 78`, `findings: []` — the ledger's own
   control claims 78/78 rows dispositioned with zero ghosts and zero
   undispositioned rows; an independent `audit.json`/`audit.md` re-checks it.
   That is the **C41..C50 seats'** reading, attributed here, not re-run by this
   seat. (b) The README revision: `zzz-lessons-index-revision-3.md` (queue
   dispositions) and `-4.md` (which additionally re-derives the per-round pins
   and dispositions the six `X63-G1` stale readings) both exist as **new files**;
   the filed `corpus/lessons/README.md` is byte-unchanged (runner-declared blob
   `a31870556c733498…`). The receipt marks C `passed: true`.

5. **C / coverage — the C53 lessons entry and the C51/C52 revision independently
   reach the same stale-reading split.** `reports/round-26/lessons/C53.md`
   (19 950 B) re-verifies the peer finding `X63-G1` and splits it into **two
   defect-class** readings (the round-12 and round-21 disposition pointers, false
   when the index was written — their receipts predate it by ~18 h and ~3 h) and
   **four honest-at-stamp** readings (Q-04-1, Q-23-1..3, whose subjects moved in
   `fc13cd2` at 17:58:37Z, after the index's 17:47Z stamp). Revision 4
   (§3) dispositions the same six. Two seats reaching the same split by different
   routes is an independent cross-check, not inheritance; neither edits the filed
   index.

6. **Cross-round coexistence (disclosed).** Seat R26-X56's
   `scribe/fragment-ledger.{json,md}` is a second read-time census of this
   subtree. Its census predates the last arrivals indexed here (it read 44 files
   and 881 431 bytes at 18:07:42Z; this census reads 91 artifacts at 18:30:25Z),
   so the two tables **will** differ — that is the expected dated-refresh delta,
   not a contradiction. Both are indexed; a divergence is a parent reconciliation
   item.

7. **The parent integrates.** No `reports/round-26/integration/` directory exists
   at the census; `report-draft.md` (13 708 B) and `rerun.json` (37 859 B) are
   drafts at the round root. Filing, scope, integration into
   `LOG.md`/`SCORECARD.md`, the O-claim re-run, and any final promotion
   verification remain parent responsibilities; in-lane attestations do not prove
   a fresh external inspection.

## Index verification

Reproducible coverage control over the table above. The generator
`reports/round-26/lessons/r26-census.py` walks the subtree; this block re-checks
that the index rows and the live tree agree on **digest**, and that the
availability markers are current. Extract and run from the lane root:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-26/lessons/r26-census.py --selftest   # 14/14 in-memory
python3 -B reports/round-26/lessons/r26-census.py              # regenerate the table
```

```sh
python3 - <<'PY'
import datetime, hashlib, re
from pathlib import Path
BASE = Path('reports/round-26')
SELF = BASE / 'fragment-index-x54.md'
text = SELF.read_text()
rows = re.findall(r"(?m)^\|\s*`([^`]+)`\s*\|\s*(\d+)\s*\|\s*`([0-9a-f]{8})`\s*\|", text)

def actual():
    return [str(p) for p in sorted(BASE.rglob('*'))
            if p.is_file() and '__pycache__' not in p.parts
            and not p.name.endswith(('.pyc', '.log')) and p != SELF]

def ok_one(p, s, h):
    f = Path(p)
    if not f.is_file() or f.stat().st_size <= 0:
        return False
    data = f.read_bytes()
    return len(data) == int(s) and hashlib.sha256(data).hexdigest()[:8] == h

names = [p for p, _, _ in rows]
drift = [(p, s, h) for p, s, h in rows if not ok_one(p, s, h)]
print('observed_at=' + datetime.datetime.now(datetime.timezone.utc).isoformat())
print(f'indexed={len(rows)} observed={len(actual())}')
print('duplicate_rows=', len(names) != len(set(names)))
print('unavailable=', sorted(set(names) - set(actual())))
print('arrivals_since_census=', sorted(set(actual()) - set(names)))
print('digest_drift=', drift)

# The wave was live at the census, so the control is DRIFT-AWARE by design:
# it must hold that no indexed row is *unavailable* and no row is duplicated,
# and it must PRINT any arrival or drift rather than assert a frozen tree.
# That is the round-20 lesson applied: a live-wave index that asserted
# equality would fail spuriously on every later read.
assert not (len(names) != len(set(names))), 'duplicate index row'
assert not (set(names) - set(actual())), 'an indexed artifact is now unavailable'

# availability markers, both directions
m_r = re.search(r'runner_present_at_census=(\w+)', text)
m_p = re.search(r'receipt_present_at_census=(\w+)', text)
assert m_r and m_p, 'availability marker line missing'
runner = BASE / 'run-validation.py'
receipt = BASE / 'validation.json'
assert (m_r.group(1) == 'Y') == runner.is_file(), 'index stale: runner presence drifted'
assert (m_p.group(1) == 'Y') == receipt.is_file(), 'index stale: receipt presence drifted'
print(f'runner_marker={m_r.group(1)} runner_now={runner.is_file()}')
print(f'receipt_marker={m_p.group(1)} receipt_now={receipt.is_file()}')

# negative controls (in memory only)
pairs = [(p, s, h) for p, s, h in rows]
def conforms(ps):
    ns = [p for p, _, _ in ps]
    return (len(ns) == len(set(ns)) and set(ns) == set(actual())
            and all(ok_one(*r) for r in ps))
assert not conforms(pairs + [pairs[0]]), 'duplicate negative missed'
assert not conforms(pairs + [('reports/round-26/__C54_nonexistent__.md', 1, '0' * 8)]), 'missing-path negative missed'
tampered = [(p, s, ('00000000' if h != '00000000' else '11111111')) for p, s, h in pairs]
assert not conforms(tampered), 'tampered-sha negative missed'
assert text.endswith('\n') and '\0' not in text
assert all(line == line.rstrip() for line in text.splitlines()), 'trailing whitespace'
assert len(re.findall(r'^```[^\n]*$', text, re.M)) % 2 == 0, 'unbalanced fences'
print('INDEX_CONTROL=PASS; duplicate/missing/tampered negatives rejected; markers current')
PY
```

The generator's `--selftest` is 14 in-memory checks (exit 0), including the
negative controls: an unknown path must classify `unassigned` (never guessed), a
runner row must not read as green, and the self row must be excluded.

**Standing caveat.** The tree went quiescent before the census (zero writes in
the 50 s before the stamp) and the receipt now binds the live runner
(`4d79d048`), so this reading is the settled one — but it settled only after
**three** samples: an earlier receipt read 149 716 B / `37b3670a` bound to runner
`060310d0` (not bound), and the runner itself moved three times in this seat's
window. A later arrival, a further runner edit, or a re-run of the counting
command invalidates this reading and requires a dated refresh. The round-25 X44
index's own control caught exactly this class of drift on its receipt (an earlier
reading `f8375af6` / 106 957 B superseded by `e887239c` / 107 893 B inside its
window); this index discloses the same hazard — and here the drift was **real
and observed**, not hypothetical.
