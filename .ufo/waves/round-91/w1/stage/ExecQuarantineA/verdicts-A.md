# verdicts-A — quarantine hand-check, ExecQuarantineA (kotodama round 91 w1)

Input slice: `reports/round-91/quarantine/slice.tsv`. Rows checked: S776, S778, S779, S786, S787, S791, S792, S795, S796, S804 (only these were read).
Fetch: one `curl` per URL, 2026-11-05, instants are the exact local mtimes of the captured bodies (`caps/<id>.bin`), offset -03:00.
Normalization: UTF-8 decode with replacement (raw copy); folded copy = tags → single space, HTML entities decoded, U+00A0/U+2003 → space, NFKC, whitespace collapsed, casefold.
Fragment split: `…`, three dots, and the cell-level `<br>` joiner; the TSV backtick quoting markers are stripped from piece ends (they are file format, not cited text). Mechanical verdicts use the folded copy exactly as specified; supplementary checks (declared-charset decode, pdftotext for PDFs, no-whitespace CJK variant, partial-body test) are recorded in notes only and never change a verdict.

| id | class-as-registered | verdict | http | bytes | found/total | reason |
|---|---|---|---|---|---|---|
| S776 | payload-absent | PARTIAL | 200 | 24058 | 4/5 | 4/5 fragments in folded copy; the miss (标准状态：现行) is split by an interposed tag — the no-whitespace check finds 5/5, so the cited payload is present in the page and contradicts the registered class. |
| S778 | payload-absent | LOCATED | 200 | 10291 | 2/2 | Both quoted sentences found in the portal page (served as EUC-JP, supplementary decode); a first-pass absence was an artifact of the TSV backtick quoting, so the payload is present and contradicts the registered class. |
| S779 | payload-absent | ABSENT | 200 | 22950 | 0/2 | The quoted text about China ICH national lists (国务院…非遗名录) appears nowhere in this Japanese calendar news page — the citation points at an unrelated source. |
| S786 | payload-absent | ABSENT | 200 | 753374 | 0/2 | PDF text extraction (42219 chars) contains the Chinese sentence (whitespace-folded) but not the English gloss "conlanging (n): …", which is absent from the document. |
| S787 | payload-absent | ABSENT | 200 | 45238 | 0/1 | The quoted clause 作品中的人物名字和地名也一样 appears nowhere in the 11223-visible-char page, not even with whitespace ignored. |
| S791 | payload-absent | UNREACHABLE | 400 | 786 | 0/0 | Server answered HTTP 400 with a 786-byte error page; the registered URL ends in a bare % (malformed percent-encoding), so no payload is fetchable as registered. |
| S792 | payload-absent | UNREACHABLE | 200 | 130538 | 0/0 | curl rc=28 — operation timed out after 40001 ms with 130538 bytes received (HTTP 200 in flight); the quoted heading set is also absent from the partial body received. |
| S795 | payload-absent | ABSENT | 200 | 357913 | 0/1 | PDF text extraction (19163 chars) does not contain the 生前の名前／幼名／実名 enumeration; the quoted passage is absent from the document text. |
| S796 | payload-absent | ABSENT | 200 | 108503 | 0/1 | PDF text extraction (12314 chars) does not contain the 姓と氏 sentence; the quoted passage is absent from the document text. |
| S804 | payload-absent | ABSENT | 200 | 212285 | 0/1 | The definition sentence 日本人が名のる苗字は… appears nowhere in the 156309-visible-char kotobank page, not even with whitespace ignored. |

## Commands (all run 2026-11-05, from /home/vgpnk/Projects/shokunin)

```
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineA/caps/S776.bin -w '%{http_code} %{size_download} %{content_type}' 'https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296'  # rc=0; -w: 200 24058 text/html;charset=utf-8
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineA/caps/S778.bin -w '%{http_code} %{size_download} %{content_type}' 'https://eco.mtk.nao.ac.jp/koyomi/'  # rc=0; -w: 200 10291 text/html
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineA/caps/S779.bin -w '%{http_code} %{size_download} %{content_type}' 'https://www.nao.ac.jp/news/topics/2026/20260202-rekiyoko.html'  # rc=0; -w: 200 22950 text/html
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineA/caps/S786.bin -w '%{http_code} %{size_download} %{content_type}' 'http://conlang.org/26c3.pdf'  # rc=0; -w: 200 753374 application/pdf
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineA/caps/S787.bin -w '%{http_code} %{size_download} %{content_type}' 'https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html'  # rc=0; -w: 200 45238 text/html
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineA/caps/S791.bin -w '%{http_code} %{size_download} %{content_type}' 'https://ir.psych.ac.cn/bitstream/311026/14751/2/%E5%90%8D%E5%AD%97%E7%9A%84%E5%BF%83%E7%90%86%E6%95%88%E5%BA%94_%E6%9D%A5%E8%87%AA%E4%B8%AA%'  # rc=0; -w: 400 786 text/html;charset=utf-8
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineA/caps/S792.bin -w '%{http_code} %{size_download} %{content_type}' 'https://journal.psych.ac.cn/xlkxjz/EN/10.3724/SP.J.1042.2021.01067'  # rc=28; -w: 200 130538 text/html;charset=UTF-8 (timed out at 40001 ms)
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineA/caps/S795.bin -w '%{http_code} %{size_download} %{content_type}' 'https://www.obirin.ac.jp/academics/postgraduate/international_studies/course_humanities/u1ta3s000005vara-att/BC-2-1-5-2-4_02.pdf'  # rc=0; -w: 200 357913 application/pdf
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineA/caps/S796.bin -w '%{http_code} %{size_download} %{content_type}' 'http://www.kankyo-u.ac.jp/f/introduction/research/innovation/field/189.pdf'  # rc=0; -w: 200 108503 application/pdf
curl -sS -L --max-time 40 -o /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ExecQuarantineA/caps/S804.bin -w '%{http_code} %{size_download} %{content_type}' 'https://kotobank.jp/word/苗字-392782'  # rc=0; -w: 200 212285 text/html; charset=UTF-8
```

Supplementary extraction (`rc=0` each): `pdftotext -q caps/S786.bin -` → 42219 chars; `pdftotext -q caps/S795.bin -` → 19163 chars; `pdftotext -q caps/S796.bin -` → 12314 chars. sha256 per capture and per-fragment booleans (including the supplementary no-whitespace flag) are in `verdicts-A.json`.

## Tooling

- curl 8.23.0 (x86_64-pc-linux-gnu) libcurl/8.23.0 OpenSSL/3.6.5 zlib/1.3.2 brotli/1.2.0 zstd/1.5.7 libidn2/2.3.8 libpsl/0.21.5 libssh2/1.11.1 nghttp2/1.70.0 ngtcp2/1.25.0 nghttp3/1.18.0 mit-krb5/1.22.2 (system, preinstalled)
- Python 3.14.8 stdlib (html, unicodedata, hashlib) — no packages installed
- pdftotext version 26.10.0 (poppler, preinstalled) — used for PDF supplementary extraction only
- No installs this seat; pacman untouched (host-wide pause honored); no sysctls touched.
