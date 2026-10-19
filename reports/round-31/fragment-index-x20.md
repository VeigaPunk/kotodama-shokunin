# R31-X20 — fragment index + conformance

Seat **SCRIBE X20**, round 31, loop 3, GLM round 1 of 2 — regimen close-out.
Axes: **C / calibration** (the rounds 8–32 closure ledger), **O / operability**
(the final green sweep), **D / depth** (the jin'i-ryu self-improvement move).
The contract is `reports/round-31/claims.json` (read **2026-10-18**); the
declared baseline is `71cd9d376ebd144e94e4f12d997f73e5d2839aa9` (round-30
admit) and the declaration commit is lane HEAD
`e8d2d0dadd3ccd1fbb7481793cfaf9bcd761826c`, whose parent is the baseline.
`reports/round-31/targets.json` allocates C-closure 5, O-sweep 6, D-jinii 3 and
X 2 — **16 requested seats**, which are declarations, not observed launches or
completions.

This index records the dated fragment census and bounded conformance readings.
It does **not** admit the round, settle claims C/O/D, attribute attendance,
assess the served upstream model, or issue canon/promotion verdicts. A file
being indexed does not mean its controls passed or its draft was landed. X20
wrote **only this file**: no scratch script, no source, gate, packet, pin,
old-round or shared-bookkeeping edit; no commit or push. Commands ran inside
this lane with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; the
protected-history replay also sets `GIT_OPTIONAL_LOCKS=0`. No mirror-safety
`/var/tmp` leg was launched by this seat (X19's receipt covers that class).
No historical validator and no `run-validation.py` invocation was made by X20
beyond reading its bytes.

## Evidence cut and availability

**Worker-completion cut, not round acceptance.** Dependencies were sampled with
60–80-second sleeps during this seat's work, within the polling bound; the last
missing dependency at filing is the parent-owned `validation.json` receipt. A
later arrival requires a new dated reading, never an inferred worker failure.
Inventory command/date for the 22:45:31Z row: `find reports/round-31 -type f
! -path '*__pycache__*' ! -name '*.pyc' ! -name '*.pyo' | sort` with per-file
`stat -c%s` and `date -u -r`, **2026-10-18**; later rows are dated directory
readings plus the 23:20:32Z full census below.

| observation UTC, 2026-10-18 | new at this reading | meaning |
|---|---|---|
| 22:45:31 | 14 files inventoried | Declarations, C ledger, two D fragments, X19 telemetry core, sweep-audit tool v1 (13,335 B). |
| 22:46:48 | `sweep-audit-O09.json`, `sweep-audit-O10.json` | First O audit receipts (106,175 B each) — later superseded, see observation 2. |
| 22:48:28 | `closure-audit-C04.md`, `sweep-audit-O09O10.json` | C re-verification and the auditors' combined receipt v1. |
| 22:50:24 | `scope.md` | X16 scope watch lands. |
| 23:11:31 | `run-validation.py`, `closure-audit-C05.md` | Acceptance instrument present; second C re-verification. Audit tool/receipts already rewritten by this point. |
| 23:19:02 | `sweep/` partition (13 files), `sweep-audit-O09O10.md` | O builder surfaces: runner, r31-post freeze, receipt, commands; auditors' report. |
| 23:19:51 | `final-sweep.md` | O11's consolidated sweep lands; only the receipt remains outstanding. |
| 23:20:32 | census cut | **37 files, 716,175 bytes** — the authoritative table below. |

**Mid-wave rewrites are dated history, not erasures:** `sweep-audit.py` grew
13,335 → 14,281 bytes (mtime 23:15:03Z) and the O09/O10/O09O10 receipts were
re-filed at 23:15:44–23:16:22Z with different byte sizes (106,175 → 24,871 /
55,659); `sweep-audit-O09O10.md` (23:18:24Z) describes a "third post-fix set".
The earlier bytes stay superseded history; any acceptance must bind the
current bytes.

## Required-artifact and conformance map

| claim / obligation | evidence surface | conformance boundary |
|---|---|---|
| C: closure ledger rounds 8–31 audited, 32 pending | `reports/round-31/closure-ledger.json`; `closure-audit-C04.md`; `closure-audit-C05.md` | 24 rows for rounds 8–31 with per-row evidence fields; round 31 is `in-flight` (its fleet report and MANIFEST closure entry are owed at integration — X20 re-checked the fleet `.ufo/reports/round-31/` absence at 23:19:38Z); round 32 is pending-by-construction. `zero_missing_rows: true` counts the ledger's own row algebra, not fleet-root cleanliness. |
| C: content-validity verdicts | `closure-ledger.json` `verdicts` field | 18 closed-admitted, 3 closed-rejected (11, 17, 22), 1 closed-with-finding (23), 1 skipped-operator (13), 1 in-flight (31) — a rejected/skipped row is content-valid closure, not a green round. Claim verdict is `verify-with-named-finding` with a stated falsification condition. |
| C: independent re-verification | `closure-audit-C04.md` (6 rows: 8, 11, 17, 23, 29, 30) | C04 re-derived sections, commit ancestry, MANIFEST verdicts from raw sources and concluded `verify`; C05 landed at 23:12:28Z and was **not depth-read by X20** — its verdict is not counted here. |
| O: the final green sweep | `reports/round-31/final-sweep.md`; `sweep/run-sweep.py`; `sweep/sweep-receipt.json`; `sweep/commands.txt` | O11 records **50 green-surface rows, all exit 0**, plus **13 historical controls at their expected filed-red codes**; battery 10/10 (pinned 20); handoff v2/v3 green; argot + law clean; the new `r31-post` frozen generation replays 4/4. The claims' "100% exit 0" holds **only under that scoping** — an unconditional 100% over every executed command would contradict the 13 kept-red controls ("a reproduced red verdict stays red"). The parent/validator must reconcile contract phrasing with the receipt. |
| O: independent audit of the sweep surface | `sweep-audit.py` + `sweep-audit-O09.json` / `-O10.json` / `-O09O10.json` / `-O09O10.md` | Two sequential 40/40 exit-0 passes with stdout/stderr SHA-256 digests and a source snapshot that did not move during the passes (`/var/tmp` legs for the two recorded external-tmp tools). These audit the **round-30 recorded surface**, not O11's full matrix; digests are per-leg evidence, not frozen-pin rows. |
| D: jin'i-ryu delta, falsifiable | `jinii/analysis.md`, `jinii/draft.md` (D12/D13), `jinii/patch-draft.md` (D14) | **Two competing drafts, one gate:** D13 proposes the telemetry finalization-closure rule (AGENTS.md bullet + SKILL.md checklist row + five retroactive closing snapshots); D14 proposes "freeze follows re-point" (folding the TMPDIR rule as executable premise). Claim D asks for **ONE** landed improvement; selection, landing and the LOG.md delta + falsification entry are the orchestrator's. Both drafts edited no operating file — the protected check below confirms SKILL.md/AGENTS.md/PROVINCE.md unchanged vs baseline. |
| D: draft anchor accuracy | current `AGENTS.md` (31 lines), `SKILL.md` | D13's SKILL.md checklist anchor (append after :534, before "## Corpus map") matches; its AGENTS.md anchor "after :30" is **off by one** — the telemetry section's last line is :31. D14's citation "SKILL.md:294 still asserts the r22 d4-repin manifest replays '3 rows, exit 0'" **does not match the current text** at :294 (a propagation/tamper table row); the nearest d4-repin mention is :339, without a replay-count verdict. Re-anchor exact bytes before landing either patch; the substance is not adjudged here. |
| D13's audit premise | the draft's one-line census command | X20 re-ran it at **23:10:11Z**: exactly the five named records (rounds 19, 25, 26, 27, 28) print — the retroactive-closure act is well-defined at this read. |
| X19: durable telemetry | `telemetry/` (8 files) | `dispatch-stats.json` keeps full-wave status `could-not-evaluate` with owner+reason (AGENTS.md convention); requested allocation ≠ completions; `--check` exit 0 findings-empty; `--selftest` 10/10 both in `$PWD/.scratch` and `/var/tmp` mirror legs (`controls.json`, `controls-vartmp.json`). Worker self-observation only — not a fleet census. |
| X16: protected-surface watch | `scope.md` | Four 60-second samples over rounds 8–30 + round-tagged frozen roots (1,823 tracked paths), manifest bound to baseline blobs; supplemental all-frozen and ignored-file watches clean. Fleet scope deliberately not assessed. |
| all: protected history | C1 block below | X20's independent check at **22:48:58Z**: `git ls-tree -r` vs baseline over `reports/round-{8..30}` + `tools/gates/frozen/round-{8..30}` — **1,823 tracked paths, 0 byte differences, 0 protected status rows**; independent agreement with X16's watch. |

## Conformance observations during integration

1. **No acceptance receipt exists at the census cut.** `run-validation.py`
   (54,237 B, sha8 `8694b9c0`, mtime 23:14:17Z at the census cut) is present
   but `validation.json` is not, and X20 did not execute the runner. The
   runner was itself rewritten post-cut (55,588 B at 23:23:28Z, sha8
   `4574b924`) — the census row is the dated reading, C1 prints the live
   bytes. This index is part of any later read set, so a receipt produced
   before the wave settles would be stale by construction; the parent reruns
   after the wave stops changing and checks runner/input binding on the
   receipt it accepts.
2. **Audit receipts were superseded mid-wave.** The 22:46–22:48Z O receipts
   (106,175-byte bodies) differ from the filed 23:15–23:16Z ones (24,871 /
   55,659) and the audit tool changed in between; the .md report names the
   final set. The parent binds acceptance to the current tool/receipt bytes
   and treats the earlier set as dated history.
3. **"100% exit 0" is scoped, not absolute.** O11's green surface is 50 rows;
   13 historical controls deliberately replay to their expected filed-red
   codes. The claims contract and the receipt must be read together; a green
   stamp over the red controls would repeat the stale-verdict pattern D14
   documents.
4. **New frozen generation, old ones untouched.** `sweep/frozen/r31-post/`
   (pinned at `e8d2d0d`, freeze-receipt 23:12:31Z, replay 4/4 per O11) is a
   new baseline; no filed round-8..30 generation was edited (protected check).
   The supersession should be recorded in the round-31 admission — which is
   precisely the "freeze follows re-point" discipline D14 asks to codify.
5. **Two D drafts, one landing slot.** Whichever patch the orchestrator lands,
   the gate's deliverable is the LOG.md delta with its falsification condition;
   the un-landed draft remains filed evidence, and D14's §7 warning (the sweep
   cannot honestly stamp frozen replays green without the dispositioned-red
   distinction) is already reflected in O11's 13 kept-red controls.
6. **Draft anchors need re-verification at landing.** See the D row above:
   one off-by-one AGENTS.md anchor (D13) and one unmatched stale-sentence
   citation (D14). Cheap to fix at landing; expensive if landed as-is.
7. **Telemetry coexistence, not duplication.** X19's durable snapshot, X16's
   scope watch and this census are three instruments over different
   populations; none attests full-wave attendance, runtime concurrency or the
   served model. Counts here are read-time, not atomic.

## Census

Executed **2026-10-18T23:20:32Z**, exit **0**: **37 files**, **716,175 bytes**,
excluding this index and Python caches. Partitions: root 13, jinii 3, sweep 13,
telemetry 8. No failed read, no file changed inside its individual read, and no
strict-JSON error (duplicate-key-rejecting parser) was observed. Sequential
read-time census, **not an atomic snapshot**; the self row is excluded as
circular. C1 regenerates a live table without rewriting these dated rows.

<!-- X20:CENSUS:BEGIN -->
| artifact | bytes | sha8 | mtime UTC | inferred owner / evidence state |
|---|---:|---|---|---|
| `reports/round-31/claims.json` | 2837 | `23dfcaea` | 2026-10-18T22:34:08Z | parent declaration |
| `reports/round-31/closure-audit-C04.md` | 11811 | `04cc3e49` | 2026-10-18T22:48:02Z | C independent re-verification |
| `reports/round-31/closure-audit-C05.md` | 5289 | `176c8d27` | 2026-10-18T23:12:28Z | C independent re-verification |
| `reports/round-31/closure-ledger.json` | 31166 | `b9a66c2d` | 2026-10-18T22:41:28Z | C closure evidence |
| `reports/round-31/final-sweep.md` | 14646 | `05cd91ef` | 2026-10-18T23:19:16Z | O final sweep |
| `reports/round-31/jinii/analysis.md` | 10408 | `11f3c481` | 2026-10-18T22:41:49Z | D jin'i-ryu analysis/draft (orchestrator lands) |
| `reports/round-31/jinii/draft.md` | 10120 | `995d12ef` | 2026-10-18T22:42:33Z | D jin'i-ryu analysis/draft (orchestrator lands) |
| `reports/round-31/jinii/patch-draft.md` | 11832 | `ed74efb8` | 2026-10-18T22:49:00Z | D jin'i-ryu analysis/draft (orchestrator lands) |
| `reports/round-31/run-validation.py` | 54237 | `8694b9c0` | 2026-10-18T23:14:17Z | acceptance instrument, not verdict |
| `reports/round-31/scope.md` | 15768 | `c711dc31` | 2026-10-18T22:51:42Z | X16 scope watch |
| `reports/round-31/sweep/commands.txt` | 3543 | `43c875f4` | 2026-10-18T23:19:16Z | O sweep-build evidence (runner, r31-post freeze, receipt) |
| `reports/round-31/sweep/freeze-r31.py` | 8891 | `f035b530` | 2026-10-18T23:11:56Z | O sweep-build evidence (runner, r31-post freeze, receipt) |
| `reports/round-31/sweep/frozen/r31-post/MANIFEST.tsv` | 2087 | `617496ed` | 2026-10-18T23:12:30Z | O sweep-build evidence (runner, r31-post freeze, receipt) |
| `reports/round-31/sweep/frozen/r31-post/d4-assembly.out` | 73 | `c60820a5` | 2026-10-18T23:12:29Z | O sweep-build evidence (runner, r31-post freeze, receipt) |
| `reports/round-31/sweep/frozen/r31-post/d4-typed-labels.out` | 81 | `1c8add32` | 2026-10-18T23:12:29Z | O sweep-build evidence (runner, r31-post freeze, receipt) |
| `reports/round-31/sweep/frozen/r31-post/freeze-receipt.json` | 4523 | `f414c452` | 2026-10-18T23:12:31Z | O sweep-build evidence (runner, r31-post freeze, receipt) |
| `reports/round-31/sweep/frozen/r31-post/inputs/examples/culture-d4/packet.d4.typed.yml` | 108251 | `d581e0ad` | 2026-10-18T23:12:30Z | O sweep-build evidence (runner, r31-post freeze, receipt) |
| `reports/round-31/sweep/frozen/r31-post/inputs/examples/culture-d4/packet.d4.yml` | 101892 | `aac91246` | 2026-10-18T23:12:30Z | O sweep-build evidence (runner, r31-post freeze, receipt) |
| `reports/round-31/sweep/frozen/r31-post/inputs/examples/culture-d4/typed-labels.d4.yml` | 82161 | `c23b0ab5` | 2026-10-18T23:12:29Z | O sweep-build evidence (runner, r31-post freeze, receipt) |
| `reports/round-31/sweep/frozen/r31-post/typed-source.out` | 2213 | `865bb03e` | 2026-10-18T23:12:30Z | O sweep-build evidence (runner, r31-post freeze, receipt) |
| `reports/round-31/sweep/frozen/r31-post/typed-typed.out` | 2140 | `a1c055b6` | 2026-10-18T23:12:30Z | O sweep-build evidence (runner, r31-post freeze, receipt) |
| `reports/round-31/sweep/run-sweep.py` | 31099 | `005371c9` | 2026-10-18T23:17:59Z | O sweep-build evidence (runner, r31-post freeze, receipt) |
| `reports/round-31/sweep/sweep-receipt.json` | 49910 | `1d05f93d` | 2026-10-18T23:19:16Z | O sweep-build evidence (runner, r31-post freeze, receipt) |
| `reports/round-31/sweep-audit-O09.json` | 24871 | `1241ab16` | 2026-10-18T23:15:44Z | O sweep-audit evidence |
| `reports/round-31/sweep-audit-O09O10.json` | 55659 | `83ae08c9` | 2026-10-18T23:16:22Z | O sweep-audit evidence |
| `reports/round-31/sweep-audit-O09O10.md` | 10172 | `e6d8507a` | 2026-10-18T23:18:24Z | O sweep-audit evidence |
| `reports/round-31/sweep-audit-O10.json` | 24871 | `985373d6` | 2026-10-18T23:16:22Z | O sweep-audit evidence |
| `reports/round-31/sweep-audit.py` | 14281 | `c6d726b2` | 2026-10-18T23:15:03Z | O sweep-audit evidence |
| `reports/round-31/targets.json` | 182 | `f91e06c4` | 2026-10-18T22:34:08Z | parent declaration |
| `reports/round-31/telemetry/check.json` | 219 | `242ccad0` | 2026-10-18T22:45:02Z | X19 durable telemetry |
| `reports/round-31/telemetry/controls-vartmp.json` | 1886 | `b7264756` | 2026-10-18T22:45:19Z | X19 durable telemetry |
| `reports/round-31/telemetry/controls.json` | 1934 | `bb9e6477` | 2026-10-18T22:45:02Z | X19 durable telemetry |
| `reports/round-31/telemetry/dispatch-stats.json` | 2398 | `cb1f9dc2` | 2026-10-18T22:45:02Z | X19 durable telemetry |
| `reports/round-31/telemetry/dispatch-telemetry.py` | 10531 | `34f8c9f7` | 2026-10-18T22:44:53Z | X19 durable telemetry |
| `reports/round-31/telemetry/inputs/claims.json` | 2837 | `23dfcaea` | 2026-10-18T22:44:26Z | X19 durable telemetry |
| `reports/round-31/telemetry/inputs/targets.json` | 182 | `f91e06c4` | 2026-10-18T22:44:26Z | X19 durable telemetry |
| `reports/round-31/telemetry/worker-observation.json` | 1174 | `bc200b90` | 2026-10-18T22:44:53Z | X19 durable telemetry |
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
8–30 and the round-tagged frozen roots.

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1 GIT_OPTIONAL_LOCKS=0
python3 -B - <<'PY'
from collections import Counter
from datetime import datetime, timezone
import hashlib, json, re, subprocess
from pathlib import Path
BASE = Path('reports/round-31')
SELF = BASE / 'fragment-index-x20.md'
REV = '71cd9d376ebd144e94e4f12d997f73e5d2839aa9'
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
        return {'jinii': "D jin'i-ryu analysis/draft (orchestrator lands)",
                'telemetry': 'X19 durable telemetry',
                'sweep': 'O sweep-build evidence (runner, r31-post freeze, receipt)'}.get(parts[0], 'unassigned: ' + parts[0])
    if name in ('claims.json', 'targets.json'):
        return 'parent declaration'
    if name == 'closure-ledger.json':
        return 'C closure evidence'
    if name.startswith('closure-audit'):
        return 'C independent re-verification'
    if name.startswith('sweep-audit'):
        return 'O sweep-audit evidence'
    if name == 'scope.md':
        return 'X16 scope watch'
    if name == 'final-sweep.md':
        return 'O final sweep'
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
roots = [f'{root}/round-{number}' for root in ('reports', 'tools/gates/frozen') for number in range(8, 31)]
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

- **2026-10-18T22:45:31Z** and **22:46:48Z**, read-only `find`/`stat`
  inventories as described above: 14 files, then the first O receipts. No
  validator was invoked at any point by this seat.
- **2026-10-18T22:48:58Z**, read-only `python3 -B -` using `git ls-tree -r
  71cd9d376ebd144e94e4f12d997f73e5d2839aa9 -- reports/round-{8..30}
  tools/gates/frozen/round-{8..30}`, per-path Git blob SHA-1 of live bytes and
  `git status --porcelain=v1 -uall -- <same roots>`: **1,823 tracked paths**,
  **0 byte differences**, **0 protected status rows**. Lane HEAD
  `e8d2d0dadd3ccd1fbb7481793cfaf9bcd761826c` was not confused with the
  declared baseline.
- **2026-10-18T23:10:11Z**, X20 re-ran the exact one-line audit command quoted
  in `jinii/draft.md` §2.2: output was exactly
  `reports/round-19/availability.json` and
  `reports/round-{25,26,27,28}/availability.json` — the draft's five-record
  premise reproduced at this read.
- **2026-10-18T23:15Z**, read-only JSON reads of the two sweep-audit pass
  receipts: each reports **40 legs, 40 exit-0, no nonzero rows**; the combined
  receipt adds the cross-pass comparison and the source-snapshot statement.
  These are attributed readings of peer evidence, not X20 executions.
- **2026-10-18T23:19:38Z**, read-only extraction of
  `closure-ledger.json`: **24 rows** for rounds 8–31; verdicts
  `closed-admitted` 18, `closed-rejected` 3, `skipped-operator` 1,
  `closed-with-finding` 1, `in-flight` 1; `zero_missing_rows: true`; claim
  verdict `verify-with-named-finding` carrying its own falsification text.
  The same command batch confirmed the fleet
  `/home/vgpnk/Projects/shokunin/.ufo/reports/round-31/` directory is absent
  (kotodama fleet reports run through round-30), matching the ledger's
  in-flight row.
- **2026-10-18T23:20:32Z**, the census above: 37 files / 716,175 bytes /
  0 read errors / 0 unstable reads / 0 strict-JSON errors.
- The exact C1 block was then extracted from this filed index and executed via
  `bash`, twice: the first filed replay exited **0** with
  `INDEX_STRUCTURE_AND_NEGATIVES=PASS` but **`snapshot_current=false`** — the
  O builders rewrote exactly four census rows in the 23:20:44–23:23:28Z window
  while the replay ran: `final-sweep.md` (14,646 B, sha8 `e928a44b`,
  23:20:44Z), `sweep/sweep-receipt.json` (49,909 B, `c794d6a5`, 23:20:44Z),
  `sweep/run-sweep.py` (31,974 B, `c3326e6e`, 23:22:46Z) and
  `run-validation.py` (55,588 B, `4574b924`, 23:23:28Z); the second replay
  (observed **23:23:27.028Z**) reported the same state: **0 arrivals**,
  **4 digest/size drift rows**, no read/unstable/JSON errors, protected
  history again **1,823 / 0 / 0**, runner present, **receipt still absent**.
  The census table keeps its dated pre-rewrite rows; C1 prints the current
  live table for any new dated census. A later reader re-runs C1 and treats
  its drift output as staleness, not a defect in this index — but the parent
  must confirm the wave has stopped changing before running acceptance, and
  the rewritten `final-sweep.md` verdict (re-checked by X20 at 23:24Z: still
  "50 green-surface rows, all exit 0" + 13 expected-red controls) should be
  re-read from its final bytes.
- **Scope limits:** X20 did not depth-read `closure-audit-C05.md` or
  `final-sweep.md` beyond head/verdict sections, did not execute
  `run-validation.py`, `sweep/run-sweep.py`, `sweep-audit.py` or any gate, did
  not assess fleet-root cleanliness, canon, rights or peer semantics, and does
  not attribute worker attendance. All counts above carry their commands and
  the date 2026-10-18.

### Parent integration still required at handoff

1. Run `reports/round-31/run-validation.py` on the final stable read set —
   after this index and all peer fragments stop changing — and bind the
   receipt to the live runner and read-set digests; then reconcile claim O's
   "100% exit 0" phrasing against O11's 50-green + 13-expected-red scoping in
   the admission text.
2. Select and land **one** jin'i-ryu patch (D13 or D14), re-anchoring exact
   bytes (D13's AGENTS.md anchor is :31, not :30; D14's SKILL.md:294 citation
   does not currently match the text), and record the delta + falsification
   condition in LOG.md per the gate. Execute the chosen patch's retroactive
   act if it has one (D13: the five closing snapshots).
3. Write the round-31 fleet report and the MANIFEST closure entry (per-axis
   verdicts), closing the ledger's `in-flight` row; round 32 stays
   pending-by-construction.
4. Record the `r31-post` frozen-generation supersession in the admission;
   integrate LOG/SCORECARD append-only; if a later fragment census is needed,
   rerun C1 for a new dated reading. No round admission, claim verdict, or
   promotion decision is issued by X20.

FILES: reports/round-31/fragment-index-x20.md | SUMMARY: X20 filed the 37-artifact dated census, C/O/D conformance map (ledger verdicts cross-checked, sweep scoping vs contract, two competing D drafts with anchor defects) and a passing drift-aware C1 replay; the acceptance receipt, one-of-two D landings and the round-31 fleet report remain parent-owned.
