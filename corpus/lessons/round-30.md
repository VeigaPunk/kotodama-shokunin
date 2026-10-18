# Round 30 — lessons gate-keeper: integrate the controls, not just the prose

source: `reports/round-30/{claims.json,targets.json,fixes/qreg-dangles.md}`; `reports/round-29/{validation.json,law-calibration-disposition.md}`; `reports/round-25/argot/forecast.md`; `reports/round-26/argot/D24-forecast-closure.md`; `reports/round-24/box1-craft.md`; `tools/{check-gate-battery.py,gates/register-law-gate.py,gates/argot-derivation-gate.py}`; `examples/culture-d4/components/13-register-law.yml`; `corpus/knowledge/linguistics/register-lexicon-ceilings.md`; `SKILL.md`; `AGENTS.md`; `PROVINCE.md`; `LOG.md`.

verified-at: opening independent reads and commands **2026-10-18T21:52:36Z–21:53:22Z**, lane HEAD `44145d5f337dea425c20dccafee98e0882678660`, declared baseline `87bfc9956f0fc60e6821fe53b622d0043e28be10`. This is a moving-tree survey; later readings are appended below rather than substituted for this opening snapshot.

scope: SCRIBE X34 writes only `corpus/lessons/round-30.md`. The path was absent before this write. This is the lessons gate-keeper's bounded evidence record, not the round verdict, the calibration seats' retrospective, the orchestrator's SKILL landing, or promotion certification. Filed rounds 8–29, their lessons, receipts, and indices remain read-only. Re-pins are new rows; corrections are new sections or files. No commit or push. All fictional systems remain NON-CANON; lore owns canon. No real-world rights ruling or game-mechanics decision is made here.

## Gate

Axes: **O / operability** (the five routed items and regressions), **C / calibration** (loop-3 retrospective, three-loop account, prospective freshness recommendation), **D / depth** (unified Register craft and the post-landing box-1 survey). These are conjunctive deliverables with distinct evidence, not interchangeable scores.

### Rule

**An integration closes a route only at the consumer that could fail it.** A record's existence must change the law replay; registering a gate must make a missing baseline fail closed; an amendment must preserve the false historical statement while correcting its interpretation; a speaker control must move the intended law row rather than an unrelated `speaker` field; and durable telemetry must remain interpretable without the scratch sample. A green control that requires the old defect is itself superseded by a successful repair.

## O — the opening controlled reading and the acceptance boundary

At **2026-10-18T21:53:01Z**, `python3 -B tools/gates/register-law-gate.py --packet examples/culture-d4/packet.d4.yml` exited **1**, with **four** `D4L-LAW-DANGLING` HOLDs: RGL-01 → QREG-05/QREG-07, RGL-02 → QREG-06, RGL-03 → QREG-08. Its coverage reported five law rows, four register identity rows, 179 record IDs, and four findings. The same-stamp `python3 -B tools/gates/register-law-gate.py --selftest` exited **0**, **33/33**. Those two facts are compatible: a selftest passing is not a clean delivered packet.

The baseline bytes, measured by the in-memory probe below, were packet SHA-256 `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f` and law-gate SHA-256 `bbad35784bfb463d41912908748ebb711f72109d811d0dc8f0110657e3b4c026`.

### Independent third-witness probe: absence of a token is not a resolved speaker

The command below ran read-only at **2026-10-18T21:53:01Z**, against the packet and gate hashes above. It deep-copies the parsed packet in memory and changes RGL-01 explicitly; it does not use the selftest's first-`speaker` regex or write tampered packets.

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
import copy, hashlib, json, runpy
from datetime import datetime, timezone
from pathlib import Path
print(datetime.now(timezone.utc).isoformat())
p = Path('examples/culture-d4/packet.d4.yml')
g = Path('tools/gates/register-law-gate.py')
gate = runpy.run_path(str(g))
packet = gate['load_naming']()['load_yaml'](p.read_text())
print('packet_sha256', hashlib.sha256(p.read_bytes()).hexdigest())
print('gate_sha256', hashlib.sha256(g.read_bytes()).hexdigest())
def read(obj):
    findings, _ = gate['evaluate_packet'](obj)
    return {gate['format_finding'](item) for item in findings}
base = read(packet)
for name, field, value in [
    ('speaker-tokenless', 'speaker', 'nobody-nowhere'),
    ('speaker-id-control', 'speaker', 'nobody-nowhere (ZZ-99)'),
    ('force-unknown-control', 'force', 'no-such-force'),
    ('force-negated', 'force', 'not-directive-binding'),
    ('consequence-blank', 'consequence', ''),
]:
    obj = copy.deepcopy(packet)
    row = obj['register_law'][0]
    row[field] = value
    new = read(obj)
    print(json.dumps({'case': name, 'row': row['id'], 'clean': len(base),
                      'tampered': len(new), 'added': sorted(new-base),
                      'removed': sorted(base-new)}, ensure_ascii=False))
PY
```

| RGL-01 mutation, 2026-10-18T21:53:01Z | Finding-line change | Reading |
|---|---|---|
| tokenless speaker `nobody-nowhere` | 4 → 4; no added or removed line | Outside the gate's ID-token resolver; not proof of speaker admissibility. |
| **Control:** speaker `nobody-nowhere (ZZ-99)` | 4 → 5; one `D4L-LAW-SPEAKER` | The resolver is discriminating, not inert. |
| **Control:** force `no-such-force` | 4 → 5; one `D4L-LAW-FORCE` | Unknown-vocabulary refusal works. |
| force `not-directive-binding` | 4 → 4; no added or removed line | Negated familiar substrings are not semantic validation. |
| blank consequence | 4 → 4; no added or removed line | An empty consequence is still not rejected by this predicate. |

The last two are **bounded residues**, not newly invented round-30 requirements: the round-28 lesson already names this vocabulary-versus-meaning boundary. The tokenless mutation and the selftest-tail defect must be distinguished too. A repaired control can prove that the intended law row was exercised; it cannot silently expand the resolver's published `Name (ID)` contract to all free-prose speaker descriptions.

### Five routes: what a closure must actually show

At the opening stamp the aggregate `routed-resolution.json` was absent; the new QREG fragment explicitly said implementation and verification were in progress. The statuses here are therefore **opening gates, not final dispositions**:

1. **QREG dangles:** supply the missing records or correct the design references, replay the resulting packet clean, and retain a missing/bogus-reference negative control. `fixes/qreg-dangles.md:9–11` chooses new QREG records while preserving RGL-02's refusal of binding stamp oaths. Importantly, the existing `delivered-packet-replays` selftest asserts `bool(base)`; a clean packet will correctly invalidate that old expectation. Replace it with successful evaluation and explicit row coverage, not a fabricated baseline finding. A resolver that is disabled to obtain zero is not a repair.
2. **Battery registration:** distinguish **baseline coverage** from **selftest execution**. At 21:53:01Z the read-only `runpy.run_path('tools/check-gate-battery.py')['REGISTERED_GATE_NAMES']` census returned **nine** gates, with the law gate absent. Closure requires the declared **10/10** coverage and a control in which the law baseline is removed or its pin is wrong; it does not automatically mean ten selftest legs execute. Preserve the isolation/write-scope guarantees when accommodating the law gate's packet dependency.
3. **X63-F2:** append the correction; do not erase line 4's false absence claim. The control is the baseline occurrence in `sound-symbolism.md:106`, not a successful current grep whose population now includes the new entry itself. This is an evidence defect, not province bleed.
4. **Speaker-tamper tail:** show the mutated target and the added finding, and show the corresponding clean row silent. Do not count a changed YAML string alone, or the continued four dangles, as a successful tamper. Preserve the tokenless-scope qualification above unless the implementation genuinely expands it.
5. **Telemetry durability:** land the convention in `AGENTS.md` and an interpretable demonstration under `reports/round-30/telemetry/`. A durable disposition of unavailable observations is honest; a provider sample, selftest, or declared worker count is not a recovered launch/completion census.

The common O gate is still **regressions green on the repaired read set**, with any necessary re-pins filed as new rows. At **21:53:11Z**, `git diff --name-only 87bfc9956f0fc60e6821fe53b622d0043e28be10 -- reports/round-{8..29} corpus/lessons/round-{8..29}.md` returned no paths. This is an opening preservation reading, not a promise about later concurrent writers.

## C — keep a disposition distinct from reproduction

The final R29 receipt is later than the R29 lesson's polling window. Reading `reports/round-29/validation.json` at this seat's opening shows `measured_at_utc: 2026-10-18T21:50:07Z`, `acceptance_checks_passed: true`, and C/O/A all true. It also keeps `law_clean_calibration.passed: false`, expected six versus observed four, and provider rows `could-not-evaluate-dispositioned` with `passed: false`. Its aggregate green accepts documented dispositions; it does **not** turn unreproduced data into reproduced observations. Preserve this distinction in the loop-3 retrospective. `r27_full_sweep_reproduced: true` also sits beside a disposition saying the full sweep was **not** independently reproduced: a boolean alone is not the evidence.

The R17 forecast is more specific than “a register exists”: the original eleven worked measure/numeral derivations, COUNT × QUOTE, `head2`/`reverse`, and the later furnace-league's FIRE × MARK/`stamp`/axis-conditioned `reverse`/`lengthen` are distinct designs (`reports/round-25/argot/forecast.md:28–39,49–112`). At **2026-10-18T21:53:11Z**, `python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` exited **0** with **183 records, 14 register-scoped records, eight derived pairs, zero violations, zero rule holds**. That is positive delivery evidence, not proof of literal zero delta against every R17 forecast element. Likewise, `reports/round-26/argot/D24-forecast-closure.md` is an explicitly early 18:07Z zero-pair reading; the final stratum and R29 matching-revision recount supersede its *current-state applicability*, not its historical bytes.

A three-loop summary must separate admissions, later semantic rejections, skips, amendments and provider designations; **R30 in progress and R31–32 scheduled are not completed rounds**. A concrete freshness recommendation is required, but operator adoption is separate. The old ratios **147/189 = 0.777777…** (comparable) and **147/192 = 0.765625** (all rows) remain below the old **0.95** threshold; loop-2 command recounts and loop-3 pin drift are different populations. The freshness pause remains in force until an operator changes the prospective contract. A new denominator must not retroactively admit a rejected round.

## D — a unified section needs executable boundaries, not only citations

At **2026-10-18T21:53:22Z**, this seat's read-only Python census used `re.findall(r'tools/[A-Za-z0-9./_-]*\.py', SKILL_text)` against files from `Path(root).glob('*.py')` for `tools`, `tools/gates`, and `tools/harness`. It found **28 live scripts, 19 named live scripts, nine unnamed**, and no `Register craft` heading. The nine were the seven historical box-1 gaps in `reports/round-24/box1-craft.md:25–35` plus the subsequently delivered argot and law gates: `assemble-d2-typed.py`, `exercise-handoff-e2e.py`, `gates/argot-derivation-gate.py`, `gates/d4-assembly-check-gate.py`, `gates/d4-typed-labels-check-gate.py`, `gates/register-law-gate.py`, `harness/packet_links.py`, `harness/r8_checks.py`, `harness/receipt_guard.py`, all under `tools/`.

The post-landing re-survey must measure again, not inherit that pre-landing nine. A section that names the two new gates may reduce the inventory gap without closing the seven older ones; the dossier permits either naming the scripts **or an explicit inventory-scoping disposition**. Neither route is promotion by itself. Every new craft row needs a resolving citation and a clear distinction between an executable leg and a design limit. In particular: register is not a checked-channel exemption; borrowed stratum is not native derivation; operation selection must replay its declared axis rule; and speaker/force/consequence checks do not imply complete legal or era enforcement.

## The lessons ledger — this new file also changes its own denominator

At **2026-10-18T21:53:01Z**, `len([p for p in Path('corpus/lessons').glob('*.md') if p.name != 'README.md'])` returned **29**, and this file did not exist. The same read-only census counted literal `corpus/lessons` references in R25/R26/R27/R28/R29 runners as **9/7/0/0/0**; the R30 runner was absent. These are source-reference counts, not a claim that every reference executes an acceptance check. Writing this lesson adds one more file to a live partition; it does not repair either filed index. Any new index or lesson pin belongs in an authorized new row or revision after these bytes settle.

## Open routes and boundary record

- **Q-30-1 — operator / freshness:** prospective measurement contract and threshold remain operator-owned. A recommendation is not adoption; retain the historical rejections and pause.
- **Q-30-2 — parent / lesson indexing:** this new lesson changes the partition and may create another unindexed file. Do not amend filed indices; explicitly disposition the live-ledger coverage if it remains outside acceptance.
- **Q-30-3 — gate owner / semantic ceiling:** named-ID speaker resolution and vocabulary/stem checks leave the controlled residues above. A bounded round-30 repair must not be described as complete enforcement of speaker admissibility or law meaning.
- **Writes:** this new lesson only. No scratch files, implementation, shared bookkeeping, prior lesson, or filed receipt written by X34. All probes so far were read-only/in-memory, with `PYTHONDONTWRITEBYTECODE=1`; no round validator was invoked.
- **Opening status:** O/C/D dependencies and final aggregate receipt were pending. This section grants no round admission, freshness recalibration, or promotion. Later dependency readings and any closeout belong in new dated sections below.

## Dated integration observation — two telemetry contracts, 2026-10-18T21:54:36Z–21:54:57Z

The durability rule now exists in `AGENTS.md:15–31`: raw evidence and count provenance belong under `reports/round-<N>/telemetry/`, unknowns remain null, and final-wave updates are new snapshots. The O11–O12 producer's `dispatch-stats.json` is a partial worker observation, explicitly not a closed wave: requested 32, observed-session lower bound one, actual route/launches/completions unknown. Its own `python3 -B reports/round-30/telemetry/dispatch-telemetry.py --check` ran at **2026-10-18T21:54:57Z**, exit **0**, `passed: true`, `findings: []`, `full_wave_status: could-not-evaluate`.

But a second delivered reader consumes the same filename under a different schema. At **2026-10-18T21:54:36Z**, `python3 -B reports/round-30/telemetry/check-dispatch.py` exited **1**, traceback at `check()`'s `record['date']`, **`KeyError: 'date'`**. Its X37 contract expects `date`, `seat: R30-X37`, `runtime`, and `raw_evidence`; the producer carries `counts_date`, `owner`, `stats`, and `sources`. This is a real producer/consumer integration disagreement at the named stamp, not evidence that null runtime counts should be fabricated. The same-stamp producer check is the positive control that keeps the finding narrow: one telemetry contract validates; the other cannot consume that payload.

At **21:54:57Z**, the read-only `hashlib.sha256(Path(path).read_bytes()).hexdigest()` command bound the observation to snapshot `a1f8ec193661eb43b1c4e8f9635588ad33518a70a0c3213403d305e38bad270f`, X37 reader `c13a04051846b37a833b9c036ef3429408b5e625ef5d574cae7211965ed2b822`, producer `a177757b3680248bd75b04252c8982864816c13b0178055b4185457f1bb61b1e`, and AGENTS `e03fc01b61d94d53aef1889ddb271f98719dd287c56798a2431e4a123a165aed`. **Q-30-4 — telemetry owners / parent:** choose or reconcile the canonical contract, re-run its actual consumers and negative controls, and disposition the incompatible reader rather than letting one green stand for both. A later repair is a new dated reading below; it does not erase this mid-wave collision.

## Dated recheck — repaired records, newly exposed consumers, 2026-10-18T21:55:24Z–21:56:34Z

**The QREG producer repair is observable and discriminating.** At **21:55:24Z**, the direct law CLI exited **0**, with five law rows, eight register identity rows, 183 record IDs, zero dangles and zero findings. Packet SHA-256 at **21:55:35Z** was `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`; the law gate still hashed `bbad3578…`. At **21:55:52Z**, this seat reused the in-memory probe above, first dropping `registers` record QREG-05 and then replacing RGL-01's `design_row` with `['ZZ-99']`: each changed zero clean findings to **one** named `D4L-LAW-DANGLING` HOLD. A clean zero was not obtained by disabling reference resolution. The same probe still read zero on a tokenless RGL-01 speaker and one SPEAKER finding on its ZZ-99 control.

**The consumer failures are distinct, and predicted.** At **21:55:35Z**, the real law `--selftest` returned **29/33**, exit **1**. Besides the obsolete `bool(base)` expectation, the three unscoped first-field mutations now hit newly added QREG identity rows rather than `register_law`. At that same stamp, this read-only battery command reported registration **ten**, coverage **9/10**, `BASELINE-GATE-UNCOVERED` for the law gate, baseline exit **2**, and still seven structural selftest legs:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
import json, runpy
from pathlib import Path
b = runpy.run_path('tools/check-gate-battery.py')
r = b['inspect_baselines'](b['BASELINE_ROOTS'])
print(json.dumps({'summary': r['summary'], 'findings': r['findings'],
                  'selftest_legs': [name for name, *_ in
                      b['leg_plan'](Path('/nonexistent-readonly-probe'))]}))
PY
```

The new speaker-seat `fixes/speaker-tamper.md` explicitly supplies an **in-memory candidate for parent landing**, not a delivered tool edit. Its proposed closed speaker/holder-clause grammar and law-block-local mutation address both limits; a future green must be measured on the delivered tool, not credited from the candidate's prose. The missing law baseline must freeze the settled gate and packet, after those edits. This is why an integrate round cannot freeze the consumer before the producer settles.

**Q-30-4 is resolved at the two readers, not by discarding evidence.** By **21:55:35Z**, X37's reader instead loads its own new `telemetry/dispatch-declaration-x37.json`, leaving the O11–O12 worker-observation snapshot on its original path. At **21:55:52Z**, actual CLI calls `python3 -B reports/round-30/telemetry/check-dispatch.py --selftest` and `python3 -B reports/round-30/telemetry/dispatch-telemetry.py --check` both exited **0**. X37's **11/11** negative controls rejected the unsupported mutations; runtime remained could-not-evaluate. Independently at **21:55:24Z**, in-memory calls to the O11–O12 producer's `validate(root, deepcopy(snapshot))` rejected all **four** planted changes: requested-as-completed inflation, a scratch-only source path, a false full-wave pass, and a missing count date; the unmodified snapshot returned no findings. These controls prove bounded declaration/durability honesty, not full-wave attendance.

**The historical census has a useful independent control.** This seat ran `python3 -B reports/round-30/retrospective-audit-C23-C25.py --numbers --selftest` at **21:55:24Z**, exit **0**. It recovered **18 admissions / three rejections (11, 17, 22) / one skip (13)** through R29, **20 archived receipts / 55 true and two false filed flags**, loop-3's **15 true flags**, and the original **147/189** and **147/192** ratios below **0.95**. Its twelve pointer controls and nine anti-inflation controls passed. R22's missing aggregate JSON is not a missing round: its rejection is in the parent LOG. The newly landed retrospective keeps R30 active and R31–32 prospective and recommends a prospective two-channel pilot: settled-tree raw replay at **≥95%**, all preregistered rows in the headline denominator, zero unexplained semantic regressions, zero protected-byte mutations, and separate authorized-change accounting. That is a concrete recommendation, not an adopted policy or a new F verdict.

**Q-30-5 — retrospective owner / parent: bind the R27 late-sweep number to its actual artifact.** The R29 C11 addendum says **41 findings** and cites `reports/round-29/recount/r27-full-sweep-reproduction.json`; the R30 retrospective repeats that channel. But this seat's **21:56:34Z** read-only `json.loads(Path(path).read_text())` / SHA-256 extraction found that receipt's `summary` is **`exit: 1, findings: 31, surfaces_enumerated: 117`**, `revision: e923d6ecaf5fd9d256e4b377745bd3d24f5e2d47`, digest `8044af93b0230c88f07e802da3d84927b5f3d97d0ac9593b6f1662bcc400e5fc`. Preserve the historical prose and receipt discrepancy; do not silently present **41** as that JSON's reproduced count, or **113** as its measured surface count. A current-round correction or separately located 41-result receipt is needed. This is a content-support finding, not a request to edit filed R29 bytes, and not an independent replay of the full sweep by X34.

## Dated recheck — preserve the discrepancy, close the bad attribution, 2026-10-18T21:59:08Z–21:59:17Z

**Q-30-5 is now dispositioned in the current retrospective.** Its “R27 full sweep” correction explicitly keeps C11's 41/41 prose beside the durable JSON's **117/31/exit 1**, refuses exact count agreement, and requests a parent follow-up without changing either filed source. The report read at **21:59:17Z** hashes `edda7ba51a6793e88f7ce30500cc7ee4e7065cbd2550640c2d7b45d260a7a6f2` (`hashlib.sha256(Path(path).read_bytes()).hexdigest()`). C24 independently reached the same finding and closed the attribution defect in `retrospective-audit-C24.md:44–52`; its earlier numeric PASS binds a different report digest and must not be inherited across later edits. The historical prose/receipt disagreement remains; the new report no longer presents it as exact reproduction.

A **different parser** confirms the QREG landing, independently of the gate's loader. At **21:59:08Z**, `ruby -ryaml -rjson -e` loaded `examples/culture-d4/packet.d4.yml`, harvested `id` values from top-level record lists, and checked every law `design_row` against that set: **five law rows, eight register rows, 183 distinct IDs, all four QREG references resolving**, and RGL-02's force still **`commissive-binding refused`**. The same-stamp command `git diff --exit-code 87bfc9956f0fc60e6821fe53b622d0043e28be10 -- examples/culture-d4/components/13-register-law.yml corpus/knowledge/linguistics/register-lexicon-ceilings.md PROVINCE.md` exited **0**. The law source, false historical absence statement and province are preserved; the correction lives in the authorized new records/companion amendment.

The more general protected-surface check, `python3 -B reports/round-30/retrospective-audit-C23-C25.py --protected`, ran at **21:57:32Z**, exit **0**: **1,764 historical report/frozen paths, zero mismatches**, manifest SHA-256 `7d4b532e5080e7783b1d544fe06afea5e84d33de9ac8ffa997fbea6b1c7577eb`. This is byte/mode equality at that stamp, not proof that no concurrent writer ever touched a byte.

**D remains a landing boundary.** The new D29 review explicitly calls its **28/28** inventory a *virtual insertion*, not post-landing verification (`craft/review-D29-box1.md:28–43,84–121`; its dated read-only inventory command). At **21:59:17Z**, this seat still reads SKILL hash `2d85bfea…` with no Register craft section, while the draft hashes `a6e8a69a4d465de9087752c5c533c9f4138d79e846d1cd5d0668a6fdbc02b5ad`. The draft and its reviewers can satisfy preparation; the parent must still land it and run the survey in **landed** mode. No author review or zero-unnamed census alone grants promotion.

The lesson partition itself is now **30 files excluding README**, counted at **21:59:17Z** by `len([p for p in Path('corpus/lessons').glob('*.md') if p.name != 'README.md'])`. That is this new lesson's predicted denominator change, not an index repair. Instrumentation note: X34's initial mutation probes invoke the delivered gate API and are independent of its selftest's target selection, **not a separately reimplemented law validator**; the Ruby check above is the independent parser/reference census. No round acceptance command has been run by this seat.

## Handoff cut — 2026-10-18T22:00:13Z

The read-only dependency watcher ran **six observations at 60-second spacing**, **21:54:18Z–21:59:18Z**, stopping when the routed ledger, retrospective and runner all existed. It printed `Path.is_file()` / size / SHA-256 states only; no scratch/polling file was written by this seat. It did not wait for parent-owned skill/tool landing, and existence was never read as acceptance.

**O — disposition coverage present, regression gate not met.** At **22:00:00Z**, `json.loads(Path('reports/round-30/routed-resolution.json').read_text())` read exactly **five** rows: QREG, X63-F2 and telemetry **fixed-with-control**; law battery and speaker tail **documented-with-owner-and-reason**. Ledger digest `c53c11d41d4daecbac1bf2d060bac46f70f62685258fb52045d957ddecdaf74e`; `regressions_green: false`. Its controls and limits agree with this survey. The dated O13 sweep, original command `python3 reports/round-30/verify-operability.py --regressions-only`, **2026-10-18T21:57:45Z–21:57:47Z**, reports **36/40**, both all-command and all-current-regression flags false, protected bytes unchanged, and no input drift (`reports/round-30/regression.json`, digest `0c97a563d66ba1afda4103fac28f600bb2a742293167ed4913d8a8850102273d`). Its four nonzero commands are the default battery (exit **2**), delivered law selftest (exit **1**), v3 handoff (exit **1**), and v3 handoff selftest (exit **1**). Owner/reason routes satisfy disposition accounting; they do not satisfy the separate **regressions green** requirement.

**C — the consolidated count controls reproduce at a named digest.** At **22:00:13Z**, this seat independently executed the two inspected, read-only `sh` blocks in `loop3-retrospective.md` through `subprocess.run(['bash'], input=block, ...)`, in a `ThreadPoolExecutor(max_workers=2)`. **2/2 exited 0**, no stderr; report digest **`edda7ba51a6793e88f7ce30500cc7ee4e7065cbd2550640c2d7b45d260a7a6f2`** was unchanged before/after. M1 reproduces the historical state/flag/recount/null-attendance boundaries; M2 reproduces the amendment identities, probe-only populations, 117/31/exit-1 sweep receipt versus preserved 41-count prose, and the bounded R29 **11/11** direct-regression inventory. The nonexistent numbered R29 report locator has also been replaced by its real `:11–22`/`X04 settled-tree rerun` locator. This is count/control and scoped content verification, not a new historical execution, a full primary-source audit, or adoption of the freshness recommendation.

**D — prepared, not landed.** The draft and cited reviews are present. The last SKILL read still has no unified Register craft subsection. The parent must land the synthesis, run D29's survey with `REGISTER_CRAFT_SURVEY_MODE=landed`, and bind the post-landing evidence to the actual SKILL digest. A virtual **28/28** does not fill that requirement.

**Aggregate receipt boundary:** the visible `reports/round-30/validation.json` read at **21:59:46Z** was measured **21:56:22Z**, `acceptance_checks_passed: false`, digest `c2560021d57e20f3b00db929be20dd50f36fd8859cd25da71dc3367e49514d04`. It predates the routed ledger and later report edits; it also reports evidence movement. Preserve it as an in-flight red, not a verdict on the final integration. The settled counting command remains the assigned runner's/parent's responsibility.

### Parent closeout actions, not waived gates

1. Land the speaker-seat candidate on the actual tool; replay clean, tokenless, ID-bearing and unchanged-field controls on that tool. Preserve force/consequence and broader law/era limits.
2. Freeze the law gate's settled packet/tool dependencies as a **new default-root baseline**, obtain battery **10/10**, and retain omission/tamper controls. Finish the v3 successor hold-set/baseline path and rerun its two failing commands; do not refresh filed old generations.
3. Land Register craft and file the actual post-landing box-1 survey. Rebind C23/C24 and the aggregate runner after the last content change. Do not inherit any older receipt's runner/input hashes or grant promotion from a self-review.
4. Keep Q-30-1 (operator freshness contract), Q-30-2 (lesson-index coverage), the remaining Q-30-3 semantic limits, and the historical source disagreement visible. Q-30-4 is resolved by distinct telemetry paths; Q-30-5 is closed as a current-retrospective attribution defect, not by rewriting historical evidence.

### Deliverable checks and write boundary

X34's lesson checks used read-only Python `ast.parse` on its embedded Python blocks, `bash -n` on its shell blocks, balanced-fence/required-Gate-marker/trailing-whitespace assertions, and an exact-positive-file citation scan with an in-memory nonexistent-path negative control; these passed at the survey's verification stamps. The generic retrospective pointer scanner initially misread the literal `round-<N>` template as a missing `reports/round-` path; that diagnostic is a template-parser limitation, not a resolving positive citation. No missing positive literal file was accepted. Final byte/structure checks belong to the consumer after any append.

**Only `corpus/lessons/round-30.md` was written by X34.** No scratch artifact, prior round/lesson/index, implementation, receipt, shared bookkeeping, province or promotion file was changed by this seat. No commit, push, network probe, historical writer or round acceptance command was invoked. **This handoff withholds O/D completion and whole-round admission while the named integration gates remain open.**

Lesson filed by SCRIBE X34, round 30. Corrections and post-landing observations are new dated sections or successor files, never silent rewrites of the readings above.
