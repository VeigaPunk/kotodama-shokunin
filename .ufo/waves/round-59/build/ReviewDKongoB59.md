# ReviewDKongoB59 — claim D falsify, kongo-kingdom.md fixes 85, 89, 93, 97a, 97b

Seat: ReviewDKongoB59 (leaf, no delegation). Date 2026-10-23. Scratch: `/fast/scratch/hyaku/kotodama-r59/ReviewDKongoB59/`.
Inputs: `reports/round-59/d-fixes.json` (kongo fixes), `corpus/knowledge/civilizations/kongo-kingdom.md` at the working tree, `corpus/SOURCES.md` rows S380, S381, S384, S385, S392, S396, S397.
Installs: none.

## Verdict

**All five fixes: AGREE.** In each case the new text is a faithful reading of the re-opened page, and the old text was wrong (an overread, a voice mix-up or a truncated date). No old text was actually right. Each `old` string occurs exactly once in the entry (count 1), and no `new` string is present yet (count 0), so every fix lands as a single replacement.

| Fix | Verdict | Old text was | Locator check |
|---|---|---|---|
| 85 | agree | wrong voice: the p. 32 date and place are in Randels's block quotation, not Batsîkama's narrative | p. 27 and p. 32 confirmed (PDF page + 6 = printed page; PDF p. 21 footer "27", PDF p. 26 footer "32") |
| 89 | agree | overread: "covers" dropped the page's "may relate to" hedge | essay = the intro description `<p>`; first `<br/><br/>` block confirmed |
| 93 | agree | overread: "centre of palero practice" for "centre de l'attention des paleros" | p. 76 confirmed (PDF p. 19 footer "76"; PDF p. 2 footer "59") |
| 97a | agree | overread: one depicted leader turned into a general "A Christian noble wore…" | p. 12 confirmed (running head "Anais … 2017. 12") |
| 97b | agree | wrong: "late-1800s" dropped the record's upper bound | `creation_date` field confirmed |

## Per fix: served sentence, locator output, judgment

### 85 — S392 Batsîkama 2021 (date and place of the execution)

- Old: `Batsîkama gives 2 July at Kimbangu (S392, p. 32), and Farias places the execution in Mbanza Kongo (S381, p. 210): date and place stay contested (to-verify).`
- New: `Batsîkama's own account gives 2 July 1706 (S392, p. 27), while the block quotation he credits to Randels places the execution at Kimbangu (S392, p. 32); Farias places it in Mbanza Kongo (S381, p. 210): date and place stay contested (to-verify).`
- Source: `https://revistas.usp.br/sankofa/article/download/187402/173183/497395` (curl HTTP 200, `application/pdf`, 985,805 bytes, 30 PDF pages = printed pp. 7–36).
- Served, printed p. 27 (author's voice, after the Thornton block quote, which ends at note 65): "Foi ele que coordenou a sua prisão, o seu primeiro julgamento em maio e o segundo julgamento em junho e com a cumplicidade do padre Lorenzo da Lucca, condenaram a profetisa angolana a morrer queimada viva. Isso aconteceu no dia 2 de julho de 1706, numa sexta-feira."
- Served, printed p. 32: "William Graham Lister Randels conclui, em relação ao movimento antoniano, que: Já antes do assalto final que em 1709 D. Pedro IV lançou contra São Salvador, … No dia 2 de julho de 1706, em Kimbangu, aos olhos dos missionários, eles foram entregues juntos às chamas. … (quer dizer, em 1712)." Note 87: "RANDELS, 2002: 153".
- Served, printed p. 30 (cross-check): "Porém, depois de queimá-la, no dia seguinte, três de julho de 1706 apareceu a Quarta Minguante".
- Locator:
  - `LOCATED https://revistas.usp.br/sankofa/article/download/187402/173183/497395` — quote "condenaram a profetisa angolana a morrer queimada viva. Isso aconteceu no dia 2 de julho de 1706, numa sexta-feira"
  - `LOCATED https://revistas.usp.br/sankofa/article/download/187402/173183/497395` — quote "No dia 2 de julho de 1706, em Kimbangu, aos olhos dos missionários, eles foram entregues juntos às chamas"
  - `LOCATED https://revistas.usp.br/sankofa/article/download/187402/173183/497395` — quote "William Graham Lister Randels conclui, em relação ao movimento antoniano, que"
  - `LOCATED https://revistas.usp.br/sankofa/article/download/187402/173183/497395` — quote "Porém, depois de queimá-la, no dia seguinte, três de julho de 1706 apareceu a Quarta Minguante"
- Judgment: **agree.** p. 27 gives 2 July 1706 in Batsîkama's own voice and names no place there. The 2 July + Kimbangu pairing is only inside the Randels block on p. 32, which note 87 credits to Randels 2002: 153. The new text attributes each element to the right voice and page.
- Note, low, optional: on p. 27, "Isso" grammatically follows "condenaram … a morrer queimada viva", so that sentence alone could be read as dating the condemnation. p. 30 ("depois de queimá-la, no dia seguinte, três de julho") fixes the burning itself on 2 July. Adding "(p. 30)" would make the execution reading airtight, but the new text is not an overread without it.

### 89 — S396 Met 312342 (what "nkisi" covers)

- Old: `The Met says the term covers cloth packets and filled vessels as well as carved wood (S396, essay, first paragraph).`
- New: `The Met says the term nkisi may relate to a wide spectrum of physical receptacles, including cloth packets, filled vessels, as well as carved wood sculptures (S396, essay, first paragraph).`
- Sources:
  - Live `https://www.metmuseum.org/art/collection/search/312342`: my first curl got HTTP 429 with the body "Vercel Security Checkpoint … Enable JavaScript to continue". That is a challenge, so it was met and not passed. Minutes later the locator's plain GET was served the page (output below), so the challenge flaps.
  - Capture `https://web.archive.org/web/20230529091312id_/https://www.metmuseum.org/art/collection/search/312342`: HTTP 200, 204,151 bytes.
- Served (first block of `artwork__intro__desc`, before the first `<br/><br/>`): "The term "nkisi" may relate to a wide spectrum of physical receptacles, including cloth packets, filled vessels, as well as the carved wood sculptures studied by art historians."
- Locator:
  - `LOCATED https://www.metmuseum.org/art/collection/search/312342` — quote "may relate to a wide spectrum of physical receptacles, including cloth packets, filled vessels"
  - `LOCATED https://web.archive.org/web/20230529091312id_/https://www.metmuseum.org/art/collection/search/312342` — same quote
  - `LOCATED https://web.archive.org/web/20230529091312id_/https://www.metmuseum.org/art/collection/search/312342` — full sentence 'The term "nkisi" may relate to … studied by art historians.'
- Judgment: **agree.** The new text restores the "may relate to" hedge and the "carved wood sculptures" object class. The old "the term covers … carved wood" asserted more than the page does. The new text drops "the" and "studied by art historians", which changes no meaning.
- Note, low, style only: the new clause copies about 20 consecutive words from the label without quotation marks. If the lane wants verbatim runs marked, quote "may relate to a wide spectrum of physical receptacles". This is not a fidelity defect.

### 93 — S385 Dianteill 2002 (minkisi in Cuba)

- Old: `In Cuba the minkisi became the centre of palero practice while every rite tied to the royal function disappeared (S385, p. 76)`
- New: `In Cuba the minkisi became the centre of the paleros' attention while every rite tied to the royal function disappeared (S385, p. 76)`
- Sources:
  - Capture `https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480`: HTTP 200, 303,987 bytes, PDF.
  - Captures `…/20230210060841id_/…` and `…/20220206013218id_/…`: HTTP 200, 303,987 bytes on a slower curl retry. All three files share sha256 `37c55794e2c95799d577bd92bb912fd163081a1bde39b692e09f1d98b1ab423a`, so they are the same document.
  - Live `https://journals.openedition.org/assr/pdf/2480`: HTTP 200 `text/html`, 5,256 bytes, an Anubis proof-of-work challenge page (`<script id="anubis_challenge" …>`). That is access control, so it was met and not passed.
- Served, printed p. 76 (Conclusion): "Tous les rituels en rapport avec la fonction royale ont disparu. … Les minkisi, qui ne représentaient qu'une partie des objets rituels en pays kongo, sont devenus le centre de l'attention des paleros."
- Locator:
  - `LOCATED https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480` — quote "Les minkisi, qui ne représentaient qu'une partie des objets rituels en pays kongo, sont devenus le centre de l'attention des paleros"
  - `NOT_LOCATED https://journals.openedition.org/assr/pdf/2480 quote-absent` — the live URL serves the Anubis challenge HTML, not the PDF.
  - `NOT_LOCATED https://web.archive.org/web/20230210060841id_/https://journals.openedition.org/assr/pdf/2480 URLError`, then `… HTTPError` on retry. Same pattern for `20220206013218` and `20190503050212` (`URLError` twice). Wayback throttled the locator's back-to-back requests: curl fetched 2023 and 2022 byte-identical to 2024 seconds later, and 2019 stayed unreachable this session (curl exit 7, "Failed to connect to web.archive.org:443 after 184 ms: Could not connect to server", HTTP 000).
  - `NOT_LOCATED https://web.archive.org/web/20240327164523id_/https://journals.openedition.org/assr/pdf/2480 URLError` — second quote "Tous les rituels en rapport avec la fonction royale ont disparu." This was the same throttling, on a capture that had located the first quote earlier. The sentence was read in the same served PDF, on PDF p. 19 = printed p. 76.
- Judgment: **agree.** "centre de l'attention des paleros" is rendered exactly, and "Tous les rituels en rapport avec la fonction royale" is rendered as "every rite tied to the royal function". The old "centre of palero practice" claimed more than "attention". The new text omits Dianteill's qualifier that minkisi "ne représentaient qu'une partie des objets rituels en pays kongo"; that omission is a narrowing, not an overread.

### 97a — S384 Fromont 2017 (the leader in Figure 1)

- Old: `A Christian noble wore an mpu, an nkutu net over the shoulders, a staff and a red coat with the order's insignia (S384, p. 12).`
- New: `In the watercolor, the richly attired leader wears an mpu cap and an nkutu net over his shoulders, carries a wooden staff, and a brilliant red coat embroidered with the Order of Christ insignia hangs behind his back (S384, p. 12).`
- Source: `https://www.redalyc.org/jatsRepo/273/27353124003/27353124003.pdf` (curl HTTP 200, 1,291,427 bytes, PDF).
- Served, printed p. 12: "Their richly attired leader walks one step in front of the group in the shade of a red umbrella that an attendant diligently holds above his head. … He wears an mpu cap on the head, an nkutu net over the shoulders. He carries a wooden staff in his left hand, and many bracelets and anklets adorn his arms and legs. As he steps, … a brilliant red coat embroidered with the insignia of the Order of Christ hangs behind his back." Figure 1 caption: "Bernardino d'Asti. Reception of a capuchin missionary by a local ruler. Italy, ca. 1740. Watercolor on paper".
- Locator (all `LOCATED https://www.redalyc.org/jatsRepo/273/27353124003/27353124003.pdf`):
  - "a brilliant red coat embroidered with the insignia of the Order of Christ hangs behind his back"
  - "Their richly attired leader walks one step in front of the group in the shade of a red umbrella"
  - "He wears an mpu cap on the head, an nkutu net over the shoulders"
  - "He carries a wooden staff in his left hand, and many bracelets and anklets adorn his arms and legs"
  - "two mestres, interpreters and leaders of the Church, wear their uniform composed of a white cloth draped over one shoulder"
- Judgment: **agree.** Every element is on p. 12, and the new text keeps it to the one depicted leader. On p. 14 Fromont identifies him as Don Francesco, the new ruler of Soyo. The old "A Christian noble wore…" turned one figure in one watercolor into a class-wide dress rule.
- Flag, low, clarity: "In the watercolor" has no antecedent inside the "Rank is worn" bullet (line 97). The only earlier mention is the line-84 fix 84a, about 13 lines up. Suggest "In Bernardino d'Asti's watercolor (S384, p. 12, fig. 1)".

### 97b — S397 Cleveland 1997.180 (cap date)

- Old: `a late-1800s cap`
- New: `a late-1800s–early-1900s cap`
- Source: `https://openaccess-api.clevelandart.org/api/artworks/159880` (curl HTTP 200, JSON, 8,764 bytes).
- Served: `"tombstone": "Prestige Cap (mpu ngola), late 1800s–early 1900s. Africa, Central Africa, Democratic Republic of Congo, Republic of Congo, or Cabinda (Angola), Kongo-style maker, possibly Yombe subgroup. …"`, `"creation_date": "late 1800s–early 1900s"`, `"creation_date_earliest": 1875`, `"creation_date_latest": 1925`.
- Locator: `LOCATED https://openaccess-api.clevelandart.org/api/artworks/159880` — quote "Prestige Cap (mpu ngola), late 1800s–early 1900s. Africa, Central Africa, Democratic Republic of Congo"
- Judgment: **agree.** The old text cut off the record's stated range.
- Flag, low, locator only: the sentence cites everything to "(S397, Description)". The `description` field does carry *zimpu*/*mpu*, *mpu ngola*, the high-status wearer, and "Known since at least 1607 in the former Loango Kingdom, as well as the adjacent Kongo Kingdom". The date (now changed) and "maker possibly Yombe" come from the `tombstone`/`creation_date` and `culture` fields. A precise locator would be "(S397, Description; tombstone)".

## Findings by severity

There are no high or medium findings against fixes 85, 89, 93, 97a or 97b. All five may land as written.

Low findings, none blocking:
1. **Fix 85, the unchanged half of the same sentence.** S380's eyewitness paragraph carries the anchor "the sentence of being thrown alive into the flames". It dates the burning itself, not only the sentence: "Then, on Sunday, the first of July, 1706, … the Judge appeared, who in public declared against them the sentence of being thrown alive into the flames. … they were cast upon two piles of wood … and fire was set to them." (Source: `https://vincentbarletta.com/blog/beatriz-kimpa-vita-and-kingdom-of-kongo`, HTTP 200, 207,293 bytes.) The entry's "Gallo dates the sentence to Sunday 1 July 1706" understates Gallo; "Gallo dates the sentence and burning to Sunday 1 July 1706" would make the date contest in fix 85 explicit. [INFERENCE, my own calendar computation, not on any page: in the Gregorian calendar, 1 July 1706 was a Thursday and 2 July 1706 a Friday. That matches Batsîkama's "numa sexta-feira" and conflicts with Gallo's "Sunday, the first of July" as Barletta translates it, which supports keeping "(to-verify)".]
2. **Fix 89.** About 20 verbatim words without quotation marks (style).
3. **Fix 97a.** "the watercolor" lacks a local antecedent (clarity).
4. **Fix 97b.** The "Description" locator does not cover the date or maker fields.
5. **Cross-fix, outside my assignment (84a), recorded so the L1 sees it.** S384's Figure 1 caption says "Italy, ca. 1740", but Fromont's own text dates the scene later. p. 14 says the watercolor celebrates "the return of the Capuchin mission to Soyo a few years after a disagreement with the former ruler Cosme Barreto da Silva had driven the friars out of the region in 1743", and p. 17 speaks of "friar Bernardino's 1750s watercolors". The "ca. 1740 watercolor" in fix 84a copies the caption faithfully, but the source's own date evidence conflicts with it.

## Residual risk and verification gaps

- **S385 live URL is gated.** `journals.openedition.org/assr/pdf/2480` now serves an Anubis challenge to plain GETs. Any future plain-GET acceptance of the S385 row will rely on the Wayback captures (2024, 2023 and 2022 are byte-identical). The 2019 capture was not reachable this session.
- **The Met live page flaps** between a Vercel challenge (HTTP 429) and a served page. The 2023 capture is the stable copy.
- I did not re-open S381 (Farias, p. 210), because fix 85 does not change the Farias clause. I read Gallo's paragraph as served, using my own `<p>` count (paragraph 138 of the served HTML). I did not re-derive the entry's "para. 136" numbering under S380's counting rule; the anchor sentence and the burning sit in the same paragraph, so the finding holds under either count.
- Every locator run used `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/reports/round-59/reopen-quote.py '<url>' '<quote>'`, run from scratch. Full log: `/fast/scratch/hyaku/kotodama-r59/ReviewDKongoB59/reopen.log`.
