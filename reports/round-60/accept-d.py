#!/usr/bin/env python3
r"""Round-60 claim D acceptance: ACCEPT-D-60 (depth — the amulets entry re-entered under a new
pre-data freeze, its four round-59 over-reach propositions restored in source-scoped wording).

Frozen predicate (the same sentence in reports/round-60/claims.json `predicate`):
  ACCEPT-D-60 passes iff, at the measured revision, the amulets entry cites exactly the 43 S-ids it
  cites at lane base 9c82a6eb plus S648, S649, S650 and S651, each new id on exactly one line that
  is not a base line, and none of S602, S616, S623, S643; carries none of the four frozen over-reach
  phrases; each new id is one Registry row, status mined, tier A or B, used-by the entry, whose
  teaches opens `supersedes <mapped id> —` and whose first URL names the same page as the mapped
  row's first URL, and whose quote locates in its pinned committed capture; the entry's sha256
  equals the entry_sha256 in the packet key whose hash was committed before the support call; and
  every one of the 47 cited ids is SUPPORTED by 2 distinct qualified, blind declared support seats
  whose own transcript fetched the row's page, with no NOT-SUPPORTED from any declared seat.

Legs (each prints PASS or FAIL with its detail; the last stdout line is `ACCEPT-D-60: PASS|FAIL`,
exit 0 on PASS, 1 on FAIL, 2 on an input error). No leg fetches anything over the network: the
only page bytes read are the committed captures (routed defect 2 of the round-59 spot-check).

  SET      cited S-ids == base-cited.txt (43) + S648..S651; none of S602 S616 S623 S643 cited.
  LINES    each new id occurs on exactly one entry line, and that line is not a line of base-entry.md.
  OLDWORD  none of the four frozen round-59 over-reach phrases occurs in the normalised entry.
  ROWS     each new id: exactly one row, inside `## Registry`, >= 11 cells, status `mined`, tier A or
           B, used-by names the entry, teaches opens `supersedes <mapped id>`, first URL names the
           same page as the mapped row's first URL (scheme, www., trailing slash and a Wayback
           `id_` prefix ignored), and every later URL of its source cell is a Wayback capture of that
           page (revision 2: an echo or self-made capture URL).
  PINNED   each new id has a manifest entry in reports/round-60/captures/manifest.json whose file
           hashes to its recorded sha256, whose url is the row's first URL or a Wayback capture of
           that page listed in the row (revision 2: echo capture) and passes the locator's url_refusal,
           and whose bytes (locator to_text) locate the row's quote (>= 8 words).
  JUDGED   the packet key hashes to reports/round-60/planted-key.sha256, the planted rows hash to
           reports/round-60/planted-rows.sha256 and to the sha256 frozen in this file (revision 2), and
           sha256(entry bytes) == key entry_sha256.
  SUPPORT  declared seats: registry members named SupportA60..SupportP60, role reviewer, agentId
           KotodamaR60A2.<name> (revision 2: attempt 2's seat ids), with a report <Seat>.md, a packet
           packet-<Seat>.md and a committed transcript transcripts/KotodamaR60A2.<Seat>.jsonl. A seat is
           BLIND when its committed transcript is a byte copy of its one session file
           (/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A2/KotodamaR60A2.<Seat>.jsonl; revision 1) and
           no tool-call argument in it names the lane repo
           (`kotodama-shokunin`), `corpus`, `SOURCES.md`, the entry's file name, a registry.json,
           round 59's sandbox (`kotodama-r59`), a planted file, the packet key, history:// or
           agent://, or another seat's name; the one exempt call is a read/write/edit of the seat's
           own report path. A seat is also BOUND (revision 2: post-verdict re-key): its packet names the
           key's entry_sha256 on a line `entry_sha256: <hex>`, and its committed packet occurs
           byte-for-byte in its own dispatched task (the transcript's session_init `task`), so a
           re-key or a packet rewrite after the verdicts cannot match. A seat is QUALIFIED when it is
           BLIND and BOUND, the key gives it >= 2 PLANTED labels, each PLANTED block equals a row of
           the frozen planted file, and its report has a line-initial `VERDICT P## NOT-SUPPORTED` and
           no `VERDICT P## SUPPORTED` for every PLANTED label. A real label's SUPPORTED verdict is
           counted when the packet block (quote, teaches without its `supersedes` prefix, entry lines
           citing the id with S-ids removed; locator-normalised) equals the landed proposition and the
           seat's transcript has a tool-call argument naming the row's page (any of its URLs, as
           host+path). PASS when every cited id has counted SUPPORTED verdicts from >= 2 distinct
           QUALIFIED seats and no declared seat gives NOT-SUPPORTED on any label the key maps to an
           S-id (revision 2, post-verdict narrowing: whether or not the block still matches or the id is still
           cited).

Review-only (no leg can check them): whether each repaired sentence is the best wording; whether
the session files are the ones omp wrote (the closure compares them with history://KotodamaR60A2.<Seat>);
whether the keys were committed before the support call (`git log` of the two .sha256 files).
"""
import argparse
import glob
import hashlib
import importlib.util
import json
import os
import re
import sys

ENTRY = "corpus/knowledge/myth-symbol/amulets-talismans-apotropaic-marks.md"
BASE_CITED = "reports/round-60/base-cited.txt"
BASE_ENTRY = "reports/round-60/base-entry.md"
NEW = {"S648": "S602", "S649": "S616", "S650": "S623", "S651": "S643"}
OLD_PHRASES = (
    "a protective object is usually aimed",
    "so the amulet s power lay in its material as much as in its carving",
    "credited to those contents rather than to the metal shell",
    "concealed shoes highly worn and often patched act as apotropaic devices",
)
MANIFEST = "reports/round-60/captures/manifest.json"
SUPPORT_DIR = ".ufo/waves/round-60/support"
KEY = SUPPORT_DIR + "/planted-key.json"
KEY_SHA = "reports/round-60/planted-key.sha256"
ROWS = SUPPORT_DIR + "/planted-rows.md"
ROWS_SHA = "reports/round-60/planted-rows.sha256"
PLANTED_ROWS_SHA256 = "1a082ff0bb8abaf87dfb0536f0e7383202ffd719d6b5771943bdd2bc3b518682"  # revision 2: frozen in the counter
SEATS = [f"Support{x}60" for x in "ABCDEFGHIJKLMNOP"]
AGENT_PREFIX = "KotodamaR60A2."
MIN_SEATS_PER_ID = 2
MIN_PLANTED = 2
VERDICT = re.compile(r"^VERDICT (P\d{2}) (SUPPORTED|NOT-SUPPORTED)\b", re.M)
PACKET_BLOCK = re.compile(r"^### (P\d{2})[ \t]*\n((?:(?!### ).*\n?)*)", re.M)
PACKET_FIELD = re.compile(r"^(quote|teaches|entry|url):[ \t]*(.*)$", re.M)
SUPERSEDES = re.compile(r"^\s*supersedes\s+S\d{3,}\s*[—–-]+\s*")
SID = re.compile(r"\bS\d{3,}\b")


def load_locator(root):
    spec = importlib.util.spec_from_file_location("locator_60", os.path.join(root, "reports/round-60/reopen-quote.py"))
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def page_of(url, locator):
    url = locator.trim(url).lower()
    url = re.sub(r"^https?://", "", url)
    url = re.sub(r"^web\.archive\.org/web/\d+(?:id_)?/(?:https?://)?", "", url)
    return re.sub(r"^www\.", "", url).rstrip("/")


def sha(path):
    return hashlib.sha256(open(path, "rb").read()).hexdigest()


def tool_args(transcript):
    """Every tool-call argument object of an omp session jsonl, as JSON strings."""
    out = []
    for line in open(transcript, encoding="utf-8", errors="replace"):
        try:
            obj = json.loads(line)
        except ValueError:
            continue
        msg = obj.get("message") if isinstance(obj, dict) else None
        if not isinstance(msg, dict) or msg.get("role") != "assistant":
            continue
        for part in msg.get("content") or []:
            if isinstance(part, dict) and part.get("type") == "toolCall":
                out.append(json.dumps(part.get("arguments"), ensure_ascii=False))
    return out


def blind(seat, args):
    """'' when no tool-call argument reaches lane truth or another seat's material, else the reason.
    The one exempt call is a read/write/edit whose `path` is the seat's own report in the lane,
    .../.ufo/waves/round-60/<wave>/<Seat>.md (the validator's Report trailer)."""
    others = [s for s in SEATS if s != seat]
    own = re.compile(rf"/kotodama-shokunin/\.ufo/waves/round-60/[a-z0-9-]+/{seat}\.md$")
    for a in args:
        try:
            obj = json.loads(a)
        except ValueError:
            obj = None
        if isinstance(obj, dict) and set(obj) <= {"path", "content", "i", "input"} \
                and own.search(str(obj.get("path", ""))):
            continue
        low = a.lower()
        for bad in ("kotodama-shokunin", "kotodama-r59", "planted", "packet-key", "corpus", "sources.md",
                    "amulets-talismans", "registry.json", "history://", "agent://"):
            if bad in low:
                return bad
        for other in others:
            if other.lower() in low:
                return other
    return ""


SESSIONS = "/home/vgpnk/.omp/agent/sessions/*/*/KotodamaR60A2/KotodamaR60A2.{seat}.jsonl"


def provenance(seat, transcript):
    """'' when the committed transcript is a byte copy of exactly one session file of that seat
    (revision 1: a fabricated transcript in the lane cannot vouch), else the reason."""
    found = glob.glob(SESSIONS.format(seat=seat))
    if len(found) != 1:
        return f"session-files={len(found)}"
    if open(found[0], "rb").read() != open(transcript, "rb").read():
        return "transcript-not-session-copy"
    return ""


def bound(transcript, packet_text, entry_sha):
    """'' when the seat's own dispatched task (the session_init `task` of its transcript) carries its
    committed packet byte-for-byte, and the packet names the judged entry's sha256 (revision 2:
    a re-key or packet rewrite after the verdicts cannot match the dispatched task)."""
    if not entry_sha or f"entry_sha256: {entry_sha}\n" not in packet_text:
        return "packet-not-naming-judged-entry"
    for line in open(transcript, encoding="utf-8", errors="replace"):
        try:
            obj = json.loads(line)
        except ValueError:
            continue
        if isinstance(obj, dict) and obj.get("type") == "session_init":
            return "" if packet_text in str(obj.get("task", "")) else "packet-not-in-dispatched-task"
    return "no-session-init"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--root", default=".")
    root = os.path.abspath(ap.parse_args().root)
    try:
        locator = load_locator(root)
        base_cited = [l.strip() for l in open(os.path.join(root, BASE_CITED), encoding="utf-8") if l.strip()]
        base_lines = set(open(os.path.join(root, BASE_ENTRY), encoding="utf-8").read().splitlines())
        entry_path = os.path.join(root, ENTRY)
        entry_bytes = open(entry_path, "rb").read() if os.path.isfile(entry_path) else b""
        entry_text = entry_bytes.decode("utf-8")
        sources = open(os.path.join(root, "corpus/SOURCES.md"), encoding="utf-8").read().splitlines()
    except (OSError, SyntaxError, UnicodeDecodeError) as error:
        print(f"ACCEPT_D_60_INPUT_ERROR {error}", file=sys.stderr)
        return 2
    if len(base_cited) != 43:
        print(f"ACCEPT_D_60_INPUT_ERROR base-cited has {len(base_cited)} ids, expected 43", file=sys.stderr)
        return 2
    legs = []
    cited = sorted(set(SID.findall(entry_text)))
    want = sorted(set(base_cited) | set(NEW))
    retired = sorted(set(cited) & set(NEW.values()))
    legs.append(("SET", cited == want and not retired,
                 f"cited={len(cited)} want={len(want)} missing={sorted(set(want) - set(cited))} "
                 f"extra={sorted(set(cited) - set(want))} retired_cited={retired}"))
    lines = entry_text.splitlines()
    line_bad = []
    for sid in NEW:
        hits = [l for l in lines if re.search(rf"\b{sid}\b", l)]
        if len(hits) != 1 or hits[0] in base_lines:
            line_bad.append(f"{sid}:lines={len(hits)} base_line={bool(hits) and hits[0] in base_lines}")
    legs.append(("LINES", not line_bad, f"bad={line_bad}"))
    norm_entry = " " + locator.normalise(entry_text) + " "
    old_hits = [p for p in OLD_PHRASES if " " + p + " " in norm_entry]
    legs.append(("OLDWORD", not old_hits, f"present={old_hits}"))

    table, count, in_registry, section = {}, {}, {}, ""
    for line in sources:
        if line.startswith("## "):
            section = line[3:].strip()
        row = re.match(r"^\|\s*(S\d{3,})\s*\|", line)
        if row:
            sid = row.group(1)
            table[sid] = line.split("|")
            count[sid] = count.get(sid, 0) + 1
            in_registry[sid] = section == "Registry"
    row_bad = []
    for sid, old in NEW.items():
        cells = table.get(sid)
        if count.get(sid, 0) != 1 or not cells or len(cells) < 13 or not in_registry.get(sid):
            row_bad.append(f"{sid}:rows={count.get(sid, 0)} registry={in_registry.get(sid)}")
            continue
        urls, _ = locator.row_target(cells)
        old_urls = locator.row_target(table[old])[0] if old in table else []
        problems = []
        if cells[8].strip() != "mined":
            problems.append(f"status={cells[8].strip()}")
        if cells[4].strip() not in ("A", "B"):
            problems.append(f"tier={cells[4].strip()}")
        if ENTRY not in [u.strip() for u in re.split(r"[,;]", cells[11])]:
            problems.append("used-by")
        if not re.match(rf"^\s*supersedes\s+{old}\b", cells[7]):
            problems.append(f"teaches-not-superseding-{old}")
        if not urls or not old_urls or page_of(urls[0], locator) != page_of(old_urls[0], locator):
            problems.append("not-same-page")
        elif any(page_of(u, locator) != page_of(urls[0], locator) or not u.startswith("https://web.archive.org/web/")
                 for u in urls[1:]):
            problems.append("extra-url-not-a-capture-of-the-page")
        if problems:
            row_bad.append(f"{sid}:{','.join(problems)}")
    legs.append(("ROWS", not row_bad, f"bad={row_bad}"))

    pin_bad = []
    try:
        manifest = json.load(open(os.path.join(root, MANIFEST), encoding="utf-8"))
    except (OSError, ValueError) as error:
        manifest = {}
        pin_bad.append(f"manifest:{type(error).__name__}")
    for sid in NEW:
        cells = table.get(sid)
        item = manifest.get(sid) if isinstance(manifest, dict) else None
        if not cells or len(cells) < 13 or not isinstance(item, dict):
            pin_bad.append(f"{sid}:no-row-or-manifest")
            continue
        urls, quote = locator.row_target(cells)
        path = os.path.join(root, os.path.dirname(MANIFEST), str(item.get("file", "")))
        if not item.get("file") or not os.path.isfile(path) or sha(path) != item.get("sha256"):
            pin_bad.append(f"{sid}:capture-missing-or-hash")
            continue
        url = str(item.get("url", ""))
        if url not in urls or locator.url_refusal(url, quote or "") or not (
                url == urls[0] or (url.startswith("https://web.archive.org/web/")
                                   and page_of(url, locator) == page_of(urls[0], locator))):
            pin_bad.append(f"{sid}:url-not-row-page-or-refused")
            continue
        if not quote or len(locator.normalise(quote).split()) < locator.MIN_WORDS:
            pin_bad.append(f"{sid}:quote-short")
            continue
        text = locator.to_text(open(path, "rb").read(), str(item.get("content_type", "")))
        if not locator.locate_in(text, quote):
            pin_bad.append(f"{sid}:not-located")
    legs.append(("PINNED", not pin_bad, f"bad={pin_bad}"))

    key, judged_notes = {}, []
    key_ok = False
    try:
        for path, declared_file in ((KEY, KEY_SHA), (ROWS, ROWS_SHA)):
            declared = open(os.path.join(root, declared_file), encoding="utf-8").read().split()[0]
            if declared != sha(os.path.join(root, path)):
                judged_notes.append(f"hash-mismatch:{path}")
        if sha(os.path.join(root, ROWS)) != PLANTED_ROWS_SHA256:
            judged_notes.append("planted-rows-not-the-frozen-file")
        key = json.load(open(os.path.join(root, KEY), encoding="utf-8"))
        entry_sha = hashlib.sha256(entry_bytes).hexdigest()
        if key.get("entry_sha256") != entry_sha:
            judged_notes.append(f"entry_sha256 key={str(key.get('entry_sha256'))[:12]} landed={entry_sha[:12]}")
        key_ok = not judged_notes and isinstance(key.get("seats"), dict)
    except (OSError, ValueError, AttributeError, IndexError) as error:
        judged_notes.append(f"no-key:{type(error).__name__}")
    legs.append(("JUDGED", key_ok, " ".join(judged_notes) or "entry equals the judged object"))

    seats, notes = set(), []
    try:
        registry = json.load(open(os.path.join(root, SUPPORT_DIR, "registry.json"), encoding="utf-8"))
        seats = {m["name"] for m in registry.get("members", [])
                 if m.get("name") in SEATS and m.get("role") == "reviewer"
                 and m.get("agentId") == f"{AGENT_PREFIX}{m.get('name')}"}
    except (OSError, ValueError, AttributeError, TypeError, KeyError) as error:
        notes.append(f"no-registry:{type(error).__name__}")
    seat_keys = key.get("seats", {}) if key_ok else {}
    entry_lines = entry_text.splitlines()
    planted_blocks = set()
    try:
        for _, body in re.findall(r"^### (PLANTED-\d+)\n((?:(?!### ).*\n?)*)", open(os.path.join(root, ROWS), encoding="utf-8").read(), re.M):
            fields = dict(PACKET_FIELD.findall(body))
            planted_blocks.add((locator.normalise(fields.get("quote", "").strip().strip('"')),
                                locator.normalise(SUPERSEDES.sub("", fields.get("teaches", ""))),
                                locator.normalise(fields.get("entry", ""))))
    except OSError as error:
        notes.append(f"no-planted-rows:{type(error).__name__}")

    def proposition(sid):
        cells = table.get(sid, [])
        quote = locator.row_target(cells)[1] if len(cells) >= 13 else ""
        teaches = SUPERSEDES.sub("", cells[7]) if len(cells) > 7 else ""
        cites = [SID.sub(" ", l) for l in entry_lines if re.search(rf"\b{sid}\b", l)]
        return (locator.normalise(quote or ""), locator.normalise(teaches), locator.normalise(" ".join(cites)))

    verdicts, qualified, seat_notes, rejected = {}, set(), [], []
    for seat in sorted(seats):
        report = os.path.join(root, SUPPORT_DIR, f"{seat}.md")
        packet = os.path.join(root, SUPPORT_DIR, f"packet-{seat}.md")
        transcript = os.path.join(root, SUPPORT_DIR, "transcripts", f"{AGENT_PREFIX}{seat}.jsonl")
        labels = seat_keys.get(seat) if isinstance(seat_keys.get(seat), dict) else {}
        if not (os.path.isfile(report) and os.path.isfile(packet) and os.path.isfile(transcript) and labels):
            seat_notes.append(f"{seat}:missing")
            continue
        args = tool_args(transcript)
        packet_text = open(packet, encoding="utf-8", errors="replace").read()
        seen = provenance(seat, transcript) or blind(seat, args) or bound(transcript, packet_text, key.get("entry_sha256", ""))
        found = VERDICT.findall(open(report, encoding="utf-8", errors="replace").read())
        shown = {}
        for label, body in PACKET_BLOCK.findall(packet_text):
            fields = dict(PACKET_FIELD.findall(body))
            shown[label] = (locator.normalise(fields.get("quote", "").strip().strip('"')),
                            locator.normalise(SUPERSEDES.sub("", fields.get("teaches", ""))),
                            locator.normalise(fields.get("entry", "")))
        planted = [l for l, t in labels.items() if t == "PLANTED"]
        if not seen and len(planted) >= MIN_PLANTED and all(shown.get(p) in planted_blocks for p in planted) and all(
                (p, "NOT-SUPPORTED") in found and (p, "SUPPORTED") not in found for p in planted):
            qualified.add(seat)
        seat_notes.append(f"{seat}:{'Q' if seat in qualified else 'X'}{len(planted)}{'' if not seen else '/sees:' + seen}")
        joined = "\n".join(a.lower() for a in args)
        for label, verdict in found:
            sid = labels.get(label)
            if not sid or sid == "PLANTED":
                continue
            if verdict == "NOT-SUPPORTED":
                rejected.append(f"{sid}:NOT/{seat}")
            if sid not in cited or label not in shown:
                continue
            if shown[label] != proposition(sid) or not all(shown[label]):
                continue
            pages = {page_of(u, locator) for u in locator.row_target(table.get(sid, []))[0]} if len(table.get(sid, [])) >= 13 else set()
            fetched = any(p and p in joined for p in pages)
            verdicts.setdefault(sid, []).append((verdict, seat, fetched))
    unsupported = list(rejected)
    for sid in cited:
        given = verdicts.get(sid, [])
        good = {seat for v, seat, f in given if v == "SUPPORTED" and f and seat in qualified}
        if len(good) < MIN_SEATS_PER_ID:
            unsupported.append(f"{sid}:good={len(good)}")
    legs.append(("SUPPORT", bool(cited) and key_ok and not unsupported,
                 f"unsupported={unsupported} qualified={sorted(qualified)} seats={seat_notes} {' '.join(notes)}".rstrip()))
    for name, ok, detail in legs:
        print(f"{name} {'PASS' if ok else 'FAIL'} {detail}")
    verdict = all(ok for _, ok, _ in legs)
    print(f"ACCEPT-D-60: {'PASS' if verdict else 'FAIL'}")
    return 0 if verdict else 1


if __name__ == "__main__":
    sys.exit(main())
