# CritEntryQuality — wave-2 falsifier, round 77

Seat item: the rewritten entry `.ufo/waves/round-77/w1/drafts/corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md` (123 lines; all line numbers below are that file, tag 74E4). Attacked against `corpus/QUALITY.md` criteria 1–29 and `PROVINCE.md`. Evidence texts: `.ufo/waves/round-77/w1/stage/ScribeEntryA/d1-live.text` (D1, sha256 f14f7a5c…) and `d2-live.text` (D2 pdftotext -layout, live PDF sha256 5d1bfa5a…), `stage/ScoutDocS897|898/evidence.txt`, `stage/ScribeEntryA/fetch-log.txt|spancheck.txt`, `stage/RevQualityFit-2/`. Base read at 211f9526800906e0c585d878d265c37e5e090c15.

Result: **not clean** — one HIGH internal contradiction (plain-client access), and four MEDIUM content defects (dehyphenated "Xingshi" span not verbatim-locatable + false "one span" count; two false locators; inverted subcategory; misstratified suffix channel). Plus LOW items. No installs; no fixtures needed; read-only.

## HIGH

**H1 — line 6 asserts "Both documents answered HTTP 200 to a plain client"; the file's own records and every fetch log say D1 answered 403 to the plain client.**
- Draft :6: "Both documents answered HTTP 200 to a plain client on 2026-10-27".
- Draft :8 and :111 define "the plain client" as `curl/8.7.1` and record it answering the D1 URL **HTTP 403, 162 bytes**. `stage/ScribeEntryA/fetch-log.txt` (UA curl/8.7.1 → HTTP 403, 162 B, wall present; browser-shaped UA → 200, 143252 B) and `stage/RevQualityFit-2/fetch-log.txt` step 3 agree.
- Within the file's own terminology "plain client" = curl/8.7.1 (":8 the plain client `curl/8.7.1`"). So :6 is false for D1; the only access path is the browser-shaped UA. A re-checker following :6 will hit a 403 wall it says cannot happen. QUALITY 1 (claim false on the artifact it describes) and the access-record spirit of 10/22. Fix: "D1 answered a browser-shaped UA (plain curl got a UA-gated 403); D2 answered HTTP 200 to plain curl."
- Related cosmetic inconsistency at :6: it cites Wayback capture `20251231111748` for D2, while :4 and :113 correctly promote `20260901045105` (byte-identical to live). Not false, but the line already fails on the UA clause.

## MEDIUM

**M1 — line 53's quoted span is not verbatim-locatable, and line 115's "the one span that crosses a line break" is false for two further spans.**
- Draft :53 quotes 「the 17 terms/characters listed in “Xingshi” as those of the highest occurrences」. `d2-live.text:205-206` has `"Xing-\nshi"` (hyphen-broken). Command: `tr '\n' ' ' < d2-live.text | grep -c -F 'the 17 terms/characters listed in “Xingshi” as those of the highest occurrences'` prints **0** (the file's own flattening method fails on the joined hyphen; only the dehyphenated rewrite locates). Under the file's own recheck rule (:6, "a span that stops locating marks its sentence unverifiable") this span is not locatable verbatim.
- Draft :115 claims "the one span that crosses a line break" is the 88-term count. Also crossing line breaks: (a) :55's second span 「given names with lexemes denoting plants and trees」 — `d2-live.text:167-168` has `lexemes\ndenoting`; (b) :53's span above; (c) :55's first span 「standard given names with lexemes reflecting feminine softness」 — `d2-live.text:167` has `softness and\nfemale` (the quote is a truncation *inside* the break's first line, so it locates, but the fuller class name is elided mid-break). The statement "every span quoted above was chosen to sit inside one line" is false for two spans and the "one span" count is wrong.
- Note the W1 span table (`spancheck.txt`) only probed the safe prefix "the 17 terms/characters listed in" — the dehyphenation defect is exactly what that truncation hid.

**M2 — line 53 locator "the lead-in paragraph of §4" is false; the paragraph is the closing paragraph of §3.**
- `d2-live.text`: §3 heading at :171 (p. 114/115); the 17-terms sentence at :205 sits in §3's last paragraph (p. 115); §4 heading "4. LIST OF THE 17 MOST COMMON LEXEMES…" is at :247 (p. 116, matching the draft's own page note). The paragraph *introduces* the list but is a §3 paragraph; a reviewer opening §4 finds a lexeme table, not the quoted sentence. Fix: "final paragraph of §3, printed p. 115".

**M3 — line 39 locator "the closing paragraph of 一、單名與雙名" is false.**
- `d1-live.text`: §一 spans :289–:634 (§二 heading at :634). The quote 「普通民眾所受影響並不明顯，仍然是單名、雙名並存」 (:608) ends a paragraph; two further §一 paragraphs follow — the 新疆拜城/西晉鎮墓文 paragraph and the closing "回到本節開始提出的問題" paragraph. Fix: "§一, paragraph before the 拜城 digression" or "antepenultimate paragraph of §一".

**M4 — line 55 inverts category and subcategory, and truncates the class label.**
- D2 :166-168: "such names may be classified as 'standard given names with lexemes reflecting feminine softness and female aesthetic values,' **and belong to the subcategory** 'given names with lexemes denoting plants and trees.'" The page calls the *softness* label the classification and the *plants-and-trees* label the subcategory. Draft :55: "The class the lexemes belong to is the field's own subcategory label: 「standard given names with lexemes reflecting feminine softness」 … where the subcategory is named as 「given names with lexemes denoting plants and trees」" — it applies "subcategory" to the softness label and then correctly names the real subcategory, contradicting itself in one line and inverting the source's hierarchy. The quote also drops "and female aesthetic values" from the class name without marking the truncation.

**M5 — line 43 and the Lever-1 table misstratify the 子/兒-suffixed double names as an elite reform.**
- Draft :43: "the new double names are built from 之 and 道 and from 子- and 兒-suffixes (S897)"; table :75: "extra given element (suffixed or prefixed) … upper stratum first … internal reform from above".
- `d1-live.text:1506` context: the elite break is 之/道 信仰性虛字 over single names; **after** the convention broke, 「屬吏階層也擺脫了單名影響，大量『子』尾、『兒』尾等帶有口語特徵的人名浮出水面」 — the 子尾/兒尾 names are *colloquial petty-official-stratum* names surfacing, and the paragraph closes 「精英文化會吸納民間文化的某些因素」 — folk→elite direction, opposite of "internal reform from above". The draft's own sentence "reaches the register later" half-marks this, but the design table hard-codes the elite-first channel for the suffix class the article assigns to 小傳統. QUALITY 1/6: misattributes the source's direction of flow.

## LOW

- **L1 — :103/:13 tier A for the 17-lexeme list is asymmetric with tier B for the 88-term count.** Both numbers are reported from a third party (Kałużyńska 2008; "Xingshi" 姓氏人名用字分析统计 1991 over the 1982 census). :13 grants A "for the 17-lexeme list it presents" while B-ing the 88 count because it "reports" it — but the article presents the 17 list from "Xingshi" exactly the same way (tier A properly covers only the article's *selection and comparison*). Defensible if A is read as "primary for the selection", flag-worthy as a consistent-grader reading of QUALITY 6.
- **L2 — :91 carries five factual numbers with no S-id.** "counted at 88 members … top 17 … 6 have vanished, 2 rose on homophony, 9 fell" — all sourced facts (S898); criterion 15's one-id-per-cited-line and criterion 1's checkable-source rule point at one `(S898)`. Other uncited lines (:93 pipeline insertions; :107 correction-note) are design/meta statements, so this is a single-line gap. LOW because every cited load-bearing line does carry exactly one S-id (mechanical check below).
- **L3 — :10/:11 ground slightly overstates base absence.** "never treats a given-name lexicon as something that can be counted" / "no entry states that a name inventory has a size" — base `naming-systems.md:61` counts the state-curated name-character inventory (Jōyō 2,136 / jinmeiyō 863–864). The objects differ (allowed-character register vs. lexeme inventory), so the claim survives narrowly, but the sentence as written is falsifiable against the base file it names.
- **L4 — :3 names the serving institute 中國社會科學院古代史研究所 while the page `<title>` (:1) says 历史研究所.** Both strings appear on the page (footer copyright :tail "版权所有： 中国社会科学院古代史研究所"); the draft's choice matches the current name, CLAIMS-DRAFT's matches the title tag. Ambiguity only.
- **L5 — :61 page note for the homophone explanation** is on printed p. 122 (`d2-live.text` after the p. 122 folio at :491), while the lead quote is p. 121. :4's "§3 (printed p. 114) for … the sample it is drawn from" is loose: the sample figures sit on p. 115 (§3 spans 114–115). Locator imprecision, not falsity.

## Verified clean (evidence, so a counter-seat cannot re-raise)

- **Criterion 15 lint:** `python3 -B tools/check-cited-lines.py <draft>` → `CITED-LINES: 0 finding(s)`, exit 0. Every factual line carries exactly one S-id; only S897/S898 appear (13×/10×); all staged legacy ids S886/S888-S891/S896 are purged (grep for `S[0-9]{3}` minus S897/S898 → nothing). The MULTI-ID findings in `RevQualityFit-2/lint-staged.txt` were against the staged ancestor, correctly removed.
- **All ten D1 quotes locate verbatim** in `d1-live.text` (`grep -n -F` hits at :240,242,252,635,1466,1466,1478,608,1475,1506), and all D2 quotes locate except the two break-crossing spans in M1 (the second locates under whitespace-fold; the "Xingshi" one does not). Word/char counts re-derived: 23 chars (:23), 17 words (:47), 10 (:49), 9 (:51), 12 (:53), 8 (:55), 7 (:59), 11 (:61) — all correct.
- **Tier/UA binding:** :7, :8, :111 correctly bind each UA to its response (403/162 B curl; 200/143252 B browser UA; 200/417093 B PDF) per criterion 22 — the defect is confined to :6.
- **Wayback/CDX numbers** (:113): 41,417 / 406,446 / 426,128 compressed bytes match the CDX `length` column in `fetch-log.txt`; sha256s match both evidence headers; 20260901045105 byte-identical claim verified by ScoutDocS898 (`5d1bfa5a…` both sides).
- **Section attribution:** :29's quote is §二's opening sentence (:634-635); :33,:35,:37,:41,:43 all sit inside §四 (:1456+); :23,:25,:27 in the unnumbered lead before §一 — consistent with `ScoutDocS897`'s "no literal 引言 heading" note.
- **Tier scoping elsewhere:** :13 B-for-S897 (reprint, section-heading locators) is honest and matches criterion 6; calibration table (:97-107) names status per claim (criterion 2); :107 explicitly refuses to correct the base's "~ancient" surname row rather than overclaiming — good calibration.
- **Couples (criterion 3):** `naming-systems.md` (§2 slot table at base :44-63, §7 pipeline steps 2 "Slot inventory & order" and 4 "Lexify" verified at :112-115 — :93's 2a/4a insertions name real steps), `toponymy-place-names.md`, `semantic-fields-lexicon-building.md` all exist at base.
- **Usability (4):** two decision tables + three-question checks — qualifies.
- **Canon hygiene (5) / PROVINCE:** :15,:67,:91,:123 all end at handoff; lore-shokunin named canon owner, matching PROVINCE's refusal clause; content is naming systems — owned domain.
- **Registry resolution:** base SOURCES.md ends at S896 (`git show <base>:corpus/SOURCES.md` rows through :851); S897/S898 are this round's planned rows — IDs free, doc map S897→D1, S898→D2 agrees with `ExecAdaptC`'s staged map (S897←S897, S898←S903).
- **Attribution:** :47's 88-term quote keeps "According to Kałużyńska (2008…)" inside the quotation and :103 downgrades it to tier B — the r76 misdescription class is handled correctly here (orthogonal to CritAttribution's wording attack).

## Smallest safe corrections

1. :6 — replace "Both documents answered HTTP 200 to a plain client" with the per-UA truth (:8's own wording), and drop or correctly attribute the 20251231111748 capture.
2. :53 — quote `the 17 terms/characters listed in “Xing- shi”` folded as 「the 17 terms/characters listed in “Xingshi”」 *with* the dehyphenation stated, and fix the locator to "§3 closing paragraph, p. 115".
3. :115 — "every span … inside one line" → name all break-crossing spans (88-count; plants-and-trees subcategory; Xingshi) or re-quote within-line spans.
4. :39 — "the closing paragraph of" → a locator matching :608's real position.
5. :55 — swap so the subcategory label is the plants-and-trees phrase; mark the elided "and female aesthetic values".
6. :43/:75 — route 子尾/兒尾 through the folk/petty-official channel (bottom-up absorption), or quote only 之/道 for the elite break.
7. :91 — append `(S898)`; consider :103's A→B if the grader rules symmetry.
