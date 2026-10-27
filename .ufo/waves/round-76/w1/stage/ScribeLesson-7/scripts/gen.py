import re,html,unicodedata,pathlib,hashlib,subprocess
ST=pathlib.Path('/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-76/w1/stage/ScribeLesson-7')
UA="Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
def fold(s):
    s=unicodedata.normalize("NFKC",s); return re.sub(r"\s+"," ",s).strip()
def text_of(p):
    t=pathlib.Path(p).read_text(errors="replace")
    t=re.sub(r"(?is)<(script|style)[^>]*>.*?</\1>"," ",t)
    t=re.sub(r"(?s)<[^>]+>"," ",t); t=html.unescape(t)
    t=re.sub(r"[ \t\r\f\v\u3000]+"," ",t); t=re.sub(r"\n\s*\n+","\n",t)
    return t
def sha(p): return hashlib.sha256(pathlib.Path(p).read_bytes()).hexdigest()
rows=[
 dict(id="S894",carrier="live",file="S908-live-digital-archives-search.html",
      url="https://www.digital.archives.go.jp/search",status="HTTP/2 200",wire=311308,ct="text/html;charset=UTF-8",
      date="2026-10-27 fetch clock (no Date header on HTTP/2 response)",
      anchor="元号名称 開始西暦年 令和 2019 選択 平成 1989 選択 昭和 1926 選択 大正 1912 選択 明治 1868",
      loc="元号選択 > 和暦元号 table (元号名称/開始西暦年): header cell + first five era rows, cells in document order (選択 buttons included)"),
 dict(id="S894",carrier="capture",file="S935-capture-digital-archives-search.html",
      url="https://web.archive.org/web/20260422145052id_/https://www.digital.archives.go.jp/search",
      status="HTTP/1.1 200 (1st of 3 attempts; attempts 2 and 3 died at TCP, curl exit 7)",wire=307700,ct="text/html",
      date="2026-10-27 fetch clock",anchor=None,loc="same era table in the 2026-04-22 capture"),
 dict(id="S895",carrier="live",file="S916-live-xingzuobaike-d165803.html",
      url="https://www.xingzuobaike.com/huangli/wannianli/d165803.html",status="HTTP/2 200",wire=9093,ct="text/html; charset=utf-8",
      date="2026-10-27 fetch clock",
      anchor="取其中最先出现的一个不包含中气的农历月为农历闰月",
      loc="标准主要内容 > 1. 农历的编排规则, clause (4); the page's own provenance line reads 此文件原载 https://openstd.samr.gov.cn/bzgk/gb/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296"),
 dict(id="S896",carrier="live",file="S938-live-showGb-type-online.html",
      url="https://openstd.samr.gov.cn/bzgk/std/showGb?type=online&hcno=E107EA4DE9725EDF819F33C60A44B296",
      status="HTTP/1.1 302 -> Location .../newGbInfo?hcno=...&refer=outter -> HTTP/1.1 200",wire=7334,ct="text/html;charset=utf-8",
      date="Tue, 27 Oct 2026 21:35:30 GMT",
      anchor="当前浏览器暂不支持标准全文在线预览服务，请使用现代浏览器",
      loc="在线预览提示 modal text, following the 标准信息表 field rows (标准号 GB/T 33661-2017 ... 发布单位)"),
 dict(id="S896",carrier="capture",file="S932-capture-newGbInfo.html",
      url="https://web.archive.org/web/20260424031027id_/https://openstd.samr.gov.cn/bzgk/std/newGbInfo?hcno=E107EA4DE9725EDF819F33C60A44B296",
      status="HTTP/1.1 200 (gzip on the wire; stored body decompressed)",wire=8075,ct="text/html",
      date="2026-10-27 fetch clock",anchor=None,loc="same page, archived 2026-04-24"),
 dict(id="S898",carrier="live",file="S937-live-gmw-2017-05-23.html",
      url="https://news.gmw.cn/2017-05/23/content_24559485.htm",status="HTTP/1.1 200 OK (gzip on the wire)",wire=8076,ct="text/html",
      date="Tue, 27 Oct 2026 21:35:30 GMT",
      anchor="规定了朔日为农历月的第一个农历日，包含冬至在内的农历月为农历十一月",
      loc="article paragraph 4 (光明日报 2017-05-23 01版, 记者陈海波): the sentence stating the 编排规则"),
]
(W:=ST/"windows").mkdir(exist_ok=True)
WIN=4096; rec=["# Wave-1 fetch receipts — ScribeLesson-7 (round 76, kotodama)","",
 f"ua on every request below: `{UA}`","","access date: **2026-10-27**. One plain request per URL; no header spoofing beyond the UA, no cookie, no login, no challenge solved.",
 "`,`wire bytes` is curl's `%{size_download}` (compressed bytes as sent); `stored bytes`/`sha256` are the body this directory keeps (`fetch/`), decompressed by curl `--compressed`.","",
 "| row | carrier | url requested | status chain | content-type | wire bytes | stored bytes | sha256 (stored) | visible chars (non-space) | server date |","|---|---|---|---|---|---|---|---|---|---|"]
anch=[]
for r in rows:
    p=ST/"fetch"/r["file"]; t=text_of(p); vis=len(re.sub(r"\s","",t)); s=sha(p)
    rec.append(f"| {r['id']} | {r['carrier']} | {r['url']} | {r['status']} | {r['ct']} | {r['wire']} | {p.stat().st_size} | `{s}` | {vis} | {r['date']} |")
    f=fold(t)
    if r["anchor"]:
        a=fold(r["anchor"]); pos=f.find(a); assert pos>=0,r["id"]
        if len(f)>WIN:
            before=min(max(0,pos-200),len(f)-WIN); w=f[before:before+WIN]; scope="excerpt"
        else:
            before=0; w=f; scope="whole-document"
        hits=w.count(a); name=f"{r['id']}-{r['carrier']}.txt"
        hdr=[f"source: {r['url']}","access: 2026-10-27",f"ua: {UA}",f"http: {r['status']}",f"bytes-on-wire: {r['wire']}",f"stored-bytes: {p.stat().st_size}",f"body-sha256: {s}",
             f"window-scope: {scope}",f"chars: {len(w)} before: {before}",f"anchor: {r['anchor']}",f"anchor-chars: {len(a)} anchor-whitespace-tokens: {len(a.split())}",f"anchor-hits-in-window: {hits}",f"locator: {r['loc']}","--- window ---"]
        (W/name).write_text("\n".join(hdr)+"\n"+w+"\n")
        anch.append(f"{name}: scope={scope} chars={len(w)} anchor-chars={len(a)} tokens={len(a.split())} hits={hits}")
    else:
        name=f"{r['id']}-{r['carrier']}.txt"; w=f[:WIN]
        hdr=[f"source: {r['url']}","access: 2026-10-27",f"ua: {UA}",f"http: {r['status']}",f"bytes-on-wire: {r['wire']}",f"stored-bytes: {p.stat().st_size}",f"body-sha256: {s}",
             f"window-scope: {'whole-document' if len(f)<=WIN else 'excerpt'}",f"chars: {len(w)}","carrier-only: the row's anchor is quoted from the live carrier's window",f"locator: {r['loc']}","--- window ---"]
        (W/name).write_text("\n".join(hdr)+"\n"+w+"\n"); anch.append(f"{name}: carrier-only chars={len(w)}")
rec += ["","**Failed attempts in the same window.** `web.archive.org` (the S935 and S932 carriers): two of three attempts aborted before any HTTP response — `curl: (7) Failed to connect to web.archive.org:443`, exit 7; the attempt that connected returned HTTP/1.1 200 with 307700 B (S935). The capture kept here is the one that connected.",
 "","**No access control was met.** No response above was a 403/429/503, a captcha (altcha, hCaptcha, reCAPTCHA), a `Just a moment...` interstitial, a login wall or a paywall; every recorded response is the document itself.","",
 "**Route tests (same UA, same window)** — the registry's own alternate routes, all resolving to one URL:","",
 "| route | status chain | wire bytes | stored bytes | sha256 (stored) |","|---|---|---|---|---|",
 "| `showGb?type=online&hcno=…` | 302 -> newGbInfo?hcno=…&refer=outter -> 200 | 7334 | 24144 | `"+sha(ST/"fetch"/"S938-live-showGb-type-online.html")+"` |",
 "| `showGb?type=download&hcno=…` | 302 -> newGbInfo?hcno=…&refer=outter -> 200 | 7334 | 24144 | `"+sha(ST/"fetch"/"S938-route-test-showGb-type-download.html")+"` |",
 "| `/bzgk/gb/newGbInfo?hcno=…` | 301 -> `/bzgk/std/newGbInfo` -> 200 | 7334 | 24144 | (same bytes as the two rows above; the seat compared with `md5sum`, which printed `e866bfd61a16f4c4fcdc1fc3a16bdf89` three times) |",
 "","The download route carries no `Content-Disposition` header and returns the record page, not a file."]
(ST/"fetch-receipts.md").write_text("\n".join(rec)+"\n")
(ST/"anchors.txt").write_text("# anchor metrics (NFKC + whitespace folded) — round 76, ScribeLesson-7\n\n"+"\n".join(anch)+"\n")
print("\n".join(rec)); print(); print("\n".join(anch))
