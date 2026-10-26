# ScoutUcass — S864 UCASS narratology syllabus re-open

## Verdict: ADMIT

The live PDF was retrievable directly by ordinary HTTPS request and is a valid five-page PDF. `pdftotext` preserved the Chinese text. The staged anchor and all four listed syllabus claims locate in the document. The source supports what this course syllabus says and schedules; it is not evidence for the full details or validity of the theories it names, nor for the Japanese-theory claims in the folded entry. No Wayback capture was found for the PDF URL, but this does not defeat the directly opened source.

**Flip condition:** refuse/reopen the row if a later ordinary fetch no longer yields this syllabus or the quoted line cannot be located. A Wayback capture appearing would improve preservation but is not required for this admission.

## Fetch and extraction evidence

Scratch: `/fast/scratch/hyaku/kotodama-r75/ScoutUcass/` (removed before yield). No tool was installed; `/usr/bin/pdftotext` and `curl` were already available.

Exact fetch command:

```sh
cd /fast/scratch/hyaku/kotodama-r75/ScoutUcass && UA='Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36' && echo "UA: $UA" && curl -sS -A "$UA" -o xushixue.pdf -w 'HTTP:%{http_code} SIZE:%{size_download} TYPE:%{content_type} URL:%{url_effective}\n' 'https://jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf' && ls -l xushixue.pdf && file xushixue.pdf && sha256sum xushixue.pdf
```

Raw output:

```text
UA: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36
HTTP:200 SIZE:225123 TYPE:application/pdf URL:https://jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf
-rw-r--r-- 1 vgpnk vgpnk 225123 Oct 27 13:55 xushixue.pdf
xushixue.pdf: PDF document, version 1.7, 5 page(s)
62a13e92e23d764c88d1e58f64cde00eb90a6aee900d52fa431bde9ca89334d1  xushixue.pdf
```

A browser-UA HEAD-style redirect check gave `final_url:https://jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf http:200 redirects:0`. A byte-range request to the same URL returned `HTTP:206 SIZE:2048 TYPE:application/pdf`. No challenge or access-control page was encountered.

Exact extraction command:

```sh
cd /fast/scratch/hyaku/kotodama-r75/ScoutUcass && pdftotext -layout xushixue.pdf xushixue.txt && wc -c xushixue.txt && wc -l xushixue.txt
```

Raw output: `14726 xushixue.txt` and `254 xushixue.txt` (14,726 bytes; 254 lines). A per-page extraction found the quote on PDF page 3, at `page3.txt:41`. The extracted whole-text file had 10,368 Unicode characters. The PDF SHA-256 is `62a13e92e23d764c88d1e58f64cde00eb90a6aee900d52fa431bde9ca89334d1`; extracted text SHA-256 is `0e7711543f3e7a3867a6264e0ceed121c345b2fc254936d7b7666b53ff124d1e`.

Located gate quote (verbatim): **“一、故事是一种深层的抽象结构，必须通过话语呈现。”** Location: PDF p. 3, `第二讲 故事：事件（一）`, point 一 (`pdftotext -layout`, page3.txt line 41). Count: **24 Unicode characters, 1 whitespace-delimited token**. NFKC-normalizing both the quote and extracted text, then folding whitespace, still locates the quote. (`pdftotext` retains the Chinese punctuation; NFKC maps the fullwidth comma to ASCII comma in both.)

## Claim checks and located replacements

| Staged claim | Observation | Suggested precise wording |
|---|---|---|
| Section 2 `故事：事件（一）` point 1 | Verified on PDF p. 3: `一、故事是一种深层的抽象结构，必须通过话语呈现。` | Cite the p. 3 point-1 sentence as the Chinese source's explicit story/discourse framing. |
| Actantial model, `行动元` / Greimas | Verified on p. 3 under `第三讲 行动元与人物`: `格雷马斯的“行动元”`; the preceding lecture also lists `格雷马斯、普洛普、布雷蒙德的故事结构分析`. | Say the syllabus schedules Greimas's “行动元” under its lecture on actants and characters; do not imply this syllabus explains the model in detail. |
| Three time axes | Verified on p. 3: `考察时间的三个维度：次序、时长和频率。` The schedule separately lists order (回叙、预叙), duration, and frequency. | Prefer “three time dimensions (次序、时长、频率)” over “axes,” which is not the source's term. |
| Chatman's participant grid | Verified on p. 3 under `第七讲 叙述层次与声音`: `查特曼的六种参与者`. | Prefer “Chatman's six participants, as the syllabus labels them”; “grid” is an interpretive gloss and this syllabus does not enumerate the six. |
| Anchor `第二讲 故事：事件（一） 第 1 点` | Verified: point 一 follows the lecture heading and is the quoted sentence above. | Retain the anchor and include the verbatim point-1 quote in the registry anchor cell. |

The course description also names Propp, Greimas, Barthes, Genette, Chatman and Rimmon-Kenan among the structuralist narratology theorists; p. 3's listed content directly corroborates the narrower claims above. The syllabus does not substantiate the entry's Japanese sources or the full theoretical content of the named models.

## Proposed lane registry row

Tier **A**, scoped narrowly to the published syllabus's declared course coverage: the university-hosted course syllabus is primary evidence for what that syllabus lists. This is not an A-tier claim about narratology theory itself; the row's `scope` and `teaches` cells explicitly limit it. This is not a community source (community is never A). If the scope were substantive theoretical claims rather than syllabus contents, B or additional primary scholarship would be appropriate.

```text
| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |
|---|---|---|---|---|---|---|---|---|---|---|
| S888 | 中国社会科学院大学《叙事学》课程大纲 — https://jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf | docs | A | the published syllabus's declared Chinese narratology course coverage, not the underlying theories' full content | p. 3, 第二讲 故事：事件（一） point 1: “一、故事是一种深层的抽象结构，必须通过话语呈现。” | the syllabus frames story as a deep abstract structure presented through discourse; its schedule lists Greimas's “行动元”, three time dimensions 次序、时长、频率, and Chatman's six participants | mined | 2026-10-27 | 180d | corpus/knowledge/myth-symbol/narrative-structure-frameworks.md |
```

The row has 11 cells and no pipe character inside any cell. The proposed `used-by` is the folded narrative-structure-frameworks entry that cites staged S864; add any other path only if its admitted entry actually contains a source line citing S888.

## Wayback CDX canonical-slug probe (QUALITY 21/24)

The live URL resolved directly, with zero redirects, so it is itself the canonical target; there was no distinct redirect target to probe. HTTP port 80 could not connect (`curl: (7) Failed to connect to web.archive.org:80`), so probes were made over HTTPS. The exact-query positive controls below used the same `url=…&output=json` query shape.

Probed URL and exact query:

```text
https://web.archive.org/cdx/search/cdx?url=jw.ucass.edu.cn/kcdg/zyk/xwcb/xushixue.pdf&output=json
```

Raw response: `[]` (no exact-slug capture). A broader parent-path prefix probe, `https://web.archive.org/cdx/search/cdx?url=jw.ucass.edu.cn/kcdg/*&output=json&matchType=prefix&limit=20`, also returned `[]`; this is supplementary, not a substitute for the exact query.

Positive control 1, exact query:

```text
https://web.archive.org/cdx/search/cdx?url=persee.fr/doc/comm_0588-8018_1966_num_8_1_1113&output=json
```

The response began with the CDX header and multiple captures, including this raw status-200 record:

```text
["urlkey","timestamp","original","mimetype","statuscode","digest","length"],
["fr,persee)/doc/comm_0588-8018_1966_num_8_1_1113","20170301225114","http://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113","text/html","200","VL44NXFEOCPALP7EWASI5JMZQKMLDBWZ","14804"]
```

Positive control 2, same exact query shape against a PDF URL:

```text
https://web.archive.org/cdx/search/cdx?url=jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf&output=json
```

Raw response included status-200 captures, e.g.:

```text
["jp,go,jst,jstage)/article/jcss/25/2/25_200/_pdf","20201212045824","https://www.jstage.jst.go.jp/article/jcss/25/2/25_200/_pdf","application/pdf","200","W2T7YMAP64LUDKUXLUSRVU64V3H5UWBP","1072509"]
```

The positive controls establish that the HTTPS CDX endpoint and query shape return captures; they do not convert the UCASS result into an archive hit. No Wayback capture was found for the probed UCASS URL.
