- Seat: O06 | executor | claim O | date 2026-10-19 | baseline 139e3b6

# O06 — negative-control spec for the lessons reconciliation (claim O)

Mission: at least three controls for the lessons-index reconciliation — a fake
unindexed file must fail C31, a row naming a nonexistent file must fail, a prose
count lie must fail C34b — with expected codes and how the integrator runs them
post-edit.

Delivered: **11 controls (C0–C9), all executed and green against the round-33
tree before any integration edit** (`CONTROLS OK: 11/11`). The harness is
embedded verbatim in §5; it writes only under `.scratch/`, so no filed byte is
touched by running it.

## 1. The verdict surface under control

`reports/round-25/audit/c31-lessons-index-audit.py` is read-only and stdlib-only
("Opens no file for writing: the receipt is the caller's stdout redirect",
:17–18), so a control can be run against a *copy* of the partition without
altering the tool.

| check | finding id | class | trigger |
|---|---|---|---|
| `C31_index_rows_eq_files` | `C31-1` | `unindexed-file` | file on disk with no README row (:201–203) |
| `C31_index_rows_eq_files` | `C31-2` | `ghost-row` | README row naming no file on disk (:204–206) |
| `C31_index_rows_eq_files` | `C31-3` | `duplicate-row` | two rows for one file (:208–210) |
| `C32_owners_resolve` | `C32-1` | `unresolvable-owner` | queue-row owner that is not a live path, `operator`, or a resolving `round-N` (:213–227) |
| `C33_formats_documented` | `C33-1` | `undocumented-format` | live format class not named in the README (:229–243) |
| `C34_pins_rederived` | `C34-1` | `pin-drift` | `bytes`/`lines`/`sha8` cell ≠ live bytes (:245–266) |
| `C34c_shape_cells_rederived` | `C34-3` | `shape-cell-drift` | `format` or `contract` cell ≠ live bytes (:268–291) |
| `C34b_prose_arithmetic` | `C34-2` | `prose-arithmetic-drift` | stated row/file/queue counts ≠ measurement (:293–317) |

Exit contract — **two different exits, only one is a verdict**:

- plain run: `return 0 if not res["findings"] else 1` (:460) — the claim-O
  counting command reads this.
- `--json` run: `return 0` unconditionally (:445–447) — an integrator who wires
  the `--json` exit code into acceptance reads green on a red index. Control C8
  pins this down.

## 2. Method: sandbox copy plus a delta model

Each control rebuilds a disposable root at `.scratch/o06-controls/` that mirrors
the tree: `corpus/lessons` and `reports/round-25/audit` are **copied** (hence
mutable), every other entry is **symlinked**, so owner paths such as
`corpus/QUALITY.md` and `corpus/knowledge/synthesis/worldbible-integration-contract.md`
resolve exactly as they do live and the C32 leg does not go spuriously red. The
tool derives its root from its own `__file__` (`ROOT = … "..", "..", ".."`, :34),
so the copy at `.scratch/o06-controls/reports/round-25/audit/` audits the sandbox
partition, not the repo.

Two properties make the expectations trustworthy:

- **C0 identity control.** The unmutated copy must reproduce the live run's
  findings *exactly* (full finding list compared, not just ids). Without it, a
  red control could be blamed on the mutation when it is really an artefact of
  the mirror.
- **Delta expectations.** Every negative control must add **exactly one** finding
  to the live baseline measured in the same run and flip **exactly one** check
  red. The baseline at the round-33 tree is already red (`C31-1`, `C34-2`), so an
  absolute expectation would either be wrong now or wrong after integration; the
  delta form is valid in both states. Post-edit the baseline is green and each
  control's expected finding set collapses to the single new id (see §6).

## 3. The controls

| # | mutation applied to the sandbox copy | expected finding (class) | expected check | expected exit |
|---|---|---|---|---|
| C0 | none (identity) | baseline only: `C31-1`, `C34-2` | baseline failing set | baseline (1 now) |
| C1 | create `corpus/lessons/round-99-probe.md` | `C31-1` `unindexed-file`, detail names `round-99-probe.md` | `C31` FAIL | 1 |
| C2 | append a row for `corpus/lessons/round-98-probe.md` (no such file) | `C31-2` `ghost-row`, detail `['round-98-probe.md']` | `C31` FAIL | 1 |
| C3 | append a second row for the existing `round-15.md` | `C31-3` `duplicate-row`, detail `['round-15.md']` | `C31` FAIL | 1 |
| C4a | rewrite the table prose to `measured+1` rows and files | `C34-2` `prose-arithmetic-drift`, detail key `table_rows_vs_files` | `C34b` FAIL | 1 |
| C4b | rewrite the queue prose count to `stated+1` | `C34-2` `prose-arithmetic-drift`, detail key `queue_rows` | `C34b` FAIL | 1 |
| C5 | mechanically reconcile: one generated row per unindexed file + true counts | none (findings `[]`) | all PASS | 0 |
| C6 | corrupt one row's `sha8` (`round-15.md` → `sha8=00000000`) | `C34-1` `pin-drift`, detail names `sha8` | `C34` FAIL | 1 |
| C7 | corrupt one row's `format` cell (`gate-keeper` → `plain`) | `C34-3` `shape-cell-drift`, detail names `format` | `C34c` FAIL | 1 |
| C8 | create the fake unindexed file, then read **both** exits | `C31-1`; `--json` exit is **0** while the plain exit is **1** | `C31` FAIL | plain 1, json 0 |
| C9 | apply **O01's seven drafted rows** verbatim + the arithmetic they imply | none (findings `[]`) | all PASS | 0 |

C4a/C4b derive their lie from the measurement (`measured+1`, `stated+1`) rather
than hardcoding a number, so the lie cannot become true after the index changes.
C5 proves the after_required state is *reachable*: a mechanically reconciled copy
reaches zero findings, i.e. no check in the set is unsatisfiable. C9 is the
end-to-end control on the sibling draft — it consumes
`reports/round-33/op/O01-row-drafts.md` (present at my seat close) and asserts the
drafted set equals the missing set before applying it.

## 4. Verified run at the round-33 tree (pre-integration)

```
$ export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
$ python3 -B .scratch/o06-controls.py --receipt .scratch/o06-receipt.json
live baseline: exit=1 checks_failing=['C31_index_rows_eq_files', 'C34b_prose_arithmetic'] findings=['C31-1', 'C34-2']
[PASS] C0 sandbox identity (unmutated copy == live result): exit=1 checks_failing=['C31_index_rows_eq_files', 'C34b_prose_arithmetic'] findings=['C31-1', 'C34-2']
[PASS] C1 fake unindexed file -> C31-1 unindexed-file: exit=1 checks_failing=['C31_index_rows_eq_files', 'C34b_prose_arithmetic'] findings=['C31-1', 'C34-2']
[PASS] C2 ghost row (nonexistent file) -> C31-2 ghost-row: exit=1 checks_failing=['C31_index_rows_eq_files', 'C34b_prose_arithmetic'] findings=['C31-1', 'C31-2', 'C34-2']
[PASS] C3 duplicate row -> C31-3 duplicate-row: exit=1 checks_failing=['C31_index_rows_eq_files', 'C34b_prose_arithmetic'] findings=['C31-1', 'C31-3', 'C34-2']
[PASS] C4a prose table-count lie -> C34-2 prose-arithmetic-drift: exit=1 checks_failing=['C31_index_rows_eq_files', 'C34b_prose_arithmetic'] findings=['C31-1', 'C34-2']
[PASS] C4b prose queue-count lie -> C34-2 (queue_rows detail): exit=1 checks_failing=['C31_index_rows_eq_files', 'C34b_prose_arithmetic'] findings=['C31-1', 'C34-2']
       (C5 reconciled 7 missing row(s): ['round-26.md', 'round-27.md', 'round-28.md', 'round-29.md', 'round-30.md', 'round-31.md', 'round-32.md'])
[PASS] C5 reachability (reconciled copy) -> zero findings, exit 0: exit=0 checks_failing=[] findings=[]
[PASS] C6 stale sha8 pin -> C34-1 pin-drift: exit=1 checks_failing=['C31_index_rows_eq_files', 'C34_pins_rederived', 'C34b_prose_arithmetic'] findings=['C31-1', 'C34-1', 'C34-2']
[PASS] C7 stale format cell -> C34-3 shape-cell-drift: exit=1 checks_failing=['C31_index_rows_eq_files', 'C34b_prose_arithmetic', 'C34c_shape_cells_rederived'] findings=['C31-1', 'C34-2', 'C34-3']
[PASS] C8 --json exit is not a verdict (must be 0 while plain exit is 1): exit=1 checks_failing=['C31_index_rows_eq_files', 'C34b_prose_arithmetic'] findings=['C31-1', 'C34-2']
       (C9 applied 7 drafted row(s) from reports/round-33/op/O01-row-drafts.md)
[PASS] C9 O01 draft rows applied -> zero findings, exit 0: exit=0 checks_failing=[] findings=[]

CONTROLS OK: 11/11 controls behaved as specified
receipt: .scratch/o06-receipt.json
```

Observed details worth keeping (from the receipt):

- C1/C8 `C31-1` detail `[…'round-32.md', 'round-99-probe.md']`; C2 `C31-2` detail
  `['round-98-probe.md']`; C3 `C31-3` detail `['round-15.md']`.
- C4a `C34-2` detail `{"table_rows_vs_files": {"stated": [99, 99], "measured": [26, 33]}}`;
  C4b `C34-2` detail `{"queue_rows": {"stated": 99, "measured": 49}}`.
- C6 `C34-1` detail `[["round-15.md", "sha8", "00000000", "13e17f0e"]]`;
  C7 `C34-3` detail `[["round-15.md", "format", "plain", "gate-keeper"]]`.
- C5 and C9 both reached `findings: []`, exit 0 — the reconciliation target is
  reachable and O01's drafted cells satisfy every check including C34/C34c.

Digests at this run: harness
`1263f15686ce2662669e8a2b9d21222b2424d117a7e057fa72085bc8262a0d2d`, receipt
`9e500c14e22bafdfd06d5630fb53f651ae4bacbb695c8f1e63aa7cd2b6024549` (both under
`.scratch/`, transient; the harness bytes are embedded in §5 and its digest is
the extraction check).

## 5. The harness (embedded verbatim — extract, do not retype)

Extraction recipe in §6 verifies the digest before running. Exactly one
`python` fence appears in this file.

```python
#!/usr/bin/env python3
"""O06 negative controls for the round-33 lessons reconciliation (claim O).

Read-only w.r.t. the repo: builds a disposable sandbox under .scratch that
mirrors the tree -- `corpus/lessons` and `reports/round-25/audit` are copied
and therefore mutable; every other entry is symlinked, so owner paths resolve
exactly as they do live. Each control then mutates the copy and runs the
round-25 C31..C34 audit against it. Nothing outside .scratch is written.

Every expectation is a DELTA from the live baseline measured in the same run,
so the harness is valid both before integration (baseline red) and after
(baseline green): a control passes only if its mutation adds exactly the
finding it is supposed to add, and nothing else changes.

    export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
    python3 -B .scratch/o06-controls.py
    python3 -B .scratch/o06-controls.py --receipt .scratch/o06-receipt.json
"""

import glob
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys

REL = "reports/round-25/audit/c31-lessons-index-audit.py"
ROW_RE = re.compile(r"^\|\s*`?corpus/lessons/([A-Za-z0-9_.-]+\.md)`?\s*\|")
CONTRACT_KEYS = ("source:", "verified-at:", "recheck:", "scope:")


def find_repo():
    env = os.environ.get("O06_REPO")
    if env:
        return os.path.abspath(env)
    p = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"], capture_output=True, text=True
    )
    if p.returncode == 0 and p.stdout.strip():
        return p.stdout.strip()
    raise SystemExit("could not locate the repo root; set O06_REPO")


REPO = find_repo()
SBX = os.path.join(REPO, ".scratch", "o06-controls")
AUDIT = os.path.join(SBX, REL)
README = os.path.join(SBX, "corpus", "lessons", "README.md")
ENV = dict(os.environ, PYTHONDONTWRITEBYTECODE="1")


def build_sandbox():
    if os.path.exists(SBX):
        shutil.rmtree(SBX)
    os.makedirs(os.path.join(SBX, "corpus"))
    shutil.copytree(
        os.path.join(REPO, "corpus", "lessons"),
        os.path.join(SBX, "corpus", "lessons"),
    )
    os.makedirs(os.path.join(SBX, "reports", "round-25"))
    shutil.copytree(
        os.path.join(REPO, "reports", "round-25", "audit"),
        os.path.join(SBX, "reports", "round-25", "audit"),
    )
    for name in sorted(os.listdir(os.path.join(REPO, "reports", "round-25"))):
        if name in ("audit", "__pycache__"):
            continue
        os.symlink(
            os.path.join(REPO, "reports", "round-25", name),
            os.path.join(SBX, "reports", "round-25", name),
        )
    for name in sorted(os.listdir(os.path.join(REPO, "reports"))):
        if name == "round-25":
            continue
        os.symlink(
            os.path.join(REPO, "reports", name), os.path.join(SBX, "reports", name)
        )
    # corpus/lessons is the mutable copy; the rest of corpus/ is mirrored so
    # owner paths (corpus/QUALITY.md, corpus/knowledge/..., corpus/README.md)
    # resolve exactly as they do live -- the C32 leg reads them.
    for name in sorted(os.listdir(os.path.join(REPO, "corpus"))):
        if name == "lessons":
            continue
        os.symlink(
            os.path.join(REPO, "corpus", name), os.path.join(SBX, "corpus", name)
        )
    for name in sorted(os.listdir(REPO)):
        if name in ("corpus", "reports", ".git", ".scratch"):
            continue
        os.symlink(os.path.join(REPO, name), os.path.join(SBX, name))


def run(audit_path):
    """Return (json_result, plain_exit_code, json_exit_code)."""
    j = subprocess.run(
        [sys.executable, "-B", audit_path, "--json"],
        capture_output=True, text=True, env=ENV,
    )
    plain = subprocess.run(
        [sys.executable, "-B", audit_path], capture_output=True, text=True, env=ENV
    )
    return json.loads(j.stdout), plain.returncode, j.returncode


def readme_text():
    with open(README, encoding="utf-8") as fh:
        return fh.read()


def write_readme(text):
    with open(README, "w", encoding="utf-8") as fh:
        fh.write(text)


def census_rows():
    """Independent census of the sandbox partition (does not import the tool)."""
    out = {}
    for path in sorted(glob.glob(os.path.join(SBX, "corpus", "lessons", "*.md"))):
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        with open(path, "rb") as fh:
            digest = hashlib.sha256(fh.read()).hexdigest()
        if re.search(r"^## Fragment index\s*$", text, re.M):
            fmt = "fragment-index"
        elif re.search(r"^## Gate\s*$", text, re.M):
            fmt = "gate-keeper"
        else:
            fmt = "plain"
        n = sum(1 for k in CONTRACT_KEYS if re.search(rf"^{k}", text, re.M))
        out[os.path.basename(path)] = {
            "format": fmt,
            "contract": f"{n}/4",
            "bytes": os.path.getsize(path),
            "lines": len(text.splitlines()),
            "sha8": digest[:8],
        }
    return out


def by_id(res):
    return {f["id"]: f for f in res["findings"]}


def fails_of(res):
    return sorted(k for k, v in res["checks"].items() if not v)


def ids_of(res):
    return sorted(f["id"] for f in res["findings"])


BASELINE = {}
RESULTS = []


def control(name, expect, fn):
    """expect: rc, add_ids (findings the mutation must add), add_fails (checks
    it must flip red), exact (full findings list; replaces the delta model),
    classes (id -> class), detail_has (id -> substring)."""
    build_sandbox()  # every control starts from the same pristine sandbox
    out = fn()
    if out == "SKIP":
        return "SKIP"
    res, rc, json_rc = out
    got = by_id(res)
    ids, fails = ids_of(res), fails_of(res)
    if expect.get("exact") is not None:
        want_ids = sorted(f["id"] for f in expect["exact"])
        want_fails = sorted(expect["want_fails"])
        ok = rc == expect["rc"] and ids == want_ids and res["findings"] == expect["exact"]
    else:
        want_ids = sorted(set(BASELINE["ids"]) | set(expect.get("add_ids", [])))
        want_fails = sorted(set(BASELINE["fails"]) | set(expect.get("add_fails", [])))
        want_rc = 1 if want_ids else 0
        ok = rc == want_rc and ids == want_ids and fails == want_fails
    ok = ok and all(got[i]["class"] == c for i, c in expect.get("classes", {}).items())
    ok = ok and all(
        str(d) in json.dumps(got[i]["detail"])
        for i, d in expect.get("detail_has", {}).items()
    )
    if expect.get("json_rc") is not None:
        ok = ok and json_rc == expect["json_rc"]
    RESULTS.append(
        {
            "control": name,
            "ok": bool(ok),
            "exit": rc,
            "json_exit": json_rc,
            "expected_ids": want_ids,
            "observed_ids": ids,
            "expected_failing_checks": want_fails,
            "observed_failing_checks": fails,
            "observed_details": {i: got[i]["detail"] for i in ids},
        }
    )
    print(
        f"[{'PASS' if ok else 'FAIL'}] {name}: exit={rc} "
        f"checks_failing={fails} findings={ids}"
    )
    return res


def main():
    receipt_path = None
    if "--receipt" in sys.argv:
        receipt_path = sys.argv[sys.argv.index("--receipt") + 1]

    build_sandbox()
    live_res, live_rc, _ = run(os.path.join(REPO, REL))
    BASELINE["ids"] = ids_of(live_res)
    BASELINE["fails"] = fails_of(live_res)
    print(
        f"live baseline: exit={live_rc} checks_failing={BASELINE['fails']} "
        f"findings={BASELINE['ids']}"
    )

    # C0 -- identity: the sandbox harness must not change audit semantics.
    control(
        "C0 sandbox identity (unmutated copy == live result)",
        {"rc": live_rc, "exact": live_res["findings"], "want_fails": BASELINE["fails"]},
        lambda: run(AUDIT),
    )

    # C1 -- fake unindexed file must fail C31 (unindexed-file).
    def c1():
        with open(
            os.path.join(SBX, "corpus", "lessons", "round-99-probe.md"), "w",
            encoding="utf-8",
        ) as fh:
            fh.write("# round-99 probe\n\nsource: probe\n")
        return run(AUDIT)

    control(
        "C1 fake unindexed file -> C31-1 unindexed-file",
        {"add_ids": ["C31-1", "C34-2"],
         "add_fails": ["C31_index_rows_eq_files", "C34b_prose_arithmetic"],
         "classes": {"C31-1": "unindexed-file", "C34-2": "prose-arithmetic-drift"},
         "detail_has": {"C31-1": "round-99-probe.md"}},
        c1,
    )

    # C2 -- a row naming a file that does not exist must fail C31 (ghost-row).
    def c2():
        write_readme(
            readme_text()
            + "\n| `corpus/lessons/round-98-probe.md` | plain | 1/4 | — | "
            "`corpus/lessons/README.md` | bytes=1 lines=1 sha8=deadbeef |\n"
        )
        return run(AUDIT)

    control(
        "C2 ghost row (nonexistent file) -> C31-2 ghost-row",
        {"add_ids": ["C31-2", "C34-2"],
         "add_fails": ["C31_index_rows_eq_files", "C34b_prose_arithmetic"],
         "classes": {"C31-2": "ghost-row", "C34-2": "prose-arithmetic-drift"},
         "detail_has": {"C31-2": "round-98-probe.md"}},
        c2,
    )

    # C3 -- a second row for an already-indexed file must fail C31 (duplicate).
    def c3():
        text = readme_text()
        row = [l for l in text.splitlines() if ROW_RE.match(l) and "round-15.md" in l][0]
        write_readme(text + "\n" + row + "\n")
        return run(AUDIT)

    control(
        "C3 duplicate row -> C31-3 duplicate-row",
        {"add_ids": ["C31-3", "C34-2"],
         "add_fails": ["C31_index_rows_eq_files", "C34b_prose_arithmetic"],
         "classes": {"C31-3": "duplicate-row", "C34-2": "prose-arithmetic-drift"},
         "detail_has": {"C31-3": "round-15.md"}},
        c3,
    )

    # C4a -- a lying table count must fail C34b. The lie is derived from an
    # independent census (measured + 1), so it cannot accidentally be true.
    def c4a():
        text = readme_text()
        n_files = len(census_rows())
        n_rows = sum(1 for l in text.splitlines() if ROW_RE.match(l))
        new, n = re.subn(
            r"\*\*Rows:\s*\d+\.\s*Files:\s*\d+\.\*\*",
            f"**Rows: {n_rows + 1}. Files: {n_files + 1}.**", text, count=1,
        )
        assert n == 1, f"table-prose regex fired {n} times"
        write_readme(new)
        return run(AUDIT)

    control(
        "C4a prose table-count lie -> C34-2 prose-arithmetic-drift",
        {"add_ids": ["C34-2"], "add_fails": ["C34b_prose_arithmetic"],
         "classes": {"C34-2": "prose-arithmetic-drift"},
         "detail_has": {"C34-2": "table_rows_vs_files"}},
        c4a,
    )

    # C4b -- a lying queue-row count must fail C34b too. Same derivation: the
    # stated count is bumped by one, which the measurement cannot match.
    def c4b():
        text = readme_text()
        m = re.search(r"Rows:\s*\*\*(\d+)\*\*", text)
        assert m, "no queue-count prose line to lie about"
        lie = int(m.group(1)) + 1
        new, n = re.subn(r"Rows:\s*\*\*\d+\*\*", f"Rows: **{lie}**", text, count=1)
        assert n == 1, f"queue-prose regex fired {n} times"
        write_readme(new)
        return run(AUDIT)

    control(
        "C4b prose queue-count lie -> C34-2 (queue_rows detail)",
        {"add_ids": ["C34-2"], "add_fails": ["C34b_prose_arithmetic"],
         "classes": {"C34-2": "prose-arithmetic-drift"},
         "detail_has": {"C34-2": "queue_rows"}},
        c4b,
    )

    # C5 -- reachability: the after_required state must be attainable, and the
    # delivered state must be green. Pre-integration the copy is reconciled
    # mechanically (rows generated from an independent census); post-integration
    # the unmutated copy already is the target state.
    def c5():
        rows = census_rows()
        text = readme_text()
        lines = text.splitlines()
        indexed = {ROW_RE.match(l).group(1) for l in lines if ROW_RE.match(l)}
        missing = sorted(set(rows) - indexed)
        if missing:
            last = max(i for i, l in enumerate(lines) if ROW_RE.match(l))
            new_rows = [
                f"| `corpus/lessons/{n}` | {rows[n]['format']} | {rows[n]['contract']} | — | "
                f"`corpus/lessons/README.md` | bytes={rows[n]['bytes']} "
                f"lines={rows[n]['lines']} sha8={rows[n]['sha8']} |"
                for n in missing
            ]
            lines = lines[: last + 1] + new_rows + lines[last + 1:]
            text = "\n".join(lines) + "\n"
            text, a = re.subn(
                r"\*\*Rows:\s*\d+\.\s*Files:\s*\d+\.\*\*",
                f"**Rows: {len(indexed) + len(missing)}. Files: {len(rows)}.**",
                text, count=1,
            )
            assert a == 1, f"table-prose regex fired {a} times"
            write_readme(text)
            print(f"       (C5 reconciled {len(missing)} missing row(s): {missing})")
        else:
            print("       (C5: index already complete; positive control on delivered state)")
        return run(AUDIT)

    control(
        "C5 reachability (reconciled copy) -> zero findings, exit 0",
        {"rc": 0, "exact": [], "want_fails": []},
        c5,
    )

    # C6 -- a stale sha8 pin must fail C34.
    def c6():
        text = readme_text()
        row = [l for l in text.splitlines() if ROW_RE.match(l) and "round-15.md" in l][0]
        bad = re.sub(r"sha8=[0-9a-f]+", "sha8=00000000", row, count=1)
        write_readme(text.replace(row, bad, 1))
        return run(AUDIT)

    control(
        "C6 stale sha8 pin -> C34-1 pin-drift",
        {"add_ids": ["C34-1"], "add_fails": ["C34_pins_rederived"],
         "classes": {"C34-1": "pin-drift"}, "detail_has": {"C34-1": "sha8"}},
        c6,
    )

    # C7 -- a stale format cell must fail C34c.
    def c7():
        text = readme_text()
        row = [l for l in text.splitlines() if ROW_RE.match(l) and "round-15.md" in l][0]
        bad = re.sub(r"\| gate-keeper \|", "| plain |", row, count=1)
        assert bad != row, "round-15.md row is not gate-keeper; pick another probe row"
        write_readme(text.replace(row, bad, 1))
        return run(AUDIT)

    control(
        "C7 stale format cell -> C34-3 shape-cell-drift",
        {"add_ids": ["C34-3"], "add_fails": ["C34c_shape_cells_rederived"],
         "classes": {"C34-3": "shape-cell-drift"}, "detail_has": {"C34-3": "format"}},
        c7,
    )

    # C8 -- the trap the integrator must not fall into: `--json` always exits 0
    # (tool line 446), so only the plain run's exit code is a verdict.
    def c8():
        with open(
            os.path.join(SBX, "corpus", "lessons", "round-99-probe.md"), "w",
            encoding="utf-8",
        ) as fh:
            fh.write("# round-99 probe\n\nsource: probe\n")
        return run(AUDIT)

    control(
        "C8 --json exit is not a verdict (must be 0 while plain exit is 1)",
        {"add_ids": ["C31-1", "C34-2"],
         "add_fails": ["C31_index_rows_eq_files", "C34b_prose_arithmetic"],
         "classes": {"C31-1": "unindexed-file", "C34-2": "prose-arithmetic-drift"},
         "json_rc": 0},
        c8,
    )

    # C9 -- end-to-end control on the sibling draft: applying O01's seven
    # drafted rows (plus the arithmetic they imply) must take the audit green.
    # Skips only when the draft is absent, and says so.
    def c9():
        draft = os.path.join(REPO, "reports", "round-33", "op", "O01-row-drafts.md")
        if not os.path.exists(draft):
            return "SKIP"
        with open(draft, encoding="utf-8") as fh:
            draft_rows = [l for l in fh.read().splitlines() if ROW_RE.match(l)]
        rows = census_rows()
        text = readme_text()
        lines = text.splitlines()
        indexed = {ROW_RE.match(l).group(1) for l in lines if ROW_RE.match(l)}
        missing = sorted(set(rows) - indexed)
        drafted = sorted(ROW_RE.match(l).group(1) for l in draft_rows)
        if not missing:
            print("       (C9: drafts already applied; positive control on delivered state)")
            return run(AUDIT)
        assert drafted == missing, f"C9 draft set {drafted} != missing set {missing}"
        last = max(i for i, l in enumerate(lines) if ROW_RE.match(l))
        lines = lines[: last + 1] + draft_rows + lines[last + 1:]
        text = "\n".join(lines) + "\n"
        text, a = re.subn(
            r"\*\*Rows:\s*\d+\.\s*Files:\s*\d+\.\*\*",
            f"**Rows: {len(indexed) + len(missing)}. Files: {len(rows)}.**",
            text, count=1,
        )
        assert a == 1, f"table-prose regex fired {a} times"
        write_readme(text)
        print(f"       (C9 applied {len(draft_rows)} drafted row(s) from {os.path.relpath(draft, REPO)})")
        return run(AUDIT)

    skipped = []
    res9 = control(
        "C9 O01 draft rows applied -> zero findings, exit 0",
        {"rc": 0, "exact": [], "want_fails": []},
        c9,
    )
    if res9 == "SKIP":
        RESULTS.pop()
        skipped.append("C9 (reports/round-33/op/O01-row-drafts.md absent)")
        print("[SKIP] C9 O01 draft rows applied -> zero findings, exit 0 (draft absent)")

    bad = [r for r in RESULTS if not r["ok"]]
    print(
        f"\nCONTROLS {'OK' if not bad else 'FAILED'}: "
        f"{len(RESULTS) - len(bad)}/{len(RESULTS)} controls behaved as specified"
        + (f"; skipped: {skipped}" if skipped else "")
    )
    if receipt_path:
        with open(receipt_path, "w", encoding="utf-8") as fh:
            json.dump(
                {"baseline": BASELINE, "controls": RESULTS,
                 "skipped": skipped, "all_ok": not bad},
                fh, indent=1, sort_keys=True,
            )
        print(f"receipt: {receipt_path}")
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
```

## 6. How the integrator runs them post-edit

```sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1

# 1. extract the harness from this fragment (exactly one ```python block)
python3 - <<'PY'
import pathlib, re
t = pathlib.Path("reports/round-33/op/O06-controls.md").read_text(encoding="utf-8")
blocks = re.findall(r"```python\n(.*?)\n```", t, re.S)
assert len(blocks) == 1, f"expected 1 python block, found {len(blocks)}"
pathlib.Path(".scratch/o06-controls.py").write_text(blocks[0] + "\n", encoding="utf-8")
PY

# 2. digest check before running anything
sha256sum .scratch/o06-controls.py
# must be 1263f15686ce2662669e8a2b9d21222b2424d117a7e057fa72085bc8262a0d2d

# 3. run the controls (exit 0 iff every control behaved as specified)
python3 -B .scratch/o06-controls.py --receipt .scratch/o06-receipt.json
echo "controls exit=$?"
```

Expected post-edit shape (**expected**, derived from the delta model — the
post-edit run itself is the integrator's evidence, not mine):

| control | expected findings | expected plain exit |
|---|---|---|
| baseline (first line printed) | `[]` — the reconciliation landed | 0 |
| C0 | `[]` | 0 |
| C1 | `['C31-1']` | 1 |
| C2 | `['C31-2']` | 1 |
| C3 | `['C31-3']` | 1 |
| C4a | `['C34-2']` | 1 |
| C4b | `['C34-2']` | 1 |
| C5 | `[]` (prints "index already complete; positive control on delivered state") | 0 |
| C6 | `['C34-1']` | 1 |
| C7 | `['C34-3']` | 1 |
| C8 | `['C31-1']`, `json_exit=0` | 1 |
| C9 | `[]` (prints "drafts already applied") | 0 |
| summary | `CONTROLS OK: 11/11 controls behaved as specified` | 0 |

Interpretation rules:

1. **Read the baseline line first.** C4a/C4b are discriminating only when the
   baseline is green; if the baseline is still red on `C34b`, the queue prose
   was not reconciled and the control cannot isolate its own mutation.
2. **Only the plain exit code is a verdict** (C8; tool :445–447).
3. **C9 is the draft's end-to-end check.** If it skips, O01's fragment is not in
   the tree at run time; that is a gap to report, not a pass.
4. A control that reports a *different* finding set than the table above means
   either the mutation no longer applies (e.g. C7's probe row `round-15.md` was
   re-classified, C4b's queue prose line moved) or a real regression — both need
   the receipt's `observed_details` before judging.
5. The harness writes only under `.scratch/o06-controls/`; a non-empty
   `git status --porcelain` beyond the expected integration edits after a run
   means the sandbox escaped its root.

## 7. Cross-checks against sibling fragments

- **O01's drafted rows** (the artifact C9 applies): an independent census
  (separate script, `glob` + `hashlib` + the README §3 markers) found **0 pin
  mismatches** on `bytes`/`lines`/`sha8` across all seven rows, and every
  `format`/`contract` cell matches (rounds 29/30 = `3/4`, the rest `4/4`).
- **O04** classifies the same seven as `gate-keeper` 7/7
  (`reports/round-33/op/O04-format-checks.md:32–40`), consistent with the
  harness's own census and with C5/C9 going green when rows carry those cells.
- **K02** confirms the unindexed set is exactly `round-26.md … round-32.md`
  (`reports/round-33/op/K02-lessons-census.md:32–36`), which is the set C1/C5/C9
  key off.
- **O07's** baseline receipt records the same pre-edit state (`C31-1`, `C34-2`,
  c31 selftest `28/28`) — my baseline line reproduces it.

## 8. Limits and honest notes

- The controls cover the **row side** of the reconciliation (rows, pins, shape
  cells, table prose) plus the **queue-side arithmetic** (C4b). They do not
  verify the content of O02's new queue rows; that side's acceptance is the same
  counting command — plain audit exit 0 — with C32/C33 covering owner
  resolution and format documentation.
- C5's mechanically generated rows use `—` in the questions column; they exist to
  prove reachability, not to be applied. C9 is the control that applies the real
  draft.
- Two harness bugs were found and fixed during development (mutations leaking
  between controls; a duplicated mutation call) — recorded here because a
  control suite that silently re-runs its mutation twice is exactly the class of
  defect these controls exist to catch. The embedded harness is the fixed
  version, digest-pinned in §6.

## Owed: none

## Citations

- `reports/round-25/audit/c31-lessons-index-audit.py:17-18` (read-only claim),
  `:34` (ROOT from `__file__`), `:42` (ROW_RE), `:45` (CELL_RE), `:101` (partition
  glob), `:197-210` (C31 + C31-1/2/3), `:213-227` (C32/C32-1), `:229-243`
  (C33/C33-1), `:245-266` (C34/C34-1), `:268-291` (C34c/C34-3), `:293-317`
  (C34b/C34-2), `:445-447` (`--json` always exits 0), `:460` (plain exit).
- `corpus/lessons/README.md:97` (`**Rows: 26. Files: 26.**`),
  `:207` (`- Rows: **49**.`), `:95` (last table row at the baseline).
- Command: `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` at
  baseline 139e3b6 → exit 1, `lesson files: 33`, `index rows: 26`,
  `FAIL C31_index_rows_eq_files`, `FAIL C34b_prose_arithmetic`, findings
  `C31-1` (seven files), `C34-2` `{stated [26,26], measured [26,33]}`.
- Command: `python3 -B reports/round-25/audit/c31-lessons-index-audit.py --selftest`
  → exit 0, `SELFTEST OK: 28/28 checks passed`.
- Command: `python3 -B .scratch/o06-controls.py --receipt .scratch/o06-receipt.json`
  → `CONTROLS OK: 11/11`, exit 0 (full output in §4).
- Command: independent census + O01 row comparison (`glob`/`hashlib` script) →
  `O01 row count: 7`, `pin mismatches vs independent census: NONE`, all
  format/contract cells `ok`.
- `reports/round-33/op/O01-row-drafts.md` (seven drafted rows consumed by C9).
- `reports/round-33/op/O04-format-checks.md:32-40` (7/7 gate-keeper).
- `reports/round-33/op/K02-lessons-census.md:32-36` (the seven unindexed files).
- `reports/round-33/op/O07-baseline-receipt.md:34,52-60` (pre-edit baseline and
  c31 selftest consistency).
- `reports/round-33/claims.json` (claim O, counting commands and thresholds).
- `git status --porcelain` after every harness run: only `LOG.md` (parent's),
  `REGIMEN.md` and `reports/round-33/` — no filed byte written by O06.

## Integrator re-run receipt (2026-10-19T06:4xZ, post-reconciliation)

The harness was re-run by the round-33 integrator against the delivered
(reconciled, green) tree after the O02 delta landed. Result: **CONTROLS OK:
11/11** (`.scratch/o06-receipt.json`, window 2026-10-19T06:4xZ;
`TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`).

**Instrument repair, recorded per append-only discipline.** Four expectation
entries were amended — C1, C2, C3, C8 — each gaining the `C34-2`
co-finding and the `C34b_prose_arithmetic` failing check. The mid-wave run
recorded above executed while the index was still red, so the baseline
carried `C34-2` already and the coupling stayed invisible in the delta; on
the delivered green index every row/file-count mutation correctly co-fires
`C34b` (stated counts vs measured census), exactly the coupling O02's trap
(b) documents ("an added queue row changes the §4 arithmetic … the two
checks are coupled through the stated counts"). The amended expectations are
therefore valid on both baselines (delta semantics: `want = BASELINE ∪
adds`). No tool behavior changed; the harness's pass criteria now assert the
tool's real, correct behavior. Embedded-block SHA-256 (source + trailing
newline, post-amendment): `8068187afcd147b8f28ebc49061c2b4141c2fc0cea09ada76c0d6d017d89cfe9`.
