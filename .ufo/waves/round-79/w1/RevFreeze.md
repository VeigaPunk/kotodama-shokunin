# RevFreeze — round-79 W1: freeze constants/ancestry, post-data amendment risks, do-nothing control design

Seat: RevFreeze (reviewer, leaf). Lane base: `44f76d456c1b326a71ffdb381590af825cbf11be`.
All paths below are relative to the lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Scope: the freeze mechanics both round-79 counters (accept-o.py, accept-ca.py) must
implement per QUALITY 25/26 — not the O/Ca claim content (peers RevOContract /
RevCaContract own those). No production file edited; everything under
`.ufo/waves/round-79/w1/stage/RevFreeze/`.

Inputs read (committed bytes at base unless named):
`.ufo/waves/round-79/CLAIMS-DRAFT.md`, `corpus/QUALITY.md` criteria 7–29,
`corpus/lessons/round-78-verifier-spotcheck.md`, `corpus/lessons/round-78.md`,
`reports/round-78/telemetry/census-end.txt`, `reports/round-78/telemetry/census-start.txt`,
`corpus/SOURCES.md` row 839 (S884), `reports/round-74/accept-ca.py` (main_check +
leg_frozencfg, :1836–1933), `.ufo/waves/round-77/w2/MutCaLedger.md`, `.ufo/waves/round-77/w2/ScoutLogPairs.md`,
`.ufo/waves/round-77/w2/ExecCaPass.md`.

## Probe run (raw output preserved)

Built an isolated fixture repository at
`/fast/scratch/hyaku/kotodama-r79/RevFreeze/fixture-repo` (explicitly initialized;
`git rev-parse --show-toplevel` verified = that directory before any mutation;
removed after receipts copied). Driver + a minimal **freeze-shape probe** (reference
only, grades no claim content) live in my stage:

- `.ufo/waves/round-79/w1/stage/RevFreeze/freeze-matrix.py` — builds a deterministic
  fixture (fixed dates/identities → stable commit ids) and runs 10 scenarios against
  any counter command template (`--counter-cmd` with `{repo} {lands} {freeze}`).
- `.ufo/waves/round-79/w1/stage/RevFreeze/freeze-shape-probe.py` — implements ONLY
  the eight refusal/do-nothing conditions; sha256 `b2634a5b…e1e8` (matches the
  `# counter sha256 (self)` line in the run).
- `.ufo/waves/round-79/w1/stage/RevFreeze/freeze-matrix-run.txt` — full raw output,
  sha256 `1627e373…c3b8c`.

Executors can point the same matrix at the real counters, e.g.:
```
python3 -B .ufo/waves/round-79/w1/stage/RevFreeze/freeze-matrix.py \
  --repo /fast/scratch/hyaku/kotodama-r79/<seat>/fixture-repo \
  --counter-cmd 'python3 -B reports/round-79/accept-ca.py --root {repo} --lands {lands} --freeze {freeze} --fleet-root /home/vgpnk/Projects/shokunin'
```

## Freeze-matrix results (observed, exit codes)

| scenario | shape exercised | observed | verdict |
|---|---|---|---|
| s01_green | freeze strict first-parent ancestor; freeze blobs == lands blobs | exit 0, `PASS legs=2/2` | as designed |
| s02_do_nothing | `--lands == --freeze` | exit 1, both legs green, `FAIL legs=2/2 (do-nothing control: PASS refused)` + `# NOTE: lands == freeze` | as designed |
| s03_lands_eq_base | `--lands` = frozen base | exit 2 `(REFUSED: --lands equals the frozen base …)` | as designed |
| s04_off_first_parent | freeze is an ancestor via merge but NOT on lands first-parent chain (`--no-ff` side commit) | exit 1, `LEG FAIL FROZENCFG … not on the lands first-parent chain` | as designed |
| s05_not_ancestor | freeze carries claims.json but is not an ancestor of lands | exit 1, `LEG FAIL FROZENCFG … is not an ancestor of --lands` | as designed |
| s06_claims_amended_at_lands | claims.json narrowed post-freeze in graded tree | exit 1, `LEG FAIL FROZENCFG … edited in the graded tree after freeze` | as designed |
| s07_freeze_non_commit | `--freeze 000…0` | exit 2 `ERROR: --freeze … is not a commit` | as designed |
| s08_lands_non_commit | `--lands 000…0` | exit 2 `ERROR: --lands … is not a commit` | as designed |
| s09_claims_not_at_freeze | freeze without claims.json | exit 2 `(REFUSED: claims file … is not committed at --freeze …)` | as designed |
| s10_legcount | counter leg table ≠ frozen `leg_names` | exit 2 `(REFUSED: leg table ['FROZENCFG','STAMP'] != the frozen 1 legs ['FROZENCFG'])` | as designed |

Caveat, stated: the probe is my own reference implementation of the QUALITY 25(a)
text — its green run proves the *fixture* is exercisable; it says nothing about the
production counters, which do not exist yet and were not run by this seat.

## Findings

### F1 — the round-79 freeze commit is greenfield; nothing to inherit

Round 78 was an honest stop: `reports/round-78/` contains only `telemetry/`
(`census-start.txt`, `census-end.txt`) — no claims.json, no ledger.json, no
counter. QUALITY 26(a) therefore binds the round-79 freeze commit to carry, in one
commit: `reports/round-79/claims.json`, `reports/round-79/ledger.json` (Ca adds it;
O's observation records ride it or the claims config per ExecOCounter's draft),
both counters (`reports/round-79/accept-o.py`, `accept-ca.py`), the guard
(`tools/ledger-token-guard.py`), the do-nothing receipts and both selftest receipts.
Junk landings, the junk generator, and `junk-o.txt`/`junk-ca.txt` land AFTER the
freeze (26(a): "evidence about the frozen counters, not part of the freeze").
No round-78 file satisfies any of these shapes, so "adapt the round-78 freeze"
is a trap: there is nothing to adapt.

### F2 — the ancestry requirement is two independent limbs; test both

QUALITY 25(a) refuses a freeze "not an ancestor of <lands> on the lands first-parent
chain". The round-74 reference (`reports/round-74/accept-ca.py:1836–1858`) implements
this as (i) `merge-base --is-ancestor freeze lands` AND (ii) `freeze ∈ rev-list
--first-parent lands`. Limb (ii) is not redundant: my s04 shows a freeze that passes
limb (i) — a `--no-ff`-merged side commit — while being off the lands first-parent
chain. A counter checking only `merge-base` accepts a freeze that the graded lands
never actually contained on its mainline; conversely a counter checking only
first-parent membership would accept a rebase-shaped history where freeze is on the
chain but not an ancestor of the lands *tree* being graded. Both limbs observed red
independently (s04, s05). Round-79 counters must refuse (or FROZENCFG-red, per the
chosen graded-vs-refused design; round-74 grades with a leg FAIL) on either limb.

### F3 — do-nothing control design: graded, NOTE'd, PASS refused — and pinned outside the lane

The do-nothing control for both O and Ca is `--lands == --freeze` (a landing that
adds nothing): graded, never passed. Observed shape (s02): both legs green, verdict
`FAIL legs=n/n (do-nothing control: PASS refused)` plus a `# NOTE: lands == freeze`
line in the receipt. QUALITY 23 additionally requires each counter to be *run at the
freeze commit* (receipts present, landing absent) pre-data, so artifact-vs-leg shape
mismatches show before data lands — for round 79 that receipt is one of the two
do-nothing receipts committed at the freeze commit itself.

QUALITY 26(c) correction binds here: `accept-c.py` grades and PASSES a complete
landing used as its own freeze while `accept-ca.py` refuses that shape; "only an
external pin decides a junk freeze, and a round that relies on lands == freeze
being red must say it is a do-nothing control only". Round 79 must record, in the
claims text and the round report: (i) lands==freeze-red is a do-nothing control
only; (ii) the freeze commit hash is pinned in the round report / fleet records
(the external pin the lane itself cannot supply — QUALITY 25 limits: "a rewritten
freeze commit is not detectable in the lane at all"). The freeze hash must also
travel in every graded receipt header (`# freeze: <40hex> (config read at this
commit only)`, round-74 shape) so a post-hoc freeze rewrite is at least detectable
as *receipt-vs-report* disagreement.

Design decision recommended for the draft: accept-o/accept-ca should both grade
(rather than refuse) lands==freeze, matching accept-c.py's 26(c)-compliant shape,
and refuse only `lands == frozen base` (s03) — refusal for the base and grading
for the do-nothing keep the two controls distinguishable in receipts.

### F4 — post-data amendment risk register

Each row names the amendment, the control that must kill it, and where it is
exercised. "FROZENCFG" = the freeze-blob/ancestry leg in its round-74 shape
(`leg_frozencfg`, problems list, graded FAIL not refusal, for graded-tree edits).

| # | post-data amendment | killing control | exercised |
|---|---|---|---|
| A1 | claims.json narrowed/rewritten at lands after data | FROZENCFG blob compare `git rev-parse <freeze>:<path>` vs `<lands>:<path>` (both claims_rel and ledger_rel) | s06 (claims leg); ledger leg identical by construction |
| A2 | ledger.json edited at lands (pair set/observations swapped post-freeze) | FROZENCFG same compare | matrix topology (same code path as s06) |
| A3 | guard stubbed at lands: `tools/ledger-token-guard.py` replaced by a printer of expected lines | QUALITY 28: O counter runs guard bytes from `git show <freeze>:tools/ledger-token-guard.py` (or sha256-compares freeze vs lands blob before exec); O selftest must carry the stub-guard mutant red | not runnable pre-data — design requirement on ExecOCounter |
| A4 | counter leg/scenario changed after freeze without a recorded revision | QUALITY 23: change lands in `reports/round-79/counter-revisions.md` (old sha, new sha); QUALITY 26(d): any gate row pinning a counter sha256 re-derives it from installed bytes before landing | s10 covers the leg-table half; counter-revisions.md is an L1 integration obligation |
| A5 | do-nothing/selftest receipt typed without the run | QUALITY 23 first limb: receipt carries verbatim verdict line + exit code + counter sha256 | s02 raw shape is the required receipt shape |
| A6 | receipt re-stamped in place, original bytes lost | QUALITY 17: original receipt bytes preserved below a marker; APPENDONLY leg (J6 class) | lane-side, post-freeze |
| A7 | original census-end.txt edited at lands to match the wrong token | Ca correction binds the original receipt digest; Ca APPENDONLY re-derives `git show <base>:reports/round-78/telemetry/census-end.txt` sha256 == bound digest | pinned below (§F5) |
| A8 | S884 registry row edited in place at lands (used-by cell changed to the wrong token) | Ca counter re-derives the actual token from `git show 4b255745dea45a45d88b17e3c3fea4cdb6700cf7:corpus/SOURCES.md` — the recorded measured revision — never from the lands worktree; in-place tier/used-by edits are QUALITY 6 defects on their own | pinned below (§F5) |
| A9 | junk freeze (freeze commit already contains the complete landing) | not detectable in-lane; external pin only (F3) | stated as residual risk |
| A10 | freeze commit rewritten after receipts stamped | not detectable in-lane; receipt `# freeze:` header + external pin make it detectable as receipt-vs-report disagreement | stated as residual risk |

### F5 — Ca's correction must bind the measured revision because the receipt doesn't

`reports/round-78/telemetry/census-end.txt` header carries only `Command:` and
`Exit:` lines — no stamped/evaluated/tree header (contrast the round-74 counter
receipt shape, QUALITY 19). That gap is part of how the defect happened, and it
makes the correction's four bindings load-bearing. Pinned at base `44f76d45…`:

- census-end receipt W01 line for S884: `used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md`; receipt sha256 `05b5011a…5867`.
- census-start receipt W01 line for S884: `used-by=…amend-2026-10-23.md`; receipt sha256 `8f753788…0461`.
- Registry S884 row 12 (`corpus/SOURCES.md:839`) at base and at `4b255745…`: `…amend-2026-10-23.md`.
- `git cat-file -e 44f76d45:corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md` → `fatal: path … does not exist` (the token names no file that ever existed in this lane, matching routed defect 2's diagnosis of an uncommitted/regressed working-tree state at capture time).
- Ancestry: `git merge-base --is-ancestor 4b255745… 44f76d45…` exit 0; `4b255745…` appears in `git rev-list --first-parent 44f76d45…`.

So the correction's binding is exactly: original receipt digest
(`05b5011a…` over the base blob), measured revision `4b255745dea45a45d88b17e3c3fea4cdb6700cf7`,
old token `…amend-2026-10-24-r13.md`, actual token `…amend-2026-10-23.md`.
Note the actual token is re-derived from the registry at the *measured revision*,
not from base: the registry at base equals the registry at `4b255745…` for this
cell today, but the receipt defect is precisely that a receipt can be captured
against working-tree state, so the correction must not silently grade "base
registry" either — it must grade the revision it names.

### F6 — LEGCOUNT is the freeze's own text; name the check owner

QUALITY 25(c): the frozen `legs[]` is authoritative; the counter refuses
(exit 2, `FAIL legs=0/<n> (refused: LEGCOUNT …)`) on count/name drift, prints
`# frozen legs: <n> (<NAMES>)`, and every `LEG PASS|FAIL <NAME>` line carries a
frozen name. s10 exercises the refusal. Round-73's own history is the warning:
it declared `LEGS (8, fixed at freeze)` while its driver required 9 (QUALITY 25(c)).
For round 79, a non-author seat must run the criterion-11 clause list against
the claim statement words before dispatch (ScribeClaims drafts; a reviewer
re-checks) — flagged as a W2 obligation, not done here.

## Exact commands (re-runnable)

```
# Ca evidence (lane, read-only)
git show 44f76d456c1b326a71ffdb381590af825cbf11be:reports/round-78/telemetry/census-end.txt | sed -n '33p'
git show 44f76d456c1b326a71ffdb381590af825cbf11be:corpus/SOURCES.md | sed -n '839p' | awk -F'|' '{print $12}'
git cat-file -e 44f76d456c1b326a71ffdb381590af825cbf11be:corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md   # fatal: does not exist
git merge-base --is-ancestor 4b255745dea45a45d88b17e3c3fea4cdb6700cf7 44f76d456c1b326a71ffdb381590af825cbf11be && echo ancestor
# freeze-matrix (fixture in own scratch; rebuilds deterministically)
python3 -B .ufo/waves/round-79/w1/stage/RevFreeze/freeze-matrix.py --repo /fast/scratch/hyaku/kotodama-r79/RevFreeze/fixture-repo
```

## Residual risk and verification gaps

- A9/A10 (junk freeze, freeze rewrite) are not in-lane detectable by design;
  the mitigation is procedural (external pin in the round report + `# freeze:`
  receipt header). This is the honest ceiling, per QUALITY 25 limits.
- The freeze-shape probe is a reference, not the production counters; the matrix
  says nothing about accept-o/accept-ca until executors run them against it.
- The O-side observation grammar (mutable-revision refusal etc.) is owned by
  SentinelExec/MutRevision seats; the freeze matrix covers only commit-level
  ancestry, not in-ledger rev operands (R77's `HEAD` survivor class,
  `.ufo/waves/round-77/w2/MutCaLedger.md:43-84`, is a ledger-grammar gap, not a
  freeze-ancestry gap — the two must not be conflated in the draft's kill rules).
- Tools installed: none (python3/git only, system channels).
- Scratch `/fast/scratch/hyaku/kotodama-r79/RevFreeze/` removed after copying
  receipts into the stage directory.
