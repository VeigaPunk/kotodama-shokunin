#!/usr/bin/env python3
r"""Round-59 declared-command runner and two-way receipt check (QUALITY criterion 9).
Copied from reports/round-56/dry-run.py (round numbers only); its round-56 change, routed by the round-55 verifier
spot-check (corpus/lessons/round-55-verifier-spotcheck.md §5 item 3: the receipts did not
name the revision they measured): `run` now requires `--rev REV`, measures inside a fresh
sandbox clone of the lane checked out at that revision, and prints
`# measured-revision <full hash>`; `check` fails a receipt with no such line.

Declared commands, read from reports/round-59/claims.json and its separability
manifest: each claim's counting_command and manifest acceptance argv, the
separability_command and the agreement_command. Run from the lane root.

  python3 -B reports/round-59/dry-run.py run --rev REV [--label TEXT]   print a receipt block to stdout
  python3 -B reports/round-59/dry-run.py check RECEIPT          two-way check of a receipt file

`run` clones the lane (`git clone --quiet --no-checkout <lane> <dir>` under
/fast/scratch/hyaku/, GIT_DIR, GIT_WORK_TREE and GIT_INDEX_FILE unset), checks out REV detached
there, prints `# measured-revision <full hash> (sandbox clone <dir>)`, and runs every command
from the clone's root; it never writes the lane. It prints `$ <command>` exactly as declared (an argv is rendered with
shlex.join), the output, `exit <n>`, and the expected pre-landing result.
`check` prints MISSING_FROM_RECEIPT <list>, UNDECLARED_IN_RECEIPT <list> and
MEASURED_REVISION <hashes or []>, and exits 0 only when both lists are empty and the receipt
names at least one 40-hex measured revision (1 otherwise, 2 on unreadable input).
"""
import json
import os
import re
import shlex
import subprocess
import sys
import tempfile
from datetime import datetime, timezone

HERE = os.path.dirname(os.path.abspath(__file__))
LANE = os.path.dirname(os.path.dirname(HERE))
SCRATCH = "/fast/scratch/hyaku"
REVLINE = re.compile(r"^# measured-revision ([0-9a-f]{40})\b", re.M)


def declared(root=LANE):
    with open(os.path.join(root, "reports/round-59/claims.json"), encoding="utf-8") as handle:
        claims = json.load(handle)
    with open(os.path.join(root, claims["separability_manifest"]), encoding="utf-8") as handle:
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
                claims.get("expected_pre_landing_separability", "exit 2 before landing: SEPARABILITY_INPUT_ERROR naming the absent C land; checker stops at its first absent land, so later legs are unevaluated")))
    out.append(("agreement", claims["agreement_command"], True, "AGREE, exit 0"))
    return out


def render(command):
    return command if isinstance(command, str) else shlex.join(command)


def sandbox(rev):
    env = {k: v for k, v in os.environ.items() if k not in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE")}
    full = subprocess.run(["git", "-C", LANE, "rev-parse", "--verify", rev + "^{commit}"], env=env,
                          capture_output=True, text=True, check=True).stdout.strip()
    os.makedirs(SCRATCH, exist_ok=True)
    clone = tempfile.mkdtemp(prefix=f"kotodama-r59-measure-{full[:8]}-", dir=SCRATCH)
    subprocess.run(["git", "clone", "--quiet", "--no-checkout", LANE, clone], env=env, check=True)
    subprocess.run(["git", "-C", clone, "-c", "advice.detachedHead=false", "checkout", "--quiet", full],
                   env=env, check=True)
    return full, clone, env


def run(label, rev):
    full, clone, env = sandbox(rev)
    stamp = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    print(f"# {label} {stamp}")
    print(f"# measured-revision {full} (sandbox clone {clone})")
    for role, command, shell, expected in declared(clone):
        print(f"$ {render(command)}")
        result = subprocess.run(command, shell=shell, capture_output=True, text=True, cwd=clone, env=env)
        text = (result.stdout + result.stderr).rstrip("\n")
        if text:
            print(text)
        print(f"exit {result.returncode}")
        print(f"# role: {role}; expected pre-landing: {expected}")
    return 0


def check(path):
    try:
        with open(path, encoding="utf-8") as handle:
            body = handle.read()
        seen = {line[2:] for line in body.splitlines() if line.startswith("$ ")}
        revisions = REVLINE.findall(body)
        want = {render(command) for _role, command, _shell, _expected in declared()}
    except (OSError, ValueError, KeyError) as error:
        print(f"CHECK_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    missing = sorted(want - seen)
    extra = sorted(seen - want)
    print(f"MISSING_FROM_RECEIPT {missing}")
    print(f"UNDECLARED_IN_RECEIPT {extra}")
    print(f"MEASURED_REVISION {revisions}")
    return 1 if missing or extra or not revisions else 0


def main(argv):
    if len(argv) >= 4 and argv[1] == "run" and argv[2] == "--rev":
        label = argv[5] if len(argv) >= 6 and argv[4] == "--label" else "dry run"
        return run(label, argv[3])
    if len(argv) == 3 and argv[1] == "check":
        return check(argv[2])
    print(__doc__, file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv))
