# ReviewCarry135to147 — round-56 carry rows S135, S141, S147 → S570, S571, S572

Seat: `KotodamaR58A2.ReviewCarry135to147` (reviewer, leaf, no delegation). Every source re-opened this session (2026-10-23 UTC) by ordinary means only: plain `curl` GETs, `pdftotext`/`pdfinfo`/`qpdf` for the PDFs, `pypdf 5.4.0` via `uv run` where `reopen-quote.py` uses it. No challenge, captcha or paywall met. Downloads under `/fast/scratch/hyaku/kotodama-r58/ReviewCarry135to147/`. Recommendation only — I edited no file but this report.

Task: re-open each named source, check the routed finding against the served text, give agree/disagree and the exact fix; re-verify the round-55 drafted superseding rows (`.ufo/waves/round-55/build/ReviewCells135to159.md`) against the live source and the CURRENT entry `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` (line numbers re-measured). Output ids S570, S571, S572 plus the exact citation re-points.

## Verdicts

| row | routed finding (round-53 lesson :213; spot-check §5 item 6) | verdict | evidence this session |
|---|---|---|---|
| S135 | anchor cell: wrong page count and the locator does not reach the pages the entry cites | **agree** | re-fetched `http://www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf` → HTTP 200, 1,439,365 B (byte-identical to round 53/55). `pdfinfo`/`qpdf`: **10** pages; `file(1)` misreports 17. Cited passages sit on pp. 1–7, not "pp. 1–2": abstract p. 1; sign-language contrast, secrecy/herding and the 2 km line p. 2; Mexico/Mazatec p. 3; tone vs segmental rendering pp. 5–6; tone-load/intelligibility paragraph p. 7. |
| S141 | anchor cell: wrong page ("p. 4 paragraph [13]") | **agree** | re-fetched `hsj-v2n1_morrison.pdf` → HTTP 200, 233,242 B. 17 PDF pages align 1:1 with printed "Page N of 17" headers. Paragraph [13] is on printed p. 5 (page carries markers [12]–[14]) and does hold the cited sentences ("blending of the multiple pipe tones"; "the instrument is played now exclusively by men when it was invented by women"). [15] p. 6 (tones/vowels/consonants), [20] p. 8 ("note by note, word by word") both correct as filed. |
| S147 | teaches cell carries the over-read "lip-locked /p/, /b/ approach /k/" | **agree** | re-fetched `icphs2007.de/.../1286.pdf` → HTTP 200, 337,860 B, 4 pages (printed 837–840). "lip-locked"/"lip locked": **0** occurrences. Printed p. 839 §3 states the [k]-similarity for **[p] alone** ("The occlusive [p] is expressed mainly with this process and is therefore very similar to [k] in whistles."); [b] is classified with the intermediate [n], [b], [v], [f] (§3.1.1, p. 839) and shares only the glottal-occlusion compensation with [m], [p] (§3, p. 839). |

All three routed findings reproduce on the live bytes: **agree, agree, agree**. The draft's secondary observations also reproduce: the taught-exclusively-by-men and glottal-occlusion clauses, the "four groups" passage (§2.1, printed p. 838: "highlights four groups … statistically distinct"), "silent gaps" (§3, p. 839), and the Kusköy/shepherds sentence (§1, printed p. 837 — verbatim is "**still** practiced", not "it is practiced"; see note N1 below). S147's scope and remaining teaches clauses verified non-defective; Siberian Yupik stays intermediate (`Fo … frequency spectrum` balanced, §1 p. 837), supporting entry :80.

## Final registry rows (11 cells, append to `corpus/SOURCES.md`)

Conventions followed: `teaches` opens `supersedes S### — `; status `mined` (each superseded row is still cited in the entry today) with the same used-by; opened 2026-10-23, recheck 2027-10-23; anchor cells carry the locator plus verbatim ≥8-word quotes (the first quoted span is the LOCATE target under `reopen-quote.py --row`); source cells carry today's live-serve line. Every anchor quote below was LOCATED this session (receipts under "Locator receipts").

```
| S570 | Julien Meyer, David Díaz Reyes, Andre Batchelder-Schwab and Bernard Gautheron 2025, "Whistled Languages and Whistled Speech", *Encyclopedia of Language and Linguistics* (Elsevier), author-hosted copy — http://www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf (direct GET 2026-10-23: HTTP 200, 1,439,365 bytes, application/pdf; byte-identical to the round-52 copy) | book | B | as S135: the mechanism and social setting of whistled speech as a secondary speech code | Abstract: "Whistled languages are secondary speech codes based on whistles anchored to, and derived from, a spoken language thanks to a relation of acoustic iconicity."; p. 2: "this also makes them substantially different from sign languages, which are self-standing lexically, grammatically, and phonologically"; p. 2: "It is also often employed to speak in secret from foreigners or to remain hidden from animal prey"; abstract p. 1, sign-language contrast and secrecy/herding p. 2, Mexico mention p. 3, tone and segmental rendering pp. 5–6, tone-load and intelligibility paragraph p. 7, of a 10-page copy (`file(1)` misreports 17; `pdfinfo` and `qpdf` agree on 10) | supersedes S135 — anchor only: S135's "pp. 1–2 of 17" miscounts the copy (10 pages) and does not reach the cited passages, which sit on pp. 1–7; teaching as S135 | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
| S571 | Morrison, Gayle 1998, "The Hmong Qeej: Speaking to the Spirit World", Hmong Studies Journal v2n2 — https://www.hmongstudiesjournal.org/uploads/4/5/8/7/4587788/hsj-v2n1_morrison.pdf (open copy; direct GET 2026-10-23: HTTP 200, 233,242 bytes, application/pdf) | paper | B | as S141: the Hmong qeej as a ritual speech instrument, from interviews with players including a master player; one community's own account, not a comparative study | p. 5 paragraph [13]: "the instrument is played now exclusively by men when it was invented by women"; p. 6 paragraph [15]: "Each of these tones can be replicated on the Hmong qeej along with all of the Hmong vowel sounds"; p. 8 paragraph [20]: "Young players are taught each song note by note, word by word" (printed "Page N of 17" headers; PDF pages align) | supersedes S141 — anchor only: S141 places paragraph [13] on p. 4; it is on p. 5, holding the "blending of the multiple pipe tones" and "exclusively by men" sentences the row is cited for; teaching as S141 | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
| S572 | Meyer, Julien 2007, "Whistled Turkish: Statistical analysis of vowel distribution and consonant modulations", ICPhS XVI (Saarbrücken), paper 1286 — http://www.icphs2007.de/conference/Papers/1286/1286.pdf (direct GET 2026-10-23: HTTP 200, 337,860 bytes, application/pdf; printed pp. 837–840, PDF pages align) | paper | A | as S147: the Kuşköy whistled Turkish system as measured — the eight vowel bands and the four statistical groups, harmony rules, and the consonant modulations; the tone/non-tonal/intermediate assignment of languages including Mazatec, Chinantec, Akha, Hmong, Surui, Siberian Yupik, Chepang | §1 p. 837: "in most tone languages (like Mazatec, Chinantec, Akha, Hmong) whistling selects primarily Fo cues carrying tone registers and tone contours"; §1 p. 837: "still practiced in the village of Kusköy and by the shepherds going in summer in the high plateaus"; §3 p. 839: "The occlusive [p] is expressed mainly with this process and is therefore very similar to [k] in whistles"; §2 and §2.2.1 (vowel groups, harmony) | supersedes S147 — teaches cell only: S147's "lip-locked /p/, /b/ approach /k/" over-reads printed p. 839, which states the [k]-similarity for [p] alone and classifies [b] as an intermediate case; in most tone languages the whistle selects primarily F0 cues carrying tone registers and contours, in most non-tonal languages primarily segmental formant cues, and in an intermediate category both; eight Turkish vowels fall into four whistle-frequency groups resolved by vowel harmony; consonants appear as frequency and amplitude modulations with silent gaps, and the occlusive [p] whistles "very similar to [k]" while [b] counts among the intermediate [n], [b], [v], [f]; the practice lives in the village of Kuşköy and with the shepherds on the summer high plateaus | mined | 2026-10-23 | 2027-10-23 | corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md |
```

## Locator receipts — `reopen-quote.py '<url>' '<quote>'` (all run 2026-10-23 UTC from the lane root)

```
LOCATED http://www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf      ← "Whistled languages are secondary speech codes based on whistles anchored to, and derived from, a spoken language thanks to a relation of acoustic iconicity"
LOCATED http://www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf      ← "this also makes them substantially different from sign languages, which are self-standing lexically, grammatically, and phonologically"
LOCATED http://www.lemondesiffle.free.fr/media/WhistledLanguages_and_Whistled_Speech_Encyclopedy.pdf      ← "It is also often employed to speak in secret from foreigners or to remain hidden from animal prey"
LOCATED https://www.hmongstudiesjournal.org/uploads/4/5/8/7/4587788/hsj-v2n1_morrison.pdf                 ← "the instrument is played now exclusively by men when it was invented by women"
LOCATED https://www.hmongstudiesjournal.org/uploads/4/5/8/7/4587788/hsj-v2n1_morrison.pdf                 ← "Each of these tones can be replicated on the Hmong qeej along with all of the Hmong vowel sounds"
LOCATED https://www.hmongstudiesjournal.org/uploads/4/5/8/7/4587788/hsj-v2n1_morrison.pdf                 ← "Young players are taught each song note by note, word by word"
LOCATED http://www.icphs2007.de/conference/Papers/1286/1286.pdf                                          ← "in most tone languages (like Mazatec, Chinantec, Akha, Hmong) whistling selects primarily Fo cues carrying tone registers and tone contours"
LOCATED http://www.icphs2007.de/conference/Papers/1286/1286.pdf                                          ← "still practiced in the village of Kusköy and by the shepherds going in summer in the high plateaus"
LOCATED http://www.icphs2007.de/conference/Papers/1286/1286.pdf                                          ← "The occlusive [p] is expressed mainly with this process and is therefore very similar to [k] in whistles"
```

Two informative misses (both resolved, no finding changes):
- `'It is also often employed … while hunting or fishing'` → `NOT_LOCATED … quote-absent`: pypdf serves "orﬁshing" with the fi-ligature (normalised text reads `orfishing`, no space). Truncating the quote at "animal prey" locates.
- `'it is practiced in the village of Kusköy …'` → `NOT_LOCATED … quote-absent`: the paper reads "**still** practiced". The round-52 filed Gate line (`corpus/lessons/round-52.md:78`) quotes the shortened form — see note N1.

## Citation re-points in `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`

21 tokens total (S135 ×16, S141 ×2, S147 ×3) — matches the round-55 draft's counts (16/2/3); current line numbers re-measured. No other corpus file cites S135/S141/S147 (`grep -rn 'S135\|S141\|S147' corpus/knowledge` — only this entry; hits in `corpus/lessons/*` and `SOURCES.md` are records, not citations).

- :16 `(S135)` col 639 → `(S570)`; `(S135)` col 800 → `(S570)`
- :18 `(S135)` col 616 → `(S570)`
- :23 `(S135)` col 142 → `(S570)` (inside `(S136; S135)` → `(S136; S570)`)
- :24 `(S135)` col 99 → `(S570)`; `(S135)` col 195 → `(S570)`
- :26 `(S135:` col 103 → `(S570:` (paren-less form `S135: whistled speech is used "…"` → `S570:`)
- :53 `(S135)` cols 168, 318 → `(S570)`; `(S135; S137)` col 253 → `(S570; S137)`
- :54 `(S135)` cols 153, 436, 472 → `(S570)`
- :58 `(S141)` col 119 → `(S571)`; `(S141)` col 429 → `(S571)` (inside `(S140; S141)` → `(S140; S571)`)
- :76 `(S147)` col 250 → `(S572)` (inside `(S147; S146)` → `(S572; S146)`); `(S147)` col 347 → `(S572)`
- :78 `(S135)` col 338 → `(S570)`
- :79 `(S135)` cols 172, 306 → `(S570)`
- :80 `(S147)` col 155 → `(S572)` (inside `(S143; S147)` → `(S143; S572)`)

## Companion edits the rows require (stated for the L1; append-only rules observed)

Per the S145→S185 precedent (`SOURCES.md:174,214`: old row `mined`→`rejected`, used-by →`—`, retirement text appended to the old teaches cell — the filed convention the round-55 seat also followed; the "only status/recheck/used-by change in place" header notwithstanding, appending the retirement line is what S145's teaches cell actually carries today). Retirement text dated for this round:

- S135 teaches cell += ` Superseded 2026-10-23 (round 58): retired in favour of S570, which carries the corrected page count and the locators of the cited passages; the entry now cites S570.` — status `mined`→`rejected`, used-by → `—`.
- S141 teaches cell += ` Superseded 2026-10-23 (round 58): retired in favour of S571, which carries the corrected page for paragraph [13]; the entry now cites S571.` — status `mined`→`rejected`, used-by → `—`.
- S147 teaches cell += ` Superseded 2026-10-23 (round 58): retired in favour of S572, which drops the "lip-locked /b/ approaches /k/" over-read; the entry now cites S572.` — status `mined`→`rejected`, used-by → `—`.

## Residual notes and gaps

- **N1 (small, adjacent defect):** `corpus/lessons/round-52.md:78` Gate line for S147 quotes `"it is practiced in the village of Kusköy…"`; the paper's verbatim is "still practiced" (receipt above: the filed form is NOT_LOCATED). Filed bytes are never rewritten; if the lesson wants an erratum it is the same class as the CODH item. Not one of my three rows — recorded only.
- Draft spot check reproduced: `pdfinfo` 10 / `qpdf --show-npages` 10 on the byte-identical S135 copy; `file(1)` says 17 — the miscount the draft recorded. S141 `pdfinfo`/`qpdf` 17, printed headers align 1:1 with PDF pages.
- S135's remaining teaches clauses verified on pp. 1–2 (secondary codes, sign-language contrast, secrecy/herding) — non-defective, restated verbatim in S570's teaches ("teaching as S135").
- Not re-audited (outside my three rows): S151, S159 (assigned to `ReviewCarry151to159`, ids S573–S574); the kongo-kingdom sentence fixes; the heraldry :41 item (id S575); the CODH erratum (id S576).
- The round-55 draft's page map for S135 (abstract pp. 1–2, contrast/secrecy p. 2, Mexico p. 3, tone pp. 5–6, tone-load p. 7) re-verified as served; entry :78's "(S135)" for "hill and mountain country of the Hmong dispersal" is loose paraphrase of the paper's rural/mountain framing — a wording question for the entry, not the registry cells; carried unchanged (the same scope as the round-53 residual note on line 79).
- No LSP server applies (corpus markdown + PDFs; no code symbols); caller/identity checks were `grep` counts on `corpus/knowledge/` plus `SOURCES.md` row reads — grep output used only for literal citation counting, not semantic proof.
- Unrun by me: `tools/check-source-access.py`, `rowcheck.py` (claim C rows only — N/A for records rows S560–S599), `accept-c.py` — the L1's landing gates.

rejected: none — every opened source is offered in the three rows above.

installs: none into the environment. Tools used: curl 8.23.0; poppler pdftotext/pdfinfo; qpdf; file(1); python3; `pypdf==5.4.0` executed via `uv run --no-project --with` (ephemeral uv cache env; channel: official PyPI wheel) — required by `reports/round-58/reopen-quote.py`'s PDF path and to reproduce its pypdf extraction view. `uv` was already present at `/home/vgpnk/.local/bin/uv` (0.13.0); pacman untouched per the pause.
