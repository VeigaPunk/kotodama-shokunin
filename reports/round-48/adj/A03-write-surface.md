# A03 — write-surface census (round 48, claim cross)

- Seat: `A03` | role: verifier | claim: **cross** | round 48, loop 2, position 2
- Out path: `reports/round-48/adj/A03-write-surface.md` (this file; the only path this seat wrote)
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` — `git rev-parse HEAD`; matches `reports/round-48/claims.json` `baseline_commit: "a01405d"` by prefix
- Census cut: **2026-10-19T19:38:40Z** (16:38:40 local, UTC-03:00). File mtimes below are local; add 3 h for UTC.
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root
- Mission (`reports/round-48/targets.json`, seat A03): *"Write-surface census: enumerate every reports/round-48/ file at close; confirm each maps to a declared out path + telemetry/validation; flag any undeclared or corpus write."*

## 0. Verdict at this cut

| census object | measurement | verdict |
|---|---|---|
| Files under `reports/round-48/` | **3 at cut** (`claims.json`, `targets.json`, `telemetry/dispatch-declared.json`); 20 by the 19:40:30Z re-snapshot, 17 of them declared seat outs (§10) | classifiable, §4 |
| Declared seat outs present | **0 / 64** | wave in flight — completeness owed, not a defect (§2) |
| Seat files at an undeclared path | **0** | §2 |
| Undeclared/near-miss paths | **0** | comparator + near-miss rule, §8 |
| Non-seat files | **3**, all allowlisted (contract + telemetry) | §4 |
| Corpus write | **NONE** — 223 total, culture-material 25, `cartography-and-mapmaking.md` absent | §5 |
| Tracked or staged modification | **NONE** — `git diff --name-only` and `git diff --cached --name-only` both empty | §5.3 |
| Writes outside `reports/round-48/` | **1 pre-existing untracked file** (`reports/round-46/review/R01-review.md`), declared by r46; gitignored `.scratch/` only | §5.1–5.2 |
| Declared digests | `claims.json` and `targets.json` SHA-256 **match** `telemetry/dispatch-declared.json` | §6 |
| Close artifacts (`validation.json`, `run-validation.py`, observed dispatch, availability close) | **ABSENT — `could-not-evaluate`** | §7 |
| **Overall** | **PASS for what exists at the cut; CLOSE NOT CERTIFIABLE** | 64 seat outs + close receipts still owed; §8 is the re-runnable close gate |

This is a **mid-wave cut, not a close census**. The round was declared at 19:45:00Z nominal (`claims.json` `declared_at_utc`; §6.2 records the timestamp anomaly) and every seat was dispatched in one batch. At 19:38:40Z no seat fragment had landed yet, so the only verifiable write-surface facts are the declaration artifacts, the absence of out-of-round writes, and the corpus hold. The 0/64 seat count must not be read as a failure of any seat: the wave was still running at the cut. `§8` re-derives every number at close.

## 1. Method

Read-only. No corpus, tool, README, LOG, PROVINCE, or filed-round byte was written or staged. The only write is this artifact. The registry is derived mechanically from `targets.json`, never from prose.

```console
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git status --porcelain=v1 -uall
?? reports/round-46/review/R01-review.md
?? reports/round-48/claims.json
?? reports/round-48/targets.json
?? reports/round-48/telemetry/dispatch-declared.json
$ find reports/round-48 -type f | wc -l
3
$ python3 -B -c 'import json;t=json.load(open("reports/round-48/targets.json"));o=[s["out"] for s in t["seats"]];print(len(o),len(set(o)),t["seat_count"])'
64 64 64
```

`targets.json` role/claim distribution, counted from the registry: verifier 32, executor 13, reviewer 5, critic 5, scribe 4, scout 3, planner 1, connector 1 (= 64); claim C 30, cross 22, Ca 12 (= 64).

## 2. Registry reconciliation

64 declared out paths, **64 unique**, no duplicate and no path collision. Present at cut: **0**. Absent: **64** (63 after this artifact lands). No declared path pre-exists a filed round — every path is under the previously non-existent `reports/round-48/`, so no filed byte can be overwritten by a seat.

| subdir | declared | present at cut | absent |
|---|---:|---:|---:|
| `adj/` | 4 | 0 | 4 |
| `calib/` | 9 | 0 | 9 |
| `cov/` | 26 | 0 | 26 |
| `cross/` | 10 | 0 | 10 |
| `op/` | 4 | 0 | 4 |
| `plan/` | 1 | 0 | 1 |
| `review/` | 5 | 0 | 5 |
| `scout/` | 2 | 0 | 2 |
| `scribe/` | 3 | 0 | 3 |
| **total** | **64** | **0** | **64** |

## 3. Full declared-out manifest (64 rows, snapshot at 19:38:40Z)

| # | seat | role | claim | declared out | at cut | bytes | sha256[:12] |
|---:|---|---|---|---|---|---:|---|
| 1 | K01 | scout | C | `scout/K01-rightsized-spec.md` | — | | |
| 2 | K02 | scout | Ca | `scout/K02-readme-defect.md` | — | | |
| 3 | P01 | planner | cross | `plan/P01-plan.md` | — | | |
| 4 | X00 | connector | cross | `cross/X00-connector.md` | — | | |
| 5 | C01 | executor | C | `cov/C01-entry.md` | — | | |
| 6 | C02 | executor | C | `cov/C02-header.md` | — | | |
| 7 | C03 | verifier | C | `cov/C03-arithmetic.md` | — | | |
| 8 | C04 | verifier | C | `cov/C04-citations.md` | — | | |
| 9 | C05 | verifier | C | `cov/C05-length-contract.md` | — | | |
| 10 | C06 | verifier | C | `cov/C06-collision.md` | — | | |
| 11 | C07 | verifier | C | `cov/C07-boundary.md` | — | | |
| 12 | C08 | verifier | C | `cov/C08-shelf.md` | — | | |
| 13 | C09 | verifier | C | `cov/C09-couples.md` | — | | |
| 14 | C10 | executor | C | `cov/C10-readme.md` | — | | |
| 15 | C11 | verifier | C | `cov/C11-sweep.md` | — | | |
| 16 | C12 | verifier | C | `cov/C12-content.md` | — | | |
| 17 | C13 | scribe | C | `cov/C13-scribe.md` | — | | |
| 18 | Ca01 | executor | Ca | `calib/Ca01-readme-fix.md` | — | | |
| 19 | Ca02 | executor | Ca | `calib/Ca02-overbuild.md` | — | | |
| 20 | Ca03 | verifier | Ca | `calib/Ca03-readme-verify.md` | — | | |
| 21 | Ca04 | verifier | Ca | `calib/Ca04-verify.md` | — | | |
| 22 | Ca05 | executor | Ca | `calib/Ca05-heading-control.md` | — | | |
| 23 | R01 | reviewer | cross | `review/R01-review.md` | — | | |
| 24 | R02 | reviewer | cross | `review/R02-review.md` | — | | |
| 25 | R03 | reviewer | C | `review/R03-c-content.md` | — | | |
| 26 | X01 | critic | cross | `cross/X01-trades.md` | — | | |
| 27 | X02 | critic | cross | `cross/X02-honesty.md` | — | | |
| 28 | A01 | verifier | cross | `adj/A01-scope.md` | — | | |
| 29 | A02 | verifier | C | `adj/A02-ownership.md` | — | | |
| 30 | A03 | verifier | cross | `adj/A03-write-surface.md` | (this file, #4 on disk) | | |
| 31 | S01 | scribe | cross | `scribe/S01-integration-draft.md` | — | | |
| 32 | S02 | scribe | cross | `scribe/S02-telemetry-draft.md` | — | | |
| 33 | S03 | scribe | cross | `scribe/S03-shonen.md` | — | | |
| 34 | V01 | verifier | C | `cov/V01-post-landing.md` | — | | |
| 35 | W01 | executor | C | `cov/W01-landing-spec.md` | — | | |
| 36 | W02 | executor | Ca | `calib/W02-landing-spec.md` | — | | |
| 37 | Q01 | verifier | cross | `cross/Q01-final-gate.md` | — | | |
| 38 | C14 | verifier | C | `cov/C14-example.md` | — | | |
| 39 | C15 | verifier | C | `cov/C15-neighbors.md` | — | | |
| 40 | O01 | verifier | cross | `op/O01-gate-live.md` | — | | |
| 41 | O02 | verifier | cross | `op/O02-resolver-edge.md` | — | | |
| 42 | O03 | scout | cross | `op/O03-next-o.md` | — | | |
| 43 | R04 | reviewer | Ca | `review/R04-readme.md` | — | | |
| 44 | X03 | critic | C | `cross/X03-overbuild.md` | — | | |
| 45 | X04 | critic | cross | `cross/X04-baseline-drift.md` | — | | |
| 46 | M01 | executor | C | `cov/M01-example.md` | — | | |
| 47 | M02 | executor | C | `cov/M02-calibration.md` | — | | |
| 48 | M03 | verifier | C | `cov/M03-method.md` | — | | |
| 49 | N01 | verifier | cross | `cross/N01-numbers.md` | — | | |
| 50 | N02 | verifier | Ca | `calib/N02-integrity.md` | — | | |
| 51 | N03 | verifier | C | `cov/N03-landing-safety.md` | — | | |
| 52 | D01 | executor | cross | `cross/D01-delta-receipt.md` | — | | |
| 53 | C16 | verifier | C | `cov/C16-topic.md` | — | | |
| 54 | C17 | verifier | C | `cov/C17-structure.md` | — | | |
| 55 | C18 | verifier | C | `cov/C18-provenance.md` | — | | |
| 56 | Ca06 | executor | Ca | `calib/Ca06-process-row.md` | — | | |
| 57 | Ca07 | verifier | Ca | `calib/Ca07-readme-integrity.md` | — | | |
| 58 | R05 | reviewer | cross | `review/R05-gate-use.md` | — | | |
| 59 | X05 | critic | Ca | `cross/X05-readme.md` | — | | |
| 60 | A04 | verifier | cross | `adj/A04-post-landing.md` | — | | |
| 61 | O04 | verifier | cross | `op/O04-gate-replay.md` | — | | |
| 62 | E01 | executor | C | `cov/E01-boundary.md` | — | | |
| 63 | E02 | verifier | C | `cov/E02-register.md` | — | | |
| 64 | F01 | verifier | cross | `cross/F01-final-census.md` | — | | |

Every path in this table is copied from `targets.json`, not retyped from prose. No seat may rename its out path; a file at a variant spelling (e.g. `C01-entry-draft.md` for `C01-entry.md`) is a near-miss defect and is caught by the §8 gate's seat-prefix rule.

## 4. Non-seat files (allowlist)

| path | class | declared by | sha256 |
|---|---|---|---|
| `reports/round-48/claims.json` | round contract | `telemetry/dispatch-declared.json` `declared_artifacts` | `bf8df21b641c…` |
| `reports/round-48/targets.json` | seat registry | same, with `seat_count: 64` | `d029eaa1e374…` |
| `reports/round-48/telemetry/dispatch-declared.json` | dispatch telemetry | this round's telemetry surface | `40a96ab6227c…` |
| `reports/round-48/validation.json` | close receipt | absent at cut | — |
| `reports/round-48/run-validation.py` | close runner (integrator only) | absent at cut; named at `claims.json:49` | — |

Any file under `reports/round-48/` other than (a) the 64 declared outs, (b) the five paths above, or (c) `telemetry/*` is **undeclared** and must be reported to the integrator, not silently adopted. At this cut the set is empty.

`claims.json:49` lists `python3 reports/round-48/run-validation.py` among claim Ca's `counting_commands`. The file does not exist at this cut, and the round's shared rule forbids any seat from running `reports/round-*/run-validation.py` in-tree. The command is therefore an **integrator close artifact**, not a seat measurement; Ca's third counting command is `could-not-evaluate` until the integrator files it (§7).

## 5. Corpus and out-of-round write check

### 5.1 Corpus hold

```console
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access 'corpus/knowledge/culture-material/cartography-and-mapmaking.md': No such file or directory
$ git status --porcelain=v1 -uall -- corpus tools examples .ufo LOG.md PROVINCE.md
(empty)
```

No seat has staged or written under `corpus/`. The single C landing and the README edit remain drafts in `reports/round-48/` for the integrator; this cut confirms the pre-landing state is intact (223 / 25 / path absent).

### 5.2 Writes outside `reports/round-48/`

| path | status | classification |
|---|---|---|
| `reports/round-46/review/R01-review.md` | untracked, mtime 14:48:54 local (17:48:54Z) | **pre-existing**; declared as `review/R01-review.md` in `reports/round-46/targets.json`; written ~1 h 50 m before this round's declaration, so not an r48 write |
| `.scratch/**` | gitignored (`.gitignore:7`), pre-existing (r22 scratch trees) | seat temp only; no r48 files at cut |
| `tools/**/__pycache__/*.pyc` | gitignored (`.gitignore:4`); no `.pyc` newer than 16:00 local | no r48 bytecode side-effect |

`git status --porcelain=v1 -uall` therefore shows exactly four lines: one r46 carryover and the three r48 declaration artifacts.

### 5.3 Tracked and staged state

```console
$ git diff --name-only
(empty)
$ git diff --cached --name-only
(empty)
$ git status --porcelain=v1 -uall | wc -l
4
```

No tracked file is modified, staged, or deleted at the cut. `LOG.md` (mtime 16:34:39 local) and `corpus/README.md` (13:31:11 local) predate the round's seat writes and are unmodified; `PROVINCE.md` is from 2026-10-17.

## 6. Provenance and digest checks

### 6.1 Declared digests reproduce

```console
$ sha256sum reports/round-48/claims.json reports/round-48/targets.json
bf8df21b641c1a49a7b71eb46504210a58096dda3f2cefa6c7618b1200535292  reports/round-48/claims.json
d029eaa1e37481918c10c20bb7ced3e3e31a8886a207cca05cb55ee3aaa20446  reports/round-48/targets.json
```

Both equal `telemetry/dispatch-declared.json` `declared_artifacts[*].sha256`. The contract and registry have not been edited since declaration.

### 6.2 Timestamp anomaly in the declarations (`to-verify`)

| artifact | `recorded_at_utc` / `declared_at_utc` | file mtime (UTC) | delta |
|---|---|---|---|
| `claims.json` | `2026-10-19T19:45:00Z` (`claims.json:7`) | `19:36:19.844Z` | declared time is **+8 m 40 s after** the file existed |
| `telemetry/dispatch-declared.json` | `2026-10-19T19:45:00Z` | `19:37:31.180Z` | **+7 m 29 s after** |

A file cannot carry a declaration time later than its own write time unless the timestamp is nominal/planned or a clock differs between the declaring process and this filesystem. This does **not** change the write-surface verdict (no write is misplaced), but it is a provenance inconsistency the round record should not inherit silently. Owner: integrator. Disposition: either the timestamp is a planned dispatch time (then say so in the record) or the clock source is skewed (`to-verify`). X04 (baseline-drift critic) is the natural second reader.

## 7. Owed close artifacts (per `AGENTS.md` telemetry rule)

`AGENTS.md` requires durable availability/dispatch evidence under `reports/round-<N>/telemetry/`, separate requested from observed, with owner, window, counting command and digests; unknown counters stay `null` with owner and reason. At this cut:

| artifact | state | disposition |
|---|---|---|
| `telemetry/dispatch-declared.json` | **present** | requested allocation (64, opencode-go / deepseek-v4.1-flash, key-2) |
| `telemetry/observed-dispatch.json` | **absent** | observed launches/completions/failures/concurrency/route → **`could-not-evaluate`**, owner integrator |
| `telemetry/availability-close-48.json` | **absent** | availability close → **`could-not-evaluate`**, owner integrator |
| `validation.json` | **absent** | claim verdicts → **`could-not-evaluate`** at this cut, owner integrator |
| `run-validation.py` | **absent** | created and run by integrator only; seats must not run it in-tree |

Per the same rule, the closing availability snapshot must be a **new append-only file** naming the record it closes and that record's SHA-256 at close time. A round is not admitted to `LOG.md` while its availability record still owes a closing snapshot.

## 8. Re-runnable close gate

Save nowhere under `corpus/`; run inline or from `.scratch`. It exits non-zero on any write-surface failure and, with `--close`, additionally requires all 64 seat outs and the close receipts. At the 19:38:40Z cut it printed `FAILS: []`, `present 0/64`, `state: pre`; at close it must print `present 64/64`, `FAILS: []`, and the post-landing corpus state (`224 / 26 / present`) if C lands.

```python
import json, os, subprocess, sys, hashlib
R = "reports/round-48"
CLOSE = "--close" in sys.argv
def sh(*a): return subprocess.run(a, capture_output=True, text=True).stdout.strip()
fails, notes = [], []

t = json.load(open(f"{R}/targets.json"))
outs = [s["out"] for s in t["seats"]]
decl = {f"{R}/{o}" for o in outs}
if len(outs) != t["seat_count"] or len(set(outs)) != len(outs):
    fails.append("registry is not 64 unique outs")

actual = {os.path.join(r, x) for r, _, f in os.walk(R) for x in f}
allow = {f"{R}/claims.json", f"{R}/targets.json", f"{R}/validation.json",
         f"{R}/run-validation.py"}
unclass = sorted(p for p in actual
                 if p not in decl and p not in allow and not p.startswith(f"{R}/telemetry/"))
if unclass: fails.append(f"undeclared files: {unclass}")
if any(os.path.getsize(p) == 0 for p in actual): fails.append("zero-byte artifact")

# near-miss: same seat-id prefix in same dir but not a declared path
decl_ids = {}
for o in decl:
    decl_ids.setdefault(os.path.dirname(o), set()).add(os.path.basename(o).split("-")[0])
for p in sorted(actual - decl - allow):
    if p.startswith(f"{R}/telemetry/"): continue
    sid = os.path.basename(p).split("-")[0]
    if sid in decl_ids.get(os.path.dirname(p), set()):
        fails.append(f"near-miss path: {p}")

head = sh("git", "rev-parse", "HEAD")
base = json.load(open(f"{R}/claims.json"))["baseline_commit"]
if not head.startswith(base): fails.append(f"HEAD {head} != baseline {base}")

dirty = sh("git", "status", "--porcelain=v1", "-uall", "--", "corpus", "tools",
           "examples", ".ufo", "LOG.md", "PROVINCE.md")
if dirty: fails.append(f"out-of-round dirty: {dirty}")
if sh("git", "diff", "--name-only") or sh("git", "diff", "--cached", "--name-only"):
    fails.append("tracked/staged modification")

tot = sum(1 for r, _, f in os.walk("corpus/knowledge") for x in f if x.endswith(".md"))
cm = sum(1 for x in os.listdir("corpus/knowledge/culture-material") if x.endswith(".md"))
cart = os.path.exists("corpus/knowledge/culture-material/cartography-and-mapmaking.md")
state = {(223, 25, False): "pre", (224, 26, True): "post"}.get((tot, cm, cart))
if state is None: fails.append(f"illegal corpus census {tot}/{cm}/cartography={cart}")

tel = json.load(open(f"{R}/telemetry/dispatch-declared.json"))
for p, v in tel["declared_artifacts"].items():
    if hashlib.sha256(open(p, "rb").read()).hexdigest() != v["sha256"]:
        fails.append(f"digest mismatch {p}")

if CLOSE:
    missing = sorted(o[len(R) + 1:] for o in decl - actual)
    if missing: fails.append(f"{len(missing)} declared outs absent: {missing}")
    for p in (f"{R}/validation.json", f"{R}/run-validation.py",
              f"{R}/telemetry/observed-dispatch.json"):
        if not os.path.exists(p): notes.append(f"close receipt absent: {p}")

print(f"present seat outs: {len(decl & actual)}/{len(decl)}")
print(f"corpus: {tot}/{cm} cartography={cart} state={state}")
print("FAILS:", fails or "none")
print("NOTES:", notes or "none")
sys.exit(1 if fails else 0)
```

## 9. Boundaries and handoff

- **Not in this seat's remit, deliberately not judged:** claim content, arithmetic, citation anchors, README arithmetic, the r47 defect disposition, telemetry *counts* (no observed sample exists). Those belong to C03–C13, Ca01–Ca07, N01, and X04.
- **What close must add to make this census a clearance:** 63 more declared seat files (this one is #4), `validation.json`, integrator-run `run-validation.py` output, `telemetry/observed-dispatch.json`, and `telemetry/availability-close-48.json`. Until then the verdict is **PASS-for-what-exists / close could-not-evaluate**.
- **Flagged to the integrator:** (1) the `declared_at_utc` vs mtime anomaly (§6.2, `to-verify`); (2) `claims.json:49`'s `run-validation.py` counting command is not runnable by seats and is absent at cut; (3) the r46 carryover is declared by r46, not an r48 write.
- **Owed by this seat:** none. The census is reproducible from the commands above; the gate is self-contained.

## 10. In-flight re-snapshot (2026-10-19T19:40:30Z)

§0 is a declaration-only cut: at 19:38:40Z no seat had landed. Two minutes later the surface had grown to **20 files**, and the registry still describes it exactly:

```console
$ find reports/round-48 -type f | wc -l
20
$ # declared outs present / undeclared / near-miss / zero-byte
present 17 of 64   unclassified []   zero []
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ git status --porcelain=v1 -uall -- corpus tools examples .ufo LOG.md PROVINCE.md
(empty)
$ git diff --name-only
(empty)
```

The 17 declared outs present at this snapshot: `adj/A02-ownership.md`, `adj/A03-write-surface.md` (this file), `calib/Ca03-readme-verify.md`, `calib/Ca05-heading-control.md`, `cov/C02-header.md`, `cov/C04-citations.md`, `cov/C09-couples.md`, `cov/C11-sweep.md`, `cov/C14-example.md`, `cov/C15-neighbors.md`, `cov/M01-example.md`, `cross/N01-numbers.md`, `cross/X00-connector.md`, `plan/P01-plan.md`, `scout/K02-readme-defect.md`, `scribe/S02-telemetry-draft.md`, `scribe/S03-shonen.md`. Every one is byte-equal to a `targets.json` `out`; the other three files are the two contract files and `telemetry/dispatch-declared.json`. Undeclared, near-miss, and zero-byte counts are all **0**.

**Why no digests here:** seats were observed revising their own declared out path in place inside this window — `cov/M01-example.md` 13,960 → 14,001 → 14,094 bytes; `cov/C02-header.md` changed SHA-256 at an unchanged 32,541 bytes; `cov/C04-citations.md` 22,313 → 22,493; `scribe/S03-shonen.md` 23,835 → 23,946 → 23,938. A seat rewriting its **own** declared out is not a write-surface violation (only another seat's path, an undeclared path, or a corpus write is). But it means mid-wave hashes are not close hashes; do not cite them as a certificate. The close-time run of §8 is the only certificate, and its `--close` mode requires 64/64 outs plus the receipts.

The present count is moving while this sentence is read. Treat §10 as evidence that the gate discriminates correctly mid-wave, not as a final tally.
