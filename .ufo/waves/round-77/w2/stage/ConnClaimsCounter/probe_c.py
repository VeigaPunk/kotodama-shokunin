#!/usr/bin/env python3
"""ConnClaimsCounter probes against the staged ACCEPT-C-77 counter (scratch only).

Every fixture lane is created under /fast/scratch/hyaku/kotodama-r77/ConnClaimsCounter/probe.
Every git call names `-C <dir>` explicitly and asserts the toplevel is the fixture dir.
"""
import importlib.util
import json
import os
import re
import subprocess
import sys

SCR = "/fast/scratch/hyaku/kotodama-r77/ConnClaimsCounter/probe"
COUNTER = "/fast/scratch/hyaku/kotodama-r77/ConnClaimsCounter/c/accept-c.py"

spec = importlib.util.spec_from_file_location("acc_c", COUNTER)
m = importlib.util.module_from_spec(spec)
spec.loader.exec_module(m)


def git(d, *args):
    r = subprocess.run(["git", "-C", d, *args], capture_output=True, text=True)
    return r


def assert_top(d):
    top = git(d, "rev-parse", "--show-toplevel").stdout.strip()
    assert os.path.realpath(top) == os.path.realpath(d), (top, d)


def commit_on(d, msg, edits):
    """Apply edits {rel: text|callable(old)->text} on top of HEAD, commit, return sha."""
    assert_top(d)
    for rel, val in edits.items():
        full = os.path.join(d, rel)
        old = open(full, encoding="utf-8").read() if os.path.exists(full) else ""
        new = val(old) if callable(val) else val
        os.makedirs(os.path.dirname(full), exist_ok=True)
        with open(full, "w", encoding="utf-8") as fh:
            fh.write(new)
        if rel.endswith(".py"):
            os.chmod(full, 0o755)
    m._st_git(d, "add", "-A")
    m._st_git(d, "-c", "user.name=ProbeFixture", "-c",
              "user.email=probe@example.invalid", "commit", "-q", "-m", msg)
    return m._st_git(d, "rev-parse", "HEAD").stdout.strip()


def run(paths, tag):
    scratch = os.path.join(SCR, "work-" + tag)
    os.makedirs(scratch, exist_ok=True)
    code, legs, verdict, out, err = m._st_run(paths, scratch)
    fails = sorted(k for k, v in legs.items() if v == "FAIL")
    print("== %s: exit=%d verdict=%s" % (tag, code, verdict))
    print("   legs: " + " ".join("%s=%s" % (k, legs.get(k, "-")) for k in m.legs_generated()))
    print("   failing: %s" % (fails or "none"))
    return code, legs, out, err


def build(tag):
    case = os.path.join(SCR, "case-" + tag)
    assert not os.path.exists(case), case
    os.makedirs(case)
    return m._st_build(case)


def main():
    which = sys.argv[1:] or ["control", "dupline", "cited-stub", "cited-two-id",
                             "zero-id", "docid", "source-case", "evidence", "source", "readme", "query"]
    results = {}

    if "control" in which:
        p = build("control")
        results["control"] = run(p, "control")

    if "dupline" in which:
        # ROWS: append a second physical `| S005 |` row line with a different teaches cell.
        p = build("dupline")
        d = p["root"]
        reg = os.path.join("corpus", "SOURCES.md")

        def dup(old):
            lines = old.split("\n")
            out = []
            for ln in lines:
                out.append(ln)
                if ln.startswith("| S005 |"):
                    out.append(ln.replace("teaches S005", "teaches S005 (second copy)"))
            return "\n".join(out)
        sha = commit_on(d, "dup S005 row line", {reg: dup})
        p2 = dict(p, lands=sha)
        print("physical S005 lines at lands:",
              sum(1 for ln in open(os.path.join(d, reg), encoding="utf-8")
                  if ln.startswith("| S005 |")))
        results["dupline"] = run(p2, "dupline")

    if "cited-two-id" in which:
        # CITEDLINES control: two S-ids on one factual line, base tool -> red expected.
        p = build("cited-two-id")
        d = p["root"]
        ent = m._FX_ENTRY

        def two(old):
            return old + "\nThe structure and the inventory are covered together (S004, S005).\n"
        sha = commit_on(d, "two-id factual line", {ent: two})
        results["cited-two-id"] = run(dict(p, lands=sha), "cited-two-id")

    if "cited-stub" in which:
        # CITEDLINES unpinned-tool probe: same two-id line, but the lander replaces the tool.
        p = build("cited-stub")
        d = p["root"]
        ent = m._FX_ENTRY
        stub = ('#!/usr/bin/env python3\nimport sys\n'
                'print("CITED-LINES: 0 finding(s) in %d file(s)" % (len(sys.argv) - 1))\n'
                'sys.exit(0)\n')

        def two(old):
            return old + "\nThe structure and the inventory are covered together (S004, S005).\n"
        sha = commit_on(d, "two-id line + stub tool",
                        {ent: two, "tools/check-cited-lines.py": stub})
        results["cited-stub"] = run(dict(p, lands=sha), "cited-stub")

    if "zero-id" in which:
        # zero-citation factual line: exactly-one rule not enforced for zero ids.
        p = build("zero-id")
        d = p["root"]
        ent = m._FX_ENTRY

        def zero(old):
            return old + ("\nAn uncited factual sentence: the naming system has a "
                          "finite lexeme inventory of plant and flower names.\n")
        sha = commit_on(d, "zero-id factual line", {ent: zero})
        results["zero-id"] = run(dict(p, lands=sha), "zero-id")

    if "docid" in which:
        # COLLCHECK identity: query-keyed record URLs
        for u1, u2 in [("https://example.org/record?id=1", "https://example.org/record?id=2"),
                       ("https://example.org/docs/alpha", "https://example.org/docs/alpha?view=print")]:
            k1, k2 = m._doc_url_key(u1), m._doc_url_key(u2)
            print("_doc_url_key(%r)=%r" % (u1, k1))
            print("_doc_url_key(%r)=%r  equal=%s" % (u2, k2, k1 == k2))

    if "source-case" in which:
        txt = ("Source: S897 — https://wrong.example/other-document ; lane row S897\n"
               "source: S897 — https://example.org/docs/alpha ; lane row S897\n"
               "**source:** S898 — https://example.org/docs/beta\n")
        print("source_field_lines(mixed-case text) =", m.source_field_lines(txt))


    if "evidence" in which:
        ev_rel = os.path.join("reports", "round-77", "evidence", "S004.txt")

        def sub_ev(old_pat, new_val):
            def f(old):
                assert re.search(old_pat, old, re.M), old_pat
                return re.sub(old_pat, new_val, old, count=1, flags=re.M)
            return f

        def sub_row_opened(old):
            out = []
            for ln in old.split("\n"):
                if ln.startswith("| S004 |"):
                    ln2 = ln.replace("| mined | %s |" % m._FX_ACCESS, "| mined | 2026-10-20 |")
                    assert ln2 != ln
                    ln = ln2
                out.append(ln)
            return "\n".join(out)

        cases = {
            "ev-http403": {ev_rel: sub_ev(r"^http-status: 200$", "http-status: 403")},
            "ev-challenge": {ev_rel: sub_ev(r"^challenge: none$", "challenge: captcha-interstitial")},
            "ev-wrong-doc": {ev_rel: sub_ev(r"^fetch: GET .*$", "fetch: GET https://example.org/docs/gamma")},
            "ev-sha-zeroed": {ev_rel: sub_ev(r"^sha256: [0-9a-f]{64}$", "sha256: " + "0" * 64)},
            "ev-access-other": {ev_rel: sub_ev(r"^access-date: .*$", "access-date: 2026-10-20")},
            "row-opened-other": {os.path.join("corpus", "SOURCES.md"): sub_row_opened},
        }
        for tag, edits in cases.items():
            p = build(tag)
            sha = commit_on(p["root"], tag, edits)
            results[tag] = run(dict(p, lands=sha), tag)


    if "source" in which:
        ent = m._FX_ENTRY

        def add_line(line):
            return lambda old: old + "\n" + line + "\n"

        def edit_lines(pred, fn):
            def f(old):
                out = []
                for ln in old.split("\n"):
                    out.append(fn(ln) if pred(ln) else ln)
                return "\n".join(out)
            return f

        cases = {
            "src-multi-id": {ent: add_line("source: S004 and S005 — https://example.org/docs/alpha")},
            "src-wrong-doc": {ent: edit_lines(lambda l: l.startswith("source: 魏斌"),
                                              lambda l: l.replace("https://example.org/docs/alpha",
                                                                  "https://example.org/docs/beta"))},
            "body-staged-id": {ent: add_line("A stray reference to S903 in the body.")},
            "body-unresolved-id": {ent: add_line("A stray reference to S999 in the body.")},
            "orphan-lane-row": {ent: edit_lines(lambda l: "lane row S005" in l, lambda l: "")},
            "caps-source-wrong-doc": {ent: add_line("Source: S005 — https://wrong.example/other ; lane row S005")},
        }
        for tag, edits in cases.items():
            p = build(tag)
            sha = commit_on(p["root"], tag, edits)
            results[tag] = run(dict(p, lands=sha), tag)


    if "readme" in which:
        rd = os.path.join("corpus", "README.md")

        def dup_old_row(old):
            # second index row for an EXISTING base knowledge file (sample.md)
            out = []
            for ln in old.split("\n"):
                out.append(ln)
                if ln.startswith("- `sample.md`"):
                    out.append(ln + " (duplicate index row)")
            return "\n".join(out)
        p = build("readme-dup-old")
        sha = commit_on(p["root"], "readme-dup-old", {rd: dup_old_row})
        results["readme-dup-old"] = run(dict(p, lands=sha), "readme-dup-old")


    if "query" in which:
        reg = os.path.join("corpus", "SOURCES.md")

        def other_record(old):
            out = []
            for ln in old.split("\n"):
                if ln.startswith("| S004 |"):
                    ln = ln.replace("https://example.org/docs/alpha",
                                    "https://example.org/docs/alpha?id=2")
                out.append(ln)
            return "\n".join(out)
        p = build("query-other-record")
        sha = commit_on(p["root"], "query-other-record", {reg: other_record})
        results["query-other-record"] = run(dict(p, lands=sha), "query-other-record")
        print("S004 row at lands:", [ln for ln in open(os.path.join(p["root"], reg), encoding="utf-8").read().split("\n") if ln.startswith("| S004 |")][0][:260])

    print("DONE")


if __name__ == "__main__":
    main()
