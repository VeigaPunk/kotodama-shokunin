# R9-F02b — freshness receipt: scholarly-fulltext hunt for the kaunakes residual

- Round: 9 (2026-10-17) · Claim: F / freshness · Shard: **FRESHNESS R9-F02b — scholarly-fulltext hunter**
- Residual: `R9-R8-F02` (prior rows `R8-F02`, `R6-02-B`) · Entry under test: `corpus/knowledge/civilizations/mesopotamia-sumer-akkad.md` (sha256 `bf6c92f9a347d361a37f5aa1080d9d04ac6d37d56c01b0ea92e87ed697a4b478`, 195 lines, unchanged this round)
- JSON companion: `reports/round-9/freshness/R9-F02b-receipt.json`

**Question.** Check its kaunakes or tufted/skirt-dress terminology against a dated object or scholarly source; distinguish modern/Greek descriptive naming, pictured texture and actual fibre/garment construction.

**Escalation this round.** Round 8 closed this residual `unresolved` with one named gap: *"UNRESOLVED: Breniquet's article remains unread"* — its scholarly leg rested on page-referenced quotations relayed by Jaramago 2023. This shard's job was the fulltext hunt for exactly that. The hunt produced the article in full.

## The flag (what was unread is now read)

**Breniquet, C. (2016), "Que savons-nous exactement du kaunakès mésopotamien ?", *Revue d'assyriologie et d'archéologie orientale* 110/1, pp. 1–22** — retrieved in full (23-page publisher PDF, 84,993 bytes of extracted text, page footers intact; local `~/.cache/r9f02b/jina-cairn.txt`, sha256 `105fe5e2…`).

Route, recorded honestly: Unpaywall reports the DOI `10.3917/assy.110.0001` as publisher-OA (`is_oa true`, `host_type publisher`, `publishedVersion`); the direct fetch from `cairn.info` and from `cairn-int.info` is bot-blocked (HTTP 403, DataDome, twice, both via `curl` and via `FetchURL`); the PDF text was obtained through the `r.jina.ai` reader proxy (HTTP 200), whose output preserves the publisher's own page footers (`Presses Universitaires de France | Téléchargé le 17/10/2026 sur https://shs.cairn.info`).

Decisive passages, with printed-page anchors computed from the running heads/footers in that text (the p. 9 anchor cross-validates against Jaramago 2023 fn. 26's own citation "Breniquet, 2016: 9"):

| p. | quotation (verbatim, French) | what it settles |
|---|---|---|
| 7 | "…le terme même fut relégué parmi les **appellations conventionnelles**, faute d'un consensus. C'est dans ce sens générique qu'on l'entend encore aujourd'hui." | the label is a scholarly convention, not a native term |
| 7 | "La première est **l'extrême difficulté à pouvoir reconnaître le matériau** et parfois même la technique de fabrication des vêtements sur les documents figurés." | pictured texture does not yield fibre/technique |
| 9 | "…nous sommes bien embarrassée **pour nommer notre kaunakès**. Aurions-nous le mot qu'il serait difficile de l'associer à une image précise… Aucun terme ne paraît correspondre précisément à une réalité." | no Sumerian/Akkadian term for the protodynastic garment |
| 9 | "le terme **aguhhum pourrait désigner** un textile tissé (et non un simple vêtement) avec de longues mèches de laine… réservé à des usages liturgiques désuets" | the only native candidate is explicitly hedged (Mari, Old Babylonian) |
| 11 | "soit le textile est un tissu…, soit c'est une autre structure textile, simple filet ou résille… ; soit les « mèches » sont prises dans sa structure, **soit elles sont rapportées**." | the construction is an open pair of alternatives |
| 13 | "la question du kaunakès trouve difficilement une réponse, elle n'est **qu'un pur produit de l'historiographie**." | the "kaunakes problem" is a modern construct |
| 14 | "non pas « le » kaunakès, mais « **les** » kaunakès… des textiles ornementés" · "La présence de **bordures tissées écarte toute possibilité que le kaunakès soit une simple toison**. Nous ignorons tout en revanche des détails techniques précis…" | woven borders exclude a plain fleece; technical details remain unknown |
| 14 | "Laine et lin en sont les deux fibres principales." | fibre plurality for the era |
| 22 | "It remains unclear if this piece is an animal fleece or a true fabric, as no archaeological sample of this cloth was found." | the author's own abstract states the open question |

Two first-hand bibliographic pins also come out of this article: its reference list dates the 2013 chapter ("Functions and Uses of …", Oxbow ATS 12, **pp. 1–25**) — so the "woven base or net" sentence relayed by Jaramago sits at p. 5 of a chapter that remains paywalled — and it locates the 19th-century origin memo (Heuzey, "Une étoffe chaldéenne (le kaunakès)", *Les origines orientales de l'art*, **pp. 120–136**).

## Retrieval index

| id | kind | source (accessed 2026-10-17) |
|---|---|---|
| S1 | peer-reviewed journal full text | Breniquet 2016, RA 110, pp. 1–22 — publisher PDF via reader proxy (Cairn direct: 403) |
| S2 | peer-reviewed museum-journal full text | Jaramago 2023, *Boletín del MAN* 42/2023, pp. 465–484 (round-8 P8, re-read at body level) |
| S3 | open-access book chapter full text | Breniquet & Michel 2024, *The Common Thread* (Brepols), pp. 71–77 — HAL `hal-04850023` |
| S4 | public-domain monograph text | Heuzey 1922, *Histoire du costume antique d'après des études sur le modèle vivant* — archive.org DjVu text layer |
| S5 | book front matter (identification) | Kawami 2018, "Elamite dress and textiles", *The Elamite World*, pp. 673–694 — DOI + first-hand TOC |
| S6 | teaching-journal PDF (not used as support) | Liñeiro, *Reflexión Académica* 19 (Palermo) — quoted only as the un-hedged fleece reading the entry guards against |
| S7 | chapter identification record | Breniquet 2013, Oxbow ATS 12, pp. 1–25 — DOI `10.2307/j.ctvh1dvx0.4` |

Supporting legs from S2/S3/S4: the article's own "known in the traditional bibliography as kaunakes" (p. 469); row counts that disagree between specialists (3–6 vs 2–7, p. 470); Heuzey's method of dressing live models in modern textiles (1922 frontispiece and preface p. XII; documented again in Breniquet & Michel 2024, whose bibliography pins Heuzey's 1886 memo — the dated act of applying the Greek word to the "Chaldean" fabric).

## What stays unreadable (deeper-limit statement)

1. **Kawami 2018 chapter body** (*The Elamite World*, pp. 673–694): Routledge paywall; Taylor & Francis HTTP 403 through the reader proxy; no open copy in HAL, OpenAlex or archive.org. DOI, page range and TOC are pinned, the text is not.
2. **Breniquet 2013 chapter body** (Oxbow ATS 12, pp. 1–25): JSTOR landing page carries only the book description; the "woven base or net" sentence remains known only as quoted by Jaramago 2023 fn. 26.
3. **Cherblanc 1937 *Le kaunakès*** and the **Heuzey 1886/1892 memo text**: no open copy located (archive.org title queries `numFound 0`; Gallica SRU HTTP 403).
4. **"The Mesopotamian kaunakes" (2023, Egyptian OA journal)**: host `archmu.journals.ekb.eg` does not resolve from this environment (no A record; DOI resolution timed out).
5. **Fibre/construction per object** stays an explicit open plurality in the specialist's own text; this receipt asserts no single reading.

## Access failures (attempted command + status, 2026-10-17)

Cairn direct PDF twice (403 DataDome) · Cairn-int mirror 403 · FetchURL of the Cairn PDF 403 · JSTOR chapter body (landing page only) · Taylor & Francis 403 (`AbuseAlleviationError`) · `archmu.journals.ekb.eg` DNS failure (two PDFs + DOI) · Gallica SRU 403 · Academia.edu full text (abstract teaser only) · Semantic Scholar 429, CORE needs a key, Google Books API 429 quota · researchgate.net 403 (carried over from round 8). All ten are recorded in the JSON with the exact command and status.

**Negative sweeps.** `grep -n -i "kaunak"` on the entry → no matches, exit 1. `grep -c -i "kaunak"` on the Heuzey 1922 text layer → 0 (cited for method and date only). Round-8 overlap sweep: `cairn 2, jstor 3, archive.org 1`, all inside round 8's *failure* lines; `jina, hal.science, crossref, unpaywall, dspace.palermo, ancientportsantiques, taylorfrancis` → 0; `man.es 1` — the single shared retrieved document.

## Disposition

**`partial-support-or-better`** for the residual's scholarly leg: the paper the earlier rounds recorded as unread is now read first-hand, and its wording corroborates the entry's row (line 142) and its limit column rather than contradicting them — the naming is a convention, the material and technique are explicitly hard to read off images, and the specialist's own reading (woven borders exclude a plain fleece) still leaves the technical details unknown. Raw round-6 labels (`supported` / `whole-bounded-claim`) are preserved verbatim in the JSON and are not rewritten by this disposition. No entry edit is proposed by this shard.

## Verification

- Self-check: `python3 -c "import json;d=json.load(open('reports/round-9/freshness/R9-F02b-receipt.json'));print(d['id'],len(d['retrievals']),sum(len(r['passages']) for r in d['retrievals']),len(d['access_failures']))"` → **`R9-F02b 7 24 10`**.
- Runner conformance (read-only import of `reports/round-9/run-validation.py`; `validation.json` untouched): the receipt binds to `R9-R8-F02`; for the row the runner sees 71 nested retrieval units, 52 passages (**44 primary/scholarly**), 1801 limit tokens, disposition state **partial-or-better**, and all escalation markers present.
- **Finding for the runner owner (R9-O16), not fixed here:** in `reports/round-9/run-validation.py` (sha256 `67a2894e…`) `first_match()` returns a *value* but `receipt_failures()` passes that value into `node.get()` as if it were a key, so `documented_failures` counts **0 for every receipt** no matter what it contains (checked directly: this receipt's 10 attempted-command/status pairs → 0 counted; the same pair re-derived by hand → 10). Claim F is unaffected for this residual because its receipts carry 44 primary/scholarly passages, so the "neither a passage nor a failure" guard cannot fire.

## Reproduction

```bash
# stage 1+2 (quotations sliced verbatim from the retrieved files)
python3 ~/.cache/r9f02b/build_receipt.py && python3 ~/.cache/r9f02b/finalize_receipt.py
# self-check (expected: R9-F02b 7 24 10)
python3 -c "import json;d=json.load(open('reports/round-9/freshness/R9-F02b-receipt.json'));print(d['id'],len(d['retrievals']),sum(len(r['passages']) for r in d['retrievals']),len(d['access_failures']))"
# shared counting command
python3 reports/round-9/run-validation.py
```

Downloads live in `~/.cache/r9f02b/` (the host's `/tmp` is at 100% inode use: `curl` error 23 / `OSError [Errno 28]`), so no bytes were added to the repo besides this receipt pair.
