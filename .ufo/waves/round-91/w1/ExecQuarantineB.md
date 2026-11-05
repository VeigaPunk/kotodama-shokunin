# ExecQuarantineB — kotodama round-91 quarantine hand-check (11 rows)

Seat: ExecQuarantineB (leaf executor). Lane: kotodama round-91, milestone r91-v1, judged on coverage.
Input: `reports/round-91/quarantine/slice.tsv`. Rows: S807, S812, S814, S816, S817, S820, S823, S824, S825, S827, S835.
Adopted: nothing. Each row carries a verdict only. No production file was written.

## Outputs
- `.ufo/waves/round-91/w1/stage/ExecQuarantineB/verdicts-B.json` (11 objects: id, url, http_status, bytes, sha256, fetched_at, fragments[{text,in_raw,in_folded}], verdict, note)
- `.ufo/waves/round-91/w1/stage/ExecQuarantineB/verdicts-B.md` (one table row per id, commands, full notes)
- `.ufo/waves/round-91/w1/stage/ExecQuarantineB/caps/<id>.bin` (raw response bytes, 11 files)
- `.ufo/waves/round-91/w1/stage/ExecQuarantineB/scripts/` (driver scripts + SHA256SUMS)

## Verdicts

| id | class-as-registered | verdict | http | bytes | fragments found/total |
|---|---|---|---|---|---|
| S807 | prose: "could not be fetched…" | UNVERIFIABLE | 200 | 597992 | 0/0 |
| S812 | prose: "could not be fetched…" | UNREACHABLE | 429 | 1478 | 0/0 |
| S814 | `payload-absent` | UNREACHABLE | 403 | 162 | 0/1 |
| S816 | `payload-absent` | ABSENT | 200 | 48536 | 0/1 |
| S817 | `payload-absent` | ABSENT | 200 | 62604 | 0/1 |
| S820 | `payload-absent` | ABSENT | 200 | 417093 | 0/1 |
| S823 | `payload-absent` | UNREACHABLE | 468 | 14863 | 0/1 |
| S824 | `payload-absent` | ABSENT | 200 | 504441 | 0/1 |
| S825 | `payload-absent` | ABSENT | 200 | 311308 | 0/2 |
| S827 | `payload-absent` | LOCATED | 200 | 325782 | 3/3 |
| S835 | prose: "could not be fetched…" | UNREACHABLE | 503 | 690 | 0/0 |

Per-row sha256 and fetched_at are in verdicts-B.json. All fetches were issued 2026-11-05 at 08:19:46 -03:00 (the JSON records the per-row instant).

## What each URL served (what was observed)
- **S807** (prose row): now fetches. DOI redirect → onomajournal.org Onoma 51 article PDF ("Linguistic composition and characteristics of Chinese given names", Kałużyńska). The prose "could not be fetched" is stale. No quote in the cell, so UNVERIFIABLE.
- **S812** (prose row): Cambridge 429 "Too many automated requests from this network." DOI redirect → cambridge.org S0008413124000215. Unreachable by ordinary request.
- **S814**: nginx `403 Forbidden`, 162 B.
- **S816**: 2xx UTF-8 article (爱潜水的乌贼 interview). The cited words 肯定考虑过 and 资深读者 appear nowhere in the body.
- **S817**: 2xx UTF-8 Chinese web-literature article (爱潜水的乌贼). The registered English fragment ("Sowers-Wills… Phonology from the inside out") appears nowhere.
- **S820**: 2xx PDF, Onoma 51 article. The quote is present in the pdftotext text layer; the registered fragment fails only on the quote glyph. Test: ASCII `'standard given names…` → False; curly `“standard given names…` → True; no-quote form → True. Under the prescribed byte-level pipeline it is ABSENT.
- **S823**: HTTP 468 SafeLine WAF page (`/.safeline/static/` assets, empty `<title id="slg-title">`).
- **S824**: 2xx PDF (Osaka U repository, 王愛静, 大阪大学言語文化学 2009). The fragment's two halves occur separately in the text layer (習俗、輩行字を使って名づける: True; 輩行字命名の習俗: True). The full contiguous fragment does not occur (False in both `pdftotext` plain and `-layout`). ABSENT under the pipeline.
- **S825**: 2xx server-rendered 国立公文書館デジタルアーカイブ 詳細検索 page, 6838 visible chars; not a JS shell. Component labels occur (元号名称 開始西暦年; 令和 2019; 平成 1989; 昭和 1926; 大正 1912; 明治 1868: all True). The full line is not contiguous after fold, and the second fragment 元号名称／開始西暦年 is not present (fullwidth slash folds to `/`). ABSENT as served today.
- **S827**: DOI redirect → link.springer.com chapter 10.1007/978-3-032-03277-5_15, 200. All three cited snippets found (3/3): LOCATED.
- **S835** (prose row): repository maintenance 503 page, 690 B: 「現在システムメンテナンスのためリポジトリをご利用いただけません。停止期間：2026年10月28日 (15:00-)」.

## Commands run (all ordinary requests; no browser, no challenge passing, no login)
For each id, one fetch exactly as specified:
```
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineB/caps/<ID>.bin -w '%{http_code} %{size_download} %{content_type}' '<URL>'
```
DOI redirect-target check (S807, S812, S827 only):
```
curl -sS -I -L --max-time 40 -o /dev/null -w '%{url_effective} %{http_code}' '<DOI URL>'
```
Driver: `python3 scripts/check_rows.py` (fetch, folded/raw copies, fragment test, verdict; rc 0). Note refinement: `python3 scripts/diagnose.py` (rc 0). Note correction and idempotent rewrite: `python3 scripts/fixup.py` (rc 1 only at its final cosmetic `print`, after both output files were written). Fragment-level checks for S820, S824, S825 were run inline with `pdftotext -q` (rc 0) and Python substring tests.

## Method and deviations (stated, not hidden)
- Folded copy per spec: UTF-8(replace) → tags to one space → HTML entities decoded → U+00A0/U+2003 to space → NFKC → whitespace collapsed → casefold. Fragment strings are normalized the same way (NFKC/casefold/entities).
- Fragments are split on `…`, three dots, and `<br>`. The `<br>` split is an addition: the register uses `<br>` as a snippet separator. Fragments under 6 characters are dropped (S807/S812/S835 have no quote cells).
- `in_raw` is the raw-decoded body with the same entity/NFKC/casefold/whitespace normalization but NO tag stripping. It is not a byte-exact search. It did not change any verdict.
- PDF text-layer and re-encoding checks are diagnostics in notes only, never verdicts (as specified).
- Verdicts for the three prose rows follow the seat rule: fetch fails → UNREACHABLE; fetch succeeds → UNVERIFIABLE. S807 fetched (UNVERIFIABLE); S812 and S835 failed (UNREACHABLE).

## Counts
- Rows: 11. LOCATED 1 (S827). PARTIAL 0. ABSENT 5 (S816, S817, S820, S824, S825). UNREACHABLE 4 (S812, S814, S823, S835). UNVERIFIABLE 1 (S807).
- Fragments: 3/3 found in S827; 0/1 in S814, S816, S817, S820, S823, S824; 0/2 in S825; 0/0 for the three prose rows.
- Measured 2026-11-05 by the commands above; counts from verdicts-B.json.

## Not measured / limits
- No headless browser; no JS execution. S825 was judged server-rendered from its visible text, not by executing its scripts.
- Wall marker bodies were identified from the response bytes only; no challenge was passed.
- S820 and S824 are PDF text-layer diagnostics; the byte-level pipeline is what sets their verdict.

## Tooling
- No install or upgrade by this seat. `curl` and `pdftotext` (poppler) were used as already present on the host. No pacman transaction, no `uv tool install`, no `~/.local/bin` write. The driver's `uv run --with pypdf` fallback was not needed (pdftotext succeeded).

## Hygiene
- Writes: stage dir and this report only. Scratch `/fast/scratch/hyaku/kotodama-r91/ExecQuarantineB/` deleted at yield. No commit, push, git mutation, or sibling-lane/production write.
- Checks for the main agent to run: none required from this seat (verification is the main agent's job). Re-check by re-running `scripts/check_rows.py` (verdicts depend on live servers; the fetch instants and sha256 in verdicts-B.json are the evidence of what was observed on 2026-11-05).
