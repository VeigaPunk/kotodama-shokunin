#!/usr/bin/env python3
"""Round-73 evidence capture builder (claim C GATE leg).

Fetches each adopted row's source with one recorded browser-shaped UA, extracts text
(pdftotext / html->text), locates the row's Gate quote verbatim (whitespace-collapsed),
and writes reports/round-73/evidence/<id>.txt: fetch line, sha256 of the fetched bytes,
extraction command, the quote with word count, and a +-400-char context window.
Never writes outside reports/round-73/evidence/ and /tmp/r73-evidence/.
"""
import hashlib, html, os, re, subprocess, sys, urllib.request

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
OUT = f"{LANE}/reports/round-73/evidence"
TMP = "/tmp/r73-evidence"
UA = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36"
DATE = "2026-10-25"

ROWS = [
    ("S876", "https://ojs.unito.it/index.php/ricognizioni/article/view/7099", "html",
     "the construction of languages by students allows them to better grasp the reality of linguistic analysis",
     "Abstract paragraph (served page, section Abstract)"),
    ("S877", "http://www.philol.msu.ru/~sidorova/files/conlangs.pdf", "pdf",
     "Языки, используемые в художественных произведениях, называют вымышленными или фикциональными.",
     "printed p. 10, Глава 1, «Классификация искусственных языков (конлангов)»"),
    ("S878", "https://journals.rudn.ru/semiotics-semantics/article/viewFile/31528/20955", "pdf",
     "the author examines the existing classifications of constructed languages and attempts to establish a connection between purposes of their creation and their linguistic features",
     "Abstract, p. 455"),
    ("S879", "https://cyberleninka.ru/article/n/klassifikatsii-konlangov-v-sovremennoy-interlingvistike", "html",
     "2.2. Personal languages Это личные, или персональные, языки, т. е. вымышленные языки, проектируемые отдельными энтузиастами лингвоконструирования",
     "comparison section «Сопоставление классификации Д. Питерсона с типологиями современных отечественных лингвистов», item 2.2 (printed p. 32)"),
    ("S880", "https://sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf", "pdf",
     "One innovation of this work is that it suggests that a multi-part, creative project can be part of a course even at the introductory level.",
     "§3 These papers, p. 5"),
]


def norm(s):
    s = html.unescape(s).replace("\u00ad", "").replace("\u2019", "'").replace("\u2018", "'")
    return re.sub(r"\s+", " ", s).strip()


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": UA})
    with urllib.request.urlopen(req, timeout=60) as r:
        return r.status, r.read()


def html_text(b):
    t = b.decode("utf-8", "replace")
    t = re.sub(r"(?is)<(script|style).*?</\1>", " ", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    return t


def main():
    os.makedirs(OUT, exist_ok=True)
    os.makedirs(TMP, exist_ok=True)
    bad = 0
    for rid, url, kind, quote, loc in ROWS:
        status, data = fetch(url)
        sha = hashlib.sha256(data).hexdigest()
        raw = f"{TMP}/{rid}.{kind}"
        open(raw, "wb").write(data)
        if kind == "pdf":
            cmd = f"pdftotext -enc UTF-8 {rid}.pdf -"
            text = subprocess.run(["pdftotext", "-enc", "UTF-8", raw, "-"], capture_output=True, text=True, check=True).stdout
        else:
            cmd = "html tags stripped, entities unescaped (python3 re/html)"
            text = html_text(data)
        nt, nq = norm(text), norm(quote)
        pos = nt.find(nq)
        found = pos >= 0
        words = len(quote.split())
        window = nt[max(0, pos - 400): pos + len(nq) + 400] if found else ""
        body = (
            f"# evidence {rid} — claim C GATE (round 73)\n"
            f"fetch: GET {url}\n"
            f"user-agent: {UA}\n"
            f"access-date: {DATE}\n"
            f"http-status: {status}\n"
            f"bytes: {len(data)}\n"
            f"sha256: {sha}\n"
            f"extract: {cmd}\n"
            f"locator: {loc}\n"
            f"quote-words: {words}\n"
            f"quote-found-verbatim: {'yes' if found else 'NO'}\n"
            f"quote: {quote}\n"
            f"--- context window (whitespace-collapsed, +-400 chars) ---\n{window}\n"
        )
        open(f"{OUT}/{rid}.txt", "w", encoding="utf-8").write(body)
        print(rid, status, len(data), sha[:12], "words", words, "found" if found else "NOT-FOUND")
        bad += 0 if found else 1
    sys.exit(1 if bad else 0)


main()
