# SentinelLanded — safety and scope attack on the landed bytes (round 73, w2 FALSIFY)

- Seat: `SentinelLanded` (leaf; no delegation, no background jobs, no `task` spawns, no lane/fleet writes outside this file).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, read-only. Attacked revision `0316b8883b4f8d44b8efd720140e7f52f734a102` (base `8841ad3b896a0227674fa0725b818c999118046f`, freeze `af65165c`).
- All experiments ran in a throwaway clone: `D=$(mktemp -d /tmp/SentinelLanded/lab.XXXX)`, `git -C "$D" init -q`, `git clone -q <lane> "$D/lane"`, `git -C "$D/lane" checkout -q --detach 0316b88…`; verified `git -C "$D" rev-parse --show-toplevel` = `/tmp/SentinelLanded/lab.WAJL`. Commits made only in that clone (`-c user.name=probe -c user.email=probe@local`).
- Tooling: **nothing installed or updated**; no `pacman` (host-wide pause respected). Downloads: none — no network request was made by this seat, so no UA/bytes/status record exists to file.
- Scope: (1) secret sweep, (2) SSRF/private-host pivots, (3) write-scope audit, (4) ledger-supplied `observe_cmd` vs the allowlist, (5) fixture-repo rule in selftest code.

---

## 1. Findings

### S-1 — MAJOR: the claim-C counter executes unverified code from the tree it grades; a forged tool yields `PASS legs=11/11`

`reports/round-73/accept-c.py:903-916` runs `tools/check-cited-lines.py` **out of the materialized lands tree** (`tool = os.path.join(mat, "tools/check-cited-lines.py")`, `subprocess.run([sys.executable, "-B", tool] + paths)`). Nothing pins that tool's sha in the receipt (the receipt header pins only the counter's own sha), and the leg's pass condition is the tool's own stdout plus exit 0. The docstring (line 50) discloses “run from the materialized tree”, so no admitted statement is *false* here — I rate it MAJOR for that reason; it becomes BLOCKER the moment the round treats `ACCEPT-C-73: PASS` as independent evidence about the tree.

Reproduction (in the clone, on a commit whose only change is that tool):

```
$ git -C /tmp/SentinelLanded/lab.WAJL/lane checkout -q -b evil
$ python3 -c 'lines=["import sys, pathlib",
  "pathlib.Path(\"/tmp/SentinelLanded/PWNED_TOOL\").write_text(\"pwned\")",
  "print(\"CITED-LINES: 0 finding(s) in %d file(s)\" % (len(sys.argv)-1))",
  "raise SystemExit(0)"]; open("tools/check-cited-lines.py","w").write("\n".join(lines)+"\n")'
$ git -c user.name=probe -c user.email=probe@local commit -q -am "hostile tool probe 2"
$ EVIL=$(git rev-parse HEAD)          # 1cd228349351dac49430c1ac49c97eabf89e6316
$ rm -f /tmp/SentinelLanded/PWNED_TOOL
$ python3 -B reports/round-73/accept-c.py --root . --lands "$EVIL" --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS CITEDLINES
ACCEPT-C-73: PASS legs=11/11
$ cat /tmp/SentinelLanded/PWNED_TOOL
pwned
```

Impact: the grader's verdict is decided by bytes supplied by the graded party, so `PASS legs=11/11` is not evidence that the *content* legs are honest — a commit that ships a lying tool passes. The same pattern exists in `leg_census`, which executes `scripts/sources-census.sh` from the fleet root (see S-4). Remediation: pin the tool by sha in the receipt and compare against the tool bytes at the counter's own revision, or run the tool from the counter's tree, not the graded tree.

*(First attempt of this probe failed because my payload had a stray newline inside a string literal — `LEG FAIL CITEDLINES … tool exit=1`. That failure was my payload's, not a counter defence; the corrected payload above is the one that ran.)*

### S-2 — BLOCKER: the admitted statement “`python3 -c` over the clone” is false; the observe allowlist is not a constraint on write, delete, network, or global config

`reports/round-73/claims.json:51` (pre-data correction CaF1-F7) states the counter was hardened so that “`observe_cmd argv[0]` is allowlisted (git, grep, find, wc, ls, cat, sha256sum, stat, python3 -c **over the clone**)”. The Ca claim's LEDGER leg repeats “argv observe_cmd over the observe allowlist”. `argv_problem` (`accept-ca.py:313-337`) checks only the basename of `argv[0]`, requires the `python3 -c` code to *mention* `pathlib|open(|subprocess|os.`, and forbids four shell substrings. `run_observe` sets `cwd=clone_path` and nothing else (`accept-ca.py:355`).

Direct probe of the predicate (imported from the graded counter):

```
$ python3 - <<'EOF'   # argv_problem from reports/round-73/accept-ca.py
("write outside clone", ["python3","-c","import subprocess;subprocess.run(['sh','-c','touch /tmp/SentinelLanded/PWNED_WRITE'])"])
("read outside clone",  ["python3","-c","print(open('/etc/hostname').read())"])
("delete via find",     ["find","/tmp/SentinelLanded/victim","-delete"])
("git outside clone",   ["git","-C","/tmp/SentinelLanded/victim","init"])
("cat arbitrary",       ["cat","/etc/shadow"])
("git global config",   ["git","config","--global","core.pager","/tmp/SentinelLanded/pwn"])
("os.system",           ["python3","-c","import os;os.system('rm -rf /tmp/SentinelLanded/victim')"])
("network",             ["python3","-c","import os,socket;os.getcwd();socket.socket().connect(('127.0.0.1',9))"])
EOF
write outside clone -> None
read outside clone -> None
delete via find -> None
git outside clone -> None
cat arbitrary -> None
git global config -> None
os.system -> None
network -> None
```

End-to-end: a ledger whose L01 `observe_cmd` is a hostile `python3 -c` is accepted and **the LEDGER leg still passes** while the command writes outside the clone:

```
$ python3 -B reports/round-73/accept-ca.py --root . --lands 0316b888… --fleet-root /home/vgpnk/Projects/shokunin \
      --ledger /tmp/SentinelLanded/evil-ledger.json
# ledger: /tmp/SentinelLanded/evil-ledger.json source=worktree-uncommitted sha256=b0971f32…
LEG PASS LEDGER
$ ls -l /tmp/SentinelLanded/PWNED_E2E
-rw-r--r-- 1 vgpnk vgpnk 0 Oct 25 20:13 /tmp/SentinelLanded/PWNED_E2E
```

Impact: `cwd` is not containment. A ledger (committed bytes, or any path handed to `--ledger`) can write, delete, rewrite `~/.gitconfig` (pager/persistence), and open sockets as the invoking user. The clone isolation the round advertises contains nothing. Remediation: drop `python3`/`find`/`git` from the allowlist in favour of a small interpreter that resolves paths under the clone and refuses absolute paths, or run observations under a namespace (`bwrap`/`unshare -n`) — and stop calling the result an allowlist.

### S-3 — MAJOR: STAMP's containment check “an observe_cmd ran outside the clone” is dead code

`accept-ca.py:855` fails STAMP when `RUN_STATE["outside_clone"]` is set; the flag is written only at `:343`, inside `run_observe(..., cwd_is_clone=False)`. The function has exactly one call site, which uses the default:

```
$ grep -n 'run_observe(' reports/round-73/accept-ca.py
340:def run_observe(clone_path, argv, cwd_is_clone=True):
373:    out, why = run_observe(clone_path, pair["observe_cmd"])
$ grep -n 'outside_clone.*=.*True' reports/round-73/accept-ca.py
343:        RUN_STATE["outside_clone"] = True
```

The guard can never fire, so the STAMP leg advertises a containment property it cannot test — consistent with S-2, where containment is in fact absent. Remediation: delete the check or make it observable (record absolute paths the child touched, or run under a namespace and fail on escape).

### S-4 — MAJOR: the CENSUS leg can be swapped by an environment variable with no trace in the receipt

`accept-c.py:926` resolves the census script as `census_sh or os.environ.get("KOTODAMA_CENSUS_SH") or <fleet>/scripts/sources-census.sh`. The receipt header names the counter sha, revisions, tree, config source, rows and entries — but never the census script or its sha.

```
$ printf '#!/bin/sh\necho "kotodama\tok\t0 findings (stub)"\nexit 0\n' > /tmp/SentinelLanded/stub-census.sh
$ chmod +x /tmp/SentinelLanded/stub-census.sh
$ KOTODAMA_CENSUS_SH=/tmp/SentinelLanded/stub-census.sh python3 -B reports/round-73/accept-c.py \
      --root . --lands 0316b888… --fleet-root /home/vgpnk/Projects/shokunin
# counter sha256 (self): 95aee881…   (no line names the census script)
LEG PASS CENSUS
ACCEPT-C-73: PASS legs=11/11
```

Impact: the same command at the same revision yields PASS with a stub census, and the receipt is indistinguishable from a genuine run; the committed telemetry cannot prove which census produced it. Remediation: record the resolved census path + sha256 in the receipt header and refuse a non-default script outside `--selftest`.

### S-5 — MAJOR: the graded counter's own USAGE line points at the superseded r1 counter, which is committed beside it under the same name

Two different `accept-ca.py` files are committed at `0316b88…`:

```
$ sha256sum .ufo/waves/round-73/counters/accept-ca.py reports/round-73/accept-ca.py
f8ebb5d849c9113d2d227494be0ec1403c746dd9124a505da0373e608bb97865  .ufo/waves/round-73/counters/accept-ca.py
222d4dd6d4082b49bfc949fa2dab804859e8f313703b70ec4e229653c2d12b89  reports/round-73/accept-ca.py
$ git show af65165cf269db346ef872e16a656eccd7264d01:reports/round-73/accept-ca.py | sha256sum
f8ebb5d849c9113d2d227494be0ec1403c746dd9124a505da0373e608bb97865  -      # the freeze bytes
```

`f8ebb5d8` is r1 (the freeze bytes, per `counter-revisions.md`); it is the file at `.ufo/waves/round-73/counters/accept-ca.py`. The graded r3 file's docstring tells the reader to run the *other* one:

```
$ grep -n 'counters/accept' reports/round-73/accept-ca.py
121:  python3 -B .ufo/waves/round-73/counters/accept-ca.py --root . \
123:  python3 -B .ufo/waves/round-73/counters/accept-ca.py --selftest
$ diff <(git show 0316b88:.ufo/waves/round-73/counters/accept-ca.py) \
       <(git show 0316b88:reports/round-73/accept-ca.py) | head -6
407c407,408
<         r = git(clone, "show", "%s:%s" % (lands, rel))
---
>         r = git(clone["path"] if isinstance(clone, dict) else clone, "show", …)
```

The stale copy lacks r2's fix (`git -C` on a dict → the `git show <lands>:ledger.json` read always failed and the counter silently read the **worktree** ledger) and r3's worktree-only-ledger guard; its selftest reports 9 scenarios instead of 10:

```
$ python3 -B .ufo/waves/round-73/counters/accept-ca.py --selftest | tail -1
SELFTEST OK: 9 scenarios — do-nothing control …, CLI exit 2 on a bad --lands
```

Impact: a reader who follows the graded artifact's instructions runs the counter whose worktree-ledger bug the round recorded as fixed, and gets a receipt with a different sha. Remediation: point the USAGE lines at `reports/round-73/accept-ca.py`, and delete or rename the frozen copy (r1's bytes are already recoverable from `af65165`).

### S-6 — MAJOR: committed absolute symlinks and hardcoded live-lane paths make the guard-proof non-reproducible and give a clone a write path into the live lane

Six symlinks were added, all absolute and all pointing at the **live** lane:

```
$ git diff --raw 8841ad3… 0316b88… | awk '$2=="120000"{print $6}'   # 6 entries
$ git cat-file -p 490ac3f2…   ->  /home/vgpnk/Projects/shokunin/kotodama-shokunin/SKILL.md
$ git cat-file -p 8d1d834f…   ->  /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge
$ git cat-file -p 6cb19182…   ->  /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/lessons
$ cd /tmp/SentinelLanded/lab.WAJL/lane && readlink -f .ufo/waves/round-73/assimilation/guard-proof/mirror/SKILL.md
/home/vgpnk/Projects/shokunin/kotodama-shokunin/SKILL.md        # not the clone
```

`.ufo/waves/round-73/assimilation/guard-proof/run-guard-proof.sh` (the script that produced the guard-proof evidence) hardcodes the live host paths (`A=`, `G=`, `L=`, `S=`, `CENSUS=`) and re-creates the symlinks with `ln -sfn "$L/…"`. It writes only to `$G/mirror/corpus/SOURCES.md` (a real file) and reads `$L/corpus/knowledge` live for the census's used-by resolution.

Impact: (a) the “mirror” is not a snapshot — its knowledge/lessons/SKILL.md are whatever the live lane holds now (including this round's own SKILL.md edit), so the guard-proof's E11 results are not reproducible from the committed bytes; (b) the archive/clone carries absolute links that resolve *out* of any clone, so any tool or rerun that writes through `…/guard-proof/mirror/corpus/knowledge/…` mutates the live lane instead of its own copy, defeating the clone rule the round applies everywhere else; (c) on any other machine the links dangle. Remediation: replace the symlinks with real copies (or relative links) and make the script take the lane root as `$1` instead of hardcoding `/home/vgpnk/…`.

### S-7 — MINOR: `--ledger` accepts an arbitrary absolute path and the LEDGER leg passes on a worktree-supplied ledger

The r3 guard refuses only the *default* path from the worktree (`accept-ca.py:416-418`); an explicit `--ledger /abs/path` is honoured and the run proceeds with `source=worktree-uncommitted` disclosed in the header (see S-2 output). The disclosure limits the damage — a receipt reader can see it — but nothing marks such a receipt as non-graded beyond that one header token. No fix required if the graded run's receipt is always checked for `source=lands`; worth a one-line note in the counter's docstring.

### S-8 — MINOR (informational): no credentials; one public author address in an evidence capture

`reports/round-73/evidence/S878.txt:14` carries the article byline's published address (`philippnovikov@gmail.com`) copied from the journal PDF. It is published data, not a credential; noted only so a later sweep does not re-litigate it.

---

## 2. What I checked and found clean

**(1) Secret sweep** over all 133 changed paths (`git diff --name-only 8841ad3… 0316b88…`, 24,658 insertions) and the five evidence captures:

```
$ git diff 8841ad3… 0316b88… | grep '^+' | grep -nE '(AKIA[0-9A-Z]{16}|ghp_[A-Za-z0-9]{36}|xox[baprs]-|AIza[0-9A-Za-z_-]{35}|sk-[A-Za-z0-9]{20,}|-----BEGIN|[A-Za-z0-9+/]{40,}={0,2})'
   (only sha256 provenance digests of fetched files, e.g. `ad56b0c8…` for the bunka capture)
$ FILES=<round-73 paths>; echo "$FILES" | xargs grep -nEi 'op://|BEGIN [A-Z ]*PRIVATE|X-Amz-Signature|PHPSESSID|JSESSIONID|csrftoken|_token|password=|api[_-]?key|Bearer |access_token|client_secret|sessionid'
   (only the identifier `stated_token` in accept-ca.py)
$ grep -nE 'https?://[^ |]*\?[^ |]*' on the five new registry rows -> none
```

No `op://` reference, no private key, no cloud/session token, no cookie, no auth-bearing query string in the new rows. The `_token` mention in a wave-1 report is prose about a CSRF field, and no token value is committed.

**(2) SSRF / private-host pivots** — the counters never fetch:

```
$ grep -nE 'urllib|requests|socket|http' reports/round-73/accept-c.py   # only urlparse (parsing), http-status field checks
$ grep -nE '^import|^from' reports/round-73/accept-ca.py                # argparse, hashlib, io, json, os, re, shlex, shutil, subprocess, sys, tempfile
$ grep -nE 'curl|wget|urllib|socket|requests' /home/vgpnk/Projects/shokunin/scripts/sources-census.sh   # hits are https:// fixture rows in heredocs only
$ grep -nE 'curl|wget|urllib|socket|requests|http' tools/check-cited-lines.py   # none
```

`materialize` clones `os.path.abspath(root)` (a path, not a URL), `git archive` is local, and no redirect is followed because no HTTP client exists. **No SSRF surface in these three tools.** The residual risk is not SSRF but code provenance (S-1, S-4).

**(3) Write scope**

```
$ git -C /home/vgpnk/Projects/shokunin status --porcelain | grep -Ei 'round-?73|kotodama'
 M .ufo/state/kotodama.report-baseline          # orchestrator state file, not a lane/round-73 path
$ git -C …/kotodama-shokunin diff --name-only 8841ad3… 0316b88… | grep -c '\.\.'     -> 0
$ git ls-tree -r 0316b88… | grep -E '\.gitmodules|160000'                            -> none
$ changed paths by top dir: .ufo/waves 101, reports/round-73 23, corpus/knowledge 2,
  corpus/lessons 1, corpus/SOURCES.md 1, corpus/README.md 1, corpus/QUALITY.md 1,
  SKILL.md 1, SHONEN.md 1, SCORECARD.md 1
$ git -C /tmp/SentinelLanded/lab.WAJL/lane status --porcelain    # after running both counters
   (empty)
```

All changed paths are inside the lane; no path traversal, no submodule, no binary addition, largest added file is `corpus/SOURCES.md` (957 KB). Both counters leave the graded clone byte-clean. The only scope escapes are the six absolute symlinks of S-6. The lane worktree still shows only the orchestrator's untracked `w2.ready*`/`build-w2.py`/`w2/`; I moved nothing.

**(4) Both counters reproduce in a fresh clone** (run from the clone at `0316b88…`, no mutation of the live lane):

```
ACCEPT-C-73: PASS legs=11/11
ACCEPT-CA-73: PASS legs=9/9
```

**(5) Fixture-repo rule** — every git call in both counters names its repo, and fixture repos are `mktemp`:

```
$ grep -nE 'subprocess\.(run|Popen|call|check_output)\(\s*\[?"?g' reports/round-73/accept-c.py reports/round-73/accept-ca.py
accept-c.py:169:    return subprocess.run(["git", "-C", root, *args], …)
accept-c.py:189:    proc = subprocess.Popen(["git", "-C", root, "archive", "--format=tar", rev], …)
accept-c.py:1213:    return subprocess.run(["git", "-C", lane, *args], …)
accept-ca.py:169:    return subprocess.run(["git", "-C", str(root), *args], …)
accept-ca.py:1006:    return subprocess.run(["git", "-C", root, *args], …)
$ grep -n '"init"' …        # accept-ca.py:1067 _g(lane,"init","-q"); :1068 _g(fleet,"init","-q"); accept-c.py:1487 gitq(lane,"init","-q")
$ grep -n 'shell=True' …    # none
```

Fixtures are created under `tempfile.mkdtemp`/`TemporaryDirectory`, identity is pinned (`-c user.name=selftest`; `GIT_AUTHOR_*`/`GIT_COMMITTER_*` env in accept-ca), and no `git` runs against the ambient repo. **No violation found in either counter.** The violation is in the guard-proof script (S-6), which hardcodes live paths instead of taking a root.

---

## 3. What I could NOT check

- **No network was used.** I re-fetched nothing, so I cannot speak to capture honesty, UA records, or live status of any of the five rows; the SSRF ruling is a code-reading result, not a fetch result.
- I did not run the hostile-ledger or hostile-tool experiments against the live lane — only inside the throwaway clone — so I have no evidence that any committed telemetry receipt was produced with a swapped census script; I only show that it could be, undetectably (S-4).
- I did not verify the historical r1 receipt (`measures-ca.txt` at `e62d731`) beyond `counter-revisions.md`'s own text.
- I did not audit the claim-C content legs (ENTRIES/ROWS/GATE/EVIDENCE quote fidelity) or the Ca numeric legs — other seats own those; my findings say nothing about whether the five rows are true.
- I did not exercise the 8 × `OBSERVE_TIMEOUT` (120 s) hang budget, and did not test `--min-pairs` misuse; both read only.
- I did not read the `.ufo/waves/round-73/w1/` seat reports beyond locating the guard-proof script, and did not examine the three dead seats' scope.

## 4. Verdict for this surface

The round's landing is **credential-clean, SSRF-free, and path-contained**; the counters reproduce and leave the graded tree untouched, and the fixture-repo rule holds in both counters. It is **not** safe as a verifier: the claim-C counter executes an unverified tool from the graded tree and prints `PASS legs=11/11` for a tree that ships a lying tool (S-1); the Ca counter's advertised hardening — “`python3 -c` over the clone”, “observe allowlist” — does not constrain writes, deletes, global config or sockets, and the LEDGER leg passes a hostile `observe_cmd` that wrote outside the clone (S-2); the containment guard that would catch this is dead code (S-3); the CENSUS verdict is swappable by an environment variable with no receipt trace (S-4); and the graded counter's own instructions point at the superseded r1 counter committed beside it (S-5).
