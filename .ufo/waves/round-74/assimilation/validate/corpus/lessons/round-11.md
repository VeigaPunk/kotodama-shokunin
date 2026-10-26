# Round 11 — typed-pipeline wiring, handoff e2e, ledger recheck (2026-10-17)

source: reports/round-11/claims.json; reports/round-11/targets.json; reports/round-11/**
worker fragments (indexed below); reports/round-11/validation.json (freshest filed
receipt, 22:21:03 UTC, runner sha256 `fab68287e74abc62…`); reports/round-10/validation.json
(prior-round admit receipt, re-read at survey open — all-green); reports/round-10/drift/
ledger.json (192 rows, all `output_sha256` 64-hex at open); tools/gates/frozen/round-11/
MANIFEST.tsv; reports/round-11/recheck/{summary.json,audit.md,dispositions.md}
verified-at: 2026-10-17 (gate-keeper survey window 22:01:02–22:27:28 UTC; freshest receipt
22:21:03; close probes 22:26:06–22:26:50; admission pending)
recheck: `python3 reports/round-11/run-validation.py` (declared counting command for D/F/O,
authored by scribe X03; live sha256 at close `fab68287e74abc62…`, = the receipt's
`runner_sha256`); re-list fragments with `find reports/round-11 -type f | sort`

Gate-keeper skeleton (scribe X01), opened before the round-11 fragments
landed and closed after a ~26-minute fragment survey. It indexes the
fragments that landed and records the declared gate candidates with bounded
reasons. Nothing is admitted on declaration alone: the admitted/rejected rows
below cite the fragment and acceptance evidence actually read during the
survey window, and every admission stays spot-check pending until the
parent's acceptance run on the settled tree and an independent re-run land.

## Fragment index

Survey commands (2026-10-17 UTC): a background poller sampled the tree every
30 s for 52 ticks, 22:01:02–22:26:32, logging to `.scratch/r11-poll.log`
(in-lane scratch, untracked; tick stamps UTC, file mtimes local UTC-03:00).
It records `find reports/round-11 -type f -printf '%T@ %p\n' | sort -k2` per
tick. `/tmp` was **not** inode-exhausted at this survey open — `df -i /tmp` →
`1048576 15695 1032881 2% /tmp` (the round-8/9/10 100% state no longer holds
at this stamp) — but scratch stayed in-lane per the standing rule
(`export TMPDIR=$PWD/.scratch`). At **open 22:01:02 UTC: 2 files**
(`claims.json`, `targets.json`); at **close 22:26:43 UTC: 255 files** (depth 27,
handoff 26, recheck 195, top-level 6, plus `__pycache__`); the last tick
(22:26:32) and the close reading agree, and the count was still 255 at
22:27:28.

`git status` watch: at open **1** modified path (path not captured — my miss;
by the 22:02 reading the set was `reports/round-10/coverage/index-update-22.md`,
`reports/round-5/validation.json`, `reports/round-6/checkpoint-validation.json`,
and index-update-22.md's mtime 22:01:18 is consistent with it being the open
path); at close **6 prior-round receipts + index-update-22.md +
`examples/culture-d2/typed-labels.d2.yml`** (the claim-D re-pin), with 15
untracked top-level entries (see the surface table).

First-seen rows (UTC; poller tick in parentheses): `depth/scribe.md` 22:02:02
(t2) · `depth/review-22.md` 22:03:02 (t4) · `report-draft.md` 22:03:32 (t5) ·
first recheck slice (rows 72–95, F04) 22:04:32 (t7) · first handoff fragment
`handoff/shard-glossary.md` 22:06:02 (t10) · `depth/design.md` 22:06:32 (t11) ·
`handoff/design.md` 22:08:02 (t14) · first `run-validation.py` 22:08:32 (t15) ·
first `validation.json` 22:09:02 (t16) · `adjacency.md` 22:12:02 (t22) ·
last recheck slice (rows 168–191) 22:12:02 (t22) · `recheck/audit.md` 22:14:32
(t27) · `recheck/summary.json` 22:15:32 (t29) · `recheck/dispositions.md`
22:16:32 (t31) · `depth/e2e-receipt.json` 22:17:32 (t33) · `handoff/impl.md`
22:18:32 (t35) · `depth/test-replay.md` 22:19:32 (t37) · `depth/integration.md`
22:20:02 (t38) · `depth/review-20.md` 22:21:32 (t41) · `handoff/frozen.md`
22:22:02 (t42). Out-of-poller close moves (below the last sample, from find):
`examples/culture-d2/packet.d2.typed.yml` re-emitted 22:24:26, `expected-holds.json`
22:25:xx, `tools/gates/typed-pipeline-gate.py` 22:26:xx; `tools/typed-gate-flow.py`
and `examples/culture-d2/typed-gate.expected.json`, both live at 22:25:54, were
**absent at 22:27** — an in-flight rename/move during close (see Gate).

| fragment surface | shards | claim | state at close |
|---|---|---|---|
| `depth/` — 27 files: `design.md`, `design-review.md`, `repin.md`, `frozen-records.md`, `integration.md`, `e2e-receipt.json`, shards `shard-{assembler,gate-adapter,holds,validator}.md`, tests `test-{e2e,differential,cli,boundary,determinism,replay,battery,interop-d3}.md`, negatives `neg-{17,18,19}.md`, reviews `review-{20,21,22,23}.md`, scribes `capability-draft.md`, `scribe.md` | R11-D01..D26 | D | landed; tests/negatives/reviews re-edited through 22:26 |
| `handoff/` — 26 files: `design.md`, `shard-{glossary,cli,assembly}.md`, `packet-attempt-{1,2,3,4}.{md,yml}`, `contract-check.md`, `gate-runs.md`, `impl.md`, `frozen.md`, `frozen-rerun.md`, `review-{16,17,18}.md`, `tamper-control.sh` + `.log`, and the exercised baseline `expected.json`, `packet.md`, `run.log`, `freeze.txt` | R11-O01..O18 | O | landed |
| `recheck/` — 195 files: `row-000.json`..`row-191.json` (all 192, eight 24-row slices), `audit.md` (F11), `dispositions.md` (F09/F10), `summary.json` (F12) | R10-F01..F08 (reruns), R11-F09..F12 | F | landed |
| top-level — `claims.json`, `targets.json`, `adjacency.md` (X02), `report-draft.md` (X04), `run-validation.py` (X03), `validation.json` | X02/X03/X04 | O + acceptance | landed |

Round-10 continuity, observed: round-10 admitted at `94ca098` ("round-10: admit
C/F/O …", 18:57:36 −03:00) and `reports/round-10/validation.json` reads
`acceptance_checks_passed: true`, D… — i.e. the round-10 lesson's "admitted:
none yet" was superseded by that commit; round-11's declared baseline is
`94ca098` and the declaration commit `e3ef171` (18:58:56 −03:00) touches only
`reports/round-11/{claims,targets}.json`. The round-10 ledger is claim F's
object: 192 rows, verdicts {current 153, stale-documented 29, stale-fixed 10},
all `output_sha256` 64-hex (sweep at survey open, exit 0).

Two filed-artifact incidents, measured and also filed by X02 (reported, never
absorbed here): (1) **six prior-round receipts rewritten in the live tree
during the wave** — `reports/round-5/validation.json` (mtime 22:01:55, later
re-written again; X02 snapshot 19:03:00), `reports/round-6/checkpoint-validation.json`
22:01:53, then round-6/7/8/9 `validation.json` by 22:02 — the mechanism is the
F seats' 1:1 re-runs of writer commands (`python3 reports/round-{5..9}/run-validation.py`,
ledger rows 102/113/114/120/129/130/131/132/147/170–173), X02 FINDING A;
(2) `reports/round-10/coverage/index-update-22.md` appended after filing
(+67/−1, X02 FINDING B; mtime 22:01:18, content stamped 21:59:52–22:00:17Z) —
at the round-10/11 boundary; the writer is not attributable from my window.

Fragment presence is not acceptance: a landed file is an input to
`run-validation.py`, not a verdict — the tree was still moving at my close
probes (a tool path was removed at ~22:26, files renamed at 22:24–26).

## Gate

Candidates are the three claims declared before dispatch in
`reports/round-11/claims.json` (operator regimen: loop 1 of 3, build round 4
of 4; requested model `opencode-go-2/deepseek-v4.1-flash`; 64 workers). Each
candidate below quotes its declared `after_required` threshold; no scalar
rubric is invented. This round's axes are D/F/O — coverage (round 10's C axis)
is absent.

- **D / depth** (capability `d2-typed-pipeline`). "The typed-label projection
  is wired into the D2 flow: assemble-d2 (or a documented adapter step)
  consumes typed labels; the D2 gates evaluate the typed packet such that
  translated labels never enter the sound channel and owed native forms are
  carried as named holds (not PHON artifacts); end-to-end command over
  examples/culture-d2 exits 0 with findings exactly equal to the expected hold
  set; frozen replay re-pinned and green; d2/d3 selftests + battery remain
  green." Counting command: `python3 reports/round-11/run-validation.py;
  python3 tools/assemble-d2.py --check`. Before-state verified at survey
  open/mid: naming gate over the legacy packet = 17 findings, `PHON-INVENTORY`
  ×10 = the ten `GAR-*` glosses; projection standalone with `--check` **exit 1**
  (committed `typed-labels.d2.yml` recorded `assembly.packet_sha256 8da90b07…`
  while the packet hashed `e0f21509…`; a fresh emission differs in exactly that
  one line — my sweep 22:01:58, matching `depth/design.md` §1.4);
  `replay-frozen.py tools/gates/frozen/round-3/MANIFEST.tsv` exit 2, 7 ×
  `gate_digest_mismatch`; expected hold set named by `depth/design.md` §4.2 =
  15 holds (10 × `D2L-FORM-UNRESOLVED` GAR-01..10 + 2 × `D2L-NATIVE` L-15/L-16
  + 3 × `D2L-RANK`) + 1 excluded note (`SR-01#a|SR-01#b`), fail set ∅.
- **O / operability** (capability `handoff-e2e-exercise`). "A runnable exercise
  (`tools/exercise-handoff-e2e.py` or documented equivalent) assembles a
  handoff packet from live D2/D3 artifacts and validates it through
  `tools/gates/handoff-packet-check.py` in an isolated copy: exit 0, 16/16
  fields, 20/20 glossary entries, contract cross-references intact; committed
  expected.json baseline; selftest with positive + malformed controls."
  Counting command: `python3 reports/round-11/run-validation.py`. Before-state:
  the gate's own commitments are pinned — round-9 baseline `run.log`
  `INFO scan: fields=16/16 glossary-entries=20 findings=0` (read at survey open)
  — and the exercise did not exist at open.
- **F / freshness** (declared lowest axis). "Recheck receipts
  (reports/round-11/recheck/) cover >=15 ledger commands re-run 1:1 with hash
  comparison: >=95% hash-stable; every drifted command dispositioned (cause
  named: legitimate change, environmental, or defect); recheck auditor
  independently re-runs >=5." Counting command:
  `python3 reports/round-11/run-validation.py`. Object at open:
  `reports/round-10/drift/ledger.json`, 192 rows, verdicts {current 153,
  stale-documented 29, stale-fixed 10}, all `output_sha256` 64-hex.

### Survey verdict at close (2026-10-17 22:21:03–22:27:28 UTC)

Freshest filed acceptance receipt: `reports/round-11/validation.json`, mtime
22:21:03 UTC, `runner_sha256 fab68287e74abc62…` (= live `run-validation.py`);
`missing_dependencies: []`; `acceptance_checks_passed: false`.

- D: `passed: true`, 0 failures on the 22:21:03 receipt. Independent close
  probes, run by this seat on the final bytes: `python3 tools/gates/
  typed-pipeline-gate.py --selftest` exit 0 — "12/12 checks passed — …
  smuggled-label, dropped-row, laundered-hold, adapter-drift, malformed and
  missing controls" (22:26:50); default run exit 0 — "16/16 legs passed"
  (L3-baseline, L3-details, L3-baseline-set, L3-routing-consistency, L4-pins);
  `python3 tools/d2-typed-labels.py --check` exit 0 byte-identical;
  `python3 tools/assemble-d2.py --check` exit 0. The ad-hoc predecessor
  `tools/typed-gate-flow.py` ran 10/10 exit 0 at 22:21:43, then **9/10 exit 1
  at 22:26:06** (`FAIL typed-packet-pinned — derived typed packet differs from
  examples/culture-d2/packet.d2.typed.yml`), and that path was gone by 22:27
  — the integration renamed the gate to the design-named
  `tools/gates/typed-pipeline-gate.py` (design §3.1) and the baseline to
  `examples/culture-d2/expected-holds.json` (design §4.5) while also
  re-emitting the typed packet (22:24:26). The D e2e receipt
  (`depth/e2e-receipt.json`, 22:18:18) records `exit_code: 0` and 10/10 checks
  (`hold-set-equal: true`, `differential-exact: true`), with the channel delta
  measured as naming-gate 17 → 7 findings, 10 removed / 0 added and the other
  four gates unchanged; the frozen `tools/gates/frozen/round-11/MANIFEST.tsv`
  carries typed-packet rows for the five gates plus `legacy/` twins (naming 17
  findings legacy → 7 typed, phonology 3 → 3).
- O: `passed: true`, 0 failures on the 22:21:03 receipt. Independent close
  probe: `python3 tools/exercise-handoff-e2e.py --selftest` exit 0 on the
  22:17 revision with the full control list (malformed-05..10, hazard probe,
  21-file preservation, tamper baseline/read-set/scan-expectation, missing
  artifact). The exercised baseline's own run log
  (`reports/round-11/handoff/run.log`, frozen 22:19:33): "gate verdict: exit 0,
  fields=16/16, glossary-entries=20, findings=0", packet sha256
  `6583b6bdbf5e3fe0…`, 21 read-set files, component digests 13/13 matched;
  `handoff/expected.json` names `baseline_digest 19f39f8489563b8e…` and the
  contract digest `sha256:5f4c02bf…`. Earlier in the same window the same
  command on an earlier revision exited 1 (22:12:41, `AssertionError: …
  cannot hash examples/culture-d2/components/02-phonology.yml` — a fixture-copy
  source missing; repaired by the 22:17 revision), matching the first
  receipt's O failures.
- F: `passed: false`, 4 failures on the 22:21:03 receipt — "recheck: reports/
  round-11/recheck/row-174.json command is not the ledger row's command 1:1 —
  keep the ledger text in `command` (the row-006 convention …)"; the same for
  `row-187.json`; "recheck: 1 receipt(s) contradict their own hashes:
  ['reports/round-11/recheck/row-047.json: stable=True but new_hash !=
  prior_hash']"; and "recheck: stability **0.788 < required 0.95**". This
  seat's independent recount of the 192 receipts at 22:25:54: **149 stable /
  43 unstable = 77.6%** (unstable rows 1, 2, 4, 5, 12, 39, 40, 51, 54, 65, 66,
  67, 68, 69, 90, 91, 98, 99, 102, 103, 111, 113, 117, 120, 121, 127, 128,
  129, 130, 152, 153, 154, 162, 163, 169, 170, 174, 175, 177, 185, 188, 189,
  190; by first keyword of `drift_cause` text: legitimate-change 14,
  non-reproducible-by-construction 12, environmental 5, run-location-dependent
  5, ledger-transcription defect 2, unclassified 5). The F scribe's
  `recheck/summary.json` (22:19:38) records `rows_reckecked: 192, stable: 149,
  unstable: 45` — its stable+unstable sums to 194, not 192 (a scribe-arithmetic
  inconsistency, reported not fixed). The F auditor (`recheck/audit.md`,
  F11, window 22:01:52–22:13Z) independently re-ran **17 rows across all eight
  slices**; its comparison table shows identical hashes except the
  nondeterministic battery rows (F11-1), and it flags row 47's prior as "a
  stripped-newline recording" (F11-4) — the same row the receipt's
  self-contradiction finding names. Under every reading measured here,
  hash-stability is far below the declared 95%.
- Overall `acceptance_checks_passed: false`; the receipt predates the D/O
  close integration (typed packet re-emitted 22:24, baseline renamed 22:25,
  gate moved 22:26).

**Admitted at this survey close: none yet.** Reasons: (1) the round verdict is
false while F is red; (2) the freshest receipt is a snapshot of a tree that was
still being integrated — the D gate's path and baseline names moved after it,
and the ad-hoc predecessor tool disappeared mid-close; (3) no independent
re-run receipt covering the final revision has landed in this window (the
round-8 `rerun.json` precedent; round-11 has none).

Rejected at this survey close (each names the observed evidence):

- **Counting the first receipt's verdict (22:09:44)**: it failed D on 5 legs
  including "e2e: no round-11 e2e evidence found … no wired flow (--e2e/--flow)
  tool" and "replay: no round-11 frozen manifest found", O on 5 legs including
  a traceback in the exercise selftest — and F on stability 0.795, three
  missing-hash receipts (rows 067–069), `row-101.json` contradicting its own
  hashes (a different self-contradiction row than the 22:21 receipt's
  `row-047.json`), and row 51's drift cause naming none of the licensed
  classes; 15 F failures in all.
  Every one of those conditions moved within 12 minutes; receipts must be
  judged on the settled tree, not at first landing.
- **Counting this seat's own 10/10 `typed-gate-flow.py` run (22:21:43) as D
  acceptance**: 14 minutes later the same command read 9/10
  (`typed-packet-pinned`), and the tool path was removed by the next reading.
  A pin check that moves under integration is exactly the object the D22
  circularity reviewer audits; the final green is the design-named gate's
  16/16 at 22:26:50, still one revision old at this close.
- **Reading the battery's exit 2 as a D failure**: `python3 tools/
  check-gate-battery.py` exits 2 with 7 pass / 0 fail standing (two gates
  uncovered under default roots) — the round-9/10 continuity state, quoted in
  `depth/scribe.md` §1.1; the 22:21 receipt passes D, and the earlier
  receipt's battery failure was its own rubric reading, not a change in the
  battery.
- **Counting the receipts' `stable` flags alone as "hash-stable"**: they are
  the right object but were themselves rewritten during the window (rows
  47/101 contradictions appear at different stamps), and F11's audit shows
  the underlying hashes mostly match — the failures are real but the
  question of which denominator the 95% leg uses (192 vs the receipt's 0.788
  arithmetic, vs summary.json's sum-194 rows) is unresolved and is the
  parent's adjudication.
- **Counting `stale-documented` and `recheck`-verified rows as "current"**:
  the claim's threshold is hash-stability, not verdict preservation; the
  ledger's 29 `stale-documented` rows were not re-adjudicated here.
- **Counting the six rewritten prior-round receipts as regressions**: they are
  the recheck's own side effect of 1:1 re-running writer commands (mtime
  evidence above; X02 FINDING A) — a scope incident to decide (restore or
  re-file), not freshness drift.
- **Treating the `index-update-22.md` appendix as round-11 work**: it is an
  append to a filed round-10 artifact (X02 FINDING B), stamped 21:59:52–
  22:00:17Z at the boundary; reported, not absorbed.
- **Counting `handoff/packet-attempt-{1,2,3}.{md,yml}` as the O deliverable**:
  those are assembly attempts; the gate-verified artifact is the exercise's
  own isolated run (`handoff/run.log`, 16/16, 20/20, exit 0) plus the committed
  baseline (`handoff/expected.json`, `freeze.txt`), and the exercise's own
  selftest is the O control surface, green only from the 22:17 revision.
- **Reading D's "findings exactly equal to the expected hold set" as satisfied
  by the e2e receipt alone**: the receipt (22:18:18) predates the baseline
  rename (`typed-gate.expected.json` 22:13:03 → `expected-holds.json` 22:25)
  and the typed packet's re-emission (22:24:26); the parent must confirm the
  gate reads the committed baseline bytes that the round actually keeps.

Spot-check status: **pending**. No parent acceptance on a settled tree, no
independent re-run receipt for the final revision, and no parent source
re-fetch receipt for the F receipts has landed in this window. Historical
receipts and frozen evidence must not be rewritten; `reports/round-{8,9,10}/**`
filed artifacts are read-only (the in-flight edits named above are observed,
not endorsed), and the D re-pin (the `typed-labels.d2.yml` packet-sha line)
belongs to the round's own seats and the parent. The round's own counting
command and the recheck receipts remain the authoritative evidence once the
tree settles; this lesson records the gate-keeper's bounded survey only.
