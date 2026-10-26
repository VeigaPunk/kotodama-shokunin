# Amendment — what the classifications say, and what the classroom study did

- source: S878 — https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955 — Abstract, p. 455; §"Correlation between types of constructed languages, purposes of their creation and linguistic features", pp. 458–460; Conclusion, pp. 465–466 — fetched 2026-10-25
- source: S879 — https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike — the comparison section (served heading: «сОпОсТАВЛЕНИЕ КЛАссИФИКАцИИ д. питерсона с типологиями современных отечественных ЛИНГВИсТОВ», case-mangled by the site's text layer), numbered items 1–2.2 — fetched 2026-10-25
- source: S880 — https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf — §3 "These papers", p. 5 — fetched 2026-10-25
- verified-at: 2026-10-25
- recheck: 180d — re-open each of the three rows above and re-locate its quoted span with the one grep per row on the next three lines (each printed 1 on 2026-10-25); each fetch line (URL, browser-shaped UA, bytes, sha256) is in `reports/round-73/evidence/`
- recheck detail (S878): `pdftotext -enc UTF-8 <pdf> - | grep -c 'this division should be seen as a scale'`
- recheck detail (S879): `grep -c '2.2. Personal languages'` over the served page text with tags stripped
- recheck detail (S880): `pdftotext -enc UTF-8 <pdf> - | tr '\n' ' ' | grep -c 'multi-part, creative project'`

- ground: the base entry `linguistics/conlang-scholarship.md` rests on two source rows — one article's abstract and one monograph, whose own classification it reports — so it can name that a peer-reviewed Russian-language and an English-language literature exist but cannot say what a review article makes of that classification, and it holds no row for a peer-reviewed Russian-language treatment of conlangs or for any account of a conlang-construction course. This amendment adds those three documents; it does not restate the base's topic, gap, or §2–§5.
- topic: the content behind the classification the base could only name — purpose-first typologies in Russian- and English-language scholarship, the a priori/a posteriori dichotomy argued down to a scale, and the design of one conlang-construction course as a companion article reports it.
- gap filled: the base could say a taxonomy of artificial languages exists and that peer-reviewed venues exist. It reports one monograph's taxonomy but could not say how a later review restates and compares taxonomies, what a peer-reviewed Russian-language article does with the a priori / a posteriori dichotomy, or what a construction exercise actually consisted of. This amendment supplies those three, and — the useful negative — the one element the companion article does *not* carry.
- sources: the three rows above, all tier B (English, Russian, English). The Sowers-Wills article that S880 describes has no row here: the Cambridge page answered HTTP 429 to both a browser-shaped and a plain client on 2026-10-25, and its abstract record, reached through Crossref (`https://api.crossref.org/works/10.1017/cnj.2024.21`, HTTP 200), was not adopted as a registry row this round (lesson Gate, Sowers-Wills row), so this amendment cites the companion article S880 only for what the study consisted of and states no duration and no claim about the study's own argument.
- couples: `linguistics/conlang-scholarship.md` (the base this amends); `linguistics/conlang-methodology.md` (the craft pipeline whose Stage 1–2 choices the scale argument bears on); `linguistics/naming-systems.md` (names are a language's first public surface).
- scope: an amendment to the conlang-scholarship entry. It records what three documents argue and what one of them reports about a course; it decides no world's language and adds no canon.

## 1. The structural dichotomy is argued down to a scale

Novikov's article states its method in the abstract: "the author examines the existing classifications of constructed languages and attempts to establish a connection between purposes of their creation and their linguistic features" — 24 words, Abstract, p. 455 (S878).

The dichotomy he works against is the a priori / a posteriori split: the article names the definitions of a priori and a posteriori languages within "One of the most important classifications of constructed languages" (p. 458) and then argues the split should be read as a scale (S878).

He argues, hedged as "it may be argued that", that "this division should be seen as a scale rather than a binary system", because every a priori language carries its creator's linguistic worldview — Balaibalan, conventionally a priori, leans on natural languages more than SolReSol does, which in turn sits differently from aUI (S878).

On the pragmatic axis he adopts Halley's split into interlangs and artlangs, and places under the interlang side the zonal languages (Križanić's Common Slavonic) and, at the highest degree of a posteriority, the controlled natural languages — e.g. Basic English, Globish, E-Prime (S878).

The artlang side is one category whose members range widely: the Star Wars universe features 68 languages, none with any formal description or consistency, while Klingon served as one of Wikipedia's official languages until that was abolished (S878).

His conclusion generalizes the move: the findings "challenge the integrity of the seemingly well-established dichotomies of a priori and a posteriori, auxiliary and artistic languages" — 18 words, Conclusion, p. 465 (S878).

Calibration: the scale reading is the article's own argument against a split the article itself lists among the most important classifications — a contested refinement, not a replacement, and the entry cites it as one author's position (S878).

The Eurocentrism finding is the article's own hypothesis-test, not a survey result: Standard Average European features appear even in a priori languages, because the creator's linguistic worldview cannot be fully escaped (S878).

## 2. Three typologies in a Russian-language review, and one reviewer's comparison

Шувалова and Сидорова's classes are in the base (§3); the 2023 review restates them as "1. Auxlangs. Вспомогательные языки", "2. Вымышленные языки (ВЯ) в широком смысле" (2.1 Artlangs, split into 2.1.1 languages that left their fiction and 2.1.2 languages that function, or are merely mentioned, only inside the work — Arëndron) and "2.2. Personal languages", so the classes gain a second, peer-reviewed voice rather than new members; the served page renders the game language of 2.1.1 as Э'П where the monograph prints D'ni (S879).

For the personal languages the article reports that their researchers propose the label «авторскими языками», author languages; its table carries that label in the Шувалова/Сидорова column (S879).

Piperski (2017) offers a three-way split instead: philosophical or logical languages (loglan, lojban), international auxiliary languages, and artistic languages (S879).

Peterson's taxonomy, delivered as a 2015 podcast episode, sorts by purpose of creation into personal, secret or stealthlang, auxiliary, fictional, artistic, and engineered languages, with Vorlin, Awolang, Esperanto/Novial, Quenya/Sindarin/Klingon/Verdurian, Okuna, and ro/Ithkuil as the respective instances (S879).

The comparison's verdict: "Наиболее детализированной классификацией, по всей видимости, является типология Д. Питерсона" — 10 tokens, in the comparison section's paragraph on differences between the classifications (S879).

The same verdict cuts the other way, and this is the part worth carrying: Peterson's set is the most detailed yet systematizes worse than the Russian typologies, which the article says is partly explained by its oral podcast form (S879).

Calibration: that ranking is one author's comparison inside one article, not a field consensus, and Peterson's taxonomy is a practitioner framework delivered orally as a 2015 podcast episode — the article cites Peterson's 2015 book elsewhere but does not say the taxonomy is published there; the article also says the six-way purpose split may be an erroneous impression, since per Rhiemeier personal and fictional languages fall inside artlangs (p. 33) (S879).

The table's Peterson column names nine classes; the prose bullet-list gives six and adds parody languages (instance: Yesqur) plus a mention of gesture- and graphic-symbol-based constructed languages, which the article counts as an advantage of the taxonomy; only the three category names are table-only (S879, printed pp. 30, 32–33).

The article's own subject is Peterson's classification and its advantages over the Russian typologies, not the reverse: Шувалова/Сидорова is one of the compared typologies (S879).

The article's own footnote calls Lojban's placement among auxlangs disputable, noting that in Piperski's work Lojban belongs to the philosophical or logical group (S879).

Location: items 1–2.2 sit on printed pp. 31–32 (PDF pp. 4–5 of 7 at `https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike/pdf`, HTTP 200, 630227 B, byte-stable), item 2.2 on p. 32, the comparison table on p. 33 (S879).

## 3. What the classroom study consisted of

The companion article's one-line description of the study: "Sara Sowers-Wills assesses students’ command of concepts in phonology through their creation of a constructed language" — 16 words, §3, p. 5 (S880).

The course design, verbatim: "In the course, examples of phonological systems in natural languages and constructed languages were presented along with instruction in language universals and typology" — 23 words, same section and page (S880).

The claimed novelty, verbatim: "One innovation of this work is that it suggests that a multi-part, creative project can be part of a course even at the introductory level" — 25 words, same section and page (S880).

The course is characterized as "an active learning approach in a project-based phonology course", which is the companion article's one-line characterization of the course's mode (§3, p. 4; the PDF text breaks the hyphenated word across a line) (S880).

What the companion article does *not* carry: the token "semester-long" occurs zero times in its nine pages (`pdftotext | grep -ci semester` → 0), so this amendment attributes no duration to the project (S880).

Whether the study itself reports a semester-long curriculum, and what it claims the project teaches that lectures do not, stays (to-verify) in this entry: the study's own record was reached this round only through the Crossref and Semantic Scholar abstract records, which are not adopted rows (lesson Gate, Sowers-Wills row), so no duration is attributed here.

## 4. What the lane does with it

Classify a world's constructed language by the purpose it serves in that world first, then by structure: the typologies the review compares use purpose-defined top-level classes (auxlang, artlang, logical), and only Peterson's adds modality classes (sign, graphic), so purpose comes first in all three (S879).

Place the language on the a priori / a posteriori scale rather than assigning a label: the scale is that article's operative claim, and a label invites exactly the false binary it argues against (S878).

Expect Eurocentrism as a default, not an accident: a constructed language built by one creator from one language background will carry that background's features, so a world that wants an alien system must design the departure explicitly (S878).

Do not upgrade the classroom evidence into a pedagogy claim: what these rows support is that creating a language assesses a student's command of phonological concepts, at introductory level and inside a project-based course — nothing here compares it with lectures (S880).

## 5. Provenance limits

The Cambridge page of the study answered HTTP 429 to both a browser-shaped and a plain client on 2026-10-25; the record reached through Crossref is not an adopted row (lesson Gate, Sowers-Wills row), so the study's own abstract is not cited here.

Section §3 therefore rests on a companion article's account of the study, not on the study itself (S880).

Two staged elements were dropped rather than repaired. The "semester-long" duration is absent from the companion article's nine pages (S880).

The term «автоконланги» is absent from the review article, which proposes «авторскими языками» for that group instead (S879).

This amendment appends to `linguistics/conlang-scholarship.md`; the base points here through its `couples:` line.
