# CritDepth — round 69 / attempt 2 — residual verification of landed claim D2

Seat: `L1Kotodama69.CritDepth` (UFO-FSD critic). Target: **D2 (depth)** at lane tip
`9e82c7b` (data `e86ed3e`, counters `52b92a6`, declaration `6a98d7d`).
All lane work done in a private clone `/tmp/critdepth-r69` (`git clone -q`), plus read-only
counter invocations against the lane's absolute path. No lane file was written except this one.
No git-mutating command was run. No tool was installed this seat.

---

## 0. Verdict

**D2 content: FAIL.**

The frozen predicate is green — `python3 -B reports/round-69/accept-d.py --root .` prints
`ACCEPT-D-69: PASS legs=8/8` (exit 0) — and the 5 states / 5 rows / 5 non-empty cells /
S859-sourcing are all really present. But the word *depth* in the claim is glossed as
"verifiable technical detail a reader can act on from SKILL.md alone"
(`reports/round-69/accept-d.py:4-9`), and on that reading the table fails:

* its **settled-closed next action is under-specified and, read the way its own worked example
  writes it (successor-side), is rejected by the lane's own `--ledger` validator on 10 of the 12
  live closed chains** (exit 1);
* its **settled-active row shape names a precondition the classifier does not test**
  (a `used-by` naming a path that does not exist still reads SETTLED-ACTIVE, exit 0);
* its **front-matter claim "otherwise it is correction debt" is false**: a malformed successor
  emits no chain at all, and a malformed *target* crashes the classifier with a `KeyError`;
* **three of the five named error signatures cite code lines that cannot detect the condition**
  they name (`entry-not-repointed`, `retired-row-minted`-class, `closed-chain-kept`);
* the **counter does not adjudicate any of this**: a five-row filler table with junk cells,
  one duplicated token and a single existing path passes 8/8 (proof in §5.1), and the counter's
  own GREEN fixture cites `:112` and `:129` — both wrong lines — and still passes (proof in §5.2).

Every defect is *content*, one cell or one leg wide, inside the frozen 5-row shape: this is a
**fixable defect, not a tradeoff the canonical Rust judge must reject**. Nothing in the axis,
the surface or the 5-state framing has to be abandoned; §7 gives the smallest safe correction.
**§9 matters before reading this as final:** another seat repaired `SKILL.md` along the lines §7
proposes and committed it as `975e8f2` while this report was being written (G1-G8 settled;
residuals R1-R3). The verdict immediately below is the one for commit `9e82c7b`, the revision the
D2 receipts name.

Impacted axes: **depth (D2) directly**; **calibration** downstream, because the records assert
the claim as verified on the strength of this counter (`LOG.md:4227` "Claim D2 (depth) —
VERIFIED"; `SCORECARD.md:1332` "improved (claim D2, sourced)"), and the counter is satisfiable by
filler. Operability (O2) is not implicated: `accept-o.py` never runs `accept-d.py`.

---

## 1. Baseline measurements (all reproduced, exact tails)

```
$ python3 -B tools/check-supersession-settlement.py --root . --scan
...
SETTLEMENT: pending=0 chains=47 usedby_paths=711 missing_paths=0
EXIT=0

class counts: SETTLED-ACTIVE 30 · SETTLED-CLOSED 12 · SETTLED-RETIRED 4 · SETTLED-SPLIT 1
              PENDING 0 · settled-closed with a `mined` successor: 10 of 12

$ python3 -B tools/check-supersession-settlement.py --root . --ledger reports/round-68/dispositions/dedup-ledger.tsv
LEDGER: rows=82 findings=0
EXIT=0

$ python3 -B reports/round-69/accept-d.py --root .            # lane, cwd = lane
ACCEPT-D-69: PASS legs=8/8
EXIT=0

$ python3 -B reports/round-69/accept-d.py --selftest          # lane, cwd = lane
GREEN FIXTURE: PASS (legs 8/8)
DO-NOTHING FIXTURE: PASS (unexpected) (legs 8/8)
SELFTEST: 1/2
EXIT=1
```
(The last block reproduces in the clone too; `reports/round-69/telemetry/controls.txt` recorded
`DO-NOTHING FIXTURE: FAIL (as required) (legs 1/8)` / `SELFTEST: 2/2` pre-data. Cause and
consequence in §5.3 — independently confirmed with peer `RevRerun`, and here with a
stripped-tree probe that does FAIL, 5/8: the counter tests *presence*, not content.)

Note the live distribution: 30/12/4/1/0. **The `pending` row has no live instance** — four
states are exercised by real registry content, the fifth only by the fixture. That is an honest
scope note for "5 states", not a defect by itself.

---

## 2. Item 1 — can a writer act on the row's next action without reading code?

Tested one concrete live row per state; "without reading code" = using only SKILL.md:468-496,
the row's own cells, and the committed ledger.

| State | Concrete row | Can act from SKILL.md alone? | Evidence |
|---|---|---|---|
| pending | **none live** (pending=0) | **Untestable against real data.** And the action is mis-ordered even in principle: it says write a ledger row *then* apply it, but `--ledger` refuses `activate` on a successor not already `mined` (`:207-208`) and `retire` on a successor not already `rejected` (`:209-210`). Probe: queued successor + `activate` → `LEDGER-FINDING L1:S002:activate_but_status=queued`, EXIT=1. | `SKILL.md:483`; `tools/check-supersession-settlement.py:207-210` |
| settled-active | **S044>S034** (`dedup-ledger.tsv:7`, target row `:41`) | **Yes** — and the live row is genuinely settled: `corpus/knowledge/culture-material/hunting-foraging-subsistence.md` cites S044 at `:104,:116,:187` and no longer cites S034. But the table's shape phrase "naming a real corpus path" is not what the tool tests (§3, G1), so the writer has no way to know the tool would also accept a fabricated path. | `SKILL.md:484`; grep of the entry |
| settled-retired | **S070>S060** (`dedup-ledger.tsv:10`) | **Yes.** "keep the target, rule `retire`": ledger row `:10` exists, ruling `retire`, row rejected (`:209-210` satisfied); full ledger validates 82/0. | `SKILL.md:485` |
| settled-closed | **S570>S135** (the modal shape: successor `mined`, target `rejected`; 10 of 12 live closed chains look like this) and **S047>S029** (both rejected) | **No — under-specified, and the worked example points the wrong way.** The action says "keep the successor: rule `keep-reject`". On the genre of the cited example (`dedup-ledger.tsv:75`, S047: the line is written on the *successor's* id) this fails for S570: `LEDGER-FINDING L1:S570:keep_reject_but_status=mined`, EXIT=1. The same ruling written on the rejected *target* (S135) validates (findings=0), and so does `keep-successor` on the successor (`dedup-ledger.tsv:78`). Two spellings, three valid target/successor pairings for one state; the table names neither the id that takes the line nor the ruling the project actually recorded — and of its two cited precedents, `:88`'s S830 is not even a `--scan` chain (no `supersedes`), while `:78`, the one matching 10 of 12, is never cited. | `SKILL.md:486`; ledger `:75,:78` |
| settled-split | **S575>S420** (`dedup-ledger.tsv:83`) | **Yes.** Limiter present verbatim ("supersedes S420 for entry :41's cadet clause only"), both rows mined, ledger `keep-split` validates. Minor wording nit only: "narrow the scope … keep both rows and both scopes" reads as self-contradictory; the live pair already has two distinct scope cells (265 vs 254 chars, S575's narrower: "…not current fees or address"). | `SKILL.md:487`, `corpus/SOURCES.md:553` |

**Result: 2 of 5 rows are executable as written (retired, split); 1 is executable but for the
wrong reason (active); 2 are not (pending, closed).**

---

## 3. Item 2 — table vs `tools/check-supersession-settlement.py`

The five state *names* match `classify()` exactly (`:123-133`: closed, retired, active, split,
else pending), and the branch-order caution (`SKILL.md:489-491`) matches `:123` running first.
Four claims do not match:

**G1 — `settled-active` precondition is not what the code tests.** `SKILL.md:484` requires
"`used-by` naming a real corpus path". `classify()` only requires a non-`—` cell (`:127` via
`usedby_paths` `:103-108`); existence is computed separately (`:164`) and **does not gate**
(`:167` returns 1 on pending only). Probe:

```
registry: S001 queued; S002 mined, used-by corpus/nope.md, teaches "supersedes S001 — fix"
$ ... --scan
SETTLED-ACTIVE S002>S001 s=mined t=queued same_url=False used_by=1
SETTLEMENT: pending=0 chains=1 usedby_paths=1 missing_paths=1
EXIT=0
```
A chain with a fabricated `used-by` is certified settled. (The docstring makes the same false
claim at `:8-10`, "naming a real corpus path".)

**G2 — `settled-closed` row shape is not the code's predicate.** `SKILL.md:486` says the
successor "is live (`mined`, `used-by` intact)". `:123` fires on the target's status alone, so
the successor may be `queued`, `rejected` or missing-`used-by`. Probe: successor `queued`,
target `rejected`, no `used-by` →
`SETTLED-CLOSED S002>S001 s=queued t=rejected same_url=False used_by=0`, EXIT=0.
Live evidence: the table's *own* cited pair, "live pair S047>S029" (`SKILL.md:490`), is
`s=rejected t=rejected used_by=0`; and S132>S094 is the same shape. 2 of 12 live closed chains
therefore contradict the row shape the table gives for them.

**G3 — `settled-closed` next action is mis-keyed** (quantified in §2): valid for the 2
both-rejected chains, invalid for the other 10.

**G4 — `pending` action ordering is rejected by the tool's own ledger gate.** `SKILL.md:483`
"write a disposition-ledger row … then apply it" cannot be done for `activate`/`retire` before the
status change lands (`:207-210`); the recorded round-68 practice is the reverse (S044 is already
`mined` at `dedup-ledger.tsv:7`). Only `keep-split` (unconstrained) can be written rule-first.

**G5 — "otherwise it is correction debt" is false for a shape the code accepts.** `SKILL.md:472-473`
asserts every chain is one of the five states or debt. Two counterexamples:

```
(i) malformed successor (10 cells, teaches opens "supersedes S001 — fix")
    $ ... --scan
    SETTLEMENT: pending=0 chains=0 usedby_paths=1 missing_paths=0
    EXIT=0
    -> no chain line at all (`:85-87` marks malformed, `:117-118` skips, `order` is never
       appended at `:99`); neither a state nor debt, and the exit code says "settled".
(ii) malformed TARGET, well-formed successor
    $ ... --scan
    Traceback ... File "...py", line 121, in classify
        t_st = t_row["status"] if t_row else "missing"
    KeyError: 'status'
    EXIT=1
    -> a traceback, not a classification; exit 1 is indistinguishable from "pending", the
       very signal SKILL.md:524 tells the writer to trust.
```
No caution in the section covers malformed rows (`grep -n malformed SKILL.md` → `:290,:377,:726`,
none in 468-496). The lesson already records the parse-level half of this as R69-M4
(`corpus/lessons/round-69.md:30`); the table — the writer-facing surface D2 claims — does not.

**Error-signature column (SKILL.md:525-528):** only `scope-limiter-missing` is tool-derivable
(it lands in the pending fallback `:133`, and the table honestly says "the chain reads
`pending`"). The other three name conditions no committed code path detects, while still
carrying a code pointer:

* **G6** `entry-not-repointed` cites `:127`. `:127` is the settled-active branch; nothing anywhere
  compares entry text to a row id — the table's own caution says so (`:495-496`), yet the
  signature row still offers the line as its detection.
* **G7** `retired-row-mined` cites `:125`. `:125` *is* the retired branch, whose predicate is
  `s_st == "rejected"`; "a rejected correction still reads `mined`" is impossible for that row,
  and "still cited" is not read by the tool.
* **G8** `closed-chain-kept` cites `:123`. Deleting the successor row drops the chain entirely
  (`chains 47 -> 46`, exit 0, no line) and a "re-ruled" successor cannot change the state
  (branch order), so neither half of the signature is observable.

None of these tokens (`chain-left-pending`, `entry-not-repointed`, `retired-row-mined`,
`closed-chain-kept`, `scope-limiter-missing`) occurs in the tool's code or output; they exist only
in SKILL.md and in the counter's fixture strings (`grep -rn` over `--include=*.py` → 0 hits).

---

## 4. Item 3 — S859 provenance

```
$ git rev-parse 52b92a6:tools/check-supersession-settlement.py
1ef2e965204f53f40ffbabf45abea3fae9f029a6          # matches the row's "file blob"
classify   def at :112, body through :146          # row's ":112-146" accurate
selftest   def at :264, last statement ~:306       # row's ":264-311" accurate
$ python3 -B tools/check-supersession-settlement.py --selftest
SELFTEST: 7/7                                      # matches lessons/round-69.md:18
```
`S859` (`corpus/SOURCES.md:814`): kind `own-work`, tier `A`, status `mined`, opened 2026-10-24,
`used-by` = `SKILL.md, corpus/lessons/round-69.md` — **honest**: SKILL.md cites the row six
times (475, 479, 483-487) and the lesson quotes it. The cited line ranges are accurate. The
lesson's located quote (`"A chain is *settled* when exactly one state holds" —
tools/check-supersession-settlement.py:6`) is verbatim at `:6`.

**G9 — but the grounds the table points at state the taxonomy differently from the table.** The
same docstring says SETTLED-ACTIVE's target is "no longer `mined` (`queued` or `rejected`)"
(`:8-10`) — i.e. it claims a rejected target is *active*, contradicting the code's branch order
and the table's caution (`SKILL.md:489-491`). The docstring also promises a
`SETTLEMENT: pending=N keep=M stale_usedby=K` summary (`:26`) and a reported `STALE-USED-BY`
class (`:20-22`) that the code does not print (`:165` prints
`pending/chains/usedby_paths/missing_paths`). The table flags only the second of these docstring
defects (`:494-496`); it does not flag the first, so a writer who follows the citation
"re-derivable from committed bytes" gets two incompatible active-preconditions with no warning.
S859's `teaches` ("the five chain states are exhaustively classified") is also false in the G5
senses.

---

## 5. Item 4 — do the 8 legs adjudicate content?

Leg inventory (`reports/round-69/accept-d.py`): STAMP `:134`, SECTION `:139`, TABLE `:147-148`,
STATES `:152`, FIELDS `:157`, SIGNATURES `:158-164`, EVIDENCE `:166-175`, SOURCE `:177-189`.

| Leg | What it actually checks | Content? |
|---|---|---|
| STAMP | sha256 of the running file = file at `root/reports/round-69/` (under the canonical `--root .` these are the same file, so the leg is vacuous — already filed as R69-M10, `corpus/lessons/round-69.md:36`) | integrity only |
| SECTION | the heading string exists | heading text only |
| TABLE | header has 5 cells **and `len(rows) == 5`** | row count only |
| STATES | first column == the five names, in order | **the only content-bearing leg** |
| FIELDS | no empty cell, 5 cells per row | non-emptiness only |
| SIGNATURES | each row's 4th cell is a **substring of the Error-patterns section** | string duplication only; no signature need exist in code or output |
| EVIDENCE | at least one path token in the 5th cell `os.path.exists` (`:173`) | file existence only; **`:line` never resolved** |
| SOURCE | any S-id mentioned in the table has a `mined` registry row whose `used-by` mentions SKILL.md | satisfied 5× by S859 |

### 5.1 Five rows of filler pass — proof

Built the counter's own fixture root, then replaced every table row except the state names with
`filler | filler | TODO | S859 — tools/check-supersession-settlement.py:1` and put `TODO` into
`## Error patterns`:

```
LEG PASS STAMP ...                      LEG PASS SIGNATURES missing=none
LEG PASS SECTION ...                    LEG PASS EVIDENCE unresolved=none
LEG PASS TABLE header=5 rows=5          LEG PASS SOURCE mined_used_by_SKILL=['S859' x5]
LEG PASS STATES states=[...5 names...]  LEG PASS FIELDS empty=none short=none
FILLER TABLE: PASS
```
So the declared target "5 non-empty cells each, 5 error signatures linked into `## Error
patterns`" is satisfiable without a single true sentence about the taxonomy.

### 5.2 The GREEN control certifies wrong evidence pointers

The control fixture (`FIXTURE_TABLE`, `:40-52`) cites `:112` for pending (real pending branch
`:132`) and `:129` for retired (real `:125`). Replaying the fixture on the pre-data base
(`git show 793f7974:SKILL.md`, no table) with those exact pointers:

```
LEG PASS EVIDENCE unresolved=none
BASE+FIXTURE-TABLE (cites :112 and :129, both wrong): PASS     (exit would be 0)
```
The green control therefore never tested evidence resolution — it has always certified
existence-only pointers. (Independent cross-check, peer `RevRerun`: the same replay is green on
all 8 legs, `:112`/`:129`/`:130` all wrong.)

### 5.3 The DO-NOTHING control no longer reproduces post-data

`build_fixture_root` seeds the fixture from the **live** lane SKILL.md (`:196`), and
`with_table=False` injects nothing; post-data the "do-nothing" tree inherits the landed table.
Lane run today: `DO-NOTHING FIXTURE: PASS (unexpected) (legs 8/8)`, `SELFTEST: 1/2`, exit 1 —
against the committed pre-data receipt `FAIL (as required) (legs 1/8)`, `SELFTEST: 2/2`
(`reports/round-69/telemetry/controls.txt`). A genuinely stripped tree does fail (my probe:
`STRIPPED (table rows deleted): FAIL legs 5/8`; `RevRerun` reports 1/8 with the section removed),
so the counter still discriminates *presence*; only the control fixture is data-leaked and
non-re-runnable. This is the same instrument class the round already recorded as R69-M1
(`corpus/lessons/round-69.md:27`).

### 5.4 The 5-row freeze blocks the correction

`len(rows) == 5` (`:147-148`) is a hard gate. If the correction to G5 is a sixth state
(`malformed` / `dangling`), the counter turns red. The corrections in §7 are therefore written
to fit inside 5 rows; adding a state requires re-declaring the predicate in a later round.

---

## 6. Bounded content gaps

| # | file:line | Gap |
|---|---|---|
| G1 | `SKILL.md:484` | `settled-active` shape says "`used-by` naming a real corpus path"; the classifier tests only a non-`—` cell, and a nonexistent path still reads SETTLED-ACTIVE with exit 0 (`tools/check-supersession-settlement.py:127,:164,:167`). The instrument gap is already filed as **R69-M5** (`corpus/lessons/round-69.md:31`) and routed to round 70 (`LOG.md:4233`); what D2 adds is the table asserting, as the state's precondition, a check the filed gap says does not exist. |
| G2 | `SKILL.md:486` | `settled-closed` shape says the successor "is live (`mined`, `used-by` intact)"; `:123` fires on the target alone — `s=queued, t=rejected, used_by=0` reads CLOSED, and 2 of 12 live closed rows (S047, S132) have rejected successors, including the table's own "live pair" at `:490`. |
| G3 | `SKILL.md:486` | `settled-closed` mixes one precedent's action with another's ruling: "keep the successor" is `dedup-ledger.tsv:78`'s action, the ruling `keep-reject` is `:75`/`:88`'s, and the cell cites `:75`/`:88` but never `:78`. Both cited precedents are rows where the *ruled* row is `rejected` (S047, S830), so the ruling validates; the generalizing precedent for 10 of the 12 live closed chains is `:78` (`S570 | S135 | keep-successor`, ruled row `mined`). A reader following the cited precedent writes `keep-reject` against the successor and fails 10/12: `LEDGER-FINDING L1:S570:keep_reject_but_status=mined`, exit 1. Target-side `keep-reject` on S135 and successor-side `keep-successor` both give findings=0; the constraint asymmetry is `tools/check-supersession-settlement.py:207-212` (`activate`→`mined`; `retire`/`keep-reject`→`rejected`; `keep-successor`/`keep-split` unconstrained). Second-order: S830 carries no `supersedes` token, so `--scan` never emits it — the cited "kept-reject fingerprint" is not reproducible from the tool at all. |
| G4 | `SKILL.md:483` | `pending` action "write a disposition-ledger row …, then apply it" is rejected by `--ledger` for `activate`/`retire`, which require the post-settlement status (`tools/check-supersession-settlement.py:207-210`); probe `activate_but_status=queued`, exit 1. The recorded practice is data-first (`dedup-ledger.tsv:7`). |
| G5 | `SKILL.md:472-473,489-496` | "settled only when exactly one of the five states holds; otherwise it is correction debt" is false: a malformed successor yields no chain line (`:85-87,:117-118`, `order` never appended) and exit 0; a malformed target raises `KeyError` at `:121` with exit 1, indistinguishable from pending. No malformed caution exists in 468-496. The swallow is filed as **R69-M4** (`corpus/lessons/round-69.md:30`, routed `LOG.md:4233`); not covered there: the malformed-*target* `KeyError` and its exit-code collision with `pending`, and the table's exhaustiveness claim contradicted by the filed gap. |
| G6 | `SKILL.md:525` | `entry-not-repointed` cites `:127`, which is the settled-active branch; no committed path checks citation containment (the section's own caution `:495-496` says so). |
| G7 | `SKILL.md:526` | `retired-row-mined` cites `:125`, whose predicate is `s == rejected`; "still reads `mined`" cannot describe that row and "still cited" is unchecked. |
| G8 | `SKILL.md:527` | `closed-chain-kept` cites `:123`; a dropped successor removes the chain (`chains 47→46`, exit 0, silent) and a re-ruled successor cannot change the state, so neither half is detectable. |
| G9 | `SKILL.md:484` vs `tools/check-supersession-settlement.py:8-10` | The table's active precondition contradicts the docstring it cites via S859 (docstring: target "`queued` or `rejected`"); `:489-496` flags only the docstring's `STALE-USED-BY`/summary defect (`:20-26`), not this one. |
| G10 | `reports/round-69/accept-d.py:40-52,147-148,158-175,193-196` | Counter: SIGNATURES is substring duplication, EVIDENCE is existence-only (wrong `:line` passes; GREEN fixture proves it), TABLE freezes 5 rows, fixture seeds from the live SKILL.md so the do-nothing control passes post-data. Filler passes 8/8. |

**Already filed vs new.** The instrument halves of G1 and G5 are filed and routed, not discoveries
of this seat: R69-M5 (`corpus/lessons/round-69.md:31`) and R69-M4 (`:30`), both routed to round 70
(`LOG.md:4233`) — so C2/C4 are *documentation* fixes for D2's surface, not new instrument asks.
The new items here are table content (G2, G3, G4, G6-G8, G9's docstring contradiction), the
malformed-*target* `KeyError`/exit-code refinement to R69-M4, and G10 (the counter's four
content-blind legs and the leaked do-nothing control).

---

## 7. Smallest safe corrections (content-only, keeps 5 rows and every frozen leg green)

* **C1 `SKILL.md:486`** — first, name the id that takes the ledger line (the convention of
  `dedup-ledger.tsv:75,:78` is the successor's id); then give the subcase rulings and cite the
  matching precedent: successor `rejected` (S047>S029, `:75`) → `keep-reject`; target `rejected`
  with successor `mined` (S570>S135, `:78`; 9 more) → `keep-successor`. Add `:78` to the Evidence
  cell and drop the `:88` pointer (`S830` carries no `supersedes`, so `--scan` cannot produce it).
  Drop or mark as typical the "successor is live" clause.
  (Either the id rule or the subcase rulings alone is safe: the under-specification is what
  misfires, not the ruling name.)
* **C2 `SKILL.md:484`** — replace "naming a real corpus path" with "a non-`—` `used-by` cell;
  path existence is reported as `missing_paths` but is not gated (`:162-167`)".
* **C3 `SKILL.md:483`** — reverse the order: "apply the settlement, then record the ruling —
  `--ledger` requires `activate` on a row already `mined`, `retire` on one already `rejected`
  (`:207-210`)".
* **C4 `SKILL.md:489-496`** — add one caution: a successor row that is not exactly 11 cells
  emits no chain and `--scan` exits 0; a malformed target crashes at `:121`. This is the only way
  the section's "otherwise it is correction debt" becomes true inside the 5-row freeze.
* **C5 `SKILL.md:525-528`** — mark `entry-not-repointed` and `closed-chain-kept` as review work
  with no tool detection; rewrite `retired-row-mined` to what the state means (successor
  `rejected`, target cited) instead of an impossible "still reads `mined`".
* **C6 (next declaration, not this round's data)** — EVIDENCE must resolve the `:line` into the
  named branch; SIGNATURES must require a token the tool emits or an explicit "review-only"
  label; build the do-nothing fixture from the frozen base revision (`git show 793f7974:SKILL.md`)
  so the control re-runs after data; and record that `len(rows) == 5` forbids adding the state
  G5 implies.

---

## 8. What I did not do

* Did not run any mutating git/jj command, did not edit SKILL.md, the checker, the counter or the
  receipts. The lane write is this file only. (`SKILL.md` was repaired and committed by another
  seat as `975e8f2` after my measurements — see §9; not my change, not reverted by me.)
* Did not re-derive the round-68 counters or O2/Ca2; other seats own those.
* Did not fetch external sources; S859 is `own-work`.
* Live-registry observations are at `9e82c7b` in a clone; the lane run of `accept-d.py`
  (`--root .` and `--selftest`) was read-only and reproduced the clone's output exactly.

---

## 9. Addendum — the repair landed while this report was being written

After the measurements in §§1-5 were taken at commit `9e82c7b`, another seat edited the shared
worktree's `SKILL.md` (`16 insertions(+), 9 deletions(-)`) and then committed the whole wave,
including this file, as **`975e8f2`**. I did not make or revert any of it (my only write is this
report). Re-measured at `975e8f2`:

```
$ python3 -B reports/round-69/accept-d.py --root .          -> ACCEPT-D-69: PASS legs=8/8   EXIT=0
$ python3 -B reports/round-69/accept-d.py --selftest        -> SELFTEST: 1/2              EXIT=1
$ python3 -B tools/check-supersession-settlement.py --root . --scan
   SETTLEMENT: pending=0 chains=47 usedby_paths=711 missing_paths=0
```
Table rows keep their line numbers (`SKILL.md:483-487`); the new malformed-row caution is at
`:496-503`; the review-only note at `:500-502`; signatures at `:531-535`. Mapping onto my gaps:

| Gap | State at `975e8f2` | Line |
|---|---|---|
| G1 | fixed — "a non-`—` `used-by` cell (path existence is reported as `missing_paths`, not gated)" | `SKILL.md:484` |
| G2 | fixed — "the superseded **target** is `rejected`; the successor's own status is free … (10 of the 12 live closed chains)" | `SKILL.md:486` |
| G3 | fixed — subcase rulings with the right precedents (`keep-successor` for `mined`, ledger `:78`; `keep-reject` for `rejected`, `:75`), the id rule, `:211-212` | `SKILL.md:486` |
| G4 | fixed — "apply the cell change first … then record the ruling … the validator refuses `activate` while the row still reads `queued` (`:207-208`) and refuses `retire` / `keep-reject` unless the row reads `rejected` (`:209-212`)" | `SKILL.md:483` |
| G5 | fixed — new caution "A row that does not split into exactly 11 cells never reaches `classify()` …" | `SKILL.md:496-503` |
| G6-G8 | fixed — signatures now read "classification branch" / "review-only signature, no committed detector", plus "The five error signatures are review-only labels: no committed code path detects them" | `SKILL.md:500-502,531-535` |

Residuals at `975e8f2`:

* **R1 (was G3 second-order)** — the `settled-closed` Evidence cell still cites "kept-reject
  fingerprint S830 `:88`", and `S830` carries no `supersedes` token (`corpus/SOURCES.md:784`), so
  `--scan` never emits it. The pointer is ledger-only, not re-derivable from the tool the cell
  cites. (`SKILL.md:486`.)
* **R2 (was G9)** — `tools/check-supersession-settlement.py:8-10` still says ACTIVE's target is
  "`queued` or `rejected`". That clause is unreachable as written: `:123` tests `t_st == "rejected"`
  before `:127`, so a rejected target returns settled-closed and ACTIVE can only be `queued`; the
  `used-by` clause is truthiness only (`:122`). The table is now on the code's side, so the residual
  is a committed code-docstring defect, not a table defect; S859's `teaches` still quotes it.
* **R3 (was G10)** — the counter is untouched: `--root .` still prints `PASS legs=8/8` at
  `975e8f2` (re-run: 8/8, exit 0), a filler table still passes, the GREEN fixture still
  certifies wrong pointers, and `--selftest` is still `SELFTEST: 1/2` exit 1. No leg checks any
  cell's content.
* **Record integrity** — the committed D2 receipt (`reports/round-69/telemetry/final-measures-d.txt`)
  names `e86ed3e…` and its header tree `b3064e1f…` contains the pre-repair `SKILL.md` blob
  `a66a75f` (`git ls-tree b3064e1f SKILL.md`); the landed file is blob `2476a9c`. The STAMP leg
  hashes only the counter (and is vacuous under `--root .`, R69-M10). So the receipt's coverage of
  D2 is void against `975e8f2`: the 8/8 still reproduces, but it was not measured on this table.
  Re-taking the measure and re-stamping at the landed revision was the outstanding bookkeeping;
  since this was written it has been done: `final-measures-d-attempt2.txt` stamps `975e8f2`,
  tree `b154a919`, clean worktree, and `controls-attempt2.txt` records the present control state
  (GREEN 8/8, DO-NOTHING PASS (unexpected), `SELFTEST: 1/2` exit 1). The three counters were
  re-measured at the repair revision and committed as `3e59d1d`. Re-verified at tip `ef75509`:
  `--root .` 8/8 exit 0, and `:88` occurs exactly once (`SKILL.md:486`). R1-R3 remain content
  notes, not blockers.

**What the landed edit closes:** G1-G8 are prose-addressed (C2/C4 are documentation fixes over the
already-filed R69-M5/R69-M4, routed at `LOG.md:4233`; the round's own lesson now carries these as
R69-M10..M12, `corpus/lessons/round-69.md:36-38`); R1 closes only if the `:88` pointer is
dropped; R2 (code docstring) and R3 (counter legs + leaked control) remain open and are round-70
instrument work, not D2 prose.

**Verdict by revision.** D2 **FAIL** at `9e82c7b` (documented in §§0-7; the original receipt
names `e86ed3e`, the attempt-2 receipt names `975e8f2` tree `b154a919`). At `975e8f2` and its
records tip `3e59d1d` (re-verified at `ef75509`) the table is writer-actionable for all five
states except R1's non-reproducible `:88` pointer; R3 still means the depth axis has no
instrument that measures content, so the counter's 8/8 there is a presence check, not support for
the depth claim.
