# `corpus/lessons/` index — revision 3 (round 26, 2026-10-18)

This is the **new revision** of the lessons index the round-25 README asked for:
the 49-row open-question queue of `corpus/lessons/README.md` §4, every row
dispositioned. It is a **new file**, not an in-place rewrite — revision 1
(round-25 C31) and revision 2 (round-25 C35) are filed bytes whose per-round
rows, pins and provenance claims stand unedited.

- **Owner of this revision:** the C seat of round 26 (claims `R26-C41..C46` in
  `reports/round-26/claims.json`). Round counting command:
  `python3 reports/round-26/run-validation.py`.
- **Canon:** NON-CANON engineering evidence. This index admits nothing, certifies
  no round, blesses no lesson and grants no promotion.
- **What revision 3 adds:** the **disposition** of every queue row (§4). It does
  **not** re-pin the per-round cells; those are revision 1/2 measurements of
  filed bytes, and the round-25 auditor remains their tool of record.

Rows: 27. Files: 27. (The partition is the runner's glob
`corpus/lessons/*.md`, which includes this index's own directory file
`README.md`, the round-25 lesson that landed mid-audit, and the round-26
gate-keeper lesson that landed during this revision's own wave. Re-run
`ls corpus/lessons/*.md | wc -l` rather than inheriting the number: the
partition is a live-wave surface, and a lesson landing after this stamp adds a
row rather than changing one.)

## 0. Counting command, and the partition control

Counting command: `ls corpus/lessons/*.md | wc -l` → 27 (2026-10-18);
`find corpus/lessons -maxdepth 1 -name '*.md' | wc -l` → 27 (same set).

This revision is **not** written into `corpus/lessons/`, because a second `*.md`
there would break the round-25 auditor, whose partition *is* that glob. Control
(2026-10-18, isolated clone):

```sh
git clone -q . .scratch/r26c/partctl/repo
printf '# probe\n' > .scratch/r26c/partctl/repo/corpus/lessons/README-rev3-probe.md
cd .scratch/r26c/partctl/repo && python3 -B reports/round-25/audit/c31-lessons-index-audit.py
# index rows: 26   formats: {'gate-keeper': 14, 'fragment-index': 5, 'plain': 8}
# (quoted auditor stamp output, not this revision's declaration)
#   FAIL C31_index_rows_eq_files      FAIL C34b_prose_arithmetic
# findings: 2   C31-1 unindexed-file: ['README-rev3-probe.md']
# exit=1
```

The same auditor on the unmodified tree: `index rows: 26  lesson files: 26
queue rows: 49`, six checks PASS, `findings: 0`, exit 0. So the revision lands
under `reports/round-26/`, and the round-25 auditor stays green. (That green was
measured before `corpus/lessons/round-26.md` landed at 15:11; the round-25
auditor's own revision-2 rule is that a lesson landing after a stamp adds a row
rather than changing one, so the 26→27 movement is the partition's, not a defect
in this revision.)

### 0.1 Why this file is named `zzz-…` (a runner-selection collision, measured)

The round-26 runner does not look for a revision by a declared name: it takes
**the lexicographically last** `.md` under `reports/round-26/` whose content
carries an index row and the phrase "open question"
(`run-validation.py:1195-1204`, `find_readme_revisions`). At this wave a sibling
scribe ledger — `reports/round-26/scribe/fragment-ledger.md`, which quotes
`report-draft.md` / `scope.md` in an index-shaped table and mentions open
questions — out-sorted a first copy of this revision at
`reports/round-26/open-questions/README-rev3.md`, so the runner graded **the
wrong document**. Measured control (2026-10-18, isolated clone, the runner's own
`find_readme_revisions` called directly):

```sh
python3 - <<'PY'
import importlib.util
spec=importlib.util.spec_from_file_location("rv","reports/round-26/run-validation.py")
m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
print([c['path'] for c in m.find_readme_revisions()][-1])
PY
# before the rename:  reports/round-26/scribe/fragment-ledger.md
# after  the rename:  reports/round-26/zzz-lessons-index-revision-3.md
```

With the wrong document selected the runner failed claim C with four findings
(27 omitted lesson files, 2 phantom files, 1 of 3 census formats, no queue ids);
with this file selected the same runner reports claim C **passed, 0 failures,
coverage 49/49 = 100%**. The rename is therefore load-bearing, not cosmetic, and
it is recorded here rather than silently applied. A future round that adds an
`.md` under `reports/round-26/` sorting after `zzz-` would re-break the selection.

## 1. Per-round index (rows re-read from revision 1; not re-pinned here)

Columns: **file** · **format** (§3) · **contract** lines present of 4 ·
**open-questions carried** · **disposition pointer**.

| file | format | contract | open-questions carried | disposition pointer |
|---|---|---|---|---|
| `corpus/lessons/README.md` | index (revision 1/2) | — | — | itself; superseded for the queue by this revision |
| `corpus/lessons/round-1-gates-and-triage.md` | plain | 0/4 | — | `LOG.md` |
| `corpus/lessons/round-2-adjacency.md` | plain | 0/4 | Q-02-1, Q-02-2, Q-02-3, Q-02-4 | §4 of this revision |
| `corpus/lessons/round-3-d2-build.md` | plain | 0/4 | Q-03-1 | §4 of this revision |
| `corpus/lessons/round-4-sol-fixes-and-audits.md` | plain | 0/4 | Q-04-1, Q-04-2, Q-04-3, Q-04-4 | `corpus/lessons/round-4-audit/`, `corpus/lessons/round-4-triage/` |
| `corpus/lessons/round-5-availability.md` | gate-keeper | 3/4 | Q-05-1 | `reports/round-5` |
| `corpus/lessons/round-5.md` | gate-keeper | 3/4 | Q-05-2, Q-05-3 | `reports/round-5/validation.json` |
| `corpus/lessons/round-6.md` | gate-keeper | 3/4 | Q-06-1, Q-06-2 | `reports/round-6/checkpoint.json` |
| `corpus/lessons/round-7.md` | plain | 3/4 | Q-07-1 | `reports/round-7` |
| `corpus/lessons/round-8.md` | fragment-index | 3/4 | Q-08-1 | `reports/round-8` |
| `corpus/lessons/round-9.md` | fragment-index | 3/4 | Q-09-1 | `reports/round-9/validation.json` |
| `corpus/lessons/round-10.md` | fragment-index | 3/4 | Q-10-1 | `reports/round-10/validation.json` |
| `corpus/lessons/round-11.md` | fragment-index | 3/4 | Q-11-1, Q-11-2, Q-11-3 | `reports/round-11/validation.json` |
| `corpus/lessons/round-12.md` | fragment-index | 3/4 | Q-12-1, Q-12-2, Q-12-3 | `reports/round-12` |
| `round-13` | — | — | — | operator-skipped; no lesson file exists |
| `corpus/lessons/round-14.md` | gate-keeper | 3/4 | Q-14-1, Q-14-2 | `reports/round-14/validation.json` |
| `corpus/lessons/round-15.md` | gate-keeper | 3/4 | Q-15-1, Q-15-2 | `reports/round-15/validation.json` |
| `corpus/lessons/round-16.md` | plain | 3/4 | Q-16-1 | `reports/round-16/civ-map.json` |
| `corpus/lessons/round-17.md` | gate-keeper | 4/4 | Q-17-1, Q-17-2 | `reports/round-17` |
| `corpus/lessons/round-18.md` | gate-keeper | 4/4 | Q-18-1, Q-18-2, Q-18-3 | `reports/round-18/d4/holds.md` |
| `corpus/lessons/round-19.md` | gate-keeper | 4/4 | Q-19-1, Q-19-2 | `reports/round-19/validation.json` |
| `corpus/lessons/round-20.md` | gate-keeper | 4/4 | Q-20-1, Q-20-2, Q-20-3, Q-20-4 | `reports/round-20/validation.json` |
| `corpus/lessons/round-21.md` | gate-keeper | 4/4 | Q-21-1, Q-21-2 | `reports/round-21/defects/ledger.json` |
| `corpus/lessons/round-22.md` | gate-keeper | 4/4 | Q-22-1, Q-22-2, Q-22-3 | `reports/round-22/routed-resolution.json` |
| `corpus/lessons/round-23.md` | gate-keeper | 4/4 | Q-23-1, Q-23-2, Q-23-3 | `reports/round-23/integration/fragment-ledger.md` |
| `corpus/lessons/round-25.md` | gate-keeper | 4/4 | — (round-25 claims pending, not carried) | `reports/round-25/claims.json` |
| `corpus/lessons/round-26.md` | gate-keeper | 4/4 | — (this round's own lesson, filed mid-wave; its claims are pending, not carried) | `reports/round-26/claims.json` |
| `corpus/lessons/supplement-opencode-1.md` | gate-keeper | 3/4 | Q-S1-1 | `reports/supplement-opencode-1` |

Rows 27 for 27 files, as declared above. Round 5 contributes two rows on purpose
(the preflight refusal record and the round); round 13 contributes a
skip row because no lesson file exists.

## 2. The three census formats

1. **gate-keeper survey** — a `## Gate` section with the marker vocabulary
   (`Opening <axis> reading:`, `Admitted`/`Rejected`, a `spot-check` sentence)
   plus the four contract lines. Sub-shape: rounds 19–20 carry the older
   three-candidate vocabulary; rounds 21–25 carry the newer `### Rule` +
   per-axis shape. Both count as gate-keeper.
2. **fragment-index** — the gate-keeper survey **plus** a `## Fragment index`
   section enumerating the round's report fragments (rounds 8–12).
3. **plain** — no `## Gate`: the pre-contract seed lessons (rounds 1–4), round 7
   (its `## Gate candidates` heading is prose), round 16 (a map-scribe record)
   and revision 1 itself.

## 3. Disposition of the 49-row open-question queue

Every queue row is dispositioned below: **fixed** (a live command answers the
row's own wording) or **carried** (named owner + reason + next touch round).
Per-row evidence, including the controls, is in the six fragments under
`reports/round-26/open-questions/`: `C41.md` (rounds 2–4, 9 rows), `C42.md`
(rounds 5–7, 6), `C43.md` (rounds 8–12, 9), `C44.md` (rounds 14–17, 7),
`C45.md` (rounds 18–22, 14), `C46.md` (round 23 + supplement, 4).

| Q-id | class | owner | reason | next touch | evidence |
|---|---|---|---|---|---|
| Q-02-1 | fixed | `corpus/knowledge/synthesis/worldbible-integration-contract.md` | reason: the checker reads the sample's field forms (16/16) | round 27 for the serialization agreement | `python3 -B tools/gates/handoff-packet-check.py examples/handoff-packet.sample.yml` → exit 0; truncated copy → 8 findings, exit 1 |
| Q-02-2 | fixed | `examples/handoff-packet.sample.yml` | reason: the §4 field row and the sample's live `validation:` section both exist | round 27 | `grep -n "^validation:" examples/handoff-packet.sample.yml` → line 629; contract line 66 |
| Q-02-3 | carried | `operator` | reason: a bilateral ack cannot be settled from this lane alone | round 27 | no `read_at` record on disk outside prose |
| Q-02-4 | fixed | `parent` | reason: the frozen submission's digest reproduces byte-equal | round 27 for the fleet-root L0 record | `python3 -B tools/exercise-handoff-e2e.py --profile v3` → `OK frozen-packet: packet sha256 a97a0f0a…`, exit 0 |
| Q-03-1 | fixed | `tools/gates/naming-collision-gate.py` | reason: the diagnostic is answered — the gate tokenizes the English gloss, not the native form | round 27 for the producer change | `python3 -B tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml` → 6 PHON-INVENTORY findings on `/f/ /q/ /c/ /-/ /(/` inside the gloss |
| Q-04-1 | fixed | `tools/gates/naming-collision-gate.py` | reason: the derivation adapter landed and replays the rules | round 27 | `python3 -B tools/gates/naming-collision-gate.py examples/culture-d4/packet.d4.yml` → 0 DERIV-REPLAY; `D4L-ARGOT-DERIV` live at `tools/gates/typed-pipeline-gate.py:536` |
| Q-04-2 | carried | `corpus/QUALITY.md` | reason: the real-language sweep is a declared pre-publication gap, not a defect | round 27 | `FINDING CROSS-HOLD: HOLD — packet declares no bounded cross-cultural review` |
| Q-04-3 | fixed | `reports/round-5` | reason: the routing landed and was reconciled at round 5 | round 27 | `reports/round-5/parent-reconciliation.json` → counts 22/13/8/1 |
| Q-04-4 | carried | `corpus/lessons/round-4-audit` | reason: a standing craft rule; it re-binds when a target is next declared | round 27 | `corpus/lessons/round-4-audit/` holds 16 files |
| Q-05-1 | carried | `operator` | reason: a standing routing rule about future rounds | round 27 | `reports/round-5/availability-attempt-1.json` → requested 16, launched 0, completed 0 |
| Q-05-2 | fixed | `reports/round-5/parent-reconciliation.json` | reason: the reconciliation landed and preserves raw counts beside logical verdicts | round 27 | `python3 -c "import json;print(json.load(open('reports/round-5/parent-reconciliation.json'))['expected_worker_raw_counts'])"` → rows 22, supported 13, unresolved 8 |
| Q-05-3 | carried | `corpus/QUALITY.md` | reason: the header-conformance and numeric-rubric debt stays explicit; no rubric is invented | round 27 | `grep -n "header\|rubric" corpus/QUALITY.md` → no matches; `reports/round-5/kotodama.md:54` names no calibrated rubric |
| Q-06-1 | carried | `reports/round-6/checkpoint.json` | reason: the round-6 checkpoint was never admitted, so no round close absorbed its residual set | round 27 | `python3 -c "import json;print(json.load(open('reports/round-6/checkpoint.json'))['admission_status'])"` → pending |
| Q-06-2 | carried | `parent` | reason: the fleet root is outside this repo's write scope | round 27 | `reports/round-25/report-draft.md:49` records the fleet root as not clean |
| Q-07-1 | carried | `reports/round-7` | reason: a multi-class carry whose every sub-class has its own live home | round 27 | `reports/round-7/parent-reconciliation.json`; `corpus/QUALITY.md` |
| Q-08-1 | fixed | `reports/round-8` | reason: the carry landed as four named per-item targets at round 9 | round 27 | `reports/round-9/targets.json` → R9-R8-F01..F04; `reports/round-9/freshness/verify-F03.md` |
| Q-09-1 | carried | `parent` | reason: the parent-side re-run and source re-fetch receipts are not filed in this repo | round 27 | `reports/round-9/validation.json` acceptance true; no parent spot-check file under `reports/round-9/` |
| Q-10-1 | fixed | `reports/round-10/validation.json` | reason: the four C-leg failures were repaired and the receipt re-admitted | round 27 | `git show 94ca098:reports/round-10/validation.json \| sha256sum` equals live `e8571db918b2c323…`; acceptance true, failures [] |
| Q-11-1 | fixed | `parent` | reason: the denominator question was dispositioned as a named defect with both denominators recorded | round 27 | `reports/round-12/defects/ledger.json` entry RATIO-11, status fixed-with-control |
| Q-11-2 | fixed | `parent` | reason: all six rewritten receipts are byte-identical to HEAD and the class has a preventive control | round 27 | `git rev-parse HEAD:reports/round-9/validation.json` equals `git hash-object reports/round-9/validation.json`; `tools/harness/receipt_guard.py --selftest` exit 0 |
| Q-11-3 | fixed | `reports/round-11` | reason: the appendix is tracked, filed and clean | round 27 | `git log --oneline -2 -- reports/round-10/coverage/index-update-22.md` → a3f6fce, 94ca098; `git status --porcelain` empty |
| Q-12-1 | carried | `reports/round-12/recount/audit.md` | reason: the mismatch is dispositioned as environmental and deliberately not patched; the sanitizer gap sits in a filed round-9 runner | round 27 | `reports/round-12/recount/audit.md:18` names the `.scratch` path leakage |
| Q-12-2 | fixed | `parent` | reason: the tuple is consistent once read as 0.778 = 147/189 with 147/192 = 0.7656 beside it | round 27 | `SCORECARD.md:110` records both denominators |
| Q-12-3 | fixed | `reports/round-12` | reason: both the structured ledger rows and the A01–A04 seat exist on the live bytes | round 27 | `python3 -c "import json;print(len(json.load(open('reports/round-12/adjacency/ledger.json'))['entries']))"`; `reports/round-12/targets.json:55` |
| Q-14-1 | carried | `reports/round-14/retro-consistency.md` | reason: the append-only integrity control is deliberately scoped and not retroactive | round 27 | `reports/round-14/retro-consistency.md:33,102` |
| Q-14-2 | fixed | `SCORECARD.md` | reason: the round-14 admission append landed with its four-axis table | round 27 | `python3 -c "print(open('SCORECARD.md').read().count('Axes — round 14'))"` → 1 (exit 0) |
| Q-15-1 | fixed | `reports/round-15/handoff/v2-design.md` | reason: OQ-V2-02 is answered by the frozen digest; OQ-V2-01/03 are bilateral | round 27 | `python3 -B tools/exercise-handoff-e2e.py --profile v2` → exit 0, claims 15, links 50/50 |
| Q-15-2 | fixed | `tools/harness/packet_uncertainty.py` | reason: the selftest is green and malformed input is a named refusal | round 27 | `python3 -B tools/harness/packet_uncertainty.py --selftest` → 19 checks passed, exit 0; malformed packet → exit 2 |
| Q-16-1 | fixed | `reports/round-16/civ-map.json` | reason: the independent auditor's stratified spot-check landed at twice the floor | round 27 | `reports/round-16/civ/map-audit.md` — 20 entries re-run, derivation built before reading shards |
| Q-17-1 | fixed | `reports/round-17` | reason: the named D blocker artifact exists and the D4 pipeline is green end-to-end | round 27 | `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → 20/20 legs, exit 0; `tools/assemble-d4-typed.py` exists |
| Q-17-2 | fixed | `reports/round-17` | reason: the revised runner supersedes the scoring defect, and the lesson records it | round 27 | `grep -n "F-X01-1 superseded" corpus/lessons/round-17.md` → line 173 |
| Q-18-1 | carried | `examples/culture-d4/components/01-brief.yml` | reason: the disposition is the parent's; no later round absorbed it | round 27 | declared 6 vs emitted 37 tokens in `examples/culture-d4/packet.d4.typed.yml`; `corpus/lessons/round-18.md:173` |
| Q-18-2 | carried | `parent` | reason: the authority question is a decision, not a measurement | round 27 | `corpus/lessons/round-18.md:222` — three seats flagged it un-decided |
| Q-18-3 | carried | `tools/d2-typed-labels.py` | reason: the register engine path is round 26's own claim D, in flight at this stamp | round 26 | `grep -rl "D4L-REGISTER-UNRESOLVED" examples/ tools/` → 0 files; `register_scoped=6 derived_pairs=0` |
| Q-19-1 | carried | `parent` | reason: the lesson-path collision's two dispositions both touch a filed byte | round 27 | `corpus/lessons/README.md:20,186` names it the standing example |
| Q-19-2 | fixed | `examples/culture-d4/expected-holds.json` | reason: the artifact now carries a reconciliation pointer and a superseded-pin block | round 27 | `python3 -c "import json;print(list(json.load(open('examples/culture-d4/expected-holds.json'))))"` → revision_note, supersedes_pins present |
| Q-20-1 | fixed | `corpus/README.md` | reason: rev 1.5 measures and names the linguistics discrepancy | round 27 | `find corpus/knowledge/linguistics -type f \| wc -l` → 19; `corpus/README.md:24` states 19 not 20 |
| Q-20-2 | fixed | `examples/culture-d2/expected-holds.json` | reason: the live pin equals the live projector and the superseded value is retained | round 27 | `python3 -c "import json,hashlib;print(json.load(open('examples/culture-d2/expected-holds.json'))['projector_sha256']==hashlib.sha256(open('tools/d2-typed-labels.py','rb').read()).hexdigest())"` → True |
| Q-20-3 | fixed | `tools/exercise-handoff-e2e.py` | reason: both profile routes are green | round 27 | `python3 -B tools/exercise-handoff-e2e.py --profile v3` → exit 0, links 105/105; `--profile v2` → exit 0 |
| Q-20-4 | fixed | `parent` | reason: the filed receipts are byte-identical to HEAD and a preventive control landed | round 27 | `git rev-parse HEAD:reports/round-5/validation.json` equals `git hash-object reports/round-5/validation.json`; `tools/harness/receipt_guard.py --selftest` exit 0 |
| Q-21-1 | carried | `reports/round-21/defects/ledger.json` | reason: two ledger rows stay open and the round-22 resolution surface does not name them | round 27 | `R17-CURRENT-RECOUNT-DISCREPANCY` and `R20-HANDOFF-LINK-COUNT` both status open; absent from `reports/round-22/routed-resolution.json` |
| Q-21-2 | fixed | `reports/round-21/defects/regression.md` | reason: the routing half is dispositioned; the re-pin half stays carried | round 27 | `python3 -B tools/replay-frozen.py tools/gates/frozen/round-18/MANIFEST.tsv` (external TMPDIR) → 1 mismatch, exit 1; `reports/round-22/routed-resolution.json` R21-R18-SUPERSESSION |
| Q-22-1 | fixed | `tools/d2-typed-labels.py` | reason: the producer reproduces the filed output byte-for-byte and the bleed rows are gone | round 27 | `python3 -B tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --emit …` diff-identical; `grep -c D2L-RANK` → 0; selftest 163/163 |
| Q-22-2 | carried | `operator` | reason: a standing operator decision; the pause stays in force until it is changed | round 27 | `SCORECARD.md:443` — freshness unchanged, axis-move claims still paused |
| Q-22-3 | fixed | `reports/round-22/routed-resolution.json` | reason: the discipline landed as a new revision row with the superseded pin retained | round 27 | `reports/round-23/pins/r2-live.md` before/after table; `tools/gates/frozen/round-23/repin-d2/MANIFEST.tsv` |
| Q-23-1 | fixed | `reports/round-25/claims.json` | reason: the superseding revision landed and is frozen with its own pin | round 27 | `reports/round-25/v3-supersession/declared-in-r4/freeze.txt` → packet_sha256 5f58db4a…, five ledger corrections |
| Q-23-2 | fixed | `reports/round-25/claims.json` | reason: the wording disposition landed and no validator rule was weakened | round 27 | `grep -c "foreign-path-stability control" reports/round-25/v3-supersession/declared-in-r4/packet.md` → 2; freeze.txt records zero grammar problems under the frozen PLACEHOLDER_RE |
| Q-23-3 | fixed | `reports/round-25/claims.json` | reason: the combined-source successor row landed as a new revision with a frozen generation | round 27 | `tools/gates/frozen/round-23/repin-d2/MANIFEST.tsv`; D2 pin equals the live projector |
| Q-S1-1 | fixed | `reports/supplement-opencode-1` | reason: the unresolved outcomes are preserved and the four boxes now carry non-author verdicts | round 27 | 21 `"unresolved"` occurrences across 15 source files; `reports/round-24/promotion-review.md` → four boxes verified-with-conditions |

Queue arithmetic: **49 rows**; **32 fixed**, **17 carried**, **0
undispositioned**. Six rows are compound (Q-02-1, Q-02-4, Q-03-1, Q-15-1,
Q-21-2, Q-22-3): each carries a second disposition whose class differs from the
leading one, so the fragments also report half-counts (32 fixed halves, 24
carried halves). Every carried row names an owner, a reason and a next touch
round — 27, except Q-18-3, which re-binds at round 26 because that round's own
claim D owns it.

## 4. Boundary record

- **Writes:** this file, the six fragments under
  `reports/round-26/open-questions/`, and gitignored scratch under
  `.scratch/r26c/`. No `corpus/lessons/round-*.md` byte was touched, **no byte of
  `corpus/lessons/README.md` was touched**, no filed round 8–25 artifact was
  edited, no tool and no gate was changed. No commit, no push.
- **Controls:** the partition control in §0; the truncated-sample refusal for
  Q-02-1/Q-02-2 (`HO-EMPTY`, `HO-MISSING`, exit 1); the malformed-packet refusal
  for Q-15-2 (exit 2); the byte-identity checks for Q-10-1, Q-11-2, Q-20-2,
  Q-22-1; the external-TMPDIR separation for Q-21-2 (`mirror_unsafe` vs
  `replay_mismatch`).
- **Independence:** every reading was re-measured from live bytes at
  2026-10-18T18:0x–18:3xZ, not transcribed from revision 1's status column.
  Where this revision and revision 1 differ, the difference is a **new row
  state** measured on later bytes; revision 1's column stands as filed.
- **Known limit:** the disposition table above is machine-readable and the
  fragments carry the controls; a consumer who needs the full command output for
  any row must read the row's fragment, which is where the controls are quoted.
