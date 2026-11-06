import hashlib, json, os, re

CAP = "captures"

def sha(p):
    h = hashlib.sha256()
    with open(p, "rb") as f:
        for b in iter(lambda: f.read(1 << 20), b""):
            h.update(b)
    return h.hexdigest()

def norm(s):
    return re.sub(r"\s+", " ", s).strip()

def count(capfile, quote):
    t = norm(open(os.path.join(CAP, capfile), encoding="utf-8", errors="replace").read())
    return t.count(norm(quote))

C = [
 dict(key="C1", url="https://archive.org/download/80204dff-c8a9-4155-a539-7ee980102875/80204dff-c8a9-4155-a539-7ee980102875_djvu.txt",
      http=200, tier="B",
      captures=["C1-finnegan-panegyric.html", "C1-finnegan-panegyric.txt", "C1b-finnegan-olia-archive.txt"],
      quote_capture="C1b-finnegan-olia-archive.txt",
      quote="In return the ruler acknowledges their praise by gifts or money which are often given publicly.",
      alt_quote="praisers can withhold praise or include implicit or explicit derogatory allusions as a kind of negative sanction",
      admitted=True,
      reason="Open-access full text of Finnegan's Oral Literature in Africa (OBP 2012 revised edition, CC BY); chapter 5 'Panegyric' is the standard comparative survey of African praise poetry.",
      supports="patronage and reward: the ruler's public gift or payment closes the praise performance; praise withheld or derogatory allusion used as a negative sanction (alt quote, count==1)",
      note="The OBP/OpenEdition chapter page (https://books.openedition.org/obp/1192?lang=en) served only a preview; the OBP chapter page returned HTTP 429 on three attempts. Full text obtained from the Internet Archive copy of the same OBP edition (CC BY)."),
 dict(key="C2", url="https://journal.oraltradition.org/wp-content/uploads/files/articles/3iii/6_opland.pdf",
      http=200, tier="A",
      captures=["C2-opland-lord-singers.pdf", "C2-opland-lord-singers.txt"],
      quote_capture="C2-opland-lord-singers.txt",
      quote="it is his duty to greet Lord with a royal praise name",
      admitted=True,
      reason="Peer-reviewed original article by the leading specialist on Xhosa oral poetry (Oral Tradition 3/3, open access).",
      supports="the praise singer's office: the imbongi's duty to greet the dignitary with a praise name, and the audience's expected repetition of it (praise performance order/audience)"),
 dict(key="C3", url="https://journal.oraltradition.org/wp-content/uploads/files/articles/20ii/Barber.pdf",
      http=200, tier="A",
      captures=["C3-barber-text-performance.pdf", "C3-barber-text-performance.txt"],
      quote_capture="C3-barber-text-performance.txt",
      quote="Obscurity in praise poetry could be deployed for political reasons.",
      admitted=True,
      reason="Peer-reviewed original article by Karin Barber (Oral Tradition 20/2, open access), the standard authority on Yoruba oriki.",
      supports="praise epithet as performance strategy: allusive, incomplete naming encodes discreet criticism of royal power (limits of flattery)"),
 dict(key="C4", url="https://journal.oraltradition.org/wp-content/uploads/files/articles/16i/Groenewald.pdf",
      http=200, tier="A",
      captures=["C4-groenewald-ndebele.pdf", "C4-groenewald-ndebele.txt"],
      quote_capture="C4-groenewald-ndebele.txt",
      quote="The praise poem for kings and chiefs has also been adapted to serve the trade union movement",
      admitted=True,
      reason="Peer-reviewed original article on Ndebele/Zulu praise poetry (Oral Tradition 16/1, open access).",
      supports="the praise singer's office and audience: royal praise adapted to unions, election campaigns and public ceremonials"),
 dict(key="C5", url="https://www.journal.oraltradition.org/wp-content/uploads/files/articles/10i/8_kaschula.pdf",
      http=200, tier="A",
      captures=["C5-kaschula-mandela.pdf", "C5-kaschula-mandela.txt"],
      quote_capture="C5-kaschula-mandela.txt",
      quote="directed at the Chief, decrying what was unworthy, praising what was worthy",
      admitted=True,
      reason="Peer-reviewed original article on the contemporary Xhosa imbongi (Oral Tradition 10/1, open access).",
      supports="praise performance: address to the chief, licensed criticism inside praise, and the political limits placed on it"),
 dict(key="C6", url="https://www.iranicaonline.org/articles/courts-and-courtiers-x/",
      http=403, tier=None, captures=["C6-iranica-court-poetry.html"], quote_capture=None,
      quote=None, admitted=False,
      reason="UNREACHABLE: Cloudflare bot challenge ('Just a moment...') on the article page (HTTP 403 shell, 5539 bytes); the ?generate_pdf=1 endpoint returned HTTP 403. Not evidence.",
      supports="none",
      note="Attempts: article page 3x (403, 5539 bytes each); PDF endpoint 1x (403, 5621 bytes). No retry beyond the transient rule because 403 is a wall, not a transient failure."),
 dict(key="C7", url="https://www.gutenberg.org/cache/epub/10717/pg10717.txt",
      http=200, tier="A",
      captures=["C7-pindar-extant-odes.txt"], quote_capture="C7-pindar-extant-odes.txt",
      quote="Yet praise is overtaken of distaste, wherewith is no justice, but from covetous men it cometh",
      admitted=True,
      reason="Primary text in public-domain translation (Pindar, Extant Odes, trans. Myers, Gutenberg #10717).",
      supports="the limits of flattery: praise is resented by the covetous; Pindar's commissioned odes for Hieron and Theron are the epinician patron model"),
 dict(key="C8", url="https://skaldic.org/m.php?p=text&v=intro&i=1258",
      http=0, tier=None, captures=[], quote_capture=None, quote=None, admitted=False,
      reason="UNREACHABLE: connection timed out after 30 s on three attempts (curl rc=28, 0 bytes). Not evidence.",
      supports="none",
      note="Attempts: 3 (all rc=28 timeout). Skaldic Project content is covered instead by C12 (Potts, ASNC)."),
 dict(key="C9", url="https://www.gutenberg.org/files/9842/9842-h/9842-h.htm",
      http=200, tier="A",
      captures=["C9-gododin.html", "C9-gododin.txt"], quote_capture="C9-gododin.txt",
      quote="A more choice act of mine will be To celebrate thy praise in song",
      admitted=True,
      reason="Primary text in public-domain translation (Y Gododdin, trans. Williams 1852, Gutenberg #9842).",
      supports="the praise poet's office: praise instead of reproach for the fallen patron; commemorative praise of named warriors"),
 dict(key="C10", url="https://archive.org/stream/book-3-purananuru/BOOK3-Purananuru_djvu.txt",
      http=200, tier="B",
      captures=["C10-purananuru.html", "C10-purananuru-clean.txt"],
      quote_capture="C10-purananuru-clean.txt",
      quote="The main themes found in Purananuuru are praise of the ruler, patronage, heroism in battles",
      admitted=True,
      reason="English translation with introduction of the Sangam puram anthology (Rajeswari, Chandrothayam); institutional-style scholarly rendering, not peer-reviewed.",
      supports="patronage and reward in Sangam puram praise: bards praise patrons and are honoured with gifts before they move on"),
 dict(key="C11", url="https://journals.uni-goettingen.de/wom/article/download/2303/1986/5234",
      http=200, tier="B",
      captures=["C11-trio-da-kali-stub.html", "C11b-trio-da-kali.pdf", "C11b-trio-da-kali.txt"],
      quote_capture="C11b-trio-da-kali.txt",
      quote="the praise-singing function is by far the most obvious and audible manifestation",
      admitted=True,
      reason="Peer-reviewed article in World of Music (open access) summarising Hale 1998 on Mande griot roles; the quoted sentence is Hale's, quoted in the article.",
      supports="the praise singer's office and genealogical recitation: griot functions listed as genealogist, historian, advisor, praise-singer"),
 dict(key="C12", url="https://www.asnc.cam.ac.uk/resources/mpvp/wp-content/uploads/2013/02/Introduction-to-Skaldic-Poetry_Debbie-Potts.pdf",
      http=200, tier="B",
      captures=["C12-potts-skaldic-intro.pdf", "C12-potts-skaldic-intro.txt"],
      quote_capture="C12-potts-skaldic-intro.txt",
      quote="There certainly was money in poetry for the skald; court poets would receive generous rewards",
      alt_quote="skalds would compete for the favour of their patron by crafting the most elaborate of praise poems",
      admitted=True,
      reason="Institutional scholarly introduction (University of Cambridge ASNC resource), open PDF.",
      supports="patronage and reward plus rivalry: skalds paid for praise of kings and earls and competing for a patron's favour (alt quote, count==1)"),
 dict(key="C13", url="https://mural.maynoothuniversity.ie/id/eprint/19500/1/Kavanagh%20Emer%20Signs%20and%20Wonders.pdf",
      http=200, tier="B",
      captures=["C13-kavanagh-satire.pdf", "C13-kavanagh-satire.txt"],
      quote_capture="C13-kavanagh-satire.txt",
      quote="a poet should not satirize or over-praise a subject, as the fili depended on the wealth of his patron",
      admitted=True,
      reason="Institutional PhD thesis (Maynooth University), open PDF; not peer-reviewed.",
      supports="the limits of flattery: law-text rule against over-praise, because the fili lived on the patron's reward (duas)"),
 dict(key="C14", url="https://journal.ru.ac.za/index.php/africanmusic/article/download/1116/591/593",
      http=200, tier="B",
      captures=["C14-african-music-hausa.pdf", "C14-african-music-hausa.txt"],
      quote_capture="C14-african-music-hausa.txt",
      quote="not above converting praise to satire of a potential patron\u2019s miserliness, if they consider his \u201cgift\u201d inadequate",
      admitted=False,
      reason="REJECTED for anchor scope: Gourlay's article is about long trumpets of northern Nigeria; the praise-singer patronage passage is a six-line aside, so a registry row scoped to praise poetry would be mis-anchored.",
      supports="satire as the sanction for an inadequate gift (usable only as corroboration)",
      note="Flip: a dedicated study of Hausa maroka praise-singing and patron exchange (e.g. Smith 1957, Africa 27/1) opened at source."),
]

out = []
for c in C:
    caps = []
    for f in c["captures"]:
        p = os.path.join(CAP, f)
        caps.append({"file": "captures/" + f, "sha256": sha(p), "bytes": os.path.getsize(p)})
    qc = c["quote_capture"]
    q = c["quote"]
    qcount = count(qc, q) if qc and q else None
    alt = c.get("alt_quote")
    altcount = count(qc, alt) if qc and alt else None
    rec = {
        "key": c["key"],
        "url": c["url"],
        "access": "2026-11-06",
        "http": c["http"],
        "bytes": next((x["bytes"] for x in caps if qc and x["file"] == "captures/" + qc), caps[0]["bytes"] if caps else 0),
        "captures": caps,
        "quote_capture": ("captures/" + qc) if qc else None,
        "tier": c["tier"],
        "quote": q,
        "quote_count": qcount,
        "admitted": c["admitted"],
        "reason": c["reason"],
        "supports": c["supports"],
    }
    if alt:
        rec["alt_quote"] = alt
        rec["alt_quote_count"] = altcount
    if c.get("note"):
        rec["note"] = c["note"]
    out.append(rec)

doc = {
    "schema": "kotodama-round-99-scout-sources-v1",
    "lane": "kotodama",
    "round": 99,
    "seat": "ScoutSources99",
    "topic": "praise poetry and panegyric",
    "access_date": "2026-11-06",
    "registry_duplicate_check": "grep -c -F '<url>' corpus/SOURCES.md returned 0 for every candidate URL and for every host+path prefix tested; no candidate duplicates an existing registry row.",
    "candidates": out,
}
json.dump(doc, open("candidates.json", "w", encoding="utf-8"), indent=1, ensure_ascii=False)
print("admitted", sum(1 for r in out if r["admitted"]), "of", len(out))
for r in out:
    print(r["key"], r["admitted"], r["tier"], r["quote_count"], r.get("alt_quote_count"))
