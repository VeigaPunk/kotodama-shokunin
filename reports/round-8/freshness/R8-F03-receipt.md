# R8-F03 — freshness receipt (round 8 re-check of R6-05-B)

- **Prior row:** R6-05-B (`corpus/lessons/round-6-sources/05.json`), prior disposition **unresolved**.
- **Entry:** `corpus/knowledge/civilizations/anatolia-hittite.md` — sha256 `5a2a3981a11f19500a224daf53a714d62624db4ac90eb17f9858b184cf1ddf84` at the start of the retrieval session, identical to the round-6 baseline revision `e7ca0fa` (body unchanged by this receipt). During this round the metadata-sweep shard added three frontmatter keys (`source:`, `verified-at:`, `recheck:`), so the working-tree hash is now `a8e421f7…` and body rows shift +3; `git diff` shows only those 3 insertions. Locators below are the post-sweep working-tree numbers; the pre-sweep equivalents are given in the JSON's `entry_post_filing_change`.
- **Round-8 head at receipt:** `cf338a713060f274269cdacb18cdc0085bb06aeb`; baseline revision `e7ca0faeb6680fa9891b907be628d9db578c28f4`.
- **Question:** Check one dated divine/royal headgear, pointed-cap or horned-crown identification in the entry; distinguish depicted rank, deity/king identification and earlier Hattic or later Neo-Hittite comparators.
- **Round-8 result:** `supported` (all three legs have fresh retrieved passages). Raw round-6 worker label `partial-support` preserved; reconciled dispositions belong to `reports/round-8/freshness/reconciliation.json`.
- **Machine receipt:** `reports/round-8/freshness/R8-F03-receipt.json` (15 passage legs, 10 additional retrievals, 4 negative sweeps, quote-fidelity and quote-verification blocks).

## 1. Dated divine/royal headgear identification — the horned pointed cap

Bonatz, Dominik, "The Iconography of Religion in the Hittite, Luwian, and Aramaean Kingdoms", *Iconography of Deities and Demons (IDD), Electronic Pre-Publication*, last revision 26 February 2007, University of Zurich — fetched live 2026-10-17, HTTP 200, 209300 bytes, sha256 `3315a9bc…6aa`; text layer `pdftotext -layout`.

> "For the most part the male gods wear a short kilt and, corresponding to their hierarchical standing, a single or multiple horned, pointed cap, the typical headgear of Hittite deities since the Old Kingdom (cf. five-faced seals, 16th cent. [BOEHMER/GÜTERBOCK 1987: fig. 39 and no. 148])." — §1.3, printed p. 5

> "The goddesses are uniformly dressed in a long pleated robe and wear a cylindrical crown, which is turreted only in the case of the major goddesses." — §1.3, p. 5

> "Behind the mountain gods, twelve nameless gods appear wearing kilts and single horned, pointed caps, and shouldering scimitars." — §1.3, p. 6

> "In contrast to the other goddesses on the east side of the chamber, she wears the horned crown of a male god, probably because of her warlike aspects." (Shaushka) — §1.3, p. 6

So the horned pointed cap is a **rank marker with a gradient** (single vs multiple horns), dated to the Yazılıkaya program under Tutḫaliya IV, with an explicit earlier comparator *inside* Hittite tradition (Old Kingdom five-faced seals, 16th cent.). This supports entry lines 123 (horned divine headdress), 135 (male divine figures) and 136 (female divine figures).

## 2. Deity/king identification — including the documented problem cases

> "Both wear the long robe and rounded skullcap, and both carry the lituus. They are distinguished only by different hieroglyphic inscriptions and the winged sun disc, which is attached to the head of the sun god but absent on the king (see also the kings in the reliefs of Alaca Höyük [fig. 8], Sirkeli [BITTEL 1976: fig. 195], and the seals of Muwatalli [BERAN 1967: nos. 250–252])." — IDD §1.4, p. 8 (Tutḫaliya IV on Yazılıkaya relief nos. 64 and 81 vs the sun god on relief no. 34)

This closes the round-6 limit "royal-cap contrast … was not inspected" and supports entry line 137 (royal rounded cap). The same chapter keeps the distinction honest:

> "In fact, the distinction between god and king often remains problematic. For example, in the case of the newly discovered rock relief of Kurunta, King of Tarhuntassa, at Hatip DİNÇOL (1995: 162–163, fig. 1, pls. 1–2) again identifies the figure with bow, lance, and high pointed horned cap as god. But the name of Kurunta written next to this figure could also refer to the image of the ruling monarch (EHRINGHAUS 2005: 101–107)." — §1.4, p. 8

> "The definite proof that in some cases the leavings [sic; evidently 'living ones'] can also be depicted as gods is given by the seal impressions of the crown prince Urhi-Teshub, found in the Nişantepe archive of Boǧazköy (fig. 14; HERBORDT 2005: 69–71, fig. 46a-d, cat.-nos. 504–505, 507), which show him wearing the high pointed horned cap and embraced by the god Sharruma." — §1.4, p. 8

> "This gesture, which is also depicted on relief no. 81 in Yazılıkaya, is to be understood not only as tutelary, it also expresses the image of the king striding alongside the god (cf. ORTHMANN 1983: 431)." — §1.4, p. 7 (supports entry line 126, the Šarruma/Tudḫaliya IV embrace; the god's name is carried by the re-fetched Wikipedia caption below)

**Consequence for the entry's wording:** "Horns mark divine status in characteristic representations" (line 123) is passage-confirmed, but the brake should be read as *with documented royal/ambiguous exceptions* (living crown prince in the horned cap; Hatip relief with two scholarly readings), not as a strict god-only rule.

## 3. Later Neo-Hittite comparators (dated twice) and the earlier-comparator leg

**Malatya Lion Gate reliefs — late 12th or 11th cent. (scholarly):**

> "He wears either a high conical double-horned crown or a rounded skull-shaped hairstyle, which may be a close-fitting cap with a pointed curl or volute. The distinction may reveal the altered status of a worshipped king, who after death is transformed into a tutelary god acting as an intermediary between the gods and the earthly world on behalf of his dynasty (cf. VAN LOON 1991: 4)." — IDD §2.1, p. 10 (ruler PUGNUS-mili of Melid)

**İvriz — 738–710 BCE (monument database with Hawkins' inscription translation):**

> "The god wears a horned helmet, a symbol of divinity. The figure of the king, which is considerably smaller than that of Tarhunza, is elaborately dressed and appears in a worshipping stance. King Warpalawa of Tuwana is known from Assyrian sources as Urballa. He was in power at least in between 738-710 BCE; thus, the monument is dated to the second half of the 8th century BCE."
> "The three-line Hieroglyphic Luwian inscription in front of the god is translated (by Hawkins) as: 'This (is) the great Tarhunza of Warpalawa. For him let him/them put long(?) Sahana(?).'" — hittitemonuments.com/ivriz/ (HTTP 200, 12050 bytes, sha256 `19bb7858…ac91`)

**Carchemish III — primary excavation report (object level):**

> "The goddess of the Processional Entry (B. 19a) has the same dress and wears no horned crown of divinity, but she is at least enthroned on a lion, whereas here we see a simple chair such as would suit a human being. On the evidence of the inscription Mr. Barnett concludes that the figure is presumably a priestess and certainly a mortal and a member of the royal family of King Luhas (v. p. 260)." — ch. VIII, printed p. 166

> "part of a horned crown from a statue of a god which may have belonged to the same figure (B. 63a)." — finds list, printed p. 174

> "Outside the north wall was found a basalt slab with a relief of a bull-legged deity grasping a tree; he wears the horned crown and a broad belt with hanging tassel but apparently no other garment, and is ithyphallic. The face has been deliberately obliterated (B. 49c)." — Water Gate chapter

Woolley, C. L. (with R. D. Barnett), *Carchemish … Part III: The Excavations in the Inner Town* (London 1952); Internet Archive scan `carchemishreport03brituoft`, HTTP 200, 20335518 bytes, sha256 `85f6806e…a5d7`. **Iron Age horizon — must not be projected back onto the Empire** (entry line 49 terminology trap).

**Earlier-comparator leg (partial):** dated pre-Hittite-period headgear *objects* at Alaca Höyük — "Fourteen shaft-grave 'Royal Tombs' (2850–2450 BC)" with the dead "richly adorned with gold fibulae, diadems, and belt buckles" (Wikipedia Alaca Höyük, HTTP 200) and "13 Early Bronze Age 'royal' tombs … dating to the second half of the third millennium b.c. Burial goods included gold diadems and jewelry" (Simpson, ch. 32 in *The Adventure of the Illustrious Scholar*, Brill 2018, HTTP 200). Empire-period Alaca orthostats (1300–1200, Ankara, Museum of Anatolian Civilizations) are the dated royal-cap comparator in the same town. **No Hattic-period horned-cap image was retrieved** (sweep recorded in the JSON); the 'Hattian' ethnic label for Alaca's Early Bronze Age tombs is a modern convention in the cited sources, not something this receipt verifies.

**Textual layers (new this round):**

- KBo 15.15, quoted in Turkish via Kümmel 1967: 136–137 in an Istanbul University dissertation: "Kralın heykeli [ ] krallığın bayram kıyafetlerini giyer, başında ise kalot başlık vardır. Kulaklarında küpe vardır. Ve o ayaklarına Hatti stilinde ayakkabılar giyer." — worker gloss: *the king's statue wears the festival garments of kingship, with a cap ('kalot') on its head, earrings, and Hatti-style shoes*. Same page: "Hitit krallarının tasvirinde, Hitit kralları başlarında iki farklı başlık ile görülebilmektedir: koni biçiminde başlık taşıyan krallar ve takke formunda başlık taşıyan krallar (van den Hout, 1995: 548…)" — *Hittite kings appear with two different headdresses: cone-shaped and skullcap-form*.
- Oreshko 2018, *Journal of Language Relationship* 16/1-2: 104–105: "…vs. Hitt. kupaḫi 'a headgear', which is known to be present also in Hurrian as kuwaḫi" — the *textual garment term* layer the entry's evidence rule asks to keep separate from depicted garments.

## 4. Fresh re-fetch of the round-6 main source

`https://en.wikipedia.org/wiki/Yaz%C4%B1l%C4%B1kaya` re-fetched 2026-10-17 (HTTP 200, 275571 bytes, sha256 `939565a7…1811`). Both round-6 sentences remain visible:

> "The left wall shows a procession of male deities, wearing the traditional kilts, pointed shoes and horned hats."
> "Rock carving in Chamber B depicting the god Sharruma and King Tudhaliya IV, dated to around 1250–1220 BCE"

## 5. Access failures and negative sweeps (commands + status)

| Sweep | Command | Result |
|---|---|---|
| Ivriz page does not describe the king's headgear | `grep -o -i -E 'cap\|crown\|helmet' /tmp/r8f03/ivriz-hm.txt \| sort \| uniq -c` | 1 `helmet` (the god's), 0 `cap`, 0 `crown` |
| IDD chapter has no Hattic headgear witness | `grep -c -i 'hattic\|hattian' /tmp/r8f03/idd-anatolia.txt` | 1 — a Water-god origin sentence, not headgear |
| British Museum object record | `curl -sL -o /dev/null -w '%{http_code}' https://www.britishmuseum.org/collection/object/H_1862-0423-1` | **403** (blocked; no museum record obtained) |
| Bonnet–Ridotto PDF (blocked) | `curl -sL … https://ricerca.sns.it/bitstream/11384/139103/5/Bonnet-Ridotto.pdf` (also with browser UA) | **403 / 403** — a search snippet from this blocked PDF was deliberately **not** used as a passage |
| Acceptance runner not yet present | `ls reports/round-8/ reports/round-8/freshness/` | `run-validation.py` absent at receipt time (O-shard pending) |

## 6. Quote fidelity and verification

Every quote in the JSON was re-checked against the fetched artifact with a 10-gram containment test: 24 quoted segments, 13 fully verbatim under the artifacts' own diacritics/line breaks, 11 differing only by disclosed normalizations (ASCII diacritics for ı/ḫ/ş/ğ; OCR forms `B. 19^`→B. 19a, `B. 49<'/`→B. 49c; Greek κύμβαχος transliterated and its footnote marker dropped; two-column OCR interleaving at "statue of a god which may have belonged"; multi-sentence `...` joins). One real transcription error was found and fixed before filing (IDD fig. 8 caption author `ÖZGÜÇ`). The Carchemish III right-column sentence is stitched from adjacent scan lines; the raw scan reads:

```
                             4. Above the top of the stairs were found fragments
                           of a human arm and hand car\ed in basalt, apparently
                           from a statue in the round of unusually large size (B.
                           636) and part of a horned crown from a statue of a god
                           which may have belonged to the same figure (B. 63a).
```

## 7. Limits (carried and new)

1. **Seeher 2011** (the entry's cited visual authority, bibliography line 28) remains uninspected at plate level; nothing here substitutes for plates.
2. **No Hattic-period headgear image** was retrieved; the earlier-comparator leg rests on pre-Hittite-period Alaca Höyük tomb jewelry (diadems) plus the Old Kingdom seal comparator.
3. **KBo 15.15** is quoted through a Turkish dissertation citing Kümmel 1967: 136–137; the cuneiform autograph and the cited editions were not read, and the Hittite word behind Turkish "kalot" was not retrieved.
4. **Dating discipline:** Carchemish, İvriz and Malatya material is Iron Age / Neo-Hittite; none of it may be projected back onto the Empire period.
5. **Entry wording nuance:** the retrieved scholarly phrase is "rounded skullcap" (entry says "rounded cap"), and the horned cap has documented royal/ambiguous exceptions, so line 123's rule is a characteristic-representation rule, not an exclusive one.
6. **Locator note (corrected):** the round-6 ledger's R6-05-B locators (:120/:123/:132/:134/:46) are correct for the round-6 baseline revision — `git show e7ca0fa:corpus/knowledge/civilizations/anatolia-hittite.md` hashes to `5a2a3981…` and places the same rows at 120/123/132/134/46. This receipt's numbers (123/126/135/137/49) are the post-metadata-sweep working-tree numbers; the +3 shift comes from the three frontmatter keys the sweep added this round, not from a round-6 miscount.

*Accessed-at for all retrievals: 2026-10-17 (session window 20:12–20:20 UTC). Fetched artifacts retained under `/tmp/r8f03/` with the sha256 values recorded in the JSON.*
