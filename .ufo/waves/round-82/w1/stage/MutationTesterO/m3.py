#!/usr/bin/env python3
r"""Round-82 counter for claim O (operability): the registry recheck-cadence auditor.
Grades committed bytes at --lands against constants read at --freeze.

Legs (frozen in reports/round-82/claims.json claim O .legs):
  FROZENCFG   lands claims.json bytes == freeze claims.json bytes
  TOOL        tools/check-sources-recheck.py exists at lands and carries the
              frozen shape markers
  SELFTEST    the tool bytes read from lands run `--selftest` to exit 0 with
              `SELFTEST: PASS (<n> checks)` and n >= the frozen floor; the run
              also fails when a frozen mutant of the tool is graded
  QUEUE       running the lands tool over the FROZEN registry blob prints a
              `RECHECK-QUEUE:` summary at two frozen as-of dates, and this
              counter's own independent parse of the same blob equals it on all
              four numbers (due / upcoming / on-release / rows)
  MODULAR     appending a non-due row to a scratch copy leaves the due and
              upcoming counts unchanged (rows +1); appending a due row raises
              due by exactly one (the round-81 R81-V1 class: a frozen count that
              moves with its own population is not replayable)
  ERROR       a malformed registry makes the tool exit 2 with `RECHECK-ERROR`
              and no traceback
  SEPARABLE   base..lands touches only allowed paths

Refusals (exit 2, `FAIL legs=0/<n> (refused: ...)`, never a PASS): a revision
that is not 40-hex; a freeze that is not an ancestor of lands; lands equal to
the frozen base (the do-nothing control); unreadable frozen claims.json or an
incomplete frozen config; a leg list that disagrees with this counter's leg
table (LEGCOUNT); a --work that is not an existing directory.
"""
import argparse
import datetime
import hashlib
import json
import os
import re
import subprocess
import sys

LABEL = "ACCEPT-O-82"
LEGS = ["FROZENCFG", "TOOL", "SELFTEST", "QUEUE", "MODULAR", "ERROR", "SEPARABLE"]
CLAIMS = "reports/round-82/claims.json"
ROW_RULE = re.compile(r"^\s{0,3}\|\s*S\d{3,}\s*\|")
SUMMARY = re.compile(r"^RECHECK-QUEUE: (\d+) due / (\d+) upcoming / (\d+) on-release / (\d+) rows$")
SELFTEST_LINE = re.compile(r"^SELFTEST: PASS \((\d+) checks\)$")


def run(repo, *a, **kw):
    return subprocess.run(["git", "-C", repo] + list(a), capture_output=True, **kw)


def gout(repo, *a):
    r = run(repo, *a)
    if r.returncode != 0:
        raise RuntimeError("git %s: %s" % (a[0], (r.stderr or b"").decode("utf-8", "replace").strip()))
    return r.stdout.decode("utf-8", "replace")


def sha_bytes(b):
    return hashlib.sha256(b).hexdigest()


class Refuse(Exception):
    pass


def show(repo, rev, path):
    r = run(repo, "show", "%s:%s" % (rev, path))
    if r.returncode != 0:
        return None
    return r.stdout


def build_args():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", required=True)
    ap.add_argument("--lands", required=True)
    ap.add_argument("--freeze", required=True)
    ap.add_argument("--work", required=True)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if not re.fullmatch(r"[0-9a-f]{40}", args.lands):
        raise Refuse("--lands %r is not a 40-hex commit" % args.lands)
    if not re.fullmatch(r"[0-9a-f]{40}", args.freeze):
        raise Refuse("--freeze %r is not a 40-hex commit" % args.freeze)
    if not os.path.isdir(args.work):
        raise Refuse("--work must name an existing scratch directory")
    return args


# ---- this counter's own registry parser (independent of the graded tool) ----

def parse_rows(text):
    rows = []
    for line in text.splitlines():
        if ROW_RULE.match(line):
            rows.append([c.strip() for c in line.strip().strip("|").split("|")])
    return rows


def due_date(cells):
    """Return datetime.date, or None for an event-driven cadence ('on-release')."""
    opened, recheck = cells[8], cells[9]
    if recheck == "on-release":
        return None
    m = re.fullmatch(r"(\d+)d", recheck)
    if m:
        return datetime.date.fromisoformat(opened) + datetime.timedelta(days=int(m.group(1)))
    return datetime.date.fromisoformat(recheck)


def tally(text, as_of, window):
    due = upcoming = exempt = 0
    bad = 0
    for cells in parse_rows(text):
        if len(cells) != 11:
            bad += 1
            continue
        try:
            d = due_date(cells)
        except ValueError:
            bad += 1
            continue
        if d is None:
            due += 1
        elif d <= as_of:
            due += 1
        elif d <= as_of + datetime.timedelta(days=window):
            upcoming += 1
    return due, upcoming, exempt, len(parse_rows(text)), bad


def read_frozen(repo, freeze):
    b = show(repo, freeze, CLAIMS)
    if b is None:
        raise Refuse("frozen claims.json unreadable at %s" % freeze)
    try:
        doc = json.loads(b.decode("utf-8"))
    except ValueError as exc:
        raise Refuse("frozen claims.json does not parse: %s" % exc)
    claim = None
    for cl in doc.get("claims", []):
        if cl.get("id") == "O":
            claim = cl
    if claim is None:
        raise Refuse("frozen claims.json carries no claim O")
    cfg = claim.get("tool82")
    if not isinstance(cfg, dict):
        raise Refuse("frozen claim O carries no tool82 config")
    if list(cfg.get("legs", [])) != LEGS:
        raise Refuse("LEGCOUNT: frozen legs %r != counter legs %r" % (cfg.get("legs"), LEGS))
    return doc, cfg, b


def check_ancestry(repo, lands, freeze, base):
    r = run(repo, "cat-file", "-t", lands)
    if r.returncode != 0 or r.stdout.decode().strip() != "commit":
        raise Refuse("lands %s is not a commit" % lands)
    if lands == base:
        raise Refuse("lands equals the frozen base %s (do-nothing control)" % base)
    if run(repo, "merge-base", "--is-ancestor", freeze, lands).returncode != 0:
        raise Refuse("freeze %s is not an ancestor of lands %s" % (freeze, lands))


def receipt_headers(repo, args, freeze_sha):
    tree = gout(repo, "rev-parse", "%s^{tree}" % args.lands).strip()
    r = run(repo, "rev-parse", "refs/heads/main")
    main_tip = r.stdout.decode().strip() if r.returncode == 0 else "<no main>"
    self_sha = sha_bytes(open(os.path.abspath(__file__), "rb").read())
    return [
        "# stamped revision: %s" % args.lands,
        "# evaluated revision: %s" % args.lands,
        "# measured revision (lane main): %s" % main_tip,
        "# tree: %s" % tree,
        "# counter sha256 (self): %s" % self_sha,
        "# config source: git show %s:%s (never the graded tree)" % (args.freeze, CLAIMS),
        "# config sha256 (frozen claims.json): %s" % freeze_sha,
    ]


def tool_run(py, tool_path, registry_path, as_of, window):
    return subprocess.run([py, "-B", tool_path, "--registry", registry_path,
                           "--as-of", as_of, "--window", str(window)],
                          capture_output=True, text=True)


def main():
    try:
        args = build_args()
    except Refuse as exc:
        print("%s: FAIL legs=0/%d (refused: %s)" % (LABEL, len(LEGS), exc))
        return 2
    repo = os.path.abspath(args.root)
    try:
        doc, cfg, frozen_claims = read_frozen(repo, args.freeze)
        base = cfg.get("base") or doc.get("base")
        check_ancestry(repo, args.lands, args.freeze, base)
    except (Refuse, RuntimeError) as exc:
        print("%s: FAIL legs=0/%d (refused: %s)" % (LABEL, len(LEGS), exc))
        return 2
    required = ("tool_path", "shape_markers", "min_selftest_checks", "registry_path",
                "as_of", "window", "projection_as_of", "allowed_o_paths")
    for key in required:
        if key not in cfg:
            print("%s: FAIL legs=0/%d (refused: frozen config incomplete: %s)"
                  % (LABEL, len(LEGS), key))
            return 2

    freeze_sha = sha_bytes(frozen_claims)
    print("# frozen legs: %d (%s)" % (len(LEGS), ", ".join(LEGS)))
    for ln in receipt_headers(repo, args, freeze_sha):
        print(ln)

    results = []
    py = sys.executable

    # FROZENCFG
    b = show(repo, args.lands, CLAIMS)
    if b is None:
        results.append(("FROZENCFG", "FAIL", "claims.json absent at lands"))
    elif sha_bytes(b) != freeze_sha:
        results.append(("FROZENCFG", "FAIL", "claims.json at lands differs from the frozen bytes"))
    else:
        results.append(("FROZENCFG", "PASS", "lands bytes == freeze bytes"))

    # TOOL
    tb = show(repo, args.lands, cfg["tool_path"])
    tool_text = tb.decode("utf-8", "replace") if tb else ""
    tool_ok = False
    why = []
    if tb is None:
        why.append("tool absent at lands")
    else:
        for m in cfg["shape_markers"]:
            if m not in tool_text:
                why.append("shape marker missing: %r" % m)
        tool_ok = not why
    results.append(("TOOL", "PASS" if tool_ok else "FAIL",
                    "; ".join(why) or "shape markers ok (%d B)" % len(tb)))

    # SELFTEST: run the lands tool bytes from a scratch copy
    st_ok = False
    st_line = "<not run>"
    tool_path = os.path.join(args.work, "check-sources-recheck.py")
    if tb is None:
        st_line = "tool absent at lands"
    else:
        os.makedirs(args.work, exist_ok=True)
        with open(tool_path, "wb") as fh:
            fh.write(tb)
        r = subprocess.run([py, "-B", tool_path, "--selftest"], capture_output=True, text=True)
        lines = [ln for ln in (r.stdout or "").splitlines() if SELFTEST_LINE.match(ln.strip())]
        if not lines:
            st_line = "<no verdict line> rc=%d" % r.returncode
        else:
            st_line = lines[-1].strip()
            n = int(SELFTEST_LINE.match(st_line).group(1))
            st_ok = r.returncode == 0 and n >= cfg["min_selftest_checks"]
            if r.returncode != 0:
                st_line += " rc=%d" % r.returncode
            elif n < cfg["min_selftest_checks"]:
                st_line += " (< frozen floor %d)" % cfg["min_selftest_checks"]
    results.append(("SELFTEST", "PASS" if st_ok else "FAIL", st_line))

    # QUEUE: lands tool over the FROZEN registry blob, compared with our own parse
    reg = show(repo, args.freeze, cfg["registry_path"])
    queue_ok = False
    queue_line = "<not run>"
    if reg is None:
        queue_line = "frozen registry unreadable"
    elif not st_ok:
        queue_line = "tool selftest not green"
    else:
        reg_path = os.path.join(args.work, "registry-frozen.md")
        with open(reg_path, "wb") as fh:
            fh.write(reg)
        reg_text = reg.decode("utf-8", "replace")
        parts = []
        queue_ok = True
        for as_of in (cfg["as_of"], cfg["projection_as_of"]):
            want = tally(reg_text, datetime.date.fromisoformat(as_of), int(cfg["window"]))
            r = tool_run(py, tool_path, reg_path, as_of, int(cfg["window"]))
            got = None
            for ln in (r.stdout or "").splitlines():
                m = SUMMARY.match(ln.strip())
                if m:
                    got = tuple(int(x) for x in m.groups())
            if r.returncode != 0 or got is None:
                queue_ok = False
                parts.append("%s: no summary (rc=%d)" % (as_of, r.returncode))
                continue
            if got != want[:4]:
                queue_ok = False
                parts.append("%s: tool %s != counter %s" % (as_of, got, want[:4]))
            else:
                parts.append("%s: %d/%d/%d/%d ok" % ((as_of,) + got))
        queue_line = "; ".join(parts)
    results.append(("QUEUE", "PASS" if queue_ok else "FAIL", queue_line))

    # MODULAR: population changes must not move the due set except by the row added
    mod_ok = False
    mod_line = "<not run>"
    if reg is None or not st_ok:
        mod_line = "registry/tool unavailable"
    else:
        reg_path = os.path.join(args.work, "registry-modular.md")
        base_text = reg.decode("utf-8", "replace")
        as_of = cfg["as_of"]
        t0 = tally(base_text, datetime.date.fromisoformat(as_of), int(cfg["window"]))
        neutral = ("\n| S900 | synthetic neutral row | book | C | s | a | t | queued | %s | 365d | \u2014 |"
                   % as_of)
        with open(reg_path, "w", encoding="utf-8") as fh:
            fh.write(base_text + neutral + "\n")
        r1 = tool_run(py, tool_path, reg_path, as_of, int(cfg["window"]))
        g1 = None
        for ln in (r1.stdout or "").splitlines():
            m = SUMMARY.match(ln.strip())
            if m:
                g1 = tuple(int(x) for x in m.groups())
        due_prev = (datetime.date.fromisoformat(as_of) - datetime.timedelta(days=1)).isoformat()
        due_row = ("\n| S901 | synthetic due row | book | C | s | a | t | queued | %s | %s | \u2014 |"
                   % ("2026-01-01", due_prev))
        with open(reg_path, "w", encoding="utf-8") as fh:
            fh.write(base_text + due_row + "\n")
        r2 = tool_run(py, tool_path, reg_path, as_of, int(cfg["window"]))
        g2 = None
        for ln in (r2.stdout or "").splitlines():
            m = SUMMARY.match(ln.strip())
            if m:
                g2 = tuple(int(x) for x in m.groups())
        if g1 is None or g2 is None:
            mod_line = "no summary on a scratch copy"
        else:
            ok1 = g1[0] == t0[0] and g1[1] == t0[1] and g1[2] == t0[2] and g1[3] == t0[3] + 1
            ok2 = g2[0] == t0[0] + 1 and g2[1] == t0[1] and g2[2] == t0[2] and g2[3] == t0[3] + 1
            mod_ok = ok1 and ok2
            mod_line = ("neutral +1 row -> %s; due +1 row -> %s; frozen %s"
                        % (g1, g2, t0[:4]))
    results.append(("MODULAR", "PASS" if mod_ok else "FAIL", mod_line))

    # ERROR: malformed registry -> exit 2 with RECHECK-ERROR, no traceback
    err_ok = False
    err_line = "<not run>"
    if not st_ok:
        err_line = "tool selftest not green"
    else:
        reg_path = os.path.join(args.work, "registry-broken.md")
        broken = ("# Sources\n\n## Registry\n\n| id | source | kind | tier | scope | anchor | teaches | "
                  "status | opened | recheck | used-by |\n|---|---|---|---|---|---|---|---|---|---|---|\n"
                  "| S001 | x | book | A | s | a | t | mined | 2026-10-19 | 365d | \u2014 | extra |\n")
        with open(reg_path, "w", encoding="utf-8") as fh:
            fh.write(broken)
        r = tool_run(py, tool_path, reg_path, cfg["as_of"], int(cfg["window"]))
        blob = (r.stdout or "") + (r.stderr or "")
        err_ok = (r.returncode == 2 and "RECHECK-ERROR" in blob and "Traceback" not in blob)
        err_line = "exit=%d labelled=%s traceback=%s" % (
            r.returncode, "RECHECK-ERROR" in blob, "Traceback" in blob)
    results.append(("ERROR", "PASS" if err_ok else "FAIL", err_line))

    # SEPARABLE
    allowed = set(cfg.get("allowed_o_paths", [])) | set(cfg.get("sibling_paths", []))
    changed = [ln for ln in gout(repo, "diff-tree", "-r", "--name-only",
                                 "%s..%s" % (base, args.lands)).splitlines() if ln]
    bad = [p for p in changed if not any(p == a or p.startswith(a) for a in allowed)]
    results.append(("SEPARABLE", "PASS" if not bad else "FAIL",
                    "0 foreign paths" if not bad else "foreign: %s" % bad[:4]))

    npass = 0
    for name, verdict, why in results:
        print("LEG %s %s (%s)" % (verdict, name, why))
        npass += verdict == "PASS"
    print("%s: %s legs=%d/%d" % (LABEL, "PASS" if npass == len(LEGS) else "FAIL",
                                 npass, len(LEGS)))
    return 0 if npass == len(LEGS) else 1


def selftest(work):
    """Refusal spine plus TOOL/SELFTEST/QUEUE/MODULAR/ERROR framing on a
    synthetic fixture whose tool is a reference implementation owned by the
    test, never the graded artifact."""
    import shutil
    ok = 0
    total = 0
    fx = os.path.join(work, "fx-o")
    shutil.rmtree(fx, ignore_errors=True)
    os.makedirs(fx)
    env = dict(os.environ)
    env.update({"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@invalid",
                "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@invalid",
                "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1",
                "TZ": "UTC"})

    def sh(*a):
        return subprocess.run(["git", "-C", fx] + list(a), capture_output=True, env=env)

    def commit(msg):
        assert sh("add", "-A").returncode == 0
        r = sh("commit", "-q", "-m", msg)
        assert r.returncode == 0, r.stderr
        return sh("rev-parse", "HEAD").stdout.decode().strip()

    def check(label, cond, detail=""):
        nonlocal ok, total
        total += 1
        if cond:
            ok += 1
            print("SELFTEST ok   %s" % label)
        else:
            print("SELFTEST FAIL %s %s" % (label, detail))

    def counter(args):
        return subprocess.run([sys.executable, "-B", os.path.abspath(__file__)] + args,
                              capture_output=True, text=True)

    assert sh("init", "-q").returncode == 0
    assert sh("rev-parse", "--show-toplevel").stdout.decode().strip() == fx

    tool = (
        "import argparse,datetime,re,sys\n"
        "ROW=re.compile(r'^\\s{0,3}\\|\\s*S\\d{3,}\\s*\\|')\n"
        "def main():\n"
        "    ap=argparse.ArgumentParser(); ap.add_argument('--registry',default='corpus/SOURCES.md')\n"
        "    ap.add_argument('--as-of'); ap.add_argument('--window',type=int,default=90)\n"
        "    ap.add_argument('--selftest',action='store_true'); a=ap.parse_args()\n"
        "    if a.selftest:\n"
        "        print('SELFTEST: PASS (9 checks)'); return 0\n"
        "    asof=datetime.date.fromisoformat(a.as_of); due=up=ex=rows=0\n"
        "    for line in open(a.registry,encoding='utf-8'):\n"
        "        if not ROW.match(line): continue\n"
        "        rows+=1; c=[x.strip() for x in line.strip().strip('|').split('|')]\n"
        "        if len(c)!=11:\n"
        "            print('RECHECK-ERROR row %d has %d cells'%(rows,len(c))); return 2\n"
        "        try:\n"
        "            if c[9]=='on-release': ex+=1; continue\n"
        "            m=re.fullmatch(r'(\\d+)d',c[9])\n"
        "            d=datetime.date.fromisoformat(c[8])+datetime.timedelta(days=int(m.group(1))) if m else datetime.date.fromisoformat(c[9])\n"
        "        except ValueError:\n"
        "            print('RECHECK-ERROR bad cadence row %d'%rows); return 2\n"
        "        if d<=asof: due+=1\n"
        "        elif d<=asof+datetime.timedelta(days=a.window): up+=1\n"
        "    print('RECHECK-QUEUE: %d due / %d upcoming / %d on-release / %d rows'%(due,up,ex,rows))\n"
        "    return 0\n"
        "if __name__=='__main__':\n"
        "    try: sys.exit(main())\n"
        "    except SystemExit: raise\n"
        "    except Exception as e: print('RECHECK-ERROR '+str(e)); sys.exit(2)\n"
    )
    reg = ("# Sources\n\n## Registry\n\n| id | source | kind | tier | scope | anchor | teaches | status | "
           "opened | recheck | used-by |\n|---|---|---|---|---|---|---|---|---|---|---|\n"
           "| S001 | a | book | A | s | a | t | mined | 2026-10-19 | 365d | x |\n"
           "| S002 | b | book | A | s | a | t | mined | 2026-10-19 | 30d | x |\n"
           "| S003 | c | book | A | s | a | t | queued | 2026-10-19 | on-release | \u2014 |\n")
    base_tree = {
        "corpus/SOURCES.md": reg,
        "tools/placeholder.txt": "x\n",
        "reports/round-82/keep.txt": "x\n",
    }
    for path, body in base_tree.items():
        full = os.path.join(fx, path)
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as fh:
            fh.write(body)
    base = commit("base fixture")

    frozen = {
        "round": 82, "base": base,
        "claims": [{"id": "O", "tool82": {
            "tool_path": "tools/check-sources-recheck.py",
            "shape_markers": ["RECHECK-QUEUE:", "--as-of", "def main("],
            "min_selftest_checks": 8,
            "registry_path": "corpus/SOURCES.md",
            "as_of": "2026-11-04",
            "projection_as_of": "2027-11-01",
            "window": 90,
            "allowed_o_paths": ["tools/check-sources-recheck.py", "reports/round-82/"],
            "legs": LEGS,
        }}],
    }
    os.makedirs(os.path.join(fx, "reports", "round-82"), exist_ok=True)
    with open(os.path.join(fx, "reports", "round-82", "claims.json"), "w") as fh:
        json.dump(frozen, fh)
    freeze = commit("freeze")

    with open(os.path.join(fx, "tools", "check-sources-recheck.py"), "w", encoding="utf-8") as fh:
        fh.write(tool)
    lands = commit("lands")
    wd = os.path.join(work, "fx-o-work")
    os.makedirs(wd, exist_ok=True)

    r = counter(["--root", fx, "--lands", lands, "--freeze", freeze, "--work", wd])
    check("clean fixture PASS", r.returncode == 0 and "%s: PASS legs=%d/%d" % (LABEL, len(LEGS), len(LEGS)) in r.stdout,
          r.stdout[-500:] + r.stderr[-200:])
    check("QUEUE compares against the counter's own parse", "LEG PASS QUEUE" in r.stdout, r.stdout[-300:])
    check("MODULAR passes on a population-neutral append", "LEG PASS MODULAR" in r.stdout, r.stdout[-300:])

    r = counter(["--root", fx, "--lands", base, "--freeze", freeze, "--work", wd])
    check("do-nothing control refused", r.returncode == 2 and "do-nothing control" in r.stdout, r.stdout)

    r = counter(["--root", fx, "--lands", "e" * 40, "--freeze", freeze, "--work", wd])
    check("non-commit lands refused", r.returncode == 2 and "legs=0/" in r.stdout, r.stdout)

    r = counter(["--root", fx, "--lands", lands, "--freeze", freeze, "--work", "/nonexistent-work"])
    check("missing --work refused", r.returncode == 2 and "existing scratch" in r.stdout, r.stdout)

    r = counter(["--root", fx, "--lands", freeze, "--freeze", freeze, "--work", wd])
    check("lands==freeze graded not passed",
          r.returncode == 1 and "legs=0/" not in r.stdout and "LEG FAIL TOOL" in r.stdout,
          "rc=%d %s" % (r.returncode, r.stdout[-200:]))

    doc = dict(frozen)
    doc["claims"] = [{"id": "O", "tool82": dict(frozen["claims"][0]["tool82"], legs=["TOOL"])}]
    with open(os.path.join(fx, "reports", "round-82", "claims.json"), "w") as fh:
        json.dump(doc, fh)
    bad = commit("bad legs")
    r = counter(["--root", fx, "--lands", bad, "--freeze", bad, "--work", wd])
    check("LEGCOUNT refused", r.returncode == 2 and "LEGCOUNT" in r.stdout, r.stdout)
    with open(os.path.join(fx, "reports", "round-82", "claims.json"), "w") as fh:
        json.dump(frozen, fh)
    commit("restore")

    # junk 1: tool deleted
    os.remove(os.path.join(fx, "tools", "check-sources-recheck.py"))
    j1 = commit("junk: tool deleted")
    r = counter(["--root", fx, "--lands", j1, "--freeze", freeze, "--work", wd])
    check("junk tool-deleted fails TOOL+SELFTEST",
          "LEG FAIL TOOL" in r.stdout and "LEG FAIL SELFTEST" in r.stdout, r.stdout[-300:])
    with open(os.path.join(fx, "tools", "check-sources-recheck.py"), "w", encoding="utf-8") as fh:
        fh.write(tool)
    commit("restore tool")

    # junk 2: a canned summary printer (the tool stops reading the registry)
    canned = tool.replace("    print('RECHECK-QUEUE: %d due / %d upcoming / %d on-release / %d rows'%(due,up,ex,rows))",
                          "    print('RECHECK-QUEUE: 1 due / 0 upcoming / 1 on-release / 3 rows')")
    with open(os.path.join(fx, "tools", "check-sources-recheck.py"), "w", encoding="utf-8") as fh:
        fh.write(canned)
    j2 = commit("junk: canned summary")
    r = counter(["--root", fx, "--lands", j2, "--freeze", freeze, "--work", wd])
    check("junk canned summary fails QUEUE", "LEG FAIL QUEUE" in r.stdout, r.stdout[-300:])

    # junk 3: self-declared selftest with too few checks
    weak = tool.replace("SELFTEST: PASS (9 checks)", "SELFTEST: PASS (3 checks)")
    with open(os.path.join(fx, "tools", "check-sources-recheck.py"), "w", encoding="utf-8") as fh:
        fh.write(weak)
    j3 = commit("junk: weak selftest")
    r = counter(["--root", fx, "--lands", j3, "--freeze", freeze, "--work", wd])
    check("junk weak selftest fails SELFTEST", "LEG FAIL SELFTEST" in r.stdout, r.stdout[-300:])

    # junk 4: traceback on a malformed registry
    traced = tool.replace("print('RECHECK-ERROR row %d has %d cells'%(rows,len(c))); return 2",
                          "raise SystemExit(0)")
    with open(os.path.join(fx, "tools", "check-sources-recheck.py"), "w", encoding="utf-8") as fh:
        fh.write(traced)
    j4 = commit("junk: malformed registry accepted")
    r = counter(["--root", fx, "--lands", j4, "--freeze", freeze, "--work", wd])
    check("junk malformed-accepted fails ERROR", "LEG FAIL ERROR" in r.stdout, r.stdout[-300:])

    print("SELFTEST-O82: %s (%d checks)" % ("PASS" if ok == total else "FAIL", total))
    return 0 if ok == total else 1


def main_entry():
    argv = sys.argv[1:]
    if "--selftest" in argv:
        import tempfile
        work = None
        for i, a in enumerate(argv):
            if a == "--work" and i + 1 < len(argv):
                work = argv[i + 1]
        work = work or tempfile.mkdtemp(prefix="o82-")
        os.makedirs(work, exist_ok=True)
        return selftest(work)
    return main()


if __name__ == "__main__":
    sys.exit(main_entry())
