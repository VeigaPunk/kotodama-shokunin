# R30-D26 — stratum synthesis review

- Date: 2026-10-18. Axes: depth, calibration, executable discoverability.
- Assigned deliverable: `reports/round-30/craft/skill-draft.md`, stratum discipline and ceiling treatment; this review is supporting evidence, not independent promotion verification.
- Draft integration: insert the complete `### Register craft` subsection after *Family-clean projection* and before `## Error patterns`. Keep all five existing sections; the new text composes their invariants rather than replacing their historical receipts.
- Scope: no SKILL.md, component, gate, pin, shared bookkeeping or filed round-8–29 artifact written by this seat. The orchestrator owns landing and LOG integration.

## What the subsection takes from the stratum

| Draft rule | Evidence read | Control / qualification |
|---|---|---|
| Select the operation from the delivered base's axis: mark → reverse, fire → lengthen | `reports/round-26/register/rules.md` §2; `examples/culture-d4/components/04-lexicon.yml` QREG-03 and L-55..L-62 | Independently resolve each `doublet_of` and `derived_from`, recompute reversal/first-vowel duplication, compare selected and delivered operation; do not claim `argot-derivation-gate.py` itself enforces the selector |
| A computed reversal and a pattern/output rule are different replay surfaces | `reports/round-26/register/rules.md` §§3.1–3.2; `reports/round-26/register/impl.md` §4.2; `tools/gates/argot-derivation-gate.py` OP_FUNCTIONS/replay_rule | The delivered id is lowercase `lengthen`, not the uppercase design spelling; no attempt is made to encode arbitrary character reversal through an indexed format template |
| Equality of derived bytes is not legality, base identity, type or era completeness | `tools/gates/argot-derivation-gate.py` evaluate_packet; `reports/round-29/defects/routed.md` register-stratum routes | Mutating L-56 `kit` to `kat` produces D4L-ARGOT-DERIV; the positive supplied forms replay. Missing-base, half-pair, typing and era limitations are named, not declared closed |
| Measure the operation's semantic ceiling with a per-syllable predicate | `corpus/knowledge/linguistics/register-strata-attestation.md` §13; `corpus/knowledge/linguistics/register-lexicon-ceilings.md` §§3–5,10 | Existing instrument selftest has a legal `sem.kit` and illegal `sig` control; use `all(is_legal_syllable(s) for s in syllabify(form))`, not one whole-word call |
| Choose a disposition and retain its price | `corpus/knowledge/linguistics/register-lexicon-ceilings.md` §5; `reports/round-28/argot/D20-ceiling-wording.md` §§3–4 | Distinguish mechanical derivation, hand-picked bases and accepted ceiling; a missing derived noun does not prove that paraphrase cannot express the concept |

## Dated live checks

Read-only batch at **2026-10-18T21:53:04Z**, packet SHA-256
`543d68a82640e1b0c53b9cb7cb26c4dc60fce5878c2bf487050ead3af0945c4f`,
argot gate SHA-256
`b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb`.
The batch compared those inputs before and after; they were stable during that batch.

```sh
export TMPDIR=$PWD/.scratch
python3 -B tools/gates/argot-derivation-gate.py --selftest
python3 -B tools/gates/argot-derivation-gate.py examples/culture-d4/packet.d4.yml
python3 -B reports/round-28/ceiling/measure-ceiling.py --selftest
python3 -B reports/round-28/ceiling/measure-ceiling.py
```

Results, all exit 0: argot selftest **27/27**; delivered packet
`records=183 register_scoped=14 derived_pairs=8 claimed_chains=8 borrow_pairs=6 violations=0 rule_holds=0`;
ceiling selftest **10/10**; **27** mark-axis plain words, **19 legal / 8 illegal**,
abstractions **1 legal / 4 illegal**, base-initial-coda mechanism **27/27**.
The pre-fix reconstruction gives **18/9**, with `L-45` the moving row. These are
counts of that command on that tree, not a universal statement about registers.

At **2026-10-18T21:53:41Z**, the independent in-memory check below also found:
L-56 tik→kit and L-57 mol→lom use reverse; L-55 tum→tuum, L-58 nes→nees,
L-59 hum→huum, L-60 mes→mees, L-61 rek→reek and L-62 sam→saam use lengthen.
All supplied rows agree with their resolved base axis and `doublet_of`, recompute
exactly and have legal syllables. L-56 kit→kat adds one D4L-ARGOT-DERIV FAIL;
the original parsed packet is not mutated.

### Reproduce the independent pairing control

```sh
export TMPDIR=$PWD/.scratch
python3 -B - <<'PY'
import copy, hashlib, json, re, runpy
from datetime import datetime, timezone
from pathlib import Path
g = runpy.run_path('tools/gates/argot-derivation-gate.py')
n = g['load_naming']()
p = Path('examples/culture-d4/packet.d4.yml')
raw = p.read_bytes()
d = n['load_yaml'](raw.decode())
byterm = {r['term']: r for r in d['lexicon']}
selector = {'mark': 'reverse', 'fire': 'lengthen'}
checks, rows = {}, []
for r in d['lexicon']:
    if r.get('register') != 'stamp':
        continue
    b = byterm[r['derived_from']]
    op = r['derivation']['op']
    value = b['term'][::-1] if op == 'reverse' else re.sub(
        r'^([^aeiou]*)([aeiou])(.*)$', r'\1\2\2\3', b['term'])
    checks[r['id']] = (r['doublet_of'] == b['id'] and
        selector[b['axis']] == op and value == r['term'] and
        all(g['is_legal_syllable'](s) for s in g['syllabify'](r['term'])))
    rows.append([r['id'], b['id'], b['axis'], op, value, checks[r['id']]])
clean, _, _ = g['evaluate_packet'](d, n)
bad = copy.deepcopy(d)
next(r for r in bad['lexicon'] if r['id'] == 'L-56')['term'] = 'kat'
f, _, _ = g['evaluate_packet'](bad, n)
checks['negative_kit_to_kat'] = (not clean and any(
    x['id'] == 'D4L-ARGOT-DERIV' and 'L-56' in x['message'] for x in f))
checks['input_preserved'] = raw == p.read_bytes()
print(json.dumps({'date': datetime.now(timezone.utc).isoformat(),
    'packet_sha256': hashlib.sha256(raw).hexdigest(), 'rows': rows,
    'checks': checks, 'passed': sum(checks.values()), 'total': len(checks)}, indent=2))
assert all(checks.values())
PY
```

## Remaining boundaries

- The draft cites moving component blocks by record/symbol, not stale line numbers.
- Existing register-era, diphthong, base-resolution and prose-operation-detector routes are not secretly repaired by documentation. See `reports/round-29/defects/routed.md`.
- X63-F2 is an evidence-sweep defect, not a reason to discard the measured ceiling. Read the ceiling entry with the separate append-only amendment `reports/round-30/fixes/x63-f2.md`; this seat does not amend corpus bytes.
- A post-landing packet digest will differ if the QREG owner lands new records. Re-run the command on that generation; do not substitute its result for the dated snapshot above.

## New QREG-generation control receipt

The exact independent pairing-control command printed above was executed at
**2026-10-18T21:57:14Z**, exit **0**, **10/10** checks passed (the supplied
form rows, kit→kat negative and input preservation). It read the QREG successor
packet SHA-256
`aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`.
The operation selections and supplied surface forms are unchanged; the new
packet records did not turn the old stratum evidence into a new semantic
clearance claim.
