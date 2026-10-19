- Seat: R05 | reviewer | O | 2026-10-19 | baseline da68a6d

# Second O pass — can the selftest fixtures pass while the instrument lies?

Mission: `reports/round-34/targets.json:69` ("the selftest fixtures' adequacy (can a
false green pass?)"). Out: `reports/round-34/review/R05-o-review.md`.

## 0. Dependency status (binding on how to read this)

At `2026-10-19` nothing of the O block is on disk: `reports/round-34/` contains only
`claims.json`, `targets.json`, `telemetry/` (`ls reports/round-34/`); `tools/harness/receipt_guard_adoption.py`
does not exist (`ls tools/harness/receipt_guard_adoption.py` → No such file or directory).
So I did **not** review the shipped fixture bytes. Instead I built the ground truth the
fixtures must reproduce, and I audit (a) the *declared* fixture spec that does exist on
disk — `targets.json:46` (O03) — and (b) the claim text's own hazard enumeration
(`claims.json:41`). The re-review of the landed `op/O02-tool-source.md` +
`op/O03-selftest.md` bytes is owed (§7).

**Verdict as specified: yes, a false green can pass — four independent ways** (§4). Two of
them are not hypothetical: they would be green while real filed hazards are reported clean
(§3, D-O-2/D-O-3).

## 1. Ground truth — independent census (the table the inventory must reproduce)

Read-only AST + grep census, never executing a runner. Command and artifact:
`python3 -B .scratch/r05-census.py` (source `.scratch/r05-census.py`, JSON `.scratch/r05-census.json`).

Population: 28 filed runners — `ls reports/round-*/run-validation.py | wc -l` → 28.

### 1a. Adopted — guard runs on the publish path before the own-receipt write (17)

| round | guard load idiom | guard call sites | own-receipt write |
|---|---|---|---|
| 14 | `importlib.util.spec_from_file_location` `:414` | `:708`, `:716` | `:717` |
| 15 | `:1038` | `:1337`, `:1345` | `:1346` |
| 16 | `:999` | `:1256`, `:1264` | `:1265` |
| 17 | `:1118` | `:1422`, `:1430` | `:1431` |
| 18 | `:1512` | `:1842`, `:1850` | `:1851` |
| 20 | `:1279` | `:1484` (publish-time only) | `:1485` |
| 22 | `runpy.run_path` `:828` | `:911`, `:921` | `:922` |
| 23 | `:1065` | `:1094` | `:1097` |
| 24 | `:1152` | `:1181` | `:1184` |
| 25 | `:1109` | `:1142` | `:1145` |
| 26 | `:1856` (via local `def guard_receipt()` `:1855`) | `:1906` | `:1909` |
| 27 | `:1854` | `:1904` | `:1907` |
| 28 | `:1997` | `:2095` | `:2098` |
| 30 | `:884` | `:903`, `:922` | `:923` |
| 31 | `:1119` | `:1139`, `:1158` | `:1159` |
| 32 | `:1103` | `:1123`, `:1142` | `:1143` |
| 33 | `:1442` | `:1459`, `:1470` | `:1471` |

All paths relative to `reports/round-<N>/run-validation.py`. **Two load idioms, not one:
6 importlib-spec (r14–r18, r20) and 11 runpy (r22–r28, r30–r33).** Sub-variants that a
fixture set must cover or misclassify: publish-time-only guard (r20 `:1484`, single call)
and guard-behind-a-local-wrapper-name (r26 `:1855`→`:1857`).

### 1b. Unguarded own-receipt writers — the real hazard set (11)

| round | write | shape |
|---|---|---|
| 5 | `:194` `(HERE / "validation.json").write_text` | fresh render |
| 6 | `:336` same | fresh render |
| 7 | `:1171` same | fresh render |
| 8 | `:1486` `output = ROOT / OUTPUT_REL` (`:99`) | fresh render |
| 9 | `:1910` (`:127` `OUTPUT_REL`) | fresh render |
| 10 | `:1054` (`:60`) | fresh render |
| 11 | `:1740` (`:125`) | fresh render |
| 12 | `:1071` `out = ROOT / OUTPUT` (`:18`) | fresh render |
| 19 | `:21` inside a `-c` source string; reads at `:19` | **in-place patch of the filed receipt** |
| 21 | `:1115` `output = ROOT / OUTPUT` (`:20`) | fresh render |
| 29 | `:922` `safe_path(OUTPUT).write_text` (`:23`) | fresh render |

11 + 17 = 28. Rounds 13 and 4 have no runner; that is not a census gap.

### 1c. Inventory-scope boundary (for the fixture that pins it)

- 5 non-runner top-level scripts under `reports/round-*/`: `round-6/check-checkpoint.py`,
  `round-30/retrospective-audit-C23-C25.py`, `round-30/verify-operability.py`,
  `round-31/sweep-audit.py`, `round-32/sweep-audit.py` — all five match `write_text|json.dump`.
- 158 nested `.py` under `reports/round-*/` at depth ≥ 2 (`find reports -mindepth 3 -name '*.py' | wc -l`).
  A walker written as `rglob("*.py")` would ingest 158+5 out-of-scope files.

## 2. The false-green mechanism, demonstrated on real bytes

I ran a deliberately naive first-pass rule ("any call/import whose spelled name contains
`guard`, or any string naming `receipt_guard`") — the same first cut a hurried
implementation takes. Its output, `.scratch/r05-census.stderr`:

```
GUARD_REFERENCING 19: ['round-7', 'round-14', ..., 'round-26', ..., 'round-29', ...]
NO_GUARD_REFERENCE  9: ['round-5', 'round-6', 'round-8', 'round-9', 'round-10', 'round-11', 'round-12', 'round-19', 'round-21']
```

Two of those 19 are **false greens**: round-29 carries no receipt-guard adoption at all;
its only guard-named symbol is `protection_guard()` at `:629`, an unrelated regression
helper (`grep -c protection_guard reports/round-29/run-validation.py` → 2), while its
receipt write at `:922` is bare. Round-7's 14 `guard` hits are the *evidence-coupling*
guard (`:28`, `:577 guard_positive_and_selftest`, `:738` "private copy of the guard"), and
its write at `:1171` is bare. A name-substring classifier therefore answers "adopted" for
two filed hazards — and it would answer "adopted" for the very runners the round is meant
to route. Note the asymmetry: my census *self-corrected* on second pass, but a one-shot
instrument has no second pass; only a fixture can encode the correction.

## 3. Defects filed against claim O's premise (`claims.json:41`, before-block)

- **D-O-1 (false hazard) — `round-26` is guarded.** The claim and `LOG.md:3560-3561` state
  "The r26 runner carries the same hazard (`:90`, `:1909`)". Filed bytes say otherwise:
  `:1855-1857` defines a local `guard_receipt()` that runs
  `runpy.run_path(str(safe_path("tools/harness/receipt_guard.py")))` and calls
  `namespace["guard_receipt"](OUTPUT, repo_root=ROOT)`; `main()` calls it at `:1906` on the
  only publish path and writes at `:1909` (`reports/round-26/run-validation.py:1905-1909`).
  The guard therefore runs before the write. Counter-reading to record honestly: adoption
  is via a same-named local wrapper, so if the taxonomy reserves `adopted` for a direct
  tool-API call, r26 is a *weaker* adopter — but it is not in the unguarded class, and the
  claim's "same hazard" wording is falsified either way. Both the claim text and
  `LOG.md` are filed/attributed elsewhere; I edit neither. **Errata row owed by the
  integrator** who owns round-34's LOG entry.
- **D-O-2 (missed hazard) — `round-29:922`** writes its filed receipt in place with zero
  `receipt_guard` references. Absent from the claim's four hazards and from the LOG
  enumeration.
- **D-O-3 (missed hazard, hardest shape) — `round-19`**: the write is
  `pathlib.Path('reports/round-19/validation.json').write_text(...)` at `:21` *inside a
  triple-quoted source string* passed to `subprocess.run([sys.executable, "-c", """…"""])`
  (`:5`), and it first reads the filed receipt at `:19` (`v=json.load(open(...));
  v['acceptance_checks_passed']=not fails`). A detector that parses only the runner's own
  AST answers `clean` here — a false green on a live hazard. It is also a distinct hazard
  *class*: patch-in-place, whose isolated-copy rerun consumes the filed receipt as input.
- **D-O-4 (4-of-11 sample)** — the claim's "Known hazards to classify: r5/r6/r7/r26" names
  four; the measured unguarded set is eleven (§1b). Fine as a seed list, wrong as a
  coverage contract; the fixture set must assert the whole population, not the seed.
- **D-O-5 (one-sided threshold, and it is one of the three declared claims)** —
  `claims.json:51` reads "zero false positives on guarded/non-runner fixtures". Only false
  *positives* are bounded. A selftest can satisfy that wording while every hazard is
  reported `clean` or `could-not-evaluate`. Required replacement wording: *each fixture
  asserts an exact class; N/N green requires both directions for every row (no hazard
  answered `guarded`/`clean`, no adopter answered `unguarded`); unreadable input yields
  `could-not-evaluate`, never `clean`.*

## 4. Can a false green pass? Four ways it can, as currently specified

`targets.json:46` (O03) declares: positive = "the r32 runner's guarded refresh pattern is
recognized as adopted"; negatives = "a guarded runner is NOT flagged, a non-runner writing
JSON is NOT flagged; a runner with no receipt write classified clean".

- **FG-1 — the positive fixture is not representative.** Only r32's runpy idiom is named,
  but 6 of 17 adopters (r14–r18, r20) load the guard via `importlib.util.spec_from_file_location`
  (§1a). A `runpy`-only detector is green on the r32 fixture and misclassifies six filed
  adopters → the inventory contradicts the claim while the selftest says pass. Same hole
  for the two sub-variants (r20 publish-only, r26 wrapper).
- **FG-2 — no publish-path fixture.** Nothing asserts the *path* condition. A fixture whose
  guard is imported/called but off the publish path (inside `--selftest`, behind
  `if args.refresh`, or for a different path) must be classified non-adopted; without it, a
  detector that keys on "guard symbol appears anywhere" passes. O08's mission builds three
  such traps — but in a verifier's `.scratch`, which is **not durable**: an unlanded trap
  cannot regress, so it does not bound the instrument's future answers.
- **FG-3 — no embedded-source or indirection fixture.** r19's shape (write inside a
  `-c`/`bash -c` string) and `os.replace`/`shutil.move`/`open(...,"w")`/`json.dump` shapes
  are unrepresented. Each is a false green by construction if the write-site detector
  enumerates only `Path.write_text`.
- **FG-4 — no completeness/fail-closed fixture.** Nothing pins the walk scope
  (28 of 28, seed of §1c) or asserts that a runner it cannot decode/parse becomes
  `could-not-evaluate` rather than silently shrinking the denominator. Without it, `--json`
  can print "100% coverage" over 27 rows and no fixture notices.

There is also no control that the *selftest itself* leaves filed bytes alone. The round-33
F-C13-1 incident was exactly this failure mode (`LOG.md:3548-3561`: `reports/round-{5,6,7}/validation.json`
rewritten in-tree 03:53:25Z–03:55:27Z, restored byte-exact) — an adoption audit whose
selftest writes fixtures near filed receipts could repeat it. The in-tree precedent for the
hygiene discipline already exists: `tools/harness/receipt_guard.py:203-214` builds every
fixture under `.scratch` in a `TemporaryDirectory` and never touches live metadata
(its stated limit at `:348-351`).

## 5. Mandatory fixture battery (wire these into `--selftest`; each asserts an exact class)

Proposed classes: `adopted` / `adopted-variant` (publish-only, wrapper-name) /
`unguarded-writer` / `unguarded-patch` / `could-not-evaluate` / `clean` (no own-receipt
write). Exact expected answer is part of the fixture, not an inspectable comment.

| # | fixture (shape) | expected class | false green it kills |
|---|---|---|---|
| F1 | runpy idiom, guard called pre-write (r32 shape) | `adopted` | the declared positive still must pass |
| F2 | `importlib.util.spec_from_file_location` idiom (r14 shape) | `adopted` | FG-1 |
| F3 | runpy idiom, single publish-time call (r20 shape) | `adopted` | FG-1 (variant) |
| F4 | importlib idiom with local wrapper name (r26 shape) | `adopted` | FG-1 (variant) |
| F5 | guard imported + `--selftest`-only call, bare receipt write | `unguarded-writer` | FG-2 |
| F6 | guard called only under `if os.environ.get("REFRESH_RECEIPTS"):` | `unguarded-writer` | FG-2 |
| F7 | guard loaded and called for a *different* path than the written receipt | `unguarded-writer` | FG-2 |
| F8 | local `def guard_receipt(): pass` + bare write (name-only impostor) | `unguarded-writer` | FG-2, §2 |
| F9 | `os.replace(tmp, OUTPUT)` / `shutil.move` after a bare render | `unguarded-writer` | FG-3 |
| F10 | `open(OUTPUT,"w")` + `json.dump` | `unguarded-writer` | FG-3 |
| F11 | write inside a `subprocess.run([sys.executable,"-c", <src>])` string; source **reads** the receipt first (r19 shape) | `unguarded-patch` (or `could-not-evaluate` if the tool refuses to parse embedded source) — **never `clean`** | FG-3, D-O-3 |
| F12 | unrelated helper named `protection_guard(...)` / docstring mentioning "guard" / "evidence-coupling guard" (r7, r29 shapes) | `unguarded-writer` | §2 substring false green |
| F13 | non-runner top-level `.py` writing JSON; and a file with invalid UTF-8 / `SyntaxError` | out of inventory; `could-not-evaluate` | FG-4 |
| F14 | runner whose receipt write sits in a function defined *after* `if __name__ == "__main__"` / inside `try/except` | `unguarded-writer` | order-dependent detection |
| F15 | scope pin: walk root must include exactly `reports/round-*/run-validation.py` (28 today), excluding F13's file and the 158 nested scripts | `inventory_len == 28` | FG-4 |

Pairwise discipline to require in the O03 receipt: every fixture row carries
`expected_class`, `observed_class`, `passed = (observed == expected)`, so a row cannot pass
by returning a superset flag. This is the same shape the guard's own selftest already uses
(`tools/harness/receipt_guard.py:236-238`, `:325-329` assert exit code **and** bytes **and**
stderr diagnostic **and** whether the callback ran — never a single boolean).

### The control that would have caught F-C13-1 mechanically

Add to `--selftest` and again to the `--json` leg: before/after digest map of all 28
`reports/round-*/validation.json` (plus `git status --porcelain reports/round-*/validation.json`
must print nothing). At baseline the tree is clean for those paths — my check
`git status --porcelain reports/round-19 reports/round-26 reports/round-29 reports/round-5
reports/round-6 reports/round-7` printed nothing, `git rev-parse HEAD` → `da68a6d705e41f369f21e8607bfaab5b54077f84`. A tool that
inventories receipt-writing runners and cannot prove it did not write a receipt is
inverted operability.

## 6. What the landed tool must reproduce (so D is checkable, not reviewed by memory)

`python3 tools/harness/receipt_guard_adoption.py --json` must yield
`28 total`, `17 adopted`, `11 unguarded` and the per-round classes of §1a/§1b. Any
deviation is a defect in either the tool or this table — both are falsifiable; I have
marked the one contested row (r26) explicitly in §3/ D-O-1 rather than smoothing it.
Recommended extra field per row: the resolved guard-load idiom and the write-line number,
so a later re-review is a diff rather than a re-derivation.

## 7. Durable reproduction (`.scratch` is cleaned before handoff)

Self-contained; reads source only, executes no runner. Run from the repo root; expected
stderr output is `TOTAL 28 ADOPTED 17 UNGUARDED 11`.

```python
import ast, pathlib, re, sys
ROOT = pathlib.Path(".").resolve()
ADOPT_LOAD = re.compile(r"receipt_guard\.py")
def cls(p):
    src = p.read_text(encoding="utf-8"); t = ast.parse(src)
    loads, calls, write = False, [], None
    for n in ast.walk(t):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and ADOPT_LOAD.search(n.value):
            loads = True                                   # runpy/spec/importlib target string
        if isinstance(n, ast.Call):
            f = ast.unparse(n.func)
            if f.endswith("run_path") and any(isinstance(a, ast.Constant)
                                              and "receipt_guard" in str(a.value) for a in n.args):
                loads = True
            if f == "guard_preflight" or f in ("guard_receipt", "round_runner_main"):
                calls.append(n.lineno)                      # not r29's protection_guard()
            if re.search(r"(OUTPUT|OUTPUT_REL|HERE)", ast.unparse(n.func)):
                write = n.lineno
    return "adopted" if (loads and calls and write) else ("unguarded" if src.count("validation.json") else "?")
runners = sorted(ROOT.glob("reports/round-*/run-validation.py"), key=lambda p: int(p.parent.name[6:]))
rows = {p.parent.name: cls(p) for p in runners}
adopt = [k for k, v in rows.items() if v == "adopted"]
print(f"TOTAL {len(rows)} ADOPTED {len(adopt)} UNGUARDED {len(rows)-len(adopt)}", file=sys.stderr)
print("ADOPTED:", ",".join(adopt), file=sys.stderr)
```

Observed at `da68a6d` (`python3 -B .scratch/r05-inline-check.py`):
`TOTAL 28 ADOPTED 17 UNGUARDED 11`; adopted = r14–r18, r20, r22–r28, r30–r33;
non-adopted = r5–r12, r19, r21, r29 — identical to §1a/§1b, and it excludes r29 and r7
from the adopted set where the substring rule of §2 included them.

## 8. Second pass — the landed core, measured (10 of 13 traps pass a false green)

§§4-5 were written before the O block landed, against the declared spec only. O01 then
landed a real core byte-exact in `reports/round-34/op/O01-impl.md:75-446`. I extracted that
fenced block to `.scratch/r05/o01core.py` and **verified the extraction is the filed bytes**:
`sha256sum .scratch/r05/o01core.py` → `a8d9e201a5afbb2ab0a4e35e992fc2a6cb7004d9c76e6ebd586773f264d34980`,
equal to the digest declared at `O01-impl.md:73`. So this is a measurement on the shipped
detector, not on a description of it.

**Method** (`python3 -B .scratch/r05/trap-battery.py`): 13 synthetic fixtures, each built
under `.scratch/r05/traps/reports/round-9xx/run-validation.py`, each classified by the
core's own `scan_runner`. No filed runner is imported or executed; the core is an audit
tool, not a round runner.

| fixture | expected class | observed | verdict |
|---|---|---|---|
| a `def guard_receipt(): pass`, never called, bare write | `unguarded-writer` | `guard-adopted` | **HOLE** |
| b guard called only on the `--selftest` path, publish branch bare | `unguarded-writer` | `guard-adopted` | **HOLE** |
| c guard called for `other.json`, receipt written bare | `unguarded-writer` | `guard-adopted` | **HOLE** |
| d guard call only *after* the receipt write | `unguarded-writer` | `guard-adopted` | **HOLE** |
| e r14 `importlib.util.spec_from_file_location` idiom, guard pre-write | `guard-adopted` | `guard-adopted` | OK |
| f r32 `runpy` idiom, guard pre-write | `guard-adopted` | `guard-adopted` | OK |
| g embedded `-c` write whose path defeats the literal pass | `unguarded-writer` | `no-receipt-write` | **HOLE** |
| h guarded module write + unguarded embedded receipt write | `unguarded-writer` | `guard-adopted` | **HOLE** |
| i write via helper parameter, no resolvable site | `could-not-evaluate` | `no-receipt-write` | **HOLE** |
| j `open(OUTPUT,"w")` + `json.dump` | `unguarded-writer` | `unguarded-writer` | OK |
| k receipt symbol named, no site resolves | `could-not-evaluate` | `no-receipt-write` | **HOLE** |
| l runner that is not valid UTF-8 | `could-not-evaluate` | raises `UnicodeDecodeError` | **HOLE** |
| m repository scan with one undecodable runner present | inventory produced | raises `UnicodeDecodeError` | **HOLE** |

**Two structural causes**, both readable in the core:

1. `o01core.py:319-332` decides the class from *whether any guard-named call exists
   anywhere*, then reports path conditions only as attributes:
   `effective = sites or embedded` → `elif call_lines: klass = "guard-adopted"`. The
   position/condition facts are computed (`guard_call_before_write`, `guard_call_conditional`,
   `_conditional_call` `:273-284`) and never consulted, so fixtures a-d are adopted by
   construction. The `hazard` flag (`:338`) is `bool(effective) and not call_lines` — false
   for all four.
2. `o01core.py:248-250` records a `FunctionDef` **named** `guard_receipt`/`round_runner_main`
   as a *call* (`"form": "def:…"`). Fixture a therefore reaches `guard-adopted` with no call
   in the file at all: defining a no-op of that name is sufficient. That is the same
   name-keyed trap as §2, now inside the instrument instead of a scratch census.

Also `:289` `path.read_text()` sits outside any `try`, so one undecodable or
non-UTF-8 runner aborts the entire repository scan (l, m) — no inventory, and the
`could-not-evaluate` class the taxonomy reserves (`:41`) is unreachable for that input.
Fixture j passing is a genuine credit to rule 3 (`:51-54`); e and f passing confirms
`F6`'s two-idiom claim on the core bytes.

**Decisive fixture sources** (these belong in O03's durable controls, not in my scratch):

```python
# (a) name-only impostor -> must be unguarded-writer
def guard_receipt():
    pass


def main():
    safe_path(OUTPUT).write_text(json.dumps({"acceptance_checks_passed": True}), encoding="utf-8")

# (b) publish-path condition -> must be unguarded-writer
def guard_receipt():
    namespace = runpy.run_path(str(safe_path("tools/harness/receipt_guard.py")))
    namespace["guard_receipt"](OUTPUT, repo_root=ROOT)


def main(argv=None):
    p = argparse.ArgumentParser(); p.add_argument("--selftest", action="store_true")
    args = p.parse_args(argv)
    if args.selftest:
        guard_receipt()          # off the publish path
        return 0
    safe_path(OUTPUT).write_text(json.dumps({"acceptance_checks_passed": True}), encoding="utf-8")

# (g) embedded payload, path built so no receipt literal survives -> never no-receipt-write
PAYLOAD = """
import json, pathlib
n = 901
p = pathlib.Path("reports/round-" + str(n) + "/va" + "lidation.json")
p.write_text(json.dumps({"acceptance_checks_passed": True}))
"""
```

**Required O03 rows** (mapping §5 → measured): F8→a, F5/F6→b, F7→c, new→d, F11→g,
new→h, F13→l (and a scan-level control for m), and the FG-E rule: a runner that names a
receipt symbol but resolves no write site must be `could-not-evaluate`, never
`no-receipt-write`. O01's own `t1`-`t5` (`O01-impl.md:1217-1223`) are sound but are
"one positive + four easy negatives"; they do not reach any row of this table.

**Status revision of §4** (honest accounting): FG-1 is **closed** in the core (`e`, `f`
pass; rule 4 `:55-58` accepts both idioms). FG-3 is **partly closed** (`j` passes; `g`, `h`
do not). FG-2 and FG-4 remain **open** — as does one hole §4 did not predict: the
`could-not-evaluate` class is unreachable for undecodable input and for unresolvable
writes, which turns the taxonomy's designated honesty lane into a `no-receipt-write`
(claimed-safe) answer.

## Owed

Status at `2026-10-19` (fragments landed after my first pass are marked):

- `reports/round-34/op/O03-selftest.md` — **still owed, and the single most important one**: the fixture list this review must audit. §8 now tells O03 exactly which rows are missing; until it lands, the trap battery lives only in `.scratch/r05/` and in §8's inlined sources.
- `reports/round-34/op/O02-tool-source.md` — **still owed**: the CLI/`--selftest` bytes. My §8 measurement is on O01's core (`O01-impl.md:75-446`); if O02 changes `scan_runner`'s class decision, §8 must be re-run against the new digest.
- `reports/round-34/op/O04-predicted-inventory.md`, `reports/round-34/op/O07-verify-tool.md`, `reports/round-34/op/O08-traps.md` — **still owed at write time**.
- Landed since my first pass and now consumed: `op/O01-impl.md` (core bytes measured, §8), `scout/K03-guard-pattern.md` (§2a reaches my D-O-1 independently), `op/O05-routing.md`, `op/O06/O09/O10`, `plan/P02-oc-plan.md`.
- **Integrator-owned (not mine to write):** the D-O-1 errata row in round-34's LOG entry vs `LOG.md:3560-3561`; the D-O-5 threshold rewording via `claims.json:51` (with §8 added: a threshold naming only false positives cannot bound fixtures a-d, g-l).

## Corroboration of §3 (independent seats, same bytes)

Three seats reached the §3 findings without my census: `op/O01-impl.md:1172-1176` (F1: "the
unguarded-writer set is 11 runners, not the 4 named in the claim"), `:1178-1185` (F2: r26
measures as guard-adopted, "wording discrepancy resolved in favour of the bytes"),
`:1187-1192` (F3: r19's embedded `-c` write is a false green for a module-body-only pass),
and `scout/K03-guard-pattern.md:50-66` ("2a. Correction to the F-C13-1 record as quoted in
`claims.json` / `LOG.md`"). Four independent instruments (mine, O01's core, K03's scout,
O05's scan per `O01-impl.md:1243-1246`) agree on 28/17/11. The §8 holes are **not**
corroborated by them — they are new here, and O07/O08 should verify or falsify them.

## Citations

- `reports/round-34/targets.json:46` (O03 mission/spec), `:69` (R05 mission), `:7-11` (shared rules)
- `reports/round-34/claims.json:41` (claim O before/gap), `:45` (after_required), `:51` (thresholds), `:70-74` (non-goals)
- `REGIMEN.md:26-30` (per-round contract), `:60-69` (scope)
- `LOG.md:3548-3561` (F-C13-1 incident record; r5/r6/r7 mechanism lines, r26 assertion, prevention)
- `tools/harness/receipt_guard.py:152-168` (guard API), `:203-214` (`.scratch` fixture discipline), `:236-238`, `:325-329` (multi-condition control shape), `:348-351` (stated limits)
- Census commands and outputs: `ls reports/round-*/run-validation.py | wc -l` → 28; `python3 -B .scratch/r05-census.py` → `.scratch/r05-census.json`, `.scratch/r05-census.stderr` (`GUARD_REFERENCING 19` incl. round-7 and round-29)
- `reports/round-5/run-validation.py:194`; `round-6/…:336`; `round-7/…:28,577,738,1171`; `round-8/…:99,1486`; `round-9/…:127,1910`; `round-10/…:60,1054`; `round-11/…:125,1740`; `round-12/…:18,1071`
- `reports/round-14/…:413-423,708,716,717`; `round-15/…:1037-1046,1337,1345,1346`; `round-16/…:998-1007,1256,1264,1265`; `round-17/…:1117-1126,1422,1430,1431`; `round-18/…:1511-1520,1842,1850,1851`; `round-20/…:1278-1287,1484,1485`
- `reports/round-19/run-validation.py:5,19,21`
- `reports/round-21/…:20,1115`; `round-22/…:828,911,921,922`; `round-23/…:1065,1094,1097`; `round-24/…:1152,1181,1184`; `round-25/…:1109,1142,1145`; `round-26/…:90,1855-1857,1905-1909`; `round-27/…:1854,1904,1907`; `round-28/…:1997,2095,2098`
- `reports/round-29/run-validation.py:23,629,779,922`; `round-30/…:884,903,922,923`; `round-31/…:1119,1139,1158,1159`; `round-32/…:1103,1123,1142,1143`; `round-33/…:1442,1459,1470,1471`
- Scope boundary: `find reports -mindepth 3 -name '*.py' | wc -l` → 158; the five top-level non-runner scripts listed in §1c
- Filed-byte control: `git status --porcelain reports/round-19 reports/round-26 reports/round-29 reports/round-5 reports/round-6 reports/round-7` → empty; `git rev-parse HEAD` → `da68a6d705e41f369f21e8607bfaab5b54077f84`
- §8 (core measurement): `reports/round-34/op/O01-impl.md:75-446` (fenced core), `:73` (declared sha256), `:1172-1192` (F1/F2/F3), `:1212-1226` (the five exercised fixtures), `:1243-1246` (O05/O09 corroboration)
- §8 commands: `sed -n '76,446p' reports/round-34/op/O01-impl.md > .scratch/r05/o01core.py`; `sha256sum .scratch/r05/o01core.py` → `a8d9e201a5afbb2ab0a4e35e992fc2a6cb7004d9c76e6ebd586773f264d34980`; `python3 -B .scratch/r05/trap-battery.py` → `HOLES 10/13`
- §8 core lines: `.scratch/r05/o01core.py:35-42` (class set), `:206-251` (`guard_signals`; `:248-250` the `def:` → call conflation), `:254-270` (`embedded_sources`), `:273-284` (`_conditional_call`), `:287-350` (`scan_runner`; `:319-332` the class decision, `:338` `hazard`, `:289` unguarded `read_text`)
- §3 corroboration: `reports/round-34/scout/K03-guard-pattern.md:50-66` (§2a correction), `:47` (r7 unguarded), `:48` (r26 guarded write-only), `:93` (r19 embedded payload), `:188` (r19/r21/r29 citation list)
- Filed row deliberately not edited: `LOG.md:3560-3561` (the r26 hazard sentence) — recorded as an errata candidate in §3/Owed instead.
