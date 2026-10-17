# R11-O05 — CLI + negatives fragment for `tools/exercise-handoff-e2e.py`

- shard: R11-O05 (handoff lane, claim O — operability), impl-support fragment
- date: 2026-10-17 (all commands and digests below measured on this date, -03:00)
- writer: L2 worker, round-11 wave (opencode-go-2/deepseek-v4.1-flash)
- write scope: this file only. The tool itself (`tools/exercise-handoff-e2e.py`) is
  the single-writer shard R11-O02..O05; no file of an earlier round was edited.
- status: fragment verified in scratch against the live gate; not the tool.

This fragment delivers two paste-ready pieces for the exercise:

1. **CLI surface** — `--selftest` / `--json` / `--keep`, the 0/1/2 exit contract,
   the stable `EX-CLI-*` / `EX-E2E-*` diagnostics, and the live-run receipt shape.
2. **Negatives battery** — seven form-aware planted-defect mutants, four
   malformed-data controls, two CLI negatives, a gate-missing fail-closed
   control, and a bogus-expectation control that proves the matcher can fail.

Reference prototype with everything wired (scratch, uncommitted, copy verbatim
into the tool): `.scratch/o05/proto_exercise_cli.py` (CLI + selftest driver) and
`.scratch/o05/mutation_battery.py` (launcher + matcher + battery). Transcripts:
`.scratch/o05/selftest-transcript.txt`, `.scratch/o05/evidence-transcript.txt`,
`.scratch/o05/two-source-verify.txt`.

## 1. Integration seams (what the tool writer must supply)

| Seam | Contract | Owner |
|---|---|---|
| Packet assembly | `assemble_packet(repo_root) -> (packet_bytes, provenance_dict)`; deterministic; no writes outside a temp dir | assembler shards (O06..O09) |
| Live expectation | `{"exit": 0, "finding_ids": [], "scan": {"fields": 16, "glossary": 20}}` — the claim's declared positive verdict; compare *exactly* | this fragment |
| Control sources | two live sources so the battery proves form-independence: `examples/handoff-packet.sample.md` (heading form) and `examples/culture-d3/handoff.md` (envelope-table form) | this fragment |
| Committed baseline | `expected.json` (O14..O15); the CLI reserves `EX-E2E-BASELINE*` codes for it but does not implement `--frozen` here | baseline shard O14..O15 |
| Path handling | closed: the tool accepts **no** input paths on argv; every path it reads is a module constant (lane convention, cf. `tools/check-evidence-coupling.py`) | this fragment |

`assemble_packet` is the only function the assembler shards must provide. The
prototype's stand-in returns the live sample bytes with a provenance dict; the
integrator replaces the function body and re-runs `--selftest`.

**Count-drift note (integration-critical):** the mutants' *finding-ID*
expectations are fixed by the gate's semantics (§5) and hold for any packet
carrying the 16 envelope fields and ≥1 glossary table with an `etymology`
column. The *scan-count* expectations (`fields=15/16`, `glossary=20`) are
properties of the graded packet: the integrator must set them from the
assembled packet's actual counts once, at freeze time. If the assembled
packet's glossary count is not 20, only the `scan.glossary` numbers change.

## 2. CLI contract

```text
python3 tools/exercise-handoff-e2e.py                 # live exercise
python3 tools/exercise-handoff-e2e.py --selftest      # controls battery
python3 tools/exercise-handoff-e2e.py --json          # machine receipt
python3 tools/exercise-handoff-e2e.py --keep          # keep the isolated mirror
```

| Invocation | Behaviour | Exit |
|---|---|---|
| (no args) | assemble from live artifacts → run `handoff-packet-check` in an isolated mirror → exact compare against the declared expectation | 0 pass · 1 mismatch · 2 could-not-evaluate |
| `--selftest` | positive + plants + malformed + CLI negatives + gate-missing + bogus-expectation; drives the real CLI as subprocesses | 0 all rows pass · 1 any row fails |
| `--json` | one JSON object on stdout (run receipt, or selftest receipt with `--selftest`); the verdict exit code is unchanged | as above |
| `--keep` | keep the isolated mirror dir; path printed on **stderr**; verdict unchanged | as above |
| `-h` / `--help` | argparse help | 0 |
| unknown flag, stray positional | argparse message on stderr, **no traceback** | 2 |

Precedence: could-not-evaluate (2) outranks mismatch (1); a run that could not be
evaluated never compares equal to anything. This mirrors `tools/replay-frozen.py`
and `tools/check-gate-battery.py`.

Diagnostics (stable; stderr, no tracebacks):

| ID | Meaning |
|---|---|
| `EX-CLI-USAGE` | reserved for a usage error the parser cannot express (argparse already exits 2 itself) |
| `EX-E2E-GATE-MISSING` | the gate script is absent — fail closed, never invent a verdict |
| `EX-E2E-GATE-UNREADABLE` | the gate bytes cannot be read |
| `EX-E2E-GATE-MUTATED` | the gate's digest changed between launch-prep and result parse |
| `EX-E2E-LAUNCH` | the subprocess could not be started |
| `EX-E2E-ASSEMBLY` | reserved: `assemble_packet` fails or returns a non-UTF-8/non-Markdown payload |
| `EX-E2E-BASELINE`, `EX-E2E-BASELINE-TAMPER` | reserved for the O14 baseline mode |

Mismatch tokens (live mode, printed after `MISMATCH`): `exit=<o>!=<e>`,
`ids=<observed>!=<expected>` (multiset), `scan.fields=<o>!=<e>`,
`scan.glossary=<o>!=<e>`. The matcher compares the finding-ID **multiset**, exit
code, and scan counts; `stdout_sha256` is reported as an advisory pin only —
per `gate-frozen-run-standard.md` §4 the byte hash is never the finding contract
(the round-10 census lesson: multiplicity differences are real disagreements).

## 3. Paste-ready code

### 3.1 Parser, exit mapping, live receipt

```python
def parse_args(argv):
    parser = argparse.ArgumentParser(
        prog="exercise-handoff-e2e.py",
        description="Assemble a handoff packet from live D2/D3 artifacts and "
                    "validate it through handoff-packet-check in an isolated copy.")
    parser.add_argument("--selftest", "--self-test", action="store_true",
                        help="positive + planted-defect + malformed + CLI-negative + "
                             "bogus-expectation controls")
    parser.add_argument("--json", action="store_true",
                        help="emit the run receipt (or the selftest receipt) as one JSON object")
    parser.add_argument("--keep", action="store_true",
                        help="keep the isolated mirror directory and print its path")
    return parser.parse_args(argv)


def main(argv=None) -> int:
    try:
        args = parse_args(sys.argv[1:] if argv is None else argv)
    except SystemExit as exc:              # argparse already printed usage + message
        return EXIT_UNEVALUATED if exc.code else EXIT_PASS
    repo_root = find_repo_root(Path(__file__))
    if args.selftest:
        receipt = selftest(repo_root)
        if args.json:
            print(json.dumps(receipt, indent=1, sort_keys=True))
        else:
            for row in receipt["rows"]:
                print(f"selftest {row['control']}: {'PASS' if row['passed'] else 'FAIL'} {row['detail']}")
            print(f"selftest: {receipt['passed']}/{receipt['total']} passed")
        return EXIT_FINDINGS if receipt["failures"] else EXIT_PASS
    packet, prov = assemble_packet(repo_root)       # seam: assembler shards
    keep = Path(tempfile.mkdtemp(prefix="handoff-e2e-keep-")) if args.keep else None
    obs = run_gate_isolated(repo_root, packet, keep_dir=keep)
    expected = CONTROLS["positive"]
    diffs = compare(obs, expected)
    receipt = {"schema": "kotodama-handoff-e2e-v1", "provenance": prov,
               "observed": obs, "expected": expected, "mismatches": diffs,
               "verdict": "pass" if not diffs else ("unevaluated" if obs.get("error") else "mismatch")}
    if args.json:
        print(json.dumps(receipt, indent=1, sort_keys=True))
    else:
        if obs.get("error"):
            _diag(E2E_PREFIX, obs["error"].removeprefix("EX-E2E-"), obs.get("detail", ""))
        else:
            print(f"handoff-e2e: exit={obs['exit']} findings={obs['ids']} scan={obs['scan']} "
                  f"gate_sha256={obs['gate_sha256'][:12]} stdout_sha256={obs['stdout_sha256'][:12]}"
                  + ("" if not diffs else " MISMATCH " + ";".join(diffs)))
        if keep:
            print(f"mirror kept at {keep}", file=sys.stderr)
    if obs.get("error"):
        return EXIT_UNEVALUATED
    return EXIT_PASS if not diffs else EXIT_FINDINGS


def find_repo_root(start: Path) -> Path:
    """Fail-closed repo root: the first ancestor carrying the gate script."""
    for cand in start.resolve().parents[1:4]:
        if (cand / GATE_REL).is_file():
            return cand
    return start.resolve().parents[1]
```

### 3.2 Isolated launch (gate + packet copied into a temp mirror)

```python
def run_gate_isolated(repo_root: Path, packet_bytes: bytes, keep_dir: Path | None = None) -> dict:
    gate_src = repo_root / GATE_REL
    if not gate_src.is_file():
        return {"error": "EX-E2E-GATE-MISSING", "detail": str(gate_src)}
    try:
        gate_sha_before = hashlib.sha256(gate_src.read_bytes()).hexdigest()
    except OSError as exc:
        return {"error": "EX-E2E-GATE-UNREADABLE", "detail": str(exc)}
    tmp = Path(tempfile.mkdtemp(prefix="handoff-e2e-", dir=str(keep_dir) if keep_dir else None))
    try:
        mirror_gate = tmp / Path(GATE_REL).name
        shutil.copyfile(gate_src, mirror_gate)
        packet = tmp / "packet.md"
        packet.write_bytes(packet_bytes)
        try:
            p = subprocess.run([sys.executable, str(mirror_gate), str(packet)],
                               capture_output=True, cwd=str(tmp))
        except OSError as exc:
            return {"error": "EX-E2E-LAUNCH", "detail": str(exc)}
        gate_sha_after = hashlib.sha256(gate_src.read_bytes()).hexdigest()
        if gate_sha_after != gate_sha_before:
            return {"error": "EX-E2E-GATE-MUTATED",
                    "gate_sha256_before": gate_sha_before, "gate_sha256_after": gate_sha_after}
        out = p.stdout.decode("utf-8", "replace")
        ids = [m.group(1) for m in FINDING_RE.finditer(out)]
        scan = None
        m = SCAN_RE.search(out)
        if m:
            scan = {"fields": int(m.group(1)), "fields_expected": int(m.group(2)),
                    "glossary": int(m.group(3)), "findings": int(m.group(4))}
        return {"exit": p.returncode, "ids": sorted(ids), "scan": scan,
                "stdout_sha256": hashlib.sha256(p.stdout).hexdigest(),
                "stderr": p.stderr.decode("utf-8", "replace")[:400],
                "gate_sha256": gate_sha_before}
    finally:
        if keep_dir is None:
            shutil.rmtree(tmp, ignore_errors=True)
```

### 3.3 Exact matcher

```python
def compare(observed: dict, expected: dict) -> list[str]:
    if observed.get("error"):
        return [f"error={observed['error']}"]
    diffs = []
    if observed["exit"] != expected["exit"]:
        diffs.append(f"exit={observed['exit']}!={expected['exit']}")
    if sorted(observed["ids"]) != sorted(expected["finding_ids"]):
        diffs.append(f"ids={','.join(observed['ids'])}!={','.join(sorted(expected['finding_ids']))}")
    scan = observed["scan"] or {}
    exp_scan = expected.get("scan")
    if exp_scan:
        for key in ("fields", "glossary"):
            if scan.get(key) != exp_scan.get(key):
                diffs.append(f"scan.{key}={scan.get(key)}!={exp_scan.get(key)}")
    return diffs
```

### 3.4 Form-aware mutation battery (the negatives fragment)

The gate recognizes a field in three forms (`handoff-packet-check.py`, module
docstring "Field recognition"): a `## field` heading, a `- field: value` list
item, or the first cell of a `| field | value |` row. A mutant that assumes one
form silently no-ops on the other — **measured**: the first version of this
battery failed 3/7 plants on `examples/culture-d3/handoff.md` (row form). The
battery below locates each field's value region in any form, and raises on a
no-op so a control that does not alter the bytes is a hard error, never a
silent pass.

```python
def _field_span(text: str, field: str):
    """(name_start, value_start, value_end, kind) or None."""
    f = re.escape(field)
    m = re.search(rf"^##\s+`?{f}`?\s*$", text, re.M)
    if m:
        nl = text.find("\n", m.end())
        value_start = len(text) if nl == -1 else nl + 1
        nxt = re.search(r"^##\s", text[value_start:], re.M)
        value_end = value_start + nxt.start() if nxt else len(text)
        return m.start(), value_start, value_end, "heading"
    m = re.search(rf"^\|\s*`?{f}`?\s*\|", text, re.M)
    if m:
        close = re.search(r"\|\s*$", text[m.end():], re.M)
        if close:
            line_start = text.rfind("\n", 0, m.start()) + 1
            return line_start, m.end(), m.end() + close.start(), "row"
    m = re.search(rf"^[-*+]\s+`?{f}`?:\s*", text, re.M)
    if m:
        cm = _ITEM_TAIL.match(text[m.end():])
        value_end = m.end() + (cm.end() if cm else 0)
        return m.start(), m.end(), value_end, "item"
    return None


def _carriage_span(text: str, field: str):
    fs = _field_span(text, field)
    if fs is None:
        return None
    name_start, _value_start, value_end, kind = fs
    if kind == "row":
        value_end = text.find("\n", value_end) + 1 or len(text)
    return name_start, value_end
```

Mutations (each raises `ValueError` on a no-op):

| Mutation | Mechanism | Planted finding |
|---|---|---|
| `drop-field` | delete the whole recognized carriage of a field | `HO-MISSING` |
| `blank-field` | value → `TBD` | `HO-EMPTY` |
| `canon-claim` | replace/replant `canon_standing` with a producer certification | `HO-CANON-CLAIM` |
| `gloss-blank` | blank the etymology cell of the first glossary data row; column index read from the **header** | `HO-GLOSS-ETYM` |
| `dep-float` | neutralize any `no/not/never … latest` negation carve-out, then inject a floating `latest` | `HO-DEP-FLOAT` |
| `contract-ref` | strip revision + digest | `HO-CONTRACT-REF` |
| `manifest-digest` | strip every `sha256:<64 hex>` from the manifest value | `HO-MANIFEST-DIGEST` |

Bodies (verbatim, as verified):

```python
def _drop_field(text: str, field: str) -> str:
    ns = _carriage_span(text, field)
    if ns is None:
        raise ValueError(f"field {field!r} not found in any recognized form")
    return _replace(text, ns, "")


def _blank_field(text: str, field: str, value: str = "TBD") -> str:
    fs = _field_span(text, field)
    if fs is None:
        raise ValueError(f"field {field!r} not found in any recognized form")
    _n, vs, ve, kind = fs
    new = f" {value} " if kind == "row" else (f"{value}\n\n" if kind == "heading" else f" {value}\n")
    return _replace(text, (vs, ve), new)


def _dep_float(text: str, field: str = "dependency_manifest") -> str:
    fs = _field_span(text, field)
    if fs is None:
        raise ValueError(f"field {field!r} not found in any recognized form")
    _n, vs, ve, kind = fs
    value = text[vs:ve]
    cleared = re.sub(r"(?i)\b(no|not|never)\b[^.\n]{0,30}\blatest\b", "versions pinned", value)
    inject = (" P-D1-UNION phonology profile `latest` (planted: floating reference);"
              if kind == "row"
              else "\n- P-D1-UNION phonology profile `latest` (planted: floating reference)\n")
    new_value = inject + cleared if kind == "row" else cleared + inject
    return _replace(text, (vs, ve), new_value)


def _set_value(text: str, field: str, new_value: str) -> str:
    fs = _field_span(text, field)
    if fs is None:
        raise ValueError(f"field {field!r} not found in any recognized form")
    _n, vs, ve, kind = fs
    new = f" {new_value} " if kind == "row" else f"{new_value}\n\n"
    return _replace(text, (vs, ve), new)


def _contract_ref_strip(text: str, field: str = "contract_ref") -> str:
    return _set_value(text, field, "kotodama-lore-adjacency (planted: no revision, no digest)")


def _manifest_strip(text: str, field: str = "artifact_manifest") -> str:
    fs = _field_span(text, field)
    if fs is None:
        raise ValueError(f"field {field!r} not found in any recognized form")
    _n, vs, ve, _kind = fs
    value = text[vs:ve]
    stripped = re.sub(r"sha256:[0-9a-f]{64}", "digest-omitted", value)
    if stripped == value:
        raise ValueError("manifest carries no sha256 digest to strip (mutation would be a no-op)")
    return _replace(text, (vs, ve), stripped)


def _canon_claim(text: str) -> str:
    new = "- canon_standing: canonized — the producer certifies this packet as canon (planted)"
    out = re.sub(r"(?i)^-?\s*canon_standing:.*$", new, text, count=1, flags=re.M)
    if out == text:
        out = re.sub(r"(?m)^(# .*)$", r"\1\n\n" + new, text, count=1)
    if out == text:
        raise ValueError("no canon_standing line and no H1 to plant after")
    return out


def _gloss_blank(text: str) -> str:
    lines = text.splitlines(keepends=True)
    header_idx = col = None
    for i, ln in enumerate(lines):
        if ln.lstrip().startswith("|") and re.search(r"(?i)\betymolog", ln):
            cells = [c.strip().strip("`").lower() for c in ln.strip().strip("|").split("|")]
            if "etymology" in cells:
                header_idx, col = i, cells.index("etymology")
                break
    if header_idx is None:
        raise ValueError("no glossary table with an etymology column found")
    ncols = len(lines[header_idx].strip().strip("|").split("|"))
    for j in range(header_idx + 1, len(lines)):
        ln = lines[j]
        if not ln.lstrip().startswith("|") or set(ln.replace("|", "").strip()) <= set("-: "):
            continue
        cells = ln.split("|")
        if len(cells) < ncols + 1 or not cells[col + 1].strip():
            continue
        cells[col + 1] = " "
        lines[j] = "|".join(cells)
        return "".join(lines)
    raise ValueError("no glossary data row with a filled etymology cell found")


def apply_mutation(packet_text: str, mutation: str, arg) -> str:
    fn = MUTATIONS[mutation]
    out = fn(packet_text, arg) if arg is not None else fn(packet_text)
    if out == packet_text:
        raise ValueError(f"mutation {mutation!r} was a no-op on this packet")
    return out
```

Controls table consumed by `--selftest` (IDs and expectations verbatim):

```python
CONTROLS = {
    "positive": {"exit": 0, "finding_ids": [], "scan": {"fields": 16, "glossary": 20}},
    "plants": [
        {"id": "M-missing-field", "mutation": "drop-field", "arg": "open_questions",
         "expected": {"exit": 1, "finding_ids": ["HO-MISSING"], "scan": {"fields": 15, "glossary": 20}}},
        {"id": "M-blank-field", "mutation": "blank-field", "arg": "request_ref",
         "expected": {"exit": 1, "finding_ids": ["HO-EMPTY"], "scan": {"fields": 15, "glossary": 20}}},
        {"id": "M-canon-claim", "mutation": "canon-claim", "arg": None,
         "expected": {"exit": 1, "finding_ids": ["HO-CANON-CLAIM"], "scan": {"fields": 16, "glossary": 20}}},
        {"id": "M-gloss-blank", "mutation": "gloss-blank", "arg": None,
         "expected": {"exit": 1, "finding_ids": ["HO-GLOSS-ETYM"], "scan": {"fields": 16, "glossary": 20}}},
        {"id": "M-dep-float", "mutation": "dep-float", "arg": None,
         "expected": {"exit": 1, "finding_ids": ["HO-DEP-FLOAT"], "scan": {"fields": 16, "glossary": 20}}},
        {"id": "M-contract-ref", "mutation": "contract-ref", "arg": None,
         "expected": {"exit": 1, "finding_ids": ["HO-CONTRACT-REF"], "scan": {"fields": 16, "glossary": 20}}},
        {"id": "M-manifest-digest", "mutation": "manifest-digest", "arg": None,
         "expected": {"exit": 1, "finding_ids": ["HO-MANIFEST-DIGEST"], "scan": {"fields": 16, "glossary": 20}}},
    ],
    "malformed": [
        {"id": "D-empty", "case": "empty-file", "expected": {"exit": 2, "finding_ids": ["HO-DATA"]}},
        {"id": "D-directory", "case": "directory", "expected": {"exit": 2, "finding_ids": ["HO-DATA"]}},
        {"id": "D-binary", "case": "non-utf8", "expected": {"exit": 2, "finding_ids": ["HO-DATA"]}},
        {"id": "D-missing", "case": "missing-path", "expected": {"exit": 2, "finding_ids": ["HO-DATA"]}},
    ],
}
```

## 4. Observed verdicts (evidence)

All rows below are **observed on 2026-10-17**, not predicted: each mutant packet
was written to a temp file and graded by the real gate
(`tools/gates/handoff-packet-check.py`, sha256 `e2fa3223…b0ad575`). Command:
`python3 .scratch/o05/proto_exercise_cli.py --selftest` (transcript
`.scratch/o05/selftest-transcript.txt`); two-source replay transcript
`.scratch/o05/two-source-verify.txt`.

| Control | `examples/handoff-packet.sample.md` (heading form) | `examples/culture-d3/handoff.md` (row form) |
|---|---|---|
| positive | exit 0, ids [], `fields=16/16 glossary=20 findings=0` | exit 0, ids [], `fields=16/16 glossary=20 findings=0` |
| M-missing-field | exit 1, `HO-MISSING`, `fields=15/16` | exit 1, `HO-MISSING`, `fields=15/16` |
| M-blank-field | exit 1, `HO-EMPTY`, `fields=15/16` | exit 1, `HO-EMPTY`, `fields=15/16` |
| M-canon-claim | exit 1, `HO-CANON-CLAIM` | exit 1, `HO-CANON-CLAIM` |
| M-gloss-blank | exit 1, `HO-GLOSS-ETYM` | exit 1, `HO-GLOSS-ETYM` |
| M-dep-float | exit 1, `HO-DEP-FLOAT` | exit 1, `HO-DEP-FLOAT` |
| M-contract-ref | exit 1, `HO-CONTRACT-REF` | exit 1, `HO-CONTRACT-REF` |
| M-manifest-digest | exit 1, `HO-MANIFEST-DIGEST` | exit 1, `HO-MANIFEST-DIGEST` |

Malformed / CLI / fail-closed / matcher controls (single run each, 2026-10-17):

| Control | Observed |
|---|---|
| D-empty (0 bytes) | exit 2, `HO-DATA` |
| D-directory (a directory as the packet) | exit 2, `HO-DATA` |
| D-binary (bytes `23 20 74 ff fe …00 00`) | exit 2, `HO-DATA` |
| D-missing (nonexistent path) | exit 2, `HO-DATA` |
| C-unknown-flag (`--bogus-flag`) | exit 2, argparse message on stderr, no traceback |
| C-positional (`some/path.md`, also after `--selftest`) | exit 2, argparse message, no traceback |
| C-gate-missing (launch against a repo root without the gate) | `EX-E2E-GATE-MISSING`, exercise exits 2 |
| bogus-expectation (every plant compared against `exit 0 / []`) | flagged **7/7** |
| selftest-can-fail (positive expectation corrupted in-process) | 22/24 rows, `main(["--selftest"]) → 1` |

Selftest totals: **24/24 rows pass** in the two-source prototype (2 sources × 8
rows + 4 malformed + 2 CLI + 1 gate-missing + 1 bogus-expectation), exit 0. With
a single assembled source the tool's battery is 17 rows; keep both live sources
so form-independence stays proven.

Live-mode receipt (prototype stand-in source), three consecutive runs identical:

```
handoff-e2e: exit=0 findings=[] scan={'fields': 16, 'fields_expected': 16, 'glossary': 20, 'findings': 0} gate_sha256=e2fa3223b2aa stdout_sha256=7c5810479045
```

`--json` receipt: `{"schema": "kotodama-handoff-e2e-v1", "provenance": …,
"observed": {exit, ids, scan, stdout_sha256, gate_sha256}, "expected": {…},
"mismatches": [], "verdict": "pass"}`.

Pins at 2026-10-17T19:08:45-03:00 (`sha256sum`, run in the lane root):

```
e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575  tools/gates/handoff-packet-check.py
4e24bd3b887cf148155d89855d3c9eb842d3e325a4fa4302fccaa6c9d23dd712  examples/handoff-packet.sample.md
0d8d660bf9797d1c15da477f96ded75553a8d2ca7f04f75aa86a8a65e28fd2fc  examples/culture-d3/handoff.md
```

(The sample digest equals its row in `examples/culture-d3/expected.json` —
the sample has not moved under this round's work.)

## 5. Rejected controls and non-controls (recorded, not fabricated)

Three candidate defects were **rejected** after observation; recording them
prevents a later shard from "fixing" a non-defect into a red control:

1. **`baseline_bible_ref: none` alone is not a defect.** Mutating the sample's
   baseline value to a bare `none` still exits 0, because the packet carries a
   deliberate unbound-research declaration elsewhere and the gate's check
   accepts `none` in that case (`handoff-packet-check.py` §4 branch: `unbound`
   search over the document or the value). The HO-BASELINE probe needs the
   narrative declaration removed, not just the field value (the gate's own
   selftest does this by rebuilding the control packet). Not used as a control.
2. **`canon-claim` trips one ID, not two.** Replacing the `canon_standing` line
   leaves the H1 phrase "…research packet; not canonized" intact, so
   `HO-CANON-MARKER` stays satisfied and only `HO-CANON-CLAIM` fires. A
   marker-only plant (expected `{HO-CANON-MARKER}`) requires replacing the H1
   phrase too — the gate's selftest does exactly that; the battery here keeps
   the single-ID expectation deliberately, so the exercise proves the *claim*
   path, not both.
3. **The dep-float plant needs the negation carve-out neutralized.** The gate
   exempts `latest` when the same value documents the rule ("no floating
   `latest`" — the D3 handoff literally says this). Injecting a second `latest`
   without clearing that wording is a no-op *by design*; the mutation clears it
   first. This is a real gate behavior worth a sentence in the tool's docstring.

## 6. What is left to the integrator (not done here)

1. `assemble_packet` — supplied by the landed tool (§7); this fragment never
   touched `tools/exercise-handoff-e2e.py` (single writer, R11-O02..O05).
2. `--frozen`/baseline mode and `expected.json` — O14..O15; the reserved
   diagnostics above are the CLI's side of that contract. Per
   `gate-frozen-run-standard.md` §3/§4 the baseline must pin the graded bytes,
   gate sha256, revision, and the expected verdict. The landed tool places its
   baseline at `tools/gates/expected/handoff-exercise/r11/expected.json`
   (observed 2026-10-17 19:1x); that root is discovered by
   `tools/check-gate-battery.py`, whose baseline inspection maps each
   `expected.json` to one of the seven gate names — whether an eighth,
   non-gate baseline there flips the battery red is a live integration
   question for the O10..O13/battery owners, raised here rather than assumed
   either way.
3. Wire the tool into `reports/round-11/run-validation.py` (X03): count the
   tool's own `--selftest` exit and the live-mode verdict.
4. `--json --selftest` receipt shape (fragment proposal): `{"schema":
   "kotodama-handoff-e2e-selftest-v1", "passed", "total", "failures", "rows"}` —
   the run-validation author may pin `passed == total` and `failures == []`.

## 7. Integration observation (2026-10-17 19:07–19:12, added after §1–§6 were written)

While this fragment was being verified, the single-writer shard landed
`tools/exercise-handoff-e2e.py` (67,252 bytes, sha256
`38d1cba429d98af79a14201d6cdf44150dd935314f4536003253f8f576b4f4c1`, mtime
19:07). Two observations, with commands, recorded so the parent can reconcile
the fragment against the landed tool — this fragment is a *specification and
control library*, not the tool:

- **Live run: green.** `python3 tools/exercise-handoff-e2e.py --quiet` →
  `exercise-handoff-e2e: PASS — fields=16/16 glossary-entries=20 findings=0`,
  exit 0 (2026-10-17 19:1x). The claim's positive condition is met by the
  landed tool as of that minute.
- **Selftest: red.** `python3 tools/exercise-handoff-e2e.py --selftest` → exit 1,
  `AssertionError: ["evaluated: cannot hash
  examples/culture-d2/components/02-phonology.yml: [Errno 2] No such file or
  directory: …/.scratch/handoff-selftest-…/fixture/examples/culture-d2/
  components/02-phonology.yml"]` (2026-10-17 19:12, two runs). The fixture
  builder (`build_fixture_root`, tool lines ~1233–1252) copies only
  `FIXTURE_INPUTS` (the declared packet/projection sources, the gate and the
  two assemblers) into the temp mirror; the D2 component tree is not among
  them, so the component-digest step cannot hash its inputs *inside the
  fixture*. Candidate repairs (for the tool's owner, not applied here): add the
  D2 component tree to `FIXTURE_INPUTS`, or make the fixture mirror copy the
  components directory verbatim.
- **CLI divergence (intentional, flag-level).** The landed tool exposes
  `--selftest / --freeze DIR / --emit PATH / --quiet`; this fragment proposed
  `--selftest / --json / --keep`. `--freeze` subsumes the baseline tooling of
  O14..O15 and `--emit` the packet output; `--json`/`--keep` are advisory only
  and were not adopted. Verdict semantics (0 pass / 1 fail / 2 could-not-evaluate)
  agree.

Limits of this fragment, stated rather than implied: the mutants were exercised
against two live packets and the real gate on 2026-10-17 (transcripts in §4);
they were not re-run against the landed tool's assembled packet, and the
scan-count expectations carry the integration-critical drift note in §1.
Nothing here is committed; no git operation was performed.

FILES: reports/round-11/handoff/shard-cli.md | SUMMARY: R11-O05 fragment — verified CLI contract (0/1/2, EX-* diagnostics) + form-aware 7-mutant negatives battery, 24/24 selftest rows exact on both live source shapes against the real gate.
