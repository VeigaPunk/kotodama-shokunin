#!/usr/bin/env python3
r"""Round-83 counter for claim D (depth): the marriage-alliance entry.

Grades committed bytes at --lands against constants read at --freeze
(reports/round-83/claims.json claim D).

Legs (frozen):
  FROZENCFG   lands claims.json bytes == freeze claims.json bytes
  BEFORE      at base: the entry is absent, 256 knowledge files, 832 registry
              rows, and the filename sweep finds 0 owning files
  ENTRY       the entry exists at lands with >= the frozen minimum bytes and
              every frozen header marker
  SECTIONS    >= the frozen minimum `## ` headings and >= the frozen minimum
              decision-table rows in the decisions section
  ANCHORS     the anchors section carries >= the frozen minimum `- ` bullets,
              each with exactly one distinct S-id
  LINT        tools/check-cited-lines.py at lands over the entry exits 0 with
              `CITED-LINES: 0 finding(s)`
  ROWS        the registry grew by >= the frozen minimum; each frozen new id
              carries 11 cells, status mined, opened the frozen date, used-by the
              entry
  SOURCED     every S-id the entry cites exists at lands, and at least three of
              them are rows added this round
  SEPARABLE   base..lands carries every own path and no foreign claim's path
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import counterlib as C  # noqa: E402

LABEL = "ACCEPT-D-83"
CLAIMS = "reports/round-83/claims.json"
LEGS = ["FROZENCFG", "BEFORE", "ENTRY", "SECTIONS", "ANCHORS", "LINT", "ROWS", "SOURCED", "SEPARABLE"]
ROW = re.compile(r"^\s{0,3}\|\s*(S\d{3,})\s*\|")
SID = re.compile(r"S\d{3,}")


def read(path):
    if not os.path.isfile(path):
        return ""
    with open(path, encoding="utf-8") as f:
        return f.read()


def parse_registry(text):
    rows = {}
    for ln, l in enumerate(text.splitlines(), 1):
        m = ROW.match(l)
        if not m:
            continue
        cells = [c.strip() for c in l.strip().strip("|").split("|")]
        rows[m.group(1)] = (cells, ln)
    return rows


def knowledge_files(root, rev):
    return [p for p in C.tree_paths(root, rev, "corpus/knowledge") if p.endswith(".md")]


def anchors_block(text, heading):
    lines = text.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == heading)
    except StopIteration:
        return None
    out = []
    for l in lines[start + 1:]:
        if l.startswith("## "):
            break
        out.append(l)
    return out


def evaluate(root, lands, freeze, work, cfg, block):
    g = C.Grader(LABEL, block["legs"])
    base = cfg["base"]
    tree = os.path.join(work, "tree")
    entry = block["entry_path"]
    C.materialize(root, lands, tree, [entry, "corpus/SOURCES.md", block["cited_lines_tool"]])
    C.materialize(root, base, os.path.join(work, "base"), ["corpus/SOURCES.md"])
    et = read(os.path.join(tree, entry))
    reg = parse_registry(read(os.path.join(tree, "corpus/SOURCES.md")))
    breg = parse_registry(read(os.path.join(work, "base", "corpus/SOURCES.md")))

    def frozen():
        bf = C.show(root, freeze, CLAIMS)
        bl = C.show(root, lands, CLAIMS)
        if bf is None or bl is None:
            return False, "claims.json missing at freeze or lands"
        return (bf == bl, "sha256 %s" % C.sha256(bl)[:12])

    def before():
        abs_ = C.show(root, base, entry) is None
        kf = knowledge_files(root, base)
        owning = [p for p in kf if re.search(r"marriage|bride|dowry|wedding|spouse|betroth", os.path.basename(p), re.I)]
        ok = abs_ and len(kf) == block["base_knowledge_files"] and len(breg) == block["base_registry_rows"] and not owning
        return ok, "absent=%s knowledge=%d registry=%d owning_files=%d" % (abs_, len(kf), len(breg), len(owning))

    def entry_leg():
        b = C.show(root, lands, entry)
        if b is None:
            return False, "absent"
        head = re.split(r"(?m)^## ", et, maxsplit=1)[0]
        miss = [m for m in block["header_markers"] if m not in head]
        return (len(b) >= block["min_bytes"] and not miss, "bytes=%d missing_header=%s" % (len(b), miss or "none"))

    def sections():
        heads = [l for l in et.splitlines() if l.startswith("## ")]
        try:
            s = next(i for i, l in enumerate(et.splitlines()) if l.strip() == "## 2. Six design decisions")
            e = next(i for i in range(s + 1, len(et.splitlines())) if et.splitlines()[i].startswith("## "))
            dec_rows = [l for l in et.splitlines()[s + 1:e] if l.startswith("| ") and not set(l.replace("|", "").strip()) <= set("-: ")]
        except StopIteration:
            dec_rows = []
        ok = len(heads) >= block["min_sections"] and len(dec_rows) >= block["min_decision_rows"]
        return ok, "sections=%d floor=%d decision_rows=%d floor=%d" % (len(heads), block["min_sections"], len(dec_rows), block["min_decision_rows"])

    def anchors():
        blk = anchors_block(et, block["anchors_heading"])
        if blk is None:
            return False, "anchors heading absent"
        bullets = [l for l in blk if l.startswith("- ")]
        bad = []
        for l in bullets:
            ids = sorted(set(SID.findall(l)))
            if len(ids) != 1:
                bad.append((l[:40], ids))
        return (len(bullets) >= block["min_anchors"] and not bad,
                "bullets=%d floor=%d multi_or_zero=%d" % (len(bullets), block["min_anchors"], len(bad)))

    def lint():
        rc, out, err = C.run_py(os.path.join(tree, block["cited_lines_tool"]), [os.path.join(tree, entry)], cwd=tree)
        line = C.one_line(out, r"^CITED-LINES: 0 finding\(s\) in \d+ file\(s\)$")
        return (rc == 0 and line is not None, "rc=%d %r" % (rc, (out or err).strip().splitlines()[-1][:140] if (out or err).strip() else ""))

    def rows_leg():
        grew = len(reg) - len(breg)
        bad = []
        for rid in block["new_row_ids"]:
            if rid not in reg:
                bad.append((rid, "absent"))
                continue
            cells, ln = reg[rid]
            if len(cells) != 11:
                bad.append((rid, "cells=%d" % len(cells)))
            elif cells[7] != "mined":
                bad.append((rid, "status=%r" % cells[7]))
            elif cells[8] != block["opened"]:
                bad.append((rid, "opened=%r" % cells[8]))
            elif entry not in cells[10]:
                bad.append((rid, "used-by=%r" % cells[10][:40]))
        return (grew >= block["min_new_rows"] and not bad, "grew=%d floor=%d bad=%s" % (grew, block["min_new_rows"], bad or "none"))

    def sourced():
        cited = sorted(set(SID.findall(et)))
        unknown = [s for s in cited if s not in reg]
        new_cited = [s for s in cited if s in block["new_row_ids"]]
        return (not unknown and len(new_cited) >= 3, "cited=%d unknown=%s new_cited=%s" % (len(cited), unknown or "none", len(new_cited)))

    def separable():
        ch = C.changed_paths(root, base, lands)
        own_missing = [p for p in block["own_paths"] if not any(c == p or c.startswith(p) for c in ch)]
        foreign = [p for p in block["foreign_paths"] if any(c == p or c.startswith(p.rstrip("/") + "/") for c in ch)]
        return (not own_missing and not foreign, "own_missing=%s foreign=%s" % (own_missing or "none", foreign or "none"))

    g.grade("FROZENCFG", frozen)
    g.grade("BEFORE", before)
    g.grade("ENTRY", entry_leg)
    g.grade("SECTIONS", sections)
    g.grade("ANCHORS", anchors)
    g.grade("LINT", lint)
    g.grade("ROWS", rows_leg)
    g.grade("SOURCED", sourced)
    g.grade("SEPARABLE", separable)
    return g


def junk_battery(root, lands, freeze, work, cfg, block):
    import subprocess
    dest = os.path.join(work, "junk")
    C.clone_at(root, lands, dest)
    entry = block["entry_path"]
    et = C.show(root, lands, entry)
    if et is None:
        print("JUNK-D-83: FAIL 0/3 (entry absent at lands)")
        return 1
    text = et.decode("utf-8")
    results = []

    def trial(name, mutate, expect):
        subprocess.run(["git", "-C", dest, "reset", "-q", "--hard", lands], check=True)
        try:
            new = mutate()
        except C.NoOp as e:
            results.append((name, expect, False))
            print("JUNK %-18s expect %-10s killed=False (no-op fixture: %s)" % (name, expect, e))
            return
        w = os.path.join(work, "junkwork-" + name)
        os.makedirs(w, exist_ok=True)
        g = evaluate(dest, new, freeze, w, cfg, block)
        leg = dict(g.rows)
        ok = leg.get(expect) is False
        results.append((name, expect, ok))
        print("JUNK %-18s expect %-10s killed=%s" % (name, expect, ok))

    def m_stub():
        return C.fixture_commit(dest, entry, "# stub\n\n" + "- topic: stub\n", "junk: entry stub")

    def m_anchor():
        lines = text.splitlines()
        killed = False
        out = []
        for l in lines:
            if not killed and l.startswith("- ") and SID.search(l):
                killed = True
                continue
            out.append(l)
        return C.fixture_commit(dest, entry, "\n".join(out) + "\n", "junk: one anchor bullet dropped")

    def m_row():
        so = C.show(root, lands, "corpus/SOURCES.md").decode("utf-8")
        rid = block["new_row_ids"][0]
        out = []
        for l in so.splitlines():
            if l.startswith("| %s |" % rid):
                cells = l.strip().strip("|").split("|")
                cells[10] = " —"
                out.append("|" + "|".join(cells) + "|")
            else:
                out.append(l)
        return C.fixture_commit(dest, "corpus/SOURCES.md", "\n".join(out) + "\n", "junk: new row used-by cleared")

    trial("entry-stub", m_stub, "ENTRY")
    trial("anchor-dropped", m_anchor, "ANCHORS")
    trial("row-usedby", m_row, "ROWS")
    ok = all(r[2] for r in results)
    print("JUNK-D-83: %s %d/%d" % ("PASS" if ok else "FAIL", sum(1 for r in results if r[2]), len(results)))
    return 0 if ok else 1


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--lands", required=True)
    ap.add_argument("--freeze", required=True)
    ap.add_argument("--work", required=True)
    ap.add_argument("--junk", action="store_true")
    a = ap.parse_args()
    try:
        if not C.rev_ok(a.lands) or not C.rev_ok(a.freeze):
            raise C.Refuse("revision is not 40-hex")
        if not os.path.isdir(a.work):
            raise C.Refuse("--work is not an existing directory")
        cfg = C.load_config(a.root, a.freeze, CLAIMS)
        _, block = C.claim_config(cfg, "D")
        if block["legs"] != LEGS:
            raise C.Refuse("LEGCOUNT: frozen leg table differs from this counter")
        if a.lands == cfg["base"]:
            raise C.Refuse("lands equals the frozen base -- do-nothing control")
        if not C.is_ancestor(a.root, a.freeze, a.lands):
            raise C.Refuse("freeze is not an ancestor of lands")
        if not a.junk and not C.is_ancestor(a.root, a.lands, "main"):
            raise C.Refuse("lands is not an ancestor of the branch tip")
    except C.Refuse as e:
        return C.refuse(LABEL, LEGS, e)
    if a.junk:
        return junk_battery(a.root, a.lands, a.freeze, a.work, cfg, block)
    g = evaluate(a.root, a.lands, a.freeze, a.work, cfg, block)
    return g.finish()


if __name__ == "__main__":
    sys.exit(main())
