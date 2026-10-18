# X28 — lessons-partition audit (round 19)

- round 19 (operator loop 2 of 3, build round 3 of 4; 64 workers on
  `hyper/deepseek-v4-flash` per `reports/round-19/claims.json`) · seat **X28**
  (SCRIBE X26..X28 — lessons audit) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X26..X28: spot-check auditors (>=6 new entries
  re-derived), coverage auditor (README vs files), lessons audit."
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  baseline revision `e5718945a1ab0a0c3db955338d2cae77d68fd348`, HEAD `169c616`
  ("round-19: declare claims D/C/O").
- canon: NON-CANON engineering evidence. This audit admits nothing, certifies no
  round, and blesses no lesson.
- writes: **this file**, its siblings `x26-spotcheck-entries.md` /
  `x27-coverage-readme-vs-files.md`, and the read-only tooling + receipts under
  `reports/round-19/audit/`. No `corpus/lessons/**` byte, no filed round-8..18
  byte, and no tool or gate is edited by this seat. No commit, no push.
- measurement window: 2026-10-18T11:32Z–11:42Z UTC. The wave was live throughout;
  every reading names its stamp and is re-measurable.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | lesson census: **20 lesson files**, rounds 1–19 (round-5 twice; `supplement-opencode-1.md` non-round; round 13 operator-skipped) | measured |
| 2 | `## Gate` section present in **15 of 20**; absent only in rounds 1–4 (pre-contract seed lessons) and round 16 | measured |
| 3 | **the round-19 lesson path was rewritten inside the audit window** by two colliding seats (a Gate-less 291-line version → the 205-line gate-keeper survey) | **finding X28-1** |
| 4 | historical lessons carry **stale repo-path references** (files later renamed / never written); round-19's two are a pending glob and a not-yet-written receipt | **finding X28-2** (informational) |
| 5 | every round lesson carries a `source:` line; the round-19 lesson is `cd3b8c13…` (205 lines, mtime 11:41Z) | measured |

## 1. Method

Read-only tool `reports/round-19/audit/lessons-audit.py` (stdlib only):

```sh
export TMPDIR=$PWD/.scratch
python3 reports/round-19/audit/lessons-audit.py            # census summary
python3 reports/round-19/audit/lessons-audit.py --json     # receipt (receipt-lessons.json)
python3 reports/round-19/audit/lessons-audit.py --selftest # in-memory controls
```

The tool extracts the `## Gate` block (bounded by the next `## ` heading),
counts opening-reading lines (`Opening <axis> reading:`), `Admitted`/`Rejected`
markers and a `spot-check` mention, and resolves every backticked repo path
against the live tree. Selftest: 5/5 checks green.

## 2. Census (2026-10-18T11:42Z, `receipt-lessons.json`)

- Lesson files: **20** (`corpus/lessons/*.md`).
- Rounds with a lesson: **1–12, 14–19** (round 13 operator-skipped; round 5 has
  two files; `supplement-opencode-1.md` is not round-numbered).
- `## Gate` present: rounds **5, 5, 6, 7, 8, 9, 10, 11, 12, 14, 15, 17, 18, 19**
  and `supplement-opencode-1` = **15 of 20**. Absent only in rounds **1, 2, 3, 4**
  (pre-contract seed lessons) and **16**.
- Opening-reading lines (`Opening <axis> reading:`): rounds 14, 15, 17, 18, 19.

## 3. Findings

### X28-1 — the round-19 lesson path was rewritten inside the audit window (finding)

The audit read `corpus/lessons/round-19.md` twice and got **two different
files**:

| stamp | digest | lines | shape |
|---|---|---|---|
| 11:36Z | (read, not yet hashed) | 291 | *Opening census*, *The D4 craft, codified*, *Live observations*, *Integration guidance*, *Limits*, *Boundary record* — **no `## Gate`** |
| 11:41Z | `cd3b8c13…` | 205 | *Opening census*, *Dated "before" controls*, **`## Gate`** (Opening D/C/O readings), *Gate-keeper closeout rule*, *Subsequent observations*, *Boundary record* |

The second version is the gate-keeper survey landed by seat **X21**; the first
was an earlier draft. The current lesson's own §"a dispatch collision on this
seat's own path" records the cause: `corpus/lessons/round-19.md` was assigned to
**both** R19-D08 (claim D's "D4 lesson entry") and X21 (the gate-keeper survey),
and X21's survey superseded D08's draft, which now sits unintegrated at
`reports/round-19/integration/d4-lessons-entry.md`.

- Consequence for the audit: a lesson census is only meaningful against a pinned
  digest. This report's §2 census binds to `cd3b8c13…`; the earlier Gate-less
  reading is **superseded** and is not a defect of the current file. The
  disposition of the collision (append D08's text as a distinct section, or land
  it at a new path such as `corpus/lessons/round-19-d4-craft.md`) is the
  parent's — the current lesson's Gate item D-4 already routes it there.
- The current lesson **does** carry a Gate with three opening readings (D, C, O),
  each naming its declared threshold and its `reports/round-19/claims.json`
  source, and a "Gate-keeper closeout rule" that explicitly declines to admit a
  claim from the model, the allocation, fragment counts, or a self-reported
  green. That is the contract shape the round-14 lessons audit expects.

### X28-2 — historical lessons carry stale repo-path references (informational)

Path-resolution sweep over all 20 lessons found references to files that do not
exist at HEAD:

| lesson | missing reference | note |
|---|---|---|
| `round-9.md` | `reports/round-9/rerun.json` | never written under that name |
| `round-11.md` | `examples/culture-d2/typed-gate.expected.json`, `tools/typed-gate-flow.py` | superseded / never landed |
| `round-14.md` | `reports/round-12/adjacency/entries.md` | round-12 layout differs |
| `round-15.md` | `reports/round-15/handoff/packet-v2.yml`, `tools/build-handoff-v2.py` | live file is `packet-v2-05.yml` |
| `round-17.md` | `reports/round-17/civ-map.json` | round-17 civ output is under `reports/round-17/civ/` |
| `round-18.md` | `reports/round-18/repin/MANIFEST.tsv`, `tools/gates/frozen/round-18-repin/MANIFEST.tsv` | repin manifest path differs |
| `round-19.md` | `reports/round-19/entries/R19-C1x.md` (glob), `corpus/lessons/round-19-d4-craft.md` (the proposed alternative path), `reports/round-19/validation.json` (**pending** — runner not yet written) | round-19 is a live artifact |

These are **historical/aspirational references**, not live defects: filed
lessons of rounds 8–18 are read-only by the lane's own rule ("moving bytes are
superseded, never silently inherited"), and the round-19 entries are pending or
proposed. Control: a dated resolution map (or the round-19 Gate closeout
observation) should carry the resolutions rather than editing filed lesson
bytes. The round-19 pending reference clears when
`reports/round-19/run-validation.py` writes its receipt.

## 4. Cross-reference

The round-19 lesson cites this audit's own file
(`corpus/lessons/round-19.md` §"a dispatch collision …": `head -30
reports/round-19/audit/x28-lessons-audit.md`). At that stamp the audit's §0
carried the Gate-less finding, which the rewrite superseded — the lesson and
this audit were measuring the same moving path. The corrected §2/§3 above are
the re-measurement.

## 5. Limits

- This is a structural and path-resolution audit. It does not re-execute any
  lesson's census commands, does not re-verify a lesson's domain claims, and does
  not adjudicate whether a lesson's prose is correct.
- The Gate-presence and digest readings bind to the stamps in §2; the round-19
  lesson is a live wave artifact and a later re-read is a new measurement.
- Counts are point-in-time (2026-10-18) and are re-measured, never inherited,
  before being quoted.
