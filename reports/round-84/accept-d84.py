#!/usr/bin/env python3
r"""Round-84 counter for claim D (depth): the witchcraft-and-sorcery accusation entry.

Grades committed bytes at --lands against constants read at --freeze
(reports/round-84/claims.json claim D).

Legs (frozen):
  FROZENCFG   lands claims.json bytes == freeze claims.json bytes
  BEFORE      at base: the entry is absent, corpus/knowledge holds the frozen
              file count, the registry holds the frozen row count, and no
              knowledge basename matches the frozen surface regex
  ENTRY       the entry exists at lands, >= the frozen byte floor, and carries
              every frozen header marker
  SECTIONS    the entry carries >= the frozen number of `## ` sections
  DECISIONS   `## 2. The decision table` carries >= the frozen data rows
  ANCHORS     `## 4. Attested anchors` carries >= the frozen bullet count, each
              bullet naming exactly one distinct S-id, across >= the frozen
              number of distinct ids
  LINT        `tools/check-cited-lines.py <entry>` at lands = 0 findings, exit 0
  ROWS        the registry grew by >= the frozen minimum; every frozen new id is
              an 11-cell row with status `mined`, the frozen `opened` date and a
              `used-by` cell naming the entry
  SOURCED     the entry cites >= (frozen new rows - 1) of the frozen new ids
  SEPARABLE   base..lands carries every own path and no foreign claim's path moved
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import counterlib as C  # noqa: E402

CLAIM_ID = "D"
LABEL = "ACCEPT-D-84"
CLAIMS = "reports/round-84/claims.json"
LEGS = ["FROZENCFG", "BEFORE", "ENTRY", "SECTIONS", "DECISIONS", "ANCHORS", "LINT", "ROWS", "SOURCED", "SEPARABLE"]
SID = re.compile(r"\bS\d{3,}\b")
ROW_LINE = re.compile(r"^ {0,3}\| *S\d{3,} *\|")
LINT_SUMMARY = re.compile(r"^CITED-LINES: (\d+) finding")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def knowledge_files(root, rev):
    return [p for p in C.tree_paths(root, rev, "corpus/knowledge") if p.endswith(".md")]


def registry_rows(text):
    """(id, cells) for every row under the `## Registry` table, 0-3 leading spaces."""
    out = []
    for line in text.splitlines():
        if not ROW_LINE.match(line):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) != 11:
            out.append((cells[0] if cells else "?", []))
            continue
        out.append((cells[0], cells))
    return out


def section_lines(text, heading):
    lines = text.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == heading)
    except StopIteration:
        return None
    body = []
    for i in range(start + 1, len(lines)):
        if lines[i].startswith("## "):
            break
        body.append(lines[i])
    return body


def table_rows(body):
    rows = []
    seen_header = False
    for line in body:
        s = line.strip()
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if set("".join(cells)) <= set("-: "):
            continue
        if not seen_header:
            seen_header = True
            continue
        rows.append(cells)
    return rows


def evaluate(root, lands, freeze, work, cfg, block):
    g = C.Grader(LABEL, block["legs"])
    base = cfg["base"]
    tree = os.path.join(work, "tree")
    btree = os.path.join(work, "base")
    entry = block["entry_path"]

    C.materialize(root, lands, tree, [entry, "corpus/SOURCES.md", block["cited_lines_tool"]])
    C.materialize(root, base, btree, ["corpus/SOURCES.md"])

    base_rows = registry_rows(read(os.path.join(btree, "corpus/SOURCES.md")))
    lands_rows = registry_rows(read(os.path.join(tree, "corpus/SOURCES.md")))
    lands_ids = [i for i, cells in lands_rows if cells]
    base_ids = [i for i, cells in base_rows if cells]

    def frozen():
        bf = C.show(root, freeze, CLAIMS)
        bl = C.show(root, lands, CLAIMS)
        if bf is None or bl is None:
            return False, "claims.json missing at freeze or lands"
        return (bf == bl, "freeze %s lands %s sha256 %s" % (freeze[:8], lands[:8], C.sha256(bl)[:12]))

    def before():
        bfiles = knowledge_files(root, base)
        names = [os.path.basename(p) for p in bfiles]
        surf = re.compile(block["surface_re"])
        owned = [n for n in names if surf.search(n)]
        entry_at_base = C.show(root, base, entry) is not None
        ok = (not entry_at_base and len(bfiles) == block["base_knowledge_files"]
              and len(base_ids) == block["base_registry_rows"] and not owned)
        return ok, "entry_at_base=%s files=%d/%d rows=%d/%d owned=%s" % (
            entry_at_base, len(bfiles), block["base_knowledge_files"],
            len(base_ids), block["base_registry_rows"], owned or "none")

    def entry_leg():
        b = C.show(root, lands, entry)
        if b is None:
            return False, "entry absent at lands"
        text = b.decode("utf-8", "replace")
        missing = [m for m in block["header_markers"] if m not in text]
        return (not missing and len(b) >= block["min_bytes"],
                "bytes=%d/%d missing=%s" % (len(b), block["min_bytes"], missing or "none"))

    def sections():
        text = read(os.path.join(tree, entry))
        n = len([l for l in text.splitlines() if l.startswith("## ")])
        return (n >= block["min_sections"], "sections=%d floor=%d" % (n, block["min_sections"]))

    def decisions():
        text = read(os.path.join(tree, entry))
        body = section_lines(text, block["decision_heading"])
        if body is None:
            return False, "no %r section" % block["decision_heading"]
        rows = table_rows(body)
        return (len(rows) >= block["min_decision_rows"], "rows=%d floor=%d" % (len(rows), block["min_decision_rows"]))

    def anchors():
        text = read(os.path.join(tree, entry))
        body = section_lines(text, block["anchors_heading"])
        if body is None:
            return False, "no %r section" % block["anchors_heading"]
        bullets, bad, ids = 0, [], set()
        for line in body:
            if not line.startswith("- "):
                continue
            found = SID.findall(line)
            if len(found) != 1 or found[0] in bad:
                bad.append(line[:60])
                continue
            bullets += 1
            ids.add(found[0])
        ok = (len(bad) == 0 and bullets >= block["min_anchors"] and len(ids) >= block["min_distinct_ids"])
        return ok, "bullets=%d/%d ids=%d/%d malformed=%d" % (
            bullets, block["min_anchors"], len(ids), block["min_distinct_ids"], len(bad))

    def lint():
        rc, out, err = C.run_py(os.path.join(tree, block["cited_lines_tool"]), [entry], cwd=tree)
        hit = C.one_line(out, LINT_SUMMARY.pattern)
        if hit is None:
            return False, "no CITED-LINES summary: %r" % ((out or err).strip()[:160])
        k = int(re.match(LINT_SUMMARY.pattern, hit).group(1))
        return (rc == 0 and k == 0, "rc=%d findings=%d line=%r" % (rc, k, hit[:80]))

    def rows_leg():
        grew = len(lands_ids) - len(base_ids)
        problems = []
        by_id = {i: cells for i, cells in lands_rows if cells}
        for rid in block["new_row_ids"]:
            cells = by_id.get(rid)
            if not cells:
                problems.append("%s missing" % rid)
                continue
            if cells[7] != "mined":
                problems.append("%s status=%r" % (rid, cells[7]))
            if cells[8] != block["opened"]:
                problems.append("%s opened=%r" % (rid, cells[8]))
            if entry not in cells[10]:
                problems.append("%s used-by" % rid)
        ok = (grew >= block["min_new_rows"] and not problems)
        return ok, "rows=%d grew=%d floor=%d problems=%s" % (len(lands_ids), grew, block["min_new_rows"], problems or "none")

    def sourced():
        text = read(os.path.join(tree, entry))
        cited = [rid for rid in block["new_row_ids"] if rid in text]
        need = block["min_new_rows"] - 1
        return (len(cited) >= need, "cited=%s need=%d" % (cited, need))

    def separable():
        other = set()
        for c in cfg["claims"]:
            if c["id"] == CLAIM_ID:
                continue
            for v in c.values():
                if isinstance(v, dict) and v.get("own_paths"):
                    other.update(v["own_paths"])
        unique = [p for p in block["own_paths"] if p not in other]
        parent = C.claim_span(root, base, lands, unique)[1]
        cumulative = C.changed_paths(root, base, lands)
        own_missing = [p for p in unique if not any(c == p or c.startswith(p) for c in cumulative)]
        foreign = [p for p in block["foreign_paths"] if C.blob_sha(root, parent, p) != C.blob_sha(root, lands, p)]
        return (not own_missing and not foreign,
                "span_parent=%s own_missing=%s foreign_moved=%s" % (parent[:8], own_missing or "none", foreign or "none"))

    g.grade("FROZENCFG", frozen)
    g.grade("BEFORE", before)
    g.grade("ENTRY", entry_leg)
    g.grade("SECTIONS", sections)
    g.grade("DECISIONS", decisions)
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
    text = C.show(root, lands, entry).decode("utf-8")
    results = []

    def trial(name, mutate, expect):
        subprocess.run(["git", "-C", dest, "reset", "-q", "--hard", lands], check=True)
        try:
            new = mutate()
        except C.NoOp as e:
            results.append((name, expect, False))
            print("JUNK %-16s expect %-10s killed=False (no-op fixture: %s)" % (name, expect, e))
            return
        w = os.path.join(work, "junkwork-" + name)
        os.makedirs(w, exist_ok=True)
        g = evaluate(dest, new, freeze, w, cfg, block)
        leg = dict(g.rows)
        ok = leg.get(expect) is False
        results.append((name, expect, ok))
        print("JUNK %-16s expect %-10s killed=%s" % (name, expect, ok))

    def m_stub():
        return C.fixture_commit(dest, entry, "# stub\n\n" + ("x" * 200) + "\n", "junk: stub entry")

    def m_two_ids():
        lines = text.splitlines()
        out, done = [], False
        for line in lines:
            if not done and line.startswith("- ") and SID.search(line):
                line = line + " S917"
                done = True
            out.append(line)
        return C.fixture_commit(dest, entry, "\n".join(out) + "\n", "junk: anchor carries two ids")

    def m_queued():
        rows = C.show(root, lands, "corpus/SOURCES.md").decode("utf-8").splitlines()
        rid = block["new_row_ids"][0]
        out, done = [], False
        for line in rows:
            if not done and ROW_LINE.match(line) and line.strip().strip("|").split("|")[0].strip() == rid:
                cells = [c.strip() for c in line.strip().strip("|").split("|")]
                if len(cells) == 11:
                    cells[7] = "queued"
                    line = "| " + " | ".join(cells) + " |"
                    done = True
            out.append(line)
        return C.fixture_commit(dest, "corpus/SOURCES.md", "\n".join(out) + "\n", "junk: new row not mined")

    trial("stub-entry", m_stub, "ENTRY")
    trial("anchor-two-ids", m_two_ids, "ANCHORS")
    trial("row-queued", m_queued, "ROWS")
    ok = all(r[2] for r in results)
    print("JUNK-D-84: %s %d/%d" % ("PASS" if ok else "FAIL", sum(1 for r in results if r[2]), len(results)))
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
