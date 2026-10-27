#!/usr/bin/env python3
"""Round-76 by-document id map (ScoutIdMap). Read-only on lane + package; writes id-renumber-map.json next to itself.
join key = round-75 norm_url (host w/o www., decoded path, persee /doc/page/<slug>/<t> -> /doc/<slug>, wayback wrapper stripped). Never arithmetic."""
import json, re, subprocess, hashlib, urllib.parse, sys
from pathlib import Path
LANE = Path("/home/vgpnk/Projects/shokunin/kotodama-shokunin")
PKG = Path("/home/vgpnk/Projects/shokuknow/merge/kotodama")
BASE = "98c486bdb4650ba5b8e651d332910e8ee60ad121"
OUT = Path(__file__).resolve().parent
A = LANE / ".ufo/waves/round-76/assimilation"
ITEM10 = re.compile(r"^ {0,3}\|\s*(S\d{3,})\s*\|", re.M)
TOKEN = re.compile(r"\bS\d{3,}\b")
URLRE = re.compile(r"https?://[^\s,)|]+")
CULT = PKG / "knowledge/corpus/knowledge/culture-material"
ENTRIES = {"a": "calendar-festival-systems.amend-2026-10-24.md"}

def norm_url(u):
    u = u.strip().rstrip(".,;")
    wm = re.match(r"https?://web\.archive\.org/web/\d+(?:[a-z_]*)/(.+)$", u)
    if wm: u = wm.group(1)
    if not u.startswith("http"): u = "https://" + u
    p = urllib.parse.urlsplit(u)
    host = p.netloc.lower()
    if host.startswith("www."): host = host[4:]
    path = urllib.parse.unquote(p.path)
    m = re.match(r"^(/doc)/page/([^/]+)/[^/]+$", path)
    if m: path = "%s/%s" % (m.group(1), m.group(2))
    if path.endswith("/") and len(path) > 1: path = path[:-1]
    return "%s%s" % (host, path) + (("?" + p.query) if p.query else "")

def cells(l): return [c.strip() for c in l.strip().strip("|").split("|")]
def rows(text):
    out = {}
    for l in text.splitlines():
        m = ITEM10.match(l)
        if m: out[m.group(1)] = cells(l)
    return out
def urls_of(c):  # urls of the source cell, document-level only (cell 1)
    return URLRE.findall(c[1])
def docset(c): return sorted({norm_url(u) for u in urls_of(c)})
def sha(b): return hashlib.sha256(b).hexdigest()

lane_bytes = subprocess.run(["git","-C",str(LANE),"show",BASE+":corpus/SOURCES.md"],capture_output=True,check=True).stdout
lane_text = lane_bytes.decode(); lane = rows(lane_text)
st_bytes = (PKG/"SOURCES.append.md").read_bytes(); st = rows(st_bytes.decode())
reg_ids = sorted(lane); staged_ids = sorted(st); collisions = sorted(set(reg_ids)&set(staged_ids))
for f,v in (("reg-ids",reg_ids),("staged-ids",staged_ids),("collisions",collisions)):
    assert (A/f).read_text().split()==v, f
assert (len(reg_ids),len(staged_ids),len(collisions))==(817,132,35)
next_free = "S%03d" % (int(reg_ids[-1][1:])+1)

lane_doc_index = {}   # normalized doc -> [lane ids] over ALL urls in the lane source cell
for i,c in lane.items():
    for d in docset(c): lane_doc_index.setdefault(d,[]).append(i)
st_doc_index = {}
for i,c in st.items():
    for d in docset(c): st_doc_index.setdefault(d,[]).append(i)

# ---- by-document assignment (planned) --------------------------------------------------------
PLAN = [  # candidate-a documents, re-pointed by the actual document
 ( ["S908","S935"], "S894", True, "National Archives live page + same-page Wayback capture"),
 ( ["S932"], "S895", True, "openstd newGbInfo record; archived capture of this same page"),
 ( ["S938"], "S895", True, "showGb route redirects by 302 to the same newGbInfo record; alias only, no second row"),
 ( ["S937"], "S896", True, "Guangming Daily 2017-05-23 report"),
 ( ["S919"], "S892", False, "already-held Marrone PDF; not cited in the admitted entry"),
 ( ["S921"], "S885", False, "already-held Barthes article; not cited in the admitted entry")]
assign=[]; mp={}
for sids,lid,planned,note in PLAN:
    docs = {d for s in sids for d in docset(st[s])}
    assert len(docs)==1, (sids,docs)
    doc = next(iter(docs))
    lane_hits = sorted(lane_doc_index.get(doc,[]))
    if planned: assert lane_hits==[], (lid,lane_hits)
    else: assert lane_hits==[lid], (lid,lane_hits)
    for s in sids:
        urls = urls_of(st[s])
        rec = {"lane_id":lid,"target":lid,"lane":lid,"document_normalized":doc,
         "staged_url_cell_urls":urls,
         "lane_row_at_base": None if planned else {"id":lid,"url_cell_urls":urls_of(lane[lid]),"normalized":docset(lane[lid]),"scope":lane[lid][4],"tier":lane[lid][3],"status":lane[lid][7],"used_by":lane[lid][10]},
         "by_document_join":{"staged_rows_naming_this_document":sorted(st_doc_index[doc]),"lane_rows_at_base_naming_this_document":lane_hits},
         "action": ("append lane row %s (reopen 2026-10-27, one row for the document; used-by = exactly the admitted citing entries)"%lid) if planned else ("no append; row %s already in the lane at base; add the calendar entry to its used-by in place (allowed: used-by changes in place, logged old->new)"%lid),
         "planned_new_row": planned, "note": note}
        mp[s]=rec
        assign.append({"staged_id":s,"new_lane_id":lid,"planned_new_row":planned,"normalized_document_url":doc,"staged_url_cell_urls":urls})

# ---- per-file token occurrences ---------------------------------------------------------------
# bare scope-file ids from earlier campaign generations (NOT package rows; prose 'round N's S###' or live brief ids)
GEN = {
 "S750":{"doc":"openstd newGbInfo?hcno=E107... record of GB/T 33661-2017","package_row":"S859","same_document_as":["S932"],"lane_id_planned":"S895","evidence":"round7/CANNOT-ANSWER.md:32-33 'S750 carries the standard's identity, live status, dates, custodianship, CCS and ICS from the official registry record'; package S859 URL == S932 withdrawn-original URL"},
 "S718":{"doc":"same openstd record as S750","package_row":"S859","same_document_as":["S932","S750"],"lane_id_planned":"S895","evidence":"round2/REJECTIONS.md:7 'the openstd record of GB/T 33661-2017 ... round 1's row S718'; lanes/kotodama/.deepresearch/20261023_171557_kotodama-corpus/final_turn_001.md:180 'S718 | spec | A | PRC standard identity, live status and custodianship'; round1 original ids +141 -> package (S718->S859, ID-REMAP.md round1 S833->S859 is a third generation)"},
 "S807":{"doc":"xingzuobaike reproduction of GB/T 33661-2017 (Tier C)","package_row":"S916","same_document_as":[],"lane_id_planned":None,"evidence":"round7/CANNOT-ANSWER.md:33 'S807 carries the clause text as reproduced by a third party'; round7 KNOWLEDGE-PROPOSED.md:168,193"},
 "S719":{"doc":"pmo.cas.cn drafting-observatory interpretation PDF P020240201504886119982.pdf","package_row":"S860","same_document_as":["S777"],"lane_id_planned":None,"evidence":"round2/REJECTIONS.md:8 'the drafting observatory's 解读材料 ... round 1's S719'; staged S860 scope text"},
 "S777":{"doc":"same pmo.cas.cn interpretation PDF as S719","package_row":"S860","same_document_as":["S719"],"lane_id_planned":None,"evidence":"round8/REJECTIONS.md:19-23 'Round 3 staged it as S777 ... scope: the operational content of GB/T 33661-2017 as stated by its drafting observatory' == staged S860 scope cell verbatim. NOTE: +109 arithmetic from the S750..S809 generation puts S777 on staged S886 (Kotobank 苗字): the arithmetic DISAGREES with the document; the document wins"},
 "S757":{"doc":"NDL NDC10 classification standard PDF NDC10code202206.pdf","package_row":"S898","same_document_as":[],"lane_id_planned":None,"evidence":"round5/KNOWLEDGE-PROPOSED.md:83 'the library's classification (round 4's S757)'; round4/REJECTIONS.md:30 'S746 and S898, which supply a dated periodisation'; staged S898 is NDC10code202206.pdf"},
 "S732":{"doc":"rekihaku.ac.jp exhibitions (museum room labels)","package_row":"S873","same_document_as":[],"lane_id_planned":None,"evidence":"round3/KNOWLEDGE-PROPOSED.md:73 'a museum's room labels (round 2's S732)'; staged S873 rekihaku.ac.jp/exhibitions/"},
 "S746":{"doc":"kotobank.jp 平安時代 (round 3 compendium entry)","package_row":"S887","same_document_as":["S887"],"lane_id_planned":None,"evidence":"era-periodization-models.amend-2026-10-23.md:7 'round 3's S746' and :30 'S887 — https://kotobank.jp/word/平安時代-128778' name one document in two id generations inside ONE file"},
 "S726":{"doc":"bunka.go.jp 文化遺産データベース heritage filing ladder (round 1)","package_row":"S867","same_document_as":[],"lane_id_planned":None,"evidence":"round2/KNOWLEDGE-PROPOSED.md:146; staged S867 文化遺産データベース"}}
lane_at_base_for_bare = {k:{"lane_row_id_equal_to_bare_token_at_base":(k in lane),"lane_document_under_that_number":(re.split(r" — |, | - ",lane[k][1],1)[0][:90] if k in lane else None)} for k in GEN}
PKGMAP = {"S859":"S895","S932":"S895","S938":"S895","S937":"S896"}
subs = {}; cited_by = {}
doc_for_pkg = {s:rec["lane_id"] for s,rec in mp.items()}
for key,fn in ENTRIES.items():
    occ=[]
    for ln,line in enumerate((CULT/fn).read_text(encoding="utf-8").splitlines(),1):
        for m in TOKEN.finditer(line):
            t=m.group(0)
            if t in mp:
                kind="campaign registry id -> lane id (by document)"; repl=mp[t]["lane_id"]; note=""
            elif t in GEN:
                kind="bare scope-file id of an earlier campaign generation (not a package row; also a live lane id for an UNRELATED document)" if (t in lane) else "bare scope-file id of an earlier campaign generation (not a package row; no lane row under this number at base)"
                repl=GEN[t]["lane_id_planned"]; note=GEN[t]["doc"]
            elif t in st:
                kind="campaign registry id of a NON-candidate staged row"; repl=None; note="staged row "+t+": "+re.split(r" — |, ",st[t][1],1)[0][:70]
                if t in lane: note+=" | COLLISION: lane "+t+" at base = "+re.split(r" — |, ",lane[t][1],1)[0][:60]
                if t in ("S898",): note+=" | post-adoption overlap: planned lane S898 = gmw.cn report (S937)"
            else:
                kind="unresolved"; repl=None; note=""
            occ.append({"line":ln,"token":t,"kind":kind,"replacement_lane_id":repl,"note":note,"context":line.strip()[:200]})
            if repl: cited_by.setdefault(repl,set()).add(fn)
    subs[fn]=occ

# ---- the 35 collisions, per side document + relevance to the candidate entries -----------------------
coll=[]
cited_in_entries = {t for occ in subs.values() for o in occ for t in [o["token"]]}
for s in collisions:
    lr,sr=lane[s],st[s]
    coll.append({"id":s,"lane_document":re.split(r" — ",lr[1],1)[0][:90],"staged_document":re.split(r" — ",sr[1],1)[0][:90],
      "same_document":bool(set(docset(lr))&set(docset(sr))),
      "cited_bare_in_entries":sorted(k for k,fn in ENTRIES.items() if any(o["token"]==s for o in subs[fn])),
      "cited_in_candidate_entries_a_to_d": any(o["token"]==s for k in ENTRIES for o in subs[ENTRIES[k]])})
rel = [c for c in coll if c["cited_bare_in_entries"]]

overlap=[]  # planned lane ids vs staged id of the same number
for lid in ("S894","S895","S896"):
    overlap.append({"planned_lane_id":lid,"planned_lane_document_staged_ids":[s for s,r in mp.items() if r["lane_id"]==lid],
      "staged_row_with_same_number":lid,"staged_document":re.split(r" — ",st[lid][1],1)[0][:90],"same_document":False})
for lid in ("S885","S892"):
    overlap.append({"existing_lane_id":lid,"staged_row_with_same_number":lid,"staged_document":re.split(r" — ",st[lid][1],1)[0][:90],"same_document":bool(set(docset(st[lid]))&set(docset(lane[lid])))})

out = {"round":76,"wave":"w1","seat":"ScoutIdMap","generated":"2026-10-27",
 "status":"scratch evidence, pre-data. Adopts nothing; the by-document map the adopted entries' citations must follow. The lane registry is written only by the L1's landing commit.",
 "base":BASE,"head_at_write":subprocess.run(["git","-C",str(LANE),"rev-parse","HEAD"],capture_output=True,text=True).stdout.strip(),
 "authority":"corpus/SOURCES.md header (append-only; a row is a claim; used-by changes in place) + .ufo/waves/round-76/CLAIMS-DRAFT.md Claim C (campaign ids re-pointed BY DOCUMENT)",
 "join_key":"normalized document URL (round-75 norm_url): host lowercased without www., path percent-decoded, persee /doc/page/<slug>/<transcription> -> /doc/<slug>, web.archive.org wrapper stripped to the embedded original. NEVER arithmetic, never a numeric id comparison.",
 "extractor":{"pattern":"^ {0,3}\\|\\s*(S\\d{3,})\\s*\\|","same_as":"round 75 ITEM10; census parser accepts 0-3 leading spaces"},
 "inputs":[{"path":"corpus/SOURCES.md","at":BASE,"sha256":sha(lane_bytes),"rows":len(lane)},
           {"path":str(PKG/"SOURCES.append.md"),"sha256":sha(st_bytes),"rows":len(st)},
           {"path":str(LANE/".ufo/waves/round-76/assimilation/reg-ids"),"sha256":sha((A/"reg-ids").read_bytes()),"lines":817},
           {"path":str(LANE/".ufo/waves/round-76/assimilation/staged-ids"),"sha256":sha((A/"staged-ids").read_bytes()),"lines":132},
           {"path":str(LANE/".ufo/waves/round-76/assimilation/collisions"),"sha256":sha((A/"collisions").read_bytes()),"lines":35}]+
          [{"path":str(CULT/fn),"sha256":sha((CULT/fn).read_bytes()),"entry_key":k} for k,fn in ENTRIES.items()],
 "registry_state":{"rows":len(lane),"first":reg_ids[0],"last":reg_ids[-1],"next_free":next_free,"lane_holds_any_document_of_the_map_except_S885_S892":[d for d in lane_doc_index if any(d in docset(st[s]) for r in mp for s in [r]) and not set(lane_doc_index[d])<= {"S885","S892"}]},
 "numeric_collisions_at_base":{"count":len(collisions),"ids":collisions,"same_document_pairs":sum(c["same_document"] for c in coll),"per_id":coll,
   "relevant_to_entries":[{"id":c["id"],"cited_bare_in_entries":c["cited_bare_in_entries"],"lane_document":c["lane_document"],"staged_document":c["staged_document"]} for c in rel],
   "cited_in_candidate_entries_a_to_d":[c["id"] for c in coll if c["cited_in_candidate_entries_a_to_d"]]},
 "post_adoption_numeric_overlap":overlap,
 "bare_scope_file_ids":{"note":"earlier-generation ids in entry prose; none is a package row id; resolved by document through the round scope files","resolution":GEN,"lane_row_under_same_number_at_base":lane_at_base_for_bare},
 "map":mp,"assignments":assign,
 "entry_substitutions":subs,"cited_by_file":{k:sorted(v) for k,v in cited_by.items()},
 "candidates_not_mapped_to_lane_ids":["S860 / bare S719,S777 (pmo.cas.cn PDF): no planned row","S898 / bare S757 (NDC PDF): no planned row; staged S898 numerically equals planned lane S898","S887/S746 (Kotobank 平安), S873/S732, S867/S726: no planned row (entry e only)"],
 "scratch_only":True}
(OUT/"id-renumber-map.json").write_text(json.dumps(out,ensure_ascii=False,indent=1)+"\n",encoding="utf-8")
print("assignments",len(assign),"map",len(mp),"collisions",len(collisions),"relevant",[c["id"] for c in rel])
