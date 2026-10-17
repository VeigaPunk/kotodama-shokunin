# provenance-audit baseline — author fragment (round 9, seat R9-O author)

- **Seat:** R9-O pair, **author** (the paired rerunner seat wrote `rerun.md` in this same
  directory). **Round:** 9, loop 1 of 3, build round 2 of 4. **Lane:**
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- **Date:** 2026-10-17, local clock UTC-03:00. Authoring window: 17:48:49–17:56 local
  (`date +%Y-%m-%dT%H:%M:%S%:z` → `2026-10-17T17:52:43-03:00` at the freeze instant).
- **Revision binding:** `HEAD = a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` (`git rev-parse HEAD`);
  the round's declared `baseline_revision` is `e1694bad6ac96aca45a11ca5746582b275929355`
  (`reports/round-9/claims.json`). Measured this window:
  `git show HEAD:tools/gates/provenance-audit.py | sha256sum` and the same for `e1694bad…` both
  print `8a96aaf4ccd14ef40defd4dce115e9ffa79c7a67ea3e9848cb63efbd3aa14e3a`, so the frozen verdict
  binds both revisions for the gate byte. The orchestrator's round-9 integration commit supersedes
  `revision` and must carry the baseline (standard §5 step 7).
- **Files written by this seat:**
  - `tools/gates/frozen/provenance-audit/r9-pre/expected.json` (the baseline pin, §4 fields)
  - `tools/gates/frozen/provenance-audit/r9-pre/run.log` (verbatim stdout at freeze time)
  - `tools/gates/frozen/provenance-audit/r9-pre/freeze.txt` (freeze/verify record, §5)
  - `tools/gates/frozen/provenance-audit/r9-pre/inputs/…` (20 byte copies, 13 corpus + 7 fixture)
  - `reports/round-9/baselines/provenance-audit/author.md` (this fragment)
  - `.scratch/r9-prov/` (untracked scratch: `manifest.tsv`, `verify_pin.py`, mirrors, batteries)
- **Not touched:** no gate source, fixture, corpus, or shared bookkeeping byte was edited
  (`git diff --stat HEAD -- tools/gates/provenance-audit.py` → empty). Nothing was committed —
  the orchestrator integrates once per round. No admission, promotion or canon is decided here.

## 1. Deliverable and its home (decision, receipts, and the divergence it sits in)

The baseline is a single home: `tools/gates/frozen/provenance-audit/r9-pre/` (standard §3 shape
`<gate-name>/<baseline-id>/{inputs,expected.json,run.log,freeze.txt}`). Reasons, measured:

- The round-9 battery extension discovers committed `expected.json` under
  `tools/gates/expected/` and `tools/gates/frozen/` only —
  `tools/check-gate-battery.py:114` (`BASELINE_ROOTS = (GATES_DIR / "expected", GATES_DIR / "frozen")`),
  read at 17:52 while that file was still being written by seat R9-O15
  (worktree sha256 at observation: `9ad0ef9516852c0f55b43edc3d3cf41795b2bd3c295b04c0b93946064bf2093c`).
  A baseline under `reports/…` is outside both roots and is not discoverable as written.
- Standard §3 names the `tools/gates/frozen/` root; `expected/` is the wave's second root.
- **Relocation (measured):** the snapshot was first staged under
  `reports/round-9/baselines/provenance-audit/`, then moved here before any record was written;
  digests were unchanged by the move — `pin verify after relocation: ok=20 bad=0`. The reports-side
  copies (`inputs/`, `run.log`) were then deleted, leaving this directory's `rerun.md` (the pair's
  other fragment) as the only file there.
- **Single-home sweep** (17:56): `find . -path ./.git -prune -o -path ./.scratch -prune -o -type f
  -name 'expected.json' -path '*provenance-audit*' -print` → exactly one hit, this baseline. The id
  `r9-pre` for `provenance-audit` resolves under exactly one root (standard §3).
- **Divergence observed, reported not absorbed** (the registry scribe's §5 item 1 and the rerunner's
  §8 record the same): at authoring time `r9-pre` baselines for other gates also sat under
  `tools/gates/expected/{costume-era-consistency-gate,phonology-sanity-gate}/`,
  `tools/gates/frozen/{handoff-packet-check,lexicon-coverage-audit}/`, and
  `reports/round-9/baselines/naming-collision-gate/` (outside both battery roots). The three-root
  split is the orchestrator's to reconcile; this seat only records it.

## 2. Input snapshot and provenance

The graded input is a composite snapshot, all byte copies made and verified 2026-10-17:

| part | files | origin | why |
|---|---|---|---|
| real corpus slice | 13 | `corpus/knowledge/verification/*.md` (the verification partition at r9-pre) | the gate grades mutable corpus entries; the slice is real, self-describing content |
| defect control | 7 | `tools/gates/fixtures/provenance/*.md` | supplies a non-empty, independently known finding set (the gate's own embedded constants) and one clean control entry |

- Copy receipt: for each file, `cp -p` then immediate re-hash of source and copy, then re-hash of
  the source again — **20/20 OK, 0 MISMATCH** (`.scratch/r9-prov/manifest.tsv`); after relocation the
  copies were re-checked against the manifest pins — **ok=20 bad=0**; and the live origins were
  re-hashed a third time — **20/20 still identical, 0 drifted**. So the snapshot equals the live
  files at freeze time, not merely two adjacent reads.
- Concurrency at freeze: the metadata shard was editing `corpus/knowledge/civilizations/*` and
  `culture-material/*` (`git status --porcelain`, 21 modified files observed at 17:52); the graded
  slice itself showed no drift at any check. The copies are frozen regardless of later edits.
- Verdict contract pins every input the gate reads: all 20 paths and digests are in
  `expected.json.inputs` (keyed `inputs/corpus/…`, `inputs/tools/gates/fixtures/…`, relative to the
  baseline directory, so the battery validator resolves them inside the baseline without an
  `input_external` reading).

## 3. Freeze receipts (commands verbatim; observed results)

| # | command (cwd = lane root) | observed |
|---|---|---|
| 1 | `python3 tools/gates/provenance-audit.py --selftest` | exit 0; `SELFTEST OK: 7 fixture file(s), planted IDs missing-topic, missing-sources, empty-sources, missing-couples, empty-couples, missing-calibration, exit 1 on the defect tree, exit 0 on the clean entry, exit 2 on a missing path` |
| 2 | `python3 tools/gates/provenance-audit.py tools/gates/frozen/provenance-audit/r9-pre/inputs > run.log` | exit **1**; stderr 0 bytes; `INFO scan: files=20 marks=74 mark-lines=74 findings=6 blocked=0`; `sha256(run.log) = 26f217410f2206bcecd871ab390cb416419a619e2727d7b6216c01d5cc9d6dac` |
| 3 | same command again, `cmp` the two stdouts | exit 1 both; **byte-identical** — the run is deterministic |
| 4 | copied tree at `.scratch/r9-prov/mirror2/` (different absolute root, same relative argv), `cmp` against `run.log` | exit 1; **stdout byte-identical** — deterministic re-execution by a stranger (standard §10, KTD-FR-S-0008) |
| 5 | tamper: append `'\n<!-- tampered byte -->\n'` to a copy of `inputs/corpus/knowledge/verification/calibration-registry.md`; recompute the digest | `cf7cceee…454c` → `e3650182…5925` — **digest mismatch → `snapshot_tampered`** (could-not-evaluate, exit 2 in the check) |
| 6 | re-run the gate over the tampered copy; `cmp` against the pre-tamper stdout | exit **1**, stdout **byte-identical** — measured: only the digest step turns this edit into `snapshot_tampered`; a stdout comparison alone would false-pass (standard §6's load-bearing point, re-measured on this gate) |
| 7 | pin re-verify (`python3 .scratch/r9-prov/verify_pin.py <baseline>/expected.json`) | `ok=20 mismatch=0 missing=0`, exit 0 |

Measured verdict: `expected.exit = 1`, `expected.class = findings`, ID set
`{empty-couples, empty-sources, missing-calibration, missing-couples, missing-sources, missing-topic}`
— each finding attributed to its fixture copy in `expected.json.finding_attribution`. The set is
identical to the gate's own embedded `EXPECTED_IDS` (`provenance-audit.py:210-217`) — an independent
ground truth for the defect control, and identical to what the rerunner seat measured independently
from the fixture tree (`rerun.md` §3 row 3/§7).

## 4. Battery validation receipts (the consumer this baseline is built for)

Run with `--baselines-root` over scratch roots holding only this baseline, `TMPDIR` moved off the
inode-exhausted `/tmp` (see §7), 2026-10-17:

- **Clean root** (`.scratch/r9-prov/root-clean/`): record
  `{baseline: root-clean/provenance-audit/r9-pre/expected.json, gate: provenance-audit.py,
  reading: "pinned", inputs_checked: 20, gate_sha256: match, stdout_pin: match, findings: []}`;
  summary `{pinned: 1, unevaluable: 0, gates_covered: ["provenance-audit.py"]}`.
- **Tampered root** (one byte appended to the same input): record
  `{reading: "snapshot_tampered", inputs_checked: 20, findings: [{id: "BASELINE-TAMPERED",
  detail: "…digest e36501826bc809fd… does not match the pin cf7cceee9008a9db…"}]}` —
  **never a silent pass**, exactly the O-claim's requirement.
- Both runs exited 2 overall only because the six other gates are uncovered in a root that isolates
  one baseline; that is the expected reading of an incomplete round, not a defect of this baseline.
  Per standard §6 step 3 the battery verifies digests and pins; the **verdict comparison** is the
  paired rerunner's byte-verified re-run (`rerun.md` §6), whose poll targets this path.

## 5. Negative control: no gate behavior change

- `git diff --stat HEAD -- tools/gates/provenance-audit.py` → **empty** (no change vs HEAD).
- `git show HEAD:tools/gates/provenance-audit.py | sha256sum` →
  `8a96aaf4ccd14ef40defd4dce115e9ffa79c7a67ea3e9848cb63efbd3aa14e3a`, equal to
  `expected.json.gate_sha256` and to the live worktree digest.
- The round-9 O-claim forbids gate behavior changes without a documented reason in the fragment:
  **this fragment documents none, because there are none** — the gate was read and executed only.
  The auditor seat's independent sweep agrees (`audit-19.md` §1–§2: gate tree byte-identical at
  declared revision and HEAD).

## 6. Cross-seat corroboration (their receipts, cited not absorbed)

- The rerunner's independent §7 corpus measurement — all 13 verification entries exit 0 with marks
  `calibration-registry 7, citation-format-and-source-registry 10, costume-era-consistency-gate 4,
  gate-frozen-run-standard 0, internal-consistency-audit 6, lexicon-coverage-audit 2,
  myth-consistency-gate 3, naming-collision-gate 4, phonology-sanity-gate 0,
  provenance-audit-ledger-format 9, real-world-inspiration-boundaries 5, to-verify-triage-protocol 13,
  verification-method-overview 9` (`rerun.md:126-131`) — matches this snapshot's own run.log
  per-file `INFO to-verify-count` lines exactly (sum 72; my `marks=74` adds the 2 on `good-entry.md`).
  Independent agreement on both the clean corpus slice and the six-ID defect set.
- The registry scribe's snapshot (`registry.md` §4) recorded `provenance-audit | r9-pre | nothing
  landed at sweep time` at 20:51:06Z, before this baseline landed — this fragment supersedes that
  row's status, and §9 below hands the scribe the row text.

## 7. Integration notes for the orchestrator (observed, not ruled)

1. **`run.log` needs `git add -f`.** `.gitignore` line 3 is `*.log`; `git check-ignore -v` confirms
   this baseline's and the other seats' `run.log` files are ignored (`git ls-files | grep -c '\.log$'`
   → 0 tracked today). Without a force-add the baseline commits without its verbatim stdout and its
   advisory `stdout_sha256` pin has nothing to compare to.
2. **Three baseline roots are in flight** (§1); the battery's hard-coded roots are
   `tools/gates/expected/` + `tools/gates/frozen/`, so `reports/round-9/baselines/naming-collision-gate/`
   would not be discovered as written. Decision needed from the integrator (registry §5 item 1).
3. **Frozen-root README index row is owed.** The standard §3 layout lists a `tools/gates/frozen/README.md`
   index (baseline id → gate, revision, verdict class). It does not exist and this seat did not create
   it: it is shared bookkeeping across seats, which the lane rules reserve for integration, and the
   O17 scribe's `registry.md` §4 is already the round's registry surface. Proposed row for whoever
   owns the file:
   `r9-pre | provenance-audit | tools/gates/frozen/provenance-audit/r9-pre/ | rev a7bb205d | exit 1 / findings (6 IDs)`.
4. **`/tmp` is inode-exhausted** (`df -i /tmp` → `1048576 1048576 0 100%`, 2026-10-17); `tempfile`
   consumers such as the battery need `TMPDIR` pointed at a disk-backed scratch (this seat used
   `.scratch/r9-prov/tmp`). Same finding as `rerun.md` §1 and the registry's measurement note.
5. **Later corpus edits do not invalidate this baseline** — they contradict it, which is the point:
   the snapshot is a copy, so a verification entry edited after 2026-10-17T17:52:43-03:00 must not be
   re-blessed; a new baseline is the remedy (standard §3 append-only, §6 `snapshot_tampered`).

## 8. Limits and calibration

- The pins prove byte identity and revision identity, never that the snapshot is good content, that
  the corpus entries are true, or that the lane is conformant overall. No design, canon, or
  admission claim is made (standard §2, §10; lane `AGENTS.md`).
- The compared verdict contract is `expected.exit` + the finding-ID **set**; stdout order and the
  advisory `stdout_sha256` are not the contract (standard §4). A clean-verdict-only baseline would
  discriminate weakly by set alone; this one is defect-bearing by construction (six IDs), and the
  `INFO scan` line (`files=20 marks=74 … blocked=0`) is recorded in `expected.json` as a
  supplementary observation, not as a substitute contract.
- Composite input is a design choice, declared: real mutable content (measurement) + committed
  fixtures (independent ground truth). Both parts are pinned; nothing was excerpted or reformatted.
- This seat measured only at `a7bb205d…`/`e1694bad…` (identical gate bytes); any later gate revision
  reads `gate_revised` and requires a re-freeze, never a comparison (standard §6 step 2).

## 9. Ready-to-paste registry row (for the R9-O17 scribe) and rerunner pointer

For `registry.md` §4 (replace the `provenance-audit | r9-pre | nothing landed` row):

| gate | baseline id | `expected.json` path (landed) | gate_sha256 | inputs pin | expected verdict |
|---|---|---|---|---|---|
| provenance-audit | r9-pre | `tools/gates/frozen/provenance-audit/r9-pre/expected.json` | `8a96aaf4…4e3a` | 20 inputs (13 corpus verification entries + 7 provenance fixtures); exemplar `inputs/corpus/knowledge/verification/calibration-registry.md` = `cf7cceee…454c` | exit 1, class findings, 6 IDs; `stdout_sha256 26f21741…6dac`; battery reading `pinned` (clean root) / `snapshot_tampered` (tamper drill) |

For the paired rerunner's §6.1 poll: the baseline is at
`tools/gates/frozen/provenance-audit/r9-pre/` as of 2026-10-17T17:53-03:00; `command` in
`expected.json` is the exact re-run command, and the ID set to compare against is
`{empty-couples, empty-sources, missing-calibration, missing-couples, missing-sources, missing-topic}`.

FILES: `tools/gates/frozen/provenance-audit/r9-pre/expected.json`; `tools/gates/frozen/provenance-audit/r9-pre/run.log`; `tools/gates/frozen/provenance-audit/r9-pre/freeze.txt`; `tools/gates/frozen/provenance-audit/r9-pre/inputs/**` (20 byte copies); `reports/round-9/baselines/provenance-audit/author.md` | SUMMARY: provenance-audit r9-pre frozen baseline authored at tools/gates/frozen/ with 20 digest-pinned inputs, measured exit 1 / six-ID verdict, deterministic replay, tamper→snapshot_tampered, battery reading `pinned`.
