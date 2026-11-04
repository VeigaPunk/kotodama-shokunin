#!/usr/bin/env python3
r"""Round-82 counter for claim D (depth): the guest-right / hospitality-law entry.
Grades committed bytes at --lands against constants read at --freeze.

Legs (frozen in reports/round-82/claims.json claim D .legs):
  FROZENCFG   lands claims.json bytes == freeze claims.json bytes
  ENTRY       the entry exists at lands with the pinned sha/size/markers
  LINT        the pinned cited-lines tool (extracted from lands) prints
              `CITED-LINES: 0 finding(s)` on the entry (extracted from lands)
  ROWS        S904/S905/S906 exist in the registry at lands with the frozen
              kind/tier/status, opened date and used-by the entry; each mined
              anchor quote sits inside <U+300C><U+300D> and is <= 25 words; the
              rejected row carries `rejected` and a `flip:` token; each capture
              record exists at lands and names its row id
  ROWCOUNT    the registry row count at lands is frozen_before + frozen_delta or
              more (827 -> >= 831), counted by this counter's own parser
  COUPLES     every corpus/*.md target named on the entry's couples line
              resolves in the lands tree
  NOCANON     the canon-hygiene markers are present in the entry
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

LABEL = "ACCEPT-D-82"
LEGS = ["FROZENCFG", "ENTRY", "LINT", "ROWS", "ROWCOUNT", "COUPLES", "NOCANON", "SEPARABLE"]
CLAIMS = "reports/round-82/claims.json"
RULE = re.compile(r"^\s{0,3}\|\s*S\d{3,}\s*\|")


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
    b = show(repo, freeze, CLAIMS)
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
    cfg = claim.get("entry82")
    if not isinstance(cfg, dict):
        raise Refuse("frozen claim D carries no entry82 config")
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


def registry_rows(text):
    rows = []
    for line in text.splitlines():
        if RULE.match(line):
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            rows.append(cells)
    return rows


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
    required = ("entry_path", "entry_sha256", "entry_min_bytes", "entry_max_bytes",
                "entry_markers", "canon_markers", "row_ids", "row_kinds", "row_tiers",
                "row_status", "row_opened", "evidence_dir", "lint_tool_path",
                "lint_tool_sha256", "registry_path", "rowcount_before", "rowcount_min_after",
                "allowed_d_paths")
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

    # ENTRY
    eb = show(repo, args.lands, cfg["entry_path"])
    ok = True
    why = []
    if eb is None:
        ok, why = False, ["entry absent at lands"]
    else:
        if sha_bytes(eb) != cfg["entry_sha256"]:
            ok = False
            why.append("entry sha mismatch")
        n = len(eb)
        if not (cfg["entry_min_bytes"] <= n <= cfg["entry_max_bytes"]):
            ok = False
            why.append("entry size %d outside [%d, %d]"
                       % (n, cfg["entry_min_bytes"], cfg["entry_max_bytes"]))
        text = eb.decode("utf-8", "replace")
        for m in cfg["entry_markers"]:
            if m not in text:
                ok = False
                why.append("marker missing: %r" % m)
    results.append(("ENTRY", "PASS" if ok else "FAIL", "; ".join(why) or "sha/size/markers ok"))
    entry_text = eb.decode("utf-8", "replace") if eb else ""

    # LINT: pinned tool bytes and entry bytes, both read from lands
    lint_ok = False
    lint_line = "<not run>"
    lb = show(repo, args.lands, cfg["lint_tool_path"])
    if not ok:
        lint_line = "entry not usable"
    elif lb is None:
        lint_line = "lint tool absent at lands"
    elif sha_bytes(lb) != cfg["lint_tool_sha256"]:
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
        out = (r.stdout or b"").decode("utf-8", "replace")
        vl = [ln for ln in out.splitlines() if ln.startswith("CITED-LINES:")] or ["<no verdict>"]
        lint_line = vl[0]
        lint_ok = (r.returncode == 0 and lint_line == "CITED-LINES: 0 finding(s) in 1 file(s)")
    results.append(("LINT", "PASS" if lint_ok else "FAIL", lint_line))

    # ROWS
    rows_ok = True
    why = []
    reg = show(repo, args.lands, cfg["registry_path"])
    reg_text = reg.decode("utf-8", "replace") if reg else ""
    if reg is None:
        rows_ok, why = False, ["registry absent at lands"]
    else:
        lines = reg_text.splitlines()
        for rid in cfg["row_ids"]:
            row = None
            for ln in lines:
                if re.match(r"^\s{0,3}\|\s*%s\s*\|" % rid, ln):
                    row = ln
                    break
            if row is None:
                rows_ok = False
                why.append("%s absent" % rid)
                continue
            cells = [c.strip() for c in row.strip().strip("|").split("|")]
            if len(cells) != 11:
                rows_ok = False
                why.append("%s has %d cells" % (rid, len(cells)))
                continue
            want_status = cfg["row_status"][rid]
            if cells[2] != cfg["row_kinds"][rid]:
                rows_ok = False
                why.append("%s kind %r != %r" % (rid, cells[2], cfg["row_kinds"][rid]))
            if cells[3] != cfg["row_tiers"][rid]:
                rows_ok = False
                why.append("%s tier %r != %r" % (rid, cells[3], cfg["row_tiers"][rid]))
            if cells[7] != want_status:
                rows_ok = False
                why.append("%s status %r != %r" % (rid, cells[7], want_status))
            if cells[8] != cfg["row_opened"][rid]:
                rows_ok = False
                why.append("%s opened %r != %r" % (rid, cells[8], cfg["row_opened"][rid]))
            if want_status == "mined":
                if cfg["entry_path"] not in cells[10]:
                    rows_ok = False
                    why.append("%s used-by lacks entry" % rid)
                m = re.search(r"\u300c([^\u300d]+)\u300d", cells[5])
                if not m:
                    rows_ok = False
                    why.append("%s anchor has no quoted span" % rid)
                elif len(m.group(1).split()) > 25:
                    rows_ok = False
                    why.append("%s anchor %d words" % (rid, len(m.group(1).split())))
            else:
                if "rejected" not in cells[6].lower():
                    rows_ok = False
                    why.append("%s teaches cell lacks 'rejected'" % rid)
                if "flip:" not in cells[6].lower():
                    rows_ok = False
                    why.append("%s teaches cell lacks 'flip:'" % rid)
            ev = show(repo, args.lands, cfg["evidence_dir"] + rid + ".txt")
            if ev is None:
                rows_ok = False
                why.append("%s capture record absent" % rid)
            elif ("row: %s" % rid) not in ev.decode("utf-8", "replace"):
                rows_ok = False
                why.append("%s capture record lacks its row id" % rid)
    results.append(("ROWS", "PASS" if rows_ok else "FAIL",
                    "; ".join(why) or "%d rows verified" % len(cfg["row_ids"])))

    # ROWCOUNT: this counter's own parser, not the census script
    n_after = len(registry_rows(reg_text)) if reg is not None else 0
    rc_ok = n_after >= cfg["rowcount_min_after"] and cfg["rowcount_before"] < cfg["rowcount_min_after"]
    results.append(("ROWCOUNT", "PASS" if rc_ok else "FAIL",
                    "rows %d -> %d (floor %d)" % (cfg["rowcount_before"], n_after,
                                                  cfg["rowcount_min_after"])))

    # COUPLES
    tree_set = set(gout(repo, "ls-tree", "-r", "--name-only", args.lands).splitlines())
    couple_paths = sorted(set(re.findall(r"corpus/[A-Za-z0-9._\-/]+\.md", entry_text)))
    missing = [p for p in couple_paths if p not in tree_set]
    if not couple_paths:
        results.append(("COUPLES", "FAIL", "no targets found"))
    elif missing:
        results.append(("COUPLES", "FAIL", "missing: %s" % missing[:4]))
    else:
        results.append(("COUPLES", "PASS", "%d targets, 0 missing" % len(couple_paths)))

    # NOCANON
    canon_ok = bool(entry_text) and all(m in entry_text for m in cfg["canon_markers"])
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
    """Refusal spine + ENTRY/LINT/ROWS/ROWCOUNT framing on a synthetic fixture."""
    import shutil
    ok = 0
    total = 0
    fx = os.path.join(work, "fx-d")
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
        r = sh("add", "-A")
        assert r.returncode == 0, r.stderr
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

    entry = ("# Guest right\n\n- topic: x\n- gap filled: y\n- couples: "
             "corpus/knowledge/myth-symbol/ritual-liminality.md\n- source: z\n"
             "verified-at: 2026-11-04\n- recheck: 365d\n- scope: q\n"
             "## 1. Partial owners\n## 2. Six design decisions\n"
             "## 3. Attested anchors\n## 6. Lore handoff\n"
             "this decides nothing about what is true in any world; never here\n")
    lint = ('import sys\nprint("CITED-LINES: 0 finding(s) in 1 file(s)")\n'
            'sys.exit(0)\n')
    os.makedirs(os.path.join(fx, "tools"))
    with open(os.path.join(fx, "tools", "check-cited-lines.py"), "w") as fh:
        fh.write(lint)
    os.makedirs(os.path.join(fx, "corpus", "knowledge", "myth-symbol"))
    with open(os.path.join(fx, "corpus", "knowledge", "myth-symbol", "ritual-liminality.md"), "w") as fh:
        fh.write("# rit\n")
    rows = [
        "| S001 | src | book | B | s | a | t | mined | 2026-10-19 | 365d | corpus/knowledge/myth-symbol/ritual-liminality.md |",
    ]
    reg = ("# Sources\n\n## Registry\n\n| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |\n"
           "|---|---|---|---|---|---|---|---|---|---|---|\n" + "\n".join(rows) + "\n")
    with open(os.path.join(fx, "corpus", "SOURCES.md"), "w") as fh:
        fh.write(reg)
    base = commit("base fixture")
    frozen = {
        "round": 82, "base": base,
        "claims": [{"id": "D", "entry82": {
            "entry_path": "corpus/knowledge/myth-symbol/guest.md",
            "entry_sha256": hashlib.sha256(entry.encode()).hexdigest(),
            "entry_min_bytes": 100, "entry_max_bytes": 100000,
            "entry_markers": ["## 6. Lore handoff", "- couples:"],
            "canon_markers": ["decides nothing about what is true in any world", "never here"],
            "row_ids": ["S904", "S907"], "row_kinds": {"S904": "book", "S907": "book"},
            "row_tiers": {"S904": "A", "S907": "B"},
            "row_status": {"S904": "mined", "S907": "rejected"},
            "row_opened": {"S904": "2026-11-04", "S907": "2026-11-04"},
            "evidence_dir": "reports/round-82/evidence/",
            "lint_tool_path": "tools/check-cited-lines.py",
            "lint_tool_sha256": hashlib.sha256(lint.encode()).hexdigest(),
            "registry_path": "corpus/SOURCES.md",
            "rowcount_before": 1, "rowcount_min_after": 3,
            "allowed_d_paths": ["corpus/knowledge/myth-symbol/guest.md", "corpus/SOURCES.md",
                                "reports/round-82/"],
            "legs": LEGS,
        }}],
    }
    os.makedirs(os.path.join(fx, "reports", "round-82"), exist_ok=True)
    with open(os.path.join(fx, "reports", "round-82", "claims.json"), "w") as fh:
        json.dump(frozen, fh)
    freeze = commit("freeze")

    with open(os.path.join(fx, "corpus", "knowledge", "myth-symbol", "guest.md"), "w") as fh:
        fh.write(entry)
    with open(os.path.join(fx, "corpus", "SOURCES.md"), "w") as fh:
        fh.write(reg + "| S904 | src | book | A | s | a \u300cstrangers and beggars are from Jove\u300d | teaches | mined | 2026-11-04 | 365d | corpus/knowledge/myth-symbol/guest.md |\n"
                     "| S907 | src | book | B | s | none quotable | rejected: stub; flip: a server-side transcription appears | rejected | 2026-11-04 | 365d | \u2014 |\n")
    os.makedirs(os.path.join(fx, "reports", "round-82", "evidence"))
    for rid in ("S904", "S907"):
        with open(os.path.join(fx, "reports", "round-82", "evidence", rid + ".txt"), "w") as fh:
            fh.write("row: %s\nurl: x\nquote: y\n" % rid)
    lands = commit("lands")
    wd = os.path.join(work, "fx-d-work")
    os.makedirs(wd, exist_ok=True)

    r = counter(["--root", fx, "--lands", lands, "--freeze", freeze, "--work", wd])
    check("clean fixture PASS", r.returncode == 0 and "%s: PASS legs=%d/%d" % (LABEL, len(LEGS), len(LEGS)) in r.stdout,
          r.stdout[-400:] + r.stderr[-200:])
    check("clean receipt prints frozen legs", ("# frozen legs: %d (" % len(LEGS)) in r.stdout)
    check("clean receipt stamps revisions",
          ("# stamped revision: %s" % lands) in r.stdout and ("# evaluated revision: %s" % lands) in r.stdout)

    r = counter(["--root", fx, "--lands", base, "--freeze", freeze, "--work", wd])
    check("do-nothing control refused", r.returncode == 2 and "do-nothing control" in r.stdout, r.stdout)

    r = counter(["--root", fx, "--lands", "f" * 40, "--freeze", freeze, "--work", wd])
    check("non-commit lands refused", r.returncode == 2 and "legs=0/" in r.stdout, r.stdout)

    r = counter(["--root", fx, "--lands", lands, "--freeze", "0000", "--work", wd])
    check("non-40-hex freeze refused", r.returncode == 2, r.stdout)

    r = counter(["--root", fx, "--lands", freeze, "--freeze", freeze, "--work", wd])
    check("lands==freeze graded not passed", r.returncode == 1 and "legs=0/" not in r.stdout and "LEG FAIL ENTRY" in r.stdout, "rc=%d " % r.returncode + r.stdout[-200:])

    r = counter(["--root", fx, "--lands", lands, "--freeze", freeze, "--work", "/nonexistent-work"])
    check("missing --work refused", r.returncode == 2 and "existing scratch" in r.stdout, r.stdout)

    # legcount: freeze a claims.json whose legs differ
    doc = dict(frozen)
    doc["claims"] = [{"id": "D", "entry82": dict(frozen["claims"][0]["entry82"], legs=["ENTRY"])}]
    with open(os.path.join(fx, "reports", "round-82", "claims.json"), "w") as fh:
        json.dump(doc, fh)
    bad = commit("bad legs")
    r = counter(["--root", fx, "--lands", bad, "--freeze", bad, "--work", wd])
    check("LEGCOUNT refused", r.returncode == 2 and "LEGCOUNT" in r.stdout, r.stdout)
    with open(os.path.join(fx, "reports", "round-82", "claims.json"), "w") as fh:
        json.dump(frozen, fh)
    commit("restore")

    # junk: entry deleted
    os.remove(os.path.join(fx, "corpus", "knowledge", "myth-symbol", "guest.md"))
    j1 = commit("junk: entry deleted")
    r = counter(["--root", fx, "--lands", j1, "--freeze", freeze, "--work", wd])
    check("junk entry-deleted fails ENTRY", "LEG FAIL ENTRY" in r.stdout and r.returncode == 1, r.stdout[-300:])
    with open(os.path.join(fx, "corpus", "knowledge", "myth-symbol", "guest.md"), "w") as fh:
        fh.write(entry)
    commit("restore entry")

    # junk: registry row count regressed
    with open(os.path.join(fx, "corpus", "SOURCES.md"), "w") as fh:
        fh.write(reg)
    j2 = commit("junk: rows removed")
    r = counter(["--root", fx, "--lands", j2, "--freeze", freeze, "--work", wd])
    check("junk rows-removed fails ROWCOUNT", "LEG FAIL ROWCOUNT" in r.stdout, r.stdout[-300:])
    with open(os.path.join(fx, "corpus", "SOURCES.md"), "w") as fh:
        fh.write(reg + "| S904 | src | book | A | s | a \u300cstrangers and beggars are from Jove\u300d | teaches | mined | 2026-11-04 | 365d | corpus/knowledge/myth-symbol/guest.md |\n"
                     "| S907 | src | book | B | s | none quotable | rejected: stub; flip: a server-side transcription appears | rejected | 2026-11-04 | 365d | \u2014 |\n")
    commit("restore rows")

    # junk: quoted anchor over 25 words
    long_row = reg + "| S904 | src | book | A | s | a \u300c" + " ".join(["word"] * 26) + "\u300d | mined | 2026-11-04 | 365d | corpus/knowledge/myth-symbol/guest.md |\n"
    with open(os.path.join(fx, "corpus", "SOURCES.md"), "w") as fh:
        fh.write(long_row)
    j3 = commit("junk: long anchor")
    r = counter(["--root", fx, "--lands", j3, "--freeze", freeze, "--work", wd])
    check("junk long-anchor fails ROWS", "LEG FAIL ROWS" in r.stdout, r.stdout[-300:])

    print("SELFTEST-D82: %s (%d checks)" % ("PASS" if ok == total else "FAIL", total))
    return 0 if ok == total else 1


def main_entry():
    argv = sys.argv[1:]
    if "--selftest" in argv:
        import tempfile
        work = None
        for i, a in enumerate(argv):
            if a == "--work" and i + 1 < len(argv):
                work = argv[i + 1]
        work = work or tempfile.mkdtemp(prefix="d82-")
        os.makedirs(work, exist_ok=True)
        return selftest(work)
    return main()


if __name__ == "__main__":
    sys.exit(main_entry())
