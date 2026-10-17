# R9-O18 — auditor: all seven baselines re-run in isolation (parse, digest, tamper)

- seat: R9-O18 auditor. lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  assignment: *re-run all seven baselines in an isolated copy; verify each
  `expected.json` parses, digests match, and tampered-copy runs are rejected.*
- date: 2026-10-17, local clock UTC-03:00; final measurement window opens 17:57:37
  (isolated copy created; earlier copies at 17:54 were tooling shakedown, not
  evidence) and closes at the write-time drift re-check recorded in §7.
- role limits: this seat executes and measures. Its only write is this file.
  It admits no claim, blesses no gate, baseline, design, or source, and absorbs
  no sibling fragment's evidence as its own.
- revision binding: `git rev-parse HEAD` = `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd`
  (round-9 declaration); declared `baseline_revision` = `e1694bad6ac96aca45a11ca5746582b275929355`.
  `git diff --stat e1694bad6ac96aca45a11ca5746582b275929355 -- tools/gates` is
  empty at measurement and at write time (measured; command in §8) — every gate
  byte my re-runs graded is identical under both revisions.
- runner revision measured: `tools/check-gate-battery.py`
  sha256 `0a126b70afa6cbd5c2565b57399c318788540e10c4940d07c906718c8b9e1aa1`
  (recorded 17:58). The runner was under active edit inside the round window
  (peer audit R9-O19 pinned earlier revisions `6fff02df…`/`50f576c5…`/`c954135e…`);
  **every battery result below binds only `0a126b70…`.** Re-run if the delivered
  bytes differ.

## 1. Verdict

1. **All seven structural gates carry a committed `expected.json` baseline: 8
   files across 7 gates** (handoff-packet-check has two byte-identical copies,
   §5.2). Sweep: `find tools/gates/frozen tools/gates/expected
   reports/round-9/baselines -name expected.json` → 8 files (2026-10-17 17:53+).
2. **8/8 baselines pass every check this seat ran**: JSON parse; every pinned
   input digest recomputes from the baseline bytes; `gate_sha256` matches the
   live gate script; an isolated re-run of the named gate over the snapshot copy
   reproduces `expected.exit` **and** the finding-ID set; the advisory
   `stdout_sha256` pin reproduces; one appended byte to a snapshot copy is
   rejected by the digest step (`snapshot_tampered`), never a silent pass.
   Harness summary (§3): `baselines 8, parse_ok 8, digest_ok 8, verdict_match 8,
   tamper_rejected 8`.
3. **The extended battery exercises the same rejection semantics**: seven
   independent tamper drills (one per gate) → exit 2, `BASELINE-TAMPERED`,
   reading `snapshot_tampered`; malformed `expected.json` → `no baseline`;
   empty `inputs` → `unpinned (legacy)`; one byte of gate drift → `gate_revised`;
   battery selftest `SELFTEST OK 28/28 controls behaved as expected`, exit 0 (§4).
4. **One coverage gap is a runner-root decision, not a baseline defect**: under
   its committed defaults (`tools/gates/expected`, `tools/gates/frozen`) the
   battery exits 2 with `BASELINE-GATE-UNCOVERED` for **myth-consistency-gate
   and naming-collision-gate**, whose baselines live only under
   `reports/round-9/baselines/`. Pointed at all three roots the same run covers
   7/7, `pinned 8`, exit 0. Exact summaries in §5; the reconciliation is the
   orchestrator's (§6.1).
5. No gate source changed: `git diff e1694ba -- tools/gates` empty; the battery's
   own selftest battery ran 7/7 gate selftests exit 0, live tree preserved
   (28 hashed paths, modified 0 / added 0 / deleted 0) in every run below.

## 2. Method and isolation

- The measured surface (`tools/gates/{frozen,expected}/`, `reports/round-9/baselines/`,
  `tools/gates/*.py`, `tools/check-gate-battery.py`) was copied into
  `~/.cache/r9o18/final/iso-final1/` (203 files, 17:57:37) and **all** executions —
  gate re-runs, tamper drills, battery runs — happened there or in children of
  that copy. No live path was ever graded or written.
- Isolation evidence, all measured: (a) the copy's graded surface re-hashed
  before and after the whole pipeline → `COPY-PRESERVED yes` (203 files, no
  modified/added/deleted); (b) the live tree re-hashed against the copy at
  17:58:34 → **drift 0** across all 203 files including the battery script; so
  the numbers below bind the delivered tree, not a stale copy.
- `~/.cache/r9o18/` was used because `/tmp` is inode-exhausted in this window:
  `df -i /tmp` → `tmpfs 1048576 1048576 0 100% /tmp`; `mkdir /tmp/r9o18` →
  `No space left on device` (both 2026-10-17; corroborated by peer seats O17/O19).
- The re-run mirrors the repo-relative layout inside the scratch mini-repo
  (`tools/gates/<gate>.py` invoked with the baseline's own repo-relative
  snapshot path as argv, `cwd` = mini-repo root), which is what makes the
  advisory stdout pin reproducible. Graded input = the byte copy inside the
  baseline, never the live origin.

## 3. Per-baseline measurements (isolated re-runs, harness record 17:57:39)

`sha256(exp)` = `expected.json` digest prefix; `re-run` = this seat's gate
execution over the snapshot copy; `ids` = observed finding-ID set equals
`expected.findings` (set, not stdout order); `pin` = advisory `stdout_sha256`
reproduced; `tamper` = digest step rejected the mutated copy. All eight rows
were produced by one harness run (record `~/.cache/r9o18/final/audit-final1.json`).

| baseline dir (under lane root) | sha256(exp) | rev | expected | re-run | ids | pin | tamper |
|---|---|---|---|---|---|---|---|
| `tools/gates/frozen/handoff-packet-check/r9-pre` | `9dc21cd508e3` | a7bb205d | 0 / clean / 0 | 0 | ✔ | ✔ | ✔ |
| `tools/gates/frozen/lexicon-coverage-audit/r9-pre` | `0fad58ba70d5` | e1694bad | 1 / findings / 18 | 1 | ✔ | ✔ | ✔ |
| `tools/gates/frozen/provenance-audit/r9-pre` | `425c74c084bb` | a7bb205d | 1 / findings / 6 | 1 | ✔ | ✔ | ✔ |
| `tools/gates/expected/costume-era-consistency-gate/r9-pre` | `7ec01a1dce61` | a7bb205d | 1 / findings / 21 | 1 | ✔ | ✔ | ✔ |
| `tools/gates/expected/phonology-sanity-gate/r9-pre` | `2763614ff269` | e1694bad | 1 / findings / 1 | 1 | ✔ | ✔ | ✔ |
| `reports/round-9/baselines/handoff-packet-check` | `9dc21cd508e3` | a7bb205d | 0 / clean / 0 | 0 | ✔ | ✔ | ✔ |
| `reports/round-9/baselines/myth-consistency-gate` | `a87edc532711` | a7bb205d | 0 / clean / 0 | 0 | ✔ | ✔ | ✔ |
| `reports/round-9/baselines/naming-collision-gate` | `2f34ee1802b3` | e1694bad | 1 / findings / 3 | 1 | ✔ | ✔ | ✔ |

- Observed finding sets (this seat's re-runs, names in §4 receipts): costume =
  `E-01, EAR-01, EAR-04, G-ERA, MAT-01..07, R-01..07, T-01..03` (21);
  lexicon = 18 IDs = pinned set; provenance = `empty-couples, empty-sources,
  missing-calibration, missing-couples, missing-sources, missing-topic` (6);
  naming = `CROSS-HOLD, NAME-NEAR, PHON-INVENTORY` (3); phonology = `A-NEUTRAL`;
  handoff and myth = clean, empty sets.
- `gate_sha256` matched the live gate for all 8 (e.g. costume `e6bffd70…`,
  naming `d9e4e8f4…`, handoff `e2fa3223…`).
- provenance grades a directory (`…/inputs`, 20 files); its stdout embeds the
  graded path, so the pin only reproduces with the authored relative path —
  measured true here; the finding contract is the ID set either way (§6.5).
- The battery deliberately does **not** replay verdicts (`"verdict_replay":
  "not-run: the battery verifies digests and pins; the verdict comparison
  belongs to the baseline's own re-run receipt"`), which is why this seat
  re-executed all seven gates itself; both layers are green.

## 4. Tamper and negative controls (all in copied trees; drill record 17:57:53)

- **This seat's digest-level tamper check (8/8)**: append one byte to the first
  snapshot file of each baseline → recomputed digest ≠ pin → `snapshot_tampered`,
  comparison refused. Same result the authors' `freeze.txt` files recorded;
  independently re-measured here.
- **Near-miss re-measured by this seat** (the standard's §6 claim that only the
  digest step catches an edit): costume and naming snapshots with one appended
  byte still exited **1 with byte-identical stdout** (`cmp` clean) — a
  stdout-only comparison would false-pass; the digest step is load-bearing.
- **Battery drills, one tamper per gate (7/7)** — e.g.
  `D2-tamper-costume-era-consistency-gate: exit=2`,
  reading `snapshot_tampered`, finding
  `BASELINE-TAMPERED: packet.yml: digest 3ac7ba1a70f99b9d… does not match the pin 36d92113d0cb8e04…`;
  D3–D8 (handoff, lexicon, myth, naming, phonology, provenance) identical shape.
- **`D9` malformed `expected.json`** (truncated half) → exit 2,
  `BASELINE-MALFORMED: not valid JSON: Unterminated string starting at: line 11
  column 3 (char 481)`, reading `no baseline`.
- **`D10` empty `inputs` map** → exit 2, `BASELINE-UNPINNED: inputs absent or
  empty: unpinned legacy baseline, held for reading and barred from any
  conformance claim (§4)`, reading `unpinned (legacy)`.
- **`D11` one comment byte appended to the gate copy** → exit 2,
  `BASELINE-GATE-REVISED: gate_sha256 e6bffd7020c0b116… differs from the live
  costume-era-consistency-gate.py 70da5b4915550c0a…`, reading `gate_revised`.
- **`D12` runner selftest** → exit 0, `SELFTEST OK 28/28 controls behaved as
  expected`. The battery also reported `originals preserved: true` (28 hashed
  paths) in every untampered run.
- Every drill also re-hashed the source copy before/after →
  `source_manifest_unchanged: true`.

## 5. Coverage: defaults vs all roots (the orchestrator's decision)

1. **Default roots** (`BASELINE_ROOTS = tools/gates/expected + tools/gates/frozen`),
   run on the live tree 17:58: exit **2**,
   `{baselines_found: 5, pinned: 5, gates_covered: costume, handoff, lexicon,
   phonology, provenance, gates_uncovered: [myth-consistency-gate.py,
   naming-collision-gate.py]}` plus 2 × `BASELINE-GATE-UNCOVERED`. This matches
   the claim-O counting command reading red on the delivered tree **only
   because of the root list**, not because any baseline fails.
2. **All three roots named on the CLI** (`--baselines-root` × 3): exit **0**,
   `{baselines_found: 8, pinned: 8, gates_covered: all seven,
   gates_uncovered: [], findings: []}`.
3. **Single non-default root** (`--baselines-root reports/round-9/baselines`):
   exit 2, `{found: 3, pinned: 3, uncovered: costume, lexicon, phonology,
   provenance}` — no single root covers all seven; the union of the three does.
4. **Layout fact** (peer seats O17/O19 record the same): baselines landed in
   three roots — `tools/gates/expected/<gate>/r9-pre/`,
   `tools/gates/frozen/<gate>/r9-pre/`, `reports/round-9/baselines/<gate>/`.
   The lane standard §3 names `tools/gates/frozen/<gate-name>/<baseline-id>/`;
   authors' `freeze.txt`/`layout_note` fields declare their chosen roots.
5. **Duplicate handoff copy**: `packet.md`, `expected.json`, `run.log`,
   `freeze.txt` byte-identical between `tools/gates/frozen/handoff-packet-check/r9-pre/`
   and `reports/round-9/baselines/handoff-packet-check/` (`cmp` each; the
   reports copy additionally holds `author.md` + `rerun.md` fragments). No
   ambiguity under the current roots (one copy per root).

## 6. Findings and integration notes (reported, not absorbed)

1. **Root-list reconciliation is open** (owner: orchestrator). Two options are
   both consistent with the measurements: add `reports/round-9/baselines/` to
   the battery's committed roots, or relocate the myth + naming baselines into
   a committed root. **Post-window observation** (after this audit's clock,
   18:00): the claim-O counting command `reports/round-9/run-validation.py`
   (sha256 `7dd80d45…a94f0`, 18:00:03) runs the battery **plain** — no
   `--baselines-root` (its source, line 1417: `run_cli(BATTERY_REL, [],
   …)`) — and records a nonzero battery exit on the delivered tree as a failure,
   with only a hint that a valid baseline exists outside the committed roots
   (source ~1440–1456). So the counting command reads red on the delivered tree
   for exactly this root-list reason, not because any baseline fails; it stays
   red until the root list or the two baselines move.
2. **`run.log` files are git-ignored**: `.gitignore` line `*.log` matches all 8
   `run.log` files under the baseline roots (`git status --porcelain
   --ignored=matching …` → 8 `!!` entries; count command in §8). The integration
   commit needs `git add -f` for them or the baselines commit without their
   verbatim stdout (costume's `freeze.txt` and the O17 registry record the same).
3. **Two `revision` values** across the round's baselines: `a7bb205d…` (costume,
   handoff, myth, provenance) and `e1694bad…` (lexicon, naming, phonology, with
   a `revision_note` that the integration commit supersedes it). Both are
   legible; the single round-9 integration commit is the reconciliation point.
4. **The runner moved while the round was live.** `sha256(tools/check-gate-battery.py)`
   was `9ad0ef95…` minutes before my final sweep and `0a126b70…` at it; peer
   audit R9-O19 pinned three earlier revisions. My results bind `0a126b70…`; if
   the delivered bytes differ, re-run §4/§5 (pipeline: ~15 s).
5. **Advisory pins**: `stdout_sha256` is not the finding contract (standard §4).
   It reproduced 8/8 here only because the re-run mirrors the authored relative
   paths; a re-run from a different cwd can reproduce findings while failing
   the stdout pin (measured for provenance under a flat scratch layout).
6. `/tmp` inode exhaustion forced all scratch into `~/.cache/r9o18/`; any
   battery run relying on `tempfile` inside `/tmp` will fail in this window
   (the battery itself resolved its mirror under `/var/tmp` here — observed
   `removed: true` mirrors).
7. Out of this seat's scope, deliberately untouched: gate-source no-change
   (R9-O19), D3/freshness/metadata claims, and the 900+-line corpus edits
   visible in `git status` (metadata shards).

## 7. Limits and write-time check

- Binds: the 8 baseline directories, 7 gate scripts and the battery at
  `0a126b70…`, as copied at 17:57:39 and re-verified against the live tree at
  17:58:34 and again at write time 17:59:40 — the graded surface saw **zero**
  drift across both re-checks (the only difference at 17:59:40 is this audit
  file itself), and an independent quiescence watcher declared the baseline
  trees quiet at **17:59:08** (no writes for 90 s). The wave was still landing
  `.md` fragments outside the graded surface earlier in the window; those do
  not enter any number here.
- Matching digests prove byte identity, not that a snapshot is good design, not
  that a gate is honest, and not absence of writes with identical bytes
  (inherited caveat). Every gate re-run here is lane-local engineering
  evidence — no canon, source, or admission content.
- My harness is my instrument; its outputs are quoted verbatim. The battery
  results are the delivered runner's own JSON, re-run in a copy.

## 8. Receipts (commands, 2026-10-17, lane root unless noted)

```
find tools/gates/frozen tools/gates/expected reports/round-9/baselines -name expected.json   # 8 files
git rev-parse HEAD                                   # a7bb205d3aecdaa24d91c047c8719cd8689e4ddd
git diff --stat e1694bad6ac96aca45a11ca5746582b275929355 -- tools/gates   # empty
sha256sum tools/check-gate-battery.py                # 0a126b70afa6cbd5c2565b57399c318788540e10c4940d07c906718c8b9e1aa1
df -i /tmp                                           # tmpfs 1048576 1048576 0 100% /tmp
bash ~/.cache/r9o18/drive.sh final1                  # isolated copy 203 files; COPY-PRESERVED yes; battery selftest exit 0
python3 ~/.cache/r9o18/audit.py --repo <iso-final1> …   # baselines 8, parse_ok 8, digest_ok 8, verdict_match 8, tamper_rejected 8
python3 ~/.cache/r9o18/drill.py <iso-final1> …       # D0 exit2 uncovered×2; D1 exit0 pinned×8; D2-D8 tamper→snapshot_tampered; D9/D10/D11 exit2; D12 exit0
python3 tools/check-gate-battery.py                  # exit 2; 5 pinned; uncovered myth+naming; originals preserved true (28 hashed)
python3 tools/check-gate-battery.py --baselines-root tools/gates/expected --baselines-root tools/gates/frozen --baselines-root reports/round-9/baselines   # exit 0; 8 pinned
python3 tools/check-gate-battery.py --baselines-root reports/round-9/baselines   # exit 2; 3 pinned; 4 uncovered
git status --porcelain --ignored=matching tools/gates/expected tools/gates/frozen reports/round-9/baselines | grep -c '^!!'   # 8 (run.log)
cmp <both handoff copies>/{packet.md,expected.json,run.log,freeze.txt}   # 4/4 byte-identical
<gate> over tampered snapshot copies (costume, naming)   # exit 1, stdout BYTE-IDENTICAL to clean run
<live vs iso-final1 re-hash of 203 graded files>     # drift 0 at 17:58:34
```

This fragment is uncommitted at handoff (orchestrator integrates once per
round). Do not trust a self-reported digest: re-derive with
`sha256sum reports/round-9/baselines/audit-18.md` if a pin is needed.
