# R30-D30 — adversarial review of Register craft

Date: 2026-10-18. Axis: D / depth; constraints: typed-pipeline compatibility, scoped verdicts, and append-only evidence. Reviewer: R30-D30..D32 worker, not the synthesis author; this is still a lane-authored review, **not** an independent promotion verification. The reviewed synthesis is `reports/round-30/craft/skill-draft.md`, read at SHA-256 `a8e727b3ca4a1037d4d8d2dae2484635acbff7f27cf85379b1ab0e20259cf167`. The orchestrator, not this worker, owns `SKILL.md` landing.

## Verdict

**Verified with precision conditions. No rule contradicting the typed pipeline was found in this draft.** In particular, it preserves translated-label routing plus owed-form holds, supplied sound-form checking, family-local provenance, the distinction between derivation arithmetic and the axis selector, and a separately invoked law gate. It explicitly declines to equate any of those passes with canon, semantic coverage, institutional authority, or an era check.

Two small corrections should accompany integration:

- **D30-P1 — identify the projection adapter's verdict mode.** The helper row currently says `d4-typed-labels-check-gate.py` “forwards projector verdict.” Replace that tail with “forwards the projector's **`--check` byte-identity verdict: 0 identical / 1 drift / 2 could-not-evaluate; not the label findings verdict**.” The adapter actually invokes `--check` (`tools/gates/d4-typed-labels-check-gate.py:48-56`); its docstring expressly denies semantic clearance (`:21-26`). Control: the clean family-preserving CLI probe below has twelve owed-form findings, while the committed projection adapter can still exit 0. This is precision, not a demand to change the executable.
- **D30-P2 — date the worked example's revision.** The ceiling paragraph cites packet `543d68a8…`, whereas the post-QREG packet measured here is `aac91246…`. Keep the older reading explicitly historical or add the new measurement below. Do not silently relabel the old digest as current. The ratios did not change; the delivered packet bytes did.

No source, gate, component, expected set, historical report, or shared bookkeeping is changed by this review. Named open implementation limits remain open; they are not secretly added to or removed from the round's five-item O contract.

## Paired adversarial controls

The full-packet CLI run was performed **2026-10-18T21:56:35Z**, after `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. Packet SHA-256: `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`; argot gate: `b5406bcdaf41c5950438bacd9ccf73ca2e97c044f631f505129cdd0e7e2352fb`; typed projector: `tools/d2-typed-labels.py`. Temporary inputs retain their `culture-d4` parent directory and their own component tree. That matters: the projector's `packet_family` resolves from that directory name (`tools/d2-typed-labels.py:2477-2486`), not from an arbitrary scratch filename.

| Control | Argot CLI | Projector CLI / label result | Draft rule tested |
|---|---|---|---|
| Clean packet | exit 0; 8 derived pairs, 0 violations | exit 1; 12 HOLDs, 0 label FAILs | Green arithmetic preserves owed garment forms; source form and slot obligations are not erased |
| L-56 `kit → kat`, base still `tik` | exit 1; named `D4L-ARGOT-DERIV` on L-56 | unchanged 12 HOLDs; no L-56 sound failure | A legal surface is not a correct derivation; this is the discriminating positive control for the other negatives |
| **Base record L-42** `axis: mark → fire`, L-56 still declares reverse | exit 0; no new finding | unchanged 12 HOLDs | The gate replays the chosen operation, not `QREG-03`'s selector from the base axis; the draft correctly says so |
| L-56 `stage: E1 → E0` | exit 0; no new finding | unchanged 12 HOLDs | Era declaration is not institution-date enforcement; the draft retains this limitation |
| L-56 `derived_from/base: wool coat`, `term: taoc loow` | exit 0; reverse arithmetic agrees | exit 1; **13 findings = 12 HOLDs + 1 `D2L-NATIVE` FAIL**, naming L-56 and illegal `c` | Register arithmetic cannot waive sound typing or convert a gloss into a legal native form |
| L-56 `doublet_of: L-42 → L-02`, literal base still `tik` | exit 0; no new finding | unchanged 12 HOLDs | A literal base replay does not establish the claimed base-record edge; the draft requires a separate resolving identity check |

Counting/reproduction command for every row above (temporary copies only; no filed receipt is run or rewritten):

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
from pathlib import Path
import json, re, shutil, subprocess, tempfile
text = Path('examples/culture-d4/packet.d4.yml').read_text()
cases = [
    ('clean', 'L-56', {}),
    ('bad-form', 'L-56', {'term': 'kat'}),
    ('base-axis-fire', 'L-42', {'axis': 'fire'}),
    ('early-era', 'L-56', {'stage': 'E0'}),
    ('gloss-arithmetic', 'L-56', {'term': 'taoc loow',
        'derived_from': 'wool coat', 'base': 'wool coat'}),
    ('wrong-doublet', 'L-56', {'doublet_of': 'L-02'}),
]
with tempfile.TemporaryDirectory(prefix='r30-d30-') as temp:
    family = Path(temp) / 'culture-d4'
    family.mkdir()
    shutil.copytree('examples/culture-d4/components', family / 'components')
    for name, rid, changes in cases:
        match = re.search(r'(?ms)^  -\n    id: "' + rid +
            r'"\n.*?(?=^  -\n|^[^ \n#][^\n]*:|\Z)', text)
        assert match, rid
        row = match[0]
        for field, value in changes.items():
            row, count = re.subn(r'(?m)^(\s*' + field + r':).*$',
                lambda m: m[1] + ' ' + json.dumps(value), row, count=1)
            assert count == 1
        packet = family / (name + '.yml')
        packet.write_text(text[:match.start()] + row + text[match.end():])
        for tool, flags in [
            ('tools/gates/argot-derivation-gate.py', []),
            ('tools/d2-typed-labels.py', ['--packet']),
        ]:
            run = subprocess.run(['python3', '-B', tool, *flags, str(packet)],
                capture_output=True, text=True)
            selected = [line for line in run.stdout.splitlines()
                if line.startswith('coverage:') or
                (line.startswith('FINDING') and 'L-56' in line)]
            print(name, tool, run.returncode, '\n'.join(selected))
PY
```

The arithmetic probe must use the argot gate's own YAML reader. An initial helper attempt passed the projector's parsed objects into the argot evaluator and manufactured eight compound-rule errors through the readers' different backslash handling. That attempt is **not** an implementation finding; the real CLI controls above supersede it. Likewise an arbitrary scratch filename invokes the legacy D2 family path; only the family-preserving run above is the D4 measurement.

## Ceiling and law cross-checks

At **2026-10-18T21:56:36Z**, `python3 -B reports/round-28/ceiling/measure-ceiling.py` exited 0 on the new packet: **27** mark-axis plain bases, **19 legal / 8 illegal**, institutional abstraction cross-tab **1 legal / 4 illegal**, pre-fix reading **18 / 9**, delta exactly **L-45**. The packet, draft, skill and law-gate hashes were unchanged across that command. Earlier in this review, `python3 -B reports/round-28/ceiling/measure-ceiling.py --selftest` returned **10/10**. The draft preserves both reader history and the exact per-syllable legality call.

A bounded-predicate control at **2026-10-18T21:55:51Z** also justifies the draft's refusal to universalize its coda shortcut:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
import runpy
m = runpy.run_path('tools/gates/argot-derivation-gate.py')
legal = lambda word: all(m['is_legal_syllable'](s) for s in m['syllabify'](word))
for base in ('tik', 'gis', 'as'):
    rev = m['op_reverse'](base)
    print(base, legal(base), rev, legal(rev), base[0] in m['CODAS'])
PY
```

Observed: `tik True kit True True`; `gis True sig False False`; synthetic vowel-initial `as True sa True False`. The coda shortcut agrees on the measured delivered population, not on all legal strings admitted by an optional-onset template. This is a scope control, not an invented D4 lexeme.

At **2026-10-18T21:56:01Z**, `python3 -B tools/gates/register-law-gate.py examples/culture-d4/packet.d4.yml` exited 0: five law rows, eight register records, zero findings. `python3 -B tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` separately returned **20/20**, exit 0, retaining twelve owed-form HOLDs. These are distinct verdicts. The same-stamp law `--selftest` was **29/33**, and the battery was **9/10** coverage, exit 2: the clean-packet selftest and new law-baseline dependencies were still being integrated by their assigned owners. This review does not describe those incomplete O legs as green.

## Citation and inventory check

At **2026-10-18T21:56:16Z**, the following command found **38** resolving concrete local paths, **26** body table rows, zero missing paths and zero uncited body rows in the then-current draft:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
from pathlib import Path
import re
text = Path('reports/round-30/craft/skill-draft.md').read_text()
paths = sorted(set(re.findall(r'(?<![\w./])(?:tools|reports|corpus|examples)/[\w./-]+\.(?:py|md|json|yml|tsv)', text)))
rows = [(i, line) for i, line in enumerate(text.splitlines(), 1)
    if line.startswith('| ') and not any(line.startswith(prefix)
        for prefix in ('| Condition |', '| Pipeline boundary |', '| Surface |'))]
print('paths', len(paths), 'missing', [p for p in paths if not Path(p).is_file()])
print('body_rows', len(rows), 'uncited', [i for i, line in rows if not any(p in line for p in paths)])
PY
```

This checks path resolution and row citation presence, not the truth of every external framework or every historical section locator. Deep review used the executable entry contracts, the label/routing invariants in `SKILL.md`, and the register/law/ceiling authorities cited above. The promotion dossier's **post-landing** box-1 executable re-survey remains its assigned reviewer's job; the present draft review cannot substitute for that result.

## Later draft disposition and delivered-command verification

At **2026-10-18T21:58:55Z**, the draft was re-read at SHA-256 `a6e8a69a4d465de9087752c5c533c9f4138d79e846d1cd5d0668a6fdbc02b5ad`. It now explicitly dates the ceiling at 21:53:04Z on the **pre-integration packet**. **D30-P2 is addressed.** The new X63-F2 amendment citation resolves, and the concrete source-packet command block improves cold execution without altering the typed-pipeline boundaries. **D30-P1 remains a recommended precision edit** to the helper row, not an executable defect or a newly found typed-pipeline contradiction.

At **2026-10-18T21:59:04Z**, all shell command blocks as actually delivered in this review were extracted with `re.findall(r'```sh\n(.*?)\n```', text, re.S)` and run using `subprocess.run(['bash', '-c', block], capture_output=True, text=True, timeout=90)`, with `TMPDIR=$PWD/.scratch` and `PYTHONDONTWRITEBYTECODE=1`. All three command blocks exited 0: the six real CLI mutation pairs reproduced the table, the bounded-predicate control reproduced its three rows, and the revised draft had **39 resolving paths, 26 cited body rows, zero missing paths and zero uncited rows**. Expected gate exit-1 findings inside the controls are intentional; they are not hidden by claiming all child gates were green.

`SKILL.md` had not yet been landed at the final dependency poll, **2026-10-18T21:58:44Z** (`sha256sum SKILL.md reports/round-30/craft/skill-draft.md tools/gates/register-law-gate.py` equivalent read-only SHA-256 calculation). This review hands the parent a reviewed draft and reproducible controls; it does not wait for or pre-approve its own orchestrator-owned integration.

**Final draft review — 2026-10-18T22:00:28Z.** The complete synthesis was read again at SHA-256 `e14e27fb90042b20d218a184a9d992f3063491720da74d82919d1dd9df72c519`. The helper row now explicitly forwards the `--check` byte-identity verdict and distinguishes it from label findings. **D30-P1 and D30-P2 are both addressed; this draft is verified for the reviewed typed-pipeline composition, with no outstanding synthesis correction from this seat.** The actual round runner's `register_section`, `craft_features`, `craft_rows`, and `local_references` functions found all eight declared craft features, 26/26 cited body rows and 39 resolving paths, with zero missing paths. This remains draft review, not final round acceptance or promotion.

At **2026-10-18T22:00:08Z**, `python3 -B tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` and `python3 -B tools/gates/d4-assembly-check-gate.py examples/culture-d4/packet.d4.yml` both exited 0 with byte-identical messages, completing D30-P1's real positive control. `python3 -B reports/round-30/run-validation.py --selftest` passed **30/30**; this is acceptance-runner capability, not a settled-tree acceptance run. `git diff --exit-code 87bfc9956f0fc60e6821fe53b622d0043e28be10 -- reports/round-{8..29} tools/gates/frozen/round-{8..29}` exited 0 for the protected tracked surfaces. No historical runner or filed receipt was modified.
