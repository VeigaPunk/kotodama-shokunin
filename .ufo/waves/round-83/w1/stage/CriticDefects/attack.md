# CriticDefects — attack on claim-C repairs and the round-82 routed-defect dispositions

Seat: CriticDefects (critic, leaf). Round 83 wave 1. READ-ONLY; this file is my only stage write.
All lane evidence is quoted at base `3088bd7fe2a55a123214abba7008dcddf12b301c` (base) or `21277b089e3c64c247bb4e0fcb033abfdfa1e668` (freeze) unless named otherwise. Frozen claim text: `reports/round-83/claims.json` @ freeze, `claims[2]` (id C) / `repair83`. Seat contracts: `.ufo/waves/round-83/w1-dispatch.json` tasks `ScribeRecord`, `ExecCitedRecords`, `ScribeRows`.
Convention: `«SCRATCH»` below denotes the fast-scratch root named by criterion 31 (an absolute path rooted there must not appear in a committed report this round); every citation below gives file, line, and the resolvable tail after the root.

## Verdict summary

| # | Finding | Class | Impacted axis |
|---|---|---|---|
| F1 | All five claim-C before-states verified; two arithmetic corrections to the round's own framing | verified + minor | calibration |
| F2 | Erratum direction is honest (filed `line 7` uncorroborated; committed bytes say `line 5`), but the ScribeRecord pointer names a receipt location that does not exist | fixable defect | calibration |
| F3 | The ExecCitedRecords mandated proof is unsatisfiable under the frozen document set; the two routed scratch receipts are outside the checker's scope | fixable defect | calibration, operability |
| F4 | Criterion 31's clause (ii) intent is wider than the checker measures (telemetry/.ufo receipts never scratch-graded; Gate clause (iii) unenforced) | tradeoff — must be named as a limit, else defect | calibration |
| F5 | S913 shape satisfies the census grammar and CORPUS rule 2 by construction; S908 stays valid history | verified | calibration |
| F6 | §6 item 7 (claim-O before-wording) is undispositioned anywhere in this round | fixable defect (low) | calibration |

---

## Task 1 — claim-C before-states, verified byte by byte at base

**1a. The record is 0 bytes.**
`git -C <lane> cat-file -s 3088bd7fe2a55a123214abba7008dcddf12b301c:reports/round-82/counter-revisions.md` → `0`. The file exists in the tree as an empty blob (it is also the only `.md` under `reports/round-82/` at base — `git ls-tree -r --name-only <base> reports/round-82/ | grep '\.md$'` returns exactly it). It is still 0 bytes at freeze 21277b08 (`git diff --stat 3088bd7f 21277b08` adds only the 13 `reports/round-83/*` files).

**1b. The three citing documents.**
- `corpus/lessons/round-82.md:12`: "r2 `696835ee…` and r3 `ea667212…` are recorded in `reports/round-82/counter-revisions.md`."
- `SCORECARD.md:1663`: "(`reports/round-82/counter-revisions.md`). Do-nothing control: at" (the round-82 counter-revision paragraph naming r2 `696835ee5a8f…`, r3 `ea667212554f…`).
- fleet closure report (outside the lane, child repo of the fleet root) `.ufo/reports/round-82/kotodama.md:51`: "(`counter-r2-caught.txt`). Record: `reports/round-82/counter-revisions.md`."
A fourth document cites it as a *defect*, not as the record: `corpus/lessons/round-82-verifier-spotcheck.md:207-208` ("Empty record cited as evidence. `reports/round-82/counter-revisions.md` is 0 bytes at `1d650c8c`…"). That matches the frozen before-text ("three committed documents cite it as the r2/r3 record") and matches §6 item 1 ("the report …, SCORECARD and the lesson").

**1c. No criterion 31.**
`git show <base>:corpus/QUALITY.md | grep -c '^31\. '` → 0; the numbered criteria run 28 (`:150`), 29 (`:199`), 30 (`:207`); the file tail is criterion 30's grounding/limit prose. `grep -n cited-records` over the whole base tree → 0 hits; the tool exists at neither base nor freeze.

**1d. S908's teaches/anchor cells** (`corpus/SOURCES.md:864`, full row read):
- `teaches` (cell 6) opens `rejected: framework status — the unilinear stage law is the Frazerian evolutionism QUALITY 2 bars from load-bearing use, …` — lowercase `rejected:`, while the registry's house spelling is `REJECTED:` (19 base rows open teaches with `REJECTED:`, e.g. S028 `:57`, S029 `:58`, S030 `:59`).
- `anchor` (cell 5) is `quote located: 「magic is a spurious system of natural law as well as a fallacious guide of conduct」 (16 words)` — a quote with no chapter/page locator. The "chapter III" location lives only in `reports/round-82/evidence/reject-golden-bough.txt` (cited from S908's source cell).
- status `rejected` (cell 7), opened `2026-11-04` (cell 8), recheck `365d` (cell 9), used-by `—` (cell 10). Row parses as exactly 11 cells.

**1e. The two fast-scratch-root citations in round 82's receipts** (the two §6 item 6 routed; tails after «SCRATCH»):
- `.ufo/waves/round-82/w1/stage/ExecEvidence/malformed-row-probe.txt:4, :9, :14` — the probe's three command lines each carry a fixture path under «SCRATCH»/hyaku/kotodama-r82/ExecToolControls/.
- `reports/round-82/telemetry/quality30-probe.txt:21, :23` — `122055 «SCRATCH»/hyaku/kotodama-r82/L1/quality30/mint-cap.html` and its sha256 line.
**Arithmetic correction (F1):** the routing undercounts. Five more committed r82 artifacts carry absolute scratch paths and were NOT routed: `reports/round-82/telemetry/controls-d.txt:2, :6, :27`; `controls-o.txt:2, :6, :26`; `junk-d.txt:6, :17, :26`; `junk-o.txt:6, :18, :29`; `.ufo/waves/round-82/w1/stage/ExecToolControls/controls.json:372`, `controls.md:290`. So r82's scratch-bearing committed receipts = 7 files, of which §6 named 2. Criterion 31's grounding should say "seven", or the limits should say the routing sampled two; saying "the two" lets a future closure claim coverage that was not routed.

## Task 2 — is the erratum honest?

**Filed claim is `line 7`, twice:** `corpus/lessons/round-82.md:94` (R82-M2 row, last cell: "the malformed-registry path is separately proven by a hand-written 12-cell fixture (`RECHECK-ERROR line 7: row has 12 cells, expected 11`, exit 2)") and fleet `.ufo/reports/round-82/kotodama.md:39` ("(`RECHECK-ERROR line 7: row has 12 cells, expected 11`, exit 2). Lesson R82-M2.").

**Which file actually says which:** every committed byte that exists says `line 5`, none says `line 7`:
- `.ufo/waves/round-82/w1/stage/ExecEvidence/malformed-row-probe.txt:7` — stdout `RECHECK-ERROR line 5: row has 12 cells, expected 11` (and `:17` for the 10-cell case).
- `corpus/lessons/round-82-verifier-spotcheck.md:72` — the non-author re-run: `RECHECK-ERROR line 5: row has 12 cells, expected 11  # exit 2`.
- `.ufo/waves/round-82/w1/ExecEvidence.md:48` — "12-cell row → `RECHECK-ERROR line 5: row has 12 cells, expected 11`".
- Counter-fixture context: another seat's independently built fixtures legitimately print `line 9` (`.ufo/waves/round-82/w1/ExecToolControls.md:34, :41`) — the number is fixture-relative, so `line 7` is not impossible in principle; it is **uncorroborated by any committed receipt**.

**Honesty judgment:** an erratum stating "filed `line 7` (lesson :94, fleet report :39) vs committed `line 5` (probe :7, spot-check :72); filed bytes stand as history" is honest and matches the frozen markers (`R82-M2`, `line 5`, `line 7`). An erratum that merely contains both strings without asserting `line 5` is the committed truth would satisfy the letter and dodge the finding — the seat spec forecloses this by wording ("the filed … vs the committed …"), keep that wording.

**F2 (fixable defect):** ScribeRecord's task (b) says the erratum names "the committed `line 5` in `reports/round-82/telemetry/`" — but `git grep -n 'line 5' <base> -- reports/round-82` returns **nothing**; no committed telemetry file prints it. The committed locations are the stage probe (above) and the spot-check `:72`. An erratum citing `reports/round-82/telemetry/…line 5` would point at a nonexistent receipt — on day one of criterion 31, clause (i)'s "resolvable at the cited revision" would fail inside the erratum itself. Smallest correction: ScribeRecord cites `.ufo/waves/round-82/w1/stage/ExecEvidence/malformed-row-probe.txt:7` + `corpus/lessons/round-82-verifier-spotcheck.md:72` (both repo-relative, both resolve at base).

## Task 3 — criterion 31 testability and the checker's scope

The checker `tools/check-cited-records.py` does not exist yet at base or freeze; what exists frozen is its contract: `repair83.checker_*` in `reports/round-83/claims.json` @ freeze, plus the `ExecCitedRecords` seat task. I judge the contract; the landed `.py` must not drift from it (QUALITY 23/28 pin the bytes at grading).

**What clause (ii) forbids, as contracted:** in round-k documents (k ≥ --bind-round, default 83), any absolute path rooted at `/tmp`, `/var/tmp`, or the fast-scratch root; and (EMPTY leg, k ≥ --from-round) any backticked repo-relative token matching `(reports|corpus|tools|\.ufo)/…\.(md|txt|json|py|tsv|yml)` that resolves to a 0-byte file. Output one `CITED-RECORDS: <empty> empty / <scratch> scratch` line; exit 0 iff both 0.

**Scope boundary (which reading the frozen contract implements):** documents are exactly `<root>/reports/round-<k>/**/*.md` and `<root>/corpus/lessons/round-<k>*.md`. That is: round reports' *markdown only* — not `reports/round-<k>/telemetry/*.txt` receipts — and the round lesson *plus its verifier-spotcheck sibling* (the glob `round-82*` admits `round-82-verifier-spotcheck.md`). It never opens `.ufo/waves/**` (a `.ufo/waves/…` path can only appear as a *cited token* in the EMPTY leg, never as a document whose own text is scratch-scanned), and never opens a `.txt` receipt for its own content. So: it grades `reports/round-NN/**` *markdown* and `corpus/lessons/round-NN*` — nothing else.

**Letter-satisfying / intent-violating sentence (primary):** a round-83 receipt file `reports/round-83/telemetry/controls-o.txt` containing `command: python3 -B reports/round-83/accept-o83.py --root «SCRATCH»/hyaku/kotodama-r83/L1/jf/work/fx-o …` — i.e., exactly the shape of r82's own controls receipts (controls-d.txt:6, controls-o.txt:6). The checker grades documents only; this file is not a document → `CITED-RECORDS: 0 empty / 0 scratch`, exit 0, while clause (ii)'s intent ("a committed receipt cites only repo-relative paths") is violated. **The checker does not catch it.** This is not hypothetical: it is the round-82 precedent the criterion grounds itself in.
**Secondary dodge:** a lesson citing `reports/round-83/telemetry/run.txt` that is never committed — "a token that does not resolve is NOT a finding" → passes. Bounded only partially: `tools/check-orphan-evidence.py` (at base) scans fleet closure reports + lane spot-checks for never-committed citations, not `corpus/lessons`; a lane-lesson citation to absent bytes is caught by nothing this round.

**F3 (fixable defect — the strongest counterexample in this attack):** the `ExecCitedRecords` mandated proof — "at `21277b08` with `--bind-round 82 --from-round 82` it must catch … the two fast-scratch-root receipts" — is **unsatisfiable under the frozen document set**. At 21277b08 the only in-scope document containing a scratch root is the spot-check's own routing prose (`corpus/lessons/round-82-verifier-spotcheck.md:233`, quoting «SCRATCH»/… with an ellipsis); both routed receipts are `.txt` outside both globs (one is under `.ufo/waves/`). A faithful implementation cannot print two scratch findings; an implementation that "catches the two receipts" must have widened the document set past the frozen contract — a QUALITY 23/28 predicate drift. The proof line is internally inconsistent with the contract it proves. Smallest safe correction (pre-freeze, no predicate move): either (a) amend the proof to "catches the spot-check's in-scope self-quote at :233 and the empty-record finding; the two routed receipts lie outside the document globs — disclose this as criterion 31's stated limit", or (b) extend the document set to `reports/round-<k>/**/*.txt` for k ≥ bind-round — viable because the round's own frozen telemetry is scratch-clean (I grepped `controls-c/d/o.txt`, `census-start.txt`, `smoke-c.txt` at 21277b08: zero scratch roots), so the round-83 green at lands is not self-tripped; record the choice in `reports/round-83/counter-revisions.md` if any frozen counter byte moves (QUALITY 23).

**F4 (tradeoff that must be named, else it is a defect):** clause (iii) (Gate rows carry URL + access date) is prose-only — the checker has no Gate leg; clause (ii)'s "resolvable at the cited revision" is also not implemented (resolution is against the *run-time* tree, not the cited revision). Calibration rule: a criterion may claim less than a tradeoff leaves on the table only if the limits sentence says so. ScribeRecord's task already seeds the right limits ("path lists are not citations; no earlier round is retro-fitted"); it must add: "the checker grades the two document globs; receipts under `telemetry/` or `.ufo/waves/` are graded only when a document cites them, and never for their own scratch text; unresolved tokens are not findings."

## Task 4 — the S913 superseding row shape

Contract (ScribeRows task): draft only, `{WAVE}/stage/ScribeRows/S913.row`; teaches starts `supersedes S908 — `, carries `REJECTED:` with the reason; anchor names `chapter III` (Frazer's stage law) and no quote; used-by `—`; L1 appends under claim C.

**Census grammar — no cell can fail, by construction:**
- `scripts/sources-census.sh validate` (fleet; the exact binary ScribeRows must run): E01 needs 13 fields (11 cells) — the row copies S908's shape; E02 id `S[0-9]{3,}`; E03 duplicate id (S913 is new); **E04 duplicate URL+scope is doubly exempt** — guard at ~`:646-650` fires only when the current row's `status!="rejected"` *and* the URL was previously seen at a non-rejected row *and* `teaches !~ /supersedes S[0-9]{3}/`; S908's row is `status rejected` (so `url_scope_nonrejected` never sets) and S913's teaches matches `supersedes S908` — either arm alone defeats it; E05 kind `book`; E06 tier `[ABC]`; E07 status ∈ {queued, mined, rejected}; E08 opened ≤ today (`2026-11-04` is today); E09 recheck (copy S908's `365d`); E10 community-at-A; E11 used-by (the `—` null marker is the no-check case). W02 thin-reject (`length(teaches)<8`) is warning-only and moot for a reasoned row. **No cell fails `sources-census.sh validate`; exit 0 is reachable.**
- Two cells the frozen contract leaves unpinned (not census risks, calibration notes): `status` — recommend `rejected` (keeps W01/W03 moot and matches a teaches whose operative verb is `REJECTED:`; `mined` would trip W03 as a warning); `opened`/`recheck` — copy S908's.

**CORPUS rule 2 — satisfied by design:** fleet `CORPUS.md` rule 2: "Append-only. Only `status`, `recheck` and `used-by` change in place … **A correction is a new row whose `teaches` opens `supersedes S0NN —`.**" S913 is exactly that form; S908's cells stay untouched (the claims' append-only legs pin existing rows to the status/opened/recheck/used-by columns; S908 needs zero in-place change — the correction is the append).

**S908 as history — stays valid:** rule 2's own rationale plus the rule-1 preamble ("`rejected` (kept — a rejection is evidence of taste)"): S908 remains the filed record of why the framework was refused; S913 supersedes its *shape* (spelling + missing chapter locator), not its verdict. The frozen after-text ("existing registry rows differ only in their status/opened/recheck/used-by cells across base..lands") is compatible with S908 unchanged.

**One letter-tension to close (fixable):** CORPUS rule 1 says the round lesson's `## Gate` records, "for every new row, the URL, the access date, and a ≤25-word quote with its location" — S913 is a new row whose frozen anchor contract is *no quote*. The smallest reconciliation that keeps both authorities: the r83 Gate entry for S913 names URL + access date (2026-11-04, inherited from S908's own opened date and capture record) + the chapter-III location, and states the ≤25-word located quote already lives committed in `reports/round-82/evidence/reject-golden-bough.txt` (rule 1 says quote "with its location grounding teaches"; a pointer to the committed located quote grounds it without inventing a fresh capture — ScribeRows' contract gives S913 no capture receipt, and rule 1's "write it only after opening the source in the round that writes the row" is satisfied by the r82 capture record S913's source cell already cites). If the L1 instead wants a fresh quote, that is a frozen-contract amendment, not a scribe choice.

## Task 5 — §6 items 1–7 vs what round 83 lands

| §6 | Routed defect | Round-83 disposition | Judgment |
|---|---|---|---|
| 1 | 0-byte record cited as evidence | ScribeRecord (a): record >400 B, names both hashes `696835ee5a8f…`/`ea667212554f…`, reconstructed only from the four committed receipts (`counter-r1-redbefore.txt`, `counter-r2-caught.txt`, `lands-o82-graded-r3.txt`, `selftest-o82-r3.txt` — all four exist at base; R82-M6 grounding exists at lesson `:100`), opening line disclosing the round-83 restoration. Counter-graded (RECORD leg). | DISPOSITIONED |
| 2 | R82-M2 line erratum | errata-r82.md with markers `R82-M2`/`line 5`/`line 7`; filed bytes stand. Counter-graded (ERRATUM leg). | DISPOSITIONED, with F2's citation fix (point at the stage probe + spot-check :72, not `reports/round-82/telemetry/`). |
| 3 | Gate registry rows missing (rounds 76–82 standing gap + r83's 3 counters) | claim O: `tools/check-gate-registry.py` + 14 rows by ScribeRegistryRows. Counter-graded (O legs). | DISPOSITIONED |
| 4 | Lesson `## Gate` omits per-row URL/access date | criterion 31 clause (iii), binding from round 83. No checker leg enforces it; no wave seat owns `corpus/lessons/round-83.md` (the 14 dispatch seats: ScoutGap, ScoutSources, ExecRegistryCensus, ExecGateRegistryTool, ScribeRegistryRows, ExecCitedRecords, ScribeEntry, ScribeRows, ScribeRecord, ConnectorOverlap, CriticClaims, CriticDefects, MutationTester, SentinelScope). | PARTIAL: the standing rule lands; this round's own Gate is the first ungraded instance (L1 integration owns it). Name that in the criterion's limits. |
| 5 | S908 row shape | superseding row S913 (drafted by ScribeRows, appended by L1). Counter-graded (SUPERSEDE leg); census-safe per Task 4. | DISPOSITIONED |
| 6 | Scratch-path commands in committed receipts | criterion 31 clause (ii), binding from round 83; checker grades the two `.md` globs only — the two routed receipts (and the five unrouted ones, F1) are outside its scope. | PARTIAL by design; the limit must be written into criterion 31 (F4) and the proof corrected (F3), else the round ships a criterion whose own grounding defects are invisible to its instrument. |
| 7 | Claim-O before-wording ("nothing read the registry's `recheck` cells" → "no tool derived a due date or queue") | **Nothing in the frozen claims, the errata contract, or any seat task addresses it.** | UNDISPOSITIONED (low). Smallest correction: one sentence in `reports/round-83/annotations/errata-r82.md` recording the narrower wording as the proven statement; the file is free-form beyond its three required markers, and §6's routing closes 7/7 only if item 7 is named somewhere committed. |

## Stop condition

This is the assigned review. I did not judge, admit, edit, integrate, or ship any claim artifact; the L1 integrates. No counter, claim file, registry row, receipt, or fleet byte was modified by this seat — only this stage file and the seat report `.ufo/waves/round-83/w1/CriticDefects.md`.
