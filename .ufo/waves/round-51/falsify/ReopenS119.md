# ReopenS119 — falsify report: SOURCES rows S119–S124

- Seat: KotodamaR51a3.ReopenS119 (leaf; read-only on the lane; writes only this file).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, HEAD `9feb69e`. Tracked files are clean; only `.ufo/waves/round-51/` is untracked.
- Item attacked: `corpus/SOURCES.md` rows S119–S124 (lines 148–153) and their lesson Gate bullets (`corpus/lessons/round-51.md:76–81`). Checked per row: quote, kind, tier (QUALITY criterion 6, `corpus/QUALITY.md:29`), scope, anchor, used-by.
- Committed bytes: `git show HEAD:corpus/SOURCES.md` has the same md5 as the working copy (`822a15ebf549b84acf186f94a675936c`), so the rows read here are the landed rows.
- Access date for every URL below: 2026-10-22.

## Verdict: FAILS as filed

- Quotes: 6 of 6 appear verbatim in the opened sources, each at most 25 words. 5 of 6 sit at the stated location. S124 sits at Introduction ¶2, not "Abstract and Introduction ¶1".
- Tier A is not supported for S119 or S122. Both rows point at a response or commentary, not an original paper, and criterion 6 reserves A for primary or authoritative sources for the exact scope. These two rows are the FAILS.
- S120, S123 and S124 hold with fixes. S121 holds.
- used-by is correct for all six. S119–S122 name the entry path. S123 and S124 carry `—`, and the entry cites neither (commands 4, 6 and 7).

| Row (line) | Kind as filed | Tier as filed → supported | Scope | Anchor | Quote | used-by | Verdict |
|---|---|---|---|---|---|---|---|
| S119 (148) | paper | A → B | "timing" holds; "roughly age 12–20" is L2-only | "Points of agreement" ¶2 holds; "decades of signing" needs reply section "Language measurement…" ¶6 | verbatim at ¶2 (14 words) | entry line 208 | FAILS |
| S120 (149) | dataset | A → A | holds | holds (page header and both headings present) | verbatim (4 words) | entry lines 11, 209, 219 | HOLDS-WITH-FIXES (low) |
| S121 (150) | docs | B → B | holds | holds (all four FAQ items present) | verbatim (21 words) | entry lines 11, 209, 210, 213, 215, 219 | HOLDS |
| S122 (151) | paper (a Commentary) | A → B | capital-D convention holds; "40+ years" and "no evidence … easier" are uncited in the source | Background ¶1 holds; "¶4" is wrong, the sentence is ¶5 | verbatim at Background ¶1 (22 words) | entry line 211 | FAILS |
| S123 (152) | book (publisher product page) | B → B | holds (publisher description) | "paragraphs 2–3" is loose; both claims sit in one paragraph | verbatim in Wayback capture (19 words) | `—` correct | HOLDS-WITH-FIXES (low) |
| S124 (153) | paper (original research, CC BY) | A → A | holds | wrong: sentence is Introduction ¶2 | verbatim (18 words), but not at the stated location | `—` correct | HOLDS-WITH-FIXES (medium) |

## Findings (severity, exact pointer, smallest fix)

Corrections to a filed row go through a superseding row whose teaches opens `supersedes S0NN —` (`corpus/SOURCES.md` lines 9–12, append-only). Use the next free id (S125 onward). Changes to an entry's citation must log the used-by change in the round lesson.

**F1 — high — S119 tier A is not supported: the row cites the authors' reply to commentaries.**
- Evidence: PMC6818964 (doi 10.1017/S1366728918000585, Biling 21(5):938–944) opens "We thank the commentators for their thoughtful critiques…", has no abstract, and answers commentators throughout. Raw HTML contains that opening once. CrossRef types the DOI as a journal article, and its "abstract" is the reply's opening paragraph. Europe PMC's "research-article" label does not change the text.
- Criterion 6 reserves A for original or authoritative sources. A reply's "Points of agreement" is the authors' summary of the field's consensus, which is a secondary statement. Tier B.
- Smallest fix: one superseding row, tier B, kind "reply to commentaries", anchor "Points of agreement" ¶2 plus "Language measurement…" ¶6. Leave S119 as it is. Move the entry's single S119 citation (`corpus/knowledge/linguistics/sign-languages-manual-modality.md:208`) to the new id. No entry claim needs tier A: the timing claim rests on reply ¶2 and the decades claim on reply ¶6.

**F2 — medium — The lesson's second S119 URL resolves a different DOI, and that keynote record carries the reply's body.**
- `corpus/lessons/round-51.md:76` cites Europe PMC for DOI 10.1017/S1366728917000724. That is the keynote, pp. 886–905, e-published 2017-12-26, PMC6329394. The row's DOI is ...918000585. The title check passes, but for the other article.
- PMC6329394 has keynote metadata but reply text. Its section headings match the reply's ("Points of Agreement", "What We Did Not Claim", … "Creating the Capacity to Learn Language"). It opens "We thank the commentators…". The keynote's abstract sentence "The hypothesis that children surpass adults…" occurs 0 times (command 12). CrossRef gives the keynote's real abstract: "age-onset effects for first vs. second language outcome are largely different".
- Europe PMC marks the keynote DOI "Subscription required". The keynote body was not verifiable from this lane. No paywall bypass was attempted.
- Smallest fix: replace the second Gate URL with the row's own DOI lookup, or drop it. Do not cite PMC6329394 as keynote text. If the keynote is cited, use its CrossRef abstract at tier B (criterion 6: abstracts are B) until its body is checked.

**F3 — medium — S119 teaches overreach: the "roughly age 12–20" cutoffs come from L2 studies.**
- Reply section "The shape of the L2 AoA function": cutoffs of 12, 15, 16, 17, 18 and 20 are listed "across L2 AoA studies". `corpus/SOURCES.md:148` presents them as the L1 critical-period range.
- Smallest fix (superseding row): teaches read "L2 AoA cutoffs debated, ages 12–20, from L2 studies; no L1 cutoff given".

**F4 — medium — S119 anchor does not carry the entry's "even after decades of signing" claim.**
- `sign-languages-manual-modality.md:208` cites S119 for "even after decades of signing". The anchor (Points of agreement ¶2) does not contain that. The support is in the reply's section "Language measurement and cognitive factors in late L1 acquisition", ¶6: Woll's case had 25 years of British Sign Language and Martin's 30 years of ASL, both with limited morphology and syntax.
- Smallest fix: add that ¶6 to the superseding row's anchor.

**F5 — low — "not deafness" in the S119 teaches is an inference.**
- The reply supports "it affects sign language too" (Points of agreement ¶1). It does not state "not deafness". Tag as [INFERENCE] or drop the phrase.

**F6 — high — S122 tier A for a Commentary.**
- The Springer page labels the item "Commentary" (`meta-citation_article_type: Commentary`; `meta-dc.type: Letter`).
- The scope claims are uncited where they matter. Background ¶5, "Over forty years of research… requisite grammatical properties", has no citation. "There is no evidence to back up the claim that sign languages are easier to learn…" (section "Second, misinforming and coercing behavior counter to the child's welfare") has no citation of its own. The nearby reference [81] supports the bilingualism sentence that follows it.
- SOURCES defines A as primary or authoritative for the scope, and B as strong secondary (expert write-up, survey, textbook). A commentary with no data is secondary for these statements, so B. The capital-D sentence (Background ¶1, verbatim) is the only part the entry uses, and it uses it under calibration code B at line 211. Calibration codes (`corpus/knowledge/verification/calibration-registry.md:35–39`) are claim statuses, not source tiers, so they do not support the A tier.
- Smallest fix: superseding row, tier B, kind "commentary", scope limited to the capitalization convention as the authors state it. Linguistic-status claims stay with S071, S077 and S078, which the entry already cites. Re-point line 211.

**F7 — low — S122 anchor paragraph is wrong.**
- The row says "Background ¶1 and ¶4". The "forty years" sentence is Background ¶5. The Background section has 5 paragraphs in the raw HTML.
- Smallest fix (superseding row): "Background ¶1 and ¶5".

**F8 — medium — S124 quote is at Introduction ¶2, not "Abstract and Introduction ¶1".**
- Raw HTML: section 1 has 17 paragraph elements, and the sentence "A deaf child in this situation develops a gestural communication system, called homesign, to communicate with family members" is ¶2. The one-paragraph abstract does not contain it (full-sentence check: not present).
- Smallest fix: superseding row with anchor "Introduction ¶2", and correct the Gate bullet location at `corpus/lessons/round-51.md:81` in the same round lesson. The teaches phrase "no accessible language model" paraphrases ¶2 ("without exposure to sign language") and holds.

**F9 — low — S120: the "own rule" has no anchor, and the count depends on the edition.**
- Subgroup page: "Subgroup of 161 languages" (131 + 29 + International Sign = 161). Methodology page (`https://www.ethnologue.com/methodology/`, "Sign languages"): "This edition of Ethnologue lists 159 living sign languages". It also limits the list to natural sign languages used exclusively within deaf communities, with manual codes excluded. So the "own rule" is real, but the row does not cite it, and the count differs by edition.
- Smallest fix (superseding row): add the methodology paragraph to the anchor, and record that 161 is the live subgroup count on the access date while the methodology gives 159 for its edition. Mark "so the categories are not settled" as the row's own gloss. Entry line 209 can carry "live page, 2026-10-22".

**F10 — low — S123 year, paragraph and source cell.**
- The MIT page says "Published: February 16, 1999" (Wayback capture 20221222142436). The row's "Brentari 1998" is the citation year S124's references also use. Add "(publisher page lists 1999)" to the source cell.
- "product description paragraphs 2–3": both claims sit in one paragraph, the one after the bold lead. Paragraph 3 is the author bio. Use "paragraph 2 (after the bold lead)".
- The source cell gives only the live URL, which returns 403. The verifiable copy is the Wayback URL the lesson Gate cites. Put that URL in the cell.

**F11 — low — checkability note (no row change).** With a custom User-Agent, Springer returns a 3,038-byte stub with HTTP 200. With curl's default agent it returns the full article (461,186 bytes). Record the agent with any Springer check.

**Entry impact.** None of the entry's admitted sentences depends on keynote text. Line 208's timing and decades claims rest on reply ¶2 and ¶6. Line 211 uses S122 under calibration code B. Lines 209 and 11 quote the S120 and S121 counts with their recheck rule. These findings change registry labels and anchors, not the entry's wording.

## Every URL opened (access date 2026-10-22)

| # | URL | HTTP | What is at the stated location | Rows |
|---|---|---|---|---|
| 1 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6818964/ | 200 | Reply to commentaries, no abstract. Opens "We thank the commentators…". DOI 10.1017/S1366728918000585, Biling 21(5):938–944. "Points of agreement" ¶2 holds the S119 quote. "Language measurement…" ¶6 holds the Woll and Martin cases. The 12–20 cutoffs are in "The shape of the L2 AoA function" and are L2 studies. | S119 |
| 2 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1017/S1366728917000724&resultType=core&format=json | 200 (JSON) | Keynote DOI: title matches; pp. 886–905; e-pub 2017-12-26; PMC6329394; DOI copy "Subscription required"; free copy is PMC6329394. (Lesson Gate second URL.) | S119 |
| 3 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1017/S1366728918000585&resultType=core&format=json | 200 (JSON) | Row's DOI: pp. 938–944; PMC6818964; pubType "research-article". | S119 |
| 4 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6329394/ | 200 | Metadata is the keynote's. Body is reply text: reply headings, opens "We thank the commentators…", keynote abstract sentence absent. | S119 |
| 5 | https://doi.org/10.1017/S1366728917000724 | 302 (CrossRef record fetched) | Keynote, journal article, 2017-12-26. Abstract is the keynote's ("…age-onset effects for first vs. second language outcome are largely different"). | S119 |
| 6 | https://doi.org/10.1017/S1366728918000585 | 302 (CrossRef record fetched) | Reply, journal article, 2018-06-13. "Abstract" is the reply's opening paragraph. | S119 |
| 7 | https://www.ethnologue.com/subgroup/2/ | 200 | "Subgroup of 161 languages"; "Deaf community sign language 131"; "Shared sign language 29"; International Sign listed separately; Plains Indian (psd) and Australian Aboriginal (asw) under Shared. | S120 |
| 8 | https://www.ethnologue.com/methodology/ | 200 | "Sign languages": "This edition … lists 159 living sign languages"; natural sign languages used within deaf communities only; manual codes excluded. | S120 |
| 9 | https://www.ethnologue.com/about/ | 200 | General about page; points to /methodology/; no sign-language rule. | S120 (checked; nothing added) |
| 10 | https://wfdeaf.org/contact/faqs/ | 200 | FAQ answers match S121 verbatim: "200+ national sign languages…, only 40%…"; "Each sign language is unique" (no universal sign language); "These terms are not acceptable"; "hearing-impaired" should not be used; "more than 70 million"; "no official count". | S121 |
| 11 | https://link.springer.com/article/10.1186/1477-7517-9-16 | 200 (default agent 461,186 bytes; custom agent 3,038-byte stub) | Article type "Commentary". Background ¶1 capital-D sentence (verbatim). Background has 5 paragraphs; "Over forty years…" is ¶5, uncited. The "Second, misinforming…" section holds the uncited "no evidence" sentence. | S122 |
| 12 | https://mitpress.mit.edu/9780262024457/a-prosodic-model-of-sign-language-phonology/ | 403 ("Failed to fetch URL (HTTP 403)") | Live page blocked, as the row says. | S123 (live) |
| 13 | http://web.archive.org/web/20221222142436/https://mitpress.mit.edu/9780262024457/a-prosodic-model-of-sign-language-phonology/ | 200 (capture 2022-12-22) | Publisher description: both claims in the paragraph after the bold lead; quote verbatim; "Published: February 16, 1999"; "Out of print". | S123 |
| 14 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13215104/ | 200 | Kita, Brentari, Goldin-Meadow; Cognition 264:106233 (2025 Jul 7); doi 10.1016/j.cognition.2025.106233; CC BY. Introduction ¶2 holds the quote; abstract does not. | S124 |

## Commands and exit codes

Commands used absolute lane paths or `git -C` on the lane. Nothing was written except this file; curl output went to memory or `/dev/null`.

1. `git -C <lane> rev-parse --abbrev-ref HEAD; git log --oneline -3; git status --porcelain` — exit 0. HEAD; commits `9feb69e`, `da31d3c`, `35f0d49`; status shows only `?? .ufo/waves/round-51/`. (Plain `git status` can refresh index stat data; no tracked content changed.)
2. `realpath <lane>; ls -ld …/.ufo/waves/round-51 …/falsify; command -v curl python3 jq git; curl --version; python3 --version` — exit 0. Both wave folders are real directories (not links). curl 8.23.0 at /usr/bin/curl; python3 3.14.8 at /usr/bin/python3; jq and git present.
3. Reads (no exit code): `reports/round-51/claims.json`; `corpus/SOURCES.md` 1–30 and 148–153 (raw); `corpus/QUALITY.md`; `corpus/lessons/round-51.md`; `~/.omp/agent/RULES.md`; `skill://godspeed`; the entry lines 195–223; `calibration-registry.md` 30–40; repo-wide grep for S119–S124.
4. `grep -n -E '^\| S1(19|2[0-4]) ' corpus/SOURCES.md` — exit 0. Rows 148–153.
5. `git --no-optional-locks -C <lane> show HEAD:corpus/SOURCES.md | md5sum` and `md5sum < corpus/SOURCES.md` — exit 0. Both `822a15eb…`.
6. `test -f corpus/knowledge/linguistics/sign-languages-manual-modality.md` — exit 0.
7. `grep -c -w` for each S-id in the entry — exit 0. S119 1 line; S120 3; S121 6; S122 3; S123 0; S124 0.
8. `grep -c -i -E 'kita|brentari|humphries|mayberry|woll'` in the entry — exit 1 (zero matches, expected). A wider earlier grep that added "ethnologue" was exit 0 with one hit: entry line 209, which cites S120.
9. HTTP status loop (`curl -w %{http_code}`) over the URLs in the table — exit 0.
10. Python checks in one process (curl in memory, nothing written): quote presence, paragraph counts, heading lists, sentence counts — exit 0 on the final runs. One earlier attempt exited 126 ("Argument list too long") before any check ran; its output was not used.
11. Springer size check, default and custom agents — exit 0 (461,186 and 3,038 bytes).
12. Keynote and reply raw-HTML counts — exit 0. Keynote abstract sentence: 0 in PMC6329394 and 0 in PMC6818964. "We thank the commentators": 1 in each.

## Installs and updates

None. Every check used tools already on the host: curl 8.23.0, python3 3.14.8, git (read-only) and jq. `RULES.md` was read. Pacman was not used, since transactions are paused host-wide.

## Unrun checks

- `python3 -B reports/round-51/boundary-count.py` — unrun (D counter; not in this slice).
- `find corpus/knowledge -name '*.md' | wc -l` and `python3 -B reports/round-28/readme/sweep.py` — unrun (C counters; not in this slice).
- `python3 -B tools/check-claim-separability.py reports/round-51/separability-manifest.json` and `reports/round-51/claims-agree.py` — unrun (not in this slice).
- `python3 -B tools/gates/provenance-audit.py corpus/knowledge/linguistics/sign-languages-manual-modality.md` — unrun (not in this slice).
- `lsp` — not applicable: no code under review.

## Residual risk and gaps

- The keynote body (DOI 10.1017/S1366728917000724) is unverified. The publisher full text is subscription-only, and the free PMC copy carries reply text. Any claim that rests on keynote text is unverified.
- Ethnologue's count depends on the edition: 161 on the live subgroup page, 159 in the methodology's "this edition" sentence.
- Springer output depends on the User-Agent string, and the MIT live page returns 403. The Wayback capture is from 2022-12-22.
- Tier judgments apply criterion 6 as written: a reply or a commentary is secondary for what the row states.
