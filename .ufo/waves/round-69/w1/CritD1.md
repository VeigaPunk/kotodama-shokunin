# CritD1 — round-69 w1 — attack D2's decision-table content before it is written

Seat: CritD1 (leaf, judged on depth). Scope: derive the exact chain-state taxonomy
`### Registry correction chains` must carry, from the code the claim cites
(`classify()` in `tools/check-supersession-settlement.py`) plus the frozen
counter (`reports/round-69/accept-d.py`) and the round-68 ledger record. Read-only
on production bytes; mutations demonstrated on /tmp copies only.

---

## 1. Instruments at base (commands + real output)

```
$ python3 -B reports/round-69/accept-d.py --root .
LEG PASS STAMP self=06b0352a0288 committed=06b0352a0288
LEG FAIL SECTION heading=### Registry correction chains
LEG FAIL TABLE no decision table
... (TABLE/STATES/FIELDS/SIGNATURES/EVIDENCE/SOURCE all FAIL, no decision table)
ACCEPT-D-69: FAIL legs=1/8        rc=1

$ python3 -B reports/round-69/accept-d.py --selftest
GREEN FIXTURE: PASS (legs 8/8)
DO-NOTHING FIXTURE: FAIL (as required) (legs 1/8)
SELFTEST: 2/2                     rc=0

$ python3 -B tools/check-supersession-settlement.py --selftest
PASS pending-detected ... PASS unreadable-exit-2
SELFTEST: 7/7                     rc=0

$ python3 -B tools/check-settlement-fixture.py --selftest
PASS fixture-green rc=0 pending=0 missing_paths=0
PASS fixture-negative rc=0 pending=0 missing_paths=1
PASS fixture-pending rc=1 pending=1 missing_paths=0
FIXTURE: 3/3                      rc=0

$ python3 -B tools/check-supersession-settlement.py --scan --root .
47 chain lines, all SETTLED-*; live examples of every class:
  SETTLED-ACTIVE  S044>S034 s=mined t=queued used_by=1   (30 chains)
  SETTLED-RETIRED S490>S379 s=rejected t=mined used_by=0 (4 chains)
  SETTLED-CLOSED  S185>S145 s=mined t=rejected used_by=1 (11 chains, incl. both-rejected S047>S029)
  SETTLED-SPLIT   S575>S420 s=mined t=mined used_by=1    (1 chain)
SETTLEMENT: pending=0 chains=47 usedby_paths=709 missing_paths=0   rc=0

$ grep -c "SKILL.md" corpus/SOURCES.md  -> 0 matches (Grep tool: no matches)
```

VERDICT: PASS — all four pre-data instruments are frozen, byte-stamped (STAMP
self==committed `06b0352a0288`), and behave as declared at base: the D2 counter
is red at base exactly as its do-nothing control requires, and green on its
fixture. The live registry is fully settled (pending=0) and has no row naming
SKILL.md yet, so the counter's SOURCE leg can only pass once S859 lands.

---

## 2. The exact taxonomy the table must carry

`classify()` (tools/check-supersession-settlement.py:112-145) walks every
well-formed row whose `teaches` matches `supersedes\s+(S\d{3,})` (SUP_RE, :53 —
searched anywhere in `teaches`, despite SOURCES.md:12 documenting "opens" and
the docstring's "opens"; verified: mid-teaches still forms a chain). With
s = successor row, t = target row (`missing` if the id does not resolve), and
s_used = the successor's used-by paths minus empties and `—` (:103-109), the
branch order is decisive (:123-133):

1. `t.status == "rejected"` → **settled-closed** (checked FIRST — wins over
   everything, including a rejected successor)
2. elif `s.status == "rejected"` → **settled-retired** (so t is NOT rejected here)
3. elif `s.status=="mined" and s_used and t.status=="queued"` → **settled-active**
4. elif `s.status=="mined" and s_used and t.status=="mined" and SPLIT_RE.search(s.teaches)` → **settled-split**
5. else → **pending** (correction debt; the only class `--scan`'s exit code gates, :167)

SPLIT_RE (:54): `for\s+(entry|line|row|cell|clause)\b.{0,40}\bonly\b` with re.S —
one of exactly five singular nouns, then any ≤40 chars (newlines count) then
`only`. The limiter is read only from the successor's `teaches`.

### The table skeleton (exact 5-column shape; states in the counter-required order)

Counter constraints first, because they are what the claim is judged by
(accept-d.py:36-37,146-189): heading line exactly `### Registry correction chains`
(first match wins; section ends at the next `## ` H2, not `### `); the FIRST
table after the heading must have a 5-cell header and EXACTLY 5 data rows, in
this order (STATES leg does a list equality on `row[0].lower()`):
`pending, settled-active, settled-retired, settled-closed, settled-split`.
Every cell non-empty; no `|` inside any cell (splits the row); no sixth row
(a "stale-used-by" row fails TABLE/STATES — keep it in prose, it is not a chain
state). Column 4 (`Error signature`) must appear verbatim as a substring in the
`## Error patterns` section. Column 5 (`Evidence`) must contain at least one
path-shaped token that exists (`tools/check-supersession-settlement.py` always
does; `:NN` line suffixes are stripped by PATH_RE and safe). Column 1 rows (or
any cell) must cite an S-id that in `corpus/SOURCES.md` is an 11-cell row with
`status=mined` and `used-by` containing `SKILL.md` — today only S859 can do
that, after it lands.

```markdown
### Registry correction chains

A supersedes pair is one successor row whose `teaches` names one target row.
Settlement is a property of the PAIR's two `status` cells plus the successor's
`used-by` and `teaches` — the checker (`tools/check-supersession-settlement.py`,
`--scan`; exit 0 iff no pending chain) reads only those. Five states, tested in
this order — the first match wins:

| State | Row shape (what the code actually tests) | Writer's next action | Error signature | Evidence |
|---|---|---|---|---|
| pending | any pair matching none of the four settled shapes — typically successor `mined` + target `mined` with no scope limiter, successor `queued`, or `used-by` still `—` | decide the ruling (activate / retire / keep-successor / keep-reject / keep-split) in a disposition ledger row, then apply its mechanism (repoint, usedby-flip, cell-flip, none); `--scan` exits 1 until then | chain-left-pending | S859 — tools/check-supersession-settlement.py:132 |
| settled-active | successor `mined` with a non-`—` `used-by` path AND target `queued` | the entry is re-pointed to the successor; ledger ruling `activate` (the tool checks the successor's own status is `mined`, :207) and the named `used-by` path must exist on disk (:213) | entry-not-repointed | S859 — tools/check-supersession-settlement.py:127 |
| settled-retired | successor `rejected` AND target NOT `rejected` (target usually stays `mined`; the entry keeps citing it) | keep the target; ledger ruling `retire` (status must be `rejected`, :209); record the flip condition in the ledger note so a later round can activate — R68-M2 did this for S490>S379 | retired-row-mined | S859 — tools/check-supersession-settlement.py:125 |
| settled-closed | target `rejected` — whatever the successor's status (both-rejected and `mined`-over-`rejected` both land here; target-rejection is tested first, :123) | keep the successor; ledger ruling `keep-successor` — never `keep-reject` for a mined successor (R68-M6: drafted backwards for S648-S651, caught by `--ledger` `keep_reject_but_status=mined`) | closed-chain-kept | S859 — tools/check-supersession-settlement.py:123 |
| settled-split | both rows `mined`, successor's `teaches` carries the limiter `for {entry,line,row,cell,clause} …≤40 chars… only` (singular nouns only; live form: S575 "for entry :41's cadet clause only") | narrow the scope, don't flip rows: each row keeps its slice; ledger ruling `keep-split`; a missing/broken limiter reads as pending — fix the limiter text or retire the successor | scope-limiter-missing | S859 — tools/check-supersession-settlement.py:129 |

Not a chain state: `STALE-USED-BY` (see Error patterns) — write it as prose
here, never as a sixth table row.
```

Companion `## Error patterns` rows (SIGNATURES leg needs each cell-4 token
verbatim somewhere in that section; house shape is the two-column
`| Observation | Reading |` table, SKILL.md:470):

```markdown
| a supersedes pair matches no settled shape | chain-left-pending: the correction never landed; `--scan` exits 1 and the debt is ruled in a disposition ledger (`tools/check-supersession-settlement.py:167`; round-68 settled 34 chains this way) |
| successor `mined`, `used-by` names a path, the entry still cites the target | entry-not-repointed: the tool checks the path EXISTS, not that the entry cites the successor — citation truth is review work (`:162-163`); repoint and re-run the harness |
| a ledger `retire` ruling against a row still `mined` | retired-row-mined: `--ledger` rejects it (`retire_but_status=mined`, `:209`); reject the successor first, or the ruling is wrong |
| a closed chain's rejected target re-activated, or its mined successor drafted `keep-reject` | closed-chain-kept: target-rejection wins the classification (`:123`); keep-successor is the ruling (R68-M6) |
| both rows `mined` with no `for <noun> … only` limiter in the successor's `teaches` | scope-limiter-missing: the pair reads pending; the limiter allows only the five singular nouns within 40 chars of `only` (`:54`) |
```

---

## 3. What a reader (or the writer) could get wrong — each verified

1. **State order.** The docstring lists SETTLED-ACTIVE → RETIRED → CLOSED →
   SPLIT, pending last ("any other non-rejected pair"). The counter demands
   `pending` FIRST (accept-d.py:36-37, `got == list(STATES)`). A writer
   following the docstring's order fails the STATES leg.
2. **Precedence inverts the obvious reading of "retired".** Both-rejected is
   **settled-closed**, not settled-retired (probe `both-rejected` →
   `SETTLED-CLOSED s=rejected t=rejected`; live S047>S029, S132>S094).
   settled-retired exists only while the target is not rejected.
3. **settled-active silently needs the used-by cell.** successor `mined` +
   target `queued` + `used-by` `—` → **pending** (probe
   `mined-empty-usedby_target-queued` → `PENDING … used_by=0`). "Mined" alone
   does not settle the correction.
4. **The split limiter grammar is narrow.** Probes on the real SPLIT_RE:
   `for entry only` PASS; `for clause only` PASS; `for entry 41 of the parent
   row only` PASS (≤40 chars); `for entry 41 of the parent registry row and its
   descendants only` FAIL (pending); `Only for entry` FAIL (order fixed:
   noun-then-only); `for entries only` FAIL (plural not in the noun set);
   `for SKILL.md only` FAIL (SKILL.md is not one of the five nouns). re.S means
   a newline inside the window still matches. Searched in the successor's
   `teaches` only.
5. **"Opens `supersedes S0NN —`" is convention, not law.** SUP_RE searches
   anywhere in `teaches` (probe `supersedes-mid-teaches` forms a chain). A ghost
   target id (`supersedes S999`, row absent) is **pending**, `t=missing` — debt,
   not an error.
6. **STALE-USED-BY is a docstring ghost.** The docstring (:19-22) defines it as
   "used-by names a path that does not contain the row's own id … reported",
   but `classify()` computes no id-containment — its `stale` list (:139-144) is
   every used-by path of every row, and `scan()` reports only file EXISTENCE
   (`missing_paths`). Do not describe STALE-USED-BY as machine-checked id
   containment; it is not tested anywhere.
7. **`missing_paths` does not gate `--scan`'s exit code.** Fixture-negative
   proves it: `rc=0 pending=0 missing_paths=1`. Scan gates `pending` alone
   (:167). Only the round-69 harness's `--root` mode additionally gates
   `missing_paths` (check-settlement-fixture.py:181-182). The table must not
   claim the checker alone catches the R68-M1 defect class — the harness does.
8. **keep-reject vs keep-successor (R68-M6).** `--ledger` checks
   `activate`/`retire`/`keep-reject` against the LEDGER ROW's OWN status
   (:207-212) — not the target's. keep-successor and keep-split have NO status
   check at all; their safety is the writer's discipline. A mined successor
   ruled keep-reject is a finding (`keep_reject_but_status=mined`).
9. **Citation truth is never machine-read.** No leg reads knowledge-file
   contents; `entry-not-repointed` (does the entry actually cite the successor?)
   is review work — the code says so at :162-163. The fixture's
   `USEDBY_FILE = "cites S002 now\n"` is never parsed.
10. **The counter cannot verify the claim's placement clause.** "under
    `## Decision table`" is not machine-checked (the ### heading is searched
    file-wide; the first match wins; an H2 boundary ends the section but a
    later `###` sibling does not). Placement is claim-fidelity duty: insert
    before `## Error patterns` (SKILL.md:468), e.g. after `### Register craft`
    (:354). House style: one-line authority prologue ("Executable authority
    `tools/check-supersession-settlement.py` (`--selftest`)…") then the table —
    the counter's `parse_table` skips prose to the first `|` line, so the
    prologue is safe.
11. **SOURCE leg depends on S859's exact shape.** Needs an 11-cell
    `| S859 | … |` row, `status` cell exactly `mined`, `used-by` cell
    containing `SKILL.md`, and the id `S859` must appear inside the TABLE rows
    (the leg scans the joined row text, not the lane). No SOURCES.md row names
    SKILL.md today (grep: 0 matches), so SOURCE is red until S859 lands —
    expected at base, do not "fix" by citing another row.
12. **Latent crash found (finding, not a table requirement): a malformed row
    used as a supersedes TARGET crashes the checker.** A ≠11-cell row is stored
    as `{"malformed": True, "id": …}` with no `status` key (:86); a successor
    citing it hits `t_row["status"]` → KeyError (:122). Reproduced on the real
    tool in /tmp: registry with a 10-cell S001 (target) + S002
    `supersedes S001` → `KeyError: 'status'` traceback, process exit 1 — not
    the documented exit 2 "unreadable registry". Evidence: probe
    `malformed-target` (scratch /tmp/r69crit/probe.py, run 2026-10-24). The L1
    may want this in the round's mistakes ledger (defect class: malformed-row
    handling in the frozen instrument; the instrument is frozen post-data, so
    the fix belongs to a later round).

Minor observation for the calibration seat (not mine to close): LOG.md:4214
says "All 34 pending chains closed (31 activate-class incl. S126 already-mined,
4 retire incl. S490)" — 31+4=35, not 34. `to-verify` by whoever owns the
round-68 records correction pass.

---

## 4. Verdicts

- VERDICT: PASS — the five-state taxonomy is fully derivable from
  `classify()` precedence (:123-133) and every branch precondition above is
  verified against the real checker by scratch probes; the live registry
  exhibits all four settled classes (47 chains, pending=0), giving the writer
  one citable live example per row.
- VERDICT: PASS — the frozen D2 counter is red at base exactly as its
  do-nothing control declares (FAIL 1/8, only STAMP green) and its selftest is
  green (2/2; checker 7/7; fixture harness 3/3).
- VERDICT: FAIL (finding) — malformed supersedes-target row crashes the frozen
  checker with `KeyError: 'status'` (exit 1 + traceback, not the documented
  exit 2); recorded above with reproduction.
- VERDICT: NOT-EVALUATED — the real `### Registry correction chains` table,
  S859, and corpus/lessons/round-69.md are not landed yet (declared as
  not-landed); the SOURCE leg could not be observed green on the live lane and
  was only verified green via the counter's own fixture.

Report: .ufo/waves/round-69/w1/CritD1.md
