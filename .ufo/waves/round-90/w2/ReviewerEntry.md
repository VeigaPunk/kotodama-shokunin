# ReviewerEntry — independent non-author re-open of claim C, round 90

Graded revision: `7f3a7aa6615624afadc2cc2d2d4f7ad225f44761` (landed bytes). Base `6b0b86e4`, freeze `d0b6f2a7`. Scratch: `/fast/scratch/hyaku/kotodama-r90/ReviewerEntry/` (TMPDIR set, removed on exit). Verdict machine copy: `Report: .ufo/waves/round-90/w2/stage/ReviewerEntry/verdict.json`.

Tooling installed this round: none (pacman paused; no need filed — curl/python3 sufficed).

## 1. Fresh re-opens (7 of 7 sources, `curl -sS -L`, ordinary HTTP, no browser)

`curl -sS -L -w "%{http_code} %{size_download}" <url> -o S94x.fresh.html` then `sha256sum`:

| id | status | bytes | my sha256 | vs manifest |
|---|---|---|---|---|
| S942 wals.info/chapter/72 | 200 | 41840 | `e28b23dc…c004c6` | identical |
| S943 wals.info/chapter/73 | 200 | 50562 | `b3f0f850…8bbc3` | identical |
| S944 wals.info/chapter/71 | 200 | 46113 | `e939d949…b02dce` | identical |
| S945 glossary.sil.org/term/vocative-case | 200 | 11053 | `f3ac4093…f00ea00` | identical |
| S946 atticinscriptions.com/inscription/IGI3/646 | 200 | 13536 | `26bb20bd…220b1c` | identical |
| S947 pmc.ncbi.nlm.nih.gov/articles/PMC13671548/ | 200 | 295969 | `78b605b1…acbc9e` | differs, same length |
| S948 drops.dagstuhl.de/…/OASIcs.CMN.2016.12 | 200 | 105415 | `0459d872…a4109b9` | differs, same length |

S947/S948 drift is page chrome only — `diff` of capture vs fresh shows exactly two changed lines each: `ncbi_phid` + `csrfmiddlewaretoken` (S947), `csrf-token` + `_token` (S948). Body content identical; every quote and claim below still matched the raw committed captures.

## 2. Gate quotes vs my fetches, grader `norm()` (NFKC, ’→', whitespace collapse, casefold, space-before-punct strip)

Checker: `python3 -B check_quotes.py` (scratch copy of `norm()` verbatim from `tools/check-advance-evidence.py:69-74`). Result, raw bytes, no tag-stripping needed:

```
S942 RAW/RAW  S943 RAW/RAW  S944 RAW/RAW  S945 RAW/RAW
S946 RAW/RAW  S947 RAW/RAW  S948 RAW/RAW   (fresh / capture)
```

All seven lesson quotes are verbatim in **my own fetches**, not only in the captures. Section attributions also verified: the S942 quote sits under `h3 1.1. Imperative and hortative`; S943's directly after the (2)/(3) examples of section 1; S944's immediately before "Four values will be distinguished. Values of Map 71A". One gate line per row confirmed by inspection.

## 3. The four factual statements

1. **Map 72A = 133/20/21/201 of 375** — from my fetch's `value-table-72A`: `maximal…not a minimal one | 133`, `minimal…not a maximal one | 20`, `both | 21`, `neither | 201`, `Total: | 375`. The entry's table column maps these correctly. **But its design-consequence prose is false — defect D1.**
2. **Map 73A = 48/271 of 319** — `Inflectional optative present | 48`, `absent | 271`, `Total: | 319`. Entry prose matches, including the verbatim areal sentence (Australia/Africa none, Albania+Karaim, New Guinea). PASS.
3. **Map 71A = 113/182/55/146 of 496** — all four values and `Total: | 496` confirmed row-for-row; the S944 gate quote is value 1 (113). PASS with prose imprecision (D5).
4. **SIL 404 sweep** — `for t in vocative prayer invocation supplication petition vow votive blessing curse vocative-case; curl -o /dev/null -w "%{http_code}"`: `404 ×9, vocative-case 200`. Entry's claim fully reproduced. PASS.

Other content verified against my fetches: S946 metadata (Translation by: Edmund Stewart; Columnar base; ca. 510-500 BC; Acropolis; "tanning may have become a specialist occupation … from before the start of the fifth century"; Tracy objection) — all present; S947 abstract carries all four findings the entry bullets plus the 11,000/GIST/I.PHI/epigraphic-habit framing; S948 abstract names both litanies "in their most ancient attested forms", n-selection, and the Faustina Kowalska test; ch72's appeal-to-addressee boundary is verbatim in the chapter.

## 4. Structure at the landed bytes

- Entry: `git show 7f3a7aa:corpus/knowledge/linguistics/petitionary-and-votive-formulae.md | wc -c` → **19930** (≥12000); `grep -c '^#'` → **9** (≥6); header keys topic/sources/verified-at/recheck present; table 5 data rows × 4 cols.
- Index: lands tool over lands tree (`git archive 7f3a7aa | tar -x`, then `index.landed.py --root <tree>`): `CORPUS-INDEX: OK files=262 rows=262 findings=0`, rc=0.
- APPENDONLY: `git diff 6b0b86e4..7f3a7aa -- corpus/SOURCES.md` → **0 deleted** lines, 8 added. Linguistics partition 35 files at lands. README move present (lines 360, 940-950).
- Registry: S942-S948 all `mined`, opened 2026-11-04, used-by the entry; S949 `rejected`, used-by the lesson; tiers six A + one B (S945 B). Lesson's "six `mined`" is a miscount — seven are mined (D4).

## 5. Defects (severity order)

- **D1 major — entry:43 (landed; still false at HEAD).** "the 'maximal' system is the marked one; most sample languages grammaticalise a minimal imperative only." Contradicted by the counts in the same cell and by my fetch: minimal-only = **20 of 375** (5.3%), maximal-only 133, neither 201 (largest class); among system languages maximal-only beats minimal-only 6.65:1. "Marked" appears nowhere in chapter 72. The registry S942 row states the mapping correctly; commit `3f56892f` fixed the adjacent definitions sentence (line 49) but left this cell false. This is the entry contradicting its own capture — the failure class the entry itself preaches against in its §7.
- **D2 moderate — entry:55.** "WALS chapters 72 and 73 explicitly set non-inflectional expressions of the wish aside." True verbatim for 73; false for 72, whose only explicit exclusion is prohibitives and which expressly admits non-uniquely-imperative-hortative constructions.
- **D3 minor — entry:61.** "…in eleven words": the quoted translation is eight words; eleven counts parentheticals the entry's own quotation omits.
- **D4 minor — lesson, registry-changes paragraph.** "six `mined`" vs seven mined rows.
- **D5 minor — entry:53.** Prohibitive tricolon (113, 182, 146) silently drops 55; "146 use a different verb entirely" is true but incomplete (value 4 also changes negation). Table and registry row are correct.
- **D6 overreach-uncited — entry:25,33,77; registry S945 teaches cell.** Argument-structure/apposition claims beyond the one-sentence glossary; the Greek/Latin "indeclinable barbarian theonyms" assertion; "attested solutions include re-dedication, erasure, legal fiction, transfer to heirs" with no source; "often a clitic". Stated as fact, unsupported by any of the seven sources; tolerable in a self-declared NON-CANON design register, but they should not read as source-backed.

## 6. Verdict

Claim C's gate, counts, captures, index, appendonly and registry legs all reproduce from my own fetches; **7/7 gate quotes verbatim, 4/4 factual statements verified, structure and index PASS**. The claim as frozen survives. One major content defect (D1) sits inside the graded entry and survives at HEAD; it does not break any frozen C leg (the counter counts structure and gate binding, not the truth of the consequence prose) but it is exactly the class the round's own QUALITY14/QUALITY36 discipline exists to catch, and I recommend it be fixed in a post-landing amendment rather than left standing.

Residual risk: the worktree moved during this review (HEAD → `3f56892f`, entry dirty at review time); S947/S948 sha pins certify a fetch instant, not the page (per-request CSRF tokens); freshness pause was respected — nothing re-verified, re-dated or repaired.
