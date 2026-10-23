# AuditA3R02 — pre-freeze wording audit (round 60 attempt 3, wave 1)

Scope: candidate entry `/fast/scratch/hyaku/kotodama-r60a3/L1/candidate-entry.md`, ids S604, S605, S607 (all base rows, tier B). Judged exactly as a blind support seat will: quote verbatim body text; page carries the teaches cell; page carries every clause of every entry line citing the id. None of my ids is among S648–S651, so the round-59 rejection comparison does not apply (S604/S605/S607 were all among the 43 blind-SUPPORTED rows at round-59 lane tip; the four rejected were S602, S616, S623, S643).

---

AUDIT S604 OK

- Row (SOURCES.md:559): British Museum, *A Guide to the Exhibition Illustrating Greek and Roman Life*, 2nd ed. 1920, Gutenberg eBook 52081 — https://www.gutenberg.org/cache/epub/52081/pg52081.txt
- Fetch: `curl -sS -L 'https://www.gutenberg.org/cache/epub/52081/pg52081.txt'` → HTTP 200, 415476 bytes (row records 415476). Plain text, body paragraph.
- Quote, verbatim (CRLF line-wraps only): "They were designed to contain amulets and charms, and were worn principally by freeborn Roman boys, and occasionally by domestic animals." — context bytes: `=Bullae.=--The flat bronze pendants (No. =384=), with a circular receptacle in the middle, are _bullae_. These are ornaments of Etruscan origin, introduced early into Rome. They were designed to\r\ncontain amulets and charms, and were worn principally by freeborn\r\nRoman boys, and occasionally by domestic animals.` Body text under the `=Bullae.=` term head — not a heading, caption, promo or navigation (the two other `bulla` hits are a TOC entry and an index line "BULLA, 136, 218").
- Teaches carried: "A bulla is a receptacle for amulets and charms, hung chiefly on freeborn boys and sometimes on farm animals" — page states bullae are pendants with a receptacle designed to contain amulets and charms, worn principally by freeborn Roman boys, occasionally by domestic animals.
- Entry line 68 `Containment: a Roman bulla was designed to contain amulets and charms and was worn mainly by freeborn Roman boys and sometimes by domestic animals (S604). **B**` — every clause carried: "designed to contain amulets and charms" verbatim; "mainly…sometimes" fairly paraphrases "principally…occasionally"; "Roman" backed by "introduced early into Rome" (the guide's Roman section).
- Entry line 94 `Body and animal: freeborn Roman boys wore the bulla, and occasionally domestic animals did, so a child and a farm animal could carry the same protective container (S604). **B**` — first two clauses carried verbatim by the quote. The coda "a child and a farm animal could carry the same protective container" rests on the same sentence (one object class worn by boys and by domestic animals; "farm animal" narrows "domestic animals" as a hedged instance, "could carry" hedged). "Protective" is carried by the page's own framing elsewhere: "More than one of the pigeons wears a _bulla_ round its neck (No. =660=) to avert the evil eye (see p. 136)" — p. 136 is this bullae section — and by the bulla containing "amulets and charms". Not a universal-from-one-object, no theory-as-fact, no added comparison.
- Consistent with round-59 outside spot-check: "The entry's 'worn mainly… sometimes' fairly paraphrases 'worn principally… occasionally'."

AUDIT S605 OK

- Row (SOURCES.md:560): Spathi/Chidiroglou/Wallensten (eds.), *Apotropaia and Phylakteria: Confronting Evil in Ancient Greece* (Archaeopress 2024), publisher open-access sample PDF, Faraone introduction pp. 1–10 — https://www.archaeopress.com/Archaeopress/DMS/84FE4CF1A07D4BD9A83AEA574427183A/9781803277493-sample.pdf
- Fetch: `curl -sS -L 'https://www.archaeopress.com/Archaeopress/DMS/84FE4CF1A07D4BD9A83AEA574427183A/9781803277493-sample.pdf'` → HTTP 200, 1227583 bytes, application/pdf (row records 1227583). Text extracted with `pdftotext` (and `-layout`).
- Quote, verbatim in the PDF body text (wrap between "to" and "ward" only): "A frontal face was also used as a protective amulet to ward off the plague." — mid-paragraph in Faraone's introduction, directly after "a powerful image of Heracles:13". Body text, not a heading or caption.
- Teaches carried: "A frontal face was a protective amulet against plague, and apotropaic eyes served as a common device on ships" — both halves on the page: the quote itself plus "…on the outer surface of military shields. Eyes also appear as a common apotropaic device on ships."
- Entry line 52 (summary table row) `| plague | a frontal face was used as a protective amulet to ward off the plague | S605 (B) |` — clause carried by the quote (entry drops "also", which in the page refers to other devices).
- Entry line 60 `- A frontal face was used as a protective amulet to ward off plague, and eyes appear as a common apotropaic device on ships (S605).` — clause 1 carried by the quote; clause 2 carried by the page sentence "Eyes also appear as a common apotropaic device on ships." (the clause rests on S605; no second id on this line). "Common" is the page's own word; no universal added.

AUDIT S607 OK

- Row (SOURCES.md:562): Gattuso, "Protection from the Evil Eye," Curationist, Sept 2025 — https://www.curationist.org/editorial-features/article/protection-from-the-evil-eye
- Live fetch: `curl -sS -L -A 'Mozilla/5.0 (X11; Linux x86_64) curl/8' 'https://www.curationist.org/editorial-features/article/protection-from-the-evil-eye'` → HTTP 403, 919 bytes (bot gate). No bypass attempted (ordinary means only; see residual risk).
- Listed capture: `curl -sS -L 'https://web.archive.org/web/20260417193418id_/https://www.curationist.org/editorial-features/article/protection-from-the-evil-eye'` → HTTP 200, 283623 bytes (row records capture 283623).
- Quote, verbatim in the rendered body: `<p …>In some times and places, people used shiny materials to craft amulets meant to reflect malicious gazes away from the user. For example, in the early modern Iberian Peninsula,…</p>` — first paragraph under `<h3 id="the-power-of-reflection">The Power of Reflection</h3>`. Body text, not a heading, caption, cookie or navigation string (the same sentence also appears once inside the page's embedded article-source blob — same wording).
- Teaches carried: "Shiny materials were chosen for amulets so that a malicious gaze would be reflected away from the person wearing it" — a fair restatement of the quote ("the user" = "the person wearing it").
- Entry line 66 `- Reflection: in some times and places, people used shiny materials to craft amulets meant to reflect malicious gazes away from the user (S607). **C**` and entry line 87 `- Shine: in some times and places, people used shiny materials to craft amulets meant to reflect malicious gazes away from the user (S607). **C**` — the claim text is the quote itself; every clause carried verbatim. (The label words "Reflection"/"Shine" and the "**C**" grade marker are entry apparatus, not page claims.)

---

## Findings by severity

- Blocking: none.
- Non-blocking observations:
  1. S607 live URL returns HTTP 403 to a plain request. FETCH-60 lets a support seat answer by the listed Wayback capture (200, size matches the row), so the claim is safe — but the seat must actually try the listed capture after a live 403. The row lists the capture correctly; no wording defect.
  2. Entry lines 66 and 87 restate the S607 quote almost identically under two labels ("Reflection", "Shine"). Both are carried by the page; this is stylistic duplication, not over-reach, and the predicate constrains only the four new rows to "exactly one line" — base rows are unaffected.
  3. Verification-tool note for other auditors: the `grep` tool's regex does not match `\s` across line boundaries, and Project Gutenberg ships CRLF — wrapped verbatim quotes must be checked on raw bytes (my `\n` and `\s+` patterns both returned false negatives on bytes that are in fact present).

## Round-59 comparison

Not applicable per scope (ids S648–S651 only). For context: none of S604/S605/S607 was a round-59 rejection; the rejected over-reach shapes (universal drawn from one object, material-versus-carving comparison, hedged theory stated as fact, contents-versus-shell contrast) do not appear on the lines citing my three ids.

## Residual risk / gaps

- S607 support depends on the seat falling back to the listed capture (live URL 403s for ordinary fetches). If a seat treats one live 403 as unreachable without trying the listed capture, it would score NOT-SUPPORTED — but the capture is listed in the row, so the packet is reachable as declared.
- S605 verification requires PDF text extraction; pdftotext handles it cleanly (locator `normalise` collapses the mid-quote wrap).
- My fetches re-confirmed the row-recorded byte sizes exactly (415476; 1227583; capture 283623), so the live/capture pages match what the row's read note describes.
- No files installed or updated. All shell work ran under `/fast/scratch/hyaku/kotodama-r60a3/AuditA3R02/` (sandbox ≤ ~2.8 MB); no lane write except this report.
