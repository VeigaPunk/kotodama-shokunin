# Claim C honest-positive calibration — PDF and non-English fixture

Seat: `KotodamaR61.CtlCHonestPdf` (leaf, wave 1, round 61, hyaku phase 4, 2026-10-23).
Lane read at `78ad4b176695e9fcd490ab607cb8218e2ce62738`; nothing written in the lane or in `/home/vgpnk/Projects/shokunin`.
Fixture root: `/fast/scratch/hyaku/kotodama-r61/KotodamaR61.CtlCHonestPdf/`, sandbox clone at `.../clone` (`git clone` of the lane, `checkout -q 78ad4b176695e9fcd490ab607cb8218e2ce62738`, rev verified by `rev-parse HEAD`).

Counter identity, measured in the clone:

- frozen `reports/round-61/accept-c.py` sha256 `0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10` — matches the digest frozen in the assignment.
- probe `.../KotodamaR61.CtlCHonestPdf/accept-c-probe.py` sha256 `138ed7e1d95c8bd7b063b72bc4edf8cb124d1dc4a1d97527da8b01adb0e354ce`, one constant changed, diff:

```
--- clone/reports/round-61/accept-c.py	2026-10-23 06:41:37.786853628 -0300
+++ accept-c-probe.py	2026-10-23 06:47:38.219033471 -0300
@@ -54,7 +54,7 @@
 TOTAL = 236
 FIRST_SID = 652
 LAST_SID = 699
-FLOOR = 20
+FLOOR = 24
 LOCATOR = "reports/round-61/reopen-quote.py"
 SHARE = 1.0
 OPENED = "2026-10-23"
```

## What the fixture is

The claimed work done honestly, 24 rows instead of the claim's 20, in the sandbox clone only:

- `clone/corpus/knowledge/culture-material/footwear-codes-terminology.md` — 24 cited bullet lines, exactly one S-id per line, no S-id in a heading or prose line; head block carries `- topic:` (single line) plus sources/couples/verified-at/recheck.
- `clone/corpus/SOURCES.md` — 24 new rows `S652`–`S675`, 11 cells each, `status=mined`, `opened=2026-10-23`, `used-by=corpus/knowledge/culture-material/footwear-codes-terminology.md`; every anchor quote 8–25 normalised words.
- `clone/corpus/README.md` — one index row whose topic is byte-equal to the entry's `- topic:` text, `## culture-material/ (29)` → `(30)`, `Total knowledge entries: 235.` → `236.`, footer `(total 235 files; directory totals 29/29/29/29/24/95)` → `(total 236 files; directory totals 29/29/30/29/24/95)`.

Source mix, all fetched live today by ordinary GET (no browser, no challenge, no login):

- 10 open-access PDF rows, text through the locator's own path (`uv run --no-project --quiet --with pypdf==5.4.0`, as the locator does; used, not installed by me): PLoS ONE e10984 (First Direct Evidence of Chalcolithic Footwear), UHRA Houlbrook concealed-shoe proof (2 anchors), Fornvännen "A cairn in Roslagen with the oldest shoe in Sweden" (2 anchors), Northampton McCormack "Embodying the history of shoes" (2 anchors), Studia Vernacula Estonian leather-footwear article, rcin.org.pl Polish review of Volken.
- 14 encyclopedia rows: English Wikipedia (Shoe, Sandal, Clog, Moccasin, Geta (footwear), Zori, Opanak, Chopine, Lapti, Caliga, Mukluk) plus the three non-English pages de `Schuh`, fr `Sabot (chaussure)`, nl `Klomp` — the diacritics leg (ü/ä/ß-free but ä/ü/é/ç/à present, plus the German `Geta-Schuhen` and French `à l'origine`).

## Receipts (full stdout, verbatim)

### honest-v1 — frozen counter, first run (my own fixture defect)

```
$ cd /fast/scratch/hyaku/kotodama-r61/KotodamaR61.CtlCHonestPdf/clone && timeout 900 python3 -B reports/round-61/accept-c.py; echo exit=$?
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=24 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=24 bad=[]
TOPIC PASS rows=24 bad=[]
LINK FAIL min=3 bad=['27:1', '38:2']
COPY FAIL max=12 bad=['19:18']
LOCATE PASS located=24 cited=24 need=24 at=2026-10-23T09:47Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: FAIL
exit=1
```

### honest-v2 — frozen counter after fixing the three lines

```
$ cd /fast/scratch/hyaku/kotodama-r61/KotodamaR61.CtlCHonestPdf/clone && timeout 900 python3 -B reports/round-61/accept-c.py; echo exit=$?
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=24 floor=20
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=24 bad=[]
TOPIC PASS rows=24 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=24 cited=24 need=24 at=2026-10-23T09:47Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

### honest-v2 — FLOOR probe (FLOOR = 24, the fixture's row count)

```
$ cd /fast/scratch/hyaku/kotodama-r61/KotodamaR61.CtlCHonestPdf/clone && timeout 900 python3 -B /fast/scratch/hyaku/kotodama-r61/KotodamaR61.CtlCHonestPdf/accept-c-probe.py; echo exit=$?
SET PASS count=236 required=236 added=['corpus/knowledge/culture-material/footwear-codes-terminology.md'] removed=[]
SWEEP PASS exit=0 rows 236 files 236 missing_from_index 0 []
FLOOR PASS cited=24 floor=24
RANGE PASS bad=[] range_notation=[]
STATUS PASS bad=[]
OPENED PASS bad=[]
USEDBY PASS bad=[]
ACCESS PASS exit=0 ACCESS: 2 flagged rows, 0 findings
LINES PASS cited_lines=24 bad=[]
TOPIC PASS rows=24 bad=[]
LINK PASS min=3 bad=[]
COPY PASS max=12 bad=[]
LOCATE PASS located=24 cited=24 need=24 at=2026-10-23T09:48Z not_located=[]
FRESH PASS rows_reusing_registry_urls=[]
ACCEPT-C-61: PASS
exit=0
```

```
RECEIPT KotodamaR61.CtlCHonestPdf/honest-v1 counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=FAIL exit=1 probe=n/a stopped-by=LINK,COPY
RECEIPT KotodamaR61.CtlCHonestPdf/honest-v2-frozen counter-sha256=0a6e55caec13395a298af615e6ced5325fb72cd3a7473212fa60970f14ffcc10 rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=n/a stopped-by=none
RECEIPT KotodamaR61.CtlCHonestPdf/honest-v2-probe-floor24 counter-sha256=138ed7e1d95c8bd7b063b72bc4edf8cb124d1dc4a1d97527da8b01adb0e354ce rev=78ad4b176695e9fcd490ab607cb8218e2ce62738 frozen=PASS exit=0 probe=PASS stopped-by=none
```

Verdict for the C item from this seat: **NONE-MET** — no fixture here skips the claimed work and passes. The honest 24-row block passes the frozen predicate and the stricter FLOOR=24 probe; the two failures in `honest-v1` were true findings about my fixture (see below), not a counter defect, and the probe is not what cleared them (the frozen counter alone drops to PASS on `honest-v2`).

## What v1's FAIL means (true positives, not counter noise)

- `LINK 27:1`, `LINK 38:2`: I had written the line for an English Wikipedia "Shoemaking" row (`Most shoes today are made on a volume basis…`) and attached it to `S658`, whose anchor is McCormack's "Other items of clothing impact on the human body but shoes do so in a unique way", and the McCormack line to `S659`, whose anchor is "Footwear therefore has the potential to tell us a great deal about the human body." The leg caught a mis-citation by shared-word count, exactly the R60-M6 defect class. The row I meant to cite never existed in the fixture (I dropped the Shoemaking row), so the honest fix was to restate the rows that do exist, not to add shared words.
- `COPY 19:18`: my German line kept 18 consecutive words of the `de.wikipedia/Schuh` quote ("…waren es Holzsandalen mit einem Lederriemen über dem Spann…"). That is a pasted quote with a token changed, and 12 is the frozen cap. Fix: break the run after `Spann` (`gebräuchlich`), final longest run 6.

## False-FAIL modes measured (the question the assignment asks)

1. **PDF extraction / hyphenation — real, reproducible, and not repaired by the locator.** pypdf emits a line-end hyphen as `word- word` (hyphen + space), while the locator's join rule is `(\w)[-¬]\s*\n\s*(\w)` — hyphen + newline only. Measured on the Fornvännen PDF body: normalised text holds `roman empire` 4× and `ro man` 6×. Direct measurement of the rule (`locate_in`, quote "the design of the shoe shows influences from the Roman Empire"):

```
hyphen+NEWLINE locate_in= True
hyphen+SPACE locate_in= False
quote words: 11
```

   Consequence for the lane: an anchor quote transcribed from the printed page can NOT_LOCATE on a document where that phrase occurs only across a hyphen split, and a `LOCATE FAIL` there is a false FAIL of the honest row. My fixture avoided it by copying anchors from the extraction's clean passages; all 24 rows located on the first attempt (`located=24 cited=24 need=24`), the 10 PDF rows included.
2. **Diacritics / NFKC — no false FAIL.** `normalise` applies NFKC + casefold before comparison, so precomposed and decomposed spellings collapse: fr `Sabot (chaussure)` located both `à` (U+00E0) and `a`+U+0300 forms:
   `("Un sabot est à l'origine…", True)` and `("Un sabot est a\u0300 l'origine…", True)`. German `ä/ü/ß`, French `é/è/à/ç` and Dutch text all located; `TOPIC` still matched through the German compound because `Geta-Schuhen` normalises to `geta schuhen` and `geta` is a lexicon word.
3. **Non-English rows force source-language lines.** `LINK` compares the line's own words with the quote's, so an English paraphrase of a German or French anchor cannot reach three shared 4-letter words. My three non-English lines are written in their source language (German, French, Dutch) and passed `LINK`/`COPY` unchanged; an English-only renderer of the lane's entry must therefore either keep such lines in the source language or not cite non-English anchors for paraphrase.

## Risks and bounds

- This fixture is *not* the lane's claimed object: different rows, different URLs, scratch clone. It shows the frozen predicate is satisfiable by an honest 24-row block with live-located PDF and non-English anchors; it does not predict the lane's own block.
- Three PDF sources carry two anchors each (`S652/S653`, `S656/S657`, `S658/S659`), so 24 rows sit on 21 distinct URLs. `FRESH` bars only reuse of registry URLs below `S652` (`rows_reusing_registry_urls=[]`), and the claim's floor counts rows, not URLs; if the lane prefers one URL per row it must add three more sources.
- `ACCESS` reports `2 flagged rows, 0 findings` at base — pre-existing rejected rows, unrelated to this fixture; exit 0.
- No installs or upgrades were made in this seat; the only external tool use is the locator's own `uv run --with pypdf==5.4.0` PDF path (disclosed).
- Time: the fixture ran past the 25-minute return box (live PDF fetches plus one counter-iteration). No background process was left running; all writes are under `/fast/scratch/hyaku/kotodama-r61/KotodamaR61.CtlCHonestPdf/` and this one report file.
