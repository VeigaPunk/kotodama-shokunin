#!/usr/bin/env python3
"""d4-assembly-check-gate — gate-shaped entry point for the D4 assembly check.

`tools/replay-frozen.py` launches a pinned gate as exactly
`[python3, tools/gates/<gate>.py, <input>]`: one input path, no flags. The D4
assembly check (`python3 tools/assemble-culture-d4.py --check`) takes no path at
all — it compares the assembler's fixed output against the assembler's own
deterministic build, so a frozen row could not name the bytes it pinned.

This gate is the thin, read-only adapter that makes that check pinnable: it
loads the assembler `tools/assemble-culture-d4.py` by path (read-only, via
`runpy.run_path`; the assembler's own `assemble()` build path is called, never
re-implemented and never written) and byte-compares the payload it returns
against the input path given on the command line. The input path string is
echoed verbatim, so the line is stable across recording and replay (the replay
mirror holds the frozen snapshot at the same relative path).

    <input>: byte-identical deterministic assembly        # stdout, exit 0
    <input> differs from the deterministic assembly       # stderr, exit 1
    assembly error: ... / could-not-evaluate: ...         # stderr, exit 2

The verdict is sensitive to the live component tree and to the assembler bytes:
the row pins the input packet, and the frozen record carries the assembler and
component digests it was frozen against, so a later component or assembler edit
reads as drift (exit 1) or as a changed gate, never as a silent edit.
Not a clearance: exit 0 asserts byte-identity of a NON-CANON packet.
"""

import runpy
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
TOOL = ROOT / "tools/assemble-culture-d4.py"
PACKET = "examples/culture-d4/packet.d4.yml"


def main(argv):
    if len(argv) > 2 or (len(argv) == 2 and argv[1] in ("-h", "--help")):
        print(__doc__.strip().splitlines()[0], file=sys.stderr)
        print("usage: d4-assembly-check-gate.py [PACKET]", file=sys.stderr)
        return 2
    target = argv[1] if len(argv) == 2 else PACKET
    if not TOOL.is_file():
        print("could-not-evaluate: assembler missing: %s" % TOOL, file=sys.stderr)
        return 2
    try:
        namespace = runpy.run_path(str(TOOL))
        payload = namespace["assemble"]()
        have = Path(target).read_bytes()
    except (ValueError, OSError, KeyError) as exc:
        print("assembly error: %s" % exc, file=sys.stderr)
        return 2
    if have != payload:
        print("%s differs from the deterministic assembly" % target, file=sys.stderr)
        return 1
    print("%s: byte-identical deterministic assembly" % target)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
