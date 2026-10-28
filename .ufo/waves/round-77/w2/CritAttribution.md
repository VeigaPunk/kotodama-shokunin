# CritAttribution — wave-2 falsifier, round 77 (hyaku run 10)

Seat: CritAttribution (leaf, no subagents). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`,
base `211f9526800906e0c585d878d265c37e5e090c15`. Scope: attack the D2 claim wording against its
article — does the 88-term count belong to Kałużyńska 2025 or is it reported from her 2008
monograph? Check p4 text, attribution quote, 17-item list scope, universal/exhaustive claims.
Named W1 artifacts attacked: `CLAIMS-DRAFT.md` D2 line (staged S903 → lane S898),
`.ufo/waves/round-77/w1/ScoutDocS898.md`, `w1/stage/ScoutDocS898/evidence.txt`,
`w1/ScribeEntryA.md`, `w1/RevQualityFit.md`, `w1/drafts/corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md`.

## Verdict

**The central attack fails: the D2 claim wording is right.** The 88-term count belongs to
Kałużyńska (2008, pp. 223, 232) — her own monograph *Chinese female namings. Past and Present*
(Warsaw: Wydawnictwo Agade) — and is *reported*, not made, by the 2025 *Onomastica* LXIX paper.
The draft's sentence "The count is reported from the cited 2008 work, not re-counted by the 2025
article; scoped to female naming, not a universal or exhaustive taxonomy" is verified verbatim
against the article. Three fixable defects found around it (stale evidence metadata, an
attribution-free Gate quote, a 17↔88 over-read in the drafted entry). None reaches the kill rule.

## Independent verification (this seat re-fetched the article)

```
$ curl -sS -L --compressed -o d2.pdf -D d2.headers -w '%{http_code}\n%{size_download}\n%{time_total}\n' \
    https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/
200
417093
2.780866
$ sha256sum d2.pdf
5d1bfa5a5f01bee68e090155ed683d848e6f75dbc456b8b631be81c1fa8d29bc   (matches W1 evidence.txt)
$ pdfinfo d2.pdf | head -8
Title: Onomastica 69_07   Subject: Flowers, plants, and trees in female naming in China
Author: Irena Kałużyńska  (Adobe InDesign 19.5; 13 pages, journal pp. 112–124)
```

## The four named checks

**1. p4 text (journal p. 114 = PDF p. 4, §3 ¶1).** `pdftotext -layout -f 4 -l 4 d2.pdf -` prints,
as the second sentence of §3's first paragraph:

```
There are many terms denoting various species of plants and trees in China.
According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms
denoting plants, flowers and trees (general terms, species or the parts of flow-
ers or trees) among the names of women figuring in the research material of the
work, and the frequency of their occurring varied.
```

The count is self-cited to the author's 2008 work at her pp. 223 and 232, and the sentence bounds
it twice in-apposition: "(general terms, species or the parts of flow-/ers or trees)" and "among
the names of women figuring in the research material of the work". The references list (pdftotext
line 547) resolves the cite: `Kałużyńska, I. (2008). Chinese female namings. Past and Present.
Warsaw: Wydawnictwo Agade.` — a monograph. `grep -c '88' d2.txt` → the number appears exactly
once in the whole paper; the 2025 article never re-counts it.

**2. Attribution quote.** The 17-word span
`According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 terms denoting plants, flowers and trees`
locates verbatim under whitespace-fold (count 1 in the p4 extract). Raw-layout note: the span is
folded across a hard line break at `terms / denoting` — so the draft's parenthetical "(folded
across a PDF line break, not claimed verbatim)" is accurate about the raw layer while `matched=
verbatim` in evidence.txt is accurate under the declared `whitespace-fold` normalise rule. No
contradiction, but see D-A below.

**3. 17-item list scope.** §4 heading (journal p. 116 / PDF p. 6):
`4. LIST OF THE 17 MOST COMMON LEXEMES/CHARACTERS DENOTING PLANTS, FLOWERS AND TREES OCCURRING IN FEMALE NAMES`.
Lead-in (journal p. 115 / PDF p. 5): the 17 are "listed in 'Xingshi' as those of the highest
occurrences among the top 150 terms/lexical items/characters used in female names" — i.e. a subset
of the 1991 *Xingshi* volume's top-150 (itself computed on the 1982 PRC census sample: "2,500
characters occurred in the names of 85,567 females"), NOT a subset of the 88. The abstract frames
the same scope: "17 Chinese terms … of the highest frequency of occurrences among the top 150 …
at the beginning of the 1980s", compared against the ZQS website's own top-150 (≈2020–2024).
So "17-item list scope" = frequency cut of a census-derived top-150, female names, plant class.

**4. Universal/exhaustive claims.** None in the article, none in the drafted entry. "Altogether"
is corpus-bounded by the same sentence's "among the names of women figuring in the research
material of the work". The draft entry marks the 88 figure tier B ("reported from the author's
2008 monograph, not re-counted on this page … the number is scoped to that monograph's corpus")
and §4 bullet 2 quotes the corpus bound. The claim title's "finite lexeme classification" is the
article's own framing (counted membership + frequency ranking), not an assertion of exhaustivity.

## Defects found (fixable; none kill-rule)

### D-A — evidence.txt quote metadata is stale (provenance/fidelity)

`.ufo/waves/round-77/w1/stage/ScoutDocS898/evidence.txt:13-14` carries `quote-words: 10`,
`quote-chars: 65` — that describes the OLD 10-word fragment
`there were altogether 88 terms denoting plants, flowers and trees` (measured this seat: 10
words / 65 chars exactly). The file's own `quote:` field and stored window now carry the 17-word /
111-char attributed sentence (measured: 17 words / 111 chars; the draft's 5-word Gate quote is 30
chars). mtimes corroborate a partial re-derivation after the ScribeLesson relay:
evidence.txt 22:52:29, ScoutDocS898.md 22:52:40 — the locator was fixed (it now correctly says
p. 114/PDF p. 4, resolving ScribeEntryA's F9 complaint about the earlier "p. 115/PDF p. 5") but
the word/char metadata was left behind.

Smallest correction: set `quote-words: 17`, `quote-chars: 111` in the committed evidence file
(and any Gate copy of it) before lands.

### D-B — the draft's "Gate quote" strips the attribution it depends on (located-quote adequacy)

`CLAIMS-DRAFT.md:15` nominates `there were altogether 88 terms` (5 words, verbatim on p. 4) as the
Gate quote while naming the 17-word attributed sentence only as "the evidence anchor". If the L1
files the 5-word fragment, the row's quote in isolation reads as the 2025 paper's own count —
precisely the misattribution this round's rewrite exists to prevent (RevQualityFit F1: "the 88
line must carry the in-paper attribution"). The 17-word sentence is inside the 25-word bound.

Smallest correction: file the 17-word attributed sentence as the Gate row's quote (drop the
fragment), or pair the fragment in the row with a locator note naming (2008, pp. 223, 232).

### D-C — the drafted entry over-reads the 17↔88 relation (scope calibration)

`w1/drafts/.../naming-systems.amend-2026-10-23.md` §4: "a frequency cut of that inventory" and
"Seventeen of eighty-eight is the ranking rule". The article NEVER states the 17 are drawn from
the 88: `grep -nE 'of the 88|among the 88|17 of' d2.txt` → 0 hits. The 17 are defined by Xingshi's
top-150; the 88 by the 2008 monograph's research material — different instruments, different
populations. §3 ¶2's "selection of the most common terms" makes the inference plausible, and the
calibration table phrases the scope correctly, so this is not verbatim-false — but the unquoted
gloss asserts a cardinality relation the page does not.

Smallest correction: reword to the article's own scope, e.g. "the highest-occurrence plant-class
terms among Xingshi's top 150 female-name characters — a frequency cut of the census statistics,
not of the 88".

### D-D — report-only anomaly (no action beyond D-A)

ScribeEntryA F9 (22:50) says ScoutDocS898 located the 88 quote at "journal p. 115 (PDF p. 5)" —
measured false by both seats (span counts 1 on PDF p. 4 / header 114, 0 on p. 5). The current
artifact says p. 114/PDF p. 4 — correct — so the locator was repaired post-relay; D-A is the
unrepaired residue of the same edit.

## Strongest counterexample tried

The best available attack was the attribution-inversion reading — i.e. that "the onomastics
literature's finite lexeme classification" plus an "88 terms" Gate quote would smuggle the count
in as the 2025 paper's own finding. It fails on the page: the count's only occurrence is inside an
"According to Kałużyńska (2008, pp. 223, 232)" sentence, and the draft explicitly records
"reported from the cited 2008 work, not re-counted". The residual risk is presentational (D-B),
not factual.

## Scope compliance

Nothing mutated outside this file and `/fast/scratch/hyaku/kotodama-r77/CritAttribution/`
(d2.pdf + headers + extracts; deleted before yielding). No installs; tools used were already
present (curl 8.x, pdftotext, pdfinfo, grep, sha256sum).
