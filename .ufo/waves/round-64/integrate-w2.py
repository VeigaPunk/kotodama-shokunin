#!/usr/bin/env python3
"""Assemble Round-64 coverage contributions without changing existing source rows."""

import argparse
import re
import sys
from pathlib import Path

PARTS = (
    "linguistics",
    "myth-symbol",
    "culture-material",
    "synthesis",
    "verification",
    "civilizations",
)
ENTRY_REL = Path("corpus/knowledge/linguistics/language-socialization-and-acquisition.md")
MINED_IDS = tuple(f"S{number:03d}" for number in range(718, 744))
REJECTED_IDS = tuple(f"S{number:03d}" for number in range(744, 750))
ALL_IDS = MINED_IDS + REJECTED_IDS
LABEL_RE = re.compile(r"^([A-Z][A-Z0-9]*):[ \t]*(.*)$")
ID_RE = re.compile(r"\bS\d{3,}\b")
REGISTRY_ID_RE = re.compile(r"^\| (S\d{3}) \|")
SECTION_RE = re.compile(r"^## ([a-z-]+)/ \((\d+)\)\s*$")
INDEX_ROW_RE = re.compile(r"^- `([^`]+\.md)` — (.*)$")
TOTAL_RE = re.compile(r"^Total knowledge entries: (\d+)\.$", re.M)
FOOTER_RE = re.compile(
    r"^(Counts checked \d{4}-\d{2}-\d{2} from the repo root:\r?\n"
    r"`[^`\r\n]+`\r?\n)"
    r"\(total (\d+) files; directory totals ([\d/]+)\)\.",
    re.M,
)
BULLET_MAP = {
    1: ("S726",),
    2: ("S718", "S719", "S729", "S724"),
    3: ("S720", "S721", "S722", "S723"),
    4: ("S725", "S737", "S743"),
    5: ("S727", "S728", "S742", "S738"),
    6: ("S730", "S731", "S732", "S733"),
    7: ("S734", "S735", "S736"),
    8: ("S739", "S740", "S741"),
    9: (),
}
BULLET_MARKER_RE = re.compile(r"^[ \t]*<!-- BULLETS (\d+) -->[ \t]*(?:\r?\n)?$")


class AssemblyError(Exception):
    """An input or destination cannot be safely assembled."""


def read_text(path):
    try:
        with path.open("r", encoding="utf-8", newline="") as handle:
            return handle.read()
    except (OSError, UnicodeError) as error:
        raise AssemblyError(f"cannot read {path}: {error}") from None


def line_ending(line):
    if line.endswith("\r\n"):
        return "\r\n"
    if line.endswith("\n"):
        return "\n"
    return ""


def parse_contribution(path, expected_sid, rejected):
    text = read_text(path)
    required = ("ROW", "TEST", "TEST2") if rejected else (
        "ROW", "BULLET", "VERIFY", "CAPTURE", "ACCESS"
    )
    fields = {}
    for number, line in enumerate(text.splitlines(), 1):
        if not line.strip():
            continue
        match = LABEL_RE.fullmatch(line)
        if not match:
            raise AssemblyError(f"{path}:{number}: malformed labelled line")
        label, value = match.groups()
        if label not in required:
            raise AssemblyError(f"{path}:{number}: unexpected label {label}")
        if label in fields:
            raise AssemblyError(f"{path}:{number}: duplicate label {label}")
        if not value.strip():
            raise AssemblyError(f"{path}:{number}: empty {label} value")
        fields[label] = value

    missing_fields = [label for label in required if label not in fields]
    if missing_fields:
        raise AssemblyError(f"{path}: missing labelled lines {', '.join(missing_fields)}")

    row = fields["ROW"].strip()
    if not (row.startswith("|") and row.endswith("|")):
        raise AssemblyError(f"{path}: ROW is not a pipe-delimited registry line")
    cells = [cell.strip() for cell in row.split("|")[1:-1]]
    if len(cells) != 11:
        raise AssemblyError(f"{path}: ROW has {len(cells)} cells, not 11")
    sid = cells[0]
    if not re.fullmatch(r"S\d{3}", sid):
        raise AssemblyError(f"{path}: invalid first-cell S-id {sid!r}")
    if sid != expected_sid:
        raise AssemblyError(f"{path}: directory id {expected_sid} disagrees with ROW id {sid}")

    # revision 1 (pre-data, matching accept-c.py leg REJECTS): a disposition row
    # may honestly carry `queued` + QUEUED-CANDIDATE when the re-test
    # contradicted the original rejection ground.
    allowed = ("rejected", "queued") if rejected else ("mined",)
    if cells[7] not in allowed:
        raise AssemblyError(f"{path}: {sid} status is {cells[7]!r}, expected one of {allowed!r}")
    if rejected:
        if not cells[6].startswith(("REJECTED:", "QUEUED-CANDIDATE:")) or "; flip:" not in cells[6]:
            raise AssemblyError(f"{path}: disposition teaches cell must contain REJECTED:/QUEUED-CANDIDATE: and ; flip:")
        if cells[10] != "—":
            raise AssemblyError(f"{path}: rejected used-by cell must be —")
    else:
        if cells[10] != ENTRY_REL.as_posix():
            raise AssemblyError(f"{path}: mined used-by cell must be {ENTRY_REL.as_posix()}")
        bullet = fields["BULLET"].strip()
        bullet_ids = ID_RE.findall(bullet)
        if not bullet.startswith("- ") or bullet_ids != [sid] or not bullet.endswith(f"({sid})"):
            raise AssemblyError(f"{path}: BULLET must be one line ending with exactly ({sid})")
        fields["BULLET"] = bullet

    return {"sid": sid, "row": row, "cells": cells, "fields": fields, "path": path}


def collect_contributions(rows_dir):
    if not rows_dir.is_dir():
        raise AssemblyError(f"rows directory does not exist: {rows_dir}")
    directories = sorted(
        path for path in rows_dir.iterdir()
        if path.is_dir() and (path.name.startswith("ScribeRow") or path.name.startswith("ScribeRej"))
    )
    if not directories:
        raise AssemblyError(f"no ScribeRow*/ or ScribeRej*/ directories under {rows_dir}")

    found = {}
    expected_set = set(ALL_IDS)
    for directory in directories:
        match = re.fullmatch(r"Scribe(Row|Rej)(S\d{3})", directory.name)
        if not match:
            raise AssemblyError(f"unexpected contribution directory name: {directory}")
        category, sid = match.groups()
        if sid not in expected_set:
            raise AssemblyError(f"unexpected contribution id {sid} in {directory}")
        rejected = category == "Rej"
        should_be_rejected = sid in REJECTED_IDS
        if rejected != should_be_rejected:
            raise AssemblyError(f"{directory}: {sid} is in the wrong mined/rejected directory class")
        path = directory / "row.txt"
        if not path.is_file():
            raise AssemblyError(f"missing contribution file: {path}")
        contribution = parse_contribution(path, sid, rejected)
        if sid in found:
            raise AssemblyError(f"duplicate S-id {sid}: {found[sid]['path']} and {path}")
        found[sid] = contribution

    missing = sorted(expected_set - set(found), key=lambda sid: int(sid[1:]))
    if missing:
        raise AssemblyError(f"missing contribution ids: {', '.join(missing)}")
    return found


def entry_from_skeleton(rows_dir, contributions):
    skeleton_path = rows_dir / "ScribeEntrySkeleton" / "entry.md"
    text = read_text(skeleton_path)
    # This range in the skeleton is descriptive metadata, not a claim citation.
    # Removing the two IDs keeps the resulting entry clean under check-cited-lines.py.
    text = text.replace(
        "Round-64 row citations S718–S743 in `corpus/SOURCES.md` supply the source claims; each claim is limited to its cited row.",
        "Round-64 registry rows in `corpus/SOURCES.md` supply the source claims; each claim is limited to its cited row.",
    )

    mapped_ids = [sid for sids in BULLET_MAP.values() for sid in sids]
    if sorted(mapped_ids, key=lambda sid: int(sid[1:])) != list(MINED_IDS):
        raise AssemblyError("internal BULLET_MAP does not cover S718-S743 exactly once")

    markers = {}
    rendered = []
    for line in text.splitlines(keepends=True):
        match = BULLET_MARKER_RE.fullmatch(line)
        if not match:
            rendered.append(line)
            continue
        section = int(match.group(1))
        if section in markers:
            raise AssemblyError(f"entry skeleton repeats BULLETS {section}")
        markers[section] = True
        ending = line_ending(line)
        bullets = sorted(BULLET_MAP.get(section, ()), key=lambda sid: int(sid[1:]))
        if bullets:
            rendered.extend(contributions[sid]["fields"]["BULLET"] + ending for sid in bullets)
        else:
            rendered.append(ending)
    if set(markers) != set(range(1, 10)):
        absent = sorted(set(range(1, 10)) - set(markers))
        unexpected = sorted(set(markers) - set(range(1, 10)))
        raise AssemblyError(f"entry skeleton BULLETS markers must be 1-9; missing={absent}, unexpected={unexpected}")
    output = "".join(rendered)
    if "<!-- BULLETS " in output:
        raise AssemblyError("unreplaced BULLETS marker remains in generated entry")

    # Match the cited-lines checker: multiple S-ids on one line or an S-id in a table row.
    for number, line in enumerate(output.splitlines(), 1):
        ids = sorted(set(ID_RE.findall(line)), key=lambda sid: int(sid[1:]))
        if len(ids) >= 2 or (ids and line.lstrip().startswith("|")):
            raise AssemblyError(f"generated entry would fail check-cited-lines.py at line {number}: {','.join(ids)}")
    return output


def readme_row_from_skeleton(rows_dir, entry_text):
    path = rows_dir / "ScribeEntrySkeleton" / "readme-row.txt"
    lines = read_text(path).splitlines()
    if len(lines) != 1:
        raise AssemblyError(f"{path}: expected exactly one README index row")
    row = lines[0]
    match = INDEX_ROW_RE.fullmatch(row)
    if not match:
        raise AssemblyError(f"{path}: malformed README index row")
    if match.group(1) != ENTRY_REL.name:
        raise AssemblyError(f"{path}: README index filename must be {ENTRY_REL.name}")
    topic = re.search(r"^- topic:(.*?)(?=\n- \w)", entry_text, re.M | re.S)
    if not topic:
        raise AssemblyError("generated entry has no - topic: field")
    actual_topic = " ".join(part.strip() for part in topic.group(1).strip("\n").splitlines() if part.strip())
    if match.group(2) != actual_topic:
        raise AssemblyError(f"{path}: README topic does not exactly match generated entry - topic:")
    return row


def markdown_files(root, part):
    directory = root / "corpus" / "knowledge" / part
    if not directory.is_dir():
        raise AssemblyError(f"missing knowledge partition: {directory}")
    return sorted(path.name for path in directory.iterdir() if path.name.endswith(".md") and path.is_file())


def assemble_readme(root, row, projected_counts):
    path = root / "corpus" / "README.md"
    text = read_text(path)
    lines = text.splitlines(keepends=True)
    headers = []
    for index, line in enumerate(lines):
        match = SECTION_RE.fullmatch(line.rstrip("\r\n"))
        if match:
            headers.append((index, match.group(1), int(match.group(2))))
    linguistics = [item for item in headers if item[1] == "linguistics"]
    if len(linguistics) != 1:
        raise AssemblyError("corpus/README.md must contain exactly one ## linguistics/ section")
    header_index, _, old_header_count = linguistics[0]
    section_end = next((item[0] for item in headers if item[0] > header_index), len(lines))

    index_rows = []
    for index in range(header_index + 1, section_end):
        if INDEX_ROW_RE.fullmatch(lines[index].rstrip("\r\n")):
            index_rows.append(index)
    if not index_rows:
        raise AssemblyError("linguistics section has no backtick-bulleted index row")
    if any(INDEX_ROW_RE.fullmatch(lines[index].rstrip("\r\n")).group(1) == ENTRY_REL.name for index in index_rows):
        raise AssemblyError(f"README already indexes {ENTRY_REL.name}")

    header_line = lines[header_index]
    ending = line_ending(header_line) or "\n"
    lines[header_index] = f"## linguistics/ ({projected_counts['linguistics']}){ending}"
    last_row_index = index_rows[-1]
    row_ending = line_ending(lines[last_row_index]) or "\n"
    if not line_ending(lines[last_row_index]):
        lines[last_row_index] += row_ending
    # revision 1 (pre-data): the index rows are filename-sorted
    # (ScribeReadmeFrontier F3 / DR-IS-07); insert at the sorted slot instead
    # of appending after the final row.
    insert_at = last_row_index + 1
    for idx in index_rows:
        existing = INDEX_ROW_RE.fullmatch(lines[idx].rstrip("\r\n")).group(1)
        if existing > ENTRY_REL.name:
            insert_at = idx
            break
    lines.insert(insert_at, row + row_ending)
    output = "".join(lines)

    totals_count = output.count("Total knowledge entries:")
    total_matches = list(TOTAL_RE.finditer(output))
    if totals_count > 1 or (totals_count == 1 and len(total_matches) != 1):
        raise AssemblyError("corpus/README.md has a malformed or duplicate Total knowledge entries line")
    if total_matches:
        output = TOTAL_RE.sub(f"Total knowledge entries: {sum(projected_counts.values())}.", output, count=1)

    footer_matches = list(FOOTER_RE.finditer(output))
    if len(footer_matches) != 1:
        raise AssemblyError("corpus/README.md must contain exactly one parseable Counts checked footer block")
    footer = footer_matches[0]
    vector = "/".join(str(projected_counts[part]) for part in PARTS)
    replacement = (
        footer.group(1)
        + f"(total {sum(projected_counts.values())} files; directory totals {vector})."
    )
    output = output[:footer.start()] + replacement + output[footer.end():]
    return output, old_header_count


def registry_output(root, contributions):
    path = root / "corpus" / "SOURCES.md"
    text = read_text(path)
    lines = text.splitlines(keepends=True)
    registry = []
    existing_ids = set()
    for index, line in enumerate(lines):
        match = REGISTRY_ID_RE.match(line)
        if match:
            registry.append(index)
            existing_ids.add(match.group(1))
    if not registry:
        raise AssemblyError("corpus/SOURCES.md has no registry rows")
    collisions = sorted(existing_ids.intersection(ALL_IDS), key=lambda sid: int(sid[1:]))
    if collisions:
        raise AssemblyError(f"target ids already exist in corpus/SOURCES.md: {', '.join(collisions)}")

    last_index = registry[-1]
    ending = line_ending(lines[last_index]) or "\n"
    if not line_ending(lines[last_index]):
        lines[last_index] += ending
    additions = [contributions[sid]["row"] + ending for sid in ALL_IDS]
    lines[last_index + 1:last_index + 1] = additions
    return "".join(lines), len(registry)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Assemble Kotodama round-64 claim-C contributions")
    parser.add_argument("--root", type=Path, default=Path.cwd(), help="lane root (default: current directory)")
    parser.add_argument("--rows-dir", required=True, type=Path, help="round-64 contribution root")
    parser.add_argument("--dry-run", action="store_true", help="print the plan without writing files")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    rows_dir = args.rows_dir.resolve()
    try:
        contributions = collect_contributions(rows_dir)
        entry_path = root / ENTRY_REL
        if entry_path.exists():
            raise AssemblyError(f"target entry already exists: {entry_path}")
        if not entry_path.parent.is_dir():
            raise AssemblyError(f"missing entry directory: {entry_path.parent}")
        entry_text = entry_from_skeleton(rows_dir, contributions)
        readme_row = readme_row_from_skeleton(rows_dir, entry_text)

        source_text, source_count = registry_output(root, contributions)
        current_counts = {part: len(markdown_files(root, part)) for part in PARTS}
        projected_counts = dict(current_counts)
        projected_counts["linguistics"] += 1
        readme_text, old_header_count = assemble_readme(root, readme_row, projected_counts)

        outputs = (
            (root / "corpus" / "SOURCES.md", source_text),
            (entry_path, entry_text),
            (root / "corpus" / "README.md", readme_text),
        )
        target_row_count = source_count + len(ALL_IDS)
        total = sum(projected_counts.values())
        mode = "DRY-RUN" if args.dry_run else "PLAN"
        print(f"{mode} root={root}")
        print(f"registry: append {len(ALL_IDS)} rows after current final row; {source_count} -> {target_row_count} rows")
        print(f"entry: write {ENTRY_REL.as_posix()} with {len(MINED_IDS)} mapped bullets")
        print(
            "README: insert index row; linguistics header "
            f"{old_header_count} -> {projected_counts['linguistics']}; "
            f"total/footer {sum(current_counts.values())} -> {total}; "
            f"directory totals {'/'.join(str(projected_counts[part]) for part in PARTS)}"
        )
        if args.dry_run:
            return 0

        for path, content in outputs:
            try:
                with path.open("w", encoding="utf-8", newline="") as handle:
                    handle.write(content)
            except (OSError, UnicodeError) as error:
                raise AssemblyError(f"cannot write {path}: {error}") from None
        for path, _ in outputs:
            print(f"WROTE {path.relative_to(root).as_posix()}")
        print(f"ASSEMBLED registry_rows={target_row_count} entry_files={total}")
        return 0
    except AssemblyError as error:
        print(f"INTEGRATE_ERROR {error}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
