# ConnectorPatterns — round 75, wave 1 (kotodama)

Seat: ConnectorPatterns (connector, leaf). Base `f556d1049fe651d3d63975600b13acd9fb686f15`.
Read only: `reports/round-75/claims.json`, `reports/round-75/ledger.json` (DRAFT, not edited), `corpus/lessons/round-73.md`, `round-74.md` (`## Gate`, `## Mistakes`, `## Corrections`, `## Routed to round 75`), `round-74-verifier-spotcheck.md`, the staged package read-only at `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/myth-symbol/narrative-structure-frameworks*.md` and `…/corpus/SOURCES.append.md`, and the wave spec `.ufo/waves/round-75/w1/spec.json`. Checks were read-only (`git show`, `git grep`, `git cat-file`, `python3` over committed bytes). No network fetches. No fixtures. No installs.

## Summary

| # | Pattern (recurring class) | Where it predicts a wrong row, entry, counter or self-assessment | Seat prompt that carries the guard |
|---|---|---|---|
| P1 | A number is not an identity: three id namespaces reuse the same numbers for different documents | staged `source:` ids and prose ids bound to unrelated lane rows; renumber map; REPOINTED/COLLCHECK legs | ScribeEntryBase, ScribeEntryAmend, ExecRenumber, ExecCCounter (REPOINTED), RevAssimilationContract |
| P2 | One document, several URLs; a row's scope does not cover the locators its entries cite; rows left without an admitted citing entry | locator cited outside the row's scope/window; `used-by` orphaned; two rows for one document | ScoutPersee1113, ScoutWaybackCarriers, ExecEvidence, ScribeEntryAmend, RevEntryQuality, CritCCounterVacuity |
| P3 | An access state (403, wall, JS viewer, 429, empty CDX body) asserted from one probe, one UA or one URL; a shell body stored as evidence; receipts printing ERROR under OK | reject reasons and "via wayback capture" bindings that flip with UA or capture; Gate rows for shells | ScoutUnipaWayback, ScoutWaybackCarriers, ScoutPersee1113, ScoutChinawriter2023, ExecEvidence, ScribeLesson |
| P4 | Ledger pairs red for the wrong reason (type mismatch, self-referential observe, absence observe, cross-repo observe, stated text not at stated_at, contradictory expected value) | Ca's BASEMISMATCH and min-pairs legs fail; the self-assessment is not a self-assessment | ExecLedger, MutCaLedger, CritCaVacuity, ExecCaCounter (observe-type legs) |
| P5 | Carry-over prose and first-match readers: staged dates, restated counts, first footer, first header block | entries keep `fetched 2026-10-23/24` against a 2026-10-27 Gate; two entries inside one file read as one; README/SHONEN/SKILL counts drift | ScribeEntryBase, ScribeEntryAmend, ScribeReadmeIndex, ExecSweepFix, ScribeLesson, ScribeSkillGates |

## P1 — A number is not an identity (three namespaces, one spelling)

Evidence (verified):
- Lane registry (base, 808 rows, last id S884) holds **different documents** under the staged numbers: `S744` = Dictionary.com "ushanka"; `S763` = Duggan, tafl games; `S864` = UNESCO "Carnival of Oruro"; `S865` = UNESCO "Flamenco"; `S866` = UNESCO "Talchum"; `S870` = ICKL (Labanotation); `S729`/`S730` = Neer et al. / Genesee; `S742`/`S743`/`S754` = unrelated lane rows. `git show f556d10:corpus/SOURCES.md`.
- The staged base file binds **S870 to the chinawriter 2023 page** (`narrative-structure-frameworks.md` line 32). The claims refuse staged S870 unless a quote locates; if the line survives a by-number rewrite, the entry's `source:` line names lane S870 (ICKL). The entry keeps S864/S865/S866 at lines 29–31; those are the staged ids for rows S888–S890 and they are lane ids of other documents at base.
- The staged package itself reuses numbers: in `SOURCES.append.md`, staged `S886` = kotobank 苗字, `S887` = 平安時代, `S888` = NDL 日本人名大辞典, `S889` = kotobank 日本人名大辞典, `S890` = Kałużyńska (onomastics), `S891` = Zhao et al. (names), `S892` = Novikov (constructed languages). The claims' `row_set` uses staged `S892` for the Marrone row (staged `S919`). Only a join by document is correct; a join by staged number maps the Marrone row onto a conlang paper.
- Amendment prose cites campaign ids: `narrative-structure-frameworks.amend-2026-10-23.md` (3× S744, "round 3's S744") and `…amend-2026-10-23c.md` (S763). Both resolve to unrelated lane rows.
- Round-74 measured the same class: a single-pass by-document substitution was needed because sequential per-id replacement re-maps (`round-74.md` §Gate, "simultaneous single pass").

Predicted wrong: any entry or report that carries a staged number after a rewrite that is not keyed by normalised URL; any prose id left in an entry; a REPOINTED leg that tests "the id exists" instead of "the id's row URL names the cited document".

Guard for seats:
- ScribeEntryBase / ScribeEntryAmend: every `source:` id is rewritten through the by-document map; every bare S-number in prose is either removed or given with its URL; S744, S763, S729, S730, S742, S743, S754, S870 may not appear as a lane id.
- ExecRenumber: map keyed by normalised URL; for each target id, assert the lane row's URL equals the document; refuse any target that collides with a `reg-ids` entry naming a different URL.
- ExecCCounter / RevAssimilationContract: REPOINTED must resolve id → row → URL and compare the URL, not only the id's presence.

## P2 — One document, several URLs; scope and orphan drift

Evidence (verified):
- Barthes 1966 (`comm_0588-8018_1966_num_8_1_1113`) is cited through the notice URL (staged S876 in the base entry; staged S885 in `amend-2026-10-23.md` with "§niveau de description, p. 5, and the concluding pages p. 26") and through page-level URLs `…_T1_0011_0000` (staged S917, `amend-2026-10-23c.md`) and `…_T1_0006_0000` (staged S921, `amend-2026-10-24.md`). Claim C folds all four into row S885.
- The staged S885 row says "full text via the Persée per-page transcription service" (`SOURCES.append.md` line 33). Claim C's kill rule names exactly that service as an access-control failure (QUALITY 10) if used through a gate. The amendment ground asserts "the per-page transcription service returns all 27 pages" with no receipt.
- Two staged rows describe the same document (S876 and S885, both the notice). The base entry cites S876 at line 4; the row-level renumber must rewrite it to S885.
- **Orphan rows.** Row S891 (staged S905, Barthes *S/Z*) is cited only by `amend-2026-10-23b.md`, which the claims list as refused. Row S892 (staged S919, Marrone) is cited only by `amend-2026-10-24.md`, also refused. Both are in `row_set`. Under the ROWS leg ("used-by exactly the admitted entries whose source: lines cite it") these two rows have an empty used-by set against an admitted set that never cites them. [INFERENCE from the claim text and the staged files: the claim as drafted cannot pass its own ROWS leg for S891/S892 unless the rows are dropped or the amendments are admitted.]
- Locator outruns the window: the base entry's header scope ("tier B, scoped to the article's own notice and opening paragraph", staged line 11) is narrower than what the entry body relies on (the "levels of description" account of the article). Round-74 item 5 records the same class (S877 cited outside its scope cell), and R73-M8 records locators one page early.

Predicted wrong: an entry that cites p. 5, p. 26, p. 30, p. 139 or p. 11 through a row whose window contains only the notice and the first paragraph; a row with an empty `used-by` set admitted anyway; a second row for the same notice admitted (W04-class duplicate-URL warnings already exist in the census).

Guard for seats:
- ScoutPersee1113: report the exact page-URL shape from the notice HTML; if a page-level endpoint answers through a viewer, a token or an access control, record that and stop. Never use a JS-viewer endpoint to read pages. Do not assert "27 pages" without a fetched page.
- ExecEvidence: the stored window must contain the locator text (page label or section heading) and the quote; `whole-document` only when the document's visible text is under 4096 characters.
- ScribeEntryAmend: each cited locator must fall inside the Gate window of its row; a locator outside it is removed or its row is re-scoped in a later round.
- RevEntryQuality: a locator check per `source:` line, not a document-level check.
- CritCCounterVacuity: flag every admitted row whose `used-by` set is empty, and every row whose `staged` list spans refused files.

## P3 — Access state from one probe, one UA or one URL; shells as evidence

Evidence (verified or measured in the repo's own records):
- Staged S919: "answers 403 to an automated client" for the live Marrone PDF, and the row binds a wayback capture (`web.archive.org/web/20251111222249if_/…`). No UA-bound record for either URL is in the staged text. Claim C's `row_set` lists the document as "(via wayback capture)". Predicted failure: a capture of a front-door 403 is often an HTML shell; the quote test must run on the body type, not only the text.
- Staged S876: "full text is served through a JavaScript viewer". No probe is recorded. The claim's kill rule makes any use of the persee page-level service through access control a failure.
- Repo precedents of one-probe errors: R73-M3 (Springer read as a wall from one UA; the wall was UA-gated the other way); R73-M7 (a CDX slug prefix with a literal `*` returned an empty body, not zero rows); round-73 S894 (Cambridge) answered 429 to both UAs and was filed as a rate limit, which QUALITY 16 reads as rate limiting, not UA-gating (`round-73.md` §Gate, refused rows).
- Receipt defect: `reports/round-73/telemetry/selftest-r3.txt` line 5 is `ERROR: base 8841ad3b… is not a commit in /tmp/r73-ca-selftest-yeg6vu1k/lane` and line 6 is `SELFTEST OK: 10 scenarios`. An ERROR line is printed under an OK verdict, and a `/tmp` path is in a committed receipt (the scratch rule forbids citing `/tmp`). Predicted: the same shape recurs in any selftest receipt of this round.

Predicted wrong: a reject reason that is UA-dependent (the S894 and S910 class); a "403" or "wall" that holds for one UA only; a stored evidence window taken from a shell that contains the quote text but not the document; a Gate row whose probed URL and response are not both recorded.

Guard for seats:
- ScoutUnipaWayback / ScoutWaybackCarriers / ScoutPersee1113: for each URL, both the default UA and the browser UA, each bound to its response (QUALITY 22); the CDX probe with a positive control in the same query shape (QUALITY 24); record the capture's body type and whether it embeds the same original URL (QUALITY 18); a challenge that is met and routed around by an ordinary copy is recorded as "met", not "passed".
- ScoutChinawriter2023: the staged chinawriter 2023 quote is located or refused on the page as it is served this round; no reuse of the round-72 refusal reason without a re-probe.
- ExecEvidence: refuse to write a window from a body whose type does not match the declared document (PDF vs HTML shell); record the body's first bytes or content type in the header.
- ScribeLesson: every Gate reject row carries probed URL, UA, HTTP status and bytes for the response it reasons about.
- Selftest receipts from counters (ExecCCounter, ExecCaCounter): no `/tmp` path in committed output; an `ERROR:` line makes the receipt's verdict non-OK.

## P4 — Ledger pairs red for the wrong reason (Ca)

I ran each of the 11 draft pairs' `observe_cmd` at base and checked the stated text against `stated_at` in the base tree (read-only):

| pair | disposition | what the pair actually measures at base | genuinely red? |
|---|---|---|---|
| L75-01 | REPAIR | SHONEN "412" vs registry 808 (`git grep -c` on SOURCES) | yes |
| L75-02 | REPAIR | README "30" vs `git diff --shortstat 4b825dc…` = 32 files | yes (shortstat counts files added since 4b825dc; 4b825dc holds 0 files there, so it equals the directory count today; any rename or delete breaks it) |
| L75-03 | REPAIR | README "36" vs shortstat = 40 files | yes (same caveat) |
| L75-04 | REPAIR | stated text "This instrument adds that leg." is wrapped across `sweep.py` lines 15–16, so a plain match at line 16 fails; observe counts `FOOTER_RE\.search` = 1 | no: stated text not found at stated_at; stated token is prose, observed is a count |
| L75-05 | ANNOTATE | observe counts the stated phrase in `corpus/lessons/round-74.md` itself (= 1 by construction); the rederive greps `reports/round-74/evidence/S883.txt` for a different phrase | no: self-referential; observe and rederive disagree |
| L75-06 | ANNOTATE | same as L75-05 for S884 | no: same class |
| L75-07 | REPAIR | stated text "the QUALITY 23 addendum" is absent from `round-74.md:208`, which holds `**QUALITY 23 addendum**` (bold markup breaks the match); observe `re-pointed read path` in QUALITY.md returns nothing | no: stated text absent; absence observation; `expected_after` says 0 while `why` says the leg expects 1 |
| L75-08 | ANNOTATE | observe runs `git grep … 3a74016…` in the lane; `git cat-file -t 3a74016…` fails in the lane repo, so the observe returns nothing | no: cross-repo; the fleet pin is not in the lane |
| L75-09 | ANNOTATE | stated text "min-pairs gate FAIL" is not at `selftest-r3.txt:6` (line ends `min-pairs gate FAI`); `stated_parse` needs parentheses the file lacks | no: stated text absent; parse mismatch |
| L75-10 | ANNOTATE | observe `ls .ufo/waves/round-74/w2` returns filenames; the stated token is the number 43 | no: type mismatch (list vs count) |
| L75-11 | REPAIR | observe `git grep -c 'SELFTEST: 10/11' … reports/round-72` returns nothing | no: absence observation (ledger status forbids these) |

Count: 3 pairs are clean reds (L75-01, 02, 03). L75-04/05/06 are red only by type mismatch. L75-07/09/11 fail the stated-text or absence rules. L75-08 cannot be observed in the lane. The ledger status says the counter "drops every pair that is not red", so the draft file falls well under the `>= 10 unique pairs` and `>= 10 BASEMISMATCH` legs unless it is repaired before the freeze. [INFERENCE from the counter's stated rule; the counter itself is not in my read set.]

Predicted wrong: Ca's `BASEMISMATCH` and min-pairs legs red at freeze; ANNOTATE rows whose "observed token" is the stated line's own text; a correction row whose re-derivation command returns nothing and so cannot "return the observed token".

Guard for seats:
- ExecLedger: for every pair, (a) `stated_text` found at `stated_at` in the base tree after plain match; (b) stated token and observed token have the same type (number vs number); (c) the observe command does not read the `stated_at` file for the stated phrase; (d) no zero-output observe; (e) observe runs in the lane repo only; (f) one `expected_after` value that agrees with `why`.
- MutCaLedger: mutants for each class above (type mismatch, self-reference, absence, cross-repo, wrapped stated text, bold markup, contradictory expected).
- CritCaVacuity: the same six checks against the draft, reported as findings for the L1.

## P5 — Carry-over prose and first-match readers

Evidence (verified):
- Staged provenance dates are carried into the entries: `narrative-structure-frameworks.md` line 4 ("fetched 2026-10-23"), `amend-2026-10-23.md` lines 4–5 ("fetched 2026-10-23"), `…amend-2026-10-23b.md` line 4 (2026-10-23), `…amend-2026-10-23c.md` line 4 (2026-10-23), `…amend-2026-10-24.md` lines 4–5 (2026-10-24); recheck cells "(ran 2026-10-23)" / "(ran 2026-10-24)". Claim C's Gate and SOURCES rows use 2026-10-27. Nothing in the ENTRIES leg checks an entry date against the row's opened date; the ENTRIES leg only rejects placeholder header values.
- Two entries in one file: `narrative-structure-frameworks.md` has an H1 at line 2 (Western anchor, S876) and a second H1 at line 27 (Chinese and Japanese theory, S864–S870, with its own `source:` lines 29–32). The file totals 940 words. An ENTRIES leg that reads the first provenance header and a word count will pass the file with the second block's ids unchecked. [INFERENCE from the leg text; the claim has one entry path per file.]
- First-match readers: `reports/round-28/readme/sweep.py` grades `FOOTER_RE.search(text)`, which is the first `Counts checked` footer (L75-04; round-74 M3). Any counter that reads the first match of a repeated block reads a stale value once a footer is appended.
- Restated counts drift: README `## linguistics/ (30)` vs 32 files; `## culture-material/ (36)` vs 40 files; SHONEN "412 rows" vs 808; `SKILL.md:701` "measured SELFTEST: 10/11" with no receipt (L75-11); round-74 R74-M4 (9 vs 10 scenarios). Each count written in prose without a pinned command drifted within one round.

Predicted wrong: entries that carry 2026-10-23/24 provenance next to a 2026-10-27 Gate; a second entry inside a file whose ids no leg checks; README footer and SHONEN/SKILL/LOG counts written from memory for the round's new totals (`808+k`, `249+k`, `legs=13/13`); a sweep that reads the first footer.

Guard for seats:
- ScribeEntryBase / ScribeEntryAmend: entry `fetched` and `verified-at` lines carry the Gate access date (2026-10-27) or cite the earlier capture explicitly with its date; one provenance header per entry file; a second entry is a second file or it is refused.
- ScribeReadmeIndex: the new footer is generated by a command at lands; earlier footers stay byte-identical; the per-directory vector is recomputed from the live tree.
- ExecSweepFix: read the last `Counts checked` footer; prove it on a two-footer fixture (the first-footer red is the regression).
- ScribeLesson / ScribeSkillGates: every count in the lesson or SKILL row carries its command; no "measured" without a receipt path.

## Verification performed

- `git show f556d10…:<path>` and `git grep` for the base-tree checks in P1, P2 (ground fragments: 0 rows for `comm_0588-8018_1966`, `jw.ucass`, `jstage…/jcss`, `jstage…/jsik`, `unige.ch/lettres/framo`, `iris.unipa` — confirmed), P4 (each pair's observe at base; stated_text presence at stated_at), P5 (counts 32/40 at base; 0 files at 4b825dc).
- `python3` over `reports/round-75/ledger.json` (11 pairs confirmed) and `SOURCES.md` (808 rows under the claim's regex, confirmed).
- Not run: any counter, any network fetch, any build or test. Checks are for the L1 and the freeze wave to re-run under the frozen counters.

## Tooling and scratch

- Installs: none.
- Scratch: `/fast/scratch/hyaku/kotodama-r75/ConnectorPatterns/` created empty and removed before yield. No fixture, clone or fetch was made.
- Writes: this file only.
