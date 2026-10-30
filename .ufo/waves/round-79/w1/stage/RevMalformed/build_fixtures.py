#!/usr/bin/env python3
"""RevMalformed (round-79 W1) — malformed calibration-ledger fixture generator.

Builds an ISOLATED scratch fixture repository (explicitly initialised here, root
verified), with fixed commit dates so every hash is reproducible:

  commit 1 (BASE)      notes.md: "item k draft" on line k, k = 1..12
  commit 2 (FIXCOMMIT) fixtures/<ID>.json : one ledger variant per fixture

Each fixture is a single-field mutation of one valid control ledger (C00), so a
fixture's verdict is attributable to exactly the field it names.  Every ledger
observes BASE, never a mutable ref.

Usage:
  python3 -B build_fixtures.py --work <explicit scratch dir> --stage <stage dir>

--work receives the fixture repo (fixrepo/); --stage receives manifest.json and the
fixture bytes at most 64 KiB under fixtures/ (larger ones are recipe-only).
"""
import argparse
import copy
import hashlib
import json
import os
import shutil
import subprocess
import sys

DATE = "2026-10-30T00:00:00Z"
GIT_ENV = dict(os.environ,
               GIT_AUTHOR_NAME="RevMalformed", GIT_AUTHOR_EMAIL="rev@hyaku.invalid",
               GIT_COMMITTER_NAME="RevMalformed", GIT_COMMITTER_EMAIL="rev@hyaku.invalid",
               GIT_AUTHOR_DATE=DATE, GIT_COMMITTER_DATE=DATE)
NOTES = "".join("item %d draft\n" % k for k in range(1, 13))
SMALL_LIMIT = 64 * 1024


def git(repo, *args):
    r = subprocess.run(["git", "-C", repo, "-c", "commit.gpgsign=false", *args],
                       capture_output=True, env=GIT_ENV)
    if r.returncode != 0:
        sys.exit("git %s failed: %s" % (" ".join(args), r.stderr.decode(errors="replace")))
    return r.stdout.decode().strip()


def pair(k, base, pattern=None):
    pat = pattern or ("^item %d " % k)
    return {
        "id": "F-%02d" % k,
        "disposition": "ANNOTATE",
        "stated_at": "notes.md:%d" % k,
        "stated_text": "item %d draft" % k,
        "stated_parse": "(draft)",
        "observe_cmd": ["git", "grep", "-c", "-E", pat, base, "--", "notes.md"],
        "parse": ":([0-9]+)$",
        "expected_after": "1",
        "observed_at_base": "1",
        "red_at_base": True,
        "rederive": "git grep -c -E '%s' %s -- notes.md" % (pat, base),
        "why": "round-79 W1 malformed-ledger fixture (scratch)",
    }


def control(base):
    return {
        "round": 76, "claim": "Ca", "axis": "calibration", "base": base,
        "status": "FIXTURE control - scratch only", "fleet_pin": None,
        "fleet_report": None, "must_track": [],
        "pairs": [pair(k, base) for k in range(1, 11)],
    }


def ser(doc):
    return json.dumps(doc, indent=1, ensure_ascii=False) + "\n"


def build_cases(base):
    """Ordered list of dicts: id, cls, expect, label, desc, data (bytes)."""
    c = control(base)
    text = ser(c)
    cases = []

    def add(fid, cls, expect, label, desc, data):
        if isinstance(data, str):
            data = data.encode("utf-8")
        cases.append(dict(id=fid, cls=cls, expect=expect, label=label, desc=desc, data=data))

    def doc_case(fid, cls, desc, mutate, expect="REFUSE", label=None):
        d = copy.deepcopy(c)
        mutate(d)
        add(fid, cls, expect, label or cls, desc, ser(d))

    def pairs_case(fid, cls, desc, mutate_pairs, expect="REFUSE", label=None):
        def m(d):
            mutate_pairs(d["pairs"])
        doc_case(fid, cls, desc, m, expect, label)

    def field1(fid, cls, desc, key, value, expect="REFUSE", label=None):
        def m(ps):
            ps[0][key] = value
        pairs_case(fid, cls, desc, m, expect, label)

    def raw(fid, cls, desc, data, expect="REFUSE", label=None):
        add(fid, cls, expect, label or cls, desc, data)

    # ---- controls (must not be refused) ------------------------------------
    raw("C00", "CONTROL", "valid 10-pair control", text, "ACCEPT", "clean")
    raw("C01", "CRLF", "control with CRLF line endings (valid JSON)",
        text.replace("\n", "\r\n"), "ACCEPT", "clean")

    def m_legit_dup_site(ps):
        extra = pair(1, base, pattern="^item 1 d")
        extra["id"] = "F-11"
        ps.append(extra)
    doc_case("C02", "LEGIT-DUP-SITE",
             "same (stated_at,stated_text) with a DIFFERENT observe_cmd: the committed R74 "
             "LC-15/LC-18 shape; must not be refused",
             lambda d: m_legit_dup_site(d["pairs"]), "ACCEPT", "clean")

    def m_extra(d):
        d["pairs"][0]["observed_note"] = "documented extra key"
        d["pairs"][0]["statement_after"] = {"path": "notes.md", "parse": "item (\\d+)"}
        d["pairs"][0]["red_at_base"] = True
    doc_case("C03", "EXTRA-KEYS-HISTORICAL",
             "documented keys seen in committed R74/R76 ledgers (observed_note, statement_after, "
             "red_at_base); must not be refused by a strict allowlist that includes them",
             m_extra, "ACCEPT", "clean")

    # ---- document shape ------------------------------------------------------
    raw("M01", "EMPTY", "zero-byte ledger", b"", label="EMPTY")
    raw("M02", "EMPTY", "whitespace-only ledger", b" \n\t\n", label="EMPTY")
    raw("M03", "NULL-DOC", "JSON null document", "null\n", label="TYPE")
    raw("M04", "EMPTY-LIST", "top-level empty array", "[]\n", label="TYPE")
    raw("M05", "BARE-LIST", "top-level array of 10 valid pairs, no round/claim/base header",
        ser([pair(k, base) for k in range(1, 11)]), label="TYPE")
    raw("M06", "NO-PAIRS-KEY", "object without a pairs key",
        ser({k: v for k, v in c.items() if k != "pairs"}), label="EMPTY")
    doc_case("M07", "EMPTY-PAIRS", "pairs is []", lambda d: d.__setitem__("pairs", []), label="EMPTY")
    doc_case("M08", "NULL-PAIRS", "pairs is null (load path iterates None)",
             lambda d: d.__setitem__("pairs", None), label="TYPE")
    doc_case("M09", "PAIRS-IS-OBJECT", "pairs is an object keyed by id (iteration yields keys)",
             lambda d: d.__setitem__("pairs", {p["id"]: p for p in d["pairs"]}), label="TYPE")
    doc_case("M10", "PAIRS-IS-STRING", "pairs is a string",
             lambda d: d.__setitem__("pairs", "F-01 F-02"), label="TYPE")
    doc_case("M11", "NONDICT-PAIR-ELEMENTS",
             "10 valid pairs plus a string, null and number element (the load filter drops them "
             "without a problem record)",
             lambda d: d["pairs"].extend(["junk", None, 5]), label="TYPE")
    raw("M12", "BOM", "UTF-8 BOM before an otherwise valid ledger", "\ufeff" + text, label="BOM")
    raw("M13", "TRAILING-GARBAGE", "valid ledger followed by 'x'", text + "x\n", label="TRAILING")
    raw("M14", "TWO-DOCUMENTS", "two concatenated JSON documents", text + text, label="TRAILING")
    raw("M15", "INVALID-UTF8", "byte 0xff inside a stated_text value",
        text.encode("utf-8").replace(b"item 3 draft", b"item 3 dr\xffft", 1), label="UTF8")
    raw("M16", "DEEP-NESTING", "200000 nested '[' (parser recursion depth)",
        "[" * 200000 + "]" * 200000, label="DEPTH")
    raw("M17", "OVERSIZE", "8 MiB ledger: pair F-01 'why' padded (recipe-only, > 64 KiB)",
        ser(dict(c, pairs=[dict(pair(1, base), why="x" * (8 * 1024 * 1024))] +
                 [pair(k, base) for k in range(2, 11)])), label="SIZE")

    # ---- non-finite and duplicate keys (raw text) -----------------------------
    raw("M18", "NAN-ROUND", "round is NaN", text.replace('"round": 76,', '"round": NaN,', 1),
        label="NONFINITE")
    raw("M19", "NAN-FIELD", "pair field 'weight' is NaN (no validator reads it)",
        text.replace('"id": "F-01",', '"id": "F-01",\n   "weight": NaN,', 1), label="NONFINITE")
    raw("M20", "INFINITY-FIELD", "pair field 'weight' is Infinity",
        text.replace('"id": "F-01",', '"id": "F-01",\n   "weight": Infinity,', 1), label="NONFINITE")
    raw("M21", "DUPKEY-TOP", "top-level 'round' appears twice (79 then 76)",
        text.replace('"round": 76,', '"round": 79,\n "round": 76,', 1), label="DUPKEY")
    raw("M22", "DUPKEY-PAIR", "pair F-01 'expected_after' appears twice ('1' then '9')",
        text.replace('"expected_after": "1",', '"expected_after": "1",\n   "expected_after": "9",', 1),
        label="DUPKEY")

    # ---- duplicate pairs -----------------------------------------------------
    doc_case("M23", "DUPID", "pair F-03 renamed to F-01 (two pairs share an id)",
             lambda d: d["pairs"][2].__setitem__("id", "F-01"), label="DUPID")

    def m_dup_content(d):
        dup = copy.deepcopy(d["pairs"][0])
        dup["id"] = "F-11"
        d["pairs"].append(dup)
    doc_case("M24", "DUP-CONTENT",
             "F-11 is a copy of F-01 with only the id changed (same site, text and observe_cmd)",
             m_dup_content, label="DUP-CONTENT")

    def m_no_observed(ps):
        del ps[0]["observed_at_base"]
    pairs_case("M57", "OBSERVED-MISSING",
               "pair F-01 has no observed_at_base key at all (the R76 leg only checks it when present)",
               m_no_observed, label="MISSING")

    # ---- pair field types / enums ---------------------------------------------
    field1("M25", "ID-NULL", "pair id is null", "id", None, label="TYPE")
    field1("M26", "ID-EMPTY", "pair id is ''", "id", "", label="EMPTY")
    field1("M27", "ID-BLANK", "pair id is whitespace only", "id", "   ", label="EMPTY")
    field1("M28", "ID-NUMBER", "pair id is the number 7", "id", 7, label="TYPE")
    field1("M29", "DISP-NULL", "disposition is null", "disposition", None, label="ENUM")
    field1("M30", "DISP-LIST", "disposition is a one-element list", "disposition", ["ANNOTATE"],
           label="ENUM")
    field1("M31", "DISP-CASE", "disposition is 'annotate' (lower case)", "disposition", "annotate",
           label="ENUM")
    field1("M32", "STATED-TEXT-NUMBER", "stated_text is the number 42 (stated_parse present)",
           "stated_text", 42, label="TYPE")
    field1("M33", "STATED-TEXT-LIST", "stated_text is a list", "stated_text", ["item 1 draft"],
           label="TYPE")
    field1("M34", "OBSERVE-STRING", "observe_cmd is a shell string, not an argv list",
           "observe_cmd", "git grep -c -E '^item 1 ' HEAD -- notes.md", label="TYPE")
    field1("M35", "OBSERVE-INT", "observe_cmd has an integer element", "observe_cmd",
           ["git", "grep", "-c", "-E", 1, "x", "--", "notes.md"], label="TYPE")
    field1("M36", "OBSERVE-EMPTY", "observe_cmd is []", "observe_cmd", [], label="TYPE")
    field1("M37", "PARSE-TRUE", "parse is the boolean true", "parse", True, label="TYPE")
    field1("M38", "PARSE-ZERO", "parse is the integer 0 (falsy: raw-stdout fallback)", "parse", 0,
           label="TYPE")
    field1("M39", "PARSE-EMPTY", "parse is ''", "parse", "", label="REGEX")
    field1("M40", "PARSE-BAD-REGEX", "parse is '[' (does not compile)", "parse", "[", label="REGEX")
    field1("M41", "PARSE-NO-GROUP", "parse has no capture group", "parse", ":[0-9]+$", label="REGEX")

    def m_st_empty(ps):
        ps[0].pop("stated_parse", None)
        ps[0]["stated_token"] = ""
    pairs_case("M42", "STATED-TOKEN-EMPTY",
               "stated_token is '' and stated_parse absent (falsy value falls back to stated_text)",
               m_st_empty, label="FALSY")

    def m_st_num(ps):
        ps[0].pop("stated_parse", None)
        ps[0]["stated_token"] = 12345
    pairs_case("M43", "STATED-TOKEN-NUMBER", "stated_token is the integer 12345",
               m_st_num, label="TYPE")
    field1("M44", "STATED-PARSE-NUMBER", "stated_parse is the integer 5", "stated_parse", 5,
           label="TYPE")
    field1("M58", "PARSE-UNKNOWN-SENTINEL", "parse is 'count_presence' (underscore typo of the "
           "count-presence sentinel: compiles as a regex with no capture group)", "parse",
           "count_presence", label="REGEX")

    def m_empty_pair(d):
        d["pairs"].append({})
    doc_case("M59", "EMPTY-PAIR-OBJECT", "an empty object {} appended as the eleventh pair",
             m_empty_pair, label="EMPTY")
    field1("M45", "EXPECTED-NUMBER", "expected_after is the integer 1", "expected_after", 1,
           label="TYPE")
    field1("M46", "EXPECTED-EMPTY", "expected_after is ''", "expected_after", "", label="EMPTY")
    field1("M47", "OBSERVED-BOOL", "observed_at_base is the boolean true", "observed_at_base", True,
           label="TYPE")
    field1("M48", "OBSERVED-EMPTY", "observed_at_base is ''", "observed_at_base", "", label="EMPTY")

    def m_typo(ps):
        ps[0].pop("observed_at_base", None)
        ps[0]["observed_at_bse"] = "1"
    pairs_case("M49", "UNKNOWN-KEY-TYPO",
               "observed_at_base renamed 'observed_at_bse' (no validator reads it, no error)",
               m_typo, label="UNKNOWNKEY")
    field1("M50", "RED-STRING", "red_at_base is the string 'yes'", "red_at_base", "yes",
           label="TYPE")

    # ---- header -------------------------------------------------------------
    doc_case("M51", "ROUND-FLOAT", "round is 76.0 (float equal to 76)",
             lambda d: d.__setitem__("round", 76.0), label="TYPE")
    doc_case("M52", "ROUND-BOOL", "round is true", lambda d: d.__setitem__("round", True), label="TYPE")
    doc_case("M53", "ROUND-STRING", "round is '76'", lambda d: d.__setitem__("round", "76"),
             label="TYPE")
    doc_case("M54", "CLAIM-CASE", "claim is 'ca'", lambda d: d.__setitem__("claim", "ca"),
             label="ENUM")
    doc_case("M55", "BASE-UPPER", "base is the upper-case form of BASE",
             lambda d: d.__setitem__("base", base.upper()), label="FORMAT")

    # ---- floor (not malformed) ----------------------------------------------
    doc_case("M56", "FEWER-PAIRS", "nine valid pairs: below the min-pairs floor of 10 (a "
             "floor failure, not malformed input)",
             lambda d: d.__setitem__("pairs", d["pairs"][:9]), label="FLOOR")
    return cases


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--work", required=True, help="explicit scratch dir (created)")
    ap.add_argument("--stage", required=True, help="stage dir for manifest.json and small fixtures")
    args = ap.parse_args()
    work = os.path.abspath(args.work)
    stage = os.path.abspath(args.stage)
    os.makedirs(work, exist_ok=True)
    os.makedirs(stage, exist_ok=True)
    fix = os.path.join(work, "fixrepo")
    if os.path.exists(fix):
        shutil.rmtree(fix)
    os.makedirs(fix)
    git(fix, "init", "-q")
    root = git(fix, "rev-parse", "--show-toplevel")
    if os.path.realpath(root) != os.path.realpath(fix):
        sys.exit("ROOT MISMATCH: %s != %s" % (root, fix))
    print("fixture repo root verified:", root)
    with open(os.path.join(fix, "notes.md"), "w", encoding="utf-8") as fh:
        fh.write(NOTES)
    git(fix, "add", "notes.md")
    git(fix, "commit", "-q", "-m", "fixture base: notes.md")
    base = git(fix, "rev-parse", "HEAD")
    cases = build_cases(base)
    ids = [c["id"] for c in cases]
    if len(ids) != len(set(ids)):
        sys.exit("DUPLICATE FIXTURE IDS: %s" % sorted({i for i in ids if ids.count(i) > 1}))
    os.makedirs(os.path.join(fix, "fixtures"))
    small = os.path.join(stage, "fixtures")
    if os.path.exists(small):
        shutil.rmtree(small)
    os.makedirs(small)
    manifest = []
    for c in cases:
        data = c["data"]
        with open(os.path.join(fix, "fixtures", c["id"] + ".json"), "wb") as fh:
            fh.write(data)
        entry = {"id": c["id"], "class": c["cls"], "strict_expect": c["expect"],
                 "strict_label": c["label"], "description": c["desc"],
                 "bytes": len(data), "sha256": hashlib.sha256(data).hexdigest(),
                 "committed_as": "fixtures/%s.json" % c["id"]}
        if len(data) <= SMALL_LIMIT:
            with open(os.path.join(small, c["id"] + ".json"), "wb") as fh:
                fh.write(data)
            entry["stage_copy"] = "fixtures/%s.json" % c["id"]
        else:
            entry["stage_copy"] = None
        manifest.append(entry)
    git(fix, "add", "fixtures")
    git(fix, "commit", "-q", "-m", "fixture ledgers")
    fixcommit = git(fix, "rev-parse", "HEAD")
    doc = {"fixture_repo_root": root, "base": base, "fixcommit": fixcommit,
           "date": DATE, "control": "C00", "generator": "build_fixtures.py",
           "cases": manifest}
    with open(os.path.join(stage, "manifest.json"), "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=1, ensure_ascii=False)
        fh.write("\n")
    print("BASE", base)
    print("FIXCOMMIT", fixcommit)
    print("cases", len(manifest))


if __name__ == "__main__":
    main()
