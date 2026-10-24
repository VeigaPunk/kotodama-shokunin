# RevClaimO — claim O: statement vs frozen predicate (round 65)

Seat: attack on claim O (operability / counter hardening). Lane repo
`/home/vgpnk/Projects/shokunin/kotodama-shokunin`. Read-only review; nothing edited or committed.

## Bytes reviewed (the instrument moved twice during review)

| artifact | first seen | reviewed in full | tip at review end |
|---|---|---|---|
| `reports/round-65/accept-o.py` | 66810 B, 01:18 | sha `2a03a2fe…` (rev 2, 68252 B, 01:52:59) | sha `20d06dd6…` (rev 3, 69897 B, 01:55:32) |
| `reports/round-65/claims.json` | 1406-char O statement | sha `02ec4204…` (01:53:44) | sha `5d6dad5d…` (1761-char O statement, 01:55:32) |
| `telemetry/dry-run-o.txt` | 01:41 | same | **stale** (predates rev 2 and rev 3) |
| `telemetry/controls-o.txt` | absent at 01:45 | — | 01:53:11, still says MUTEX "under debug" |
| `telemetry/exactness-sweep-o65.txt` | absent | — | **absent** (claim land) |
| `.ufo/waves/round-65/rows/row-*.txt` | 0 | 4 | **6** (FRAG needs 26) |

Line numbers below are rev 2 (`2a03a2fe`) unless marked rev 3; rev-3 re-checks are stated explicitly.
The frozen predicate sentence is unchanged in both claims.json revisions and reads verbatim in
`accept-o.py` line 116: `ACCEPT-O-65: every leg of reports/round-65/accept-o.py prints PASS.`

## Verdict

**BLOCKER.** At the reviewed tip, ACCEPT-O-65 cannot print PASS honestly, and the claim text that
reviewers were told was frozen pre-wave was rewritten mid-wave with only one of its substantive
changes recorded. The predicate sentence itself is stable, so the frozen-predicate letter is intact;
the *statement* — the object every receipt is supposed to satisfy — was not.

## Direct answers to the three questions

### 1. Clauses with no leg (review_only honesty)

`claims.json` claim O declares only two review-only items (MUTEX table honesty; FULL's bound). Every
clause below is **not** in `review_only` and **not** measured by any leg:

- **Six-surface historical attribution** ("the round-64 closure's LOG names six … not repaired").
  No leg. The premise is true — `LOG.md:4165` names all six with the cited files (I checked) — but it
  is prose, not measurement. Acceptable only if declared review-only.
- **accept-c RESTATE rev-2 closure** ("accept-c revision 2 RESTATE … >= 80% in-order token coverage").
  `accept-o.py` never runs accept-c: the only occurrences are docstring prose (lines 8–10). Regression
  in accept-c cannot make ACCEPT-O-65 red. Claims C's predicate covers it, but O's statement asserts
  it and O's predicate cannot see it.
- **accept-ca clause.** In the pre-rewrite statement this read "accept-ca revision 1 keyed legs plus
  NITS value-pair pinning". That was **false**: round-65 `accept-ca.py` has only `R1..R7, CRITERION,
  QUOTES` (`grep 'leg("' reports/round-65/accept-ca.py`); `HISTOGRAM/R63SEP/DISPO/NITS` exist only in
  `reports/round-64/accept-ca.py` and in prose in `accept-o.py:12-14`/`claims.json`. The tip statement
  replaced the clause with a "retired with their round … keyed-by-design" disposition and recorded it
  in `statement_revision` — see finding D for what the record omits.
- **"unchanged" tool and "every round-62/63/64 leg".** No leg — see answer 2.
- **"committed exactness-sweep-o65.txt matches the live measurement".** No committed file exists, so
  MUTEX prints FAIL `exactness-sweep-o65.txt:not_committed` (observed in `dry-run-o.txt`); and the
  match is self-referential — see answer 3.
- **"zero SKIP" / FRAG scope were silently relaxed/strengthened in the statement** to fit the counter
  (finding D). Those clauses now have no review-only marker either.

### 2. Is "the unchanged tools/reopen-row.py passes every round-62/63/64 leg" verified by a leg?

**No.** It decomposes into three propositions and only the first is measured:

1. *Passes* — yes, the current battery is green at base: `dry-run-o.txt` shows GEN, ORDER, BOUND, EXIT,
   PRIV, DEFAULT, ERR, REDIRECT, MALFORMED, GZIP, TRUNC, TIMEOUT, all seven EDGE legs, DRIP and MUT all
   `PASS`.
2. *Unchanged* — **no leg**. `leg("TOOL", …)` (line 469) checks only `os.path.isfile` +
   `os.access(X_OK)`; INDEP (line ~481) only scans the tool text for counter path names. There is no
   sha/commit pin. The docstring pins `c0f10a8450b4…` in prose only. Rev 3 adds a sha check inside
   MUTEX (line 1237) but it only requires the committed table to name the *current* tool's sha — a
   self-consistency check, not the base revision. (I verified by hand that the working-tree tool hash
   equals the base blob `git cat-file 17c32302:tools/reopen-row.py`; that is my check, not a leg, and
   cannot be carried by a predicate that only runs `accept-o.py`.)
3. *Every round-62/63/64 leg* — **no leg**. Nothing maps a legacy leg identity into the round-65 run,
   and no legacy receipt is replayed. Round-64's `accept-o.py` has the same CORE/EDGE names, but the
   round-65 file is a rewrite (rev-5 note at line 426; revs 2 and 3 today), so name identity is not
   assertion identity.
   Worse, MUT and MUTEX derive every mutant from the live tool bytes, so a tool edit that preserves
   the needles leaves both green: the kill set is self-adaptive and cannot detect "unchanged".

Needed: a `TOOL_SHA` leg pinning the base blob hash, plus an explicit legacy-leg list (or a replayed
round-62/63/64 receipt leg). Until then the clause belongs in `review_only`.

### 3. Is the MUTEX "disclosed expectation" the same object in statement, counter, future receipt?

**No — three different objects.**

- **Statement** cites `w2/RevVerifyO2.md` / `exactness-sweep-o.txt` and names only "m1
  +EDGE_USERINFO+EDGE_HTTPS, m2 +EDGE_MALTARG".
- **The cited disclosure** (`reports/round-64/telemetry/exactness-sweep-o.txt`) measures **only m1 and
  m2**; its own header says the exactness claim "is false for m1 and m2" and that exclusivity beyond
  them was unmeasured. It has no rows for m3/m5/m6/m7/m8/m9/m10/mread.
- **The counter** hardcodes `SWEEP_EXPECT` for all ten mutants (rev 2 lines 1166–1177; unchanged at
  rev 3). Eight of those sets have no prior disclosure anywhere; MUTEX never opens the cited file, so
  "equal the disclosed expectation" is never checked against the disclosure.
- **The future receipt** `exactness-sweep-o65.txt` is never written by the counter; a seat must
  transcribe the live sweep. The table is therefore the measurement, not an independent expectation —
  MUTEX compares the live measurement to a copy of itself. The only independent content is the tool
  sha line added in rev 3.

So "superset the pins and equal the disclosed expectation" is honest only for m1/m2; for the other
eight the expectation is fitted in the same file that grades it. It stays review-only only if the
statement says so.

## Findings by severity

### BLOCKER A — MUTEX was unsatisfiable at rev 2 (digit-blind extraction); root cause now fixed at rev 3
`failed = … if re.match(r"^[A-Z_]+ FAIL", l)` (rev 2 line 1188) cannot match `EDGE_308 FAIL` or
`EDGE_5TH200 FAIL` because `[A-Z_]+` excludes digits (verified directly: `bool(re.match(...))` is
False for both). Consequence exactly as observed: `dry-run-o.txt` MUTEX
`bad=["m6:pinned_not_failed=['EDGE_308']", "m6:measured=[]…", "m7:pinned_not_failed=['EDGE_5TH200']",
"m7:measured=[]…"]`, even though the same receipt's MUT line shows `m6->EDGE_308 FAIL` and
`m7->EDGE_5TH200 FAIL`. Rev 3 changed all three sites to `[A-Z0-9_]+` (lines 1145/1147/1208) and cites
`RevCounterO.md` V2/V3 — so this blocker is closed in bytes, but no receipt certifies rev 3 (finding C).
The same blind spot was a *soundness* hole, not only a red leg: an undeclared extra failure on those
two legs could never be seen.

### BLOCKER B — FULL was unsatisfiable at rev 2 for two independent reasons; both fixed at rev 3
1. `pass_lines` used the same digit-blind regex, so a 100 % green inner run scored 21/23 against
   `len(run_legs_all) == 23` — the receipt's own `pass=21/23 skip=3 fail=0` shows a fully green
   battery failing the leg.
2. `verdict_line == ["ACCEPT-O-65: PASS"]` while the inner invocation always passes `--only`, so the
   child always appends ` [filtered: 23/26 legs]` (line 1259) and the exact compare can never succeed.
Rev 3 computes `expected_verdict = f"ACCEPT-O-65: PASS [filtered: {len(run_legs_all)}/{len(ALL_LEGS)}
legs]"` and uses digit-aware counting. Note the honest residual: FULL re-executes 23 of 26 legs and
never re-executes MUTEX or FRAG, so "complete-battery" is 23/26 by construction.

### BLOCKER C — stale receipts: no receipt certifies the reviewed bytes
`dry-run-o.txt` (01:41) predates rev 2 (01:52:59) and rev 3 (01:55:32). `controls-o.txt` (01:53:11)
predates rev 3 and still states control 3 (MUTEX) is "under debug … will be repaired or dispositioned
before integration". The only rev-3 run on disk is FRAG-only (`controls-o.txt`, `files=0/26`). The
claims' own controls clause requires pre-data controls meeting the prior form and failing the
round-65 form *before data*; at the tip there is no full-battery receipt for the shipped counter, and
the exactness land is still absent. Also, `dry-run-o.txt`'s header asserts "FULL/MUTEX/FRAG must
FAIL" while its own body shows `FRAG PASS … 0 finding(s) in 0 file(s)` — the vacuous pass it was
supposed to forbid.

### BLOCKER D — the frozen statement was rewritten mid-wave and the record under-declares it
Pre-rewrite statement captured at first read: 1406 chars, contained
(a) "accept-o revision 1 gains FULL (complete-battery subprocess re-execution, **zero SKIP**)", and
(b) "FRAG (… scans `.ufo/waves/round-65/rows` with 0 findings …)". Current statement: 1761 chars,
reads "zero **unexpected** SKIP" and "scans **exactly 26** … row fragments", plus "accept-c revision 2
… with every row cited" and the Ca retirement paragraph. `statement_revision` records **only** the Ca
clause ("the 'keyed Ca legs …' clause described legs the round-65 accept-ca does not carry …
Predicate unchanged"). The SKIP relaxation, the FRAG 26-file requirement, and the accept-c revision
bump are **undeclared**. A receipt cannot name which statement it satisfies; the record is not an
honest account of the change. (Timeline: rows dirs from scout seats exist at 01:53/01:56, before the
01:55:32 rewrite, so "pre-data" is also questionable for the FRAG dataset.)

### HIGH E — surface 1's closure is outside O's predicate and its control does not isolate the rule
The accept-c teaches near-copy closure is measured only by claim C. `controls-c.txt` itself notes that
in control 2 the failure came from the in-order quote rule and that "the S750 teaches near-copy
(coverage 0.92 …) is additionally caught by revision 1's teaches_nearcopy rule — the nearcopy-first
demonstration rides seat MutCounterC's crafted fixtures". So the only control for O's surface 1 does
not isolate the new rule. Also `claims.json` separability ("accept-o.py reads only tools/reopen-row.py,
the round-65 counters and tools/check-row-fragments.py") is inaccurate: accept-o reads
`reports/round-65/telemetry/*` and, via FRAG, the rows tree.

### HIGH F — FRAG is a shared-directory count, not row identity, and couples O to C's data
Rev 3 requires `files == 26` from `FRAG: k finding(s) in m file(s)` (line 1265) over a recursive walk
of `.ufo/waves/round-65/rows` for `row-*.txt`. Any 26 valid fragments pass — the check never binds
them to S750–S775, so draft fragments in per-seat subdirectories (`ScoutRow02/07/12`, `ScoutGapGames`
already exist) can satisfy the count while the actual registry rows differ; conversely 27 fragments
(a draft plus its final) fail the claim for a reason the statement does not describe. At review end
there were **6** `row-*.txt`, so FRAG is red at tip. Requirement to fix: bind scanned fragments to the
claim-C row IDs (and their `used-by`), or move FRAG to claim C.

### MEDIUM G — "unchanged" and legacy-leg coverage are unpredicated (see answer 2)
Recommend a `TOOL_SHA` leg and a legacy-leg manifest/replay; otherwise move the clause to review-only.

### MEDIUM H — the committed expectation table has no provenance column (see answer 3)
Require the table to mark, per mutant, whether the expectation is disclosed (m1/m2, with the
round-64 file cited) or first-measured this round, and have MUTEX cross-check m1/m2 against the cited
round-64 file rather than a hardcoded literal.

### LOW I — docstring revision headers lag their own histories
`accept-c.py` header "revision 1" with history rev 2/2a; `accept-ca.py` header "revision 1" with
history rev 3; `accept-o.py` header "revision 1" with history rev 2/3. Receipts and the claim quote the
header, so the header is a false provenance line.

### LOW J — table comparison accepts any preamble
`committed.splitlines()[-len(sweep_rows):] != sweep_rows` only compares the tail; a table with a false
preamble passes once the tail matches. The rev-3 tool-sha substring is the only content anchor.

## Residual risk (even if every red is repaired)

- MUTEX's exactness for eight of ten mutants remains fitted, not disclosed; fixing the regex makes the
  table *match* without making it an independent prediction.
- FULL cannot cover MUTEX/FRAG (recursion), so the "filtered-green" class is closed only for the 23
  legs FULL re-runs. Every green `ACCEPT-O-65` line obtainable today is filtered — one exists at
  `.ufo/waves/round-65/w1/MutReceipts-evidence.txt:25` (`ACCEPT-O-65: PASS [filtered: 1/26 legs]`),
  also recorded by `ExecCounterReview.md`. The class the statement says is closed is still producible.
- FRAG's exactly-26 count is a filename proxy and is coupled to another claim's working directory.

## Verification gaps

- I did not execute the ~7-minute full battery; FULL/MUTEX findings are static analysis corroborated by
  the base receipt's own numbers (`pass=21/23`, `m6/m7 measured=[]`, `FRAG … 0 file(s)`), and the
  regex behaviour was verified directly in Python.
- I did not run the rev-3 counter; its fixes are read from bytes and comments only, so BLOCKER A/B are
  "closed in source, unverified by receipt".
- `lsp` is not mounted in this runtime (`xd://lsp` → "No such tool … Mounted devices: ast_edit,
  debug"), so caller/definition checks are textual grep, not semantic; for a single-file counter with
  self-contained leg names the grep result (no import/subprocess of accept-c/accept-ca) is conclusive,
  but it is not an LSP-confirmed reference set.
- No tools were installed or upgraded during this review.

## Recommended dispositions (recommendation only; not an admission)

1. Keep the pre-wave statement text on record; add a `statement_revision` entry itemising **each**
   changed clause (SKIP tolerance, FRAG 26, accept-c revision), or restore the pre-wave text and file
   the divergences as errata.
2. Land a rev-3 full-battery receipt with the exactness table before any further claim-O scoring;
   update `controls-o.txt` control 3 from "under debug" to its disposition.
3. Add `TOOL_SHA` (base blob hash) and a legacy-leg manifest leg, or declare both clauses review-only.
4. Bind FRAG's 26 fragments to S750–S775 (or move FRAG to claim C) and assert the count equals the
   registry row count, not a literal.
5. Record expectation provenance in `exactness-sweep-o65.txt` and cross-check m1/m2 against the cited
   round-64 file.

Report: .ufo/waves/round-65/w1/RevClaimO.md
