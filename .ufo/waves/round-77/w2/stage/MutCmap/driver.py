#!/usr/bin/env python3
"""MutCmap — wave-2 falsifier probes against ACCEPT-C-77 COLLCHECK.

Detector bytes stay pristine: the counter is always executed as a subprocess
of the untouched copy at <SCRATCH>/detector/accept-c.py.  Mutations are
injected into the FIXTURE (map document bytes at freeze, frozen document_url,
or the lands registry source cell), never into the detector.
"""
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys

SCRATCH = "/fast/scratch/hyaku/kotodama-r77/MutCmap"
DET = os.path.join(SCRATCH, "detector", "accept-c.py")
CASES = os.path.join(SCRATCH, "cases")
RESULTS = os.path.join(SCRATCH, "results")
WORK = os.path.join(SCRATCH, "work")

BETA = "https://example.org/docs/beta"
ALPHA = "https://example.org/docs/alpha"
BETA_ALIAS = "https://example.org/docs/beta-alias"          # different doc, same host
ALPHA_OTHER_HOST = "https://other-host.example.org/docs/alpha"  # different doc, other host
GAMMA = "https://example.org/docs/gamma"                    # different doc
WB_BETA = "https://web.archive.org/web/20261027000000id_/" + BETA
WB_GAMMA = "https://web.archive.org/web/20240111092427id_/" + GAMMA  # Wayback carrier, WRONG embedded original
WB_BETA_ALT_FORM = "https://web.archive.org/web/20200101000000if_/" + BETA  # same doc, other ts/mod
BETA_WWW = "https://www.example.org/docs/beta"              # same doc, www form

spec = importlib.util.spec_from_file_location("accept_c", DET)
ac = importlib.util.module_from_spec(spec)
spec.loader.exec_module(ac)


def sha(b):
    return hashlib.sha256(b).hexdigest()


def gitC(lane, *args, check=True):
    r = subprocess.run(["git", "-C", lane, *args], capture_output=True, text=True)
    if check and r.returncode != 0:
        raise RuntimeError("git -C %s %s failed: %s" % (lane, " ".join(args), r.stderr))
    return r


def blob_sha(lane, ref, path):
    r = gitC(lane, "show", "%s:%s" % (ref, path))
    return sha(r.stdout.encode("utf-8"))


def assert_toplevel(lane):
    top = gitC(lane, "rev-parse", "--show-toplevel").stdout.strip()
    if os.path.realpath(top) != os.path.realpath(lane):
        raise RuntimeError("toplevel %r != fixture %r" % (top, lane))
    return top


def tree_hashes(paths):
    lane = paths["root"]
    return {
        "map@freeze": blob_sha(lane, paths["freeze"], ac.ASSIM + "/id-renumber-map.json"),
        "claims@freeze": blob_sha(lane, paths["freeze"], ac.CLAIMS),
        "registry@lands": blob_sha(lane, paths["lands"], ac.REGISTRY),
        "entry@lands": blob_sha(lane, paths["lands"], ac._FX_ENTRY),
    }


def run_counter(paths, probe):
    work = os.path.join(WORK, probe)
    os.makedirs(work, exist_ok=True)
    rc, legs, verdict, out, err = ac._st_run(paths, work)
    with open(os.path.join(RESULTS, probe + ".txt"), "w") as fh:
        fh.write("$ %s -B %s --root %s --lands %s --freeze %s --fleet-root %s --work %s\n"
                 % (sys.executable, DET, paths["root"], paths["lands"],
                    paths["freeze"], paths["fleet"], work))
        fh.write("exit=%d\n%s%s" % (rc, out, err))
    fails = sorted(k for k, v in legs.items() if v == "FAIL")
    return {"probe": probe, "exit": rc, "legs": legs, "failing": fails,
            "verdict": verdict, "receipt": os.path.join(RESULTS, probe + ".txt")}


def build(tag, mut=None):
    d = os.path.join(CASES, tag)
    shutil.rmtree(d, ignore_errors=True)
    return ac._st_build(d, mut)


def failing_set(res):
    return "(" + ", ".join("'%s'" % f for f in res["failing"]) + ")"


def main():
    os.makedirs(RESULTS, exist_ok=True)
    os.makedirs(WORK, exist_ok=True)
    det_sha_before = sha(open(DET, "rb").read())
    out = {"detector_sha_before": det_sha_before, "probes": []}

    # ---------- baseline on pristine bytes ----------
    p0 = build("p0-clean")
    res = run_counter(p0, "P0-clean-baseline")
    res["tree_hashes"] = tree_hashes(p0)
    out["p0"] = res
    print("P0 clean baseline:", res["verdict"], "exit", res["exit"])

    r = subprocess.run([sys.executable, "-B", DET, "--selftest"],
                       capture_output=True, text=True,
                       env=dict(os.environ,
                                HYAKU_SCRATCH=os.path.join(WORK, "selftest")))
    with open(os.path.join(RESULTS, "P0b-selftest.txt"), "w") as fh:
        fh.write("$ HYAKU_SCRATCH=%s %s -B %s --selftest\nexit=%d\n%s%s"
                 % (os.path.join(WORK, "selftest"), sys.executable, DET,
                    r.returncode, r.stdout, r.stderr))
    out["selftest_exit"] = r.returncode
    out["selftest_line"] = [ln for ln in r.stdout.splitlines()
                            if ln.startswith("SELFTEST")]
    print("P0b selftest:", out["selftest_line"], "exit", r.returncode)

    if res["exit"] != 0 or r.returncode != 0:
        out["baseline"] = "FAILED — all probes inconclusive"
        json.dump(out, open(os.path.join(RESULTS, "summary.json"), "w"), indent=1)
        print(json.dumps(out, indent=1))
        return 2

    # ---------- helper: map-document probes (freeze-side bytes) ----------
    def map_text(s902_doc):
        return json.dumps({"round": ac.ROUND, "assignments": [
            {"staged_id": "S901", "new_target": "S004", "document_url": ALPHA},
            {"staged_id": "S902", "new_target": "S005", "document_url": s902_doc},
        ]}, indent=2) + "\n"

    def probe_map(tag, s902_doc, name):
        orig = ac._st_map_text
        ac._st_map_text = lambda mut=None: map_text(s902_doc)
        try:
            paths = build(tag)
        finally:
            ac._st_map_text = orig
        res = run_counter(paths, name)
        res["tree_hashes"] = tree_hashes(paths)
        res["map_s902_doc"] = s902_doc
        # restoration: rebuild pristine, hash-verify against P0, rerun clean
        rp = build(tag + "-restore")
        rr = run_counter(rp, name + "-restore")
        res["restore_hashes_equal_p0"] = (tree_hashes(rp) == out["p0"]["tree_hashes"])
        res["restore_run"] = rr["verdict"]
        print(name, "->", res["verdict"], "fails:", res["failing"],
              "| restore hashes match P0:", res["restore_hashes_equal_p0"],
              "| restore rerun:", rr["verdict"])
        return res

    # ---------- M1: staged->lane map document URL -> a different document ----------
    out["probes"].append(probe_map("M1b", ALPHA_OTHER_HOST, "M1b-map-other-host"))

    # ---------- M2: Wayback embedded original changed ----------
    out["probes"].append(probe_map("M2b", WB_GAMMA, "M2b-map-wayback-wrong-original"))

    # ---------- M3: same-document URL forms ----------
    out["probes"].append(probe_map("M3a", BETA_WWW, "M3a-map-www-same-doc"))
    out["probes"].append(probe_map("M3b", WB_BETA_ALT_FORM, "M3b-map-archive-same-doc"))

    # ---------- M1a: W1's own named map-alias case, reproduced ----------
    paths = build("M1a", {"map_doc_alias": True})
    res = run_counter(paths, "M1a-map-alias-w1case")
    res["tree_hashes"] = tree_hashes(paths)
    rp = build("M1a-restore")
    rr = run_counter(rp, "M1a-map-alias-restore")
    res["restore_hashes_equal_p0"] = (tree_hashes(rp) == out["p0"]["tree_hashes"])
    res["restore_run"] = rr["verdict"]
    out["probes"].append(res)
    print("M1a ->", res["verdict"], "fails:", res["failing"],
          "| restore:", res["restore_hashes_equal_p0"], rr["verdict"])

    # ---------- M2a: Wayback embedded original in the lands SOURCE cell ----------
    paths = build("M2a")
    lane = paths["root"]
    top = assert_toplevel(lane)
    reg_path = os.path.join(lane, ac.REGISTRY)
    before_bytes = open(reg_path, "rb").read()
    lands_before = paths["lands"]
    h_before = sha(before_bytes)
    hits = before_bytes.decode("utf-8").count(WB_BETA)
    if hits != 1:
        raise RuntimeError("expected exactly 1 %s in registry, found %d" % (WB_BETA, hits))
    mutated = before_bytes.decode("utf-8").replace(WB_BETA, WB_GAMMA.replace("20240111092427", "20261027000000"))
    open(reg_path, "w").write(mutated)
    h_mut = sha(open(reg_path, "rb").read())
    gitC(lane, "add", "-A")
    gitC(lane, "-c", "user.name=MutCmap", "-c", "user.email=mut@example.invalid",
         "commit", "-q", "-m", "M2a: S005 source-cell Wayback embedded original beta->gamma")
    lands_mut = gitC(lane, "rev-parse", "HEAD").stdout.strip()
    res = run_counter({**paths, "lands": lands_mut}, "M2a-sourcecell-wayback-wrong-original")
    # restore exact bytes
    open(reg_path, "wb").write(before_bytes)
    h_after = sha(open(reg_path, "rb").read())
    gitC(lane, "add", "-A")
    gitC(lane, "-c", "user.name=MutCmap", "-c", "user.email=mut@example.invalid",
         "commit", "-q", "-m", "M2a: restore exact registry bytes")
    lands_rest = gitC(lane, "rev-parse", "HEAD").stdout.strip()
    rr = run_counter({"k": None, **paths, "lands": lands_rest}, "M2a-sourcecell-restore")
    res.update({
        "probe": "M2a-sourcecell-wayback-wrong-original",
        "toplevel_asserted": top,
        "registry_sha_before": h_before, "registry_sha_mutant": h_mut,
        "registry_sha_restored": h_after,
        "restored_bytes_identical": h_after == h_before,
        "restore_run": rr["verdict"], "restore_failing": rr["failing"],
    })
    out["probes"].append(res)
    print("M2a ->", res["verdict"], "fails:", res["failing"],
          "| bytes restored:", res["restored_bytes_identical"],
          "| restore rerun:", rr["verdict"])

    # ---------- M2c: frozen document_url is a Wayback carrier of a WRONG original ----------
    orig_claims = ac._st_claims

    def claims_wrong_wrapper(base, map_sha, mut):
        c = orig_claims(base, map_sha, mut)
        c["claims"][0]["row_set"][1]["document_url"] = WB_GAMMA
        return c

    ac._st_claims = claims_wrong_wrapper
    try:
        paths = build("M2c")
    finally:
        ac._st_claims = orig_claims
    res = run_counter(paths, "M2c-frozen-doc-wayback-wrong-original")
    res["tree_hashes"] = tree_hashes(paths)
    rp = build("M2c-restore")
    rr = run_counter(rp, "M2c-frozen-doc-restore")
    res["restore_hashes_equal_p0"] = (tree_hashes(rp) == out["p0"]["tree_hashes"])
    res["restore_run"] = rr["verdict"]
    out["probes"].append(res)
    print("M2c ->", res["verdict"], "fails:", res["failing"],
          "| restore:", res["restore_hashes_equal_p0"], rr["verdict"])

    # ---------- M3c: frozen document_url as the same-page Wayback carrier (W1 archive_doc) ----------
    paths = build("M3c", {"archive_doc": True})
    res = run_counter(paths, "M3c-frozen-doc-archive-same-doc")
    res["tree_hashes"] = tree_hashes(paths)
    rp = build("M3c-restore")
    rr = run_counter(rp, "M3c-frozen-doc-restore")
    res["restore_hashes_equal_p0"] = (tree_hashes(rp) == out["p0"]["tree_hashes"])
    res["restore_run"] = rr["verdict"]
    out["probes"].append(res)
    print("M3c ->", res["verdict"], "fails:", res["failing"],
          "| restore:", res["restore_hashes_equal_p0"], rr["verdict"])

    det_sha_after = sha(open(DET, "rb").read())
    out["detector_sha_after"] = det_sha_after
    out["detector_unchanged"] = det_sha_before == det_sha_after
    json.dump(out, open(os.path.join(RESULTS, "summary.json"), "w"), indent=1)
    print("detector unchanged:", out["detector_unchanged"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
