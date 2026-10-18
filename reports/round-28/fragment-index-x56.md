# R28-X56 — fragment index + conformance

Seat **R28-X56** (scribe: fragment index + conformance) for round 28 (operator:
loop 3 of 3, **build round 4 of 4 — the last build round**; 64 workers on
`devin/deepseek-v4-1-flash-high`). Axes watched: **D / depth** (the register
law's replay leg + the RL-4 `packet_keys` fix), **O / operability** (the final
pin sweep + regressions), **C / coverage** (the RL-3 ceiling as craft knowledge).
Declaration: `reports/round-28/claims.json` (baseline
`6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede`, the round-27 admit); seat allocation:
`reports/round-28/targets.json` (D-law-replay 28, O-sweep 16, C-ceiling 10, X 10 =
64). Lane HEAD at this index's census: `69cecbc`.

This is the assigned X56 index — an availability read plus a presence/conformance
census. It is **not** a round-admission receipt, not a verdict replay, and not an
independent promotion review. The round's own counting command is
`python3 reports/round-28/run-validation.py`; the round's verdict is
`reports/round-28/validation.json`, which is indexed here, not adjudicated here.
No round validator was executed by this seat; no filed rounds 8–27 artifact was
read as writable, and none was modified.

**Filing note.** This index files at the round root
`reports/round-28/fragment-index-x56.md`. Seat **R28-D24** files
`reports/round-28/scribe/fragment-ledger.{json,md}`, a read-time census of the
same subtree that calls itself the integration ledger; the paths do not collide,
but the roles overlap. Both are indexed here; neither settles the other, and a
divergence between the two tables is a parent reconciliation item, not a verdict.
The round-27 precedent (`fragment-index-x56.md`, same seat name, same form) is the
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
  rows (the `ceiling/` partition and the round-root `regression.md` were added to
  the classifier during the seat's own window, before the census; see **Index
  verification**).
- Counts carry their command and date; quotations name their location; a missing
  required artifact is named, never inferred.

## Availability (at the census stamp)

- Census: **2026-10-18T20:47:50Z** (command: `python3 -B
  reports/round-28/scribe/x56-census.py`; `__pycache__/`, `*.pyc`, `*.log`
  excluded; this index file is the self row, written after the census, never
  self-measured). Census count: **130** artifacts plus this index (3 800 327 B,
  76 933 lines). Raw walk: 136 files, minus 3 `__pycache__/*.pyc` and 3 `*.log`.
- **Counting command** `reports/round-28/run-validation.py` — **present** at
  census (108 915 B, sha256
  `20e09ea8db7bcb306b0c8948c7b8afb62eca5e0d47f674ebfea9643f2f6add77`, mtime
  20:28:26Z).
- **Runner receipt** `reports/round-28/validation.json` — **present** at census
  (245 834 B, sha256 prefix `37842da3`, mtime 20:36:46Z). It reads
  `measured_at_utc: 2026-10-18T20:36:46+00:00`,
  `acceptance_checks_passed: **true**`, **0** failures, claims
  `{C: true, D: true, O: true}`, `missing_dependencies: []`. **The round reads
  admitted by its own receipt** — but see the binding and stamp caveats below,
  which are the substance of this section.
- Marker line for the control: `runner_present_at_census=Y` and
  `receipt_present_at_census=Y` and `binding_ok_at_census=Y`.
- **Binding check (the round-20 lesson).** The receipt's `runner_sha256` is
  `20e09ea8db7bcb306b0c8948c7b8afb62eca5e0d47f674ebfea9643f2f6add77`; the live
  `reports/round-28/run-validation.py` hashes
  `20e09ea8db7bcb306b0c8948c7b8afb62eca5e0d47f674ebfea9643f2f6add77` at the
  census — **the receipt DOES bind the live runner bytes**, so its `true` verdict
  is a reading of the runner that is on disk now, not a superseded snapshot.
  **This reading took three samples to settle, and the drift is disclosed rather
  than hidden:**
  - 20:25:44Z — receipt 242 900 B / runner declared `b8f08546…`, live runner
    `7310a945…`: **NOT bound**; `acceptance_checks_passed: false`, 13 failures,
    `missing_dependencies: ["reports/round-28/pinsweep/v3-baseline-r28/expected.json"]`.
  - 20:28:26Z — the live runner was rewritten (`7310a945…` → `20e09ea8…`).
  - 20:36:46Z — receipt 245 834 B / `37842da3`, declaring runner `20e09ea8…`,
    which **is** the live runner: bound, `true`, 0 failures, 0 missing.
  A further runner edit or a re-run of the counting command invalidates this and
  needs a dated refresh. The verdict moved **false → true** inside this seat's
  window; both readings carry their stamp and both are reported.
- **Wave shape.** The wave was **live at dispatch and for most of the seat's
  window**, then settled. The round-28 tree grew **2 → 8 → 29 → 74 → 93 → 119 →
  130 → 131 → 133** files between 20:10:20Z and 20:42Z; it went quiescent from
  **20:42:58Z** (zero writes in the 60 s before each of four consecutive samples
  at 20:43:53Z, 20:44:48Z, 20:45:43Z and 20:46:11Z) and stayed quiescent through
  the census. Two files arrived at 20:41:35Z (`report-draft.md`) and 20:39:39Z
  (`scribe/x58-d4-chain-cold-rerun.md`) as the tail closed. **The census was
  taken on a settled tree**, which is the round-26 X54 situation rather than the
  round-27 X56 live-wave one; a file arriving after this stamp still needs a
  dated refresh, not an inferred worker failure.
- **Protected surface** (rounds 8–27, `git status --porcelain=v1` over
  `reports/round-{8..27}` **plus** `tools/gates/frozen/round-{8..27}` at the
  census): **clean** — 0 rows. The round-28 runner's own
  `protected_filed_artifacts` leg agrees (`passed: true`, **1 587** protected
  paths, `differences: []`, `differences_total 0`, `protected_status_rows 0`,
  `missing_dependencies: []`). **One transient breach is disclosed by two peer
  seats and confirmed by this seat's `git` read:** a filed round-27 artifact,
  `reports/round-27/gate-tests/receipt.json`, was rewritten in place at
  20:13:21Z (its verdict flipped `passed: true, 55/55` → `passed: false, 42/55`)
  and restored to its baseline blob by 20:14:42Z — see **Conformance
  observation 8**. At this census the path is byte-clean and the only residue is
  its post-dispatch mtime.
- **Fleet root** `/home/vgpnk/Projects/shokunin`: four untracked/modified entries
  — the gitignored `.scratch/`, a pre-existing `M .ufo/l0-questions.md`, an
  `M MANIFEST.json`, and `?? .ufo/reports/round-101/game-dev-2d.md`, all outside
  this lane. The round-28 scope seat (`reports/round-28/scope.md`) reports the
  assignment's "fleet root clean" clause as **failing as observed** and names
  four debris families, three of them byte- and mtime-identical to the round-27
  record and the fourth (`.ufo/l0-questions.md`) **growing inside the round-28
  window** (a second appended line, mtime 20:14:10Z). Disclosed here, not
  dispositioned; none is a kotodama filed artifact.

## Census

Read-time census of `reports/round-28/**` at **2026-10-18T20:47:50Z** (command:
`python3 -B reports/round-28/scribe/x56-census.py`, sha8 digests via
`hashlib.sha256`; see **Index verification** for the reproducible coverage
control). Files under `__pycache__/` and `*.log` are excluded. **The tree was
quiescent at the census** (zero writes in the 60 s before each of the five
preceding samples); a file arriving after it needs a dated refresh. Counts are
artifact counts, not worker counts. Owner inference is directory/name based.

| artifact | bytes | sha8 | mtime UTC | inferred owner | conformance state / limit |
|---|---:|---|---|---|---|
| `reports/round-28/adjacency.md` | 44110 | `d91634ec` | 20:16:11 | X (adjacency/scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-28/argot/D17-law-bypass.md` | 37609 | `ca353a05` | 20:21:51 | D (law-replay / packet_keys seats) | D fragment (law-replay derivation); attributed evidence, not independently re-executed here. |
| `reports/round-28/argot/D18-force-overmatch.md` | 25584 | `4238041a` | 20:21:51 | D (law-replay / packet_keys seats) | D fragment (law-replay derivation); attributed evidence, not independently re-executed here. |
| `reports/round-28/argot/D19-ab-crosscheck.md` | 21264 | `b4d47a6e` | 20:17:12 | D (law-replay / packet_keys seats) | D fragment (law-replay derivation); attributed evidence, not independently re-executed here. |
| `reports/round-28/argot/D20-ceiling-wording.md` | 30828 | `8a037288` | 20:20:28 | D (law-replay / packet_keys seats) | D fragment (law-replay derivation); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/entry-audit.py` | 13017 | `918a0c1e` | 20:20:45 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/o37-inventory-receipt.json` | 150220 | `ad1b1419` | 20:31:59 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/o37-sweep-inventory-audit.md` | 17215 | `588b1a2f` | 20:30:11 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/o37-sweep-inventory-audit.py` | 33185 | `b256da77` | 20:24:59 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/o38-adjudication-receipt.json` | 21901 | `73c5d6c8` | 20:32:10 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/o38-sweep-inventory-adjudication.md` | 12905 | `9aa393ab` | 20:28:10 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/o38-sweep-inventory-adjudication.py` | 28158 | `73fb7d5b` | 20:27:21 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/o39-o40-law-replay-and-sweep-adversarial.md` | 27996 | `e7bb25b0` | 20:30:17 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x-c48-entry-audit.md` | 7988 | `244c92f6` | 20:21:24 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x57-lessons-audit.md` | 30241 | `b0950bf4` | 20:18:48 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x57-lessons-audit.py` | 50540 | `4f19f9e3` | 20:16:37 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x57-lessons-live.txt` | 2952 | `f2a2a9b2` | 20:18:27 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x57-lessons-receipt.json` | 17432 | `878ab09a` | 20:18:24 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x57-lessons-selftest.json` | 7744 | `c4da75a4` | 20:18:25 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x59-register-law-negatives.md` | 16843 | `67a75d23` | 20:23:33 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x59-register-law-negatives.py` | 38945 | `a4482c9c` | 20:15:19 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x60-sweep-completeness.md` | 15006 | `8e4bc190` | 20:23:28 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x60-sweep-completeness.py` | 22568 | `81afd19d` | 20:14:46 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x61-pin-sweep.md` | 17213 | `4164b600` | 20:18:34 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x61-pin-sweep.py` | 37705 | `12add076` | 20:18:06 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x62-frozen-record-audit.md` | 16932 | `2db32da8` | 20:19:24 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x62-frozen-record-audit.py` | 35260 | `e7ca8f99` | 20:19:29 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x63-entry-source-resolvability.md` | 17563 | `44c00773` | 20:29:28 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x63-entry-source-resolvability.py` | 54831 | `efbc86fe` | 20:24:07 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x64-cold-rerun.md` | 12596 | `3da6a2cc` | 20:30:08 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/audit/x64-cold-rerun.py` | 27283 | `f6cdd1f4` | 20:24:44 | auditors (X5x/X6x) | Audit fragment (read-only tool/report/receipt); attributed evidence, not independently re-executed here. |
| `reports/round-28/availability.json` | 35597 | `aceb019c` | 20:14:38 | X (availability seat) | Availability record; a route/liveness measurement, not acceptance. |
| `reports/round-28/ceiling/C41.md` | 10187 | `ef5bff80` | 20:25:53 | C (ceiling-knowledge entry seats) | C fragment (register-lexicon ceiling knowledge); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-28/ceiling/C42.md` | 7225 | `96ad8d26` | 20:24:52 | C (ceiling-knowledge entry seats) | C fragment (register-lexicon ceiling knowledge); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-28/ceiling/C43.md` | 6504 | `6e3ecb6d` | 20:24:52 | C (ceiling-knowledge entry seats) | C fragment (register-lexicon ceiling knowledge); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-28/ceiling/C44.md` | 5981 | `3fe94791` | 20:23:15 | C (ceiling-knowledge entry seats) | C fragment (register-lexicon ceiling knowledge); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-28/ceiling/C45.md` | 6345 | `f17b109b` | 20:21:46 | C (ceiling-knowledge entry seats) | C fragment (register-lexicon ceiling knowledge); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-28/ceiling/C46.md` | 6172 | `1e003462` | 20:21:51 | C (ceiling-knowledge entry seats) | C fragment (register-lexicon ceiling knowledge); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-28/ceiling/measure-ceiling.py` | 12571 | `ff1a7f24` | 20:19:12 | C (ceiling-knowledge entry seats) | C fragment (register-lexicon ceiling knowledge); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-28/ceiling/review-C41.md` | 4778 | `680cb038` | 20:24:48 | C (ceiling-knowledge entry seats) | C fragment (register-lexicon ceiling knowledge); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-28/ceiling/review-C42.md` | 7591 | `57e8c1ca` | 20:24:52 | C (ceiling-knowledge entry seats) | C fragment (register-lexicon ceiling knowledge); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-28/ceiling/review-C43.md` | 4599 | `37fca94f` | 20:24:52 | C (ceiling-knowledge entry seats) | C fragment (register-lexicon ceiling knowledge); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-28/ceiling/review-C44.md` | 6181 | `62e76925` | 20:23:25 | C (ceiling-knowledge entry seats) | C fragment (register-lexicon ceiling knowledge); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-28/ceiling/review-C45.md` | 4985 | `5e821f5a` | 20:23:32 | C (ceiling-knowledge entry seats) | C fragment (register-lexicon ceiling knowledge); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-28/ceiling/review-C46.md` | 5787 | `70087bd5` | 20:23:37 | C (ceiling-knowledge entry seats) | C fragment (register-lexicon ceiling knowledge); attributed evidence; the landed corpus entry is outside this subtree. |
| `reports/round-28/claims.json` | 2453 | `c1a4ea22` | 20:10:20 | declaration (parent) | Declared thresholds and seat allocation, not achieved outcomes. |
| `reports/round-28/gate-tests/D13-argot-gate.md` | 6295 | `c130304a` | 20:24:52 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-28/gate-tests/D14-typed-gate.md` | 5707 | `f28a4401` | 20:23:26 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-28/gate-tests/D15-law-negative.md` | 9326 | `e49f8943` | 20:23:34 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-28/gate-tests/D16-rl4-fix.md` | 7107 | `1b7dea6c` | 20:25:03 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-28/gate-tests/receipt.json` | 31360 | `af374a41` | 20:27:36 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-28/gate-tests/run-gate-tests.py` | 55285 | `47f74b9a` | 20:21:50 | D/O (gate test fixtures + runner) | Gate negative/positive fixture set + its runner/receipt; attributed evidence, not re-executed here. |
| `reports/round-28/law/design.md` | 31226 | `e0a59168` | 20:21:07 | D (law-replay / packet_keys seats) | D fragment (law-replay derivation); attributed evidence, not independently re-executed here. |
| `reports/round-28/law/impl-1.md` | 10347 | `2ad9b2ff` | 20:26:47 | D (law-replay / packet_keys seats) | D fragment (law-replay derivation); attributed evidence, not independently re-executed here. |
| `reports/round-28/law/impl-2.md` | 7945 | `5418d6c6` | 20:26:47 | D (law-replay / packet_keys seats) | D fragment (law-replay derivation); attributed evidence, not independently re-executed here. |
| `reports/round-28/law/impl-3.md` | 7076 | `830d3bc0` | 20:26:47 | D (law-replay / packet_keys seats) | D fragment (law-replay derivation); attributed evidence, not independently re-executed here. |
| `reports/round-28/law/impl-4.md` | 6632 | `98e9b4a9` | 20:24:57 | D (law-replay / packet_keys seats) | D fragment (law-replay derivation); attributed evidence, not independently re-executed here. |
| `reports/round-28/law/impl-5.md` | 6506 | `1d67bd00` | 20:25:02 | D (law-replay / packet_keys seats) | D fragment (law-replay derivation); attributed evidence, not independently re-executed here. |
| `reports/round-28/law/impl-6.md` | 6368 | `969e9b05` | 20:25:09 | D (law-replay / packet_keys seats) | D fragment (law-replay derivation); attributed evidence, not independently re-executed here. |
| `reports/round-28/law/impl-7.md` | 7187 | `5322206d` | 20:25:15 | D (law-replay / packet_keys seats) | D fragment (law-replay derivation); attributed evidence, not independently re-executed here. |
| `reports/round-28/law/impl-8.md` | 9116 | `6fdfb557` | 20:26:47 | D (law-replay / packet_keys seats) | D fragment (law-replay derivation); attributed evidence, not independently re-executed here. |
| `reports/round-28/law/review.md` | 19079 | `13917fb5` | 20:21:09 | D (law-replay / packet_keys seats) | D fragment (law-replay derivation); attributed evidence, not independently re-executed here. |
| `reports/round-28/law/rl4-delta.md` | 18269 | `6e3dbb4a` | 20:17:04 | D (law-replay / packet_keys seats) | D fragment (law-replay derivation); attributed evidence, not independently re-executed here. |
| `reports/round-28/law/vocab.md` | 19436 | `cc8a9a31` | 20:16:20 | D (law-replay / packet_keys seats) | D fragment (law-replay derivation); attributed evidence, not independently re-executed here. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/examples/culture-d4/components/01-brief.yml` | 33067 | `649aa111` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/examples/culture-d4/components/02-phonology.yml` | 17921 | `7aa9cac5` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/examples/culture-d4/components/03-orthography.yml` | 14989 | `0f2ff454` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/examples/culture-d4/components/04-lexicon.yml` | 34656 | `d0d4e17c` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/examples/culture-d4/components/05-naming.yml` | 12782 | `b154d807` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/examples/culture-d4/components/06-myth.yml` | 9406 | `2ca4935d` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/examples/culture-d4/components/07-symbolism.yml` | 7172 | `5da857dc` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/examples/culture-d4/components/08-eras.yml` | 9387 | `1c9202e3` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/examples/culture-d4/components/09-costumes.yml` | 12535 | `f61cc684` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/examples/culture-d4/components/10-ritual-calendar.yml` | 7044 | `5a8d41b4` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/examples/culture-d4/components/11-contact-history.yml` | 6630 | `7b6932af` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/examples/culture-d4/components/12-provenance.yml` | 11496 | `540f7d22` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/examples/culture-d4/components/13-register-law.yml` | 8870 | `c0d77181` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/examples/culture-d4/packet.d4.yml` | 98841 | `543d68a8` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/expected.json` | 3971 | `e30f303d` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/tools/assemble-culture-d4.py` | 33840 | `943f487b` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/tools/assemble-d2.py` | 19955 | `8ea6bdde` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-assembly-check-gate/r28-post/tools/gates/costume-era-consistency-gate.py` | 71174 | `e6bffd70` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-typed-labels-check-gate/r28-post/examples/culture-d2/components/11-costumes.yml` | 57392 | `b6e2c5c2` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-typed-labels-check-gate/r28-post/examples/culture-d2/components/12-rank-rules.yml` | 60479 | `28696a5a` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-typed-labels-check-gate/r28-post/examples/culture-d4/packet.d4.yml` | 98841 | `543d68a8` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-typed-labels-check-gate/r28-post/examples/culture-d4/typed-labels.d4.yml` | 82161 | `339bfd83` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-typed-labels-check-gate/r28-post/expected.json` | 2681 | `eba2f034` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-typed-labels-check-gate/r28-post/tools/d2-typed-labels.py` | 194937 | `2819f687` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/baselines/d4-typed-labels-check-gate/r28-post/tools/gates/costume-era-consistency-gate.py` | 71174 | `e6bffd70` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/d4-pins.json` | 18158 | `552fc7bd` | 20:31:29 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/frozen/r28-post/MANIFEST.tsv` | 2105 | `eac71388` | 20:30:59 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/frozen/r28-post/d4-assembly.out` | 73 | `c60820a5` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/frozen/r28-post/d4-source.out` | 2213 | `14d0d806` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/frozen/r28-post/d4-typed-labels.out` | 81 | `1c8add32` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/frozen/r28-post/d4-typed.out` | 2140 | `1f00abac` | 20:30:59 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/frozen/r28-post/freeze-receipt.json` | 2027 | `2f80d53f` | 20:30:59 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/frozen/r28-post/inputs/examples/culture-d4/packet.d4.typed.yml` | 105200 | `15c81ec1` | 20:30:59 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/frozen/r28-post/inputs/examples/culture-d4/packet.d4.yml` | 98841 | `543d68a8` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/frozen/r28-post/inputs/examples/culture-d4/typed-labels.d4.yml` | 82161 | `339bfd83` | 20:30:58 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/v3-baseline-r28/expected.json` | 10856 | `b3b21b44` | 20:31:06 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/v3-baseline-r28/freeze.txt` | 521 | `6c1899e7` | 20:31:06 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/v3-baseline-r28/packet.md` | 105585 | `a20ae059` | 20:31:06 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/pinsweep/v3-baseline-r28/twin.json` | 103544 | `247d863b` | 20:31:06 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/readme/reconcile.md` | 10636 | `ac25dbeb` | 20:23:38 | C (corpus-README reconciliation seats) | C fragment (corpus/README reconciliation sweep); attributed evidence; the landed README is outside this subtree. |
| `reports/round-28/readme/sweep.py` | 17117 | `9b2ccac0` | 20:12:13 | C (corpus-README reconciliation seats) | C fragment (corpus/README reconciliation sweep); attributed evidence; the landed README is outside this subtree. |
| `reports/round-28/readme/verify.md` | 5886 | `5884e86b` | 20:22:29 | C (corpus-README reconciliation seats) | C fragment (corpus/README reconciliation sweep); attributed evidence; the landed README is outside this subtree. |
| `reports/round-28/regression.md` | 20565 | `aada880f` | 20:38:34 | O (regression / handoff seats) | O fragment (regression battery / handoff baseline); attributed evidence. |
| `reports/round-28/report-draft.md` | 13740 | `7b28c5c7` | 20:41:35 | X (scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-28/rerun.json` | 23174 | `8118bf5b` | 20:41:25 | X (scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-28/run-validation.py` | 108915 | `20e09ea8` | 20:28:26 | acceptance runner | Executable runner; existence is not a green end-to-end acceptance (the receipt is the verdict). |
| `reports/round-28/scope.md` | 32811 | `f61b462c` | 20:19:31 | X (scribe seats) | Presence recorded; not independently re-executed here. |
| `reports/round-28/scribe/capability-row.md` | 37591 | `9096a493` | 20:32:20 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-28/scribe/fragment-ledger.json` | 38371 | `2f7d987d` | 20:31:09 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-28/scribe/fragment-ledger.md` | 27588 | `a4bc5640` | 20:35:56 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-28/scribe/frozen-rows.md` | 27965 | `42880232` | 20:34:51 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-28/scribe/skill-rule-row.md` | 18986 | `de60cb7a` | 20:19:29 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-28/scribe/x54-law-negatives-spotcheck.md` | 19189 | `10fedbb2` | 20:18:32 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-28/scribe/x54-law-negatives-spotcheck.py` | 36191 | `4dbb4132` | 20:16:56 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-28/scribe/x56-census.py` | 11086 | `b9c0b7e5` | 20:47:49 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-28/scribe/x58-d4-chain-cold-rerun.md` | 46941 | `7bb2bb51` | 20:39:39 | X (scribe seats) | X scribe fragment; attributed evidence. |
| `reports/round-28/sweep/poll-d-landing.py` | 2782 | `21512276` | 20:17:16 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/sweep/repin-rows.json` | 15747 | `ee588875` | 20:31:29 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/sweep/repin.py` | 24155 | `899e61f2` | 20:26:20 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/sweep/sweep-census.md` | 6049 | `b3d0ad68` | 20:29:32 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/sweep/sweep-receipt.json` | 155139 | `dea0113c` | 20:29:39 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/sweep/sweep-selftest.json` | 2245 | `421a4de9` | 20:29:42 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/sweep/sweep.md` | 19732 | `7210231a` | 20:29:56 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/sweep/sweep.py` | 31938 | `2b2dd31d` | 20:25:00 | O (pin-sweep seats) | O fragment (final pin sweep / new pin row); attributed evidence; a pin is a measurement, not a claim. |
| `reports/round-28/targets.json` | 191 | `040e3511` | 20:10:20 | declaration (parent) | Declared thresholds and seat allocation, not achieved outcomes. |
| `reports/round-28/validation.json` | 245834 | `37842da3` | 20:36:46 | acceptance runner/receipt | Primary receipt; written by the runner. Binding checked below. |
CENSUS_COUNT=130

**Census:** 130 artifacts indexed (this index file is the 131st, self-indexed
without size/sha). Excluded: `__pycache__/` (three `.pyc` files under
`reports/round-28/audit/`) and `*.log` (three: the `run.log` under each of
`pinsweep/v3-baseline-r28/`,
`pinsweep/baselines/d4-assembly-check-gate/r28-post/` and
`pinsweep/baselines/d4-typed-labels-check-gate/r28-post/`). Partition shape:
`pinsweep` 39, `audit` 26, `ceiling` 13, `law` 12, `scribe` 9, `sweep` 8,
`gate-tests` 6, `argot` 4, `readme` 3, round root 10. By inferred owner:
O (pin-sweep) 47, auditors 26, D (law-replay/packet_keys) 16, C (ceiling entry)
13, X (scribe) 12, D/O (gate tests) 6, C (README reconciliation) 3,
declaration 2, X (adjacency) 1, X (availability) 1, O (regression) 1,
acceptance runner 1, acceptance runner/receipt 1.

**Absent required artifacts, named:** no `reports/round-28/integration/`
directory exists at the census, so no LOG/SCORECARD integration draft is
indexed; `reports/round-28/report-draft.md` and `rerun.json` are drafts at the
round root instead. Nothing else the declaration requires is missing: the
counting command, the receipt, and the D/O/C evidence directories all exist, and
the receipt's own `missing_dependencies` reads `[]` (an earlier sample at
20:25:44Z named `reports/round-28/pinsweep/v3-baseline-r28/expected.json` as a
missing dependency; that row has since landed — 10 856 B at 20:31:06Z — and the
leg reads green).

## Conformance observations

1. **Declared, then achieved — and the achieved outcome is GREEN, bound.** Both
   `claims.json` and `targets.json` are the parent's declaration
   (`state: declared-before-dispatch`). The receipt landed and reads
   `acceptance_checks_passed: true` with claims `{C: true, D: true, O: true}` and
   **zero** failures, and at the census it **binds** the live runner
   (`20e09ea8…` = live `20e09ea8…`). So the round reads admitted on its own
   instrument. This index reports that verdict; it does not produce or contest
   it. The verdict moved inside the window (see **Availability**): it was
   `false` with 13 failures at 20:25:44Z and `true` with 0 at 20:36:46Z, the
   movement being the D/O seats landing, not a defect.

2. **D / depth — the replay leg landed, and this seat reproduced its teeth and
   its one un-closed resolution.** The law now has a delivered checking leg:
   `tools/gates/register-law-gate.py` (new file this round). **This seat ran it
   read-only, from the lane root with `TMPDIR=/tmp`, on the delivered packet and
   on three tampered copies this seat wrote itself under `.scratch/x56/tamper/`**
   (the runner grades the same class of control; this seat's copies are its own):
   - clean packet → exit **1**, `law_rows=5 identity_rows=4 record_ids=179
     registers=9 speaker_tokens=3 force_failures=0 consequence_failures=0
     dangling=4 findings=4` — four `D4L-LAW-DANGLING` HOLDs, all on
     `design_row` tokens `QREG-05..08` that no delivered record carries;
   - `force: "no-such-force"` on RGL-01 → **5** findings, adding
     `D4L-LAW-FORCE: FAIL`, exit 1 — **the round-27 RL-1 probe is now closed for
     `force`**;
   - `consequence: "nothing happens"` on RGL-01 → **5** findings, adding
     `D4L-LAW-CONSEQUENCE: FAIL`, exit 1 — closed for `consequence`;
   - `speaker: "no-such-speaker"` on RGL-02 → **4** findings, **byte-identical
     to the clean run** — **NOT closed for the speaker *class*.** This seat's
     reading agrees with the independent adversarial audit
     (`reports/round-28/audit/o39-o40-law-replay-and-sweep-adversarial.md` §3,
     which names the same 4-vs-4) and with the law seat's own `law/review.md`.
     The claim's `after_required` wording ("speaker classes resolve against
     delivered records") is **stronger than the delivered code**: the leg
     resolves `Name (ID)` tokens, not bare speaker classes.
   The `D4L-LAW-*` class exists in three delivered producers
   (`tools/gates/register-law-gate.py`, `reports/round-28/gate-tests/run-gate-tests.py`,
   `reports/round-28/scribe/x54-law-negatives-spotcheck.py`) where round 27 had
   none. The delivered gates are green where the claim names them:
   `argot-derivation-gate.py` on the packet → exit 0 (`records=183
   register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6
   violations=0 rule_holds=0`), its `--selftest` → **27/27** exit 0,
   `typed-pipeline-gate.py` → **20/20 legs** exit 0 (all three re-run by this
   seat). The gate-test battery is **57/57 checks, 0 failures, 0 gaps** (its own
   receipt), and it carries three law plants whose verdicts name the added
   finding (`law_plants[force].verdicts` → `added_named: ["D4L-LAW-FORCE"]`).
   **The law leg itself is not green on the delivered packet** (exit 1, four
   HOLDs) — a standing, disclosed condition the claim's wording does not cover.

3. **D / depth — RL-4 landed, measured two ways.** Both components now declare
   `packet_keys`: `03-orthography.yml` → `[orthography, records,
   literacy_institutions]`, `09-costumes.yml` → `[costumes, materials,
   cloth_sources, rank_rules, form_slots, enforcement]`. **This seat read the
   packet directly:** all eight ids `OR-01..03`, `LI-01..03`, `EN-01..02` are
   present exactly once (`grep -c` on each → 1), and the four blocks
   (`records:`, `literacy_institutions:`, `enforcement:`, `register_law:`) exist
   at `examples/culture-d4/packet.d4.yml:2628..2710`. Records moved **175 → 183**
   and the assembly `skipped_keys` ledger is empty for these blocks. The runner's
   `rl4` leg agrees (`records_absent: []`, `still_skipped: {}`), as does the peer
   audit `audit/x59-register-law-negatives.md` (`rl4_ids_missing=0`). **Two
   sibling blocks still do not reach the packet** (`signs` 20 rows,
   `orthography_rules` 7) — disclosed by the D seat's `law/rl4-delta.md`, not a
   defect against the claim's named eight. **A distinct standing HOLD survives:**
   the `register_law` block is declared in neither `PACKET_KEYS` nor
   `RECORD_FIELDS` in `tools/assemble-culture-d4.py` (round-27 X59's `L9`,
   unchanged); the block reaches the packet only through the component's own
   `packet_keys`.

4. **O / operability — the final pin sweep is complete and the replays are
   green, and this seat re-ran the replays.** The sweep enumerated **121
   surfaces across 10 families, 39 findings**, and re-pinned **8 drifted D4
   surfaces** as NEW rows (`pinsweep/baselines/**/r28-post/`,
   `pinsweep/frozen/r28-post/`, `pinsweep/v3-baseline-r28/`), each verifying
   green; `sweep/repin-rows.json` carries the structured surface → live-digest
   rows (65 rows in the runner's own count). **This seat re-ran, read-only, with
   `TMPDIR=/tmp`:**
   - `python3 tools/check-gate-battery.py` → exit **0**, `9/9` coverage,
     `pass 7 / fail 0 / unevaluable 0`;
   - `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit **0**,
     `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27
     statuses=16/7/4 v2_subset=equal alias_leg=landed
     packet_sha256=a20ae059aa7cac9e28345d1a80a4dae3fa302117e26b5b1405f05b38d12f0001`;
   - `--profile v3 --selftest` → exit **0**.
   The v3 handoff baseline is a **new successor row**
   (`pinsweep/v3-baseline-r28/expected.json`, 10 856 B) and the tool's own
   `V3_BASELINE_DEFAULT` was re-pointed to it; the runner's `v3_successor_replays`
   records exactly that one row green, and `unrepinned_surfaces: []`. The
   battery's `pass 7` against `gates_registered 9` is the tool's own disclosed
   shape (two registered gates ship no `--selftest` leg), not a failure.

5. **O / operability — a real, disclosed instrument caveat this seat found and
   reproduced.** `python3 reports/round-28/sweep/sweep.py --selftest` is
   **TMPDIR-sensitive**: with `TMPDIR=$PWD/.scratch` (the assignment's own
   scratch convention, and *inside* the lane) it reads
   **10/12 controls passed** — its own `selftest-tmpdir-outside-repo` control
   fails (`root=…/.scratch/r28-sweep-selftest-…`) and `r28-generation-replays-green`
   then degrades to `could-not-evaluate`; with `TMPDIR=/var/tmp/k28x56`
   (outside the repo) it reads **12/12, `passed: true`**, exit 0. The filed
   `sweep/sweep-selftest.json` records the **12/12** reading, which is correct
   for the way the seat ran it; a reader who follows the assignment's
   `TMPDIR=$PWD/.scratch` convention gets the 10/12 reading. Disclosed, not
   adjudicated — the instrument's control is asserting a real constraint.

6. **C / coverage — both halves landed, and this seat re-ran the sweeps.** (a)
   The knowledge entry: `corpus/knowledge/linguistics/register-lexicon-ceilings.md`
   landed (**34 400 B**, sha256 `bb579d51cea0a900571e77b6690978256a607ec08f500923674738107dc1bffe`),
   frontmatter-complete (`topic`, `gap filled`, `sources`, `verified-at`,
   `recheck`, `couples`), gap-named with a five-command absence sweep, and
   grounded in both round-27/28 artifacts and external literature (Dixon,
   Halliday, Gotowski, Aronoff, Bauer, Labov; 44 citation years). (b) The
   amendment: `corpus/knowledge/linguistics/register-strata-attestation.md`
   gained **§13 "Amendment (round 28): the register-lexicon ceiling, re-measured,
   with its mechanism"** (line 315) as an **append-only new section** — 12 → 13
   section headers, no section lost, prefix preserved (57 996 → 64 928 B). (c) The
   README: `corpus/README.md` is at **revision 1.9** (linguistics 20 → 21,
   totals 200 → 201; revision 1.8 in the same file is the counts-footer repair).
   **This seat re-ran:** `python3 reports/round-28/readme/sweep.py` → `rows 201
   files 201`, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`,
   `header_drift {}`, `totals_line 201 totals_ok True`, `footer_ok True`,
   exit **0**; and `python3 reports/round-28/ceiling/measure-ceiling.py` → the
   ceiling reading **19 legal / 8 illegal** under the delivered gate (abstract
   class **1/4**), the filed round-27 **18/9** reproduced exactly under the
   pre-fix reader, delta `{L-45}`, and the mechanism
   `reverse is legal <=> the base-initial consonant is a licensed coda → True
   (27/27)`. The corpus counts `21` linguistics files and `201` knowledge files
   by plain `ls`/`find`, agreeing with the README. The runner's C leg reads
   `claims.C.passed = true` with `new_entries: ["register-lexicon-ceilings.md"]`
   and the same entry sha256.

7. **C / coverage — a filed-count divergence is named by the C seat, not
   smoothed.** The round-28 ceiling re-measurement does **not** reproduce round
   27's filed `18 legal / 9 illegal`; it reads **19/8** under the delivered gate,
   because round 27 replaced its own `syllabify` mid-round and never re-took the
   count. The delta is exactly one row (`L-45 tikmes`). Both readings are kept
   in the entry (§13) and in the round-28 instrument; the divergence is the
   finding, and this index records that the count is **reader-dependent**, not
   that round 27 was wrong at its stamp.

8. **A filed round-27 artifact was rewritten in place mid-wave, then restored
   (disclosed, healed).** `reports/round-27/gate-tests/receipt.json` moved
   `854ed1a3…` → `fbc1f4b6…` at **20:12:33Z** (inside the dispatch window) with
   its verdict flipping `passed: true, 55/55` → `passed: false, 42/55`, and was
   restored to its baseline blob by **20:14:42Z**. Three independent seats report
   it: the round-28 scope watch (`reports/round-28/scope.md`, which calls the
   filed surface **FAIL as observed**), the adversarial audit
   (`audit/o39-o40-…-adversarial.md` §1), and the runner's own protected-surface
   leg (which reads 0 differences **at the census**, after the restore).
   **This seat's own `git status --porcelain=v1` over the protected surface at
   the census returns 0 rows**, agreeing with the healed state. The residual is
   a post-dispatch **mtime** on that one path, which is why a settled tree can
   still show one row on an mtime channel. This is the round-20/25/26/27 hazard
   class recurring, and here it is **real and observed**.

9. **Cross-round coexistence (disclosed).** Seat `R28-D24`'s
   `scribe/fragment-ledger.{json,md}` is a second read-time census of this
   subtree, taken at its own earlier stamp (`census_utc 2026-10-18T20:31:09Z`,
   count 130). Its ledger's own prose stamp is **20:18:12Z** (when the subtree
   held 81 files), while its JSON `census_utc` is 20:31:09Z — so the two files
   of that one seat disagree with each other about their stamp, and both differ
   from this index's 20:47:50Z. That is the expected dated-refresh delta, not a
   contradiction, but the internal stamp disagreement is named here so the parent
   does not read it as a third census. Both are indexed; a divergence is a parent
   reconciliation item.

10. **The parent integrates.** No `reports/round-28/integration/` directory
    exists at the census; `report-draft.md` and `rerun.json` are drafts at the
    round root. Filing, scope, integration into `LOG.md`/`SCORECARD.md`, the
    final promotion review, and any external verification remain parent
    responsibilities; in-lane attestations do not prove a fresh external
    inspection. This is the **last build round of loop 3** (rounds 25–28), so the
    parent's integration is also the loop's close.

## Index verification

Reproducible coverage control over the table above. The generator
`reports/round-28/scribe/x56-census.py` walks the subtree; this block re-checks
that the index rows and the live tree agree on **digest**, and that the
availability/binding markers are current. Extract and run from the lane root:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B reports/round-28/scribe/x56-census.py --selftest   # 20/20 in-memory
python3 -B reports/round-28/scribe/x56-census.py              # regenerate the table
```

```sh
python3 - <<'PY'
import datetime, hashlib, re
from pathlib import Path
BASE = Path('reports/round-28')
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

# The tree was quiescent at the census, but the control stays DRIFT-AWARE by
# design: it must hold that no indexed row is *unavailable* and no row is
# duplicated, and it must PRINT any arrival or drift rather than assert a frozen
# tree. That is the round-20 lesson applied: a live-wave index that asserted
# equality would fail spuriously on every later read.
assert not (len(names) != len(set(names))), 'duplicate index row'
assert not (set(names) - set(actual())), 'an indexed artifact is now unavailable'

# availability markers, both directions
m_r = re.search(r'runner_present_at_census=(\w+)', text)
m_p = re.search(r'receipt_present_at_census=(\w+)', text)
m_b = re.search(r'binding_ok_at_census=(\w+)', text)
assert m_r and m_p and m_b, 'availability marker line missing'
runner = BASE / 'run-validation.py'
receipt = BASE / 'validation.json'
assert (m_r.group(1) == 'Y') == runner.is_file(), 'index stale: runner presence drifted'
assert (m_p.group(1) == 'Y') == receipt.is_file(), 'index stale: receipt presence drifted'
import json
live = hashlib.sha256(runner.read_bytes()).hexdigest()
declared = json.loads(receipt.read_text()).get('runner_sha256')
assert (m_b.group(1) == 'Y') == (live == declared), 'index stale: binding drifted'
print(f'runner_marker={m_r.group(1)} runner_now={runner.is_file()}')
print(f'receipt_marker={m_p.group(1)} receipt_now={receipt.is_file()}')
print(f'binding_marker={m_b.group(1)} bound_now={live == declared}')

# negative controls (in memory only)
pairs = [(p, s, h) for p, s, h in rows]
def conforms(ps):
    ns = [p for p, _, _ in ps]
    return (len(ns) == len(set(ns)) and set(ns) == set(actual())
            and all(ok_one(*r) for r in ps))
assert not conforms(pairs + [pairs[0]]), 'duplicate negative missed'
assert not conforms(pairs + [('reports/round-28/__X56_nonexistent__.md', 1, '0' * 8)]), 'missing-path negative missed'
tampered = [(p, s, ('00000000' if h != '00000000' else '11111111')) for p, s, h in pairs]
assert not conforms(tampered), 'tampered-sha negative missed'
assert text.endswith('\n') and '\0' not in text
assert all(line == line.rstrip() for line in text.splitlines()), 'trailing whitespace'
assert len(re.findall(r'^```[^\n]*$', text, re.M)) % 2 == 0, 'unbalanced fences'
print('INDEX_CONTROL=PASS; duplicate/missing/tampered negatives rejected; markers current')
PY
```

The generator's `--selftest` is 20 in-memory checks (exit 0), including the
negative controls: an unknown path must classify `unassigned` (never guessed), a
runner row must not read as green, and the self row must be excluded. The
classifier's round-28 additions (`ceiling/`, round-root `regression.md`) each
carry a named check, so the zero-`unassigned` reading is a measured claim about
the classifier, not an assertion.

**Standing caveat.** The tree was **quiescent** at the census (zero writes in the
60 s before each of the five preceding samples) and the receipt **binds** the
live runner, so this reading is the settled one — but it settled only after
**three** samples: an earlier receipt read `b8f08546…` / 242 900 B with 13
failures and a missing dependency, and the runner itself moved twice inside this
seat's window. A later arrival, a further runner edit, or a re-run of the
counting command invalidates this reading and requires a dated refresh. The
round-27 X56 index's own control caught exactly this class of drift on its
receipt (bound at 19:36:13Z, unbound by 19:43:59Z); here the drift is **real and
observed** in the opposite direction — unbound and red, then bound and green.

**Dated post-census refresh (2026-10-18T20:50:21Z).** This index's own coverage
control, run 2 min 31 s after the census, reports `indexed=130 observed=130`,
`unavailable=[]`, `arrivals=[]`, and **exactly one digest-drift row**:
`reports/round-28/validation.json` moved `37842da3…` (245 834 B, mtime 20:36:46Z)
→ `ed8aa84c…` (246 931 B, mtime **20:50:17Z**). The re-run **keeps every reading
this index binds**: `measured_at_utc: 2026-10-18T20:50:17+00:00`,
`acceptance_checks_passed: true`, 0 failures, claims `{C: true, D: true, O:
true}`, `missing_dependencies: []`, and it still **binds** the live runner
(`runner_sha256 20e09ea8…` = live `20e09ea8…`, which has not moved since
20:28:26Z). So the **verdict is unchanged and the binding is unchanged**; only the
receipt's byte size and its `measured_at_utc` stamp advanced. The census table's
`validation.json` row (`245834` / `37842da3` / `20:36:46`) is left as the census
stamp it was, per this index's own dated-row convention, and this block is the
newer reading. **The receipt was rewritten by someone other than this seat** —
this seat never ran the counting command — so the parent should treat 20:50:17Z
as its own re-run and confirm the authority; the two readings agree on the
verdict, so nothing in this index is invalidated by the movement.

## Boundary record

- **Writes:** this file and its instrument
  `reports/round-28/scribe/x56-census.py` (plus the gitignored generator scratch
  under `.scratch/x56/`, including the three tampered packet copies used for the
  replay-leg control). No `reports/round-{8..27}` byte was touched, no tool,
  gate, component, packet, pin or corpus entry was edited, and no shared
  bookkeeping (`LOG.md`, `SCORECARD.md`) was appended. `export
  TMPDIR=$PWD/.scratch` preceded every scratch-writing command; read-only gate
  runs used `TMPDIR=/tmp` (and `/var/tmp/k28x56` for the sweep-selftest control).
  No commit, no push.
- **Independence:** the census table was re-derived from the live bytes by
  `reports/round-28/scribe/x56-census.py`, not transcribed from the D24 ledger.
  The register-law-gate runs (clean + three tampers), the argot gate and its
  selftest, the typed gate, the battery, the two handoff-v3 runs, the README
  sweep, the ceiling measurement, the sweep-selftest pair and the protected-surface
  `git status` were all executed by this seat in its own shell. Where this index
  and a sibling fragment agree on a digest, the agreement is a cross-check, not
  inheritance.
- **Canon:** NON-CANON engineering evidence. This index admits nothing, certifies
  no round and adjudicates no claim.
