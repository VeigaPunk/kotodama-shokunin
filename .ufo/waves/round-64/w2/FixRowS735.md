# FixRowS735 — claim C

## Change

Updated only the `BULLET` in `rows/ScribeRowS735/row.txt`.

- Old: `- Teacher questions and comments shape sharing-time discourse toward structure and focus, showing how oral classroom interaction can rehearse literacy. (S735)`
- New: `- In the observed classroom, the teacher tried through questions and comments to help children structure and focus their discourse. (S735)`

The revised statement reports the teacher's attempt, not successful scaffolding or a learning/literacy outcome, and is bounded to the observed classroom. Anchor and teaches cells were left unchanged.

## Evidence

- Lane locator: `python3 -B reports/round-61/reopen-quote.py 'https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf' 'The teacher, through her questions and comments, tries to help the children structure and focus their discourse.'` → `LOCATED https://www.ling.ohio-state.edu/research/groups/lacqueys/readings/earlier/Michaels1981.pdf` (canonical pypdf path, not pdftotext).
- Ran `python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows`. At the final observed run, `S735 OK`, but the full result was `CHECK-ROWS: 29/32 clean`, not 32/32: S728 reported `bullet_shape`, S739 `quote_words=5 in_order=0`, and S742 `bullet_shape`. These are outside this assignment's editable path; rerun after wave integration.

## Axes / risk

- Coverage: retains the specific classroom finding without generalizing literacy success.
- Calibration: removes the unsupported success/learning implication and preserves the source's attempt wording.
- Operability: S735 passes the row checker; the observed full-set check is blocked from 32/32 by the three non-S735 rows above.

No tools installed or updated.

Report: .ufo/waves/round-64/w2/FixRowS735.md
