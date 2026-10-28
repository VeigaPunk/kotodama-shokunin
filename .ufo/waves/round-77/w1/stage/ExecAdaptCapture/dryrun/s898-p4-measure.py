#!/usr/bin/env python3
"""Where does the D2 quote actually sit in the PDF, page by page?

Run with the PDF fetched by `capture-evidence.py`'s own curl argv:

  s898-p4-measure.py <d2.pdf>

Uses the tool's own `extract_text` (pdftotext -enc UTF-8, form feeds kept) and
its own `locate`/`page_at`, so the pages reported here are the pages the
evidence file's `find-page`/`quote-page`/`anchor-page` report -- not a second
extraction's opinion.  It also re-extracts page 4 with `pdftotext -layout` and
counts the 17-word form there, so the two modes can be compared.
"""

import hashlib
import importlib.util
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(os.path.dirname(HERE), "capture-evidence.py")
Q17 = ("According to Kałużyńska (2008, pp. 223, 232), there were altogether 88 "
       "terms denoting plants, flowers and trees")
LOCATOR = "According to Kałużyńska (2008, pp. 223, 232)"


def load_tool():
    spec = importlib.util.spec_from_file_location("capture_evidence", TOOL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def main(argv):
    if len(argv) not in (1, 2):
        print("usage: %s <d2.pdf> [scratch-root]" % os.path.basename(__file__),
              file=sys.stderr)
        return 2
    path = os.path.abspath(argv[0])
    tool = load_tool()
    with open(path, "rb") as fh:
        body = fh.read()
    work = tool.make_work_dir(argv[1] if len(argv) > 1 else None, "s898-measure-")
    try:
        text, extract = tool.extract_text(body, "application/pdf", work, "measure")
        print("pdf: %s bytes=%d" % (path, len(body)))
        print("pdf sha256: %s" % hashlib.sha256(body).hexdigest())
        print("extract: %s" % extract)
        print("page-count: %d" % tool.page_count(text))
        feeds = [i for i, ch in enumerate(text) if ch == "\f"]
        print("form-feed offsets: %r" % (feeds,))
        for page in range(1, tool.page_count(text) + 1):
            start = 0 if page == 1 else feeds[page - 2] + 1
            head = " ".join(text[start:start + 120].split())
            print("page %2d: %s" % (page, head[:100]))
        for name, span in (("17-word-quote", Q17), ("locator", LOCATOR)):
            hit = tool.locate(text, span)
            pages = []
            start = 0
            while True:
                found = text.find(span, start)
                if found < 0:
                    break
                pages.append(tool.page_at(text, found))
                start = found + 1
            print("%s: found=%s verbatim=%s tier=%s start=%s pages=%r"
                  % (name, hit["found"], hit["verbatim"], hit["tier"],
                     hit["start"], pages))
        around = text[max(0, (tool.locate(text, LOCATOR)["start"] or 0) - 20):][:200]
        print("raw around the locator: %r" % around)
        layout = subprocess.run(
            ["pdftotext", "-layout", "-enc", "UTF-8", "-f", "4", "-l", "4",
             path, "-"], capture_output=True)
        flat = layout.stdout.decode("utf-8", "replace")
        print("pdftotext -layout page 4: 17-word occurrences=%d"
              % flat.count(Q17))
        single = "there were altogether 88 terms denoting plants, flowers and trees"
        print("verbatim single-line sub-span %r: %d"
              % (single, text.count(single)))
    finally:
        import shutil
        shutil.rmtree(work, ignore_errors=True)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
