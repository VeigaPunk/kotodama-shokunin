# ScoutSurface100 — claim C coverage surface (report)

Read-only scout for Kotodama round 100, wave w1. Stage output:
`.ufo/waves/round-100/w1/stage/ScoutSurface100/surface.md` (29,183 B) — the full sweep, hit
classification, adjacency table, skeleton and partition walk live there. This file is the summary.

## Answer

The work-song / labour-chant surface is **unowned at base**, and the new entry belongs in
`linguistics/`. C8 passes today with margin: 0 heading owners and 0 topic-line owners for all six
frozen phrases, and the token *shanty* does not occur anywhere in `corpus/knowledge` in any
spelling.

## Sweeps (exact commands, rc)

1. Assigned broad sweep over `corpus/knowledge` — **rc 0, 14 lines**. Two are false positives from
   substring alternation: `numerals-and-measures.md:91` ("**Chantyal**", matched by `chant(e)?y`)
   and `politeness-taboo-euphemism.md:88` ("**slumber** rooms", matched by `lumber`).
2. Word-boundary refinement — **rc 0, 12 lines in 7 files**: lullaby 4, funerary 3,
   verbal-duelling 1, material-culture-inference-method 1, mississippian 1, maori 1, balts 1.
3. Heading-owner sweep, six phrases — **rc 0, 0 hits each**.
4. Topic-line-owner sweep, six phrases — **rc 0, 0 hits each**.
5. `grep -rIl -i -F "work song" corpus/knowledge` — **rc 0, exactly 4 files** (balts,
   material-culture-inference-method, funerary-lament, lullaby), reproducing claim C's own
   `before` clause.
6. `grep -rIn -i -w -E 'shanty|shanties' corpus/knowledge` — **rc 1**, no match.
7. Partition census `find … -name '*.md' | awk -F/ '{print $(NF-1)}' | sort | uniq -c | sort -rn` —
   **rc 0**: civilizations 95, linguistics 44, culture-material 43, myth-symbol 36, synthesis 29,
   verification 24; total 271, equal to `corpus/README.md`'s live footer (44/36/43/29/24/95).
8. Registry: `grep -c '^| S' corpus/SOURCES.md` → **941 rows**, highest **S1017**; no row owns the
   surface (adjacent `labour` hits are S032/S034 division-of-labour, S618 birthing girdle, S856
   labouring-folk — all unrelated).

## Hit classification

12 real hits: **0 owners, 0 substantive-but-single-owner, 5 substantive sections** (funerary §8
genre test `:129`, funerary antiphonal row `:206`, funerary checklist `:245`, lullaby repertoire
graph `:193`, lullaby carrier/worked-example `:245,253,285`, verbal-duelling frame `:52`) and
**4 passing mentions** (balts `:165` directive, maori `:52` encounter karanga, mississippian
`:145` hauling arithmetic, material-culture-inference-method `:15` stale routing). The lullaby
entry is the strongest invitation: it already treats a work song as a repertoire-graph node it
does not own (`:193`, `:285`).

## Adjacency (13 boundaries the entry owes)

Sharpest collisions, in order: **`maritime-seafaring-lexicon.md:22-32`** (its §2 row already says
"the songs that pace shared labour" — maritime owns commands and the wage cycle, the new entry
owns the songs); **`sacred-registers-liturgical-language.md:101-107`** (chant as enforced
recitation norm vs labour chant); **`timekeeping-instruments.md:64`** ("market and work bells …
the rhythm of labor" — clock time vs task time); **`verbal-duelling-ritual-insult.md:91-109`**
(song duel = adjudicated contest; work-song satire has no verdict); **`praise-poetry-panegyric.md:172-198`**
(the R99-M2 oríkì/drummer cell lives here and must not be restated); **`lullaby…:172-199`** (tune
carrier — the new entry owns the work-song side of the shared tune); **`funerary…:84-109`**
(antiphony as mourning vs antiphony as pull); **`orality…:30-37,99-129`** (formula engine borrowed,
not re-derived); plus music-instrument (no melody), dance (no movement), agrarian (peak-labour
month as input only), craft (workshop register stays), toast/speech-surrogates/cuisine/trade/games
(passing). Full table with anchors in `surface.md` §3.

## Skeleton

11 h2, all six frozen phrases as headings (C1 needs 4): §1 scope + 13×3 boundary table, §2
`work rhythm` + task/body/song/failure table (5+ rows), §3 `song leader`, §4 `call and response`,
§5 `hauling song` + per-repertoire table, §6 `shanty`, §7 improvised verses/complaint/satire,
§8 decision table (10–12 × 5), §9 NON-CANON worked example, §10 error patterns, §11 limits and
handoff. `norm()` maps `-` to space, so `work-song` matches `work song`; `shanties` does **not**
match `shanty` — use the singular.

## Planning data-walk (contract mechanics, read off the frozen counter)

- **C5 requires editing `corpus/README.md`, and the row topic must be byte-equal to the entry's
  `- topic:`.** `check-corpus-index.py:77` reads `corpus/README.md`; `ROW_RE`/`TOPIC_MISMATCH`
  (`:30`, `:120-135`) compare the row text to the entry topic after whitespace collapse. Proved on
  the live lullaby pair: equal, 277 chars each (python compare rc 0). So the README row must repeat
  the full 440-char frozen topic, not a summary.
- Three count sites move together: `## linguistics/ (44)` → `(45)`; an **appended** footer block
  `Total knowledge entries: 272.` / `Counts checked 2026-11-06 from the repo root:` / the command /
  `(total 272 files; directory totals 45/36/43/29/24/95).` — `TOTALS_RE` and `FOOTER_RE` both take
  the last match, so appending is correct and older blocks stay untouched.
- **C8 does not see `corpus/README.md`** (`tree_knowledge()` walks only `corpus/knowledge`), so the
  README row carrying all six phrases creates no owner.
- C1 measures **bytes** (`len(raw.encode('utf-8'))`), counts `## ` only (not `###`), and needs one
  table ≥5 data rows × ≥3 cols. C2 rows are exactly 11 cells with `used-by` exactly the entry path.
  C7 manifest is a JSON list of `{id, captures:[{file,sha256}], quote, quote_capture}` with
  basenames only inside `reports/round-100/evidence/`, quote 1–25 words occurring exactly once and
  contained in the registry row's `anchor` cell.

## Files written

- `stage/ScoutSurface100/surface.md` (29,183 B)
- `stage/ScoutSurface100/DONE`
- this report

## Tooling

None installed or upgraded. Scratch `/fast/scratch/hyaku/kotodama-r100/ScoutSurface100/` removed
before yield. No git/jj mutation; no sibling or fleet file edited (the stale work-song routing at
`material-culture-inference-method.md:15` is left in place deliberately and flagged in the entry's
limits).
