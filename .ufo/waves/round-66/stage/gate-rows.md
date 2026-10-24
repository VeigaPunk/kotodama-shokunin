# Round 66 — lesson Gate draft (kotodama-shokunin), 2026-10-24

STATUS: **DRAFT / NOT COMMITTED.** Author: ScribeGateRows (leaf). Integration owner: L1.
Verified rows ready to paste: **19** — S776 plus 18 of the 24 claimed ids (S779, S780, S781,
S782, S784, S785, S786, S787, S788, S789, S790, S791, S792, S793, S794, S796, S799, S800).
Blocked (fragment present, anchor or capture not verifiable): **2** (S783, S795).
Awaiting fragments: **4** (S777, S778, S797, S798).

Destination in the lesson: `corpus/lessons/round-66.md`, `## Gate` section, which
`tools/check-gate-quotes.py` closes at the next `## ` heading.

## Shape contract (round-65 `## Gate` + the frozen checker)

Line shape, copied from `corpus/lessons/round-65.md` `## Gate` (line 21 onward):

    - S### | <live URL> (<capture URL, https:// scheme>) | 2026-10-24 | "<anchor quote>"

Enforced by `tools/check-gate-quotes.py` (read, not modified):

- row must begin `- S<digits>` (`ROW = ^(?:-\s+(?:\*\s+)?|\*\s+)(S\d+)\b`);
- every continuous quote run on the row is `<= 25` words (`MAX_WORDS = 25`); a run is
  grouped by punctuation-only gaps, so two adjacent quoted spans on one row are one run;
- no HTML entities, no ellipsis-joined spans (`html-entity`, `ellipsis-joined`);
- capture locators carry the `https://` scheme (R65-M3: the frozen locator in
  `reports/round-61/reopen-quote.py` matches `https?://...` only; a bare
  `web.archive.org/web/...` capture is never tried);
- `ACCEPT-CA-66` QUOTES leg additionally needs `>= 25` distinct ids matching
  `S(77[6-9]|7[89]\d|800)` somewhere in the lesson and the checker printing `0 finding`.

Obligation inherited from the round-65 Gate preamble: a row whose live URL answers a bot
challenge keeps its located status through the same-page capture listed in its source cell,
and the challenge is named in the row's VERIFY cell, never bypassed. Two landed rows fall in
that class today (S780, S781 - see the per-row table).

## Verified rows (paste-ready, id order)

- S776 | https://www.penn.museum/documents/publications/expedition/58-1/sowing-seeds.pdf (https://web.archive.org/web/20261024111013id_/https://www.penn.museum/documents/publications/expedition/58-1/sowing-seeds.pdf) | 2026-10-24 | "Versions of mancala are traditionally played across Africa and Asia, with gameplay and board dimensions varying considerably between different regions."
- S779 | https://escholarship.org/content/qt0pb1r0w3/qt0pb1r0w3.pdf (https://web.archive.org/web/20231015204944id_/https://escholarship.org/content/qt0pb1r0w3/qt0pb1r0w3.pdf) | 2026-10-24 | "The most famous of all scents was kyphi, known from three versions on temple walls (two at Edfu, one at Philae), from papyri (P. Ebers)"
- S780 | https://www.metmuseum.org/essays/trade-between-arabia-and-the-empires-of-rome-and-asia (https://web.archive.org/web/20260311081454id_/https://www.metmuseum.org/essays/trade-between-arabia-and-the-empires-of-rome-and-asia) | 2026-10-24 | "The Incense Route ran along the western edge of Arabia’s central desert about 100 miles inland from the Red Sea coast"
- S781 | https://ecampusontario.pressbooks.pub/dressandadornmentancientgreece/chapter/perfume-and-scented-oils/ (https://web.archive.org/web/20260511112644id_/https://ecampusontario.pressbooks.pub/dressandadornmentancientgreece/chapter/perfume-and-scented-oils/) | 2026-10-24 | "Beyond its culinary uses, olive oil served as the base for perfumes, cosmetics, and medicines"
- S782 | https://www.iranicaonline.org/articles/atr-perfume/ (https://web.archive.org/web/20251125160314id_/https://www.iranicaonline.org/articles/atr-perfume/) | 2026-10-24 | "large quantities of rose-water were regularly distilled in Persia and Iraq at least from the ninth century"
- S784 | https://ich.unesco.org/en/RL/the-skills-related-to-perfume-in-pays-de-grasse-the-cultivation-of-perfume-plants-the-knowledge-and-processing-of-natural-raw-materials-and-the-art-of-perfume-composition-01207 (https://web.archive.org/web/20260906234122id_/https://ich.unesco.org/en/RL/the-skills-related-to-perfume-in-pays-de-grasse-the-cultivation-of-perfume-plants-the-knowledge-and-processing-of-natural-raw-materials-and-the-art-of-perfume-composition-01207) | 2026-10-24 | "Inscribed in 2018 (13.COM) on the Representative List of the Intangible Cultural Heritage of Humanity"
- S785 | https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S0185-62862016000200045 (https://web.archive.org/web/20250604073907id_/https://www.scielo.org.mx/scielo.php?script=sci_arttext&pid=S0185-62862016000200045) | 2026-10-24 | "its aromatic smoke, that was also considered divine food, allowed the link between deities and humans"
- S786 | https://lockwoodonlinejournals.com/index.php/jaos/article/view/1362 (https://web.archive.org/web/20260811211617id_/https://lockwoodonlinejournals.com/index.php/jaos/article/view/1362) | 2026-10-24 | "elite scent culture had already begun to be transformed by the importation of foreign aromatics"
- S787 | https://www.seiryo-u.ac.jp/u/research/gakkai/ronbunlib/humanities_ronsyu_pdf/No2/04_koiso.pdf (https://web.archive.org/web/20261024113504id_/https://www.seiryo-u.ac.jp/u/research/gakkai/ronbunlib/humanities_ronsyu_pdf/No2/04_koiso.pdf) | 2026-10-24 | "sandalwood paste, incense, pastille, camphor, lamps of burning oil or ghī, and fragranced flowers to the deity"
- S788 | https://david-howes.com/senses/Consert-Odor.htm (https://web.archive.org/web/20260827025307id_/https://david-howes.com/senses/Consert-Odor.htm) | 2026-10-24 | "Men are socialized through initiation and lose their strong-smelling odor. Women, on the other hand, by their very sexuality are strong smelling."
- S789 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8951631/ (https://web.archive.org/web/20250415135912id_/https://pmc.ncbi.nlm.nih.gov/articles/PMC8951631/) | 2026-10-24 | "More than 3000 kg of rose flowers produce 1 kg of rose oil by water distillation."
- S790 | https://collections.vam.ac.uk/item/O78794/pair-of-gloves-unknown/ (https://web.archive.org/web/20260108224147id_/https://collections.vam.ac.uk/item/O78794/pair-of-gloves-unknown/) | 2026-10-24 | "Recipes for scenting gloves survive from the 17th century using ingredients such as musk, ambergris, floral extracts and aromatic spices."
- S791 | https://collections.vam.ac.uk/item/O105969/pomander-unknown/ (https://web.archive.org/web/20240914050836id_/https://collections.vam.ac.uk/item/O105969/pomander-unknown/) | 2026-10-24 | "strong-scented substances had the power to disinfect the air and to ward off plague and other diseases"
- S792 | https://cienciassociales.uniandes.edu.co/opca/articulo/paraiso-perfumado-crear-y-recrear-los-mundos-olfativos-de-los-mayas-del-periodo-clasico%C2%B9/ (https://web.archive.org/web/20240818230454id_/https://cienciassociales.uniandes.edu.co/opca/articulo/paraiso-perfumado-crear-y-recrear-los-mundos-olfativos-de-los-mayas-del-periodo-clasico%C2%B9/) | 2026-10-24 | "como lo registraron observadores españoles con respecto a los palacios aztecas de Centroamérica en el siglo XVI"
- S793 | https://www.nhm.ac.uk/discover/what-is-ambergris.html (https://web.archive.org/web/20261013203536id_/https://www.nhm.ac.uk/discover/what-is-ambergris.html) | 2026-10-24 | "For hundreds of years, perfumers have categorised the quality of ambergris according to its colour"
- S794 | https://www.chateauversailles-recherche.fr/article964.html (https://web.archive.org/web/20260608021222id_/https://www.chateauversailles-recherche.fr/article964.html) | 2026-10-24 | "les gantiers-parfumeurs fabriquent les gants parfumés, dont le succès est à son apogée à la cour de Louis XIV"
- S796 | https://research-information.bris.ac.uk/ws/files/150040263/Bessard_paper_preliminary_edit_FB.pdf (https://web.archive.org/web/20231119220323id_/https://research-information.bris.ac.uk/ws/files/150040263/Bessard_paper_preliminary_edit_FB.pdf) | 2026-10-24 | "designed them to function as a set of defined zones for various commodities and the streets took on the name of the trade plied there"
- S799 | https://knmdb.kyohaku.go.jp/eng/30115.html (https://web.archive.org/web/20261024113446id_/https://knmdb.kyohaku.go.jp/eng/30115.html) | 2026-10-24 | "In these games, over several rounds, a host selects varieties of incense for their guests to savor and identify."
- S800 | https://bmcr.brynmawr.edu/2013/2013.04.46/ (https://web.archive.org/web/20250729161944id_/https://bmcr.brynmawr.edu/2013/2013.04.46/) | 2026-10-24 | "it was an oil press for the production of perfume and not a textile press"

Fragments read for these eight: `rows/ScoutRow02/row-S779.txt`, `rows/ScoutRow02/row-S780.txt`,
`rows/ScoutRow03/row-S781.txt`, `rows/ScoutRow03/row-S782.txt`,
`rows/ScoutRow05/row-S785.txt`, `rows/ScoutRow05/row-S786.txt`, `rows/ScoutRow07/row-S789.txt`,
`rows/ScoutRow07/row-S790.txt`, `rows/ScoutRow08/row-S791.txt`, `rows/ScoutRow08/row-S792.txt`,
`rows/ScoutRow09/row-S793.txt`, `rows/ScoutRow09/row-S794.txt`.
Every quote above is the fragment's own anchor quote, taken verbatim (no rewording, no
trimming); I re-located each one in the fetched body/capture rather than trusting the
fragment's VERIFY line.

## S776 supersession — disposition note

S776 is the S753 durability repair (round-65 verifier spot-check R65-D1). Disposition: S776
**supersedes** S753's capture for the same live URL; S753's registry row stays `mined` (its
live anchor still resolves), the games entry's mancala bullet re-points `(S753) -> (S776)`,
and S753 must be cited zero times by that entry afterwards
(`reports/round-66/accept-ca.py` D1 leg: `s776_citations == 1`, `s753_citations == 0`).

Independently re-verified at drafting time (2026-10-24T11:3xZ), not copied from the seat:

1. live URL `https://www.penn.museum/documents/publications/expedition/58-1/sowing-seeds.pdf`
   answers `206`/`200` `application/pdf` (range probe; the seat's receipt records HEAD 200).
2. fresh capture `20261024111013` replays `200 application/pdf`, `529795` bytes,
   sha256 `cb6ff9b8ef73c176782b12c7b4cada9be63de54feac248069eb009f17e538632`.
3. CDX lists exactly two captures for the URL and **both carry the same digest**
   `F5PON6QPZ4DXOBF5DE2MQCTJPNVBUZVC`, so the fresh capture is byte-identical to the archived
   original and to the live PDF - this is what "replays byte-exact" in claims.json Ca rests on.
4. the anchor quote is present verbatim in the fresh capture after whitespace normalisation,
   and it is present only under **plain** `pdftotext`, not `pdftotext -layout` (see finding 7).
5. the old timestamp `20250926172224` no longer replays its own bytes: requested over HTTP it
   302-redirects to the `20261024111013` replay (same bytes), so archive.org is substituting
   the new capture. This confirms the R65-D1 premise; do not restore the old timestamp.

Row-shape consequence: S776's registry source cell must carry its capture **with the
`https://` scheme** (`https://web.archive.org/web/20261024111013id_/...`). S753's own cell
still carries the scheme-less form, so copying S753's cell shape into S776 re-introduces the
R65-M3 locator defect (finding 4 below).

## Awaiting fragments (4 rows - NOT paste-ready)

No fragment for these four ids exists under `.ufo/waves/round-66/rows/` as of
2026-10-24T12:20Z, so no quote is asserted and no gate line is drafted. Listed with their
owning seat and the spec's target so the L1 can check the output the moment it lands:

- S777 — awaiting fragment: `rows/ScoutRow01/row-S777.txt` (target: UNESCO intangible-heritage incense listing, UAE/Omani Arabian incense craft)
- S778 — awaiting fragment: `rows/ScoutRow01/row-S778.txt` (target: kodo Japanese incense ceremony, museum/scholarly)
- S797 — awaiting fragment: `rows/ScoutRow11/row-S797.txt` (target: scented oils and anointing, Egypt and Near East)
- S798 — awaiting fragment: `rows/ScoutRow11/row-S798.txt` (target: alabastron / aryballos perfume vessels)

## Blocked rows — fragment on disk, gate line withheld (2)

Both fragments exist and were read; neither yields a gate line I can stand behind, so neither
is drafted. Neither is "awaiting" anything except a repair by its owner.

- **S783** (`rows/ScoutRow04/row-S783.txt`) - the anchor carries **nested straight quotes**:
  `"first-named, alcohol-based perfume, "Hungary water" is believed to have been produced
  around 1370"`. `tools/check-row-fragments.py` parses the first span only and reports
  `quote-words: S783:5` (its floor is 8), and any Gate line built from it splits into two
  spans with `is believed...` between them. Repair the anchor to one unbroken span (inner
  title in single or curly quotes) and it can be gated. Evidence is otherwise good: live 200
  (27739 B) and capture `20201101061450` 200 (27133 B) both contain the sentence.
- **S795** (`rows/ScoutRow10/row-S795.txt`) - the capture is **not a same-page capture**:
  the source cell pairs the archive.org PDF with `web.archive.org/web/20251011060403id_/https://www.jstor.org/stable/1005923`
  (the JSTOR landing page), and `check-row-fragments.py` reports
  `capture-url-mismatch: S795:https://jstor.org/stable/1005923 != https://archive.org/download/...1005923.pdf`.
  The fragment's own CAPTURE line states the reason (no Wayback capture for that download URL;
  a fresh save answered HTTP 523). Separately, the quote is **OCR-interleaved** in the 8,751,290-byte
  PDF: the two lines read `By burningincense[we] knowthe | night, With graduated candle [we]
  confirmthe tally of | the watches.` across a column gutter, so a contiguous substring test
  fails while the poem is plainly there. That names the wording and the page; it does not give
  the CAPTURE leg a same-page capture.

A row id that is missing from this Gate after integration costs two legs at once: the row's
own absence and the `>= 25 gate_ids` requirement of ACCEPT-CA-66 QUOTES (25 ids needed:
S776 + S777-S800).

**Do not integrate this pending list.** These lines still match the checker's `ROW` regex
(it only needs `- S<id>`), and the QUOTES leg counts ids anywhere in the lesson file, so
pasting the list would satisfy `len(gate_ids) >= 25` with zero anchored quotes. The id count
must come from real rows; each line above must be replaced by a fragment-backed row, not
supplemented.

## Per-row probe table (my measurements, 2026-10-24T11:36-12:15Z)

| id | live probe | capture probe | quote words | teaches len | challenge class |
|---|---|---|---|---|---|
| S776 | 206/200 `application/pdf` | 20261024111013 -> 200 pdf, 529795 B | 20 | n/a (row not yet in SOURCES.md) | none |
| S779 | 200 `application/pdf`, 588894 B | 200 pdf, 588894 B, digest-equal | 25 (at cap) | 191 | live bare curl gets 202 empty body; browser UA needed (fragment states it) |
| S780 | **429** `text/html` (Vercel Security Checkpoint) | 200, 120339 B, quote verbatim | 21 | 175 | live challenge, capture locates |
| S781 | **403** to `-A Mozilla`, **200** to full Chrome UA (93515 B) | 200, 94069 B, quote verbatim | 15 | 216 | UA-sensitive live server |
| S782 | 200, 376940 B | 200, gzip body decodes, quote verbatim | 17 | 239 (1 under cap) | none |
| S785 | 200, 123616 B | 200, 124982 B, quote verbatim | 16 | 221 | none |
| S786 | 200, 45032 B | 200, 9860 B zstd-encoded, 45391 B decoded, quote verbatim | 15 | 235 | capture stored as `content-encoding: zstd` |
| S791 | 200, 61493 B | 200, 59919 B, quote verbatim | 17 | **242 (>240)** | none |
| S792 | 200, 184045 B | 200, 168231 B, quote verbatim | 17 | **260 (>240)** | none |
| S789 | 200, 249918 B | 200, 246314 B, quote verbatim | 16 | **260 (>240)** | none |
| S790 | 200, 52730 B | 200, 52164 B, quote verbatim | 20 | **258 (>240)** | none |
| S793 | 200, 254761 B (fragment) / quote verbatim | 200, 55782 B, quote verbatim | 15 | **256 (>240)** | none |
| S794 | 200, 51511 B (fragment) / quote verbatim | 200, 50770 B, quote verbatim | 19 | **264 (>240)** | none |
| S784 | 200, 155824 B | 200, 22847 B, quote verbatim | 15 | 209 | none (UNESCO ICH listing) |
| S787 | 200, 701396 B | 200, 701396 B (fresh save 20261024113504), quote verbatim | 17 | 215 | none |
| S788 | 200, 22050 B | 200, 9419 B, quote verbatim | 22 | 221 | none |
| S796 | 200, 487491 B pdf | 200, 493286 B pdf, quote verbatim | 25 (at cap) | **271 (>240)** | none |
| S799 | 200, 13625 B | 200, 13625 B (fresh save 20261024113446), quote verbatim | 19 | 203 | none |
| S800 | 200, 51003 B | 200, 12708 B, quote verbatim | 15 | 210 | capture note: fresh save timed out, 2025 capture kept |
| S783 | 200, 27739 B | 200, 27133 B, sentence present | 13 (nested quotes) | 227 | **blocked: anchor malformed** |
| S795 | 200, 8751290 B pdf, poem OCR-interleaved | 200, 3980 B JSTOR landing page only | 20 | **249 (>240)** | **blocked: capture-url-mismatch** |

Commands used (read-only against the lane; network probes in a scratch dir, no lane writes):
`curl -sS -L --max-time 40 -A '<UA>' -w '\n%{http_code} %{content_type}'` per live/capture URL;
`pdftotext` for PDFs; NFKC+casefold+`[\W_]+`->space normalisation before the substring test;
`curl 'http://web.archive.org/cdx/search/cdx?url=...&output=json'` for CDX.

## Blocking issues found while drafting (for the L1; none edited by me)

1. **teaches cells over the 240 cap** - `tools/check-row-fragments.py` (`TEACHES_MAX = 240`)
   flags nine rows: `S789:260`, `S790:258`, `S791:242`, `S792:260`, `S793:256`, `S794:264`,
   `S795:249`, `S796:271`, plus out-of-range `S801:249`. The Gate row itself is unaffected (the
   teaches cell is not part of the Gate line), but the registry ROWS leg and the fragment
   checker refuse them as-is; each cell needs trimming before integration.
2. **Round-65 entry hardcoded in the fragment checker** - `tools/check-row-fragments.py`
   line 40 `ENTRY = ".../games-play-sport-contests.md"`, used by `check_rows(rows_dir, entry=ENTRY)`,
   and `main()` exposes only `--rows/--quiet/--selftest`. Run on the round-66 rows it prints a
   `used-by` finding for **every** row (`FRAG: 12 finding(s) in 8 file(s)` at 11:44Z: 8 used-by +
   4 teaches-length). Those 8 used-by findings are tool staleness, not row defects - they must
   not be routed as defects, and the tool must not be edited mid-round without re-running its
   `--selftest`.
3. **S801-S804 sit outside the frozen claim range** - spec items `ScoutReject01` and
   `ScoutReject02` instruct "admit-or-reject for a row slot **S801**/**S802**", and
   `rows/ScoutReject01/row-S801.txt`, `rows/ScoutReject02/row-S802.txt` already exist as fully
   `mined` rows naming the scent entry (`row-S803.txt`, `row-S804.txt` appeared during the sweep).
   claims.json C promises "exactly 24 mined registry rows S777-S800", and `accept-c.py`'s SET leg
   only iterates `NEW_IDS = S777..S800`, so an admitted S801/S802 would land **undetected** and
   falsify the count. Either the reject seats must stay rejected or the claim must be revised
   before data - not silently.
4. **S753's R65-M3 locator defect survives in the registry** - S753's source cell still reads
   `web.archive.org/web/20250926172224id_/...` with no scheme, while S750 and S775 carry
   `https://web.archive.org/...`. `reopen-quote.py` extracts URLs with `https?://[^\s<>"|`]+`,
   so S753's capture is still never tried. Repair S753's cell in the same append as S776, and
   give S776 the scheme-bearing form.
5. **`s753-recapture.txt` lacks the verbatim quote** - `accept-ca.py` D1 requires
   `QUOTE = "Versions of mancala are traditionally played across Africa and Asia"` to appear in
   the receipt (`if QUOTE not in d1: d1_bad.append("quote")`). As of 1413 bytes / 11:35Z the
   receipt carries live status, CDX, the fresh capture and the disposition, but **0 occurrences**
   of that string -> D1 currently FAILS on `bad=['quote']`. The receipt also keeps a stale
   `old_capture status=000` and an empty first `--- CDX: latest captures ---` block above the
   successful `CDX retry (broad)`; and its disposition says "committed capture 20250926172224
   replays PDF not pdf", which contradicts its own later `old_replay_status=200` and is not
   decodable as written.
6. **archive.org is flapping on this host** - HTTPS to `web.archive.org:443` refused
   (`curl (7)`, status 000) at 11:34Z and again at 11:38Z, worked at 11:36Z and 11:45Z; HTTP:80
   refused where HTTPS worked moments later. A `000` here is transport, not capture death:
   every capture in this table re-probed to 200 on retry. Routing a `000` as a dead capture
   would manufacture a defect of the R65-M3 class.
7. **Captures are served with a transfer encoding** - S782's capture is gzip and S786's is
   **zstd** (`content-encoding: zstd`, 9860 B on the wire, 45391 B decoded); a plain `curl | grep`
   reports `quote-absent` for both. Decode before judging, or the row is falsely dead.
8. **`pdftotext -layout` breaks two-column PDFs** - the S753 quote extracts as interleaved
   columns under `-layout` (`played across Africa` / page gutter / `and Asia`) and the substring
   test fails; plain `pdftotext` reproduces the sentence contiguously. A reviewer's `-layout`
   check would falsely report `quote-absent` for S776/S753.

## Regeneration recipe (validated against the nineteen verified rows)

When the remaining fragments land, rebuild the whole block mechanically instead of retyping:

```python
import re, glob
def gate_line(path):
    t = open(path, encoding='utf-8').read()
    m = re.search(r'^ROW=\|\s*(S\d+)\s*\|(.*)$', t, re.M)
    sid, cells = m.group(1), [c.strip() for c in m.group(2).split('|')]
    src = cells[0]
    live = re.findall(r'https?://[^\s;]+', src)[0]
    cap  = re.findall(r'https?://web\.archive\.org\S+', src)[0].rstrip('.').rstrip(';')
    return f'- {sid} | {live} ({cap}) | {cells[7]} | {cells[4]}'
for f in sorted(glob.glob('.ufo/waves/round-66/rows/*/row-S*.txt')):
    print(gate_line(f))
```

`cells[4]` is the quoted anchor (kept with its own quotes, so no re-quoting happens),
`cells[7]` is `opened`. The recipe prints rows in fragment order; sort by id before pasting.
It assumes no `|` inside the source or anchor cells - true for all twenty rows read today
(S783 excepted: its anchor quotes are unbalanced, which is finding 2).

## Provenance

- Shape source: `corpus/lessons/round-65.md` lines 15-46 (`## Gate` and preamble).
- Checker: `tools/check-gate-quotes.py` (`MAX_WORDS=25`, `ROW`, `QUOTE`, `ellipsis_joins`,
  `gate_rows`, `registry_teaches`), read in full; not executed against the lesson yet because
  `corpus/lessons/round-66.md` does not exist at drafting time (dependency, not a defect).
- Claims: `reports/round-66/claims.json` (C SET/ROWS/ONEID/RESTATE/CAPTURE/LINK; Ca D1/QUOTES).
- Receipts read: `reports/round-66/telemetry/s753-recapture.txt`,
  `reports/round-66/telemetry/seat-evidence.txt`.
- Fragments read: the twenty `row-S*.txt` files listed above (`rows/` held 24 row files at
  12:12Z, including four out-of-range ones under `ScoutReject*`); `rows/ScoutReject02/row-S802.txt`
  read for finding 3 only.
- Scratch: PDFs and probe bodies written under `/tmp` only (`/tmp/s753-fresh.pdf`,
  `/tmp/s753-plain.txt`); nothing outside this file was written in the lane.
- Tool installs: none.
