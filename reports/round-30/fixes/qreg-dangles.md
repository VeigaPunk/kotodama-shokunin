# R30-O01..O03 — QREG dangling-record repair

- Date: 2026-10-18. Axis: operability; guardrails: calibration and append-only provenance.
- Scope: `R28-LAW-DANGLING-DESIGN-ROW-REFERENCES` only. No filed report from rounds 8–29 is rewritten.
- State: QREG packet repair landed and independently exercised with controls; whole-round regression integration remains blocked on the orchestrator-owned law tool/baseline landings. This is not a full-battery acceptance receipt.

## Chosen repair and integration dependency

Land the four previously proposed records QREG-05..QREG-08 as a new, marked amendment section in the existing `04-lexicon.yml` registers block. Preserve QREG-01..04 and all RGL rows. The new oath record must retain delivered RGL-02's refusal of binding stamp oaths; the historical round-27 proposal's positive `commissive-binding` wording is not a license to overturn that exclusion. New field declarations belong in an additive contract section. Rebuild packet, projection and typed packet; record the resulting pin generation as new history rows.

**Law-gate/selftest owner (live integration dependency):** the zero-finding packet invalidates `selftest()`'s current `delivered-packet-replays` check (`bool(base)`, `tools/gates/register-law-gate.py:483-485`). Assert successful evaluation/expected row coverage, not baseline findings. **All three delivered controls must also be scoped to `register_law`:** their global first-match regex now mutates the newly delivered QREG act records, which precede the RGL block and are not the gate's replay domain. The real current selftest is therefore **29/33**, with exactly `delivered-packet-replays` and the force/speaker/consequence tail red; synthetic controls remain green. Do not weaken this repair to preserve a saturated baseline. The gate docstring's four-dangle clean baseline is now historical. This seat does not edit the gate because the speaker-tamper seat owns those bytes. Preserve a dropped-register or bogus-design-row negative control so zero findings is not obtained by weakening the dangling resolver.

## Before measurement

At 2026-10-18T21:52:44Z:

```sh
export TMPDIR=$PWD/.scratch
python3 tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
python3 tools/assemble-culture-d4.py --check
sha256sum examples/culture-d4/components/04-lexicon.yml examples/culture-d4/components/13-register-law.yml examples/culture-d4/packet.d4.yml examples/culture-d4/typed-labels.d4.yml examples/culture-d4/packet.d4.typed.yml examples/culture-d4/expected-holds.json tools/gates/typed-pipelines.json
```

The law gate returned exit 1, four HOLD findings, all `D4L-LAW-DANGLING`: RGL-01 → QREG-05/QREG-07; RGL-02 → QREG-06; RGL-03 → QREG-08. Coverage: five law rows, four register records, 179 record IDs, `dangling=4`, `findings=4`, force/consequence failures zero. Deterministic assembly check returned exit 0.

| Artifact | Before SHA-256 |
|---|---|
| `examples/culture-d4/components/04-lexicon.yml` | `d0d4e17cc3c43a11e598259271fe16f18539c8bce3c3a30a40b6d2554b6c7240` |
| `examples/culture-d4/components/13-register-law.yml` | `c0d77181ac567c4c4625540579b784df1781a3585c7675e1c046fe6f7bcf50b7` |
| `examples/culture-d4/packet.d4.yml` | `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f` |
| `examples/culture-d4/typed-labels.d4.yml` | `339bfd83bf66832479b5b8ffbbce708c8be15e13b08967fa7049b848661a3cf8` |
| `examples/culture-d4/packet.d4.typed.yml` | `15c81ec11b42efaa7d683dd9320bfc7cd9b5d1e812e042d99dbf8d8726ec5da6` |
| `examples/culture-d4/expected-holds.json` | `65f5a03e092fb4bb1e04f26d73180ca411c1f91bd29d2f1912d275407e15e423` |
| `tools/gates/typed-pipelines.json` | `7f5a9c722a5ccca51f15b704368831381a428f1b977ad75c5b88aa85704a886a` |

## Landed amendment and calibration

`04-lexicon.yml` gains only the marked round-30 act-record section inside `registers`; `01-brief.yml` gains only `contract.record_fields_amendments`, declaring the five act fields for the four new records. No assembler, projector, adapter, phonology, lexical form, rank rule, prior register record, or RGL row is changed. An insertion-only line comparison against `git show HEAD:<component>` passes for both components. Parsing old and new packets also proves equality of every old packet block except the explicitly additive contract/register blocks and generated assembly pins; stripping `record_fields_amendments` restores the old contract exactly.

The law gate at **2026-10-18T21:53:54Z** returned **exit 0**, `law_rows=5 identity_rows=8 record_ids=183 registers=17 speaker_tokens=3 force_failures=0 consequence_failures=0 dangling=0 findings=0`. The pre-repair finding set was exactly four real dangles; the post-repair set is empty because the cited records now exist, not because a finding class was suppressed. The older six-finding design probe also counted two non-speech-act consequences; those were already scoped out of the shipped gate before this repair. This repair removes the actual shipped four-dangle baseline, not six findings and not any unrelated law limitation.

The added records are design-choice declarations, not a new replay domain or canon acceptance. RGL-01..05 remain the gate's replayed law. In particular, QREG-06's `commissive-binding refused` and void/no-entry consequence explicitly decline the historical positive oath proposal, preserving the delivered exclusion and the lexical ceiling (`gis` → illegal `sig`). QREG-07 cites OR-02 as a delivered record, not as the historically missing component-only record. No new vocabulary or speaker office is coined.

## Pin cascade: new generations, old rows preserved

- `tools/gates/typed-pipelines.json`: insert a new **first-match** `d4` generation (`round-30-qreg-records`) before the old profile. The entire former `profiles` list remains content-equivalent as the successor list's tail; no prior profile object is rewritten. First-match selection is the existing `load_profile()` contract.
- `examples/culture-d4/expected-holds.json`: append predecessor/successor `pin_generations` rows with commands, dates and evidence, retain every pre-existing historical note and hold row, and advance only the two current packet/projection scalar pointers. The predecessor row retains the former pointers and the full former-file digest `65f5a03e092fb4bb1e04f26d73180ca411c1f91bd29d2f1912d275407e15e423`; `active_pin_generation` selects the new row. `schema`, `counts`, `holds`, `notes`, `revision_note`, and `supersedes_pins` equal the former values exactly: **12 holds / 0 notes / 0 fails**, no added or retired form obligations.
- The conventional hold-file path is retained because `tools/exercise-handoff-e2e.py` directly mines and verifies it (`v3_mine_d4_holds`, `v3_verify_d4_pins`). An initial, unfiled successor-only `expected-holds.r30-qreg.json` approach passed the typed gate but would strand that reader; it was removed before delivery. The intermediate profile prefix `b42ebfaf9016` is an earlier measurement, not the final profile. The final profile prefix is `76ecdfdcbf09` and the wider v3 replay below is green. No handoff tool change or hidden bypass was needed.
- Packet, projection and typed packet are regenerated by their existing tools. `d2-typed-labels.py --emit` returns 1 when it emits the twelve expected design holds; the subsequent `--check` returns 0 and proves deterministic freshness. No filed freeze or round-8..29 artifact is rebuilt.

Measured with `sha256sum` on **2026-10-18**, final pin-file measurement at **21:59:59Z** and subsequent profile measurement:

| Artifact | After SHA-256 |
|---|---|
| `examples/culture-d4/components/01-brief.yml` | `a1e532ad05a9ee2bbc2f0a0cce56127338110942389630b1ace1918f7f2ade9e` |
| `examples/culture-d4/components/04-lexicon.yml` | `ed7093d6b92111c2300e7c04b9100f9e57f6d5802101b69335f9fe138858755d` |
| `examples/culture-d4/packet.d4.yml` | `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3` |
| `examples/culture-d4/typed-labels.d4.yml` | `c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e` |
| `examples/culture-d4/packet.d4.typed.yml` | `d581e0ad5384ce56622839b6ae4d6cf8b5a4447300cf7d8cd295f3efea0c9182` |
| `examples/culture-d4/expected-holds.json` | `e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3` |
| `tools/gates/typed-pipelines.json` | `76ecdfdcbf09c3c7f384d74cd81ddc5e57ef261a4be4267579081766fa8b986d` |

## Discriminating linkage controls

The real CLI controls below passed at **2026-10-18T21:55:57.718478+00:00**. Each fixture is a text transform, never a reserialization; selectors are anchored to the top-level block so the contract's own field declarations cannot be mistaken for the replay domain.

| Control | Command suffix after `python3 tools/gates/register-law-gate.py` | Exit / findings |
|---|---|---|
| Remove QREG-05 only | `.scratch/r30-qreg-controls/drop-QREG-05.yml` | 1 / exactly one dangling HOLD, RGL-01 → QREG-05 |
| Remove QREG-06 only | `.scratch/r30-qreg-controls/drop-QREG-06.yml` | 1 / exactly one dangling HOLD, RGL-02 → QREG-06 |
| Remove QREG-07 only | `.scratch/r30-qreg-controls/drop-QREG-07.yml` | 1 / exactly one dangling HOLD, RGL-01 → QREG-07 |
| Remove QREG-08 only | `.scratch/r30-qreg-controls/drop-QREG-08.yml` | 1 / exactly one dangling HOLD, RGL-03 → QREG-08 |
| Remove all four new records | `.scratch/r30-qreg-controls/drop-all-four.yml` | 1 / exactly the original four dangling HOLDs |
| Change RGL-02's design reference to QREG-99 | `.scratch/r30-qreg-controls/bogus-design-row.yml` | 1 / exactly one dangling HOLD, RGL-02 → QREG-99 |
| Restore delivered bytes | `.scratch/r30-qreg-controls/restored.yml` | 0 / zero findings |

Every nonzero control finding is `D4L-LAW-DANGLING: HOLD`; none adds a force/consequence finding. The deletion-all control reproduces the old **179** record IDs / **4** register rows / **4** findings, proving the new **183** record IDs / **8** register rows / **0** findings did not come from changing the resolver. Scratch receipt: `.scratch/r30-qreg-controls/results.json`; the dated results and reconstruction command are retained here so cleanup of scratch does not remove the evidence.

Reconstruction and assertion command (run on 2026-10-18):

```sh
export TMPDIR=$PWD/.scratch
python3 -B - <<'PY'
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import re, subprocess, sys
text = Path('examples/culture-d4/packet.d4.yml').read_text()
out = Path('.scratch/r30-qreg-controls'); out.mkdir(parents=True, exist_ok=True)
start = re.search(r'(?m)^registers:\n', text).start()
end = re.search(r'(?m)^pantheon:', text[start:]).start() + start
block = text[start:end]
def drop(value, rid):
    result, count = re.subn(r'(?ms)^  -\n    id: "' + rid + r'"\n.*?(?=^  -\n|\Z)', '', value, count=1)
    assert count == 1
    return result
ids = ['QREG-05', 'QREG-06', 'QREG-07', 'QREG-08']
cases = {'drop-' + rid: (text[:start] + drop(block, rid) + text[end:], 1) for rid in ids}
removed = block
for rid in ids: removed = drop(removed, rid)
cases['drop-all-four'] = (text[:start] + removed + text[end:], 4)
leg = re.search(r'(?m)^register_law:\n', text).start()
assert '      - "QREG-06"' in text[leg:]
cases['bogus-design-row'] = (text[:leg] + text[leg:].replace('      - "QREG-06"', '      - "QREG-99"', 1), 1)
cases['restored'] = (text, 0)
def run(item):
    label, (payload, count) = item
    target = out / (label + '.yml'); target.write_text(payload)
    p = subprocess.run([sys.executable, 'tools/gates/register-law-gate.py', str(target)], text=True, capture_output=True)
    findings = [line for line in p.stdout.splitlines() if line.startswith('FINDING ')]
    assert p.returncode == (1 if count else 0)
    assert len(findings) == count and all(line.startswith('FINDING D4L-LAW-DANGLING: HOLD') for line in findings)
    if label.startswith('drop-QREG-'): assert label[5:] in findings[0]
    if label == 'bogus-design-row': assert 'QREG-99' in findings[0]
    return label, p.returncode, findings
with ThreadPoolExecutor(max_workers=7) as pool:
    for result in pool.map(run, cases.items()): print(result)
PY
```

A separate pin control at **2026-10-18T21:56:16.670931+00:00** copies the profile in scratch, replaces only the active packet pin with 64 zeroes, then calls the existing `grading(packet, flags={'profile': <scratch profile>})` path via `runpy.run_path('tools/gates/typed-pipeline-gate.py')`. It returns **exit 2**, with exactly failed `L1-profile`: `packet: pins 000000000000, live aac91246cede`. The public CLI does not expose `--profile`; that unsupported option is not counted as a passing control. Both real clean CLI pipeline runs below use the new live first-match profile and pass.

## Regression measurements and remaining integration owners

Commands run on **2026-10-18**, with `export TMPDIR=$PWD/.scratch` first; temporary mirror-safety runs use `TMPDIR=/var/tmp` and remove their mirrors:

| Command | Result |
|---|---|
| `python3 tools/assemble-culture-d4.py --check` | exit 0, byte-identical |
| `python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml --check examples/culture-d4/typed-labels.d4.yml` | exit 0, byte-identical |
| `python3 tools/assemble-d4-typed.py --check` | exit 0, byte-identical |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | exit 0, **20/20** legs |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.typed.yml` | exit 0, **17/17** legs |
| `python3 tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml` | exit 0, records=187, register_scoped=14, derived_pairs=8, claimed_chains=8, borrow_pairs=6, violations=0, rule_holds=0 |
| `TMPDIR=/var/tmp python3 tools/assemble-culture-d4.py --selftest` | exit 0, **81/81** |
| `TMPDIR=/var/tmp python3 tools/assemble-d4-typed.py --selftest` | exit 0, **12/12** |
| `python3 tools/gates/typed-pipeline-gate.py --selftest-generalized` | exit 0, **16/16** |
| `python3 tools/gates/register-law-gate.py --selftest` | at 21:57:17Z, exit 1, **29/33**; exact four tail assumptions above remain owned by the gate/speaker-tamper seat |
| `python3 tools/check-gate-battery.py` | at 21:56:17Z, exit 2, structural **7/7** pass, baseline **9/10**, law baseline absent; owned by battery/baseline integration, not a new packet mismatch |
| `git diff --check` | exit 0 |
| `git diff --name-only -- 'reports/round-[89]/**' 'reports/round-1*/**' 'reports/round-2*/**'` | no filed report changes |

This fragment does **not** claim whole-round or full-battery acceptance while those separate-owner dependencies remain red. The repair's real clean CLI and seven linkage controls pass; the all-green regression requirement still needs (1) gate-tail scoping and a clean-coverage assertion, (2) a newly frozen law baseline for 10/10 coverage, and (3) the parent-owned round-30 validator. Do not edit the old freezes to satisfy those dependencies.

## Final compatibility replay and orchestrator handoff

On **2026-10-18**, after finalizing the conventional hold-file pointers, both commands returned exit 0:

```sh
export TMPDIR=$PWD/.scratch
TMPDIR=/var/tmp python3 tools/exercise-handoff-e2e.py --profile v3 --freeze "$PWD/.scratch/r30-qreg-v3"
TMPDIR=/var/tmp python3 tools/exercise-handoff-e2e.py --profile v3 --baseline "$PWD/.scratch/r30-qreg-v3/expected.json"
```

The delivered v3 replay reports **58/58** read-set digests, **26/26** component digests, **8/8** D4 tree pins, **16/16** fields, **20/20** glossary entries, **105/105** links, **27** claim rows and zero gate/semantic findings; preservation confirms all 58 read-set files unchanged. Packet SHA-256 `ec30b11f12accfa4c43e24a36e53fca858eddb07397d4bed715e938c693343f7`; twin SHA-256 `6633443d70ce44ed2bb43ab58aa60a1c98e4bbc79b2f577a63181c89dc16fd4e`; fresh scratch baseline SHA-256, measured by `sha256sum` at **22:01:26Z**, `6a461a81f7863ff9356f94252146821ddd8fa6c7e9cb341451300b92972abdd7`. This is a new scratch freeze/replay, not a claim that older frozen handoff prose was refreshed or that its reported historical claims are now current.

At **22:00:54Z**, all three deterministic checks above again returned exit 0 and `git diff --check` remained clean. At **22:01:05.150812+00:00**, the stale-profile control was rerun against the final profile and again returned exit 2 with exactly `L1-profile` failed. The exact reconstruction command embedded in this report was extracted and executed, returning **7/7** successful linkage controls.

Outstanding parent-owned work, not permission for this seat to edit other owners' files:

1. Land the tool candidate in `reports/round-30/fixes/speaker-tamper.md`. That report explicitly assigns `tools/gates/register-law-gate.py` landing to the orchestrator; polling the unmodified tool at 21:57:17Z and 21:59:06Z still returned 29/33. The supplied candidate already addresses both the empty clean baseline and all three law-block-scoped mutations. Freeze the law baseline only after those final tool bytes settle.
2. Refresh `reports/round-30/routed-resolution.json`'s QREG evidence path and limits. Its first draft cites the **removed, unfiled** `examples/culture-d4/expected-holds.r30-qreg.json`; the final evidence path is `examples/culture-d4/expected-holds.json`, with new history rows and SHA-256 `e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3`. Its claim that v3 still needs a successor hold path is superseded by the green compatibility replay here. The speaker report's intermediate `b42ebfaf9016` profile measurement is historical; do not treat it as the final profile.
3. The round-30 validator arrived during this seat's run. Use its read-only `--check` mode or the orchestrator's guarded publication path after the remaining landings. A QREG closure is narrower than all regression/claim acceptance.

## Read-only round-30 acceptance measurement

At **2026-10-18**, command `export TMPDIR=$PWD/.scratch; python3 reports/round-30/run-validation.py --check > "$PWD/.scratch/r30-qreg-validation-check.json"` returned exit 1 after the runner arrived. The JSON was measured at **22:03:55Z** by `sha256sum`: `156f15e74c8b612a6254033f4c8f42bad7a9304aeacdde5e0dfcb0e3fa2afe9b`.

- Independent `live_fix_controls`: **`qreg-dangles: true`, `dangling-control: true`**. The runner's clean law CLI returned exit 0 / zero finding lines; its separately generated QREG-99 law mutation fired correctly. Routed-resolution validation and protected-file preservation both passed.
- C passed. D remained pending the orchestrator-owned `SKILL.md` landing and post-landing box-1 receipt. This seat does not claim or alter those axes.
- O remained red for exactly three regression commands: `battery` (exit 2), `law-selftest` (exit 1), and default `handoff-v3` (exit 1). The last is distinct from the fresh-baseline compatibility replay above.
- To resolve the handoff ambiguity, `TMPDIR=/var/tmp python3 tools/exercise-handoff-e2e.py --profile v3` was run without quiet mode on **2026-10-18**. It returned exit 1 with **E2E-DIGEST: six read-set files changed**: the two amended components, packet, projection, typed packet, and expected-holds file. That is expected freeze drift from this amendment, not a semantic/shape failure; the explicit fresh-baseline replay passes all eight current D4 pins. **The orchestrator must land a new v3 baseline generation and route the standing regression to it; never rewrite the old freeze or suppress input-digest checks.**

The final full-battery/round acceptance is therefore **not complete**. Shared tool, battery baseline, default v3 baseline, and D-axis landings remain parent-owned; this seat has not edited those files. `reports/round-30/routed-resolution.json` was independently accepted during the check, but any remaining prose or path referring to the removed intermediate hold-file name should still be refreshed by its owner.

Files retained by this seat: `examples/culture-d4/components/01-brief.yml`, `examples/culture-d4/components/04-lexicon.yml`, `examples/culture-d4/packet.d4.yml`, `examples/culture-d4/typed-labels.d4.yml`, `examples/culture-d4/packet.d4.typed.yml`, `examples/culture-d4/expected-holds.json`, `tools/gates/typed-pipelines.json`, and this report. Scratch-only outputs are under `.scratch/r30-qreg-controls/`, `.scratch/r30-qreg-v3/`, and `.scratch/r30-qreg-validation-check.json`. No commit or push.
