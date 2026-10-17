# R9-F03c — alternate-angle hunt on residual R8-F03 (round-9 freshness)

- **Shard:** R9-F03c · **role:** alternate-angle hunter (escalated strategy c of the F claim) · **residual:** R9-R8-F03
  (prior rows R8-F03, R6-05-B) · **date:** 2026-10-17 · **baseline:** `a7bb205d3aecdaa24d91c047c8719cd8689e4ddd`
  (`git rev-parse HEAD`; the F claim's declared baseline `e1694ba…` is HEAD~1, the admitted round-8 state).
- **Question under test:** *"Check one dated divine/royal headgear, pointed-cap or horned-crown identification in the
  entry; distinguish depicted rank, deity/king identification and earlier Hattic or later Neo-Hittite comparators."*
- **Entry:** `corpus/knowledge/civilizations/anatolia-hittite.md`, sha256
  `a8e421f7118eb956418a2abbeb24890cfa05e1b35de41f7db72dfa6b9f7332a0` (unmodified by this shard).
  Locators used: line 123 (horned divine headdress), 135 (male divine figures), 136 (female divine figures),
  137 (royal ceremonial representation), 49 (New/Neo-Hittite terminology trap), 139–140 (depicted garment vs
  textual garment term discipline).
- **Result:** **partial-support** — passage support for the terminology leg, the royal-headgear leg and a dated
  earlier (pre-Hittite) head-adornment leg; the Hattic horned-crown limb and any tablet-level witness stay open and
  are named below. Raw round-6/round-8 labels are untouched.
- **Machine copy:** `reports/round-9/freshness/R9-F03c-receipt.json` (same session data, per-quote spans).

## 1. Angle — why this is the *alternate* route

Round 8 reached the headgear question through the imperial relief programme and its excavation literature
(Wikipedia Yazılıkaya, Bonatz's IDD chapter, the Carchemish III scan, Hittite Monuments pages, Oreshko 2018).
This shard goes at the same entry rows from two different evidence registers:

1. **the Hittite *words* for headgear** as edited in the philological literature (what the texts call the thing,
   which Sumerograms they use, and which comparison chains are hypotheses);
2. **the pre-Hittite Anatolian object register** — dated elite head adornments (diadems/headbands) from the
   Alacahöyük Early Bronze Age "Royal Tombs" and their calibrated chronology.

Neither lane is the museum-record hunter's (that is R9-F03a, which filed Cleveland 1971.45 / Louvre Neo-Hittite
records) nor the scholarly-fulltext hunter's (the imperial relief programme is R9-F03b's lane). **No round-8 artifact
was re-fetched, and no round-8 passage is restated as newly retrieved.**

## 2. Session and scratch

- **Window:** 2026-10-17 20:49:02Z – 20:53:22Z, all `date -u` on this host (UTC; local = UTC-3).
- **Scratch:** `/var/tmp/r9f03c`. `/tmp` was unusable — `mkdir -p /tmp/r9f03c` → *"No space left on device"* while
  `df -h /tmp` showed 8.5G free; `df -i /tmp` → `1048576 1048576 0 100%` (no free inodes) at 20:47 and again at
  20:53 UTC. `/var/tmp` (same filesystem as `/home`, 781G free) was used instead. The fetched artifacts and the two
  verification scripts (`build_receipt.py`, `verify2.py`) live there; every artifact below carries its sha256.

## 3. Artifacts retrieved (fresh fetches, this shard)

| Artifact | Source | HTTP / bytes | sha256 (short) |
|---|---|---|---|
| `hoffner-djvu.txt` (+ `hoffner-meta.json`) | archive.org item `hoffner-studies-1964-2003` — *Selected Writings of Harry A. Hoffner, Jr.* (29 articles, 1964–2003) | 200 / 857 916 (+ metadata 9 957) | `f94d303f…54e6b` |
| `bilkent-content.pdf` → `bilkent.txt` | Thomas Zimmermann, *Symbols of Salvation? …*, **Anodos 6-7/2006-2007, 509-520** (Bilkent repository) | 200 / 993 749 | `c2321a6a…ff92a` |
| `pam-diadem.pdf` → `pam.txt` | Zuzanna Wygnańska, *Tracing the "Diadem-Wearers" …*, **PAM 23/2 (2014), 85-144** (BAZHUM) | 200 / 6 416 638 | `cf59066c…261e74` |
| `simpson-ch32.pdf` → `simpson.txt` | Simpson, *Luxury Arts of the Ancient Near East*, ch. 32 of **The Adventure of the Illustrious Scholar** (Brill 2018) | 200 / 2 730 752 | `8576b52e…12b4558b` |
| `votive-djvu.txt` | sweep artifact only (Hittite votive texts; grep found no kupaḫi) | 200 / 560 286 | `ff15cf2e…fbb49f` |

Retrieval used `curl -sL --max-time <30-120> -A 'Mozilla/5.0 … research-retrieval'`, then `pdftotext -layout`;
each artifact's exact command, accessed-at timestamp and full sha256 are recorded in the JSON receipt.

## 4. Legs and what they support

### Leg A1 — the Hittite term for the headgear *(Hoffner, JNES 23/1 (1964), 66-68, p. 67 + n. 16)*

> "Another possible example of this “</” laryngeal in Hittite is the term Jcupahi -, which denotes a type of
> headgear." — artifact lines 434-437 (OCR: `Jcupahi` = kupaḫi; `“</”` = "g")

> "See A. Goetze, “Hittite Dress,” in Corolla Linguistica, p. 59. Goetze shows that in lists Hittite hupahi
> alternates with TUG SAG.DUL." — n. 16, lines 455-457 (OCR: `hupahi` = kupaḫi; `TUG` = TÚG)

Supports the entry's discipline that the *textual garment term* is a separate layer from the depicted garment: the
Hittite headgear word is written with the textile classifier TÚG ("cloth") in lexical lists, so the Hittites' own
naming is a cloth head-covering term and does not by itself licence a metal "helmet/crown" construction. The
Hebrew/Greek comparison (Hoffner: "we might wish to posit the pronunciation Jcubagi- for the cuneiform Jcupahi -,
“helmet, headgear.”") is explicitly a hypothesis, not an object identification.

### Leg A2 — gender contrast in the same terminology *(Hoffner, JBL 85/3 (1966), 326-334, p. 331 n. 33)*

> "The TtJG kuressar is a kind of headgear characteristic for women." — artifact lines 2309-2313

> "headgear is kupafri- (Goetze, op. cit., p. 59) possibly the source of Hebrew" — line 2330 (OCR `kupafri-` = kupaḫi-)

In the same note Hoffner establishes TÚG.NÍG.MUNUS = TÚG kureššar from two independent lines of evidence. This puts
the entry's male/female divine-figure contrast (lines 135–136) on textual terms as well as silhouettes. Nothing here
dates either term or ties it to a relief.

### Leg B — the royal headgear register: named images and a written term *(Wygnańska, PAM 23/2 (2014): 95, 116)*

> "Headbands continued to be used in Anatolia in the Late Bronze Age and they may be seen on a number of official
> Hittite depictions, perhaps worn together with a textile band. They are found on kings: Tudhaliya IV from
> Yazilikaya (scene from Room 64), royal couple on an Alacahöyük orthostat, Muwatalli II on a relief from Sirkeli,
> and on the Sun god in a depiction from Hattuša (Südburg …" — p. 95 left column, lines 477-486

> "In Late Bronze Age Anatolia, Hittite inventory texts contained references to headbands. In his study of linen,
> Matteo Vigo (2010) proposed to interpret the term lupan(n)i in a specific context as “fabric worn on the head”,
> associating it with the Sumerogram eme, translated literally as “tongue”." — p. 116, lines 1357-1364

and, from the same page: the headband, "sometimes adorned with jewels or thin metal layers and fixed on the
forehead, is thus interpreted as a head adornment of Hittite priests or priestesses, perhaps even worn by rulers to
legitimize their simultaneous role of high priest (Vigo 2010: 310–311)".

This is an independent convergence with round 8's Bonatz leg on **relief no. 64 (Tudhaliya IV)** from a different
venue and genre, and it supplies a *textual* royal/priestly headband term — so the entry's line-137 royal row can
rest on "depicted headband + named kings + inventory term" rather than a single "rounded cap" paraphrase. The
`lupan(n)i` interpretation is quoted at second hand from Vigo 2010 (not retrieved → `to-verify`).

### Leg C — the earlier (pre-Hittite) object register, dated

> "…like the openwork headbands from Alacahüyük that probably functioned as a crown (Koşay 1938: Pl. 82; 1951:
> Pl. 129; Muscarella 2003: 280)" and "the diadems from Alacahöyük were found in a restricted number of elite
> burials and were clearly attributes of power and elevated social position." — PAM, p. 94, lines 407-416

> "Generally, diadems, mostly of gold, proliferated in Anatolia in the second half of the 3rd millennium BC, but the
> context seems to have become differentiated." — PAM, p. 95, lines 455-458

> "This allows to establish an upper limit at around 2,300 BC cal. for the “early” graves, with the youngest burials
> to be dated around 2,000/1,950 BC." — Zimmermann, Anodos 6-7, p. 511, lines 167-171

> "Indeed, despite being firmly embedded in a Pre-Hittite sequence and cultural environment, the Alaca standards are
> still often erroneously referred to as “Hittite” products." — same article, notes, lines 379-381

> "Outstanding jewelry and metal artifacts were recovered from 13 Early Bronze Age “royal” tombs at Alaca Höyük in
> central Anatolia, dating to the second half of the third millennium b.c." — Simpson, Brill 2018, p. 666

An **earlier** Anatolian headgear comparator with dates and two independent scholarly anchors — but in the
headband/diadem register, not the horned-crown register. It also yields a second naming trap for the entry: pre-Hittite
Alaca material is still "erroneously referred to as 'Hittite'", parallel to the entry's line-49 New/Neo-Hittite trap.
The "Hattian" ethnic attribution of those tombs is a modern convention, not something these sources assert.

## 5. Quote fidelity and verification

- **Fidelity.** Quotes preserve the artifact bytes; disclosed departures are: OCR-form mapping (Jcupahi→kupaḫi,
  Jcubagi→kubagi, kupafri→kupaḫi, hupahi→kupaḫi, TtJG→TÚG, NlG→NÍG, `“</”`→"g"), joining of line-final hyphens
  (`contain-ed`→contained, `Küçük-höyuk`→Küçükhöyuk) except where the hyphen belongs to the word (Q_H2 keeps
  `Jcubagi- for`), omission of printed footnote markers and page-break duplication, and normalization of
  source-internal quotation marks inside JSON strings. The PAM pages 92–95 / 115–116 are two-column, so
  `pdftotext` interleaves the right column between left-column lines; quotes from those pages are the contiguous
  column text.
- **Verification.** `python3 /var/tmp/r9f03c/build_receipt.py` extracts each quote by artifact + line span and
  measures the longest contiguous token n-gram of the quote present in the artifact (NFKC → disclosed OCR mapping →
  diacritic folding → lowercase → alphanumerics only), mirroring the sibling verifier's ≥10-token pass rule.
  **Result: 15/15 pass, longest contained n-gram 14–74 tokens**, tested against a column reconstruction for the
  two-column pages (against the raw interleaved text the same test necessarily yields only 8–10 tokens — that gap
  *is* the interleave evidence, recorded per quote).

## 6. Access failures and sweeps (negatives carry their sweep)

| Attempt | Command (as run) | Result |
|---|---|---|
| CHD K entry for kupaḫi- | `curl -sIL …/shared/docs/chd_k.pdf`; `…/publications/hittite-dictionary-volume-k` | **404**; ISAC's CHD page (200, 182 208 bytes) lists only volumes L-N, P, S — no published K fascicle |
| Electronic CHD | `…/electronic-chicago-hittite-dictionary`; `ochre.lib.uchicago.edu/eCHD/` | **404 / 403** |
| IA full-text sweep for "kupahi" | `ia-pub-fts-api…/search/v1/scrape?q=%22kupahi%22`; `archive.org/search?query=%22kupahi%22&sin=TXT` | empty body / 1 951-byte JS shell — no server-side results |
| IA for Goetze 1955 *Hittite Dress* | `archive.org/advancedsearch.php?q=title:("hittite dress")…` | 0 documents (288-byte JSON) |
| Google Books "kupahi" | `googleapis.com/books/v1/volumes?q=%22kupahi%22` | **429** rate-limited |
| Iron Age divine-headdress lead (Kubaba chapter, OpenAlex W4384571244, CC-BY) | `curl -sL https://doi.org/10.36253/979-12-215-0109-4.12` | **403** Cloudflare interstitial ("Just a moment…") |
| Tablet-level kupaḫi | `cdli.mpiwg-berlin.mpg.de/search?q=kupahi` | JS shell returns the unfiltered collection (10 000+ results) — no term filter |
| HPM corpus search | `hethport.uni-wuerzburg.de` | landing page only (1 744 bytes) |
| Goetze 1955 full text | bibliographic sweep only | article real and heavily cited (Cambridge Core 1969; Athens Journal 2016; DergiPark) but no open copy → claim kept at second hand with its page locator |

**Sweeps run** (WebSearch ×5, OpenAlex API, archive.org ×2; all 2026-10-17): the term/"kupahi" sweep produced the
lexical leg; the Hattic/Early-Bronze-Anatolia sweep and the OpenAlex "Hittite horned crown" query (34 works) produced
**no pre-Hittite horned-crown image or study**; the Alaca/diadem sweep produced the dated pre-Hittite leg; the CHD
volume-K sweep confirmed the dictionary entry does not yet exist.

## 7. Unresolved limbs and deeper limits

1. **Earlier Hattic comparator for the horned/pointed divine crown — unresolved after sweep.** No pre-Hittite
   (Hattian-horizon) image or text showing/naming a horned or pointed divine crown was retrieved; the pre-Hittite
   Anatolian headgear record that *was* retrieved (Alacahöyük diadems/headbands, c. 2300–2000/1950 BC) is a different
   register. The nearest earlier comparators remain the Old Kingdom five-faced seals of the 16th cent. (inside Hittite
   tradition, round-8 Bonatz leg).
2. **Tablet-level attestation of kupaḫi- — unresolved**: CHD K unpublished, e-CHD 404/403, CDLI and HPM unreachable
   as search surfaces; Goetze 1955 p. 59 unread at first hand (the alternation claim is quoted via Hoffner 1964 n. 16).
3. **Vigo 2010's `lupan(n)i` argument — quoted at second hand** from Wygnańska 2014: 116.
4. **Plate-level cap construction (Seeher 2011)** — unchanged from rounds 6/8; no image-level inspection by this shard.

## 8. Cross-checks and boundaries

- Sibling verifier file `reports/round-9/freshness/verify-F03.md` (V02): its §5.5 requirement that an unresolved
  Hattic leg name the sweeps that failed is answered in §6–§7 above; its §4 failure table and this shard's
  `access_failures` agree that the Oreshko HAL file and the CHD/e-CHD routes are unreachable this round. This shard
  did not read that file before its own retrievals (it landed during them; alignment checked afterwards, no claim
  adjusted to match).
- Sibling hunter R9-F03a took the **primary-source/museum-record** lane (Cleveland 1971.45 "horned conical crown";
  dated but headgear-silent Louvre Neo-Hittite records) — no overlap with this receipt's sources.
- **No repository mutation:** this shard wrote no corpus file, tool or gate; the only writes are
  `reports/round-9/freshness/R9-F03c-receipt.{json,md}`. No `git` state was changed.
- Reconciled dispositions for the residual belong to the round-9 reconciliation/orchestrator, not to this shard.
