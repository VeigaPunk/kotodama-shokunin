# CritD4 — D2 sourced leg: is own-work tier-A S859 admissible under SOURCES-CONTRACT-v1?

Seat: round-69 w1, critic (depth, calibration). Read-only on production bytes;
every command below was run by this seat on 2026-10-24 from the lane root
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`. No network fetches.

## Ruling

VERDICT: ADMISSIBLE — an own-work, tier-A registry row (S859) pointing at the
lane's own re-runnable settlement check is contract-clean under fleet
SOURCES-CONTRACT-v1. The lane does NOT need an external source for this row.

VERDICT: PASS — the source is openable today: both gates re-ran green in this
session (outputs below), so rule 1's "opened in the round that writes the row"
duty is satisfiable by the integrating seat's own re-run.

VERDICT: PASS (conditional) — the counter's SOURCE leg is reachable exactly one
way: a landed S859 row with `status=mined` and `used-by` containing
`SKILL.md`, cited from the table. Today zero rows satisfy it (evidence below).

## The contract lines that decide it

Fleet contract: `/home/vgpnk/Projects/shokunin/.ufo/waves/kaika/SOURCES-CONTRACT-v1.md`
(frozen, kaika 2026-10-19; adopted by the lane at `corpus/SOURCES.md:5-6`
"Shape and rules: fleet contract `SOURCES-CONTRACT-v1`").

1. **Deciding line — tier A.** SOURCES-CONTRACT-v1.md lines 26-30:
   > `tier` — scoped to `scope`, never global. **A**: primary or authoritative
   > for that scope (spec, official docs, source code, original paper,
   > maintainer statement, **the lane's own re-runnable gate output**). …
   > `community` is never A.

   The settlement check (`tools/check-settlement-fixture.py`,
   `tools/check-supersession-settlement.py`) is literally "the lane's own
   re-runnable gate output" — the clause exists for exactly this row. Tier A
   is scoped, so the scope cell must name the settlement-verdict scope, not a
   general scope.

2. **Deciding line — source cell.** SOURCES-CONTRACT-v1.md line 23:
   > `source` — title — canonical URL or DOI (**a repo path or command for
   > `own-work`**).

   The URL-vs-repo-path question is answered: S859's `source` cell carries the
   repo path / command, not a URL. Combined with this round's no-fetch rule,
   no external source is required or wanted.

3. **Kind + tier legality.** SOURCES-CONTRACT-v1.md lines 24-25 list `own-work`
   in the `kind` enum; the census enum check (line 78) flags tier-inflation
   only for `kind=community` at tier A — `own-work` at tier A is not inflation.
   Lane mirror of clause 1: `corpus/SOURCES.md:16-18` carries the identical
   "the lane's own re-runnable gate output" wording.

4. **Obligations that ride along** (not blockers; they are the standard Gate
   duties). SOURCES-CONTRACT-v1.md rule 1 (lines 45-48): "Write it only after
   opening the source in the round that writes the row. The round lesson's
   `## Gate` records, for every new row, the URL, the access date, and a
   ≤25-word quote with its location grounding `teaches`." For own-work the
   "URL" slot is the repo path or command (clause 2 above); the quote should be
   verbatim captured output of a real run. Rule 2 (lines 49-51): append-only;
   S859 is a new appended row — compliant. Census line 80: "mined rows whose
   used-by paths do not exist — must print nothing" — `SKILL.md` exists at the
   lane root (verified below). Rule 6: no credentials — a local command output
   carries none.

## Current state (measured, not assumed)

- `grep S859 corpus/SOURCES.md` → no matches. S859 is unclaimed; S858 is the
  last row (line 813), so S859 is the next free id.
- `grep SKILL\.md corpus/SOURCES.md` → no matches. **Zero rows have used-by
  naming SKILL.md**, so the D2 counter's SOURCE leg cannot pass except via the
  new S859 row.
- `grep own-work corpus/SOURCES.md` → no matches. S859 would be the lane's
  first own-work row; the contract provisions the kind, and the counter's own
  fixture row (accept-d.py lines 214-216) is the tested 11-column shape:
  `| S859 | … | own-work | A | … | mined | 2026-10-24 | 90d | SKILL.md |`.
- `python3 -B reports/round-69/accept-d.py --root .` at the current tree:

  ```
  LEG PASS STAMP self=06b0352a0288 committed=06b0352a0288
  LEG FAIL SECTION heading=### Registry correction chains
  LEG FAIL TABLE no decision table
  LEG FAIL STATES no decision table
  LEG FAIL FIELDS no decision table
  LEG FAIL SIGNATURES no decision table
  LEG FAIL EVIDENCE no decision table
  LEG FAIL SOURCE no decision table
  ACCEPT-D-69: FAIL legs=1/8
  exit=1
  ```

  SOURCE is red only because SECTION is red — the table does not exist yet
  (declared do-nothing state). `SKILL.md` present at lane root;
  `corpus/lessons/round-69.md` absent (as declared: not landed).

## The source is re-runnable today (rule 1 satisfied by real runs)

```
$ python3 -B tools/check-settlement-fixture.py --selftest
PASS fixture-green rc=0 pending=0 missing_paths=0
PASS fixture-negative rc=0 pending=0 missing_paths=1
PASS fixture-pending rc=1 pending=1 missing_paths=0
FIXTURE: 3/3
exit=0

$ python3 -B tools/check-settlement-fixture.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin
… FIXTURE: 3/3
LANE: pending=0 missing_paths=0
exit=0

$ python3 -B tools/check-supersession-settlement.py --scan
SETTLED-ACTIVE S044>S034 s=mined t=queued same_url=True used_by=1
… (47 chain lines) …
SETTLEMENT: pending=0 chains=47 usedby_paths=709 missing_paths=0
exit=0
```

Both tools are contract read-only ("never mutates the lane tree, never touches
the network" — headers at check-settlement-fixture.py:34-35 and
check-supersession-settlement.py:40-41).

**Gate quote candidates** (verbatim, each ≤25 words, location = command + exit
code):

- From the harness negative case: location
  `python3 -B tools/check-settlement-fixture.py --selftest` (exit 0) —
  quote: `PASS fixture-negative rc=0 pending=0 missing_paths=1` (7 words). This
  is the round's own negative case — the missing-used-by defect class O2
  targets — so it grounds `teaches` best.
- From the live scan: location
  `python3 -B tools/check-supersession-settlement.py --scan` (exit 0) —
  quote: `SETTLEMENT: pending=0 chains=47 usedby_paths=709 missing_paths=0`
  (6 words).

Round-68 Gate line shape precedent (`corpus/lessons/round-68.md:50-82`,
`- S8NN | URL | date | "quote"`, 25-word band noted at lines 53-57): for S859
the URL slot becomes the command, e.g.

```
- S859 | repo path/command: python3 -B tools/check-settlement-fixture.py --selftest (exit 0) | 2026-10-24 | "PASS fixture-negative rc=0 pending=0 missing_paths=1"
```

The integrating seat must re-run the command at write time and quote its own
capture (fleet AGENTS.md evidence rules: "Claimed" ≠ "re-executed"); the runs
above prove openability, they are not a substitute for that Gate capture.

## Attack findings — failure classes that would break the sourced leg after landing

1. **Status must be `mined` at landing, not `queued`.** accept-d.py:186
   requires `cells[7] == "mined"`. A queued S859 fails SOURCE → claim fails as
   declared. `mined` is honest at landing because SKILL.md's new table cites
   the row (contract: mined = "cited by ≥1 path in `used-by`", line 36-37).
2. **used-by must contain the literal substring `SKILL.md`** (accept-d.py:187).
   Cell exactly `SKILL.md` is safest; the fleet census then verifies that path
   exists relative to lane root — it does.
3. **Eleven-column shape, no `|` inside cells** (census NF=13 check,
   SOURCES-CONTRACT-v1.md:70). First own-work row in the registry — no live
   precedent to copy; use the counter's own fixture-row shape.
4. **Only S859 needs the mined+SKILL.md property.** The SOURCE leg
   (accept-d.py:177-189) collects every S-id appearing anywhere in the table's
   cells and passes if ≥1 satisfies; a second cited S-id that is mined with
   SKILL.md used-by would also satisfy, but no such row exists today — cite
   S859 and nothing else.
5. **EVIDENCE leg is per-row** (accept-d.py:167-175): each Evidence cell must
   contain a path token that exists on disk (PATH_RE matches e.g.
   `tools/check-supersession-settlement.py`; a `:NN` suffix survives the
   regex). Point Evidence cells at real lane paths and keep the line numbers
   accurate — the checker does not read them, a human gate will.
6. **Gate duties:** `opened` = 2026-10-24; anchor = command + exit code (never
   a bare "homepage" analog); ≤25-word located quote; `scope` names the
   settlement-verdict scope so tier A stays claim-scoped (QUALITY.md criterion
   6 spirit: authority is scoped, and for gate behavior the gate output is the
   primary source).
7. **Append-only discipline:** S859 is appended; nothing in existing rows may
   be edited to admit it. No used-by flips elsewhere are needed for D2.

## Not evaluated

- The D2 table's five-state content, signatures and Error-patterns linkage
  (other seats' legs; SECTION is red at base by design).
- Claim admission of the SKILL.md entry itself (QUALITY.md's province; no
  entry exists yet).
- Anything requiring network or fleet writes (out of bounds this round).
