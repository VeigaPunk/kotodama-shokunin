- Seat: X04 | critic | claim cross | date 2026-10-19 | baseline 4a7aede

# X04 — honesty critic: to-verify census, fabrication-risk hunt over the ten entry drafts

**Mission** (`reports/round-35/targets.json:400-406`, seat X04): "Honesty critic: to-verify
census, fabrication-risk hunt across the 10 drafts (unresolvable citations)." Out path:
`reports/round-35/cross/X04-honesty.md`.

**Read window.** 2026-10-19T08:16Z–08:2xZ (`date -u +%FT%TZ` → `2026-10-19T08:21:21Z`), lane
HEAD `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4` (`git rev-parse HEAD`), working tree tracked-clean
(`git status --porcelain` → only `?? reports/round-35/`), env
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

**Boundary statement.** This seat wrote exactly one file: this one. No `corpus/` byte, no tool
byte, no `reports/round-1..34` byte was written or edited. **No `reports/round-*/run-validation.py`
was executed anywhere** (F-C13-1 prevention), and `tools/exercise-handoff-e2e.py` was not executed
by this seat (the O-claim's seats own that run). The only executables this seat ran are: its own
read-only resolver (script embedded in §2, no write path in its source), `python3 -B
tools/source-audit-inventory.py --json --summary` (filed tool, `read_only: true` in its own output),
and read-only shell (`grep`/`sha256sum`/`wc`/`find`/`sed`/`ls`).

**Dependency state at cut.** The ten entry drafts **are not on disk**.
`find reports/round-35 -name '*.md'` → 12 fragments: `adj/{A05,A06,A09}`, `cov/{C11,C15,C16}`,
`cross/X02`, `op/{O08,O10}`, `review/R06`, `scribe/{S01,S02,S03,S05}`. **No `cov/C01..C10` and no
`cov/C12/C13/C14/C17` exists**, and `plan/`, `scout/`, `depth/`-equivalents are absent. §3 is
therefore a **pre-landing** fabrication-risk register over the declared claim, plus a runnable hunt
recipe (§2, §7) the integrator or a later seat can apply to the drafts the moment they land. This
is stated as a limit, not hidden: the mission's core artifact could not be executed against bytes
that do not exist.

---

## 1. to-verify census (live, at HEAD `4a7aede`)

### 1.1 Corpus marker census — filed instrument, this seat's own run

`python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` (read-only
per its own `read_only: true` / `deterministic: true` header):

| metric | value |
|---|---|
| files | 201 (36395 lines) |
| `files_with_any_mark` / `files_with_marker` | 147 / 135 |
| `raw_lines` / `raw_occurrences` | 717 / 731 |
| `marker_occurrences` | 655 (bare 621 + detailed 34) |
| `marker_lines` | 650 |
| `unparenthesized_occurrences` | 78 |
| heuristic classes | substantive-flag-candidate 563 / policy-use-mention 37 / needs-review 133 |

The instrument's own caveat block states the reading discipline this census keeps:
`marker_absence_is_not_verification: true`, `markers_never_auto_cleared: true`,
`classification_is_heuristic_needs_review: true`. **A clean file is not a verified file**, and no
seat may read a zero-marker entry as sourced truth.

**13 files carry the detailed `(to-verify: …)` form** — a named research target rather than a naked
mark: `linguistics/sound-symbolism.md` (2), `linguistics/language-shift-obsolescence-revival.md`,
`myth-symbol/direction-symbolism.md`, `culture-material/ritual-garments.md`,
`culture-material/vessel-container-lexicon.md`, `synthesis/costume-language-coupling-table.md` (4),
`synthesis/taboo-euphemism-lifecycle.md`, `civilizations/levant-canaan-phoenician.md` (2),
`civilizations/dine-navajo.md`, `civilizations/ottoman.md` (4), plus three not printed at the cut
(§6 limit). Of the two partitions claim C expands, **`myth-symbol/direction-symbolism.md` and
`culture-material/vessel-container-lexicon.md` already carry detailed markers** — new entries must
not silently supersede them.

### 1.2 Policy surfaces (marker count, `grep -c 'to-verify'`)

| surface | count | disposition |
|---|---|---|
| `SKILL.md` | 19 | policy vocabulary (`status: to-verify` as a verdict value; triage rules) — not open research claims |
| `LOG.md` | 95 | findings vocabulary + filed `to-verify` attributions (e.g. the F-C13-1 writer attribution) — must stay marked, never upgraded |
| `corpus/README.md` | 2 | policy prose (the "or is marked to-verify" rule) |
| `corpus/QUALITY.md` | 1 | the admission-bar rule itself (`QUALITY.md:5-7`) |
| `AGENTS.md` | 1 | the rule "claims you cannot verify are marked `to-verify`" |
| `PROVINCE.md`, `SCORECARD.md`, `MINT.md`, `SHONEN.md`, `README.md`, `REGIMEN.md` | 0 | findings carried as `F-…` ids instead |

### 1.3 Round surfaces

| surface | raw `to-verify` lines / files |
|---|---|
| `reports/round-33/**` | 137 / 66 |
| `reports/round-34/**` | 99 / 64 |
| `reports/round-35/**` (12 landed fragments) | 10 / 12 |

The round-35 lines are: `adj/A06-province.md:185,193` (a limits heading + an explicit
fleet-level `to-verify`), `op/O10-scribe.md:147` (a named stale-wording question),
`scribe/S01-c-receipt.md:42,242,243,248,316` (the claim text, two inventory INFO lines, and its own
owed-path table), `scribe/S05-telemetry-draft.md:461,464` (two named telemetry unknowns). **Every
one is a named unknown with an owner or a policy mention — none is an unflagged assertion.**

### 1.4 Inherited open items that must NOT be read as closed

| id | filed source | status re-verified at this cut |
|---|---|---|
| **F-C15-1** — the numeral "12" (SCORECARD:444-445 / LOG:3513 / round-32 dossier:107-108) is reconstructed, not quoted | `reports/round-33/calib/open-items-ledger.json` `findings[]` → `{"id": "F-C15-1", "status": "to-verify", …}` | **still `to-verify` at HEAD** (read this seat). Claim C's landing does not touch it; it must not drop out of the ledger |
| F-C13-1 writer attribution (`LOG.md:3556`, "probable writer: seat C05, `to-verify`") | filed | unprovable from artifacts; **no seat may upgrade it** |
| R34-N1 (KeyError replay) | `reports/round-34/handoff/repin.json`; `reports/round-35/scout/K03-keyerror-path.md:30,101,107` | **open by design** — claim O owns the fix; K03 confirms `E2E-READSET` occurs 0 times in the renderer (`K03:101`) |
| round-35 telemetry close | `reports/round-35/telemetry/dispatch-declared.json` → `"closing_snapshot": "open-at-seat-close: …"` | **owed**; round 35 is not admissible to `LOG.md` while owed (`AGENTS.md:32-38`) |

---

## 2. The hunt instrument — built, calibrated, and runnable

### 2.1 Calibration on the live corpus (the honest baseline a draft is judged against)

Read-only resolver run over all 201 entries (`--root corpus/knowledge`):

| metric | value |
|---|---|
| in-repo `path[:line]` citations | **736** |
| unresolved in-repo paths | **3** (99.6% resolve) |
| cited line out of file range | **0** |
| basename citations | 513 (7 ambiguous, 14 unresolved) |
| unique `http(s)` URLs | 1765 |
| files with no URL at all | 51 of 201 |
| files with URLs but **zero** freshness declaration (`fetched`/`carried`/`not re-retrieved`) | 102 of 150 |

**The three live dangling in-repo citations** (filed bytes — recorded, never edited in place):

| citing line | dangling target | reading |
|---|---|---|
| `corpus/knowledge/myth-symbol/flood-traditions.md:18` | `corpus/myth-symbol/comparative-frameworks.md` | missing the `knowledge/` segment; the real file is `corpus/knowledge/myth-symbol/comparative-frameworks.md` |
| `corpus/knowledge/verification/gate-frozen-run-standard.md:66` | `corpus/verification/citation-format-and-source-registry.md` | same class: real file is `corpus/knowledge/verification/citation-format-and-source-registry.md` |
| `corpus/knowledge/verification/provenance-audit-ledger-format.md:14` | `corpus/lessons/provenance-audit-ledger.md` | names a *suggested future* ledger location ("Suggested future ledger location: … does not create a ledger") — deliberate, not a defect |

The 14 unresolved basenames split into two honest classes: **9** name documents of the sibling/bible
trees that do not live in this repo (`PROTOCOL.md` ×2 and `PROTOCOL-APPENDIX.md` ×2 at
`gate-frozen-run-standard.md:5,6,7,16`; `CORPUS.md` ×4 at `header-conformance-readings.md:7,28,137,158`;
`lore-handoff-contract.md` at `conlang-methodology.md:146`) — checkable only outside this lane; and
**5** name corpus `.md` files absent at HEAD (`sound-change.md`, `tone-prosody.md` at
`phonetics-phonology.md:279`; `phonology-basics.md`, `naming-and-onomastics.md`,
`honorifics-and-register.md` at `language-contact.md:7`) — **`to-verify`** whether these are planned,
renamed, or stale pointers.

**URL host census (top hosts, unique URLs):** doi.org 309, books.google.com 80, en.wikipedia.org 39,
ich.unesco.org 28, metmuseum.org 27, cambridge.org 26, archive.org 25, assets.cambridge.org 22,
penelope.uchicago.edu 22, wals.info 20, ucpress.edu 17, uhpress.hawaii.edu 16. By partition:
civilizations 1373, synthesis 231, verification 120, linguistics 25, **culture-material 15**,
**myth-symbol 1**. The two partitions claim C expands hold **16 unique http URLs across 37 files** —
the drafts' sourcing must therefore lean on bibliographic records and in-repo carriers, and no
reviewer in this round can re-fetch anything (§3 R1).

### 2.2 The defect classes the resolver catches

1. **dangling in-repo path** — a `corpus/…md`/`reports/…`/`tools/…` citation whose file is absent;
2. **line drift** — a cited `:line` beyond the target file's length;
3. **ambiguous basename** — a bare `` `foo.md` `` matching more than one live file;
4. **unmarked freshness** — a URL with no `fetched`/`carried`/`not re-retrieved` declaration in its
   file (file-level, not per-URL — stated as a limit);
5. **marker inventory** — raw / parenthesized / detailed `to-verify` counts per file.

### 2.3 The instrument (embedded so the recipe is durable; `.scratch` is gitignored)

Write to any temp path and run: `python3 -B <path> --root reports/round-35/cov` (summary) or
`--json --verbose` (per-citation records). No write path exists in the script.

```python
#!/usr/bin/env python3
"""honesty-scan — read-only citation/marker resolver (X04 round-35)."""
import json, os, re, sys
from collections import Counter
ROOT = os.path.abspath(os.getcwd())
PATH_RE = re.compile(r"(?<![\w/.-])((?:corpus|tools|examples|reports|\.scratch)/[\w./-]+?\.(?:md|py|json|yml|yaml|txt))(?::(\d+)(?:-(\d+))?)?")
BASE_RE = re.compile(r"`([\w][\w.-]*\.md)(?::(\d+)(?:-(\d+))?)?`")
URL_RE  = re.compile(r"https?://[^\s)\]>,;\"']+")
FM = ("source", "verified-at", "recheck", "couples", "topic")
def idx():
    d = {}
    for base in ("corpus/knowledge", "corpus/lessons", "tools", "."):
        for dp, _s, fs in os.walk(os.path.join(ROOT, base)):
            if "/frozen/" in dp or "/scratch/" in dp or ".git" in dp: continue
            for fn in fs:
                if fn.endswith(".md"):
                    rel = os.path.relpath(os.path.join(dp, fn), ROOT)
                    if rel not in d.setdefault(fn, []): d[fn].append(rel)
    return d
IDX = idx()
def nlines(p):
    try: return sum(1 for _ in open(os.path.join(ROOT, p), encoding="utf-8", errors="replace"))
    except OSError: return None
def scan(p):
    lines = open(p if os.path.isabs(p) else os.path.join(ROOT, p), encoding="utf-8", errors="replace").read().splitlines()
    out = {"file": p, "repo": [], "base": [], "urls": [], "tv": Counter(), "fresh": Counter(), "fm": {}}
    for i, ln in enumerate(lines, 1):
        for m in PATH_RE.finditer(ln):
            q, a, b = m.group(1), m.group(2), m.group(3)
            ok = os.path.isfile(os.path.join(ROOT, q)); r = {"p": q, "line": int(a) if a else None, "src": i, "exists": ok}
            if ok and a:
                n = nlines(q); r["in_range"] = bool(n and int(a) <= n and int(b or a) <= n)
            out["repo"].append(r)
        for m in BASE_RE.finditer(ln):
            h = IDX.get(m.group(1), [])
            out["base"].append({"p": m.group(1), "src": i, "exists": bool(h), "ambig": len(h) > 1, "cand": h})
        out["urls"] += URL_RE.findall(ln)
        if re.search(r"to-verify", ln, re.I): out["tv"]["raw_lines"] += 1
        for m in re.finditer(r"\(to-verify([^)]*)\)", ln, re.I): out["tv"]["detailed" if m.group(1).strip() else "bare"] += 1
        if re.search(r"(fetched|re-fetched|web-retrieved|retrieved)\b[^.\n]{0,40}?\d{4}-\d{2}-\d{2}", ln, re.I): out["fresh"]["fetched"] += 1
        if re.search(r"(not re-retrieved|carried via|carried in this partition|not retrieved this session|web-retrieved)", ln, re.I): out["fresh"]["carried"] += 1
    head = "\n".join(lines[:25])
    for f in FM:
        pat = r"^-\s*(sources?)\s*:" if f == "source" else r"^-\s*%s\s*:" % f
        out["fm"][f] = bool(re.search(pat, head, re.M))
    out["urls"] = sorted(set(out["urls"])); out["tv"] = dict(out["tv"]); out["fresh"] = dict(out["fresh"])
    return out
files = []
if "--root" in sys.argv:
    base = sys.argv[sys.argv.index("--root") + 1]
    for dp, _s, fs in os.walk(os.path.join(ROOT, base)):
        files += [os.path.relpath(os.path.join(dp, f), ROOT) for f in fs if f.endswith(".md")]
else:
    files = [a for a in sys.argv[1:] if not a.startswith("--")]
recs = [scan(f) for f in files]
repo = [c for r in recs for c in r["repo"]]
print(json.dumps({
    "files": len(recs), "repo_citations": len(repo),
    "repo_unresolved": sum(1 for c in repo if not c["exists"]),
    "repo_line_out_of_range": sum(1 for c in repo if c.get("in_range") is False),
    "basename_unresolved": sum(1 for r in recs for c in r["base"] if not c["exists"]),
    "basename_ambiguous": sum(1 for r in recs for c in r["base"] if c["ambig"]),
    "urls_unique": sum(len(r["urls"]) for r in recs),
    "hosts": dict(Counter(re.sub(r"^https?://", "", u).split("/")[0] for r in recs for u in r["urls"]).most_common(10)),
    "to_verify": dict(Counter({k: sum(r["tv"].get(k, 0) for r in recs) for k in ("raw_lines", "bare", "detailed")})),
    "freshness": {k: sum(r["fresh"].get(k, 0) for r in recs) for k in ("fetched", "carried")},
    "frontmatter_missing": {f: sum(1 for r in recs if not r["fm"][f]) for f in FM},
}, indent=1))
for r in recs:
    bad = [("path", c["p"], c["src"]) for c in r["repo"] if not c["exists"]] + \
          [("base", c["p"], c["src"]) for c in r["base"] if not c["exists"] or c["ambig"]]
    if bad: print("UNRESOLVED", r["file"], bad[:6])
```

---

## 3. Fabrication-risk register for the ten drafts (pre-landing, over the declared claim)

Each risk names the evidence at HEAD, the failure mode, and the check that discharges it. None of
these is asserted as a defect in the drafts — the drafts do not exist at this cut.

**R1 (high) — no network in this round, so every URL in a draft is a carried citation.**
`reports/round-35/targets.json:9` binds every seat: "no git commits/pushes, no installs, no network".
Therefore "source-resolving" for a URL can only mean *resolves to a source recorded in a prior
round's receipt* or *is marked `to-verify` in-file* (`corpus/QUALITY.md:5-7`: "A claim the author
cannot verify is marked `(to-verify)` inline — never laundered into assertion"). A draft that dates
a fetch to **2026-10-19** would be claiming a network act no seat could perform.
*Check:* `freshness` counts + the `verified-at:` date per draft; a 2026-10-19 fetch claim on a URL
is a **fabrication signal**, not a style issue.

**R2 (high) — claim C's audit bar names a field the corpus does not carry.**
`claims.json:24` requires "frontmatter-complete (source / verified-at / recheck / scope)";
`claims.json:29` requires "frontmatter 4/4 or documented 3/4 class". Measured: **0 of 201**
`corpus/knowledge/**` files carry a `- scope:` line (full-file `grep -rlE '^- scope:'` → 0), and the
four live entry fields are `- topic:`, `- sources:`, `- couples:`, `- verified-at:`/`- recheck:`.
The filed precedent instrument states the real contract:
`reports/round-19/audit/entry-audit.py:106` → `required = {"topic", "sources", "couples"}`,
`:108` → `tail_ok = ("verified-at" in fields) and ("recheck" in fields or "source" in fields)`.
A literal reading of claim C would score **every** draft "3/4 (no `scope:`)" and manufacture ten
false defects.
*Check / required action:* the integrator re-keys the threshold wording (append-only correction to
the dossier, never an edit of `claims.json`'s filed intent) or states that "4/4" means
`topic/sources/couples` + the verified-at/recheck tail. C13/C14/C17 and R01/R02 should audit against
the filed instrument's contract.

**R3 (medium) — "two independent auditors" is in-batch independence.**
The threshold (`claims.json:35`) says "10/10 new entries audited clean (two independent auditors)".
C13, C14 and C17 are same-batch seats, as are R01/R02. `REGIMEN.md:41` requires a **named non-author
reviewer** for any `unprovable-but-better` verdict — a name exists, but the dossier must state the
seat **and** the artifact it read, and must not present an in-batch peer as external verification.
*Check:* the coverage dossier names seats + read artifacts; no "independent" claim without that.

**R4 (medium) — the defect class this mission names has precedent, and it was filed, not waived.**
Round 19's ten entry drafts + reviews (the closest analogue: same shape, +10 entries) carry **5
unresolvable in-repo citations**: `.scratch/r19c/check.py` (`review-C11.md:47`, `-C12.md:38`,
`-C13.md:39` — a transient instrument, unreproducible by design),
`corpus/knowledge/linguistics/phonology-sanity.md` (`review-C11.md:68`),
`reports/round-18/d4/ASSEMBLY.md` (`review-C11.md:115`). One of them became a filed finding:
`reports/round-19/entries/review-C11.md:115-117` → **R19C21-F1**, "L14 `couples` names
`../linguistics/phonology-sanity.md`; no such file exists", severity low, **open — reported to
parent**. So: a dangling `couples:` pointer is a *finding*, not a rejection, but it must be filed.
*Check:* run §2.3 over `reports/round-35/cov/C01..C10` after landing; every `couples:` target must
resolve (the r19 instrument resolves brace-aware against the entry dir, the lane root, and
`corpus/knowledge/`).

**R5 (medium) — the README reconciliation is a four-surface edit, and one surface has already been
missed once by a green sweep.** Verified at HEAD: `corpus/README.md` sha256
`053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`, 106 218 bytes, 493 lines;
index rows **201** = live files **201**, per-section headers 21/19/18/29/20/94, `Total knowledge
entries: 201.` (`:469`), footer `(total 201 files; directory totals 21/19/18/29/20/94).`
(`:471-473`). A +6/+4 landing must move: (a) section headers `## myth-symbol/ (19)` → `(23)` and
`## culture-material/ (18)` → `(24)`, (b) 10 rows, (c) `:469` totals line, (d) the `:471-473`
footer, plus (e) a new revision block. `corpus/README.md:16-30` (revision 1.8) records that the
**footer** was left stale while the totals line moved, and that round-27's sweep went green over it
— the reason the round-28 sweep adds a footer leg. Claim C's `after_required` names "README
partition counts and index rows" but not the footer; a validator that checks only rows and headers
would repeat revision 1.8's miss.
*Check:* `python3 -B reports/round-28/readme/sweep.py` (filed, read-only in live mode; digest
`9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`, matches
`reports/round-35/cov/C11-readme-delta.md:20`) with `footer_ok` read, not just `totals_ok`.

**R6 (medium) — the O-claim's "no freeze bytes move" leg is currently true; the moving digest that
looks like drift is the r34 repoint, not a defect.** Independent verification this seat ran:
`reports/round-30/handoff/declared-in-r6/freeze.txt` pins `packet_sha256 6ced88ad009f1cfc…` and
`twin_sha256 6633443d70ce44ed…`; live `packet.md`/`twin.json` hash **6ced88ad…/6633443d…** —
**MATCH, no freeze byte moved**. Separately, `tools/exercise-handoff-e2e.py:1933-1934` now defaults
to `reports/round-34/handoff/declared-in-r7/…`, and the r7 packet's live sha256 is
`45f5713261762a959ba77b057654c8db06d140e12e2236ef9bc8ad676e7fac19` — **exactly** the
`packet_sha256=45f57132…` in `reports/round-35/op/O08-validation-legs.md:31`. So the digest
difference against round 34's own reading (`reports/round-34/cross/X01-trades.md:11`,
`6ced88ad…` at the r6 default) is **explained** by the r34 D-claim's repoint, not by input drift.
*Check:* keep the r6 pin re-verified at close; do not report the r7 digest as a regression.

**R7 (low) — the telemetry honesty legs are partially owed.** See §5.

**R8 (low) — my own census must not manufacture defects.** The round-34 fragment set shows **214**
unresolved in-repo citations, but classification by citing-line context gives: **59** future-round
paths quoted from fixtures (`reports/round-9x/run-validation.py` inside selftest designs), **51**
deliberate negatives/fixtures (`r8_checks_MUTATED.py`, `cache-export.py` as a C− control,
`corpus/lessons/round-33.md` explicitly recorded as "does not exist"), **41** round-34 self-refs to
artifacts not yet landed at write time, **11** `.scratch` transients, and **52** unclassified. **No
fabricated citation was found in the round-34 fragments by this pass**; the 52-file residue is
unread → `to-verify` (§6).

---

## 4. Declared before-states and premises — verified / corrected

| premise | verdict | evidence |
|---|---|---|
| C `before.partition_counts` = 21/19/18/29/20/94 = 201 | **verified** | `ls corpus/knowledge/$p/*.md \| wc -l` per partition → 21/19/18/29/20/94; total 201 |
| C `before` matches the README index | **verified** | README rows 201 = live 201, headers 21/19/18/29/20/94, `:469` totals 201, `:471-473` footer 201 |
| C threshold "README counts == live census" is a *new* reconciliation | **correct as of HEAD** | README revision 1.9 (`:3-15`) already reconciles to 201/201; the delta is purely additive |
| C "frontmatter 4/4 (source / verified-at / recheck / scope)" | **imprecise — see R2** | 0/201 entries carry `- scope:`; filed contract is `entry-audit.py:106,108` |
| O "the r6-row replay dies with `KeyError`" | **verified by K03, not re-run here** | `reports/round-35/scout/K03-keyerror-path.md:30` (`KeyError: 'reports/round-20/handoff/claims-map.md'`), `:101` (`E2E-READSET` occurs 0 times), `:107` (exit-1 family) |
| O "no freeze bytes move" | **verified this seat** | r6 pins 6ced88ad…/6633443d… match live bytes (R6) |
| O "the r7 default chain still exits 0" | **corroborated** | `O08-validation-legs.md:31` (B2) exit 0 with the r7 packet digest; consistent with `exercise-handoff-e2e.py:1933-1934` |
| A "the last two rounds touched shared files" | **verified in part** | `git log --oneline -3` → `4a7aede` (round 34) / `da68a6d` (round 33); both are the only commits since `139e3b6`; this seat did not re-audit each surface (A01-A11 own that) |
| X04's own calibration numbers | **self-measured, reproducible** | §2.1 commands; digests: `corpus/README.md` 053966a2…, `reports/round-28/readme/sweep.py` 9b2ccac0… |

**Nothing in the round-35 declarations was found fabricated.** Every path, line, digest and count
this seat re-measured resolved as declared. The two declaration defects are wording/scope (R2) and
an under-specified threshold surface (R5) — both correctable by append-only dossier wording, neither
requiring a filed-byte edit.

---

## 5. Telemetry honesty (the one place a reader could misread the round)

| observation | evidence | verdict |
|---|---|---|
| three 402'd keys recorded, **zero launched** on each, `null` never faked | `telemetry/availability-attempt-{1,2,3}.json`: `launched_workers 0`, `failed_workers 64`, `failure_class '402 …'`, each with a `counting_command` and `counting_date` | **honest** |
| keys 6-7 not probed | `availability-attempt-3.json` `disposition`: "presumed dry by pattern (not probed …; labeled inference)" | **honest** — an inference, labeled as one |
| declared lane ≠ observed route | `dispatch-declared.json` → `allocation/provider_lane 'opencode-go-3'`; `availability-attempt-3.json` → `key_census_so_far` records key 3 as 402/zero-launched; this seat's own batch ran on **key 1** (seat prompt; corroborated independently by `reports/round-35/scribe/S05-telemetry-draft.md:19-21`: "declared `opencode-go-3`, actual `opencode-go key 1`") | **owed** — the observed-dispatch record must state the actual route; `AGENTS.md:21-29` keeps requested allocation separate from observed route |
| closing snapshot | `dispatch-declared.json` → `"closing_snapshot": "open-at-seat-close: …"` | **owed** (owner: integrating parent) — round 35 is not admissible to `LOG.md` while owed (`AGENTS.md:32-38`) |

---

## 6. Truthful limits of this seat

- **The mission's core artifact does not exist at my cut**: no `cov/C01..C10` entry draft. §3 is a
  register over the declared claim + a runnable hunt (§2.3, §7), not a finding set over draft bytes.
  A reviewer must not read §3 as "the drafts were audited".
- The URL freshness census is **file-level**, not per-URL: a file with one `fetched` line counts as
  declared even if other URLs in it are unmarked. 102/150 URL-bearing files carry no declaration at
  all — so demanding the declaration of the ten drafts is a **new bar**, defensible (no network) but
  not a live corpus norm. Stated so it is not sold as one.
- Three of the 13 detailed-marker files were not printed in §1.1 (output cut); their identities are
  recoverable with `--json --verbose`.
- The 52 unclassified round-34 unresolved citations (§3 R8) were not read line by line.
- `reports/round-19/audit/entry-audit.py` was **read, not run** (its `--since` mode is a filed-round
  instrument; F-C13-1 discipline keeps this seat off filed runners and their helpers where a write
  path cannot be excluded by reading).
- The 5 unresolved corpus basenames in `language-contact.md:7`/`phonetics-phonology.md:279` are
  `to-verify`: this seat did not establish whether they name planned, renamed, or stale targets.
- No axis verdict is claimed by this seat: this fragment is evidence for claim C's coverage verdict
  and for the cross-claim conformance record, not a verdict of its own.

## 7. Post-landing hunt — status at cut and the exact recipe

At my final cut (`ls reports/round-35/cov/` → `C11-readme-delta.md`, `C15-receipt.md`,
`C16-scribe.md`) the drafts had not landed. The hunt is therefore **owed** and is fully specified:

```sh
# write the §2.3 script to any temp path, then:
python3 -B <script> --root reports/round-35/cov          # summary over the drafts
python3 -B <script> --json --verbose --root reports/round-35/cov > /tmp/x04-drafts.json
# per-draft manual legs (no network):
grep -n '^- \(topic\|sources\|couples\|verified-at\|recheck\|gap\)' reports/round-35/cov/C0[1-9]-entry-*.md reports/round-35/cov/C10-entry-10.md
grep -nE 'https?://' reports/round-35/cov/C0[1-9]-entry-*.md reports/round-35/cov/C10-entry-10.md
grep -n '2026-10-19' reports/round-35/cov/C0[1-9]-entry-*.md reports/round-35/cov/C10-entry-10.md   # any 10-19 fetch claim = fabrication signal (R1)
```

**Pass criteria** (each leg falsifiable): (1) every in-repo `path[:line]` in every draft resolves and
is in range — judged against the live baseline **733/736 (99.6%)**; (2) every `couples:` target
resolves (R19C21-F1 class); (3) no URL is dated `fetched 2026-10-19`; carried sources say so;
(4) each entry carries `- topic:`/`- sources:`/`- couples:` + `- verified-at:` + (`- recheck:` or
`- source:`) per `entry-audit.py:106,108` — **not** a `scope:` field; (5) every `to-verify` marker in
a draft is either a detailed named target or a policy mention, and the count is added to §1.3;
(6) any draft whose unresolved-citation rate exceeds the live corpus baseline is a named finding with
an owner, not a silent pass.

## 8. Draft hunt — executed on the drafts that landed (appended after §1–§7)

The drafts began landing at ~08:22Z; this section is the hunt §7 specified, run on real bytes at
**08:26Z–08:31Z** with the §2.3 resolver (`--json --verbose --root reports/round-35/cov`).
Landed and hunted: **C01, C02, C03, C05, C06, C07, C08, C09, C10** (9 of 10). **Not landed at this
cut: C04** (and C13; `cov/C12`'s own slot map already reads "not written" for C04 —
`C12-audit-runbook.md:868`).

**The tree is moving under this table.** The drafts were being edited while this seat hunted them:
between two scans 40 seconds apart, C02's citation count moved 36 → 56 and C03's 53 → 65 (drafts
re-cut their self-audit blocks). The numbers below are the **stamped reading at 08:31Z**
(`.scratch/x04/cov4.json`, transient) — a later reader must re-run the resolver rather than quote
this table as current. Totals for the nine hunted drafts: **720 in-repo citations, 31 unresolved**
(95.7% resolve; the live-corpus baseline is 99.6%, §2.1 — the gap is almost entirely the owed P01
dependency and the drafts' own not-yet-landed targets, not bad sourcing).

| draft | in-repo `path` cites | unresolved | classification of every unresolved |
|---|---|---|---|
| C01-entry-1 | 132 | 6 | own proposed target `culture-material/mortuary-material-culture.md` ×4 (`:7,:13,:281,:309`); `reports/round-35/plan/P01-c-plan.md` ×2 (`:8,:309`) |
| C02-entry-2 | 56 | 3 | own target `agrarian-field-system-lexicon.md` (`:11`, labelled "Proposed target path (integrator applies)"); `P01-c-plan.md` (`:263`); `culture-material/plant-symbolism.md` (`:281`) — **corrected in the same line** to `corpus/knowledge/myth-symbol/plant-symbolism.md:1-9` |
| C03-entry-3 | 65 | 5 | own target `writing-media-and-surface-economy.md` (`:31,:292`); `P01-c-plan.md` (`:8,:292`); `culture-material/C03-draft.md` (`:263`, the draft's own staged extraction name inside its quoted self-audit JSON) |
| C05-entry-5 | 84 | 4 | own target `furniture-interior-lexicon.md` (`:6,:251`); `era-periodization-models.md` missing the `culture-material/` segment (`:80`) — **corrected in the same line**; `P01-c-plan.md` (`:263`) |
| C06-entry-6 | 45 | 3 | own target `fire-fuel-light.md` (`:5,:240`); `P01-c-plan.md` (`:255`) |
| C07-entry-7 | 78 | 4 | own target `eschatology-world-end-systems.md` (`:7,:296`); `P01-c-plan.md` (`:13,:301`) |
| C08-entry-8 | 53 | 4 | own target `sacred-kingship-mythic-charter.md` (`:20,:79`); `P01-c-plan.md` (`:314,:351`) |
| **C09-entry-9** | 102 | 3 | own target `myth-symbol/death-afterlife-eschatology.md` (`:34,:41,:47`) — **no P01 citation, and no other unresolved path** |
| **C10-entry-10** | 82 | **8** | own target `myth-symbol/binding-speech-complex.md` ×4 (`:24,:378,:462,:492`); `P01-c-plan.md` ×2 (`:13,:474`); **`reports/round-28/entry/C41.md` (`:551`) — DANGLING, see H8**; `reports/round-35/review/R01-c-review.md` (`:489`, peer fragment not yet landed) |

**H1 (medium, owed) — eight of the nine drafts cite a plan fragment that has not landed.**
`reports/round-35/plan/P01-c-plan.md` is cited **13 times across 8 drafts** (C09 is the exception)
and **does not exist** (`plan/` holds only `P02-oa-plan.md`). C12's runbook independently records the
same dependency as owed (`C12-audit-runbook.md:21,24,860,987`). Owner: the P01 seat / integrator —
either P01 lands, or those citations must be repointed at close. **Post-integration, this is a
dangling citation in eight filed entries' audit trail.**

**H2 (low, positive) — no genuine dangling *corpus* pointer survives context reading.**
Two mechanically-flagged wrong corpus paths exist (`C02:281`, `C05:80`) and **both carry the
corrected path in the same line**. This is the R19C21-F1 class, and it does not fire here on corpus
targets. **Independent corroboration (landed at 08:32Z):** `cov/C13-audit-1-5.md:110` files the same
C05 pointer as **F2** — "**C05 carried a literal dangling pointer** `corpus/knowledge/era-periodization-models.md`
(partition segment missing)", observed at staging sha `9dddc9d1fb1a3175` where the runbook's own
checker read `FAIL … [blocker] unresolved-pointer:…`, and **repaired in the current revision**
(`eaa48a8988d27466`, `ptr=5/5`). So the auditor caught it before I did and the draft fixed it; my
08:29Z reading caught the interim state. Recommended: C12's leg 2 already exempts same-line
`(to-verify)`-marked tokens (`C12-audit-runbook.md:37,915`); extend the same treatment to *same-line
corrected* paths so the audit does not file a false blocker — and note that a wrong form sitting in
the bytes is worth normalizing even when a corrected form follows it.

**H3 (medium) — marker-form divergence will make the round's own to-verify census undercount.**
The filed inventory tool counts a marker only in the parenthesized form
(`\(to-verify[^)]*\)`, `tools/source-audit-inventory.py` metric definitions; `unparenthesized_occurrences`
= the complement). Measured per draft (paren / backticked / bold): **C01 0/10/34**; C02 22/1/0;
C03 20/2/0; C05 7/3/13; **C06 1/37/0**; C07 5/0/1; **C08 7/4/54**; C10 26/0/0; **C09 3/31/0**. So a
census keyed to the filed regex reads C01 as **zero open items** while its `- sources:` block marks
~10 works "**to-verify** for direct reading" (e.g. `C01-entry-1.md:56-60`), and reads C09 as 3 while
it marks 31 items in backticked form. Required: the round's census (and any validator leg) accepts
the backticked/bold forms too, or the drafts normalize to `(to-verify)`. This is a census-integrity
defect, not a sourcing defect — the drafts' honesty is intact; the *measurement* of it is not.

**H4 (positive) — the drafts claim no network act, and carry no web URLs.**
**0 `http(s)` URLs** across all nine landed drafts (the only two URLs anywhere in `cov/` are
`e.org`/`example.invalid` inside C12's fixtures). Sourcing is in-repo `path:line` anchors +
bibliographic works, so §3 R1's URL-freshness risk **does not materialize**. Every landed entry
states the constraint in its own `verified-at:` line: "no external URL was fetched this round …
Nothing here is asserted as fetched" (`C01:9`, `:45`, `:82`), "this draft was written under round-35
with **no network access**" (`C05:82`), "offline seat (no network this round)" (`C06:45`), "no
network ac[cess]" (`C09:65`). The residual unverifiable surface is **bibliographic** (author-year
works: ~14 year-hits in C01, 21 in C06) and is flagged as such.

**H5 (confirms §3 R2 on draft bytes) — the live frontmatter vocabulary is followed, `scope:` is not.**
All 9 landed entries carry `- topic:`, `- sources:`, `- couples:`, `- verified-at:`, `- recheck:`
and `- gap:`/`- gap filled:`. **0 of 9 carry `- scope:`** — so claim C's literal "source / verified-at
/ recheck / scope" 4/4 reading would score **0/9** while the entries are contract-clean under the
filed instrument (`reports/round-19/audit/entry-audit.py:106,108`). The threshold wording must be
corrected before C13/C14/C17's verdicts are read as defects.

**H6 (owed) — self-target paths must resolve after integration.** Each entry names its own future
filename (H-table column 3). If the integrator lands an entry under a different slug, that entry's
own self-citation dangles. Check at close: re-run §2.3 over `corpus/knowledge/{culture-material,myth-symbol}/`
and confirm the nine proposed slugs resolve.

**H7 (informational) — two resolver ambiguities are artifacts, not defects.** `maya-classic.md`
(`C01:203`) and `persia-sasanian.md` (`C06:41`) each match a corpus file **and** a same-named
round-17 fragment (`reports/round-17/civ/…`); the citation intent is unambiguous. A checker that
reports these as ambiguous should be tuned to prefer `corpus/knowledge/**`.

**H8 (low, filed-class defect) — one genuine dangling citation to a filed round path, in C10.**
`C10-entry-10.md:551` cites **`reports/round-28/entry/C41.md:1-40`** as the newest entry-authoring
convention. **That path does not exist**: round 28's C41 fragment lives at
`reports/round-28/ceiling/C41.md` (verified present); `reports/round-27/entry/C41.md` *does* exist,
so the citation carries round-27's directory shape onto round 28. The neighbouring citation on the
same line — `reports/round-28/audit/x63-entry-source-resolvability.md:1-45` — **does** resolve
(file present in `reports/round-28/audit/`). Severity low (an evidence-ledger pointer, not a source
pointer), but this is exactly the class C12's leg 2 is written to block, and it should be filed as a
finding with the corrected path rather than passed: the draft's own honesty claim ("every in-repo
pointer resolves") is falsified on its own bytes at `:551`. Owner: C10's author / integrator
(repoint to `reports/round-28/ceiling/C41.md:1-40`). **This is the only genuine dangling citation
found in 9 hunted drafts (720 in-repo citations total).**

## Owed

- `reports/round-35/cross/X04-honesty.md` (this file) — **the hunt over the remaining draft**:
  `cov/C04-entry-4.md` (not landed at 08:31Z), plus the **post-integration re-run** of §2.3 over the
  landed corpus paths (H6: the nine self-target slugs must resolve; H2: the two corrected paths
  normalized or recorded). `cov/C13-audit-1-5.md` landed at 08:32Z and was read for H2's
  corroboration only — its other findings were **not** independently re-verified by this seat.
  Owner: integrating parent or a post-landing seat. **Until it runs, "the 10 drafts carry no
  unresolvable citation" is established for 9 of 10 only, and H8 stands unfixed.**
- `reports/round-35/cov/C10-entry-10.md:551` — **dangling citation** (`reports/round-28/entry/C41.md`
  → the real path is `reports/round-28/ceiling/C41.md`), H8. Owner: C10's author or integrator; the
  fix is a one-path repoint, and it must be recorded as a filed finding (append-only), never a
  silent edit.
- `reports/round-35/claims.json:24,29` **threshold-wording correction** (R2: `scope:` is not a corpus
  field; the filed contract is `entry-audit.py:106,108`) — owner: integrating parent (append-only
  dossier wording; the declaration file is the integrator's to amend, never a seat's).
- `corpus/README.md` reconciliation must include the **footer leg** (`:471-473`) and the `:469`
  totals line, not only rows/headers (R5) — owner: integrator, with `reports/round-28/readme/sweep.py`
  `footer_ok` read.
- `reports/round-35/telemetry/observed-dispatch.json` (actual route = key 1, launches/completions
  per `AGENTS.md:21-29`) and `reports/round-35/telemetry/availability-close-35.json` (closing
  snapshot, digest-pinned per `AGENTS.md:32-38`) — owner: integrating parent.
- `to-verify` (inherited, must not be closed by round 35): F-C15-1 the "12" numeral
  (`reports/round-33/calib/open-items-ledger.json`); the F-C13-1 writer attribution (`LOG.md:3556`).
- `to-verify` (this seat, unread residue): the 52 unclassified round-34 unresolved citations (§3 R8);
  the 5 unresolved corpus basenames (§2.1); three unprinted detailed-marker files (§1.1).

## Citations

**Files read (read-only):** `reports/round-35/{claims.json,targets.json}`;
`reports/round-35/telemetry/{dispatch-declared,availability-attempt-1,availability-attempt-2,availability-attempt-3}.json`;
`reports/round-35/{adj/A05-records.md,adj/A06-province.md,adj/A09-receipt.md,cov/C11-readme-delta.md,cov/C15-receipt.md,cov/C16-scribe.md,cross/X02-conformance.md,op/O08-validation-legs.md,op/O10-scribe.md,review/R06-a-review.md,scout/K03-keyerror-path.md,scribe/S01-c-receipt.md,scribe/S02-o-receipt.md,scribe/S03-a-receipt.md,scribe/S05-telemetry-draft.md}`;
**§8 drafts (hunted, not authored):** `reports/round-35/cov/{C01-entry-1,C02-entry-2,C03-entry-3,C05-entry-5,C06-entry-6,C07-entry-7,C08-entry-8,C09-entry-9,C10-entry-10}.md`
with `cov/{C12-audit-runbook.md:21,24,37,860,868,915,987,C14-audit-6-10.md:590-592,C17-audit-sample.md}`;
`REGIMEN.md:26-51`; `AGENTS.md:21-38`; `corpus/QUALITY.md:1-14`; `corpus/README.md:1-36,44,57,90,147,169,469,471-473`;
`corpus/knowledge/myth-symbol/flood-traditions.md:18`; `corpus/knowledge/verification/gate-frozen-run-standard.md:5-7,16,66`;
`corpus/knowledge/verification/provenance-audit-ledger-format.md:14`;
`corpus/knowledge/linguistics/{phonetics-phonology.md:279,language-contact.md:7,conlang-methodology.md:146}`;
`corpus/knowledge/verification/header-conformance-readings.md:7,28,137,158`;
`reports/round-19/audit/entry-audit.py:25-27,74-79,105-121`; `reports/round-19/audit/x26-spotcheck-entries.md:1-60`;
`reports/round-19/entries/review-C11.md:60-72,113-117`;
`reports/round-28/readme/sweep.py` (digest only); `reports/round-30/handoff/declared-in-r6/{freeze.txt,packet.md,twin.json}`;
`reports/round-34/handoff/declared-in-r7/packet.md`; `reports/round-33/calib/open-items-ledger.json` (F-C15-1 record);
`reports/round-34/cross/X01-trades.md:11`; `reports/round-34/calib/{C03-anchor-reissue.md:71,351,C09-final-receipt.md:60,134,137}`;
`tools/exercise-handoff-e2e.py:1933-1934`.

**Commands run (all read-only; no round runner, in-tree or in a copy):**
`git rev-parse HEAD` → `4a7aede22cd8395b01ce6dd9f46bcae364ca24e4`; `git status --porcelain` → `?? reports/round-35/`;
`python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → the §1.1 table;
`python3 -B .scratch/x04/honesty-scan.py --root corpus/knowledge [--json --verbose]` → the §2.1 table;
same over `reports/round-{19/entries,33,34,35}` → §1.3/§3 R4/R8;
`for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` → 21/19/18/29/20/94;
`grep -rlE '^- scope:' corpus/knowledge/ | wc -l` → 0; `grep -rlE '^- scope:' corpus/lessons/*.md | wc -l` → 0;
`sha256sum corpus/README.md` → `053966a2…`; `wc -c -l corpus/README.md` → 493 / 106218;
`sed -n '469p;471,473p' corpus/README.md`; `sha256sum reports/round-28/readme/sweep.py` → `9b2ccac0…`;
README-vs-live row/header reconciliation (python, 201 rows = 201 files, 0 missing, 0 ghosts);
r6 freeze pin re-hash (packet 6ced88ad…, twin 6633443d… — MATCH); r7 packet re-hash → `45f57132…`;
`grep -n "V3_BASELINE_DEFAULT\|V3_FROZEN_DIR_DEFAULT" tools/exercise-handoff-e2e.py` → `:1933-1934`;
`grep -c 'to-verify'` over the 11 policy surfaces → the §1.2 table; `date -u +%FT%TZ` → `2026-10-19T08:21:21Z`.
