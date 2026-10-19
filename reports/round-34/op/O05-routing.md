- Seat: O05 | executor | claim O | date 2026-10-19 | baseline da68a6d

# O05 — F-C13-1 routing receipt (draft): guarded vs unguarded filed runners

Scope of this fragment: the routing half of claim O's `after_required` —
"a receipt draft names the routing (guarded re-run protocol for adopted
runners; isolated-copy-only for unguarded ones)" — plus the adoption-gap
standing debt row drafted for SCORECARD. Nothing here executes a filed round
runner in-tree; nothing here writes a filed byte.

## 1. Method, provenance, and what stood in for missing dependencies

The seats this fragment was to read (`scout/K03-guard-pattern.md`,
`op/O04-predicted-inventory.md`, `op/O01-impl.md`, `op/O02-tool-source.md`,
`plan/P02-oc-plan.md`) do not exist on disk at the time of writing, so per the
missing-dependency rule I ran my **own read-only census** and it is the source
of every number below. It will have to be reconciled row-for-row with O04's
predicted inventory and O01/O02's landed instrument (see §7 `## Owed`).

Provenance:

- HEAD = `da68a6d705e41f369f21e8607bfaab5b54077f84` (`git rev-parse HEAD`);
  baseline `da68a6d` per `reports/round-34/claims.json:8`.
- Guard under audit: `tools/harness/receipt_guard.py`, sha256
  `d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1`.
- Working tree at write time: `git status --porcelain` → only `?? reports/round-34/`
  (no filed byte touched by this seat).
- Census inventory: `ls reports/round-*/run-validation.py | wc -l` → **28**.

## 2. Census (28 filed runners, classified)

Machine reproduction (single command, run from the repo root with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

```bash
python3 -c '
import pathlib, re
NAMES = re.compile(r"\b(OUTPUT_REL|OUTPUT|RECEIPT|OUT|output|out)\b")
GUARD = re.compile(r"^\s*(?:namespace\[\"guard_receipt\"\]\(|module\.guard_receipt\(|guard_receipt\(\))")
rows = []
for p in sorted(pathlib.Path(".").glob("reports/round-*/run-validation.py"), key=lambda q: int(q.parts[1].split("-")[1])):
    L = p.read_text().splitlines()
    sites = []
    for i, l in enumerate(L):
        if ".write_text(" not in l:
            continue
        target = l.split(".write_text(")[0].strip()
        window = " ".join(L[max(0, i - 4):i + 1])
        if "validation.json" not in window and not NAMES.search(target):
            continue
        if re.search(r"scratch|temp|clone", target):
            continue
        sites.append(i + 1)
    calls = [i + 1 for i, l in enumerate(L) if GUARD.match(l)]
    site = sites[-1] if sites else None
    pre = [c for c in calls if site and c < site]
    cls = "unguarded" if site and not pre else ("guarded" if site else "NO-RECEIPT-WRITE")
    rows.append(f"{p.parts[1]:>11} {cls:<16} write={site} guard={pre[-1] if pre else None}")
print("\n".join(rows))
'
```

Output (28 lines; identical bytes were held at
`.scratch/o05-census.txt`, sha256
`f71a3b1c04dc85d71b76cefd4ea57cb119d769768851ab806bcaef92ecfffcac` —
scratch is disposable, this listing is the durable copy):

```
    round-5 unguarded        write=194 guard=None
    round-6 unguarded        write=336 guard=None
    round-7 unguarded        write=1171 guard=None
    round-8 unguarded        write=1486 guard=None
    round-9 unguarded        write=1910 guard=None
   round-10 unguarded        write=1054 guard=None
   round-11 unguarded        write=1740 guard=None
   round-12 unguarded        write=1071 guard=None
   round-14 guarded          write=717 guard=420
   round-15 guarded          write=1346 guard=1044
   round-16 guarded          write=1265 guard=1005
   round-17 guarded          write=1431 guard=1124
   round-18 guarded          write=1851 guard=1518
   round-19 unguarded        write=21 guard=None
   round-20 guarded          write=1485 guard=1285
   round-21 unguarded        write=1115 guard=None
   round-22 guarded          write=922 guard=921
   round-23 guarded          write=1097 guard=1094
   round-24 guarded          write=1184 guard=1181
   round-25 guarded          write=1145 guard=1142
   round-26 guarded          write=1909 guard=1906
   round-27 guarded          write=1907 guard=1904
   round-28 guarded          write=2098 guard=2095
   round-29 unguarded        write=922 guard=None
   round-30 guarded          write=923 guard=922
   round-31 guarded          write=1159 guard=1158
   round-32 guarded          write=1143 guard=1142
   round-33 guarded          write=1471 guard=1470
```

Counts: **28 runners, 11 unguarded, 17 guarded.** Each of the 11 unguarded
sites was additionally confirmed by direct reading (not by the heuristic
alone); the target-path constants are cited per row below.

### 2.1 The 11 unguarded runners (receipt written in place, no guard call)

| runner | receipt target | write site | evidence |
|---|---|---|---|
| r5 | `reports/round-5/validation.json` | `run-validation.py:194` | `(HERE / "validation.json").write_text(...)`; `HERE` = `ROOT / "reports/round-5"` |
| r6 | `reports/round-6/validation.json` | `:336` | same idiom as r5 |
| r7 | `reports/round-7/validation.json` | `:1171` | written from the `finally:` block (`try:` `:1053`, `finally:` `:1155`) — **it rewrites the receipt even when measurement raises** |
| r8 | `reports/round-8/validation.json` | `:1486` | `OUTPUT_REL` `:99`; `output = ROOT / OUTPUT_REL` `:1485` |
| r9 | `reports/round-9/validation.json` | `:1910` | `OUTPUT_REL` `:127` |
| r10 | `reports/round-10/validation.json` | `:1054` | `OUTPUT_REL` `:60` |
| r11 | `reports/round-11/validation.json` | `:1740` | `OUTPUT_REL` `:125`; `mkdir` `:1739` |
| r12 | `reports/round-12/validation.json` | `:1071` | `ROUND_DIR` `:15`, `OUTPUT` `:18`; `out = ROOT / OUTPUT` `:1069` |
| r19 | `reports/round-19/validation.json` | `:21` | `pathlib.Path('reports/round-19/validation.json')` — **in-place mutator, see §2.2** |
| r21 | `reports/round-21/validation.json` | `:1115` | `ROUND_DIR` `:18`, `OUTPUT` `:20`; `output = ROOT / OUTPUT` `:1113` |
| r29 | `reports/round-29/validation.json` | `:922` | `ROUND_DIR` `:21`, `OUTPUT` `:23`; `safe_path(OUTPUT).write_text(...)` |

### 2.2 Hazard subclasses worth routing differently

- **B2 — failure-path write (r7 only):** the write at `:1171` sits in the
  `finally:` of `main()` (`:1053`–`:1155`), so an exception mid-measurement
  still lands a receipt. Isolated-copy-only is not merely the polite option
  for r7; an in-tree run can rewrite filed bytes *because* the run failed.
- **B3 — receipt mutation, not regeneration (r19 only):** r19's runner is a
  24-line stub that `json.load`s the *filed* receipt (`:19`), overwrites
  `acceptance_checks_passed`/`failures`/`rerun_at_close` (`:20`) and writes it
  back with `indent=1, ensure_ascii=False` (`:21`). Any provenance field the
  filed receipt carried is either preserved only by luck of the mutation
  (dict update) or re-serialized into a different byte shape than
  `indent=2, sort_keys=True` siblings. Highest blast radius of the eleven:
  it does not regenerate a receipt, it edits filed bytes in place.
- **B4 — receipt that claims isolation while writing in-tree (r5):** r5's own
  receipt text says the previous acceptance receipt "is regenerated only in an
  isolated copy, never overwritten in this tree" (`:193`), 1 line above the
  unconditional in-tree write at `:194`. The prose that the round-33 record
  leant on is not implemented by the code.
- **B5 — non-adoption after the guard existed (r19, r21, r29):** the guard
  debuted in round 14 (`tools/harness/receipt_guard.py` is loaded by r14 at
  `:414`). r14–r18, r20, r22–r28, r30–r33 adopted it; **r19, r21 and r29 were
  filed after the guard existed and still wrote unguarded.** Adoption is
  non-monotonic, not a pre-guard historical accident.

### 2.3 The 17 guarded runners and the two idioms in use

| runner | guard call site(s) | receipt write | idiom |
|---|---|---|---|
| r14 | `guard_preflight()` `:708` (pre-measure) and `:716` (pre-write); `module.guard_receipt(...)` `:420` | `:717` | importlib `spec_from_file_location` (`:414`) |
| r15 | `:1337`, `:1345` | `:1346` | importlib (`:1038`) |
| r16 | `:1256`, `:1264` | `:1265` | importlib (`:999`) |
| r17 | `:1422`, `:1430` | `:1431` | importlib (`:1118`) |
| r18 | `:1842`, `:1850` | `:1851` | importlib (`:1512`) |
| r20 | `:1484` | `:1485` | importlib (`:1279`) |
| r22 | `:911`, `:921` | `:922` | runpy helper (`:827-829`) |
| r23 | `:1094` | `:1097` | runpy helper (`:1064-1066`) |
| r24 | `:1181` | `:1184` | runpy helper (`:1151-1153`) |
| r25 | `:1142` | `:1145` | runpy helper (`:1108-1110`) |
| r26 | `:1906` | `:1909` | runpy helper (`:1855-1857`) |
| r27 | `:1904` | `:1907` | runpy helper (`:1853-1855`) |
| r28 | `:2095` | `:2098` | runpy helper (`:1996-1998`) |
| r30 | `:903`, `:922` | `:923` | runpy helper (`:883-885`) |
| r31 | `:1139`, `:1158` | `:1159` | runpy helper (`:1118-1120`) |
| r32 | `:1123`, `:1142` | `:1143` | runpy helper (`:1102-1104`) |
| r33 | `:1459`, `:1470` | `:1471` | runpy helper (`:1441-1443`) |

Two-phase (guard before `measure()` **and** before the write): r14–r18, r22,
r30, r31, r32, r33. Single pre-write guard: r20, r23–r28. In every one of the
17 the guard call line precedes the receipt write line in the same
unconditional `else`/non-`--check` branch, which is what makes the refresh
protocol in §3 safe (the guard is not merely imported, it is on the write path).

## 3. F-C13-1 routing table (the standing protocol)

Guard semantics, established live and read-only on 2026-10-19 (no file was
written by any of these commands; `git status --porcelain` unchanged):

| command | exit | stderr/stdout |
|---|---|---|
| `python3 tools/harness/receipt_guard.py --selftest` | 0 | `"selftest_passed": true` (JSON receipt, `controls_passed` == `controls_total`) |
| `python3 tools/harness/receipt_guard.py reports/round-33/validation.json` | 3 | `receipt_guard: refusing overwrite path=reports/round-33/validation.json committed_sha=da68a6d705e41f369f21e8607bfaab5b54077f84 committed_blob=4e8089a9f84071bfd81e8bf8c20b412bc852948a; explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]` |
| `REFRESH_RECEIPTS=1 python3 tools/harness/receipt_guard.py reports/round-33/validation.json` | 0 | `receipt_guard: REFRESH_RECEIPTS=1 permits overwrite path=reports/round-33/validation.json … [RECEIPT-GUARD-REFRESH]` |
| `python3 tools/harness/receipt_guard.py reports/round-29/validation.json` | 3 | `… committed_blob=749e6385dd4aa9f92517fef43af26acd32e1ba09 … [RECEIPT-GUARD-COMMITTED]` |
| `python3 tools/harness/receipt_guard.py reports/round-34/validation.json` (uncommitted/nonexistent target) | 0 | (no output — uncommitted receipts are not refused) |

The three branches in code: committed target without `REFRESH_RECEIPTS=1` →
`RECEIPT-GUARD-COMMITTED` refusal (`tools/harness/receipt_guard.py:144-147`);
committed target with the exact value `1` → permission printed, write allowed
(`:148-149`); target not present in `HEAD` → silent pass (`:132-133`; the
unreadable-HEAD pass is `:127-128`).
CLI shape: `receipt_guard.py [--repo-root ROOT] RECEIPT | --selftest`
(`:13`), and the CLI never writes (`main()` at `:354-370` calls `guard_receipt`
and returns; verified above).

### Routing rule R-A — adopted runner (the 17 in §2.3): refresh protocol

Use when a round's declared work must re-verify a filed receipt whose runner
is adopted:

1. Preflight (read-only, never writes):
   `python3 tools/harness/receipt_guard.py reports/round-<N>/validation.json`
   — exit 3 means the receipt is committed and the runner will refuse to
   overwrite it unless step 2's env value is set; exit 0 means the target is
   not committed and the runner will write it without a refresh flag.
2. When the preflight is exit 3 and a refresh is genuinely intended:
   `REFRESH_RECEIPTS=1 python3 reports/round-<N>/run-validation.py`
   The runner guards before measuring (two-phase subset) or before writing,
   and the guard itself re-checks at write time, so a concurrent commit turns
   into `RECEIPT-GUARD-COMMITTED` (exit 3) rather than a silent overwrite.
3. Record the refresh as a new row (before/after digests) per the lane's
   supersession convention; never present a refreshed receipt as the filed one.

### Routing rule R-B — unguarded runner (the 11 in §2.1): isolated-copy only

There is no flag that makes an unguarded runner safe in-tree: it writes
`reports/round-<N>/validation.json` unconditionally (r7 even from `finally:`),
and r19 additionally mutates the filed receipt. For any purpose — verification,
replay, regression evidence — the ONLY sanctioned path is an isolated copy:

```bash
git archive <rev> | tar -x -C .scratch/iso-<N>     # then run inside .scratch/iso-<N>
cd .scratch/iso-<N> && python3 reports/round-<N>/run-validation.py
```

Precedent and form: the round-33 incident was reproduced byte-identically by
"an isolated `git archive` run — `.scratch/c05-iso/`" (`LOG.md:3555`, per
`reports/round-33/adj/A11` §4). Diff the isolated receipt against
`git show HEAD:reports/round-<N>/validation.json` if a re-derivation is
claimed; never copy the isolated receipt back over the filed one.

### Boundary for THIS round

`reports/round-34/targets.json` `shared_rules` states the absolute prohibition
for round 34 ("never execute any `reports/round-*/run-validation.py` in-tree …
isolated git-archive copies only"). The routing table above is the standing
rule for future rounds' declared refreshes; it does not license any in-tree
execution inside round 34, and no round-34 counting command may run a filed
runner in-tree.

## 4. Corrections this census files against the claim O / round-33 record

1. **r26 is guarded, not a hazard.** `reports/round-34/claims.json:41` and
   `LOG.md:3560` name "reports/round-26/run-validation.py … the same hazard
   (`:90`, `:1909`)". The write at `:1909` is preceded by the guard call at
   `:1906` in the same branch (`:1902-1909`), using the runpy helper defined at
   `:1855-1857`. The cited `:90` is the constant
   `OUTPUT = f"{ROUND_DIR}/validation.json"` — a string assignment, not a write
   site, and the apparent source of the misread. r26 must be reclassified
   adopted; the count "four known hazards" is therefore 3 confirmed
   (r5/r6/r7) + 1 disproven (r26).
2. **The real hazard set is larger and was named nowhere:** 11 unguarded
   runners — the record names only r5/r6/r7; the other eight are five
   pre-guard runners (r8–r12) and three filed *after* the guard existed
   (r19, r21, r29; §2.2 B5).
3. **The R-B protocol is not optional bookkeeping for r7 and r19:** r7 writes
   from `finally:` and r19 edits the filed receipt in place, so their hazard is
   not "a stale receipt could be regenerated" but "a failed run or a
   verification run can overwrite filed acceptance bytes".

## 5. Adoption-gap standing debt row for SCORECARD (draft — integrator applies)

Anchors (both verified by `grep -n`): the round-33 admission paragraph ends at
`SCORECARD.md:603`; `SCORECARD.md:604` is `## Planned`.

**Before** (end of the round-33 block, `SCORECARD.md:593-603`):

```
Admission: O/C/A verify and no axis is harmed. Findings on record: **F-C13-1**
… Operator directive recorded: outlined batch
counts per round (concurrency); integrator seats recorded in telemetry.

## Planned
```

**After** (insert between `:603` and `:604`; keep the round-33 paragraph
bytes untouched):

```
## Standing debt (not an axis move)

| debt | status | measurement | re-check command | evidence |
|---|---|---|---|---|
| F-C13-1 guard-adoption gap | open — 17 adopted / 11 unguarded of 28 filed runners; 3 of the unguarded (r19, r21, r29) landed after the guard's round-14 debut; r26 reclassified adopted (the `:90`/`:1909` hazard citation was a constant, not a write) | census 2026-10-19 at `da68a6d` (`reports/round-34/op/O05-routing.md` §2, output digest `f71a3b1c04dc…`) | `python3 tools/harness/receipt_guard.py reports/round-<N>/validation.json` (read-only preflight; exit 3 = committed receipt) | `reports/round-34/op/O05-routing.md` §2–§3; `tools/harness/receipt_guard.py` sha256 `d2297da4e6ce…` |

Owner: future integrate rounds (the runners are filed bytes and are not
repaired in place — `LOG.md:3565-3567`). Reason carried: the filed runners
cannot be edited, and the refresh protocol (rule R-A) only covers adopted
runners; for the eleven unguarded runners the isolated-copy rule (R-B) is the
permanent routing until (if ever) the operator rules otherwise. Next touch:
the first round whose declared work re-verifies a filed receipt.
```

The row deliberately carries no improved/harmed verdict — it is a debt row,
not a claim, and this seat decides no acceptance.

## 6. Limits of this fragment

- The census command in §2 is a heuristic (name + literal window, excluding
  `scratch|temp|clone` targets); it is reproducible and its output is listed
  above, but the classification rests on the direct reads cited in §2.1–§2.3.
  A second heuristic false-negative on one of the 11 was caught during this
  seat's own iteration and fixed in the command above — the listed output, not
  the command's form, is the evidence.
- "Guarded" here means *a guard call precedes the receipt write on the write
  path*; it does not assert that the guard is unbypassable (the guard's own
  limits note publication is not race-proof, `tools/harness/receipt_guard.py`
  selftest `limits[1]`).
- I did not run the instrument (`tools/harness/receipt_guard_adoption.py`) —
  it does not exist yet (§7). My class labels may need mapping onto O01/O02's
  taxonomy; the row-level facts (path, write site, guard site) are what should
  survive that mapping.
- Unknowns left `to-verify`: (a) whether any round's counting commands in
  rounds 8–33 ran an unguarded runner in-tree before the round-33 incident
  (only the r33 window is on record, `LOG.md:3548-3556`); (b) whether r21's
  `--check`-less runner is reachable from any filed counting command.

## 7. Owed

- `reports/round-34/op/O04-predicted-inventory.md` — the predicted inventory
  this fragment was told to route from; not on disk. **Owed**: O04's inventory
  must reproduce §2's 28/11/17 split and the 11 rows in §2.1, or the
  discrepancy must be filed as a defect between the two censuses.
- `reports/round-34/scout/K03-guard-pattern.md` — pattern/taxonomy scout;
  not on disk. **Owed**: reconcile §2.3's two idioms (importlib, runpy) and
  the two-phase/single-phase split with K03's stated pattern.
- `reports/round-34/op/O01-impl.md`, `op/O02-tool-source.md`,
  `op/O03-selftest.md` — instrument design/source/fixtures; not on disk.
  **Owed**: the landed instrument's `--json` output must match §2.1's rows 1:1
  (O07 verifies tool-vs-inventory; this fragment supplies the independent
  census for that comparison).
- `reports/round-34/op/O09-verify-routing.md` — verification of this table's
  coverage; **Owed** to O09: confirm every unguarded runner in the landed
  inventory appears in §2.1 with rule R-B, and that no *adopted* runner is
  routed R-B.
- `reports/round-34/run-validation.py` does not exist yet (confirmed absent
  this round); per the shared rules it was not created or executed here.

## Citations

Files read (line-anchored):

- `reports/round-34/claims.json:8,24,39-49,68-73`
- `reports/round-34/targets.json` (seat O05 object; `shared_rules`)
- `REGIMEN.md:27-50,60-70`
- `SCORECARD.md:593-603`, `SCORECARD.md:604`, `SCORECARD.md:365,400,419,427-446`
  (standing-debt prose convention and row shape)
- `LOG.md:3548-3567` (F-C13-1 incident record, mechanism, prevention, standing
  debt line), `LOG.md:3555` (isolated `git archive` precedent), `LOG.md:3560`
  (r26 hazard claim), `LOG.md:3565-3567` (owners/next touch)
- `tools/harness/receipt_guard.py:1-13` (contract + CLI), `:82-149`
  (`_check_receipt`, path checks, committed-blob branch, `REFRESH_ENV`
  branches), `:152-170` (`guard_receipt`, `round_runner_main`), `:348-351`
  (selftest limits), `:354-370` (`main`)
- Filed runners (write sites and guard calls as tabulated in §2):
  `reports/round-{5,6,7,8,9,10,11,12,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33}/run-validation.py`
  — specific lines: r5 `:152,:193,:194`; r6 `:336`; r7 `:1053,:1155,:1171`;
  r8 `:99,:1485,:1486`; r9 `:127,:1910`; r10 `:60,:1054`; r11 `:125,:1739,:1740`;
  r12 `:15,:18,:1069,:1071`; r14 `:414,:420,:708,:716,:717`;
  r19 `:19,:20,:21`; r21 `:18,:20,:472,:845,:474,:1106,:1113,:1115`;
  r26 `:90,:1855-1857,:1902-1909`; r29 `:21,:23,:919,:922`; r33 `:1441-1443,:1459,:1470,:1471`

Commands run (all read-only; none executed a filed round runner):

- `git rev-parse HEAD` → `da68a6d705e41f369f21e8607bfaab5b54077f84`
- `git status --porcelain` → `?? reports/round-34/` (only)
- `ls reports/round-*/run-validation.py | wc -l` → `28`
- the §2 census command → 28 lines, `sha256(f71a3b1c04dc85d71b76cefd4ea57cb119d769768851ab806bcaef92ecfffcac)`
- `sha256sum tools/harness/receipt_guard.py` → `d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1`
- `sha256sum reports/round-33/validation.json` → `93b28f3635cc11765dd5c4be00e7b8c31ed95dad2f23ce6ec9846684b1b51d9f`
  (matches `SCORECARD.md:582` `93b28f36…`)
- `python3 tools/harness/receipt_guard.py --selftest` → exit 0, `"selftest_passed": true`
- `python3 tools/harness/receipt_guard.py reports/round-33/validation.json` → exit 3, `RECEIPT-GUARD-COMMITTED`
- `REFRESH_RECEIPTS=1 python3 tools/harness/receipt_guard.py reports/round-33/validation.json` → exit 0, `RECEIPT-GUARD-REFRESH`
- `python3 tools/harness/receipt_guard.py reports/round-29/validation.json` → exit 3, `RECEIPT-GUARD-COMMITTED`
- `python3 tools/harness/receipt_guard.py reports/round-34/validation.json` → exit 0 (uncommitted target)
