# QUALITY 7-29 binding map — round 79 O (tool acquisition) and Ca (correction-only)

Seat: RevQuality (round 79 W1). Base: 44f76d456c1b326a71ffdb381590af825cbf11be.
Scope: which clauses of corpus/QUALITY.md criteria 7-29 *exactly bind* the two draft claims
in `.ufo/waves/round-79/CLAIMS-DRAFT.md`, and which do not. "Binds" = a claim/counter
 artefact must satisfy it mechanically or name it review-only; "NOT binding" = importing it
into the claim or the counters would be an invented obligation (the seat item says: avoid
excessive invented obligations). Quotes are verbatim from corpus/QUALITY.md at base.

Claim shapes (from the draft):
- **O** = acquire one bounded ledger-token guard `tools/ledger-token-guard.py` (absent at
  base, verified: `git ls-tree 44f76d45 tools/ | grep -i ledger` → empty). Re-runs approved
  read-only observations against immutable committed bytes; refuses mutable
  revisions/constant printers; rejects an `observed_at_base` differing from the actual
  observation and rejects `stated_token` equal to the actual observation. Ships red/green
  fixtures, mutation controls, selftest, and an independent acceptance counter; owns
  own-work source row S897 (absent at base, verified 0 rows).
- **Ca** = one correction record for R78 routed defect 2: `reports/round-78/telemetry/census-end.txt`
  line 33 S884 `used-by` token drift. Owns records only, not the O tool, not S897.

---

## Binding table

| crit | O | Ca | binding clause (exact, abbreviated where the criterion is long) |
|---|---|---|---|
| 7  | BINDS | BINDS | "each round claim verifies on the base commit plus only the paths it lands itself. Its added lines may not cite an identifier another claim newly exports, nor name a path another claim newly lands" |
| 8  | BINDS | BINDS | "every declared counting or acceptance command runs once on its exact declared input before the round dispatches, and the receipt is committed with the declaration" |
| 9  | BINDS | BINDS | "Every declared counting, acceptance and separability command must appear in the pre-dispatch receipt, and every receipt command must match a declaration verbatim" |
| 10 | not binding | not binding | no external source is opened by either claim (draft: O has "no external-source or new knowledge coverage claim"; Ca works on internal receipts) |
| 11 | BINDS | BINDS | "The declaration lists each claim's clauses … and a non-author seat checks the list against the statement's words before dispatch. A clause no command checks mechanically … is listed as review-only and is never covered by a weaker stand-in predicate" |
| 12 | not binding | not binding | neither claim files a reject/not-registered reason; the dining-candidate REJECTED is a pre-freeze scope disposition (review-only), not a claim clause |
| 13 | not binding | not binding | no live-fetch leg |
| 14 | not binding | not binding | no blind packets / judged-object keys |
| 15 | not binding | not binding | no knowledge entry admitted (dining candidate already rejected; S897 is a registry row, not a cited-line knowledge entry) |
| 16 | not binding | not binding | no live fetch; the reopen-row hold is irrelevant |
| 17 | BINDS | BINDS | "A receipt names the revision its read-path bytes actually equaled, the tree hash of that revision, and the counter's sha256; a run over a moving worktree is disclosed as such, and the original receipt bytes stay preserved below a marker when a re-stamp corrects attribution" |
| 18 | not binding (review-only if S897 names a live URL) | not binding | no registry row naming a live URL + same-page capture is re-validated by these claims |
| 19 | BINDS | BINDS | "every round counter takes a required lands revision (--lands <40hex>) and never grades whatever worktree it happens to sit in … the receipt proves stamp and evaluation agree, carrying # stamped revision:, # evaluated revision:, # measured revision (lane main):, # tree: and # counter sha256 (self:)" |
| 20 | BINDS (declare unchanged) | BINDS (declare unchanged) | "record/instrument repairs (receipt headers, pointer fixes, quote trims, dispositions) are calibration work, never quality or discernment observables … A round that repairs records must declare unchanged on both trends unless an observable fires" |
| 21 | not binding | not binding | no "no capture" ruling |
| 22 | not binding | not binding | no wall/captcha/status Gate record |
| 23 | BINDS | BINDS | "A round counter that offers --selftest has its verdict line, exit code and counter sha256 committed under the round's telemetry before the falsify wave is dispatched … the counter is also run at the FREEZE commit (receipts present, landing absent)" + round-75 addendum (clean green before mutants) |
| 24 | not binding | not binding | no CDX probe |
| 25 | BINDS | BINDS | "(a) The counter takes a required --freeze <40hex> beside --lands and refuses to grade — exit 2, verdict line FAIL legs=0/<n> (refused: …), never a PASS"; (b) freeze ships junk landings it must reject; (c) "The frozen legs[] array is authoritative for the leg set" |
| 26 | BINDS | BINDS | supersedes 25: junk receipts committed AFTER the freeze; J4/J4b fail FROZENCFG never LEDGER; "a round that relies on lands == freeze being red must say it is a do-nothing control only"; "a gate row that pins a counter sha256 or a selftest count must be re-derived from the installed bytes before landing" |
| 27 | not binding | not binding | no Gate reject row in either claim |
| 28 | BINDS | BINDS | "A counter leg whose verdict is produced by a repository tool (a checker, a guard, a census or generator script) runs bytes pinned at the freeze commit: the tool is read with git show <freeze>:<path> into the run directory, or its sha256 is frozen and compared with git show <lands>:<path> before the tool runs" |
| 29 | BINDS | BINDS | "Every numeric statement names its artifact path and measured revision; the evidence records the command, raw result, and comparison. If the measurement is instead about a staged copy, name that copy and do not attribute it to the lane artifact" |

---

## Exact sub-clauses with claim application

### Criterion 7 — separability
- Draft already says "Distinct paths and separable evaluation required."
- O exports: `tools/ledger-token-guard.py`, its fixture/receipt paths, source row S897.
- Ca exports: the correction record (LOG.md/SCORECARD.md rows), its counter
  (`reports/round-79/accept-ca.py`), its telemetry.
- Check (criterion 7's own command): `python3 -B tools/check-claim-separability.py` on the
  round manifest before dispatch. Ca's added lines must not name the guard path; O's must not
  name Ca's correction rows.

### Criterion 8 — declared inputs run before dispatch
- O: guard selftest + acceptance counter commands run once at base on committed bytes;
  receipt committed with the declaration.
- Ca: `accept-ca.py` runs once at base; its mismatch=1 re-derivation is recorded pre-dispatch.

### Criterion 9 — dry runs both ways
- The round manifest's every declared counting/acceptance/separability command must appear
  in the pre-dispatch receipt verbatim and vice versa; expected pre-landing results named
  (absent land → exit 2 with the land named; after-value comparison fails with the before
  value printed). Ca's after-value: `unresolved mismatch=0` can only pass post-landing; the
  receipt must name the expected pre-landing failure (mismatch=1 unresolved at base).

### Criterion 11 — every clause able to fail; review-only named
- O clauses that must each have a failing fixture: (i) re-run observation against immutable
  committed bytes; (ii) refuse mutable revision / constant printer (J4, J4b class); (iii)
  reject `observed_at_base` ≠ actual observation (R78-M1's exact class: the round-77 probe
  rows passed structural LEDGER-CHECK while their recorded base observation did not equal the
  re-run — see corpus/lessons/round-78.md R78-M1); (iv) reject `stated_token` == actual
  observation; (v) stable clean/error exit 0/1/2 labels.
- Ca clauses that must each fail: do-nothing (no correction row), lying correction (row whose
  old/actual tokens do not equal the measured receipt/registry tokens), wrong revision
  (correction naming a revision whose bytes do not carry the stated tokens), changed receipt
  (any edit to `reports/round-78/telemetry/census-end.txt` — it must stay byte-identical;
  verified blob `62eb55b7…` sha256 `05b5011a…` at both 4b255745 and base).
- Review-only candidates to name explicitly: "one working guard (base: absent)" (absence is
  checkable; "working" is review-only), "not historical truth certification", O's
  "independent acceptance counter" independence (review-only), Ca's "without rewriting
  historical receipt" (checkable via blob diff; the *intent* is review-only).

### Criterion 17 — receipts pin measured revision + tree hash
- Ca correction must bind: original receipt digest measured at the revision whose bytes it
  names. Measured here (probe-receipt-digests.txt):
  `git show 4b255745:reports/round-78/telemetry/census-end.txt | sha256sum` →
  `05b5011aaceb5730a94e49022c9bf657b1fe8fa49437874f96071944d9e35867`; identical blob at base
  44f76d45 (spot-check commit did not touch the receipt).
- The correction is an append; original receipt bytes stay preserved (criterion 17's
  append-only limb; see also seat RevAppendOnly).

### Criterion 19 — counters run at the revision they stamp
- Both counters take required `--lands <40hex>` and explicit `--work` scratch (draft:
  "required --lands and explicit scratch"); they grade `git show` committed bytes, never the
  moving worktree (draft: "Counters grade git-show committed bytes, never moving worktree").
- Receipt headers: `# stamped revision:`, `# evaluated revision:`, `# measured revision
  (lane main):`, `# tree:`, `# counter sha256 (self:)`.

### Criterion 20 — trends
- Ca is record/instrument repair → calibration work. Both O and Ca must file
  `unchanged` on expansion/quality/discernment trends. The draft's "No new numeric axis
  score" is criterion 20 restated for this round.

### Criterion 23 — selftest receipt + run at FREEZE commit
- Both counters ship `--selftest` with the verdict line, exit code and counter sha256
  committed under `reports/round-79/telemetry/` before the falsify wave.
- Run each counter at the FREEZE commit (receipts present, landing absent) so
  artifact-vs-leg shape mismatches show before data (the round-73 R73-M6 class).
- Round-75 addendum to 23 (label binds): the selftest receipt must carry the clean scenario
  green before the mutant rows (`selftest: clean -> exit=0 …` before mutants). A
  `NN/NN scenarios` line alone does not satisfy it.

### Criteria 25/26 — freeze constants + junk landings
- Both counters read every constant with `git show <freeze>:reports/round-79/claims.json`
  (Ca adds the ledger/correction config), refuse: non-commit revision, freeze not on the
  lands first-parent chain, `lands == freeze` (graded, never passed), unreadable frozen
  claims.json, LEGCOUNT disagreement with the frozen legs[].
- Junk landings the freeze ships and the counters must reject — mapped to round 79:
  | fixture class | round-79 instance | must fail |
  |---|---|---|
  | J4 constant printer observe_cmd (literal `python3 -c print` / `echo`) | guard ledger pair whose observe_cmd constant-prints the expected token | the guard's LEDGER/grammar leg |
  | J4b evasive constant printer (`import os;print(str(…))`, reads no clone byte) | guard pair with an evasive printer | guard leg (FROZENCFG per 26(b) if it is a graded-tree config edit; the guard's own refusal if it is a pair-level channel) |
  | J5 correction row naming only its id | Ca correction row = "S884" alone | ANNOTATE |
  | J6 in-place edit of a frozen receipt | any edit to `reports/round-78/telemetry/census-end.txt` (e.g. FAIL→PASS flip of a line) | APPENDONLY |
  | J7 correction citing claim-C/incidental rows | Ca correction row citing O's guard fixtures or S897 | SEPARABLE |
- Criterion 26(c): a round-79 counter that refuses `lands == freeze` must say its
  do-nothing control is `lands == base` (or the uncorrected tree), never rely on
  lands==freeze being red.

### Criterion 28 — tool authority pinned at freeze
- Directly binds O: `accept-o.py` executes `tools/ledger-token-guard.py`; per 28 the guard
  bytes must be read with `git show <freeze>:tools/ledger-token-guard.py` into the run
  directory, or the guard's sha256 frozen and compared with `git show
  <lands>:tools/ledger-token-guard.py` before it runs. A stub guard swapped in at lands must
  fail the selftest (add the stub-tool mutant).
- Binds Ca the same way for any repository tool `accept-ca.py` executes.

### Criterion 29 — filed numbers re-derived
- Ca's filed numbers and their re-derivations (this seat, raw output preserved in
  probe-receipt-registry-mismatch.txt / probe-receipt-digests.txt):
  - "mismatch=1 at base": re-derived by count over committed bytes at 44f76d45 — receipt
    W01 used-by tokens vs registry field-12 cells → exactly 1 mismatch (S884).
  - old token = `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md`
    (sha256 `62114297…`), at receipt `reports/round-78/telemetry/census-end.txt:33`,
    revision 4b255745 (blob identical at base).
  - actual token = `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md`
    (sha256 `dad9788a…`), at registry `corpus/SOURCES.md` S884 row field 12, same revision.
- O's filed numbers (fixture counts, timeout/output caps, exit-code labels) must each name
  artifact + measured revision in its report.

---

## Deliberately NOT imported (invented-obligation guard)

10, 12, 13, 14, 15, 16, 18, 21, 22, 24, 27 do not bind O or Ca as mechanical clauses.
Rationale per criterion is in the table; the common shape: no Gate rows, no live fetches, no
knowledge admission, no blind packets, no CDX probes, no external-source opening. Two need
words:

- **12**: the dining/tableware REJECTED disposition names corpus files and could be re-tested
  by grep, but it is a planner scope record in CLAIMS-DRAFT, not a clause of claim O or Ca.
  Making it a claim clause would widen both claims beyond the draft.
- **18**: S897 is an own-work row citing opened R77 mismatch evidence. If the landed S897 row
  names a live URL + wayback capture, criterion 18 becomes review-only for that row; it still
  does not bind the O or Ca counters.
