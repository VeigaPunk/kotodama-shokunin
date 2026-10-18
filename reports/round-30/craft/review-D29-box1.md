# R30-D29 — box-1 executable re-survey draft

- Date: 2026-10-18. Axes: executable discoverability, citation integrity, calibrated promotion evidence.
- Prior condition: `reports/round-24/promotion-review.md` Box 1, inventory condition; the seven names are filed in `reports/round-24/box1-craft.md` §1.
- Scope: the explicit union `tools/*.py`, `tools/gates/*.py`, `tools/harness/*.py`, matching the historical condition's command. Not a recursive count of frozen copies, report instruments, shell scripts, modules outside those roots or entry points inside a Python file.
- This seat authors `skill-draft.md`. This is a re-survey **draft**, not the required named non-author promotion verification; `SHONEN.md` and the promotion decision remain untouched/operator-owned.

## Dated pre-landing count and proposed disposition

At **2026-10-18T21:53:04Z**, exact repo-relative path membership in the live
SKILL.md found **28** scoped Python files, **19 named / 9 unnamed**. SKILL.md
SHA-256 was `2d85bfea6e6a7503b4267b84fda5f393ed14e1a3f5eae108940e7fad8adb6048`.
The original seven omissions reproduce, and the two register gates added since
the old review are also unnamed:

| Unnamed executable before landing | Draft treatment | Primary contract citation |
|---|---|---|
| `tools/exercise-handoff-e2e.py` | Supporting-surface row; explicit successor-baseline selection, no assertion that old rendered count prose is current | module docstring Profiles / Assertions; `reports/round-29/defects/routed.md` Fresh v3 renderer claim drift |
| `tools/assemble-d2-typed.py` | Supporting-surface row; D2 adapter is distinguished from the D4 family's own build | module docstring Interface / Fail-closed rules |
| `tools/gates/d4-assembly-check-gate.py` | Supporting-surface row; correct flagless source-packet operand and 0/1/2 verdict map | module docstring / main; `reports/round-18/d4/manifest.md` §2 |
| `tools/gates/d4-typed-labels-check-gate.py` | Supporting-surface row; projection operand and explicitly selected D4 source packet | module docstring / main; `reports/round-18/d4/manifest.md` §2 |
| `tools/harness/packet_links.py` | Supporting-surface row; claim/edge link resolver, not a culture gate | module docstring CLI; `reports/round-15/handoff/v2-design.md` §3 |
| `tools/harness/receipt_guard.py` | Supporting-surface row; committed-receipt write refusal, no claim of sandboxing | module docstring / guard_receipt / round_runner_main |
| `tools/harness/r8_checks.py` | Supporting-surface row; internal historical measurement, not a new general gate | module docstring Corrected semantics / Modes |
| `tools/gates/argot-derivation-gate.py` | Stratum authority, scope limits and actual source-packet entry surface | module docstring / evaluate_packet / selftest |
| `tools/gates/register-law-gate.py` | Law authority, actual source-packet entry surface and separate control requirement | module docstring / evaluate_packet / selftest |

At **2026-10-18T21:54:54Z**, the proposed union of live SKILL.md plus
`reports/round-30/craft/skill-draft.md` named **28/28**, with **0** unnamed
files in that scope. This is a **virtual insertion** result, not post-landing
closure. The same check found **26/26** table body rows carrying a concrete
local path, **38** distinct local paths resolving, and no missing path at
that draft snapshot. Later edits are rechecked rather than silently assigned
these historical counts.

## Reproduce before or after landing, with controls

The command is read-only, prints its command/mode/date and hashes, distinguishes
virtual from landed counts, and fails if the measured index omits a scoped
file. The negative controls remove one real gate name and add a nonexistent
path **in memory**; neither writes or deletes a file. Run it after SKILL.md
lands by setting `REGISTER_CRAFT_SURVEY_MODE=landed` before the same Python
command. The default virtual mode is only draft evidence.

```sh
export TMPDIR=$PWD/.scratch
python3 -B - <<'PY'
import hashlib, json, os, re
from datetime import datetime, timezone
from pathlib import Path
mode = os.environ.get('REGISTER_CRAFT_SURVEY_MODE', 'virtual')
assert mode in ('virtual', 'landed')
skill = Path('SKILL.md').read_text()
draft_path = Path('reports/round-30/craft/skill-draft.md')
draft = draft_path.read_text()
files = sorted(p.as_posix() for root in ('tools', 'tools/gates', 'tools/harness')
               for p in Path(root).glob('*.py') if p.is_file())
index = skill + ('\n' + draft if mode == 'virtual' else '')
missing = lambda text: [p for p in files if p not in text]
refs = re.compile(r'tools/[A-Za-z0-9_./-]+\.py')
unknown = lambda text: sorted(set(refs.findall(text)) - set(files))
control = 'tools/gates/register-law-gate.py'
phantom = 'tools/gates/' + 'REGISTER-CRAFT-NONEXISTENT-CONTROL.py'
checks = {
    'all_scoped_files_named': not missing(index),
    'negative_removed_gate_detected': control in missing(index.replace(control, '')),
    'negative_unknown_tool_detected': phantom in unknown(index + '\n' + phantom),
    'all_indexed_tool_paths_real': not unknown(index),
    'register_craft_heading_present': bool(re.search(r'^### Register craft\s*$', index, re.M)),
}
print(json.dumps({'date': datetime.now(timezone.utc).isoformat(),
    'command': 'python3 -B - (R30-D29 inventory command)', 'mode': mode,
    'scope': ['tools/*.py', 'tools/gates/*.py', 'tools/harness/*.py'],
    'skill_sha256': hashlib.sha256(skill.encode()).hexdigest(),
    'draft_sha256': hashlib.sha256(draft.encode()).hexdigest(),
    'scoped_files': len(files), 'named_before': len(files)-len(missing(skill)),
    'unnamed_before': missing(skill), 'named_in_mode': len(files)-len(missing(index)),
    'unnamed_in_mode': missing(index), 'unknown_indexed_tools': unknown(index),
    'checks': checks}, indent=2))
assert all(checks.values()), checks
PY
```

## Executed control receipt and citation check

At **2026-10-18T21:57:14Z**, the exact inventory command above was executed
in `virtual` mode, exit **0**: **28/28** scoped files named, no unknown indexed
tool paths, and all **five** positive/negative checks passed. It still reads
SKILL.md SHA-256
`2d85bfea6e6a7503b4267b84fda5f393ed14e1a3f5eae108940e7fad8adb6048`;
this is deliberately not labeled post-landing closure.

At **2026-10-18T21:58:23Z**, a read-only Python invocation imported
`reports/round-30/run-validation.py` and applied its actual
`register_section`, `craft_features`, `craft_rows` and `local_references`
functions to the proposed subsection. It found all **eight** required craft
features, **26/26** cited table body rows, **39** distinct resolving draft
paths and no missing local references in the craft reports. The change from
the earlier 38-path snapshot is the added X63-F2 successor citation, not a
rewritten historical count. The same invocation ran
`git diff --exit-code 87bfc9956f0fc60e6821fe53b622d0043e28be10 -- reports/round-{8..29}`
with explicit expanded path arguments and observed exit **0**: filed report
bytes remain preserved. No acceptance receipt was published.

Final draft check at **2026-10-18T21:59:31Z** again passed the structural
contract on draft SHA-256
`e14e27fb90042b20d218a184a9d992f3063491720da74d82919d1dd9df72c519`:
all eight craft features, 26 cited rows and 39 resolving paths. The D26
embedded pairing command returned 10/10; the inventory command above returned
28/28 virtually named files and all five controls true. The D27 differential
also executed successfully, retaining its explicitly observed tokenless
speaker defect rather than calling that mutation green. Reproduce the draft
contract check with:

```sh
export TMPDIR=$PWD/.scratch
python3 -B - <<'PY'
import hashlib, json, runpy
from datetime import datetime, timezone
from pathlib import Path
m = runpy.run_path('reports/round-30/run-validation.py')
s = Path('reports/round-30/craft/skill-draft.md').read_text()
section = m['register_section'](s)
features = m['craft_features'](section)
rows = m['craft_rows'](section)
refs = m['local_references'](section)
print(json.dumps({'date': datetime.now(timezone.utc).isoformat(),
    'command': 'python3 -B - (R30-D29 draft contract)',
    'draft_sha256': hashlib.sha256(s.encode()).hexdigest(),
    'features': features, 'rows': len(rows),
    'uncited': [r for r in rows if not r['cited']],
    'local_paths': len(refs['paths']), 'missing': refs['missing']}, indent=2))
assert all(features.values()) and rows and all(r['cited'] for r in rows)
assert refs['paths'] and not refs['missing']
PY
```

## Ready-to-file post-landing wording (conditional, not yet a verdict)

> The round-24 box-1 **unnamed-executable inventory condition** is re-surveyed
> against the landed SKILL.md using the same bounded roots and exact-path rule.
> Record the command's timestamp, SKILL digest, named/total count, missing set
> and paired-control results here. Only if `mode=landed`, the missing set is
> empty and the controls pass may this one condition be called satisfied.
> Do not change the historical dossier or mark promotion boxes from this
> author review; a named non-author verifier and operator still own those acts.

## Conditions deliberately not declared closed

1. Post-landing execution has not happened in this worker's assignment: the orchestrator owns SKILL.md. A virtual append proves the proposed text names the bounded surface, not that the delivered file already does.
2. Naming tools is not proving their runtime success, frozen dependency isolation, law semantics or current handoff prose. The relevant distinct command results and moving integration dependencies are in `reports/round-30/craft/review-D27.md` and `review-D28.md`.
3. The old dossier's other box-1 conditions—loanword-dating pointers, boilerplate-basis citation, dangling legacy symbol anchors and the duplicated uncertainty block—are not collectively disposed by this inventory re-survey. No whole-SKILL staleness audit or promotion claim is made here.
4. The draft's rows are file/symbol/section cited; this worker checks local resolution and the load-bearing semantics it synthesizes, not every source's primary-text merits or real-world permission status.
5. Final round-30 validation, regressions and the post-landing citation/box-1 checks must run on the actual integrated deliverable. No filed round-8–29 artifact, SHONEN mark or canon record is rewritten.
