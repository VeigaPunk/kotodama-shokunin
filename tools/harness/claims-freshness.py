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

# =============================================================================
# Part 3/3 -- verdict + exit contract        (r47 claim O; defect R01-43-12)
# =============================================================================
# Integration seam.  This block is pure decision algebra and imports neither
# git nor the probe registry:
#
#   part 1 (core)   load_claims(path) -> (header, claims)
#                   resolve_baseline(ref) -> 40-hex sha
#   part 2 (probes) validate_check(check, claim_id, index) -> list[str]
#                   evaluate_check(check, baseline) -> ClauseResult
#   part 3 (this)   judge_claim / run_verdict / build_report / render_human
#
# ClauseResult is duck-typed: a mapping or object carrying
#   status    HOLDS | CONTRADICTED | NOT_EVALUATED
#   measured  value re-derived at baseline_commit
#   expected  value declared by the claim (the polarity)
#   reason    required prose for NOT_EVALUATED
# Any other status is an evaluator contract violation and is downgraded to
# NOT_EVALUATED -- never to HOLDS.
# =============================================================================


import hashlib
import json
import math

FRESH = "fresh"
STALE = "stale"
COULD_NOT_EVALUATE = "could-not-evaluate"
MALFORMED = "malformed"

EXIT_FRESH = 0
EXIT_STALE = 1
EXIT_MALFORMED = 2
EXIT_NOT_EVALUATED = 3

EXIT_BY_VERDICT = {
    FRESH: EXIT_FRESH,
    STALE: EXIT_STALE,
    MALFORMED: EXIT_MALFORMED,
    COULD_NOT_EVALUATE: EXIT_NOT_EVALUATED,
}

# Precedence, low to high.  A malformed file cannot yield a trustworthy
# verdict at all; a measured contradiction outranks "not evaluated"; an
# unevaluated claim outranks "fresh".
_RANK = {FRESH: 0, COULD_NOT_EVALUATE: 1, STALE: 2, MALFORMED: 3}

REPORT_SCHEMA = "kotodama-claims-freshness-report-v1"

_CLAUSE_STATUS = ("HOLDS", "CONTRADICTED", "NOT_EVALUATED")


def _get(obj, name, default=None):
    if isinstance(obj, dict):
        return obj.get(name, default)
    return getattr(obj, name, default)


def _clip(text, limit=240):
    text = " ".join(str(text or "").split())
    return text if len(text) <= limit else text[: limit - 1] + "\u2026"


def json_safe(value):
    """Deterministic JSON projection.  Raises TypeError on foreign objects."""
    if value is None or isinstance(value, (bool, int, str)):
        return value
    if isinstance(value, float):
        if not math.isfinite(value):
            raise TypeError("non-finite float is not strict JSON: %r" % value)
        return value
    if isinstance(value, (list, tuple)):
        return [json_safe(item) for item in value]
    if isinstance(value, (set, frozenset)):
        return [json_safe(item) for item in sorted(value, key=repr)]
    if isinstance(value, dict):
        return {
            str(key): json_safe(value[key])
            for key in sorted(value, key=lambda k: str(k))
        }
    raise TypeError("not JSON-serialisable: %s" % type(value).__name__)


def normalise_clause_result(result):
    """(status, measured, expected, reason) with status in _CLAUSE_STATUS."""
    status = _get(result, "status", "")
    status = status.strip().upper() if isinstance(status, str) else ""
    measured = _get(result, "measured")
    expected = _get(result, "expected")
    reason = _get(result, "reason", "") or ""
    if status not in _CLAUSE_STATUS:
        return (
            "NOT_EVALUATED",
            measured,
            expected,
            "evaluator-contract-violation: status %r is not one of %s"
            % (status, "/".join(_CLAUSE_STATUS)),
        )
    if status == "NOT_EVALUATED" and not reason:
        reason = "not-evaluated: probe supplied no reason"
    return status, measured, expected, reason


def _target_text(check):
    if not isinstance(check, dict):
        return ""
    target = check.get("target", check.get("path", check.get("glob", "")))
    try:
        return _clip(json.dumps(target, sort_keys=True))
    except (TypeError, ValueError):
        return _clip(target)


def clause_row(index, check, result):
    """One auditable row; measured/expected are JSON-safe or NOT_EVALUATED."""
    status, measured, expected, reason = normalise_clause_result(result)
    check = check if isinstance(check, dict) else {}
    try:
        measured = json_safe(measured)
        expected = json_safe(expected)
    except TypeError as exc:
        status = "NOT_EVALUATED"
        reason = ("%s; " % reason if reason else "") + str(exc)
        measured, expected = None, None
    return {
        "index": index,
        "clause": _clip(check.get("clause", "")),
        "probe": str(
            check.get("probe", check.get("probe_kind", check.get("kind", "?")))
        ),
        "target": _target_text(check),
        "status": status,
        "expected": expected,
        "measured": measured,
        "reason": _clip(reason, 400),
        "evidence": _clip(check.get("evidence", "")),
    }


def judge_claim(
    claim_id,
    checks,
    results=None,
    *,
    axis=None,
    before="",
    schema_errors=(),
    owner=None,
):
    """Return the per-claim verdict row.

    Rules, in order:
      * any schema error or a missing/blank `before` -> MALFORMED
      * zero declared checks                         -> COULD_NOT_EVALUATE
      * any CONTRADICTED clause                      -> STALE
      * any NOT_EVALUATED clause                     -> COULD_NOT_EVALUATE
      * every clause HOLDS                           -> FRESH
    """
    checks = list(checks or [])
    results = list(results or [])
    errors = [str(err) for err in (schema_errors or [])]
    if not isinstance(claim_id, str) or not claim_id.strip():
        errors.append("claim id is missing or not a string")
    if not isinstance(before, str) or not before.strip():
        errors.append("claim has no non-empty `before` assertion")
    if errors:
        return {
            "id": claim_id,
            "axis": axis,
            "before": before,
            "owner": owner or claim_id,
            "verdict": MALFORMED,
            "checks_declared": len(checks),
            "checks_evaluated": 0,
            "counts": {"holds": 0, "contradicted": 0, "not_evaluated": 0},
            "clauses": [],
            "failing_clauses": [],
            "not_evaluated_clauses": [],
            "errors": errors,
        }

    if not checks:
        return {
            "id": claim_id,
            "axis": axis,
            "before": before,
            "owner": owner or claim_id,
            "verdict": COULD_NOT_EVALUATE,
            "checks_declared": 0,
            "checks_evaluated": 0,
            "counts": {"holds": 0, "contradicted": 0, "not_evaluated": 0},
            "clauses": [],
            "failing_clauses": [],
            "not_evaluated_clauses": [],
            "unevaluated_reason": (
                "no before_checks declared; a claim with no declared checks "
                "is not fresh"
            ),
            "errors": [],
        }

    if len(results) > len(checks):
        return {
            "id": claim_id,
            "axis": axis,
            "before": before,
            "owner": owner or claim_id,
            "verdict": COULD_NOT_EVALUATE,
            "checks_declared": len(checks),
            "checks_evaluated": 0,
            "counts": {"holds": 0, "contradicted": 0, "not_evaluated": len(checks)},
            "clauses": [],
            "failing_clauses": [],
            "not_evaluated_clauses": [],
            "unevaluated_reason": (
                "result-count-exceeds-checks: %d results for %d checks"
                % (len(results), len(checks))
            ),
            "errors": [],
        }

    rows = []
    for index, check in enumerate(checks):
        if index < len(results):
            rows.append(clause_row(index, check, results[index]))
        else:
            rows.append(
                clause_row(
                    index,
                    check,
                    {
                        "status": "NOT_EVALUATED",
                        "reason": "not-run: the harness returned no result",
                    },
                )
            )

    failing = [row for row in rows if row["status"] == "CONTRADICTED"]
    unevaluated = [row for row in rows if row["status"] == "NOT_EVALUATED"]
    holds = [row for row in rows if row["status"] == "HOLDS"]

    if failing:
        verdict = STALE
    elif unevaluated:
        verdict = COULD_NOT_EVALUATE
    else:
        verdict = FRESH

    row = {
        "id": claim_id,
        "axis": axis,
        "before": before,
        "owner": owner or claim_id,
        "verdict": verdict,
        "checks_declared": len(checks),
        "checks_evaluated": min(len(results), len(checks)),
        "counts": {
            "holds": len(holds),
            "contradicted": len(failing),
            "not_evaluated": len(unevaluated),
        },
        "clauses": rows,
        "failing_clauses": failing,
        "not_evaluated_clauses": unevaluated,
        "errors": [],
    }
    if verdict == COULD_NOT_EVALUATE:
        row["unevaluated_reason"] = (
            "%d of %d declared clauses not evaluated"
            % (len(unevaluated), len(checks))
        )
    return row


def run_verdict(claim_rows):
    """Aggregate per-claim verdicts; malformed > stale > unevaluated > fresh."""
    rows = list(claim_rows or [])
    if not rows:
        return MALFORMED
    return max((row["verdict"] for row in rows), key=_RANK.__getitem__)


def exit_code(verdict):
    try:
        return EXIT_BY_VERDICT[verdict]
    except KeyError:
        raise ValueError("unknown verdict: %r" % (verdict,))


def _refusal(verdict, rows, baseline_commit, errors=()):
    at = baseline_commit or "unresolved baseline"
    if verdict == FRESH:
        return None
    if verdict == MALFORMED:
        bad = [row["id"] for row in rows if row["verdict"] == MALFORMED]
        subject = "claim(s) %s are" % ", ".join(map(str, bad)) if bad else "input is"
        detail = "; ".join(str(err) for err in errors[:3])
        suffix = (": " + detail) if detail else ""
        return (
            "REFUSE: %s malformed at %s%s; exit 2 -- no freshness verdict is "
            "possible." % (subject, at, suffix)
        )
    if verdict == STALE:
        stale = [row["id"] for row in rows if row["verdict"] == STALE]
        text = (
            "REFUSE: claim(s) %s have a `before` already false at %s; "
            "do not dispatch." % (", ".join(map(str, stale)), at)
        )
        stuck = [row["id"] for row in rows if row["verdict"] == COULD_NOT_EVALUATE]
        if stuck:
            text += (
                " Claim(s) %s could not be evaluated either."
                % ", ".join(map(str, stuck))
            )
        return text
    stuck = [row["id"] for row in rows if row["verdict"] == COULD_NOT_EVALUATE]
    return (
        "REFUSE: claim(s) %s could not be evaluated at %s (no declared checks "
        "or probe failure); absence of a verdict is not freshness."
        % (", ".join(map(str, stuck)), at)
    )


def _summary(rows, errors=()):
    summary = {
        "claims": len(rows),
        "fresh": 0,
        "stale": 0,
        "could_not_evaluate": 0,
        "malformed": 0,
        "clauses": 0,
        "holds": 0,
        "contradicted": 0,
        "not_evaluated": 0,
        "document_errors": len(errors),
    }
    for row in rows:
        key = row["verdict"].replace("-", "_")
        if key in summary:
            summary[key] += 1
        counts = row.get("counts", {})
        summary["clauses"] += row.get("checks_declared", 0)
        summary["holds"] += counts.get("holds", 0)
        summary["contradicted"] += counts.get("contradicted", 0)
        summary["not_evaluated"] += counts.get("not_evaluated", 0)
    return summary


def _decision_digest(report):
    body = {key: value for key, value in report.items() if key != "decision_sha256"}
    canonical = json.dumps(
        body, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    )
    return hashlib.sha256(canonical.encode("utf-8")).hexdigest()


def build_report(
    claim_rows,
    *,
    round_id=None,
    baseline_commit=None,
    baseline_sha=None,
    document_errors=(),
):
    """Assemble the machine-readable report from per-claim verdict rows."""
    rows = list(claim_rows or [])
    errors = [str(err) for err in (document_errors or [])]

    seen = set()
    for row in rows:
        claim_id = row.get("id")
        if claim_id in seen:
            errors.append("duplicate claim id: %s" % claim_id)
        seen.add(claim_id)

    if baseline_sha is not None and (
        not isinstance(baseline_sha, str)
        or len(baseline_sha) != 40
        or any(ch not in "0123456789abcdef" for ch in baseline_sha)
    ):
        errors.append(
            "baseline_sha is not a 40-hex commit id: %r" % (baseline_sha,)
        )

    verdict = run_verdict(rows)
    if errors:
        verdict = MALFORMED

    report = {
        "schema": REPORT_SCHEMA,
        "round": round_id,
        "baseline_commit": baseline_commit,
        "baseline_sha": baseline_sha,
        "run_verdict": verdict,
        "exit_code": exit_code(verdict),
        "refuse": verdict != FRESH,
        "refusal": _refusal(verdict, rows, baseline_commit, errors),
        "summary": _summary(rows, errors),
        "claims": rows,
        "errors": errors,
    }
    report["decision_sha256"] = _decision_digest(report)
    return report


def malformed_report(reason, *, round_id=None, baseline_commit=None):
    """Uniform report for input that never reached claim evaluation (exit 2)."""
    return build_report(
        [],
        round_id=round_id,
        baseline_commit=baseline_commit,
        baseline_sha=None,
        document_errors=[reason],
    )


def render_human(report):
    lines = [
        "claims-freshness: round %s baseline %s (%s)"
        % (
            report.get("round"),
            report.get("baseline_commit") or "unresolved",
            report.get("baseline_sha") or "unresolved",
        )
    ]
    for row in report.get("claims", []):
        counts = row.get("counts", {})
        verdict = row["verdict"]
        if verdict == FRESH:
            detail = "%d/%d clauses hold" % (
                counts.get("holds", 0),
                row.get("checks_declared", 0),
            )
        elif verdict == STALE:
            detail = "%d/%d clauses contradict" % (
                counts.get("contradicted", 0),
                row.get("checks_declared", 0),
            )
        elif verdict == COULD_NOT_EVALUATE:
            detail = row.get("unevaluated_reason") or "%d clause(s) not evaluated" % (
                counts.get("not_evaluated", 0),
            )
        else:
            detail = "; ".join(row.get("errors", [])) or "malformed"
        lines.append("  [%s] %-17s %s" % (row.get("id"), verdict.upper(), detail))
        for clause in row.get("failing_clauses", []):
            lines.append(
                "      clause %d (%s): measured=%r expected=%r -- %s"
                % (
                    clause["index"],
                    clause["probe"],
                    clause["measured"],
                    clause["expected"],
                    clause["clause"],
                )
            )
        for clause in row.get("not_evaluated_clauses", []):
            lines.append(
                "      clause %d (%s) NOT EVALUATED: %s"
                % (clause["index"], clause["probe"], clause["reason"])
            )
    summary = report.get("summary", {})
    text = (
        "summary: %d fresh, %d stale, %d could-not-evaluate, %d malformed; "
        "clauses %d (%d hold, %d contradict, %d not evaluated)"
        % (
            summary.get("fresh", 0),
            summary.get("stale", 0),
            summary.get("could_not_evaluate", 0),
            summary.get("malformed", 0),
            summary.get("clauses", 0),
            summary.get("holds", 0),
            summary.get("contradicted", 0),
            summary.get("not_evaluated", 0),
        )
    )
    if summary.get("document_errors"):
        text += "; %d document error(s)" % summary["document_errors"]
    lines.append(text)
    for error in report.get("errors", []):
        lines.append("error: %s" % error)
    if report.get("refusal"):
        lines.append(report["refusal"])
    lines.append("exit %d" % report["exit_code"])
    return "\n".join(lines)

# W01-SEAM-BEGIN
# =============================================================================
# Part 4/4 -- landing seam: document loader, compatibility target encodings,
# evaluation bridge, CLI and control set.  (r47 W01 landing spec)
# =============================================================================
# Why this block exists (measured, not stylistic):
#
#   1. Part 1's `load_claims` types every `expect` as a JSON boolean.  Part 2
#      requires an integer for `count_eq` and a 64-hex string for `sha256_eq`,
#      so a filed claims file with a count clause is rejected by part 1 before
#      part 2 can type it.  The loader below delegates every check's typing to
#      part 2's `validate_check`; part 1's `Check`/`Claim`/`load_claims` remain
#      importable but are not used by the CLI.
#   2. The filed demonstrations use three target encodings: canonical target
#      objects (part 2), string targets (O06/O10), and the O05 overlay
#      (`{"capability": ..., "scope": ...}` / `{"glob": ..., "value": ...}`).
#      `_coerce_check` normalizes all three to part 2's canonical schema before
#      validation.  The canonical object form is authoritative; the other two
#      are compatibility renderings, named in the landing spec.
#   3. Part 2 returns `{status: holds|mismatch|could-not-evaluate, measured,
#      expect}`; part 3's `judge_claim` expects
#      `{status: HOLDS|CONTRADICTED|NOT_EVALUATED, measured, expected}`.
#      `_bridge` is the one-way adapter.
#
# Nothing here names a round, a commit, a corpus entry or a tool.  The r43
# literals live only in the demo fixtures under reports/round-47/calib/.
# =============================================================================

import argparse

ALL_PARTITIONS = (
    "myth-symbol",
    "linguistics",
    "culture-material",
    "civilizations",
    "verification",
    "synthesis",
)

# Named capabilities available to compatibility targets.  The canonical form
# is part 2's behavioural target; this table is data, not prose inference.
# `couples_census` is the r39 basename-couples policy probe used by the r43
# demonstration: a candidate must parse the wrapped couples field and report
# four references (part 2's measured fixture, O02 section 5.2).
CAPABILITY_TARGETS = {
    "couples_census": {
        "globs": ["tools/harness/*.py"],
        "exclude_globs": ["tools/gates/frozen/**", "tools/harness/claims-freshness.py"],
        "argv": ["--census"],
        "fixture": {
            "corpus/knowledge/fixture/entry.md":
                "# Fixture entry\n\n- topic: fixture\n"
                "- couples: language \u2014 `sound-symbolism.md`, `writing-systems.md`; "
                "prospective\n  sibling files: sound-change.md, tone-\n  prosody.md\n"
        },
        "success_regex": r"refs=4\b",
        "timeout_s": 20,
        "max_candidates": 32,
    },
}


class Document:
    """Parsed claims file.  `checks` are already validated part-2 dicts."""

    def __init__(self, path, round_no, baseline_input, claims, raw):
        self.path = path
        self.round = round_no
        self.baseline_input = baseline_input
        self.claims = claims
        self.raw = raw


def _read_json_object(path):
    try:
        text = pathlib.Path(path).read_text(encoding="utf-8")
    except OSError as exc:
        raise GateInputError("cannot read %s: %s" % (path, exc)) from exc
    try:
        data = json.loads(text)
    except json.JSONDecodeError as exc:
        raise GateInputError(
            "%s: invalid JSON at line %d column %d: %s"
            % (path, exc.lineno, exc.colno, exc.msg)
        ) from exc
    if not isinstance(data, dict):
        raise GateInputError("%s: top level is not a JSON object" % path)
    return data, text


def _string_target(kind, target):
    """Compatibility form: a bare string target, normalized per probe kind."""
    text = target.strip()
    if kind in ("path_absent", "path_present", "sha256_eq"):
        return {"path": text}
    if kind == "count_eq":
        return {"glob": text}
    if kind == "grep_absent":
        path, sep, regex = text.partition("::")
        if not sep:
            raise CheckError("grep_absent string target must be <glob>::<regex>")
        return {"glob": path, "regex": regex}
    if kind == "topic_owner_absent":
        partition, sep, topic = text.partition(":")
        if sep:
            return {
                "topic": [topic],
                "partitions": [partition],
                "fields": ["h1", "topic", "gap filled"],
                "mode": "word",
            }
        return {
            "topic": [text],
            "partitions": list(ALL_PARTITIONS),
            "fields": ["h1", "topic", "gap filled"],
            "mode": "word",
        }
    raise CheckError("probe_kind %r has no string-target compatibility form" % kind)


def _coerce_check(raw):
    """Normalize the three filed encodings to part 2's canonical check dict."""
    if not isinstance(raw, dict):
        raise CheckError("check is not an object")
    check = dict(raw)
    if "probe_kind" not in check and "kind" in check:
        check["probe_kind"] = check.pop("kind")
    kind = check.get("probe_kind")
    target = check.get("target")

    if isinstance(target, str):
        if kind == "capability_present":
            path, sep, regex = target.partition("::")
            if not sep:
                raise CheckError(
                    "capability_present string target must be <path>::<regex>"
                )
            expect = check.get("expect")
            if not isinstance(expect, bool):
                raise CheckError("capability_present requires a boolean expect")
            check["probe_kind"] = "grep_absent"
            check["target"] = {"glob": path, "regex": regex}
            check["expect"] = not expect
        else:
            check["target"] = _string_target(kind, target)
        return check

    if not isinstance(target, dict):
        raise CheckError("target must be an object or a compatibility string")

    target = dict(target)
    if kind == "capability_present":
        if "capability" in target:
            name = target.pop("capability")
            spec = CAPABILITY_TARGETS.get(name)
            if spec is None:
                raise CheckError("unknown named capability %r" % (name,))
            check["target"] = dict(spec)
        elif "path" in target and "regex" in target:
            expect = check.get("expect")
            if not isinstance(expect, bool):
                raise CheckError("capability_present requires a boolean expect")
            check["probe_kind"] = "grep_absent"
            check["target"] = {"glob": target["path"], "regex": target["regex"]}
            check["expect"] = not expect
        return check

    if kind == "count_eq" and "value" in target:
        check["expect"] = target.pop("value")
        check["target"] = {"glob": target.get("glob")}
        return check

    if kind == "topic_owner_absent":
        topics = target.get("topic", target.get("topics"))
        if topics is None:
            raise CheckError("topic_owner_absent target has no topic(s)")
        partitions = target.get("partitions")
        if partitions is None:
            partitions = [target["partition"]] if "partition" in target else list(ALL_PARTITIONS)
        fields = target.get("fields", ["h1", "topic", "gap filled"])
        normalized_fields = []
        for field in fields:
            key = str(field).strip().lower()
            normalized_fields.append(key)
        check["target"] = {
            "topic": topics if isinstance(topics, list) else [topics],
            "partitions": partitions,
            "fields": normalized_fields,
            "mode": target.get("mode", "word"),
        }
        return check

    return check


def _load_check(raw, before, seen_ids, where):
    """Part-2 validation with the round's clause-label policy.

    O02 rejects a `clause` that is not a verbatim substring of `before`.
    The filed acceptance artifacts disagree: O06's negative control and
    O10's exit-conformance fixtures use descriptive labels ("no lithic
    owner", "the gap is unowned") that are not verbatim spans.  The
    measurement never depends on the label, so a non-verbatim clause is
    accepted as a *label* and recorded; a verbatim one is recorded as
    *verbatim*.  An empty clause is still malformed (part 2 enforces it).
    """
    try:
        coerced = _coerce_check(raw)
        clause = coerced.get("clause")
        normalized_before = " ".join(str(before).split())
        verbatim = (
            isinstance(clause, str)
            and " ".join(clause.split()).lower() in normalized_before.lower()
        )
        probe = coerced if verbatim else dict(coerced, clause=normalized_before)
        result = validate_check(probe, before, seen_ids)
        if not verbatim:
            result["clause"] = " ".join(str(clause).split())
            result["clause_match"] = "label"
        else:
            result["clause_match"] = "verbatim"
        return result
    except CheckError as exc:
        raise GateInputError("%s: %s" % (where, exc)) from exc


def load_document(path):
    """Parse a claims file; every check is typed by part 2."""
    data, _text = _read_json_object(path)
    round_no = data.get("round")
    if isinstance(round_no, bool) or not isinstance(round_no, int) or round_no < 1:
        raise GateInputError("%s: `round` must be an integer >= 1" % path)
    baseline = data.get("baseline_commit")
    if not isinstance(baseline, str) or not baseline.strip():
        raise GateInputError(
            "%s: no baseline_commit; worktree evaluation is forbidden" % path
        )
    raw_claims = data.get("claims")
    if not isinstance(raw_claims, list) or not raw_claims:
        raise GateInputError("%s: `claims` must be a non-empty list" % path)

    claims = []
    seen = set()
    for index, raw in enumerate(raw_claims):
        where = "%s: claims[%d]" % (path, index)
        if not isinstance(raw, dict):
            raise GateInputError("%s is not an object" % where)
        claim_id = raw.get("id")
        if not isinstance(claim_id, str) or not claim_id.strip():
            raise GateInputError("%s has no non-empty `id`" % where)
        claim_id = claim_id.strip()
        if claim_id in seen:
            raise GateInputError("%s: duplicate claim id %r" % (where, claim_id))
        seen.add(claim_id)
        axis = raw.get("axis")
        if not isinstance(axis, str) or not axis.strip():
            raise GateInputError("%s: claim %s has no non-empty `axis`" % (where, claim_id))
        before = raw.get("before")
        if not isinstance(before, str) or not before.strip():
            raise GateInputError("%s: claim %s has no non-empty `before`" % (where, claim_id))
        legacy = raw.get("freshness_probes")
        if legacy is not None:
            if not isinstance(legacy, list):
                raise GateInputError(
                    "%s: claim %s `freshness_probes` is not a list" % (where, claim_id)
                )
            if legacy:
                raise GateInputError(
                    "%s: claim %s declares non-empty `freshness_probes`; the legacy "
                    "entries carry no `clause`/`expect` polarity and are not accepted "
                    "-- declare before_checks" % (where, claim_id)
                )
            if "before_checks" in raw:
                raise GateInputError(
                    "%s: claim %s declares both `freshness_probes` and "
                    "`before_checks`; declare exactly one" % (where, claim_id)
                )
        raw_checks = raw.get("before_checks", [])
        if raw_checks is None:
            raw_checks = []
        if not isinstance(raw_checks, list):
            raise GateInputError("%s: claim %s `before_checks` is not a list" % (where, claim_id))
        check_ids = set()
        checks = [
            _load_check(entry, before, check_ids, "%s: before_checks[%d]" % (where, j))
            for j, entry in enumerate(raw_checks)
        ]
        claims.append(
            {
                "id": claim_id,
                "axis": axis.strip(),
                "before": before.strip(),
                "checks": checks,
            }
        )
    return Document(pathlib.Path(path), round_no, baseline.strip(), claims, data)


def load_overlay(path, document, baseline, claims_bytes):
    """Load an O05-shaped `--checks` overlay, pinned to the claims bytes."""
    data, _text = _read_json_object(path)
    rows = data.get("checks")
    if not isinstance(rows, dict) or not rows:
        raise GateInputError("%s: overlay has no non-empty `checks` object" % path)
    pinned = data.get("claims_sha256")
    if pinned is not None:
        actual = hashlib.sha256(claims_bytes).hexdigest()
        if pinned != actual:
            raise GateInputError(
                "%s: claims_sha256 %s does not match the claims file (%s)"
                % (path, pinned, actual)
            )
    overlay = {}
    known = {claim["id"]: claim for claim in document.claims}
    for claim_id, entries in rows.items():
        if claim_id not in known:
            raise GateInputError(
                "%s: overlay names claim %r, absent from the claims file" % (path, claim_id)
            )
        if not isinstance(entries, list):
            raise GateInputError("%s: overlay claim %s is not a list" % (path, claim_id))
        before = known[claim_id]["before"]
        check_ids = set()
        overlay[claim_id] = [
            _load_check(entry, before, check_ids,
                        "%s: checks[%s][%d]" % (path, claim_id, j))
            for j, entry in enumerate(entries)
        ]
    return overlay


_PROBE_STATUS = {
    "holds": "HOLDS",
    "mismatch": "CONTRADICTED",
    "could-not-evaluate": "NOT_EVALUATED",
}


def _bridge(result):
    status = _PROBE_STATUS.get(result.get("status"), "NOT_EVALUATED")
    reason = result.get("detail") or ""
    if status == "NOT_EVALUATED" and not reason:
        reason = "not-evaluated: probe supplied no reason"
    return {
        "status": status,
        "measured": result.get("measured"),
        "expected": result.get("expect"),
        "reason": reason,
    }


def _display_check(check):
    return {
        "clause": check["clause"],
        "probe_kind": check["probe_kind"],
        "target": check["target"],
        "evidence": check.get("evidence_command", ""),
    }


def evaluate_document(document, baseline, overlay=None, allow_exec=True):
    rows = []
    for claim in document.claims:
        if overlay is None:
            checks = claim["checks"]
        else:
            checks = overlay.get(claim["id"], [])
        results = [
            _bridge(evaluate_check(check, baseline, allow_exec=allow_exec))
            for check in checks
        ]
        rows.append(
            judge_claim(
                claim["id"],
                [_display_check(check) for check in checks],
                results,
                axis=claim["axis"],
                before=claim["before"],
            )
        )
    return rows


def _emit(report, as_json):
    if as_json:
        print(json.dumps(report, indent=2, sort_keys=True, ensure_ascii=False))
    else:
        print(render_human(report))


def run_cli(args):
    if args.selftest:
        return run_selftest(args.root)
    if not args.claims:
        print("claims-freshness: --claims is required (or --selftest)", file=sys.stderr)
        return EXIT_MALFORMED

    claims_path = pathlib.Path(args.claims)
    round_no = None
    declared = None
    try:
        claims_bytes = claims_path.read_bytes()
        document = load_document(claims_path)
        round_no = document.round
        declared = document.baseline_input
        root = _repo_root(pathlib.Path(args.root))
        used = args.at.strip() if isinstance(args.at, str) and args.at.strip() else declared
        baseline = Baseline(root, used)
        deviation = None
        if used != declared:
            deviation = {
                "declared": declared,
                "used": used,
                "reason": "--at override; measurement is still a committed tree, never the worktree",
            }
        overlay = (
            load_overlay(pathlib.Path(args.checks), document, baseline, claims_bytes)
            if args.checks else None
        )
        rows = evaluate_document(document, baseline, overlay, allow_exec=not args.no_exec)
        report = build_report(
            rows,
            round_id=round_no,
            baseline_commit=declared,
            baseline_sha=baseline.commit,
        )
        if deviation:
            report["deviation"] = deviation
        if deviation and report["exit_code"] == EXIT_FRESH:
            report["run_verdict"] = COULD_NOT_EVALUATE
            report["exit_code"] = EXIT_NOT_EVALUATED
            report["refuse"] = True
            report["refusal"] = (
                "REFUSE: --at override used; a fresh verdict under an override is "
                "not a dispatch license."
            )
    except GateInputError as exc:
        report = malformed_report(str(exc), round_id=round_no, baseline_commit=declared)
    _emit(report, args.json)
    return report["exit_code"]


# --- control set -----------------------------------------------------------

def run_selftest(root="."):
    print("== registry controls (part 2) ==")
    import contextlib
    import io

    buffer = io.StringIO()
    with contextlib.redirect_stdout(buffer):
        registry_rc = selftest_registry()
    registry_text = buffer.getvalue()
    sys.stdout.write(registry_text)
    match = re.search(r"PROBE-REGISTRY SELFTEST: (\d+)/(\d+)", registry_text)
    registry_count = "%s/%s" % match.groups() if match else "?"
    registry_ok = (
        registry_rc == 0
        and match is not None
        and match.group(1) == match.group(2)
    )
    head_sha = _git(_repo_root(pathlib.Path(root)), "rev-parse", "HEAD").strip()

    controls = []

    def check(name, condition, detail=""):
        controls.append((name, bool(condition)))
        if condition:
            print("PASS " + name)
        else:
            print("FAIL " + name + (("  [%s]" % detail) if detail else ""))

    import tempfile

    def write_temp(name, payload):
        directory = tempfile.mkdtemp(prefix="w01-selftest-", dir=os.environ.get("TMPDIR"))
        path = os.path.join(directory, name)
        with open(path, "w", encoding="utf-8") as handle:
            handle.write(payload)
        return path

    def fixture_doc(checks, before="fixture clause"):
        return json.dumps(
            {
                "round": 999,
                "baseline_commit": "HEAD",
                "claims": [{"id": "X", "axis": "operability", "before": before,
                            "before_checks": checks}],
            }
        )

    good_check = {
        "clause": "fixture clause",
        "probe_kind": "path_absent",
        "target": "tools/harness/never-there.py",
        "expect": True,
        "evidence_command": "git ls-tree -r --name-only HEAD",
    }

    # 1. loader
    path = write_temp("ok.json", fixture_doc([good_check]))
    document = load_document(path)
    check("1 loader parses a compatibility string target", len(document.claims) == 1)

    # 2. empty checks -> CNE, exit 3
    path = write_temp("empty.json", fixture_doc([]))
    document = load_document(path)
    row = judge_claim("X", [], [], axis="operability", before="fixture clause")
    report = build_report([row], round_id=999, baseline_commit="HEAD", baseline_sha=head_sha)
    check("2 empty before_checks -> could-not-evaluate, exit 3",
          row["verdict"] == COULD_NOT_EVALUATE and report["exit_code"] == 3)

    # 3. missing expect -> malformed
    broken = dict(good_check)
    broken.pop("expect")
    try:
        load_document(write_temp("no-expect.json", fixture_doc([broken])))
        check("3 missing expect -> malformed", False)
    except GateInputError:
        check("3 missing expect -> malformed", True)

    # 4. unknown kind -> malformed
    broken = dict(good_check, probe_kind="vibes_absent")
    try:
        load_document(write_temp("bad-kind.json", fixture_doc([broken])))
        check("4 unknown probe_kind -> malformed", False)
    except GateInputError:
        check("4 unknown probe_kind -> malformed", True)

    # 5. legacy schema refused
    legacy = {"round": 999, "baseline_commit": "HEAD", "claims": [
        {"id": "X", "axis": "operability", "before": "b",
         "freshness_probes": [{"kind": "path_absent", "path": "x"}]}]}
    try:
        load_document(write_temp("legacy.json", json.dumps(legacy)))
        check("5 non-empty legacy freshness_probes -> malformed", False)
    except GateInputError:
        check("5 non-empty legacy freshness_probes -> malformed", True)

    # 5b. empty legacy list = no declared checks, not a schema error
    empty_legacy = {"round": 999, "baseline_commit": "HEAD", "claims": [
        {"id": "X", "axis": "operability", "before": "b",
         "freshness_probes": []}]}
    empty_doc = load_document(write_temp("legacy-empty.json", json.dumps(empty_legacy)))
    check("5b empty legacy freshness_probes -> zero checks (CNE, not malformed)",
          empty_doc.claims[0]["checks"] == [])

    # 6. duplicate id -> malformed
    dup = json.loads(fixture_doc([good_check]))
    dup["claims"].append(dict(dup["claims"][0]))
    try:
        load_document(write_temp("dup.json", json.dumps(dup)))
        check("6 duplicate claim id -> malformed", False)
    except GateInputError:
        check("6 duplicate claim id -> malformed", True)

    # 7. count_eq compatibility target carries its integer
    count_doc = json.loads(fixture_doc([]))
    count_doc["claims"][0]["before_checks"] = [{
        "clause": "fixture clause",
        "probe_kind": "count_eq",
        "target": {"glob": "corpus/knowledge/*/*.md", "value": 2},
        "expect": True,
        "evidence_command": "git ls-tree -r --name-only HEAD -- corpus/knowledge",
    }]
    document = load_document(write_temp("count.json", json.dumps(count_doc)))
    tree = FixtureTree({"corpus/knowledge/a/one.md": "", "corpus/knowledge/b/two.md": ""})
    result = evaluate_check(document.claims[0]["checks"][0], tree)
    check("7 count_eq target.value -> integer expect, measured 2",
          document.claims[0]["checks"][0]["expect"] == 2
          and result["status"] == "holds")

    # 8. polarity flip on the same measurement
    a = evaluate_check(validate_check(_coerce_check(dict(good_check)), "fixture clause"),
                       FixtureTree({}))
    flipped = dict(good_check)
    flipped["expect"] = False
    b = evaluate_check(validate_check(_coerce_check(flipped), "fixture clause"),
                       FixtureTree({}))
    check("8 same measurement, flipped expect -> opposite status",
          a["status"] == "holds" and b["status"] == "mismatch")

    # 9. bridge statuses
    check("9 bridge maps holds/mismatch/could-not-evaluate, unknown -> NOT_EVALUATED",
          [_bridge({"status": s})["status"] for s in ("holds", "mismatch", "could-not-evaluate")]
          == ["HOLDS", "CONTRADICTED", "NOT_EVALUATED"]
          and _bridge({"status": "PASS"})["status"] == "NOT_EVALUATED")

    # 10. precedence
    malformed = judge_claim("M", [], [], schema_errors=["bad"])
    stale = judge_claim("S", [{"clause": "c"}],
                        [{"status": "CONTRADICTED"}], before="c")
    cne = judge_claim("N", [], [], before="c")
    fresh = judge_claim("F", [{"clause": "c"}], [{"status": "HOLDS"}], before="c")
    check("10 precedence malformed > stale > CNE > fresh",
          run_verdict([fresh, cne, stale, malformed]) == MALFORMED
          and run_verdict([fresh, cne, stale]) == STALE
          and run_verdict([fresh, cne]) == COULD_NOT_EVALUATE
          and run_verdict([fresh]) == FRESH)

    # 11. determinism of the decision surface
    r1 = build_report([fresh], round_id=1, baseline_commit="HEAD", baseline_sha=head_sha)
    r2 = build_report([fresh], round_id=1, baseline_commit="HEAD", baseline_sha=head_sha)
    check("11 identical inputs -> identical decision digest",
          r1["decision_sha256"] == r2["decision_sha256"])
    check("12 report carries no timestamp field",
          "generated_at" not in r1 and "timestamp" not in r1)

    # 13. exit table
    check("13 exit table 0/1/2/3",
          exit_code(FRESH) == 0 and exit_code(STALE) == 1
          and exit_code(MALFORMED) == 2 and exit_code(COULD_NOT_EVALUATE) == 3)

    # 14. baseline is a commit, not the worktree
    try:
        base = Baseline(_repo_root(pathlib.Path(root)), "7ceff59")
        head = Baseline(_repo_root(pathlib.Path(root)), "6e9a30d")
        check("14 baseline-only: resolver absent at 7ceff59, present at 6e9a30d",
              base.exists("tools/harness/basename-couples-resolver.py") is False
              and head.exists("tools/harness/basename-couples-resolver.py") is True)
    except GateInputError as exc:
        check("14 baseline-only: resolver absent at 7ceff59, present at 6e9a30d",
              False, str(exc))

    # 15. capability string form maps to a source signature with inverted polarity
    cap = dict(good_check, probe_kind="capability_present",
               target="tools/harness/x.py::four_class", expect=False)
    coerced = _coerce_check(cap)
    result = evaluate_check(validate_check(coerced, "fixture clause"),
                            FixtureTree({"tools/harness/x.py": "no marker\n"}))
    check("15 path::regex capability -> grep_absent with inverted expect",
          coerced["probe_kind"] == "grep_absent" and coerced["expect"] is True
          and result["status"] == "holds")

    # 16. overlay pin
    claims_path = write_temp("pin-claims.json", fixture_doc([good_check]))
    overlay = {
        "round": 999,
        "baseline_commit": "HEAD",
        "claims_sha256": "0" * 64,
        "checks": {"X": [good_check]},
    }
    try:
        doc = load_document(claims_path)
        load_overlay(write_temp("pin-overlay.json", json.dumps(overlay)), doc, None,
                     pathlib.Path(claims_path).read_bytes())
        check("16 overlay claims_sha256 mismatch -> malformed", False)
    except GateInputError:
        check("16 overlay claims_sha256 mismatch -> malformed", True)

    # 17. r43-shaped verdict (synthetic): two stale + one fresh -> exit 1
    rows = [
        judge_claim("O", [{"clause": "c"}], [{"status": "CONTRADICTED"}], before="c"),
        judge_claim("C", [{"clause": "c"}], [{"status": "CONTRADICTED"}], before="c"),
        judge_claim("Ca", [{"clause": "c"}], [{"status": "HOLDS"}], before="c"),
    ]
    report = build_report(rows, round_id=43, baseline_commit="7ceff59", baseline_sha=head_sha)
    check("17 two stale + one fresh -> STALE, exit 1, refusal names O and C",
          report["exit_code"] == 1 and "O, C" in report["refusal"]
          and "Ca" not in report["refusal"].split("do not dispatch")[0].split("claim(s)")[-1])

    # 18. render is line-oriented and ends with the exit code
    text = render_human(r1)
    check("18 human render ends with 'exit 0'", text.strip().endswith("exit 0"))

    seam_passed = sum(1 for _name, ok in controls if ok)
    seam_total = len(controls)
    print("SELFTEST %s: registry %s + seam %d/%d controls"
          % ("OK" if registry_ok and seam_passed == seam_total else "FAIL",
             registry_count, seam_passed, seam_total))
    return 0 if registry_ok and seam_passed == seam_total else 1


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="claims-freshness.py",
        description="Pre-dispatch claims-freshness gate (r47 claim O).",
    )
    parser.add_argument("--claims", help="claims.json to evaluate")
    parser.add_argument("--checks", help="optional before_checks overlay (O05 shape)")
    parser.add_argument("--root", default=".", help="repository root")
    parser.add_argument("--at", default=None, help="commit override (recorded as a deviation)")
    parser.add_argument("--json", action="store_true", help="machine-readable report")
    parser.add_argument("--no-exec", action="store_true",
                        help="disable capability execution (yields could-not-evaluate)")
    parser.add_argument("--selftest", action="store_true", help="run the control set")
    return run_cli(parser.parse_args(argv))


if __name__ == "__main__":
    sys.exit(main())
# W01-SEAM-END
