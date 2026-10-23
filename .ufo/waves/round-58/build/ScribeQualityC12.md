# Round 58 — QUALITY criterion 12 proposal

## Finding
The routed defect is a calibration failure: two source grounds stated as factual checks were wrong. Round 56 says koon1244 has “no quotable passage” (lesson line 83); the round-57 erratum says the opened JSON and N3 contain quotable fields and that non-registration was actually because S379 already carried the classification (round-57 lesson line 105). Round 57 says CODH quotes fall below the eight-word locator minimum (lesson line 92); the verifier spot-check records four quotes normalizing to 11/10/15/11 words, each `LOCATED` by `reopen-quote.py` (spot-check §3, line 169; routed defect §5.1, line 203). These observations are from the opened lesson records; this seat did not rerun the tools.

## Exact append-only text

12. **Re-test stated rejection grounds** — A reject or not-registered reason that names a tool, gives a measurable result (such as a word count, locator failure, or HTTP error), or asserts a source property that can be checked by a tool names the re-test tool and includes its verbatim output in the lesson's Gate line. Without that output, the reason is unverified and cannot justify the decision. Grounded in the round-56 koon1244 reason (“no quotable passage,” contradicted by quoted JSON fields) and round-57 CODH reason (“below the 8-word minimum,” contradicted by four quotes that each locate).

## Scope and evidence
- Reviewed `corpus/QUALITY.md` in full (criteria 1–11), `corpus/lessons/round-57-verifier-spotcheck.md` §§3 and 5 items 1–2, `corpus/lessons/round-56.md:83`, and `corpus/lessons/round-57.md:92` (also the koon1244 erratum at line 105).
- Axis: calibration. Proposed behavior: re-test measurable/source-checkable rejection grounds and preserve the tool output in the Gate line; unsupported reasons cannot support the disposition.
- Gates: no acceptance, build, or test commands run. The prior `LOCATED` results are reported only as evidence recorded in the verifier spot-check, not as execution by this seat.
- Touched surface: this report only. `corpus/QUALITY.md` and both lesson files remain unchanged; criterion 12 is proposed, not applied.
- Out of scope: any erratum, registry or lesson edits, and any new source/tool re-test.
- Artifact: `.ufo/waves/round-58/build/ScribeQualityC12.md` in the Kotodama lane.
- Installs: none.
