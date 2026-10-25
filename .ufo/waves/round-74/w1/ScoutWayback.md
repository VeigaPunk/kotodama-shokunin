# ScoutWayback — carrier probes for staged rows S883/S884/S899/S900 (lane S881..S884)

Seat: scout leaf, read-only. Probes ran 2026-10-25 21:15–21:30 local (2026-10-26 00:15–00:30 UTC; `date -u` = Mon 26 Oct 2026 00:30:00). Scratch: `/tmp/ScoutWayback/` (probe.sh, cdx*.json, d*/b*/dl*.html live fetches, cap25_<ts>.html, cap22.html). No tool installed. No fleet/lane file written except this report. claims.json read, not edited.

curl 8.23.0. UA strings: **default** = `curl/8.23.0` (curl's own); **browser** = `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`. No browser automation, no captcha, no Save-Page-Now (that would write to the Archive).

## 1. Verdict table

| lane row | staged | live (curl default / browser UA) | CDX 200 captures of canonical slug | dated capture in source cell? |
|---|---|---|---|---|
| S881 litmemo.com/ja/blog/novel-worldbuilding-guide | S883 | 200 / 200 (101615 B, 3/3 each) | **none** (every shape probed; positive control OK) | **NO — live-only** |
| S882 tuduku.space/column/novel-worldbuilding | S884 | 200 / 200 (17068 B; one browser-UA SSL EOF, see §3) | **none**, and **zero captures for the whole host** | **NO — live-only** |
| S883 chinawriter…/n1/2025/0605/c404024-40494534.html | S899 | 200 / 200 (48536 B, 3/3 each) | 3 × 200; latest **20250813004013** | **YES** |
| S884 chinawriter…/n1/2022/1207/c404024-32582252.html | S900 | 200 / 200 (62604 B, 3/3 each) | 1 × 200; latest **20221207080111** | **YES** |

## 2. CDX probes (all `http://web.archive.org/cdx/search/cdx?…&output=json`; HTTP status of the CDX call itself)

Positive control (same query shape as the 4 canonical probes, `filter=statuscode:200&limit=10`):
- `url=http://example.com/&output=json&filter=statuscode:200&limit=10` → **200**, 10 rows, first `20020120142510` (`http://example.com:80/`). Also without filter → 200, same rows. Availability API `archive.org/wayback/available?url=example.com` → closest 200 `20261026000041`. The CDX endpoint therefore returns captures for a known-captured URL in this exact shape: an empty result for the four slugs is not a broken query.

Canonical probes (`…&output=json&filter=statuscode:200&limit=10`), each also repeated without the status filter (identical results):
1. `url=https://litmemo.com/ja/blog/novel-worldbuilding-guide` → 200, `[]` (no-filter: `[]`).
2. `url=https://tuduku.space/column/novel-worldbuilding` → 200, `[]` (no-filter: `[]`).
3. `url=https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html` → 200, 3 rows (header + 3):
   - `20250610015519` original `https://www.chinawriter.com.cn/n1/2025/0605/c404024-40494534.html`, len 17039
   - `20250611013901` original `http://www.chinawriter.com.cn/…/c404024-40494534.html`, len 17051
   - `20250813004013` original `http://www.chinawriter.com.cn/…/c404024-40494534.html`, len 17497
   - all digest `YLWQHESEMVFPYCHPECTNZ6Z7LLN7ZVTU` (same payload).
4. `url=https://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html` → 200, 1 row: `20221207080111` original `http://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html`, len 21294, digest `KE5X2PG2W2AZ2H2OG4VZKZSIQOB4WAF2`.

Variant probes for the two empty slugs (all 200 `[]` unless noted):
- litmemo: `http://litmemo.com/ja/blog/novel-worldbuilding-guide`; `https://www.litmemo.com/ja/blog/novel-worldbuilding-guide`; `https://litmemo.com/ja/blog/novel-worldbuilding-guide/` (trailing slash); `https://litmemo.com/blog/novel-worldbuilding-guide` (non-/ja/ path); `litmemo.com/ja/blog/novel-worldbuilding-guide&matchType=prefix` and `…guide*` (503 "Internet Archive: Temporarily Offline" once, then 200 `[]`); `litmemo.com/ja/blog/*` → 1 row only, `…/ja/blog/novel-character-relationship-map` @ `20260911102425`; `litmemo.com&matchType=domain&collapse=urlkey&filter=original:.*blog.*` → 15 blog rows (`/blog`, `/blog/character-management-guide`, `/blog/novel-three-act-structure`, `/ja/blog/novel-character-relationship-map`, `/zh-Hans/…`, `/en/…` etc.; captured 20260911 and 20261010) — **no worldbuilding-guide slug in any language**; `filter=original:.*worldbuild.*` → only `https://litmemo.com/assets/worldbuilding-Cr8K19h0.js` @ `20260911102621` (a JS asset, not the article). So the host *is* crawled (positive control for the host: domain rows exist) but the article slug is not.
- tuduku: `http://tuduku.space/column/novel-worldbuilding`; `https://www.tuduku.space/…`; `…/novel-worldbuilding/`; `tuduku.space/column/novel-worldbuilding&matchType=prefix`; `tuduku.space/*`; `tuduku.space`; `tuduku.space&matchType=domain` → all `[]`. No capture of the host at all.
- chinawriter 2025 prefix (`chinawriter.com.cn/n1/2025/0605/c404024-40494534.html&matchType=prefix`) → also lists `…html?utm_source=chatgpt.com` @ `20261010190001` (a different URL; same digest YLWQ… → same payload), len 17530. That query-string capture is NOT the canonical URL and should not be cited as the carrier.
- chinawriter 2022 prefix → same single row.

Rate/availability notes (so a re-run is not misread): an early burst got `429 Too Many Requests` from `archive.org/wayback/available` and port-80 connection refused from web.archive.org for ~2 minutes; recovered after a 90 s pause. Prefix/wildcard CDX queries returned the 503 "Temporarily Offline" page intermittently. All four canonical probes (§2 items 1–4) were answered 200 on the first shot, before the throttle.

## 3. Live fetches — status lines (QUALITY 22)

Each fetched 3× per UA with `curl -sS -m 40 -o /dev/null -D h -w code/bytes`; `-L` followed (no redirects occurred: final URL == requested).

| URL | curl default UA | browser UA |
|---|---|---|
| litmemo.com/ja/blog/novel-worldbuilding-guide | `HTTP/2 200`, 101615 B, text/html;charset=UTF-8 ×3 | `HTTP/2 200`, 101615 B ×3 |
| tuduku.space/column/novel-worldbuilding | `HTTP/2 200`, 17068 B, text/html ×3 | `HTTP/2 200`, 17068 B ×3; **first attempt** of the very first script run failed `curl: (55) OpenSSL SSL_read: unexpected eof while reading` (0 B) — a one-off transport blip, not UA walling: the same URL under the same browser UA succeeded 3/3 on immediate retry, and the default UA was 200 every time |
| chinawriter…/2025/0605/c404024-40494534.html | `HTTP/1.1 200 OK`, 48536 B, text/html ×3 | `HTTP/1.1 200 OK`, 48536 B ×3 |
| chinawriter…/2022/1207/c404024-32582252.html | `HTTP/1.1 200 OK`, 62604 B, text/html ×3 | `HTTP/1.1 200 OK`, 62604 B ×3 |

No UA wall on any of the four. The recorded UA for the evidence windows may be either; the page bytes were identical under both for all four (same byte counts). Page titles (live): S881 `世界観の作り方｜小説の世界観設定5ステップと架空の国・魔法の例 — LitMemo ブログ`; S882 `Web小説の世界観・設定の作り方｜読者を没入させる世界構築の手順と注意点 | つづく編集室`; S883 `爱潜水的乌贼：“我先设定世界观，再考虑怎么升级”--网络文学--中国作家网`; S884 `爱潜水的乌贼：网络文学不断“升级”的“奥术”--网络文学--中国作家网`.
Key-term counts in the live bytes (grep -o): S883 世界观 ×10 / 设定 ×14; S884 世界观 ×16 / 设定 ×53; S881 世界観 ×69; S882 世界観 ×27, 設定ノート ×7. (Term presence only — quote selection is another seat's job.)

## 4. Capture replay and "embeds the same original URL" (QUALITY 18)

Replayed with `http://web.archive.org/web/<ts>id_/<canonical https URL>` (raw bytes), `-L`, HTTP 200 each, final URL is the Wayback URL for the requested `<ts>` and the canonical original:
- `20250610015519`, `20250611013901`, `20250813004013` → each 48536 B, **sha256 `a3b6640ce2b1ca30dbb04a53e87d22de3939f75db06a7243d2191c2e68bee94d`, byte-identical to today's live page** (`d4.html`). So for S883 the 2025 captures and the live page are the same bytes: a quote located in the live page is verifiably present in the capture.
- `20221207080111` (`…/web/20221207080111id_/http://www.chinawriter.com.cn/n1/2022/1207/c404024-32582252.html`) → 62623 B, title `爱潜水的乌贼：网络文学不断“升级”的“奥术”--网络文学--中国作家网`, article published `2022年12月07日10:07`; differs from live (62604 B, sha `344de345…`) only in chrome: http↔https link schemes, an extra `portamento.js` tag, a share-script URL, `&nbsp;` vs space in the byline, and the footer owner line (`文艺报社` live vs `中国作家出版集团` capture; one phone-number line dropped). With tags stripped, whitespace and `&nbsp;` normalised, the texts differ **only** in those footer spans (offsets 12003–12151 of 12233 chars) — the article body text is identical, so an S884 quote from the body appears in the capture.
- The pages themselves embed **no** self-URL: `grep canonical|og:url` and `grep c404024-…` find nothing in the chinawriter pages (so "embeds the original URL" is satisfied only by the Wayback replay path/CDX `original` field, not by an in-page tag). litmemo (`rel=canonical` = `https://litmemo.com/ja/blog/novel-worldbuilding-guide`) and tuduku (`canonical` and `og:url` = `https://tuduku.space/column/novel-worldbuilding`) do embed their own canonical URL, but have no capture to cite.
- CDX `original` for 2025 captures 2 and 3 and for the 2022 capture is the `http://www.…` scheme; capture 1 is `https://www.…`. Wayback normalises both to the same key (`cn,com,chinawriter)/n1/…`), and the https replay path served each timestamp. Cite the https canonical plus the timestamp; the capture was verified at those exact `<ts>id_` paths.
- I did not fetch the non-`id_` replay form or check Wayback's per-capture sub-resources; only the HTML payload was compared.

## 5. Answers to the assignment

- **Can each row carry a dated capture in its source cell?** S883 (chinawriter 2025) yes — latest 200 `20250813004013` (earliest `20250610015519`; all same digest, identical to live bytes). S884 (chinawriter 2022) yes — sole 200 capture `20221207080111` (body text identical to live). S881 (litmemo) and S882 (tuduku) **no**.
- **Live-only pages:** S881 and S882. For these the source cell can only carry the live fetch date (2026-10-25 under whichever UA is recorded) and the local evidence-window bytes; a "no capture" ruling is supported by: canonical CDX probe (filter and no-filter) empty, six litmemo / seven tuduku URL/prefix/domain variants empty, and positive controls — `example.com` in the identical query shape returns rows, and `litmemo.com` host rows exist (so the empty slug is not an unreachable index) while `tuduku.space` has no rows for the host at all. Residual risk: S881's litmemo host was first captured 20260911, i.e. new/low-footprint; absence is "not captured as of 2026-10-26 00:30 UTC", not "never will be".
- **Row implication for the claim [INFERENCE]:** `row_set` S881..S884 assumes a uniform carrier; two of four rows have no archive carrier, so recheck/evidence cells for S881/S882 must be live-fetch-dated only; any leg demanding a Wayback capture timestamp for all four rows would fail on S881/S882 by construction.
- The 503 "Temporarily Offline" pages and 429 responses were Archive-side throttling and were retried; no result in §2 rests on a throttled response.
