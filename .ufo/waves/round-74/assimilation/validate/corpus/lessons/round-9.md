# Round 9 — escalated residual retrieval, gate-baseline drift pins, D3 acceptance (2026-10-17)

source: reports/round-9/claims.json; reports/round-9/targets.json; reports/round-9/** worker fragments (indexed below); reports/round-9/validation.json (freshest acceptance receipt); reports/round-8/validation.json (prior round, admitted at `e1694ba`)
verified-at: 2026-10-17 (gate-keeper survey window 20:49:06–21:02:22 UTC; acceptance receipt re-run 21:01:39 and again post-close 21:03:16 UTC on a tree still being written; admission and spot-check pending)
recheck: `python3 reports/round-9/run-validation.py` (declared counting command for F/O/D, authored by shard R9-O16); re-list fragments with `find reports/round-9 -type f | sort`

Gate-keeper skeleton (scribe X01), opened before the round-9 fragments landed
and closed after a ~13-minute fragment survey. It indexes the fragments that
landed and records the declared gate candidates with bounded reasons. Nothing
is admitted on declaration alone: the admitted/rejected rows below cite the
fragment and acceptance evidence actually read during the survey window, and
every admission stays marked spot-check pending until the parent's acceptance
run on the settled tree and an independent re-run land.

## Fragment index

Survey commands (2026-10-17 UTC): `find reports/round-9 -type f | sort` and
per-surface counts; a background poller was started for 40 ticks at 30 s each
and recorded 29 ticks (ticks 1–29, 20:49:06–21:03:07 UTC) before it was
stopped at the survey close. The poll log is outside the repo and not shipped:
it first had to move to `/dev/shm/r9-poll.log` because `/tmp` was
**inode-exhausted** for the whole window — `df -i /tmp` → `tmpfs 1048576
1048576 0 100% /tmp` (checked 20:48:35 UTC; the by-volume view disagreed,
`df -h /tmp` → 8.5G avail), and `cat > /tmp/r9-poll.sh` → `/tmp/r9-poll.sh:
No space left on device`. At least four shards (registry R9-O17, D01, D03,
verifier V02) independently recorded the same `/tmp` limit as a measured
environment defect; scratch moved to `/dev/shm`, `/var/tmp` and
`~/.cache/…` per shard.

- 20:49:06 UTC (tick 1, survey open): **11 files** — `claims.json`,
  `targets.json`, one naming-gate baseline packet, and a sibling's
  `freshness/.scratch-v03/` scratch. Zero acceptance receipts at that moment.
- Peak within the window: tick 7 (20:52:06) 76, falling to 65 at tick 8
  (scratch created and removed between ticks), then rising to **84 at tick 25
  (21:01:07)**, 85 at tick 28 and 86 at tick 29 (21:02:37, 21:03:07); poller
  counts exclude `__pycache__`.
- 21:01:42 UTC (survey close): **84 files** excluding scratch and
  `__pycache__` (85 files with `__pycache__`); `freshness/.scratch-v03/` had
  been removed and the root `.scratch/` worker dirs (r9d02, r9f02c,
  r9-naming-author, r9o17, r9phon) were gone by 21:02:22.
- Poller limit, recorded honestly: its per-path "NEW" leg compared
  `find -newermt` against the tick instant, so it under-sampled (14 NEW lines
  for ~73 net new files). Per-path first-seen rows are therefore not
  available; the rows below use presence at close plus file mtimes.

| fragment surface | shard range | claim | state at close |
|---|---|---|---|
| `freshness/` — 12 receipt ids `R9-F01a…c`, `R9-F02a…c`, `R9-F03a…c`, `R9-F04a…c` (`.json`; 11 `.md` companions — `F02b` had no companion) + `verify-F03.md` + `audit.md` (25 files) | R9-F01..F04×hunters+verifier | F | landed, all 4 residual ids covered |
| `baselines/` — 7 gate dirs (`costume-era-consistency`, `handoff-packet-check`, `lexicon-coverage-audit`, `myth-consistency-gate`, `naming-collision-gate`, `phonology-sanity-gate`, `provenance-audit`) + `registry.md`, `audit-18.md`, `audit-19.md`, `battery-extension.md` (30 files) | R9-O01..O20 | O | landed |
| `d3/` — `check-diagnosis.md`, `determinism.md`, `evidence-coupling.md`, `replay.md`, `interop.md`, `docs.md`, `capability-draft.md`, `scribe.md`, `findings.md`, `findings-10.md` (12 files) | R9-D01..D12 | D | landed |
| `metadata/` — `v01`, `v02`, `v04`, `v05`, `v10`, `v11` shard fragments + `audit.md` (11 files) | metadata re-audit (11 shards) | (metadata) | 11 of 11 landed |
| top-level — `run-validation.py` (20:53 first seen, rewritten 21:01), `validation.json`, `adjacency.md`, `report-draft.md` (6 files with claims/targets) | R9-O16, X03, X04 | F/O/D acceptance + scribes | landed |

Key mtimes at close (local -03:00 shown by `stat`): `baselines/naming-collision-gate/run.log`
17:48:49 · `d3/check-diagnosis.md` 17:50:35 · `d3/replay.md` 17:52:15 ·
first F receipt `freshness/R9-F01b-receipt.json` 17:54:39 ·
`baselines/registry.md` 17:55:10 · `freshness/R9-F02a-receipt.json` 18:00:25 ·
`reports/round-9/run-validation.py` 18:01:14 · `validation.json` 18:01:39 ·
`adjacency.md` 18:01:32. Round declarations: `claims.json`/`targets.json`
17:46:36.

Round-8 continuity, observed: the round-8 lesson closed with admission
pending; commit `e1694ba` (`round-8: admit F/O/D — freshness receipts,
harness+gate repairs, d2-typed-labels`, 17:44:17 -03:00) landed afterwards and
`reports/round-8/validation.json` reads `acceptance_checks_passed: true`. The
round-9 declared `baseline_revision` `e1694ba…` is that admit commit = `HEAD~1`
of observed `HEAD a7bb205…` (round-9 declare). Three independent shards
measured `git diff --stat e1694ba..HEAD` → only `claims.json` (34+) and
`targets.json` (125+), 159 insertions, 0 deletions, so the graded artifact
tree is identical under both revisions (`baselines/registry.md`; `baselines/audit-19.md`;
`baselines/phonology-sanity-gate/rerun.md`). Fragment presence is not
acceptance: a landed file is an input to `run-validation.py`, not a verdict.

## Gate

Candidates are the three claims declared before dispatch in
`reports/round-9/claims.json` (operator regimen: loop 1 of 3, build round
2 of 4; requested model `opencode-go-2/deepseek-v4.1-flash`, 64 workers).
Each candidate below quotes its declared `after_required` threshold

- **F / freshness** (declared lowest axis). The 4 residuals that stayed
  unresolved after round 8 (`R9-R8-F01..F04`, rows R6-02-A, R6-02-B, R6-05-B,
  R6-07-A in `reports/round-9/targets.json`) must each carry ">=2
  escalated-strategy retrieval receipts" (primary-source/museum-record
  hunter, scholarly-fulltext hunter, alternate-angle hunter, an independent
  verifier); ">=2 of the 4 move to partial-support-or-better on primary or
  scholarly passages; any that stay unresolved carry a deeper-limit receipt
  naming exactly what remains unreadable/unretrievable. Raw labels preserved
  apart from reconciled dispositions." Counting command:
  `python3 reports/round-9/run-validation.py`.
- **O / operability**. All 7 structural gates (`tools/gates/*.py`) must
  "carry a committed expected.json baseline layout (expected outputs + sha256
  digests of snapshot inputs) per the gate standard; the battery runner
  validates every baseline (tampered snapshot -> could-not-evaluate, never a
  silent pass); battery selftest remains green; no gate behavior changes
  without a documented reason in the fragment." Claim text also asks to
  "verify actual count first and record it" — at survey open (20:48 UTC) the
  verified count was **7 gate scripts, 0 `expected.json` baselines under
  `tools/`** (`ls tools/gates/*.py | wc -l` → 7; `find tools -name
  expected.json` → empty), matching the declared before-state.
- **D / depth** (capability `culture-d3-acceptance`, round-7's unadmitted
  debt). "`python3 tools/assemble-culture-d3.py --check` exits 0 with
  byte-identical deterministic assembly on the delivered tree; `python3
  tools/check-evidence-coupling.py --selftest` green; D3 replays frozen
  without digest drift; the capability row for reproducible D3 culture
  assembly enters SCORECARD only on demonstrated run (orchestrator admits)."

### Survey verdict at close (2026-10-17 21:01:39 UTC; receipt re-run post-close 21:03:16 UTC)

Freshest filed acceptance receipt (close reading): `reports/round-9/validation.json`,
mtime 21:01:39 UTC, sha256 `cca9fb60ff8a4d45…`; runner `reports/round-9/run-validation.py`
(mtime 21:01:14, sha256 of the battery it drives `0a126b70afa6cbd5…`);
`missing_dependencies: []`; `acceptance_checks_passed: false`. A post-close
re-run at 21:03:16 UTC (sha256 `d5fd16bec6f6dabd…`, runner rewritten 21:03:13)
reproduced the same per-claim verdicts and the same single D failure; it is
the freshest receipt as of 21:03:21. An earlier
run of the same runner (20:53 UTC, sha256 `19f26f40a8e7e662…`) still listed
missing dependencies `freshness/*R9-R8-F02*` and `freshness/*R9-R8-F04*`
and failed all three claims.

- F: `passed: true`, 0 failures; 4 declared ids; dispositions recorded in the
  receipt: F01 "supported at scholarly-passage scope by this shard's new
  material"; F02 "partial-support-or-better — the residual's scholarly leg …
  resolved on a first-hand retrieved full text"; F03 "partial-support-or-better
  … supported for the royal-cap/god-headgear contrast … partial for the
  earlier pre-Hittite comparator"; F04 "partial-support (raw label, preserved;
  not upgraded to full support by this shard)". Three of four moved, above the
  >=2 requirement as the receipt measures it.
- O: `passed: true`, 0 failures; 7 gates covered, 8 baselines discovered;
  `gate_revisions` shows all 7 gate sources byte-unchanged (`unchanged: true`
  each, head-vs-worktree sha256 equal); battery selftest exit 0 with the
  baseline tamper control (`tampered-digest-rejected` → `snapshot_tampered`);
  battery `summary` still `{battery_exit: 2, fail: 0, pass: 7, unevaluable: 0}`
  with the new baselines under a separate top-level key.
- D: `passed: false`, 1 failure. Green legs measured by the runner:
  `assemble-culture-d3.py --check` exit 0 twice, `repeat_identical: true`,
  identical stdout sha256 `8e8910da3adaed53…`; coupling selftest exit 0
  (16/16 domain, 5/5 frozen, 4/4 malformed controls). Red leg: `tools/
  check-evidence-coupling.py examples/culture-d3/packet.json --frozen
  examples/culture-d3/expected.json` exit 2, 3 × `D3-SNAPSHOT`:
  `corpus/knowledge/synthesis/worldbible-integration-contract.md`
  (50c4c2f2… → 5f4c02bf…), `tools/gates/costume-era-consistency-gate.py`
  (29a9361c… → e6bffd70…), `tools/gates/naming-collision-gate.py`
  (8c5afb0a… → d9e4e8f4…); `replay_note`: "no round-9 D3 replay manifest
  discovered".
- Overall `acceptance_checks_passed: false`.

Post-close observation (21:03:21 UTC, for the parent's audit): the round-9
tree had 86 files; the two post-close receipt re-runs reproduced the verdicts
above; and `git status` showed metadata shards writing `corpus/knowledge/**`
in place (modified `bali.md`, `byzantium.md`, `carthage.md`, …), i.e. the
corpus surface was moving outside `reports/round-9/` as well. These are
timestamped observations of an unsettled tree, not a settled-tree receipt.

**Admitted at this survey close: none yet.** Reasons: (1) the round verdict is
false while D is red; (2) the tree was still being written during and after
the window — `run-validation.py` and `validation.json` were rewritten at
21:01, ~40 s before the close reading, and `adjacency.md` landed at 21:01:32,
so the receipt is a snapshot of an unsettled tree; (3) the independent re-run
receipt (`reports/round-9/rerun.json` in round-8's idiom) has not landed — no
`*rerun*.json` exists under `reports/round-9/`. F and O currently read green
in that receipt; that is recorded as observed evidence, not admitted, because
admission requires the parent's acceptance on the settled tree plus the
independent re-run.

Rejected at this survey close (each names the observed evidence):

- **D as currently delivered**: the committed freeze
  `examples/culture-d3/expected.json` (sha256 `74496aa8aa7db2d7…`) pins three
  digests that no longer match the tree. `d3/check-diagnosis.md` and
  `d3/replay.md` diagnose the three drifts as round-8 repairs landing after
  the pin was frozen (`e1694ba`), i.e. **legitimate pins refusing edited
  inputs by design** — the failure is stale-pin, not D3 regeneration. But the
  declared threshold is "replays frozen without digest drift", and the
  frozen replay is red; the demonstrated remediation (a scratch refresh
  `expected-refresh.json` with exactly 3 digest lines updated, exit 0, with
  tampered twin staying red — `d3/replay.md` §E) is a scratch exercise, not
  a committed re-freeze. Refreshing the pin is an orchestrator act, flagged
  by the shards and not absorbed by them.
- **Counting the two non-standard-root baselines as covered by a default
  battery run**: the battery's committed default roots re-run is exit 2 with
  2 × `BASELINE-GATE-UNCOVERED` (`myth-consistency-gate.py`,
  `naming-collision-gate.py`), whose baselines live at
  `reports/round-9/baselines/<gate>/expected.json` rather than under
  `tools/gates/**` (the standard's §3 layout quoted in `baselines/registry.md`).
  Coverage of 7/7 gates is only via the acceptance's explicit round roots
  (`round_roots_run` exit 0, 8 baselines, 0 uncovered); the receipt records
  the default-root gap separately (`default_root_gap`) instead of hiding it.
  Whether the round's `committed baseline layout` requirement is met with two
  baselines outside the standard root is a parent-audit item, not decided here.
- **Treating the mid-flight acceptance run as the verdict**: the 20:53 run
  failed F on 0 receipts for F02/F04 and on F03's receipt shape, and O on the
  then-uncovered gates; those conditions were repaired later in the window.
  Receipts must be judged on the settled tree, not at first landing.
- **Re-freezing the D3 pin by regeneration-as-blessing**: regenerating a
  packet to match a changed pin, then calling the result drift-free, is the
  circularity the round's adversarial-review seats (R9-D09/D10) exist to
  catch; `d3/replay.md` §C/§E keeps regeneration and pin-refresh as separate
  measured acts with old/new digests named.
- **Claiming "no digest drift" from the packet's own `--check` alone** — the
  `--check` leg (passing) covers the two generator outputs; the frozen-replay
  leg is a different command over the committed pin and it is red
  (`replay_note`).
- **Counting fragment file presence or a fragment's self-report as
  acceptance** — fragments are inputs to `run-validation.py`; admission
  requires the parent's run and independent re-run.
- **Reading the battery's legacy `summary.pass = 7` as proof of the 7/7
  baselines** — that counter is the seven-gate legacy pass; the baseline
  verdict block is a separate key whose `baseline_exit` is what the O leg
  consults (and which is 2 under the default roots).
- **Promoting a reconciled disposition to more than the receipt says** — F04's
  raw `partial-support` label is preserved and explicitly "not upgraded to
  full support by this shard"; F01's scholarly-passage support is stated at
  passage scope, not whole-claim or whole-culture.

Spot-check status: **pending**. No parent acceptance on a settled tree, no
independent re-run receipt, and no parent source re-fetch receipt for the
round-9 F receipts has landed in this window. Historical receipts and frozen
evidence must not be rewritten; `reports/round-7/`, `reports/round-8/` filed
artifacts are read-only, and the D3 re-freeze belongs to the orchestrator.
The round's own counting command and the freshness receipts' access limits
remain the authoritative evidence once the tree settles; this lesson records
the gate-keeper's bounded survey only.
