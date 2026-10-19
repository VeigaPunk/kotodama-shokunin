# O02 — freshness-gate probe registry: seven typed probes, declared polarity, measured at `7ceff59`

- Seat: `O02` | role `executor` | claim `O` | round 47, loop 2
- Out path: `reports/round-47/op/O02-probe-registry.md` (the only file this seat writes in the repo)
- Mission: `reports/round-47/targets.json:34` — "the probe registry — typed probes (`path_absent/path_present/grep_absent/count_eq/sha256_eq/topic_owner_absent/capability_present`) each with declared polarity; a claim's `before_checks` list schema. Fenced tool draft part 2."
- Baseline for every measurement: `7ceff59` (the r43 claim baseline, `reports/round-43/claims.json:7`). This seat's round baseline is `6e9a30d` (`reports/round-47/claims.json:7`); no repo file was changed.
- Environment: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root.
- Boundary: I wrote only this out path. All experiments ran from `.scratch/o02/`; no `corpus/` staging, no filed-byte edit, no `run-validation.py`, no git mutation, install, or network. The r43 file is read, never annotated in place.

## 1. Verdict

Part 2 is delivered as a fenced, runnable module: the seven-kind probe registry, the `before_checks` schema, a strict validator, a baseline evaluator, and a registry selftest. The registry selftest is **43/43, exit 0**. Measured against the real r43 baseline `7ceff59` through `git ls-tree`/`git show`, it reproduces the required positive regression:

| claim | declaration | measured | verdict |
|---|---|---|---|
| r43 **O** | `capability_present`, `expect=false` ("no durable instrument implements the r39 basename-couples policy") | a candidate passes the declared behavior — `tools/harness/couples-reference-extractor.py`, exit 0, `entries=1 refs=4` | **STALE** |
| r43 **C** | `topic_owner_absent`, `expect=true` ("lithic slot … unbuilt") | one owner — `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:1,3` | **STALE** |
| r43 **Ca** | `path_absent`, `expect=true` ("no per-finding disposition on record") | `reports/round-43/calib/dispositions-r38-r39.json` absent at `7ceff59` | **FRESH** |

C's two count clauses also measured true at the same baseline — `myth-symbol` 26 and total 223 — so C is stale **only** on ownership, exactly as `reports/round-44/review/R01-review.md:236-237` reported. The anti-theater control renames the witness blob to `zzz-renamed.py` and the probe still measures the capability; flipping `expect` flips the verdict; `--no-exec` yields `could-not-evaluate`, never green.

This is part 2 of 3, not the durable tool. `O01` owns claims parsing and the baseline tree; `O03` owns verdict aggregation and exit codes; the integrator applies the assembled tool. The module here is the probe layer those parts call.

## 2. The polarity rule (the r44 defect this part exists to stop)

`reports/round-44/review/R01-review.md:239` states the failure precisely:

> My first probe run marked O's first premise "fresh" because I encoded `asserted=True` for "resolver exists" when the claim asserts absence. A gate cannot infer polarity from prose; each clause must declare the measured state that makes it true.

The registry encodes one rule, and only one:

> **`expect` is the measured value under which the quoted clause is TRUE.** It is not "what the claim asserts", and it is not inferred from the probe kind's name.

This is a deliberate reversal of the intuitive reading. For the r43 O clause "no durable instrument implements the r39 basename-couples policy", the measurement `capability_present` is **true** (the witness exists), so the clause is true only if that measurement is **false**. The check declares `"expect": false`. A naive schema that stored `asserted=true` for "no instrument" would have read this as fresh — the r44 defect verbatim.

The registry enforces the rule structurally:

- `expect` is required on every check; it is never defaulted.
- Its JSON type must exactly match the probe's measured type: `bool` for the five boolean probes, `int` for `count_eq`, a 64-hex string for `sha256_eq`.
- `type(expect) is bool` is checked, so JSON `true` is accepted and `1` / `"true"` are rejected. Python's `bool`-is-an-`int` trap cannot launder a polarity error.
- The report prints the declared polarity in words (`polarity_label`), so a reviewer sees "clause asserts the NEGATION of the capability_present predicate" rather than a bare `false`.
- A check whose `clause` is not a verbatim (whitespace-normalized, case-insensitive) substring of the claim's `before` is rejected as malformed. A check cannot drift away from the sentence it claims to ground.

Measured polarity controls (selftest S1/S1b, S6/S6b, S7/S7b, S3/S3c) flip only `expect` on the same measurement and require the verdict to flip. The registry never contains a `kind -> expected polarity` table.

## 3. The seven-kind registry

| kind | measures | measured type | `target` schema | `expect=true` means | why it is not literal theater |
|---|---|---|---|---|---|
| `path_absent` | is the path absent at baseline? | `bool` | `{"path": "..."}` | the path is absent | baseline `git ls-tree` membership, not a prose grep |
| `path_present` | is the path present at baseline? | `bool` | `{"path": "..."}` | the path is present | baseline membership |
| `grep_absent` | does the regex have zero hits in the glob? | `bool` | `{"glob": "...", "regex": "..."}` | zero hits | scans baseline blobs; `expect=false` is the explicit "at least one hit" polarity |
| `count_eq` | how many files match the glob? | `int` | `{"glob": "..."}` | exactly `expect` files | baseline file list + a `paths_sha256` over the sorted matches |
| `sha256_eq` | sha256 of the file bytes | `str` | `{"path": "..."}` | digest equals `expect` | raw blob bytes from `git show`, not the worktree and not the git blob id |
| `topic_owner_absent` | do zero entries own the topic in their header? | `bool` | `{"topic": [...], "partitions": [...], "fields": [...], "mode": "word\|phrase\|all_tokens"}` | zero owners | parses H1 / `- topic:` / `- gap filled:` at baseline and returns owner paths; no keyword grep over prose |
| `capability_present` | does a candidate pass the declared behavioral test? | `bool` | `{"globs": [...], "exclude_globs": [...], "argv": [...], "fixture": {...}, "success_regex": "...", "timeout_s": N, "max_candidates": N}` | at least one candidate passes | executes extracted baseline blobs against a fixture tree; the target has **no name/tool field** |

Notes that matter for review:

- **`path_absent` and `path_present` are duals.** Either can express the other with `expect=false`; the named dual is preferred because the report then reads naturally. Both are exercised by controls, so neither is a dead kind.
- **`grep_absent` is the only grep kind** in the closed r47 vocabulary. `expect=false` is the declared polarity for "at least one hit"; no `grep_present` alias is needed. A regex that matches the empty string (`.*`, `^`) is rejected: it can never be absent and is almost always a mistake.
- **`count_eq` is equality only.** The closed vocabulary has no `count_le`/`count_ge`; a range claim must be expressed as an exact count or split into two checks. `paths_sha256` is reported over the sorted match list so a future re-run can detect path drift even when the count is unchanged.
- **`sha256_eq` hashes raw bytes** via `git show <baseline>:<path>`; this is the convention the r43/r44 evidence objects use, not `git hash-object` (which prefixes a blob header). A missing blob is `could-not-evaluate`, never a mismatch or a pass.
- **`topic_owner_absent` is an ownership probe, not a vocabulary probe.** It scans only header fields (first 200 lines, stopping at the first `## `), matches whole aliases or phrases, and returns distinct owner paths plus the exact `path:line (field)`. A topic mentioned only in body prose or `- scope:` is not an owner by design. Generic category words (`register`, `system`, `culture`, `slot`, `family`, …) are rejected unless an alias carries at least one non-generic token — this is the R02 llama-herding false-positive guard (`reports/round-44/review/R02-review.md:207-227`).
- **`capability_present` is the anti-theater probe.** The target describes behavior: candidate globs, argv, a fixture tree, and a success regex. It deliberately has no `name`, `tool`, or `tool_name` key, and the schema rejects unknown keys. Renaming a tool, or rewriting the claim's prose to name a different tool, cannot change the measurement; only the behavior can. The r43 witness is found because it parses a wrapped `- couples:` fixture and prints `refs=4`, not because its filename appears anywhere in the check.
- **Capability execution boundary.** Each candidate blob is written under a fresh temp tree at `tools/harness/<basename>`, with the declared fixture materialized beside it; it runs as `python3 -I -B <blob> <argv...>` with `cwd=<temp>`, a per-candidate timeout, and no shell. A candidate counts only on exit 0 **and** a `success_regex` match. Candidates that all fail to execute produce `could-not-evaluate`, not "absent". The execution is not an OS sandbox: a tool that walks above the fixture root could read the worktree. This is a declared limitation (`§7`), mitigated by in-repo-only globs, `exclude_globs`, the candidate cap, and `--no-exec`.
- **Candidate cap.** If the glob yields more than `max_candidates`, the probe returns `could-not-evaluate` rather than scanning a truncated list and reporting a false absence.

## 4. `before_checks` schema

Each claim gains an optional `before_checks` array. It lives in a successor/overlay file for a filed claims file; **never annotate `reports/round-43/claims.json` in place** (see §6).

Required keys per check:

| key | type | rule |
|---|---|---|
| `clause` | string | verbatim substring of the claim's `before`, after whitespace normalization and case-folding |
| `probe_kind` | string | one of the seven; unknown kinds are malformed |
| `target` | object | closed schema per kind (table above); unknown keys rejected |
| `expect` | bool/int/string | exact JSON type for the kind; the measured value that makes the clause true |
| `evidence_command` | string | one line, ≤500 chars, read-only (destructive `rm`/`mv`/`git checkout|reset|commit|push|clean` rejected) |

Optional: `id` (unique within the claim; used in reports) and `note` (human context). `before_checks` absent or `[]` is legal input and means `could-not-evaluate`; it is never green.

Complete declarations used in the measured run (the exact objects are also in Appendix B):

```json
{
  "id": "O-1",
  "clause": "no durable instrument implements the r39 basename-couples policy",
  "probe_kind": "capability_present",
  "target": {
    "globs": ["tools/harness/*.py"],
    "exclude_globs": ["tools/gates/frozen/**"],
    "argv": ["--census"],
    "fixture": {
      "corpus/knowledge/fixture/entry.md": "# Fixture entry\n\n- topic: fixture\n- couples: language — `sound-symbolism.md`, `writing-systems.md`; prospective\n  sibling files: sound-change.md, tone-\n  prosody.md\n"
    },
    "success_regex": "refs=4\\b",
    "timeout_s": 20,
    "max_candidates": 24
  },
  "expect": false,
  "evidence_command": "git ls-tree -r --name-only 7ceff59 -- tools/harness"
}
```

```json
{
  "id": "C-1",
  "clause": "lithic slot named but unbuilt since r42's C01/C04 collision routed this draft to spare",
  "probe_kind": "topic_owner_absent",
  "target": {
    "topic": ["lithic", "lapidary"],
    "partitions": ["myth-symbol"],
    "fields": ["h1", "topic", "gap filled"],
    "mode": "word"
  },
  "expect": true,
  "evidence_command": "git grep -n -i -E '^# |^- (topic|gap filled):' 7ceff59 -- 'corpus/knowledge/myth-symbol/*.md'"
}
```

```json
{
  "id": "Ca-1",
  "clause": "have no per-finding disposition on record",
  "probe_kind": "path_absent",
  "target": {"path": "reports/round-43/calib/dispositions-r38-r39.json"},
  "expect": true,
  "evidence_command": "git ls-tree -r --name-only 7ceff59 -- reports/round-43/calib"
}
```

The C-2/C-3 count checks are `count_eq` on `corpus/knowledge/myth-symbol/*.md` (26) and `corpus/knowledge/*/*.md` (223), both `expect` integer. Their verbatim `clause` quotes are `myth-symbol 26` and `total 223` from `reports/round-43/claims.json:40`.

## 5. Measured evidence

### 5.1 Registry selftest: 43/43, exit 0

Command: `python3 -B .scratch/o02/probe_registry.py` (the module is fenced in Appendix A; `python3 -B <extracted>.py` reproduces it).

```
PROBE-REGISTRY SELFTEST: 43/43
exit=0
```

The 43 controls cover: all seven kinds positively and negatively; polarity flips (`S1/S1b`, `S3/S3c`, `S6/S6b`, `S7/S7b`); a missing blob is `could-not-evaluate`; the generic-topic rejection; the renamed-tool capability hit; the no-capability mismatch; `--no-exec`; strict typing (`"true"`, `1`, string count); unknown kind; non-verbatim clause; path escape; unknown target key; capability target naming a tool; empty-matching grep; claim-level precedence (malformed > stale > could-not-evaluate > fresh); glob semantics (`*` does not cross `/`, `**` does); `validate_claim_checks` absent/non-list/duplicate cases; destructive `evidence_command`.

### 5.2 r43 regression at `7ceff59` (the positive regression)

Command: `python3 -B .scratch/o02/run_baseline.py` (reads `reports/round-43/claims.json` and a `git ls-tree`/`git show` baseline view). Verbatim output:

```
O -> stale
  O-1  capability_present   measured=True    expect=False mismatch           1/7 candidate(s) pass the declared behavior: tools/harness/couples-reference-extractor.py
       tools/harness/couples-reference-extractor.py: exit=0 regex=hit entries=1 refs=4 -> prospective=4
C -> stale
  C-1  topic_owner_absent   measured=False   expect=True  mismatch           1 owner(s): corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
       corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:1 (h1; lithic) # Stone, gem and metal symbolism — the lithic register: the lapidary code, material prestige, and t
       corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:3 (gap filled; lithic) - gap filled: the lithic/mineral register is absent from the partition and this entry fills
  C-2  count_eq             measured=26      expect=26    holds              corpus/knowledge/myth-symbol/*.md -> 26 file(s); paths_sha256=364491775f6085ef
  C-3  count_eq             measured=223     expect=223   holds              corpus/knowledge/*/*.md -> 223 file(s); paths_sha256=2cb71c5e211c8421
Ca -> fresh
  Ca-1 path_absent          measured=True    expect=True  holds              reports/round-43/calib/dispositions-r38-r39.json is absent
```

The facts behind it, all measured at `7ceff59`:

- `git ls-tree -r --name-only 7ceff59 corpus/knowledge | grep -c '\.md$'` → `223`; `corpus/knowledge/myth-symbol/*.md` → `26`.
- The lithic owner is `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`; its H1 names "the lithic register" and its `- topic:` line (line 5) names "the lithic register of a fictional culture's symbolic grammar". The probe finds it on the H1 and on `- gap filled:` (line 3), both within the header scan.
- The witness blob at `7ceff59` is `tools/harness/couples-reference-extractor.py`, sha256 `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`; its selftest is 8/8 and its `--census` on the wrapped fixture prints `entries=1 refs=4 -> prospective=4`.
- `git ls-tree -r --name-only 7ceff59 -- reports/round-43/calib` → empty, so Ca's artifact is absent.

### 5.3 Anti-theater: capability and ownership, not literal text

Command: `python3 -B .scratch/o02/anti_theater.py`. Verbatim:

```
witness sha256 at 7ceff59: d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1
candidate tools/harness/couples-reference-extractor.py         measured=True status=mismatch
candidate tools/harness/zzz-renamed.py                         measured=True status=mismatch
capability-free candidate                                  measured=False status=holds
same witness, expect=true                                  measured=True status=holds
same witness, --no-exec                                    measured=None status=could-not-evaluate
ANTI-THEATER OK: renamed tool still measured; expectation flips the verdict; no-exec is not green
```

The check's `target` never names `couples-reference-extractor.py`; the same bytes under `zzz-renamed.py` still satisfy the behavior. The clause-level expectation, not the filename, produces the stale verdict.

### 5.4 Negative control and digest probe

```
negative control (tool absent at baseline):
  tools/harness/claims-freshness.py is absent -> measured=True expect=True status=holds

sha256 probe, deliberately wrong expect:
  measured=c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f status=mismatch
```

The real sha256 of `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` at `7ceff59` is `c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f`; the control passes a wrong digest and gets a mismatch, proving the comparison is not a tautology.

### 5.5 What this proves, and what it does not

Proved: the seven probes measure baseline state, the polarity declaration is load-bearing, capability is behavioral and name-independent, the r43 O/C/Ca regression reproduces, and the registry selftest is deterministic on identical inputs.

Not proved here: the durable tool's CLI, its claims-file parser, and its exit codes (O01/O03); the r44 negative control at `c9f4eaa` (O06); the full r43 O "0/4 tokens" clause (O05 — see §7); and the assembled tool's behavior from the durable path (O08/O12).

## 6. Integration contract

**Seam with O01 (core).** The registry calls only:

```
tree.files() -> list[str]        # git ls-tree -r --name-only <baseline_commit>
tree.exists(path) -> bool
tree.read(path) -> str           # git show <baseline_commit>:<path>
tree.sha256(path) -> str         # sha256 of the raw blob bytes
```

It does not call `tree.glob` or `tree.grep`; glob semantics are implemented in the registry (`_match_glob`: `*` within a segment, `**` across segments), so the probe layer cannot be silently changed by a different tree dialect.

**Seam with O03 (verdict/exit).** Import `validate_claim_checks`, `evaluate_check`, `claim_status`, `polarity_label`. `validate_claim_checks` returns `[]` for an absent/empty list (the caller must mark the claim `could-not-evaluate`, not fresh) and raises `CheckError` for malformed input (the caller maps that to exit 2). `claim_status` precedence is malformed > stale > could-not-evaluate > fresh. Recommended exit codes: `0` all fresh, `1` any stale, `2` malformed, `3` could-not-evaluate; the r47 contract's hard requirements are "exit 0 only for all-fresh" and "could-not-evaluate is non-zero" — code 3 satisfies both and avoids colliding with stale/malformed.

**Splice.** Append the Appendix A body to `tools/harness/claims-freshness.py` after the O01 tree/loader. The only global names likely to collide are `PARTITIONS`, `PROBES`, and `FixtureTree`; keep one `PARTITIONS`, keep `PROBES = dict(_PROBES)` as the exported table, and keep `FixtureTree` only if the assembled selftest uses it. The module is stdlib-only and `sys.dont_write_bytecode = True`.

**Filed bytes.** The r43 demonstration must be a **successor artifact** in `reports/round-47/calib/` (or an overlay keyed by claim id), never an edit to `reports/round-43/claims.json`. The `clause` verbatim rule means an overlay must carry the exact `before` text it quotes; if the prose is edited, the check must be re-declared, and the gate should surface that as malformed rather than silently accepting drift. A suggested overlay shape (O03/O05 may adopt it):

```json
{"source_claims": "reports/round-43/claims.json",
 "source_sha256": "<sha of the filed file>",
 "baseline_commit": "7ceff59",
 "claims": {"O": [ ...checks... ], "C": [ ... ], "Ca": [ ... ]}}
```

**Execution.** Capability probes execute in-repo baseline blobs; run the r43 demo with execution enabled. `--no-exec` is for hostile or offline environments and must produce `could-not-evaluate` (exit 3), not a green. The candidate cap is a safety valve: exceeding it is `could-not-evaluate`, never a truncated "absent".

**Selftest.** The registry selftest is `selftest_registry()` with 43 controls. O04 owns the tool-wide control set; this run is the registry subset and should remain callable from the assembled `--selftest` (or be merged, keeping the count honest). The assembler must not claim 43/43 for the whole tool unless the whole selftest passes.

## 7. Open items (`to-verify`)

1. **r43 O's second clause, "the single wrapped couples field reads 0/4 tokens"** (`reports/round-43/claims.json:27`), is not probed in this fragment. A behavioral probe can run the candidate against a baseline-corpus snapshot and assert the wrapped-field token count, but that needs O01's baseline tree plus a corpus materialization; `to-verify` for O05. The first clause alone already makes O stale.
2. **Capability execution is not OS-sandboxed.** `-I -B`, cwd, timeout, and the fixture root are the containment; a tool that walks above the fixture can read the worktree. In-repo-only globs and `exclude_globs` are the policy boundary. A future hardening (bubblewrap/firejail/unshare) is out of scope and must not be claimed.
3. **`topic_owner_absent` header scope.** First 200 lines, stops at the first `## `; only H1/`- topic:`/`- gap filled:` are ownership fields. A topic owned only in body prose or `- scope:` is intentionally not counted. If a future entry's ownership line moves below line 200, the probe under-counts owners; the `evidence_command` and owner list make that visible, but it is a declared limit.
4. **Exit code 3** is a recommendation to O03; if O03 chooses a different non-zero code for `could-not-evaluate`, the registry is unaffected.
5. **Durability** is not this seat's deliverable: the module is fenced here, not staged under `tools/`. The integrator's apply and O08/O12's independent run are the durability evidence.

## Appendix A — probe registry (fenced tool draft, part 2)

<!-- The bytes below are the verified module; `sha256sum` of the fenced body is
     reported after the fence. Extract with:
     awk '/^```python$/{f=1;next}/^```$/{f=0}f' reports/round-47/op/O02-probe-registry.md > /tmp/probe_registry.py
-->

```python
#!/usr/bin/env python3
"""Typed probe registry for the pre-dispatch claims-freshness gate (r47 claim O, part 2).

A claim's ``before`` is prose.  This module turns each declared clause into a
*check* whose measurement is mechanical and whose polarity is declared, never
inferred:

    {
      "id": "O-1",                       # optional, unique within the claim
      "clause": "no durable instrument implements the r39 basename-couples policy",
      "probe_kind": "capability_present",
      "target": {"globs": ["tools/**/*.py"], ...},
      "expect": false,                   # THE MEASURED VALUE THAT MAKES THE CLAUSE TRUE
      "evidence_command": "git ls-tree -r --name-only 7ceff59 -- tools/",
      "note": "optional human note"
    }

Polarity rule (the r44 defect this registry exists to stop)
----------------------------------------------------------
``expect`` is *the value the probe must measure for the quoted clause to be
true*.  It is not "what the claim asserts", and it is not inferred from the
probe kind's name.  The r44 prototype encoded "no resolver exists" as
``asserted=True`` against ``path_present``; that reads fresh when the resolver
is absent.  Here the same clause would be ``capability_present`` with
``expect=false`` (the capability must *not* be measurable), or
``path_absent`` with ``expect=true``.  The registry rejects a missing or
wrong-typed ``expect``; ``True`` vs ``1`` is rejected for boolean probes.

Closed probe vocabulary
-----------------------
``path_absent``          bool  is the path absent at baseline?
``path_present``         bool  is the path present at baseline?
``grep_absent``          bool  does the regex have zero hits in the glob?
``count_eq``             int   how many files match the glob? (equality)
``sha256_eq``            str   sha256 of the file bytes (equality)
``topic_owner_absent``   bool  do zero entries own the topic in their header?
``capability_present``   bool  does a candidate pass the declared behavioral test?

Every probe is measured through a baseline view (``tree``), never the
worktree.  The view contract is the seam with part 1:

    tree.files() -> list[str]            tracked paths at the baseline
    tree.exists(path) -> bool
    tree.read(path) -> str
    tree.sha256(path) -> str             sha256 of the blob bytes

Glob matching is implemented here (``*`` stays within a path segment, ``**``
crosses segments), so the registry does not depend on the view's glob dialect.
``tree.files()`` must come from ``git ls-tree -r --name-only <baseline>`` and
``tree.read()`` from ``git show <baseline>:<path>``; the worktree is never
consulted.

``capability_present`` additionally executes candidate blobs.  Candidates are
written to a private temp tree, run with ``python3 -I -B``, a timeout, and no
shell; a candidate counts only on exit 0 *and* a ``success_regex`` match.  The
target has no ``name``/``tool`` field: capability is found by behavior, so
renaming a tool cannot launder a stale premise.

Read-only with respect to the repository.  Stdlib only.
"""
from __future__ import annotations

import fnmatch
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

sys.dont_write_bytecode = True

PARTITIONS = (
    "myth-symbol",
    "linguistics",
    "culture-material",
    "civilizations",
    "verification",
    "synthesis",
)
HEADER_FIELDS = {
    "h1": re.compile(r"^#\s+(.*)$"),
    "topic": re.compile(r"^- topic:\s*(.*)$"),
    "gap filled": re.compile(r"^- gap filled:\s*(.*)$"),
}
GENERIC_TOPIC_TOKENS = {
    "register", "system", "culture", "practice", "slot", "family", "complex",
    "code", "material", "method", "knowledge", "reference", "entry", "topic",
    "domain", "tradition", "pattern", "form", "class", "type", "set",
}
HEX64 = re.compile(r"^[0-9a-f]{64}$")
SAFE_REL = re.compile(r"^(?!/)(?!.*(?:^|/)\.\.(?:/|$))[A-Za-z0-9_./*?\[\]-]+$")


class CheckError(ValueError):
    """A malformed check.  Never downgraded to a green verdict."""


def _norm_ws(text):
    return " ".join(str(text).split())


def _tokens(text):
    return [tok for tok in re.split(r"[^a-z0-9]+", str(text).lower()) if tok]


def _match_glob(pattern, path):
    """Repo-relative glob: `*` stays within a segment, `**` crosses segments."""
    def walk(pat_parts, path_parts):
        if not pat_parts:
            return not path_parts
        head = pat_parts[0]
        if head == "**":
            return walk(pat_parts[1:], path_parts) or (
                bool(path_parts) and walk(pat_parts, path_parts[1:])
            )
        if not path_parts:
            return False
        if not fnmatch.fnmatchcase(path_parts[0], head):
            return False
        return walk(pat_parts[1:], path_parts[1:])

    return walk(pattern.split("/"), path.split("/"))


def _glob(tree, pattern):
    return [path for path in tree.files() if _match_glob(pattern, path)]


def _grep(tree, regex, pattern, case_sensitive=False, max_lines=0):
    match = re.compile(regex, 0 if case_sensitive else re.I)
    hits = []
    for path in _glob(tree, pattern):
        for number, line in enumerate(tree.read(path).splitlines(), 1):
            if max_lines and number > max_lines:
                break
            if match.search(line):
                hits.append((path, number, line))
    return hits


def _require_rel_path(path, field="path"):
    if not isinstance(path, str) or not path or "\\" in path:
        raise CheckError("%s must be a non-empty repo-relative path" % field)
    if not SAFE_REL.match(path):
        raise CheckError("%s escapes the repo or is not a plain path: %r" % (field, path))


def _require_keys(obj, allowed, where):
    if not isinstance(obj, dict):
        raise CheckError("%s must be an object" % where)
    unknown = sorted(set(obj) - set(allowed))
    missing = sorted(set(allowed) - set(obj))
    if unknown:
        raise CheckError("%s has unknown key(s): %s" % (where, ", ".join(unknown)))
    if missing:
        raise CheckError("%s is missing key(s): %s" % (where, ", ".join(missing)))


def _as_aliases(topic):
    if isinstance(topic, str):
        topic = [topic]
    if not isinstance(topic, list) or not topic:
        raise CheckError("topic must be a non-empty string or list of strings")
    aliases = []
    for item in topic:
        if not isinstance(item, str) or not item.strip():
            raise CheckError("every topic alias must be a non-empty string")
        aliases.append(_norm_ws(item).lower())
    return aliases


def _alias_match(field_text, alias, mode):
    text = _norm_ws(field_text).lower()
    if mode == "phrase":
        pattern = r"(?<![a-z0-9])" + r"[^a-z0-9]+".join(
            re.escape(tok) for tok in _tokens(alias)
        ) + r"(?![a-z0-9])"
        return re.search(pattern, text) is not None
    if mode == "all_tokens":
        present = set(_tokens(text))
        return all(tok in present for tok in _tokens(alias))
    # word (default): whole-word or whole-phrase hit for a single token
    return re.search(
        r"(?<![a-z0-9])%s(?![a-z0-9])" % re.escape(alias), text
    ) is not None


def _normalize_target(kind, target):
    if kind in ("path_absent", "path_present"):
        _require_keys(target, ("path",), "%s target" % kind)
        _require_rel_path(target["path"])
        return {"path": target["path"]}
    if kind == "grep_absent":
        _require_keys(target, ("glob", "regex"), "%s target" % kind)
        _require_rel_path(target["glob"], "glob")
        try:
            regex = re.compile(target["regex"])
        except re.error as exc:
            raise CheckError("grep_absent regex does not compile: %s" % exc)
        if regex.search(""):
            raise CheckError("grep_absent regex matches the empty string; it can never be absent")
        return {"glob": target["glob"], "regex": target["regex"]}
    if kind == "count_eq":
        _require_keys(target, ("glob",), "%s target" % kind)
        _require_rel_path(target["glob"], "glob")
        return {"glob": target["glob"]}
    if kind == "sha256_eq":
        _require_keys(target, ("path",), "%s target" % kind)
        _require_rel_path(target["path"])
        return {"path": target["path"]}
    if kind == "topic_owner_absent":
        _require_keys(
            target, ("topic", "partitions", "fields", "mode"), "%s target" % kind
        )
        aliases = _as_aliases(target["topic"])
        non_generic = [
            tok
            for alias in aliases
            for tok in _tokens(alias)
            if tok not in GENERIC_TOPIC_TOKENS
        ]
        if not non_generic:
            raise CheckError(
                "topic_owner_absent refuses a generic topic (%s); name the register, not a category word"
                % ", ".join(aliases)
            )
        partitions = target["partitions"]
        if not isinstance(partitions, list) or not partitions:
            raise CheckError("partitions must be a non-empty list")
        bad = sorted(set(partitions) - set(PARTITIONS))
        if bad:
            raise CheckError("unknown partition(s): %s" % ", ".join(bad))
        fields = target["fields"]
        if not isinstance(fields, list) or not fields:
            raise CheckError("fields must be a non-empty list")
        bad = sorted(set(fields) - set(HEADER_FIELDS))
        if bad:
            raise CheckError("unknown header field(s): %s" % ", ".join(bad))
        mode = target["mode"]
        if mode not in ("word", "phrase", "all_tokens"):
            raise CheckError("mode must be word|phrase|all_tokens")
        return {
            "topic": aliases,
            "partitions": list(partitions),
            "fields": list(fields),
            "mode": mode,
        }
    if kind == "capability_present":
        allowed = (
            "globs", "exclude_globs", "argv", "fixture", "success_regex",
            "timeout_s", "max_candidates",
        )
        _require_keys(target, allowed, "%s target" % kind)
        globs = target["globs"]
        if not isinstance(globs, list) or not globs:
            raise CheckError("globs must be a non-empty list")
        for pattern in globs:
            _require_rel_path(pattern, "glob")
        excludes = target["exclude_globs"]
        if not isinstance(excludes, list):
            raise CheckError("exclude_globs must be a list")
        for pattern in excludes:
            _require_rel_path(pattern, "exclude_glob")
        argv = target["argv"]
        if not isinstance(argv, list) or not all(isinstance(arg, str) for arg in argv):
            raise CheckError("argv must be a list of strings (may be empty)")
        fixture = target["fixture"]
        if not isinstance(fixture, dict) or not fixture:
            raise CheckError("fixture must be a non-empty path -> content map")
        for path, content in fixture.items():
            _require_rel_path(path, "fixture path")
            if not isinstance(content, str):
                raise CheckError("fixture %r content must be a string" % path)
        try:
            success = re.compile(target["success_regex"])
        except re.error as exc:
            raise CheckError("success_regex does not compile: %s" % exc)
        if success.search(""):
            raise CheckError("success_regex matches the empty string")
        timeout = target["timeout_s"]
        if type(timeout) is not int or not 1 <= timeout <= 120:
            raise CheckError("timeout_s must be an integer in 1..120")
        cap = target["max_candidates"]
        if type(cap) is not int or not 1 <= cap <= 64:
            raise CheckError("max_candidates must be an integer in 1..64")
        return {
            "globs": list(globs),
            "exclude_globs": list(excludes),
            "argv": list(argv),
            "fixture": dict(fixture),
            "success_regex": target["success_regex"],
            "timeout_s": timeout,
            "max_candidates": cap,
        }
    raise CheckError("unknown probe_kind: %r" % (kind,))


PROBE_VALUE_TYPES = {
    "path_absent": bool,
    "path_present": bool,
    "grep_absent": bool,
    "count_eq": int,
    "sha256_eq": str,
    "topic_owner_absent": bool,
    "capability_present": bool,
}


def validate_check(check, before_text, seen_ids=None):
    """Validate one declared check against its claim's `before`.

    Returns the normalized check.  Raises CheckError for anything the gate
    must not silently accept: unknown kind, missing/wrong-typed expect, a
    clause that is not a verbatim substring of `before`, a target with
    unknown keys, or a capability target that names a tool instead of
    describing behavior.
    """
    if not isinstance(check, dict):
        raise CheckError("check must be an object")
    allowed = ("id", "clause", "probe_kind", "target", "expect", "evidence_command", "note")
    unknown = sorted(set(check) - set(allowed))
    if unknown:
        raise CheckError("check has unknown key(s): %s" % ", ".join(unknown))
    for required in ("clause", "probe_kind", "target", "expect", "evidence_command"):
        if required not in check:
            raise CheckError("check is missing required key %r" % required)
    if not isinstance(check["clause"], str) or not _norm_ws(check["clause"]):
        raise CheckError("clause must be a non-empty string")
    clause = _norm_ws(check["clause"])
    if _norm_ws(before_text).lower().find(clause.lower()) < 0:
        raise CheckError("clause is not a verbatim substring of the claim's `before`: %r" % clause)
    kind = check["probe_kind"]
    if kind not in PROBE_VALUE_TYPES:
        raise CheckError(
            "unknown probe_kind %r; closed set is %s"
            % (kind, ", ".join(sorted(PROBE_VALUE_TYPES)))
        )
    expect = check["expect"]
    expected_type = PROBE_VALUE_TYPES[kind]
    if expected_type is bool:
        if type(expect) is not bool:
            raise CheckError("%s expect must be a JSON boolean, got %r" % (kind, expect))
    elif expected_type is int:
        if type(expect) is not int:
            raise CheckError("count_eq expect must be a JSON integer, got %r" % (expect,))
        if expect < 0:
            raise CheckError("count_eq expect must be >= 0")
    else:
        if not isinstance(expect, str) or not HEX64.match(expect.lower()):
            raise CheckError("sha256_eq expect must be 64 hex characters")
        expect = expect.lower()
    target = _normalize_target(kind, check["target"])
    evidence = check["evidence_command"]
    if not isinstance(evidence, str) or not evidence.strip():
        raise CheckError("evidence_command must be a non-empty string")
    if "\n" in evidence or len(evidence) > 500:
        raise CheckError("evidence_command must be a single line of at most 500 characters")
    if re.search(r"(?:^|[;&|]\s*)(?:rm|mv)\s|git\s+(?:checkout|reset|commit|push|clean)\b", evidence):
        raise CheckError("evidence_command must be read-only: %r" % evidence)
    check_id = check.get("id")
    if check_id is not None:
        if not isinstance(check_id, str) or not check_id.strip():
            raise CheckError("id must be a non-empty string when present")
        if seen_ids is not None:
            if check_id in seen_ids:
                raise CheckError("duplicate check id %r" % check_id)
            seen_ids.add(check_id)
    note = check.get("note")
    if note is not None and not isinstance(note, str):
        raise CheckError("note must be a string when present")
    return {
        "id": check_id,
        "clause": clause,
        "probe_kind": kind,
        "target": target,
        "expect": expect,
        "evidence_command": evidence.strip(),
        "note": note,
    }


def validate_claim_checks(claim):
    """Validate a claim's `before_checks`.

    Returns a list of normalized checks.  An absent or empty list is legal
    *input* and returns ``[]`` -- the claim is then ``could-not-evaluate`` at
    the verdict layer, never fresh.  Structural errors raise CheckError and
    the caller must map them to exit 2 (malformed), not to a verdict.
    """
    if not isinstance(claim, dict):
        raise CheckError("claim must be an object")
    before = claim.get("before")
    if not isinstance(before, str) or not _norm_ws(before):
        raise CheckError("claim %r has no non-empty `before` string" % claim.get("id"))
    raw = claim.get("before_checks")
    if raw is None:
        return []
    if not isinstance(raw, list):
        raise CheckError("claim %r: before_checks must be a list" % claim.get("id"))
    seen_ids = set()
    return [validate_check(item, before, seen_ids) for item in raw]


def polarity_label(check):
    """Human-readable statement of the declared polarity, for the report."""
    kind = check["probe_kind"]
    expect = check["expect"]
    if PROBE_VALUE_TYPES[kind] is bool:
        if expect:
            return "clause asserts the %s predicate" % kind
        return "clause asserts the NEGATION of the %s predicate" % kind
    if kind == "count_eq":
        return "clause asserts exactly %d match(es)" % expect
    return "clause asserts sha256 == %s" % expect


def _clip(text, limit=160):
    text = _norm_ws(text)
    return text if len(text) <= limit else text[: limit - 1] + "\u2026"


def _result(check, measured, holds, detail, evidence, status=None):
    return {
        "id": check["id"],
        "clause": check["clause"],
        "probe_kind": check["probe_kind"],
        "target": check["target"],
        "expect": check["expect"],
        "measured": measured,
        "status": status or ("holds" if holds else "mismatch"),
        "detail": detail,
        "evidence": evidence,
        "evidence_command": check["evidence_command"],
        "polarity": polarity_label(check),
    }


def _probe_path_absent(check, tree):
    path = check["target"]["path"]
    present = tree.exists(path)
    return _result(
        check,
        not present,
        (not present) == check["expect"],
        "%s is %s" % (path, "present" if present else "absent"),
        [path],
    )


def _probe_path_present(check, tree):
    path = check["target"]["path"]
    present = tree.exists(path)
    return _result(
        check,
        present,
        present == check["expect"],
        "%s is %s" % (path, "present" if present else "absent"),
        [path],
    )


def _probe_grep_absent(check, tree):
    target = check["target"]
    hits = _grep(tree, target["regex"], target["glob"])
    value = len(hits) == 0
    evidence = ["%s:%d: %s" % (path, number, _clip(line)) for path, number, line in hits[:8]]
    return _result(
        check,
        value,
        value == check["expect"],
        "%s /%s/ -> %d hit(s)" % (target["glob"], target["regex"], len(hits)),
        evidence,
    )


def _probe_count_eq(check, tree):
    target = check["target"]
    paths = sorted(_glob(tree, target["glob"]))
    value = len(paths)
    digest = hashlib.sha256("\n".join(paths).encode("utf-8")).hexdigest()
    return _result(
        check,
        value,
        value == check["expect"],
        "%s -> %d file(s); paths_sha256=%s" % (target["glob"], value, digest[:16]),
        paths[:8] + (["... paths_sha256=%s" % digest] if paths else []),
    )


def _probe_sha256_eq(check, tree):
    path = check["target"]["path"]
    try:
        digest = tree.sha256(path).lower()
    except Exception as exc:  # absent/unreadable blob is not a fresh premise
        return _result(
            check, None, False, "%s: could not read at baseline (%s)" % (path, exc),
            [path], status="could-not-evaluate",
        )
    return _result(
        check,
        digest,
        digest == check["expect"],
        "%s sha256=%s" % (path, digest),
        ["%s sha256 %s" % (path, digest)],
    )


def _probe_topic_owner_absent(check, tree):
    target = check["target"]
    hits = []
    for partition in target["partitions"]:
        for path in sorted(_glob(tree, "corpus/knowledge/%s/*.md" % partition)):
            lines = tree.read(path).splitlines()
            in_body = True
            for number, line in enumerate(lines, 1):
                if number > 200:
                    break
                if line.startswith("## "):
                    in_body = False
                if not in_body and number > 1:
                    break
                for field in target["fields"]:
                    match = HEADER_FIELDS[field].match(line)
                    if not match:
                        continue
                    for alias in target["topic"]:
                        if _alias_match(match.group(1), alias, target["mode"]):
                            hits.append((path, number, field, alias, line))
    owners = sorted({path for path, _n, _f, _a, _l in hits})
    value = len(owners) == 0
    evidence = [
        "%s:%d (%s; %s) %s" % (path, number, field, alias, _clip(line))
        for path, number, field, alias, line in hits[:8]
    ]
    return _result(
        check,
        value,
        value == check["expect"],
        "%d owner(s): %s" % (len(owners), ", ".join(owners) if owners else "none"),
        evidence,
    )


def _materialize_fixture(root, fixture):
    for rel, content in fixture.items():
        target = os.path.join(root, rel)
        os.makedirs(os.path.dirname(target), exist_ok=True)
        with open(target, "w", encoding="utf-8") as handle:
            handle.write(content)


def _probe_capability_present(check, tree, allow_exec=True):
    target = check["target"]
    candidates = set()
    for pattern in target["globs"]:
        candidates.update(_glob(tree, pattern))
    for pattern in target["exclude_globs"]:
        candidates.difference_update(_glob(tree, pattern))
    candidates = sorted(
        path for path in candidates if path.endswith(".py")
    )
    if not candidates:
        return _result(
            check, False, False == check["expect"], "no candidate .py matched",
            ["globs: %s" % ", ".join(target["globs"])],
        )
    if len(candidates) > target["max_candidates"]:
        return _result(
            check, None, False,
            "%d candidates exceed max_candidates=%d; refusing a partial scan"
            % (len(candidates), target["max_candidates"]),
            candidates[:8], status="could-not-evaluate",
        )
    if not allow_exec:
        return _result(
            check, None, False, "capability execution disabled (--no-exec)",
            candidates[:8], status="could-not-evaluate",
        )
    success = re.compile(target["success_regex"])
    hits, evidence, errors = [], [], 0
    for path in candidates:
        try:
            source = tree.read(path)
        except Exception as exc:
            errors += 1
            evidence.append("%s: unreadable (%s)" % (path, exc))
            continue
        work = tempfile.mkdtemp(prefix="claims-freshness-cap-")
        try:
            _materialize_fixture(work, target["fixture"])
            rel = os.path.join("tools", "harness", os.path.basename(path))
            os.makedirs(os.path.dirname(os.path.join(work, rel)), exist_ok=True)
            with open(os.path.join(work, rel), "w", encoding="utf-8") as handle:
                handle.write(source)
            proc = subprocess.run(
                [sys.executable, "-I", "-B", rel, *target["argv"]],
                cwd=work,
                capture_output=True,
                text=True,
                timeout=target["timeout_s"],
            )
            output = (proc.stdout or "") + (proc.stderr or "")
            matched = proc.returncode == 0 and success.search(output) is not None
            if matched:
                hits.append(path)
            first = _clip(output.splitlines()[0]) if output.splitlines() else ""
            evidence.append(
                "%s: exit=%d regex=%s %s"
                % (path, proc.returncode, "hit" if matched else "miss", first)
            )
        except subprocess.TimeoutExpired:
            errors += 1
            evidence.append("%s: timeout after %ds" % (path, target["timeout_s"]))
        except OSError as exc:
            errors += 1
            evidence.append("%s: execution error (%s)" % (path, exc))
        finally:
            shutil.rmtree(work, ignore_errors=True)
    value = bool(hits)
    if not hits and errors == len(candidates):
        return _result(
            check, None, False,
            "all %d candidate(s) failed to execute; capability not measurable" % errors,
            evidence, status="could-not-evaluate",
        )
    return _result(
        check,
        value,
        value == check["expect"],
        "%d/%d candidate(s) pass the declared behavior%s"
        % (len(hits), len(candidates), (": " + ", ".join(hits)) if hits else ""),
        evidence,
    )


_PROBES = {
    "path_absent": _probe_path_absent,
    "path_present": _probe_path_present,
    "grep_absent": _probe_grep_absent,
    "count_eq": _probe_count_eq,
    "sha256_eq": _probe_sha256_eq,
    "topic_owner_absent": _probe_topic_owner_absent,
    "capability_present": _probe_capability_present,
}


def evaluate_check(check, tree, allow_exec=True):
    """Measure one validated check.  Never returns holds=True on an error."""
    try:
        if check["probe_kind"] == "capability_present":
            return _PROBES[check["probe_kind"]](check, tree, allow_exec=allow_exec)
        return _PROBES[check["probe_kind"]](check, tree)
    except CheckError:
        raise
    except Exception as exc:
        return _result(
            check, None, False, "probe error: %s" % exc, [], status="could-not-evaluate"
        )


def claim_status(results):
    """Claim-level status.  A proven mismatch outranks an unmeasurable clause."""
    if not results:
        return "could-not-evaluate"
    statuses = [row["status"] for row in results]
    if "malformed" in statuses:
        return "malformed"
    if "mismatch" in statuses:
        return "stale"
    if "could-not-evaluate" in statuses:
        return "could-not-evaluate"
    return "fresh"


# --- registry selftest ----------------------------------------------------

class FixtureTree:
    """Minimal in-memory baseline view used only by the selftest."""

    def __init__(self, files):
        self._files = dict(files)

    def files(self):
        return sorted(self._files)

    def exists(self, path):
        return path in self._files

    def glob(self, pattern):
        return [path for path in sorted(self._files) if fnmatch.fnmatch(path, pattern)]

    def read(self, path):
        if path not in self._files:
            raise FileNotFoundError(path)
        return self._files[path]

    def sha256(self, path):
        return hashlib.sha256(self.read(path).encode("utf-8")).hexdigest()

    def grep(self, regex, glob, case_sensitive=False, max_lines=0):
        flags = 0 if case_sensitive else re.I
        match = re.compile(regex, flags)
        hits = []
        for path in self.glob(glob):
            for number, line in enumerate(self.read(path).splitlines(), 1):
                if max_lines and number > max_lines:
                    break
                if match.search(line):
                    hits.append((path, number, line))
        return hits


def _fixture_capability_tool(name, body, ok=True):
    return (
        "#!/usr/bin/env python3\n"
        "%s\n" % body
    )


def selftest_registry():
    checks = []
    used_kinds = set()

    def check(name, condition, detail=""):
        checks.append((name, bool(condition), detail))
        print(("PASS " if condition else "FAIL ") + name + ((" " + detail) if detail else ""))

    def one(kind, target, expect, clause="fixture clause", before="fixture clause"):
        normalized = validate_check(
            {
                "clause": clause,
                "probe_kind": kind,
                "target": target,
                "expect": expect,
                "evidence_command": "git ls-tree -r --name-only HEAD",
            },
            before,
        )
        used_kinds.add(kind)
        return normalized

    # S1/S2 path probes and polarity
    tree = FixtureTree({"alpha.md": "alpha\n"})
    r = evaluate_check(one("path_absent", {"path": "beta.md"}, True), tree)
    check("S1 path_absent true holds", r["status"] == "holds", r["detail"])
    r2 = evaluate_check(one("path_absent", {"path": "beta.md"}, False), tree)
    check("S1b same measurement, declared expect=false mismatches", r2["status"] == "mismatch")
    r = evaluate_check(one("path_present", {"path": "alpha.md"}, True), tree)
    check("S2 path_present true holds", r["status"] == "holds")
    r = evaluate_check(one("path_present", {"path": "alpha.md"}, False), tree)
    check("S2b path_present false mismatches", r["status"] == "mismatch")

    # S3 grep_absent
    tree = FixtureTree({"a.md": "harbour\nquay\n", "b.md": "quarry\n"})
    r = evaluate_check(one("grep_absent", {"glob": "*.md", "regex": "lithic"}, True), tree)
    check("S3 grep_absent no hit holds", r["status"] == "holds")
    r = evaluate_check(one("grep_absent", {"glob": "*.md", "regex": "quarry"}, True), tree)
    check("S3b grep_absent hit mismatches", r["status"] == "mismatch")
    r = evaluate_check(one("grep_absent", {"glob": "*.md", "regex": "harbour"}, False), tree)
    check("S3c grep_absent expect=false holds on a hit (polarity is declared)", r["status"] == "holds")

    # S4 count_eq
    tree = FixtureTree({"a.md": "", "b.md": "", "c.txt": ""})
    r = evaluate_check(one("count_eq", {"glob": "*.md"}, 2), tree)
    check("S4 count_eq 2 holds", r["status"] == "holds", r["detail"])
    r = evaluate_check(one("count_eq", {"glob": "*.md"}, 3), tree)
    check("S4b count_eq 3 mismatches", r["status"] == "mismatch")

    # S5 sha256_eq
    digest = hashlib.sha256(b"alpha\n").hexdigest()
    tree = FixtureTree({"alpha.md": "alpha\n"})
    r = evaluate_check(one("sha256_eq", {"path": "alpha.md"}, digest), tree)
    check("S5 sha256_eq holds", r["status"] == "holds")
    r = evaluate_check(one("sha256_eq", {"path": "alpha.md"}, "0" * 64), tree)
    check("S5b sha256_eq wrong digest mismatches", r["status"] == "mismatch")
    r = evaluate_check(one("sha256_eq", {"path": "missing.md"}, digest), tree)
    check("S5c sha256_eq absent file is could-not-evaluate, never green",
          r["status"] == "could-not-evaluate")

    # S6 topic_owner_absent
    owned = FixtureTree(
        {
            "corpus/knowledge/myth-symbol/mineral-stone-symbolism.md":
                "# Stone, gem and metal symbolism — the lithic register\n\n- topic: the lithic register\n",
            "corpus/knowledge/linguistics/phonetics.md":
                "# Phonetics\n\n- topic: segmental phonology\n",
        }
    )
    topic_target = {
        "topic": ["lithic"],
        "partitions": ["myth-symbol", "linguistics"],
        "fields": ["h1", "topic"],
        "mode": "word",
    }
    r = evaluate_check(one("topic_owner_absent", topic_target, True), owned)
    check("S6 topic_owner_absent finds the real owner and mismatches",
          r["status"] == "mismatch" and "mineral-stone-symbolism.md" in r["detail"], r["detail"])
    r = evaluate_check(one("topic_owner_absent", topic_target, False), owned)
    check("S6b topic_owner_absent expect=false holds on an owner", r["status"] == "holds")
    clean = FixtureTree({"corpus/knowledge/myth-symbol/other.md": "# Other\n\n- topic: celestial\n"})
    r = evaluate_check(one("topic_owner_absent", topic_target, True), clean)
    check("S6c topic_owner_absent clean tree holds", r["status"] == "holds")
    try:
        one("topic_owner_absent", dict(topic_target, topic=["register"]), True)
        check("S6d generic topic is rejected", False)
    except CheckError:
        check("S6d generic topic is rejected", True)

    # S7 capability_present, behavioral and name-independent
    passing = _fixture_capability_tool(
        "passing.py",
        "import sys\nprint('CAP_OK')\nsys.exit(0)\n",
    )
    failing = _fixture_capability_tool(
        "failing.py",
        "import sys\nprint('CAP_NO')\nsys.exit(1)\n",
    )
    cap_tree = FixtureTree(
        {
            "tools/harness/zzz-renamed.py": passing,
            "tools/harness/aaa-other.py": failing,
            "corpus/knowledge/fixture/a.md": "# Fixture\n",
        }
    )
    cap_target = {
        "globs": ["tools/**/*.py"],
        "exclude_globs": ["tools/gates/frozen/**"],
        "argv": [],
        "fixture": {"corpus/knowledge/fixture/a.md": "# Fixture\n"},
        "success_regex": "CAP_OK",
        "timeout_s": 20,
        "max_candidates": 8,
    }
    r = evaluate_check(one("capability_present", cap_target, True), cap_tree)
    check("S7 capability_present finds behavior under a renamed tool",
          r["status"] == "holds" and "zzz-renamed.py" in r["detail"], r["detail"])
    r = evaluate_check(one("capability_present", cap_target, False), cap_tree)
    check("S7b capability_present expect=false mismatches on a real capability",
          r["status"] == "mismatch")
    no_cap = FixtureTree({"tools/harness/aaa-other.py": failing})
    r = evaluate_check(one("capability_present", cap_target, True), no_cap)
    check("S7c no behavior -> measured false, mismatch", r["status"] == "mismatch")
    r = evaluate_check(one("capability_present", cap_target, True), cap_tree, allow_exec=False)
    check("S7d --no-exec is could-not-evaluate, never green",
          r["status"] == "could-not-evaluate")

    # S8 strict typing / malformed schema
    def rejects(name, **kwargs):
        try:
            one(**kwargs)
            check(name, False)
        except CheckError:
            check(name, True)

    rejects("S8 string 'true' is not a boolean expect",
            kind="path_absent", target={"path": "x.md"}, expect="true")
    rejects("S8b integer 1 is not a boolean expect",
            kind="path_absent", target={"path": "x.md"}, expect=1)
    rejects("S8c count_eq string is rejected",
            kind="count_eq", target={"glob": "*.md"}, expect="2")
    rejects("S8d unknown probe kind is rejected",
            kind="path_exists", target={"path": "x.md"}, expect=True)
    rejects("S8e clause not present in before is rejected",
            kind="path_absent", target={"path": "x.md"}, expect=True,
            clause="a different sentence")
    rejects("S8f path escape is rejected",
            kind="path_absent", target={"path": "../outside.md"}, expect=True)
    rejects("S8g unknown target key is rejected",
            kind="path_absent", target={"path": "x.md", "glob": "*"}, expect=True)
    rejects("S8h capability target naming a tool is rejected",
            kind="capability_present",
            target=dict(cap_target, name="couples-reference-extractor.py"), expect=True)
    rejects("S8i grep regex matching empty string is rejected",
            kind="grep_absent", target={"glob": "*.md", "regex": ".*"}, expect=True)

    # S9 claim-level precedence
    malformed = {"status": "malformed"}
    stale = {"status": "mismatch"}
    unknown = {"status": "could-not-evaluate"}
    holds = {"status": "holds"}
    check("S9 no checks -> could-not-evaluate", claim_status([]) == "could-not-evaluate")
    check("S9b mismatch outranks could-not-evaluate", claim_status([stale, unknown]) == "stale")
    check("S9c malformed outranks stale", claim_status([malformed, stale]) == "malformed")
    check("S9d all holds -> fresh", claim_status([holds, holds]) == "fresh")

    # S10 every registry kind exercised + determinism
    check("S10 registry and value-type tables agree", set(_PROBES) == set(PROBE_VALUE_TYPES))
    check("S10b all seven probe kinds exercised by at least one control",
          used_kinds == set(PROBE_VALUE_TYPES), ", ".join(sorted(used_kinds)))
    check("S10c glob: * does not cross /, ** does",
          _match_glob("corpus/knowledge/*/*.md", "corpus/knowledge/a/b.md")
          and not _match_glob("corpus/knowledge/*/*.md", "corpus/knowledge/a/b/c.md")
          and _match_glob("tools/**/*.py", "tools/harness/candidate.py")
          and _match_glob("tools/**/*.py", "tools/deep/harness/candidate.py"))
    r1 = evaluate_check(one("count_eq", {"glob": "*.md"}, 2), FixtureTree({"a.md": "", "b.md": ""}))
    r2 = evaluate_check(one("count_eq", {"glob": "*.md"}, 2), FixtureTree({"a.md": "", "b.md": ""}))
    check("S11 deterministic on identical inputs",
          r1["measured"] == r2["measured"] and r1["status"] == r2["status"])

    # S12 claim-level validator
    payload = {
        "id": "X",
        "before": "a premise",
        "before_checks": [
            {
                "clause": "a premise",
                "probe_kind": "path_absent",
                "target": {"path": "x.md"},
                "expect": True,
                "evidence_command": "git ls-tree -r --name-only HEAD",
            }
        ],
    }
    check("S12 validate_claim_checks returns one normalized check",
          len(validate_claim_checks(payload)) == 1)
    check("S12b absent before_checks returns [] (could-not-evaluate, not fresh)",
          validate_claim_checks({"id": "X", "before": "a premise"}) == [])
    for label, bad in (
        ("S12c non-list before_checks rejected", {"id": "X", "before": "a", "before_checks": {}}),
        ("S12d missing before rejected", {"id": "X", "before_checks": []}),
        ("S12e duplicate check ids rejected", {
            "id": "X", "before": "a premise",
            "before_checks": [
                {"id": "1", "clause": "a premise", "probe_kind": "path_absent",
                 "target": {"path": "x.md"}, "expect": True,
                 "evidence_command": "git ls-tree"},
                {"id": "1", "clause": "a premise", "probe_kind": "path_absent",
                 "target": {"path": "y.md"}, "expect": True,
                 "evidence_command": "git ls-tree"},
            ],
        }),
    ):
        try:
            validate_claim_checks(bad)
            check(label, False)
        except CheckError:
            check(label, True)

    # S13 evidence_command is read-only by lint
    try:
        validate_check(
            {
                "clause": "fixture clause", "probe_kind": "path_absent",
                "target": {"path": "x.md"}, "expect": True,
                "evidence_command": "rm -rf corpus",
            },
            "fixture clause",
        )
        check("S13 destructive evidence_command rejected", False)
    except CheckError:
        check("S13 destructive evidence_command rejected", True)

    passed = sum(1 for _n, ok, _d in checks if ok)
    total = len(checks)
    print("PROBE-REGISTRY SELFTEST: %d/%d" % (passed, total))
    return 0 if passed == total else 1


# The actual probe function table, exported for the assembler.
PROBES = dict(_PROBES)


if __name__ == "__main__":
    sys.exit(selftest_registry())
```

Fenced-body sha256 (LF line endings, no trailing fence): `a60b0a22df2d73c1a4075662d76a1d5c25a5caa8f6f35b72ffdf0c2ed772c191`.

## Appendix B — exact checks used in the measured run

The declarations in §4 are the O-1, C-1 and Ca-1 checks. The full set adds C-2 and C-3:

```json
{"id": "C-2", "clause": "myth-symbol 26", "probe_kind": "count_eq",
 "target": {"glob": "corpus/knowledge/myth-symbol/*.md"}, "expect": 26,
 "evidence_command": "git ls-tree -r --name-only 7ceff59 -- corpus/knowledge/myth-symbol"}
{"id": "C-3", "clause": "total 223", "probe_kind": "count_eq",
 "target": {"glob": "corpus/knowledge/*/*.md"}, "expect": 223,
 "evidence_command": "git ls-tree -r --name-only 7ceff59 -- corpus/knowledge | grep -c '\\.md$'"}
```

## Appendix C — reproduction

The registry selftest is self-contained (its `FixtureTree` is in Appendix A):

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
awk '/^```python$/{f=1;next}/^```$/{f=0}f' reports/round-47/op/O02-probe-registry.md > .scratch/o02/probe_registry.py
python3 -B .scratch/o02/probe_registry.py
# PROBE-REGISTRY SELFTEST: 43/43 ; exit 0
```

The baseline table in §5.2 was produced by a scratch adapter that supplies the four `tree` methods from `git ls-tree`/`git show`; that adapter belongs to O01's core and is intentionally not fenced here. Its behavior is fully specified by the seam in §6, and the Appendix A selftest exercises the same probe functions with `FixtureTree`.
