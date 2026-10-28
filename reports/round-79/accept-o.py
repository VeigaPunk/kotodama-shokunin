#!/usr/bin/env python3
r"""Round-79 claim O -- ledger-token-guard acquisition counter.

Claim O acquires `tools/ledger-token-guard.py`: a bounded guard that re-runs
approved read-only ledger observations against immutable committed bytes,
refuses mutable revisions and historical argv-ledger shapes, and rejects a
recorded `observed_at_base` differing from the re-run observation (the
round-77 R78-M1 defect class) and a `stated_token` equal to the actual
observation (the vacuity class). This counter grades the LANDED tool bytes
extracted from the lands commit (`git show <lands>:<tool>`), never a moving
worktree and never a self-reported receipt.

Reads: committed git objects only (`git show`, `git rev-parse`, `git
rev-list`, `git diff-tree`, `git cat-file`) plus the extracted tool run as
`python3 -B <extracted>`. Constants come from the FREEZE commit:
`git show <freeze>:reports/round-79/claims.json`, claim id "O", object "guard".

CLI
  python3 -B reports/round-79/accept-o.py --root . --lands <40hex> \
      --freeze <40hex> --work <dir>
  python3 -B reports/round-79/accept-o.py --selftest --work <dir> [--keep]

EXIT 0 every leg passes; 1 any leg fails; 2 refusal or input error.
Refusals print `ACCEPT-O-79: FAIL legs=0/10 (refused: ...)` and exit 2: lands
or freeze not 40-hex or not commits; freeze has no readable/well-formed
claims.json; LEGCOUNT (frozen leg list differs from LEG_TABLE); lands equal
to the frozen base; freeze or base not on lands' first-parent chain. `--work`
must name an existing directory: explicit scratch, no TMPDIR fallback. A
graded run writes its verdict record to `<work>/accept-o-79-<lands12>.txt`.

LEGS (the frozen leg list must equal LEG_TABLE, in order)
  FROZENCFG  claims.json at lands is byte-identical to the freeze blob.
  TOOL       tools/ledger-token-guard.py exists at lands, 30..200 KB, its
             sha256 equals the frozen tool_sha256, and its text carries the
             contract markers and none of the banned channels.
  RED        extracted tool on the frozen red fixture ledger exits 1 and
             labels >= frozen red_bad pair failures (the round-77 probe
             ledger: recorded observations '1' vs actual '149' plus one
             stated==observed vacuity).
  GREEN      extracted tool on the frozen green fixture exits 0 with
             pairs=<frozen green_pairs>.
  SELFTEST   extracted tool `--selftest --work <dir>` exits 0, prints a
             SELFTEST line and >= frozen selftest_min_expected scenario
             verdicts, and materializes fixture git repositories under the
             work dir (canned-receipt control).
  REFUSALS   every committed fixture under the frozen refusal_dir exits
             non-zero with the stable LEDGER-TOKEN-GUARD label.
  NOSTUB     fresh-nonce oracle: the extracted tool exits 0 and carries the
             independently-observed token on a nonce ledger the counter
             materializes this run, while the shipped echo stub
             (reports/round-79/counters/junk-stub-tool.py) exits 0 echoing
             the stated token and never the observed one.
  SEPARABLE  every path changed between freeze and lands is inside the
             frozen allowed_o_paths or sibling_paths carve-outs.
  S897       corpus/SOURCES.md at lands carries exactly one `| S897 |` row,
             kind own-work, status mined, used-by naming the tool or the
             round lesson; the row is absent at base.
  SKILLROW   SKILL.md at lands carries a registry row naming the tool path
             with verdict codes 0/1/2 and a --selftest command; no such row
             at base.

Limit, stated: this counter proves the guard lands and demonstrates the
frozen contract on the frozen fixtures and a fresh oracle. It does not
certify that the guard handles every future ledger shape, that the fixture
base facts are historically true, or that the tool's selftest scenarios are
complete; those stay review-only per QUALITY 11.
"""

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

ROUND = 79
ROUND_TAG = "ACCEPT-O-79"
CLAIM_ID = "O"
CLAIMS_PATH = "reports/round-79/claims.json"
LEG_TABLE = ("FROZENCFG", "TOOL", "RED", "GREEN", "SELFTEST", "REFUSALS",
             "NOSTUB", "SEPARABLE", "S897", "SKILLROW")
CFG_KEYS = ("tool_path", "tool_sha256", "fixture_base", "red_ledger",
            "green_ledger", "red_bad", "green_pairs", "selftest_min_expected",
            "allowed_o_paths", "sibling_paths", "registry_path", "skill_path",
            "refusal_dir", "base", "legs", "tool_min_bytes", "tool_max_bytes")
TOOL_MARKERS = ("STRICT LEDGER SCHEMA", "observe_cmd", "immutable",
                "observed_at_base", "observed token")
TOOL_BANNED = ("os.system", "/bin/sh", "eval(", "exec(")
RUN_LIMIT = 120  # seconds per extracted-tool invocation
GUARD_LABEL = "LEDGER-TOKEN-GUARD"

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
    fixed = []
    for rec in out.split("\x00"):
        if not rec or "\t" not in rec:
            continue
        st, p = rec.split("\t", 1)
        fixed.append((st[0], p))
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
    cfg = claims.get(CLAIM_ID, {}).get("guard")
    if not isinstance(cfg, dict):
        raise Refusal("frozen claims.json has no claims[O].guard object")
    missing = [k for k in CFG_KEYS if k not in cfg]
    if missing:
        raise Refusal("frozen guard cfg missing keys: %s" % ",".join(missing))
    if list(cfg["legs"]) != list(LEG_TABLE):
        raise Refusal("LEGCOUNT: frozen legs %s != implemented %s"
                      % (",".join(cfg["legs"]), ",".join(LEG_TABLE)))
    return cfg, raw


def extract(root, rev, path, dest):
    raw = show(root, rev, path)
    if raw is None:
        return None
    with open(dest, "wb") as fh:
        fh.write(raw)
    return dest


def run_tool(tool, args, work, timeout=RUN_LIMIT):
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


def _guard_args(ledger_path, repo, base, work):
    return ["--ledger", ledger_path, "--repo", repo, "--base", base,
            "--work", work]


def leg_frozencfg(root, lands, ctx):
    raw = show(root, lands, CLAIMS_PATH)
    lb = hashlib.sha256(raw).hexdigest() if raw is not None else None
    fb = ctx["claims_freeze_sha"]
    return lb == fb, ["claims.json sha256 at lands %s, at freeze %s"
                      % (lb, fb)]


def leg_tool(root, lands, ctx):
    cfg = ctx["cfg"]
    raw = show(root, lands, cfg["tool_path"])
    if raw is None:
        return False, ["%s absent at lands" % cfg["tool_path"]]
    problems = []
    lo, hi = int(cfg["tool_min_bytes"]), int(cfg["tool_max_bytes"])
    if not (lo <= len(raw) <= hi):
        problems.append("tool bytes %d outside [%d, %d]" % (len(raw), lo, hi))
    sha = hashlib.sha256(raw).hexdigest()
    if sha != cfg["tool_sha256"]:
        problems.append("tool sha256 %s != frozen %s"
                        % (sha, cfg["tool_sha256"]))
    text = raw.decode("utf-8", "replace")
    for marker in cfg.get("tool_markers", TOOL_MARKERS):
        if marker not in text:
            problems.append("contract marker %r absent" % marker)
    for banned in TOOL_BANNED:
        if banned in text:
            problems.append("banned channel %r present" % banned)
    return not problems, ["tool sha256 %s, %d bytes" % (sha, len(raw))] + \
        ["ERROR %s" % p for p in problems]


def leg_red(root, lands, ctx):
    cfg = ctx["cfg"]
    led = os.path.join(ctx["work"], "red-ledger.json")
    if extract(root, ctx["freeze"], cfg["red_ledger"], led) is None:
        return False, ["red fixture %s unreadable at freeze"
                       % cfg["red_ledger"]]
    if not os.path.isfile(ctx["tool_file"]):
        return False, ["graded tool absent at lands"]
    code, out, err = run_tool(
        ctx["tool_file"],
        _guard_args(led, root, cfg["fixture_base"], ctx["work"] + "/red"),
        ctx["work"])
    text = out.decode("utf-8", "replace")
    fails = set(re.findall(r"pair ([A-Za-z0-9_-]+):", text))
    ok = code == 1 and GUARD_LABEL in text and len(fails) >= cfg["red_bad"]
    return ok, ["exit=%d (want 1); labeled pair failures=%d (want >=%d); "
                "label=%s" % (code, len(fails), cfg["red_bad"],
                              GUARD_LABEL in text),
                "pairs failed: %s" % ",".join(sorted(fails)),
                "verdict: %s" % (text.splitlines() or ["<none>"])[0][:160]]


def leg_green(root, lands, ctx):
    cfg = ctx["cfg"]
    led = os.path.join(ctx["work"], "green-ledger.json")
    if extract(root, ctx["freeze"], cfg["green_ledger"], led) is None:
        return False, ["green fixture unreadable at freeze"]
    if not os.path.isfile(ctx["tool_file"]):
        return False, ["graded tool absent at lands"]
    code, out, err = run_tool(
        ctx["tool_file"],
        _guard_args(led, root, cfg["fixture_base"], ctx["work"] + "/green"),
        ctx["work"])
    text = out.decode("utf-8", "replace")
    ok = (code == 0 and "PASS" in text
          and "pairs=%d" % cfg["green_pairs"] in text)
    return ok, ["exit=%d (want 0); PASS=%s; pairs=%d expected"
                % (code, "PASS" in text, cfg["green_pairs"]),
                "verdict: %s" % (text.splitlines() or ["<none>"])[0][:160]]


def leg_selftest(root, lands, ctx):
    cfg = ctx["cfg"]
    if not os.path.isfile(ctx["tool_file"]):
        return False, ["graded tool absent at lands"]
    stwork = os.path.join(ctx["work"], "tool-selftest")
    os.makedirs(stwork, exist_ok=True)
    code, out, err = run_tool(ctx["tool_file"],
                              ["--selftest", "--work", stwork],
                              stwork, timeout=600)
    text = out.decode("utf-8", "replace")
    fixture_dirs = []
    for base_dir, dirs, _files in os.walk(stwork):
        for d in dirs:
            if os.path.isdir(os.path.join(base_dir, d, ".git")):
                fixture_dirs.append(os.path.join(base_dir, d))
    expected = len(re.findall(r"as-expected", text))
    ok = (code == 0 and "SELFTEST" in text and fixture_dirs
          and expected >= cfg["selftest_min_expected"])
    return ok, ["exit=%d (want 0); SELFTEST line=%s; fixture repos=%d; "
                "as-expected=%d (want >=%d)"
                % (code, "SELFTEST" in text, len(fixture_dirs), expected,
                   cfg["selftest_min_expected"]),
                "tail: %s" % (text.strip().splitlines()[-1][:160]
                              if text.strip() else "no output")]


def leg_refusals(root, lands, ctx):
    cfg = ctx["cfg"]
    if not os.path.isfile(ctx["tool_file"]):
        return False, ["graded tool absent at lands"]
    details, problems = [], []
    listing = git(root, "ls-tree", "-r", "--name-only", ctx["freeze"],
                  cfg["refusal_dir"])
    cases = [p for p in listing.stdout.decode().splitlines()
             if p.endswith(".json")]
    if not cases:
        return False, ["no refusal fixtures under %s at freeze"
                       % cfg["refusal_dir"]]
    for rel in cases:
        name = os.path.basename(rel)
        src = show(root, ctx["freeze"], rel)
        if src is None:
            problems.append("%s unreadable at freeze" % rel)
            continue
        dst = os.path.join(ctx["work"], "refuse-%s" % name)
        with open(dst, "wb") as fh:
            fh.write(src)
        code, out, err = run_tool(
            ctx["tool_file"],
            _guard_args(dst, root, cfg["fixture_base"],
                        ctx["work"] + "/refuse-%s" % name),
            ctx["work"])
        text = out.decode("utf-8", "replace") + \
            err.decode("utf-8", "replace")
        if code == 0:
            problems.append("%s: exit 0 (refusal expected)" % name)
        elif GUARD_LABEL not in text:
            problems.append("%s: exit %d without stable label" % (name, code))
        else:
            details.append("%s -> exit %d labeled" % (name, code))
    return not problems, details + ["ERROR %s" % p for p in problems]


def leg_nostub(root, lands, ctx):
    """Fresh-nonce oracle: the tool must observe bytes nobody could pre-print."""
    cfg = ctx["cfg"]
    if not os.path.isfile(ctx["tool_file"]):
        return False, ["graded tool absent at lands"]
    work = ctx["work"]
    stub = os.path.join(work, "junk-stub-tool.py")
    if extract(root, ctx["freeze"],
               "reports/round-79/counters/junk-stub-tool.py", stub) is None:
        return False, ["shipped stub tool unreadable at freeze"]
    repo = os.path.join(work, "oracle-repo")
    os.makedirs(repo, exist_ok=True)
    env = _env({"GIT_AUTHOR_NAME": "oracle", "GIT_AUTHOR_EMAIL": "o@i",
                "GIT_COMMITTER_NAME": "oracle", "GIT_COMMITTER_EMAIL": "o@i"})
    nonce = hashlib.sha256(os.urandom(32)).hexdigest()[:16]
    subprocess.run(["git", "-C", repo, "init", "-q", "-b", "main"],
                   env=env, check=True)
    with open(os.path.join(repo, "probe.txt"), "w") as fh:
        fh.write("token: %s\n" % nonce)
    subprocess.run(["git", "-C", repo, "add", "probe.txt"], env=env, check=True)
    subprocess.run(["git", "-C", repo, "commit", "-q", "-m", "probe"],
                   env=env, check=True)
    rev = subprocess.run(["git", "-C", repo, "rev-parse", "HEAD"], env=env,
                         capture_output=True, check=True).stdout.decode().strip()
    ledger = {"round": ROUND, "claim": "O-oracle", "base": rev, "pairs": [{
        "id": "N1", "stated_at": "probe.txt:1",
        "stated_text": "token: %s" % nonce,
        "stated_parse": r"token: (.+)",
        "observe": {"op": "count", "rev": rev, "path": "probe.txt",
                    "pattern": "^token:"},
        "observed_at_base": "1"}]}
    led = os.path.join(work, "oracle-ledger.json")
    with open(led, "w") as fh:
        json.dump(ledger, fh)
    code_r, out_r, _e = run_tool(
        ctx["tool_file"], _guard_args(led, repo, rev, work + "/oracle-real"),
        work)
    code_s, out_s, _e2 = run_tool(
        stub, _guard_args(led, repo, rev, work + "/oracle-stub"), work)
    txt_r = out_r.decode("utf-8", "replace")
    txt_s = out_s.decode("utf-8", "replace")
    real_ok = code_r == 0 and re.search(r"observed[= ]+1\b", txt_r)
    stub_echoes_nonce = bool(re.search(r"observed[= ]+%s"
                                       % re.escape(nonce), txt_s))
    stub_has_true_token = bool(re.search(r"observed[= ]+1\b", txt_s))
    problems = []
    if not real_ok:
        problems.append("real tool exit=%d without observed=1 "
                        "(nonce unobserved?)" % code_r)
    if code_s != 0 or not stub_echoes_nonce or stub_has_true_token:
        problems.append("shipped stub failed to run its documented echo "
                        "attack (exit=%d echoes_nonce=%s true_token=%s)"
                        % (code_s, stub_echoes_nonce, stub_has_true_token))
    return not problems, [
        "real tool on nonce ledger: exit=%d observed-token=1 carried=%s"
        % (code_r, real_ok),
        "stub on same ledger: exit=%d echoes stated nonce=%s, never the "
        "observed token=%s" % (code_s, stub_echoes_nonce,
                               not stub_has_true_token)] + \
        ["ERROR %s" % p for p in problems]


def _in(path, prefixes):
    return any(path == p.rstrip("/") or path.startswith(p)
               for p in prefixes)


def leg_separable(root, lands, ctx):
    cfg = ctx["cfg"]
    allowed = cfg["allowed_o_paths"]
    siblings = cfg["sibling_paths"]
    changes = changes_between(root, ctx["freeze"], lands)
    bad = [(s, p) for s, p in changes
           if not _in(p, allowed) and not _in(p, siblings)]
    return not bad, ["changed paths freeze..lands %d; outside allowed %d"
                     % (len(changes), len(bad)),
                     "allowed: %s" % ", ".join(allowed),
                     "sibling carve-outs: %s" % ", ".join(siblings)] + \
        ["OUTSIDE %s %s" % (s, p) for s, p in bad]


def leg_s897(root, lands, ctx):
    cfg = ctx["cfg"]
    raw = show(root, lands, cfg["registry_path"])
    if raw is None:
        return False, ["registry unreadable at lands"]
    text = raw.decode("utf-8", "replace")
    rows = [ln for ln in text.splitlines()
            if re.match(r"^\| ?S897 ?\|", ln)]
    problems = []
    if len(rows) != 1:
        problems.append("%d S897 rows at lands (want 1)" % len(rows))
    else:
        cells = [c.strip() for c in rows[0].split("|")]
        if len(cells) < 12:
            problems.append("S897 row has <11 cells")
        else:
            kind, status, used = cells[3], cells[8], cells[11]
            if kind != "own-work":
                problems.append("S897 kind %r != own-work" % kind)
            if status != "mined":
                problems.append("S897 status %r != mined" % status)
            if used not in ("tools/ledger-token-guard.py",
                            "corpus/lessons/round-79.md"):
                problems.append("S897 used-by %r not a named citing path"
                                % used)
    raw_b = show(root, cfg["base"], cfg["registry_path"])
    if raw_b is not None and re.search(r"^\| ?S897 ?\|",
                                       raw_b.decode("utf-8", "replace"),
                                       re.M):
        problems.append("S897 row already present at base")
    return not problems, ["S897 row at lands: %s"
                          % (rows[0][:120] if rows else "none")] + \
        ["ERROR %s" % p for p in problems]


def leg_skillrow(root, lands, ctx):
    cfg = ctx["cfg"]
    raw = show(root, lands, cfg["skill_path"])
    if raw is None:
        return False, ["SKILL.md unreadable at lands"]
    text = raw.decode("utf-8", "replace")
    tool = cfg["tool_path"]
    rows = [ln for ln in text.splitlines()
            if tool in ln and ln.startswith("|")]
    problems = []
    if not rows:
        problems.append("no registry row names %s" % tool)
    else:
        row = rows[-1]
        for code in ("0", "1", "2"):
            if not re.search(r"(?<![0-9.])%s(?![0-9.])" % code, row):
                problems.append("row missing verdict code %s" % code)
                break
        if "--selftest" not in row:
            problems.append("row carries no --selftest command")
    raw_b = show(root, cfg["base"], cfg["skill_path"])
    if raw_b is not None and tool in raw_b.decode("utf-8", "replace"):
        problems.append("SKILL.md already names %s at base" % tool)
    return not problems, ["registry rows naming tool at lands: %d"
                          % len(rows)] + ["ERROR %s" % p for p in problems]


def grade(root, lands, freeze, work):
    cfg, cfg_raw = read_frozen(root, freeze)
    ctx = {"cfg": cfg, "freeze": freeze, "work": work,
           "claims_freeze_sha": hashlib.sha256(cfg_raw).hexdigest()}
    tool = os.path.join(work, "graded-tool.py")
    raw = show(root, lands, cfg["tool_path"])
    if raw is not None:
        with open(tool, "wb") as fh:
            fh.write(raw)
    ctx["tool_file"] = tool

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
        "TOOL": lambda: leg_tool(root, lands, ctx),
        "RED": lambda: leg_red(root, lands, ctx),
        "GREEN": lambda: leg_green(root, lands, ctx),
        "SELFTEST": lambda: leg_selftest(root, lands, ctx),
        "REFUSALS": lambda: leg_refusals(root, lands, ctx),
        "NOSTUB": lambda: leg_nostub(root, lands, ctx),
        "SEPARABLE": lambda: leg_separable(root, lands, ctx),
        "S897": lambda: leg_s897(root, lands, ctx),
        "SKILLROW": lambda: leg_skillrow(root, lands, ctx),
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
    rec = os.path.join(work, "accept-o-79-%s.txt" % lands[:12])
    with open(rec, "w") as fh:
        fh.write("\n".join(out) + "\n")
    print("\n".join(out))
    return 0 if passed == len(LEG_TABLE) else 1


# ------------------------------------------------------------------ selftest

def _st_fixture_repo(work):
    """Build a deterministic fixture repo: base -> freeze -> lands -> mutants.

    Returns (repo_dir, {name: rev})."""
    fix = os.path.join(work, "fixture")
    os.mkdir(fix)
    env = _env({"GIT_AUTHOR_NAME": "o79", "GIT_AUTHOR_EMAIL": "o79@invalid",
                "GIT_COMMITTER_NAME": "o79", "GIT_COMMITTER_EMAIL": "o79@invalid"})

    def fg(*a):
        return subprocess.run(["git", "-C", fix, *a], env=env,
                              capture_output=True, check=True).stdout.decode().strip()

    def put(rel, data):
        p = os.path.join(fix, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(data)

    def commit(msg):
        subprocess.run(["git", "-C", fix, "add", "-A"], env=env, check=True)
        subprocess.run(["git", "-C", fix, "-c", "commit.gpgsign=false",
                        "commit", "-q", "--allow-empty", "-m", msg],
                       env=env, check=True)
        return fg("rev-parse", "HEAD")

    here = os.path.dirname(os.path.abspath(__file__))
    fg("init", "-q", "-b", "main")
    put("README.md", "fixture base\n")
    base = commit("base")
    # claims.json with the real cfg shape; fixture_base names the oracle repo
    cfg = {"tool_path": "tools/ledger-token-guard.py",
           "tool_sha256": "f" * 64,
           "fixture_base": "0" * 40,
           "red_ledger": "reports/round-79/fixtures/red.json",
           "green_ledger": "reports/round-79/fixtures/green.json",
           "red_bad": 11, "green_pairs": 11, "selftest_min_expected": 1,
           "allowed_o_paths": ["tools/ledger-token-guard.py", "corpus/SOURCES.md",
                               "SKILL.md"],
           "sibling_paths": ["reports/round-79/corrections/"],
           "registry_path": "corpus/SOURCES.md", "skill_path": "SKILL.md",
           "refusal_dir": "reports/round-79/fixtures/refusals/",
           "tool_min_bytes": 1, "tool_max_bytes": 512 * 1024,
           "base": base, "legs": list(LEG_TABLE)}
    claims = {"round": ROUND, "claims": [{"id": CLAIM_ID, "guard": cfg}]}
    put(CLAIMS_PATH, json.dumps(claims, indent=1) + "\n")
    freeze = commit("freeze")
    put("tools/ledger-token-guard.py", "# stub\n" * 100)
    lands_stub = commit("lands with stub tool")
    return fix, {"base": base, "freeze": freeze, "lands_stub": lands_stub}


def selftest(work, keep):
    st = os.path.join(work, "selftest-o79")
    if os.path.exists(st):
        raise Refusal("selftest scratch %s already exists; remove it first" % st)
    os.mkdir(st)
    problems = []
    print("selftest-o79: work=%s" % st)
    repo, revs = _st_fixture_repo(st)

    def run(lands, freeze):
        proc = subprocess.run(
            [sys.executable, "-B", os.path.abspath(__file__), "--root", repo,
             "--lands", lands, "--freeze", freeze, "--work", st],
            capture_output=True)
        return proc.returncode, proc.stdout.decode("utf-8", "replace")

    cases = [
        ("lands==base refused", revs["base"], revs["freeze"], 2,
         ["refused"]),
        ("lands==freeze graded red", revs["freeze"], revs["freeze"], 1,
         ["LEG FAIL TOOL", "LEG FAIL RED", "LEG FAIL S897",
          "LEG PASS FROZENCFG"]),
        ("stub tool at lands", revs["lands_stub"], revs["freeze"], 1,
         ["LEG FAIL TOOL", "LEG FAIL RED", "LEG FAIL S897",
          "LEG PASS FROZENCFG"]),
        ("non-hex lands refused", "z" * 40, revs["freeze"], 2, ["refused"]),
        ("off-chain freeze refused", revs["lands_stub"], revs["base"], 2,
         ["refused"]),
    ]
    for name, lands, freeze, want_code, needles in cases:
        code, out = run(lands, freeze)
        missing = [n for n in needles if n not in out]
        ok = code == want_code and not missing
        print("  %s -> exit=%d want=%d missing=%s %s"
              % (name, code, want_code, missing or "-",
                 "OK" if ok else "BAD"))
        if not ok:
            problems.append("%s: exit=%d missing=%s" % (name, code, missing))
    ok = not problems
    print("SELFTEST-O79: %s" % ("PASS" if ok else "FAIL %s" % problems))
    if not keep:
        shutil.rmtree(st, ignore_errors=True)
    return 0 if ok else 1


def main(argv=None):
    ap = argparse.ArgumentParser(
        description="Round-79 O ledger-token-guard acceptance counter.")
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
