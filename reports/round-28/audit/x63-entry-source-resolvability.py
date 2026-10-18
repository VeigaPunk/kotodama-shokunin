#!/usr/bin/env python3
"""x63-entry-source-resolvability — round-28 read-only entry auditor.

Audits corpus entry documents (never culture packets, never round fragments)
against the round-10/round-19 audit bar this lane's entries are held to, the
pin and sweep surfaces later rounds added, and the three surfaces round 28
adds because claim C is an *amendment plus a new entry* rather than a single
landing:

  X63-A  frontmatter      every lane-bar field present and non-empty
  X63-B  gap              the entry names the gap it fills
  X63-C  decision record  a `## … decision record …` heading exists
  X63-D  locators         every repo-path locator resolves on disk
  X63-E  pins             every `sha256` bound to a named repo path re-derives
  X63-F  sweeps           every quoted absence sweep reproduces
  X63-G  amendment        an amended entry must be **append/insert only**: no
                          line present at the declared baseline may be deleted
                          or rewritten (the round-28 rule that a correction is
                          a NEW section, never an in-place rewrite)
  X63-H  ceiling          the register-lexicon ceiling is recorded **as a
                          design constraint** and the record cites the round-27
                          measurements that produced it (RL-3)

The tool is a **resolvability** instrument, not a merits instrument. It does
not judge whether a source is the right source, whether a calibration is
warranted, whether the ceiling is real, or whether a gap is worth filling. A
locator that resolves is reported as resolved even when the source it names is
weak; a finding is only ever "the document says X and the bytes say not-X".

The declared-absent exemption. A cell that names a path and *states in the same
cell* that the path was never filed (`no `reports/round-4*` exists`, `not
filed`, `absent`, `never existed`) is exempt from the resolution check: the
entry is making a negative claim, and reading it as a broken link inverts its
meaning. The exemption is reported, never silent.

Negative controls. `--selftest` plants one clean entry and one entry per defect
class in a temp tree under $TMPDIR, and asserts the exit code and the finding
ids. A check that cannot fail is not a check, so every check here has a planted
control that makes it fire — including the two round-28 legs, which are
exercised against a planted amendment (a preserved line and a rewritten line)
and against a planted ceiling record (present and absent).

Read-only by construction: no code path opens a file for writing except the
selftest's own temp tree, which is created under `--scratch` (default $TMPDIR)
and removed at the end. Network access is attempted only for URL locators, is
bounded to a few seconds, and its outcome is recorded as an observation.
`--offline` suppresses the attempt and records `not-attempted`.

Target location. With `--baseline <rev>` the audited set is derived from the
tree, never guessed: `git ls-tree` at the baseline vs the live worktree gives
the **new** files, and a blob comparison gives the **amended** ones. A round
that lands two entries audits both; a round that amends one audits one; a round
that lands none reports `no-target`.

Output: one line per finding on stdout, then an `INFO scan:` summary line; with
`--json`, the full receipt object on stdout instead. Exit codes: 0 clean;
1 findings; 2 could-not-evaluate (missing path, not an entry document,
unreadable, or not UTF-8 text), also 2 for argparse usage errors. `--selftest`
exits 0 when every planted control behaves as asserted, 1 when one does not.

Stdlib only.
"""

from __future__ import annotations

import argparse
import difflib
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

SCHEMA = "kotodama-entry-source-resolvability-x63-r28-v1"

# The frontmatter bar. Kept identical to the round-10 acceptance constant
# (reports/round-10/run-validation.py) so a green here is comparable with a
# green there; `gap` is checked separately because it has a field form and a
# heading form.
FRONTMATTER_FIELDS = ("topic", "sources", "verified-at", "recheck", "couples")

# Locators: repo-relative paths, the shape the lane's entries actually use.
# A locator may carry a line-range suffix (`file.md:88-98`, `file.md:92,121`),
# which names a *passage* of the file, not a different path — stripping it is
# what makes the locator resolvable.
REPO_PATH_RE = re.compile(
    r"\b((?:corpus|tools|reports|examples|\.ufo)/[\w./*\-]+\.(?:md|py|yml|json|tsv|txt|jsonl|yaml))"
    r"(?::[0-9][0-9,\-]*)?"
)
LINE_SUFFIX_RE = re.compile(r":\d[\d,\-]*$")
BRACE_RE = re.compile(r"\{([^{}]+)\}")
URL_RE = re.compile(r"https?://[^\s`)\]<>]+")

GAP_FIELD_RE = re.compile(
    r"(?i)(?:^|[\s.;\u2014\u2013|-])gap(?:[\s-]+(?:filled|addressed|served))?\s*:\s*(\S[^\n]{0,300})"
)
GAP_HEADING_RE = re.compile(r"(?mi)^#{2,4}[^\n]*\bgap\b[^\n]*$")
DECISION_RE = re.compile(r"(?mi)^#{2,4}[^\n]*decision[- ]record[^\n]*$")
CALIBRATION_RE = re.compile(r"(?i)calibrat")

# A quoted absence sweep. Two forms are recognised, because the lane uses both
# and round 27's limit named the second as the missing improvement:
#   `grep -rln "<pattern>" <path> -> 0 files`            (the count form)
#   `grep -rl -i "<pattern>" <path> | wc -l -> 0`        (the piped-count form)
# The second is how the round-27 entry quotes all five of its sweeps, and the
# round-27 audit recorded that neither leg scored them — a green sweep column
# that no instrument produced. Recognising it is what closes that limit.
SWEEP_RE = re.compile(
    r"grep\s+-rl[n]?\s+(?P<flags>(?:-[a-zA-Z]+\s+)*)[\"'\u201c](?P<pattern>[^\"'\u201d]+)[\"'\u201d]\s+"
    r"(?P<path>[^\s;`|)\u2014]+)(?P<pipe>\s*\|\s*wc\s+-l)?"
)
SWEEP_ZERO_RE = re.compile(r"(?:→|->)\s*\*{0,2}0\b")

DECLARED_ABSENT_RE = re.compile(
    r"(?i)(not filed|never filed|never existed|no such file|absent|does not exist|"
    r"not round-numbered|no `[^`]+` exists|no `[^`]+` at)"
)

NOT_ENTRY_RE = re.compile(r"(?m)^(#{1,6}\s+\S|[-*]\s+[A-Za-z][A-Za-z-]*\s*:)")

# --- round-28 legs -------------------------------------------------------

# The ceiling record: the register cannot spell its own law's vocabulary.
CEILING_RE = re.compile(r"(?i)\bceiling\b")
CONSTRAINT_RE = re.compile(
    r"(?i)(design constraint|design bound|constrains?|a constraint|"
    r"bounds? the design|limits? (?:what|which))"
)
ROUND27_RE = re.compile(r"(?i)(round[- ]?27|reports/round-27/|RL-3\b|RL3\b)")

# The canon boundary: this lane generates systems, never canon. A presence
# check (the entry must say so), never a keyword hunt for violations.
CANON_BOUNDARY_RE = re.compile(
    r"(?i)(not canon|never canon|no canon claim|canon decisions belong|"
    r"NON-CANON|canon (?:is|belongs to) lore)"
)


class CannotEvaluate(Exception):
    """The named path cannot be graded as an entry document."""


def sha256_file(path):
    h = hashlib.sha256()
    with open(path, "rb") as fh:
        for chunk in iter(lambda: fh.read(1 << 16), b""):
            h.update(chunk)
    return h.hexdigest()


def sha256_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


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


def expand_braces(token):
    """Expand `a{b,c}d` into `abd`, `acd`; a token without braces yields itself."""
    m = BRACE_RE.search(token)
    if not m:
        return [token]
    out = []
    for alt in m.group(1).split(","):
        out.extend(expand_braces(token[:m.start()] + alt + token[m.end():]))
    return out


def header_lines(text, limit=40):
    return text.splitlines()[:limit]


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
                                 headers={"User-Agent": "kotodama-x63-r28-resolvability/1"})
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
REMOTE_PIN_RE = re.compile(
    r"(?i)(https?://|web\.archive\.org|raw snapshot|downloaded|fetched|"
    r"retrieved from|transcription)"
)


def _bullets(text):
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


def check_pins(text, root):
    """A pin is a digest bound to the **source path the bullet opens with**.

    The lane's source bullets have the shape
    ``- KTD-XX-S-NNNN — `path` (… sha256 `abc…` …): prose``. The path right
    after the id is the source the bullet is about, and a digest in that bullet
    is a claim about **that** file. Four classes are reported, and only
    ``re-derived``/``drift`` are graded: ``remote-artifact`` (a fetched page or
    download cannot re-derive from the tree), ``historical-self-digest`` (the
    record of this file's own past bytes, *supposed* not to match), and
    ``revision-bound``/``unbound`` (the digest is attributed to a past lane
    revision or names no repo path).
    """
    checks = []
    spans = _bullets(text)
    for m in re.finditer(r"sha256[^\n]{0,60}?([0-9a-f]{12,64})", text):
        digest = m.group(1)
        body, _off = _bullet_of(spans, m.start())
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
    straight with `re.compile` silently reinterprets it — measured in round 19,
    the entry `gate-battery-surface-verification.md` quotes
    `grep -rln "check-gate-battery\\|gate battery\\|battery_exit" corpus/knowledge/`
    → 0 files, and Python reads `\\|` as a *literal* pipe, so the sweep appears
    to reproduce when the real `grep` returns a hit. That is a false green, the
    one error an auditor must not make, so the translation is explicit here.
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


def check_sweeps(text, root, self_path, baseline_rev=None, self_rel=None):
    """Quoted `grep -rl[n] [-i] "<pat>" <dir> [| wc -l] -> 0` lines re-run.

    The count form and the piped-count form are both scored; the `-i` flag is
    honoured so a case-insensitive sweep is reproduced case-insensitively rather
    than silently read as case-sensitive (which would manufacture a false green
    on any sweep whose pattern only matches in another case).

    **A non-reproducing sweep is classified, not just reported.** In a parallel
    wave a sibling seat can land a document *between* the moment an entry was
    authored and the moment it is audited, so a sweep that was true when written
    reads false now. That is a different finding from a sweep that was false when
    written, and only the second is an authoring defect. When `--baseline` is
    given, the same pattern is re-run at the baseline revision with `git grep`,
    **excluding the audited document itself** (the lane's sweeps say "over
    `corpus/knowledge/` minus this entry", so the entry's own text must not count
    as a pre-existing hit — counting it would call every self-referential sweep
    an authoring defect). A surviving hit means the sweep was false when written
    (`authoring-defect`); no surviving hit means the sweep was true and a sibling
    landing broke it (`sibling-landing`). Without a baseline the leg reports the
    plain `does-not-reproduce` and says the classification was not attempted,
    rather than guessing.
    """
    out = []
    for m in SWEEP_RE.finditer(text):
        pattern, target = m.group("pattern"), m.group("path").rstrip(".,;")
        tail = text[m.end():m.end() + 200]
        claims_zero = bool(SWEEP_ZERO_RE.search(tail))
        flags = m.group("flags")
        ignore_case = bool(flags and re.search(r"-i\b", flags))
        rec = {"pattern": pattern, "path": target, "claims_zero": claims_zero,
               "ignore_case": ignore_case, "piped_count": bool(m.group("pipe"))}
        target_path = root / target
        if not target_path.exists():
            rec["verdict"] = "target-absent"
            out.append(rec)
            continue
        try:
            rx = re.compile(bre_to_python(pattern), re.IGNORECASE if ignore_case else 0)
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
            if baseline_rev:
                base_hits = _baseline_sweep_hits(baseline_rev, pattern, target,
                                                 ignore_case, root)
                if self_rel:
                    base_hits = [h for h in base_hits if h != self_rel]
                rec["baseline_hits"] = base_hits
                rec["verdict"] = ("authoring-defect" if base_hits
                                  else "sibling-landing")
        else:
            rec["verdict"] = "reproduces"
        out.append(rec)
    return out


def _baseline_sweep_hits(baseline_rev, pattern, target, ignore_case, root):
    """Paths matching `pattern` under `target` **at the baseline revision**.

    Run with `git grep -G` (BRE, matching the quoted command's dialect) so the
    baseline reading is taken with the real tool over the real revision rather
    than by re-reading a checkout. A git failure returns `[]` and is reported by
    the caller as "no baseline hits" — the leg errs toward calling a row an
    authoring defect only when the evidence says so, and the receipt carries the
    empty list.
    """
    cmd = ["git", "grep", "-l", "-G"] + (["-i"] if ignore_case else []) + \
          ["-e", pattern, baseline_rev, "--", target]
    try:
        proc = subprocess.run(cmd, cwd=str(root), capture_output=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired):
        return []
    if proc.returncode not in (0, 1):   # 1 = no match, which is a clean negative
        return []
    prefix = baseline_rev + ":"
    out = []
    for line in proc.stdout.decode("utf-8", "replace").split("\n"):
        line = line.strip()
        if not line:
            continue
        out.append(line[len(prefix):] if line.startswith(prefix) else line)
    return out


def check_amendment(baseline_text, live_text, sample=8):
    """Append/insert-only: no baseline line may be deleted or rewritten.

    The round-28 rule is that a correction to a filed entry is a **new section**
    or a new file, never an in-place rewrite. The check is a line-level diff
    (`difflib.SequenceMatcher`), so a single rewritten line costs exactly one
    deleted row.

    **A greedy pointer walk is wrong here and was measured wrong.** Advancing a
    pointer only on equality desynchronises the moment a line is rewritten: the
    pointer stalls at the first changed baseline line and every later baseline
    line is then reported as deleted. Measured on a planted one-line rewrite of
    the round-27 entry, the greedy walk reported `deleted_or_rewritten: 311`
    against the true count of 1 — a finding whose *existence* was right and
    whose *magnitude* was fabricated. A count a consumer will read must not be
    produced that way, so the diff is computed properly.
    """
    base_lines = baseline_text.splitlines()
    live_lines = live_text.splitlines()
    sm = difflib.SequenceMatcher(None, base_lines, live_lines, autojunk=False)
    deleted, inserted = [], 0
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag in ("replace", "delete"):
            deleted.extend(base_lines[i1:i2])
        if tag in ("replace", "insert"):
            inserted += j2 - j1
    return {
        "baseline_lines": len(base_lines),
        "live_lines": len(live_lines),
        "preserved": len(base_lines) - len(deleted),
        "inserted": inserted,
        "deleted_or_rewritten": len(deleted),
        "sample_deleted": [l[:160] for l in deleted[:sample]],
        "append_only": not deleted,
    }


def check_ceiling(text):
    """The ceiling recorded as a design constraint, citing the round-27 numbers."""
    ceiling = bool(CEILING_RE.search(text))
    constraint = bool(CONSTRAINT_RE.search(text))
    cites = bool(ROUND27_RE.search(text))
    samples = {}
    if ceiling:
        m = CEILING_RE.search(text)
        samples["ceiling"] = text[max(0, m.start() - 80):m.start() + 160].replace("\n", " ")[:240]
    if cites:
        m = ROUND27_RE.search(text)
        samples["round27"] = text[max(0, m.start() - 80):m.start() + 160].replace("\n", " ")[:240]
    return {"ceiling_named": ceiling, "constraint_language": constraint,
            "cites_round27": cites, "samples": samples,
            "recorded_as_constraint": ceiling and constraint and cites}


def check_canon_boundary(text):
    m = CANON_BOUNDARY_RE.search(text)
    return {"stated": bool(m),
            "sample": (text[max(0, m.start() - 40):m.start() + 160].replace("\n", " ")[:200]
                       if m else "")}


def audit_entry(path, root, offline=False, baseline_text=None, baseline_rev=None,
                self_rel=None):
    text = read_text(path)
    if not NOT_ENTRY_RE.search(text):
        raise CannotEvaluate(f"{path}: not an entry document (no heading, no header line)")
    fields, missing = check_frontmatter(text)
    gap_ok, gap_form, gap_text = check_gap(text)
    dec_ok, dec_head = check_decision(text)
    resolved, unresolved, exempt, urls = check_locators(text, root, offline)
    pins = check_pins(text, root)
    sweeps = check_sweeps(text, root, path, baseline_rev=baseline_rev,
                          self_rel=self_rel)
    amendment = None
    if baseline_text is not None:
        amendment = check_amendment(baseline_text, text)
    ceiling = check_ceiling(text)
    canon = check_canon_boundary(text)

    findings = []
    if missing:
        findings.append({"id": "X63-A", "kind": "missing-frontmatter", "detail": missing})
    if not gap_ok:
        findings.append({"id": "X63-B", "kind": "gap-not-named",
                         "detail": "no gap field or heading"})
    if not dec_ok:
        findings.append({"id": "X63-C", "kind": "no-decision-record",
                         "detail": "no decision-record heading"})
    for u in unresolved:
        findings.append({"id": "X63-D", "kind": "unresolved-locator", "detail": u})
    for p in pins:
        if p["verdict"] in ("drift", "unresolved-path"):
            findings.append({"id": "X63-E", "kind": f"pin-{p['verdict']}", "detail": p})
    for s in sweeps:
        if s["verdict"] in ("does-not-reproduce", "authoring-defect", "sibling-landing"):
            findings.append({"id": "X63-F", "kind": f"sweep-{s['verdict']}",
                             "detail": {"pattern": s["pattern"], "path": s["path"],
                                        "pre_existing_hits": s["hits"],
                                        "baseline_hits": s.get("baseline_hits")}})
    if amendment is not None and not amendment["append_only"]:
        findings.append({"id": "X63-G", "kind": "amendment-not-append-only",
                         "detail": {"deleted_or_rewritten": amendment["deleted_or_rewritten"],
                                    "sample_deleted": amendment["sample_deleted"]}})
    if not ceiling["recorded_as_constraint"]:
        findings.append({"id": "X63-H", "kind": "ceiling-not-recorded-as-constraint",
                         "detail": {k: ceiling[k] for k in
                                    ("ceiling_named", "constraint_language", "cites_round27")}})
    return {
        "entry": str(path),
        "sha256": sha256_file(path),
        "bytes": os.path.getsize(path),
        "lines": text.count("\n") + (0 if text.endswith("\n") else 1),
        "baseline_rev": baseline_rev,
        "baseline_sha256": (sha256_bytes(baseline_text.encode("utf-8"))
                            if baseline_text is not None else None),
        "is_amendment": baseline_text is not None,
        "frontmatter": {"present": sorted(fields), "missing": missing},
        "gap": {"named": gap_ok, "form": gap_form, "text": gap_text},
        "decision_record": {"present": dec_ok, "heading": dec_head},
        "calibration_vocabulary": bool(CALIBRATION_RE.search(text)),
        "canon_boundary": canon,
        "amendment": amendment,
        "ceiling": ceiling,
        "locators": {"resolved": resolved, "unresolved": unresolved,
                     "declared_absent": exempt, "urls": urls},
        "pins": pins,
        "sweeps": sweeps,
        "findings": findings,
    }


# --------------------------------------------------------------------------
# target location by set difference against the declared baseline
# --------------------------------------------------------------------------

def _git(root, *args):
    try:
        out = subprocess.run(("git",) + args, cwd=str(root), capture_output=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired) as exc:
        raise CannotEvaluate(f"git {' '.join(args)} failed: {exc}")
    if out.returncode != 0:
        raise CannotEvaluate(f"git {' '.join(args)}: "
                             f"{out.stderr.decode('utf-8', 'replace').strip()[:200]}")
    return out.stdout


def locate_targets(root, baseline_rev, partition):
    """(new_paths, amended_paths) by Git identity, never by a guessed filename."""
    base = _git(root, "ls-tree", "-r", "--name-only", baseline_rev, "--", partition)
    live = _git(root, "ls-files", "--cached", "--others", "--exclude-standard", "--", partition)
    base_set = {p for p in base.decode("utf-8").split("\n") if p.strip()}
    live_set = {p for p in live.decode("utf-8").split("\n") if p.strip()}
    new = sorted(live_set - base_set)
    amended = []
    for rel in sorted(base_set & live_set):
        blob = _git(root, "show", f"{baseline_rev}:{rel}")
        disk = (root / rel)
        try:
            live_bytes = open(str(disk), "rb").read()
        except OSError:
            continue
        if sha256_bytes(blob) != sha256_bytes(live_bytes):
            amended.append(rel)
    return new, amended, sorted(base_set)


# --------------------------------------------------------------------------
# selftest
# --------------------------------------------------------------------------

CLEAN_ENTRY = """# Register-lexicon ceilings

- topic: Why a register's derivation operation bounds the semantic fields it can spell
- gap filled: the corpus covers register strata and speech acts but no entry
  states the ceiling a register's operation imposes on its own vocabulary;
  absence sweep 2026-10-18: `grep -rln "lexicon ceiling" corpus/knowledge/linguistics/` → 0 files
- sources:
  - KTD-RLC-S-0001 — `reports/round-26/register/design.md` (read at the round-26 stamp)
  - KTD-RLC-S-0002 — `corpus/QUALITY.md` — the admission bar
- calibration: this is house method, not a published standard
- couples: linguistics — `sociolinguistics-registers.md`
- verified-at: 2026-10-18 — re-measured at lane root
- recheck: when the register design changes
- canon: not canon; canon decisions belong to lore-shokunin

## 1. The ceiling as a design constraint

The round-27 measurements (RL-3) show the register cannot spell its own law's
vocabulary; the ceiling is a design constraint, not a defect.

## 6. Decision record

DR-RLC-01: the ceiling is recorded, not repaired.
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

DEFECT_NO_CEILING = """# Ceiling not recorded

- topic: something
- gap filled: a real gap
- sources:
  - KTD-X-S-0001 — `corpus/QUALITY.md`
- calibration: house policy
- couples: none
- verified-at: 2026-10-18
- recheck: never

## 1. Body

The register has forms and a law; nothing here records a bound.

## 6. Decision record

DR-01: x
"""


def selftest(scratch_root):
    failures = []
    controls = 0
    root = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "..", ".."))
    tmp = tempfile.mkdtemp(prefix="x63r28-selftest-", dir=scratch_root)
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

        clean = plant("clean.md", CLEAN_ENTRY)
        rec = audit_entry(clean, _Path(tmp), offline=True)
        if rec["findings"]:
            failures.append(f"clean entry should be green, got {rec['findings']}")
        if not rec["gap"]["named"] or not rec["decision_record"]["present"]:
            failures.append("clean entry: gap/decision not detected")
        if "reports/round-26/register/design.md" not in rec["locators"]["resolved"]:
            failures.append("clean entry: a live locator was not resolved")
        if not rec["ceiling"]["recorded_as_constraint"]:
            failures.append("clean entry: the ceiling record was not detected")
        if not rec["canon_boundary"]["stated"]:
            failures.append("clean entry: the canon boundary was not detected")

        cases = [
            ("missing-frontmatter", DEFECT_MISSING_FRONTMATTER, "X63-A"),
            ("no-gap", DEFECT_NO_GAP, "X63-B"),
            ("no-decision", DEFECT_NO_DECISION, "X63-C"),
            ("unresolved", DEFECT_UNRESOLVED, "X63-D"),
            ("pin-drift", DEFECT_PIN_DRIFT, "X63-E"),
            ("sweep-false", DEFECT_SWEEP_FALSE, "X63-F"),
            ("no-ceiling", DEFECT_NO_CEILING, "X63-H"),
        ]
        for name, body, want in cases:
            p = plant(name + ".md", body)
            rec = audit_entry(p, _Path(tmp), offline=True)
            ids = {f["id"] for f in rec["findings"]}
            if want not in ids:
                failures.append(f"{name}: expected finding {want}, got {sorted(ids) or 'none'}")

        p = plant("declared-absent.md", CLEAN_DECLARED_ABSENT)
        rec = audit_entry(p, _Path(tmp), offline=True)
        ids = {f["id"] for f in rec["findings"]}
        if "X63-D" in ids:
            failures.append("declared-absent: the exemption did not apply")
        if not rec["locators"]["declared_absent"]:
            failures.append("declared-absent: the exemption was silent")

        p = plant("sweep-true.md",
                  CLEAN_ENTRY.replace('"lexicon ceiling"', '"nothing matches this at all"'))
        rec = audit_entry(p, _Path(tmp), offline=True)
        if "does-not-reproduce" in {s["verdict"] for s in rec["sweeps"]}:
            failures.append("true sweep: a matching-free sweep was reported red")

        p = plant("sweep-bre.md",
                  CLEAN_ENTRY.replace('"lexicon ceiling"',
                                      '"admission bar\\|nothing matches this"'))
        rec = audit_entry(p, _Path(tmp), offline=True)
        sw = rec["sweeps"][0] if rec["sweeps"] else None
        if sw is None:
            failures.append("BRE sweep: the quoted command was not parsed")
        elif sw["verdict"] != "does-not-reproduce":
            failures.append("BRE sweep: `\\|` alternation read as a literal pipe "
                            f"(verdict {sw['verdict']})")

        # The piped-count form (`| wc -l`) and the `-i` flag: round 27's limit
        # named this form as unscored by either leg, and the round-27 entry
        # quotes all five of its sweeps in it. A true sweep must reproduce and a
        # false one must fire, in that form.
        piped_true = plant("sweep-piped-true.md",
                           CLEAN_ENTRY.replace(
                               '`grep -rln "lexicon ceiling" corpus/knowledge/linguistics/` → 0 files',
                               '`grep -rl -i "lexicon ceilingzzz" corpus/knowledge/linguistics/ | wc -l` → **0**'))
        rec = audit_entry(piped_true, _Path(tmp), offline=True)
        sw = rec["sweeps"][0] if rec["sweeps"] else None
        if sw is None or not sw.get("piped_count"):
            failures.append("piped sweep: the `| wc -l` form was not parsed")
        elif sw["verdict"] == "does-not-reproduce":
            failures.append("piped sweep: a matching-free sweep was reported red")

        piped_false = plant("sweep-piped-false.md",
                            CLEAN_ENTRY.replace(
                                '`grep -rln "lexicon ceiling" corpus/knowledge/linguistics/` → 0 files',
                                '`grep -rl -i "ADMISSION BAR" corpus/knowledge/linguistics/ | wc -l` → **0**'))
        rec = audit_entry(piped_false, _Path(tmp), offline=True)
        sw = rec["sweeps"][0] if rec["sweeps"] else None
        if sw is None:
            failures.append("piped sweep: the command was not parsed")
        elif sw["verdict"] != "does-not-reproduce":
            failures.append("piped sweep: a case-insensitive sweep that does match "
                            f"was not caught (verdict {sw['verdict']})")
        elif not sw.get("ignore_case"):
            failures.append("piped sweep: the `-i` flag was not honoured")

        # The baseline-aware classifier. In a parallel wave a sibling seat can
        # land a document between authoring and audit, so a sweep that was true
        # when written reads false now. That must be named `sibling-landing`,
        # not conflated with an authoring defect — and the control must exercise
        # both classes on a real git repo, or the classifier is untested.
        import subprocess as _sp
        grepo = os.path.join(tmp, "gitrepo")
        os.makedirs(os.path.join(grepo, "corpus", "knowledge", "linguistics"))
        open(os.path.join(grepo, "corpus", "knowledge", "linguistics", "sibling.md"), "w").write(
            "# sibling\n\nThis file mentions PRE-EXISTING TERM.\n")
        env = dict(os.environ, GIT_AUTHOR_NAME="t", GIT_AUTHOR_EMAIL="t@t",
                   GIT_COMMITTER_NAME="t", GIT_COMMITTER_EMAIL="t@t")
        for cmd in (["git", "init", "-q"], ["git", "add", "-A"],
                    ["git", "commit", "-q", "-m", "base"]):
            _sp.run(cmd, cwd=grepo, env=env, capture_output=True)
        base_rev = _sp.run(["git", "rev-parse", "HEAD"], cwd=grepo,
                           capture_output=True, text=True).stdout.strip()
        # A sibling lands AFTER the baseline, introducing a new term.
        open(os.path.join(grepo, "corpus", "knowledge", "linguistics", "newcomer.md"), "w").write(
            "# newcomer\n\nThis file mentions FRESH TERM.\n")
        # An authoring defect: the pattern already matched at the baseline.
        pre = plant("sweep-pre-existing.md",
                    CLEAN_ENTRY.replace('"lexicon ceiling"',
                                        '"PRE-EXISTING TERM"'))
        rec = audit_entry(pre, _Path(grepo), offline=True, baseline_rev=base_rev)
        sw = rec["sweeps"][0] if rec["sweeps"] else None
        if sw is None or sw["verdict"] != "authoring-defect":
            failures.append("classifier: a baseline-matching sweep was not called "
                            f"an authoring defect (verdict {sw and sw['verdict']})")
        # A sibling landing: the pattern did NOT match at the baseline.
        sib = plant("sweep-sibling.md",
                    CLEAN_ENTRY.replace('"lexicon ceiling"', '"FRESH TERM"'))
        rec = audit_entry(sib, _Path(grepo), offline=True, baseline_rev=base_rev)
        sw = rec["sweeps"][0] if rec["sweeps"] else None
        if sw is None or sw["verdict"] != "sibling-landing":
            failures.append("classifier: a post-baseline sibling landing was not "
                            f"called a sibling landing (verdict {sw and sw['verdict']})")

        hist = CLEAN_ENTRY.replace(
            "- calibration: this is house method, not a published standard",
            "- calibration: this is house method, not a published standard\n"
            "- **2026-10-17 — source recheck (baseline fe34faa; entry sha256 before append "
            "`8272a8f606b72504f433dc163f1ca545a43e99feb6a6572e8bb0a080c1bf738d`):** a past state")
        p = plant("historical-digest.md", hist)
        rec = audit_entry(p, _Path(tmp), offline=True)
        if "X63-E" in {f["id"] for f in rec["findings"]}:
            failures.append("historical self-digest was scored as a pin drift")
        if not any(c["verdict"] == "historical-self-digest" for c in rec["pins"]):
            failures.append("historical self-digest was not recognised at all")

        remote = CLEAN_ENTRY.replace(
            "  - KTD-RLC-S-0001 — `reports/round-26/register/design.md` (read at the round-26 stamp)",
            "  - KTD-RLC-S-0001 — locators re-attempted 2026-10-18 "
            "(`reports/round-26/register/design.md`): the transcription "
            "(raw snapshot 130,398 B, sha256 `27d6a210bfc3a88da9015e52537c51f6b529411b`); "
            "the design itself read live")
        p = plant("remote-digest.md", remote)
        rec = audit_entry(p, _Path(tmp), offline=True)
        if "X63-E" in {f["id"] for f in rec["findings"]}:
            failures.append("remote-artifact digest was scored as a pin drift")
        if not any(c["verdict"] == "remote-artifact" for c in rec["pins"]):
            failures.append("remote-artifact digest was not classified")

        nonadjacent = CLEAN_ENTRY.replace(
            "  - KTD-RLC-S-0002 — `corpus/QUALITY.md` — the admission bar",
            "  - KTD-RLC-S-0002 — see `corpus/QUALITY.md` for the bar; an unrelated "
            "page (sha256 `deadbeefdeadbeefdeadbeefdeadbeef`) was fetched")
        p = plant("nonadjacent-digest.md", nonadjacent)
        rec = audit_entry(p, _Path(tmp), offline=True)
        if "X63-E" in {f["id"] for f in rec["findings"]}:
            failures.append("a non-adjacent path was bound to a digest (false positive)")

        still_caught = CLEAN_ENTRY.replace(
            "  - KTD-RLC-S-0002 — `corpus/QUALITY.md` — the admission bar",
            "  - KTD-RLC-S-0002 — `corpus/QUALITY.md` (sha256 `deadbeefdeadbeefdeadbeef`)")
        p = plant("adjacent-drift.md", still_caught)
        rec = audit_entry(p, _Path(tmp), offline=True)
        if "X63-E" not in {f["id"] for f in rec["findings"]}:
            failures.append("adjacent-pin drift was no longer caught after the fix")

        # --- round-28 leg G: amendment discipline ---------------------------
        # A clean append: the baseline text is preserved and a new section added.
        amended_ok = plant("amended-ok.md", CLEAN_ENTRY)
        # A genuine prefix of the live text: the amendment appended a section
        # and touched no earlier line, so the leg must stay green.
        base = "\n".join(CLEAN_ENTRY.splitlines()[:6]) + "\n"
        rec = audit_entry(amended_ok, _Path(tmp), offline=True, baseline_text=base)
        if "X63-G" in {f["id"] for f in rec["findings"]}:
            failures.append("append-only amendment was scored as a rewrite")
        if not rec["amendment"]["append_only"]:
            failures.append("append-only amendment not recognised")

        # A rewrite: a baseline line is altered in place -> G must fire.
        rewritten = plant("amended-rewritten.md", CLEAN_ENTRY)
        base_bad = ("# Register-lexicon ceilings\n\n"
                    "- topic: THE ORIGINAL TOPIC LINE\n")
        rec = audit_entry(rewritten, _Path(tmp), offline=True, baseline_text=base_bad)
        ids = {f["id"] for f in rec["findings"]}
        if "X63-G" not in ids:
            failures.append("in-place rewrite was not caught by X63-G")
        if rec["amendment"]["deleted_or_rewritten"] != 1:
            failures.append(f"rewrite count wrong: {rec['amendment']['deleted_or_rewritten']}")

        # The magnitude must be right, not merely non-zero: a greedy pointer walk
        # reported 311 deleted lines for a one-line rewrite of the real entry
        # (measured), so the count is controlled here on a longer document.
        long_base = ("# Magnitude control\n\n- topic: x\n" +
                     "\n".join(f"line {i}" for i in range(40)) + "\n")
        long_live = long_base.replace("line 5\n", "LINE FIVE REWRITTEN\n") + "line 40\n"
        p = plant("amended-magnitude.md", long_live)
        rec = audit_entry(p, _Path(tmp), offline=True, baseline_text=long_base)
        got = rec["amendment"]["deleted_or_rewritten"]
        if got != 1:
            failures.append(f"rewrite magnitude wrong: got {got}, want 1 "
                            "(a greedy walk desynchronises)")
        if rec["amendment"]["preserved"] != rec["amendment"]["baseline_lines"] - 1:
            failures.append(f"preserved count wrong: {rec['amendment']['preserved']}, want "
                            f"{rec['amendment']['baseline_lines'] - 1}")

        # The still-caught control for G: a real append-only amendment to the
        # real round-27 entry must stay green under the same check.
        p27 = os.path.join(root, "corpus", "knowledge", "linguistics",
                           "register-strata-attestation.md")
        if os.path.exists(p27):
            txt = open(p27, "rb").read().decode("utf-8")
            rec = audit_entry(p27, _Path(root), offline=True, baseline_text=txt)
            if "X63-G" in {f["id"] for f in rec["findings"]}:
                failures.append("an entry compared with itself was scored as a rewrite")

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
    parser.add_argument("--baseline", default=None,
                        help="declared baseline revision; targets are located by set difference")
    parser.add_argument("--partition", default="corpus/knowledge/linguistics")
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
              f"(a clean entry, seven defect classes, the declared-absent exemption, a "
              f"reproducing sweep, a BRE-alternation sweep, a historical self-digest, a "
              f"remote-artifact digest, a non-adjacent path, a still-caught adjacent drift, "
              f"an append-only amendment, an in-place rewrite, a self-comparison, two "
              f"refusal controls and the read-only control); failures={len(failures)}")
        return code

    root = _Path(args.root or os.path.abspath(os.path.join(os.path.dirname(__file__),
                                                           "..", "..", "..")))
    targets = []            # (path, baseline_text, rel)
    if args.baseline and not args.entries:
        new, amended, base_set = locate_targets(root, args.baseline, args.partition)
        if not new and not amended:
            print(json.dumps({"schema": SCHEMA, "root": str(root), "baseline": args.baseline,
                              "partition": args.partition, "targets": [], "entries": [],
                              "findings": [], "verdict": "no-target"},
                             indent=1, ensure_ascii=False) if args.json else
                  "INFO scan: no-target (no new or amended entry vs the baseline)")
            return 0
        for rel in new:
            targets.append((str(root / rel), None, rel))
        for rel in amended:
            blob = _git(root, "show", f"{args.baseline}:{rel}").decode("utf-8")
            targets.append((str(root / rel), blob, rel))
    else:
        if not args.entries:
            parser.error("no entry given (or use --baseline/--selftest)")
        for e in args.entries:
            targets.append((e, None, e))

    receipts, findings = [], []
    for path, baseline_text, rel in targets:
        try:
            rec = audit_entry(path, root, offline=args.offline,
                              baseline_text=baseline_text,
                              baseline_rev=args.baseline,
                              self_rel=rel)
        except CannotEvaluate as exc:
            print(f"CANNOT-EVALUATE: {exc}", file=sys.stderr)
            return 2
        rec["rel"] = rel
        receipts.append(rec)
        findings.extend(rec["findings"])

    if args.json:
        print(json.dumps({"schema": SCHEMA, "root": str(root), "baseline": args.baseline,
                          "partition": args.partition,
                          "observed_at_utc": _now(), "entries": receipts,
                          "findings": findings}, indent=1, ensure_ascii=False))
    else:
        for f in findings:
            print(f"FINDING {f['id']}: {f['kind']}: {json.dumps(f['detail'], ensure_ascii=False)}")
        for rec in receipts:
            print(f"INFO entry: {rec['entry']} sha256={rec['sha256'][:16]} "
                  f"amendment={rec['is_amendment']} "
                  f"locators={len(rec['locators']['resolved'])} "
                  f"unresolved={len(rec['locators']['unresolved'])} "
                  f"exempt={len(rec['locators']['declared_absent'])} "
                  f"pins={len(rec['pins'])} sweeps={len(rec['sweeps'])} "
                  f"ceiling={rec['ceiling']['recorded_as_constraint']}")
        print(f"INFO scan: entries={len(receipts)} findings={len(findings)}")
    return 1 if findings else 0


def _now():
    import datetime
    return datetime.datetime.now(datetime.timezone.utc).isoformat()


if __name__ == "__main__":
    sys.exit(main())
