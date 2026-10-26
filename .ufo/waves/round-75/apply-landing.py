#!/usr/bin/env python3
"""Round-75 landing edits applied to a worktree root.
Usage: apply-landing.py <root> ca | c | c-census <census-end.txt> | axes <ca-lands> <c-lands>
Sources: the real lane's .ufo/waves/round-75/w2/stage (never the root's copy)."""
import re, sys, shutil, os
LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
ST = LANE + "/.ufo/waves/round-75/w2/stage"
root, which = sys.argv[1], sys.argv[2]

def rd(p): return open(p, encoding="utf-8").read()
def wr(p, t):
    os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, "w", encoding="utf-8").write(t)
def cp(rel_stage, rel_root):
    os.makedirs(os.path.dirname(f"{root}/{rel_root}"), exist_ok=True)
    shutil.copyfile(f"{ST}/{rel_stage}", f"{root}/{rel_root}")

def readme_ca():
    p = f"{root}/corpus/README.md"; t = rd(p).split("\n")
    recs = re.findall(r"(?ms)^(LINE-REPLACE|INSERT-AFTER)\n(.*?)\nEND$", rd(f"{ST}/corpus/README.md.ca-edits"))
    for kind, payload in recs:
        lines = payload.split("\n")
        if kind == "LINE-REPLACE":
            k = lines.index("==>"); old, new = "\n".join(lines[:k]), "\n".join(lines[k + 1:])
            assert t.count(old) == 1, old
            t[t.index(old)] = new
        else:
            anchor, rows = lines[0], lines[1:]
            hit = [i for i, l in enumerate(t) if l.startswith(anchor)]
            assert len(hit) == 1, (anchor, hit)
            t[hit[0] + 1:hit[0] + 1] = rows
    wr(p, "\n".join(t))

def lesson_split():
    t = rd(f"{ST}/corpus/lessons/round-75.md")
    i = t.index("\n## Gate\n"); j = t.index("\n## Corrections\n")
    return t[:i], t[i:j], t[j:]   # head, middle (C sections), corrections (Ca)

if which == "ca":
    # SKILL.md line 701 + gate rows
    s = rd(f"{root}/SKILL.md")
    sk = rd(f"{ST}/SKILL.md.ca-edits.md")
    old701 = re.search(r"<!-- OLD-701 -->\n(.*?)\n<!-- /OLD-701 -->", sk, re.S).group(1)
    new701 = re.search(r"<!-- NEW-701 -->\n(.*?)\n<!-- /NEW-701 -->", sk, re.S).group(1)
    assert s.count(old701) == 1; s = s.replace(old701, new701)
    rows = [l for l in rd(f"{LANE}/.ufo/waves/round-75/skill-rows.md").split("\n") if l.startswith("| accept-c")]
    assert len(rows) == 2, len(rows)
    lines = s.split("\n")
    idx = [i for i, l in enumerate(lines) if l.startswith("| accept-ca-74 |")]
    assert len(idx) == 1
    lines[idx[0] + 1:idx[0] + 1] = rows
    wr(f"{root}/SKILL.md", "\n".join(lines))
    # QUALITY append
    q = rd(f"{root}/corpus/QUALITY.md")
    if not q.endswith("\n"): q += "\n"
    wr(f"{root}/corpus/QUALITY.md", q + rd(f"{ST}/corpus/QUALITY.md.append"))
    # SCORECARD corrections append
    sc = rd(f"{root}/SCORECARD.md")
    if not sc.endswith("\n"): sc += "\n"
    wr(f"{root}/SCORECARD.md", sc + rd(f"{ST}/SCORECARD.md.append"))
    readme_ca()
    if os.path.abspath(root) != LANE:
        shutil.copyfile(f"{LANE}/SHONEN.md", f"{root}/SHONEN.md")
        shutil.copyfile(f"{LANE}/reports/round-28/readme/sweep.py", f"{root}/reports/round-28/readme/sweep.py")
    head, _mid, corr = lesson_split()
    wr(f"{root}/corpus/lessons/round-75.md", head + corr)
    for n in ("selftest-r72-repeat.txt", "sweep-base.txt", "sweep-fixed-at-base.txt", "sweep-fixed-after-ca.txt", "accept-ca-74-at-lands.txt"):
        cp(f"reports/round-75/telemetry/{n}", f"reports/round-75/telemetry/{n}")
    print("ca applied")
elif which == "c":
    d = "corpus/knowledge/myth-symbol/"
    for n in sorted(os.listdir(f"{ST}/{d}")):
        cp(d + n, d + n)
    # registry rows after S884
    p = f"{root}/corpus/SOURCES.md"; t = rd(p).split("\n")
    rows = rd(f"{ST}/corpus/SOURCES.rows").rstrip("\n").split("\n")
    idx = max(i for i, l in enumerate(t) if re.match(r"^ {0,3}\|\s*S884\s*\|", l))
    t[idx + 1:idx + 1] = rows
    wr(p, "\n".join(t))
    # README: three rows at the end of the myth-symbol section, heading, footer
    p = f"{root}/corpus/README.md"; t = rd(p)
    assert t.count("## myth-symbol/ (29)") == 1; t = t.replace("## myth-symbol/ (29)", "## myth-symbol/ (32)")
    crows = rd(f"{ST}/corpus/README.md.c-rows").rstrip("\n")
    k = t.index("\n## culture-material/ (")
    sect = t[:k].rstrip("\n")
    t = sect + "\n" + crows + "\n" + t[k:]
    if not t.endswith("\n"): t += "\n"
    t += rd(f"{ST}/corpus/README.md.c-footer")
    wr(p, t)
    # lesson: C sections go in front of Corrections
    head, mid, corr = lesson_split()
    wr(f"{root}/corpus/lessons/round-75.md", head + mid + corr)
    for n in sorted(os.listdir(f"{ST}/reports/round-75/evidence")):
        cp(f"reports/round-75/evidence/{n}", f"reports/round-75/evidence/{n}")
    print("c applied")
elif which == "c-census":
    census = rd(sys.argv[3]).rstrip("\n")
    p = f"{root}/corpus/lessons/round-75.md"; t = rd(p)
    ph = "CENSUS-END: <filled by the L1 at landing>"
    assert t.count(ph) == 1
    wr(p, t.replace(ph, census))
    print("census filled")
elif which == "axes":
    ca, c = sys.argv[3], sys.argv[4]
    a = rd(f"{ST}/SCORECARD.round75-claims.append")
    assert a.count("<filled by the L1>") >= 1
    a = a.replace("LANDS: <filled by the L1>", f"LANDS: Ca {ca} ; C {c}")
    sc = rd(f"{root}/SCORECARD.md")
    if not sc.endswith("\n"): sc += "\n"
    wr(f"{root}/SCORECARD.md", sc + a)
    print("axes appended")
