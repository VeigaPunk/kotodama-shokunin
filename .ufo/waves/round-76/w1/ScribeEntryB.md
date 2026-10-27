# ScribeEntryB — round 76, wave 1: candidate b (calendar-festival-systems amend r10)

Seat: ScribeEntryB (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base
`98c486bdb4650ba5b8e651d332910e8ee60ad121`. Campaign id S938 is not cited anywhere; the draft cites **S897** only.

## Verdict

**Candidate b: ADMIT, reduced and corrected** — the staged "Proposed body" is not usable as written (its central
measurement does not reproduce and one inference is refuted), but what the page itself carries is enough for a
short, decision-usable amendment. Draft written; gate notes written; evidence windows copied. No captcha was
solved, no page image downloaded, no clause text read. Scratch deleted.

One claim-level finding for the L1 outside the entry: **Claim C's declared before-state is false at base**
(§Findings F5). The counter leg that tests it will fail if it asserts the draft's "prints nothing".

## Deliverables

| path (lane-relative) | what |
|---|---|
| `.ufo/waves/round-76/w1/drafts/corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24-r10.md` | the lane-form draft (body 1,345 words; provenance trio first; S897 only) |
| `.ufo/waves/round-76/w1/stage/ScribeEntryB/gate-notes.md` | per-route gate records: URL, access date 2026-10-27, ≤25-word located quote, status/bytes/UA, ADMIT/REFUSE + flip |
| `.ufo/waves/round-76/w1/stage/ScribeEntryB/evidence/S897-catalogue.html` | F3 response body, 24,144 B |
| `.ufo/waves/round-76/w1/stage/ScribeEntryB/evidence/S897-viewer-zh.html` | F6 body, 89,039 B |
| `.ufo/waves/round-76/w1/stage/ScribeEntryB/evidence/S897-viewer-en.html` | F7 body, 89,002 B |
| `.ufo/waves/round-76/w1/stage/ScribeEntryB/evidence/S897-download-zh.html` | F8 body, 7,606 B |
| `.ufo/waves/round-76/w1/stage/ScribeEntryB/evidence/S897-f{1,6,8}-headers.txt` | raw response headers for the three routes |

## Gates

### G1 — cited-lines lint (required, pasted verbatim)

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B tools/check-cited-lines.py \
    .ufo/waves/round-76/w1/drafts/corpus/knowledge/culture-material/calendar-festival-systems.amend-2026-10-24-r10.md
CITED-LINES: 0 finding(s) in 1 file(s)
exit=0
```
S-id inventory on the draft: `16 S897` (grep output: `     16 S897`); no other id occurs, no campaign id.

### G2 — couples exist at base

```
$ git -C ... cat-file -e 98c486b:<path> && echo OK
OK corpus/knowledge/culture-material/calendar-festival-systems.md
OK corpus/knowledge/culture-material/timekeeping-instruments.md
OK corpus/knowledge/culture-material/era-periodization-models.md
OK corpus/knowledge/culture-material/worldbuilding-setting-practice.md
```
(The fourth is the house-shape file, checked as a model, not cited.)

### G3 — ground at base (corrected twice; see F5)

```
$ git -C ... grep -l -E 'GB/T 33661' 98c486b -- corpus/knowledge
(no output) exit=1
$ git show 98c486b:corpus/SOURCES.md | grep -c '33661'
0
$ git show 98c486b:corpus/SOURCES.md | grep -c openstd
0
$ git grep -l -E 'GB/T 33661' 98c486b -- corpus/lessons
98c486b:corpus/lessons/round-68.md
98c486b:corpus/lessons/round-69.md
```
The entry's `ground:` line states exactly this: no knowledge file, no registry row, two lesson-file mentions.

### G4 — fetches (browser-shaped UA bound to each response; QUALITY 22)

UA = `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`.

```
F1 GET showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296   (no Referer, no cookie)
   → HTTP/1.1 302, Location: https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296&refer=outter
F2 same with type=download                                        → 302, same Location
F3 GET the Location target (curl -L)                              → 200, 24,144 B, sha256 80b4c781…aa9, md5 e866bfd6…f89
F4 F3 repeated                                                    → cmp: IDENTICAL
F5 F3 with Accept-Language: zh-CN,zh;q=0.9                         → 24,144 B, identical bytes
F6 GET showGb?type=online&…&request_locale=zh  + Referer catalogue → 200, 89,039 B, sha256 f32c3f47…ecb9
F7 GET showGb?type=online&… (no locale)        + Referer catalogue → 200, 89,002 B, sha256 f15dedfc…c0b7
F8 GET showGb?type=download&…&request_locale=zh + Referer catalogue → 200,  7,606 B, sha256 124ebe19…3d99
F10 F6 repeated with a JSESSIONID jar                             → 200, 89,039 B, differs from F6 in exactly one line
```

F10 diff (`diff <(tr -d '\r' < r2-online.html) <(tr -d '\r' < f-online-zh.html)`):

```
1523c1523
<            var data = {'hcno':'4BDA8B272E81D392AB7BE9AFB22707CC','time':totalTime,'rate':rate};
---
>            var data = {'hcno':'8CF29BDF27DDD7A6AB802129A6B2AE1E','time':totalTime,'rate':rate};
```
i.e. the viewer body embeds a per-response analytics token and is **not byte-stable**; only the catalogue page is.

Viewer content probes (`grep -c` on the F6 body): `范围 0, 术语 0, 编算 0, 农历 0, 历法 0, 朔 0, 节气 0,
紫金山 0`. Page tiles: 12 `<div id="N" class="page">` elements, ids 0–11, each 2315×3274 px, with
`var page = 12;` (line 1368) and the loader `request.open('get', 'viewGbImg?fileName='+bg, true);` (line 1463).

Download modal (F8): title `GB/T 33661-2017 全文下载`; `<input id="verifyCode" maxlength="4" placeholder="验证码">`;
`refreshVerifyCode()` sets `src='gc?_'+new Date().getTime()`; `checkCode()` POSTs `{verifyCode: …}` to `verifyCode`
and reloads on success. The captcha was **not** attempted.

## Findings against the staged text (candidate b)

**F1 — the staged byte-identity does not reproduce.** Staged: "byte-identical responses — 24148 bytes each, md5
`9791d9dc0f17384eeab4ff4791eed437`". Measured today: the no-navigation pair is identical at **24,144 B**, md5
`e866bfd61a16f4c4fcdc1fc3a16bdf89`, sha256 `80b4c781…`. Two consecutive fetches and one `Accept-Language`
variant all returned 24,144 B; a 24,148-byte response did not appear. The draft therefore carries no byte count
from the staged note except the ones re-measured today.

**F2 — "the download route is the catalogue page again, not a file" is refuted.** The identity in F1 is the
302 redirect's, not the route's. With the Referer the page's own buttons use, `type=download` returns a
7,606-byte 全文下载 captcha modal. The draft states this correction in §2 and the gate notes carry the record.

**F3 — the 在线预览提示 sentence is dead code.** The string 「当前浏览器暂不支持标准全文在线预览服务…」 exists
(catalogue lines 69 and 588) but the click handler's `if(supported)` guard is commented out (lines 114–119), so
the modal is never shown and 在线预览 always opens the viewer. The staged text read this string as the registry
"stating why the text is not on the page" — an overread the draft replaces.

**F4 — "no non-browser channel reaches the text" is too wide.** A request carrying the page's Referer gets the
viewer (89 KB); the viewer's ceiling is 12 raster tiles plus a captcha-gated file. The draft narrows the claim to
what is served and says the sentences are painted from images, not carried as text.

**F5 — Claim C's before-state is falsified at base (for the L1, not the entry).** The claims draft says
`git grep -l -E 'GB/T 33661' 98c486b -- corpus` prints nothing. It prints two lesson files (exit 0):
`corpus/lessons/round-68.md:111` ("S776 (openstd.samr.gov.cn GB/T 33661-2017 page, HTTP 200)" listed as present
and adoptable) and `corpus/lessons/round-69.md:39,111` (a package-row note). Only the `corpus/knowledge` scope is
empty. If `accept-c.py` asserts the declared before-state as written, it will fail; the honest before-state is
"no knowledge file and no registry row", which is what the entry's `ground:` line now states.

**F6 — lesson ids do not match the registry (collision guard).** `round-68.md:111` calls S776 the openstd page,
but registry row S776 at this base is the Penn Museum mancala paper; `round-69.md:39` calls S859 a package row
for this standard, but registry S859 is the lane's settlement classifier. So S776/S859 in those lessons are
package/comment ids, not registry ids. Registry `S897` is free (last row S893 per the claims draft; no openstd
row exists), so appending S897 does not collide — but the L1 should not treat the lesson ids as registry rows.

## What the draft contains (summary)

Provenance trio first (`source:` S897 with the three route URLs and C1–C9 locator scheme; `verified-at:
2026-10-27`; `recheck: 90d` with the four-request matrix and the re-located spans), then ground/topic/gap/sources/
couples/scope, then five dated sections: the catalogue fields as a citable table; the measured route family
(redirect vs viewer vs captcha modal) with the corrected byte counts; why the reading page carries no sentences
(tiles, loader, zero-word sweep, dead modal); a six-row decision table a worldbuilder can act on; and the
non-establishment + lore handoff. Calibration vocabulary is used for the one framework-level claim (the
instrument's in-force status = `mainstream`; the byte-identity inference = `discredited`); canon hygiene holds
(no world decided, no rights ruling, ends at the handoff).

## Out of scope / not done

- No clause text read, paraphrased or OCR'd; no `viewGbImg` image fetched; no captcha submitted.
- No writing outside the draft + stage dirs; no git mutation; no fleet-root writes.
- No installs during this seat (no tool needed).
- Scratch `/fast/scratch/hyaku/kotodama-r76/ScribeEntryB/` deleted after copying the evidence windows.

## Recheck (for the L1, before commit)

1. `python3 -B tools/check-cited-lines.py <draft>` → expect `CITED-LINES: 0 finding(s) in 1 file(s)`.
2. Re-run F1/F2/F3/F6/F8 and confirm: 24,144 B catalogue; 89,039/89,002 B viewer; 7,606 B download modal; 302
   without Referer. If the 302 rule changes, §2's claim changes and the entry must be re-measured, not softened.
3. Confirm the three couples still exist at the freeze revision.
