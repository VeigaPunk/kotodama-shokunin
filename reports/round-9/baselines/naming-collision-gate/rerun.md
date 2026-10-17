# naming-collision-gate baseline — independent re-run (round 9, rerunner seat)

- role: **rerunner** — second worker of the `naming-collision-gate` baseline pair. This worker
  writes only this file (`reports/round-9/baselines/naming-collision-gate/rerun.md`); the author
  seat owns `expected.json`, the snapshot copy, `run.log` and `freeze.txt` in the same directory.
  Nothing here was committed; the orchestrator integrates once per round.
- date: 2026-10-17; checks executed 20:48–20:53Z (17:48–17:53 local, −03:00). All digests below
  are from commands re-executed by this seat, not copied from the author's files.
- lane revision at re-run start: `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd` (`git rev-parse HEAD`).
  `reports/round-9/claims.json` names `baseline_revision: e1694bad…`; `git log --oneline` shows that
  is `e1694ba` (HEAD~1, the round-8 admit commit). `git diff --stat
  e1694bad…..HEAD -- tools/gates` → empty and `-- examples` → empty (2026-10-17), so the graded gate
  and the graded packet are byte-identical between the declared revision and HEAD. `git status
  --porcelain` shows the baseline directory itself still untracked (wave rule: workers never commit).
- gate under test: `tools/gates/naming-collision-gate.py`, sha256
  `d9e4e8f4f93a21b3b8574856a7d8bc6b93d224eee490ab37ed5f98741a630a1d`
  (`sha256sum`, 2026-10-17; `git show
  e1694bad6ac96aca45a11ca5746582b275929355:tools/gates/naming-collision-gate.py | sha256sum` →
  same digest).
- graded snapshot: `packet.yml` = byte copy of `examples/culture-d2/packet.d2.yml`
  (`cmp` clean; both sha256 `e0f21509e14ac03ed5747e6bbbb48183cbe56d6b61afff8c8475e4a50137b643`; the
  blob at the declared revision carries the same digest) — the D2 packet the standard §9 names as
  the intended first real input.
- standard followed: `corpus/knowledge/verification/gate-frozen-run-standard.md` §4 (required
  `expected.json` fields), §5 (freeze procedure), §6 (verify procedure, tamper semantics, class
  mapping). This file is the independent second half of the pair's evidence.

## 1. Artifacts under validation (digests of the 17:50-local revision, re-measured through 17:51 local)

| file | sha256 | pinned by |
|---|---|---|
| `packet.yml` | `e0f21509…37b643` | `expected.json.inputs["packet.yml"]` — match |
| `run.log` | `ebc8850d…a66f4b` | `expected.json.stdout_sha256` (advisory) — match; 17 lines, 17 `FINDING` |
| `expected.json` | `2f34ee18…4b9a45` | not self-pinned (contract) — validated in §2 |
| `freeze.txt` | `07074cc1…8befef` | not self-pinned (contract) — read in full |

- The directory held one extra 0-byte `.stderr` at 17:49:29 local (observed by this seat); by
  17:50:25 it was gone. The validated artifacts are the four files above plus the author fragment
  `author.md` (see below) — layout is clean.
- Author revision during the check window (recorded because this seat's first read predates it):
  `expected.json` (2311 → 2545 bytes) and `freeze.txt` (2539 → 3823 bytes) were revised at 17:50
  local, after this seat's first read at 17:49:40. Both were re-read and re-verified against the
  **current** bytes; the change is additive — `revision_note` expanded with the HEAD / claims-targets
  detail, and `freeze.txt` gained a revision-detail block, a KNOWN LIMIT line on the absent internal
  digest check, and integration notes. Every pin quoted in this fragment (`gate_sha256`, `inputs`,
  `stdout_sha256`, tamper sha, expected verdict) is identical in both revisions, and no value in
  §2–§4 depends on the revised regions; `packet.yml` and `run.log` digests were stable across the
  whole window (re-measured 17:48, 17:50:36, 17:51:15 local).
- `author.md` (the pointer in `frozen_by`) landed at 17:50 local, 6954 bytes, sha256
  `60f95dd1eea99812fe87d262e8657d61d50c14854cf8101680df13213149e945` — the pointer now resolves.
- `expected.json` required fields per §4: `schema` = `kotodama-frozen-run-v1`, `gate` =
  `naming-collision-gate` (equals the directory name), `gate_sha256`, `revision`, `frozen_at`,
  `frozen_by`, `inputs` (non-empty), `expected.{exit, class, findings}` — **all present**
  (`python3 -c 'import json; …'` field sweep). Extras (`baseline_id: r9-pre`, `gate_script`,
  `revision_note`, `input_origin`, `input_class`, `command`, `finding_counts`,
  `finding_count_total`, `gate_selftest`, `stdout_sha256`, `tamper_evidence`, `layout_note`) are
  tolerated by §4 and are themselves checkable claims — checked below.

## 2. Digest and revision checks (§6 steps 1–2)

| # | Command (2026-10-17) | Observed |
|---|---|---|
| 1 | `sha256sum reports/round-9/baselines/naming-collision-gate/packet.yml` vs `inputs` pin | `e0f21509…37b643` = `e0f21509…37b643` — **match** |
| 2 | `cmp packet.yml examples/culture-d2/packet.d2.yml` | byte-identical; `input_origin` claim reproduced |
| 3 | `sha256sum tools/gates/naming-collision-gate.py` vs `gate_sha256` | `d9e4e8f4…630a1d` = pin — **match**, `gate_revised` reading not triggered |
| 4 | gate blob at `e1694bad…` (declared revision) | same `d9e4e8f4…630a1d`; packet blob at that revision also `e0f21509…` — the named revision resolves to these exact bytes |

## 3. Verdict re-run (copied trees only; never a live graded path)

| # | Setting | Observed |
|---|---|---|
| 1 | partial scratch copy (gate + snapshot under `/var/tmp/r9-naming-rerun/tree`, cwd ≠ lane root) | exit **1**; 17 findings; ID set **{CROSS-HOLD, NAME-NEAR, PHON-INVENTORY}**; counts 10 PHON-INVENTORY, 6 NAME-NEAR, 1 CROSS-HOLD = `finding_counts` / `finding_count_total` reproduced; stdout sha256 `ebc8850d…a66f4b` — **byte-identical to `run.log`** |
| 2 | full pristine copy: `git archive HEAD \| tar -x -C …/full` + the four baseline files copied in | same exit 1, stdout **byte-identical** (`cmp` clean) — the verdict reproduces in a clean checkout of HEAD, not only in the author's tree |
| 3 | `--selftest` in the copied gate tree (fixture pair copied beside the gate) | exit **0**; `selftest: OK — fixture findings 12 across 11 ids (…); positive control clean; malformed inputs exit 2; missing profile held; case policy routed` — capability re-executed, not read |
| 4 | determinism: three consecutive runs over the snapshot | 3/3 exit 1; one distinct stdout digest (`ebc8850d…a66f4b`) — deterministic |
| 5 | path-independence: gate over the **live** `examples/culture-d2/packet.d2.yml`, cwd `/` | exit 1; stdout byte-identical to `run.log` — the author's `freeze.txt` step-4 claim reproduced |

- Expected verdict comparison (§6 step 3): observed exit 1 = `expected.exit` 1; observed ID set =
  `expected.findings` {CROSS-HOLD, NAME-NEAR, PHON-INVENTORY} as a **set** (order-insensitive per
  §4) — **match**. No drift, no could-not-evaluate.

## 4. Negative controls (§6 §5 semantics re-measured)

| # | Control | Observed |
|---|---|---|
| 1 | tamper: copy of `packet.yml` + `printf '\n# tampered byte\n' >>` | sha256 **`265bd5c6a37fd90a5e0692ce39a6564622e0a787bc4293cf7dcedf944f7009d7`** — exactly the author's `tamper_evidence.tampered_copy_sha256`; digest ≠ pin → `snapshot_tampered`, could-not-evaluate (external `sha256sum`/hashlib check, as §8 declares gates do not verify digests internally yet) |
| 2 | gate over the tampered copy | exit 1, stdout byte-identical to `run.log` — the load-bearing §6 point: only the digest step detects the edit |
| 3 | gate-revision control: gate copy + one appended comment byte | sha256 `2bc2c492…cd1b26` ≠ `gate_sha256` → would read `gate_revised` (could-not-evaluate); never compare across an unnamed revision |
| 4 | read-only over graded input: `sha256sum packet.yml` before/after all runs | unchanged `e0f21509…`; scratch tree `find -newer` sweep → no file written by any run |
| 5 | input-completeness sweep (negative claim): `grep -n "read_text\|open(" tools/gates/naming-collision-gate.py` | 3 hits only: lines 1790/1793 (fixture + `.expected`, `--selftest` path) and 1912 (the argv packet). A normal run reads exactly the file given on the command line → the one-entry `inputs` map is complete per §4 "pin **every** input the gate reads" |

## 5. Battery status — measured, including the extended battery (R9-O15 landed mid-window)

- 20:50Z (before the extension): `grep -n "expected.json\|baselines\|frozen"
  tools/check-gate-battery.py` → no hits, i.e. the old battery read no `expected.json`; the old
  `--selftest` run → exit 0, `SELFTEST OK 10/10 controls behaved as expected`.
- 20:52:19Z the extension landed (`tools/check-gate-battery.py` sha256
  `9ad0ef9516852c0f55b43edc3d3cf41795b2bd3c295b04c0b93946064bf2093c`). This seat re-ran it three ways
  (20:52–20:53Z, TMPDIR on the scratch root; 7/7 gate selftests pass in every run):

| run | roots | observed |
|---|---|---|
| default | `tools/gates/expected` + `tools/gates/frozen` | exit **2**; 4 baselines discovered, all `pinned` (costume-era, phonology, handoff-packet-check, lexicon-coverage-audit); **`BASELINE-GATE-UNCOVERED` for myth-consistency-gate, naming-collision-gate, provenance-audit** — the gates whose baselines live only under `reports/round-9/baselines/` |
| round-9 root only | `--baselines-root reports/round-9/baselines` | exit 2 (coverage 3/7); **the naming baseline reads `pinned`** — the battery itself verified its input digest, gate pin and stdout pin vs `run.log`, an independent cross-check of §1–§2; handoff-packet-check and myth-consistency-gate also `pinned` |
| all three roots | round-9 + expected + frozen | exit **0**; 8 baselines discovered, **all pinned**, coverage **7/7**, no findings |

- Reading: the naming baseline is valid in the battery's own terms (`pinned`); the round's baseline
  set reaches coverage only when all three roots are passed explicitly — reconciliation is note 1.
  The battery never re-executes a verdict by design (`verdict_replay: not-run: digests and pins
  verified only`), so §3's byte-identity runs remain the verdict evidence.

## 6. Notes routed to the orchestrator (not defects of this baseline)

1. **Three baseline roots are in flight — measured, not hypothetical.** Independent sweeps and
   battery runs (2026-10-17): `reports/round-9/baselines/<gate>/` (naming-collision-gate,
   myth-consistency-gate, handoff-packet-check, provenance-audit), `tools/gates/expected/<gate>/r9-pre/`
   (costume-era-consistency-gate, phonology-sanity-gate), `tools/gates/frozen/<gate>/r9-pre/`
   (lexicon-coverage-audit, provenance-audit — the root `gate-frozen-run-standard.md` §3 names).
   Consequence measured on the extended battery (§5): default discovery covers 4/7 gates and exits 2
   with `BASELINE-GATE-UNCOVERED` for myth/naming/provenance; with all three roots explicit → 7/7,
   exit 0. One discovery rule must be chosen before the O claim is read (or the baselines relocated
   into the standard's root). Sub-finding: `handoff-packet-check` currently has **byte-identical
   copies in two roots** (`reports/round-9/baselines/handoff-packet-check/expected.json` and
   `tools/gates/frozen/handoff-packet-check/r9-pre/expected.json`, both sha256 `9dc21cd5…`) —
   harmless while identical, but two homes invite drift; the registry should name one home per
   baseline. Routed, not resolved here. (The author's revised `freeze.txt` flags the same contest;
   this seat reproduced and quantified it.)
2. **Commit trap: `.gitignore:3` is `*.log`, and `run.log` is part of the baseline.** Reproduced with
   `git check-ignore -v reports/round-9/baselines/naming-collision-gate/run.log` →
   `.gitignore:3:*.log`; the same for `tools/gates/expected/costume-era-consistency-gate/r9-pre/run.log`.
   A plain `git add` of the baseline directories integrates this baseline **without its verbatim
   stdout** — the file §3 requires and the byte-identity evidence in §3 cites. Orchestrator action at
   integration: `git add -f` each baseline's `run.log` (or exempt the baseline roots in `.gitignore`;
   that edit is the orchestrator's call, not this seat's).
3. **Revision semantics.** The baseline is uncommitted at freeze time (wave rule), so `revision`
   names the base revision plus a `revision_note`; the carrying commit will be the orchestrator's
   round-9 integration commit. The revised `revision_note` now carries the HEAD detail; this seat
   reproduced it: `git diff --stat e1694bad…..HEAD` → `claims.json` 34 +, `targets.json` 125 +,
   159 insertions, 0 deletions — the graded artifact tree is identical between the two. If any byte
   of `tools/gates/naming-collision-gate.py` changes before integration, this baseline must read
   `gate_revised` (fail-closed) and be re-frozen as a **new** baseline (append-only, §3) — never
   edited in place.
4. **`gate_selftest` field** carries the author's observed summary string; this seat re-ran the
   selftest independently (§3 row 3) and the substance (exit 0, 12 findings / 11 ids) reproduces.

## 7. What this re-run does not claim

- Scope: the `naming-collision-gate` baseline only — nothing about the other six gates' baselines.
- The §5 battery runs validate discovery, digests and pins; the battery does **not** re-execute the
  naming verdict (`verdict_replay` is `not-run` by design) — the verdict comparison is §3 here.
- Digest verification is the interim **external** check (hashlib/`sha256sum`); the gate has no
  internal `--frozen` mode — measured, not assumed (same finding as the phonology rerun seat).
- A reproduced verdict is a byte-level measurement, not a design PASS and not canon: the 17 findings
  (incl. 10 PHON-INVENTORY over costume display strings) are review evidence for lore-shokunin,
  never a ruling, and this fragment stays inside that boundary (`PROVINCE.md`).
- The `/tmp` inode hazard is unchanged from round 8 (`df -i /tmp` → 1048576/1048576 used, 0 free at
  20:48Z); all this seat's work used `/var/tmp/r9-naming-rerun` on the root filesystem because a
  command run under `/tmp` would fail ENOSPC. Scratch is disposable; the four baseline files were
  never edited (digests in §1 re-measured after all controls).

**Verdict: reproduced — baseline r9-pre is valid at revision `a7bb205…`.** Digests match, the
verdict re-runs byte-identically in three independent settings (partial copy, pristine HEAD
archive, live path), determinism and tamper/gate-revision controls behave exactly as the standard
§6 requires, and the four notes in §6 route to the orchestrator.
