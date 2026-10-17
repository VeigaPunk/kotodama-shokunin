# R8-F14 freshness receipt — Nubia/Kush Meroitic decipherment vs understanding (R6-12-A)

- **Shard:** targets.json freshness[13] · **Axis:** freshness · **Date:** 2026-10-17 · **Baseline:** `e7ca0faeb6680fa9891b907be628d9db578c28f4`
- **Prior row:** `R6-12-A` (ledger `corpus/lessons/round-6-sources/12.json`) · **Prior disposition:** `partial-support`
- **Raw worker labels preserved:** `verdict: supported`, `support_scope: partial` (reconciliation belongs to `reports/round-8/freshness/reconciliation.json`, the F-integrator's file, not this shard)
- **Entry:** `corpus/knowledge/civilizations/nubia-kush.md`, section “Language family and writing: what is actually deciphered?”, lines 48–52
- **Entry sha256 at recheck:** `351fa8335997659ca81b9c0e645603c4a5cb63f9e97b23e3f76f90e932c4aa0f` — identical to the round-6 baseline, so the recheck applies to unchanged bytes
- **Question:** Check the entry's Meroitic decipherment-versus-understanding and proposed language-family affiliation distinction using a scholarly passage; sound values are not unrestricted translation or identity with Old Nubian.

**Fresh disposition:** passage support `supported` / whole-claim support `partial-support` (unchanged). Two of three legs re-verified against freshly re-downloaded byte-identical files; the third leg (Rowan) upgraded from tertiary-only corroboration to a directly read primary passage, closing the round-6 limit “Rowan's full argument remains unread”. The other round-6 limit (R12 ch. III itself unread) stands.

## Retrieval 1 — main source re-fetch: Rilly 2011, Ityopis

- **URL:** http://www.ityopis.org/Issues-1_files/ITYOPIS-I-Rilly.pdf · **Accessed:** 2026-10-17T20:12:53Z
- **Method:** live re-download this pass, `curl -sS --fail --location --retry 2`; HTTP 200, application/pdf, 418,773 bytes; sha256 `c718e208fb1bfcff17207c2db9cda0940af24576fc3956b886beba80a1b3dd76` — **byte-identical** to the round-6 scratch copy (both hashes computed this pass). 15 pages; `pdftotext -layout` extraction (661 lines, sha256 `f9468027…`).
- **Passages (each ≤40 words, location named):**
  - PDF p. 1 (abstract): “The script was deciphered 100 years ago but the knowledge of the language remains scanty because no bilingual texts were found.” (21 words)
  - PDF p. 1 (abstract): “It belongs to the Nilo-Saharan phylum and more accurately to a sub-branch termed “Northern East Sudanic” (NES), together with Nara, Nubian, Tama and Nyimang.” (24 words)
  - PDF p. 3, printed p. 12: “Both of them were deciphered between 1909 and 1911 by the British Egyptologist Francis Llewelyn Griffith (Griffith 1911).” (18 words)
  - PDF p. 5, printed p. 14: “The Meroitic language is only superficially known, although both scripts were deciphered a hundred years ago.” (16 words)
  - PDF p. 6, printed p. 15: “Meroitic belongs to a sub-group of East Sudanic, which he termed “Northern East Sudanic” (NES), comprizing also Nubian, Nara, Taman and Nyima” (22 words)
  - PDF p. 6, printed p. 15: “The present author recently confirmed his theory (Rilly 2010).” (9 words)

## Retrieval 2 — corroboration re-fetch: Rilly & de Voogt publisher excerpt ([R12])

- **URL:** https://assets.cambridge.org/97811070/08663/excerpt/9781107008663_excerpt.pdf · **Accessed:** 2026-10-17T20:13:30Z
- **Method:** live re-download this pass; HTTP 200, application/pdf, 198,308 bytes; sha256 `b55e1928…` — **byte-identical** to the round-6 copy. 10 pages.
- **Passages:**
  - excerpt PDF p. 4 (Griffith paragraph): “The value of the signs was deciphered, but the vocabulary remained incomprehensible apart from names of people and deities, titles, and place-names.” (22 words) — matches the entry's own [R12, pp. 3–4] citation location.
  - excerpt PDF p. 8: “There are, however, two or perhaps three signs that appear in the Old Nubian alphabet” (15 words) — the “not identity with Old Nubian” leg.

## Retrieval 3 — NEW: Rowan 2006 full argument (round-6 limit closed)

- **URL:** https://eprints.soas.ac.uk/18491/1/Meroitic%20an%20afroasiatic%20language.pdf · **Accessed:** 2026-10-17T20:15:34Z
- **Method:** local `curl` of the eprints URL failed DNS (see failures); `FetchURL` of the same URL returned the article from its opening through §3.1.3 (pp. 169–179). The remainder was read from the Internet Archive capture of the same repository file: https://web.archive.org/web/20240524163800/https://eprints.soas.ac.uk/18491/1/Meroitic%20an%20afroasiatic%20language.pdf — HTTP 200, application/pdf, 377,413 bytes, PDF 1.3, 38 pages, sha256 `a74ac1e8…`; `pdftotext` extraction 2,076 lines (sha256 `e2a167bb…`). Wayback CDX shows application/pdf captures with digest `LKLU6WHVBQDISZLWVM7J4TJPNT4T634E` from 2015–2024 — the archived payload is the repository's file, not a third-party scan.
- **Passages:**
  - printed p. 169: “this paper puts forward the proposal that the investigation should instead be concentrated on the Afroasiatic phylum” (17 words)
  - printed p. 169: “This investigation rests upon the firmest known aspect of the language, namely the phonemic values of the signs and their distribution.” (21 words)
  - printed p. 169: “the affiliation of Meroitic with the Nilo-Saharan Nubian language should finally be abandoned” (13 words)
  - printed p. 195 (§4.7): “it can be proposed from this analysis that the investigation into an affiliation of Meroitic with a related language should be focused upon Afroasiatic languages” (25 words)
  - printed p. 196 (§5): “I will show in this section that through a phonological consonantal compatibility analysis, Meroitic and Old Nubian show no parity.” (20 words)
  - printed p. 201 (§7): “there is no strong evidence against Meroitic not being a member of Afroasiatic, and that on the contrary, the investigation into consonantal compatibility restrictions shows a strong possibility for its inclusion” (31 words)
  - printed p. 201 (§7): “This paper does not make any claims as to the likeliest individual candidate for relatedness with Meroitic, but hopes to redirect this research with promising results.” (26 words)

## Access failures (attempted command + status)

- `curl` of `https://soas-repository.worktribe.com/previewfile/350119/…pdf` → **HTTP 403** (curl exit 22; retried with browser UA + referer, 403 again); `…/file/350106/1/…pdf` also 403.
- `curl` of `https://eprints.soas.ac.uk/18491/1/…pdf` → **curl (6) Could not resolve host** (3 attempts); `getent hosts` exit 2. FetchURL of the same URL succeeded the same minute — local DNS only.
- `curl` of the Wayback capture of the Wikipedia-cited original path `soas.ac.uk/lingfiles/workingpapers/rowan2.pdf` → **HTTP 404** (CDX shows only 301/404 captures; no PDF was ever archived there).
- Semantic Scholar API → **HTTP 429** (rate limit); OpenAlex used instead and yielded the working eprints URL.

## Basis and limits

**Basis.** Fresh retrieval against current bytes reproduces the entry's three-layer distinction: (1) sign values deciphered (Griffith 1909–1911) versus language “only superficially known”; (2) the affiliation stated as a proposal by its proposer (Rilly's “recently confirmed his theory”), not settled genealogy — and Rilly writes “Northern East Sudanic” where the entry writes “North Eastern Sudanic”, the naming variant recorded in round 6; (3) Rowan's Afroasiatic counter-proposal read first-hand: she “puts forward the proposal”, argues the Meroitic–Nubian affiliation “should finally be abandoned”, concludes only “a strong possibility”, makes “no claims as to the likeliest individual candidate”, and her §5 independently denies Meroitic–Old Nubian parity. Her analysis runs on “the phonemic values of the signs”, i.e. the deciphered layer — exactly the separation the entry draws.

**Limits (whole-claim support stays partial).** The entry cites [R12, ch. III]; the book chapter itself remains unread, and a same-author open-access summary is not the chapter. Rowan's paper is itself a contested proposal in a working-papers volume; nothing here adjudicates the classification, and no independent promotion verification is performed. Unrestricted translation remains unverified — no Meroitic text was translated in this pass. No restricted or pirated texts were used: all retrievals are from the official publisher/journal/repository, the repository copy reached via its Internet Archive capture.

## Counts (2026-10-17)

- `python3 -c "import json;d=json.load(open('reports/round-8/freshness/R8-F14-receipt.json'));print(len(d['retrievals']), len(d['access_failures']), sum(len(r['passages']) for r in d['retrievals']))"` → `3 4 15`
- Retrievals succeeded: 3 · substantive passages: 15 quotes across 3 sources, each with a named location and ≤40 words · documented access failures: 4
- Raw scratch (PDFs + extractions) under ignored `reports/supplement-opencode-1/scratch/round8-f14/`; not redistributed.
