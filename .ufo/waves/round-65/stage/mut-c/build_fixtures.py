#!/usr/bin/env python3
"""Build the six per-mutant land-state fixtures for seat MutCounterC (round 65).

Each fixture is a minimal root accepted by reports/round-65/accept-c.py revision 2
(sha 8f44b649...) with the fake-git layer supplied by harness.py.  Modes:

  clean  : honest landed tree (baseline: original PASS, every mutant PASS)
  m1     : S762 clause is a trailing-word teaches near-copy (cov 0.90)
  m3     : S751/S752 live URLs differ only in query, captures carry the query
  m4     : S750 cited twice and S775 never cited (26 cited lines)
  m5     : pinned base already carries a valid S750 row; only 25 rows appended
  m6     : S765/S770/S775 rows exist but the locator cannot reopen them

Writes stay under .ufo/waves/round-65/stage/mut-c/.
"""
import pathlib
import shutil

STAGE = pathlib.Path(__file__).resolve().parent
ENTRY = "corpus/knowledge/culture-material/games-play-sport-contests.md"
BASE_LINES = (STAGE / "base-sources.md").read_text().splitlines()
TOPIC = "fixture games play sport contests"


def sid_for(i):
    return f"S{750 + i}"


def generic(i):
    L = chr(97 + i)
    cw = [f"zephyr{L}", f"meadow{L}", f"lantern{L}", f"granite{L}", f"whistle{L}"]
    clause = " ".join(cw)
    quote = f"{cw[0]} and {cw[1]} with {cw[2]} near {cw[3]} from distant lands"
    teaches = f"throw{L} catch{L} relay{L} sprint{L} baton{L}"
    return clause, quote, teaches


NEAR_CLAUSE = "rolling hoop chasing game with wooden sticks and rope zephyr"
NEAR_QUOTE = "rolling hoop chasing game with wooden sticks and rope across the courtyard"
NEAR_TEACHES = "rolling hoop chasing game with wooden sticks and rope"

TWIN_URLS = {1: "https://twin.test/ref?ed=1", 2: "https://twin.test/ref?ed=2"}


def row_line(sid, source, quote, teaches):
    return (f'| {sid} | {source} | web | B | fixture scope | "{quote}" | {teaches} '
            f"| mined | 2026-10-24 | 180d | {ENTRY} |")


def source_for(i, sid, mode):
    if mode == "m3" and i in TWIN_URLS:
        live = TWIN_URLS[i]
        cap = f"https://web.archive.org/web/20240101{i:06d}id_/{live}"
        return f"{live} capture {cap}"
    live = f"https://fixture{i}.test/ref/{sid}?ed=1"
    cap = f"https://web.archive.org/web/20240101{i:06d}id_/{live}"
    return f"{live} capture {cap}"


def build(mode, root):
    if root.exists():
        shutil.rmtree(root)
    for d in ("corpus/knowledge/culture-material", "corpus", "tools",
              "reports/round-28/readme", "reports/round-61"):
        (root / d).mkdir(parents=True, exist_ok=True)

    rows, bullets = [], []
    for i in range(26):
        sid = sid_for(i)
        if mode in ("m1", "m2") and sid == "S762":
            clause, quote, teaches = NEAR_CLAUSE, NEAR_QUOTE, NEAR_TEACHES
        else:
            clause, quote, teaches = generic(i)
        rows.append(row_line(sid, source_for(i, sid, mode), quote, teaches))
        bullets.append(f"- {clause} ({sid})")

    if mode == "m4":
        # S750 cited twice (identical honest restatements), S775 never cited.
        bullets = [b for b in bullets if not b.endswith("(S775)")]
        bullets.append(f"- {generic(0)[0]} (S750)")
        assert len(bullets) == 26

    entry = (f"# Games, play, sport, contests\n\n- topic: {TOPIC}\n\n## Terms\n\n"
             + "\n".join(bullets)
             + "\n\n## Notes\n\n- fixture lore handoff line for the acceptance counter.\n")
    (root / ENTRY).write_text(entry)

    head_rows = rows
    head = "\n".join(BASE_LINES + ([] if mode == "red" else head_rows)) + "\n"
    (root / "corpus/SOURCES.md").write_text(head)

    if mode == "m5":
        base5 = STAGE / "fixtures/m5-base-SOURCES.md"
        base5.write_text("\n".join(BASE_LINES + [rows[0]]) + "\n")
    if mode != "red":
        (root / "corpus/README.md").write_text(
            f"- `games-play-sport-contests.md` — {TOPIC}\n")

    (root / "tools/check-cited-lines.py").write_text(
        'import sys\nprint("0 findings")\nsys.exit(0)\n')
    (root / "reports/round-28/readme/sweep.py").write_text(
        "import sys\nsys.exit(0)\n")
    allow = "{'S750', 'S755', 'S760'}" if mode == "m6" else "{'S750', 'S755', 'S760', 'S765', 'S770', 'S775'}"
    (root / "reports/round-61/reopen-quote.py").write_text(
        "import sys\n"
        f"ALLOW = {allow}\n"
        "row = sys.argv[sys.argv.index('--row') + 1] if '--row' in sys.argv else ''\n"
        "if row in ALLOW:\n"
        "    print(f'LOCATED {row} fixture')\n"
        "    sys.exit(0)\n"
        "print(f'NOT_LOCATED {row} fixture')\n"
        "sys.exit(1)\n")
    if mode == "red":
        (root / "corpus/knowledge/culture-material/games-play-sport-contests.md").unlink()
        (root / "reports/round-61/reopen-quote.py").write_text(
            "import sys\nprint('NOT_LOCATED red fixture')\nsys.exit(1)\n")


if __name__ == "__main__":
    for mode in ("clean", "m1", "m3", "m4", "m5", "m6", "red"):
        build(mode, STAGE / "fixtures" / mode)
        print(f"built {mode}")
