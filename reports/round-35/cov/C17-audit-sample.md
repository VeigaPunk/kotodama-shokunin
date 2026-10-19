- Seat: C17 | verifier (third independent entry auditor) | claim C | date 2026-10-19 | baseline 4a7aede

# C17 — third independent entry auditor: pre-registered contract, before-state pins, README-delta instrument, and the sample lot

NON-CANON engineering evidence. This audit admits no entry, certifies no round,
blesses no source, and decides no canon. Writes: **this file only**.

## 0. Status, lot choice, and independence posture

- Mission (verbatim, `reports/round-35/targets.json:180`): "Third independent
  entry auditor: re-audit any 3 of the 10 drafts chosen by lot (odds 1,4,7 /
  evens 2,6,10 — your choice, state it) plus the README delta numbers; defects
  filed." Out path `reports/round-35/targets.json:181`.
- **Lot choice: EVENS — entry 2, entry 6, entry 10**, i.e. the drafts owed at
  `reports/round-35/cov/C02-entry-2.md`, `cov/C06-entry-6.md`,
  `cov/C10-entry-10.md`.
- **Anti-cherry-pick evidence.** The choice was fixed at 2026-10-19 before any
  draft existed. At that stamp `find reports/round-35 -type f` returned exactly
  six files — `claims.json`, `targets.json`, `telemetry/availability-attempt-{1,2,3}.json`,
  `telemetry/dispatch-declared.json` — and no `cov/` directory at all. The lot
  was therefore drawn against nothing but the mission's own enumeration, and no
  substitution is permitted after the drafts land.
- **Independence posture (who is independent of whom).** I authored none of the
  ten drafts, none of `cov/C11-readme-delta.md`, none of `cov/C12-audit-runbook.md`,
  and I am neither C13 (entries 1–5) nor C14 (entries 6–10). I derived the audit
  contract from the lane's own instruments and the corpus, **not** from C12's
  runbook — so a defect in C12 cannot propagate into this pass. Where I did read
  another seat's product I name it (the round-19 audit fragment, §3 L4/L5 below).
- **What this seat could not do** is in §6. Two of my four named inputs landed
  while this pass ran — `cov/C02-entry-2.md` (05:21) and `cov/C11-readme-delta.md`
  (05:22) — and are audited in §7; entries 6 and 10 were still absent at this
  stamp and remain owed (§Owed).

## 1. The entry-shape contract, derived independently

### 1.1 The contract's authorities (cited, not invented)

| leg | authority |
|---|---|
| header fields | `reports/round-10/run-validation.py:81-82` — `C_FRONTMATTER_FIELDS = ("topic","sources","verified-at","recheck","couples")` |
| named gap | `reports/round-10/run-validation.py:363-367` (frontmatter gap field **or** body heading naming the gap) |
| decision record | `reports/round-10/run-validation.py:368-370` (`^#{2,4}…decision[- ]record…` + one non-blank line) |
| retrievable locator | `reports/round-10/run-validation.py:372-376` (existing repo path or URL) |
| README legs | `reports/round-10/run-validation.py:459-477` (heading count == files, rows == files, no ghosts, totals line == files) |
| inventory leg | `reports/round-10/run-validation.py:485-488` (inventory total == files on disk) |
| admission bar | `corpus/QUALITY.md:3-20` (provenance / calibration / coupling / usability / canon hygiene) |
| fleet sentence | `corpus/README.md:376-378` — "Most historical entries lack the fleet's complete `source`, `verified-at`, `recheck` header. The existing provenance gate checks the older topic/sources/couples profile, not full corpus conformance." |
| reading-id discipline | `corpus/knowledge/verification/header-conformance-readings.md:3,88,101,149` — a header count may not circulate without its reading id; `corpus/README.md:454-456` keeps fleet header conformance an open integrator question |

### 1.2 Measured header census at HEAD 4a7aede (2026-10-19)

Command (repo root): `for f in topic sources couples verified-at recheck source scope; do grep -rlE -- "^- $f:" corpus/knowledge/*/*.md | wc -l; done`

| field | files carrying it (of 201) |
|---|---|
| `- topic:` | 201 |
| `- sources:` (plural) | 201 |
| `- couples:` | 201 |
| `- verified-at:` | 201 |
| `- recheck:` | 201 |
| `- source:` (singular locator line) | 134 |
| `- scope:` | **0** |
| `- gap filled:` / `- gap:` | 13 / 2 |

All five lane fields are carried by **201/201** files (script reading: per-file
regex over `corpus/knowledge/*/*.md`, "files: 201 | all five lane fields: 201 |
files missing a lane field: 0").

### 1.3 Finding C17-1 — the declared frontmatter set is unsatisfiable (severity: blocking for the audit leg as written)

`reports/round-35/claims.json:25` declares each new entry
"frontmatter-complete (**source / verified-at / recheck / scope**)", and
`claims.json:29` requires "frontmatter 4/4 or documented 3/4 class".

- `- scope:` is carried by **0 of 201** existing entries. A 4/4 reading that
  includes `scope` cannot be met by any entry, old or new.
- `- source:` (singular) is carried by **134 of 201**; the corpus's own header
  profile uses plural `- sources:` (201/201) plus, in the newer round-10+ style,
  an optional singular locator line. So even the 3/4 subset
  (`source`/`verified-at`/`recheck`) is not universal: 67 entries lack the
  singular line.
- **Recommended operational reading** for round 35 (for C13/C14/C15/S04 and the
  validator author): audit against the lane profile
  `topic`/`sources`/`couples`/`verified-at`/`recheck` = **5/5**, and report the
  declared 4-field set separately as a *declaration* reading with the counts
  above. Do **not** silently reinterpret "4/4" — per
  `header-conformance-readings.md:88`, an unlabeled header count is false under
  at least one defensible reading.
- Owner: integrator (declaration defect in `claims.json`, which is filed round-35
  bytes and is not mine to edit).

### 1.4 Finding C17-2 — "documented 3/4 class" is undefined anywhere in the lane (severity: threshold defect)

`claims.json:29` and `claims.json:35` ("10/10 new entries audited clean (two
independent auditors)") make the accept condition depend on a class that no
artifact defines: what makes an entry "documented 3/4", who documents it, and
what evidence discharges it.

- Command: `grep -rn "frontmatter 4/4\|3/4 class" --include=*.md --include=*.json --include=*.py . | grep -v '^./reports/round-35/' | grep -v '^./.git/' | wc -l` → **0**.
  (The 45 loose `4/4` hits elsewhere in the repo are verifier-set counts, HTTP
  sample counts and control counts — none is a frontmatter class.)
- Consequence: any auditor may mark any entry "documented 3/4 class" and the
  threshold still reads clean; the claim's audit leg is unfalsifiable as written.
- **Recommended discharge condition** (so the leg can fail): an entry is
  "3/4-class" only if the missing field is named, the reason is stated in-file,
  and the reason is *re-checkable* (a path or command). A missing field with no
  such note is a defect, not a class.
- Owner: integrator (claims/threshold wording); the auditor applying it is me
  (C13/C14 too).

### 1.5 Finding C17-3 — the README-delta spec must name the footer and revision legs, or the filed sweep fails the landing (severity: landing-blocking if omitted)

`claims.json:29` asks only that "partition counts and index rows" be reconciled.
The README's own instrument of record enforces more, and the claim's own
counting command list (`claims.json:31-34`) does not name it.

- `reports/round-28/readme/sweep.py:164-189` fails the sweep (`ok=false`,
  exit 1) on `FOOTER_ABSENT`, `FOOTER_TOTAL`, `FOOTER_DIR_TOTALS`, in addition to
  heading/row/totals drift (`sweep.py:191-194`). The counts footer is a
  **present-tense** claim — the round-28 revision 1.8 exists precisely because a
  landing moved the totals line and left the footer stale (`corpus/README.md:17-35`).
- The README revision convention (`corpus/README.md:3-15`) requires a **new**
  revision block per landing, with earlier blocks and the
  "Superseded reading, preserved as the dated record it was" paragraph
  (`corpus/README.md:476-481`) left untouched; and the new row must carry the
  entry's own `- topic:` text (`corpus/README.md:6-7`, revision 1.9's wording).
- **Pre-registered delta spec** for the landing (see §4 for the runnable check):
  `## myth-symbol/ (19→23)`, `## culture-material/ (18→24)`,
  `Total knowledge entries: 201→211`, footer `(total 201→211 files; directory
  totals 21/19/18/29/20/94 → 21/23/24/29/20/94)` — directory order is section
  order (`sweep.py:180-181`), so the vector is **21/23/24/29/20/94**, not sorted.
- Owner: integrator / `cov/C11-readme-delta.md`.

## 2. Before-state pins (every reading re-runnable, all at HEAD 4a7aede)

| reading | command | observed |
|---|---|---|
| partition census | `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md \| wc -l; done` | 21 / 19 / 18 / 29 / 20 / 94 = **201** |
| inventory | `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` | exit 0, `totals.files 201`, `files_with_marker 135`, `lines 36395` |
| README census (mine) | `.scratch/c17/row_audit.py .` (§4 recipe) | rows == files per section 21/19/18/29/20/94; 0 missing; 0 ghosts; **topic byte-equal 201/201, 0 mismatches** |
| README census (filed) | `python3 -B reports/round-28/readme/sweep.py` in an isolated `git archive` copy | `rows 201 files 201`, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`, `totals_line 201 totals_ok True`, `footer_ok True`, exit 0 |
| filed sweep controls | `python3 -B reports/round-28/readme/sweep.py --selftest` (isolated copy) | **12/12 checks passed**, exit 0 |
| README digest | `sha256sum corpus/README.md` | `053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c` |
| expected after-state | arithmetic from `claims.json:24,29` | myth-symbol 19→23, culture-material 18→24, **total 211**, vector **21/23/24/29/20/94** |

Anchors for the delta (line numbers at HEAD, for the diff leg):
`corpus/README.md:123` `## linguistics/ (21)`, `:147` `## myth-symbol/ (19)`,
`:169` `## culture-material/ (18)`, `:190` synthesis, `:222` verification,
`:245` civilizations, `:469` totals line, `:471-473` counts footer,
`:3-15` revision 1.9 block.

### 2.1 Self-caught instrument artifact (honesty record, not a finding)

My first row comparator reported **2 topic mismatches**
(`linguistics/numerals-and-measures.md`, `linguistics/phonetics-phonology.md`).
Both were **my instrument's defect**, in two successive forms: a first-line-only
extractor (truncating multi-line `- topic:` fields) and then an over-capturing
stop rule that swallowed following fields. The lane's declared semantics are
`reports/round-28/readme/sweep.py:61,74-82` (the `- topic:` head block,
continuation lines space-joined) and the filed sweep reads **0** mismatches on
the same tree. Corrected reader: **201/201 byte-equal**, agreeing with the filed
sweep on both the live tree and the isolated copy. Recorded because the
false-positive class is exactly the one
`corpus/knowledge/verification/verification-independence-anti-circularity.md:242`
names (regex false positives) — an audit instrument that fires on the wrong
thing is evidence against the auditor, not the artifact.

## 3. Pre-registered audit legs for the sampled drafts (entries 2, 6, 10)

Registered now, before the bytes exist, so the post-landing pass cannot drift to
whatever the drafts happen to satisfy. Each leg reports an observed result and
every defect is severity-ranked (blocking / major / minor / note).

- **L1 header** — the five lane fields present, quoted with line numbers; the
  declared set (`source`/`verified-at`/`recheck`/`scope`) reported separately
  under finding C17-1's reading, never silently folded together.
- **L2 gap** — round-10 gap detection (`run-validation.py:363-367`) **plus** the
  stronger filler test (`reports/round-19/audit/x26-spotcheck-entries.md:133-147`):
  the gap must name what the partition lacked, not merely use the word.
- **L3 decision record** — a `## … decision record …` section with content
  (`run-validation.py:368-370`), read, not just matched.
- **L4 locator resolution** — every `corpus|tools|reports|examples/…` path the
  draft cites is tested with `test -e`; every URL token is well-formed and
  carries the draft's own `web-checked` stamp. **Limit: this seat has no network
  access**, so URLs are not re-fetched — the leg is presence + form + stamp, and
  I will say so rather than imply a fetch.
- **L5 couples resolution** — brace-aware, resolved against the entry directory,
  the lane root, and `corpus/knowledge/` (the three bases
  `reports/round-19/audit/x26-spotcheck-entries.md:39-45` describes), so a
  phantom path of the X26-1 class is caught.
- **L6 no-bleed language** — scan for promotion / canon / clearance / closure /
  verdict language outside negations, and for any sibling-path or
  `lore-shokunin`-owned assertion (`corpus/QUALITY.md:18-20`; the same discipline
  claim A audits, applied to C drafts).
- **L7 topic byte-equality after landing** — the landed README row for each of
  the three entries compared to the entry's own joined `- topic:` value (§4
  recipe). This is the leg the third pass adds beyond C13/C14's entry-only slices.
- **L8 no fabrication** — every citation either resolves (path or well-formed
  URL + stamp) or is marked `(to-verify)` in-file; an unresolvable citation that
  is *not* marked is a blocking defect (`corpus/QUALITY.md:6-8`,
  `claims.json:29`).
- **L9 duplication** — the draft's domain checked against the 201 existing
  entries' slugs/topics for a restatement of an existing file (the corpus's own
  "nearest neighbours are extended, never restated" rule,
  `corpus/knowledge/linguistics/register-lexicon-ceilings.md:5`).

## 4. README-delta auditor (pre-registered, with controls)

Legs D1–D6: new-row counts (+6 culture-material, +4 myth-symbol) and file
existence; row text byte-equal to the entry's joined `- topic:` value; per-section
filename order; heading counts == live file counts and totals line == live total;
footer total + directory vector (section order) == live counts; and a line-level
diff leg that fails on any replaced/deleted line outside {new revision block,
headings, totals, footer count lines, new index rows}.

**Controls, run 2026-10-19 on synthetic fixtures under `.scratch/c17/fix/`:**

| fixture | planted condition | observed |
|---|---|---|
| `post_ok.md` | correct landing (10 new rows, headings, totals, footer, revision block) | `VERDICT: PASS`, **exit 0** |
| `post_bad.md` | one paraphrased new row + totals line left at 201 | `VERDICT: FAIL`, **exit 1** — D2 (row 20c vs topic 28c), D4 (totals 201 != live 211) |
| `post_bad2.md` | `## myth-symbol/ (23)` reverted to `(19)` | `VERDICT: FAIL`, **exit 1** — D4 (heading declares 19, 23 files) |

A first control run also surfaced a **D6 false positive on blank-line
reshuffling**; the allowed-line pattern now admits blank lines and the clean
fixture reads PASS. Recorded rather than hidden: the leg's calibration is part of
its evidence.

Integrator: apply the block below to a durable path of your choosing (suggested
`reports/round-35/cov/C17-readme-delta.py`) and run it **after** the landing:

```python
#!/usr/bin/env python3
"""C17 README-delta auditor (read-only). Usage:
  python3 reports/round-35/cov/C17-readme-delta.py --pre <pre-README> --post <post-README> --tree <root>
Pre-README = git show HEAD:corpus/README.md (baseline 4a7aede)."""
import argparse, re, sys, difflib
from pathlib import Path
PARTS = ("linguistics","myth-symbol","culture-material","synthesis","verification","civilizations")
SEC = re.compile(r"^## ([a-z-]+)/ \((\d+)\)\s*$", re.M)
ROW = re.compile(r"^- `([^`]+\.md)` — (.*)$", re.M)
TOP = re.compile(r"^- topic:(.*?)(?=\n- \w)", re.M | re.S)
TOT = re.compile(r"^Total knowledge entries: (\d+)\.\s*$", re.M)
FOOT = re.compile(r"^Counts checked (\d{4}-\d{2}-\d{2}) from the repo root:\n`([^`]+)`\n"
                  r"\(total (\d+) files; directory totals ([\d/]+)\)\.", re.M)

def sections(text):
    marks = [(m.start(), m.group(1), int(m.group(2))) for m in SEC.finditer(text)]
    out = {}
    for i, (pos, part, decl) in enumerate(marks):
        if part not in PARTS: continue
        end = marks[i+1][0] if i+1 < len(marks) else len(text)
        out[part] = {"declared": decl, "rows": ROW.findall(text[pos:end])}
    return out

def topic_of(p):
    m = TOP.search(p.read_text(encoding="utf-8"))
    if not m: return None
    return " ".join(x for x in (l.strip() for l in m.group(1).strip("\n").splitlines()) if x)

ap = argparse.ArgumentParser()
ap.add_argument("--pre", required=True); ap.add_argument("--post", required=True); ap.add_argument("--tree", required=True)
a = ap.parse_args()
root = Path(a.tree)
pre = Path(a.pre).read_text(encoding="utf-8"); post = Path(a.post).read_text(encoding="utf-8")
S_pre, S_post = sections(pre), sections(post)
fail = []
for part in PARTS:
    live = sorted(p.name for p in (root/"corpus/knowledge"/part).glob("*.md")) if (root/"corpus/knowledge"/part).is_dir() else []
    d = S_post[part]["declared"]
    if d != len(live): fail.append(f"D4 heading {part}: declares {d}, {len(live)} files")
    names = [n for n, _ in S_post[part]["rows"]]
    if names != sorted(names): fail.append(f"D3 {part}: rows not in filename order")
    if set(names) != set(live): fail.append(f"D4 {part}: rows {len(names)} vs files {len(live)}")
    pre_names = [n for n, _ in S_pre[part]["rows"]]
    new = [(n, t) for n, t in S_post[part]["rows"] if n not in pre_names]
    print(f"{part}: {len(pre_names)} -> {len(names)} rows ({len(new)} new)")
    for n, t in new:
        f = root/"corpus/knowledge"/part/n
        if not f.is_file(): fail.append(f"D1 new row {part}/{n}: no such file"); continue
        real = topic_of(f)
        if real is None: fail.append(f"D2 {part}/{n}: entry carries no `- topic:` field")
        elif t != real: fail.append(f"D2 {part}/{n}: row NOT byte-equal to topic (row {len(t)}c / topic {len(real)}c)")
tot = TOT.search(post)
live_total = sum(len(list((root/'corpus/knowledge'/p).glob('*.md'))) for p in PARTS)
if not tot or int(tot.group(1)) != live_total:
    fail.append(f"D4 totals line {tot.group(1) if tot else None} != live {live_total}")
f = FOOT.search(post)
if not f: fail.append("D5 footer absent")
else:
    vec = [int(x) for x in f.group(4).split("/")]
    live_vec = [len(list((root/'corpus/knowledge'/p).glob('*.md'))) for p in PARTS]
    if int(f.group(3)) != live_total or vec != live_vec:
        fail.append(f"D5 footer total {f.group(3)}/{f.group(4)} != live {live_total}/{live_vec}")
pre_lines = pre.splitlines(); post_lines = post.splitlines()
allowed = re.compile(r"^(|revision: |## [a-z-]+/ \(\d+\)$|Total knowledge entries: \d+\.$|Counts checked "
                     r"|`python3 tools/source-audit-inventory|\(total \d+ files; directory totals"
                     r"|The inventory counts markers|- `[^`]+\.md` — )")
replaced, deleted = [], []
for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, pre_lines, post_lines, autojunk=False).get_opcodes():
    if tag in ("replace", "delete"):
        for ln in pre_lines[i1:i2]:
            if not allowed.match(ln):
                (replaced if tag == "replace" else deleted).append(ln[:90])
if replaced: fail.append(f"D6 {len(replaced)} replaced line(s) outside the allowed set: {replaced[:3]}")
if deleted: fail.append(f"D6 {len(deleted)} deleted line(s) outside the allowed set: {deleted[:3]}")
print("live total:", live_total, "| footer:", f.groups() if f else None)
print("VERDICT:", "PASS" if not fail else "FAIL")
for x in fail: print("  -", x)
sys.exit(0 if not fail else 1)
```

Expected reading for the real landing, if all legs hold:
`myth-symbol: 19 -> 23 rows (4 new)`, `culture-material: 18 -> 24 rows (6 new)`,
the other four sections `(0 new)`, `live total: 211`, footer
`(…, '211', '21/23/24/29/20/94')`, `VERDICT: PASS`, exit 0.

## 5. What C17 will run when the drafts land

For each of entries 2, 6, 10: legs L1–L9 with observed results and severity-ranked
defects; then the §4 delta auditor against the landed README with the pre-README
taken from `git show 4a7aede:corpus/README.md`. If a draft is missing, the
missing path is recorded and the rest still runs — the same missing-dependency
rule this fragment itself follows.

## 6. Limits

- **No network.** URL citations in the drafts are checked for presence,
  well-formedness and the draft's own `web-checked` stamp; they are **not**
  re-fetched. Any claim that depends on a fetched body is therefore
  unverifiable *by this seat* and will be reported as such, not as clean.
- **Two of four inputs landed mid-pass** and are audited in §7; entries 6 and 10
  were still absent at this stamp (see §Owed).
- The instruments in `.scratch/c17/` are not durable. Their semantics and the
  delta auditor are reproduced in this fragment; the row-census recipe is
  `reports/round-28/readme/sweep.py`'s own (cited) plus the direction
  classifier described in §2.
- This audit reads structure, resolution and language. It does not judge whether
  a draft's history is right, and it decides no canon (`corpus/QUALITY.md:18-20`).

## 7. Audit of the inputs that landed during this pass

**Byte pins.** Audited at `cov/C02-entry-2.md` sha256
`bff366523d7c9efb86cd2a4defb89d457f95f77007a89641b291de7181615797` and
`cov/C11-readme-delta.md` sha256
`5ae025606506596100bba2b4067041e6d02cd1072e3e4a94f436a05b4d712d59` (both
2026-10-19). C02 revised its own fragment during this pass (its `(to-verify)`
count moved 21 → "11 lines / 12 occurrences"); every reading below is against the
digest above, and a later revision needs a re-run, not an inheritance.

### 7.1 Entry 2 (`cov/C02-entry-2.md`) — legs L1–L9, all run

| leg | observed | verdict |
|---|---|---|
| L1 header | 7 fields present (`topic`, `sources`, `couples`, `verified-at`, `recheck`, `gap`, `source`); five lane fields **5/5** | pass |
| L2 gap | `- gap:` present and names what the partition lacked ("absent from culture-material … no entry owns the field system itself") | pass |
| L3 decision record | `## 11. Decision record` with 10 `DR-AG-nn` rows; round-10 regex (`run-validation.py:368-370`) fires | pass |
| L4 locators | **28 cited `path:line` anchors re-derived independently** (own resolver, own keyword expectations): 26 exact. The 2 flagged are the *endpoints* of the range citation `austronesia-philippines-taiwan.md:109-126`, whose content sits at `:111-117` (`muyong`/`uma`/`payo`) — citation correct, my endpoint test too strict. 0 URLs; 12 `(to-verify)` occurrences on 11 lines, matching C02's corrected count exactly | pass |
| L5 couples | 22 unique `.md` targets, **0 unresolved**: 20 dir-shaped + 2 bare (`AGENTS.md`, bare `textile-technology.md`). A resolver must handle the bare class — C02's 22 is the complete count; my first reading (20) was my regex's narrower token class | pass |
| L6 bleed | no promotion / canon / clearance / closure language; the single hit was my regex firing on "cleared by fire" (agricultural sense) | pass |
| L7 topic shape | `- topic:` is one 1127-char line, so a README row **can** be byte-equal (`sweep.py:140`); the integrator must emit it from a generator, never paraphrase | pass |
| L8 fabrication | every external work carries `(to-verify)`; no unflagged external figure found in the claims I could re-derive | pass |
| L9 duplication | C02's §1 census **re-derived independently: 19/19 numbers identical** (three-field 0 … Hesiod 8); no existing partition file owns the field-system register | pass |

**Defects against entry 2: none.** Two integrator notes: (i) the row text for
`corpus/knowledge/culture-material/agrarian-field-system-lexicon.md` must be the
full 1127-char topic line; (ii) C02's own finding 1 is **confirmed** by me —
`corpus/knowledge/culture-material/transport-mobility-lexicon.md:3` reads
"… — this entry fills it", and the round-19 `GAP_RE`
(`reports/round-19/audit/entry-audit.py:26`: `residual gap|gap filled|the gap
this entry fills|known gaps|missing from|no entry (?:covers|states)|not covered
by`) does not match that phrasing, so an auditor applying `GAP_RE` alone would
fail the filed round-34 entry. The round-35 audit should accept a `- gap:` field
as the contract, as the round-10 runner does (`run-validation.py:363-367`).

### 7.2 README delta (`cov/C11-readme-delta.md`) — the numbers, checked

| check | observed |
|---|---|
| pinned README digest | `053966a2…` — matches my own pin, and the file's 493-line length exactly |
| line map | verified line by line: `:3` revision 1.9 block start; `:147` `## myth-symbol/ (19)`; rows `:149-167` (19); `:169` `## culture-material/ (18)`; rows `:171-188` (18); `:469` totals; `:471-473` footer; `:475-480` superseded paragraph; `:482-493` dated index paragraphs |
| E2/E3/E4/E5 before-blocks | all five before-patterns present exactly once → byte-exact against the pin |
| delta arithmetic | totals 201→211; footer `21/19/18/29/20/94 → 21/23/24/29/20/94` (section order); headers 19→23 and 18→24 — **identical to my independent computation** |
| row-count command | `grep -c '^- \`[A-Za-z0-9._-]*\.md\`' corpus/README.md` → **201** today, calibrated for 211 |
| generator, live tree | no-op as designed: rows==files in all six sections, `ghosts []`, totals/footer before==after, digest `053966a2…` |
| generator, my own fixture | cross-instrument: C11's generator applied to **my** synthetic +10 tree emitted the 10 rows with correct anchors, totals 211, footer `21/23/24/29/20/94`; **my** delta auditor then read that output `VERDICT: PASS`, exit 0 |
| cross-surface claim | `git grep -ln '^Total knowledge entries: ' -- .` → **exactly `corpus/README.md`** in the tracked tree — C11's claim holds |
| LOG.md leg of that claim | **not reproducible** → finding C17-4 |

**Finding C17-4 (minor).** C11 states "Live surfaces carrying the 201 count
today: `corpus/README.md:469,473` and `LOG.md`". The LOG.md half does not
reproduce: `git grep -n '201 files\|201 entries\|201 rows\|total 201' -- LOG.md`
→ **0 matches**; LOG.md's only census-shaped line is the historical round-10
entry `LOG.md:2993` ("179 → 189 knowledge entries"). Impact is low — the parent
could go looking for a LOG count surface that does not exist — but it matters
because LOG.md is append-only and a phantom count surface is exactly what a later
auditor chases. Owner: integrator / C11 (wording only; no byte change needed).

### 7.3 Two-reader agreement ledger

| reading | C02 / C11 | C17 | resolution |
|---|---|---|---|
| `(to-verify)` marks | 11 lines / 12 occurrences (C02, after self-correcting a first-draft 21) | 11 lines / 12 occurrences | **agree** |
| couples targets | 22 (C02) | 20 first pass → 22 after token-class alignment | **agree — C02 was right** |
| README delta numbers | 211 / 21/23/24/29/20/94 | same, computed independently | **agree** |
| README rows vs `- topic:` | 0 mismatches | 0 mismatches (filed sweep + my reader, two trees) | **agree** |

### 7.4 Entry 6 (`cov/C06-entry-6.md`) — legs L1–L9, run on the 3-backtick draft block

Byte pins: fragment sha256 `5558ace843c00315c8cbbf43e598b0b003a767563622c27ef988dc51d01eb05d`;
extracted entry block **47,669 bytes** — matching C06's own stated byte count exactly
(my extraction counts 173 lines where C06 states 174; a trailing-newline counting
convention, not a content difference).

| leg | observed | verdict |
|---|---|---|
| L1 header | seven fields present (`topic`, `sources`, `couples`, `verified-at`, `recheck`, `gap`, `source`); five lane fields **5/5** | pass |
| L2 gap | `- gap:` names the partition hole (fire/fuel/light register absent; the four neighbours that come closest are each named with a `path:line`) | pass |
| L3 decision record | decision-record section present, 7 `DR-` rows; round-10 regex fires | pass |
| L4 locators | **32 unique in-repo `path:line` refs, all resolving, all in bounds**; each cited line read and its content matches the claim it carries (heating lexicon, forge deities, energy/fuel row, hearth-threshold rows, Aztec New Fire, lamp vocabulary, …) | pass |
| L5 couples | 44 unique `.md` targets, **all dir-shaped, 0 unresolved** | pass |
| L6 bleed | the only hit is a **negation** — "No admission, no promotion, no canon." (line 19) → pass, and a reminder that a bleed scanner must exclude negated forms | pass |
| L7 topic shape | `- topic:` one 1215-char line → row can be byte-equal | pass |
| L8 fabrication | 0 URLs (offline seat, declared); external works cited with author + year + standard edition (QUALITY.md:6's checkable-source bar); `verified-at:` states globally that external works were **not** re-fetched, and `recheck:` names exactly what must be re-verified before use | pass, with C17-5 |
| L9 duplication | its gap sweep names the three nearest files and the zero-hit classes; proposed landing path `corpus/knowledge/culture-material/fire-fuel-light.md` collides with no existing slug | pass |

**Defects against entry 6: none.** **Finding C17-5 (minor, filed here — §8's table
predates it): flag-granularity variance across the ten drafts.** Entry 6 carries
**1** inline `(to-verify)` mark on 1 line (the O'Dea edition) and discloses the
un-fetched status of all eleven external works in `verified-at:`; entry 2 carries
**12** occurrences on 11 lines, flagging each work inline. Both satisfy
`corpus/QUALITY.md:6-8` (a checkable citation *and* a disclosed unverified leg), so
neither is a defect — but an auditor who counts inline marks as a proxy for
provenance discipline would rank the two drafts differently on a difference that
is house style, not evidence. Recommended: auditors judge the *pair* (checkable
citation + disclosure), and the integrator may align the ten drafts' flag
granularity in one pass. Owner: integrator / C12 (runbook wording).

### 7.5 Entry 10 (`cov/C10-entry-10.md`) — legs L1–L9, run on the 4-backtick draft block

Byte pins: fragment sha256 `02eca884edd458f4e61cadccb3a25cf34b51e5010bcceb0e2b1396f70f2abf39`;
extracted entry block **74,529 bytes / 306 lines**. Intended landing path
`corpus/knowledge/myth-symbol/binding-speech-complex.md` (collides with no existing slug).

| leg | observed | verdict |
|---|---|---|
| L1 header | five lane fields **5/5** (`topic`, `sources`, `couples`, `verified-at`, `recheck`) plus `source`; **no `- gap:` field** — it uses `- gap filled:` instead | pass, see L2 |
| L2 gap | `- gap filled:` (line 3) names the hole substantively ("no entry owns the binding-speech complex itself") **and** the body carries `## 1. The gap this entry fills — and the boundary it keeps`; the round-10 contract accepts either (`run-validation.py:363-367`), and the round-19 `GAP_RE` matches the phrase `gap filled` | pass |
| L3 decision record | decision-record section present, 12 `DR-` rows; round-10 regex fires | pass |
| L4 locators | **30 unique in-repo `path:line` refs; 29 in-bounds**, 0 out-of-range. The 1 flag (`QUALITY.md:5`) was **my resolver's base limitation** — the file is `corpus/QUALITY.md`, and `corpus/QUALITY.md:5` is the provenance bar as cited. 0 URLs | pass |
| L5 couples | **40 unique targets; my first reading said 40/40 unresolved — that was my resolver's bug.** Entry 10 writes targets as relative paths (`../civilizations/celts.md`), which resolve from the entry's own directory; under the round-19 three-base resolver (entry dir, lane root, `corpus/knowledge/`) **40/40 resolve, 0 unresolved** | pass — **false alarm withdrawn** |
| L6 bleed | 3 regex hits, all non-bleed senses: "the god's verdict presumed" (ordeal procedure), "the three **canonical** moves" (standard moves of a tale type), "not a verdict" (negation). No promotion / canon-decision / clearance / closure language | pass, with a wording note |
| L7 topic shape | `- topic:` one **1631-char** line → row can be byte-equal | pass |
| L8 fabrication | 5 `(to-verify)` occurrences on 4 lines in a 74.5 KB entry; `verified-at:` states the pass and the anchor re-checks; `recheck:` names exactly what must be re-derived before use | pass, with C17-5 extended |
| L9 duplication | the gap line names the three nearest files and what each owns instead (reading side, register side, the oath-forms hook); no existing file owns the binding-speech complex | pass |

**Defects against entry 10: none.** Notes for the integrator: (i) the row text is
a 1631-char line — emit it from a generator; (ii) **flag granularity** — entry 10
carries 5 inline `(to-verify)` marks in 74.5 KB where entry 2 carries 12 in 36.6 KB;
finding **C17-5** (§7.4) covers the whole set, and no draft should be ranked on it;
(iii) the word "canonical" in §7.5's L6 list is used in the tale-type sense — if the
integrator wants a bleed scanner to run clean over the ten entries, "standard moves"
is the safer wording, but it is not a defect today.

**Method note (filed because it is the lesson, not the artifact):** two of my own
readings in this pass were wrong before they were right — the topic comparator (§2.1)
and entry 10's couples resolver. Both were caught by comparing against the lane's
declared semantics (`sweep.py:74-82`; `x26-spotcheck-entries.md:39-45`) rather than
by trusting my first instrument. A third auditor's false positive is the same class
of hazard as a planted green, and it is recorded here so the integrator can weight
my "0 defects" readings by how they were produced.

## 8. Findings summary (this seat)

| id | severity | finding | owner |
|---|---|---|---|
| C17-1 | blocking for the audit leg as written | declared frontmatter set (`source`/`verified-at`/`recheck`/`scope`) unsatisfiable — `- scope:` 0/201, `- source:` 134/201; use the 5-field lane profile | integrator |
| C17-2 | threshold defect | "documented 3/4 class" is undefined anywhere in the repo → the claim's audit leg is unfalsifiable as written | integrator |
| C17-3 | landing-blocking if omitted | the README delta must carry the footer + revision legs `sweep.py:164-189` enforces, not only counts and rows | integrator / C11 |
| C17-4 | minor | C11's LOG.md "201 count surface" claim does not reproduce (0 count-shaped matches) | integrator / C11 |
| C17-5 | minor | inline `(to-verify)` flag granularity varies 5–12 marks across the drafts; not a provenance defect under QUALITY.md:6-8, but not a ranking signal either | integrator / C12 |
| — | none | **entries 2, 6, 10: 0 defects each** across L1–L9; README delta: 0 numeric defects | — |

§7's new citations: `reports/round-19/audit/entry-audit.py:26` (GAP_RE, read
only); `corpus/knowledge/culture-material/transport-mobility-lexicon.md:3`;
`corpus/knowledge/civilizations/austronesia-philippines-taiwan.md:111-117`;
`corpus/QUALITY.md:5`; `reports/round-35/cov/C02-entry-2.md`,
`cov/C06-entry-6.md`, `cov/C10-entry-10.md`, `cov/C11-readme-delta.md` (sha256s in
§7.1/§7.4/§7.5 and below); `LOG.md:2993`. §7's new commands: the anchor
re-derivation loops (28 + 32 + 30 `path:line` assertions); `sha256sum` over the
four audited fragments; the couples token censuses (22 / 44 / 40 targets) under the
three-base resolver; `git grep -n '201 files\|201 entries\|201 rows\|total 201' --
LOG.md` → 0; `git grep -ln '^Total knowledge entries: ' -- .` → `corpus/README.md`;
C11's generator extracted from its fenced block and run (a) on the live tree
(no-op) and (b) `--apply` onto my fixture tree; my §4 auditor on the result.

## Owed

- **All three sampled drafts are audited** (§7.1 entry 2, §7.4 entry 6, §7.5 entry
  10), each with 0 defects across legs L1–L9. Nothing on the sample remains owed.
- The landed `corpus/README.md` plus the ten applied entries — the §4 auditor's
  real-tree run is owed after the integrator applies C11 (expected reading in §4).
  For that run: entry 2's row text is 1127 chars, entry 6's 1215, entry 10's 1631 —
  all single-line, all to be emitted from a generator, never retyped.
- `reports/round-35/cov/C13-audit-1-5.md` — absent at this stamp; the
  agreement/disagreement comparison against it (and against C14, which landed) is
  owed so the claim's "two independent auditors" count can be read honestly.
- Finding **C17-5** is filed in §7.4 and extended in §7.5; §8's table now carries it.

## Citations

Paths (all read at HEAD `4a7aede`, 2026-10-19):

- `reports/round-35/targets.json:176-182` (seat C17 mission and out path); `reports/round-35/claims.json:8,22-35,60-64` (baseline, claim C, claim A language rule)
- `REGIMEN.md:25-50,52-58` (per-round contract, done-when)
- `reports/round-10/run-validation.py:81-82,363-376,459-488,1018-1020` (the entry-audit contract)
- `reports/round-28/readme/sweep.py:61,74-82,136-148,164-194,239-289,415-431` (README instrument of record + selftest)
- `reports/round-19/audit/x26-spotcheck-entries.md:39-45,74-93,133-147` (couples resolution bases; X26-1 phantom-path class; filler test)
- `corpus/QUALITY.md:3-20` (admission bar)
- `corpus/README.md:3-15,17-35,123,147,169,190,222,245,376-378,454-456,469,471-481,482-493`
- `corpus/knowledge/verification/header-conformance-readings.md:3,7,67,88,101,149`
- `corpus/knowledge/verification/verification-independence-anti-circularity.md:242`
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:5` (extend, never restate)
- `corpus/knowledge/linguistics/numerals-and-measures.md:3`, `corpus/knowledge/linguistics/phonetics-phonology.md:3` (the two probe `- topic:` fields)

Commands (all run from the repo root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):

- `find reports/round-35 -type f | sort` → six files, no `cov/` (2026-10-19)
- `for p in linguistics myth-symbol culture-material synthesis verification civilizations; do ls corpus/knowledge/$p/*.md | wc -l; done` → 21/19/18/29/20/94
- `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` → exit 0, `totals.files 201`, `files_with_marker 135`, `lines 36395`
- `for f in topic sources couples verified-at recheck source scope; do grep -rlE -- "^- $f:" corpus/knowledge/*/*.md | wc -l; done` → 201/201/201/201/201/134/0
- `grep -rn "frontmatter 4/4\|3/4 class" --include=*.md --include=*.json --include=*.py . | grep -v '^./reports/round-35/' | grep -v '^./.git/' | wc -l` → 0
- `sha256sum corpus/README.md` → `053966a2147e5e71675b290d12bd4e523b73b31c764513ccb26a672bed37d57c`
- `mkdir -p .scratch/c17/iso && git archive HEAD | tar -x -C .scratch/c17/iso` then, inside the copy, `python3 -B reports/round-28/readme/sweep.py --selftest` → 12/12, exit 0, and `python3 -B reports/round-28/readme/sweep.py` → `rows 201 files 201`, `topic_mismatch 0`, `footer_ok True`, exit 0
- `python3 -B .scratch/c17/row_audit.py .` (and `.scratch/c17/iso`) → `topic byte-equal: 201 | mismatches: 0`, `VERDICT: AGREE-with-filed-sweep` on both trees
- `python3 -B .scratch/c17/readme_delta.py --pre .scratch/c17/fix/pre.md --post .scratch/c17/fix/post_{ok,bad,bad2}.md --tree .scratch/c17/fix` → exit 0 / 1 / 1 with the findings in §4
- `git status --porcelain` → `?? reports/round-35/` only (no filed byte touched by this seat)
