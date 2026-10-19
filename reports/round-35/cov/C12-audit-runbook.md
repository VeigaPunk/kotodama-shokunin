- Seat: C12 | executor | claim C | date 2026-10-19 | baseline 4a7aede

# C12 — entry-audit instrument runbook (claim C / coverage)

- Round 35, seat C12, role executor, claim C. Lane root
  `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; HEAD `4a7aede`; declared
  baseline `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` (`reports/round-35/claims.json:8-9`).
- Mission (verbatim, `reports/round-35/targets.json` → `seats[id=C12].mission`):
  *"Entry-audit instrument runbook: the per-entry check list (frontmatter,
  resolving pointers, decision record, gap statement, no-bleed language) as a
  runnable recipe + the expected results for the 10 drafts."*
- Writes: this fragment only, plus gitignored `.scratch/c12/`. No corpus byte, no
  `tools/**` byte and no filed round byte is touched; the instrument is **drafted
  here as bytes** and is deliberately not installed under `tools/` (the
  integrator applies tool changes, `reports/round-35/targets.json` `shared_rules`).
- Canon: NON-CANON. This runbook reads structure. It admits no entry, certifies
  no round, clears nothing and decides no canon; promotion/canon/closure verdicts
  are operator- and lore-shokunin-owned (`PROVINCE.md:20-27`).
- Dependency status at write time (2026-10-19, single 64-seat batch): the ten
  drafts (`reports/round-35/cov/C01..C10-entry-*.md`), the coverage plan
  (`reports/round-35/plan/P01-c-plan.md`) and the audit scout
  (`reports/round-35/scout/K02-entry-audit-method.md`) do not exist yet — all
  three probed absent by command (§7, control 5). §6 therefore states the
  expected results **per slot**; the slug/topic mapping is owed to P01 (§Owed).

## 1. The per-entry check list

Five check families, each a named reading with its own tier. Tiers: **blocker** /
**major** fail the structural contract (`pass: false`); **review** never fails the
contract — it is routed to the auditor to rank (see §8, limit 3).

| # | family | exact reading | tier | expected for a new draft |
|---|---|---|---|---|
| 1a | frontmatter, reading `R35-4F-1` | the four legs named in `reports/round-35/claims.json:24` — source leg satisfied by `- sources:` **or** `- source:`; `- verified-at:`; `- recheck:`; scope leg satisfied by `- scope:` **or** `- couples:` | blocker if a leg is missing | 4/4 present |
| 1b | frontmatter, reading `R35-5F-1` | round-10's field set `topic, sources, verified-at, recheck, couples` (`reports/round-10/run-validation.py:81`) | major | 5/5 present |
| 1c | frontmatter hygiene | no scalar field empty; a block-valued `- sources:` whose value sits on indented bullets counts as filled; `- verified-at:` carries an ISO `YYYY-MM-DD` | major | empty = none, `verified_at_iso: true` |
| 2 | resolving pointers | every backticked repo-path token `(corpus\|tools\|reports\|examples)/….(md\|json\|py\|yml\|yaml\|tsv\|txt)` resolves on disk, **brace groups expanded one level**; a dangling token is a blocker unless the same line marks it `(to-verify` — then it is reported as documented and is not a blocker; URLs are recorded as `urls_unfetched` and are **never** counted as resolved (no network in this wave) | blocker | `pointers_unresolved: []` (or all documented) |
| 2b | digest pins | a backticked 8–64-hex pin adjacent to a resolved pointer is compared with that file's sha256; a mismatch is **review**-tier, and a line carrying `went / → / superseded / at HEAD / revision / re-pin / history` is classed `historical_pin` (a dated pin is legitimate) | review | 0 stale-pin candidates |
| 3 | decision record | a `## …decision-record…` heading followed by body text (`reports/round-10/run-validation.py:368-370`), or a `DR-XX-NN` id | major | present |
| 4 | gap statement | a frontmatter gap field (`- gap filled:` / `- gap:` / `- gap addressed:` / `- gap served:`), or an inline `gap filled:` clause, or a body heading naming the gap (`reports/round-10/run-validation.py:362-367`) | blocker | present; `- gap filled:` recommended |
| 5a | no-bleed, strict | unnegated hits of `promoted / promotion / promote / cleared / clearance / closure / closed as / signed off / green-lit`, with a negation/boundary window (`not, never, non-, without, rather than, outside, beyond, instead of, refuses, rejected, neither, lore-shokunin, theirs, handoff, world bible, unresolved, owed, operator-owned, is not, does not, nothing about, stays a verdict, at that revision, same bytes`) | review | read each hit; the word-list is polysemous (§8, limit 4) |
| 5b | no-bleed, ownership assertion | a strict hit whose context also names the lane's own act (`this entry / this lane / this round / this seat / the entry / the draft / the fragment / the wave / the round / the corpus / the artifact / the packet`) | review | 0 |
| 5c | no-bleed, `canon` mentions | unnegated `canon / canonical / canonized`; `admitted / admission / approved / acceptance` are counted separately as prior-round idioms and are informational | review | read each hit against `PROVINCE.md:20-27` |
| 6 | canon-boundary named (context, not a gate) | the entry names the handoff/refusal (`lore-shokunin`, `non-canon`, `world-bible`, `canon decisions are/belong`) | informational | present |

Two verdicts are reported and never merged: **`pass`** = families 1–4 hold (the
structural contract); **`clean`** = `pass` **and** zero review-tier observations.
A green reading is a structural reading of the bytes — never a verdict on the
scholarship, never canon, never an admission.

## 2. Why the frontmatter reading must be named

The claim's four legs (`reports/round-35/claims.json:24`) include `scope`, and
**no live corpus entry carries a literal `- scope:` field**: measured 2026-10-19
at HEAD `4a7aede`, `grep -rl -- '^- scope:' corpus/knowledge/ | wc -l` → **0**;
`- couples:` → 201; `- sources:` → 201; `- source:` → 134; `- verified-at:` →
201; `- recheck:` → 201. A literal-`scope` reading would therefore report **0/201**
on the already-admitted corpus and 0/10 on compliant drafts — a reading, not a
finding. This is the same discipline the lane already applies to header counts
(`corpus/knowledge/verification/header-conformance-readings.md:1-6`): no header
count circulates without its reading id. Use **`R35-4F-1`** (documented
substitution: source leg = `sources|source`, scope leg = `couples`) and report
`frontmatter_4of4_literal_scope` alongside it if the literal reading is wanted.

## 3. Baseline calibration measured today (2026-10-19, HEAD `4a7aede`)

Instrument census over all 201 entries (`--census`, §7 control 4). This is the
**calibration baseline, not the expected rate for the new drafts**: the contract
in `reports/round-35/claims.json:24-35` is the *new* bar, and most of the corpus
predates it.

| reading | corpus result (n=201) | how to read it |
|---|---|---|
| `R35-4F-1` frontmatter 4/4 | **201/201** | the whole corpus satisfies the substituted reading |
| literal `- scope:` field | **0/201** | never gate on this (§2) |
| `R35-5F-1` (round-10 set) | **201/201** | — |
| `verified_at_iso`, no empty frontmatter | **201/201** | — |
| gap named | **29/201** | historical practice; expected for drafts is 10/10 |
| decision record (heading reading) | **22/201** | idem; loose reading 38/201 |
| full contract `pass` | **22/201** | exactly the 22 entries that carry both a gap statement and a decision record — i.e. the post-round-10/19/28 authoring shape |
| `clean` (pass + no review items) | **8/201** | review items are ordinary-word artefacts (§8, limit 4) |
| source entries (min/median/max) | **1 / 1 / 36** | ≥1 with a locator is the gate; breadth is not gated |
| `recheck` length (min/median, chars) | **88 / 182** | no boilerplate threshold is asserted here |

## 4. The runnable recipe

All commands from the lane root. Step 0 is mandatory for every step after it.

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1

# 0. install the instrument bytes from §5 of this fragment into scratch, then
#    prove the bytes are the audited bytes:
mkdir -p .scratch/c12
awk '/^```python$/{f=1;next} /^```$/{f=0} f' \
  reports/round-35/cov/C12-audit-runbook.md > .scratch/c12/entry-audit-runbook.py
sha256sum .scratch/c12/entry-audit-runbook.py
# expected: 973610275404e9e3183d46e33e5352562265e6c2e397c92291e63c401ed7562d  (663 lines)

# 1. instrument self-controls — must print SELFTEST PASS and exit 0
python3 -B .scratch/c12/entry-audit-runbook.py --selftest

# 2. stage the ten drafts out of their fragments and audit the staged bytes.
#    Point --fragments at a directory holding ONLY the ten entry fragments, so a
#    sibling fragment that also names a corpus path cannot be staged by mistake.
mkdir -p .scratch/c12/drafts && cp reports/round-35/cov/C0*-entry-*.md .scratch/c12/drafts/
python3 -B .scratch/c12/entry-audit-runbook.py \
  --fragments .scratch/c12/drafts --stage .scratch/c12/stage
# prints one STAGED line per fragment (fragment -> corpus/knowledge/<partition>/<slug>.md)
# then one PASS/clean|review or FAIL/... line per staged entry, then TOTAL pass N/10

# 3. per-entry detail, including line numbers for every review item
python3 -B .scratch/c12/entry-audit-runbook.py --json \
  .scratch/c12/stage/corpus/knowledge/*/*.md > .scratch/c12/drafts-audit.json

# 4. one entry at a time (when a fragment's target path must be confirmed by hand)
python3 -B .scratch/c12/entry-audit-runbook.py .scratch/c12/stage/corpus/knowledge/myth-symbol/<slug>.md

# 5. corpus baseline (re-measure the §3 numbers on the post-landing tree)
python3 -B .scratch/c12/entry-audit-runbook.py --census --json > .scratch/c12/census-post.json
```

Exit codes: `0` every audited entry passes; `1` at least one fails; `2`
could-not-evaluate (missing path, unreadable/non-UTF-8 file, or a fragment that
names no `corpus/knowledge/<partition>/<slug>.md` target or carries no fenced
`markdown`/`md` block). Exit 2 on an absent draft is the correct reading of
"not yet written" — it is not a defect of the draft.

### 4b. The partition/README leg (claim C's counting commands)

```bash
# census (claim C counting command 1) — before: 21 19 18 29 20 94, total 201
for p in linguistics myth-symbol culture-material synthesis verification civilizations; do
  printf '%s %s\n' "$p" "$(ls corpus/knowledge/$p/*.md | wc -l)"; done
ls corpus/knowledge/*/*.md | wc -l

# inventory (claim C counting command 2) — before: totals.files 201
python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge | \
  python3 -c "import json,sys; d=json.load(sys.stdin); print(d['totals']['files'])"

# README reconciliation: rows vs files, section headings vs census, footer vs census
python3 -B - <<'PY'
import re, pathlib
readme = pathlib.Path("corpus/README.md").read_text()
rows, declared, current = {}, {}, None
for line in readme.splitlines():
    h = re.match(r"^##\s+([a-z][a-z-]*)/\s*\((\d+)\)\s*$", line)
    if h:
        current = h.group(1); declared[current] = int(h.group(2)); rows.setdefault(current, set()); continue
    if line.startswith("## "):
        current = None; continue
    if current:
        row = re.match(r"^-\s+`([^`]+\.md)`", line)
        if row:
            rows[current].add(row.group(1))
total = re.search(r"(?m)^Total knowledge entries:\s*(\d+)\.", readme)
footer = re.search(r"(?m)^`python3 tools/source-audit-inventory\.py --json --summary --root corpus/knowledge`\n"
                   r"\(total (\d+) files; directory totals ([\d/]+)\)", readme)
live = {p: sorted(f.name for f in pathlib.Path("corpus/knowledge", p).glob("*.md"))
        for p in ("linguistics","myth-symbol","culture-material","synthesis","verification","civilizations")}
live_n = {p: len(v) for p, v in live.items()}
print("headings:", declared)
print("live     :", live_n)
print("rows vs files:", {p: (len(rows[p]), live_n[p]) for p in live_n})
print("missing rows:", {p: sorted(set(live[p]) - rows[p]) for p in live_n})
print("ghost rows  :", {p: sorted(rows[p] - set(live[p])) for p in live_n})
print("total line:", total.group(1) if total else None, "footer:", footer.groups() if footer else None)
PY
```

Expected after the ten land (derived from `reports/round-35/claims.json:24,29` and
the README's own revision convention at `corpus/README.md:3-15`):
`culture-material 24`, `myth-symbol 23`, total **211**; headings
`## myth-symbol/ (23)` and `## culture-material/ (24)`; footer
`(total 211 files; directory totals 21/23/24/29/20/94)`; every new row byte-equal
to its entry's own `- topic:` text (the round-20 repair rule,
`corpus/README.md:69-93`). The exact delta bytes are C11's deliverable
(`reports/round-35/cov/C11-readme-delta.md`) — cross-read it, do not re-derive
from this paragraph alone.

## 5. The instrument (bytes, verbatim)

sha256 `973610275404e9e3183d46e33e5352562265e6c2e397c92291e63c401ed7562d`,
663 lines, stdlib only, read-only apart from the optional `--stage` extraction.
Install it with step 0 of §4 — do not retype it.

```python
#!/usr/bin/env python3
"""C12 entry-audit instrument (round 35, claim C) — read-only, stdlib only.

Audits one staged corpus entry (or a directory of fragments) against the
round-35 claim-C entry contract:

  1. frontmatter completeness, under two named readings (R35-4F-1 / R35-5F-1),
     each scalar field non-empty, `verified-at` ISO-dated;
  2. source pointers resolve: every backticked repo-path token exists on disk
     (brace groups expanded); sha-prefix pins are compared against the file
     they name and a mismatch is a *review* observation (a dated historical pin
     is legitimate); URLs are recorded as `url-unfetched` (no network) and are
     never counted as resolved;
  3. decision record: a `decision-record` heading, or a DR-id;
  4. gap statement: a frontmatter gap field, an inline gap clause, or a body
     heading naming the gap;
  5. no-bleed language: promotion/canon/clearance/closure vocabulary, split
     into negated mentions (expected), strict unnegated candidates, unnegated
     `canon` mentions (review-only), and prior-round admission idioms
     (informational).

Two verdicts per entry, never merged:

  `pass`   the structural contract holds (frontmatter, pointers, gap, decision
           record). A `pass` is a structural reading of the bytes, never a
           verdict on the scholarship, never canon, never an admission.
  `clean`  `pass` and zero review-tier observations (bleed candidates,
           stale-pin candidates).

What this instrument does NOT do, by construction:

  * it never writes inside a scanned tree, never clears a marker, never edits
    an entry; the only writes are the optional `--stage` extraction, which goes
    to a caller-named directory outside the corpus;
  * it never fetches a URL and never treats an unfetched URL as resolved;
  * every bleed and pin observation is `heuristic: true, review_required: true`;
    the classes are triage sort keys, not adjudications;
  * it does not read scholarship: marker absence is not verification.

Usage:
  entry-audit-runbook.py --selftest
  entry-audit-runbook.py [--json] FILE [FILE ...]
  entry-audit-runbook.py --census [--json]            # whole corpus baseline
  entry-audit-runbook.py --fragments DIR --stage DIR2 # extract fenced entries

Exit codes: 0 every audited entry passes; 1 at least one fails; 2
could-not-evaluate (path missing, unreadable, not UTF-8, or a fragment whose
target path cannot be resolved).
"""

import argparse
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

SCHEMA = "kotodama-entry-audit-runbook/2"
LANE = Path(__file__).resolve().parent
for _ in range(8):
    if (LANE / "corpus" / "knowledge").is_dir():
        break
    LANE = LANE.parent

# --- frontmatter readings -------------------------------------------------
# R35-4F-1: the four legs named by reports/round-35/claims.json claim C
#   ("frontmatter-complete (source / verified-at / recheck / scope)"), with the
#   observable substitutes this corpus actually carries: `sources` or `source`
#   for the source leg, and `couples` for the scope leg (0 of 201 live entries
#   carry a literal `- scope:` field; measured 2026-10-19).
# R35-5F-1: the round-10 runner's C_FRONTMATTER_FIELDS
#   (reports/round-10/run-validation.py:81).
FM_4F = (("source", ("sources", "source")), ("verified-at", ("verified-at",)),
         ("recheck", ("recheck",)), ("scope", ("scope", "couples")))
FM_5F = ("topic", "sources", "verified-at", "recheck", "couples")
BLOCK_FIELDS = ("sources",)
FIELD_RE = re.compile(r"^- ([a-z][a-z-]*):[ \t]*(.*)$", re.M)

GAP_FIELD_RE = re.compile(r"^- (gap filled|gap|gap addressed|gap served):[ \t]*(\S.*)$",
                          re.M | re.I)
GAP_INLINE_RE = re.compile(r"(?i)(?:^|[\s.;—–|-])gap(?:[\s-]+(?:filled|addressed|"
                           r"served))?\s*:\s*(\S[^\n]{0,300})")
GAP_HEADING_RE = re.compile(r"(?mi)^#{2,4}[^\n]*\bgap\b[^\n]*\n(?:[^\n]*\n)*?"
                            r"[^\n\s][^\n]*$")
DECISION_HEADING_RE = re.compile(r"(?mi)^#{2,4}[^\n]*decision[- ]record[^\n]*\n+"
                                 r"\s*(\S[^\n]*)")
DECISION_LOOSE_RE = re.compile(r"(decision record|decision table|DR-[A-Z]{2}-\d|"
                               r"decisions? taken)", re.I)
CANON_BOUNDARY_RE = re.compile(r"(lore-shokunin|non-canon|world[- ]bible|"
                               r"canon decisions? (?:are|belong))", re.I)

REPO_PATH_RE = re.compile(r"`((?:corpus|tools|reports|examples)/[\w./{},-]+"
                          r"\.(?:md|json|py|yml|yaml|tsv|txt))`")
BRACE_RE = re.compile(r"\{([^{}]*)\}")
PIN_RE = re.compile(r"`([0-9a-f]{8,64})(?:…|\.\.\.)?`")
LOCATOR_RE = re.compile(r"(https?://|\b(?:19|20)\d{2}\b|"
                        r"`[^`]*\.(?:md|py|json|yml|yaml|tsv)`|\b[0-9a-f]{16,64}\b)")
URL_RE = re.compile(r"https?://[^\s`)\]>,]+")

# Bleed vocabulary, tiered. STRICT verbs assert an ownership action the lane
# refuses; CANON is reported separately because `canon` is legitimately used in
# boundary prose; IDIOMS are this corpus's historical/round-acceptance usage and
# are informational only.
BLEED_STRICT = ("promoted", "promotion", "promote", "cleared", "clearance",
                "closure", "closed as", "signed off", "green-lit")
BLEED_CANON = ("canon", "canonical", "canonized")
BLEED_IDIOMS = ("admitted", "admission", "approved", "acceptance")
NEGATION_RE = re.compile(r"(?i)(\bnot\b|\bnever\b|\bno\b|\bnone\b|\bnon-|"
                         r"\bcannot\b|\bwithout\b|\brather than\b|\boutside\b|"
                         r"\bbeyond\b|\binstead of\b|\brefus|\breject|"
                         r"\bneither\b|\blore-shokunin\b|\blore\b|"
                         r"\bbelongs? to\b|\bhandoff\b|\bhands? off\b|\btheirs\b|"
                         r"\bworld bible\b|\bunresolved\b|\bowed\b|"
                         r"\boperator-owned\b|\bnot a\b|\bis not\b|\bare not\b|"
                         r"\bdoes not\b|\bdo not\b|\bnothing about\b|"
                         r"\bstays a verdict\b|\bat that revision\b|"
                         r"\bwhen it was\b|\bsame bytes\b)")
HISTORICAL_PIN_RE = re.compile(r"(?i)(went|→|superseded|at head|revision|"
                               r"re-?pin|history|was `|as recorded)")
# An ownership assertion is a bleed term whose subject is the lane's own act
# ("this entry is cleared", "promoted to canon") rather than an ordinary or
# in-world use of the word ("garment closure", "cleared area", "court promotes").
OWNERSHIP_RE = re.compile(r"(?i)(this entry|this lane|this round|this seat|"
                          r"the entry|the draft|the fragment|the wave|the round|"
                          r"the corpus|the artifact|the packet)")
WINDOW = 70


def sha256_file(path):
    return hashlib.sha256(Path(path).read_bytes()).hexdigest()


def expand_braces(value):
    match = BRACE_RE.search(value)
    if not match:
        return [value]
    out = []
    for part in match.group(1).split(","):
        out.extend(expand_braces(value[:match.start()] + part + value[match.end():]))
    return out


def field_values(text):
    """Field name -> list of raw values. A block-valued field (`sources`) whose
    value sits on indented bullets below counts as present and non-empty."""
    out = {}
    for match in FIELD_RE.finditer(text):
        name, value = match.group(1), match.group(2).strip()
        tail = text[match.end():]
        following = tail.split("\n", 1)[1][:200] if "\n" in tail else ""
        block_valued = bool(re.match(r"[ \t]+- ", following))
        out.setdefault(name, []).append(
            {"value": value, "block": block_valued})
    return out


def source_entries(text):
    """Source entries: indented bullets under `- sources:`, else the field's own
    inline value as a single entry (plant-symbolism.md style)."""
    bullets, inline, inside = [], [], False
    for line in text.splitlines():
        if re.match(r"^- sources:", line):
            inside = True
            inline.append(line.split(":", 1)[1].strip())
            continue
        if inside:
            if re.match(r"^- \w", line) and not line.startswith("  "):
                inside = False
                continue
            if line.startswith("  - "):
                bullets.append(line)
    entries = bullets if bullets else [v for v in inline if v]
    return entries


def resolve_pointers(text):
    resolved, unresolved, unfetched, pins = [], [], [], []
    tokens = set()
    for raw in REPO_PATH_RE.findall(text):
        tokens.update(expand_braces(raw))
    for token in sorted(tokens):
        hit = LANE / token
        (resolved if hit.is_file() else unresolved).append(token)
    for line in text.splitlines():
        for token in tokens:
            if f"`{token}`" in line or token in line:
                for pin in PIN_RE.findall(line):
                    hit = LANE / token
                    if not hit.is_file():
                        continue
                    digest = sha256_file(hit)
                    if not digest.startswith(pin.lower()):
                        pins.append({
                            "pointer": token, "pin": pin,
                            "file_sha256": digest,
                            "historical_pin_heuristic": bool(
                                HISTORICAL_PIN_RE.search(line)),
                            "heuristic": True, "review_required": True,
                            "context": line.strip()[:200],
                        })
                break
    for url in sorted(set(URL_RE.findall(text))):
        unfetched.append(url)
    return resolved, unresolved, unfetched, pins


def bleed_hits(text):
    negated, strict, canon, idioms = [], [], [], []
    for number, line in enumerate(text.splitlines(), start=1):
        lowered = line.lower()
        for tier, terms in (("strict", BLEED_STRICT), ("canon", BLEED_CANON),
                            ("idiom", BLEED_IDIOMS)):
            for term in terms:
                start = 0
                while True:
                    at = lowered.find(term, start)
                    if at < 0:
                        break
                    start = at + len(term)
                    window = lowered[max(0, at - WINDOW):at + len(term) + WINDOW]
                    record = {"line": number, "term": term, "tier": tier,
                              "heuristic": True, "review_required": True,
                              "context": line.strip()[:200]}
                    if NEGATION_RE.search(window):
                        negated.append(record)
                    elif tier == "strict":
                        strict.append(record)
                    elif tier == "canon":
                        canon.append(record)
                    else:
                        idioms.append(record)
    return negated, strict, canon, idioms


def audit_entry(path, raw=None):
    if raw is None:
        raw = Path(path).read_bytes()
    text = raw.decode("utf-8")
    values = field_values(text)
    present = {name for name, hits in values.items()}
    missing_4f = [label for label, names in FM_4F
                  if not any(n in present for n in names)]
    missing_5f = [name for name in FM_5F if name not in present]
    empty = sorted(name for name, hits in values.items()
                   if any(h["value"] == "" and not h["block"] for h in hits))
    verified = " ".join(h["value"] for h in values.get("verified-at", []))
    verified_iso = bool(re.search(r"\b(19|20)\d{2}-\d{2}-\d{2}\b", verified))
    recheck_len = len(" ".join(h["value"] for h in values.get("recheck", [])))
    sources = source_entries(text)
    with_locator = [s for s in sources if LOCATOR_RE.search(s)]
    resolved, unresolved, unfetched, pins = resolve_pointers(text)
    documented = [tok for tok in unresolved
                  if any(tok in line and "(to-verify" in line.lower()
                         for line in text.splitlines())]
    gap_field = GAP_FIELD_RE.search(text)
    gap_named = bool(gap_field or GAP_INLINE_RE.search(text)
                     or GAP_HEADING_RE.search(text))
    decision = DECISION_HEADING_RE.search(text)
    decision_loose = DECISION_LOOSE_RE.search(text)
    negated, strict, canon, idioms = bleed_hits(text)
    stale_pins = [p for p in pins if not p["historical_pin_heuristic"]]
    historical_pins = [p for p in pins if p["historical_pin_heuristic"]]
    contract = []
    if missing_4f:
        contract.append(("blocker", "frontmatter-4of4-missing:" + ",".join(missing_4f)))
    if missing_5f:
        contract.append(("major", "lane-profile-5f-missing:" + ",".join(missing_5f)))
    if empty:
        contract.append(("major", "frontmatter-empty:" + ",".join(empty)))
    if not verified_iso:
        contract.append(("major", "verified-at-not-iso-dated"))
    if not sources or not with_locator:
        contract.append(("major", "source-entries-without-locator"))
    undoc = [tok for tok in unresolved if tok not in documented]
    if undoc:
        contract.append(("blocker", "unresolved-pointer:" + ",".join(undoc)))
    if not gap_named:
        contract.append(("blocker", "gap-not-named"))
    if not decision:
        contract.append(("major", "decision-record-absent"))
    review = []
    ownership = [c for c in strict if OWNERSHIP_RE.search(c["context"])]
    if strict:
        review.append(("review", "bleed-candidate:" + ",".join(sorted(
            {c["term"] for c in strict}))))
    if ownership:
        review.append(("review", "ownership-assertion-candidate:" + ",".join(sorted(
            {c["term"] for c in ownership}))))
    if canon:
        review.append(("review", "canon-mention-unnegated:" + ",".join(sorted(
            {c["term"] for c in canon}))))
    if stale_pins:
        review.append(("review", "stale-pin-candidate:" + ",".join(sorted(
            {p["pointer"] for p in stale_pins}))))
    return {
        "schema": SCHEMA,
        "path": Path(path).as_posix(),
        "sha256": hashlib.sha256(raw).hexdigest(),
        "size_bytes": len(raw),
        "header_fields": sorted(present),
        "frontmatter_4of4": not missing_4f,
        "frontmatter_4of4_missing": missing_4f,
        "frontmatter_4of4_literal_scope": "scope" in present,
        "lane_profile_5f": not missing_5f,
        "lane_profile_5f_missing": missing_5f,
        "frontmatter_empty": empty,
        "verified_at_iso": verified_iso,
        "recheck_chars": recheck_len,
        "source_entries": len(sources),
        "source_entries_with_locator": len(with_locator),
        "pointers_resolved": resolved,
        "pointers_unresolved": unresolved,
        "pointers_unresolved_documented": documented,
        "urls_unfetched": len(unfetched),
        "digest_pins_compared": len(pins),
        "digest_pins_stale_candidates": stale_pins,
        "digest_pins_historical": historical_pins,
        "gap_named": gap_named,
        "gap_field": gap_field.group(1) if gap_field else None,
        "decision_record": bool(decision),
        "decision_record_loose": bool(decision_loose),
        "canon_boundary_named": bool(CANON_BOUNDARY_RE.search(text)),
        "bleed_negated_mentions": len(negated),
        "bleed_candidates": strict,
        "ownership_assertions": ownership,
        "canon_mentions_unnegated": canon,
        "admission_idioms": len(idioms),
        "contract_defects": [{"severity": s, "detail": d} for s, d in contract],
        "review_observations": [{"severity": s, "detail": d} for s, d in review],
        "pass": not contract,
        "clean": not contract and not review,
    }


def render(records):
    lines = []
    for r in records:
        flag = "PASS" if r["pass"] else "FAIL"
        clean = "clean" if r["clean"] else "review"
        lines.append(
            f"{flag}/{clean} {r['path']} 4of4={r['frontmatter_4of4']} "
            f"5f={r['lane_profile_5f']} src={r['source_entries_with_locator']}/"
            f"{r['source_entries']} ptr={len(r['pointers_resolved'])}/"
            f"{len(r['pointers_resolved']) + len(r['pointers_unresolved'])} "
            f"gap={r['gap_named']} dec={r['decision_record']} "
            f"bleed={len(r['bleed_candidates'])}/{len(r['canon_mentions_unnegated'])}")
        for d in r["contract_defects"]:
            lines.append(f"     [{d['severity']}] {d['detail']}")
        for d in r["review_observations"]:
            lines.append(f"     [{d['severity']}] {d['detail']}")
    passed = sum(1 for r in records if r["pass"])
    clean = sum(1 for r in records if r["clean"])
    lines.append(f"TOTAL pass {passed}/{len(records)}; clean {clean}/{len(records)}")
    return "\n".join(lines) + "\n"


def census(root):
    records = []
    for path in sorted(Path(root).rglob("*.md")):
        try:
            records.append(audit_entry(path))
        except (UnicodeDecodeError, OSError) as exc:  # pragma: no cover
            records.append({"path": path.as_posix(), "pass": False, "clean": False,
                            "contract_defects": [{"severity": "could-not-evaluate",
                                                  "detail": str(exc)[:120]}],
                            "review_observations": []})
    return records


POSITIVE = """# Fixture entry \u2014 contract-complete

- gap filled: the fixture gap this entry fills (fixture only)
- topic: A planted fixture entry that satisfies every leg of the round-35 entry contract; its sources are citation-shaped fixtures.
- sources:
  - Fixture Author (2001), *A Citation-Shaped String*, Example Press, https://example.invalid/fixture (fetched 2026-10-19).
  - In-corpus locator `corpus/knowledge/verification/provenance-audit-ledger-format.md` (fixture cross-reference).
- couples: verification/provenance-audit-ledger-format.md \u2014 the fixture coupling; handoff target: lore-shokunin world bible (fixture; canon decisions are theirs).
- source: `corpus/knowledge/verification/provenance-audit-ledger-format.md` + Fixture Author (2001) (fixture)
- verified-at: 2026-10-19 \u2014 fixture pass; every citation above is a fixture and cites nothing real.
- recheck: before reusing this fixture, re-run the planted control and confirm the audit still reads it clean.

## 1. Gap filled
The fixture partition carries no contract-complete control; this file is one.

## 2. Decision record
- DR-FX-01: keep the fixture minimal so the audit's positive leg is unambiguous.
"""

PROSE_SOURCES = """# Fixture entry \u2014 prose sources block (plant-symbolism style)

- gap: fixture gap, prose-sources shape
- topic: A planted fixture whose `- sources:` line carries its citations inline instead of as bullets.
- sources: Fixture Author (2004), *A Fourth Citation-Shaped String*, Example Press \u2014 web-checked 2026-10-19; and `corpus/knowledge/verification/provenance-audit-ledger-format.md`
- couples: verification/provenance-audit-ledger-format.md
- verified-at: 2026-10-19
- recheck: fixture prose-sources control

## 1. Gap filled
Fixture.

## 2. Decision record
Fixture.
"""

BRACES = """# Fixture entry \u2014 brace-grouped pointers

- gap: fixture gap, brace shape
- topic: A planted fixture whose source locators use one-level brace groups.
- sources:
  - `reports/round-26/register/{design,rules,review}.md` (fixture brace group)
- couples: verification/provenance-audit-ledger-format.md
- verified-at: 2026-10-19
- recheck: fixture

## 1. Gap filled
Fixture.

## 2. Decision record
Fixture.
"""

NEGATIVE_BLEED = """# Fixture entry \u2014 bleed language

- gap: fixture gap
- topic: A planted fixture whose prose asserts a clearance the lane does not own.
- sources:
  - Fixture Author (2002), *Another Citation-Shaped String*, Example Press.
- couples: verification/provenance-audit-ledger-format.md
- verified-at: 2026-10-19
- recheck: fixture

## 1. Gap filled
Fixture.

## 2. Decision record
Fixture.
This entry is cleared and the culture is promoted to canon.
"""

NEGATIVE_UNRESOLVED = """# Fixture entry \u2014 unresolvable pointer

- gap: fixture gap
- topic: A planted fixture citing a corpus path that does not exist.
- sources:
  - `corpus/knowledge/verification/does-not-exist-fixture.md` (planted dangling pointer).
- couples: verification/provenance-audit-ledger-format.md
- verified-at: 2026-10-19
- recheck: fixture

## 1. Gap filled
Fixture.

## 2. Decision record
Fixture.
"""

NEGATIVE_NO_GAP_NO_DECISION = """# Fixture entry \u2014 no gap, no decision record

- topic: A planted fixture with a source but no gap statement and no decision record.
- sources:
  - Fixture Author (2003), *A Third Citation-Shaped String*, Example Press.
- couples: verification/provenance-audit-ledger-format.md
- verified-at: 2026-10-19
- recheck: fixture
"""


def selftest():
    failures = []

    def check(condition, label):
        if not condition:
            failures.append(label)

    with tempfile.TemporaryDirectory(prefix="entry-audit-runbook-") as tmp:
        root = Path(tmp)
        fixtures = {"positive/complete.md": POSITIVE,
                    "positive/prose-sources.md": PROSE_SOURCES,
                    "positive/braces.md": BRACES,
                    "negative/bleed.md": NEGATIVE_BLEED,
                    "negative/unresolved.md": NEGATIVE_UNRESOLVED,
                    "negative/no-gap-no-decision.md": NEGATIVE_NO_GAP_NO_DECISION}
        for rel, body in fixtures.items():
            (root / rel).parent.mkdir(parents=True, exist_ok=True)
            (root / rel).write_text(body, encoding="utf-8")
        before = {rel: sha256_file(root / rel) for rel in fixtures}

        pos = audit_entry(root / "positive/complete.md")
        check(pos["pass"] is True, "positive control did not pass: " +
              json.dumps(pos["contract_defects"]))
        check(pos["clean"] is True, "positive control not clean: " +
              json.dumps(pos["review_observations"]))
        check(pos["frontmatter_4of4"] is True, "positive: 4of4 false")
        check(pos["lane_profile_5f"] is True, "positive: 5f false")
        check(pos["verified_at_iso"] is True, "positive: verified-at not ISO")
        check(pos["gap_named"] is True, "positive: gap not named")
        check(pos["decision_record"] is True, "positive: decision record not read")
        check(pos["source_entries_with_locator"] >= 1, "positive: no located entry")
        check(pos["pointers_unresolved"] == [], "positive: unresolved pointer")
        check(pos["bleed_candidates"] == [], "positive: bleed candidates")

        prose = audit_entry(root / "positive/prose-sources.md")
        check(prose["pass"] is True, "prose-sources control failed: " +
              json.dumps(prose["contract_defects"]))
        check(prose["source_entries_with_locator"] == 1,
              "prose-sources control: inline value not counted as a source entry")

        braces = audit_entry(root / "positive/braces.md")
        check(braces["pointers_unresolved"] == [],
              "brace control: expansion left unresolved pointers: " +
              json.dumps(braces["pointers_unresolved"]))

        bleed = audit_entry(root / "negative/bleed.md")
        check(bleed["pass"] is True,
              "bleed control failed the structural contract (bleed must be a "
              "review-tier observation, never a contract defect)")
        check(bleed["clean"] is False, "bleed control read clean")
        check(len(bleed["bleed_candidates"]) >= 1, "bleed control produced no candidate")
        check(len(bleed["ownership_assertions"]) >= 1,
              "bleed control produced no ownership assertion")
        check(any(d["detail"].startswith("bleed-candidate")
                  for d in bleed["review_observations"]), "bleed control produced no observation")

        unres = audit_entry(root / "negative/unresolved.md")
        check(unres["pass"] is False, "unresolved control passed")
        check(unres["pointers_unresolved"] != [], "unresolved control found no dangling pointer")
        check(any(d["detail"].startswith("unresolved-pointer")
                  for d in unres["contract_defects"]), "unresolved control produced no defect")

        bare = audit_entry(root / "negative/no-gap-no-decision.md")
        check(bare["pass"] is False, "no-gap control passed")
        check(bare["gap_named"] is False, "no-gap control found a gap")
        check(bare["decision_record"] is False, "no-gap control found a decision record")

        doc = root / "negative/documented.md"
        doc.write_text(NEGATIVE_UNRESOLVED.replace(
            "does-not-exist-fixture.md` (planted dangling pointer)",
            "does-not-exist-fixture.md` (to-verify: planted dangling pointer)"),
            encoding="utf-8")
        d = audit_entry(doc)
        check(d["pointers_unresolved_documented"] != [],
              "documented-unresolved control not recognised")
        check(not any(x["detail"].startswith("unresolved-pointer")
                      for x in d["contract_defects"]),
              "documented-unresolved control still a blocker")

        neg = root / "positive/negated-bleed.md"
        neg.write_text(NEGATIVE_BLEED.replace(
            "This entry is cleared and the culture is promoted to canon.",
            "This entry is not cleared; the culture is never promoted to canon, "
            "and canon decisions are lore-shokunin's."), encoding="utf-8")
        n = audit_entry(neg)
        check(n["bleed_candidates"] == [], "negated bleed control produced a strict candidate")
        check(n["ownership_assertions"] == [],
              "negated bleed control produced an ownership assertion")
        check(n["pass"] is True, "negated bleed control failed the contract")

        again = audit_entry(root / "positive/complete.md")
        check(json.dumps(again, sort_keys=True) == json.dumps(pos, sort_keys=True),
              "two audits of the same file differ")
        check(before == {rel: sha256_file(root / rel) for rel in fixtures},
              "the scan wrote to its own tree")

    return (0 if not failures else 1), failures


def stage_fragments(fragments_dir, stage_dir):
    """Extract each fragment's fenced entry block to <stage>/<declared path>."""
    mapping, errors = [], []
    stage = Path(stage_dir)
    for frag in sorted(Path(fragments_dir).glob("*.md")):
        text = frag.read_text(encoding="utf-8")
        target = None
        for match in re.finditer(r"(corpus/knowledge/[a-z-]+/[a-z0-9-]+\.md)", text):
            target = match.group(1)
            break
        blocks = re.findall(r"^```(?:markdown|md)\s*$([\s\S]*?)^```\s*$", text, re.M)
        if target is None or not blocks:
            errors.append({"fragment": frag.as_posix(),
                           "reason": "no corpus target path or no fenced block"})
            continue
        out = stage / target
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(blocks[0], encoding="utf-8")
        mapping.append({"fragment": frag.as_posix(), "staged": out.as_posix(),
                        "bytes": len(blocks[0].encode())})
    return mapping, errors


def main(argv=None):
    parser = argparse.ArgumentParser(
        prog="entry-audit-runbook.py",
        description="Read-only round-35 claim-C entry audit (staged bytes).")
    parser.add_argument("files", nargs="*")
    parser.add_argument("--json", action="store_true")
    parser.add_argument("--census", action="store_true",
                        help="audit every corpus/knowledge/**/*.md as a baseline")
    parser.add_argument("--root", default=str(LANE / "corpus" / "knowledge"))
    parser.add_argument("--fragments", default=None,
                        help="extract fenced entry blocks from fragment files")
    parser.add_argument("--stage", default=str(LANE / ".scratch" / "c12" / "stage"))
    parser.add_argument("--selftest", action="store_true")
    args = parser.parse_args(argv)

    if args.selftest:
        code, failures = selftest()
        if code:
            for failure in failures:
                print(f"SELFTEST FAIL: {failure}", file=sys.stderr)
            print(f"INFO selftest: failed={len(failures)}")
        else:
            print("SELFTEST PASS: 3 positive controls (bullets, prose sources, brace "
                  "pointers) and 4 negative controls (bleed, dangling pointer, "
                  "no-gap/no-decision, documented-dangling) behave; negated-bleed "
                  "control reads clean; determinism and no-write checked")
        return code

    mapping, errors = [], []
    if args.fragments:
        mapping, errors = stage_fragments(args.fragments, args.stage)
        if errors:
            for error in errors:
                print(f"CANNOT-EVALUATE: {error['fragment']}: {error['reason']}",
                      file=sys.stderr)
            return 2

    paths = [Path(p) for p in args.files]
    if args.fragments:
        paths += [Path(m["staged"]) for m in mapping]
    if args.census:
        paths += sorted(Path(args.root).rglob("*.md"))
    paths = sorted({p.resolve() for p in paths})
    if not paths:
        print("CANNOT-EVALUATE: no entries given", file=sys.stderr)
        return 2
    missing = [p for p in paths if not p.is_file()]
    if missing:
        for path in missing:
            print(f"CANNOT-EVALUATE: {path}: not a regular file", file=sys.stderr)
        return 2
    try:
        records = [audit_entry(p) for p in paths]
    except (UnicodeDecodeError, OSError) as exc:
        print(f"CANNOT-EVALUATE: {exc}", file=sys.stderr)
        return 2
    if args.json:
        print(json.dumps({"schema": SCHEMA, "stage": args.stage,
                          "staged": mapping, "entries": records,
                          "summary": {"total": len(records),
                                      "pass": sum(1 for r in records if r["pass"]),
                                      "clean": sum(1 for r in records if r["clean"])}},
                         indent=2, ensure_ascii=False))
    else:
        sys.stdout.write(render(records))
        for item in mapping:
            print(f"STAGED {item['fragment']} -> {item['staged']} "
                  f"({item['bytes']} bytes)")
    return 0 if all(r["pass"] for r in records) else 1


if __name__ == "__main__":
    sys.exit(main())
```

## 6. Expected results for the ten drafts

Slot map: C01–C06 author **culture-material**, C07–C10 author **myth-symbol**
(`reports/round-35/claims.json:24` = "+6 culture-material (18 → 24) and +4
myth-symbol (19 → 23)"; per-slot missions in `reports/round-35/targets.json`
`seats[id=C01..C10].mission`, each *"Author entry N (culture-material|myth-symbol,
topic per P01)"*). The exact slug per slot is **owed to P01** — the target path
column below is the shape, not the name.

| slot | partition | target path shape | expected audit reading | status at write time |
|---|---|---|---|---|
| C01 | culture-material | `corpus/knowledge/culture-material/<slug>.md` | `PASS/clean` — 4/4 + 5/5 frontmatter, `verified_at_iso`, 0 unresolved pointers, gap named, decision record, 0 ownership assertions | not written (exit 2, §7 control 5) |
| C02 | culture-material | idem | idem | not written |
| C03 | culture-material | idem | idem | not written |
| C04 | culture-material | idem | idem | not written |
| C05 | culture-material | idem | idem | not written |
| C06 | culture-material | idem | idem | not written |
| C07 | myth-symbol | `corpus/knowledge/myth-symbol/<slug>.md` | idem | not written |
| C08 | myth-symbol | idem | idem | not written |
| C09 | myth-symbol | idem | idem | not written |
| C10 | myth-symbol | idem | idem | not written |

Falsifiable expectations, per draft:

1. `frontmatter_4of4: true` and `lane_profile_5f: true`; `frontmatter_empty: []`;
   `verified_at_iso: true`; `recheck_chars >= 40`.
2. `pointers_unresolved: []`, or every dangling token marked `(to-verify` on its
   own line (`pointers_unresolved_documented`) — an unresolved *undocumented*
   pointer is a blocker, and `reports/round-35/claims.json:29` requires each new
   entry's citations to resolve or be marked in-file.
3. `gap_named: true` with `gap_field` reading `gap filled` (the modern shape: 13
   live entries carry it, e.g. `corpus/knowledge/myth-symbol/plant-symbolism.md:3`).
4. `decision_record: true` — a `## N. Decision record` heading, matching the
   round-10 runner's reading (`reports/round-10/run-validation.py:368-370`).
5. `bleed_candidates`/`ownership_assertions`: expected **0 ownership
   assertions**; any strict hit is read by the auditor (§8, limit 4).
6. `digest_pins_stale_candidates: []` — a pin that does not match the file at
   audit time must be re-measured or dated (7 live entries currently carry a
   stale pin, e.g. `corpus/knowledge/linguistics/register-lexicon-ceilings.md:18`
   pins `examples/culture-d4/packet.d4.yml` at `543d68a8…`, the file now reads
   `aac91246…` — a dated pin whose referent moved, not a fabricated source).
7. `--census` after the ten land: 211 files, `culture-material 24`,
   `myth-symbol 23`; `TOTAL pass 10/10` for the staged set.

**Deviation rules.** A `pass: false` on families 1–4 is a real defect of the
draft and must be filed with the slot id (severity as tiered in §1). A `review`
item is **not** a defect: it is a line to read, and the auditor records
`read — ordinary sense` or `read — ownership language` with the line number. A
staged file that differs in bytes from what the fragment shows means the
fragment and the audit disagreed — file it against the fragment, never against
the entry. An exit `2` on a slot means the fragment names no target path or
carries no fenced `markdown` block; that is a fragment defect, filed as
`target-path-unresolved` with the fragment path.

## 7. Controls run on the instrument itself (2026-10-19, HEAD `4a7aede`)

1. `python3 -B .scratch/c12/entry-audit-runbook.py --selftest` → exit 0,
   `SELFTEST PASS` — 3 positive controls (bullet sources, prose `- sources:`
   line as in `plant-symbolism.md:5`, brace-grouped pointers as in
   `corpus/knowledge/linguistics/register-lexicon-ceilings.md:18`), 4 negative
   controls (bleed language, dangling pointer, no-gap/no-decision, dangling
   pointer marked `(to-verify)`), a negated-bleed control that must read clean,
   plus determinism (two audits byte-identical) and no-write (fixture digests
   unchanged).
2. Six live exemplar entries: `PASS 6/6`; `clean 4/6` — the two review items are
   `stale-pin-candidate:examples/culture-d4/packet.d4.yml` and
   `:examples/culture-d4/expected-holds.json`, i.e. the dated pins of item 6.
3. Staging probe: a synthetic fragment written to `.scratch/c12/frag-probe/`
   naming `corpus/knowledge/culture-material/probe-fixture.md` staged to
   `.scratch/c12/stage-probe/…` and read `PASS/clean 1/1`, exit 0 — the §4 recipe
   proven end-to-end on the fragment→stage→audit path; the probe directory was
   deleted afterwards.
4. `--census` over all 201 entries: the §3 table (summary
   `{'total': 201, 'pass': 22, 'clean': 8}`; contract defect classes
   `decision-record-absent 179`, `gap-not-named 172`, `unresolved-pointer 2`;
   review classes `bleed-candidate 63`, `canon-mention-unnegated 95`,
   `stale-pin-candidate 7`).
5. Absent-dependency probes: `--fragments` over a fragment with no target path →
   `CANNOT-EVALUATE … no corpus target path or no fenced block`, exit 2;
   `python3 -B .scratch/c12/entry-audit-runbook.py
   reports/round-35/cov/C01-entry-1.md` → `CANNOT-EVALUATE … not a regular file`,
   exit 2. Same probe for `reports/round-35/plan/P01-c-plan.md` and
   `reports/round-35/scout/K02-entry-audit-method.md` → absent.

## 8. Limits — what a green reading does not mean

1. **Structural, not scholarly.** The instrument reads bytes: it never fetches a
   URL, never validates a citation's content, and never treats the absence of a
   `(to-verify)` marker as verification — the same caveat the lane already
   carries at `tools/source-audit-inventory.py:277-288`.
2. **`pass` is not admission.** No reading here is a clearance, a promotion, an
   acceptance or a canon decision (`PROVINCE.md:20-27`); claim C's thresholds
   (`reports/round-35/claims.json:35`) are met by the auditors' and reviewers'
   findings, not by this runbook's exit code.
3. **Two tiers, deliberately.** Review items never fail the contract, because
   they are heuristic (every record is `heuristic: true, review_required: true`);
   a runbook that failed entries on a word-list would be a false-positive
   machine. The auditor's job on a review item is to read the printed line.
4. **The bleed word-list is polysemous — measured.** 63/201 live entries carry an
   unnegated strict hit, only 5/201 an ownership-shaped one, and all 5 read as
   ordinary or in-world senses: `corpus/knowledge/civilizations/celts.md:181`
   "brooch at garment **closure**", `corpus/knowledge/civilizations/nazca.md:87`
   "Line, **cleared** area, bounded path", `corpus/knowledge/verification/
   real-world-inspiration-boundaries.md:11` "**legal clearance**",
   `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:96` "**Closure**
   over the base partition". Treat the list as a pointer to lines, never as a
   verdict; the tier that matters for the drafts is 5b (ownership assertion).
5. **URLs are unfetched by rule** (no network in this wave): `urls_unfetched`
   counts them, it does not resolve them; a draft's URL leg is checked by the
   human auditor against the access-date convention the corpus uses
   (`corpus/knowledge/myth-symbol/plant-symbolism.md:5` "web-checked 2026-10-17").
6. **The corpus baseline is not the expected rate** (§3): the 22/201 pass rate is
   the pre-contract corpus, not a prediction about the drafts.

## 9. Handoff

- **C13** (`cov/C13-audit-1-5.md`) and **C14** (`cov/C14-audit-6-10.md`): install
  the instrument with §4 step 0, confirm the sha256 equals the §5 digest, run
  steps 1–3, and report per slot with observed readings, not conclusions. The
  digest makes instrument drift detectable between the two auditors.
- **C17** (`cov/C17-audit-sample.md`): the third auditor re-runs the same bytes on
  a sample chosen by lot, and re-derives the §4b README numbers independently.
- **R01/R02/R03**: this runbook covers structure only; source-pointer resolution
  re-checked by reading, frontmatter re-read, no-fabrication hunt and the
  audit-runbook adequacy judgement are theirs (they may falsify any §6
  expectation).
- **C15/S01** (receipts) and the **integrator**: the instrument is drafted here,
  not installed; if the round wants it durable the integrator may copy the §5
  bytes to a `tools/` path under its own change record — that decision is not
  this seat's.

## Owed

- `reports/round-35/plan/P01-c-plan.md` — the slug/topic mapping for C01–C10 and
  therefore the exact `corpus/knowledge/<partition>/<slug>.md` target paths; §6
  is stated per slot until it lands. Missing at write time (§7 control 5).
- `reports/round-35/scout/K02-entry-audit-method.md` — prior-art cross-read of the
  defect classes. My checklist is built from the primary sources K02 was to
  summarize (`reports/round-10/run-validation.py:81,362-370`,
  `reports/round-19/audit/entry-audit.py:25-31,49-96`), so no method gap is
  expected; a cross-read is owed to the integrator.
- `reports/round-35/cov/C01..C10-entry-*.md` — the ten drafts themselves; §6 is
  the contract they are audited against, and the per-slot readings are the
  auditors' to fill in.
- `reports/round-35/cov/C11-readme-delta.md` — the exact README delta bytes; §4b's
  post-landing numbers are derived from the claim, not read from C11.
- `reports/round-35/run-validation.py` — claim C counting command 3
  (`reports/round-35/claims.json:33`); absent, and per the wave's absolute rule
  it is never executed in-tree by a seat — an isolated `git archive` copy only.

## Citations

- `reports/round-35/claims.json:5,8-9,17,24,29,30-35` — round position, baseline,
  claim C's text, `after_required`, counting commands and thresholds.
- `reports/round-35/targets.json` — `seats[id=C12].mission`, `seats[id=C01..C10]
  .mission`, `seats[id=C13,C14,C17].mission`, `shared_rules`.
- `reports/round-35/telemetry/availability-attempt-{1,2,3}.json`,
  `telemetry/dispatch-declared.json` — the wave's declared provider/attempt record
  (read for context; no availability claim is made here).
- `reports/round-10/run-validation.py:81` — `C_FRONTMATTER_FIELDS`; `:362-370` —
  the gap and decision-record readings; `:381-398` — the README index parser shape
  reused in §4b.
- `reports/round-19/audit/entry-audit.py:25-31` — the prior entry-audit regexes;
  `:49-71` — the source-bullet locator definition; `:74-96` — couples resolution.
- `corpus/QUALITY.md:3-23` — the admission bar (provenance, calibration, coupling,
  usability, canon hygiene) that families 1–4 read structurally.
- `corpus/README.md:3-15,69-93,123,147,169,342,469,471-480` — revision convention,
  the round-20 verbatim-row repair rule, the three partition headings, the totals
  line, the counts footer and its measured command.
- `corpus/knowledge/verification/header-conformance-readings.md:1-6` — "no header
  count without its reading id", the discipline §2 applies.
- `corpus/knowledge/myth-symbol/plant-symbolism.md:3-9` — the modern frontmatter
  shape (`gap`, `topic`, prose `sources`, `couples`, `source`, `verified-at`,
  `recheck`) used as a positive control.
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:18` — the dated digest
  pin and brace-grouped pointers used as controls.
- `corpus/knowledge/civilizations/celts.md:181`,
  `corpus/knowledge/civilizations/nazca.md:87`,
  `corpus/knowledge/verification/real-world-inspiration-boundaries.md:11`,
  `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:96` — the four
  measured polysemy examples of §8 limit 4.
- `tools/source-audit-inventory.py:277-288` — the read-only/heuristic caveat
  convention copied into §8 limit 1.
- `PROVINCE.md:5-27` — owns/refuses and the adjacent contract (§8 limit 2).
- Command outputs, 2026-10-19 at HEAD `4a7aede` (`git rev-parse --short HEAD` →
  `4a7aede`): the §3 census summary and class counts; the §7 controls 1–5; the
  partition census `21 19 18 29 20 94` / total `201`; the inventory
  `totals.files 201`; the frontmatter field census `scope 0, sources 201,
  source 134, couples 201, verified-at 201, recheck 201`; the instrument digest
  `973610275404e9e3183d46e33e5352562265e6c2e397c92291e63c401ed7562d` (663 lines).
