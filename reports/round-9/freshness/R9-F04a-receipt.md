# R9-F04a — primary-source / museum-record hunt for R9-R8-F04 (row R6-07-A, Melqart)

- **Round:** 9 (loop 1 of 3, build round 2 of 4) · **Axis:** freshness · **Date:** 2026-10-17
- **Residual:** R9-R8-F04 = R8-F04 = R6-07-A — *"Check mlqrt/Melqart's king-of-the-city analysis and the limits of a fixed merchant-patron/theological profile against an inscription, philological source or scholarly passage."*
- **Entry:** `corpus/knowledge/civilizations/levant-canaan-phoenician.md`, §4 bullet 1 = **line 78**
- **Entry digest at recheck:** `2ca21052…b8e9e4da` (`sha256sum`, 2026-10-17T20:48Z) — equals the blob at the declared round-9 baseline `e1694ba`, so the entry is unmodified since the round-8 admit commit. Round 8's recorded `a2c548aa…` was a transient working-tree state; the tested sentence compares **identical** (199 chars, programmatic regex comparison, same day).
- **Raw label:** `partial-support` (preserved; prior disposition `unresolved`).
- **Counting command:** `python3 reports/round-9/run-validation.py`
- Retrieval window (UTC): **2026-10-17T20:48:22Z → 2026-10-17T20:53:48Z** (`date -u` bracket).

## What this shard hunted

Round 8 already had two inscriptions (KAI 201, KAI 47), WiBiLex and one peer-reviewed article. This shard took the **primary-source / museum-record** lane and returned **7 new retrievals** — none of them a re-fetch of a round-8 source:

| # | Witness | Date | Place | God form | Role attested |
|---|---------|------|-------|----------|---------------|
| 1–3 | **Louvre AO 4826 = CIS I 88** (statue base, marble) | c. 380–370 BCE (Louvre bracket −392/−362) | Kition (found 1860 in Nicosia) | *domino suo Melqarto* | dedication dated by the city-king's regnal year, dedicant = "royal interpreter"; names **Abdpumams / Abdmelqartus** |
| 4 | **Louvre AO 7676 = IGLS 7, 4001** (the entry's own object) | 25/24 BCE (civic era year 235) | Arados = Arwad | "à Hermès et à Héraklès" / `lʾrms wlmlqrt` | gymnasiarch's dedication; `mlqrt` = *translated* Herakles |
| 5 | **Aliquot 2025**, *Semitica et Classica* 18, 247–260 (HAL `hal-05325053`) | autopsy of AO 7676 at the Louvre | — | — | peer-reviewed: Greek names "soit transcrit (ʾrms), soit traduit en phénicien (mlqrt)" |
| 6 | **Virtual Museum of Syria / Aleppo** — Melqart (Bir-Hadad) stele | 790–760 BCE (contested) | Bureij, N of Aleppo | `lmrʔh lmlqrt` | king's votive relation to "his lord, Melqart"; palaeographic caveat stated |
| 7 | **Heritage Malta** — the Cippi, National Museum of Archaeology, Valletta | 2nd c. BCE | Malta | "Lord of Tyre" / Greek archegete | twin of the Louvre cippus; museum itself calls the provenance unresolved |

Plus the **CIS I editor's note** (scan OCR line 3076) that the clause *"because he heard his voice"* is one "**which very often closes Phoenician inscriptions**" — the same formula closes the Kition dedications to Reshef-Mikal and Esmun-Melqart in the same volume.

## Key quotations (locations in the JSON receipt)

- Louvre AO 4826 record: *"Base de statue avec inscription phénicienne : dédicace du roi Milkyathon à Melqart"* … *"AO 4826 ; CIS I 88"* … *"Kition = Larnaca"*.
- CIS I 88 (Latin translation): *"…filius Azratbaalis, [interpres soliorum,] **domino suo Melqarto**, (quia) au[diit vocem]… **quia audiit Melqartus vocem eorum**; benedicat [eis]"*, dated *"anno circiter 380-370"*.
- Louvre AO 7676 record: *"Inscription bilingue grecque (3 lignes) et phénicienne (3 lignes)** … dédicace aux dieux du gymnase, Hermès et Héraclès-Milqart"*, date *"−25 −24"*; its bibliography cites **Bonnet 1988, p. 117**.
- Aliquot 2025: *"les dieux grecs du gymnase, dont les noms sont soit transcrit (ʾrms), soit traduit en phénicien (mlqrt)"*; date *"An 235 … = 25/24 av. J.-C."*; and, refining the entry, the Phoenician term renders **παλαίστρα**, not γυμνάσιον.

## Calibrations this shard hands to the entry

1. **Line 78 (the claim)** — the civic/royal semantics are now object-witnessed in **three Phoenician cities across four centuries**; nothing retrieved casts Melqart as a fixed merchant patron (calibrated absence). The hedge *"conventionally Melqart"* is epigraphically motivated: the name is written consonantal (`lmlqrt` on the stele, `wlmlqrt` at Arados), so no object can supply the vowels.
2. **Line 82** — confirmed at source (the entry's own AO 7676) **with two refinements**: the Louvre says "gymnase", Aliquot 2025 reads a calque of *palaestra*; the Louvre hedges the dedicant as *"Astarhut (?)"* where Aliquot argues ʿAštartiḥawwot. The record's summary also attributes the AO 4826 dedication to the king, while the corpus text shows the dedicant is the royal interpreter — do not tighten museum summary wording.
3. **Line 146 (bonus, not the tested claim)** — the ʿbd + divine-name type is now attested on a dated object (CIS I 88: *Abdpumams et Abdmelqartus*).
4. **Do not upgrade to full support**: **Bonnet 1988 is still unread**. Nothing in the open record changes that; what this shard adds is that the Louvre's own bibliography routes the entry's object to that book at **p. 117**.

## Access failures (all with command + status in the JSON)

British Museum object `W_1872-0816-79` and search — Cloudflare/JS (403, "Just a moment…"); `journals.openedition.org/cchyp/733` (Cannavò & Le Meaux 2021 on AO 4826) — Anubis bot wall; Persée CRAI 2012 / Syria 1968 — opening page only, PDFs behind altcha; Louvre search endpoint — HTTP 429; Bonnet 1988 — HAL metadata-only (the one deposited 2009 chapter extracts to a cover page, 1,182 chars) and not on archive.org (`title:(melqart)` numFound 6; Lipiński `Semitic Languages` numFound 0 — the Internet Archive was back **online** this round, HTTP 200); `virtual-museum-syria.org/about/` — fetch failed (operator identity unverified).

## Disposition

**partial-support** at whole-claim scope (unchanged label, materially deepened base). This shard's contribution: the primary-source/museum-record leg of the round-9 F claim is satisfied — 7 escalated retrievals, 4 museum/national-agency object records, the CIS I corpus text, a 2025 peer-reviewed autopsy of the entry's own object, and a formula calibration. Full-support promotion stays blocked on **Bonnet 1988** (book-level; p. 117 is the page to read).

## Files

- `reports/round-9/freshness/R9-F04a-receipt.json` — full receipt (7 retrievals / 16 passage records, 5 dated witnesses, 5 leg-coverage groups, 7 access failures, 3 negative claims with sweeps, 6 `to-verify` items, counting commands + outputs).
- `reports/round-9/freshness/R9-F04a-receipt.md` — this summary.

No files outside `reports/round-9/freshness/` were written; temporary scan extracts were deleted; no git commands that mutate state were run.
