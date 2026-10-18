# Round 22 — loop-2 retrospective (rounds 17–21)

Prepared **2026-10-18** by C05–C06. Axes: **calibration**, with operability,
depth and adjacency evidence kept distinct. This is a recorded-outcome
checkpoint over the build/verify rounds, not independent promotion verification
or a round-22 admission. The amended loop is rounds **17–24**; integration and
the GLM rounds are not silently counted as completed by this checkpoint
(`LOG.md:3073-3076`). All artifacts from rounds 8–21 remain historical.

## Recorded final states and count boundaries

The filed receipts and parent closure records agree on **four admissions
(18, 19, 20, 21), one rejection (17)** and **14 passing / one failing claim
flags**. These are historical harness/parent decisions, not 14 independently
certified literal contracts. Read-only census **M1**, measured **2026-10-18**,
re-extracts these values without running a historical validator.

Every round below has the historical counting command
`python3 reports/round-N/run-validation.py`, dated **2026-10-18**, in its own
`claims.json` and `validation.json`. That identifies the filed instrument; it
is not permission to invoke a receipt-writing runner in the live lane.

| round | recorded final state / claim flags | demonstrated result and qualification | evidence |
|---|---|---|---|
| 17 — build 1 | **REJECTED**; C/coverage and O PASS, D FAIL | Civ work records seven fixed entries / five attempted replacements / 16 fragments; D4 assembler selftest 81/81 and deterministic assembly pass. The filed D receipt reports missing typed/projection/expected/frozen evidence. Later landed files and a projection run do not turn that receipt into an end-to-end pass. | `reports/round-17/validation.json`; `reports/round-17/claims.json`; `reports/round-17/reviews/review-4.md`; `LOG.md:3223-3240` |
| 18 — build 2 | **admitted**; O/D/C PASS | Generalized gate and D4 adapter supply an executable chain; D4 gate 19/19, emitted expectation 15 holds + one note, and D2 compatibility pass. New civ-map revision has 94 rows. This repairs the executable boundary, not every literal pre-implementation promise from round 17. | `reports/round-18/validation.json`; `reports/round-18/d4/holds.md`; `reports/round-21/recount/r18-1.md`–`r18-4.md`; `LOG.md:3242-3256` |
| 19 — build 3 | **admitted**; D/C/O PASS | D4 craft knowledge, ten entries (verification 15→20; synthesis 24→29), and battery registration land. The later recount finds baseline-binding and replayability-of-the-runner defects; an admission receipt is not a clean later-tree replay. | `reports/round-19/validation.json`; `reports/round-21/recount/r19-1.md`–`r19-4.md`; `reports/round-21/report-draft.md:15`; `LOG.md:3258-3271` |
| 20 — build 4 | **admitted**; D/O/C PASS | Handoff v3 adds D4, alias-family dependency is repaired, README reconciled. Keep filed 102/102 links separate from later 105/105, and declared linguistics 20 separate from measured 19. Candidate selection, malformed aliases and inherited rank payload remain distinct defects. | `reports/round-20/validation.json`; `reports/round-21/recount/dispositions.md`; `reports/round-21/adjacency/ledger.json`; `LOG.md:3273-3284` |
| 21 — verify | **admitted**; C/calibration, O, A PASS | Recount and discrepancy dispositions, defect queue and source-boundary audit are admitted. Audit success does not clear the filed D2→D4 contamination or accept the handoff. Freshness/depth/coverage are not claimed moves. | `reports/round-21/validation.json`; `reports/round-21/recount/ledger.json`; `reports/round-21/defects/ledger.json`; `reports/round-21/adjacency/ledger.json`; `LOG.md:3286-3296` |

This consolidation incorporates `reports/round-22/retro/r17.md`,
`reports/round-22/retro/r18.md`, `reports/round-22/retro/r19.md` and
`reports/round-22/retro/r20-21.md`. Their four read-only `python3 -B` reproduction
blocks were re-executed concurrently on **2026-10-18 14:46:13Z**, all exit 0.
The C07/C08 audit fragments supply independent pointer/number controls; their
version/hash-specific findings are not blanket approval of later edits.

For row-specific counts, the cited filed measurements carry command/date pairs.
The independent command/date controls are in
`reports/round-21/recount/audit.md` (2026-10-18). Its **23 distinct sampled
command strings** are a sample, not the whole recount. M1 finds **63 recount
rows = 39 matches + 24 dispositions**, with **52 distinct literal command
strings**. The validator's 63 source requirements and this 52-string set use
different units; neither means 63 independent exact matches. No unqualified
“100% reproduced” reading is justified by 100% match-or-disposition coverage.

### Coverage, provider and instrument limits

- **The map is not 94 fresh certifications:** M1 (2026-10-18) verifies r18's
  **94 rows / 12 transitions / 82 carried verbatim**, raw statuses **83 current /
  11 stale-fixed**, and the five r17 attempt rows still named in the receipt.
  Terminal labeling as 94 current uses different semantics from seven changed
  locators / five attempted replacements. Retain reasons and evidence, not a
  newly invented twelve-fix or freshness-axis result (`reports/round-22/retro/r18.md`).
- **Credit r19's outputs, not an unmeasured provider advantage:** the Hyper
  substitution returned useful SKILL/corpus/battery work. Completion figures
  are parent-reported, availability still leaves completion null, and no
  matched-task latency, token/cost or operator-time measurement proves a
  performance/cost gain. The span between declaration and close commits also
  includes waiting/integration, not inference latency. The command/date and
  qualified comparison are in `reports/round-22/retro/r19.md`, **2026-10-18**.
- **A zero process exit can still be a failed recheck:** r19's compact runner
  counts untracked rather than delivered committed entries, leaves old
  per-claim measurements in its refreshed receipt, and reports exit 0 while
  acceptance is false in r21's isolated recheck. Its ten actual additions are
  independently supported by Git-diff counts, not that status selector
  (`reports/round-22/retro/r19.md:72-78`). Ordinary gate positives also do not
  close the separately routed executable-path/expected-set trust boundaries.
- **Reader surfaces are not interchangeable:** the historical independent
  markdown reader's 92/92 links are separate from build-16's filed 102/102
  and the later machine pair's 105/105. Mtime selection explains which artifact
  the runner evaluated, not a license to collapse every historical count or
  field-preservation difference into one number (`reports/round-22/retro/r20-21.md`).

### Baseline-binding correction — append, never rewrite

Claims, declaration commits and closure labels must remain different fields.
M1 and revision control M2 (2026-10-18) establish:

| round | declared baseline in claims | filed receipt baseline | declaration incorrectly used as baseline in closure prose |
|---|---|---|---|
| 17 | `f30b6f8188937632bbedd0e7b29aeefff6f8b07b` | same | `9b49a4a` |
| 18 | `3dd3754207032cb81f5fb3e202fe85cf79211339` | same | `c66ac3c` |
| 19 | `e5718945a1ab0a0c3db955338d2cae77d68fd348` | **`169c616` — mismatch** | `169c616` |
| 20 | `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d` | same | `122086b` |
| 21 | `35b6797b42d48bec52e1e3ddba1f3afc9bb85046` | same | `8115eaa` |

This new table corrects metadata, not old receipts or outcomes. In particular,
round 19 has a receipt-binding defect, not merely abbreviated closure prose.
Round 20's intermediate runner/receipt mismatch was later rebound; its final
runner digest match does not repair round 19's baseline or prove measurement
correctness (`reports/round-21/defects/ledger.json`).

## The r17-rejection / r18-repair arc — a qualified repair

**Did round 18 verify what round 17 claimed? It verified the executable repair,
but not the full original contract without qualification.**

- **What genuinely improved:** round 17's D declaration required brief →
  components → typed projection/packet → gate equality and frozen replay.
  The filed receipt has no usable typed chain. Normalizing the era shape made
  the projector run, but the D2-bound identity leg and absent D4 adapter still
  prevented an accepted pipeline. Round 18 generalized identity selection,
  supplied `tools/assemble-d4-typed.py`, and exercised the emitted expectation.
  `reports/round-21/recount/r18-1.md` and `r18-3.md` independently reproduce
  **19/19 D4 legs** and **byte-identical D2 output** (commands and date:
  `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`
  and the default gate at before/after revisions, **2026-10-18**).
- **The goalposts are visible, not erased:** r17's delivered brief declares
  **six holds / zero notes**; the separate weigh-court design fragment declares
  **17 holds / one note**. Round 18 instead verifies the emitted **15 holds /
  one note**, a target expressly named in r18's own D declaration. The six
  garments plus their six slot rows account for 12 form holds; inherited D2
  constants supply three rank holds and one note. `reports/round-18/d4/holds.md`
  §§2–5 records the extraction, commands, date and deltas; §7 leaves declaration
  authority with the parent. Written reconciliation is not evidence that the
  original no-import boundary or a unique pre-implementation set was satisfied.
- **The later source-boundary finding matters:**
  `reports/round-21/adjacency/ledger.json` files `A21-D4-XF-01`: the D4 view
  carries D2 rank-source citations/material despite D4's no-import rule.
  Round 18's derivation already disclosed these constants; disclosure and
  deterministic equality were useful, but neither made the output family-clean.
  The source repair belongs to round 22 D, not a retrospective rewrite of r17
  or r18. A shared `D2L-*` diagnostic name alone is not fixture contamination;
  the foreign records, citations and ownership assertions are the defect.
- **Replay claims have generation boundaries:** the original r18 D4 manifest
  recorded **2/2** check rows, not a frozen full typed-pipeline row
  (`reports/round-18/d4/replay.md`, command/date **2026-10-18 10:41Z**).
  Later r20 projector changes leave it **1/2**, exit 1, while the r18 D2
  successor replays **11/11**, exit 0. Commands/date:
  `python3 tools/replay-frozen.py tools/gates/frozen/round-18/MANIFEST.tsv --json`
  and `python3 tools/replay-frozen.py tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv --json`,
  **2026-10-18**, `reports/round-21/defects/regression.md:52-68`.
  The D2 successor does not itself supersede the D4 row. The new
  `reports/round-22/fixes/r18-supersession.md` supplies
  `R22-O11-SUPERSESSION-1` at immutable post-r20 revision `cd9c8e4`:
  its original stale-row negative is **1/2**, its new-row positive **2/2**, and
  a zeroed-digest manifest refuses before launch (commands and date
  **2026-10-18 14:40:46–14:42:24Z** in that note). That documentation
  disposition preserves the original mismatch and does not pin the later
  moving-r22 source repair. Calling every historical replay green is false.
- **The r17 clone question is not missing civ evidence:** r21's recount
  ledger/X04 draft identify an absolute-path `.scratch` filter, while its
  disposition prose still calls the mechanism unproven. The new
  `reports/round-22/fixes/snapshot-r17.md` resolves this by documentation with
  an isolated control, not a frozen-runner edit. Its reproduction command on
  **2026-10-18 14:40:46Z** verifies **16/16** tracked fragments present and
  hash-matching, yet the original scanner returns **zero**. Rebasing only its
  enumeration root to `Path('.')` yields **16 fragments / seven fixed / five
  attempted**, and restoring the original helper restores zero. Protected
  paths stay unchanged. This demonstrates a sufficient scanner mechanism and
  supersedes the unproven-mechanism disposition; it does not reconstruct the
  transient original clone, refresh its receipt, or re-admit r17. Earlier
  evidence remains at `reports/round-21/recount/ledger.json:1-84`,
  `reports/round-21/recount/dispositions.md:5-9` and
  `reports/round-21/report-draft.md:11`.

Thus r17 **stays rejected**. R18's admitted executable capability is real and
independently reproducible at its measured revisions; the older “its artifacts
are now fully verified” phrase is too broad if read as literal r17 conformance,
a repaired predeclared contract, or an assertion that every later replay is green.

## Conformance-defect classes and dispositions

This taxonomy groups the **23 filed r21 ledger entries**, not 23 repairs or
23 open defects. M1 (2026-10-18) finds classification totals
**nine conformance / seven process / seven bookkeeping**, and statuses
**13 open / five closed / five observation**. The validator's **18 routes**
are all non-closed rows, including observations, not 18 open defects. These
counts preserve the filed queue; round-22 dispositions are additional records.
The wider `reports/round-21/defects/routed.md` carries more review-level items,
and the primary round-22 six-item O worklist is yet another unit.

| class | filed entries (each counted once) | disposition / control and remaining limit |
|---|---|---|
| K1 — revision, baseline and receipt binding | `R17-BASELINE-METADATA`, `R18-BASELINE-METADATA`, `R19-BASELINE-RECEIPT-BINDING`, `R20-BASELINE-METADATA`, `R20-INTERMEDIATE-RECEIPT-BINDING` | Four baseline issues remain open in the filed queue; the final r20 runner binding is an observation with a successful hash control. The new correction table plus M1/M2 distinguish declaration from baseline without altering history. R22 must disposition the baseline class; hash agreement is not correctness. |
| K2 — execution isolation, snapshot/scanner context and filed-byte preservation | `R17-CURRENT-RECOUNT-DISCREPANCY`, `R20-HISTORICAL-RECEIPT-REWRITE` | Both filed open. R22's `fixes/snapshot-r17.md` now resolves the scanner mechanism with complete-clone and counterfactual-root controls; a current-tree failure does not revoke an archived decision. R20's transient r9 receipt overwrite was restored, but restoration is not prevention. Historical validators run only in disposable in-lane clones, with protected-byte comparisons before/after. |
| K3 — declared versus delivered pipeline / frozen generation / test surface | `R17-HISTORICAL-D-REJECTION`, `R18-ORIGINAL-FROZEN-REPLAY`, `R19-ADAPTER-SELFTEST`, `R19-BATTERY-UNEVALUABLE-GATE` | R17's executable gap, adapter selftest and battery mismatch are bounded closed by later controls. R18 replay was filed open; `reports/round-22/fixes/r18-supersession.md` now names its historical successor at a pinned post-r20 revision, with original/new/tamper replay controls. This is not the final moving-r22 generation. R21 regression records adapter 12/12, seven battery selftests and nine baseline-covered gates; do not equate registrations with tests or D2 replay with D4 replay. |
| K4 — family isolation and malformed-data fail-open | `R19-MIRROR-FAITHFULNESS-WART`, `R20-MALFORMED-ALIAS-FAIL-OPEN` | The foreign-tree dependency is closed by a D4-only mirror and D2 byte-identity control; list-valued alias stringification remains open in the filed queue. The helper probe is not a full CLI refusal. R22 needs a valid alias positive plus malformed full packet/CLI negative; fixing alias dependency does not close the separate rank-payload bleed. |
| K5 — staffing, fallback and artifact ownership | `R17-ROUTE-CAPACITY`, `R19-SCRIBE-SEAT-FAILURE`, `R19-LESSON-PATH-COLLISION`, `R20-FRAGMENT-INDEX-COLLISION` | Declaration arithmetic is bounded closed by r18; actual r17 attendance is still to-verify. Scribe fallback, lesson collision and canonical index choice stay open with parent/dispatcher owners. Require a named fallback trigger/owner, retained authorship and an explicit resolving pointer; peer landings alone do not choose authority. |
| K6 — final-report provenance | `R18-FINAL-REPORT-POINTER`, `R19-FINAL-REPORT-POINTER`, `R20-FINAL-REPORT-POINTER` | All observations. Repo-only searches do not prove external reports absent; no external fleet paths are inspected here. Keep authorized final-report pointers to-verify until the integrator has evidence. |
| K7 — measurement contract, candidate selection and declared figures | `R20-CONTRACT-AUDIT-RECOUNT`, `R20-HANDOFF-LINK-COUNT`, `R20-LINGUISTICS-DECLARED-COUNT` | Audit/link items filed open; linguistics is an observation. R21 dispositions tie audit/link differences to same-build candidates selected by mtime. R22 needs content-based selection plus an inverted-mtime control and exact packet/twin binding. Preserve 102 archived versus 105 later links and 20 declared versus 19 live entries; documented causes are not equal measurements. |

Additional findings are **not inserted into that 23-entry historical count**:
`A21-D4-XF-01` belongs to the separate adjacency ledger; lost v3 edge
`declared_in` belongs to the handoff audit and the primary O worklist.
Round 22 must couple the source-level D4 fix to a family-clean ownership/citation
control, and edge restoration to a v2/v3 edge-payload comparison plus a
field-deletion negative. Re-pins are **new rows/files**, never replacements.
This retrospective does not itself claim these technical controls have passed.

The primary **six O items** are edge payload loss, mtime selection,
malformed alias coercion, the r17 clone/scanner attribution, r18 D4 replay
supersession, and baseline-binding drift (`reports/round-22/claims.json`,
2026-10-18; read-only count in M1). Their settlement belongs to
`reports/round-22/routed-resolution.json` and the assigned dated control reports.
The separate D source fix is not a seventh historical O route. Closing that
primary worklist must not be advertised as closing every review-level debt.

## Operator amendments, provider substitution and execution evidence

The inherited shorthand is **two structural regimen amendments plus one
provider substitution**, not two total amendment commits or two new amendments
during rounds 17–21. M2 (2026-10-18) resolves the original commits:

- `51e590100f7bb3c2d30f5cc9e91a0ad981505179`: add GLM end rounds.
- `94377884a78a73ad5396acb0d5f48a539a7a0448`: explicitly designate r19's
  `hyper/deepseek-v4.1-flash` provider, retaining the model family.
- `3dba77a722c6a2e885447a47971205fd97c11605`: cancel expand rounds and pin
  GLM worker/effort settings; r13 is operator-skipped.

The source is `LOG.md:3048-3080`, not inferred requested-model strings.
`reports/round-19/availability.json` leaves `completed_workers: null`, while
parent closure prose reports completion counts. Retain that attribution gap:
requested/allocated seats, scratch markers, parent-reported completions and
actual dispatch/wire-model evidence are different channels. No provider failure,
additional swarm or independently measured attendance is invented here.

## Restated freshness-threshold question — operator decision still pending

**For future build-round freshness claims, which preregistered, revision-bound
instrument should apply: raw byte stability on a quiet pinned tree, a declared
semantic/exit comparison, or a separately reported change-aware budget? What
threshold and denominator apply, and how are legitimate change, environment
and actual defects kept visible rather than normalized away?**

Loop-2 data strengthens the need for an explicit contract, not a looser
retroactive threshold:

- **The original failure remains:** r11 has 147 stable / 189 comparable =
  77.7778%, or 147 / 192 all rows = 76.5625%; both miss 95%. M1 re-extracts
  these values (2026-10-18). R17–21 have no freshness-axis move declarations;
  source repair under C/coverage does not silently end the pause.
- **The r20 audit window is not a new stable-tree score:**
  `reports/round-20/ledger-snapshot.md` §§1–2 records 192 attempted rows,
  176 rerun and 16 carried; among the 176, 110 byte-identical, 15
  convention/value-identical, 50 moved with named causes and one intentional
  command reconstruction. Commands/date: its `rerun.py` / `fullcap.py`
  invocations, **2026-10-18 13:01–13:10Z**, with a dirty, moving tree.
  The carried/prose/scratch-input rows do not become successes. Do not divide
  a mixed “acceptable” numerator by a selectively reduced denominator.
- **Environment and meaning can diverge:** the r17 `.scratch` scanner question,
  missing ignored replay log, mtime-based r20 audit selection and volatile
  temp paths show that identical revisions alone do not guarantee identical
  instruments. Conversely, a deterministic projection can still carry foreign
  D2 material and a green link census can omit an edge field.
- **Change-aware still needs failures:** r21's 63 rows contain 39 matches and
  24 dispositions (M1); all mismatches explained is not 100% byte stability.
  R18's old D4 replay is non-green despite later green D2 successors. The
  disclosed linguistics figure defect and alias fail-open must remain defects.

Before dispatch, name baseline and evaluation revisions, the settled
measurement window, exact commands/inputs and count unit, comparable/no-hash
and carried populations, stdout/stderr/exit streams, any normalization,
authorized re-pins/supersession, and the failure threshold. Required negative
controls include an exit-only regression, a semantic/finding loss, a missing
input/non-executable command, a changed candidate mtime, an omitted ignored
replay prerequisite and a receipt-writing side effect. Protect original bytes
independently of command output. **No option or new threshold is selected
here; r11 and r17 remain rejected and freshness-axis moves stay paused.**

## Reproduction controls

### M1 — read-only historical census and anti-inflation controls

Measured **2026-10-18**. Run from the lane root; this reads JSON and Git blobs
only, without importing a validator or touching its receipt. Assertions reject
promoting r17, counting dispositions as exact matches, rewriting the queue's
status totals, or treating r19's declaration as its declared baseline.

```sh
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
from collections import Counter
from datetime import datetime, timezone
from pathlib import Path
import json, subprocess
load = lambda p: json.loads(Path(p).read_text())
base = load('reports/round-22/claims.json')['baseline_revision']
accept = {17: False, 18: True, 19: True, 20: True, 21: True}
flags, states = Counter(), Counter()
for n, expected in accept.items():
    p = f'reports/round-{n}/validation.json'
    v, c = load(p), load(f'reports/round-{n}/claims.json')
    assert Path(p).read_bytes() == subprocess.check_output(['git', 'show', base + ':' + p])
    assert v['acceptance_checks_passed'] is expected
    assert set(v['claims']) == {r['id'] for r in c['claims']}
    flags.update(r['passed'] for r in v['claims'].values())
    states['admitted' if expected else 'rejected'] += 1
    assert not any(r['axis'] == 'freshness' for r in c['claims'])
    if n != 19:
        assert c['baseline_revision'] == v['baseline_revision']
    else:
        assert c['baseline_revision'] == 'e5718945a1ab0a0c3db955338d2cae77d68fd348'
        assert v['baseline_revision'] == '169c616'
        assert c['baseline_revision'] != v['baseline_revision']
    print(n, expected, {k: r['passed'] for k, r in v['claims'].items()},
          c['baseline_revision'], v['baseline_revision'])
assert states == {'admitted': 4, 'rejected': 1}
assert flags == {True: 14, False: 1}
q = load('reports/round-21/defects/ledger.json')['entries']
assert len(q) == len({r['id'] for r in q}) == 23
assert Counter(r['classification'] for r in q) == {'conformance': 9, 'process': 7, 'bookkeeping': 7}
assert Counter(r['status'] for r in q) == {'open': 13, 'closed': 5, 'observation': 5}
rows = load('reports/round-21/recount/ledger.json')
assert len(rows) == 63
assert Counter(r['verdict'] for r in rows) == {'match': 39, 'disposition': 24}
assert len({r['command'] for r in rows}) == 52
m = load('reports/round-21/validation.json')['claims']['C']['measurement']
assert (m['source_command_total']['value'], m['recounted_rows']['value'],
        m['matched_rows']['value'], m['dispositioned_rows']['value']) == (63, 63, 39, 24)
f = load('reports/round-11/validation.json')['claims']['F']
s = load('reports/round-11/recheck/summary.json')
assert f['passed'] is False
assert f['measurement']['stable'] == s['stable'] == 147
assert f['measurement']['rows_rechecked'] == 189 and s['rows_reckecked'] == 192
assert 147 / 189 < .95 and 147 / 192 < .95
non_closed = sum(r['status'] != 'closed' for r in q)
assert non_closed == load('reports/round-21/validation.json')['claims']['O']['measurement']['round22_routes']['value'] == 18
c17 = load('reports/round-17/validation.json')['claims']['C']['measurement']
assert (c17['fixed_count']['value'], c17['attempted_count']['value'], c17['fragments']['value']) == (7, 5, 16)
c18 = load('reports/round-18/validation.json')['claims']['C']['measurement']
assert len(c18['attempt_rows']) == 5
civ = load('reports/round-18/civ-map-r18.json')
assert (len(civ['entries']), len(civ['transitions']), civ['rows_carried_verbatim']) == (94, 12, 82)
assert Counter(r['status'] for r in civ['entries']) == {'current': 83, 'stale-fixed': 11}
assert civ['terminal_status_counts'] == {'current': 94, 'stale-documented': 0}
import re
declaration = load('reports/round-22/claims.json')['claims']
assert len(declaration) == 3
primary = re.findall(r'\((\d+)\)', next(r for r in declaration if r['id'] == 'O')['before'])
assert primary == ['1', '2', '3', '4', '5', '6']
print('measured_at_utc=' + datetime.now(timezone.utc).isoformat())
print('states', dict(states), 'claim_flags', dict(flags))
print('queue', len(q), dict(Counter(r['classification'] for r in q)), dict(Counter(r['status'] for r in q)), 'non_closed_routes', non_closed)
print('recount', len(rows), dict(Counter(r['verdict'] for r in rows)), 'literal_commands', 52)
print('r18_map', len(civ['entries']), len(civ['transitions']), civ['rows_carried_verbatim'], dict(Counter(r['status'] for r in civ['entries'])), 'attempts', c18['attempt_rows'])
print('r22_primary_O_items', len(primary))
print('r11 comparable/all ratios', 147 / 189, 147 / 192)
print('PASS: historical flags, baseline exception, count units and original receipt bytes preserved')
PY
```

### M2 — declaration/baseline and operator-amendment identity control

Measured **2026-10-18**; read-only Git identity/date/subject lookup:

```sh
export TMPDIR=$PWD/.scratch
python3 - <<'PY'
from datetime import datetime, timezone
import subprocess
revisions = ('f30b6f8', '9b49a4a', '3dd3754', 'c66ac3c', 'e571894', '169c616',
             'caf1bea', '122086b', '35b6797', '8115eaa',
             '51e590100f7bb3c2d30f5cc9e91a0ad981505179',
             '94377884a78a73ad5396acb0d5f48a539a7a0448',
             '3dba77a722c6a2e885447a47971205fd97c11605')
print('measured_at_utc=' + datetime.now(timezone.utc).isoformat())
for rev in revisions:
    print(subprocess.check_output(['git', 'show', '-s', '--format=%H %cI %s', rev], text=True).strip())
PY
```

Parent owns round-22 final acceptance, routed-resolution integration, source
fix/re-pin controls, SCORECARD/LOG append and authorized filing. This document
supplies the calibration assessment; it does not claim O/D completion or lore
acknowledgment, canon, authenticity, rights or permission clearance.
