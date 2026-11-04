#!/usr/bin/env python3
"""Round-82 junk-landing generator (QUALITY 25b).

Builds ONE scratch fixture repo per claim (each claim's artifacts alone, so the
counter's SEPARABLE leg is graded against its own lands geometry), proves the
clean landing PASSES that claim's counter first, then applies one junk landing
per fixture and records the counter's own LEG FAIL line, verdict and exit code.

Usage:
  python3 -B reports/round-82/counters/junk-fixtures.py --lane <repo> --work <scratch> --out <dir>

Writes junk-o.txt, junk-d.txt, controls-o.txt, controls-d.txt into --out.
Reads every constant from the lane worktree's reports/round-82/claims.json.
"""
import argparse
import json
import os
import shutil
import subprocess
import sys

CLAIMS = "reports/round-82/claims.json"
COUNTER = {"o": "reports/round-82/accept-o82.py", "d": "reports/round-82/accept-d82.py"}


class Fx:
    def __init__(self, root, lane):
        self.root = root
        self.lane = lane
        self.env = dict(os.environ)
        self.env.update({"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@invalid",
                         "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@invalid",
                         "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
                         "TZ": "UTC"})

    def init(self, base_files=()):
        shutil.rmtree(self.root, ignore_errors=True)
        os.makedirs(self.root)
        self.git("init", "-q")
        top = self.git("rev-parse", "--show-toplevel").stdout.strip()
        assert os.path.realpath(top) == os.path.realpath(self.root), top
        self.put("README", "fixture\n")
        for rel in base_files:
            self.copy(rel)
        return self.commit("fixture base")

    def git(self, *argv):
        return subprocess.run(["git", "-C", self.root] + list(argv), capture_output=True,
                              text=True, env=self.env)

    def put(self, rel, data):
        path = os.path.join(self.root, rel)
        os.makedirs(os.path.dirname(path) or ".", exist_ok=True)
        mode = "wb" if isinstance(data, bytes) else "w"
        with open(path, mode) as fh:
            fh.write(data)

    def copy(self, rel):
        with open(os.path.join(self.lane, rel), "rb") as fh:
            self.put(rel, fh.read())

    def read(self, rel):
        with open(os.path.join(self.root, rel), encoding="utf-8", errors="replace") as fh:
            return fh.read()

    def commit(self, msg):
        self.git("add", "-A")
        r = self.git("commit", "-q", "-m", msg)
        assert r.returncode == 0, r.stderr
        return self.git("rev-parse", "HEAD").stdout.strip()


def run_counter(lane, claim, root, lands, freeze, work):
    return subprocess.run([sys.executable, "-B", os.path.join(lane, COUNTER[claim]),
                           "--root", root, "--lands", lands, "--freeze", freeze,
                           "--work", work], capture_output=True, text=True)


def fail_legs(out):
    return [ln for ln in out.splitlines() if ln.startswith("LEG FAIL")]


def verdict(out):
    for ln in out.splitlines():
        if ln.startswith("ACCEPT-"):
            return ln.strip()
    return "<no verdict>"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lane", required=True)
    ap.add_argument("--work", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    lane = os.path.abspath(args.lane)
    os.makedirs(args.work, exist_ok=True)
    os.makedirs(args.out, exist_ok=True)
    doc = json.load(open(os.path.join(lane, CLAIMS), encoding="utf-8"))
    cfg_o = next(c for c in doc["claims"] if c["id"] == "O")["tool82"]
    cfg_d = next(c for c in doc["claims"] if c["id"] == "D")["entry82"]
    work = os.path.join(args.work, "counter-work")
    os.makedirs(work, exist_ok=True)

    receipts = {"o": ["JUNK-RECEIPT round-82 claim O (accept-o82.py; each junk landing must FAIL)"],
                "d": ["JUNK-RECEIPT round-82 claim D (accept-d82.py; each junk landing must FAIL)"]}
    controls = {"o": ["CONTROLS round-82 claim O (clean fixture must PASS, do-nothing must refuse)"],
                "d": ["CONTROLS round-82 claim D (clean fixture must PASS, do-nothing must refuse)"]}
    ok = True

    def build(claim, cfg, files, base_files):
        fx = Fx(os.path.join(args.work, "fx-" + claim), lane)
        base = fx.init(base_files=base_files)
        fx.copy(CLAIMS)
        doc_fx = json.loads(fx.read(CLAIMS))
        doc_fx["base"] = base
        for cl in doc_fx.get("claims", []):
            for key in ("tool82", "entry82"):
                if isinstance(cl.get(key), dict):
                    cl[key]["base"] = base
        fx.put(CLAIMS, json.dumps(doc_fx, indent=1))
        freeze = fx.commit("freeze (claims.json, fixture base rewritten)")
        for rel in files:
            fx.copy(rel)
        clean = fx.commit("clean landing")
        return fx, base, freeze, clean

    def battery(claim, fx, base, freeze, clean, junks):
        nonlocal ok
        r = run_counter(lane, claim, fx.root, clean, freeze, work)
        controls[claim] += [
            "fixture: %s" % fx.root,
            "do-nothing base: %s" % base,
            "freeze: %s" % freeze,
            "clean: %s" % clean,
            "command: python3 -B %s --root %s --lands %s --freeze %s --work <scratch>"
            % (COUNTER[claim], fx.root, clean, freeze),
            r.stdout.strip(),
            "exit=%d" % r.returncode,
            "",
            "do-nothing control: lands = base",
            "command: python3 -B %s --root %s --lands %s --freeze %s --work <scratch>"
            % (COUNTER[claim], fx.root, base, freeze),
        ]
        r0 = run_counter(lane, claim, fx.root, base, freeze, work)
        controls[claim] += [r0.stdout.strip(), "exit=%d" % r0.returncode, ""]
        if r.returncode != 0:
            ok = False
            receipts[claim].append("# CLEAN FIXTURE NOT GREEN: %s" % verdict(r.stdout))
            receipts[claim] += fail_legs(r.stdout)
            return
        receipts[claim].append("# clean fixture green first: %s" % verdict(r.stdout))
        receipts[claim].append("")
        for name, want, mutate, restore in junks:
            mutate()
            c = fx.commit("junk %s" % name)
            rr = run_counter(lane, claim, fx.root, c, freeze, work)
            got = sorted({ln.split()[2] for ln in fail_legs(rr.stdout)})
            receipts[claim] += [
                "# ---- junk-%s / %s ----" % (claim, name),
                "commit: %s" % c,
                "command: python3 -B %s --root %s --lands %s --freeze %s --work <scratch>"
                % (COUNTER[claim], fx.root, c, freeze),
            ]
            receipts[claim] += fail_legs(rr.stdout) or ["LEG FAIL <none>"]
            receipts[claim] += ["verdict: %s" % verdict(rr.stdout),
                                "exit=%d" % rr.returncode,
                                "named-legs-failed: %s (wanted [%r]) -> %s"
                                % (got, want, "OK" if want in got else "MISS"),
                                ""]
            if want not in got:
                ok = False
            restore()
            fx.commit("restore after %s" % name)

    # ---- claim O fixture: the tool alone ----
    fx_o, base_o, freeze_o, clean_o = build("o", cfg_o, [cfg_o["tool_path"]],
                                            [cfg_o["registry_path"]])
    tool_src = fx_o.read(cfg_o["tool_path"])

    def o_delete():
        os.remove(os.path.join(fx_o.root, cfg_o["tool_path"]))

    def o_restore():
        fx_o.put(cfg_o["tool_path"], tool_src)

    def o_canned():
        lines = tool_src.splitlines()
        for i, ln in enumerate(lines):
            if ln.strip().startswith("return (f\"RECHECK-QUEUE:") or ln.strip().startswith("return f\"RECHECK-QUEUE:"):
                indent = ln[:len(ln) - len(ln.lstrip())]
                lines[i] = indent + 'return "RECHECK-QUEUE: 1 due / 0 upcoming / 1 on-release / 3 rows"'
                for j in range(i + 1, min(i + 4, len(lines))):
                    if "on-release" in lines[j] and "rows" in lines[j] and "f\"" in lines[j]:
                        lines[j] = indent + "        "
                break
        else:
            raise SystemExit("no summary return found to mutate")
        fx_o.put(cfg_o["tool_path"], "\n".join(lines) + "\n")

    def o_weak():
        fx_o.put(cfg_o["tool_path"],
                 tool_src.replace('f"SELFTEST: PASS ({len(checks)} checks)"',
                                  '"SELFTEST: PASS (3 checks)"', 1))

    battery("o", fx_o, base_o, freeze_o, clean_o, [
        ("JO1 tool deleted", "TOOL", o_delete, o_restore),
        ("JO2 canned summary", "QUEUE", o_canned, o_restore),
        ("JO3 selftest below the frozen floor", "SELFTEST", o_weak, o_restore),
    ])

    # ---- claim D fixture: entry + registry + evidence ----
    d_files = [cfg_d["entry_path"], cfg_d["registry_path"]]
    d_files += [cfg_d["evidence_dir"] + rid + ".txt" for rid in cfg_d["row_ids"]]
    entry_text = open(os.path.join(lane, cfg_d["entry_path"]), encoding="utf-8").read()
    import re as _re
    base_d_files = [cfg_d["registry_path"], cfg_d["lint_tool_path"]] + sorted(
        {p for p in _re.findall(r"corpus/[A-Za-z0-9._\-/]+\.md", entry_text)
         if os.path.exists(os.path.join(lane, p)) and p != cfg_d["entry_path"]})
    fx_d, base_d, freeze_d, clean_d = build("d", cfg_d, d_files, base_d_files)
    entry_src = fx_d.read(cfg_d["entry_path"])
    reg_src = fx_d.read(cfg_d["registry_path"])

    def d_delete():
        os.remove(os.path.join(fx_d.root, cfg_d["entry_path"]))

    def d_restore():
        fx_d.put(cfg_d["entry_path"], entry_src)

    def d_rows_removed():
        lines = [ln for ln in reg_src.splitlines()
                 if not any(ln.startswith("| %s |" % rid) for rid in cfg_d["row_ids"])]
        fx_d.put(cfg_d["registry_path"], "\n".join(lines) + "\n")

    def d_reg_restore():
        fx_d.put(cfg_d["registry_path"], reg_src)

    def d_long_anchor():
        lines = reg_src.splitlines()
        for i, ln in enumerate(lines):
            if ln.startswith("| %s |" % cfg_d["row_ids"][0]):
                lines[i] = ln.replace("\u300c", "\u300c" + " ".join(["word"] * 26) + " ", 1)
                break
        fx_d.put(cfg_d["registry_path"], "\n".join(lines) + "\n")

    battery("d", fx_d, base_d, freeze_d, clean_d, [
        ("JD1 entry deleted", "ENTRY", d_delete, d_restore),
        ("JD2 registry rows removed", "ROWS", d_rows_removed, d_reg_restore),
        ("JD3 anchor quote over 25 words", "ROWS", d_long_anchor, d_reg_restore),
    ])

    with open(os.path.join(args.out, "junk-o.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(receipts["o"]) + "\n")
    with open(os.path.join(args.out, "junk-d.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(receipts["d"]) + "\n")
    with open(os.path.join(args.out, "controls-o.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(controls["o"]) + "\n")
    with open(os.path.join(args.out, "controls-d.txt"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(controls["d"]) + "\n")
    print("JUNK-FIXTURES: %s (clean green first; 3 junk landings per claim)" % ("PASS" if ok else "FAIL"))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
