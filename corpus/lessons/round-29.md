# Round 29 — lessons gate-keeper: a count belongs to its snapshot, and a runner green is not an independent calibration

source: `reports/round-29/{claims.json,targets.json,rerun.json,report-draft.md}`; `reports/round-29/recount/{r25-1.md,r25-2.md,r25-3.md,r25-4.md,C05.md,C06.md,C07.md,C08.md,C09.md,C10.md,C11.md,C12.md,C13-C16.md}`; `reports/round-29/defects/{ledger.json,fix-09.md,fix-10.md,fix-11.md,fix-12.md,fix-13.md,fix-14.md,fix-15.md,fix-16.md,sweep-r25.md,sweep-r26.md,sweep-r27.md,sweep-r28.md}`; `reports/round-29/adjacency/{ledger.json,register-law.md,province-entries.md,A09-A12-handoff.md}`; `reports/round-29/scope.md`; rounds 25–28 claims, validation receipts, runners, and availability records; `PROVINCE.md`; `corpus/knowledge/linguistics/{register-strata-attestation.md,register-lexicon-ceilings.md}`; `corpus/lessons/round-25.md`–`round-28.md`.

verified-at: read-only evidence review **2026-10-18T20:59:34Z–21:13:09Z**; lane HEAD at the settled-tree rerun **`e923d6ecaf5fd9d256e4b377745bd3d24f5e2d47`**. R29 fragments arrived during this review; readings below are tied to their commands, dates, and revisions, not treated as one timeless tree.

scope: SCRIBE X01 — independent gate-keeper lesson for loop-3 rounds 25–28. This is not the R29 acceptance verdict or parent integration. Only this new lesson is the tracked write. Filed rounds 8–28, their receipts, `PROVINCE.md`, and the lesson index remain untouched. No commit or push; **`reports/round-29/run-validation.py` was not run**.

## Gate

Axes: **C / calibration** (historical readings and independent recounts), **O / operability** (defect ledger and replay surface), **A / adjacency** (province and bleed boundary). Keep a historical receipt, a settled-tree runner result, and an independent check in separate columns of thought: none silently replaces the others.

### Rule

**A count is true of the bytes and command that produced it, at that revision.** A later packet population is not a correction to an earlier snapshot; a design probe is not the delivered gate; and a runner's green is only as broad as its named checks. Record a changed reading as drift, scope mismatch, or an unresolved defect—not as a number to normalize.

## C — calibration: the R26 landing reproduces; the clean-law six does not

### Historical readings and snapshot boundaries

- On **2026-10-18**, the R25 recount ran `python3 reports/round-25/run-validation.py` against its admitted isolated snapshot. `recount/r25-1.md` reproduces **26 lesson files and 26 index rows**; `r25-4.md` reports an independent replay of the fixed regression inventory with filed labels, arguments, and exits matching. These are R25-snapshot results, not the current lesson partition. At X04's settled-tree rerun stamp before this lesson landed, `python3 reports/round-25/run-validation.py --check` (**2026-10-18**) reads **29** lesson files against the old **26**-file index and **82** typed labels against the old expected **74**. The later tree drift does not rewrite the historical R25 receipt.
- The R26 register landing is independently reproduced at its own commit. On **2026-10-18**, the R26 frozen-packet/component census command in `recount/C05.md` found **8** `register=stamp` forms in each source. In that isolated R26 checkout, `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` returned **170 records, 14 register-scoped records, 8 derived pairs, and 0 violations** (`C06.md`); `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` exited **0** with **20/20** legs (`C07.md`). These counts describe R26's pinned packet, not later live bytes.
- The snapshot distinction is independently visible in the dated R27/R28 recounts. On **2026-10-18**, `recount/C11.md`'s manifest census counted **12 manifests / 86 rows / 16 D4-marker rows** at the R27 declaration revision, then **13 / 88 / 18** at the later R27-admitted snapshot; its note explicitly does not claim to replay the frozen manifests. `recount/C12.md` ran the archived R27 X63 locator check on **2026-10-18**: **41 resolved locators, 0 unresolved**, while the filed “32 resolved” described a different **44,136-byte / 234-line** entry; the admitted entry was **57,996 bytes / 313 lines**. Its own unpinned `verified-at` text says **36**, so **32/36/41** remain revision/tool readings, not a silently reconciled count.
- `recount/C13-C16.md` ran the delivered argot gate on **2026-10-18T21:03:53Z**: `python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` exited **0** with **183 records, 14 register-scoped records, 8 derived pairs, 0 violations, 0 rule holds**. Its separate packet census compared the R27 frozen packet and R28 live packet on **2026-10-18**: **175** record rows with **0/8** RL-4 IDs versus **183** rows with **8/8**, a measured **+8** row delta. The **170** R26 records, **175** R27 rows, and **183** R28/live records are different snapshots, not inconsistent counts.

### Clean-law calibration: preserve six versus four

The R29 claim asks for a delivered clean-packet law calibration of **6** findings. At **2026-10-18T21:03:53Z**, the direct command `python3 -B tools/gates/register-law-gate.py --packet examples/culture-d4/packet.d4.yml` exited **1** and emitted **4** `D4L-LAW-DANGLING` HOLDs for QREG-05 through QREG-08. The settled R28 runner's clean-law reader, `python3 reports/round-28/run-validation.py --check` on **2026-10-18**, also reports **4**. Exit **1** is the delivered gate's findings result, not an unevaluable result.

A separate probe, `python3 -B .scratch/r28-law/replay-probe.py`, was run at **2026-10-18T20:59:34Z** against packet SHA-256 `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f`; it reports **6** total: **4** dangling references plus **2** consequence-class-fit heuristics on `force: none` rows. The delivered reader scopes those constraint rows out. Thus the design/reference probe's six do not reproduce as six delivered-gate findings. **Do not call the delivered four “six”; the R29 six-finding criterion remains unresolved pending an explicit scope disposition.**

A related definition mismatch was counted at **2026-10-18T21:04:22Z** by the design-table/gate-ID extraction command in `C13-C16.md`: the design heading says “six classes” but the table has **7** distinct IDs; the gate's declared-ID section has **10** IDs. That is a separate documentation/coverage count, not evidence that those IDs all fire on a clean packet.

The R28 final sweep is another independent counterexample to reading a green runner as a complete sweep. At **2026-10-18T21:03:53Z**, `python3 -B .scratch/r29-c13-c16/clone/reports/round-28/sweep/sweep.py --json --tmp-parent "$PWD/.scratch/r29-c13-c16/tmp"` in the isolated settled-tree clone reported **121 surfaces, 39 findings, 11/12 nonzero manifest replays**, and exit **1** for drift/re-pin owed. This does not edit or overturn R28's filed receipt; it shows that the R28 runner's “all replays” green does not grade that manifest sweep.

### Devin availability samples

On **2026-10-18T21:08:29Z**, a read-only `python3 -B -` aggregation over the local raw sample JSON files (paths and script below) counted these sample rows and HTTP statuses:

```sh
python3 -B - <<'PY'
import json
from pathlib import Path
samples = {
    25: ['.scratch/x41/sample-60x16.json', '.scratch/x41/sample-24x8.json', '.scratch/x41/labeled.json'],
    26: ['.scratch/x59/sample.json', '.scratch/x59/sample2.json'],
    27: ['.scratch/x53/sample.json', '.scratch/x53/labeled.json'],
    28: ['.scratch/x53-r28/sample.json', '.scratch/x53-r28/labeled.json'],
}
for rnd, files in samples.items():
    total, rows_n = {}, 0
    for name in files:
        data = json.loads(Path(name).read_text())
        rows = data.get('attempts', []) if isinstance(data, dict) else data
        rows_n += len(rows)
        for row in rows:
            status = str(row.get('http_status'))
            total[status] = total.get(status, 0) + 1
    print(rnd, rows_n, total)
PY
```

| Round | Rows in sampled JSON | HTTP status totals |
|---|---:|---|
| R25 | 118 | 113 × 200, 5 × 400 |
| R26 | 175 | 173 × 200, 2 × 400 |
| R27 | 156 | 152 × 200, 4 × 400 |
| R28 | 163 | 156 × 200, 6 × 400, 1 × 403 |

These are local sample/control populations, not counts of accepted worker launches. The availability records identify the temperature-zero 400s and R28's deliberate error-path probes; they are not silently reclassified as provider failures. The R28 availability record separately defines its well-formed clean sample and records **151/151**; its reproducible command is in `reports/round-28/availability.json` (`wellformed_population.counting_command`), dated **2026-10-18**. The seat records leave launched/completed worker counts unobservable; declared worker intent must not be presented as a measured launch count. The raw-sample recount confirms sample populations only; it does not certify launch/completion totals or the complete provider availability claim.

### Settled-tree runner readings are not the historical receipts

On **2026-10-18**, X04 ran each command below with `--check` in its own clean clone at settled HEAD `e923d6ecaf5fd9d256e4b377745bd3d24f5e2d47`; `reports/round-29/rerun.json` records no receipt writes. The filed R25–R28 receipts remain unchanged and historically green. These are readings at X04's recorded rerun stamp, before this lesson landed—not a fresh verdict on the post-lesson tree:

| Settled-tree command (2026-10-18) | Runner reading and cause |
|---|---|
| `python3 reports/round-25/run-validation.py --check` | Exit **1**, C/D/O fail/pass/fail: later lesson/index drift and current typed-label projection **82** versus expected **74**. |
| `python3 reports/round-26/run-validation.py --check` | Exit **1**, C/D/O fail/pass/fail: pin-repoint check **16/17** (`new-v3-row-replays-green` fails) plus later lesson/index drift; current packet count **183**, not the R26 snapshot's **170**. |
| `python3 reports/round-27/run-validation.py --check` | Exit **1**, C/D/O fail/pass/fail: **6** D4 surfaces lack the required R27 structured re-pin. Its canon-claim warning conflicts with the entry's explicit NON-CANON boundary and is not an independently established adjacency breach. |
| `python3 reports/round-28/run-validation.py --check` | Exit **0**, C/D/O pass/pass/pass. This is the runner result only; the separate law-gate and final-sweep commands above expose checks the runner does not grade. |

The R26 runner also has a measured clone-isolation limitation: when probing a historical state, its `live_lane()`/sync path can copy current lane bytes into an in-repo clone. That mixed-revision result is excluded as historical R26 evidence; the direct matching-commit gate recount is the relevant independent reading (`rerun.json`, **2026-10-18**).

## O — operability: ledger is useful only if its status and limits survive

`reports/round-29/defects/ledger.json` consolidates dated evidence, defect classes, status, owners, bounded controls, and Round-30 routes. It keeps prior bounded corrections (such as the R25 typed-input false red and append-only v3 supersession) distinct from open or merely observed issues. The sweep reports also separate the R27 inventory/snapshot failures from the R28 runner and replay defects; neither historical red nor later green is promoted into a timeless product verdict.

The still-routed examples include single-row null/missing typed holds and malformed-input tracebacks; argot identity/pair-scope, label-typing, and diphthong behavior; law-force polarity, consequence/speaker blind spots, dangling design references, missing regression registration, and assembler field validation; frozen replay against live dependencies and misclassified refusals; acceptance-clone self-sync; check-mode receipt writes; and sweep inventory/key coverage. These are not one failure mode. The ledger's `open`, `observation`, `closed`, and `superseded` statuses must remain distinct, and unverified historical probes must not be described as current failures or current fixes.

The dated defect sweeps found that the R25 production derivation path had **0** delivered pairs despite its clean gate exit (`python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml`, 2026-10-18); the R27 inventory's D4 denominator changed from **26** surfaces/**9** swept/**17** missed to **29**/**24** missed across snapshots (`python3 reports/round-27/audit/o37-sweep-inventory-audit.py`, 2026-10-18); and the R28 acceptance clause omitted frozen-manifest replay while `replay-frozen.py` could read live-tree inputs (`python3 reports/round-28/run-validation.py --check` and isolated replay audit, 2026-10-18). The R29 ledger documents controls and routes; it is not itself proof that every open issue has been fixed. This scribe changed no implementation and grants no O verdict.

## A — adjacency: scoped in-province pass, with an evidence defect kept separate

The independent read of `PROVINCE.md` and both knowledge entries agrees with the scoped R29 adjacency audit. On **2026-10-18T21:03:06Z**, the exact-anchor command recorded in `adjacency/A09-A12-handoff.md` found the same **5** RGL IDs in the law component and packet and one corpus-index row for each of the **2** entries. On **2026-10-18T21:05:40Z**, the adjacency ledger census reported **6** scoped paths, **0** bleed, and **0** unfiled bleed; the ledger itself limits the claim to those paths.

“Rights, duties, permissions” is used as theoretical speech-act/deontic vocabulary; “furnace right” and “right-of-way” are fictional D4 design/gloss content. “Verlan” and “language games” are linguistic analogues, not game mechanics. The law component and both entries explicitly mark the exercise NON-CANON and hand canon/world truth to lore. `PROVINCE.md` remains accurate and unchanged in its recorded hash check. No real-world rights ruling, attribution/permission clearance, canon decision, or game-mechanics ruling is made here.

A separate source-sweep problem is an evidence defect, not province bleed. At **2026-10-18T21:02:17Z**, the offline X63 command `python3 -B reports/round-28/audit/x63-entry-source-resolvability.py --offline --json --baseline 6c0ac4484d7ee5d15aaf190e7ad3b8817ea13ede` exited **1** because **4** quoted sweeps did not reproduce: one absence claim was already contradicted at baseline by `sound-symbolism.md`, while **3** were sibling-entry landings. The audit classifies one as an authoring defect and three as later landings; it does not find out-of-province content. The cited URLs were not all independently retrieved, so this is not a source-merits certification. The adjacency review also excludes the whole D4 tree and does not close the older R21 `typed-labels.d4.yml` boundary finding.

## Closeout and rejected readings

- **Reject:** “the clean-law calibration is six because the design probe says six.” The delivered gate emits four dangling findings; the two extra reference-probe heuristics are not delivered-gate findings.
- **Reject:** “the later 183-record packet disproves the R26 170-record reading.” Both direct commands are correct for different revisions; preserve the boundary.
- **Reject:** “R28 runner PASS means every manifest replay and clean-law calibration passed.” The independently rerun R28 sweep exits **1** with drift findings, and the law gate is not covered by the runner's replay clause.
- **Reject:** “R27's canon warning proves the entry is out of province.” The independent content read finds explicit NON-CANON and canon-handoff boundaries; the warning is not a demonstrated breach.
- **Reject:** “the scoped adjacency pass proves all D4 surfaces clean.” The audit's explicit non-scope includes the previously filed `typed-labels.d4.yml` finding.
- **Reject:** “a new lesson repairs the old index or receipt.” The lesson index and all prior round files are read-only in this assignment; any index repair belongs in a new authorized revision.

At the last completed dependency inventory, **2026-10-18T21:13:09Z**, `reports/round-29/run-validation.py` and `reports/round-29/validation.json` were absent; the lesson was also absent before this write. The `claims.json` read during this review (**2026-10-18**) still said `declared-before-dispatch`. Therefore: **C remains incomplete** (the six-versus-four calibration is unresolved, provider worker launches are unobservable, and the visible recount set does not establish every R25–R28 counting command); **O has a consolidated queue but open work remains**; **A passes only within its audited slice, with the source-sweep evidence defect preserved**. These are this seat's scoped readings, not a Round-29 verdict. **No round verdict or promotion is independently granted.**

## Boundary record

- **Writes:** this lesson only as tracked output; read-only polling log under `.scratch/x01-r29/`. No R25–R28 receipt, report, index, source, or province file changed. No R29 validator, commit, or push.
- **Independence:** historical recount fragments and R29 worker reports are attributed to their commands; X04's C/D/O states are identified as runner results; the local Devin raw-sample aggregation and direct law/argot probes are independent measurements, not round acceptance.
- **Known limits:** no aggregate R29 receipt was present at the polling deadline; not all claimed counts have independently landed; the adjacency pass is scoped; raw Devin samples do not show launched-worker totals; and the R28 independent sweep is a dated snapshot, not a current replay guarantee.

Lesson filed by SCRIBE X01, round 29. Any correction belongs in a new dated record or successor lesson, not an in-place rewrite of these readings.
