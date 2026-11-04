#!/usr/bin/env python3
r"""Round-83 counter for claim C (calibration): QUALITY 31 + the routed record repairs.

Grades committed bytes at --lands against constants read at --freeze
(reports/round-83/claims.json claim C).

Legs (frozen):
  FROZENCFG   lands claims.json bytes == freeze claims.json bytes
  BEFORE      at base: no `^31. ` criterion, a 0-byte round-82 record, no checker
  CRITERION   exactly one `^31. ` criterion carrying the three frozen clauses
  RECORD      the round-82 record is nonempty and names both revision hashes
  ERRATUM     the named erratum exists and carries its three markers
  SUPERSEDE   a row's teaches opens `supersedes S908 —`, carries `REJECTED:` and
              a `chapter III` anchor; S908's own cells 0..6 are unchanged
  CHECKER     the checker exists, --selftest is green at the frozen floor, and a
              run over the materialised lands tree prints `CITED-RECORDS: 0 empty
              / 0 scratch` exit 0
  APPENDONLY  across base..lands every registry row present in both keeps cells
              0..6; no id disappears
  SEPARABLE   base..lands carries every own path and no foreign claim's path
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import counterlib as C  # noqa: E402

LABEL = "ACCEPT-C-83"
CLAIMS = "reports/round-83/claims.json"
LEGS = ["FROZENCFG", "BEFORE", "CRITERION", "RECORD", "ERRATUM", "SUPERSEDE", "CHECKER", "APPENDONLY", "SEPARABLE"]
ROW = re.compile(r"^\s{0,3}\|\s*(S\d{3,})\s*\|")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def parse_registry(text):
    rows = {}
    for ln, l in enumerate(text.splitlines(), 1):
        m = ROW.match(l)
        if m:
            rows[m.group(1)] = ([c.strip() for c in l.strip().strip("|").split("|")], ln)
    return rows


def round83_docs(root, rev):
    docs = [p for p in C.tree_paths(root, rev, "reports/round-83") if p.endswith(".md")]
    docs += [p for p in C.tree_paths(root, rev, "corpus/lessons") if re.match(r"corpus/lessons/round-83[^/]*\.md$", p)]
    return docs


def evaluate(root, lands, freeze, work, cfg, block):
    g = C.Grader(LABEL, block["legs"])
    base = cfg["base"]
    tree = os.path.join(work, "tree")
    C.materialize(root, lands, tree,
                  [block["criterion_file"], "corpus/SOURCES.md", block["record_path"],
                   block["erratum_path"], block["checker_path"], "corpus/QUALITY.md"] + round83_docs(root, lands))
    C.materialize(root, base, os.path.join(work, "base"), ["corpus/SOURCES.md", "corpus/QUALITY.md"])
    bq = read(os.path.join(work, "base", "corpus/QUALITY.md"))
    q = read(os.path.join(tree, "corpus/QUALITY.md"))
    reg = parse_registry(read(os.path.join(tree, "corpus/SOURCES.md")))
    breg = parse_registry(read(os.path.join(work, "base", "corpus/SOURCES.md")))

    def frozen():
        bf = C.show(root, freeze, CLAIMS)
        bl = C.show(root, lands, CLAIMS)
        if bf is None or bl is None:
            return False, "claims.json missing at freeze or lands"
        return (bf == bl, "sha256 %s" % C.sha256(bl)[:12])

    def before():
        no_crit = not re.search(block["criterion_marker"], bq, re.M)
        rec = C.blob_size(root, base, block["record_path"])
        no_checker = C.show(root, base, block["checker_path"]) is None
        return (no_crit and rec == 0 and no_checker, "criterion_at_base=%s record_bytes=%d checker_at_base=%s"
                % (not no_crit, rec, not no_checker))

    def criterion():
        hits = [l for l in q.splitlines() if re.match(block["criterion_marker"], l)]
        if len(hits) != 1:
            return False, "criterion lines=%d" % len(hits)
        started = False
        blk = []
        for l in q.splitlines():
            if re.match(block["criterion_marker"], l):
                started = True
            elif started and re.match(r"^3[2-9]\. ", l):
                break
            if started:
                blk.append(l)
        body = "\n".join(blk)
        miss = [m for m in block["criterion_markers"] if m.lower() not in body.lower()]
        return (not miss and len(body) >= 400, "bytes=%d missing_markers=%s" % (len(body), miss or "none"))

    def record():
        b = C.show(root, lands, block["record_path"])
        if b is None:
            return False, "record absent"
        txt = b.decode("utf-8", "replace")
        miss = [h for h in block["record_hashes"] if h not in txt]
        return (len(b) >= block["record_min_bytes"] and not miss, "bytes=%d missing_hashes=%s" % (len(b), miss or "none"))

    def erratum():
        p = os.path.join(tree, block["erratum_path"])
        if not os.path.isfile(p):
            return False, "erratum absent"
        txt = read(p)
        miss = [m for m in block["erratum_markers"] if m not in txt]
        return (not miss, "missing_markers=%s" % (miss or "none"))

    def supersede():
        hit = [(rid, cells) for rid, (cells, _) in reg.items() if len(cells) > 6 and cells[6].startswith(block["supersede_prefix"])]
        if len(hit) != 1:
            return False, "superseding rows=%d" % len(hit)
        rid, cells = hit[0]
        miss = [m for m in block["supersede_markers"] if m not in cells[6] + " " + (cells[5] if len(cells) > 5 else "")]
        old_ok = block["superseded_id"] in reg and block["superseded_id"] in breg and \
            reg[block["superseded_id"]][0][:7] == breg[block["superseded_id"]][0][:7]
        return (not miss and old_ok, "row=%s missing=%s superseded_cells_unchanged=%s" % (rid, miss or "none", old_ok))

    def checker():
        tp = os.path.join(tree, block["checker_path"])
        rc, out, err = C.run_py(tp, ["--selftest"], cwd=tree)
        line = C.one_line(out, r"^SELFTEST: PASS \((\d+) checks\)$")
        n = int(re.match(r"^SELFTEST: PASS \((\d+) checks\)$", line).group(1)) if line else -1
        rc2, out2, err2 = C.run_py(tp, ["--root", tree, "--from-round", str(block["from_round"])], cwd=tree)
        summ = C.one_line(out2, block["checker_summary_re"])
        m = re.match(block["checker_summary_re"], summ) if summ else None
        shape = C.show(root, lands, block["checker_path"]).decode("utf-8", "replace")
        marks = [k for k in block["checker_shape_markers"] if k not in shape]
        ok = (rc == 0 and n >= block["checker_min_selftest_checks"] and rc2 == 0 and m is not None
              and int(m.group(1)) == 0 and int(m.group(2)) == 0 and not marks)
        return ok, "selftest_rc=%d checks=%d floor=%d scan_rc=%d summary=%r missing_markers=%s" % (
            rc, n, block["checker_min_selftest_checks"], rc2, summ, marks or "none")

    def appendonly():
        removed = [rid for rid in breg if rid not in reg]
        changed = [rid for rid in reg if rid in breg and reg[rid][0][:7] != breg[rid][0][:7]]
        return (not removed and not changed, "removed=%s changed_cells0to6=%s" % (removed or "none", changed or "none"))

    def separable():
        ch = C.changed_paths(root, base, lands)
        own_missing = [p for p in block["own_paths"] if not any(c == p or c.startswith(p) for c in ch)]
        foreign = [p for p in block["foreign_paths"] if any(c == p or c.startswith(p.rstrip("/") + "/") for c in ch)]
        return (not own_missing and not foreign, "own_missing=%s foreign=%s" % (own_missing or "none", foreign or "none"))

    g.grade("FROZENCFG", frozen)
    g.grade("BEFORE", before)
    g.grade("CRITERION", criterion)
    g.grade("RECORD", record)
    g.grade("ERRATUM", erratum)
    g.grade("SUPERSEDE", supersede)
    g.grade("CHECKER", checker)
    g.grade("APPENDONLY", appendonly)
    g.grade("SEPARABLE", separable)
    return g


def junk_battery(root, lands, freeze, work, cfg, block):
    import subprocess
    dest = os.path.join(work, "junk")
    C.clone_at(root, lands, dest)
    results = []

    def trial(name, mutate, expect):
        subprocess.run(["git", "-C", dest, "reset", "-q", "--hard", lands], check=True)
        new = mutate()
        w = os.path.join(work, "junkwork-" + name)
        os.makedirs(w, exist_ok=True)
        g = evaluate(dest, new, freeze, w, cfg, block)
        leg = dict(g.rows)
        ok = leg.get(expect) is False
        results.append((name, expect, ok))
        print("JUNK %-18s expect %-10s killed=%s" % (name, expect, ok))

    def m_record():
        return C.fixture_commit(dest, block["record_path"], "", "junk: empty the record again")

    def m_crit():
        q = C.show(root, lands, "corpus/QUALITY.md").decode("utf-8")
        out = [l for l in q.splitlines() if not re.match(block["criterion_marker"], l)]
        return C.fixture_commit(dest, "corpus/QUALITY.md", "\n".join(out) + "\n", "junk: criterion line removed")

    def m_rowedit():
        so = C.show(root, lands, "corpus/SOURCES.md").decode("utf-8")
        out = []
        for l in so.splitlines():
            if l.startswith("| %s |" % block["superseded_id"]):
                cells = l.strip().strip("|").split("|")
                cells[6] = " rewritten in place"
                out.append("|" + "|".join(cells) + "|")
            else:
                out.append(l)
        return C.fixture_commit(dest, "corpus/SOURCES.md", "\n".join(out) + "\n", "junk: in-place rewrite of an existing row")

    trial("record-emptied", m_record, "RECORD")
    trial("criterion-gone", m_crit, "CRITERION")
    trial("row-rewritten", m_rowedit, "APPENDONLY")
    ok = all(r[2] for r in results)
    print("JUNK-C-83: %s %d/%d" % ("PASS" if ok else "FAIL", sum(1 for r in results if r[2]), len(results)))
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
        _, block = C.claim_config(cfg, "C")
        if block["legs"] != LEGS:
            raise C.Refuse("LEGCOUNT: frozen leg table differs from this counter")
        if not C.is_ancestor(a.root, a.freeze, a.lands):
            raise C.Refuse("freeze is not an ancestor of lands")
        if a.lands == cfg["base"]:
            raise C.Refuse("lands equals the frozen base -- do-nothing control")
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
