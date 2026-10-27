# round-76 Gate (fixture)

## Gate

| source | quote | evidence | verdict |
|---|---|---|---|
| S894 | 「alpha span」 | `reports/round-76/evidence-clean/S894.txt` | admitted |

Rejections — each with the artifact it was observed on, the reason, and the flip:

| reason | flip | probed URL | verdict |
|---|---|---|---|
| the quote 「alpha span」 is absent from reports/round-76/evidence-clean/S895.txt (0 hits) | a fresh quote located on the same page | https://example.invalid/a | refused; not used |
| 「beta span」 is present once on reports/round-76/evidence-clean/S895.txt (1 hit) | another page of the same document | https://example.invalid/b | refused as a live-only anchor |
| a reason that names no artifact and a `backticked` quote | flip | https://example.invalid/c | refused |
