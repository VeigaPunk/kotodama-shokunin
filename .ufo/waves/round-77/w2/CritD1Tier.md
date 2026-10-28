# CritD1Tier — wave-2 falsification of S897 (document D1) source scope/tier and claims

Seat: CritD1Tier. Target: S897 = 魏斌〈單名與雙名：漢晉南方人名的變遷及其意義〉, the row drafted
in `w1/stage/ExecCensusEnd/rows-897-898.md` and the claims pinned on it by CLAIMS-DRAFT.md D1 and by
the adopted staged entry `naming-systems.amend-2026-10-23.md`. All lane reads at base
`211f9526800906e0c585d878d265c37e5e090c15`; all probes re-run fresh in my own scratch
(`/fast/scratch/hyaku/kotodama-r77/CritD1Tier`, deleted after write-up).

## Live/capture probe — re-executed, byte-identical to W1

```
$ curl -sS -o d1-plain.body -D d1-plain.hdr -w 'plain http=%{http_code} bytes=%{size_download} type=%{content_type}\n' --max-time 45 'http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml'
plain http=403 bytes=162 type=text/html
$ curl -sS -o d1-browser.body -D d1-browser.hdr -w 'browser http=%{http_code} bytes=%{size_download} type=%{content_type}\n' --max-time 45 -A 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36' 'http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml'
browser http=200 bytes=143252 type=text/html

$ sha256sum d1-browser.body d1-plain.body
f14f7a5c03cb187f50870a8702a88505da0aea58427a829ea197e66909a11d5c  d1-browser.body   (== w1/stage/ScoutCDXPositive/d1-live-browser.body)
1d08335e65da7cf40d1c4a7ba0088e0f39b9c5a4b2e42de95fc9ffa69fb96c7a  d1-plain.body     (== w1/stage/ScoutCDXPositive/d1-live-plain.body)

$ curl -sS -o d1-wayback.html -w 'wayback http=%{http_code} bytes=%{size_download}\n' --max-time 60 'https://web.archive.org/web/20240111092427id_/http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml'
wayback http=200 bytes=143457
$ sha256sum d1-wayback.html
68c6ed377334199f5372fff16192be71a46e5ffbb6eee71611c3535bae42bf35  (== ScoutDocS897 wayback-sha256)
```

403 body verbatim: `<html><head><title>403 Forbidden</title></head><body bgcolor="white"><center><h1>403 Forbidden</h1></center><hr><center>nginx</center></body></html>` — 162 bytes, `Set-Cookie: SF_cookie_1=…` present on the blocked response too. So the DRAFT statement "plain UA 403/162, browser UA 200/143252; do not claim both UAs were blocked" is TRUE as of 2026-10-28T02:17Z.

## F1 — DEFECT (fixable): the staged S897 row asserts false provenance — "live answered HTTP 403 to both" — and hides the original venue

`w1/stage/ExecCensusEnd/rows-897-898.md` S897 row states:

> live answered HTTP 403 to both the plain and the browser-shaped request on 2026-10-27 (wall met, not passed)

That is the stale L1-probe premise (w1/spec.json ScoutDocS897 prompt asserted the same), disproven
three independent times (ScoutCDXPositive, SentinelSources s897-live-probe, ScribeEntryA fetch-log,
and my re-probe above). The row also says `kind = paper`, `tier = A`, and its source cell names only
"中国社会科学院历史研究所 site (lishisuo.cssn.cn), posted 2021-03-16".

What the page actually is: a second-hand repost. Footer of both live and capture bytes:

```
$ grep -o '來源：《歷史研究》[^<]*' d1-wayback.html d1-browser.body
d1-wayback.html:來源：《歷史研究》2012年第1期  → "來源：《歷史研究》" then line "2012年第1期"
d1-browser.body:來源：《歷史研究》 …same…
…版权所有： 中国社会科学院古代史研究所 … 欢迎转载，敬请注明：转载自 中国古代学术网
```

The article was published in 《歷史研究》 (Historical Research) 2012 no. 1; the cssn page is a
2021-03-16 repost (page meta `publishdate=2021-03-16`, `author=庄小霞` — a website editor, NOT 魏斌;
`source` meta EMPTY; body shows `发布日期：2021-03-16 原文刊于：` with the venue field blank).
Citation that omits "原載《歷史研究》2012年第1期" mis-dates the scholarship by 9 years and
mis-attributes provenance. The draft row's own sentence "live answered HTTP 403 to both" is
directly falsified above; if the frozen Gate/row repeats it, the located source is declared
unreachable when it is not — a provenance lie, and it contradicts CLAIMS-DRAFT.md's own
"Do not claim both UAs were blocked. Lane's browser-UA live copy is the located source."

## F2 — overclaim (scope): "a habit formed under contact" is the staged entry's gloss, not S897's claim

Staged entry `naming-systems.amend-2026-10-23.md` topic cell: "a Chinese naming system is a *late
cultural acquisition* — 名 precedes 姓, and their combination is a habit formed under contact, not a
natural given." The article's lead says only:

> 名的使用要早于姓，兩者組合是一種後起的文化習慣。… 具體到古代中國而言，春秋戰國以降中原地區逐漸形成穩定的華夏式姓名習慣，即「姓（氏）＋名」。

"後起" = later-arising; the text locates the 姓+名 combination's formation *inside* the Central
Plains 華夏 tradition from 春秋戰國 onward — endogenous development, not formation "under contact".
Contact (文化接觸) is the mechanism by which southern peoples *adopted* the already-formed pattern
("南方地區華夏式姓名的使用是文化接觸的結果", section 二 opening). The staged topic conflates
origin-of-pattern with spread-of-pattern. CLAIMS-DRAFT.md is narrower ("姓+名 a contact-era
acquisition" scoped to the southern system) and defensible; the staged sentence is not and must not
survive the re-grounded rewrite, or the entry teaches a mechanism the source does not state.

## F3 — supported: the three substantive claims DO check out verbatim

Verified by `grep -c -F` = 1 each in the W1 extracted text and my live body:

| claim | article text (verbatim) |
|---|---|
| 名 predates 姓; 姓+名 combination late-arising | 名的使用要早于姓，兩者組合是一種後起的文化習慣 (lead ¶2, after fn[5], before fn[6]) |
| historical pairing 姓（氏）+名 stable from 春秋戰國 | 春秋戰國以降中原地區逐漸形成穩定的華夏式姓名習慣，即「姓（氏）＋名」 |
| contact spread into the south | 南方地區華夏式姓名的使用是文化接觸的結果； conclusion: 上層人群在與華夏國家的接觸中，較早的模仿或被賜予華夏式人名；下層人群華夏式人名的大規模實現，則與編戶化過程密切相關 |

Caveat for the rewrite: the article's own conclusion is *stratified* — elite adoption via contact
vs. mass adoption via 編戶化 (household registration). "Contact spread" alone flattens a two-channel
argument; a faithful line keeps both channels. Also note the staged row's stored locator "引言"
names a section that does not exist — the page has no literal 引言 heading; the anchor is the
unnumbered lead (paragraphs 2–4 before heading 一、單名與雙名), as ScoutDocS897 already recorded.

## F4 — tier A is DEFENSIBLE, but only under corrected provenance

Registry rule (SOURCES.md): A = "primary or authoritative for that scope (… original paper …)".
The scope cell is "the single-name to double-name shift in Han-Jin southern Chinese personal naming
and what it implies about the 姓/名 sequence as a system-level structure" — i.e., the claims of a
specific paper. The repost page carries that paper's full text verbatim (body identical across live
and capture; all 11 S897 spans located once each). Under QUALITY.md criterion 6 — publisher
descriptions B, original paper A — a faithfully reposted full text of the original journal article
can serve as "original paper" for this scope; precedent rows (e.g., S037 full web text, tier A)
agree. The w1/spec hypothesis "tier B (academic institution portal)" treats the *page* as the
source; but the document is the journal paper — the page is merely its host. Tier A stands IF the
row cites the true venue 《歷史研究》2012(1) and treats 2021-03-16 as repost date; tier B would be
required only if the row claimed the cssn page itself as primary provenance. Smallest safe
correction: keep tier A, fix the source cell and the false 403-to-both sentence.

## F5 — ground claim confirmed (no duplicate authority)

`git grep -l -E 'lishisuo\.cssn\.cn|onomastica\.ijppan' 211f9526:corpus/knowledge` → exit 1, nothing.
Base SOURCES.md has no row for 魏斌/單名/歷史研究/cssn (only `onomasticafelecan.ro`, a different
domain — S543). Base `naming-systems.md` covers Chinese taboo (bìhuì), slot order and generation
pools ("hereditary surname ~ancient"), but no system-level 名-predates-姓 or contact-spread
account. The negative-sweep ground holds.

## Impacted axes and smallest safe correction

- ROWS/EVIDENCE/GATE legs at risk only if the staged row text lands verbatim: the "403 to both"
  sentence is false and the venue is under-cited. Correction: rewrite the S897 row source cell as
  "魏斌〈單名與雙名：漢晉南方人名的變遷及其意義〉, 原載《歷史研究》2012年第1期; reposted
  中国社会科学院历史研究所 (lishisuo.cssn.cn) 2021-03-16 (page meta author 庄小霞 is the site
  editor)", status cell "live 403 plain-UA / 200 browser-UA 2026-10-27", and Gate quote = the
  23-char anchor (verified verbatim in live+capture).
- Claim C text: keep the DRAFT scope; do NOT re-import the staged phrase "habit formed under
  contact" — replace with "later-arising (後起) within the 華夏 姓（氏）+名 pattern; southern
  adoption a product of cultural contact (上層 via contact/bestowal, 下層 via 編戶化)".
- Verdict: S897's source scope is real and the three pinned claims are verbatim-supported; the
  attack finds two fixable defects (false both-403 provenance + missing original venue) and one
  overclaim in the staged entry text (contact-formed vs. 後起+contact-spread). No defect forces the
  canonical judge to reject tier A or the document itself; reject only if the frozen row repeats
  the both-403 sentence or omits the 《歷史研究》 venue.
