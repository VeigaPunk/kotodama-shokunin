# Kotodama round 52 — non-author verification

author: hyaku closure (non-author integrator, @m_opus)

Runtime model as exposed to this session: `anthropic/claude-opus-5-5`, reached through the configured `task` route with no model parameter. This closure did not author round 52. It judged only committed bytes: base `2b956d7c31e063da2fe18286077192ad04ace4d4`, head `2eb489fb954bfa448918223cf1c9bad622c694a5`, plus the prerequisite `147cfde` and the declaration `d9f73c8`, each exported read-only with `git archive` into `/fast/scratch/hyaku/kotodama-r52-closure/{base,pre,decl,head}`. Four read-only reviewer seats re-opened sources by ordinary means (plain `curl`, Wayback captures); no lane gate was executed. The held `kotodama51-prereg-critic` item was not opened, retried or reproduced. Tool installs: none.

## Decision

**Admitted.** Claim D (depth) and claim C (coverage) both re-derive to their declared after-values, and no axis is harmed. C's integrated text was never attacked by a falsify wave, so this closure attacked it: 55 sentences checked against re-opened sources, 46 supported, 4 partly supported, 5 not supported as cited, none found false. The attack found citation defects (one quoted figure rests on a source with no registry row, 11 unresolved draft-id fragments, several over-reads). They are routed below and do not void the claim. The ruling on R52-M3 is below.

## Step-1 conformance

| check | command | observed |
|---|---|---|
| report committed by the lane identity | `git log --format='%an %H' -- .ufo/reports/round-52/kotodama.md` (fleet root) | `kotodama-shokunin 821fb6023c1ad1b385e289733cd54ae5c0169605`, on `origin/master` |
| SHONEN heading, one line per box | report `## SHONEN`; `grep -cE '^- \[[ x~]\]'` on the report and on `SHONEN.md` | 4 report lines, 4 boxes, all `[~]` |
| cited commits exist and are ancestors of `main` | `git merge-base --is-ancestor <hash> main` for `147cfde d9f73c8 dea5ece 5b7ecfb 7cee23b 2eb489f` | all six exist, all ancestors; `git log 2b956d7c..2eb489fb` shows exactly these six, all by `kotodama-shokunin` |
| lane pushed | `scripts/hyaku/jj-lane.sh state <lane>`; `git ls-remote origin refs/heads/main` | `ahead=0 behind=0`, local = remote = `2eb489fb…` |
| no leftovers | `git status --porcelain` | 1 line: ` M .ufo/waves/round-52/build/ScribeSec05Drummed.md` (defect 1 below) |
| prompt carries the template contract | every non-placeholder line of `templates/round-prompt.md` present in `.ufo/prompts/kotodama-round-52.md` | 105 of 105 lines present; addendum §6 with directive 3 verbatim (line 143) and §9 Claim sizing (line 342) |
| declaration frozen | `git diff --stat d9f73c8 2eb489fb -- reports/round-52/claims.json reports/round-52/separability-manifest.json` | empty |

Driver digest (copied from `.ufo/watchdog.log`): `2026-10-22T07:32:14-03:00 launch kotodama round=52 pgid=12209 driver=hyaku-inline attempt=1`; `2026-10-22T10:04:53-03:00 complete kotodama round=52; hyaku-inline attempt=1`.

Conformance defect (status-neutral): the tracked wave file `.ufo/waves/round-52/build/ScribeSec05Drummed.md` is modified in the lane working copy (mtime 2026-10-22 10:05:29 -03:00), after the last lane commit (10:02:51) and the report commit (10:04:02). The diff rewrites three items of that seat's report (+5/−4). A section scribe the report lists as cancelled wrote after the report said "No seat is running". It carries no claim land.

## Per-claim re-check (re-measured, not evidence-verified)

Every number below is from a command this closure ran on the exported trees. The separability checker needs a git checkout and is a lane gate, so its verdict was taken from the committed receipt only (`reports/round-52/telemetry/final-measures.txt`: `SEPARABILITY: 0 findings`, exit 0, `AGREE claims=['C', 'D']`, `MISSING_FROM_RECEIPT []`; tree `7cee23b` plus the then-uncommitted records, timestamp 13:01:30Z, before the commit that ships it at 13:02:51Z).

**Claim D — depth, repair-first.**

- `awk '/S094/{n++} END{print n+0}' corpus/knowledge/linguistics/sign-languages-manual-modality.md` → base 5, `147cfde` 5, `d9f73c8` 5, head 0. The declared manifest acceptance, run on head: `S094_lines=0`, exit 0 (no S-id from S134 up).
- `grep -rc S094` over `corpus/knowledge`, `SKILL.md` and `corpus/README.md` at head → 0 everywhere. S094 reads `rejected`, `used-by` `—`. S132 supersedes it (`rejected`) and S133 supersedes S097's locator (`queued`).
- Re-opened by plain `curl` (HTTP 200, no challenge): S096 (CSLDS Module 6) and S097 (CSLDS Module 7). Every detail now cited to them on lines 83, 87, 90, 92 and 93 is on the page:
  - "Battison (1978) proposed that palm orientation should be added as the fourth phonological parameter in ASL"
  - "NAME – ASL (Battison, 1978) … SHORT – ASL (Battison 1978)" and "the examples given by him were CHAIR and NAME"
  - CAR/WHICH tagged Battison 1978, ONION/APPLE untagged, so "all but APPLE/ONION credited to Battison 1978" is exact
  - "Out of the 45 possible handshapes in ASL, only 7 can appear as the passive hand of a Type-3 two-handed sign"
  - "A, S, B, 5, G (i.e., 1), C and O"
- Line 92 marks the 1974 set `(to-verify)`. OFFER/MAYBE and SHORT/TRAIN are gone. No falsifier condition trips.

**Claim C — coverage, the learning claim.**

- `find corpus/knowledge -name '*.md' | wc -l` → base 227, `d9f73c8` 227, head 228. `git diff --name-status 147cfde 7cee23b -- corpus/knowledge` → one `A` (the new entry) and one `M` (D's entry).
- The declared acceptance argv, run on head → `knowledge_files=228`, `C_SID_BAD 0 [] cited 49`, exit 0.
- The sweep run on its own, `python3 -B reports/round-28/readme/sweep.py`, gives `rows 228 files 228` and `missing_from_index 0 []`. It also prints `footer_ok True` and `totals_ok True`, and exits 0. README line 265 carries the index row.
- Registry: 49 distinct S-ids, all in S134–S183. S178 and every id below S134 are absent. All 49 rows are `mined` with the entry in `used-by`. S178 is `rejected`, `—`.
- Gap at the claim base `147cfde`: the filename sweep finds 0 files. The topic grep finds only `culture-material/music-instrument-lexicon.md`, a partial owner.
- Partial owners: the four (`phonetics-phonology.md:197-199`, `music-instrument-lexicon.md:98-100`, `orality-formulaic-language.md:114,124`, `sound-symbolism.md:121`) are each named once in §2 and then deferred to. No register is restated (reviewer seat AttackCEntryA).
- Access: QUALITY criterion 10 allows a Wayback copy after a challenge. Every gated case this closure met was routed to Wayback, not passed: S157/S163 captcha, S173 Anubis, S166/S176 HTTP 403. This closure re-checked the new rows' cells for bypass wording; only the two rows that record a challenge met and left unsolved (S152, S173) match.

**Ruling on R52-M3 (C's statement is wider than its acceptance argv).** The defect is real. On a scratch copy of head with the entry's README index row removed, the declared C acceptance still prints `knowledge_files=228`, `C_SID_BAD 0` and exits 0. The sweep alone gives `rows 227 files 228`, `missing_from_index 1 ['linguistics/speech-surrogates-whistled-drummed.md']` and exits 1. The cause: `grep -q '"total": 228'` also matches the live `footer_live` line, and the pipe drops the sweep's exit code. The ruling has three parts:

- The declared after-value (228) and every clause of the statement re-derive at head with one plain command each: the count, the sweep alone and the S-id check. So C verifies on what it states.
- The declaration was frozen, not narrowed after landing.
- The weak argv is a claim-sizing defect, routed below. This class repeats from round 51 (D's statement wider than its counter), so this is the second consecutive round. A third trips the drift sentinel.

**Attack on C's integrated text (substituting for the falsify wave that did not run).** Seats AttackCEntryA (§§1–6, 35 sentences) and AttackCEntryB (§§7–12, 20 sentences) re-opened the cited rows. Results:

- **Supported at stated strength:** 46 of 55 sentences (4 more partly supported, 5 not supported as cited), including:
  - the reach figures 2 km, 10 km "reported" and 20 km;
  - the Turkish 8 bands in 4 groups;
  - Silbo's 2 vowel slots against 4 distinct bands;
  - 39.15 bits/s over 17 languages;
  - 70% for words against 80–90% for sentences;
  - the Yorùbá and Akan court roles, and the Kuşköy taboo;
  - the La Gomera 1999 mandate;
  - the 80/40 and 70 counts, each with its counting standard.
- **Grounding:** DR-SRG-01..05 rest on cited rows. §9 is marked NON-CANON throughout.
- **Defects found (none false):**
  - **Unregistered source.** Line 104 quotes Silbo's range "up to five kilometres" with hamlets in the ravines as `(S157, -2)`. This closure fetched the S157 Wayback capture 20260204053249 and found no "kilomet" or "ravine" on the page. The quote is in the UNESCO nomination form 00172 (`ich.unesco.org/doc/src/01610-EN.doc`, Wayback `2018id_`): "an unlimited range of messages over a distance of up to five kilometres". That source was opened by seat ScribeSec08Ecology but has no SOURCES row.
  - **Draft-id fragments.** `grep -o -E ', -[0-9]+\b'` finds 11 tokens on 8 lines (104, 106, 107, 113, 174, 177, 179, 181). Integration left these seat draft-ids unmapped. All but the line-104 one map to registered rows (S162, S159, S174, S175, S176, S157, S180) through the committed seat reports.
  - **Wrong row cited.** On line 106 the "working their farms" quote is in S162, not S159. On line 113 the mobile-phone decline is in S159, not S163.
  - **Over-reads:**
    - line 54: "two tones (Suruí) force fixed formulas" (S135 says "more formulaic and therefore more predictable");
    - line 54: Hmong "(Laos, Thailand, United States)", which S135 does not list;
    - line 76: /b/ merging with /k/ (S147 states it for [p] only);
    - line 79: "learned young", an inference from one MPI deposit;
    - line 121: one drummer's biography (S165) stated as "Akan practice";
    - line 176: the sub-quote "primitive peoples" is not on S181's page.

The protocol's harm test is "found false". None of these meets it: each fact checked is true in a source the round opened and committed. But line 104's figure is not checkable from the registry, and the fragments are not stable IDs (QUALITY criterion 1). They stay open defects of the admitted entry until the lane repairs them.

## Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| depth | improved | D 5 → 0 re-measured; all five re-cited lines carried by re-opened S096/S097; 1974 set marked `(to-verify)` |
| coverage | improved | C 227 → 228; acceptance exit 0; sweep alone exit 0, 228 rows = 228 files; 49 of 49 cited rows mined with the entry in `used-by`; gap at `147cfde` 0 filename owners |
| calibration | unchanged | not claimed. SCORECARD's round-52 values match observed state (D 0, C 228, rows 183, A=106 B=69 C=8, mined 142 queued 33 rejected 8). SHONEN line 6 is now correct. Line 8's corrected split "53 mined, 8 queued" does not match the observed 52 mined, 9 queued for S071–S131 at `2b956d7`: S081 has been `queued` since `da31d3c` |
| operability | unchanged | not claimed; the criterion-10 checker is a new gate, recorded, not a claim |
| freshness | unchanged | not claimed; paused by the open round-11 L0 question |
| adjacency | unchanged | not claimed; C hands off instruments, sound production and canon (§12); connector found 0 sibling owners |

`git diff 2b956d7c 2eb489fb -- SCORECARD.md` only appends a round-52 section and edits no prior row. It adds no capability row. Pre-existing SOURCES rows: only S094 changed, and only in `status`/`used-by`. A diff of S001–S131 with columns 9, 11 and 12 blanked is empty.

## Discernment spot-check

| item | gate decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S139 (Seifart et al., Bora manguaré, PMC5936885) | admit, tier A, mined | https://pmc.ncbi.nlm.nih.gov/articles/PMC5936885/ (curl, 200) | agree | All four Gate quotes are verbatim (14, 23, 15 and 13 words): §1.4 "up to 20 km away", "only two pitches (one of each drum)", the four rhythmic units and the few lexical contrasts. It is a primary open-access paper, so tier A fits |
| S145 (Rialland 2003, ICPhS) — new row, quote checked | admit, tier A, mined | https://www.internationalphoneticassociation.org/icphs-proceedings/ICPhS2003/papers/p15_2131.pdf (curl, 200, `pdftotext`) | agree | Content is present: "It was commonly used in the past to convey messages over distances of 2 or 3 kms and could be heard as far as 8 kms". Two defects. The Gate quote ("Silbo Gomero was commonly used…", 18 words) silently replaces "It was" inside the quotation marks. The passage sits on printed p. 2132, not p. 2131 |
| S157 (UNESCO element 00172, Silbo Gomero) | admit, tier B, mined | live ich.unesco.org: 200, an image and audio captcha page, not passed; Wayback 20260204053249 (200) | agree | Both Gate quotes are present ("two distinct whistles replace the five Spanish vowels…", 15 words; "replicates the islanders' habitual language (Castilian Spanish) with whistling"). A Wayback route is ordinary under criterion 10. But the row's own cells do not say the live captcha was met and not passed, which criterion 10 asks for. The entry's line-104 "five kilometres" is not on this page (above) |
| S178 (Wikipedia, Guanche language) | reject, tier C | https://en.wikipedia.org/wiki/Guanche_language (curl, 200) | agree | Quote verbatim in the History section (14 words). A tertiary encyclopedia page is a lead only. The entry does not cite it. The Gate line still says "queued" while the row and the change log say `rejected` |
| S132 (Battison 1974, supersedes S094) | reject | https://ida.gallaudet.edu/cgi/viewcontent.cgi?article=1004&context=sls (one plain curl) | agree | HTTP 403, `server: cloudflare`, `cf-mitigated: challenge`, matching the row and `prereq-access-check.txt`. It cannot be reached by ordinary means, so it is rejected under criterion 10 |

The sample agrees with the gate on three admits and two rejects. Census: `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → `kotodama ok`, exit 0, W04 duplicate-URL warnings on S127–S133 only (superseding rows by design). Rows 131 → 183, malformed 0.

**Criterion 10 (the round-51 disagreement), evidence-verified.** `reports/round-52/telemetry/prereq-access-check.txt` was committed in `147cfde` and timestamped 10:38:02Z on tree `2b956d7c`, before the commit at 10:38:30Z. It shows the self-test at 10/10 and the live run on the base registry with `ACCESS: 1 flagged rows, 6 findings`, exit 1 (S094 `mined` plus 5 citing lines). The checker can fail. `final-measures.txt` shows it clean after the change (`2 flagged rows, 0 findings`, exit 0) and the widened self-test at 15/15. The criterion cites lesson R52-M1. It was not re-executed (lane gate).

## Wave shape and the `solutionSpace` field

- `.ufo/waves/round-52/build-dispatch.json`: `counts.total` 35. Policy v1 band 32–64. Roles: scribe 14, reviewer 7, critic 5, scout 4, executor 3, connector 1, mutation-tester 1. Attack seats (reviewer, critic, mutation-tester) are 13 of 35 (37%). No `model` key anywhere in the payload.
- The round total of 35 is inside the 32–100 band. The falsify wave did not run because Main froze scope at 12:32Z. The addendum's wave 2 is conditional, so this is not a lane conformance defect. Its cost is that C was unattacked after integration, which this closure covered above.
- **`solutionSpace` classification: a conformant host-binding adaptation, not a policy deviation.**
  - The OMP `task` schema requires `solutionSpace` on every task item (this closure's own `task` tool rejects items without it).
  - The field carries no route, model, seat count or role change.
  - Evidence gap: the validated payload `build-dispatch.json` holds 0 `solutionSpace` strings, and the bytes actually sent are not committed. Only the undispatched `residual-dispatch.json` shows the pattern (8 strings for 8 tasks). Future waves should commit the sent payload.

## Trend verdicts

- **expansion: improved.** One new entry on ground that had 0 filename owners at `147cfde` and only a partial topic owner. It cites 49 rows, every one `mined` with the entry in `used-by`, and is indexed at footer total 228. Counter-evidence: line 104's quoted range rests on an unregistered source, and 11 draft-id fragments are unresolved (routed).
- **quality: improved.** D moved five lines off a source no fresh session can open onto two pages this closure re-opened and found carrying every detail. Two over-reads were cut and an unverifiable set was marked `(to-verify)`. The post-integration attack found no admitted entry false. Counter-evidence: the over-reads and mis-cited rows listed above, which the lane must correct.
- **discernment: improved.** The round-51 outside disagreement (S094) became QUALITY criterion 10. It is grounded in lesson R52-M1, and its checker is shown able to fail on the base. The outside sample agrees with the gate on three admits and two rejects. Counter-evidence:
  - R52-M3 repeats the claim-sizing class, the second round running.
  - The SHONEN line-8 fix introduced a new split mismatch.
  - Gate-text slips: the S178 status, and the S145 quote substitution and page.

## Routed defects (lane, next round)

1. **C entry citations.**
   - Register the UNESCO nomination form 00172 (01610-EN.doc) as a row, or re-cite line 104's range or mark it `(to-verify)`.
   - Replace all 11 `, -N` draft-id fragments with S-ids, and teach the provenance gate to flag them.
   - Fix line 106 (S162) and line 113 (S159).
   - Soften or re-source the over-reads on lines 54, 76, 79 and 121, and the "primitive peoples" sub-quote.
2. **Claim sizing (R52-M3, 2nd consecutive round).** The next declaration's acceptance must exit nonzero when the README row is missing. Gate on the sweep's own exit status or on `missing_from_index 0`, not on a piped `grep`.
3. **Calibration.**
   - SHONEN line 8 says "53 mined, 8 queued"; the observed figure is 52 mined, 9 queued (S081).
   - The filed round-51 SCORECARD frontier line ("S071–S122 mined") carries the same error and needs an appended correction, not a rewrite.
4. **Gate text.**
   - S178's Gate line says "queued".
   - S145's Gate quote substitutes words inside the quotation marks and gives the wrong page (2132, not 2131).
   - S157's row does not record the captcha met and not passed.
   - Duplicate "Seat:" tags on the S139 and S172 lines.
5. **Leftover.** Resolve the uncommitted `.ufo/waves/round-52/build/ScribeSec05Drummed.md` edit: commit it as late seat output, or revert it.
6. **Carried.**
   - The undrafted drummed-speech and decline sections, and the phonetics §7 ownership wording.
   - The checker's limits and the `dry-run.py check` gaps.
   - S072, and the separability spelling misses.
   - Index this file in `corpus/lessons/README.md`.

SHONEN: all four boxes are `[~]` with asserted pointers and no named non-author verifier. This closure does not judge them fully checkable. Promotion is operator-owned.
