#!/usr/bin/env python3
"""d4-typed-labels-check-gate — gate-shaped entry point for the D4 projection check.

`tools/replay-frozen.py` launches a pinned gate as exactly
`[python3, tools/gates/<gate>.py, <input>]`: one input path, no flags. The D4
projection check is a flag-shaped invocation of a peer that lives outside
`tools/gates/`:

    python3 tools/d2-typed-labels.py --packet examples/culture-d4/packet.d4.yml \
        --check examples/culture-d4/typed-labels.d4.yml

This gate is the thin, read-only adapter that makes that check pinnable by a
frozen row: it runs the peer (`tools/d2-typed-labels.py`, loaded by path, never
written and never re-implemented) in its own `--check` mode over the input path
given on the command line, against the D4 packet, and forwards the peer's own
stdout, stderr and exit code unchanged. The input path string is passed through
verbatim, so the peer's own `<path>: byte-identical deterministic projection`
line is stable across recording and replay (the replay mirror holds the frozen
snapshot at the same relative path).

Exit codes are the peer's: 0 the projection is the peer's deterministic build,
1 drift, 2 could-not-evaluate (malformed input, missing packet, tool error).
Usage errors exit 2.

This gate adds no semantics of its own and is not a clearance: exit 0 asserts
byte-identity of a NON-CANON projection, not that its content is sound.
"""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
TOOL = ROOT / "tools/d2-typed-labels.py"
PACKET = "examples/culture-d4/packet.d4.yml"
PROJECTION = "examples/culture-d4/typed-labels.d4.yml"


def main(argv):
    if len(argv) > 2 or (len(argv) == 2 and argv[1] in ("-h", "--help")):
        print(__doc__.strip().splitlines()[0], file=sys.stderr)
        print("usage: d4-typed-labels-check-gate.py [PROJECTION]", file=sys.stderr)
        return 2
    target = argv[1] if len(argv) == 2 else PROJECTION
    if not TOOL.is_file():
        print("could-not-evaluate: peer missing: %s" % TOOL, file=sys.stderr)
        return 2
    proc = subprocess.run(
        [sys.executable, str(TOOL), "--packet", str(ROOT / PACKET), "--check", target],
        stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=False,
    )
    sys.stdout.buffer.write(proc.stdout)
    sys.stdout.flush()
    sys.stderr.buffer.write(proc.stderr)
    sys.stderr.flush()
    return proc.returncode


if __name__ == "__main__":
    sys.exit(main(sys.argv))
