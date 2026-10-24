#!/usr/bin/env python3
"""Round-65 mutant probe for reports/round-65/accept-ca.py (claim Ca).

Builds five single-point loosening mutants of the frozen detector, plus a
synthetic fixture battery in which every leg is genuinely green except the one
property each mutant stops checking. Runs the full instrument x root matrix
(6 instruments: pristine + 5 mutants; 6 roots: green + 5 defect variants) and
the base-bytes conformance matrix against the committed pre-data receipt
reports/round-65/telemetry/dry-run-ca.txt.

Read-only with respect to the lane: writes only under
.ufo/waves/round-65/stage/mut-ca/.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
STAGE = os.path.join(LANE, ".ufo/waves/round-65/stage/mut-ca")
SRC = os.path.join(LANE, "reports/round-65/accept-ca.py")
BASE = "17c32302c6845c8f164b985a8cb312d3181c8788"
TRUE_TREE = "0ec0e50ea828ca6d8e20298f72af49414692e9e4"
FALSE_TREE = "1111111111111111111111111111111111111111"

MUTANTS = {
    "m1-r1-tree-any-hex": (
        '             and re.search(rf"^tree: {re.escape(tree)}$", receipt, re.MULTILINE) is not None\n',
        '             and re.search(r"^tree: [0-9a-f]{40}$", receipt, re.MULTILINE) is not None\n',
    ),
    "m2-r2-append-only-dropped": (
        '    leg("R2", r2_original_intact and r2_named,\n',
        '    leg("R2", r2_named,\n',
    ),
    "m3-r7-skeleton-anywhere": (
        '    r7_ok = (m is not None\n'
        '             and not re.search(r"skeleton|await L1", verified_at, re.IGNORECASE))\n',
        '    r7_ok = (m is not None\n'
        '             and not re.search(r"skeleton", entry, re.IGNORECASE))\n',
    ),
    "m4-quotes-other-lesson": (
        'R65_LESSON = "corpus/lessons/round-65.md"\n',
        'R65_LESSON = "corpus/lessons/round-64.md"\n',
    ),
    "m5-criterion-17-substring": (
        '    r_criterion = re.search(r"^1[7-9]\\.\\s", quality, re.MULTILINE) is not None and \\\n'
        '        re.search(r"tree hash", quality) is not None\n',
        '    r_criterion = re.search(r"17\\.", quality) is not None\n',
    ),
}


def sha(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as fh:
        fh.write(text)


def build_mutants():
    src = open(SRC, encoding="utf-8").read()
    out = {}
    shutil.copyfile(SRC, os.path.join(STAGE, "accept-ca.pristine.py"))
    for name, (old, new) in MUTANTS.items():
        assert src.count(old) == 1, (name, src.count(old))
        path = os.path.join(STAGE, name + ".py")
        write(path, src.replace(old, new))
        out[name] = path
    out["pristine"] = os.path.join(STAGE, "accept-ca.pristine.py")
    return out


def base_revisions():
    proc = subprocess.run(["git", "-C", LANE, "show",
                           BASE + ":reports/round-63/telemetry/revisions.txt"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    assert proc.returncode == 0, proc.stderr
    return proc.stdout.decode("utf-8")


GREEN = {
    "reports/round-64/telemetry/final-measures-ca.txt":
        "# final measures, claim Ca (round 64)\n"
        "re-stamped in round 65 (R1) to the revision its read-path bytes equalled\n"
        "measured revision: 8bab271c691c6b1006da95316a24ae1958ec01e2\n"
        "tree: " + TRUE_TREE + "\n"
        "\n"
        "## original receipt bytes (preserved verbatim below this marker)\n"
        "measured revision: 95c9194ef938e1338b2af894086a46e8b8677ee2\n",
    "LOG.md":
        "# LOG\n"
        "- Correction (round 65, R1): final-measures-ca.txt re-stamped; repeat corrected here,\n"
        "  SCORECARD.md and .ufo/waves/round-64/w2/LessonFinal.md.\n"
        "- Correction (round 65, R3): the actual path is .ufo/waves/round-64/w1/ReviewerCa.md;\n"
        "  the filed report's w2/ReviewerCa.md is named as the erratum target.\n"
        "- Control-O binding: reports/round-64/telemetry/control-o.txt is bound to counter\n"
        "  revision 3 (sha256 c27a9fef) measured at b7d22703.\n",
    "SCORECARD.md":
        "# SCORECARD\n"
        "- Correction (round 65, R1): final-measures-ca.txt re-stamped; repeats corrected.\n"
        "- Correction (round 65, R3): actual path is .ufo/waves/round-64/w1/ReviewerCa.md.\n",
    ".ufo/waves/round-64/w2/LessonFinal.md":
        "- Correction (round 65, R1): the repeat of the false measured revision is corrected.\n",
    "reports/round-64/claims.json":
        json.dumps({"claims": [{"id": "O", "statement_correction":
                                "the mutant wording is the honest at least their pinned leg",
                                "predicate":
                                "ACCEPT-O-64: every leg of reports/round-64/accept-o.py prints PASS."}]},
                   indent=2) + "\n",
    "reports/round-64/telemetry/control-o.txt":
        "control-o.txt bound to counter revision 3 sha256 c27a9fef measured at b7d22703\n",
    "corpus/lessons/round-64.md":
        "# Round 64 - lesson\n\n## Gate\n\n"
        "- S690 \"a short quotation of five words\" - accessed 2026-10-23 - grounds here.\n\n"
        "- Correction (round 65, R6): R64-M12 status corrected; S687 flip is committed in 95c9194e.\n",
    "corpus/knowledge/linguistics/language-socialization-and-acquisition.md":
        "# Entry\n\n- verified-at: 2026-10-24 - corrected this round; citation check passed.\n",
    "corpus/QUALITY.md":
        "# QUALITY\n\n"
        "17. **Receipt provenance** - a receipt must pin the measured revision and a tree hash\n"
        "    of its read inputs, never only the counter sha.\n",
    "corpus/lessons/round-65.md":
        "# Round 65 - lesson\n\n## Gate\n\n"
        "- S750 \"a short quotation of six words here\" - accessed 2026-10-24 - grounds here.\n"
        "\n## Status\n",
}

LONG_QUOTE = " ".join("word%d" % i for i in range(30))


def build_fixtures():
    roots = {}
    rev = base_revisions()

    def make(name, overrides):
        root = os.path.join(STAGE, "fixture-" + name)
        if os.path.isdir(root):
            shutil.rmtree(root)
        for rel, text in GREEN.items():
            write(os.path.join(root, rel), text)
        write(os.path.join(root, "reports/round-63/telemetry/revisions.txt"),
              rev + "Correction (round 65, R2): the header clause measured 8d2041fa for\n"
                    "final-measures-c.txt is false; the path is absent at 8d2041fa.\n")
        link = os.path.join(root, "tools")
        os.makedirs(link, exist_ok=True)
        for f in ("check-gate-quotes.py",):
            shutil.copyfile(os.path.join(LANE, "tools", f), os.path.join(link, f))
        for rel, text in overrides.items():
            write(os.path.join(root, rel), text)
        roots[name] = root

    make("green", {})
    make("d1-wrong-tree", {
        "reports/round-64/telemetry/final-measures-ca.txt":
            GREEN["reports/round-64/telemetry/final-measures-ca.txt"].replace(
                "tree: " + TRUE_TREE, "tree: " + FALSE_TREE)})
    make("d2-append-only-violated", {
        "reports/round-63/telemetry/revisions.txt":
            "Correction (round 65, R2): final-measures-c.txt measured revision corrected.\n"})
    make("d3-stale-await-L1", {
        "corpus/knowledge/linguistics/language-socialization-and-acquisition.md":
            "# Entry\n\n- verified-at: 2026-10-23 - structure prepared; "
            "cited source claims await L1 insertion and review.\n"})
    make("d4-long-quote-r65", {
        "corpus/lessons/round-65.md":
            "# Round 65 - lesson\n\n## Gate\n\n"
            '- S751 "%s" - accessed 2026-10-24 - grounds here.\n\n## Status\n' % LONG_QUOTE})
    make("d5-no-criterion-17", {
        "corpus/QUALITY.md":
            "# QUALITY\n\nThe routed defects are listed in section 17.2 of the round-64\n"
            "spot-check; no criterion row is added and no tree hash is required.\n"})
    return roots


def run(instrument, root):
    proc = subprocess.run([sys.executable, "-B", instrument, "--root", root],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    text = proc.stdout.decode("utf-8", "replace")
    legs = {}
    for line in text.splitlines():
        m = re.match(r"^(\w+) (PASS|FAIL) (.*)$", line)
        if m:
            legs[m.group(1)] = (m.group(2), m.group(3))
    tail = text.strip().splitlines()[-1] if text.strip() else ""
    return {"exit": proc.returncode, "legs": legs, "verdict": tail,
            "stderr": proc.stderr.decode("utf-8", "replace")[-400:]}


def receipt_legs():
    path = os.path.join(LANE, "reports/round-65/telemetry/dry-run-ca.txt")
    out = {}
    for line in open(path, encoding="utf-8"):
        m = re.match(r"^(\w+) (PASS|FAIL) (.*)$", line.rstrip("\n"))
        if m:
            out[m.group(1)] = (m.group(2), m.group(3))
    return out


def main():
    os.makedirs(STAGE, exist_ok=True)
    instruments = build_mutants()
    roots = build_fixtures()
    rec = receipt_legs()
    report = {"instrument_hash_before": sha(SRC), "receipt_legs": rec,
              "mutant_hash": {k: sha(v) for k, v in instruments.items()},
              "base": {}, "matrix": {}}

    print("== base-bytes conformance (root=lane, tip == base %s) ==" % BASE[:8])
    for name, inst in instruments.items():
        r = run(inst, LANE)
        div = []
        for leg, (status, detail) in r["legs"].items():
            want = rec.get(leg)
            if want is None:
                div.append("%s: receipt has no line" % leg)
            elif want[0] != status:
                div.append("%s: receipt=%s/%s got=%s/%s" % (leg, want[0], want[1][:40], status, detail[:40]))
            elif want[1] != detail:
                div.append("%s: detail drift receipt=%r got=%r" % (leg, want[1][:70], detail[:70]))
        report["base"][name] = {"verdict": r["verdict"], "exit": r["exit"], "diverge": div}
        print("%-28s %-22s exit=%d diverge=%s" % (name, r["verdict"], r["exit"],
                                                  div if div else "none"))

    print("\n== fixture matrix (rows=instrument, cols=root) ==")
    cols = list(roots)
    print("%-28s %s" % ("", " ".join("%-26s" % c for c in cols)))
    for name, inst in instruments.items():
        cells = []
        for c in cols:
            r = run(inst, roots[c])
            report["matrix"].setdefault(name, {})[c] = {
                "verdict": r["verdict"], "exit": r["exit"],
                "legs": {k: v[0] for k, v in r["legs"].items()},
                "detail": {k: v[1] for k, v in r["legs"].items() if v[0] == "FAIL"}}
            cells.append("%-26s" % ("%s e%d" % (r["verdict"].replace("ACCEPT-CA-65: ", ""), r["exit"])))
        print("%-28s %s" % (name, " ".join(cells)))

    report["instrument_hash_after"] = sha(SRC)
    out = os.path.join(STAGE, "results.json")
    write(out, json.dumps(report, indent=2, sort_keys=True) + "\n")
    print("\ninstrument sha256 before=%s after=%s" %
          (report["instrument_hash_before"], report["instrument_hash_after"]))
    print("results: " + out)


if __name__ == "__main__":
    main()
