#!/usr/bin/env python3
# MutPath (kotodama round-79 W1): run the COMMITTED round-74 H2 observe guard, loaded from a
# scratch copy of its base bytes (`git show 44f76d4:reports/round-74/accept-ca.py`), against
# adversarial observe_cmd argvs on the MutPath fixture repository. Records the guard's static
# verdict (observe_problem) and, where it accepts, the dynamic observation (run_observe).
# Argvs marked static_only are never executed (they would write a file or run a pager); their
# execution evidence is already in the mutpath-probe-raw receipts (F1, F2b, F2c).
#
# Usage: python3 -B probe_committed_h2.py <base-copy accept-ca.py> <fixture-clone> <work-dir> <receipt>
import importlib.util
import os
import subprocess
import sys

MOD, FIX, WORK, RECEIPT = sys.argv[1], os.path.realpath(sys.argv[2]), os.path.realpath(sys.argv[3]), sys.argv[4]

spec = importlib.util.spec_from_file_location("ca74_base", MOD)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)

top = subprocess.run(["git", "-C", FIX, "rev-parse", "--show-toplevel"], capture_output=True, text=True).stdout.strip()
if os.path.realpath(top) != FIX:
    sys.exit("refused: fixture toplevel %r != %r" % (top, FIX))
C1 = subprocess.run(["git", "-C", FIX, "rev-parse", "HEAD~1"], capture_output=True, text=True).stdout.strip()
C2 = subprocess.run(["git", "-C", FIX, "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()

# worktree-only file: present on disk in the clone, absent from C1's tree (fixture-only, untracked)
with open(os.path.join(FIX, "corpus/worktree-only.md"), "wb") as fh:
    fh.write(b"worktree S001\n")

# worktree symlink whose target lies OUTSIDE the clone (fixture-only, untracked)
OUTSIDE = os.path.join(WORK, "outside-secret.txt")
with open(OUTSIDE, "wb") as fh:
    fh.write(b"SECRET S777 outside the repository\n")
LINK = os.path.join(FIX, "corpus/link-ext")
if os.path.lexists(LINK):
    os.remove(LINK)
os.symlink(OUTSIDE, LINK)

SUBS = {"@C1@": C1, "@C2@": C2, "@FIX@": FIX, "@WORK@": WORK}


def sub(a):
    for k, v in SUBS.items():
        a = a.replace(k, v)
    return a


# id, argv, expect (REFUSE/ACCEPT/REVIEW), static_only, why
CASES = [
    ("K1", ["git", "show", "@C1@:corpus/SOURCES.md"], "ACCEPT", False, "committed blob, legitimate"),
    ("K2", ["git", "show", "@C1@:../SOURCES.md"], "REFUSE", False, "traversal out of repo via rev:path"),
    ("K3", ["git", "show", "@C1@:/etc/passwd"], "REFUSE", False, "absolute path via rev:path"),
    ("K4", ["git", "show", ":corpus/SOURCES.md"], "REFUSE", False, "EMPTY rev reads the mutable index"),
    ("K5", ["git", "show", "HEAD:corpus/SOURCES.md"], "REFUSE", False, "symbolic HEAD (by design allowed in REV_NAMES; mutable if clone moves)"),
    ("K6", ["git", "show", "main:corpus/SOURCES.md"], "REFUSE", False, "named branch as rev (mutable)"),
    ("K7", ["git", "show", "--output=@WORK@/k7-out.txt", "@C1@:corpus/SOURCES.md"], "REFUSE", True, "write escape via --output (static only)"),
    ("K8", ["git", "grep", "--open-files-in-pager=@WORK@/pager.sh", "-c", "S001", "--", "corpus/SOURCES.md"], "REFUSE", True, "pager exec escape, worktree form (static only; executed in F2b)"),
    ("K9", ["git", "grep", "-O@WORK@/pager.sh", "-c", "S001", "--", "corpus/SOURCES.md"], "REFUSE", True, "pager exec escape, -O short form (static only; executed in F2c)"),
    ("K10", ["git", "grep", "-c", "S001", "@C1@", "--", ":!corpus/SOURCES.md"], "REVIEW", False, "exclude magic: named set not an existence-checked path"),
    ("K11", ["git", "grep", "-c", "S001", "@C1@", "--", ":/etc/passwd"], "REFUSE", False, "top-magic path that does not exist -> rc 1 -> observed as zero"),
    ("K12", ["git", "grep", "-c", "S001", "@C1@", "--", "corpus/nothing/*.md"], "REFUSE", False, "glob matching nothing -> rc 1 -> observed as zero"),
    ("K13", ["git", "grep", "-c", "S001", "@C1@", "--", "corpus/worktree-only.md"], "REFUSE", False, "path exists in clone WORKTREE, absent at @C1@ -> false zero"),
    ("K14", ["git", "grep", "-c", "S001", "@C1@", "--", "corpus/nope.md"], "REFUSE", False, "path absent everywhere"),
    ("K15", ["git", "show", "@C1@:corpus/a:b.md"], "ACCEPT", False, "legitimate colon-in-filename at rev"),
    ("K16", ["git", "show", "@C1@:corpus/a:b.md:x"], "REFUSE", False, "second colon: path does not exist at rev"),
    ("K17", ["git", "show", ":corpus/a:b.md"], "REFUSE", False, "colon form with EMPTY rev (index)"),
    ("K18", ["git", "grep", "-c", "S001", "", "--", "corpus/SOURCES.md"], "REFUSE", False, "EMPTY rev operand"),
    ("K19", ["git", "grep", "-c", "S001", "@C1@", "HEAD", "--", "corpus/SOURCES.md"], "REFUSE", False, "two revision operands; regex reads one capture"),
    ("K20", ["git", "grep", "-c", "S001", "main", "--", "corpus/SOURCES.md"], "REFUSE", False, "named branch as grep revision (mutable)"),
    ("K21", ["cat", "corpus/SOURCES.md"], "REFUSE", False, "worktree read through OBSERVE_ALLOW cat (not committed bytes)"),
    ("K22", ["grep", "-c", "S001", "corpus/SOURCES.md"], "REFUSE", False, "worktree read through OBSERVE_ALLOW grep"),
    ("K23", ["git", "show", "@C1@\n:corpus/SOURCES.md"], "REFUSE", False, "newline inside argv element"),
    ("K24", ["git", "-C", "/etc", "show", "@C1@:corpus/SOURCES.md"], "REFUSE", False, "-C global option redirects repo"),
    ("K25", ["git", "--git-dir=/etc/x/.git", "show", "@C1@:corpus/SOURCES.md"], "REFUSE", False, "--git-dir global option"),
    ("K26", ["git", "cat-file", "-e", "@C1@:../../etc/passwd"], "REFUSE", False, "cat-file traversal via rev:path"),
    ("K27", ["git", "show", "@C1@:corpus/SOURCES.md/"], "REFUSE", False, "trailing slash on blob path"),
    ("K28", ["git", "show", "@C1@:corpus/link-abs"], "REVIEW", False, "symlink blob: committed bytes are link text, not target"),
    ("K29", ["git", "show", "@C1@:corpus/sub"], "REFUSE", False, "tree, not blob: git show exits 0 with a listing"),
    ("K30", ["git", "grep", "-c", "S001", "@C1@", "--", "corpus/*.md"], "REVIEW", False, "plain wildcard crosses directory separators"),
    ("K34", ["grep", "-c", "SECRET", "corpus/link-ext"], "REFUSE", False, "worktree symlink to a file OUTSIDE the repo: lexical containment passes, exists() follows the link"),
    ("K35", ["git", "grep", "-c", "S001", "@C1@", "--", ":../../etc/passwd"], "REFUSE", False, "pathspec magic-prefixed traversal (exempt from existence check by _pathspec_ok)"),
    ("K31", ["git", "-C/etc", "show", "@C1@:corpus/SOURCES.md"], "REFUSE", True, "attached -C form (static only; not in GIT_GLOBAL_OPTS exact match)"),
    ("K32", ["git", "-ccore.pager=@WORK@/pager.sh", "show", "@C1@:corpus/SOURCES.md"], "REFUSE", True, "attached -c config injection (static only)"),
    ("K33", ["git", "--exec-path=@WORK@", "show", "@C1@:corpus/SOURCES.md"], "REFUSE", True, "--exec-path= form (static only)"),
]

lines = []
lines.append("# MutPath round-79 W1: committed round-74 H2 observe guard probe (raw)")
lines.append("# guard module: %s" % MOD)
lines.append("# guard sha256: %s" % __import__("hashlib").sha256(open(MOD, "rb").read()).hexdigest())
lines.append("# source: git show 44f76d456c1b326a71ffdb381590af825cbf11be:reports/round-74/accept-ca.py (blob bb69fb04f5971a8d5c2d9da7b4a3f9afc65d9b12)")
lines.append("# fixture clone: %s (toplevel verified)" % FIX)
lines.append("# C1 (rev used in argvs) = %s ; C2 (HEAD, main) = %s" % (C1, C2))
lines.append("# verdict columns: static = observe_problem(argv, clone); dynamic = run_observe(clone, argv) when static accepts")
lines.append("")

summary = []
for cid, argv_t, expect, static_only, why in CASES:
    argv = [sub(a) for a in argv_t]
    problem = m.observe_problem(argv, FIX)
    static = "REFUSE" if problem else "ACCEPT"
    if problem is None and static_only:
        dyn = "NOT-EXECUTED (static_only)"
        final = "ACCEPT (static)"
    elif problem is None:
        value, note = m.run_observe(FIX, argv)
        dyn = "observed=%r note=%s" % (value, note)
        final = "ACCEPT"
    else:
        dyn = "-"
        final = "REFUSE"
    # verdict vs expectation: REVIEW cases are recorded, not graded
    if expect == "REVIEW":
        grade = "REVIEW"
    else:
        grade = "MATCH" if (final.startswith("REFUSE") == (expect == "REFUSE")) else "GAP"
    lines.append("== [%s] %s" % (cid, why))
    lines.append("argv: %r" % argv)
    lines.append("expect: %s   static: %s   dynamic: %s" % (expect, static, dyn))
    if problem:
        lines.append("refusal: %s" % problem)
    lines.append("grade: %s" % grade)
    lines.append("")
    summary.append((cid, expect, final, grade))

lines.append("== summary (grade GAP = committed guard accepts what the draft's fixture must refuse)")
for cid, expect, final, grade in summary:
    lines.append("%s expect=%-6s guard=%-18s %s" % (cid, expect, final, grade))
lines.append("GAP count: %d" % sum(1 for s in summary if s[3] == "GAP"))
lines.append("MATCH count: %d" % sum(1 for s in summary if s[3] == "MATCH"))

with open(RECEIPT, "w") as fh:
    fh.write("\n".join(lines) + "\n")
print("receipt: %s (%d lines)" % (RECEIPT, len(lines)))
