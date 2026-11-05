# Counterfeit entry-mode landings — CriticClaims91 (round 91)

Frozen grader: `tools/check-advance-evidence.py` sha256 `88597a66c7912861d0a593f984b9eb224a3c46cba3b35d06209b529bc6031093` (verified before every run), run in `entry` mode with the exact argument vector of `grade_c` in the frozen `reports/round-91/measure91.py` (`--topic`, `--topic-phrases "argot;anti-language;backslang;ludling;cant;in-group concealment"`, `--min-topic-phrases 4`, `--min-bytes 12000`, `--min-headings 6`, `--min-new-ids 3`, `--min-topic-overlap 10`, `--table-min-rows 5`, `--table-min-cols 3`, `--as-of 2026-11-05`, `--graded corpus/SOURCES.md --graded corpus/lessons/round-91.md`, relative `--capture-dir reports/round-91/evidence`). All trees built under `/fast/scratch/hyaku/kotodama-r91/CriticClaims91/trees/` (since deleted); driver `run_attacks.py` sha256 `a10509d13010b4910b89d30b5f62df087d6c2479dda365b708a32fe2e08357b4`. Capture bytes and manifest for the honest rows are the L1's committed-to-working-tree evidence for S952–S955. Base registry (875 rows) and base lesson are `git show d39434b3:...` extractions; read-only.

Control G0 is a compliant-shaped landing (12225 B entry, 8 h2, 5x3 table, 4 qualifying new rows S952–S955, gates with capture-located quotes): **rc 0, LEG PASS 8/8** — the harness can pass, so every FAIL below is the mutation's, and every rc 0 below is a real evasion.

Command shape (one per tree, rc as listed):

```
python3 -B <frozen tool copy> entry --root <tree> --entry <tree>/corpus/knowledge/linguistics/secret-and-ludic-languages.md \
  --base-registry <scratch>/base-registry.md --lands-registry <tree>/corpus/SOURCES.md \
  --lesson <tree>/corpus/lessons/round-91.md --manifest <tree>/reports/round-91/evidence/manifest.json \
  --capture-dir reports/round-91/evidence --as-of 2026-11-05 --topic <claims C.topic> \
  --topic-phrases argot;anti-language;backslang;ludling;cant;in-group concealment --min-topic-phrases 4 \
  --min-bytes 12000 --min-headings 6 --min-new-ids 3 --min-topic-overlap 10 --table-min-rows 5 \
  --table-min-cols 3 --base-lesson <scratch>/base-lesson.md --graded corpus/SOURCES.md --graded corpus/lessons/round-91.md
```

| name | class | rc | PASS legs | FAIL legs | verdict |
|---|---|---|---|---|---|
| G0-control | none (compliant-shaped control) | 0 | 8/8 | – | baseline |
| V1-offtopic-filler | off-topic filler (bakery rota, phrases absent everywhere) | 1 | ENTRY SHAPE NEWIDS UNIQUENESS GATE CAPTURE APPENDONLY | TOPIC | refused (as claimed) |
| V2-phrase-gaming-headings | phrase gaming in headings: same bakery body, all 6 phrases in one h2 + one bridge sentence | 0 | 8/8 | – | **passed** |
| V3-shadow-url-fragment | new row shadows a base url via `#fragment` suffix | 0 | 8/8 | – | **passed** |
| V4-two-new-rows-one-url | two new rows share one url (S952+S955 both Lancaster home.htm) | 1 | ENTRY SHAPE TOPIC NEWIDS CAPTURE APPENDONLY | UNIQUENESS GATE | refused (as claimed; GATE fail incidental) |
| V5-gate-quote-teaching-cell | gate quote is the row teaching cell | 1 | ENTRY SHAPE TOPIC NEWIDS UNIQUENESS APPENDONLY | GATE CAPTURE | refused (as claimed) |
| V6-gate-quote-source-cell | gate quote is from the row source cell (title) | 1 | ENTRY SHAPE TOPIC NEWIDS UNIQUENESS CAPTURE APPENDONLY | GATE | refused (as claimed) |
| V7-chrome-quote-entry-sentence | task (b): gate quote is site chrome found in the capture, carried in the entry as its own sentence | 0 | 8/8 | – | **passed** |
| V8-capture-copies-graded-file | capture byte-copies a graded file (lands corpus/SOURCES.md) | 1 | ENTRY SHAPE TOPIC NEWIDS UNIQUENESS GATE APPENDONLY | CAPTURE | refused (as claimed) |
| V9-capture-copies-base-registry | capture byte-copies the *base* registry (d39434b3 bytes) — outside the graded byte set | 0 | 8/8 | – | **passed** |
| V10a-lesson-nodash-reverification | task (a): old id S776 gains a disposition with no leading dash | 0 | 8/8 | – | **passed** |
| V10b-lesson-dash-colon-flip | task (a): `- S940: NOT-LOCATED` (dash+colon) | 1 | ENTRY SHAPE TOPIC NEWIDS UNIQUENESS GATE CAPTURE | APPENDONLY | refused (colon form counts) |
| V10b2-lesson-dash-colon-gained | task (a): `- S001: LOCATED` on old id absent from base lesson | 1 | ENTRY SHAPE TOPIC NEWIDS UNIQUENESS GATE CAPTURE | APPENDONLY | refused (colon form counts) |
| V10c-lesson-blockquote | chosen: `> - S001 LOCATED …` blockquote-wrapped disposition | 0 | 8/8 | – | **passed** |
| V11-duplicate-lands-id | duplicate lands id (S952 twice) | 1 | ENTRY SHAPE TOPIC NEWIDS UNIQUENESS* APPENDONLY → 7/8 | UNIQUENESS | refused (as claimed) |
| V12-row-url-unbound-shared-capture | chosen: row url never captured; manifest reuses S955's capture for new id S960 | 0 | 8/8 | – | **passed** |

*V11 UNIQUENESS FAIL text: `duplicate ids at lands: S952`.

Every cell above is from the recorded LEG lines of that run (16 runs, each rc captured; full LEG transcripts preserved in the run output and `results.json` while scratch existed). No counterfeit was counted as passing without a rc 0 run of the frozen tool bytes against it.

Named refusal classes score: 6 of 9 hold on frozen bytes (off-topic filler, shared url, teaching-cell quote, source-cell quote, graded-file byte copy, duplicate id — V4/V11 counted in their own rows); 1 of 9 holds only in its dash form (lesson-channel re-verification: refused with `-`/`*` start, evaded otherwise); 2 of 9 hold as stated but have sibling evasions proved in the same run set (base-url shadow: exact-string match only, V3; sub-topic phrases absent from headings: refusal covers absence only, V2).
