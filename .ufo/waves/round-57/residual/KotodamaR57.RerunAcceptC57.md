# KotodamaR57.RerunAcceptC57 — residual falsify re-run of ACCEPT-C-57

Date: 2026-10-23 (UTC window of run). Role: reviewer, read-only leaf. No installs performed (python3 3.14.8 and git already present; no pacman/uv/npm used).

Method: fresh clones under `/fast/scratch/hyaku/kotodama-r57/KotodamaR57.RerunAcceptC57/` (`clone` at 78d83b5e, `clone-base` at 0314aa98), all git invoked with `env -u GIT_DIR -u GIT_WORK_TREE -u GIT_INDEX_FILE`. Clone `status --porcelain` = 0 lines at both revisions. Lane HEAD is detached at 78d83b5e (parent 43f1e78; base 0314aa98 is 43f1e78^).

## Findings

### 1. PASS — predicate at the landed revision (fresh clone, 78d83b5e, live LOCATE)

`python3 -B reports/round-57/accept-c.py` in the clean clone at 78d83b5e7145317a048c8f584d62739168b836bd (132.9 s):

```
SET PASS count=233 required=233 added=['corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md'] removed=[]
SWEEP PASS exit=0 rows 233 files 233 missing_from_index 0 []
FLOOR PASS cited=42 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE PASS located=40 cited=42 need=34 at=2026-10-23T00:08Z not_located=['S419: http://web.archive.org/web/20251010095509/https://www.college-of-arms.gov.uk/resources/faqs HTTPError', 'S422: https://web.archive.org/web/20230725183454/https://www.legislation.gov.uk/aosp/1672/47/1995-08-01?view=plain HTTPError; https://www.legislation.gov.uk/aosp/1672']
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-57: PASS
rc=0
```

Matches `after_required` (exit 0, all nine legs PASS). The declared falsifier ("LOCATE below ceil(0.8 × cited) when re-run live") is not triggered: 40 ≥ 34.

### 2. PASS — predicate fails at base 0314aa98

`python3 -B reports/round-57/accept-c.py` in the clean clone at 0314aa981071220d206760b5263467faeea05b60 (script exists at base; run from the clone root):

```
SET FAIL count=232 required=233 added=[] removed=[]
SWEEP FAIL exit=0 rows 232 files 232 missing_from_index 0 []
FLOOR FAIL cited=0 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LOCATE FAIL located=0 cited=0 need=0 at=2026-10-23T00:08Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-57: FAIL
rc=1
```

Byte-for-byte the shape declared in `claims.json` `expected_pre_landing_counting`. (First base attempt with cwd outside the clone gave `ACCEPT_C_INPUT_ERROR rc=2` on a relative path — rerun correctly from the clone root; the rc=2 run is superseded by the one above.)

### 3. PASS — entry length

`corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md` at 78d83b5e: 172 lines (`awk END{NR}` = 172, `grep -c ''` = 172, so trailing newline present), 23,334 bytes. ≤ 230.

### 4. PASS — citations exactly S413–S454, one SOURCES row each

- Entry cites 42 distinct ids, exactly S413…S454 (per-id counts: S413×16, S414×2, S415×4, S416×3, S417×4, S418×3, S419×7, S420×3, S421×6, S422×3, S423×3, S424×2, S425×4, S426×3, S427×2, S428×4, S429×6, S430×2, S431×4, S432×3, S433×1, S434×4, S435×3, S436×2, S437×3, S438×2, S439×4, S440×1, S441×4, S442×3, S443×4, S444×2, S445×1, S446×3, S447×3, S448×2, S449×2, S450×4, S451×3, S452×3, S453×2, S454×1; 141 citations total; `outside_S413_S480=0`; no `S###-S###` range notation anywhere in the entry).
- `corpus/SOURCES.md` at 78d83b5e: `row_defs_total=454 max_id=454 in_range_single=42 in_range_multi=[] in_range_missing=[] ids_above_454=[]` — exactly one row per id S413–S454, no gaps, none above S454. Each of the 42 ids is also mentioned exactly once in the whole file (`ids_mentioned_exactly_once=42 ids_not_exactly_once=[]`), so no cross-row noise. Rows are contiguous: S413 at line 442, S454 at line 483 (483−442+1 = 42).
- Diff on SOURCES between base and 78d83b5e: 42 added content lines, all row starts `\| S4xx`, 0 removed content lines, 0 added ids in S481–S489.

### 5. MEASURED DEVIATION — `git diff --name-only 0314aa98 78d83b5e` is 10 files, not 3

```
corpus/README.md
corpus/SOURCES.md
corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md
reports/round-57/claims.json
reports/round-57/separability-manifest.json
reports/round-57/telemetry/controls-c.txt
reports/round-57/telemetry/controls-o.txt
reports/round-57/telemetry/declaration-dry-run.txt
reports/round-57/telemetry/locator-calibration.txt
tools/check-gate-quotes.py
```

Attribution (measured): `git diff --name-only 43f1e78 78d83b5e` = exactly the three declared lands; `git diff --name-only 0314aa98 43f1e78` = the other seven (claim O's checker land plus instruments/receipts). The instructed range spans both claims' commits because claim O (43f1e78) sits between base and C; the three-land property holds exactly for claim C's own commit. No amendment made; this is the measurement.

### 6. PASS with caveat — census

`/home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` from the fleet root: `rc=0`, final line `kotodama	ok	/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md`, with 14 `W04 duplicate url ... across scopes` warnings — S127–S133, S185, S186, S358 (pre-existing rows) and S482, S483, S485, S490 (record rows). None in S413–S454.

Caveat: the census ran on the lane working tree, which is dirty (`git status --porcelain`: 6 modified tracked files + untracked `.ufo/`, lessons, telemetry). Both `corpus/SOURCES.md` and the heraldry entry differ from 78d83b5e there (sha256: README `215e23f8…` matches the commit; SOURCES lane `6171e4a0…` vs commit `7479ec5f…`; entry lane `50a59d2d…` vs commit `28385cb3…`; `git diff --stat` shows entry 30 lines touched — still 172 lines — and SOURCES +11 lines, the uncommitted S481+ record rows). The census verdict therefore describes the live tree, not the frozen claim commit; the predicate-level checks above were run in the clean clone at 78d83b5e and are the authoritative ones.

### 7. PASS — README land consistent

README diff (base→78d83b5e, 11+/3−): revision 2.14 note for the heraldry landing, `## myth-symbol/ (27)` → `(28)`, entry added in filename order between `flood-traditions.md` and `hero-journey-variants.md`, `Total knowledge entries: 232` → `233`, footer `232 files` → `233 files`, directory totals 28/27/… → 28/28/… (full diff at artifact://45356).

## Verdict

**Agree** with what landed at 78d83b5e for claim C. Every check in the assignment passes at the commit: predicate PASS (9/9 legs, live LOCATE 40/42 ≥ need 34), predicate FAIL at base with the exact declared shape, entry 172 ≤ 230 lines, citations exactly S413–S454 with exactly one SOURCES row per id, README/SOURCES/entry lands self-consistent. The only literal miss is that `git diff --name-only 0314aa98 78d83b5e` lists 10 files — fully attributed to claim O's commit 43f1e78 sitting between base and C; claim C's own commit diff is exactly the three declared lands, so no fix is required to claim C (if the three-land check is ever re-asserted, the correct range is `43f1e78 78d83b5e`).

## Residual risk / verification gaps

- LOCATE margin is live-network fragile: S419 and S422 already fail today (web.archive.org HTTPError on two snapshot URLs); the pass needs ≥34 of 42 and currently sits at 40. Upstream availability, not lane content, is the swing factor — consistent with the claim's own falsifier definition.
- Census was not re-run inside the clone (assignment fixes its invocation at the fleet root); its `ok` covers the dirty working tree, per finding 6.
- `reports/round-57/telemetry/controls-c.txt` stub controls were not independently re-executed in this re-run (out of this seat's scope; they are frozen receipts in the diff).
