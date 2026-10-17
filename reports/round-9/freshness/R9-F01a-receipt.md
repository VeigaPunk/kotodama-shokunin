# R9-F01a — freshness receipt (primary-source / museum-catalogue hunter)

- **Round:** 9 (loop 1 of 3, build round 2 of 4) · **Date:** 2026-10-17 · **Shard:** FRESHNESS R9-F01a
- **Residual:** R9-R8-F01 ← R8-F01 ← prior row R6-02-A (Sumerian–Akkadian contact; scribal survival vs spoken replacement; "which dated text or scholarly passage supports the institutional coupling?")
- **Entry:** `corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md` — sha256 `bf6c92f9a347d361a37f5aa1080d9d04ac6d37d56c01b0ea92e87ed697a4b478`
- **Strategy:** museum catalogue records (Louvre) + the CDLI catalogue itself (artifact JSON API and the full catalogue dump) + the primary text (ATF) + excavation-publication pointers for a sister witness. Disjoint from the round-8 set, complementary to the sibling shard R9-F01b (scholarly fulltext, already present).
- **Outcome:** the round-8 receipt's `to-verify` item — *"Louvre AO 5477 object record (museum accession page)"* — is **closed at catalogue + transliteration level**. Nothing retrieved contradicts the entry.

## 1. What the round-8 receipt could not get, and how it was escalated

| Round 8 state | Round 9 escalation | Result |
|---|---|---|
| Louvre search returned HTTP 429; a guessed ark resolved to a different object ("vase") | direct ark route `collections.louvre.fr/en/ark:/53355/cl010166127` + its JSON API | **retrieved** (HTTP 200) |
| "CDLI search for the same tablet … client-rendered results with no server-side row" | per-artifact JSON route + the full CDLI catalogue dump via the CDLI GitHub LFS copy | **retrieved** — CDLI holds the object as **P220619** |
| no primary text of the object | CDLI ATF of the copy (P220619) and of the composition (P461964) | **retrieved** |
| no excavation-provenienced witness | CDLI P227513, Penn Museum `CBS 02344 (+) CBS 14547 + N 3539`, provenience Nippur | **retrieved at catalogue level** |

## 2. Museum catalogue record — Louvre AO 5477 *(primary, institutional author)*

URL `https://collections.louvre.fr/en/ark:/53355/cl010166127` (machine-readable: `…/ark:/53355/cl010166127.json`), accessed **2026-10-17T20:54:04Z/20:54:05Z**; JSON 5,930 bytes `sha256 e9b0f67e…70aa7`; page 58,975 bytes `sha256 7cb3f261…b5a78`. Record last updated 10.01.2025.

Quoted fields (JSON paths / page sections):

- `description` — *"Précision sur l'objet : Copie d'une inscription votive de Rimush, roi d'Akkad"*
- `displayDateCreated` — *"Akkad : Rimush (Vers 2270 av. J. - C. ; **copie d'époque paléo-babylonienne du début du IIe mill**) et 1ère dynastie de Babylone (-2278 - -2270 et -1894 - -1595)"*
- `inscriptions` — *'"Personne n'avait exécuté (jusqu'à présent) une statue de fer, Rimush, roi de Kish, sa statue de fer exécuta : devant Enlil elle se tiendra…" La statue devait se trouver dans le temple du dieu Enlil à Nippur. Langue : akkadien (bilingue) sumérien (bilingue)* (the first sentence is the catalogue's translation of the text; the second is its placement inference)
- `placeOfDiscovery` / `previousOwner` / `acquisitionDetails` — *"Babylonie = Sumer"* / *"Géjou, Elias Ibrahim"* / *"achat", 1910*
- `bibliography[0..2]` — RIME 2 (Frayne 1993) **E2.1.2.18**; FAOS 7 (Gelb & Kienast 1990) **Rimuš C9 Text D**; Thureau-Dangin, *"Notes assyriologiques. XIII. Deux inscriptions d'Urmuš"*, **RA 8 (1911) 135-142**
- dimensions 12 × 8 × 3.5 cm, argile; on display Richelieu, salle 228, vitrine 2

## 3. CDLI catalogue record — P220619 (`AO 05477`)

URL `https://cdli.earth/artifacts/220619.json` (human page `/artifacts/220619`), accessed **2026-10-17T20:54:06Z**; 4,694 bytes `sha256 a7c94e4d…6d5b`.

- `designation: "RIME 2.01.02.18, ex. 03"`, `museum_no: "AO 05477"`, `dates_referenced: "Rimush.00.00.00"`
- `period: "Old Babylonian (ca. 1900-1600 BC)"`; `collections: Louvre Museum, Paris, France`
- publications: primary **RIME 2** (1993), `exact_reference "01.02.18, ex. 03"`; history **`RA 008 (pp. 135 - 158)`, `bibtexkey Thureau-Dangin1911RA8Notes`, `exact_reference "p. 138ff, AO 5477"`**

**Whole-dump sweep** (bypasses the client-rendered search): `cdli_cat.csv` from `https://media.githubusercontent.com/media/cdli-gh/data/master/cdli_cat.csv` (LFS copy of CDLI's daily dump), 154,768,722 bytes, 353,284 lines, `sha256 2e3232f7…353d09c` — identical to the LFS pointer's declared oid. The single row with `museum_no = 'AO 05477'` (line 69,374):

```
id=69373  id_text=220619  designation='RIME 2.01.02.18, ex. 03'  museum_no='AO 05477'
collection='Louvre Museum, Paris, France'  composite_id='Q000842'
period='Old Babylonian (ca. 1900-1600 BC)'  dates_referenced='Rimush.00.00.00'
primary_publication='RIME 2.01.02.18, ex. 03' (1993)  publication_history='RA 08, p. 138ff'
genre='Royal/Monumental'  subgenre='witness'  provenience/excavation_no/findspot_remarks = empty
```

Sweep result: rows mentioning `2.01.02.18` = **3** — `ex. 03` (P220619, Louvre copy), `ex. 02` (P227513, Penn), and the composite (P461964). Composite `Q000842` = **1** row (the Louvre copy).

## 4. Primary text — the bilingual inscription itself

- **Object (P220619)**, `inscription.atf`: `&P220619 = RIME 2.01.02.18, ex 03 / #atf: lang sux / @tablet / $ (vertical dividing line between Sumerian and Akkadian)` — obverse 1–15 and reverse 1–13 in parallel Sumerian and Akkadian, e.g. `14. igi {d}en-lil2-la2-sze3 %a _igi_-me {d}en-lil2 / 15. i3-gub %a i-za-[az]`; ends `$ rest broken`.
- **Composition (P461964)**, `designation "RIME 2.01.02.18 composite"`, `composite_no Q008372`, `period Old Akkadian (ca. 2340-2200 BC)`; same lines with English renderings: *"1. [ri2-mu-us2] … Rimuš, / 5. [{d}en-lil2-ra] … for the god Enlil / 7. alan an-[na] … a statue of meteoric iron / 14. igi {d}en-lil2-la2-sze3 … in front of Enlil / 15. i3-gub … it (now) stands."*

## 5. Sister witness with an excavated findspot

CDLI **P227513** (accessed 2026-10-17T20:54:08Z; 12,250 bytes `sha256 1a93486c…237a`): `museum_no "CBS 02344 (+) CBS 14547 + N 3539"`, Penn Museum, `provenience Nippur (mod. Nuffar)`, designation includes `RIME 2.01.02.18, ex. 02`; publication history **PBS 4 (1914) 209-215**, **PBS 5 (1914) 036 & pl. 101**, **JCS 32 (1980) 233-246**, FAOS 7 (1990) 213/215/226. (Penn's own record returned HTTP 403 — see §7.)

## 6. The qualification that matters for reuse

The retrieved object is a **palaeo-Babylonian copy of a Rimush composition** (Louvre: *"copie d'époque paléo-babylonienne du début du IIe mill"*; CDLI: period Old Babylonian, `dates_referenced Rimush`). So it is evidence for **scribal copying of an older royal bilingual** — exactly the entry's line 14 rule (*"A first-millennium copy can preserve older tradition…"*) and line 72 staging rule — **not** evidence of Sargonic-era speech. It must not be cited as a contemporaneous Sargonic object.

Entry locators (current file): line 14 coupling rule; line 39 `Contact ecology` row; line 51 *"Sumerian word-signs can be used inside Akkadian writing…"*; line 72 `Stage separately`; line 169 craft-grid row `Ritual language survives vernacular change`; line 30 museum-record method line; line 192 colonial-collection caution (the 1910 purchase from Géjou is an accession, not a findspot).

**Digest drift note:** the round-8 receipt recorded `730e1be8…`; the current digest is `bf6c92f9…` because the round-8 admitted commit `e1694ba` added 3 frontmatter lines and 1 source-shelf line (Quillien 2019) and reworded the Early Dynastic costume row — locators moved 36→39 and 166→169; the `Contact ecology` row text is unchanged.

## 7. Access failures (attempted command + status, all 2026-10-17)

| Attempt | Status |
|---|---|
| `cdli.earth/search?q=AO+5477` | HTTP 200, 1,633,509 bytes, **no server-side result row** (only the default id list; client-rendered table) |
| `cdli.earth/search.json?q=AO+5477` / `?q=zzzznoresultqqqq` / `&format=json` | all HTTP 200 with **byte-identical 109,715-byte payloads** → the route ignores `q` |
| `cdli.earth/api/search`, `/api/v1/artifacts`, `/api/artifacts` | HTTP 404 |
| `cdli.ucla.edu/search/archival_view.php?ObjectID=P464358` | curl (6) could not resolve host |
| `api.cdli.mpiwg-berlin.mpg.de/artifacts?q=…` | curl (6) could not resolve host |
| Gallica SRU (`gallica.bnf.fr/SRU?…`) incl. via FetchURL | HTTP 403 Cloudflare interstitial |
| `catalog.hathitrust.org/Search/Home?…` | HTTP 403 Cloudflare |
| `jstor.org/stable/23284567` | HTTP 200 but 3,038-byte JS/consent shell — no article |
| `archive.org/download/revuedassyriolog0000vsch_djvu.txt` / `…_m7x7_djvu.txt` | HTTP 500 (170 B) / HTTP 403 (4,868 B) |
| `penn.museum/collections/search?keywords=CBS 2344` and `/collections/api/search` | HTTP 403 (961 B) |
| `armep.gwi.uni-muenchen.de/api/documents?cdli=P220619` | HTTP 404 |
| host: `df -i /tmp`, `touch /tmp/_wtest` | inode table 100% full → `curl -o /tmp/…` fails (curl 23); all staging moved to `/dev/shm/kscratch` |

## 8. Negative claims with their sweeps

1. **CDLI has one catalogued witness of composite Q000842** — sweep: full 353,284-line dump scan (`composite_id == 'Q000842'`) → 1 row; `'2.01.02.18'` in designation/primary publication/history → 3 rows.
2. **No archaeological findspot in the Louvre record** — sweep: full JSON field dump; only `placeOfDiscovery 'Babylonie = Sumer'`, purchase 1910 (Géjou); CDLI agrees (provenience/excavation_no/findspot_remarks empty).
3. **No free full scan of RA 8 (1911)** — sweep: `archive.org identifier:revuedassyriolog*` → 15 items (vols 1, 5, 24, 30, 33, 55-57, 58-60, 70-80, 84-86, 93-95, 96-98, 110, 3 unlabelled), none vol. 8; Gallica/HathiTrust 403; JSTOR shell.
4. **CDLI's search surfaces cannot substitute for the dump** — `/artifacts/69373.json` 404 vs `/artifacts/220619.json` 200; `/search.json` ignores `q` (three byte-identical payloads).

## 9. Counting commands

```
date -u                                        -> 2026-10-17T20:48:15Z (start); receipts stamped 20:51Z–20:54:09Z
curl … collections.louvre.fr/ark:/53355/cl010166127.json -> 200  5930 B  sha256 e9b0f67e…
curl … collections.louvre.fr/en/ark:/53355/cl010166127   -> 200 58975 B  sha256 7cb3f261…
curl … cdli.earth/artifacts/220619.json                  -> 200  4694 B  sha256 a7c94e4d…
curl … cdli.earth/artifacts/461964.json                  -> 200  3543 B  sha256 f9b1c2f7…
curl … cdli.earth/artifacts/227513.json                  -> 200 12250 B  sha256 1a93486c…
curl … wikidata.org/…/Q87473226.json                     -> 200 11177 B  sha256 59a47cbf…
curl … media.githubusercontent.com/media/cdli-gh/data/master/cdli_cat.csv -> 200 154,768,722 B
sha256sum csv -> 2e3232f7…353d09c (= LFS pointer oid) ; wc -l -> 353,284
sha256sum corpus/…/mesopotamia-sumer-akkad.md -> bf6c92f9…4b478
git show e1694ba --stat -- corpus/…/mesopotamia-sumer-akkad.md -> 1 file changed, 3 insertions(+)
```

## 10. Limits that remain (to-verify)

- Thureau-Dangin 1911 (RA 8, 135-142 / "p. 138ff") is attested by two independent catalogue records only — **body text unread**.
- RIME 2.01.02.18 (Frayne 1993) and FAOS 7 Rimuš C9 (Gelb & Kienast 1990) — **print editions not inspected**.
- The ATF is CDLI's edition of record and was **not collated against the tablet, its photographs, or a print edition**; the tablet is broken.
- Penn excavation-series pointers (PBS 4/PBS 5/Michalowski JCS 32) come from CDLI's publication history — **not read**; Penn's own record 403s.
- No claim about Sargonic-era speech, pronunciation, or a vernacular-loss date is made here.

## 11. Disposition

- **Round 8:** resolved-passage-level; object witness a tertiary pointer; object record `to-verify`.
- **Round 9 (this shard):** object-level retrieved — Louvre catalogue record, CDLI catalogue record P220619, bilingual ATF of copy and composition, Nippur-provenienced sister witness; the `to-verify` item is closed at catalogue/transliteration level.
- **Raw labels preserved:** round-6 `supported / whole-bounded-claim` and the round-8 reconciled `unresolved` and `resolved-passage-level` are copied, not rewritten; this shard does not re-adjudicate them. Sibling shard `R9-F01b-receipt.json` covers the scholarly-fulltext strategy.
