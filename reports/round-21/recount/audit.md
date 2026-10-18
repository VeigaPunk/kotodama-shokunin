# R21-C23..C24 — Independent recount audit

- Axis: calibration. Audit date: 2026-10-18.
- I independently re-ran **23 distinct command strings from the recorded recount material**, covering R17, R18, R19, and R20. The R18 D2 gate was run at both snapshots for the byte-identity comparison. A fresh clone of current HEAD `8115eaaeb57c9dce157fe291337cb52dd914c6cf` and a separate pre-generalization clone at `3dd3754207032cb81f5fb3e202fe85cf79211339` were kept under `.scratch/r21-c23-audit.QVZzSt/`. All commands ran on 2026-10-18. No historical `reports/round-17..20/run-validation.py` runner was invoked; no artifact under `reports/round-8..20` was written in the source checkout. `TMPDIR` was set to the lane `.scratch/` before scratch-writing commands.
- The R17–R19 recorded values below are from the named Round 21 recount reports; R20 values are from the filed R20 validation receipt. This is an audit sample, not a claim that this report alone covers every source command.

## Independent comparisons

| Command (rerun date) | Recorded observation | Independent observation | Result |
|---|---|---|---|
| `python3 tools/assemble-culture-d4.py --check` (R17 C02; 2026-10-18) | `reports/round-21/recount/r17-2.md`: exit 0. | Exit 0; `packet.d4.yml: byte-identical deterministic assembly`. | Match. |
| `python3 tools/assemble-culture-d3.py --check` (R17 C03; 2026-10-18) | `r17-3.md`: exit 0. | Exit 0; both `packet.json` and `packet.gates.yml` reported byte-identical deterministic assembly. | Match. |
| `python3 tools/assemble-culture-d3.py --selftest` (R17 C03; 2026-10-18) | `r17-3.md`: exit 0. | Exit 0; selftest 85/85. | Match. |
| `python3 tools/assemble-d2.py --check` (R17 C03; 2026-10-18) | `r17-3.md`: exit 0. | Exit 0; `packet.d2.yml: byte-identical deterministic assembly`. | Match. |
| `python3 tools/assemble-d2.py --selftest` (R17 C03; 2026-10-18) | `r17-3.md`: exit 0. | Exit 0; selftest 42/42. | Match. |
| `python3 tools/assemble-d2-typed.py --check` (R17 C03; 2026-10-18) | `r17-3.md`: exit 0. | Exit 0; `examples/culture-d2/packet.d2.typed.yml: byte-identical deterministic typed packet`. | Match. |
| `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` (R18 C05; 2026-10-18) | `r18-1.md`: exit 0; 19/19 legs; 15 FINDING + 1 NOTE; 2,508 stdout bytes, SHA-256 `f7630ddbeac2ce6b3e3ceb4e4fc2c275d428f1fe5588873656d9bc7fe7b5aee1`; empty stderr. | Same exit, counts, byte length, SHA-256, and empty stderr in the current clone. | Match. |
| `python3 tools/gates/typed-pipeline-gate.py` (R18 C06; 2026-10-18) | `r18-2.md`: exit 0; 16/16 legs; 15 FINDING + 1 NOTE; 2,677 stdout bytes, SHA-256 `15cdfbda73cd56cb6107d2fdbee533dbce47e9381e2082085ca1f0c45f2e695b`; empty stderr. | Same exit, counts, byte length, SHA-256, and empty stderr in the current clone. | Match. |
| `python3 tools/gates/typed-pipeline-gate.py` (R18 C07; 2026-10-18; run once at each revision) | `r18-3.md`: pre-generalization `3dd3754207032cb81f5fb3e202fe85cf79211339` and current `8115eaaeb57c9dce157fe291337cb52dd914c6cf` both exit 0, 16/16, 2,677 bytes, stdout SHA-256 `15cdfbda73cd56cb6107d2fdbee533dbce47e9381e2082085ca1f0c45f2e695b`; byte-identical. | Both isolated-clone runs returned those same values; stdout byte strings and exit codes were identical. | Match; the R18 D2 byte-identity repair is reproduced. |
| `python3 tools/replay-frozen.py tools/gates/frozen/round-18/repin-d2/MANIFEST.tsv --json` (R18 C08; 2026-10-18) | `r18-4.md`: initial run 10/11 reproduced, 0 mismatches, 1 unevaluable, exit 2 because fresh clone omitted ignored `tools/gates/frozen/round-11/typed-pipeline/run.log`; after copying the source log with SHA-256 `9a69985aabdf3e9bf233653f7b31ce6f3bf5fd12858cfedf7e9ebca14ada4606`, final run 11/11 reproduced, exit 0. | With `TMPDIR` correctly set outside the isolated clone: initial run reproduced 10/11, 0 mismatches, 1 unevaluable, exit 2 for that missing log. Source and clone log hashes matched the recorded SHA-256; after copying, rerun was 11/11 reproduced, 0 mismatches, 0 unevaluable, exit 0. | Match; the clone-only missing ignored output is an evidenced environmental disposition, not a silent pass or content mismatch. |
| `python3 reports/round-19/audit/coverage-audit.py` (R19 C09; 2026-10-18) | `r19-1.md`: 199 rows / 199 files, six of six partitions clean. | 199 rows / 199 files, six of six clean; per-partition rows and disk counts agree. | Match. |
| `git ls-tree -r --name-only e5718945a1ab0a0c3db955338d2cae77d68fd348 -- corpus/knowledge/verification corpus/knowledge/synthesis \| python3 -c 'import sys,collections; c=collections.Counter(p.split("/")[2] for p in sys.stdin if p.rstrip().endswith(".md")); print(dict(sorted(c.items())))'` (R19 C09; 2026-10-18) | `r19-1.md`: baseline counts `synthesis=24`, `verification=15`. | `{'synthesis': 24, 'verification': 15}`. | Match. |
| `git diff --name-status e5718945a1ab0a0c3db955338d2cae77d68fd348 HEAD -- corpus/knowledge/verification corpus/knowledge/synthesis` (R19 C09; 2026-10-18) | `r19-1.md`: ten Markdown additions, five per partition, with paths listed there. | Exactly the same ten paths: `synthesis/{era-material-scoped-reconciliation,finding-disposition-workflow,generated-artifact-lifecycle,hold-set-contract-in-brief,typed-label-routing-workflow}.md` and `verification/{gate-battery-surface-verification,generated-artifact-roundtrip-verification,label-channel-routing-verification,pre-declared-hold-set-reconciliation,two-reader-interop-agreement}.md`. | Match. |
| `python3 tools/check-gate-battery.py` (R19 C10; 2026-10-18) | `r19-2.md`: battery exit 0; 7 pass, 0 fail, 0 unevaluable; baseline exit 0, 18 found / 18 pinned, 9/9 registered gates covered. | Exit 0; same battery and baseline counts; 9 registered gates, 9/9 coverage, no findings. | Match. |
| `python3 - <<'PY'` baseline-file inventory script (R19 C10; 2026-10-18; full command below) | `r19-2.md`: 5 expected files under `tools/gates/expected`, 10 under `tools/gates/frozen`, 3 under `reports/round-9/baselines`, total 18. | Same root counts and total; the additional file is `tools/gates/expected/d4-typed-labels-check-gate/r20-post/expected.json`. | Match. |
| `git log -1 --format="%h %s" -- tools/gates/expected/d4-typed-labels-check-gate/r20-post/expected.json` (R19 C10; 2026-10-18) | `r19-2.md`: added by `35b6797` (`round-20: admit D/O/C`). | `35b6797 round-20: admit D/O/C — handoff v3 with D4, alias-wart closed, README reconciled`. | Match. |
| `python3 tools/gates/typed-pipeline-gate.py --selftest` (R19 C11; 2026-10-18) | `r19-3.md`: exit 0; selftest 12/12. | Exit 0; `selftest: 12/12 checks passed`. | Match. |
| `python3 - <<'PY'` SKILL subsection scan (R19 C12; 2026-10-18; full command below) | `r19-4.md`: current headings at lines 131 and 189; neither in baseline; five `###` sections. | Same headings and positions, both absent at baseline `e5718945a1ab0a0c3db955338d2cae77d68fd348`, five sections. | Match. |
| `ls corpus/knowledge/civilizations/*.md \| wc -l` (R20 C; 2026-10-18) | `reports/round-20/validation.json`: 94. | 94. | Match. |
| `ls corpus/knowledge/culture-material/*.md \| wc -l` (R20 C; 2026-10-18) | R20 receipt: 18. | 18. | Match. |
| `ls corpus/knowledge/linguistics/*.md \| wc -l` (R20 C; 2026-10-18) | R20 receipt: 19 live (the declared 20 is separately named as a delta). | 19. | Match; declared/live delta remains documented, not normalized. |
| `ls corpus/knowledge/myth-symbol/*.md \| wc -l` (R20 C; 2026-10-18) | R20 receipt: 19. | 19. | Match. |
| `ls corpus/knowledge/synthesis/*.md \| wc -l` (R20 C; 2026-10-18) | R20 receipt: 29. | 29. | Match. |
| `ls corpus/knowledge/verification/*.md \| wc -l` (R20 C; 2026-10-18) | R20 receipt: 20. | 20. | Match. |

The exact pipe-bearing commands shown with escaped separators in the table were independently executed on 2026-10-18:

```text
git ls-tree -r --name-only e5718945a1ab0a0c3db955338d2cae77d68fd348 -- corpus/knowledge/verification corpus/knowledge/synthesis | python3 -c 'import sys,collections; c=collections.Counter(p.split("/")[2] for p in sys.stdin if p.rstrip().endswith(".md")); print(dict(sorted(c.items())))'
ls corpus/knowledge/civilizations/*.md | wc -l
ls corpus/knowledge/culture-material/*.md | wc -l
ls corpus/knowledge/linguistics/*.md | wc -l
ls corpus/knowledge/myth-symbol/*.md | wc -l
ls corpus/knowledge/synthesis/*.md | wc -l
ls corpus/knowledge/verification/*.md | wc -l
```

The multiline scripts above were independently executed on 2026-10-18 as follows:

```text
python3 - <<'PY'
from pathlib import Path
for root in (Path('tools/gates/expected'), Path('tools/gates/frozen'), Path('reports/round-9/baselines')):
    files = sorted(root.rglob('expected.json')) if root.exists() else []
    print(root, len(files))
    for p in files:
        print(' ', p)
PY
```

```text
python3 - <<'PY'
import re, subprocess
from pathlib import Path
text = Path('SKILL.md').read_text()
want = ('Slot-label routing', 'Derivation replay')
headings = [line.removeprefix('### ').split(' — ', 1)[0] for line in text.splitlines() if line.startswith('### ')]
found = {name: [i for i, line in enumerate(text.splitlines(), 1) if line.startswith('### ' + name)] for name in want}
base = subprocess.run(['git', 'show', 'e5718945a1ab0a0c3db955338d2cae77d68fd348:SKILL.md'], text=True, capture_output=True, check=True).stdout
print('CURRENT_MATCHING_HEADINGS', {k: v for k, v in found.items()})
print('CURRENT_PRESENT', {k: bool(v) for k, v in found.items()})
print('BASELINE_MATCHING_HEADINGS', {k: [i for i, line in enumerate(base.splitlines(), 1) if line.startswith('### ' + k)] for k in want})
print('SECTION_COUNT', len(headings))
PY
```

## Finding and limits

Across the 23 distinct command strings, every recorded count, verdict, and exact-output digest selected here reproduced. The validator-equivalent source-command coverage check on 2026-10-18 imported `reports/round-21/run-validation.py`, called `command_sources()`, and applied its markdown-substring rule: 10 distinct source command strings matched this report, exceeding the eight-command minimum. The R18 frozen replay's one unevaluable row was reproduced and resolved by restoring the matching ignored log in the disposable clone, as its recount note states. A preliminary attempt with `TMPDIR` inside the clone was refused by the replay tool as `mirror_unsafe`; rerunning with the required lane `.scratch/` outside the clone produced the recorded 10/11 then 11/11 sequence. That was a harness-location correction, not a corpus mismatch. No independent discrepancy remains in this sample.

The source checkout's `git diff --name-status HEAD -- reports/round-{8..20}` and `git status --porcelain=v1 --untracked-files=all -- reports/round-{8..20}` were both empty on 2026-10-18T11:02:25-03:00. All receipt-writing/scratch effects and the copied ignored log were confined to disposable clones under `.scratch`; the only source-checkout file this seat wrote is this assigned audit report. Filed rounds 8–20 were not modified. No commit or push was made.
