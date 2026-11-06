#!/usr/bin/env python3
"""Check that each Gate-table row names the capture file its sha256 refers to.

Round 97 closure routed defect 3 (`corpus/lessons/round-97-verifier-spotcheck.md`
§5 item 3): Gate-table hash column did not name the capture file each hash
refers to (S993's hash is the PDF's while the quote is counted in the .txt).
This checker makes that row shape checkable.

What it reads
  * Only the `## Gate` section of the lesson: from the `## Gate` heading up
    to (not including) the next `## ` heading.
  * Only markdown table rows (`| ... |`) in that section. A row is in scope
    when its first cell matches `S\\d+` (after trimming markup) and some cell
    carries a sha256 token (full 64-hex, or the round-97 truncated
    16-hex + ellipsis legacy form). Separator rows (`|---|`) are skipped.

Hash resolution
  * A full 64-hex token is compared exactly against the named file's sha256.
  * A truncated 16-hex legacy token is compared as a prefix: the file passes
    iff its sha256 starts with the token; otherwise it is a mismatch. Legacy
    round-97 rows are normally reported CAPTURE-MISSING before any hash
    comparison (they have no capture-file column).

Capture file
  * The header column named `capture file` (case-insensitive, whitespace-
    normalised) carries a bare file name resolved under the evidence dir.
    Values that are paths, or empty, are treated as absent-file findings
    when the name is not a bare basename.

Findings (one line per in-scope row)
  * CAPTURE-MISSING  — the table has no `capture file` header column, or the
    row's cell for it is empty.
  * CAPTURE-ABSENT   — the named file does not exist under the evidence dir.
  * SHA-MISMATCH     — the file exists but its sha256 differs from the row
    hash (exact for 64-hex; prefix for truncated legacy tokens).
  * OK               — all of the above pass.

Output
  * stdout: `ROW <id> <OK|CAPTURE-MISSING|CAPTURE-ABSENT|SHA-MISMATCH> <file>`
    per row (`-` for the file when missing), then
    `GATE-CAPTURES: <k> finding(s) in <m> row(s)`.
  * stderr: `GATE_CAPTURES_ERROR: <reason>` on usage error, missing lesson,
    missing evidence dir, invalid UTF-8, or no `## Gate` section.
  * exit 0 iff 0 findings, 1 iff any finding, 2 on error (no traceback).

Usage:
  python3 -B check-gate-captures.py <lesson.md> <evidence-dir>
  python3 -B check-gate-captures.py --selftest --work <existing-dir>

--selftest builds fixtures under --work and refuses a work dir inside
/tmp (the resolved tempfile dir). It never uses /tmp. Stdlib only.
"""

import argparse
import hashlib
import os
import re
import shutil
import subprocess
import sys
import tempfile

GATE_HEADING = re.compile(r"^##\s+Gate\b")
NEXT_H2 = re.compile(r"^##\s")
SID = re.compile(r"^S\d+$")
SHA_FULL = re.compile(r"\b[0-9a-fA-F]{64}\b")
SHA_TRUNC = re.compile(r"[0-9a-fA-F]{16}(?:\.\.\.|…)")
FINDINGS = ("CAPTURE-MISSING", "CAPTURE-ABSENT", "SHA-MISMATCH", "OK")


class GateError(Exception):
    pass


def gate_section(text):
    lines = text.splitlines()
    lines = [line.rstrip("\r") for line in lines]
    start = None
    for index, line in enumerate(lines):
        if GATE_HEADING.match(line):
            start = index + 1
            break
    if start is None:
        raise GateError("no `## Gate` section")
    body = []
    for index in range(start, len(lines)):
        if NEXT_H2.match(lines[index]):
            break
        body.append((index + 1, lines[index]))
    return body


def split_row(line):
    stripped = line.strip()
    if not stripped.startswith("|") or not stripped.endswith("|"):
        return None
    cells = [c.strip() for c in stripped.strip("|").split("|")]
    if not cells:
        return None
    return cells


def is_separator(cells):
    return all(re.fullmatch(r":?-{3,}:?", c or "-") for c in cells)


def find_hash(cells):
    for cell in cells:
        match = SHA_FULL.search(cell)
        if match:
            return ("full", match.group(0).lower())
        match = SHA_TRUNC.search(cell)
        if match:
            token = match.group(0)[:-3].lower() if match.group(0).endswith("...") else match.group(0)[:-1].lower()
            return ("trunc", token)
    return None


def check_lesson(text, evidence_dir):
    section = gate_section(text)
    parsed_rows = []  # (id, hash_tuple|None, header_cells|None, cells|None)
    header = None
    header_cells = None
    for _number, line in section:
        cells = split_row(line)
        if cells is None or is_separator(cells):
            continue
        norm = [c.strip().strip("`").casefold() for c in cells]
        if header is None:
            if "capture file" in norm:
                header = "capture file"
                header_cells = cells
                header_index = norm.index("capture file")
            else:
                # header without capture file column; remember it so data rows
                # know there is no capture column
                first = (cells[0].strip().strip("`") if cells else "")
                if first.casefold() == "id" or norm[0] == "id":
                    header = "no-capture"
                    header_cells = cells
                    header_index = None
            continue
        sid = cells[0].strip().strip("`") if cells else ""
        # first cell might carry text like "`S993`"; take first token
        sid_token = sid.split()[0] if sid.split() else ""
        if not SID.match(sid_token):
            continue
        hash_info = find_hash(cells)
        if hash_info is None:
            continue
        capture_name = None
        if header == "capture file" and header_index is not None and header_index < len(cells):
            capture_name = cells[header_index].strip().strip("`")
        parsed_rows.append((sid_token, hash_info, capture_name))

    results = []
    for sid, (kind, token), capture_name in parsed_rows:
        if not capture_name:
            results.append((sid, "CAPTURE-MISSING", "-", kind, token))
            continue
        if "/" in capture_name or "\\" in capture_name or capture_name in (".", ".."):
            results.append((sid, "CAPTURE-ABSENT", capture_name, kind, token))
            continue
        path = os.path.join(evidence_dir, capture_name)
        if not os.path.isfile(path):
            results.append((sid, "CAPTURE-ABSENT", capture_name, kind, token))
            continue
        digest = hashlib.sha256()
        with open(path, "rb") as handle:
            for chunk in iter(lambda: handle.read(65536), b""):
                digest.update(chunk)
        actual = digest.hexdigest()
        if kind == "full":
            ok = actual == token
        else:
            ok = actual.startswith(token)
        results.append((sid, "OK" if ok else "SHA-MISMATCH", capture_name, kind, token))
    return results


def run(paths):
    # paths: (lesson_path, evidence_dir)
    if len(paths) != 2:
        print("GATE_CAPTURES_ERROR: usage: check-gate-captures.py <lesson.md> <evidence-dir>", file=sys.stderr)
        return 2
    lesson_path, evidence_dir = paths
    try:
        with open(lesson_path, "r", encoding="utf-8") as handle:
            text = handle.read()
    except FileNotFoundError:
        print("GATE_CAPTURES_ERROR: %s: not found" % lesson_path, file=sys.stderr)
        return 2
    except UnicodeDecodeError as exc:
        print("GATE_CAPTURES_ERROR: %s: not valid UTF-8 (%s)" % (lesson_path, exc), file=sys.stderr)
        return 2
    except OSError as exc:
        print("GATE_CAPTURES_ERROR: %s: unreadable: %s" % (lesson_path, exc.strerror), file=sys.stderr)
        return 2
    if not os.path.isdir(evidence_dir):
        print("GATE_CAPTURES_ERROR: %s: not a directory%s" % (evidence_dir, "" if os.path.exists(evidence_dir) else ": not found"), file=sys.stderr)
        return 2
    try:
        results = check_lesson(text, evidence_dir)
    except GateError as exc:
        print("GATE_CAPTURES_ERROR: %s: %s" % (lesson_path, exc), file=sys.stderr)
        return 2
    findings = 0
    for sid, status, fname, _kind, _token in results:
        print("ROW %s %s %s" % (sid, status, fname))
        if status != "OK":
            findings += 1
    print("GATE-CAPTURES: %d finding(s) in %d row(s)" % (findings, len(results)))
    return 1 if findings else 0


def _sha(data):
    return hashlib.sha256(data).hexdigest()


def _lesson(rows, header="| id | URL | capture sha256 | capture file |"):
    return (
        "# Round 98 — lesson (kotodama)\n\n## Gate\n\n" + header + "\n"
        "|---|---|---|---|\n" + "\n".join(rows) + "\n\n## Status\n"
    )


def selftest(work):
    resolved = os.path.realpath(work)
    temp_base = os.path.realpath(tempfile.gettempdir())
    if resolved == temp_base or resolved.startswith(temp_base + os.sep):
        print("GATE_CAPTURES_ERROR: --work must not be inside %s" % temp_base, file=sys.stderr)
        return 2

    root = os.path.join(resolved, "check-gate-captures-selftest")
    shutil.rmtree(root, ignore_errors=True)
    evidence = os.path.join(root, "evidence")
    os.makedirs(evidence, exist_ok=True)
    checks = []

    def write_evidence(name, data):
        with open(os.path.join(evidence, name), "wb") as handle:
            handle.write(data)

    def write_lesson(name, body):
        path = os.path.join(root, name)
        out = path if isinstance(body, str) else path
        if isinstance(body, bytes):
            with open(path, "wb") as handle:
                handle.write(body)
        else:
            with open(path, "w", encoding="utf-8") as handle:
                handle.write(body)
        return path

    def cli(lesson_path, ev=evidence):
        proc = subprocess.run(
            [sys.executable, "-B", os.path.abspath(__file__), lesson_path, ev],
            capture_output=True, text=True,
        )
        return proc.returncode, proc.stdout, proc.stderr

    # 1 clean row
    good_sha = _sha(b"good capture")
    write_evidence("S001.txt", b"good capture")
    clean = write_lesson("clean.md", _lesson([
        "| S001 | https://example.org/a | `%s` | S001.txt |" % good_sha,
    ]))
    rc, out, err = cli(clean)
    checks.append(("clean-row", rc == 0 and "ROW S001 OK S001.txt" in out
                   and out.strip().endswith("GATE-CAPTURES: 0 finding(s) in 1 row(s)")
                   and "Traceback" not in (out + err), rc, out, err))

    # 2 missing column (no capture file header) - round-97 shape, full hash
    missing = write_lesson("missing.md", (
        "# Round 97 — lesson\n\n## Gate\n\n"
        "| id | URL | capture sha256 |\n|---|---|---|\n"
        "| S002 | https://example.org/b | `%s` |\n\n## Status\n" % good_sha))
    rc, out, err = cli(missing)
    checks.append(("missing-column", rc == 1 and "ROW S002 CAPTURE-MISSING -" in out
                   and out.strip().endswith("GATE-CAPTURES: 1 finding(s) in 1 row(s)")
                   and "Traceback" not in (out + err), rc, out, err))

    # 3 absent file
    absent = write_lesson("absent.md", _lesson([
        "| S003 | https://example.org/c | `%s` | S003-missing.txt |" % good_sha,
    ]))
    rc, out, err = cli(absent)
    checks.append(("absent-file", rc == 1 and "ROW S003 CAPTURE-ABSENT S003-missing.txt" in out
                   and "Traceback" not in (out + err), rc, out, err))

    # 4 sha mismatch
    other_sha = _sha(b"other capture")
    write_evidence("S004.txt", b"other capture")
    mismatch = write_lesson("mismatch.md", _lesson([
        "| S004 | https://example.org/d | `%s` | S004.txt |" % good_sha,
    ]))
    rc, out, err = cli(mismatch)
    checks.append(("sha-mismatch", rc == 1 and "ROW S004 SHA-MISMATCH S004.txt" in out
                   and "Traceback" not in (out + err), rc, out, err))

    # 5 round-97 S993 case: row hash is the PDF's; named file is the .txt
    pdf_data = b"%PDF-1.4 fake pdf bytes for S993"
    txt_data = b"extracted text for S993"
    write_evidence("S993.pdf", pdf_data)
    write_evidence("S993.txt", txt_data)
    pdf_sha = _sha(pdf_data)
    assert pdf_sha != _sha(txt_data)
    s993 = write_lesson("s993.md", _lesson([
        "| S993 | https://example.org/threnoi | `%s` | S993.txt |" % pdf_sha,
    ]))
    rc, out, err = cli(s993)
    checks.append(("s993-pdf-vs-txt", rc == 1 and "ROW S993 SHA-MISMATCH S993.txt" in out
                   and "Traceback" not in (out + err), rc, out, err))

    # 5b same S993 row naming the PDF is clean
    s993pdf = write_lesson("s993pdf.md", _lesson([
        "| S993 | https://example.org/threnoi | `%s` | S993.pdf |" % pdf_sha,
    ]))
    rc, out, err = cli(s993pdf)
    checks.append(("s993-pdf-clean", rc == 0 and "ROW S993 OK S993.pdf" in out
                   and "Traceback" not in (out + err), rc, out, err))

    # 6 truncated legacy hash still counted as a row (round-97 shape)
    trunc = write_lesson("trunc.md", (
        "# Round 97 — lesson\n\n## Gate\n\n"
        "| id | URL | capture sha256 |\n|---|---|---|\n"
        "| S005 | https://example.org/e | `%s…` |\n\n## Status\n" % good_sha[:16]))
    rc, out, err = cli(trunc)
    checks.append(("truncated-legacy-row", rc == 1 and "ROW S005 CAPTURE-MISSING -" in out
                   and "Traceback" not in (out + err), rc, out, err))

    # 7 invalid UTF-8
    invalid = write_lesson("invalid.md", b"## Gate\n\n| id | capture sha256 | capture file |\n|---|---|\n| S006 | `%s` | S001.txt |\n" % good_sha.encode() + b"\n\xff\xfe\n")
    # fix: build bytes properly
    with open(invalid, "wb") as handle:
        handle.write(b"## Gate\n\n| id | capture sha256 | capture file |\n|---|---|---|\n")
        handle.write(b"| S006 | `" + good_sha.encode() + b"` | S001.txt |\n\xff\xfe\n")
    rc, out, err = cli(invalid)
    checks.append(("invalid-utf8", rc == 2 and "GATE_CAPTURES_ERROR" in err
                   and "not valid UTF-8" in err and "Traceback" not in (out + err), rc, out, err))

    # 8 no Gate section
    nogate = write_lesson("nogate.md", "# Round 98\n\n## Status\n\nNothing.\n")
    rc, out, err = cli(nogate)
    checks.append(("no-gate-section", rc == 2 and "GATE_CAPTURES_ERROR" in err
                   and "no `## Gate` section" in err and "Traceback" not in (out + err), rc, out, err))

    # 9 usage error: missing evidence dir
    proc = subprocess.run(
        [sys.executable, "-B", os.path.abspath(__file__), clean, os.path.join(root, "no-such-dir")],
        capture_output=True, text=True)
    checks.append(("missing-evidence-dir", proc.returncode == 2 and "GATE_CAPTURES_ERROR" in proc.stderr
                   and "Traceback" not in (proc.stdout + proc.stderr), proc.returncode, proc.stdout, proc.stderr))

    # 10 usage error: no args
    proc = subprocess.run([sys.executable, "-B", os.path.abspath(__file__)],
                          capture_output=True, text=True)
    checks.append(("no-args", proc.returncode == 2 and "GATE_CAPTURES_ERROR" in proc.stderr
                   and "Traceback" not in (proc.stdout + proc.stderr), proc.returncode, proc.stdout, proc.stderr))

    # 11 --work inside temp dir is refused
    bad_work = tempfile.gettempdir()
    proc = subprocess.run(
        [sys.executable, "-B", os.path.abspath(__file__), "--selftest", "--work", bad_work],
        capture_output=True, text=True)
    checks.append(("refuse-tmp-work", proc.returncode == 2 and "GATE_CAPTURES_ERROR" in proc.stderr
                   and "Traceback" not in (proc.stdout + proc.stderr), proc.returncode, proc.stdout, proc.stderr))

    # 12 empty capture-file cell is CAPTURE-MISSING
    empty = write_lesson("empty.md", _lesson([
        "| S007 | https://example.org/f | `%s` |  |" % good_sha,
    ]))
    rc, out, err = cli(empty)
    checks.append(("empty-capture-cell", rc == 1 and "ROW S007 CAPTURE-MISSING -" in out
                   and "Traceback" not in (out + err), rc, out, err))

    passed = sum(1 for name, ok, rc, out, err in checks if ok)
    for name, ok, rc, out, err in checks:
        sys.stdout.write("%s %s rc=%d" % ("PASS" if ok else "FAIL", name, rc))
        if not ok:
            sys.stdout.write(" out=%r err=%r" % (out.strip()[-300:], err.strip()[-300:]))
        sys.stdout.write("\n")
    print("SELFTEST PASS %d/%d" % (passed, len(checks)))
    shutil.rmtree(root, ignore_errors=True)
    return 0 if passed == len(checks) else 1


def main():
    parser = argparse.ArgumentParser(description="Check Gate-table capture-file naming.")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--work")
    parser.add_argument("paths", nargs="*")
    args = parser.parse_args()
    if args.selftest:
        if not args.work:
            print("GATE_CAPTURES_ERROR: --selftest needs --work <existing-dir>", file=sys.stderr)
            return 2
        if not os.path.isdir(args.work):
            print("GATE_CAPTURES_ERROR: --work %s: not a directory" % args.work, file=sys.stderr)
            return 2
        return selftest(args.work)
    if args.work:
        print("GATE_CAPTURES_ERROR: --work is only valid with --selftest", file=sys.stderr)
        return 2
    if len(args.paths) != 2:
        print("GATE_CAPTURES_ERROR: usage: check-gate-captures.py <lesson.md> <evidence-dir>", file=sys.stderr)
        return 2
    return run(args.paths)


if __name__ == "__main__":
    sys.exit(main())
