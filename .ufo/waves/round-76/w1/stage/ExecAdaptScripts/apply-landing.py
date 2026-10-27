#!/usr/bin/env python3
r"""Round-76 draft-landing applier — skeleton (data-driven, two-phase).

The round-75 applier (.ufo/waves/round-75/apply-landing.py, read and copied,
never edited) hard-coded the round-75 stage directory, the round-75 claim list
and the round-75 edit shapes in the script body: `if which == "ca": ...`.
That cannot absorb a round whose drafts are written after the freeze.  This
round-76 skeleton keeps the *effects* (SOURCES rows block, entry files, README
rows + heading + footer, SKILL/QUALITY/SCORECARD edits and evidence copies)
and moves every path, anchor and payload out of the code and into a manifest
that the L1 / wave 2 fill in:

    python3 -B apply-landing.py --root <clone> --claim ca --drafts <dir>
    python3 -B apply-landing.py --root <clone> --claim c  --drafts <dir> --check

Two phases, so a bad draft can never half-land:

  1. plan     every op is resolved against an in-memory copy of the target
              tree: sources must exist and be non-empty, anchors must match the
              declared number of times, a `replace` must hit its declared
              occurrence count, destinations must not already exist unless the
              op says `overwrite`.  Every failure is a `REFUSED:` line and
              exit 3, with nothing written.
  2. apply    only when every op of the claim planned cleanly are the dirty
              files written, parents created.

Guards
  * --root must be a git worktree toplevel: `git -C <root> rev-parse
    --show-toplevel` must name <root> itself.
  * --root may not be the live lane unless --allow-lane is given, so a
    rehearsal cannot touch the lane by accident.
  * every draft/target path is relative and may not escape its directory.

Manifest schema (JSON; default `<drafts>/manifest.json`, override --manifest):

  {
    "round": 76,
    "claims": {
      "ca": {"ops": [ <op>, ... ]},
      "c":  {"ops": [ <op>, ... ]}
    }
  }

Ops (all paths repo/draft-relative, "/"-separated):

  copy        {"op":"copy","from":"<drafts path>","to":"<root path>"}
              `to` defaults to `from`.  Refuses an empty source and an
              existing destination unless `"overwrite": true`.

  copy_glob   {"op":"copy_glob","from":"reports/round-76/evidence/*.txt",
               "to":"reports/round-76/evidence"}
              copies each match's basename into the `to` directory.

  append      {"op":"append","to":"corpus/QUALITY.md",
               "from":"corpus/QUALITY.md.append",
               "unless_present":"optional guard string"}
              appends the payload after ensuring the target ends in "\n".
              `unless_present` makes the op refuse when the landing is already
              applied (no double append).

  insert_block {"op":"insert_block","to":"corpus/SOURCES.md",
                "from":"corpus/SOURCES.rows",
                "anchor":"^ {0,3}\\|\\s*S893\\s*\\|",
                "where":"after"|"before",
                "match":"exactly-one"|"first"|"last"}
              inserts the payload lines at the anchor.  `match` defaults to
              "exactly-one"; use "last" for a registry whose row ids are not
              unique across scopes.  The anchor is a Python `re` pattern, not a
              shell/POSIX one: use \\s and \\| rather than [[:space:]].

  replace     {"op":"replace","to":"corpus/README.md",
               "old":"## culture-material/ (40)",
               "new":"## culture-material/ (43)","count":1}
              exact-string replacement with an occurrence assertion (`count`
              defaults to 1).  Multi-line `old`/`new` are allowed.  The
              round-75 LINE-REPLACE record shape is also accepted:
              {"op":"replace","to":..., "from":"<drafts path>"} where the file
              is `old lines`, a line `==>`, `new lines`, nothing else.

  assert      {"op":"assert","to":"SKILL.md","contains":"..."} or
              {"op":"assert","to":"corpus/README.md","absent":"..."}
              a precondition/after-state check with no write.

Nothing here is trusted to be idempotent: re-running a claim over an already
landed tree refuses (copy destination exists, append guard present, replace
count 0), which is the required shape for a rehearsal.

Scratch: this tool needs none (no temporary files, no /tmp).  Exit codes:
0 applied (or --check planned cleanly), 2 usage, 3 refused.
"""

import argparse
import fnmatch
import json
import os
import re
import subprocess
import sys

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
ROUND = 76
CLAIMS = ("ca", "c")
EXIT_USAGE = 2
EXIT_REFUSED = 3


class Refused(Exception):
    pass


def safe_rel(rel, what):
    """A relative path that cannot escape its base directory."""
    if not isinstance(rel, str) or not rel:
        raise Refused("%s must be a non-empty string, got %r" % (what, rel))
    if os.path.isabs(rel):
        raise Refused("%s must be relative, got %r" % (what, rel))
    norm = os.path.normpath(rel)
    if norm in (".", "") or norm.startswith(".." + os.sep) or norm == "..":
        raise Refused("%s escapes its base directory: %r" % (what, rel))
    return norm


class Plan(object):
    """An in-memory view of the target tree plus the ops already planned."""

    def __init__(self, root, drafts):
        self.root = root
        self.drafts = drafts
        self.vfs = {}          # rel -> text (loaded targets and pending writes)
        self.dirty = set()     # rels to write on apply
        self.planned = []      # (op name, target rel) for --check output

    # -- target side -----------------------------------------------------
    def target_path(self, rel):
        return os.path.join(self.root, rel)

    def read_target(self, rel):
        if rel in self.vfs:
            return self.vfs[rel]
        path = self.target_path(rel)
        if not os.path.isfile(path):
            raise Refused("target does not exist: %s" % rel)
        with open(path, encoding="utf-8", newline="") as fh:
            text = fh.read()
        self.vfs[rel] = text
        return text

    def exists_target(self, rel):
        return rel in self.vfs or os.path.isfile(self.target_path(rel))

    def set_target(self, rel, text):
        self.vfs[rel] = text
        self.dirty.add(rel)

    # -- draft side ------------------------------------------------------
    def draft_path(self, rel):
        return os.path.join(self.drafts, rel)

    def read_draft(self, rel):
        path = self.draft_path(rel)
        if not os.path.isfile(path):
            raise Refused("draft missing: %s (looked at %s)" % (rel, path))
        with open(path, encoding="utf-8", newline="") as fh:
            text = fh.read()
        if not text.strip():
            raise Refused("draft is empty: %s" % rel)
        return text


# --------------------------------------------------------------------------
# ops
# --------------------------------------------------------------------------

def op_copy(plan, op):
    src = safe_rel(op.get("from"), "copy.from")
    dst = safe_rel(op.get("to") or src, "copy.to")
    if plan.exists_target(dst) and not op.get("overwrite"):
        raise Refused("copy destination exists (already landed?): %s" % dst)
    plan.set_target(dst, plan.read_draft(src))
    plan.planned.append(("copy", dst))


def op_copy_glob(plan, op):
    pattern = safe_rel(op.get("from"), "copy_glob.from")
    dst_dir = safe_rel(op.get("to"), "copy_glob.to")
    matches = _glob_drafts(plan, pattern)
    if not matches:
        raise Refused("copy_glob matched no draft file: %s" % pattern)
    for src in matches:
        dst = safe_rel(os.path.join(dst_dir, os.path.basename(src)), "copy_glob.to")
        if plan.exists_target(dst) and not op.get("overwrite"):
            raise Refused("copy_glob destination exists (already landed?): %s" % dst)
        plan.set_target(dst, plan.read_draft(src))
        plan.planned.append(("copy_glob", dst))


def _glob_drafts(plan, pattern):
    """Sorted drafts-relative matches of a shell-style glob (recursive on **)."""
    base = plan.drafts
    out = []
    for dirpath, _dirnames, filenames in os.walk(base):
        for name in filenames:
            rel = os.path.relpath(os.path.join(dirpath, name), base)
            rel = rel.replace(os.sep, "/")
            if fnmatch.fnmatch(rel, pattern):
                out.append(rel)
    return sorted(out)


def op_append(plan, op):
    dst = safe_rel(op.get("to"), "append.to")
    src = safe_rel(op.get("from"), "append.from")
    payload = plan.read_draft(src)
    current = plan.read_target(dst)
    guard = op.get("unless_present")
    if guard and guard in current:
        raise Refused("append guard already present in %s: %r" % (dst, guard))
    if current and not current.endswith("\n"):
        current += "\n"
    if not payload.endswith("\n"):
        payload += "\n"
    plan.set_target(dst, current + payload)
    plan.planned.append(("append", dst))


def op_insert_block(plan, op):
    dst = safe_rel(op.get("to"), "insert_block.to")
    src = safe_rel(op.get("from"), "insert_block.from")
    block = plan.read_draft(src).rstrip("\n").split("\n")
    where = op.get("where", "after")
    if where not in ("after", "before"):
        raise Refused("insert_block.where must be after|before, got %r" % where)
    match = op.get("match", "exactly-one")
    if match not in ("exactly-one", "first", "last"):
        raise Refused("insert_block.match must be exactly-one|first|last, got %r" % match)
    try:
        anchor = re.compile(op.get("anchor", ""))
    except re.error as exc:
        raise Refused("insert_block.anchor is not a regex: %s" % exc)
    lines = plan.read_target(dst).split("\n")
    hits = [i for i, line in enumerate(lines) if anchor.search(line)]
    if not hits:
        raise Refused("insert_block anchor found no line in %s: %r" % (dst, op.get("anchor")))
    if match == "exactly-one" and len(hits) != 1:
        raise Refused("insert_block anchor matched %d lines in %s (want 1): %s"
                      % (len(hits), dst, hits))
    idx = hits[-1] if match == "last" else hits[0]
    at = idx + 1 if where == "after" else idx
    lines[at:at] = block
    plan.set_target(dst, "\n".join(lines))
    plan.planned.append(("insert_block", dst))


def op_replace(plan, op):
    dst = safe_rel(op.get("to"), "replace.to")
    if "old" in op or "new" in op:
        old = op.get("old")
        new = op.get("new")
        if not isinstance(old, str) or not isinstance(new, str):
            raise Refused("replace needs both \"old\" and \"new\" as strings for %s" % dst)
    elif "from" in op:
        payload = plan.read_draft(safe_rel(op["from"], "replace.from")).rstrip("\n")
        if "\n==>\n" not in payload:
            raise Refused("replace record %s has no lone '==>' separator line" % op["from"])
        old, new = payload.split("\n==>\n", 1)
    else:
        raise Refused("replace needs old/new or from for %s" % dst)
    try:
        count = int(op.get("count", 1))
    except (TypeError, ValueError):
        raise Refused("replace.count must be an integer for %s" % dst)
    current = plan.read_target(dst)
    seen = current.count(old)
    if seen != count:
        raise Refused("replace in %s: the old text occurs %d times, manifest expects %d: %r"
                      % (dst, seen, count, old[:80]))
    plan.set_target(dst, current.replace(old, new))
    plan.planned.append(("replace", dst))


def op_assert(plan, op):
    dst = safe_rel(op.get("to"), "assert.to")
    current = plan.read_target(dst)
    if "contains" in op:
        if op["contains"] not in current:
            raise Refused("assert failed: %s does not contain %r" % (dst, op["contains"]))
    if "absent" in op:
        if op["absent"] in current:
            raise Refused("assert failed: %s contains %r" % (dst, op["absent"]))
    plan.planned.append(("assert", dst))


OPS = {
    "copy": op_copy,
    "copy_glob": op_copy_glob,
    "append": op_append,
    "insert_block": op_insert_block,
    "replace": op_replace,
    "assert": op_assert,
}


# --------------------------------------------------------------------------
# driver
# --------------------------------------------------------------------------

def git_toplevel(path):
    try:
        res = subprocess.run(
            ["git", "-C", path, "rev-parse", "--show-toplevel"],
            stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
            env=dict(os.environ, GIT_OPTIONAL_LOCKS="0"),
        )
    except OSError:
        return None
    if res.returncode != 0:
        return None
    return res.stdout.decode("utf-8", "replace").strip()


def check_root(root, allow_lane):
    real = os.path.realpath(root)
    if not os.path.isdir(real):
        raise Refused("--root is not a directory: %s" % root)
    if real == os.path.realpath(LANE) and not allow_lane:
        raise Refused("--root is the live lane %s; pass --allow-lane for the real "
                      "landing (a rehearsal must target a clone)" % LANE)
    top = git_toplevel(real)
    if top is None:
        raise Refused("--root is not a git worktree: %s" % root)
    if os.path.realpath(top) != real:
        raise Refused("--root is not the worktree toplevel: %s (git says %s)" % (root, top))
    return real, top


def load_manifest(drafts, manifest):
    path = manifest or os.path.join(drafts, "manifest.json")
    if not os.path.isfile(path):
        raise Refused("manifest not found: %s (the draft set is incomplete)" % path)
    try:
        with open(path, encoding="utf-8") as fh:
            doc = json.load(fh)
    except (OSError, ValueError) as exc:
        raise Refused("manifest unreadable: %s: %s" % (path, exc))
    if not isinstance(doc, dict):
        raise Refused("manifest is not a JSON object: %s" % path)
    if "round" in doc and doc["round"] != ROUND:
        raise Refused("manifest is for round %r, this applier is round %d"
                      % (doc["round"], ROUND))
    claims = doc.get("claims")
    if not isinstance(claims, dict):
        raise Refused("manifest has no \"claims\" object: %s" % path)
    for name in claims:
        if name not in CLAIMS:
            raise Refused("manifest names an unknown claim %r (known: %s)"
                          % (name, ", ".join(CLAIMS)))
    return path, doc


def ops_for(doc, claim, path):
    entry = doc["claims"].get(claim)
    if not isinstance(entry, dict):
        raise Refused("manifest has no claim %r (drafts incomplete): %s" % (claim, path))
    ops = entry.get("ops")
    if not isinstance(ops, list) or not ops:
        raise Refused("claim %r has no ops (drafts incomplete): %s" % (claim, path))
    return ops


def apply_plan(plan):
    written = []
    for rel in sorted(plan.dirty):
        dst = plan.target_path(rel)
        parent = os.path.dirname(dst)
        if parent:
            os.makedirs(parent, exist_ok=True)
        with open(dst, "w", encoding="utf-8", newline="") as fh:
            fh.write(plan.vfs[rel])
        written.append(rel)
    return written


def main(argv=None):
    ap = argparse.ArgumentParser(
        prog="apply-landing.py",
        description="Apply a round-76 DRAFT landing (manifest-driven) to a worktree.",
    )
    ap.add_argument("--root", default=None, help="worktree the landing is applied to")
    ap.add_argument("--claim", default=None, choices=CLAIMS,
                    help="claim whose op list to apply")
    ap.add_argument("--drafts", default=None, help="directory holding the drafted lane files")
    ap.add_argument("--manifest", default=None,
                    help="manifest path (default <drafts>/manifest.json)")
    ap.add_argument("--check", action="store_true",
                    help="plan and validate only; write nothing")
    ap.add_argument("--allow-lane", action="store_true",
                    help="permit --root to be the live lane (the L1's real landing)")
    ap.add_argument("--print-example", action="store_true",
                    help="print the example manifest and exit")
    args = ap.parse_args(argv)

    if args.print_example:
        sys.stdout.write(EXAMPLE)
        return 0

    missing = [name for name in ("root", "claim", "drafts") if not getattr(args, name)]
    if missing:
        ap.error("missing required argument(s): %s"
                 % ", ".join("--" + name for name in missing))

    try:
        root, top = check_root(args.root, args.allow_lane)
        drafts = os.path.realpath(args.drafts)
        if not os.path.isdir(drafts):
            raise Refused("--drafts is not a directory: %s" % args.drafts)
        manifest_path, doc = load_manifest(drafts, args.manifest)
        ops = ops_for(doc, args.claim, manifest_path)
        plan = Plan(root, drafts)
        for number, op in enumerate(ops, 1):
            if not isinstance(op, dict) or op.get("op") not in OPS:
                raise Refused("claim %s op %d is not a known op: %r (known: %s)"
                              % (args.claim, number, op, ", ".join(sorted(OPS))))
            try:
                OPS[op["op"]](plan, op)
            except Refused as exc:
                raise Refused("claim %s op %d (%s): %s" % (args.claim, number, op["op"], exc))
        if not plan.planned:
            raise Refused("claim %s planned no op" % args.claim)
    except Refused as exc:
        print("REFUSED: %s" % exc, file=sys.stderr)
        return EXIT_REFUSED

    prefix = "PLAN" if args.check else "APPLIED"
    for name, target in plan.planned:
        print("%s %-12s %s" % (prefix, name, target))
    if args.check:
        print("PLAN claim=%s ops=%d would-write=%d root=%s (nothing written)"
              % (args.claim, len(plan.planned), len(plan.dirty), root))
        return 0
    written = apply_plan(plan)
    for rel in written:
        print("WROTE %s" % rel)
    print("APPLIED claim=%s ops=%d wrote=%d root=%s"
          % (args.claim, len(plan.planned), len(written), root))
    return 0


EXAMPLE = """{
  "round": 76,
  "claims": {
    "ca": {
      "ops": [
        {"op": "replace", "to": "SKILL.md",
         "old": "<base line 701 verbatim>", "new": "<corrected line>", "count": 1},
        {"op": "insert_block", "to": "SKILL.md", "from": "skill/skill.rows",
         "anchor": "^\\\\| accept-ca-75 \\\\|", "where": "after", "match": "exactly-one"},
        {"op": "append", "to": "corpus/QUALITY.md", "from": "corpus/QUALITY.md.append"},
        {"op": "append", "to": "SCORECARD.md", "from": "SCORECARD.md.append",
         "unless_present": "## Corrections — round 76"},
        {"op": "replace", "to": "corpus/README.md",
         "from": "corpus/README.md.ca-edits"},
        {"op": "append", "to": "corpus/lessons/round-75.md",
         "from": "corpus/lessons/round-75.corrections-76.md"}
      ]
    },
    "c": {
      "ops": [
        {"op": "copy", "from": "corpus/knowledge/culture-material/ENTRY-a.md",
         "to": "corpus/knowledge/culture-material/ENTRY-a.md"},
        {"op": "insert_block", "to": "corpus/SOURCES.md", "from": "corpus/SOURCES.rows",
         "anchor": "^ {0,3}\\\\|\\\\s*S893\\\\s*\\\\|", "where": "after", "match": "last"},
        {"op": "insert_block", "to": "corpus/README.md", "from": "corpus/README.md.c-rows",
         "anchor": "^## synthesis/ \\\\(", "where": "before", "match": "exactly-one"},
        {"op": "replace", "to": "corpus/README.md",
         "old": "## culture-material/ (40)", "new": "## culture-material/ (43)", "count": 1},
        {"op": "append", "to": "corpus/README.md", "from": "corpus/README.md.c-footer"},
        {"op": "copy", "from": "corpus/lessons/round-76.md"},
        {"op": "copy_glob", "from": "reports/round-76/evidence/*.txt",
         "to": "reports/round-76/evidence"}
      ]
    }
  }
}
"""


if __name__ == "__main__":
    sys.exit(main())
