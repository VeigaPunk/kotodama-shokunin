#!/usr/bin/env python3
"""Round-77 freeze-manifest gate: the freeze commit carries exactly this set.

`manifest.json` (this directory) is the list of files the round-77 freeze
commit must carry, each pinned by the sha256 of its committed blob, plus the
LEGCOUNT rule that binds the frozen `legs[]` lists to the counters' own leg
tables.

Two modes:

  (build)   manifest-check.py --root <lane>
            The counters and claims are not installed yet, so absent files and
            unpinned digests are reported as PENDING, never as a pass.  Exit 3.

  (freeze)  manifest-check.py --root <lane> --freeze <freeze-commit>
            Authoritative: every file is read as the committed blob
            `git show <freeze>:<path>`, its sha256 must equal the pinned digest,
            and both counts' LEGCOUNT must be green.  Exit 0 only when all of
            that holds; any shortfall is exit 1.

  --record  pins the digests of the files that exist in the worktree, so the L1
            fills the `<sha256-at-freeze>` placeholders from the bytes about to
            be committed.  Record, then commit, then re-run with --freeze: the
            worktree digest and the blob digest must agree (a mismatch means
            the commit did not carry the recorded bytes).

Digest rule: sha256 over the file's committed blob content
(`git show <rev>:<path> | sha256sum`), not over the worktree file and not over
a re-serialization.  Line endings are whatever the blob holds.

usage:
  manifest-check.py [--root DIR] [--manifest P] [--freeze REV] [--record]
                    [--no-legs] [--json]

exit: 0 PASS, 1 FAIL (freeze blocker), 2 usage/IO error, 3 PENDING (build).

Read-only apart from --record, which rewrites this directory's manifest.json
and touches nothing else.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys

PLACEHOLDER = "<sha256-at-freeze>"
HERE = os.path.dirname(os.path.abspath(__file__))
LEGCOUNT = os.path.join(HERE, "legcount.py")


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def repo_root(start: str) -> str:
    proc = subprocess.run(["git", "-C", start, "rev-parse", "--show-toplevel"],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        raise SystemExit("ERROR: %s is not inside a git worktree: %s"
                         % (start, proc.stderr.decode("utf-8", "replace").strip()))
    return proc.stdout.decode().strip()


def blob_at(root: str, rev: str, rel: str):
    """(exists, bytes|None) of `rel` in commit `rev`."""
    proc = subprocess.run(["git", "-C", root, "show", "%s:%s" % (rev, rel)],
                          stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    if proc.returncode != 0:
        return False, None
    return True, proc.stdout


def safe_rel(rel) -> str | None:
    """Normalized repo-relative path, or None when it could escape the lane."""
    if not isinstance(rel, str) or not rel or rel.strip() != rel:
        return None
    if rel.startswith("/") or rel.startswith("~") or "\\" in rel:
        return None
    parts = rel.split("/")
    if any(p in ("", ".", "..") for p in parts):
        return None
    return rel


def load_manifest(path: str):
    with open(path, "rb") as fh:
        doc = json.loads(fh.read().decode("utf-8"))
    problems = []
    if doc.get("round") != 77:
        problems.append("manifest round is %r, not 77" % doc.get("round"))
    files = doc.get("files")
    if not isinstance(files, list) or not files:
        problems.append("manifest has no non-empty files[] list")
        files = []
    seen = {}
    for index, item in enumerate(files):
        if not isinstance(item, dict):
            problems.append("files[%d] is not an object" % index)
            continue
        rel = safe_rel(item.get("path"))
        if rel is None:
            problems.append("files[%d] path %r is not a safe repo-relative path"
                            % (index, item.get("path")))
            continue
        item["path"] = rel
        if rel in seen:
            problems.append("files[%d] repeats path %s (also files[%d])"
                            % (index, rel, seen[rel]))
        seen[rel] = index
        digest = item.get("sha256")
        if not isinstance(digest, str) or not digest:
            problems.append("files[%d] %s has no sha256 field" % (index, rel))
        elif digest != PLACEHOLDER and not (len(digest) == 64
                                            and all(c in "0123456789abcdef" for c in digest)):
            problems.append("files[%d] %s sha256 %r is neither the placeholder nor "
                            "64 lowercase hex" % (index, rel, digest))
    return doc, files, problems


def check_legs(doc, root: str, rev: str | None, enabled: bool):
    """[(claim, status, detail)] for each legcount entry in the manifest."""
    out = []
    if not enabled:
        return out
    entries = (doc.get("legcount") or {}).get("checks") or []
    if not entries:
        out.append(("-", "FAIL", "manifest declares no legcount checks"))
        return out
    for entry in entries:
        claim = entry.get("claim", "?")
        cmd = [sys.executable, "-B", LEGCOUNT, "--claim", claim, "--root", root]
        if entry.get("claims"):
            cmd += ["--claims", entry["claims"]]
        if entry.get("counter"):
            cmd += ["--counter", entry["counter"]]
        if entry.get("symbol"):
            cmd += ["--symbol", entry["symbol"]]
        if rev:
            cmd += ["--rev", rev]
        proc = subprocess.run(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        text = (proc.stdout + proc.stderr).decode("utf-8", "replace").strip()
        status = {0: "PASS", 1: "FAIL", 3: "PENDING"}.get(proc.returncode, "ERROR")
        out.append((claim, status, text))
    return out


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(add_help=True)
    ap.add_argument("--root", default=None)
    ap.add_argument("--manifest", default=os.path.join(HERE, "manifest.json"))
    ap.add_argument("--freeze", default=None)
    ap.add_argument("--record", action="store_true")
    ap.add_argument("--no-legs", action="store_true")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args(argv)

    if not os.path.isfile(args.manifest):
        print("ERROR: no manifest at %s" % args.manifest, file=sys.stderr)
        return 2
    try:
        doc, files, problems = load_manifest(args.manifest)
    except (OSError, ValueError) as exc:
        print("ERROR: cannot read %s: %s" % (args.manifest, exc), file=sys.stderr)
        return 2
    root = repo_root(args.root or HERE)

    if args.freeze:
        proc = subprocess.run(["git", "-C", root, "cat-file", "-e",
                               "%s^{commit}" % args.freeze],
                              stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        if proc.returncode != 0:
            print("ERROR: --freeze %s is not a commit in %s" % (args.freeze, root),
                  file=sys.stderr)
            return 2

    rows, ok_count, pinned = [], 0, 0
    record_changed = False
    for item in files:
        rel, want = item["path"], item.get("sha256")
        if args.freeze:
            exists, data = blob_at(root, args.freeze, rel)
            if not exists:
                rows.append((rel, "MISSING", "absent at %s" % args.freeze, None))
                continue
            actual = sha256_bytes(data)
        else:
            path = os.path.join(root, rel)
            if not os.path.isfile(path):
                rows.append((rel, "MISSING", "absent in the worktree", None))
                continue
            if os.path.realpath(path) != os.path.realpath(os.path.join(root, rel)):
                rows.append((rel, "ESCAPES", "resolves outside the lane", None))
                continue
            with open(path, "rb") as fh:
                data = fh.read()
            actual = sha256_bytes(data)

        if args.record and not args.freeze:
            if want != actual:
                item["sha256"] = actual
                record_changed = True
            rows.append((rel, "RECORD", actual, actual))
            pinned += 1
            ok_count += 1
            continue

        if want == PLACEHOLDER:
            rows.append((rel, "UNPINNED", "placeholder %s" % PLACEHOLDER, actual))
            if args.freeze:
                problems.append("%s is still unpinned at the freeze" % rel)
            continue
        pinned += 1
        if actual == want:
            rows.append((rel, "ok", actual, actual))
            ok_count += 1
        else:
            rows.append((rel, "MISMATCH", "pinned %s actual %s" % (want, actual), actual))
            problems.append("%s: pinned %s != actual %s" % (rel, want, actual))

    if args.record and record_changed:
        with open(args.manifest, "w", encoding="utf-8") as fh:
            json.dump(doc, fh, indent=1, ensure_ascii=False)
            fh.write("\n")

    legs = check_legs(doc, root, args.freeze, not args.no_legs)
    leg_fail = [c for c, s, _ in legs if s in ("FAIL", "ERROR")]
    leg_pending = [c for c, s, _ in legs if s == "PENDING"]

    if args.json:
        print(json.dumps({
            "manifest": args.manifest, "root": root, "freeze": args.freeze,
            "files": [{"path": p, "status": s, "detail": d, "sha256": a}
                      for p, s, d, a in rows],
            "legs": [{"claim": c, "status": s, "detail": d} for c, s, d in legs],
            "problems": problems,
        }, indent=1))
    else:
        for rel, status, detail, actual in rows:
            print("MANIFEST-FILE %-9s %s %s" % (status, rel, detail))
        for claim, status, text in legs:
            if status == "PASS":
                print("MANIFEST-LEGCOUNT %s PASS" % claim)
            else:
                print("MANIFEST-LEGCOUNT %s %s" % (claim, status))
                for line in text.splitlines():
                    print("  | %s" % line)
        for problem in problems:
            print("MANIFEST-PROBLEM %s" % problem)

    missing = [p for p, s, _, _ in rows if s in ("MISSING", "ESCAPES")]
    unpinned = [p for p, s, _, _ in rows if s == "UNPINNED"]
    mismatched = [p for p, s, _, _ in rows if s == "MISMATCH"]

    if mismatched or leg_fail or (args.freeze and (missing or unpinned)) or problems:
        verdict, code = "FAIL", 1
    elif missing or unpinned or leg_pending:
        verdict, code = "PENDING", 3
    else:
        verdict, code = "PASS", 0

    if not args.json:
        print("MANIFEST r77: %s files=%d/%d pinned=%d missing=%d unpinned=%d "
              "mismatched=%d legs=%d/%d"
              % (verdict, ok_count, len(files), pinned, len(missing), len(unpinned),
                 len(mismatched),
                 sum(1 for _, s, _ in legs if s == "PASS"), len(legs)))
        if verdict == "PENDING":
            print("MANIFEST r77: pending items are the freeze-installed inputs; "
                  "re-run with --freeze <commit> after the freeze commit")
        elif verdict == "FAIL":
            print("MANIFEST r77: freeze blocker — fix the named files/legs and re-run")
    return code


if __name__ == "__main__":
    sys.exit(main())
