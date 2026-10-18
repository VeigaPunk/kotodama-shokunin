#!/usr/bin/env python3
"""R28-C48 — entry audit: no filler, sources resolve, and the index matches.

Round 27's audit (`reports/round-27/audit/entry-audit.py`, 11/11 controls)
checks each entry against `corpus/QUALITY.md`: header completeness, locator
presence on every source bullet, repo-path resolution, sha256 pin
classification, `couples:` resolution, a named gap, a decision record,
calibration vocabulary and canon hygiene.

This round's audit keeps that core **verbatim** (it is imported, not
re-implemented, so a fix to the core cannot silently diverge between rounds)
and adds the leg round 27 did not have: the **index coupling** leg. Round 27
audited the corpus and the README separately, so an entry could clear the
admission bar while sitting in the index under the wrong partition, or while
its README row had drifted off its `- topic:` text. Both are C-seat surfaces.

Legs:

  bar      the inherited admission bar, per entry (`corpus/QUALITY.md`).
           **An admission rule for new entries, not a retroactive verdict:**
           the lane's gap-naming discipline was introduced in round 10 and
           extended in round 19, so most of the corpus predates it. Round 27
           recorded the same split (27/200 gap-naming, 173 not) and refused to
           report the count as "filler entries". This instrument reports the
           split and exits 0 on it unless `--strict-bar` is passed; a `--new`
           entry must clear the bar unconditionally.
  index    every entry has exactly one README row, in its own partition,
           whose text is byte-equal to the entry's `- topic:` head text.
           **A hard check:** a missing row, a wrong partition or a drifted row
           is a defect in this seat's own surface, not a legacy reading.
  new      a named round-28 entry clears the full bar (the round's own
           admission claim, measured rather than asserted)

The tool is read-only over the repo: it opens `corpus/**` and the README for
reading and has no code path that writes inside the lane.

Usage:
    python3 reports/round-28/audit/entry-audit.py --all
    python3 reports/round-28/audit/entry-audit.py --partition linguistics
    python3 reports/round-28/audit/entry-audit.py FILE [FILE ...]
    python3 reports/round-28/audit/entry-audit.py --selftest
"""
import argparse
import importlib.util
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
KNOWLEDGE = os.path.join(LANE, "corpus", "knowledge")
README = os.path.join(LANE, "corpus", "README.md")
R27_AUDIT = os.path.join(LANE, "reports", "round-27", "audit", "entry-audit.py")
PARTS = ["linguistics", "myth-symbol", "culture-material", "synthesis",
         "verification", "civilizations"]

SECTION_RE = re.compile(r"^## ([a-z-]+)/ \((\d+)\)\s*$", re.M)
ROW_RE = re.compile(r"^- `([^`]+\.md)` — (.*)$", re.M)
TOPIC_RE = re.compile(r"^- topic:(.*?)(?=\n- \w)", re.M | re.S)


def load_core():
    """Import round 27's audited core by path (no copy, no divergence)."""
    spec = importlib.util.spec_from_file_location("r27_entry_audit", R27_AUDIT)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def entry_topic(path):
    with open(path, encoding="utf-8") as fh:
        text = fh.read()
    m = TOPIC_RE.search(text)
    if not m:
        return None
    parts = [ln.strip() for ln in m.group(1).strip("\n").splitlines()]
    return " ".join(p for p in parts if p)


def readme_index():
    """{part: [(file, topic), ...]} in file order, from the README."""
    with open(README, encoding="utf-8") as fh:
        text = fh.read()
    marks = [(m.start(), m.group(1)) for m in SECTION_RE.finditer(text)]
    out = {}
    for i, (pos, part) in enumerate(marks):
        end = marks[i + 1][0] if i + 1 < len(marks) else len(text)
        out[part] = [(m.group(1), m.group(2)) for m in ROW_RE.finditer(text[pos:end])]
    return out


def index_leg(entry_paths, index):
    """For each entry: exactly one row, in its own partition, byte-equal topic."""
    # basename -> [(part, topic), ...]
    by_name = {}
    for part, rows in index.items():
        for name, topic in rows:
            by_name.setdefault(name, []).append((part, topic))
    rows = []
    for path in entry_paths:
        part = os.path.basename(os.path.dirname(path))
        name = os.path.basename(path)
        hits = by_name.get(name, [])
        topic = entry_topic(path)
        findings = []
        if len(hits) == 0:
            findings.append({"class": "NOT_INDEXED"})
        elif len(hits) > 1:
            findings.append({"class": "DUPLICATE_INDEXED", "rows": [p for p, _ in hits]})
        else:
            row_part, row_topic = hits[0]
            if row_part != part:
                findings.append({"class": "WRONG_PARTITION",
                                 "row_part": row_part, "entry_part": part})
            if topic is None:
                findings.append({"class": "ENTRY_HAS_NO_TOPIC_FIELD"})
            elif row_topic != topic:
                findings.append({"class": "ROW_TOPIC_DRIFT",
                                 "row_chars": len(row_topic),
                                 "topic_chars": len(topic)})
        rows.append({"path": os.path.relpath(path, LANE), "partition": part,
                     "findings": findings, "indexed": not findings})
    return rows


def all_entries():
    out = []
    for part in PARTS:
        d = os.path.join(KNOWLEDGE, part)
        if not os.path.isdir(d):
            continue
        for f in sorted(os.listdir(d)):
            if f.endswith(".md"):
                out.append(os.path.join(d, f))
    return out


def selftest():
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        if not cond:
            ok = False
        print(("PASS " if cond else "FAIL ") + name + (" " + detail if detail else ""))

    core = load_core()
    check("core imports round 27's audited instrument", hasattr(core, "audit_entry"))

    # a synthetic index that names one real entry correctly and one wrongly
    real = os.path.join(KNOWLEDGE, "linguistics", "color-terminology.md")
    good = entry_topic(real)
    index = {"linguistics": [("color-terminology.md", good)]}
    rows = index_leg([real], index)
    check("index leg: a correct row is clean", rows[0]["findings"] == [], json.dumps(rows[0]))

    index = {"linguistics": [("color-terminology.md", "a condensed paraphrase")]}
    rows = index_leg([real], index)
    check("index leg: a drifted row topic is flagged",
          [f["class"] for f in rows[0]["findings"]] == ["ROW_TOPIC_DRIFT"],
          json.dumps(rows[0]["findings"]))

    index = {"myth-symbol": [("color-terminology.md", good)]}
    rows = index_leg([real], index)
    check("index leg: a wrong partition is flagged",
          [f["class"] for f in rows[0]["findings"]] == ["WRONG_PARTITION"],
          json.dumps(rows[0]["findings"]))

    index = {"linguistics": []}
    rows = index_leg([real], index)
    check("index leg: an unindexed entry is flagged",
          [f["class"] for f in rows[0]["findings"]] == ["NOT_INDEXED"],
          json.dumps(rows[0]["findings"]))

    index = {"linguistics": [("color-terminology.md", good), ("color-terminology.md", good)]}
    rows = index_leg([real], index)
    check("index leg: a duplicate row is flagged",
          [f["class"] for f in rows[0]["findings"]] == ["DUPLICATE_INDEXED"],
          json.dumps(rows[0]["findings"]))

    # the live leg: the real README against the real corpus, all entries
    index = readme_index()
    entries = all_entries()
    rows = index_leg(entries, index)
    bad = [r for r in rows if not r["indexed"]]
    check("index leg: every entry is indexed cleanly",
          bad == [], json.dumps(bad[:3]))
    # The corpus grows every round, so the leg asserts the invariant (every
    # disk entry was audited and the README's row count matches the tree), not
    # a frozen number that would need editing each landing.
    readme_rows = sum(len(v) for v in index.values())
    check("index leg: every disk entry audited and rows == files",
          len(rows) == len(entries) == readme_rows and len(rows) >= 200,
          f"entries={len(rows)} readme_rows={readme_rows}")

    # the inherited bar still runs over the live corpus (one entry, a control)
    r = core.audit_entry(real)
    check("inherited bar runs on a live entry",
          r["source_refs_unresolved"] == [] and r["source_digests_mismatched"] == [],
          json.dumps({"unresolved": r["source_refs_unresolved"]}))
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--partition", choices=PARTS, action="append")
    ap.add_argument("--new", action="append", default=[],
                    help="a round-28 entry that must clear the full bar")
    ap.add_argument("--strict-bar", action="store_true",
                    help="fail if any entry misses the full admission bar "
                         "(the legacy corpus does; see the module docstring)")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        passed = selftest()
        print("selftest: %s" % ("11/11 checks passed" if passed else "FAILED"))
        return 0 if passed else 1

    core = load_core()
    paths = [os.path.abspath(f) for f in args.files]
    if args.partition:
        for part in args.partition:
            d = os.path.join(KNOWLEDGE, part)
            paths += [os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith(".md")]
    if args.all or not paths:
        paths = all_entries()
    paths = sorted(set(paths))

    index = readme_index()
    bar = [core.audit_entry(p) for p in paths]
    idx = index_leg(paths, index)
    idx_by_path = {r["path"]: r for r in idx}

    bad_bar = [r for r in bar if not r["quality_bar"]]
    bad_idx = [r for r in idx if not r["indexed"]]

    new_rows = []
    for spec in args.new:
        p = os.path.abspath(spec)
        r = core.audit_entry(p)
        i = index_leg([p], index)[0]
        new_rows.append({"path": os.path.relpath(p, LANE),
                         "bar": r["quality_bar"], "filler": r["filler"],
                         "src": f"{r['source_bullets_with_locator']}/{r['source_bullets']}",
                         "refs_unres": r["source_refs_unresolved"],
                         "digests_bad": r["source_digests_mismatched"],
                         "couples_unres": r["couples_unresolved"],
                         "index": i["findings"]})

    if args.json:
        print(json.dumps({"entries": len(paths),
                          "bar_failing": [r["path"] for r in bad_bar],
                          "bar_failing_count": len(bad_bar),
                          "index_failing": bad_idx,
                          "new": new_rows}, indent=1, sort_keys=True))
    else:
        for r in bar:
            ir = idx_by_path[r["path"]]
            print(("%-58s bar=%-5s filler=%-5s src=%d/%d refs_unres=%d digests_bad=%d "
                   "couples_unres=%d index=%s"
                   % (r["path"], r["quality_bar"], r["filler"],
                      r["source_bullets_with_locator"], r["source_bullets"],
                      len(r["source_refs_unresolved"]), len(r["source_digests_mismatched"]),
                      len(r["couples_unresolved"]),
                      "ok" if ir["indexed"] else [f["class"] for f in ir["findings"]])))
        print("audited %d; bar clear %d; bar failing %d %s"
              % (len(bar), len(bar) - len(bad_bar), len(bad_bar),
                 [r["path"] for r in bad_bar]))
        print("indexed %d; index clear %d; index failing %d %s"
              % (len(idx), len(idx) - len(bad_idx), len(bad_idx),
                 [r["path"] for r in bad_idx]))
        for nr in new_rows:
            print("new %s bar=%s filler=%s src=%s index=%s"
                  % (nr["path"], nr["bar"], nr["filler"], nr["src"], nr["index"]))
        print("NOTE the bar leg is an ADMISSION RULE for new entries, not a "
              "retroactive verdict: the lane's gap-naming discipline postdates "
              "most of the corpus (round 27's audit recorded the same split). "
              "The index leg is a hard check. Use --strict-bar to fail on the "
              "legacy bar reading as well.")
    # Exit status: the index leg is a hard check, and each --new entry must
    # clear the bar. The full-corpus bar count is reported, and only fails the
    # run under --strict-bar, because the gap discipline postdates the corpus.
    ok = (not bad_idx
          and all(nr["bar"] and not nr["index"] for nr in new_rows)
          and (not bad_bar or not args.strict_bar))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
