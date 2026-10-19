# O12 — negative proof: write surface + wrapped-field read

- Seat: `O12` (verifier), claim **O** (operability). Mission: confirm the draft never writes
  outside `tools/harness/` + `reports/round-43/`, never edits the filed r19/r27/r28
  instruments or the corpus, and that the wrapped couples field is read, not skipped.
- Observer: O12 subagent. Observation window **2026-10-19T16:54:45Z – 2026-10-19T16:56Z**
  (`date -u` → `2026-10-19T16:54:45Z`).
- Tree: HEAD `7ceff59a0216a8ea21ee43262d9fc72abf770cee` (= round baseline `7ceff59`).
- All commands read-only; `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; no git
  mutation, network, install, or in-tree `run-validation.py`.

## 0. Verdict at filing time

| Object | Verdict | Basis |
|---|---|---|
| Live tree — no write-surface violation | **PASS** | `git status --porcelain` = `?? reports/round-43/` only; `git diff HEAD` empty; sha256 manifest unchanged across the reference run |
| Reference durable instrument (`tools/harness/couples-reference-extractor.py`) | **PASS-static + PASS-dynamic** | §3 outputs, §4 gate |
| Wrapped field read (`phonetics-phonology.md:72-77`) | **PASS — 4/4 by identity** | §5; 0 tokens under the r19 single-line capture |
| **The r43 draft (`basename-couples-resolver.py` / O01)** | **could-not-evaluate — draft absent** | `find reports/round-43 -type f` at 16:54:45Z lists only `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`; `tools/harness/basename-couples-resolver.py` does not exist |

The draft-specific clauses therefore cannot be signed off by this seat. §6 is the exact
acceptance gate the integrator must run once O01 lands; it has been proven non-vacuous
against a planted-violation fixture (§4.2).

## 1. Draft absence evidence

```
$ find reports/round-43 -type f | sort
reports/round-43/claims.json
reports/round-43/targets.json
reports/round-43/telemetry/dispatch-declared.json
$ ls -l tools/harness/basename-couples-resolver.py
ls: cannot access 'tools/harness/basename-couples-resolver.py': No such file or directory
$ ls -l reports/round-43/run-validation.py
ls: cannot access 'reports/round-43/run-validation.py': No such file or directory
```

`reports/round-43/{op,calib,cov,scout,plan,cross,review,scribe,adj}/` are empty at this
window. No O01, O02, O06 or O07 draft bytes exist to scan. This seat did **not** wait for
other seats; the gate is conditional and reproducible.

## 2. Write-surface baseline (pre-run)

```
$ git status --porcelain
?? reports/round-43/
$ git diff --stat HEAD -- corpus tools reports/round-19 reports/round-27 reports/round-28
(empty)
$ git diff --cached --stat
(empty)
$ git status --porcelain --ignored -- corpus tools
!! tools/__pycache__/
!! tools/gates/__pycache__/
!! tools/gates/expected/**/run.log        (pre-existing)
!! tools/gates/frozen/**/run.log          (pre-existing)
```

No tracked change and no staged change anywhere; the only untracked path is the round
directory itself. The ignored entries are pre-existing `run.log`/`__pycache__` artifacts,
none under `corpus/`.

Integrity manifest (recursive sha256 over `corpus/`, `tools/`, `reports/round-19`,
`reports/round-27`, `reports/round-28`, `reports/round-39`, `reports/round-40`,
`reports/round-42`, excluding `__pycache__`):

```
1212 files
sha256(.scratch/o12-baseline-manifest.txt) =
3fef8d58465df045d40d3c1db1804696ddd21d84df2f3f80ee05d9090bd17335
```

Load-bearing digests at HEAD (recompute with `sha256sum`):

| File | sha256 |
|---|---|
| `tools/harness/couples-reference-extractor.py` | `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1` |
| `reports/round-19/audit/entry-audit.py` | `e7992c325a479aa7415c42722a034a95a9ea342a58367ead9cd2636a5a62830c` |
| `reports/round-27/audit/entry-audit.py` | `fb589b28cf4769ac2ce39d820640bb464a93601f4486f54268d31e1c4c06bcda` |
| `reports/round-28/readme/sweep.py` | `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3` |
| `corpus/knowledge/linguistics/phonetics-phonology.md` | `b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b` (325 lines, 20405 bytes) |
| `reports/round-39/calib/basename-couples-policy.md` | `105dfff6c667ad5b77c28be8d6070ec243b5e19029fb60ae83d6028aa2e941cf` |
| `reports/round-42/calib/basename-couples-policy-full.md` | `8c3d7c356ea7c1df3bcaab414ccc2035f6dc90272aaed305e4edf35b2890cdd6` |

The r19/r27/r28 instrument inventory is 50 `.py` files; the three named filed instruments
above are the ones the O claim names, and all 50 are covered by the manifest digest.

## 3. Reference-instrument run and tree integrity

The only durable candidate at HEAD is the r42 N6 successor
(`tools/harness/couples-reference-extractor.py`, tracked blob `1ded489b…`, committed in
`7ceff59` on 2026-10-19T13:36:54-03:00). It is used here as the **positive control** for
the gate, not as the r43 draft.

```
$ python3 -B tools/harness/couples-reference-extractor.py --selftest
PASS wrapped positive 4/4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
PASS wrapped positive heals soft wrap
PASS unwrapped regression
PASS over-capture trap (prose excluded) ['sound-symbolism.md']
PASS phantom negative: absent wrapped targets are visible, not zeroed {...}
PASS N6 regression guard: single-line capture still yields 0 tokens
PASS N6 regression guard: block read yields 4 tokens ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
PASS glob fragment classified
exit=0

$ python3 -B tools/harness/couples-reference-extractor.py --census
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  unresolved distinct=1: ../linguistics/phonology-sanity.md(x2)
  misaligned: none
exit=0
```

Tree integrity across those runs: `sha256sum` of the 1212-file manifest set before vs
after → **`NO-DIFF`**; `git status --porcelain` before vs after → **`SAME`**. The tool
opened corpus files `rb` only; its one write call is a `tempfile.mkdtemp()` selftest
fixture (line 273), which lands under the declared `TMPDIR=.scratch`, not the repo. It has
no `.scratch` path dependency (`grep -n '\.scratch'` → none) and no non-stdlib import.

## 4. The gate

### 4.1 Checks

`.scratch/o12-negative-gate.py` parses the candidate tool with `ast` and enforces:

- **W1** any `open(..., mode containing w/a/x/+)`, `Path.write_*`, `os.remove|unlink|rename|replace|rmdir|mkdir(s)`,
  `shutil` mutation must have a literal target under `reports/round-43/` or `tools/harness/`;
  a non-literal target is reported `ALLOW` only with a named reason (tempfile); otherwise
  `VIOLATION`.
- **W2** `subprocess`/`os.system|popen` → `REVIEW`; `urlopen`/`urlretrieve` → `VIOLATION`.
- **W3** imports must be stdlib-only; `sys.dont_write_bytecode` must be present.
- **W4** dynamic canary: runs `--selftest`, `--census`, and the single-path form; diffs the
  1212-file sha256 manifest and `git status --porcelain` before/after.
- **W5** wrapped-field read is checked from the per-path output: the four exact tokens
  must appear and a standalone `prosody.md` line must not.

### 4.2 Non-vacuity control (planted violations)

A fixture writing to `corpus/knowledge/planted.md`, appending to
`reports/round-19/audit/entry-audit.py`, deleting the phonetics file, importing
`requests`, and omitting `dont_write_bytecode`:

```
FILE .scratch/o12-bad-fixture.py
  dont_write_bytecode False
  non-stdlib  ['requests']
  os:remove  line 5  target=corpus/knowledge/linguistics/phonetics-phonology.md -> VIOLATION
  open       line 2  mode=w target=corpus/knowledge/planted.md -> VIOLATION
  open       line 3  mode=a target=reports/round-19/audit/entry-audit.py -> VIOLATION
  VERDICT FAIL
gate_exit=1
```

So the gate fails a violating tool and passes the reference tool; it is not a rubber stamp.

## 5. Wrapped field: read vs skipped (D1 live reproduction)

Target bytes (`corpus/knowledge/linguistics/phonetics-phonology.md:72-77`, sha256
`b4f9b003…`):

```
72  - couples: language (this file, core method); myth (divine/true names, taboo
73    naming, onomatopoeic etiologies); symbol (sound symbolism, name-shape,
74    bouba/kiki iconography); era (Neolithic bite → f/v, sound-change dating of
75    strata); costume (masks/mouthgear vs articulation, whistle & drum channels);
76    environment/anatomy design; prospective sibling files: sound-change.md, tone-
77    prosody.md, sound-symbolism.md, writing-systems.md
```

**Skipped (the filed defect):** the r19 capture
`re.search(r"^- couples:\s*(.*)$", text, re.M)` returns
`'language (this file, core method); myth (divine/true names, taboo'` and
`MDREF.findall(...)` returns **`[]` — 0 tokens**.

**Read (block extraction):** 6 continuation-bounded parts. Token extraction depends on the
join rule, and this is the trap:

| join rule | tokens found | count |
|---|---|---|
| newline join `"\n".join(parts)` | `sound-change.md`, **`prosody.md`**, `sound-symbolism.md`, `writing-systems.md` | 4 |
| space join `" ".join(parts)` | `sound-change.md`, **`prosody.md`**, `sound-symbolism.md`, `writing-systems.md` | 4 |
| hyphen-retained heal | `sound-change.md`, **`tone-prosody.md`**, `sound-symbolism.md`, `writing-systems.md` | 4 |

Only the hyphen-retained join names the four targets the field intends. Existence check:

```
sound-change.md        (absent repo-wide)
tone-prosody.md        (absent repo-wide)
sound-symbolism.md     corpus/knowledge/linguistics/sound-symbolism.md
writing-systems.md     corpus/knowledge/linguistics/writing-systems.md
prosody.md             (absent repo-wide)
```

The reference tool's per-path output confirms the correct read and classes:

```
$ python3 -B tools/harness/couples-reference-extractor.py corpus/knowledge/linguistics/phonetics-phonology.md
corpus/knowledge/linguistics/phonetics-phonology.md wrapped=True tokens=4
    sound-change.md       prospective
    sound-symbolism.md    direct
    tone-prosody.md       prospective
    writing-systems.md    direct
```

### Finding O12-F1 — a count-only "4/4" threshold can pass a wrong parse

All three join rules yield **4 tokens**; two of them yield the wrong identity set. The claim's
threshold "the wrapped field reads 4/4" is therefore satisfiable by a defective parser that
splits `tone-prosody.md` across the line break. Required: the selftest and census assertion
must compare the **token identity set**
`{sound-change.md, sound-symbolism.md, tone-prosody.md, writing-systems.md}` and assert that
a standalone `prosody.md` is absent. Owner: O01 (draft) / O02 (controls); this seat cannot
close it without the draft.

## 6. Draft acceptance gate (run when O01 lands)

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 -B .scratch/o12-negative-gate.py tools/harness/basename-couples-resolver.py --dynamic
```

Per-clause bar:

| # | Requirement | Pass criterion |
|---|---|---|
| W1 | Durable path | exactly `tools/harness/basename-couples-resolver.py` is new; no other path is created/mutated |
| W2 | Writes | none to `corpus/`, `reports/round-19|27|28`, `tools/gates/frozen/**`, other `tools/harness/*`; selftest temp only under `$TMPDIR` (`.scratch`) or `tempfile.TemporaryDirectory()` |
| W3 | Runtime | stdlib only; `sys.dont_write_bytecode = True`; no subprocess/network; no `.scratch` read dependency |
| W4 | CLI | `--selftest` exits 0; `--census` writes stdout only (any file output only via explicit `--out` under `reports/round-43/`); `[paths]` form names tokens |
| W5 | Dynamic | pre/post 1212-file manifest `NO-DIFF`; `git status` unchanged except `reports/round-43/` |
| R1 | Wrapped positive | exact four-token set above; no standalone `prosody.md` |
| R2 | Regression guard | the single-line capture still yields 0 on `phonetics-phonology.md` (so the block path is demonstrably the reader) |
| R3 | Filed bytes | r19/r27/r28 digests in §2 unchanged; no corpus edit |

The exact gate source used here is Appendix A. If `.scratch` is cleaned before integration,
the gate can be re-created from Appendix A verbatim; the digests in §2 are the durable
baseline.

## 7. Findings routed

**O12-F1 (O claim, blocking for the "4/4" wording)** — count-vs-identity trap, §5.
Owner: O01/O02; integrator must not accept a length-only assertion.

**O12-F2 (calibration/honesty, blocking for the claim's "before" text)** — `claims.json:27`
states "no durable instrument implements the r39 basename-couples policy; the only resolver
that ever ran (r39 I-C05) lives in ephemeral .scratch". This is **false at HEAD**:
`tools/harness/couples-reference-extractor.py` is tracked in `7ceff59` (blob `1ded489b…`),
its selftest passes here, and `reports/round-42/validation.json` records claim O
`"passed": true` (the round was refused on C, not O). A narrower true statement would be
"no instrument *named* `basename-couples-resolver.py` exists; the r42 extractor implements
the policy including D1/D2". Route to the integrator/scribe (`LOG.md`/`SHONEN.md`): either
re-scope the r43 O claim as consolidation/naming or replace the false before-line. Do not
land the round text with the current wording. This seat takes no position on which route.

**O12-F3 (minor, selftest cleanliness)** — the reference selftest uses
`tempfile.mkdtemp()` without cleanup (line 271). Under `TMPDIR=$PWD/.scratch` this is
scratch-only and not a write-surface violation, but the draft should use
`tempfile.TemporaryDirectory()` or delete its fixture so repeated runs do not accumulate
directories.

**O12-F4 (informational)** — the claim's counting command omits `-B`
(`python3 tools/harness/basename-couples-resolver.py --selftest`). That is safe for a
standalone script, but any local import would emit `__pycache__`; the shared
`PYTHONDONTWRITEBYTECODE=1` export covers it. Keep the export in the validation harness.

## 8. Limits / to-verify

- **Draft clauses could-not-evaluate**: no O01 bytes existed in the window. This is not a
  pass for the draft, and not a failure; it is an unrendered verdict.
- I did not execute `reports/round-43/run-validation.py` (absent; in-tree execution is
  forbidden by the round rules in any case).
- I did not inspect other seats' future `reports/round-43/**` outputs beyond the file list;
  any violation there is outside this seat's allowlist check (the rule permits those paths).
- Future integration (applying a corpus landing, filing `calib/` census) is the
  integrator's write; only the current tree was measured.
- The "prospective" class is the r42 successor's fifth class beyond the r39 policy's four
  (`reports/round-42/calib/basename-couples-policy-full.md` §2 + O10 §4); the r43 claim text
  says four classes. Whether that is a conflict or a naming shorthand is `to-verify` with
  the O scribe; it does not affect the wrapped-field read result.

## Appendix A — gate source (as run)

```python
#!/usr/bin/env python3
"""O12 negative-proof gate for the r43 basename-couples resolver draft.

Static (AST) write-surface scan + optional dynamic canary. Reads only.
Usage: python3 -B .scratch/o12-negative-gate.py TOOL.py [--dynamic]
"""
import ast, hashlib, os, subprocess, sys

ALLOWED_PREFIXES = ("reports/round-43/", "tools/harness/")
WRITE_METHODS = {"write_text", "write_bytes", "unlink", "mkdir", "touch", "rename", "replace", "rmdir"}
WRITE_OS = {"remove", "unlink", "rename", "replace", "rmdir", "makedirs", "mkdir"}


def calls(tree):
    for node in ast.walk(tree):
        if isinstance(node, ast.Call):
            yield node


def callee(node):
    f = node.func
    if isinstance(f, ast.Attribute):
        return f.attr
    if isinstance(f, ast.Name):
        return f.id
    return ""


def literal_target(node):
    if node.args:
        a = node.args[0]
        if isinstance(a, ast.Constant) and isinstance(a.value, str):
            return a.value
    return None


def scan(path):
    src = open(path, encoding="utf-8").read()
    tree = ast.parse(src, filename=path)
    findings = []
    has_dwb = "dont_write_bytecode" in src
    imports = sorted({n.names[0].name.split(".")[0] for n in ast.walk(tree)
                      if isinstance(n, ast.Import)} |
                     {n.module.split(".")[0] for n in ast.walk(tree)
                      if isinstance(n, ast.ImportFrom) and n.module})
    for node in calls(tree):
        name = callee(node)
        if name == "open":
            mode = ""
            if len(node.args) > 1 and isinstance(node.args[1], ast.Constant):
                mode = str(node.args[1].value)
            for kw in node.keywords:
                if kw.arg == "mode" and isinstance(kw.value, ast.Constant):
                    mode = str(kw.value.value)
            if any(ch in mode for ch in "wax+"):
                tgt = literal_target(node)
                ok = tgt is None or tgt.startswith(ALLOWED_PREFIXES)
                findings.append(("open", node.lineno, mode, tgt, "ALLOW" if ok else "VIOLATION"))
        elif name in WRITE_METHODS:
            tgt = literal_target(node)
            ok = tgt is None or tgt.startswith(ALLOWED_PREFIXES)
            findings.append(("method:" + name, node.lineno, "", tgt, "ALLOW" if ok else "VIOLATION"))
        elif name in WRITE_OS:
            tgt = literal_target(node)
            ok = tgt is None or tgt.startswith(ALLOWED_PREFIXES)
            findings.append(("os:" + name, node.lineno, "", tgt, "ALLOW" if ok else "VIOLATION"))
        elif name in {"system", "popen", "run", "call", "check_output", "check_call"}:
            findings.append(("exec:" + name, node.lineno, "", None, "REVIEW"))
        elif name in {"urlopen", "urlretrieve"}:
            findings.append(("net:" + name, node.lineno, "", None, "VIOLATION"))
    nonstd = [m for m in imports if m not in sys.stdlib_module_names and m not in {"__future__"}]
    print(f"FILE {path}")
    print(f"  sha256      {hashlib.sha256(src.encode()).hexdigest()}")
    print(f"  dont_write_bytecode {has_dwb}")
    print(f"  imports     {imports}")
    print(f"  non-stdlib  {nonstd or 'none'}")
    for f in findings:
        print("  %-16s line %-4d mode=%-3s target=%s -> %s" % f)
    if not findings:
        print("  write-calls none")
    violations = [f for f in findings if f[-1] == "VIOLATION"]
    print(f"  VERDICT {'FAIL' if violations or nonstd else 'PASS-static'}")
    return not violations and not nonstd


def manifest(roots):
    rows = {}
    for root in roots:
        for dp, dn, fn in os.walk(root):
            dn[:] = sorted(d for d in dn if d not in {"__pycache__", ".git"})
            for f in sorted(fn):
                p = os.path.join(dp, f)
                with open(p, "rb") as fh:
                    rows[p] = hashlib.sha256(fh.read()).hexdigest()
    return rows


def dynamic(tool):
    roots = ["corpus", "tools", "reports/round-19", "reports/round-27", "reports/round-28", "reports/round-42"]
    before = manifest(roots)
    st_before = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout
    runs = []
    for args in (["--selftest"], ["--census"]):
        p = subprocess.run([sys.executable, "-B", tool] + args, capture_output=True, text=True)
        runs.append((args, p.returncode, p.stdout.strip().splitlines()[-3:]))
    target = "corpus/knowledge/linguistics/phonetics-phonology.md"
    p = subprocess.run([sys.executable, "-B", tool, target], capture_output=True, text=True)
    runs.append(([target], p.returncode, p.stdout.strip().splitlines()))
    after = manifest(roots)
    st_after = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout
    changed = sorted(set(before) ^ set(after)) + sorted(k for k in before if k in after and before[k] != after[k])
    print("DYNAMIC")
    for args, rc, tail in runs:
        print(f"  run {args} rc={rc}")
        for line in tail:
            print(f"    | {line}")
    print(f"  tree-diff {changed or 'NO-DIFF'}")
    print(f"  git-status-diff {'SAME' if st_before == st_after else 'CHANGED'}")
    return not changed and st_before == st_after


if __name__ == "__main__":
    tool = sys.argv[1]
    ok = scan(tool)
    if "--dynamic" in sys.argv:
        ok = dynamic(tool) and ok
    raise SystemExit(0 if ok else 1)
```

## Appendix B — reproduction commands

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1

# 0. draft presence
find reports/round-43 -type f | sort
ls -l tools/harness/basename-couples-resolver.py

# 1. write-surface state
git status --porcelain
git diff --stat HEAD -- corpus tools reports/round-19 reports/round-27 reports/round-28
git status --porcelain --ignored -- corpus tools

# 2. baseline manifest (1212 files)
find corpus tools reports/round-19 reports/round-27 reports/round-28 \
     reports/round-39 reports/round-40 reports/round-42 -type f \
     -not -path '*/__pycache__/*' -print0 | sort -z | xargs -0 sha256sum

# 3. reference instrument + integrity
python3 -B tools/harness/couples-reference-extractor.py --selftest
python3 -B tools/harness/couples-reference-extractor.py --census
python3 -B tools/harness/couples-reference-extractor.py \
  corpus/knowledge/linguistics/phonetics-phonology.md

# 4. D1 single-line vs block read (throwaway, no writes)
python3 - <<'PY'
import re
text = open("corpus/knowledge/linguistics/phonetics-phonology.md", encoding="utf-8").read()
MD = re.compile(r"[A-Za-z0-9_./{},\-]+\.md")
m = re.search(r"^- couples:\s*(.*)$", text, re.M)
print("single-line:", MD.findall(m.group(1)))          # []
PY

# 5. gate (after O01 lands)
python3 -B .scratch/o12-negative-gate.py tools/harness/basename-couples-resolver.py --dynamic
```

## 9. Addendum at 2026-10-19T17:00:21Z — cross-seat convergence + fragment scan

The wave landed 20+ seat files between §0 and now, but the O01 draft never appeared:
`ls reports/round-43/op/O01-tool-draft.md` and `ls tools/harness/basename-couples-resolver.py`
both still return "No such file or directory" at 17:00:21Z. The draft-specific verdict in §0
therefore stands as `could-not-evaluate`.

### 9.1 Independent convergence (no coordination; separate seats, separate commands)

| Finding | Independent corroboration |
|---|---|
| `claims.json:27` "before" is stale; the r42 extractor is durable at HEAD | `reports/round-43/op/O02-controls.md:18`; `reports/round-43/op/O07-durability.md:30,482`; `reports/round-43/op/O10-census-artifact.md:14,586`; `reports/round-43/scout/K01-resolver-scout.md:18,135`; `reports/round-43/adj/A01-scope.md:176,208`; `reports/round-43/scribe/S01-integration-draft.md:44` |
| **O12-F1** count-only 4/4 is a false green; identity set must be asserted | `reports/round-43/op/O02-controls.md:42-45` ("Space-join and hyphen-aware join both return 4 tokens … only the latter returns the intended identities") and its run matrix `:383` ("4 tokens but the wrong 4 (`prosody.md`); an arity-only positive would be a false green"); `reports/round-43/op/O04-verify.md:345` cites this report's §5/O12-F1 |
| Draft absent → `could-not-evaluate`, not a pass | `reports/round-43/op/O04-verify.md:26,322`; `reports/round-43/scribe/S01-integration-draft.md:262-263` (quotes this report's conditional verdict: "live tree PASS, wrapped field PASS, r43 draft could-not-evaluate") |
| The real remaining delta is the disposition leg/four-class census, not D1 | `reports/round-43/op/O06-disposition-leg.md:32-33` (r42 `--census` has "no per-row mapping list, no reason code, no disposition, and no artifact file"); `reports/round-43/op/O04-verify.md:206-208` (r42 fails R6/R7, no ambiguous control); `reports/round-43/op/O05-traps.md:329` (C7 host fails: totals-only) |

A01 (`adj/A01-scope.md:176`) records the route disagreement (K01/O12 vs O07) as an unresolved
**operability design fork**, not scope bleed — matching §7 O12-F2's "takes no position on
which route".

### 9.2 Static scan of the landed draft fragments

Three fenced `python` blocks exist in the landed O-seat files (O02 ×1, O06 ×2; O10 has none).
Extracted to `.scratch/o12-frags/`, all parse, and the §4 gate reports:

```
O02-controls-1.py     SYNTAX-OK 209 lines   write-calls none   non-stdlib none   PASS-static
O06-disposition-leg-1.py  SYNTAX-OK 32 lines   write-calls none   non-stdlib none   PASS-static
O06-disposition-leg-2.py  SYNTAX-OK 26 lines   write-calls none   non-stdlib none   PASS-static
```

Gate-scope note: the static verdict enforces write targets and stdlib-only imports;
`sys.dont_write_bytecode` is printed as a separate field because these are fragments, not a
host script. The host (O01) must still carry it (W3); the fragments introduce no write surface
into whatever host they are pasted into.

### 9.3 Effect on the verdict

None of the above changes §0: live tree PASS, reference instrument PASS, wrapped field PASS by
identity, **r43 draft could-not-evaluate**. It does strengthen O12-F1 and O12-F2 from
single-seat observations to independently reproduced findings. If O01 lands after this cut,
run §6's gate; if the round proceeds without it, claim O has no draft to score and its
thresholds are unmet by absence, not by a failed test. The corrected census artifact
(`reports/round-43/calib/`) is likewise still absent at 17:00:21Z.
