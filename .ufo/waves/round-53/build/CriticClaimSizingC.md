# CriticClaimSizingC — round 53, claim sizing of C and D

Seat: `KotodamaR53.CriticClaimSizingC` (critic, leaf). Read at lane worktree, HEAD `60f1d2a3d832b926e37f82b11c67496d131a1431` (declaration). Inputs read in full: `reports/round-53/claims.json`, `reports/round-53/accept-c.py`, `reports/round-53/d-count.py`, `reports/round-28/readme/sweep.py`, `reports/round-53/separability-manifest.json`, `tools/check-claim-separability.py` (docstring and pair logic, lines 1-60 and 600-700), `corpus/lessons/round-52-verifier-spotcheck.md`, and the L1's uncommitted `reports/round-53/final-measures.py` (read only).

Method: one `git archive HEAD` export under `/tmp` (outside the lane), copied once per mutant. Each mutant was built by a throwaway script, and both were deleted after the run. Nothing in the lane was written except this report. Tool installs: none.

## 0. Result

| question | answer | evidence |
|---|---|---|
| Is the R52-M3 class (a missing README row passes) closed? | **Yes, for that hole.** | mutant C-no-readme-row: `SWEEP FAIL exit=1 rows 228 files 229 missing_from_index 1 ['linguistics/gesture-co-speech-pointing.md']`, accept-c exit 1 |
| Can C's acceptance pass on a hollow entry? | **Yes, with two lines and one S-id.** A one-line entry fails, because the sweep needs a `- topic:` line followed by another `- field`. | mutant C-hollow: all four legs PASS, exit 0 |
| Is any clause of C's statement wider than accept-c.py? | **Yes: two clauses.** "one new entry" and "on co-speech gesture, pointing and quotable gestures as conlang and worldbuilding method" are not checked. | mutants C-swap-delete-other and C-hollow, both exit 0 |
| Does SIDS catch a queued or rejected row? | **Yes.** | `SIDS FAIL ... ['S187:status-queued']` and `['S187:status-rejected']`, exit 1 |
| Does SIDS have holes? | **Yes, four.** A used-by substring match; a duplicate id where the last row wins; leftover draft ids pass; zero-padded ids escape the pattern. | section 2 |
| Can D reach OPEN 0 by deleting lines? | **Yes.** Deleting nine routed lines gives OPEN 0 and SID_BAD 0, and seven S-ids leave the entry. Cutting the entry down to 2 lines also gives OPEN 0. | mutants D-repair-by-deletion and D-gut-entry |
| Can D reach OPEN 0 with no repair at all? | **Yes.** Rewording each phrase trivially and writing `,-6` for `, -6` passes. | mutant D-synonym-evasion |
| What does D's declaration say that the counter does not check? | The mapping method and the drop rule. **At base the drop rule applies to no fragment**: none of the 10 mapped S-ids is already on its line, so every dropped fragment loses support. | section 4 |

Verdict class: every hole below is a **fixable sizing defect** that wave 2 and the closure can re-derive with one plain command each. None is a tradeoff the judge must reject. Round 52 had the same unchecked "one new entry ... on X" clause, and its closure re-derived it by hand with `git diff --name-status` (`corpus/lessons/round-52-verifier-spotcheck.md:44`). The declaration is frozen, so the correction belongs in the wave-2 falsifiers and in the lesson, not in the argv.

## 1. Claim C — the SWEEP leg (R52-M3 check)

- At base, accept-c gives `SWEEP FAIL exit=0 rows 228 files 228 missing_from_index 0 []`. The leg fails on the row count even though the sweep exits 0, so it does not just echo the exit code.
- The patterns are line-anchored: `^rows (\d+) files (\d+)$` and `^missing_from_index (\d+) (.*)$` (`reports/round-53/accept-c.py:45-46`). Neither can match the `footer_live` JSON line. That line was the round-52 false match (`corpus/lessons/round-52-verifier-spotcheck.md:53`).
- `sweep.returncode` is read directly, with no pipe (`accept-c.py:39-49`). The sweep returns 1 whenever `inv["ok"]` is false (`reports/round-28/readme/sweep.py`, `main`, `return 0 if inv["ok"] else 1`). That covers missing rows, ghost rows, topic mismatch, header drift, the totals line and the footer.
- Mutant C-no-readme-row (a hollow entry with every other README count bumped, but no index row): `SWEEP FAIL exit=1 rows 228 files 229 missing_from_index 1`, accept-c exit 1. **The R52-M3 hole is closed.**
- Residual limit: the sweep reads only top-level `.md` files in each part directory (`sweep.py` `disk_files`, `os.listdir`), while COUNT uses `os.walk` (`accept-c.py:32-33`). A nested file would raise COUNT and stay invisible to the sweep. That would show up as a rows/files split, not a pass, so it is low risk.

## 2. Claim C — the hollow entry and the SIDS leg

Every mutant below has the same frame: the entry file, one README row `- \`gesture-co-speech-pointing.md\` — x` (byte-equal to the entry's topic `x`), the linguistics header 27→28, the totals line and footer 228→229 with footer vector `28/26/28/29/24/94`, and one SOURCES row `| S187 | x | docs | A | x | x | x | <status> | 2026-10-22 | x | <used-by> |` after S186.

| mutant | change from the frame | accept-c |
|---|---|---|
| C-hollow | entry = `- topic: x` / `- sources: S187` (2 lines), status `mined`, used-by = entry path | **exit 0, all PASS** |
| C-500-lines | entry is 502 lines of filler | **exit 0** (the 230-line bound is not checked) |
| C-swap-delete-other | also deletes `linguistics/numerals-and-measures.md` and its README row, and adds `linguistics/zz-extra.md` with its row | **exit 0**, so "one new entry" is not checked |
| C-draftid-left | body adds `(S187, -4)` and `(NEW-ScribeSec04Pointing-2)` | **exit 0**: this round's mined mistake passes C's acceptance |
| C-usedby-bak | used-by = `corpus/knowledge/linguistics/gesture-co-speech-pointing.md.bak` | **exit 0** (`accept-c.py:75`, substring test) |
| C-usedby-negated | used-by = `not corpus/knowledge/...pointing.md` | **exit 0** |
| C-dup-row-queued-first | two S187 rows, `queued` then `mined` | **exit 0** (`accept-c.py:61`: the dictionary keeps the last row) |
| C-sid-padded | body adds `(S0135)` and `(S 135)` | **exit 0** (`\bS\d{3}\b` at `accept-c.py:65` does not see either) |
| C-cites-D-line | body adds `` `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md:106` `` | **exit 0**. C's must_not_cite clause ("lines changed by D") has no check: the separability static leg ignores a land path that already exists at base (`tools/check-claim-separability.py:25-27`) |
| C-queued / C-rejected | status `queued` / `rejected` | exit 1, `S187:status-queued` / `S187:status-rejected` (caught) |

On "one line, one S-id": a single line `- topic: x S187` fails. The sweep's `TOPIC_RE` needs a following `\n- \w` field (`sweep.py:61`), otherwise the row is `NO_TOPIC_FIELD` and the sweep exits 1. **The minimum hollow entry is two lines.**

"mined" is read from the status cell only. Nothing checks that `corpus/lessons/round-53.md` `## Gate` holds the row's URL and its quote of at most 25 words. The statement asks only for a "mined corpus/SOURCES.md row", so this is not wider than the statement. It is a frontier check (F-C6 below).

The L1's red controls in `reports/round-53/final-measures.py:115-138` (README row removed, used-by emptied, entry deleted) are all absence controls. None builds a hollow or swapped tree. `final-measures.py:80` runs `tools/check-draft-ids.py`, but that file is a record land (`claims.json`, `records_not_claims`), it is not in the working tree yet, and it is not part of C's acceptance.

## 3. Claim D — deletion, evasion and relabelling

| mutant | change from base | d-count | other |
|---|---|---|---|
| D-repair-by-deletion | delete lines 54, 76, 79, 121, 174, 176, 177, 179, 181; strip every `, -N`; line 106 `(S159; S162)`; line 113 `(S159)` | **OPEN 0, SID_BAD 0, exit 0**; cited 50 → 43 | lost S151 S163 S165 S166 S179 S181 S182; README sweep still exit 0; entry 195 → 186 lines |
| D-gut-entry | keep only the `working their farms` and `mobile phone` lines, then repair as above | **OPEN 0, SID_BAD 0, exit 0**; cited 2 | the sweep exits 1 (topic line gone), but d-count never runs the sweep |
| D-synonym-evasion | `force set formulas`; `(Laos, Thailand and the United States) (S135)`; `/b/ falling together with /k/`; `learnt in childhood`; `in Akan practice (Ghana)`; `primitive  peoples` (two spaces); every `, -N` → `,-N`; line 106 adds S162; line 113 S163 → S159 | **OPEN 0, SID_BAD 0, exit 0** | no over-read repaired; all 10 fragments still present as `,-N` |
| D-new-draftid | every `, -N` → `, NEW-ScribeSec14Calibration-N` | OPEN 8 (FRAG 0; only the 2 WROW and 6 OVER instances remain) | the fragments are relabelled, not resolved |
| D-hyphen-phone | line 113 → `mobile-phone networks arrived (S159)` | OPEN 17, WROW2 `absent` | the absence guard works (`d-count.py:67,70`) |

What holds: WROW1 and WROW2 count an absent phrase as open (`reports/round-53/d-count.py:66-71`). Deleting or rewording lines 106 and 113 alone cannot close them.

What does not hold:
- Every OVER leg is a literal regex (`d-count.py:31-38`), and FRAG is literally `, -[0-9]+\b` (`d-count.py:39`).
- Deleting the line or making a trivial edit closes OVER and FRAG.
- SID_BAD reads only the used-by cell, not status (`d-count.py:73`). At base all 50 cited rows are `mined`, and a non-mined row naming the entry could only come from editing `corpus/SOURCES.md`. That file is a C land, so a separability overlap or dependency would show it. Low risk.

D's statement is sized to the counter: "d-count.py prints OPEN 0 and SID_BAD 0 ... its 18 instances are ...". So the statement is not wider than the counter. The width sits in `method_not_statement` and in the `falsifier` ("a fragment was dropped where its source detail lost all support"). The counter cannot see either.

D's must_not_cite list is covered by separability, not by d-count:
- A cited S187 or above matches C's export `\bS(18[7-9]|19[0-9]|2[0-9][0-9])\b` (`reports/round-53/separability-manifest.json`; the regex stops at S299).
- The gesture entry and `corpus/lessons/round-53.md` are land paths absent at base, so naming either one is a finding (`tools/check-claim-separability.py:617-634`: the dependee loop runs over every unit, records included).

## 4. Claim D — the fragment mapping (the drop rule has no case at base)

Each `, -N` is the second id in a seat's `(NEW-<Seat>-a, -N)` pair. The first id was mapped at integration, and the continuation kept only `-N`. Each draft id was resolved through its row URL in the seat report against `corpus/SOURCES.md`:

| entry line | fragment | seat source of the pair | draft id → URL | S-id | already on the line at base? |
|---|---|---|---|---|---|
| 106 | -6 | `.ufo/waves/round-52/build/ScribeSec08Ecology.md:34` `(NEW-ScribeSec08Ecology-4, -6)` | Ecology-6 (`:89`) → Cloarec-Heiss PDF | S162 | no (line cites S159) |
| 107 | -6 | `ScribeSec08Ecology.md:35` `(NEW-ScribeSec08Ecology-5, -6)` | Ecology-6 → Cloarec-Heiss PDF | S162 | no (line cites S160) |
| 113 | -4 | `ScribeSec08Ecology.md:41` `(NEW-ScribeSec08Ecology-3, -4)` | Ecology-4 (`:87`) → `ich.unesco.org/doc/src/36234-EN.doc` | S159 | no (line cites S163) |
| 174 | -5 | `ScribeSec14Calibration.md:20` `(…-4, -5)` | Calibration-5 (`:40`) → `par.nsf.gov/servlets/purl/10166941` | S174 | no (S179) |
| 177 | -5, -6, -7 | `ScribeSec14Calibration.md:23` `(…-4, -5, -6, -7)` | -5 → S174; -6 (`:41`) → `pen.org/drums-that-talk/`; -7 (`:42`) → TIME drum-telegraphy Wayback | S174, S176, S175 | no (S179) |
| 179 | -12 | `ScribeSec14Calibration.md:25` `(…-3, -12)` | Calibration-12 (`:47`) → `news.cnrs.fr/opinions/the-fascinating-art-of-whistled-speech` | S180 | no (S157, S183, S179) |
| 181 | -2 | `ScribeSec14Calibration.md:27` `(…-1, -2)` | Calibration-2 (`:37`) → UNESCO element 00172 | S157 (S186 shares the URL, but it is `queued` with used-by `—`, so citing it trips SID_BAD) | no (S173, S175) |
| 181 | -12 | `ScribeSec14Calibration.md:27` `(…-1, -12)` | Calibration-12 → CNRS | S180 | no |

The mapping matches the closure's own list (S162, S159, S174, S175, S176, S157, S180; `corpus/lessons/round-52-verifier-spotcheck.md:71`).

Every mapped row is already `mined` with D's entry in its used-by cell:
- S162 is cited at line 111, S159 at 105 and 109, S174 at 170, S175 at 172 and 181, S176 at 172, S180 at 175, and S157 at 170, 171, 173 and 179.
- So **D needs no SOURCES edit**, and C and D stay separable.

S163 is cited only on line 113. After the repair, the entry's cited set must be exactly the base set minus S163 (49 ids). S163's used-by cell will then name an entry that no longer cites it. d-count checks only the direction from citation to row, so it cannot see this, and C owns `corpus/SOURCES.md`. Record it as a stale back-reference in the lesson or route it. It is not a D falsifier.

## 5. Wave-2 falsifiers (run on the landed tree; `B=a9cf95f`, `H=<landing commit>`)

Each falsifier fires when its observation differs from the expectation shown.

**Claim C**

- **F-C1 contract and hollow.** Run the round-50 checker Part A (`.ufo/waves/round-50/build/ReviewEntryContract.md:125-190`) on the entry and its README row, with the length cap changed from 250 to **230**. Expect `PASS`. Also expect:
  - exactly 14 `^## [0-9]+\. ` headings;
  - H2 13 contains `Recheck` and H2 14 contains `Scope`;
  - `grep -c '^### '` = 0;
  - `grep -cE 'DR-GES-0[1-9]'` ≥ 1;
  - `grep -c 'lore-shokunin'` ≥ 1;
  - the `- topic:` line matches `gestur` and `pointing` and (`quotab` or `emblem`).
- **F-C2 one new entry.** `git diff --name-status B H -- corpus/knowledge` must be exactly `A corpus/knowledge/linguistics/gesture-co-speech-pointing.md` and `M corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`. Any `D`, `R` or extra `A` fires.
- **F-C3 draft ids (both entries).** `grep -nE 'NEW-[A-Za-z0-9]+-[0-9]+|[,;(] ?-[0-9]+\b|\bS0[0-9]{3}\b|\bS [0-9]{3}\b' <entry>` must print 0 lines. Review any hit by hand: a numeric range like `(-5 °C` would be a false positive.
- **F-C4 exact used-by and unique ids.**
  - For each cited S-id, split the used-by cell on `,`, `;` or whitespace; one token must equal the entry path exactly.
  - `awk -F'|' '/^\| S[0-9]{3} /{print $2}' corpus/SOURCES.md | sort | uniq -d` must print nothing.
- **F-C5 no citation of D-changed lines.** `grep -nE 'speech-surrogates-whistled-drummed\.md' <C entry>` must have no hit pointing at lines 54, 76, 79, 106, 107, 113, 121, 174, 176, 177, 179 or 181, or at their rewritten text.
- **F-C6 frontier (not a claim).** Each cited S-id needs a `## Gate` line in `corpus/lessons/round-53.md` with:
  - the URL;
  - `accessed 2026-10-22`;
  - a location;
  - a quote of at most 25 words, character for character;
  - for a challenge, the wording "challenge met, not passed".

**Claim D**

- **F-D1 lines conserved.** `wc -l` of D's entry must be 195 at H. The hunks of `git diff -U0 B H -- <D entry>` must all be `-n,1 +n,1` with n in {54, 76, 79, 106, 107, 113, 121, 174, 176, 177, 179, 181}. Any other hunk, or any deletion, fires (the mutants D-repair-by-deletion and D-gut-entry).
- **F-D2 S-id set conserved.** (cited S-ids at H) must equal (cited S-ids at B) − {S163}, giving 49. A missing id or an added id fires.
- **F-D3 per-line mapping.** Each line must carry its mapped S-ids from the section 4 table:
  - 106 ⊇ {S159, S162}
  - 107 ⊇ {S160, S162}
  - 113 ⊇ {S159}, and S163 not on the line
  - 174 ⊇ {S179, S174}
  - 177 ⊇ {S179, S174, S175, S176}
  - 179 ⊇ {S183, S180}
  - 181 ⊇ {S173, S157, S175, S180}
  A missing id means a dropped fragment lost its support, which is the declared falsifier.
- **F-D4 over-reads gone, not just reworded.** The first five greps must find 0 lines unless the line carries `(to-verify)` or an added S-id whose re-opened page carries the detail:
  - `sed -n 54p | grep -E 'Hmong[^|]*(Laos|Thailand|United States)[^|]*\(S135\)'`
  - `sed -n 54p | grep -E 'Suruí[^|]*(force|fix|set|rigid)'`
  - `sed -n 76p | grep -E '/b/[^|]*(merg|fall|collaps|fus|confus|neutrali)\w*[^|]*/k/'`
  - `sed -n 79p | grep -iE 'learn\w*[^|]*(young|child)'`
  - `grep -cE 'primitive\s+peoples' <D entry>`
  - Line 121 must no longer generalise one drummer's biography (S165) into "Akan practice". This is a reviewer read of the re-opened S165 page.
- **F-D5 entry still whole.** `python3 -B reports/round-28/readme/sweep.py` must exit 0 at H (D-gut-entry turns it red), and the draft-id grep F-C3 must print 0 lines for D's entry (D-new-draftid).

## 6. Lesson wording (for the L1 to paste into `corpus/lessons/round-53.md`; the declaration stays frozen)

> **R53-Mx — acceptances count presence and absence, not content (claim sizing).** Round 53 closed the R52-M3 hole: C's acceptance reads the README sweep's own exit code and line-anchored `rows`/`missing_from_index` values, and a scratch tree without the index row fails `SWEEP` (exit 1). But both acceptances still pass on trees that break their statements:
>
> - A two-line entry (`- topic: x`, `- sources: S187`) with one mined row passes all four C legs.
> - Deleting one other knowledge file and adding two keeps the count at 229, which contradicts "one new entry".
> - Deleting nine routed lines of the speech-surrogates entry, or rewording each routed phrase by one word, prints `OPEN 0 SID_BAD 0`. In the deletion case seven cited S-ids are lost.
> - Writing `,-6` for `, -6`, or relabelling a fragment as `NEW-<Seat>-<n>`, clears `FRAG`. The draft-id class this round mined is still invisible to both acceptances.
>
> Rule for the next declaration:
>
> - A count-down acceptance (`OPEN n → 0`) must carry a conservation leg: the line count and the cited S-id set are unchanged except for the declared edits.
> - A coverage acceptance must carry a content leg: the entry-contract checker with the length cap, the topic words of the statement, a `git diff --name-status` showing exactly one added file, and a draft-id leg (`NEW-\w+-\d+`, `[,;(] ?-\d+`).
> - Until then, the falsify wave runs these legs by hand and records them in the final measures.

## 7. Unrun checks and limits

- `scripts/sources-census.sh validate` (fleet root) was not run against the duplicate-row mutant. It reads the fleet copy of the lane, not a scratch tree, so whether the census catches a duplicate S187 is not observed `[INFERENCE: its W04 duplicate-URL rule may catch it]`.
- The separability checker was not run on any mutant. Its coverage of D's must_not_cite list is read from the code (`tools/check-claim-separability.py:617-634`), not exercised.
- `tools/check-draft-ids.py` does not exist in the working tree yet, so whether it would catch C-draftid-left or D-new-draftid is untested.
- No external source was opened. The section 4 mapping uses committed seat reports and SOURCES URLs only.
