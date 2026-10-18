# R30-X40 — fragment index + conformance

Seat **SCRIBE X40**, round 30, loop 3 integrate round. Axes: **O / operability**
(required artifacts, discriminating controls and regressions), **C / calibration**
(dated counts, final-state and denominator separation), **D / depth** (landed
Register craft and post-landing box-1 evidence). Constraint: append-only history.
The contract is `reports/round-30/claims.json`; the declared baseline is
`87bfc9956f0fc60e6821fe53b622d0043e28be10`. `targets.json` allocates O-routed 12,
C-retro 10 and D-craft 10, totaling **32 requested seats**, not observed launches
or completions (C1 declaration read, **2026-10-18**).

This index records availability and bounded conformance, **not admission,
promotion, canon, source merits, rights clearance or worker attendance**. A file
being indexed does not mean its controls passed or its draft landed. The parent
owns shared LOG/SCORECARD integration and the actual SKILL landing. X40 writes
**only this file**, with no scratch script, source, gate, packet, pin, old-round
artifact or shared-bookkeeping edit; no commit or push. All commands run inside
this lane with `export TMPDIR=$PWD/.scratch`; no mirror-safety leg is launched by
this seat. The only validator invocation by X40 so far is `--selftest`, not a
receipt-writing historical runner.

## Evidence cut and availability

**Worker-completion cut, not round completion.** Dependencies were sampled with
60-second sleeps during this seat's work, within the 20-minute bound. This
index deliberately hands off parent-owned integration rather than pretending a
worker can land SKILL.md or a shared gate. The dated census is **22:02:41Z**;
the final replay below reports arrivals and changed bytes separately. A later
arrival requires a new dated reading, never an inferred worker failure.

The read-only poll command is `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1; python3 -B -`, with `Path('reports/round-30').rglob('*')`,
`is_file()`, sorted paths, and Python cache exclusions. Dated observations below
exclude this index once it exists; initial polls also excluded `.log`, and no
such round-30 file was present in those lists. C1 retains durable logs.

| observation UTC, 2026-10-18 | non-cache files excluding this index | meaning |
|---|---:|---|
| 21:52:49 | 2 | Declarations only; no worker-output inference. |
| 21:54:00 | 11 | Fix fragments, first law audit and durable telemetry begin landing. |
| 21:55:06 | 27 | Validator, regression instrument and craft draft present. |
| 21:56:11 | 42 | Consolidated retrospective and multiple reviews present. |
| 21:57:25 | 45 | First validation receipt present; not settled. |
| 21:59:52 | 51 | Resolution ledger, second fragment ledger and craft reviews present. |
| 22:01:01 | 51 | Same path population, six peer files written in the preceding 60 seconds. |
| 22:02:27 | 51 | A newer red receipt exists; source/runner still moving. |
| 22:04:18 | 51 | Three peer files written in the preceding 60 seconds; SKILL still unlanded. |

**Receipt trajectory, read rather than adjudicated:**

- **21:57:33Z reading:** receipt measured 21:56:22Z; all three claim flags false;
  its `df6cca3e…` runner pin did not match live `7b451818…`; nine input paths
  had changed. That earlier missing list named the resolution ledger, SKILL
  landing and box-1 survey. This is an in-flight result, not a final rejection.
- **22:02:41Z C1 reading:** receipt measured **22:01:58Z**,
  `acceptance_checks_passed: false`, `{C: true, D: false, O: false}`. Its runner
  pin is `26319fc0437b806f1a47392abe7cfde5574d8d163cf8bab575716e5e57459358`;
  live runner is `45ebb036982dcb2008a75509fa4b25ae719705ba19800ef05719381a69ab331a`.
  **Still not bound.** Its four changed inputs were the law spot-check report,
  QREG fix report, report draft and runner. The receipt's missing list now names
  only the actual SKILL landing, but its D failure also names the missing
  post-landing digest-bound box-1 result. A filename containing box1 is not
  sufficient evidence of that post-landing result.
- No aggregate validator was executed or receipt published by X40. A runner's
  passing `--selftest`, its existence, or a green C flag in an unbound receipt
  is not a delivered-tree O/C/D acceptance. The parent must rerun after landing
  and after this index stops changing.

### Routed disposition at the census

Read-only JSON census, **2026-10-18T22:02:41Z**, command `python3 -B -` reading
`routed-resolution.json`, `regression.json` and `operability-verification.json`:
exactly **five rows**, **three fixed-with-control** (QREG, X63-F2, telemetry),
**two documented-with-owner-and-reason** (battery baseline, speaker tail).
The ledger explicitly says `integration-in-progress-not-round-acceptance` and
`regressions_green: false`. Those dispositions satisfy neither an assertion
that all five were fixed nor the separate requirement for green regressions.

The regression receipt at that read reports **37/40** exit-zero commands,
with battery exit 2, law-selftest exit 1 and handoff-v3 exit 1; it also records
QREG-report read-set movement. This is attributed evidence from
`python3 -B reports/round-30/verify-operability.py --regressions-only`, not an
X40 execution or a stable green endpoint. The three initial failures must not
be erased or inherited as the final regression verdict.

## Required-artifact and conformance map

| claim / obligation | evidence surface | conformance boundary |
|---|---|---|
| O: exactly five routed items dispositioned | `reports/round-30/routed-resolution.json`; `reports/round-30/fixes/` | A fixed route needs its dated control; a documented route needs owner + reason. The five-item contract does not close all historical R29 open defects. |
| O: QREG-05..08 dangles | `reports/round-30/fixes/qreg-dangles.md`; `reports/round-30/audit/x38-law-gate-clean-state.md` | A genuinely finding-free successor is a new result, not the historical R28/R29 four-HOLD reading. Retain a planted dangling-reference control; update selftest baseline assumptions and law-block targeting. |
| O: law battery 10/10 | `reports/round-30/fixes/battery-registration.md`; `tools/check-gate-battery.py` | Registered gates, pinned-baseline coverage and executed structural selftests are different counters. A final law baseline must bind final gate/packet bytes; 9/10 remains fail-closed, not green. |
| O: X63-F2 | `reports/round-30/fixes/x63-f2.md` | This is a new companion amendment withdrawing the false phrase-zero inference. It preserves the corpus entry; do not require an unauthorized rewrite or turn the historical finding-bearing audit into a green one. |
| O: speaker-tamper tail | `reports/round-30/fixes/speaker-tamper.md` | An in-memory candidate is not a delivered gate fix. Mutate a speaker inside `register_law`, not an earlier QREG identity row; compare added emitted finding lines and retain positive/ID-bearing controls. |
| O: durable telemetry | `AGENTS.md`; `reports/round-30/fixes/telemetry-convention.md`; `reports/round-30/telemetry/` | Distinct declaration and worker-observation schemas need distinct paths/checkers. Requested seats and unknown/null runtime totals are not completions; durability does not recover R25–28 lost samples. |
| O: regressions | `reports/round-30/regression.json`; `reports/round-30/verify.md`; `reports/round-30/validation.json` | Initial red observations remain dated history; only the final stable read set supports delivered-tree green. Pin verification is not frozen-verdict replay. |
| C: loop-3 + three-loop retrospective | `reports/round-30/loop3-retrospective.md`; `reports/round-30/retro/`; `reports/round-30/retrospective-audit-C23.md`; `reports/round-30/retrospective-audit-C24.md` | Final states versus draft cuts, forecast versus actual delivery, flags versus literal contracts, and receipt versus parent-prose counters remain separate. R30 is active and R31/R32 prospective at the historical cut. |
| C: freshness question + recommendation | `reports/round-30/loop3-retrospective.md` §4 | A prospective ≥95% split-instrument recommendation is not an operator ruling, a new F measurement, or retroactive admission of R11/R17/R22. Disposition is not a stable numerator. |
| D: unified Register craft | `reports/round-30/craft/skill-draft.md`; `reports/round-30/craft/review-D26.md`; `reports/round-30/craft/review-D27.md`; `reports/round-30/craft/review-D28.md`; `SKILL.md` | A cited synthesis draft is not the actual landing. The D26–D28 reports explicitly identify author/self-review; do not present them as non-author promotion verification. |
| D: box-1 post-landing re-survey | `reports/round-30/craft/review-D29-box1.md`; actual `SKILL.md` bytes | A virtual union naming 28/28 files is draft evidence. The required new survey must pin the landed skill digest and bounded roots; it does not close all promotion conditions. |
| all: protected history and scope | `reports/round-30/scope.md`; C1 baseline check below | Sampled byte/mode preservation is not proof of no transient write-and-restore; fleet/sibling cleanliness is not assessed. |

## Conformance observations during integration

1. **The acceptance receipt must bind both the live runner and read set.** The
   first receipt is present but unbound/red at the dated cut above. This index
   will not infer a final result from that receipt, a runner's existence or a
   green unrelated leg. C1 prints runner binding and every changed input.
2. **Companion amendment versus runner contract.** At the 21:57Z cut, the X63-F2
   worker authorized only its new report and preserved the corpus entry. The
   independent verifier explicitly accepts that new-file amendment, while an
   earlier aggregate-runner version demanded inserted corpus sections. That is
   an integration/read-contract discrepancy, not grounds for X40 to rewrite a
   filed entry. A later runner/disposition must reconcile the authorized form.
3. **Telemetry coexistence is not worker duplication.** X37's declaration
   snapshot and O11–O12's worker-observation snapshot are different instruments.
   `verify.md` records an initial collision at `dispatch-stats.json`; the X37
   checker now reads `dispatch-declaration-x37.json`. Both controls must read
   their actual current inputs; an older receipt is not sufficient. Neither
   schema attests full-wave attendance or a served upstream model.
4. **Retrospective freshness does not restart F.** The consolidated report
   explicitly retains rejected rounds and separates raw stability, semantic
   regression and explained drift. Its numerical recommendation is prospective;
   no comparable new three-loop F percentage or operator ratification exists.
5. **Author review is disclosed.** Craft reports D26–D29 are useful source-bound
   checks, not independent non-author promotion reviews. Their virtual box-1
   calculation cannot substitute for the actual skill landing and digest-bound
   re-survey. A re-survey is not a promotion decision.

## Census

C1 executed **2026-10-18T22:02:41Z**, exit **0**: **51 files**, **1,054,616
bytes**, excluding this index and Python caches. Partitions: root 21, audit 4,
craft 6, fixes 5, retro 3, scribe 2, telemetry 10. No failed read, file changed
inside its individual read, or strict-JSON error was observed. This is a
sequential read-time census, **not an atomic or settled snapshot**. The self row
is excluded because its own digest would be circular. C1 regenerates a complete
new live table to stdout without rewriting the dated rows below.

<!-- X40:CENSUS:BEGIN -->
| artifact | bytes | sha8 | mtime UTC | inferred owner / evidence state |
|---|---:|---|---|---|
| `reports/round-30/adjacency.md` | 18906 | `a9729d0a` | 2026-10-18T21:58:27Z | X scope/scribe or parent-integration draft |
| `reports/round-30/audit/x38-law-gate-baseline.json` | 43682 | `52a557ad` | 2026-10-18T21:53:45Z | X law spot-check |
| `reports/round-30/audit/x38-law-gate-clean-state.json` | 36977 | `a9189f11` | 2026-10-18T22:02:06Z | X law spot-check |
| `reports/round-30/audit/x38-law-gate-clean-state.md` | 8793 | `3c7bdc32` | 2026-10-18T22:02:28Z | X law spot-check |
| `reports/round-30/audit/x38-law-gate-clean-state.py` | 10365 | `f02158f9` | 2026-10-18T22:01:55Z | X law spot-check |
| `reports/round-30/claims.json` | 2987 | `d506b87b` | 2026-10-18T21:51:37Z | parent declaration |
| `reports/round-30/craft/review-D26.md` | 7187 | `d967ad0f` | 2026-10-18T21:57:43Z | D craft draft/review |
| `reports/round-30/craft/review-D27.md` | 8708 | `06da9e6f` | 2026-10-18T21:57:59Z | D craft draft/review |
| `reports/round-30/craft/review-D28.md` | 7881 | `f1ac4d88` | 2026-10-18T21:59:20Z | D craft draft/review |
| `reports/round-30/craft/review-D29-box1.md` | 10348 | `08226bf2` | 2026-10-18T21:59:49Z | D craft draft/review |
| `reports/round-30/craft/review-D30.md` | 13295 | `ab0a7496` | 2026-10-18T22:00:43Z | D craft draft/review |
| `reports/round-30/craft/skill-draft.md` | 18030 | `e14e27fb` | 2026-10-18T21:59:20Z | D craft draft/review |
| `reports/round-30/fixes/battery-registration.md` | 14132 | `5c933bc5` | 2026-10-18T21:58:41Z | O routed-fix evidence |
| `reports/round-30/fixes/qreg-dangles.md` | 18291 | `1dabdbc0` | 2026-10-18T22:01:53Z | O routed-fix evidence |
| `reports/round-30/fixes/speaker-tamper.md` | 23337 | `f2070a10` | 2026-10-18T21:57:05Z | O routed-fix evidence |
| `reports/round-30/fixes/telemetry-convention.md` | 5353 | `ab25fd06` | 2026-10-18T21:55:23Z | O routed-fix evidence |
| `reports/round-30/fixes/x63-f2.md` | 8442 | `10c2b9f2` | 2026-10-18T21:53:40Z | O routed-fix evidence |
| `reports/round-30/log-draft.md` | 4086 | `0b4fa761` | 2026-10-18T21:58:33Z | X scope/scribe or parent-integration draft |
| `reports/round-30/loop3-retrospective.md` | 36829 | `edda7ba5` | 2026-10-18T21:58:22Z | C synthesis/audit evidence |
| `reports/round-30/operability-verification.json` | 46445 | `116eab1f` | 2026-10-18T22:01:40Z | O measurement/disposition evidence |
| `reports/round-30/regression-initial.json` | 116620 | `aff2cba3` | 2026-10-18T21:55:30Z | O measurement/disposition evidence |
| `reports/round-30/regression.json` | 128713 | `4c00f9dd` | 2026-10-18T22:01:40Z | O measurement/disposition evidence |
| `reports/round-30/report-draft.md` | 12171 | `01279f11` | 2026-10-18T22:01:29Z | X scope/scribe or parent-integration draft |
| `reports/round-30/rerun.json` | 27506 | `3a01671d` | 2026-10-18T22:01:29Z | X scope/scribe or parent-integration draft |
| `reports/round-30/retro/r25-26.md` | 12120 | `b81d6524` | 2026-10-18T21:54:07Z | C retrospective evidence |
| `reports/round-30/retro/r27-28.md` | 13148 | `b36ca943` | 2026-10-18T21:55:29Z | C retrospective evidence |
| `reports/round-30/retro/r29.md` | 13594 | `c0434d49` | 2026-10-18T21:56:07Z | C retrospective evidence |
| `reports/round-30/retrospective-audit-C23-C25.py` | 14354 | `316afc30` | 2026-10-18T21:57:31Z | C synthesis/audit evidence |
| `reports/round-30/retrospective-audit-C23.md` | 8495 | `5322c057` | 2026-10-18T21:59:51Z | C synthesis/audit evidence |
| `reports/round-30/retrospective-audit-C24.md` | 13887 | `f59ad44e` | 2026-10-18T22:00:28Z | C synthesis/audit evidence |
| `reports/round-30/retrospective-audit-C25.md` | 3181 | `e6bb454e` | 2026-10-18T21:59:51Z | C synthesis/audit evidence |
| `reports/round-30/routed-resolution.json` | 8836 | `c53c11d4` | 2026-10-18T21:58:44Z | O measurement/disposition evidence |
| `reports/round-30/run-validation.py` | 51204 | `45ebb036` | 2026-10-18T22:02:03Z | acceptance instrument, not verdict |
| `reports/round-30/scope.md` | 15253 | `9adcb8c6` | 2026-10-18T21:57:07Z | X scope/scribe or parent-integration draft |
| `reports/round-30/scorecard-draft.md` | 4912 | `e0cfcd48` | 2026-10-18T21:58:33Z | X scope/scribe or parent-integration draft |
| `reports/round-30/scribe/capability-row.md` | 6596 | `216ce762` | 2026-10-18T22:00:53Z | X scribe evidence |
| `reports/round-30/scribe/fragment-ledger.md` | 10679 | `ae83749d` | 2026-10-18T22:00:43Z | X scribe evidence |
| `reports/round-30/targets.json` | 174 | `c03e9c95` | 2026-10-18T21:51:37Z | parent declaration |
| `reports/round-30/telemetry/check-dispatch.py` | 7784 | `c13a0405` | 2026-10-18T21:54:54Z | O/X durable telemetry |
| `reports/round-30/telemetry/check.json` | 219 | `032e4a5c` | 2026-10-18T21:54:42Z | O/X durable telemetry |
| `reports/round-30/telemetry/control-receipt.json` | 3225 | `c897ab16` | 2026-10-18T21:55:11Z | O/X durable telemetry |
| `reports/round-30/telemetry/controls.json` | 1934 | `d5df29a0` | 2026-10-18T21:54:42Z | O/X durable telemetry |
| `reports/round-30/telemetry/dispatch-declaration-x37.json` | 3688 | `4b7a9c13` | 2026-10-18T21:54:54Z | O/X durable telemetry |
| `reports/round-30/telemetry/dispatch-stats.json` | 2389 | `a1f8ec19` | 2026-10-18T21:54:42Z | O/X durable telemetry |
| `reports/round-30/telemetry/dispatch-telemetry.py` | 10531 | `a177757b` | 2026-10-18T21:54:10Z | O/X durable telemetry |
| `reports/round-30/telemetry/inputs/claims.json` | 2987 | `d506b87b` | 2026-10-18T21:54:32Z | O/X durable telemetry |
| `reports/round-30/telemetry/inputs/targets.json` | 174 | `c03e9c95` | 2026-10-18T21:54:32Z | O/X durable telemetry |
| `reports/round-30/telemetry/worker-observation.json` | 1207 | `bfcd8693` | 2026-10-18T21:54:10Z | O/X durable telemetry |
| `reports/round-30/validation.json` | 183009 | `e050f81d` | 2026-10-18T22:01:58Z | acceptance receipt: check binding |
| `reports/round-30/verify-operability.py` | 28520 | `8f9e522c` | 2026-10-18T21:58:11Z | O measurement/disposition evidence |
| `reports/round-30/verify.md` | 3432 | `08d60251` | 2026-10-18T21:56:58Z | O measurement/disposition evidence |
<!-- X40:CENSUS:END -->

Names in the census are path/partition-based **inferences**, not a native dispatch
roster. Hash prefixes are diagnostic abbreviations, **not new frozen pin rows**.
All files, including durable telemetry logs if present, are retained; only
`__pycache__/`, `.pyc` and `.pyo` are excluded. Failed reads and files changing
while read are printed, not silently omitted or counted green.

## C1 — reproducible census, binding and index controls

Run this exact block from the lane root. It writes no files and executes no
historical validator. It prints a new dated inventory and a drift-aware replay
of this index; arrivals/digest changes are **staleness**, not missing-worker or
quality verdicts. Controls reject duplicate rows, a missing path, altered byte
size, altered digest and duplicate JSON keys **in memory**. The live table is
printed separately, so it can be used for a new dated census without overwriting
this one. Protected-history checks compare Git blob identities with the declared
baseline, including the report files of round 29.

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1 GIT_OPTIONAL_LOCKS=0
python3 -B - <<'PY'
from collections import Counter
from datetime import datetime, timezone
import hashlib, json, re, subprocess
from pathlib import Path
BASE = Path('reports/round-30')
SELF = BASE / 'fragment-index-x40.md'
REV = '87bfc9956f0fc60e6821fe53b622d0043e28be10'
def digest(data):
    return hashlib.sha256(data).hexdigest()
def pairs(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError('duplicate JSON key: ' + key)
        out[key] = value
    return out
def strict(text):
    return json.loads(text, object_pairs_hook=pairs)
def category(relative):
    parts = Path(relative).relative_to(BASE).parts
    name = parts[-1]
    if len(parts) > 1:
        return {'audit': 'X law spot-check', 'craft': 'D craft draft/review',
                'fixes': 'O routed-fix evidence', 'retro': 'C retrospective evidence',
                'telemetry': 'O/X durable telemetry', 'pins': 'O successor pins',
                'pinsweep': 'O successor pins', 'scribe': 'X scribe evidence'}.get(parts[0], 'unassigned: ' + parts[0])
    if name in ('claims.json', 'targets.json'):
        return 'parent declaration'
    if name == 'run-validation.py':
        return 'acceptance instrument, not verdict'
    if name == 'validation.json':
        return 'acceptance receipt: check binding'
    if name.startswith('retrospective-audit') or name == 'loop3-retrospective.md':
        return 'C synthesis/audit evidence'
    if name.startswith(('regression', 'operability', 'verify', 'routed-resolution')):
        return 'O measurement/disposition evidence'
    if 'box' in name.lower() and '1' in name:
        return 'D box-1 survey evidence'
    if name in ('scope.md', 'adjacency.md', 'report-draft.md', 'rerun.json', 'log-draft.md', 'scorecard-draft.md'):
        return 'X scope/scribe or parent-integration draft'
    return 'unassigned'
rows, errors, unstable, bad_json = [], [], [], []
for path in sorted(BASE.rglob('*')):
    if not path.is_file() or path == SELF or '__pycache__' in path.parts or path.suffix in ('.pyc', '.pyo'):
        continue
    try:
        before = path.stat()
        raw = path.read_bytes()
        after = path.stat()
        if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
            unstable.append(str(path))
        if path.suffix == '.json':
            try:
                strict(raw.decode())
            except (ValueError, UnicodeError) as exc:
                bad_json.append({'path': str(path), 'error': str(exc)})
        rows.append((str(path), len(raw), digest(raw)[:8],
                     datetime.fromtimestamp(after.st_mtime, timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), category(str(path))))
    except OSError as exc:
        errors.append({'path': str(path), 'error': str(exc)})
actual = {p: (size, sha8) for p, size, sha8, _, _ in rows}
text = SELF.read_text()
section = text.split('<!-- X40:CENSUS:BEGIN -->', 1)[1].split('<!-- X40:CENSUS:END -->', 1)[0]
indexed = [(p, int(size), sha8) for p, size, sha8 in re.findall(
    r'(?m)^\| `([^`]+)` \| (\d+) \| `([a-f0-9]{8})` \|', section)]
def conforms(items, expected):
    names = [p for p, _, _ in items]
    return len(names) == len(set(names)) and set(names) == set(expected) and all(expected.get(p) == (size, sha8) for p, size, sha8 in items)
probe = [(str(BASE / 'CONTROL.json'), 2, digest(b'{}')[:8])]
expected = {probe[0][0]: probe[0][1:]}
checks = {'positive_exact_snapshot': conforms(probe, expected),
          'negative_duplicate': not conforms(probe + probe, expected),
          'negative_missing_path': not conforms([(str(BASE / 'ABSENT.json'), 2, probe[0][2])], expected),
          'negative_size': not conforms([(probe[0][0], 3, probe[0][2])], expected),
          'negative_digest': not conforms([(probe[0][0], 2, '0'*8)], expected)}
try:
    strict('{"id": 1, "id": 2}')
except ValueError:
    checks['negative_duplicate_json_key'] = True
else:
    checks['negative_duplicate_json_key'] = False
names = [p for p, _, _ in indexed]
receipt_path, runner_path = BASE / 'validation.json', BASE / 'run-validation.py'
receipt = strict(receipt_path.read_text()) if receipt_path.is_file() else {}
runner_sha = digest(runner_path.read_bytes()) if runner_path.is_file() else None
inputs = receipt.get('input_sha256', {})
input_drift = [p for p, sha in inputs.items() if not Path(p).is_file() or digest(Path(p).read_bytes()) != sha]
roots = [f'{root}/round-{number}' for root in ('reports', 'tools/gates/frozen') for number in range(8, 30)]
entries = subprocess.check_output(['git', 'ls-tree', '-r', '-z', REV, '--', *roots]).split(b'\0')
protected, changed = 0, []
for entry in entries:
    if not entry:
        continue
    meta, rawpath = entry.split(b'\t', 1)
    _, kind, oid = meta.decode().split()
    if kind != 'blob':
        continue
    protected += 1
    path = Path(rawpath.decode())
    raw = path.read_bytes() if path.is_file() else None
    observed = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() if raw is not None else None
    if observed != oid:
        changed.append(str(path))
status = subprocess.check_output(['git', 'status', '--porcelain=v1', '-uall', '--', *roots], text=True).splitlines()
summary = {'observed_at_utc': datetime.now(timezone.utc).isoformat(),
    'command': 'C1: python3 -B - (exact block in fragment-index-x40.md)',
    'files_excluding_self_and_caches': len(rows), 'bytes': sum(r[1] for r in rows),
    'partitions': dict(sorted(Counter(Path(r[0]).relative_to(BASE).parts[0] if len(Path(r[0]).relative_to(BASE).parts)>1 else '(root)' for r in rows).items())),
    'read_errors': errors, 'changed_during_read': unstable, 'json_errors': bad_json,
    'index_rows': len(indexed), 'duplicate_index_rows': len(names) != len(set(names)),
    'unavailable': sorted(set(names)-set(actual)), 'arrivals_since_census': sorted(set(actual)-set(names)),
    'digest_or_size_drift': [p for p, size, sha8 in indexed if actual.get(p) != (size, sha8)],
    'snapshot_current': conforms(indexed, actual), 'controls': checks,
    'runner_present': runner_path.is_file(), 'receipt_present': receipt_path.is_file(),
    'runner_sha256_live': runner_sha, 'runner_sha256_receipt': receipt.get('runner_sha256'),
    'runner_bound': runner_sha is not None and runner_sha == receipt.get('runner_sha256'),
    'receipt_measured_at_utc': receipt.get('measured_at_utc'),
    'acceptance_checks_passed': receipt.get('acceptance_checks_passed'),
    'claims': {k: v.get('passed') for k, v in receipt.get('claims', {}).items()},
    'receipt_input_drift': input_drift, 'missing_dependencies': receipt.get('missing_dependencies'),
    'protected_paths': protected, 'protected_byte_differences': changed, 'protected_status_rows': status}
print(json.dumps(summary, indent=2))
print('| artifact | bytes | sha8 | mtime UTC | inferred owner / evidence state |')
print('|---|---:|---|---|---|')
for path, size, sha8, modified, owner in rows:
    print(f'| `{path}` | {size} | `{sha8}` | {modified} | {owner} |')
assert all(checks.values()) and not errors and not unstable and not bad_json
assert indexed and len(names) == len(set(names)) and not (set(names)-set(actual))
assert not changed and not status
print('INDEX_STRUCTURE_AND_NEGATIVES=PASS; snapshot_current=' + str(summary['snapshot_current']))
PY
```

## Verification record and boundaries

- **2026-10-18T21:53:00Z**, read-only `python3 -B -` using `git ls-tree -r
  87bfc9956f0fc60e6821fe53b622d0043e28be10 -- reports/round-{8..29}
  tools/gates/frozen/round-{8..29}`, per-path `git hash-object` and
  `git status --porcelain=v1 -- <same roots>`: **1,764 tracked paths**, **0 byte
  mismatches**, **0 protected status rows**. The lane HEAD was
  `44145d5f337dea425c20dccafee98e0882678660`; the head is not confused with the
  declared baseline. No historical validator was invoked.
- **2026-10-18T21:57:33Z**, `export TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1; python3 -B reports/round-30/run-validation.py
  --selftest`: exit **0**, **30/30** controls. That is the runner's unit/control
  result on its observed bytes, not a full O/C/D acceptance.
- **2026-10-18T22:01:27Z**, X40 independently executed `python3 -B
  tools/gates/register-law-gate.py --packet examples/culture-d4/packet.d4.yml`:
  exit **0**, `law_rows=5 identity_rows=8 record_ids=183 registers=17 dangling=0
  findings=0`. The separate `python3 -B tools/gates/register-law-gate.py
  --selftest` exited **1**, **29/33**, failing the baseline replay and delivered
  force/speaker/consequence controls. The packet and gate hashes were identical
  before/after these two CLI calls: packet
  `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`, gate
  `bbad35784bfb463d41912908748ebb711f72109d811d0dc8f0110657e3b4c026`.
  A clean law input does **not** fix the gate's selftest or prove tokenless
  speaker coverage. Record-ID and argot total-row counts are different readers'
  populations, not interchangeable totals.
- **2026-10-18T22:01:27Z**, read-only `python3 -B -` loading
  `tools/check-gate-battery.py` with `runpy.run_path` and calling
  `inspect_baselines(BASELINE_ROOTS)`: **10 registered**, **19/19 pinned
  baselines**, **9/10 gate coverage**, law gate uncovered, `baseline_exit: 2`.
  No structural selftest or frozen verdict replay was run by that inspection.
- **2026-10-18T22:01:27Z**, `python3 -B
  reports/round-30/telemetry/check-dispatch.py --selftest`: exit **0**, the
  declaration positive check and **11/11** negative controls pass. Separately,
  `python3 -B reports/round-30/telemetry/dispatch-telemetry.py --check`: exit
  **0**, no findings. Both actual checker inputs now coexist on distinct durable
  paths. The collision is resolved at this read; full-wave runtime remains
  **could-not-evaluate** in both, not an inferred completion count.
- **2026-10-18T22:04:46Z** and **22:05:06Z**, the exact C1 block was extracted
  from this filed index with `re.findall` and executed via
  `subprocess.run(['bash'], input=block, ...)`, no scratch script or redirection.
  Both exited **0**: **51 indexed / 51 observed**, **0 duplicate rows**, **0
  unavailable paths**, **0 arrivals**, **6/6** in-memory controls true; protected
  history still **1,764 paths / 0 byte differences / 0 protected status rows**.
  The index remains intentionally **drift-aware**, not falsely current: exactly
  **seven** rows changed after the 22:02:41Z census — adjacency, law spot-check
  report, QREG fix report, report draft, rerun receipt, routed resolution and
  operability verifier. Their names and current bytes are printed by C1.
  The observed live total was then **1,074,490 bytes**. The table's earlier
  hashes are retained as the dated reading, not silently re-pinned.
- At the same **22:05:06Z** replay, runner binding was still false; the receipt
  remained the red **22:01:58Z** cut with C true / D false / O false. Its seven
  changed read-set paths include **this index**, which is why the parent must
  rerun after workers finish writing rather than accept an older receipt.
  `SKILL.md` remained unlanded in the latest dependency poll at **22:04:18Z**.
- **2026-10-18T22:05:06Z**, a separate read-only Python text check on this file
  passed: final newline, no NUL, no trailing whitespace, balanced fences and
  exactly one extractable C1 shell block. `git diff --check` also exited **0**
  at **22:04:46Z**; since the index is new/untracked, that Git check alone is
  not treated as verification of this file.

### Coexisting indexes and resolved read-contract issue

`reports/round-30/scribe/fragment-ledger.md` is D32's separate dated census,
not a colliding write target. It uses its own earlier stamp and excludes its
own ledger, whereas X40 excludes this index and includes that ledger. The two
populations need not have equal counts/hashes; compare date and exclusion rule,
not an artifact count to requested workers. Neither index settles the other.

The companion-amendment discrepancy described above was reconciled in the
live runner source inspected **2026-10-18T22:05Z**, command `Read` of
`reports/round-30/run-validation.py` at `measure_operability`: it accepts preserved
corpus history plus an authorized new companion file and checks the original
sound-symbolism witness. This is a source-contract observation, **not** an X40
execution of full acceptance or permission to rewrite the filed entry.

### Parent integration still required at handoff

1. Land the authorized speaker candidate in the actual gate and replay its
   clean/tokenless/ID-bearing/missing-record controls, including law-block-only
   mutation and the zero-finding baseline. The delivered selftest was red at
   X40's execution; an in-memory candidate must not be relabeled delivered.
2. Freeze a **new** law baseline for the settled gate and packet, obtain actual
   default battery **10/10**, and settle the v3 successor/replay. Preserve old
   expected sets, rows and filed receipts; record controls and supersession.
3. Land the cited Register craft subsection in actual `SKILL.md`, then run and
   digest-bind the real post-landing box-1 survey. Virtual 28/28 and author review
   do not do this, and the survey does not confer promotion.
4. Refresh the five-item ledger from final controls; run the standard round-30
   validator/regressions on the final stable read set after this index stops
   changing. A ledger with documented residuals is allowed by the declaration,
   but green regressions are a separate requirement. Keep the retrospective's
   freshness recommendation prospective and the wider R29 backlog open.
5. Integrate LOG/SCORECARD append-only and, if a later fragment census is needed,
   rerun C1 for a **new dated** reading. No full-round admission, stable green
   regression endpoint, non-author promotion verification, canon, rights,
   source-merits or fleet-cleanliness verdict is issued by X40.

FILES: reports/round-30/fragment-index-x40.md | SUMMARY: X40 filed the 51-artifact dated census, conformance/ownership map and passing drift-aware controls; unbound red acceptance, law/battery gaps and parent-owned skill integration remain explicit.
