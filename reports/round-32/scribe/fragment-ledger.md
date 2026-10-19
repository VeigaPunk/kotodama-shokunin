# R32-D14 — fragment ledger for parent integration + the dossier's honest limits

Date: 2026-10-18 (round-32 declared date; all observation times below are UTC and
fall on **2026-10-19** — the wall clock rolled past midnight UTC during the wave).
Seat: **R32-D14** (dossier scribe), the regimen's final round (operator: loop 3,
GLM round 2 of 2; 16 workers on zai-coding-plan/glm-5.3-flash-low, host-pinned
MAX effort). Assignment group: R32-D11..D14 (dossier fragments + scribe). Axes:
D / depth integration, evidence completeness, scoped provenance.

This is a **read-time census and a limits record**, not an admission, not a
promotion or closure verdict, not fragment certification, and not a declaration
that every worker has finished. This seat wrote **only this file**: no scratch
script beyond the census/recount printers under `$TMPDIR`, no source, gate,
pin, packet, old-round or shared-bookkeeping edit; no commit, no push. The
counting validator `python3 reports/round-32/run-validation.py` was **not
executed** by this seat — it is the round's counting command and writes
`validation.json`, a parent-owned integration artifact.

## Census boundary

At **2026-10-19T00:44:49Z**, lane HEAD was
`4d500501a286d96f2eea8a6188c649255581301a` (round-32 declare); the declared
baseline remains `17e90b9047b289d7a63180a1dc1bebb074137e29`. The census
measured **30 files / 605,626 bytes** under the round, excluding `__pycache__`
and this ledger's own file (no self-hash cycle). The census is sequential and
the wave was still writing: each row describes bytes read at this cut, not an
atomic or final tree. Re-measure before integration instead of inheriting these
hashes. Partition counts at the cut: **sweep 6; telemetry 8; top-level 16**.

All counts and row fingerprints use this command, run on **2026-10-19** with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
from pathlib import Path
from collections import Counter
from datetime import datetime, timezone
import hashlib, json, subprocess
base = Path('reports/round-32')
exclude = {str(base / 'scribe/fragment-ledger.md')}
rows = []
for path in sorted(base.rglob('*')):
    if not path.is_file() or '__pycache__' in path.parts or str(path) in exclude:
        continue
    data = path.read_bytes()
    rows.append({'path': str(path), 'bytes': len(data),
        'sha256': hashlib.sha256(data).hexdigest(),
        'mtime_utc': datetime.fromtimestamp(path.stat().st_mtime,
            timezone.utc).isoformat(timespec='seconds')})
partitions = Counter((Path(r['path']).relative_to(base).parts[0]
    if len(Path(r['path']).relative_to(base).parts) > 1 else 'top-level') for r in rows)
print(json.dumps({'census_utc': datetime.now(timezone.utc).isoformat(),
    'lane_head': subprocess.check_output(['git', 'rev-parse', 'HEAD'],
        text=True).strip(), 'files': len(rows),
    'bytes': sum(r['bytes'] for r in rows),
    'partitions': dict(sorted(partitions.items())), 'rows': rows}, indent=2))
PY
```

Table paths are relative to `reports/round-32/`; SHA prefixes are 12 hex
characters for readability (the command emits full digests). A fingerprint
printer is an inventory, not a drift gate and not an expected verdict.

| Fragment path | Bytes at cut | SHA-256 prefix | mtime UTC |
|---|---:|---|---|
| `claims.json` | 2558 | `043dcc6c5aa8` | 00:30:17 |
| `completion-audit-C04.md` | 10356 | `0157a001343e` | 00:41:45 |
| `completion-audit-C05.md` | 10120 | `2c166510ab9c` | 00:42:24 |
| `completion-audit.md` | 10376 | `01bbac20c142` | 00:43:31 |
| `completion-ledger.json` | 55253 | `b90ed4726152` | 00:43:31 |
| `dossier-d11-shonen-boxes.md` | 14001 | `e5b34e19f597` | 00:39:03 |
| `dossier-d12-capability-inventory.md` | 10338 | `c4765bf3d79e` | 00:39:49 |
| `dossier-d13-operator-decisions.md` | 8989 | `1ededf01f72d` | 00:40:32 |
| `final-dossier.md` | 9733 | `b82319b50749` | 00:41:54 |
| `run-validation.py` | 55918 | `300889d0a0cd` | 00:44:06 |
| `scope.md` | 17932 | `da1bd1f4c763` | 00:41:10 |
| `sweep/commands.txt` | 3681 | `60309bfc1dbb` | 00:44:42 |
| `sweep/receipt-O06.json` | 48949 | `1869d3f1602f` | 00:44:42 |
| `sweep/receipt-O07.json` | 48955 | `fa3ff7d34044` | 00:44:42 |
| `sweep/receipt-O08.json` | 48957 | `72479d1a2b40` | 00:44:42 |
| `sweep/run-sweep.py` | 32296 | `51684b6d45b8` | 00:38:08 |
| `sweep/sweep-receipt.json` | 53614 | `25bcbc22b0f0` | 00:44:42 |
| `sweep-audit-O09.json` | 60214 | `9aab2662c939` | 00:37:38 |
| `sweep-audit-O09O10.json` | 4032 | `294e48d2bea8` | 00:38:16 |
| `sweep-audit-O10.json` | 60215 | `393368f10ffc` | 00:38:16 |
| `sweep-audit.py` | 17948 | `4b5485376cb1` | 00:36:54 |
| `targets.json` | 187 | `906c23a2e1df` | 00:30:17 |
| `telemetry/check.json` | 219 | `d740d97ed20c` | 00:34:36 |
| `telemetry/controls-vartmp.json` | 1886 | `379b52eabce6` | 00:34:36 |
| `telemetry/controls.json` | 1934 | `8fe6fc43cf53` | 00:34:36 |
| `telemetry/dispatch-stats.json` | 2403 | `8316c0d4151f` | 00:34:36 |
| `telemetry/dispatch-telemetry.py` | 10531 | `289744bcbd97` | 00:34:29 |
| `telemetry/inputs/claims.json` | 2558 | `043dcc6c5aa8` | 00:33:28 |
| `telemetry/inputs/targets.json` | 187 | `906c23a2e1df` | 00:33:28 |
| `telemetry/worker-observation.json` | 1286 | `f10ffe07e64e` | 00:33:40 |

## Integration map and ownership qualifications

These are routing pointers, not authorizations to edit another seat's files.
Ownership outside this worker's file is inferred from the declaration/targets
roles (`reports/round-32/targets.json`: C-completion 5, O-sweep 5, D-dossier 4,
X 2); the parent remains integrator of record.

- **C / completion audit:** `completion-audit.md` (the criterion verification,
  audited `2026-10-18T21:43:31-03:00` per its header = 00:43:31Z), backed by
  `completion-ledger.json`; `completion-audit-C04.md` and
  `completion-audit-C05.md` are independent re-verifications with **distinct
  methods** (C04 raw-only sample {8, 11, 13, 20, 26, 31}; C05 re-derivation +
  field-diff against `reports/round-31/closure-ledger.json` over
  {9, 13, 17, 22, 24, 30, 31}) — two facets, not automatic approval of a later
  unseen edit. Their `.scratch` extractor scripts are cited inside those files
  and were not re-run by this seat.
- **O / final sweep:** `sweep/run-sweep.py` is the runner;
  `sweep/sweep-receipt.json` + `sweep/receipt-O06/O07/O08.json` +
  `sweep/commands.txt` are the receipts (all filed 00:44:42Z, seven seconds
  before this census); `sweep-audit.py` + `sweep-audit-O09.json` /
  `sweep-audit-O10.json` / `sweep-audit-O09O10.json` are the auditors'
  independent receipts (00:36:54–00:38:16Z, i.e. they predate the final
  receipts and may need their own dated re-read — an auditor question, not one
  this seat answers). Receipt headline fields **quoted as filed, not
  re-adjudicated**: `failures: []`; cross-pass digest equality
  (`digest_equal_across_passes: true`, exempted `battery`,
  `pin-repoint-selftest`); battery `coverage: "10/10"`, pinned 20;
  `law_clean_findings: 0`; `matrix_provenance` imports 50 green rows + 13
  controls from `reports/round-31/sweep/run-sweep.py`.
- **D / final dossier:** `final-dossier.md` (§1 boxes re-survey, §2 capability
  inventory, §3 operator decision materials, §4 method/limits) assembled from
  `dossier-d11-shonen-boxes.md`, `dossier-d12-capability-inventory.md`,
  `dossier-d13-operator-decisions.md`. Its limits are carried forward below —
  this section is the scribe's independent record, not an edit of the dossier.
- **X / scope + telemetry:** `scope.md` (SCRIBE X17, the final scope watch:
  PASS at four instants 00:34:51–00:37:51Z over 1,870 tracked paths vs
  baseline — quoted as filed) and `telemetry/` (owner R32-X19:
  `dispatch-stats.json` records `full_wave_status: "could-not-evaluate"`,
  scope "partial-worker-observation; not a closed full-wave sample"; null
  counters are unavailable, not zero; `controls-vartmp.json` covers the
  `/var/tmp` mirror leg). Requested allocation (16 seats) is a declaration;
  no fleet completion rate is inferred from any of this.
- **Parent-owned at integration (open at this cut):** `validation.json` (the
  counting command's receipt), the LOG.md/SCORECARD/MANIFEST round-32 entries,
  the fleet report, and — per the jin'i-ryu finalization-closure rule
  (`SKILL.md:710-715`, `AGENTS.md`) — the **closing telemetry snapshot** for
  `telemetry/check.json`, filed as a new append-only artifact after
  `validation.json` lands, naming the record it closes and that record's
  SHA-256 at close time. Round 32 is not admitted while that closing snapshot
  is owed.

## The dossier's honest limits

Recorded by this scribe at the 00:44:49Z cut, after reading
`final-dossier.md` and all three D fragments end to end. These are the
boundaries the final dossier (and anything built on it) must keep carrying;
each is either stated in the dossier itself or is a dated observation this
seat adds. They are limits, not defects found.

1. **Evidence, not decision.** The dossier claims no promotion, no canon, no
   clearance, no closure verdict; it "IS the decision's evidence"
   (`reports/round-32/claims.json`, claim D). SHONEN marks stay
   operator-owned (`SHONEN.md:10-11`); D13's four decision materials table
   options and falsifiers and take none. Confirmed at this read: nothing in
   the four D files awards a mark or a verdict.
2. **The only promotion-grade non-author pass on file is r24's — over the
   r24 tree.** Post-r24 deltas (Register-craft landing r30, jin'i-ryu rule
   r31, QREG resolution r30) carry craft reviews (`reports/round-30/craft/`),
   sweep legs and this round's re-measurements, but no non-author
   promotion-grade verification. D13 says this plainly; the limit survives
   every green receipt in the round.
3. **Box-1's closure is scoped to the inventory condition.** The r30 survey
   (`reports/round-30/craft/review-D29-box1.md:140-152`) closed the
   unnamed-executable condition and explicitly did **not** collectively
   dispose the other box-1 conditions. D11 re-measures them open at HEAD
   (loanword pointers `SKILL.md:486/:488`, contract-`:183` mis-cite at
   `SKILL.md:501/:128`, zero hits for `TL-01`/`TL-02`/`FIELD_DEFAULTS` in
   `tools/d2-typed-labels.py`). This seat re-ran the read-only survey:
   `python3 -B reports/round-30/craft/box1-survey.py` → exit 0, **28/28
   named**, at `SKILL.md` SHA-256
   `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d`
   (2026-10-19T00:44Z) — the condition stays closed at current bytes; the
   citation-level conditions stay open.
4. **Cut-dependence is real, and disclosed.** The dossier's own evidence cut
   predates the O receipts (00:44:42Z) and the re-filed `run-validation.py`
   (00:44:06Z, 55,918 B; it was already present at 00:39:39Z and was
   rewritten — the earlier bytes are superseded history). Its dated addendum
   honestly recorded "sweep receipt not yet filed"; that was true at its cut
   and is superseded at this one. No reader may cite the dossier's cut as the
   settled tree; the parent re-measures at integration.
5. **Round 32 closes by construction, and cannot self-certify.** The
   completion criterion covers rounds 8–31 verified plus the 32-by-construction
   slot (its report + ledger entry land in the same integration pass that
   admits it). Nothing filed inside the round can assert the round's own
   admission; acceptance is `python3 reports/round-32/run-validation.py` on
   the settled deliverable — a command this seat never executed.
6. **Verdicts are quoted, not re-adjudicated, and red stays red.** The sweep
   receipt's green headline is the O-lane's machine record; the O09/O10
   audits are the auditors' verdicts. The 13 imported historical controls sit
   at their expected filed-red codes by design; a reproduced red verdict
   stays red, and reproduction is not clearance.
7. **Declarations are not observations.** 16 requested seats is a
   declaration; the only filed observation is one worker's partial
   self-observation (`full_wave_status: could-not-evaluate`). Attendance,
   completion rates and provider liveness are not inferable from this round's
   files, and the round's acceptance does not depend on them being inferred.
   The telemetry record stays open until the parent's closing snapshot lands.
8. **Green is integrity, never quality, canon or coverage.** NON-CANON
   engineering evidence throughout (`PROVINCE.md`: lore-shokunin owns canon);
   capability-inventory rows demonstrate commands, not universal guarantees;
   no calibrated numeric rubric exists (SCORECARD header gap; D13 debt
   table); freshness is paused, not strong (r30 retrospective: full-regimen
   replay 147/189 = 0.7778 and 147/192 = 0.765625, both < 0.95 — quoted as
   filed, not re-executed by this seat).
9. **Standing debts survive closure.** D13's twelve-item open-debt table
   (12 D4 garment holds, empty `head2`, RL-3 ceiling, box-1 conditions 2–4,
   cold-run N1/N4/N5/N7, lore-owned bilateral read + L0 contract-digest
   ratification, the rubric gap, devin-telemetry could-not-evaluate, D4-adapter
   supersession semantics) is carried unchanged into closure. "Nothing blocks
   closure" is not "nothing is owed".

## Read-set movement across this seat's polls

Dependencies were sampled with 60-second polls (00:35:19Z → 00:43:39Z, six
observations) while this seat read the filed fragments, within the polling
bound. Sequence: telemetry core first (00:33–00:34Z), C audit + O audit tool +
runner (00:37–00:41Z), D fragments in seat order d11 → d12 → d13 →
`final-dossier.md` (00:39:03–00:41:54Z), C04/C05 auditor re-verifications
(00:41:45–00:42:24Z), then `run-validation.py` rewritten (00:44:06Z) and the
entire `sweep/` receipt set (00:44:42Z) — seven seconds before the census cut.
Every arrival above is a dated observation; nothing was inferred backward, and
no missing dependency was declared failed.

## Final handoff checks (2026-10-19T00:47Z)

Read-only probes this seat actually executed, all on **2026-10-19**, all inside
the lane: the box-1 survey re-run (item 3 above), `sha256sum SKILL.md` →
`79fe91d3d429…` (matches the dossier's cited HEAD bytes), and
`git log --oneline -- PROVINCE.md` → last touch `c53782a`
("supplement-opencode-1: recheck sources and harden reproducible evidence"),
confirming D11's byte-identical-since-`c53782a` claim. The census table above
was emitted by the census command itself; its 30 rows are the same machine
output, not retyped counts. This ledger cannot substitute for the counting
command on the settled tree; final acceptance remains
`python3 reports/round-32/run-validation.py` on the parent-integrated
deliverable.

## Supersession note (2026-10-19T00:47:20Z recount, appended 00:48Z)

The wave was still moving after the census cut, exactly as this ledger's
boundary paragraph warned. A recount at **00:47:20Z** (same command, same
exclusions) again found **30 files** — no arrivals or deletions under
`reports/round-32/` — but **605,626 → 608,194 bytes**, with six table rows
superseded by in-place rewrites after 00:44:49Z:

| path | filed bytes/sha (00:44:49Z cut) | current bytes/sha (00:47:2xZ reads) | new mtime UTC |
|---|---|---|---|
| `run-validation.py` | 55918 / `300889d0a0cd` | 56343 / `ce313b258c4d` | 00:47:25 |
| `sweep/run-sweep.py` | 32296 / `51684b6d45b8` | 32517 / `907fda671b79` | 00:45:47 |
| `sweep-audit.py` | 17948 / `4b5485376cb1` | 19144 / `f94af20cd180` | 00:47:22 |
| `sweep-audit-O09.json` | 60214 / `9aab2662c939` | 60205 / `73b1648da99b` | 00:46:32 |
| `sweep-audit-O10.json` | 60215 / `393368f10ffc` | 60210 / `a124cb7a2b8d` | 00:47:10 |
| `sweep-audit-O09O10.json` | 4032 / `294e48d2bea8` | 4911 / `25524a011e5e` | 00:47:10 |

The O receipt set did **not** move: `sweep/sweep-receipt.json`
(53614 / `25bcbc22b0f0`), `sweep/receipt-O06/O07/O08.json` and
`sweep/commands.txt` still carry their 00:44:42Z bytes at the 00:47:2xZ reads —
so the receipts this census indexed remain current, while the runner and
auditor tools around them were rewritten (the r31 pattern of dated mid-wave
tool revisions; the O-lane owns whether its audits needed a re-run against the
new runner bytes). The table above stays as filed — a dated historical cut,
per this round's append-only discipline; the parent integrates against current
bytes, not this table's.

One arrival outside the census partition, recorded for completeness:
`corpus/lessons/round-32.md` (12879 bytes, sha256 prefix `8aacfc2bd9f5`, mtime
00:43:27Z) appeared in `git status` at the recount. It is not this seat's
file, not indexed as a round-32 report fragment here, and its ownership
belongs to whichever seat's assignment covers the corpus partition.
