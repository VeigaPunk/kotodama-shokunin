#!/usr/bin/env python3
r"""Round-79 claim Ca -- census-receipt correction counter (DRAFT, pre-freeze).

Claim Ca grades ONE recorded mismatch: reports/round-78/telemetry/census-end.txt
line `kotodama W01 S884 tierC mined used-by=...amend-2026-10-24-r13.md` against the
used-by cell of row S884 in corpus/SOURCES.md at the measured round-78 revision
4b255745dea45a45d88b17e3c3fea4cdb6700cf7 (`...amend-2026-10-23.md`). The correction is a
NEW append-only record under reports/round-79/corrections/; the receipt is never rewritten.

Reads: committed git objects only (`git show <rev>:<path>`, `git rev-parse`,
`git rev-list`, `git diff-tree`). No worktree byte is ever opened. Every constant comes from
the FREEZE commit: `git show <freeze>:reports/round-79/claims.json`, claim id "Ca", object
"census_correction". The counter performs no network access and runs no repository tool.

CLI
  python3 -B reports/round-79/accept-ca.py --root . --lands <40hex> --freeze <40hex> --work <dir>
  python3 -B reports/round-79/accept-ca.py --derive --root . --at <40hex> --receipt-path P --registry-path Q
  python3 -B reports/round-79/accept-ca.py --selftest --work <dir> [--keep]

EXIT 0 every leg passes; 1 any leg fails; 2 refusal or input error.
Refusals print `ACCEPT-CA-79: FAIL legs=0/7 (refused: ...)` and exit 2: lands or freeze not
40-hex or not commits; freeze has no readable or well-formed claims.json; LEGCOUNT (frozen leg
list differs from LEG_TABLE); lands equal to the frozen base; freeze, measured revision or base
not on lands' first-parent chain. `--work` must name an existing directory: explicit scratch,
with no TMPDIR fallback. A graded run writes its verdict record to `<work>/accept-ca-79-<lands12>.txt`.

LEGS (the frozen leg list must equal LEG_TABLE, in order)
  FROZENCFG  claims.json at lands is present and byte-identical to the freeze blob.
  RECEIPT    the receipt blob at measured and at lands equals the frozen blob id, and the sha256
             of its bytes at lands equals the frozen digest (the original receipt is unchanged).
  DERIVE     mismatches re-derived from committed bytes (receipt used-by vs registry used-by at
             the measured revision) equal the frozen list exactly, with count expected_mismatches.
  CORRECTION every file added under correction_dir between freeze and lands is a well-formed
             key: value record binding exactly the frozen constants for one frozen mismatch row;
             exactly one correction per frozen row; no spurious row; no modified or deleted one.
  UNRESOLVED re-derived mismatches not covered by a valid correction at lands: count 0.
  SEPARABLE  every path changed between freeze and lands is an added file under correction_dir;
             O paths (tools/ledger-token-guard*, accept-o*), the registry and the receipt cannot
             change in this claim's lands.
  NOSTUB     at least one correction; no key empty, a placeholder (TODO/TBD/FIXME/XXX/n/a/?) or <...>.

Limit, stated: the derivation parses the receipt's `used-by=` lines and the registry's used-by
cell; it does not re-run sources-census.sh (a fleet-root script with no pin in this lane). A
correction whose values pass every leg is a record about the receipt, not a claim that the
S884 used-by path is right for the page; that stays review-only.
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
ROUND_TAG = "ACCEPT-CA-79"
CLAIM_ID = "Ca"
CLAIMS_PATH = "reports/round-79/claims.json"
LEG_TABLE = ("FROZENCFG", "RECEIPT", "DERIVE", "CORRECTION", "UNRESOLVED", "SEPARABLE", "NOSTUB")
CFG_KEYS = ("receipt_path", "receipt_blob", "receipt_sha256", "registry_path", "measured_revision",
            "base", "expected_mismatches", "mismatches", "correction_dir", "legs")
CORR_KEYS = ("correction-id", "row", "receipt-path", "receipt-blob", "receipt-sha256",
             "measured-revision", "registry-path", "old-token", "actual-token", "reason")
FORBIDDEN_PREFIXES = ("tools/ledger-token-guard", "reports/round-79/accept-o", "reports/round-79/guard",
                      "corpus/SOURCES.md", "reports/round-78/", "corpus/knowledge/", "corpus/lessons/")
PLACEHOLDERS = {"todo", "tbd", "fixme", "xxx", "n/a", "?"}
HEX40 = re.compile(r"^[0-9a-f]{40}$")
HEX64 = re.compile(r"^[0-9a-f]{64}$")
ROW_ID = re.compile(r"^S[0-9]{3,}$")
USED_BY_LINE = re.compile(r"^kotodama (\S+) (S[0-9]{3,}) .*used-by=(\S+)$")
CORR_LINE = re.compile(r"^([a-z][a-z0-9-]*): (.*)$")
GIT_ENV_DROP = ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE", "GIT_NAMESPACE", "GIT_OBJECT_DIRECTORY")


class Refusal(Exception):
    """Input or constant problem: exit 2, no leg verdicts."""


class GitFail(Exception):
    """A git plumbing call failed where a result was required."""


def _env():
    env = {k: v for k, v in os.environ.items() if k not in GIT_ENV_DROP}
    env.update(GIT_CONFIG_GLOBAL=os.devnull, GIT_CONFIG_NOSYSTEM="1", LC_ALL="C")
    return env


def git(root, *args, check=True):
    try:
        p = subprocess.run(["git", "-C", root, *args], capture_output=True, env=_env(), timeout=120)
    except subprocess.TimeoutExpired as e:
        raise GitFail("git %s timed out" % " ".join(args[:2])) from e
    if check and p.returncode != 0:
        raise GitFail("git %s exited %d: %s" % (" ".join(args[:2]), p.returncode,
                                                  p.stderr.decode("utf-8", "replace").strip()))
    return p


def show(root, rev, path):
    """Committed blob bytes at rev:path, or None when absent at that revision."""
    p = git(root, "show", "%s:%s" % (rev, path), check=False)
    return p.stdout if p.returncode == 0 else None


def blob_id(root, rev, path):
    p = git(root, "rev-parse", "--verify", "-q", "%s:%s" % (rev, path), check=False)
    return p.stdout.decode().strip() if p.returncode == 0 else None


def commit_id(root, rev):
    p = git(root, "rev-parse", "--verify", "-q", "%s^{commit}" % rev, check=False)
    return p.stdout.decode().strip() if p.returncode == 0 else None


def changes_between(root, freeze, lands):
    """(status, path) for every path differing between two commits; plumbing only."""
    out = git(root, "diff-tree", "-r", "-z", "--no-commit-id", "--no-renames", "--name-status",
              freeze, lands).stdout
    toks = out.split(b"\0")
    res, i = [], 0
    while i + 1 < len(toks):
        if toks[i] == b"":
            i += 1
            continue
        res.append((toks[i].decode("utf-8", "replace"), toks[i + 1].decode("utf-8", "replace")))
        i += 2
    return res


def read_frozen(root, freeze):
    raw = show(root, freeze, CLAIMS_PATH)
    if raw is None:
        raise Refusal("frozen %s unreadable at freeze %s" % (CLAIMS_PATH, freeze))
    try:
        doc = json.loads(raw.decode("utf-8"))
    except (UnicodeDecodeError, ValueError) as e:
        raise Refusal("frozen %s is not JSON: %s" % (CLAIMS_PATH, e))
    found = [c for c in doc.get("claims", []) if isinstance(c, dict) and c.get("id") == CLAIM_ID]
    if len(found) != 1 or not isinstance(found[0].get("census_correction"), dict):
        raise Refusal("frozen %s lacks exactly one Ca census_correction object" % CLAIMS_PATH)
    cfg = found[0]["census_correction"]
    missing = [k for k in CFG_KEYS if k not in cfg]
    if missing:
        raise Refusal("CONFIG: frozen census_correction missing %s" % ",".join(missing))
    if list(cfg["legs"]) != list(LEG_TABLE):
        raise Refusal("LEGCOUNT: frozen legs %s differ from the counter leg table %s"
                      % (",".join(cfg["legs"]), ",".join(LEG_TABLE)))
    for k in ("receipt_blob", "measured_revision", "base"):
        if not (isinstance(cfg[k], str) and HEX40.match(cfg[k])):
            raise Refusal("CONFIG: %s is not a 40-hex id" % k)
    if not (isinstance(cfg["receipt_sha256"], str) and HEX64.match(cfg["receipt_sha256"])):
        raise Refusal("CONFIG: receipt_sha256 is not 64-hex")
    for k in ("receipt_path", "registry_path"):
        if not (isinstance(cfg[k], str) and cfg[k]):
            raise Refusal("CONFIG: %s empty" % k)
    if not (isinstance(cfg["correction_dir"], str) and cfg["correction_dir"].endswith("/")):
        raise Refusal("CONFIG: correction_dir must be a directory path ending in /")
    if not (isinstance(cfg["expected_mismatches"], int) and cfg["expected_mismatches"] >= 1):
        raise Refusal("CONFIG: expected_mismatches must be an int >= 1")
    ms = cfg["mismatches"]
    if not (isinstance(ms, list) and len(ms) == cfg["expected_mismatches"] and all(
            isinstance(m, dict) and set(m) == {"row", "old_token", "actual_token"} for m in ms)):
        raise Refusal("CONFIG: mismatches must list expected_mismatches row/old_token/actual_token objects")
    return cfg


def parse_registry(text):
    rows, errors = {}, []
    for n, line in enumerate(text.split("\n"), 1):
        if not line.startswith("| S"):
            continue
        cells = line.split("|")
        if len(cells) != 13:
            errors.append("registry line %d: %d cells, expected 11" % (n, len(cells) - 2))
            continue
        rid = cells[1].strip()
        if not ROW_ID.match(rid):
            errors.append("registry line %d: bad id %r" % (n, rid))
        elif rid in rows:
            errors.append("registry duplicate row %s" % rid)
        else:
            rows[rid] = cells[11].strip()
    return rows, errors


def derive(receipt_raw, registry_raw):
    """Re-derive receipt used-by values that differ from the registry used-by cell."""
    try:
        receipt_text = receipt_raw.decode("utf-8")
        registry_text = registry_raw.decode("utf-8")
    except UnicodeDecodeError as e:
        return {"lines": 0, "mismatches": [], "errors": ["not UTF-8: %s" % e]}
    reg, errors = parse_registry(registry_text)
    mismatches, seen, n_lines = [], set(), 0
    for n, line in enumerate(receipt_text.split("\n"), 1):
        if "used-by=" not in line:
            continue
        n_lines += 1
        m = USED_BY_LINE.match(line)
        if not m:
            errors.append("receipt line %d: unparsed used-by line" % n)
            continue
        rid, token = m.group(2), m.group(3)
        if rid in seen:
            errors.append("receipt duplicate used-by row %s" % rid)
            continue
        seen.add(rid)
        actual = reg.get(rid, "<absent>")
        if token != actual:
            mismatches.append({"row": rid, "old_token": token, "actual_token": actual})
    if n_lines == 0:
        errors.append("receipt has no used-by lines")
    return {"lines": n_lines, "mismatches": sorted(mismatches, key=lambda m: m["row"]), "errors": errors}


def parse_correction(raw):
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError as e:
        return {}, ["not UTF-8: %s" % e]
    rec, errors = {}, []
    for n, line in enumerate(text.split("\n"), 1):
        if not line.strip() or line.startswith("#"):
            continue
        m = CORR_LINE.match(line)
        if not m:
            errors.append("line %d: not key: value" % n)
            continue
        key, val = m.group(1), m.group(2)
        if key not in CORR_KEYS:
            errors.append("line %d: unknown key %s" % (n, key))
        elif key in rec:
            errors.append("line %d: duplicate key %s" % (n, key))
        else:
            rec[key] = val
    missing = [k for k in CORR_KEYS if k not in rec]
    if missing:
        errors.append("missing keys: %s" % ",".join(missing))
    return rec, errors


def added_corrections(root, freeze, lands, corr_dir):
    changes = changes_between(root, freeze, lands)
    in_dir = [(s, p) for s, p in changes if p.startswith(corr_dir)]
    non_add = [(s, p) for s, p in in_dir if s != "A"]
    added = []
    for s, p in in_dir:
        if s != "A":
            continue
        raw = show(root, lands, p)
        rec, perr = parse_correction(raw) if raw is not None else ({}, ["unreadable at lands"])
        added.append({"path": p, "rec": rec, "errors": perr})
    return changes, added, non_add


def bindings(cfg, m):
    return [("receipt-path", cfg["receipt_path"]), ("receipt-blob", cfg["receipt_blob"]),
            ("receipt-sha256", cfg["receipt_sha256"]), ("measured-revision", cfg["measured_revision"]),
            ("registry-path", cfg["registry_path"]), ("row", m["row"]),
            ("old-token", m["old_token"]), ("actual-token", m["actual_token"])]


def _norm(ms):
    return sorted((m["row"], m["old_token"], m["actual_token"]) for m in ms)


# ---------------------------------------------------------------- legs

def leg_frozencfg(root, lands, ctx):
    freeze = ctx["freeze"]
    lb = blob_id(root, lands, CLAIMS_PATH)
    fb = blob_id(root, freeze, CLAIMS_PATH)
    if lb is None:
        return False, ["%s absent at lands" % CLAIMS_PATH]
    return lb == fb, ["%s blob at lands %s, at freeze %s" % (CLAIMS_PATH, lb, fb)]


def leg_receipt(root, lands, ctx):
    cfg = ctx["cfg"]
    rp, want = cfg["receipt_path"], cfg["receipt_blob"]
    bm = blob_id(root, cfg["measured_revision"], rp)
    bl = blob_id(root, lands, rp)
    raw = show(root, lands, rp)
    sha = hashlib.sha256(raw).hexdigest() if raw is not None else None
    ok = bm == want and bl == want and sha == cfg["receipt_sha256"]
    return ok, ["frozen blob %s" % want, "blob at measured %s" % bm, "blob at lands %s" % bl,
                "sha256 at lands %s (frozen %s)" % (sha, cfg["receipt_sha256"])]


def leg_derive(root, lands, ctx):
    cfg, d = ctx["cfg"], ctx["derived"]
    ok = (not d["errors"] and _norm(d["mismatches"]) == _norm(cfg["mismatches"])
          and len(d["mismatches"]) == cfg["expected_mismatches"])
    details = ["used-by lines %d, derived mismatches %d (frozen %d)"
               % (d["lines"], len(d["mismatches"]), cfg["expected_mismatches"])]
    details += ["MISMATCH %s old=%s actual=%s" % (m["row"], m["old_token"], m["actual_token"])
                for m in d["mismatches"]]
    details += ["ERROR %s" % e for e in d["errors"]]
    return ok, details


def leg_correction(root, lands, ctx):
    cfg = ctx["cfg"]
    frozen_by_row = {m["row"]: m for m in cfg["mismatches"]}
    errs, valid, rows = [], [], []
    for s, p in ctx["non_add"]:
        errs.append("%s %s is not an added file" % (s, p))
    for c in ctx["added"]:
        errs += ["%s: %s" % (c["path"], e) for e in c["errors"]]
        if c["errors"]:
            continue
        rec = c["rec"]
        m = frozen_by_row.get(rec["row"])
        if m is None:
            errs.append("%s: row %s is not a frozen mismatch" % (c["path"], rec["row"]))
            continue
        bad = [k for k, want in bindings(cfg, m) if rec.get(k) != want]
        if bad:
            errs.append("%s: %s differ from freeze" % (c["path"], ",".join(bad)))
            continue
        rows.append(rec["row"])
        valid.append(rec)
    if len(ctx["added"]) != cfg["expected_mismatches"]:
        errs.append("%d correction(s) added, %d frozen mismatch(es)" % (len(ctx["added"]), cfg["expected_mismatches"]))
    if sorted(rows) != sorted(frozen_by_row):
        errs.append("covered rows %s, frozen rows %s" % (sorted(rows), sorted(frozen_by_row)))
    ctx["valid"] = valid
    details = ["corrections added %d (frozen %d); valid %d" % (len(ctx["added"]), cfg["expected_mismatches"], len(valid))]
    return not errs, details + ["ERROR %s" % e for e in errs]


def leg_unresolved(root, lands, ctx):
    unresolved = []
    for m in ctx["derived"]["mismatches"]:
        covered = any(r["row"] == m["row"] and r["old-token"] == m["old_token"]
                      and r["actual-token"] == m["actual_token"] for r in ctx["valid"])
        if not covered:
            unresolved.append(m)
    ok = not unresolved and not ctx["derived"]["errors"]
    details = ["re-derived mismatches %d; covered by a valid correction %d; unresolved %d"
               % (len(ctx["derived"]["mismatches"]),
                  len(ctx["derived"]["mismatches"]) - len(unresolved), len(unresolved))]
    details += ["UNRESOLVED %s old=%s actual=%s" % (m["row"], m["old_token"], m["actual_token"]) for m in unresolved]
    return ok, details


def leg_separable(root, lands, ctx):
    corr_dir = ctx["cfg"]["correction_dir"]
    bad = [(s, p) for s, p in ctx["changes"] if not (s == "A" and p.startswith(corr_dir))]
    forbidden = sorted({p for _, p in bad if p.startswith(FORBIDDEN_PREFIXES)})
    details = ["changed paths freeze..lands %d; outside allowed set %d" % (len(ctx["changes"]), len(bad))]
    details += ["OUTSIDE %s %s" % (s, p) for s, p in bad]
    if forbidden:
        details.append("forbidden prefixes hit: %s" % ",".join(forbidden))
    return not bad, details


def leg_nostub(root, lands, ctx):
    bad = []
    for c in ctx["added"]:
        for k in CORR_KEYS:
            v = c["rec"].get(k, "").strip()
            if not v or v.lower() in PLACEHOLDERS or "<" in v or ">" in v:
                bad.append("%s:%s" % (c["path"], k))
    ok = bool(ctx["added"]) and not bad
    return ok, ["corrections %d; empty, placeholder or <...> keys: %s" % (len(ctx["added"]), ",".join(bad) or "none")]


LEGS = {
    "FROZENCFG": leg_frozencfg, "RECEIPT": leg_receipt, "DERIVE": leg_derive,
    "CORRECTION": leg_correction, "UNRESOLVED": leg_unresolved,
    "SEPARABLE": leg_separable, "NOSTUB": leg_nostub,
}


# ---------------------------------------------------------------- modes

def grade(root, lands, freeze, work):
    if not (lands and HEX40.match(lands)):
        raise Refusal("lands is not a 40-hex commit")
    if not (freeze and HEX40.match(freeze)):
        raise Refusal("freeze is not a 40-hex commit")
    if commit_id(root, lands) != lands:
        raise Refusal("lands %s is not a commit in this repository" % lands)
    if commit_id(root, freeze) != freeze:
        raise Refusal("freeze %s is not a commit in this repository" % freeze)
    cfg = read_frozen(root, freeze)
    if lands == cfg["base"]:
        raise Refusal("lands equals the frozen base %s" % cfg["base"])
    chain = set(git(root, "rev-list", "--first-parent", lands).stdout.decode().split())
    for name, rev in (("freeze", freeze), ("measured revision", cfg["measured_revision"]), ("base", cfg["base"])):
        if rev not in chain:
            raise Refusal("%s %s is not on lands %s first-parent chain" % (name, rev, lands))

    measured = cfg["measured_revision"]
    rec_raw = show(root, measured, cfg["receipt_path"])
    reg_raw = show(root, measured, cfg["registry_path"])
    if rec_raw is None or reg_raw is None:
        derived = {"lines": 0, "mismatches": [], "errors": ["receipt or registry absent at measured revision"]}
    else:
        derived = derive(rec_raw, reg_raw)
    changes, added, non_add = added_corrections(root, freeze, lands, cfg["correction_dir"])
    ctx = {"cfg": cfg, "derived": derived, "changes": changes, "added": added,
           "non_add": non_add, "valid": [], "freeze": freeze}

    results = []
    for name in LEG_TABLE:
        try:
            ok, details = LEGS[name](root, lands, ctx)
        except GitFail as e:
            ok, details = False, ["git: %s" % e]
        results.append((name, ok, details))

    tree = git(root, "rev-parse", "%s^{tree}" % lands).stdout.decode().strip()
    with open(os.path.abspath(__file__), "rb") as fh:
        self_sha = hashlib.sha256(fh.read()).hexdigest()
    out = ["# frozen legs: %d (%s)" % (len(LEG_TABLE), ", ".join(LEG_TABLE)),
           "# stamped revision: %s" % lands,
           "# evaluated revision: %s" % lands,
           "# measured revision: %s" % measured,
           "# freeze: %s" % freeze,
           "# tree: %s" % tree,
           "# counter sha256 (self): %s" % self_sha]
    passed = 0
    for name, ok, details in results:
        passed += ok
        out.append("LEG %s %s" % ("PASS" if ok else "FAIL", name))
        out += ["  " + d for d in details]
    verdict = "%s: %s legs=%d/%d" % (ROUND_TAG, "PASS" if passed == len(LEG_TABLE) else "FAIL",
                                     passed, len(LEG_TABLE))
    out.append(verdict)
    text = "\n".join(out) + "\n"
    with open(os.path.join(work, "accept-ca-79-%s.txt" % lands[:12]), "w", encoding="utf-8") as fh:
        fh.write(text)
    sys.stdout.write(text)
    return 0 if passed == len(LEG_TABLE) else 1


def derive_mode(root, at, receipt_path, registry_path):
    if not (at and HEX40.match(at)) or not receipt_path or not registry_path:
        raise Refusal("--derive needs --at <40hex>, --receipt-path and --registry-path")
    if commit_id(root, at) != at:
        raise Refusal("%s is not a commit" % at)
    rec_raw = show(root, at, receipt_path)
    reg_raw = show(root, at, registry_path)
    if rec_raw is None or reg_raw is None:
        raise Refusal("receipt or registry absent at %s" % at)
    d = derive(rec_raw, reg_raw)
    print("# derive at %s: receipt %s vs registry %s" % (at, receipt_path, registry_path))
    print("# receipt blob %s; registry blob %s" % (blob_id(root, at, receipt_path), blob_id(root, at, registry_path)))
    print("DERIVE used-by-lines=%d mismatches=%d errors=%d" % (d["lines"], len(d["mismatches"]), len(d["errors"])))
    for m in d["mismatches"]:
        print("MISMATCH %s old=%s actual=%s" % (m["row"], m["old_token"], m["actual_token"]))
    for e in d["errors"]:
        print("ERROR %s" % e)
    return 2 if d["errors"] else 0


# ---------------------------------------------------------------- selftest

ST_RECEIPT = "reports/round-78/telemetry/census-end.txt"
ST_REGISTRY = "corpus/SOURCES.md"
ST_CORR_DIR = "reports/round-79/corrections/"
ST_CORR_PATH = ST_CORR_DIR + "census-r78-S884.txt"
ST_OLD = "corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-24-r13.md"
ST_ACT = "corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md"
ST_REG_HEAD = ("| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |\n"
               "| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |\n")


def _st_row(rid, used_by):
    return ("| %s | fixture source | community | C | scope | anchor | teaches | mined | 2026-10-25 | 180d | %s |\n"
            % (rid, used_by))


def _st_receipt(s884_token):
    return ("Command: fixture census validate\nExit: 0\n"
            "kotodama W01 S881 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md\n"
            "kotodama W01 S882 tierC mined used-by=corpus/knowledge/culture-material/worldbuilding-setting-practice.md\n"
            "kotodama W01 S884 tierC mined used-by=%s\n"
            "kotodama W01 S893 tierC mined used-by=corpus/knowledge/myth-symbol/narrative-structure-frameworks.md\n"
            "kotodama ok fixture\n" % s884_token)


def _st_correction(receipt_blob, receipt_sha, measured, **kw):
    vals = {"correction-id": "CA79-R78-S884", "row": "S884", "receipt-path": ST_RECEIPT,
            "receipt-blob": receipt_blob, "receipt-sha256": receipt_sha, "measured-revision": measured,
            "registry-path": ST_REGISTRY, "old-token": ST_OLD, "actual-token": ST_ACT,
            "reason": "fixture: receipt S884 used-by names the r13 path; registry at measured names the 10-23 path"}
    vals.update(kw)
    return ("# census receipt correction (round 79, claim Ca): append-only record; receipt not rewritten\n"
            + "".join("%s: %s\n" % (k, vals[k]) for k in CORR_KEYS))


def _fixture_env():
    env = _env()
    env.update(GIT_AUTHOR_NAME="ca79", GIT_AUTHOR_EMAIL="ca79@invalid",
               GIT_COMMITTER_NAME="ca79", GIT_COMMITTER_EMAIL="ca79@invalid")
    return env


def _fixture_git(fix, *args):
    return subprocess.run(["git", "-C", fix, "-c", "core.hooksPath=/dev/null", *args],
                          capture_output=True, env=_fixture_env(), check=True).stdout.decode().strip()


def build_fixture(fix):
    """Commit the isolated fixture repository inside `fix` (created by the caller).

    Returns (base, measured, freeze, freeze_tamper, lands_clean, lands_nocorr, lands_lie, lands_rev,
    lands_recpt, lands_tamper, side, top): the base, the measured analogue of 4b255745, the freeze,
    the tampered freeze, one lands per scenario, the side branch, and the verified toplevel.
    """
    def fg(*a):
        return _fixture_git(fix, *a)

    def put(rel, data):
        p = os.path.join(fix, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(data)

    def commit(msg):
        fg("add", "-A")
        fg("-c", "commit.gpgsign=false", "commit", "-q", "--allow-empty", "-m", msg)
        return fg("rev-parse", "HEAD")

    def checkout(rev):
        fg("checkout", "-q", "--detach", rev)

    fg("init", "-q", "-b", "main")
    top = os.path.realpath(fg("rev-parse", "--show-toplevel"))
    if top != os.path.realpath(fix):
        raise Refusal("fixture toplevel %s is not %s" % (top, fix))

    put("README.md", "fixture base\n")
    base = commit("base")
    put(ST_REGISTRY, ST_REG_HEAD + _st_row("S881", "corpus/knowledge/culture-material/worldbuilding-setting-practice.md")
        + _st_row("S882", "corpus/knowledge/culture-material/worldbuilding-setting-practice.md")
        + _st_row("S884", ST_ACT) + _st_row("S893", "corpus/knowledge/myth-symbol/narrative-structure-frameworks.md"))
    put(ST_RECEIPT, _st_receipt(ST_OLD))
    measured = commit("measured (fixture analogue of 4b255745)")

    rec_blob = fg("rev-parse", "%s:%s" % (measured, ST_RECEIPT))
    with open(os.path.join(fix, ST_RECEIPT), "rb") as fh:
        rec_sha = hashlib.sha256(fh.read()).hexdigest()

    def claims(actual):
        cfg = {"receipt_path": ST_RECEIPT, "receipt_blob": rec_blob, "receipt_sha256": rec_sha,
               "registry_path": ST_REGISTRY, "measured_revision": measured, "base": base,
               "expected_mismatches": 1,
               "mismatches": [{"row": "S884", "old_token": ST_OLD, "actual_token": actual}],
               "correction_dir": ST_CORR_DIR, "legs": list(LEG_TABLE)}
        return json.dumps({"round": ROUND, "claims": [{"id": CLAIM_ID, "census_correction": cfg}]}, indent=1) + "\n"

    put(CLAIMS_PATH, claims(ST_ACT))
    freeze = commit("freeze")
    checkout(measured)
    put(CLAIMS_PATH, claims(ST_OLD))
    freeze_tamper = commit("freeze with tampered actual constant")
    checkout(freeze)

    put(ST_CORR_PATH, _st_correction(rec_blob, rec_sha, measured))
    lands_clean = commit("correction: clean")
    checkout(freeze)
    lands_nocorr = commit("empty commit on freeze (no correction)")
    checkout(freeze)
    put(ST_CORR_PATH, _st_correction(rec_blob, rec_sha, measured, **{"actual-token": ST_OLD}))
    lands_lie = commit("correction: lying actual-token")
    checkout(freeze)
    put(ST_CORR_PATH, _st_correction(rec_blob, rec_sha, base))
    lands_rev = commit("correction: wrong measured revision (base)")
    checkout(freeze)
    put(ST_RECEIPT, _st_receipt(ST_ACT))
    put(ST_CORR_PATH, _st_correction(rec_blob, rec_sha, measured))
    lands_recpt = commit("receipt edited in place plus correction")
    checkout(freeze_tamper)
    put(ST_CORR_PATH, _st_correction(rec_blob, rec_sha, measured, **{"actual-token": ST_OLD}))
    lands_tamper = commit("correction bound to tampered constants")
    checkout(base)
    put(ST_CORR_PATH, _st_correction(rec_blob, rec_sha, measured))
    side = commit("side branch off base carrying a correction")
    checkout(base)
    return (base, measured, freeze, freeze_tamper, lands_clean, lands_nocorr, lands_lie, lands_rev,
            lands_recpt, lands_tamper, side, top)


def selftest(work, keep):
    st = os.path.join(work, "selftest-ca79")
    if os.path.exists(st):
        raise Refusal("selftest scratch %s already exists; remove it first" % st)
    os.mkdir(st)
    fix = os.path.join(st, "fixture")
    os.mkdir(fix)
    env = _env()
    (base, _measured, freeze, freeze_tamper, lands_clean, lands_nocorr, lands_lie, lands_rev,
     lands_recpt, lands_tamper, side, top) = build_fixture(fix)

    me = os.path.abspath(__file__)
    scenarios = [
        ("clean", lands_clean, freeze, 0, set(), "PASS legs=7/7"),
        ("do-nothing", freeze, freeze, 1, {"CORRECTION", "UNRESOLVED", "NOSTUB"}, "FAIL legs=4/7"),
        ("no-correction", lands_nocorr, freeze, 1, {"CORRECTION", "UNRESOLVED", "NOSTUB"}, "FAIL legs=4/7"),
        ("lying-token", lands_lie, freeze, 1, {"CORRECTION", "UNRESOLVED"}, "FAIL legs=5/7"),
        ("wrong-revision", lands_rev, freeze, 1, {"CORRECTION", "UNRESOLVED"}, "FAIL legs=5/7"),
        ("changed-receipt", lands_recpt, freeze, 1, {"RECEIPT", "SEPARABLE"}, "FAIL legs=5/7"),
        ("frozen-tamper", lands_tamper, freeze_tamper, 1, {"DERIVE", "UNRESOLVED"}, "FAIL legs=5/7"),
        ("refuse-lands-is-base", base, freeze, 2, None, "refused: lands equals the frozen base"),
        ("refuse-off-chain", side, freeze, 2, None, "refused: freeze"),
        ("refuse-freeze-unreadable", lands_clean, base, 2, None, "refused: frozen"),
        ("refuse-nonhex", "HEAD", freeze, 2, None, "refused: lands is not a 40-hex"),
    ]
    log, rows = [], []
    for name, lands, frz, want_exit, want_fail, want_text in scenarios:
        p = subprocess.run([sys.executable, "-B", me, "--root", fix, "--lands", lands, "--freeze", frz,
                            "--work", st], capture_output=True, env=env, timeout=600)
        text = p.stdout.decode("utf-8", "replace")
        fails = {ln.split()[2] for ln in text.splitlines() if ln.startswith("LEG FAIL ")}
        verdict = [ln for ln in text.splitlines() if ln.startswith(ROUND_TAG + ":")]
        verdict = verdict[-1] if verdict else (p.stderr.decode("utf-8", "replace").strip() or "<no verdict>")
        ok = p.returncode == want_exit and want_text in verdict
        if want_fail is not None:
            ok = ok and fails == want_fail
        rows.append((name, ok))
        log.append("selftest: %s -> exit=%d want=%d failing=%s verdict=%s => %s"
                   % (name, p.returncode, want_exit, sorted(fails), verdict, "OK" if ok else "MISMATCH"))
        log.append(text.rstrip("\n"))

    _fixture_git(fix, "checkout", "-q", "--detach", base)
    p = subprocess.run([sys.executable, "-B", me, "--root", fix, "--lands", lands_clean, "--freeze", freeze,
                        "--work", st], capture_output=True, env=env, timeout=600)
    text = p.stdout.decode("utf-8", "replace")
    verdict = [ln for ln in text.splitlines() if ln.startswith(ROUND_TAG + ":")][-1:]
    ok = p.returncode == 0 and verdict == [ROUND_TAG + ": PASS legs=7/7"]
    rows.append(("clean-after-worktree-moved", ok))
    log.append("selftest: clean-after-worktree-moved (worktree at base) -> exit=%d verdict=%s => %s"
               % (p.returncode, verdict[0] if verdict else "<none>", "OK" if ok else "MISMATCH"))

    passed = sum(1 for _, ok in rows if ok)
    with open(os.path.abspath(__file__), "rb") as fh:
        self_sha = hashlib.sha256(fh.read()).hexdigest()
    head = ["# counter sha256 (self): %s" % self_sha, "# fixture repo verified toplevel: %s" % top,
            "# scratch: %s" % st]
    summary = "SELFTEST: %d/%d" % (passed, len(rows))
    out = "\n".join(log + head + [summary]) + "\n"
    sys.stdout.write(out)
    with open(os.path.join(work, "selftest-ca79.txt"), "w", encoding="utf-8") as fh:
        fh.write(out)
    if not keep:
        shutil.rmtree(st)
    return 0 if passed == len(rows) else 1


def main(argv=None):
    ap = argparse.ArgumentParser(description="Round-79 Ca census-correction counter (draft).")
    ap.add_argument("--root")
    ap.add_argument("--lands")
    ap.add_argument("--freeze")
    ap.add_argument("--work")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--keep", action="store_true")
    ap.add_argument("--derive", action="store_true")
    ap.add_argument("--at")
    ap.add_argument("--receipt-path")
    ap.add_argument("--registry-path")
    a = ap.parse_args(argv)
    try:
        if a.derive:
            if not a.root:
                raise Refusal("--derive needs --root")
            return derive_mode(a.root, a.at, a.receipt_path, a.registry_path)
        if not a.work or not os.path.isdir(a.work):
            raise Refusal("--work must name an existing scratch directory (explicit; no fallback)")
        if a.selftest:
            return selftest(a.work, a.keep)
        if not (a.root and a.lands and a.freeze):
            raise Refusal("grading needs --root, --lands and --freeze")
        return grade(a.root, a.lands, a.freeze, a.work)
    except Refusal as e:
        print("%s: FAIL legs=0/%d (refused: %s)" % (ROUND_TAG, len(LEG_TABLE), e))
        return 2
    except GitFail as e:
        print("%s: FAIL legs=0/%d (refused: git: %s)" % (ROUND_TAG, len(LEG_TABLE), e))
        return 2


if __name__ == "__main__":
    sys.exit(main())
