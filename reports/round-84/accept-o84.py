#!/usr/bin/env python3
r"""Round-84 counter for claim O (operability): the ordered sound-law applier.

Grades committed bytes at --lands against constants read at --freeze
(reports/round-84/claims.json claim O).

Legs (frozen):
  FROZENCFG   lands claims.json bytes == freeze claims.json bytes
  BEFORE      at base: the tool and the example directory are absent, and no
              committed byte in tools/ or examples/ carries the SOUNDLAWS marker
  TOOL        the tool exists at lands, >= the frozen byte floor, with every
              frozen shape marker
  SELFTEST    the lands tool runs `--selftest` to exit 0 with
              `SELFTEST: PASS (<n> checks)` and n >= the frozen floor
  DEMO        `apply` over the committed example exits 0, prints one summary
              line at or above the frozen floors, reproduces the committed
              expected.tsv byte-for-byte, and its trace fires every rule
  NEGATIVE    three malformed inputs each exit 2 with a SOUNDLAW_ERROR label and
              no traceback
  REGISTRY    a SKILL.md `## Gates and probes` row names the tool, and the
              committed gate-registry auditor over the lands tree reports 0
              missing / >= the frozen registered rows / >= the frozen instruments
              / 0 dead, with the unrowed-tool count not growing
  SEPARABLE   base..lands carries every own path and no foreign claim's path moved
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import counterlib as C  # noqa: E402

CLAIM_ID = "O"
LABEL = "ACCEPT-O-84"
CLAIMS = "reports/round-84/claims.json"
LEGS = ["FROZENCFG", "BEFORE", "TOOL", "SELFTEST", "DEMO", "NEGATIVE", "REGISTRY", "SEPARABLE"]
INSTR = re.compile(r"^reports/[^/]+/accept-[^/]+\.py$")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def registry_rows(skill_text, heading):
    lines = skill_text.splitlines()
    try:
        start = next(i for i, l in enumerate(lines) if l.strip() == heading)
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


def evaluate(root, lands, freeze, work, cfg, block):
    g = C.Grader(LABEL, block["legs"])
    base = cfg["base"]
    tree = os.path.join(work, "tree")
    outdir = os.path.join(work, "demo")
    os.makedirs(outdir, exist_ok=True)
    tool = block["tool_path"]
    example = block["example_dir"]

    lands_inst = [p for p in C.tree_paths(root, lands, "reports") if INSTR.match(p)]
    tools_py = [p for p in C.tree_paths(root, lands, "tools") if p.endswith(".py")]
    examples = C.tree_paths(root, lands, example)

    C.materialize(root, lands, tree, [tool, "SKILL.md", "tools/check-gate-registry.py"]
                  + lands_inst + tools_py + examples)

    rows = registry_rows(read(os.path.join(tree, "SKILL.md")), block["registry_heading"])
    if rows is None:
        raise RuntimeError("lands SKILL.md carries no %r" % block["registry_heading"])

    def frozen():
        bf = C.show(root, freeze, CLAIMS)
        bl = C.show(root, lands, CLAIMS)
        if bf is None or bl is None:
            return False, "claims.json missing at freeze or lands"
        return (bf == bl, "freeze %s lands %s sha256 %s" % (freeze[:8], lands[:8], C.sha256(bl)[:12]))

    def before():
        tool_at_base = C.show(root, base, tool) is not None
        example_at_base = C.tree_paths(root, base, example)
        marker = 0
        for p in C.tree_paths(root, base, "tools") + C.tree_paths(root, base, "examples"):
            b = C.show(root, base, p)
            if b and b"SOUNDLAWS" in b:
                marker += 1
        ok = (not tool_at_base and not example_at_base and marker == 0)
        return ok, "tool_at_base=%s example_files=%d marker_files=%d" % (tool_at_base, len(example_at_base), marker)

    def tool_leg():
        b = C.show(root, lands, tool)
        if b is None:
            return False, "tool absent at lands"
        text = b.decode("utf-8", "replace")
        missing = [m for m in block["shape_markers"] if m not in text]
        return (not missing and len(b) >= block["min_tool_bytes"],
                "bytes=%d/%d missing=%s" % (len(b), block["min_tool_bytes"], missing or "none"))

    def selftest():
        rc, out, err = C.run_py(os.path.join(tree, tool), ["--selftest"], cwd=tree)
        line = C.one_line(out, block["selftest_re"])
        n = int(re.match(block["selftest_re"], line).group(1)) if line else -1
        tail = ((out or err).strip().splitlines() or [""])[-1][:120]
        return (rc == 0 and n >= block["min_selftest_checks"],
                "rc=%d checks=%d floor=%d tail=%r" % (rc, n, block["min_selftest_checks"], tail))

    def demo():
        out_path = os.path.join(outdir, "derived.tsv")
        trace_path = os.path.join(outdir, "trace.tsv")
        for p in (out_path, trace_path):
            if os.path.exists(p):
                os.remove(p)
        rc, out, err = C.run_py(os.path.join(tree, tool), [
            "apply", "--rules", block["rules_path"], "--input", block["input_path"],
            "--out", out_path, "--trace", trace_path], cwd=tree)
        line = C.one_line(out, block["summary_re"])
        if line is None:
            return False, "no single summary line (rc=%d): %r" % (rc, (out or err).strip()[:200])
        w, r, c = (int(x) for x in re.match(block["summary_re"], line).groups())
        if rc != 0:
            return False, "apply exit %d" % rc
        got = open(out_path, "rb").read() if os.path.exists(out_path) else b""
        want = C.show(root, lands, block["expected_path"]) or b""
        if got != want:
            return False, "derived != expected (%d vs %d bytes)" % (len(got), len(want))
        if not os.path.exists(trace_path):
            return False, "no trace file"
        tl = [l for l in read(trace_path).splitlines() if l.strip()]
        fired = {l.split("\t")[2] for l in tl if len(l.split("\t")) >= 3}
        try:
            rule_names = [x["name"] for x in json.loads(C.show(root, lands, block["rules_path"]).decode("utf-8"))["rules"]]
        except Exception as e:
            return False, "rules.json unreadable: %s" % e
        ok = (w >= block["min_words"] and r >= block["min_rules"] and c >= block["min_changes"]
              and len(fired) >= block["min_rules_fired"] and set(rule_names) <= fired
              and len(tl) == c)
        return ok, "summary=(%d,%d,%d) floors=(%d,%d,%d) trace=%d rules_fired=%d/%d" % (
            w, r, c, block["min_words"], block["min_rules"], block["min_changes"],
            len(tl), len(fired), len(rule_names))

    def negative():
        bad = os.path.join(outdir, "bad.json")
        with open(bad, "w", encoding="utf-8") as f:
            f.write("{not json\n")
        empty = os.path.join(outdir, "empty-from.json")
        with open(empty, "w", encoding="utf-8") as f:
            json.dump({"rules": [{"name": "x", "from": "", "to": "a", "pre": [], "post": []}]}, f)
        cases = [
            ("missing-rules", ["apply", "--rules", os.path.join(outdir, "absent.json"),
                               "--input", block["input_path"], "--out", os.path.join(outdir, "n1.tsv")]),
            ("bad-json", ["apply", "--rules", bad,
                          "--input", block["input_path"], "--out", os.path.join(outdir, "n2.tsv")]),
            ("empty-from", ["apply", "--rules", empty,
                            "--input", block["input_path"], "--out", os.path.join(outdir, "n3.tsv")]),
        ]
        problems = []
        for name, args in cases:
            rc, out, err = C.run_py(os.path.join(tree, tool), args, cwd=tree)
            if rc != 2 or "SOUNDLAW_ERROR:" not in err or "Traceback" in err:
                problems.append("%s rc=%d err=%r" % (name, rc, err.strip()[:80]))
        return (not problems, "cases=%d problems=%s" % (len(cases), problems or "none"))

    def registry():
        named = [cells for cells, _ in rows if len(cells) > 2 and tool in cells[2]]
        if not named:
            return False, "no row names %s" % tool
        rc, out, err = C.run_py(os.path.join(tree, "tools/check-gate-registry.py"), ["--root", tree], cwd=tree)
        gl = C.one_line(out, block["gate_re"])
        il = C.one_line(out, block["info_re"])
        if gl is None or il is None:
            return False, "no single GATE-REGISTRY/INFO line: %r" % ((out or err).strip()[:200])
        miss, reg, ins, dead = (int(x) for x in re.match(block["gate_re"], gl).groups())
        unrowed = int(re.match(block["info_re"], il).group(1))
        ok = (rc == 0 and miss == 0 and dead == 0 and reg >= block["min_registered_rows"]
              and ins >= block["min_instruments_at_lands"] and unrowed <= block["max_unrowed_tools"])
        return ok, "gate=(%d,%d,%d,%d) unrowed=%d floors=(%d,%d,%d)" % (
            miss, reg, ins, dead, unrowed, block["min_registered_rows"],
            block["min_instruments_at_lands"], block["max_unrowed_tools"])

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
    g.grade("TOOL", tool_leg)
    g.grade("SELFTEST", selftest)
    g.grade("DEMO", demo)
    g.grade("NEGATIVE", negative)
    g.grade("REGISTRY", registry)
    g.grade("SEPARABLE", separable)
    return g


def junk_battery(root, lands, freeze, work, cfg, block):
    import subprocess
    dest = os.path.join(work, "junk")
    C.clone_at(root, lands, dest)
    tool = block["tool_path"]
    example = block["example_dir"]
    skill = C.show(root, lands, "SKILL.md").decode("utf-8")
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

    def m_row_dropped():
        kept = [l for l in skill.splitlines() if not (l.startswith("|") and tool in l)]
        if len(kept) == len(skill.splitlines()):
            raise C.NoOp("no row names the tool")
        return C.fixture_commit(dest, "SKILL.md", "\n".join(kept) + "\n", "junk: drop the tool registry row")

    def m_copy():
        stub = ("#!/usr/bin/env python3\nimport sys, shutil\n"
                "a = sys.argv[1:]\n"
                "if '--selftest' in a:\n"
                "    print('SELFTEST: PASS (99 checks)')\n    sys.exit(0)\n"
                "i = a.index('--input') + 1; o = a.index('--out') + 1\n"
                "shutil.copyfile(a[i], a[o])\n"
                "print('SOUNDLAWS: 12 words / 6 rules / 99 changes')\n")
        return C.fixture_commit(dest, tool, stub, "junk: copy input to out and claim changes")

    def m_no_trace():
        text = C.show(root, lands, tool).decode("utf-8")
        out, done = [], False
        for line in text.splitlines():
            if not done and "trace" in line:
                out.append("    pass  # trace disabled")
                done = True
            else:
                out.append(line)
        return C.fixture_commit(dest, tool, "\n".join(out) + "\n", "junk: trace disabled")

    trial("row-dropped", m_row_dropped, "REGISTRY")
    trial("copy-input", m_copy, "DEMO")
    trial("no-trace", m_no_trace, "DEMO")
    ok = all(r[2] for r in results)
    print("JUNK-O-84: %s %d/%d" % ("PASS" if ok else "FAIL", sum(1 for r in results if r[2]), len(results)))
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
