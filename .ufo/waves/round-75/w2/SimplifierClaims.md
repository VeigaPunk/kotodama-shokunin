# SimplifierClaims — cut list for claims C and Ca (round 75, wave 2, pre-freeze)

Seat: `SimplifierClaims` (simplifier, leaf). Lane base `f556d1049fe651d3d63975600b13acd9fb686f15`.
Read-only: `reports/round-75/claims.json`, `reports/round-75/ledger.json`, the w1 crits, the round-74
counters, and the wave-2 leg parts **as they stood at 16:51–16:55** (they are being written concurrently;
every code citation below is a line I read, not an inference). No claim, ledger, counter, lane file or
git state was modified. No installs. Scratch `/fast/scratch/hyaku/kotodama-r75/SimplifierClaims/` was
recreated after another seat's cleanup deleted the shared parent at ~16:55 and is removed before yield;
every measurement it produced is reproduced verbatim below.

Verdict in one line: **C 13 → 10 legs, Ca 12 → 10 legs, 6 clause deletions, 0 pair deletions, 2 net-new
clauses and 3 clause transfers.** Every deletion is argued from a measured landing-invariance or a measured
fabrication, not from taste.

---

## 1. The cuts, with the junk-penetration proof

Rule applied: a leg or clause is cut only if (a) no junk landing listed in `CritCCounterVacuity.md` or
`CritCaVacuity.md` becomes newly possible, **and** (b) either no landing can change its verdict, or every
passing value it accepts is reachable by a landing that never performed the act it certifies.

### 1.1 CUT — C leg 7 `GROUND` (13 → 12)

Frozen text:

> `GROUND: reports/round-75/telemetry/gap-sweep.txt names the 808-row registry and 0 matches per
> fragment at base; the counter independently re-derives 0 at base`

Its two halves separate cleanly:

- **"the counter independently re-derives 0 at base"** reads `mat_base` only. `mat_base` is the frozen
  base revision: **no landing can change it**. A check whose only input is `<base>` is green or red
  independently of `<lands>` — it cannot distinguish a junk landing from an honest one, by construction.
- **"the receipt … names the 808-row registry and 0 matches per fragment"** is satisfied by 27 bytes of
  prose. Measured against the in-flight `leg_ground` predicates (`leg-ground-cited-census.py:19-86`:
  `(\d+)[- ]row`, one `0` within the fragment's own line + 2 continuation lines):

```
A/ fabricated GROUND receipt: N-row ok: True
A/ per-fragment zero: [True, True, True]
```

`CritCCounterVacuity` already records this as its GROUND row ("**No** to receipt provenance/content";
round-74 `MutPredicateC` F8 executed it). Cutting GROUND therefore removes **no** survivor the crit
lists. Cost to behaviour: a landing could omit `gap-sweep.txt`; that file is a freeze-time sweep record
and belongs with the controls/receipts, not in the per-landing PASS table.

### 1.2 CUT — C leg 10 `SCRATCHMIRROR` (12 → 11)

> `SCRATCHMIRROR: .ufo/waves/round-75/assimilation/validate-receipt.txt shows \`validate --file\` exit 0
> on a mirrored corpus carrying the frozen rows and entries, committed strictly before the
> registry-append commit`

Two things are graded: receipt words, and commit order.

- **The receipt words are free.** Against the in-flight regexes (`leg-mirror-coll.py:96-113`), a 230-byte
  hand-typed file passes every predicate — measured:

```
B/ SCRATCHMIRROR fabricated receipt: p1 True p2 True ids True entries True bytes 230
```

- **The validation itself is already executed elsewhere, on the same bytes.** `CENSUS` runs
  `sources-census.sh validate --file <mat>/corpus/SOURCES.md --today <access_date>` on the landed tree
  (`leg-ground-cited-census.py:131-170`). Measured at base, in a full base tree extracted to scratch:

```
base exit=0
0          # E-code lines
```

  A mirrored corpus carrying "the frozen rows and entries" is byte-for-byte that same content; a second
  leg cannot grade it differently.
- **Commit order** is a process fact with no failing landing in the crit set: a junk landing commits the
  fabricated receipt first and the rows second.

Cut adds no survivor to `CritCCounterVacuity`'s SCRATCHMIRROR row ("**No**", F2 executed the fabricated
marker). Cost: the receipt survives as a committed review artifact; nothing graded is lost.

### 1.3 CUT (with transfer) — C leg 11 `COLLCHECK` (11 → 10)

> `COLLCHECK: reg-ids/staged-ids/collisions files and guard-proof show a planted 1-3-space-indented
> collision found and a 4-space one not found; no adopted lane id is in reg-ids; the map maps
> staged->lane by document for every adopted id`

Item by item against the in-flight implementation (`leg-mirror-coll.py:165-320`):

| Clause | What it grades | Verdict |
|---|---|---|
| guard-proof "show … found … not found" | prose patterns (`positive`/`negative` regexes, `:265-286`) | fabricable (F3 executed); cut |
| `reg-ids`/`collisions` files | counter re-derives both from the base registry and cross-checks (`:204-247`) | self-consistency of derived evidence; a junk landing can emit the same bytes; the content is either base-derived or freeze-derived |
| "no adopted lane id is in reg-ids" | adopted id ∉ base ids | **already double-covered**: `ROWS` requires `base..<lands>` to add *exactly* the frozen row_set, so an id that already exists cannot be "added"; and census `E03 duplicate id` fires — measured: `file E03 S884 duplicate id` (exit 1) |
| "map maps staged->lane for every adopted id" | row_set × frozen map | **freeze-invariant**: both operands come from `git show <freeze>`; no landing can change the verdict |
| map record URL ⊆ row source cell | land row vs frozen map (`:302-320`) | **the only unique, landing-dependent content** → transfer to `REPOINTED` |

Transfer (add to `REPOINTED`, verbatim):

> `for every freeze map record old -> new that the row_set stages on new, the record's URL appears in
> new's source cell under URL-key normalisation (netloc+path); a staged id is never cited alone as a
> lane row`

Removing COLLCHECK as a leg does not let any crit-listed junk through: the duplicate-document gap that
E04 does *not* catch is separate and is closed in §3 below (it is a hook in `ROWS`, not a reason to keep
COLLCHECK). The indent-guard behaviour belongs with the counter's `--selftest` fixtures; the three id
files and `guard-proof/` stay committed as review evidence.

### 1.4 CUT — C leg 13 `INDEX`, the SHONEN clause (clause only; C stays at 10)

Frozen text, the middle clause:

> `, the SHONEN.md:6 registry summary reflects the registry and mined/queued/rejected counts at <lands>,`

This is **already cut in the in-flight counter**, with the L1's authority on the record:

```
leg-index.py:3-4
#   legs[-1]; the SHONEN.md:6 clause was removed from this leg by the L1 before
#   data, SHONEN.md being claim Ca's, so this leg never reads SHONEN.md):
```

So today the frozen text carries a clause the counter does not grade — a second authority of exactly the
kind this seat removes. `SHONEN.md:6` is Ca's ledger surface (pairs L75-01/05/06/07 with
`statement_after` parses and a REPAIR obligation); grading it twice, from two claims, with two different
expected values at two different trees (Ca: `rows: 808`; C after its append: `rows: 817`), is the one
cross-claim line that no single-tree run can satisfy. Delete the clause; Ca's REPAIR owns the line. No
crit survivor depends on it (the crit's INDEX row is about ghost rows and topic strings, not SHONEN).

**Freeze blocker this creates if not fixed:** claims.json must be amended to match, because
`leg-frozencfg.py:271-278` asserts `cfg["frozen_legs"] == claims.legs` and reports any divergence.

### 1.5 CUT (transfer) — C leg 4 `GATE`, the reject half

> `… and >=1 admit and >=1 reject; every reject row of a probed URL carries its probed URL, reason and
> flip`

`REJECTS` already requires each refused row and file to carry reason and flip (§2 word fixes). Two legs
grading the same cells of the same file is duplicate authority. Move the clause into `REJECTS` (where the
refusal set is enumerated), keep only ">=1 admit" in `GATE`. Leg count unchanged; nothing is let through.

### 1.6 CUT — Ca leg 7 `NOSTUB` (12 → 11)

> `NOSTUB: every correction row carries id + old token + new token + the re-derivation command and no
> header-field placeholder token in {TODO, TBD, FIXME, XXX, n/a, ?} or <...>`

`ANNOTATE` already requires the row to name the pair id, the base stated token and the observed token, and
requires the row's re-derivation to reproduce the observed token. Id + old + new + command is therefore
implied on every *graded* row, and a placeholder cannot equal a parsed token. The only residue is the
placeholder ban on rows nobody grades (REPAIR rows, if any). Fold that sentence into `ANNOTATE` (§2 row
14) and delete the leg. No `CritCaVacuity` finding depends on NOSTUB (F5 is about ANNOTATE's containment
test, which §2 row 14 fixes).

### 1.7 CUT — Ca leg 6 `R1EXEMPT` as a graded leg (11 → 10), kept as a selftest

> `R1EXEMPT: fixtures committed with the freeze prove the exemption both ways: …`

Both trees it grades are committed **with the freeze**. A landing cannot make it red or green; the claim's
own control text says so ("R1EXEMPT green (its G/R fixtures are present and re-run)"). It is a
counter-quality control, and the correct home for a counter-quality control is the counter's `--selftest`
(the round-74 counters have one; `accept-ca.py:2488` runs mutants there) or the controls receipt — not a
slot in the 12/12 PASS table that is green at every tree including the do-nothing one.

Enforcement is *not* lost: the same two fixture runs become selftest items, and the do-nothing control
keeps reporting them. Cost of keeping it as a leg: one permanently-green row in the PASS count, i.e. a
claim that reports a check no landing can fail.

### 1.8 CUT — Ca leg 5 `APPENDONLY`, the fleet clauses

> `; the fleet round-74 report at the ledger's fleet_pin is byte-identical to the blob and sha256 named in
> ledger.json, and the lane has no uncommitted fleet-root bytes`

Measured, both trivial or impossible to change from the lane:

```
$ git -C /home/vgpnk/Projects/shokunin cat-file -p 3a74016…:.ufo/reports/round-74/kotodama.md | sha256sum
354273bc972d8b86a012a8aac024618d5defa73e72ea1eae5a960fdf64f84107  -      # == ledger.fleet_report.sha256
$ git rev-parse 3a74016…:.ufo/reports/round-74/kotodama.md
5df0118b9152a23830cc9f0912c004c095c90459                              # == ledger.fleet_report.blob
$ git -C <clone at base> status --porcelain
                                                                       # empty — the clause is a tautology in a clone
```

The fleet report lives in the **fleet** repo. The lane cannot write it (the L1 commits the lane; this seat
is forbidden the fleet tree), so "byte-identical at the pin" is a premise that no landing can break, and
"the lane has no uncommitted fleet-root bytes" is true by construction of every materialised clone. Ca's
`before` clause (f) also has no ledger pair and no leg of its own; it is claim prose. Delete the two
clauses, and delete `ledger.fleet_pin` + `ledger.fleet_report` (dead config once nothing reads them). The
verified hashes above can go into the freeze receipt if the L1 wants the premise on the record.

---

### 1.9 CUT — clause-only deletions (leg count unchanged, listed for completeness)

- **Ca `LEDGER`, `>= 10 unique pairs`** — `BASEMISMATCH` already requires "the number of such pairs >= 10"
  on a strictly narrower set (pairs that are red at base and observable). The ledger declares exactly ten
  pairs today; the floor adds no content beyond the stronger one.
- **Ca `SEPARABLE`, trailing `; every observation is the token the pair's observe_cmd returns in the clone
  at the revision the ledger names`** — BASEMISMATCH, REPAIR and ANNOTATE each compute that same token;
  the clause is the third statement of one property, and it is the statement with the weakest enforcement
  (no clone is named). Delete it; keep the read-set clauses.
- **C `REPOINTED`, `no unrelated staged id is preserved`** — restates the campaign-id clause with an
  undefined adjective; replacement in §2 row 7.
- **C `INDEX`, the SHONEN clause** — §1.4; already absent from the implementation.
- **C `GATE`, the reject half** — §1.5; moved into `REJECTS`.
- **Ca `APPENDONLY`, the two fleet clauses** — §1.8.

Recommended **not** cut: Ca `REPAIR`'s lesson rows for S899/S900 (§5).

---

## 2. Words the counters cannot compute — exact replacements

Each row: the frozen words, why they are uncomputable (with the measurement), and the replacement text to
paste. Replacements are written to be mechanically decidable by the leg tables already in flight.

| # | Where | Frozen words | Why not computable | Exact replacement |
|---|---|---|---|---|
| 1 | C `ROWS` | `a cadence-only recheck cell` | "cadence-only" is not a grammar. The in-flight reading is `_rows_cadence_ok` (`leg-rows.py:21-35`), three lowercase words max — a rule the frozen text never states, and `RECHECK_RE` alone would accept `re-open on 2026-10-23 and …`. Base column vocabulary measured: `365d`×392, `180d`×230, `90d`×18, `on-release`×14, ISO×154. | `a recheck cell matching ^(?:[0-9]+d\|on-release)$ (never an ISO date, never a composite cell)` |
| 2 | C `EVIDENCE` | `(window >= 4096 characters around the quote)` | "around" is unmeasurable; a quote may sit on byte 1 or byte 4095 of a 4096-char window. | `(the stored window is >= 4096 characters and the Gate quote's character span begins at or after 25% of the window's length and ends at or before 75% of it)` |
| 3 | C `REJECTS` | `names each refused staged row and file with reason and flip` | global word presence — F6 executed a single generic reason/flip pair covering every refusal. | `for each refused staged row and file, the reason cell and the flip cell are individually non-empty, neither is -, and the reason names the artifact it was observed on (QUALITY criterion 27); one global reason/flip paragraph satisfies nothing` |
| 4 | C `REJECTS` | `the triage counts of the 40 staged knowledge files adopted/refused` | the two integers are never parsed; "40" is a constant no leg compares. | `an adopted: N / refused: M pair parsed as integers with N + M = 40` |
| 5 | C `GATE` | `+ locator` | locator is prose (`PDF p. 1, English abstract`, `§世界观…, paragraph 1, sentence 2`). | `and a locator cell that is non-empty, not -, and carries a page-level reference matching (?:p\. ?[0-9]+\|§ ?[0-9.]+\|paragraph [0-9]+\|第[一二三四五六七八九十]+讲\|abstract\|heading)` |
| 6 | C `FROZENCFG` | `row set, entry paths, fragments, reject counts and every constant are read from` | "every constant" is an unbounded set the counter cannot enumerate; it can only enumerate what it consumes. | `the frozen constants — row_set ids, entry paths, ground fragments, reject counts, access date, map path, map sha256, frozen leg list — are read from` |
| 7 | C `REPOINTED` | `no unrelated staged id is preserved` | "unrelated" has no definition; and it restates the preceding clause. | delete; make the preceding clause enumerate: `every S-id token in an entry's source: lines is an id in the frozen row_set; every other S-id token in an entry is either a row_set id or a staged id that the frozen map maps to a row_set id` |
| 8 | C `INDEX` | `the last 'Counts checked' footer's total equals the live file count with the per-directory vector 32/32/40/29/24/95; older footers are byte-identical` | "older footers" is a set with no delimiter; "the last" is unambiguous only because a footer block grammar exists (in flight: `_footer_blocks`, `leg-index.py:58-63`). | `the base's Counts checked block sequence is a prefix of the landed one and every base block is byte-identical; the last block's total is the live .md count and its six numbers, in README section order, equal (32, 32, 40, 29, 24, 95)` |
| 9 | Ca `LEDGER` | `no absence-observation pair` | undefined term; Ca's own pairs L75-08/09 are presence pairs whose stated token is the word `absent`, and their parse is the non-regex `"count-presence"`. | `an absence-observation pair is a count pair whose base observation is 0 and whose expected_after is a positive integer; it is never kept` |
| 10 | Ca `LEDGER` | `compiling parse with a capture group` | **the ledger violates it**: L75-08/09 carry `"parse": "count-presence"`, a regex that matches the literal string. Measured: `re.search("count-presence","reports/round-74/evidence/S883.txt:1")` → `None` → the round-74 `observed_token` returns `parse-miss`, i.e. **unobservable**, and BASEMISMATCH ("none is unobservable") fails at base. With `:([0-9]+)$` the same output yields `1`. | add a `pair_type` field: `each pair declares pair_type in {count, presence, token}; parse compiles with a capture group for every type; a presence pair's stated_parse captures absent\|present and its parse captures the count :([0-9]+)$; it is red iff (absent and count > 0) or (present and count == 0)`; and set L75-08/L75-09 `"parse": ":([0-9]+)$"`, `"pair_type": "presence"`, `"observed_at_base": "1"` (not `"present"`) |
| 11 | Ca `ANNOTATE` | `the row's re-derivation command is re-run by the counter and returns the observed token` | F5: round-74 `leg_annotate` uses `token_in(out_text, obs)` = boundary-matched **containment** in raw output (`accept-ca.py:1339`), so `cat` of any file carrying the token incidental to other output passes. | `the counter re-runs the row's re-derivation command in the base-materialised clone, applies the pair's parse to its stdout, and requires exact equality with the observed token; raw-output containment or an extra match fails` |
| 12 | Ca `APPENDONLY` | `exempt ONLY when the change is inside the status, recheck or used-by cell of that row` | a location, not a change: F6's counterexample edits `teaches` and `used-by` on one line and a line-level exemption passes the `teaches` edit. | `each pre-existing row parses into exactly 11 cells in both trees with an identical id and delimiter shape; the row is exempt iff the changed-cell index set is a subset of {8 status, 10 recheck, 11 used-by}; any malformed or ambiguous row fails` (adopt CritR1Exemption's used-by path rule in the same sentence) |
| 13 | Ca `SEPARABLE` | `the telemetry receipts and controls named in this file's Ca section` | "this file's Ca section" has no section marker; the referent is in the claims prose, not in a parseable location. | enumerate: `{reports/round-75/telemetry/controls-ca.txt, junk-ca.txt, accept-ca-74-at-lands.txt, measures-ca-head.txt, selftest-r72-repeat.txt, sweep-red-before.txt, sweep-green-after.txt, measures-ca-combined.txt}` |
| 14 | Ca `ANNOTATE` | (absorbed from `NOSTUB`) | — | append: `and no correction row carries a placeholder token in {TODO, TBD, FIXME, XXX, n/a, ?} or a <...> stub` |
| 15 | Ca `STAMP` | `the receipt carries the stamped/evaluated/measured …` | "the receipt" has an antecedent only in COMBINED (`measures-ca-combined.txt`); STAMP's own receipt is never named. | `reports/round-75/telemetry/measures-ca-head.txt carries …` |
| 16 | Ca `COMBINED` | `invoked with --combined <combined-revision> … carries the Ca-lands stamp and exact combined revision/tree` | no landing creates a combined revision; if the counter synthesises it in scratch, the receipt cites a revision that does not exist in the lane repo, and no later run can resolve it. | `the counter builds the combined tree from <Ca-lands> and <C-lands> in its own scratch clone; the receipt carries both landing revisions and git rev-parse <synthetic>^{tree}; no revision absent from the lane repo is cited` |

---

## 3. The one measured hole that is **not** a leg deletion: "one row per distinct document"

`claims.json` claim C, `after`:

> `Registry 808 -> 817 rows (9 new rows S885-S893, one row per distinct document, IDs by document not by
> occurrence).`

No leg computes this. `CENSUS`'s duplicate check is E04 = duplicate **URL+scope**; the same URL across
scopes is only W04, a warning that does not change the exit status. Measured, on a full base tree with two
rows added that re-adopt S884's document under fresh ids, distinct scopes, `mined`, opened `2026-10-27`,
`30d`, a real `used-by`:

```
m6 exit=0
     # zero E-code lines
file  W04  S885 duplicate url www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html across scopes
file  W01  S885 tierC mined used-by=corpus/knowledge/linguistics/naming-systems.md
file  W04  S886 duplicate url … (same document)
```

A landing that covers one document three times passes every C leg as drafted (`ROWS` never compares URLs;
`REPOINTED` only binds an id to the URL on its own row). This is the junk class `CritCCounterVacuity`'s
REPOINTED row names, and it is **cheaper to close with a hook than to keep COLLCHECK**:

> add to `ROWS`: `no added row's neutral URL keys (neutral_url_keys, which folds a page-level view onto
> its document) intersect the neutral URL keys of any other registry row at <lands> or at base`

Cost: ~12 lines in the in-flight `leg_rows`, no new leg, and no new helper: `norm_url`, `urls_in` and
`neutral_url_keys` are FIXED assembly helpers (`CFG-CONTRACT.md:7-9`), and `neutral_url_keys` is the key
widening SimplifierRows §4.1 already relies on.

---

## 4. Leg-count cost ledger (what must change with the deletions)

| Surface | Current | After cuts |
|---|---|---|
| `claims.json` claim C, `after` | `ACCEPT-C-75: PASS legs=13/13` | `legs=10/10` |
| `claims.json` claim Ca, `after` | `ACCEPT-CA-75: PASS legs=12/12` | `legs=10/10` |
| frozen leg list (`claims.legs`, asserted by `leg-frozencfg.py:271-278`) | 13 / 12 | 10 / 10 |
| `part-main.py:37-51` `LEGS` | 13 entries | drop `("GROUND", leg_ground)`, `("SCRATCHMIRROR", leg_scratch_mirror)`, `("COLLCHECK", leg_collcheck)` |
| `part-main.py` header (`Legs (13)`) and the LEGCOUNT refusal | 13 | 10 |
| `leg-ground-cited-census.py` | GROUND + CITEDLINES + CENSUS | delete `leg_ground` (~68 lines), keep the other two; rename to `leg-cited-census.py` |
| `leg-mirror-coll.py` | SCRATCHMIRROR + COLLCHECK (~321 lines) | retire; ~12 lines of map-URL logic move into `leg-repointed.py` |
| Ca counter (not yet in `parts/`) | 12 | 10 |
| C `do_nothing_control` | "the data legs red and FROZENCFG green" | "ENTRIES/ROWS/REPOINTED/GATE/EVIDENCE/REJECTS/INDEX red and CENSUS/FROZENCFG green" — **measured**: census exits 0 with 0 E-codes at base, so CENSUS is green even at `lands == freeze` |
| Ca `do_nothing_control` | "REPAIR and ANNOTATE red, R1EXEMPT green … FROZENCFG/LEDGER green" | "REPAIR and ANNOTATE red, LEDGER/FROZENCFG green, and `--selftest` green (the R1 fixtures run there)" |
| w1 crit tables | `CritCCounterVacuity` 13 rows; the Ca crit's leg references | 3 C rows and 2 Ca slots disappear; no surviving finding changes |

Two freeze blockers observed while counting:

1. `claims.json` `claims[C].map.sha256` is **`null`**. `leg-frozencfg.py:265-270` compares it with the
   computed map sha and, when empty, notes `the by-document map is uncheckable at this freeze` — i.e.
   FROZENCFG can never be green. Fill it before freeze (the map on disk is
   `.ufo/waves/round-75/assimilation/id-renumber-map.json`, 49,388 B).
2. `claims.json` claim C `legs[12]` still carries the SHONEN clause the L1 already removed in code
   (`leg-index.py:3-4`) — see §1.4.

### 4.1 Text / implementation divergences found while counting (frozen text must equal the graded contract)

A rule the implementation grades but the frozen text does not state is a second authority — the same defect
as an uncomputable word, in the other direction. Three such rules are live in the wave-2 parts:

1. `leg-rows.py:160-163` fails a row that "is cited by no admitted entry (orphan row)". The frozen `ROWS`
   text only says `used-by exactly the admitted entries whose source: lines cite it`, which an empty
   citation set satisfies with `used-by: —`. Either add `each added row is cited by at least one admitted
   entry` to `ROWS` or drop the implementation rule. (Census `E11` also fails a `mined` row whose `used-by`
   is `—`, measured, so the substance is covered by `CENSUS`; the text still needs the clause.)
2. `leg-index.py:24-30` (reading R2) requires the entry's row to be the only row for that basename
   *anywhere in README* and inside the myth-symbol section; the frozen text says only "in the myth-symbol
   section". State the stricter reading, or a duplicate row outside the section is counter-red but
   text-green.
3. `leg-ground-cited-census.py:131-143` notes that `--file` resolves every `used-by` against the registry's
   parent, so the graded registry must sit at `<mat>/corpus/SOURCES.md`; measured, the identical bytes in a
   bare directory produce 741 E-code lines. Freeze the invocation path in the `CENSUS` clause (same words
   as §5).

---

## 5. What I did **not** cut, and why (the frontier's edge)

- **C `ENTRIES`** — its "length-and-shape gate only" self-description is honest and it is the only
  existence/word-floor check on the three entries; without it the orphan-row hole SimplifierRows §2.2
  identified (a row no entry cites) reopens. Keep (the orphan rule belongs in `ROWS`, §4.1 item 1).
- **C `EVIDENCE`** — load-bearing and currently biting: the staged lesson's own Gate row for S888 records
  "the anchor quote is **not** in that stored window (note 2)", which the leg's window rule rejects. A leg
  that rejects the current staged artifact is not vacuous. Keep; only fix "around" (§2 row 2).
- **C `CENSUS`** — the only mechanical guard for `E03`/`E04`/`E12` (measured: duplicate id, duplicate
  URL+scope, row outside `## Registry`) and for used-by path existence (`E11`). Keep, with the invocation
  path frozen as in §4.1 item 3 — the materialisation path is part of the leg's meaning, not an
  implementation detail.
- **C `CITEDLINES`, C `FROZENCFG`, C `GATE`'s quote-size limits** — each gradable and each catches
  something the crit did not show surviving (CITEDLINES is the crit's own repair #1; FROZENCFG is the
  freeze-tamper leg; the quote caps bind).
- **Ca `REPAIR`'s lesson rows for S899/S900** — duplicate content of `ANNOTATE`'s SCORECARD rows, but the
  lesson carries the reasoning, and provenance marked historical is never deleted by this seat. Recommend
  keeping the clause; if the L1 wants the round's leg shorter, this is the one duplicate clause that can
  go without any junk landing (the same old→new tokens are still graded at SCORECARD).
- **Ca `RECEIPTS`** — it re-executes an older counter and compares the committed stdout to its own run, so
  the receipt is not fabricable; its landing-dependent part (the receipt exists, verbatim) is real.
- **Ca `COMBINED`, Ca `BASEMISMATCH`, Ca `LEDGER`'s structure rules** — COMBINED is the only leg that
  grades the two landings' exemptions on one tree (the merge conflict is real: both claims write
  `SHONEN.md:6`), and BASEMISMATCH/LEDGER are the anti-vacuity floor for the whole calibration claim. Keep
  all three; fix COMBINED's unverifiable revision referent (§2 row 16) instead.

---

## 6. Evidence trail (every measurement cited above)

Scratch `/fast/scratch/hyaku/kotodama-r75/SimplifierClaims/` (recreated 16:56 after another seat's
cleanup deleted the shared parent; removed before yield).

1. Base facts, from `git show f556d10…`:
   `SHONEN.md:6` = `(412 rows after round 56 — 367 mined, 35 queued, 10 rejected`;
   registry rows `808`, last ids `S880…S884` (so `S885…S893` are free);
   knowledge `.md` total `249`; partition `civilizations 95, culture-material 40, linguistics 32,
   synthesis 29, myth-symbol 29, verification 24`;
   README headings `30/29/36/29/24/95` at lines 344/376/407/447/479/505; index rows `247`;
   `Counts checked` blocks beginning at 751 (`243 files; 30/29/36/29/24/95`) and 815
   (`249 files; 32/29/40/29/24/95`).
2. Census on the base registry, full base tree: `base exit=0`, `0` E-code lines; W04 warnings only.
   Re-run from `/` with an absolute `--file` into the same tree: `exit=0`, `0` E-codes (path discipline).
3. Census mutants: duplicate id → `E03`; duplicate URL+scope → `E04`; row-shaped line after
   `## Registry` → `E12`; duplicate document under a fresh id with a different scope → **`exit=0`, W04
   only** (the §3 hole).
4. Fabrication checks: GROUND receipt (27 bytes → all predicates true); SCRATCHMIRROR receipt (230 bytes →
   all four predicates true).
5. Tautology and pin checks: clone at base → `git status --porcelain` empty; fleet report blob
   `5df0118b…` and sha256 `354273bc…` equal the ledger's fields.
6. Ledger observability: `git grep -c '非凡特性来自最初造物主' <base> -- reports/round-74/evidence/S883.txt`
   → `f556d10…:reports/round-74/evidence/S883.txt:1`; `parse "count-presence"` → no match (parse-miss),
   `parse ":([0-9]+)$"` → `1`; `stated_parse "\b(absent)\b"` → `absent`.
7. Code readings (state at 16:51–16:55, parts are in flight):
   `part-main.py:37-51` (13-leg table), `leg-ground-cited-census.py:19-170` (GROUND receipt predicates,
   CENSUS `--file` invocation), `leg-mirror-coll.py:87-320` (SCRATCHMIRROR regexes, COLLCHECK
   re-derivations, guard-proof positive/negative regexes), `leg-index.py:1-63` (SHONEN clause removed;
   footer-block grammar), `leg-rows.py:21-163` (cadence reading, orphan rule), `leg-frozencfg.py:254-278`
   (map sha and frozen leg-list assertions), `reports/round-74/accept-ca.py:838-1000,1290-1340` (observe /
   token / containment semantics), `reports/round-74/accept-c.py:183-330,746-1066` (round-74 leg shapes).

No tool install or upgrade (nothing was needed: `git`, `python3`, `awk`, `bash` sufficed). No network
fetch. No file outside this report was written; no lane, fleet, jj/git state, `.ufo/state`, or index was
touched.
