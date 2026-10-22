#!/usr/bin/env python3
"""Round-55 declared-command runner and two-way receipt check (QUALITY criterion 9).
Copied from reports/round-53/dry-run.py; one change: a claim's expected pre-landing
counting result is read from its `expected_pre_landing_counting` field when present.

Declared commands, read from reports/round-55/claims.json and its separability
manifest: each claim's counting_command and manifest acceptance argv, the
separability_command and the agreement_command. Run from the lane root.

  python3 -B reports/round-55/dry-run.py run [--label TEXT]   print a receipt block to stdout
  python3 -B reports/round-55/dry-run.py check RECEIPT          two-way check of a receipt file

`run` prints `$ <command>` exactly as declared (an argv is rendered with
shlex.join), the output, `exit <n>`, and the expected pre-landing result.
`check` prints MISSING_FROM_RECEIPT <list> and UNDECLARED_IN_RECEIPT <list> and
exits 0 only when both lists are empty (1 otherwise, 2 on unreadable input).
"""
import json
import os
import shlex
import subprocess
import sys
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))


def declared():
    with open(os.path.join(HERE, "claims.json"), encoding="utf-8") as handle:
        claims = json.load(handle)
    with open(os.path.join(claims["separability_manifest"]), encoding="utf-8") as handle:
        manifest = json.load(handle)
    acceptance = {u["id"]: u["acceptance"] for u in manifest["claims"] if u.get("acceptance")}
    out = []
    for claim in claims["claims"]:
        out.append((f"{claim['id']} counting", claim["counting_command"], True,
                    claim.get("expected_pre_landing_counting",
                              f"before value {claim['before']} (exit 0)")))
        argv = acceptance[claim["id"]]
        out.append((f"{claim['id']} acceptance", argv, False,
                    f"fails before landing (exit 1), printing the before value; passes at {claim['after_required']}"))
    out.append(("separability", claims["separability_command"], True,
                "exit 2 before landing: SEPARABILITY_INPUT_ERROR naming the absent C land; checker stops at its first absent land, so later legs are unevaluated"))
    out.append(("agreement", claims["agreement_command"], True, "AGREE, exit 0"))
    return out


def render(command):
    return command if isinstance(command, str) else shlex.join(command)


def run(label):
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"# {label} {stamp}")
    for role, command, shell, expected in declared():
        print(f"$ {render(command)}")
        result = subprocess.run(command, shell=shell, capture_output=True, text=True)
        text = (result.stdout + result.stderr).rstrip("\n")
        if text:
            print(text)
        print(f"exit {result.returncode}")
        print(f"# role: {role}; expected pre-landing: {expected}")
    return 0


def check(path):
    try:
        with open(path, encoding="utf-8") as handle:
            seen = {line[2:].rstrip("\n") for line in handle if line.startswith("$ ")}
        want = {render(command) for _role, command, _shell, _expected in declared()}
    except (OSError, ValueError, KeyError) as error:
        print(f"CHECK_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    missing = sorted(want - seen)
    extra = sorted(seen - want)
    print(f"MISSING_FROM_RECEIPT {missing}")
    print(f"UNDECLARED_IN_RECEIPT {extra}")
    return 1 if missing or extra else 0


def main(argv):
    if len(argv) >= 2 and argv[1] == "run":
        label = argv[3] if len(argv) >= 4 and argv[2] == "--label" else "dry run"
        return run(label)
    if len(argv) == 3 and argv[1] == "check":
        return check(argv[2])
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
