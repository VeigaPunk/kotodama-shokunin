# ExecSweepReceipts — round 75, wave 2 (BUILD)

Seat: `ExecSweepReceipts` (leaf executor). Lane `kotodama-shokunin`, base
`f556d1049fe651d3d63975600b13acd9fb686f15`. Item: build the red-before / green-after receipts
for claim Ca's sweep repair (ledger pair L75-04, `REPAIR`, fixed surface
`reports/round-28/readme/sweep.py`), with the repaired sweep's `--selftest` case count.

No predicate was judged or widened, no claim/ledger byte touched, the sweep was not edited.

## 1. Files written (all staged, ready to commit)

| staged path | sha256 | bytes |
|---|---|---|
| `.ufo/waves/round-75/w2/stage/reports/round-75/telemetry/sweep-base.txt` | `f88aebae60367741259e7872d6f252b35531edfef67842a114219a36f79d3265` | 4195 |
| `.ufo/waves/round-75/w2/stage/reports/round-75/telemetry/sweep-fixed-at-base.txt` | `5335a51f074eb0d2b8d32aaba2980e25f95743b44163d29c37a95e5845616f7d` | 7060 |
| `.ufo/waves/round-75/w2/stage/reports/round-75/telemetry/sweep-fixed-after-ca.txt` | `745c3c1c07a295d528322fecbcc9d4e7dead61c0ac2ecf37abc9c46fb3d1c60e` | 8260 |
| `.ufo/waves/round-75/w2/ExecSweepReceipts.md` (this report) | — | — |

Each receipt carries the four required elements — the command, the revision/tree identity
(commit + `HEAD^{tree}` + the graded file's sha256), full stdout, exit code — plus a reading that
names the legs the exit code rests on.

## 2. Behavior — the measured chain

| # | tree | instrument | exit | rows/files | red legs |
|---|---|---|---|---|---|
| R1 | base `f556d10` (tree `bb2e1b6f`) | BASE sweep blob `9b2ccac0…` | **1** | 247 / 249 | footer 243 vs live 249 (`FOOTER_TOTAL` + `FOOTER_DIR_TOTALS`), totals 243, 4 missing rows (2 heritage + 2 conlang), 2 `civilizations/` ghost rows, drift 30/32 + 36/40 |
| R2 | base tree + repaired sweep (tree `b191ee8f`) | worktree sweep `7e0566ad…` | **1** | 247 / 249 | exactly 2 missing rows (both heritage) + drift 30/32 + 36/40; footer/totals/ghosts green |
| R3 | base + Ca README edits + repaired sweep (tree `45fcb720`) | worktree sweep `7e0566ad…` | **0** | 249 / 249 | none — footer 249, totals 249, missing [], ghosts [], drift {} |
| C1 | same as R3 | BASE sweep blob `9b2ccac0…` | **1** | 249 / 249 | 243 first footer, totals 243, 2 missing + 2 ghosts (conlang rows) — the instrument mutant |
| C2 | same as R3 minus the two heading repairs | worktree sweep | **1** | 249 / 249 | drift 30/32 + 36/40 only — heading repairs are necessary |
| C3 | same as R3 plus the 2 in-section conlang rows (the superseded 4-row staging) | worktree sweep | **0** but selftest **1** | 251 / 249 | `duplicate_rows` on both conlang files; live selftest check FAIL |

`--selftest` (the repaired instrument's own; `selftest()` at worktree line 257, **14 checks**):
`selftest: 14/14 checks passed` on the R3 tree, exit 0; at base 13 PASS + 1 FAIL ("FAIL live …"),
exit 1 — the first check is a live check on the grade target, so 14/14 is reachable only on a
green tree. Case count as asked: **14**.

The repair's mechanism, as actually measured (report §2 of each receipt):
(a) `FOOTER_RE` now allows the one-line dated-block layout (`[ \t]*\n?[ \t]*` instead of `\n`),
so the existing README:794 and README:815 blocks parse at all; (b) `footer_reading()` takes the
LAST match (249, vector 32/29/40/29/24/95) instead of the first (243); (c) the totals line takes
the last `Total knowledge entries:` match; (d) a partition now ends at any `^## ` heading, and
rows outside every partition are attributed to the unique partition whose disk holds the
basename — which is what turns the round-73 block's two rows into `linguistics` rows instead of
`civilizations` ghosts. No README footer had to be appended for Ca to be green: the live 249
reading already existed at README:815 and the repair reads it.

## 3. Instrument identity — the two "repaired sweep" copies are NOT identical

```
cmp <lane>/reports/round-28/readme/sweep.py <lane>/.ufo/waves/round-75/drafts/sweep-fixed.py
  -> differ: byte 1400, line 28   (worktree 475 lines / 19420 B ; draft 501 lines / 20800 B ;
     diff -u = 50 changed lines: 38 added, 12 removed)
  sha256  worktree 7e0566ad1ae8ec2c5a0f10c62dc8de66abcc180ec3f7af560bceeba1601cad2b
  sha256  draft    6bf975a069d02aee0a10bdc06defb75a5ecc4167d9f24656b1c39aa8f4bd6399
```

**B1 (blocker, resolved by the L1's second IRC but recorded here).** The draft copy does NOT
compile: `py_compile` → `PyCompileError`, and running it on the base tree prints
`IndentationError: unexpected indent` at line 170 (`for f in sorted(fileset - seen):`), exit 1.
Cause: the draft moved `ghosts.extend("unassigned/%s" …)` from before the
`for part in sorted(sections)` loop to after that loop's body (`dup = …`, 8 spaces), leaving the
loop interior at 8 spaces under a 4-space statement. The draft is also a superset: it adds two
constants (`FOOTER_HEAD_RE`, `FOOTER_MARK`) that appear nowhere else in the file (dead code — the
worktree copy has neither). Every number in my receipts is the WORKTREE copy's, confirmed
authoritative by the L1 IRC; if the draft were landed, the sweep would die with a traceback
instead of grading. `sweep-fixed-at-base.txt` §B keeps the failure output as evidence.

## 4. Deviations from the wave-2 ticket, measured (not assumed)

**B2 — "still red on the 4 missing index rows" is not what the repaired instrument reports.**
At base the repaired sweep reports **2** missing rows, not 4: the two
`linguistics/conlang-scholarship…` files are not missing under the repair — their rows already
exist at README:787-788 and the boundary fix attributes them to `linguistics`
(`parts.linguistics.rows = 32`, `duplicate_rows []`). The remaining red is exactly those 2
heritage rows plus the two header-drift partitions. Re-adding the conlang rows in-section is
what produces rows > files (C3) and a failing live selftest. The ticket's item text and
`ScribeReadmeFinal`'s current staging agree with the measurement; the ticket's parenthetical
("4 missing index rows") does not.

**B3 — the staged README edit set moved under this seat twice.** `README.md.ca-edits` was
2341 B / 3 records at 16:51, 3070 B / 4 records (sha256 `3dca9cfd…`, two extra in-section
linguistics rows) at 16:54–16:56, and 2291 B / 3 records (sha256 `e3fa4f8d…`) from 16:57. The
receipts grade the current set — 2 heading LINE-REPLACEs + 2 heritage rows — and pin
`e3fa4f8d…`; C3 preserves what the transient 4-row set would have graded. The tree was built
twice independently (commit `f1bc42aa…` and commit `0a6c6a5a…`) and produced the **same tree
object `45fcb720126077cf52d70a9c9438c012b6e25a9a`**, which is the reproducible identity the
receipts cite; the commit ids differ only by timestamp.

## 5. Attack notes for the judge (evidence, no adjudication)

- **A1.** The sweep's graded `ok` never compares `total_rows` with `total_files`; only the
  selftest's live check does. C3 measured exit 0 with `rows 251 / files 249` and two
  `duplicate_rows`. So the instrument can exit 0 while the README holds more rows than files —
  the claim-Ca REPAIR wording "zero missing rows/ghosts" does not exclude it, and only the
  selftest (not the exit code) catches it.
- **A2.** `ScribeReadmeIndex` F3's claim that the one-line round-73/74 footers "match nothing" is
  true of the BASE regex only; the repaired regex's optional newline is what makes them match, so
  the "variant A / variant B footer grammar fork" in that draft is moot — no new footer is needed
  for Ca, and no future landing is forced into the three-line shape.
- **A3.** The exemption the receipt asks for is only `reports/round-28/readme/sweep.py` (one file,
  +58/−14 vs base): the R3 tree's README delta is exactly 2 changed lines (`:344`, `:407`) and 2
  inserted lines (after `:428`) — nothing else in the tree moves.
- **A4.** Attribution makes claims of index *coverage* depend on filename uniqueness: a future
  same-basename file in two partitions turns those two rows into `unassigned/` ghosts (the
  `len(owners) == 1` branch). Not measured this wave; flagged as the fragile edge of the repair.

## 6. Scope, tooling, scratch

- Wrote only the three staged receipts and this report. Touched no claim, ledger, sweep, corpus
  file, lane git/jj state or index, fleet repo, `scripts/`, `templates/`, `.ufo/state`,
  `shokuknow`.
- Install record: **none** — no tool installed or upgraded (python3 stdlib + git only; pacman
  never run).
- Scratch: `/fast/scratch/hyaku/kotodama-r75/ExecSweepReceipts/` (three clone trees + two
  controls), deleted before yielding; each tree asserted
  `git rev-parse --show-toplevel` == its own dir before any commit. The scratch directory was
  reaped externally mid-run (it vanished once); the two independent rebuilds described in B3 are
  the response, and every number in the receipts is reproduced from a run made after the reap.

## 7. Risks / open items for the L1

1. **B1 persists until the draft is deleted or fixed** — it is a trap for any seat that copies
   `drafts/sweep-fixed.py` instead of the worktree file. The receipts name the worktree sha
   explicitly.
2. **B3** — staging files in this wave are being rewritten in place; the receipts pin sha256 of
   every input they used, so a later re-stage will visibly disagree rather than silently.
3. **A1** — if claim Ca's REPAIR leg is meant to imply rows == files, the leg wording does not
   say so; only the selftest carries it, and the claim does not cite this sweep's selftest.
