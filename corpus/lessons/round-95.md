# kotodama round 95 — lesson

Round: kotodama round 95, attempt 1. Base `19aa4dd03dfd37b435d0b8ea5b313635d9d51592`; freeze `d41eb594d27fa71869c0c28d9c2dc051fda40079` (claims O, C, predispatch receipt and wave-1 spec). Claims O (operability) and C (coverage) are exactly as frozen in `reports/round-95/claims.json`; the frozen bytes are not amended here.

Freshness remains paused by the open L0 questions kotodama round-11 and round-89 ("Freshness axis-move claims are paused until ruled"; `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` lines 47 and 303, both still carrying no L0 ANSWER). The lowest-axis obligation is neither met nor waived this round, and no freshness claim is declared.

## Gate

Claim C's registry rows. Five new rows, opened by ordinary means on 2026-11-05 (plain `curl`, default user agent, `-L` follow-redirects, `--max-time 30`; no browser, no challenge passed, no verification disabled). Every quote below was re-verified by this seat against the committed capture bytes: each is an exact substring occurring exactly once (`bytes.count(quote) == 1`) and each is 25 words or fewer. The capture sha256 values are re-measured here and match `stage/ExecRegistry95/evidence/`.

- S970 admit A/mined. https://sciendo.com/pdf/10.2478/jef-2025-0006 — accessed 2026-11-05 — body: “the antiphonal way of performing Seto songs makes it possible for the lead singer”
- S971 admit A/mined. https://journals.library.columbia.edu/index.php/currentmusicology/article/download/5043/2312/ — accessed 2026-11-05 — body: “antiphonal nature of voceru performance, though not discussed in detail here, suggests that Corsican lament”
- S972 admit A/mined. https://mdpi-res.com/d_attachment/religions/religions-10-00235/article_deploy/religions-10-00235.pdf — accessed 2026-11-05 — body: “core, the keen was a sacred improvised chant”
- S973 admit A/mined. https://mdpi-res.com/d_attachment/religions/religions-15-00879/article_deploy/religions-15-00879.pdf — accessed 2026-11-05 — body: “was important in the role of the female professional mourner who performed”
- S974 admit A/mined. https://dergipark.org.tr/en/download/article-file/1673889 — accessed 2026-11-05 — body: “recitation, Sima praises the good deeds and grace of the deceased,”
| row | URL | access date | HTTP status | located quote (≤25 words, exact substring of the capture) | words | capture sha256 |
|---|---|---|---|---|---|---|
| S970 | https://sciendo.com/pdf/10.2478/jef-2025-0006 | 2026-11-05 | 200 | "the antiphonal way of performing Seto songs" | 7 | `dc7394e9862003b0b26e7631520e3dcb19832d25b19ddd4e6898cda06c371316` (S970.txt); `e8fb753b6b3adf3fe45075604e36e6c20034c5432748d19dd26aeb36465d3a8e` (S970.pdf) |
| S971 | https://journals.library.columbia.edu/index.php/currentmusicology/article/download/5043/2312/ | 2026-11-05 | 200 | "The antiphonal nature of voceru performance" | 6 | `656c45388dbfcab8f9de8a233eada5d8f8571647a1f04955605bff71cbc4a26a` (S971.txt); `85b821c7233c85bf1d3907b5db5ce98d368d19f6a06cdacc029a7df628345fbe` (S971.pdf) |
| S972 | https://mdpi-res.com/d_attachment/religions/religions-10-00235/article_deploy/religions-10-00235.pdf | 2026-11-05 | 200 | "Professional keeners took over." | 4 | `d3ff0209b9d80418bcc9345535f5fd440a3fc8a2433da6982c42a65d777293ce` (S972.txt); `1e0b0f8d8b529aae60ff2138d591aeb40465e778d11702b88b176d68334b30c8` (S972.pdf) |
| S973 | https://mdpi-res.com/d_attachment/religions/religions-15-00879/article_deploy/religions-15-00879.pdf | 2026-11-05 | 200 | "was important in the role of the female professional mourner" | 10 | `e017b3958dac14b32ff08a11f1750638e997c5df43ec9674a91413f5c42cac76` (S973.txt); `8750510347c20a3ef8a12112435cc917c2737a42a4ffeadab3f85b557720a5d9` (S973.pdf) |
| S974 | https://dergipark.org.tr/en/download/article-file/1673889 | 2026-11-05 | 200 | "ends with a refrain exclamation" | 5 | `251b4d3f420164baa4bdc6508e54736cb0d00a42bc66940363203c264060159d` (S974.txt); `f1e4be9fd0868713bf363ea18b368a501dd48d87dc7bd3039e801f4954ad2672` (S974.pdf) |

Rejected and unreachable candidates, one line each with its exact response and a reason class per QUALITY criterion 37 (topic, access or scope; never title-only). None of these is a registry row.

- Thrênoi to Moirologia (Oral Tradition 23/2, 2008) — UNREACHABLE, reason class access: curl exit 28, connection timed out after 30001 ms on the PDF, the site root and the issue page; the most on-point candidate for the moirologia professional-mourner facet, so no Oral Tradition row is proposed.
- MDPI Religions 10(4) article page and PDF (`https://www.mdpi.com/2077-1444/10/4/235`, `.../pdf`, `.../xml`) — UNREACHABLE, reason class access: HTTP 403 on every request; the candidate was recovered instead from the publisher's own asset host at HTTP 200, so it is a row and not an exclusion.
- MDPI Religions 15(7) article page and PDF (`https://www.mdpi.com/2077-1444/15/7/879`, `.../pdf`) — UNREACHABLE, reason class access: HTTP 403 (400- and 408-byte bodies); recovered from the publisher's asset host at HTTP 200 and landed as S973.
- Gender Performativity in Burgenland Croatian Laments (`https://minpaku.repo.nii.ac.jp/record/8716/files/SES105_14.pdf`) — UNREACHABLE, reason class access: HTTP 503 on two attempts.
- Olonets Karelian prichitannye tradition (`https://www.trad-culture.ru/sites/default/files/files_pdf/02_2026_...95-108.pdf`) — UNREACHABLE, reason class access: HTTP 404 (25345-byte HTML error page) at the locator OpenAlex published.
- Pure Corpses, Dangerous Citizens (`https://durham-repository.worktribe.com/preview/1371952/20127.pdf`) — UNREACHABLE, reason class access: HTTP 403 (5486-byte body).
- Shaping the pain, 2012 and 2011 (`http://www.doiserbia.nb.rs/img/doi/0350-0861/2012/0350-08611202139S.pdf` and the 2011 sibling) — UNREACHABLE, reason class access: connection timed out at 30 s on repeated attempts; both titles remain unsourced.
- Seto lamenting song via De Gruyter (`https://www.degruyterbrill.com/document/doi/10.2478/jef-2025-0006/pdf` and the legacy host) — UNREACHABLE, reason class access: HTTP 202 with 0 bytes (challenge interstitial); the same article was obtained at HTTP 200 from `sciendo.com/pdf/...`.
- Madwoman, Banshee, Shaman (`http://hdl.handle.net/10072/30483`) and Keening the Nation, the Bean Chaointe (`http://hdl.handle.net/1808/7785`) — UNREACHABLE, reason class access: HTTP 200 but a JavaScript-only DSpace shell (755 and 827 bytes, no article text).
- Mourners and mediums (`https://opus.bath.ac.uk/19457/1/Walter_Bt_Care_2008_27_3_p47.pdf`) — UNREACHABLE, reason class access: HTTP 200 but the bytes are an HTML portal page, not a PDF (46859 bytes).
- Semaine seto (`https://journals.openedition.org/efo/pdf/6912`) and Briséis et la plainte funèbre (`https://journals.openedition.org/mondesanciens/729`) — UNREACHABLE, reason class access: HTTP 200 but a ~1.5 KB / 1.6 KB shell, no article body.
- Mäetagused Arukask (`https://www.folklore.ee/tagused/mt2011.47.arukask.pdf`) — UNREACHABLE, reason class access: HTTP 404 (510 bytes), wrong filename pattern.
- Mäetagused Ing (`https://www.folklore.ee/tagused/nr08/ing.pdf`) — UNREACHABLE, reason class access: HTTP 404 (510 bytes).
- Folklore vol. 58 Kalkun at the wrong filename (`https://www.folklore.ee/folklore/vol58/kalkun.pdf`) — UNREACHABLE, reason class access: HTTP 404 (510 bytes); the file is `kalkun_oras.pdf`.
- Crossref `itkuviis lament refrain` — UNREACHABLE, reason class access: HTTP 429 (rate limited), empty body, so that query returned no records to screen.
- Kama, Pikne (2017), How old is runosong? Dating the motifs of burial-related folk songs (`https://www.folklore.ee/folklore/vol68/kama.pdf`, HTTP 200, 8226843 bytes) — excluded, reason class scope: an archaeological dating argument that uses burial songs as a dating instrument and does not treat the lament as a speech register with performers, structure or content types.
- Jouste, Marko (2020), Suonikylän kolttasaamelainen itkuperinne 1900-luvulla (`https://etnomusikologia.journal.fi/article/download/90118/57605`, HTTP 200) — excluded, reason class scope: an ethnographic inventory of one community's twentieth-century repertoire, whose register structure overlaps S978's Karelian/Lithuanian comparative account.
- Kalkun, Andreas (2014), Seto Singing Tradition in Siberia (`https://www.folklore.ee/folklore/vol58/kalkun_oras.pdf`, HTTP 200) — excluded, reason class scope: a song-tradition survey of Seto leelo, not a lament register account; S970 covers the Seto lament proper.
- Kalkun, Andreas (2017), Introducing Setos on Stage (`https://www.folklore.ee/folklore/vol68/kalkun.pdf`, HTTP 200) — excluded, reason class scope: staged Seto song history, not the mourning register.
- Korolëva, Svetlana (2018), Cherdyn funeral laments (`https://press.psu.ru/index.php/philology/article/download/1450/1082`, HTTP 200) — excluded, reason class scope: a Russian-language study of one region's ritual lexicon and the vestka letter-message motif, whose address-to-the-dead facet is already grounded by the Ingrian and Svan rows.
- Lamentations in the Turkish culture and their functions in society, on the example of Kyrgyz (`https://dergipark.org.tr/tr/download/article-file/490587`, HTTP 200) — excluded, reason class scope: a general survey of lament function in one Turkic society, adding no frozen sub-topic the landed rows do not already cover.
- Literary and historical scholarship on written lament named by Crossref (Mourning Becomes Eclectic, 2005; The Ritual Lament in Greek Tradition, 2002; Antiphonal Lament Between Achilles and Briseis, 1997; Thrēnos and Ritual Lament, 2010; Do Brothers Weep?, 2017; 12 Virgilian Matres, 2020; Radegund and Amalfrid in The Wife's Lament, 2021; The Book of Ezekiel and Mesopotamian City Laments, 2011) — excluded, reason class scope: scholarship on written, literary lament, not the sung speech register as a social institution with performers, refrain structure and a design procedure, and no plain full-text OA capture was reachable.
- Generic refrain and formulaic-theory chapters named by Crossref (The Refrain in David's lament over Saul and Jonathan, 1972; Refrain, Oxford Music Online, 2001; A Good Refrain Sells the Song, 2010; A Nuclear Refrain, 2018; Formulaic Language: An Overview, 2010) — excluded, reason class scope: no mourning-lament corpus and no OA capture.
- Literary-historical and law-review treatments named by Crossref (Funeral song poetry, 2025; Servile Mourning for the Powerful, 2023; Comforted But Not Compensated?, 2015; Mourners at Sir Philip Sidney's Funeral, 1941, three records) — excluded, reason class scope: no accessible full text, so not usable for a quote under the ordinary-means rule.
- Non-OA or shell-only records named by OpenAlex (The Funeral Lament as an Anthropopoietical Ritual, 2018; Of Commodified Grief and Emotions, 2025; A Witness to Death, 2015; Keening as a cross-cultural phenomenon, 1993; Pure Corpses, Dangerous Citizens, 2016; Social Support in Perinatal Grief, 2020) — excluded, reason class access: the OA URL returned 403 or a JS-only shell, or the object is not about the lament register, or it is a thesis whose landing page carries no quotable body text.
- The Context and Structure of Funeral Oratory among the Bukusu (2014) — excluded, reason class scope: funeral oratory, not the sung lament register.
- Creative dynamism and religious syncretism in Igbo oral funeral songs (2024) — excluded, reason class scope: Igbo syncretism, not the lament register as such.
- The Therapeutic Dimensions of BaTonga Mourning Songs (2025) — excluded, reason class scope: a therapeutic framing that overlaps S972's clinical framing without adding a distinct frozen sub-topic.
- folklore.ee site search `?s=lament` (1 hit, an unrelated Estonian Parishes article) — excluded, reason class scope: the record's subject is Estonian parishes, not the lament register.

Search method (screening only; every row above was then opened by a direct request to the article page or PDF): the DOAJ open-access article API `https://doaj.org/api/search/articles/<query>?pageSize=25` over twelve queries, the Crossref works API `https://api.crossref.org/works?query.bibliographic=&rows=15` over five queries, the OpenAlex works API `https://api.openalex.org/works?search=&per-page=25` over eight queries, and two folklore.ee site operations (a site search and an index sweep of eleven volumes). The APIs were used as finders; every included record was then fetched at its publisher or OJS URL.

Search-log summary as the scout measured it from the saved API JSON: 27 query operations (25 API plus 2 site); 263 API records returned and screened (DOAJ 42, OpenAlex 161, Crossref 60) plus 2 site-search hits, 265 records screened in all; 12 direct captures staged (11 tier A, 1 tier C); 253 excluded at screening. A candidate may be returned by more than one query, so the per-query included counts sum to more than 12 (20 query-candidate hits resolving to 12 distinct candidates). The API-reported identified counts are the providers' fuzzy-match totals for the whole index, not the size of a relevant set; only the returned page was screened. Stop rationale: a coverage stop, not a volume stop — after 27 query operations and 265 screened records every one of the six frozen sub-topic phrases had at least one tier-A primary capture with a verified single-occurrence quote, so further candidates would have widened the sample without closing an unfilled sub-topic. The gap that remains open in the landed set is a professional-mourner source from a non-European tradition: the scout staged one (S981, the Kenyan Abanyole dirge) but the registry seat landed five rows and did not carry it, so that gap is recorded rather than papered over.

## Mistakes

| id | class | evidence pointer | captured-by | fix |
|---|---|---|---|---|
| R95-M1 | stale-premise | the round-94 mutation manifest's `dispo-fallback` pattern was written against v4 bytes and scored BROKEN-PATTERN against v5 (`/home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-94/mutation-score-lands.txt`, line `MUTANT dispo-fallback-off BROKEN-PATTERN selftest_rc=n/a`); re-measured here: the pattern `            m = DISPO_ANY_RE.search(plain)` occurs once in the v4 bytes and zero times in the v5 bytes, where the fallback moved into `_dispo_match` at eight-space indent | none — no pattern-freshness verification existed | mutants95 verifies every pattern against the target bytes at run start (declared exactly-once / replace-all match counts) before any scoring |
| R95-M2 | vacuous-survivor | the v5 selftest carried no pin for the >= 2-token heading anchor rule, so `head-qualify-off` survived the 88-mutant scoring (same receipt: `MUTANT head-qualify-off SURVIVED selftest_rc=0`); re-measured here: mutating the v5 bytes with that pattern still prints `SELFTEST PASS 126/126` at rc 0, so the mutation is invisible to the v5 selftest | none — no pin exercised the rule | the v6 head-qualify pin (the selftest fails under the mutant) |
| R95-M3 | reference-drift | the SKILL.md `## Gates and probes` registry carries no row for `tools/check-advance-evidence.py` v2–v5: `grep -in advance SKILL.md` returns nothing (rc 1), and the gate-registry auditor lists the tool under `tools_without_rows` while its own instrument set covers only `reports/round-*/accept-*.py` — yet the tool has been the round instrument since round 90 (named in `reports/round-90/claims.json` through `reports/round-94/claims.json`), with grader v2 at round 91, v3 at 92, v4 at 93 and v5 at 94 | the gate-registry auditor is informational only | the L1 lands the v6 registry row this round |
| R95-M4 | coupling defect | four of the five new registry rows open their `teaches` cell with their own anchor quote verbatim (the fifth escapes only because its anchor quote ends in a full stop), so the grader's GATE leg refuses the lesson's own gate line with the named diagnostic `gate quote is the row teaching cell (self-quote)`: measured over a scratch mirror of the staged rows, `LEG FAIL GATE` on four of five rows with both the v5 base bytes and the v6 candidate, and `LEG PASS GATE` with `ENTRY-EVIDENCE: PASS legs=9/9` once the gate lines carry a second span from the same capture (the gate lines in this lesson) | none — the round-95 counter has no entry-mode leg, so nothing in the frozen measurement sees it, and the base registry shows no such collision (0 of its 5 anchor-quote rows) | the L1 decides at landing: either the four teaching cells are reworded so the anchor quote is not their opening, or the landed lesson keeps the second-span gate lines written above |
| R95-M5 | missing deliverable | no round-95 seat staged `reports/round-95/evidence/manifest.json`, the per-row capture/url/http_status/fetched_at/sha256/quote manifest the grader's CAPTURE leg reads; without it the grader refuses the lesson with rc 2 and the named diagnostic `ADVANCE-EVIDENCE_ERROR: unreadable .../reports/round-95/evidence/manifest.json` (measured), and round 94 shipped the same file in its land commit | none — the wave specification names no seat for it | the L1 writes the manifest at landing, as it did for round 94 |
| R95-M7 | grader-input hazard in the lesson text | the grader's verdict-disguise channel reads every lesson line: a line that names a registry id and also carries the word `located` in any case is refused outright with `ADVANCE-EVIDENCE_ERROR: line N: lowercase verdict token outside the anchored rule (VERDICT-LOWERCASE)`, and the refusal aborts the whole entry grade before any leg is scored. Measured by drafting this lesson: the first draft of this row named the affected ids in the same line as that word and the grader refused the draft at line 82 with rc 2 | none — the round-95 counter has no entry-mode leg, and the round-92 to round-94 lessons happen to avoid the shape | the lesson keeps ids and that word on separate lines (this row and R95-M4 were reworded for it); a lesson author should assume every id-bearing line is parsed |
| R95-M6 | reason-not-recorded | the scout staged twelve candidates and the registry seat landed five of them without recording a reason for the seven it dropped, one of them the only non-European professional-mourner source in the set (the Kenyan Abanyole dirge, staged as S981, which the scout counted as closing that gap) | none — the registry seat's report lists the five landed rows and is silent on the other seven | the L1 records the drop reason, or lands the non-European row, at landing |

Each of the three named mistakes is shown able to fail by measurement, not by assertion. R95-M1: the round-94 pattern counts 1 in the v4 bytes and 0 in the v5 bytes, which is the BROKEN-PATTERN condition its own driver enforces. R95-M2: the mutated v5 bytes still print `SELFTEST PASS 126/126` at rc 0, so the rule the mutant removes is unpinned. R95-M3: `grep -in advance SKILL.md` prints nothing while the tool is named in five consecutive claims.json files. R95-M4 and R95-M5 are each reproduced by a command that fails in one shape and passes in the other; the receipts are the grader runs recorded in this seat's report.

## Routed to round 96

- CriticO95's nine surviving new classes against the v6 candidate (the critic's own measurement: `BATTERY-SUMMARY survivors=10 refused=6 unnamed=0 traceback=0`, of which 9 are fresh classes and the tenth is the ZWNJ1 control). Four are splitlines-severing verdict channels — VT1 (U+000B), FF1 (U+000C), LS1 (U+2028) and NEL1 (U+0085) — where `str.splitlines()` in `dispositions()` severs a forged gained `LOCATED` line before APPENDONLY can see it: one mechanism, four codepoints. Two are token-breakers NFKC cannot rejoin, NB1 (NBSP U+00A0, which folds to a space inside the token) and ANSI1 (ESC U+001B + `[31m`). One is CYR1, a Cyrillic small-a U+0430 in place of the id letter, which `_refuse_disguised` never reaches because it gates on `[Ss]\d{3,}` first. Two are heading-token anchors the v6 number-strip does not enumerate, BR1 (`## (1) address`) and DASH1 (`## - address`), where any leading token that is not an ASCII, roman or fullwidth dot-form number still counts as a token. The critic's three smallest safe corrections are recorded with its report.
- The title-only exclusion re-decisions stay open. `corpus/lessons/round-92-verifier-spotcheck.md` §4 and §6 item 1 record three candidates whose exclusion was decided on title or metadata and whose re-opened text disagrees with the gate: Awetí motion events (2015), Zulu Lexikos (2011) and Turkish Signifiances (2020). Nothing in round 93, 94 or 95 re-decided them, and no L0 ANSWER stands on them; the round-92 lesson's criterion-37 sweep cannot retro-fit them.
- The F1 non-numbered variant is covered by behaviour but not by the battery predicate. Measured here against both the v5 base bytes and the v6 candidate: an entry whose h2 headings are content-free is refused on TOPIC with rc 1 and `ENTRY-EVIDENCE: FAIL legs=8/9 failed=TOPIC`, in the numbered form `## 1. alpha` and in the non-numbered form `## alpha beta` alike, so the v6 heading work closes both shapes. What is still open is the predicate, not the tool: the round-95 battery manifest lists fourteen classes (A1, B1, G1, H1, I1, J1, K1, CD1, LR1, TAB1, ID1, NUM1, RM1, NUM2) and no F1 entry, so the round that routed F1 out of round 93 has still not had the battery assert it. Round 96 should add the class rather than leave the coverage implicit.
- The registry's teaching cells and the grader's GATE leg are coupled (R95-M4 above) and the coupling is a row-shape rule, not a wording accident: any new row whose teaching cell opens with its anchor quote makes that anchor quote unusable as a gate quote. Round 96 should fix the rule (a teaching cell that paraphrases rather than quotes) or state the exemption, so the next wave does not rediscover it.
- The lands evidence manifest is still unwritten (R95-M5 above) and the seven staged-but-unlanded candidates still carry no recorded reason (R95-M6 above). Both are L1 landing decisions; neither is a claim failure.
- The freshness pause and the lowest-axis obligation are unchanged and open: `/home/vgpnk/Projects/shokunin/.ufo/l0-questions.md` lines 47 and 303 (round-11 drift-threshold calibration, round-89 live re-verification admissibility) carry no L0 ANSWER, and the round-92 ideophones overlap question at line 356 is still open. The lowest-axis obligation is neither met nor waived.


## L1 integration record (added at landing, 2026-11-05; the seat text above is verbatim)

This section supersedes the stale items in the seat drafts where they disagree with what happened
at integration. Nothing above is rewritten.

1. **Claim O landed green, independently attacked.** The v6 candidate bytes
   `f7981ba2881bff2a49a5c603436caefb90f416e6d6843e8e9cd6a63813ac1fec` are the landed
   `tools/check-advance-evidence.py`. ExecBattery95's v5 red-before
   (`reports/round-95/controls/red-before-v5.txt`) prints the frozen before exactly
   (`BATTERY-SUMMARY survivors=7 unnamed=0 refused=7`, the seven new classes surviving rc 0 on
   9/9 legs, no fixture tuning); ExecMutants95's v5 red-before
   (`reports/round-95/controls/mutation-red-before-v5.txt`) prints `87/95 killed, 1 survived,
   7 broken-pattern` — an honest deviation from the predicted red composition, disclosed by the
   seat: the refreshed dispo-fallback pattern matches v5 once and is killed there, so the stale
   break only shows against the v4 bytes as recorded in R95-M1. ReviewerO95 re-ran all five legs
   itself (PASS 5/5), MutationTester95 re-ran the full set (MATCH, 95/95, hand probes
   kill-direction positive). CriticO95's nine fresh-class survivors are routed below and do not
   touch the frozen predicate.
2. **Claim C landed with the CriticC95 recipes applied before landing** (seven fixes, entry lines
   31, 60, 68, 90, 112, 114, 133, 157, 250 in the landed bytes): the two lullaby-restating
   paragraphs rewritten (F1), the Seremetakis/Maniat footnote attribution named with "a family's"
   dropped and the Greek-context line marked as a report via S971 (F2), the cross-tradition
   "recur" claim reworded as design (F3), the Svan vocative gloss marked design (F4), "classical
   division" reworded (F5), the spliced-quote sentence repaired with the quote byte-identical
   (F6), and the Ó Madagáin description attributed through S973 (F7). Every edited line keeps
   exactly one S-id; no edited line names a registry id and the refusal-channel vocabulary of
   R95-M7 together.
3. **R95-M5 closed:** `reports/round-95/evidence/manifest.json` landed, one row per new
   S-row with url, http_status 200, the capture path, sha256, byte count, the anchor quote, the
   pdf twin and `fetched_at` taken from the scout-stage capture file mtimes (the observed fetch
   instants, 15:26:06-03:00), `as_of` 2026-11-05.
4. **R95-M6 closed with recorded reasons, not new rows:** the seven staged-but-unlanded
   candidates S975-S981 stay out of the registry because the landed entry cites S970-S974 only,
   and CORPUS rule 4 appends no row an admitted entry does not cite; S979 is additionally a
   tier-C lead by the scout's own table (never sole support). Their captures stay in the wave
   stage as evidence; widening the entry's citation set is a later round's act, not a
   mid-landing edit of reviewed bytes.
5. **R95-M7 held:** this record keeps every registry id and the word that triggers the
   lowercase-verdict refusal on separate lines; the grader's entry run over the landed lesson
   and entry (below) is the receipt.
6. **ReviewerC95's wave Report file was not written** (its stage `review.md` and DONE exist and
   carry the full PASS 5/5); the stage file is the artifact of record and its UNMEASURED caveat
   on the search-log counts is dispositioned here: 42+161+60=263 and 263+2=265 hold as
   arithmetic over the scout's stated per-API split; the three addends are ScoutTopic95's own
   measurement of its saved API JSON, the raw JSON bodies were not staged, and that staging gap
   is routed below. MutationTester95's tasking-pointer note (the round-94 lesson has no
   R94-M5 row; the substance sits in its L1 integration record item 3) is confirmed and the
   pointer here is corrected to that item.
7. **Lands receipts** (all under `reports/round-95/controls/` and `reports/round-95/`):
   predispatch lands receipt, selftest, battery, REG diff, mutation score, grader entry run,
   census, index — commands and rc recorded in this round's report.

## Routed to round 96 (integration additions)

- Staging gap: future search-log seats stage the raw API JSON (or its digest file) beside the
  counts so a non-author can re-derive identified/screened without re-querying.
- CriticO95's nine survivors (recipes in its stage `attacks.md`): VT1/FF1/LS1/NEL1
  splitlines-severing channels, NB1 NBSP, ANSI1 ESC, CYR1 homoglyph id gating, BR1 `## (1)`,
  DASH1 `## -`; the seat's "smallest safe corrections for a v7" is the recipe.
- Everything in the seat-draft routed list above stands: the round-96 battery should carry an
  F1 entry; the row-shape rule (teaches cell vs anchor quote) needs a stated rule; the round-92
  title-only re-decisions stay open; freshness and the ideophones overlap stay open at L0.
