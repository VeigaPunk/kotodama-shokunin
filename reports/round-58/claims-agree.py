#!/usr/bin/env python3
r"""Round-58 agreement check (copied unchanged in logic from round 56): claims.json and separability-manifest.json declare the same
claim ids with the same lands, and the same base. Prints AGREE or one DISAGREE line per
difference; exit 0 on agreement, 1 on disagreement, 2 on unreadable input. Stdlib only."""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))


def main():
    try:
        with open(os.path.join(HERE, "claims.json"), encoding="utf-8") as handle:
            claims = json.load(handle)
        with open(os.path.join(HERE, "separability-manifest.json"), encoding="utf-8") as handle:
            manifest = json.load(handle)
        declared = {c["id"]: sorted(c["lands"]) for c in claims["claims"]}
        checked = {u["id"]: sorted(u["lands"]) for u in manifest["claims"]
                   if u.get("role", "claim") == "claim"}
    except (OSError, ValueError, KeyError, TypeError) as error:
        print(f"AGREE_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    problems = []
    if claims.get("base") != manifest.get("base"):
        problems.append(f"DISAGREE base {claims.get('base')} != {manifest.get('base')}")
    for cid in sorted(set(declared) | set(checked)):
        if declared.get(cid) != checked.get(cid):
            problems.append(f"DISAGREE claim {cid} lands {declared.get(cid)} != {checked.get(cid)}")
    for line in problems:
        print(line)
    if not problems:
        print(f"AGREE claims={sorted(declared)}")
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main())
