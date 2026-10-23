# ReviewSupportA — round-64 wave-1 blind support (claim C falsifier), rows S718–S727

Seat: `kotodama-r64.ReviewSupportA`. Scope: for each staged row in
`.ufo/waves/round-64/rows/ScribeRowS7{18..27}/row.txt`, re-open the live URL
(plain GET, `curl -sSL --max-time 60`, browser UA; archived `id_` capture as
fallback), locate the anchor quote verbatim, and judge whether the BULLET
faithfully restates ONLY what the quoted passage supports at the row's tier.
Run date: 2026-10-23. No row files edited. No tools installed (system `curl`,
`pdftotext` sufficed; pacman untouched).

## Fetch results

| Row | Live GET | Fallback | Anchor quote located |
|-----|----------|----------|----------------------|
| S718 | HTTP 200, 197,724 B | — | verbatim, Results (utterances/min) |
| S719 | HTTP 200, application/pdf, 327,063 B | — | verbatim, §4 first paragraph |
| S720 | HTTP 200, 295,680 B | — | verbatim, Abstract |
| S721 | HTTP 200, 318,427 B | — | verbatim, "developmental trajectory…" ¶1 |
| S722 | HTTP 200, 198,771 B | — | verbatim (see locator defect D2) |
| S723 | — | — | row.txt MISSING |
| S724 | HTTP 200, 142,861 B | archive capture | verbatim, opening ¶ |
| S725 | HTTP 200, 298,211 B | — | verbatim, Introduction (Farrar 1992) |
| S726 | HTTP 200, 13,576 B | — | verbatim, ERIC abstract claim (1) |
| S727 | HTTP 429 | capture `20260323195634id_` HTTP 200 (gzip) | verbatim, publisher abstract final sentence |

## Verdicts

- **S718 — SUPPORTED.** Quote: "Lebanese mothers, compared to American
  mothers, produced more IDS". Bullet keeps the pairwise sample scope ("in
  this sample") matching the row's scope field; no overclaim.
- **S719 — NOT-SUPPORTED (overclaim by caveat omission).** The anchor quote
  itself ends "(with the aforementioned caveats)" and §3 (PDF pp. 5–6 /
  printed 161–162) supplies them: "the draw towards IDS is modulated by
  experience. First, newborns can actually prefer their mother's ADS over
  her IDS", weaker preference for male voices, and of four synthetic-pitch
  experiments one positive, one opposite, two null. The BULLET "Infants
  attend preferentially to IDS-like prosody, helping caregivers attract a
  baby's attention" asserts the preference flatly — it states more than the
  quoted passage supports (the passage's own qualifier, quoted verbatim in
  the row, is dropped). Cross-verified independently by
  `kotodama-r64.CriticEntrySweep` (same PDF, same caveat locus).
- **S720 — SUPPORTED.** Quote verbatim in Abstract; bullet preserves the
  "may" hedge and the canonical-syllable → language-specific-shape link.
- **S721 — SUPPORTED.** Quote verbatim; bullet restates the
  proto-conversation definition; the "gives worldbuilders a basis" clause
  is the entry's frame gloss, not an added empirical claim.
- **S722 — SUPPORTED, with anchor-locator defect (D2).** Quote verified
  verbatim, but the live article places it under heading "New Directions
  and Next Steps" (byte ~78,044 of the HTML), NOT "Section A Continuous
  Vocabulary Spurt" as the row locator states (that section runs
  ~73,052–78,044). The passage supports the bullet; the recorded locator
  is wrong — provenance defect, not a support failure. "toddlers" is
  within the row's word-learning scope.
- **S723 — UNREACHABLE.** `.ufo/waves/round-64/rows/ScribeRowS723/row.txt`
  does not exist (read error). There is no ROW, quote, or BULLET to test.
  This is the known inherited defect from dead attempt-1 (30/32 clean under
  `check-rows.py`); it must be filled before claim C's ROWS leg can pass.
- **S724 — SUPPORTED.** Live GET returned HTTP 200 today (the row's VERIFY
  note records a 403 — stale access note, favorable drift; archive capture
  also available). Quote verbatim under the telegraphic-speech opening
  paragraph; "fewer inflectional morphemes" reads the implicit comparative
  (vs adult speech) — acceptable restatement.
- **S725 — SUPPORTED.** Quote verbatim (Farrar 1992 result cited in
  Introduction); bullet restates the maternal-morpheme imitation claim with
  "may", matching the "more likely to" hedge.
- **S726 — SUPPORTED.** Quote verbatim in the ERIC record's numbered
  abstract claim (1). "linked to social membership" is weaker than "deeply
  affected" — no overclaim.
- **S727 — SUPPORTED.** Live 429; `id_` capture verified verbatim. The
  bullet maps turn-taking/clarification/interpretation → "local caregiving
  beliefs", inside the abstract's "beliefs and expectations concerning the
  nature of children and the social organization of caregiving".

## Defects found (in scope)

- **D1 (high): S719 caveat-erasure.** Row BULLET (and the same clause in
  `stage/bullets.json` per CriticEntrySweep) drops the quote's own
  "(with the aforementioned caveats)" qualifier and asserts a flat
  preference the source explicitly modulates. Fix: hedge the bullet
  ("often / in most age groups / with documented exceptions").
- **D2 (medium): S723 row missing.** `ScribeRowS723/row.txt` absent —
  claim C needs 26 mined rows S718–S743; a missing row leaves the entry's
  bullet table one short and its row contribution unverifiable.
- **D3 (low): S722 locator wrong.** Quote lives under "New Directions and
  Next Steps", not "A Continuous Vocabulary Spurt". Fix the row's locator
  string; support itself verified.

## Residual risk / verification gaps

- Verdicts judge bullet↔quote fidelity only; the stage-level bullets
  (`stage/bullets.json`) are separately under review by CriticEntrySweep —
  its S719 finding independently converges on D1.
- S726 live page is the ERIC metadata record (13,576 B); the underlying
  working-paper full text was not fetched — the scoped anchor is the ERIC
  abstract, which was verified.
- S727 assessed via `id_` byte-capture only (live 429); a later live GET
  may succeed, but the capture is a faithful same-URL snapshot.
- S720's bullet compresses the abstract's two-case phrasing ("words or
  canonical syllables") into the canonical-syllable clause; within row
  scope and preserved hedges, but slightly narrower than the full quote.
- Tools: none installed; `curl` + `pdftotext` (system) used. Scratch:
  `/home/vgpnk/.cache/hyaku/kotodama-r64-w1/ReviewSupportA/`.
