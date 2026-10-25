# Exec1 — round-69 w1 — claim D2 (depth): drafted `### Registry correction chains` for SKILL.md

Axes (godspeed): **depth** (judged — every cell derived from `classify()` and the
round-68 ledger, then attacked against the frozen counter), **attack** (controls
re-run, doc-vs-code gaps hunted in the committed instruments), **speed** (one
batched validation pass; leaf bound respected — no subagents dispatched).

Everything below was produced read-only: no production byte was edited, no git/jj
mutation, scratch only under `/tmp`. The draft is handed to the L1 for landing.

## 1. Commands run (absolute paths, real output)

### 1.1 Live registry scan (read-only)

```
$ python3 -B tools/check-supersession-settlement.py --scan --root /home/vgpnk/Projects/shokunin/kotodama-shokunin
SETTLED-ACTIVE S044>S034 s=mined t=queued same_url=True used_by=1
... (47 chain lines total)
SETTLED-SPLIT S575>S420 s=mined t=mined same_url=False used_by=1
SETTLEMENT: pending=0 chains=47 usedby_paths=709 missing_paths=0
exit=0
```

Census of the 47 lines: 30 `SETTLED-ACTIVE`, 4 `SETTLED-RETIRED`
(S070>S060, S125>S095, S186>S157, S490>S379), 12 `SETTLED-CLOSED`
(S047>S029, S132>S094, S185>S145, S570>S135, S571>S141, S572>S147, S573>S151,
S574>S159, S648>S602, S649>S616, S650>S623, S651>S643), 1 `SETTLED-SPLIT`
(S575>S420), `pending=0`.

### 1.2 Tool selftest (green + do-nothing pre-data controls)

```
$ python3 -B tools/check-supersession-settlement.py --selftest
PASS pending-detected / settled-active / settled-retired-closed / settled-split
PASS ledger-clean / ledger-inconsistent-rejected / unreadable-exit-2
SELFTEST: 7/7   exit=0
```

### 1.3 Ledger ruling locations

```
$ grep -n -E "keep-reject|keep-split" reports/round-68/dispositions/dedup-ledger.tsv
75:S047 | S029 | — | keep-reject | none | corpus/SOURCES.md | settled-closed at base ...
76:S132 | S094 | — | keep-reject | none | ... settled-retired at base ...
83:S575 | S420 | — | keep-split | none | ... both rows mined, S575 teaches carries the for-entry-only limiter re-sourcing heraldry line 41
88:S830 | S252 | — | keep-reject | none | kept reject at base ...
$ wc -l reports/round-68/dispositions/dedup-ledger.tsv   -> 88  (82 ruling rows + 6 header lines)
$ grep -n "^S034 | S044" ...  -> 41  (target-side keep-successor + deactivate)
$ grep -n "^S044 | S034" ...  -> 7   (activate | repoint)
$ grep -n "^S186 | S157" ...  -> 19  (retire | cell-flip)
$ grep -n "^S490 | S379" ...  -> 30  (retire | none; FORCED BY FROZEN SET)
```

Round-68 ruling record: `LOG.md:4214` ("All 34 pending chains closed (31
activate-class incl. S126 already-mined, 4 retire incl. S490)"); forced-retire
mistake entry `corpus/lessons/round-68.md:92` (R68-M2); unreachable-EXEC
fixture `corpus/lessons/round-68.md:91` (R68-M1).

### 1.4 S575 scope limiter, verbatim from the live row (`corpus/SOURCES.md:553`)

```
teaches: supersedes S420 for entry :41's cadet clause only — Scottish arms
usually descend to the eldest son, while a younger son may only petition ...
status: mined    usedby: corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md
```

Matches `SPLIT_RE` (`tools/check-supersession-settlement.py:54`):
`for\s+(entry|line|row|cell|clause)\b.{0,40}\bonly\b` — "for entry" + 20 chars
+ "only". The selftest fixture FIX4 (`:252`) mirrors it.

## 2. Derivation line map — `tools/check-supersession-settlement.py`, `classify()` (`:112-145`)

| State | Branch | Assignment | Live instance |
|---|---|---|---|
| settled-closed | `:123` (`if t_st == "rejected"`) | `:124` | S047>S029 (both rejected — see Finding F3) |
| settled-retired | `:125` (`elif s_st == "rejected"`) | `:126` | S490>S379 (ledger `:30`, R68-M2) |
| settled-active | `:127` (`elif s_st == "mined" and s_used and t_st == "queued"`) | `:128` | S044>S034 (ledger `:7` activate + `:41` keep-successor/deactivate) |
| settled-split | `:129-130` (`elif ... and SPLIT_RE.search(teaches)`) | `:131` | S575>S420 (ledger `:83`) |
| pending | `:132` (`else`) | `:133` | none live; 34 ruled at round 68 (`LOG.md:4214`) |

Supporting lines: docstring state list `:8-17`, "pending = correction debt"
`:19-20`, `SPLIT_RE` `:54`, `RULINGS` `:55`, `usedby_paths` `:103-109`,
`same_url` recorded `:136`, scan gate `return 1 if pending else 0` `:167`,
existence-only used-by comment `:162-164`.

## 3. THE DRAFT (verbatim; hand to L1 — do not edit here)

Insertion anchors against current SKILL.md (734 lines at base):
**(a)** insert the whole section below immediately **before** the line
`## Error patterns` (i.e. after line 466), as the last `###` subsection of
`## Decision table`. **(b)** append the five signature rows to the **first**
`## Error patterns` table, directly after the row ending
`(\`naming-collision-gate.md:54\`) |` (current line 493).
The five error-signature names deliberately reuse the frozen green control's
names (`reports/round-69/accept-d.py` `FIXTURE_TABLE`/`FIXTURE_SIGNATURES`),
so landed data and the pre-data control stay one vocabulary.

### 3(a) New subsection (exact bytes)

```markdown
### Registry correction chains

The registry's correction mechanism is append-only: a defective row keeps its
cells, and the new row whose `teaches` opens `supersedes S### —` carries the
fix. Every opened chain sits in exactly one of five states, decided by
`classify()`; four are settled, one is debt. Executable authority
`tools/check-supersession-settlement.py` (`--scan`: one line per chain plus
`SETTLEMENT: pending=N …`, exit 1 while any chain is pending, `:167`;
`--ledger F` validates a disposition TSV against live statuses; `--selftest`
7/7). Disposition authority `reports/round-68/dispositions/dedup-ledger.tsv`
(82 ruling rows; header `:1-6`); round-68 ruling record `LOG.md:4214`. The
table is opened as registry row S859 (own-work, tier A).

| State | Row shape | Writer's next action | Error signature | Evidence |
|---|---|---|---|---|
| pending | successor opened (`supersedes S### —` in its teaches), neither side `rejected`, and no settled shape holds — e.g. successor `queued`, or `mined` with no `used-by`, or both `mined` without the limiter | rule the chain: write a disposition-ledger row (ruling `activate` / `retire` / `keep-split`), then apply it — repoint + deactivate, reject the successor, or write the limiter | chain-left-pending | S859 — tools/check-supersession-settlement.py:132 (scan gate `:167`); the 34 chains ruled at settlement: reports/round-68/dispositions/dedup-ledger.tsv:1-6; LOG.md:4214 |
| settled-active | successor `mined` with `used-by` naming a real corpus path; target `queued` (deactivated: `used-by` cell reads `—`) | repoint the entries: inline citations move to the successor's id; the target's deactivation lands in the same settlement, not before (ledger mechanisms `repoint`, then `deactivate`) | entry-not-repointed | S859 — tools/check-supersession-settlement.py:127; ruling S044>S034 `activate` reports/round-68/dispositions/dedup-ledger.tsv:7, target row `:41` |
| settled-retired | successor `rejected` — the correction was audited and refused; the target keeps its own status and `used-by` (typically still `mined`) | keep the target: record the refusal (ruling `retire`); if a mutation already touched target cells, flip them back (`cell-flip`, S186); when the frozen ruling vocabulary lacks a target-retained class, note the true disposition in the ledger | retired-row-mined | S859 — tools/check-supersession-settlement.py:125; `cell-flip` S186>S157 reports/round-68/dispositions/dedup-ledger.tsv:19; forced retire S490>S379 `:30` (R68-M2, corpus/lessons/round-68.md:92) |
| settled-closed | the superseded target itself is `rejected` — the keep-successor fingerprint: the chain resolved earlier and the successor is live (`mined`, `used-by` intact) | keep the successor: rule `keep-reject` from the registry bytes alone; nothing flips | closed-chain-kept | S859 — tools/check-supersession-settlement.py:123; S047>S029 `keep-reject` reports/round-68/dispositions/dedup-ledger.tsv:75; kept-reject fingerprint S830 `:88` |
| settled-split | both rows `mined`, successor has `used-by`, and its teaches carries the limiter `for entry/line/row/cell/clause … only` (regex window 40 chars, `:54`) | narrow the scope: the supersession covers only the named slice; keep both rows and both scopes (ruling `keep-split`) | scope-limiter-missing | S859 — tools/check-supersession-settlement.py:129; S575>S420 `keep-split` reports/round-68/dispositions/dedup-ledger.tsv:83, live row corpus/SOURCES.md:553 |

Cautions that are part of the rule: branch order decides overlaps — the
closed test runs first, so a pair with **both** rows `rejected` reads
settled-closed, never settled-retired (`:123-131`; live pair S047>S029).
`same_url` is diagnostic only: `classify()` records it (`:136`) and no state
depends on it. An existing `used-by` path is not a reading `used-by`: the
scan checks path existence only (`:162-164`); whether the entry actually
contains the row id is review work — the docstring's `STALE-USED-BY` class
(`:21-22`) names a containment check no committed code path implements.
```

### 3(b) Five rows appended to the first `## Error patterns` table (exact bytes)

```markdown
| chain-left-pending | an opened `supersedes` chain with no settled shape is correction debt: rule it in the disposition ledger, then apply the ruling — `--scan` exits 1 while any chain is pending (`tools/check-supersession-settlement.py:167`) |
| entry-not-repointed | the successor is `mined` but the entry still cites the deactivated target — repoint citations to the successor before the target's deactivation lands (`tools/check-supersession-settlement.py:127`) |
| retired-row-mined | a rejected correction still reads `mined` or is still cited — the audit refused it; the target keeps its status and citations (`tools/check-supersession-settlement.py:125`) |
| closed-chain-kept | the closed chain's live successor was dropped or re-ruled — the target's `rejected` is the keep-successor fingerprint; the successor stays `mined` (`tools/check-supersession-settlement.py:123`) |
| scope-limiter-missing | both rows are `mined` without the `for entry/line/row/cell/clause … only` limiter — the chain reads `pending`, not split; write the named slice into the successor's teaches (`tools/check-supersession-settlement.py:129`) |
```

### 3(c) Companion data the L1 must land for leg SOURCE (not part of SKILL.md)

The SOURCE leg requires the S-id cited in the table to exist in
`corpus/SOURCES.md` with 11 cells, `status=mined`, and `used-by` containing
`SKILL.md` (`accept-d.py:177-189`). S859 is not landed at base — expected
pre-data. Suggested row shape (validated in §4; L1 owns the landed wording and
the `corpus/lessons/round-69.md` `## Gate` quote per claims.json `D2.sourced`):
11 cells, `own-work`, tier A, `mined`, `used-by` = `SKILL.md`, teaching the
five-state taxonomy of `classify()`.

## 4. Validation of the draft against the frozen counter (scratch only)

Script `/tmp/r69d-draft-validate.py` (committed to nothing): builds two
fixture trees in `/tmp` from the real lane bytes — `green` = real SKILL.md +
the §3 draft inserted at the §3 anchors + S859 row appended to a copy of
`corpus/SOURCES.md`; `bare` = same but no draft — copies
`tools/check-supersession-settlement.py`, `reports/round-69/accept-d.py`, the
dedup ledger and `LOG.md` into each, then runs the counter from inside each
tree.

```
$ python3 -B /tmp/r69d-draft-validate.py
$ python3 -B reports/round-69/accept-d.py --root /tmp/r69d-fx-green
LEG PASS STAMP self=06b0352a0288 committed=06b0352a0288
LEG PASS SECTION heading=### Registry correction chains
LEG PASS TABLE header=5 rows=5
LEG PASS STATES states=['pending', 'settled-active', 'settled-retired', 'settled-closed', 'settled-split']
LEG PASS FIELDS empty=none short=none
LEG PASS SIGNATURES missing=none
LEG PASS EVIDENCE unresolved=none
LEG PASS SOURCE mined_used_by_SKILL=['S859', 'S859', 'S859', 'S859', 'S859']
ACCEPT-D-69: PASS legs=8/8    exit=0
$ python3 -B reports/round-69/accept-d.py --root /tmp/r69d-fx-bare
LEG PASS STAMP / LEG FAIL SECTION / FAIL TABLE / STATES / FIELDS / SIGNATURES / EVIDENCE / SOURCE ("no decision table")
ACCEPT-D-69: FAIL legs=1/8    exit=1
```

VERDICT: DRAFT-VALIDATED — the §3 bytes satisfy all 8 legs of the frozen
`reports/round-69/accept-d.py` when S859 is landed as §3(c) specifies, and the
do-nothing tree is caught (1/8). This is scratch evidence, not a lane
measurement; the lane verdict belongs to the L1's counting command
(`python3 -B reports/round-69/accept-d.py --root .`) after landing.

## 5. Findings

- **F1 — VERDICT: FINDING (instrument, pre-data, no leg impact).** The frozen
  green control's Evidence line-cites are partially off: in
  `reports/round-69/accept-d.py` `FIXTURE_TABLE` (`:46-50`),
  `settled-retired` cites `check-supersession-settlement.py:129`, but
  `:129-130` is the **settled-split** condition; the retired branch is
  `:125-126`. `pending` cites `:112` (the `def classify` line) where the
  assignment is `:133`. The counter's legs never validate line accuracy
  (EVIDENCE only requires an existing path token), so the predicate is
  unaffected and the fixture must NOT be edited post-freeze; the §3 draft
  carries the corrected cites (`:125`, `:132`).
- **F2 — VERDICT: FINDING (doc-vs-code gap in the committed tool).**
  `tools/check-supersession-settlement.py:21-22` (docstring) promises a
  `STALE-USED-BY` class — "a row whose used-by names a path that does not
  contain the row's own id … (reported)" — but no committed code implements
  the containment test: `scan()` collects **all** used-by paths into the
  misnamed `stale` list (`:139-144`) and only checks `os.path.exists`
  (`:162-164`); `--ledger` likewise (`:213-215`); the round-69 harness
  `tools/check-settlement-fixture.py` greps only the `SETTLEMENT:` summary
  (`:74-76`). The §3 cautions paragraph states this honestly instead of
  inventing the behavior.
- **F3 — VERDICT: CONFIRMED (behavioral detail encoded in the draft).**
  Branch precedence in `classify()` (`:123-131`) means closed outranks
  retired: the live pair S047>S029 has **both** rows `rejected` and reads
  `SETTLED-CLOSED` (scan §1.1), and ledger `:76` records S132>S094 the same
  way. A writer reading the docstring alone ("superseded row itself is
  rejected") could mis-rule such a pair as retired; the draft's caution names
  the precedence.
- **F4 — VERDICT: CONFIRMED (data shape).** Live chain census 47 = 30
  settled-active + 4 settled-retired + 12 settled-closed + 1 settled-split,
  `pending=0`, `missing_paths=0` — every row of the draft table has live
  instances except pending, which is instantiated by the round-68 history
  (34 chains ruled, `LOG.md:4214`) and by the tool's own pending fixture
  (`selftest` `pending-detected`).
- **F5 — VERDICT: DEPENDENCY (expected pre-data state).** At base, the lane
  tree fails leg SOURCE (and SECTION) because the table and S859 are not
  landed; the do-nothing control documents exactly this red. Landing order
  that keeps the predicate honest: S859 row + `corpus/lessons/round-69.md`
  `## Gate` quote, then the §3 SKILL.md insert, then the counting command.

## 6. Compliance

Wrote exactly one repo file (this report) plus `/tmp` scratch
(`/tmp/r69d-draft-validate.py`, `/tmp/r69d-fx-green/`, `/tmp/r69d-fx-bare/`,
`/tmp/r69d-draft-section.md`, `/tmp/r69d-draft-signatures.md`). No production
byte edited; no git/jj mutation; no network fetch; no installs (none needed);
no subagent dispatched.
