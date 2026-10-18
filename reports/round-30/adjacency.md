# Round 30 — Adjacency / connector (SCRIBE X39)

- Date: 2026-10-18; timestamps are UTC. Axes: **O / operability**, **C / calibration**, **D / depth**, constrained by province ownership, immutable history, and independently discriminating evidence.
- Assigned write surface: this fragment only. Disposable CLI controls use auto-cleaned `.scratch/x39-speaker-*` under `TMPDIR="$PWD/.scratch"`; no source, shared bookkeeping, filed round-8–29 artifact, sibling repository, Git state, commit, or push is written by this seat. No historical round validator is run.
- Declared baseline: `87bfc9956f0fc60e6821fe53b622d0043e28be10` (`claims.json:5`); observed HEAD at the initial sample: `44145d5f337dea425c20dccafee98e0882678660`.
- State: **in-flight observations, not round acceptance**. Late dependencies are polled at 60-second intervals, bounded by 20 minutes. The orchestrator owns `SKILL.md` landing, final claim disposition, and the final integrated counting command.

## Boundary verdict and meaning of a green connector

The inspected register forms, law, knowledge entries, and handoff contract remain linguistic-cultural system/design work. The D4 law is explicitly NON-CANON, disclaims real institutions and rights decisions, and reserves canon/adoption to lore (`examples/culture-d4/components/13-register-law.yml:2-3,13-25,60-71`; `04-lexicon.yml:282-287`). The ceiling entry likewise distinguishes its measured design procedure from claims about real registers and reserves canon to lore (`corpus/knowledge/linguistics/register-lexicon-ceilings.md:240-248,274-289`). `PROVINCE.md:9-25` remains accurate on that slice. No province or contract edit is proposed.

The contract is not activated by an author-side gate. It still requires same-revision bilateral read records, leaves initial acknowledgement pending until they exist, and separates delivery, review, acceptance, and canon import (`corpus/knowledge/synthesis/worldbible-integration-contract.md:12-19,124-136`). No lore-side record or sibling tree is read or inferred here. No real-world rights, historical-truth, source-merit, screening, freshness-policy, or canon certification is made.

**Three different green readings must not be merged:** the typed pipeline's exit 0 means equality with a frozen hold set; the battery's `pinned` means snapshot digests/pins verify, not that baseline verdicts were replayed; the v3 handoff's author-side exit 0 is not lore acceptance. A law-leg finding can coexist with all three. The independent initial sample below demonstrates precisely that combination.

## Initial control: 2026-10-18T21:53:00Z–21:53:05Z

Every command ran from the lane root with `export TMPDIR="$PWD/.scratch" PYTHONDONTWRITEBYTECODE=1`.

- `python3 -B tools/check-gate-battery.py` — exit 0; duty-1 selftests **7 pass / 0 fail / 0 unevaluable**, coverage **9/9**, **19/19** baselines pinned, originals preserved. The law gate was not registered at this stamp. This is not a ten-gate pass or a verdict replay.
- `python3 -B tools/gates/register-law-gate.py --selftest` — exit 0, **33/33**; `python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` — exit **1**, **4** `D4L-LAW-DANGLING` HOLDs, for `RGL-01 → QREG-05/QREG-07`, `RGL-02 → QREG-06`, `RGL-03 → QREG-08`. Coverage: **5** law rows, **4** identity rows, **179** record IDs, **3** speaker tokens; force/consequence failures **0**.
- `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` — exit 0, **20/20** legs; **12** form holds remain, representing the paired garment/slot views of **6** owed forms, not cleared obligations.
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` — exit 0; fields **16/16**, glossary **20/20**, findings **0**, links **105/105**, claims **27**, statuses **16/7/4**, v2 subset equal; packet digest `a20ae059aa7cac9e28345d1a80a4dae3fa302117e26b5b1405f05b38d12f0001`.

The initial protected-surface command at **21:53:01.074546Z**, `python3 -B -` using `git ls-tree -r -z <baseline> -- reports/round-{8..29} tools/gates/frozen/round-{8..29}`, compared each observed Git blob and executable/symlink mode to its baseline. It measured **1,764 tracked paths**, **0 mismatches**, **0 missing**, and **0 protected status rows** (`git status --porcelain=v1 -uall -- <same roots>`). The sorted `path + NUL + sha256(bytes) + newline` manifest digest was `0f028072980cb1455cb92693b43488f8c62c5122e4a27d8314b100aaea3a4f0d`. An appended in-memory probe changed the calculated blob of `reports/round-8/claims.json` while its reread bytes stayed unchanged: a control for the detector, not a disk tamper. This is sampled preservation, not proof that no transient write occurred between samples or fleet-root cleanliness.

At the same stamp, `git show <baseline>:<path>` versus live bytes and `hashlib.sha256` confirmed baseline identity for `PROVINCE.md`, `AGENTS.md`, `SKILL.md`, `corpus/README.md`, the world-bible contract, the law component, packet, law gate, and battery. The profile's five named packet/assembler/projection/adapter/expected pins all matched live bytes. These observations predate round-30 source landings.

## Independent speaker-tail control: 2026-10-18T21:53:21.417385Z

The CLI control modifies only the first named field **inside the `register_law:` block**, not the first similarly named field anywhere in the packet. All copies retain a `culture-d4` parent directory to avoid the projector's documented filename-family fallback. Unmodified and tampered inputs are read by the actual CLI; the live packet is unchanged on reread.

Command: the Python reproducer below with `python3 -B -`, `TMPDIR="$PWD/.scratch"`. Bound bytes: gate SHA-256 `bbad35784bfb463d41912908748ebb711f72109d811d0dc8f0110657e3b4c026`; packet SHA-256 `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f`.

- Unmodified control: exit **1**, **4** findings.
- `speaker: no-such-speaker`: exit **1**, **4** findings, finding lines **identical** to the control.
- `holder: no-such-speaker`: exit **1**, **4** findings, finding lines **identical** to the control.
- `speaker: no-such-speaker (ZZ-99)`: exit **1**, **5** findings, adding exactly `D4L-LAW-SPEAKER` naming `RGL-01`, `speaker`, and `ZZ-99`.
- `force: no-such-force`: exit **1**, **5** findings, adding exactly `D4L-LAW-FORCE` naming `RGL-01` and the value.
- `consequence: the act evaporates silently`: exit **1**, **5** findings, adding exactly `D4L-LAW-CONSEQUENCE` naming `RGL-01` and the value.

This independently reproduces the routed tokenless tail and shows the resolver is not globally silent. It is the pre-fix reading, not a new unresolved defect if the later paired control closes it.

```sh
export TMPDIR="$PWD/.scratch" PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
import datetime, hashlib, json, pathlib, re, subprocess, sys, tempfile
root = pathlib.Path.cwd()
gate = root / 'tools/gates/register-law-gate.py'
packet = root / 'examples/culture-d4/packet.d4.yml'
text = packet.read_text()
header, law = text.split('\nregister_law:', 1)
print('AUDIT_UTC=' + datetime.datetime.now(datetime.timezone.utc).isoformat())
print('GATE_SHA256=' + hashlib.sha256(gate.read_bytes()).hexdigest())
print('PACKET_SHA256=' + hashlib.sha256(packet.read_bytes()).hexdigest())
with tempfile.TemporaryDirectory(prefix='x39-speaker-', dir=root / '.scratch') as tmp:
    parent = pathlib.Path(tmp) / 'culture-d4'
    parent.mkdir()
    variants = {'control': text}
    for name, field, value in (
        ('speaker-tokenless', 'speaker', 'no-such-speaker'),
        ('speaker-tokenized', 'speaker', 'no-such-speaker (ZZ-99)'),
        ('holder-tokenless', 'holder', 'no-such-speaker'),
        ('force', 'force', 'no-such-force'),
        ('consequence', 'consequence', 'the act evaporates silently'),
    ):
        new, n = re.subn(r'(?m)^(\s*)' + field + r':.*$',
                         lambda m: m.group(1) + field + ': ' + json.dumps(value),
                         law, count=1)
        assert n == 1, (name, n)
        variants[name] = header + '\nregister_law:' + new
    base = None
    for name, value in variants.items():
        path = parent / (name + '.yml')
        path.write_text(value)
        p = subprocess.run([sys.executable, '-B', str(gate), str(path)],
                           capture_output=True, text=True, cwd=root)
        findings = [line for line in p.stdout.splitlines() if line.startswith('FINDING ')]
        if name == 'control':
            base = findings
        print(json.dumps({'variant': name, 'exit': p.returncode,
                          'findings': len(findings), 'same_as_control': findings == base,
                          'added': sorted(set(findings) - set(base)),
                          'removed': sorted(set(base) - set(findings))}, ensure_ascii=False))
print('LIVE_PACKET_UNCHANGED=' + str(packet.read_text() == text))
PY
```

## Late-landing watch and integration route

At **2026-10-18T21:54:21.671218Z**, the first 60-second poll (`sleep 60; python3 -B -`, enumerating `reports/round-30`, hashing the named connector surfaces, and checking product paths) observed the QREG packet and battery changes plus the new durable telemetry directory. `SKILL.md` still matched the initial digest. The aggregate routed ledger, consolidated retrospective, round-30 runner, and validation receipt were not yet present. This is an in-flight dependency observation, not rejection.

- QREG owner: `fixes/qreg-dangles.md` explicitly requires a zero-finding gate without weakening the dangling control. Its warning that `delivered-packet-replays` must stop requiring nonempty findings is load-bearing.
- Battery owner: `fixes/battery-registration.md` explicitly separates duty-2 registration from duty-1 execution and routes the missing final gate/packet baseline to integration. Registration alone must not be reported as **10/10** coverage.
- X63-F2: `fixes/x63-f2.md` is an append-only successor withdrawing the baseline-false phrase sweep, not a rewrite of the original corpus line. The historical auditor's finding-bearing result must not be laundered into a green unamended audit. Its author-side controls are reported by that fragment; an independent bounded check follows below if performed.
- Telemetry: `AGENTS.md:15-31` now requires durable raw samples/extracts, observation windows, commands/dates/digests, explicit unknown counters, and no private payloads. `telemetry/worker-observation.json` labels its source as one worker's own active-state observation, not native full-wave results. Requesting 32 workers is not observing 32 launches, completions, concurrent workers, or the actual model route.
- Register craft landing and post-landing box-1 survey are orchestrator-owned. A draft or a pre-landing survey does not close D. A freshness recommendation does not enact an operator threshold, and a retrospective must not count rounds 31–32 as completed at this round-30 evidence cut.

Further measurements and the final bounded handoff will be added as new sections below; no initial reading is silently replaced.

## Post-QREG connector control: 2026-10-18T21:56:24Z–21:57:57Z

The second and third 60-second polls (`sleep 60; python3 -B -` with the same existence/hash census) at **21:56:13.262162Z** and **21:57:37.518326Z** observed the consolidated retrospective, synthesis draft/reviews, runner and first receipt land. The routed ledger was still absent, `SKILL.md` remained byte-unlanded, and the speaker fix was a documented in-memory candidate rather than a delivered gate edit. These are not unknown authorship claims: `fixes/speaker-tamper.md:4-5,24-35,300-310` explicitly reserves landing to the orchestrator.

Actual CLI rechecks, all on **2026-10-18** with `TMPDIR="$PWD/.scratch"`:

- **21:56:24.070986Z:** `python3 -B tools/gates/register-law-gate.py --selftest` → exit **1**, **29/33**. The clean replay's `bool(base)` and broad first-field replacements are invalidated by genuinely clean QREG records occurring before `register_law`; do not restore dangles to make this selftest pass.
- **21:56:24.142487Z:** `python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` → exit **0**, **0** findings, **5** law rows, **8** identity rows, **183** record IDs, **17** register names/IDs/titles, **0** dangling. Those last two counters are resolver-set sizes, not 17 distinct registers or 183 linguistic forms.
- **21:56:24.180601Z:** `python3 -B tools/check-gate-battery.py` → exit **2**, structural selftests **7/7**, coverage **9/10**, baselines **19/19** pinned, originals preserved; the sole uncovered gate is `register-law-gate.py`. Registering the gate successfully exposed missing evidence rather than laundering it.
- **21:56:24.600424Z:** `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → exit **0**, **20/20**, retaining the unchanged **12** form holds. It now selects the new `examples/culture-d4/expected-holds.r30-qreg.json` through the updated profile, not the historical `expected-holds.json`.
- **21:56:25.164907Z:** `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit **1**, packet not assembled. The same command was green at the initial control: the source landing has exposed a real downstream integration obligation.

### QREG repair is discriminating, tokenless speaker is not yet delivered

At **21:57:56.435846Z**, an independent `python3 -B -` CLI batch bound gate `bbad35784bfb463d41912908748ebb711f72109d811d0dc8f0110657e3b4c026` and packet `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`. It reused the law-block control above and additionally parsed every candidate with the naming loader, asserting that its entire mapping differed only in the intended field. All copies were auto-cleaned; live packet reread was unchanged.

- Control → exit **0**, **0** findings; IDs `QREG-01` through `QREG-08` are delivered **register record IDs**, not accidental citations.
- Tokenless `speaker` and tokenless `holder` separately → exit **0**, **0** findings, identical to control. The routed tail therefore remains unlanded at this stamp.
- Tokenized speaker, force, and consequence separately → exit **1**, exactly **1** added finding of their respective classes and no removed finding.
- **Negative dangling control:** inside the parsed `registers:` block, change only the record ID `QREG-05` to `QREG-99`, leaving every law reference untouched. The loader's whole-mapping equality check confirms that sole mutation. CLI → exit **1**, exactly **1** `D4L-LAW-DANGLING` HOLD: `RGL-01 design_row names QREG-05`. This proves the zero-finding QREG repair did not disable the dangling resolver.

The new QREG wording also preserves the existing law's oath exclusion and guest asymmetry (`examples/culture-d4/components/04-lexicon.yml:255-260`). `QREG-06` says `commissive-binding refused` and keeps the binding oath in plain speech; `QREG-08` records the guest act under a stamp-name without granting furnace-roll access. They do not silently adopt the round-27 proposed positive oath or expand this lane into canon/rights adjudication.

### V3 requires the new hold path, not merely a successor packet baseline

At **21:57:56.864721Z**, `python3 -B tools/exercise-handoff-e2e.py --profile v3 --json` returned exit **1**, `E2E-DIGEST`: historical `examples/culture-d4/expected-holds.json` pins packet `543d68a82640…` while live bytes measure `aac91246cede…`. At **21:57:56.971008Z**, the actual `--profile v3 --selftest` returned exit **1** with the same `Failed` exception. The tool's constant `D4_HOLDS` still points to the old filename (`tools/exercise-handoff-e2e.py:150,2187,2245-2247`); typed-profile selection alone does not re-point this consumer. Route to the authorized handoff/tool integrator: honor the new expected-file generation, then add a new v3 baseline/claim-map record and rerun. Do not overwrite the preserved old expected file or old baseline to hide the mismatch.

Instrument note: my first attempt to parse the whole `--json` stdout as JSON failed (`JSONDecodeError`) because this CLI prints human diagnostics before the JSON document on this failure path. It produced no measurement. The corrected capture above records the actual exit, full diagnostic and trailing document without assuming a one-document stdout contract.

## Independent X63-F2 check: 2026-10-18T21:55:13.224147Z

Command: `python3 -B -` invoking `git show <round-28-baseline>:<sound-symbolism/strata-path>` and `git show <round-30-baseline>:<ceilings-path>`, scanning the literal case-insensitive phrase, and checking the operative successor line in `fixes/x63-f2.md`. All **4/4** bounded assertions passed: the baseline hit at `sound-symbolism.md:106` rejects the original zero-hit claim; that line is explicitly about ideophones; the original ceilings entry remains byte-identical to the round-30 baseline; the new successor names the baseline/locator/sense and withdraws the phrase as gap evidence. The strata match is absent at round-28 baseline and present at current line 399. This supports **an append-only evidence correction**, not a new proof of the substantive ceiling or a green historical auditor.

The same dated command verified that `PROVINCE.md` and the world-bible contract remain baseline-identical, SHA-256 `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` and `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` respectively.

## Craft and telemetry adjacency review

`craft/skill-draft.md` keeps the useful boundary distinctions: a form derivation does not prove institutional semantics, a ceiling does not make the missing concept inexpressible, the tokenless case is separate from an ID-bearing speaker, ROOT-relative frozen replay is not automatically isolated, and prepared handoff is not lore acceptance. Its appended helpers are explicitly supporting executable surfaces, not new culture-clearance gates. No out-of-province material or province expansion was found in this draft slice. This is a draft-boundary result, not a post-landing or every-citation audit.

`craft/review-D29-box1.md:28-34,84-100` correctly labels its insertion as virtual and declines promotion closure. The parent must still land the actual subsection and obtain a survey pinned to the final `SKILL.md` digest. The old dossier's other conditions are not closed merely by naming executables.

The durable `telemetry/dispatch-stats.json` observed at **21:56:24Z** declares `full_wave_status: could-not-evaluate`, pins its request/allocation/self-observation sources, keeps actual launches/completions/route/concurrency/HTTP counters null, and assigns their evidence to the orchestrator. That is a durability improvement, not a provider-availability result or proof that the requested model served the wave. No telemetry/source payload is copied into this report.

## Later integration supersedes the alternate-hold-path reading

**Read this section before acting on the earlier in-flight v3 route.** By the stable source sample at **2026-10-18T22:02:09Z**, the QREG owner had replaced the unfiled alternate-hold-file experiment with history rows in the conventional `examples/culture-d4/expected-holds.json`. The temporary `expected-holds.r30-qreg.json` named in the earlier measurements no longer exists. The original conventional-path file's historical content is preserved as data/rows, not as unchanged current scalar pointers. This is distinct from rewriting a filed freeze.

At **22:02:39.808022Z**, command `python3 -B -` parsed `git show 87bfc9956f0fc60e6821fe53b622d0043e28be10:examples/culture-d4/expected-holds.json` and the live file. Every old key except the two active packet/projection pointers was unchanged: `schema`, `projector_sha256`, `revision_note`, `supersedes_pins`, `counts`, `holds`, and `notes`; no unexpected old-key change was found. The new keys are `active_pin_generation` and `pin_generations`, and the old full-file digest is carried in the new history. Thus the twelve form holds and historical notes survive the re-pin. The new first-match profile also preserves the previous profiles as later objects (`fixes/qreg-dangles.md:44-49`).

**The v3 failure has changed cause:** at **22:02:19Z**, `python3 -B tools/exercise-handoff-e2e.py --profile v3` returned exit **1**, now naming **6** input digests changed relative to the old round-28 default baseline, not a stale current hold pointer. The changed paths were the brief, lexicon, expected holds, typed packet, source packet, and projection. Do not keep diagnosing the earlier pointer error after this repair.

The proper paired compatibility control is green: at **22:02:39Z**, command

```sh
export TMPDIR="$PWD/.scratch" PYTHONDONTWRITEBYTECODE=1
TMPDIR=/var/tmp python3 -B tools/exercise-handoff-e2e.py --profile v3 \
  --baseline "$PWD/.scratch/r30-qreg-v3/expected.json" --quiet
```

returned exit **0**, fields **16/16**, glossary **20/20**, findings **0**, links **105/105**, claims **27**, statuses **16/7/4**, v2 subset equal, packet SHA-256 `ec30b11f12accfa4c43e24a36e53fca858eddb07397d4bed715e938c693343f7`. This seat only replayed the QREG owner's new scratch baseline; it did not freeze or alter it. The control proves compatibility on a new generation, not durable delivery of that baseline and not reproduction of the old default baseline. The integration owner should land an authorized durable successor and select it explicitly in current regressions; the scratch path is not a final receipt surface.

An attempted source-hash batch at **22:01:59Z** stopped before launching any command when the experimental alternate file had disappeared. It produced no gate measurement. The corrected **22:02:09Z** batch records absent optional paths as null and checks before/after hashes; its source set was unchanged during that batch.

## Runner controls: historical instrument error is already repaired

The first filed `validation.json` (measurement **2026-10-18T21:56:22Z**, runner SHA-256 `df6cca3edb4f3d5b41751a06e80e27a7faad34d812dd21527e3afd95d2e0fa3c`) reported `law-control-dangling` exit **2**, `D4L-LAW-DATA`, unexpected indentation. That was the mutation helper replacing only the `design_row:` key line while retaining its multiline list values, not a failure of dangling-record detection. This seat read the control's exact receipt at **21:58:27.697842Z** and independently had already demonstrated a valid scalar record-removal control above.

The owner repaired the helper while this watch was active. At **21:59:47.028073Z**, command `python3 -B -` loaded current `mutate_law()` from runner `ef7a5478355fb13ecd869f91f6af298e6933c1244f2d4c2f35c7b02f1b801bc3` and compared its output with an independently constructed whole-value replacement. The clean CLI returned exit **0**, zero findings; both valid `RGL-01 design_row: [QREG-99]` mutations returned exit **1**, exactly one `D4L-LAW-DANGLING` HOLD naming QREG-99. The independent mutation was parsed and asserted equal to the original mapping except for that one list value. This instrument issue is **closed on the measured runner revision**, not another pending source defect to fix.

## Read-only integrated check: explicitly not a settled-tree verdict

Command `python3 -B reports/round-30/run-validation.py --check` ran **2026-10-18T22:00:01.307397Z–22:00:41.908662Z** and returned exit **1**. It did not publish `validation.json`. The runner changed from SHA-256 `ef7a5478355fb13ecd869f91f6af298e6933c1244f2d4c2f35c7b02f1b801bc3` to `a0f453fc982647e3ee50080b42655179094ebb25bf5a76f4b7465106197c4c53` during the run; its own coherence check named that change and a changing C24 audit. Its O/C/D false readings therefore describe an **in-flight, incoherent input cut**, not final round adjudication.

Within that dated invocation, the fixed inventory executed **30** regressions: **25** exited 0; **5** did not (battery, typed D4 source, typed D4 typed input, law selftest, and default-baseline v3). The other law negative controls passed, including the repaired dangling fixture; tokenless speaker remained silent. It also named the removed alternate expected-file reference in the QREG disposition, insufficient current-document-hash-bound retrospective reviews, the absent landed skill subsection, and absence of a final-skill-hash box-1 survey. The subsequent direct typed-D4 run below is green on stable bytes, so the two earlier typed-input refusals must not be quoted as the settled final profile state.

## Final bounded handoff: 2026-10-18T22:03:43Z

The final 60-second poll at **22:03:43.552344Z** (`sleep 60; python3 -B -`, hashing the four named skill/law/battery/handoff surfaces) still found the original skill and law gate. No claim is made that parent-owned landings can complete before the parent receives this handoff.

A concurrent real-CLI batch at **22:02:09.661431Z–22:02:13Z**, command `python3 -B -` using a six-worker `ThreadPoolExecutor` over the exact commands below with `TMPDIR="$PWD/.scratch"`, measured:

| Command after `python3 -B` | Exit | Observed reading |
|---|---:|---|
| `tools/check-gate-battery.py` | 2 | structural 7/7, default-root coverage 9/10, 19/19 pins, only law uncovered, originals preserved |
| `tools/check-gate-battery.py --selftest` | 0 | 44/44 controls |
| `tools/gates/register-law-gate.py --selftest` | 1 | 29/33, old delivered tail assumptions remain red |
| `tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` | 0 | 5 law rows, 8 identity rows, 0 findings/dangles |
| `tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | 0 | 20/20; unchanged form debt |
| `tools/exercise-handoff-e2e.py --profile v3 --quiet` | 1 | old default baseline drift; successor control above is green |

The named source hashes were identical before/after that batch. New observation rows from that command/date, not replacements for historical pins:

| Surface | SHA-256 at 22:02:09Z |
|---|---|
| `SKILL.md` | `2d85bfea6e6a7503b4267b84fda5f393ed14e1a3f5eae108940e7fad8adb6048` |
| `tools/gates/register-law-gate.py` | `bbad35784bfb463d41912908748ebb711f72109d811d0dc8f0110657e3b4c026` |
| `tools/gates/typed-pipelines.json` | `76ecdfdcbf09c3c7f384d74cd81ddc5e57ef261a4be4267579081766fa8b986d` |
| `examples/culture-d4/packet.d4.yml` | `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3` |
| `examples/culture-d4/expected-holds.json` | `e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3` |
| `tools/exercise-handoff-e2e.py` | `96f963d705565ddc3f87a42eb62bd05984ac4a1db92182a092c6c86d72be2256` |

At **22:01:59.650812Z**, the protected blob/mode census from the initial section was repeated with `python3 -B -`, `git ls-tree -r -z <baseline> -- <report/frozen roots for rounds 8–29>`, and `git status --porcelain=v1 -uall -- <same roots>`. It again found **1,764** tracked paths, **0** missing, **0** mismatches, **0** protected status rows, and the identical manifest digest `0f028072980cb1455cb92693b43488f8c62c5122e4a27d8314b100aaea3a4f0d`. This preserves the bounded history verdict while live source integration moves.

**Parent integration route, not independent acceptance:**

1. Land the closed-clause speaker/holder candidate and law-block-scoped selftest from `fixes/speaker-tamper.md`; replay clean, tokenless and ID-bearing controls on the delivered gate.
2. Freeze a **new** law baseline under a default battery root against those final gate/packet bytes; require 10/10 coverage separately from the seven structural selftests.
3. Preserve/select a durable successor v3 baseline. Retain the old default's historical drift reading; do not leave current evidence only under scratch.
4. Correct the routed ledger's stale alternate expected-file reference and refresh its limits/controls after the conventional-path re-pin. The ledger was read as three fixed-with-control and two explicitly documented owner/reason rows at this cut, not five verified fixes or green regressions.
5. Land the unified Register craft subsection and acquire the post-landing box-1 survey pinned to the exact final skill digest; refresh retrospective reviews against their exact final document. Neither the draft nor a freshness recommendation is a promotion or operator-policy decision.
6. Re-run the declared round-30 counting command after all writers settle. This seat's in-flight --check is not the final receipt and cannot support admission.

**Scoped result:** no out-of-province expansion or canon/rights laundering found on the reviewed connector and draft surfaces; protected history stayed byte/mode-clean at the dated samples. QREG and amendment controls are discriminating, telemetry is durably but honestly partial, and the remaining delivery dependencies are explicitly routed. Whole-round O/C/D acceptance, final regression greenness, skill landing, and promotion remain unclaimed.

FILES: reports/round-30/adjacency.md | SUMMARY: X39 scoped adjacency pass with dated connector controls; QREG closure verified, historical/updated v3 readings separated, and final gate, battery baseline, durable handoff, skill, audit and settled-run integration remain parent-owned.
