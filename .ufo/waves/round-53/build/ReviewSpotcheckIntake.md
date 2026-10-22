# ReviewSpotcheckIntake — round-52 spotcheck routed defects and carried items (round 53)

Written 2026-10-22T14:20Z. Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, HEAD `60f1d2a` (declaration) on `a9cf95f` (instruments) on `9ae5af9` (prerequisite). **Live-lane note:** at read time the L1 was mid-integration — the entry carries an uncommitted 10+/10− diff and `reports/round-53/clauses.py` and `reports/round-53/final-measures.py` are untracked; statuses below are stamped to that moment. All checks are direct file reads, read-only git, and the round's own declared counters; no LSP server exists for these Markdown records in this seat's toolset, so no semantic-index proof is claimed. Prerequisite commit `9ae5af9` verified by reading `git show` in full: SHONEN.md 1 line, SOURCES.md +3 rows (S184–S186), entry line 104 re-cite, census receipt.

## 1. Routed defects — round-52-verifier-spotcheck.md:130-151

| item (spotcheck:line) | what round 53 does | status at 2026-10-22T14:20Z | evidence |
|---|---|---|---|
| 1a register UNESCO 00172 nomination / re-cite line 104 (:133) | **Done in the prerequisite**, not a claim: S184 registered (`mined`, used-by the entry) and entry line 104 re-cited from `(S157, -2)` to S184 with the nomination's own wording | landed | `9ae5af9` diff; corpus/SOURCES.md:213; round-53.md Gate S184 (Wayback 20190622061452id_, `soffice` conversion, "over a distance of up to five kilometres", converted-text line 17) |
| 1b replace the 11 `, -N` fragments (:134) | **Claim D, FRAG leg.** Calibration: the closure counted 11 at round-52 close; the prerequisite's line-104 re-cite removed the 11th (`(S157, -2)`), so 10 remain at base — the receipt itemizes all 10 (lines 106, 107, 113, 174, 177×3, 179, 181×2). "Teach the provenance gate" is routed to a new `tools/check-draft-ids.py`, declared a record (REC land), not a claim | in flight: 0 FRAG left in the uncommitted working copy; the tool file is **not on disk yet** | declaration receipt (d-count OPEN 18 block); my base recount `git show a9cf95f:<entry> \| grep -oE ', -[0-9]+' \| wc -l` → 10; d-count.py FRAG regex; manifest REC lands list |
| 1c line 106 → S162, line 113 → S159 (:135) | **Claim D, WROW legs** (counter requires "working their farms" cited S162; mobile-phone decline cited S159 and not S163) | in flight: both closed in the uncommitted diff (counter's OPEN list no longer shows WROW1/WROW2) | declaration receipt items WROW1/WROW2; working-copy `git diff` (artifact 45143); live run |
| 1d over-reads 54×2, 76, 79, 121, "primitive peoples" 176 (:136) | **Claim D, OVER1–6 legs** — soften to what the cited row's page carries or mark `(to-verify)` | **open — the only remaining D leg**: live counter reads OPEN 6, exactly OVER1–6 | d-count.py run 14:1xZ (OVER1..OVER6 at :54,:54,:76,:79,:121,:176), exit 1 |
| 2 claim sizing (:137) | **Done by C's instrument**: accept-c.py runs the README sweep standalone (subprocess, no pipe) and requires its exit 0 plus `rows 229 files 229` and `missing_from_index 0`; a missing README row fails SWEEP | instrument landed at `a9cf95f`; intended pre-landing fail receipted (all four legs FAIL, exit 1) | accept-c.py SWEEP leg + docstring; declaration-dry-run.txt C acceptance block |
| 3a SHONEN line 8 "53 mined, 8 queued" (:139) | **Done in the prerequisite**: line 8 now reads 52 mined, 9 queued at `2b956d7` (S081, S123–S125, S127–S131) with the note "Corrected in round 53 from '53 mined, 8 queued' (round-52 closure, routed defect 3)" | landed | SHONEN.md:8; `9ae5af9` diff |
| 3b round-51 SCORECARD frontier line "S071–S122 mined" (:140) | **Not yet**: needs an appended correction (SCORECARD.md is a REC land this round; round-53.md's Frontier section is still a placeholder) | open | SCORECARD.md:1017 unchanged; grep "round-53" in SCORECARD.md → 0 hits; round-53.md Frontier placeholder |
| 4a S178 Gate line says "queued" (:142) | Erratum route: round-53.md "Errata to the round-52 lesson's Gate (filed bytes not rewritten)" | line still present; errata section a placeholder at read time | round-52.md:114 ("encyclopedia lead (tier C), queued") vs SOURCES S178 `rejected` |
| 4b S145 Gate quote substitutes words, wrong page (:143) | Data side **fixed by S185** (queued, supersedes anchor+quote: passage on printed p. 2132 left column, quote begins "It was"); the round-52.md Gate line itself is filed bytes → erratum route | S185 landed; Gate-line erratum placeholder | SOURCES.md:214; round-52.md:75; round-53.md Gate S185 |
| 4c S157 row lacks captcha note (:144) | **Done in the prerequisite** by supersession: S186's row records verbatim "the captcha was met and not passed, and the content was read from the Wayback capture, as QUALITY criterion 10 asks a row to say"; S157's own filed cells unchanged | landed | SOURCES.md:215 |
| 4d duplicate "Seat:" tags, S139/S172 lines (:145) | Erratum route (same block as 4a) | still present | round-52.md:62, :63 (S139) and :107, :108 (S172) — `grep -nE 'Seat: [A-Za-z0-9]+\. Seat:'` |
| 5 leftover ScribeSec05Drummed.md (:146) | **Nothing left to do** — the round-52 closure's own erratum resolved it (disk bytes matched the `2eb489fb` blob; `git status --porcelain` empty after `c3297ff`); stays a status-neutral note | closed at round-52 | spotcheck :155-157 |
| 6a undrafted drummed-speech / decline sections; phonetics §7 ownership wording (:148) | **Not this round**: no claim adds sections (D repairs routed wording only; C is a new gesture entry); the stale wording pair is outside both claims' lands, as round-52 already routed | open | round-52.md:143-144; entry §1–§12 headings (no such sections); sound-symbolism.md:19 ("its §7 owns whistled/drum channels"); phonetics-phonology.md:75-78 (couples line routes "whistle & drum channels" to costume/anatomy, no §7 owner named) |
| 6b checker limits; dry-run.py check gaps (:149) | **Mostly not this round.** The round-53 dry-run.py is a copy of round-52's with one change (expected pre-landing result now read from `expected_pre_landing_counting`) — but `check` still compares only `$ command` lines, so both ReviewDryRunReceipt gaps persist: expected-result lines are printed, not enforced, and a manifest acceptance keyed by an id absent from claims.json is still silently ignored. Access-checker limits untouched (no REC or claim lands tools/check-source-access.py) | open | reports/round-53/dry-run.py docstring + check(); round-52.md:146-147 |
| 6c S072; separability spelling misses (:150) | **Not this round**: S072 still `mined`, tier B publisher-description, still not re-openable (De Gruyter DOI); no claim or REC land touches its row. The R50-M6 checker limit (whole-path matching) is unchanged; this round's manifest avoids the trap by using full correct paths, so the round's verdict does not hinge on spelling — the tool, not the manifest, stays defective | open | SOURCES.md:101; round-51-verifier-spotcheck.md:127; round-50.md:102 (R50-M6); reports/round-53/separability-manifest.json (all `corpus/…` paths) |
| 6d index this file in corpus/lessons/README.md (:152) | Routed to this round's records: corpus/lessons/README.md is a REC land | open at read time — no `round-52-verifier-spotcheck` row in the index yet | grep in corpus/lessons/README.md → 0 hits |

## 2. Discernment table (spotcheck:98-108) — intake view

| item | gate decision | intake view | round-53 action | evidence |
|---|---|---|---|---|
| S139 Seifert et al., Bora manguaré | admit, tier A, mined | agree — primary open-access paper; the four Gate quotes carry the cited facts | no action on the admission; only 4d's duplicate Seat tags on its log lines | round-52.md:58-63, :107-108 |
| S145 Rialland 2003 | admit, tier A, mined | agree, with the two stated defects (quote substitution, page 2131 vs 2132) | S185 supersedes anchor+quote (prerequisite); Gate-line erratum pending | SOURCES.md:214; round-52.md:75 |
| S157 UNESCO element 00172 | admit, tier B, mined | agree; Wayback route ordinary under criterion 10; row's cells lacked the captcha note | S186 supersedes with the note (prerequisite); the five-kilometre figure moved off this row to S184 | SOURCES.md:215, :213 |
| S178 Wikipedia Guanche | reject, tier C | agree — tertiary lead, uncited by the entry | no row action; the "queued" Gate line is an erratum item (4a) | SOURCES S178 `rejected`; round-52.md:114 |
| S132 Battison 1974 | reject | agree — HTTP 403 `cf-mitigated: challenge`, unreachable by ordinary means | none; upheld | round-52.md:29; spotcheck :106 |

## 3. corpus/lessons/operator-*.md teaching

None exists, so nothing is unreflected. Evidence: round-52.md:23 states it; `git ls-files | grep -i operator` in the lane returns only `reports/round-32/dossier-d13-operator-decisions.md` (a round-32 dossier, not a lesson); globs over `corpus/lessons/*perator*`, lane root and fleet root found no operator lesson file. One recursive fleet-wide glob timed out incomplete, but the tracked-file listing plus the non-recursive sweeps of the only plausible directory cover the named pattern.

## 4. Carried items — still open?

- **Undrafted drummed-speech and decline sections** — open. Entry has §1–§12 with no such sections; round-52.md:143 records they folded into §3/§5/DR-SRG-05 as "candidates for a later round"; no round-53 claim adds them.
- **Phonetics §7 ownership wording** — open. sound-symbolism.md:19 and phonetics-phonology.md:75-78 unchanged; outside both claims' lands (round-52.md:144 routed it to a later round).
- **Checker limits** — open. round-52.md:146 (bypass-only visibility, S-id-only citation matching, no superseding-row test); no round-53 land touches tools/check-source-access.py.
- **dry-run.py check gaps** — open, one cosmetic improvement (see 6b above).
- **S072** — open. SOURCES.md:101 unchanged; not re-openable (round-51-verifier-spotcheck.md:127); no round-53 instrument claims it.
- **Separability spelling misses** — open as a tool limit (R50-M6); this round's manifest is spelled out in full so its own verdict is not spelling-dependent.
- **Indexing the spotcheck in lessons README** — open at read time; README is a REC land this round.

## 5. Calibration notes

- The declared before-value decomposes exactly: 10 FRAG + 2 WROW + 6 OVER = OPEN 18 at base, verified three ways (declaration receipt, my independent `git show a9cf95f` recounts, live counter ancestry). The 11-vs-10 fragment arithmetic is the prerequisite's doing, not a counter undercount.
- Live observation 14:1xZ: working copy (uncommitted) OPEN 6 / SID_BAD 0 / cited 50, exit 1 — D's acceptance (OPEN 0, exit 0) is **not yet met**; the remaining work is exactly the six over-reads.
- d-count's SID_BAD leg enforces "every cited S-id is a registered row naming the entry in used-by", which blocks stray ids in practice but would **not** by itself reject a hypothetical S187+ row that named the entry; D's must-not-cite list (no S187+, no gesture entry, no round-53.md) therefore rests on review and the falsify wave, not on the counter. C's SIDS leg does enforce ≥S187.
- Untracked `reports/round-53/final-measures.py` and `clauses.py` appeared during this audit — integration artifacts, not yet measured by me.

## 6. Residual risk and verification gaps

- D's final landed state was not measured by me (integration in flight); `final-measures.py` run and the red-after scratch copies remain the L1's closure steps.
- C has not started: `find corpus/knowledge -iname '*gestur*' -o -iname '*pointing*' -o -iname '*kinesic*'` → 0 files at read time; accept-c.py not run by me (its pre-landing fail is receipted).
- Separability and claims-agree were taken from the receipt, not re-run (the checker needs a git checkout, a lane gate).
- The round-53.md record still holds INTAKE_TABLE / GATE_C / CHANGELOG_C / ERRATA / SEARCH_C / MISTAKES / FRONTIER placeholders at read time; the tables above are written to paste into INTAKE_TABLE and the errata items (4a, 4b Gate line, 4d) are the text the ERRATA block still owes.
