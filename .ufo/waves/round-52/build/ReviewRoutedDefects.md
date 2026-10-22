# ReviewRoutedDefects — round 52, repair-first audit of the round-51 routed defects

Assigned item: for each routed defect in `corpus/lessons/round-51-verifier-spotcheck.md:121-129` and the S094 disagreement at `:108`, state what round 52 does or why not, as a table; verify defect 4 by hand; list any `corpus/lessons/operator-*.md` teaching not reflected.

Method: every command and byte cited below was re-run or re-read by this seat at the lane worktree on 2026-10-22. Tree state at read time: prerequisite `147cfde`, claim D landed `dea5ece` (worktree contains D's diff; claim C not yet landed — `find corpus/knowledge -name '*.md' | wc -l` → 227). No tool installed or upgraded.

## Disposition table

| Routed item | What round 52 does | Evidence | Verified by this seat |
|---|---|---|---|
| S094 disagreement (`round-51-verifier-spotcheck.md:108`) | New QUALITY criterion 10 (ordinary access) at `corpus/QUALITY.md:37`; checker `tools/check-source-access.py` (status leg + cited leg, `--selftest`); S094 `status` mined → rejected, `used-by` → `—` (`corpus/SOURCES.md:123`); superseding rejected row S132 with reason and flip (`corpus/SOURCES.md:161`); mined as mistake R52-M1 (drafted, `.ufo/waves/round-52/build/ScribeMistake.md` §1–2) | `corpus/lessons/round-52.md:16`; prereq receipt `reports/round-52/telemetry/prereq-access-check.txt` (selftest 10/10 PASS; live run at `2b956d7`: "ACCESS: 1 flagged rows, 6 findings", exit 1; `curl` re-open → `http=403 server=cloudflare cf-mitigated=challenge`) | Re-ran checker on worktree: `ACCESS: 2 flagged rows, 0 findings`, exit 0 (S094 + S132 both flagged, both rejected, neither cited); `--selftest` exit 0 |
| 1. D statement wider than its counter (`:123`) | Row not anchored — the `civilizations/` row stays a directory (`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:29,:43`). Worded out instead: round-52 D's statement is the exact predicate of its counter ("0 lines that cite S094" vs the awk line counter); C's statement lists only clauses its acceptance command checks | `corpus/lessons/round-52.md:17`; `reports/round-52/claims.json` claim D statement + `counting_command` | The note at entry `:29` (directory-row qualifier) already landed at `e6b6629`, before the round-51 lesson commit — the spotcheck's defect 1 was partly stale when routed; the row-level option stays open |
| 2. S094 sole-support details (`:124`) | Claim D at `dea5ece`: 5-line 1:1 re-cite. `:83` parameters → S071+S096, palm orientation → S096 ("fourth phonological parameter"); `:87` handshape → S097 ("45 possible handshapes … only 7 … passive"); `:90` orientation pair → S096 (CHAIR/NAME); `:92` two-handed → S097 seven shapes A,S,B,5,G,C,O + `(to-verify)` on the 1974 six-shape set; `:93` pairs → S096, CAR/WHICH and OFFER/MAYBE cut | `corpus/lessons/round-52.md:18`; diff `git diff 147cfde dea5ece -- corpus/knowledge/linguistics/sign-languages-manual-modality.md` (5 insertions, 5 deletions, lines 83/87/90/92/93) | Counter: awk → 5 at `147cfde` (lines 83, 87, 90, 92, 93 confirmed), 0 at worktree; no S134+ id in the entry; SOURCES untouched under D. Re-opened S096 by ordinary `curl` today: page carries APPLE, ONION, SHORT, CHAIR, NAME (also CAR, WHICH, TRAIN) and does **not** contain OFFER/MAYBE — the cut matches the page |
| 3. Gate locators (`:125`) | Half-dispositioned: S097's locator fixed by superseding anchor-only row S133 (`corpus/SOURCES.md:162`), and the study path now reads S071 → S096 → S133 → S095 → … (`corpus/SOURCES.md:197`) | `corpus/lessons/round-52.md:19` | The defect's second sentence — the four-row list S071, S076, S089, S090 — is dispositioned nowhere: `grep -c 'supersedes S071\|S076\|S089\|S090'` over SOURCES → 0; not mentioned in `round-52.md`. Carried silently (finding F2) |
| 4. Count mismatch (`:126`) | Erratum in the round-52 lesson: at `2b956d7` 13 marks on 12 lines (parenthesised grep), "the lesson's '14 marks on 13 lines' counted the legend line 200"; after D 14 on 13 | `corpus/lessons/round-52.md:20` | See next section — the erratum's arithmetic is right but its premise is wrong; the routed defect itself mis-framed a metric difference (finding F1) |
| 5. Carried items (`:127-128`) | Criterion 9 repaired: two-way dry-run check green on round 52's receipt and red on round 51's (kept red; filed bytes not rewritten). S072 and the separability spelling misses carried unchanged | `corpus/lessons/round-52.md:21`; receipt `reports/round-52/telemetry/declaration-dry-run.txt` (`$$ two-way check` → `MISSING_FROM_RECEIPT []`, `UNDECLARED_IN_RECEIPT []`, exit 0; control on round-51 receipt exit 1) | Re-ran `python3 -B reports/round-52/dry-run.py check reports/round-52/telemetry/declaration-dry-run.txt` → exit 0. S072 row unchanged (`corpus/SOURCES.md:101`, status `mined`, used-by the sign entry); separability tool unchanged `2b956d7..dea5ece` (empty `git log`) |
| Operator question (`:129`) | Answered lane-side by the criterion-10 landing: the route is forbidden, bypass-marked rows count as unopened and are rejected through a superseding row | `corpus/QUALITY.md:37`; `corpus/lessons/round-52.md:16` | Checker demonstrates both directions live (fail at `2b956d7`, pass at worktree) |

## Defect 4, verified by hand (assigned self-check)

Measurements on the entry `corpus/knowledge/linguistics/sign-languages-manual-modality.md`:

| commit | `grep -o '(to-verify)' \| wc -l` | `grep -c '(to-verify)'` | legend line 200 | `tools/gates/provenance-audit.py` (MARK_RE = `to-verify`, any case, `tools/gates/provenance-audit.py:79`) |
|---|---|---|---|---|
| `2b956d7` | 13 | 12 | bare "T to-verify" | **14 mark(s) on 13 line(s)** |
| worktree (post-D `dea5ece`) | 14 | 13 | same | **15 mark(s) on 14 line(s)** |

The round-51 lesson carries both sentences:

- `corpus/lessons/round-51.md:109` — "The C entry carries 11 `(to-verify)` marks on 9 lines (`python3 -B tools/gates/provenance-audit.py …`)". Correct at the lesson's draft commit `9feb69e`, stale after falsify fix `364eeff` — the round-51 falsify seat caught exactly this as F8 (`.ufo/waves/round-51/falsify/ReviewLessonGate.md:87-91`, verdict HOLDS-WITH-FIXES, fix not landed). This is the true defect-4 residue.
- `corpus/lessons/round-51.md:129` — "the entry now carries 14 `(to-verify)` marks on 13 lines". Present verbatim at `10f433cd` and at `2b956d7` (byte-checked via `git show 10f433cd:… | sed -n 129p`). Under the tool the lesson itself names at `:109`, 14 on 13 is exactly right at `2b956d7`.

So the spotcheck's defect 4 (`round-51-verifier-spotcheck.md:126`) quoted the lesson accurately but measured with the narrower parenthesised grep and called the lesson's 14/13 wrong. Under the lesson's declared metric it was not wrong; the real error is `:109`'s stale 11/9. Round 52's erratum (`round-52.md:20`) adopts the narrower metric, "corrects" a figure that was already right under the lesson's named tool, and leaves the metric unpinned — and the drafted R52-M2 (`.ufo/waves/round-52/build/ScribeMistake.md` §3–4) builds its case on the false premise that "the quotation is not in the lesson" (its own `git grep` hit at `round-51.md:129` is dismissed as unrelated). The durable repair is to pin the metric and date the `:109` figure, not to re-correct `:129`.

## Operator lessons

None exist: `git ls-files 'corpus/lessons/operator*'` → empty; the lessons directory listing has no `operator-*` file; `corpus/lessons/round-52.md:23` states the same. Nothing to reflect.

## Findings by severity

- **F1 (medium) — defect-4 erratum and drafted R52-M2 mis-state the record.** `corpus/lessons/round-52.md:20` and ScribeMistake §3–4 treat `round-51.md:129`'s 14/13 as the error; byte-level evidence shows that sentence exists, matches the tool metric named at `:109`, and the stale figure is `:109`'s 11/9 (F8, never landed as a fix). Advice (author-lane): reword the erratum to (a) name the metric each figure uses, (b) date `:109`'s 11/9 as stale since `364eeff`, (c) drop the "misquote" premise from R52-M2 before it is pasted into the `## Mistakes` table.
- **F2 (low) — defect 3's second clause unaddressed.** The S071, S076, S089, S090 locator list (`round-51-verifier-spotcheck.md:125`) has no superseding rows and no disposition note in `round-52.md`. Suggestion: one carried-items line in the lesson, as done for S072.
- **F3 (low) — S072 carried without disclosure.** `corpus/SOURCES.md:101` keeps status `mined` with the sign entry in `used-by`; the round-51 falsify seat recorded the De Gruyter challenge (HTTP 202) and proposed marking it seat-opened and not re-verified (`.ufo/waves/round-51/falsify/ReviewLessonGate.md:86`). Criterion 10 does not reach it (no bypass marker), so the row is not auto-rejected — but the round-51 lesson does not disclose it as unverified and round 52 changed nothing.
- **F4 (info) — dangling pointer.** `corpus/lessons/round-52.md:16` says "Mistake R52-M1 below", but the landed lesson has no `## Mistakes` section yet; rows R52-M1/R52-M2 exist only as drafts in ScribeMistake §2/§4. Integration-pending, not a defect of D.

## Residual risk and unrun checks

- S097/S133's page was not re-opened by this seat; the seven-shape and 45/7 details rest on the S133 row (`corpus/SOURCES.md:162`) and the round-52 lesson's gate quote (`round-52.md:30-33` region). S096 was re-opened by this seat (plain `curl`, 2026-10-22): pair words present as listed above; the location/movement grouping of APPLE/ONION and NAME/SHORT rests on the lesson's item-3 quote and the row anchor, not on my read of the list headings.
- The receipt's four pre-landing expectations (D counting 5, D acceptance exit 1, C counting 227, C acceptance exit 1, separability exit 2, agreement AGREE) were read from `declaration-dry-run.txt`, not re-executed against `147cfde`; the two-way check itself was re-run (exit 0).
- Claim C's entry, sources and README indexing are out of scope here (other seats hold them); worktree knowledge-file count was 227 at read time, i.e. C not yet landed.
- Separability checker spelling misses were not re-tested; the tool is byte-unchanged `2b956d7..dea5ece` and the lesson carries them (`round-52.md:21`).
