# RevSeparability — round 65, attack seat: separability of C / O / Ca

Scope attacked: `reports/round-65/claims.json` separability block, `tools/check-claim-separability.py`
(schema `kotodama-separability-manifest-v1`), and the three frozen counters as read-sets.
Lane tip reviewed: detached HEAD `a0c7e50d5f75` (jj wc), base `17c32302c6845c8f164b985a8cb312d3181c8788`,
counters at their 01:55 bytes (`accept-c.py` rev2 19938 B, `accept-o.py` rev2 68904 B, `accept-ca.py` rev1 9038 B).
No tool installs were needed.

## Verdict in one line

Data-level separability holds for all three claims, but the separability block's *own* `check`
command has no artifact to run on, and three of the four dependencies the re-run will print are
**claim→claim or claim→base**, not the allowed claim→record class. A 0-finding manifest is not
reachable with the frozen instruments as allocated; the floor is 4 findings.

## The three questions, answered from the counters' read sets

**Does `accept-c.py` read any accept-o / accept-ca land? — No (data). Yes at program level.**
Rev2 read set: `corpus/knowledge/culture-material/games-play-sport-contests.md`, `corpus/SOURCES.md`
(+ base bytes via `git show BASE:`), `corpus/README.md`, `tools/check-cited-lines.py`,
`reports/round-28/readme/sweep.py`, `reports/round-61/reopen-quote.py` (sha-pinned to base), plus
`git diff BASE main` and six locator network reopens. None of those is an O or Ca land. But the
program it runs, `reports/round-65/accept-c.py`, **is** an O land (`claims.json` O.lands[1]) — so
`base+C.lands` cannot even start it (rc=2, the round-63 `C->REC` shape).
`accept-ca.py` likewise reads nothing of C or O; its program is O's land.

**Does `accept-o.py` read the games entry or the registry? — The entry: no open. The registry: no.**
It reads `tools/reopen-row.py`, `reports/round-65/telemetry/exactness-sweep-o65.txt` (`:1224-1237`),
`tools/check-row-fragments.py`; every registry it touches is written into scratch dirs
(`accept-o.py:522,594,...`). Two real couplings exist that the claims sentence omits:
1. it *spawns* `tools/check-row-fragments.py` with no `--rows`, whose default is
   `.ufo/waves/round-65/rows` (`tools/check-row-fragments.py:265`), and the tool walks that tree
   (`:99-108`) — i.e. O's verdict is computed over claim C's seat drafts;
2. its lands hardcode claim C's entry path (`tools/check-row-fragments.py:40`, `accept-c.py:75`).

**Does `accept-ca.py` read the fragment tool? — No.** Read set: its 8 declared lands,
`tools/check-gate-quotes.py` (base), `git rev-parse TRUE_REV^{tree}` + `git show BASE:REV63`, and —
undeclared — `LOG.md`, `SCORECARD.md`, `.ufo/waves/round-64/w2/LessonFinal.md`
(`accept-ca.py:74-76,113-115`, used by R1/R3/R5). `SPOTCHECK` (`accept-ca.py:77`) is a dead constant.

## Findings by severity

### HIGH-1 — the separability check has no manifest; the frozen `check` command exits 2
`claims.json` separability.check points at `reports/round-65/separability-manifest.json`; the file
does not exist (`ls` → ENOENT). The separator's last malformed control is literally
`manifest file absent` → exit 2 (`_load_manifest` → `InputError`). The block is therefore
unfalsifiable as written, and the phrase "the counters are record lands of this round" is
contradicted by `claims.json` itself, which puts all three counters in **O's claim lands**.

### HIGH-2 — O is not separable at all: FRAG requires exactly 26 files under an unclaimed directory
`accept-o.py` rev2, FRAG leg (01:55 bytes): it runs the tool with no `--rows` and now demands
`files == 26`:
```
scan_last = ...; m = re.search(r"in (\d+) file\(s\)", ...); files = int(...)
frag_ok = (st.returncode == 0 and sc.returncode == 0 and "0 finding" ... and files == 26)
```
The target directory is absent at base (`.ufo/waves/round-65/` is untracked; `git ls-tree 17c32302` has
no round-65 path), and the tool then exits 1 with a finding — measured:
```
$ cd /tmp/sep-probe && python3 -B <lane>/tools/check-row-fragments.py
FRAG: /tmp/sep-probe/.ufo/waves/round-65/rows:rows-dir: missing
FRAG: 1 finding(s) in 0 file(s)
exit=1
```
Consequence: every counterfactual run of O fails FRAG, and **no declared unit's lands can repair it**
(the rows are lands of no unit) → `SEPARABILITY_DEPENDENCY O-><base>`. In the lane it is worse than
a missing dir: the count is a function of *all seats'* draft `.txt` files. At 01:55 the lane scan
printed `0 finding(s) in 2 file(s)` while `find .ufo/waves/round-65/rows -name '*.txt'` listed **3**
(`ScoutRow02/rejects.txt`, `row-S752.txt`, `row-S753.txt`) — the directory is being written under
the counter's feet, `rejects.txt` counts toward the 26, and a second seat's copy of the same row id
turns the count into 27+. O's verdict is owned by C's draft hygiene, not by O.

### HIGH-3 — `NOHARM` compares base to the `main` ref, and `main` is still at base
`accept-c.py:387` runs `git diff --name-only BASE main -- corpus/knowledge`. Measured in the lane:
`git rev-parse main` = `17c32302…` (== base), HEAD detached (`a0c7e50d5f75`, jj wc), and in a
`git clone --shared --no-checkout` + `checkout --detach BASE` exactly as `_git_counterfactual`
builds it, `main` exists but the diff is empty. So NOHARM fails post-integration unless the L1
advances the git ref `main` to the integrated commit; and in the separator's clone NOHARM reads
*lane refs*, never the overlay — the leg cannot be repaired by any unit's lands. This blocks claim
C's predicate independently of separability, and it also means `base+C.lands` fails for two
independent reasons (missing program **and** empty diff).

### MED-1 — Ca's lands are incomplete: its acceptance reads three undeclared corrected files
R1 needs `"Correction (round 65, R1)"` in `LOG.md`, `SCORECARD.md`,
`.ufo/waves/round-64/w2/LessonFinal.md`; R3 needs LOG + SCORECARD; R5 needs `LOG.md`. None of the
three is in `claims.json` Ca.lands. On `base+Ca.lands` the repeats are uncorrected and no unit lands
those files → `SEPARABILITY_DEPENDENCY Ca-><base>`. Fix: add the three paths to Ca.lands (they are
Ca's own work per the Ca statement) before the manifest is written.

### MED-2 — structural static dependency O→C, proven on the real bytes
`_static_findings` flags a claim whose added lines name a sibling land path absent at base. The
fragment tool is O's land and its line 40 is `ENTRY = "corpus/knowledge/culture-material/games-play-sport-contests.md"`;
`accept-c.py:75` (also O's land) repeats it. Probe against the *real* tool bytes in a synthetic
two-unit lane:
```
$ python3 -B tools/check-claim-separability.py /tmp/probe/m.json --lane /tmp/probe/lane
SEPARABILITY_DEPENDENCY O->C via land path 'corpus/knowledge/culture-material/games-play-sport-contests.md' named at tools/check-row-fragments.py:40
SEPARABILITY: 1 findings
```
This is a claim→claim dependency created by the row-format instrument (it must know the entry path
to check `used-by`). It cannot be removed by manifest allocation; only by parameterizing `ENTRY`
out of every O land (and out of `accept-c.py`, which is also O's), or by moving `accept-c.py` to C.

### MED-3 — "record lands" is the wrong label for this allocation
`claims.json`: "the counters are record lands of this round, a record dependency only". But O.lands
holds `accept-c.py` and `accept-ca.py`, and O is a *claim* unit (it carries `acceptance`); the
separator will therefore print **C→O** and **Ca→O** — claim→claim, which the round-63 precedent
(`reports/round-63/telemetry/rev-separability.txt`, `C->REC`) does not cover. Declaring a
`role:"record"` unit for the counters instead is refused if it carries acceptance
(`_parse_manifest`: "records carry no acceptance"), so the counters would have to be split from the
programs that run them, and `accept-o.py`'s docstring naming `reports/round-65/accept-c.py` /
`accept-ca.py` (`:8,:12`) would then add a *static* O→REC hit on top. Net: relabelling makes the
receipt worse (5 findings), not better.

### MED-4 — default `--timeout 600` is below one O acceptance run; a timeout is scored as FAIL
`DEFAULT_TIMEOUT = 600.0`; `_run_acceptance` returns `(False, "timeout after %gs")` on
`TimeoutExpired`, and the selftest pins that as a negative control ("an acceptance run that times out
is a failure"). O's FULL leg alone measured `wall=426.3s` at base (`telemetry/dry-run-o.txt`) and
re-executes the battery in a subprocess with an inner 1800 s budget, on top of MUT (10 mutants),
DEFAULT (wall 150 s) and DRIP. One O run is structurally > 600 s → the separator would record a
false dependency. The re-run must pass `--timeout 2400` (see design below).

### LOW-1 — the O "base dry-run" receipt is a worktree run and is stale against rev2
`telemetry/dry-run-o.txt` is headed "base dry-run … at base 17c32302" but was executed at the lane
root; its `FRAG PASS … 0 finding(s) in 0 file(s)` is only possible because the untracked
`.ufo/waves/round-65/rows` existed (empty) in the worktree. At base bytes the tool exits 1
(HIGH-2 experiment), and under rev2 the same run prints `files=0/26` → FAIL. The receipt therefore
cannot be cited as the FRAG leg's base behaviour for the counter it now describes.

### LOW-2 — `controls-ca.txt` is absent
`claims.json` controls: "controls-c …, controls-o.txt, controls-ca.txt land before any data seat".
`reports/round-65/telemetry/` holds `controls-c.txt` (01:29) and `controls-o.txt` (01:53); there is
no `controls-ca.txt`. Ca rev1 is unforced, so the re-run's precondition (counter met its prior form
and failed the round-65 form) is unmet for Ca. (Recorded as a dependency, not adjudicated here.)

### LOW-3 — receipt noise
`accept-c.py` still emits `SyntaxWarning: "\w" is an invalid escape sequence` (docstring near :99) in
every receipt, including `controls-c.txt`; `accept-ca.py:77` keeps an unused `SPOTCHECK` constant.
Cosmetic; worth one line of cleanup before the final receipt.

## Re-run design (post-integration)

Write the manifest at `reports/round-65/separability-manifest.json`, generated *after* integration so
`WORKTREE` bytes are final. Acceptance argvs must stay **relative** (as in `claims.json`):
`accept-o.py`'s FULL leg re-executes `os.path.abspath(__file__)` (`:1136`; MUT `:1095`, MUTEX `:1198`); with an absolute argv it
would re-execute the *lane* copy against the counterfactual root and mix bytes.

```json
{
  "schema": "kotodama-separability-manifest-v1",
  "base": "17c32302c6845c8f164b985a8cb312d3181c8788",
  "claims": [
    {"id": "C", "tree": "WORKTREE",
     "lands": ["corpus/knowledge/culture-material/games-play-sport-contests.md",
               "corpus/SOURCES.md", "corpus/README.md"],
     "exports": [],
     "acceptance": ["python3", "-B", "reports/round-65/accept-c.py", "--root", "."],
     "needs_git": true},
    {"id": "O", "tree": "WORKTREE",
     "lands": ["reports/round-65/accept-c.py", "reports/round-65/accept-ca.py",
               "reports/round-65/accept-o.py", "tools/check-row-fragments.py",
               "reports/round-65/telemetry/exactness-sweep-o65.txt"],
     "exports": [],
     "acceptance": ["python3", "-B", "reports/round-65/accept-o.py", "--root", "."]},
    {"id": "Ca", "tree": "WORKTREE",
     "lands": ["reports/round-64/telemetry/final-measures-ca.txt",
               "reports/round-63/telemetry/revisions.txt",
               "reports/round-64/claims.json",
               "reports/round-64/telemetry/control-o.txt",
               "corpus/lessons/round-64.md",
               "corpus/knowledge/linguistics/language-socialization-and-acquisition.md",
               "corpus/QUALITY.md", "corpus/lessons/round-65.md",
               "LOG.md", "SCORECARD.md", ".ufo/waves/round-64/w2/LessonFinal.md"],
     "exports": [],
     "acceptance": ["python3", "-B", "reports/round-65/accept-ca.py", "--root", "."],
     "needs_git": true},
    {"id": "ROWS", "role": "record", "tree": "WORKTREE",
     "lands": [".ufo/waves/round-65/rows/row-S750.txt", "… row-S775.txt (exactly the 26 row-*.txt)"],
     "exports": []}
  ]
}
```
(`O` keeps `needs_git` false: no O leg runs git, and the git-free materialization is what exposes the
rows-dir dependency honestly. `ROWS` is the only way to get O repaired at all — the row fragments
must exist in the overlay for `files==26`.)

Command and budget:
```
python3 -B tools/check-claim-separability.py reports/round-65/separability-manifest.json --timeout 2400
```
4 units → up to 12 acceptance runs (1 + 3 per failing unit); O's runs dominate (~400-700 s each) →
budget 45-70 min wall. Run it once, capture stdout+stderr to
`reports/round-65/telemetry/separability-rerun.txt`, and cite `SEPARABILITY_NOTE units=4
ordered_pairs=12 acceptance_runs=N` in the receipt.

Preconditions the L1 must satisfy before the run (each is a finding above if skipped):
1. `git rev-parse main` == the integrated commit (jj `bookmark set main`), else C's NOHARM fails (HIGH-3).
2. `find .ufo/waves/round-65/rows -name '*.txt' | wc -l` == 26 **and no `rejects.txt`**; the count is
   part of O's verdict (HIGH-2).
3. Ca.lands extended with `LOG.md`, `SCORECARD.md`, `.ufo/waves/round-64/w2/LessonFinal.md` (MED-1).
4. `controls-ca.txt` present (LOW-2); counters frozen at their final revision and their sha pinned in
   the receipt (O and C are already rev2).
5. No seat is writing `.ufo/waves/round-65/rows/` during the run (the count flips mid-run otherwise).

Expected output with this manifest (all four are the design's floor, not surprises):
```
SEPARABILITY_DEPENDENCY O->C via land path 'corpus/knowledge/culture-material/games-play-sport-contests.md' named at tools/check-row-fragments.py:40
SEPARABILITY_DEPENDENCY O->ROWS via acceptance ...fails on base+O.lands (FRAG files=0/26, rows-dir missing) and passes on base+O.lands+ROWS.lands
SEPARABILITY_DEPENDENCY C->O via acceptance ...fails on base+C.lands (rc=2, can't open reports/round-65/accept-c.py) and passes on base+C.lands+O.lands
SEPARABILITY_DEPENDENCY Ca->O via acceptance ...fails on base+Ca.lands (rc=2, can't open reports/round-65/accept-ca.py) and passes on base+Ca.lands+O.lands
SEPARABILITY: 4 findings
```
Every one must be adjudicated as the disclosed instrument class, not as a claim defect — but note the
class here is **claim→claim / claim→base**, so the round-63 record-dependency allowance does not
cover them as written. To reach the allowed class, the durable fix is Option B, filed as a lands
correction with a receipt:
- B: move `reports/round-65/accept-c.py` into C.lands and `reports/round-65/accept-ca.py` into
  Ca.lands (each claim lands its own counter), leaving O = tool + sweep receipt. That removes the two
  acceptance findings and leaves 2 (O→C static, O→ROWS) — all instrument-class, no overlap
  (`_overlap_findings` stays empty because no path is landed twice).
- C (zero findings, next round): parameterize `ENTRY` out of every O land (accept-c.py included) and
  scope FRAG's `files==26` count to a fixture set O lands, moving the real-draft scan to a wave-local
  convenience. Both are counter revisions; both need their own forcing control. Not this round.

## Residual risk

- Network determinism: O's LIVE-adjacent legs (`DEFAULT` 150 s, `DRIP`, MUT, MUTEX) and C's six
  locator reopens make verdicts time- and network-dependent; MUTEX compares regenerated rows to the
  committed `exactness-sweep-o65.txt` byte-for-byte.
- `needs_git` units read lane refs, not overlays: NOHARM (C) is insensitive to the separator's
  counterfactual — it validates the integrated commit, so the re-run cannot detect a bad C overlay
  through that leg.
- jj worktree churn: the lane is a jj wc with a detached git HEAD; any `main`-ref movement by a
  parallel seat changes C's NOHARM between runs.
- Row-draft churn during the run (observation at 01:55: tool saw 2 `.txt`, `find` saw 3).

## Verification gaps (what I ran and what I did not)

Ran: `check-claim-separability.py --selftest` → 56/56 pass (2.6 s); a synthetic two-unit lane with
the real `check-row-fragments.py` bytes → the O→C static finding above; the missing-rows-dir probe →
exit 1, 1 finding; the lane FRAG scan at 01:55 → 0 findings/2 files; a `--shared --no-checkout` clone
at base → `main` present, `git diff BASE main` empty.
Did not run: a full separator evaluation (needs the integrated lands; O ≥ 400 s/run, ~12 runs) and
any accept-o end-to-end run. Those are the L1's post-integration step, with the preconditions above.
