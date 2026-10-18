# R19-A18 — interop audit 2/2: handoff validators, the battery default run, and the battery↔counting-command contract (NON-CANON)

- seat: R19-A18 (interop auditor, handoff + battery surface). Lane:
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  Assignment (verbatim): *"AUDIT R19-A15..A18 (filler+interop auditors x4): … interop:
  D2/D3/D4 typed paths + handoff validators all green after battery changes; reports/round-19/
  audit-{1..4}.md"*.
- date: 2026-10-18 (lane-local UTC-03:00; stamps UTC). Readings **11:33–11:44Z** on a **live,
  actively edited** wave; §4 records the settle re-check. HEAD `169c616`; baseline
  `e5718945a1ab0a0c3db955338d2cae77d68fd348`.
- role limits: this seat executes the fixed checks and reports. Writes only `audit-3.md`,
  `audit-4.md`, `.scratch/audit/`. No gate, pin, packet or battery byte is changed by this seat.
- instrument: `.scratch/audit/interop.py` (`stdout_sha256` per check; `TMPDIR` outside the repo
  for `replay-frozen`). The round-19 counting command
  (`reports/round-19/run-validation.py`) is read as a peer artifact, never executed as my
  evidence and never modified.
- filler half of this seat's assignment: reported in `audit-1.md` / `audit-2.md` — the settled
  filler verdict is **10/10 entries pass, zero naming no gap**. This file carries the interop
  half (handoff validators + battery + the battery↔counting-command contract).

## 1. Verdict

**The handoff validators are all green and unchanged. The battery's D4 integration is
partially landed and, at this reading, its default run does not pass: it exits 2 because it now
runs `d4-assembly-check-gate.py --selftest`, which exits 2.** The battery and the counting
command were visibly converging during the window (the runner switched from reading
`summary.pass` to reading `baselines.summary.coverage`), but at 11:44Z they are **not yet
consistent** and claim O's `9/9` battery default does not hold. §4 re-measures after settle.

## 2. Handoff validators — all green

| check | exit | result | stdout sha256 |
|---|---:|---|---|
| `tools/gates/handoff-packet-check.py --selftest` | 0 | OK — 11 fixture findings across 9 ids; clean control exit 0; malformed inputs exit 2 | `be1ef058b2cfc67a…` |
| `tools/exercise-handoff-e2e.py --selftest` | 0 | positive + control matrix (tamper read-set/baseline/scan, missing artifact) | `3ffc034e8b1bf23a…` |
| `tools/exercise-handoff-e2e.py` (positive run) | 0 | `fields=16/16 glossary=20/20 findings=0 packet_sha256=6583b6bdbf5e3fe0…` | — |
| `tools/harness/packet_links.py --selftest` | 0 | 38 checks passed | `ff9712c316dadd65…` |
| `tools/harness/packet_links.py --packet reports/round-16/handoff/packet-v2-07.yml --json` | 0 | `links_checked 83, resolved 83, findings 0` | `c25ae1557ae32faf…` |
| `tools/harness/packet_uncertainty.py --selftest` | 0 | 19 checks passed | `a374464322a4f255…` |
| `tools/harness/packet_uncertainty.py --packet …packet-v2-07.yml` | 0 | `claims=15 findings=0` | `9dd9297da93fb34e…` |
| `tools/harness/receipt_guard.py --selftest` | 0 | `selftest_passed: true` | `ebcd138992803797…` |
| `tools/check-craft-exercise.py --selftest` | 0 | `10/10 tamper cases detected` + `18/18 CLI cases` | `77d408e10a494fa5…` |
| `tools/check-evidence-coupling.py --selftest` | 0 | `selftest_passed: true` | `cf62bc50e303b793…` |
| `tools/check-evidence-coupling.py examples/culture-d3/packet.json` | 0 | `findings: []`, profile `kotodama-d3-evidence-coupling/1` | `e282a06884980341…` |

The handoff contract (round-15 packet-v2-07) resolves 83/83 links with zero findings and 15
claims with zero uncertainty findings. No handoff validator was perturbed by the battery
changes. **This half of the assignment is green.**

## 3. The battery default run — D4 integration, partially landed (reading 11:44Z)

Command: `python3 tools/check-gate-battery.py` (JSON on stdout). Current shape:

| reading | value |
|---|---|
| `summary` | `{battery_exit: 2, fail: 0, pass: 8, unevaluable: 1}` |
| top-level `gates` ids | 9 — the 7 structural gates **plus** `d4-assembly-check-gate.py`, `d4-typed-labels-check-gate.py` |
| `baselines.summary` | `{coverage: "9/9", gates_registered: 9, gates_uncovered: [], baselines_found: 17, pinned: 17, baseline_exit: 0, unevaluable: 0}` |
| findings | `GATE-UNEVALUABLE-EXIT: selftest exited 2` on `d4-assembly-check-gate.py` |
| `--selftest` controls | **35/35 OK** (up from 29/29 at baseline; adds the `CTRL-D4-*` controls) |

- **Duty 2 (coverage) is fully landed and green.** The battery discovers 17 committed
  `expected.json` baselines, covers all 9 registered gates (`9/9`), leaves none uncovered, and
  pins all 17. The two D4 baselines are committed under the standard layout at
  `tools/gates/expected/d4-typed-labels-check-gate/r19-pre/expected.json` and
  `tools/gates/expected/d4-assembly-check-gate/r19-pre/expected.json`.
- **Duty 1 (selftests) is not green.** The battery now runs the D4 adapters' `--selftest`:
  - `d4-typed-labels-check-gate.py --selftest` → exit 0, `39/39 checks passed` (works: the
    adapter forwards to `tools/d2-typed-labels.py`, whose own `--selftest` runs).
  - `d4-assembly-check-gate.py --selftest` → **exit 2**,
    `assembly error: [Errno 2] No such file or directory: '--selftest'`. This gate has **no
    `--selftest` mode**: it treats its first argv element as the packet path and calls the
    assembler's `assemble()` against it, so `--selftest` reads as a missing file.
  - That single unevaluable child forces the battery's duty-1 to `unevaluable=1` and the
    combined exit to **2**.
- The battery's earlier docstring design ("the two adapters are deliberately excluded from
  duty 1: each resolves ROOT from its own location and loads a peer that lives outside the
  mirrored tree, so a mirrored `--selftest` launch could only report could-not-evaluate") is
  **inconsistent with the current code**, which does launch them under duty 1. The design note
  and the implementation have diverged.

## 4. The battery↔counting-command contract (claim O1)

The round's counting command `reports/round-19/run-validation.py` reads the battery document.
It moved during this window; at 11:44Z its O1 block (`:540-608`) requires:

1. battery `exit == 0` — **currently 2** → fails;
2. `summary.pass == len(LEGACY_GATES)` (7) — battery reports `8` → fails;
3. `summary.fail`/`unevaluable` in `(0, None)` — `unevaluable=1` → fails;
4. `baselines.summary.coverage == "9/9"` and `gates_registered == 9` — **passes**;
5. `gates_uncovered` empty, `baseline_exit == 0` — **passes**;
6. both D4 gates in `baselines.summary.gates_covered` and in the baseline list — **passes**.

So at 11:44Z the runner would fail claim O on items 1–3. Note items 1–3 are exactly the
consequence of the duty-1 D4-selftest problem in §3; item 2 additionally shows the battery's
`pass=8` (it counts the D4 typed gate's passing selftest) against the runner's expected 7
structural.

**Disposition (routed, not this seat's call):** either
(a) `d4-assembly-check-gate.py` gains a `--selftest` mode (exit 0 with a stable `N/N checks
passed` line, matching the typed adapter and the runner's O2 regex), **or**
(b) the battery excludes both D4 adapters from duty 1 and reports them only through duty 2
coverage (restoring its documented design), and the runner's `summary.pass` expectation is set
to the structural count. Either resolves items 1–3; the two artifacts must agree on which.

This is reported as an **open integration finding**, not a defect of either artifact alone: the
battery and the counting command are two round-19 artifacts encoding different contracts for
the same field.

## 5. Settle re-check (2026-10-18T11:45:59Z; worktree hash `071b5acf90a2` stable ×3)

**The handoff half is green at settle (§2 unchanged, same exit codes and shas). The battery
finding in §3–§4 is UNRESOLVED at settle: the battery still exits 2, and the counting command
still requires exit 0.**

Settled readings (11:46Z):

| reading | value |
|---|---|
| `check-gate-battery.py` | `{battery_exit: 2, fail: 0, pass: 8, unevaluable: 1}` — stdout sha `bb83d30d53b50ccc…` |
| battery `gates` ids | 9 (7 structural + 2 D4) |
| battery `baselines.summary` | `coverage "9/9"`, `gates_registered 9`, `gates_uncovered []`, `baselines_found 17`, `pinned 17`, `baseline_exit 0`, `unevaluable 0` |
| battery finding | `GATE-UNEVALUABLE-EXIT` on `d4-assembly-check-gate.py` |
| `check-gate-battery.py --selftest` | **35/35 OK** (sha `5beae67e79f425f2…`) |
| `d4-typed-labels-check-gate.py --selftest` | exit 0, `39/39 checks passed` |
| `d4-assembly-check-gate.py --selftest` | **exit 2**, `assembly error: [Errno 2] No such file or directory: '--selftest'` |
| D4 baselines | `tools/gates/expected/d4-{typed-labels,assembly}-check-gate/r19-pre/expected.json`; both `gate_sha256` pins verified against the live gates; real input digests incl. peer tools + components; `expected {class: clean, exit: 0, findings: []}` |

So the claim-O contract is **not met at settle**: `reports/round-19/run-validation.py`
(`sha256 86c4906c6fb7d53d…`, `BATTERY_GATE_TOTAL = 9`) checks battery `exit == 0`,
`summary.pass == len(LEGACY_GATES)` (7) and `fail`/`unevaluable ∈ (0, None)`; the battery
returns `exit 2`, `pass 8`, `unevaluable 1`. Items 4–6 of §4 (the `coverage 9/9`,
`gates_registered`, `gates_covered` reads) **do** pass, so duty 2 is fully landed and only the
duty-1 D4-selftest leg blocks.

**Routed to the parent as the single blocking integration finding** (with `audit-3.md` clean):
either `d4-assembly-check-gate.py` gains a `--selftest` mode (exit 0 with a stable
`N/N checks passed` line), or the battery drops both D4 adapters from duty 1 and the runner's
`summary.pass` expectation is set to the structural count. Both artifacts are round-19 files;
they must agree on one contract before claim O can read green.

Also noted at settle, outside this file's scope: `SKILL.md` is **byte-unchanged from baseline**
(`e8d238a6…` at settle), so the claim-D landings (`reports/round-19/knowledge/skill-draft-a/b.md`)
are not integrated — the parent's post-wave integration step, not a validator finding.

## 6. Limits

- The counting command is read, never executed by this seat as evidence; the O1 requirement list
  above is a read of its source at the stated revision (`sha256 a2db3fbcc82f6e30…` at 08:39:58,
  revised again to `86c4906c6fb7d5…` at 08:41 — bind the revision, not the summary). Its own
  verdict lives in `reports/round-19/validation.json` once it runs.
- All readings are on a live, actively edited wave; §5 re-binds. Non-canon; read-only.
