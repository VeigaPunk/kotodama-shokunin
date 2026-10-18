# R23-X08 — availability + conformance index

Seat **R23-X08** (scribe: availability + conformance index) for round 23 (operator: loop 2, GLM round 1 of 2; 16 workers — `reports/round-23/targets.json`: O-successor-pins 8, O-wording 4, D-rule 4). Axes watched: **O / operability** (the two round-22 tails: PLACEHOLDER_RE wording false positive; combined-source successor pins) and **D / depth** (the family-clean projection rule drafted for SKILL.md). This is the assigned X08 index — an availability read plus a presence/conformance census — not a round-admission receipt, not a verdict replay, and not an independent promotion review. The lane declaration remains `reports/round-23/claims.json` (baseline `0e81d9d9…` = the round-22 close; counting command for both claims: `python3 reports/round-23/run-validation.py`). No round validator was executed for this index; no filed rounds 8–22 artifact was read as writable, and none was modified.

Filing note: this index files at the seat-named path (the round-19/round-20 collision lesson, X28-1 / X24-L1); the R23-D04 fragment ledger under `integration/` is a separate parent-owned artifact and is indexed here, not edited.

## Reading this index

- **Indexed** means the named artifact existed at the census and its size and sha256 were read. It does not mean the claim passed, a draft was integrated, or a control was executed.
- **Attributed** results belong to their source fragment; a row is an X08 execution only where it says so.
- **Draft / declared / in-flight** are deliberate distinctions: a landed draft is not a landing; a declared threshold is not an achieved outcome; an arrived fragment is not a completed seat.
- Counts carry their command and date; quotations name their location; a missing required artifact is named, never inferred.

## Availability (at the census stamp)

- Census: **2026-10-18T15:23:40Z** (command: `python3 -B .scratch/x08/gen-index.py`; `__pycache__/`, `*.pyc`, `*.log` excluded; this index file is the self row, written after the census, never self-measured). Lane HEAD `7b181a52eb74…` (the round-23 declaration commit).
- **Counting command** `python3 reports/round-23/run-validation.py` — absent at census — until it lands, neither round-23 claim has a runnable counting command (`reports/round-23/claims.json:15,22`). Marker for the control: `runner_present_at_census=N`.
- **Runner receipt** `reports/round-23/validation.json` — absent at census. The round-20 lesson holds: a receipt that does not bind to the live runner bytes is a superseded receipt, and the close must re-run at the final revision.
- **Seat-plan arrivals** (file counts by inferred owner, not completion claims): O successor pins 0, O-wording 4, D-rule 4. The wave was in flight at the census: a file arriving after it needs a dated refresh, not an inferred worker failure.
- **Integration drafts** named by the D04 ledger (`integration/log-draft.md`, `integration/scorecard-draft.md`): log-draft present, scorecard-draft present at census — parent-owned landing inputs, indexed here, not edited.
- **D-rule landing surface**: `SKILL.md` does not contain a family-clean rule at census (`grep family-clean SKILL.md`) — the orchestrator lands the drafted rule; workers file drafts only.
- **Protected surface** (rounds 8–22, `git status --porcelain=v1` over `reports/round-{8..22}` at the census): exactly the one disclosed round-22 straggler (`M reports/round-22/fixes/regression.md`, uncommitted, adjudicated in `reports/round-23/scope.md` — a round-22 straggler, not a round-23 write); disposition is the parent integrator's.
- **Fleet root** `/home/vgpnk/Projects/shokunin`: clean (the fleet `.gitignore` ignores `*-shokunin/`; cleanliness of ignored lane files is not implied).

## Conformance census

24 artifacts indexed at 2026-10-18T15:23:40Z; every row carries bytes, sha8, mtime UTC, inferred owner seat, and conformance state. Owner-seat inference follows the R23-D04 ledger rules; `unassigned` is never guessed.

| artifact | bytes | sha8 | mtime UTC | owner seat | conformance state / limit |
|---|---:|---|---|---|---|
| `reports/round-23/adjacency.md` | 10634 | `c120de12` | 15:15:59 | unassigned | Header self-identifies as SCRIBE X06 (adjacency/connector scribe), serving claim O's two tails; the D04 owner rules read this shape `unassigned` — parent reconciliation item, attributed here only from the fragment's own header. |
| `reports/round-23/audit/x05-pins-spotcheck.md` | 7076 | `a77652b8` | 15:11:15 | auditors | Audit fragment; attributed evidence, not independently re-executed here. |
| `reports/round-23/audit/x09-lessons-audit.md` | 12614 | `0b9d4859` | 15:13:50 | auditors | Audit fragment; attributed evidence, not independently re-executed here. |
| `reports/round-23/audit/x09-lessons-audit.py` | 9515 | `ecdfa345` | 15:10:51 | auditors | Audit fragment; attributed evidence, not independently re-executed here. Attributed to the auditors from the sibling audit .md and content; the D04 name rules read this shape `unassigned` — parent reconciliation item. |
| `reports/round-23/audit/x09-lessons-receipt.json` | 16318 | `e7ce1d12` | 15:11:17 | auditors | Audit fragment; attributed evidence, not independently re-executed here. Attributed to the auditors from the sibling audit .md and content; the D04 name rules read this shape `unassigned` — parent reconciliation item. |
| `reports/round-23/audit/x12-retro-spotcheck.md` | 12411 | `c19ea46a` | 15:17:00 | auditors | Audit fragment; attributed evidence, not independently re-executed here. |
| `reports/round-23/claims.json` | 1986 | `a8e2b7a6` | 15:00:40 | declaration (parent) | Declared thresholds and seat allocation, not achieved outcomes (`state: declared-before-dispatch`). |
| `reports/round-23/fragment-index.md` | 12749 | `20f11d88` | 15:22:42 | X scribes (report/index) | Scribe fragment; this file is the seat's own index row. |
| `reports/round-23/integration/fragment-ledger.json` | 6020 | `e4f7d263` | 15:21:54 | integration (R23-D04 fragment ledger) | NON-CANON read-time census ledger; admits nothing. |
| `reports/round-23/integration/fragment-ledger.md` | 4684 | `57aefd53` | 15:21:54 | integration (R23-D04 fragment ledger) | NON-CANON read-time census ledger; admits nothing. |
| `reports/round-23/integration/ledger-gen.py` | 10817 | `c087c0b7` | 15:20:50 | integration (R23-D04 fragment ledger) | NON-CANON read-time census ledger; admits nothing. |
| `reports/round-23/integration/log-draft.md` | 5022 | `cb8b3f09` | 15:17:48 | integration (R23-D04 fragment ledger) | NON-CANON read-time census ledger; admits nothing. |
| `reports/round-23/integration/scorecard-draft.md` | 3274 | `e255b6be` | 15:18:03 | integration (R23-D04 fragment ledger) | NON-CANON read-time census ledger; admits nothing. |
| `reports/round-23/rule/fragment-D01.md` | 4582 | `732b554f` | 15:14:44 | D-rule | D-rule fragment; attributed draft from reports/round-22/bleed/design.md — SKILL.md landing is the orchestrator's. |
| `reports/round-23/rule/fragment-D02.md` | 5118 | `1734e357` | 15:14:44 | D-rule | D-rule fragment; attributed draft from reports/round-22/bleed/design.md — SKILL.md landing is the orchestrator's. |
| `reports/round-23/rule/fragment-D03.md` | 4360 | `659ff387` | 15:14:44 | D-rule | D-rule fragment; attributed draft from reports/round-22/bleed/design.md — SKILL.md landing is the orchestrator's. |
| `reports/round-23/rule/skill-draft.md` | 19897 | `044655b8` | 15:14:44 | D-rule | D-rule fragment; attributed draft from reports/round-22/bleed/design.md — SKILL.md landing is the orchestrator's. |
| `reports/round-23/scope.md` | 10166 | `fcf59e14` | 15:09:11 | scope auditor (X02) | Scope watch; attributed evidence — PASS verdict with one disclosed inherited deviation, not re-executed here. |
| `reports/round-23/shonen-survey.md` | 8704 | `d07fb10e` | 15:16:26 | unassigned | Header self-identifies as SCRIBE X11 (SHONEN-box evidence survey for round 24's promotion review); the D04 owner rules read this shape `unassigned` — parent reconciliation item, attributed here only from the fragment's own header. |
| `reports/round-23/targets.json` | 180 | `817813ae` | 15:00:40 | declaration (parent) | Declared thresholds and seat allocation, not achieved outcomes (`state: declared-before-dispatch`). |
| `reports/round-23/wording/analysis.md` | 7576 | `8bd4d872` | 15:23:35 | O-wording | O-wording fragment; attributed evidence — disposition draft/receipt, no placeholder rule weakened. |
| `reports/round-23/wording/declared-in-r3/expected.json` | 1330 | `737e5484` | 15:21:18 | O-wording | O-wording fragment; attributed evidence — disposition draft/receipt, no placeholder rule weakened. |
| `reports/round-23/wording/declared-in-r3/packet.md` | 107119 | `084dc5db` | 15:19:02 | O-wording | O-wording fragment; attributed evidence — disposition draft/receipt, no placeholder rule weakened. |
| `reports/round-23/wording/wording-check.py` | 16882 | `d41a8463` | 15:22:29 | O-wording | O-wording fragment; attributed evidence — disposition draft/receipt, no placeholder rule weakened. |
| `reports/round-23/fragment-index-x08.md` | — | — | — | X scribes (report/index) | This file (self row; size/sha not self-measurable at write time — the control below checks its presence and shape). |

**Census:** 24 indexed + 1 self row.

## Conformance observations

- **Tail arrivals at census** — wording disposition: files under wording/ (wording/analysis.md, wording/declared-in-r3/expected.json, wording/declared-in-r3/packet.md, wording/wording-check.py); combined-source successor pins: none yet; family-clean rule drafts: files under rule/. Arrival is not clearance: each tail's outcome belongs to the counting command and its receipt.
- The two round-22 tails this round owes: no successor-pin row, wording disposition, or D-rule draft may claim claim-level clearance here; the counting command and its receipt govern that, and their availability is recorded above, not assumed.
- The R23-D04 ledger (census 15:08:18Z, `fragment_count` 4 at that stamp) predates the arrivals indexed here; its own reading rule already requires a dated refresh on the settled tree — the two indexes must not be merged.
- Round-22 close state, for binding: round 22 closed REJECTED on D (fleet HEAD `3335751…`, "close kotodama round-22: REJECTED on D"); the bleed recipe lives at `reports/round-22/bleed/` (`design.md`, `skill-rule-draft.md`, `repin.md`).
- Filing, scope, integration into `LOG.md`/`SCORECARD.md`, the straggler disposition, and any final promotion verification remain parent responsibilities.

## Index verification

X08 writes only this file. The stdout-only control re-derives the index inventory against the live tree (this file excluded), re-hashes every indexed file, re-checks the runner-availability marker, and runs in-memory negatives (duplicate row, dropped row, nonexistent path) plus Markdown shape checks. No file is written; no validator is executed. A later-arriving artifact, a drifted digest, or a runner landing after the census invalidates the reading and requires a dated refresh.

```sh
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
#!/usr/bin/env python3
"""R23-X08 index verification — stdout-only, read-only, in-memory negatives.

Verifies the delivered reports/round-23/fragment-index-x08.md:
  1. census-table coverage == observed files (index itself excluded),
  2. digest/byte columns match the live files it rows,
  3. availability claims re-derive true (runner/receipt presence states),
  4. negative controls: duplicate row, dropped row, nonexistent path must fail,
  5. Markdown shape: balanced fences, no trailing whitespace, final newline.
No file is written; no validator is executed.
"""
import datetime, hashlib, re, sys
from pathlib import Path

INDEX = Path('reports/round-23/fragment-index-x08.md')
BASE = Path('reports/round-23')
text = INDEX.read_text()
rows = re.findall(r'^\| `(reports/round-23/[^`]+)` \| (\d+) \| `([0-9a-f]{8})', text, re.M)
def observed():
    return sorted(
        str(p) for p in BASE.rglob('*')
        if p.is_file()
        and '__pycache__' not in p.parts
        and not p.name.endswith(('.pyc', '.log'))
        and p != INDEX
    )
actual = observed()
names = [r[0] for r in rows]
def conforms(ns):
    return (len(ns) == len(set(ns)) and set(ns) == set(actual)
            and all(Path(p).is_file() and Path(p).stat().st_size > 0 for p in ns))
print('observed_at=' + datetime.datetime.now(datetime.timezone.utc).isoformat())
print(f'indexed={len(rows)} observed={len(actual)}')
print('unindexed=' + repr(sorted(set(actual) - set(names))))
print('unavailable=' + repr(sorted(set(names) - set(actual))))
assert conforms(names), 'index inventory incomplete or invalid'
# digest/bytes re-derivation for every indexed file
mismatch = []
for path, size, sha12 in rows:
    data = Path(path).read_bytes()
    if len(data) != int(size) or hashlib.sha256(data).hexdigest()[:8] != sha12:
        mismatch.append(path)
print('digest_mismatch=' + repr(mismatch))
assert not mismatch, 'indexed bytes/digest drifted from live files'
# availability claims embedded in the index
runner = BASE / 'run-validation.py'
receipt = BASE / 'validation.json'
m = re.search(r'runner_present_at_census=(\w+)', text)
assert m, 'availability line missing'
claim_runner = m.group(1) == 'Y'
print(f'runner_indexed={claim_runner} runner_now={runner.is_file()}')
assert claim_runner == runner.is_file(), 'index stale: runner presence drifted since census'
# negative controls (in memory only)
assert not conforms(names + [names[0]]), 'duplicate negative missed'
assert not conforms(names[1:]), 'dropped-row negative missed'
assert not conforms(names + ['reports/round-23/__X08_nonexistent__.md']), 'missing-path negative missed'
# shape
assert text.endswith('\n') and '\0' not in text
assert all(line == line.rstrip() for line in text.splitlines()), 'trailing whitespace'
assert len(re.findall(r'^```[^\n]*$', text, re.M)) % 2 == 0, 'unbalanced fences'
print('INDEX_CONTROL=PASS; duplicate/drop/missing negatives rejected; digests match; availability state current')
PY
```
