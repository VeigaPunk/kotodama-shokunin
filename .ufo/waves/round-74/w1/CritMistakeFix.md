# CritMistakeFix — attack on the round-74 mined-mistake plan

Seat `CritMistakeFix` (leaf; no delegation, no background jobs, no `task`). Round 74 / hyaku run 7.
Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `f7104cbce186bc2e1522abf0cfd619cc834628bb`.
Target of the attack: the plan, not the task owner.

Plan under attack

- `reports/round-74/claims.json` (DRAFT, read at 127 lines; claim C 12 legs, claim Ca 11 legs).
- `.ufo/waves/round-74/drafts/mistakes.md` (R74-M1..M4, every row `pending landing`, fix cell 5).
- `.ufo/waves/round-74/drafts/quality-25.md` (the round's quality candidate).
- The wave-1 dispatch briefs that implement the fixes: `ExecLeftovers`, `ExecReceiptRerun73`,
  `ExecJunkFixtures`, `ExecLedger` (`.ufo/waves/round-74/build-w1.py:58-66`).

Rules read for the "which criterion should have caught this" question: `corpus/QUALITY.md`
criteria 11, 17, 19, 21, 22, 23, 24; `PROTOCOL.md:90` (round prompts are snapshots),
`:99,101` (commit-then-push and commit-before-report ordering), `:118-122` ("Landed means
committed, so changes that exist only in a working tree do not count for the round").

## 0. What I ran (honesty block)

Read-only git/grep plus one read-only tool run. No writes outside this file. No fetches (no UA to
record). No tool installs (pacman not run; nothing installed). Scratch: `/tmp/CritMistakeFix/`.

- `git -C <lane> status --porcelain -- .ufo/waves/round-73/w2` → 6 lines (pasted in F1).
- `git ls-tree f7104cb -- .ufo/waves/round-73/w2/` → 37 paths; `RevengerOrigins.md` absent (F6).
- `grep -c scenarios SCORECARD.md` → `0`; `grep -c 'Ca 9 scenarios' LOG.md` → `1` (line 4297);
  `grep -o 'SELFTEST OK: [0-9]* scenarios' reports/round-73/telemetry/selftest-r3.txt` → `10` (F5, F6).
- `python3 -B reports/round-28/readme/sweep.py` → exit 1, output pasted in F7 (the tool is
  documented read-only; it writes only into `tempfile` fixtures).
- `accept-ca.py:806-855,868-915` and `accept-c.py:1137-1143,1186` read as source (F2, F3).
- `/tmp/ScoutLedgerSweepB/ca-at-lands.txt`, `ca-at-lands-main.txt`, `c-at-lands.txt` re-read. Those
  runs are **ScoutLedgerSweepB's**, not mine; I re-read the receipts and the counter source and did
  not re-run the round-73 counters. Every claim I make from them is marked `[peer receipt]`.
- No round-74 counter exists yet (`reports/round-74/` holds `claims.json` and
  `telemetry/census-start.txt`), so no round-74 verdict is claimed anywhere below.

## 1. Verdict table

| mistake | rule that should have caught it | planned fix | recurrence the plan must survive | leg that turns red on the recurrence | verdict |
|---|---|---|---|---|---|
| M1 late seat writes after the push | `PROTOCOL.md:99,101,118-122` (commit-then-push; a working-tree-only change does not count) — no QUALITY criterion | Ca `TRACKED` over the six round-73 paths; `ExecLeftovers` commits them | a round-74 seat edits/creates `.ufo/waves/round-74/w2/*.md` after the L1 push | **none** (no leg reads the round's own seat-report surface; `TRACKED` is round-73-scoped and lands-time) | fix is instance-only; class unfixed (F1) |
| M2 PASS only in seat reports | `QUALITY.md` 19 ("a receipt that does not exist at the lands revision is a FAIL (`unreadable`), never a skip") + 17 (pins) + 23 | Ca `RECEIPTS`: committed PASS receipts for ACCEPT-C-73/CA-73, stamp == `2d1cd91` | the same defect for round 74's own counters | Ca `RECEIPTS` for the round-73 pair only; **claim C has no `STAMP`/`RECEIPTS` leg at all** | the fix cannot produce the receipt it requires as briefed; C's class recurs (F2, F3) |
| M3 counter survivors | `QUALITY.md` 11 (per-clause control, nearest near-miss, "a clause with no control is unverified") + 23 (freeze run) | QUALITY 25 + `FROZENCFG` legs + 4 junk landings (C) / 7 selftest scenarios (Ca) | each round-73 survivor replayed against the round-74 counter | only the four legs the control list names | partial: 4/12 C legs and 5/11 Ca legs controlled; five named survivors have no fixture (F4) |
| M4 scenario-count drift | none exists (the draft says `captured_by: none`) — 17/19/23 pin receipts, not prose | ledger ANNOTATE pair + a SCORECARD correction row | a round-74 report/LOG restating a leg fraction or scenario count that the receipt contradicts | **none** | instance only; the declared red-before is the forbidden all-false base run (F5) |
| defect 5 README footer reading | none (a reading convention, not a rule) | `ScribeReadmeIndex` drafts rows + a new footer | a third dated footer with the same date, read by a first-footer tool | **none**; the tool that measures it still reads the first footer | the plan makes the instrument redder, and the ledger cannot express the tool defect (F7) |

## 2. Findings

### F1 — M1's fix cannot fail on its own recurrence; the plan admits it and ships nothing

Counterexample (constructed — the recurrence has not happened; what is measured is that the plan
contains no leg that would see it). A round-74 wave-2 seat appends to
`.ufo/waves/round-74/w2/ScribeReport.md` after
the L1's push. Which leg turns red?

- Claim C's twelve legs (`ENTRIES ROWS REPOINTED GATE EVIDENCE REJECTS GROUND CITEDLINES CENSUS
  SCRATCHMIRROR COLLCHECK FROZENCFG`) read the registry, the two entries, the four evidence files,
  three named `.ufo/waves/round-74/assimilation/*` artifacts and the two counters' config. None
  reads `.ufo/waves/round-74/w1|w2/*.md` and none reads the worktree.
- Claim Ca's `TRACKED` names the **six round-73 paths** and compares committed bytes at `<lands>`
  to a sha256 recorded in the ledger. A lands-time leg also cannot, by construction, see a write
  that happens after lands.
- `APPENDONLY` covers LOG/SCORECARD/two lessons and the fleet round-73 report; a seat report is not
  in that set.

So no leg turns red, and no further round is needed to reach that conclusion: the plan's own M1 fix
cell already says `none`, and no w1 seat is tasked to add a leg. What the plan ships is the *round-73
instance* (six files committed) — a repair a future round cannot distinguish from a fix.

Evidence.
- `reports/round-74/claims.json:109` — `TRACKED: the ledger's must_track paths (the six
  .ufo/waves/round-73/w2 files) …`.
- `grep -c 'porcelain\|untracked\|worktree' reports/round-74/claims.json` → 1 (that same line).
- `corpus/lessons/round-73-verifier-spotcheck.md:13` routes the class, not the instance.
- The recurrence is already visible in this very round: `git status --porcelain -uall -- .ufo reports
  corpus` at base returns **581** lines, because the round's own scratch (`reports/round-74/`,
  `.ufo/waves/round-74/assimilation/guard-proof/mirror-*`) is untracked. Untracked round scratch is
  normal before the freeze; the point is that only a *scoped, closure-time* check can tell normal
  scratch from a late seat write.

Impacted axes: calibration (the round's own record), operability (the instrument that should make
the next closure cheap).

Smallest safe correction (two pieces, both pre-data):
1. Freeze a **closure receipt**, not a claim leg: `reports/round-74/telemetry/worktree-at-push.txt`,
   produced from the pushed tip after the push, one line per dirty path under the round's surface,
   committed as a post-records commit (QUALITY 19's post-records shape: cited by no frozen predicate).
2. Have the *next* round generate `must_track` from that receipt instead of hand-enumerating, so the
   class is caught one round late by construction, and add a QUALITY criterion (26) that names the
   receipt — a prompt-only rule is a snapshot (`PROTOCOL.md:90`) and cannot carry it.

Red-before (a reviewer runs this; the output is the defect):

```
$ git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin status --porcelain -- .ufo/waves/round-73/w2
 M .ufo/waves/round-73/w2/CritEntryAmendFinal.md
 M .ufo/waves/round-73/w2/ExecSelftestAll.md
 M .ufo/waves/round-73/w2/ScribeLogScorecard.md
 M .ufo/waves/round-73/w2/SimplifierEntries.md
 M .ufo/waves/round-73/w2/drafts/log-entry.md
?? .ufo/waves/round-73/w2/RevengerOrigins.md
```

A `WORKTREE-CLEAN` leg scoped to the round's own surface (`.ufo/waves/round-74 reports/round-74`)
must print `WORKTREE-CLEAN: FAIL dirty=6` on that same state and `PASS dirty=0` at the pushed tip;
fixture: commit a file then append one byte, same command shows ` M <path>`.

Secondary defect in the same row: `TRACKED` freezes the *resolver's verdict*. It requires the six
files at lands to be "byte-equal to the worktree-at-base content recorded in the ledger
(sha256)", while `ExecLeftovers` is briefed to choose per file between `COMMIT-AS-IS` and `REVERT`
(`build-w1.py:66`). If the resolver reverts one, `TRACKED` reds — two authorities over one decision.
Freeze the decision: either declare commit-as-is and tell the resolver revert is out of scope, or
widen the leg to "tracked at lands and the worktree is clean for these six paths", with the
byte choice recorded in the lesson.

### F2 — M2's fix, as briefed, cannot produce the receipt the claim requires

Counterexample. `ExecReceiptRerun73` is briefed to clone the lane, `checkout --detach` at
`2d1cd9140d3a6c42296d71e4f29587582a4a88c0`, and run the two round-73 counters with `--root .`
(`build-w1.py:60`). Both verdicts are known and neither is a PASS:

- ACCEPT-CA-73 prints `LEG FAIL STAMP … problems=['measured f7104cbce186… != lands
  2d1cd9140d3a…']` then `ACCEPT-CA-73: FAIL legs=8/9`, exit 1. Cause:
  `accept-ca.py:896-901` sets `measured` from `git rev-parse --verify main` of `--root`; in a clone
  of the lane `main` is the lane tip, and `leg_stamp` (`:833-855`, check at `:843`) requires `measured == lands`.
  `[peer receipt]` `/tmp/ScoutLedgerSweepB/ca-at-lands.txt`.
- ACCEPT-C-73 prints `LEG FAIL CENSUS … census script not found: <fleet>/scripts/sources-census.sh`
  then `ACCEPT-C-73: FAIL legs=10/11`. Cause: `accept-c.py:1186` defaults
  `fleet_root = dirname(root)`, which in a clone is the mktemp parent. `[peer receipt]`
  `/tmp/ScoutLedgerSweepB/c-at-lands.txt`; the same defect is on record at
  `.ufo/waves/round-73/w2/ExecRerunC.md:363` (M5, "CENSUS needs an undocumented `--fleet-root`").

So claim Ca's `RECEIPTS` leg ("a PASS-at-lands receipt for ACCEPT-C-73 and for ACCEPT-CA-73 …
stamped==evaluated==measured==that revision") is unsatisfiable under the brief. The only way the
executor can make it green is the step ScoutLedgerSweepB used as a *control* — move the clone's
local `main` to the lands (`git -C "$D/lane" branch -f main 2d1cd91…`) — and a receipt produced that
way carries `# measured revision (lane main): 2d1cd91…`, a value the lane's `main` never had. A
re-opener who runs the command printed in `SCORECARD.md:1431` gets FAIL 8/9. That is false
provenance, and it entrenches the live false statement instead of annotating it.

Evidence.
- `SCORECARD.md:1429` (C row) prints a re-run command with **no** `--fleet-root` → CENSUS FAIL.
- `SCORECARD.md:1430` (Ca row) prints a re-run command that FAILs STAMP in any plain clone.
- `[peer receipt]` `/tmp/ScoutLedgerSweepB/ca-at-lands-main.txt` shows PASS 9/9 **only** after
  moving `main`; the pair of receipts is the proof that the PASS depends on a hand-edit of the graded
  root.
- `accept-ca.py:833-855` also makes the failure text misleading: the detail line is formatted
  `stamped=evaluated=measured=<lands>` from `lands`, so the printed header reads
  `measured=2d1cd9140d3a` even in the FAIL line that says measured is `f7104cb…`.

Impacted axes: calibration (primary), operability.

Smallest safe correction (pre-data):
1. `RECEIPTS` requires the receipt to carry a `# reproduce:` line with the **exact** command,
   including `--fleet-root /home/vgpnk/Projects/shokunin` for the C counter and
   `git -C "$D/lane" branch -f main <lands>` before the Ca run; the leg re-runs the stamped
   revision's counter sha (`git rev-parse <stamp>:reports/round-73/accept-ca.py`) and compares it to
   the receipt's `# counter sha256 (self):`.
2. The receipt carries `# provenance: re-derivation at round-73 lands produced by round 74` and the
   `RECEIPTS` leg requires it — otherwise the receipt claims to be round 73's own lands receipt and
   is not.
3. Add a ledger pair (ANNOTATE) for `SCORECARD.md:1429` and `:1430` naming the observed FAIL legs and
   the corrected commands. The round-73 record cannot be repaired; it can only be annotated.
4. Round 74's own counter must define `measured` as the clone's `HEAD` (the evaluated revision) with
   the lane tip as a separate, ungraded disclosure line — otherwise the round reproduces
   `accept-ca.py`'s defect in its own STAMP leg, whose text is copied verbatim from round 73's.

Red-before (reviewer command; `[peer receipt]` output quoted, exit 1):

```
$ D=$(mktemp -d); git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane"
$ git -C "$D/lane" checkout -q --detach 2d1cd9140d3a6c42296d71e4f29587582a4a88c0
$ cd "$D/lane" && python3 -B reports/round-73/accept-ca.py --root . \
    --lands 2d1cd9140d3a6c42296d71e4f29587582a4a88c0 \
    --fleet-root /home/vgpnk/Projects/shokunin | tail -3
LEG FAIL STAMP
     stamped=evaluated=measured=2d1cd9140d3a tree=516ea6c7d926 counter=222d4dd6d408 \
     problems=['measured f7104cbce186bc2e1522abf0cfd619cc834628bb != lands 2d1cd9140d3a6c42296d71e4f29587582a4a88c0']
ACCEPT-CA-73: FAIL legs=8/9
```

```
$ cd "$D/lane" && python3 -B reports/round-73/accept-c.py --root . \
    --lands 2d1cd9140d3a6c42296d71e4f29587582a4a88c0 | tail -2
LEG FAIL CENSUS
ACCEPT-C-73: FAIL legs=10/11
```

### F3 — M2's class recurs for claim C, and the claim invites M4 back

Counterexample. Claim C's after-state is `prints ACCEPT-C-74: PASS legs=<n>/<n>` — no receipt. Claim
C has no `STAMP` and no `RECEIPTS` leg (verified: `C`'s leg names are `ENTRIES ROWS REPOINTED GATE
EVIDENCE REJECTS GROUND CITEDLINES CENSUS SCRATCHMIRROR COLLCHECK FROZENCFG`; `Ca`'s are `LEDGER
BASEMISMATCH REPAIR ANNOTATE APPENDONLY NOSTUB SEPARABLE TRACKED RECEIPTS FROZENCFG STAMP`). After
round 74 lands, ACCEPT-C-74's PASS can again live only in a seat report — the exact routed defect 2,
on the other counter. Ca's `RECEIPTS` leg grades *round 73's* receipts, so it cannot cover it.

Second instance, same family: the after-state `PASS legs=<n>/<n>` is a number a report will restate
by hand. When it drifts, nothing reds (F5). The claim that fixes number drift writes the drift in.

Impacted axes: calibration; coverage (the receipt is the only durable evidence for the four rows).

Smallest safe correction: give claim C the same `STAMP` leg Ca has (adapted: receipt under
`reports/round-74/telemetry/`, stamped == evaluated == measured == `<lands>`, tree equal to
`rev-parse <lands>^{tree}`, counter sha == the blob at lands), and state the after-state as
`ACCEPT-C-74: PASS` plus "receipt committed at `reports/round-74/telemetry/<name>.txt`", not as a
hand-copied fraction. The round's own receipt is post-lands evidence, so grade it post-records or by
the counter's own stdout, never by a lands-time read of a file that lands later (QUALITY 19).

Red-before: at the freeze, run the C counter at a commit where everything else is green and delete
the receipt file → `LEG FAIL STAMP` naming `unreadable`/absent; that is the near-miss. At base the
leg fails for every reason at once, which QUALITY 11 says is not a control. The current absence is
visible now:

```
$ python3 -c "import json;d=json.load(open('reports/round-74/claims.json'));\
print([x.split(':')[0] for x in d['claims'][0]['legs']])"
['ENTRIES','ROWS','REPOINTED','GATE','EVIDENCE','REJECTS','GROUND','CITEDLINES','CENSUS','SCRATCHMIRROR','COLLCHECK','FROZENCFG']
```

### F4 — M3's control set is smaller than the survivor list it claims to close

The draft names eight surviving junctions (`.ufo/waves/round-73/w2/MutPredicateC.md:55-64`: P1,
P2, P3, P4, P5b, P6b, P7a, P7b) plus `ExecRerunC.md:333,347,363` (forged sha256, SCRATCHMIRROR
pins, unreproducible after-command). The round-74 plan's controls are `J1`–`J7`
(`build-w1.py:64`) plus C's four junk landings (`claims.json` `do_nothing_control`). Five named
survivors have no fixture and no leg sentence that could fail on them:

| survivor (round-73 receipt) | round-74 leg | why it can still pass | fixture to add |
|---|---|---|---|
| P5b `(staged s894)` lowercase (`MutPredicateC.md:60`) | `REPOINTED` — "no staged-namespace id … is cited as if it were a lane row" | the sentence names ids in the staged set `S882..S884, S899, S900`; P5b's id is `S894` **and** lowercase, and no case-insensitivity is stated; the fallback clause ("every inline S-id … resolves to one of those five rows") only catches it under an `(?i)` scan | `J8 staged-id-lowercase` → must print `LEG FAIL REPOINTED` |
| P6b fabricated reject row (`:62`) | `REJECTS` — presence of refused ids/files/families with reason and flip | text presence cannot tell a real refuse row from an invented one; the leg reads no staged file and no probed URL | `J9 fabricated-reject` (refuse row naming a file absent from `/home/vgpnk/Projects/shokuknow/merge/kotodama`) → `LEG FAIL REJECTS` |
| P7a rows uncited (`:63`; finding `:109`) | `ROWS` | round 73's sentence carried "union = both entries" and round 74 **dropped it** — `grep -c 'union = both entries' reports/round-74/claims.json` → `0`, while round 73's claims had it. `used-by` "correctly" empty is now the pass condition | restore "union = both entries" (every adopted row cited by at least one admitted entry) and add `J10 rows-uncited` → `LEG FAIL ROWS` |
| EVIDENCE sha256 shape-only (`ExecRerunC.md:333`) | `EVIDENCE` — "a 64-hex sha256 of the fetched body … the body window around the quote stored verbatim" | the stored artifact is a ±400-char window (`reports/round-73/evidence/S876.txt:13`), so the sha can never be recomputed; `sha256: 000…0` passed round 73 and the round-74 sentence does not change the storage shape (`ExecEvidence`'s grammar is `--- window ---` only) | require the full body (or a committed body file) and recompute; `J11 forged-sha` → `LEG FAIL EVIDENCE` |
| SCRATCHMIRROR pins (`ExecRerunC.md:347`) | `SCRATCHMIRROR` — "carrying the four rows and both entries, in a commit strictly before the registry-append commit" | the sentence is carried over: round 73's implementation tested the receipt's **add** commit (`git log --diff-filter=A`), not its bytes at lands, and the entries check was not live | restate as "the receipt's bytes **at `<lands>`** were last written in a commit strictly before the append commit, and the receipt's ids block names both entry paths"; `J12 mirror-entry-pins` → `LEG FAIL SCRATCHMIRROR` |

Two further control-list defects:

- `quote-outside-window` (J2) is an **easy break**, not the nearest near-miss QUALITY 11 demands: a
  forged window that *does* contain the quote (P3/P4) still passes. Either add the near-miss fixture
  or list the quote-provenance clause as review-only/closure re-open (QUALITY 11 explicitly forbids
  covering a clause with a weaker stand-in).
- QUALITY 25's mandatory five slugs (`stub-entries`, `rows-from-staged`, `quote-outside-window`,
  `config-edit-in-graded-tree`, `constant-observe`) are **not** the seven fixtures the round builds.
  `rows-from-staged` has no builder in J1–J7 (J1 is stub entries + matching rows). A freeze that
  ships J1–J7 therefore fails its own criterion: `tools/check-quality25.sh` prints
  `JUNK: PASS controls=4/5` at best. Freeze one slug list and derive both the fixtures and the
  criterion's check from it.

Impacted axes: calibration (the survivor class is exactly the calibration axis), coverage (the
entry/row evidence legs).

Smallest safe correction: add the five fixtures above and the two sentence fixes (`(?i)` on
`REPOINTED`, restore `union = both entries`), then freeze the slug list in one place. Each is
pre-data, cheap, and each one's red-before is the round-73 survivor replay
(`counters/junk-fixtures.py --run-r73`) followed by the round-74 counter on the same fixture.

Red-before (already on disk for the two I can run):

```
$ grep -c 'union = both entries' reports/round-74/claims.json      # round 74
0
$ git show f7104cb:reports/round-73/claims.json | grep -c 'union = both entries'
1
```

### F5 — M4's fix is instance-only and its declared red-before is the control QUALITY 11 forbids

Constructed recurrence (not observed — no round-74 LOG entry or selftest receipt exists at this
read; the numbers are deliberately off by one from a plausible pair): the round-74 LOG entry says
`(claim-C selftest 30/30, Ca 12 scenarios)` while `reports/round-74/telemetry/selftest-ca.txt` would
print `SELFTEST OK: 13 scenarios`. No leg reads either
line: the ledger is frozen pre-data and cannot contain a post-data number, and no criterion compares
prose to a receipt. The M4 fix cell's red-before is "`controls-ca.txt` prints the ANNOTATE leg FAIL
at base" — i.e. the lands==base run, where every clause is false at once. QUALITY 11: "The base run
does not count as a control." As filed, M4's fix is not shown able to fail.

Evidence: `corpus/QUALITY.md` 17/19/23 pin receipt *shape* (`stamped`, `tree`, `counter sha`), never
a prose number; the draft's own `captured-by` cell for M4 is `none`.

Impacted axes: calibration.

Smallest safe correction: a `NUMBERDRIFT` leg in Ca — at `<lands>`, extract every
`legs=<a>/<b>`, `SELFTEST OK: <n> scenarios`, `PASS legs=<n>` and `(… [0-9]+ rows …)` from
`reports/round-74/`+`LOG.md`+the SCORECARD round block, and require each to equal the corresponding
committed receipt; pairs the ledger also carries stay in the ledger. Declare it review-only where no
receipt exists (e.g. a prose count with no instrument) — QUALITY 11's "never covered by a weaker
stand-in".

Red-before (exercised; the two numbers are the defect):

```
$ R=$(grep -o 'SELFTEST OK: [0-9]*' reports/round-73/telemetry/selftest-r3.txt | grep -o '[0-9]*')
$ P=$(grep -o 'Ca [0-9]* scenarios' LOG.md | grep -o '[0-9]*')
$ echo "receipt=$R prose=$P"; [ "$R" = "$P" ]; echo "equal_exit=$?"
receipt=10 prose=9
equal_exit=1
```

Near-miss red-before at lands (the one the fix cell owes): delete only the
`## Corrections — round 74` row → `LEG FAIL ANNOTATE pairs=[<id>]` with every other leg PASS.

### F6 — two claim `before` cells are not re-runnable statements (freeze must correct them)

1. Ca `before`: "report/LOG/SCORECARD '9 scenarios'". `grep -c scenarios SCORECARD.md` → `0`. The
   stale token lives in `LOG.md:4297` and the fleet report only. A pair that also asserts SCORECARD
   is red for the wrong reason.
2. Ca `before`: "the six .ufo/waves/round-73/w2 files modified/untracked in the worktree and absent
   from the pushed tree". `git ls-tree f7104cb -- .ufo/waves/round-73/w2/` lists **37** paths: five
   of the six are present at older bytes; only `RevengerOrigins.md` is absent. "Absent" is true of
   one and false-shaped for five.
3. The ledger brief's mandatory pair (c) asks the builder to "compare sha256 of the base blob vs a
   pinned expected_after sha256 of the worktree content" — but the `LEDGER` leg requires
   `stated_text` found at `stated_at` **in the BASE tree**, and one of the six has no base-tree
   bytes. That pair must anchor on the closure's sentence (`round-73-verifier-spotcheck.md:13`,
   "RevengerOrigins returned no report by filing time") with disposition ANNOTATE, not on the
   absent path.

Correction: both `before` cells and the pair anchoring are pre-data edits; nothing above was
measured after data. Red-before for the freeze: the commands in the cells themselves must return
`0` for SCORECARD and `37`(present)/`absent` for the split, exactly as pasted here.

### F7 — defect 5: the plan's framing misses the live defect, and the instrument stays red

The routed item is "any census reader must take the last footer". Running the committed instrument
shows the README is red for more than the footer, and redder after the plan:

```
$ python3 -B reports/round-28/readme/sweep.py ; echo "exit=$?"
parts {"civilizations": 95, "culture-material": 38, "linguistics": 32, "myth-symbol": 29, "synthesis": 29, "verification": 24}
rows 245 files 247
missing_from_index 4 ['culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md', 'culture-material/heritage-taxonomy-models.md', 'linguistics/conlang-scholarship.amend-2026-10-23.md', 'linguistics/conlang-scholarship.md']
orphan_rows 2 ['civilizations/conlang-scholarship.amend-2026-10-23.md', 'civilizations/conlang-scholarship.md']
header_drift {'culture-material': {'declared': 36, 'files': 38}, 'linguistics': {'declared': 30, 'files': 32}}
totals_line 243 totals_ok False
footer_live {"total": 247, ...}
footer_findings [{"class": "FOOTER_TOTAL", "declared": 243, "live": 247, "date": "2026-10-25"}, ...] footer_ok False
exit=1
```

Three things follow.

1. The tool already computes `footer_live` (247) and still judges the **first** footer
   (`footer_reading()` uses `FOOTER_RE.search`, `reports/round-28/readme/sweep.py:106-115`). Both
   footers are dated `2026-10-25`, so "take the last footer" is not a date rule but a file-order rule.
2. `orphan_rows 2` is a *round-73* defect the wave-1 sweeps did not report: the two
   `conlang-scholarship` index rows were appended at `corpus/README.md:770-771`, after the last
   section (`## civilizations/ (95)` at `:503`), so the section parser attributes them to
   `civilizations/` while the files live in `linguistics/`. Adding two more rows at the end (the
   plan's `ScribeReadmeIndex` item 1) plus a third dated footer (item 2) leaves the tool at exit 1
   with a larger delta: after landing there are three `Counts checked 2026-10-25` footers and the
   first-footer reader is off by 6.
3. The ledger cannot express the tool defect: a pair whose `observe_cmd` runs
   `reports/round-28/readme/sweep.py` needs an interpreter, and Ca's `LEDGER` leg excludes
   interpreters and shell strings (`claims.json` `LEDGER`; selftest scenario
   `shell-string/interpreter argv`). Defect 5's tool half is therefore unobservable as the ledger is
   specified, and `REPAIR`/`ANNOTATE` are statement classes, not tool classes.

Smallest safe correction: (a) one-line repair of `footer_reading()` to take the last match, plus a
ledger pair anchored on `corpus/README.md:734` (disposition REPAIR) whose `observe_cmd` is an
allowlisted first-party tool entry — add `<repo>/reports/round-28/readme/sweep.py` with `python3 -B`
to the allowlist **and** its mutation control (a copy whose `footer_reading` is reverted must change
the observed token from `247` to `243`); (b) file the `orphan_rows`/`header_drift` findings as their
own pairs (the plan's `ScribeReadmeIndex` `## Known gaps` block is the right home for the backlog
line) so the round does not claim a green instrument it does not have.

Red-before: the command above; the fix's red-before is the same command on a copy that still reads
the first footer (`observed 243`) versus the repaired tool (`observed 247`).

### F8 — QUALITY 25, as worded, fails on the round's own control receipts

`quality-25.md` (a) says "no receipt or counter source may contain `config source: lands tree` or
`config source: lane worktree`", and its check "counts every `config source:` line against the
one-line shape". But the round's do-nothing/config control **must** contain exactly that string:

```
$ grep -n 'config source' reports/round-73/telemetry/controls-c.txt
13:# config source: lane worktree: row_set, entries, rejects.refused_staged, …
```

Round 74's `controls-ca.txt` and `junk/*.txt` will carry it too (`config-edit-in-graded-tree`). A
re-opener applying the criterion's words to `reports/round-74/telemetry/` gets `CONFIG: FAIL
forbidden=N` on a correct round. Scope the check to graded receipts (`accept-*.txt`,
`selftest-*.txt` excluded from the forbidden-string scan, or an explicit
`controls-*/junk/**` exclusion) and say so in the clause.

Second, mechanical: the criterion binds from round 74 and requires per-leg `label` +
`leg_sha256` in the claim file, but the frozen candidate has neither —
`grep -c 'leg_sha256\|"label"' reports/round-74/claims.json` → `0`, and every leg is a bare string.
Either convert `legs` to `{label, text, leg_sha256}` at the freeze (pre-data, allowed) or the
criterion's `LEGTEXT: PASS claims=<n> names=0` is a foregone fail.

Impacted axes: calibration, operability (a criterion that cannot pass).

### F9 — committing the round-73 files changes their attribution; the plan checks bytes only

`PROTOCOL.md` (round contract, corrections clause): "history is never rewritten to fix attribution
— but the integrator records the attribution defect in the round notes." Committing the six files
in round-74 commits gives them round-74 committer identity over round-73 content. `TRACKED` checks
bytes and non-emptiness; nothing checks that the round notes say "authored by round-73 seats, landed
late by round 74, commit `<sha>`". Add the sentence to the lesson/report and have the Ca correction
row for the six files cite the commit; otherwise a later reader attributes them to round 74.

Red-before: `grep -c 'late' SCORECARD.md` is not a fair test of prose, so make the requirement
mechanical where it can be — the correction row must carry the landing commit hash
(`grep -c '<sha>' SCORECARD.md` ≥ 1) and the lesson line must name the authoring round.

## 3. What the plan gets right (do not over-rotate)

- `FROZENCFG` with `<freeze>` a **strict ancestor** of `<lands>`, constants read by
  `git show <freeze>:…` — this closes round 73's P7b/F1 in the right place, and the freeze=lands
  degenerate case is rejected in the criterion's own fixture (`quality-25.md`, design note).
- `ExecLeftovers`'s classification brief (late append vs already-carried vs new evidence) is the
  correct shape for the six files; only its interface with `TRACKED` needs freezing (F1).
- The junk-landing receipts being committed **at the freeze** (not after lands) is the right
  application of QUALITY 23; the defect is the fixture set, not the timing (F4).
- The six-file `TRACKED` leg did work as specified in round 73 (`LEG PASS TRACKED paths=2
  problems=[]`, `[peer receipt]`), so the leg is sound; it is the scope that is one round stale.

## 4. Limits of this review

- No round-74 counter exists at this read, so every "the leg will pass/fail" statement about it is a
  prediction from the frozen sentence, not a run. Where I claim a verdict I name the round-73 receipt
  that measured the class, or the source line that decides it.
- The two round-73 reruns (ACCEPT-C-73 10/11, ACCEPT-CA-73 8/9) are ScoutLedgerSweepB's receipts,
  re-read by me at `/tmp/ScoutLedgerSweepB/`; I did not re-execute the counters. The commands above
  are the reproduction path.
- I did not run `tools/check-quality25.sh` (it does not exist in the lane; `quality-25.md` says its
  harness is a `/tmp` artifact). F8's LEGTEXT/CONFIG findings are read from the criterion text and
  the draft claim file.
- Fetch hygiene: no live page was fetched for this review, so no User-Agent is recorded; nothing in
  this report is a "no capture" or unreachability ruling.
