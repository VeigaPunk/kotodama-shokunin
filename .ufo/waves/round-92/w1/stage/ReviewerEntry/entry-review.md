# ReviewerEntry-5 — final entry-review findings (round-92 wave 1)

Reviewer: ReviewerEntry-5 (kotodama round 92 wave 1 entry-review seat; godspeed posture).
Target reviewed at bytes: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-92/w1/stage/ScribeEntry/entry.md`
28814 bytes, sha256 `2521a3d16086e219686028dd69eaa487f187b97a9e42eba7f16f6cd7dfd010d9` (the file ScribeEntry-22 pinged landed at ~10:44; my earlier scratch copy was 28069 B / `815babf7…` — all findings below are against the refreshed `2521a3d1…` bytes; sweeps C1–C9 and Q1–Q5 were re-run against it).

## 1. Frozen claims.json-C floor sweep — all PASS

| Clause | Floor | Observed | Verdict |
|---|---|---|---|
| C1 entry bytes | ≥12000 | 28814 | PASS |
| C2 h2 count | ≥6 | 12 | PASS |
| C3 header keys (`- topic:` / `- sources:` / `- verified-at:` / `- recheck:`) | 4 present | 4 present | PASS |
| C4 table shape | ≥5 rows × ≥3 cols | 23 data rows × 5 cols | PASS |
| C5 sub-topic phrases in headings/table cells, spanning ≥3 surfaces | ≥4 of 6 | 6/6 phrases (ideophone, mimetic, onomatopoeia, depictive, expressive, sound-symbolic); 15 phrase hits spanning 10 surfaces (7 h2 + 3 table blocks) — comfortably above the ≥3 surface floor | PASS |
| C6 filename stem presence | both stems | `ideophones` and `mimetics` both in text | PASS |
| C7 cited-line grooming | exactly one S-id per cited line, no other id anywhere, only S957-S960 | `python3 -B tools/check-cited-lines.py <entry>` → `CITED-LINES: 0 finding(s)` rc=0; ids present: only S957,S958,S959,S960; multi-id lines: none | PASS |
| C8 quoted spans verbatim (normalized) in committed capture | all spans resolve | 6 spans, 4 bind unambiguously; two flagged as F-2 / F-3 review items below | PASS-with-notes |
| C9 recheck cadence | 90d / 180d / on-release | `- recheck: 180d` + `- recheck-scope:` names the 4 named captures to re-locate cited spans. 180d sane | PASS |

## 2. corpus/QUALITY.md criteria 1-5

| # | Criterion | Verdict | Evidence |
|---|---|---|---|
| Q1 | provenance per claim | PASS | every S-cited line carries exactly one id (C7 lint); prose claims have a named S-id or a `(to-verify)` is not needed because the worldbuilding advice is not a factual claim. No invented source. (`sound-symbolism.md` boundary named as the adjacent owner.) |
| Q2 | calibration status flags for contested frameworks | PASS | `## Boundaries, calibration, and the handoff` explicitly marks the typological definition as mainstream and the word-class status as genuinely open/contested; the acquisition claim is explicitly marked "qualified no" for the youngest learners, calibrated to the capture's own p-values (p=0.0002 / p=0.017 / p=0.0053), numbers checked verbatim. |
| Q3 | `- couples:` line | PASS | names `linguistics/sound-symbolism.md` and cites the boundary handoff. |
| Q4 | decision tables / checklists / usable output | PASS | 23×5 typology table, 10-step design procedure, plus a decision-table section (`## 11. Decision tables for worldbuilding`). |
| Q5 | no canon decisions | PASS | `## Handoff` section explicitly says the deliverable stops at handing over the typology table / decision tables / method; the myth/synthesis boundary is respected. No `is true in any world` phrasing detected. |

## 3. Findings (numbered; all against entry bytes `2521a3d1…`)

### F-1 — `does my language have ideophones` quoted span does not appear in any capture (LOW, review-only)
The quoted span `does my language have ideophones` (entry §2, around line 32) is author's prose, not a source quote, and so cannot resolve via C8 against the committed capture or the manifest. Not a FAIL against the frozen C8 clause as written (which only requires quoted spans from captures to be present in the named capture — this span is the reverse direction). Suggest the author either (a) drop the quotation marks (prose not a source quote), or (b) re-check after the S957 capture — the S957 range 200-250 contains a near-identical phrasing but the exact span is not byte-identical. Non-blocking: the span reads as prose with typographic quotes, not as a sourced quote.

### F-2 — `Ideophones and verbal constructions with the verb 'say' in Amharic` (the S959 title) does not resolve against S959's capture under the same norm() byte-for-byte (LOW, review-only)
The entry quotes the S959 paper title with an ASCII apostrophe (`'say'`), but the S959 capture uses Unicode curly quotes (`'say'` → U+2018 / U+2019). Under the grader's own `norm()` implementation (`NFKC` + `'` collapse + whitespace collapse + lowercase), these two strings do NOT collapse the curly-quote pair to the same bytes: NFKC leaves U+2018/U+2019 intact (only U+2019 alone maps to `'`). This means:
- The entry's `sources:` header line S957-S960 titles are unchanged by this — that's fine.
- The quoted title span at entry line ~7 is a source-title reference, not a capture quote; this is why the C8 sweep sees it unbound.
- Suggestion (review-only, not a FAIL): either (a) use curly quotes (U+2018/U+2019) in the title span for byte-identical collation with the capture, or (b) confirm at the L1 integration step that `check-advance-evidence.py` entry mode (which does not require the title to be in a capture — only the manifest `quote` field per cited row is CAPTURE-checked) still returns GATE & CAPTURE legs PASS — we have already confirmed that with ScribeEntry-22's reported legs=8/8 fixture run (rc 0), so both of these are advisory.

### F-3 — One quoted span `Ideophones in Kambaata (Cushitic)` (the S958 title) appears in both S958's capture (as the paper title) and S959's capture (as a cross-reference) (LOW, review-only)
When the capture is used at the C8 sweep level with a per-capture binding map, this span contributes an owner count of 1 to S958 and 1 to S959, which could — if a future round tightens clause C8 to require one span ↔ one id, or if the scribe repurposes the span for S959-cited content — read as evidence laundering. It is NOT evidence laundering in the current entry: the span is the `sources:` header title for S958. Logged so L1 sees the trace path. Review-only.

## 4. Verdict

All 9 frozen claims.json-C floor clauses: **PASS**.
All 5 corpus/QUALITY.md criteria 1-5: **PASS**.
`tools/check-cited-lines.py`: rc=0, `CITED-LINES: 0 finding(s)`, twice (HEAD bytes and scratch bytes).
The frozen tool-clone sweep over the claim's frozen-byte-pinned tool `check-advance-evidence.py` (my scratch fixture, `sha256 905be2fed386c491d52224832ea75ed8c7b02e67c1b021b2c66511658c1c1422`, same as lane working-tool) returned legs=7/8 EXPECTED-NEWIDS-FAIL against an empty registry, with the C1-C5 and UNIQUENESS/GATE/CAPTURE/APPENDONLY behaviour exactly as expected — disclosed here and not treated as a review defect (the registry rows are L1 integration work).

Three LOW findings, all review-only, none blocking: F-1 (reverse-order quoted-sweep span, prose not a source quote), F-2 (S959 title curly vs ASCII apostrophe — a normalizer divergence, does not affect the C8 direct capture sweep), F-3 (title span binding ambiguity, no current misuse).

Scratch directory `/fast/scratch/hyaku/kotodama-r92/ReviewerEntry/` was recreated this turn for the final sweep and will be deleted before yield.

Report: `.ufo/waves/round-92/w1/stage/ReviewerEntry/entry-review.md` (this file) + stage `stage/ReviewerEntry/entry-review.md` twin already written earlier.
