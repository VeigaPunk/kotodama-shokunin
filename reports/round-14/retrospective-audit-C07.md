# R14-C07 — retrospective pointer audit

Axis: calibration / evidence traceability. Status: consolidated retrospective audited at SHA-256 `c1457e85320f3d4616e5029fed107f0ed4a12f49b41bb2b2d1927f5c3b0d413b`; see the final hash-bound audit below. All four delivered C07/C08 reproduction blocks passed at 2026-10-18T00:09:30Z. Earlier sections preserve dated in-flight observations. Resolving evidence citations are distinguished from explicitly disclosed historical missing-file gaps. No filed round runner was invoked.

## Source-map controls already completed

At 2026-10-17T23:59:51Z, a read-only Python loop loaded each round-8–13 `claims.json.baseline_revision` and called `git cat-file -e <revision>^{commit}`. Every declaration baseline resolved. The loop then called `git show -s --format='%H %s' <revision>` for the admission/rejection and amendment commits below; all resolved in this lane's Git object store.

- Final-state record pointers: `reports/round-8/validation.json`, `reports/round-9/validation.json`, `reports/round-10/validation.json`, `reports/round-11/validation.json`, `reports/round-12/validation.json`, and the operator-skip entry at `LOG.md:3077-3080`.
- Admission/rejection revisions: `e1694bad6ac96aca45a11ca5746582b275929355`, `9dc18ec1339bffd6f81e74f1a5742464ef578749`, `94ca098b8ab03be52ec80f6925538e5e2c0ed327`, `a3f6fcef2d92a1099581140c81d4264e9a4e2aa3`, `44070b4a6038f54e78d8d5be551e549fe202b0ee`.
- Amendment revisions: `51e590100f7bb3c2d30f5cc9e91a0ad981505179`, `94377884a78a73ad5396acb0d5f48a539a7a0448`, `3dba77a722c6a2e885447a47971205fd97c11605`.
- Round-11 denominator correction: `reports/round-12/recount/r11-1.md:9-17`, `reports/round-12/recount/r11-2.md:9-15`, `reports/round-12/recount/dispositions.md:77-79`. All paths and cited line ranges were read directly on 2026-10-17.
- Handoff semantics vs shape: `reports/round-12/adjacency/A11-A12-handoff.md:7-17` and `reports/round-12/adjacency/contract.md:9-11,27-32,44-48` resolve. These say the transfer is rejected / unproven despite a passing shape gate; they do not overturn round-12 admission.
- Immutable receipt mechanism: `reports/round-8/run-validation.py:99,1485-1486` and `reports/round-9/run-validation.py:127,1909-1910` resolve and name their filed output paths plus unconditional `write_text`. These were searched read-only on 2026-10-17T23:59:51Z, not executed.

## Pointer interpretation rules for the final audit

A local path will be checked as a file, its line/range if supplied, and its JSON key/Markdown heading when the retrospective cites one. A commit pointer will be checked in this repository's object store. A matching filename alone does not establish that a claim is supported; the cited material must preserve the distinction between historical final state, in-flight draft, current-tree recheck, and operator-reported dispatch.

Out-of-lane `.ufo` / fleet paths are **outside this assignment's read scope**. They must be presented as citations carried by a lane-local record, not as freshly verified paths. A claim requiring independent inspection of the fleet's file is `to-verify` for the authorized parent, not a nonexistent-file finding.

Historical source inconsistencies that a resolving pointer must not hide are detailed in `reports/round-14/retrospective-audit-C08.md`: the round-12 defect-status split, round-11 denominators, amendment counting boundary, and the difference between worker requests and a runtime dispatch trace.

## Pointer-control verification

A read-only Python presence/type/range probe ran at 2026-10-18T00:00:28Z (local date 2026-10-17). It loaded the round-8–13 declaration and target JSON files, verified Boolean `claims.<id>.passed` leaves in every round-8–12 validation receipt, and checked the cited skip / denominator line ranges against actual file line counts. All checks passed. Negative controls independently detected a nonexistent `reports/round-14/__C07_missing_negative__.json`, a nonexistent `__C07_missing_key__` in the round-11 receipt, and line 999999 outside round-11 claims. These controls do not create or mutate a planted file.

The C08 fragment's embedded reproduction command was extracted and executed verbatim with `subprocess.run(['bash', '-c', block])` on 2026-10-17T23:59:51Z; it exited 0 and reproduced the displayed historical counts. None of these controls imports or executes a filed round runner.

## Upstream shard audit

The retrospective shards landed during the dependency wait. At 2026-10-18T00:04:31Z (local date 2026-10-17), a read-only Python regex/path/range scan checked explicit repo-root path citations in `reports/round-14/retro/r8.md`, `r9.md`, `r10.md`, and `r11-13.md`. Distinct `(path, line locator)` counts were respectively 19, 22, 24, and 34; these are per-document scan populations, not unique sources across the whole retrospective. Existing line ranges resolved. The only missing explicit file was the already-disclosed `reports/round-12/adjacency/entries.md` in `retro/r11-13.md:219-229,299-301`.

**C07-F01 — underlying R12 entry pointers do not resolve.** This is honestly disclosed by the shard, not a broken claim that the shard possesses those receipts. Its read-only command confirms all original adjacency-ledger entry rows point to the absent path; the consolidated retrospective must retain that limitation and point to the real A11-A12 source-boundary review without calling it the missing assigned receipt. A future repair needs a new correction/evidence record and a positive path-resolution control; this auditor does not manufacture the missing historical file or rewrite the ledger.

At 2026-10-18T00:04:39Z, source shard SHA-256 values were:

- `reports/round-14/retro/r8.md`: `48594b8c523a2d5c0130d8ce178c5ffd48c83ca474a404965aa0a4b136f18892`.
- `reports/round-14/retro/r9.md`: `268931b2629e00c8d91427599a14ec11524019d4cd58a389c3eed6edf7a3a2d3`.
- `reports/round-14/retro/r10.md`: `35fe0615d1cc9ec1dbfff6a0d4ae17f89213467c8694ea81d1d3d08a5a7421b0`.
- `reports/round-14/retro/r11-13.md`: `3f24acdbaf15396106d5a22f4aef478b26cfad9929b8ecb6cdb41470cbb15d3b`.

Control: `python3` using `pathlib.Path.read_text`, a regex for repo-root `reports|tools|corpus|examples` paths plus LOG/SCORECARD/SKILL/SHONEN/PROVINCE, `Path.exists()`, and cited line-number bounds; hashes with `hashlib.sha256(Path.read_bytes())`. Glob/brace shorthand was excluded from the automatic literal-path population and interpreted against its named round context. The four shards' embedded read-only count controls were independently extracted and executed; all exited 0. This proves the shard measurements and disclosures, not a pass on the still-pending consolidated text.

## Final hash-bound pointer and claim audit

Audited deliverable: `reports/round-14/loop1-retrospective.md`, SHA-256 `c1457e85320f3d4616e5029fed107f0ed4a12f49b41bb2b2d1927f5c3b0d413b`, 428 lines, observed 2026-10-18T00:07:58Z and re-audited at 00:08:31Z. The dependency watcher first detected the draft at 00:05:22Z after seven 60-second intervals, within the 20-minute bound. The first snapshot's checks passed, but its stale digest was correctly rejected at 00:07:52Z after the scribe revised the text. The updated version removes the absent runner from executable-looking citations, locates the amendment wording, and records M2's result; it does not alter the historical measurements. This final binding supersedes that initial snapshot audit.

**Result: the retrospective's positive evidence citations resolve and its claim coverage is complete; an unqualified claim that every underlying historical pointer resolves would be false.** C07-F01 remains an explicitly disclosed historical provenance gap, not an audit failure hidden as green. The absent round-13 runner is correctly described as an absent declared deliverable, not cited as executable evidence.

- The final literal path/range scan found 79 distinct `(path, locator)` citations spanning 58 paths and checked 37 line-range occurrences. Every positive literal root-qualified citation resolves, and all cited existing ranges fit their files. No unexplained missing positive citation remains.
- The separate adjacency-ledger control confirms all ten original entry rows point to absent `reports/round-12/adjacency/entries.md`. The retrospective names this gap at lines 169–186 and 258 rather than pretending those receipts exist. Its real substitute evidence is separately attributed at `reports/round-12/adjacency/A11-A12-handoff.md:13,19-26,44-59`. A future new correction/evidence record remains the integrator's task.
- Each executed round's claim-ID set matches its original declaration exactly: round 8 F/O/D, round 9 F/O/D, round 10 C/F/O, round 11 D/O/F, round 12 C/O/A. Round 13's D/C/O are separately marked unexecuted/deferred. Thus all 15 measured claim rows and all three deferred declarations are covered without treating a stored PASS flag as proof of literal conformance.
- Manual source-content comparison retained the strict qualifications: round-8 repaired-live replay gap (lines 60–69), round-9 standard/default-root gap (81–96), round-10 retained stale-fixed assertion failures (108–116), round-11 unchanged F rejection and both denominators (138–158), and round-12 entry-receipt provenance gap / semantic handoff rejection (169–192). The six-class taxonomy is explicitly a grouping, not six incident counts.
- The resolving LOG/SCORECARD, declaration, receipt, shard, fix/erratum, and Git revision pointers support the described final states and corrections. Context-relative `r10-4.md`, `r11-2.md`, `r11-4.md`, and correction-file shorthand were checked in their named recount/round-14 directories. Fleet final-report attestations are explicitly carried through lane-local evidence, not newly verified outside the lane.

Reproduction command for the final citation/claim check (read-only; final observation 2026-10-18T00:08:31Z, local date 2026-10-17):

```sh
export TMPDIR="$PWD/.scratch"
python3 - <<'PY'
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json, re, subprocess
p = Path('reports/round-14/loop1-retrospective.md')
s = p.read_text()
assert sha256(p.read_bytes()).hexdigest() == 'c1457e85320f3d4616e5029fed107f0ed4a12f49b41bb2b2d1927f5c3b0d413b'
pat = re.compile(r'(?<![\w/])((?:reports|tools|corpus|examples)/[A-Za-z0-9_./{}*,\[\]-]+|(?:LOG|SCORECARD|SKILL|SHONEN|PROVINCE)\.md)(?::([0-9][0-9, -]*))?')
refs, missing, ranges = set(), set(), 0
for m in pat.finditer(s):
    path, locator = m.groups()
    path = path.rstrip('.,')
    if any(c in path for c in '{}*['):
        continue
    q = Path(path)
    refs.add((path, locator))
    if not q.exists():
        missing.add(path)
    elif locator and q.is_file():
        ranges += 1
        assert all(1 <= int(n) <= len(q.read_text().splitlines()) for n in re.findall(r'\d+', locator)), (path, locator)
assert not missing
assert (len(refs), len({x[0] for x in refs}), ranges) == (79, 58, 37)
for n in range(8, 14):
    section = re.search(rf'^## Round {n} —.*?(?=^## |\Z)', s, re.M | re.S).group()
    pattern = r'^\| ([DFOCA]) /' if n < 13 else r'^- \*\*([DFOCA]) /'
    ids = re.findall(pattern, section, re.M)
    declared = [x['id'] for x in json.loads(Path(f'reports/round-{n}/claims.json').read_text())['claims']]
    assert len(ids) == len(declared) and set(ids) == set(declared), (n, ids)
assert re.findall(r'^\| K([1-6]) —', s, re.M) == list('123456')
base = json.loads(Path('reports/round-14/claims.json').read_text())['baseline_revision']
a = json.loads(subprocess.check_output(['git', 'show', base + ':reports/round-12/adjacency/ledger.json']))
assert len(a['entries']) == 10
assert {x['filed_path'] for x in a['entries']} == {'reports/round-12/adjacency/entries.md'}
assert not Path('reports/round-12/adjacency/entries.md').exists()
for path in ('reports/round-12/recount/r10-4.md', 'reports/round-12/recount/r11-2.md',
             'reports/round-12/recount/r11-4.md', 'reports/round-14/fix-status-conflicts.md',
             'reports/round-14/fix-tracker-pointer.md', 'reports/round-14/fix-runner-hash.md',
             'reports/round-12/defects/fix-11.md'):
    assert Path(path).is_file(), path
print('C07 PASS: positive evidence paths/ranges and all declared claim IDs; explicitly disclosed absence retained')
print('citations', len(refs), 'paths', len({x[0] for x in refs}), 'ranges', ranges)
print('measured_at_utc', datetime.now(timezone.utc).isoformat())
PY
```

This result is bound to the named digest. Any later retrospective edit needs a fresh comparison. No retrospective, historical artifact, tool, shared LOG/SCORECARD, or sibling path was written by this auditor; only the assigned C07/C08 fragments changed. Overall round-14 acceptance and the remaining integration obligations are not asserted here.
