# R9-F03a receipt — primary-source/museum-record hunt (round 9, freshness[2])

- **Shard:** FRESHNESS **R9-F03a** — strategy: *primary-source/museum-record hunter*. Not the scholarly-fulltext
  hunter (b), the alternate-angle hunter (c) or the independent verifier (V02); their material is theirs.
- **Residual:** `R8-F03` (prior row `R6-05-B`), declared unresolved in `reports/round-9/targets.json`
  freshness[2]. **Question:** *"Check one dated divine/royal headgear, pointed-cap or horned-crown
  identification in the entry; distinguish depicted rank, deity/king identification and earlier Hattic or
  later Neo-Hittite comparators."*
- **Entry:** `corpus/knowledge/civilizations/anatolia-hittite.md` — sha256
  `a8e421f7118eb956418a2abbeb24890cfa05e1b35de41f7db72dfa6b9f7332a0` (equals round-8's post-sweep hash;
  `git status --porcelain <file>` empty at 20:51:18Z, so this receipt attaches to committed text). Locators
  used: line 123 (*Horned divine headdress*), 135 (*Male divine figures in imperial relief*), 137 (*Royal
  ceremonial representation*, “rounded cap”), 49 (terminology trap), 28/141 (Seeher plates not inspected).
- **Window:** 2026-10-17, 20:47–20:53 UTC, all fetches live from this host.
- **Scratch:** `/var/tmp/r9f03a/` — `/tmp` was unusable for the whole window (`df -i /tmp` → 0 free inodes,
  `1048576 1048576 0 100%`; `mkdir -p /tmp/r9f03a` → *No space left on device*). Artifacts: `/var/tmp/r9f03a/ev/`
  with `SHA256SUMS`; every receipt line below carries status + bytes + sha256.
- **Result (this shard's own):** **partial-support**. The dated headgear identification and the deity/king
  ambiguity are now supported **at museum-object-record level**; the later Neo-Hittite half is dated at
  record level but headgear-silent; the earlier-Hattic leg is **not** reached (deeper-limit section).
- **Raw round-6 label preserved:** `supported` / support_scope `partial` (as carried in
  `reports/round-8/freshness/reconciliation.json` row R8-F03). Never rewritten here.

## 1. New museum-record legs (none of these passages appears in the round-8 receipt)

### 1.1 Cleveland 1971.45 — a dated horned crown, accessioned and museum-described

`https://openaccess-api.clevelandart.org/api/artworks/1971.45` → **HTTP 200, 16000 bytes, sha256
`30e4e3444fc30eb6dfb265d85d0238a866338789ab5a6eaba12ddbac9d8759e4`**
(`/var/tmp/r9f03a/ev/cle1971.45.json`); human page `https://clevelandart.org/art/1971.45`.

| field | value |
|---|---|
| accession | **1971.45** ("Priest-King or Deity") |
| date | **c. 1600 BCE** (API earliest −1605 / latest −1595) |
| culture | Hittite, North Syria |
| medium / size | basalt with bone eyes (left ancient, right restored); 87.6 cm (34½ in.) |
| credit / location | Leonard C. Hanna Jr. Fund; on view 102A Ancient Near East; CC0 |

> “This large basalt sculpture is exceptionally rare in depicting a Hittite god or priest-king wearing a
> **horned conical crown**, false beard, and long robe.”

*Supports:* the residual's first clause at object level — a **dated, accessioned, headgeared** Hittite figure —
and its second clause in the museum's own voice: the object title is *Priest-King **or** Deity*. *Does not
support:* it is not the imperial Yazılıkaya program and carries no hieroglyphic figure label.

### 1.2 Cleveland 1985.70 — dated deity/king separation (and a separate priest role)

`…/api/artworks/1985.70` → **HTTP 200, 6017 bytes, sha256 `0880e7d7607246078747b42d178b0798f643be8d6beb410fafe6f6e73f9065c6`**.
Date 1400–1200 BCE, Eastern Turkey, Hittite.

> “The scene on the front of this vase shows a **seated god or king** holding a drinking vase in the form of a
> stag. … The standing figure is a **priest** pouring a liquid offering.”

*Supports:* the role-separation clause — the museum keeps god/king open and names a third role in the same
scene. *Does not support:* no headgear is described on any figure.

### 1.3 Neo-Hittite later comparators — dated records, headgear-silent

| museum / id | date | find-spot (notice) | notice excerpt | HTTP receipt |
|---|---|---|---|---|
| Louvre **AO 11073** (*Orthostate : génie ailé*) | Néo-hittite −1000/−700 | Tell Halaf, palais de Kapara (mur ouest tour III, pierre 99); 1911–1927; Baron Oppenheim | `Inscription : ("Temple du dieu de l'Orage")`; on display Salle 302 Aile Sully | 200, 51590 B, `9444d7dc…a82a` |
| Louvre **AO 11072** (*Orthostate : archer*) | Néo-hittite −1000/−700 | same palace (mur est tour IV, pierre 144) | `Inscription : (Palais de Kapara, fils de Hadianu)` | 200, 52369 B, `5d3ea9c8…0806` |
| Louvre **AO 8191** (stèle/orthostate, reclining woman) | Néo-hittite −1000/−700 | Zendjirli, 1888–1891; donated 05/1922 | — | 200, 48585 B, `f0db48e4…586c` |
| Cleveland **1973.19** (*Banquet Pyxis*) | 800–750 BCE | Anatolia, Neo-Hittite | (no description field) | 200, 4019 B, `b9d5dfd6…d53f` |

*Supports:* accessioned, dated museum notices with inscriptions and physical dimensions exist for the later
horizon — the record type the entry's line 129 asks for. *Does not support:* **none** of the notices mentions
a headdress; the later-comparator half is dated-record-only, not a headgear witness.

### 1.4 The earlier horizon and the display locations (state records, gallery-level)

- **Hittite Monuments, Alacahöyük** — `https://www.hittitemonuments.com/alacahoyuk/` → 200, 28578 B,
  `e5fd321c…8416` (byte-identical to round 8's artifact for this URL; re-fetched and hashed this round):
  “Excavations reveal that the site must have been an important settlement already in **pre-Hittite** times.”
  and “The sphinxes and the orthostats that were found in situ have been replaced with replicas and **moved to
  the Anatolian Civilizations Museum in Ankara**.” — pins the dated Empire-period Alaca orthostats (line 137's
  comparator class) to a named museum, but describes no headgear.
- **Turkish Ministry of Culture — Boğazköy Museum (BOG01)** — 200, 52602 B, `360d338d…1722`: gallery-level
  only; “Among the exhibits is the Boğazköy Yerkapı Sphinx, which was returned by the Berlin museum and has
  been on display at the Boğazköy Museum since 26 November 2011”; “displays on Hittite religion … with
  accompanying panel information”. No object numbers, no headgear.
- **Turkish Ministry of Culture — Alacahöyük Museum (ALC01)** — 200, 51631 B, `cdef33fa…8cd3`: “Alacahöyük was
  a significant religious and artistic centre during the Bronze Age and Hittite period”; no object list.
- **Met 55.137.14 (Hattian axe, ca. 2300–2000 BCE, Central Anatolia)** — read via FetchURL; page now reads
  “**Restituted.** This artwork was restituted in September 2026. It is no longer in the museum's collection.”
  Confirms “Hattian” as a museum classification for EBA III Anatolia — and that this particular record cannot
  serve as a gallery-verifiable headgear witness.

## 2. Negative sweeps (command + result)

| Sweep | Command | Result |
|---|---|---|
| Louvre notices have no headgear vocabulary | regex word-boundary count over the three extracted notices for {horn, crown, cap, headdress, helmet, coiffure, bonnet, casque, couronne, corne, tiara} | **0 hits per term in all three** |
| State/monument pages have no headgear vocabulary | same count over `tr_bogazkoy_museum.html`, `tr_alacahoyuk_museum.html`, `hm_alaca.html`, `hm_yazilikaya.html` (+ Turkish `boynuz`, `başlık`, `takke`) | **0 hits per term in all four**; the Yazılıkaya page is 1808 chars of text and discusses no relief headgear |
| Yazılıkaya has no accessioned-object / relief-level record | `curl -sL -A <UA> http://www.hittitemonuments.com/yazilikaya/YAZILIKAYA_64.htm` | **HTTP 404**, 1251 B (relief pages do not exist; the index links only `yazilikaya01.jpg…`). Contrast: `/bogazkoy/BOGAZKOY_03.htm` → 200, 3106 B, “A stele of Tudhaliya IV … on display in the Anatolian Civilizations Museum”, literature *Hawkins, CHLI Vol 3, 2024: 39–40, plt. 27* |
| Cleveland's Hittite holdings are tiny; one headgear description | `…/api/artworks/?q=Hittite&limit=30` → 200, 35564 B, `09b7aed0…6715`; parsed `info.total` | **total = 5**: 1971.45, 1975.13 (Stag Poletop), 1985.70, 1973.19, 1971.265. Only 1971.45 describes headgear. `?q=orthostat`, `?q=Hattian`, `?q=Alaca`, `?q=Tell+Halaf`, `?q=Carchemish` → **0 objects each** |
| Met Heilbrunn essay (2002) names no headgear | FetchURL read of `…/toah/hd/htit/hd_htit.htm`; read-level sweep for horn/crown/cap/headdress/helmet/hat; curl re-fetch for a byte artifact → **429** | **0 headgear terms**; its only Yazılıkaya sentence is chronological (“the king completed the construction of a nearby religious sanctuary, known today as Yazılıkaya”). Disclosed as read-level because the 429 blocked an artifact |

## 3. Access failures (receipts, not refutations)

| Attempt | Command | Status |
|---|---|---|
| Met collection **API** | `curl … collectionapi.metmuseum.org/public/collection/v1/search?q=Hittite` | **410**, 0 B — path gone |
| Met website (curl) | same host, browser UA | **429**, 34222 B (rate-limit page) |
| British Museum object record | `…/britishmuseum.org/collection/object/H_1862-0423-1` + browser UA | **403**, 5707 B — same wall as round 8 |
| BM fallback | `archive.org/wayback/available?url=…` | `{"archived_snapshots": {}}` — no snapshot |
| Penn Museum search | `penn.museum/collections/search/?q=Hittite` | **403**, 961 B |
| Louvre search endpoint (4 term queries, incl. after a 20 s pause) | `collections.louvre.fr/en/recherche?q=…` | **429** every time — no term sweep possible; notices reachable by ark URL only |
| museum-digital Berlin (UI + JSON API) | `smb.museum-digital.de/objects?search=Boğazköy`; `…/json/objects?search=Boğazköy` | UI = JS shell (“Objekte gefunden: 261213”, 0 Hittite hits); API 200, 6971 B, `24f4b589…3ce5` but returned **unfiltered coin objects** (Münzkabinett, total 261213) |
| Wikidata fallback (BM Kubaba C.149 relay seen in an image repository) | `wikidata.org/w/api.php?action=wbsearchentities&search=Kubaba stele` | 200, `"search":[]` — zero entities; a relay would not substitute for a museum record anyway |

## 4. Deeper limit — exactly what remains unreadable / unretrievable (2026-10-17, this host)

1. **Yazılıkaya reliefs** (nos. 34/42/64/81, Chamber A processions) — *in-situ rock carvings*, not accessioned
   objects: no museum object record exists to fetch, and the monument database has no relief-level pages
   (404). Their figure labels are still unread first-hand by this shard.
2. **Seeher 2011 plates** (the entry's cited visual authority, bibliography line 28) — no online full text or
   plate set found; unchanged from round 8.
3. **Museum of Anatolian Civilizations (Ankara)** — no retrievable object catalogue; the Alaca Höyük orthostats
   (dated Empire period, “moved to the Anatolian Civilizations Museum in Ankara”) have no inventory-numbered
   online record.
4. **Boğazköy Museum** — gallery-level record only; the “Hittite religion” display panels are not published.
5. **British Museum** — 403 with browser UA and no Wayback snapshot: BM-held Carchemish horned-crown objects
   stay unreadable from here.
6. **Met object pages** — API 410, curl 429: only rendered-page reads succeed, so no hashable artifact.
7. **Louvre search** — 429 on every term query: the Louvre's own headgear vocabulary could not be swept.
8. **museum-digital Berlin** — no filterable record obtained, so no cast/original record of Hattusa reliefs.
9. **Hattic-period headgear witness** — *not retrieved by any route*. Nearest earlier-horizon museum records:
   the Hattian EBA III axe (now restituted) and the Old Kingdom 16th-century seal comparator already carried
   by round 8's scholarly passage. Filed as unretrieved, **not** as support.

## 5. Limits (retained and new)

No headgear image was inspected at pixel level — every horned-crown statement here is the museum's own text.
Cleveland 1971.45 (c. 1600 BCE, North Syria) must not be back-projected onto the imperial Yazılıkaya rows, and
the Iron Age Louvre/Cleveland records stay comparators (entry line 49). The **depicted-rank** limb (single vs
multiple horns) was **not** advanced here; it still rests on round-8's scholarly passage, not re-claimed by
this receipt. State museum records carry no inventory numbers, so entry line 137 cannot yet be pinned to a
photographed, accessioned object. Hittite Monuments is a compiled monument database, not a museum authority,
and is used only for display-location and site-phase statements. The Met object page was read through the
FetchURL tool (curl was 429), so that record has no byte artifact in this shard's store — disclosed rather
than papered over.

*Every quote above was copied from the artifact named in its receipt line; accents are preserved as delivered
and whitespace collapsed only. Artifacts: `/var/tmp/r9f03a/ev/` + `SHA256SUMS`.*
