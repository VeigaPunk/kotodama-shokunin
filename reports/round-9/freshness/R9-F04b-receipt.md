# R9-F04b — Melqart / *mlqrt* scholarly-fulltext hunt (round 9 escalation)

- **id**: R9-F04b · **role**: scholarly-fulltext hunter for residual **R8-F04** (prior row `R6-07-A`; round-8 receipt `reports/round-8/freshness/R8-F04-receipt.json`, raw label `partial-support`, reconciled `unresolved`)
- **entry**: `corpus/knowledge/civilizations/levant-canaan-phoenician.md` (§4 bullet 1 — **line 78** today; sha256 `2ca21052…e4da`)
- **entry drift**: `git diff e1694bad… -- <entry>` is **empty** — the file is byte-identical to the round-8 admit commit; the round-8 hash note (`a2c548aa…`) was measured mid-round before that pass landed. No drift against the round-9 baseline revision.
- **accessed**: 2026-10-17, session from ~20:48Z onward (clock reading 2026-10-17T20:48:09Z); all artifacts hash-pinned below
- **counting command**: `python3 reports/round-9/run-validation.py`

Tested claim (line 78): *"The name mlqrt, conventionally Melqart, is understood as 'king of the city'; its civic semantics are more productive than assigning the god the modern job 'patron of merchants' alone (Bonnet 1988)."*

Round 8 left two named items unread: **Bonnet 1988** and **Lipiński's page**. This hunt attacked both.

## Passages retrieved

**S1 — Lipiński, *Semitic Languages: Outline of a Comparative Grammar* (OLA 80, Peeters **1997**, first edition) — the relayed source itself, now read.** Digitised copy at [eyobkelemework.wordpress.com mirror](https://eyobkelemework.wordpress.com/wp-content/uploads/2013/12/semitic-languages-outline-of-a-comparative-grammar.pdf) · artifact `~/r9-scratch/lipinski1997_wp.pdf`, sha256 `11982779862b…72cf7d2e`, 21,929,634 B, 756 pp. (ABBYY OCR layer).

> p. 228 (§29.55): "some Phoenician divine names as Mlqrt, "Melqart", from milk ("king") + qart ("city")…"
> p. 196 (§27.20): "A similar development gave rise to the divine name Mlqrt < *milk qart, "the king of the City", and to mlkty < *milk Kitti, "king of Kition"."
> p. 188 (§27.4 d)): "in the Phoenician name of the god mlqrt < *milk-qart, "the king of the city""

Printed folios verified from the pages' own running heads; the General Index lists `Mlqrt "Melqart" 27.20; 29.55` — nothing else. **Edition caveat**: the relay cites "Lipiński **2002**, p. 235" (2nd ed., 2001/780 pp.); this copy is the 1997 first edition, so literal p. 235 stays `to-verify` — the **content** is verified three times in the grammar's own text.

**S2 — Jourdain-Annequin's peer-reviewed review of Bonnet 1988** (*Revue des Études Anciennes* 92, 1990, no. 3–4, pp. 446–449), [persee.fr](https://www.persee.fr/doc/rea_0035-2004_1990_num_92_3_5573_t1_0446_0000_3) — page-anchored witness to the book.

> p. 447: "Nous disposons donc désormais d'un recensement exhaustif et critique des testimonia relatifs aux cultes et aux mythes de Melqart dans le bassin méditerranéen…"
> p. 448: "«Melqart est, en terre phénicienne, l'avatar stricto sensu d'une lignée d'ancêtres royaux divinisés» propose l'auteur (p. 417)"; "le Baal de Tyr s'affirmant alors comme «l'expression culminante de ce phénomène de la religion urbaine» (p. 431)"
> p. 449: "il concentrait entre ses mains «un éventail toujours plus large de prérogatives» (p. 432)"

The review (book = thesis, Liège 1987) reports a **dynastic-royal and urban** profile of Melqart and quotes the book at pp. 417/421/431/432/436; a keyword sweep of all four review pages for *marchand / commerce / négoc / trafic / merchant* returns **0 hits**. Quotations are Persée's OCR text layer for the scanned pages.

**S3 — Bonnet 2009, open-access chapter, author-signed** (Hal, [hal-01996916](https://hal.science/hal-01996916/document); body image-only, read via 150/300-dpi page renders; sha256 `d4f3fe4a…8057e1`). The article is cited as pp. 295–308; the **PDF page numbers (3 and 5 of 10) are the exact anchors** — the printed folios on this scan are not reliably readable (the verso digit is eroded; best read ~298).

> PDF p. 3 (≈ printed p. 295, Résumé): "on envisage ici le cas de Melqart, dieu poliade de Tyr, associé au moment de la fondation de la ville et du sanctuaire, mais aussi dieu de l'expansion et des établissements coloniaux"
> PDF p. 5 n. 10 (folio ≈298): "Sur Melqart, je renvoie à ma synthèse: C. BONNET, Melqart. Cultes et mythes de l'Héraclès tyrien en Méditerranée, Namur-Louvain, 1988."

The author's own later framing is city/foundation/expansion — and the footnote names the 1988 book as **"ma synthèse"**, closing the attribution loop for the entry's `(Bonnet 1988)`.

Sibling escalation shards landed the same session (R9-F04a primary-source, R9-F04c alternate-angle); R9-F04a's whole-claim verdict reads `partial-support` (raw label), converging with this shard's `partial-support (escalated)`.

**S4 — HAL `hal-01853704`** (API, 2026-10-17): record exists (Bonnet, 1988) but **no `fileMain_s`/`files_s`** — the monograph is still metadata-only; the book's own pages remain unread.

## Access failures (attempted command → status)

- **e-learning.tsu.ge** (institutional copy of the Lipiński PDF): `curl … --max-time 120` → `(28) Resolving timed out after 120001 ms`, HTTP 000; follow-up `getent hosts` / `dig @1.1.1.1` empty → **DNS-dead this session**; mirror used instead.
- **HathiTrust catalog**: HTTP **403** (Cloudflare "Just a moment…"); **Google Books API**: HTTP **429** (daily quota exhausted); **Open Library**: curl (28) timeout; **archive.org** title/fulltext sweeps: no such book (6/18 hits, none Bonnet 1988; archive.org itself is back up this round).
- **Persée `docAsPDF`**: HTTP 403 (curl and FetchURL) → page-text service used.
- **melqart.huma-num.fr**: `curl (6) Could not resolve host` — **third consecutive round**; Wayback CDX `[]` and availability `{"archived_snapshots": {}}` (real negatives, archive.org was up). Primary-source hunter owns this target.
- **Environment**: `/tmp` **inode-exhausted** (`df -i`: 1048576/1048576 used; `dd` → "No space left on device"; two curl downloads into /tmp wrote 0 bytes). Artifacts moved to `~/r9-scratch/`; fleet-wide operational note.

## Result

**`partial-support (escalated)`** (raw label; reconciliation is the freshness auditor's). Naming leg: read at source in the very grammar the designated page relays (1997 ed., pp. 188/196/228). Attribution leg: Bonnet 1988 now witnessed at book level by a peer-reviewed review quoting it page-anchored, and by the author's own "ma synthèse" self-citation — but the book's own pages are still unread. Anti-fixing leg: no commercial-role framing in any source retrieved this session (calibrated absence over the retrieved set only).

**Limits**: book body unread (review = second-hand, OCR-mediated); literal "p. 235" in the 2nd edition `to-verify`; the Lipiński copy is an unauthorised third-party digitisation (publisher copy not opened; rights out of province — reported, not absorbed); Bonnet 2009 quotes are vision transcriptions from image pages (crop sha256s recorded); reviewer's silence ≠ book's silence; HathiTrust unchecked (403); WiBiLex author line not re-attempted here.

**Coupling implication**: keep the city-god frame primary (name, poliadic cult, royal house, urban religion, colonial expansion), commercial protection as one late/local function at most, Greek equivalence as late translation instrument; keep the entry's hedges and the `(Bonnet 1988)` citation — but do not quote Bonnet 1988 by page without the book in hand.
