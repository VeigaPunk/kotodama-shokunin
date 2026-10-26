# ScribeSkillFinal — SKILL.md staged edits for claim Ca (round 75, wave 2)

Seat: `ScribeSkillFinal` (scribe, leaf; no delegation, no background jobs, no `task` spawn).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Base:
`f556d1049fe651d3d63975600b13acd9fb686f15`. Wave 2, round 75 (hyaku run 10).

Nothing was applied to the lane. No lane file outside `.ufo/waves/round-75/w2/` was written; no git/jj
mutation was run; the fleet repo, sibling lanes, `scripts/`, `templates/`, `.ufo/state` and
`/home/vgpnk/Projects/shokuknow` were not touched. All scratch lived under
`/fast/scratch/hyaku/kotodama-r75/ScribeSkillFinal/` and was deleted before yield (receipts copied into
this report and the staged files first).

## 1. Deliverables

| file | bytes | sha256 |
|---|---|---|
| `.ufo/waves/round-75/w2/stage/SKILL.md.ca-edits.md` | 17967 | `08a9cb5eea6f0af7187a41e1fa8a1aa9056e83ca172b0465314ebdfe08a48a2d` |
| `.ufo/waves/round-75/w2/stage/reports/round-75/telemetry/selftest-r72-repeat.txt` | 1543 | `1942ef3817a60eef0f1b765610886da227e05763e7823ae1f77081a4aed9ac57` |
| `.ufo/waves/round-75/w2/ScribeSkillFinal.md` (this report) | — | — |

## 2. Inputs read (DRAFT, not frozen; never edited)

- `reports/round-75/claims.json` — 22398 B, mtime 15:09, `frozen: null`. Claim C: 13 legs, row_set S885..S893
  (nine rows), three entry paths. Claim Ca: 12 legs, `fixed_surfaces` of five entries, including
  `{"path": "SKILL.md", "line": 701, "required": "this is narrative evidence, not a standalone committed receipt"}`
  and `{"path": "reports/round-75/telemetry/selftest-r72-repeat.txt", "required": "SELFTEST: 10/11"}`.
- `reports/round-75/ledger.json` — 10751 B, mtime 14:55: 10 pairs (6 REPAIR, 4 ANNOTATE), `must_track []`.
- `.ufo/waves/round-75/counters/accept-ca.py` — 151903 B, sha256
  `d167093537864fc9572fedec2ee8cd0f8e1f86c7c6daa380e81bfde893975bdb`.
- `.ufo/waves/round-75/counters/accept-c.py` — 20043 B, sha256
  `5e65ba73e88c422980f2bab1b78ee612540cd424c3d4a98af9969d9547bddc8a`.
- `.ufo/waves/round-75/drafts/skill-gates-rows.md` (w1 draft; contract-only, no counter existed when it was
  written — its §5 already flags that the counters must be re-read).

## 3. Lane state at every read

- `git -C … rev-parse HEAD` → `f556d1049fe651d3d63975600b13acd9fb686f15` (equals base).
- `git -C … status --porcelain` (tracked) → `M SHONEN.md`, `M SKILL.md`, `M reports/round-28/readme/sweep.py`;
  untracked `.ufo/waves/round-75/`, `reports/round-75/`. These uncommitted edits were **ignored and never
  graded**; every SKILL.md byte below comes from `git show <base>:SKILL.md`.
- In particular the worktree already carries an uncommitted, longer rewrite of line 701; it was not used.
- Base SKILL.md: 822 lines, 112136 B. Line 701 = the `accept-c-72` gate row (891 chars).
- Registry arithmetic at base: 45 `gate`/`probe` rows naming `reports/round-N/accept-*.py`
  (`grep -cE '^\| [^|]+ \| (gate|probe) \| .*reports/round-[0-9]+/accept-[a-z]+\.py'`) and 45 such blobs
  (`git ls-tree -r --name-only <base> reports | grep -c 'accept-.*\.py$'`) — the `45 == 45` invariant that
  becomes `47 == 47` when both round-75 `gate` rows land with both counter files.

## 4. Edit (a): SKILL.md line 701 — old line → new line

Mechanically derived: `git show <base>:SKILL.md` → line 701; a single substring replacement; the result was
byte-verified against the staged block (`OLD_EQ_BASE True`, `NEW_EQ_COMPUTED True`).

**Old (891 chars):**

```
| accept-c-72 | gate | `python3 -B reports/round-72/accept-c.py --root . --lands <40-hex> [--fleet-root <fleet>]` | Output ends `ACCEPT-C-72: PASS` or `: FAIL legs=10/10` — the denominator is a literal, so a FAIL receipt still reads `legs=10/10`; 0 pass / 1 fail; 2 on missing or non-40-hex `--lands`, or when `--root` has no `.git`; a missing `<fleet>/scripts/sources-census.sh` is an uncaught FileNotFoundError (exit 1, no verdict line). | `python3 -B reports/round-72/accept-c.py --selftest` — measured `SELFTEST: 10/11`, exit 1 at HEAD (`--- clean fixture: expected PASS 10/10, got exit=1`; receipt: SCORECARD.md `## Corrections — round 73`) | base `b60c7b14…`, ids S874/S875, both entry paths, scratch-mirror receipt path, ten mutants pinned in script | read-only against `--lands` via `git show`; selftest builds `tempfile.mkdtemp` fixtures and leaves them behind | kotodama-shokunin |
```

**New (959 chars; sha256 of the line + `\n` = `f6d41163fc2e1a2cd4d64db0cc318b54fc07fcd64fbc541df95f086449d8800a`):**

```
| accept-c-72 | gate | `python3 -B reports/round-72/accept-c.py --root . --lands <40-hex> [--fleet-root <fleet>]` | Output ends `ACCEPT-C-72: PASS` or `: FAIL legs=10/10` — the denominator is a literal, so a FAIL receipt still reads `legs=10/10`; 0 pass / 1 fail; 2 on missing or non-40-hex `--lands`, or when `--root` has no `.git`; a missing `<fleet>/scripts/sources-census.sh` is an uncaught FileNotFoundError (exit 1, no verdict line). | `python3 -B reports/round-72/accept-c.py --selftest` — measured `SELFTEST: 10/11`, exit 1 at HEAD (`--- clean fixture: expected PASS 10/10, got exit=1`; recorded in SCORECARD.md `## Corrections — round 73` — this is narrative evidence, not a standalone committed receipt) | base `b60c7b14…`, ids S874/S875, both entry paths, scratch-mirror receipt path, ten mutants pinned in script | read-only against `--lands` via `git show`; selftest builds `tempfile.mkdtemp` fixtures and leaves them behind | kotodama-shokunin |
```

Single changed span, inside the self-test cell:

- old: `` `--- clean fixture: expected PASS 10/10, got exit=1`; receipt: SCORECARD.md `## Corrections — round 73`) ``
- new: `` `--- clean fixture: expected PASS 10/10, got exit=1`; recorded in SCORECARD.md `## Corrections — round 73` — this is narrative evidence, not a standalone committed receipt) ``

Verified: 8 cells / 9 `|` before and after; no cell gains a `|`; the claim's required sentence is present
verbatim (`NEW_HAS_REQUIRED True`); the required phrase is a substring so the counter's containment check
passes by construction.

Why the base wording is wrong: `SCORECARD.md`'s `## Corrections — round 73` is a section of a larger prose
file, not a standalone committed receipt; the base cell calls it one.

## 5. Edit (b): two `gate` rows staged, with per-sentence provenance

Insertion point: after base line 706 (`accept-ca-74`), before base line 707 (the
`accept-c-73 / accept-ca-73 correction` `note` row) — round order, `note` rows trail. 8 columns; each staged
row verified at 9 `|` / 8 cells with no inner pipe.

### 5.1 `accept-ca-75` — measured and verified

Every cell was checked against the installed counter source and against a real `--selftest` run:

| cell claim | verified at |
|---|---|
| flag set and defaults (`--root .`, `--lands`, `--freeze`, `--fleet-root`, `--main main`, `--combined`, `--selftest`) | `accept-ca.py:3354-3363` |
| `LEG PASS <name>` / `LEG FAIL <name>` + indented detail per leg | `accept-ca.py:280-285` |
| `ACCEPT-CA-75: PASS legs=12/12` / `: FAIL legs=<n>/12`, exit 0/1 | `accept-ca.py:2561-2569` |
| refusal line `ACCEPT-CA-75: FAIL legs=0/12 (refused: …)`, exit 2 | `2430-2432` (printer), `2564-2565` (freeze==lands green), `2467-2468` (LEGCOUNT), `2476-2477` (lands==base) |
| twelve implemented leg names | `203-205` |
| missing `--lands`/`--freeze`/`--fleet-root` → `ERROR:`, exit 2 | `3366-3369` |
| non-40-hex `--lands`/`--freeze`/`--combined` → exit 2 | `3372-3378` |
| `--fleet-root` not a directory → exit 2 | `3380-3382` |
| absent `--lands`/`--freeze`/`--combined` commit → `ERROR: … is not a commit in <root>`, exit 2 | `2446-2457` |
| unreadable frozen claims → exit 2 | `584-594`, `2459-2462` |
| frozen base not a commit → exit 2 | `2472-2474` |
| `--freeze` off the lands first-parent chain → FROZENCFG FAIL, exit 1 (graded, not refused) | `2351-2355`; measured in selftest scenario `freeze-off-first-parent` (`exit=1`, `FROZENCFG=FAIL`) |
| no `--combined` → COMBINED FAIL, `the explicit --combined revision is required`, exit 1 | `2311-2313` |
| pair floor 10, nine-name observe allowlist, round-74 lands `5e4796c0…` / freeze `00c408a0…`, receipt `ACCEPT-CA-74: PASS legs=11/11` | `183-199` |
| read-only, scratch materialization | `2479` (`tempfile.mkdtemp(prefix="r75-ca-")`), allowlist rejections `1017-1055` |

Measured `--selftest` run (counter sha256 `d1670935…`, `TMPDIR` under the seat scratch, 2026-10-27):
**exit 1**, 51 output lines, 34 `selftest:` scenario blocks, **seven** `SELFTEST FAIL:` lines, **no**
`SELFTEST OK:` line:

```
SELFTEST FAIL: clean exit got 1 want 0
SELFTEST FAIL: clean RECEIPTS got 'FAIL' want 'PASS'
SELFTEST FAIL: clean text 'ACCEPT-CA-75: PASS legs=12/12' 
SELFTEST FAIL: annotate-other-token NOSTUB got 'FAIL' want 'PASS'
SELFTEST FAIL: r1-rule2-exempt exit got 1 want 0
SELFTEST FAIL: r1-rule2-exempt text 'ACCEPT-CA-75: PASS legs=12/12' 
SELFTEST FAIL: repair-no-statement LEDGER got 'PASS' want 'FAIL'
```

`clean RECEIPTS` failing in the counter's own fixture is the load-bearing one: the fixture landing cannot yet
satisfy the RECEIPTS leg. The staged row states this red rather than claiming a green selftest.

### 5.2 `accept-c-75` — provisional, declared grammar only

`accept-c.py` is **not runnable**: 511 lines, 20043 B, last line `# --- PART B ---`; no `def main`, no
`argparse`, no `REQUIRED_LEGS`, no leg implementation. Measured twice:

- `python3 -B .ufo/waves/round-75/counters/accept-c.py --selftest` → **exit 0, stdout empty, stderr empty**.
- `python3 -B .ufo/waves/round-75/counters/accept-c.py --root . --lands f556d10… --freeze f556d10…` →
  **exit 0, empty output** (no verdict line).

`reports/round-75/accept-c.py` does not exist yet (`reports/round-75/` holds `claims.json`, `ledger.json`,
`telemetry/`), so the row's entry path is prospective. The staged row therefore quotes the counter's
docstring grammar (`ACCEPT-C-75: PASS legs=13/13`; `ACCEPT-C-75: FAIL legs=0/13 (refused: …)`; `ERROR:` +
exit 2) and labels it **DECLARED GRAMMAR ONLY — NOT MEASURED; DO NOT LAND AS-IS**, with the measured
emptiness spelled out in the same cell. This is the round-74 `accept-ca-74` failure class avoided (a row that
pinned a sha256 and a scenario count that existed nowhere).

### 5.3 Claim-side drift found while verifying

The counter docstring says "eight adopted rows (S885..S892), two entries"; `claims.json` now names nine rows
(S885..S893) and three entry paths. The counter reads its constants from the frozen claims, so the docstring
is prose only — but the frozen `legs[]` must equal the implemented table or LEGCOUNT refuses. Handed to the
freeze.

## 6. Edit (c): ledger pairs that point into SKILL.md

`reports/round-75/ledger.json` holds **10** pairs:

| pair | disposition | `stated_at` |
|---|---|---|
| L75-01, L75-05, L75-06, L75-07 | REPAIR | `SHONEN.md:6` |
| L75-02 | REPAIR | `corpus/README.md:344` |
| L75-03 | REPAIR | `corpus/README.md:407` |
| L75-04 | ANNOTATE | `corpus/README.md:813` |
| L75-08, L75-09 | ANNOTATE | `corpus/lessons/round-74.md:37`, `:38` |
| L75-10 | ANNOTATE | `LOG.md:4318` |

**No pair points into SKILL.md** (no `stated_at` and no `statement_after.path`), and no pair cites
`reports/round-75/telemetry/selftest-r72-repeat.txt`. Both SKILL.md obligations are `fixed_surfaces` entries
with no REPAIR/ANNOTATE disposition; the counter enforces them in the REPAIR leg's fixed-surface loop
(`accept-ca.py:1545-1554`: containment of `required` in `git show <lands>:<path>`, sliced to `line` when an
int is given) and permits the line-701 rewrite through APPENDONLY (`1718-1722` adds a fixed surface's `line`
to the allowed changed lines). Neither surface freezes a sha256, so only the required sentence is pinned.

Consequence for the L1: the SKILL.md edit and the receipt must land in the Ca landing; no SCORECARD correction
row closes them, and claim Ca's kill rule fails the claim on any false leg at `<lands>`.

Line-number fragility: the check slices line 701 literally at `<lands>`. Claim C does not edit SKILL.md, so
701 keeps pointing at the `accept-c-72` row for this round's landings; any future insertion above 701 moves
the target.

## 7. Edit (d): the staged receipt `selftest-r72-repeat.txt`

Claim Ca requires the content `SELFTEST: 10/11` on this surface. Derivation (a genuine repeat, not a
transcription):

- Clone: `git clone -q --no-checkout <lane> /fast/scratch/hyaku/kotodama-r75/ScribeSkillFinal/base/lane` then
  `git checkout -q --detach f556d10…`; `rev-parse HEAD` = `f556d10…` (matches the requested revision),
  `rev-parse --show-toplevel` = the scratch clone, tree `bb2e1b6fa5221db1f11cb3148a1fee7813d20639`.
- Counter in that clone: `reports/round-72/accept-c.py`, sha256
  `355e67f1bdb15d52368ad454d68d8391fd72d1de59622570689c4822d21da3c1`.
- Run: `TMPDIR=<scratch> GIT_CONFIG_GLOBAL=/dev/null GIT_CONFIG_NOSYSTEM=1 GIT_AUTHOR_*… python3 -B
  reports/round-72/accept-c.py --selftest` → **exit 1**, stderr empty, stdout (393 B, 17 lines, verbatim):

```
SELFTEST: 10/11
--- clean fixture: expected PASS 10/10, got exit=1
LEG PASS ENTRIES
LEG PASS ROWS
LEG PASS REPOINTED
LEG PASS GATE
LEG PASS REJECTS
LEG FAIL GROUND
     receipt missing: reports/round-72/telemetry/gap-sweep.txt
LEG PASS CITEDLINES
LEG PASS CENSUS
     exit=0 head=accaa7ffbf35 last-line=kotodama	ok	stub
LEG PASS SCRATCHMIRROR
LEG PASS COLLCHECK
ACCEPT-C-72: FAIL legs=10/10


```

- Staged file = provenance header (command, revision, tree, counter sha256, date, exit, stderr) + that stdout
  block delimited by `# --- stdout (verbatim; the run ends with two empty lines) ---` and
  `# --- end stdout ---`. The block was byte-compared against the captured run: **equal**, including the two
  trailing blank lines and the tab in the CENSUS detail line.
- No committed round-72 selftest receipt exists at base: `reports/round-72/telemetry/` holds `baseline.txt`,
  `census-start.txt`, `census-end.txt`, `controls-c.txt`, `controls-ca.txt`, `gap-sweep.txt`,
  `measures-c.txt`, `measures-ca.txt` — no selftest file. The prior record of the red is narrative:
  `SCORECARD.md:1423` (`## Corrections — round 73`) and `corpus/lessons/round-73.md:111` (R73-M4). Both are
  cited in the receipt header as the prior record, not as the receipt.
- The file contains no lane S-id from claim C's row set and no claim-C path family, so the Ca counter's
  SEPARABLE read set stays clean.

## 8. Commands run (all read-only; scratch under `/fast/scratch/hyaku/kotodama-r75/ScribeSkillFinal/`)

| command | outcome |
|---|---|
| `git -C <lane> show <base>:SKILL.md \| sed -n 690,715p`, `… \| sed -n 701p \| cat -A` | line 701 = `accept-c-72` row, 891 chars, 900 B with newline |
| `git -C <lane> show <base>:SKILL.md \| grep -cE '^\| [^|]+ \| (gate\|probe) \| .*reports/round-[0-9]+/accept-[a-z]+\.py'` | `45` |
| `git -C <lane> ls-tree -r --name-only <base> reports \| grep -c 'accept-.*\.py$'` | `45` |
| python (read-only) over the base line: replace + measure | old 891 → new 959 chars; 8 cells both; new-line sha256 `f6d41163…` |
| `sha256sum .ufo/waves/round-75/counters/accept-c.py .ufo/waves/round-75/counters/accept-ca.py` | `5e65ba73…`, `d1670935…` |
| `python3 -B .ufo/waves/round-75/counters/accept-c.py --selftest` | exit 0, no output |
| `python3 -B .ufo/waves/round-75/counters/accept-c.py --root . --lands <base> --freeze <base>` | exit 0, no output |
| `TMPDIR=<scratch> python3 -B .ufo/waves/round-75/counters/accept-ca.py --selftest` | exit 1; 51 lines; 34 scenario blocks; 7 distinct `SELFTEST FAIL:` lines; no `SELFTEST OK:` |
| `grep` of the Ca counter for `fixed_surfaces` / `SKILL` / `r72` | `fixed_surfaces` read at 618 and used at 1546/1719; the counter names neither `SKILL.md` nor `r72` literally — both obligations flow from the frozen `fixed_surfaces` list |
| `git clone -q --no-checkout … ; git checkout --detach <base>` (scratch) | HEAD = base; `rev-parse --show-toplevel` = the scratch clone |
| `TMPDIR=<scratch> … python3 -B reports/round-72/accept-c.py --selftest` (scratch clone) | exit 1; `SELFTEST: 10/11`; 393 B stdout; empty stderr |
| python byte-comparison of the staged stdout block vs the captured run | equal |
| python row-shape verification of the staged deliverable | `OLD_EQ_BASE True`, `NEW_EQ_COMPUTED True`, `NEW_SHA_OK True`, `NEW_HAS_REQUIRED True`, both rows 9 pipes / 8 cells |
| `sha256sum` of both staged files | `08a9cb5e…`, `1942ef38…` |

No installs or upgrades (nothing was needed); no network access, so no User-Agent record applies to this
seat. No `pacman`.

## 9. Findings and limits

1. **`accept-c.py` is incomplete** — PART A only, ending at `# --- PART B ---`; it prints nothing for every
   invocation. The `accept-c-75` row is staged as declared-grammar-plus-measured-emptiness and **must not be
   landed** until the driver exists and its verdict/refusal grammar is re-measured.
2. **`accept-ca.py --selftest` is red** at sha256 `d1670935…` (exit 1, seven failing checks; `clean RECEIPTS`
   among them). QUALITY 23 wants a green selftest receipt before the falsify wave, so this is a freeze blocker
   unless the counter is repaired; if it is repaired, the staged `accept-ca-75` self-test cell must be
   re-measured (it pins the sha256 it was measured at).
3. **Claims/counter drift**: docstring "eight adopted rows / two entries" vs claims "nine rows S885..S893 /
   three entries". Harmless for the counter (constants come from the frozen claims) but confusing as prose.
4. **The ledger has 10 pairs, not the 11 the w1 draft recorded**; 6 REPAIR / 4 ANNOTATE matches claim Ca's
   after-state exactly.
5. **Neither SKILL.md obligation is anchored by a ledger pair** (see §6). A grader looking for a pair id will
   not find one; the closure is the counter's fixed-surface loop plus the APPENDONLY `line` exemption.
6. **Line-701 fragility**: the frozen `line: 701` is a literal index at `<lands>`; anything inserting a line
   above 701 before the Ca landing moves the target. Claim C does not edit SKILL.md.
7. **Worktree contamination**: the lane worktree already carries an uncommitted rewrite of SKILL.md:701 (and
   `SHONEN.md`, `reports/round-28/readme/sweep.py`). None of it was graded, used or copied; the staged line is
   computed from `git show <base>:SKILL.md`.
8. **Not proven here**: the fixed-surface containment was verified by reading the six-line loop
   (`accept-ca.py:1545-1554`) and by byte-computing the target line, not by running the full counter against a
   simulated `<lands>` (that needs the complete C landing, absent this wave). The staged line and receipt
   satisfy the loop's stated predicate by construction; the end-to-end REPAIR run belongs to the post-freeze
   grading wave.

Scratch `/fast/scratch/hyaku/kotodama-r75/ScribeSkillFinal/` deleted before yield; the two staged files and
this report were the only copies kept.

Report: .ufo/waves/round-75/w2/ScribeSkillFinal.md
