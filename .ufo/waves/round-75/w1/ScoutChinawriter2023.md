# ScoutChinawriter2023 — re-open staged S870 (tentative lane S893)

## Verdict: ADMIT (proposed row; source is live and the cited passage locates)

The staged base entry's locator, 三九音域「世界观是打开小说幻想屋的钥匙」段, is present verbatim on the fetched page as the heading `世界观是打开小说幻想屋的钥匙`. The staged S870 anchor and its recheck phrase also locate. The round-72 refusal span from register S787, `作品中的人物名字和地名也一样…`, remains absent. This re-open validates the staged entry's cited passage, not that register span; the source/quote mismatch remains a fact about the old register record.

Flip to REFUSE if the ordinary live page no longer serves the located heading / evidence window, or the stored round evidence fails to reproduce the quote. UNVERIFIABLE only if ordinary access ceases to yield the document (e.g. challenge or non-200 with no accessible ordinary copy). No Wayback capture was found in the successful CDX probes; this does not prevent ADMIT because the live source returned the full article and the quote located.

## Fetch: exact command and raw output

Browser UA used:

`Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

Command (run from the assigned scratch directory):

```sh
UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36'
curl -sS -L -A "$UA" -D headers.txt -o page.html -w 'HTTP=%{http_code} bytes=%{size_download} url=%{url_effective}\n' 'https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html'
sha256sum page.html
```

Raw output:

```text
HTTP=200 bytes=45238 url=https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html
51251e22c617617af797d164684e8927dc792a06140ff35fbaebc158515415f0  page.html
```

`headers.txt` includes `HTTP/1.1 200 OK`, `Date: Tue, 27 Oct 2026 16:56:51 GMT`, `Content-Type: text/html`, `Content-Length: 45238`, `Server: RMW-WEB/260923`, `Last-Modified: Thu, 24 Oct 2024 01:57:00 GMT`. A plain-curl comparison also returned `plain-curl HTTP=200 bytes=45238`. The round-68 `quarantine-handcheck.json` record for S787 has the same 45238 bytes and sha256 prefix `51251e22c617617a`; its `found` is null for the register's unrelated-to-this-located-heading span.

The page identifies itself by `<title>` as `我是怎样创作网络小说的--网络文学--中国作家网`; `publishdate` is `2023-09-22`, `contentid` is `40083104`. The printed source line is `来源：文艺报`, with displayed date `2023年09月22日09:04`; the article is part of the “网络文学名家谈写作” feature. The located section is headed `世界观是打开小说幻想屋的钥匙`, followed by `□三九音域`.

## Located quote and counts

Recommended Gate quote: `世界观是打开小说幻想屋的钥匙` — 14 Unicode characters, 1 whitespace-delimited token. It occurs once verbatim in the fetched HTML and once after NFKC normalization plus whitespace folding. Locator: the 三九音域 section heading, HTML `<p>` element index 32 (zero-based; the 33rd non-empty `<p>` element).

Additional corroboration in the same section:

- Staged row anchor `我喜欢把写小说想象成邀请读者走进一个由我搭建的幻想屋` — 26 characters, 1 whitespace token, one hit; paragraph immediately after the `□三九音域` byline.
- `网络小说中的世界观，指的是故事设定中世间万物运转的方式` — 27 characters, one whitespace token, one hit; same paragraph. The staged row's exact recheck term `世间万物运转的方式` occurs once, and its command returned `1`.
- `世界观的创新本质上是构成小说世界的基本规则的创新` — 24 characters, one whitespace token, one hit; later in the same author's section.
- Old register span `作品中的人物名字和地名也一样` — zero hits in the page.

The quoted heading is short (14 chars) and directly matches the staged base entry's cited locator. Extracted visible paragraph text is 7891 characters, so any evidence file for the round's EVIDENCE leg should use an excerpt of at least 4096 characters around the heading, rather than labeling a short excerpt whole-document.

## PROPOSED lane registry row

Tier: **C**, kind **community**. This is a writer's practitioner explanation in a literary feature, suitable as native practitioner vocabulary / lead evidence; it is not peer-reviewed scholarship or factual authority. A community source is never tier A.

```text
| S893 | 三九音域, 「世界观是打开小说幻想屋的钥匙」 section in 网络文学名家谈写作, 中国作家网 reprint, source line 文艺报, 2023-09-22 — https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html | community | C | Practitioner vocabulary for Chinese web-fiction world-building; 世界观 as the operating rules of a fictional world, not a scholarly authority | 三九音域 section heading: 「世界观是打开小说幻想屋的钥匙」; following paragraph defines it as 故事设定中世间万物运转的方式 and 故事发生的场景、规则; fetched 2026-10-27 | The native practitioner framing of 世界观 as a fictional world's operating rules, rather than merely a list of setting elements | mined | 2026-10-27 | 180d | corpus/knowledge/myth-symbol/narrative-structure-frameworks.md |
```

This is a proposal, not a registry edit. The only staged knowledge file citing staged S870 is `myth-symbol/narrative-structure-frameworks.md`; the used-by path above is therefore the sole proposed admitted entry path for this row.

## Wayback CDX canonical-slug probe (QUALITY 21/24)

CDX requests used the same browser UA. Successful probes:

```text
http://web.archive.org/cdx/search/cdx?url=www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html&output=json&limit=20
-> []

https://web.archive.org/cdx/search/cdx?url=www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html&output=json&limit=20
-> []

https://web.archive.org/cdx/search/cdx?url=chinawriter.com.cn/n1/2023/0922/c404024-40083104.html&output=json&limit=5
-> []

https://web.archive.org/cdx/search/cdx?url=example.com&output=json&limit=2
-> [["urlkey","timestamp","original","mimetype","statuscode","digest","length"],
   ["com,example)/","20020120142510","http://example.com:80/","text/html","200","HT2DYGA5UKZCPBSFVCV3JOBXGW2G5UUA","1792"],
   ["com,example)/","20020328012821","http://www.example.com:80/","text/html","200","UY3I2DT2AMWAY6DECFCFYMT5ZOTFHUCH","481"]]

https://web.archive.org/cdx/search/cdx?url=www.chinawriter.com.cn/&output=json&limit=2
-> [["urlkey","timestamp","original","mimetype","statuscode","digest","length"],
   ["cn,com,chinawriter)/","20040321111222","http://www.chinawriter.com.cn:80/","text/html","200","UMG5C2AFVHLPHDDJGJAIRDJHQ6HI3XDZ","8877"],
   ["cn,com,chinawriter)/","20040401160922","http://www.chinawriter.com.cn:80/","text/html","200","VGJZLKHSIW5G74KIVPVPMJ3ZFIGS7Y24","8865"]]
```

Additional successful no-scheme slug probe (`https://web.archive.org/cdx/search/cdx?url=chinawriter.com.cn/n1/2023/0922/c404024-40083104.html&output=json&limit=5`) also returned `[]`. The positive controls establish that CDX answered and that the host is indexed. Initial subsequent `http://` CDX requests transiently failed to connect after the first empty result; retrying the slug and controls over HTTPS succeeded. No capture row exists for the canonical slug in these probes.

## Commands / scratch

Quote checks used literal fixed-string counts in the saved response (`grep -o -F <quote> page.html | wc -l`) and Python NFKC + whitespace-folded matching against extracted article paragraphs; counts are given above. No tools were installed. Scratch was confined to `/fast/scratch/hyaku/kotodama-r75/ScoutChinawriter2023/` and removed before handoff.
