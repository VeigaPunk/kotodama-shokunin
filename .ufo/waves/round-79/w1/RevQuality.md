# RevQuality — round 79 W1: QUALITY 7-29 exact binding clauses for O and Ca

Seat: RevQuality (reviewer, leaf). Base: 44f76d456c1b326a71ffdb381590af825cbf11be.
Read: `.ufo/waves/round-79/CLAIMS-DRAFT.md`, `corpus/QUALITY.md` (whole),
`corpus/lessons/round-78-verifier-spotcheck.md`, `corpus/lessons/round-78.md` (R78-M1),
`reports/round-78/telemetry/census-{start,end}.txt` at committed revisions,
`.ufo/waves/round-77/w1/stage/ExecAdaptCa/{probe-real-ledger.json,selftest-ca.txt}`
and the round-77 counter lineage. Stage: `.ufo/waves/round-79/w1/stage/RevQuality/`
(binding-map.md, check-commands.md, count-mismatch.py, two probe receipts with raw output).

No lane/fleet file was mutated; no tool installed. All probes read committed bytes.

## 1. Deliverable: which clauses bind

Full per-criterion table with verbatim quotes is in
`stage/RevQuality/binding-map.md`. Summary:

**BINDS O (tool acquisition):** 7, 8, 9, 11, 17, 19, 20, 23 (+round-75 addendum), 25, 26, 28, 29.

**BINDS Ca (correction-only):** 7, 8, 9, 11, 17, 19, 20, 23 (+round-75 addendum), 25, 26, 28, 29.

**NOT binding (invented-obligation guard):** 10, 12, 13, 14, 15, 16, 18, 21, 22, 24, 27.
Reason: no Gate rows, no live fetches, no knowledge admission, no blind packets, no CDX
probes, no external-source opening, no reject reasons filed by these two claims. Two need
words (12 dining disposition = planner scope record, review-only; 18 S897 = own-work row,
review-only if it names a live URL).

Highest-value exact clauses for the counter drafters:

- **11** — every claim clause must have a failing fixture; review-only clauses named, never
  covered by a weaker stand-in predicate. This is routed defect 3's class: R78-M1's fix was
  "proposed but not yet demonstrated able-to-fail" (`corpus/lessons/round-78-verifier-spotcheck.md`
  routed defect 3; `corpus/lessons/round-78.md` R78-M1).
- **25(a)/26** — counters read every constant with `git show <freeze>:…`, refuse
  (exit 2, `FAIL legs=0/<n> (refused: …)`, never PASS) on: non-commit, freeze off the lands
  first-parent chain, `lands == freeze` (graded, never passed), unreadable frozen
  claims.json, LEGCOUNT disagreement. 26(c): a counter refusing lands==freeze must say its
  do-nothing control is lands==base.
- **28** — accept-o executes `tools/ledger-token-guard.py`; the guard bytes must be
  `git show <freeze>:tools/ledger-token-guard.py`-materialized or sha256-pinned and compared
  with `git show <lands>:…` before running; a stub guard at lands must fail selftest.
- **29** — every filed number names artifact + measured revision with command, raw result,
  comparison. Ca's filed numbers are re-derived below.
- **20** — Ca is record/instrument repair; both claims file `unchanged` on all trends;
  "No new numeric axis score" (draft) is criterion 20 restated.

## 2. Verification probes run (raw output preserved in stage)

**(a) Ca filed number "mismatch=1 at base" — RE-DERIVED, confirmed.**
`stage/RevQuality/count-mismatch.py` compares the W01 used-by tokens in
`reports/round-78/telemetry/census-end.txt` against registry field-12 cells of
`corpus/SOURCES.md`, at both 44f76d45 and 4b255745
(`stage/RevQuality/probe-receipt-registry-mismatch.txt`):

```
receipt W01 rows=4 registry rows=820 MISMATCH count=1
MISMATCH ('S884',
 'corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md',
 'corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md')
```

The other three W01 rows (S881, S882, S893) match their registry cells at both revisions.

**(b) Receipt/registry blob identity across revisions — confirmed.**
`stage/RevQuality/probe-receipt-digests.txt`:
- census-end.txt blob `62eb55b77f44bf47c283c98c5645dd7141e98495`, sha256
  `05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867`, identical at 4b255745
  and base 44f76d45 (the spot-check commit did not touch the receipt).
- SOURCES.md blob `c28330a37535223939ea5820af50d8d8595ed059` at both revisions.
- census-start vs census-end differ ONLY at line 33 (the S884 used-by line) — diff captured.
- `git log --all -- corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md` → 0 commits (the receipt's full path never existed).

**(c) Correction-binding tokens measured** (sha256 of the exact token strings, no newline):
old token `621142976cca5e6049bd5e206764126abad4e6281e283c86c848fe7238e549e8`;
actual token `dad9788a35771cd368d34792f7428ab2a002783f5ad1f8304733c70ab6d485a4`.

## 3. Review findings on the draft and evidence

- **F1 (supports Ca, exact wording available).** The draft's Ca sentence ("round-78
  census-end.txt's S884 used-by token differs from the registry at its recorded round-78
  revision") is re-derivable as filed; probe (a) confirms exactly one mismatch and names both
  tokens. No wording change needed for that clause.
- **F2 (correction diagnosis nuance — pass to ScribeCorrection).** The R78 spot-check's
  parenthetical "(and …24-r13.md never existed in this lane)" is true of the full path
  `worldbuilding-setting-practice.amend-2026-10-24-r13.md` (0 commits), but the suffix
  `amend-2026-10-24-r13.md` DOES exist on a different file at 4b255745:
  `corpus/knowledge/culture-material/heritage-taxonomy-models.amend-2026-10-24-r13.md`.
  The correction row must bind the full path strings, not a substring, or a token-level diff
  could drift toward the wrong sibling file.
- **F3 (O genesis evidence located).** O's two rejections are exactly R78-M1's recorded
  classes: rows whose "recorded base observation did not equal the re-run observation" and
  the requirement to "reject any pair where stated token equals that observed token"
  (`corpus/lessons/round-78.md` R78-M1). The red-before evidence the draft needs under
  criterion 23 is W2's executed BASEMISMATCH failure on the 11-pair probe, as R78-M1 itself
  states. The round-77 counter lineage (ExecAdaptCa accept-ca.py LEDGER/BASEMISMATCH legs,
  selftest scenarios 31/32: fabricated-base-observation and green-pair both red) is the
  existing implementation reference for the guard's grammar; the guard is the standalone
  bounded version of that leg pair.
- **F4 (base-absent claims verified).** `tools/ledger-token-guard.py` absent at base
  (`git ls-tree 44f76d45 tools/` has no ledger entry); S897 absent at base (0 registry rows,
  0 census mentions). O's "base: absent" and S897-as-new-export hold on committed bytes.
- **F5 (junk-fixture mapping to the draft's kill rules).** The draft's "Do-nothing/lying
  correction/wrong revision/changed receipt must fail" maps one-to-one onto the criterion-25
  fixture classes: do-nothing = lands==base (correction absent), lying = ANNOTATE-class red,
  changed receipt = J6/APPENDONLY (§3 of check-commands.md gives the exact
  `git diff --numstat` control, expected empty). "Wrong revision" needs its own fixture: a
  correction row naming a revision whose bytes do not carry the stated tokens — the counter
  must re-derive tokens at the named revision rather than trust the row (criteria 11/29).
- **F6 (review-only clauses to name, per criterion 11).** "one working guard" (working =
  review-only), "independent acceptance counter" independence (review-only), "not historical
  truth certification" (review-only), Ca's "without rewriting historical receipt" intent
  (the blob-diff check is mechanical; the intent is review-only). Naming these now prevents a
  weaker stand-in predicate being substituted later.

## 4. Fixtures/commands drafted

`stage/RevQuality/check-commands.md` holds the runnable set: mismatch re-derivation (§1),
receipt digest binding (§2), append-only control (§3), criterion 25/26 shape one-liners over
both counters (§4), selftest-receipt checks (§5), expected junk-receipt red legs (§6), and
the O guard's bounded-grammar clauses (§7). These are drafts for L1 integration; no counter
source exists yet to run them against (base-absent per F4), so §4/§5 are recorded unrun —
they are checks to run once ExecGuard/ExecOCounter/ExecCaCounter land their drafts.

## 5. Residual risk / not done

- No claim-separability manifest for round 79 exists yet; criterion 7's
  `tools/check-claim-separability.py` run is pending the L1's manifest (recorded, not run).
- S897's landed row shape was not inspectable (row does not exist at base); criterion 18's
  review-only note stands until ScribeLesson's S897 draft lands.
- I did not run any counter selftest (no counter exists at base) and did not verify the
  executors' drafts — out of this seat's scope and time ordering.

Report: `.ufo/waves/round-79/w1/RevQuality.md` (this file).
