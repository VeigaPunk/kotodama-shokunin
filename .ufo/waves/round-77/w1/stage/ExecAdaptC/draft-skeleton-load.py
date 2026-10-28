#!/usr/bin/env python3
"""Loader proof: the r77 draft claim-C shape loads through accept-c.py.

Builds a throw-away git repo under $HYAKU_SCRATCH (asserted toplevel), commits a
base tree, commits reports/round-77/claims.json = claims-C.skeleton.json with the
base revision stamped, then calls load_frozen_config() on that freeze.  Prints
the values the counter will grade with.  No lane file is touched.
"""
import importlib.util
import json
import os
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    spec = importlib.util.spec_from_file_location(
        "accept_c", os.path.join(HERE, "accept-c.py"))
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)

    scratch = os.environ.get("HYAKU_SCRATCH") or ""
    if not scratch:
        print("ERROR: set HYAKU_SCRATCH to a scratch root", file=sys.stderr)
        return 2
    root = tempfile.mkdtemp(dir=scratch)
    d = os.path.join(root, "draftlane")
    os.makedirs(d)

    def git(*args):
        r = subprocess.run(["git", "-C", d, *args], capture_output=True, text=True)
        if r.returncode != 0:
            raise SystemExit("git %s: %s" % (" ".join(args), r.stderr.strip()))
        return r

    git("init", "-q")
    top = git("rev-parse", "--show-toplevel").stdout.strip()
    print("fixture toplevel matches: %s" % (
        os.path.realpath(top) == os.path.realpath(d)))
    with open(os.path.join(d, "README"), "w", encoding="utf-8") as fh:
        fh.write("base\n")
    git("add", "-A")
    git("-c", "user.name=AcceptFixture", "-c", "user.email=accept@example.invalid",
        "commit", "-q", "-m", "base")
    base = git("rev-parse", "HEAD").stdout.strip()

    with open(os.path.join(HERE, "claims-C.skeleton.json"), encoding="utf-8") as fh:
        skel = json.load(fh)
    skel["base"] = base
    os.makedirs(os.path.join(d, "reports/round-77"))
    with open(os.path.join(d, "reports/round-77/claims.json"), "w",
              encoding="utf-8") as fh:
        json.dump(skel, fh, indent=2)
        fh.write("\n")
    git("add", "-A")
    git("-c", "user.name=AcceptFixture", "-c", "user.email=accept@example.invalid",
        "commit", "-q", "-m", "freeze")
    freeze = git("rev-parse", "HEAD").stdout.strip()

    cfg = m.load_frozen_config(d, freeze)
    print("frozen_sha256: %s" % cfg["frozen_sha256"])
    print("base: %s" % cfg["base"])
    print("rows: %s" % cfg["rows"])
    print("row_staged: %s" % cfg["row_staged"])
    for lane in cfg["rows"]:
        print("doc key %s: %s%s" % ((lane,) + m._doc_url_key(cfg["row_doc"][lane])))
    print("entries: %s (min_entries %d)" % (cfg["entries"], cfg["min_entries"]))
    print("counts: rows_before=%d knowledge_before=%d"
          % (cfg["rows_before"], cfg["knowledge_before"]))
    print("required_sections: %s"
          % [(s["label"], s["min"], s["pattern"]) for s in cfg["required_sections"]])
    print("sweeps: %s" % [(s["pattern"], s["scope"]) for s in cfg["sweeps"]])
    print("refused_staged: %s" % cfg["refused_staged"])
    print("removed_ids: %s" % cfg["removed_ids"])
    print("staged universe: %d id(s) from %s"
          % (len(cfg["staged_universe"]), cfg["staged_ids_path"]))
    print("scratch_mirror: %s receipt=%s"
          % (cfg["scratch_mirror"]["dir"],
             (cfg["scratch_mirror"]["receipt"] or {}).get("path") or "-"))
    print("census_start: %s rows=%s"
          % ((cfg["census_start"] or {}).get("path") or "-",
             (cfg["census_start"] or {}).get("rows")))
    print("ground receipt: %s"
          % ((cfg["ground_receipt"] or {}).get("path") or "-"))
    print("frozen_legs == generated: %s (%d names)"
          % (cfg["frozen_legs"] == m.legs_generated(), len(cfg["frozen_legs"])))
    print("map declared: %s %r" % (bool(cfg["map_path"]), cfg["map_sha256"]))
    live = "http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml"
    cap = ("https://web.archive.org/web/20240111092427id_/"
           "http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/t20210316_5318560.shtml")
    print("same page capture folds to the live document: %s"
          % (m._doc_url_key(cap) == m._doc_url_key(live)))
    print("scratch fixture: %s (removed by the caller)" % d)
    return 0


if __name__ == "__main__":
    sys.exit(main())
