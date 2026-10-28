#!/usr/bin/env python3
"""Bounded LEDGER-leg mutation detector — seat MutLedgerPairs, kotodama round-77 W1.

Detector under test: reports/round-76/accept-ca.py (the schema parent named by
.ufo/waves/round-77/CLAIMS-DRAFT.md: "Schema inherits round 76's"), imported
UNMODIFIED from the seat's scratch copy.  The detector's own leg_ledger() runs
on pristine, mutated and restored BYTES of each pairs file; lane bytes are
only ever read, mutated variants live under this scratch dir.

cfg fields that round-76 load_frozen() would otherwise parse out of the frozen
claims text are supplied from CLAIMS-DRAFT.md's frozen sets:
  annotate_append = LOG.md, SCORECARD.md, corpus/lessons/round-75.md,
                    corpus/lessons/round-76.md   (ANNOTATE stated_at allowlist)
  repair_mutable  = corpus/README.md, SKILL.md, SHONEN.md
CTX fleet_root mirrors the counter's runtime config (only --fleet-root may be
named after git -C).  min_pairs is scoped to the pairs under test so the
pristine baseline is judgeable; the frozen floor >=10 applies to the whole
ledger and is orthogonal to the per-pair mutations under test.
"""
import ast
import contextlib
import copy
import hashlib
import importlib.util
import io
import json
import os
import re
import subprocess

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
FLEET = "/home/vgpnk/Projects/shokunin"
BASE = "211f9526800906e0c585d878d265c37e5e090c15"
SCRATCH = "/fast/scratch/hyaku/kotodama-r77/MutLedgerPairs"
DETECTOR = os.path.join(SCRATCH, "detector", "accept-ca-r76.py")
W1STAGE = os.path.join(LANE, ".ufo/waves/round-77/w1/stage")
SCOUT_C = os.path.join(W1STAGE, "ScoutLedgerC/pairs.json")
SCOUT_A = os.path.join(W1STAGE, "ScoutLedgerA/pairs.json")
SCOUT_B = os.path.join(W1STAGE, "ScoutLedgerB/pairs.json")
RUNS = os.path.join(SCRATCH, "runs")
WORK = os.path.join(SCRATCH, "work")

ANNOTATE_APPEND = ["LOG.md", "SCORECARD.md",
                   "corpus/lessons/round-75.md", "corpus/lessons/round-76.md"]
REPAIR_MUTABLE = ["corpus/README.md", "SKILL.md", "SHONEN.md"]

spec = importlib.util.spec_from_file_location("aca", DETECTOR)
aca = importlib.util.module_from_spec(spec)
spec.loader.exec_module(aca)
os.makedirs(WORK, exist_ok=True)
aca.RUN_STATE["work"] = WORK          # scratch root for observation subprocesses
aca.CTX["fleet_root"] = FLEET         # mirror main_check's runtime config

# ---------------------------------------------------------------- fixture ---
FIX_LINE_NO = 3
FIX_TEXT = "Base `98c486bdb4650ba5b8e651d332910e8ee60ad121`"


def build_annotate_fixture():
    """ANNOTATE-family fixture pair, schema-faithful, built from real base
    bytes (shape mirrors r76 ledger L76-01).  Labeled FIXTURE — not scout
    output.  Asserted against the base tree before use."""
    r = subprocess.run(["git", "-C", LANE, "show",
                        "%s:corpus/lessons/round-76.md" % BASE],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    line = r.stdout.splitlines()[FIX_LINE_NO - 1]
    assert FIX_TEXT in " ".join(line.split()), \
        "fixture stated_text not on line %d: %r" % (FIX_LINE_NO, line[:120])
    return {
        "round": 77, "claim": "Ca", "base": BASE,
        "note": "FIXTURE pair by seat MutLedgerPairs (ANNOTATE family "
                "demonstrator); stated_text verified against git show %s:"
                "corpus/lessons/round-76.md line %d" % (BASE, FIX_LINE_NO),
        "pairs": [{
            "id": "FIX-A-01",
            "disposition": "ANNOTATE",
            "stated_at": "corpus/lessons/round-76.md:%d" % FIX_LINE_NO,
            "stated_text": FIX_TEXT,
            "stated_parse": "`([0-9a-f]{4})",
            "observe_cmd": ["git", "grep", "-c", "-E", "Base", BASE,
                            "--", "corpus/lessons/round-76.md"],
            "parse": "count-presence",
            "expected_after": "present",
            "observed_at_base": "present",
            "red_at_base": True,
            "rederive": "git grep -c -E 'Base' %s -- corpus/lessons/round-76.md" % BASE,
            "why": "Fixture: the lesson states a base token; the count "
                   "observation returns a different token, so the pair is a "
                   "genuine mismatch at base.",
        }],
    }


# -------------------------------------------------------------- mutations ---
def _corrupt_index(text, parse):
    """First char index OUTSIDE the stated_parse match span."""
    m = re.search(parse, text) if parse else None
    span = (m.start(), m.end()) if m else (-1, -1)
    for i in range(len(text)):
        if not (span[0] <= i < span[1]) and text[i] != " ":
            return i
    return len(text) - 1


def m_pristine(p):
    return p


def m_a(p):
    st = p.get("stated_text") or ""
    i = _corrupt_index(st, p.get("stated_parse"))
    ch = "#" if st[i] != "#" else "@"
    p["stated_text"] = st[:i] + ch + st[i + 1:]


def m_b1(p):
    p["stated_at"] = "corpus/lessons/round-77.md:4"


def m_b2(p):
    p["statement_after"] = {"path": "LOG.md",
                            "parse": p.get("stated_parse") or "([0-9]+)"}


def m_c1(p):
    p["observe_cmd"] = ["python3", "-c",
                        "print(%s)" % (p.get("observed_at_base") or "1")]


def m_c2(p):
    p["observe_cmd"] = ["echo", p.get("observed_at_base") or "1"]


def m_d(p):
    """Move the pinned base revision out of rev position: to just after '--'
    (path-operand position)."""
    argv = list(p["observe_cmd"])
    hexre = re.compile(r"^[0-9a-f]{40}$")
    sep = argv.index("--") if "--" in argv else len(argv)
    rev_idx = next((i for i, a in enumerate(argv[:sep])
                    if hexre.match(a) and a != aca.EMPTY_TREE), None)
    assert rev_idx is not None, "no pinned rev in %r" % (argv,)
    tok = argv.pop(rev_idx)
    sep = argv.index("--") if "--" in argv else len(argv)
    argv.insert(sep + 1, tok)
    p["observe_cmd"] = argv


def m_e(p):
    p["expected_after"] = p.get("observed_at_base")


def m_einv(p):
    p["expected_after"] = "999"


MUTATIONS = [
    ("pristine", m_pristine, "unmodified bytes"),
    ("a-stated-text-1char", m_a,
     "corrupt stated_text by one char (outside the stated_parse span)"),
    ("b1-stated-at-out-of-set", m_b1,
     "stated_at -> corpus/lessons/round-77.md:4 (not in the frozen allowlist)"),
    ("b2-statement-after-out-of-set", m_b2,
     "REPAIR only: statement_after.path -> LOG.md (not in the frozen mutable set)"),
    ("c1-observe-python3", m_c1,
     "observe_cmd executable -> python3 (interpreter class)"),
    ("c2-observe-echo", m_c2,
     "observe_cmd executable -> echo (constant-printer class)"),
    ("d-rev-out-of-rev-position", m_d,
     "move the pinned 40-hex revision after '--' (path-operand position)"),
    ("e-expected-after-equals-observed", m_e,
     "expected_after := observed_at_base"),
    ("einv-expected-after-999", m_einv,
     "BONUS counterfactual: expected_after := 999"),
]

BASE_CLONE = None


def get_base_clone():
    global BASE_CLONE
    if BASE_CLONE is None:
        cl = aca.materialize(LANE, BASE, WORK, "base")
        assert cl is not None, "materialize failed"
        top = subprocess.run(["git", "-C", cl["path"], "rev-parse",
                              "--show-toplevel"],
                             capture_output=True, text=True).stdout.strip()
        assert top == cl["path"], "clone toplevel %r != %r" % (top, cl["path"])
        assert cl["head"] == BASE
        BASE_CLONE = cl
    return BASE_CLONE


def run_ledger(label, source, family, mut_name, mut_desc, doc,
               unfiltered=False):
    if isinstance(doc, list):
        pairs_all, parsed_top = doc, {}
        meta_src = {}
    else:
        pairs_all = doc["pairs"]
        meta_src = {k: doc.get(k) for k in ("round", "claim", "base")}
    if family in ("ALL", "REPAIR-SYNTH") or unfiltered:
        pairs = pairs_all
    else:
        pairs = [p for p in pairs_all if p.get("disposition") == family]
    bytes_out = json.dumps(doc, indent=1, sort_keys=True).encode()
    parsed = json.loads(bytes_out)
    pairs_parsed = parsed if isinstance(parsed, list) else parsed["pairs"]
    if not (family in ("ALL", "REPAIR-SYNTH") or unfiltered):
        pairs_parsed = [p for p in pairs_parsed
                        if p.get("disposition") == family]
    cfg = {
        "round": meta_src.get("round", 77) if meta_src.get("round") else 77,
        "base": BASE,
        "fleet_root": FLEET,
        "root": LANE,
        "ledger_rel": "reports/round-77/ledger.json",
        "ledger_raw": bytes_out.decode(),
        "ledger_meta": meta_src,
        "min_pairs": len(pairs_parsed),
        "annotate_append": list(ANNOTATE_APPEND),
        "repair_mutable": list(REPAIR_MUTABLE),
        "lane_row_ids": [],
        "c_families": [],
    }
    out = []
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        aca.leg_ledger(out, cfg, pairs_parsed, get_base_clone(), ev=[])
    _name, ok, detail = out[-1]
    problems, n_problems = [], 0
    m = re.search(r"problems=(\d+) (\[.*\])$", detail, re.S)
    if m:
        n_problems = int(m.group(1))
        try:
            problems = ast.literal_eval(m.group(2))
        except (ValueError, SyntaxError):
            problems = [m.group(2)]
    return {
        "label": label, "source": source, "family": family,
        "mutation": mut_name, "mutation_desc": mut_desc,
        "bytes_sha256": hashlib.sha256(bytes_out).hexdigest(),
        "ledger": "PASS" if ok else "FAIL",
        "detail": detail,
        "n_problems": n_problems,
        "problems": problems,
    }


def emit(rec):
    print("RUN [%(source)s|%(family)s] %(mutation)s LEDGER=%(ledger)s "
          "problems=%(n_problems)d" % rec)
    for p in rec["problems"]:
        print("   P: %s" % p)
    if not rec["problems"]:
        print("   P: (no problem lines — detail: %s)" % rec["detail"])
    with open(os.path.join(RUNS, "transcript.jsonl"), "a") as fh:
        fh.write(json.dumps(rec) + "\n")


def load_doc(path, label):
    with open(path, "rb") as fh:
        raw = fh.read()
    try:
        return json.loads(raw), None
    except ValueError as exc:
        note = ("%s: INVALID JSON as staged — json.loads: %s"
                % (label, exc))
        print("FINDING %s" % note)
        fixed_lines = []
        for ln in raw.decode().splitlines(keepends=True):
            if '"observe_cmd"' in ln:
                ln = ln.replace("\\(", "\\\\(").replace("\\)", "\\\\)")
            fixed_lines.append(ln)
        fixed = "".join(fixed_lines)
        json.loads(fixed)  # must parse now
        out = os.path.join(RUNS, "%s.parsecopy.json" % label)
        with open(out, "w") as fh:
            fh.write(fixed)
        print("FINDING %s: fixed-for-parse copy at runs/%s.parsecopy.json "
              "(only the observe_cmd line's JSON escapes doubled; rederive/"
              "parse fields were already valid)" % (label, label))
        return json.loads(fixed), note


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def pairs_of(doc):
    return doc if isinstance(doc, list) else doc["pairs"]


def main():
    os.chdir(SCRATCH)
    print("detector sha256: %s" % sha(DETECTOR))
    for f in (SCOUT_A, SCOUT_B, SCOUT_C):
        print("stage %s sha256 (pre): %s" % (os.path.basename(os.path.dirname(f)),
                                             sha(f)))

    doc_c, note_c = load_doc(SCOUT_C, "ScoutLedgerC")
    doc_a, note_a = load_doc(SCOUT_A, "ScoutLedgerA")
    doc_b, note_b = load_doc(SCOUT_B, "ScoutLedgerB")
    assert note_c is None and note_b is None
    doc_fix = build_annotate_fixture()
    with open(os.path.join(RUNS, "annotate_fixture.json"), "w") as fh:
        json.dump(doc_fix, fh, indent=1)

    recs = []
    recs.append(run_ledger("baseline-pre", "ScoutLedgerC/ALL", "ALL",
                           "pristine", "unmodified bytes", copy.deepcopy(doc_c)))

    # SYNTH-COMPLETE REPAIR variant: ScoutLedgerC's pairs completed to
    # structural validity so REPAIR-family mutations are graded on a PASS
    # baseline.  Documented deltas from the scout bytes (SYNTH variant ONLY):
    #   1. meta "base": BASE added (scout file omits it);
    #   2. statement_after {path: corpus/README.md, parse: stated_parse} added
    #      to every REPAIR pair (r76 schema requires it; scouts omit it);
    #   3. LC77-C-05 stated_text replaced by the exact normalized base line 791
    #      (the scout's lowercase leading "the" is not a byte substring of the
    #      base "The `## linguistics/ (30)` heading ...").
    synth = copy.deepcopy(doc_c)
    synth["base"] = BASE
    for p in pairs_of(synth):
        p["statement_after"] = {"path": "corpus/README.md",
                                "parse": p.get("stated_parse") or "([0-9]+)"}
    body = subprocess.run(["git", "-C", LANE, "show", "%s:corpus/README.md" % BASE],
                          capture_output=True, text=True).stdout
    line791 = " ".join(body.splitlines()[790].split())
    p5 = [p for p in pairs_of(synth) if p["id"] == "LC77-C-05"][0]
    p5["stated_text"] = line791
    with open(os.path.join(RUNS, "synth_complete.json"), "w") as fh:
        json.dump(synth, fh, indent=1)
    print("SYNTH: LC77-C-05 stated_text := base line 791: %r" % line791[:110])

    sources = [
        ("ScoutLedgerC", doc_c, "REPAIR", False),
        ("ScoutLedgerC-SYNTH", synth, "REPAIR-SYNTH", False),
        ("ScoutLedgerA", doc_a, "ALL", True),
        ("ScoutLedgerB", doc_b, "ANNOTATE", False),
        ("FixtureA", doc_fix, "ANNOTATE", False),
    ]
    for src_label, doc, family, unfiltered in sources:
        fam_pairs = pairs_of(doc) if (family in ("ALL", "REPAIR-SYNTH")
                                      or unfiltered) else \
            [p for p in pairs_of(doc) if p.get("disposition") == family]
        eq = [(p.get("id"), p.get("expected_after") == p.get("observed_at_base"))
              for p in fam_pairs]
        print("family %s/%s pristine expected_after==observed_at_base: %s"
              % (src_label, family, eq))
        for mut_name, fn, desc in MUTATIONS:
            if mut_name == "b2-statement-after-out-of-set" and \
                    family != "REPAIR-SYNTH":
                print("RUN [%s|%s] %s SKIPPED (b2 n/a: applies only to REPAIR-typed pairs)"
                      % (src_label, family, mut_name))
                continue
            d = copy.deepcopy(doc)
            for p in pairs_of(d):
                fn(p)
            recs.append(run_ledger(mut_name, src_label, family, mut_name,
                                   desc, d, unfiltered=unfiltered))

    recs.append(run_ledger("restored-post", "ScoutLedgerC/ALL", "ALL",
                           "pristine",
                           "unmodified bytes re-read after campaign",
                           copy.deepcopy(doc_c)))
    for r in recs:
        emit(r)

    print("---- mutation deltas (new problem strings vs source pristine) ----")
    by = {}
    for r in recs:
        by.setdefault((r["source"], r["mutation"]), []).append(r)
    for src_label, _doc, family, _u in sources:
        base = by.get((src_label, "pristine"), [None])[0]
        base_set = set(base["problems"]) if base else set()
        for mut_name, _fn, _desc in MUTATIONS:
            rs = by.get((src_label, mut_name))
            if not rs:
                continue
            new = [p for p in rs[0]["problems"] if p not in base_set]
            print("DELTA %s/%s: +%d %s" % (src_label, mut_name, len(new),
                                           new[:2]))

    print("stage ScoutLedgerC/pairs.json sha256 (post): %s" % sha(SCOUT_C))
    print("stage ScoutLedgerA/pairs.json sha256 (post): %s" % sha(SCOUT_A))
    print("stage ScoutLedgerB/pairs.json sha256 (post): %s" % sha(SCOUT_B))
    pre, post = recs[0], recs[-1]
    print("baseline-pre == restored-post (ledger flag + problems): %s"
          % (pre["ledger"] == post["ledger"]
             and pre["problems"] == post["problems"]))


if __name__ == "__main__":
    main()
