# ScoutKongoNaming — personal names and titles: Christian name, Kikongo name, office

- seat: `KotodamaR56.ScoutKongoNaming` (scout, claim C ground: the Kingdom of Kongo entry)
- round: kotodama 56 (hyaku phase 4), 2026-10-22
- lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, claim base `052f145cbcff6996c153d460d81ce346ce74bfbc`, declaration `b4b7db91a38447bb2c07b0ef436fc9654dcec89c`
- assignment: how a Kongo ruler's name combined a Christian baptismal name with a Kikongo name and lineage; the title words `mani`, `ntotila`, `mwene`; the province titles (Mani Soyo, Mani Mbata); an early dictionary plus an open scholarly source, aimed at worldbuilder decisions
- rows: this seat files one row, `NEW-ScoutKongoNaming-1` (Bostoen, Ndonda Tshiyayi and de Schryver 2013). Two further sources were opened at page level and are **already rowed by sibling seats** — Bentley 1887 as `NEW-ScoutBentleyDictionary-1`, Lopes/Pigafetta as `NEW-ScoutPigafettaLopes-1` — so this report supplies the quotes and page data those two rows need for their naming sentences instead of filing duplicates. The L1 assigns final `S` ids at integration.
- access date for every source below: 2026-10-22
- verification: the Bostoen and Bentley fragments were substring-checked against the saved extracted text after whitespace normalisation only (6 of 6 and 6 of 6 found); the 1881 Lopes fragments were checked after mapping that OCR's `f` for long `s` (4 of 4 found, the OCR behaviour `NEW-ScoutPigafettaLopes-1` already declares); the 1591 Italian print was read from page images at 170-300 dpi because its OCR is corrupt at exactly these passages. No tool was installed.

## Route summary

| source | file actually read | route | size |
|---|---|---|---|
| Bostoen et al. 2013 | `https://repository.up.ac.za/bitstreams/902842e3-d5eb-4688-bf3f-40b310b24959/download` | direct plain `curl`, HTTP 200, `application/pdf`, no challenge, no login; read with `pdftotext -layout` | 2,360,681 bytes, 31 pages |
| Bentley 1887 | `https://archive.org/download/dictionarygramma00bent/dictionarygramma00bent_djvu.txt` and `.../dictionarygramma00bent.pdf` | direct, HTTP 200; print pages 368, 369, 401, 502 re-read as 200 dpi page images from the PDF to settle exact wording | 2,174,902 bytes text; 56,700,534 bytes PDF |
| Lopes/Pigafetta 1591 (Italian) | `https://archive.org/download/ARes04525/ARes04525.pdf` (leaves 33 and 42) | direct, HTTP 200; page images at 170 and 300 dpi, since the OCR garbles the passages | 11,274,635 bytes, 97 leaves |
| Lopes/Pigafetta 1881 (English) | `https://archive.org/download/reportofkingdomo00lope/reportofkingdomo00lope_djvu.txt` | direct, HTTP 200; same copy as `NEW-ScoutPigafettaLopes-1` | 441,931 bytes |

Printed page numbers are used throughout, not PDF page indices. In the 1591 Italian scan printed page = leaf minus 8 (leaf 33 header reads 25, leaf 42 is page 34); in the Bentley scan the folio is printed at the top of each page. For Bentley I cite the printed folio and, where I name a scan page, the PDF page number: PDF pages 396, 397, 429 and 530 print 368, 369, 401 and 502. The item's djvu object index is PDF page minus one, so those are objects 395, 396, 428 and 529; the item's `_page_numbers.json` sidecar is itself off by one and should not be used for folios.

---

### NEW-ScoutKongoNaming-1

citation: Bostoen, Koen, Odjas Ndonda Tshiyayi, and Gilles-Maurice de Schryver. 2013. "On the origin of the royal Kongo title ngangula." *Africana Linguistica* 19: 53-83. Open repository copy, University of Pretoria (UPSpace).

url: https://repository.up.ac.za/bitstreams/902842e3-d5eb-4688-bf3f-40b310b24959/download

route: direct plain request (curl), HTTP 200, `application/pdf`, 2,360,681 bytes, 31 pages, read with `pdftotext -layout`; no challenge, paywall or login met, 2026-10-22.

kind: paper

tier: A — a peer-reviewed historical-linguistic study whose subject is exactly this: the etymology and title status of `ngangula` and the other royal Kongo titles. Tier B for the political history it reports from Thornton and Vansina, which the entry should cite through those authors if it leans on it.

scope: what the royal titles `ngangula`, `ntinu` and `ntotila` are and that they co-exist; the literal sense of `ngangula a Kongo`; the `Mwene Vunda` office in the selection and coronation of kings; the kinship-titled lordship of Mbata and the naming chain of the founder's line (`Nsaku Lau`, `Nimi a Nzima`, `Lukeni lua Nimi` also called `Ntinu Wene`); a royal style that carries a Christian name (`Pedro II Afonso`). Not a source for the `mani` form, the number of provinces, regalia inventories, minkisi, or royal chronology.

quotes:
- p. 55, Introduction: "ngangula a Kongo literally means ‘blacksmith of Kongo’"
- p. 55, Introduction: "which co-exists with others such as ntinu and ntotila"
- p. 69, on Alvaro II's burial and Pedro II's coronation: "the Mwene Vunda (an official who played an important role in the selection and coronation of the kings)"
- p. 73, on Mbata and the founder traditions: "father of the bride of Nimi a Nzima, himself father of Lukeni lua Nimi or Ntinu Wene"

teaches: Kongo royal style stacked Kikongo titles — ngangula, literally "blacksmith of Kongo", ntinu and ntotila — while selection and coronation belonged partly to the Mwene Vunda office.

draft sentences:
- Royal style was a stack of Kikongo titles rather than one crown word: ngangula a Kongo, literally "blacksmith of Kongo", co-existed with ntinu and ntotila, so let a ruler carry several titles with separate histories (NEW-ScoutKongoNaming-1, p. 55).
- Give the throne a craft metaphor as well as a rank: the title that names the king also names the smith, which lets legitimacy rest on arbitration and making rather than descent alone (NEW-ScoutKongoNaming-1, p. 55).
- Put accession partly in an office: the Mwene Vunda played an important role in the selection and coronation of the kings, so a worldbuilder should name the official who convenes and crowns, not only the heir (NEW-ScoutKongoNaming-1, p. 69).
- Let a name record a lineage link and an alias: the founder's line is given as Nsaku Lau, Nimi a Nzima and Lukeni lua Nimi, also called Ntinu Wene, so the connector a or lua can join a person to a forebear while a second name marks the same person (NEW-ScoutKongoNaming-1, p. 73).
- Run two naming systems in parallel: the article's source calls a king Pedro II Afonso, so a Christian name and a Kikongo name can stand in one style instead of one replacing the other (NEW-ScoutKongoNaming-1, p. 70, note 17).

---

## Quotes and pages for the two sibling rows this report cites

### NEW-ScoutBentleyDictionary-1 — Bentley 1887, *Dictionary and Grammar of the Kongo Language* (archive.org `dictionarygramma00bent`)

Please put these four in that row's Gate; they are the evidence behind my Bentley sentences and they are page-verified on the 1887 print, not the 1895 Appendix.

- p. 368, s.v. `Ndom`: "Ndom (P. dom), corrupt forms of Portuguese names, preceded by the title Ndom, are assumed by Kongos as Christian names"
- p. 369, s.v. `Ndwafunsu`: "Ndwafunsu (a Santu name); Dom Alfonso; see Ndom"
- p. 502, Appendix, "TITLES OF NOBILITY": "They are not hereditary, but on the death of one noble, the title (ngenda, 2) is conferred to another"
- p. 502, same section: "Ntinu nekongo, is not a title, but used in addressing a person of high rank"

Page-carried details on the same pages, usable without a fifth quote: "Women are styled Ndona" and the women's forms `Ndonamadia, Dona Maria` (p. 368); the title list itself, `Mfutila`, `Kabata`, `Nenkondo`, `Lubatabata`, `Nelumbu`, `Tulante`, `Masaku`, `Nsaku`, `Sengele`, `Nemwanda`, `Nempangu`, `Nkondi`, `Katendi`, `Nkangampaka`, `Mpidixipe (P. Principe)`, `Nemiaia`, `Neloto (the spoon-bearer)` (p. 502); `Ntotela, 2, emperor (title of the kings of Congo)` and the fuller style `ntotela ntinu nekongo, "king of Kongo"` (p. 401).

draft sentences:
- Baptismal names passed through Kikongo phonology: Bentley records that Kongos assumed corrupt forms of Portuguese names, preceded by the title Ndom, as Christian names, with Ndona for women, so a worldbuilder should derive Christian names locally rather than import them intact (NEW-ScoutBentleyDictionary-1, p. 368).
- One person can hold two convertible names: the dictionary pairs a Kikongo name with the saint's name it renders — Ndwafunsu, Dom Alfonso — so a baptismal name can be a second name rather than a replacement (NEW-ScoutBentleyDictionary-1, p. 369).
- Make noble titles offices, not hereditary ranks: on a holder's death the title, ngenda, was conferred on another, so separate the lineage from the office and let a title move between houses (NEW-ScoutBentleyDictionary-1, p. 502).
- Let outsiders mistake an honorific for an office: Bentley states that ntinu nekongo is not a title but an address to a high-ranking person, which is exactly the error a foreign record makes (NEW-ScoutBentleyDictionary-1, p. 502).
- Keep the top style distinct: Ntotela is entered as "emperor (title of the kings of Congo)", with the phrase ntotela ntinu nekongo glossed "king of Kongo", so the style is a phrase rather than a single word (NEW-ScoutBentleyDictionary-1, p. 401).

Observed absence worth recording in the entry if it discusses the word: the 1887 dictionary of the capital's dialect has no `Mani` headword (zero hits in the full text) and enters `Chief` as `mfumu` and `Emperor` as `mfumu` or `ntinu`; `mwene` appears in the note on the prefix `Ne`/`ne-` (p. 369) but has no headword of its own. Absence in a dictionary is not absence in the language, and `Sonio` is itself corrected there: "Sonio, a corruption of San Antonio at the mouth of the river" (Preface, p. xi).

### NEW-ScoutPigafettaLopes-1 — Lopes and Pigafetta, English 1881 (archive.org `reportofkingdomo00lope`)

That row's scope already covers "the Mani lords" and the six provinces. The one passage it does not yet quote is the naming paragraph on p. 72, which is the strongest single statement in any opened source for a Christian name beside a territorial title:

- p. 72, Book I: "was called Mani Sogno, that is Lord of Sogno, although known by the name of Emmanuel after his baptism"
- p. 72, Book I: "neither men or women had proper names, such as are used by rational beings, but adopted those belonging to plants, stones, birds, and beasts"
- p. 72, Book I: "The lords took the names of the several provinces over which they ruled"

Reading of the 1591 Italian print, for the L1's information (not a quote request, because that scan's OCR is corrupt and the volume is not to be rowed twice): leaf 42, printed p. 34, reads that the lords who govern Soyo "si chiamano Mani Sogno cioè signori di Sogno", that they come from the royal house, and that the holder is "D. Diego Mani Sogno"; leaf 33, printed p. 25, glosses the word — "questa parola Mani significa signore, & il resto è paese, & la signoria" — and names the six provinces "Bamba, Sogno, Sundi, Pango, Batta, & Pemba". The 1881 translation is faithful on both points.

draft sentences:
- Let a baptismal name sit beside a territorial title rather than replace it: the first convert lord "was called Mani Sogno, that is Lord of Sogno, although known by the name of Emmanuel after his baptism" (NEW-ScoutPigafettaLopes-1, p. 72).
- Treat the report's claim that people had no proper names before Christianity as the reporter's over-reading: it says they used plant, stone, bird and beast names and that lords took province names, which a dictionary holding thousands of Kikongo personal names contradicts (NEW-ScoutPigafettaLopes-1, p. 72).
- Let the office rename the holder: because the lords took the names of the provinces they ruled, a worldbuilder can make accession swap a personal name for a territorial one (NEW-ScoutPigafettaLopes-1, p. 72).

---

## Findings for integration

### The title vocabulary, separated by what each word is

| form | opened evidence | what it is, and what it is not |
|---|---|---|
| `ntotila` / `ntotela` | Bostoen p. 55; Bentley p. 401, p. 502 | the king's title, glossed "emperor (title of the kings of Congo)"; the style is a phrase, `ntotela ntinu nekongo` |
| `ntinu` | Bostoen p. 55; Bentley p. 502 | a royal title in its own right; but `Ntinu nekongo` in Bentley's usage is "not a title, but used in addressing a person of high rank" |
| `ngangula (a Kongo)` | Bostoen p. 55 | a royal title whose literal sense is "blacksmith of Kongo"; the article argues the political sense is prior to the craft sense |
| `mwene` | Bentley p. 369 (prefix note, forms `mwene`, `mwenye`); Bostoen p. 69 (`Mwene Vunda`) | the possessive/agent prefix that appears "in the names of some titles of nobility, of clans, and of persons"; not a rank by itself, since the complement names the office |
| `mani` | Lopes/Pigafetta, 1591 p. 25 and 1881 p. 43 | the Portuguese-orthography rendering the reporters use, glossed "Lord", followed by the territory: `Mani Bamba`, `Mani Sogno` |
| `ngenda` | Bentley p. 502 | the title as a thing conferred ("to confer a title: yeka e ngenda"), which is why a title is an object in the gift of the crown |
| `Ndom` / `Ndona` | Bentley p. 368 | the prefix carried by Christian names of men, and its women's counterpart; not a noble title |

`[INFERENCE]` `mwene` and `mani` are the same morpheme seen through two orthographies. No opened source states the equation: Bentley gives `mwene` as the prefix in titles, and Lopes's reporters gloss `Mani` as "lord". Do not write the equation as sourced; either hedge it in the entry or leave it as a note.

### How a name was built — three separable layers the entry can hand the world bible

1. **A Kikongo name, often chained to a forebear.** Bostoen p. 73 gives `Nsaku Lau`, `Nimi a Nzima`, `Lukeni lua Nimi` (also called `Ntinu Wene`). The connector `a`/`lua` joins a person to another name; the article does not gloss it, so the entry should not translate it as "son of" without another row.
2. **A Christian name, either Portuguese or Kikongo-ised.** Lopes p. 72 has the lord "known by the name of Emmanuel after his baptism"; Bentley p. 368 has the systematic later form, Portuguese names "preceded by the title Ndom" and assumed "as Christian names", with `Ndwafunsu` for Dom Alfonso (p. 369) and `Ndona` for women.
3. **An office title drawn from a place or a function.** Lopes p. 25: "the rest is the country"; Bentley p. 502 shows function titles too (`Neloto (the spoon-bearer)`) beside territorial ones, and `Mpidixipe (P. Principe)` shows a title coined from a Portuguese place-name.

The design decision this supports: a ruler's full style can be *personal name + Christian name + office title*, and the sources show these moving independently — a title is conferred at death (Bentley p. 502), a baptismal name is added at baptism (Lopes p. 72), and a second Kikongo name can mark the same person (Bostoen p. 73).

### Succession, as far as these three sources carry it

- Titles were not hereditary: on the death of a noble the title was conferred on another (Bentley p. 502).
- Selection and coronation belonged partly to an office, the `Mwene Vunda` (Bostoen p. 69).
- Mbata's lords held privileges in the selection and enthronement of kings, says the article (Bostoen p. 74, page-carried: "This continued to be reflected in the privileges, which Mbata leaders enjoyed with respect to the selection and enthronement of Kongo kings").
- Nothing in these three sources fixes an electoral college, a fixed number of electors, or a rule of primogeniture. Lopes's succession narrative (rowed by `NEW-ScoutPigafettaLopes-1`, pp. 92-94) shows contested claimants, not a rule; the entry should not manufacture a constitution.

### Where the outsider's record over-reads or misnames

- "Neither men or women had proper names" (Lopes p. 72) is contradicted by the 1887 dictionary's thousands of `ne-` personal names and by its `Ndom`/`Ndona` Christian-name system; keep the claim as the reporter's, not as Kongo practice.
- "Mani" is the reporters' spelling and gloss, not a Kikongo headword: Bentley's dictionary of the capital's dialect has no `Mani` entry.
- "Sonio" is a misnaming: Bentley corrects it to "a corruption of San Antonio at the mouth of the river" (Preface, p. xi), i.e. Soyo, and notes that Brusciotto's grammar is in the Sonyo dialect, not the court's.
- "Ntinu nekongo" looks like a title in European lists; Bentley says it is an address (p. 502).
- `[GAP]` **`Mani Mbata` is not attested in any source I opened.** Lopes lists `Batta` among the six provinces and names `Don Sebastião Manibamba` as governor of Bamba, but gives no `Mani Batta`; Bostoen calls Mbata's ruler "the duke of Mbata", a Portuguese style. The entry should either write "the duke of Mbata" with Bostoen's locator, or use `mwene Mbata` only after a row that carries it. `Mani Soyo` is safe: Lopes p. 72 ("called Mani Sogno, that is Lord of Sogno") and the 1591 print p. 34.
- Kongo king lists in modern writing give styles such as `Afonso I Mvemba a Nzinga` and `Garcia II Nkanga a Lukeni`; no source opened this session carries either full pair. Bostoen p. 73 carries the naming *pattern* and p. 70 note 17 carries `Pedro II Afonso`; a sentence using the two famous pairs needs another row (Cavazzi, the Afonso letters, or a king-list study).

## unopened

- Thornton, "The Kingdom of Kongo, ca. 1390-1678," *Cahiers d'études africaines* 22 (1982): the Persée landing page opened (HTTP 200), but the full-text endpoint `https://www.persee.fr/docAsPDF/cea_0008-0055_1982_num_22_87_3380.pdf` answered HTTP 403 both plain and with a browser user agent and referer. Challenge met, not passed; the paper was not read and is not cited.
- Cavedon, "Kongolese Sacred Sovereignties and Legalities in the Early Modern Trans-Atlantic," *Religions* 16(4):444 (2025), which search surfaced as a candidate for the baptismal-name and succession-conflict material: `https://www.mdpi.com/2077-1444/16/4/444` answered HTTP 403 with a 400-byte body. Challenge met, not passed; not read, not cited.
- The 1597 English translation of Pigafetta by Abraham Hartwell was searched for in archive.org's advanced search together with the 1591 Italian, 1598 Latin and 1596 Dutch editions; no Hartwell scan appeared in the result set, so it was not opened.
- Bentley 1895, *Appendix to the Dictionary and Grammar of the Kongo Language* (archive.org `dictionarygramma00bentuoft`): not opened by this seat, because `NEW-ScoutBentleyDictionary-1` covers the Bentley rows and every cited page here is in the 1887 volume.
- Hilton, *The Kingdom of Kongo* (1985) and MacGaffey, *Custom and Government in the Lower Congo* (1970): both archive.org items are lending-restricted, which needs a login, so neither was opened (QUALITY criterion 10).
