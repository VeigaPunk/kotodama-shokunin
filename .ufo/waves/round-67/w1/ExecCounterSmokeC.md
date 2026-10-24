# ExecCounterSmokeC — accept-c.py smoke (base clone + live lane + STAMP attacks)

Seat: L1-kotodama-r67.ExecCounterSmokeC (executor, frozen-instrument smoke). Read-only over the lane;
all writes confined to a throwaway clone under `.scratch/smoke-c` (gitignored, removed at end) and this report.
**Counter not modified** — `reports/round-67/accept-c.py` sha256 `3e5f1a5883c52ee41ce6c61aa536bc289d9b23abe5bafa48fcf744b5efaa97a5`
before and after (equal to the sha recorded in `reports/round-67/telemetry/dry-run-c.txt` and to `git show b78f8b8:reports/round-67/accept-c.py`).

Lane state at smoke: main = `b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21` (instruments commit), base/lands = `ad5b52b0ab5691358cd38718ab75649dc9916f9a`,
tree of base `de353b046be5e119c5203f0c5c82e92790c3e546`. Entry absent at base (`git cat-file -e` fatal);
the counter itself is also absent at base (added in `b78f8b8`), so a "clone at lands" run necessarily executes the
lane-tip counter file against the base tree — that is what `dry-run-c.txt` did too.

Command deviation: the ticket's `python3 -B ../reports/round-67/accept-c.py` resolves to
`/home/vgpnk/Projects/shokunin/reports/...` (outside the lane, does not exist). Used the claims.json form
`python3 -B reports/round-67/accept-c.py --root <root> --lands <40hex>` from the lane root instead.
Ticket's clone command was run verbatim; it does **not** materialize base (see §1).

## 1. Prescribed clone command as written → STAMP FAIL (clone main is the tip, not lands)

```
git clone --no-local --single-branch --branch main . .scratch/smoke-c     # clone main = b78f8b8e
python3 -B reports/round-67/accept-c.py --root .scratch/smoke-c --lands ad5b52b0ab5691358cd38718ab75649dc9916f9a
```
```
# counter sha256 (self): 3e5f1a5883c52ee41ce6c61aa536bc289d9b23abe5bafa48fcf744b5efaa97a5
# stamped revision: ad5b52b0ab5691358cd38718ab75649dc9916f9a
# evaluated revision: b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21
# measured revision (lane main): b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21
# tree: de353b046be5e119c5203f0c5c82e92790c3e546
# worktree dirty (tracked): False
STAMP FAIL stamped=ad5b52b0 evaluated=b78f8b8e equal=False tree=de353b04 dirty_tracked=False
ACCEPT-C-67: FAIL
EXIT=1
```
Before the wave lands, a plain `--branch main` clone of the lane has main = instruments tip, so the exact command in the
ticket cannot produce a base receipt. To materialize base the clone must be reset (`git -C .scratch/smoke-c reset --hard <lands>`);
that is what §2 does, and what the frozen `dry-run-c.txt` evidently assumed (its `.scratch/eval-base` predates the instruments commit).
**For L1: the lands-time eval procedure must state `reset --hard <lands>` (or clone then `checkout -B main <lands>`), not just `--branch main`.**
RevCounterC's F9 records the consequence for the frozen telemetry: `controls-c.txt:2` records the `--branch main` command while
`dry-run-c.txt` prints `evaluated revision: ad5b52b0…` (base) — the committed base receipt is **not reproducible from the command it records**.

## 2. Base-materialized clone, `--lands base` — FAILS on base bytes (matches frozen dry-run-c.txt)

```
git -C .scratch/smoke-c reset --hard ad5b52b0ab5691358cd38718ab75649dc9916f9a     # main == lands
python3 -B reports/round-67/accept-c.py --root .scratch/smoke-c --lands ad5b52b0ab5691358cd38718ab75649dc9916f9a
```
```
# counter sha256 (self): 3e5f1a5883c52ee41ce6c61aa536bc289d9b23abe5bafa48fcf744b5efaa97a5
# stamped revision: ad5b52b0ab5691358cd38718ab75649dc9916f9a
# evaluated revision: ad5b52b0ab5691358cd38718ab75649dc9916f9a
# measured revision (lane main): ad5b52b0ab5691358cd38718ab75649dc9916f9a
# tree: de353b046be5e119c5203f0c5c82e92790c3e546
# worktree dirty (tracked): False
STAMP PASS stamped=ad5b52b0 evaluated=ad5b52b0 equal=True tree=de353b04 dirty_tracked=False
FILE FAIL unreadable: [Errno 2] No such file or directory: '/home/vgpnk/Projects/shokunin/kotodama-shokunin/.scratch/smoke-c/corpus/knowledge/culture-material/medicine-healing-codes.md'
SET FAIL missing=['S805', ... 'S828'] non-unique=['S805', ... 'S828']
ROWS PASS bad=[] n=0
ONEID FAIL bad=['S805:citations=0', 'S806:citations=0', 'S807:citations=0', 'S808:citations=0', 'S809:citations=0', 'S810:citations=0']
RESTATE FAIL bad=['S805:bullets=0', 'S806:bullets=0', 'S807:bullets=0', 'S808:bullets=0']
HOSTS FAIL hosts=0
LINK PASS bad=[]
APPEND PASS missing_old=[] appended=0 extra=[] immutable_violations=[]
NOHARM PASS diff=[] allowed=['corpus/knowledge/culture-material/medicine-healing-codes.md']
SWEEP PASS exit=0 readme_sha256 f6e0cb87217b2be78d6a6be52d244c8c3486ec207e3f8e0fe0424d0ec23252ce
CAPTURE FAIL bad=['S805:absent', ... 'S812:absent']
TOPIC FAIL entry topic text appears verbatim in the README row
ACCEPT-C-67: FAIL
EXIT=1
```
(Full SET/ONEID/CAPTURE lists identical to `telemetry/dry-run-c.txt`: all 24 ids listed; only the FILE path string differs.)
Byte-for-byte the same verdict shape as the committed frozen dry run. Expected FAIL set confirmed:
**FILE, SET, ONEID, RESTATE, HOSTS, CAPTURE, TOPIC**. Vacuous/conditional PASS confirmed: **ROWS (n=0), LINK, APPEND, NOHARM, SWEEP**.
Two additions to the ticket's expected list: RESTATE also fails (bullets=0), and **STAMP PASS requires the clone reset described in §1**.

## 3. Live lane

* `--root . --lands ad5b52b0…` → `STAMP FAIL stamped=ad5b52b0 evaluated=b78f8b8e equal=False tree=de353b04 dirty_tracked=False`, `ACCEPT-C-67: FAIL`, exit 1.
  (Correct: the live worktree has moved past base.)
* `--root . --lands b78f8b8e…` (tip) → STAMP PASS, then FILE/SET/ONEID/RESTATE/HOSTS/CAPTURE/TOPIC FAIL, ROWS/LINK/APPEND/NOHARM/SWEEP PASS, `ACCEPT-C-67: FAIL`, exit 1.
  So the pre-data tip is also a do-nothing FAIL with STAMP satisfied — the predicate is not reachable by showing up.

## 4. STAMP vs wrong `--lands` (clone at base unless noted)

| lands passed | evaluated | STAMP | exit | note |
|---|---|---|---|---|
| `b78f8b8e…` (real commit ahead) | base | FAIL `equal=False tree=e5bf3a7e` | 1 | tree resolvable — pure equality rejection |
| `4589ebdd36659060a978d0bb5b41b8c4e275a549` (real older commit) | base | FAIL `equal=False tree=5f158e91` | 1 | ran while clone held the §8 fixture (dirty=True); STAMP still rejected on equality alone |
| `0000…0000` (40 hex, nonexistent) | base | FAIL `equal=False tree=00000000` | 1 | header prints literal `000…^{tree}` (cosmetic: unresolved rev-parse echo leaks into the `# tree:` line) |
| `4589ebd0…` (39 hex, typo) | — | FAIL `--lands is not a full commit hash` | 2 | no headers printed on this path |
| `deadbeef` | — | FAIL `--lands is not a full commit hash` | 2 | |
| omitted | — | argparse `error: the following arguments are required: --lands` | 2 | `--lands` genuinely required |

STAMP equality is sound: no wrong-lands case reached a data leg.

## 5. Unusable roots — no crash

`--root /tmp/r67smoke/notgit` and `--root /tmp/r67smoke/does-not-exist` both print
`# evaluated revision: unresolvable`, `# tree: unresolvable`, `STAMP FAIL stamped=ad5b52b0 evaluated= equal=False tree= dirty_tracked=False`,
`ACCEPT-C-67: FAIL`, exit 1. No traceback.

## 6. CRASH FOUND (RevCounterC F5): KeyError on a plausible intermediate draft

Fixture: base clone + **untracked** entry containing header, `- topic:`, and one bullet citing `(S805)`; registry untouched.
```
STAMP PASS stamped=ad5b52b0 evaluated=ad5b52b0 equal=True tree=de353b04 dirty_tracked=False
FILE PASS exists lines=5 h1=1 h2=0 h3=0 topic=True
SET FAIL missing=['S805', … 'S828'] non-unique=['S805', … 'S828']
ROWS PASS bad=[] n=0
ONEID FAIL bad=['S806:citations=0', … 'S811:citations=0']
COUNTER_FAULT infrastructure unusable: KeyError('S805')
ACCEPT-C-67: FAIL
EXIT=2
```
Cause: `RESTATE` does `row_line = reg_by_id[sid][0]` for every id that has a bullet (`accept-c.py:304`) with no
guard for ids absent from the registry; `main()`'s `except KeyError` converts it into `COUNTER_FAULT infrastructure unusable`.
Consequences: (a) a draft that cites an id before its registry row exists crashes instead of failing the leg; (b) legs after ONEID
(HOSTS…TOPIC) never run, so the receipt is truncated and mislabels a data condition as infrastructure; (c) exit 2, not 1.
Predicate still non-PASS, so this cannot manufacture a false PASS — but it will bite during draft integration if the entry and
registry rows land in different commits/order, and the "infrastructure unusable" wording is wrong for it.

## 7. FALSE-STAMP BYPASS (highest severity): ACCEPT-C-67 PASS with zero committed wave bytes

The counter reads ENTRY, `corpus/SOURCES.md` and `corpus/README.md` **from the worktree**, never `git show lands:<path>`;
`dirty_tracked` is only printed, never a leg; `--untracked-files=no` hides untracked files from that probe; and
`NOHARM` is `git diff --name-status BASE -- corpus/knowledge`, which does not show untracked additions.

Fixture (base clone, main still == lands `ad5b52b0`): untracked entry with 24 bullets; 24 synthetic registry rows appended to the
working-tree `corpus/SOURCES.md` (cells: fixture source URL `https://host{i}.example.org/article/S{id}` + `web.archive.org/web/20261024120000id_/…`,
kind paper, tier A, mined, opened 2026-10-24, used-by the entry, shared quote `"medicinal healing physician remedy codex"`, teaches
`Registry note describing clinic organization apprenticeship transmission practitioners`); one README index row plus the
section count 33→34, totals 240→241 and footer `30/29/33/29/24/95`→`30/29/34/29/24/95` in the working tree.

Output:
```
# counter sha256 (self): 3e5f1a5883c52ee41ce6c61aa536bc289d9b23abe5bafa48fcf744b5efaa97a5
# stamped revision: ad5b52b0ab5691358cd38718ab75649dc9916f9a
# evaluated revision: ad5b52b0ab5691358cd38718ab75649dc9916f9a
# measured revision (lane main): ad5b52b0ab5691358cd38718ab75649dc9916f9a
# tree: de353b046be5e119c5203f0c5c82e92790c3e546
# worktree dirty (tracked): True
STAMP PASS stamped=ad5b52b0 evaluated=ad5b52b0 equal=True tree=de353b04 dirty_tracked=True
FILE PASS exists lines=27 h1=1 h2=0 h3=0 topic=True
SET PASS missing=[] non-unique=[]
ROWS PASS bad=[] n=0
ONEID PASS bad=[]
RESTATE PASS bad=[]
HOSTS PASS hosts=24
LINK PASS bad=[]
APPEND PASS missing_old=[] appended=24 extra=[] immutable_violations=[]
NOHARM PASS diff=[] allowed=['corpus/knowledge/culture-material/medicine-healing-codes.md']
SWEEP PASS exit=0 readme_sha256 71e6dd8398a89796399cd3e6f11f0ba9d85e2b2181a7210ad69aec861fc2f780
CAPTURE PASS bad=[]
TOPIC PASS entry topic text appears verbatim in the README row
ACCEPT-C-67: PASS
EXIT=0
```
What was actually committed in that clone at the moment of PASS:
```
git -C .scratch/smoke-c rev-parse main                 -> ad5b52b0ab5691358cd38718ab75649dc9916f9a   (== lands)
git -C .scratch/smoke-c status --porcelain
 M corpus/README.md
 M corpus/SOURCES.md
?? corpus/knowledge/culture-material/medicine-healing-codes.md
git show main:corpus/SOURCES.md | sha256sum -> 8811130821ec57e3b03ede213c271fca0bfa35ecd5720a60fb1dbc50d37e266e   (== base blob)
git show main:corpus/README.md  | sha256sum -> f6e0cb87217b2be78d6a6be52d244c8c3486ec207e3f8e0fe0424d0ec23252ce   (== base blob)
git cat-file -e main:corpus/knowledge/culture-material/medicine-healing-codes.md -> absent
git show main:corpus/SOURCES.md | grep -c '^| S805 |' -> 0
```
The receipt headers of this PASS are **identical** to the honest FAIL in `telemetry/dry-run-c.txt` — same stamped, evaluated,
measured, tree `de353b04`, same counter sha — differing only in `dirty_tracked` and the verdict. After `reset --hard` + `clean -fd`
the same clone returns the §2 FAIL (STAMP PASS, FILE/SET fail, exit 1), proving the PASS came entirely from uncommitted bytes.
Caveat for severity: the forged rows share one quote and one teaches string, and all hosts are `.example.org`; RESTATE/HOSTS/LINK
do not detect repeated quotes or synthetic hosts, and nothing in C checks that `corpus/SOURCES.md`/`README.md`/ENTRY blobs equal the
lands tree. The bypass is therefore complete at the instrument level: `git rev-parse main == --lands` binds the branch name, not the bytes.

## 8. Other code-read observations (not separately exercised)

* **(F7)** `ROW_RE` accepts a row in any section, so SET/ROWS/APPEND ignore `## Registry` placement — the r66 E12 class is invisible to C (Ca owns it).
* **(F6)** Duplicate ids: `reg_by_id` keeps the **first** line, `tip_set`/`base_set` keep the **last**; a duplicated base row edited only in its last copy can evade APPEND's immutable-cell check while SET still reads the first. **Now measured by RevCounterC**: appending an identical copy of base row S100 passes APPEND with `appended=0` while the registry grows 724→725 lines — no leg pins line count or base-row uniqueness.
* **(F8 class, not defects on their own)** ONEID's `foreign` rule rejects any `(S###)` outside S805-S828, i.e. an entry cannot parenthetically cross-reference an older row (design choice, but it will surprise the entry author); whole-text ONEID counting, substring TOPIC matching, www-only host normalization and no cross-row quote freshness all read as intended-but-loose, not exploitable by themselves.
* **(F3)** `CAPTURE` accepts a capture whose timestamp is any 14 digits and does not require uniqueness across rows, **and has no no-capture branch**: the docstring/claims.json allow an explicit `no-capture` reason token in the source cell, but the code (`accept-c.py:403-417`) records `no_capture` unconditionally — RevCounterC measured a valid `(no-capture: paywalled, checked 2026-10-24)` cell failing `CAPTURE`.

## 9. Recommendations (for L1 decision — counter is frozen, not changed here)

1. Add a gating leg (or make STAMP fail) when `dirty_tracked` is true **and** include untracked files in that probe (`git status --porcelain -uall`), or read ENTRY/REGISTRY/README via `git show <lands>:<path>` so measured bytes are the stamped tree.
2. Extend NOHARM with `git status --porcelain -uall -- corpus/knowledge` (untracked additions) — otherwise an uncommitted entry is invisible.
3. Guard RESTATE's `reg_by_id[sid][0]` (missing row → leg FAIL, not `COUNTER_FAULT`/exit 2).
4. In the lands-time protocol, spell out clone-then-`reset --hard <lands>`; `git clone --branch main` alone is not base-materialization (§1).
5. If these are fixed before data, re-freeze and re-run `controls-c.txt`/`dry-run-c.txt` with the new sha (the "do-nothing control" rule already permits pre-data revision).

## 10. Cross-confirmation from RevCounterC (independent seat, same counter sha 3e5f1a58)

RevCounterC reproduced F1 three ways at tip `b78f8b8e` (untracked entry → STAMP PASS + FILE PASS with `dirty_tracked=False`;
`git checkout --detach ad5b52b0` with main still at tip → STAMP PASS while reading base bytes; dirty used-by/status edit → APPEND PASS)
and cites this seat's §7 as the completed all-legs form. Their measured additions, recorded here as reported (not re-run by me):

* **F2 — frozen-declaration mismatch (leg weaker than declared; no exploit needed).** APPEND `:369` pins cells 0-6 and 8, so cells
  7 (status), 9 (recheck) and 10 (used-by) may flip on **any** base row: S100 status→rejected with used-by→the new entry passes with
  `immutable_violations=[]`, contradicting claims.json's "the one declared in-place flip is S753's used-by cell". Precision note: the 24
  *new* rows' used-by **is** asserted by ROWS (`accept-c.py:272`, `ENTRY not in c[10]` → bad); what no leg bounds is which **base** rows
  may name ENTRY, how many may, or that mutable-cell churn stays inside the declared set. This is a leg-weaker-than-declared defect even
  if no seat exploits it, and it is independent of F1 — the §7 PASS required none of this looseness.
* **F1 — the exploit** (this seat's §7): uncommitted bytes satisfy every leg at `main == lands`.
* **F9 — protocol text**: `controls-c.txt:2` records `git clone --branch main` with no `reset --hard <lands>`/HEAD assert, so the control
  command is not the command that produced `dry-run-c.txt`; the same edit that fixes F1's worktree reads should carry the reset/HEAD assert.
* **F3**: CAPTURE has no no-capture branch (`:403-417`) — a valid `(no-capture: paywalled, checked 2026-10-24)` source cell → `CAPTURE FAIL S805:no_capture`,
  although docstring and claims.json both allow the token. (Logged in §8.)
* **F4, uncaught IndexError**: a degenerate row line `| S805 |` reaches `anchor_quote(c[5])` (`:306`) → traceback, no `ACCEPT-C-67:` line, rc=1;
  `main()`'s except tuple (`:441`) omits IndexError. Sibling of my §6 KeyError path (their F5).
* **F6, duplicate base row**: identical copy of S100 appended → `APPEND PASS appended=0`, registry 724→725 lines — tip line count is unpinned.
* **F7, ROW_RE is section-blind**: S805-S828 placed under `## Leads` passes C's whole predicate (base already holds 23 such rows); only
  Ca D2's external census catches the placement. Matches my §8 first bullet.

Combined verdict with RevCounterC: rev0 should not be frozen as-is. Blockers, by class: **F1** exploit — worktree-read legs + dirty/untracked
blind spot (§1/§7) allow `ACCEPT-C-67: PASS` from uncommitted bytes; **F2** declaration — APPEND `:369` permits base-row cells 7/9/10
flips the claim forbids; **F9** protocol — control command lacks `reset --hard <lands>`/HEAD assert, making `dry-run-c.txt` unreproducible
from its recorded command; **§6/§10** robustness — uncaught KeyError/IndexError turn data states into `COUNTER_FAULT`/traceback. All are
pre-data, not post-data, findings.

Reviewer disposition closed on the same sha (RevCounterC, `.ufo/waves/round-67/w1/RevCounterC.md`, F1-F9): **freeze blocker set = F1, F2, F9
plus the F4/F5 exception class**; F3/F6/F7/F8 are recorded defects for the post-freeze revision. This seat concurs and originates no
counter change (rev0 stays byte-identical for the L1's edit).

## 11. Joint satisfiability of C's APPEND vs Ca's D4 (L1 sequencing resolution)

CriticFrontier's alert is correct as a single-registry-state reading of the two frozen documents:
* C: `allowed_new = set(NEW_IDS) | EXTRA_IDS` (S805-S828 ∪ S801-S804) → any other appended id is `extra_ids`.
* Ca D4 (`accept-ca.py:219-236`): `rej_opened_today >= len(R66_REJECTS) + 2` = **6** with `R66_REJECTS = [S801..S804]` (`:68`), i.e. ≥2
  rejected rows opened 2026-10-24 beyond S801-S804 — ids S829+ would be `extra` for C. (`new_rejects` at `:232` is computed and unused,
  so the "beyond S801-S804" intent lives only in the threshold arithmetic.)

Measured here (base clone + one synthetic `S829` rejected row, opened 2026-10-24):
```
STAMP PASS stamped=ad5b52b0 evaluated=ad5b52b0 equal=True tree=de353b04 dirty_tracked=True
APPEND FAIL missing_old=[] appended=1 extra=['S829'] immutable_violations=[]
ACCEPT-C-67: FAIL   EXIT=1
```
So one shared lands commit cannot satisfy both predicates; CriticFrontier/RevWaveShape read the documents right.

**L1 resolution (in-session): no counter or claims revision; per-claim lands separation.**
`A_r` (S801-S804 + the r66 disposition repairs) lands before `A_c`; `A_c` appends only S805-S828 and carries C's receipt
(evaluated==stamped==A_c); `A_ca` follows with the S829+ reject rows and the round-67 lesson and carries Ca's receipt, where D4 sees
6 today-dated rejects. The joint predicate is satisfiable **as sequenced**, not at one shared tree.

Constraint this puts on the receipt protocol (for `check-receipt-seq.py --topo` and closure):
* C must never be re-derived at `A_ca` — the measured `extra=['S829']` above; Ca must never be stamped at `A_c`
  (`rejected_opened_today=4 < 6`).
* STAMP equality rejects a clone whose `main` moved past its lands, but §7's worktree-read legs mean the clone's **bytes** must also be
  at that lands: a clone reset to `A_c` while carrying `A_ca` content (or the converse) is not a valid receipt environment.

## Risks / blockers
* No blocker. `reports/round-67/accept-c.py` is byte-identical before/after (`3e5f1a58…`, also equal to `git show b78f8b8:`), main is `b78f8b8e…`,
  and `.scratch/smoke-c` was removed (only pre-existing `.scratch/eval-base` remains). At close the tracked worktree carried foreign in-flight
  modifications not made by this seat — observed: `reports/round-67/accept-ca.py` (L1's QUOTES `gate_ids` capture-group fix at `:272`) and
  `corpus/SOURCES.md` (wave row writes) — recorded so the integrity claim stays exact; neither affects any C evidence or the C counter's bytes.
  Untracked lane entries at close are the wave's own seat reports (`w1/`) plus `corpus/lessons/` scribe drafts; mine is only `ExecCounterSmokeC.md`.
* Items §1, §6, §7, §10 are instrument-level; none of them lets a *committed-data-free* run be mistaken for a legitimate lands receipt unless the reviewer ignores `dirty_tracked` — but the predicate itself ("every leg prints PASS") does exactly that, which is why §7 matters for the r66 D3 closure claim. RevCounterC concurs (F1/F2) that §7 and the uncaught-exception paths are pre-data blockers.
* No tool installs/upgrades were needed (none performed).

Report: /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-67/w1/ExecCounterSmokeC.md
