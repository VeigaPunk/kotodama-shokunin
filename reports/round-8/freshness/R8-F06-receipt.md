# R8-F06 freshness receipt — Hittite/Hattic/Luwian/Hurrian language-versus-ritual layering

- receipt: `reports/round-8/freshness/R8-F06-receipt.json` (machine record; this file is its human mirror)
- prior row: `R6-05-A` — disposition `partial-support`; raw round-6 worker label preserved: verdict `supported`, support_scope `whole-bounded-claim` (`corpus/lessons/round-6-sources/05.json`)
- entry: `corpus/knowledge/civilizations/anatolia-hittite.md`, sha256 `5a2a3981a11f19500a224daf53a714d62624db4ac90eb17f9858b184cf1ddf84` — unchanged since round 6 (pure evidence refresh, entry not edited)
- question (verbatim from `reports/round-8/targets.json`): *Check the entry's Hittite/Hattic/Luwian/Hurrian language-versus-ritual layering against a located text or scholarly passage; separate script, language affiliation and a deity's cult provenance.*
- accessed-at for all retrievals: **2026-10-17**
- harness conformance: evaluated read-only against `reports/round-8/run-validation.py` (R8-O15) on 2026-10-17 — row shape `retrieved`, passage/claim fields separate, counted substantive; no validation.json written by this shard. Flat fields the harness reads: `retrieved_passage`, `whole_claim_support`, `source_url`, `accessed_at`, `source_locator`, `source_excerpt`.

## Round-6 limits this receipt targets

1. Hattic non-Indo-European status and the "no demonstrated Caucasian genealogy" claim were not established by the round-6 page.
2. The Taru / Tarḫunt- name forms and the named monographs (Melchert 2003; Soysal 2004; Klinger 1996) were unread.
3. The round-6 source was authored teaching, not repository scholarship.

## Fresh retrievals (8; all carry a quoted passage with a named location)

| id | source | kind | locator | passage support |
|---|---|---|---|---|
| F06-R1 | [UT LRC *Hittite Online*, Lesson 2](https://lrc.la.utexas.edu/eieol/hitol/20) | university teaching | opening commentary; "Reading and Textual Analysis"; IṢ-BAT gloss | supports |
| F06-R2 | [Hattic language — Wikipedia](https://en.wikipedia.org/wiki/Hattic_language) | tertiary | lead; infobox; Classification; Corpus | supports |
| F06-R3 | [Tarḫunna — Wikipedia](https://en.wikipedia.org/wiki/Tar%E1%B8%ABunna) | tertiary | Name; Equivalents | supports |
| F06-R4 | [RlA 15, "Wettergott(heiten). A. Philologisch" §6.1 (D. Schwemer)](https://publikationen.badw.de/de/043880078/043880078.pdf) | scholarly reference work | pp. 84–85; text layer lines 7772–7836 | supports |
| F06-R5 | [Luwian language — Wikipedia](https://en.wikipedia.org/wiki/Luwian_language) | tertiary | lead; Script and dialects; Hieroglyphic Luwian; seals | supports |
| F06-R6 | [UT LRC *Hittite Online*, Series Introduction](https://lrc.la.utexas.edu/eieol/hitol/00) | university teaching | "The Source of the Hittites…" | supports |
| F06-R7 | [Glottolog 5.3, Hattic (hatt1246)](https://glottolog.org/resource/languoid/id/hatt1246.json) | scholarly database record | JSON record fields | supports (absence-of-classification) |
| F06-R8 | [Teshub — Wikipedia](https://en.wikipedia.org/wiki/Teshub) | tertiary | lead | supports |

### Load-bearing passages

**F06-R4 — Reallexikon der Assyriologie 15, § 6.1 "Namen und Traditionsgeflecht", pp. 84–85 (signed D. Schwemer, signature at text-layer line 8176).**
This is the upgrade over round 6: a signed reference-work article, not a teaching page.

> Der hatt. W. heißt Taru (syll. dTa-a-ru, dDa-a-ru, van Gessel, HittPantheon 1, 449−451, gelegentlich auch dŠa-a-ru …; logogr. dIŠKUR bzw. d10)

> Die wichtigste luw. Form des Namens ist die Partizipialbildung Tarḫwant-, Tarḫunt- (keil.-luw. Nom. dIŠKUR/10-an-za [Tarḫwanz], dTar-ḫu-un-za [Tarḫunz] …), wovon heth. ein a-Stamm Tarḫunta- gebildet wird

> Es ist auffällig, dass es sich beim Namen des heth.-luw. W. um ein Appellativ handelt, das keine Entsprechung in anderen indogerm. Panthea hat und lautlich an hatt. Taru anklingt. Es handelt sich daher wahrscheinlich um eine in Anlehnung an hatt. Taru geformte Neubildung (Oettinger 2006, 474). Der heth.-luw. Tarḫu(nta) wäre dann nichts anderes als der von Luwiern und Hethitern adaptierte altanatol.-hatt. W.- und Stiergott.

Reading: Hattic **Taru** and Hittite-Luwian **Tarḫunt-** are distinct traditions in a contact relation (adaptation, "wahrscheinlich"), not one unchanged god — exactly the entry's line-84 calibration. *Quote normalization:* the PDF text layer renders digit `1` as `G` (e.g. `449−45G`) and writes ḫ as `h`+combining ring; normalized to `1`/`10` and `ḫ` with no other change. Raw extraction: `/tmp/rla-wettergott.txt` (sha256 `9d6a5c1a…`), PDF sha256 `154534d8…`.

**F06-R2 — Hattic language (Wikipedia).** "was a non-Indo-European agglutinative language"; infobox family "Unclassified language isolate"; Caucasian (Abkhazo-Adyghean, Kartvelian) and Kassian's Yeniseian/Burushaski links appear only as *proposals*; "No document has been found in which native Hattic-speakers wrote their own language … the explanation 'the priest is now speaking in Hattic'"; bilinguals "CTH 728, 729, 731, 733, and 736".

**F06-R5 — Luwian language (Wikipedia).** Varieties are "known after the scripts in which they were written"; "no consensus as to whether these were a single language or two closely related languages"; "Hieroglyphic Hittite" is obsolete; logogram-only seals make even "a certain attribution of the text to a specific language" impossible.

**F06-R1 — UT LRC Lesson 2.** "Telepenus, son of the Hattic Stormgod"; Middle Hittite copy of an earlier version; Akkadogram IṢ-BAT with "# The Hittite reading is ēpta" (logographic spelling ≠ spoken language inside one clause).

**F06-R3 / F06-R8 — Tarḫunna and Teshub.** "In Hattian … he was called Taru; in Luwian, Tarḫunz (Cuneiform: Tarḫu(wa)nt(a)-, Hieroglyphic: DEUS TONITRUS)"; Teshub "influenced Hittite Tarḫunna and Luwian Tarḫunz, though all of these gods were also worshipped separately from each other".

**F06-R6 — UT LRC Series Introduction.** Hatti (people/land name) vs Hittite (language) separated; cuneiform adopted "from these [Assyrian colonies]"; "Hittite and Luvian and Palaic were the 'big three' Anatolian languages, all being recorded in cuneiform inscriptions".

**F06-R7 — Glottolog record.** `"classification": []`, `"family_pk": null` — Hattic carries no genealogical classification in the reference database.

## Access failures / limits (documented, with attempted command and status)

- `FetchURL https://publikationen.badw.de/…pdf` → **failed**: "Response body too large: 49069107 bytes exceeds maxBytes (10485760)". Resolved with `curl -sSL --max-time 200 -o /tmp/rla-wettergott.pdf <url>` + `pdftotext -layout` (49,069,107 bytes; 35,142 lines).
- `FetchURL https://glottolog.org/resource/languoid/id/hatt1246` (HTML) → returned page shell only (license/footer; JavaScript-rendered), no article text. Resolved via the static `.json` endpoint.
- `FetchURL https://www.die-bibel.de/ressourcen/wibilex/altes-testament/wettergott-wettergoetter` → returned newsletter boilerplate only, no article body (JavaScript-rendered). **No passage from this URL is used.**

## Passage support vs whole-claim support

- **Passage support** is recorded per source above; all 8 retrieval records carry substantive quoted passages (requirement was ≥1 per receipt, ≥8 across the 15 residuals).
- **Whole-claim support: `supported-with-residue`.** All legs of R6-05-A now carry a fresh located passage, including the two legs round 6 named as unchecked (Hattic non-IE / genealogy; Taru and Tarḫunt forms) and the teaching-vs-scholarship limit (upgraded by F06-R4).
- **Residue (not resolved):**
  - Melchert 2003, Soysal 2004 and Klinger 1996 (StBoT 37) still not read directly — Klinger 1996 is cited inside F06-R4's bibliography but was not opened.
  - No cuneiform autograph and no Hattic-language text read directly; Hattic evidence is Hittite-mediated by the sources' own account.
  - "No demonstrated genealogical relation" is supported only as *absence of an accepted classification/demonstration* (F06-R2, F06-R7); the Caucasian/Yeniseian proposals remain live hypotheses and were not read first-hand. `to-verify` for any stronger negative reading.

## Commands

```
sha256sum corpus/knowledge/civilizations/anatolia-hittite.md   # 5a2a3981… (== round-6 before)
curl -sSL --max-time 200 -o /tmp/rla-wettergott.pdf https://publikationen.badw.de/de/043880078/043880078.pdf
pdftotext -layout /tmp/rla-wettergott.pdf /tmp/rla-wettergott.txt
sed -n '7772,7836p' /tmp/rla-wettergott.txt
grep -n 'D. Schwemer' /tmp/rla-wettergott.txt                  # signature, line 8176
python3 reports/round-8/run-validation.py                      # counting command; not present yet (R8-O15 shard)
```

Scope: entry untouched; no canon decisions; no git commit. Handoff stays with the orchestrator.
