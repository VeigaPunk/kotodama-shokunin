# Round 77 WAVE 1 — ScoutCDXPositive: Wayback CDX exact-url recon + positive control

Scope: QUALITY 21+24 — every "capture exists" / "no capture" statement below is backed by an
exact-matchType CDX probe plus a positive control run in the same session, same UA, same query shape.
UA bound to each request is recorded per QUALITY 22. No challenge was passed or bypassed: the cssn.cn
403 below is a UA filter met with the plain UA and reported as such; the browser-UA 200 was an
ordinary GET on the live URL, no captcha/paywall/login/geo workaround involved.

UA strings used:
- plain  = `curl/8.23.0` (tool default; `curl --version` → `curl 8.23.0 (x86_64-pc-linux-gnu) ...`)
- browser = `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`

Raw artifacts (headers, bodies, CDX JSON): `.ufo/waves/round-77/w1/stage/ScoutCDXPositive/`
(`d1-live-probe.txt`, `d1-live-{plain,browser}.{hdr,body}`, `cdx-{d1,d2,control,empty}.{out,hdr}`).

## (a) D1 — lishisuo.cssn.cn article (staged S897 → lane S897; DRAFT claim C row D1)

Probed URL verbatim (provenance: CLAIMS-DRAFT.md D1, `http://` scheme):
`http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml`

Live redirect/canonical probe FIRST, per spec:
- `curl -sS -m 30 -A <browser> -D hdr -o body -w ...` →
  `code=200 effective=http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml redirect_url= num_redirects=0`
- `curl -sSL -m 60` (plain UA, follow) → `code=403 ... num_redirects=0`
- `curl -sS -m 30` (plain UA, no follow) → `code=403 ... num_redirects=0`, 162-byte nginx 403 page,
  `Set-Cookie: SF_cookie_1=...` (WAF cookie), `Server: nginx`.

**Redirect/canonical target recorded: NONE.** The live URL serves directly —
`%{url_effective}` == requested URL, `num_redirects=0`, and grep of the 143252-byte body finds no
`<link rel="canonical">` and no meta refresh (found only `<title>` elements). The page IS the target.

**DRAFT attack datum (stale wall claim):** DRAFT says "live: HTTP 403 wall both UAs at L1 probe".
Observed now: browser UA gets **HTTP 200, 143252 bytes**, real article HTML —
`<title>魏斌:單名與雙名：漢晉南方人名的變遷及其意義-中国社会科学院历史研究所</title>`.
Only the plain `curl` UA is refused (403). The D1 ground therefore does NOT depend on the Wayback
capture: the live document opens by ordinary means with the fleet's browser-shaped UA. (If the L1
probe also used this UA and got 403, the wall is intermittent — report as observed at this seat's
probe time, Date header `Wed, 28 Oct 2026 01:32:19 GMT`.)

CDX exact query verbatim (browser UA):
`http://web.archive.org/cdx/search/cdx?url=lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml&output=json&matchType=exact&filter=statuscode:200`
- Response: HTTP 200, 295 bytes; raw output lines = 2 — `wc -l < cdx-d1.out`
- Rows: header + 1 capture.
- **First status-200 capture timestamp: `20240111092427`** —
  `["cn,cssn,lishisuo)/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml","20240111092427","http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml","text/html","200","MRIGYUAH7BQACKUKQCJ5BNS64GWDTXGA","41417"]`
- Matches DRAFT's stated capture `20240111092427` status 200.

## (b) D2 — onomastica.ijppan.pl PDF (staged S903 → lane S898; DRAFT claim C row D2)

Probed URL verbatim (provenance: CLAIMS-DRAFT.md D2; trailing slash as drafted):
`onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/`

CDX exact query verbatim (browser UA):
`http://web.archive.org/cdx/search/cdx?url=onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/&output=json&matchType=exact&filter=statuscode:200`
- Response: HTTP 200, 525 bytes; raw output lines = 3 — `wc -l < cdx-d2.out`
- Rows: header + 2 captures.
- **First status-200 capture timestamp: `20251231111748`** —
  `["pl,ijppan,onomastica)/index.php/onom/article/download/574/763","20251231111748","https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/","application/pdf","200","ZCYDDH2NSNNGJESPPEKUQTJVACTNUBDG","426128"]`
- Second capture `20260901045105` — same key, `application/pdf`, status 200 (original recorded
  without trailing slash; the exact-match key is normalized, so both originals roll up to this URL).
- Both DRAFT-stated captures (`20251231111748`, `20260901045105`) confirmed, status 200.

## (c) Positive control — en.wikipedia.org/wiki/Onomastics

Probed URL verbatim (provenance: seat spec, QUALITY 21/24 control):
`en.wikipedia.org/wiki/Onomastics`

CDX query verbatim (browser UA):
`http://web.archive.org/cdx/search/cdx?url=en.wikipedia.org/wiki/Onomastics&output=json&matchType=exact`
- Response: HTTP 200, 46523 bytes; raw output lines = 293 — `wc -l < cdx-control.out`
- **First status-200 capture timestamp: `20040723185055`** —
  `["org,wikipedia,en)/wiki/onomastics","20040723185055","http://en.wikipedia.org:80/wiki/Onomastics","text/html","200","24PROYLA5TEXNA6E7GB4VHBJNTBJR6MX","2556"]`
  (first row overall is a 2003 302; first 200 is as shown — `grep -m1 ',"200"' cdx-control.out`)
- Control positive ⇒ the CDX endpoint, this UA, and this query shape return real rows this session;
  any empty target result below is a property of the URL, not the probe.

## (d) Deliberately empty probe — composed absent slug

Probed URL verbatim (provenance: seat spec example slug, host matches D1):
`lishisuo.cssn.cn/xsyj/zzz-nonexistent-r77`

CDX query verbatim (browser UA):
`http://web.archive.org/cdx/search/cdx?url=lishisuo.cssn.cn/xsyj/zzz-nonexistent-r77&output=json&matchType=exact&filter=statuscode:200`
- Response: HTTP 200, **3 bytes**, body `[]`; raw output lines = 1 — `wc -l < cdx-empty.out`
- Confirmed: an absent slug returns an EMPTY array (`[]`), distinguishable from a populated result.
  This empty result is about the composed slug only — the real D1 slug returned a capture in the
  identical shape, session, and UA (see (a)), so `[]` here is NOT read as absence for the real URL
  (and vice versa: (a)'s non-empty result is not inferred from (d)).

## Findings vs DRAFT

1. DRAFT D1 capture claim verified: exact CDX returns capture `20240111092427`, status 200.
2. DRAFT D2 capture claims verified: `20251231111748` (first 200) and `20260901045105`, both 200.
3. DRAFT D1 "403 wall both UAs" is STALE at probe time: browser UA → live HTTP 200 full article
   (no redirect, no canonical elsewhere). Plain curl UA → 403 (UA filter, `SF_cookie_1` WAF cookie).
   Consequence for the claim's "ordinary means via capture" framing: the live page itself is
   openable; capture remains useful as a stable same-page pair (QUALITY 18) but is not the only
   open route observed by this seat.
4. Control + empty-probe pair bounds every positive statement above (QUALITY 21+24 satisfied).

No tools installed. Scratch `/fast/scratch/hyaku/kotodama-r77/ScoutCDXPositive` held no persistent
artifacts (all receipts under the wave stage dir); removed at exit.

Report: .ufo/waves/round-77/w1/ScoutCDXPositive.md
