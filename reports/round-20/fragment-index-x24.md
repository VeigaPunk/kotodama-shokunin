# R20-X24 — fragment conformance index

Axes: **D / depth** (the handoff e2e v3 exercise over D2+D3+D4 with the
uncertainty dimension and resolving links); **O / operability** (per-family
era-alias resolution closing the round-19 projector wart, D2 path byte-
identical, repin cascade as new rows); **C / coverage** (`corpus/README.md`
reconciled against the partition contents, command-carried). This is the
assigned X24 index, not a round-admission receipt or independent promotion
review. The lane declaration remains `reports/round-20/claims.json`; work
allocation remains `reports/round-20/targets.json`.

**Path note (declared collision, not absorbed).** Seat **X19..X20**'s
`rerun.json` lists `reports/round-20/fragment-index.md` in its `write_scope`
and its index landed there at census 13:07:37Z (33 rows). This seat was also
assigned a fragment index; to avoid two writers on one path (the round-19
lesson, X28-1 / X24-L1), X24 files its later census at this seat-named path.
Both artifacts coexist; the parent owns the choice of canonical index. This
file does not edit the other index's bytes.

## Reading this index

- **Indexed** means the named artifact existed at the census and its size and
  sha256 were read. It does not mean the whole claim passed, that a draft was
  integrated, or that a proposed control was executed.
- **Attributed** results belong to their source fragment; a row is an X24
  execution only where it says so.
- **Draft / design / pending** are deliberate distinctions. A landed draft is
  not a landing; a proposed check is not a pass; a baseline pin is not a
  verdict replay.
- Counts carry their command and date; quotations name their location; a
  missing required integration artifact is named, never inferred. No
  historical round validator is run for this index.

## Census

Read-time census of `reports/round-20/**` at 2026-10-18T13:26:59Z (command:
`python3 -B .scratch/x24/gen-index.py`, sha8 digests via `hashlib.sha256`; see
**Index verification** for the reproducible coverage control); files under
`__pycache__/` and `*.log` are excluded. The wave was in flight at the census
(first artifact 12:56:53Z; 71 non-log artifacts read; the census count grew
from 2 at the declaration to 56 by 13:17Z); a file arriving after it needs a
dated refresh, not an inferred worker failure. Counts are artifact counts,
not worker counts.

| artifact | axis / owner | conformance state / limit |
|---|---|---|
| `reports/round-20/audit-10.md` | O/D/C (auditors) | Auditor receipt; attributed evidence, not independently re-executed here. 8020 B, sha8 `ec598816`. |
| `reports/round-20/audit-11.md` | O/D/C (auditors) | Auditor receipt; attributed evidence, not independently re-executed here. 11904 B, sha8 `08cc32ab`. |
| `reports/round-20/audit-12.md` | O/D/C (auditors) | Auditor receipt; attributed evidence, not independently re-executed here. 13658 B, sha8 `3e606ff7`. |
| `reports/round-20/audit-9.md` | O/D/C (auditors) | Auditor receipt; attributed evidence, not independently re-executed here. 9804 B, sha8 `c983c9a6`. |
| `reports/round-20/audit/x21-v3-claims-spotcheck.md` | auditors | Auditor receipt/script; attributed evidence, not independently re-executed here. 16648 B, sha8 `c97b5ac4`. |
| `reports/round-20/audit/x22-readme-rows-spotcheck.md` | auditors | Auditor receipt/script; attributed evidence, not independently re-executed here. 9811 B, sha8 `d9c6ab08`. |
| `reports/round-20/audit/x24-lessons-audit.md` | X24 (this seat) | X24 lessons audit; NON-CANON, admits nothing; §6 carries the 13:26:39Z round-20 lesson observation. 13414 B, sha8 `61419b79`. |
| `reports/round-20/audit/x24-lessons-audit.py` | X24 (this seat) | X24 read-only tool; `--selftest` 12/12 exit 0; opens no file for writing. 7130 B, sha8 `2d77294a`. |
| `reports/round-20/audit/x24-lessons-receipt-r2.json` | X24 (this seat) | X24 receipt (stdout redirect of the tool); binds to its `observed_at_utc` 13:26:39Z. 13138 B, sha8 `e91e406d`. |
| `reports/round-20/audit/x24-lessons-receipt.json` | X24 (this seat) | X24 receipt (stdout redirect of the tool); binds to its `observed_at_utc` 12:56:53Z. 12552 B, sha8 `10e975e4`. |
| `reports/round-20/claims.json` | D/O/C declaration | Declared thresholds, not achieved outcomes (`state: declared-before-dispatch`). 2436 B, sha8 `96d02da6`. |
| `reports/round-20/entries/R20-D21.md` | D (frozen/entry seats) | Entry fragment (frozen baseline + tamper control); attributed evidence. 5004 B, sha8 `67f50357`. |
| `reports/round-20/entries/R20-D22.md` | D (frozen/entry seats) | Entry fragment (frozen baseline + tamper control); attributed evidence. 2915 B, sha8 `84b1d0ac`. |
| `reports/round-20/entries/R20-D23.md` | D (frozen/entry seats) | Entry fragment (frozen baseline + tamper control); attributed evidence. 2820 B, sha8 `7ec16d75`. |
| `reports/round-20/entries/R20-D24.md` | D (frozen/entry seats) | Entry fragment (frozen baseline + tamper control); attributed evidence. 3251 B, sha8 `4a576275`. |
| `reports/round-20/fragment-index-x24.md` | X24 (this seat) | Presence/conformance index only; this file (self row — size/sha are not self-measurable at write time; the control below checks its presence and shape). |
| `reports/round-20/fragment-index.md` | O/D/C (X19..X20 scribes) | Presence/conformance index only; census 13:07:37Z (X19..X20's own stamp); self-check confers no admission. 11298 B, sha8 `3621ee0c`. |
| `reports/round-20/handoff/audit-v3.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 15227 B, sha8 `10f09b9b`. |
| `reports/round-20/handoff/capability-draft.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 8153 B, sha8 `691add89`. |
| `reports/round-20/handoff/claims-map.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 24888 B, sha8 `4b1b9a35`. |
| `reports/round-20/handoff/design.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 34784 B, sha8 `793fc8a6`. |
| `reports/round-20/handoff/expected.json` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 8818 B, sha8 `40ba13de`. |
| `reports/round-20/handoff/freeze.txt` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 430 B, sha8 `faeb1378`. |
| `reports/round-20/handoff/frozen.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 10732 B, sha8 `3041d391`. |
| `reports/round-20/handoff/interop.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 11014 B, sha8 `a5b07f46`. |
| `reports/round-20/handoff/packet-v3-13.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 103919 B, sha8 `5b3b8ae6`. |
| `reports/round-20/handoff/packet-v3-14.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 103919 B, sha8 `1ad4562c`. |
| `reports/round-20/handoff/packet-v3-15.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 103919 B, sha8 `2f3d8750`. |
| `reports/round-20/handoff/packet-v3-16.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 103919 B, sha8 `9f37c08a`. |
| `reports/round-20/handoff/packet.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 67683 B, sha8 `6de822f4`. |
| `reports/round-20/handoff/regression-v2.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 11855 B, sha8 `3effd3b9`. |
| `reports/round-20/handoff/review-adversarial.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 8150 B, sha8 `4f7f7e33`. |
| `reports/round-20/handoff/review.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 14894 B, sha8 `521e2dfc`. |
| `reports/round-20/handoff/twin.json` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 59335 B, sha8 `b3e2bad7`. |
| `reports/round-20/handoff/uncertainty-plan.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 12986 B, sha8 `3514eece`. |
| `reports/round-20/handoff/v3.md` | D (handoff-e2e v3 seats) | D fragment for the v3 handoff exercise; attributed evidence. 10616 B, sha8 `ed7f1b8c`. |
| `reports/round-20/integration/fragment-ledger.json` | integration | Integration fragment (ledger, LOG/SCORECARD drafts); parent-owned landing. 17315 B, sha8 `30fc5d1b`. |
| `reports/round-20/integration/fragment-ledger.md` | integration | Integration fragment (ledger, LOG/SCORECARD drafts); parent-owned landing. 8600 B, sha8 `6a5a9767`. |
| `reports/round-20/integration/ledger-gen.py` | integration | Integration fragment (ledger, LOG/SCORECARD drafts); parent-owned landing. 8098 B, sha8 `e37df15f`. |
| `reports/round-20/ledger-snapshot.md` | freshness auditors (R20-A15..A16) | Drift-ledger snapshot; audit-only, no axis-move; attributed evidence. 14326 B, sha8 `655ad20a`. |
| `reports/round-20/readme/gaps.md` | C (README reconciliation) | C README reconciliation fragment; attributed evidence. 27043 B, sha8 `cdf6692d`. |
| `reports/round-20/readme/reconcile.md` | C (README reconciliation) | C README reconciliation fragment; attributed evidence. 17208 B, sha8 `4907adc8`. |
| `reports/round-20/readme/verify.md` | C (README reconciliation) | C README reconciliation fragment; attributed evidence. 8089 B, sha8 `cbb9a592`. |
| `reports/round-20/regression.md` | O regression seat | O seat's regression receipt; attributed evidence. 15191 B, sha8 `b0c04ba2`. |
| `reports/round-20/repin/O11-repin-d2.md` | O (repin cascade) | O repin cascade fragment; NEW rows only, filed rounds untouched. 11088 B, sha8 `bcfa74ad`. |
| `reports/round-20/repin/O12-repin-v207.md` | O (repin cascade) | O repin cascade fragment; NEW rows only, filed rounds untouched. 8341 B, sha8 `97f32ac0`. |
| `reports/round-20/repin/O13-repin-baselines.md` | O (repin cascade) | O repin cascade fragment; NEW rows only, filed rounds untouched. 7886 B, sha8 `463e666c`. |
| `reports/round-20/repin/O14-repin-table.md` | O (repin cascade) | O repin cascade fragment; NEW rows only, filed rounds untouched. 12353 B, sha8 `8f03cfd0`. |
| `reports/round-20/repin/evidence/baseline-projector-scan.txt` | O (repin cascade) | O repin cascade fragment; NEW rows only, filed rounds untouched. 2131 B, sha8 `377bc3f2`. |
| `reports/round-20/repin/evidence/readings-after.txt` | O (repin cascade) | O repin cascade fragment; NEW rows only, filed rounds untouched. 2828 B, sha8 `e67e7f93`. |
| `reports/round-20/repin/evidence/readings-before.txt` | O (repin cascade) | O repin cascade fragment; NEW rows only, filed rounds untouched. 3135 B, sha8 `986e8dd6`. |
| `reports/round-20/repin/evidence/readings-final.txt` | O (repin cascade) | O repin cascade fragment; NEW rows only, filed rounds untouched. 2233 B, sha8 `f0a84510`. |
| `reports/round-20/repin/evidence/runner-claim-o.json` | O (repin cascade) | O repin cascade fragment; NEW rows only, filed rounds untouched. 6732 B, sha8 `35250a52`. |
| `reports/round-20/repin/evidence/runner-final.json` | O (repin cascade) | O repin cascade fragment; NEW rows only, filed rounds untouched. 3443 B, sha8 `fd97b92a`. |
| `reports/round-20/repin/expected-v2-07-r20.json` | O (repin cascade) | O repin cascade fragment; NEW rows only, filed rounds untouched. 4802 B, sha8 `e594137c`. |
| `reports/round-20/report-draft.md` | O/D/C (X19..X20 scribes) | Explicit integration draft, not authorized final filing. 13924 B, sha8 `036071e9`. |
| `reports/round-20/rerun.json` | O/D/C (X19..X20 scribes) | Bounded evidence record; status `in-flight-at-the-draft-stamp`. 12443 B, sha8 `286d591d`. |
| `reports/round-20/run-validation.py` | acceptance runner | Executable; live sha8 `200e0bf8` at the census; existence is not a green end-to-end acceptance. 73740 B, sha8 `200e0bf8`. |
| `reports/round-20/scope-a14.md` | scope/adjacency scribes | Presence recorded; not independently re-executed by this seat. 9270 B, sha8 `bb757943`. |
| `reports/round-20/scope.md` | scope/adjacency scribes | Presence recorded; not independently re-executed by this seat. 14768 B, sha8 `741ad1ce`. |
| `reports/round-20/targets.json` | D/O/C declaration | Seat allocation only; not a per-seat launch/completion trace. 201 B, sha8 `630995e7`. |
| `reports/round-20/validation.json` | acceptance runner | Primary receipt; written only by the assigned runner. 997210 B, sha8 `4e979e9f`; mtime 13:21:07Z, `acceptance_checks_passed: true`, `failures: []`, all three claims `passed: true` — see the runner-revision note below. |
| `reports/round-20/wart/design.md` | O (wart-analysis seats) | O fragment for the per-family era-alias resolution; attributed evidence. 13135 B, sha8 `fbb77c77`. |
| `reports/round-20/wart/expected-v2-07-r20.json` | O (wart-analysis seats) | O fragment for the per-family era-alias resolution; attributed evidence. 4435 B, sha8 `ad761a61`. |
| `reports/round-20/wart/repin-r20.json` | O (wart-analysis seats) | O fragment for the per-family era-alias resolution; attributed evidence. 6200 B, sha8 `2e5d2090`. |
| `reports/round-20/wart/review.md` | O (wart-analysis seats) | O fragment for the per-family era-alias resolution; attributed evidence. 12098 B, sha8 `664479a1`. |
| `reports/round-20/wart/shard-1.md` | O (wart-analysis seats) | O fragment for the per-family era-alias resolution; attributed evidence. 6289 B, sha8 `64d237aa`. |
| `reports/round-20/wart/shard-2.md` | O (wart-analysis seats) | O fragment for the per-family era-alias resolution; attributed evidence. 4438 B, sha8 `a5788c0d`. |
| `reports/round-20/wart/shard-3.md` | O (wart-analysis seats) | O fragment for the per-family era-alias resolution; attributed evidence. 4581 B, sha8 `5ed798d6`. |
| `reports/round-20/wart/shard-4.md` | O (wart-analysis seats) | O fragment for the per-family era-alias resolution; attributed evidence. 8207 B, sha8 `0b6ef08a`. |
| `reports/round-20/wart/shard-5.md` | O (wart-analysis seats) | O fragment for the per-family era-alias resolution; attributed evidence. 7033 B, sha8 `963e48af`. |
| `reports/round-20/wart/shard-6.md` | O (wart-analysis seats) | O fragment for the per-family era-alias resolution; attributed evidence. 6132 B, sha8 `f4e57e45`. |

**Census:** 72 artifacts indexed (71 non-log artifacts read at
13:26:59Z; this index file is the 72nd, self-indexed without size/sha).
Excluded: `__pycache__/` and `*.log` (e.g. `reports/round-20/handoff/run.log`).

## Conformance observations

- **The round's own receipt is green but binds to a superseded runner
  revision.** `reports/round-20/validation.json` (mtime 13:21:07Z, sha8
  `4e979e9f`) reads `acceptance_checks_passed: true`, `failures: []`, claims
  C/D/O `passed: true`, and carries `runner_sha256 6da4f7ed92b6f206…`. The
  live `reports/round-20/run-validation.py` was revised at 13:23:41Z and
  hashes `200e0bf84f85ba7a…` at the census — **the receipt does not bind to
  the live runner bytes**. This is attributed evidence (the runner wrote it),
  and it is the reason a close should re-run the runner at the final
  revision rather than quote the 13:21Z receipt.
- **D / depth:** the v3 handoff family landed — design, claims map, packet
  drafts `packet-v3-13` … `packet-v3-16`, `expected.json`, `twin.json`,
  `frozen.md`/`freeze.txt`, `audit-v3.md`, `regression-v2.md`, reviews and
  the interop/capability drafts — and the receipt's claim D leg reads passed.
  Per this index's rules that is attributed evidence; the packet bytes are
  drafts/frozen artifacts, not a verified end-to-end clearance.
- **O / operability:** the wart and repin shards landed (`wart/design.md` +
  six shards + review, `repin/O11..O14` + six evidence files) and
  `repin/O14-repin-table.md` records status COMPLETE with the round's own
  counting command reading claim O `failures: []`. The round-19 erratum
  (mirror carrying the foreign `examples/culture-d2` tree) is addressed by
  those fragments; whether it is closed is the runner/auditor verdict, not
  this index's.
- **C / coverage:** `readme/{reconcile,verify,gaps}.md` landed; the receipt's
  claim C leg reads passed. The README bytes themselves are outside
  `reports/round-20/**` and are not indexed here.
- **X24's own artifacts:** the lessons-audit trio (tool, two receipts, audit
  report) plus this index. The lessons audit census (12:56:53Z) read 20
  lesson files with Gate in 15; the r2 receipt (13:26:39Z) reads 21 files —
  `corpus/lessons/round-20.md` (X17) landed at 13:17:16Z with the full
  contract surface (source / verified-at / recheck / scope + `## Gate`, 57
  path refs, 0 missing). The audit report carries the dated observation.
- **Filing, scope and dispatch** (launch/completion trace, final work
  revision, authorized external filing, non-author promotion marks) remain
  parent responsibilities; in-lane attestations do not prove a fresh external
  inspection.

## Index verification

X24 writes only this file (plus the seat's lessons-audit trio under
`reports/round-20/audit/`). This stdout-only control verifies the delivered
index's path coverage, duplicate/missing-entry detection, nonempty artifacts,
and Markdown shape. Negative controls are in-memory: duplicate and dropped
index rows must fail, and a nonexistent path must be detected. No fixture file
is created. A later-arriving artifact requires a dated index refresh.

```sh
export TMPDIR=$PWD/.scratch
export PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
from datetime import datetime, timezone
from pathlib import Path
import re
index = Path('reports/round-20/fragment-index-x24.md')
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
assert not conforms(rows + ['reports/round-20/__X24_nonexistent__.md']), 'missing-path negative missed'
assert text.endswith('\n') and '\0' not in text
assert all(line == line.rstrip() for line in text.splitlines()), 'trailing whitespace'
assert len(re.findall(r'^```[^\n]*$', text, re.M)) % 2 == 0, 'unbalanced fences'
print('INDEX_CONTROL=PASS; duplicate/drop/missing negatives rejected')
PY
```

Control run **2026-10-18T13:28:33Z**: `indexed=72 observed=72`, `unindexed=[]`,
`unavailable=[]`, `INDEX_CONTROL=PASS` (duplicate/drop/missing negatives
rejected). A later arrival invalidates this reading and needs a dated refresh.
