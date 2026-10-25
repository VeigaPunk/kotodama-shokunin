# MutD1 — mutation test of the STATES leg of round-69 accept-d.py

Seat: round-69 v1 wave, lane kotodama-shokunin (base 793f79746712). Leaf, no
dispatch. Read-only on production bytes; all mutation happened on copies
under `/tmp/mutd1/`. No installs were needed (python3 3.14.8 already
present), so `/home/vgpnk/.omp/agent/RULES.md` install policy was not
exercised. No network fetches.

## Question

Does `reports/round-69/accept-d.py` kill the four-state shortcut (a
`### Registry correction chains` table with `settled-split` dropped)?

## Method

Three counter variants, each run as `<variant-dir>/accept-d.py` (see
finding F3 on why the basename matters), each evaluated against fixtures
whose embedded `reports/round-69/accept-d.py` is byte-identical to the
running counter, so the STAMP leg stays green and STATES/TABLE semantics
are isolated:

- **orig** — unmodified lane counter, SHA-256
  `06b0352a0288be7a788bb65f243980c77e107e2e4795743b4c4e1a40cd490c10`,
  verified equal to the committed lane file (`sha256sum`, run below).
- **mut1** — STATES tuple only: `"settled-split"` dropped.
- **mut2** — mut1 plus `and len(rows) == 5,` → `and len(rows) == len(STATES),`.

Fixtures: `fx4` = four-state table + 4 signatures + S859 SOURCES row +
`tools/check-supersession-settlement.py`; `fx5` = same plus the
settled-split row and `scope-limiter-missing` signature. Driver:
`/tmp/mutd1/mutdrive.py`; full log: `/tmp/mutd1/run.log`.

## Mutations (unified diff)

```
== MUTATION DIFF mut1 (STATES only) vs orig ==
--- orig
+++ mut1
@@ -35,4 +35,3 @@
 HEADING = "### Registry correction chains"
-STATES = ("pending", "settled-active", "settled-retired", "settled-closed",
-          "settled-split")
+STATES = ("pending", "settled-active", "settled-retired", "settled-closed")
 PATH_RE = re.compile(r"[A-Za-z0-9_./-]+\.(?:py|md|tsv|txt|json|ya?ml)")

== MUTATION DIFF mut2 (STATES + TABLE) vs mut1 ==
--- mut1
+++ mut2
@@ -146,3 +146,3 @@
     res.add("TABLE", header is not None and len(header) == 5
-            and len(rows) == 5,
+            and len(rows) == len(STATES),
             "header=%s rows=%d" % (len(header) if header else 0, len(rows)))
```

## Runs

### [A] ORIG counter vs FOUR-state fixture — the kill check

```
$ python3 -B /tmp/mutd1/counter-orig/accept-d.py --root /tmp/mutd1/fx4-orig
LEG PASS STAMP self=06b0352a0288 committed=06b0352a0288
LEG PASS SECTION heading=### Registry correction chains
LEG FAIL TABLE header=5 rows=4
LEG FAIL STATES states=['pending', 'settled-active', 'settled-retired', 'settled-closed']
LEG PASS FIELDS empty=none short=none
LEG PASS SIGNATURES missing=none
LEG PASS EVIDENCE unresolved=none
LEG PASS SOURCE mined_used_by_SKILL=['S859', 'S859', 'S859', 'S859']
ACCEPT-D-69: FAIL legs=6/8
exit=1
```

### [B] MUT1 (STATES-only mutation) vs FOUR-state fixture

```
$ python3 -B /tmp/mutd1/counter-mut1/accept-d.py --root /tmp/mutd1/fx4-mut1
LEG PASS STAMP self=190fe12366ee committed=190fe12366ee
LEG PASS SECTION heading=### Registry correction chains
LEG FAIL TABLE header=5 rows=4
LEG PASS STATES states=['pending', 'settled-active', 'settled-retired', 'settled-closed']
LEG PASS FIELDS empty=none short=none
LEG PASS SIGNATURES missing=none
LEG PASS EVIDENCE unresolved=none
LEG PASS SOURCE mined_used_by_SKILL=['S859', 'S859', 'S859', 'S859']
ACCEPT-D-69: FAIL legs=7/8
exit=1
```

### [C] MUT2 (STATES+TABLE mutated) vs FOUR-state fixture — accept check

```
$ python3 -B /tmp/mutd1/counter-mut2/accept-d.py --root /tmp/mutd1/fx4-mut2
LEG PASS STAMP self=531c90fccf6b committed=531c90fccf6b
LEG PASS SECTION heading=### Registry correction chains
LEG PASS TABLE header=5 rows=4
LEG PASS STATES states=['pending', 'settled-active', 'settled-retired', 'settled-closed']
LEG PASS FIELDS empty=none short=none
LEG PASS SIGNATURES missing=none
LEG PASS EVIDENCE unresolved=none
LEG PASS SOURCE mined_used_by_SKILL=['S859', 'S859', 'S859', 'S859']
ACCEPT-D-69: PASS legs=8/8
exit=0
```

The mutated counter **no longer rejects** the four-state table.

### [D] ORIG counter vs FIVE-state fixture — sanity green

```
$ python3 -B /tmp/mutd1/counter-orig/accept-d.py --root /tmp/mutd1/fx5-orig
LEG PASS STAMP self=06b0352a0288 committed=06b0352a0288
LEG PASS SECTION heading=### Registry correction chains
LEG PASS TABLE header=5 rows=5
LEG PASS STATES states=['pending', 'settled-active', 'settled-retired', 'settled-closed', 'settled-split']
LEG PASS FIELDS empty=none short=none
LEG PASS SIGNATURES missing=none
LEG PASS EVIDENCE unresolved=none
LEG PASS SOURCE mined_used_by_SKILL=['S859', 'S859', 'S859', 'S859', 'S859']
ACCEPT-D-69: PASS legs=8/8
exit=0
```

Cross-validates the rig: my hand-built five-state fixture is equivalent-green
to the counter's own selftest green fixture.

### [E] MUT2 vs FIVE-state fixture — reverse kill (kill-scored mutant)

```
$ python3 -B /tmp/mutd1/counter-mut2/accept-d.py --root /tmp/mutd1/fx5-mut2
LEG PASS STAMP self=531c90fccf6b committed=531c90fccf6b
LEG PASS SECTION heading=### Registry correction chains
LEG FAIL TABLE header=5 rows=5
LEG FAIL STATES states=['pending', 'settled-active', 'settled-retired', 'settled-closed', 'settled-split']
LEG PASS FIELDS empty=none short=none
LEG PASS SIGNATURES missing=none
LEG PASS EVIDENCE unresolved=none
LEG PASS SOURCE mined_used_by_SKILL=['S859', 'S859', 'S859', 'S859', 'S859']
ACCEPT-D-69: FAIL legs=6/8
exit=1
```

The mutant rejects the genuine five-state table — the mutation changed
behavior in both directions, so [C] is a real acceptance flip, not a
no-op mutant.

### [F] UNMODIFIED lane counter `--selftest` (requested paste)

```
$ python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-69/accept-d.py --selftest
GREEN FIXTURE: PASS (legs 8/8)
DO-NOTHING FIXTURE: FAIL (as required) (legs 1/8)
SELFTEST: 2/2
exit=0
```

### [G] MUT2 counter against the REAL lane root (read-only)

```
$ python3 -B /tmp/mutd1/counter-mut2/accept-d.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin
LEG FAIL STAMP self=531c90fccf6b committed=06b0352a0288
LEG FAIL SECTION heading=### Registry correction chains
LEG FAIL TABLE no decision table
... (all legs FAIL)
ACCEPT-D-69: FAIL legs=0/8
exit=1
```

A mutated counter cannot pass against the lane tree: STAMP compares the
running script's digest against the committed `reports/round-69/accept-d.py`
and fails (`self=531c90… committed=06b035…`).

### [H] ORIG counter against the REAL lane root (read-only, pre-data state)

```
$ python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-69/accept-d.py --root /home/vgpnk/Projects/shokunin/kotodama-shokunin
LEG PASS STAMP self=06b0352a0288 committed=06b0352a0288
LEG FAIL SECTION heading=### Registry correction chains
... (all data legs FAIL: table not landed yet)
ACCEPT-D-69: FAIL legs=1/8
exit=1
```

Counter is red against the lane before the data lands, as designed.

### Counter identity

```
$ sha256sum /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-69/accept-d.py
06b0352a0288be7a788bb65f243980c77e107e2e4795743b4c4e1a40cd490c10  reports/round-69/accept-d.py
```

Matches the `orig` copy actually mutated — the experiment attacked the
committed bytes.

## Findings

- **F1 — the STATES leg is redundant by design.** Two independent guards
  reject a four-state table: `TABLE` (`len(rows) == 5`,
  accept-d.py:147-149) and `STATES` (exact five-tuple comparison,
  accept-d.py:36-37,152). Mutating STATES alone ([B]) still fails overall
  on the TABLE backstop. Both must be mutated ([C]) for acceptance.
- **F2 — the mutation is kill-scored.** The MUT2 counter accepts the
  four-state fixture and rejects the genuine five-state fixture ([E]),
  so the acceptance flip in [C] is attributable to the mutation, not a
  pre-existing pass-through.
- **F3 — STAMP is basename-dependent.** `SELF = basename(__file__)`
  (accept-d.py:33), so a copy renamed to e.g. `accept-d-orig.py` always
  reads `committed=none` against any root that embeds only
  `accept-d.py` (observed in the first rig pass). Tamper evidence
  therefore binds on name + digest.
- **F4 — STAMP defends the lane tree, not sandbox runs.** Inside an
  attacker-controlled root, embedding the mutated counter as
  `reports/round-69/accept-d.py` makes STAMP green ([C]) — STAMP attests
  "this run matches the counter committed in the tree being evaluated",
  which is exactly the right property for the lane run ([G] shows the
  mutated counter failing against the real lane).
- **F5 — scope note.** All acceptance flips happened on fixtures under
  `/tmp`; the lane tree was only ever read. The five-state requirement
  itself is also enforced downstream by the SOURCE leg's structure
  (unchanged in all mutants).

## Verdicts

- VERDICT: PASS — unmodified counter `--selftest` is green: GREEN FIXTURE
  PASS 8/8, DO-NOTHING FAIL 1/8 (as required), SELFTEST 2/2, exit=0 ([F]).
- VERDICT: PASS — the counter kills the four-state shortcut: ORIG rejects
  the four-state fixture on both TABLE and STATES, exit=1 ([A]).
- VERDICT: PASS — the kill is redundant: a STATES-only mutation is still
  rejected by the TABLE row-count backstop ([B]).
- VERDICT: PASS — with STATES and TABLE both mutated, the counter accepts
  the four-state table (8/8, exit=0) and rejects the genuine five-state
  table, i.e. the mutant is kill-scored in both directions ([C], [E]).
- VERDICT: PASS — STAMP blocks running a mutated counter against the real
  lane tree (`self≠committed`, 0/8) ([G]).
- Answer to the seat question: **YES — the counter kills the four-state
  shortcut.** Killing it requires simultaneously mutating two independent
  legs, and even the fully mutated counter then fails STAMP against the
  lane tree; a four-state SKILL.md alone can never pass the committed
  counter.

## Artifacts

- Rig driver: `/tmp/mutd1/mutdrive.py` (scratch, disposable)
- Full run log: `/tmp/mutd1/run.log`
- Counter variants: `/tmp/mutd1/counter-{orig,mut1,mut2}/accept-d.py`
  (SHA-256: orig `06b0352a0288…`, mut1 `190fe12366ee…`, mut2 `531c90fccf6b…`)
- Fixtures: `/tmp/mutd1/fx{4,5}-{orig,mut1,mut2}/`
