#!/usr/bin/env python3
"""Guard-proof fixtures for the CORPUS item-10 id-collision extractor.

Each fixture is a mirror tree  <root>/mirror-<name>/corpus/SOURCES.md  whose
registry is the REAL lane registry at base f556d1049fe651d3d63975600b13acd9fb686f15
with ONE planted row inserted immediately after the last registry row, INSIDE the
`## Registry` table.

The planted row is a clone of the lane's real S884 row (11 cells, valid kind/tier/
status/opened/recheck) with the id cell set to a STAGED id that is NOT in the lane
registry at base (S985 -> katobank, S986 -> Persee 1120, S987 -> Persee 1114,
S988 -> UCASS, S989 -> JStage jcss, S990 -> K10plus) and its URLs rewritten to
example.invalid/guard-proof/planted-<id>.pdf, so the planted row can never be
dismissed as a duplicate of an existing lane row.

Why a STAGED id: the guard's job is to detect a staged-vs-lane id collision. A
planted row whose id is in the staged id set is a real collision; a planted row
whose id is unique to the lane proves nothing about the guard.

Indent per fixture:
  control  0 spaces (the real registry, unmodified)
  1sp      1 leading space
  2sp      2 leading spaces
  3sp      3 leading spaces
  4sp      4 leading spaces  (indented code per the census parser note)
  tab      one leading TAB    (the markdown table-row grammar is spaces, not tabs)

corpus/knowledge and corpus/lessons are symlinks to the lane's real dirs so the
census used-by existence check (E11) resolves exactly as it does on the lane.
SKILL.md is symlinked for the same reason (two rows cite it in used-by).

Run:  python3 make-fixtures.py <root>     (root is created if absent)
"""
import os
import pathlib
import re
import sys

LANE = pathlib.Path("/home/vgpnk/Projects/shokunin/kotodama-shokunin")
BASE = "f556d1049fe651d3d63975600b13acd9fb686f15"

# planted ids: staged ids that the lane registry does NOT hold at base
PLANTS = [
    ("1sp", "S985", " "),
    ("2sp", "S986", "  "),
    ("3sp", "S987", "   "),
    ("4sp", "S988", "    "),
    ("tab", "S989", "\t"),
]


def lane_registry():
    import subprocess
    r = subprocess.run(["git", "-C", str(LANE), "show", "%s:corpus/SOURCES.md" % BASE],
                       capture_output=True, check=True)
    return r.stdout.decode("utf-8")


def main():
    root = pathlib.Path(sys.argv[1] if len(sys.argv) > 1 else ".").resolve()
    root.mkdir(parents=True, exist_ok=True)
    text = lane_registry()
    lines = text.splitlines()
    idx = next(i for i, l in enumerate(lines) if re.match(r"^ {0,3}\|\s*S884\s*\|", l))
    cells = lines[idx].split("|")
    assert len(cells) == 13, "the S884 row must have 11 cells, got %d" % (len(cells) - 2)

    # control: the real registry, byte-identical
    for name, pid, prefix in [("control", None, None)] + PLANTS:
        mirror = root / ("mirror-%s" % name)
        (mirror / "corpus").mkdir(parents=True, exist_ok=True)
        body = list(lines)
        if pid is not None:
            c = list(cells)
            c[1] = " %s " % pid
            c[2] = re.sub(r"https?://[^ |]+", "https://example.invalid/guard-proof/planted-%s.pdf" % pid.lower(), c[2])
            # a clean row: kind paper / tier A / queued / used-by "—", so the ONLY
            # difference between the control and the planted fixtures is the id
            # collision itself (no new census finding is introduced)
            c[3] = " paper "   # kind
            c[4] = " A "   # tier
            c[8] = " queued "   # status
            c[11] = " — "   # used-by
            planted = prefix + "|".join(c)
            assert "example.invalid" in planted, planted[:200]
            body.insert(idx + 1, planted)
        (mirror / "corpus/SOURCES.md").write_text("\n".join(body) + "\n", encoding="utf-8")
        for link in ("knowledge", "lessons"):
            p = mirror / "corpus" / link
            if not p.exists():
                os.symlink(LANE / "corpus" / link, p)
        top = mirror / "SKILL.md"
        if not top.exists():
            os.symlink(LANE / "SKILL.md", top)
        print("%-8s planted=%-6s indent=%d" % (name, pid or "-",
              len(prefix) if prefix is not None else 0))


if __name__ == "__main__":
    main()
