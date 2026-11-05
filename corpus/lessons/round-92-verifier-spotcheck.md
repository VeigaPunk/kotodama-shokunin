author: hyaku closure (non-author integrator, @m_zfl)

# Round 92 — non-author verifier spot-check (kotodama)

Subject: kotodama round 92, claims O (operability) and C (coverage), lane tip `0948cdb9fb8b63005bcbf977f810b9d54edefa7c`, base `21350361500aa000b90f91082bf9d7295a9c24cd`, freeze `066b9728fc64e78735769c4740d05c1000d31a3b`.
Report: `.ufo/reports/round-92/kotodama.md` (fleet commit `4468b372`, on origin/main).
Method: plain measurements over committed bytes (git, grep, python), fresh re-opens of sources over HTTP, and committed evidence for lane-owned gates. No lane gate was executed by this closure.

## 1. Conformance

| check | command | observed | result |
|---|---|---|---|
| report attribution | `git log --format='%an %H' -- .ufo/reports/round-92/kotodama.md` | `kotodama-shokunin <kotodama@shokunin.local>`, commits `4468b372` (final) and `9988cf8a` | lane identity |
| report in fleet main | `git branch -r --contains 4468b372` | `origin/main` | pushed |
| cited hashes ancestors | `git -C kotodama-shokunin merge-base --is-ancestor <h> main` for `21350361 066b9728 66b3ae93 b83a1dae 1473606b 793fa35a 0948cdb9` | all seven exit 0 | pass |
| lane state | `scripts/hyaku/jj-lane.sh state …/kotodama-shokunin` | `branch=main local=0948cdb9… remote=0948cdb9… ahead=0 behind=0 tracked=0 untracked=1` | ahead=0 |
| remote tip | `git ls-remote origin refs/heads/main` | `0948cdb9fb8b63005bcbf977f810b9d54edefa7c` | pushed |
| leftovers | `git status --porcelain` in lane | `?? .ufo/waves/round-92/w1.ready.dispatched` only | not round work by content; see §6 item 6 |
| driver lines | `grep -n "kotodama round=92" .ufo/watchdog.log` | `2834:…09:27:07… launch kotodama round=92 pgid=1140163 driver=hyaku-inline attempt=1`; `2852:…11:04:38… complete kotodama round=92; hyaku-inline attempt=1` | digests match the prompt |
| SHONEN heading | report `## SHONEN` | four lines, each `[~]` with a pointer; no `[x]` | pass |
| required sections | report headings | Work performed, Landed changes, Before→after, Sources & frontier, Trend verdicts, SHONEN all present | pass |
| wave shape | report `## Round shape` | 10 seats (3 executor, 1 scribe, 1 scout, 1 connector, 2 reviewer, 1 critic, 1 mutation-tester); attack 4/10 | within 8–16; attack ≥25 % |
| L2 role floor | prompt §3 vs wave | planner is not a seat (report: L1 holds planner; validator rejects planner) | conformance defect, status-neutral |
| stale-lane | report `## Stale-lane` | one sentence: no other mission open; no progressing/silent row | thin; conformance defect, status-neutral |

Conformance defects are status-neutral and do not bar admission. Lane status is `ok`: the report is real, its cited commits exist and are ancestors, and the lane repo is pushed with no round-work leftovers.

## 2. Per-claim re-check

### Claim O — operability (grader v3, `tools/check-advance-evidence.py`)

Evidence-verified (committed bytes; lane gate not executed):

- Tool sha at tip: `git show 0948cdb9:tools/check-advance-evidence.py | sha256sum` → `905be2fed386c491d52224832ea75ed8c7b02e67c1b021b2c66511658c1c1422`, equal to `claims.json` `O.tool_sha256`.
- Base tool sha: `git show 21350361:tools/…| sha256sum` → `88597a66c7912861d0a593f984b9eb224a3c46cba3b35d06209b529bc6031093`, equal to `O.v2_tool_sha256_base`.
- Frozen-inputs stability: `git diff --stat 066b9728 0948cdb9 -- reports/round-92/claims.json reports/round-92/measure92.py reports/round-92/mutants.py tools/check-advance-evidence.py reports/round-92/controls/stub-tool.py reports/round-92/controls/make-counterfeits.py reports/round-92/evidence` → empty. Nothing frozen moved after the freeze.
- Selftest committed: `reports/round-92/controls/selftest-at-instruments.txt` → `SELFTEST PASS 89/89`; `grep -c '^  ok '` → 89.
- Mutation receipt committed: `reports/round-92/mutation-score.txt` header `# tool sha256 905be2fe…`, `# clean selftest rc=0 ['SELFTEST PASS 89/89']`, `MUTATION-SCORE: 60/60 killed, 0 survived, 0 broken-pattern`.
- Lands receipt committed: `reports/round-92/final/lands-O.txt` → legs TOOL, SELFTEST, OKCOUNT, REFUSALS, MUTATION, MUTRECEIPT, STUB all PASS; `MEASURE92-O: PASS legs=8/8`.

Re-measured with plain counts (refusal names from `claims.json` `O.refusal_cases`, 21 names; `grep -cF` equivalent in python):

- base tool source: 9 of 21 names present (`git show 21350361:tools/check-advance-evidence.py`). The frozen `O.before` text says 12/21; the lane's erratum R92-M9 records 9/21. I confirm 9.
- tip tool source: 21 of 21 present.
- each of the 21 names is present in `reports/round-92/controls/selftest-at-instruments.txt`.

Not re-measured: the seven-counterfeit battery (lane control, sha-pinned builder) and the selftest rerun. The D3 intermittent selftest failure (`88/89` in a reviewer window, not reproduced by the lane) is unresolved and is an open risk to any re-run.

Verdict O: **verifies on the frozen predicate. Operability = improved.** Bounds: the frozen predicate does not claim completeness; 16 of 21 new counterfeits survive v3 (CriticClaims92, routed to round 93).

### Claim C — coverage (`corpus/knowledge/linguistics/ideophones-mimetics.md`)

Re-measured with plain commands (base `21350361` vs tip `0948cdb9`):

| quantity | base | tip | command |
|---|---|---|---|
| filename owners (ideophone\|mimetic\|onomatopoe) under corpus/knowledge | 0 | 1 | `git ls-tree -r --name-only <rev> corpus/knowledge \| grep -ciE '(ideophone\|mimetic\|onomatopoe)'` |
| linguistics partition files | 36 | 37 | `git ls-tree -r --name-only <rev> corpus/knowledge/linguistics \| wc -l` |
| registry rows | 880 | 884 | `git show <rev>:corpus/SOURCES.md \| grep -cE '^\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'` |
| tier-A rows | 518 | 522 | awk on column 5 |
| SOURCES.md numstat | — | `4 0` | `git diff --numstat 21350361 0948cdb9 -- corpus/SOURCES.md` (additions only) |
| entry size / `##` sections | — | 28814 B / 12 | `git show 0948cdb9:<entry> \| wc -c`; `grep -c '^## '` |
| README diff | — | one deleted line `## linguistics/ (36)`, replaced by `(37)`, plus an added row and a Round 92 section | `git diff 21350361 0948cdb9 -- corpus/README.md` |

Committed evidence: `reports/round-92/final/lands-C.txt` → `MEASURE92-C: PASS legs=4/4` (ENTRY, INDEX `CORPUS-INDEX: OK files=264 rows=264 findings=0`, APPENDONLY); `reports/round-92/final/tip-C.txt` → `PASS` at stamped revision `793fa35a` (the entry's last change is at `1473606b`; the tip commit adds only the receipt). Frozen-input stability as in O.

Fleet census (requested by the round prompt): `scripts/sources-census.sh validate --root /home/vgpnk/Projects/shokunin kotodama` → rc 0. The output lists warnings W04 (duplicate URLs across scopes) and W01 (tierC mined used-by). None names S957–S960. Pre-existing, not new.

Re-opened sources (see §4) confirm the four new rows' quotes and the entry's numeric claims: 162 words per ideophone (S958, Gospel of John, 13 types / 73 tokens), 1 per ~31 words in conversation (S958 Table 16), 64 children, 29 boys / 35 girls (S960).

Premise caveat (recorded, not a verdict change): the claim's frozen "before" says the nearest owner `sound-symbolism.md` has "no ideophone-class entry". At base, `sound-symbolism.md` §6 ("Ideophones — the depictive class") already holds a word-class definition, grammar profile, reduplication, giongo/gitaigo and a five-step register procedure (`git show 21350361:corpus/knowledge/linguistics/sound-symbolism.md` lines 99–111). The lane's claim is defined as a *dedicated-entry* gap, which the counter measures; that gap existed. The overlap is a contested-scope trade for the operator (L0 `kotodama | round-92`), not an absorption.

Verdict C: **verifies on the frozen predicate. Coverage = improved**, qualified by the §6 overlap.

## 3. Per-axis verdicts

| axis | verdict | basis |
|---|---|---|
| operability | improved | O verified (§2) |
| coverage | improved | C verified on its dedicated-entry predicate (§2); overlap with §6 reported as a trade |
| depth | unchanged | no existing entry deepened; no SKILL/QUALITY change in scope |
| freshness | unchanged | no registry row re-verified, re-dated or repaired; paused by open L0 kotodama round-11 and round-89; lowest-axis obligation neither met nor waived (disclosed by the lane) |
| calibration | unchanged | lane made no calibration claim; the closure finding in §4 is discernment, see §5 |
| adjacency | unchanged | `sound-symbolism.md` not edited; the overlap is intra-lane, reported by the lane and routed |

No axis is harmed. Admission rule: claims verify and no axis is harmed → admitted.

## 4. Discernment spot-check (LEARNING.md)

Gate decisions are from `corpus/lessons/round-92.md` `## Gate` at tip. Re-opened 2026-11-05 by plain HTTP (`curl/8.7.1`), with committed captures in `reports/round-92/evidence/` for the admits.

| item | decision | re-opened source | agree/disagree | reason |
|---|---|---|---|---|
| S957 | admit (A, mined) | `https://typologyatcrossroads.unibo.it/article/view/19369` → HTTP 200 (50 KB); committed `S957.txt` | agree | quote "whether or not ideophones make up a clear-cut word class in different languages" present in live text and committed capture (13 words, ≤25) |
| S958 | admit (A, mined) | `…/article/view/16393` → HTTP 200; committed `S958.txt` | agree | quote "do they constitute a word class on their own, or should they be subsumed under another word class" present live and committed (18 words); the entry's 162-word and 31-word frequency figures are in the captured text |
| S959 | admit (A, mined) | `…/article/view/16466` → HTTP 200; committed `S959.txt` | agree | quote "complex predicates consisting of an invariant coverb followed by an inflecting light verb, most commonly the verb alä 'say'" present live and committed (ASCII apostrophe in my check; the lesson uses curly quotes; no content difference) |
| S960 | admit (A, mined) | `https://www.frontiersin.org/articles/10.3389/flang.2026.1785036/full` → HTTP 200 (525 KB, redirected to `/journals/language-sciences/…`); committed `S960.html` | agree | quote "Sound-symbolic effects have been claimed to facilitate word learning, because of the motivated relationship between form and meaning" present live and committed; abstract says younger children are "mostly insensitive" and the sample is 29 boys / 35 girls, n=64 |
| DOAJ search `ideophone` | 20 results re-queried | `https://doaj.org/api/search/articles/ideophone` → 20 records | agree | the four admits are among the 20; the 16 others match the lesson's exclusion list by title (one descriptive slip, see below) |
| Siamese musical instruments (2024) | reject (search log) | `logos-verlag.de` → HTTP 200 (19 KB); abstract on Ayutthaya diplomacy; 1 "ideophon" hit | agree | off-topic; the captured text is not about ideophones |
| Uirtus literary interjections (2025) | reject | `uirtus.net/…2025/11/uirtus.2025.2984.pdf` → HTTP 200 (4.5 MB); `pdftotext` 26 "interjection", 7 "onomatop", 3 "ideophon" | agree | interjections are a separate class (S957 says so); the paper is about interjections in text messages |
| Lulubo phonology (1987) | reject (duplicate OJS + FLVC) | `journals.flvc.org/sal/article/view/107478` → HTTP 200; abstract mentions "special features of ideophones" among six items | agree | ideophones are a minor part of a phonology outline |
| Awetí motion events (2015) | reject | `journals.openedition.org/cognitextes/765` → HTTP 200 (83 KB text); Résumé names "gesture and ideophones" as the two modes studied; 144 "ideophon" hits | **disagree** | excluded on DOAJ title alone. The text is an ideophone-bearing corpus study of motion events. The exclusion gives no reason on record |
| Zulu ideophone lexicography (2011) | reject | `lexikos.journals.ac.za/pub/article/view/429` → HTTP 200; abstract: the ideophone is "a word class not unique to but highly characteristic of the Bantu languages", meaning "highly elusive" | **disagree** (reason absent) | on-topic for word class and meaning; if the reason is "lexicography is out of scope", the lesson must say so per candidate |
| Turkish ideophone vowel alternation (Signifiances 2020, French-language) | reject | `revues.polen.uca.fr/…/Signifiances/article/view/232` → HTTP 200 (32 KB); Résumé "analyser l'alternance vocalique des idéophones du turc" | **disagree** (reason absent) | on-topic, accessible, and the search log calls it "a French study" without saying it concerns Turkish. Language alone is not a stated reason |
| Arusa Maasai ideophones (Open Linguistics 2022) | reject (search log: "DOI front door, not fetched") | `doi.org/10.1515/opli-2022-0220` → 202 with 0 bytes after redirect to degruyterbrill.com | unprovable (could not re-open) | title "Ideophones in Arusa Maasai: Syntax, morphology, and phonetics" is on-topic. Exclusion is an access decision, not a judgment; should be "unassessed" |
| Iconic hand gestures from ideophones (2025) | reject ("DOI front door, not fetched") | `doi.org/10.1515/cog-2024-0033` → 202 with 0 bytes | unprovable (could not re-open) | on-topic title; same access-vs-judgment label issue |
| Japanese pain descriptions (2025) | reject ("Cambridge front door, not fetched") | `cambridge.org/core/product/identifier/S1866980824000607/…` → HTTP 429 | unprovable (could not re-open) | on-topic title ("Ideophones are more reliable than metaphors…"); same label issue |
| Mandarin ABB vividness (2024) | reject | Cambridge `S186698082400022X` → HTTP 429 | unprovable (could not re-open) | not re-openable from this host |
| Korean vowel phonotactics (2023) | reject | `mdpi.com/2226-471X/8/3/172` → HTTP 403 | unprovable (could not re-open) | not re-openable |
| Persian onomatopoeias (2023) | reject | `zabanpazhuhi.alzahra.ac.ir/…pdf` → no connection | unprovable (could not re-open) | not re-openable |
| Arabic sound-meaning (2019), Mofolo Chaka (2013), comics libretto (2024) | reject | `alustath…/874` → HTTP 404; Mofolo and comics not fetched | unprovable | title-only; no re-open possible in this pass |

Tally. Admits: 4 re-opened, 4 agree. Rejects re-opened: 6 (agree 3: Siamese, Uirtus, Lulubo; disagree 3: Awetí, Zulu, Turkish). Rejects unprovable: 7 (could not re-open). Trend-level reading of the spot-check: admits agree on both source and content; rejects do not. The lane's gate decided rejects on DOAJ metadata for every exclusion, and it gave no per-candidate reason for 16 of 16. `## Gate` says "No row was rejected this round", which is literal (no registry row was rejected), but the exclusions carry the decision.

Descriptive slip (routed, minor): the lesson calls the Signifiances item "a French study of vocalic alternation in ideophones". The article is French-language and about Turkish ideophones.

## 5. Trend verdicts

- **expansion — improved (qualified).** Four A-tier mined rows (S957–S960) cited by a dedicated entry on ground that had no filename owner. Qualification: `sound-symbolism.md` §6 already holds part of the same ground (§3 above). The trade is reported to the operator (L0), not absorbed.
- **quality — unchanged.** No admitted entry was re-verified, deepened or superseded this round. The entry's numeric and quoted claims that I re-checked agree with their sources, but that check is this closure's, not the lane's re-verification duty.
- **discernment — unchanged.** Admits: 4/4 agree. Rejects: 3 of 6 re-opened disagree, and 7 could not be re-opened. The disagreements are first recorded in this closure, and the lane's round record has no lesson for them yet. LEARNING.md grades discernment `harmed` when a disagreement is left unlearned. I read "left unlearned" as applying to a disagreement the lane has had before it. These are routed to round 93 as must-learn items (§6 item 1). If round 93's closure finds them unlearned, the verdict becomes `harmed`.

## 6. Routed defects for the lane (round 93)

1. **Discernment (must learn).** Re-decide the 16 search-log exclusions with a per-candidate reason. Re-decide Awetí (2015), Turkish Signifiances (2020) and Zulu Lexikos (2011) on their captured text. Re-label the four unfetched candidates (Arusa Maasai, iconic gestures, Japanese pain, Mandarin ABB) as `unassessed (access)`, not `excluded`. Add a grounded QUALITY criterion: title-only triage is not an exclusion; a rejected candidate needs a topic or access reason on record. Write the lesson that cites this closure.
2. **Overlap (operator).** `ideophones-mimetics.md` vs `sound-symbolism.md` §6 is open under L0 `kotodama | round-92`. The lane must not extend either without the operator's choice (a), (b) or (c).
3. **Premise correction.** The round-92 claim's "before" describes `sound-symbolism.md` as having "no ideophone-class entry". §6 is an ideophone-class section. File an append-only erratum naming the sentence and §6.
4. **Tool, carried from R92-M7 to M10:** 16 of 21 new counterfeits survive v3 (incl. A6g unhandled `AttributeError`); nine selftest-level survivors outside the frozen 60; `mutants.py` has no refusal path for missing `--work`; the C predicate does not run `check-cited-lines.py`; D3 intermittent selftest `88/89` unresolved — capture the reviewer evidence and reproduce it under load before the next O measurement.
5. **Lesson description slip:** "a French study … (Signifiances)" → French-language study of Turkish ideophones (see §4).
6. **Lane leftover:** `.ufo/waves/round-92/w1.ready.dispatched` is untracked in the lane repo. It is the dispatch-renamed wave marker. Resolve it under the lane's own guard (commit, or remove), not in a round commit. Status-neutral.
7. **Conformance (status-neutral):** L2 role floor — the planner is not a seat (held by the L1); the stale-lane section lacks the per-mission progressing/silent row; the `Wave-1 dispatch` commit message (`66b3ae93`) says 4 executors, the actual count is 3 (the report corrects this).
8. **Freshness:** paused by open L0 kotodama round-11 and round-89. Operator ruling still outstanding; the lowest-axis obligation is neither met nor waived this round (disclosed).

## 7. Notes for the operator

- SHONEN: none of the four boxes is checkable by a non-author from this closure. Box 1's §10/§11 decision tables and procedure were explicitly deferred to closure by the lane's `## Understanding and trial`; I did not do the rule-by-rule check, so box 1 stays `[~]`. Box 4 is blocked by the open §6 overlap. Boxes 2 and 3 were not examined in this pass.
- No promotion, mint or other-lane write was performed by this closure.
