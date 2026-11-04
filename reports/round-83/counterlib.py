#!/usr/bin/env python3
r"""Shared grading helpers for the kotodama round-83 counters.

Frozen with the claims (reports/round-83/claims.json). Every counter reads the
frozen config with `git show <freeze>:reports/round-83/claims.json` and grades
blobs materialised from `--root:<rev>` into `<work>/tree`, never worktree
bytes. No helper writes inside the lane repo: fixtures live under --work.
"""
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

HEX40 = re.compile(r"^[0-9a-f]{40}$")


class Refuse(Exception):
    pass


def _p(root, *a):
    return ["git", "-C", root] + list(a)


def run(root, *a):
    return subprocess.run(_p(root, *a), capture_output=True)


def gout(root, *a):
    r = run(root, *a)
    if r.returncode != 0:
        raise RuntimeError("git %s: %s" % (a[0], r.stderr.decode("utf-8", "replace").strip()[:300]))
    return r.stdout.decode("utf-8", "replace")


def show(root, rev, path):
    r = run(root, "show", "%s:%s" % (rev, path))
    return r.stdout if r.returncode == 0 else None


def blob_size(root, rev, path):
    r = run(root, "cat-file", "-s", "%s:%s" % (rev, path))
    try:
        return int(r.stdout.strip())
    except ValueError:
        return -1


def tree_paths(root, rev, prefix):
    r = run(root, "ls-tree", "-r", "--name-only", rev, "--", prefix)
    if r.returncode != 0:
        return []
    return [l for l in r.stdout.decode("utf-8", "replace").splitlines() if l.strip()]


def rev_ok(s):
    return bool(HEX40.match(s or ""))


def sha256(b):
    return hashlib.sha256(b).hexdigest()


def is_ancestor(root, older, newer):
    return run(root, "merge-base", "--is-ancestor", older, newer).returncode == 0


def changed_paths(root, a, b):
    r = run(root, "diff", "--name-only", "%s..%s" % (a, b))
    if r.returncode != 0:
        raise RuntimeError("git diff failed")
    return [l for l in r.stdout.decode("utf-8", "replace").splitlines() if l.strip()]


def materialize(root, rev, sink, paths):
    """Write blobs at rev under sink, preserving repo-relative paths. Returns count."""
    n = 0
    for p in paths:
        b = show(root, rev, p)
        if b is None:
            continue
        d = os.path.join(sink, p)
        os.makedirs(os.path.dirname(d), exist_ok=True)
        with open(d, "wb") as f:
            f.write(b)
        n += 1
    return n


def run_py(path, args, cwd=None, timeout=600):
    env = dict(os.environ)
    env.pop("PYTHONPATH", None)
    env["PYTHONDONTWRITEBYTECODE"] = "1"
    r = subprocess.run([sys.executable, "-B", path] + list(args), capture_output=True, cwd=cwd, env=env, timeout=timeout)
    return r.returncode, r.stdout.decode("utf-8", "replace"), r.stderr.decode("utf-8", "replace")


def one_line(stdout, regex):
    """Return the single line matching regex, or None when absent or ambiguous."""
    hits = [l for l in stdout.splitlines() if re.match(regex, l)]
    return hits[0] if len(hits) == 1 else None


def clone_at(root, rev, dest):
    """A scratch clone of root, checked out at rev. Fixture identity stays local to dest."""
    if os.path.exists(dest):
        shutil.rmtree(dest)
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    r = subprocess.run(["git", "clone", "--shared", "--no-hardlinks", "-q", root, dest], capture_output=True)
    if r.returncode != 0:
        raise RuntimeError("clone failed: %s" % r.stderr.decode("utf-8", "replace")[:300])
    subprocess.run(["git", "-C", dest, "config", "user.email", "fixture@round83.invalid"], check=True)
    subprocess.run(["git", "-C", dest, "config", "user.name", "round83-fixture"], check=True)
    subprocess.run(["git", "-C", dest, "checkout", "-q", rev], check=True)
    return dest


def fixture_commit(dest, relpath, content, msg):
    p = os.path.join(dest, relpath)
    os.makedirs(os.path.dirname(p), exist_ok=True)
    with open(p, "wb") as f:
        f.write(content if isinstance(content, bytes) else content.encode("utf-8"))
    subprocess.run(["git", "-C", dest, "add", "--", relpath], check=True)
    subprocess.run(["git", "-C", dest, "commit", "-q", "-m", msg], check=True)
    return gout(dest, "rev-parse", "HEAD").strip()


class Grader:
    def __init__(self, label, legs):
        self.label = label
        self.legs = legs
        self.rows = []

    def grade(self, name, fn):
        if name not in self.legs:
            raise Refuse("LEGCOUNT: %s is not in the frozen leg table" % name)
        try:
            ok, detail = fn()
        except Exception as e:  # a leg that cannot run is a failed leg, never a pass
            ok, detail = False, "error: %s" % str(e)[:300]
        self.rows.append((name, ok))
        print("LEG %-11s %s %s" % (name, "PASS" if ok else "FAIL", detail))
        return ok

    def finish(self):
        seen = [r[0] for r in self.rows]
        missing = [n for n in self.legs if n not in seen]
        if missing:
            print("LEGCOUNT missing: %s" % ",".join(missing))
        passed = sum(1 for r in self.rows if r[1])
        ok = not missing and passed == len(self.legs)
        print("%s: %s legs=%d/%d" % (self.label, "PASS" if ok else "FAIL", passed, len(self.legs)))
        return 0 if ok else 1


def refuse(label, legs, reason):
    print("%s: FAIL legs=0/%d (refused: %s)" % (label, len(legs), reason))
    return 2


def load_config(root, freeze, claims_path):
    """Frozen config is read from --freeze only; the lands bytes are a graded leg."""
    bf = show(root, freeze, claims_path)
    if bf is None:
        raise Refuse("frozen claims.json unreadable at freeze")
    try:
        cfg = json.loads(bf.decode("utf-8"))
    except Exception as e:
        raise Refuse("frozen claims.json not JSON: %s" % e)
    return cfg


def claim_config(cfg, cid):
    for c in cfg.get("claims", []):
        if c.get("id") == cid:
            blocks = [k for k in c if k.endswith("83") and isinstance(c[k], dict)]
            if len(blocks) != 1:
                raise Refuse("frozen config for claim %s carries %d constants blocks" % (cid, len(blocks)))
            return c["counter"], c[blocks[0]]
    raise Refuse("frozen config has no claim %s" % cid)
