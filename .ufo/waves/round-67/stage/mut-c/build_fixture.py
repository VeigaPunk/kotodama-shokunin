#!/usr/bin/env python3
"""Build the ACCEPT-C-67 mutation harness fixture in a private base clone.

Synthetic data only: it exists to make every accept-c leg reachable so a
single-leg counter mutant can be shown to accept a planted defect. It is NOT
evidence for claim C and never touches the lane repo.
"""
import os
import subprocess
import sys

ENTRY = "corpus/knowledge/culture-material/medicine-healing-codes.md"
TOPIC = ("healing codes of the premodern apothecary as a harness fixture for "
         "ACCEPT-C-67 mutation testing")
IDS = [f"S{n}" for n in range(805, 829)]
QUOTE = "balm resin salve myrrh"
TEACHES = "tincture decoction poultice fumigation plaster cautery"


def row(sid, n, with_capture=True, tier="A"):
    live = f"https://medharness{n:02d}.example.org/item/{n}"
    src = f"Harness source {n:02d} — {live}"
    if with_capture:
        src += f" ; https://web.archive.org/web/20261024{n:02d}0000id_/{live}"
    return (f"| {sid} | {src} | docs | {tier} | synthetic scope {n} | "
            f"\"{QUOTE}\" | {TEACHES} | mined | 2026-10-24 | 180d | {ENTRY} |")


def bullet(sid, n):
    return (f"- Balm, resin, salve: harness teaching line {n} for ({sid}); "
            f"valued by healers beside tincture and decoction.")


def build_entry():
    lines = ["# Medicine healing codes", "",
             f"- topic: {TOPIC}",
             "- sources: harness fixture row set S805-S828", "",
             "## Register", ""]
    for n, sid in enumerate(IDS, 1):
        lines.append(bullet(sid, n))
    lines += ["", "## Notes", "",
              "Synthetic fixture for the frozen counter's mutation probe.", ""]
    return "\n".join(lines)


def main():
    root = os.path.abspath(sys.argv[1] if len(sys.argv) > 1 else "repoc")
    p = lambda *a: os.path.join(root, *a)

    entry_path = p(ENTRY)
    os.makedirs(os.path.dirname(entry_path), exist_ok=True)
    with open(entry_path, "w", encoding="utf-8") as fh:
        fh.write(build_entry())

    reg_path = p("corpus/SOURCES.md")
    with open(reg_path, encoding="utf-8") as fh:
        reg = fh.read()
    assert reg.endswith("\n"), "registry tail assumption"
    reg += "\n" + "\n".join(row(sid, n) for n, sid in enumerate(IDS, 1)) + "\n"
    with open(reg_path, "w", encoding="utf-8") as fh:
        fh.write(reg)

    rd_path = p("corpus/README.md")
    with open(rd_path, encoding="utf-8") as fh:
        rd = fh.read()
    rd = rd.replace("## culture-material/ (33)", "## culture-material/ (34)", 1)
    row_line = f"- `medicine-healing-codes.md` — {TOPIC}\n"
    assert "\n## synthesis/ (29)" in rd
    rd = rd.replace("\n## synthesis/ (29)",
                    "\n" + row_line + "\n## synthesis/ (29)", 1)
    rd = rd.replace("Total knowledge entries: 240.", "Total knowledge entries: 241.", 1)
    old_footer = "(total 240 files; directory totals 30/29/33/29/24/95)."
    new_footer = "(total 241 files; directory totals 30/29/34/29/24/95)."
    assert rd.count(old_footer) >= 1
    rd = rd.replace(old_footer, new_footer, 1)
    with open(rd_path, "w", encoding="utf-8") as fh:
        fh.write(rd)

    subprocess.run(["git", "-C", root, "-c", "user.name=mut-harness",
                    "-c", "user.email=mut@local", "add", "--",
                    ENTRY, "corpus/SOURCES.md", "corpus/README.md"], check=True)
    subprocess.run(["git", "-C", root, "-c", "user.name=mut-harness",
                    "-c", "user.email=mut@local", "commit", "--no-verify",
                    "-m", "mut-c fixture: reachable ACCEPT-C-67 legs"],
                   check=True, stdout=subprocess.DEVNULL)
    rev = subprocess.run(["git", "-C", root, "rev-parse", "main"],
                         capture_output=True, text=True, check=True).stdout.strip()
    print(rev)


if __name__ == "__main__":
    main()
