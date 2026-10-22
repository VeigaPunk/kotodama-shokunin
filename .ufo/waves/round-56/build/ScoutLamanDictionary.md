# ScoutLamanDictionary — Laman's Kikongo-French dictionary, opened

Seat: KotodamaR56.ScoutLamanDictionary. Round 56, claim C, civilization ground (Kingdom of Kongo).
Access date for every source below: 2026-10-22. No tools installed, no packages changed.

## Findings

**An open copy exists and was opened.** Karl Edvard Laman's *Dictionnaire kikongo-français*
(1936) is on the Internet Archive as item `dictionnairekikongofrancais`, in the `opensource`
collection with no access-restricted flag, so the full scan and its OCR layer download without a
login. I read the OCR text file (5,479,385 bytes) and checked every entry I quote against the
scanned page image at 1200 px width. The item's OCR is machine-degraded (metadata
`ocr_degraded = pdf-text-convert`, `page_number_confidence = 0`); it writes `nzimbu` as
"n z in ib u" and drops accents, so nothing below rests on the text layer alone.

**How to find an entry.** The dictionary is ordered by stem, not by written prefix: `ntinu`
sits in the `tinu` run, `nzimbu` inside the `nzi` run, `nkisi` among the `nki` words. Searching
for a headword as a whole word fails on this OCR. I located entries by scanning page text and
then confirmed them on the image. Printed page = scan leaf minus 92; I checked the offset on ten
pages carrying a printed folio, then read the folio off each image I cite (95, 211, 212, 266,
293, 321, 480, 523, 536, 720, 721, 795, 828).

**What the front matter adds.** The abbreviations page lists the dialect sigla used in every
entry: N, S, E, O (north, south, east, west), Be Bembe, Vi Vili, My Mayombe, SB "Sud Bantu",
EB "Est Butaye", NO north-west, NE north-east, Nd Ndingi, Kako Kakongo, Mb Mboka, B Bantu.
The orthography section states that the dictionary follows the orthography of the Institut
International des Langues et Civilisations africaines, with aspirated kh, th, ph where a nasal
prefix has dropped and with four tonal classes marked on the radical. A worldbuilder should not
assume the 1936 spellings are the early-modern ones: the introduction, paragraph 1 (unnumbered
front matter), names its predecessors, Bentley 1887 with Appendix 1895 on the southern dialects
around San Salvador, Butaye 1909-1910 on the eastern dialect around Kisantu, the Landana mission
dictionary of the Kakongo dialect 1890, Marichelle 1912 on Vili, De Clercq 1921 on Kiyombe, and
Van Wing and Penders, *Le plus ancien dictionnaire bantu*, 1928.

**A caution on nzimbu.** Laman glosses nzimbu as blue beads and as currency of former times;
Bentley glosses it as currency. Neither opened page says the beads were shells, so a sentence
that calls nzimbu shell money needs a different row to carry the shell identification.

**Read alongside Bentley.** To test Laman's glosses against an earlier missionary record I opened
Bentley's *Appendix* (1895), the Kongo-English companion to his 1887 dictionary. It carries both
a dictionary and a long preface on the 1624 Kongo catechism, which is the earliest Kongo printed
text and the reason both names (Ntotela, nkisi) matter for a Kongo entry.

### NEW-ScoutLamanDictionary-1

citation: Laman, Karl Edvard. 1936. *Dictionnaire kikongo-français avec une étude phonétique décrivant les dialectes les plus importants de la langue dite kikongo*. Mémoire présenté à la séance du 18 janvier 1932; the scan's file name carries the series as "Hum.Sc.(IRCB) T.II,1". Internet Archive item `dictionnairekikongofrancais`, ARK ark:/13960/s2p9z8152v1, uploaded 2026-09-12; 1,276 scan leaves. No DOI.
url: https://archive.org/download/dictionnairekikongofrancais/Hum.Sc.%28IRCB%29_T.II%2C1_LAMAN%20K.-E._Dictionaire%20Kikongo-Fran%C3%A7ais%20_1936_djvu.txt — page images read to verify: https://archive.org/download/dictionnairekikongofrancais/page/n303_w1200.jpg (p. 211), n304 (p. 212), n358 (p. 266), n385 (p. 293), n413 (p. 321), n572 (p. 480), n615 (p. 523), n628 (p. 536), n812 (p. 720), n813 (p. 721), n887 (p. 795), n920 (p. 828), n187 (p. 95).
route: direct plain GET, HTTP 200; text 5,479,385 bytes; page JPEGs HTTP 200 `image/jpeg` about 0.5-0.6 MB each; the item is in the `opensource` collection with no access restriction, so the full view is public, not controlled lending; no challenge, no login.
kind: book
tier: A — a lexicographic primary source for Kikongo as recorded by a missionary resident from 1891, authoritative for the scope below and for nothing wider; the French glosses are Laman's own categories, not community definitions.
scope: Kikongo and its dialects (Kongo, Vili, Bembe, Mayombe, Ndingi, Kakongo labels) as glossed in 1936: kin terms and lineage words, chiefly and royal titles with their verbs of appointment, place words, raffia cloth, cloth money and beads, shrine words. Not evidence for dates, politics or events; not a source for the Kingdom's history.
quotes:
- p. 211: "kànda, pl. ma-, parenté, famille, souche, tribu; genre, nature, espèce, sorte (de chants)"
- p. 795: "ntinu, roi, chef, président, empereur; (E) albinos; ~ ankama, reine, chef féminin."
- p. 828: "nzimbu, pl. de luzimbu, perles bleues; biens, propriété; monnaie courante (d'autrefois); monnaie d'échange (de jadis)"
- p. 721: "nkisi, fétiche, sorcellerie, ensorcellement, force magique, sortilège, charme"
teaches: Laman's 1936 Kikongo-French dictionary glosses kànda as family and tribe, ntinu as king, nzimbu as former currency and nkisi as magic force and charm.
draft sentences:
- If a lineage needs a word, kànda glosses kinship, family, stock and tribe, and a slave's child counts inside the family, so household and descent are not the same list (NEW-ScoutLamanDictionary-1, p. 211).
- Call the ruler ntinu, glossed king, chief, president or emperor, and give a woman ruler the same noun with ankama (NEW-ScoutLamanDictionary-1, p. 795).
- For succession the dictionary separates byâdi, a regent or paramount chief, from byâdika, to appoint a regent or chief, and byâdila, to inherit, so appointment and inheritance are different verbs (NEW-ScoutLamanDictionary-1, p. 95).
- If a shrine appears, note that nkisi is glossed with the missionary's word fétiche alongside sorcery and magic force, and that nzo a nkisi is given as tomb (NEW-ScoutLamanDictionary-1, p. 721).
- If raffia cloth is traded, note that ma-kángi is the cloth used in trade and that one piece of it is called lubongo (NEW-ScoutLamanDictionary-1, p. 480).
- For payment, use nzimbu with its hedges: blue beads, property, the currency of former times, a medium of exchange of long ago, and also a slave who has entered the family (NEW-ScoutLamanDictionary-1, p. 828).

Locator digest from the same opened copy (each read on the page image; wording paraphrased, exact text on the cited page):

- p. 212: kanda without the tone mark is style, fashion, model, drawing; kàndu, from the same stem, is a ban, prohibition, law, rule, testament; kàndika is to hang a nkisi as a warning or prohibition and to forbid expressly; kàndila (SB) is to excommunicate.
- p. 95: byâdi is the regent or paramount chief word; byâdika is to appoint, consecrate, and also to lay a prohibition on a shrine or chief; byâdila is to inherit (byâdila fwa, to inherit); byâdisa is to crown or call to an office; byâdama is to become regent, be appointed, be rich, have much to inherit; Vili byâsyа is to consecrate a person or re-elect. A whole investiture-and-succession cluster sits on one page.
- p. 266: ki-nene, ki-nene-nene is "titre, expression de profond respect ajouté à ntotela = le roi" — the only ntotela in the dictionary, and it is a title of address, not a headword.
- p. 293: ki-tinu, from ntinu, means office, authority, the quality of a governor, government, prefecture, dominion, power, empire; kitisa means to entrust someone with an office, to consecrate the king, and in Mayombe to marry.
- p. 321: kùba (O) is a heap of goods, a bale, a bundle of mats; kùba dyalubongo is a bundle of raffia mats; kùba mbongo is to contribute goods towards a purchase.
- p. 480: ma-kángi (N) is raffia cloth (mpusu) used in trade, and one piece is called lubongo. This is the only place the cloth sense of lubongo is stated; the word has no headword of its own.
- p. 523: mbànza, from bànzama, covers town, principal village, citadel, the chief's residence, the capital, and the cemetery; a fortified town with a fortress is mbànza yasyamu.
- p. 536: mbōngo is raffia cloth (étoffe de mpusu) and the general word for goods, property, money, treasure, clothing and wealth; it also names cloth woven in Kongo, capital in trade, and a contribution; muntu a mbōngo is a purchased person in servitude.
- p. 720: nkinda, a kind of nkisi, has its force in its head or its belly for as long as it has not lost its virtue; the image or idol holds the soul of the nkisi; such an nkisi stands at the entrance of the village or at its centre.
- p. 721: nkisi also names illness attributed to a shrine, and the derived adjective means magical; fwa nkisi is to be struck by magical punishment for breaking a taboo.
- p. 828: nzimbu also covers property, taking fines or payments (dia nzimbu), putting a price on (tanga nzimbu), a rich person (nkwa nzimbu) and the child of a slave mother; the same page glosses nzimbakani as a branch of the family trunk, race, stock.
- Unnumbered front matter, Abréviations and Les dialectes: N, S, E, O and the sigla Be, Vi, My, SB, EB, NO, NE, Nd, Kako, Mb, B as listed in Findings.
unopened: the 1624 *Doutrina Christã* itself (only Bentley's report of it, below); Butaye 1910 and Van Wing and Penders 1928 (named as predecessors in Laman's introduction, not needed for this scope); the Royal Museum for Central Africa catalogue record for this title (no need once a full public scan was confirmed); Laman's ethnographic monograph volumes (not in scope).

### NEW-ScoutLamanDictionary-2

citation: Bentley, William Holman. 1895. *Appendix to the Dictionary and Grammar of the Kongo Language, as spoken at San Salvador, the Ancient Capital of the Old Kongo Empire, West Africa*. London: Baptist Missionary Society. Preface dated Wathen Station, Congo Free State, September 1st, 1894. Internet Archive item `dictionarygramma00bentuoft` (Robarts and University of Toronto copy), 348 scan pages, printed pages to 920. The 1887 main volume is item `dictionarygramma00bent` (University of Illinois), not quoted here.
url: https://archive.org/download/dictionarygramma00bentuoft/dictionarygramma00bentuoft_djvu.txt — page images read to verify: https://archive.org/download/dictionarygramma00bentuoft/page/n8_w1200.jpg (Preface, p. vii), n130 (p. 841), n191 (p. 902), n208 (p. 919).
route: direct plain GET, HTTP 200; text 969,065 bytes; page JPEGs HTTP 200 `image/jpeg` about 0.85-0.93 MB; the item sits in the `robarts` and `toronto` collections with no access-restricted flag, so full view without login; no challenge. For this item the `page/nNNN` image index runs one ahead of the djvu page-object index, so locators below are printed folios read off the images.
kind: book
tier: A for Bentley's own glosses and his stated objection; B for the content of the 1624 catechism, which I know only through his quotations of it, not from the catechism itself.
scope: the southern Kongo dialect around San Salvador as lexicographed for the Baptist Mission in 1887-1895, plus Bentley's reading of the 1624 Portuguese-Kongo catechism: what the catechism used ntotela and nkisi for, and what a missionary of 1894 thought of that usage. Not evidence for the kingdom's institutions.
quotes:
- p. vii: "It is interesting to find untotela (p. 39) used for majesty, so that Ntotela is not simply a dynastic name of the present kings."
- p. vii: "This is a very objectionable use of nkisi, fetish."
- p. 902: "Nzimbu, 2, n.+currency."
- p. 841: "Kanda, 12, n., build, make, style, pattern"
teaches: Bentley's 1895 appendix reports that the 1624 Kongo catechism used untotela for majesty and nkisi for holy, a use he calls very objectionable.
draft sentences:
- If the entry stages the 1624 catechism, Bentley reports that it used untotela for majesty, so Ntotela was not only a dynastic name (NEW-ScoutLamanDictionary-2, p. vii).
- He records that the catechism used nkisi, which he glosses as fetish, for holy and sacred, and he calls this a very objectionable use (NEW-ScoutLamanDictionary-2, p. vii).
- He also notes that the catechism's phrase for the Church of Rome was literally the fetish house, and that nzo ankisi meant the grave as well (NEW-ScoutLamanDictionary-2, p. vii).
- For an earlier generation of money, his Kongo-English list gives nzimbu simply as currency, without Laman's range of beads, property and family slave (NEW-ScoutLamanDictionary-2, p. 902).
- His kanda entry gives build, make, style and pattern, agreeing with Laman's non-lineage sense, so not every kanda in a translation is a clan (NEW-ScoutLamanDictionary-2, p. 841).

Locator digest from the same opened copy:

- p. vii: the catechism was translated from a Portuguese original printed by order of Mattheus Cardoso and Bentley dates it 1624; he quotes the Kongo string "Canca auquissi yanzua muquissi acuna Roma" and says its sense is fetish devotion of the fetish house at Rome; baptism is dia mungua, to eat salt; Purgatory is ecussuilu, the place of smearing.
- p. 841: kandu is a ban, interdiction, curse or sentence of excommunication, pronounced at a junction of two roads with the mouth rubbed in dust and the knees struck by hand; dia e kandu is to lay such a curse; mwana a kandu is a person under it. This is the law-and-sanction side of the same root as kànda.
- p. 902: nzimbakani is the parent stock or common stock, the whole race, with nzimbakani a uwuntu for the whole human race; the same page has bwa e nzula, to kneel three times in approaching the king.
- p. 919: the entry Untotela repeats the catechism point: in the Doutrina Christã of 1624, untotela means majesty, so Ntotela is not a simple dynastic name.
unopened: the 1624 Doutrina Christã (only Bentley's quotations); the 1887 main volume (sampled at four points, grammar and word lists, and not quoted here); Butaye's Bunda grammar of 1804, mentioned by Bentley, not opened.

## Negative finding on the title "Mani"

Neither opened dictionary carries `mani` as a lordly title (the word of the early Portuguese documents, as in Mani Kongo and Mani Soyo). Searching the full OCR text of both items finds no "Mani Kongo", no "Mani Soyo" and no headword `Mani` as a title. Laman's only entries are `mani (My), bientôt` and `mani lumbu (SB), majordome`. For the king the dictionaries give ntinu and, as a title of address, ntotela; for a chief, mfumu and byâdi. Inference, not a quoted claim: a Kongo entry that writes "Mani Kongo" as a Kikongo word would need the early Portuguese documents themselves, which I did not open; these two rows cannot carry it.

## Notes for the L1

- The two rows do not restate each other: Laman gives the 1936 lexicon (kin words, titles and appointment verbs, place words, cloth and cloth money, shrine words), Bentley gives the 1894 missionary reading of the 1624 catechism and an earlier one-line gloss for currency and for kanda. Both are Kongo-Kikongo lexicography, not Kongo history.
- `lubongo` has no headword in Laman; its cloth sense is stated only inside `ma-kángi` (p. 480) and in `kùba dyalubongo` (p. 321). A sentence that calls lubongo a cloth word should say it is the name of one piece in the trade, not a general cloth noun.
- Laman's French "fétiche" and "sorcellerie" are the dictionary's own wording, not community usage; Bentley's "very objectionable use of nkisi, fetish" is an 1894 missionary judgment of the catechism's translation. Keep both inside quotation when the entry uses them.
- The dictionary is not a history: it has no dates for the kingdom, no kings list and no Antonian movement material. Nothing above supports a chronological claim.

## Unrun checks

- No image-by-image collation of the whole dictionary; I verified thirteen Laman pages and four Bentley pages on the images and left the rest on the OCR text layer.
- No check of Laman's ethnographic volumes or of his Kongo grammar, which may gloss titles differently.
- No semantic check of the dialect sigla beyond the abbreviations page (for example whether Laman's `SB` and `EB` mean the same thing a modern reader would take them for).
