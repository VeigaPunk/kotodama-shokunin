# R20-D22 — capability-row draft: `handoff-e2e-v3` (SCORECARD paste-ready row)

- seat **R20-D22** (scribe, claim D), round 20 (operator: loop 2 of 3, build round
  4 of 4; `reports/round-20/claims.json`). Assignment, verbatim: "capability-row
  draft".
- writes: this file only (scratch under `.scratch/r20-d21/`). No commit, no push,
  no tool/example/SCORECARD/LOG edit; `reports/round-{8..19}/**` are filed and
  read-only here.
- canon: **NON-CANON engineering evidence. The row in §3 is a draft — the
  orchestrator admits it, if and when claim D's demonstrated run exists.**
- measurement tree: baseline revision
  `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d` (round-19 admit), declare revision
  `122086bce0aa577bec221bb2d37eedf20f4f3ed2`. All stamps UTC (lane clock
  UTC-03:00). `export TMPDIR=$PWD/.scratch` before every scratch write.
- status at this stamp: **complete for this shard's scope, revision 2 —
  before-state measured; after-state measured against the delivered profile
  CLI (tool `08ad1d75…`, baseline `e2bfa52a…`) at 2026-10-18T13:38–13:41Z; the
  one remaining gap (the v1 default path red on the claim-O projector pin) is
  named in §2/§4 rather than smoothed over.** The row is still a draft: the
  orchestrator admits it and owns routing that gap.

## 0. What this shard is and is not

One paste-ready SCORECARD capability row for the round-20 depth capability
`handoff-e2e-v3`, plus the exact commands and evidence paths by which each of
its clauses can be checked. It is not a claim of the capability, not an
acceptance run, and not a substitute for `reports/round-20/run-validation.py`
(claim D's counting command, owned by another seat). The row proposes the
successor to the round-11 `handoff-e2e` demonstration — or nothing, if that
state is not reached.

## 1. Before-state, measured (2026-10-18T12:57–12:59Z, lane root)

| # | command | observed |
|---|---|---|
| 1 | `python3 tools/exercise-handoff-e2e.py --quiet` | exit 0; `handoff-e2e: exit=0 fields=16/16 glossary=20/20 findings=0 packet_sha256=6583b6bdbf5e3fe039d1eee1d9f53d63ef09a04e3eeb5c98ae4943ed1771a64f` (receipt sha256 `46233a67…`) |
| 2 | `python3 tools/exercise-handoff-e2e.py --selftest` | exit 0; `selftest: OK — positive run … plus 17 controls` (receipt sha256 `3ffc034e…`) |
| 3 | `grep -c "culture-d4" tools/exercise-handoff-e2e.py` | **0** — the exercise reads no D4 byte |
| 4 | `sha256sum tools/exercise-handoff-e2e.py` | `a21934ade22b2cda338645ee389c7f848256348446d8a79f38a9c9ff827d2005` (the v2-era bytes) |

What the before state is: the round-11 exercise assembles and validates the
handoff envelope from the **21-file D2+D3 read set only**. The v2 semantic
dimension (per-claim uncertainty, resolving claim-to-record links) lives in
*separate* round-15 surfaces — `reports/round-15/handoff/packet-v2-05.{md,yml}`
judged by `tools/harness/packet_uncertainty.py` and `tools/harness/packet_links.py`
— not in the exercise, and the exercise's own claim ledger carries neither
dimension. The D4 drill (round 19, fully gate-verified 19/19) is carried by no
handoff packet at all.

The before state is green end to end (rows 1–2): this is a **capability
extension**, not a defect repair — the row's `before` clause is "the exercise
carries D2+D3; D4 is outside the handoff path".

## 2. After-state (the row's after clause) — measured, revision 2

Measured 2026-10-18T13:38–13:41Z from the delivered profile CLI (tool sha256
`08ad1d75f730fad19c73652187fe5c798d5bda39a07c3d8170d13b7f2ae823d0`; the tool
was rewritten inside the wave — revision 1's pins and its superseded baseline
are recorded in `reports/round-20/handoff/frozen.md` §1):

| # | command | observed |
|---|---|---|
| 5 | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 0; `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=e92f5e6775b657c24fa6260e340e4e7a04cf6c3777188cba80678bed079ae43b` |
| 6 | `python3 tools/exercise-handoff-e2e.py --profile v3 --selftest` | exit 0; `selftest: OK — positive run … plus 28 controls` |
| 7 | `python3 tools/exercise-handoff-e2e.py --profile v3 --freeze reports/round-20/handoff` | exit 0; baseline `e2bfa52a35e51858…` (profile `kotodama-handoff-e2e/3`), packet `e92f5e67…`, twin `58cb2460…`, **58 input pins**, `v2_subset_digest ad35c860…`, `alias_state landed` |
| 8 | `.scratch/d21-tamper.py` (eleven controls) | 11/11 PASS; committed baseline byte-unchanged |
| 9 | `python3 reports/round-20/run-validation.py --check` | C pass, O pass, **D fail — one leg: the v1 default run** (§4) |
| 10 | `python3 tools/exercise-handoff-e2e.py --profile v2 --quiet` | exit 0; `handoff-v2: exit=0 claims=15 links=50/50 drift=named(tools/harness/packet_links.py round-16)` |

What the after state actually is, against the row's wording:

- **The exercise now assembles from D2+D3+D4** in the v3 profile: 58-file read
  set (v1's 21 in place and in order), D4 manifest rows, **12 D4 claim rows**
  (rendered from `claims-map.md`) with `uncertainty {status, basis}` in the
  clause grammar, and `105/105` links resolving into `examples/culture-d4/`
  records; uncertainty findings 0.
- **Census 27 claims / 16-7-4**, `v2_subset=equal`, `alias_leg=landed`. The
  design §2's pre-flip table (15/7/5) differs in the supported/unresolved
  split because **D4-CL08 flipped to `supported` when the O alias evidence
  landed** — the design §4 flip rule, and the packet document
  (`packet-v3-16.md`) carries the same 16/7/4 histogram.
- **The v2 path is green** with a named allowance
  (`drift=named(tools/harness/packet_links.py round-16)`); the v2 packet bytes
  are unchanged.
- **The v1 default path is RED** (the one remaining D failure): the round-11
  baseline pins `tools/d2-typed-labels.py` at `0da0015f…`, the claim-O fix
  moved it to `76536a92…`, so the default run fails `input-digest`
  (`E2E-DIGEST`, exit 1). The O cascade re-pinned the v2 rows but not the
  round-11 baseline; `run-validation.py` requires the default run green. Owner:
  impl seat or the O cascade — a new v1 successor row or a named allowance
  mirroring the v2 profile's.

No value above is copied from `reports/round-20/handoff/design.md` §6 targets
or from `reports/round-20/run-validation.py`'s selftest fixtures; the design
targets are quoted only where they differ from the measurement.

## 3. The row draft (SCORECARD paste surface)

| axis | verdict | before → after / observation | re-run command | measured evidence |
|---|---|---|---|---|
| depth | improved (claim D, capability `handoff-e2e-v3`) | The exercise assembled the envelope from the D2+D3 read set only (21 files, 0 D4 mentions) → the profile CLI's v3 assembles from D2+D3+D4 (58-file read set): 12 D4 claim rows with `uncertainty {status, basis}` in the `grounding:/restriction:/open:/owner:` grammar, `105/105` links resolving into `examples/culture-d4/` records, 27-claim ledger 16/7/4, `v2_subset=equal`, `alias_leg=landed`, gate `16/16 + 20/20 + 0`; frozen baseline `reports/round-20/handoff/expected.json` `e2bfa52a…` with 58 input pins; eleven-control tamper matrix PASS; v2 profile green with a named round-16 allowance. **Limit: the v1 default path is red on the claim-O projector pin (`0da0015f…` → `76536a92…`), the one remaining counting-command failure.** | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet`; `python3 tools/exercise-handoff-e2e.py --profile v3 --selftest`; `python3 reports/round-20/run-validation.py` | `reports/round-20/handoff/{expected.json,packet.md,twin.json,freeze.txt,frozen.md}`; receipts `.scratch/r20-d21/{v3-verify-rev2.out,v3-selftest-rev2.out,tamper-matrix-rev2.out,validator-check-rev2.json}` |

## 4. Limits

- The row names a **computational** capability: it pins bytes, verdicts and
  counts. It does not certify any claim inside the packet, lore acceptance,
  canon standing, or a transfer clearance (all artifacts NON-CANON).
- The v3 read set includes D4 artifacts whose own verification belongs to the
  round-18/19 receipts; this row cites, and does not re-derive, that work.
- The summary line carries the design §6 `claims=`/`statuses=`/`v2_subset=`/
  `alias_leg=` tokens at revision 2; the census in this row is read from both
  the summary line and the frozen baseline (`expected.json`
  `uncertainty`/`counts`) and they agree (27 / 16-7-4).
- The tool was rewritten inside the wave (revision 1 → 2); the rev-1 pins and
  the superseded baseline are recorded in `reports/round-20/handoff/frozen.md`
  §1. If the tool or the read set moves again, this row's after clause must be
  re-measured and the baseline re-frozen as a **new** revision row with the
  reason recorded, never an in-place edit.
- Counts are point-in-time and re-measured before quoting.
