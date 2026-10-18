# R27-X56 — fragment index + conformance

Seat **R27-X56** (scribe: fragment index + conformance) for round 27 (operator:
loop 3 of 3, build round 3 of 4; 64 workers on
`devin/deepseek-v4-1-flash-high`). Axes watched: **D / depth** (the register law
lands + the syllabify disagreement is fixed), **O / operability** (the D4 pin
sweep + regressions), **C / coverage** (the register-strata knowledge entry +
README). Declaration: `reports/round-27/claims.json` (baseline
`4f09c990d4c17f23b5e2cda0871f81db875635fc`, the round-26 admit); seat allocation:
`reports/round-27/targets.json` (D-register-law 24, O-sweep 20, C-entry 10, X 10 =
64). Lane HEAD at this index's census: `b95fca1`.

This is the assigned X56 index — an availability read plus a presence/conformance
census. It is **not** a round-admission receipt, not a verdict replay, and not an
independent promotion review. The round's own counting command is
`python3 reports/round-27/run-validation.py`; the round's verdict is
`reports/round-27/validation.json`, which is indexed here, not adjudicated here.
No round validator was executed by this seat; no filed rounds 8–26 artifact was
read as writable, and none was modified.

**Filing note.** This index files at the round root
`reports/round-27/fragment-index-x56.md`. Seat **R27-D24** files
`reports/round-27/scribe/fragment-ledger.{json,md}`, a read-time census of the
same subtree that calls itself the integration ledger; the paths do not collide,
but the roles overlap. Both are indexed here; neither settles the other, and a
divergence between the two tables is a parent reconciliation item, not a verdict.
The round-26 precedents (`fragment-index-x54.md`, `fragment-index-x62.md`) are the
form this index follows.

## Reading this index

- **Indexed** means the named artifact existed at the census and its size and
  sha8 were read. It does not mean the claim passed, a draft was integrated, or a
  control was executed.
- **Attributed** results belong to their source fragment; a row is an X56
  execution only where it says so. Where this seat re-ran an instrument itself,
  the observation says so and names the command.
- **Draft / declared / in-flight** are deliberate distinctions: a landed draft is
  not a landing; a declared threshold is not an achieved outcome; a runner on
  disk is not a green acceptance.
- Owner inference is directory/name based (stated in the table); `unassigned` is
  never guessed — and at this census the classifier returns **zero** `unassigned`
  rows (the `pinsweep/` partition was added to the classifier during the seat's
  own window, before the census; see **Index verification**).
- Counts carry their command and date; quotations name their location; a missing
  required artifact is named, never inferred.

## Availability (at the census stamp)

- Census: **2026-10-18T19:45:06Z** (command: `python3 -B
  reports/round-27/scribe/x56-census.py`; `__pycache__/`, `*.pyc`, `*.log`
  excluded; this index file is the self row, written after the census, never
  self-measured). Census count: **125** artifacts plus this index (3 327 278 B,
  70 052 lines).
- **Counting command** `python3 reports/round-27/run-validation.py` — **present**
  at census (92 131 B, sha256
  `48667305388b1e842e9470875d1f9809111f01c0130e7bd8409c4417a386ec3f`, mtime
  19:43:24Z).
- **Runner receipt** `reports/round-27/validation.json` — **present** at census
  (232 081 B, sha256 prefix `9c7abac2`, mtime 19:42:56Z). It reads
  `measured_at_utc: 2026-10-18T19:42:56+00:00`,
  `acceptance_checks_passed: **false**`, **2** failures, claims
  `{C: true, D: true, O: false}`, `missing_dependencies: []`. **The round is
  OPEN, not admitted**: the O claim is red and the receipt says so.
- Marker line for the control: `runner_present_at_census=Y` and
  `receipt_present_at_census=Y` and `binding_ok_at_census=N`.
- **Binding check (the round-20 lesson).** The receipt's `runner_sha256` is
  `2195398055a6a5e0…`; the live `reports/round-27/run-validation.py` hashes
  `48667305388b1e84…` at the census — **the receipt does NOT bind the live runner
  bytes**, because the runner was rewritten (mtime 19:43:24Z) after the receipt
  was written (19:42:56Z). **So the `false` verdict above is a reading of the
  runner as it stood at 19:42:56Z, not of the runner on disk now.** The verdict
  was `false` at every sample this seat took (19:23Z: 7 failures; 19:24Z: 8;
  19:28Z: 4; 19:31Z: 2; 19:33Z: 2; 19:36Z: 3; 19:42Z: 2), so the O red is stable
  across the runner revisions even though the exact failure list moved; but a
  reader who needs a *bound* verdict must re-run the counting command. This is
  disclosed rather than hidden, and it is the round-25 X44 / round-26 X54 hazard
  recurring: a live-wave receipt is a dated reading.
- **Wave shape.** The wave was **live at the census**. The round-27 tree grew
  **2 → 4 → 8 → 19 → 35 → 64 → 99 → 123** files between 19:11:04Z and 19:38Z,
  went briefly quiescent (zero writes in 60 s at 19:37:47Z), then resumed a long
  tail (the O seat re-freezing its pin baselines, 41 writes/min at 19:45:04Z).
  The census at 19:45:06Z was taken **inside that tail**. A file arriving after
  this stamp needs a dated refresh, not an inferred worker failure.
- **Protected surface** (rounds 8–26, `git status --porcelain=v1` over
  `reports/round-{8..26}` at the census): **clean** — 0 modified protected
  artifact. `git status` over `tools/gates/frozen` is also clean (0 rows). The
  round-27 scope seat (`reports/round-27/scope.md`) reports the same for its own
  window, with 1 460 tracked paths under `reports/round-{8..26}` plus
  `tools/gates/frozen/round-{8..26}` matching the declared baseline in Git blob
  identity and mode (0 mismatches, 0 missing).
- **Fleet root** `/home/vgpnk/Projects/shokunin`: two untracked/modified entries
  — the gitignored `.scratch/` and a pre-existing `M .ufo/l0-questions.md`, both
  outside this lane and predating round-27 dispatch. The round-27 scope seat
  discloses four debris families at the fleet root (the ten `.scratch/*.out`
  files, the stray `bash: ` tree, `.scratch/goal-20261018-game-dev-2d-training.md`,
  and the `.ufo/l0-questions.md` modification) and reports the assignment's
  "fleet root clean" clause as **failing as observed**; all four predate dispatch,
  so no round-27 seat authored them. Disclosed here, not dispositioned.

## Census

Read-time census of `reports/round-27/**` at **2026-10-18T19:45:06Z** (command:
`python3 -B reports/round-27/scribe/x56-census.py`, sha8 digests via
`hashlib.sha256`; see **Index verification** for the reproducible coverage
control). Files under `__pycache__/` and `*.log` are excluded. **The wave was
live at the census; a file arriving after it needs a dated refresh.** Counts are
artifact counts, not worker counts. Owner inference is directory/name based.

| artifact | bytes | sha8 | mtime UTC | inferred owner | conformance state / limit |
|---|---:|---|---|---|---|
| `reports/round-27/adjacency.md` | 54021 | `ae332145` | 19:29:29 | X (adjacency/scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-27/argot/D17-speech-act-outside-the-law.md` | 14395 | `a59885bd` | 19:35:09 | D (register-law seats) | D fragment (register-law derivation); attributed evidence, not independently re-executed here. |
| `reports/round-27/argot/D18-mis-syllabified-form.md` | 12254 | `c02fdbeb` | 19:35:19 | D (register-law seats) | D fragment (register-law derivation); attributed evidence, not independently re-executed here. |
| `reports/round-27/argot/D19-label-typing-crosscheck.md` | 9802 | `6bd71e0a` | 19:35:30 | D (register-law seats) | D fragment (register-law derivation); attributed evidence, not independently re-executed here. |
| `reports/round-27/argot/D20-gap-closure-record.md` | 13464 | `90795a10` | 19:35:45 | D (register-law seats) | D fragment (register-law derivation); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/entry-audit.py` | 21446 | `fb589b28` | 19:23:32 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/o37-sweep-inventory-audit.py` | 14662 | `020b743d` | 19:32:32 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/o38-sweep-inventory-adjudication.py` | 19638 | `62e87ec2` | 19:33:30 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/o39-o40-sweep-adversarial.md` | 24747 | `65f910bd` | 19:30:43 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/x-c48-entry-audit.md` | 14593 | `6eef2b70` | 19:24:28 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/x-c48-receipt.json` | 175262 | `de4a4634` | 19:23:37 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/x57-lessons-audit.md` | 16970 | `78ed683d` | 19:16:30 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/x57-lessons-audit.py` | 36947 | `3b5aa5c6` | 19:15:38 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/x57-lessons-receipt.json` | 12672 | `9ea21438` | 19:16:34 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/x57-lessons-selftest.json` | 4398 | `0b6d9ea4` | 19:16:33 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/x59-register-law-negatives.md` | 16094 | `84a2fb8a` | 19:25:36 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/x59-register-law-negatives.py` | 23147 | `52672606` | 19:25:09 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/x60-sweep-completeness.md` | 13480 | `9a56622a` | 19:26:06 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/x60-sweep-completeness.py` | 18502 | `6c56a7fc` | 19:21:05 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/x61-pin-sweep.md` | 19130 | `90bf1d3d` | 19:25:51 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/x61-pin-sweep.py` | 29623 | `c97e442a` | 19:19:55 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/x62-frozen-record-audit.md` | 13863 | `5b1adac1` | 19:26:01 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/x62-frozen-record-audit.py` | 28143 | `4e0c16be` | 19:23:40 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/x63-entry-source-resolvability.md` | 17870 | `da4ebde0` | 19:25:10 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/x63-entry-source-resolvability.py` | 36967 | `0622aa72` | 19:25:03 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/audit/x64-cold-rerun.py` | 20650 | `8f67ea5d` | 19:23:42 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-27/availability.json` | 29324 | `987b04e1` | 19:23:36 | X (availability seat) | Availability record; a route/liveness measurement, not acceptance. |
| `reports/round-27/claims.json` | 2355 | `373df289` | 19:11:04 | declaration (parent) | Declared thresholds and seat allocation, not achieved outcomes. |
| `reports/round-27/entry/C41.md` | 8082 | `48e5efdd` | 19:31:38 | C (register-knowledge entry seats) | C fragment (register-strata knowledge entry); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-27/entry/C42.md` | 6040 | `c2a9ad5e` | 19:29:25 | C (register-knowledge entry seats) | C fragment (register-strata knowledge entry); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-27/entry/C43.md` | 5875 | `e43cb993` | 19:31:50 | C (register-knowledge entry seats) | C fragment (register-strata knowledge entry); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-27/entry/C44.md` | 6205 | `3d609449` | 19:27:13 | C (register-knowledge entry seats) | C fragment (register-strata knowledge entry); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-27/entry/C45.md` | 6219 | `907c6ba4` | 19:30:54 | C (register-knowledge entry seats) | C fragment (register-strata knowledge entry); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-27/entry/C46.md` | 4410 | `ea2b38dd` | 19:27:33 | C (register-knowledge entry seats) | C fragment (register-strata knowledge entry); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-27/entry/review-C41.md` | 8397 | `3e54f88b` | 19:28:54 | C (register-knowledge entry seats) | C fragment (register-strata knowledge entry); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-27/entry/review-C42.md` | 5734 | `29ffd2b3` | 19:29:21 | C (register-knowledge entry seats) | C fragment (register-strata knowledge entry); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-27/entry/review-C43.md` | 5899 | `da60096f` | 19:29:31 | C (register-knowledge entry seats) | C fragment (register-strata knowledge entry); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-27/entry/review-C44.md` | 5533 | `98dbc3ee` | 19:29:37 | C (register-knowledge entry seats) | C fragment (register-strata knowledge entry); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-27/entry/review-C45.md` | 5455 | `8484a2bb` | 19:30:47 | C (register-knowledge entry seats) | C fragment (register-strata knowledge entry); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-27/entry/review-C46.md` | 4775 | `13731e8e` | 19:30:59 | C (register-knowledge entry seats) | C fragment (register-strata knowledge entry); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-27/gate-tests/D13-argot-gate.md` | 9237 | `bccf65fe` | 19:27:19 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-27/gate-tests/D14-typed-gate.md` | 5832 | `ba24b6da` | 19:26:45 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-27/gate-tests/D15-law-negative.md` | 9930 | `0d066d1f` | 19:26:19 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-27/gate-tests/D16-syllabify-negative.md` | 9183 | `862c70b8` | 19:27:36 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-27/gate-tests/fixtures/s1-head2-unconstrained.yml` | 686 | `b503ec44` | 19:21:28 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-27/gate-tests/fixtures/s2-head2-constrained.yml` | 601 | `c3e35714` | 19:21:28 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-27/gate-tests/fixtures/s3-head2-maximal-coda.yml` | 774 | `622c054e` | 19:16:51 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-27/gate-tests/fixtures/s4-head2-prefix-reading.yml` | 642 | `0d812394` | 19:21:28 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-27/gate-tests/receipt.json` | 24951 | `cfb4f58d` | 19:27:46 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-27/gate-tests/run-gate-tests.py` | 41656 | `a3cbec8f` | 19:25:43 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-27/law/design.md` | 22728 | `9d5c1dd7` | 19:20:37 | D (register-law seats) | D fragment (register-law derivation); attributed evidence, not independently re-executed here. |
| `reports/round-27/law/impl-1.md` | 15471 | `d99af8b7` | 19:31:49 | D (register-law seats) | D fragment (register-law derivation); attributed evidence, not independently re-executed here. |
| `reports/round-27/law/impl-2.md` | 6361 | `82eb4c9a` | 19:29:29 | D (register-law seats) | D fragment (register-law derivation); attributed evidence, not independently re-executed here. |
| `reports/round-27/law/impl-3.md` | 7427 | `183ebe65` | 19:29:37 | D (register-law seats) | D fragment (register-law derivation); attributed evidence, not independently re-executed here. |
| `reports/round-27/law/impl-4.md` | 7818 | `fe7b0b18` | 19:31:45 | D (register-law seats) | D fragment (register-law derivation); attributed evidence, not independently re-executed here. |
| `reports/round-27/law/impl-5.md` | 6906 | `036df69e` | 19:29:52 | D (register-law seats) | D fragment (register-law derivation); attributed evidence, not independently re-executed here. |
| `reports/round-27/law/impl-6.md` | 5494 | `60d11b48` | 19:29:58 | D (register-law seats) | D fragment (register-law derivation); attributed evidence, not independently re-executed here. |
| `reports/round-27/law/impl-7.md` | 5651 | `46b0b4bf` | 19:30:03 | D (register-law seats) | D fragment (register-law derivation); attributed evidence, not independently re-executed here. |
| `reports/round-27/law/impl-8.md` | 8043 | `4b04d4ff` | 19:31:51 | D (register-law seats) | D fragment (register-law derivation); attributed evidence, not independently re-executed here. |
| `reports/round-27/law/review.md` | 27313 | `9a3f1071` | 19:22:35 | D (register-law seats) | D fragment (register-law derivation); attributed evidence, not independently re-executed here. |
| `reports/round-27/law/rules.md` | 17739 | `c6935957` | 19:20:12 | D (register-law seats) | D fragment (register-law derivation); attributed evidence, not independently re-executed here. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/examples/culture-d4/components/01-brief.yml` | 33067 | `649aa111` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/examples/culture-d4/components/02-phonology.yml` | 17921 | `7aa9cac5` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/examples/culture-d4/components/03-orthography.yml` | 14035 | `de1820b0` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/examples/culture-d4/components/04-lexicon.yml` | 34656 | `d0d4e17c` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/examples/culture-d4/components/05-naming.yml` | 12782 | `b154d807` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/examples/culture-d4/components/06-myth.yml` | 9406 | `2ca4935d` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/examples/culture-d4/components/07-symbolism.yml` | 7172 | `5da857dc` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/examples/culture-d4/components/08-eras.yml` | 9387 | `1c9202e3` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/examples/culture-d4/components/09-costumes.yml` | 12047 | `82fb92ad` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/examples/culture-d4/components/10-ritual-calendar.yml` | 7044 | `5a8d41b4` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/examples/culture-d4/components/11-contact-history.yml` | 6630 | `7b6932af` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/examples/culture-d4/components/12-provenance.yml` | 11496 | `540f7d22` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/examples/culture-d4/components/13-register-law.yml` | 8870 | `c0d77181` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/examples/culture-d4/packet.d4.yml` | 96555 | `86079a67` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/expected.json` | 3880 | `0029c0d7` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/tools/assemble-culture-d4.py` | 33840 | `943f487b` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/tools/assemble-d2.py` | 19955 | `8ea6bdde` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-assembly-check-gate/r27-post/tools/gates/costume-era-consistency-gate.py` | 71174 | `e6bffd70` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-typed-labels-check-gate/r27-post/examples/culture-d2/components/11-costumes.yml` | 57392 | `b6e2c5c2` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-typed-labels-check-gate/r27-post/examples/culture-d2/components/12-rank-rules.yml` | 60479 | `28696a5a` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-typed-labels-check-gate/r27-post/examples/culture-d4/packet.d4.yml` | 96555 | `86079a67` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-typed-labels-check-gate/r27-post/examples/culture-d4/typed-labels.d4.yml` | 82161 | `88a94422` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-typed-labels-check-gate/r27-post/expected.json` | 2590 | `b4c492c7` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-typed-labels-check-gate/r27-post/tools/d2-typed-labels.py` | 194937 | `2819f687` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/baselines/d4-typed-labels-check-gate/r27-post/tools/gates/costume-era-consistency-gate.py` | 71174 | `e6bffd70` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/d4-pins.json` | 6917 | `40d23916` | 19:44:43 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/frozen/r27-post/MANIFEST.tsv` | 1118 | `b5f5799e` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/frozen/r27-post/d4-assembly.out` | 73 | `c60820a5` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/frozen/r27-post/d4-typed-labels.out` | 81 | `1c8add32` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/frozen/r27-post/freeze-receipt.json` | 1313 | `fc254b03` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/frozen/r27-post/inputs/examples/culture-d4/packet.d4.yml` | 96555 | `86079a67` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/frozen/r27-post/inputs/examples/culture-d4/typed-labels.d4.yml` | 82161 | `88a94422` | 19:44:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/o37-inventory-receipt.json` | 14132 | `fb8c5387` | 19:34:34 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/o37-sweep-inventory-audit.md` | 13552 | `d1b14016` | 19:33:02 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/o38-adjudication-receipt.json` | 11575 | `0785ac28` | 19:34:20 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/o38-sweep-inventory-adjudication.md` | 14143 | `99e0e401` | 19:34:44 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/repin.py` | 16768 | `3dca4e37` | 19:44:18 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/sweep-census.md` | 4989 | `1a2c76ba` | 19:43:48 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/sweep-receipt.json` | 135822 | `905174ba` | 19:43:55 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/sweep.md` | 19814 | `e6cda3d8` | 19:44:54 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/sweep.py` | 26704 | `b956d53c` | 19:42:56 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/v3-baseline-r27/expected.json` | 10856 | `b1d065e0` | 19:44:24 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/v3-baseline-r27/freeze.txt` | 521 | `5661e183` | 19:44:24 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/v3-baseline-r27/packet.md` | 105583 | `a2b2a5fc` | 19:44:24 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/pinsweep/v3-baseline-r27/twin.json` | 103440 | `39879478` | 19:44:24 | O (pin-sweep seats) | O fragment (D4 pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-27/readme/reconcile.md` | 8353 | `154377eb` | 19:26:13 | C (corpus-README reconciliation seats) | C fragment (corpus/README reconciliation sweep); attributed evidence; the landed README is outside this subtree. |
| `reports/round-27/readme/sweep.py` | 12665 | `368bd669` | 19:13:30 | C (corpus-README reconciliation seats) | C fragment (corpus/README reconciliation sweep); attributed evidence; the landed README is outside this subtree. |
| `reports/round-27/readme/verify.md` | 9951 | `da80f226` | 19:26:17 | C (corpus-README reconciliation seats) | C fragment (corpus/README reconciliation sweep); attributed evidence; the landed README is outside this subtree. |
| `reports/round-27/report-draft.md` | 12539 | `c80b97aa` | 19:32:49 | X (scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-27/rerun.json` | 21553 | `4fbfedfa` | 19:32:39 | X (scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-27/run-validation.py` | 92131 | `48667305` | 19:43:24 | acceptance runner | Executable runner; existence is not a green end-to-end acceptance (the receipt is the verdict). |
| `reports/round-27/scope.md` | 21085 | `a632f989` | 19:17:11 | X (scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-27/scribe/capability-row.md` | 28826 | `db893d07` | 19:24:10 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-27/scribe/fragment-ledger.json` | 25741 | `e3bb54c7` | 19:26:20 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-27/scribe/fragment-ledger.md` | 22835 | `26dd6013` | 19:26:16 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-27/scribe/frozen-rows.md` | 23867 | `cbd759bd` | 19:25:01 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-27/scribe/skill-rule-row.md` | 21639 | `f784daec` | 19:25:21 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-27/scribe/x54-syllabify-spotcheck.md` | 43820 | `60786007` | 19:28:47 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-27/scribe/x54-syllabify-spotcheck.py` | 22069 | `ee370f78` | 19:21:16 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-27/scribe/x56-census.py` | 9891 | `feea8b18` | 19:37:59 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-27/scribe/x58-d4-chain-cold-rerun.md` | 42601 | `6034c99a` | 19:22:57 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-27/scribe/x64-entry-source-resolvability-cold.md` | 12632 | `6e147099` | 19:24:26 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-27/targets.json` | 191 | `04c18533` | 19:11:04 | declaration (parent) | Declared thresholds and seat allocation, not achieved outcomes. |
| `reports/round-27/validation.json` | 232081 | `9c7abac2` | 19:42:56 | acceptance runner/receipt | Primary receipt; written by the runner. Binding checked below. |
CENSUS_COUNT=125

**Census:** 125 artifacts indexed (this index file is the 126th, self-indexed
without size/sha). Excluded: `__pycache__/` (four `.pyc` files under
`reports/round-27/audit/`) and `*.log` (three: the `run.log` under each of
`pinsweep/v3-baseline-r27/`, `pinsweep/baselines/d4-assembly-check-gate/r27-post/`
and `pinsweep/baselines/d4-typed-labels-check-gate/r27-post/`). Partition shape:
`pinsweep` 45, `audit` 21, `entry` 12, `law` 11, `scribe` 10, `gate-tests` 10,
`argot` 4, `readme` 3, round root 9.

**Absent required artifacts, named:** no `reports/round-27/integration/`
directory exists at the census, so no LOG/SCORECARD integration draft is
indexed; `reports/round-27/report-draft.md` and `rerun.json` are drafts at the
round root instead. Nothing else the declaration requires is missing: the
counting command, the receipt, and the D/O/C evidence directories all exist, and
the receipt's own `missing_dependencies` reads `[]` (an earlier sample at
19:24:55Z named `reports/round-27/handoff/declared-in-r5/expected.json` as a
missing dependency; that leg now reads the round-26 `declared-in-r5` row and
reports it as a **drift**, not an absence).

## Conformance observations

1. **Declared, not achieved — and the achieved outcome is RED.** Both
   `claims.json` and `targets.json` are the parent's declaration
   (`state: declared-before-dispatch`). The receipt landed and reads
   `acceptance_checks_passed: false` with claims `{C: true, D: true, O: false}`.
   So the round is **open on O**; this index reports that verdict, it does not
   produce or contest it. The receipt is **not bound** to the live runner at the
   census (see **Availability**), so its verdict is a dated reading of the runner
   as of 19:42:56Z.

2. **O / operability — the round's red, named.** Both settled failures are on
   claim O, quoted from the receipt (19:42:56Z):
   - `claim O: replay handoff-v3 is not green (exit 1)`.
   - `claim O: Regression failed: python3 tools/exercise-handoff-e2e.py --profile
     v3 --quiet (exit 1, 2026-10-18)`.
   **This seat reproduced the second independently:** running
   `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` from the lane root
   with `TMPDIR=/tmp` returns `REAL_EXIT=1` and the line `handoff-v3: exit=1
   fields=? glossary=?/20 findings=? links=? claims=? statuses=? v2_subset=unequal
   alias_leg=? packet_sha256=(not assembled)`. The O claim's own sweep names the
   mechanism: the round-27 register-law landing moved the D4 bytes the v3
   read-set pins, and the frozen v3 baseline at
   `reports/round-26/handoff/declared-in-r5/expected.json` is now drifted
   (`declared_packet_sha256 e3fb1ca5…` vs `live_packet_sha256 86079a67…`). An
   earlier sample (19:24:55Z) carried a third O failure — one drifted D4 surface
   (`examples/culture-d4/components/01-brief.yml`) not re-pinned — which the O
   seat's later re-freeze resolved; the O failure set **moved with the runner
   revision** and the settled pair above is the one this index binds. Which of
   the two is a real defect versus a baseline-convention question is the O
   claim's and the parent's, not this index's.

3. **D / depth — the register law landed, and the syllabify fix landed, and this
   seat re-ran the gates.** The law landed as a **new component**:
   `examples/culture-d4/components/13-register-law.yml` (7 284 B, header seat
   `R27-D05..D12`), declaring `packet_keys: [register_law]` and the five law rows
   `RGL-01..RGL-05` — the round-26 finding `RD-5c`/`RL-6` ("no component owns the
   register law") now has an owner. The runner's D measurement confirms the
   landing (`component_ownership.register_law`: component and packet both carry
   `RGL-01..RGL-05`, `ids_equal: true`). The syllabify disagreement is fixed by a
   **new algorithm in the delivered gate**: `tools/gates/argot-derivation-gate.py`
   moved from `5b5abe78…` to `48667305388b1e84…`-era bytes, gaining `CODAS` and
   `ONSET_CLUSTERS = False` (quoted from `02-phonology.yml`) and a rewritten
   `syllabify` that enforces the design's legality clause (`tikmes` → `tik.mes`,
   `ker` → one syllable). **This seat re-ran three instruments read-only, from the
   lane root with `TMPDIR=/tmp`:**
   - `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml`
     → **exit 0**, `records=175 register_scoped=14 derived_pairs=8 claimed_chains=8
     borrow_pairs=6 violations=0 rule_holds=0`;
   - `python3 tools/gates/argot-derivation-gate.py --selftest` → **27/27**, exit 0;
   - `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`
     → **20/20 legs passed**.
   The runner's own D leg agrees (`claims.D.passed = true`) and its
   `syllabify_fix` controls show the gate's splits agreeing with the runner's on
   `tikmes`/`kalker`/`tumhai`/`haitun`/`saalumi`. The gate-test battery
   (`reports/round-27/gate-tests/`) carries D13–D16 with a four-fixture head2
   reading set (`s1` unconstrained → `tikme`, `s2` constrained → `tik`, `s3`
   maximal-coda → `saalum`, `s4` prefix-reading) and its receipt reads
   `failures: []`, `gaps: []`.

4. **D / depth — a peer audit names two real, un-closed D gaps.** The independent
   instrument `reports/round-27/audit/x59-register-law-negatives.py` (a different
   YAML loader and its own `reverse`/`lengthen`, no lane kernel) emits two HOLDs
   on the delivered packet: **`L6b`** — a tampered law *value* is invisible in
   every delivered gate; and **`L9`** — the `register_law` block is landed but the
   assembler `tools/assemble-culture-d4.py` declares it in neither `PACKET_KEYS`
   nor `RECORD_FIELDS`, so the block reaches the packet only through the
   component's own per-file `packet_keys` (measured: stripping an `id` from a
   `register_law` row assembles exit 0 and lands `id: None`, where the same edit
   to a `lexicon` row refuses exit 2). The `law/review.md` seat independently
   names the same class (`RL-1` the law has no replay leg; the new block is not
   declared in the schema). **The law is landed; the law is not yet enforced by a
   gate.** Reported, not adjudicated.

5. **C / coverage — both halves landed.** (a) The knowledge entry:
   `corpus/knowledge/linguistics/register-strata-attestation.md` landed
   (57 996 B at the census, sha256 `0d993a267f6beb43…`; the receipt's C
   measurement binds the same bytes), frontmatter-complete (`topic`, `gap
   filled`, `sources`, `verified-at`, `recheck`, `couples`), with the gap named
   against the partition and an absence sweep. It is authored by seats
   `R27-C41..C46` (`reports/round-27/entry/C4x.md`) and reviewed by
   `R27-C47..C52` (`reports/round-27/entry/review-C4x.md`) — twelve fragments,
   present. (b) The README revision: `corpus/README.md` is at **revision 1.7**
   (19 → 20 linguistics entries, totals 199 → 200), reconciled by
   `reports/round-27/readme/sweep.py`. **This seat re-ran the sweep and the entry
   audit:** `python3 reports/round-27/readme/sweep.py` → `rows 199 files 199` at
   the pre-entry stamp this seat sampled (`missing_from_index 0`,
   `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`, `totals_ok True`), and
   `python3 reports/round-27/audit/entry-audit.py --selftest` → **11/11 checks
   passed**, exit 0. The runner's C leg reads `linguistics_entries 19 → 20`,
   `mismatches {}`, `total_files 200`, `claims.C.passed = true`. Two independent
   C legs (X63's Python instrument and X64's cold `sha256sum`/`grep`/`test -e`
   re-derivation) are indexed.

6. **The syllabify disagreement is a *moving* quantity, and the review says so.**
   The round-27 `law/review.md` seat (`RL-5`) re-measured the round-26 "15 of 62"
   figure and reports it is **reader-dependent**: 0 of 70 under a naive
   maximal-onset reader, 8 of 70 under the design's legality-checking reading,
   15 of 62 under round 26's reading — a third reading the review could not
   reproduce. The `scribe/x54-syllabify-spotcheck.py` seat adds a **third,
   author-declared** witness (the packet's own `syllables:` field on the 8 `names`
   records), which the entry's own `sources` records as agreeing **8/8** with the
   design's algorithm and **0/8** with the old gate. This index records that the
   fix landed and that its correctness is measured against a stated predicate,
   not that "15 of 62" was ever a stable defect count.

7. **Cross-round coexistence (disclosed).** Seat `R27-D24`'s
   `scribe/fragment-ledger.{json,md}` is a second read-time census of this
   subtree, taken at its own earlier stamp (its file landed 19:2xZ); it will
   differ from this census in count because the wave kept writing. Both are
   indexed; a divergence is a parent reconciliation item.

8. **The parent integrates.** No `reports/round-27/integration/` directory exists
   at the census; `report-draft.md` and `rerun.json` are drafts at the round root.
   Filing, scope, integration into `LOG.md`/`SCORECARD.md`, the O-claim re-run,
   and any final promotion verification remain parent responsibilities; in-lane
   attestations do not prove a fresh external inspection.

## Index verification

Reproducible coverage control over the table above. The generator
`reports/round-27/scribe/x56-census.py` walks the subtree; this block re-checks
that the index rows and the live tree agree on **digest**, and that the
availability/binding markers are current. Extract and run from the lane root:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-27/scribe/x56-census.py --selftest   # 15/15 in-memory
python3 -B reports/round-27/scribe/x56-census.py              # regenerate the table
```

```sh
python3 - <<'PY'
import datetime, hashlib, re
from pathlib import Path
BASE = Path('reports/round-27')
SELF = BASE / 'fragment-index-x56.md'
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
assert not conforms(pairs + [('reports/round-27/__X56_nonexistent__.md', 1, '0' * 8)]), 'missing-path negative missed'
tampered = [(p, s, ('00000000' if h != '00000000' else '11111111')) for p, s, h in pairs]
assert not conforms(tampered), 'tampered-sha negative missed'
assert text.endswith('\n') and '\0' not in text
assert all(line == line.rstrip() for line in text.splitlines()), 'trailing whitespace'
assert len(re.findall(r'^```[^\n]*$', text, re.M)) % 2 == 0, 'unbalanced fences'
print('INDEX_CONTROL=PASS; duplicate/missing/tampered negatives rejected; markers current')
PY
```

The generator's `--selftest` is 15 in-memory checks (exit 0), including the
negative controls: an unknown path must classify `unassigned` (never guessed), a
runner row must not read as green, and the self row must be excluded.

**Standing caveat.** The wave was live at the census (a 41-writes-per-minute tail
at 19:45:04Z), and the receipt does **not** bind the live runner at the census
(runner mtime 19:43:24Z > receipt 19:42:56Z), so this reading is a dated snapshot
and the verdict is a reading of the runner as of 19:42:56Z. The census was taken
twice more inside this seat's window (19:38:02Z, 19:43:59Z, 19:45:06Z) and the
count moved 120 → 125 as the O seat re-froze its pin baselines. A later arrival,
a further runner edit, or a re-run of the counting command invalidates this
reading and requires a dated refresh. The round-25 X44 index's control caught
exactly this class of drift on its own receipt; this index discloses the same
hazard, and here the drift is **real and observed** (the receipt was bound at
19:36:13Z and unbound by 19:43:59Z).

## Boundary record

- **Writes:** this file and its instrument `reports/round-27/scribe/x56-census.py`
  (plus the gitignored generator `.scratch/x56/gen-index.py` and scratch under
  `.scratch/x56/`). No `reports/round-{8..26}` byte was touched, no tool or gate
  was edited, and no shared bookkeeping (`LOG.md`, `SCORECARD.md`) was appended.
  `export TMPDIR=$PWD/.scratch` preceded every scratch-writing command; read-only
  gate runs used `TMPDIR=/tmp`. No commit, no push.
- **Independence:** the census table was re-derived from the live bytes by
  `reports/round-27/scribe/x56-census.py`, not transcribed from the D24 ledger.
  The three gate re-runs in observation 3 and the `exercise-handoff-e2e` re-run
  in observation 2 were executed by this seat in its own shell. Where this index
  and a sibling fragment agree on a digest, the agreement is a cross-check, not
  inheritance.
- **Canon:** NON-CANON engineering evidence. This index admits nothing, certifies
  no round and adjudicates no claim.
