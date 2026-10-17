# R8-F11 — freshness receipt (prior row R6-09-A)

- **Round / axis:** 8 / freshness (targets.json `freshness[10]`)
- **Date:** 2026-10-17 · **Baseline revision:** `e7ca0faeb6680fa9891b907be628d9db578c28f4`
- **Entry:** `corpus/knowledge/civilizations/persia-achaemenid.md`
  (sha256 at check `e50e281be670eae31a101a61c5713c15ac8819bd1c2279a9eb515868172065d0`)
- **Named source:** `http://www.achemenet.com/document/2007.001-Stolper-Tavernier.pdf`
  (Stolper & Tavernier 2007, ARTA 2007.001)
- **Question:** Check Old Persian/Elamite/Babylonian royal trilingualism and its
  administrative limits using an inscription or archive passage; distinguish
  monumental ideology from the languages of all subjects and daily provisioning.
- **Prior disposition:** partial-support. **Prior limits:** Behistun cross-version
  repetition, Hallock pages and subject populations' spoken languages not newly
  verified.
- **This round's worker label:** `partial-support` (raw label preserved; reconciled
  dispositions belong to the parent in `reports/round-8/freshness/reconciliation.json`).
  Passage support: substantive. Whole-claim support: partial.

## Retrieval route (fresh this round)

The live source URL **failed**: `curl` to the http URL returned **HTTP 000 after a
90 s timeout** (window 20:12:34Z–20:14:04Z) and https returned HTTP 000 after 40 s.
The document was retrieved from the pinned Internet Archive capture
`https://web.archive.org/web/20250922051004id_/http://www.achemenet.com/document/2007.001-Stolper-Tavernier.pdf`
(HTTP 200, application/pdf, 1,242,395 bytes, 1.9 s, accessed 2026-10-17T20:15:15Z).

Artifact identity: the fresh copy's sha256
`c7664821696a92d968b8000bdd9ae0b61020680023f3eb29e7bb7d59f79a59f8` is **byte-identical
to the parent's round-6 copy** recorded in the entry tail (lines 178–179). This is a
fresh fetch of the same artifact, not a new edition.

## Main passage — ARTA 2007.001, PDF/printed page 9

> "What is extraordinary is to find Old Persian in an administrative record, a
> "practical" text. It may not demonstrate general use of Old Persian, but even as an
> isolate it indicates wider use than previously supposed."

36 words; extraction `scratch/round8-f11/arta.txt` lines 243–246. The quotation sits on
**page 9**, independently re-deriving the parent's corrected locator (the raw round-6
worker range had been pp. 5–8). The sentence keeps the Fort. 1208-101 counterexample
bounded — it does not license general practical use.

## Corroborating retrievals

**1. Hallock, *Persepolis Fortification Tablets*, OIP XCII (1969) — primary edition,
first-hand this round.** The round-6 blocker is cleared: the Oriental Institute OIP-92
page now exposes a direct PDF href to ISAC's S3
(`oip92.pdf`, 58,797,092 bytes, HTTP 200, accessed 2026-10-17T20:15:33Z,
sha256 `3d9ee70f…4ab41d`).

- Printed p. 6 = PDF p. 16: "the official who had provided the travelers with a
  "sealed document" (halmi) or "authorization" (miyatukkam) … Although the authorizing
  documents are mentioned again and again, **our texts include no actual document of
  this nature.**"
- Printed p. 6: "Presumably, like the other fortification texts, they all come from
  **Persis and southern Elam** (in certain texts this is clearly stated or indicated)."
- Printed p. 6: "Thus the "fast messengers" (m.pirradaziS) presumably used the
  "express" (pirradaziS)horses." — the last two tokens run together in the scan/OCR
  and are reproduced that way; elsewhere OCR hyphenation across a line break was
  joined ("authoriz-ing documents" → "authorizing documents").
- Printed p. 42 = PDF p. 52: "One is pirradazis … meaning "express-runner" …
  Although I translate pirradazisas "fast messenger" when it refers to persons in the
  Q texts (and also in PF 300), **it is not clear that it is a title in the strict
  sense.**"

Page mapping was verified from running heads (PDF 14='4', 18='8', 20='10', 22='12',
24='14', 52='42', 53='43'). The PDF is OCR of a printed scan: diacritics and italics
are partly lost ("pirradaziS", "pirradazisas", "pirradazigis"); quotes are transcribed
exactly as OCR'd, with two normalizations: line-break hyphenation was joined
("authoriz-ing" → "authorizing"), and one run-together token is kept as scanned
("(pirradaziS)horses"). On the Livius page, a space that its link markup introduces
before a closing parenthesis ("Achaemenid Empire )") was normalized to "Empire)".
Every quotation in this receipt was machine-checked against the retrieved artifacts
after whitespace normalization, HTML tag removal and hyphenation joining; all match
modulo the two normalizations documented here.
These passages supply the wording behind entry lines 118–122.

**2. Parian 2017, "A New Edition of the Elamite Version of the Behistun Inscription
(I)", CDLB 2017:3 — peer-reviewed** (`https://cdli.mpiwg-berlin.mpg.de/articles/cdlb/2017-3`,
HTTP 200, accessed 2026-10-17T20:17:50Z; original host `cdli.ucla.edu` failed with DNS
error 6).

> "This monument consists of a relief sculpture and a tri-lingual inscription in Old
> Persian, Elamite and Babylonian Akkadian." (§2.1)
>
> "The older Elamite version of the Behistun inscription was engraved to the right of
> the sculptured reliefs. But since it became necessary later to make room for the
> relief of the captured Scythian rebel "Skunxa," this version was erased by the same
> engravers and then, as its copy, the newer Elamite version was written beneath the
> Babylonian version." (§3.1)

Supports the entry's line 54 "different composition histories and coverage"; the
article does not itself discuss the column-five appendix.

**3. Livius.org, "Behistun" — the entry's own cited overview (line 59)**
(`https://www.livius.org/articles/place/behistun/`, HTTP 200, accessed
2026-10-17T20:16:21Z).

> "The text consists of four columns and an appendix and has a total length of about
> 515 lines. Another panel telling more or less the same story in Babylonian. The
> appendix ("column five") is missing. A third panel with the same text in Elamite
> (the language of the administration of the Achaemenid Empire). This translation of
> the Persian text has a length of 650 lines. Again, the appendix is missing."

Re-verifies the residual's Behistun cross-version leg for entry line 59, with the
caveat that this is a reference page (and its "missing" wording also reflects panel
damage), not an edition or collation.

**4. ARTA pp. 2 and 22 — administrative limits.**

- p. 2: "Persepolis included documents of three main kinds: tablets and fragments with
  texts in Elamite language … tablets and fragments with texts in Aramaic language …
  and tablets or tags with seal impressions but no discernible texts. These were
  products of **three strands of a single information system** …"
- p. 22 (quoting David Lewis): "This makes Persepolis administration a complex
  linguistic phenomenon, even at the level of script. **At the level of speech … the
  position will have been even worse** …"
- p. 22: "The Persepolis Fortification Archive reflects **interplay among several
  streams of information** … (hence the Elamite and Aramaic tablets) … (hence the
  Greek and Old Persian tablets)."

## Leg status

| Leg of the residual question | Status |
|---|---|
| Behistun repeats the king's claim across OP/Elamite/Babylonian (monumental) | supported (CDLB, livius) |
| DB versions not mechanically identical; OP column-five appendix absent from Elamite/Babylonian panels | supported by reference-site statement |
| OP corpus royal-dominated; not every subject's language; ARTA isolate bounded | supported (ARTA p. 9) |
| Daily provisioning in other media (Elamite + Aramaic strand; Greek/OP latitude) | supported (ARTA pp. 2, 22; Hallock p. 6) |
| Credential versus record (halmi/miyatukkam cited, no specimen) | supported (Hallock p. 6) |
| Languages actually spoken by all imperial subjects | not established — and not claimed by the entry (line 48) |

## Negative sweeps

- `grep -i "spoken|speech|vernacular|mother tongue|native language"` over the fresh
  ARTA extraction (1,008 lines) returns only line 796, inside the quoted Lewis remark;
  the same pattern over the first 4,000 lines of the fresh Hallock extraction
  (introduction, printed pp. 1–40) returns **no match**. Commands run 2026-10-17 in
  `/tmp/r8f11`. Conclusion: no retrieved passage speaks to subject-population speech.
- The credential gap is asserted by the source itself (Hallock p. 6, quoted above),
  not inferred.
- This receipt does not restate Fort. 1208-101's individual readings, preserving the
  entry's deliberate restraint at line 47. Correction made during verification: the
  ARTA article **does** carry its own transliteration and word-level commentary for the
  tablet (PDF pp. 11–13; extraction `scratch/round8-f11/arta.txt` lines 363–420 —
  dimensions, "Baked after c. 1975.", obverse lines 1–9, lower edge line 10, reverse
  lines 11–13, cylinder-seal description). The entry's restraint is therefore its own
  editorial choice, not a limit of the source.

## Documented access failures

| Attempt | Command / URL | Result |
|---|---|---|
| Live ARTA PDF (http) | `curl --max-time 90 http://www.achemenet.com/document/2007.001-Stolper-Tavernier.pdf` | HTTP 000, 0 bytes, curl error 28 after 90,001 ms |
| Live ARTA PDF (https) | `curl --max-time 40 https://www.achemenet.com/document/2007.001-Stolper-Tavernier.pdf` | HTTP 000, 0 bytes, timed out |
| Iranica "Bisitun iii" | `curl -sSL https://www.iranicaonline.org/articles/bisotun-iii/` | HTTP 403, 5,485 bytes (automated access refused) |
| Internet Archive fallback for Iranica | `archive.org/wayback/available`, CDX prefix `iranicaonline.org/articles/bisitun*` | "Internet Archive: Temporarily Offline" (transient; CDX and PDF endpoints served minutes earlier) |
| CDLI original host | `curl https://cdli.ucla.edu/pubs/cdlb/2017/cdlb2017_003.html` | curl error 6, could not resolve host; mirrors cdli.mpiwg-berlin.mpg.de and cdli.earth both HTTP 200, identical bytes |

## Limits

The ARTA retrieval is a fresh fetch of the same artifact (identical sha256 to the
round-6 copy), not a new edition; the "practical text" sentence remains the authors'
isolate assessment. Hallock evidence is OCR of a 1969 scan (diacritics lost; page
numbers mapped from running heads). The appendix statement rests on a reference page,
not an edition; the physical state of the panels (damage versus absence) was not
inspected, and no scholarly cross-check of that sentence was retrievable this round
(Iranica 403). No source retrieved this round establishes subject-population spoken
languages, and none is claimed. No PDF or extraction is published in the repository;
artifacts live only in the git-ignored scratch
`reports/supplement-opencode-1/scratch/round8-f11/`.

## Artifacts

`reports/supplement-opencode-1/scratch/round8-f11/` — `arta-wb.pdf`
(sha256 `c7664821…59f79a59f8`), `arta.txt`, `oip92.pdf`
(sha256 `3d9ee70f…4ab41d`), `oip92.txt`, `livius-behistun.html`
(sha256 `ce1ace5d…c816e8c`), `cdlb-ddb519.html`
(sha256 `36f1bdf1…d428803c`). Machine-readable companion:
`reports/round-8/freshness/R8-F11-receipt.json`.
