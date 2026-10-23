# FixRowS722 — anchor locator repair

- **Axis:** coverage (row provenance locator); no operability or calibration behavior changed.
- **Changed file:** `.ufo/waves/round-64/rows/ScribeRowS722/row.txt` only.
- **Anchor:** old `Section A Continuous Vocabulary Spurt, paragraph 35`; new `New Directions and Next Steps, paragraph 35`. No other row fields changed.
- **Live evidence:** reopened https://pmc.ncbi.nlm.nih.gov/articles/PMC5182137/. The quote appears below the heading `New Directions and Next Steps`: “This emerging view emphasizes the importance of domain-general processes like novelty, attention, statistical learning, association, competition, and parallel learning, as well as ecological factors like the properties of the body and communicative context.”
- **Check:** `python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows` → `CHECK-ROWS: 32/32 clean` (all S718–S749 rows reported OK).
- **Risks/blockers:** none observed for this locator-only repair; no tools installed.
