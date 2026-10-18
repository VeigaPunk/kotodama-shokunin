#!/usr/bin/env python3
import argparse
import datetime
import hashlib
import json
import os
from pathlib import Path
import shutil
import subprocess
import sys
import tempfile

ROOT = Path(__file__).resolve().parents[3]
FROZEN = Path("tools/gates/frozen/round-22/d4-repin")


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def within(root, relative):
    path = Path(relative)
    if path.is_absolute() or ".." in path.parts:
        raise ValueError("unsafe relative path: " + str(relative))
    target = (root / path).resolve()
    if not target.is_relative_to(root.resolve()):
        raise ValueError("path escapes root: " + str(relative))
    return target


def main():
    parser = argparse.ArgumentParser(description="Verify the R22 D4 peer snapshots, restore them in an isolated clone, then replay the three new rows")
    parser.add_argument("--require-live", action="store_true", help="also refuse if current live peers differ from the new frozen revision")
    args = parser.parse_args()
    scratch = ROOT / ".scratch"
    if Path(os.environ.get("TMPDIR", "")).resolve() != scratch.resolve():
        print("could-not-evaluate: first export TMPDIR=$PWD/.scratch from the lane root", file=sys.stderr)
        return 2
    try:
        receipt = json.loads((ROOT / FROZEN / "freeze-receipt.json").read_text())
        snapshots = receipt["snapshot_pins"]
        live = receipt["live_tool_and_input_pins"]
        if not snapshots or not live or len(snapshots) != len(live):
            raise ValueError("missing or unequal peer pin sets")
        for relative, pinned in live.items():
            source_rel = str(FROZEN / "inputs" / relative)
            if snapshots.get(source_rel) != pinned:
                raise ValueError("peer/snapshot pin mismatch: " + relative)
            source = within(ROOT, source_rel)
            if digest(source) != pinned:
                raise ValueError("snapshot_tampered: " + source_rel)
            if args.require_live and digest(within(ROOT, relative)) != pinned:
                raise ValueError("live_peer_revised: " + relative)
        scratch.mkdir(parents=True, exist_ok=True)
        with tempfile.TemporaryDirectory(prefix="r22-d4-pinned-replay-", dir=scratch) as directory:
            clone = Path(directory) / "repo"
            subprocess.run(["git", "clone", "--quiet", "--no-hardlinks", str(ROOT), str(clone)], check=True, capture_output=True)
            for relative in live:
                target = within(clone, relative)
                target.parent.mkdir(parents=True, exist_ok=True)
                shutil.copyfile(within(ROOT, FROZEN / "inputs" / relative), target)
            shutil.copytree(ROOT / FROZEN, clone / FROZEN, dirs_exist_ok=True)
            for relative, pinned in live.items():
                if digest(within(clone, relative)) != pinned:
                    raise ValueError("restored peer pin mismatch: " + relative)
            command = [sys.executable, "tools/replay-frozen.py", str(FROZEN / "MANIFEST.tsv"), "--json"]
            result = subprocess.run(command, cwd=clone, env={**os.environ, "PYTHONDONTWRITEBYTECODE": "1"}, capture_output=True, text=True, timeout=180)
            if result.stderr:
                sys.stderr.write(result.stderr)
            replay = json.loads(result.stdout)
            output = {
                "date": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                "command": "python3 reports/round-22/bleed/replay.py" + (" --require-live" if args.require_live else ""),
                "peer_snapshot_pairs_checked": len(live),
                "live_peers_checked": args.require_live,
                "execution_context": "isolated Git clone with all pinned D4 peers restored from the new snapshot; TMPDIR is a sibling inside the lane",
                "replay": replay,
            }
            print(json.dumps(output, indent=2, ensure_ascii=False))
            return result.returncode
    except (OSError, ValueError, KeyError, TypeError, subprocess.SubprocessError) as exc:
        print("could-not-evaluate: " + str(exc), file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
