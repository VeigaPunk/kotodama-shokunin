- Seat: K04 | scout | claim A | date 2026-10-19 | baseline 139e3b6

# K04 — adjacency method scout (round 33)

Scope: extract the check set, scope-watch method and counting commands from the two
prior consolidated adjacency audits (`reports/round-21/adjacency/`,
`reports/round-29/adjacency/`), then record the round-33 HEAD quick-reads named in this
seat's mission. Read-only: this seat wrote only this fragment; no validator was run, no
filed round byte was touched, no Git mutation.

Limits (carried from both prior audits, still binding): an adjacency verdict is a
source-boundary review, **not** canon adjudication, real-world legal/rights review,
community consultation, source-truth certification, round acceptance, or fleet-root
cleanliness. `reports/round-21/adjacency/entries.md:3` states the same; r29 restated it at
`reports/round-29/adjacency/A09-A12-handoff.md:5,11`.

## 1. Check set extracted from r21 (12-seat audit)

r21 ran a full consolidated boundary audit; its check set is the closest precedent to
round 33's A01–A16.

| # | check | what it measures | evidence |
|---|---|---|---|
| A01 | inventory and per-entry coverage | dated `pathlib.Path.is_file()` census of every named path group; counts printed as `found/total` | `reports/round-21/adjacency/entries.md:7-9`; command verbatim in `reports/round-21/adjacency/ledger.json:19` |
| A02 | canon boundary | no canon bleed; entries label themselves NON-CANON; candidate world-facts stay typed + routed to lore | `entries.md:17` |
| A03 | real-world rights/attribution | no lane ruling made; screening stays an open question | `entries.md:18` |
| A04 | game-mechanics bleed | no gameplay/mechanics content; lexical hits read in context | `entries.md:19` |
| A05–A10 | per-entry verdicts | one verdict + boundary evidence + sha256 prefix per audited content path | `entries.md:25-56` |
| A11–A12 | consolidated ledger + handoff verdict | province accuracy, `unfiled_bleed` count, transfer decision, dated command list | `A11-A12-handoff.md:6-10,41-50` |

The r21 ledger's `checks[]` block is the reusable command inventory
(`ledger.json:80-91`): handoff v3 end-to-end envelope; handoff v3 positive+control
selftest; standalone packet shape; claim uncertainty census; claim links; D4 typed
pipeline; D4 projection reproducibility; D4 projection source/count comparison;
PROVINCE + filed-round preservation; ledger path/bleed census. The bleed census is a
join of bleed rows to filed finding ids — r21's own note is explicit that
`unfiled_bleed=0` does **not** mean no bleed was found (`A11-A12-handoff.md:54`).

Language/boundary-verdict legs are validated textually in the r21 validator
(`reports/round-21/run-validation.py:886-926`: required-path citation, `R19 author
fragments: 10 10` / `R20 author fragments: 4 4` inventory regexes, full-tree lexical-scan
documentation, `**A0n … **PASS` verdict regexes, `no bleed found` presence). Round 33's
A08 language grep is the successor of that textual leg.

## 2. Check set extracted from r29 (scoped audit)

r29 audited six surfaces (2 entries, 0 rows, 4 audits) and is the better template for a
**scoped** round-33 audit because it keeps the finding/verdict split explicit:

- **Ledger shape:** `entries` + `rows` + `audits`, each row carrying
  `path/status/scope/out_of_province/bleed/evidence` (`reports/round-29/adjacency/ledger.json:22-74`).
- **Exact-anchor ID extraction:** the law's `RGL-01..RGL-05` IDs were extracted from
  *both* the component and the assembled packet, and compared as sets — a substring count
  was explicitly rejected as an instrument error
  (`ledger.json:76-82`; command `A09-A12-handoff.md:26-48`).
- **Index-row check:** one README filename row per entry, matched by exact line prefix
  (`A09-A12-handoff.md:37-40`).
- **Boundary sentinels:** `NON-CANON` and `Canon boundary and handoff` markers present in
  each audited entry; explicit no-real-world-rights disclaimer in the law component
  (`A09-A12-handoff.md:41-46`).
- **Province integrity:** `git diff --quiet -- PROVINCE.md` + `sha256sum PROVINCE.md`
  (`A09-A12-handoff.md:52-57`).
- **Baseline reconstruction:** quoted absence sweeps re-run against the *declared*
  baseline commit and the live corpus, then classified (baseline-false authoring defect
  vs baseline-clean sibling landing) — a false-at-authoring evidence claim was filed as
  `A29-ADJ-EVID-01` with `bleed=false` (`A09-A12-handoff.md:59-108`; `ledger.json:98-144`).
- **Final ledger census:** JSON assertions over counts, boundary booleans, finding
  filing, and sweep dispositions (`A09-A12-handoff.md:112-142`).
- **Method-notes discipline:** discarded preliminary probes are disclosed as instrument
  history, never as evidence, and the superseded earlier census is named
  (`ledger.json:146-148`).
- **Non-scope observation:** the previously filed `A21-D4-XF-01` is explicitly *not*
  re-evaluated or closed by the later audit (`ledger.json:149-154`; `A09-A12-handoff.md:11`).

**Round-33 carry-over rules for A10/A15:** (1) a scoped pass is not a general
fixture-isolation claim; (2) prior filed findings stay open unless a round-33 seat
re-measures them; (3) findings split into `bleed` vs non-bleed evidence defects, and only
the former feed `unfiled_bleed`.

## 3. Scope-watch method

Two precedents, in increasing strength:

- **r21 (`reports/round-21/scope.md:10-22`)** — tracked-surface only: baseline→HEAD diff
  on the protected surface, worktree diff vs baseline, `git status --porcelain=v1 -uall`
  on protected paths, `git ls-files <protected> | wc -l`, plus an explicit verification
  boundary that ignored paths have no Git baseline and are **not** claimed byte-identical
  (`scope.md:22`). r21 also read the fleet root (`git -C /home/vgpnk/Projects/shokunin
  status --short --branch -uall`, `scope.md:37`).
- **r29 (`reports/round-29/scope.md:8-51`)** — byte+mode comparison of every tracked path
  against `git ls-tree -r -z <baseline>`, repeated at six samples ~60 s apart with a
  sorted-path/sha256 manifest digest, a mtime-vs-declaration-cutoff check, an in-memory
  detector control, and a copy-pasteable replay script (`scope.md:53-91`). r29
  deliberately does **not** assert fleet-root cleanliness (`scope.md:14,97`) — round 33's
  A03 mission does require an out-of-lane write scan, so A03 must state its own boundary
  (reads allowed; writes only in-repo per `shared_rules`).

**Replay template for round 33** (r29's script with the baseline and surface extended;
the round-33 baseline is `139e3b662900557afe54f632b468619593dc9fcb`,
`reports/round-33/claims.json:8`):

```bash
export TMPDIR="$PWD/.scratch"
python3 -B - <<'PY'
import datetime, hashlib, os, stat, subprocess
base = '139e3b662900557afe54f632b468619593dc9fcb'
paths = [f'reports/round-{n}' for n in range(8, 33)] + [f'tools/gates/frozen/round-{n}' for n in range(8, 33)]
def git(*args): return subprocess.check_output(['git', *args])
def blob(data): return hashlib.sha1(b'blob ' + str(len(data)).encode() + b'\0' + data).hexdigest()
entries = []
for row in git('ls-tree', '-r', '-z', base, '--', *paths).split(b'\0'):
    if row:
        meta, rawpath = row.split(b'\t', 1)
        mode, _, oid = meta.decode().split()
        entries.append((os.fsdecode(rawpath), mode, oid))
cutoff = datetime.datetime.fromisoformat(git('show', '-s', '--format=%cI', 'HEAD').decode().strip()).astimezone(datetime.timezone.utc)
mismatches, missing, newer, manifest = [], [], [], []
for path, mode, oid in entries:
    try:
        st = os.lstat(path)
        data = os.readlink(path).encode() if stat.S_ISLNK(st.st_mode) else open(path, 'rb').read()
    except FileNotFoundError:
        missing.append(path); continue
    live_mode = '120000' if stat.S_ISLNK(st.st_mode) else ('100755' if st.st_mode & 0o111 else '100644')
    if (blob(data), live_mode) != (oid, mode): mismatches.append(path)
    manifest.append(path.encode() + b'\0' + hashlib.sha256(data).hexdigest().encode() + b'\n')
    if datetime.datetime.fromtimestamp(st.st_mtime, datetime.timezone.utc) > cutoff: newer.append(path)
print('tracked', len(entries), 'mismatches', mismatches, 'missing', missing)
print('manifest_sha256', hashlib.sha256(b''.join(sorted(manifest))).hexdigest())
print('protected_status', git('status', '--porcelain=v1', '-uall', '--', *paths).decode().splitlines())
print('baseline_head_diff', git('diff', '--name-status', base, 'HEAD', '--', *paths).decode().splitlines())
print('tracked_newer_than_declaration', newer)
print('protected_ignored_count', len(git('ls-files', '--others', '--ignored', '--exclude-standard', '-z', '--', *paths).split(b'\0')) - 1)
PY
```

Caveat that must be carried into A03's wording: the protected-surface pass is byte/mode
cleanliness at the sampled instants, not proof that no transient rewrite occurred between
samples (`reports/round-29/scope.md:35,95`).

## 4. Counting commands (adjacency claim)

Commands and their round-33 expected green, all re-measured by this seat on 2026-10-19:

| purpose | command | expected green |
|---|---|---|
| handoff gate | `python3 tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md` | exit 0; `fields=16/16 glossary-entries=20 findings=0` |
| handoff e2e | `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` | exit 0; `fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed` |
| handoff e2e controls | `python3 tools/exercise-handoff-e2e.py --profile v3 --selftest` | exit 0 (positive run + control matrix; r21 recorded 28 controls, `A11-A12-handoff.md:42`) |
| uncertainty census | `python3 tools/harness/packet_uncertainty.py --packet reports/round-30/handoff/declared-in-r6/twin.json --require-oq --json` | exit 0; `claims: 27`, `findings: []` |
| claim links | `python3 tools/harness/packet_links.py --packet reports/round-30/handoff/declared-in-r6/twin.json --json` | exit 0; `links_checked: 105`, `resolved: 105`, `findings: []` |
| province integrity | `git diff --quiet -- PROVINCE.md && sha256sum PROVINCE.md` | diff exit 0; digest `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` |
| scope count | `git ls-files \| wc -l` | 2655 (declared regimen-2 baseline) |
| protected surface | `git status --porcelain=v1 -uall -- reports/round-{8..32} tools/gates/frozen` | zero rows |
| language grep (A08) | `grep -rn -iE 'promot(e\|ion)\|canoniz\|clearance\|closure\|verified-without' reports/round-33/` | every hit a negation or routed-reference |
| regression battery (r21 pattern) | the 20-command `REGRESSIONS` list at `reports/round-21/run-validation.py:603-623` (gate battery, craft exercise, assemble-d2/d3/d4 ±typed, d2-typed-labels, typed-pipeline-gate, evidence-coupling, handoff e2e selftest+quiet) | all exit 0 |

The r29 validator's adjacency leg (`reports/round-29/run-validation.py:678-764`) is the
model for a machine-checkable round-33 A-leg: it hard-pins the PROVINCE digest
(`:734,759`), requires `unfiled_bleed == 0` and all-false boundary flags (`:715-724`),
and asserts the ledger row counts (`:736`). **That pin still holds at round-33 HEAD** (see
§5), so the round-33 validator can reuse the same digest constant.

## 5. HEAD quick-reads at round 33 (measured 2026-10-19)

All commands run from the lane root with `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`; `date -u` stamps: `2026-10-19T03:52:25Z`–`03:53:12Z`.

1. **`git log -- PROVINCE.md`** → last commit `c53782ab875e88d7311c8b9b1db310357b944685`
   (`2026-10-17T13:09:14-03:00`, `supplement-opencode-1: recheck sources and harden
   reproducible evidence`); only two commits ever touch the file (`a527120` mint,
   `c53782a`). `git rev-parse HEAD:PROVINCE.md` → `313b182f251564b7997b06996b4f063370778f11`
   — **identical to the blob r21 recorded** (`reports/round-21/adjacency/province.md:17`),
   so PROVINCE is byte-stable across rounds 21→33. This confirms the claims.json before-state
   (`reports/round-33/claims.json:57`) and r32 dossier D11's `c53782a` claim
   (`reports/round-32/dossier-d11-shonen-boxes.md:192-194`).
   `sha256sum PROVINCE.md` → `05b34a579c5d…b942d6` (unchanged since r20/r21/r29 records);
   `git diff --quiet -- PROVINCE.md` → exit 0.
   Adjacent digests at the same stamp: `corpus/knowledge/synthesis/worldbible-integration-contract.md`
   → `5f4c02bfc4e6e4e943c2dd6983750ba34538219a6e239e451c81dc3fd4f79069` (unchanged, matches
   `reports/round-29/adjacency/province-entries.md:15`); `AGENTS.md` → `1afaf106f20b440ad263ab231c215773436c7f42ab106848f5550b87ecf41035`
   (**drifted** from r29's `be3a9477ed28ba401352ebce7c182d529223e552d0dba0d75f3b97b956be2c8b`,
   `province-entries.md:15`). The drift is fully explained by committed rounds: `git log --
   AGENTS.md` shows `11df1fd5` (round-30 wave integration, `2026-10-18T19:22:35-03:00`) and
   `17e90b90` (round-31 admission, `2026-10-18T21:28:45-03:00`) after r29's measurement
   stamp; the working file is clean vs HEAD. **Not an unexplained drift — do not file it as
   one.**

2. **Handoff gate command + expected green.** The current packet pair is
   `reports/round-30/handoff/declared-in-r6/{packet.md,twin.json,expected.json}` — the
   latest of four filed pairs (`reports/round-22/handoff/declared-in/`,
   `reports/round-22/handoff/declared-in-r2/`, `reports/round-26/handoff/declared-in-r5/`,
   `reports/round-30/handoff/declared-in-r6/`); there is **no** `reports/round-3{1,2}/handoff/`
   directory. Re-run today, all green:
   - `python3 tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md`
     → `INFO scan: fields=16/16 glossary-entries=20 findings=0`, exit 0.
   - `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` → exit 0,
     `handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27
     statuses=16/7/4 v2_subset=equal alias_leg=landed
     packet_sha256=6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb`.
     That digest equals the filed `packet_sha256` in
     `reports/round-30/handoff/declared-in-r6/freeze.txt:2` → the packet is byte-identical
     to its freeze.
   - `python3 tools/exercise-handoff-e2e.py --profile v3 --selftest` → exit 0 (control
     matrix; tail shows the tamper/negative controls, e.g. `m12a tamper baseline: exit 2
     E2E-BASELINE`).
   - `python3 tools/harness/packet_uncertainty.py --packet …/twin.json --require-oq --json`
     → exit 0, `claims: 27`, `findings: []`.
   - `python3 tools/harness/packet_links.py --packet …/twin.json --json` → exit 0,
     `links_checked: 105`, `resolved: 105`, `findings: []`.
   - `python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md` (the
     SCORECARD sample command, `SCORECARD.md:35`) → exit 0, `fields=16/16
     glossary-entries=20 findings=0`.

3. **`git ls-files | wc -l` → 2655**, equal to the regimen-2 opening baseline declared in
   `reports/round-33/claims.json:57`. Frozen-generation surface for A09's pin work:
   `git ls-files tools/gates/frozen | wc -l` → 237; frozen dirs present: `round-3, round-4,
   round-11, round-18, round-20, round-22, round-23, round-25, round-26` plus seven named
   gate dirs (`costume-era-consistency-gate, handoff-packet-check, lexicon-coverage-audit,
   myth-consistency-gate, naming-collision-gate, phonology-sanity-gate, provenance-audit`).
   Preliminary lead only (A09 owns the verdict): `grep -rl 'SKILL.md\|corpus/lessons'
   tools/gates/frozen/` hits frozen *snapshots* that carry their own copies
   (`handoff-packet-check/r9-pre/freeze.txt`, `provenance-audit/*/inputs/...`), i.e. they
   pin by digest rather than re-reading live files — A09 must confirm whether any *live*
   gate re-reads SKILL.md or the lessons README before claiming cascade risk.

4. **Write-scope snapshot** (`git status --porcelain=v1 -uall`): 5 rows —
   ` M LOG.md`, `?? REGIMEN.md`, `?? reports/round-33/claims.json`,
   `?? reports/round-33/targets.json`, `?? reports/round-33/telemetry/dispatch-declared.json`.
   `LOG.md` diff is `18 insertions(+)`, and its tail is the regimen-2 declaration entry
   (`3 loops × 14 rounds … freshness pause remains`, `LOG.md` tail) — the integrator's
   append, not a seat write. `git status --porcelain=v1 -uall -- reports/round-{8..32}
   tools/gates/frozen` → **0 rows**: the filed surface is clean. All round-33 deltas are
   inside `reports/round-33/` plus `REGIMEN.md`/`LOG.md`, which is exactly the scope-delta
   explanation claim A's threshold requires (`reports/round-33/claims.json:63`).

5. **A08 language-grep rehearsal** (baseline for the A08 seat, which must re-run it over
   the *then-current* fragment set): `grep -rn -iE 'promot(e|ion)|canoniz|clearance|closure'
   reports/round-33/` at scout time → **4 hits, all in the declaration files**, all
   negations or requirements: `claims.json:59` (the after-required clause requiring no such
   language), `claims.json:68` (non-goal `no promotion, canon, clearance, or closure
   verdicts`), `targets.json:51` and `targets.json:55` (A04/A08 mission text). Zero
   affirmative promotion/canon/closure claims at this stamp.

## 6. Round-33 check-set mapping (for A10/A15)

Historical r21 check → round-33 seat: inventory/coverage → A03 (scope counts) + A05
(corpus partitions); canon/rights/mechanics boundary → A04 (bleed) + A06 (contested);
province accuracy → A01; handoff envelope/uncertainty/links/gate → A02; filed-command
replay → A07; language leg → A08; **new at round 33**: A09 pin-cascade exposure (no r21/r29
precedent — r21 checked "PROVINCE and filed-round preservation" only, `ledger.json:89`) and
A16 SHONEN material (r32 D11 box 4 is its source, `dossier-d11-shonen-boxes.md:169-208`).
Contested-scope items to restate in A06 with current pointers: the §1 bilateral same-revision
read record (still pending) and the L0 contract-digest question (`fleet .ufo/l0-questions.md:44`
round-2 handoff-format question; `:45` round-8 contract-digest drift vs lore's r93
ratification; `:47` round-11 freshness-threshold question) — all routed-not-absorbed.

## Owed: none

No dependency fragment was needed for this mission. Two items are *by design* left to their
owner seats and are not owed by K04: A09's live-gate pin verdict (lead recorded in §5.3) and
A08's post-fragment language re-grep (§5.5 is a scout-stamp baseline only).

## Citations

- `reports/round-33/claims.json:5-8,19-71` — round/regimen/baseline, claims O/C/A, non-goals
- `reports/round-33/targets.json:5-16,48-63` — shared_rules, A01–A16 missions/out paths
- `REGIMEN.md:25-50,60-69` — per-round contract, scope, stop-and-report
- `reports/round-21/adjacency/entries.md:3-19,25-56` — r21 check set and verdicts
- `reports/round-21/adjacency/ledger.json:19,80-91,92-112,113-123` — inventory command, checks, finding, transfer decision
- `reports/round-21/adjacency/A11-A12-handoff.md:6-10,14-21,41-50,54` — r21 consolidated verdict, dated commands, bleed-census caveat
- `reports/round-21/adjacency/province.md:7-17,25` — PROVINCE blob/digest record
- `reports/round-21/scope.md:8-30,36-43` — r21 scope-watch method and command list
- `reports/round-21/run-validation.py:603-623,886-926,929-984` — regression battery, adjacency text legs, handoff gate/links legs
- `reports/round-29/adjacency/ledger.json:22-74,76-82,98-154` — ledger shape, RGL extraction, finding, method notes, non-scope observation
- `reports/round-29/adjacency/A09-A12-handoff.md:5-20,26-48,52-57,59-108,112-146` — r29 method, commands, sweeps, census, limits
- `reports/round-29/adjacency/province-entries.md:15-17` — PROVINCE/AGENTS/contract digests at r29
- `reports/round-29/scope.md:8-51,53-91,95-98` — r29 byte+mode scope watch, replay script, limits
- `reports/round-29/run-validation.py:72,678-764` — handoff e2e leg, adjacency measure with PROVINCE digest pin
- `reports/round-30/handoff/declared-in-r6/{freeze.txt,run.log,packet.md,twin.json}` — current handoff pair, freeze digests
- `reports/round-32/dossier-d11-shonen-boxes.md:169-208` — box 4 (no bleed / PROVINCE accurate), standing readings, summary table
- `SCORECARD.md:3,35,239,384,439` — axis list, handoff gate sample command, r21/r29 adjacency rows
- `LOG.md` (working-tree tail, `18 insertions(+)`) — regimen-2 declaration append
- `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md:44,45,46,47` — kotodama L0 open questions (read-only, external to this repo)
- Command outputs (2026-10-19T03:52:25Z–03:53:12Z, lane root, `TMPDIR=$PWD/.scratch`): `git log --format='%H %cI %s' -- PROVINCE.md`; `git rev-parse HEAD`/`HEAD:PROVINCE.md`; `sha256sum PROVINCE.md AGENTS.md corpus/knowledge/synthesis/worldbible-integration-contract.md SKILL.md`; `git diff --quiet -- PROVINCE.md`; `git ls-files | wc -l`; `git ls-files tools/gates/frozen | wc -l`; `git status --porcelain=v1 -uall` (lane and protected surface); `python3 tools/gates/handoff-packet-check.py` (r30 pair, sample); `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet|--selftest`; `python3 tools/harness/packet_uncertainty.py`/`packet_links.py` (r30 twin); `grep -rn -iE 'promot(e|ion)|canoniz|clearance|closure' reports/round-33/`; `grep -rl 'SKILL.md\|corpus/lessons' tools/gates/frozen/`

FILES: reports/round-33/adj/K04-method-scout.md | SUMMARY: r21/r29 adjacency check sets, scope-watch method and counting commands extracted; round-33 HEAD quick-reads measured green (PROVINCE last commit c53782a / blob 313b182f unchanged, handoff gate exit 0 on the r30 `declared-in-r6` pair with packet_sha256 6ced88ad matching its freeze, ls-files 2655); AGENTS.md digest drift explained by rounds 30/31 commits; zero out-of-lane writes.
