#!/usr/bin/env python3
"""x63-entry-source-resolvability — round-27 read-only entry auditor.

Audits corpus entry documents (never culture packets, never round fragments)
against the three criteria the round-10 and round-19 auditor seats applied to
this lane's knowledge entries, plus the pin and sweep surfaces a later round
added:

  * names the gap it fills      (a frontmatter `gap` clause or a body heading)
  * carries a decision record   (a `## .. decision record ..` heading)
  * its sources resolve         (every repo path locator exists; every quoted
                                 command re-runs; every `sha256` pin re-derives;
                                 every URL gets a documented access attempt)
  * states its absence sweep    (a quoted `grep ... -> 0 files` line reproduces
                                 against the tree minus the entry itself)

The tool is a **resolvability** instrument, not a merits instrument. It does not
judge whether a source is the right source, whether a calibration is warranted,
or whether a gap is worth filling. A locator that resolves is reported as
resolved even when the source it names is weak; a finding is only ever "the
entry says X and the bytes say not-X".

The declared-absent exemption. A cell that names a path and *states in the same
cell* that the path was never filed (`no `reports/round-4*` exists`, `not
filed`, `absent`, `never existed`) is exempt from the resolution check: the
entry is making a negative claim, and reading it as a broken link inverts its
meaning. The exemption is reported, never silent — every exempted token appears
in the receipt under `declared_absent`. The round-25 X45 pointer tool does not
carry this exemption and reports such a cell red; the round-26 X63 audit added
it. This tool adopts the exemption and names it.

Negative controls. `--selftest` plants one clean entry and one entry per defect
class in a temp tree under $TMPDIR, and asserts the exit code and the finding
ids. A check that cannot fail is not a check, so every check here has a planted
control that makes it fire.

Read-only by construction: no code path opens a file for writing except the
selftest's own temp tree, which is created under the directory named by
`--scratch` (default $TMPDIR) and removed at the end. Network access is
attempted only for URL locators, is bounded to a few seconds, and its outcome
is recorded as an observation: an unreachable URL is reported, never scored as
a defect, because a failed fetch cannot distinguish a dead link from a dead
network. `--offline` suppresses the attempt and records `not-attempted`.

Output: one line per finding on stdout, then an `INFO scan:` summary line; with
`--json`, the full receipt object on stdout instead. Exit codes: 0 clean;
1 findings; 2 could-not-evaluate (missing path, not an entry document,
unreadable, or not UTF-8 text), also 2 for argparse usage errors. `--selftest`
exits 0 when every planted control behaves as asserted, 1 when one does not.

Stdlib only.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import urllib.error
import urllib.request

SCHEMA = "kotodama-entry-source-resolvability-x63-v1"

# The frontmatter bar. Kept identical to the round-10 acceptance constant
# (reports/round-10/run-validation.py:81) so a green here is comparable with a
# green there; `gap` is checked separately because it has a field form and a
# heading form.
FRONTMATTER_FIELDS = ("topic", "sources", "verified-at", "recheck", "couples")

# Locators: repo-relative paths, the shape the lane's entries actually use.
# A locator may carry a line-range suffix (`file.md:88-98`, `file.md:92,121`),
# which names a *passage* of the file, not a different path — stripping it is
# what makes the locator resolvable. Both the file part and the full token are
# kept so the receipt shows what the entry actually wrote.
REPO_PATH_RE = re.compile(
    r"\b((?:corpus|tools|reports|examples|\.ufo)/[\w./*\-]+\.(?:md|py|yml|json|tsv|txt|jsonl|yaml))"
    r"(?::[0-9][0-9,\-]*)?"
)
LINE_SUFFIX_RE = re.compile(r":\d[\d,\-]*$")
# Brace expansion: `reports/round-26/register/{design,forms,rules}.md` names
# four files, and the lane's entries use it heavily. Expanding is what keeps a
# compressed citation from reading as a dead link.
BRACE_RE = re.compile(r"\{([^{}]+)\}")
URL_RE = re.compile(r"https?://[^\s`)\]<>]+")


def expand_braces(token):
    """Expand `a{b,c}d` into `abd`, `acd`; a token without braces yields itself."""
    m = BRACE_RE.search(token)
    if not m:
        return [token]
    out = []
    for alt in m.group(1).split(","):
        out.extend(expand_braces(token[:m.start()] + alt + token[m.end():]))
    return out


GAP_FIELD_RE = re.compile(
    r"(?i)(?:^|[\s.;\u2014\u2013|-])gap(?:[\s-]+(?:filled|addressed|served))?\s*:\s*(\S[^\n]{0,300})"
)
GAP_HEADING_RE = re.compile(r"(?mi)^#{2,4}[^\n]*\bgap\b[^\n]*$")
DECISION_RE = re.compile(r"(?mi)^#{2,4}[^\n]*decision[- ]record[^\n]*$")
CALIBRATION_RE = re.compile(r"(?i)calibrat")

# A quoted absence sweep: `grep -rln "<pattern>" <path>` with a stated `-> 0`.
SWEEP_RE = re.compile(
    r"grep\s+-rln?\s+[\"'\u201c](?P<pattern>[^\"'\u201d]+)[\"'\u201d]\s+(?P<path>[^\s;`)\u2014]+)"
)
SWEEP_ZERO_RE = re.compile(r"(?:→|->)\s*0\b")

DECLARED_ABSENT_RE = re.compile(
    r"(?i)(not filed|never filed|never existed|no such file|absent|does not exist|"
    r"not round-numbered|no `[^`]+` exists|no `[^`]+` at)"
)

NOT_ENTRY_RE = re.compile(r"(?m)^(#{1,6}\s+\S|[-*]\s+[A-Za-z][A-Za-z-]*\s*:)")


class CannotEvaluate(Exception):
    """The named path cannot be graded as an entry document."""


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def read_text(path):
    try:
        with open(path, "rb") as fh:
            raw = fh.read()
    except FileNotFoundError:
        raise CannotEvaluate(f"{path}: no such file")
    except IsADirectoryError:
        raise CannotEvaluate(f"{path}: is a directory")
    except OSError as exc:
        raise CannotEvaluate(f"{path}: unreadable ({exc})")
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        raise CannotEvaluate(f"{path}: not UTF-8 text")


def header_lines(text, limit=40):
    """The header block: leading `- field:` lines plus their continuations."""
    out = []
    for line in text.splitlines()[:limit]:
        out.append(line)
    return out


def parse_frontmatter(text):
    """field -> value, where a value absorbs indented continuation lines."""
    fields = {}
    current = None
    for line in header_lines(text):
        if line.startswith(("#", "  ", "\t")) or not line.strip():
            if current and line.strip() and line.startswith(("  ", "\t")):
                fields[current].append(line.strip())
            continue
        m = re.match(r"^\s*[-*]?\s*([A-Za-z][A-Za-z-]*)\s*:\s*(.*)$", line)
        if m:
            current = m.group(1).lower()
            fields.setdefault(current, []).append(m.group(2).strip())
        else:
            current = None
    return {k: " ".join(v).strip() for k, v in fields.items()}


def check_frontmatter(text):
    fields = parse_frontmatter(text)
    missing = [f for f in FRONTMATTER_FIELDS if f not in fields or not fields[f].strip()]
    return fields, missing


def check_gap(text):
    m = GAP_FIELD_RE.search(text)
    if m and m.group(1).strip():
        return True, "field", m.group(1).strip()[:120]
    m = GAP_HEADING_RE.search(text)
    if m:
        return True, "heading", m.group(0).strip()[:120]
    return False, "none", ""


def check_decision(text):
    m = DECISION_RE.search(text)
    if not m:
        return False, ""
    return True, m.group(0).strip()[:120]


def declared_absent_in(text, token):
    """True when the token sits in a cell that declares the path was never filed."""
    for line in text.splitlines():
        if token in line:
            if DECLARED_ABSENT_RE.search(line):
                return True
            # multi-line cells: the declaration may sit one line below
            idx = text.find(line)
            window = text[idx:idx + len(line) + 400]
            if DECLARED_ABSENT_RE.search(window):
                return True
    return False


def check_locators(text, root, offline=False):
    """Resolve every repo-path locator the entry cites.

    Two lane conventions would read as dead links if taken literally, and both
    are handled explicitly rather than being reported as defects:

      * a **passage locator** — `file.md:88-98` — names a line range inside a
        file that exists; the line suffix is stripped before resolution;
      * a **brace-compressed citation** — `{design,forms,rules}.md` — names
        several files at once; each expansion is resolved, and the token
        resolves if every expansion does.

    A token that resolves only in part is reported with the expansions that
    failed, so a genuinely dead branch of a compressed citation is still named.
    """
    resolved, unresolved, exempt, urls = [], [], [], []
    seen = set()
    for token in REPO_PATH_RE.findall(text):
        if token in seen:
            continue
        seen.add(token)
        bare = LINE_SUFFIX_RE.sub("", token.rstrip(".,;:"))
        expanded = expand_braces(bare)
        if "*" in bare:
            if declared_absent_in(text, token):
                exempt.append({"token": token, "why": "declared-absent glob"})
            elif not any((root / p).exists() for p in _glob_expand(root, bare)):
                unresolved.append({"token": token, "why": "glob matched nothing"})
            else:
                resolved.append(bare)
            continue
        missing = [p for p in expanded if not (root / p).exists()]
        if not missing:
            resolved.append(token)
        elif declared_absent_in(text, token):
            exempt.append({"token": token, "why": "declared-absent"})
        else:
            unresolved.append({"token": token, "why": "path does not exist",
                               "missing": missing})
    for url in sorted(set(URL_RE.findall(text))):
        urls.append(probe_url(url, offline))
    return resolved, unresolved, exempt, urls


def _glob_expand(root, pattern):
    import glob
    return glob.glob(str(root / pattern))


def probe_url(url, offline=False):
    rec = {"url": url, "attempted": not offline}
    if offline:
        rec["outcome"] = "not-attempted"
        return rec
    req = urllib.request.Request(url, method="HEAD",
                                 headers={"User-Agent": "kotodama-x63-resolvability/1"})
    try:
        with urllib.request.urlopen(req, timeout=6) as resp:
            rec["outcome"] = "reachable"
            rec["status"] = getattr(resp, "status", None)
    except urllib.error.HTTPError as exc:
        rec["outcome"] = "http-error"
        rec["status"] = exc.code
    except Exception as exc:  # noqa: BLE001 - a fetch failure is an observation
        rec["outcome"] = "unreachable"
        rec["detail"] = type(exc).__name__
    return rec


HISTORICAL_PIN_RE = re.compile(
    r"(?i)(before append|before this|prior revision|earlier revision|previous revision|"
    r"at the stamp|historical|superseded|pre-append|before the (?:append|revision)|"
    r"sha8? of this file|this file(?:'s)? sha)"
)


def _bullets(text):
    """Source bullets: each starts at a line beginning `  - ` or `- `."""
    starts = [m.start() for m in re.finditer(r"(?m)^\s*[-*] ", text)]
    spans = []
    for i, s in enumerate(starts):
        e = starts[i + 1] if i + 1 < len(starts) else len(text)
        spans.append((s, e, text[s:e]))
    return spans


def _bullet_of(spans, pos):
    for s, e, body in spans:
        if s <= pos < e:
            return body, pos - s
    return "", pos


REMOTE_PIN_RE = re.compile(
    r"(?i)(https?://|web\.archive\.org|raw snapshot|downloaded|fetched|"
    r"retrieved from|transcription)"
)


def check_pins(text, root):
    """A pin is a digest bound to the **source path the bullet opens with**.

    The lane's source bullets have the shape
    ``- KTD-XX-S-NNNN — `path` (… sha256 `abc…` …): prose``. The path right
    after the id is the source the bullet is about, and a digest in that bullet
    is a claim about **that** file. Binding a digest to any path that merely
    appears later in the bullet is how an auditor manufactures false positives:
    measured, `civilizations/mesoamerica-primary-sources.md` cites
    `reports/round-17/civ/mesoamerica.md` as a *trail* and then quotes the
    digest of a web-archive snapshot — binding the two reported a stale pin
    where the entry had recorded a fetched page.

    Four classes are reported, and only the first is graded:

      * ``re-derived`` / ``drift`` — the bullet opens with a repo path that
        resolves, and the digest does or does not match its live bytes;
      * ``remote-artifact`` — the bullet is about a fetched page, download or
        snapshot (a URL, a quoted byte size), which cannot re-derive from the
        tree at all;
      * ``historical-self-digest`` — "entry sha256 *before append* `abc…`", the
        record of this file's own past bytes, which is *supposed* not to match;
      * ``revision-bound`` / ``unbound`` — the bullet attributes the digest to a
        past lane revision, or names no repo path at all.

    A class other than the first is reported, never silently dropped: a consumer
    must see what the leg refused to grade.
    """
    checks = []
    spans = _bullets(text)
    for m in re.finditer(r"sha256[^\n]{0,60}?([0-9a-f]{12,64})", text):
        digest = m.group(1)
        body, _off = _bullet_of(spans, m.start())
        # The lead path: the bullet's *source* is the path right after its id
        # prefix. A path cited later in running prose is a trail, not a source.
        lead = None
        head = body[:400]
        prefix = re.match(r"\s*[-*]\s*(?:KTD-[A-Z0-9]+-S-\d+\s*[\u2014\u2013-]\s*)?", head)
        start = prefix.end() if prefix else 0
        lead_m = re.match(r"\s*`((?:corpus|tools|reports|examples)/[^`\s]+)`", head[start:])
        if lead_m:
            lead = lead_m.group(1)
        else:
            lead_m = re.match(r"\s*((?:corpus|tools|reports|examples)/[\w./-]+)", head[start:])
            if lead_m:
                lead = lead_m.group(1)
        # Adjacency: `` `path` (sha256 `abc…`) `` — only punctuation between.
        adjacent = None
        for pm in REPO_PATH_RE.finditer(head[:m.start() - _off + 200] if m.start() > _off else head):
            between = head[pm.end():m.start() - _off]
            if re.fullmatch(r"[\s`,;:()\[\]{}~*_\-]{0,40}", between):
                adjacent = pm.group(1)
        if HISTORICAL_PIN_RE.search(body):
            checks.append({"digest": digest, "path": None,
                           "verdict": "historical-self-digest",
                           "why": "the bullet marks the digest as a past state of this file"})
            continue
        # A resolvable source path is graded even when the bullet also names a
        # revision: the digest either matches the live bytes or it does not, and
        # refusing to look would hide a real drift. The revision binding is
        # recorded beside the verdict rather than used to skip the check.
        path = adjacent or lead
        revision_bound = bool(re.search(r"at lane revision|at revision|read at `[0-9a-f]{7,40}`", body))
        if path is not None and (root / path).exists():
            actual = sha256_file(root / path)
            rec = {"digest": digest, "path": path,
                   "verdict": "re-derived" if actual.startswith(digest) else "drift",
                   "actual": actual[:len(digest)]}
            if revision_bound:
                rec["revision_bound"] = True
            checks.append(rec)
            continue
        if path is None and (
                REMOTE_PIN_RE.search(body) or re.search(r"[\d,]{3,}\s*(?:B|bytes)\b", body)):
            checks.append({"digest": digest, "path": None,
                           "verdict": "remote-artifact",
                           "why": "the bullet is about a fetched page or download"})
            continue
        if revision_bound:
            checks.append({"digest": digest, "path": None,
                           "verdict": "revision-bound",
                           "why": "the bullet attributes the digest to a past lane revision"})
            continue
        if path is None:
            checks.append({"digest": digest, "path": None, "verdict": "unbound",
                           "why": "the bullet names no repo path"})
            continue
        checks.append({"digest": digest, "path": path, "verdict": "unresolved-path",
                       "why": "the bullet's source path does not exist"})
    return checks


def bre_to_python(pattern):
    """Translate a POSIX BRE pattern (what `grep -rln` actually runs) to Python.

    The entries quote shell commands, so the pattern is a **basic** regular
    expression: `\\|` is alternation while a bare `|` is a literal pipe, and the
    same inversion holds for `(`, `)`, `+`, `?`, `{`. Compiling a BRE string
    straight with `re.compile` silently reinterprets it — measured: the round-19
    entry `gate-battery-surface-verification.md` quotes
    `grep -rln "check-gate-battery\\|gate battery\\|battery_exit" corpus/knowledge/`
    → 0 files, and Python reads `\\|` as a *literal* pipe, so the sweep appears to
    reproduce when the real `grep` returns a hit. That is a false green, the one
    error an auditor must not make, so the translation is explicit here.
    """
    out, i = [], 0
    while i < len(pattern):
        ch = pattern[i]
        if ch == "\\" and i + 1 < len(pattern):
            nxt = pattern[i + 1]
            if nxt in "|()+?{}":
                out.append(nxt)          # BRE escaped operator -> ERE operator
            elif nxt == "n":
                out.append("\n")
            elif nxt == "t":
                out.append("\t")
            else:
                out.append(re.escape(nxt))
            i += 2
            continue
        if ch in "|()+?{}":
            out.append(re.escape(ch))    # bare operator in BRE is a literal
        else:
            out.append(ch)
        i += 1
    return "".join(out)


def check_sweeps(text, root, self_path):
    """Quoted `grep -rln "<pat>" <dir> -> 0` lines re-run minus the entry itself."""
    out = []
    for m in SWEEP_RE.finditer(text):
        pattern, target = m.group("pattern"), m.group("path").rstrip(".,;")
        tail = text[m.end():m.end() + 200]
        claims_zero = bool(SWEEP_ZERO_RE.search(tail))
        rec = {"pattern": pattern, "path": target, "claims_zero": claims_zero}
        target_path = root / target
        if not target_path.exists():
            rec["verdict"] = "target-absent"
            out.append(rec)
            continue
        try:
            rx = re.compile(bre_to_python(pattern))
        except re.error:
            rec["verdict"] = "unparsable-pattern"
            out.append(rec)
            continue
        hits, self_hit = [], False
        for dirpath, _dirnames, filenames in os.walk(target_path):
            for name in sorted(filenames):
                if not name.endswith((".md", ".py", ".yml", ".json", ".tsv", ".txt")):
                    continue
                fp = os.path.join(dirpath, name)
                try:
                    body = open(fp, "rb").read().decode("utf-8")
                except (OSError, UnicodeDecodeError):
                    continue
                if rx.search(body):
                    rel = os.path.relpath(fp, root)
                    if os.path.abspath(fp) == os.path.abspath(str(self_path)):
                        self_hit = True
                    else:
                        hits.append(rel)
        rec["hits"] = hits
        rec["self_hit"] = self_hit
        if not claims_zero:
            rec["verdict"] = "no-zero-claim"
        elif hits:
            rec["verdict"] = "does-not-reproduce"
        else:
            rec["verdict"] = "reproduces"
        out.append(rec)
    return out


def audit_entry(path, root, offline=False):
    text = read_text(path)
    if not NOT_ENTRY_RE.search(text):
        raise CannotEvaluate(f"{path}: not an entry document (no heading, no header line)")
    fields, missing = check_frontmatter(text)
    gap_ok, gap_form, gap_text = check_gap(text)
    dec_ok, dec_head = check_decision(text)
    resolved, unresolved, exempt, urls = check_locators(text, root, offline)
    pins = check_pins(text, root)
    sweeps = check_sweeps(text, root, path)
    findings = []
    if missing:
        findings.append({"id": "X63-A", "kind": "missing-frontmatter",
                         "detail": missing})
    if not gap_ok:
        findings.append({"id": "X63-B", "kind": "gap-not-named", "detail": "no gap field or heading"})
    if not dec_ok:
        findings.append({"id": "X63-C", "kind": "no-decision-record", "detail": "no decision-record heading"})
    for u in unresolved:
        findings.append({"id": "X63-D", "kind": "unresolved-locator", "detail": u})
    for p in pins:
        if p["verdict"] in ("drift", "unresolved-path"):
            findings.append({"id": "X63-E", "kind": f"pin-{p['verdict']}", "detail": p})
    for s in sweeps:
        if s["verdict"] == "does-not-reproduce":
            findings.append({"id": "X63-F", "kind": "sweep-does-not-reproduce",
                             "detail": {"pattern": s["pattern"], "path": s["path"],
                                        "pre_existing_hits": s["hits"]}})
    return {
        "entry": str(path),
        "sha256": sha256_file(path),
        "bytes": os.path.getsize(path),
        "lines": text.count("\n") + (0 if text.endswith("\n") else 1),
        "frontmatter": {"present": sorted(fields), "missing": missing},
        "gap": {"named": gap_ok, "form": gap_form, "text": gap_text},
        "decision_record": {"present": dec_ok, "heading": dec_head},
        "calibration_vocabulary": bool(CALIBRATION_RE.search(text)),
        "locators": {"resolved": resolved, "unresolved": unresolved,
                     "declared_absent": exempt, "urls": urls},
        "pins": pins,
        "sweeps": sweeps,
        "findings": findings,
    }


# --------------------------------------------------------------------------
# selftest
# --------------------------------------------------------------------------

CLEAN_ENTRY = """# Register strata for attestation speech

- topic: How a marked attestation register is separated from the plain baseline
- gap filled: the corpus covers politeness and taboo but no entry covers the
  marked-register discipline; absence sweep 2026-10-18: `grep -rln "attestation register" corpus/knowledge/linguistics/` → 0 files
- sources:
  - KTD-RS-S-0001 — `reports/round-26/register/design.md` (read at the round-26 stamp)
  - KTD-RS-S-0002 — `corpus/QUALITY.md` — the admission bar
- calibration: this is house policy, not a published standard
- couples: linguistics — `sociolinguistics-registers.md`
- verified-at: 2026-10-18 — re-measured at lane root
- recheck: when the register design changes

## 1. What this entry licenses

Nothing about any world.

## 6. Decision record

DR-RS-01: the marked register is the scope unit.
"""

DEFECT_MISSING_FRONTMATTER = """# Thin entry

- topic: something
- couples: nothing

## 6. Decision record

DR-01: x
"""

DEFECT_NO_GAP = """# No gap named

- topic: something
- sources:
  - KTD-X-S-0001 — `corpus/QUALITY.md`
- calibration: house policy
- couples: none
- verified-at: 2026-10-18
- recheck: never

## 6. Decision record

DR-01: x
"""

DEFECT_NO_DECISION = """# No decision record

- topic: something
- gap filled: a real gap
- sources:
  - KTD-X-S-0001 — `corpus/QUALITY.md`
- calibration: house policy
- couples: none
- verified-at: 2026-10-18
- recheck: never

## 1. Body
"""

DEFECT_UNRESOLVED = """# Broken locator

- topic: something
- gap filled: a real gap
- sources:
  - KTD-X-S-0001 — `reports/round-99/nope.md`
- calibration: house policy
- couples: none
- verified-at: 2026-10-18
- recheck: never

## 6. Decision record

DR-01: x
"""

CLEAN_DECLARED_ABSENT = """# Declared absent is not broken

- topic: something
- gap filled: a real gap
- sources:
  - KTD-X-S-0001 — `corpus/QUALITY.md`; `reports/round-4/audit.md` **not filed**
- calibration: house policy
- couples: none
- verified-at: 2026-10-18
- recheck: never

## 6. Decision record

DR-01: x
"""

DEFECT_PIN_DRIFT = """# Pin drift

- topic: something
- gap filled: a real gap
- sources:
  - KTD-X-S-0001 — `corpus/QUALITY.md` (sha256 `deadbeefdeadbeef`)
- calibration: house policy
- couples: none
- verified-at: 2026-10-18
- recheck: never

## 6. Decision record

DR-01: x
"""

DEFECT_SWEEP_FALSE = """# Sweep does not reproduce

- topic: something
- gap filled: a real gap; absence sweep 2026-10-18: `grep -rln "admission bar" corpus/knowledge/linguistics/` → 0 files
- sources:
  - KTD-X-S-0001 — `corpus/QUALITY.md`
- calibration: house policy
- couples: none
- verified-at: 2026-10-18
- recheck: never

## 6. Decision record

DR-01: x
"""


def selftest(scratch_root):
    failures = []
    controls = 0
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    tmp = tempfile.mkdtemp(prefix="x63-selftest-", dir=scratch_root)
    try:
        corpus = os.path.join(tmp, "corpus", "knowledge", "linguistics")
        os.makedirs(corpus)
        reports = os.path.join(tmp, "reports", "round-26", "register")
        os.makedirs(reports)
        open(os.path.join(reports, "design.md"), "w").write("# design\n")
        open(os.path.join(tmp, "corpus", "QUALITY.md"), "w").write("# bar\n")

        def plant(name, body):
            nonlocal controls
            controls += 1
            p = os.path.join(corpus, name)
            open(p, "w").write(body)
            return p

        # A clean entry: green, zero findings.
        clean = plant("clean.md", CLEAN_ENTRY)
        rec = audit_entry(clean, _Path(tmp), offline=True)
        if rec["findings"]:
            failures.append(f"clean entry should be green, got {rec['findings']}")
        if not rec["gap"]["named"] or not rec["decision_record"]["present"]:
            failures.append("clean entry: gap/decision not detected")
        if "reports/round-26/register/design.md" not in rec["locators"]["resolved"]:
            failures.append("clean entry: a live locator was not resolved")

        # One planted control per defect class.
        cases = [
            ("missing-frontmatter", DEFECT_MISSING_FRONTMATTER, "X63-A"),
            ("no-gap", DEFECT_NO_GAP, "X63-B"),
            ("no-decision", DEFECT_NO_DECISION, "X63-C"),
            ("unresolved", DEFECT_UNRESOLVED, "X63-D"),
            ("pin-drift", DEFECT_PIN_DRIFT, "X63-E"),
            ("sweep-false", DEFECT_SWEEP_FALSE, "X63-F"),
        ]
        for name, body, want in cases:
            p = plant(name + ".md", body)
            rec = audit_entry(p, _Path(tmp), offline=True)
            ids = {f["id"] for f in rec["findings"]}
            if want not in ids:
                failures.append(f"{name}: expected finding {want}, got {sorted(ids) or 'none'}")

        # Declared-absent exemption: a negative claim must not read as a defect.
        p = plant("declared-absent.md", CLEAN_DECLARED_ABSENT)
        rec = audit_entry(p, _Path(tmp), offline=True)
        ids = {f["id"] for f in rec["findings"]}
        if "X63-D" in ids:
            failures.append("declared-absent: the exemption did not apply")
        if not rec["locators"]["declared_absent"]:
            failures.append("declared-absent: the exemption was silent")

        # A true sweep reproduces against the planted tree.
        p = plant("sweep-true.md",
                  CLEAN_ENTRY.replace('"attestation register"', '"nothing matches this at all"'))
        rec = audit_entry(p, _Path(tmp), offline=True)
        verdicts = {s["verdict"] for s in rec["sweeps"]}
        if "does-not-reproduce" in verdicts:
            failures.append("true sweep: a matching-free sweep was reported red")

        # A BRE `\|` alternation must be read as alternation, not as a literal
        # pipe. This is the false-green control: the planted pattern has one
        # branch that matches a file in the tree and one that matches nothing.
        p = plant("sweep-bre.md",
                  CLEAN_ENTRY.replace('"attestation register"',
                                      '"admission bar\\|nothing matches this"'))
        rec = audit_entry(p, _Path(tmp), offline=True)
        sw = rec["sweeps"][0] if rec["sweeps"] else None
        if sw is None:
            failures.append("BRE sweep: the quoted command was not parsed")
        elif sw["verdict"] != "does-not-reproduce":
            failures.append("BRE sweep: `\\|` alternation read as a literal pipe "
                            f"(verdict {sw['verdict']})")

        # A historical self-digest must NOT be scored as a drifted pin.
        hist = CLEAN_ENTRY.replace(
            "- calibration: this is house policy, not a published standard",
            "- calibration: this is house policy, not a published standard\n"
            "- **2026-10-17 — source recheck (baseline fe34faa; entry sha256 before append "
            "`8272a8f606b72504f433dc163f1ca545a43e99feb6a6572e8bb0a080c1bf738d`):** a past state")
        p = plant("historical-digest.md", hist)
        rec = audit_entry(p, _Path(tmp), offline=True)
        ids = {f["id"] for f in rec["findings"]}
        if "X63-E" in ids:
            failures.append("historical self-digest was scored as a pin drift")
        if not any(c["verdict"] == "historical-self-digest" for c in rec["pins"]):
            failures.append("historical self-digest was not recognised at all")

        # A remote-artifact digest is the digest of a fetched page/download. It
        # can never re-derive from the tree, and a repo path cited elsewhere in
        # the same clause is a trail, not a binding.
        remote = CLEAN_ENTRY.replace(
            "  - KTD-RS-S-0001 — `reports/round-26/register/design.md` (read at the round-26 stamp)",
            "  - KTD-RS-S-0001 — locators re-attempted 2026-10-18 "
            "(`reports/round-26/register/design.md`): the transcription "
            "(raw snapshot 130,398 B, sha256 `27d6a210bfc3a88da9015e52537c51f6b529411b`); "
            "the design itself read live")
        p = plant("remote-digest.md", remote)
        rec = audit_entry(p, _Path(tmp), offline=True)
        ids = {f["id"] for f in rec["findings"]}
        if "X63-E" in ids:
            failures.append("remote-artifact digest was scored as a pin drift")
        if not any(c["verdict"] == "remote-artifact" for c in rec["pins"]):
            failures.append("remote-artifact digest was not classified")

        # A non-adjacent repo path must not be bound to a digest: the sibling
        # tool's own false positive (mesoamerica-primary-sources.md) is this
        # shape, so it is planted here as a regression guard.
        nonadjacent = CLEAN_ENTRY.replace(
            "  - KTD-RS-S-0002 — `corpus/QUALITY.md` — the admission bar",
            "  - KTD-RS-S-0002 — see `corpus/QUALITY.md` for the bar; an unrelated "
            "page (sha256 `deadbeefdeadbeefdeadbeefdeadbeef`) was fetched")
        p = plant("nonadjacent-digest.md", nonadjacent)
        rec = audit_entry(p, _Path(tmp), offline=True)
        ids = {f["id"] for f in rec["findings"]}
        if "X63-E" in ids:
            failures.append("a non-adjacent path was bound to a digest (false positive)")

        # An adjacent path that really does not match MUST still be caught: the
        # fix must not blunt the leg it protects.
        still_caught = CLEAN_ENTRY.replace(
            "  - KTD-RS-S-0002 — `corpus/QUALITY.md` — the admission bar",
            "  - KTD-RS-S-0002 — `corpus/QUALITY.md` (sha256 `deadbeefdeadbeefdeadbeef`)")
        p = plant("adjacent-drift.md", still_caught)
        rec = audit_entry(p, _Path(tmp), offline=True)
        ids = {f["id"] for f in rec["findings"]}
        if "X63-E" not in ids:
            failures.append("adjacent-pin drift was no longer caught after the fix")

        # Non-entry documents are refused, not graded.
        plain = os.path.join(tmp, "corpus", "notes.txt")
        open(plain, "w").write("just a plain note, no heading and no header line\n")
        try:
            audit_entry(plain, _Path(tmp), offline=True)
            failures.append("non-entry document was graded instead of refused")
        except CannotEvaluate:
            pass
        try:
            audit_entry(os.path.join(tmp, "missing.md"), _Path(tmp), offline=True)
            failures.append("missing path was not refused")
        except CannotEvaluate:
            pass

        # The tool must be read-only over the repo root it audits.
        controls += 1
        probe = os.path.join(root, "corpus", "QUALITY.md")
        before = sha256_file(probe)
        audit_entry(probe, _Path(root), offline=True)
        if sha256_file(probe) != before:
            failures.append("read-only violated: an audited file changed")
    finally:
        shutil.rmtree(tmp, ignore_errors=True)
    return (0 if not failures else 1), failures, controls


class _Path:
    """A minimal pathlib-free path joiner so the tool stays dependency-light."""

    def __init__(self, base):
        self.base = base

    def __truediv__(self, other):
        return _Path(os.path.join(self.base, other))

    def exists(self):
        return os.path.exists(self.base)

    def __str__(self):
        return self.base

    def __fspath__(self):
        return self.base


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("entries", nargs="*", help="entry documents to audit")
    parser.add_argument("--root", default=None, help="repository root (default: this file's repo)")
    parser.add_argument("--json", action="store_true", help="emit the full receipt JSON")
    parser.add_argument("--offline", action="store_true", help="skip URL access attempts")
    parser.add_argument("--selftest", action="store_true")
    parser.add_argument("--scratch", default=None, help="scratch dir for --selftest")
    args = parser.parse_args(argv)

    scratch = args.scratch or os.environ.get("TMPDIR") or tempfile.gettempdir()
    if args.selftest:
        os.makedirs(scratch, exist_ok=True)
        code, failures, controls = selftest(scratch)
        for f in failures:
            print(f"SELFTEST FAIL: {f}", file=sys.stderr)
        print(f"SELFTEST {'PASS' if not code else 'FAIL'}: {controls} planted controls "
              f"(a clean entry, six defect classes, the declared-absent exemption, a "
              f"reproducing sweep, a BRE-alternation sweep, a historical self-digest, a "
              f"remote-artifact digest, a non-adjacent path, a still-caught adjacent drift, "
              f"two refusal controls and the read-only control); failures={len(failures)}")
        return code

    if not args.entries:
        parser.error("no entry given (or use --selftest)")

    root = _Path(args.root or os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", "..")))
    receipts, findings = [], []
    for entry in args.entries:
        try:
            rec = audit_entry(entry, root, offline=args.offline)
        except CannotEvaluate as exc:
            print(f"CANNOT-EVALUATE: {exc}", file=sys.stderr)
            return 2
        receipts.append(rec)
        findings.extend(rec["findings"])

    if args.json:
        print(json.dumps({"schema": SCHEMA, "root": str(root),
                          "observed_at_utc": _now(), "entries": receipts,
                          "findings": findings}, indent=1, ensure_ascii=False))
    else:
        for f in findings:
            print(f"FINDING {f['id']}: {f['kind']}: {json.dumps(f['detail'], ensure_ascii=False)}")
        for rec in receipts:
            print(f"INFO entry: {rec['entry']} sha256={rec['sha256'][:16]} "
                  f"locators={len(rec['locators']['resolved'])} unresolved={len(rec['locators']['unresolved'])} "
                  f"exempt={len(rec['locators']['declared_absent'])} pins={len(rec['pins'])} "
                  f"sweeps={len(rec['sweeps'])}")
        print(f"INFO scan: entries={len(receipts)} findings={len(findings)}")
    return 1 if findings else 0


def _now():
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


if __name__ == "__main__":
    sys.exit(main())
