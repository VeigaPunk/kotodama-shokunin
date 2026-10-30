#!/usr/bin/env python3
"""SentinelExec W1 probe of the DRAFT observation grammar (stage/SentinelExec/observe_grammar.py).
Reuses the fixtures built by probe_observe.py v2 (probe/lane, probe/other, probe/home with the
hostile config). Imports the draft with -B (no bytecode in stage). Records: verdict of check_argv
for every case; for admitted cases, the run() output and the driver markers; plus controls:
(a) hostile-config effect under the scrubbed env for NON-admitted forms (env-only defence),
(b) materialize under the scrubbed env (hook must not fire)."""
import importlib.util, json, os, pathlib, subprocess, sys

SCR = pathlib.Path("/fast/scratch/hyaku/kotodama-r79/SentinelExec").resolve()
PROBE = SCR / "probe"
STAGE = pathlib.Path("/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-79/w1/stage/SentinelExec")
assert (PROBE / "lane").is_dir() and (PROBE / "other").is_dir(), "run probe_observe.py first"
spec = importlib.util.spec_from_file_location("observe_grammar", str(STAGE / "observe_grammar.py"))
og = importlib.util.module_from_spec(spec); spec.loader.exec_module(og)

REV2 = subprocess.run(["git", "-C", str(PROBE / "lane"), "rev-parse", "HEAD"],
                      capture_output=True, text=True, check=True).stdout.strip()
REV1 = subprocess.run(["git", "-C", str(PROBE / "lane"), "rev-parse", "HEAD~1"],
                      capture_output=True, text=True, check=True).stdout.strip()
OTHER = PROBE / "other"
OTHER_REV = subprocess.run(["git", "-C", str(OTHER), "rev-parse", "HEAD"],
                           capture_output=True, text=True, check=True).stdout.strip()
HOSTILE_HOME = PROBE / "home"
MARK = PROBE / "MARK"
SCRUB_HOME = PROBE / "home-scrubbed"
SCRUB_HOME.mkdir(exist_ok=True)
MAT = PROBE / "mat-draft"
if MAT.exists():
    import shutil; shutil.rmtree(MAT)
MAT.mkdir()

env_ver = subprocess.run(["git", "--version"], capture_output=True, text=True).stdout.strip()
print("git:", env_ver)
print("REV1=%s REV2=%s OTHER_REV=%s" % (REV1, REV2, OTHER_REV))

if MARK.exists(): MARK.unlink()
clone, why = og.materialize(str(PROBE / "lane"), REV2, str(MAT / "obs"), str(SCRUB_HOME))
print("MATERIALIZE(scrubbed):", clone, why, "markers:", MARK.read_text().split() if MARK.exists() else [])
mat_markers = MARK.read_text().split() if MARK.exists() else []
if MARK.exists(): MARK.unlink()

CASES = [
    ("C01", "mutable HEAD in cat-file", ["git", "cat-file", "-p", "HEAD:a.txt"], False),
    ("C02", "git show REV:path (textconv path)", ["git", "show", REV2 + ":a.txt"], False),
    ("C03", "control: cat-file blob pinned", ["git", "cat-file", "blob", REV2 + ":a.txt"], True),
    ("C04", "git grep -O worktree (pager)", ["git", "grep", "-O", "needle", "--", "a.txt"], False),
    ("C04r", "git grep -O pinned", ["git", "grep", "-O", "needle", REV2, "--", "a.txt"], False),
    ("C05", "argv -c core.pager", ["git", "-c", "core.pager=/bin/cat", "grep", "-O", "needle", "--", "a.txt"], False),
    ("C06", "git diff (ext-diff default)", ["git", "diff", REV1 + ".." + REV2, "--", "a.txt"], False),
    ("C06b", "git diff --no-ext-diff (textconv)", ["git", "diff", "--no-ext-diff", REV1 + ".." + REV2, "--", "a.txt"], False),
    ("C07", "git diff --no-ext-diff --no-textconv", ["git", "diff", "--no-ext-diff", "--no-textconv", "--no-color", "-U0", REV1 + ".." + REV2, "--", "a.txt"], False),
    ("C08", "git -C <other> cat-file", ["git", "-C", str(OTHER), "cat-file", "-p", OTHER_REV + ":secret.txt"], False),
    ("C09", "git --git-dir <other> cat-file", ["git", "--git-dir", str(OTHER / ".git"), "cat-file", "-p", OTHER_REV + ":secret.txt"], False),
    ("C10", "find -fprint", ["find", ".", "-maxdepth", "0", "-fprint", str(PROBE / "FPRINT-draft")], False),
    ("C11", "cat absolute path", ["cat", str(OTHER / "secret.txt")], False),
    ("C12", "python3 -c print(245)", ["python3", "-c", "print(245)"], False),
    ("C12b", "python3 -c decoy pathlib print(245)", ["python3", "-c", "import pathlib;print(245)"], False),
    ("C13", "python3 subprocess sh escape", ["python3", "-c", "import subprocess;subprocess.run(['sh','-c','echo x'])"], False),
    ("C14", "7-hex revision", ["git", "cat-file", "-p", REV2[:7] + ":a.txt"], False),
    ("C15", "git -C <other> update-ref -d", ["git", "-C", str(OTHER), "update-ref", "-d", "refs/heads/victim"], False),
    ("C16", "ls-files --others", ["git", "ls-files", "--others", "--exclude-standard"], False),
    ("C18", "control: ls-tree pinned path filter", ["git", "ls-tree", "-r", "--name-only", REV2, "--", "a.txt"], True),
    # additional forms the probe must exercise on the admitted side
    ("A01", "grep -n -E pinned, path filter", ["git", "grep", "-n", "-E", "needle", REV2, "--", "a.txt"], True),
    ("A02", "grep -c pinned", ["git", "grep", "-c", "needle", REV2, "--", "a.txt"], True),
    ("A03", "rev-parse --verify tree of pinned rev", ["git", "rev-parse", "--verify", "--quiet", REV2 + "^{tree}"], True),
    ("A04", "rev-list --count pinned", ["git", "rev-list", "--count", REV2], True),
    ("R01", "cat-file path traversal", ["git", "cat-file", "-p", REV2 + ":../other/secret.txt"], False),
    ("R02", "cat-file absolute path", ["git", "cat-file", "-p", REV2 + ":/etc/passwd"], False),
    ("R03", "grep pattern starting with dash", ["git", "grep", "-n", "--", "-x", REV2, "--", "a.txt"], False),
    ("R04", "grep --open-files-in-pager=sh", ["git", "grep", "--open-files-in-pager=sh", "needle", REV2, "--", "a.txt"], False),
    ("R05", "cat-file --textconv", ["git", "cat-file", "-p", REV2 + ":a.txt", "--textconv"], False),
    ("R06", "ls-tree with branch rev", ["git", "ls-tree", "-r", "--name-only", "main", "--", "a.txt"], False),
    ("R07", "rev-parse ^{tree} on a branch name", ["git", "rev-parse", "--verify", "--quiet", "main^{tree}"], False),
]

results = []
for cid, desc, argv, want in CASES:
    verdict, reason = og.check_argv(argv)
    row = {"id": cid, "desc": desc, "argv": argv, "admitted": verdict, "reason": reason,
           "expected_admit": want, "match": verdict == want}
    if verdict:
        if MARK.exists(): MARK.unlink()
        out, why = og.run(clone, argv, REV2, str(SCRUB_HOME))
        row.update({"run_why": why, "stdout": (out or "")[:200],
                    "markers": MARK.read_text().split() if MARK.exists() else []})
    results.append(row)
    print(json.dumps(row, ensure_ascii=False))

# controls: env-only defence. Run NON-admitted forms raw under the scrubbed env, with the hostile
# HOME that would otherwise fire pager / external diff / textconv. Expect no markers.
CONTROLS = [
    ("E01", "raw git diff, ext-diff on, scrubbed env", ["git", "diff", REV1 + ".." + REV2, "--", "a.txt"]),
    ("E02", "raw git diff --no-ext-diff, scrubbed env", ["git", "diff", "--no-ext-diff", REV1 + ".." + REV2, "--", "a.txt"]),
    ("E03", "raw git grep -O worktree, scrubbed env", ["git", "grep", "-O", "needle", "--", "a.txt"]),
]
for cid, desc, argv in CONTROLS:
    if MARK.exists(): MARK.unlink()
    env = og.scrubbed_env(str(SCRUB_HOME)); env.pop("GIT_PAGER"); env.pop("PAGER")  # isolate config-off defence
    p = subprocess.run(argv, cwd=clone, env=env, capture_output=True, text=True)
    row = {"id": cid, "desc": desc, "exit": p.returncode, "stdout": p.stdout[:120],
           "markers_under_scrub": MARK.read_text().split() if MARK.exists() else []}
    results.append(row); print(json.dumps(row, ensure_ascii=False))
# same controls under the HOSTILE home (no scrub): proves the markers are real, not environmental noise
for cid, desc, argv in CONTROLS:
    if MARK.exists(): MARK.unlink()
    env = og.scrubbed_env(str(HOSTILE_HOME)); [env.pop(k) for k in ("GIT_CONFIG_GLOBAL", "GIT_PAGER", "PAGER")]
    p = subprocess.run(argv, cwd=clone, env=env, capture_output=True, text=True)
    row = {"id": cid.replace("E", "H"), "desc": desc + " [HOSTILE HOME, unscrubbed config]",
           "exit": p.returncode, "markers_hostile": MARK.read_text().split() if MARK.exists() else []}
    results.append(row); print(json.dumps(row, ensure_ascii=False))

out = PROBE / "draft-results.jsonl"
out.write_text("\n".join(json.dumps(r, ensure_ascii=False) for r in results) + "\n")
print("MATERIALIZE_MARKERS", mat_markers)
print("RESULTS", out)
