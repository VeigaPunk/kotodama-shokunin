# R22-C07 — retrospective pointer audit

Axis: calibration / evidence traceability. Scope: the round-22 loop-2 retrospective, not admission or promotion. Date: 2026-10-18. **Positive evidence pointers PASS; strict all-local-path completion is BLOCKED only by the explicitly parent-owned future `reports/round-22/routed-resolution.json`.** Audited retrospective SHA-256: `4966516923f3b8e6bc4bba8d203607ee2e76fa51c4154024c93892525ef501a1`. C07-F01/C08-F07 is fixed by the owner and independently controlled. Earlier sections retain dated in-flight observations; the final handoff below states the one parent action still needed.

## Source controls and integration requirements

Read-only `git show <revision>:reports/round-<n>/validation.json` byte comparisons passed against all five closure revisions: R17 `3dd3754207032cb81f5fb3e202fe85cf79211339`, R18 `e5718945a1ab0a0c3db955338d2cae77d68fd348`, R19 `caf1beac19b55f3bbce47e4a9e7e8710cc1c581d`, R20 `35b6797b42d48bec52e1e3ddba1f3afc9bb85046`, R21 `46a03257ee75dd8f685a105e47da3f45a0154172`. Every revision resolves in the lane's object store. These are historical receipt bindings, not reruns of their validators.

The retrospective must preserve these distinctions when choosing resolving evidence:

- R17's filed receipt reports C/O pass and D fail, with missing-artifact failures. Its closure prose additionally diagnoses the D2-bound identity gate. Neither an in-flight draft nor a later successful D4 run retroactively admits R17.
- R18's delivered pipeline really was verified: `reports/round-21/recount/r18-1.md:3-7` reproduces 19/19, `r18-2.md:3-7` reproduces D2 16/16, `r18-3.md:3-8` proves default-D2 stdout byte identity, and `r18-4.md:3-11` separates the ignored-log prerequisite from the final 11/11 replay.
- That architectural repair is not proof the original D4 declaration was satisfied. `reports/round-17/reviews/review-4.md:41-49,142-168` records the competing 6/0/0 and 17/1/0 declarations. `reports/round-18/d4/holds.md:131-180,208-231` explicitly reports a delivered 15-hold/1-note set, D2 rank carry, and an owner decision still owed. A citation to that reconciliation cannot be represented as an explicit parent decision.
- The original R18 D4 frozen generation and the R18 repin-D2 successor are different manifests. `reports/round-18/d4/replay.md:70-79` discloses live-peer dependence and the missing typed-packet row. R21's successful 11/11 repin-D2 replay is not proof the old two-row D4 generation still reproduces.
- `reports/round-21/recount/dispositions.md:5-9` calls the clone-snapshot mechanism unproven, whereas `reports/round-21/report-draft.md:11` and the recount ledger identify an absolute `.scratch` path scanner. A new R22 control must resolve this disagreement; do not silently choose the stronger hypothesis.
- `reports/round-19/availability.json:16-25` leaves completion unknown, while `LOG.md:3260-3270` reports 17/64 and says the availability record was closed. Report these as separate source channels; the LOG statement is not an independently observed dispatch receipt.
- Lane-local final reports are not established by drafts. R18 has no lane-local report draft at the checked canonical path; R19/R20 drafts explicitly reserve final filing to the parent. External final-report pointers, if not locally verifiable, must remain attributed/to-verify rather than be certified as freshly inspected.
- `SCORECARD.md:242` calls loop 2 complete at R21, but the amended schedule at `LOG.md:3073-3080` still assigns loop 2 to rounds 17–24. A retrospective through R21 is a build/verify checkpoint, not proof rounds 22–24 completed.

The amendment pointers `51e5901`, `9437788`, and `3dba77a` resolve; `git show -s --format='%H %ad %s' --date=iso-strict <revision>` ran 2026-10-18T14:40:37Z. Their structural-versus-provider counting boundary is audited separately in C08.

## Final-control contract

When the consolidated file lands, check every positive local path, explicit line/range, JSON selector, Markdown heading and Git revision against its actual source; expand contextual shorthand rather than treating it as a literal filename. Explicitly disclosed historical absence is a limitation, not a fabricated positive receipt. Source-file existence alone does not establish support for its associated assertion.

Controls must reject a nonexistent path, an out-of-range line, a missing JSON key, a missing heading and an invalid Git revision without creating fixtures. Bind the final result to the consolidated file's SHA-256 and recheck the digest after any independently executed read-only count blocks. The source census and final numeric controls are in `reports/round-22/retrospective-audit-C08.md`.

## Pointer-control verification

At 2026-10-18T14:42:02Z, a read-only Python probe accepted a real file, a real line, `claims.D.passed` in the R17 receipt, `0. Verdict` in the R18 holds report and the R21 admission revision. It rejected a nonexistent path, line 999999, an absent JSON key, an absent heading and the zero Git revision. No planted file was created. At 14:42:36Z, a literal positive-path/range scan of this initial fragment resolved 11 distinct citations across 10 paths, with no missing file or out-of-range locator.

Reproduction of the positive/negative pointer controls (read-only; observed 2026-10-18):

```sh
export TMPDIR="$PWD/.scratch"
python3 - <<'PY'
from pathlib import Path
from datetime import datetime, timezone
import json, subprocess
print('AUDIT_UTC', datetime.now(timezone.utc).isoformat())
def file_ok(p):
    return Path(p).is_file()
def line_ok(p, n):
    return file_ok(p) and 1 <= n <= len(Path(p).read_text().splitlines())
def key_ok(p, parts):
    try:
        v = json.loads(Path(p).read_text())
        for k in parts:
            v = v[k]
        return True
    except (OSError, KeyError, TypeError):
        return False
def heading_ok(p, heading):
    return any(s.lstrip('#').strip() == heading for s in Path(p).read_text().splitlines() if s.startswith('#'))
def revision_ok(rev):
    return subprocess.run(['git', 'cat-file', '-e', rev + '^{commit}'], stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL).returncode == 0
p = 'reports/round-17/validation.json'
h = 'reports/round-18/d4/holds.md'
checks = {
    'real_file': file_ok(p),
    'absent_file_rejected': not file_ok('reports/round-22/__C07_missing_negative__.json'),
    'real_line': line_ok(p, 1),
    'absent_line_rejected': not line_ok(p, 999999),
    'real_key': key_ok(p, ['claims', 'D', 'passed']),
    'absent_key_rejected': not key_ok(p, ['claims', '__C07_missing_key__']),
    'real_heading': heading_ok(h, '0. Verdict'),
    'absent_heading_rejected': not heading_ok(h, '__C07_missing_heading__'),
    'real_revision': revision_ok('46a03257ee75dd8f685a105e47da3f45a0154172'),
    'absent_revision_rejected': not revision_ok('0000000000000000000000000000000000000000'),
}
assert all(checks.values()), checks
print('C07 pointer controls PASS', checks)
PY
```

## First consolidated pointer audit

At 2026-10-18T14:43:37Z, the retrospective at SHA-256 `16b66788d4af85a8f924c4aaa3f300dc0f36353d82ed470110aa357ae693ae9f` (311 lines) passed both embedded M1/M2 commands, executed concurrently and with its bytes unchanged across execution. The root-qualified path scan found 42 distinct `(path, line locator)` citations over 33 paths and 12 line-range occurrences; every cited existing range fit its file. All 13 distinct backtick Git revision pointers resolved.

The only missing literal path at that observation was `reports/round-22/routed-resolution.json`, explicitly identified by the retrospective as a parent-owned integration target rather than an already-filed control. This is not a fabricated positive historical receipt. Its eventual presence is being checked at 60-second intervals before a final unqualified local-pointer conclusion. The generic `reports/round-N/run-validation.py` and `{n}` code templates were expanded over R17–R21, not treated as missing filenames. Context-relative recount ranges (`r18-1.md`–`r18-4.md`, `r19-1.md`–`r19-4.md`) resolve in the named R21 recount directory.

Content cross-checks preserve the needed boundaries: original R17 rejection versus later repair; 6/0/0 versus 17/1/0 versus delivered 15/1/0 hold contracts; original R18 D4 replay versus D2 successor; R19 baseline/availability provenance; filed versus current census; and a R17–R21 checkpoint rather than full R17–R24 completion. The new R17 scanner note is a resolving, bounded control, not an archived receipt rewrite. R18 holds sections 2–5 and 7 and R20 ledger-snapshot sections 1–2 exist and support the attributed qualifications; the claims and JSON selectors exercised by M1 resolve.

**C07-F01 / C08-F07 — CLOSED by the retrospective owner.** The first delivered M1 counted three axis claims without deriving the six-item O count attributed to it. The later M1 now extracts the O declaration's six numbered markers, asserts exactly `(1)`–`(6)` and prints the count; the independent rerun at 2026-10-18T14:47:00Z passes. The total was always six; this fixes its control attribution without changing the worklist or historical numbers.

## Updated integrated draft and upstream shards

At 2026-10-18T14:47:00Z, the integrated retrospective SHA-256 was `4966516923f3b8e6bc4bba8d203607ee2e76fa51c4154024c93892525ef501a1` (368 lines). Both M1/M2 blocks and all four upstream shard blocks were executed concurrently; all six exited 0 with their document bytes unchanged. The updated retrospective incorporates the new R17 scanner disposition and named R18 replay supersession, while retaining original recorded outcomes and generation boundaries.

Literal pointer/range scan populations at that same observation (per document, not distinct across the whole set):

- Consolidation: 49 distinct citations / 39 paths / 13 range occurrences; the only absent path is the explicitly future parent integration target.
- `reports/round-22/retro/r17.md`: 19 citations / 18 paths / 11 ranges; all existing.
- `reports/round-22/retro/r18.md`: 17 citations / 17 paths / 3 ranges; all existing.
- `reports/round-22/retro/r19.md`: 15 citations / 14 paths / 5 ranges; all existing.
- `reports/round-22/retro/r20-21.md`: 14 citations / 14 paths / 4 ranges; all existing.

Brace/dynamic templates and indexed-path expressions were checked separately against their stated round/key context; their exclusion from the literal scan does not imply they are unverified. The C08 control reruns the shard commands and historical JSON selectors rather than treating prose counts as measurements. The provider shard's time differences are Git declaration-to-close intervals, explicitly not inference latency; final-report/dispatch gaps are attributed rather than represented as resolving independent receipts.

At 14:46:18Z, an additional independent reproduction of `reports/round-22/fixes/snapshot-r17.md` imported the historical scanner module **only inside a fresh in-lane isolated clone**, without calling the full validator or its writer. It reproduced complete 16-file evidence, zero original scan, 16/7/5 relative-root control and zero changes to 1,030 protected clone paths. Thus the earlier no-import statement applies to the initial read-only census; this later bounded import is explicitly isolated and does not rewrite a filed receipt.

The live protected-surface control at 14:46:18Z independently compared all 1,018 filed R8–R21 paths with the R22 baseline, including Git blob bytes and file mode: zero mismatches and empty protected status. The SHA-256 manifest was `8eaa73b290eb0b85240b79d91d8f2cb5d41b77d2e009003be0072e699a896ff4`; an in-memory appended-byte negative was detected without writing a fixture.

## Digest-bound final pointer control

The updated hash was accepted and the stale first-draft hash rejected at 2026-10-18T14:48:13Z. All 14 Git revision pointers, generic per-round file templates, contextual recount ranges and named source sections passed. The strict replay below additionally requires the parent integration target to exist; until it lands, that last condition is explicitly pending rather than reported green.

```sh
export TMPDIR="$PWD/.scratch"
python3 - <<'PY'
from pathlib import Path
from hashlib import sha256
from datetime import datetime, timezone
import json, re, subprocess
p = Path('reports/round-22/loop2-retrospective.md')
s = p.read_text()
expected = '4966516923f3b8e6bc4bba8d203607ee2e76fa51c4154024c93892525ef501a1'
assert sha256(p.read_bytes()).hexdigest() == expected
assert expected != '16b66788d4af85a8f924c4aaa3f300dc0f36353d82ed470110aa357ae693ae9f'
pat = re.compile(r'(?<![\w/])((?:reports|tools|corpus|examples)/[A-Za-z0-9_./{}*,\[\]-]+|(?:LOG|SCORECARD|SKILL|SHONEN|PROVINCE)\.md)(?::([0-9][0-9, -]*))?')
refs, missing, ranges = set(), set(), 0
for m in pat.finditer(s):
    path, locator = m.groups()
    path = path.rstrip('.,')
    if any(c in path for c in '{}*[') or 'round-N/' in path:
        continue
    q = Path(path)
    refs.add((path, locator))
    if not q.exists():
        missing.add(path)
    elif locator and q.is_file():
        ranges += 1
        assert all(1 <= int(n) <= len(q.read_text().splitlines()) for n in re.findall(r'\d+', locator)), (path, locator)
assert (len(refs), len({x[0] for x in refs}), ranges) == (49, 39, 13)
assert not missing, ('unresolved local pointer', sorted(missing))
json.loads(Path('reports/round-22/routed-resolution.json').read_text())
revisions = set(re.findall(r'`([0-9a-f]{7,40})`', s))
assert len(revisions) == 14
for rev in revisions:
    subprocess.run(['git', 'cat-file', '-e', rev + '^{commit}'], check=True)
for n in range(17, 22):
    for kind in ('claims.json', 'validation.json', 'run-validation.py'):
        assert Path(f'reports/round-{n}/{kind}').is_file()
for prefix in ('r18', 'r19'):
    for i in range(1, 5):
        assert Path(f'reports/round-21/recount/{prefix}-{i}.md').is_file()
for path, want in [('reports/round-18/d4/holds.md', {'2','3','4','5','7'}),
                   ('reports/round-20/ledger-snapshot.md', {'1','2'})]:
    assert want <= set(re.findall(r'^## (\d+)\.', Path(path).read_text(), re.M))
print('C07 final pointer control PASS', datetime.now(timezone.utc).isoformat())
print('sha256', expected, 'citations', len(refs), 'paths', len({x[0] for x in refs}), 'ranges', ranges, 'revisions', len(revisions))
PY
```

## Final handoff — 2026-10-18T14:51:38Z

**All 48 positive existing citations over 38 existing paths resolve; all 13 explicit range occurrences and 14 revision pointers pass.** The 49th literal citation / 39th path is the explicitly future parent-owned `reports/round-22/routed-resolution.json`. The strict final replay was executed from this delivered fragment and exited 1 **only** with `('unresolved local pointer', ['reports/round-22/routed-resolution.json'])`; this is preserved as a real pending integration condition, not called green. The positive/negative pointer block passed.

The retrospective itself states that the parent owns routed-resolution integration. The 60-second dependency watch ran from 14:45:00Z until 14:50:58Z, then was stopped once this parent-after-handoff ownership was confirmed; waiting for a parent-created artifact would withhold the very handoff needed to create it. **Parent action:** file the assigned resolution JSON, then execute the strict final block above. If the retrospective digest changes, re-audit it and update the binding before claiming all-local-pointer completion.

All three delivered C08 blocks passed concurrently at 14:51:38Z, including the eight-control replay. A fresh live protected-byte/mode comparison again found **1,018 baseline matches, zero mismatches, empty protected status**, and manifest `8eaa73b290eb0b85240b79d91d8f2cb5d41b77d2e009003be0072e699a896ff4`. Both audit fragments passed whitespace checks. No full historical validator, shared bookkeeping edit, commit, push or out-of-lane write occurred; bounded scanner/replay effects were confined to fresh in-lane scratch clones. There is no background task left running.

This is a complete evidence audit with one explicitly blocked parent integration condition, not an assertion of overall round-22 acceptance or strict all-literal-pointer success.
