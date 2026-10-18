# R30-D27 — law, speech-act and ceiling composition review

- Date: 2026-10-18. Axes: depth, bounded calibration, discriminating controls.
- Supporting review of `reports/round-30/craft/skill-draft.md`; this seat authors the draft and therefore does not claim non-author promotion verification.
- Scope: this fragment only. Law-gate, QREG data, pin generations and battery registration remain with their assigned owners.

## What is unified, and what is deliberately not collapsed

| Distinction kept in the draft | Primary evidence | Rejection/control |
|---|---|---|
| Register identity/stratum versus law over acts | `corpus/knowledge/linguistics/register-strata-attestation.md` §§1,4.1; `reports/round-27/law/design.md` §§1–3 | Landing QREG identity rows does not supply speaker, force or consequence. A law can be present, unread, unregistered or unenforced; these are separate states |
| Six-condition design walk versus the delivered replay's actual resolution scope | `corpus/knowledge/linguistics/register-strata-attestation.md` §§2–4,8; `tools/gates/register-law-gate.py` evaluate_packet | Venue, uptake, institutional legitimacy and record transactions are not simulated by string/record checks; the draft never claims they are |
| Misfire versus abuse | `corpus/knowledge/linguistics/register-strata-attestation.md` §§2–3,10 RSA-3 | Void/not-performed is not performed-but-sanctionable; the penalty and record result must be stated independently |
| Speech authority versus costume entitlement | `reports/round-27/law/design.md` §§4–5; `reports/round-28/law/impl-1.md` §§1–2 | Widening a costume-kind guard without a speech target can silently yield `not-applies`; link the authorizing row rather than merging ledgers |
| Historical proposed QREG acts versus the landed RGL law | `reports/round-27/law/design.md` §3; `examples/culture-d4/components/13-register-law.yml` RGL-01..03 | Do not reintroduce the proposed positive stamp-oath force over RGL-02's refusal. RGL-03 explicitly enters a guest act under a stamp-name while withholding furnace-roll access; “not-rollable” must not be paraphrased as no record anywhere |
| Early all-HOLD design versus executable severities | `reports/round-28/law/design.md` §2; `tools/gates/register-law-gate.py` Finding ids | Current FORCE/SPEAKER/CONSEQUENCE/REGISTER/AXIS violations are FAIL, while missing/dangling/kind/coverage rows are HOLD; the draft retains emitted severity rather than propagating the old design wording |
| Semantic ceiling versus inability to perform any act | `corpus/knowledge/linguistics/register-lexicon-ceilings.md` §§4–5,10; `reports/round-28/argot/D20-ceiling-wording.md` §§3–4 | `gis → sig` is illegal under the selected operation; it does not prove that a paraphrase, alternative base or separate record channel cannot carry the obligation |

## Dated pre-integration law reading

At **2026-10-18T21:53:04Z**, the following source-packet commands were run with
`export TMPDIR=$PWD/.scratch`:

```sh
python3 -B tools/gates/register-law-gate.py --selftest
python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml
python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml
```

- Law selftest: exit 0, **33/33**. This is capability evidence, not a clean-law result.
- Law packet: exit **1**, **four** D4L-LAW-DANGLING HOLDs, mapping RGL-01→QREG-05/QREG-07, RGL-02→QREG-06, RGL-03→QREG-08. Five law rows, four register records, 179 delivered record IDs; force/consequence failures zero.
- Typed pipeline: exit 0, **20/20** legs, twelve owed-form HOLDs retained. A green typed pipeline and a finding-bearing standalone law run coexist; neither result substitutes for the other.
- Inputs were stable during that batch. Packet SHA-256 `543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f`; law gate SHA-256 `bbad35784bfb463d41912908748ebb711f72109d811d0dc8f0110657e3b4c026`.

At **2026-10-18T21:53:41Z**, in-memory single-field mutations of the same parsed
packet through `evaluate_packet` independently confirmed:

| Mutation of RGL-01 | Added finding / result | Scope |
|---|---|---|
| `force: no-such-force` | +1 D4L-LAW-FORCE FAIL | force-value control |
| `speaker: nobody-nowhere (ZZ-99)` | +1 D4L-LAW-SPEAKER FAIL | unresolved record-token control |
| `speaker: nobody-nowhere` | no added line; identical finding set | the tokenless tail is **not** proved by the token-bearing control |
| `consequence: the act evaporates silently` | +1 D4L-LAW-CONSEQUENCE FAIL | binding-act consequence control |

### Reproduce the differential without touching a packet

```sh
export TMPDIR=$PWD/.scratch
python3 -B - <<'PY'
import copy, hashlib, json, runpy
from datetime import datetime, timezone
from pathlib import Path
g = runpy.run_path('tools/gates/register-law-gate.py')
p = Path('examples/culture-d4/packet.d4.yml')
raw = p.read_bytes()
d = g['load_naming']()['load_yaml'](raw.decode())
sig = lambda f: {(r['id'], r['message']) for r in f}
base, _ = g['evaluate_packet'](d)
rows = []
for field, value in [('force', 'no-such-force'),
                     ('speaker', 'nobody-nowhere (ZZ-99)'),
                     ('speaker', 'nobody-nowhere'),
                     ('consequence', 'the act evaporates silently')]:
    q = copy.deepcopy(d)
    q['register_law'][0][field] = value
    f, _ = g['evaluate_packet'](q)
    rows.append({'field': field, 'value': value,
                 'added': sorted(sig(f) - sig(base)),
                 'same_finding_set': sig(f) == sig(base)})
print(json.dumps({'date': datetime.now(timezone.utc).isoformat(),
    'packet_sha256': hashlib.sha256(raw).hexdigest(),
    'gate_sha256': hashlib.sha256(Path('tools/gates/register-law-gate.py').read_bytes()).hexdigest(),
    'baseline_findings': len(base), 'controls': rows,
    'input_preserved': raw == p.read_bytes()}, indent=2))
PY
```

The current result of this command may properly improve after the assigned
speaker-tail repair. That is a **new reading**, not grounds to rewrite the
pre-integration observation above. The draft states the paired-control
requirement rather than freezing the old blindness into a rule.

## Integration dependencies, not claimed closed here

- `reports/round-30/fixes/qreg-dangles.md` chooses actual QREG-05..08 records, preserving the delivered oath refusal. A zero-finding successor also requires the law selftest to stop treating `bool(base)` as a success condition and to scope mutations to `register_law`, not earlier QREG act fields. The data owner explicitly routes those gate bytes to the speaker-tail owner.
- `reports/round-30/fixes/battery-registration.md` separates registered-gate coverage from seven structural selftests. A law baseline must bind the final gate bytes and final packet generation; the draft does not pre-announce 10/10 coverage or green regressions.
- The draft's law-row caveats remain truthful after the dangles close: structural references, force substrings and consequence stems are not a complete semantics/authority checker. Broader routes in `reports/round-29/defects/routed.md` are not all closed by the narrow speaker-tail or QREG fixes.
- Parent/orchestrator must re-run the final direct law command and selftest after all owners settle. This review is not the round-30 routed-resolution or acceptance receipt.

## New QREG-generation reading, not a whole-round closure

At **2026-10-18T21:56:24Z**, a read-only before/after hash-stable batch ran
`python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml`
and `python3 -B tools/gates/register-law-gate.py --selftest`, with
`export TMPDIR=$PWD/.scratch`. The successor packet SHA-256 was
`aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`;
the law gate was still `bbad35784bfb463d41912908748ebb711f72109d811d0dc8f0110657e3b4c026`.
The packet run now exits **0**, `law_rows=5 identity_rows=8 record_ids=183
dangling=0 findings=0`: actual QREG records discharge the old dangles.
The selftest exits **1**, **29/33**, because its historical nonempty-baseline
condition and broad field mutations remain in the unamended executable.
Do not report that partial integration as regressions green.

The exact in-memory differential command printed above was replayed at
**2026-10-18T21:57:14Z**, exit **0**. It confirms the new zero-finding clean
baseline, the same three discriminating force/token-bearing-speaker/consequence
mutations, and the still-inert tokenless speaker on these gate bytes.
`reports/round-30/fixes/speaker-tamper.md` supplies a verified **candidate**,
explicitly not a delivered edit; the orchestrator must land it and replay the
real CLI before claiming the tail fixed.
