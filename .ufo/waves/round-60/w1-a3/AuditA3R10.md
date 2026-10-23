# AuditA3R10 — pre-freeze wording audit, ids S631, S632, S633

Round 60 attempt 3, wave 1 build attack. Audited as the blind support seat will: each
row shown as url, quote, teaches (no `supersedes` prefix), and the entry line(s) citing
the id with the id removed. Every page re-opened live by plain `curl` GET (first URL in
each row; URL literal in the command). No heading/caption/promo/cookie/nav text was
used as a quote anywhere below — each quote is verbatim body text.

## AUDIT S631 OK

- Row: `corpus/SOURCES.md` line 586. Paper: Tahir, "A Discursive Analysis of
  Religio-cultural Perceptions about Evil Eye among Female Residents of Ghareebabad,
  Multan", Global Sociological Review VI(II), 2021.
- Entry line citing it (candidate-entry.md:127):
  `- The prescriber: in Multan, imams are considered spiritual healers who suggest an evil eye amulet and talisman (S631). **B**`
- Fetch evidence: `curl -sS -L https://www.gsrjournal.com/pdf/gsr/d6KYBF41pB.pdf`
  → HTTP 200, application/pdf, 1,037,920 bytes (exactly the row's recorded bytes);
  7 pages; text via `pdftotext`.
- Quote verbatim: row's quote `Most commonly, imams are considered as spiritual
  healers and they suggest evil eye amulet and talisman.` appears verbatim in body
  text — Conclusion section, PDF p. 6 (journal p. 102): "For healing and protection,
  people visit imams and religious leaders. Most commonly, imams are considered as
  spiritual healers and they suggest evil eye amulet and talisman." (pdftotext lines
  585-589; the pdftotext run inserts a line break between "they" and "suggest", no
  hyphenation gap).
- Teaches carried: "who supplied protective amulets in a Pakistani town — imams acting
  as spiritual healers who recommended an evil-eye amulet and talisman" — same
  sentence; "a Pakistani town" = the study site.
- Every clause carried: (a) "in Multan" — the quoted sentence is in the paper's
  Conclusion summarising its own findings; the study population is "Female Residents
  of Ghareebabad, Multan" (title, abstract) and Methodology states Ghareebabad "is
  situated in Multan district" (p. 3). Multan scoping is page-carried. (b) "imams are
  considered spiritual healers" — verbatim in quote. (c) "suggest an evil eye amulet
  and talisman" — verbatim in quote ("evil eye amulet and talisman").
- No universalisation, no added comparison/cause/date/place beyond the page.

## AUDIT S632 OK

- Row: `corpus/SOURCES.md` line 587. Paper: Elnaggar et al. 2025, Multianalytical
  Study of Amuletic and Talismanic Islamic-African Paper Manuscripts in the Slovene
  Ethnographic Museum, ChemPlusChem 90(12), PMC12701302.
- Entry lines citing it (both checked fully; each line cites only S632):
  - candidate-entry.md:73: `- Shape and use: amulets or talismans gain their power first through their customized shape and form and second through being worn or placed, while others can only be activated by reading the text written on them (S632). **B**`
  - candidate-entry.md:109: `- Placement as act: being worn or placed is the second source of an amulet's power after its customized shape, while others can only be activated by reading the text written on them (S632). **B**`
- Fetch evidence: `curl -sS -L https://pmc.ncbi.nlm.nih.gov/articles/PMC12701302/` →
  HTTP 200, text/html; charset=utf-8, 273,314 bytes (exactly the row's recorded bytes).
- Quote verbatim: row's quote `Amulets or talismans gain their power firstly through
  their customized shape and form and secondly through their application by simply
  being worn or placed` is verbatim body text — Discussion, the paragraph after the
  amulet-and-talisman definition. The page sentence continues in the same sentence:
  "…while others can only be activated by reading the text written on them." — so the
  row quote is a verbatim prefix of one continuous body sentence, not a caption or
  fragment.
- Teaches carried: "the paper's synthesis of how Islamic amulets and talismans are
  made and switched on (customised shape, wearing or placing, or reading the written
  text)…" — the page sentence is exactly that synthesis (the tier note correctly flags
  it as a general statement the discussion draws from cited scholarship, ref. [49]).
- Every clause carried, line 73: "gain their power first through their customized
  shape and form" / "second through being worn or placed" / "others can only be
  activated by reading the text written on them" — all in the one page sentence
  ("firstly/secondly" → "first/second", "application by simply being" elided; no added
  content).
- Every clause carried, line 109: "being worn or placed is the second source…after its
  customized shape" restates the same firstly/secondly ordering (inversion preserved:
  placing is second, shape first); "activated by reading the text" clause identical.
- Universal wording is the page's own ("Amulets or talismans gain their power…"), not
  a universal drawn from one object — the sentence sits in the paper's general
  discussion, explicitly the scholarship synthesis the row's teaches describes.

## AUDIT S633 OK

- Row: `corpus/SOURCES.md` line 588. Page: Hassani, "Talismanic Tunic", Visual
  Resources of the Middle East, North Africa, and South Asia (Yale), post 10 June
  2026; object 2021.32.3, shirt from Ghana ca. 1920-50.
- Entry line citing it (candidate-entry.md:100):
  `- Inside the garment: on a Ghanaian talismanic shirt, cowrie shells adorn the neck and leather pouches, presumably containing additional amulets, are sewn into the interior (S633). **C**`
- Fetch evidence: `curl -sS -L https://vrme.yale.edu/posts/2026-06-10-talismanic-tunic`
  → HTTP 200, text/html; charset=UTF-8, 58,701 bytes (exactly the row's recorded
  bytes).
- Quote verbatim: row's quote `Cowrie shells adorn the neck, and leather pouches,
  presumably containing additional amulets, are sewn into the interior of the shirt.`
  is verbatim body text — the essay paragraph describing the shirt's construction
  (follows the sentence on magic squares/hexagrams, precedes "Recent scholarship has
  revealed that talismanic shirts were likely commissioned…").
- Teaches carried: "one Ghanaian talismanic shirt and what carries its protection:
  inscribed Qur'anic text and supplications, magic squares, cowrie shells, and leather
  pouches sewn inside" — the page's essay names exactly these elements on this shirt
  ("Qur'anic verses, Islamic supplications, and amuletic motifs… 'magic squares'
  (awfāq)… Cowrie shells adorn the neck, and leather pouches…").
- Every clause carried: (a) "a Ghanaian talismanic shirt" — header/body: "Talismanic
  Tunic, Ghana, ca. 1920-50… This talismanic shirt (figs. 1-2) from Ghana dates to the
  first half of the twentieth century". (b) "cowrie shells adorn the neck" — verbatim.
  (c) "leather pouches, presumably containing additional amulets" — verbatim
  (page's own hedge "presumably" retained, not stated as fact). (d) "sewn into the
  interior" — verbatim ("of the shirt" elided; equivalent).
- Singular-object scoping: the line claims only what this one shirt carries — no
  universal, no added comparison/contrast/cause/date/place. Page is a named-author
  essay on a Yale site; row tier B with honest tier note.

## Summary

- AUDIT S631 OK — all clauses of the citing line page-carried; quote verbatim body text.
- AUDIT S632 OK — both citing lines fully carried by one body sentence; quote is a
  verbatim prefix of that sentence; teaches matches.
- AUDIT S633 OK — singular-object scoping preserved incl. the page's "presumably"
  hedge; quote verbatim body text.
- No REWRITE, no TEACHES flag. No heading/caption/promo/cookie/nav quotes found.
- Fetch receipts (all live, plain GET, literal URLs): S631 HTTP 200 / 1,037,920 B
  application/pdf; S632 HTTP 200 / 273,314 B text/html; S633 HTTP 200 / 58,701 B
  text/html — each matching its row's recorded byte count.
- No tools installed; no fixtures needed (wording audit only, not a counter receipt).
- Sandbox: /fast/scratch/hyaku/kotodama-r60a3/AuditA3R10/ (s631.pdf, s631.txt,
  s631-p6.txt, s632.html, s633.html) — ~1.4 MB total, no processes left running.
