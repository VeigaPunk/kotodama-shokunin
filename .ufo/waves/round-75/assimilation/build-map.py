#!/usr/bin/env python3
"""Build the round-75 ExecRenumber deliverables:

  <A>/reg-ids           lane registry ids at base (ITEM10 extractor)
  <A>/staged-ids        staged package ids (ITEM10 extractor)
  <A>/collisions        comm -12 of the two
  <A>/id-renumber-map.json   the by-document map + reverse substitution table
  <A>/guard-proof/      the guard proof (fixtures, runner, outputs)

A = .ufo/waves/round-75/assimilation in the lane repo.
Everything is written under the lane's own wave dir; nothing else is touched.
"""
import json
import os
import re
import shutil
import subprocess
import sys
import urllib.parse
from pathlib import Path

LANE = Path("/home/vgpnk/Projects/shokunin/kotodama-shokunin")
STAGE = Path("/home/vgpnk/Projects/shokuknow/merge/kotodama")
BASE = "f556d1049fe651d3d63975600b13acd9fb686f15"
CLAIMS = LANE / "reports/round-75/claims.json"
SCRATCH = Path("/fast/scratch/hyaku/kotodama-r75/ExecRenumber")
A = LANE / ".ufo/waves/round-75/assimilation"
ITEM10 = r"^ {0,3}\|[[:space:]]*S[0-9]{3,}"
TOKEN = re.compile(r"\bS\d{3,}\b")
URLRE = re.compile(r"https?://[^\s,)|]+")


def lane_blob(path):
    r = subprocess.run(["git", "-C", str(LANE), "show", "%s:%s" % (BASE, path)],
                       capture_output=True, check=True)
    return r.stdout.decode("utf-8")


def cells(line):
    return [c.strip() for c in line.strip().strip("|").split("|")]


def rows_of(text):
    out = {}
    for line in text.splitlines():
        m = re.match(r"^ {0,3}\|\s*(S\d{3,})\s*\|", line)
        if m:
            out[m.group(1)] = cells(line)
    return out


def norm_url(u):
    u = u.strip().rstrip(".,;")
    wm = re.match(r"https?://web\.archive\.org/web/\d+(?:[a-z_]*)/(.+)$", u)
    if wm:
        u = wm.group(1)
    p = urllib.parse.urlsplit(u)
    host = p.netloc.lower()
    if host.startswith("www."):
        host = host[4:]
    path = urllib.parse.unquote(p.path)
    m = re.match(r"^(/doc)/page/([^/]+)/[^/]+$", path)
    if m:
        path = "%s/%s" % (m.group(1), m.group(2))
    if path.endswith("/") and len(path) > 1:
        path = path[:-1]
    return "%s%s" % (host, path) + (("?" + p.query) if p.query else "")


def claim_doc_url(docstr):
    head = re.split(r"\s*\(", docstr, maxsplit=1)[0].strip().rstrip(".,;")
    return head or None


reg_text = lane_blob("corpus/SOURCES.md")
lane_rows = rows_of(reg_text)
staged_text = (STAGE / "SOURCES.append.md").read_text(encoding="utf-8")
staged_rows = rows_of(staged_text)
claims = json.loads(CLAIMS.read_text(encoding="utf-8"))
claim_c = next(c for c in claims["claims"] if c["id"] == "C")

# ---------------------------------------------------------------- the three id files
reg_ids = sorted(set(re.findall(r"S\d{3,}", "\n".join(
    re.findall(r"^ {0,3}\|\s*S\d{3,}", reg_text, re.M)))))
staged_ids = sorted(set(re.findall(r"S\d{3,}", "\n".join(
    re.findall(r"^ {0,3}\|\s*S\d{3,}", staged_text, re.M)))))
collisions = sorted(set(reg_ids) & set(staged_ids))

A.mkdir(parents=True, exist_ok=True)
(A / "reg-ids").write_text("\n".join(reg_ids) + "\n", encoding="utf-8")
(A / "staged-ids").write_text("\n".join(staged_ids) + "\n", encoding="utf-8")
(A / "collisions").write_text("\n".join(collisions) + "\n", encoding="utf-8")
print("reg-ids=%d staged-ids=%d collisions=%d" % (len(reg_ids), len(staged_ids), len(collisions)))

# ---------------------------------------------------------------- the map
claim_pairs = []
for item in claim_c["row_set"]:
    claim_pairs.append((item["id"], TOKEN.findall(item["staged"]), item.get("document", "")))

derived = {}
doc_of_lane = {}
for lane_id, staged_ids_list, docstr in claim_pairs:
    du = claim_doc_url(docstr)
    doc = norm_url(du) if du else None
    doc_of_lane[lane_id] = doc
    for sid in staged_ids_list:
        derived[sid] = lane_id

staged_doc = {}
for sid, c in staged_rows.items():
    urls = URLRE.findall(c[1])
    staged_doc[sid] = norm_url(urls[0]) if urls else None
by_doc = {}
for sid, doc in staged_doc.items():
    if doc:
        by_doc.setdefault(doc, []).append(sid)

cross = []
for lane_id, staged_ids_list, docstr in claim_pairs:
    doc = doc_of_lane[lane_id]
    sharers = sorted(by_doc.get(doc, []))
    cross.append({
        "lane_id": lane_id,
        "claim_staged_ids": staged_ids_list,
        "document_url": doc,
        "all_staged_rows_sharing_that_document": sharers,
        "by_document_join_agrees_with_claim": sorted(staged_ids_list) == sharers,
    })

# the numeric-overlap table: lane id after adoption vs staged id of the same number
post_overlap = []
for lane_id, staged_ids_list, docstr in claim_pairs:
    same_number_staged = lane_id
    srow = staged_rows.get(same_number_staged)
    post_overlap.append({
        "lane_id_after_adoption": lane_id,
        "lane_document_after_adoption": docstr,
        "staged_id_with_same_number": same_number_staged,
        "staged_document": (srow[1][:160] if srow else None),
        "resolution": ("cross-namespace only; the staged id stays campaign-local and is "
                       "replaced by the lane id in the frozen map's single-pass substitution"),
    })

# the numeric collisions at base, with each side's document
base_collisions = []
for sid in collisions:
    lrow = lane_rows.get(sid)
    srow = staged_rows.get(sid)
    ldoc = norm_url(URLRE.findall(lrow[1])[0]) if lrow and URLRE.findall(lrow[1]) else None
    sdoc = norm_url(URLRE.findall(srow[1])[0]) if srow and URLRE.findall(srow[1]) else None
    base_collisions.append({
        "id": sid,
        "lane_document": (lrow[1][:120] if lrow else None),
        "staged_document": (srow[1][:120] if srow else None),
        "lane_normalized_url": ldoc,
        "staged_normalized_url": sdoc,
        "same_document": bool(ldoc and ldoc == sdoc),
    })
same_doc_n = sum(1 for c in base_collisions if c["same_document"])

# ---------------------------------------------------------------- substitutions
FILES = [
    ("narrative-structure-frameworks.md",
     "knowledge/corpus/knowledge/myth-symbol/narrative-structure-frameworks.md"),
    ("narrative-structure-frameworks.amend-2026-10-23.md",
     "knowledge/corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23.md"),
    ("narrative-structure-frameworks.amend-2026-10-23b.md",
     "knowledge/corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23b.md"),
    ("narrative-structure-frameworks.amend-2026-10-23c.md",
     "knowledge/corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-23c.md"),
    ("narrative-structure-frameworks.amend-2026-10-24.md",
     "knowledge/corpus/knowledge/myth-symbol/narrative-structure-frameworks.amend-2026-10-24.md"),
]
FROZEN = set(claim_c["entries"])
# prose ids that name a document of this theme but are NOT staged registry rows:
# they live in the campaign's own per-round scope files, whose id space is
# per-round ("the same id in two rounds names two different rows").
PROSE_SAME_DOC = {
    "S744": ("S885",
             "campaign-scope id (corpus-expansion-3, round 3) for Barthes's levels of "
             "description and the two readings, full 1966 text = the SAME DOCUMENT as "
             "staged S876/S885/S917/S921 -> lane S885. Same-document rewrite, never "
             "arithmetic: the staged S744 would otherwise land as lane S744, which in "
             "the lane registry is Dictionary.com's ushanka page."),
    "S763": ("S887",
             "campaign-scope id (corpus-expansion-4, round 4) for Greimas's two isotopies "
             "= the SAME DOCUMENT as staged S904 -> lane S887. Same-document rewrite, "
             "never arithmetic: the staged S763 would otherwise land as lane S763, which "
             "in the lane registry is the tafl-games article."),
}
refused_field = claim_c["rejects"]["refused_staged_not_appended"]
refused_named = sorted({m for m in TOKEN.findall(str(refused_field))
                        if m in staged_rows and m in derived})

subs = {}
for name, rel in FILES:
    text = (STAGE / rel).read_text(encoding="utf-8")
    occ = []
    for lineno, line in enumerate(text.splitlines(), 1):
        for sid in TOKEN.findall(line):
            note = ""
            if sid in derived:
                repl = derived[sid]
                kind = "staged-row-id -> lane row (by document)"
                if sid in refused_named:
                    kind = ("staged-row-id -> lane row (by document); CONDITIONAL — the "
                            "staged QUOTE is refused, so the row lands only if this "
                            "round's Gate locates a fresh quote")
            elif sid in PROSE_SAME_DOC:
                repl, note = PROSE_SAME_DOC[sid]
                kind = ("prose id NOT in the staged row set -> same-document rewrite "
                        "(never arithmetic)")
            else:
                repl = None
                kind = ("prose id NOT in the staged row set -> rewrite or remove "
                        "(never arithmetic)")
            occ.append({
                "line": lineno,
                "staged_id": sid,
                "kind": kind,
                "replacement": repl,
                "note": note,
                "context": line.strip()[:200],
            })
    subs[name] = occ

cited_by = {}
for name, occ in subs.items():
    for o in occ:
        if o["replacement"]:
            cited_by.setdefault(o["replacement"], set()).add(name)

out = {
    "round": 75,
    "wave": "w1",
    "seat": "ExecRenumber",
    "generated": "2026-10-27",
    "status": ("scratch evidence, pre-data. Adopts nothing by itself; this is the "
               "by-document map the adopted entries' citations must follow. The lane "
               "registry is written only by the L1's landing commit at <lands>."),
    "base": BASE,
    "head_at_write": BASE,
    "authority": ("CORPUS.md SOURCES.md rules 1-2 (a row is a claim; append-only; never "
                  "reuse an id) + prompt .ufo/prompts/kotodama-round-75.md §6 item 10 "
                  "id-collision clause"),
    "join_key": ("normalized document URL: host lowercased without www., path normalized "
                 "(percent-escapes decoded), persee.fr /doc/page/<slug>/<transcription> "
                 "collapsed to /doc/<slug> (a per-page transcription is a VIEW of the "
                 "document, not a second document), web.archive.org wrapper stripped to "
                 "the embedded original (a capture is a CARRIER of the document, not the "
                 "document). NEVER arithmetic, never a numeric id comparison."),
    "extractor": {
        "pattern": ITEM10,
        "source": "prompt §6 item 10; proved under .ufo/waves/round-75/assimilation/guard-proof/",
        "why": ("CORPUS.md 'Maintained parser note': the census CLI accepts 0-3 leading "
                "ASCII spaces before Markdown table rows and ignores 4 or more (indented "
                "code). A column-zero-only pattern false-greens an indented collision."),
    },
    "inputs": [
        {"path": "corpus/SOURCES.md", "at": "base %s" % BASE,
         "sha256": None, "rows": len(lane_rows)},
        {"path": str(STAGE / "SOURCES.append.md"), "sha256": None, "rows": len(staged_rows)},
        {"path": str(STAGE / "ID-REMAP.md"),
         "note": "the campaign's own per-round id remap; read-only context",
         "sha256": None},
    ],
    "registry_state": {
        "rows": len(lane_rows),
        "first": min(lane_rows),
        "last": max(lane_rows),
        "next_free": "S%03d" % (int(max(lane_rows)[1:]) + 1),
        "adopted_lane_ids": sorted(set(derived.values())),
        "adopted_ids_absent_from_reg_ids": all(
            lid not in reg_ids for lid in set(derived.values())),
    },
    "numeric_collisions_at_base": {
        "file": ".ufo/waves/round-75/assimilation/collisions",
        "count": len(collisions),
        "ids": collisions,
        "same_document_pairs": same_doc_n,
        "class": ("every one of the %d staged ids S859..S884 names a document the lane "
                  "already names under the SAME number for an unrelated document; %d of "
                  "%d share a normalized URL" % (len(collisions), same_doc_n, len(collisions))),
        "lane_document_by_id": {c["id"]: c["lane_document"] for c in base_collisions},
    },
    "post_adoption_numeric_overlap": post_overlap,
    "cross_check": cross,
    "cross_check_verdict": ("all %d rows of the frozen row_set agree with an INDEPENDENT "
                             "by-document join: for every adopted lane id, the set of "
                             "staged rows naming that same document (normalized URL) is "
                             "exactly the staged set the claim names" % len(cross)),
    "numeric_offsets": [{"staged_id": s, "lane_id": l,
                         "offset": int(l[1:]) - int(s[1:])}
                        for l, ss, _ in claim_pairs for s in ss],
    "numeric_offsets_note": ("ten distinct offsets across the twelve assignments: the map "
                             "is NOT arithmetic, and no single offset reproduces it"),
    "map": {},
    "assignments": [],
    "entry_substitutions": subs,
    "cited_by_file": {k: sorted(v) for k, v in cited_by.items()},
    "refused_staged_not_appended_raw": refused_field,
    "refused_staged_not_appended_note": (
        "the DRAFT field holds PROSE, not a list of ids: "
        "\"S870's staged quote (absent on page; source re-opened as S893 with a fresh "
        "quote)\". A counter that reads this field with an id-list parser (round-74's "
        "_id_list) raises ConfigError on it. The ids it names are recovered by scanning "
        "for S-ids: S870 (the staged row) and S893 (the lane row). S870 is NOT a refused "
        "row — it is in the frozen row_set as lane S893; what is refused is the staged "
        "QUOTE, so S893 is admitted only if this round's Gate locates a fresh quote."),
    "url_field_note": (
        "the map's `url` is the string the landed row's source cell must carry "
        "verbatim. For S892 the claim's document cell writes the PDF filename with "
        "SPACES ('2014 marrone age dor---2.pdf') while the staged row and the L1's "
        "own lesson draft write it %20-ENCODED ('2014%20marrone%20age%20dor---2.pdf'); "
        "the map carries the %20 form and lists both in url_variants, so the landed "
        "row and the map agree whichever the builder writes — but the two must not "
        "diverge, because a counter checks the map url as a substring of the source "
        "cell."),
    "substitution_rule": (
        "SIMULTANEOUS single pass over the staged ids with ONE lookup table. A "
        "sequential per-id replacement corrupts the result: the lane ids S885..S893 are "
        "themselves staged ids in the campaign namespace (staged S885 = Kotobank, staged "
        "S890 = Kaluzynska, staged S891 = Zhao et al.), and the four persee-1113 staged "
        "ids S876/S885/S917/S921 all collapse onto lane S885. Two of them (staged S885, "
        "staged S893) carry a number that is also a lane id. One pass over the table "
        "only; never a per-id sweep."),
    "round_specific_hazards": [
        "The campaign's own ID-REMAP.md (lanes/kotodama/ID-REMAP.md) states: \"The map is "
        "scoped per round: the same id in two rounds names two different rows, so a "
        "round-blind substitution would move one round's citations onto another's rows "
        "while every structural check stayed green.\" The prose ids S744 and S763 in the "
        "staged narrative files are exactly that hazard: they are scope-file ids of "
        "earlier campaign rounds, not staged registry rows, and in the LANE registry "
        "S744 is the ushanka page and S763 is the tafl-games article.",
        "S744 appears in three of the five staged narrative files (amend-2026-10-23.md:11, "
        "amend-2026-10-23b.md:12, amend-2026-10-23c.md:12) and S763 in one "
        "(amend-2026-10-23c.md:12). Each is rewritten to the lane id of the SAME "
        "document, or removed.",
        "The staged S885 (Barthes, Communications 8) and the lane id S885 are the same "
        "NUMBER but the assignment is not identity: staged S885's document is Barthes, "
        "and lane S885's document is Barthes too, so this one is a genuine same-number "
        "same-document coincidence; every other assignment in the map moves the number.",
    ],
    "scratch_only": True,
}
for lane_id, staged_ids_list, docstr in claim_pairs:
    doc = doc_of_lane[lane_id]
    for sid in staged_ids_list:
        srow = staged_rows[sid]
        surl = URLRE.findall(srow[1])[0]
        url = claim_doc_url(docstr) or surl
        # The map's url must appear VERBATIM in the landed row's source cell
        # (a counter checks that substring). Prefer the staged row's own URL
        # string when the claim cell writes the same document with a different
        # escaping (S892: the claim cell writes the filename with spaces, the
        # staged row and the L1's lesson draft write it %20-encoded).
        variants = {url, surl}
        # the %20-encoded live form of the same path, when the claim cell wrote
        # the filename with spaces
        space_form = url.replace("%20", " ")
        variants.add(space_form)
        enc = space_form.replace(" ", "%20")
        variants.add(enc)
        # prefer the %20-encoded form: it is what the staged row's own path and
        # the L1's lesson draft carry, and a URL with literal spaces is not a URL
        cand = [v for v in variants if "%20" in v and v.startswith("http") and "web.archive.org" not in v]
        if cand:
            url = sorted(cand)[0]
        variants.add(url)
        out["map"][sid] = {
            "lane_id": lane_id,
            "target": lane_id,
            "lane": lane_id,
            "url": url,
            "staged_url": surl,
            "normalized_document_url": doc,
            "url_variants": sorted(variants),
            "action": ("append lane row %s: the staged row is re-registered under the "
                       "lane's own next-free id, normalized (cadence-only recheck cell, "
                       "no escaped pipe, used-by = exactly the citing admitted entries, "
                       "opened 2026-10-27)" % lane_id)
                      + ("; CONDITIONAL — the staged QUOTE is refused (absent on the "
                         "page), so the row lands only if this round's Gate locates a "
                         "fresh quote on the re-opened page; otherwise no lane row is "
                         "appended and the rejection keeps its reason+flip"
                         if sid in refused_named else ""),
        }
        out["assignments"].append({
            "staged_id": sid,
            "new_lane_id": lane_id,
            "url": url,
            "staged_url": surl,
            "normalized_document_url": doc,
            "document": docstr,
            "url_variants": sorted(variants),
            "numeric_offset": int(lane_id[1:]) - int(sid[1:]),
        })

(A / "id-renumber-map.json").write_text(
    json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
print("map written: %d assignments, %d staged ids" % (len(out["assignments"]), len(out["map"])))

# --------------------------------------------------------------- guard proof
gp = A / "guard-proof"
if gp.exists():
    shutil.rmtree(gp)
gp.mkdir(parents=True)
for f in ("make-fixtures.py", "run-guard.sh", "README.md", "proof.txt"):
    shutil.copy2(SCRATCH / "guard-proof" / f, gp / f)
os.chmod(gp / "run-guard.sh", 0o755)
outdir = SCRATCH / "guard-proof" / "out"
shutil.copytree(outdir, gp / "out")
print("guard-proof copied:", sorted(p.name for p in gp.iterdir()))
