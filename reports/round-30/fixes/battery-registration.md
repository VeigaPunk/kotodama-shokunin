# R30-O04..O06 — register-law battery registration

- Date: 2026-10-18. Axes: operability, discriminating controls, append-only provenance.
- Assigned write surface: `tools/check-gate-battery.py` and this fragment only.
- State: registration implemented and controlled; default-battery coverage is **blocked on parent integration**, not closed. Ten gates are registered; the last measured default coverage is `9/10`, exit 2.

## Integration dependency

The law gate belongs in duty 2, like the two D4 adapters. Its `--selftest` resolves `ROOT/examples/culture-d4/packet.d4.yml` from the script's own location; the structural-only disposable mirror cannot supply that packet. Registration must extend both the baseline coverage set and the before/after live-script preservation snapshot, without inventing an eighth mirror selftest.

**Baseline owner / parent integration:** no register-law `expected.json` exists under any default battery root at the initial measurement. Registration will deliberately yield `9/10` coverage and `BASELINE-GATE-UNCOVERED`, exit 2, until a new law baseline lands under `tools/gates/expected/` or `tools/gates/frozen/`. Creating that baseline is outside this seat's assigned write surface. Freeze final law-gate bytes after the speaker-tamper repair and the settled round-30 packet after the QREG repair; do not rewrite an older baseline or silently label the historical four-dangle packet clean. The final report will record the observed dependency state.

## Before measurement

Measured `2026-10-18T18:53:15-03:00` with:

```sh
export TMPDIR=$PWD/.scratch
python3 -B - <<'PY'
import importlib.util
from pathlib import Path
p = Path('tools/check-gate-battery.py')
spec = importlib.util.spec_from_file_location('battery', p)
b = importlib.util.module_from_spec(spec)
spec.loader.exec_module(b)
r = b.inspect_baselines(b.BASELINE_ROOTS)
print(r['summary'])
print('law baselines', [(str(p), p.read_text()[:100])
      for root in b.BASELINE_ROOTS for p in b.find_expected_files(root)
      if 'law' in str(p)])
PY
python3 -B tools/check-gate-battery.py --selftest
```

The default baseline inspection registered nine gates, covered `9/9`, pinned `19/19` baselines, and found no law baseline. The pre-change selftest returned exit 0, `35/35` controls. These are separate counters: baseline pins are not gate-verdict replays, and seven structural selftest legs are not ten executed gates.

## Implementation and controls

`REGISTER_LAW_GATE_NAMES` adds only `register-law-gate.py`; `BASELINE_ONLY_GATE_NAMES` keeps it beside the existing D4 adapters. `REGISTERED_GATE_NAMES` now has ten unique names, and `preservation_paths()` includes all ten scripts. `GATE_NAMES` and the structural-only mirror remain seven legs. Module/CLI/function documentation now distinguishes those counters and states the packet dependency. Baseline discovery, pin verification, expected-verdict preservation, and fail-closed exit semantics are unchanged.

Measured `2026-10-18T18:55:56-03:00`:

```sh
export TMPDIR=$PWD/.scratch
python3 -B tools/check-gate-battery.py --help
python3 -B tools/check-gate-battery.py --selftest
git diff --check -- tools/check-gate-battery.py reports/round-30/fixes/battery-registration.md
```

All commands exited 0. The selftest passed `44/44` controls, including the existing D4 seven-versus-nine discrimination and nine new law controls. The historical `CTRL-D4-DEFAULT-9-OF-9` is now named `CTRL-D4-9-OF-9`: nine is a historical coverage slice, not today's default.

| Law control | Required observed result |
|---|---|
| `CTRL-LAW-PRESTATE-9-GREEN` | Old registry + nine baselines: exit 0, `9/9`. |
| `CTRL-LAW-POSTSTATE-UNCOVERED` | Same tree + default registry: exit 2, `9/10`, only law `BASELINE-GATE-UNCOVERED`. |
| `CTRL-LAW-DEFAULT-10-OF-10` | Add the law baseline: exit 0, `10/10`, ten pins. |
| `CTRL-LAW-PRESTATE-REJECTS-LAW` | Old registry + law baseline: exit 2, only law baseline unknown. |
| `CTRL-LAW-FINDING-BASELINE` | A declared exit-1 dangling-HOLD verdict stays findings-bearing; inspection is explicitly not replay. |
| `CTRL-LAW-BASELINE-TAMPERED` | Append bytes only to the synthetic law snapshot: exit 2, `BASELINE-TAMPERED`, despite nominal `10/10`. |
| `CTRL-LAW-GATE-REVISED` | Revise only the synthetic law script: exit 2, `BASELINE-GATE-REVISED`. |
| `CTRL-LAW-REGISTRY` | Exact ten unique registered names, law script present, law outside the structural set. |
| `CTRL-LAW-SURFACE` | Exactly seven mirror-rooted legs, no law execution/copy, law included in preservation hashing. |

These controls test registration and pin inspection, not force/speaker/consequence semantics. The gate's dedicated selftest and the round's independent law probes own those semantics.

## Actual CLI measurements

All measurements below ran on `2026-10-18`, with `export TMPDIR=$PWD/.scratch` before creating temporary fixtures and `TMPDIR=/var/tmp` on battery children so disposable mirror legs stay outside the repo. Temporary fixtures were deleted automatically; none is filed as a baseline or substituted for the default roots.

1. **Default battery, `2026-10-18T18:55:30-03:00`:**

   ```sh
   TMPDIR=/var/tmp python3 -B tools/check-gate-battery.py
   ```

   Exit 2; `pass=7, fail=0, unevaluable=0`; ten registered, `coverage=9/10`, `pinned=19/19`, and only `register-law-gate.py` uncovered (`BASELINE-GATE-UNCOVERED`). Preservation measured 33 files before and after, zero modified/added/deleted, `preserved=true`. This is an explicit open dependency, not a green default battery.

2. **Independent omission control, `2026-10-18T18:55:55-03:00`:** construct one valid synthetic baseline for each of the nine non-law gates, pinning each live gate's actual digest, then execute:

   ```sh
   TMPDIR=/var/tmp python3 -B tools/check-gate-battery.py --baselines-root "$temporary_root"
   ```

   Observed exit 2, `9/10`, only law `BASELINE-GATE-UNCOVERED`; seven structural legs passed and 33 live files stayed preserved. The wrapper asserted the exact finding tuple, not merely any nonzero exit.

3. **Positive + tampered law snapshot, `2026-10-18T18:56:21-03:00`–`18:56:22-03:00`:** construct a temporary new law baseline from a byte-copy of the delivered packet, copy/pin the naming peer, measure the actual law CLI over that snapshot, and declare the observed exit/finding set. Keep all default roots, adding only the temporary root:

   ```sh
   python3 -B tools/gates/register-law-gate.py --packet "$temporary_root/register-law-gate/r30-temporary-control/packet.yml"
   TMPDIR=/var/tmp python3 -B tools/check-gate-battery.py \
     --baselines-root tools/gates/expected \
     --baselines-root tools/gates/frozen \
     --baselines-root reports/round-9/baselines \
     --baselines-root "$temporary_root"
   ```

   The law CLI observed exit 0 and zero finding lines after the QREG packet amendment. The battery observed exit 0, `10/10`, `pinned=20/20`; seven structural legs passed, and 33 live files stayed preserved. After appending only `\n# temporary snapshot-tamper control\n` to that snapshot, the same battery command observed exit 2, nominal `10/10`, `pinned=19/20`, and only law `BASELINE-TAMPERED`. The declared clean law verdict remained unchanged. Both wrapper assertions passed. This demonstrates real-CLI registration and tamper handling; **it does not close the missing filed-baseline dependency**.

   Law gate at this measurement: `bbad35784bfb463d41912908748ebb711f72109d811d0dc8f0110657e3b4c026`. Snapshot packet: `aac91246cede8840a52b710e8d17a6254c68ff7d93f6720c4a4a458b6c76eee3`. Any subsequent law edit needs a new pin generation.

## Adjacent regressions and limits

Measured concurrently `2026-10-18T18:56:22-03:00`–`18:56:27-03:00`, using these exact commands with `TMPDIR=$PWD/.scratch`:

| Command | Observed |
|---|---|
| `python3 -B tools/check-craft-exercise.py --selftest` | Exit 0; `10/10` domain tamper cases, `18/18` CLI cases. |
| `python3 -B tools/assemble-culture-d4.py --check` | Exit 0; byte-identical deterministic assembly. |
| `python3 -B tools/gates/typed-pipeline-gate.py --selftest` | Exit 0; `19/19`. |
| `python3 -B tools/gates/register-law-gate.py --selftest` | Exit 1; `29/33` during the live QREG/gate integration: the old `bool(base)` clean check and the three delivered mutation-tail checks fail. The speaker-tamper gate owner must settle these before freezing the law baseline. This seat does not edit that gate. |

At `2026-10-18T18:56:22-03:00`, `git diff --name-only -- reports/round-{8..29} tools/gates/frozen/round-{8..29}` emitted no paths. This seat touched no filed round-8–29 artifact, gate fixture, live packet, shared bookkeeping, or pin row, and made no commit/push. The parent owns the LOG.md entry, any new filed law baseline, and round-wide acceptance. Registration implementation is delivered; default-battery closure remains pending the dependency watch below.

## In-memory fault-injection check

Measured `2026-10-18T18:57:24-03:00`–`18:57:29-03:00`: all five deliberate regressions were rejected by named `CTRL-LAW-*` failures, exit 1. No mutant source was written to disk and no live law selftest leg was launched. Counting command (the unused import from the executed harness is omitted):

```sh
export TMPDIR=$PWD/.scratch
python3 -B - <<'PY'
from pathlib import Path
import contextlib, datetime, io, json
source_path = Path('tools/check-gate-battery.py').resolve()
compiled = compile(source_path.read_text(), str(source_path), 'exec')
mutants = ('omit-law-preservation', 'add-live-law-leg', 'ignore-law-input-tamper',
           'ignore-law-gate-revision', 'erase-law-finding-verdict')
def run(name):
    ns = {'__file__': str(source_path), '__name__': 'battery_mutation'}
    exec(compiled, ns)
    if name == 'omit-law-preservation':
        original = ns['preservation_paths']
        ns['preservation_paths'] = lambda: {
            k: v for k, v in original().items() if k != 'register-law-gate.py'}
    elif name == 'add-live-law-leg':
        original = ns['leg_plan']
        ns['leg_plan'] = lambda mirror: original(mirror) + [
            ('register-law-gate.py', [ns['sys'].executable,
             str(ns['GATES_DIR'] / 'register-law-gate.py'), '--selftest'], ns['GATES_DIR'])]
    else:
        original = ns['verify_baseline_spec']
        target = {'ignore-law-input-tamper': 'BASELINE-TAMPERED',
                  'ignore-law-gate-revision': 'BASELINE-GATE-REVISED'}.get(name)
        def verify(*args, **kwargs):
            record = original(*args, **kwargs)
            if record['gate'] == 'register-law-gate.py':
                if target:
                    record['findings'] = [r for r in record['findings'] if r['id'] != target]
                    if not record['findings']:
                        record['reading'] = 'pinned'
                else:
                    record['expected'] = {'exit': 0, 'class': 'clean', 'findings': []}
            return record
        ns['verify_baseline_spec'] = verify
    stream = io.StringIO()
    with contextlib.redirect_stdout(stream):
        code = ns['run_selftest']()
    failures = [line for line in stream.getvalue().splitlines()
                if line.startswith('SELFTEST FAIL')]
    return {'mutant': name, 'date': datetime.datetime.now().astimezone().isoformat(timespec='seconds'),
            'exit': code, 'killed': code == 1 and any('CTRL-LAW-' in line for line in failures),
            'failures': failures}
rows = [run(name) for name in mutants]
for row in rows:
    print(json.dumps(row, indent=2))
print(json.dumps({'killed': sum(row['killed'] for row in rows), 'total': len(rows)}))
raise SystemExit(0 if all(row['killed'] for row in rows) else 1)
PY
```

## Dependency watch

Started `2026-10-18T18:55:55-03:00`: read-only `inspect_baselines(BASELINE_ROOTS)` every 60 seconds, with a 20-minute upper bound. A tick succeeds only when a discovered law baseline reads `pinned` and the complete baseline inspection exits 0. No default root was hidden or replaced. The `python3 -B -u` loop imported the battery through `runpy.run_path('tools/check-gate-battery.py')`, called its baseline inspector and printed the following completed observations verbatim:

```jsonl
{"tick": 0, "at": "2026-10-18T18:55:55-03:00", "coverage": "9/10", "baseline_exit": 2, "law_baselines": []}
{"tick": 1, "at": "2026-10-18T18:56:55-03:00", "coverage": "9/10", "baseline_exit": 2, "law_baselines": []}
{"tick": 2, "at": "2026-10-18T18:57:55-03:00", "coverage": "9/10", "baseline_exit": 2, "law_baselines": []}
```

The watch was explicitly stopped after these completed polls, not reported as successful or timed out. `reports/round-30/fixes/speaker-tamper.md` confirms that even the law tool repair is a report-only candidate requiring the orchestrator to land it; both that edit and the filed baseline are parent-owned prerequisites. Waiting for the caller while withholding this handoff would not resolve them.

Final real default-battery command at **`2026-10-18T18:58:07-03:00`**, `export TMPDIR=$PWD/.scratch; TMPDIR=/var/tmp python3 -B tools/check-gate-battery.py`: exit **2**, seven structural passes, ten registered, **`9/10` coverage**, `19/19` pins, only law `BASELINE-GATE-UNCOVERED`, 33 preserved paths, zero changes. Final `python3 -B tools/check-gate-battery.py --selftest` at **`2026-10-18T18:58:26-03:00`**: exit 0, **`44/44`**; `git diff --check -- tools/check-gate-battery.py reports/round-30/fixes/battery-registration.md`: exit 0. `sha256sum tools/check-gate-battery.py` at that observation: `455b595ad6d5b1be7844fc9b53a259a5b8a0efbd788b129dbfd2cc0d0ad173ce`.

**Required parent follow-up:** land and replay the speaker-tail candidate in the law tool; freeze a **new** law baseline under a default root (for example, `tools/gates/expected/register-law-gate/r30-post/`, with the actual final gate/peer/input bytes and measured verdict); then rerun the default battery and independent omitted-law control. Do not mark the route fixed-with-control or cite default `10/10` until that measured closure exists. The temporary `10/10` smoke test above remains only a discriminating registration control.
