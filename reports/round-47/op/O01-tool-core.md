# O01 — freshness-gate core: claims parser + commit-only baseline

- Seat: `O01` | role executor | claim **O** (operability) | round 47, loop 2
- Out path: `reports/round-47/op/O01-tool-core.md` (this seat's only durable write)
- Contract: `reports/round-47/claims.json:36-48`; seat mission `reports/round-47/targets.json:33`
- Round baseline: `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`claims.json:7`; `git rev-parse --verify '6e9a30d^{commit}'`), tree `765306d294a2f0d6634cfbb15380bcdfd30144cf`
- Cut: 2026-10-19T18:02Z, `git version 2.55.0`, `Python 3.14.7`
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`
- Scope: **part 1 of 3** — input contract, claim parsing, baseline snapshot. It does not implement probe semantics (O02), verdict/exit dispatch (O03), or a CLI.

## 1. Deliverable and assembly contract

The fenced block in §8 is 633 lines / 24,754 bytes, SHA-256
`72c294f2c49dc53f3f7e7e65b0dc646e238a56b19473f84b63f1cb5bbf13b876`.
It is written as the **head** of the assembled tool `tools/harness/claims-freshness.py`
(absent at HEAD: `ls tools/harness/claims-freshness.py` → no such file), followed by:

1. this block (docstring, constants, errors, parser, `Baseline`);
2. part 2 (O02): probe handlers over the `Baseline` API and the optional legacy miner;
3. part 3 (O03): verdict aggregation, exit dispatch, argparse entry point.

Part 1 defines **no `main()`** and no probe semantics, so it is importable and testable
alone. The assembly is plain concatenation; nothing in part 2/3 needs to edit these bytes.

## 2. What the core enforces

| invariant | implementation | measured control |
|---|---|---|
| A claims file cannot be evaluated without a baseline | `load_claims` raises `GateInputError` when `baseline_commit` is absent/empty; `Baseline` has no worktree constructor | `no-baseline.json` → rejected (exit-2 class) |
| A baseline is always a **commit**, never a tree/tag/blob | `resolve_commit` runs `rev-parse <rev>^{commit}` then `cat-file -t` and requires `commit` | `HEAD` resolves to the full sha; `--help` and `no-such-rev-o01` rejected |
| Every corpus/tool byte comes from the named commit | `ls-tree -r -z --full-tree` builds a path→blob-oid index; `cat-file --batch` returns blob bytes; `read`/`sha256`/`grep`/`glob`/`file_count` all route through that index | resolver absent at `7ceff59`, present at `6e9a30d`; §3 |
| Probe vocabulary is closed | `PROBE_KINDS` is a frozenset of the seven names in the claim; unknown kinds are malformed | `unknown-kind.json` (`vibes`) → rejected |
| Polarity is declared, never inferred | `before_checks[].expect` is required and must be boolean; missing `expect` is malformed | `no-expect.json` → rejected |
| One schema per claim | declaring both `before_checks` and legacy `freshness_probes` is malformed | `both-fields.json` → rejected |
| Claims are identifiable and unambiguous | non-empty unique `id`, non-empty `axis` and `before`, integer `round >= 1` | duplicate id, missing id/before/round, empty claims list, non-JSON, top-level array all rejected |
| Paths cannot escape the repo | `_safe_relpath` rejects absolute paths, `..`, empty and `.` segments; globs use the same rule | `../etc/passwd`, `/etc/passwd`, `../*` → rejected |
| Globs are segment-local | `*`/`?` are matched per segment with `fnmatch.fnmatchcase`; only a whole `**` segment recurses | `corpus/knowledge/*/*.md` does **not** match `corpus/knowledge/a/b/c.md`; `tools/**/*.py` matches both `tools/x.py` and `tools/harness/x.py` |
| Evaluation is deterministic | no timestamps/randomness in parse or measurement; blob cache keyed by path; sorted file lists | parsing and measuring twice yields the identical `describe()` dict |
| Input failures are typed | every malformed case raises `GateInputError` whose `exit_code` is `EXIT_MALFORMED` (2) | 12 malformed fixtures |

Exit constants are defined here and enforced in part 3:
`EXIT_OK=0`, `EXIT_STALE=1`, `EXIT_MALFORMED=2`, `EXIT_COULD_NOT_EVALUATE=3`.
A claim with no declared checks is legal input but **could-not-evaluate**, never fresh;
part 3 must exit non-zero for it (the r47 O threshold: "could-not-evaluate != green").

## 3. Baseline-only evidence — the r43 trap, measured

The design decision is not stylistic. At the r43 baseline the durable couples resolver was
absent; in the current worktree it exists. A gate that could fall back to the worktree would
pass the exact claim it exists to catch.

| measurement | command | result |
|---|---|---|
| resolver at r43 baseline | `git ls-tree -r --name-only 7ceff59 tools/harness/` | no `basename-couples-resolver.py` |
| resolver at r47 baseline | `git ls-tree -r --name-only 6e9a30d tools/harness/` | `basename-couples-resolver.py` present |
| resolver in worktree | `sha256sum tools/harness/basename-couples-resolver.py` | `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64` |
| witness at r43 baseline | `Baseline.sha256` = `git show 7ceff59:… \| sha256sum` | `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1` |
| corpus count at both commits | `Baseline.file_count("corpus/knowledge")` | 223 at `7ceff59` and at `6e9a30d` |
| r43 Ca artifact at baseline | `git ls-tree -r --name-only 7ceff59 reports/round-43/calib/` | **0 files** |
| r43 Ca artifact in worktree | `ls reports/round-43/calib/` | 5 files, incl. `dispositions-r38-r39.json` |

The Ca row is the mirror image: a worktree-based gate would flag r43 Ca **stale** because the
disposition artifact exists *now*. Baseline evaluation correctly leaves it fresh. There is
therefore no worktree mode in the core at all — not a flag, not a fallback. The only override
is another commit (`open_claims(..., at=...)`), and the deviation is returned for part 3 to
print.

## 4. Probe-design facts handed to O02 and O05

1. **A naive `path_absent` probe does not catch r43 O.** At `7ceff59`,
   `Baseline.exists("tools/harness/basename-couples-resolver.py")` is `False`, so a
   `path_absent` check on the claim-named path is **true** and the claim would pass. This
   reproduces R01 §4.2: the gate needs capability/ownership, not literal paths.
2. **A capability conjunction does catch it.** Requiring all four tokens
   `def couples_block`, `basename_index`, `ambiguous`, `fallback` in one `tools/**/*.py`
   file yields exactly `['tools/harness/couples-reference-extractor.py']` at `7ceff59`
   and both the witness and successor at `6e9a30d`. An alternation over those four tokens
   is noise: it produces 523 hits in 39 files; the conjunction is the signal.
3. **Topic ownership is a header scan.** `lithic` at `7ceff59` is owned by
   `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:1` (H1), `:3` (`- gap filled:`)
   and `:5` (`- topic:`). A whole-file word-boundary search finds 13 lines in 3 files — the
   other two are an archaeology title and a mulch row — so O02's `topic_owner_absent` must
   scan H1 + those two fields, as the prototype did; a plain grep would claim three owners.
4. **The interface composes.** A throwaway adapter (scratch-only, **not** the durable
   registry) implements each kind as a one-line predicate over `Baseline` and applies
   `measured == expect`:

```
r43 O at 7ceff59: STALE (capability_present measured=True expect=False)
r43 C at 7ceff59: STALE (topic_owner_absent measured=False expect=True)
r43 Ca at 7ceff59: FRESH (path_absent measured=True expect=True)
r44 O control at c9f4eaa: FRESH (path_absent measured=True expect=True)
```

So the core's public surface is sufficient for the required positive regression, the Ca
negative control and a fresh r44 control; O02/O05 own the durable handlers and the filed
artifacts.

## 5. Defects found by this seat's own suite (before filing)

Two real bugs in the first draft, both caught by assertions rather than review:

1. **Glob segments crossed `/`.** The first translator used `fnmatch.translate` per segment,
   whose `.*` matches `/`; `corpus/knowledge/*/*.md` matched `corpus/knowledge/a/b/c.md`.
   Replaced with segment-wise `fnmatch.fnmatchcase` recursion; only `**` recurses.
2. **`grep` indexed undecoded blobs.** `warm()` populated the byte cache, then `grep` read
   the text cache and raised `KeyError` on the first corpus scan. Fixed to decode through
   `read()`; the batch loader remains the only byte path.

No other defect is claimed. Both fixes are inside the fenced bytes; the suite was re-run
green afterwards.

## 6. Verification transcript

Command and result (full output kept at `.scratch/o01-r47/selftest.out`; scratch is not durable):

```
$ export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
$ python3 -B -W error::DeprecationWarning .scratch/o01-r47/check_core.py
...
PASS cat-file batch == git show bytes
PASS read text decodes

PASS 70 / 70
elapsed 0.069s
exit=0
```

70 assertions in nine groups: live-claims parsing (r47/r43), commit resolution, baseline-only
evaluation, counts/glob semantics, path safety, grep semantics, valid/legacy schema,
12 malformed fixtures, override provenance and determinism, and blob-read integrity
(`cat-file --batch` bytes equal `git show` bytes for the witness). Representative measured
values are in §3; timings on this host: full 223-file glob 0.002 s, one 61 KB entry read
0.001 s, `grep` over 223 entries 0.014 s, capability scan over 55 Python files 0.052 s.

## 7. API handoff (binding for parts 2 and 3)

```text
load_claims(path) -> ClaimsDoc(round, baseline_input, claims, raw)
open_baseline(root, rev) -> Baseline
open_claims(path, at=None, repo_root=None) -> (ClaimsDoc, Baseline, deviation|None)
Baseline: commit, tree, short, files(prefix), file_count(prefix), exists(path),
          read(path), read_bytes(path), sha256(path), glob(pattern),
          grep(pattern, glob, max_lines=0, limit=0), provenance()
Check:    clause, probe_kind, target (immutable mapping), expect (bool),
          evidence_command, expect_source ("declared" | "implied")
PROBE_KINDS: path_absent, path_present, grep_absent, count_eq, sha256_eq,
             topic_owner_absent, capability_present
```

Part 2 supplies `evaluate_check(check, baseline) -> bool` (the raw predicate for the kind);
part 3 decides a clause holds iff `measured == check.expect`. Part 2 also owns each kind's
target keys; part 1 deliberately does not freeze them. `describe(doc, baseline, deviation)`
is the JSON-safe provenance block for the report. `open_claims` binds parsing to baseline
resolution in one call, so a part-3 `--at` flag is a one-line pass-through and cannot
accidentally measure the worktree.

## 8. Fenced tool draft — part 1/3

```python
#!/usr/bin/env python3
"""Pre-dispatch claims-freshness gate — part 1/3: input contract + baseline.

A round declares a `baseline_commit` and, for each claim, a `before` sentence
describing the state that makes the claim worth dispatching.  r43 dispatched O
and C on premises already false at `7ceff59` (the durable resolver existed; the
lithic slot was owned) because nobody re-measured the prose before opening the
round — defect R01-43-12.  This gate re-derives each declared premise from the
Git object store at the claim's own baseline and refuses a stale dispatch.

This file is part 1 of 3 and is assembled by concatenation:

    part 1 (this block)  constants, errors, claim parsing, baseline snapshot
    part 2 (O02)         PROBE_HANDLERS + evaluate_check()
    part 3 (O03)         verdict aggregation, exit contract, argparse CLI

Part 1 defines no `main()` and no probe semantics.  It is importable on its own
and must remain so: the parser and the baseline are the parts every later probe
depends on.

Input contract
--------------
`claims.json` is a JSON object with:

    round             int >= 1
    baseline_commit   non-empty string, any rev `git rev-parse <rev>^{commit}`
                      resolves inside this repository (full sha, short sha, ref)
    claims            non-empty list of objects, each with:
        id            non-empty, unique within the file
        axis          non-empty (coverage|operability|calibration|cross|...)
        before        non-empty prose: the factual premise being checked
        after_required, claim, counting_commands, thresholds   optional
        before_checks optional list of declared probes:
            clause           non-empty quoted fragment of `before`
            probe_kind       one of PROBE_KINDS (closed vocabulary)
            target           object, probe-kind specific
            expect           boolean polarity: true iff the clause asserts the
                             raw predicate holds; REQUIRED — an undeclared
                             polarity is malformed, never assumed
            evidence_command optional shell command that reproduces the value
        freshness_probes  optional legacy alias for `before_checks`, entry shape
                          {"kind": ..., <target fields>}; polarity is implied
                          true and recorded as `implied`, never as declared

A claim with neither field has no declared checks.  That is legal input but it
is *could-not-evaluate*, never fresh: part 3 must exit non-zero for it.  Part 2
may additionally mine legacy prose, and must label every mined premise as mined.

Baseline semantics
------------------
Every measurement is taken from the commit named by `baseline_commit`, through
`git ls-tree -r -z` (path -> blob oid) and `git cat-file --batch` (blob bytes).
The worktree is never read.  There is deliberately no worktree mode: r43's O
premise is true at `7ceff59` and false in the worktree, so a gate that could
fall back to the worktree would pass the very claim it exists to catch.  An
override is allowed only as another commit (`--at <commit>`); the caller must
record the deviation.  A missing/unresolvable `baseline_commit` is malformed
input (exit 2), not an invitation to measure HEAD.

Exit constants (enforced by part 3)
-----------------------------------
    0  all claims fresh
    1  at least one claim stale
    2  malformed input or unusable baseline
    3  could-not-evaluate (a claim declared no checks and no premise was mined)

Read-only: opens files for reading and runs read-only Git plumbing.  Stdlib
only; no network, no worktree writes, no bytecode (`sys.dont_write_bytecode`).
"""
from __future__ import annotations

import fnmatch
import hashlib
import json
import os
import pathlib
import re
import subprocess
import sys
from dataclasses import dataclass
from types import MappingProxyType
from typing import Any, Iterable, Mapping

sys.dont_write_bytecode = True

TOOL = "tools/harness/claims-freshness.py"
VERSION = "2.0-part1"

EXIT_OK = 0
EXIT_STALE = 1
EXIT_MALFORMED = 2
EXIT_COULD_NOT_EVALUATE = 3

# Closed vocabulary.  Part 2 must implement exactly these handlers; a claims
# file naming anything else is malformed (never silently skipped).
PROBE_KINDS = frozenset(
    {
        "path_absent",
        "path_present",
        "grep_absent",
        "count_eq",
        "sha256_eq",
        "topic_owner_absent",
        "capability_present",
    }
)

CHECK_FIELDS = ("clause", "probe_kind", "target", "expect", "evidence_command")
_SHA1_RE = re.compile(r"^[0-9a-f]{40}$")


class GateInputError(ValueError):
    """Malformed claims input or unusable baseline.  CLI maps to exit 2."""

    exit_code = EXIT_MALFORMED


def _git_env() -> dict[str, str]:
    env = {key: value for key, value in os.environ.items()
           if not key.startswith("GIT_")}
    env.update(GIT_OPTIONAL_LOCKS="0", GIT_NO_REPLACE_OBJECTS="1", LC_ALL="C")
    return env


def _git(root: pathlib.Path, *args: str, binary: bool = False,
         stdin: bytes | None = None) -> Any:
    """Run one read-only git command; any failure is unusable input."""
    command = ["git", "--literal-pathspecs", "-C", str(root), *args]
    try:
        proc = subprocess.run(
            command,
            input=stdin,
            capture_output=True,
            env=_git_env(),
            timeout=60,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise GateInputError(f"cannot run {' '.join(command)}: {exc}") from exc
    if proc.returncode != 0:
        detail = proc.stderr.decode("utf-8", "replace").strip()
        raise GateInputError(f"git {' '.join(args)} failed: {detail or 'exit %d' % proc.returncode}")
    return proc.stdout if binary else proc.stdout.decode("utf-8", "replace")


def _repo_root(start: pathlib.Path) -> pathlib.Path:
    start = start.resolve()
    if start.is_file():
        start = start.parent
    try:
        top = _git(start, "rev-parse", "--show-toplevel").strip()
    except GateInputError as exc:
        raise GateInputError(f"{start} is not inside a Git repository: {exc}") from exc
    if not top:
        raise GateInputError(f"{start} is not inside a Git repository")
    return pathlib.Path(top)


def _safe_relpath(path: Any) -> str:
    """Normalize a repo-relative path and refuse escapes."""
    if not isinstance(path, str) or not path.strip():
        raise GateInputError(f"invalid path {path!r}: expected a non-empty string")
    text = path.strip().replace("\\", "/")
    while text.startswith("./"):
        text = text[2:]
    if text.startswith("/") or re.match(r"^[A-Za-z]:/", text):
        raise GateInputError(f"invalid path {path!r}: must be repo-relative")
    parts = text.split("/")
    if any(part in ("", ".", "..") for part in parts):
        raise GateInputError(f"invalid path {path!r}: empty, '.' or '..' component")
    return text


def resolve_commit(root: pathlib.Path, rev: str) -> str:
    """Resolve any rev to a full commit sha; refuse anything that is not one."""
    if not isinstance(rev, str) or not rev.strip():
        raise GateInputError("baseline_commit is empty; worktree evaluation is forbidden")
    rev = rev.strip()
    if rev.startswith("-") or "\n" in rev or "\x00" in rev:
        raise GateInputError(f"baseline_commit {rev!r} is not a valid revision name")
    try:
        resolved = _git(root, "rev-parse", "--verify", f"{rev}^{{commit}}").strip()
        kind = _git(root, "cat-file", "-t", resolved).strip()
    except GateInputError as exc:
        raise GateInputError(
            f"baseline_commit {rev!r} does not resolve to a commit in {root}: {exc}"
        ) from exc
    if kind != "commit" or not resolved:
        raise GateInputError(f"baseline_commit {rev!r} resolves to {kind!r}, not a commit")
    return resolved


def _glob_segments(pattern: str) -> tuple[str, ...]:
    """Validate a repo glob and return its segments.

    `*` and `?` are matched per path segment by `fnmatch.fnmatchcase`, so they
    can never cross a `/`; a whole-segment `**` matches zero or more segments.
    This is deliberately not `fnmatch.fnmatch` on the full path, whose `*`
    would let `corpus/*/*.md` match arbitrary depth.  Absolute paths and `..`
    are rejected.
    """
    if not isinstance(pattern, str) or not pattern.strip():
        raise GateInputError(f"invalid glob {pattern!r}: expected a non-empty string")
    text = pattern.strip()
    if text.startswith("/") or re.match(r"^[A-Za-z]:/", text):
        raise GateInputError(f"invalid glob {pattern!r}: must be repo-relative")
    segments = text.split("/")
    if any(seg in ("", ".", "..") for seg in segments):
        raise GateInputError(f"invalid glob {pattern!r}: empty, '.' or '..' segment")
    return tuple(segments)


_SEGMENT_CACHE: dict[str, tuple[str, ...]] = {}


def _segments(pattern: str) -> tuple[str, ...]:
    cached = _SEGMENT_CACHE.get(pattern)
    if cached is None:
        cached = _glob_segments(pattern)
        _SEGMENT_CACHE[pattern] = cached
    return cached


def _match_segments(pattern: tuple[str, ...], path: tuple[str, ...]) -> bool:
    if not pattern:
        return not path
    head = pattern[0]
    if head == "**":
        if len(pattern) == 1:
            return True
        return any(
            _match_segments(pattern[1:], path[index:])
            for index in range(len(path) + 1)
        )
    if not path:
        return False
    if not fnmatch.fnmatchcase(path[0], head):
        return False
    return _match_segments(pattern[1:], path[1:])


def glob_match(pattern: str, path: str) -> bool:
    return _match_segments(_segments(pattern), tuple(path.split("/")))


@dataclass(frozen=True)
class Check:
    """One declared premise clause and the probe that re-derives it."""

    clause: str
    probe_kind: str
    target: Mapping[str, Any]
    expect: bool
    evidence_command: str | None
    expect_source: str  # "declared" | "implied"

    def as_dict(self) -> dict[str, Any]:
        return {
            "clause": self.clause,
            "probe_kind": self.probe_kind,
            "target": dict(self.target),
            "expect": self.expect,
            "evidence_command": self.evidence_command,
            "expect_source": self.expect_source,
        }


@dataclass(frozen=True)
class Claim:
    id: str
    axis: str
    text: str
    before: str
    after_required: str
    checks: tuple[Check, ...]
    checks_field: str | None  # "before_checks" | "freshness_probes" | None
    raw: Mapping[str, Any]

    @property
    def has_declared_checks(self) -> bool:
        return bool(self.checks)


@dataclass(frozen=True)
class ClaimsDoc:
    path: pathlib.Path
    round: int
    baseline_input: str
    claims: tuple[Claim, ...]
    raw: Mapping[str, Any]


def _check_entry(entry: Any, index: int, where: str) -> Check:
    if not isinstance(entry, dict):
        raise GateInputError(f"{where}: before_checks[{index}] is not an object")
    clause = entry.get("clause")
    if not isinstance(clause, str) or not clause.strip():
        raise GateInputError(f"{where}: before_checks[{index}] has no non-empty `clause`")
    kind = entry.get("probe_kind")
    if kind not in PROBE_KINDS:
        raise GateInputError(
            f"{where}: before_checks[{index}] probe_kind {kind!r} is not in the closed "
            f"vocabulary {sorted(PROBE_KINDS)}"
        )
    target = entry.get("target", {})
    if not isinstance(target, dict):
        raise GateInputError(f"{where}: before_checks[{index}] target is not an object")
    if "expect" not in entry:
        raise GateInputError(
            f"{where}: before_checks[{index}] has no `expect` polarity; an undeclared "
            "polarity is malformed, not assumed true"
        )
    expect = entry["expect"]
    if not isinstance(expect, bool):
        raise GateInputError(f"{where}: before_checks[{index}] expect is not boolean")
    evidence = entry.get("evidence_command")
    if evidence is not None and not isinstance(evidence, str):
        raise GateInputError(f"{where}: before_checks[{index}] evidence_command is not a string")
    return Check(
        clause=clause.strip(),
        probe_kind=kind,
        target=MappingProxyType(dict(target)),
        expect=expect,
        evidence_command=evidence,
        expect_source="declared",
    )


def _legacy_probe(entry: Any, index: int, where: str) -> Check:
    if not isinstance(entry, dict):
        raise GateInputError(f"{where}: freshness_probes[{index}] is not an object")
    kind = entry.get("kind")
    if kind not in PROBE_KINDS:
        raise GateInputError(
            f"{where}: freshness_probes[{index}] kind {kind!r} is not in the closed "
            f"vocabulary {sorted(PROBE_KINDS)}"
        )
    target = {key: value for key, value in entry.items() if key != "kind"}
    return Check(
        clause=f"freshness_probes[{index}]",
        probe_kind=kind,
        target=MappingProxyType(target),
        expect=True,
        evidence_command=None,
        expect_source="implied",
    )


def load_claims(path: str | pathlib.Path) -> ClaimsDoc:
    """Parse and validate a claims file.  Never touches Git or the worktree."""
    source = pathlib.Path(path)
    try:
        text = source.read_text(encoding="utf-8")
    except OSError as exc:
        raise GateInputError(f"cannot read claims file {source}: {exc}") from exc
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise GateInputError(
            f"{source}: invalid JSON at line {exc.lineno} column {exc.colno}: {exc.msg}"
        ) from exc
    if not isinstance(data, dict):
        raise GateInputError(f"{source}: top level is not a JSON object")

    round_no = data.get("round")
    if isinstance(round_no, bool) or not isinstance(round_no, int) or round_no < 1:
        raise GateInputError(f"{source}: `round` must be an integer >= 1")

    baseline = data.get("baseline_commit")
    if not isinstance(baseline, str) or not baseline.strip():
        raise GateInputError(
            f"{source}: no baseline_commit; a claim premise cannot be evaluated "
            "without the commit it describes (worktree evaluation is forbidden)"
        )

    raw_claims = data.get("claims")
    if not isinstance(raw_claims, list) or not raw_claims:
        raise GateInputError(f"{source}: `claims` must be a non-empty list")

    claims: list[Claim] = []
    seen: set[str] = set()
    for index, raw in enumerate(raw_claims):
        where = f"{source}: claims[{index}]"
        if not isinstance(raw, dict):
            raise GateInputError(f"{where} is not an object")
        claim_id = raw.get("id")
        if not isinstance(claim_id, str) or not claim_id.strip():
            raise GateInputError(f"{where} has no non-empty `id`")
        claim_id = claim_id.strip()
        if claim_id in seen:
            raise GateInputError(f"{where}: duplicate claim id {claim_id!r}")
        seen.add(claim_id)
        axis = raw.get("axis")
        if not isinstance(axis, str) or not axis.strip():
            raise GateInputError(f"{where}: claim {claim_id} has no non-empty `axis`")
        before = raw.get("before")
        if not isinstance(before, str) or not before.strip():
            raise GateInputError(f"{where}: claim {claim_id} has no non-empty `before`")
        after = raw.get("after_required", "")
        if not isinstance(after, str):
            raise GateInputError(f"{where}: claim {claim_id} `after_required` is not a string")

        has_checks = "before_checks" in raw
        has_legacy = "freshness_probes" in raw
        if has_checks and has_legacy:
            raise GateInputError(
                f"{where}: claim {claim_id} declares both `before_checks` and "
                "`freshness_probes`; declare exactly one"
            )
        checks: tuple[Check, ...] = ()
        field: str | None = None
        if has_checks:
            entries = raw["before_checks"]
            if not isinstance(entries, list):
                raise GateInputError(f"{where}: `before_checks` is not a list")
            checks = tuple(_check_entry(entry, j, where) for j, entry in enumerate(entries))
            field = "before_checks"
        elif has_legacy:
            entries = raw["freshness_probes"]
            if not isinstance(entries, list):
                raise GateInputError(f"{where}: `freshness_probes` is not a list")
            checks = tuple(_legacy_probe(entry, j, where) for j, entry in enumerate(entries))
            field = "freshness_probes"

        claims.append(
            Claim(
                id=claim_id,
                axis=axis.strip(),
                text=raw.get("claim", "") if isinstance(raw.get("claim", ""), str) else "",
                before=before.strip(),
                after_required=after.strip(),
                checks=checks,
                checks_field=field,
                raw=MappingProxyType(dict(raw)),
            )
        )

    return ClaimsDoc(
        path=source,
        round=round_no,
        baseline_input=baseline.strip(),
        claims=tuple(claims),
        raw=MappingProxyType(dict(data)),
    )


class Baseline:
    """Read-only view of one commit.  The worktree is unreachable by design."""

    scope = "baseline"

    def __init__(self, root: str | pathlib.Path, commit_input: str):
        self.root = _repo_root(pathlib.Path(root))
        self.commit_input = str(commit_input).strip()
        self.commit = resolve_commit(self.root, self.commit_input)
        self.tree = _git(self.root, "rev-parse", "--verify", f"{self.commit}^{{tree}}").strip()
        self.short = self.commit[:7]
        self._entries: dict[str, tuple[str, str]] | None = None
        self._bytes: dict[str, bytes] = {}
        self._text: dict[str, str] = {}

    def __repr__(self) -> str:
        return f"Baseline({self.root}, {self.commit_input} -> {self.short})"

    def _index(self) -> dict[str, tuple[str, str]]:
        if self._entries is None:
            raw = _git(self.root, "ls-tree", "-r", "-z", "--full-tree", self.commit, binary=True)
            entries: dict[str, tuple[str, str]] = {}
            for record in raw.split(b"\x00"):
                if not record:
                    continue
                try:
                    meta, path_bytes = record.split(b"\t", 1)
                    mode, kind, oid = meta.decode("ascii").split(" ")
                except (ValueError, UnicodeDecodeError) as exc:
                    raise GateInputError(f"cannot parse ls-tree record {record!r}") from exc
                if kind != "blob":
                    continue
                path = path_bytes.decode("utf-8", "surrogateescape")
                entries[path] = (mode, oid)
            self._entries = entries
        return self._entries

    def files(self, prefix: str | None = None) -> tuple[str, ...]:
        paths = sorted(self._index())
        if prefix is not None:
            prefix = prefix.rstrip("/") + "/"
            paths = [path for path in paths if path.startswith(prefix)]
        return tuple(paths)

    def file_count(self, prefix: str | None = None) -> int:
        return len(self.files(prefix))

    def exists(self, path: str) -> bool:
        return _safe_relpath(path) in self._index()

    def _oid(self, path: str) -> str:
        key = _safe_relpath(path)
        entry = self._index().get(key)
        if entry is None:
            raise GateInputError(f"{key}: not present at baseline {self.short}")
        return entry[1]

    def warm(self, paths: Iterable[str]) -> None:
        """Batch-load blob bytes through one `git cat-file --batch` call."""
        wanted = [path for path in (_safe_relpath(p) for p in paths) if path not in self._bytes]
        if not wanted:
            return
        oids = [self._oid(path) for path in wanted]
        payload = ("\n".join(oids) + "\n").encode("ascii")
        out = _git(self.root, "cat-file", "--batch", binary=True, stdin=payload)
        position = 0
        for oid, path in zip(oids, wanted):
            newline = out.find(b"\n", position)
            if newline < 0:
                raise GateInputError(f"truncated cat-file output at {path}")
            header = out[position:newline].decode("ascii", "replace").split(" ")
            if len(header) != 3 or header[1] != "blob":
                raise GateInputError(f"{path}: cat-file returned {header!r}, not a blob")
            size = int(header[2])
            start = newline + 1
            data = out[start:start + size]
            if len(data) != size:
                raise GateInputError(f"{path}: truncated blob at baseline {self.short}")
            self._bytes[path] = data
            position = start + size + 1

    def read_bytes(self, path: str) -> bytes:
        key = _safe_relpath(path)
        if key not in self._bytes:
            self.warm([key])
        return self._bytes[key]

    def read(self, path: str) -> str:
        key = _safe_relpath(path)
        if key not in self._text:
            self._text[key] = self.read_bytes(key).decode("utf-8", "replace")
        return self._text[key]

    def sha256(self, path: str) -> str:
        return hashlib.sha256(self.read_bytes(path)).hexdigest()

    def glob(self, pattern: str) -> tuple[str, ...]:
        _segments(pattern)  # validate early
        return tuple(path for path in self.files() if glob_match(pattern, path))

    def grep(
        self,
        pattern: str,
        glob_pattern: str,
        max_lines: int = 0,
        limit: int = 0,
    ) -> tuple[tuple[str, int, str], ...]:
        try:
            regex = re.compile(pattern)
        except re.error as exc:
            raise GateInputError(f"invalid grep regex {pattern!r}: {exc}") from exc
        if max_lines < 0 or limit < 0:
            raise GateInputError("grep max_lines/limit must be >= 0")
        paths = self.glob(glob_pattern)
        self.warm(paths)
        hits: list[tuple[str, int, str]] = []
        for path in paths:
            for number, line in enumerate(self.read(path).splitlines(), 1):
                if max_lines and number > max_lines:
                    break
                if regex.search(line):
                    hits.append((path, number, line))
                    if limit and len(hits) >= limit:
                        return tuple(hits)
        return tuple(hits)

    def provenance(self) -> dict[str, str]:
        return {
            "scope": self.scope,
            "repo": str(self.root),
            "commit_input": self.commit_input,
            "commit": self.commit,
            "short": self.short,
            "tree": self.tree,
        }


def open_baseline(repo_root: str | pathlib.Path, commit_input: str) -> Baseline:
    return Baseline(repo_root, commit_input)


def open_claims(
    path: str | pathlib.Path,
    at: str | None = None,
    repo_root: str | pathlib.Path | None = None,
) -> tuple[ClaimsDoc, Baseline, dict[str, str] | None]:
    """Parse a claims file and open its baseline (or an explicit `at` commit).

    Returns (doc, baseline, deviation).  `deviation` is non-None only when the
    caller overrode the declared baseline; part 3 must print it.  There is no
    worktree path: a missing baseline raises GateInputError.
    """
    doc = load_claims(path)
    root = pathlib.Path(repo_root) if repo_root is not None else _repo_root(pathlib.Path(path))
    used = at.strip() if isinstance(at, str) and at.strip() else doc.baseline_input
    deviation = None
    if at is not None and used != doc.baseline_input:
        deviation = {
            "declared": doc.baseline_input,
            "used": used,
            "reason": "--at override (measurement is still a committed tree, never the worktree)",
        }
    baseline = Baseline(root, used)
    return doc, baseline, deviation


def describe(doc: ClaimsDoc, baseline: Baseline,
             deviation: Mapping[str, str] | None = None) -> dict[str, Any]:
    """JSON-safe provenance block for part 3's report."""
    return {
        "tool": TOOL,
        "version": VERSION,
        "claims_file": str(doc.path),
        "round": doc.round,
        "baseline": baseline.provenance(),
        "deviation": dict(deviation) if deviation else None,
        "claims": [
            {
                "id": claim.id,
                "axis": claim.axis,
                "checks_field": claim.checks_field,
                "declared_checks": len(claim.checks),
                "probe_kinds": [check.probe_kind for check in claim.checks],
                "expect_sources": sorted({check.expect_source for check in claim.checks}),
            }
            for claim in doc.claims
        ],
    }
```

## 9. Limits and to-verify

- **No CLI yet.** Part 1 cannot be run as a command; the assembly with parts 2/3 is required
  before `python3 tools/harness/claims-freshness.py --selftest` exists. The evidence here is
  import-level plus the scratch adapter, not the durable CLI. Parts 2/3 were absent at this
  cut, so the three parts have not been concatenated yet — `to-verify` by the integrator.
- **The adapter is not the registry.** Its handlers are deliberately one-line and live in
  `.scratch/o01-r47/interface_demo.py`; O02 must not mistake them for the durable probe
  implementation, and O05's r43 demo must use the assembled registry.
- **Git object-format assumption.** `cat-file --batch` header parsing splits on spaces and
  reads the size, so it should be agnostic to SHA-1 vs SHA-256 object ids, but this repo is
  SHA-1 and no SHA-256 clone was tested (`to-verify`).
- **Python floor.** The module uses `X | None` syntax and `from __future__ import
  annotations`; it parses on 3.10+. Only 3.14.7 was exercised here.
- **Tripwire, not a theorem prover.** The gate can only check declared clauses. A `before`
  whose premise is not expressible as one of the seven kinds remains could-not-evaluate and
  must not be reported as fresh. The r44 R01 §4.3 could-not-evaluate rule is preserved.
- **Performance measured on this host only**; `cat-file --batch` avoids one process per file,
  but no large-repo benchmark exists.

## 10. Ledger

Writes:

- `reports/round-47/op/O01-tool-core.md` — this file (durable deliverable).
- `.scratch/o01/core_part1.py` — the tested source of the fenced block (scratch only).
- `.scratch/o01-r47/check_core.py`, `selftest.out`, `interface_demo.py` — the suite and its
  transcript (scratch only; not cited as durable evidence).

Commands run: `git rev-parse`, `git ls-tree`, `git show`, `git cat-file`, `git status`,
`sha256sum`, `stat`, `python3 -B` on the core and the two scratch scripts. No commit, no
push, no install, no network. No filed byte edited; nothing staged under `corpus/`; no
round runner executed; `declared-in-r7` untouched. `git status --porcelain` at cut shows
only `?? reports/round-47/` and the pre-existing `?? reports/round-46/review/`.
