# R8-F02 — freshness receipt: kaunakes / tufted skirt-dress terminology

- Round: 8 (2026-10-17) · Claim: F / freshness · Worker: FRESHNESS R8-F02
- Prior row: `R6-02-B` (disposition `unresolved`) · Prior ledger: `corpus/lessons/round-6-sources/02.json`
- Entry under test: `corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md` (sha256 `bf6c92f9a347d361a37f5aa1080d9d04ac6d37d56c01b0ea92e87ed697a4b478`, 195 lines)
- JSON companion: `reports/round-8/freshness/R8-F02-receipt.json`

**Question.** Check its kaunakes or tufted/skirt-dress terminology against a dated object or scholarly source; distinguish modern/Greek descriptive naming, pictured texture and actual fibre/garment construction.

**Prior limits being tested.** "Named books, Breniquet's article and first-hand dated-object texture descriptions were not retrieved. Tertiary object mentions do not satisfy the requested object/scholarly leg."

## What changed this round

Round 6's residual was an unretrieved object leg plus an unretrieved scholarly leg. Both are now retrieved fresh, and the naming question is answered against primary/reference works rather than tertiary relays:

1. **Dated object, first-hand.** Louvre notice AO 17551 (Ebih-Il, Dynastic IIIB, ~2400 BCE): *"orant aux mains jointes (kaunakès, tabouret : vannerie) … vêtu d'une jupe de type kaunakès"*, Akkadian votive inscription. Second record: Louvre notice AO 2354 (Relief de Dudu, Enmetena, ~2400 BCE): *"le prêtre Dudu vêtu d'un jupon kaunakès"*, Sumerian inscription. Neither notice states fibre or construction.
2. **Reference-work primary (the citation behind the encyclopedias).** CAD vol. 5 (G), p. 134, s.v. **gunakku** (official ISAC PDF downloaded, page located by its printed number): *"gunakku s.; (a cloth or garment); LB\*; foreign word"* — one attestation, a Late Babylonian legal text (BRM 2 50:18), with *"For possible connection with Greek kaunakes and Aram. gonakka cf. Meissner"*. The flat "Akkadian: TÚGGU-NAK-KU" in Wikipedia is a tertiary flattening of a hedged entry.
3. **Greek label, primary.** Aristophanes, *Wasps* 1137 (422 BCE, Greek text retrieved): *"οἱ μὲν καλοῦσι Περσίδ' οἱ δὲ καυνάκην"* — the label's ancient referent is a costly wool garment *"woven in Ecbatana"* (1143, 1147–1149). LSJ s.v. καυνάκης: *"thick cloak … said to be of Persian or Babylonian make"*, cited to Ar. V.1137, Men. 972, Arr. An. 6.29.5, Poll. 7.59 and 3rd-c. BC papyri.
4. **Scholarly leg (peer-reviewed, open access).** Jaramago 2023, *Boletín del Museo Arqueológico Nacional* 42/2023, fn. 26 (p. 469): *"En cuanto al término sumerio o acadio para denominar esta prenda, nos es desconocido"* — the native term is unknown; cites CAD vol. 5 p. 134 s.v. gunakku (independently matching item 2). It quotes Breniquet 2013:5 that the material cannot be securely identified, Kawami 2018:675 (*"flounces or perhaps lappets"*) and Breniquet 2016:9's hedged Mari candidate *aguhhum* ("pourrait …", archaic/liturgical use).
5. **Native lexicon, primary.** ETCSL 1.4.1, lines 20–25: garments named in their own terms (*pala* dress, turban, wig, beads, pectoral, ring) — no Greek-derived label.
6. **Prior main source rechecked.** FIT "Kaunakes" still resolves and still separates form (Boucher: *"referred not to a material but to a form"*), competing texture readings (Tortora: sheepskin vs tuft-simulation) and one construction proposal (Kemper).

## Fresh retrieval index

| rid | kind | source (accessed 2026-10-17) |
|---|---|---|
| P1 | reference-work primary | CAD vol. 5 (G) p. 134, s.v. gunakku — https://isac-assets.s3.amazonaws.com/isac-publications/cad_g.pdf |
| P2 | reference-work primary (Greek) | LSJ 1940 s.v. καυνάκης — https://www.perseus.tufts.edu/hopper/text?doc=Perseus%3Atext%3A1999.04.0057%3Aentry%3Dkauna%2Fkhs |
| P3 | primary text (422 BCE) | Aristophanes, Wasps 1136–1149 — https://reader.humanitext.ai/en/read/urn:cts:greekLit:tlg0019.tlg004.humanitext-grc2:1113-1189 |
| P4 | dated object | Louvre AO 17551 (Ebih-Il) — https://collections.louvre.fr/en/ark:/53355/cl010120528 |
| P5 | dated object | Louvre AO 2354 (Relief de Dudu) — https://collections.louvre.fr/ark:/53355/cl010121765 |
| P6 | dated object (API) | Met 59.2, ca. 2090 BCE — https://collectionapi.metmuseum.org/public/collection/v1/objects/329072 |
| P7 | dated object | Ministère de la Culture, Ebih-Il — https://archeologie.culture.gouv.fr/mari/en/statue-ebih-il |
| P8 | secondary-scholarly | Jaramago 2023, MAN Boletín 42, fn. 26 — https://www.man.es/man/dam/jcr:cb411f22-9ac9-447b-a42e-59c3239a1996/2023-bolman-42-27-jaramago.pdf |
| P9 | primary text (Sumerian) | ETCSL 1.4.1, lines 20–25 — https://etcsl.orinst.ox.ac.uk/section1/tr141.htm |
| P10 | tertiary (prior source) | FIT "Kaunakes" recheck — https://fashionhistory.fitnyc.edu/kaunakes/ |
| P11 | tertiary (relay caution) | Wikipedia "Kaunakes" — https://en.wikipedia.org/wiki/Kaunakes |
| P12 | tertiary | Wikipédia (fr) "Kaunakès" — https://fr.wikipedia.org/wiki/Kaunak%C3%A8s |

All twelve returned a substantive passage (`retrieved_passage: true`).

## Support scope vs whole-claim support

- **Passage support (per passage, not upgraded):** P1–P5, P8, P9 are the load-bearing fresh passages; P6/P7 are object metadata; P10 is a recheck; P11/P12 are tertiary corroboration and are explicitly not used as support for the entry.
- **Whole-claim support (reconciled judgment):** the bounded row at entry line 142 plus its limit column is **supported**, now with the dated-object leg (P4, P5) and the scholarly leg (P8) that round 6 recorded as missing. The entry's avoidance of the word "kaunakes" is positively motivated by P1–P3, P8: the label is Greek, its Akkadian counterpart is a hedged Late Babylonian loanword, and the native term for the garment is reported unknown. No retrieved passage contradicts the row.
- **Locator drift recorded and explained:** round-6 ledger locators sit +3 lines from the current file (row now line 142; Gudea statues 144; institutional textile records 145; craft rule 152; dating spread 190); `git diff` against the baseline shows the shift is exactly the three frontmatter lines added by the round-8 metadata pass (receipts: `reports/round-8/metadata/m04-civ-58-76.md`), and the file's sha256 still matches the hash recorded at recheck. Negative sweep: `grep -n -i "kaunak" …mesopotamia-sumer-akkad.md` → no matches (exit 1, 2026-10-17).
- **Acceptance conformance (2026-10-17, no writes):** importing `reports/round-8/run-validation.py` and running its F-check functions reports, for R8-F02, shape `retrieved`, separation `True`, and 12 detected passages (all ≥ `F_MIN_TOKENS`) plus 12 documented failures; the whole-claim F check reports 0 failures across all 15 rows.

## Access failures (attempted command + status, 2026-10-17)

- Breniquet 2016 full text: Cairn `shs.cairn.info` **403**; JSTOR `stable/pdf/44646389.pdf` **Client Challenge**; ResearchGate **403**. → Breniquet remains unread; P8 supplies page-referenced second-hand quotations only.
- LSJ.gr **403** (LSJ obtained from Perseus instead).
- Perseus search **503** after ~190 s; first LSJ attempt **503** (retry succeeded).
- papyri.info (search and `ddbdp/p.cair.zen;48`) and Scaife Viewer: **bot-check / Anubis interstitials**, no content — the LSJ-cited 3rd-c. BC papyri stay citation-only.
- scholar.archive.org: rate-limit page. Wikipedia `action=raw`: network error (article page retrieved instead).
- Legacy `oi.uchicago.edu` CAD path: **404**; current ISAC S3 asset downloaded successfully.

## Reconciled disposition

**`resolved`** for the residual R6-02-B object/scholarly legs. Not resolved by this receipt: Breniquet's own article text (unread), the LSJ-cited papyri (citation-only), and fibre/construction for any specific object (an open plurality by design, exactly as the entry's limit column requires). No entry edit is proposed; raw round-6 worker/parent labels are preserved verbatim in the JSON companion.

## Reproduction

```bash
# CAD entry (P1)
curl -sSL -o cad_g.pdf https://isac-assets.s3.amazonaws.com/isac-publications/cad_g.pdf
pdftotext -layout cad_g.pdf cad_g.txt   # entry on the page whose printed number is 134 (dump lines 9293-9303)
# self-check of this receipt
python3 -c "import json;d=json.load(open('reports/round-8/freshness/R8-F02-receipt.json'));print(d['id'],len(d['fresh_retrievals']),sum(1 for r in d['fresh_retrievals'] if r['retrieved_passage']),len(d['access_failures']))"
# expected: R8-F02 12 12 12
```
