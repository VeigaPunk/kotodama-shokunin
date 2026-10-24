#!/usr/bin/env python3
"""r67 entry-class mutation fixture: build a *valid* claim-C baseline in a
throwaway clone, then emit mutable entry variants.

Never touches the lane. Registry rows are synthetic (fixture hosts), all 24
ids S805-S828, 11 cells, mined/2026-10-24/used-by the entry, capture URL equal
to the live URL. README row/section/totals/footer are advanced by one so the
inherited SWEEP leg is green in the fixture.
"""
import sys

ENTRY = "corpus/knowledge/culture-material/medicine-healing-codes.md"
REGISTRY = "corpus/SOURCES.md"
README = "corpus/README.md"
TOPIC = "fixture entry for mutation probe with 24 mined rows"
NEW_IDS = [f"S{n}" for n in range(805, 829)]


def tok(i, k):
    """Distinct content word per (row, slot): alpha-only, len 8."""
    return f"z{chr(97 + i)}q{chr(97 + k)}vex"


def row(i, sid):
    q = [tok(i, k) for k in range(5)]
    t = [tok(i, k) for k in range(5, 9)]
    live = f"https://host{i}.example.org/doc{i}"
    cap = f"https://web.archive.org/web/20251024{i + 1:06d}id_/{live}"
    claim = f"fixture claim {i} about material practice and workshop evidence"
    quote = f'"{q[0].capitalize()} {q[1]} {q[2]} {q[3]} {q[4]}."'
    teaches = (f"Paraphrase marker {t[0]} {t[1]} {t[2]} {t[3]} contextual "
               f"reading of the fixture source.")
    cells = [sid, f"Fixture source {i}, {live} ; {cap} .", "paper", "A", claim,
             quote, teaches, "mined", "2026-10-24", "180d", ENTRY]
    return "| " + " | ".join(cells) + " |"


def bullet(i, sid):
    q = [tok(i, k) for k in range(3)]
    return (f"- {q[0]} {q[1]} {q[2]} workshop notes and drawing conventions "
            f"({sid})")


def baseline_entry():
    out = ["# Fixture entry for mutation probe",
           "",
           f"- topic: {TOPIC}",
           "- sources: fixture registry rows S805-S828",
           "- verified-at: 2026-10-24",
           "- recheck: 180 days",
           ""]
    for s in range(4):
        out.append(f"## {s + 1}. Fixture section {s + 1}")
        out.append("")
        for i in range(s * 6, s * 6 + 6):
            out.append(bullet(i, NEW_IDS[i]))
        out.append("")
    return "\n".join(out).rstrip("\n") + "\n"


def apply_baseline(root):
    import re
    with open(f"{root}/{REGISTRY}", "a", encoding="utf-8") as fh:
        fh.write("\n" + "\n".join(row(i, sid) for i, sid in enumerate(NEW_IDS)) + "\n")
    with open(f"{root}/{ENTRY}", "w", encoding="utf-8") as fh:
        fh.write(baseline_entry())
    with open(f"{root}/{README}", encoding="utf-8") as fh:
        r = fh.read()
    assert "## culture-material/ (33)" in r
    r = r.replace("## culture-material/ (33)", "## culture-material/ (34)", 1)
    nxt = r.index("## synthesis/")
    rowline = f"- `medicine-healing-codes.md` — {TOPIC}\n"
    assert "medicine-healing-codes.md" not in r
    r = r[:nxt] + rowline + "\n" + r[nxt:]
    assert "Total knowledge entries: 240." in r
    r = r.replace("Total knowledge entries: 240.", "Total knowledge entries: 241.", 1)
    r = r.replace("(total 240 files; directory totals 30/29/33/29/24/95).",
                  "(total 241 files; directory totals 30/29/34/29/24/95).", 1)
    with open(f"{root}/{README}", "w", encoding="utf-8") as fh:
        fh.write(r)


MUTANTS = {}


def mutant(name):
    def deco(fn):
        MUTANTS[name] = fn
        return fn
    return deco


@mutant("M1-notopic")
def m1(text):
    return "\n".join(l for l in text.splitlines() if not l.startswith("- topic:")) + "\n"


@mutant("M2-h3")
def m2(text):
    return text.replace("## 1. Fixture section 1",
                        "### 1a. Unwanted heading\n\n## 1. Fixture section 1", 1)


@mutant("M3-251lines")
def m3(text):
    return text + "".join(f"filler line {n}\n" for n in range(251 - len(text.splitlines())))


@mutant("M4-foreign-paren")
def m4(text):
    return text.replace("(S805)", "(S805) (S099)", 1)


@mutant("M5-foreign-bare")
def m5(text):
    # attack: same foreign citation, no parentheses -> outside ONEID's regex
    return text.replace("(S805)", "(S805), see S099", 1)


@mutant("M6-dup-paren")
def m6(text):
    return text.replace("(S805)", "(S805) (S805)", 1)


@mutant("M7-drop-bullet")
def m7(text):
    return "\n".join(l for l in text.splitlines() if "(S828)" not in l) + "\n"


@mutant("M8-swap-bullets")
def m8(text):
    lines = text.splitlines()
    i5 = next(n for n, l in enumerate(lines) if "(S805)" in l)
    i6 = next(n for n, l in enumerate(lines) if "(S806)" in l)
    assert lines[i5] == bullet(0, "S805"), lines[i5]
    assert lines[i6] == bullet(1, "S806"), lines[i6]
    lines[i5], lines[i6] = bullet(1, "S805"), bullet(0, "S806")
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    root = sys.argv[1]
    if len(sys.argv) == 2:
        apply_baseline(root)
        print(baseline_entry())
    else:
        name = sys.argv[2]
        with open(f"{root}/{ENTRY}", encoding="utf-8") as fh:
            text = fh.read()
        out = MUTANTS[name](text)
        with open(f"{root}/{ENTRY}", "w", encoding="utf-8") as fh:
            fh.write(out)
        print(f"applied {name}: lines={len(out.splitlines())}")
