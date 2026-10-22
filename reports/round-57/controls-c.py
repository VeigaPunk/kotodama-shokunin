#!/usr/bin/env python3
r"""Round-57 claim C pre-data controls (addendum §9). Run from the lane root:

  python3 -B reports/round-57/controls-c.py

Each control is a sandbox clone of the lane at the claim base (git clone under
/fast/scratch/hyaku/kotodama-r57/controls-c/, GIT_DIR, GIT_WORK_TREE and GIT_INDEX_FILE unset; never
the lane), edited as below and scored with `python3 -B reports/round-57/accept-c.py` run in the clone
(the clone's own instrument bytes, which are the claim base's). Expected: every control exits 1 with
`ACCEPT-C-57: FAIL` and its named failing legs print FAIL.

  base          the claim base unchanged (do nothing) -> SET, SWEEP, FLOOR, LOCATE
  stub-invalid  the skip-the-work shortcut: the entry path with a `- topic:` line and 20 cited
                S-ids S413-S432, its README index row, section count, totals line and footer
                moved, and 20 registry rows (mined, used-by the entry, opened 2026-10-22) whose
                source cells name https://example.invalid/ URLs and whose anchors quote invented
                text -> exactly LOCATE
  stub-realurl  the same, but each source cell names a real URL a round-56 row was read from and
                each anchor quotes invented text -> exactly LOCATE, FRESH
  stub-short    fresh real URLs (UNESCO list pages 1-20) with the anchor quote "of the"
                -> exactly LOCATE (quote under 8 words)
  stub-echo     an archive.org advancedsearch URL whose query carries the invented quote (a page
                that reflects its request) -> exactly LOCATE (search URL)
  stub-selfhost the lane's own registry on raw.githubusercontent.com with real round-56 anchor
                quotes -> exactly LOCATE (denied host)
  stub-copied   twenty round-56 rows (8-word-or-longer anchor quotes) copied under the new ids with
                their real URLs and quotes -> at least FRESH
Exit 0 when every control fails as expected; 1 otherwise.
"""
import os
import re
import shutil
import subprocess
import sys

SCRATCH = "/fast/scratch/hyaku/kotodama-r57/controls-c"
ENTRY = "corpus/knowledge/myth-symbol/heraldry-emblems-identity-marks.md"
TOPIC = "control stub on emblems, never a real entry"
EXPECT = {"base": ["FLOOR", "LOCATE", "SET", "SWEEP"], "stub-invalid": ["LOCATE"],
          "stub-realurl": ["FRESH", "LOCATE"], "stub-short": ["LOCATE"], "stub-echo": ["LOCATE"],
          "stub-selfhost": ["LOCATE"], "stub-copied": ["FRESH"]}
AT_LEAST = {"stub-copied"}
INVENTED = "the banner of the ninth river house shows a silver heron on a field of {} stars"
URL = re.compile(r"https?://[^\s<>\"|`]+")


def git(*args, cwd=None):
    env = {k: v for k, v in os.environ.items() if k not in ("GIT_DIR", "GIT_WORK_TREE", "GIT_INDEX_FILE")}
    return subprocess.run(["git"] + list(args), cwd=cwd, env=env, capture_output=True, text=True, check=True).stdout


def stub(clone, mode, real):
    ids = [f"S{n}" for n in range(413, 433)]
    body = ["# Control stub", "", f"- topic: {TOPIC}", "- couples: none (control)", "",
            "## Body", ""] + [f"- Claim {i} rests on {sid}." for i, sid in enumerate(ids)]
    open(os.path.join(clone, ENTRY), "w", encoding="utf-8").write("\n".join(body) + "\n")
    readme = os.path.join(clone, "corpus/README.md")
    text = open(readme, encoding="utf-8").read()
    text = text.replace("## myth-symbol/ (27)\n",
                        f"## myth-symbol/ (28)\n- `heraldry-emblems-identity-marks.md` — {TOPIC}\n", 1)
    text = text.replace("Total knowledge entries: 232.", "Total knowledge entries: 233.", 1)
    text = text.replace("(total 232 files; directory totals 28/27/29/29/24/95)",
                        "(total 233 files; directory totals 28/28/29/29/24/95)", 1)
    open(readme, "w", encoding="utf-8").write(text)
    rows = []
    for i, sid in enumerate(ids):
        quote = INVENTED.format(i)
        if mode == "invalid":
            url = f"https://example.invalid/{sid.lower()}"
        elif mode == "realurl":
            url = real[i][0]
        elif mode == "short":
            url, quote = f"https://whc.unesco.org/en/list/{i + 1}/", "of the"
        elif mode == "echo":
            url = "https://archive.org/advancedsearch.php?q=" + quote.replace(" ", "+") + "&output=json"
        elif mode == "selfhost":
            url = "https://raw.githubusercontent.com/vgpnk/kotodama-shokunin/main/corpus/SOURCES.md"
            quote = real[i][1]
        else:
            url, quote = real[i]
        rows.append(f"| {sid} | Control source {i} — {url} | paper | A | control | p. {i + 1}: "
                    f"\"{quote}\" | control teaching {i} | mined | 2026-10-22 | 2027-10-22 | {ENTRY} |")
    with open(os.path.join(clone, "corpus/SOURCES.md"), "a", encoding="utf-8") as handle:
        handle.write("\n".join(rows) + "\n")


def main():
    lane = os.getcwd()
    base = git("rev-parse", "main", cwd=lane).strip()
    real = []
    for line in open(os.path.join(lane, "corpus/SOURCES.md"), encoding="utf-8"):
        match = re.match(r"^\|\s*S(\d{3})\s*\|", line)
        if match and 359 <= int(match.group(1)) <= 412:
            cells = line.split("|")
            quote = re.search(r'"([^"]+)"|“([^“”]+)”', cells[6])
            quote = (quote.group(1) or quote.group(2)) if quote else ""
            if len(re.findall(r"\w+", quote)) >= 8:
                real.append((URL.findall(cells[2])[0].rstrip(").,;:'"), quote))
    real = real[:20]
    shutil.rmtree(SCRATCH, ignore_errors=True)
    os.makedirs(SCRATCH)
    ok_all = True
    print(f"# measured-revision {base} (sandbox clones under {SCRATCH})")
    for name in EXPECT:
        clone = os.path.join(SCRATCH, name)
        git("clone", "--quiet", lane, clone)
        git("checkout", "--quiet", "--detach", base, cwd=clone)
        if name != "base":
            stub(clone, name[5:], real)
        done = subprocess.run([sys.executable, "-B", "reports/round-57/accept-c.py"], cwd=clone,
                              capture_output=True, text=True, timeout=1800)
        legs = dict(re.findall(r"^([A-Z]+) (PASS|FAIL)\b", done.stdout, re.M))
        failed = sorted(k for k, v in legs.items() if v == "FAIL")
        ok = (done.returncode == 1 and "ACCEPT-C-57: FAIL" in done.stdout
              and (set(EXPECT[name]) <= set(failed) if name in AT_LEAST else failed == sorted(EXPECT[name])))
        ok_all &= ok
        print(f"## control {name} exit {done.returncode} failed_legs {failed} expected {sorted(EXPECT[name])} "
              f"-> {'AS-EXPECTED' if ok else 'UNEXPECTED'}")
        for line in done.stdout.splitlines():
            print("   " + line[:600])
        if done.stderr.strip():
            print("   stderr: " + done.stderr.strip()[:400])
    print(f"CONTROLS-C-57: {'all controls fail ACCEPT-C-57 as expected' if ok_all else 'a control did not fail as expected'}")
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
