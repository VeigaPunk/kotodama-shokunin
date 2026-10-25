#!/usr/bin/env python3
"""Build the CORPUS item-10 guard-proof fixtures.

Each fixture is a mirror tree  guard-proof/mirror-<name>/corpus/SOURCES.md  whose
registry is the real lane registry with ONE planted row carrying the staged id
S883 (a member of staged-ids, so the guard must report it as soon as the row
counts as a row at all).  The planted row is a clone of lane row S880 with the id
cell and the URLs swapped, inserted immediately after S880 INSIDE the Registry
table, so the census parser sees it as a Registry row and not as stray text.
corpus/knowledge and corpus/lessons are symlinks to the lane's real dirs so the
census `used-by` existence check resolves exactly as it does on the lane.
"""
import pathlib
import re

HERE = pathlib.Path(__file__).resolve().parent
LANE = pathlib.Path("/home/vgpnk/Projects/shokunin/kotodama-shokunin")
registry = (LANE / "corpus/SOURCES.md").read_text(encoding="utf-8")

lines = registry.splitlines()
idx = next(i for i, l in enumerate(lines) if re.match(r"^ {0,3}\|\s*S880\s*\|", l))
cells = lines[idx].split("|")
cells[1] = " S883 "
cells[2] = cells[2].replace(
    "sanders.phonologist.org/Papers/anderson-etal-cjl-sotl.pdf",
    "example.invalid/guard-proof/planted.pdf",
)
planted = "|".join(cells)
assert "example.invalid" in planted, "planted row did not get the fixture URL"

for name, prefix in (
    ("control", None),
    ("2sp", "  "),
    ("3sp", "   "),
    ("4sp", "    "),
):
    mirror = HERE / f"mirror-{name}"
    (mirror / "corpus").mkdir(parents=True, exist_ok=True)
    body = list(lines)
    if prefix is not None:
        body.insert(idx + 1, prefix + planted)
    (mirror / "corpus/SOURCES.md").write_text("\n".join(body) + "\n", encoding="utf-8")
    for link in ("knowledge", "lessons"):
        p = mirror / "corpus" / link
        if not p.exists():
            p.symlink_to(LANE / "corpus" / link)
    top = mirror / "SKILL.md"          # two rows cite SKILL.md in used-by
    if not top.exists():
        top.symlink_to(LANE / "SKILL.md")
print("mirrors:", sorted(p.name for p in HERE.glob("mirror-*")))
print("planted row:", planted[:150], "...")
