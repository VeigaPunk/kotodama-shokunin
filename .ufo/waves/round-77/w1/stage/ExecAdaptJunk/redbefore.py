#!/usr/bin/env python3
"""Measure the round-76 counter's verdict on the classes round-77's fixtures
name.  Read-only outside the mktemp fixture clones; stdlib only.

Every measurement is one fixture commit in a private clone of the lane at the
round-76 base (`git clone --shared`), graded with the round-76 counters and
recorded with the exact argv, exit code and LEG lines.
"""
import importlib.util
import json
import os
import re
import shutil
import subprocess
import sys

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
FLEET = "/home/vgpnk/Projects/shokunin"
WORK = "/fast/scratch/hyaku/kotodama-r77/ExecAdaptJunk/redbefore-work"
R76 = os.path.join(LANE, "reports/round-76")
JUNK76 = os.path.join(R76, "counters/junk-fixtures.py")
C76 = os.path.join(R76, "accept-c.py")
CA76 = os.path.join(R76, "accept-ca.py")
FREEZE = "df0f0309d61e5485bb17035d3f8791b1e6a11d40"
CA_LANDS = "a43ed807ea38b5fc5a7875a839d576cea73aba7c"
C_LANDS = "c792ea50f1cfba2b56c16a0f5102b2877fd2eefd"
LEDGER = "reports/round-76/ledger.json"

spec = importlib.util.spec_from_file_location("jf76", JUNK76)
jf = importlib.util.module_from_spec(spec)
sys.modules["jf76"] = jf
spec.loader.exec_module(jf)


def git(repo, *args):
    return jf.git(repo, *args)


def fresh(label, ref):
    d, repo = jf.clone_lane(WORK, label)
    git(repo, "checkout", "-q", "-B", "main", ref)
    git(repo, "read-tree", "-u", "--reset", ref)
    git(repo, "checkout", "-q", "main")
    return d, repo


def grade(repo, claim, rev, freeze, work):
    if claim == "C":
        cmd = [sys.executable, "-B", C76, "--root", repo, "--lands", rev,
               "--freeze", freeze, "--fleet-root", FLEET, "--work", work]
    else:
        cmd = [sys.executable, "-B", CA76, "--root", repo, "--lands", rev,
               "--freeze", freeze, "--fleet-root", FLEET,
               "--combined", rev, "--main", rev, "--work", work]
    r = subprocess.run(cmd, cwd=repo, capture_output=True, text=True,
                       timeout=1800)
    out = r.stdout + ("\n" + r.stderr if r.stderr.strip() else "")
    return {"cmd": " ".join(cmd), "exit": r.returncode, "out": out,
            "legs": jf.leg_table(r.stdout),
            "verdict": [l for l in r.stdout.splitlines()
                        if l.startswith("ACCEPT-")]}


def block(name, r77_class, res, fixture_note, lands, freeze, changed=""):
    legs = res["legs"]
    red = sorted(n for n, ok in legs.items() if not ok)
    raw = res["out"].splitlines()
    keep = []
    for i, l in enumerate(raw):
        if l.startswith("LEG ") and any(l.split()[2] == x
                                        for x in _watch(name)):
            keep.append(l)
            j = i + 1
            while j < len(raw) and raw[j].startswith("     "):
                keep.append(raw[j])
                j += 1
    return "\n".join([
        "### %s  ->  %s" % (name, r77_class),
        "# fixture: %s" % fixture_note,
        "# freeze: %s" % freeze,
        "# lands: %s" % lands,
        "# changed: %s" % (changed or "(none)"),
        "# counter: %s" % res["cmd"],
        "# exit: %d" % res["exit"],
        "# verdict: %s" % (res["verdict"][-1] if res["verdict"] else "(none)"),
        "# red-legs: %s" % (", ".join(red) or "(none)"),
        ] + [l if len(l) < 2000 else l[:2000] + " …" for l in keep])


def _watch(name):
    return {
        "J1": ("ENTRIES",), "J2": ("EVIDENCE", "GATE"), "J3": ("FROZENCFG",),
        "J4": ("LEDGER",), "J4b": ("LEDGER",), "J5": ("ANNOTATE", "NOSTUB"),
        "J6": ("APPENDONLY",), "J7": ("SEPARABLE",), "J8": ("LEDGER",),
        "J9": ("LEDGER",), "J10": ("LEDGER",), "J11": ("ROWS",),
    }[name]


def ledger_clean(drop=(), fix_stated_text=False):
    doc = json.loads(git(LANE, "show", "%s:%s" % (FREEZE, LEDGER)))
    pairs = [p for p in doc["pairs"] if p["id"] not in drop]
    if fix_stated_text:
        for p in pairs:
            if p["id"] == "L76-19":
                p["stated_text"] = "(`chars=4097 before=284`)"
    doc["pairs"] = pairs
    return doc


def commit_own_freeze(repo, doc, label, mutate=None, ref=FREEZE):
    jf.write_json(repo, LEDGER, doc)
    if mutate:
        mutate(repo)
    fz = jf.commit_all(repo, "r76-class %s: defective freeze" % label)
    lands = jf.commit_all(repo, "r76-class %s: empty landing" % label,
                          allow_empty=True)
    changed = tuple(git(repo, "diff", "--name-only", ref, fz).split())
    return fz, lands, changed


def measure_own_freeze(name, r77_class, label, doc, mutate=None, claim="Ca",
                       note=""):
    d, repo = fresh(label, FREEZE)
    try:
        fz, lands, changed = commit_own_freeze(repo, doc, label, mutate)
        res = grade(repo, claim, lands, fz, os.path.dirname(d))
        return block(name, r77_class, res, note or label, lands, fz,
                     ", ".join(changed))
    finally:
        shutil.rmtree(d, ignore_errors=True)


def measure_r76_fixture(name, r76name, claim, reference):
    fx = jf.build(r76name, FREEZE, reference, None, WORK)
    res = grade(fx.repo, claim, fx.rev, fx.freeze, os.path.dirname(fx.repo))
    return block(name, "r76 fixture %s" % r76name, res,
                 fx.detail, fx.rev, fx.freeze, ", ".join(fx.paths)), fx


def main():
    os.makedirs(WORK, exist_ok=True)
    out = ["# red-before: the round-76 counter's verdict on the round-77 "
           "fixture classes",
           "# lane base for r77: 211f9526; round-76 freeze %s" % FREEZE,
           "# round-76 Ca lands %s ; round-76 C lands %s" % (CA_LANDS, C_LANDS),
           ""]

    # --- J1: one header-only stub entry on the r76 C landing ---------------
    try:
        d, repo = fresh("stub", C_LANDS)
        claims = json.loads(git(LANE, "show", "%s:reports/round-76/claims.json"
                               % FREEZE))
        claim = [c for c in claims["claims"] if c["id"].upper() == "C"][0]
        path = claim["entries"][0]
        rid = claim["row_set"][0]["id"]
        doc = claim["row_set"][0].get("document") or "https://example.invalid/x"
        jf._stub_entry(repo, path, rid, doc)
        cols = jf.registry_columns(repo)
        text = jf.read(repo, "corpus/SOURCES.md")
        out_lines = []
        for line in text.splitlines(keepends=True):
            m = jf.ROW_RE.match(line)
            if m and m.group(1) == rid:
                line = jf.set_cell(line.rstrip("\n"), cols["used-by"],
                                   path) + "\n"
            out_lines.append(line)
        jf.write(repo, "corpus/SOURCES.md", "".join(out_lines))
        rev = jf.commit_all(repo, "r76-class J1: header-only stub entry")
        res = grade(repo, "C", rev, FREEZE, os.path.dirname(d))
        out.append(block("J1", "header-only stub entry", res,
                         "the frozen entry %s replaced by a %d-line "
                         "provenance header and no body; %s's used-by names it"
                         % (path, 10, rid), rev, FREEZE,
                         "corpus/SOURCES.md, " + path))
        out.append("")
    finally:
        shutil.rmtree(d, ignore_errors=True)

    # --- the r76 fixtures that already exist for these classes -------------
    for name, r76name, claim, ref in (
            ("J2", "J2", "C", C_LANDS),
            ("J3", "J3", "C", C_LANDS),
            ("J4", "J4f", "Ca", CA_LANDS),
            ("J5", "J5", "Ca", CA_LANDS),
            ("J6", "J6", "Ca", CA_LANDS),
            ("J7", "J8", "Ca", CA_LANDS)):
        try:
            text, fx = measure_r76_fixture(name, r76name, claim, ref)
            out.append(text)
            out.append("# created-paths: %s" % (", ".join(fx.paths) or "-"))
            out.append("")
            jf.cleanup(fx)
        except Exception as exc:                       # noqa: BLE001
            out.append("### %s\n# ERROR %s: %s\n" % (name, type(exc).__name__,
                                                     exc))

    # --- J4b: the evasive constant printer on the frozen ledger ------------
    def evasive(repo):
        doc = jf.read_json(repo, LEDGER)
        jf.write_json(repo, LEDGER, jf.rewrite_ledger_observe(doc, "evasive"))

    try:
        d, repo = fresh("evasive", FREEZE)
        base = json.loads(git(LANE, "show", "%s:%s" % (FREEZE, LEDGER)))
        jf.write_json(repo, LEDGER, jf.rewrite_ledger_observe(base, "evasive"))
        fz = jf.commit_all(repo, "r76-class J4b: evasive printers (freeze)")
        lands = jf.commit_all(repo, "r76-class J4b: empty landing",
                              allow_empty=True)
        changed = tuple(git(repo, "diff", "--name-only", FREEZE, fz).split())
        res = grade(repo, "Ca", lands, fz, os.path.dirname(d))
        out.append(block("J4b", "evasive constant printer", res,
                         "every observe_cmd rewritten to "
                         "python3 -c 'import os;assert os.sep;print(str(...))'",
                         lands, fz, ", ".join(changed)))
        out.append("")
    finally:
        shutil.rmtree(d, ignore_errors=True)

    # --- J8: stated_at outside the allowlist (L76-19 cleaned) --------------
    try:
        out.append(measure_own_freeze(
            "J8", "stated_at outside the allowlist",
            "allowlist", ledger_clean(fix_stated_text=True),
            note="r76 frozen ledger with L76-19's stated_text made verbatim "
                 "(the only remaining LEDGER problem is L76-13's "
                 "out-of-allowlist stated_at)"))
        out.append("")
    except Exception as exc:                           # noqa: BLE001
        out.append("# ERROR J8: %s\n" % exc)

    # --- J9: stated_text absent at base (L76-13 dropped) -------------------
    try:
        out.append(measure_own_freeze(
            "J9", "stated_text absent at base",
            "statedtext", ledger_clean(drop=("L76-13",)),
            note="r76 frozen ledger with L76-13 removed (the only remaining "
                 "LEDGER problem is L76-19's absent stated_text)"))
        out.append("")
    except Exception as exc:                           # noqa: BLE001
        out.append("# ERROR J9: %s\n" % exc)

    # --- J10: grep -E pattern operand carrying an escaped pipe --------------
    def pipe_pattern(repo):
        doc = jf.read_json(repo, LEDGER)
        first = doc["pairs"][0]
        first["observe_cmd"] = ["grep", "-c", "-E", "zzz\\|zzz",
                               "corpus/SOURCES.md"]
        first["expected_after"] = "0"
        jf.write_json(repo, LEDGER, doc)

    try:
        out.append(measure_own_freeze(
            "J10", "unexecutable / unmarked pattern-operand argv",
            "argv", ledger_clean(drop=("L76-13",), fix_stated_text=True),
            mutate=pipe_pattern,
            note="clean r76 ledger; L76-01's observe_cmd is "
                 "grep -c -E 'zzz\\|zzz' corpus/SOURCES.md (an escaped pipe in "
                 "the -E operand, no pattern-operand mark); the operand exists "
                 "at base and the pattern matches nothing"))
        out.append("")
    except Exception as exc:                           # noqa: BLE001
        out.append("# ERROR J10: %s\n" % exc)

    # --- J11: the required non-row lines inside the row_set scope ----------
    d = None
    try:
        d, repo = fresh("rows-scope", C_LANDS)
        text = jf.read(repo, "corpus/SOURCES.md")
        lines = text.splitlines(keepends=True)
        keep = [l for l in lines
                if not (l.startswith("- calendar-standard design — S896")
                        or l.startswith("**State-standard calendar"))]
        dropped = len(lines) - len(keep)
        jf.write(repo, "corpus/SOURCES.md", "".join(keep))
        rev = jf.commit_all(repo, "r76-class J11: required Paths/Search-log "
                                  "lines removed (rows unchanged)")
        res = grade(repo, "C", rev, FREEZE, os.path.dirname(d))
        out.append(block("J11", "required non-row lines counted as out-of-set",
                         res,
                         "r76 C landing with its %d required non-row "
                         "Paths/Search-log line(s) removed; the row append is "
                         "untouched" % dropped, rev, FREEZE, "corpus/SOURCES.md"))
        out.append("")
    except Exception as exc:                           # noqa: BLE001
        out.append("# ERROR J11: %s\n" % exc)
    finally:
        if d:
            shutil.rmtree(d, ignore_errors=True)

    text = "\n".join(out)
    with open(sys.argv[1] if len(sys.argv) > 1 else "/dev/stdout", "w",
              encoding="utf-8") as fh:
        fh.write(text + "\n")
    print(text)


if __name__ == "__main__":
    main()
