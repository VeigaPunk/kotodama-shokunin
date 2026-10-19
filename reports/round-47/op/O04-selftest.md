# O04 — freshness-gate selftest control set (claim O, round 47)

- Seat: `O04` | role executor | claim `O` | round 47, loop 2
- Out path: `reports/round-47/op/O04-selftest.md` (the only write by this seat)
- Baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD` at seat start)
- Cut: 2026-10-19, lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`

**Scope.** This seat authors the **control set** for `tools/harness/claims-freshness.py` — the four
required controls (synthetic stale, synthetic fresh, could-not-evaluate, malformed) plus the probe,
polarity, baseline, and determinism controls the round's acceptance contract implies. It does **not**
land the tool: O01–O03 draft the implementation, O05–O07 file the r43/negative-control/anti-theater
demonstrations, and the integrator applies the assembled bytes.

At this cut the durable path is absent, verified:

```
$ ls tools/harness/claims-freshness.py
ls: cannot access 'tools/harness/claims-freshness.py': No such file or directory
```

What is delivered here is a spec that is **executable today**: a scratch reference gate implementing
the round's probe vocabulary, the 46-control selftest body that the assembled tool can embed, the
measured green run (46/46), and an 11-mutant battery proving the controls are not vacuous.

## 1. What the control set must prove

The O claim (`reports/round-47/claims.json:37-47`) requires a durable gate that re-derives each
claim's `before` at its `baseline_commit` through typed probes with declared polarity, flags STALE on
any contradiction, exits non-zero on stale, and treats `could-not-evaluate` as not-green
(`claims.json:47`). R01-44 §4.3 fixes the acceptance shape (`reports/round-44/review/R01-review.md:245-250`):
a per-claim `before_checks` list, baseline-only measurement via `git ls-tree`/`git show`, all-match
FRESH / any-mismatch STALE / no-checks CNE, exit 0/1/2, and no filed-byte writes.

The r44 prototype is the negative example this control set must outgrow: its own selftest was red at
**17/19** (`R01-review.md:241`; `reports/round-44/review/R02-review.md:217-221`) and its prose miner
false-positived on the novel phrasing "the llama-herding register slot is unbuilt"
(`R02-review.md:209`). Both defects are control-set defects, not tool-logic defects: a control that
does not assert the exact expected failure can be "green" while the fixture is wrong, and a control
that does not isolate prose from declared checks cannot detect prose mining.

## 2. Control matrix (46 controls)

All controls run inside `--selftest`; a control increments the denominator whether it passes or fails,
and the process exits non-zero if any control fails. IDs are stable names in the output, not just
counts — this is the fix for the r44 "seventeen checks collected" stale-count failure
(`R02-review.md:220`).

### V — verdict core (7)

| ID | Fixture | Expected | Guards |
|---|---|---|---|
| V1 | one `path_absent` target truly absent, `expect:true` | FRESH | all-match is FRESH |
| V2 | same check, target present | STALE | any-mismatch is STALE |
| V3 | 3 clauses, 1 mismatches (count 2 vs 1) | STALE | partial failure |
| V3b | same verdict | clause vector `[true,true,false]` | matching clauses still reported |
| V3c | same verdict | failing clause carries `measured:1`, `expect:2`, `ok:false` | measured value, not prose |
| V4 | `before_checks: []` | COULD-NOT-EVALUATE | empty ≠ green |
| V5 | `before_checks` key absent | COULD-NOT-EVALUATE | undeclared ≠ green |

### P — polarity and no prose mining (3)

| ID | Fixture | Expected | Guards |
|---|---|---|---|
| P1 | identical measurement, `expect` flipped | opposite `ok` | declared polarity, not a default |
| P2 | `before` says "llama-herding slot is unbuilt; no tool … unowned", checks are true | FRESH | the r44/R02 novel-phrasing false positive |
| P3 | `before` says "the gate is present and green", `path_absent` check is true | FRESH | prose is not evidence |

### K — every probe kind, both outcomes (16)

| ID | Probe | Expected | Guards |
|---|---|---|---|
| K1/K2 | `path_present` true / false | ok / mismatch | existence |
| K3/K4 | `grep_absent` miss / hit | ok / mismatch | absence-by-search |
| K4b/K4c | `grep_present` hit / miss | ok / mismatch | presence-by-search (R01 §4.3's 8th kind) |
| K5/K6 | `count_eq` equal / off by one | ok / mismatch (`measured==3`) | counts |
| K7/K8 | `sha256_eq` match / mismatch | ok / mismatch | byte pinning |
| K9/K10 | `topic_owner_absent` zero / one owner | ok / mismatch | ownership |
| K11/K12 | `capability_present` true / false | ok / mismatch | capability leg |
| K13 | capability carrier renamed to `renamed-witness.py` | ok, carrier named | not a literal-path lookup (anti-theater at unit level) |
| K14 | topic word in body prose only | ok | ownership = H1 + `- topic:` lines only |

### B — baseline, not worktree (3, real commits)

| ID | Fixture | Expected | Guards |
|---|---|---|---|
| B1 | `baseline_commit:7ceff59`, `path_absent:…basename-couples-resolver.py` | FRESH, exit 0 | file is **present in the worktree**; a worktree reader says STALE |
| B2 | same check at `6e9a30d` | STALE, exit 1 | measurement actually varies with the commit |
| B3 | `count_eq:corpus/knowledge/*/*.md`, `expect:223` at `6e9a30d` | FRESH, exit 0 | historical count stays 223 after C lands 224 |

### C — CLI exit contract (4)

| ID | Fixture | Expected | Guards |
|---|---|---|---|
| C1 | one FRESH claim | exit 0 | clean run |
| C2 | one CNE claim | non-zero, status COULD-NOT-EVALUATE | CNE ≠ green |
| C3 | FRESH + CNE | exit 1 | one ungrounded claim blocks dispatch |
| C4 | STALE + FRESH | exit 1, both verdicts present | mixed reporting |

### M — malformed inputs (11, each exit 2, no traceback)

| ID | Input | Expected |
|---|---|---|
| M1 | non-JSON text | exit 2 |
| M2 | top-level JSON array | exit 2 |
| M3 | missing `baseline_commit` | exit 2 |
| M4 | unresolvable `baseline_commit` (`deadbeef`) | exit 2 |
| M5 | claim missing `id` | exit 2 |
| M6 | claim missing `before` | exit 2 |
| M7 | `before_checks` not a list | exit 2 |
| M8 | unknown probe kind (`vibes_absent`) | exit 2 |
| M9 | check missing `target` | exit 2 |
| M10 | check missing `expect` | exit 2 |
| M11 | `expect:"true"` (string) | exit 2 |

### D — determinism (2)

| ID | Fixture | Expected | Guards |
|---|---|---|---|
| D1 | same document run twice | identical JSON and exit | no run-to-run drift |
| D2 | verdict JSON | no `time`/`rand` keys or values | no timestamp/randomness |

Count: 7 + 3 + 16 + 3 + 4 + 11 + 2 = **46**.

## 3. Schema decisions the controls pin

The tool is O01–O03's to assemble; these are the decisions the control set cannot leave ambiguous.

| Decision | Rule | Reason |
|---|---|---|
| check shape | `{clause, kind, target, expect, evidence_command?}` | R01 §4.3 names the field `probe_kind`, claims.json names no field. **One name only**; if the assembler adopts `probe_kind`, map it once in the loader and change the fixtures' `kind` in one place. Do not accept both silently. |
| `expect` | the measured state that makes the clause true; **required**, never defaulted | the r44 polarity bug: a gate cannot infer polarity from prose (`R01-review.md:239-241`) |
| `expect` types | bool for path/grep/topic/capability; int for count; 64 lowercase hex for sha | `"true"` is malformed, not truthy (M11) |
| `before_checks` missing | COULD-NOT-EVALUATE (exit 1) | an old claims file has no declared probes; it must not pass |
| `before_checks: []` | COULD-NOT-EVALUATE (exit 1) | same |
| `before_checks: {}` | malformed (exit 2) | wrong type, not an empty declaration |
| `before` missing | malformed (exit 2) | the gate has nothing to check |
| unknown kind | malformed (exit 2) | a probe registry with silent skips is theater |
| exit aggregation | 2 if any schema error; 1 if any STALE **or** CNE; 0 only all-FRESH | `claims.json:47` + R01 §4.3.2; exit 1 means "not dispatchable", not "stale" |
| count glob | `*` does not cross `/`; `**` does | `corpus/knowledge/*/*.md` must count 223, not every nested file |
| topic ownership | scan H1 (`# `) and `- topic:` lines only, word-boundary, case-insensitive | r44's divination/dream boundary lesson (`R01-review.md:293`, R01-44-12); body mentions are not ownership |
| capability | registry keyed by capability name → (path family, marker regexes), scanned at baseline | renaming the carrier must not hide the capability (K13); a literal path lookup is theater |
| baseline reader | `git ls-tree`/`git show` at `baseline_commit`; `FixtureBaseline` is **test-only** and must have no CLI constructor | B1 proves the worktree is not read; a `--baseline-root` flag would reopen that hole |
| output | stable JSON, sorted keys, no timestamps | D1/D2 |

## 4. Baseline anchors (measured, not asserted)

Historical commits are used deliberately: the round's C claim lands 223 → 224 at HEAD, and after the
gate itself lands `tools/harness/claims-freshness.py` exists at HEAD. A control anchored at HEAD would
change meaning during integration; these anchors do not.

```
$ git rev-parse 7ceff59 6e9a30d
7ceff59a0216a8ea21ee43262d9fc72abf770cee
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe

$ for c in 7ceff59 6e9a30d; do
    git cat-file -e $c:tools/harness/basename-couples-resolver.py && echo "$c PRESENT" || echo "$c ABSENT"
    git cat-file -e $c:tools/harness/claims-freshness.py && echo "$c GATE PRESENT" || echo "$c GATE ABSENT"
    git ls-tree -r --name-only $c -- corpus/knowledge | grep -c '\.md$'
  done
7ceff59 ABSENT
7ceff59 GATE ABSENT
223
6e9a30d PRESENT
6e9a30d GATE ABSENT
223

$ sha256sum tools/harness/basename-couples-resolver.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64

$ git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1

$ git cat-file -e 7ceff59:corpus/knowledge/myth-symbol/mineral-stone-symbolism.md && echo PRESENT
PRESENT
```

The same facts the r43/R01 probes measured (`R01-review.md:227-241`): at the r43 baseline the
resolver is absent, the witness extractor is present, the lithic owner exists; the difference is
that these controls use them as **fixtures**, not as the demonstration.

## 5. Fenced selftest body (drop-in)

**Seam.** The block below calls six module-level symbols and one test double. The assembled tool must
provide them (names may be adapted in one place, but the assertions must not be weakened):

```
PROBE_KINDS: dict/set of the 8 kinds
CAPABILITIES: dict[name] -> (path_glob, [marker_regex, ...])
SchemaError
FixtureBaseline(files: dict[str, str])      # test-only; no CLI constructor
evaluate_check(check, baseline, registry=None) -> (ok: bool, measured)
evaluate_claim(claim, baseline, registry=None) -> {id, status, clauses:[...]}
```

`selftest(root=...)` must pass the **repo root**, resolved from the tool file
(`Path(__file__).resolve().parents[2]`), not the caller's cwd, because B1–B3 shell out to
`git -C root`. `--selftest` is expected to print one `PASS`/`FAIL` line per control and end with
`SELFTEST OK: 46/46 controls`, exit 0 on all-pass.

````python
def selftest(quiet=False, root=None):
    root = root or os.getcwd()
    passed, failed = 0, []

    def check(name, condition, detail=""):
        nonlocal passed
        if condition:
            passed += 1
            if not quiet:
                print("PASS " + name)
        else:
            failed.append(name)
            if not quiet:
                print("FAIL " + name + (("  [" + str(detail) + "]") if detail != "" else ""))

    def cli(doc_text):
        """Run the CLI on a fixture file; return (exit, parsed_json_or_None, stderr)."""
        import tempfile

        tmp = tempfile.mkdtemp(prefix="o04-selftest-", dir=os.environ.get("TMPDIR"))
        path = os.path.join(tmp, "claims.json")
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(doc_text)
        res = subprocess.run(
            [sys.executable, "-B", os.path.abspath(__file__), "--claims", path, "--json"],
            capture_output=True,
            text=True,
            encoding="utf-8",
            cwd=root,
        )
        parsed = None
        try:
            parsed = json.loads(res.stdout)
        except Exception:
            parsed = None
        return res.returncode, parsed, res.stderr

    def doc(commit, claims):
        return {"round": 0, "baseline_commit": commit, "claims": claims}

    def dump(obj):
        return json.dumps(obj, sort_keys=True)

    # ---- fixtures -------------------------------------------------------
    absent_tree = {}
    present_tree = {"tools/harness/live.py": "x\n"}
    fixture_checks = {
        "absent_ok": {"clause": "tool absent", "kind": "path_absent",
                      "target": "tools/harness/live.py", "expect": True},
        "absent_bad": {"clause": "tool absent", "kind": "path_absent",
                       "target": "tools/harness/live.py", "expect": False},
    }

    # ---- V: verdict core ------------------------------------------------
    v = evaluate_claim({"id": "V1", "before": "no tool",
                        "before_checks": [fixture_checks["absent_ok"]]},
                       FixtureBaseline(absent_tree))
    check("V1 single path_absent satisfied -> FRESH", v["status"] == "FRESH", v["status"])
    v = evaluate_claim({"id": "V2", "before": "no tool",
                        "before_checks": [fixture_checks["absent_ok"]]},
                       FixtureBaseline(present_tree))
    check("V2 single path_absent violated -> STALE", v["status"] == "STALE", v["status"])
    v = evaluate_claim({"id": "V3", "before": "no tool", "before_checks": [
        {"clause": "gone.py absent", "kind": "path_absent",
         "target": "tools/harness/gone.py", "expect": True},
        {"clause": "live.py present", "kind": "path_present",
         "target": "tools/harness/live.py", "expect": True},
        {"clause": "two python files", "kind": "count_eq",
         "target": "tools/**/*.py", "expect": 2},
    ]}, FixtureBaseline(present_tree))
    check("V3 multi-clause 1/3 mismatches -> STALE", v["status"] == "STALE", v["status"])
    check("V3b the two matching clauses still report ok",
          [c["ok"] for c in v["clauses"]] == [True, True, False],
          [c["ok"] for c in v["clauses"]])
    check("V3c failing clause reports measured value not prose",
          v["clauses"][2]["measured"] == 1 and v["clauses"][2]["ok"] is False,
          v["clauses"][2])
    v = evaluate_claim({"id": "V4", "before": "x", "before_checks": []},
                       FixtureBaseline({}))
    check("V4 empty before_checks -> COULD-NOT-EVALUATE", v["status"] == "COULD-NOT-EVALUATE",
          v["status"])
    v = evaluate_claim({"id": "V5", "before": "x"}, FixtureBaseline({}))
    check("V5 absent before_checks -> COULD-NOT-EVALUATE (not FRESH)",
          v["status"] == "COULD-NOT-EVALUATE", v["status"])

    # ---- P: polarity / no prose mining ----------------------------------
    a, _ = evaluate_check({"kind": "path_absent", "target": "tools/harness/live.py",
                           "expect": True}, FixtureBaseline(present_tree))
    b, _ = evaluate_check({"kind": "path_absent", "target": "tools/harness/live.py",
                           "expect": False}, FixtureBaseline(present_tree))
    check("P1 same measurement with flipped expect -> opposite verdict", a != b, (a, b))
    llama = {"id": "P2", "before":
             "the llama-herding register slot is unbuilt; no tool, resolver or "
             "instrument exists and the topic is unowned",
             "before_checks": [{"clause": "target path absent", "kind": "path_absent",
                                "target": "tools/harness/live.py", "expect": True}]}
    v = evaluate_claim(llama, FixtureBaseline(absent_tree))
    check("P2 novel prose with true checks -> FRESH (no prose mining)", v["status"] == "FRESH",
          v["status"])
    v = evaluate_claim({"id": "P3", "before": "the gate is present and green",
                        "before_checks": [fixture_checks["absent_ok"]]},
                       FixtureBaseline(absent_tree))
    check("P3 prose contradicting the checks is ignored", v["status"] == "FRESH", v["status"])

    # ---- K: every probe kind, both outcomes -----------------------------
    base = FixtureBaseline({
        "corpus/knowledge/a/one.md": "# One\n\n- topic: alpha-subject\n\nBody mentions beta.\n",
        "corpus/knowledge/b/two.md": "# Two\n\n- topic: other\n\nBody mentions gamma.\n",
        "tools/harness/live.py": "def classify(x):\n    return 'couples'\n# selftest\n",
        "tools/harness/renamed-witness.py": "def classify(x):\n    return 'couples'\n# selftest\n",
        "corpus/knowledge/a/three.md": "# Three\n\n- topic: third\n",
    })
    ok, _ = evaluate_check({"kind": "path_present", "target": "tools/harness/live.py",
                            "expect": True}, base)
    check("K1 path_present true -> ok", ok)
    ok, _ = evaluate_check({"kind": "path_present", "target": "tools/harness/nope.py",
                            "expect": True}, base)
    check("K2 path_present false -> mismatch", not ok)
    ok, _ = evaluate_check({"kind": "grep_absent", "pattern": "zeta", "target": "corpus/",
                            "expect": True}, base)
    check("K3 grep_absent no hit -> ok", ok)
    ok, _ = evaluate_check({"kind": "grep_absent", "pattern": "beta", "target": "corpus/",
                            "expect": True}, base)
    check("K4 grep_absent hit -> mismatch", not ok)
    ok, _ = evaluate_check({"kind": "grep_present", "pattern": "beta", "target": "corpus/",
                            "expect": True}, base)
    check("K4b grep_present hit -> ok", ok)
    ok, _ = evaluate_check({"kind": "grep_present", "pattern": "zeta", "target": "corpus/",
                            "expect": True}, base)
    check("K4c grep_present miss -> mismatch", not ok)
    ok, measured = evaluate_check({"kind": "count_eq", "target": "corpus/knowledge/*/*.md",
                                   "expect": 3}, base)
    check("K5 count_eq equal -> ok", ok and measured == 3, measured)
    ok, measured = evaluate_check({"kind": "count_eq", "target": "corpus/knowledge/*/*.md",
                                   "expect": 4}, base)
    check("K6 count_eq off by one -> mismatch", not ok and measured == 3, measured)
    digest = hashlib.sha256(b"def classify(x):\n    return 'couples'\n# selftest\n").hexdigest()
    ok, _ = evaluate_check({"kind": "sha256_eq", "target": "tools/harness/live.py",
                            "expect": digest}, base)
    check("K7 sha256_eq match -> ok", ok)
    ok, _ = evaluate_check({"kind": "sha256_eq", "target": "tools/harness/live.py",
                            "expect": "0" * 64}, base)
    check("K8 sha256_eq mismatch -> mismatch", not ok)
    ok, measured = evaluate_check({"kind": "topic_owner_absent", "target": "alpha",
                                   "expect": True}, base)
    check("K9 topic_owner_absent zero owners -> ok", ok and measured["owner_count"] == 0, measured)
    ok, measured = evaluate_check({"kind": "topic_owner_absent", "target": "other",
                                   "expect": True}, base)
    check("K10 topic owner present -> mismatch", (not ok) and measured["owner_count"] == 1,
          measured)
    ok, measured = evaluate_check({"kind": "capability_present", "target": "couples-policy-resolver",
                                   "expect": True}, base)
    check("K11 capability_present true -> ok", ok and measured["present"] is True, measured)
    ok, _ = evaluate_check({"kind": "capability_present", "target": "claims-freshness-gate",
                            "expect": True}, base)
    check("K12 capability_present false -> mismatch", not ok)
    ok, measured = evaluate_check({"kind": "capability_present", "target": "couples-policy-resolver",
                                   "expect": True}, FixtureBaseline(
        {"tools/harness/renamed-witness.py":
         "def classify(x):\n    return 'couples'\n# selftest\n"}))
    check("K13 renamed carrier still satisfies capability (not a path lookup)",
          ok and measured["carrier"] == "tools/harness/renamed-witness.py", measured)
    body_only = FixtureBaseline({
        "corpus/knowledge/a/one.md": "# One\n\n- topic: alpha-subject\n\n"
                                     "The body discusses the lithic register at length.\n",
    })
    ok, measured = evaluate_check({"kind": "topic_owner_absent", "target": "lithic",
                                   "expect": True}, body_only)
    check("K14 body prose is not a topic owner (header scan only)", ok, measured)

    # ---- B: baseline, not worktree (real commits) -----------------------
    doc_fresh = doc("7ceff59", [{
        "id": "B1", "before": "resolver absent at baseline",
        "before_checks": [{"clause": "resolver absent", "kind": "path_absent",
                           "target": "tools/harness/basename-couples-resolver.py",
                           "expect": True}]}])
    code, parsed, err = cli(dump(doc_fresh))
    check("B1 absent at 7ceff59 but present in worktree -> FRESH/exit0",
          code == 0 and parsed and parsed["verdicts"][0]["status"] == "FRESH",
          (code, parsed, err[-200:]))
    doc_stale = doc("6e9a30d", [{
        "id": "B2", "before": "resolver absent at baseline",
        "before_checks": [{"clause": "resolver absent", "kind": "path_absent",
                           "target": "tools/harness/basename-couples-resolver.py",
                           "expect": True}]}])
    code, parsed, err = cli(dump(doc_stale))
    check("B2 present at 6e9a30d -> STALE/exit1",
          code == 1 and parsed and parsed["verdicts"][0]["status"] == "STALE",
          (code, parsed, err[-200:]))
    doc_count = doc("6e9a30d", [{
        "id": "B3", "before": "total 223",
        "before_checks": [{"clause": "total 223", "kind": "count_eq",
                           "target": "corpus/knowledge/*/*.md", "expect": 223}]}])
    code, parsed, err = cli(dump(doc_count))
    check("B3 corpus count pinned at 223 on the historical commit",
          code == 0 and parsed and parsed["verdicts"][0]["status"] == "FRESH",
          (code, parsed, err[-200:]))

    # ---- C/M: CLI exit contract -----------------------------------------
    code, parsed, _ = cli(dump(doc("6e9a30d", [{
        "id": "C1", "before": "gate absent",
        "before_checks": [{"clause": "gate absent", "kind": "path_absent",
                           "target": "tools/harness/claims-freshness.py",
                           "expect": True}]}])))
    check("C1 all fresh -> exit 0", code == 0 and parsed and parsed["summary"]["fresh"] == 1,
          (code, parsed))
    code, parsed, _ = cli(dump(doc("6e9a30d", [{
        "id": "C2", "before": "no checks"}])))
    check("C2 could-not-evaluate -> non-zero, never green",
          code != 0 and parsed and parsed["verdicts"][0]["status"] == "COULD-NOT-EVALUATE",
          (code, parsed))
    code, parsed, _ = cli(dump(doc("6e9a30d", [
        {"id": "C3", "before": "no checks"},
        {"id": "C4", "before": "gate absent",
         "before_checks": [{"clause": "gate absent", "kind": "path_absent",
                            "target": "tools/harness/claims-freshness.py",
                            "expect": True}]}])))
    check("C3 fresh + CNE -> exit 1 (CNE is not green)", code == 1, (code, parsed))
    code, parsed, _ = cli(dump(doc("6e9a30d", [
        {"id": "C5", "before": "resolver absent",
         "before_checks": [{"clause": "resolver absent", "kind": "path_absent",
                            "target": "tools/harness/basename-couples-resolver.py",
                            "expect": True}]},
        {"id": "C6", "before": "gate absent",
         "before_checks": [{"clause": "gate absent", "kind": "path_absent",
                            "target": "tools/harness/claims-freshness.py",
                            "expect": True}]}])))
    check("C4 mixed stale+fresh -> exit 1, both verdicts present",
          code == 1 and [v["status"] for v in parsed["verdicts"]] == ["STALE", "FRESH"],
          (code, parsed))

    # malformed -> exit 2, no traceback
    malformed = [
        ("M1 non-JSON", "not json at all"),
        ("M2 top-level array", "[]"),
        ("M3 missing baseline_commit", dump({"claims": [{"id": "x", "before": "y"}]})),
        ("M4 unresolvable baseline_commit", dump({"baseline_commit": "deadbeef",
                                                  "claims": [{"id": "x", "before": "y"}]})),
        ("M5 claim missing id", dump({"baseline_commit": "6e9a30d",
                                      "claims": [{"before": "y"}]})),
        ("M6 claim missing before", dump({"baseline_commit": "6e9a30d",
                                          "claims": [{"id": "x"}]})),
        ("M7 before_checks not a list", dump({"baseline_commit": "6e9a30d",
                                              "claims": [{"id": "x", "before": "y",
                                                          "before_checks": {}}]})),
        ("M8 unknown probe kind", dump({"baseline_commit": "6e9a30d", "claims": [{
            "id": "x", "before": "y", "before_checks": [
                {"clause": "c", "kind": "vibes_absent", "target": "p", "expect": True}]}]})),
        ("M9 check missing target", dump({"baseline_commit": "6e9a30d", "claims": [{
            "id": "x", "before": "y", "before_checks": [
                {"clause": "c", "kind": "path_absent", "expect": True}]}]})),
        ("M10 check missing expect", dump({"baseline_commit": "6e9a30d", "claims": [{
            "id": "x", "before": "y", "before_checks": [
                {"clause": "c", "kind": "path_absent", "target": "p"}]}]})),
        ("M11 expect wrong type", dump({"baseline_commit": "6e9a30d", "claims": [{
            "id": "x", "before": "y", "before_checks": [
                {"clause": "c", "kind": "path_absent", "target": "p", "expect": "true"}]}]})),
    ]
    for name, text in malformed:
        code, parsed, err = cli(text)
        check("%s -> exit 2, no traceback" % name,
              code == 2 and "Traceback" not in err, (code, err[-160:]))

    # ---- D: determinism --------------------------------------------------
    code1, out1, _ = cli(dump(doc("6e9a30d", [{
        "id": "D1", "before": "gate absent",
        "before_checks": [{"clause": "gate absent", "kind": "path_absent",
                           "target": "tools/harness/claims-freshness.py",
                           "expect": True}]}])))
    code2, out2, _ = cli(dump(doc("6e9a30d", [{
        "id": "D1", "before": "gate absent",
        "before_checks": [{"clause": "gate absent", "kind": "path_absent",
                           "target": "tools/harness/claims-freshness.py",
                           "expect": True}]}])))
    check("D1 two runs -> identical verdict JSON and exit", (code1, out1) == (code2, out2))
    check("D2 verdict JSON has no timestamp/random field",
          "time" not in json.dumps(out1).lower() and "rand" not in json.dumps(out1).lower())

    total = passed + len(failed)
    print("SELFTEST %s: %d/%d controls" % ("OK" if not failed else "FAIL", passed, total))
    if failed and not quiet:
        print("  failed: " + ", ".join(failed))
    if quiet and failed:
        print("  failed: " + ", ".join(failed))
    return not failed
````

## 6. Evidence — measured runs

The reference file is scratch-only and is evidence for the spec, not the deliverable:
`.scratch/o04/ref_gate.py`, sha256 `fc864dc685494692028f07c19cb3f4d22bbe4f1e19321418b7f417238f35eac8`
(the digest moves whenever the reference is edited; the fenced block above is the artifact that
matters).

Green run:

```
$ python3 -B .scratch/o04/ref_gate.py --selftest | tail -3
PASS D1 two runs -> identical verdict JSON and exit
PASS D2 verdict JSON has no timestamp/random field
SELFTEST OK: 46/46 controls
$ echo $?
0
```

Mutation battery — 11 deliberately broken gates, each must fail the selftest, and the failing control
must name the broken property (`python3 -B .scratch/o04/mutate.py`, exit 0 when all are caught):

| Mutant | Break | Caught by (first) |
|---|---|---|
| `worktree_baseline` | reads the worktree | B1 |
| `polarity_ignored` | ignores `expect` | P1 |
| `unknown_kind_passthrough` | accepts + passes unknown kinds | M8 |
| `cne_exit_zero` | CNE is green | C2, C3 |
| `count_always_eq` | counts never fail | V3, V3b, V3c, K6 |
| `sha_always_eq` | digests never fail | K8 |
| `topic_scans_body` | body prose is ownership | K14 |
| `capability_is_path` | capability = literal path | K11, K13 |
| `malformed_crash` | traceback instead of exit 2 | M3 |
| `always_fresh` | never STALE | V2, V3, B2, C4 |
| `always_exit_zero` | exits 0 always | B2, C4 |

Result: `11 mutants, 11 caught`. Two earlier single-layer mutants (schema-only and evaluator-only
unknown-kind bypasses) survived because each guard masked the other; they were merged into
`unknown_kind_passthrough`, which removes both and is caught. This is the control set's own anti-theater
evidence: it detects a gate that looks right but does not measure.

## 7. What this control set does not cover

- **The r43 positive regression.** O05 annotates `reports/round-43/claims.json` with `before_checks`
  encoding its premises (`r43 claims.json:27,40,53`); my B1/B2 controls prove the same mechanism on
  the same commits, but do not run the filed r43 claims. Run over the unannotated r43 file, the gate
  correctly returns 3× COULD-NOT-EVALUATE and exit 1 — that is the expected pre-annotation result,
  not the regression.
- **The r44 negative control.** O06 owns the filed fresh-claim demo. My C1/V1 controls are its
  synthetic equivalent.
- **The anti-theater demo.** O07 owns the r43 mutation demo. K13 is its unit-level core.
- **Capability registry content.** The reference's `CAPABILITIES` markers (`couples`, `selftest`,
  `classif`; `before_checks`, `baseline_commit`, `STALE`) are fixture-level; O05/O07 must pin the
  real family against the witness `d8d23a26…` and the successor `43ce341f…`. `to-verify`.
- **The landed tool's digest.** This report's reference sha is not the tool's sha; the integrator's
  `calib/` demonstration must name the landed digest and baseline.

## 8. Handoff

1. O12 assembles the tool from O01–O03; embed the §5 block as `selftest()` (or a module-level
   `selftest.py` invoked by `--selftest`).
2. Resolve `root` from the tool file, not cwd, before B1–B3.
3. If the assembler uses `probe_kind` instead of `kind`, change the loader once and the fixtures'
   key once; do **not** accept both.
4. Run `python3 tools/harness/claims-freshness.py --selftest` from the lane root; expected
   `SELFTEST OK: 46/46 controls`, exit 0.
5. If any control fails, the tool is not green and O is not improved — report the failing ID, not a
   count.
6. Do not add a CLI flag that constructs `FixtureBaseline`; the baseline reader must stay
   `git ls-tree`/`git show` at `baseline_commit`.
