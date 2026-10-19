# R32-X20 — fragment index (the regimen's final census)

Seat **SCRIBE X20**, round 32, loop 3, GLM round 2 of 2 — **the regimen's final
round**. Axes: **C / calibration** (the completion-criterion audit),
**O / operability** (the r32 final sweep), **D / depth** (the final dossier).
The contract is `reports/round-32/claims.json` (read **2026-10-19T00:31Z**); the
declared baseline is `17e90b9047b289d7a63180a1dc1bebb074137e29` (the round-31
admit) and the declaration commit is lane HEAD
`4d500501a286d96f2eea8a6188c649255581301a` ("round-32: declare THE FINAL ROUND
claims C/O/D", 2026-10-18T21:30:17-03:00), whose parent X20 verified equal to
the baseline at **2026-10-19T00:33:33Z**. All worker observation times in this
index are UTC and fall on **2026-10-19** — the wall clock rolled past midnight
UTC during the wave, while the declaration artifacts carry date 2026-10-18.
`reports/round-32/targets.json` allocates C-completion 5, O-sweep 5, D-dossier
4 and X 2 — **16 requested seats**, which are declarations, not observed
launches or completions.

This index records the dated fragment census — the regimen's final one — and
bounded conformance readings. It does **not** admit the round, settle claims
C/O/D, attribute attendance, assess the served upstream model, or issue
canon/promotion/closure verdicts. A file being indexed does not mean its
controls passed. X20 wrote **only this file**: no scratch script (every probe
below is an inline `python3 -B -` or read-only shell heredoc), no source, gate,
packet, pin, old-round or shared-bookkeeping edit; no commit or push. Commands
ran inside this lane with `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`; the protected-history replay also sets
`GIT_OPTIONAL_LOCKS=0`. Both TMPDIR legs were exercised at **00:33:33Z**
(`$PWD/.scratch` and `/var/tmp` tempfile create/unlink, each OK). No
historical validator and no `run-validation.py` invocation was made by X20
beyond reading its bytes.

## Evidence cut and availability

**Worker-completion cut, not round acceptance.** Dependencies were sampled with
a 60-second diff poller (15 samples, 00:34:15Z–00:48:15Z, within the polling
bound; `POLL-DONE 00:48:15` at the sample cap with the wave still landing), then
direct 60-second checks to **00:48:32Z** — the 15-minute cap. A second direct
checker in that window reported false NOCHANGE rows: its `-newermt` window was
parsed in local −0300, silently matching nothing; the defect was caught by
cross-checking against the diff poller's log and is recorded here as dated
tooling history. Inventory command/date:
`find reports/round-32 -type f ! -path '*__pycache__*' ! -name '*.pyc'
! -name '*.pyo' -printf '%s %T@ %p\n' | sort -k3`, samples **2026-10-19**;
later rows are the two dated census cuts below.

| observation UTC, 2026-10-19 | new at this reading | meaning |
|---|---|---|
| 00:34:15 | 5 files | Declaration pair + X19 telemetry inputs (byte-identical copies) + worker observation. |
| 00:35:15 | +5 | X19 telemetry core (`check`, `controls`, `controls-vartmp`, `dispatch-stats`, `dispatch-telemetry.py`) — 10 files. |
| 00:37:15 | +1 | `sweep-audit.py` v1 (17,948 B). |
| 00:38:15 | +4 | C audit draft v1 (9,209 B), C ledger v1 (48,661 B), `sweep-audit-O09.json` v1 (60,214 B), `sweep/run-sweep.py` v1 (32,296 B). |
| 00:39:15 | +4 | `dossier-d11` (14,001 B), `dossier-d12` (10,338 B), `sweep-audit-O09O10.json` v1 (4,032 B), `sweep-audit-O10.json` v1 (60,215 B); C ledger v2 (52,655 B). |
| 00:40–00:42 | rewrites + d13, scope, dossier | `dossier-d13` (8,989 B), `scope.md` (17,932 B), `final-dossier.md` (9,733 B), C audits C04/C05; iterative rewrites of the C audit/ledger across every sample. |
| 00:43:31 | C settled | `completion-audit.md` + `completion-ledger.json` (55,253 B) final at this mtime. |
| 00:44:02 | census cut A | **25 files, 401,471 bytes** — superseded; `final-sweep.md`, the `sweep/` receipts and the audit rewrites had not landed. |
| 00:47–00:49 | O burst | `sweep-audit.py` v2 (19,173 B), O09/O10/O09O10 refiled, `run-sweep.py` v2 (32,517 B), `sweep/commands.txt`, `sweep/sweep-receipt.json`, `sweep/receipt-O{06,07,08}.json`, `final-sweep.md` (15,310 B), `run-validation.py` v-final (56,421 B), D14's `scribe/fragment-ledger.md`. |
| **00:49:52** | **census cut B** | **32 files, 642,787 bytes** — the authoritative table below. Only the parent-owned `validation.json` is absent at this cut. |
| 00:50:29–00:53:57 | O rewrites, 0 arrivals | **Cut-B staleness window — open-ended at filing.** The O lane kept iterating after cut B: a first burst touched `run-sweep.py`, `sweep-audit.py`, `run-validation.py`, O09/O10 (00:50–00:53Z); a second touched `final-sweep.md`, `sweep/sweep-receipt.json`, `sweep/receipt-O{06,07,08}.json`, `sweep/commands.txt`, `sweep-audit-O09.json` (00:53:54–57Z). **No cut-B digest row for any O-lane artifact may be used for acceptance binding**; the dated rows remain history, and the binding record is a fresh C1 run taken after the wave stops changing (C1 prints the live table and the drift list). Both filed C1 replays (00:52–00:54Z) passed structure/negatives/protected controls with an empty arrivals list throughout. |

**Mid-wave rewrites are dated history, not erasures:** the C audit/ledger pair
was rewritten at least five times before settling (48,661 → 52,655 → 53,565 →
52,701 → 54,890 → 55,253 B), `sweep-audit.py` grew 17,948 → 19,173 B, the O09/
O10/O09O10 receipts were refiled twice, and the O sweep build was re-cut at
00:49:17Z, 35 seconds before cut B. The earlier bytes stay superseded history;
any acceptance must bind the current bytes and confirm the wave has stopped
changing first.

## Required-artifact and conformance map

| claim / obligation | evidence surface | conformance boundary |
|---|---|---|
| C: completion-criterion audit, end-to-end | `completion-audit.md`; `completion-ledger.json`; `completion-audit-C04.md`; `completion-audit-C05.md` | The r32 ledger (audited_at 2026-10-18T21:43:31-03:00, lane_head `4d50050`) keeps **24 rows for rounds 8–31**, verdicts **19 closed-admitted / 3 closed-rejected / 1 operator-skipped / 1 closed-with-finding**, `zero_missing_rows: true`, plus `rounds_1_7`, `round_32`, `criterion_holds_through_round_31` and `manifest_closure_entries_8_31` keys and `claim_C_verdict: "verify"`. It supersedes the filed r31 ledger snapshot (which still shows 31 `in-flight` at its 22:41Z audit time) — dated history, not an erasure. X20 verified the r31 admission chain independently: LOG.md admission entry, admit commit `17e90b9`, `reports/round-31/validation.json` with `acceptance_checks_passed: true` and C/D/O all passed, fleet report `/home/vgpnk/Projects/shokunin/.ufo/reports/round-31/kotodama.md` (filed 21:29-0300). |
| O: the r32 final sweep | `final-sweep.md`; `sweep/run-sweep.py`; `sweep/commands.txt`; `sweep/sweep-receipt.json`; `sweep/receipt-O{06,07,08}.json` | The consolidated sweep records **51 green rows per pass — the r31 sweep's 50-command matrix plus round 32's own harness selftest — all exit 0 in every pass**, plus the **13 filed-red historical controls at their expected codes** (scoped exactly like r31). Receipt: seat R32-O06..O08, `passed: true`, measured 00:45:55Z, completed 00:49:17Z, `law_clean_findings: 0`. The claims' "100% exit 0" holds **only under that scoping** — an unconditional 100% over every executed command would contradict the 13 kept-red controls. |
| O: independent audit of the sweep surface | `sweep-audit.py` + `sweep-audit-O09.json` / `-O10.json` / `-O09O10.json` | Two legs over the round-32 sweep build with per-leg counting command `python3 -B reports/round-32/sweep-audit.py`, baseline/head recorded; the combined receipt pins `claims_json_sha256` and `targets_json_sha256` (both match X20's byte reads) and honestly records `tree_clean_at_start: false` — true mid-wave untracked state, not a defect. X20 read the receipts' summary fields, not their full bodies. |
| D: final dossier | `final-dossier.md` + `dossier-d11-shonen-boxes.md` / `-d12-capability-inventory.md` / `-d13-operator-decisions.md` | Assembled by D11/D12/D13 from sibling fragments; head declares **no promotion, canon, clearance or closure verdict** and a non-author declaration. Its evidence-cut note says the sibling C/O artifacts were "not yet landed" at its byte-check time — true at its reading, superseded by cut B where they all exist; a reader should bind dossier citations to cut-B bytes. |
| D14: peer fragment ledger | `scribe/fragment-ledger.md` | R32-D14's read-time census + limits record for parent integration. Deliberately overlaps this index (two scribe instruments over different populations); neither attests attendance, runtime concurrency or the served model. |
| X19: durable telemetry | `telemetry/` (8 files) | Inputs snapshots byte-identical to the declarations (sha8 `043dcc6c` / `906c23a2`); `controls-vartmp.json` present — the `/var/tmp` mirror leg is covered at this seat; full-wave status fields per AGENTS.md convention. Worker self-observation only — not a fleet census. |
| X: protected-surface watch | `scope.md` (17,932 B) | Present at cut; **not depth-read by X20** — its verdict is not counted here. |
| all: protected history | C1 block below | X20's independent check at **00:33:33Z**: `git ls-tree -r` vs baseline `17e90b9` over `reports/round-{8..31}` + `tools/gates/frozen/round-{8..31}` — **1,870 tracked paths, 0 byte differences, 0 protected status rows**. (r31's index checked 8–30: 1,823 paths; the delta is round 31's own 47 now-filed paths.) Frozen roots `tools/gates/frozen/round-{3,4}` predate the audited window and are outside it. |
| regimen-wide final census | table below | Per-round evidence tally at **2026-10-19T00:36Z**: `reports/round-5..32` = **1,824 files / 34,185,508 bytes** (caches excluded); the round-32 row of that tally (10 files / 23,749 B) is a mid-wave reading superseded by cut B. The landed jin'i-ryu rule's retroactive act is visible in-tree: five closing snapshots filed 23:50:30Z (2026-10-18), all tracked at baseline. |
| jin'i-ryu integrity leg | `reports/round-{19,25,26,27,28}/telemetry/availability-close-*.json` | X20 re-checked all five at **00:42:17Z**: every `closes_sha256` matches the live `availability.json` bytes and every `validation_sha256` matches the live `validation.json` bytes (**5/5 + 5/5**); closed fields 12/12, 26/26, 24/24, 24/24, 24/24 with honest `could_not_recover` lists. The rule's falsification condition (ii) holds at this read. |

## Conformance observations during integration

1. **No acceptance receipt exists at the census cut.** `run-validation.py`
   (56,421 B, sha8 `154e314b`, mtime 00:48:53Z at cut B) is present but
   `validation.json` is not, and X20 did not execute the runner. This index is
   part of any later read set, so a receipt produced before the wave settles
   would be stale by construction; the parent reruns after the wave stops
   changing and checks runner/input binding on the receipt it accepts.
2. **Cut B is 35 seconds behind the O burst — and the wave kept resuming.**
   `final-sweep.md`, `sweep/commands.txt`, `sweep/sweep-receipt.json` and the
   three O-leg receipts all carry mtime 00:49:17Z; cut B read them at
   00:49:52Z with zero unstable reads. The O lane then rewrote artifacts in
   at least two further bursts (00:50–00:53Z and 00:53:54–57Z; see the
   evidence-cut addendum row). C1 reports drift as staleness, not as a
   worker failure — the parent must take a fresh dated reading after the
   wave settles and bind acceptance to those bytes, never to cut B's O rows.
3. **"100% exit 0" is scoped, not absolute.** 51 green rows per pass; 13
   historical controls deliberately replay to their expected filed-red codes.
   The claims contract and the receipt must be read together — the same
   reconciliation the parent owed round 31's admission.
4. **Two ledgers, two generations.** The filed r31 `closure-ledger.json`
   (protected, 22:41Z audit, round 31 `in-flight`) and the r32
   `completion-ledger.json` (00:43:31Z audit, round 31 `closed-admitted`) are
   successive dated snapshots; the r32 artifact is the criterion's current
   record and the r31 artifact stays filed history. The parent's admission
   text should name the supersession explicitly.
5. **Fleet slot is shared across lanes.** At 00:36Z and again at 00:44Z,
   `/home/vgpnk/Projects/shokunin/.ufo/reports/round-32/` held only
   `kumitate.md` — another lane's report. Kotodama's round-32 fleet report is
   still owed at integration; the round-31 precedent (`kotodama.md` filed at
   21:29-0300 alongside the admit) is the pattern to repeat.
6. **Manifest durability.** The C audit cites the authoritative fleet
   `/home/vgpnk/Projects/shokunin/MANIFEST.json` (251,143 B, mtime 21:29-0300,
   outside this repo). The lane-local `.scratch/MANIFEST.json` is gitignored
   working state and must not be cited as the closure record.
7. **Telemetry coexistence, not duplication.** X19's durable snapshot, the X
   scope watch, D14's ledger and this census are four instruments over
   different populations; none attests full-wave attendance, runtime
   concurrency or the served model. Counts here are read-time, not atomic.

## Regimen-wide final census (dated 2026-10-19T00:36Z)

Command: per-`round` `rglob('*')` file count / byte sum / latest mtime (UTC),
caches excluded; same run also tallied `tools/gates/frozen/round-*`.

| evidence root | files | bytes | latest mtime (UTC) |
|---|---:|---:|---|
| `reports/round-5` | 23 | 209,862 | 10-18T16:13Z |
| `reports/round-6` | 20 | 227,610 | 10-18T13:00Z |
| `reports/round-7` | 17 | 223,339 | 10-18T16:14Z |
| `reports/round-8` | 153 | 2,063,222 | 10-17T23:30Z |
| `reports/round-9` | 90 | 2,055,621 | 10-18T13:03Z |
| `reports/round-10` | 73 | 1,214,772 | 10-17T23:57Z |
| `reports/round-11` | 254 | 1,922,137 | 10-17T22:33Z |
| `reports/round-12` | 44 | 515,904 | 10-18T00:03Z |
| `reports/round-13` | 2 | 3,222 | 10-17T23:38Z |
| `reports/round-14` | 40 | 1,228,250 | 10-18T00:22Z |
| `reports/round-15` | 20 | 1,019,280 | 10-18T02:26Z |
| `reports/round-16` | 23 | 927,047 | 10-18T09:11Z |
| `reports/round-17` | 67 | 1,483,571 | 10-18T10:06Z |
| `reports/round-18` | 60 | 1,174,360 | 10-18T11:28Z |
| `reports/round-19` | 72 | 542,155 | 10-18T23:50Z |
| `reports/round-20` | 82 | 2,389,014 | 10-18T13:45Z |
| `reports/round-21` | 45 | 410,513 | 10-18T14:36Z |
| `reports/round-22` | 79 | 1,029,774 | 10-18T15:53Z |
| `reports/round-23` | 44 | 1,599,328 | 10-18T16:02Z |
| `reports/round-24` | 20 | 318,794 | 10-18T17:21Z |
| `reports/round-25` | 68 | 1,173,859 | 10-18T23:50Z |
| `reports/round-26` | 104 | 2,277,832 | 10-18T23:50Z |
| `reports/round-27` | 131 | 3,407,663 | 10-18T23:50Z |
| `reports/round-28` | 135 | 3,861,782 | 10-18T23:50Z |
| `reports/round-29` | 46 | 492,810 | 10-18T21:50Z |
| `reports/round-30` | 60 | 1,348,647 | 10-18T22:32Z |
| `reports/round-31` | 42 | 1,041,391 | 10-19T00:28Z |
| `reports/round-32` (mid-wave) | 10 | 23,749 | 10-19T00:34Z |
| **total `reports/round-5..32`** | **1,824** | **34,185,508** | — |
| `tools/gates/frozen/round-3` | 28 | 421,227 | (pre-window) |
| `tools/gates/frozen/round-4` | 5 | 4,726 | (pre-window) |
| `tools/gates/frozen/round-11` | 19 | 653,543 | (in-window) |
| `tools/gates/frozen/round-18` | 13 | 513,114 | (in-window) |
| `tools/gates/frozen/round-20` | 6 | 331,524 | (in-window) |
| `tools/gates/frozen/round-22` | 39 | 1,142,877 | (in-window) |
| `tools/gates/frozen/round-23` | 15 | 332,779 | (in-window) |
| `tools/gates/frozen/round-25` | 14 | 825,667 | (in-window) |
| `tools/gates/frozen/round-26` | 32 | 2,311,669 | (in-window) |

The 23:50Z mtimes on rounds 19 and 25–28 are the five `telemetry/
availability-close-*.json` snapshots — the jin'i-ryu landing's retroactive
act, executed once (all five within the same second) before the round-31 admit.

## Census

Executed **2026-10-19T00:49:52Z**, exit **0**: **32 files**, **642,787 bytes**,
excluding this index and Python caches. Partitions: root 17, scribe 1, sweep 6,
telemetry 8. No failed read, no file changed inside its individual read, and no
strict-JSON error (duplicate-key-rejecting parser) was observed. Sequential
read-time census, **not an atomic snapshot**; the self row is excluded as
circular. C1 regenerates a live table without rewriting these dated rows.

<!-- X20:CENSUS:BEGIN -->
| artifact | bytes | sha8 | mtime UTC | inferred owner / evidence state |
|---|---:|---|---|---|
| `reports/round-32/claims.json` | 2558 | `043dcc6c` | 2026-10-19T00:30:17Z | parent declaration |
| `reports/round-32/completion-audit-C04.md` | 10356 | `0157a001` | 2026-10-19T00:41:45Z | C completion-audit evidence |
| `reports/round-32/completion-audit-C05.md` | 10120 | `2c166510` | 2026-10-19T00:42:24Z | C completion-audit evidence |
| `reports/round-32/completion-audit.md` | 10376 | `01bbac20` | 2026-10-19T00:43:31Z | C completion-audit evidence |
| `reports/round-32/completion-ledger.json` | 55253 | `b90ed472` | 2026-10-19T00:43:31Z | C completion evidence |
| `reports/round-32/dossier-d11-shonen-boxes.md` | 14001 | `e5b34e19` | 2026-10-19T00:39:03Z | D final dossier |
| `reports/round-32/dossier-d12-capability-inventory.md` | 10338 | `c4765bf3` | 2026-10-19T00:39:49Z | D final dossier |
| `reports/round-32/dossier-d13-operator-decisions.md` | 8989 | `1ededf01` | 2026-10-19T00:40:32Z | D final dossier |
| `reports/round-32/final-dossier.md` | 9733 | `b82319b5` | 2026-10-19T00:41:54Z | D final dossier |
| `reports/round-32/final-sweep.md` | 15310 | `9853c351` | 2026-10-19T00:49:17Z | O final-sweep evidence |
| `reports/round-32/run-validation.py` | 56421 | `154e314b` | 2026-10-19T00:48:53Z | acceptance instrument, not verdict |
| `reports/round-32/scope.md` | 17932 | `da1bd1f4` | 2026-10-19T00:41:10Z | X scope watch |
| `reports/round-32/scribe/fragment-ledger.md` | 16792 | `fccb8f9b` | 2026-10-19T00:48:11Z | D14 peer fragment ledger |
| `reports/round-32/sweep/commands.txt` | 3681 | `60309bfc` | 2026-10-19T00:49:17Z | O sweep-build evidence (runner, receipt, O06–O08 legs) |
| `reports/round-32/sweep/receipt-O06.json` | 48947 | `37ce3736` | 2026-10-19T00:49:17Z | O sweep-build evidence (runner, receipt, O06–O08 legs) |
| `reports/round-32/sweep/receipt-O07.json` | 48953 | `2fba9dc8` | 2026-10-19T00:49:17Z | O sweep-build evidence (runner, receipt, O06–O08 legs) |
| `reports/round-32/sweep/receipt-O08.json` | 48954 | `91b67eeb` | 2026-10-19T00:49:17Z | O sweep-build evidence (runner, receipt, O06–O08 legs) |
| `reports/round-32/sweep/run-sweep.py` | 32517 | `907fda67` | 2026-10-19T00:45:47Z | O sweep-build evidence (runner, receipt, O06–O08 legs) |
| `reports/round-32/sweep/sweep-receipt.json` | 53611 | `8677f88c` | 2026-10-19T00:49:17Z | O sweep-build evidence (runner, receipt, O06–O08 legs) |
| `reports/round-32/sweep-audit-O09.json` | 61228 | `f79044c3` | 2026-10-19T00:48:29Z | O sweep-audit evidence |
| `reports/round-32/sweep-audit-O09O10.json` | 5117 | `f6fe4972` | 2026-10-19T00:49:07Z | O sweep-audit evidence |
| `reports/round-32/sweep-audit-O10.json` | 61236 | `e5ebb431` | 2026-10-19T00:49:07Z | O sweep-audit evidence |
| `reports/round-32/sweep-audit.py` | 19173 | `3d70085a` | 2026-10-19T00:47:47Z | O sweep-audit evidence |
| `reports/round-32/targets.json` | 187 | `906c23a2` | 2026-10-19T00:30:17Z | parent declaration |
| `reports/round-32/telemetry/check.json` | 219 | `d740d97e` | 2026-10-19T00:34:36Z | X19 durable telemetry |
| `reports/round-32/telemetry/controls-vartmp.json` | 1886 | `379b52ea` | 2026-10-19T00:34:36Z | X19 durable telemetry |
| `reports/round-32/telemetry/controls.json` | 1934 | `8fe6fc43` | 2026-10-19T00:34:36Z | X19 durable telemetry |
| `reports/round-32/telemetry/dispatch-stats.json` | 2403 | `8316c0d4` | 2026-10-19T00:34:36Z | X19 durable telemetry |
| `reports/round-32/telemetry/dispatch-telemetry.py` | 10531 | `289744bc` | 2026-10-19T00:34:29Z | X19 durable telemetry |
| `reports/round-32/telemetry/inputs/claims.json` | 2558 | `043dcc6c` | 2026-10-19T00:33:28Z | X19 durable telemetry |
| `reports/round-32/telemetry/inputs/targets.json` | 187 | `906c23a2` | 2026-10-19T00:33:28Z | X19 durable telemetry |
| `reports/round-32/telemetry/worker-observation.json` | 1286 | `f10ffe07` | 2026-10-19T00:33:40Z | X19 durable telemetry |
<!-- X20:CENSUS:END -->

Names in the census are path/partition-based **inferences**, not a native
dispatch roster. Hash prefixes are diagnostic abbreviations, **not new frozen
pin rows**. All files are retained; only `__pycache__/`, `.pyc` and `.pyo` are
excluded. Failed reads and files changing while read are printed, not silently
omitted or counted green.

## C1 — reproducible census, binding and index controls

Run this exact block from the lane root. It writes no files and executes no
historical validator or acceptance runner. It prints a new dated inventory and
a drift-aware replay of this index; arrivals/digest changes are **staleness**,
not missing-worker or quality verdicts. Controls reject duplicate rows, a
missing path, altered byte size, altered digest and duplicate JSON keys **in
memory**. The live table prints separately for a new dated census. Protected
history compares Git blob identities with the declared baseline over rounds
8–31 and the round-tagged frozen roots.

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1 GIT_OPTIONAL_LOCKS=0
python3 -B - <<'PY'
from collections import Counter
from datetime import datetime, timezone
import hashlib, json, re, subprocess
from pathlib import Path
BASE = Path('reports/round-32')
SELF = BASE / 'fragment-index-x20.md'
REV = '17e90b9047b289d7a63180a1dc1bebb074137e29'
def digest(data):
    return hashlib.sha256(data).hexdigest()
def pairs(items):
    out = {}
    for key, value in items:
        if key in out:
            raise ValueError('duplicate JSON key: ' + key)
        out[key] = value
    return out
def strict(text):
    return json.loads(text, object_pairs_hook=pairs)
def category(relative):
    parts = Path(relative).relative_to(BASE).parts
    name = parts[-1]
    if len(parts) > 1:
        return {'telemetry': 'X19 durable telemetry',
                'sweep': 'O sweep-build evidence (runner, receipt, O06–O08 legs)',
                'scribe': 'D14 peer fragment ledger'}.get(parts[0], 'unassigned: ' + parts[0])
    if name in ('claims.json', 'targets.json'):
        return 'parent declaration'
    if name == 'completion-ledger.json':
        return 'C completion evidence'
    if name.startswith('completion-audit'):
        return 'C completion-audit evidence'
    if name.startswith('dossier-') or name == 'final-dossier.md':
        return 'D final dossier'
    if name == 'final-sweep.md' or name.startswith('sweep-audit'):
        return 'O final-sweep evidence'
    if name == 'scope.md':
        return 'X scope watch'
    if name == 'run-validation.py':
        return 'acceptance instrument, not verdict'
    if name == 'validation.json':
        return 'acceptance receipt: check binding'
    return 'unassigned'
rows, errors, unstable, bad_json = [], [], [], []
for path in sorted(BASE.rglob('*')):
    if not path.is_file() or path == SELF or '__pycache__' in path.parts or path.suffix in ('.pyc', '.pyo'):
        continue
    try:
        before = path.stat()
        raw = path.read_bytes()
        after = path.stat()
        if (before.st_size, before.st_mtime_ns) != (after.st_size, after.st_mtime_ns):
            unstable.append(str(path))
        if path.suffix == '.json':
            try:
                strict(raw.decode())
            except (ValueError, UnicodeError) as exc:
                bad_json.append({'path': str(path), 'error': str(exc)})
        rows.append((str(path), len(raw), digest(raw)[:8],
                     datetime.fromtimestamp(after.st_mtime, timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'), category(str(path))))
    except OSError as exc:
        errors.append({'path': str(path), 'error': str(exc)})
actual = {p: (size, sha8) for p, size, sha8, _, _ in rows}
text = SELF.read_text()
section = text.split('<!-- X20:CENSUS:BEGIN -->', 1)[1].split('<!-- X20:CENSUS:END -->', 1)[0]
indexed = [(p, int(size), sha8) for p, size, sha8 in re.findall(
    r'(?m)^\| `([^`]+)` \| (\d+) \| `([a-f0-9]{8})` \|', section)]
def conforms(items, expected):
    names = [p for p, _, _ in items]
    return len(names) == len(set(names)) and set(names) == set(expected) and all(expected.get(p) == (size, sha8) for p, size, sha8 in items)
probe = [(str(BASE / 'CONTROL.json'), 2, digest(b'{}')[:8])]
expected = {probe[0][0]: probe[0][1:]}
checks = {'positive_exact_snapshot': conforms(probe, expected),
          'negative_duplicate': not conforms(probe + probe, expected),
          'negative_missing_path': not conforms([(str(BASE / 'ABSENT.json'), 2, probe[0][2])], expected),
          'negative_size': not conforms([(probe[0][0], 3, probe[0][2])], expected),
          'negative_digest': not conforms([(probe[0][0], 2, '0'*8)], expected)}
try:
    strict('{"id": 1, "id": 2}')
except ValueError:
    checks['negative_duplicate_json_key'] = True
else:
    checks['negative_duplicate_json_key'] = False
names = [p for p, _, _ in indexed]
receipt_path, runner_path = BASE / 'validation.json', BASE / 'run-validation.py'
receipt = strict(receipt_path.read_text()) if receipt_path.is_file() else {}
runner_sha = digest(runner_path.read_bytes()) if runner_path.is_file() else None
inputs = receipt.get('input_sha256', {})
input_drift = [p for p, sha in inputs.items() if not Path(p).is_file() or digest(Path(p).read_bytes()) != sha]
roots = [f'{root}/round-{number}' for root in ('reports', 'tools/gates/frozen') for number in range(8, 32)]
entries = subprocess.check_output(['git', 'ls-tree', '-r', '-z', REV, '--', *roots]).split(b'\0')
protected, changed = 0, []
for entry in entries:
    if not entry:
        continue
    meta, rawpath = entry.split(b'\t', 1)
    _, kind, oid = meta.decode().split()
    if kind != 'blob':
        continue
    protected += 1
    path = Path(rawpath.decode())
    raw = path.read_bytes() if path.is_file() else None
    observed = hashlib.sha1(b'blob ' + str(len(raw)).encode() + b'\0' + raw).hexdigest() if raw is not None else None
    if observed != oid:
        changed.append(str(path))
status = subprocess.check_output(['git', 'status', '--porcelain=v1', '-uall', '--', *roots], text=True).splitlines()
summary = {'observed_at_utc': datetime.now(timezone.utc).isoformat(),
    'command': 'C1: python3 -B - (exact block in fragment-index-x20.md)',
    'files_excluding_self_and_caches': len(rows), 'bytes': sum(r[1] for r in rows),
    'partitions': dict(sorted(Counter(Path(r[0]).relative_to(BASE).parts[0] if len(Path(r[0]).relative_to(BASE).parts)>1 else '(root)' for r in rows).items())),
    'read_errors': errors, 'changed_during_read': unstable, 'json_errors': bad_json,
    'index_rows': len(indexed), 'duplicate_index_rows': len(names) != len(set(names)),
    'unavailable': sorted(set(names)-set(actual)), 'arrivals_since_census': sorted(set(actual)-set(names)),
    'digest_or_size_drift': [p for p, size, sha8 in indexed if actual.get(p) != (size, sha8)],
    'snapshot_current': conforms(indexed, actual), 'controls': checks,
    'runner_present': runner_path.is_file(), 'receipt_present': receipt_path.is_file(),
    'runner_sha256_live': runner_sha, 'runner_sha256_receipt': receipt.get('runner_sha256'),
    'runner_bound': runner_sha is not None and runner_sha == receipt.get('runner_sha256'),
    'receipt_measured_at_utc': receipt.get('measured_at_utc'),
    'acceptance_checks_passed': receipt.get('acceptance_checks_passed'),
    'claims': {k: v.get('passed') for k, v in receipt.get('claims', {}).items()},
    'receipt_input_drift': input_drift, 'missing_dependencies': receipt.get('missing_dependencies'),
    'protected_paths': protected, 'protected_byte_differences': changed, 'protected_status_rows': status}
print(json.dumps(summary, indent=2))
print('| artifact | bytes | sha8 | mtime UTC | inferred owner / evidence state |')
print('|---|---:|---|---|---|')
for path, size, sha8, modified, owner in rows:
    print(f'| `{path}` | {size} | `{sha8}` | {modified} | {owner} |')
assert all(checks.values()) and not errors and not unstable and not bad_json
assert indexed and len(names) == len(set(names)) and not (set(names)-set(actual))
assert not changed and not status
print('INDEX_STRUCTURE_AND_NEGATIVES=PASS; snapshot_current=' + str(summary['snapshot_current']))
PY
```

## Verification record and boundaries

- **2026-10-19T00:31Z**, read-only `cat` of `claims.json`/`targets.json` and
  directory listings: the contract and allocation as cited above.
- **2026-10-19T00:33:33Z**, read-only `python3 -B -` using `git ls-tree -r
  17e90b9047b289d7a63180a1dc1bebb074137e29 -- reports/round-{8..31}
  tools/gates/frozen/round-{8..31}`, per-path Git blob SHA-1 of live bytes and
  `git status --porcelain=v1 -uall -- <same roots>`: **1,870 tracked paths**,
  **0 byte differences**, **0 protected status rows**. Lane HEAD `4d50050` was
  not confused with the declared baseline; `git rev-parse HEAD^` returned the
  baseline exactly. The same batch exercised both TMPDIR legs (scratch and
  `/var/tmp` tempfile create/unlink): both OK.
- **2026-10-19T00:34:15–00:48:15Z**, the 60-second diff poller (15 samples):
  the arrival/rewrite history summarized in the evidence-cut table, ending
  `POLL-DONE 00:48:15` at the sample cap with the O burst still landing.
- **2026-10-19T00:42:17Z**, integrity leg of the landed jin'i-ryu rule:
  `sha256(live bytes)` vs `closes_sha256`/`validation_sha256` in all five
  `telemetry/availability-close-{19,25,26,27,28}.json` — **5/5 + 5/5 match**.
  The five snapshots' mtimes all read 2026-10-18T23:50:30Z (one second, one
  act) and all five are tracked at the baseline.
- **2026-10-19T00:43–00:44Z**, bounded reads: r31 `validation.json`
  (`acceptance_checks_passed: true`, C/D/O all passed), r31
  `closure-ledger.json` shape (24 rows, 31 `in-flight`, `zero_missing_rows:
  true`), r31 fleet report and the authoritative fleet `MANIFEST.json` present
  at 251,143 B; then census cut A (25 files / 401,471 B, 0/0/0 errors).
- **2026-10-19T00:45–00:48Z**, a direct 60-second re-check reported false
  NOCHANGE rows: its `-newermt` window was parsed in local −0300 and silently
  matched nothing. Recorded as dated tooling history; the diff poller's log is
  the controlling instrument for that window. No conclusion in this index
  rests on the buggy checker's output.
- **2026-10-19T00:49:52Z**, census cut B: 32 files / 642,787 bytes / 0 read
  errors / 0 unstable reads / 0 strict-JSON errors — the table above. Bounded
  head/summary reads the same minute: `final-sweep.md` verdict lines (51 green
  rows per pass + 13 controls), `sweep-receipt.json` summary (`passed: true`,
  measured 00:45:55Z, completed 00:49:17Z), `completion-ledger.json` shape
  (verdicts 19/3/1/1, `claim_C_verdict: "verify"`), D14's ledger head, and the
  three sweep-audit receipts' summary fields (including
  `tree_clean_at_start: false`).
- **2026-10-19T00:52–00:54Z**, the exact C1 block extracted from this filed
  index and executed via `bash` three times as the index was amended: every
  run exited **0** with `INDEX_STRUCTURE_AND_NEGATIVES=PASS`, **32 index
  rows**, no duplicates/unavailable rows, **0 arrivals**,
  **0 read/unstable/JSON errors**, and protected history again
  **1,870 / 0 / 0**; `receipt_present: false` throughout. The drift lists
  grew with the O lane's post-cut bursts (five rows at 00:52–53Z, ten rows at
  00:54Z), each naming exactly the artifacts the bursts touched —
  `snapshot_current: false` is the index's designed staleness signal, not a
  defect. A later reader reruns C1 for the current live table; the parent
  must confirm the wave has stopped changing before running acceptance.
  A final execution of the last filed block at **00:55:14Z** repeated the
  pass (exit 0, PASS; 11 drift rows after a further sweep-audit micro-burst
  at 00:54:32Z; 0 arrivals).
- **Scope limits:** X20 did not depth-read `scope.md`, `final-dossier.md`'s
  body, the C audit bodies, or any O receipt's full body beyond the summary
  fields quoted; did not execute `run-validation.py`, `sweep/run-sweep.py`,
  `sweep-audit.py` or any gate; did not assess fleet-root cleanliness beyond
  the two dated directory listings, canon, rights or peer semantics; and does
  not attribute worker attendance. All counts above carry their commands and
  the date 2026-10-19 (wall clock; declaration artifacts dated 2026-10-18).

### Parent integration still required at handoff

1. Confirm the wave has stopped changing, then run
   `reports/round-32/run-validation.py` on the final read set and bind the
   receipt to the live runner and read-set digests; reconcile claim O's
   "100% exit 0" phrasing against the 51-green + 13-expected-red scoping in
   the admission text.
2. Write the round-32 fleet report at
   `/home/vgpnk/Projects/shokunin/.ufo/reports/round-32/kotodama.md` (the
   slot is shared; `kumitate.md` is another lane's file) and the round-32
   closure entry in the authoritative fleet `MANIFEST.json`, closing the
   criterion's last by-construction slot; record the r32 completion-ledger's
   supersession of the r31 ledger snapshot in the admission.
3. Integrate LOG/SCORECARD append-only; if a later fragment census is needed,
   rerun C1 for a new dated reading. No round admission, claim verdict, or
   promotion decision is issued by X20.

FILES: reports/round-32/fragment-index-x20.md | SUMMARY: X20 filed the regimen's final census — 32-artifact dated cut B with full C/O/D/X conformance map, protected history 1,870/0/0, jin'i-ryu integrity 5/5, regimen-wide tally (1,824 files), scoped-sweep and supersession observations — and a passing drift-aware C1; the parent's validation.json, fleet report and MANIFEST closure remain outstanding.
