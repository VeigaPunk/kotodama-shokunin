# neg-11 — negative control + repair receipt (shard R8-O11, defect index 7 = review 26 §3 D7)

- **Round:** 8 · **shard:** R8-O11 (operability, claim O) · **neg-control dir:** `reports/round-8/operability/neg-controls/neg-11/`
- **Date:** 2026-10-17 (all commands below; consolidated control run at `run_at_utc = 2026-10-17T20:19:07Z`)
- **Baseline:** declared `e7ca0faeb6680fa9891b907be628d9db578c28f4` (`reports/round-8/claims.json`); worktree `HEAD = cf338a713060f274269cdacb18cdc0085bb06aeb` (`git rev-parse HEAD`). Pre-fix bytes are taken from `e7ca0fa` by `git show`, and their sha256 values equal the pins in review 26 §0 (below), so the control binds to the declared baseline.
- **Role:** repair shard. Writes only my own hunks in the two repaired gates, this directory, and this report. No commit, no push.
- **Live fixtures:** `git status --short tools/gates/fixtures/` → empty; `sha256(tools/gates/fixtures/phonology-sanity-gate.yml) = 96dfa97e87c85a5c…` = the `e7ca0fa` blob hash (all selftest runs were done in a copy, see §3.4).

## 0. Defect selection (dependency status)

`reports/round-8/operability/defect-inventory.json` (R8-O03's artifact) did **not** exist when this shard started:

```
$ ls -la reports/round-8/operability/
total 0
drwxr-xr-x 2 vgpnk vgpnk  0 Oct 17 17:12 .
drwxr-xr-x 1 vgpnk vgpnk 86 Oct 17 17:12 ..
```

Per the shard fallback ("if inventory lands late, fall back to the two named reviews directly"), both
named reviews were read in full: `reports/supplement-opencode-1/26-parser-controls.md` and
`reports/supplement-opencode-1/29-local-boundaries.md`.

**Index assignment.** Every O-shard on disk reads its assigned "defect index" as 1-based register
order over review 26 §3 `D1…D9` (then review 29's selftest defects), and three siblings corroborate it:

- `reports/round-8/operability/neg-controls/neg-04/neg-04-report.md` §0: "The first defect in register
  order is review 26 §3 **D1** … so this shard owns **D1**" → **index 1 = D1**.
- `reports/round-8/operability/neg-controls/neg-07/neg-07-report.md` §0: "so **defect index 3 =
  review 26 §3 D3** … 1-based register order" → **index 3 = D3**.
- `reports/round-8/operability/neg-controls/neg-09/probe-prefix.py` docstring: "Pre-fix probe for
  R8-O09 (**defect D5**): … tab indentation and multi-document streams" → **index 5 = D5**.

Index 7 is therefore review 26 §3 **D7** (`26-parser-controls.md:146`), reproduced below.

**Inventory landed — numbering reconciled.** The poll found `reports/round-8/operability/defect-inventory.json`
at 3 minutes (R8-O03's artifact; sha256 `a56b8b635c36d2a2091c06c6dc46c4d696f504099fadc278a170cafa77878fc5`,
top-level **list** of 20 rows). Its `idx` field enumerates defects **per file** (D2 is split into five
rows), so its `idx 7 = R26-D3` (anchor/tag guessing — already repaired and controlled by shard
R8-O07/`neg-07`) and its `idx 11 = R26-D7` (this shard's defect). Under the dispatch convention above,
my "index 7" = register-order D7, which is what is repaired and controlled here; under the inventory's
per-file numbering my defect is row 11. Both readings leave **both** defects shipping fail-before /
pass-after controls (`neg-07` for D3, `neg-11` for D7) — the orchestrator should pick one numbering and
label the fragments accordingly, and should note that the inventory's `status_at_head` column predates
this shard's repair (row 11 reads `present_at_head`; the worktree is now repaired).

## 1. Defect and pre-fix reproduction

Review 26 §3 D7 (`26-parser-controls.md:146-150`): "Non-UTF-8 packet file → traceback, exit 1, in 2 of
5 gates. File `name: caf\xe9-probe` encoded Latin-1: `phonology` and `myth` raise uncaught
`UnicodeDecodeError` (traceback, rc=1) because their `main` catches only `OSError`
(`phonology-sanity-gate.py:1279-1284`, `myth-consistency-gate.py:833-837`)."

Pre-fix code at the declared baseline (blobs `git rev-parse e7ca0fa:<path>`):

| gate | blob | `except` at | caught |
|---|---|---|---|
| `tools/gates/phonology-sanity-gate.py` | `441f1c5dada40cf6a35691f648dc7a3ec6c4d874` | `:1282` | `OSError` only |
| `tools/gates/myth-consistency-gate.py` | `21a5e3b5c88f8a4e65a64770da2c78d93b80b534` | `:835` | `OSError` only |

Both gates document `2  could-not-evaluate — unreadable/unparseable packet` (phonology docstring
`:11-15`, myth docstring `:9-13`), so a crash with exit 1 (the "findings" code) both leaks a traceback
and breaks the caller contract: a crash is indistinguishable from a FAIL.

**Probe bytes** (shipped in the control, sha256-pinned):

```python
PROBE = ("name: t\nphonology:\n  consonants: [p, t, k]\n  vowels: [a]\n"
         "  phonotactics: (C)V\n  tones: 0\n# caf\xe9-probe\n").encode("latin-1")
# sha256 = 2d3722282732ba9846887bd5101ab7a7bbbfb385810f48c39629870f8b4175bf (102 bytes)
```

**Pre-fix sweep, all seven `tools/gates/*.py` scripts on those bytes** (pre-fix copies extracted with
`git show e7ca0fa:…`; command in §6):

```
--- PRE e7ca0fa
  phonology-sanity-gate.py         rc=1   crash=True
  naming-collision-gate.py         rc=2   crash=False
  myth-consistency-gate.py         rc=1   crash=True
  costume-era-consistency-gate.py  rc=2   crash=False
  lexicon-coverage-audit.py        rc=2   crash=False
  provenance-audit.py              rc=2   crash=False
  handoff-packet-check.py          rc=2   crash=False
```

Only the two gates the review named crash; the other five (including the two markdown gates outside
review 26's scope) already return 2 — this sweep is the negative claim's evidence.

## 2. Repair (my hunks only)

`tools/gates/phonology-sanity-gate.py` — the read boundary now covers both input paths and reports
could-not-evaluate:

```diff
     path = args[0]
-    if path == "-":
-        text = sys.stdin.read()
-    else:
-        try:
+    try:
+        if path == "-":
+            text = sys.stdin.read()
+        else:
             with open(path, encoding="utf-8") as handle:
                 text = handle.read()
-        except OSError as error:
-            print("FINDING G-DATA: UNEVALUABLE — packet could not be read: %s"
-                  % error)
-            return 2
+    except UnicodeDecodeError as error:
+        print("FINDING G-DATA: UNEVALUABLE — packet is not UTF-8 text: %s"
+              % error)
+        return 2
+    except OSError as error:
+        print("FINDING G-DATA: UNEVALUABLE — packet could not be read: %s"
+              % error)
+        return 2
```

`tools/gates/myth-consistency-gate.py` — purely additive branch after the existing handler:

```diff
     path = Path(argv[0])
     try:
         text = path.read_text(encoding="utf-8")
     except OSError as error:
         print("FINDING G-DATA: cannot read %s: %s" % (path, error))
         return 2
+    except UnicodeDecodeError as error:
+        print("FINDING G-DATA: cannot decode %s as UTF-8 text: %s"
+              % (path, error))
+        return 2
```

Both messages mirror the lane's strictest gate (`naming-collision-gate.py:1719-1721`, "not UTF-8
text"), keep the pre-existing OSError message byte-identical, and use exit 2 as documented.

**Concurrent-edit note:** the two gate files also carry other shards' hunks (D1/D3/D5/duplicate-key and
the fixture-pin repair). Only the hunks above are mine; the hash pairs in `receipts.json` pin exactly
which bytes this control ran against.

## 3. Post-fix evidence

### 3.1 Isolated negative control — 13/13 pass, exit 0

`reports/round-8/operability/neg-controls/neg-11/neg-11-control.py` (stdlib only; payloads and pre-fix
copies in a temp dir, gates as subprocesses, no live path written):

```
$ python3 reports/round-8/operability/neg-controls/neg-11/neg-11-control.py \
      --scratch /home/vgpnk/.cache/o11-tmp \
      --receipts reports/round-8/operability/neg-controls/neg-11/receipts.json
PASS C1-probe-sha256                                probe sha256 2d3722282732ba9846887bd5101ab7a7bbbfb385810f48c39629870f8b4175bf
PASS C2-fail-before-phonology                       rc=1 traceback=True findings=False
PASS C3-fail-before-myth                            rc=1 traceback=True findings=False
PASS C4-pass-after-phonology                        rc=2 msg="FINDING G-DATA: UNEVALUABLE — packet is not UTF-8 text: 'utf-8' codec "
PASS C5-pass-after-myth                             rc=2 msg='FINDING G-DATA: cannot decode … as UTF-8 text'
PASS C6-utf8-ascii-still-evaluates                  phonology rc=1, myth rc=1
PASS C7-utf8-nonascii-still-evaluates               phonology rc=1, myth rc=1
PASS C8-missing-file-path-unchanged                 phonology rc=2, myth rc=2
PASS C9-cross-gate-invariance                       naming 2->2, costume 2->2, lexicon 2->2
PASS C10-selftest-mirror                            phonology rc=0, myth rc=0
PASS C11-worktree-differs-from-pre-fix              phonology-sanity-gate.py: pre fb05c644cafb -> work 722ff91bd0d4
PASS C12-fail-before-phonology-stdin                rc=1 traceback=True
PASS C13-pass-after-phonology-stdin                 rc=2 msg="FINDING G-DATA: UNEVALUABLE — packet is not UTF-8 text: 'utf"
neg-11: 13/13 controls pass
$ echo $?
0
```

Control intent: **C2/C3/C12 fail on the pre-fix pattern** (exit 1 + traceback + no finding line),
**C4/C5/C13 pass on the repaired pattern** (exit 2 + one `G-DATA` line + no traceback). C6-C8 are the
"harm none" side: valid ASCII *and* non-ASCII UTF-8 packets still evaluate (no over-broad rejection),
and the missing-file path keeps its original message. C9 shows the three already-correct gates are
byte-behaviour-identical pre/post on the same bytes. C11 asserts the worktree actually differs from the
pre-fix bytes.

`receipts.json` (same directory) records the machine-readable result: `{"pass": 13, "fail": 0,
"verdict": "pass"}`, pre/post sha256 for the five packet gates, probe hash, and `pre_fix_rev`.

**Subsequent runs** (same control, while siblings kept editing the same two gates): `run_at_utc =
2026-10-17T20:20:49Z` → 13/13, exit 0; worktree sha256 `phonology = b3764f00a057…`, `myth =
48477d38dfa1…` (the transcript above shows the 20:19:07Z values `722ff91bd0d4…`). The pre-fix pins are
unchanged (`fb05c644…`, `26d246e9…`), because the control re-derives them from `e7ca0fa` on every run —
the fail-before leg never depends on worktree state, only the pass-after leg does, and that is the
point of the control.

### 3.2 Acceptance-harness conformance (`reports/round-8/run-validation.py`)

The O harness (R8-O15) runs every `.py` artifact under `neg-controls/` as `python3 <relative>` with
cwd = repo root, requires exit 0 and no traceback, and requires the artifact referencing a repaired
defect id (`\b[DEF]\d+\b`) to declare **both** a pre-fix and a post-fix leg marker
(`SEPARATION_LEG_MARKERS`, `run-validation.py:125-130`). This control conforms:

- the docstring names defect `D7` and both legs; the run prints `…fail-before…` (C2/C3/C12) and
  `…pass-after…` (C4/C5/C13) markers;
- the **no-argument run — exactly how the harness invokes it — exits 0**: verified at
  `2026-10-17T20:20:45Z` with `TMPDIR` unset (scratch fell to `/var/tmp`) and again with
  `TMPDIR=/proc/definitely-not-writable`, where the scratch-resolution chain (`--scratch` → `TMPDIR` →
  system temp → `~/.cache`) skips the unusable candidate and still reports 13/13. This matters: the
  64-worker wave repeatedly exhausted the 16 GB `/tmp` tmpfs during this shard, and a full temp
  directory must not turn the control into a crash;
- the harness still fails claim O on `missing defect inventory:
  reports/round-8/operability/defect-inventory.json` (R8-O03's artifact, absent at `20:21Z`) — that is
  outside this shard's write scope.

### 3.3 Seven-gate post-fix sweep

```
--- POST worktree
  phonology-sanity-gate.py         rc=2   crash=False
  naming-collision-gate.py         rc=2   crash=False
  myth-consistency-gate.py         rc=2   crash=False
  costume-era-consistency-gate.py  rc=2   crash=False
  lexicon-coverage-audit.py        rc=2   crash=False
  provenance-audit.py              rc=2   crash=False
  handoff-packet-check.py          rc=2   crash=False
```

### 3.4 Selftest matrix (run in a copy, `TMPDIR` redirected)

The live `reports/` tree is 325 MB and `/tmp` (16 GB tmpfs) was saturated by the 64-worker wave
(`rsync: … No space left on device` at 17:15Z), so verification ran on an 22 MB copy at
`$HOME/.cache/o11-verify/{pre,post}` (`tools/ examples/ corpus/ reports/supplement-opencode-1/32-craft-exercise.md`),
with `TMPDIR=$HOME/.cache/o11-tmp`. `pre` = the copy with the two gates replaced by their `e7ca0fa`
bytes; `post` = the worktree bytes.

| command (cwd = copy root) | pre (e7ca0fa gates) | post (worktree) |
|---|---|---|
| `python3 tools/gates/phonology-sanity-gate.py --selftest` | exit 0 — "15/15 planted finding IDs present; 26 control cases passed" | exit 0 — same line |
| `python3 tools/gates/myth-consistency-gate.py --selftest` | exit 0 | exit 0 |
| `python3 tools/check-gate-battery.py --selftest` | — | exit 0 — "SELFTEST OK 10/10 controls behaved as expected" |
| `python3 tools/check-gate-battery.py` (full battery) | exit 0 — `{"battery_exit": 0, "fail": 0, "pass": 7, "unevaluable": 0}` | exit 0 — same summary |
| `python3 tools/check-craft-exercise.py --selftest` | — | exit 0 — "CLI-SELFTEST OK 18/18 cases passed" |

So the repair changes no gate's selftest outcome (7/7 before and after) — expected, since review 26 §3
D10 already notes the battery has no non-UTF-8 control; that gap is exactly what C2/C4 close.

### 3.5 Blocker for the O counting command (outside this shard's write scope)

With the inventory now present, `python3 reports/round-8/run-validation.py` (R8-O15's acceptance
harness, sha256 `ab9023053b15681c58ba4499cb06995f22b44306213151b2a5cdf11b67ec943a`) **crashes** instead of
scoring claim O — it expects a mapping and the inventory is a list:

```
$ date -u +%Y-%m-%dT%H:%M:%SZ ; python3 reports/round-8/run-validation.py ; echo exit=$?
2026-10-17T20:22:10Z
Traceback (most recent call last):
  File "reports/round-8/run-validation.py", line 1121, in <module>
    sys.exit(main())
  File "reports/round-8/run-validation.py", line 1038, in main
    o_result = measure_o()
  File "reports/round-8/run-validation.py", line 866, in measure_o
    defects, defect_failures = measure_o_defects()
  File "reports/round-8/run-validation.py", line 712, in measure_o_defects
    value = inventory.get(key)
AttributeError: 'list' object has no attribute 'get'
exit=1
```

Reproduced twice (also at `20:21Z`); the crash is deterministic for the delivered pair, and it aborts
the run before any claim verdict is written (`validation.json` mtime stayed at the earlier run). Either
side can fix it — the harness can accept a top-level list (`run-validation.py:709-715`), or the
inventory can wrap its rows (`{"defects": [...]}`) — but **neither file is this shard's to write**, so
this is filed for routing to R8-O15 / R8-O03. Until it is fixed, the O claim's declared counting
command cannot run, and my `neg-11` artifacts cannot be seen by the harness's `measure_neg_controls`
path (they were checked against its requirements by hand: id reference `D7`, both leg markers, and a
no-argument run that exits 0 — §3.2).

## 4. Corpus-rule compliance

- Every count above carries its command and date: control run `2026-10-17T20:19:07Z` (13/13),
  battery `2026-10-17` (7 pass/0 fail/0 unevaluable), craft 18/18.
- Every negative claim carries its sweep: "only two gates crash on non-UTF-8" = the seven-gate PRE
  sweep in §1 plus the read-site grep
  (`grep -n "except OSError\|except (OSError\|except UnicodeDecodeError" tools/gates/*.py` →
  handlers at costume `:1154`, handoff `:882/:885`, lexicon `:983/:1449`, naming `:1716/:1719`,
  provenance `:286/:290`, and the two added sites phonology `:1324/:1328`, myth `:841/:844`).
- Every quote names its location: review 26 §3 D7 = `reports/supplement-opencode-1/26-parser-controls.md:146-150`;
  review 26 §0 pin table = same file `:16-20`; review 29 §F1 = `reports/supplement-opencode-1/29-local-boundaries.md:37-97`.

## 5. Limits and untested

1. **Index label.** `defect-inventory.json` landed during this shard's 60 s × 20 poll (at minute 3,
   `2026-10-17T17:20` local). Its per-file `idx` numbering differs from the register-order numbering
   used by every O-shard prompt on disk; §0 records both readings and the reconciliation. Index 7 = D7
   rests on register order + the neg-04/neg-07/neg-09 corroboration.
2. **Harness blocker.** `reports/round-8/run-validation.py` crashes on the delivered inventory format
   (§3.5); the O counting command cannot score until R8-O15 or R8-O03 resolves it. Not this shard's
   file to write.
3. **Scope of the repair.** Only the file/stdin read boundary was changed. Other D-register defects
   (D2 duplicate keys, D4 boolean coercion, D6 `RecursionError`, D8 ReDoS, D9 `str.format`) are other
   shards' items and are untouched here; D6 in particular is the same "crash looks like a FAIL" class
   but a different exception and a different code path.
4. **Surfaces not probed:** `provenance-audit.py`/`handoff-packet-check.py` were run on the probe bytes
   (both exit 2) but their own markdown-input error paths were not otherwise exercised; myth has no
   stdin path; no directory-path, symlink or FIFO input was tested for the new branch.
5. **Environment:** `/tmp` exhaustion and hash drift from concurrent sibling edits. `receipts.json`
   pins the exact bytes; re-running the control later will legitimately show different worktree hashes
   as siblings land more hunks in the same two files.
6. **Non-atomic fixture writes (review 29 §F1)** are another shard's item; the control avoids the
   question entirely by running `--selftest` in a mirror that starts with no `fixtures/` directory.

## 6. Reproduce

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
mkdir -p /home/vgpnk/.cache/o11-tmp            # /tmp may be full during the wave
python3 reports/round-8/operability/neg-controls/neg-11/neg-11-control.py \
    --scratch /home/vgpnk/.cache/o11-tmp \
    --receipts reports/round-8/operability/neg-controls/neg-11/receipts.json

# raw seven-gate sweep (pre vs post), no repo writes:
python3 - <<'PY'
import os, subprocess, sys, tempfile
REPO=os.getcwd()
ALL=["phonology-sanity-gate.py","naming-collision-gate.py","myth-consistency-gate.py",
     "costume-era-consistency-gate.py","lexicon-coverage-audit.py",
     "provenance-audit.py","handoff-packet-check.py"]
PROBE=("name: t\nphonology:\n  consonants: [p, t, k]\n  vowels: [a]\n"
       "  phonotactics: (C)V\n  tones: 0\n# caf\xe9-probe\n").encode("latin-1")
with tempfile.TemporaryDirectory() as d:
    p=os.path.join(d,"probe.yml"); open(p,"wb").write(PROBE)
    pre=os.path.join(d,"pre"); os.makedirs(pre)
    for g in ALL:
        open(os.path.join(pre,g),"wb").write(
            subprocess.run(["git","show","e7ca0fa:tools/gates/"+g],capture_output=True,cwd=REPO).stdout)
    for label,tree in (("PRE e7ca0fa",pre),("POST worktree",os.path.join(REPO,"tools/gates"))):
        print("---",label)
        for g in ALL:
            r=subprocess.run([sys.executable,os.path.join(tree,g),p],capture_output=True,text=True,timeout=25)
            print("  %-32s rc=%-3s crash=%s" % (g, r.returncode, "UnicodeDecodeError" in (r.stderr or "")))
PY
```
