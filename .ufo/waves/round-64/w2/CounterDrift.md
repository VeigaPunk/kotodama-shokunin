# CounterDrift — round-64 wave-2 post-revision counter drift audit

Seat: `kotodama-r64.CounterDrift` (reviewer). Read-only: no counter, row, log, git index,
or jj state was edited; no tools installed or updated. Scratch:
`/home/vgpnk/.cache/hyaku/kotodama-r64-w2/CounterDrift/` (snapshots + a shared clone probe).
LSP: no `lsp` device was exposed to this seat (tool inventory: read/bash/edit/eval/glob/grep/
task/wait/web_search/write), so structural claims below use Python `ast` over the counter
sources plus executed runs, not semantic LSP references.

Axes judged: coverage (C), operability (O), calibration (Ca and evidence provenance).

Revision-provenance anchor for the counter edits: the RevCounters seat's own report is
`.ufo/waves/round-64/w2/RevCounters.md` (4,792 bytes, mtime 2026-10-23 23:55 local /
2026-10-24T02:55Z), assigned by `.ufo/waves/round-64/nw2-spec.json` name `RevCounters`.
It states explicitly: "No post-revision counter/control run was made in this editing wave"
and that the m5 paired run and unknown-selector exit-2 are "owed". Wave-2 verifier reports
consulted: `.ufo/waves/round-64/w2/RevVerifyCa.md`, `RevVerifyO2.md`, `CriticRevCa.md`,
`CaReceipts.md`, `SeparabilityRe.md`, `ReportFrag2.md`.

## Snapshot identity (binding)

The counters were a live construction site during this audit; every statement below is
bound to these bytes/times. Final state check at 2026-10-24T02:59Z (Ca changed once more
at 02:58:58Z; the table is updated to that state):

| file | final sha256 | mtime (local, -0300) |
|---|---|---|
| `reports/round-64/accept-c.py` | `979050ce21fa01758c075745b08bf3ecf7d6e73baad543a1df83f666ecc5de2b` | 2026-10-23 23:56:55 |
| `reports/round-64/accept-ca.py` | `7319ff4b9c7eb2cd23f866eb4db62d469a539b8dd99b8326fb6bae8f1cb0d4c5` | 2026-10-23 23:58:58 |
| `reports/round-64/accept-o.py` | `6d9c9354f0d7a9535aba4e781541b04626dd3a91791175a7d5f845c559615fa1` | 2026-10-23 23:54:09 |
| `reports/round-64/claims.json` | `e970aaceafa377230c91775f5b1b34e69aeb176faa52404715653d911a09bd3a` | unchanged since `097c21d` (not in `git status`) |
| `tools/reopen-row.py` | `c0f10a8450b425bb0959b00c18031fde43ac4809a5334538e9c1d4d9199568a0` | unchanged; equals `ff30a205` blob (verified) |

Observed churn inside the audit window (recorded, not hidden):

- C: `4df7b32b…` (rev1) → `073e9716…` (rev3, buggy) → `979050ce…` (rev3, fixed 02:56:55Z).
- Ca: `f222648e…` (rev1) → `a8088092…` (rev2, 02:53:26Z) → `63510c4d…` (still stamped rev2, 02:57:32Z, crashed) → `7319ff4b…` (still stamped rev2, 02:58:58Z, fixed and passing).
- O: `c27a9fef…` (rev3) → `6d9c9354…` (rev4, 02:54:09Z).

At the declaration commit `097c21d`: `accept-c.py` = `3519c9c8…` and `accept-ca.py` =
`3a5a79d1…` (both docstring-stamped "revision 0"); `accept-o.py` is **absent** from the
commit (`git show 097c21d:reports/round-64/accept-o.py` → `fatal: path … exists on disk,
but not in 097c21d`).

## Findings by severity

### HIGH

**H1 — every claim-O receipt binds rev3, but the counter is now rev4; rev1/rev2 history
cites bytes that are not on disk.**
Current `accept-o.py` = revision 4, sha `6d9c9354…` (`:2`, `:117-122`). All filed O receipts
bind revision 3 / sha `c27a9fef…`:

```text
reports/round-64/telemetry/final-measures-o.txt:2  (revision 3, working-copy bytes) sha256 c27a9fef…
reports/round-64/telemetry/mut-o.txt:2             (revision 3) sha256 c27a9fef…
reports/round-64/telemetry/edge-o.txt:2            (revision 3) sha256 c27a9fef…
reports/round-64/telemetry/control-o.txt:2         (revision 3) sha256 c27a9fef…
```

`ls reports/round-64/telemetry/*rev4*` → none. Rev4 materially changed the MUT mechanism
(m5 paired selector, `accept-o.py:1093`, `:1116-1121`) and `--only` input handling
(`:437-450`), so the rev3 receipts do not measure the current instrument. Worse, the
docstring's revision-1 and revision-2 histories (`:94-108`) both say their run is
"preserved at `reports/round-64/telemetry/final-measures-o.txt`" with counter sha
`bb0c74a486ae53ebc9a09787670020b69a03ef373df68f04fee8a30a827bf280` at measured revision
`ff30a205…`; that path now holds rev3/sha `c27a9fef…`, so the cited rev1/rev2 evidence is
absent/overwritten. This corroborates wave-1 `ReviewerOReceipt` M3 (rev1/rev2 forcing
receipt `bb0c74a4` absent). No receipt on disk measures rev4.

**H2 — O rev4's m5 mutant is syntactically invalid, so MUT cannot pass; the rev4 docstring
also contradicts its own isolation check.**
The m5 replacement string (`accept-o.py:1056`) inserts a 12-space `if (…` immediately after
an 8-space `parsed_location = …` line inside `tools/reopen-row.py`. Extracted with
`ast.literal_eval` from the `MUTANTS` assignment, the needle occurs once; applying it yields
mutant sha256 `795b8d196eec4b64344b39338bf73a3cc6a73c075671702d4b963959a6e6ecb6` (identical
to the mutant RevVerifyO2 rebuilt independently), and `compile()` fails:
`SyntaxError: unexpected indent (line 605)` at the inserted `if`. Consequence: the inner m5
run cannot print `EDGE_SCHEMEREL PASS`; the isolation check at `:1116-1121` therefore appends
to `mut_bad`, MUT FAILs, and the frozen `ACCEPT-O-64` cannot print PASS at `6d9c9354…`.
Separately, the revision-4 docstring sentence says the paired run "requires the former
[EDGE_SCHEMEREL] to FAIL and the latter [EDGE_SLASHLESS] to PASS" (`:117-120`), while the
code requires `EDGE_SCHEMEREL PASS` (`:1119`) — the prose is inverted relative to the check.
(RevVerifyO2 independently reports both legs FAIL with `rows=[]` for the rebuilt mutant.)

**H3 — C's frozen statement/exports are now false of the landed rows: three of the six
disposition rows are `queued`, not rejected.**
`claims.json` C states "six rejected rows S744-S749" and `exports` says
`"S744-S749 (rejected)"`. The landed registry in the working tree (`corpus/SOURCES.md`,
modified during this audit) carries S744/S745/S747 status `rejected` and S746/S748/S749
status `queued`, with `QUEUED-CANDIDATE: …` teach cells; the entry and all 32 rows are now
present (entry untracked). `accept-c.py:246` accepts `cs[7] in ("rejected", "queued")` and
`:250` accepts the queued teach prefix, so `ACCEPT-C-64` can pass while the frozen statement
and `exports` say all six are rejected. `claims.json` is unmodified (`e970aac…`, not in
`git status`). This is declaration-vs-land drift; the predicate is unaffected.

### MEDIUM

**M1 — Ca revision number "2" names three materially different byte states.**
`a8088092…` (02:53:26Z; NITS phrase-proximity, RevVerifyCa verified PASS 7/7 and quoted this
sha at `RevVerifyCa.md:12`; RevCounters.md:48 calls it "Current revision-2 counter SHA-256")
was replaced at 02:57:32Z by `63510c4d…` (rewritten NITS, crashed — see R2) and again at
02:58:58Z by `7319ff4b…` (NITS exact affirmative "Round-63 numeric corrections" sentences,
passes). All three are stamped "revision 2" in the header (`:2`), whose history still lists
only revision 2 (`:40-45`). Five wave-2 reports name `a8088092…` as current rev2
(`RevVerifyCa.md:12`, `CaReceipts.md:17,46`, `SeparabilityRe.md:13`,
`ReportFrag2.md:45,52`). A revision stamp must identify one byte state; here it does not.

**M3 — C revision ledger is not monotonic: header 3, body labels 1 and 4.**
Header `:2` says "revision 3"; history `:51-55` lists only revisions 2 and 3; `:231` carries
"revision 1 (pre-data)"; `:428` carries "revision 4 (pre-data, receipt:
`telemetry/row-verify.txt` S706 flakiness)". The revision-4 marker is present already in the
declaration commit `097c21d` (checked with `git show 097c21d:reports/round-64/accept-c.py`),
i.e. it predates the declared revision and is not in the history. Its cited path
`telemetry/row-verify.txt` does not exist under `reports/round-64/telemetry/`; the only
match is `reports/round-63/telemetry/row-verify.txt` (S706 NOT_LOCATED ×3). The highest
in-body revision label (4) disagrees with the file's own stamp (3).

**M4 — O's "exactly their pinned leg" / "observed failure-leg set equals its pins" is
still not what MUT verifies.**
Each mutant inner run is launched with `--only <pins>` (`accept-o.py:1093`), so non-pinned
legs print `SKIP`; `pinned_lines` is filtered to pinned prefixes (`:1103-1106`) and
`pinned_fail` tests `set(failed) == set(pinned)` (`:1108-1110`) — that is pins ⊆ failures
among the printed pinned lines, not equality over all 23 legs. Only m5 gets an additional
paired check (`:1116-1121`). claims.json O still says "ten byte-patched mutants each fail
exactly their pinned leg". Extra failures are unobservable for m1, m2, m3, m6, m7, m8, m9,
m10, mread; the docstring rev3 sentence "requires the observed failure-leg set to equal its
pins (`:113-116`) overstates the code.

**M5 — the stated "byte-identical" predicate criterion fails literally in all three
counters, and no receipt contains the predicate sentence.**
claims.json predicates are one line; each docstring hard-wraps at 79 columns:
C `:56-58` and O `:123-125` break before `PASS.`; Ca `:46-48` breaks before `prints PASS.`.
So raw docstring bytes contain one LF where the predicate has a space; after normalising
newlines the three sentences are content-identical to claims.json (verified for C, O, Ca).
The receipts carry only the label (`ACCEPT-O-64: PASS` in `final-measures-o.txt:28`,
`edge-o.txt:15`, `mut-o.txt:26`, `control-o.txt:41`; `ACCEPT-C-64: FAIL` in
`dry-run-c.txt:13`; `ACCEPT-CA-64: FAIL` in `dry-run-ca.txt:8`), never the sentence. The
docstring phrase "the same sentence in … every receipt" is therefore not literally true.
RevVerifyCa independently recorded the same wrap fact at `RevVerifyCa.md:87`.

**M6 — O filtered-mode contract still differs from its docstring.**
`--only TOOL` from the lane root prints only 9 lines and a full verdict:

```text
TOOL PASS path=tools/reopen-row.py exists=True executable=True
EDGE_SCHEMEREL SKIP … EDGE_5TH200 SKIP
DRIP SKIP
MUT SKIP
ACCEPT-O-64: PASS
exit 0
```

The 13 CORE legs print nothing at all (`run_core` gate at `:462`; `leg()` filter at `:456`),
contradicting "legs not run print `<LEG> SKIP` and do not count" (`:18-19`), and a valid
single-selector run emits a full `ACCEPT-O-64: PASS`. Unknown selectors are now correctly
fail-closed: `--only NOSUCHLEG` and `--only EDGE_308,BOGUS` both print
`ACCEPT_O_INPUT_ERROR unknown --only leg(s): …` and exit 2 (ReviewerCounterO2 H1 repaired,
`:437-450`). The frozen no-`--only` command is unaffected.

### LOW

**L1 — declared instruments are not reproducible from the declaration commit.**
`accept-o.py` is untracked (`??`); all O receipts bind the working-copy sha. Tracked C/Ca at
`097c21d` are revision-0 blobs (`3519c9c8…`, `3a5a79d1…`); the current rev3/rev2 working
bytes are uncommitted (`M`). No revision commit exists yet (expected pre-data, but the
frozen predicate cannot be replayed from VCS history at this moment).

**L2 — Ca revision 1 is absent from the history and its cited forcing receipt is only a
base dry run.**
Header rev2 (`:2`) and history (`:40-45`) enumerate only revision 2; revision 1 exists only
as three inline comments (`:89`, `:97`, `:144`) and cites `telemetry/dry-run-ca.txt` as its
forcing receipt. That receipt is the base-tree rev0 dry run: six legs (REVNAMES absent),
`CANONLOG FAIL … prior_rounds=0`; it evidences the base's absence, not the falsified
counting logic (`## Round` count, over-broad PTRS scope) the rev1 code changed.

### Audit-window churn — resolved, but bind reports to the right hash

**R1 (C, fixed).** At `073e9716…` (02:53–02:56Z) `accept-c.py` used `row` before assignment:
`:296 teaches = cells(row)[6] if row else None` while the only `row =` store in `main()` was
`:300` (AST: Load 296, Store 300; no earlier binding). Reproduced in a shared clone at
`097c21d` with a probe entry citing S718: FILE/ROWS/REJECTS/ONEID printed, then
`UnboundLocalError: cannot access local variable 'row' where it is not associated with a
value`, no further legs, no label, exit 1. It was fixed at 02:56:55Z by moving
`row = reg_by_id.get(sid, [None])[0]` above the teaches guard (diff: one line moved). The
final `979050ce…` runs all 11 legs (probe ends `… RESTATE FAIL … LIVE FAIL …
ACCEPT-C-64: FAIL`, exit 1). Any citation of the crash must name `073e9716…`, not the final
bytes.

**R2 (Ca, twice revised, fixed).** `a8088092…` (rev2) passed all 7 legs on the lane root at
02:54Z (my run: `ACCEPT-CA-64: PASS`, exit 0; also RevVerifyCa). It was replaced at
02:57:32Z by `63510c4d…`, which crashed with `NameError: name 'r64_log' is not defined` at
`:157` after five legs (I reproduced it from the lane root; the defining block had been
deleted). It was replaced again at 02:58:58Z by `7319ff4b…`, which restores
`r64_heading`/`r64_log` at `:155-162`; my 02:59Z run prints all 7 legs PASS and
`ACCEPT-CA-64: PASS`, exit 0. All three bytes are stamped revision 2 (see M1).

## Drift matrix (final bytes)

| claim | frozen predicate sentence | claims `legs` == printed == `leg()` AST | revision stamp | receipts |
|---|---|---|---|---|
| C | content-equal to claims.json; raw docstring differs by one hard-wrap LF | 11 == 11 == 11 (set equality; runtime order FILE first, then ROWS…LIVE; probe at `979050ce…` printed all 11) | header 3; body labels 1 and 4 unlisted | only `dry-run-c.txt` at rev0; no post-fix run |
| O | content-equal; one hard-wrap LF | 23 == 23 == 23 (set equality; full-run receipt order matches claims; filtered run prints only 9 lines) | header 4 == bytes 4, but rev4 has no valid m5 mutant (H2) | all four receipts measure rev3; rev4 unmeasured and currently unpassable; rev1/2 cited sha absent |
| Ca | content-equal; one hard-wrap LF | 7 == 7 printed PASS at `7319ff4b…` (02:59Z) and at `a8088092…`; `63510c4d…` died after 5 legs | header 2 covers three byte states (`a8088092…`, `63510c4d…`, `7319ff4b…`) | no `final-measures-ca.txt`; RevVerifyCa measured only `a8088092…` |

## Residual risk and verification gaps

1. **No rev4 O acceptance, and rev4 cannot pass as landed.** All four O receipts are rev3;
   before any rerun the m5 replacement (`:1056`) must be indented to the tool's block level
   (8 spaces for `if`, 12 for its body) and the revision stamp advanced, because the landed
   mutant is a `SyntaxError` (H2). The unknown-selector exit-2 path and the filtered `--only`
   contract were observed by me; the paired m5 run was observed by RevVerifyO2 (both legs
   FAIL on the rebuilt mutant, `rows=[]`). A new receipt bound to the fixed bytes is owed.
2. **Ca passes at current bytes but needs a fresh rev-bound receipt.** `7319ff4b…` defines
   `r64_heading`/`r64_log` (`:155-162`) and prints all 7 legs PASS (my 02:59Z run, exit 0),
   but existing Ca reports/receipts name the superseded `a8088092…` or the broken
   `63510c4d…`. The exact-sentence NITS is untested against legitimate paraphrase variants
   (possible over-narrowness) and against the phrase-aware forger boundary RevVerifyCa
   raised.
3. **C land has appeared but no full acceptance run exists.** During this audit the entry
   (untracked), 26 rows S718-S743 and six disposition rows S744-S749 landed in the working
   tree with modified `corpus/SOURCES.md`/`corpus/README.md`. I did not run the network LIVE
   leg or the full predicate; the final counter is clean on the probe path, but a post-fix
   acceptance run and its receipt are still owed, and H3 must be resolved (statement/export
   versus the three `queued` rows).
4. **M4's "exactly" is a claim-text overreach** unless the L1 either narrows the claims.json
   wording or adds an all-23-leg mutant run; a stamp/receipt alone cannot close it.
5. **Live construction site.** Counters changed repeatedly during this audit (C twice, Ca three times, O twice). If any byte
   differs from the table above, re-run this drift check; the findings are hash-bound.

## Provenance

- RevCounters seat report (owner of the counter edits): `.ufo/waves/round-64/w2/RevCounters.md`
  (44 lines, 4,792 bytes; mtime 02:55Z). It claims the predicate sentences were left intact
  (true at the sentence level, modulo pre-existing wrapping), reports revision 2 for Ca at
  `a8088092…` (now stale), and explicitly makes no post-edit run claims.
- Wave-2 verifier reports used as cross-checks: `.ufo/waves/round-64/w2/RevVerifyCa.md`
  (`a8088092…` verified, wrap note at `:87`, NITS-forger boundary at `:60-66`),
  `RevVerifyO2.md` (rev3-only verification; rev4 dependency), `CaReceipts.md`,
  `CriticRevCa.md`, `SeparabilityRe.md`, `ReportFrag2.md`.
- RevVerifyO2's live message during this audit reported the invalid m5 mutant; I rebuilt it
  independently from `accept-o.py:1056` and obtained the same mutant sha256
  (`795b8d19…`) and the same `SyntaxError: unexpected indent (line 605)` before reading
  their diagnosis, so H2 is double-witnessed.
- Wave-1 attack receipts corroborated: `ReviewerCounterC.md` (D1 citation vacuity),
  `CriticCa.md` (NITS bare-token flip), `ReviewerCounterO2.md` (H1 fail-open, H2 "exactly"),
  `ReviewerOReceipt.md` (M3 `bb0c74a4` absent).

No counter, receipt, row, log, index, or jj state was modified by this seat; the only lane
write is this report. No tools were installed or updated.
