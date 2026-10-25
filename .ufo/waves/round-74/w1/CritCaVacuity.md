# CritCaVacuity — claim Ca: vacuity and self-reference attack (round 74, w1 FALSIFY)

Seat: CritCaVacuity. 2026-10-25. Leaf: no delegation, no `task`, no background jobs. Lane
`/home/vgpnk/Projects/shokunin/kotodama-shokunin` (base `f7104cbce186bc2e1522abf0cfd619cc834628bb`,
worktree carries the six inherited round-73 w2 seat files — read, never written). Draft attacked:
`reports/round-74/claims.json` claim **Ca** (`frozen: null`, so every finding is a pre-freeze text
edit). Reference implementation: `reports/round-73/accept-ca.py` (r3, sha256
`222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89`) — the round-74 counter does not
exist yet (`ls reports/round-74/accept-*.py` → absent), so every leg I attack is the drafted
*sentence*, with the r73 code read as the baseline any successor will inherit. Mutation fixtures:
`D=/tmp/CritCaVacuity/mut.yxLvJq` (`mktemp -d`; `git -C "$D" rev-parse --show-toplevel` == `$D`
verified before the first commit; clone `$D/lane`; throwaway identity `CritCaVacuity throwaway
<crit@throwaway.invalid>` used only inside the clone). Receipt-determinism runs in a second scratch
clone `/tmp/CritCaVacuity/lane`. No lane write except this file. No fetch made (no live page is in
this seat's scope, so QUALITY 21/22 UA records do not apply); nothing installed; pacman untouched.

## 0. Verdict

The draft's Ca predicate is **not vacuous in the "passes without doing anything" sense** — I verified
its hardest reachable obligation is satisfiable (both round-73 PASS-at-lands receipts can be
produced; §4). But it admits a **fabricated after-state**: six executions below (X1–X6) show a ledger, a
correction row, a repair and a receipt-passing configuration that satisfy the drafted legs while the
underlying statement is false, the row is a stub, or the observation is a constant. Three of the
drafted sentences are *internally inconsistent with each other*, which is the more dangerous class:
a counter that implements one sentence is red, a counter that implements the other is green on
garbage (R73 F1 "implemented wider/narrower than frozen", one level up).

| # | drafted sentence | contradictory or under-specified because |
|---|---|---|
| i | REPAIR: "the truth observed at `<lands>`" | SEPARABLE blesses count pairs whose `observe_cmd` pins an older revision; for those, the truth is *not* observed at lands (X4). |
| ii | REPAIR: "statement re-read at `<lands>` (last occurrence)" | "(last occurrence)" is a **regression** against r73's first-match read: it re-opens the shadow-truth append (X6). |
| iii | APPENDONLY: "in-place edits permitted only in files a ledger REPAIR pair names", measured "base..`<lands>`" | a range diff cannot see a line added *and* removed inside the range, so the round's own correction rows and telemetry are unprotected (X2); and the r73 code's authorization was narrower (INPLACE_PATHS + footer/registry span), not "any REPAIR-named file". |
| iv | LEDGER: "compiling `parse` with a capture group" | compiling ≠ matching; a parse-miss is warn-only and the raw stdout is used, and a miss still counts as a red pair (X1). |
| v | ANNOTATE: "naming the pair id, the base stated token and the observed token" | substring-anywhere row matching: a row that merely *mentions* the id serves as evidence, and cell roles are not checked (X2, X3). |
| vi | ANNOTATE: "the row's re-derivation command re-runs inside the counter" | the phrase has no schema (free-text row), so the counter will match the ledger's `rederive` string and re-type the observation; and executing an unconstrained author string (`echo 245`) returns the token (X5). |
| vii | TRACKED: "byte-equal to the worktree-at-base content recorded in the ledger (sha256)" | the recorded sha is computed from an unversioned worktree, so it authenticates nothing older than the freeze (X7, mtimes). |

Smallest safe correction is per-item in §3; all of them are text edits that fit before the freeze.

## 1. Executed counterexamples

All mutants are children of the round-73 lands `2d1cd9140d3a6c42296d71e4f29587582a4a88c0` and were
graded with the r3 counter at the mutant commit:
`python3 -B reports/round-73/accept-ca.py --root . --lands <mut> --fleet-root
/home/vgpnk/Projects/shokunin --main <mut>` (`--main` only so STAMP's `measured == lands` holds for a
detached mutant; the frozen command has no `--main`, so a mutant not on `main` dies on STAMP
regardless — harness note, not a detector response). Baseline before any mutant:
`ACCEPT-CA-73: PASS legs=9/9`, exit 0, at `2d1cd91`.

| # | mutant commit | mutation | drafted leg it should trip | observed |
|---|---|---|---|---|
| X1 | `148e5499c45a987b9a8f9541d7c83aed417f4627` | L01 `parse` := `^(\d+)-NOPE$` (never matches) | LEDGER (compiling parse) / BASEMISMATCH | **PASS 9/9**; `NOTE L01 parse-miss (raw stdout token used)` |
| X2 | `bdd74b5d622f5bb8f17bfa777dede77991e1caba` | delete the `| L01 | 243 | …` correction row from SCORECARD | ANNOTATE, NOSTUB, APPENDONLY | **PASS 9/9** |
| X3 | `9ac847e13fc0728d337059b2641a03ce9ff8aa28` | swap L06 cells to `| L06 | FAIL | PASS |` (the opposite of the truth) | ANNOTATE / NOSTUB | **PASS 9/9** |
| X4 | `c1e56fc3476993c6e98d69970f0063d4d531375d` | L01 → REPAIR, statement `README:732` rewritten 243→245, truth from the pinned `8841ad3` count | REPAIR ("truth observed at lands") | **PASS 9/9** while the lands tree holds **247** `.md` files |
| X5 | `da4629cea720ed04bb4c7cc66ec8a2bef825b855` | L01 `stated_parse` removed, `stated_token` := `3`; row := `| L01 | 3 | 245 | <pasted ledger rederive> | - |` | LEDGER / ANNOTATE / NOSTUB | **PASS 9/9** |
| X6 | `b32d4b502fe191a2b9db918a93cd3d01b1264e80` (on `c24f6933139a512a6396801133ebcf7f4ec12c85`) | SHONEN:6 reverted to `:468`/`:522` **and** a shadow line appended; L04 `statement_after.parse` := `(?s).*:(\d+)` \(Error patterns\)` (the drafted "last occurrence") | REPAIR | **L04 green** with `SHONEN.md:6` still stale (`green=['L04','L08']`) |

### X1 — `parse` is decorative (answers Q1: pairs can be red for free)

```
LEG PASS LEDGER
     NOTE L01 parse-miss (raw stdout token used)
LEG PASS BASEMISMATCH
ACCEPT-CA-73: PASS legs=9/9
```

`leg_basemismatch` (`accept-ca.py:552-570`) appends a parse-miss to `misses` **and then** counts it
as a mismatch (`if tok is None or norm(tok) != norm(obs)`), and `leg_repair` / `leg_annotate` /
`leg_nostub` never read `parsed` at all. So ten pairs whose `parse` never matches satisfy
"≥ 10 red pairs at base" while no observation was ever parsed; the observed token is
`norm(stdout)[:200]`. The draft keeps the hole: it requires only that `parse` *compile*.

### X2 — a deleted correction row is invisible, and a mention substitutes for it (answers Q2, Q4)

```
removed 1
LEG PASS ANNOTATE
LEG PASS NOSTUB
LEG PASS APPENDONLY
ACCEPT-CA-73: PASS legs=9/9
```

Two mechanisms, both executed:

1. **Row interchangeability.** `row_names_id` (`:619`) matches the id anywhere in the row and
   `leg_annotate` (`:624-654`) only demands `stated in row and observed in row`. The surviving L03
   row says "same 243 → 245 drift as L01 …", carries L01's `rederive` string as a prefix, and
   therefore serves as L01's evidence after L01's own row is deleted. The draft's "a row naming the
   pair id" does not change this.
2. **Range-diff blindness.** `git diff --numstat 8841ad3 bdd74b5 -- SCORECARD.md` → `15 0` (0
   removed) while `git diff-tree -r --numstat --no-commit-id bdd74b5` → `0 1 SCORECARD.md` (the row
   was removed). The row was added
   in round 73 and removed by the mutant, both inside `base..lands`, so `numstat_removed` sees
   nothing. The round-74 correction section is authored *inside* this round: every row of it is an
   in-range addition, so the drafted APPENDONLY leg protects none of the rows the claim is about.
   (This is exactly CritAppendOnly §0's structural finding, still unaddressed by the draft text.)

### X3 — token roles are not checked (answers Q2)

```
LEG PASS ANNOTATE
LEG PASS NOSTUB
LEG PASS APPENDONLY
ACCEPT-CA-73: PASS legs=9/9
1417:| L06 | FAIL | PASS | grep -ho 'ACCEPT-CA-72: [A-Z]*' ...
```

The row now asserts old=`FAIL`, new=`PASS` — the inverse of the filed truth — and both legs stay
green because containment is role-blind (the note cell quotes both tokens). A stub row is not even
needed: any row containing the two strings qualifies.

### X4 — a REPAIR can be green while its truth was measured at a revision that does not contain the repaired bytes (answers Q3)

```
PAIR L01 disposition=REPAIR stated_at=corpus/README.md:732 stated='243' observed_base='245' observed_lands='245'
LEG PASS REPAIR
LEG PASS APPENDONLY
ACCEPT-CA-73: PASS legs=9/9
--- actual count at this lands ---
247
Total knowledge entries: 245.
```

The repaired statement at lands says 245; the lands tree holds 247 `.md` files. The pair is green
because its `observe_cmd` carries the hard-coded revision `8841ad3…` (r73's L01/L02/L03 shape), so
"observed_lands" is a constant of an older tree. The draft does not forbid pins and its SEPARABLE
leg *requires* pins for count pairs ("count pairs measure at the pinned base revision so landing C
cannot move them") — so the two sentences cannot both be true for a count pair, and REPAIR's "truth
observed at `<lands>`" is false for every pinned pair. r73 avoided the consequence only because all
three REPAIR pairs happen to grep the graded clone; nothing in the predicate says so.

### X5 — degenerate stated token + a row pasted from the ledger (answers Q1, Q2)

```
stub: | L01 | 3 | 245 | git ls-tree -r --name-only 8841ad3… corpus/knowledge (count the .md paths) -> 245 | - |
LEG PASS LEDGER
PAIR L01 … stated='3' observed_base='245' observed_lands='245'
LEG PASS BASEMISMATCH / REPAIR / ANNOTATE / NOSTUB / APPENDONLY / SEPARABLE / TRACKED / STAMP
ACCEPT-CA-73: PASS legs=9/9
```

`stated_token` overrides `stated_parse`, and LEDGER only asks that the token be **anchored in**
`stated_text` — `"3"` is a substring of `"Total knowledge entries: 243."`. A one-character token
makes the pair red for free, and every containment check then passes on a one-character match. The
row is the pure copy Q2 asks about: id + the two tokens + the ledger's own `rederive` string + `-`.
The draft's only defence (execute the row's command) cannot distinguish this row from a real one
when the command was copied (see Q2/Q6).

### X6 — "(last occurrence)" re-opens the shadow-truth append (answers Q3)

Without the ledger edit, MH (`c24f693`) is killed (REPAIR red: first-match reads `:468`). With
`statement_after.parse` forced to last-match — i.e. implementing the draft's parenthetical —
`green=['L04','L08']` and `SHONEN.md:6` still reads `:468`. (The leg is red overall only because
L05's parse was deliberately left first-match, to isolate the mechanism on L04.) The drafted
"(last occurrence)" is therefore strictly *weaker* than r73's default and is the fix instruction for
the M4 survivor.
Note also that this mutant removes a line from `SHONEN.md`, a path in neither `APPENDONLY_FILES` nor
`INPLACE_PATHS`: `LEG PASS APPENDONLY` (F3 in CritAppendOnly, still true of the draft's set).

### X7 — "inherited evidence committed unchanged" is not what the TRACKED leg can show (answers Q5)

The six paths, worktree fingerprints, and base status (lane, read-only):

```
2026-10-25 20:47:11  41013  290a6ccd839cb8cd  M  .ufo/waves/round-73/w2/CritEntryAmendFinal.md   (base blob eeb3344773b4632d)
2026-10-25 20:41:11  37204  dfc8fe0d2c54442b  M  .ufo/waves/round-73/w2/ExecSelftestAll.md      (base blob 20df0f0b12423adf)
2026-10-25 20:37:36  23535  db254d8896d7cbce  M  .ufo/waves/round-73/w2/ScribeLogScorecard.md     (base blob 7fd5ae056e8e74b3)
2026-10-25 20:41:42  20039  9469d4d689aeb1f3  M  .ufo/waves/round-73/w2/SimplifierEntries.md      (base blob 5afdac54dbcbb579)
2026-10-25 20:37:02  10810  079728a53490714a  M  .ufo/waves/round-73/w2/drafts/log-entry.md       (base blob 3e9af53d7c848e20)
2026-10-25 20:47:30  26043  7d14591923aff7b1  ?? .ufo/waves/round-73/w2/RevengerOrigins.md       (untracked at base)
```

Facts that bound the honesty claim:

- The lane's last round-73 commit is `c1b5b47` at **20:36:38** -0300; the driver logged
  `2026-10-25T20:43:58-03:00 complete kotodama round=73` (`.ufo/watchdog.log:1441`). Two of the six
  were written **after** the round-complete line (20:47:11 and 20:47:30); the later one is
  `RevengerOrigins.md`, whose seat the round-73 report records as "returned no report by filing
  time". So at least one file is output of a seat that never returned, written after the driver
  stopped watching.
- No independent copy exists: the files have never been committed in these bytes, the round-73
  closure spot-check recorded names only (no hashes), and the ledger's sha256 will be computed from
  the same worktree it is meant to authenticate. The leg therefore proves "no write **after the
  freeze**", not "unchanged since round 73".
- Five of the six are **already tracked at base**; only `RevengerOrigins.md` is not. The claim's
  `after` sentence "the round-73 w2 seat files tracked" is therefore satisfied at base for five
  paths and must not be used as the predicate (the draft's leg text is right; the after-text invites
  a reader to score it as already true).
- The race the item asks about is real but lands on the other side: TRACKED evaluates the **tree at
  `<lands>`**, so a sibling seat that re-writes any of the six after the lands commit leaves the
  claim green and the worktree dirty — the exact round-73 recurrence, invisible. Conversely, a
  sibling write between freeze and the lands commit *does* turn TRACKED red, failing the claim for a
  reason the owner cannot repair at lands.

## 2. Direct answers

**(1) Can the ledger be authored to pass trivially?** Yes, in four ways, all executed or read from
the r73 code: (a) pairs made red by a degenerate/overridden stated token (X5) — nothing requires the
stated token to be parsed from `stated_text` or to have the same value-shape as the observation;
(b) pairs red on a parse-miss (X1); (c) pairs whose observation has no binding to the statement's
subject — the draft never says the `observe_cmd` must read the statement's subject, so a number can
be compared with an unrelated number (r73's `wc -l /dev/null` → `0 /dev/null` survivor M2b is the
degenerate case; the draft's "read-only allowlist" is a *program* allowlist and does not close it);
(d) **circular truth** (r73 survivor M3b): the author appends the expected token to an append-only
file this round and greps it back — at base the token is absent (red), at lands the append supplies
it, and no leg reads provenance. "Pairs that already match" are ruled out by the `>= 10 red`
requirement, but only if the red count is measured (it is) and not inflated by (a)/(b).

**(2) Can an ANNOTATE row be a stub copied from the ledger?** Yes. The draft's four required
elements are all satisfiable by copy: id, both tokens (the ledger holds both) and the re-derivation
command (the ledger holds it). Two additives are needed to make the row a *record*: the row's id must
be the row's **id cell** and the tokens must be in the **old**/**new** cells (kills X2, X3); and the
command must be the row's own **argv** cell, executed by the counter, with an output token equal to
the observed token, on the same allowlist as `observe_cmd` and not equal to that pair's
`observe_cmd` (kills the `echo` re-type). As drafted, "the row's re-derivation command re-runs inside
the counter" cannot even be located deterministically: the r73 ledger's `rederive` is prose
(`"… (count the .md paths) -> 245"`), so a counter will fall back to matching the ledger's string —
and then it is the *ledger's* command that runs, not the row's.

**(3) Does REPAIR admit a receipt produced at a revision that does not contain the repaired bytes?**
Yes — X4. Two doctored readings of "receipt": (a) the *observation* may be taken at a pinned older
revision, so the repaired statement at lands can be false of lands and still green; (b) the
*statement* may be read by a last-occurrence search, so the stale line at `stated_at` can remain
while an appended shadow line carries the truth (X6). The draft's own SEPARABLE sentence mandates the
pin for count pairs, so (a) is not hypothetical. Fix: REPAIR pairs must observe the graded revision
(no 40-hex pin in `observe_cmd`), must declare `measured_at`, and must read the statement at the line
`stated_at` names (or the line the repair diff touched) — never a first/last search.

**(4) Does APPENDONLY's file set cover every file the repairs touch?** No. The set
(`LOG.md`, `SCORECARD.md`, `corpus/lessons/round-73.md`, `corpus/lessons/round-72.md`, the fleet
round-73 report) omits, at least: `reports/round-73/telemetry/**` (the witness side of pairs — the
M10 in-place receipt edit is still open), `reports/round-73/counter-revisions.md`,
`.ufo/waves/round-73/assimilation/**` (F2's 127-line post-grade rewrite was green), `SHONEN.md`
(the only base..lands removal in r73, and it is invisible because it is in neither list — X6), and
`corpus/lessons/round-74.md` (this round's own Gate/Mistakes file). Worse than omission: the
`base..<lands>` range-diff *method* cannot protect anything the round adds, including the correction
rows themselves (X2) and the new telemetry. And the exception "in-place edits permitted only in files
a ledger REPAIR pair names" is a global invariant that no list-based implementation can enforce;
written literally it also lets a REPAIR pair naming any path (e.g. `QUORUM.md`, `corpus/QUALITY.md`)
authorize arbitrary in-place rewrites there. r73's implementation was *narrower* than this sentence
(path must be in `INPLACE_PATHS` and the hunk must fall in the authorized span) — the draft widens
the rule, the R73 F1 direction again.

**(5) The TRACKED leg and the race.** See X7. The leg is a tautology over an unversioned worktree
(surface: "no write after freeze"), it cannot distinguish seat output from any other bytes present at
freeze, two of the six post-date the round-complete line, and it reads the tree rather than the
worktree so post-lands writes are invisible. Smallest fix that makes the sentence honest and removes
the race: materialize the six into the **freeze commit** (or write their blobs with `git hash-object
-w` at freeze and record the blob ids), then TRACKED compares the lands blob to the freeze blob; add
a one-line provenance header inside each file (as CritAppendOnly F8 asked for the round-72 pair); and
reword the claim to "committed as inherited; content authenticated by the freeze-time blob, not by
the seat's original output".

**(6) Can a receipt be forged by a counter that prints PASS?** Yes, two levels. (a) The receipt is
text: `tools/check-receipt-seq.py` default mode checks header equality, `tree == <rev>^{tree}` and
`counter sha == sha256(counter)` and nothing else; the draft's RECEIPTS/STAMP legs likewise only read
headers, so a hand-written file with the five header lines and the line `ACCEPT-CA-73: PASS legs=9/9`
passes. (b) A patched counter ("prints PASS") is caught only if the receipt's counter-sha is compared
to the *committed* counter blob — a forger who runs a patched copy and pastes the committed sha into
the header defeats a header-only check. `stamped==evaluated==measured==<lands>` is also degenerate in
the draft: r73's `measured` was an independent observable (lane `main`), and the draft fixes all
three to `<lands>`, so the triple-equality becomes "the counter echoed its argument three times"; the
only non-self-referential facts left are `tree` and `counter sha256`. The one check that cannot be
forged is re-execution, and I verified it is implementable (§4: both receipts are byte-deterministic
except four tmpdir lines).

## 3. Ranked tightenings (≤8, smallest first)

Each is a replacement sentence for the corresponding draft leg; none changes the claim's scope.

1. **LEDGER — pair integrity (closes X1, X5; Q1).** Replace "compiling `parse` with a capture group …
   stated token anchored in it" with: "`stated_parse` is required and its group 1 is the stated token
   (no `stated_token` override); the match must lie on the `stated_at` line; the token is
   boundary-matched (`(?<![0-9A-Za-z])tok(?![0-9A-Za-z])`) and has the same shape class as the
   observed token (digits↔digits, one of a declared status word set↔same set). Each pair declares
   `subject` (a tracked path/glob); the `observe_cmd` must read bytes under `subject` at the graded
   revision, and `parse` must match at base and at lands — a parse-miss fails the leg."*
2. **BASEMISMATCH — no free reds (closes X1; Q1).** "…at the base revision every pair is red
   (`mismatches == len(pairs)`), parsed, observable, ≥10 pairs, and ≥10 **distinct**
   (`subject`, stated token) combinations; a pair declared green at base contradicts the claim's
   before-state."* (The draft's `before` says "every listed pair red"; the leg says only "≥10 red" —
   make the leg carry the stronger sentence.)
3. **REPAIR — lands-measured and line-anchored (closes X4, X6; Q3).** "Every REPAIR pair carries
   `statement_after` (`path` + `parse`), and `expected_after` is forbidden (or must equal the
   statement token). The statement is read at the line `stated_at` names (after a repair: the line
   the base..lands diff touched) — never a first/last-occurrence search. `observe_cmd` must not
   contain a 40-hex revision: a pair that pins is ANNOTATE-only and declares `measured_at: <rev>`;
   for REPAIR the observation is taken in the clone materialized at `<lands>` under a name that
   cannot be overridden by the worktree. **Base-attestation:** every path an `observe_cmd` reads
   must exist at base, and must be byte-identical at base and lands unless it is the pair's own
   `stated_at` subject under repair — so the truth cannot be a token the round itself appended
   (r73 survivor M3b)."*
4. **ANNOTATE + NOSTUB — fixed row schema, role-aware (closes X2, X3; Q2).** "The
   `## Corrections — round 74` table has exactly five columns; cell 1 equals the pair id (or
   `- <id>`), cell 2 equals the base stated token, cell 3 equals the token observed at
   `measured_at`, cell 4 is the re-derivation argv JSON, cell 5 is free. A row is evidence for one
   pair only; a mention of the id in note text is not a row; tokens must match cells exactly
   (boundary-matched, not substring)."
5. **Re-derivation execution is constrained (Q2, Q6).** "Cell 4 is an argv list on the same allowlist
   and shell-construct ban as `observe_cmd`; the counter executes it in a clone at the declared
   `measured_at` and requires its parsed token to equal cell 3; it must not be textually equal to
   any pair's `observe_cmd`; if the executable is a tracked script, the script's blob must be
   byte-identical at base, freeze and lands (a script edited this round can be a constant printer)."
6. **APPENDONLY — whole-tree, per-commit, derived set (closes X2, X6, X4's witness side; Q4).**
   "(a) Whole tree: `git diff --numstat base..<lands>` shows 0 removed lines on **every** path except
   paths a REPAIR pair names in `stated_at`. (b) Per commit: for each commit in `freeze..<lands>` the
   correction table is monotone (rows appended, never removed or edited) and no path under
   `reports/round-74/telemetry/` shrinks or disappears — else a row/receipt added this round is
   unprotected. (c) Protected set = the four declared paths + the fleet report **+ every path any
   pair's `stated_at`/`observe_cmd`/`rederive`/row reads or cites + `reports/round-73/telemetry/**`,
   `reports/round-73/counter-revisions.md`, `.ufo/waves/round-73/assimilation/**`**. (d) Precedence:
   the protected set is unconditionally zero-removal; the REPAIR allowance never applies to it."
7. **RECEIPTS — re-execute, don't read (closes Q6).** "For each committed round-73 receipt the counter
   (i) checks `counter sha256` against `sha256(<blob of the counter path at the receipt's measured
   revision>)`, (ii) materializes a fresh clone at that revision, re-runs the counter, masks only
   tmpdir occurrences (`^# clone:`, `^# base-clone:`, `^# materialized:`, `clone=/tmp/…`, the census
   `last-line=…/corpus/SOURCES.md` path) and requires the receipt body to be **byte-equal**, and
   (iii) requires the PASS line and legs count to match the fresh run. A header-only check is
   forgeable (I verified the bodies are otherwise deterministic, §4)."*
8. **TRACKED — freeze-anchored provenance, race-free (closes X7; Q5).** "The six paths are committed
   (or their blobs written and recorded) in the freeze commit; TRACKED requires the lands blob to
   equal the freeze blob (and non-empty), and the worktree at grading to be clean for those paths.
   Five of the six are already tracked at base; only `RevengerOrigins.md` is untracked, so the leg
   must not be worded "tracked". Each file carries a one-line provenance header: produced in
   round-73 w2, written into the worktree after the round-73 push (two files after the
   round-complete line), committed unchanged from the freeze blob, content not otherwise
   authenticated."

If only one can be taken: **#3** (REPAIR at lands, line-anchored) and **#6** (whole-tree/per-commit
append-only) carry the most weight, because they close the two legs the claim's own corrective value
rests on; **#7** is what makes defect 2 (missing receipts) mean anything.

## 4. Verified green — not defects (so the claim is not unsatisfiable)

- Both round-73 PASS-at-lands receipts are producible at the revision the draft names:
  `accept-ca.py --lands 2d1cd91…` → `ACCEPT-CA-73: PASS legs=9/9`, exit 0;
  `accept-c.py --lands 2d1cd91…` → `ACCEPT-C-73: PASS legs=11/11`, exit 0 (runs in
  `/tmp/CritCaVacuity/lane`, receipts `ca-pass-1.txt`, `c-pass-1.txt`). Neither claim is in the
  R69-M7 "after-state requires rewriting frozen bytes" class.
- Both also pass at the **pushed** tip `c1b5b4761b6ae5ef9ffd81267c3e5e2189ed428d`
  (`ACCEPT-CA-73: PASS legs=9/9` with `--main c1b5b47`), so the draft may choose either revision;
  naming `c1b5b47` would make the receipt cover the pushed tree the closure spot-check graded.
- Receipt re-execution is implementable: two independent runs of each counter differ only in tmpdir
  paths — `accept-ca.py` lines 9/10 (`# clone:`, `# base-clone:`) and the STAMP detail's
  `clone=/tmp/…`; `accept-c.py` line 8 (`# materialized:`) and the CENSUS `last-line=…` path. A
  regex mask `(/tmp/[A-Za-z0-9._-]+)` makes both bodies byte-stable (diffed: only those lines).
- The claim's own "before" facts I re-measured at base: no committed PASS receipt for either
  round-73 counter (`ls reports/round-73/telemetry` → 13 files, none a PASS measure); the five
  modified + one untracked w2 files exist as the worktree state; `LOG.md:4297` still reads
  "Ca 9 scenarios" while `telemetry/selftest-r3.txt` prints 10.
- `2d1cd91` is a strict ancestor of the round-74 base `f7104cb` and carries both PASS results, so
  the RECEIPTS leg's chosen revision is consistent with the round-73 report's own after-lines.

## 5. Could not check

- The round-74 counter itself: it does not exist at the time of this seat, so every finding is a
  finding about the drafted *sentence*, demonstrated on the r3 implementation as its plausible
  parent. Two classes could be closed by an implementation stricter than the draft: the per-commit
  append-only scan and the row-cell schema. The draft must state them (QUALITY 25's direction), not
  leave them to the implementer.
- `claims.json` is DRAFT and `ledger.json` absent, so pair identities, `min_pairs`, the fleet pin and
  the `measured_at` values cannot be attacked yet; my tightenings are all pre-freeze text edits for
  that reason.
- Whether the six inherited files' bytes are what the round-73 seats wrote. No copy exists outside
  this worktree (mtimes and base blobs are recorded above); that is the whole of the evidence
  available, which is why I recommend rewording rather than asserting provenance.
- Side effects of sibling round-74 seats on the six paths: I read them once (mtimes/sha256
  above); I did not monitor for later writes, and my only lane write is this report.
