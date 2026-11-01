#!/usr/bin/env python3
r"""Round-81 counter for claim D (depth): the ordeal-judicial-proof entry.
Grades committed bytes at --lands against constants read at --freeze.

Legs (frozen in reports/round-81/claims.json claim D .legs):
  FROZENCFG  lands claims.json bytes == freeze claims.json bytes
  ENTRY      the entry exists at lands with the pinned sha/size/markers
  LINT       the pinned cited-lines tool (extracted from lands) prints
             `CITED-LINES: 0 finding(s)` on the entry (extracted from lands)
  ROWS       S901/S902/S903 exist in the registry at lands with the frozen
             kind/tier, status mined, opened 2026-11-01, used-by the entry;
             each anchor quote is inside 「」 and <= 25 words; each capture
             record exists at lands and names its row id
  COUPLES    every corpus/*.md target named on the entry's couples line
             resolves in the lands tree
  NOCANON    the canon-hygiene markers are present in the entry
  SEPARABLE  base..lands touches only allowed_d_paths + sibling_paths

Refusals (exit 2, `FAIL legs=0/<n> (refused: ...)`, never a PASS): a revision
that is not 40-hex; a freeze that is not an ancestor of lands; lands equal to
the frozen base (the do-nothing control); unreadable frozen claims.json or an
incomplete frozen config; a leg list that disagrees with this counter's leg
table (LEGCOUNT); a --work that is not an existing directory.
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

LABEL = "ACCEPT-D-81"
LEGS = ["FROZENCFG", "ENTRY", "LINT", "ROWS", "COUPLES", "NOCANON", "SEPARABLE"]


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


def read_frozen(repo, freeze):
    b = show(repo, freeze, "reports/round-81/claims.json")
    if b is None:
        raise Refuse("frozen claims.json unreadable at %s" % freeze)
    try:
        doc = json.loads(b.decode("utf-8"))
    except ValueError as exc:
        raise Refuse("frozen claims.json does not parse: %s" % exc)
    claim = None
    for cl in doc.get("claims", []):
        if cl.get("id") == "D":
            claim = cl
    if claim is None:
        raise Refuse("frozen claims.json carries no claim D")
    legs = claim.get("entry81", {}).get("legs", [])
    if list(legs) != LEGS:
        raise Refuse("LEGCOUNT: frozen legs %r != counter legs %r" % (legs, LEGS))
    return doc, claim["entry81"], b


def check_ancestry(repo, lands, freeze, base):
    r = run(repo, "cat-file", "-t", lands)
    if r.returncode != 0 or r.stdout.decode().strip() != "commit":
        raise Refuse("lands %s is not a commit" % lands)
    if lands == base:
        raise Refuse("lands equals the frozen base %s (do-nothing control)" % base)
    r = run(repo, "merge-base", "--is-ancestor", freeze, lands)
    if r.returncode != 0:
        raise Refuse("freeze %s is not an ancestor of lands %s" % (freeze, lands))


def receipt_headers(repo, args, freeze_sha):
    tree = gout(repo, "rev-parse", "%s^{tree}" % args.lands).strip()
    r = run(repo, "rev-parse", "main")
    main_tip = r.stdout.decode().strip() if r.returncode == 0 else "<no main>"
    self_sha = sha_bytes(open(os.path.abspath(__file__), "rb").read())
    return [
        "# stamped revision: %s" % args.lands,
        "# evaluated revision: %s" % args.lands,
        "# measured revision (lane main): %s" % main_tip,
        "# tree: %s" % tree,
        "# counter sha256 (self): %s" % self_sha,
        "# config source: git show %s:reports/round-81/claims.json (never the graded tree)" % args.freeze,
        "# config sha256 (frozen claims.json): %s" % freeze_sha,
    ]


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
    for key in ("entry_path", "entry_sha256", "entry_min_bytes", "entry_max_bytes",
                "entry_markers", "canon_markers", "row_ids", "row_kinds",
                "row_tiers", "evidence_dir", "lint_tool_path",
                "lint_tool_sha256", "registry_path", "allowed_d_paths"):
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
    b = show(repo, args.lands, "reports/round-81/claims.json")
    if b is None:
        results.append(("FROZENCFG", "FAIL", "claims.json absent at lands"))
    elif sha_bytes(b) != sha_bytes(frozen_claims):
        results.append(("FROZENCFG", "FAIL", "claims.json at lands differs from the frozen bytes"))
    else:
        results.append(("FROZENCFG", "PASS", "lands bytes == freeze bytes"))

    # ENTRY
    eb = show(repo, args.lands, cfg["entry_path"])
    ok = True
    why = []
    if eb is None:
        ok, why = False, ["entry absent at lands"]
    else:
        if sha_bytes(eb) != cfg["entry_sha256"]:
            ok = False; why.append("entry sha mismatch")
        n = len(eb)
        if not (cfg["entry_min_bytes"] <= n <= cfg["entry_max_bytes"]):
            ok = False; why.append("entry size %d outside [%d, %d]" % (n, cfg["entry_min_bytes"], cfg["entry_max_bytes"]))
        text = eb.decode("utf-8", "replace")
        for m in cfg["entry_markers"]:
            if m not in text:
                ok = False; why.append("marker missing: %r" % m)
    results.append(("ENTRY", "PASS" if ok else "FAIL", "; ".join(why) or "sha/size/markers ok"))
    entry_text = eb.decode("utf-8", "replace") if eb else ""

    # LINT: pinned tool + entry, both extracted from lands
    lint_ok = False
    lint_line = "<not run>"
    lb = show(repo, args.lands, cfg["lint_tool_path"])
    if not ok or lb is None:
        lint_line = "lint tool absent at lands" if lb is None else "entry not usable"
    else:
        if sha_bytes(lb) != cfg["lint_tool_sha256"]:
            lint_line = "lint tool sha mismatch"
        else:
            wd = os.path.join(args.work, "lint")
            os.makedirs(wd, exist_ok=True)
            lp = os.path.join(wd, "check-cited-lines.py")
            ep = os.path.join(wd, "entry.md")
            with open(lp, "wb") as fh:
                fh.write(lb)
            with open(ep, "wb") as fh:
                fh.write(eb)
            r = subprocess.run([py, "-B", lp, ep], capture_output=True)
            text = (r.stdout or b"").decode("utf-8", "replace")
            vl = [ln for ln in text.splitlines() if ln.startswith("CITED-LINES:")] or ["<no verdict>"]
            lint_line = vl[0]
            lint_ok = (r.returncode == 0 and lint_line == "CITED-LINES: 0 finding(s) in 1 file(s)")
    results.append(("LINT", "PASS" if lint_ok else "FAIL", lint_line))

    # ROWS
    rows_ok = True
    why = []
    reg = show(repo, args.lands, cfg["registry_path"])
    if reg is None:
        rows_ok, why = False, ["registry absent at lands"]
    else:
        reg_text = reg.decode("utf-8", "replace")
        lines = reg_text.splitlines()
        for rid in cfg["row_ids"]:
            row = None
            for ln in lines:
                if re.match(r"^\|\s*%s\s*\|" % rid, ln):
                    row = ln
                    break
            if row is None:
                rows_ok = False; why.append("%s absent" % rid)
                continue
            cells = [c.strip() for c in row.split("|")[1:-1]]
            # cells: id source kind tier scope anchor teaches status opened recheck used-by
            if len(cells) != 11:
                rows_ok = False; why.append("%s has %d cells" % (rid, len(cells)))
                continue
            if cells[2] != cfg["row_kinds"][rid]:
                rows_ok = False; why.append("%s kind %r != %r" % (rid, cells[2], cfg["row_kinds"][rid]))
            if cells[3] != cfg["row_tiers"][rid]:
                rows_ok = False; why.append("%s tier %r != %r" % (rid, cells[3], cfg["row_tiers"][rid]))
            if cells[7] != "mined":
                rows_ok = False; why.append("%s status %r" % (rid, cells[7]))
            if cells[8] != "2026-11-01":
                rows_ok = False; why.append("%s opened %r" % (rid, cells[8]))
            if cfg["entry_path"] not in cells[10]:
                rows_ok = False; why.append("%s used-by lacks entry" % rid)
            m = re.search(r"「([^」]+)」", cells[5])
            if not m:
                rows_ok = False; why.append("%s anchor has no 「」 span" % rid)
            elif len(m.group(1).split()) > 25:
                rows_ok = False; why.append("%s anchor %d words" % (rid, len(m.group(1).split())))
            ev = show(repo, args.lands, cfg["evidence_dir"] + rid + ".txt")
            if ev is None:
                rows_ok = False; why.append("%s capture record absent" % rid)
            elif ("row: %s" % rid) not in ev.decode("utf-8", "replace"):
                rows_ok = False; why.append("%s capture record lacks its row id" % rid)
    results.append(("ROWS", "PASS" if rows_ok else "FAIL", "; ".join(why) or "3 rows verified"))

    # COUPLES: every corpus/*.md token on the couples line resolves at lands
    tree_set = set(gout(repo, "ls-tree", "-r", "--name-only", args.lands).splitlines())
    couple_paths = sorted(set(re.findall(r"corpus/[A-Za-z0-9._\-/]+\.md", entry_text)))
    missing = [p for p in couple_paths if p not in tree_set]
    results.append(("COUPLES", "PASS" if couple_paths and not missing else "FAIL",
                    "%d targets, 0 missing" % len(couple_paths)
                    if couple_paths and not missing else
                    ("no targets found" if not couple_paths else "missing: %s" % missing[:4])))

    # NOCANON
    canon_ok = all(m in entry_text for m in cfg["canon_markers"]) if entry_text else False
    results.append(("NOCANON", "PASS" if canon_ok else "FAIL",
                    "canon markers ok" if canon_ok else "canon marker missing"))

    # SEPARABLE
    allowed = set(cfg.get("allowed_d_paths", [])) | set(cfg.get("sibling_paths", []))
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
    """Prove the refusal spine plus ENTRY/LINT/ROWS framing on a synthetic
    fixture with a stub lint tool and a one-row registry."""
    import shutil
    ok = 0
    total = 0
    fx = os.path.join(work, "fx")
    if os.path.exists(fx):
        shutil.rmtree(fx, ignore_errors=True)
    env = dict(os.environ)
    env.update({"GIT_AUTHOR_NAME": "t", "GIT_AUTHOR_EMAIL": "t@invalid",
                "GIT_COMMITTER_NAME": "t", "GIT_COMMITTER_EMAIL": "t@invalid",
                "GIT_CONFIG_GLOBAL": os.devnull, "GIT_CONFIG_NOSYSTEM": "1"})

    def sh(*a):
        return subprocess.run(["git", "-C", fx] + list(a), capture_output=True, env=env)

    os.makedirs(fx, exist_ok=True)
    subprocess.run(["git", "init", "-q", fx], capture_output=True, env=env)
    with open(os.path.join(fx, "seed.txt"), "w", newline="") as fh:
        fh.write("seed\n")
    sh("add", "seed.txt"); sh("commit", "-q", "-m", "base")
    base = sh("rev-parse", "HEAD").stdout.decode().strip()

    lint_body = (
        "# stub lint (selftest fixture)\n"
        "import sys, io\n"
        "text = io.open(sys.argv[1], encoding='utf-8').read()\n"
        "import re\n"
        "bad = 0\n"
        "for i, ln in enumerate(text.splitlines(), 1):\n"
        "    ids = re.findall(r'S[0-9]{3,}', ln)\n"
        "    if len(set(ids)) > 1:\n"
        "        print('MULTI-ID %s:%d %s' % (sys.argv[1], i, ','.join(sorted(set(ids)))))\n"
        "        bad += 1\n"
        "print('CITED-LINES: %d finding(s) in 1 file(s)' % bad)\n"
        "sys.exit(1 if bad else 0)\n")
    lint_sha = hashlib.sha256(lint_body.encode()).hexdigest()
    entry_body = (
        "# stub entry\n"
        "- topic: judicial proof as a ritual system\n"
        "gap filled: x\n"
        "- couples: corpus/knowledge/myth-symbol/other.md\n"
        "verified-at: 2026-11-01\n"
        "- recheck: 180d\n"
        "- scope: it decides nothing about what is true in any world, never here\n"
        "## 1. Partial owners\n## 2. Six design decisions\n## 3. Attested anchors\n## 6. Lore handoff\n"
        "- S901: the anchor 「one two three」 line\n")
    entry_sha = hashlib.sha256(entry_body.encode()).hexdigest()
    registry_row = ("| S901 | some source | book | A | scope | anchor — quote located: 「one two three」 (3 words) "
                    "| teaches | mined | 2026-11-01 | 180d | corpus/knowledge/myth-symbol/stub-entry.md |\n")
    ev_body = "row: S901\ncapture: 2026-11-01\n"

    cfg_stub = {
        "legs": LEGS, "base": base,
        "entry_path": "corpus/knowledge/myth-symbol/stub-entry.md",
        "entry_sha256": entry_sha, "entry_min_bytes": 10, "entry_max_bytes": 9000,
        "entry_markers": ["- topic: judicial proof as a ritual system", "gap filled:", "## 3. Attested anchors"],
        "canon_markers": ["never here"],
        "row_ids": ["S901"], "row_kinds": {"S901": "book"}, "row_tiers": {"S901": "A"},
        "evidence_dir": "reports/round-81/evidence/",
        "lint_tool_path": "tools/check-cited-lines.py", "lint_tool_sha256": lint_sha,
        "registry_path": "corpus/SOURCES.md",
        "allowed_d_paths": ["corpus/knowledge/myth-symbol/stub-entry.md",
                            "corpus/knowledge/myth-symbol/other.md",
                            "corpus/SOURCES.md",
                            "reports/round-81/", "tools/"], "sibling_paths": [],
    }
    claims = json.dumps({"round": 81, "base": base, "claims": [
        {"id": "D", "axis": "depth", "entry81": cfg_stub}]}, indent=1) + "\n"

    # freeze first (claims only), then land the rest
    os.makedirs(os.path.join(fx, "reports", "round-81"), exist_ok=True)
    with open(os.path.join(fx, "reports", "round-81", "claims.json"), "w", newline="") as fh:
        fh.write(claims)
    sh("add", "reports/round-81/claims.json"); sh("commit", "-q", "-m", "freeze")
    freeze = sh("rev-parse", "HEAD").stdout.decode().strip()

    os.makedirs(os.path.join(fx, "corpus", "knowledge", "myth-symbol"), exist_ok=True)
    os.makedirs(os.path.join(fx, "corpus"), exist_ok=True)
    os.makedirs(os.path.join(fx, "tools"), exist_ok=True)
    os.makedirs(os.path.join(fx, "reports", "round-81", "evidence"), exist_ok=True)
    with open(os.path.join(fx, "corpus", "knowledge", "myth-symbol", "stub-entry.md"), "w", newline="") as fh:
        fh.write(entry_body)
    with open(os.path.join(fx, "corpus", "knowledge", "myth-symbol", "other.md"), "w", newline="") as fh:
        fh.write("# other\n")
    with open(os.path.join(fx, "corpus", "SOURCES.md"), "w", newline="") as fh:
        fh.write(registry_row)
    with open(os.path.join(fx, "tools", "check-cited-lines.py"), "w", newline="") as fh:
        fh.write(lint_body)
    with open(os.path.join(fx, "reports", "round-81", "evidence", "S901.txt"), "w", newline="") as fh:
        fh.write(ev_body)
    sh("add", "-A"); sh("commit", "-q", "-m", "lands")
    lands = sh("rev-parse", "HEAD").stdout.decode().strip()

    me = os.path.abspath(__file__)
    wd = os.path.join(work, "wd")
    os.makedirs(wd, exist_ok=True)

    def counter(lands_, freeze_):
        return subprocess.run([sys.executable, "-B", me, "--root", fx,
                               "--lands", lands_, "--freeze", freeze_, "--work", wd],
                              capture_output=True)

    def scenario(name, r, want_re, want_exit):
        nonlocal ok, total
        total += 1
        text = (r.stdout or b"").decode("utf-8", "replace")
        got = re.search(want_re, text)
        good = (r.returncode == want_exit) and bool(got)
        print("selftest: %s -> exit=%d %s as-expected=%s"
              % (name, r.returncode, (got.group(0) if got else text.strip()[:70])[:70],
                 "True" if good else "False"))
        if good:
            ok += 1

    r = counter(base, freeze)
    scenario("lands==base refused", r, r"refused: lands equals the frozen base", 2)
    r = counter("zz", freeze)
    scenario("non-40hex refused", r, r"refused: --lands .* not a 40-hex", 2)
    r = counter(lands, freeze)
    scenario("full pass on stub lands", r, r"ACCEPT-D-81: PASS legs=7/7", 0)
    # tamper: put two ids on the anchor line -> LINT fails
    with open(os.path.join(fx, "corpus", "knowledge", "myth-symbol", "stub-entry.md"), "w", newline="") as fh:
        fh.write(entry_body.replace("- S901: the anchor", "- S901 and S902: the anchor"))
    sh("add", "-A"); sh("commit", "-q", "-m", "multiid")
    lands2 = sh("rev-parse", "HEAD").stdout.decode().strip()
    r = counter(lands2, freeze)
    scenario("multi-id line fails LINT", r, r"LEG FAIL LINT", 1)
    # tamper: flip the row tier -> ROWS fails
    with open(os.path.join(fx, "corpus", "SOURCES.md"), "w", newline="") as fh:
        fh.write(registry_row.replace("| book | A |", "| book | B |"))
    sh("add", "-A"); sh("commit", "-q", "-m", "tierflip")
    lands3 = sh("rev-parse", "HEAD").stdout.decode().strip()
    r = counter(lands3, freeze)
    scenario("tier flip fails ROWS", r, r"LEG FAIL ROWS", 1)
    print("SELFTEST-D81: %s (%d checks; counter sha256 %s)"
          % ("PASS" if ok == total else "FAIL", total,
             sha_bytes(open(me, "rb").read())))
    return 0 if ok == total else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser(add_help=False)
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--work", default="")
    known, _ = ap.parse_known_args()
    if known.selftest and known.work:
        sys.exit(selftest(known.work))
    sys.exit(main())
