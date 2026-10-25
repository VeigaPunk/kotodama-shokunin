# MutLandedCa — claim-Ca mutation sweep (round 73, wave 2 / FALSIFY, hyaku run 7)

Seat: MutLandedCa. Target: the landed claim-Ca bytes at `0316b8883b4f8d44b8efd720140e7f52f734a102`
(counter `reports/round-73/accept-ca.py`, ledger `reports/round-73/ledger.json`, SCORECARD
`## Corrections — round 73`, SHONEN/SKILL/LOG/README regulation). Leaf seat: no delegation,
no background jobs. Every run below is a real command I executed; outputs pasted are verbatim.

## Method

Throwaway clone, per the item recipe (identity `MutLandedCa throwaway <mut@throwaway.invalid>`
used only inside the clone; one commit per mutant; mutants committed on the clone's `main` so
STAMP's `measured == lands` holds — see "Harness note"):

```
D=/tmp/MutLandedCa/scratch; git -C "$D" init -q && git clone -q \
  /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane" \
  && git -C "$D/lane" checkout -q --detach 0316b8883b4f8d44b8efd720140e7f52f734a102
git -C "$D" rev-parse --show-toplevel     # -> /tmp/MutLandedCa/scratch  (verified before first commit)
```

Detector baseline (cwd `$D/lane`):

```
$ python3 -B reports/round-73/accept-ca.py --selftest
...
SELFTEST OK: 10 scenarios — do-nothing control ... ACCEPT-CA-73: PASS legs=9/9 (clean fixture)
$ python3 -B reports/round-73/accept-ca.py --root . --lands 0316b8883b4f8d44b8efd720140e7f52f734a102 \
    --fleet-root /home/vgpnk/Projects/shokunin
# counter sha256 (self): 222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89
# tree: 9b10fa06a2d3756c8bacfc8fc7b2115921370d97
# ledger: reports/round-73/ledger.json source=lands sha256=c912401dd511d712567d8a704a690bf02fa4a8253a628b8e67ab9473798356b9
LEG PASS LEDGER / BASEMISMATCH / REPAIR / ANNOTATE / NOSTUB / APPENDONLY / SEPARABLE / TRACKED / STAMP
ACCEPT-CA-73: PASS legs=9/9
EXIT=0
```

Baseline green → detector live; every mutant graded against it. Runs used the item's exact
command form: `python3 -B reports/round-73/accept-ca.py --root . --lands <mutant> --fleet-root /home/vgpnk/Projects/shokunin`.

**Harness note:** my first M01 commit sat on a side branch (`m01`) with `main` still at lands;
STAMP went red (`measured (lane main) != lands`) — a harness artifact of my procedure, not a
detector response. Discarded; every recorded mutant below is committed on the clone's `main`.
Corollary for anyone re-running: the frozen run command has no `--main`, so a mutant not on
`main` always dies on STAMP regardless of its mutation.

## Table — mutant | expected leg | observed legs red | survivor?

| # | mutant (one behavior each) | expected leg | observed legs red | survivor? | mutant commit |
|---|---|---|---|---|---|
| M01 | delete correction row L01 from SCORECARD | ANNOTATE (+NOSTUB) | **none — 9/9 PASS** | **SURVIVOR** | 130f5c6b4bb2cced1e1be371bc51273549ca1664 |
| M02 | shorten L02 row to id + one token (`\| L02 \| fixed \| \| \| \|`) | ANNOTATE + NOSTUB | NOSTUB (`stubs=['L02:stated-token,observed-token,rederive-cmd']`); ANNOTATE stayed green | partial kill | eebb99217e8d8d480623303c1393255b07fbd3f5 |
| M03 | swap old/new tokens in L06 row (`\| L06 \| FAIL \| PASS \|`) | ANNOTATE (or NOSTUB) | **none — 9/9 PASS** | **SURVIVOR** | ea267c1d02b77d2eab03c4dd653a343ce9dc321d |
| M04 | remove L03 re-derivation command (cell → `-`) | NOSTUB | NOSTUB | killed | d69d6dc1773e3a76212b391fa9a14035cf3c5428 |
| M05 | `git rm .ufo/waves/round-72/w1/ScoutMergeScan.md` | TRACKED | TRACKED (`absent or empty at lands`) | killed | 4c62635bed77d8b913c5c1af181c9fba5adace27 |
| M06 | blank the `:505` pointer on SHONEN.md:6 | REPAIR | REPAIR (`L04(statement-after='' truth='505' stated-at-base='468')`) | killed | e66b5ff7cdd147187b08e633476c299891582cd4 |
| M07 | revert SKILL.md registry last row to `accept-o-69` | REPAIR | REPAIR (`L08(statement-after='accept-o-69' truth='accept-ca-73' ...)`) | killed | c8329eaa46408b376a284ff422eaeddbac09052a |
| M08 | delete 2 lines from SCORECARD.md body (append-only file) | APPENDONLY | APPENDONLY (`lane-removed=2 ... SCORECARD.md`) | killed | 882a7d08791d65b7551affe138cc11a05e136c80 |
| M09 | remove a line from LOG.md | APPENDONLY | APPENDONLY (`lane-removed=3 1\t3\tLOG.md`) | killed | ce0a84fb261c3409eeaa0a638d5775de10794d76 |
| M10 | edit `corpus/lessons/round-72.md` in place | APPENDONLY | APPENDONLY (`1\t1\tcorpus/lessons/round-72.md`) | killed | 8dd0b69ce7e94e5f8da4bdafdc5b1e66ab0787f5 |
| M11 | rewrite stated line `corpus/README.md:732` in place (`243.` → `999.`) | APPENDONLY (or none) | **none — 9/9 PASS** | **SURVIVOR** | 5fbcec4701c1b7a187d337b22f194ab131c15c55 |
| M12 | add claim-C path `corpus/lessons/round-73.md` into L02 row | SEPARABLE | SEPARABLE (`corrections-rows names corpus/lessons/round-73.md`) | killed | 45fcc06f8a924a0882b2d5fc5e84ba8ad6f33df4 |
| M13 | change ledger `base` to the lands hash | LEDGER | LEDGER (`base='0316b888...' != 8841ad3b...`) | killed | 6f3c08522a974c5dde1512248ac21fe0509d1519 |
| M14 | delete `reports/round-73/ledger.json` | LEDGER (+fail-closed) | LEDGER, BASEMISMATCH, REPAIR, ANNOTATE, NOSTUB, APPENDONLY, TRACKED (7 red; `legs=2/9`) | killed | e518ab3102ac796274df33f1e08aacc751b22ae8 |
| M15 | edit L04 `expected_after` `"505"` → `"999"` | REPAIR | **none — 9/9 PASS** (`green=['L04','L05','L08']`, receipt prints `expected_after='999'`) | **SURVIVOR** | c5d2eb49b406b59edc5286ae599302b04f209e76 |
| M16 | ledger committed only in the worktree (`git rm --cached` + commit; file left on disk) | LEDGER fail-closed | LEDGER (`not committed at <lands> (the default ledger is never read from the worktree)`) + BASEMISMATCH, REPAIR, ANNOTATE, NOSTUB, APPENDONLY, TRACKED (7 red; `legs=2/9`) | killed | 28ce5209cc4486a45ac730cd07dfa17eea78982e |

Observed exit codes: baseline `EXIT=0` (captured); killed mutant `EXIT=1` (captured on the
discarded first M01 run and the M02 rerun); survivor runs end `ACCEPT-CA-73: PASS legs=9/9`.
16 mutants, 4 survivors, 1 partial (M02).

## Survivors — what the leg should check

**M01 + M02 (row↔pair matching is substring-anywhere, so rows are interchangeable).**
`leg_annotate` accepts any correction row that names the pair id *anywhere* and contains both
tokens; the surviving L03 row's note says "same 243 → 245 drift as L01 and 36 → 38 as L02",
so it satisfies L01 (and L02) entirely — same tokens (243/245, 36/38) and L01's rederive text
is a substring of L03's command cell. Deleting L01's row or gutting L02's row leaves both legs
(or ANNOTATE alone) green. Legs should: anchor the id to the id cell (table row must begin
`| L01 |`; list row `^- L01\b`), and reject a row as evidence for a pair whose id it merely
mentions in prose (or require id-cell == pair id). Severity: MAJOR coverage gap in the ANNOTATE
leg — the claim's "each ANNOTATE row carries id, old token, new token and the re-derivation
command" is enforced as prose co-occurrence, not as a per-row record.

**M03 (role-blind token check).** ANNOTATE/NOSTUB verify token *presence*, not *role*: the L06
row asserting old=`FAIL`/new=`PASS` (the exact opposite of the filed truth) passes 9/9. Legs
should: check the stated token in the old/as-filed cell and the observed token in the
new/observed cell (column-aware), since L06's note quotes both tokens inside receipt quotes —
whole-row presence can never catch a swap here. Severity: MAJOR coverage gap shared by both
legs.

**M11 (an annotated statement can be silently falsified in place).** After the mutant, the
README line the L01 row "supersedes" reads `Total knowledge entries: 999.` — a new false
statement — and the counter passes 9/9 because (a) LEDGER/ANNOTATE read the stated side at the
*base* revision only (`statement_after` exists only on the three REPAIR pairs), and (b)
`footer_range` anchors the authorized in-place zone *at* the totals line itself, so the very
line a correction row corrects is an authorized in-place-edit target. Legs should: re-read
`stated_at` at lands for ANNOTATE pairs and fail when the stated token is gone or changed
without a `statement_after` declaration; and/or exclude pair-cited lines from the authorized
in-place span (or require the rewrite to be recorded in the row). Severity: MAJOR — the
append-only discipline the claim advertises ("filed lines stand as filed") is not actually
guarded for the five ANNOTATE pairs.

**M15 (`expected_after` is dead weight for `statement_after` pairs).** L04 graded green with
`expected_after='999'`; `leg_repair` takes the `statement_after` branch and never compares
`expected_after`. The frozen docstring schema documents `expected_after` as "the value at
--lands" and never documents `statement_after` (allowed only as an undeclared extra key), so
the precedence rule is undocumented and unchecked. REPAIR should: fail when
`norm(expected_after) != statement_after token` (cross-check), or the frozen schema must say
`expected_after` is ignored when `statement_after` is present. Severity: MAJOR coverage gap
(a corrupted frozen ledger field is invisible).

## Other landed-bytes findings (not mutants)

- **MINOR — counter docstring leg count is stale.** `reports/round-73/accept-ca.py` docstring
  says "LEGS (8, fixed at freeze)" and names 8; the driver runs and *requires* 9 legs
  (`ok = passed == total and total == 9`; selftest expects the 9 names incl. TRACKED), and
  TRACKED appears nowhere in the module docstring. Reproducer:
  `grep -n 'LEGS (8' reports/round-73/accept-ca.py; grep -n 'def leg_tracked\|total == 9' reports/round-73/accept-ca.py`.
- **MINOR — SKILL.md:704 registry row misstates the selftest output.** Row `accept-ca-73`
  says the selftest "prints `SELFTEST OK: 9 scenarios`"; at lands it prints
  `SELFTEST OK: 10 scenarios` (and the summary then names 9). Reproducer:
  `python3 -B reports/round-73/accept-ca.py --selftest | tail -1` vs
  `grep -n '9 scenarios' SKILL.md`. (Observed in this seat's clone at lands.)

## Honesty / could NOT check

- I did not independently re-derive the fleet-side APPENDONLY inputs (fleet pin `80d8c9b5…`
  blob compare ran green inside every one of the 18 counter runs; I did not audit fleet HEAD
  movement myself).
- I did not attack claim-C bytes or `accept-c.py` (other seats' scope).
- Exit codes were captured directly only for the baseline (`EXIT=0`) and killed runs
  (`EXIT=1`); for other rows the verdict rests on the captured `ACCEPT-CA-73:` legs line
  (exit follows it per the frozen docstring).
- I could not check whether the M01/M02/M03/M11/M15 survivors would be caught by the wave's
  sibling reviewers; this seat only measures the frozen counter.
- First M01 attempt (side-branch STAMP red, commit be0321bc8286e99dc1b3dcf82d4c4d0929943728)
  is harness artifact, excluded from the table.

## Bounds, tooling, restoration evidence

- No tools installed (python3 3.14.8, git 2.56.0 present; PACMAN untouched). No live fetches,
  no downloads, no captures. No `task` spawns. Never messaged peers.
- All reads/writes under the lane were read-only; the lane's only write from this seat is this
  report file. All mutations/commits happened in `/tmp/MutLandedCa/scratch` (disposable), with
  the throwaway identity; `git -C "$D" rev-parse --show-toplevel` verified before the first commit.
- Restoration: after the sweep the clone was reset and verified —
  `git status --porcelain | wc -l` → `0`; `git rev-parse HEAD` → `0316b8883b4f8d44b8efd720140e7f52f734a102`;
  `git rev-parse "main^{tree}"` → `9b10fa06a2d3756c8bacfc8fc7b2115921370d97` (equals the
  baseline receipt's tree). Lane `main` re-read after the sweep: `0316b8883b4f8d44b8efd720140e7f52f734a102` (unchanged).
- Hashes: lands tree `9b10fa06a2d3756c8bacfc8fc7b2115921370d97`; counter sha256
  `222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89`; ledger sha256
  `c912401dd511d712567d8a704a690bf02fa4a8253a628b8e67ab9473798356b9`; per-mutant commits in the table.
