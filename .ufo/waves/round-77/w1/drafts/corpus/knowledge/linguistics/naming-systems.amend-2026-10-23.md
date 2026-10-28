# Amendment — a naming system acquired rather than given, and a name lexicon that is finite and dated

- source: S897 — 魏斌〈單名與雙名：漢晉南方人名的變遷及其意義〉, 《歷史研究》2012 年第 1 期, served as a reprint by 中國社會科學院古代史研究所 (posted 2021-03-16; the page's own closing line reads 來源：《歷史研究》2012 年第 1 期) — http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml — the opening paragraphs before the heading 一、單名與雙名, which carry 「名的使用要早于姓」 and 「春秋戰國以降…華夏式姓名習慣」; the closing paragraph of 一、單名與雙名 for 「單名、雙名並存」; 四、結語 for the stratified-acquisition, 大傳統/小傳統 and 邊緣的強化 passages — fetched 2026-10-27
- source: S898 — Kałużyńska, I. (2025), "Flowers, Plants, and Trees in Female Naming in China", *Onomastica* LXIX, PL ISSN 0078-4648, DOI 10.17651/ONOMAST.69.7 — https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/ (same-page Wayback capture 20260901045105 is byte-identical to the live response) — §2 (printed p. 114) for the subcategory label, §3 (printed p. 114) for the 88-term count and the sample it is drawn from, §4 lead-in (printed p. 115) and its list heading (printed p. 116) for the 17 lexemes, §5 Conclusions (printed pp. 121–122) for the frequency comparison — fetched 2026-10-27
- verified-at: 2026-10-27
- recheck: 180d — re-open both rows by the two requests below and re-locate every span quoted in this file; a span that stops locating marks its sentence unverifiable, and the sentence is cut rather than softened. Both documents answered HTTP 200 to a plain client on 2026-10-27, and both are also held by the Wayback Machine on the same URLs (captures 20240111092427 for the first, 20251231111748 for the second, status 200 each), so a later live failure leaves a same-page capture to re-open.
- recheck detail (S897): `curl -sS -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml | grep -c -F '名的使用要早于姓，兩者組合是一種後起的文化習慣'` printed 1 on 2026-10-27, with the same request answering HTTP 200 and 143,252 bytes.
- recheck detail (S897): the plain client `curl/8.7.1` answered the same URL with HTTP 403 and 162 bytes on 2026-10-27, so the refusal is User-Agent-gated rather than a property of the document; the page is open under the browser-shaped User-Agent and its full text is what the greps above read.
- recheck detail (S898): `curl -sS -o onom69.pdf -w '%{http_code} %{size_download}\n' https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/` printed `200 417093` on 2026-10-27, and `pdftotext -layout onom69.pdf - | tr '\n' ' ' | grep -o -F 'According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees' | wc -l` printed 1; the archived capture of the same URL was fetched on the same day and returned the same PDF text layer, its two quoted spans locating there too.
- ground: the base entry `linguistics/naming-systems.md` holds the slot inventory (§2) and Chinese name taboo (§6) but never says when the surname and the given name fused, never says the fusion spread by contact, and never treats a given-name lexicon as something that can be counted. Rounds 2 and 3 added scholarship about Chinese names from psychology and from the wider onomastics field; neither added a Chinese-language system-level account, and no entry states that a name inventory has a size. Negative sweep scope is corpus/knowledge only: no file under it carries a system-level account of 姓/名 succession or a counted Chinese name lexicon.
- topic: two things the base entry could not say — that a Chinese naming system is a *late acquisition* rather than a given (名 precedes 姓, the pairing is a contact-era habit, and the acquisition ran on two different channels at two different speeds), and that the given-name lexicon is a *finite, countable, dated inventory* (a fixed number of lexemes, a frequency ranked subset, and a measurable shift across two samples forty years apart).
- gap filled: the base can describe the slots a name system has and what a bureaucracy does to names it forbids. It could not say that the slots arrived one at a time, that their arrival was stratified, or that a name lexicon has a size and a date. This amendment supplies the structure claim, the acquisition-timing claim, and the inventory claim, and stops there.
- sources: the two rows above. The first is a peer-reviewed Chinese-language article read in the original from an institutional reprint (tier B for the claims used here: its periodization of 姓/名 is its own argument, and its page is a reprint, so printed page numbers are not available and locators are section headings). The second is a peer-reviewed English-language article in the field's own journal, open in full as a PDF (tier A for the 17-lexeme list it presents and the frequency comparison it runs; tier B for the 88-term figure, which it reports from the author's own 2008 monograph and does not re-count).
- couples: `linguistics/naming-systems.md` (the entry this amends — its §2 slot table gains a fusion date and an acquisition channel; its §7 pipeline gains steps 2a and 4a, below); `linguistics/toponymy-place-names.md` (the place-name half of the same onomastic surface: it owns element grammar for names of places, this file owns the person-name inventory beside it); `linguistics/semantic-fields-lexicon-building.md` (a name lexicon is a semantic field with a counted membership, which is that entry's apparatus).
- scope: an amendment to the naming entry. It records how one naming system is structured, how it was acquired, and how its inventory can be specified and dated; it decides no world's names and sets no canon.

## 1. What the two documents add, and what they do not

The first document is a study of single- and double-character given names in Han–Jin southern China, and its opening paragraphs are where it states the structure it is working inside. The second is a study of one lexeme class inside Chinese female given names, and it is where the inventory claim is made countable. Neither document is a general theory of naming; both are used here for the one claim each makes and verifies on its own pages.

## 2. The system is acquired, not given

The article separates the two slots before it studies either of them: 「名的使用要早于姓，兩者組合是一種後起的文化習慣」 — 23 characters including the comma, opening paragraphs (S897). The given name is the older institution; the pair is the later habit. A worldbuilder who starts from "a person has a surname and a given name" has started from the end of a process.

It then dates the pairing in the Central Plains, and the date is a period rather than an event: 「春秋戰國以降中原地區逐漸形成穩定的華夏式姓名習慣」 — opening paragraphs, where the pattern the page names is 姓（氏）＋名 (S897). The fusion is datable, and it is a habit that stabilised, which is a different design object from a rule that was decreed.

The mechanism it gives for the spread is contact, not descent: 「在華夏國家向周邊擴展其勢力的過程中，這種文化標籤也會隨之擴散到周邊地帶」 — opening paragraphs (S897). The name pattern travels with the polity that carries it, and the article is explicit that this is a label rather than a genealogy.

What acceptance means on the receiving side is stated without hedging: 「南方地區華夏式姓名的使用是文化接觸的結果」 — the opening sentence of 二、漢代南方人名的變化與單名問題 (S897). A name system can therefore be an import, and the import has a date and a direction.

## 3. Acquisition is stratified, and the strata leave different records

The article's conclusion separates the channels rather than averaging them. The first channel is elite and early: 「上層人群在與華夏國家的接觸中，較早的模仿或被賜予華夏式人名」 — 四、結語, where the page adds that the acquisition served both communication and the display of authority (S897). A borrowed name is a claim to standing before it is a convenience.

The second channel is administrative and later: 「下層人群華夏式人名的大規模實現，則與編戶化過程密切相關」 — 四、結語 (S897). The mass acquisition of the imported pattern runs through registration, which is why the register is where a world's naming history is legible.

The article names the resulting split in the terms the corpus already uses for elite and popular culture: 「人名背後其實是精英文化與民間文化」 — 四、結語, where the two are 大傳統 and 小傳統 (S897). The two traditions do not acquire the same slots at the same time, which is the whole design content of this section.

What the popular tradition does with the given-name count is concrete: 「普通民眾所受影響並不明顯，仍然是單名、雙名並存」 — the closing paragraph of 一、單名與雙名 (S897). One character or two is a live variable among commoners while the elite runs a single-character norm.

The article's most portable structural finding is about the margin: 「邊緣的強化」 — 四、結語, its own coinage for a core that pushes a tidier rule onto its periphery than it enforces at home (S897). A worldbuilder gets a free asymmetry: the frontier can be more orthodox than the capital.

And the norm breaks from above: 「晉宋之際，上層社會的單名慣例開始被突破」 — 四、結語, where the break is dated to the Jin–Song transition and the new double names are built from 之 and 道 and from 子- and 兒-suffixes (S897). A naming reform is an elite event that reaches the register later.

## 4. The inventory is finite

The second document counts rather than illustrates. Its count of the plant, flower and tree lexemes in female naming is 「According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees」 — 17 words, §3, printed p. 114, and the attribution stays inside the quotation because the page is reporting a count rather than making one (S898). The page does not re-count it, which is the grade this file uses it at.

The page scopes that number twice in the same sentence, and both scopes matter: it is the research material of that monograph, and within it 「among the names of women figuring in the research material」 — 10 words, §3, printed p. 114 (S898). Eighty-eight is a count inside a corpus, not a claim that Chinese has eighty-eight plant words.

The sample behind the frequency work is stated, which is what makes the inventory checkable rather than asserted: 「2,500 characters occurred in the names of 85,567 females」 — 9 words, §3, printed p. 115, over names the page dates to people born approximately 1900–1980 (S898). An inventory with a sample size and a birth cohort is an instrument; one without them is a list.

The list the article actually works through is a frequency cut of that inventory: the 17 lexemes are 「the 17 terms/characters listed in “Xingshi” as those of the highest occurrences」 — 12 words, the lead-in paragraph of §4, printed p. 115 (the §4 heading itself is on p. 116) (S898). Seventeen of eighty-eight is the ranking rule, and the article names the source volume (《姓氏人名用字分析统计》, 语文出版社, 1991) and the census behind it (PRC, 1982).

The class the lexemes belong to is the field's own subcategory label, not this file's invention: 「standard given names with lexemes reflecting feminine softness」 — 8 words, §2, printed p. 114, where the subcategory is named as 「given names with lexemes denoting plants and trees」 (S898). A worldbuilder can borrow the label and must then earn it with the same kind of counted sample.

## 5. The inventory is dated, not eternal

The comparison the article runs is the part that makes the inventory a design instrument. Against an internet list of the top 150 characters for roughly 2020–2024, 「Six of these seventeen terms are absent」 — 7 words, §5, printed p. 121, and the page names them: 花, 林, 芹, 茹, 杏, 树 (S898). A lexeme can fall out of use inside one working lifetime.

The rest of the movement is stated as a count: 「The frequency position of the other 9 terms is now lower」 — 11 words, §5, printed p. 122, with two terms (桂, 蓉) rising because they are homophones of auspicious words rather than because of their plant meaning (S898). Frequency is not a property of a lexeme; it is a property of a lexeme at a date, and homophony can move it independently.

The article's own explanation is a change in naming preference rather than in language: the shift is attributed to more unisex naming and to avoiding overt sex stereotyping (S898). That is the second design lever this file takes from the page: a name inventory changes for social reasons that a lexicon table can record but cannot predict.

## 6. Design levers for a worldbuilder

Two levers, each a sheet to fill rather than a rule to obey. The first is acquisition timing; the second is the lexicon as a tabulated inventory. Both are stated as questions, so a draft can be checked against them.

**Lever 1 — the acquisition schedule.** Ask when each slot arrived, who got it first, and through which channel. Fill one row per slot per stratum.

| Slot | Arrival date | First holders | Channel | Later holders | What the late stratum does |
|---|---|---|---|---|---|
| given name | earliest; no pairing required | everyone | inherited practice | — | keeps older single/double variation |
| surname, fused to given | a datable period of stabilisation | upper stratum, by imitation or bestowal | contact with a prestige polity | lower stratum, later | keeps the unfused or variable form until the register reaches it |
| extra given element (suffixed or prefixed) | later still | upper stratum first | internal reform from above | diffuse, unevenly | absorbs the new form only after the elite has moved on |

Check a draft against this table by asking three questions: does every slot have a date, does each date have a channel, and does any stratum hold a slot it could not have acquired by its stated channel? A draft that answers "everyone has a surname" has erased the process the table is for.

**Lever 2 — the name-lexicon inventory sheet.** A name lexicon becomes checkable when it is tabulated with a count, a rank and a date. Fill one row per lexeme class.

| Column | What goes in it | Why the column exists |
|---|---|---|
| lexeme class | the semantic class the root is drawn from (plant, virtue, office, animal, place) | makes "does this name fit" a lookup rather than an argument |
| members counted | the number of distinct lexemes in your sample | forces the inventory to have a size, as the studied corpus has 88 |
| frequency rank | rank within the sample, with the sample's size | separates a lexeme that is possible from one that is common |
| cultural reading | what the class is taken to say about its bearer | records the reading as a dated belief, not as a meaning |
| sample date and population | when the names were borne or recorded, and whose names they are | lets a later table be compared with this one |

Check a draft by two questions: can two names be compared on the sheet without appealing to taste, and does the sheet state which population and which decade it describes? A lexicon with no sample date cannot be dated later, and an inventory with no member count cannot be shown to be finite.

The worked shape, using the two documents' own numbers and deciding nothing about any world: a culture's plant-class given-name lexicon is counted at 88 members in one corpus, ranked, and the top 17 re-checked against a second sample forty years later; 6 have vanished, 2 rose on homophony, 9 fell. That is one complete cycle of the instrument — count, rank, re-date — and it is repeatable for any class in any invented language, provided the second sample is stated as a second sample.

What the base entry's pipeline should gain from this, without restating its steps: after its step 2 (slot inventory and order) insert a step 2a that dates the fusion of lineage and given slots and names each stratum's acquisition channel; after its step 4 (lexify) insert a step 4a that counts the lexicon's members, ranks them, and records the sample's date and population. Both insertions are the same two levers, placed where the pipeline already asks the neighbouring question.

## 7. Calibration

| Claim | Status | Why |
|---|---|---|
| 名 precedes 姓, and the pair is a later cultural habit | mainstream within the article's argument, asserted as background | the page states it as the premise of its own study and cites a classical tag; it offers no comparative survey, so the file does not treat it as a cross-cultural law |
| The stable 姓（氏）＋名 pattern formed from the 春秋戰國 period in the Central Plains | the article's own periodization, consistent with standard accounts | one historian's dating on one page; usable as a date, not as a consensus date |
| The pattern spread to the south by contact | the article's conclusion from its own corpus | it is what the article argues from the southern documents, not a sampled result |
| Acquisition was stratified (elite early, register later) | the article's conclusion | stated as its finding on its own material; the file uses it as a design lever rather than as a law |
| 88 plant, flower and tree lexemes | tier B: reported from the author's 2008 monograph, not re-counted on this page | the number is scoped to that monograph's corpus; cited at that grade |
| The top 17 lexemes among the top 150 female-name characters | tier A for the list as presented | presented with rank, count and percentage per lexeme from a named 1991 statistical volume over a 1982 census sample |
| The inventory's frequency shifted between the two samples | indicative, not a measured trend | the two samples differ in population, in source and in collection method (a census-derived statistical volume against a commercial naming website's list) |
| A name lexicon is a countable inventory | the method both documents use, not a finding either states | the file adopts it as a design method, and says so |
| The base entry's Chinese row dates a hereditary surname "~ancient" | not corrected here | the article dates the pairing of the two slots (春秋戰國 onward, Central Plains) and says nothing about when either slot first appeared, so this file adds a fusion date and leaves the base's surname date standing, marked as undated by anything read here |

## 8. Provenance limits

Both documents were opened on 2026-10-27 by plain requests with no automation, no CAPTCHA and no account. The Chinese article's reprint URL answered HTTP 200 and 143,252 bytes to the browser-shaped User-Agent `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`, and HTTP 403 and 162 bytes to `curl/8.7.1`; the refusal is User-Agent-gated, so the document is open by ordinary means and no wall is recorded against it. The onomastics PDF answered HTTP 200 and 417,093 bytes to `curl/8.7.1` with no challenge.

Same-page captures exist for both and were each fetched and read on 2026-10-27: the Wayback Machine holds capture 20240111092427 of the reprint URL (text/html, status 200, 41,417 compressed bytes; fetched body 143,457 bytes) and captures 20260901045105 and 20251231111748 of the PDF URL (application/pdf, status 200, 406,446 and 426,128 compressed bytes). The capture's embedded original URL is the live URL in both cases. Capture 20260901045105 is byte-identical to the live PDF — both are 417,093 bytes with sha256 5d1bfa5a5f01bee68e090155ed683d848e6f75dbc456b8b631be81c1fa8d29bc — so it is the capture the row should pair with the live URL; 20251231111748 is an earlier OJS regeneration of the same article (546,440 bytes on the wire, sha256 1b4c60f2d1ba56cde6e1209d610f00f4899234416fdf7c64bcf14be43b8a2ff9) whose text layer locates every span below unchanged. Every span quoted in this file was re-located in the capture's own text as well as in the live response; a span present in one and absent from the other would have been reported here rather than used.

Two limits belong to the material rather than to the access. First, the Chinese article is served as a reprint page with no printed page numbers, so every locator above is a section heading on the served page, not a journal page; a reviewer checking a quotation must match the heading, not a page. Second, the PDF's text layer is born-digital but breaks words across lines and hyphenates 姓氏 in the list's title; every span quoted above was chosen to sit inside one line, and the one span that crosses a line break — the 88-term count, which the page itself attributes to the author's 2008 monograph — is quoted as a flattened string with its recheck command given above, attribution included.

## 9. Superseded passage note

The staged file this amendment is adapted from folds a second, earlier entry into its own bytes: a round-3 amendment on the professional Japanese reference layer, the terminology of 苗字 against 姓, and the onomastics literature about Chinese names, carried there as a "Superseded passage — retained as the dated record" section. That fold is **not** carried into this lane file, and the reason is a rule rather than a preference. This round's claim admits one entry citing the rows it mined; the round-3 text cites six rows of an earlier round, sharpened only by its own staged row ids in the second block, and reproducing them here would make this entry cite rows no round-77 command can check. The round-3 material is therefore left where it lives — in the staged corpus and in the lane's source registry — and is not re-cited, restated or superseded by this file. Nothing in §1–§8 depends on it.

## 10. Handoff

This amendment appends to `linguistics/naming-systems.md`, which points here through its `couples:` line. It hands over: a dated acquisition schedule for the surname–given-name fusion, a stratified account of who acquired the pattern first and by which channel, a counted and dated name-lexicon sheet, and the two pipeline insertions (2a and 4a) that put both levers where the base entry already asks the neighbouring question. It records method and orders design checks. Which culture's names these levers are applied to, which lexemes a given world's lexicon actually holds, and what a name does metaphysically in a world remain canon decisions owned by lore-shokunin through the world-bible integration contract, and this file decides none of them.
