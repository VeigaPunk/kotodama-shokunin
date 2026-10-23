# ReviewerClaims — claims.json / counters / seats / controls review

Seat: `kotodama-r64.ReviewerClaims` (nw1-spec.json, wave `kotodama-r64-w1b`, 32 seats).
Scope: `reports/round-64/claims.json` + docstrings of `reports/round-64/accept-{c,o,ca}.py`. Read-only review; no counters executed by this seat — evidence below is file reads, grep, and byte-compare. Tooling: nothing installed (stdlib + git only).

## 1. Separability statement — TRUE (verdict: PASS)

`claims.json.separability` asserts: C exports S718–S749 and lands `{entry, corpus/SOURCES.md, corpus/README.md}`; O and Ca export no id and land no path C reads; `reports/round-63/telemetry/revisions.txt` (Ca REVNAMES land) is read by no other claim's command; each predicate is scored by its own counter alone. Verified clause by clause:

- **accept-c.py** reads only C lands + frozen base + shared harnesses: `corpus/SOURCES.md` (worktree :162 and `git show ff30a205:` :167), `corpus/README.md` (:377), the entry (:148), `reports/round-61/reopen-quote.py` (:389, sha-pinned to base bytes), and subprocesses `tools/check-cited-lines.py` (:261) and `reports/round-28/readme/sweep.py` (:370) under `cwd=root`. No `LOG.md`/`SCORECARD.md`/`revisions.txt`/`accept-{o,ca}.py`/`telemetry/` reads (grep + full read of the 434 lines). Helpers carry no cross-land reads (`grep -nE 'LOG\.md|SCORECARD|revisions\.txt|accept-[a-z]' tools/check-cited-lines.py reports/round-28/readme/sweep.py` → no hits).
- **accept-o.py** reads only `tools/reopen-row.py` (`src = os.path.join(root, TOOL)` :450, opened :463, copied to a mkdtemp :468-470) and `__file__` (:1076, to re-run itself against mutant roots). Every `SOURCES.md`/`corpus/` reference is a fixture it *writes* inside `mkdtemp` workdirs (:505-506, :577, etc.) — never the repo registry. `.ufo/waves/round-63/w1/CtlORedirectEdge.md` appears only in docstring/comment (:6, :788), never opened. No Ca-land reads.
- **accept-ca.py** reads `LOG.md`, `corpus/LOG.md`, `SCORECARD.md`, `reports/round-63/telemetry/revisions.txt` (:52-55) — all Ca lands — plus `git show ff30a205:corpus/SOURCES.md` (:105). See nit N3.
- **REVNAMES uniqueness**: neither accept-c nor accept-o references `revisions.txt` (grep). TRUE.
- **Per-claim scoring**: each counter prints its own `ACCEPT-<id>-64` verdict from its own `legs` list (accept-c.py:429, accept-o.py:1111, accept-ca.py:153). TRUE.
- Bonus: `claims.json` leg lists match the code's `leg("NAME")` call sites exactly — C: 11, O: 23, Ca: 7 (in print order, REVNAMES correctly between DISPO and NITS).

## 2. Frozen predicate identity — PASS for claims↔docstring; see N4 for receipts

Byte-compared the three `claims.json` `predicate` strings against the "Frozen predicate … :" sentence in each counter docstring (normalizing the docstring's line wrap to one line):

- C: `ACCEPT-C-64: every leg of reports/round-64/accept-c.py prints PASS.` — claims.json == docstring (accept-c.py:49-51). IDENTICAL.
- O: `ACCEPT-O-64: every leg of reports/round-64/accept-o.py prints PASS.` — identical (accept-o.py:117-119).
- Ca: `ACCEPT-CA-64: every leg of reports/round-64/accept-ca.py prints PASS.` — identical (accept-ca.py:40-42).
- Receipt label: all three counters print `ACCEPT-<id>-64: {PASS|FAIL}` (accept-c.py:429, accept-o.py:1111/460, accept-ca.py:153); dry-run receipts show `ACCEPT-C-64: FAIL` / `ACCEPT-CA-64: FAIL` — label matches the predicate's `ACCEPT-<id>-64:` token, consistent with the rounds 57-59 convention. See N4.

## 3. review_only seat coverage — all four covered this wave (nw1-spec.json)

| review_only item | covering seat(s) | prompt evidence |
|---|---|---|
| topic fit of the entry to the lane province | **ReviewerEntry** (item 1: "topic fit — does the entry stay inside kotodama's province and out of lore's canon?"); **ConnectorOverlap** (province-boundary scan of sibling PROVINCE.md/MANIFEST.json); **CriticEntrySweep** (item 4 lore-boundary) | prompts at nw1-spec.json items ReviewerEntry/ConnectorOverlap/CriticEntrySweep |
| sentence support (bullet = faithful restatement of row quote) | **ReviewSupportA** (S718–S727), **ReviewSupportB** (S728–S736), **ReviewSupportC** (S737–S743 + S744–S749 dispositions), **ReviewSupportD** (8-row independent spot sample) — blind live re-open protocol, SUPPORTED/NOT-SUPPORTED/UNREACHABLE per row; **CriticEntrySweep** item 1 (clause asserting beyond source) | prompts enumerate same protocol |
| one-way pointing to partial owners | **ReviewerEntry** item 3: "one-way pointing — partial owners cited one-way, not restated" | nw1-spec.json ReviewerEntry prompt |
| lore handoff in final section | **ReviewerEntry** item 2: "the final section's lore handoff — does it hand off without claiming canon?" | same |

Note: the accept-c.py docstring's own "Review-only:" line (:53) names only "blind per-row support judgment, topic fit, sentence support" — shorter than claims.json's four-item list, and mentions neither one-way pointing nor lore handoff. Cosmetic; claims.json is authoritative and all four have seats.

## 4. Controls — all three realizable (verdict: PASS)

- **C** (sourceless stub + copied registry rows): realizable via `accept-c.py --root DIR` against a scratch worktree. ROWS fails because copied rows carry stale `opened`/`usedby`/quote values (:183-221); RESTATE fails on `no_novel_content_word` (:299-300) and `copy_run>12` (:312-313) for verbatim stubs; FILE/ONEID pass by construction, SWEEP needs a README index row — consistent with the "FILE/ONEID/SWEEP-shaped" wording. Seat **CriticClaims** is assigned to reproduce it. Receipt `telemetry/controls-c.txt` does not yet exist (pending).
- **O**: `grep -nE 'EDGE_|DRIP' reports/round-63/` → the round-63 counter has **no** EDGE_/DRIP leg (verified). A docstring-only patch to `tools/reopen-row.py` leaves GEN green (tool behavior unchanged) while MUT still fails: mutants are rebuilt from the tool's committed bytes (:1059, :1064-1074) and every MUT needle is executable code (:1016-1056), not docstring. Seat ExecCounterO pending. `control-o.txt` (singular) is in O's lands — naming asymmetry with `controls-c.txt` is cosmetic.
- **Ca**: "base tree fails every leg" verified — dry-run-ca.txt shows all six printed legs FAIL; the seventh (REVNAMES, added in rev1) must also fail because base `revisions.txt` — which existed at base but lacked names — is checked against `need = [8d2041fa, 38ec1316, 0c892ce, 80ff34c, final-measures-c.txt, final-measures-o.txt, rev-separability.txt, census-end.txt]` (:131-133). A prose-only commit cannot satisfy PTRS (requires literal `final-measures-{o,c}.txt` present and `final-measures.txt` absent), HISTOGRAM (`A 13 / B 11`-form correction token :115), or REVNAMES (eight literal strings). Mechanism: every leg is substring/regex over committed bytes plus one `git show` read — realizable. (The repaired `revisions.txt` now in the worktree does carry all eight strings.)

## Findings

### MEDIUM
- **F1 — Claim-C sentence wider than frozen predicate (citation coverage unenforced).** `claims.json` claims "26 registry rows S718-S743 ... **cited by it**", but no leg requires coverage: ROWS/APPEND count registry rows independently of the entry; RESTATE only constrains `- clause (S###)` lines that exist (accept-c.py:270-313, `leg("RESTATE", not restate_bad)` :314 — `cited` may be empty or a subset); ONEID only forbids multi-id lines. An entry citing 1-25 of the new ids — or zero — passes every leg while the claim sentence fails. Dry-run confirms the shape (`RESTATE PASS lines=0`, `ONEID FAIL` only via FILE-absent `check-cited-lines` exit). Proposed pre-data revision with forcing control: extend RESTATE (or ONEID) to require `set(cited) == set(NEW_IDS)`; the existing declared C control (stub+copied rows must FAIL RESTATE) already exercises a near-zero-citation stub, and a "cite only S718" control would pin the new clause. This is a predicate-vs-statement gap for the declaration seat (CriticClaims/ScribeClaimsJson territory), not a leg to weaken.

### LOW
- **F2 — REJECTS docstring overstates the leg.** Docstring :28-29 says disposition rows carry "ordinary re-open/status evidence recorded in the round-64 lesson Gate"; code (:233-244) checks only cell count, status ∈ {rejected, queued}, and the `REJECTED:`/`QUEUED-CANDIDATE:` + `; flip:` teaches shape — no lesson file is read (and `corpus/lessons/round-64.md` does not yet exist). The lesson-Gate evidence is staged separately (ScribeLesson prompt: "one row per new registry row S718-S749"). Recommend docstring revision marking the lesson-Gate clause as REC-review, or accept the leg as row-only. Forcing control if revised: a row meeting the teaches shape but absent from the Gate must fail REJECTS — that requires the lesson to exist before final scoring, so REC-review wording is the cheaper fix.
- **F3 — accept-ca reads a C-land path at BASE.** `git show ff30a205:corpus/SOURCES.md` (:105) is a path claim C also lands — the frozen-base read observes no C-authored bytes (C appends post-base) and matches the R63SEP "REC lands read by acceptance runs" dependency class (:148-150). Separability statement remains true (it claims only lands/exports non-crossing); noting the boundary read for completeness.
- **F4 — Docstring "same sentence ... in every receipt" is literally stronger than what counters emit.** Receipts carry the `ACCEPT-<id>-64:` verdict line, not the full frozen sentence (e.g. dry-run-c.txt:13). Convention-identical across rounds 57-59, and the printed label is the same token — flagging only because the docstring says verbatim-in-receipt. Precedent: round-59 claims.json `predicate_rule` describes it correctly ("the same label in every receipt").
- **F5 — Stale pin comment.** accept-c.py:75 comments "base 65b393e" (a round-61-era base); the code pins LOCATOR against the actual round base ff30a205 (:396-398). Comment-only; no behavior impact.

### Verification gaps (not defects; in-flight seats own these)
- `telemetry/final-measures-o.txt` (22 lines) ends at DRIP PASS — no MUT leg, no `ACCEPT-O-64` verdict line, no measured-revision header; `mut-o.txt`, `edge-o.txt`, `control-o.txt` absent. The rev3 MUT leg has no complete receipt yet; ExecCounterO's fresh run is the evidence to wait for. `dry-run-o.txt`/`dry-run-o-baseline-copy.txt` are identical 7-leg prefixes — early legs only.
- `controls-c.txt` absent; C control exercise is CriticClaims' ticket.
- `corpus/lessons/round-64.md` absent; ScribeLesson stages it.
- dry-run-ca.txt predates rev1 (6 of 7 legs printed); a rev1 base re-run would show 7/7 FAIL — consistent with, not contradicting, the control claim.

### Numbers spot-checks (claim statement arithmetic — all verified at base)
`git ls-tree -r --name-only ff30a205 -- corpus/knowledge` = 237; `corpus/knowledge/linguistics` = 29; registry row lines `^\| S[0-9]+ ` in `ff30a205:corpus/SOURCES.md` = 643; LIVE subset derivation `(n-717)%5==1` = {S718,S723,S728,S733,S738,S743} matching docstring.

## Per-item verdicts
1. Separability statement true: **TRUE** (with F3 boundary note).
2. Predicate identical claims.json↔docstring: **YES, byte-identical for all three**; receipt label carries the `ACCEPT-<id>-64` token + verdict (F4 cosmetic overstatement in docstring).
3. review_only coverage: **YES — all four items have assigned seats** in nw1-spec.
4. Controls realizable: **YES for all three**; receipts pending seats; F1 notes the stub control's ROWS failure relies on stale opened/status/quote fields, and a citation-coverage control is proposed for the F1 gap.
