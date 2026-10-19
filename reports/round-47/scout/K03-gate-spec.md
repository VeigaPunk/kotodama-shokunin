# K03 — durable claims-freshness gate: exact API, probe vocabulary, exit contract

- Seat: `K03` | role `scout` | claim `O` (operability) | round 47, loop 2
- Out path: `reports/round-47/scout/K03-gate-spec.md` (the only deliverable written by this seat)
- Measured at HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`), 2026-10-19
- Read: `reports/round-44/review/R01-review.md` §4 (`:212-254`, six-part contract at `:245-250`); `reports/round-44/review/R02-review.md:190-245,410-440`; `reports/round-43/claims.json:27,40,53`; `reports/round-43/review/R01-review.md:400` (R01-43-12); `reports/round-44/claims.json:7,27,40,52`; `.scratch/ca01/claims-freshness.py` (915 lines, sha256 `dd88d9e12bda5ade6b4f93864db138e0a5ce54b0ef5cbcf6e4f5050783121434`)
- Boundary: read-only. I ran the `.scratch` prototype and my own probes with `TMPDIR=$PWD/.scratch`; I edited no filed byte, staged nothing under `corpus/`, ran no round runner, and made no git/network/install mutation. `git status --porcelain` at write time → `?? reports/round-46/review/`, `?? reports/round-47/` only (both untracked round surface, not filed bytes).

This spec is **normative for O01–O15 and W01**: where it says MUST, a durable implementation that omits it fails the r47 O claim's own `after_required` (`reports/round-47/claims.json:37-48`). It deliberately supersedes two conventions in the r44 prototype: its exit numbering and its prose miner.

---

## 1. What this spec settles

`reports/round-44/review/R01-review.md:245-250` set a six-part minimum contract. Every part is answered here:

| R01-44 §4.3 part | Section |
|---|---|
| 1. per-claim `before_checks` with `{clause, probe_kind, target, expect, evidence_command}`, closed probe set, evaluated at `baseline_commit` via git plumbing, never worktree | §3.3–§3.7, §4 |
| 2. `STALE` if any clause mismatches; `FRESH` only if all match; `could-not-evaluate` if no checks; non-zero for unevaluable; 0/1/2 exits | §3.8–§3.9 |
| 3. r43 positive regression: O and C flagged, Ca not | §7.1 |
| 4. r44 negative control at `c9f4eaa` | §7.2 |
| 5. anti-theater mutation (witness rename, live literals) | §7.3, §8 |
| 6. no writes to `reports/round-43/**` or any filed byte; new `calib/` artifact naming tool digest and baseline | §3.10, §7, §9 |

The r47 O claim additionally requires `could-not-evaluate != green` and "exit non-zero on stale" (`reports/round-47/claims.json:37-48`); §3.9 makes both mechanical.

---

## 2. Measured state of the r44 prototype

All commands below were run from the lane root, read-only.

### 2.1 The regression that works

```
$ python3 -B .scratch/ca01/claims-freshness.py --claims reports/round-43/claims.json
[O]  operability -- STALE (0/2 premises hold)
[C]  coverage     -- STALE (2/3 premises hold)
[Ca] calibration  -- FRESH (1/1 premises hold)
summary: 1 fresh, 2 stale, 0 unverifiable, 2 ungrounded clause(s)
REFUSE: claims O, C have a `before` already false at 7ceff59…; do not dispatch.
exit 2
```

The ownership evidence is the real one: `topic_owners` returns 3 hits, all in `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` (H1 `:1`, `- gap filled:` `:3`, `- topic:` `:5`). The counts (26/223) pass. This confirms the r43 defect is an **ownership** failure, not a count failure — a count-only gate would call C fresh.

### 2.2 The defects, with measured reproductions

| ID | Defect | Measured evidence | Root cause | Required fix |
|---|---|---|---|---|
| **D1** | Red selftest: `grep_absent` fixture | `--selftest` → `FAIL grep_absent hit fails`; `selftest 17/19 FAIL` exit 1 | the fixture glob `corpus/knowledge/beta/*.md` (`:791`) matches 0 files, so `grep_absent` measured "no hit" and passed; the control asserts failure | negative controls MUST use a real hit fixture; `grep_absent` MUST return `could-not-evaluate` on a zero-file universe (§4.3) |
| **D2** | Stale check-count assertion | `FAIL seventeen checks collected (18)` at `:876` | hardcoded `len(checks) == 17` while 18 ran | assert `set(observed_names) == set(EXPECTED_NAMES)`; no numeric literal (§6.4) |
| **D3** | Novel-phrasing false positive | synthetic `"the llama-herding register slot is unbuilt"` → `E3a-unowned-slot`, `51 owner hit(s) for register`, verdict STALE | E3a captures one hyphen-word before `slot` (`:476-485`), yielding the generic term `register` | declared `topic_owner_absent` topics; reject a topic whose tokens are **all** generic; in opt-in legacy mode a generic capture is `could-not-evaluate`, never stale (§4.6) |
| **D4** | Unknown probe kind treated as stale | declared `{"kind":"capability_vibes"}` → `probe error: unknown probe kind`, verdict STALE, exit 2 | `evaluate_probe` raises `ValueError` (`:360`), `analyze_claim` catches it and sets `passed=False` | classify structural errors at parse time as **malformed**, exit 2, never a verdict (§3.9) |
| **D5** | Vacuous globs pass | `grep_absent` on `corpus/knowledge/beta/*.md` and on `corpus/knowledge/nonexistent/*.md` both → `(True, [], "0 hit(s)")`; a declared claim using it → FRESH | absence over an empty universe is vacuously true | `grep_absent` requires `min_files` (default 1); below it → could-not-evaluate; `topic_owner_absent` on an empty partition → could-not-evaluate (§4) |
| **D6** | Polarity is inferred, not declared | R01's own first probe marked r43 O's "resolver exists" premise fresh because it encoded the wrong asserted state (`reports/round-44/review/R01-review.md:239`) | legacy miner derives polarity from prose patterns | every check MUST carry `expect: true|false`; the measured predicate is defined by the probe kind (§3.5, §4.1) |
| **D7** | Exit numbering inverted vs the r47 contract | prototype docstring `:69-76`: 1=usage, 2=stale, 3=unverifiable | written for r44, before the r47 O/W contracts fixed 0/1/2 | adopt §3.9 verbatim: 0 fresh, 1 stale, 2 malformed, 3 could-not-evaluate |
| **D8** | Family scan admits unrelated gates | r43 O output lists `tools/gates/provenance-audit.py:12` as a "couples family candidate" because its text mentions `- couples:` | token scan of header/docstring text, not structure | `capability_present` MUST use the closed AST registry (§5) and exclude `tools/gates/frozen/**` by default |
| **D9** | No clause↔`before` binding | declared probes are accepted even if unrelated to the prose | no integrity check | `clause` MUST be a substring of `before` after whitespace normalization, else malformed (exit 2) |

D1 and D5 share a root; fixing the probe semantics also fixes the fixture, but the fixture MUST still be repaired so the control is a genuine positive.

---

## 3. Normative API

### 3.1 Identity and runtime

- Path: `tools/harness/claims-freshness.py` (the r47 O claim's durable path; `tools/harness/` is where the other instruments live).
- Python 3, **stdlib only**; `sys.dont_write_bytecode = True`; shebang `#!/usr/bin/env python3`.
- Read-only: opens inputs read-only, uses only read-only git plumbing (`rev-parse`, `cat-file -t`, `ls-tree`, `cat-file blob`, `merge-base --is-ancestor`), writes only stdout/stderr. No `--write`, no `--fix`, no corpus or report staging.
- `VERSION` string exposed by `--version`; the report carries it.

### 3.2 CLI

```
python3 tools/harness/claims-freshness.py --selftest
python3 tools/harness/claims-freshness.py --claims <claims.json> [--checks <overlay.json>]
        [--root <repo>] [--at <commit-ish>] [--json] [--quiet] [--require-head]
        [--allow-worktree] [--version]
```

| Flag | Meaning |
|---|---|
| `--claims PATH` | input claims file (worktree path; required in gate mode) |
| `--checks PATH` | optional sidecar overlay; merge by claim id; overlay entries replace in-file `before_checks` for the same id |
| `--root PATH` | repo root for git plumbing (default `.`); resolved with `git -C` |
| `--at REF` | measure at `REF` instead of `claims.baseline_commit`; recorded as a deviation. `worktree` refused unless `--allow-worktree` |
| `--json` | emit the report as JSON (schema §3.10) |
| `--quiet` | one line per claim + summary; no evidence lines |
| `--require-head` | pre-dispatch mode: if `baseline_resolved != HEAD`, the run is `could-not-evaluate` (exit 3), not silently green |
| `--allow-worktree` | permits `--at worktree`; report marks `source: "worktree"` and the run cannot be cited as baseline evaluation |
| `--selftest` | run the synthetic control set (§6); 0 pass / 1 fail |
| `--version` | print version and exit 0 |

`--selftest` is isolated: it MUST NOT resolve git, contact the network, or write outside `TMPDIR`.

### 3.3 Input A — `claims.json`

The existing round schema is unchanged. Required for gate mode:

| Field | Rule |
|---|---|
| `baseline_commit` | non-empty string, present at top level; resolved as a commit (§3.6). Its absence is malformed (exit 2), even with `--at`. |
| `claims` | array; each entry has unique `id` (string), `axis`, `before` (string). A missing/duplicate `id` or missing `before` is malformed. |
| `before_checks` | optional per claim: array of check records (§3.5). If absent and no overlay entry exists, the claim is `could-not-evaluate`. |

The claims file and the overlay are **inputs read from disk**. Targets are never read from the worktree. The claims file need not exist at `baseline_commit` — verified: `git cat-file -e 7ceff59:reports/round-43/claims.json` → absent, while the gate must still read the worktree file as input. State this in the tool docstring so it is not "fixed" later.

### 3.4 Input B — checks overlay

```json
{
  "schema": "kotodama-claims-freshness-checks-v1",
  "round": 43,
  "baseline_commit": "7ceff59",
  "claims_sha256": "9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b",
  "checks": {"O": [Check, ...], "C": [...], "Ca": [...]}
}
```

Rules:

- `schema` MUST equal the literal above; `round` MUST equal the claims file's `round`; `baseline_commit` MUST resolve to the same commit as the claims file's `baseline_commit` (compare resolved shas, not the declared spellings), else malformed.
- `claims_sha256` MUST equal the sha256 of the claims file bytes, else malformed. This is how a successor artifact re-derives r43's premises **without editing the filed file**.
- `checks` keys MUST be claim ids present in the claims file; unknown ids are malformed.
- An overlay is authoritative for the ids it names; in-file `before_checks` remain for others.

### 3.5 Check record

```json
{
  "clause": "no durable instrument implements the r39 basename-couples policy",
  "probe_kind": "capability_present",
  "target": {"capability": "couples_census", "scope": "tools/**.py"},
  "expect": false,
  "evidence_command": "git ls-tree -r -z --name-only 7ceff59 -- tools/"
}
```

| Field | Rule |
|---|---|
| `clause` | verbatim fragment of the claim's `before` after collapsing runs of whitespace; MUST be a substring, else malformed (D9). Its only role is the human binding. |
| `probe_kind` | one of the seven in §4; anything else is malformed (D4). |
| `target` | object, kind-specific (§4). Unknown keys are malformed (typo guard). |
| `expect` | JSON boolean, required. The check passes iff `measured == expect` (D6). |
| `evidence_command` | optional string, recorded verbatim in the report; **never executed** (no shell, no injection, deterministic). If absent, the renderer synthesizes a git command from `target`. |

### 3.6 Baseline resolution and tree access

1. `ref = --at or claims.baseline_commit`. If `ref == "worktree"` and `--allow-worktree` is absent → malformed.
2. `git -C ROOT cat-file -t REF` → `commit|tag|tree|blob`. A `tag` is accepted; `tree`/`blob` are malformed.
3. `git -C ROOT rev-parse --verify --quiet REF^{commit}` → full sha. Failure → malformed (exit 2), with the git stderr in the report.
4. Record `baseline.declared` (verbatim), `baseline.resolved` (full sha), `baseline.kind` (`sha|short-sha|tag|branch`).
5. `baseline.head = git rev-parse HEAD`; `baseline.relation = equal | ancestor | unreachable` via `git merge-base --is-ancestor RESOLVED HEAD`. With `--require-head`, `relation != equal` → every claim `could-not-evaluate` and exit 3.
6. Tree listing: `git -C ROOT ls-tree -r -z --name-only RESOLVED`, split on NUL. Never `os.walk`, never `pathlib.rglob`, never the worktree.
7. Blob bytes: `git -C ROOT cat-file blob RESOLVED:PATH` (raw bytes for `sha256_eq`; UTF-8 with `errors="replace"` for text scans).

`--at` is a **measurement override, not a claim re-declaration**. The overlay's `baseline_commit` is validated against the claims file's declared baseline (both must name the same commit, e.g. `7ceff59` in the r43 demo); `--at` then changes where probes measure and is recorded in `deviation`. This is what makes §7.4's state flip lawful: the checks and the claim stay fixed while only the measurement baseline moves.

`--at worktree` (only with `--allow-worktree`) may use the filesystem for measurement, sets `source: "worktree"`, and MUST NOT be cited as baseline evaluation.

### 3.7 Path and glob semantics

- All `target` paths/globs are repo-relative POSIX paths. Reject absolute paths and any segment `..` (malformed).
- Glob translation: `*` matches any run of characters **except `/`**; `**` matches any run **including `/`**; `?` matches one non-`/` character; `[...]` classes allowed. Implement with an explicit regex translation, not `fnmatch` (Python's `fnmatch` lets `*` cross `/`, which would make `corpus/knowledge/*/*.md` match deeper nesting).
- `tools/**.py` therefore matches `tools/a.py` and `tools/harness/a.py`; `corpus/knowledge/*/*.md` matches exactly the two-level partition layout.
- Case-sensitive matching on the git path list.

### 3.8 Verdict algorithm

Per check:

| status | condition |
|---|---|
| `match` | `measured == expect` |
| `mismatch` | `measured != expect` |
| `unevaluable` | the probe's universe is empty, a required blob cannot be parsed, or `--require-head` drift applies |
| `malformed` | structural error: unknown kind/capability, missing/extra target field, wrong type, bad sha, bad glob, generic topic, clause not in `before` |

Per claim:

1. `stale` if **any** check is `mismatch`;
2. else `could-not-evaluate` if the claim has **no checks** or **any** check is `unevaluable`;
3. else `fresh` (all checks `match`).

A `malformed` check aborts the whole run before verdicts (exit 2), because the input is not a valid contract.

### 3.9 Exit codes

| Exit | Meaning |
|---|---|
| **0** | every claim `fresh` |
| **1** | at least one claim `stale` — REFUSE to dispatch |
| **2** | malformed input or usage error |
| **3** | no stale claim, but at least one `could-not-evaluate` — REFUSE to dispatch |

Precedence: malformed is decided first (parse/validate, no verdicts); otherwise `1` if any stale; otherwise `3` if any unevaluable; otherwise `0`.

Why `3`: O10's contract says "exit 2 for malformed, and could-not-evaluate produces a non-zero exit (never green)". A distinct `3` preserves the six-part contract's distinction between "the premise is false" and "the premise could not be measured". If the integrator insists on exactly `{0,1,2}`, folding `3` into `1` is the only lawful fallback; folding it into `0` is forbidden.

**Do not copy the prototype's numbering** (`:69-76`: 1=usage, 2=stale, 3=unverifiable). O03/O10 must test the new mapping.

`--selftest` uses its own contract: `0` all controls pass, `1` any control fails. It never returns `2`/`3` unless a control deliberately exercises the parser, in which case the parser's return is asserted, not propagated as the process exit.

### 3.10 Report schema (`--json`)

```json
{
  "gate": "claims-freshness",
  "schema": "kotodama-claims-freshness-v1",
  "version": "1.0",
  "tool": {"path": "tools/harness/claims-freshness.py", "sha256": "<digest of __file__ bytes>"},
  "round": 43,
  "claims_file": "reports/round-43/claims.json",
  "claims_sha256": "9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b",
  "checks_overlay": {"path": "...json", "sha256": "..."},
  "baseline": {"declared": "7ceff59", "resolved": "7ceff59a0216a8ea21ee43262d9fc72abf770cee",
               "kind": "short-sha", "head": "6e9a30d...", "relation": "ancestor"},
  "deviation": null,
  "observed_at": "2026-10-19T17:50:05Z",
  "claims": [
    {"id": "O", "axis": "operability", "verdict": "stale",
     "checks": [
       {"clause": "...", "probe_kind": "capability_present", "target": {...}, "expect": false,
        "measured": true, "status": "mismatch", "evidence": ["..."],
        "evidence_command": "...", "error": null}
     ],
     "mismatch_count": 2, "unevaluable_count": 0}
  ],
  "summary": {"fresh": 1, "stale": 2, "could_not_evaluate": 0,
              "stale_ids": ["O", "C"], "could_not_evaluate_ids": []},
  "verdict_digest": "sha256:...",
  "exit": 1
}
```

Human render MUST end with `exit N` and, when stale, a line naming the stale ids and the resolved baseline; when unevaluable, a line naming the ids and the reason.

### 3.11 Determinism

`verdict_digest = sha256("\n".join(f"{id}\t{verdict}\t{','.join(sorted(failing_check_indexes))}"))` over claims in file order. It excludes `observed_at`, evidence strings, and the tool digest. Two runs over the same claims bytes, overlay bytes, baseline tree, and tool bytes MUST produce identical `verdict_digest` and identical `exit`. `--json` output may differ only in `observed_at`. O14 should compare the digest, not the whole stdout.

---

## 4. Probe vocabulary

Closed set of seven, matching the r47 O claim (`reports/round-47/claims.json:37-48`). The six-part contract's `grep_present` is expressible as `grep_absent` with `expect:false`; `glob_absent`/`glob_present` as `count_eq` with `op: "eq"` value 0 / `op: "ge"` value 1; the prototype's `tool_family_absent` and `topic_unowned` as `capability_present expect:false` and `topic_owner_absent` (with `expect` chosen). No other kind is accepted.

Every probe defines a **measured boolean predicate**; `expect` is the value the claim asserts. `measured == expect` → match.

### 4.1 `path_absent`

| | |
|---|---|
| target | `{"path": "<repo-relative>"}` |
| measured | the path is **not** in the baseline `ls-tree` |
| evidence | `"<path>: absent|present"` |
| unevaluable | never (absence is decisive) |
| malformed | absolute path, `..`, missing `path` |

### 4.2 `path_present`

Same as 4.1 with the predicate inverted: measured = the path **is** in the baseline tree. Use it with `expect:false` only to assert absence explicitly (redundant but legal).

### 4.3 `grep_absent`

| | |
|---|---|
| target | `{"glob": "...", "regex": "...", "max_lines": N?, "min_files": N?}` |
| measured | **no line** in any baseline file matched by `glob` matches `regex` (Python `re`) |
| universe guard | let `F` = number of baseline files matching `glob`. If `F < min_files` (default **1**), the probe is `unevaluable`. `min_files: 0` is a deliberate opt-in to vacuous truth and MUST be recorded in the report as `vacuous: true`. |
| evidence | up to 6 `path:line: <clipped line>` |
| malformed | bad regex, negative `max_lines`/`min_files`, missing fields |
| note | a zero-hit result is only meaningful when the universe is non-empty; the guard closes D1/D5. |

### 4.4 `count_eq`

| | |
|---|---|
| target | `{"glob": "...", "value": N, "op": "eq"|"ge"|"le"|"gt"|"lt"?}` |
| measured | `count(baseline files matching glob) OP value`, `op` default `eq` |
| evidence | `"<glob> -> N (want op V)"` + first 5 matching paths |
| unevaluable | never: 0 is a legitimate count |
| malformed | negative value, unknown `op`, missing fields |

This is the count leg, not an ownership or capability leg. r43 C's counts were **true** (26/223) while its ownership premise was false; a suite made only of `count_eq` reproduces the exact defect the gate exists to catch.

### 4.5 `sha256_eq`

| | |
|---|---|
| target | `{"path": "...", "value": "<64 hex>"}` |
| measured | the baseline blob's sha256 equals `value` |
| evidence | `"<path> sha256 <actual>"` |
| unevaluable | never; an absent path yields `measured=false` (the asserted digest cannot hold) |
| malformed | value not 64 hex |

### 4.6 `topic_owner_absent`

| | |
|---|---|
| target | `{"topics": ["..."], "partition": "..."?, "fields": ["H1","topic","gap filled"]?}` |
| measured | **no** owner hit: no scanned header field in any baseline entry in the selected partition(s) matches any topic as a whole word/phrase, case-insensitive |
| scan | first 200 lines of each `corpus/knowledge/<partition>/*.md`; `H1` = the first line matching `^# `; `topic` = `^- topic:`; `gap filled` = `^- gap filled:`; default fields = all three |
| universe guard | if the selected partition(s) contain 0 entries → `unevaluable` |
| evidence | up to 6 `path:line (field) <clipped line>` |
| malformed | empty `topics`, unknown field, unknown partition, absolute/`..` |
| generic-topic guard | normalize each topic (lowercase, collapse whitespace/hyphens to single spaces). If **every** token is in `GENERIC_TOPICS`, the check is malformed (exit 2). `GENERIC_TOPICS = {register, registers, slot, topic, tradition, complex, system, systems, practice, practices, culture, material, symbol, symbols, authority, instrument, tool, mechanism, policy, artifact, record, disposition, census, family, form, class, type, kind, mode, domain, field, area, sphere}`. A phrase with at least one non-generic token (`llama-herding register`, `lithic`) is legal. Matching: split the declared topic on whitespace/hyphens into tokens and build `\btok1[\s-]+tok2...\b`, case-insensitive, so `llama-herding register` matches both hyphenated and spaced forms in a header. Do not match the tokens independently — `llama` alone must not create an owner hit. |
| note | this closes D3 at the contract level: the gate refuses to guess what a generic noun owns. It does not try to infer an owner from a vague phrase. |

### 4.7 `capability_present`

| | |
|---|---|
| target | `{"capability": "<name>", "scope": "tools/**.py"?, "path": "<exact>"?, "include_frozen": false?}` |
| measured | at least one baseline Python file in scope satisfies **all** required AST facts of the named capability (§5) |
| scope | `scope` and `path` are mutually exclusive; default scope `tools/**.py`; `tools/gates/frozen/**` excluded unless `include_frozen:true` |
| evidence | up to 6 `path: <fact satisfied>` or `path (parse error)`; the report names every scanned file count |
| unevaluable | the scope contains 0 `.py` files, or every in-scope file fails to parse and none satisfies the capability |
| malformed | unknown capability (D4), unknown target key, both `scope` and `path`, bad glob |
| note | this is the anti-theater leg: it measures structural capability, never a claim-named literal. A renamed tool is still found; a docstring mention is not. |

Optional `path` narrows to one file and makes absence a decisive `measured=false` (not unevaluable): a capability at that exact path does not exist.

---

## 5. Capability registry

The registry is **closed and lives in the tool** (`CAPABILITIES` dict). A capability name unknown to the tool is malformed, never silently false.

Required AST facts are computed from the baseline blob with `ast.parse`; comments/docstrings are not scanned.

| Capability | Required facts (all) | Purpose |
|---|---|---|
| `selftest_cli` | parses; defines top-level `main`; has an `argparse` `add_argument` constant `--selftest` | any instrument with a self-check |
| `claims_cli` | parses; defines `main`; has `add_argument` constants `--claims` and `--selftest` | this gate itself |
| `couples_census` | parses; defines `main`, `classify`, `resolve_entry`; has `--census` and `--selftest` | the r39 basename-couples policy instrument |
| `couples_four_class` | parses; has `--census`; and either a constant string `four_class_totals` or a module-level `CLASSES` tuple/list whose constant elements include `direct`, `fallback`, `ambiguous`, `unresolved` | the r44 successor's four-class report, without keying on a variable name |
| `read_only` | parses; no `open(...)` with a write mode (`w/a/x/+`), no `.write_text`/`.write_bytes` call | the read-only property for instruments |

Measured at four baselines (AST scan over every `tools/**.py` excluding `tools/gates/frozen/`):

| Baseline | `couples_census` | `couples_four_class` | `claims_cli` | `selftest_cli` |
|---|---|---|---|---|
| `ac47c78` (7ceff59^) | **false** — no `tools/harness/couples-reference-extractor.py` | false | false | true — 24 in-scope files |
| `7ceff59` (r43 baseline) | **true** — `tools/harness/couples-reference-extractor.py` (`main`, `classify`, `resolve_entry`, `--census`, `--selftest`) | **false** — no `four_class_totals` constant, no `CLASSES` tuple | false | true — 25 in-scope files |
| `c9f4eaa` (r44 baseline) | **true** — same witness | **false** — successor not yet landed | false | true — 25 in-scope files |
| `6e9a30d` (HEAD) | **true** — witness and landed successor `tools/harness/basename-couples-resolver.py` | **true** — successor has `CLASSES = ("direct","fallback","ambiguous","unresolved")` at `:140` and the `four_class_totals` key at `:260`; witness false | false (not yet landed) | true — 26 in-scope files |

Important calibration note: `couples_four_class` MUST NOT be keyed on a bare identifier `four_class`. The landed successor uses a variable named `four` and the **string key** `"four_class_totals"` (`tools/harness/basename-couples-resolver.py:254,260`); an identifier scan returns false and would make the r44 negative control pass for the wrong reason. The registry uses the constant string / `CLASSES` tuple facts above, both measured.

---

## 6. Selftest control set

`--selftest` builds a `MemoryTree` (or a temp dir under `TMPDIR`) with synthetic files; it does not resolve git. Controls are named; the final check asserts set equality (§6.4).

### 6.1 Probe controls

| ID | Fixture / check | Expected |
|---|---|---|
| `P01` | `path_absent` on an absent path, expect true | match |
| `P02` | `path_absent` on a present path, expect true | mismatch |
| `P03` | `path_present` on a present path, expect true | match |
| `P04` | `path_present` on an absent path, expect true | mismatch |
| `P05` | polarity flip: same target, `expect` flipped | verdict flips |
| `G01` | `grep_absent` where a **real fixture file** contains the hit | mismatch (D1) |
| `G02` | `grep_absent` where the universe is non-empty and no line matches | match |
| `G03` | `grep_absent` with a zero-file glob, default `min_files` | unevaluable (D5) |
| `G04` | same with `min_files: 0` | match, report `vacuous: true` |
| `C01` | `count_eq` true | match |
| `C02` | `count_eq` false | mismatch |
| `C03` | `count_eq op:ge` true / false | match / mismatch |
| `C04` | unknown `op` | malformed |
| `S01` | `sha256_eq` matching | match |
| `S02` | `sha256_eq` mismatch | mismatch |
| `S03` | `sha256_eq` absent path | mismatch |
| `S04` | non-hex digest | malformed |
| `T01` | `topic_owner_absent` on a partition with no hit | match |
| `T02` | `topic_owner_absent` on a hit (fixture H1 names the topic) | mismatch |
| `T03` | topic `register` (all tokens generic) | malformed (D3) |
| `T04` | topic `llama-herding register` (non-generic phrase) | evaluates; no hit → match |
| `T05` | partition with 0 entries | unevaluable |
| `T06` | unknown `fields` value | malformed |
| `K01` | `capability_present` on a fixture tool with `main` + `--selftest` | match |
| `K02` | same with `expect:false` | mismatch |
| `K03` | capability absent from a non-empty scope | measured false |
| `K04` | unknown capability name | malformed (D4) |
| `K05` | scope contains only an unparsable `.py` | unevaluable |
| `K06` | capable file only under `tools/gates/frozen/` | measured false by default; true with `include_frozen:true` |

### 6.2 Claim/exit controls

| ID | Fixture | Expected |
|---|---|---|
| `V01` | claim with no checks and no overlay | could-not-evaluate; exit 3 (never green) |
| `V02` | claim with one mismatch + one match | stale |
| `V03` | claim with one unevaluable + one match | could-not-evaluate |
| `V04` | file with one stale claim and one unevaluable claim | exit 1 (stale precedence) |
| `V05` | malformed JSON | exit 2 |
| `V06` | no `baseline_commit` | exit 2 |
| `V07` | claim missing `before` | exit 2 |
| `V08` | unknown probe kind | exit 2 (prototype returned stale — D4) |
| `V09` | missing `expect` | exit 2 |
| `V10` | `clause` not a substring of `before` | exit 2 (D9) |
| `V11` | duplicate claim ids | exit 2 |
| `V12` | overlay `claims_sha256` mismatch | exit 2 |
| `V13` | overlay baseline ≠ claims baseline | exit 2 |
| `V14` | `--at worktree` without `--allow-worktree` | exit 2 |
| `V15` | `--require-head` with baseline ≠ HEAD | exit 3 |

### 6.3 Determinism and baseline controls

| ID | Fixture | Expected |
|---|---|---|
| `D01` | run the whole selftest twice, compare verdict digests | identical |
| `D02` | `verdict_digest` excludes `observed_at` | identical across two runs |

### 6.4 Count assertion

Define `EXPECTED_NAMES` as a tuple literal of every control id in §6.1–§6.3. The selftest records `(name, passed)` and ends with:

```
assert set(names) == set(EXPECTED_NAMES)
assert len(names) == len(set(names))
```

No numeric literal. This closes D2 permanently.

---

## 7. Required demonstrations (not part of `--selftest`)

These are the filed evidence the r47 O claim requires. Names proposed for the integrator: `reports/round-47/calib/r43-checks.json`, `r44-checks.json`, `r43-premise-checks.json`, `freshness-gate-demo.json` (the gate's `--json` output), `freshness-gate-demo.txt` (human output).

### 7.1 r43 positive regression

Input: `reports/round-43/claims.json` (sha `9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b`), overlay:

```json
{
  "schema": "kotodama-claims-freshness-checks-v1",
  "round": 43,
  "baseline_commit": "7ceff59",
  "claims_sha256": "9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b",
  "checks": {
    "O": [
      {"clause": "no durable instrument implements the r39 basename-couples policy",
       "probe_kind": "capability_present",
       "target": {"capability": "couples_census", "scope": "tools/**.py"},
       "expect": false,
       "evidence_command": "git ls-tree -r -z --name-only 7ceff59 -- tools/"},
      {"clause": "the only resolver that ever ran (r39 I-C05) lives in ephemeral .scratch",
       "probe_kind": "capability_present",
       "target": {"capability": "couples_census", "scope": "tools/**.py"},
       "expect": false,
       "evidence_command": "git show 7ceff59:tools/harness/couples-reference-extractor.py | grep -n add_argument"}
    ],
    "C": [
      {"clause": "myth-symbol 26", "probe_kind": "count_eq",
       "target": {"glob": "corpus/knowledge/myth-symbol/*.md", "value": 26},
       "expect": true,
       "evidence_command": "git ls-tree -r --name-only 7ceff59 -- corpus/knowledge/myth-symbol | wc -l"},
      {"clause": "lithic slot named but unbuilt", "probe_kind": "topic_owner_absent",
       "target": {"topics": ["lithic"], "partition": "myth-symbol",
                  "fields": ["H1", "topic", "gap filled"]},
       "expect": true,
       "evidence_command": "git grep -n -i lithic 7ceff59 -- 'corpus/knowledge/myth-symbol/*.md'"},
      {"clause": "total 223", "probe_kind": "count_eq",
       "target": {"glob": "corpus/knowledge/*/*.md", "value": 223},
       "expect": true,
       "evidence_command": "git ls-tree -r --name-only 7ceff59 -- corpus/knowledge | wc -l"}
    ],
    "Ca": [
      {"clause": "have no per-finding disposition on record", "probe_kind": "path_absent",
       "target": {"path": "reports/round-43/calib/dispositions-r38-r39.json"},
       "expect": true,
       "evidence_command": "git ls-tree -r --name-only 7ceff59 -- reports/round-43/calib/"}
    ]
  }
}
```

Measured facts behind it (all verified at `7ceff59`):

- `tools/harness/couples-reference-extractor.py` parses with top-level `main`, `classify`, `resolve_entry`, and argparse flags `--selftest`, `--census` → `couples_census` true. O's two capability checks therefore mismatch `expect:false` → **O STALE**.
- `corpus/knowledge/myth-symbol/*.md` → 26; `corpus/knowledge/*/*.md` → 223; both count checks match. `topic_owner_absent` for `lithic` finds 3 hits in `mineral-stone-symbolism.md` (`:1` H1, `:3` gap filled, `:5` topic) → measured false vs `expect:true` → **C STALE** (counts fresh).
- `reports/round-43/calib/dispositions-r38-r39.json` is absent at `7ceff59` (no `calib/` paths in the tree) → **Ca FRESH**.

Expected: `summary {fresh:1, stale:2, could_not_evaluate:0}`, `stale_ids ["O","C"]`, **exit 1**, `REFUSE` line naming both.

### 7.2 r44 negative control

Input: `reports/round-44/claims.json` (sha `5bd54b714bd5238c2f8494e1c17b3126de000bdc1d3bbbdd9333f8e8bb5c06e8`), baseline `c9f4eaa`, overlay:

```json
{
  "schema": "kotodama-claims-freshness-checks-v1",
  "round": 44,
  "baseline_commit": "c9f4eaa",
  "claims_sha256": "5bd54b714bd5238c2f8494e1c17b3126de000bdc1d3bbbdd9333f8e8bb5c06e8",
  "checks": {
    "O": [
      {"clause": "no four-class census authority exists",
       "probe_kind": "capability_present",
       "target": {"capability": "couples_four_class", "scope": "tools/**.py"},
       "expect": false},
      {"clause": "223/2730", "probe_kind": "count_eq",
       "target": {"glob": "corpus/knowledge/*/*.md", "value": 223}, "expect": true}
    ],
    "C": [
      {"clause": "total 223", "probe_kind": "count_eq",
       "target": {"glob": "corpus/knowledge/*/*.md", "value": 223}, "expect": true}
    ],
    "Ca": [
      {"clause": "no mechanical pre-dispatch freshness check exists",
       "probe_kind": "capability_present",
       "target": {"capability": "claims_cli", "scope": "tools/**.py"},
       "expect": false}
    ]
  }
}
```

Measured at `c9f4eaa`: witness present but `couples_four_class` false (no `four_class_totals`, no `CLASSES`); total 223; no `claims_cli` tool. All checks match → **all FRESH, exit 0**. Note the r44 O `before` also asserts `223/2730 -> 2556/166/2/5/1`; the overlay uses only the count clause that is stable and checkable at baseline. The remaining prose is informational: only declared clauses are verdict-bearing, and the length of the report's `checks` array shows how much of the `before` was actually re-derived. An undeclared clause is neither fresh nor stale; it is simply not part of the contract.

### 7.3 Anti-theater mutants

| Mutant | Change | Expected |
|---|---|---|
| `M1-witness-rename` | rewrite the r43 O claim's `before` so the tool it names is `couples-reference-extractor.py` (the pre-existing witness); update the overlay's `clause` quotes and `claims_sha256` to the mutant fixture | still **STALE** — the capability scan over `tools/**.py` finds the witness regardless of what the claim names |
| `M2-live-literals` | rewrite r43 C's numbers to the live values (26/223) — they already are — and, in a second variant, remove the two count checks, leaving only the ownership check | still **STALE** — ownership fails; a count-only gate would call it fresh |
| `M3-novel-prose` | replace the r43 O/C `before` prose with a paraphrased assertion of the same premise; update the `clause` quotes | verdict unchanged — the gate never parses prose for a verdict |

Each mutant is a **new file** under `reports/round-47/calib/fixtures/` (or an in-memory fixture in the demo script); `reports/round-43/claims.json` is never touched. The mutant's overlay pins the mutant file's own sha.

### 7.4 State-flip control (the decisive non-theater proof)

Input: `reports/round-43/claims.json` plus a reduced overlay with only the two premise checks:

```json
{
  "schema": "kotodama-claims-freshness-checks-v1",
  "round": 43,
  "baseline_commit": "7ceff59",
  "claims_sha256": "9662e2bdaa73d3dd075e68148ae55c8c35d6fbdab527fc2602083745dcbc174b",
  "checks": {
    "O": [{"clause": "no durable instrument implements the r39 basename-couples policy",
           "probe_kind": "capability_present",
           "target": {"capability": "couples_census", "scope": "tools/**.py"},
           "expect": false}],
    "C": [{"clause": "lithic slot named but unbuilt",
           "probe_kind": "topic_owner_absent",
           "target": {"topics": ["lithic"], "partition": "myth-symbol",
                      "fields": ["H1", "topic", "gap filled"]},
           "expect": true}],
    "Ca": [{"clause": "have no per-finding disposition on record",
            "probe_kind": "path_absent",
            "target": {"path": "reports/round-43/calib/dispositions-r38-r39.json"},
            "expect": true}]
  }
}
```

Run it twice:

1. `--at 7ceff59` → **O STALE, C STALE, Ca FRESH, exit 1**.
2. `--at ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4` (the parent of `7ceff59`) → measured: witness absent, 0 `lithic` header owners, disposition artifact absent → **O FRESH, C FRESH, Ca FRESH, exit 0**.

Same tool, same overlay, earlier baseline, flipped verdict. A hardcoded-by-round or id-keyed gate cannot pass this control. This is the strongest evidence that the gate re-derives state.

### 7.5 Baseline-vs-worktree control

Synthetic claim: `before` "the r43 claims file exists", one check `path_present` on `reports/round-43/claims.json`, `expect:true`, baseline `7ceff59`.

- Measured at `7ceff59`: absent (verified `git cat-file -e 7ceff59:reports/round-43/claims.json` → absent) → **mismatch**.
- Worktree: present. The gate must still report `absent`.

A gate that reads the worktree would report the opposite. O11 runs this and records both readings.

### 7.6 Determinism

Run §7.1 twice; compare `verdict_digest` and `exit`. They MUST be equal; `observed_at` may differ. O14 records both digests.

---

## 8. Anti-theater argument

A "two-string lookup table" fails at least one of these measured controls:

| Theater implementation | Caught by |
|---|---|
| `if round == 43: stale` | §7.4 state flip (same round, different baseline → fresh) |
| literal `path_absent` on the claim-named `basename-couples-resolver.py` | §7.3 M1 (tool renamed to the witness; the literal path stays absent, but a state gate flags on the capability) |
| count-only checks | §7.1 C (26/223 are true; ownership is false) and §7.3 M2 |
| regex over claim prose | §7.3 M3 (novel phrasing) and the llama/register control `T03`/`T04` |
| docstring/name token scan for a "couples family" | `D8` fixture: `tools/gates/provenance-audit.py:12` must not count; `couples_census` requires AST facts |
| accept unknown probe kinds as "stale" | `V08` (must be malformed, not a verdict) |
| green when it cannot measure | `V01`/`G03`/`T05` (could-not-evaluate, exit 3) |

The gate earns the name only if the verdict changes when the **tree** changes while the **prose** is held fixed, and stays fixed when the **prose** changes while the **tree** is held fixed. §7.4 tests the first; §7.3 M3 tests the second.

---

## 9. Handoff and open items

- **O01 (core):** implement §3.1–§3.7, §3.11. `Tree` abstraction with a git backend and a `MemoryTree` backend; NUL-split `ls-tree`; `cat-file blob`; no worktree fallback.
- **O02 (probes):** implement §4 and §5 verbatim, including `expect`, `min_files`, the generic-topic guard, and the closed capability registry. Do not port `tool_family_absent` or the E1–E6 miner.
- **O03 (verdict/exit):** implement §3.8–§3.10; the exit table is 0/1/2/3, not the prototype's 0/1/2/3 meanings.
- **O04 (selftest):** implement §6 with named controls and set equality; the four required cases are `P02`/`P01`/`G03`/`V05`.
- **O05 (r43 demo):** use §7.1 verbatim; the expected run is exit 1, not the prototype's exit 2.
- **O06 (negative control):** use §7.2; expected exit 0.
- **O07 (anti-theater):** use §7.3 and §7.4; the state flip is the strongest evidence and should be in the filed demo, not only in the selftest.
- **O08/O09/O10/O11/O14/O15:** the control ids in §6 and §7 are the test vectors. O09's traps map to `T03/T04` (novel phrasing), `V08` (no polarity/unknown kind), and §5/§3.6 (tag baseline accepted via `^{commit}` resolution, recorded as `kind: tag`).
- **W01:** the integrator's apply target is `tools/harness/claims-freshness.py`, byte source the assembled fenced tool; the filed demo artifacts are the `calib/` names in §7. Pin the applied tool's sha256 in the demo report (`tool.sha256`).

`to-verify` (owner O01/O08, not asserted here):

1. The exact AST fact set for `couples_four_class` on the landed successor is measured at HEAD (`CLASSES` tuple `:140`, `four_class_totals` `:260`), but the successor's own bytes are pinned by the r44 landing; if the integrator changes them, re-measure.
2. `GENERIC_TOPICS` is a judgment list; O09 should try at least three novel phrasings not in §4.6 and record whether any falsely matches. The contract's guard is "all tokens generic → malformed"; a non-generic but wrong topic can still produce a false owner hit if the corpus uses the word in a header. That is a declared-topic risk, not a prose-mining risk.
3. The overlay schema pins `claims_sha256`; the r43 demo must recompute it from the filed bytes at apply time, not copy the value above blindly. The value above was measured now (`sha256sum reports/round-43/claims.json`).
4. `--at worktree` remains available only for diagnosing a mismatch; it must never be used for the filed demonstration. O08 should run `git status --porcelain` after the demo to prove no write.

---

## 10. Evidence ledger

Commands run by this seat (all read-only; scratch writes only under `.scratch/k03/` and `TMPDIR`):

```
python3 -B .scratch/ca01/claims-freshness.py --selftest          # 17/19 FAIL, exit 1
python3 -B .scratch/ca01/claims-freshness.py --claims reports/round-43/claims.json
                                                                  # O 0/2 STALE, C 2/3 STALE, Ca 1/1 FRESH, exit 2
python3 -B - <<'PY' ... analyze_claim(llama-herding register) ... # STALE, 51 owners (D3)
python3 -B - <<'PY' ... evaluate_probe(grep_absent, beta/*.md) ... # True, 0 hits (D5)
git rev-parse HEAD                                                 # 6e9a30d...
git rev-parse --verify '7ceff59^{commit}'                          # 7ceff59a0216...
git rev-parse '7ceff59^'                                           # ac47c786...
git ls-tree -r --name-only 7ceff59 -- tools/harness/               # couples-reference-extractor.py present
git cat-file -e 7ceff59:reports/round-43/calib/dispositions-r38-r39.json  # absent
git cat-file -e 7ceff59:reports/round-43/claims.json               # absent (input, not a target)
git grep -n -i lithic 7ceff59 -- 'corpus/knowledge/*/*.md'         # 3 header hits in mineral-stone-symbolism.md
AST scan, all tools/**.py at ac47c78/7ceff59/c9f4eaa/6e9a30d       # capability table §5
sha256sum reports/round-43/claims.json reports/round-44/claims.json # pins above
```

Counts verified: `7ceff59` total 223, myth-symbol 26; `ac47c78` total 220, myth-symbol 23; `c9f4eaa` total 223, myth-symbol 26; `6e9a30d` total 223, myth-symbol 26 (the r47 C landing is not applied yet).

Limits: I did not build or land the tool (that is O01–O03); no durable `tools/harness/claims-freshness.py` exists at HEAD (`git cat-file -e 6e9a30d:tools/harness/claims-freshness.py` → absent). I did not run any `run-validation.py`. The r43/r44 overlays above are drafted, not filed; their `claims_sha256` pins must be re-read at apply time. The selftest control list is normative but not yet executed against an implementation; O04 owns that execution and must file its own `N/N` output.

**Bottom line:** the durable gate must be a state re-deriver with declared polarity, not a prose parser and not a count checker. The seven-probe vocabulary plus the closed AST capability registry covers every r43/r44 premise measured in this round; the exit contract is 0 fresh / 1 stale / 2 malformed / 3 could-not-evaluate; and the decisive proof that it is not theater is the `ac47c78` state flip, where the same checks that flag `7ceff59` return fresh one commit earlier.
