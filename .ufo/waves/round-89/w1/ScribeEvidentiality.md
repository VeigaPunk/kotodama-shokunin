# ScribeEvidentiality — round 89 claim C stage report (r89-v1)

Seat: scribe, leaf. Axis: coverage. No production file was edited. Nothing was committed or pushed in the lane. No tools were installed or upgraded.

## Behavior delivered (stage only; L1 integrates)

Stage dir: `.ufo/waves/round-89/w1/stage/ScribeEvidentiality/`

| file | purpose | integrate to |
|---|---|---|
| `entry.md` | new entry, 19,901 bytes, 10 `## ` headings, header keys topic/sources/verified-at/recheck/couples (+ gap filled), one design table of 5 cols × 6 data rows, cites only S936–S940 | `corpus/knowledge/linguistics/evidentiality-epistemic-marking.md` |
| `rows.md` | 6 registry rows S936–S941, 11 cells each | append after the S935 row in `corpus/SOURCES.md` |
| `gate.md` | 6 Gate lines (URL, 2026-11-04, locator, curly-quoted quote, grounds) | `## Gate` of `corpus/lessons/round-89.md` |
| `evidence/S936.txt … S941.txt` | text captures (html.parser text outside script/style; PDFs via pdftotext) | `reports/round-89/evidence/` |
| `evidence-manifest.json` | url / http_status 200 / fetched_at -03:00 / capture path / sha256 for all 6 | `reports/round-89/evidence/manifest.json` (C manifest; F uses `rechecks/manifest.json`) |
| `readme-row.md` | README index row with the topic text copied exactly from the entry | `corpus/README.md` `## linguistics/`, between `dialect-register-consistency.md` and `gesture-co-speech-pointing.md`; the header goes 33→34, and totals 260→261 / dir totals 34/36/43/29/24/95 need a new block |
| `fixture-receipt.txt`, `fixture-diffstat.txt` | frozen counter + index/recheck/access tool output on a scratch fixture | receipts only |

## Ids used

| id | source (exact fetched URL) | tier/status | quote checked with measure89.contains |
|---|---|---|---|
| S936 | de Haan, WALS ch. 77 — https://wals.info/chapter/77 | A mined | True |
| S937 | de Haan, WALS ch. 78 — https://wals.info/chapter/78 | A mined | True |
| S938 | de Haan 1999 SWJL 18 abstract page — https://lassoling.org/wp-content/uploads/2020/12/18.1-1999.pdf | A mined (scope: abstract thesis only) | True |
| S939 | Tournadre & LaPolla 2014 LTBA 37(2) preprint — http://www.nicolas-tournadre.net/wp-content/uploads/multimedia/2014-evidentiality.pdf | A mined | True |
| S940 | Greed 2022, SIL Glossary "Evidentiality" — https://glossary.sil.org/term/evidentiality | B mined | True |
| S941 | Glottopedia "Evidentiality" stub — http://www.glottopedia.org/index.php/Evidentiality | C rejected | True |

All fetches returned HTTP 200 on 2026-11-04 between 19:07:48 and 19:08:08 -03:00 (file mtimes). Every quote has 13–23 words, and each one passes `quote_ok`.

## Sources rejected / not registered

- **S941 Glottopedia — REJECTED (C).** The page is an unreferenced stub that carries its own reference-needed block. It defines evidentiality as "a way of marking epistemic modality", which contradicts S936, S938 and S940, and its Turkmen paradigm has no source. Flip: a referenced revision that cites a Turkmen grammar and treats the boundary as contested. The entry does not cite it, because a cited tier-C new id would fail NEWIDS.
- **Wikipedia "Evidentiality"** (https://en.wikipedia.org/wiki/Evidentiality): fetched (200), but it is tertiary and was not used. It got no id and no capture.
- **Zeisler questionnaire** (https://tulquest.huma-num.fr/sites/default/files/questionnaires/41/QuestionnaireEvidentiality.pdf): HTTP 404. No id. The Wayback capture was not tried, because no row depends on it.

## Gates (observed commands, rc)

- `curl -sL` ×8 (WALS 77, WALS 78, Glottopedia, SIL, Wikipedia, de Haan PDF, Tournadre PDF, Zeisler PDF): rc 0. HTTP 200 for seven of them; Zeisler returned 404.
- `pdftotext` on the de Haan and Tournadre PDFs: rc 0. A first `pdftotext` on the 404 HTML failed (the chained bash command returned rc 1, which is expected).
- Quote check: `python3 q.py` using `measure89.contains` / `quote_ok` gave all 6 True. The gate/manifest builder re-checked url_ok, quote_ok, contains and the date: all True for all 6.
- Fixture: I created a `git clone --shared` into scratch, asserted toplevel, checked out freeze `1cbd0efc`, applied the stage package plus a simulated README row, header and totals block, and committed fixture `73cadcb8`.
  - `python3 -B reports/round-89/measure89.py --root . --freeze 1cbd0efc… --lands 73cadcb8… --claim C --work <scratch>` gave rc 0 and **ACCEPT-C-89: PASS legs=8/8**: FROZENCFG, ENTRY (19901 B, 10 headings), TABLE [[5,6]], NEWIDS (S936–S940 qualifying, 0 unqualified), GATE, CAPTURE, INDEX (row true, tool_rc 0) and APPENDONLY all passed.
  - `tools/check-corpus-index.py --root .`: rc 0, `CORPUS-INDEX: OK files=261 rows=261 findings=0`.
  - `tools/check-sources-recheck.py --as-of 2026-11-04 --window 90`: rc 0, `0 due / 20 upcoming / 16 on-release / 865 rows`. The 20 upcoming are unchanged, so the new rows do not enter F's population.
  - `tools/check-source-access.py --root .`: rc 0, `3 flagged rows, 0 findings`, identical to base.

## Out of scope

Claim F rechecks; the README narrative block and footer wording (the totals block in the fixture was my simulation, not a proposal); the lesson's other sections; any commit. Lore or canon: the Tessaly micro-design is labelled NON-CANON.

## Unresolved defects / honest limits

1. The fixture was built on freeze `1cbd0efc`, not on the live lane HEAD `9ad00be`, and the live `corpus/SOURCES.md` is currently modified by F seats. L1 must re-run the counter at the real lands revision. The row append point is after S935.
2. S938 is a journal **abstracts page** (2 pages), not the article. The row, the gate line and the entry all say the body was not read. Tier A covers only the author's stated thesis.
3. The WALS chapter pages print no publication year. The rows say "no year printed on the opened page" instead of guessing.
4. The entry is 19.9 KB, above the 12–18 KB aim; the frozen requirement is only ≥ 8000.
5. The counter checks structure and source binding, not typological truth (claims.json bounds). Per the bounds, a quote pasted into a fabricated capture would pass. Defence: re-fetch the 6 URLs; the sha256 values are in the manifest.
6. Clause-scope citation: most cited claims carry one S-id on its own line. Two lines carry two ids (the §5 origins bullet, and the §8/§9 bullets citing S936+S937 or S938+S939).

## Artifact paths

- `.ufo/waves/round-89/w1/stage/ScribeEvidentiality/{entry.md,rows.md,gate.md,evidence-manifest.json,readme-row.md,fixture-receipt.txt,fixture-diffstat.txt,evidence/S936.txt…S941.txt}`
- this report: `.ufo/waves/round-89/w1/ScribeEvidentiality.md`
- scratch `/fast/scratch/hyaku/kotodama-r89/ScribeEvidentiality/` removed before yield.
