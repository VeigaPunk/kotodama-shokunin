# S739 scope-anchor repair

Reopened the live PDF at `https://journal.uny.ac.id/index.php/litera/article/download/39455/pdf`. The selected sentence is in **RESULTS AND DISCUSSION > Results**, in the paragraph beginning “Based on the data obtained”; it reports the study's own urban Sleman findings. Kept tier A and the existing scope because this primary-results evidence supports them.

## Old → new cells

- **Scope (unchanged):** `parental use of address terms with children in urban Sleman, Indonesia`
- **Tier (unchanged):** `A`
- **Anchor:** `introduction, paragraph beginning According to Aledo (2018): "Parents can use various terms of address to children depending on situational contexts."` → `RESULTS AND DISCUSSION > Results, paragraph beginning Based on the data obtained: "Based on the data obtained, urban parents in Sleman, Yogyakarta used various forms of address when interacting with their children."`
- **Teaches:** `Helps worldbuilders model how caregivers vary terms of address across situations as children learn community language practices.` → `Helps worldbuilders model urban parents' use of varied address forms with children.`
- **Bullet:** `Parents use various terms of address with children across changing contexts, shaping culturally situated family communication.` → `Study results show urban parents in Sleman using varied address forms when interacting with their children.`

The scope, tier, source identity, live URL, archived capture, status, date, recheck interval, and used-by field were otherwise retained. The new bullet tracks the selected results sentence and avoids claiming that the results sentence itself establishes variation across situations.

## Evidence and limits

- Direct live-PDF read showed the exact selected sentence under Results.
- Lane locator: `python3 -B reports/round-61/reopen-quote.py 'https://journal.uny.ac.id/index.php/litera/article/download/39455/pdf' 'Based on the data obtained, urban parents in Sleman, Yogyakarta used various forms of address when interacting with their children.'` → `LOCATED https://journal.uny.ac.id/index.php/litera/article/download/39455/pdf`.
- Latest required row check: `python3 -B .ufo/waves/round-64/check-rows.py --rows-dir .ufo/waves/round-64/rows` reported `S739 OK` and `CHECK-ROWS: 31/32 clean`; the only reported problem was `S719 PROBLEMS bullet_shape`. Thus the S739 row passes the checker, but I cannot report a 32/32 result from this run. I did not edit S719 or any other row.
- No tools installed; no other files changed except this scoped report.
