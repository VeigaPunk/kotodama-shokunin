import re, html, sys, unicodedata
entry = "/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-82/w1/drafts/corpus/knowledge/myth-symbol/guest-right-hospitality-law.md"
base = "/fast/scratch/hyaku/kotodama-r82/ScribeEntry/fetch/"

def norm(s):
    s = s.replace("\u00a0", " ").replace("\u2003", " ").replace("\u200b", "")
    s = s.replace("\u2019", "'").replace("\u2018", "'")
    s = re.sub(r"\s+", " ", s)
    s = re.sub(r"\s+([,.;:])", r"\1", s)
    return s.strip()

def plain_html(path):
    t = open(path, encoding="utf-8", errors="replace").read()
    t = re.sub(r"<script.*?</script>", "", t, flags=re.S)
    t = re.sub(r"<style.*?</style>", "", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return norm(html.unescape(t))

src = {
    "S904": norm(open(base+"pg1727.txt", encoding="utf-8", errors="replace").read()),
    "S905": plain_html(base+"germania.html"),
    "S906": norm(open(base+"pg26073.txt", encoding="utf-8", errors="replace").read()),
    "S907": plain_html(base+"guest_wayback.html"),
}
text = open(entry, encoding="utf-8").read()
bad = 0
for lineno, line in enumerate(text.splitlines(), 1):
    ids = sorted(set(re.findall(r"\bS\d{3,}\b", line)))
    quotes = re.findall(r"「([^」]*)」", line)
    for q in quotes:
        if not ids:
            print(f"NO-ID quote line {lineno}: {q[:60]}")
            bad += 1
            continue
        sid = ids[0]
        nq = norm(q)
        ok = nq in src[sid]
        wc = len(nq.split())
        flag = "OK" if ok else "MISS"
        if not ok or wc > 25:
            bad += 1
        print(f"{flag} line {lineno} {sid} words={wc} :: {nq[:90]}")
print("BAD", bad)
