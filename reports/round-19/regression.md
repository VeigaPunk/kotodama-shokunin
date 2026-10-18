# Round 19 — Regression report (R29-O13 / R29-O14)

- **Seats:** R29-O13 and R29-O14 (regression ×2). **Lane:**
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
- **Date:** 2026-10-18, local clock UTC−03:00. Observation window
  **08:32:00–08:41:00 -03:00**.
- **Revision binding:** lane `HEAD = 169c616613899f7ba86b8fb58ed808bdfd4b5ccd`
  ("round-19: declare claims D/C/O", 2026-10-18T08:30:39-03:00);
  `HEAD^ = e5718945a1ab0a0c3db955338d2cae77d68fd348` = the declared
  `baseline_revision` (round-18 admit). The declare commit is the baseline's
  direct child, so the graded tree is identical at both.
- **Role limits:** this seat executes and measures only. It decides no
  admission, promotes no claim, certifies no canon/source content. Its only
  writes are this file and scratch under `.scratch/r19-regression/`
  (`TMPDIR=$PWD/.scratch` exported for every in-repo scratch command;
  `TMPDIR` outside the repo for `replay-frozen.py`, which refuses an in-repo
  mirror root by design). No git mutation, no commit, no push, no write outside
  the lane, no filed-round byte of rounds 8–18 touched.
- **What "regression" means here:** the authoritative contract is the O5 block
  of the round's counting command, `reports/round-19/run-validation.py:643-669`
  (13 fixed items). This file runs that contract, extends it with the frozen
  replays and the full typed/assembly selftest sweep, and reports every nonzero.

## 0. Verdict

**Two genuine reds. F-O13-2 is the round-19 claim-O blocker; F-O13-1 is outside
the O5 contract.** The validator's O5 regression contract — the 13 fixed items of
`reports/round-19/run-validation.py:643-669` — is green, and so are craft, the
typed/assembly `--check` paths, `replay-frozen --selftest` and the frozen
`round-18` replay. But the **battery default run is RED at the closing stamp**,
and the battery default run is exactly what claim O's O1 leg grades.

**F-O13-2 (claim-O blocker) — the battery default run regresses to exit 2.**
`python3 tools/check-gate-battery.py` → **exit 2**, `pass: 8, unevaluable: 1`,
finding `GATE-UNEVALUABLE-EXIT` on `d4-assembly-check-gate.py`. The validator
(`reports/round-19/run-validation.py:576-590`) requires that run to exit 0 with
`pass ∈ {7, 9}` and `unevaluable ∈ {0, None}`; **8 fails all three**, so claim O's
O1 leg fails at this stamp. Full before/after in §1, root cause in §5.

**F-O13-1 (outside the O5 contract)** — `python3 tools/assemble-d4-typed.py
--selftest` → **exit 1, 4/11** on the committed baseline bytes
(`087846719041db0ba32c005a34a6075c452e122a1f7b7bc4527ae4e0bfc4d798`). Its
production path is green (`--check` exit 0); only its selftest mirror is broken.
The O5 block does **not** name this tool, so it is not itself the claim-O
blocker — but claim O's prose ("keeps every typed/assembly selftest … green",
`reports/round-19/run-validation.py:23-24`) is broader than the O5 set, so it is
a real gap between the claim text and its check. See §3 and §5.

Two further nonzeros are **expected, not defects**: **N1**
(`d4-assembly-check-gate.py --selftest` → exit 2 — the same root cause as
F-O13-2) and **N2** (round-11 replay's one documented `gate_digest_mismatch`).
No lane byte was edited by this seat: both reds are routed, not absorbed.

| suite | command | result |
|---|---|---|
| battery default | `python3 tools/check-gate-battery.py` | **exit 2 — RED (F-O13-2)**; pass 8, unevaluable 1; coverage 9/9 |
| battery selftest | `… --selftest` | exit 0 — `SELFTEST OK 35/35` |
| craft | `tools/check-craft-exercise.py --selftest` | exit 0 — 10/10 tamper + CLI 18/18 |
| evidence coupling | `tools/check-evidence-coupling.py --selftest` | exit 0 — `selftest_passed: true` (32 cases) |
| typed/assembly selftests | 9 invocations (§3) | 7 green, **1 red (F-O13-1)**, 1 red (N1) |
| typed/assembly checks | 8 invocations (§3) | all exit 0 |
| frozen replay round-18 | `replay-frozen.py …/round-18/MANIFEST.tsv` | exit 0 — 2/2 reproduced |
| frozen replay round-11 | `replay-frozen.py …/round-11/MANIFEST.tsv` | exit 2 — 10 reproduced, 1 expected (N2) |

## 1. Battery — default run RED at the closing stamp (claim O's O1)

The battery script moved twice inside this window, and **the movement is the
finding**, so both readings are recorded with their stamps.

**Reading A (08:35:16 → 08:38, GREEN and validator-compliant).**
`python3 tools/check-gate-battery.py` (default roots, `TMPDIR=$PWD/.scratch`) →
**exit 0**; `summary {battery_exit: 0, pass: 7, fail: 0, unevaluable: 0}`;
`originals {added: 0, deleted: 0, modified: 0, files_hashed_before: 28,
files_hashed_after: 28, preserved: true}`; baseline coverage **9/9**
(`baselines_found: 17, pinned: 17, gates_registered: 9, gates_uncovered: []`,
`gates_covered` = the seven structural gates + both D4 adapters). `… --selftest`
→ exit 0, `SELFTEST OK 34/34`. Script digest
`sha256 = 72d6e0116a775ab4bc771de32e3763885d97341532cf745de6f0f316aa940094`.
This is the design the validator's O1 accepts as **`pass == 7` + coverage `9/9`**
(`reports/round-19/run-validation.py:578-581`).

**Reading B (08:40:08 → closing, RED — F-O13-2).**
`python3 tools/check-gate-battery.py` → **exit 2**;
`summary {battery_exit: 2, pass: 8, fail: 0, unevaluable: 1}`; per-gate outcomes
`[(7 structural gates, exit 0, pass), (d4-typed-labels-check-gate.py, 0, pass),
(d4-assembly-check-gate.py, 2, unevaluable)]`; findings
`[{"id": "GATE-UNEVALUABLE-EXIT", "gate": "d4-assembly-check-gate.py",
"detail": "selftest exited 2"}]`. Baseline coverage still **9/9**, `pinned: 17`,
`unevaluable: 0`. `… --selftest` → exit 0, `SELFTEST OK 35/35`. Script digest
`sha256 = 83d9e3e5ce49d936e94c40a2df38b4a4fa480343241069db31cad66f7058cd1b`
(git: `M tools/check-gate-battery.py`, uncommitted, mtime 08:40:08).

**Why B is red.** The 08:40 revision moved the two D4 adapters from duty 2
(baseline coverage) into duty 1 (the selftest leg): `leg_plan()` now launches
them from their live paths as `[python3, tools/gates/<gate>.py, "--selftest"]`
(`tools/check-gate-battery.py:208-224`), and the docstring states the policy
plainly — "An adapter that cannot answer `--selftest` is not worked around here
— the leg reports could-not-evaluate and the battery exits 2"
(`tools/check-gate-battery.py:45-48`). `d4-typed-labels-check-gate.py` answers
(39/39, exit 0); **`d4-assembly-check-gate.py` does not** — it is flagless, its
CLI is `[PACKET]` only (`tools/gates/d4-assembly-check-gate.py:29-40`), so
`--selftest` is read as an input path and exits 2. The battery therefore reports
`pass: 8`, and the validator fails it three ways: `exit != 0`, `pass ∉ {7, 9}`,
`unevaluable != 0` (`reports/round-19/run-validation.py:576-590`). Note the
validator deliberately accepts **either** nine selftests (`pass 9`) **or** seven
selftests with the 9/9 coverage reading (`pass 7`); reading A satisfies the
second, reading B satisfies neither.

**Preservation unchanged.** Both readings report `originals.preserved: true`
(28 files hashed before and after, 0 added/deleted/modified).
**Unchanged gate:** `sha256(tools/gates/d4-assembly-check-gate.py) =
df1a364b3970365c217a9b6a16f075bab854ee87aefab831de50df4a9d71544a` (mtime
07:25:18 — no seat has touched it across the whole window, so the missing
`--selftest` is not in flight).

## 2. Craft

| command | exit | headline |
|---|---|---|
| `tools/check-craft-exercise.py --selftest` | 0 | `SELFTEST OK 10/10 tamper cases detected` + `CLI-SELFTEST OK 18/18 cases passed` |
| `tools/check-evidence-coupling.py --selftest` | 0 | `"selftest_passed": true`, `"note": "all committed-input selftest cases passed"`; 2 positive + 2 domain controls, 2 frozen + 2 malformed cases, 32 results |
| `tools/exercise-handoff-e2e.py --selftest` | 0 | `selftest: OK — positive run (exit 0, fields=16/16, glossary-entries=20, findings=0)` + 17 controls |
| `tools/source-audit-inventory.py --selftest` | 0 | `SELFTEST PASS` (planted entries, exact counts, no-write + determinism) |
| `tools/replay-frozen.py --selftest` | 0 | `selftest: 79/79 checks passed` |

## 3. Typed / assembly selftests and checks

**Selftests (the full sweep — this is the list F-O13-1 lives in):**

| tool | `--selftest` |
|---|---|
| `tools/gates/typed-pipeline-gate.py` | exit 0 — 12/12 |
| `tools/gates/d4-typed-labels-check-gate.py` | exit 0 — 39/39 |
| `tools/d2-typed-labels.py` | exit 0 — 39/39 |
| `tools/assemble-d2-typed.py` | exit 0 — 11/11 |
| `tools/assemble-d2.py` | exit 0 — 42/42 |
| `tools/assemble-culture-d3.py` | exit 0 — 85/85 |
| `tools/assemble-culture-d4.py` | exit 0 — 81/81 |
| `tools/assemble-d4-typed.py` | **exit 1 — 4/11 (F-O13-1)** |
| `tools/gates/d4-assembly-check-gate.py` | exit 2 — no `--selftest` (N1 → F-O13-2) |

**Checks (conformance paths, `--check` / default run):**

| command | exit | stdout |
|---|---|---|
| `tools/gates/typed-pipeline-gate.py` | 0 | `summary: 16/16 legs passed` |
| `tools/gates/d4-typed-labels-check-gate.py` | 0 | `examples/culture-d4/typed-labels.d4.yml: byte-identical deterministic projection` |
| `tools/gates/d4-assembly-check-gate.py` | 0 | `examples/culture-d4/packet.d4.yml: byte-identical deterministic assembly` |
| `tools/d2-typed-labels.py --check` | 0 | byte-identical deterministic projection |
| `tools/assemble-d2-typed.py --check` | 0 | byte-identical deterministic typed packet |
| `tools/assemble-d2.py --check` | 0 | byte-identical deterministic assembly |
| `tools/assemble-culture-d3.py --check` | 0 | packet.json + packet.gates.yml byte-identical |
| `tools/assemble-culture-d4.py --check` | 0 | byte-identical deterministic assembly |

`typed-pipeline-gate.py` also runs the **D4** packet green:
`python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`
→ exit 0, `summary: 19/19 legs passed` (the round-18 "19/19" reading, still
reproduced here).

## 4. Frozen replays (round-18 + round-11)

`TMPDIR` must be **outside** the repo (`tools/replay-frozen.py` refuses an
in-repo mirror root by design). All replays below ran with
`TMPDIR=/tmp/r19-regression-outside`.

- **round-18** — `tools/gates/frozen/round-18/MANIFEST.tsv`
  (`3688e8bc5e67e74039758515b849b61e0759f22dfd770c7f0770ee43ca1db68b`):
  **exit 0, `REPLAY OK: 2/2 rows reproduced the recorded verdicts`.** Rows: the
  two D4 adapters (`d4-typed-labels-check-gate.py`, `d4-assembly-check-gate.py`),
  both recorded exit 0 / 0 findings.
- **round-11** — `tools/gates/frozen/round-11/MANIFEST.tsv`
  (`aad230bfdcc1bfe4cc137339b47daf0154208b6c69225e0c0a4505ce52532063`):
  **exit 2 — `10 reproduced, 0 mismatch, 1 could-not-evaluate of 11`.**
  The single unevaluable row is line 2, `tools/gates/typed-pipeline-gate.py`:
  `reason: gate_digest_mismatch` — pinned `d102fd1d…` (round-11 bytes) vs live
  `04ad4bb479562c419b48d750a8f9303c4a5a717ca7f2fe3b3658cc1bb9578a48`. Rows 3–12
  reproduce (including the two recorded reds, naming 17 and 7 findings, and
  phonology 3).
- **Cross-reference (why round-11's mismatch is expected, not a regression):**
  `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` — the append-only re-pin
  generation — replays **exit 0, `REPLAY OK: 11/11 rows reproduced`**, and its
  row 1 pins the **live** gate `04ad4bb4…`. So the round-11 row-1 pin names the
  pre-generalization gate revision and is superseded by a new file, exactly as
  round-18 declared: "The round-11 generation's typed row is EXPECTED to read
  could-not-evaluate/gate_digest_mismatch once the gate is generalized … The
  row's filed bytes are never edited." (`reports/round-18/validation.json:7007`).

## 5. Findings

### F-O13-2 — the battery default run is RED (exit 2, 8 pass + 1 unevaluable) — GENUINE, claim-O blocker

**Evidence.** `python3 tools/check-gate-battery.py` (default roots, HEAD,
`TMPDIR=$PWD/.scratch`, 2026-10-18 08:40:08 → 08:50 -03:00, stable across ~9 min
of 60 s polling) → **exit 2**, `{pass: 8, unevaluable: 1}`,
`GATE-UNEVALUABLE-EXIT` on `d4-assembly-check-gate.py`. Script digest
`83d9e3e5ce49d936e94c40a2df38b4a4fa480343241069db31cad66f7058cd1b` (uncommitted:
`git status` → `M tools/check-gate-battery.py`).

**Root cause.** The 08:40 revision added the two D4 adapters to the duty-1
selftest leg (`leg_plan()`, `tools/check-gate-battery.py:208-224`) and made a
non-answering adapter a hard failure by policy
(`tools/check-gate-battery.py:45-48`). `d4-typed-labels-check-gate.py` answers
`--selftest` (delegates to `d2-typed-labels.py`, 39/39); `d4-assembly-check-gate.py`
does not — it is a flagless `[PACKET]` gate
(`tools/gates/d4-assembly-check-gate.py:29-40`), so it exits 2. The battery
regresses from reading A (exit 0, `pass 7`, §1) to reading B (exit 2, `pass 8`).

**Impact — this fails the round's own counting command.** Claim O's O1 leg
(`reports/round-19/run-validation.py:576-590`) requires the default run to exit 0
with `pass ∈ {7, 9}` and `unevaluable ∈ {0, None}`; reading B violates all three.
Claim O therefore cannot admit at this stamp.

**Fix and its control (not applied by this seat — writes are restricted to this
file).** Two equivalent routes: (a) give `tools/gates/d4-assembly-check-gate.py`
a `--selftest` that exits 0 (mirroring the `assemble-culture-d4.py --selftest`
positive/tamper controls, and copying `tools/assemble-d2.py` into the mirror as
`tools/assemble-culture-d4.py:557` does), or (b) revert the battery to reading A
(adapters in duty 2 only). Control either way: `python3 tools/check-gate-battery.py`
must exit **0** with `pass ∈ {7, 9}`, `unevaluable == 0`, coverage `9/9`.

**Routing.** This is the highest-value red in this report: it is inside the O5
contract's subject matter (the battery) and it blocks claim O. Left for the
parent to route to the O-battery seat or a fix seat.

### F-O13-1 — `tools/assemble-d4-typed.py --selftest` is red (exit 1, 4/11) — GENUINE

**Evidence.** `python3 tools/assemble-d4-typed.py --selftest` (HEAD, 2026-10-18
08:34 -03:00) → **exit 1**:
`selftest: 4/11 checks passed — failures: positive: --emit exit 0; determinism:
two builds byte-identical; --check: exit 0 on the build; tamper: --check exit 1
on a changed byte; tamper: restored build passes; stale projection: exit 2 and
the pin is named; routing: the checked field is moved, not flagged`.
Digest of the tool at this stamp:
`sha256(tools/assemble-d4-typed.py) = 087846719041db0ba32c005a34a6075c452e122a1f7b7bc4527ae4e0bfc4d798`
(mtime 08:21:01 -03:00, unchanged across the window — no concurrent seat is
editing it).

**Root cause (two independent defects, both inside the selftest, neither on the
production path):**

1. **The selftest mirror omits the serializer peer.** The mirror copy loop at
   `tools/assemble-d4-typed.py:409-410` copies `assemble-d4-typed.py`,
   `assemble-culture-d4.py`, `d2-typed-labels.py` and one gate — but **not**
   `tools/assemble-d2.py`, which the loaded `assemble-culture-d4.py`'s
   assembler-identity leg requires. Every mirror-launched build therefore dies
   `exit 2: FAIL assembler_identity: assembler refused the components: required
   file not found: tools/assemble-d2.py`, cascading into the first five failures.
   The sibling tool proves the intended shape: `tools/assemble-culture-d4.py:557`
   does `shutil.copyfile(SERIALIZER, tmp / "tools" / "assemble-d2.py")` in its
   own mirror, and its selftest is green (81/81).
2. **The routing check's guard compares the wrong operands.** At
   `tools/assemble-d4-typed.py:238-240` the routing row sets
   `owed_slot = owed_slot(slot) if record_key == slot else None`; with
   `record_key = "GAR-99"` and `slot = "LEX-GAR-99, (to-verify)"` the guard is
   false, so `owed_slot` is `None` and the check at line 477
   (`routing[0]["owed_slot"] == "LEX-GAR-99"`) fails. Observed routing row:
   `{'record': 'GAR-99', … 'off_channel_field': 'garment_gloss', 'hold':
   'D2L-FORM-UNRESOLVED', 'owed_slot': None}`.

**Control (the red is test-only).** The production path is green on the same
bytes: `python3 tools/assemble-d4-typed.py --check` → exit 0,
`examples/culture-d4/packet.d4.typed.yml: byte-identical deterministic typed
packet`; `--emit` writes 89554 bytes / 12 routing rows, exit 0. So the defect
cannot produce a wrong artifact — it only makes the tool's own selftest
un-runnable, which is why no earlier receipt caught it: round-18 measured the
`--emit` leg (`reports/round-18/validation.json:618-623`, exit 0) and never ran
`--selftest`.

**Fix and its control (not applied by this seat — writes are restricted to this
file).** Add `"assemble-d2.py"` to the copy loop at
`tools/assemble-d4-typed.py:409-410`, and compare the owed slot name rather than
the record key at line 238 (e.g. attach the row's owed slot when
`owed_slot(slot) == label_id`, or compare `slot_owner`). Control: re-run
`python3 tools/assemble-d4-typed.py --selftest` and require **11/11, exit 0**,
with `--check` still exit 0 and the D4 typed packet byte-unchanged.

**Routing.** Outside the O5 contract (`reports/round-19/run-validation.py:644-663`
does not name this tool), inside claim O's prose (`run-validation.py:23-24`,
"every typed/assembly selftest … green"). Left as a finding for the parent to
route to a fix seat or to scope explicitly; not absorbed.

### N1 — `d4-assembly-check-gate.py --selftest` exits 2 — expected for the gate, but it is F-O13-2's trigger

`tools/gates/d4-assembly-check-gate.py` is a **flagless** adapter by design: its
CLI is `[PACKET]` only (`tools/gates/d4-assembly-check-gate.py:29-40`), so
`--selftest` is read as an input path and reads
`assembly error: [Errno 2] No such file or directory: '--selftest'`, exit 2. In
isolation this is not a defect: the gate's conformance evidence is its committed
`expected.json` baseline and its frozen round-18 row (§4). But it is precisely
the invocation the 08:40 battery revision now makes mandatory, so this same exit
2 is what turns the battery red — see **F-O13-2**. The gate is unchanged across
the window (mtime 07:25:18), so no fix is in flight.

### N2 — round-11 replay line 2 reads `gate_digest_mismatch` — EXPECTED

Documented in §4 and in `reports/round-18/validation.json:7007`; the append-only
re-pin is `tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv` (11/11 green, pins
the live gate). No round-11 byte was or should be edited.

## 6. Commands (all 2026-10-18, window above)

- Battery: `python3 tools/check-gate-battery.py` and `… --selftest`
  (`TMPDIR=$PWD/.scratch`); full JSON captured at
  `.scratch/r19-regression/battery.json`.
- Craft/checks: the §2–§3 rows, captured as
  `.scratch/r19-regression/results.json` by `.scratch/r19-regression/run-all.py`.
- Replays: `TMPDIR=/tmp/r19-regression-outside python3 tools/replay-frozen.py
  tools/gates/frozen/round-18/MANIFEST.tsv`; same for `…/round-11/MANIFEST.tsv`
  and `…/round-18/repin-d2/MANIFEST.tsv`.
- Digests: `sha256sum tools/assemble-d4-typed.py tools/gates/d4-*.py
  tools/gates/typed-pipeline-gate.py tools/check-gate-battery.py
  tools/replay-frozen.py tools/gates/frozen/round-{11,18}/MANIFEST.tsv`;
  `git rev-parse HEAD`.
- Defect isolation: `python3 tools/assemble-d4-typed.py --check` (exit 0);
  `… --emit .scratch/r19-regression/d4-emitted.yml` (exit 0, 89554 bytes);
  `sed -n '395,445p' tools/assemble-d4-typed.py`;
  `sed -n '545,575p' tools/assemble-culture-d4.py`.
- Battery before/after (F-O13-2): `python3 tools/check-gate-battery.py` run at
  08:35:16 (exit 0, `pass 7`) and re-run every 60 s from 08:40 to 08:50 (exit 2,
  `pass 8`, `unevaluable 1`) with `stat -c %y tools/check-gate-battery.py` and
  `stat -c %y tools/gates/d4-assembly-check-gate.py` beside it to prove the
  change landed and no gate fix followed. JSON captured at
  `.scratch/r19-regression/battery.json` (reading A) and
  `.scratch/r19-regression/battery-final.json` (reading B).

## 7. Compliance self-attestation

This seat wrote only `reports/round-19/regression.md` and scratch under
`.scratch/r19-regression/` (`TMPDIR=$PWD/.scratch` exported for in-repo scratch;
`TMPDIR` outside the repo for `replay-frozen.py` per that tool's own guard). No
git mutation, no commit, no push, no write outside the lane repo, no filed-round
byte of rounds 8–18 touched, no tool under `tools/` edited, no historical
validator executed. F-O13-1 and F-O13-2 are routed, not repaired in place.
