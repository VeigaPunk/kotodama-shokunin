# R23-X07 — fragment conformance index

Axes: **O / operability** (the PLACEHOLDER_RE wording disposition and the
combined-source successor pins, each pin a new row with before/after digests);
**D / depth** (the family-clean projection rule drafted for SKILL.md, landed by
the orchestrator). Basis: `reports/round-23/claims.json` (declaration,
`state: declared-before-dispatch`; claims baseline revision `0e81d9d` =
round-22 close) and `reports/round-23/targets.json` (8 successor-pin / 4
wording / 4 D-rule seats). Lane HEAD at this index's draft: `7b181a5`. This is
the assigned X07 index, not a round-admission receipt or independent promotion
review. This seat's only filed write is this file.

## Reading this index

- **Indexed** means the named artifact existed at the census and its size and
  sha256 were read. It does not mean the whole claim passed, that a draft was
  integrated, or that a proposed control was executed.
- **Attributed** results belong to their source fragment; a row is an X07
  execution only where it says so. Seat attribution beyond the declaration
  files is inferred from name/path against `targets.json` and is not a launch
  or completion trace.
- **Draft / design / pending** are deliberate distinctions: a drafted rule is
  not a landed SKILL.md row; a proposed pin is not a verified replay; a runner
  on disk is not a green acceptance.
- Counts carry their command and date; quotations name their location; a
  missing required artifact is named, never inferred. No historical round
  validator is run for this index.
- Excluded from inventory (convention from R14/R20 indexes): paths under
  `__pycache__/` and `*.log` transcripts. Any such file present at
  census is named below so nothing is silently dropped:
- `reports/round-23/wording/__pycache__/wording-check.cpython-314.pyc` (29403 B, mtime 2026-10-18T15:25:12.693017+00:00)

## Census

Read-time census of `reports/round-23/**` at the moment this index was generated (see
**Index verification** for the reproducible command). **The wave was in flight at the census** (first artifact 2026-10-18T15:00:40.764216+00:00; census 2026-10-18T15:26:21.571860+00:00): a file arriving after it needs a dated refresh, not an inferred worker failure.

| artifact | axis / owner | size | sha8 | conformance state / limit |
|---|---|---|---|---|
| `reports/round-23/adjacency.md` | O/D/C (adjacency scribe; self-identifies SCRIBE X06) | 10634 B | c120de12 | Adjacency/connector fragment serving both tails; presence recorded, not independently re-executed here. |
| `reports/round-23/audit/x05-pins-spotcheck.md` | O/D/C (auditors) | 7076 B | a77652b8 | Audit fragment (spot-check / lessons audit); attributed evidence, not independently re-executed here. |
| `reports/round-23/audit/x09-lessons-audit.md` | O/D/C (auditors) | 12614 B | 0b9d4859 | Audit fragment (spot-check / lessons audit); attributed evidence, not independently re-executed here. |
| `reports/round-23/audit/x09-lessons-audit.py` | O/D/C (auditors) | 9515 B | ecdfa345 | Audit fragment (spot-check / lessons audit); attributed evidence, not independently re-executed here. |
| `reports/round-23/audit/x09-lessons-receipt.json` | O/D/C (auditors) | 16318 B | e7ce1d12 | Audit fragment (spot-check / lessons audit); attributed evidence, not independently re-executed here. |
| `reports/round-23/audit/x12-retro-spotcheck.md` | O/D/C (auditors) | 12411 B | c19ea46a | Audit fragment (spot-check / lessons audit); attributed evidence, not independently re-executed here. |
| `reports/round-23/claims.json` | O/D declaration | 1986 B | a8e2b7a6 | Declared thresholds and required outcomes, not achieved ones (`state: declared-before-dispatch`). |
| `reports/round-23/fragment-index-x08.md` | O/D/C (X08 scribe, sibling index) | 14199 B | 91b3249f | Seat-named suffixed twin index (R19/R20 collision lesson); presence/conformance index only; neither index settles the other. |
| `reports/round-23/fragment-index.md` | O/D/C (X07 scribe, this seat) | - | - | Presence/conformance index only; self-check confers no admission. Single assigned writer of this path (R20 collision pattern avoided by allocation; a sibling index would be a parent-owned disposition). |
| `reports/round-23/integration/fragment-ledger.json` | O/D/C (integration seat R23-D04) | 6020 B | e4f7d263 | Non-canon integration ledger / LOG-SCORECARD draft; parent-owned landing; admits nothing by itself. |
| `reports/round-23/integration/fragment-ledger.md` | O/D/C (integration seat R23-D04) | 4684 B | 57aefd53 | Non-canon integration ledger / LOG-SCORECARD draft; parent-owned landing; admits nothing by itself. |
| `reports/round-23/integration/ledger-gen.py` | O/D/C (integration seat R23-D04) | 10817 B | c087c0b7 | Non-canon integration ledger / LOG-SCORECARD draft; parent-owned landing; admits nothing by itself. |
| `reports/round-23/integration/log-draft.md` | O/D/C (integration seat R23-D04) | 5022 B | cb8b3f09 | Non-canon integration ledger / LOG-SCORECARD draft; parent-owned landing; admits nothing by itself. |
| `reports/round-23/integration/scorecard-draft.md` | O/D/C (integration seat R23-D04) | 3274 B | e255b6be | Non-canon integration ledger / LOG-SCORECARD draft; parent-owned landing; admits nothing by itself. |
| `reports/round-23/pins/d4frozen.md` | O (successor-pin seats, x8 per targets.json) | 3270 B | 6fa25975 | O fragment: combined-source successor pins as new rows with before/after digests; attributed evidence, not independently re-executed here. |
| `reports/round-23/pins/d4profile.md` | O (successor-pin seats, x8 per targets.json) | 3260 B | 35d298c4 | O fragment: combined-source successor pins as new rows with before/after digests; attributed evidence, not independently re-executed here. |
| `reports/round-23/pins/frozen.md` | O (successor-pin seats, x8 per targets.json) | 3541 B | 3015fea7 | O fragment: combined-source successor pins as new rows with before/after digests; attributed evidence, not independently re-executed here. |
| `reports/round-23/pins/r2-live.md` | O (successor-pin seats, x8 per targets.json) | 3838 B | bb1cd91d | O fragment: combined-source successor pins as new rows with before/after digests; attributed evidence, not independently re-executed here. |
| `reports/round-23/pins/table.md` | O (successor-pin seats, x8 per targets.json) | 5347 B | 4a2845e9 | O fragment: combined-source successor pins as new rows with before/after digests; attributed evidence, not independently re-executed here. |
| `reports/round-23/pins/v2.md` | O (successor-pin seats, x8 per targets.json) | 3287 B | a4cb7392 | O fragment: combined-source successor pins as new rows with before/after digests; attributed evidence, not independently re-executed here. |
| `reports/round-23/report-draft.md` | O/D/C (report scribe, by name) | 7935 B | 7792e48e | Explicit integration draft, not authorized final filing; the parent owns the round report. |
| `reports/round-23/rerun.json` | O/D/C (scribe seat, by name) | 16151 B | fa99ca72 | A scribe seat's bounded evidence record; attributed by name, not written by this seat and not independently verified here. |
| `reports/round-23/rule/fragment-D01.md` | D (rule seats, x4 per targets.json) | 4582 B | 732b554f | D fragment: family-clean projection rule drafted for SKILL.md (orchestrator lands); attributed evidence. |
| `reports/round-23/rule/fragment-D02.md` | D (rule seats, x4 per targets.json) | 5118 B | 1734e357 | D fragment: family-clean projection rule drafted for SKILL.md (orchestrator lands); attributed evidence. |
| `reports/round-23/rule/fragment-D03.md` | D (rule seats, x4 per targets.json) | 4360 B | 659ff387 | D fragment: family-clean projection rule drafted for SKILL.md (orchestrator lands); attributed evidence. |
| `reports/round-23/rule/skill-draft.md` | D (rule seats, x4 per targets.json) | 19897 B | 044655b8 | D fragment: family-clean projection rule drafted for SKILL.md (orchestrator lands); attributed evidence. |
| `reports/round-23/scope.md` | C (scope scribe; self-identifies SCRIBE X02) | 10166 B | fcf59e14 | Filed-artifact immutability / fleet-cleanliness watch; scoped observation, not round acceptance. |
| `reports/round-23/shonen-survey.md` | O/D/C (survey scribe, allocation by name) | 8704 B | d07fb10e | Survey fragment; presence recorded; seat attribution inferred from name, not a launch trace. |
| `reports/round-23/targets.json` | O/D declaration | 180 B | 817813ae | Seat allocation counts only; not a per-seat launch/completion trace. |
| `reports/round-23/wording/analysis.md` | O (wording seats, x4 per targets.json) | 7576 B | 8bd4d872 | O fragment: PLACEHOLDER_RE wording disposition; attributed evidence, not independently re-executed here. |
| `reports/round-23/wording/declared-in-r3/expected.json` | O (wording seats, x4 per targets.json) | 1330 B | 737e5484 | O fragment: PLACEHOLDER_RE wording disposition; attributed evidence, not independently re-executed here. |
| `reports/round-23/wording/declared-in-r3/packet.md` | O (wording seats, x4 per targets.json) | 107119 B | 084dc5db | O fragment: PLACEHOLDER_RE wording disposition; attributed evidence, not independently re-executed here. |
| `reports/round-23/wording/evidence/check-receipt.json` | O (wording seats, x4 per targets.json) | 6114 B | 8c2403ed | O fragment: PLACEHOLDER_RE wording disposition; attributed evidence, not independently re-executed here. |
| `reports/round-23/wording/wording-check.py` | O (wording seats, x4 per targets.json) | 18162 B | de8dc7ca | O fragment: PLACEHOLDER_RE wording disposition; attributed evidence, not independently re-executed here. |

**Census:** 34 artifacts including this index (excluding
`__pycache__/` and `*.log`); stamp 2026-10-18T15:26:21.571860+00:00. Arrivals by inferred owner
(file counts, not completion claims): D-rule: 4; O-successor-pins: 6; O-wording: 5; audits: 5; declarations: 2; integration (D04): 5; other: 2; scope/adjacency/survey: 3; scribe indexes: 2. The counting command
`python3 reports/round-23/run-validation.py` is
**absent** at census —
until it and its receipt land, neither claim has a runnable counting command
at the live revision.

## Conformance observations

1. **Declared, not achieved.** Both claims in `reports/round-23/claims.json`
   are `declared-before-dispatch`; nothing in this index converts a
   declaration into an achieved outcome. Counts in fragments belong to their
   own commands and dates.
2. **The parent integrates.** `LOG.md` had no round-23 entry at census
   (command: `grep -n 'round-23' LOG.md`, read-only, 2026-10-18) — workers
   file fragments only; LOG/SCORECARD appends and the SKILL.md landing are
   parent-owned (`reports/round-23/integration/log-draft.md` and
   `scorecard-draft.md` are drafts, not landings).
3. **Cross-round straggler (attributed; adjudicated by X02, dispositioned by
   the parent).** `reports/round-22/fixes/regression.md` differs from its
   filed blob in the working tree. This seat independently confirmed the
   modification existed (read-only `git status --porcelain` +
   `git diff -- reports/round-22/fixes/regression.md`, 2026-10-18T15:03Z) and
   did not touch it. `reports/round-23/scope.md` adjudicates it a round-22
   straggler (worktree mtime 14:59:32Z, after the round-22 close commit and
   before round-23 dispatch; no post-close commit touched any protected
   path). Whether to commit it as a late round-22 fragment or restore the
   filed bytes is the parent integrator's decision; content of the rewritten
   verdict is not certified by X02 or by this seat.
4. **Census coexistence (R20-collision pattern, disclosed).** Seat R23-D04
   files `reports/round-23/integration/fragment-ledger.md`, a read-time
   census of the same subtree that calls itself "the index the parent uses to
   integrate". This seat's assigned path is `fragment-index.md`; the paths do
   not collide, but the roles overlap. Neither census settles the other; a
   divergence between the two tables is a parent reconciliation item, not a
   verdict. (Precedent: R20's two index files, R21 `defects/fix-12.md`.)
5. **Attribution discrepancies noted for the parent.** The D04 ledger's
   owner-inference rules read self-identified seats as `unassigned`:
   `reports/round-23/scope.md` (header: SCRIBE X02) is row-marked
   "unassigned" in `integration/fragment-ledger.md`, and
   `reports/round-23/adjacency.md` (header: SCRIBE X06) matches the same
   shape per X08's index. This index attributes both by self-identification;
   the parent owns the reconciliation. Similarly, two index seats are in
   flight: X08 deliberately files the seat-named suffixed path (R19/R20
   collision lesson, per its own filing note) and X07 files the unsuffixed
   path assigned here; the two indexes' rows may diverge as the wave lands —
   divergence is a parent reconciliation item, not a verdict.
6. **Live derived surface modified in-tree at the stamp (attributed to the
   in-flight O seats, not adjudicated here).** `git status --porcelain` at
   the index stamp (2026-10-18, read-only) shows
   `M examples/culture-d2/expected-holds.json` alongside the round-22
   straggler of observation 3. Regenerating permitted live derived surfaces
   is inside claim O's successor-pin mandate
   (`reports/round-22/bleed/design.md`, "Integration obligations"); the
   landed pin rows must bind the regenerated bytes with before/after
   digests. This index neither ran nor verified that regeneration.
7. **Out-of-subtree landing surface.** The x09 lessons audit's receipt is
   indexed above, but its landing surface `corpus/lessons/round-23.md` lives
   outside `reports/round-23/` (untracked in git at the stamp) and is
   therefore not in this census, which walks only this round's subtree. The
   parent should integrate the pair, not the receipt alone.

## Index verification

X07 writes only this file. This stdout-only control verifies the delivered
index's path coverage, per-row size/sha8 bindings, duplicate/missing-entry
detection, nonempty artifacts, and Markdown shape. Negative controls are
in-memory: duplicate and dropped index rows must fail, a nonexistent path must
be detected, and a tampered sha8 must be detected. No fixture file is created.
A later-arriving artifact or a post-census fragment edit requires a dated
index refresh, not reuse of this receipt.

```sh
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
from datetime import datetime, timezone
from pathlib import Path
import hashlib, re
index = Path('reports/round-23/fragment-index.md')
text = index.read_text()
rows = re.findall(r'^\| `(reports/round-23/[^`]+)` \| [^|]+ \| ([0-9]+ B|-) \| ([0-9a-f]{8}|-) \|', text, re.M)
paths = [r[0] for r in rows]
actual = sorted(str(p) for p in index.parent.rglob('*')
                if p.is_file() and '__pycache__' not in p.parts
                and not p.name.endswith('.log'))
def conforms(pairs):
    names = [p for p, _ in pairs]
    ok_hash = all(
        s == '-' or hashlib.sha256(Path(p).read_bytes()).hexdigest()[:8] == s
        for p, s in pairs)
    return (len(names) == len(set(names)) and set(names) == set(actual)
            and ok_hash
            and all(Path(p).is_file() and Path(p).stat().st_size > 0
                    for p in names))
pairs = [(p, s) for p, _, s in rows]
print('observed_at=' + datetime.now(timezone.utc).isoformat())
print('indexed=' + str(len(paths)) + ' observed=' + str(len(actual)))
print('unindexed=' + repr(sorted(set(actual) - set(paths))))
print('unavailable=' + repr(sorted(set(paths) - set(actual))))
assert conforms(pairs), 'index inventory incomplete, stale, or invalid'
assert not conforms(pairs + [pairs[0]]), 'duplicate negative missed'
assert not conforms(pairs[1:]), 'dropped-row negative missed'
assert not conforms(pairs + [('reports/round-23/__X07_nonexistent__.md', '-')]), 'missing-path negative missed'
tampered = [(p, '00000000' if s != '-' else s) for p, s in pairs]
assert not conforms(tampered), 'tampered-sha negative missed'
assert text.endswith('\n') and '\0' not in text
assert all(line == line.rstrip() for line in text.splitlines()), 'trailing whitespace'
assert len(re.findall(r'^```[^\n]*$', text, re.M)) % 2 == 0, 'unbalanced fences'
print('INDEX_CONTROL=PASS; duplicate/drop/missing/tampered-sha negatives rejected')
PY
```
