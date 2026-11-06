# ExecRegistry97 — round-97 registry rows (S985-S993)

All 8 admitted scout candidates re-verified by ExecRegistry97 on 2026-11-05 before writing:
plain curl (-L, --max-time 30, default UA; transient retry 3x/20s), fresh capture sha256
recomputed, located quote recounted on the fresh capture text (bytes.count == 1 for all 8).
Static artifacts byte-identical to ScoutSources97's shas; the only divergent artifact is
the dynamic Internet Archive details page for S986 (expected; quote lives on its djvu text).
Id assignment: sequential from S985 in candidates.json `admitted` array (candidate-key) order.
Collision check before assignment: grep -c -F full URL and host+path vs corpus/SOURCES.md
-> 0/0 for all 8 (loop rc 0). Registry rows at check: 908, highest S984.

## Claim-C rows (used-by corpus/knowledge/linguistics/verbal-duelling-ritual-insult.md)

### S985 — pagliai_2009 — tier A, paper
- source cell: Pagliai 2009, 'The Art of Dueling with Words: Toward a New Understanding of Verbal Duels across the World', Oral Tradition 24/1 (2009): 61-88 — https://journal.oraltradition.org/wp-content/uploads/files/articles/24i/04_24.1.pdf
- capture: attempt1 rc=0 http=200, 269331 B, sha256 5799114d2e3fac10d9372a78637ef47605ac429b1fcde5a2b11855cfa119fd63 (== scout)
- extraction: pdftotext -layout rc=0, 91127 B, sha256 967e3cd4a33b2cc4e77bff6927b308bd417ce143a1188112c19f468960b9578b (== scout)
- quote (byte-exact, single line, count 1): "A common view of verbal duels posits that they are a cathartic expression of aggression"
- evidence: reports/round-97/evidence/S985.pdf, reports/round-97/evidence/S985.txt
- scope: verbal duel; survey; social order
- teaches: The survey rejects the catharsis reading and shows verbal duels negotiating social order before an audience; use for function and framing, not for any single tradition's rules.

### S986 — hoebel_1954 — tier A, book
- source cell: Hoebel 1954, The Law of Primitive Man: A Study in Comparative Legal Dynamics, Harvard University Press (open scan, Internet Archive in.gov.ignca.2688) — https://archive.org/details/in.gov.ignca.2688
- captures: details page attempt1 rc=0 http=200, 212777 B, sha256 966655bbbe73… (dynamic page, differs from scout's 277031 B — expected); quote-bearing djvu OCR attempt1 rc=28 timeout http=302, attempt2 rc=0 http=200, 844105 B, sha256 d786726a8213030a822f916747e357f25dc52fef23909c9cb429c771469eb16d (== scout)
- quote (byte-exact, single line, count 1, on djvu OCR): "Among the East Greenlanders song duels may be carried on for"
- evidence: reports/round-97/evidence/S986.html (details page), reports/round-97/evidence/S986.txt (djvu OCR, quote-bearing)
- scope: song duel; nith song; dispute settlement
- teaches: The monograph treats East Greenland song duels as juridical dispute settlement with prestige as the stake; Inuit-specific, not a universal model of insult litigation.

### S987 — lokasenna_bellows — tier A, book
- source cell: The Poetic Edda, tr. Henry Adams Bellows, 'Lokasenna', Wikisource transcription of the 1923/1936 translation — https://en.wikisource.org/wiki/The_Poetic_Edda_(tr._Bellows)/Lokasenna
- capture: attempt1 rc=0 http=200, 307750 B, sha256 5f3353dce7d2583786f287495adacfac428bb98fc79e5656345ff3e5ee4f2f2b (== scout)
- quote (byte-exact, single line, count 1, raw HTML bytes): "Then Loki went into the hall, but when they who were there saw who had entered, they were all silent."
- evidence: reports/round-97/evidence/S987.html
- scope: senna; primary text; insult contest
- teaches: The transcription gives the Lokasenna senna in a public-domain translation with stable per-stanza anchors; cite as primary text while distinguishing translation choices from the Old Norse.

### S988 — dunbar_kennedie_murphy — tier B, docs
- source cell: Dunbar & Kennedy, 'The Flyting of Dunbar and Kennedy', normalized and glossed by Michael Murphy (clan society-hosted edition) — http://www.clanstrachan.org/history/Flyting_of_Dunbar_and_Kennedy.pdf
- capture: attempt1 rc=0 http=200, 390354 B, sha256 d12852cea4cac0eab4a3c99396cd0800828359a1ce86cc9f73f98c5cd4142737 (== scout); pdftotext -layout rc=0, 66211 B, sha256 aa06f258d8cac7be3bac9534e8f175cac0315fb211e70dbe3dd7b360f1264efd (== scout)
- quote byte-exact (count 1, contains one newline shown as ⏎): "The flyting was a verbal competition in which the participants vied in heaping abuse of⏎all sorts on each other, some of it quite gross."
- quote cell form (newline -> space, 25 words): "The flyting was a verbal competition in which the participants vied in heaping abuse of all sorts on each other, some of it quite gross."
- evidence: reports/round-97/evidence/S988.pdf, reports/round-97/evidence/S988.txt
- scope: flyting; heaped abuse; literary game
- teaches: The glossed edition defines flyting as heaped-abuse verbal competition, at least in part a literary game; community-hosted edition, cite its framing rather than the host site's authority.

### S989 — ruszkiewicz_2020 — tier A, paper
- source cell: Ruszkiewicz 2020, 'The Flyting of Dumbar and Kennedie as an Inverted Litany: The Scottish Perspective on a Poetic Agon', Prace Filologiczne. Literaturoznawstwo 10(13), DOI 10.32798/pflit.575 — https://repo.ignatianum.edu.pl/pl/file_records/866/download
- capture: attempt1 rc=0 http=200, 130290 B, sha256 8a59f531d9e6eace014db8f512ffe043148c5153c4c5401c5b182fe56eda4292 (== scout); pdftotext -layout rc=0, 38886 B, sha256 3cae64e59e7938ecfb8067b3f24fe3063eb3f5413a79c17bae8e5b966a5f0472 (== scout)
- quote byte-exact (count 1, one newline ⏎): "the Scottish genre of flyting, whose main⏎purpose was to humiliate the opponent"
- quote cell form: "the Scottish genre of flyting, whose main purpose was to humiliate the opponent"
- evidence: reports/round-97/evidence/S989.pdf, reports/round-97/evidence/S989.txt
- scope: flyting; genre definition; poetic agon
- teaches: The peer-reviewed article defines the Scottish flyting genre by its purpose to humiliate the opponent and reads it as poetic agon; genre-bound to the Scots evidence it discusses.

### S990 — garzia_2007 — tier A, paper
- source cell: Garzia 2007, 'History of Improvised Bertsolaritza: A Proposal', Oral Tradition 22/2 (2007): 77-115 — https://journal.oraltradition.org/wp-content/uploads/files/articles/22ii/8_garzia3.pdf
- capture: attempt1 rc=0 http=200, 370994 B, sha256 b7f8247b890ec1ef9fb444209fa7903ccd81d3b28dac52037a6e5c0d66aa3052 (== scout); pdftotext -layout rc=0, 117600 B, sha256 01f7f2180616ababbace1a49c0026bb1c9d08e9b66ddbc593d5e99c8d88b9ba9 (== scout)
- quote byte-exact (count 1, one newline ⏎): "the references to the verbal combats between bertsolaris and the social importance that such⏎ad hoc compositions appeared to have had at the time."
- quote cell form: "the references to the verbal combats between bertsolaris and the social importance that such ad hoc compositions appeared to have had at the time."
- evidence: reports/round-97/evidence/S990.pdf, reports/round-97/evidence/S990.txt
- scope: bertsolaritza; improvised verse; judged contest
- teaches: The article reconstructs historical verbal combats between bertsolaris and the social weight of ad hoc improvised verse; a historical reconstruction, not a description of today's judged championships.

### S991 — nadera_2019 — tier A, paper
- source cell: Nadera Jr & Mooney-Singh 2019, 'Balagtasan Beyond Balagtas: Debate Poetry, a Filipino Tradition', SARE 56/1 (2019) — https://ojie.um.edu.my/index.php/SARE/article/download/19055/10299
- capture: attempt1 rc=0 http=200, 229711 B, sha256 6e5ab013b2436459789bacb21af3193b2ab578bd5c49954c3205096589ce02bd (== scout); pdftotext -layout rc=0, 48514 B, sha256 fab38ff4b650c10bc77dc66527393a2d9f40838e5a284ae63c5d0114375edc50 (== scout)
- quote (byte-exact, single line, count 1): "Balagtasan is an indigenous form of competitive Filipino debate poetry in the Tagalog language"
- evidence: reports/round-97/evidence/S991.pdf, reports/round-97/evidence/S991.txt
- scope: balagtasan; debate poetry; adjudication
- teaches: The article frames balagtasan as indigenous competitive debate poetry with a moderator and adjudication; Philippine-specific, do not generalize the lakandiwa role beyond it.

### S992 — nicholson_1907 — tier A, book
- source cell: Nicholson 1907, A Literary History of the Arabs, Project Gutenberg #37985 transcription of the 1907 Cambridge edition — https://www.gutenberg.org/files/37985/37985-0.txt
- capture: attempt1 rc=0 http=200, 1203657 B, sha256 e356cd7d2e57677d48413768956fa9b517ed8f28d9ff8ff63b3651cfa0893066 (== scout)
- quote byte-exact (count 1, contains CRLF line breaks shown as ⏎; note the curly apostrophe in Naqá'iḍ is U+2019): "Soon these 'Flytings' (_Naqá'iḍ_) were recited⏎everywhere, and each poet had thousands of enthusiastic partisans who⏎maintained that he was superior to his rival."
- quote cell form (line breaks -> space): "Soon these 'Flytings' (_Naqá'iḍ_) were recited everywhere, and each poet had thousands of enthusiastic partisans who maintained that he was superior to his rival."
- evidence: reports/round-97/evidence/S992.txt
- scope: naqaid; invective; partisan audience
- teaches: The history describes the Naqaid of Jarir and Farazdaq as a public scolding-match recited before thousands of partisans; secondhand early-Islamic material, keep the partisan-audience claim bounded to his account.

## Frontier-curation row (after the claim-C rows; used-by funerary-lament entry)

### S993 — Threnoi to Moirológia — tier A, paper
- nominated in .ufo/waves/round-96/w1/stage/ReviewerThrenoi96/decision.md section 5
- source cell: Fishman 2008, 'Thrênoi to Moirológia: Female Voices of Solitude, Resistance, and Solidarity', Oral Tradition 23/2 (2008): 267-295 — https://journal.oraltradition.org/wp-content/uploads/files/articles/23ii/07_23.2.pdf
- re-open by ExecRegistry97: attempt1 rc=0 http=200, 302080 B, sha256 1e53dabf880576270d134fa285914b17c802d62ee84b159a72e535fc3fc5599a (byte-identical to the round-96 decision capture); pdftotext rc=0, 83367 B; quote counts Q1=1 Q2=1 Q3=1
- anchor quote byte-exact (count 1, one newline ⏎): "the antiphonal structure and style of lament performance contribute to⏎social bonding among women; they mourn in a fugue."
- quote cell form: "the antiphonal structure and style of lament performance contribute to social bonding among women; they mourn in a fugue."
- evidence: reports/round-97/evidence/S993.pdf, reports/round-97/evidence/S993.txt
- scope: lament; antiphony; professional mourner
- teaches: The article reads Maniat antiphonal lament as social bonding among women and names the professional dirge leader (koriféa); Greek-specific evidence, supplementary to the lament entry's antiphony section.
- used-by: corpus/knowledge/linguistics/funerary-lament-dirge-formulae.md

## Dropped (re-verified or scout-adjudicated, not written)

See dropped.md in this stage dir for bevan_nakaid_edition and labov_chapter
(opened, quote uniqueness unattainable, no row written).
