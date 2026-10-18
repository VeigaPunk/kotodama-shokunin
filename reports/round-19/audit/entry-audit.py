#!/usr/bin/env python3
"""X26 — QUALITY-bar audit over a set of corpus entries (read-only).

Given entry paths (or a git revision range), checks each against the lane's
admission bar (corpus/QUALITY.md) and the round-19 claim-C requirements
(gap-named, frontmatter-complete, decision-record carrying, grounded), then
resolves every `couples:` target on disk. Emits JSON or a summary.

Usage:
    python3 reports/round-19/audit/entry-audit.py FILE [FILE ...]
    python3 reports/round-19/audit/entry-audit.py --since REV   # git diff names
    python3 reports/round-19/audit/entry-audit.py --selftest
"""
import argparse
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))

HEADER_RE = re.compile(r"^- (topic|sources|couples|source|verified-at|recheck|status|gap):", re.M)
GAP_RE = re.compile(r"(residual gap|gap filled|the gap this entry fills|known gaps|missing from|no entry (?:covers|states)|not covered by)", re.I)
DECISION_RE = re.compile(r"(decision record|decision table|DR-[A-Z]{2}-\d|decisions? taken)", re.I)
CALIB_RE = re.compile(r"(mainstream|contested|discredited|calibrat|pop-myth|to-verify)", re.I)
CANON_RE = re.compile(r"(lore-shokunin|non-canon|world[- ]bible|canon)", re.I)
URL_RE = re.compile(r"https?://")
MDREF_RE = re.compile(r"[A-Za-z0-9_./{},\-]+\.md")


def expand_braces(s):
    """Expand one level of {a,b} brace groups into concrete strings."""
    m = re.search(r"\{([^{}]*)\}", s)
    if not m:
        return [s]
    out = []
    for part in m.group(1).split(","):
        out.extend(expand_braces(s[: m.start()] + part + s[m.end():]))
    return out


def header_fields(text):
    return set(HEADER_RE.findall(text))


def source_locators(text):
    """Count source bullets that carry a locator.

    A locator is a URL, a publication year, a backticked repo path, or a
    sha256 digest — the forms this lane's `- sources:` block actually uses
    (internal receipt paths are located by path+digest, not by URL).
    """
    lines = text.splitlines()
    srcs = []
    in_src = False
    for line in lines:
        if re.match(r"^- sources:", line):
            in_src = True
            continue
        if in_src:
            if re.match(r"^- \w", line) and not line.startswith("  "):
                in_src = False
                continue
            if line.startswith("  - "):
                srcs.append(line)
    loc_re = re.compile(r"(https?://|\b(?:19|20)\d{2}\b|`[^`]*\.(?:md|py|json|yml|yaml|tsv)`|\b[0-9a-f]{16,64}\b)")
    with_loc = [s for s in srcs if loc_re.search(s)]
    return len(srcs), len(with_loc)


def couples_targets(text, path):
    m = re.search(r"^- couples:\s*(.*)$", text, re.M)
    if not m:
        return [], []
    line = m.group(1)
    refs = set()
    for raw in MDREF_RE.findall(line):
        for c in expand_braces(raw):
            refs.add(c)
    base = os.path.dirname(os.path.abspath(path))
    knowledge = os.path.join(LANE, "corpus", "knowledge")
    resolved, unresolved = [], []
    for ref in sorted(refs):
        candidates = [
            os.path.normpath(os.path.join(base, ref)),
            os.path.normpath(os.path.join(LANE, ref)),
            os.path.normpath(os.path.join(knowledge, ref)),
        ]
        if any(os.path.isfile(c) for c in candidates):
            resolved.append(ref)
        else:
            unresolved.append(ref)
    return resolved, unresolved


def audit_entry(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8", "replace")
    fields = header_fields(text)
    n_src, n_loc = source_locators(text)
    resolved, unresolved = couples_targets(text, path)
    required = {"topic", "sources", "couples"}
    missing = sorted(required - fields)
    tail_ok = ("verified-at" in fields) and ("recheck" in fields or "source" in fields)
    checks = {
        "path": os.path.relpath(path, LANE),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "size_bytes": len(raw),
        "header_fields": sorted(fields),
        "header_missing_required": missing,
        "header_tail_ok": tail_ok,
        "source_bullets": n_src,
        "source_bullets_with_locator": n_loc,
        "couples_resolved": len(resolved),
        "couples_unresolved": unresolved,
        "gap_named": bool(GAP_RE.search(text)),
        "decision_record": bool(DECISION_RE.search(text)),
        "calibration_flagged": bool(CALIB_RE.search(text)),
        "canon_hygiene": bool(CANON_RE.search(text)),
    }
    checks["quality_bar"] = (
        not missing
        and tail_ok
        and n_src >= 1
        and n_loc >= 1
        and not unresolved
        and checks["gap_named"]
        and checks["decision_record"]
    )
    return checks


def git_new_entries(rev):
    """New/modified corpus entries vs `rev`, including untracked files."""
    out = subprocess.run(
        ["git", "diff", "--name-only", rev, "--", "corpus/knowledge"],
        cwd=LANE, capture_output=True, text=True, check=True,
    ).stdout
    untracked = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard", "--", "corpus/knowledge"],
        cwd=LANE, capture_output=True, text=True, check=True,
    ).stdout
    files = {f for f in (out + "\n" + untracked).splitlines() if f.endswith(".md")}
    return [os.path.join(LANE, f) for f in sorted(files) if os.path.isfile(os.path.join(LANE, f))]


def selftest():
    import tempfile
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        if not cond:
            ok = False
        print(("PASS " if cond else "FAIL ") + name + (" " + detail if detail else ""))

    check("braces", expand_braces("x/{a,b}.md") == ["x/a.md", "x/b.md"], str(expand_braces("x/{a,b}.md")))
    check("braces nested", "x/a.md" in expand_braces("x/{a,{b,c}}.md"))
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "linguistics"))
    open(os.path.join(d, "linguistics", "color-terminology.md"), "w").close()
    p = os.path.join(d, "e.md")
    with open(p, "w") as fh:
        fh.write("- topic: t\n- sources:\n  - Author (2001), *Book*, Pub. https://e.org\n"
                 "- couples: linguistics/color-terminology.md\n- verified-at: 2026-10-18\n- recheck: x\n"
                 "## 1. Gap filled\n## 2. Decision record\n")
    r = audit_entry(p)
    check("selftest entry quality", r["quality_bar"] is True, json.dumps(r))
    check("selftest source locator", r["source_bullets_with_locator"] == 1, str(r["source_bullets_with_locator"]))
    check("selftest gap", r["gap_named"] is True)
    check("selftest decision", r["decision_record"] is True)
    check("selftest couples resolve", r["couples_unresolved"] == [], str(r["couples_unresolved"]))
    # negative control: drop the sources field -> bar must fail
    with open(p, "w") as fh:
        fh.write("- topic: t\n- couples: linguistics/color-terminology.md\n"
                 "## 1. Gap filled\n## 2. Decision record\n")
    check("negative control (no sources fails)", audit_entry(p)["quality_bar"] is False)
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--since")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return 0 if selftest() else 1
    paths = [os.path.abspath(f) for f in args.files]
    if args.since:
        paths += git_new_entries(args.since)
    paths = sorted(set(paths))
    if not paths:
        print("no entries given", file=sys.stderr)
        return 1
    reps = [audit_entry(p) for p in paths]
    npass = sum(1 for r in reps if r["quality_bar"])
    if args.json:
        print(json.dumps({"schema": "kotodama-entry-audit-v1", "entries": reps,
                          "summary": {"total": len(reps), "pass": npass}}, indent=2))
    else:
        for r in reps:
            flag = "PASS" if r["quality_bar"] else "FAIL"
            print(f"{flag} {r['path']} src={r['source_bullets_with_locator']}/{r['source_bullets']} "
                  f"couples={r['couples_resolved']} unresolved={r['couples_unresolved']} "
                  f"gap={r['gap_named']} dec={r['decision_record']}")
        print(f"TOTAL {npass}/{len(reps)} clear the bar")
    return 0 if npass == len(reps) else 2


if __name__ == "__main__":
    sys.exit(main())
