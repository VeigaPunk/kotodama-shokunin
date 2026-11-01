#!/usr/bin/env python3
r"""check-orphan-evidence.py — find evidence files cited by closed round reports
but never committed to the lane repo (the "orphaned evidence" hygiene duty).

Scans the fleet repo's closed round reports for this lane
(`<fleet>/.ufo/reports/round-*/<lane>.md`, all rounds present) — plus,
optionally, a directory of lane closure files (`--extra-dir`, default glob
`round-\d+-verifier-spotcheck\.md`, cited as `lane-closure:<name>`) — and
extracts lane-side path citations:

    reports/...  corpus/...  tools/...  examples/...  templates/...
    scripts/...  .ufo/waves/...
plus root documents LOG.md / SCORECARD.md / SKILL.md / PROVINCE.md /
SHONEN.md / README.md / AGENTS.md / MINT.md / REGIMEN.md.

Line (`:12`, `:12-14`, `:12,13`) and anchor (`#sec`, ` §1`) suffixes are
stripped; `<placeholder>` angles are ignored; only files with a known
extension (.md .txt .json .py .sh .yml .yaml .csv .html .cfg .conf .digest)
count. Each cited path is classified against the lane repo's committed tree
(`git ls-tree -r --name-only HEAD`, plumbing only) and the worktree:

    OK-COMMITTED   in the lane HEAD tree
    OK-FLEET       not a lane path but resolved in the fleet repo tree
                   (fleet scripts/templates/.ufo/...; the fleet tree cannot
                   contain lane paths — the lane junction is untracked there)
    ORPHAN-ONDISK  not in the lane HEAD tree, but the bytes sit uncommitted
                   on disk -> landable via treecommit explicit paths
    ORPHAN-ABSENT  not in the lane HEAD tree and not on disk -> bytes
                   unknowable, record honestly, never fabricate

Exit 0 when no ORPHAN-* line is printed, 1 when at least one is, 2 on input
errors (missing repo, unreadable report dir, git failure) with a stable
`ORPHAN-EVIDENCE-ERROR` label and no traceback.

Limits, stated: the extractor sees only backtick/whitespace/paren-delimited
paths with the known prefixes; a citation built by string concatenation or a
path cited without its directory is invisible to it. Case is compared exactly
against the git tree (NTFS lookups are case-insensitive, so an ORPHAN-ONDISK
may be a case-variant of a committed path — the tool names it, the author
decides). A report citing a path it never claimed was committed is still
flagged: the classification is mechanical, the disposition (land it, or file
a corrections row naming the citation absent) stays the author's.
"""
import argparse
import os
import re
import subprocess
import sys

LABEL = "ORPHAN-EVIDENCE-ERROR"
PREFIXES = (".ufo/waves/", ".ufo/reports/", "reports/", "corpus/", "tools/",
            "examples/", "templates/", "scripts/")
ROOT_DOCS = ("LOG.md", "SCORECARD.md", "SKILL.md", "PROVINCE.md", "SHONEN.md",
             "README.md", "AGENTS.md", "MINT.md", "REGIMEN.md")
EXTS = (".md", ".txt", ".json", ".py", ".sh", ".yml", ".yaml", ".csv",
        ".html", ".cfg", ".conf", ".digest")

# a path-ish token starting with a known prefix or a root doc name;
# never matches directly after a <placeholder> sentinel (\x00) or a path
# separator (a nested non-lane prefix like foo/reports/... is not a lane path)
PATH_RE = re.compile(
    r"(?<![\x00/])(?:\.ufo/(?:waves|reports)|reports|corpus|tools|examples|templates|scripts)"
    r"/[A-Za-z0-9._\-]+(?:/[A-Za-z0-9._\-]+)*"
    r"|(?:LOG|SCORECARD|SKILL|PROVINCE|SHONEN|README|AGENTS|MINT|REGIMEN)\.md")
LINE_SUFFIX_RE = re.compile(r":\d+(?:[-,]\d+)*$")
ANCHOR_RE = re.compile(r"[#§].*$")
TRAIL_RE = ".,;:)'\"]»》"


def sh(repo, *a):
    kw = {"capture_output": True}
    return subprocess.run(["git", "-C", repo] + list(a), **kw)


def git_out(repo, *a):
    r = sh(repo, *a)
    if r.returncode != 0:
        sys.stderr.write("%s: git %s failed: %s\n"
                         % (LABEL, a[0], (r.stderr or b"").decode("utf-8", "replace").strip()))
        sys.exit(2)
    return r.stdout.decode("utf-8", "replace")


def clean_token(tok):
    tok = ANCHOR_RE.sub("", tok)
    tok = LINE_SUFFIX_RE.sub("", tok)
    tok = tok.rstrip(TRAIL_RE)
    return tok.replace("\\", "/")


def candidate_tokens(text):
    # mask <placeholder> shapes with a sentinel the path regex refuses to
    # match after, so `<scratch>/reports/x.txt` yields nothing
    text = re.sub(r"<[^<>\n]*>", "\x00", text)
    for m in PATH_RE.finditer(text):
        tok = clean_token(m.group(0))
        if not tok or not tok.lower().endswith(EXTS):
            continue
        yield tok


def collect_reports(fleet_root, lane_id):
    rdir = os.path.join(fleet_root, ".ufo", "reports")
    if not os.path.isdir(rdir):
        sys.stderr.write("%s: no reports dir under %s\n" % (LABEL, fleet_root))
        sys.exit(2)
    found = {}
    for name in sorted(os.listdir(rdir)):
        m = re.fullmatch(r"round-(\d+)", name)
        if not m:
            continue
        path = os.path.join(rdir, name, "%s.md" % lane_id)
        if os.path.isfile(path):
            try:
                with open(path, "r", encoding="utf-8", errors="replace") as fh:
                    found[name] = fh.read()
            except OSError as exc:
                sys.stderr.write("%s: unreadable report %s: %s\n" % (LABEL, path, exc))
                sys.exit(2)
    if not found:
        sys.stderr.write("%s: no reports found for lane %s\n" % (LABEL, lane_id))
        sys.exit(2)
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--fleet", default="", help="fleet repo root (closed reports)")
    ap.add_argument("--lane", default="", help="lane repo (worktree + HEAD tree)")
    ap.add_argument("--lane-id", default="kotodama")
    ap.add_argument("--extra-dir", default="",
                    help="optional dir of lane closure files (e.g. corpus/lessons) to scan too")
    ap.add_argument("--extra-glob", default=r"round-\d+-verifier-spotcheck\.md",
                    help="filename glob (re.fullmatch) for --extra-dir")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args()
    if not args.selftest and (not args.fleet or not args.lane):
        sys.stderr.write("%s: --fleet and --lane are required without --selftest\n" % LABEL)
        sys.exit(2)

    if args.selftest:
        return selftest()

    lane, fleet = os.path.abspath(args.lane), os.path.abspath(args.fleet)
    if not os.path.isdir(os.path.join(lane, ".git")) and not os.path.exists(os.path.join(lane, ".git")):
        sys.stderr.write("%s: %s is not a git repo\n" % (LABEL, lane))
        sys.exit(2)
    tree = set(git_out(lane, "ls-tree", "-r", "--name-only", "HEAD").splitlines())
    fleet_tree = set(git_out(fleet, "ls-tree", "-r", "--name-only", "HEAD").splitlines())
    reports = collect_reports(fleet, args.lane_id)
    if args.extra_dir:
        glob = args.extra_glob
        for name in sorted(os.listdir(args.extra_dir)):
            if not re.fullmatch(glob, name):
                continue
            path = os.path.join(args.extra_dir, name)
            try:
                with open(path, "r", encoding="utf-8", errors="replace") as fh:
                    reports["lane-closure:" + name] = fh.read()
            except OSError as exc:
                sys.stderr.write("%s: unreadable extra %s: %s\n" % (LABEL, path, exc))
                sys.exit(2)

    cites = {}   # path -> sorted round names
    for rnd, text in reports.items():
        for tok in candidate_tokens(text):
            cites.setdefault(tok, set()).add(rnd)

    orphans = 0
    for path in sorted(cites):
        rounds = ",".join(sorted(cites[path],
                                 key=lambda r: int(r.split("-")[-1].split(":")[0])
                                 if r.split("-")[-1].split(":")[0].isdigit() else 10 ** 6))
        if path in tree:
            print("OK-COMMITTED %s cited=%s" % (path, rounds))
            continue
        # not in the lane tree: fleet-side infrastructure (scripts/, templates/,
        # fleet .ufo/...) may resolve in the fleet repo; the fleet tree cannot
        # contain lane paths (the lane junction is untracked there)
        if path in fleet_tree:
            print("OK-FLEET %s cited=%s" % (path, rounds))
            continue
        full = os.path.join(lane, path.replace("/", os.sep))
        if path.startswith(".ufo/"):
            full = os.path.join(fleet, path.replace("/", os.sep))
        if os.path.isfile(full):
            print("ORPHAN-ONDISK %s cited=%s" % (path, rounds))
            orphans += 1
        else:
            print("ORPHAN-ABSENT %s cited=%s" % (path, rounds))
            orphans += 1
    print("ORPHAN-EVIDENCE: %d orphan(s) over %d cited path(s) in %d report(s)"
          % (orphans, len(cites), len(reports)))
    return 1 if orphans else 0


def selftest():
    cases = [
        # (token, expected class of cleaned path)
        ("`reports/round-5/validation.json`", "reports/round-5/validation.json"),
        ("`corpus/lessons/round-49.md#post-review-corrections`", "corpus/lessons/round-49.md"),
        ("LOG.md:4341,4345", "LOG.md"),
        ("`corpus/lessons/round-74.md:37-38`", "corpus/lessons/round-74.md"),
        (".ufo/waves/round-56/build/CriticSeparabilityExports.md §1-§2",
         ".ufo/waves/round-56/build/CriticSeparabilityExports.md"),
        ("<scratch>/reports/x.txt", None),
        ("reports/round-2", None),                       # no extension -> skip
        ("`SKILL.md:767`", "SKILL.md"),
        ("corpus/SOURCES.md.", "corpus/SOURCES.md"),     # trailing period stripped
        ("reports/round-79/telemetry/x.txt`", "reports/round-79/telemetry/x.txt"),
    ]
    bad = 0
    for text, want in cases:
        got = list(candidate_tokens(text))
        ok = (want in got) if want else (len(got) == 0)
        print("selftest: %-58r -> %s as-expected=%s" % (text, got, "True" if ok else "False"))
        if not ok:
            bad += 1
    # suffix-strip edge: a path that legitimately contains a dot-version
    got = list(candidate_tokens("reports/round-9/summary-v1.2.md"))
    ok = got == ["reports/round-9/summary-v1.2.md"]
    print("selftest: dotted filename passthrough -> %s as-expected=%s" % (got, "True" if ok else "False"))
    bad += 0 if ok else 1
    print("SELFTEST: %s" % ("PASS" if bad == 0 else "FAIL %d" % bad))
    return 0 if bad == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
