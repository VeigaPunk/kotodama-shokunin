# ExecCaptureEvidence — round 76, wave 1 (claim C, evidence captures)

Seat: `ExecCaptureEvidence` (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`.
Base revision: `98c486bdb4650ba5b8e651d332910e8ee60ad121`. Access date: 2026-10-27.
Assignment: BUILD evidence captures for the five planned lane documents S894-S898, by ordinary means
only, in the round-75 grammar, choosing the located quote myself. No claim edits.

## Verdict

**BUILD DONE.** Five row captures written (S894, S895, S896, S897, S898) plus one auxiliary witness
for the S894 Wayback capture. All six re-verify with `--verify`: `VERIFY OK ... quote-in-window=yes`,
`http-status: 200`, `access-date: 2026-10-27`, `challenge: none`. One plan-relevant collision was
measured: **S897 (`showGb`) is not a second document — it 302-redirects to the S896 `newGbInfo` page,
and the extracted text of both is byte-identical (664 chars, sha256
`deefd5bb50d6f2a17a3efb8b486210d8a1bd811d7a1f3466ab9dfbcad928b3cf`).** See Risk R1.

## 1. Evidence table

`bytes:` and `sha256:` are the *fetched body* fields written into each file by the capture command in
§2; `quote-in-window` is the `--verify` verdict in §3. Every file binds the browser-shaped UA to the
response that request got in the same file (`ua:` + `http:` + `bytes:` + `sha256:` + `fetched:`).

| id | URL | HTTP | bytes | sha256 | quote (<=25 tokens, <=80 chars) | quote-in-window |
|---|---|---|---|---|---|---|
| S894 | https://www.digital.archives.go.jp/search | 200 | 311308 | `204b7188493573f85b0a7d394983ce90e1a1b1280786643de6c60fc50b763ea8` | `元号名称 開始西暦年 令和 2019 選択 平成 1989` | yes |
| S894 (aux) | https://web.archive.org/web/20260422145052id_/https://www.digital.archives.go.jp/search | 200 | 307700 | `c015e1dce915d4c9f3d3fa6d04e25605cc59547526284372de55112f268a13e0` | same quote | yes |
| S895 | https://www.xingzuobaike.com/huangli/wannianli/d165803.html | 200 | 33179 | `830495598c1f769095438473b8cfb7819d9906f730713a1ba95ac016d077735e` | `本标准主要技术内容包括两部分，编算部分规定了农历的编排规则、计算模型和精度以及农历的表示方法。` | yes |
| S896 | https://web.archive.org/web/20260424031027id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296 | 200 | 24174 | `f04feb475163287e85238628d5425846fde0118ce277daca7081c76058101e0e` | `标准号：GB/T 33661-2017 中文标准名称：农历的编算和颁行` | yes |
| S897 | https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296 | 200 (after 302) | 24144 | `80b4c781f4b772107427218dc0a3596842a66388a5c05635679787fe41530aa9` | `标准状态： 现行` | yes |
| S898 | https://news.gmw.cn/2017-05/23/content_24559485.htm | 200 | 25250 | `670850ea26dd6de7d480a80d95381d21107b9fbc3cd32414bd4a80123a2366f1` | `此次发布的《农历的编算和颁行》首次明确了农历的编排规则、计算模型和精度等，为农历日历编算提供了科学的规范依据。` | yes |

Sizes/shapes: S894 quote 7 tokens / 29 chars, visible 6815 chars, window `chars=4103` scope
`excerpt`; S894 aux quote 7/29, visible 6724, window 4103 `excerpt`; S895 quote 1 token / 47 chars,
visible 4165, window 4098 `excerpt`; S896 quote 3 tokens / 35 chars, visible 664, window 664
`whole-document`; S897 quote 2 tokens / 8 chars, visible 664, window 664 `whole-document`; S898 quote
1 token / 55 chars, visible 1487, window 1487 `whole-document`. Source of each number: the `quote-*`,
`visible-chars`, `window:` and `window-scope:` fields of the id's evidence file, written by §2's command.

Evidence-file digests (`sha256sum` over the staged files, §3 receipt):

```
ff311810628b9a33ee9a7150a8c4a6d31a86fa7affa4d76dd1457d209ab6c4a7  evidence/S894.txt
b144615fb453bc18f67778701f84eef957a86ed977aedf4f7966ddc6c10f93f4  evidence/S895.txt
7abec3e58745d5cdcd065c78a7a610673dd6abcd2215becc06a6ae279b13ef2a  evidence/S896.txt
d432f499598e90307d4acd97c1da256cdc7c40f94af1764f319f7c86459cde13  evidence/S897.txt
6a30f64306ba617aed222d0fe0042067877539f117103f1df7e0e00710369b87  evidence/S898.txt
bb2ef02512a2b8a85b52de5b0e71e5e5a0f9ef7e50c883db22743ae419eb6031  aux/S894-wayback.txt
```

## 2. Capture commands (raw stdout)

Pre-flight ordinary GETs (same browser-shaped UA, same scratch), raw `curl -w` lines:

```
s898 200 https://news.gmw.cn/2017-05/23/content_24559485.htm 8076 text/html
s896wb 200 https://web.archive.org/web/20260424031027id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296 8075 text/html;charset=utf-8
s894wb 200 https://web.archive.org/web/20260422145052id_/https://www.digital.archives.go.jp/search 34997 text/html;charset=UTF-8
s895 200 https://www.xingzuobaike.com/huangli/wannianli/d165803.html 9093 text/html; charset=utf-8
s897 200 https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296&refer=outter 7334 text/html;charset=utf-8
s894live 200 https://www.digital.archives.go.jp/search 311308 text/html;charset=UTF-8
```

(`size_download` is the wire size; `bytes:` is the decoded body length. The S897 row shows the final
URL after the 302 — see §4.1.)

The tool was run six times as
`TMPDIR="$S" python3 .ufo/waves/round-75/counters/capture-evidence.py --id <ID> --url <URL> --quote '<QUOTE>' --locator '<LOCATOR>' --ua 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' --out <STAGE>/.../<ID>.txt --access-date 2026-10-27`
with `$S=/fast/scratch/hyaku/kotodama-r76/ExecCaptureEvidence` and
`<STAGE>=/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-76/w1/stage/ExecCaptureEvidence`.
Raw stdout:

```
EVIDENCE S898: quote-found=yes verbatim=yes http=200 bytes=25250 sha256=670850ea26dd6de7 window-chars=1487 window-scope=whole-document window-sha256=3b0fc54b88339ebd -> .../evidence/S898.txt
VERIFY OK: .../evidence/S898.txt window-sha256=3b0fc54b88339ebd4f48ebb00230d9b33175e07eccdaa3edbeef1efbd2ab2be0 window-bytes=4005 window-chars=1487 quote-in-window=yes
[exit 0] S898
EVIDENCE S895: quote-found=yes verbatim=yes http=200 bytes=33179 sha256=830495598c1f7690 window-chars=4098 window-scope=excerpt window-sha256=3ae29936e95ecda1 -> .../evidence/S895.txt
VERIFY OK: .../evidence/S895.txt window-sha256=3ae29936e95ecda1f707435af2b6807c3eb8944ce63577057fd8874eea223008 window-bytes=10874 window-chars=4098 quote-in-window=yes
[exit 0] S895
EVIDENCE S897: quote-found=yes verbatim=no http=200 bytes=24144 sha256=80b4c781f4b77210 window-chars=664 window-scope=whole-document window-sha256=882d1f9a9eb38eef -> .../evidence/S897.txt
VERIFY OK: .../evidence/S897.txt window-sha256=882d1f9a9eb38eef75eefbc27258e6f863c87b3704eed435b91edcfc85808549 window-bytes=1445 window-chars=664 quote-in-window=yes
[exit 0] S897
EVIDENCE S894: quote-found=yes verbatim=no http=200 bytes=311308 sha256=204b7188493573f8 window-chars=4103 window-scope=excerpt window-sha256=86428e0ae827d76f -> .../evidence/S894.txt
VERIFY OK: .../evidence/S894.txt window-sha256=86428e0ae827d76ffb3481ebdd88cc84fe7579cc562da618b358000e05538dad window-bytes=9059 window-chars=4103 quote-in-window=yes
[exit 0] S894
EVIDENCE S896: quote-found=yes verbatim=no http=200 bytes=24174 sha256=f04feb475163287e window-chars=664 window-scope=whole-document window-sha256=882d1f9a9eb38eef -> .../evidence/S896.txt
VERIFY OK: .../evidence/S896.txt window-sha256=882d1f9a9eb38eef75eefbc27258e6f863c87b3704eed435b91edcfc85808549 window-bytes=1445 window-chars=664 quote-in-window=yes
[exit 0] S896
EVIDENCE S894wb: quote-found=yes verbatim=no http=200 bytes=307700 sha256=c015e1dce915d4c9 window-chars=4103 window-scope=excerpt window-sha256=9c18391cd861e9dd -> .../aux/S894-wayback.txt
VERIFY OK: .../aux/S894-wayback.txt window-sha256=9c18391cd861e9ddd64af178f9ae858be1c9e1eb62beed2ccaa5b5c7040af8ba window-bytes=9061 window-chars=4103 quote-in-window=yes
[exit 0] S894wb
```

No `[exit != 0]` line occurred (the wrapper echoed `[exit $?]` after each run). The pre-flight body
hashes matched the tool's independently re-fetched `sha256:` exactly for all six URLs — see
`stage/ExecCaptureEvidence/receipts/preflight-body-sha256.txt`; e.g. S894 pre-flight body
`204b7188493573f85b0a7d394983ce90e1a1b1280786643de6c60fc50b763ea8` equals the `sha256:` field of
`evidence/S894.txt`.

## 3. Verification (raw)

```
VERIFY OK: .../evidence/S894.txt window-sha256=86428e0ae827d76ffb3481ebdd88cc84fe7579cc562da618b358000e05538dad window-bytes=9059 window-chars=4103 quote-in-window=yes access-date=2026-10-27 http-status=200
VERIFY OK: .../evidence/S895.txt window-sha256=3ae29936e95ecda1f707435af2b6807c3eb8944ce63577057fd8874eea223008 window-bytes=10874 window-chars=4098 quote-in-window=yes access-date=2026-10-27 http-status=200
VERIFY OK: .../evidence/S896.txt window-sha256=882d1f9a9eb38eef75eefbc27258e6f863c87b3704eed435b91edcfc85808549 window-bytes=1445 window-chars=664 quote-in-window=yes access-date=2026-10-27 http-status=200
VERIFY OK: .../evidence/S897.txt window-sha256=882d1f9a9eb38eef75eefbc27258e6f863c87b3704eed435b91edcfc85808549 window-bytes=1445 window-chars=664 quote-in-window=yes access-date=2026-10-27 http-status=200
VERIFY OK: .../evidence/S898.txt window-sha256=3b0fc54b88339ebd4f48ebb00230d9b33175e07eccdaa3edbeef1efbd2ab2be0 window-bytes=4005 window-chars=1487 quote-in-window=yes access-date=2026-10-27 http-status=200
VERIFY OK: .../aux/S894-wayback.txt window-sha256=9c18391cd861e9ddd64af178f9ae858be1c9e1eb62beed2ccaa5b5c7040af8ba window-bytes=9061 window-chars=4103 quote-in-window=yes access-date=2026-10-27 http-status=200
```

Identical `window-sha256` for S896 and S897 (`882d1f9a9eb38eef75eefbc27258e6f863c87b3704eed435b91edcfc85808549`,
`window-bytes=1445`) is the folding-level statement of R1: the two captures store the same text.

## 4. What each document carries, and document-level findings

### 4.1 S896 vs S897 — one document, not two (material to the claim's `k`)

Raw response chain for the S897 request (`receipts/s897.headers.txt`; session-cookie values removed):

```
HTTP/1.1 302 
Date: Tue, 27 Oct 2026 21:34:00 GMT
Location: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296&refer=outter
Content-Language: en-US
HTTP/1.1 200 
Date: Tue, 27 Oct 2026 21:34:00 GMT
Content-Type: text/html;charset=utf-8
Content-Language: zh
```

`final-url:` in `evidence/S897.txt` is
`https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296&refer=outter`.
Extracted visible text of the S896 Wayback capture and of the S897 final body:

```
deefd5bb50d6f2a17a3efb8b486210d8a1bd811d7a1f3466ab9dfbcad928b3cf  openstd-newGbInfo-wayback-text.txt
deefd5bb50d6f2a17a3efb8b486210d8a1bd811d7a1f3466ab9dfbcad928b3cf  openstd-showGb-final-text.txt
cmp exit=0
 664 openstd-newGbInfo-wayback-text.txt
 664 openstd-showGb-final-text.txt
```

(`receipts/openstd-s896-s897-identity.txt`; both texts also copied beside it.) The body bytes differ
(24174 vs 24144) but only by the `refer=outter` parameter and Wayback framing; the extractable text is
identical. `showGb` served no standard text on this plain GET: the metadata page itself carries the
notice `当前浏览器暂不支持标准全文在线预览服务` (visible in the stored window). So S897 satisfies the
planned anchor (the 标准状态 field row) but **does not add a distinct document**, and it is not the
standard's 编排规则 text — that clause is only in the S895 reproduction.

### 4.2 S894 — era-name table, two witnesses

Live page and the 2026-04-22 Wayback capture both contain the 元号選択 table. Raw era block (identical
for the first 30 lines in both):

```
元号名称
開始西暦年
令和
2019
選択
平成
1989
選択
昭和
1926
選択
大正
```

Quoted span is the header plus the two requested rows. The two witnesses are not byte-identical pages
(the live page differs in institution lists and 請求番号 examples; live text 6815 chars vs Wayback
6724), but the era block is unchanged. Primary row evidence is the live page (`evidence/S894.txt`);
`aux/S894-wayback.txt` is the second witness if the L1 wants the frozen capture to be the stable one.

### 4.3 S895 — tier-C reproduction of GB/T 33661

Title on the page: `国家标准《农历的编算和颁行》GB/T 33661-2017 原文及解读材料`. The quoted span is
the opening sentence of `标准主要内容` and carries the 编排规则 + 计算模型/精度 claim. Page self-identifies
its source as `https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296`
(note the `/bzgk/gb/` path, whereas the live registry path in S896/S897 is `/bzgk/std/`). This is a
reproduction page, consistent with the draft's "S916 (tier C reproduction page)" note; it cannot be the
sole support of an admitted entry under the claim's own rule.

### 4.4 S898 — gmw.cn report

The quote is the report's technical-content sentence (编排规则、计算模型和精度; "为农历日历编算提供了
科学的规范依据"). Visible text 1487 chars, hence `whole-document` window.

### 4.5 Quote provenance

Each quote is the span I located in the extracted page text myself; `--locator` records where it sits.
`quote-found-verbatim: no` for S894/S896/S897 is expected and benign: those spans cross block
boundaries (newlines in the extracted text), so the exact-string test fails while the tool's
NFKC + whitespace-fold `quote-found: yes` succeeds. The round-75 grammar carries both fields and
`--verify` grades `quote-in-window` on the folded window; all six are `yes`.

## 5. Access control / QUALITY 10 and 22

- All six fetches are ordinary GETs with the browser-shaped UA
  `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`.
- Every response was `http: 200` (`http-status: 200` after `--verify`); `challenge: none` and
  `challenge-detail: (none)` in all six files. No captcha, login wall, consent wall or geo-block was
  met, and none was bypassed.
- The S897 302 is ordinary application routing to a metadata page (it hands out a session cookie and
  redirects the un-sessioned request); it is not an access control. No JS challenge was solved.
- UA-to-response binding: each evidence file carries `ua:` + `http:` + `bytes:` + `sha256:` +
  `fetched:` for that one request; the pre-flight table above used the same UA.
- Session material: `Set-Cookie` values appeared in the raw headers. They were never used and were
  removed from the copied receipts (`receipts/*.headers.txt` keeps only HTTP status, `Location`,
  `Content-Type`, `Date`/`memento`/`content-language`; grep for `JSESSIONID`/`^set-cookie` now finds
  nothing but the redaction note). Cookie values are not reproduced in this report.

## 6. Tooling and scratch

- Tool used: `kotodama-shokunin/.ufo/waves/round-75/counters/capture-evidence.py` (read-only use; not
  edited). No packages installed or upgraded.
- `TMPDIR` is honoured: the tool's internal `tempfile.mkdtemp(prefix="capture-evidence-")` (line 929)
  resolved under the scratch dir — `TMPDIR=$S python3 -c 'import tempfile; print(tempfile.gettempdir())'`
  printed `/fast/scratch/hyaku/kotodama-r76/ExecCaptureEvidence`; `ls -d /tmp/capture-evidence-*`
  printed `none`. The tool has no `--work` flag (its only scratch knob is `TMPDIR`).
- Scratch root `/fast/scratch/hyaku/kotodama-r76/ExecCaptureEvidence` was created for pre-flight bodies;
  receipts were copied into the stage dir and the scratch dir was deleted before this seat returned.
- The tool hardcodes `ROUND = 75`, so every file's comment line reads
  `# evidence <id> — claim C GATE (round 75)`. That is the grammar the ticket asked for; if the
  round-76 counter greps for `round 76` in that comment it must tolerate this (see Risk R5).

## 7. Files written (all under the wave dir; nothing else changed)

```
.ufo/waves/round-76/w1/ExecCaptureEvidence.md                                  (this report)
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/evidence/S894.txt
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/evidence/S895.txt
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/evidence/S896.txt
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/evidence/S897.txt
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/evidence/S898.txt
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/aux/S894-wayback.txt
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/receipts/s894live.headers.txt
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/receipts/s894wayback.headers.txt
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/receipts/s895.headers.txt
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/receipts/s896wayback.headers.txt
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/receipts/s897.headers.txt
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/receipts/s898.headers.txt
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/receipts/preflight-body-sha256.txt
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/receipts/openstd-s896-s897-identity.txt
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/receipts/openstd-newGbInfo-wayback-text.txt
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/receipts/openstd-showGb-final-text.txt
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/receipts/evidence-sha256-verify.txt
.ufo/waves/round-76/w1/stage/ExecCaptureEvidence/SHA256SUMS.txt
```

No lane tracked file, no fleet file, no `.ufo/state`, no `reports/round-76/**`, no LOG/SCORECARD/SKILL/
SHONEN and no corpus file was written. No commit was made (the L1 commits).

## 8. Risks / blockers for the L1

- **R1 (claim-shaping, measured): S896 and S897 are one document.** `showGb` 302s to `newGbInfo`; the
  two evidence windows hash identically (`882d1f9a…`, 1445 bytes, 664 chars) and the extracted texts
  are byte-identical (cmp exit 0). If the frozen `row_set` keeps both S896 and S897, the declared
  "one row per document" and `k = number of distinct documents` are contradicted. Either merge the
  two campaign ids onto one row, or make S897 name a genuinely distinct reachable document. The
  metadata page itself is opened and its fields quoted, so the planned anchor is satisfiable from
  either row alone.
- **R2: S897's intended subject (the standard's online full text) is not reachable by plain GET.**
  The endpoint redirects to metadata; the metadata page's own text says the browser cannot run the
  online-preview service. No access control was met or bypassed; I did not pursue alternate
  preview endpoints (out of this assignment). If the claim expected 编排规则 text from S897, that
  expectation fails; the 编排规则 quote is held by S895 (tier C).
- **R3: S895 is tier C (reproduction).** The claim's "no tier-C row is the sole support of an admitted
  entry" therefore constrains whatever entry cites S895.
- **R4: `quote-found-verbatim: no` on S894/S896/S897** is a newline-fold artifact, not a missing quote:
  `quote-found: yes` and `quote-in-window=yes` on the folded window. If the round-76 counter requires
  `quote-found-verbatim: yes`, these three files would fail; that requirement would also reject any
  multi-line quote and is stricter than the round-75 `--verify`, which grades the folded window. Flag
  so the L1 can either accept the folded form or ask for single-line quotes (single-line alternatives
  exist for S896 `标准号：GB/T 33661-2017` and S897 `现行`, but no single line carries the 令和/2019 +
  平成/1989 mapping for S894).
- **R5: tool comment says `round 75`.** Hardcoded `ROUND = 75`; the grammar requested this tool, so the
  files are correct as artefacts, but any round-76 header grep must tolerate it (or copy the tool and
  set `ROUND`).
- **R6: S894's live page is not byte-stable** with its April capture (institution lists differ; 6815 vs
  6724 visible chars), while the era block is identical. The row's quote is present in both; the aux
  witness is available if a frozen capture is preferred.

## 9. Not run (unrun checks, stated as unrun)

- No counter (`accept-c.py` or any round-76 counter) was run: the evidence is staged, uncommitted, and
  the round-76 counters/paths are the L1's to install at the freeze.
- No census, no gate/junk fixtures, no repository verification; editing-wave rule and leaf scope.
- No attempt was made to reach the standard's online-preview full text beyond the ordinary `showGb`
  GET recorded above; no alternate endpoint was probed.
