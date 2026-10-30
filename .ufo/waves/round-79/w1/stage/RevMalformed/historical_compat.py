#!/usr/bin/env python3
"""RevMalformed: check a PROPOSED strict ledger allowlist against committed ledger bytes.

Reads each committed reports/round-<N>/ledger.json with `git show <rev>:<path>` (read-only,
never the worktree) and reports, per ledger: byte count, sha256, duplicate keys at any depth,
non-finite constants, pair-level keys outside the proposed allowlist, pair-level required
keys missing, and value types of the validated fields. The allowlist below is the
PROPOSAL under review (RevMalformed), not a frozen contract.

Usage: python3 -B historical_compat.py <lane> <rev>
"""
import collections
import hashlib
import json
import subprocess
import sys

LANE, REV = sys.argv[1], sys.argv[2]
ROUNDS = (73, 74, 75, 76)
PAIR_REQUIRED = ("id", "disposition", "stated_at", "stated_text", "observe_cmd", "parse",
                 "expected_after", "observed_at_base")
PAIR_OPTIONAL = ("stated_parse", "stated_token", "red_at_base", "rederive", "why",
                 "statement_after", "stated_fleet", "observed_note")
PAIR_ALLOWED = set(PAIR_REQUIRED) | set(PAIR_OPTIONAL)


def git_show(path):
    r = subprocess.run(["git", "-C", LANE, "show", "%s:%s" % (REV, path)], capture_output=True)
    return r.returncode, r.stdout


def walk_dupes_and_nonfinite(raw):
    dupes, nonfinite = [], []

    def hook(pairs):
        for k, c in collections.Counter(k for k, _ in pairs).items():
            if c > 1:
                dupes.append(k)
        return dict(pairs)

    def const(name):
        nonfinite.append(name)
        return float("nan")

    doc = json.loads(raw.decode("utf-8"), object_pairs_hook=hook, parse_constant=const)
    return doc, sorted(set(dupes)), sorted(set(nonfinite))


for rnd in ROUNDS:
    path = "reports/round-%d/ledger.json" % rnd
    rc, raw = git_show(path)
    print("== round-%d %s" % (rnd, path))
    if rc:
        print("   git show rc=%d: absent at %s" % (rc, REV[:12]))
        continue
    print("   bytes=%d sha256=%s" % (len(raw), hashlib.sha256(raw).hexdigest()))
    try:
        doc, dupes, nonf = walk_dupes_and_nonfinite(raw)
    except ValueError as exc:
        print("   STRICT-PARSE REFUSE: %s" % exc)
        continue
    print("   duplicate keys: %s | non-finite constants: %s" % (dupes or "none", nonf or "none"))
    pairs = doc.get("pairs") if isinstance(doc, dict) else None
    if not isinstance(pairs, list):
        print("   pairs: not a list -> UNSUPPORTED")
        continue
    bad_nondict = [i for i, p in enumerate(pairs) if not isinstance(p, dict)]
    print("   pairs=%d non-object elements=%s" % (len(pairs), bad_nondict or "none"))
    unknown = collections.Counter()
    missing = collections.Counter()
    types = collections.defaultdict(collections.Counter)
    for p in pairs:
        if not isinstance(p, dict):
            continue
        for k in p:
            if k not in PAIR_ALLOWED:
                unknown[k] += 1
        for k in PAIR_REQUIRED:
            if k not in p:
                missing[k] += 1
        for k in ("id", "disposition", "stated_at", "stated_text", "parse", "expected_after",
                  "observed_at_base", "red_at_base", "rederive", "why", "stated_parse"):
            if k in p:
                types[k][type(p[k]).__name__] += 1
        if "observe_cmd" in p:
            types["observe_cmd"][type(p["observe_cmd"]).__name__] += 1
    print("   pair keys outside allowlist: %s" % (dict(unknown) or "none"))
    print("   pair required keys missing: %s" % (dict(missing) or "none"))
    for k in sorted(types):
        print("   type %-16s %s" % (k, dict(types[k])))
    ids = [p.get("id") for p in pairs if isinstance(p, dict)]
    dup_ids = [i for i, c in collections.Counter(ids).items() if c > 1]
    print("   duplicate ids: %s" % (dup_ids or "none"))
    content = collections.Counter(
        (p.get("stated_at"), p.get("stated_text"), json.dumps(p.get("observe_cmd")))
        for p in pairs if isinstance(p, dict))
    dup_exact = [k for k, c in content.items() if c > 1]
    print("   exact duplicate (stated_at, stated_text, observe_cmd): %s" % (dup_exact or "none"))
    top = doc if isinstance(doc, dict) else {}
    print("   top-level round=%r (type %s) claim=%r base=%r fleet_pin=%r" % (
        top.get("round"), type(top.get("round")).__name__, top.get("claim"),
        top.get("base"), top.get("fleet_pin")))
