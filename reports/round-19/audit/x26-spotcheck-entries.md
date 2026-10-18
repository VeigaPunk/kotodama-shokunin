# X26 — spot-check audit: the round-19 C entries re-derived, and the filler auditor

- round 19 (operator loop 2 of 3, build round 3 of 4; 64 workers on
  `hyper/deepseek-v4-flash`) · seat **X26** (SCRIBE X26..X28 — spot-check
  auditors, >=6 new entries re-derived) · owner: L2 worker, kotodama-shokunin lane.
- assignment (verbatim): "SCRIBE X26..X28: spot-check auditors (>=6 new entries
  re-derived), coverage auditor (README vs files), lessons audit."
- date: 2026-10-18. Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`;
  baseline revision `e5718945a1ab0a0c3db955338d2cae77d68fd348`, HEAD `169c616`.
- canon: NON-CANON engineering evidence. This audit admits no entry, certifies no
  round, and blesses no source.
- writes: **this file** and its siblings `x27-coverage-readme-vs-files.md`,
  `x28-lessons-audit.md`, plus the read-only tooling and receipts under
  `reports/round-19/audit/`. No `corpus/` byte is edited by this seat. No commit,
  no push.
- measurement window: 2026-10-18T11:32Z–11:40Z UTC. The wave was live throughout;
  every reading names its stamp and is re-measurable.

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | **10 new entries** landed (5 verification + 5 synthesis) — claim C's `>=8, >=3 each` satisfied | measured (11:40Z) |
| 2 | **all 10 re-derived** against their own cited measurements (>=6 required) | **PASS** |
| 3 | QUALITY-bar audit: **8/10 clear**; the 2 failures are a single phantom `couples:` path | **finding X26-1** |
| 4 | every new entry is gap-named, frontmatter-complete, decision-record carrying, sourced | measured |
| 5 | filler auditor present (this file, §4): an entry naming no gap is rejected | control |

## 1. Method

Two read-only instruments plus manual re-derivation:

```sh
export TMPDIR=$PWD/.scratch
python3 reports/round-19/audit/entry-audit.py --since e5718945a1ab0a0c3db955338d2cae77d68fd348
python3 reports/round-19/audit/entry-audit.py --selftest   # in-memory controls
```

`entry-audit.py` checks each new entry against the lane's admission bar
(`corpus/QUALITY.md`) and claim C's requirements: header fields
(`topic`/`sources`/`couples` + `verified-at`/`recheck`), source-bullet locators,
`couples:` target resolution (brace-aware; resolved against the entry dir, the
lane root, and `corpus/knowledge/`), a named gap, a decision record, calibration
vocabulary, and canon hygiene. Selftest: 7/7 checks green, including a negative
control (an entry with no `sources` field fails the bar).

"Re-derived" means: **not** trusting the entry's own numbers, but re-running the
command it names (or re-reading the artifact it cites) at HEAD and comparing.

## 2. The 10 new entries, re-derived (11:36Z–11:40Z)

| entry | cited measurement | re-derivation (this seat, HEAD `169c616`) | match |
|---|---|---|---|
| `verification/label-channel-routing-verification.md` | three sha256 pins; projector `stats {fail 0, hold 15, labels 74, note 1}`; gate exit 0; selftest 39/39 | `sha256sum` → `d2-typed-labels.py` `0da0015f…`, `typed-labels.d4.yml` `a59990bb…`, `expected-holds.json` `09490a27…`; projector exit 1 with the same stats; `d4-typed-labels-check-gate` exit 0 `byte-identical deterministic projection` | **yes** |
| `verification/pre-declared-hold-set-reconciliation.md` | `expected-holds.json` `counts {hold 15, note 1, fail 0}`; projector stats | read → same counts, `packet_sha256 e7ecd204…`, `projection_sha256 a59990bb…`; projector stats equal | **yes** |
| `verification/generated-artifact-roundtrip-verification.md` | three `--check`/gate legs exit 0; typed selftest 39/39; assembly gate ships no selftest | `assemble-culture-d4.py --check` exit 0; `d4-assembly-check-gate` exit 0; `d4-typed-labels-check-gate` exit 0; `d4-assembly-check-gate --selftest` → exit 2 `No such file or directory: '--selftest'` | **yes** |
| `verification/gate-battery-surface-verification.md` | battery exit 0, `pass 7`, originals preserved, mirror removed | `check-gate-battery.py` → exit 0, `{battery_exit 0, fail 0, pass 7, unevaluable 0}`, `files_hashed_before/after 28`, `preserved true`, mirror removed | **yes** |
| `verification/two-reader-interop-agreement.md` | two D4 adapter legs exit 0 with the peers' own lines | both adapter gates exit 0 with `…: byte-identical deterministic {projection,assembly}` | **yes** |
| `synthesis/typed-label-routing-workflow.md` | coverage block: `typed_labels 74`, `labels_by_kind {native-form 56, translated-label 12, borrowed-strata 6}`, holds 12, fails 0; projector stats | read `typed-labels.d4.yml` `coverage` → identical block; projector stats equal | **yes** |
| `synthesis/generated-artifact-lifecycle.md` | the three `--check`/gate legs exit 0 | re-ran all three → exit 0 | **yes** |
| `synthesis/hold-set-contract-in-brief.md` | projector stats; `expected-holds.json` counts | equal | **yes** |
| `synthesis/era-material-scoped-reconciliation.md` | `d2-typed-labels.py --selftest` → exit 0, 39/39; coverage read | `--selftest` → exit 0, `39/39 checks passed`; coverage read | **yes** |
| `synthesis/finding-disposition-workflow.md` | projector stats; `expected-holds.json` counts | equal | **yes** |

**All 10 re-derived clean** — every cited digest, count, exit code, and
byte-identity line reproduces at HEAD. No entry overstates its evidence.

## 3. QUALITY-bar result

`entry-audit.py --since e571894…` (11:40Z): **8/10 clear the bar**. Every entry
carries all required header fields, locator-bearing sources, a named gap, a
decision record, and calibration vocabulary. The two failures are:

### X26-1 — phantom `couples:` path `../linguistics/phonology-sanity.md` (finding)

`corpus/knowledge/verification/label-channel-routing-verification.md:13` and
`corpus/knowledge/synthesis/typed-label-routing-workflow.md` both list
`../linguistics/phonology-sanity.md` in their `couples:` line. **That file does
not exist.** The linguistics partition holds `phonetics-phonology.md`; the file
actually named `phonology-sanity-gate.md` lives in the *verification* partition
(and both entries already list it there). So the reference is a phantom — wrong
partition and wrong name — almost certainly a copy-paste of the shared couples
template.

- Blast radius: 2 of 10 new entries fail the couples-resolution check on this one
  path; it does not affect the entries' substantive claims (all re-derived clean
  above).
- Control: `entry-audit.py` resolves `couples:` refs against three bases and
  reports unresolved targets; a correct target (`../linguistics/phonetics-phonology.md`
  or the already-listed `phonology-sanity-gate.md`) resolves and clears the check.
- Disposition: this is a correction for the integrator — per the lane rule,
  corrections are **new** files/rows, never in-place edits of landed bytes. The
  auditor does not edit the entries.

### X26-2 — the battery-surface entries state a now-false surface fact (finding)

`verification/gate-battery-surface-verification.md` codifies the battery's
surface as a **"seven-name constant"** and states, as an adopted reading (§4),
that the D4 legs are *outside* the battery. Its §6 marks the question
"should the D4 family join the battery's constant" as **open (to-verify)**,
owner "this lane's O axis". The round-19 README revision note repeats the same
sentence ("the D4 gate family is outside the battery's seven-name constant").

**But the same round's O work has already changed that surface.** At 11:35Z
`tools/check-gate-battery.py` carries `GATE_NAMES` (seven structural, duty 1) and
`D4_GATE_NAMES` (two D4 adapters) with `REGISTERED_GATE_NAMES = GATE_NAMES +
D4_GATE_NAMES` (nine) for duty 2; a default run reports baseline coverage
`"9/9"`, `gates_uncovered []`, 17/17 pinned. The file is a live edit
(`git status` shows `M tools/check-gate-battery.py`).

- The tension: the entry's `topic`/§4 assert a boundary the round has moved. Its
  own `recheck:` line anticipates this ("whenever the D4 family is added to the
  battery's surface (corrections are new entries, never rewrites)") — so the
  correct disposition is a **dated qualifier or a new entry**, not an in-place
  edit. The C entry and the O change are both defensible at their own stamps;
  a reader at close must not read the entry as the current surface.
- Distinguish the two duties, as the round-19 lesson does: duty 2 (baselines)
  reads 9/9; duty 1 (selftests) still runs only the **seven** structural gates,
  and **neither D4 gate ships its own selftest** (`d4-assembly-check-gate
  --selftest` → exit 2; `d4-typed-labels-check-gate --selftest` → exit 0 by
  forwarding into the peer's own selftest). "9/9" is a coverage statement, not a
  "9/9 with selftest controls" statement.
- This is reported, not adjudicated: whether the entry is superseded, qualified,
  or left as a dated reading is the parent's call.

## 4. Filler auditor (control for claim C §C4)

The round-19 validator's `measure_c` §C4 requires a **filler auditor**: a
round-19 file that (a) mentions "filler" and (b) names the **gap** discipline, so
an entry naming no gap it fills is rejected rather than admitted. This section is
that auditor.

**Rule.** An entry is *filler* when its `- gap filled:` / topic line names no gap
— i.e. it neither states what the partition lacked before it nor points at the
absence it fills. The check is mechanical and re-runnable:

```sh
python3 reports/round-19/audit/entry-audit.py --since e5718945a1ab0a0c3db955338d2cae77d68fd348
# an entry whose `gap_named` is False is rejected as filler
```

**Applied to the 10 new entries:** every one names a gap (all ten report
`gap=True`), and each cites an absence sweep or a named partition hole
(`reports/round-19/gaps.md` carries the ten declared gaps, one per author seat,
with a collision log). **No filler was admitted this round.** The negative
control is the tool's selftest: stripping the word "gap" from a sample entry flips
`gap_named` to False and the entry is rejected.

## 5. Limits

- Re-derivation re-runs the *commands the entries name*; it does not re-inspect
  the round-8/17/18 receipts the entries cite by path (those were read by path,
  not re-executed), and it does not judge design quality or canon.
- The `couples:` finding is about path resolution, not about whether the coupling
  is conceptually right; the entries' prose couplings are not audited here.
- Counts are point-in-time (2026-10-18) and are re-measured, never inherited,
  before being quoted.
