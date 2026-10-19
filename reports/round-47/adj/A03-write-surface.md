# A03 — write-surface census (round 47, claim cross)

- Seat: `A03` | role: verifier | claim: **cross** | round 47, loop 2, position 1 (refire wave, key 6)
- Out path: `reports/round-47/adj/A03-write-surface.md` (this file; the only path this seat wrote)
- Baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` — equals `reports/round-47/claims.json:7` (`6e9a30d`) and `git rev-parse HEAD`
- Census cut: **2026-10-19T19:08:57Z** (16:08:57 local, UTC-03:00). File mtimes below are local; add 3 h for UTC.
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root
- Mission (`reports/round-47/targets.json` seat A03): *"Write-surface census: enumerate every reports/round-47/ file at close; confirm each maps to a declared out path + telemetry/validation; flag any undeclared or corpus write."*

## 0. Verdict at this cut

| census object | verdict | basis |
|---|---|---|
| Files under `reports/round-47/` | **54 at cut** (55 after this file) | `find reports/round-47 -type f \| wc -l` → 54 before this write; full manifest §3 |
| Declared seat outs present | **50 / 64**, exact 1:1, no stray seat path | `targets.json` has 64 unique `out` values; 50 exist as files, 14 do not (§2) |
| Seat files mapping to an undeclared path | **0** | every seat file's path is byte-equal to its declared `out`; 0 duplicate-content groups (§6) |
| Non-seat files | **4**, all classifiable (contract or telemetry) | `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`, `telemetry/refire-key6.json` (§4) |
| Corpus write | **NONE** | `git status --porcelain -uall -- corpus/ tools/ examples/ .ufo/ PROVINCE.md LOG.md` empty; corpus still 223, culture-material still 25, cartography path absent (§5) |
| Tracked / staged modifications | **NONE** | `git diff --name-only` → 0; `git diff --cached --name-only` → 0; `git rev-list --count 6e9a30d..HEAD` → 0 (§5) |
| Writes outside `reports/round-47/` | **1 file, not an r47 seat path** | `reports/round-46/review/R01-review.md`, untracked, mtime 17:48:54Z — an r46-declared artifact (§5.1) |
| Bytecode side-effect under `tools/` | **1 gitignored `.pyc`** | `tools/harness/__pycache__/basename-couples-resolver.cpython-314.pyc`, mtime 17:58:36Z (§5.2) |
| Close artifacts (`validation.json`, `run-validation.py`, observed dispatch, availability close) | **ABSENT — `could-not-evaluate`** | measured absent at cut; `claims.json` cites `reports/round-47/run-validation.py`, which does not exist (§7) |
| **Overall** | **PASS for the seat artifacts present at the snapshot (50) and this one (51); CLOSE NOT CERTIFIABLE from this cut** | the round is still in flight (13 declared outs absent after this write); §8 is the re-runnable close gate |

This is a mid-wave cut, not a close census. `telemetry/refire-key6.json` (mtime 16:07:19 local) records a 14-seat refire still being dispatched when this seat started; other refire seats may add files after 19:08:57Z. The 50 seat files present at the snapshot, plus this artifact, are clean; the close-state half — all 64 outs plus the receipt — is owed and specified as a re-run in §8. Do not read §0 as a close clearance.

## 1. Method

Read-only. No corpus, tool, README, LOG, or filed-round byte was written or staged. The only write is this artifact.

The registry is derived mechanically from `targets.json`, never from prose:

```console
$ python3 -B -c 'import json;t=json.load(open("reports/round-47/targets.json"));o=[s["out"] for s in t["seats"]];print(len(o),len(set(o)))'
64 64
$ find reports/round-47 -type f | wc -l
54
$ git status --porcelain=v1 -uall | wc -l
55          # 54 round-47 entries + the r46 review file in §5.1
$ git status --porcelain=v1 -uall | grep -v '^?? reports/round-47/'
?? reports/round-46/review/R01-review.md
```

A prior A03 pass left scratch-only evidence (`.scratch/a03-snapshot.json`, mtime 15:09 local; `.scratch/a03-write-surface-census.py`, 15:10) reporting 47 files on disk and 44 seat fragments. That pass never filed its out path — which is why A03 appears in `telemetry/refire-key6.json:5`. Its numbers are consistent with my pre-cut measurement (50 seats + 4 non-seat files), but I re-derived everything below from the live tree and cite only my own commands; scratch is volatile and is not treated as durable evidence.

## 2. Registry reconciliation

64 declared out paths, 64 unique. Present at cut: 50. Absent: 14 (13 after this artifact lands).

| subdir | present | absent | absent seats |
|---|---:|---:|---|
| `adj/` | 2 | 1 | A03 (this file) |
| `calib/` | 7 | 0 | — |
| `cov/` | 15 | 1 | W02 |
| `cross/` | 5 | 2 | X03, Q01 |
| `op/` | 10 | 7 | O07, O08, O11, O14, O15, V02, W01 |
| `plan/` | 3 | 0 | — |
| `review/` | 2 | 3 | R01, R03, R04 |
| `scout/` | 3 | 0 | — |
| `scribe/` | 3 | 0 | — |
| **total** | **50** | **14** | |

The absent set is exactly `telemetry/refire-key6.json`'s `missing_seats` list (`O07 O08 O11 R01 R03 X03 V02 W01 W02 Q01 O14 O15 R04 A03`), re-measured rather than trusted:

```console
$ for o in op/O07-anti-theater.md op/O08-verify.md op/O11-baseline-eval.md \
           review/R01-review.md review/R03-c-content.md cross/X03-gate-theater.md \
           op/V02-gate-verify.md op/W01-landing-spec.md cov/W02-landing-spec.md \
           cross/Q01-final-gate.md op/O14-determinism.md op/O15-malformed.md \
           review/R04-gate.md adj/A03-write-surface.md; do
    [ -e "reports/round-47/$o" ] && echo "PRESENT $o" || echo "absent  $o"; done
absent  op/O07-anti-theater.md
absent  op/O08-verify.md
absent  op/O11-baseline-eval.md
absent  review/R01-review.md
absent  review/R03-c-content.md
absent  cross/X03-gate-theater.md
absent  op/V02-gate-verify.md
absent  op/W01-landing-spec.md
absent  cov/W02-landing-spec.md
absent  cross/Q01-final-gate.md
absent  op/O14-determinism.md
absent  op/O15-malformed.md
absent  review/R04-gate.md
absent  adj/A03-write-surface.md      # created by this write
```

No filed r47 artifact cites any of the still-absent outs as present evidence; a grep for `reports/round-47/<dir>/<seat>-` across all r47 `.md` files returns 0 hits for all 13 other absent seats. The many `review/R01-review.md` mentions in the round are to `reports/round-44/review/R01-review.md`, which exists at HEAD (`git cat-file -e HEAD:reports/round-44/review/R01-review.md` → present). So the missing seats are a completeness gap, not a citation-integrity gap.

## 3. Full seat manifest (50 declared files, sorted by path)

| # | path under `reports/round-47/` | seat | claim | bytes | sha256[:12] | mtime |
|---|---|---|---|---:|---|---|
| 1 | `adj/A01-scope.md` | A01 | cross | 28607 | `abfc39a924cd` | 15:10:16 |
| 2 | `adj/A02-ownership.md` | A02 | C | 38024 | `7d9a42e3d367` | 15:09:37 |
| 3 | `calib/Ca01-stale-premises.md` | Ca01 | Ca | 21761 | `e0e51e5600a1` | 15:01:58 |
| 4 | `calib/Ca02-resolver-edge.md` | Ca02 | Ca | 11885 | `91cd4484b780` | 14:56:50 |
| 5 | `calib/Ca03-manifest-schemas.md` | Ca03 | Ca | 18666 | `a2e61cdba818` | 15:00:17 |
| 6 | `calib/Ca04-provider-amendments.md` | Ca04 | Ca | 22167 | `94b99878a31a` | 15:04:22 |
| 7 | `calib/Ca05-verify.md` | Ca05 | Ca | 23924 | `5dfe7b12c0f4` | 15:09:54 |
| 8 | `calib/Ca06-queue-successor.md` | Ca06 | Ca | 46854 | `15bb86dfff09` | 15:05:01 |
| 9 | `calib/Ca07-integrity.md` | Ca07 | Ca | 21264 | `895d76f7cc2c` | 15:10:45 |
| 10 | `cov/C01-entry-a.md` | C01 | C | 47829 | `cfb429556173` | 15:06:15 |
| 11 | `cov/C02-entry-b.md` | C02 | C | 60985 | `5f5683a72ea0` | 15:10:09 |
| 12 | `cov/C03-entry-c.md` | C03 | C | 41114 | `4b699e065371` | 15:02:59 |
| 13 | `cov/C04-entry-header.md` | C04 | C | 36044 | `cb5a7489676d` | 15:04:56 |
| 14 | `cov/C05-freshness.md` | C05 | C | 17554 | `62f9f702540f` | 14:55:44 |
| 15 | `cov/C06-source-audit.md` | C06 | C | 46231 | `f28e19dd4477` | 15:09:41 |
| 16 | `cov/C07-contract-audit.md` | C07 | C | 32056 | `89d0003c934a` | 15:08:54 |
| 17 | `cov/C08-boundary.md` | C08 | C | 35618 | `94e35a44ec36` | 15:09:37 |
| 18 | `cov/C09-readme.md` | C09 | C | 28281 | `b63df4134101` | 15:05:35 |
| 19 | `cov/C10-sweep.md` | C10 | C | 14831 | `916e8c6b186d` | 15:01:15 |
| 20 | `cov/C11-scribe.md` | C11 | C | 20304 | `4637ab101832` | 15:09:58 |
| 21 | `cov/C12-shelf.md` | C12 | C | 21238 | `7bba92cdfd01` | 15:10:02 |
| 22 | `cov/C13-couples.md` | C13 | C | 15728 | `bf57bdc7fbad` | 15:05:52 |
| 23 | `cov/C14-example.md` | C14 | C | 21031 | `8621d68fd2db` | 15:09:53 |
| 24 | `cov/V01-post-landing.md` | V01 | C | 23663 | `5c09f3ba3cd6` | 15:09:33 |
| 25 | `cross/X00-connector.md` | X00 | cross | 29655 | `d1ba81ee52b9` | 14:58:37 |
| 26 | `cross/X01-trades.md` | X01 | cross | 35170 | `4c359080a868` | 15:10:09 |
| 27 | `cross/X02-honesty.md` | X02 | cross | 32156 | `c8add64a9be7` | 15:09:22 |
| 28 | `cross/X04-coverage-critic.md` | X04 | C | 26620 | `651b741667ba` | 15:04:45 |
| 29 | `cross/X05-baseline-drift.md` | X05 | cross | 23281 | `e7ec7c92f34a` | 15:00:27 |
| 30 | `op/O01-tool-core.md` | O01 | O | 37601 | `d5b13986c115` | 15:09:37 |
| 31 | `op/O02-probe-registry.md` | O02 | O | 62722 | `67fdf9c26ec4` | 15:08:26 |
| 32 | `op/O03-verdict-contract.md` | O03 | O | 36200 | `01efab175ee2` | 15:09:26 |
| 33 | `op/O04-selftest.md` | O04 | O | 31266 | `b4ba0b77a6ca` | 15:10:10 |
| 34 | `op/O05-r43-demo.md` | O05 | O | 17698 | `04ca9ce60cc9` | 15:10:06 |
| 35 | `op/O06-negative-control.md` | O06 | O | 44006 | `99b702c2cd5a` | 15:09:55 |
| 36 | `op/O09-traps.md` | O09 | O | 35965 | `90409c408f37` | 15:06:59 |
| 37 | `op/O10-exit-codes.md` | O10 | O | 31858 | `31f954fde809` | 14:59:13 |
| 38 | `op/O12-scribe.md` | O12 | O | 35604 | `2df14ad43fd7` | 15:10:15 |
| 39 | `op/O13-probe-coverage.md` | O13 | O | 20462 | `4ad5a727af65` | 15:04:28 |
| 40 | `plan/P01-plan.md` | P01 | cross | 51753 | `214cc4b6a83f` | 15:04:27 |
| 41 | `plan/P02-c-plan.md` | P02 | C | 84874 | `f1448993c468` | 15:09:58 |
| 42 | `plan/P03-o-plan.md` | P03 | O | 44814 | `ee020ac54e9a` | 15:08:53 |
| 43 | `review/R02-review.md` | R02 | cross | 37777 | `fc041d41b89a` | 15:10:01 |
| 44 | `review/R05-reconciliation.md` | R05 | Ca | 18473 | `52a1f54fb555` | 15:10:15 |
| 45 | `scout/K01-gap-recheck.md` | K01 | C | 23754 | `b137a0c2983d` | 15:01:32 |
| 46 | `scout/K02-seed-extract.md` | K02 | C | 30802 | `5bd7aefbd901` | 15:00:33 |
| 47 | `scout/K03-gate-spec.md` | K03 | O | 44109 | `f3a8ba0c6c94` | 15:07:09 |
| 48 | `scribe/S01-integration-draft.md` | S01 | cross | 53872 | `e85fe75ccbf9` | 15:10:23 |
| 49 | `scribe/S02-telemetry-draft.md` | S02 | cross | 38512 | `1caf32141ee7` | 15:08:57 |
| 50 | `scribe/S03-shonen.md` | S03 | cross | 21604 | `7748474b58bf` | 15:09:35 |

Totals: 50 files, 1,646,267 bytes. Every row's path is the seat's declared `out` verbatim; no file name, subdirectory, or seat id is off-registry. All files are regular, non-empty (minimum 11,885 bytes) and none is a symlink (`find reports/round-47 -type l -o -type f -size 0` → empty). Zero duplicate-content groups among all 54 files at cut.

Claim mix, measured after this artifact lands (declared in `targets.json`, not inferred): C 20 present / 22 declared, O 12 / 21, cross 11 / 13, Ca 8 / 8. The shortfall is therefore O 9 seats (O07, O08, O11, O14, O15, V02, W01, X03, R04), C 2 (W02, R03) and cross 2 (R01, Q01); Ca is complete. This artifact is the 51st declared file; it is not in the table above, which is the pre-write cut.

## 4. Non-seat files (4)

None of these is a declared `seats[].out`; each is a round-contract or telemetry artifact permitted by round policy, and each is named explicitly here rather than waved through as "expected".

| path | class | bytes | sha256 |
|---|---|---:|---|
| `reports/round-47/claims.json` | round contract (claims + baseline) | 6113 | `7eb16979ba88bb43a61553c6b62168854f6fe2e2f98852dc14affe45f9e1fa34` |
| `reports/round-47/targets.json` | round contract (seat registry) | 18755 | `d60e55724c8695ed9980b0543324275b28ff97d7de001d2999f3669cdb09ca3d` |
| `reports/round-47/telemetry/dispatch-declared.json` | telemetry: declared dispatch | 985 | `3d82636945893f15666ea0a99097ffaab41ef922182367073a94d112497d31e8` |
| `reports/round-47/telemetry/refire-key6.json` | telemetry: refire note | 605 | `caa92a0fcc4e4a22d2e7654598135cb3c95b58e8a1cad0c7227b5be9957984b0` |

Digest-pin check: `telemetry/dispatch-declared.json:15-16` pins `claims.json` = `7eb16979…` and `targets.json` = `d60e55…`; both measured values above match byte-for-byte at the cut. `claims.json:7` pins baseline `6e9a30d`; HEAD resolves to `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe`. No contract drift.

Telemetry completeness (AGENTS.md obligation: owner, observation window, counting command and date, durable paths and digests):

- `dispatch-declared.json` — complete for its kind: owner, `declared_at_utc`, provider/model/key, requested 64, batched 1, baseline, and digests of both contract files. It declares intent only; it is not an observed count.
- `refire-key6.json` — **partial**. It records owner (`kotodama-shokunin (integrator)`), a date-only `recorded_at_utc: "2026-10-19"` (no time or sampling window), the missing-seat list, and the key-6/402 contingency. It has no counting command, no observed launch/completion/failure counts, and no digests. Its `missing_seats` list re-measures exactly at this cut (§2), so its one checkable claim holds; everything else stays `null` rather than inferred zero.

## 5. Writes outside `reports/round-47/`

```console
$ git rev-list --count 6e9a30d..HEAD
0
$ git diff --name-only
(empty)
$ git diff --cached --name-only
(empty)
$ git status --porcelain=v1 -uall -- corpus/ tools/ examples/ .ufo/ PROVINCE.md LOG.md
(empty)
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ test -e corpus/knowledge/culture-material/cartography-and-mapmaking.md && echo present || echo absent
absent
```

No corpus byte was written, staged, or committed by this round's seats; the C landing is still a fenced draft (the single proposed corpus delta is absent at the cut, as the claim requires pre-apply). `LOG.md` is untouched (no r47 entry; integration is the parent's job). The only status entry outside `reports/round-47/` is the file in §5.1.

### 5.1 `reports/round-46/review/R01-review.md` — one write into a filed round

```console
$ git status --porcelain=v1 -uall | grep -v '^?? reports/round-47/'
?? reports/round-46/review/R01-review.md
$ stat -c '%y %s' reports/round-46/review/R01-review.md
2026-10-19 14:48:54.991867030 -0300 6657
$ grep -n 'R01-review' reports/round-46/targets.json
17:  {"id": "R01", ... "out": "review/R01-review.md"}
$ grep -n 'R01-review' reports/round-46/validation.json
148:  "Named non-author reviewer: ... its review lands at review/R01-review.md."
```

Classification: **not an r47 seat write and not a corpus write.** It is the r46-declared `R01` review artifact (`reports/round-46/targets.json:17`) that r46's own receipt says lands at that path (`reports/round-46/validation.json:148`). Its mtime, 17:48:54Z, is 2 m 02 s after r47's declaration (17:46:52Z), i.e. it was filed during the r47 window into a round directory that was already closed (`reports/round-46/validation.json` exists; LOG.md admits r46). It is untracked, so no filed byte was edited — a new file, not a rewrite.

Disposition: r46's owner/integrator should decide whether it is accepted as a late r46 artifact or removed; it cannot map to any r47 seat out, so under the r47 write-surface rule it is **out of registry**. Attribution to a process is `to-verify` — git has no commit for it and untracked files carry no author metadata. Do not count it toward r47's 64 outs.

### 5.2 `tools/harness/__pycache__/basename-couples-resolver.cpython-314.pyc` — bytecode side-effect

```console
$ stat -c '%y %s' tools/harness/__pycache__/basename-couples-resolver.cpython-314.pyc
2026-10-19 14:58:36.264542273 -0300
$ git check-ignore -v tools/harness/__pycache__/basename-couples-resolver.cpython-314.pyc
.gitignore:4:__pycache__/   tools/harness/__pycache__/basename-couples-resolver.cpython-314.pyc
```

Classification: **gitignored, content-neutral bytecode**, not a source write and not a tracked-byte change. Its mtime (17:58:36Z) proves at least one in-tree import of the couples resolver ran during this round without `PYTHONDONTWRITEBYTECODE=1`, contrary to the shared-environment rule. It does not alter `tools/harness/basename-couples-resolver.py` and cannot affect any claim's evidence; it is recorded here because the census must name every non-round path whose mtime moved. Whether the resolver's source digest changed is outside this seat (none did: working tree clean); `to-verify` only which seat ran it — untraceable.

## 6. Integrity checks on the filed artifacts

- **Self-declaration:** 51/51 seat files (including this one) contain their own seat id within the first 25 lines; 50/51 contain their own out path. The exception is `cov/C07-contract-audit.md`, whose header says `Writes: this fragment only` and never echoes the path; its filename, seat id, and digest are otherwise on-registry (§3 #16). Recorded as a cosmetic header omission, not a path error.
- **One seat, one file:** every declared out maps to exactly one file and no seat has a second artifact anywhere under `reports/round-47/`. No file sits in a subdirectory that its seat did not declare.
- **No stubs or duplicates:** all 51 seat files are ≥ 11,885 bytes; 0 duplicate sha256 groups across all 55 files after this write. Nothing is a symlink or empty.
- **Header hygiene:** all 51 seat files mention baseline `6e9a30d`; 30/51 name `targets.json` explicitly. `tools/gates/frozen/**` and `.ufo/**` appear only as scan exclusions or rule recitals (e.g. `scout/K03-gate-spec.md:59,319`, `plan/P01-plan.md:110`), not as proposed apply targets; full proposal-surface review is A01's remit and this census verifies only actual bytes on disk.

## 7. Telemetry / validation mapping

Round precedent (`reports/round-44/telemetry/`, `reports/round-46/telemetry/`) and the round-runner template (`templates/round-runner-template.py:14,20`) define the close set. Measured at cut:

| required artifact | at cut | evidence |
|---|---|---|
| `reports/round-47/telemetry/dispatch-declared.json` | **present** | §4; digests pinned |
| `reports/round-47/telemetry/observed-dispatch.json` | **absent** | `ls` → no such file |
| `reports/round-47/telemetry/availability-close-47.json` | **absent** | `ls` → no such file |
| `reports/round-47/run-validation.py` | **absent** | `ls` → no such file |
| `reports/round-47/validation.json` | **absent** | `ls` → no such file |

This matters twice over. First, `claims.json` cites `python3 reports/round-47/run-validation.py` as a `counting_command` for the O and Ca claims (`claims.json:45,56`); that command is not runnable at this cut, so any claim of a green receipt would be unearned. Second, AGENTS.md requires the availability record to be closed by a new append-only snapshot under the same round's `telemetry/` once `validation.json` lands. Neither the observed-dispatch snapshot nor the closing snapshot exists, and `refire-key6.json` is a dispatch note, not a close. Status: **`could-not-evaluate`** for the close-state half; the prior A03 scratch snapshot independently named the same three missing close artifacts (`.scratch/a03-snapshot.json`, `pending`), corroborating the required set without being used as evidence.

## 8. Re-runnable close gate

The census is deterministic and read-only. Re-run this after the integrator's apply and after every refire seat lands; it exits 1 on any undeclared file, corpus write, or registry mismatch, and prints `PENDING` for absent declared outs and close artifacts. The authoritative, byte-level procedure is embedded here so no scratch script is needed:

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B - <<'PY'
import json, os, subprocess, sys
root='reports/round-47'
t=json.load(open(root+'/targets.json'))
outs={s['out']:s['id'] for s in t['seats']}
present={p for p in outs if os.path.exists(os.path.join(root,p))}
files={os.path.relpath(os.path.join(d,f),root)
       for d,_,fs in os.walk(root) for f in fs}
allowed={'claims.json','targets.json'} | {f'telemetry/{n}' for n in
         ('dispatch-declared.json','observed-dispatch.json','availability-close-47.json')}
undeclared=sorted(files - set(outs) - allowed)
absent=sorted(set(outs) - present)
required=['validation.json','run-validation.py','telemetry/observed-dispatch.json',
          'telemetry/availability-close-47.json']
pending=[r for r in required if not os.path.exists(os.path.join(root,r))]
st=subprocess.run(['git','status','--porcelain=v1','-uall','--','corpus/','tools/',
                   'examples/','.ufo/','PROVINCE.md','LOG.md'],
                  capture_output=True,text=True).stdout.strip()
print('files',len(files),'seats_present',len(present),'seats_absent',len(absent))
print('absent',absent); print('undeclared',undeclared); print('close_pending',pending)
print('outside_corpus_status',repr(st))
bad = undeclared or st or len(present)!=64 or pending
sys.exit(1 if bad else 0)
PY
```

Expected at this cut (measured by running it): `files 55`, `seats_present 51`, `seats_absent 13`, `undeclared ['telemetry/refire-key6.json']`, `close_pending [validation.json, run-validation.py, telemetry/observed-dispatch.json, telemetry/availability-close-47.json]`, `outside_corpus_status ''`, exit 1 (PENDING, not violation). The one `undeclared` hit is the refire note: it is a legitimate dispatch note classified in §4, but its name is outside the three-snapshot convention, so the gate refuses to wave it through silently. The integrator should either whitelist that exact name in `allowed` at close or rename it to the convention; the strictness is intentional.

At true close the gate must print `seats_present 64`, `seats_absent []`, `undeclared []`, `close_pending []`, empty `outside_corpus_status`, and exit 0. The file count is then whatever the integrator's declared non-seat set produces — at minimum 64 seats + `claims.json` + `targets.json` + `run-validation.py` + `validation.json` + three standard telemetry snapshots = 71, plus `refire-key6.json` if retained and whitelisted. The gate asserts the set, not a magic total, so a 71-vs-72 difference is not a failure by itself.

## 9. Open items for the integrator

1. **Fill the 13 absent outs** (O07, O08, O11, O14, O15, V02, W01, R01, R03, R04, X03, Q01, W02) before close; until then `seats_present` < 64 and §8 exits non-zero.
2. **File the close artifacts**: `run-validation.py` (whose path `claims.json:45,56` already cites), `validation.json`, `telemetry/observed-dispatch.json`, and the append-only `telemetry/availability-close-47.json`. Until all four exist, the round's own counting command is non-runnable and the availability record is unclosed.
3. **Disposition `reports/round-46/review/R01-review.md`** (§5.1): an r46-declared artifact filed after r46's receipt and during r47's window. It is not an r47 seat out; the r46 owner should accept it as late or remove it, and it must not be counted in r47's registry.
4. **Record the `.pyc` side-effect** (§5.2) or delete it in the integrator's cleanup; it is gitignored and content-neutral, but it is evidence that the environment rule was not followed by at least one invocation.
5. **Correct `refire-key6.json`'s telemetry shape** if it is retained as availability evidence: add an observation time/window, the counting command, and digests, or explicitly label it a dispatch note rather than a snapshot (it already reads as one). Unknown observed counts stay `null`, not zero.
6. **Optional cosmetic**: `cov/C07-contract-audit.md` does not echo its own out path; add it if headers are machine-parsed.

## 10. Limits of this artifact

- The cut is mid-refire: 51 of 64 seats filed after this write (50 at the 19:08:57Z snapshot), 13 outs still absent. Any file added after the cut is not in §3 and must be caught by §8, not assumed away.
- The census maps paths and digests; it does not judge whether each artifact's content satisfies its claim. That is the reviewers' remit (R01/R02/R04/R05) and the validation runner's.
- File authorship is not observable: all files are untracked, so mtimes and contents are the only provenance. The r46 stray's writer and the `.pyc`'s invoking command are both `to-verify`.
- No command was run against `reports/round-*/run-validation.py`; none exists for r47 and in-tree execution is forbidden by the round rules.
