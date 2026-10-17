# R9-F02c — alternate-angle hunter

**Residual:** R9-R8-F02 (prior row R8-F02, round-6 row R6-02-B) · **Round:** 9 · **Date:** 2026-10-17
**Entry:** `corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md` — sha256 `bf6c92f9a347d361a37f5aa1080d9d04ac6d37d56c01b0ea92e87ed697a4b478`, 195 lines (byte-identical to the round-8 receipt's recorded state; locators line 142 / line 152 still read the same). The entry still contains no occurrence of the word `kaunakes` (`grep -n -i kaunak` → exit 1, 2026-10-17).

**Question (verbatim, `reports/round-9/targets.json`):** "Check its kaunakes or tufted/skirt-dress terminology against a dated object or scholarly source; distinguish modern/Greek descriptive naming, pictured texture and actual fibre/garment construction."

## Strategy — the angle round 8 did not use

Round 8 worked from reference works, museum notices and a 2023 museum-study article, and closed with three items unread: Breniquet 2016 (Cairn/JSTOR/ResearchGate blocked), the LSJ papyri, and the fibre question. This shard did not re-try the blocked hosts; it went to **digitised-volume full text and French full-text repositories** the earlier rounds had not touched:

- **archive.org item scans** (the DLI copy of JRAS 1931; the scan of Heuzey's 1902 Louvre catalogue) — the *early philological literature* behind the term, which round 8 only knew through later relays;
- **Persée** document full text (Parrot's 1935 Mari excavation report);
- **Crossref / OpenAlex / HAL APIs** to size the modern literature and to bound where Breniquet 2016 exists and where it does not.

## Retrievals (all read 2026-10-17; full URLs, locators and OCR notes in the JSON)

**A1. Przyluski 1931, "Une étoffe orientale, le kaunakes", JRAS 63(2): 339-347** — full text from the archive.org scan of the 1931 volume (item `in.ernet.dli.2015.70576`; `djvu.txt` 2,081,613 bytes, HTTP 200; 23 `kaunak` matches; TOC line 101 lists the article). This is the article whose existence round 8 knew only as a citation inside Jaramago 2023. What it contains, first-hand:

- Heuzey's technical conclusion, reproduced by Przyluski (p. 341): the garment "était une étoffe d'un grand prix, chaude et très velue, dont la laine tombait en longues mèches frisées", belonging to "le même groupe de tissus que les tapis"; the scholiast on Wasps understood "des mèches saillantes et tortillées, produites par la trame de l'étoffe" (p. 340).
- The classical locus pinned: Pollux, *Onomasticon* VII.60 ("Βαβυλωνίων δ' ἐστὶν ὁ καυνάκης") and Aristophanes, *Wasps* 1131-1156; Heuzey 1887 = RA 3e sér. t. IX, p. 257 sqq.
- **The origin of the "Akkadian/Sumerian kaunakes" claim**: Przyluski quotes Langdon (JRAS 1920, 326-9) verbatim at p. 346 n. 2 — "The Sumerian word gu-en is always employed in the texts, never the Semitic naḫlaptu or aṣit kikadi … this should be guennakku, guannakku, the original of the Greek καυνάκης" — and then argues the opposite: an Iranic *gaunaka from *gaona* "hair", supported by Pali *gonaka* "a woollen cover with long fleece" (Rhys Davids & Stede; p. 343). Conclusion (p. 347): the Greek/Latin/Indo-Aryan words "s'expliquent tous par un dérivé iranien *gaunaka".
- **Consequence for the entry:** what modern compilations relay as a flat "Akkadian TÚGGU-NAK-KU" equivalence is a *1920 hypothesis*, contested already in 1931 and hedged by CAD ("foreign word", "possible connection") in round 8. The entry's decision not to use the term is positively motivated, and the term's ancient referent is a costly long-locked wool wrap of Babylonian/Persian make — not the Early Dynastic sculpted skirt.

**A2. Heuzey 1902, *Catalogue des antiquités chaldéennes* (Louvre)** — full text from the archive.org scan (item `cataloguedesanti00muse_0`; `djvu.txt` 466,874 bytes; 26 `kaunak` matches). Two entries read:

- **no. 12** (printed pp. 121-125) — the Dou-dou relief from Tello, dated by the eponymous priesthood ("Son nom, qui se lit Dou-dou, reparaît sur le célèbre vase d'argent du patési Entéména … un véritable sacerdoce éponyme, qui fixe la date des deux objets"), shows a figure "vêtu à mi-corps du châle de kaunakès". The modern Louvre notice (round-8 R8-F02-P5) cites this same entry for inv. AO 2354 — and calls the garment a *jupon* (skirt). One object, two catalogue generations, two garment-form descriptions: the label is classificatory, not a native term.
- **no. 66, "Vêtement de kaunakès"** (printed pp. 103-104; found in the palace of Tello): Heuzey's own reading is explicitly about representation — "j'ai reconnu une **façon conventionnelle** de représenter les longues boucles … de l'étoffe appelée kaunakès", and he warns that on cylinder seals "l'exiguïté des représentations l'a fait prendre pour une robe à tuyaux ou à volants". His note catalogues the variants by period: "nᵒˢ 5, 215, 224 (façon primitive), 82 (façon très archaïque), 8, 10, 12, 66, 67 (façons archaïques et conventionnelles), 27, 226 (façon soignée), 24, 25, 28, 89 (façon simplifiée)" — plus the classical passages (Aristophanes *Wasps* 1131-1156; Pollux VII.60) and the Heuzey 1887 reference.

**A3. Parrot 1935, "Les fouilles de Mari", Syria 16(2): 117-140 (Persée, DOI 10.3406/syria.1935.3820)** — the excavator's description of statuette M.164: "Le personnage a le torse nu, ayant comme vêtement le **jupon kaunakès à cinq rangs**." Rows are counted; no fibre is stated. A second first-hand object description from a dated excavation.

**A4-A6. Index/metadata layer:** the whole indexed literature titled "kaunakes" is 5 Crossref records / 7 OpenAlex works; the 2023 Egyptian journal article (Aswan University) still describes the Sumerian garment with Greek-derived vocabulary ("kaunakes") and a Greek analogy ("flocata") in its own abstract; HAL holds a record of Breniquet 2016 with **no deposited full text** (`openAccess_bool: false`, no files), OpenAlex registers **no open-access location** for it.

## Leg coverage

| Leg | Status |
|---|---|
| Modern/Greek descriptive naming vs native terminology | **retrieved first-hand** (A1 Pollux/Aristophanes/Langdon/Przyluski; A2 classical-passage note; A5 modern usage) |
| Pictured texture vs actual fibre/construction | **documented plurality**, now with first-hand evidence that the texture is a representational convention (A2 "façon conventionnelle" + typology; A3 rows counted, no fibre; A1 classical-period wool cloth) |
| Dated object | **retrieved** — Heuzey 1902 no. 12 (Tello, Entéména-linked dating) and no. 66 (Tello), Parrot 1935 M.164, on top of round 8's Louvre records |
| Breniquet 2016 first-hand text | **not retrieved**, status bounded by evidence (no HAL deposit, no OpenAlex OA location, Cairn/Cairn International 403, ResearchGate 403 inherited from round 8) |

## Remaining unreadable / unretrievable (named exactly)

Breniquet 2016 body text (bounded as above); Cherblanc 1937, *Le Kaunakès* (the one book-length study; no digital copy located — archive.org metadata searches empty, Gallica 403); Langdon 1920 and Heuzey 1887 as standalone texts (read only as cited/quoted by A1 and A2); the EKB/Aswan 2023 article body (journal host DNS-fails from this environment); the exact printed folio of the Parrot sentence (`pageId T1_118` only); fibre of any specific object (no source identifies it from textile evidence).

## Discovered access failures (all with attempt + status in the JSON)

HAL file downloads → Anubis bot-check interstitial (HTTP 200, HTML; two URL forms); cairn-int.info → 403; Persée `docAsPDF` → 403; Gallica SRU → 403 (twice); EKB journal (PDF and landing) → DNS resolution timeout (three attempts); Google Books API → 429 (three queries); archive.org FTS hosts → NXDOMAIN; Cambridge Core IRAQ page → 429.

## Reading

**Whole-claim reading: partial-support-or-better.** The row's guardrail ("carved texture does not uniquely establish fleece, woven pile, tufting, or construction") now has first-hand support on both sides of the question: the naming separation (Greek-derived label; the native-term equation is a contested 1920 hypothesis) and the representation separation (the Louvre's own catalogue calls the carved texture a convention and catalogues its variants by period; excavators count rows and state no fibre). No retrieved passage contradicts the row; nothing here edits the entry. Raw labels are preserved untouched (round-6 worker: *supported / whole-bounded-claim*; round-6 reconciled: *unresolved*; round-8 receipt: *resolved for the object/scholarly legs, Breniquet 2016 unread*).

**Sibling shards:** `R9-F02a-receipt.json` (primary-source/museum hunter) was present at write time and covers the museum-record and lexicographic legs (CAD *aguhhu*, further Louvre objects); this shard deliberately did not duplicate its fetches and contributes the 1887-1935 printed-literature full texts, which no other shard on this residual retrieved. `R9-F02b-receipt.json` (scholarly-fulltext hunter) landed after this receipt was written; its own leg is the specialist-paper search. Neither sibling touched the printed-literature route used here.

## Verification

- Self-check: `python3 -c "import json;d=json.load(open('reports/round-9/freshness/R9-F02c-receipt.json'));print(d['id'],d['residual_id'],len(d['retrievals']),sum(len(r.get('quoted_passages',[])) for r in d['retrievals']),len(d['access_failures']))"` → `R9-F02c R9-R8-F02 6 13 9`.
- Acceptance-runner conformance (read-only import of `reports/round-9/run-validation.py`, `main()` not invoked, no writes). Observed with the documents bound at that moment (this receipt, `R9-F02a-receipt.json`, `audit.md`): 3 documents, 53 nested retrieval units, 28 passages, **20 classified primary/scholarly**, 0 documented-failure gaps, disposition class *partial-or-better* read from this receipt's `reconciled_disposition`, limit-evidence tokens 1,382, no claim-level label disagreements, no runner problems. Re-checked after `R9-F02b-receipt.json` landed: 4 documents, 71 retrieval units, 52 passages (**44 primary/scholarly**), 1,801 limit-evidence tokens — the row's score-0 label then resolves to F02b's longer `reconciled_disposition` string, the same class (partial-or-better), with no fail-closed disagreement between the sibling labels and this receipt's.
