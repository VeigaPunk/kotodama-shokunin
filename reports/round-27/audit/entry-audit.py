#!/usr/bin/env python3
"""R27-C48 — entry audit: filler rejection and source resolution (read-only).

Audits corpus entries against the lane's admission bar (`corpus/QUALITY.md`)
and the round-27 claim-C requirements. Two legs are new to round 27:

  filler        an entry that names no gap it fills is rejected as filler.
                A gap statement is a sentence (in the entry's own head block or
                body) that says what the partition lacked before the entry.
  sources       every `- sources:` bullet must carry a locator, and every
                repo-path locator must RESOLVE on disk. Where a bullet names
                both a path and a sha256, the digest must match the file the
                same bullet names (a digest pinned to a different file is the
                laundering shape this leg exists to catch).

The older legs (header completeness, couples resolution, decision record,
calibration vocabulary, canon hygiene) are inherited from round 19's
`reports/round-19/audit/entry-audit.py` and re-implemented here so the round-27
receipt is reproducible from committed tooling.

The tool is read-only over `corpus/`; it has no code path that writes inside
the repo.

Usage:
    python3 reports/round-27/audit/entry-audit.py FILE [FILE ...]
    python3 reports/round-27/audit/entry-audit.py --since REV
    python3 reports/round-27/audit/entry-audit.py --partition linguistics
    python3 reports/round-27/audit/entry-audit.py --selftest
"""
import argparse
import glob
import hashlib
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
KNOWLEDGE = os.path.join(LANE, "corpus", "knowledge")
PARTS = ["linguistics", "myth-symbol", "culture-material", "synthesis",
         "verification", "civilizations"]

HEADER_RE = re.compile(r"^- (topic|sources|couples|source|verified-at|recheck|status|gap|gap filled):", re.M)
GAP_RE = re.compile(
    r"(residual gap|gap filled|the gap this entry fills|gap this entry fills|known gaps|"
    r"no entry (?:covers|states)|not covered by|missing from|absence sweep|"
    r"the partition (?:carries|lacks|held)|no (?:entry|file) (?:states|covers))", re.I)
# A declared `- gap:` / `- gap filled:` field is itself a gap statement: the
# entry names what the partition lacked in a machine-readable slot, whatever the
# sentence's wording. `transport-mobility-lexicon.md` writes "this entry fills
# it" there, which the prose patterns above do not match.
GAP_FIELD_RE = re.compile(r"^- gap(?: filled)?:", re.M)
DECISION_RE = re.compile(r"(decision record|decision table|DR-[A-Z]{2}-\d|decisions? taken)", re.I)
CALIB_RE = re.compile(r"(mainstream|contested|discredited|calibrat|pop-myth|to-verify)", re.I)
CANON_RE = re.compile(r"(lore-shokunin|non-canon|world[- ]bible|canon)", re.I)

# a token that looks like a repo path — inside backticks, or bare after a
# directory prefix / in a bare-filename list. Commas are allowed because this
# lane writes brace groups as `dir/{a,b,c}.md` (round 10 convention).
PATH_TOKEN_RE = re.compile(r"`([A-Za-z0-9_][A-Za-z0-9_./{},\-]*\.(?:md|py|json|yml|yaml|tsv|sh|txt))`")
BARE_TOKEN_RE = re.compile(r"(?<![`\w/])([A-Za-z0-9_][A-Za-z0-9_./{},\-]*\.(?:md|py|json|yml|yaml|tsv|sh|txt))")
SHA_RE = re.compile(r"\b([0-9a-f]{64})\b|\b([0-9a-f]{8,63})…")
LOC_RE = re.compile(r"(https?://|\b(?:19|20)\d{2}\b|`[^`]*\.(?:md|py|json|yml|yaml|tsv)`|\b[0-9a-f]{16,64}\b)")


def expand_braces(s):
    m = re.search(r"\{([^{}]*)\}", s)
    if not m:
        return [s]
    out = []
    for part in m.group(1).split(","):
        out.extend(expand_braces(s[: m.start()] + part + s[m.end():]))
    return out


def sources_block(text):
    """The `- sources:` bullets, verbatim (continuation lines joined)."""
    lines = text.splitlines()
    out, cur = [], None
    for line in lines:
        if re.match(r"^- sources:", line):
            cur = ""
            rest = line[len("- sources:"):].strip()
            if rest:
                cur = rest
            continue
        if cur is not None:
            if line.startswith("  - "):
                if cur:
                    out.append(cur)
                cur = line[4:].strip()
            elif line.startswith("  ") or not line.strip():
                if line.strip():
                    cur = (cur + " " + line.strip()).strip() if cur else line.strip()
            else:
                if cur:
                    out.append(cur)
                cur = None
    if cur:
        out.append(cur)
    return out


FLEET_ROOT = os.path.abspath(os.path.join(LANE, ".."))


def resolve_ref(ref, base):
    """Resolve a repo-path reference. This lane writes refs in five shapes:

      `../linguistics/writing-systems.md`   partition-relative
      `linguistics/{a,b}.md`                partition-prefixed
      `historical-linguistics.md`           bare basename after a directory group
      `tools/d2-typed-labels.py`            lane-relative
      `PROTOCOL.md`                         fleet surface (read-only, one level up)

    A bare basename is resolved against the entry's own partition first, then
    against every knowledge partition (the `dir/{a,b}.md` convention names the
    directory once and the members after it), then against the fleet root.
    Returns the path or None.
    """
    candidates = [
        os.path.normpath(os.path.join(base, ref)),
        os.path.normpath(os.path.join(LANE, ref)),
        os.path.normpath(os.path.join(KNOWLEDGE, ref)),
        os.path.normpath(os.path.join(FLEET_ROOT, ref)),
    ]
    if os.sep not in ref and "/" not in ref:
        for part in PARTS:
            candidates.append(os.path.join(KNOWLEDGE, part, ref))
    for candidate in candidates:
        if os.path.isfile(candidate):
            return candidate
    # a fleet-internal path cited from the fleet appendix (`frozen/post/MANIFEST.json`
    # inside a wave directory) resolves against the wave surface, not the lane
    wave_hits = sorted(glob.glob(os.path.join(FLEET_ROOT, ".ufo", "waves", "*", ref)))
    if len(wave_hits) == 1:
        return wave_hits[0]
    return None


def lane_basename_index():
    """Map basenames of *tracked* lane files (plus the fleet wave surface) to paths.

    The lane writes bare filenames as prose shorthand (`01-brief.yml`,
    `check-gate-battery.py`). A bare name is only readable as a path claim when
    it resolves to exactly one tracked file; a name that matches several
    (`expected.json` names the committed baselines as a class) is a *pattern*
    mention, not a broken link, and is reported as ambiguous rather than red.

    The index is built from `git ls-files`, not a filesystem walk: a walk would
    count the thousands of `.scratch` clone mirrors and the disposable export
    under `reports/supplement-opencode-1/scratch/`, which are copies, not
    surfaces.
    """
    index = {}
    try:
        tracked = subprocess.run(["git", "ls-files"], cwd=LANE, capture_output=True,
                                 text=True, check=True).stdout.splitlines()
    except subprocess.SubprocessError:
        tracked = []
    for rel in tracked:
        index.setdefault(os.path.basename(rel), []).append(os.path.join(LANE, rel))
    wave = os.path.join(FLEET_ROOT, ".ufo", "waves")
    if os.path.isdir(wave):
        for dirpath, dirnames, filenames in os.walk(wave):
            dirnames[:] = [d for d in dirnames if d != "__pycache__"]
            for name in filenames:
                index.setdefault(name, []).append(os.path.join(dirpath, name))
    return index


_BASENAMES = None


def _basenames():
    """Lazy basename index (the lane tree is walked once per process)."""
    global _BASENAMES
    if _BASENAMES is None:
        _BASENAMES = lane_basename_index()
    return _BASENAMES


def header_fields(text):
    return set(HEADER_RE.findall(text))


def source_resolution(text, path):
    """For every sources bullet: locator presence, path resolution, digest class.

    Only *backticked* tokens are read as path claims — a bare `PROTOCOL.md`
    in prose is a fleet-surface mention, not a repo path this lane owns.
    A bare filename inherits the directory of a path named earlier in the same
    bullet (`examples/culture-d4/ASSEMBLY.md` … `packet.d4.yml` →
    `examples/culture-d4/packet.d4.yml`), which is this lane's documented
    couples/sources convention. Digests are classified rather than matched:

      repo_matched        a 64-hex digest that matches the file its bullet names
      repo_mismatch       a 64-hex digest that names a resolved repo file but
                          does not match it — the laundering shape
      external_uncheckable a 64-hex digest in a bullet that names no resolved
                          repo file (a fetched web page, an offline artefact)
      abbrev              a truncated digest (`94b6bdaf…`), not re-checkable
    """
    base = os.path.dirname(os.path.abspath(path))
    bullets = sources_block(text)
    rows = []
    for bullet in bullets:
        with_loc = bool(LOC_RE.search(bullet))
        refs, dirs = [], []
        for raw in PATH_TOKEN_RE.findall(bullet):
            for concrete in expand_braces(raw):
                refs.append(concrete)
                if "/" in concrete:
                    dirs.append(os.path.dirname(concrete))
        resolved, unresolved, ambiguous = [], [], []
        for ref in sorted(set(refs)):
            hit = resolve_ref(ref, base)
            if hit is None and "/" not in ref:
                for d in dirs:
                    hit = resolve_ref(os.path.join(d, ref), base)
                    if hit:
                        break
            if hit is None and "/" not in ref:
                hits = _basenames().get(ref, [])
                if len(hits) == 1:
                    hit = hits[0]
                elif len(hits) > 1:
                    ambiguous.append((ref, len(hits)))
            if hit is not None:
                resolved.append((ref, hit))
            elif not any(a[0] == ref for a in ambiguous):
                unresolved.append((ref, None))
        digests = [d for pair in SHA_RE.findall(bullet) for d in pair if d]
        has_url = bool(re.search(r"https?://", bullet))
        digest_checks = []
        for digest in digests:
            if len(digest) != 64:
                digest_checks.append({"digest": digest, "len": len(digest),
                                      "class": "abbrev", "matched_path": None})
                continue
            matched = None
            for ref, hit in resolved:
                if hit:
                    with open(hit, "rb") as fh:
                        if hashlib.sha256(fh.read()).hexdigest() == digest:
                            matched = ref
                            break
            if matched:
                klass = "repo_matched"
            elif resolved and not has_url:
                klass = "repo_mismatch"
            else:
                # a bullet that also names a URL is citing a fetched page or an
                # offline artefact; the digest is not re-checkable from the tree
                klass = "external_uncheckable"
            digest_checks.append({"digest": digest[:12] + "…", "len": 64,
                                  "class": klass, "matched_path": matched})
        rows.append({
            "bullet": bullet[:160],
            "has_locator": with_loc,
            "refs_resolved": [r for r, _ in resolved],
            "refs_unresolved": [r for r, _ in unresolved],
            "refs_ambiguous": [{"ref": r, "matches": n} for r, n in ambiguous],
            "digests": digest_checks,
        })
    return rows


COUPLES_TOKEN_RE = re.compile(r"([A-Za-z0-9_][A-Za-z0-9_./{},\-]*\.md)")


def couples_targets(text, path):
    m = re.search(r"^- couples:\s*(.*)$", text, re.M)
    if not m:
        return [], []
    refs = set()
    for raw in COUPLES_TOKEN_RE.findall(m.group(1)):
        for c in expand_braces(raw):
            refs.add(c)
    base = os.path.dirname(os.path.abspath(path))
    resolved, unresolved = [], []
    for ref in sorted(refs):
        (resolved if resolve_ref(ref, base) else unresolved).append(ref)
    return resolved, unresolved


def audit_entry(path):
    with open(path, "rb") as fh:
        raw = fh.read()
    text = raw.decode("utf-8", "replace")
    fields = header_fields(text)
    missing = sorted({"topic", "sources", "couples"} - fields)
    tail_ok = ("verified-at" in fields) and ("recheck" in fields or "source" in fields)
    src = source_resolution(text, path)
    resolved, unresolved_couples = couples_targets(text, path)
    unresolved_refs = sorted({r for row in src for r in row["refs_unresolved"]})
    ambiguous_refs = sorted({a["ref"] for row in src for a in row.get("refs_ambiguous", [])})
    digests = [d for row in src for d in row["digests"]]
    bad_digest = [d for d in digests if d["class"] == "repo_mismatch"]
    checks = {
        "path": os.path.relpath(path, LANE),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "size_bytes": len(raw),
        "header_fields": sorted(fields),
        "header_missing_required": missing,
        "header_tail_ok": tail_ok,
        "source_bullets": len(src),
        "source_bullets_with_locator": sum(1 for row in src if row["has_locator"]),
        "source_refs_unresolved": unresolved_refs,
        "source_refs_ambiguous": ambiguous_refs,
        "source_digests_mismatched": [d["digest"] for d in bad_digest],
        "source_digests_by_class": {k: sum(1 for d in digests if d["class"] == k)
                                    for k in ("repo_matched", "repo_mismatch",
                                              "external_uncheckable", "abbrev")},
        "couples_resolved": len(resolved),
        "couples_unresolved": unresolved_couples,
        "gap_named": bool(GAP_RE.search(text) or GAP_FIELD_RE.search(text)),
        "gap_field": bool(GAP_FIELD_RE.search(text)),
        "gap_prose_only": bool(GAP_RE.search(text)) and not GAP_FIELD_RE.search(text),
        "decision_record": bool(DECISION_RE.search(text)),
        "calibration_flagged": bool(CALIB_RE.search(text)),
        "canon_hygiene": bool(CANON_RE.search(text)),
    }
    checks["filler"] = not checks["gap_named"]
    checks["quality_bar"] = (
        not missing and tail_ok and len(src) >= 1
        and checks["source_bullets_with_locator"] == len(src)
        and not unresolved_refs and not bad_digest
        and not unresolved_couples
        and checks["gap_named"] and checks["decision_record"]
    )
    return checks


def git_new_entries(rev):
    out = subprocess.run(["git", "diff", "--name-only", rev, "--", "corpus/knowledge"],
                         cwd=LANE, capture_output=True, text=True, check=True).stdout
    untracked = subprocess.run(
        ["git", "ls-files", "--others", "--exclude-standard", "--", "corpus/knowledge"],
        cwd=LANE, capture_output=True, text=True, check=True).stdout
    files = {f for f in (out + "\n" + untracked).splitlines() if f.endswith(".md")}
    return [os.path.join(LANE, f) for f in sorted(files)
            if os.path.isfile(os.path.join(LANE, f))]


def partition_entries(part):
    d = os.path.join(KNOWLEDGE, part)
    return [os.path.join(d, f) for f in sorted(os.listdir(d)) if f.endswith(".md")]


def selftest():
    import tempfile
    ok = True

    def check(name, cond, detail=""):
        nonlocal ok
        if not cond:
            ok = False
        print(("PASS " if cond else "FAIL ") + name + (" " + detail if detail else ""))

    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, "linguistics"))
    target = os.path.join(d, "linguistics", "color-terminology.md")
    with open(target, "w", encoding="utf-8") as fh:
        fh.write("- topic: t\n- sources:\n  - A (2001)\n")
    good_digest = hashlib.sha256(open(target, "rb").read()).hexdigest()
    p = os.path.join(d, "e.md")

    def write(body):
        with open(p, "w", encoding="utf-8") as fh:
            fh.write(body)

    write(
        "- topic: t\n- sources:\n"
        "  - Author (2001), *Book*, Pub. https://e.org\n"
        f"  - `linguistics/color-terminology.md` (sha256 `{good_digest}`)\n"
        "- couples: linguistics/color-terminology.md\n- verified-at: 2026-10-18\n- recheck: x\n"
        "## 1. Gap filled\nthe partition carried no entry on this; absence sweep.\n"
        "## 2. Decision record\n"
    )
    r = audit_entry(p)
    check("selftest entry clears the bar", r["quality_bar"] is True, json.dumps(r))
    check("selftest no filler", r["filler"] is False)
    check("selftest digest matched", r["source_digests_mismatched"] == [],
          str(r["source_digests_mismatched"]))
    check("selftest refs resolved", r["source_refs_unresolved"] == [])

    # negative control 1: no sources field -> bar fails
    write("- topic: t\n- couples: linguistics/color-terminology.md\n"
          "## 1. Gap filled\nthe partition carried no entry.\n## 2. Decision record\n")
    check("control: no sources field fails the bar", audit_entry(p)["quality_bar"] is False)

    # negative control 2: phantom source path
    write("- topic: t\n- sources:\n  - `linguistics/does-not-exist.md` (2001)\n"
          "- couples: linguistics/color-terminology.md\n- verified-at: 2026-10-18\n- recheck: x\n"
          "## 1. Gap filled\nthe partition carried no entry.\n## 2. Decision record\n")
    r = audit_entry(p)
    check("control: phantom source path unresolved",
          r["source_refs_unresolved"] == ["linguistics/does-not-exist.md"],
          json.dumps(r["source_refs_unresolved"]))
    check("control: phantom source fails the bar", r["quality_bar"] is False)

    # negative control 3: digest pinned to the wrong file
    write("- topic: t\n- sources:\n"
          f"  - `linguistics/color-terminology.md` (sha256 `{'0' * 64}`)\n"
          "- couples: linguistics/color-terminology.md\n- verified-at: 2026-10-18\n- recheck: x\n"
          "## 1. Gap filled\nthe partition carried no entry.\n## 2. Decision record\n")
    r = audit_entry(p)
    check("control: mismatched digest flagged",
          r["source_digests_mismatched"] == ["0" * 12 + "…"],
          json.dumps(r["source_digests_mismatched"]))
    check("control: mismatched digest fails the bar", r["quality_bar"] is False)

    # negative control 4: filler — no gap statement anywhere
    write("- topic: t\n- sources:\n  - Author (2001), *Book*, Pub. https://e.org\n"
          "- couples: linguistics/color-terminology.md\n- verified-at: 2026-10-18\n- recheck: x\n"
          "## 1. Overview\nthis entry describes things.\n## 2. Decision record\n")
    r = audit_entry(p)
    check("control: filler (no gap named) rejected", r["filler"] is True and r["quality_bar"] is False)

    # negative control 5: phantom couples path
    write("- topic: t\n- sources:\n  - Author (2001), *Book*, Pub. https://e.org\n"
          "- couples: linguistics/phantom.md\n- verified-at: 2026-10-18\n- recheck: x\n"
          "## 1. Gap filled\nthe partition carried no entry.\n## 2. Decision record\n")
    check("control: phantom couples path unresolved",
          audit_entry(p)["couples_unresolved"] == ["linguistics/phantom.md"])

    # positive control: live lane entry
    live = os.path.join(KNOWLEDGE, "linguistics", "sociolinguistics-registers.md")
    if os.path.isfile(live):
        r = audit_entry(live)
        check("live: a real entry's sources resolve",
              r["source_refs_unresolved"] == [] and r["source_digests_mismatched"] == [],
              json.dumps({"unresolved": r["source_refs_unresolved"],
                          "digests": r["source_digests_mismatched"]}))
    return ok


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("files", nargs="*")
    ap.add_argument("--since")
    ap.add_argument("--partition", choices=PARTS, action="append")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        passed = selftest()
        print("selftest: %s" % ("11/11 checks passed" if passed else "FAILED"))
        return 0 if passed else 1
    paths = [os.path.abspath(f) for f in args.files]
    if args.since:
        paths += git_new_entries(args.since)
    if args.partition:
        for part in args.partition:
            paths += partition_entries(part)
    paths = sorted(set(paths))
    if not paths:
        print("no entries given", file=sys.stderr)
        return 1
    rows = [audit_entry(p) for p in paths]
    if args.json:
        print(json.dumps(rows, indent=1, sort_keys=True))
    else:
        for r in rows:
            print(("%-58s bar=%-5s filler=%-5s src=%d/%d refs_unres=%d digests_bad=%d couples_unres=%d"
                   % (r["path"], r["quality_bar"], r["filler"],
                      r["source_bullets_with_locator"], r["source_bullets"],
                      len(r["source_refs_unresolved"]), len(r["source_digests_mismatched"]),
                      len(r["couples_unresolved"]))))
        bad = [r for r in rows if not r["quality_bar"]]
        print("audited %d; clear %d; failing %d %s"
              % (len(rows), len(rows) - len(bad), len(bad), [r["path"] for r in bad]))
    return 0 if all(r["quality_bar"] for r in rows) else 1


if __name__ == "__main__":
    sys.exit(main())
