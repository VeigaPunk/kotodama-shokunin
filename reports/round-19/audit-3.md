# R19-A17 — interop audit 1/2: the D2 / D3 / D4 typed paths and the D4 gates (NON-CANON)

- seat: R19-A17 (interop auditor, typed/assembly surface). Lane:
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
  Assignment (verbatim): *"AUDIT R19-A15..A18 (filler+interop auditors x4): … interop:
  D2/D3/D4 typed paths + handoff validators all green after battery changes; reports/round-19/
  audit-{1..4}.md"*.
- date: 2026-10-18 (lane-local UTC-03:00; stamps UTC). Readings **11:33–11:39Z** on a live
  wave; §5 settle re-check. HEAD `169c616`; baseline `e5718945a1ab0a0c3db955338d2cae77d68fd348`.
- role limits: this seat executes and measures the fixed checks and reports. It writes only
  `audit-3.md`, `audit-4.md` and `.scratch/audit/`; it changes no gate, no pin, no artifact.
- method: `.scratch/audit/interop.py` (each check launched as a fixed argv with `shell=False`
  in its own `TMPDIR`; `stdout_sha256` recorded per check). The `replay-frozen` check runs with
  an **outside** `TMPDIR` because `tools/replay-frozen.py` refuses an in-repo mirror root by
  design (`reports/round-18/run-validation.py` note). Instrument JSON:
  `.scratch/audit/interop.json`.
- filler half of this seat's assignment: reported in `audit-1.md` (verification partition) and
  `audit-2.md` (synthesis partition + wave roll-up) — the settled filler verdict is **10/10
  entries pass, zero naming no gap**. This file carries the interop half only.

## 1. Verdict

**The D2, D3 and D4 typed/assembly paths are green and byte-stable.** Every typed surface is
byte-identical to the baseline revision, so every verdict below is the round-18 behaviour
reproduced, not a new result. One path — the D4 typed packet graded *directly* — exits 1, but it
did so in round 18 with the **same stdout digest**, so it is a pre-existing, pinned condition,
not a round-19 regression.

## 2. Byte-stability of the typed surface (O4 precondition)

Every component of the typed family is unchanged from HEAD (command: `git show HEAD:<f> |
sha256sum` vs live `sha256sum`, 11:38Z):

| surface | baseline = live | note |
|---|---|---|
| `tools/gates/typed-pipeline-gate.py` | `04ad4bb47956…` SAME | generalized gate, round-18 bytes |
| `tools/gates/typed-pipelines.json` | `434e90509a1c…` SAME | declared-pipeline profile |
| `tools/d2-typed-labels.py` | `0da0015f7003…` SAME | projector |
| `tools/assemble-d2.py` / `assemble-d2-typed.py` | SAME | D2 serializer / adapter |
| `tools/assemble-culture-d3.py` | `ba8d19d5855f…` SAME | D3 assembler |
| `tools/assemble-culture-d4.py` | `943f487ba991…` SAME | D4 assembler |
| `tools/assemble-d4-typed.py` | `087846719041…` SAME | D4 adapter |
| `tools/gates/d4-typed-labels-check-gate.py` | `05f99629d870…` SAME | D4 thin gate |
| `tools/gates/d4-assembly-check-gate.py` | `df1a364b3970…` SAME | D4 thin gate |
| `examples/culture-{d2,d4}/*` (packets, projections, typed packets, expected-holds) | SAME | all seven artifacts byte-identical |

Consequence for claim O's "no gate behavior change without documented reason": for the typed
family the stronger statement holds — **no byte changed at all**. The only gate file that moved
in round 19 is `tools/check-gate-battery.py` (audited in `audit-4.md`).

## 3. Typed-path matrix (11:36–11:39Z)

| check | exit | result | stdout sha256 |
|---|---:|---|---|
| `tools/gates/typed-pipeline-gate.py --selftest` | 0 | 12/12 checks passed | `22ce048a65288088…` |
| `typed-pipeline-gate.py` (D2 default) | 0 | **16/16 legs** | `15cdfbda73cd56cb…` |
| `typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0 | **19/19 legs** | `ec9d6d3b61120ef6…` |
| `typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | **1** | 14/16 legs (L3-routing-consistency red) | `765fa267db346430…` |
| `tools/gates/d4-assembly-check-gate.py` | 0 | `packet.d4.yml: byte-identical deterministic assembly` | `c60820a54742ecaa…` |
| `tools/gates/d4-typed-labels-check-gate.py` | 0 | `typed-labels.d4.yml: byte-identical deterministic projection` | `1c8add321259a9f0…` |
| `tools/assemble-d2.py --check` | 0 | `packet.d2.yml: byte-identical deterministic assembly` | `2fa0c8c197459f54…` |
| `tools/assemble-culture-d3.py --check` | 0 | `packet.json` + `packet.gates.yml`: byte-identical | `e20620fabdf28532…` |
| `tools/replay-frozen.py tools/gates/frozen/round-18/MANIFEST.tsv` | 0 | **2/2 rows reproduced** | `331719a0a8ab5643…` |

- **D2 default 16/16 and D4 packet 19/19** reproduce round-18's declared legs exactly. The D2
  default is byte-identical in behaviour, as claim O requires.
- **The D4 typed packet graded directly** (`packet.d4.typed.yml`) exits 1 with
  `FAIL L3-routing-consistency`; the detail names `naming-collision-gate.py` DERIV-REPLAY
  failures on `NM-01..NM-07`. This is **not** a round-19 regression: round 18 recorded the same
  command at exit 1 with stdout sha256 `765fa267db3464309622e1ba47fb47418af616d887ac331c7744981215999e76`
  (`reports/round-18/validation.json` → `claims.O.measurement.declared_runs.typed-run`), and my
  re-run reproduces that digest **exactly**. The typed packet's own `--check` build path is the
  green one (the D4 gate rows in §3 above and `replay-frozen` ROW 2/3); grading the delivered
  typed packet *as input* is the path that reads red, by design of the L3 routing leg.
- **`replay-frozen` reproduces both round-18 D4 rows** (typed-labels gate over
  `typed-labels.d4.yml`, assembly gate over `packet.d4.yml`), `exit 0/0`, `bytes=match`. This is
  the strongest single interop result for the D4 family: the frozen generation replays green
  under the round-19 tree.

## 4. What this does and does not show

- Shows: the typed/assembly family was not perturbed by round 19; the D4 gates remain
  gate-shaped and pinned; the frozen D4 rows replay; the D2 path is unchanged.
- Does **not** show: that the D4 typed packet graded directly *should* be red — that is a design
  reading of the L3 routing leg, and the round-18 record already carries it. It also does not
  re-run the round-18 validator (a filed receipt); the exit-1 pin is quoted from
  `reports/round-18/validation.json`, which is a filed artifact read by path.

## 5. Settle re-check (2026-10-18T11:45:59Z; worktree hash `071b5acf90a2` stable ×3)

**§2 byte-stability holds at settle: every typed surface and every typed artifact is still
byte-identical to HEAD, and §3's matrix reproduces with the same exit codes and the same
`stdout_sha256` values.** Final matrix (`.scratch/audit/interop.json`, 11:46Z):

| check | exit | stdout sha256 |
|---|---:|---|
| `typed-pipeline-gate.py --selftest` | 0 | `22ce048a65288088…` |
| `typed-pipeline-gate.py` (D2 default) | 0 | `15cdfbda73cd56cb…` |
| `typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0 | `ec9d6d3b61120ef6…` |
| `typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | 1 | `765fa267db346430…` (= round-18 pin) |
| `d4-assembly-check-gate.py` | 0 | `c60820a54742ecaa…` |
| `d4-typed-labels-check-gate.py` | 0 | `1c8add321259a9f0…` |
| `assemble-d2.py --check` | 0 | `2fa0c8c197459f54…` |
| `assemble-culture-d3.py --check` | 0 | `e20620fabdf28532…` |
| `replay-frozen.py …/round-18/MANIFEST.tsv` | 0 | `331719a0a8ab5643…` (2/2 reproduced) |

**Settled verdict: the D2/D3/D4 typed and assembly paths are fully green and byte-stable.**
The single exit-1 path (D4 typed packet graded directly) is unchanged from round 18 at the same
digest. The only typed-surface delta of round 19 remains zero bytes.

## 6. Limits

- Verdicts bind the §2 digests and the 11:36–11:39Z window. Exit codes and `stdout_sha256` are
  measured, not asserted; the one quoted round-18 digest is read from a filed receipt, not
  recomputed by a historical runner.
- Read-only: no gate, pin, packet or projection was modified by this seat. Non-canon.
