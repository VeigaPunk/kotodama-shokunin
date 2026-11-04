#!/usr/bin/env python3
r"""Round-83 counter for claim O (operability): the gate-registry coverage auditor.

Grades committed bytes at --lands against constants read at --freeze
(reports/round-83/claims.json claim O).

Legs (frozen):
  FROZENCFG   lands claims.json bytes == freeze claims.json bytes
  BEFORE      at base: 58 accept-* counters, the frozen 11-item missing set,
              and no tools/check-gate-registry.py
  TOOL        the tool exists at lands, >= 4000 bytes, with the frozen shape markers
  SELFTEST    the lands tool bytes run --selftest to exit 0 with
              `SELFTEST: PASS (<n> checks)` and n >= the frozen floor
  REGISTRY    the lands tool over a materialised lands tree prints one summary
              line with 0 missing / 0 dead, exits 0, and its --json sets equal
              this counter's independent glob and parse (instruments, missing, dead)
  ROWS        every frozen base-missing counter and all three round-83 counters
              appear in the entry-command cell of some registry row
  DEAD        every .py path token in a registry row resolves in the materialised
              lands tree, and the row count grew by at least the frozen minimum
  SEPARABLE   base..lands carries every own path and no foreign claim's path
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import counterlib as C  # noqa: E402

LABEL = "ACCEPT-O-83"
CLAIMS = "reports/round-83/claims.json"
LEGS = ["FROZENCFG", "BEFORE", "TOOL", "SELFTEST", "REGISTRY", "ROWS", "DEAD", "SEPARABLE"]
TOKEN = re.compile(r"((?:tools|reports)/[A-Za-z0-9_./-]+\.py)")
INSTR = re.compile(r"^reports/[^/]+/accept-[^/]+\.py$")


def instrument_paths(root, rev):
    return [p for p in C.tree_paths(root, rev, "reports") if INSTR.match(p)]


def registry_rows(skill_text):
    """Rows of the `## Gates and probes` table: (cells, line number). Header row included."""
    lines = skill_text.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == "## Gates and probes")
    except StopIteration:
        return None
    rows = []
    for i in range(start + 1, len(lines)):
        s = lines[i].lstrip()
        if s.startswith("## ") and i > start + 1:
            break
        if not s.startswith("|"):
            continue
        cells = [c.strip() for c in s.strip().strip("|").split("|")]
        if len(cells) < 2:
            continue
        if set("".join(cells)) <= set("-: "):
            continue
        rows.append((cells, i + 1))
    return rows


def missing_of(instr, rows):
    return [p for p in instr if not any(p in cells[2] for cells, _ in rows if len(cells) > 2)]


def dead_of(rows, tree):
    dead = []
    for cells, ln in rows:
        if len(cells) < 3:
            continue
        for tok in TOKEN.findall(cells[2]):
            if not os.path.isfile(os.path.join(tree, tok)):
                dead.append((cells[0], tok, ln))
    return dead


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def evaluate(root, lands, freeze, work, cfg, block):
    g = C.Grader(LABEL, block["legs"])
    base = cfg["base"]
    tree = os.path.join(work, "tree")
    btree = os.path.join(work, "base")
    lands_inst = instrument_paths(root, lands)
    base_inst = instrument_paths(root, base)

    tools_py = [p for p in C.tree_paths(root, lands, "tools") if p.endswith(".py")]

    def prep_lands():
        C.materialize(root, lands, tree, [block["tool_path"], "SKILL.md"] + lands_inst + tools_py)

    def prep_base():
        C.materialize(root, base, btree, ["SKILL.md"] + base_inst)

    prep_lands()
    prep_base()
    base_rows = registry_rows(read(os.path.join(btree, "SKILL.md")))
    if base_rows is None:
        raise RuntimeError("base SKILL.md carries no ## Gates and probes")
    rows = registry_rows(read(os.path.join(tree, "SKILL.md")))
    if rows is None:
        raise RuntimeError("lands SKILL.md carries no ## Gates and probes")

    def frozen():
        bf = C.show(root, freeze, CLAIMS)
        bl = C.show(root, lands, CLAIMS)
        if bf is None or bl is None:
            return False, "claims.json missing at freeze or lands"
        return (bf == bl, "freeze %s lands %s sha256 %s" % (freeze[:8], lands[:8], C.sha256(bl)[:12]))

    def before():
        miss = set(missing_of(base_inst, base_rows))
        want = set(block["base_missing"])
        tool_at_base = C.show(root, base, block["tool_path"]) is not None
        ok = len(base_inst) == block["base_instruments"] and miss == want and not tool_at_base
        return ok, "instruments=%d missing=%d/%d tool_at_base=%s" % (len(base_inst), len(miss & want), len(want), tool_at_base)

    def tool():
        b = C.show(root, lands, block["tool_path"])
        if b is None:
            return False, "tool absent at lands"
        t = b.decode("utf-8", "replace")
        marks = [m for m in block["shape_markers"] if m not in t]
        return (not marks and len(b) >= 4000, "bytes=%d missing_markers=%s" % (len(b), marks or "none"))

    def selftest():
        tp = os.path.join(tree, block["tool_path"])
        rc, out, err = C.run_py(tp, ["--selftest"], cwd=tree)
        line = C.one_line(out, r"^SELFTEST: PASS \((\d+) checks\)$")
        n = int(re.match(r"^SELFTEST: PASS \((\d+) checks\)$", line).group(1)) if line else -1
        tail = ((out or err).strip().splitlines() or [""])[-1][:120]
        return (rc == 0 and n >= block["min_selftest_checks"], "rc=%d checks=%d floor=%d tail=%r" % (rc, n, block["min_selftest_checks"], tail))

    def registry():
        tp = os.path.join(tree, block["tool_path"])
        rc, out, err = C.run_py(tp, ["--root", tree, "--json"], cwd=tree)
        if rc != 0:
            return False, "tool --json exit %d: %r" % (rc, (out or err).strip()[:200])
        rc2, out2, err2 = C.run_py(tp, ["--root", tree], cwd=tree)
        line = C.one_line(out2, block["summary_re"])
        if line is None:
            return False, "no single summary line: %r" % out2.strip()[:200]
        miss, reg, ins, dead = (int(x) for x in re.match(block["summary_re"], line).groups())
        try:
            js = json.loads(out)
        except Exception:
            return False, "--json not JSON: %r" % out.strip()[:160]
        mine_miss = missing_of(lands_inst, rows)
        mine_dead = dead_of(rows, tree)
        ok = (rc2 == 0 and miss == 0 and dead == 0
              and reg >= len(rows) - 1
              and sorted(js.get("missing", [])) == sorted(mine_miss) == []
              and sorted(js.get("instruments", [])) == sorted(lands_inst)
              and ins == len(lands_inst) >= block["min_instruments_at_lands"]
              and not mine_dead and not js.get("dead"))
        return ok, "summary=(%d,%d,%d,%d) own=(miss=%d instr=%d dead=%d) reg=%d rows=%d" % (
            miss, reg, ins, dead, len(mine_miss), len(lands_inst), len(mine_dead), reg, len(rows))

    def rows_leg():
        need = list(block["base_missing"]) + ["reports/round-83/accept-%s83.py" % k for k in ("o", "d", "c")]
        absent = [p for p in need if not any(p in cells[2] for cells, _ in rows if len(cells) > 2)]
        return (not absent, "rows=%d prepared=%d absent=%s" % (len(rows), len(need), absent or "none"))

    def dead_leg():
        dead = dead_of(rows, tree)
        grew = len(rows) - len(base_rows)
        return (not dead and grew >= block["min_new_rows"], "dead=%d rows=%d base_rows=%d grew=%d floor=%d" % (len(dead), len(rows), len(base_rows), grew, block["min_new_rows"]))

    def separable():
        ch = C.changed_paths(root, base, lands)
        own_missing = [p for p in block["own_paths"] if not any(c == p or c.startswith(p) for c in ch)]
        foreign = [p for p in block["foreign_paths"] if any(c == p or c.startswith(p.rstrip("/") + "/") for c in ch)]
        return (not own_missing and not foreign, "own_missing=%s foreign=%s" % (own_missing or "none", foreign or "none"))

    g.grade("FROZENCFG", frozen)
    g.grade("BEFORE", before)
    g.grade("TOOL", tool)
    g.grade("SELFTEST", selftest)
    g.grade("REGISTRY", registry)
    g.grade("ROWS", rows_leg)
    g.grade("DEAD", dead_leg)
    g.grade("SEPARABLE", separable)
    return g


def junk_battery(root, lands, freeze, work, cfg, block):
    import subprocess
    dest = os.path.join(work, "junk")
    C.clone_at(root, lands, dest)
    skill = C.show(root, lands, "SKILL.md").decode("utf-8")
    drop = block["base_missing"][-1]
    kept = [l for l in skill.splitlines() if drop not in l]
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

    def m_rows():
        return C.fixture_commit(dest, "SKILL.md", "\n".join(kept) + "\n", "junk: drop a missing registry row")

    def m_dead():
        out, done = [], False
        for l in skill.splitlines():
            if not done and l.startswith("| accept-"):
                cells = l.strip().strip("|").split("|")
                cells[2] = cells[2] + " tools/round83-absent-tool.py"
                out.append("|" + "|".join(cells) + "|")
                done = True
            else:
                out.append(l)
        return C.fixture_commit(dest, "SKILL.md", "\n".join(out) + "\n", "junk: dead entry-command token")

    def m_canned():
        stub = ("#!/usr/bin/env python3\nimport sys\n"
                "print('GATE-REGISTRY: 0 missing / 99 registered / 61 instruments / 0 dead')\n"
                "if '--json' in sys.argv: print('{\"instruments\":[],\"registered\":[],\"missing\":[],\"dead\":[],\"rows\":99}')\n"
                "if '--selftest' in sys.argv: print('SELFTEST: PASS (99 checks)')\n"
                "sys.exit(0)\n")
        C.fixture_commit(dest, block["tool_path"], stub, "junk: canned summary stub")
        return C.fixture_commit(dest, "SKILL.md", "\n".join(kept) + "\n", "junk: registry row dropped under a canned tool")

    trial("rows-dropped", m_rows, "ROWS")
    trial("dead-token", m_dead, "DEAD")
    trial("canned-tool", m_canned, "REGISTRY")
    ok = all(r[2] for r in results)
    print("JUNK-O-83: %s %d/%d" % ("PASS" if ok else "FAIL", sum(1 for r in results if r[2]), len(results)))
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
        _, block = C.claim_config(cfg, "O")
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
