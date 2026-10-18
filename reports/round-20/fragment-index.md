# R20-X20 — fragment conformance index

Axes: **D / depth** (the handoff-e2e v3 design fragments and the claims map);
**O / operability** (the per-family era-alias resolution and the re-pin
cascade); **C / coverage** (the corpus README reconciliation and its receipts).
This is the assigned X20 index, not a round-admission receipt or independent
promotion review. The lane declaration remains `reports/round-20/claims.json`;
work allocation remains `reports/round-20/targets.json`.

## Reading this index

- **Indexed** means the named artifact existed at the census and its size and
  sha256 were read. It does not mean the whole claim passed, that a draft was
  integrated, or that a proposed control was executed.
- **Attributed** results belong to their source fragment; a row is an X19/X20
  execution only where it says so.
- **Draft / design / pending** are deliberate distinctions. A landed draft is
  not a landing; a proposed check is not a pass; a baseline pin is not a
  verdict replay.
- Counts carry their command and date; quotations name their location; a
  missing required integration artifact is named, never inferred. No
  historical round validator is run for this index.

## Census

Read-time census of `reports/round-20/**` at the moment this index was
generated (see **Index verification** for the reproducible command); files
under `__pycache__/` and `*.log` are excluded. **The wave was in flight at the
census** (first artifact 12:56:53Z; census 13:07:37Z): a file arriving after it
needs a dated refresh, not an inferred worker failure. Counts are artifact
counts, not worker counts.

| artifact | axis / owner | conformance state / limit |
|---|---|---|
| `reports/round-20/audit-10.md` | O/D/C (auditors) | Auditor receipt/script; attributed evidence, not independently re-executed here. |
| `reports/round-20/audit-11.md` | O/D/C (auditors) | Auditor receipt/script; attributed evidence, not independently re-executed here. |
| `reports/round-20/audit-12.md` | O/D/C (auditors) | Auditor receipt/script; attributed evidence, not independently re-executed here. |
| `reports/round-20/audit/x22-readme-rows-spotcheck.md` | O/D/C (auditors) | Auditor receipt/script; attributed evidence, not independently re-executed here. |
| `reports/round-20/audit/x24-lessons-audit.md` | O/D/C (auditors) | Auditor receipt/script; attributed evidence, not independently re-executed here. |
| `reports/round-20/audit/x24-lessons-audit.py` | O/D/C (auditors) | Auditor receipt/script; attributed evidence, not independently re-executed here. |
| `reports/round-20/audit/x24-lessons-receipt.json` | O/D/C (auditors) | Auditor receipt/script; attributed evidence, not independently re-executed here. |
| `reports/round-20/claims.json` | O/D/C declaration | Declared thresholds, not achieved outcomes (`state: declared-before-dispatch`). |
| `reports/round-20/fragment-index.md` | O/D/C (X19..X20 scribes) | Presence/conformance index only; self-check confers no admission. |
| `reports/round-20/handoff/audit-v3.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. |
| `reports/round-20/handoff/capability-draft.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. |
| `reports/round-20/handoff/claims-map.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. |
| `reports/round-20/handoff/design.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. |
| `reports/round-20/handoff/interop.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. |
| `reports/round-20/handoff/packet-v3-13.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. |
| `reports/round-20/handoff/packet-v3-14.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. |
| `reports/round-20/handoff/packet-v3-15.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. |
| `reports/round-20/handoff/regression-v2.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. |
| `reports/round-20/handoff/review-adversarial.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. |
| `reports/round-20/handoff/review.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. |
| `reports/round-20/handoff/uncertainty-plan.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. |
| `reports/round-20/integration/ledger-gen.py` | O/D/C (integration) | Integration fragment (ledger, LOG/SCORECARD drafts); parent-owned landing. |
| `reports/round-20/readme/gaps.md` | C (README seats) | C fragment for the corpus README reconciliation; attributed evidence. |
| `reports/round-20/readme/reconcile.md` | C (README seats) | C fragment for the corpus README reconciliation; attributed evidence. |
| `reports/round-20/readme/verify.md` | C (README seats) | C fragment for the corpus README reconciliation; attributed evidence. |
| `reports/round-20/report-draft.md` | O/D/C (X19..X20 scribes) | Explicit integration draft, not authorized final filing. |
| `reports/round-20/rerun.json` | O/D/C (X19..X20 scribes) | This seat's bounded evidence record; status `in-flight-at-the-draft-stamp`. |
| `reports/round-20/run-validation.py` | O/D/C (acceptance runner) | Executable; `--selftest` 21 controls exit 0; `--check` exit 1 (C pass, D/O fail). Existence is not a green end-to-end acceptance. |
| `reports/round-20/scope-a14.md` | O/D/C (scope scribes) | Scope/adjacency scribe fragment; presence recorded, not independently re-executed here. |
| `reports/round-20/scope.md` | O/D/C (scope scribes) | Scope/adjacency scribe fragment; presence recorded, not independently re-executed here. |
| `reports/round-20/targets.json` | O/D/C declaration | Seat allocation only; not a per-seat launch/completion trace. |
| `reports/round-20/validation.json` | O/D/C (primary receipt) | Primary receipt; not written or overwritten by this seat. |
| `reports/round-20/wart/design.md` | O (wart seats) | O fragment for the per-family era-alias resolution / re-pin cascade; attributed evidence. |
| `reports/round-20/wart/expected-v2-07-r20.json` | O (wart seats) | O fragment for the per-family era-alias resolution / re-pin cascade; attributed evidence. |
| `reports/round-20/wart/repin-r20.json` | O (wart seats) | O fragment for the per-family era-alias resolution / re-pin cascade; attributed evidence. |
| `reports/round-20/wart/review.md` | O (wart seats) | O fragment for the per-family era-alias resolution / re-pin cascade; attributed evidence. |
| `reports/round-20/wart/shard-1.md` | O (wart seats) | O fragment for the per-family era-alias resolution / re-pin cascade; attributed evidence. |
| `reports/round-20/wart/shard-2.md` | O (wart seats) | O fragment for the per-family era-alias resolution / re-pin cascade; attributed evidence. |
| `reports/round-20/wart/shard-3.md` | O (wart seats) | O fragment for the per-family era-alias resolution / re-pin cascade; attributed evidence. |
| `reports/round-20/wart/shard-4.md` | O (wart seats) | O fragment for the per-family era-alias resolution / re-pin cascade; attributed evidence. |
| `reports/round-20/wart/shard-5.md` | O (wart seats) | O fragment for the per-family era-alias resolution / re-pin cascade; attributed evidence. |
| `reports/round-20/wart/shard-6.md` | O (wart seats) | O fragment for the per-family era-alias resolution / re-pin cascade; attributed evidence. |

**Census:** 42 artifacts including this index and the rerun record (excluding `__pycache__/` and `*.log`); refreshed 2026-10-18T13:14:01.489509+00:00. The wave was in flight at the refresh: a later-arriving artifact needs a dated refresh, not an inferred worker failure.
1. **No `validation.json` at the census.** The primary receipt
   (`reports/round-20/validation.json`) did not exist; the runner's verdicts
   above are from this seat's read-only `--check` run at 13:07Z.
2. **The runner's `missing_dependencies` names two D artifacts:**
   `reports/round-20/<contract-audit-rerun>.md` and
   `reports/round-20/handoff/expected.json` — a v3 freeze has not landed.
3. **The O re-pin cascade is incomplete at the census:** one re-pin row
   (`wart/expected-v2-07-r20.json`) exists; no files under
   `reports/round-20/repin/**` or `tools/gates/frozen/round-20/**`, and the
   runner names five stale pins across `examples/culture-d4/expected-holds.json`
   and `examples/culture-d4/packet.d4.typed.yml`.
4. **The C receipts the README cites exist** (`readme/reconcile.md`,
   `readme/verify.md`, `readme/gaps.md`) — at 13:00Z the README revision block
   already cited them before they were on disk; by 13:03–13:04Z all three had
   landed.
5. **Filed-rounds incident (attributed, closed):** `reports/round-9/validation.json`
   was overwritten at 13:00:55Z by a seat re-running historical round
   validators (rounds 5/7/9, seconds apart); restored to its committed bytes by
   13:05Z. Evidence: `.scratch/x19/filed-r9.diff` (sha `3134443d…`),
   `.scratch/x19/filed-r5-r7.diff`; the runner's own guard reads 897 files
   byte-identical at 13:07Z. This index neither performed nor repaired the
   write.

## Index verification

X20 writes only this file (and the sibling `rerun.json`). This stdout-only
control verifies the delivered index's path coverage, duplicate/missing-entry
detection, nonempty artifacts, and Markdown shape. Negative controls are
in-memory: duplicate and dropped index rows must fail, and a nonexistent path
must be detected. No fixture file is created. A later-arriving artifact
requires a dated index refresh.

```sh
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
from datetime import datetime, timezone
from pathlib import Path
import re
index = Path('reports/round-20/fragment-index.md')
text = index.read_text()
rows = re.findall(r'^\| `(reports/round-20/[^`]+)` \|', text, re.M)
actual = sorted(str(p) for p in index.parent.rglob('*')
                if p.is_file() and '__pycache__' not in str(p) and not str(p).endswith('.log'))
def conforms(names):
    return (len(names) == len(set(names)) and set(names) == set(actual)
            and all(Path(p).is_file() and Path(p).stat().st_size > 0 for p in names))
print('observed_at=' + datetime.now(timezone.utc).isoformat())
print('indexed=' + str(len(rows)) + ' observed=' + str(len(actual)))
print('unindexed=' + repr(sorted(set(actual) - set(rows))))
print('unavailable=' + repr(sorted(set(rows) - set(actual))))
assert conforms(rows), 'index inventory incomplete or invalid'
assert not conforms(rows + [rows[0]]), 'duplicate negative missed'
assert not conforms(rows[1:]), 'dropped-row negative missed'
assert not conforms(rows + ['reports/round-20/__X20_nonexistent__.md']), 'missing-path negative missed'
assert text.endswith('\n') and '\0' not in text
assert all(line == line.rstrip() for line in text.splitlines()), 'trailing whitespace'
assert len(re.findall(r'^```[^\n]*$', text, re.M)) % 2 == 0, 'unbalanced fences'
print('INDEX_CONTROL=PASS; duplicate/drop/missing negatives rejected')
PY
```
