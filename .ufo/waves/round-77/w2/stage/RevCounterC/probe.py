#!/usr/bin/env python3
"""RevCounterC falsification probes against staged accept-c.py.

Reuses the counter's own _st_build/_st_run fixture machinery, then applies
extra mutations on top of a clean landing to test ROWS-scope, INDEX,
FROZENCFG and COLLCHECK edge cases the selftest does not cover.
"""
import importlib.util
import json
import os
import subprocess
import sys

AC_PATH = "/fast/scratch/hyaku/kotodama-r77/RevCounterC/accept-c.py"
SEAT = "/fast/scratch/hyaku/kotodama-r77/RevCounterC"
CASES = os.path.join(SEAT, "cases")
WORK = os.path.join(SEAT, "work")

spec = importlib.util.spec_from_file_location("ac", AC_PATH)
ac = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ac)

REG = "corpus/SOURCES.md"
README = "corpus/README.md"
CLAIMS = "reports/round-77/claims.json"


def sh(*a, cwd=None):
    r = subprocess.run(list(a), capture_output=True, text=True, cwd=cwd)
    return r


def g(d, *a):
    return ac._st_git(d, *a)


def read(p):
    with open(p, encoding="utf-8") as fh:
        return fh.read()


def write(p, text):
    with open(p, "w", encoding="utf-8") as fh:
        fh.write(text)


def recommit(paths, msg):
    """Commit current worktree state of the fixture lane as a new lands."""
    new = ac._st_commit(paths["root"], msg)
    paths = dict(paths)
    paths["lands"] = new
    return paths


def build(name, mut=None, claims_patch=None):
    d = os.path.join(CASES, name)
    os.makedirs(d, exist_ok=True)
    if claims_patch:
        orig = ac._st_claims
        def patched(base, map_sha, m):
            doc = orig(base, map_sha, m)
            claims_patch(doc)
            return doc
        ac._st_claims = patched
        try:
            paths = ac._st_build(d, mut or {})
        finally:
            ac._st_claims = orig
    else:
        paths = ac._st_build(d, mut or {})
    return paths


def run(paths, tag):
    code, legs, verdict, out, err = ac._st_run(paths, os.path.join(WORK, tag))
    fails = sorted(n for n, v in legs.items() if v == "FAIL")
    return {"exit": code, "fail_legs": fails, "verdict": verdict,
            "stderr": err.strip()[:300]}


def show(name, res):
    print("PROBE %-34s exit=%d fails=%s" %
          (name, res["exit"], ",".join(res["fail_legs"]) or "-"))
    print("      verdict: %s" % res["verdict"])
    if res["stderr"]:
        print("      stderr: %s" % res["stderr"].splitlines()[0])


def main():
    os.makedirs(CASES, exist_ok=True)
    os.makedirs(WORK, exist_ok=True)
    results = {}

    # P0 clean control -------------------------------------------------------
    paths = build("clean")
    res = run(paths, "clean")
    show("P0-clean", res)
    results["P0-clean"] = res
    base_registry = read(os.path.join(paths["root"], REG))
    base_readme = read(os.path.join(paths["root"], README))

    # P1: verbatim duplicate of a BASE row appended inside ## Registry -------
    p = build("dup-verbatim")
    reg = read(os.path.join(p["root"], REG))
    s002 = [l for l in reg.splitlines() if l.startswith("| S002 ")][0]
    # inject the twin right after the last row (still inside ## Registry,
    # before the ## Paths heading)
    reg2 = reg.replace("\n\n## Paths", "\n" + s002 + "\n\n## Paths", 1)
    write(os.path.join(p["root"], REG), reg2)
    p = recommit(p, "dup base row verbatim")
    res = run(p, "dup-verbatim")
    show("P1-dup-base-row-verbatim", res)
    results["P1-dup-base-row-verbatim"] = res

    # P2: same-id duplicate with DIFFERENT cells, corrupt twin FIRST ----------
    p = build("dup-shadow")
    reg = read(os.path.join(p["root"], REG))
    s002 = [l for l in reg.splitlines() if l.startswith("| S002 ")][0]
    shadow = ("| S002 | SHADOW ROW — https://example.org/shadow "
              "| junk | Z | shadow | shadow | shadow | queued | "
              "1999-01-01 | daily | — |")
    reg2 = reg.replace(s002, shadow + "\n" + s002, 1)
    write(os.path.join(p["root"], REG), reg2)
    p = recommit(p, "shadow dup row first")
    res = run(p, "dup-shadow")
    show("P2-dup-id-diff-content", res)
    results["P2-dup-id-diff-content"] = res

    # P3: delete non-row registry lines (## Search log heading + base note) --
    p = build("del-nonrow")
    reg = read(os.path.join(p["root"], REG))
    reg2 = reg.replace("## Search log\n\n(base searches recorded by earlier "
                       "rounds)\n", "")
    assert reg2 != reg
    write(os.path.join(p["root"], REG), reg2)
    p = recommit(p, "delete non-row lines")
    res = run(p, "del-nonrow")
    show("P3-delete-non-row-lines", res)
    results["P3-delete-non-row-lines"] = res

    # P3b: delete the REQUIRED search-log line -> INDEX must fail ------------
    p = build("del-required")
    reg = read(os.path.join(p["root"], REG))
    reg2 = "\n".join(l for l in reg.splitlines()
                     if "round 77" not in l)
    write(os.path.join(p["root"], REG), reg2)
    p = recommit(p, "delete required search-log line")
    res = run(p, "del-required")
    show("P3b-delete-required-line", res)
    results["P3b-delete-required-line"] = res

    # P4: freeze claims.json with NO `frozen` stamp key -----------------------
    def strip_frozen(doc):
        doc.pop("frozen", None)
    p = build("no-frozen-stamp", claims_patch=strip_frozen)
    res = run(p, "no-frozen-stamp")
    show("P4-frozen-stamp-absent", res)
    results["P4-frozen-stamp-absent"] = res

    # P4b: frozen legs reordered -> LEGCOUNT refusal expected -----------------
    def reorder_legs(doc):
        doc["claims"][0]["legs"] = list(reversed(doc["claims"][0]["legs"]))
    p = build("legs-reorder", claims_patch=reorder_legs)
    res = run(p, "legs-reorder")
    show("P4b-frozen-legs-reordered", res)
    results["P4b-frozen-legs-reordered"] = res

    # P4c: frozen legs renamed (STAMP instead of INDEX) -> refuse -------------
    def rename_legs(doc):
        legs = doc["claims"][0]["legs"]
        doc["claims"][0]["legs"] = ["STAMP" if l == "INDEX" else l
                                    for l in legs]
    p = build("legs-rename", claims_patch=rename_legs)
    res = run(p, "legs-rename")
    show("P4c-frozen-legs-renamed", res)
    results["P4c-frozen-legs-renamed"] = res

    # P5: required_sections lines present but under the WRONG headings -------
    p = build("misplaced")
    reg = read(os.path.join(p["root"], REG))
    lines = reg.splitlines()
    bullet = [l for l in lines if l.startswith("- naming-system design")][0]
    search = [l for l in lines if l.startswith("**Chinese naming-system")][0]
    reg2 = "\n".join(l for l in lines
                     if l not in (bullet, search))
    # re-add them in wrong sections: the Paths bullet inside ## Registry
    # (just before the ## Paths heading), the search-log entry inside ## Paths
    reg2 = reg2.replace("\n## Paths", "\n" + bullet + "\n\n## Paths", 1)
    reg2 = reg2.replace("(base paths recorded by earlier rounds)",
                        "(base paths recorded by earlier rounds)\n" + search, 1)
    write(os.path.join(p["root"], REG), reg2 + "\n")
    p = recommit(p, "misplaced required lines")
    res = run(p, "misplaced")
    show("P5-required-lines-wrong-section", res)
    results["P5-required-lines-wrong-section"] = res

    # P6a: fabricated README index row for a BASE file (no fake heading) -----
    p = build("fake-index-a")
    rd = read(os.path.join(p["root"], README))
    rd2 = rd.replace("- `sample.md` — Fixture sample symbol entry.",
                     "- `sample.md` — Fixture sample symbol entry.\n"
                     "- `sample.md` — FABRICATED duplicate index row.", 1)
    write(os.path.join(p["root"], README), rd2)
    p = recommit(p, "fabricated index row only")
    res = run(p, "fake-index-a")
    show("P6a-fabricated-index-row-only", res)
    results["P6a-fabricated-index-row-only"] = res

    # P6b: fabricated row + fabricated duplicate section heading -------------
    p = build("fake-index")
    rd = read(os.path.join(p["root"], README))
    rd2 = rd.rstrip("\n") + (
        "\n- `sample.md` — FABRICATED duplicate index row.\n"
        "\n## linguistics/ (2)\n\n- `sample.md` — second fabricated row.\n")
    write(os.path.join(p["root"], README), rd2)
    p = recommit(p, "fabricated index rows")
    res = run(p, "fake-index")
    show("P6b-fabricated-index-row+heading", res)
    results["P6b-fabricated-index-row+heading"] = res

    # P7: lands branched from BASE, not descending the freeze ----------------
    p = build("off-base")
    g(p["root"], "checkout", "-q", "-b", "probe", p["base"])
    g(p["root"], "checkout", "-q", p["lands"], "--", ".")
    new = ac._st_commit(p["root"], "lands off base")
    p["lands"] = new
    res = run(p, "off-base")
    show("P7-lands-not-descending-freeze", res)
    results["P7-lands-not-descending-freeze"] = res

    # P8: extra unrelated URL in a new row's source cell ----------------------
    p = build("extra-url")
    reg = read(os.path.join(p["root"], REG))
    s004 = [l for l in reg.splitlines() if l.startswith("| S004 ")][0]
    reg2 = reg.replace(
        s004,
        s004.replace("at https://web.archive.org",
                     "; also https://unrelated.example.net/page "
                     "at https://web.archive.org"), 1)
    write(os.path.join(p["root"], REG), reg2)
    p = recommit(p, "extra url in source cell")
    res = run(p, "extra-url")
    show("P8-extra-url-source-cell", res)
    results["P8-extra-url-source-cell"] = res

    # P9: non-S junk row line inside ## Registry ------------------------------
    p = build("junk-row")
    reg = read(os.path.join(p["root"], REG))
    junk = "| T001 | junk row — https://example.org/junk | docs | A | j | j " \
           "| j | queued | 2026-10-27 | 90d | — |"
    reg2 = reg.replace("\n\n## Paths", "\n" + junk + "\n\n## Paths", 1)
    write(os.path.join(p["root"], REG), reg2)
    p = recommit(p, "junk non-S row")
    res = run(p, "junk-row")
    show("P9-junk-non-S-row", res)
    results["P9-junk-non-S-row"] = res

    # P10: lands == freeze where freeze CONTAINS the landing ------------------
    # build fixture, then create a single commit holding claims+landing
    d = os.path.join(CASES, "samecommit")
    os.makedirs(d, exist_ok=True)
    lane = os.path.join(d, "lane")
    os.makedirs(lane)
    g(lane, "init", "-q")
    ac._st_write(lane, REG, ac._st_base_registry())
    ac._st_write(lane, README, ac._st_readme(2, [1, 1]))
    ac._st_write(lane, "corpus/knowledge/linguistics/naming-systems.md",
                 ac._FX_BASE_ENTRY)
    ac._st_write(lane, "corpus/knowledge/myth-symbol/sample.md",
                 ac._FX_BASE_SAMPLE)
    ac._st_write(lane, "tools/check-cited-lines.py", ac._st_cited_tool(),
                 mode=0o755)
    ac._st_write(lane, ac.BASE_LESSON,
                 "# Round 76 — fixture lesson\n\n## Gate\n\n(none)\n")
    base = ac._st_commit(lane, "base")
    map_text = ac._st_map_text({})
    map_sha = ac.hashlib.sha256(map_text.encode("utf-8")).hexdigest()
    ac._st_write(lane, ac.ASSIM + "/id-renumber-map.json", map_text)
    claims = ac._st_claims(base, map_sha, {})
    ac._st_write(lane, CLAIMS, json.dumps(claims, indent=2) + "\n")
    ac._st_assim_files(lane, {})
    ac._st_write(lane, ac.TELEMETRY + "/census-start.txt",
                 "sources-census.sh validate --root . kotodama\nrows 3\n"
                 "exit 0\n")
    ac._st_write(lane, ac.TELEMETRY + "/gap-sweep.txt",
                 "gap sweep %s: 單名與雙名 and Flowers, Plants, and Trees "
                 "absent at base\nexit 0\n" % ac._FX_ACCESS)
    freeze = ac._st_commit(lane, "freeze")
    fleet = ac._st_census_stub(os.path.join(d, "fleet"), red=False)
    ac._st_landing_files(lane, freeze, {})
    lands = ac._st_commit(lane, "lands")
    # rewrite history: a single commit off base holding freeze+landing content
    g(lane, "checkout", "-q", "-b", "squashed", base)
    g(lane, "checkout", "-q", lands, "--", ".")
    squashed = ac._st_commit(lane, "squashed freeze+landing")
    p = {"root": lane, "base": base, "freeze": squashed,
         "lands": squashed, "fleet": fleet}
    res = run(p, "samecommit")
    show("P10-lands-eq-freeze-full-landing", res)
    results["P10-lands-eq-freeze-full-landing"] = res

    # P11: repointed source line carrying ONLY the archive URL ---------------
    p = build("archive-only")
    entry = read(os.path.join(p["root"], ac._FX_ENTRY))
    entry2 = entry.replace("https://example.org/docs/beta",
                           ac._archive_for("https://example.org/docs/beta"), 1)
    write(os.path.join(p["root"], ac._FX_ENTRY), entry2)
    p = recommit(p, "archive-only source line")
    res = run(p, "archive-only")
    show("P11-archive-only-source-line", res)
    results["P11-archive-only-source-line"] = res

    with open(os.path.join(SEAT, "probe-results.json"), "w") as fh:
        json.dump(results, fh, indent=1)


if __name__ == "__main__":
    main()
