#!/usr/bin/env python3
r"""Round-80 claim D -- maritime-seafaring-lexicon entry counter.

Claim D adds `corpus/knowledge/culture-material/maritime-seafaring-lexicon.md`
grounded in three SOURCES rows opened this round (S898 Falconer 1769, S899
Smyth 1867, S900 Britannica 1911/Ship). This counter grades the LANDED bytes
read from the lands commit (`git show <lands>:<path>`), never a moving
worktree. The clause-scoping lint it executes is a repository tool, so per
QUALITY 28 its authority is pinned: the counter reads it from the lands
commit and refuses to run it unless its sha256 equals the frozen pin.

Reads: committed git objects only (`git show`, `git rev-parse`, `git
rev-list`, `git diff-tree`, `git cat-file`, `git ls-tree`) plus the pinned
lint tool run as `python -B <extracted>`. Constants come from the FREEZE
commit: `git show <freeze>:reports/round-80/claims.json`, claim id "D",
object "entry80".

CLI
  python -B reports/round-80/accept-d.py --root . --lands <40hex> \
      --freeze <40hex> --work <dir>
  python -B reports/round-80/accept-d.py --selftest --work <dir> [--keep]

EXIT 0 every leg passes; 1 any leg fails; 2 refusal or input error.
Refusals print `ACCEPT-D-80: FAIL legs=0/7 (refused: ...)` and exit 2:
lands or freeze not 40-hex or not commits; freeze has no readable claims.json;
LEGCOUNT (frozen leg list differs from LEG_TABLE); lands equal to the frozen
base; freeze or base not on lands' first-parent chain; the lint tool at lands
not matching its frozen sha256. `--work` must name an existing directory.
A graded run writes its verdict record to `<work>/accept-d-80-<lands12>.txt`.

LEGS (the frozen leg list must equal LEG_TABLE, in order)
  FROZENCFG  claims.json at lands is byte-identical to the freeze blob.
  ENTRY      the entry exists at lands, inside the frozen byte bounds, its
             sha256 equals the frozen pin, its header markers are present,
             and it is absent at base.
  LINT       the lands copy of tools/check-cited-lines.py matches its frozen
             sha256 and prints 0 finding(s) for the extracted entry.
  ROWS       SOURCES.md at lands carries exactly one row per frozen row id
             with the frozen kind and tier cells, status mined, used-by
             naming the entry; each row is absent at base; each row's
             capture record exists at lands under the frozen evidence dir
             and names the row id.
  COUPLES    every .md filename token in the entry's `couples:` line
             resolves at lands to a path under corpus/.
  NOCANON    the entry carries the canon-hygiene markers.
  SEPARABLE  every path changed between freeze and lands is inside the
             frozen allowed_d_paths or sibling_paths carve-outs.

Limit, stated: this counter proves the entry and its three opened rows land
with the declared shape and a clean clause-scoping lint. It does not certify
the entry's craft quality, that the quoted passages mean what the entry
restates, or that the civilization-scoped neighbours agree with the one-way
pointers; those stay review-only per QUALITY 11.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

ROUND = 80
ROUND_TAG = "ACCEPT-D-80"
CLAIM_ID = "D"
CLAIMS_PATH = "reports/round-80/claims.json"
LEG_TABLE = ("FROZENCFG", "ENTRY", "LINT", "ROWS", "COUPLES", "NOCANON",
             "SEPARABLE")
CFG_KEYS = ("entry_path", "entry_sha256", "entry_min_bytes",
            "entry_max_bytes", "entry_markers", "canon_markers", "row_ids",
            "row_kinds", "row_tiers", "evidence_dir", "lint_tool_path",
            "lint_tool_sha256", "registry_path", "allowed_d_paths",
            "sibling_paths", "base", "legs")

HEX40 = re.compile(r"^[0-9a-f]{40}$")
GIT_ENV_DROP = ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_NAMESPACE",
                "GIT_OBJECT_DIRECTORY")


class Refusal(Exception):
    """Input or constant problem: exit 2, no leg verdicts."""


class GitFail(Exception):
    """A git plumbing call failed where a result was required."""


def _env(extra=None):
    env = {k: v for k, v in os.environ.items() if k not in GIT_ENV_DROP}
    env.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1",
               LC_ALL="C")
    if extra:
        env.update(extra)
    return env


def git(root, *args, check=True):
    proc = subprocess.run(["git", "-C", root, *args], capture_output=True,
                          env=_env())
    if check and proc.returncode != 0:
        raise GitFail("git %s exit=%d: %s"
                      % (" ".join(args), proc.returncode,
                         proc.stderr.decode("utf-8", "replace")[:200]))
    return proc


def show(root, rev, path):
    proc = git(root, "show", "%s:%s" % (rev, path), check=False)
    if proc.returncode != 0:
        return None
    return proc.stdout


def commit_id(root, rev):
    proc = git(root, "rev-parse", "--verify", "--quiet", rev + "^{commit}",
               check=False)
    if proc.returncode != 0:
        return None
    return proc.stdout.decode().strip()


def changes_between(root, a, b):
    proc = git(root, "diff-tree", "--name-status", "-r", "--no-renames",
               "-z", a, b)
    out = proc.stdout.decode("utf-8", "surrogateescape")
    recs = [r for r in out.split("\x00") if r]
    fixed = []
    i = 0
    while i + 1 < len(recs):
        st, p = recs[i], recs[i + 1]
        if st and st[0] in "ACDMRT":
            fixed.append((st[0], p))
        i += 2
    return fixed


def on_first_parent(root, anc, desc):
    cur = commit_id(root, desc)
    anc_id = commit_id(root, anc)
    if cur is None or anc_id is None:
        return False
    seen = 0
    while cur is not None:
        if cur == anc_id:
            return True
        seen += 1
        if seen > 100000:
            return False
        proc = git(root, "rev-parse", "--verify", "--quiet", cur + "^",
                   check=False)
        cur = proc.stdout.decode().strip() if proc.returncode == 0 else None
    return False


def read_frozen(root, freeze):
    raw = show(root, freeze, CLAIMS_PATH)
    if raw is None:
        raise Refusal("frozen %s unreadable at freeze %s"
                      % (CLAIMS_PATH, freeze))
    try:
        doc = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as exc:
        raise Refusal("frozen claims.json not valid JSON: %s" % exc)
    claims = {c.get("id"): c for c in doc.get("claims", [])
              if isinstance(c, dict)}
    cfg = claims.get(CLAIM_ID, {}).get("entry80")
    if not isinstance(cfg, dict):
        raise Refusal("frozen claims.json has no claims[D].entry80 object")
    missing = [k for k in CFG_KEYS if k not in cfg]
    if missing:
        raise Refusal("frozen entry80 cfg missing keys: %s"
                      % ",".join(missing))
    if list(cfg["legs"]) != list(LEG_TABLE):
        raise Refusal("LEGCOUNT: frozen legs %s != implemented %s"
                      % (",".join(cfg["legs"]), ",".join(LEG_TABLE)))
    return cfg, raw


def run_tool(tool, args, work, timeout=120):
    try:
        proc = subprocess.run([sys.executable, "-B", tool] + args,
                              capture_output=True, timeout=timeout,
                              cwd=work,
                              env=_env({"PYTHONDONTWRITEBYTECODE": "1"}))
    except subprocess.TimeoutExpired:
        return 124, b"", b"timeout"
    except OSError as exc:
        return 126, b"", str(exc).encode()
    return proc.returncode, proc.stdout, proc.stderr


def _self_sha():
    try:
        with open(os.path.abspath(__file__), "rb") as fh:
            return hashlib.sha256(fh.read()).hexdigest()
    except OSError:
        return "<unreadable>"


def _last(out):
    return (out.strip().splitlines() or ["<none>"])[-1][:160]


def leg_frozencfg(root, lands, ctx):
    raw = show(root, lands, CLAIMS_PATH)
    lb = hashlib.sha256(raw).hexdigest() if raw is not None else None
    fb = ctx["claims_freeze_sha"]
    return lb == fb, ["claims.json sha256 at lands %s, at freeze %s"
                      % (lb, fb)]


def leg_entry(root, lands, ctx):
    cfg = ctx["cfg"]
    raw = show(root, lands, cfg["entry_path"])
    if raw is None:
        return False, ["%s absent at lands" % cfg["entry_path"]]
    problems = []
    lo, hi = int(cfg["entry_min_bytes"]), int(cfg["entry_max_bytes"])
    if not (lo <= len(raw) <= hi):
        problems.append("entry bytes %d outside [%d, %d]"
                        % (len(raw), lo, hi))
    sha = hashlib.sha256(raw).hexdigest()
    if sha != cfg["entry_sha256"]:
        problems.append("entry sha256 %s != frozen %s"
                        % (sha, cfg["entry_sha256"]))
    text = raw.decode("utf-8", "replace")
    for marker in cfg["entry_markers"]:
        if marker not in text:
            problems.append("header marker %r absent" % marker)
    raw_b = show(root, cfg["base"], cfg["entry_path"])
    if raw_b is not None:
        problems.append("entry already present at base")
    return not problems, ["entry sha256 %s, %d bytes" % (sha, len(raw))] + \
        ["ERROR %s" % p for p in problems]


def leg_lint(root, lands, ctx):
    cfg = ctx["cfg"]
    raw_entry = show(root, lands, cfg["entry_path"])
    if raw_entry is None:
        return False, ["entry absent at lands"]
    tool_raw = show(root, lands, cfg["lint_tool_path"])
    if tool_raw is None:
        return False, ["%s absent at lands" % cfg["lint_tool_path"]]
    sha = hashlib.sha256(tool_raw).hexdigest()
    if sha != cfg["lint_tool_sha256"]:
        return False, ["lint tool sha256 %s != frozen pin %s (QUALITY 28: "
                       "authority not pinned at freeze)"
                       % (sha, cfg["lint_tool_sha256"])]
    work = ctx["work"]
    tool = os.path.join(work, "pinned-check-cited-lines.py")
    with open(tool, "wb") as fh:
        fh.write(tool_raw)
    entry = os.path.join(work, "graded-entry.md")
    with open(entry, "wb") as fh:
        fh.write(raw_entry)
    code, out, err = run_tool(tool, [entry], work)
    text = (out + err).decode("utf-8", "replace")
    ok = code == 0 and "0 finding(s)" in text
    return ok, ["lint tool sha256 %s == pin" % sha,
                "exit=%d (want 0); output tail: %s" % (code, _last(text))]


def leg_rows(root, lands, ctx):
    cfg = ctx["cfg"]
    raw = show(root, lands, cfg["registry_path"])
    if raw is None:
        return False, ["registry unreadable at lands"]
    text = raw.decode("utf-8", "replace")
    problems, details = [], []
    for sid in cfg["row_ids"]:
        rows = [ln for ln in text.splitlines()
                if re.match(r"^\| ?%s ?\|" % sid, ln)]
        if len(rows) != 1:
            problems.append("%d %s rows at lands (want 1)" % (len(rows), sid))
            continue
        cells = [c.strip() for c in rows[0].split("|")]
        if len(cells) < 12:
            problems.append("%s row has <11 cells" % sid)
            continue
        kind, tier, status, used = cells[3], cells[4], cells[8], cells[11]
        if kind != cfg["row_kinds"][sid]:
            problems.append("%s kind %r != %r"
                            % (sid, kind, cfg["row_kinds"][sid]))
        if tier != cfg["row_tiers"][sid]:
            problems.append("%s tier %r != %r"
                            % (sid, tier, cfg["row_tiers"][sid]))
        if status != "mined":
            problems.append("%s status %r != mined" % (sid, status))
        entry_name = os.path.basename(cfg["entry_path"])
        if entry_name not in used:
            problems.append("%s used-by %r does not name the entry"
                            % (sid, used[:60]))
        details.append("%s: kind=%s tier=%s status=%s" % (sid, kind, tier,
                                                          status))
        cap = show(root, lands, cfg["evidence_dir"] + sid + ".txt")
        if cap is None:
            problems.append("capture record %s%s.txt absent at lands"
                            % (cfg["evidence_dir"], sid))
        elif sid not in cap.decode("utf-8", "replace"):
            problems.append("capture record for %s does not name the row id"
                            % sid)
    raw_b = show(root, cfg["base"], cfg["registry_path"])
    if raw_b is not None:
        base_text = raw_b.decode("utf-8", "replace")
        for sid in cfg["row_ids"]:
            if re.search(r"^\| ?%s ?\|" % sid, base_text, re.M):
                problems.append("%s row already present at base" % sid)
    return not problems, details + ["ERROR %s" % p for p in problems]


def leg_couples(root, lands, ctx):
    cfg = ctx["cfg"]
    raw = show(root, lands, cfg["entry_path"])
    if raw is None:
        return False, ["entry absent at lands"]
    text = raw.decode("utf-8", "replace")
    cline = None
    for ln in text.splitlines():
        if ln.startswith("- couples:"):
            cline = ln
            break
    if cline is None:
        return False, ["entry carries no couples: line"]
    tokens = sorted(set(re.findall(r"[A-Za-z0-9][A-Za-z0-9._-]*\.md", cline)))
    listing = git(root, "ls-tree", "-r", "--name-only", lands,
                  "corpus/").stdout.decode().split()
    known = set(os.path.basename(p) for p in listing)
    problems = []
    for t in tokens:
        if t not in known:
            problems.append("couples token %s resolves to no path under "
                            "corpus/ at lands" % t)
    return not problems, ["couples tokens: %d (%s)"
                          % (len(tokens), ", ".join(tokens[:8]) +
                             (" ..." if len(tokens) > 8 else ""))] + \
        ["ERROR %s" % p for p in problems]


def leg_nocanon(root, lands, ctx):
    cfg = ctx["cfg"]
    raw = show(root, lands, cfg["entry_path"])
    if raw is None:
        return False, ["entry absent at lands"]
    text = raw.decode("utf-8", "replace")
    problems = []
    for marker in cfg["canon_markers"]:
        if marker not in text:
            problems.append("canon-hygiene marker %r absent" % marker)
    return not problems, ["canon markers present: %d/%d"
                          % (len(cfg["canon_markers"]) - len(problems),
                             len(cfg["canon_markers"]) )] + \
        ["ERROR %s" % p for p in problems]


def _in(path, prefixes):
    return any(path == p.rstrip("/") or path.startswith(p)
               for p in prefixes)


def leg_separable(root, lands, ctx):
    cfg = ctx["cfg"]
    allowed = list(cfg["allowed_d_paths"]) + list(cfg["sibling_paths"])
    changes = changes_between(root, ctx["freeze"], lands)
    bad = [(s, p) for s, p in changes if not _in(p, allowed)]
    return not bad, ["changed paths freeze..lands %d; outside allowed %d"
                     % (len(changes), len(bad)),
                     "allowed: %s" % ", ".join(cfg["allowed_d_paths"]),
                     "sibling carve-outs: %s" % ", ".join(cfg["sibling_paths"])] + \
        ["OUTSIDE %s %s" % (s, p) for s, p in bad]


def grade(root, lands, freeze, work):
    cfg, cfg_raw = read_frozen(root, freeze)
    ctx = {"cfg": cfg, "freeze": freeze, "work": work,
           "claims_freeze_sha": hashlib.sha256(cfg_raw).hexdigest()}

    out = ["# frozen legs: %d (%s)" % (len(LEG_TABLE), ", ".join(LEG_TABLE)),
           "# stamped revision: %s" % lands,
           "# evaluated revision: %s" % lands,
           "# measured revision (lane main): %s" % lands,
           "# freeze: %s" % freeze,
           "# tree: %s" % git(root, "rev-parse",
                              lands + "^{tree}").stdout.decode().strip(),
           "# counter sha256 (self): %s" % _self_sha()]
    legs = {
        "FROZENCFG": lambda: leg_frozencfg(root, lands, ctx),
        "ENTRY": lambda: leg_entry(root, lands, ctx),
        "LINT": lambda: leg_lint(root, lands, ctx),
        "ROWS": lambda: leg_rows(root, lands, ctx),
        "COUPLES": lambda: leg_couples(root, lands, ctx),
        "NOCANON": lambda: leg_nocanon(root, lands, ctx),
        "SEPARABLE": lambda: leg_separable(root, lands, ctx),
    }
    passed = 0
    for name in LEG_TABLE:
        try:
            ok, details = legs[name]()
        except (GitFail, Refusal, OSError, ValueError) as exc:
            ok, details = False, ["leg error: %s" % exc]
        out.append("LEG %s %s" % ("PASS" if ok else "FAIL", name))
        out += ["  %s" % d for d in details]
        passed += 1 if ok else 0
    verdict = "%s: %s legs=%d/%d" % (
        ROUND_TAG, "PASS" if passed == len(LEG_TABLE) else "FAIL",
        passed, len(LEG_TABLE))
    out.append(verdict)
    rec = os.path.join(work, "accept-d-80-%s.txt" % lands[:12])
    with open(rec, "w") as fh:
        fh.write("\n".join(out) + "\n")
    print("\n".join(out))
    return 0 if passed == len(LEG_TABLE) else 1


# ------------------------------------------------------------------ selftest

def _st_fixture_repo(work):
    """Deterministic fixture: base -> freeze -> lands with entry missing,
    then lands2 with a mutant entry carrying a table-row S-id."""
    fix = os.path.join(work, "fixture")
    os.mkdir(fix)
    env = _env({"GIT_AUTHOR_NAME": "d80", "GIT_AUTHOR_EMAIL": "d80@invalid",
                "GIT_COMMITTER_NAME": "d80", "GIT_COMMITTER_EMAIL": "d80@invalid"})

    def fg(*a):
        return subprocess.run(["git", "-C", fix, *a], env=env,
                              capture_output=True, check=True
                              ).stdout.decode().strip()

    def put(rel, data):
        p = os.path.join(fix, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8", newline="\n") as fh:
            fh.write(data)

    def commit(msg):
        subprocess.run(["git", "-C", fix, "add", "-A"], env=env, check=True)
        subprocess.run(["git", "-C", fix, "-c", "commit.gpgsign=false",
                        "commit", "-q", "--allow-empty", "-m", msg],
                       env=env, check=True)
        return fg("rev-parse", "HEAD")

    fg("init", "-q", "-b", "main")
    put("README.md", "fixture base\n")
    base = commit("base")
    entry = ("# Entry\n\n- topic: seafaring\n- gap filled: none\n"
             "- couples: `README.md` (the fixture readme)\n"
             "- verified-at: now\n- recheck: 180d\n- scope: fixture\n\n"
             "## 1. Partial owners\n\n- none\n\n"
             "## 2. Six design decisions\n\n| a | b |\n|---|---|\n| x | y |\n\n"
             "## 3. Attested anchors (one source per line)\n\n"
             "- alpha line. (S898)\n- beta line. (S899)\n\n"
             "## 6. Lore handoff\n\nIt decides nothing about what is true "
             "in any world and never records it as canon.\n")
    lint = show_here("tools/check-cited-lines.py")
    put("tools/check-cited-lines.py", lint)
    cfg = claims_cfg(base)
    claims = {"round": ROUND, "claims": [{"id": CLAIM_ID, "entry80": cfg}]}
    put(CLAIMS_PATH, json.dumps(claims, indent=1) + "\n")
    freeze = commit("freeze")
    return fix, base, freeze, entry, commit


def claims_cfg(base):
    import hashlib as _h
    lint_sha = _h.sha256(show_here("tools/check-cited-lines.py")
                         .encode("utf-8")).hexdigest()
    return {"entry_path": "entry.md", "entry_sha256": "f" * 64,
            "entry_min_bytes": 10, "entry_max_bytes": 100000,
            "entry_markers": ["- topic: seafaring", "## 3. Attested anchors"],
            "canon_markers": ["never records it as canon"],
            "row_ids": ["S898", "S899"], "row_kinds": {"S898": "dictionary",
                                                       "S899": "dictionary"},
            "row_tiers": {"S898": "A", "S899": "A"},
            "evidence_dir": "evidence/", "lint_tool_path":
            "tools/check-cited-lines.py", "lint_tool_sha256": lint_sha,
            "registry_path": "sources.md",
            "allowed_d_paths": ["entry.md", "sources.md", "evidence/"],
            "sibling_paths": [], "base": base, "legs": list(LEG_TABLE)}


def show_here(rel):
    here = os.path.dirname(os.path.abspath(__file__))
    root = os.path.abspath(os.path.join(here, "..", ".."))
    with open(os.path.join(root, rel), encoding="utf-8") as fh:
        return fh.read()


def selftest(work, keep):
    st = os.path.join(work, "selftest-d80")
    if os.path.exists(st):
        raise Refusal("selftest scratch %s already exists; remove it first"
                      % st)
    os.mkdir(st)
    problems = []
    print("selftest-d80: work=%s" % st)
    fix, base, freeze, entry_text, commit = _st_fixture_repo(st)

    sources = ("| id | subject | kind | tier | teaches | anchor | so | "
               "status | opened | recheck | used-by |\n"
               "|---|---|---|---|---|---|---|---|---|---|---|\n"
               "| S898 | falconer | dictionary | A | t | a | s | mined | "
               "2026-10-31 | 180d | entry.md |\n"
               "| S899 | smyth | dictionary | A | t | a | s | mined | "
               "2026-10-31 | 180d | entry.md |\n")
    evidence = "evidence/S898.txt: S898 capture\n"
    os.makedirs(os.path.join(fix, "evidence"), exist_ok=True)
    with open(os.path.join(fix, "evidence", "S898.txt"), "w") as fh:
        fh.write(evidence)
    with open(os.path.join(fix, "sources.md"), "w", encoding="utf-8") as fh:
        fh.write(sources)

    # lands2: entry lands but S899 capture record missing -> ROWS FAIL,
    # ENTRY sha mismatch (fake pin) -> ENTRY FAIL, others graded as-is
    with open(os.path.join(fix, "entry.md"), "w", encoding="utf-8") as fh:
        fh.write(entry_text)
    lands2 = commit("lands entry")

    def run(lands, freeze_rev):
        proc = subprocess.run(
            [sys.executable, "-B", os.path.abspath(__file__), "--root", fix,
             "--lands", lands, "--freeze", freeze_rev, "--work", st],
            capture_output=True)
        return proc.returncode, proc.stdout.decode("utf-8", "replace")

    cases = [
        ("lands==base refused", base, freeze, 2, ["refused"]),
        ("entry lands, pins unfixed", lands2, freeze, 1,
         ["LEG FAIL ENTRY", "LEG FAIL ROWS", "LEG PASS LINT",
          "LEG PASS FROZENCFG"]),
        ("non-hex lands refused", "z" * 40, freeze, 2, ["refused"]),
        ("off-chain freeze refused", lands2, base, 2, ["refused"]),
    ]
    for name, lands, freeze_rev, want_code, needles in cases:
        code, out = run(lands, freeze_rev)
        missing = [n for n in needles if n not in out]
        ok = code == want_code and not missing
        print("  %s -> exit=%d want=%d missing=%s %s"
              % (name, code, want_code, missing or "-",
                 "OK" if ok else "BAD"))
        if not ok:
            problems.append("%s: exit=%d missing=%s" % (name, code, missing))

    # mutant case: entry with a table-row S-id must fail LINT
    mut = entry_text.replace("| x | y |", "| x | y (S899) |")
    with open(os.path.join(fix, "entry.md"), "w", encoding="utf-8") as fh:
        fh.write(mut)
    lands3 = commit("lands mutant entry")
    code, out = run(lands3, freeze)
    ok = code == 1 and "LEG FAIL LINT" in out
    print("  mutant table-row S-id -> exit=%d LINT FAIL shown=%s %s"
          % (code, "LEG FAIL LINT" in out, "OK" if ok else "BAD"))
    if not ok:
        problems.append("mutant LINT: exit=%d" % code)

    ok = not problems
    print("SELFTEST-D80: %s" % ("PASS" if ok else "FAIL %s" % problems))
    if not keep:
        shutil.rmtree(st, ignore_errors=True)
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Round-80 D maritime-seafaring-lexicon entry counter.")
    ap.add_argument("--root")
    ap.add_argument("--lands")
    ap.add_argument("--freeze")
    ap.add_argument("--work")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--keep", action="store_true")
    args = ap.parse_args(argv)
    try:
        if args.selftest:
            if not args.work or not os.path.isdir(args.work):
                raise Refusal("--work must name an existing scratch directory "
                              "(explicit; no fallback)")
            return selftest(args.work, args.keep)
        for flag in ("--root", "--lands", "--freeze", "--work"):
            if getattr(args, flag[2:]) is None:
                raise Refusal("missing %s" % flag)
        if not os.path.isdir(args.work):
            raise Refusal("--work must name an existing scratch directory "
                          "(explicit; no fallback)")
        root = os.path.abspath(args.root)
        lands, freeze = args.lands, args.freeze
        for label, rev in (("lands", lands), ("freeze", freeze)):
            if not HEX40.match(rev):
                raise Refusal("%s is not a 40-hex commit" % label)
            if commit_id(root, rev) is None:
                raise Refusal("%s %s is not a commit in %s"
                              % (label, rev, root))
        cfg0, _raw = read_frozen(root, freeze)
        base = cfg0["base"]
        if lands == base:
            raise Refusal("lands equals the frozen base %s" % base)
        if not on_first_parent(root, freeze, lands):
            raise Refusal("freeze %s is not on lands %s first-parent chain"
                          % (freeze, lands))
        if not on_first_parent(root, base, lands):
            raise Refusal("base %s is not on lands %s first-parent chain"
                          % (base, lands))
        return grade(root, lands, freeze, args.work)
    except Refusal as exc:
        print("%s: FAIL legs=0/%d (refused: %s)"
              % (ROUND_TAG, len(LEG_TABLE), exc))
        return 2
    except GitFail as exc:
        print("%s: FAIL legs=0/%d (refused: %s)"
              % (ROUND_TAG, len(LEG_TABLE), exc))
        return 2


if __name__ == "__main__":
    sys.exit(main())
