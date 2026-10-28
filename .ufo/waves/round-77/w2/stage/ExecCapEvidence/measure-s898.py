#!/usr/bin/env python3
"""Independent measurement of the D2/S898 spans against the tool's own locate().

Reuses the round-77 capture tool's fold()/locate() (imported, not reimplemented)
so the tiers reported here are the same tiers the tool would report. Reads the
two PDFs already fetched into /fast/scratch/hyaku/kotodama-r77/ExecCapEvidence
and extracts them with pdftotext in the tool's default mode (-enc UTF-8) and in
-layout mode (the mode the W1 scout file says it used).
"""
import importlib.util
import json
import os
import subprocess
import sys

TOOL = ("/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-77/"
        "w1/stage/ExecAdaptCapture/capture-evidence.py")
SPEC = importlib.util.spec_from_file_location("cap_evidence", TOOL)
mod = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(mod)

QUOTE5 = "there were altogether 88 terms"
ANCHOR17 = ("According to Kałużyńska (2008, pp. 223, 232), there were altogether "
            "88 terms denoting plants, flowers and trees")
FIND = "According to Kałużyńska (2008, pp. 223, 232)"
WINDOW_FILE = ("/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/"
               "round-77/w2/stage/ExecCapEvidence/S898-candidate.txt")
WORK = "/fast/scratch/hyaku/kotodama-r77/ExecCapEvidence"


def extract(pdf, layout):
    argv = ["pdftotext", "-enc", "UTF-8"]
    if layout:
        argv.append("-layout")
    argv += [pdf, "-"]
    return subprocess.run(argv, check=True, capture_output=True).stdout.decode("utf-8")


def page_of(text, offset):
    return text.count("\f", 0, offset) + 1


def page_head(text, page):
    pages = text.split("\f")
    return pages[page - 1][:80].replace("\n", "\\n")


def occurrences(text, span):
    n, page_hits, start = 0, [], text.find(span)
    while start >= 0:
        n += 1
        page_hits.append(page_of(text, start))
        start = text.find(span, start + 1)
    return n, page_hits


def stored_window(path):
    lines = open(path, encoding="utf-8").read().split("\n")
    a = lines.index("--- window ---")
    b = lines.index("--- quote ---")
    return lines[a + 1]


def main():
    out = {}
    pdfs = {"live": os.path.join(WORK, "d2-live.pdf"),
            "wayback": os.path.join(WORK, "d2-wb.pdf")}
    win = stored_window(WINDOW_FILE)
    for name, pdf in pdfs.items():
        for layout in (False, True):
            text = extract(pdf, layout)
            mode = "layout" if layout else "enc-utf8"
            hit5 = mod.locate(text, QUOTE5)
            hit17 = mod.locate(text, ANCHOR17)
            hitfind = mod.locate(text, FIND)
            n17_verbatim, p17 = occurrences(text, ANCHOR17)
            n5_verbatim, p5 = occurrences(text, QUOTE5)
            pages = text.split("\f")
            out["%s/%s" % (name, mode)] = {
                "chars": len(text),
                "pages": len(pages),
                "quote5": {"tier": hit5["tier"], "verbatim": hit5["verbatim"],
                           "form": hit5["form"], "start": hit5["start"],
                           "page": page_of(text, hit5["start"])
                           if hit5["found"] else None,
                           "verbatim_occurrences": n5_verbatim,
                           "verbatim_pages": p5},
                "anchor17": {"tier": hit17["tier"], "verbatim": hit17["verbatim"],
                             "form": hit17["form"], "start": hit17["start"],
                             "page": page_of(text, hit17["start"])
                             if hit17["found"] else None,
                             "verbatim_occurrences": n17_verbatim,
                             "verbatim_pages": p17},
                "find": {"verbatim": hitfind["verbatim"], "tier": hitfind["tier"],
                         "start": hitfind["start"],
                         "page": page_of(text, hitfind["start"])},
                "page4_head": page_head(text, 4),
                "page4_chars": len(pages[3]),
                "page_chars": [len(p) for p in pages],
                "anchor_in_stored_window": mod.folded_has(win, ANCHOR17),
                "quote_in_stored_window": mod.folded_has(win, QUOTE5),
                "quote_in_anchor": mod.folded_has(ANCHOR17, QUOTE5),
                "anchor_prefix_len": len(ANCHOR17) - len(ANCHOR17.split(QUOTE5, 1)[1]) - len(QUOTE5),
                "window_chars": len(win),
            }
    print(json.dumps(out, indent=1, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    sys.exit(main())
