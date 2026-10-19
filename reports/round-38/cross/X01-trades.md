- Seat: X01 | critic | claim cross | date 2026-10-19 | baseline 9bccc9b

# X01 — trade hunter + conformance

Mission (`reports/round-38/targets.json`, seat `X01`): *"Trade hunter + conformance."*
Round 38, loop 1 position 6. This is a completion seat: the single 32-seat batch on
`xai-oauth/grok-4.7-fast` failed 32/32 at launch (`403 out of credits`,
`telemetry/availability-attempt-1.json:7-13`), the re-dispatch onto
`devin/deepseek-v4-1-flash-high` is a **named deviation** with no declared fallback
(`REGIMEN.md:16` carries none for this row), and 22 of 32 declared outputs landed before
this seat ran.

Write scope: **this file only**. No tool, gate, packet, component, pin, battery baseline,
telemetry record, or filed round-1..37 byte written. Every mutation below ran in a
`git archive 9bccc9b` copy under the gitignored `.scratch/x01/`; the live tree was never
written (`git status --porcelain --untracked-files=all` → 27 rows, **all** `?? reports/round-38/…`;
`git diff --name-status 9bccc9b` → empty). No `reports/round-*/run-validation.py` was
executed anywhere, in-tree or in a copy (F-C13-1); `reports/round-38/run-validation.py`
does not exist (`ls` → No such file). No `--freeze`, no commit, no push, no install, no
network. `HEAD` = `9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26`. Stamp
**2026-10-19T11:14:45Z**–**11:26Z**; `TMPDIR=$PWD/.scratch`,
`PYTHONDONTWRITEBYTECODE=1` before every python call.

Canon: NON-CANON engineering evidence. A digest is integrity, never truth, never
clearance. This fragment claims no promotion, canon, clearance or closure, and takes no
admission verdict — that is the integrator's, against the tests below.

---

## 0. Verdict

**No axis is harmed by either claim's recommended route.** But the round carries **one
unpriced trade that decides whether claim D's own acceptance test can be met**, and
**three conformance defects** that the landed fragments do not report:

| # | item | class | severity |
|---|---|---|---|
| **T1** | The era leg's **finding id** decides whether the typed pipeline can see the era defect. Same host, same defect, three ids → **three different pipeline verdicts** (measured §3). The D block's four drafts carry three ids across two hosts and no fragment prices the id against pipeline visibility. | trade | **high** |
| **T2** | "The two named tool/example artifacts" (`claims.json:16,27`) is not two under the verified route: P01's route touches **one** gate, D02/D08's touches **two plus a new battery baseline**. The count is route-dependent and unbound. | trade | medium |
| **C1** | `op/O07-scribe.md` is **0 bytes** and is counted as landed. It is the only empty fragment in rounds 33–38, and `scribe/S01-integration-draft.md §2.5` lists the absent outputs **without** it. | conformance | medium |
| **C2** | The seat census carries claim ids `claims.json` never declares — but `cross` is undeclared in **every** round 33–38, so only **`A`** is the r38 delta. The landed fragments say "first round with this shape" without that distinction. | conformance | low |
| **C3** | The round's record set is incomplete: `validation.json`, `run-validation.py`, `.ufo/reports/round-38/kotodama.md`, and the LOG/SCORECARD/MANIFEST rows are all absent. Expected pre-integration — recorded so "closed" is never read off fragment count. | conformance | low |

Converged-with-peers (not re-claimed as new, attributed): the F-6 route cost split
(D04/D08/D09), the O guard's naming-vs-detection character (R02 F6), the O guard's
"refuses contradicts its own threshold" constraint (R02 F3), the r7 roster defect's
non-r7-only generality (X02 §4a, A02 F-A02-3).

---

## 1. Method

Pristine control first, so every later red is attributable. Isolated copy
`.scratch/x01/iso` = `git archive 9bccc9b | tar -x`:

```
$ python3 -B tools/check-gate-battery.py
  "summary": { "battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0 }        exit 0
$ python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
coverage: … records=187 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0   exit 0
$ python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
coverage: … law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0   exit 0
$ python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
summary: 20/20 legs passed                                                              exit 0
```

All green, matching D03 §1, R03 §1, D08 §1. Membership census (independent, resolved
from the constants and the filed baseline, not read from a summary):

```
r7 expected.json inputs           : 58
  of which culture-d4/components/ : 12     13-register-law present: False
tools/d2-typed-labels.py          : IN the r7 read set
tools/assemble-d4-typed.py        : IN the r7 read set
tools/assemble-culture-d4.py      : IN the r7 read set
tools/gates/argot-derivation-gate.py    : NOT in the r7 read set
tools/gates/register-law-gate.py        : NOT in the r7 read set
tools/gates/typed-pipeline-gate.py      : NOT in the r7 read set
tools/exercise-handoff-e2e.py           : NOT in the r7 read set
```

and the five filed v3 baselines are uniform in the defect class:

| filed baseline | `inputs` | D4 components | `13-register-law` |
|---|---:|---:|---|
| `round-22/handoff/declared-in` | 58 | 12 | no |
| `round-22/handoff/declared-in-r2` | 58 | 12 | no |
| `round-26/handoff/declared-in-r5` | 58 | 12 | no |
| `round-30/handoff/declared-in-r6` | 58 | 12 | no |
| `round-34/handoff/declared-in-r7` | 58 | 12 | no |

---

## 2. T1 — the era leg's finding id is a pipeline-visibility decision (the round's unpriced trade)

### 2.1 Three drafts, two hosts, three ids — measured in the drafts' own text

| draft | host | finding id | pins moved (draft's own claim) |
|---|---|---|---|
| `plan/P01-d-plan.md §3.4`, applied verbatim by `depth/D03-isolated.md §3` | `tools/gates/argot-derivation-gate.py` | **`D4L-ARGOT-ERA`** | **zero** (verified end-to-end, D03 §3.1) |
| `depth/D02-rl8-design.md` | `tools/gates/register-law-gate.py` | **`D4L-LAW-ERA`** | one new battery baseline |
| `depth/D08-gap-fill.md §4.2` | `tools/gates/register-law-gate.py` | **`D4L-ERA`** | one new battery baseline |

Id census over the drafts' own bytes (`grep -o` per file):

```
plan/P01-d-plan.md      : 7 × D4L-ARGOT-ERA, 16 × D4L-ERA (the r26 id, in prose and in the rejected option)
depth/D02-rl8-design.md : 28 × D4L-LAW-ERA, 2 × D4L-ERA (both in the quoted r26 rule)
depth/D08-gap-fill.md   : 8 × D4L-ERA
depth/D03-isolated.md   : 3 × D4L-ARGOT-ERA, 1 × D4L-LAW-ERA, 1 × D4L-ERA (the comparison table)
```

`plan/P01-d-plan.md §6.2` names the id choice explicitly and prices **two** options —
`D4L-ARGOT-ERA` (pipeline sees it, no pipeline edit) versus keeping `D4L-ERA` **and
widening the pipeline filter** at `typed-pipeline-gate.py:531` (id fidelity to r26,
costs a pipeline edit and a re-pin of its selftest expectation). What P01 §6.2 does
**not** state, and what D02 and D08 do not evaluate at all, is the third option their
own drafts actually take: emit a non-`D4L-ARGOT-` id **without** widening the filter.
That option is not a trade — it is a silent loss, and §2.3 measures it.

### 2.2 The pipeline's filter, read from the delivered bytes

```
tools/gates/typed-pipeline-gate.py:84      ARGOT_GATE = GATES_DIR / "argot-derivation-gate.py"
tools/gates/typed-pipeline-gate.py:530-531
        argot_lines = [line for line in proc.stdout.splitlines()
                       if line.startswith("FINDING D4L-ARGOT-")]
```

The pipeline invokes the **argot gate only**:

```
$ grep -n "register-law\|register_law\|REGISTER" tools/gates/typed-pipeline-gate.py
1346,1352,1353,1426:  'D9L-REGISTER-UNRESOLVED'   # a fixture string, not a gate invocation
$ grep -n "GATES_DIR /" tools/gates/typed-pipeline-gate.py
84:   ARGOT_GATE = GATES_DIR / "argot-derivation-gate.py"
131:  PROFILE_DEFAULT = GATES_DIR / "typed-pipelines.json"
```

So the law gate is **never run by the typed pipeline**. An era FAIL emitted from the law
gate cannot reach the pipeline by any id; an era FAIL emitted from the argot gate reaches
it only if the id carries the `D4L-ARGOT-` prefix. Pure filter arithmetic:

```
D4L-ARGOT-ERA   "FINDING D4L-ARGOT-ERA: FAIL - probe"   kept_by_L3b_filter = True
D4L-LAW-ERA     "FINDING D4L-LAW-ERA: FAIL - probe"     kept_by_L3b_filter = False
D4L-ERA         "FINDING D4L-ERA: FAIL - probe"         kept_by_L3b_filter = False
D4L-ARGOT-DERIV "FINDING D4L-ARGOT-DERIV: FAIL - probe" kept_by_L3b_filter = True
```

### 2.3 The decisive control — same host, same defect, three ids, three verdicts

I injected one emitter into a fresh `git archive` copy of the **argot** gate
(`.scratch/x01/idiso`), emitting a single `FAIL` line under a chosen id and returning
exit 1 — i.e. exactly the shape a landed era leg has on a tampered packet. This isolates
the **id** from the **host**, which no landed fragment does:

```
# argot gate itself, exit 1 in every case (the leg fires)
id=D4L-ARGOT-ERA : argot exit=1 | FAIL L3b-argot — argot leg exit 1: FINDING D4L-ARGOT-ERA: FAIL - x01 era probe
                                 | summary: 19/20 legs passed | pipeline exit=1
id=D4L-LAW-ERA   : argot exit=1 | ok   L3b-argot
                                 | summary: 20/20 legs passed | pipeline exit=0
id=D4L-ERA       : argot exit=1 | ok   L3b-argot
                                 | summary: 20/20 legs passed | pipeline exit=0
```

**The same era defect, in the same host, on the same packet, reads `20/20 legs passed`
and exits 0 for two of the three ids.** That is the vacuous pass X02 §5 row 2, D10b §2,
and R03 §7.1 warn about, now demonstrated with a concrete id rather than inferred from
the filter's text.

### 2.4 The trade, named and not averaged

| id | r26 fidelity | pipeline sees the era defect | extra edit owed |
|---|---|---|---|
| `D4L-ARGOT-ERA` | **no** — r26 filed `D4L-ERA` (`reports/round-26/register/rules.md:110-128`) | **yes** | none |
| `D4L-ERA` | **yes** | **no**, unless the filter at `:531` is widened | a `typed-pipeline-gate.py` edit + its selftest expectation re-pin |
| `D4L-LAW-ERA` | no (a new id) | **no**, and cannot — the pipeline never runs the law gate | a filter widening **and** a host change |

Neither fidelity nor visibility is reachable alone without a second edit. **This is a
real trade, not a defect in any one draft**, and it must be decided rather than left to
whichever draft the integrator happens to apply. The consequence for claim D's acceptance
is concrete: `after_required` says *"the era leg runs … argot/law/typed legs green"*. A
green typed pipeline is **not** evidence the era leg ran under the `D4L-ERA` or
`D4L-LAW-ERA` shapes (§2.3). An integrator who accepts "typed legs green" as the era-leg
witness admits a vacuous pass.

**Recommended reading (mine, as trade-hunter, not a decision):** `D4L-ARGOT-ERA` with the
r26 id named in the message text (P01 §6.2's option 1). It is the only shape that is both
pipeline-visible and free, and it keeps `D4L-ERA` resolvable as a token in the message.
The cost is that the gate's own finding-id vocabulary gains a fourth `D4L-ARGOT-` member
while r26's filed id is not the emitted one — a documentation cost, not a pin cost.

---

## 3. T2 — "the two named artifacts" is route-dependent, and the count is wrong for both routes

`claims.json:16` and `:27` both say *"the two named tool/example artifacts"*; no round-38
byte names which two (`grep -rn "two named" reports/round-38/` → the two claim occurrences
plus the fragments that quote them). `depth/D04-pins.md:112` reads the pair as *"the argot
gate and the law gate"*; `depth/D05-verify.md:159` hedges it as *"…or the D01/D02-named
equivalents"*. Measured against the routes:

| route | files actually changed | battery baseline | claim's "two artifacts" |
|---|---|---|---|
| **P01 §3.4** (both legs in the argot gate), verified D03 §3 | **1** — `tools/gates/argot-derivation-gate.py` | none | **over-counts** (one, not two) |
| **D02 / D08** (era leg in the law gate) | **2** — argot gate (F-6) + law gate (era) | **one new** `expected/register-law-gate/<new-id>/` | under-counts (three surfaces) |
| F-6 route B (projection) | 5 surfaces + a D2 freeze-control break | none | under-counts badly |

So the phrase is unsatisfiable as written on every route: P01's verified landing moves
**one** artifact, and D02/D08's moves **two files plus a new baseline directory**. The
count is not a detail — it is the sentence the round's scope non-goal
(`no filed byte rewrites beyond the two named artifacts`) is enforced against.

I independently reproduced the D02/D08 battery cost (the one measurement in §3 I did not
take from a peer): appending a single comment to the law gate in a fresh archive copy
flips the battery to exit 2 with **no gate failing** —

```
$ printf '\n# x01 conformance control\n' >> tools/gates/register-law-gate.py   # isolated copy
$ python3 -B tools/check-gate-battery.py
  battery_exit: {'battery_exit': 2, 'fail': 0, 'pass': 7, 'unevaluable': 0}
```

`fail: 0` is the load-bearing part: the reading is `BASELINE-GATE-REVISED` on
`expected/register-law-gate/r30-post` (`gate_sha256 15f8b232…`), i.e. a **pinned-gate
digest moved**, not a gate broken. It is recoverable with a new baseline id in the same
edit set (D04 §4, D08 §4.5, D02 §6) and is **not a harm** — but it is a cost the claim's
`after_required` does not size, and the "two artifacts" sentence actively obscures it.

---

## 4. C1 — `op/O07-scribe.md` is 0 bytes and is counted as landed

```
$ ls -la reports/round-38/op/O07-scribe.md
-rw-r--r-- 1 vgpnk vgpnk 0 Oct 19 08:10 reports/round-38/op/O07-scribe.md
```

`O07` is a **declared seat** (`targets.json`: role scribe, claim O, mission
"Landed-changes material", out `op/O07-scribe.md`) and its out path **exists**. Every
existence-based census therefore counts it as delivered. Measured against the peer rounds:

```
rounds 33, 34, 35, 36, 37 : no empty fragments (0-byte scan over reports/round-<N>/*/*.md)
round 38                  : reports/round-38/op/O07-scribe.md — 0 bytes  ← the only one
```

and the integration dossier did not catch it — `scribe/S01-integration-draft.md §2.5`
lists the *absent* outputs (10 paths) and **does not include `O07`**, because the file
exists. So the round currently carries a "landed" O-block scribe deliverable that contains
nothing, and the O block's landed-changes material has no scribe fragment at all
(`op/O06-receipt.md` and `op/O08-regression.md` are genuinely absent and correctly listed).

**Consequence.** `O07`'s mission is "Landed-changes material" for claim O. Since nothing
has landed for claim O at any cut so far (R02, O05, S01 §0 all measure zero O artifacts),
the honest content of `O07` is a *declared-empty* record, not silence. An empty file is
indistinguishable from a truncated write, a crashed seat, or a seat that wrote and was
overwritten. The integrator's runner must assert **non-empty** on every declared out path,
and the round record must state `O07`'s disposition (empty-by-design vs not-delivered).

---

## 5. C2 — the claim-declaration census, with the correction the landed fragments omit

```
seat_count declared 32 | targets.json rows 32 | unique ids 32 | unique out paths 32
claims.json declares   : D (depth), O (operability)          axes_in_play: [depth, operability]
seat claim census      : D 13, O 10, cross 6, A 3
undeclared             : cross (6 seats), A (3 seats)  → 9 of 32 seats
```

Three landed fragments report this (`adj/A01-scope.md §5`, `adj/A02-receipt.md F-A02-1`,
`scribe/S01-integration-draft.md §2.3`), and two add "r38 is the first regimen-2 round
with this shape" (`S02 §2 F2`, `A02 F-A02-1`). I checked that against the sibling rounds:

| round | claims declared | non-`cross` census keys | non-`cross` undeclared |
|---|---|---|---|
| 33 | A, C, O | A, C, O | none |
| 34 | C, D, O | C, D, O | none |
| 35 | A, C, O | A, C, O | none |
| 36 | C, Ca, D | C, Ca, D | none |
| 37 | A, Ca, O | A, Ca, O | none |
| **38** | **D, O** | **A, D, O** | **A** |

```
cross declared in any of rounds 33–38 : False
```

**Correction.** The `cross` block is undeclared in **every** round 33–38 — it is the
lane's standing convention for cross-cutting seats, not a r38 anomaly. The r38 delta is
**`A` alone**: r33/35/37 all *declare* an `A` claim, and r38 does not. So the finding is
"r38 declares two claims but seats a third (`A`) that five of its six siblings declare",
which is sharper and more actionable than "first round with this shape" — and it means the
runner's `CO` leg must **not** be written to fail on the `cross` block, or it will fail
every round including the admitted ones. The integrator's real decision is narrow: file
`A` as unadjudicated adjacency work, or have the runner assert the partition and fail r38.

---

## 6. C3 — the record set at my cut, so "closed" is never read off fragment count

```
reports/round-38/validation.json      ABSENT
reports/round-38/run-validation.py    ABSENT
reports/round-38/kotodama.md          ABSENT
../.ufo/reports/round-38/             ABSENT (../.ufo/reports/round-37/kotodama.md exists)
../MANIFEST.json rounds[] has 38      False (252 rows; last ids 33,34,35,36,37)
LOG.md r38 entry                      ABSENT (last lane entry is round 37, LOG.md:3705-3722)
SCORECARD.md r38 row                  ABSENT (last table is "Axes — round 37", SCORECARD.md:668)
```

Two consequences the integrator must not lose:

1. **Both claims' threshold command is `to-verify` and both `after_required` states are
   unreachable at every cut so far.** No D or O artifact has landed — the fragments are
   drafts (`targets.json:6`: tool/example changes are integrator-applied). A runner
   measuring the live tree today measures the **before** state for every claim leg. This
   matches `S01 §0`; I record it because it is the reason the round cannot be reported
   as an admitted build yet.
2. **The telemetry close obligation is open.** `telemetry/dispatch-declared.json` carries
   `closing_snapshot: "open-at-seat-close: owed once validation.json lands"`, and
   `AGENTS.md` makes a round inadmissible to `LOG.md` while its own availability record
   still owes a closing snapshot. That is a hard gate on this round, not a formality, and
   it is owed in the same integrating pass that files `validation.json`.

---

## 7. Harm check per axis (the admission rule)

| axis | before → after at my cut | harm? |
|---|---|---|
| depth | unchanged — the two residues (F-6 counters, RL-8 era leg) are real, reproducible and **unlanded**; the drafts are verified-good in isolation (D03 §3) | **no** |
| operability | unchanged — no guard landed; R02 §6 measures the guard's gain as *naming*, not new detection (`13-register-law.yml` is already digest-checked transitively by `v3_verify_component_digests`) | **no** |
| coverage | untouched — no seat touched the corpus; `no freshness axis-move` non-goal held (`claims.json:26`) | **no** |
| freshness | **paused** by operator ruling (`claims.json:11`); no seat made a fetch or a freshness claim (`grep` over the round-38 drafts → no `http`/`fetch` work) | **no** |
| calibration | untouched — r38 is a build round; no `calib/` directory, no recount ledger (contrast r33/35/37) | **no** |
| adjacency | unchanged — the A block carries no declared claim (§5); its fragments are scope watch and routed findings, not axis moves | **no** |

**Trades that would harm if landed alone** (named so the integrator does not land them alone):
route B for F-6 harms operability (breaks a pinned selftest control and reddens the
default chain — D09 §2.2 controls E/I/J/K, R03 §4); the law-gate era leg harms the
battery's pinned reading until a new baseline id lands in the same edit set (§3); and the
era-leg id choice under `D4L-ERA`/`D4L-LAW-ERA` silently reduces depth's *verifiability*
without changing any file's green reading (§2.3).

---

## Owed

- **Integrator — T1, the era-leg id decision (blocking claim D's acceptance).** Decide the
  emitted id and the pipeline-visibility question **before** applying any era-leg draft, and
  do not accept "typed legs green" as the era-leg witness unless the id is
  `D4L-ARGOT-`-prefixed (§2.3). Owner: integrator; input to `O01`/`R03` if the O guard's
  named-row channel is touched in the same pass.
- **Integrator — T2, bind "the two named artifacts" to an explicit roster** that matches the
  route actually taken (one file under P01, two files plus a new baseline under D02/D08).
  Owner: integrator, before any draft is applied.
- **Integrator — C1, `op/O07-scribe.md`'s disposition.** Record it as empty-by-design or as
  not-delivered, and add a **non-empty** assertion on every declared out path to the r38
  runner (no such assertion exists in the fragment record; the 0-byte file is the proof).
  Owner: integrator / the O-block scribe seat.
- **Integrator — C2, the `A`-block disposition**, and write the runner's `CO` leg to
  tolerate the `cross` block (undeclared in every round 33–38) while reporting the `A`
  delta. Owner: integrator.
- **Integrator — C3, the record set**: `validation.json`, the runner (copy the
  `reports/round-33/run-validation.py:23` relative-`ROOT` shape, never the r34/r35 absolute
  `os.chdir` shape — `S01 §5`, defect `O12`), `.ufo/reports/round-38/kotodama.md`, the
  LOG/SCORECARD/MANIFEST rows, and the telemetry closing snapshot
  (`availability-close-38.json`, naming `closes` = `dispatch-declared.json` and its digest
  at close time).
- **Not owed / out of scope:** no re-freeze of `declared-in-r7` (zero bytes moved at my cut —
  packet `45f57132…`, twin `0e229138…`, expected `bbe15887…`); no freshness axis-move; no
  promotion/canon/clearance/closure; no filed-byte rewrite; no in-tree round-runner execution.
- **`to-verify` (blocked):** `reports/round-38/run-validation.py` does not exist, so claim
  D's third declared counting command and both claims' threshold command could not be
  exercised. Per F-C13-1 it must not be run in-tree regardless.
- **Not measured by this seat:** the `op/` block's absent drafts (`O01`, `O02`, `O03`,
  `O06`, `O08`) and `scout/K02`, `cross/X00`, `depth/D01` — absent at my cut, so their
  shapes are unverified here and T1 is argued from the three drafts that **did** land.

## Citations

Binding rules and this seat's assignment: `reports/round-38/targets.json` (seat `X01`,
`shared_rules`; seat census; seats `O07`, `O01`/`O02`, `S01`); `reports/round-38/claims.json`
(`:9,11,13-24,26-27` — the D and O claim text, thresholds, non-goals, the "two named
artifacts" phrases); `REGIMEN.md:16` (position-6 schedule row, no fallback clause) and
`:66-75` (undeclared providers forbidden; failed lane with no declared fallback routes to
`could-not-dispatch`); `AGENTS.md` (telemetry close-what-you-open gate).

Files and lines cited: `tools/gates/typed-pipeline-gate.py:84,131,460-472,526-541`
(the argot-gate-only invocation and the `FINDING D4L-ARGOT-` filter at `:530-531`);
`tools/gates/argot-derivation-gate.py:917-921` (the coverage line);
`tools/gates/register-law-gate.py:121` (`era` in `DECLARED_KINDS`);
`tools/check-gate-battery.py:117-132` (`REGISTER_LAW_GATE_NAMES`), `:540-545`
(`BASELINE-GATE-REVISED`); `tools/gates/expected/register-law-gate/r30-post/expected.json`
(`gate_sha256 15f8b232…`, `append_only_note`); `tools/exercise-handoff-e2e.py:157-170`
(`D4_COMPONENTS`, 12), `:1939-1965` (`V3_READ_SET`), `:2208-2222`
(`v3_verify_component_digests`), `:3811-3838` (`v3_exercise`, the existing one-directional
roster guard); `examples/culture-d4/packet.d4.yml` (L-53/L-54 loan rows, `stage: "E0"`,
no `register` key; L-55..L-62 stamp forms, `stage: "E1"`);
`reports/round-34/handoff/declared-in-r7/expected.json` (58 inputs, 12 D4 components);
`reports/round-26/register/rules.md:110-128` (`REGISTER-ERA-01`, the r26 `D4L-ERA` id);
`corpus/knowledge/verification/gate-frozen-run-standard.md:74` (baselines never rewritten).

Peer fragments read in full or in the cited sections, and folded with attribution:
`scout/K01-residue.md`; `plan/P01-d-plan.md` (§3.4 the verified draft, §3.3 the loan-layer
trap, §4.2 host pricing, §6.2 the id options); `depth/D02-rl8-design.md` (§2.1 host
rationale, §3.5/§6 the battery cost); `depth/D03-isolated.md` (§3 the verbatim
apply-and-verify, §4 the D08 host comparison, §5 the consumer probe, §6.1 pin cost by
host); `depth/D04-pins.md` (§2 the "two artifacts" reading, §3 the F-6 route costs, §4
RL-8's one new row); `depth/D05-verify.md` (§3 the C1–C4 era controls, §4 baseline
readings, §5 the harness); `depth/D06-verify-pins.md`; `depth/D07-receipt.md` (§0, §3.1,
§4.2, §5); `depth/D08-gap-fill.md` (§2.1/§2.3, §3 the placement fork, §4.2/§4.5);
`depth/D09-scribe.md` (§2.1/§2.2/§2.3 blast radii, §4 cross-claim observations, §5);
`depth/D10b-verify.md` (§2 route A, §3 route B, §4 the guard draft, §5); `op/O04-fix-route.md`;
`op/O05-verify-route.md` (§2 D-1, §3 D-2, §5 the r34/r35 literal assertions);
`adj/A01-scope.md` (§1 census, §3a–§3d blast radius, §4 the two-named-artifacts ambiguity,
§5 the A-block ruling); `adj/A02-receipt.md` (§2, F-A02-1, F-A02-3, §6); `adj/A03-verify.md`;
`review/R01-d-review.md` (§1–§5); `review/R02-o-review.md` (F1–F6, the guard-point
recommendation); `review/R03-cross-review.md` (§2, C1–C4, §5, §7); `cross/X02-honesty.md`
(§0–§5); `scribe/S01-integration-draft.md` (§0, §2.2, §2.3, §2.5, §5, §6, §7, §8, §9, §10);
`scribe/S02-telemetry-draft.md` (§1–§4).

Commands run (all from the lane root or an isolated `git archive 9bccc9b` copy under
`.scratch/x01/`, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

```
git rev-parse HEAD                                                          # 9bccc9b998bc9ee3542eb1fe3ee981f07cb26a26
git status --porcelain --untracked-files=all                                # 27 rows, all ?? reports/round-38/
git diff --name-status 9bccc9b                                              # empty
git diff --name-status 9bccc9b -- 'reports/round-[1-9]' 'reports/round-[1-3][0-9]' corpus/lessons tools/gates/frozen LOG.md   # empty
date -u +%FT%TZ                                                             # 2026-10-19T11:14:45Z
python3 -B tools/check-gate-battery.py                                      # battery_exit 0, fail 0, pass 7, unevaluable 0
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml   # exit 0, derived_pairs=8 violations=0
python3 -B tools/gates/register-law-gate.py    examples/culture-d4/packet.d4.yml    # exit 0, findings=0
python3 -B tools/gates/typed-pipeline-gate.py  examples/culture-d4/packet.d4.yml    # 20/20, exit 0
# T1 — id ⇒ pipeline visibility (injected emitter, .scratch/x01/idiso, fresh archive per run)
X01_ID=D4L-ARGOT-ERA python3 -B tools/gates/typed-pipeline-gate.py …        # FAIL L3b-argot, 19/20, exit 1
X01_ID=D4L-LAW-ERA   python3 -B tools/gates/typed-pipeline-gate.py …        # ok L3b-argot, 20/20, exit 0
X01_ID=D4L-ERA       python3 -B tools/gates/typed-pipeline-gate.py …        # ok L3b-argot, 20/20, exit 0
# T2 — the law-gate battery cost (.scratch/x01/lawedit, fresh archive)
printf '\n# x01 conformance control\n' >> tools/gates/register-law-gate.py && python3 -B tools/check-gate-battery.py
                                                                            # battery_exit 2, fail 0, pass 7, unevaluable 0
# membership census, read-set constants, filed-baseline replay, id/empty scans — python3 -c over the live tree
ls -la reports/round-38/op/O07-scribe.md                                    # 0 bytes
ls reports/round-38/validation.json reports/round-38/run-validation.py reports/round-38/kotodama.md   # all No such file
ls ../.ufo/reports/round-38                                                 # No such file or directory
```

Mutated bytes exist only under `.scratch/x01/` (gitignored); the in-tree digests were
re-verified after every control. `reports/round-34/handoff/declared-in-r7/**` was read
only; no `--freeze` was issued against it.
