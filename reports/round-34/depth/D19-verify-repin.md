- Seat: D19 | verifier | claim D | date 2026-10-19 | baseline da68a6d

# D19 — Verification of D10's re-pin drafts (before-exactness + after-path consistency)

**Object verified:** `reports/round-34/depth/D10-repin-drafts.md` at revision
`sha256 093caddd1b3e2eca3013021a2c94fc0a8ab54f8beced1ad6e7572c8dec950768`,
446 lines (`sha256sum` / `wc -l`, 2026-10-19). The fragment grew under me
mid-run (354 → 446 lines); the §2 constants pair was verified at both revisions,
the six-block object at the revision above. Any later D10 revision needs a
re-run of the embedded verifier (one command, §Rerun).

## Verdict

| criterion (from the D19 mission) | result |
|---|---|
| each **before-block matches live bytes exactly once** | **PASS** — 6/6 blocks: byte-exact and exactly one code/config occurrence each |
| each **after-block's new path is consistent across all surfaces** | **PASS for the §2 pair; FAIL for §3-B1** (five competing successor names for the claims-map; F1) |
| D10's own census (§1/§7) against my independent census | **agrees** — exactly one live pin surface (`tools/exercise-handoff-e2e.py:1933-1934`), all other occurrences filed/record-class |
| pre-build obligations (C4/C5) | correctly **PENDING**, not claimed green |

Machine verdict on the object: `VERDICT: PASS`, `FAILURES: []` for C1/C2/C3/C6
(my verifier scores *byte and path consistency*, not the still-unresolved
naming decision in F1 — F1 is a human decision the verifier can only report).

## 1. Before-block exactness (C1)

Method: every `before:`/`**Before**` block line, taken byte-for-byte from the
fragment, is counted over the live tree (`.git/`, `.scratch/`, filed rounds
`reports/round-<N>/` N≤33, and the fragment itself excluded), split by surface
class (`CODE/config` vs `RECORD`). The uniqueness criterion is applied to CODE
class only, because round records *legitimately quote* the before-state — D10's
own before block, D01:171-172, D05:147, D14:96-97, K01:16-17, K02:35-36,
P01:112-114, X01:18, X04:189 all quote it (my run: `record_occurrences` 1–4 per
line).

Counts are the verifier's own (`text.count` per file, its extension filter on both
sides); the verdict-relevant column is `code_count`, stable at 1. `record`/`filed`
columns drift upward as sibling fragments land — the numbers below are the
2026-10-19 run quoted in §5.

| # | before-line (D10 §) | code_count | RECORD | filed-round | verdict |
|---|---|---|---|---|---|
| 1 | `V3_BASELINE_DEFAULT = "reports/round-30/handoff/declared-in-r6/expected.json"` (§2) | 1 | 1 | 2 | PASS |
| 2 | `V3_FROZEN_DIR_DEFAULT = "reports/round-30/handoff/declared-in-r6"` (§2) | 1 | 1 | 2 | PASS |
| 3 | `CLAIMS_MAP = "reports/round-20/handoff/claims-map.md"` (§3-B1) | 1 | 2 | 1 | PASS |
| 4 | `f"{counts['contact']} contact layers, twelve authored components); all native spellings are "` (§3-B2) | 1 | 1 | 0 | PASS |
| 5 | `"D4's inherited and own holds stay open: twelve form holds + three rank holds + one "` (§3-B3) | 1 | 4 | 0 | PASS |
| 6 | `"note, thirteen unresolved rank items, three quarantine handles and four conflicts — "` (§3-B3) | 1 | 4 | 0 | PASS |

Byte-exactness (not just substring equality) for the §2 pair, `cat -A`:

```
$ sed -n '1933,1934p' tools/exercise-handoff-e2e.py | cat -A
V3_BASELINE_DEFAULT = "reports/round-30/handoff/declared-in-r6/expected.json"$
V3_FROZEN_DIR_DEFAULT = "reports/round-30/handoff/declared-in-r6"$
```

Single space before `=`, double quotes, no trailing whitespace — D10's "one
space before `=`" note is correct. The other four sites, `grep -n` → `:184`,
`:2779`, `:3526`, `:3527` (live bytes identical to the drafts, incl. the U+2014
em dash at the end of `:3527`).

**The before-block's referent is live and green** — I ran the default route
myself at the pre-state (read-only, tool not runner):

```
$ python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet
handoff-v3: exit=0 fields=16/16 glossary=20/20 findings=0 links=105/105 claims=27 statuses=16/7/4 v2_subset=equal alias_leg=landed packet_sha256=6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb
E2E_EXIT=0
```

`6ced88ad…` equals `freeze.txt:2` of the r6 pair, so the constants the before
block names are the pair the default route actually reads — not a stale echo.

## 2. After-block invariants (C2) — the §2 pair is airtight

All five checks PASS on D10's after block:

| invariant | why it matters | result |
|---|---|---|
| `after_baseline == after_frozen + "/expected.json"` | the tool's own selftest derives the baseline from the dir constant (`tools/exercise-handoff-e2e.py:4172` (`baseline_rel = V3_FROZEN_DIR_DEFAULT + "/expected.json"`)); a divergent pair breaks the isolation leg | PASS |
| no trailing slash | `:4149` joins the constant onto a fixture root | PASS |
| baseline dir == frozen | same directory, one revision home | PASS |
| frozen/baseline startswith `reports/round-34/handoff/declared-in-r7` | matches `reports/round-34/claims.json:30` and the r2→r6 naming chain (round-22/23/25/26/30 → round-34) | PASS |

Successor spelling census (round-34 records): 22 record files name
`reports/round-34/handoff/declared-in-r7`, and **every distinct spelling of the
r7 path in the round is under `reports/round-34/handoff/`** — no divergent
parent directory, no typo variant:

```
$ grep -rho 'reports/round-34/[A-Za-z0-9_./-]*declared-in-r7[A-Za-z0-9_./-]*' reports/round-34/ | sort | uniq -c
29 …/declared-in-r7/    21 …/declared-in-r7    19 …/packet.md    12 …/expected.json
 7 …/claims-map.md      5 …/freeze.txt         4 …/twin.json     1 …/run.log
 1 reports/round-34/handoff/build-declared-in-r7.sh
```

`:3185` emitted into the packet body (`{V3_BASELINE_DEFAULT}`) is the one
derived surface; D10 assigns it "no edit" — correct (`grep -n 'declared-in'
tools/exercise-handoff-e2e.py` → `:38,:39,:1933,:1934` only; `:3185`, `:4149`,
`:4172`, `:4561`, `:3806` consume the constants, none hardcodes the path).

## 3. Findings

**F1 (material — the §3-B1 after-path is NOT consistent across surfaces; five
competing names).** D10's `CLAIMS_MAP` after-block names
`reports/round-34/handoff/claims-map-r34.md`. That spelling appears in **D10
only** (3 mentions inside its own fragment). Other seats name three other homes,
and the third D-pass recommends a fourth:

| successor spelling | named by | evidence |
|---|---|---|
| `reports/round-34/handoff/claims-map-v3-next.md` | D01 (layout), R03, D15, D16 | `depth/D01-layout.md:61,150,164`; `review/R03-d-review.md:246` |
| `reports/round-34/handoff/claims-map.md` | R03 (recommended home), S01, D16 | `review/R03-d-review.md:60` "Recommended home: `reports/round-34/handoff/claims-map.md`"; `scribe/S01-d-receipt.md` |
| `reports/round-34/handoff/claims-map-v3-r7.md` | D08, D16 | `depth/D08-links-uncertainty.md` |
| `reports/round-34/handoff/declared-in-r7/claims-map.md` | D15, D20 | `depth/D15-gap-fill.md` (6×), `depth/D20-verify-preservation.md` |
| `reports/round-34/handoff/claims-map-r34.md` | **D10 only** | `depth/D10-repin-drafts.md:113,334,395` |

P01's plan names the stale source (`plan/P01-d-plan.md:19,21,35`) but decides no
successor name. My verdict on the criterion as written: **the after-block's new
path is not yet consistent across all surfaces** — the integrator must fix one
name before applying, or the swap lands a path three other seats will disagree
with. The *invariants* of D10's after-block are sound (a single read-set member
swap: `CLAIMS_MAP` is in `V3_READ_SET` at `:1957`, read at `:2291`, rendered at
`:2881`/`:2934`, and fixture-anchored at `:4381` — so the constant swap
propagates the path automatically, and the packet's `A-57` row + intro follow).
Naming is a planner/integrator decision, not mine; F1 is a report, not a
unilateral fix.

**F2 (plumbing consequence of the winner's choice).** If the winner is D15/D20's
`declared-in-r7/claims-map.md`, the frozen dir holds **six** files: `v3_freeze`
writes exactly five (`expected.json`, `packet.md`, `twin.json`, `run.log`,
`freeze.txt`; R02-F2 cites `:4073-4117`), so the claims-map would be an
unfrozen sixth member of the revision dir, and my C4 file-set check plus the
freeze's own write set would need widening. The three "sibling" names avoid
this. Recorded so the choice is made knowingly.

**F3 (boundary note — scope, not defect).** D10 §2's "no other line of the tool
changes **for the re-point**" is correctly scoped, and its new §3 (three further
edits: `:184`, `:2779`, `:3526-3527`) closes the gap I would otherwise have
filed: K02-B7 (`scout/K02-repin-census.md:59`) measured that `OQ-V3-05`'s text is
a hardcoded literal, not a path pin, so the re-point alone cannot deliver claim
D's after_required. D04 §3a and D05 §4 own the wording; my C1 rows 3–6 confirm
D10's byte-text drafts are exact live bytes, while the *numbers* in rows 4–6 are
D18/D07/D17's verification surface (I spot-checked them: `ls
examples/culture-d4/components/*.yml | wc -l` → `13` for `:2779`;
`examples/culture-d4/expected-holds.json` → `counts {hold 12, note 0, fail 0}`
for `:3526-3527`, agreeing with R02:205 / D18:37-46).

**F4 (ordering — agrees with D10 §5 and R02-F1; independently reproduced).** The
freeze must follow the constant move. Two filed precedents I re-measured myself:

```
$ grep -n 'frozen baseline in' reports/round-25/v3-supersession/declared-in-r4/packet.md
:298 … compared against the frozen baseline in `reports/round-22/handoff/declared-in-r2/expected.json`
$ grep -n 'frozen baseline in' reports/round-30/handoff/declared-in-r6/packet.md
:295 … compared against the frozen baseline in `reports/round-30/handoff/declared-in-r6/expected.json`
```

The r4 row names **r2** — a freeze taken before its re-point, the self-inconsistent
row class; `SCORECARD.md:330` states the rule ("freeze must follow the re-point
edit"); r30's `freeze.txt:8` carries the re-frozen chain
(`ec30b11f… -> 6ced88ad…`). My C5 check encodes this as a post-build gate:
`packet.md` must name its own baseline exactly once and its predecessor zero
times — the same invariant the filed r5/r6 pairs satisfy (control pair: r6 `1/0`,
r5 `1/0`, both PASS).

**F5 (found-adjacent, my own measurement — the census has a fifth `tools/` hit).**
`tools/__pycache__/exercise-handoff-e2e.cpython-314.pyc` (mtime 2026-10-18 16:48)
contains the token `declared-in-r2`, so a reviewer's `grep -rn "declared-in"
tools/` returns a **fifth** hit that D10 §7 and K02 §A do not name. It is not a
pin: gitignored (`.gitignore:4: __pycache__/`), untracked (`git ls-files
tools/__pycache__/` → empty), generated — and the round rules set
`PYTHONDONTWRITEBYTECODE=1` precisely to stop new ones. Recorded so a re-grep is
not read as a missed surface; no edit proposed.

**F6 (advisory).** C3 lists 34 record files carrying the predecessor path
(filed rounds: 40 occurrences across 12 files). Records quoting the before-state
are expected and are why C1 counts CODE class only; the single CODE-class
occurrence is the tool, and it is covered by the before block.

## 4. Verifier artifact (re-runnable, stdlib only)

`verify` below is embedded verbatim; `sha256sum` of the embedded bytes
`4623c7421dd1bee90536962736b0e9c07158e6440040978cc50f1958f21806cf`
(425 lines, 18031 bytes at capture). It writes only under `TMPDIR`. Checks:
C1 before-exactness (code class, exactly once), C2 after-invariants, C3 census
completeness (code-class undeclared occurrence = FAIL; record-class = advisory),
C4 successor-dir file set, C5 packet self-consistency, C6 declared-surface
digest. I re-extracted the block from this fragment after writing it, confirmed
the digest, and ran `--selftest` from the extracted copy (both recorded in §5).

**Rerun** (extract, hash, selftest, then check any D10 revision):

```sh
python3 - <<'PY'
import hashlib, re, pathlib
t = pathlib.Path('reports/round-34/depth/D19-verify-repin.md').read_text()
src = re.search(r'```python\n(.*?)\n```', t, re.S).group(1) + '\n'
pathlib.Path('.scratch/d19/extracted.py').write_text(src)   # .scratch, not durable
print('sha256', hashlib.sha256(src.encode()).hexdigest())
PY
python3 -B .scratch/d19/extracted.py --selftest
python3 -B .scratch/d19/extracted.py --fragment reports/round-34/depth/D10-repin-drafts.md
```

```python
#!/usr/bin/env python3
"""D19 re-pin verifier — checks a re-pin draft fragment against live tree bytes.

Read-only. stdlib only. Writes only under TMPDIR.

Usage:
  python3 verify_repin.py --fragment reports/round-34/depth/D10-repin-drafts.md
  python3 verify_repin.py --selftest        # 5 synthetic cases, synthetic root
  python3 verify_repin.py --control-pairs   # filed r5/r6 pairs satisfy C5

Draft fragment format (fenced blocks; first content line names the block kind):

    before:            exact live byte lines the edit replaces
    after:             the replacement byte lines
    superseded:        occurrences deliberately NOT edited, as `<path> - <reason>`

Checks
  C1 before-exactness      every before-line occurs EXACTLY ONCE in the live tree
                           (live = outside .git/, .scratch/, filed rounds
                           reports/round-<N>/ N<=33, and the fragment itself)
  C2 after-invariants      baseline == frozen + "/expected.json" (mirrors
                           tools/exercise-handoff-e2e.py:4172), no trailing
                           slash, same directory, both under the successor dir
  C3 census-completeness   every live occurrence of the predecessor path is
                           either a declared before-line, declared under
                           `superseded:`, or in a record file (reports/**,
                           root *.md) — an UNDECLARED occurrence in a code or
                           config file is a missed pin surface => FAIL
  C4 sequencing            successor dir holds packet.md, twin.json,
                           expected.json, freeze.txt, run.log; PENDING before
                           the build lands (not a failure)
  C5 packet self-consistency  once landed: packet.md names its own baseline path
                           exactly once and its predecessor zero times (the
                           :3185 template). Filed r5/r6 pairs are the control.

Exit 0 iff C1/C2/C3 pass; C4/C5 may be PENDING.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
PREDECESSOR = "reports/round-30/handoff/declared-in-r6"
SUCCESSOR = "reports/round-34/handoff/declared-in-r7"
CONSTANTS = ("V3_BASELINE_DEFAULT", "V3_FROZEN_DIR_DEFAULT")
DRAFT_EXTS = {".py", ".md", ".json", ".yml", ".yaml", ".txt", ".tsv", ".log",
              ".jsonl", ".sh", ".toml", ".cfg", ".ini", ".csv", ".rst"}
SKIP_DIRS = {".git", ".scratch", "__pycache__", "node_modules", "out"}
FILED = re.compile(r"^reports/round-(\d+)/")
ROOT_RECORDS = {"LOG.md", "SCORECARD.md", "README.md", "AGENTS.md", "SKILL.md",
                "MINT.md", "PROVINCE.md", "SHONEN.md", "MANIFEST.json"}
ASSIGN = re.compile(
    r'^(V3_BASELINE_DEFAULT|V3_FROZEN_DIR_DEFAULT)\s*=\s*"([^"]*)"\s*$')


def classify(rel: str) -> str:
    """RECORD = evidence surface (never a pin target); CODE = code/config."""
    if (rel in ROOT_RECORDS or rel.startswith("reports/")
            or rel.startswith("corpus/") or rel.startswith(".ufo/")):
        return "RECORD"
    return "CODE"


def iter_files(root: Path):
    for path in sorted(root.rglob("*")):
        if not path.is_file() or path.suffix not in DRAFT_EXTS:
            continue
        rel = path.relative_to(root)
        if any(part in SKIP_DIRS for part in rel.parts):
            continue
        posix = rel.as_posix()
        m = FILED.match(posix)
        if m and int(m.group(1)) <= 33:
            continue
        yield posix, path


def _kind_of(label: str):
    """`before:` / `**Before** (…):` / `after:` -> canonical kind or None."""
    s = re.sub(r"^[\s*#>`_-]+", "", label.strip())
    s = re.sub(r"^[`\s]+", "", s)
    m = re.match(r"(before|after|superseded)\b", s, re.I)
    return m.group(1).lower() if m else None


def parse_blocks(text: str):
    """Label may sit on the line before the fence, or be the fence's first line."""
    blocks = {"before": [], "after": [], "superseded": []}
    lines = text.splitlines()
    i = 0
    while i < len(lines):
        if not lines[i].strip().startswith("```"):
            i += 1
            continue
        j = i - 1
        kind = None
        seen = 0
        while j >= 0 and seen < 6:            # tolerate a wrapped label line
            stripped = lines[j].strip()
            if stripped:
                seen += 1
                if stripped.startswith("```"):
                    break
                kind = _kind_of(stripped)
                if kind:
                    break
            j -= 1
        k, content = i + 1, []
        while k < len(lines) and not lines[k].strip().startswith("```"):
            content.append(lines[k].strip())
            k += 1
        if kind is None:
            for c in content:
                if c:
                    kind = _kind_of(c)
                    break
        if kind:
            if content and _kind_of(content[0]) == kind:
                content = content[1:]
            blocks[kind].extend(c for c in content if c)
        i = k + 1
    return blocks


def occurrence_rows(root: Path, needle: str, self_path: Path):
    """[(rel, [(lineno, line)])] over the live tree."""
    rows = []
    for rel, path in iter_files(root):
        if path.resolve() == self_path:
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        if needle not in text:
            continue
        hits = [(i + 1, l.strip()) for i, l in enumerate(text.splitlines())
                if needle in l]
        rows.append((rel, hits))
    return rows


def filed_count(root: Path, needle: str):
    total = files = 0
    for path in sorted((root / "reports").glob("round-*")):
        m = FILED.match(path.relative_to(root).as_posix() + "/")
        if not m or int(m.group(1)) > 33:
            continue
        for f in sorted(path.rglob("*")):
            if not f.is_file() or f.suffix not in DRAFT_EXTS:
                continue
            try:
                n = f.read_text(encoding="utf-8").count(needle)
            except (UnicodeDecodeError, OSError):
                continue
            if n:
                total += n
                files += 1
    return total, files


def check(root: Path, fragment: Path, successor: str = SUCCESSOR,
          predecessor: str = PREDECESSOR):
    blocks = parse_blocks(fragment.read_text(encoding="utf-8"))
    before, after, superseded = (blocks["before"], blocks["after"],
                                 blocks["superseded"])
    self_path = fragment.resolve()
    out = {"fragment": str(fragment), "root": str(root), "checks": {},
           "failures": []}

    # ---- C1 before-exactness (exactly once, CODE class) --------------------
    # Records (reports/**, root *.md) legitimately QUOTE the before-state, so the
    # uniqueness criterion is over code/config surfaces only; record counts are
    # reported informationally.
    c1 = []
    for line in sorted(set(l for l in before if l)):
        rows = occurrence_rows(root, line, self_path)
        code = rec = 0
        for rel, hits in rows:
            n = sum(1 for _, l in hits if l == line)
            if classify(rel) == "CODE":
                code += n
            else:
                rec += n
        filed, filed_files = filed_count(root, line)
        ok = code == 1
        c1.append({"line": line, "code_count": code, "want": "exactly 1",
                   "record_occurrences": rec, "ok": ok,
                   "filed_round_occurrences": filed,
                   "verdict": "PASS" if ok else "FAIL"})
        if not ok:
            out["failures"].append(
                f"C1: before-line occurs {code}x in code/config surfaces "
                f"(want exactly 1): {line!r}")
    out["checks"]["C1_before_exactness"] = c1

    # ---- C2 after-invariants ------------------------------------------------
    vals = {}
    for line in after:
        m = ASSIGN.match(line)
        if m:
            vals[m.group(1)] = m.group(2)
    c2 = []
    if set(vals) != set(CONSTANTS):
        out["failures"].append(f"C2: after-block constants {sorted(vals)}")
        c2.append({"id": "both-constants-declared", "ok": False,
                   "verdict": "FAIL"})
    else:
        base, frozen = vals["V3_BASELINE_DEFAULT"], vals["V3_FROZEN_DIR_DEFAULT"]
        checks = (
            ("baseline == frozen + '/expected.json'",
             base == frozen + "/expected.json"),
            ("no trailing slash",
             not frozen.endswith("/") and not base.endswith("/")),
            ("baseline dir == frozen", base.rsplit("/", 1)[0] == frozen),
            ("frozen startswith successor dir", frozen.startswith(successor)),
            ("baseline under successor dir", base.startswith(successor + "/")),
        )
        for name, ok in checks:
            c2.append({"id": name, "ok": bool(ok),
                       "verdict": "PASS" if ok else "FAIL"})
            if not ok:
                out["failures"].append(f"C2: {name} ({base!r} / {frozen!r})")
    out["checks"]["C2_after_invariants"] = c2

    # ---- C3 census-completeness --------------------------------------------
    declared = set(before)
    decl_superseded = set()
    for row in superseded:
        path_part = row.split(":", 1)[0].split(" ", 1)[0].lstrip("-* `")
        if path_part:
            decl_superseded.add(path_part.strip("`"))
    c3 = []
    for rel, hits in occurrence_rows(root, predecessor, self_path):
        uncovered = [f"{rel}:{n}" for n, l in hits if l not in declared]
        if not uncovered:
            verdict = "PASS-covered-by-before"
        elif rel in decl_superseded:
            verdict = "PASS-declared-superseded"
        elif classify(rel) == "RECORD":
            verdict = "ADVISORY-record-undeclared"
        else:
            verdict = "FAIL-undeclared-code-occurrence"
            out["failures"].append(
                f"C3: undeclared code occurrence(s) {uncovered}")
        c3.append({"file": rel, "class": classify(rel),
                   "occurrences": len(hits), "uncovered": uncovered,
                   "verdict": verdict})
    out["checks"]["C3_census_completeness"] = c3

    # ---- C4 sequencing ------------------------------------------------------
    succ = root / successor
    need = ["packet.md", "twin.json", "expected.json", "freeze.txt", "run.log"]
    present = [f for f in need if (succ / f).exists()]
    missing = [f for f in need if f not in present]
    out["checks"]["C4_sequencing"] = {
        "dir_exists": succ.exists(), "present": present, "missing": missing,
        "verdict": "LANDED" if not missing else "PENDING"}

    # ---- C5 packet self-consistency ----------------------------------------
    if not missing:
        pkt = (succ / "packet.md").read_text(encoding="utf-8")
        own, pred = pkt.count(successor + "/expected.json"), pkt.count(predecessor)
        ok = own == 1 and pred == 0
        out["checks"]["C5_packet_self_consistency"] = {
            "own_baseline_path_occurrences": own,
            "predecessor_occurrences": pred, "ok": ok,
            "verdict": "PASS" if ok else "FAIL"}
        if not ok:
            out["failures"].append(
                f"C5: packet names own baseline {own}x (want 1), "
                f"predecessor {pred}x (want 0)")
    else:
        out["checks"]["C5_packet_self_consistency"] = {
            "verdict": "PENDING",
            "note": "tools/exercise-handoff-e2e.py:3185 templates "
                    "V3_BASELINE_DEFAULT into the packet's gate-leg prose, so the "
                    "freeze must run AFTER the constant moves, else the new "
                    "packet names the old baseline"}
    # ---- C6 declared-surface digest ----------------------------------------
    # Any 64-hex digest the draft states beside the renderer surface or a
    # `surface_sha256` field must include the live digest of the tool.
    tool = root / "tools" / "exercise-handoff-e2e.py"
    if tool.exists():
        import hashlib
        live = hashlib.sha256(tool.read_bytes()).hexdigest()
        text = fragment.read_text(encoding="utf-8")
        declared = set()
        for line in text.splitlines():
            if "surface_sha256" in line or "exercise-handoff-e2e.py" in line:
                declared |= set(re.findall(r"\b[0-9a-f]{64}\b", line))
        ok = live in declared
        out["checks"]["C6_declared_surface_digest"] = {
            "live_tool_sha256": live, "declared_digests": sorted(declared)[:6],
            "ok": ok, "verdict": "PASS" if ok else ("FAIL" if declared else "PENDING")}
        if declared and not ok:
            out["failures"].append(
                "C6: the draft states tool digests but not the live one "
                f"({live})")
    else:
        out["checks"]["C6_declared_surface_digest"] = {"verdict": "PENDING"}

    out["filed_round_predecessor_occurrences"] = filed_count(root, predecessor)
    out["verdict"] = "PASS" if not out["failures"] else "FAIL"
    return out


GOOD = ("# synthetic D10-style draft\n\nbefore:\n```\n"
        f'{CONSTANTS[0]} = "{PREDECESSOR}/expected.json"\n'
        f'{CONSTANTS[1]} = "{PREDECESSOR}"\n'
        "```\n\nafter:\n```\n"
        f'{CONSTANTS[0]} = "{SUCCESSOR}/expected.json"\n'
        f'{CONSTANTS[1]} = "{SUCCESSOR}"\n'
        "```\n\nsuperseded:\n```\n"
        "LOG.md - historical ledger row, never edited\n"
        "SCORECARD.md - historical scored row, never edited\n"
        "```\n")


def _mkroot(tmp: Path):
    root = Path(tmp) / "root"
    (root / "tools").mkdir(parents=True)
    (root / "tools" / "exercise-handoff-e2e.py").write_text(
        f'{CONSTANTS[0]} = "{PREDECESSOR}/expected.json"\n'
        f'{CONSTANTS[1]} = "{PREDECESSOR}"\n', encoding="utf-8")
    (root / "LOG.md").write_text("  re-pointed to declared-in-r6.\n",
                                 encoding="utf-8")
    (root / "SCORECARD.md").write_text(
        "| operability | re-pointed to declared-in-r6 |\n", encoding="utf-8")
    return root


def selftest():
    cases = []
    with tempfile.TemporaryDirectory(prefix="d19-repin-") as tmp:
        base_root = _mkroot(tmp)
        # trap: a SECOND code occurrence of the predecessor path
        root_extra = Path(tmp) / "root-extra"
        import shutil
        shutil.copytree(base_root, root_extra)
        (root_extra / "tools" / "pin.py").write_text(
            f'BASELINE = "{PREDECESSOR}/expected.json"\n', encoding="utf-8")
        # trap: the before-line duplicated (must be exactly once)
        root_dup = Path(tmp) / "root-dup"
        shutil.copytree(base_root, root_dup)
        tool = root_dup / "tools" / "exercise-handoff-e2e.py"
        tool.write_text(tool.read_text(encoding="utf-8") * 2, encoding="utf-8")

        cases = [
            ("positive/good", base_root, GOOD, "PASS"),
            ("negative/stale-before-line", base_root,
             GOOD.replace('declared-in-r6/expected.json"',
                          'declared-in-r6/expected-old.json"', 1), "FAIL"),
            ("negative/inconsistent-after", base_root,
             GOOD.replace(f'{CONSTANTS[0]} = "{SUCCESSOR}/expected.json"',
                          f'{CONSTANTS[0]} = "{SUCCESSOR}/twin.json"'), "FAIL"),
            ("negative/undeclared-code-occurrence", root_extra, GOOD, "FAIL"),
            ("negative/before-line-occurs-twice", root_dup, GOOD, "FAIL"),
        ]
        results, failures = [], []
        for name, root, body, want in cases:
            p = Path(tmp) / (name.replace("/", "-") + ".md")
            p.write_text(body, encoding="utf-8")
            res = check(root, p)
            got = res["verdict"]
            results.append({"case": name, "want": want, "got": got,
                            "failures": res["failures"]})
            if got != want:
                failures.append(f"{name}: want {want} got {got}")
    print(json.dumps({"selftest": "OK" if not failures else "FAILED",
                      "cases": results, "failures": failures},
                     indent=1, ensure_ascii=False))
    return 0 if not failures else 1


def control_pairs():
    """Positive control: filed r5/r6 pairs satisfy C5's invariant."""
    cases = [
        ("reports/round-30/handoff/declared-in-r6",
         "reports/round-26/handoff/declared-in-r5"),
        ("reports/round-26/handoff/declared-in-r5",
         "reports/round-25/v3-supersession/declared-in-r4"),
    ]
    rows, failures = [], []
    for own_dir, pred_dir in cases:
        text = (ROOT / own_dir / "packet.md").read_text(encoding="utf-8")
        own, pred = text.count(own_dir + "/expected.json"), text.count(pred_dir)
        ok = own == 1 and pred == 0
        rows.append({"packet": f"{own_dir}/packet.md", "own": own,
                     "predecessor": pred, "ok": ok,
                     "verdict": "PASS" if ok else "FAIL"})
        if not ok:
            failures.append(f"{own_dir}/packet.md: own={own} pred={pred}")
    print(json.dumps({"control": "filed-pair-C5", "rows": rows,
                      "verdict": "PASS" if not failures else "FAIL",
                      "failures": failures}, indent=1, ensure_ascii=False))
    return 0 if not failures else 1


def main(argv=None):
    ap = argparse.ArgumentParser()
    ap.add_argument("--fragment")
    ap.add_argument("--root")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--control-pairs", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest()
    if args.control_pairs:
        return control_pairs()
    if not args.fragment:
        ap.error("--fragment or --selftest required")
    res = check(Path(args.root).resolve() if args.root else ROOT,
                Path(args.fragment))
    print(json.dumps(res, indent=1, ensure_ascii=False))
    return 0 if res["verdict"] == "PASS" else 1


if __name__ == "__main__":
    sys.exit(main())
```

## 5. Observed outputs

Selftest, 5 controls, synthetic root (no live-tree dependency):

```
$ python3 -B .scratch/d19/verify_repin.py --selftest
selftest: OK
  positive/good -> PASS
  negative/stale-before-line -> FAIL          (C1: 0x in code class)
  negative/inconsistent-after -> FAIL         (C2: baseline != frozen + '/expected.json')
  negative/undeclared-code-occurrence -> FAIL (C3: tools/pin.py:1)
  negative/before-line-occurs-twice -> FAIL   (C1: 2x, want exactly 1)
```

Positive control on filed history (proves C5's invariant is the lane's real
convention, not my invention):

```
$ python3 -B .scratch/d19/verify_repin.py --control-pairs
{"control": "filed-pair-C5", "verdict": "PASS", "rows": [
 {"packet": "reports/round-30/handoff/declared-in-r6/packet.md", "own": 1, "predecessor": 0, "ok": true, "verdict": "PASS"},
 {"packet": "reports/round-26/handoff/declared-in-r5/packet.md", "own": 1, "predecessor": 0, "ok": true, "verdict": "PASS"}]}
```

On D10 (final run, object revision `093caddd…`):

```
EXIT=0
VERDICT: PASS  FAILURES: []
 C1 code=1 record=4 filed=0 PASS   # OQ-V3-05 line 1
 C1 code=1 record=4 filed=0 PASS   # OQ-V3-05 line 2
 C1 code=1 record=2 filed=1 PASS   # CLAIMS_MAP
 C1 code=1 record=1 filed=2 PASS   # V3_BASELINE_DEFAULT  (the two filed hits are the round-33
 C1 code=1 record=1 filed=2 PASS   # V3_FROZEN_DIR_DEFAULT   A02:19-20 / A11:88 quotes)
 C1 code=1 record=1 filed=0 PASS   # contact layers / twelve authored components
 C3 files: 35 | code rows: [('tools/exercise-handoff-e2e.py','PASS-covered-by-before')] | advisory records: 34
 C2/C6: PASS ×5 / PASS     C4: PENDING (dir does not exist)     C5: PENDING (pre-build)
```

(Note: rows print in sorted line order — `"` sorts before `C`, `V`, `f` — so
the OQ lines lead; the `record`/`filed` columns shift as sibling fragments land,
while the verdict-relevant `code` column is stable at 1. §1's table is keyed by
line, so its per-line counts are the same six numbers rearranged.)

Embedded-artifact round trip (extract → hash → run):

```
extracted sha256: 4623c7421dd1bee90536962736b0e9c07158e6440040978cc50f1958f21806cf
matches claimed …06cf: True      matches .scratch source: True
$ python3 -B .scratch/d19/extracted.py --selftest      → selftest: OK cases: 5
$ python3 -B .scratch/d19/extracted.py --control-pairs → control: PASS
```

Independent D10 measurements I reproduced (all agree):

| D10 claim | my measurement |
|---|---|
| tool digest `a5e4a8c5…`, 4612 lines | `sha256sum` → identical; `wc -l` → 4612 |
| r6 five-file digests (`packet 6ced88ad…`, `twin 6633443d…`, `expected ea1e2927…`, `freeze 6fe70c0c…`, `run b5ee3351…`) | identical, all five |
| `expected.json`: 58 inputs, renderer absent, `baseline_digest 714b41fc…` | identical; 12 `tools/*` inputs enumerated |
| `V3_READ_SET` does not contain the renderer → re-point invisible to read-set digests | `python` regex over `V3_READ_SET` → mentions the tool: `False` |
| `grep -rn "declared-in" tools/` → `:38,:39,:1933,:1934` | identical for durable bytes (F5 adds the ignored `.pyc`) |
| `.ufo/` absent, no `MANIFEST*` in-repo | `ls -d .ufo` → No such file; `find . -maxdepth 4 -name 'MANIFEST*'` → none (fleet-root location stays `to-verify`) |

## Owed

- **to-verify (integrator, post-apply):** re-run this verifier after the re-point
  and freeze — C4 must flip to `LANDED` and C5 to `PASS`
  (`packet.md` names its own baseline once, predecessor never). Pre-build they are
  correctly PENDING, so claim D's "gate green on the new pair" is **not yet
  measured** and I claim no green for it.
- **F1 decision (planner/integrator):** one successor home for the new claims-map
  before the §3-B1 swap lands; F2 names the consequence of the in-dir option.
- **not mine:** the row-number correctness of D10 §3's after-values (D18/D07/D17),
  the OQ wording (D04/D05), the tamper control (D09), and the applied edit itself
  (integrator only — no seat edits `tools/exercise-handoff-e2e.py`).

## Citations

Reads: `reports/round-34/targets.json:41` (D19 mission), `:32` (D10 mission);
`reports/round-34/claims.json:24-36`; `reports/round-34/depth/D10-repin-drafts.md`
(whole file, revision `093caddd…`); `reports/round-34/depth/D11-preservation.md`;
`reports/round-34/scout/K02-repin-census.md:35-36,53-59,89-133`; 
`reports/round-34/plan/P01-d-plan.md:19-35`; `reports/round-34/depth/D01-layout.md:61,143-167`;
`reports/round-34/depth/D03-ledger-rows.md:70,116`; `reports/round-34/depth/D04-oq-glossary.md:56-65,220`;
`reports/round-34/depth/D05-packet-draft.md:42-44,51,64,70,76`; `reports/round-34/depth/D08-links-uncertainty.md`;
`reports/round-34/depth/D15-gap-fill.md`; `reports/round-34/depth/D20-verify-preservation.md`;
`reports/round-34/review/R02-d-review.md:92-166`; `reports/round-34/review/R03-d-review.md:60,246`;
`reports/round-34/scribe/S01-d-receipt.md`; `tools/exercise-handoff-e2e.py:38,39,184,1933-1934,1957,2289-2307,2566,2779,2881,2934,3185,3512,3523-3531,3806,4073-4117,4149,4172,4381,4488,4561,4577`;
`reports/round-30/handoff/declared-in-r6/{packet.md:295,freeze.txt:2,8,expected.json,twin.json,run.log}`;
`reports/round-25/v3-supersession/declared-in-r4/packet.md:298`;
`reports/round-22/handoff/declared-in-r2/packet.md:295`;
`reports/round-26/handoff/declared-in-r5/packet.md:295`; `SCORECARD.md:330,400`;
`examples/culture-d4/expected-holds.json`; `examples/culture-d4/typed-labels.d4.yml:29-46`;
`.gitignore:4`.

Commands (all `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, HEAD `da68a6d`,
none of them a `reports/round-*/run-validation.py`):

- `sed -n '1933,1934p' tools/exercise-handoff-e2e.py | cat -A`; `grep -n "CLAIMS_MAP = \|contact layers, twelve\|D4's inherited and own holds" tools/exercise-handoff-e2e.py`
- `grep -rn "declared-in" tools/`; `grep -rn "declared-in-r6" .` (census); `grep -rn 'round-30/handoff' .`; `grep -rho 'reports/round-34/[A-Za-z0-9_./-]*declared-in-r7[A-Za-z0-9_./-]*' reports/round-34/ | sort | uniq -c`
- `python3 -B tools/exercise-handoff-e2e.py --profile v3 --quiet` (exit 0, `packet_sha256=6ced88ad…`) — the tool, not a runner
- `python3 -B .scratch/d19/verify_repin.py --selftest|--control-pairs|--fragment reports/round-34/depth/D10-repin-drafts.md`
- `sha256sum tools/exercise-handoff-e2e.py reports/round-30/handoff/declared-in-r6/*`; `wc -l tools/exercise-handoff-e2e.py`
- `python3 -c "…json.load(…expected.json)…"` (58 inputs, renderer absent, `baseline_digest 714b41fc…`); `python3 -c` regex over `V3_READ_SET`
- `ls examples/culture-d4/components/*.yml | wc -l` → 13; `python3 -c` over `expected-holds.json` → `{hold 12, note 0, fail 0}`
- `ls -d tools/__pycache__ reports/round-34/handoff .ufo`; `git check-ignore -v tools/__pycache__/exercise-handoff-e2e.cpython-314.pyc`; `git ls-files tools/__pycache__/`; `strings …pyc | grep -o 'declared-in-r[0-9]' | sort -u`
- `git rev-parse HEAD` → `da68a6d…`; `git status --porcelain` → `?? reports/round-34/`
