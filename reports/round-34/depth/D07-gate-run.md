- Seat: D07 | executor | claim D | date 2026-10-19 | baseline da68a6d

## Mission (targets.json, seat D07, verbatim)

"Gate the draft: run handoff-packet-check.py against the D05 draft (extract it
to .scratch first); report fields/glossary/findings; iterate the draft until
16/16 + 20/20 + 0."

## Status: the draft to gate does not exist yet — the gate run on it is owed

`reports/round-34/depth/D05-packet-draft.md` was absent when this seat ran
(`find reports/round-34 -type f` returned 44 files including D02-render.md,
D03-ledger-rows.md, D04-oq-glossary.md, D08-links-uncertainty.md, K01, K02 —
and no `D05-*`, no `D01-*`; that count is the state at my dispatch scan, later
landings are recorded under `## Owed`). Per the missing-dependency rule this
seat did every part that does not require D05, and filed the pipeline that
performs the gating in one command once D05 lands (§3). **No gate verdict on the
r7 draft is claimed here.**

Two things this seat could and did verify in the meantime:

1. the gate instrument is healthy and the lane's green shape is exact (`§1`);
2. the rewrite class D03/D04 will apply to the r6 prose is envelope-safe — it
   keeps the gate at 16/16 + 20/20 + 0 (`§7`).

## §1 What "16/16 + 20/20 + 0" is, and that the instrument is green

The triple is the gate's own scan line — `fields`, `glossary-entries`,
`findings` — printed as `INFO scan:` on every run
(`tools/gates/handoff-packet-check.py:591`), and repeated by the e2e receipt
(`reports/round-30/handoff/declared-in-r6/run.log:3`, `…/freeze.txt:4`).

| command (2026-10-19, `TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`) | observed |
|---|---|
| `python3 tools/gates/handoff-packet-check.py --selftest` | exit 0 — "selftest: OK — fixture findings 11 across 9 ids (HO-BASELINE, HO-CANON-CLAIM, HO-CANON-MARKER, HO-CONTRACT-REF, HO-DEP-FLOAT, HO-EMPTY, HO-GLOSS-ETYM, HO-MANIFEST-DIGEST, HO-MISSING); clean control exit 0; probes cover canon, baseline, dependency, contract_ref and glossary vocabulary; malformed inputs exit 2; CLI verified from another cwd" |
| `python3 tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md` | exit 0 — `INFO scan: fields=16/16 glossary-entries=20 findings=0` |
| `python3 tools/gates/handoff-packet-check.py .scratch/d02/rendered/packet.md` (the D02 render, sha256 `6ced88ad…`) | exit 0 — `INFO scan: fields=16/16 glossary-entries=20 findings=0` |

So the current default pair is shape-green while carrying the six stale figures
(§6): **the gate cannot see stale prose.** Its own docstring says so — "Scope
that stays outside this kernel: judging whether the declared checks were really
run, whether digests match bytes … and whether the payload content is any good"
(`tools/gates/handoff-packet-check.py:83-89`). The stale-figure census is the
D13/D17/D18/D20 leg; this gate run must never be cited as evidence that the
draft's numbers are live, and the census must never be cited for the envelope.

## §2 Live values the r7 packet prose must carry (measured from bytes, not inferred)

| metric | live value | source |
|---|---|---|
| typed labels (D4 projection) | **82** | `examples/culture-d4/typed-labels.d4.yml:46` |
| labels_by_kind | native-form **64** / translated-label **12** / borrowed-strata **6** | `examples/culture-d4/typed-labels.d4.yml:35-38` |
| findings_total / findings_hold_or_fail / label_findings_fail | **12** / **12** / **0** | `…typed-labels.d4.yml:31-33` (also `label_findings_hold: 12` at `:34`) |
| conflicts | **0** | `…typed-labels.d4.yml:30` |
| rank_quarantine_handles | **0** | `…typed-labels.d4.yml:40` |
| rank_rules_unresolved_items | **0** | `…typed-labels.d4.yml:44` |
| reconciliation_records | **6** | `…typed-labels.d4.yml:45` |
| committed hold set | hold **12** / note **0** / fail **0**, all twelve rows `D2L-FORM-UNRESOLVED` (GAR-01…06 and LEX-GAR-01…06) | `examples/culture-d4/expected-holds.json` `counts` + `holds` rows |

Independent witnesses for the same numbers, both exit 0 on the live tree:
`python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml`
→ "examples/culture-d4/typed-labels.d4.yml: byte-identical deterministic
projection"; `python3 tools/gates/typed-pipeline-gate.py
examples/culture-d4/packet.d4.yml` → "summary: 20/20 legs passed" (its
`L3-holds` leg is the emitted-equals-committed hold-set equality). Digests at
measurement: `typed-labels.d4.yml` = `c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e`
(= the r6 packet's own A-30 pin, `packet.md:68`); `expected-holds.json` =
`e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3` (= A-31 pin,
`packet.md:69`).

Invocation caution for the D block: `d4-typed-labels-check-gate.py` takes the
**projection** path; passing `examples/culture-d4/packet.d4.yml` prints
"examples/culture-d4/packet.d4.yml differs from the deterministic projection"
and exits 1 (`tools/gates/d4-typed-labels-check-gate.py:8-14` documents the
peer invocation). That red is an operator error, not drift.

## §3 The extract-and-gate pipeline (run this the moment D05 lands)

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
mkdir -p .scratch/d07
# 1. write the embedded tool (next block) to .scratch/d07/extract_and_gate.py
# 2. gate the D05 draft:
python3 -B .scratch/d07/extract_and_gate.py reports/round-34/depth/D05-packet-draft.md \
    --out .scratch/d07/d05.packet.md
```

Expected green output (this exact shape was reproduced end-to-end on the r6
bytes wrapped in a D05-shaped fragment, §5):

```
EXTRACT fragment=reports/round-34/depth/D05-packet-draft.md mode=fenced block-lines=… blocks-used=1 bytes=… sha256=…
EXTRACT wrote .scratch/d07/d05.packet.md
GATE-OUT INFO scan: fields=16/16 glossary-entries=20 findings=0
VERDICT exit=0 fields=16/16 glossary=20/20 findings=0 expected fields=16/16 glossary=20/20 findings=0 -> OK
```

Variants: `--join` when the draft is chunked across doc fences; `--block N`
after reading the printed `CANDIDATE` lines when the fragment holds several
packet-shaped fences; `--expect F/G/N` to check a different declared shape.
Exit codes: 0 green, 1 findings-or-mismatch, 2 could-not-extract (no verdict is
invented; nothing is written).

**Always gate the extracted bytes, never the fragment**: the gate reads any
`- field: value` list item or `| field | value |` row anywhere in the document
it is given (`tools/gates/handoff-packet-check.py:274-314`), so a fragment whose
prose happens to name all sixteen fields can mask a draft that drops one.

Tool (locates the repo by walking up to the gate, so it runs from any depth; also drafted for a durable home — integrator's call; before → after:
`tools/harness/extract_and_gate.py` **does not exist** → land this file at
`tools/harness/extract_and_gate.py` unchanged):

````python
#!/usr/bin/env python3
"""extract_and_gate — pull a handoff-packet draft out of a seat fragment and
judge it with tools/gates/handoff-packet-check.py.

Usage:
    python3 extract_and_gate.py <fragment.md> [--out PATH] [--block N]
    python3 extract_and_gate.py <fragment.md> --join          # chunked drafts
    python3 extract_and_gate.py <fragment.md> --whole-body
    python3 extract_and_gate.py --selftest

The lane's declared expectation for the v3 packet is fields=16/16
glossary-entries=20 findings=0 (--expect 16/20/0, the default). Exit 0 only
when the gate exits 0 AND the scan line equals the expectation; 1 when the
gate reports findings or the scan mismatches; 2 when no draft could be
extracted (nothing is written and no verdict is invented).

Block selection, stated so it cannot be mistaken:
  * default      the single fenced block whose first non-blank line is a
                 level-1 heading, longest first if several qualify;
  * --join       every doc fence (empty/markdown/md/text info string) in file
                 order, concatenated; the joined bytes must still open with a
                 level-1 heading or the run is refused;
  * --whole-body the fragment body itself, only when it opens with a heading.
Every candidate block is printed with its size so a wrong pick is visible.
"""

from __future__ import annotations

import argparse
import hashlib
import importlib.util
import re
import subprocess
import sys
import tempfile
from pathlib import Path

def _find_repo():
    """The repo root is the nearest ancestor holding the gate this tool drives."""
    here = Path(__file__).resolve().parent
    for candidate in (here, *here.parents):
        if (candidate / "tools" / "gates" / "handoff-packet-check.py").is_file():
            return candidate
    raise SystemExit(f"could not locate the repo root above {here}: tools/gates/handoff-packet-check.py not found")


REPO = _find_repo()
GATE = REPO / "tools" / "gates" / "handoff-packet-check.py"
DEFAULT_EXPECT = (16, 20, 0)
DOC_INFO = {"", "markdown", "md", "text", "plain", "plaintext"}
SCAN_RE = re.compile(r"^INFO scan: fields=(\d+)/(\d+) glossary-entries=(\d+) findings=(\d+)$", re.M)

EXIT_OK, EXIT_FINDINGS, EXIT_UNEXTRACTABLE = 0, 1, 2


class ExtractionError(Exception):
    pass


def find_fenced_blocks(lines):
    """[{start, end, width, info, body}] for every fenced block, in file order."""
    blocks = []
    index = 0
    while index < len(lines):
        opener = re.match(r"^\s{0,3}(`{3,})\s*([A-Za-z0-9_+-]*)\s*$", lines[index])
        if not opener:
            index += 1
            continue
        width = len(opener.group(1))
        info = opener.group(2).lower()
        body = []
        cursor = index + 1
        while cursor < len(lines):
            closer = re.match(r"^\s{0,3}(`{3,})\s*$", lines[cursor])
            if closer and len(closer.group(1)) >= width:
                break
            body.append(lines[cursor])
            cursor += 1
        blocks.append({"start": index + 1, "end": cursor + 1, "width": width, "info": info, "body": body})
        index = cursor + 1
    return blocks


def _opens_with_heading(body):
    first = next((line for line in body if line.strip()), "")
    return bool(re.match(r"^\s{0,3}#\s+\S", first))


def packet_candidates(blocks):
    """Blocks that open with a level-1 heading, longest first."""
    candidates = [block for block in blocks if _opens_with_heading(block["body"])]
    candidates.sort(key=lambda block: -sum(len(line) for line in block["body"]))
    return candidates


def report_block(rank, block):
    size = len("\n".join(block["body"]).encode("utf-8"))
    print(f"CANDIDATE {rank}: block-lines={block['start']}-{block['end']} fence={block['width']} "
          f"info={block['info'] or '(none)'} bytes={size} opens-heading={_opens_with_heading(block['body'])}")


def extract(fragment_text, block_index=None, whole_body=False, join=False):
    lines = fragment_text.splitlines()
    blocks = find_fenced_blocks(lines)
    for rank, block in enumerate(blocks, 1):
        report_block(rank, block)

    if join:
        doc_blocks = [block for block in blocks if block["info"] in DOC_INFO]
        if not doc_blocks:
            raise ExtractionError("--join given but the fragment has no doc fence (empty/markdown/md/text info string)")
        print(f"JOIN using {len(doc_blocks)} doc fence(s) of {len(blocks)} fence(s), file order")
        body = [line for block in doc_blocks for line in block["body"]]
        if not _opens_with_heading(body):
            raise ExtractionError("--join built bytes that do not open with a level-1 heading — refuse rather than guess")
        return "\n".join(body) + "\n", {
            "mode": "joined", "start": doc_blocks[0]["start"], "end": doc_blocks[-1]["end"],
            "candidates": len(doc_blocks),
        }

    candidates = packet_candidates(blocks)
    if block_index is not None:
        if not 1 <= block_index <= len(blocks):
            raise ExtractionError(f"--block {block_index} out of range: the fragment has {len(blocks)} fence(s)")
        chosen = blocks[block_index - 1]
    elif candidates:
        chosen = candidates[0]
    elif whole_body:
        first = lines[0] if lines else ""
        if not re.match(r"^\s{0,3}#\s+\S", first):
            raise ExtractionError("--whole-body given but the fragment does not start with a level-1 heading")
        return fragment_text, {"mode": "whole-body", "start": 1, "end": len(lines), "candidates": 0}
    else:
        raise ExtractionError(
            "no fenced block opens with a level-1 heading — pass --join for a chunked draft, or --block N to "
            "pick a specific fence, or --whole-body only when the fragment body is itself the packet")
    return "\n".join(chosen["body"]) + "\n", {
        "mode": "fenced", "start": chosen["start"], "end": chosen["end"], "candidates": len(candidates),
    }


def run_gate(packet_path):
    completed = subprocess.run(
        [sys.executable, str(GATE), str(packet_path)],
        capture_output=True, text=True, cwd=str(REPO),
    )
    return completed.returncode, completed.stdout, completed.stderr


def judge(exit_code, stdout, expect):
    match = SCAN_RE.search(stdout)
    if not match:
        return None, f"scan line absent (gate exit {exit_code}, no INFO scan line)"
    got = (int(match.group(1)), int(match.group(3)), int(match.group(4)))
    if exit_code != 0:
        return got, f"gate exit {exit_code} (findings present)"
    if got != expect:
        return got, f"scan {got} != expected {expect}"
    return got, "OK"


def gate_fragment(fragment_path, out_path=None, block_index=None, expect=DEFAULT_EXPECT, whole_body=False,
                  join=False):
    text = Path(fragment_path).read_text(encoding="utf-8")
    try:
        packet, how = extract(text, block_index, whole_body, join)
    except ExtractionError as exc:
        print(f"EXTRACT-REFUSED fragment={fragment_path} reason={exc}")
        return EXIT_UNEXTRACTABLE
    out_path = Path(out_path) if out_path else Path(str(fragment_path) + ".packet.md")
    out_path.write_text(packet, encoding="utf-8")
    digest = hashlib.sha256(packet.encode("utf-8")).hexdigest()
    print(f"EXTRACT fragment={fragment_path} mode={how['mode']} block-lines={how['start']}-{how['end']} "
          f"blocks-used={how['candidates']} bytes={len(packet.encode('utf-8'))} sha256={digest}")
    print(f"EXTRACT wrote {out_path}")
    exit_code, stdout, stderr = run_gate(out_path)
    for line in stdout.splitlines():
        print(f"GATE-OUT {line}")
    if stderr.strip():
        print(f"GATE-ERR {stderr.strip()}")
    got, verdict = judge(exit_code, stdout, expect)
    expected = f"fields={expect[0]}/{expect[0]} glossary={expect[1]}/{expect[1]} findings={expect[2]}"
    if got is None:
        print(f"VERDICT exit={exit_code} {verdict}; expected {expected}")
        return EXIT_UNEXTRACTABLE
    print(f"VERDICT exit={exit_code} fields={got[0]}/16 glossary={got[1]}/20 findings={got[2]} "
          f"expected {expected} -> {verdict}")
    return EXIT_OK if verdict == "OK" else EXIT_FINDINGS


def load_control_packet():
    spec = importlib.util.spec_from_file_location("handoff_packet_check", GATE)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module.CONTROL_PACKET


def wrap(packet_text, prose_head="# D-fixture fragment\n\nDraft below.\n\n", tail="\n\ntrailing prose\n"):
    return prose_head + "```markdown\n" + packet_text.rstrip("\n") + "\n```" + tail


def chunked(packet_text, split=400):
    """Split at a line boundary: the join is byte-faithful and reconstructs the packet."""
    lines = packet_text.rstrip("\n").splitlines()
    head, tail = lines[:split], lines[split:]
    return ("# D-fixture fragment (chunked draft)\n\npart 1:\n\n```markdown\n" + "\n".join(head)
            + "\n```\n\npart 2 (continues):\n\n```markdown\n" + "\n".join(tail) + "\n```\n")


def chunked_midrow(packet_text, split=400):
    """Split mid-line: the join cannot repair the seam, so the gate must go red."""
    body = packet_text.rstrip("\n")
    return ("# D-fixture fragment (seam-damaged chunked draft)\n\npart 1:\n\n```markdown\n" + body[:split]
            + "\n```\n\npart 2 (continues):\n\n```markdown\n" + body[split:] + "\n```\n")


def selftest():
    control = load_control_packet()
    toy = (16, 2, 0)  # the gate's control packet carries 2 glossary rows
    drop_request_ref = control.replace("| request_ref | brief F-T02 (synthetic; illustrative only) |\n", "")
    blank_request_ref = control.replace("| request_ref | brief F-T02 (synthetic; illustrative only) |",
                                        "| request_ref |  |")
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        tmpdir = Path(tmp)
        cases = [
            ("green-control-wrapped", wrap(control), toy, {}, EXIT_OK),
            ("red-dropped-request_ref", wrap(drop_request_ref), toy, {}, EXIT_FINDINGS),
            ("red-blank-request_ref-value", wrap(blank_request_ref), toy, {}, EXIT_FINDINGS),
            ("green-second-non-packet-fence", wrap(control) + "\n```text\n# not a packet\n```\n", toy, {}, EXIT_OK),
            ("refuse-no-packet-fence", "# fragment\n\n```python\nprint(1)\n```\n", toy, {}, EXIT_UNEXTRACTABLE),
            ("green-whole-body-flag", control, toy, {"whole_body": True}, EXIT_OK),
            ("refuse-glossary-mismatch", wrap(control), (16, 20, 0), {}, EXIT_FINDINGS),
            ("green-join-chunked-draft", chunked(control, 25), toy, {"join": True}, EXIT_OK),
            ("red-join-seam-mid-row", chunked_midrow(control, 400), toy, {"join": True}, EXIT_FINDINGS),
        ]
        for name, text, expect, options, want in cases:
            fragment = tmpdir / f"{name}.md"
            fragment.write_text(text, encoding="utf-8")
            print(f"--- selftest case {name} (want exit {want}) ---")
            got = gate_fragment(fragment, tmpdir / f"{name}.packet.md", expect=expect, **options)
            if got != want:
                failures.append(f"{name}: want exit {want}, got {got}")
    if failures:
        print("extract_and_gate selftest: FAILED — " + "; ".join(failures))
        return 1
    print("extract_and_gate selftest: OK — 9/9 cases. The fenced green control extracts and gates green "
          "(exit 0); a dropped field and a blank field value gate red (exit 1); a second non-packet fence does "
          "not divert selection; a fragment with no packet-shaped fence is refused (exit 2, no verdict invented); "
          "--whole-body is required to read a bare packet body; a glossary-count shortfall against the lane "
          "expectation is a mismatch even though the gate itself exits 0; a chunked draft split at a line "
          "boundary gates green under --join, while the same draft split mid-row stays red under --join because "
          "joining is byte-faithful and cannot repair a damaged seam")
    return 0


def parse_expect(text):
    match = re.fullmatch(r"(\d+)/(\d+)/(\d+)", text.strip())
    if not match:
        raise argparse.ArgumentTypeError("--expect wants FIELDS/GLOSSARY/FINDINGS, e.g. 16/20/0")
    return tuple(int(part) for part in match.groups())


def main(argv=None):
    parser = argparse.ArgumentParser(prog="extract_and_gate.py")
    parser.add_argument("fragment", nargs="?")
    parser.add_argument("--out")
    parser.add_argument("--block", type=int, default=None)
    parser.add_argument("--expect", type=parse_expect, default=DEFAULT_EXPECT,
                        help="expected FIELDS/GLOSSARY/FINDINGS scan (default 16/20/0)")
    parser.add_argument("--whole-body", action="store_true",
                        help="treat the fragment body itself as the packet (no fenced block)")
    parser.add_argument("--join", action="store_true",
                        help="concatenate every doc fence in file order (chunked drafts)")
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args(argv)
    if args.selftest:
        return selftest()
    if not args.fragment:
        parser.error("a fragment path is required unless --selftest is used")
    return gate_fragment(args.fragment, args.out, args.block, args.expect, args.whole_body, args.join)


if __name__ == "__main__":
    sys.exit(main())
````

Its own selftest is 9/9 green (`python3 -B .scratch/d07/extract_and_gate.py --selftest`,
exit 0, printed at the end):

> extract_and_gate selftest: OK — 9/9 cases. The fenced green control extracts
> and gates green (exit 0); a dropped field and a blank field value gate red
> (exit 1); a second non-packet fence does not divert selection; a fragment with
> no packet-shaped fence is refused (exit 2, no verdict invented); --whole-body
> is required to read a bare packet body; a glossary-count shortfall against the
> lane expectation is a mismatch even though the gate itself exits 0; a chunked
> draft split at a line boundary gates green under --join, while the same draft
> split mid-row stays red under --join because joining is byte-faithful and
> cannot repair a damaged seam.

## §4 Iteration playbook: finding id → the fix (gate ids, exit codes)

Finding ids and levels are defined at `tools/gates/handoff-packet-check.py:49-70`;
the required field list at `:122-139`; the placeholder vocabulary at `:144-160`;
licensed etymology statuses at `:174`.

| finding | what it means for the draft | fix in the draft |
|---|---|---|
| `HO-DATA` (HOLD, exit 2) | no level-1 heading — not a packet document | the fenced block must contain the packet bytes verbatim, starting at `# …` |
| `HO-MISSING` (FAIL) | one finding per absent §4 field | add the field as a `## field` heading, a `- field: value` item, or a `| field | value |` row |
| `HO-EMPTY` (FAIL) | present but blank/placeholder; `to-verify`, `unknown`, `-`, `TODO`, `n/a` all count as absent evidence | supply real content; "unknowns are not blank cells" (§11) |
| `HO-BASELINE` (REVIEW) | `baseline_bible_ref: none` without an unbound-research declaration | keep the lore-bible baseline ref, or declare the packet deliberately unbound |
| `HO-CONTRACT-REF` (REVIEW) | `contract_ref` missing revision (`X.Y.Z`) or hex digest | cite `kotodama-lore-adjacency 1.0.0 sha256:5f4c02bf…` as the r6 packet does (`packet.md:103`) |
| `HO-MANIFEST-DIGEST` (REVIEW) | `artifact_manifest` names no file digest | keep the per-artifact sha256 column |
| `HO-DEP-FLOAT` (REVIEW) | `dependency_manifest` floats `latest` | pin exact versions; the "no floating latest" wording is allowed |
| `HO-CANON-MARKER` (FAIL) | the `not canonized` / `not yet canonized` marker is gone | keep the §8.7 wording |
| `HO-CANON-CLAIM` (FAIL) | producer-side canon certification | never pair `approved/established/ratified/final/granted` with `canon` in any edited cell — see the live trap in §5 |
| `HO-GLOSS-ETYM` (FAIL, once per table if the column is missing) | a glossary row carries no etymology, or its stated status is outside {attested, reconstructed, constructed, contested, unknown} | keep the 20-row inline payload with `status: constructed|unknown` per row (`packet.md:314-335`) |

## §5 Controls run on this claim (each re-runnable, outputs quoted)

- **green, real bytes**: the r6 packet bytes wrapped in a D05-shaped fragment
  extract to sha256 `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb`
  (equal to the filed `freeze.txt:2` packet digest) and gate green —
  `VERDICT exit=0 … -> OK`.
- **red, dropped field**: removing the `| request_ref | … |` row yields
  `FINDING HO-MISSING: FAIL — required field/section request_ref absent`,
  `fields=15/16 … findings=1`, exit 1.
- **red, blank value**: blanking a required value yields `HO-EMPTY`, exit 1.
- **trap, live in rewritten cells**: appending "… the hold set is now
  `established as canon` for the D4 drill" to a rewritten row yields
  `FINDING HO-CANON-CLAIM: FAIL — producer-side canon certification at line 149:
  'established as canon'`, exit 1. Any D03/D04 rewrite must avoid this pairing.
- **seam**: a draft chunked mid-row stays red under `--join`
  (`fields=13/16 … findings=3`) — joining cannot repair a damaged seam, so a
  chunked draft must be split at line boundaries.
- **scope**: the r6 packet itself — carrying every stale figure — gates green
  (§1, §6). This is the red-team control against using the gate as a
  stale-number audit.

## §6 Census of the sites the r7 draft must change, and two audit traps

Stale sites in `reports/round-30/handoff/declared-in-r6/packet.md` (line-quoted
by the census command in Citations): `:148` D4-CL05 (`typed_labels 74`,
`native-form 56`, `findings_total 16`, `findings_hold_or_fail 15`, and the
statement "types 74 labels — 56 native-form … carries 16 findings of which 15
are hold-or-fail"); `:149` D4-CL06 (`hold 15, note 1, fail 0`, "15 holds, 1 note
and 0 fails", "three `D2L-RANK` holds, plus one `D2L-RANK` note"); `:150`
D4-CL07 (`conflicts (4)`, `quarantine handles (3)`, "carry four conflicts");
`:152` D4-CL09 (`rank_rules_unresolved_items 13`, `rank_quarantine_handles 3`,
`conflicts 4` in the link refs, the digits `13 … 3 … 4` in the statement, **and**
the spelled-out "the thirteen unresolved rank items, three quarantine handles
and four conflicts" in the open clause); `:307` OQ-V3-05 ("twelve form holds +
three rank holds + one note, thirteen unresolved rank items, three quarantine
handles and four conflicts").

The packet already contradicts itself: `:68` (A-30: "82 labels (64 native-form /
12 translated-label / 6 borrowed-strata), 12 findings, 0 unresolved rank items")
and `:69` (A-31: "12 holds / 0 note / 0 fail") agree with the live bytes while
`:148-152` and `:307` do not.

Two traps for whoever does the rewrite or the census (both cost me a false red
or a false green while building the pipeline):

- **Trap 1 — spelled-out forms.** The same figures appear as words: "thirteen
  unresolved rank items, three quarantine handles and four conflicts"
  (`packet.md:152`, `:307`). A digits-only sweep (and a digits-only rewrite)
  leaves `:152` stale; after my nine-pair digit rewrite the residual census still
  reports conflicts/quarantine/unresolved hits at `:152`. Any "zero stale
  figures" test must search both forms.
- **Trap 2 — D2 lookalikes.** `13 / 3 / 4` and `16 / 15` are **live and correct
  for the D2 projection** (`examples/culture-d2/typed-labels.d2.yml:29-46`
  coverage block: `conflicts 4`, `findings_total 16`, `findings_hold_or_fail 15`,
  `label_findings_fail 2`, `label_findings_hold 10`, `rank_quarantine_handles 3`,
  `rank_rules_unresolved_items 13`, `reconciliation_records 10`,
  `typed_labels 58`) and are carried by `packet.md:49`, `:129`, `:130`, `:266`,
  `:267`, `:284`, `:301`. A tree-wide grep for the six stale figures therefore
  reports those rows as hits that must **not** be "fixed": the census has to be
  scoped to D4-context rows (claims D4-CL05…D4-CL09, OQ-V3-05). Digits like `56`
  are also noise (`:48`, `:77`, `:94`, `:114` — digests and byte counts).

## §7 Pre-validation of the D03/D04 rewrite class (green, and its gap)

Nine exact replacement pairs (old → new) covering every digit-form stale figure
at `:148`, `:149`, `:150`, `:152`, `:307` were each asserted to occur exactly
once in the r6 bytes, applied to a scratch copy, and gated
(`.scratch/d07/rewrite_probe.py`): all nine pairs `occurrences=1 OK`; the
rewritten copy (sha256 `0a8ef62dd636e7c345ba9f0750709d24bc59d247c7d22cddba4650fe8fb9aba3`)
gates `INFO scan: fields=16/16 glossary-entries=20 findings=0`, exit 0. **The
rewrite class cannot break the envelope**, and the link tokens it keeps
(`#coverage`, `#labels_by_kind`, `#stats`, `#typed_labels`) all exist in the
live file (`typed-labels.d4.yml:29`, `:35`, `:2865`, `:46`) so the links leg is
not disturbed by the number change.

Tenth pair, owed to D03/D04 (it closes Trap 1; my nine-pair run left this text
in place):

- old: `the thirteen unresolved rank items, three quarantine handles and four conflicts are inherited D2 normalization residuals and none of them is promoted by this packet`
- new: `no unresolved rank item, quarantine handle or conflict remains in that block, and none of them is promoted by this packet`

Two content points this gate run cannot settle, flagged for D03/D04/D05 rather
than decided here:

- D4-CL06's row-kind sentence ("three `D2L-RANK` holds, plus one `D2L-RANK`
  note") must be re-worded to the live hold list, which now contains twelve
  `D2L-FORM-UNRESOLVED` rows and no `D2L-RANK` row or note (§2). My pair text
  for `:149` is a draft.
- D02 measured that the render from live bytes reproduces the filed r6 packet
  **exactly** (`packet_sha256: 6ced88ad…`, `reports/round-34/depth/D02-render.md`
  §1-§2; independently re-gated here in §1), so the stale figures are produced
  by the renderer's own sources rather than by a stale filing. An r7 revision
  whose prose is edited only in `packet.md` must say how it becomes the frozen
  share of a deterministic render (source-level change vs documented re-freeze);
  the r6 receipt shows the precedent — `freeze.txt:8` records a re-freeze
  `ec30b11f… -> 6ced88ad…`.

## §8 What this fragment does not claim

- **No gate verdict on the r7 draft** — it does not exist (§Status).
- No claim that the D05 draft's own numbers are live: that is the census leg
  (D13/D17/D18/D20/R01), not this gate (§1, §6).
- No iterate-until-green run against a draft: the pipeline is ready and its
  controls are green, but the loop has no input yet.
- Byte preservation was checked only incidentally: `git status --porcelain`
  reported `?? reports/round-34/` and `git diff --stat` was empty after all my
  work; the full preservation receipt belongs to D11/D20.

## Owed

- `reports/round-34/depth/D05-packet-draft.md` — the draft to gate. Until it
  lands, the mission's iterate-to-green gate run cannot be produced; whoever
  lands D05 (D05, D15, D16, or the integrator) runs §3 and, on red, walks §4.
- Upstream of D05: nothing is blocked there any more — `D01-layout.md`,
  `D02-render.md`, `D03-ledger-rows.md`, `D04-oq-glossary.md` are all present at
  my close. `D05-packet-draft.md` itself is still absent at my close
  (`ls reports/round-34/depth/`); D20's independent poll at 04:12 records the
  same absence (`reports/round-34/depth/D20-verify-preservation.md:20`), and D16
  lists it among the fragments still missing at its close
  (`reports/round-34/depth/D16-gap-fill.md:373`).
- Optional durable landing of the embedded tool at
  `tools/harness/extract_and_gate.py` (integrator applies; the before state is
  "file does not exist").
- The tenth replacement pair in §7 is a draft for D03/D04 to accept or re-word.

## Citations

Files (paths relative to the repo root):

- `tools/gates/handoff-packet-check.py` — `:49-70` finding ids/levels, `:83-89`
  scope outside the kernel, `:117-119` exit codes, `:122-139` FIELD_NAMES,
  `:144-160` PLACEHOLDERS, `:174` ETYM_STATUSES, `:274-314` collect_fields,
  `:591` the `INFO scan` line, `:686-855` selftest
- `reports/round-30/handoff/declared-in-r6/packet.md` — `:68` A-30, `:69` A-31,
  `:103` contract_ref, `:130` D2-CL02, `:148` D4-CL05, `:149` D4-CL06, `:150`
  D4-CL07, `:152` D4-CL09, `:266-267`, `:284`, `:297-308` open_questions, `:301`
  OQ-V2-03, `:307` OQ-V3-05, `:314-335` glossary payload; sha256
  `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb`
- `reports/round-30/handoff/declared-in-r6/{run.log,freeze.txt,expected.json}` —
  `run.log:3`, `freeze.txt:2,:4,:8`
- `examples/culture-d4/typed-labels.d4.yml` — `:29` coverage, `:30` conflicts,
  `:31-34` findings/label findings, `:35-38` labels_by_kind, `:40`
  rank_quarantine_handles, `:44` rank_rules_unresolved_items, `:45`
  reconciliation_records, `:46` typed_labels, `:2865` stats; sha256
  `c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e`
- `examples/culture-d4/expected-holds.json` — `counts` + 12 `holds` rows; sha256
  `e6ae9828d6c82aa6e14431a02840ad565f9f7c30a660afcbed1b1079166bfba3`
- `examples/culture-d2/typed-labels.d2.yml` — coverage block (D2 lookalikes)
- `tools/gates/d4-typed-labels-check-gate.py:8-14`; `tools/gates/typed-pipeline-gate.py`
- `tools/exercise-handoff-e2e.py:1933-1934` (V3_BASELINE_DEFAULT /
  V3_FROZEN_DIR_DEFAULT still point at `declared-in-r6`)
- `reports/round-34/depth/D02-render.md` §1-§2 (render == filed r6 bytes)
- scratch (transient, reproducible via the embedded tool):
  `.scratch/d07/extract_and_gate.py` sha256
  `265526270fb69f07be38bcd15e790f901c5161b9143d186f8b0b5779462ee675`,
  `.scratch/d07/rewrite_probe.py` sha256
  `f7185b90c273aa48f65399d0f1b877c8dcc922e4f581d49e123a8590e1bca627`,
  `.scratch/d07/rewritten-live-numbers.md` sha256
  `0a8ef62dd636e7c345ba9f0750709d24bc59d247c7d22cddba4650fe8fb9aba3`,
  `.scratch/d07/rewritten-canon-trap.md` sha256
  `8c2da82625d02155e1606b2f1ee6586c1123859c7de869d03da53ef34b02f99c`

Commands run by this seat (2026-10-19, `TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`; no filed `run-validation.py` was executed):

- `python3 tools/gates/handoff-packet-check.py --selftest` → exit 0
- `python3 tools/gates/handoff-packet-check.py reports/round-30/handoff/declared-in-r6/packet.md` → exit 0, `fields=16/16 glossary-entries=20 findings=0`
- `python3 tools/gates/handoff-packet-check.py .scratch/d02/rendered/packet.md` → exit 0, same scan
- `python3 tools/gates/d4-typed-labels-check-gate.py examples/culture-d4/typed-labels.d4.yml` → exit 0; with `…packet.d4.yml` → exit 1 (operator error, §2)
- `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` → exit 0, `summary: 20/20 legs passed`
- `sha256sum examples/culture-d4/{typed-labels.d4.yml,expected-holds.json}` → digests quoted in §2
- `python3 -B .scratch/d07/extract_and_gate.py --selftest` → exit 0, 9/9 cases
- `python3 -B .scratch/d07/extract_and_gate.py .scratch/d07/fx-d05-shaped-realbytes.md --out .scratch/d07/fx-realbytes.packet.md` → exit 0, extract sha256 `6ced88ad…`, `VERDICT … -> OK` (controls quoted in §5)
- `python3 .scratch/d07/rewrite_probe.py` → 9/9 pairs unique, rewritten copy gates exit 0, canon trap exits 1, residual census quoted in §6
- `grep -n`/`sed -n`/`sha256sum` probes for the census, key lines and digests quoted in §2, §6
- `git status --porcelain` → `?? reports/round-34/` only; `git diff --stat` → empty
- `find reports/round-34 -type f` → the 44-file listing quoted in §Status
