#!/usr/bin/env python3
"""MutCentryIDs seat: REPOINTED mutation probe on the real round-77 entry bytes.

Cases:
  pristine : W1 clean draft entry (S897/S898 only)      -> REPOINTED expected PASS
  mut1     : pristine + staged S903 retained in the S898 source line, one
             legacy id (S886) retained as a source line, one inline (S898)
             flipped to (S903)                          -> REPOINTED expected FAIL
  mut2     : the pre-rewrite draft (RevQualityFit-2 copy) verbatim:
             S903 + all six legacy ids                  -> REPOINTED expected FAIL
  restored : mut1 fixture with pristine bytes restored   -> REPOINTED expected PASS
"""
import hashlib
import importlib.util
import json
import os
import subprocess
import sys

sys.dont_write_bytecode = True

LANE = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
COUNTER = LANE + "/.ufo/waves/round-77/w1/stage/ExecAdaptC/accept-c.py"
PRISTINE = (LANE + "/.ufo/waves/round-77/w1/drafts/corpus/knowledge/"
            "linguistics/naming-systems.amend-2026-10-23.md")
MUT2_SRC = (LANE + "/.ufo/waves/round-77/w1/stage/RevQualityFit-2/"
            "naming-systems.amend-2026-10-23.md")
STAGED_IDS = LANE + "/.ufo/waves/round-77/assimilation/staged-ids"
SCRATCH = "/fast/scratch/hyaku/kotodama-r77/MutCentryIDs"
WORK = SCRATCH + "/work"
ENTRY_PATH = "corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md"

LISHISUO = ("http://lishisuo.cssn.cn/xsyj/qhs/yjcg/202103/"
            "t20210316_5318560.shtml")
ONOM = "https://onomastica.ijppan.pl/index.php/ONOM/article/download/574/763/"
Q1 = "名的使用要早于姓"
Q2 = "there were altogether 88 terms"
LEGACY_S886_LINE = ("- source: S886 — https://kotobank.jp/word/苗字-392782 — "
                    "「世界大百科事典(旧版)」所収 苗字 項 — fetched 2026-10-23")
REMOVED_IDS = ["S886", "S888", "S889", "S890", "S891", "S896"]

spec = importlib.util.spec_from_file_location("acceptc", COUNTER)
M = importlib.util.module_from_spec(spec)
spec.loader.exec_module(M)

PRISTINE_TEXT = open(PRISTINE, encoding="utf-8").read()
MUT2_TEXT = open(MUT2_SRC, encoding="utf-8").read()

# ---- exact MUT-1 construction (three counted substitutions on PRISTINE) ----
old_s98 = "- source: S898 — Kałużyńska"
new_s903 = "- source: S903 — Kałużyńska"
assert PRISTINE_TEXT.count(old_s98) == 1, "S898 source-line anchor not unique"
mut1 = PRISTINE_TEXT.replace(old_s98, new_s903, 1)
# legacy S886 source line retained directly under the S903 line
lines = mut1.splitlines(keepends=True)
idx = next(i for i, l in enumerate(lines) if l.startswith(new_s903))
lines.insert(idx + 1, LEGACY_S886_LINE + "\n")
mut1 = "".join(lines)
# one inline (S898) -> (S903): the 88-term count sentence
anchor = "making one (S898). The page does not re-count"
assert mut1.count(anchor) == 1, "inline (S898) anchor not unique"
mut1 = mut1.replace(anchor, "making one (S903). The page does not re-count", 1)

CURRENT = {"text": PRISTINE_TEXT}
FX_ROWS = [("S897", "S897", LISHISUO, Q1), ("S898", "S903", ONOM, Q2)]
ROW_URL = {"S897": LISHISUO, "S898": ONOM}
REAL_STAGED = [l.strip() for l in open(STAGED_IDS, encoding="utf-8")
               if l.strip()]
assert "S897" in REAL_STAGED and "S903" in REAL_STAGED
assert not (set(REAL_STAGED) & {"S001", "S002", "S003"})

# --------------------------- module overrides -------------------------------
M._FX_ROWS = FX_ROWS
M._st_entry_text = lambda mut: CURRENT["text"]

_orig_claims = M._st_claims
def _claims(base, map_sha, mut):
    doc = _orig_claims(base, map_sha, mut)
    c = doc["claims"][0]
    c["removed_ids"] = list(REMOVED_IDS)
    c["ground"]["fragments"] = ["lishisuo.cssn.cn", "onomastica.ijppan.pl"]
    return doc
M._st_claims = _claims

def _map_text(mut=None):
    return json.dumps({"round": 77, "assignments": [
        {"staged_id": "S897", "new_target": "S897", "document_url": LISHISUO},
        {"staged_id": "S903", "new_target": "S898", "document_url": ONOM},
    ]}, indent=2) + "\n"
M._st_map_text = _map_text

def _assim_files(d, mut):
    base_text = M._st_base_registry()
    reg = list(M.parse_rows(base_text))
    staged = list(REAL_STAGED)
    collisions = sorted(set(reg) & set(staged))
    planted = "S004"
    header = ("# SOURCES — fixture guard proof\n\nA planted row, not a real "
              "registry.\n\n## Registry\n\n")
    indented = (header + M._st_registry_rows([
        ("S001", "planted-proof S001", "docs", "A", "x", "y", "z", "queued",
         "2026-10-27", "90d", "—"),
        ("S002", "planted-proof S002", "docs", "A", "x", "y", "z", "queued",
         "2026-10-27", "90d", "—"),
        ("S003", "planted-proof S003", "docs", "A", "x", "y", "z", "queued",
         "2026-10-27", "90d", "—"),
    ]) + "   | %s | planted 3space row | paper | A | x | y | z | queued | "
         "2026-10-27 | 90d | — |\n" % planted)
    fourspace = (header + "    | %s | planted row | paper | A | x | y | z | "
                 "queued | 2026-10-27 | 90d | — |\n" % planted)
    M._st_write(d, M.ASSIM + "/reg-ids", "\n".join(reg) + "\n")
    M._st_write(d, M.ASSIM + "/staged-ids", "\n".join(staged) + "\n")
    M._st_write(d, M.ASSIM + "/collisions",
                ("\n".join(collisions) + "\n") if collisions else "")
    M._st_write(d, M.ASSIM + "/guard-proof/indented.md", indented)
    M._st_write(d, M.ASSIM + "/guard-proof/fourspace.md", fourspace)
    M._st_write(d, M.ASSIM + "/guard-proof/reg-ids-indented",
                "\n".join(reg + [planted]) + "\n")
    M._st_write(d, M.ASSIM + "/guard-proof/reg-ids-four", "")
M._st_assim_files = _assim_files

def _evidence_doc(sid, quote, freeze_sha, claims_source=None):
    url = ROW_URL[sid]
    body = ("Fixture evidence window for %s in the round-77 REPOINTED mutation "
            "probe; the real capture bytes are not re-fetched here. " % sid
            + " ".join(["window"] * 40))
    window = body if quote in body else body + " " + quote
    src = claims_source if claims_source is not None else \
        "git show %s:reports/round-77/claims.json" % freeze_sha
    return "\n".join([
        "# evidence %s — claim C GATE (round 77)" % sid,
        "url: %s" % url,
        "fetch: GET %s" % url,
        "user-agent: Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 "
        "(KHTML, like Gecko) Chrome/130.0 Safari/537.36",
        "http-status: 200",
        "bytes: %d" % len(body.encode("utf-8")),
        "sha256: %s" % hashlib.sha256(body.encode("utf-8")).hexdigest(),
        "access-date: %s" % M._FX_ACCESS,
        "claims-source: %s" % src,
        "claims-frozen: yes",
        "challenge: none",
        "window-scope: whole-document",
        "visible-chars: %d" % len(window),
        "window-sha256: %s" % hashlib.sha256(window.encode("utf-8")).hexdigest(),
        "window-bytes: %d" % len(window.encode("utf-8")),
        "quote-words: %d" % len(quote.split()),
        "quote-chars: %d" % len(quote),
        "",
        "--- window ---",
        window,
        "--- quote ---",
        "「%s」" % quote,
        "",
    ])
M._st_evidence_doc = _evidence_doc

_orig_lesson = M._st_lesson
def _lesson(rows, rejects, quote_ok_flag=True):
    return _orig_lesson(rows, rejects, quote_ok_flag) \
        .replace("evidence/S004.txt", "evidence/S897.txt") \
        .replace("evidence/S005.txt", "evidence/S898.txt")
M._st_lesson = _lesson

# ------------------------------- cases ---------------------------------------
def run_case(name, entry_text):
    case_dir = os.path.join(SCRATCH, "case-" + name)
    CURRENT["text"] = entry_text
    paths = M._st_build(case_dir, None)
    lane_dir = paths["root"]
    cmd = [sys.executable, "-B", COUNTER,
           "--root", lane_dir, "--lands", paths["lands"],
           "--freeze", paths["freeze"], "--fleet-root", paths["fleet"],
           "--work", WORK]
    argv = " ".join(cmd)
    r = subprocess.run(cmd, capture_output=True, text=True)
    out = r.stdout or ""
    blob = git_out(lane_dir, "rev-parse", paths["lands"] + ":" + ENTRY_PATH)
    return {"name": name, "argv": argv, "rc": r.returncode, "out": out,
            "err": r.stderr or "", "lands": paths["lands"],
            "freeze": paths["freeze"], "lane": lane_dir, "entry_blob": blob}

def git_out(d, *args):
    r = subprocess.run(["git", "-C", d, *args], capture_output=True, text=True)
    if r.returncode != 0:
        raise RuntimeError("git %s failed: %s" % (" ".join(args), r.stderr))
    return r.stdout.strip()

def assert_toplevel(d):
    top = git_out(d, "rev-parse", "--show-toplevel")
    assert os.path.realpath(top) == os.path.realpath(d), \
        "toplevel %r != %r" % (top, d)

os.makedirs(SCRATCH, exist_ok=True)
runs = {}

runs["pristine"] = run_case("pristine", PRISTINE_TEXT)
runs["mut1"] = run_case("mut1", mut1)

# restore: exact pristine bytes back into the mut1 fixture, re-commit
lane = runs["mut1"]["lane"]
assert_toplevel(lane)
with open(os.path.join(lane, ENTRY_PATH), "w", encoding="utf-8") as fh:
    fh.write(PRISTINE_TEXT)
subprocess.run(["git", "-C", lane, "add", "-A"], check=True)
subprocess.run(["git", "-C", lane, "-c", "user.name=MutProbe", "-c",
                "user.email=mut@example.invalid", "commit", "-q",
                "-m", "lands-restored"], check=True)
lands2 = git_out(lane, "rev-parse", "HEAD")
blob2 = git_out(lane, "rev-parse", "HEAD:" + ENTRY_PATH)
cmd = [sys.executable, "-B", COUNTER, "--root", lane, "--lands", lands2,
       "--freeze", runs["mut1"]["freeze"], "--fleet-root",
       os.path.join(os.path.dirname(lane), "fleet"), "--work", WORK]
r = subprocess.run(cmd, capture_output=True, text=True)
runs["restored"] = {"name": "restored", "argv": " ".join(cmd),
                    "rc": r.returncode, "out": r.stdout or "",
                    "err": r.stderr or "", "lands": lands2,
                    "freeze": runs["mut1"]["freeze"], "lane": lane,
                    "entry_blob": blob2}

runs["mut2"] = run_case("mut2", MUT2_TEXT)

# ------------------------------- report --------------------------------------
os.makedirs(SCRATCH + "/runs", exist_ok=True)
summary = []
for name in ("pristine", "mut1", "restored", "mut2"):
    run = runs[name]
    fn = SCRATCH + "/runs/%s.stdout.txt" % name
    with open(fn, "w", encoding="utf-8") as fh:
        fh.write("$ %s\n# exit=%d\n%s" % (run["argv"], run["rc"], run["out"]))
        if run["err"]:
            fh.write("\n# stderr:\n" + run["err"])
    legs = [l for l in run["out"].splitlines() if l.startswith("LEG ")]
    rep = [l for l in legs if l.startswith("LEG REPOINTED") or
           l.startswith("LEG PASS REPOINTED") or l.startswith("LEG FAIL REPOINTED")]
    verdict = [l for l in run["out"].splitlines() if "ACCEPT-C-77" in l]
    fails = [l for l in run["out"].splitlines() if l.startswith("FAIL legs=")]
    passing = [l for l in run["out"].splitlines() if l.startswith("PASS legs=")]
    print("=== %s ===" % name)
    print("entry-blob:", run["entry_blob"])
    print("verdict:", (verdict or ["-"])[0])
    print("REPOINTED:", (rep or ["-"])[0])
    print("all legs:")
    for l in legs:
        print("  " + l)
    print("stdout-file:", fn)
    summary.append({"case": name, "rc": run["rc"], "lands": run["lands"],
                    "freeze": run["freeze"], "entry_blob": run["entry_blob"],
                    "verdict": (verdict or ["-"])[0],
                    "repointed": (rep or ["-"])[0]})

print("\n=== restoration evidence ===")
print("pristine entry blob:", runs["pristine"]["entry_blob"])
print("mut1     entry blob:", runs["mut1"]["entry_blob"])
print("restored entry blob:", runs["restored"]["entry_blob"])
print("mut2     entry blob:", runs["mut2"]["entry_blob"])
print("blob(restored)==blob(pristine):",
      runs["restored"]["entry_blob"] == runs["pristine"]["entry_blob"])
print("mut1 sha256:", hashlib.sha256(mut1.encode("utf-8")).hexdigest())
print("pristine sha256:",
      hashlib.sha256(PRISTINE_TEXT.encode("utf-8")).hexdigest())
print("mut2 sha256:", hashlib.sha256(MUT2_TEXT.encode("utf-8")).hexdigest())
with open(SCRATCH + "/runs/summary.json", "w", encoding="utf-8") as fh:
    json.dump(summary, fh, indent=2, ensure_ascii=False)
    fh.write("\n")
