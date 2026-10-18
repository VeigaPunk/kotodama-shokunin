#!/usr/bin/env python3
"""R28-X64 — entry source-resolvability: independent cold re-run.

Seat R28-X64 (SCRIBE X64: entry auditor, source resolvability — cold leg) for
round 28, claim **C** (the register-lexicon ceiling: an amendment to
`corpus/knowledge/linguistics/register-strata-attestation.md` plus a new
knowledge entry on register-lexicon ceilings).

This is the **independent** half of the round-28 entry audit. X63 audits the
documents with a Python instrument whose locator check is a compiled regex over
the text and whose amendment check is an in-process ordered-subsequence walk.
This seat re-derives the same readings with **different machinery**, so that an
agreement between the two is evidence and not a shared bug:

    reading                 X63 instrument                 this harness
    locator resolution      REPO_PATH_RE over text,       shell `test -e` per
                            `(root/token).exists()`        token extracted by a
                                                           different regex
    pin re-derivation       hashlib over the path          `sha256sum(1)` subprocess
    absence sweep           `os.walk` + `re.search`        `grep -rln` subprocess
    amendment discipline    in-process subsequence walk    `git diff` numstat over
                                                           the baseline blob
    gap / decision record   independent regexes            independent regexes,
                                                           plus a heading-line scan
    ceiling record          regex over the live text       a `grep -c` over a
                                                           round-27-cited window
    tree isolation          runs in the lane worktree      runs in a
                                                           `git clone --shared`

Running in a clone is the point: the lane worktree moves under a live wave, and
a measurement taken in a moving tree cannot be compared with a later one. The
harness clones, overlays the lane's uncommitted state (untracked **and**
modified — a clone that cannot see uncommitted work blesses exactly the stale
pins a live round creates), measures there, and reports the clone's own revision
beside every reading.

The documents under audit are located **by set difference**, never by a guessed
filename: the harness lists the partition at the declared baseline revision and
in the overlaid clone, and audits the **new** paths plus the **amended** ones.
A round that lands two entries is audited for both; a round that amends one is
audited for the amendment; a round that does neither is reported as `no-target`
rather than silently passing.

Read-only over the repo: the clone is the only thing written, and it is written
under `--scratch` (gitignored). `--selftest` is in-memory plus one temp tree.

Usage:
    python3 reports/round-28/audit/x64-cold-rerun.py --baseline <rev> \\
        --out <receipt.json> --scratch <dir> [--partition corpus/knowledge/linguistics]
    python3 reports/round-28/audit/x64-cold-rerun.py --selftest

Exit codes: 0 all readings reproduced and no defect; 1 a reading disagreed with
the X63 receipt handed in, or a defect was found; 2 could-not-evaluate (clone
failed, baseline unknown, no receipt to compare against). Stdlib only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

SCHEMA = "kotodama-entry-cold-rerun-x64-r28-v1"

# A deliberately different locator regex from X63's: this one anchors on the
# backtick quoting the lane's entries use, and accepts a bare relative path too.
# A backticked token must contain a `.` so that a bare directory mention
# (`reports/round-28/law/`) is not mistaken for a file locator; a trailing
# `:NN` passage suffix is kept and stripped at resolution time.
TICK_PATH_RE = re.compile(r"`((?:corpus|tools|reports|examples)/[^`\s]*\.[\w*\-]+(?::\d[\d,\-]*)?)`")
BARE_PATH_RE = re.compile(
    r"(?<![\w/`])((?:corpus|tools|reports|examples)/[\w./-]+\.(?:md|py|yml|json|tsv|txt|jsonl|yaml))"
)
SHA_LINE_RE = re.compile(r"sha256[^\n]{0,60}?([0-9a-f]{12,64})")
SWEEP_CMD_RE = re.compile(
    r"grep\s+-rl[n]?\s+(?P<flags>(?:-[a-zA-Z]+\s+)*)[\"'`\u201c](?P<pattern>[^\"'`\u201d]+)[\"'`\u201d]\s+"
    r"(?P<path>[^\s;`|)\u2014]+)(?P<pipe>\s*\|\s*wc\s+-l)?"
)
DECLARED_ABSENT_RE = re.compile(
    r"(?i)(not filed|never filed|never existed|no such file|absent|does not exist|"
    r"not round-numbered|no `[^`]+` exists)"
)
GAP_RE = re.compile(r"(?i)(?:^|[\s.;\u2014\u2013|-])gap(?:[\s-]+(?:filled|addressed|served))?\s*:")
GAP_HEAD_RE = re.compile(r"(?mi)^#{2,4}[^\n]*\bgap\b[^\n]*$")
DECISION_HEAD_RE = re.compile(r"(?mi)^#{2,4}[^\n]*decision[- ]record[^\n]*$")

# --- round-28 legs -------------------------------------------------------
CEILING_RE = re.compile(r"(?i)\bceiling\b")
CONSTRAINT_RE = re.compile(
    r"(?i)(design constraint|design bound|constrains?|a constraint|"
    r"bounds? the design|limits? (?:what|which))"
)
ROUND27_RE = re.compile(r"(?i)(round[- ]?27|reports/round-27/|RL-3\b)")


def run(cmd, cwd=None, check=False):
    proc = subprocess.run(cmd, cwd=cwd, capture_output=True, text=True)
    if check and proc.returncode != 0:
        raise RuntimeError(f"{' '.join(cmd)} -> exit {proc.returncode}: {proc.stderr.strip()[:300]}")
    return proc


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def clone_lane(lane, dest, rev=None):
    os.makedirs(os.path.dirname(dest), exist_ok=True)
    if os.path.exists(dest):
        shutil.rmtree(dest)
    cmd = ["git", "clone", "--quiet", "--no-hardlinks", "--shared", lane, dest]
    run(cmd, check=True)
    if rev:
        run(["git", "checkout", "--quiet", rev], cwd=dest, check=True)
    head = run(["git", "rev-parse", "HEAD"], cwd=dest, check=True).stdout.strip()
    return head


def overlay_untracked(lane, clone):
    """Copy the lane's uncommitted state into the clone — untracked **and modified**.

    A `git clone` carries committed content only, so anything the wave has
    written but not committed does not exist inside the clone. Two failure modes
    follow, and the second is the dangerous one:

      * a new entry that has not been committed is invisible, so the harness
        would report `no-target` while the artifact sits on disk in the lane;
      * a **modified** tracked surface is still present at its committed bytes,
        so a pin that the live worktree has already invalidated **re-derives
        clean in the clone**. **A cold leg that cannot see uncommitted work
        blesses exactly the stale pins a live round creates.**

    Both sets are therefore copied, and the manifest is returned so a consumer
    can see that the clone is worktree-equivalent rather than commit-pinned.
    Ignored paths (`.scratch/`, `__pycache__/`) are not copied.
    """
    untracked = run(["git", "ls-files", "--others", "--exclude-standard"],
                    cwd=lane, check=True).stdout
    modified = run(["git", "diff", "--name-only", "HEAD"], cwd=lane, check=True).stdout
    copied = []
    for rel in sorted(set(untracked.split("\n")) | set(modified.split("\n"))):
        rel = rel.strip()
        if not rel:
            continue
        src = os.path.join(lane, rel)
        dst = os.path.join(clone, rel)
        if not os.path.isfile(src):
            continue
        os.makedirs(os.path.dirname(dst) or clone, exist_ok=True)
        shutil.copy2(src, dst)
        copied.append(rel)
    return copied


def partition_listing(clone, partition):
    """Every `.md` in the partition — tracked **and** untracked."""
    out = run(["git", "ls-files", "--cached", "--others", "--exclude-standard", partition],
              cwd=clone, check=True).stdout
    return sorted(p for p in out.split("\n") if p.endswith(".md"))


def locate_targets(clone, partition, baseline):
    """(new, amended, baseline_set) by Git identity, never by a guessed filename."""
    at_baseline = run(["git", "ls-tree", "-r", "--name-only", baseline, "--", partition],
                      cwd=clone).stdout
    base = {p for p in at_baseline.split("\n") if p.endswith(".md")}
    live = set(partition_listing(clone, partition))
    new = sorted(live - base)
    amended = []
    for rel in sorted(base & live):
        blob = run(["git", "show", f"{baseline}:{rel}"], cwd=clone).stdout
        disk = os.path.join(clone, rel)
        try:
            with open(disk, "rb") as fh:
                live_bytes = fh.read()
        except OSError:
            continue
        if hashlib.sha256(blob.encode("utf-8")).hexdigest() != hashlib.sha256(live_bytes).hexdigest():
            amended.append(rel)
    return new, amended, sorted(base), sorted(live)


def resolve_locators(text, clone):
    """Independent resolution: extract, expand, then `test -e` in a shell."""
    tokens, seen = [], set()
    for rx in (TICK_PATH_RE, BARE_PATH_RE):
        for m in rx.finditer(text):
            tok = m.group(1).rstrip(".,;:")
            if tok in seen:
                continue
            seen.add(tok)
            tokens.append(tok)
    resolved, unresolved, exempt = [], [], []
    for tok in tokens:
        if "*" in tok:
            if DECLARED_ABSENT_RE.search(_line_of(text, tok)):
                exempt.append({"token": tok, "why": "declared-absent glob"})
                continue
            hits = run(["bash", "-c", f"ls -d {tok} 2>/dev/null"], cwd=clone).stdout.strip()
            (resolved if hits else unresolved).append(tok)
            continue
        bare = re.sub(r":\d[\d,\-]*$", "", tok)
        expanded = expand_braces(bare)
        missing = [p for p in expanded if run(["test", "-e", p], cwd=clone).returncode != 0]
        if not missing:
            resolved.append(tok)
        elif DECLARED_ABSENT_RE.search(_line_of(text, tok)):
            exempt.append({"token": tok, "why": "declared-absent"})
        else:
            unresolved.append(tok)
    return resolved, unresolved, exempt


def expand_braces(token):
    """Expand `a{b,c}d` into `abd`, `acd`; a token without braces yields itself."""
    m = re.search(r"\{([^{}]+)\}", token)
    if not m:
        return [token]
    out = []
    for alt in m.group(1).split(","):
        out.extend(expand_braces(token[:m.start()] + alt + token[m.end():]))
    return out


def _line_of(text, token):
    for line in text.splitlines():
        if token in line:
            return line
    return ""


def rederive_pins(text, clone):
    checks = []
    for m in SHA_LINE_RE.finditer(text):
        digest = m.group(1)
        start = text.rfind("\n", 0, m.start()) + 1
        end = text.find("\n", m.end())
        line = text[start:end if end > 0 else len(text)]
        if re.search(r"(?i)(before append|before this|prior revision|historical|superseded)", line):
            checks.append({"digest": digest, "verdict": "historical-self-digest"})
            continue
        left = line[:m.start() - start]
        paths = TICK_PATH_RE.findall(left) or BARE_PATH_RE.findall(left)
        if not paths:
            prev_start = text.rfind("\n", 0, start - 1) + 1
            prev = text[prev_start:start]
            if "sha256" not in prev:
                paths = TICK_PATH_RE.findall(prev) or BARE_PATH_RE.findall(prev)
        if not paths:
            checks.append({"digest": digest, "verdict": "unbound"})
            continue
        path = paths[-1]
        if not os.path.exists(os.path.join(clone, path)):
            checks.append({"digest": digest, "path": path, "verdict": "unresolved-path"})
            continue
        actual = run(["sha256sum", path], cwd=clone, check=True).stdout.split()[0]
        checks.append({"digest": digest, "path": path,
                       "verdict": "re-derived" if actual.startswith(digest) else "drift",
                       "actual": actual[:len(digest)]})
    return checks


def rerun_sweeps(text, clone, entry_rel, baseline=None):
    out = []
    for m in SWEEP_CMD_RE.finditer(text):
        pattern, target = m.group("pattern"), m.group("path").rstrip(".,;")
        flags = m.group("flags") or ""
        ignore_case = bool(re.search(r"-i\b", flags))
        tail = text[m.end():m.end() + 200]
        claims_zero = bool(re.search(r"(?:→|->)\s*\*{0,2}0\b", tail))
        rec = {"pattern": pattern, "path": target, "claims_zero": claims_zero,
               "ignore_case": ignore_case, "piped_count": bool(m.group("pipe"))}
        if not os.path.exists(os.path.join(clone, target)):
            rec["verdict"] = "target-absent"
            out.append(rec)
            continue
        # The real tool, with the real flags — a case-insensitive sweep must be
        # re-run case-insensitively or the leg manufactures a false green.
        cmd = ["grep", "-rln"] + (["-i"] if ignore_case else []) + [pattern, target]
        proc = run(cmd, cwd=clone)
        hits = [h for h in proc.stdout.split("\n") if h.strip()]
        pre = [h for h in hits if h != entry_rel]
        rec["hits"] = pre
        rec["self_hit"] = entry_rel in hits
        if not claims_zero:
            rec["verdict"] = "no-zero-claim"
        elif pre:
            # Classify: was the sweep false when written, or did a sibling land
            # between authoring and audit? The same `git grep` at the baseline,
            # minus the audited document itself (the lane's sweeps say "minus
            # this entry").
            rec["verdict"] = "does-not-reproduce"
            if baseline:
                cmd = ["git", "grep", "-l", "-G"] + (["-i"] if ignore_case else []) + \
                      ["-e", pattern, baseline, "--", target]
                bp = run(cmd, cwd=clone)
                base = []
                if bp.returncode in (0, 1):
                    base = [h.strip() for h in bp.stdout.split("\n") if h.strip()]
                    base = [h[len(baseline) + 1:] if h.startswith(baseline + ":") else h
                            for h in base]
                base = [h for h in base if h != entry_rel]
                rec["baseline_hits"] = base
                rec["verdict"] = "authoring-defect" if base else "sibling-landing"
        else:
            rec["verdict"] = "reproduces"
        out.append(rec)
    return out


def amendment_numstat(clone, baseline, entry_rel):
    """Append/insert-only, read from `git diff --numstat`, not from a walk.

    The round-28 rule is that a correction to a filed entry is a **new section**
    or a new file, never an in-place rewrite. `git diff <baseline> -- <path>`
    against the overlaid worktree reports the added and deleted line counts
    directly: a deletion of any size is a rewritten line, which the rule
    forbids. This is deliberately not X63's ordered-subsequence walk — the two
    legs must not share a failure mode.
    """
    proc = run(["git", "diff", "--numstat", "--no-color", baseline, "--", entry_rel],
               cwd=clone)
    added = deleted = 0
    files = []
    for line in proc.stdout.split("\n"):
        line = line.strip()
        if not line:
            continue
        parts = line.split("\t")
        if len(parts) < 3:
            continue
        a, d, path = parts[0], parts[1], parts[2]
        files.append(path)
        if a.isdigit():
            added += int(a)
        if d.isdigit():
            deleted += int(d)
    # The removed-line bodies, so a consumer sees what was rewritten, not just
    # how much. `git diff` marks them with a leading `-` and not `---`.
    body = run(["git", "diff", "--no-color", "--unified=0", baseline, "--", entry_rel],
               cwd=clone).stdout
    removed = [l[1:][:160] for l in body.split("\n")
               if l.startswith("-") and not l.startswith("---")]
    return {"baseline": baseline, "path": entry_rel,
            "added": added, "deleted": deleted, "files": files,
            "sample_removed": removed[:8],
            "append_only": deleted == 0}


def ceiling_read(clone, entry_rel):
    """The ceiling record, read with `grep -c` rather than a Python regex."""
    path = os.path.join(clone, entry_rel)
    ceiling_n = run(["grep", "-c", "-i", "ceiling", path], cwd=clone)
    r27_n = run(["grep", "-c", "-E", "round[- ]?27|reports/round-27/|RL-3", path], cwd=clone)
    constraint_n = run(["grep", "-c", "-E", "-i", "design constraint|constrains?", path], cwd=clone)

    def n(proc):
        try:
            return int(proc.stdout.strip().split("\n")[0] or 0)
        except (ValueError, IndexError):
            return 0

    return {"ceiling_lines": n(ceiling_n), "round27_lines": n(r27_n),
            "constraint_lines": n(constraint_n),
            "recorded_as_constraint": n(ceiling_n) > 0 and n(r27_n) > 0 and n(constraint_n) > 0}


def audit_in_clone(clone, entry_rel, baseline=None, is_amendment=False):
    path = os.path.join(clone, entry_rel)
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8")
    resolved, unresolved, exempt = resolve_locators(text, clone)
    pins = rederive_pins(text, clone)
    sweeps = rerun_sweeps(text, clone, entry_rel, baseline=baseline)
    amendment = amendment_numstat(clone, baseline, entry_rel) if is_amendment else None
    ceiling = ceiling_read(clone, entry_rel)
    gap = bool(GAP_RE.search(text) or GAP_HEAD_RE.search(text))
    decision = bool(DECISION_HEAD_RE.search(text))
    findings = []
    if not gap:
        findings.append({"id": "X64-B", "kind": "gap-not-named"})
    if not decision:
        findings.append({"id": "X64-C", "kind": "no-decision-record"})
    for tok in unresolved:
        findings.append({"id": "X64-D", "kind": "unresolved-locator", "token": tok})
    for p in pins:
        if p["verdict"] in ("drift", "unresolved-path"):
            findings.append({"id": "X64-E", "kind": f"pin-{p['verdict']}", "detail": p})
    for s in sweeps:
        if s["verdict"] in ("does-not-reproduce", "authoring-defect", "sibling-landing"):
            findings.append({"id": "X64-F", "kind": f"sweep-{s['verdict']}",
                             "detail": {"pattern": s["pattern"], "hits": s["hits"],
                                        "baseline_hits": s.get("baseline_hits")}})
    if amendment is not None and not amendment["append_only"]:
        findings.append({"id": "X64-G", "kind": "amendment-not-append-only",
                         "detail": {"deleted": amendment["deleted"],
                                    "sample_removed": amendment["sample_removed"]}})
    if not ceiling["recorded_as_constraint"]:
        findings.append({"id": "X64-H", "kind": "ceiling-not-recorded-as-constraint",
                         "detail": ceiling})
    return {
        "entry": entry_rel,
        "sha256": hashlib.sha256(raw).hexdigest(),
        "bytes": len(raw),
        "lines": text.count("\n") + (0 if text.endswith("\n") else 1),
        "gap_named": gap,
        "decision_record": decision,
        "is_amendment": amendment is not None,
        "amendment": amendment,
        "ceiling": ceiling,
        "locators": {"resolved": resolved, "unresolved": unresolved, "declared_absent": exempt},
        "pins": pins,
        "sweeps": sweeps,
        "findings": findings,
    }


def compare_with_x63(cold, x63_receipt_path):
    """Agreement matrix between this cold leg and the X63 instrument's receipt."""
    if not os.path.exists(x63_receipt_path):
        return {"comparable": False, "why": "no X63 receipt at the given path"}
    with open(x63_receipt_path, encoding="utf-8") as fh:
        x63 = json.load(fh)
    by_name = {}
    for rec in x63.get("entries", []):
        by_name[os.path.basename(rec["entry"])] = rec
    rows = []
    for rec in cold:
        name = os.path.basename(rec["entry"])
        other = by_name.get(name)
        if other is None:
            rows.append({"entry": name, "comparable": False,
                         "why": "X63 did not audit this document"})
            continue
        rows.append({
            "entry": name,
            "comparable": True,
            "sha256_agree": other.get("sha256") == rec["sha256"],
            "gap_agree": bool(other.get("gap", {}).get("named")) == rec["gap_named"],
            "decision_agree": bool(other.get("decision_record", {}).get("present")) == rec["decision_record"],
            "resolved_set_agree": sorted(other.get("locators", {}).get("resolved", [])) == sorted(rec["locators"]["resolved"]),
            "unresolved_set_agree": sorted(other.get("locators", {}).get("unresolved", [])) == sorted(rec["locators"]["unresolved"]),
            "x63_only_resolved": sorted(set(other.get("locators", {}).get("resolved", [])) - set(rec["locators"]["resolved"])),
            "cold_only_resolved": sorted(set(rec["locators"]["resolved"]) - set(other.get("locators", {}).get("resolved", []))),
            "amendment_agree": (other.get("amendment") is None) == (rec["amendment"] is None),
            "ceiling_agree": bool(other.get("ceiling", {}).get("recorded_as_constraint")) == rec["ceiling"]["recorded_as_constraint"],
        })
    return {"comparable": True, "rows": rows}


def selftest():
    failures = []
    # The two locator regexes must agree on the shapes the lane uses.
    sample = "see `corpus/QUALITY.md` and reports/round-26/register/design.md"
    a = set(TICK_PATH_RE.findall(sample))
    b = set(BARE_PATH_RE.findall(sample))
    if "corpus/QUALITY.md" not in a:
        failures.append("tick regex missed a backticked path")
    if "reports/round-26/register/design.md" not in b:
        failures.append("bare regex missed an unquoted path")
    # The sweep regex must read all three quote styles and the piped-count form
    # the round-27 entry uses for all five of its sweeps.
    s1 = 'grep -rln "hold set" corpus/knowledge/verification/ → 0 files'
    s2 = "grep -rln 'hold set' corpus/knowledge/verification/ → 0 files"
    s3 = 'grep -rl -i "illocutionary" corpus/knowledge/ | wc -l` → **0**'
    for s, want in ((s1, "corpus/knowledge/verification/"),
                    (s2, "corpus/knowledge/verification/"),
                    (s3, "corpus/knowledge/")):
        m = SWEEP_CMD_RE.search(s)
        if not m or m.group("path").rstrip(".,;") != want:
            failures.append(f"sweep regex failed on: {s}")
    m = SWEEP_CMD_RE.search(s3)
    if not m or not m.group("pipe"):
        failures.append("sweep regex missed the `| wc -l` piped-count form")
    if not m or not re.search(r"-i\b", m.group("flags") or ""):
        failures.append("sweep regex missed the `-i` flag")
    # A declared-absent token must be exempt; a live token must not.
    if not DECLARED_ABSENT_RE.search("**no `reports/round-4*` exists**"):
        failures.append("declared-absent regex missed the house phrasing")
    if DECLARED_ABSENT_RE.search("see `corpus/QUALITY.md` for the bar"):
        failures.append("declared-absent regex fired on a plain citation")
    # The gap and decision regexes must fire on the house shapes.
    if not GAP_RE.search("- gap filled: the partition lacked X"):
        failures.append("gap regex missed the field form")
    if not GAP_HEAD_RE.search("## 1. The gap this entry fills"):
        failures.append("gap regex missed the heading form")
    if not DECISION_HEAD_RE.search("## 6. Decision record — the rules adopted"):
        failures.append("decision regex missed the heading form")
    # The round-28 ceiling regexes must fire on the record and stay quiet on a
    # document that states a ceiling without calling it a constraint.
    good = "The round-27 measurements (RL-3) show the ceiling is a design constraint."
    bad = "The round-27 measurements (RL-3) show the ceiling."
    if not (CEILING_RE.search(good) and CONSTRAINT_RE.search(good) and ROUND27_RE.search(good)):
        failures.append("ceiling regexes missed the house record shape")
    if not CEILING_RE.search(bad):
        failures.append("ceiling regex missed a bare ceiling mention")
    if CONSTRAINT_RE.search(bad):
        failures.append("constraint regex fired without constraint language")
    return (0 if not failures else 1), failures


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("--lane", default=None, help="lane root (default: this file's repo)")
    parser.add_argument("--baseline", default=None, help="declared baseline revision")
    parser.add_argument("--partition", default="corpus/knowledge/linguistics")
    parser.add_argument("--out", default=None, help="write the receipt JSON here")
    parser.add_argument("--x63", default=None, help="an X63 receipt to compare against")
    parser.add_argument("--scratch", default=None, help="scratch dir for the clone")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args(argv)

    if args.selftest:
        code, failures = selftest()
        for f in failures:
            print(f"SELFTEST FAIL: {f}", file=sys.stderr)
        print(f"SELFTEST {'PASS' if not code else 'FAIL'}: locator regexes, sweep regexes, "
              f"declared-absent exemption, gap and decision shapes, ceiling and constraint "
              f"shapes (failures={len(failures)})")
        return code

    lane = args.lane or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    scratch = args.scratch or os.environ.get("TMPDIR") or tempfile.gettempdir()
    os.makedirs(scratch, exist_ok=True)
    clone = os.path.join(scratch, "x64r28-cold-clone")
    try:
        head = clone_lane(lane, clone)
    except RuntimeError as exc:
        print(f"CANNOT-EVALUATE: clone failed: {exc}", file=sys.stderr)
        return 2
    overlaid = overlay_untracked(lane, clone)

    baseline = args.baseline or "HEAD"
    new, amended, base, live = locate_targets(clone, args.partition, baseline)
    receipts = [audit_in_clone(clone, rel, baseline=baseline, is_amendment=False) for rel in new]
    receipts += [audit_in_clone(clone, rel, baseline=baseline, is_amendment=True) for rel in amended]
    findings = [f for r in receipts for f in r["findings"]]
    result = {
        "schema": SCHEMA,
        "clone_head": head,
        "baseline": baseline,
        "partition": args.partition,
        "counts": {"baseline": len(base), "live": len(live),
                   "new": len(new), "amended": len(amended)},
        "new_entries": new,
        "amended_entries": amended,
        "untracked_overlaid": [p for p in overlaid if p.startswith(args.partition)],
        "worktree_overlaid_count": len(overlaid),
        "entries": receipts,
        "findings": findings,
        "x63_comparison": compare_with_x63(receipts, args.x63) if args.x63 else None,
    }
    if not new and not amended:
        result["note"] = "no-target: the partition is unchanged against the baseline"
    if args.out:
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(result, fh, indent=1, ensure_ascii=False)
    else:
        print(json.dumps(result, indent=1, ensure_ascii=False))
    return 1 if findings else 0


if __name__ == "__main__":
    sys.exit(main())
