#!/usr/bin/env python3
r"""Raw receipts for the two round-76 fixes, run through the CLI (not the
selftest harness), so the report can paste real command output.

Writes fixtures and receipts under $HYAKU_SCRATCH (default: this stage dir's
`receipts/`), never into a lane path outside the stage directory.  The lane is
only read (the round-75 evidence file for the last two receipts).

  HYAKU_SCRATCH=/fast/scratch/hyaku/kotodama-r76/ExecAdaptCapture \
      python3 demo-fixes.py
"""

import importlib.util
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "capture-evidence.py")
CLAIMS = os.path.join(HERE, "claims.json")
LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
SCRATCH = os.environ.get("HYAKU_SCRATCH") or os.path.join(HERE, "receipts")
RECEIPTS = os.path.join(HERE, "receipts")


def load_tool():
    spec = importlib.util.spec_from_file_location("capture_evidence", TOOL)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def run(name, argv):
    """Run the CLI, write stdout+stderr+exit to receipts/<name>.txt, print it."""
    proc = subprocess.run([sys.executable, TOOL] + argv, capture_output=True,
                          text=True, env=dict(os.environ, HYAKU_SCRATCH=SCRATCH))
    body = ("$ python3 capture-evidence.py %s\n%s%sEXIT=%d\n"
            % (" ".join(argv), proc.stdout, proc.stderr, proc.returncode))
    os.makedirs(RECEIPTS, exist_ok=True)
    with open(os.path.join(RECEIPTS, name + ".txt"), "w", encoding="utf-8") as fh:
        fh.write(body)
    print(body)
    return proc.returncode


def main():
    ce = load_tool()
    os.makedirs(SCRATCH, exist_ok=True)
    pdf = os.path.join(SCRATCH, "pages.pdf")
    with open(pdf, "wb") as fh:
        fh.write(ce._pdf(ce._pdf_pages("PDF fixture quote sentence.",
                                       "PDF fixture anchor span.",
                                       locator_on_page=5)))
    far = os.path.join(SCRATCH, "far-anchor.html")
    with open(far, "w", encoding="utf-8") as fh:
        fh.write(ce._fixture_far_anchor_html())
    top = os.path.join(SCRATCH, "top.html")
    with open(top, "w", encoding="utf-8") as fh:
        fh.write(ce._fixture_html())

    common = ["--claims-file", CLAIMS]
    run("pdf-no-find", common + ["--id", "PDF-no-find", "--url", "file://" + pdf,
                                 "--quote", "PDF fixture quote sentence.",
                                 "--anchor-quote", "PDF fixture anchor span.",
                                 "--out", os.path.join(SCRATCH, "PDF-no-find.txt"),
                                 "--allow-file"])
    run("pdf-find-page5", common + ["--id", "PDF-p5", "--url", "file://" + pdf,
                                    "--quote", "PDF fixture quote sentence.",
                                    "--anchor-quote", "PDF fixture anchor span.",
                                    "--find", "LOCATOR-MARKER page five",
                                    "--locator", "p. 5",
                                    "--out", os.path.join(SCRATCH, "PDF-p5.txt"),
                                    "--allow-file"])
    run("pdf-find-first-occurrence", common + ["--id", "PDF-p2", "--url", "file://" + pdf,
                                               "--quote", "PDF fixture quote sentence.",
                                               "--anchor-quote", "PDF fixture anchor span.",
                                               "--find", "LOCATOR-MARKER",
                                               "--out", os.path.join(SCRATCH, "PDF-p2.txt"),
                                               "--allow-file"])
    run("anchor-outside-window", common + ["--id", "FAR", "--url", "file://" + far,
                                           "--quote", ce.CJK_QUOTE,
                                           "--anchor-quote", ce.FAR_ANCHOR,
                                           "--out", os.path.join(SCRATCH, "FAR.txt"),
                                           "--allow-file"])
    run("anchor-absent-from-page", common + ["--id", "ABS", "--url", "file://" + top,
                                             "--quote", ce.CJK_QUOTE,
                                             "--anchor-quote", "この錨はページに存在しません",
                                             "--out", os.path.join(SCRATCH, "ABS.txt"),
                                             "--allow-file"])
    run("verify-round75-file", common + ["--verify",
                                         os.path.join(LANE, "reports", "round-75",
                                                      "evidence", "S885.txt"),
                                         "--allow-file"])
    run("verify-r76-file", common + ["--verify",
                                     os.path.join(HERE, "evidence", "S885.txt")])
    return 0


if __name__ == "__main__":
    sys.exit(main())
