# W01 — O-claim landing spec: the integrator's exact apply for the pre-dispatch freshness gate

- Seat: `W01` | role executor | claim **O** (operability) | round 47, loop 2 (refire)
- Out path: `reports/round-47/op/W01-landing-spec.md` — the only file this seat writes
- Declared baseline: `6e9a30d` (`reports/round-47/claims.json:7`); HEAD at cut `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe`
- Mission: `reports/round-47/targets.json` seat W01 — "produce the integrator's exact apply instructions (target path, byte source = the assembled fenced tool, sha pin) + the calib/ demonstration artifact name"
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, lane root
- Status: **apply-ready, pre-landing**. `tools/harness/claims-freshness.py` is still absent; every measured result below comes from the assembled bytes in `.scratch/w01/claims-freshness.py`, which are pinned by §5 and reproducible by §7. The durable-path re-run is the integrator's (§3) and V02's job.

## 1. Bottom line

| item | value |
|---|---|
| **target path** | `tools/harness/claims-freshness.py` |
| **byte source** | four durable fences: O01 §8 (core), O02 Appendix A (probes), O03 §6 (verdict), this file's seam fence (§8) |
| **assembly** | `build-claims-freshness.py` (§7), four documented strips; **not** plain concatenation (§2) |
| **pinned sha256** | `d4e4d60ee45fdc3a5310527e03f829393b67440dc9694fcb8a24a31127ae8833` |
| **size** | 105,526 bytes / 2,714 lines, exactly one trailing LF |
| **pre-landing checks** | selftest exit 0 (`registry 43/43 + seam 19/19`); r43 demo exit 1 with O/C stale + Ca fresh; O06 negative control exit 0 with 9/9 clauses; O10 exit suite 14/14; anti-theater mutation unchanged; two runs byte-identical |
| **demo artifact** | `reports/round-47/calib/claims-freshness-demo.json` (§10) |
| **demo fixtures** | `reports/round-47/calib/r43-checks.json` (O05 §3, sha `0f43e907…`), `reports/round-47/calib/negative-control.claims.json` (O06 §3, sha `38857b08…`) |
| **other tracked delta** | none. No corpus byte, no packet surface, no filed-byte edit, no re-freeze. Rollback = delete the one file. |

The apply is gated on the sha: if the assembled bytes differ from the pin, **stop** — the fragments changed and this spec is stale. Do not "fix up" bytes by hand.

## 2. Why this is not plain concatenation (measured seam defects)

O01 §1 says the assembly "is plain concatenation; nothing in part 2/3 needs to edit these bytes." That is false, and the failures are not cosmetic. Each was reproduced while building the pinned bytes:

| # | defect | evidence |
|---|---|---|
| S1 | **duplicate future imports** — parts 2 and 3 each carry `from __future__ import annotations`; a mid-file future import is a `SyntaxError` | `python3 -m py_compile` on the naive concatenation fails at the second occurrence (O02 line 61, O03 line 22 of the fence) |
| S2 | **embedded `__main__` guard** — part 2 ends with `if __name__ == "__main__": sys.exit(selftest_registry())`; in a concatenated script that guard runs mid-file and exits before the CLI | first assembled run printed only `PROBE-REGISTRY SELFTEST: 43/43` and exited 0; no seam control ran |
| S3 | **part 1 mistypes `expect`** — `_check_entry` requires a JSON boolean, while part 2 requires an integer for `count_eq` and a 64-hex string for `sha256_eq` | a count check is rejected by part 1 before part 2 can type it; the seam loader delegates typing to part 2 and does not call `load_claims` |
| S4 | **part 2 / part 3 API mismatch** — part 2 returns `{status: holds\|mismatch\|could-not-evaluate, measured, expect}`; part 3 expects `{status: HOLDS\|CONTRADICTED\|NOT_EVALUATED, measured, expected}` | without the bridge, every clause would downgrade to `NOT_EVALUATED` (`evaluator-contract-violation`, O03 §3) and the r43 demo would become could-not-evaluate |
| S5 | **three target encodings** — canonical objects (O02), bare strings (O06/O10), and the O05 overlay (`{"capability": …}` / `{"glob": …, "value": …}`); O02's validator accepts only the first | O06's fixture is rejected with `path_absent target must be an object`; O05's overlay is rejected on unknown keys |
| S6 | **clause labels are not always verbatim spans** — O02 requires `clause` to be a substring of `before`; O06's fixture and O10's generated fixtures use labels ("no lithic owner", "the gap is unowned") | strict enforcement makes both filed acceptance artifacts malformed (exit 2) |
| S7 | **O01's docstring is part-1-specific** — it says "part 1/3" and "defines no `main()`"; in the assembled file both statements are false | doc drift only; recorded, not rewritten (that would change the pinned bytes) |

The seam (§8) supplies the four missing pieces: a loader that delegates typing to part 2, target-encoding compatibility, the result bridge, and the CLI/control set. It names no round, commit, corpus entry, or tool in its dispatch logic — the r43 literals live only in the demo fixtures (and in the embedded O02 selftest fixtures, a named divergence in §12). V02 §0 and O14 §1.2 independently measured S1–S4 on the same three fences; their reconstructed adapters reach the same r43 verdicts, which is why the seam's job is integration, not a semantic redesign.

## 3. Apply sequence (integrator)

Run from the lane root, with `TMPDIR` set. Steps 1–4 are pre-apply; 5–8 are the durable apply.

1. **Extract the seam.** Take the §8 fence whose first content line is the begin marker (do **not** use a bare first-occurrence search — the build script quotes the marker). With the fenced file saved as `.scratch/w01/seam.py` plus one trailing LF, its sha256 must be `d06ef2307e13c82e405733c6f440880433add4f8f0b2dcdaf9f9c9e75191652d` (692 lines, 28,598 bytes). The build script reads §8 directly, so this extraction is for inspection and the digest check, not a required input.
2. **Build and verify the pin.**
   ```
   python3 -B .scratch/w01/build-claims-freshness.py \
     --root . --out .scratch/w01/claims-freshness.assembled.py \
     --check d4e4d60ee45fdc3a5310527e03f829393b67440dc9694fcb8a24a31127ae8833
   ```
   Expect `assembled … bytes 105526 sha256 d4e4d60e…8833`, exit 0. A mismatch is a stop condition (re-check the four fence digests in §5).
3. **Pre-apply smoke test** on the assembled copy:
   ```
   python3 -B -m py_compile .scratch/w01/claims-freshness.assembled.py
   python3 -B .scratch/w01/claims-freshness.assembled.py --selftest
   ```
   Expect exit 0 and `SELFTEST OK: registry 43/43 + seam 19/19 controls`.
4. **Extract the two demo fixtures** (new records; never edit filed bytes):
   - `reports/round-47/calib/r43-checks.json` from `reports/round-47/op/O05-r43-demo.md` §3 (first `json` fence). Verify sha256 `0f43e90746ed99a1cae06e6887db87f9ca648aaeeebd3b7101a652bd82d8b25d` (2,175 bytes).
   - `reports/round-47/calib/negative-control.claims.json` from `reports/round-47/op/O06-negative-control.md` §3 (first `json` fence). Verify sha256 `38857b08543964cf2fd4a0154412279803043997d86fdcab1b2ce20499d4df1c` (5,031 bytes).
5. **Apply the bytes.** Write the assembled file to `tools/harness/claims-freshness.py` byte-exact; preserve exactly one trailing LF. Record `sha256sum tools/harness/claims-freshness.py` in `reports/round-47/validation.json`. Optional `chmod +x`; the counting commands invoke `python3`.
6. **Run from the durable path** (not `.scratch`); capture stdout and exit codes verbatim:
   ```
   python3 -B tools/harness/claims-freshness.py --selftest
   python3 -B tools/harness/claims-freshness.py --claims reports/round-43/claims.json \
     --checks reports/round-47/calib/r43-checks.json
   python3 -B tools/harness/claims-freshness.py --claims reports/round-47/calib/negative-control.claims.json
   python3 -B tools/harness/claims-freshness.py --claims reports/round-47/calib/negative-control.claims.json --at 6e9a30d
   ```
   Expected: 0; 1 (O/C stale, Ca fresh); 0 (9/9 clauses); 1 (O stale, C/Ca fresh — the baseline discriminator).
7. **File the demonstration** at `reports/round-47/calib/claims-freshness-demo.json` (§10), filled from the durable run, not copied from §9.
8. **Reclass the Ca row** only when G1–G7 pass (§11); otherwise leave `r43-stale-premises` at `routed-with-owner`.

Rollback: delete `tools/harness/claims-freshness.py`; the demo artifacts are additive records under `reports/round-47/`. No other tracked path changes.

## 4. Assembly transform (exact, reproducible)

Inputs are the four durable fences. The build script (§7) applies exactly these edits and nothing else:

| step | transform |
|---|---|
| part 1 | taken whole (its shebang and docstring stay the file header) |
| part 2 | drop lines through its `from __future__ import annotations` (shebang + module docstring); drop the trailing `if __name__ == "__main__":` / `sys.exit(selftest_registry())` pair |
| part 3 | drop its `from __future__ import annotations` line only; keep its comments and imports |
| join | `part1.rstrip("\n") + "\n" + part2.strip("\n") + "\n\n" + part3.strip("\n") + "\n\n" + seam.strip("\n") + "\n"` |
| output | 2,714 lines, 105,526 bytes, one trailing LF |

The build script selects fences by language and length: O01 has one `python` fence; O02 has one; O03 has three, and the longest (487 lines, sha `097a3198…`) is part 3. This avoids the four-backtick fence in O03 tripping a naive `awk '/^```python$/…'`.

## 5. Byte-source inventory and pins

| block | durable source | fence | sha256 | lines |
|---|---|---|---|---|
| core | `reports/round-47/op/O01-tool-core.md` | §8, sole `python` fence | `72c294f2c49dc53f3f7e7e65b0dc646e238a56b19473f84b63f1cb5bbf13b876` | 633 |
| probes | `reports/round-47/op/O02-probe-registry.md` | Appendix A, sole `python` fence | `a60b0a22df2d73c1a4075662d76a1d5c25a5caa8f6f35b72ffdf0c2ed772c191` | 967 |
| verdict | `reports/round-47/op/O03-verdict-contract.md` | §6, longest `python` fence | `097a31987cc334d93eaa117e60d7112cddeb7fbf9a356d10ca4dc178721cfcef` | 487 |
| seam | this file, §8 | between the SEAM markers | `d06ef2307e13c82e405733c6f440880433add4f8f0b2dcdaf9f9c9e75191652d` | 692 |
| **assembled** | — | — | **`d4e4d60ee45fdc3a5310527e03f829393b67440dc9694fcb8a24a31127ae8833`** | **2,714** |

Each of the first three digests equals the digest the owning seat published for its fence (O01 §1, O02 Appendix A, O03 §6), so the byte sources are the tested drafts, not re-typed copies.

## 6. Contract decisions the tool pins

These are the choices a reviewer must judge; each is implemented in the pinned bytes and exercised by a control.

1. **Seven probe kinds, closed.** `path_absent`, `path_present`, `grep_absent`, `count_eq`, `sha256_eq`, `topic_owner_absent`, `capability_present` (part 2's `PROBE_VALUE_TYPES`). Unknown kinds are malformed (exit 2). This follows the r47 claim (`claims.json:39`); P03/O13's recommended eighth kind `grep_present` is **not** implemented — a named divergence (§12).
2. **`expect` is predicate truth.** For boolean probes, `true` means the named predicate holds; `false` means its negation is the premise. For `count_eq`, `expect` is the integer; for `sha256_eq`, the 64-hex digest. Missing/null/wrong-typed `expect` is malformed. This is O06 §85 / O09 §3.0, not P01's inverted wording.
3. **Baseline is a commit, never the worktree.** `resolve_commit` uses `^{commit}` plus `git cat-file -t`; `Baseline` reads `git ls-tree -r -z` and `git cat-file --batch` only. `--at` is another commit, is recorded as a deviation, and cannot yield exit 0.
4. **Exit contract 0/1/2/3.** 0 all fresh; 1 any stale; 2 malformed/unusable baseline; 3 could-not-evaluate. Precedence malformed > stale > CNE > fresh. No `--allow-*` escape hatch exists.
5. **No prose miner.** A claim with no `before_checks` is could-not-evaluate, never mined. A non-empty `freshness_probes` list (the prototype/legacy schema) is refused as malformed because its entries carry no `clause`/`expect` polarity; an **empty** legacy list is a declaration of no checks and yields CNE (exit 3), matching O09 T2e. This diverges from P03's §5 miner; it is the contract-first choice and makes T1a (novel phrasing) exit 3 rather than false-STALE.
6. **Clause-label policy.** A `clause` that is a verbatim whitespace-normalized substring of `before` is recorded `verbatim`; a non-verbatim, non-empty label is accepted as `label`. This is a named relaxation of O02/P01: O06's and O10's filed fixtures use labels, and the measurement never depends on the label. An empty clause is still malformed.
7. **Target encodings.** Canonical part-2 objects are authoritative. Compatibility forms accepted by the loader: a bare string per kind (`path_*`/`sha256_eq` → path; `count_eq` → glob; `grep_absent` → `glob::regex`; `topic_owner_absent` → `partition:topic` or a bare topic across all partitions); `capability_present` as `<path>::<regex>` is mapped to `grep_absent` with inverted `expect`; O05's `{"capability": …}` is resolved through the named capability table; O05's `{"glob": …, "value": N}` becomes an integer `expect`.
8. **Named capability `couples_census` is behavioural.** It runs each `tools/harness/*.py` candidate against a wrapped-couples fixture with `--census`, requiring exit 0 and `refs=4`. The target carries no tool name, so the verdict survives the anti-theater rename (§9.5). `tools/gates/frozen/**` and the gate itself are excluded; the candidate cap is 32.
9. **Read-only, stdlib only, no bytecode.** No writes under `reports/`, `corpus/`, or `tools/`; capability probes execute in a per-candidate temp tree under `TMPDIR` (which these commands set to `.scratch`), removed afterwards.

## 7. Build script (fenced byte source)

Extract to `.scratch/w01/build-claims-freshness.py`; sha256 of the fenced file is `67c5bda72d7c0a8de226e0aea9f524e16b9eadf6fbb8b322cad96f696891b7d7`.

```python
#!/usr/bin/env python3
"""Build tools/harness/claims-freshness.py from the r47 round-47 fragments.

Inputs (all durable):
  reports/round-47/op/O01-tool-core.md    one python fence: core
  reports/round-47/op/O02-probe-registry.md  one python fence: probes
  reports/round-47/op/O03-verdict-contract.md  python fences; the longest is part 3
  reports/round-47/op/W01-landing-spec.md  the marker-delimited seam fence (section 8)

The transform is not plain concatenation; each edit below is required and is
named in W01 section 4:
  * part 2's shebang, module docstring and `from __future__` are dropped
  * part 3's duplicate `from __future__` is dropped
  * part 2's embedded `if __name__ == "__main__"` guard is dropped
  * the seam block is appended after part 3

Usage: python3 -B build-claims-freshness.py [--out PATH] [--check SHA]
Exit 0 when the output was written (and matches --check, if given).
"""
import argparse
import hashlib
import pathlib
import re
import sys


def fences(path):
    text = pathlib.Path(path).read_text(encoding="utf-8")
    out = []
    for match in re.finditer(r"(?m)^(`{3,4})([A-Za-z0-9_+-]*)\s*$", text):
        ticks, info = match.group(1), match.group(2)
        if not info:
            continue
        start = match.end() + 1
        close = re.search(r"(?m)^`{%d}\s*$" % len(ticks), text[start:])
        if not close:
            continue
        out.append((info, text[start:start + close.start()]))
    return out


def python_fence(path):
    bodies = [body for info, body in fences(path) if info == "python"]
    if not bodies:
        raise SystemExit("no python fence in %s" % path)
    return max(bodies, key=lambda body: body.count("\n"))


def part2_body(raw):
    lines = raw.splitlines(keepends=True)
    for index, line in enumerate(lines):
        if line.strip() == "from __future__ import annotations":
            body = "".join(lines[index + 1:])
            break
    else:
        raise SystemExit("part 2 has no future import")
    tail = body.rstrip("\n").splitlines()
    if len(tail) >= 2 and tail[-2].strip() == 'if __name__ == "__main__":' \
            and tail[-1].strip() == "sys.exit(selftest_registry())":
        tail = tail[:-2]
    return "\n".join(tail)


def part3_body(raw):
    return "\n".join(
        line for line in raw.splitlines()
        if line.strip() != "from __future__ import annotations"
    )


def seam_body(w01_path):
    text = pathlib.Path(w01_path).read_text(encoding="utf-8")
    match = re.search(
        r"(?ms)^```python\n(# W01-SEAM-BEGIN\n.*?\n# W01-SEAM-END)\n```",
        text,
    )
    if not match:
        raise SystemExit("no marker-delimited seam fence in %s" % w01_path)
    return match.group(1)


def assemble(root):
    root = pathlib.Path(root)
    part1 = python_fence(root / "reports/round-47/op/O01-tool-core.md")
    part2 = part2_body(python_fence(root / "reports/round-47/op/O02-probe-registry.md"))
    part3 = part3_body(python_fence(root / "reports/round-47/op/O03-verdict-contract.md"))
    seam = seam_body(root / "reports/round-47/op/W01-landing-spec.md")
    return (
        part1.rstrip("\n") + "\n"
        + part2.strip("\n") + "\n\n"
        + part3.strip("\n") + "\n\n"
        + seam.rstrip("\n") + "\n"
    )


def main(argv=None):
    parser = argparse.ArgumentParser()
    parser.add_argument("--root", default=".")
    parser.add_argument("--out", default=".scratch/w01/claims-freshness.assembled.py")
    parser.add_argument("--check", default=None)
    parser.add_argument("--print-sha", action="store_true")
    args = parser.parse_args(argv)

    text = assemble(args.root)
    data = text.encode("utf-8")
    digest = hashlib.sha256(data).hexdigest()
    pathlib.Path(args.out).parent.mkdir(parents=True, exist_ok=True)
    pathlib.Path(args.out).write_bytes(data)
    print("assembled %s bytes %d sha256 %s" % (args.out, len(data), digest))
    if args.print_sha:
        print(digest)
    if args.check is not None and digest != args.check:
        print("SHA MISMATCH: expected %s" % args.check, file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
```

## 8. Seam block (fenced byte source)

This is the block the build script takes between the two marker comments. It is byte-identical to the seam that produced the §9 transcript. Do not re-indent or re-wrap it.

```python
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
```

## 9. Pre-landing verification transcript (measured, not asserted)

All commands from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`; the subject is `.scratch/w01/claims-freshness.py` (sha `d4e4d60e…8833`), i.e. the assembled bytes, not the durable path.

### 9.1 Selftest — exit 0, counts from the controls

```
$ python3 -B .scratch/w01/claims-freshness.py --selftest | tail -2
PASS 18 human render ends with 'exit 0'
SELFTEST OK: registry 43/43 + seam 19/19 controls
$ echo $?
0
```

The registry block is part 2's own 43 controls (all seven kinds, polarity flips, strict typing, unknown-kind rejection, glob semantics, claim-level precedence). The seam block adds 19 controls (the labels are stable names, not a sequence; the count is `len(controls)`): loader, empty checks → CNE/3, missing `expect`, unknown kind, non-empty legacy schema refusal, empty legacy → CNE, duplicate id, count compatibility, polarity flip, bridge, precedence, determinism, no timestamp, exit table, baseline-only (7ceff59 vs 6e9a30d), `path::regex` capability mapping, overlay pin, r43-shaped verdict, render.

### 9.2 r43 positive regression — O and C STALE, Ca FRESH, exit 1

```
$ python3 -B .scratch/w01/claims-freshness.py \
    --claims reports/round-43/claims.json --checks .scratch/w01/r43-checks.json
claims-freshness: round 43 baseline 7ceff59 (7ceff59a0216a8ea21ee43262d9fc72abf770cee)
  [O] STALE             2/2 clauses contradict
      clause 0 (capability_present): measured=True expected=False -- no durable instrument implements the r39 basename-couples policy
      clause 1 (capability_present): measured=True expected=False -- the only resolver that ever ran (r39 I-C05) lives in ephemeral .scratch
  [C] STALE             1/3 clauses contradict
      clause 1 (topic_owner_absent): measured=False expected=True -- lithic slot named but unbuilt
  [Ca] FRESH             1/1 clauses hold
summary: 1 fresh, 2 stale, 0 could-not-evaluate, 0 malformed; clauses 6 (3 hold, 3 contradict, 0 not evaluated)
REFUSE: claim(s) O, C have a `before` already false at 7ceff59; do not dispatch.
exit 1
```

With `--json`, the decision digest is `653fe34e24958de2cdb9ee1886a10d3ab39a37e2a5d487bb1c23e9a8df2fb83f` and the claims are `[('O','stale'), ('C','stale'), ('Ca','fresh')]`.

### 9.3 Negative control — 9/9 clauses, exit 0

```
$ python3 -B .scratch/w01/claims-freshness.py \
    --claims .scratch/w01/negative-control.claims.json
claims-freshness: round 44 baseline c9f4eaa (c9f4eaa707b6e977ff6e1616463e91f4b8afea5d)
  [O] FRESH             5/5 clauses hold
  [C] FRESH             2/2 clauses hold
  [Ca] FRESH             2/2 clauses hold
summary: 3 fresh, 0 stale, 0 could-not-evaluate, 0 malformed; clauses 9 (9 hold, 0 contradict, 0 not evaluated)
exit 0
```

The fixture is O06's original fenced bytes, sha `38857b08…df1c` — no adaptation. Clause counts are O 5/5, C 2/2, Ca 2/2 (9/9), matching O06 §4's table.

### 9.4 Baseline discriminator — the same fixture at HEAD is not green

```
$ python3 -B .scratch/w01/claims-freshness.py \
    --claims .scratch/w01/negative-control.claims.json --at 6e9a30d
...
  [O] STALE (path_absent measured=false; count_eq measured=2 expected=1)
  [C] FRESH
  [Ca] FRESH
exit 1
```

Excerpt: the O detail lines are omitted. A worktree-reading gate would make the baseline run stale and the HEAD run "fresh"; this tool does the opposite, which is the contract (`git show`/`ls-tree` at `baseline_commit`). `--at` is recorded as a deviation; a fresh verdict under an override is capped to exit 3 (seam `run_cli`).

### 9.5 Anti-theater mutation — literal names replaced, verdict unchanged

The r43 claims copy was mutated: `basename-couples-resolver.py` → `zzz-renamed-instrument.py`, `basename-couples` → `zzz-policy`, `couples-reference-extractor.py` → `zzz-witness.py`; the overlay was re-pinned to the mutated bytes (`9688042f…`).

```
$ python3 -B .scratch/w01/claims-freshness.py \
    --claims .scratch/w01/r43-mutated.json --checks .scratch/w01/r43-mutated-checks.json
  [O] STALE 2/2 clauses contradict
  [C] STALE 1/3 clauses contradict
  [Ca] FRESH 1/1 clauses hold
exit 1
```

The O verdict comes from the behavioural `couples_census` capability; C's from the header ownership scan. The claim's prose and `after_required` names are never measured. A control in the same run also proves the overlay pin: with the original overlay, the mutated claims file exits 2 (`claims_sha256 … does not match`).

### 9.6 Exit-code conformance — O10's suite, 14/14

```
$ python3 -B .scratch/w01/o10-exit-conformance.py \
    --tool .scratch/w01/claims-freshness.py --root .
14 case(s), 0 failure(s)
EXIT-CONFORMANCE: PASS        # suite exit 0
```

The suite (sha `374f5021…645f3`) covers fresh-all, stale-one, stale-topic, mixed, stale+CNE, empty/missing checks, six malformed shapes, non-JSON, and the exit-0 invariant.

### 9.7 Determinism and read-only

```
$ python3 -B .scratch/w01/claims-freshness.py --claims reports/round-43/claims.json \
    --checks .scratch/w01/r43-checks.json --json > run1.json
$ ... > run2.json
$ sha256sum run1.json run2.json
705d8de4704786b1f1bc8bb45bc123a9ebdd1a266fb6d6f0518ad83f702e5b93  run1.json
705d8de4704786b1f1bc8bb45bc123a9ebdd1a266fb6d6f0518ad83f702e5b93  run2.json
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-47/
```

No tracked path changed, no corpus byte staged, no `.pyc` written. The two runs are byte-identical (no timestamp in the decision surface).

## 10. Demonstration artifact — `reports/round-47/calib/claims-freshness-demo.json`

This is the O claim's "filed demonstration at `reports/round-47/calib/`". It is an **integrator-authored new record**, not a seat write. Schema `kotodama-claims-freshness-demo-v1`:

```json
{
  "schema": "kotodama-claims-freshness-demo-v1",
  "round": 47,
  "claim": "O",
  "tool": {
    "path": "tools/harness/claims-freshness.py",
    "sha256": "<durable-path sha256; must equal d4e4d60e…8833>",
    "bytes": 105526,
    "lines": 2714,
    "version": "2.0-part1 (O01 VERSION constant; assembled path pinned by sha256)"
  },
  "baseline_commit": "6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe",
  "environment": {"python": "3.14.7", "git": "2.55.0", "tmpdir": "<repo>/.scratch"},
  "runs": [
    {"id": "selftest", "command": "python3 tools/harness/claims-freshness.py --selftest",
     "exit": 0, "summary": "registry 43/43 + seam 19/19 controls"},
    {"id": "r43-regression",
     "command": "python3 tools/harness/claims-freshness.py --claims reports/round-43/claims.json --checks reports/round-47/calib/r43-checks.json",
     "exit": 1, "verdicts": {"O": "stale", "C": "stale", "Ca": "fresh"},
     "decision_sha256": "<from the durable run>"},
    {"id": "negative-control",
     "command": "python3 tools/harness/claims-freshness.py --claims reports/round-47/calib/negative-control.claims.json",
     "exit": 0, "claims": 3, "clauses": 9, "holds": 9},
    {"id": "baseline-discriminator",
     "command": "python3 tools/harness/claims-freshness.py --claims reports/round-47/calib/negative-control.claims.json --at 6e9a30d",
     "exit": 1, "verdicts": {"O": "stale", "C": "fresh", "Ca": "fresh"}},
    {"id": "exit-conformance",
     "command": "python3 <O10 suite> --tool tools/harness/claims-freshness.py --root .",
     "exit": 0, "cases": 14, "failures": 0}
  ],
  "fixtures": [
    {"path": "reports/round-47/calib/r43-checks.json",
     "sha256": "0f43e90746ed99a1cae06e6887db87f9ca648aaeeebd3b7101a652bd82d8b25d"},
    {"path": "reports/round-47/calib/negative-control.claims.json",
     "sha256": "38857b08543964cf2fd4a0154412279803043997d86fdcab1b2ce20499d4df1c"}
  ],
  "source_fragments": {
    "O01": "72c294f2…b876", "O02": "a60b0a22…c191",
    "O03": "097a3198…cef", "seam": "d06ef230…652d"
  },
  "limits": ["capability execution is not an OS sandbox", "no honest live control for tag ambiguity", "pre-landing values are not the durable run"]
}
```

Fill every `<>` from the durable run; do not copy §9's values as though they were the durable run. The demo's `runs[].exit` and verdict tokens are the G3/G4 evidence for Ca06.

## 11. Ca06 reclass mapping (`r43-stale-premises`: G1–G7)

`reports/round-47/calib/Ca06-queue-successor.md` (row `r43-stale-premises`, `reclass_gates` G1–G7 in its §5 fenced successor) reclasses only when all seven pass. This spec supplies the command and the expected evidence for each:

| gate | requirement | evidence from this apply |
|---|---|---|
| G1 | durable path exists, sha recorded, not `.scratch` | step 5; `sha256sum tools/harness/claims-freshness.py` == `d4e4d60e…8833` |
| G2 | green selftest, asserted count == controls run | §9.1: `registry 43/43 + seam 19/19`; the seam computes 19 from `len(controls)`, the registry computes 43 from its own list |
| G3 | r43 O/C STALE, Ca FRESH, non-zero exit, actual codes quoted | §9.2: exit 1, two stale + one fresh, 6 clauses |
| G4 | negative control not flagged, exit 0 | §9.3: 3 fresh, 9/9 clauses, exit 0 |
| G5 | anti-theater mutation still flags from capability/ownership | §9.5: same three verdicts after the rename |
| G6 | worktree-true/baseline-false clause flags | §9.4: the c9f4eaa fixture at 6e9a30d makes O stale (path present, family count 2) |
| G7 | CNE not green; malformed exits 2 | §9.6: cne-empty/missing → 3; malformed shapes → 2; O10 suite |

If any gate is red on the durable path, the row stays `routed-with-owner`; do not reclass on tool existence alone (Ca06's own instruction).

## 12. Named divergences from sibling drafts (do not silently reconcile)

| source | divergence | disposition in the pinned tool |
|---|---|---|
| O01 §1 | "plain concatenation, nothing needs editing" | false; four strips are required (§2 S1/S2) and the seam loader replaces `load_claims` (§2 S3) |
| O01 docstring | says "part 1/3", "defines no `main()`" | stale in the assembled file; kept to preserve the fence digest; the seam header supersedes it |
| O02 `validate_check` | clause must be a verbatim substring | relaxed to verbatim-or-label (§6.6) because O06 and O10 use labels; empty clause still malformed |
| O02 capability target | behavioural only, no tool name | kept canonical; the compatibility `capability`/`scope` and `path::regex` forms are resolved by the seam (§6.7/6.8) |
| O03 §4 | exit 3 is a recommendation; 0/1/2 named | adopted 0/1/2/3, precedence malformed > stale > CNE > fresh; `--at` caps fresh at 3 |
| O04 §5 | 46-control drop-in expecting `kind`, `FixtureBaseline`, `evaluate_claim` | not embedded; the landed control set is O02's 43 registry controls + 19 seam controls. O04's assertions for `grep_present` and its `FixtureBaseline` API are not applicable to the seven-kind claim. Record as a spec divergence, not a green claim. |
| O05 §3 | overlay count checks use `expect:true` + `target.value` | coerced to integer `expect` before validation; the measurement is unchanged |
| O06 §3 | three clause labels are paraphrases | accepted as labels (§6.6); original fixture digest preserved (`38857b08…`) |
| O10 §3 | fixtures use bare string targets and label clauses | compatibility forms accepted; suite passes 14/14 |
| P03 §1/§5 | `polarity` field, 8th kind `grep_present`, prose miner, `--regress` | not implemented; the claim's seven-kind `expect` schema governs. P03 is a plan, not the drafted bytes. Record as a named deviation. |
| O13 §2.3 | recommends the eight-kind P01 set | the seventh/sixth ambiguity is resolved in favour of the claim's seven; `grep_present` is not in the closed registry |
| O09 T2e | `freshness_probes: []` must be CNE (exit 3), not malformed | adopted: empty legacy list → zero checks → CNE; non-empty legacy entries → malformed (2) |
| O07 §8.3 | O02 uses `{"topic", "partitions"}`, O05 uses `{"topics", "partition"}` | both accepted; the seam normalizes to O02's canonical keys, so O07's mutation fixtures and O05's overlay run unchanged |
| P03 §8 G3 | the tool body must contain none of `7ceff59`, `c9f4eaa`, `lithic`, `basename-couples` | **not satisfied**: the embedded O02 selftest fixtures and O01 docstring contain `7ceff59`, `6e9a30d`, `lithic`, `basename-couples`, `mineral-stone`. They are test/doc strings, never dispatch keys; a source-grep control would need to exclude the selftest section. Recorded, not hidden. |

## 13. Limits and `to-verify`

1. **Capability execution is not sandboxed.** Candidates run as `python3 -I -B` in a temp cwd with a timeout; a tool that walks above the fixture root could read the worktree. Mitigations: in-repo globs, `exclude_globs`, candidate cap, `--no-exec`. Do not claim an OS sandbox.
2. **The capability probe is behavioural but broad.** It runs every `tools/harness/*.py` with `--census`; a future tool that happens to print `refs=4` would satisfy it. At `7ceff59` only the witness passes; at `6e9a30d` both the witness and the successor pass (measured: the r43 overlay run with `--at 6e9a30d` reports `2/8 candidate(s) pass`), which is the intended signal; a narrower registry is a future refinement.
3. **Absence claims and failed candidates (V02 §6).** The capability probe counts a candidate only on exit 0 + `success_regex`; a present-but-crashing capability is therefore measured absent, and for an `expect:false` clause that can launder a stale premise as fresh. The r43 witness exits 0 (measured), so the demo is unaffected. The hardening is per-candidate: an execution failure should be `could-not-evaluate`, not "no capability". `to-verify` for r48.
4. **No tag in the lane.** `resolve_commit` handles tags via `^{commit}`, but O09 T3's annotated-tag/ambiguous-ref vectors were not run against the durable path. `to-verify`; the rule is documented and the tree/blob rejection is in O01's selftest.
5. **Python floor.** `X | None` syntax and `from __future__ import annotations` (stripped from parts 2/3) put the tool at 3.10+; only 3.14.7 was exercised.
6. **SHA-1 object format only.** This repo is SHA-1; `cat-file --batch` header parsing should be object-format agnostic but was not tested on SHA-256.
7. **The demonstration values in §9 are pre-landing.** The durable-path run may differ in elapsed time and file path; verdicts, exit codes and the decision digest must match. If they do not, the apply is not accepted.
8. **The round runner `reports/round-47/run-validation.py` does not exist at this cut** and must not be created in-tree by a seat. The integrator runs the round's validation out-of-tree and records the O evidence there.

## 14. Seat ledger

Writes: this file only (`reports/round-47/op/W01-landing-spec.md`). Scratch work (not durable, not cited as evidence): `.scratch/w01/part1.py`, `part2.raw.py`, `part3.raw.py`, `seam.py`, `claims-freshness.py`, `r43-checks.json`, `negative-control.claims.json`, `o10-exit-conformance.py`, `build-claims-freshness.py`, `run*.json`, `final-*.json`, `r43-mutated*.json`.

Commands run: `git rev-parse`, `git ls-tree`, `git show`, `git cat-file`, `git status`, `sha256sum`, `wc`, `python3 -B` (compile, selftest, demos, O10 suite). No commit/push/install/network; no `run-validation.py`; no filed byte edited; nothing staged under `corpus/`; `declared-in-r7` untouched; no packet-surface change.
9. **Selftest portability.** The baseline-only control anchors `7ceff59` and `6e9a30d`; `--selftest` is therefore lane-specific. In another repository the control needs equivalent anchors or must be skipped with a named `could-not-evaluate` (never a silent green).
