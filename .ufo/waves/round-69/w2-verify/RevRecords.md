# RevRecords — round-69 record audit (w2 residual verification)

Seat: RevRecords (reviewer). Date: 2026-10-25. Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
(read-only; the only lane write is this file). Lane tip audited: `9e82c7b47651e0aba6ee05cc19770f78bf120cfd`;
data land `e86ed3e99c0ed3abfd7716896315fae4cdca77a2`.

Method: every claim was read from the committed record (`SCORECARD.md` round-69 section
lines 1324–1347, `LOG.md` round-69 entry lines 4221–4234, `corpus/lessons/round-69.md`) and
matched against its committed receipt. Counters were re-run in a sandbox clone
(`git clone -q … /tmp/RevRecords-r69`) at records HEAD, **not** against the live lane. Census was
re-run from the fleet script `/home/vgpnk/Projects/shokunin/scripts/sources-census.sh` against the
clone at base `793f7974` and at HEAD. No installs, no network, no `shokuknow` write, no git mutation
in the lane; the only `git checkout` was inside the /tmp clone.

Re-run tail at records HEAD 9e82c7b (supports every counter claim below):

```
$ python3 -B reports/round-69/accept-o.py --root .      → ACCEPT-O-69: PASS legs=7/7  (rc=0)
$ python3 -B reports/round-69/accept-d.py --root .      → ACCEPT-D-69: PASS legs=8/8  (rc=0)
$ python3 -B reports/round-69/accept-ca.py --root . --fleet-root /home/vgpnk/Projects/shokunin
                                                        → ACCEPT-CA-69: PASS legs=8/8 (rc=0)
```

---

## 1. Numeric claim → receipt line → verdict

| # | claim (SCORECARD / LOG, round 69) | receipt line that carries it | verdict |
|---|---|---|---|
| 1 | O2 `ACCEPT-O-69 PASS 7/7` | `reports/round-69/telemetry/final-measures-o.txt:15` `ACCEPT-O-69: PASS legs=7/7` | **MATCH** |
| 2 | controls-rev1 GREEN 7/7 | `telemetry/controls-rev1.txt:5` `GREEN FIXTURE: PASS (legs 7/7) — as required` | **MATCH** |
| 3 | DO-NOTHING 5/7 FAIL as required | `controls-rev1.txt:6` `DO-NOTHING FIXTURE: FAIL (legs 5/7) — as required` | **MATCH** |
| 4 | SPOOF 6/7 FAIL as required | `controls-rev1.txt:7` `SPOOF FIXTURE: FAIL (legs 6/7) — as required` | **MATCH** |
| 5 | lane registry `pending=0 missing_paths=0` | `final-measures-o.txt:12` `LEG PASS LANE rc=0 pending=0 missing_paths=0` | **MATCH** |
| 6 | Ca2 `5 unannotated mismatches → 0` | before: `declaration-dry-run.txt:23` and `before-measures.txt:13` `LEG FAIL MISMATCHES live_mismatches=5 unannotated_mismatches=5`; after: `final-measures-ca.txt:15` `LEG PASS MISMATCHES live_mismatches=4 unannotated_mismatches=0` | **MATCH** |
| 7 | "5 declared (class, surface) pairs" | `reports/round-69/claims.json` `calibration_pairs` = 5 entries; `reports/round-69/corrections-r68.md` = 5 correction rows (`grep -c '^\| \(LEGCOUNT\|DEADPOINTER\|OVERREACH\)'` → 5) | **MATCH** |
| 8 | "4 live mismatches remain" | `final-measures-ca.txt:15` `live_mismatches=4` | **MATCH** |
| 9 | Ca2 `ACCEPT-CA-69 PASS 8/8` | `final-measures-ca.txt:16` `ACCEPT-CA-69: PASS legs=8/8` | **MATCH** |
| 10 | D2 `ACCEPT-D-69 PASS 8/8` | `final-measures-d.txt:16` `ACCEPT-D-69: PASS legs=8/8` | **MATCH** |
| 11 | D2 five states / 5 rows / 5 non-empty cells / 5 signatures | `final-measures-d.txt:10` `TABLE header=5 rows=5`; `:11` `STATES states=[…5…]`; `:13` `SIGNATURES missing=none`; `:12` `FIELDS empty=none short=none` | **MATCH** |
| 12 | registry `782 → 783` rows | `before-measures.txt:19-21` (`=== registry rows…`, `782`, `783`); re-derived: `git show 793f7974:corpus/SOURCES.md \| grep -cE '^\| *S[0-9]+'` → **782**; HEAD → **783** | **MATCH** |
| 13 | "census exit 0 at start (`census-start.txt`)" | **no receipt line**: `census-start.txt` is 29 lines = 28 × W04 + `kotodama ok …/corpus/SOURCES.md`; `grep -n exit` → no match (also absent at declaration commit `6a98d7d`) | **MISMATCH** (claim not carried; independently reproduced below) |
| 14 | "census exit 0 at end (`census-end.txt`)" | `census-end.txt:32` `exit=0` (28 W04, same flagged set) | **MATCH** |
| 15 | 32 seats | `w1/settle.tsv:1` `seats=32 settled=32`; `spec-v1.json` `items` = 32; `taskcall-v1.json` `counts.spawn=32` | **MATCH** |
| 16 | `26/32 attack roles = 81.3%` | `spec-v1.json` roles: mutation-tester 9 + reviewer 9 + critic 8 = 26; `claims.json` `attack_roles=26`; 26/32 = 81.25 % → 81.3 % | **MATCH** |
| 17 | 21 reports returned | `settle.tsv:1` `reports=21`; 21 `w1/*.md`; set-identical to settle `report=yes` names (`diff` empty) | **MATCH** |
| 18 | 11 dead seats | 32 − 21 = 11; `settle.tsv` has 32 unique seat rows; `claims.json` `dead_seats` length 11 | **MATCH** |
| 19 | `9 × provider.rate_limit: 429` | rc tally from `stdout/*.rc`: 21 × `0`, 9 × `1`, 2 × `124`; `grep -c 'provider.rate_limit: 429' stdout/*.err \| grep -v ':0'` → exactly **9** files (CritD5, MutO1, RevC2, RevO1, RevO2, RevO7, ScoutFrontier, Scribe1, Scribe2) | **MATCH** (note: `grep -l '429'` hits 11 files — CritO2 and MutO5 mention 429 in their transcripts but returned reports; only 9 carry the provider error) |
| 20 | `2 × 1200 s timeout` | `settle.tsv` rc=124 for CritO3, RevO4; `CritO3.rc` mtime = start+1200 s (1792896326 vs 1792895126), `RevO4.rc` = +1201 s | **MATCH** (see F7: dispatcher default is 1500; the 1200 override is not itself recorded) |
| 21 | `1201 s wall` | `settle.tsv:2` `start=1792895126 end=1792896327 wall_seconds=1201` | **MATCH** |
| 22 | dead seats "none replaced" | `settle.tsv` = exactly the 32 declared names (`sort -u` → 32), no extra/replacement rows | **MATCH** |
| 23 | "one dispatch call" | `taskcall-v1.json` `counts {spawn:32, resume:0, total:32}`; `dispatch-v1.sh` dispatches the 32 prompts in one invocation | **MATCH** (indirect: the dispatcher's stdout line is not committed) |
| 24 | round-68 corrections: "9 legs: 8 PASS and 1 FAIL (EXEC)" | `grep -cE '^[A-Z0-9_]+ (PASS\|FAIL) ' reports/round-68/telemetry/final-measures-o.txt` → **9**; PASS → **8**; `:13 EXEC FAIL base_pending_fail=True lands_pass=False` | **MATCH** |
| 25 | "`grep -c 'R68-M9' LOG.md corpus/lessons/round-68.md corpus/lessons/round-69.md` → 3 (0 before this round)" | actual output `LOG.md:2`, `corpus/lessons/round-68.md:0`, `corpus/lessons/round-69.md:2` = **4 matched lines in 2 files** (`grep -o` = 10 occurrences); base `793f7974` = 0/0 → "0 before" is correct, the "→ 3" is not | **MISMATCH** |
| 26 | "`ACCEPT-CA-68: PASS` → 0" | `grep -c 'ACCEPT-CA-68: PASS' reports/round-68/telemetry/final-measures-ca.txt` → **0** | **MATCH** |
| 27 | "R68FROZEN proves the crashed round-68 counter is byte-identical to its receipt's sha256" | `final-measures-ca.txt:8` `LEG PASS R68FROZEN live=a6d1c1c24e77 recorded=a6d1c1c24e77`; round-68 receipt line 1 = `# counter sha256 (self): a6d1c1c24e77…` | **MATCH** |
| 28 | S859 "own-work, tier A, opened 2026-10-24", mined, used-by SKILL.md | `corpus/SOURCES.md:814` cells: `S859`, `own-work`, `A`, `mined`, `2026-10-24`, `SKILL.md, corpus/lessons/round-69.md` | **MATCH** |
| 29 | "depth last moved at round 62" | SCORECARD round-62 depth row = `author: PASS (claim D, sourced claim, S693)`; rounds 63–68 depth rows all `unchanged` | **MATCH** |

Census claim #13, independent reproduction (the substance is true even though the receipt omits it):

```
$ cd /tmp/RevRecords-r69 && git checkout -q 793f7974
$ /home/vgpnk/Projects/shokunin/scripts/sources-census.sh validate /tmp/RevRecords-r69 \
    --file /tmp/RevRecords-r69/corpus/SOURCES.md > /tmp/census-base.out 2>&1; echo rc=$?
rc=0
$ wc -l /tmp/census-base.out   → 29   (28 W04 + `file ok …/corpus/SOURCES.md`)
```

Same at HEAD (`rc=0`, 29 lines). The census tool documents `exit 0` for W-only findings; the
receipt's last line is `kotodama ok …/corpus/SOURCES.md`, so the claim is *inferable* from the
cited file plus the tool's documented exit table, but the file does not state the exit code.

---

## 2. Evidence-pointer existence (`test -e`, lane-relative unless noted)

Alive (all tested): `tools/check-settlement-fixture.py`; `reports/round-69/{accept-o,accept-ca,
accept-d}.py`; `reports/round-69/telemetry/{final-measures-o,final-measures-ca,final-measures-d,
controls-rev1,controls,before-measures,declaration-dry-run,census-start,census-end}.txt`;
`reports/round-69/{claims.json,corrections-r68.md}`; `.ufo/waves/round-69/w1/{settle.tsv,CritO1.md,
CritO2.md,ScoutAdj.md,swarm-registry.json}`; `.ufo/waves/round-69/w1/stdout/` (32 `.err`, 32 `.txt`,
32 `.rc`); `.ufo/waves/round-69/{spec-v1.json,taskcall-v1.json,dispatch-v1.sh}`;
`.ufo/waves/round-69/assimilation/{quarantine-slice,reg-ids,staged-ids,collisions}`;
`corpus/{SOURCES.md,lessons/round-69.md,lessons/round-68.md,lessons/round-68-verifier-spotcheck.md,
knowledge}`; `SKILL.md`; `tools/{check-supersession-settlement.py,source-audit-inventory.py}`;
`reports/round-68/telemetry/{final-measures-o,final-measures-ca,final-measures-c}.txt`;
`reports/round-68/accept-ca.py` (its line 224 is `_bh.write(git_bytes(root, BASE, REGISTRY) or "")`,
matching the receipt's `line 224` traceback).

Dead pointers:

1. **`reports/round-69/w1/ScoutAdj.md`** — SCORECARD.md:1333 (coverage row, "measured evidence"
   column). Does not exist and never did: `git log --all -- reports/round-69/w1` is empty; the
   directory `reports/round-69/w1/` does not exist. The correct path used in the same row's
   observation column is `.ufo/waves/round-69/w1/ScoutAdj.md` (exists e.g. as
   `.ufo/waves/round-69/w1/ScoutAdj.md` and the seat's committed report). **Dead.**
2. **`.ufo/reports/round-68/kotodama.md`** (LOG.md:4229–4230) — dead against the lane root; it
   resolves at the fleet root `/home/vgpnk/Projects/shokunin/.ufo/reports/round-68/kotodama.md`
   (exists) and `claims.json` declares that surface `"fleet": true`. **Not dead, but lane-relative
   as written**; a reader starting at the lane gets a dead path.

Not dead, listed for completeness: `census-end.txt` (LOG.md:4231) is a bare filename resolved by
its sibling `reports/round-69/telemetry/census-end.txt`; `considerthese/` (lesson:64) is declared
absent in the same sentence; `.ufo/waves/round-69/w1/stdout/*.err` is a glob over 32 existing
files; `accept-ca.py:224` resolves to the round-68 counter (see above).

---

## 3. Wave accounting vs `settle.tsv` and `spec-v1.json`

```
$ cat .ufo/waves/round-69/w1/settle.tsv | head -2
wave=kotodama-r69-v1 seats=32 settled=32 reports=21
start=1792895126 end=1792896327 wall_seconds=1201

$ cat .ufo/waves/round-69/w1/stdout/*.rc | sort | uniq -c
     21 0
      9 1
      2 124

$ awk '/report=yes/{print $1".md"}' …/settle.tsv | sort > a; ls …/w1/*.md | xargs -n1 basename | sort > b
$ diff a b   → empty; both 21 lines

spec-v1.json: 32 items
roles: mutation-tester 9, reviewer 9, critic 8, scout 3, scribe 2, executor 1
attack = 9+9+8 = 26 (81.25 %); non-attack = 3+1+2 = 6
```

Verdict: **MATCH** on seats (32), rc distribution (21/9/2), `report=yes` (21), dead (11),
attack/non-attack split (26/6, roles exactly as LOG states: reviewer 9, critic 8, mutation-tester 9;
scout 3, executor 1, scribe 2), and wall (1201 s). Spec seat IDs and settle seat IDs are the same
32 names; `report=yes` set equals the 21 report files.

---

## 4. `corpus/lessons/round-69.md` structure

```
10:## Gate
24:## Mistakes
34:## Corrections (round 68, append-only)
48:## Quarantine — shokuknow absent-defect register, kotodama slice (item 10, wave-4 quarantine-first)
```

- **Gate — PASS.** One row (S859) with an access/opened date `2026-10-24` and a located quote of
  **9 words** ("A chain is *settled* when exactly one state holds") at
  `tools/check-supersession-settlement.py:6`; `python3 -B tools/check-gate-quotes.py
  corpus/lessons/round-69.md` → `GATE_QUOTES: 0 findings`. The cited blob
  `1ef2e965204f53f40ffbabf45abea3fae9f029a6` equals
  `git show 52b92a6b:tools/check-supersession-settlement.py | git hash-object --stdin`; the quoted
  command prints `SELFTEST: 7/7`. One candidate admitted (`mined`), none rejected — **≥1 admit**.
- **Mistakes — PASS.** 7 rows: `R68-M9` (backfilled) + `R69-M1..R69-M6`.
- **Quarantine — present, but one sentence FAILS its own cited artefact.** The 21-row slice,
  `reg-ids` 782 and empty `collisions` are as committed (slice = 21 lines; `reg-ids` = 782 lines;
  `staged-ids` = 123 lines; `collisions` = 0 bytes; S859 is not in `reg-ids`, `grep -c` → 0). But:
  ```
  $ head -1 .ufo/waves/round-69/assimilation/staged-ids   → S859
  $ grep -oE '^ *\| *S[0-9]+' corpus/SOURCES.md | grep -oE 'S[0-9]+' | sort -u > /tmp/reg-now  # 783
  $ comm -12 /tmp/reg-now <(sort .ufo/waves/round-69/assimilation/staged-ids)
  S859                                                      # 1 collision
  ```
  The lesson's "The lane's own new row is S859, which is **outside the staged id set**" is false:
  S859 is line 1 of the committed `staged-ids`, and the package row
  (`shokuknow/merge/kotodama/SOURCES.append.md:7`, mirrored in
  `shokuknow/lanes/kotodama/SOURCES-PROPOSED.md:17`: `S859` = GB/T 33661-2017) is the first staged
  package row. The collision file is honestly 0 *at the base snapshot* (782 ids end at S858), but
  the sentence's reassurance is contradicted by the committed artefact it cites. This corroborates
  the same finding in `.ufo/waves/round-69/w2-verify/ScoutItem10.md` §4 (independently re-derived
  here; the package today holds 132 rows — `grep -c '^\| S[0-9]' merge/kotodama/SOURCES.append.md`
  → 132 — so the committed 123 is a snapshot, not a re-derivable count).

---

## 5. Record-consistency verdict

**FAIL (strict) — 3 defects, all record-level; every headline counter claim reproduces.**

- **F1 (MEDIUM, claim not carried):** "census exit 0 at round start (`census-start.txt`)" — the
  named receipt has no exit line (29 lines: 28 W04 + `ok`), unlike the end receipt (`exit=0` at
  `census-end.txt:32`). Independent re-run of the census recipe at base `793f7974` gives `rc=0` with
  the same 28 W04 rows, so the fact is true; the citation is not.
- **F2 (LOW/MEDIUM, wrong number):** SCORECARD:1344 re-derivation
  `grep -c 'R68-M9' LOG.md corpus/lessons/round-68.md corpus/lessons/round-69.md` is printed as
  `→ 3 (0 before this round)`. Actual: `2 / 0 / 2` = 4 matched lines in 2 files (10 occurrences);
  "0 before" is correct.
- **F3 (MEDIUM, false sentence with future consequence):** `corpus/lessons/round-69.md`:60
  "S859 … is outside the staged id set" contradicts `staged-ids:1 = S859`; the current registry
  collides with the staged set on S859 (count 1). Nothing was adopted this round, so the immediate
  consequence is nil, but a future adoption round must treat S859 as contested, not free.

Lower-severity wording/imprecision findings (do not change any verdict):

- **F4 (LOW):** LOG.md:4227 lists **7** leg names for `ACCEPT-D-69 PASS 8/8` (SECTION, TABLE,
  STATES, FIELDS, SIGNATURES, EVIDENCE, SOURCE) and omits `STAMP`; the receipt prints 8 legs
  including `LEG PASS STAMP`.
- **F5 (LOW, disclosed deviation):** `claims.json` `freeze_rule` says the counters are "not edited
  after any seat scores them", yet revision 1 landed at `52b92a6` 23:47:22 **after** the wave
  (23:25:26–23:45:27) in which attack seats scored rev 0 (CritO1's spoof is the forcing receipt),
  and **before** the data land `e86ed3e` 23:49:45. The LOG calls this "before any *data* seat scored
  it"; that is true only under the narrower "data seat" reading. The revision and its forcing
  receipt are disclosed, so this is a rule-wording/practice tension, not a hidden edit.
- **F6 (LOW):** SCORECARD/LOG say "both new counters carry a `R68FROZEN` leg re-deriving the three
  round-68 counters' sha256"; `accept-o.py:238-248` re-derives three (accept-o/ca/c + their
  receipts), `accept-ca.py:220-226` re-derives only the round-68 ca counter. The union covers three;
  the distributive reading overstates the Ca leg.
- **F7 (INFO):** `dispatch-v1.sh` defaults `SEAT_TIMEOUT=${SEAT_TIMEOUT:-1500}`, while the record
  claims a 1200 s per-seat timeout. The rc=124 seats' mtimes sit at start+1200/+1201 s, so 1200 was
  evidently exported; no committed receipt records the override.

Residual risk / verification gaps:

- `staged-ids` (123) is a snapshot of an unversioned package working tree; the package today holds
  132 ids (`grep -c '^\| S[0-9]' merge/kotodama/SOURCES.append.md` → 132, and ScoutItem10 reports
  104 at shokuknow HEAD), so the 123 is not re-derivable from current bytes. I did not diff the
  123-row prefix against today's set. The S859 collision finding rests on the committed `staged-ids`
  and the current registry only.
- "one dispatch call" and "parent alive until settlement" are established from
  `dispatch-v1.sh` + `settle.tsv`; the dispatcher's console line (`dispatched 32 seats …`) is not a
  committed receipt.
- Census exit 0 at start was verified by re-running the recipe on a clone checked out at the base
  revision, not on the original 23:16 worktree; the W04 row set and rc match.
- I did not rule on admission or on whether F5 crosses the kumitate r42 class; that is the
  non-author closure's call.
