- Seat: C07 | verifier (claim C) | round 47 | date 2026-10-19 | baseline `6e9a30d`

# C07 — pre-landing contract audit: `culture-material/cartography-and-mapmaking.md`

- Mission (verbatim, `reports/round-47/targets.json` seat C07): "Contract audit: the draft satisfies corpus/QUALITY.md (calibration, living-practice flags, no canon claim, handoff target) + the culture-material entry convention + the one-owner rule. Pass/fail per clause."
- Writes: this fragment only. No corpus byte, no instrument byte, no filed-round byte was written. No `run-validation.py` was executed. No git commit, push, install, or network.
- All measurements are read-only, from the lane root, at HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`git rev-parse HEAD`), 2026-10-19T17:55Z, with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.
- **Draft availability at audit cut: none.** `find reports/round-47 -type f` at 17:55Z returned only `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`, and `calib/Ca02-resolver-edge.md`. The C01–C04 draft fragments this audit is written to check did not exist. This is a parallel 64-seat wave; the audit therefore separates what is measurable now (the landing contract and ownership) from what cannot be measured until the assembled entry bytes are filed.

## 0. Verdict at a glance

| audit object | verdict | basis |
|---|---|---|
| Landing path, partition, sort position | **PASS** | target absent; culture-material at 25; sort slot between `calendar-festival-systems.md` (5) and `costume-semiotics.md` (6) |
| One-owner rule at HEAD `6e9a30d` | **PASS** | 0 filename owners, 0 topic owners; 11 topic-line hits all metaphor/handoff, re-dispositioned in §4 |
| Neighbour/boundary targets resolve | **PASS** | all 7 K02-named neighbours exist at HEAD |
| README arithmetic (223 → 224, vector 224) | **PASS as arithmetic; edit not yet filed** | live footer sums 223; post-landing target `25/26/26/29/24/94` sums 224 (§5) |
| QUALITY.md Q1–Q5 **as delivered** | **could-not-evaluate** | no entry bytes at audit cut; `could-not-evaluate` is **not** green and must not be staged as such |
| Culture-material convention N1–N8 **as delivered** | path/ownership legs **PASS**; head-block, topic-equality, source-honesty legs **could-not-evaluate** | convention measured from live entries (§3); draft bytes absent |
| Seed coverage of the contract | **PASS-with-two-named-gaps** (F1, F2 in §6) | `reports/round-44/scout/K02-gap-scout.md` §4 |

**This is not a landing approval.** It certifies that the claim's structural premises hold at HEAD and that the seed carries the contract material, and it names two seed defects the assembled draft must cure. Content clauses stay `could-not-evaluate` until the bytes exist; §7 supplies a re-runnable check so the integrator can convert them to PASS/FAIL in one command before staging.

## 1. Evidence base and method

Read for the contract: `corpus/QUALITY.md` (the admission bar), `PROVINCE.md` (handoff/refusal), `corpus/knowledge/synthesis/worldbible-integration-contract.md` (the handoff interface), and the live culture-material partition for the entry convention. Read for the claim: `reports/round-47/claims.json:24-34` (claim C), `reports/round-44/scout/K02-gap-scout.md` (seed, boundary table, shelf, calibration bank, README implications). Read for precedent: `reports/round-43/cov/C04-contract-audit.md` (the closest prior contract audit; its 9-field r42 convention is *not* the culture-material convention — see F5).

Measurements at HEAD `6e9a30d`:

```
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-47/
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access '.../cartography-and-mapmaking.md': No such file or directory
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|\batlas\b|\bitinerar|\bsurvey\b|\btopograph|\bmap\b|\bcharts?\b)' corpus/knowledge/ | wc -l
11
```

No `corpus/` or `reports/round-1..46/` byte was edited; the only tracked-tree change in this seat is this out file.

## 2. `corpus/QUALITY.md` — clause by clause

The admission bar is five clauses (`corpus/QUALITY.md:3`): provenance (`:5-8`), calibration (`:9-12`), coupling (`:13-15`), usability (`:16-17`), canon hygiene (`:18-20`). For each: what the clause requires, what the K02 seed already supplies, and the draft-level verdict at audit cut.

### Q1 — Provenance (`corpus/QUALITY.md:5-8`)

**Requirement.** Every factual claim carries a cited, checkable source; unverified claims are marked `(to-verify)` inline; invented sources are a conformance defect.

**Seed provision.** `K02-gap-scout.md:249-286` gives a two-tier shelf. Tier A is in-corpus registrations cited by path (9 rows, e.g. `cosmology-cosmography.md` sources, `sacred-topography-pilgrimage.md:167-168`, `mesoamerica-primary-sources.md:28,58`, `polynesia-navigation.md:52-74`). Tier B is 17 external works (Harley & Woodward; Harley 1989; Wood; Monmonier; Jacob; Ptolemy/Berggren & Jones; Campbell; Edson; Kain & Baigent; Mundy; Boone; Pickles; Buisseret; Snyder; Dilke; al-Idrisi; Peutinger/Antonine; Ortelius/Mercator), with the seed's own instruction: "Every Tier B item must be marked `(to-verify)` for direct quotation/page reference in the entry" (`:286`).

**Draft-level verdict: could-not-evaluate (no bytes).** The seed shelf is contract-shaped but the clause is satisfied only by the *entry's* inline handling. Two hazards are named: (a) presenting a Tier B work as inspected when it was not (`F4`); (b) asserting a page range the seed itself marks `to-verify` — e.g. Campbell's page range is explicitly `to-verify` at `K02-gap-scout.md:273`. The in-corpus Tier A rows are checkable now; §4 verifies their paths resolve, and the exact `path:line` readings are C06's seat.

### Q2 — Calibration (`corpus/QUALITY.md:9-12`)

**Requirement.** Every framework entry names its status — mainstream / contested / discredited — with the reason; pop-mythography is flagged on first use.

**Seed provision.** `K02-gap-scout.md:288-297` gives a six-row bank: neutral/objective map **discredited**; medieval flat-earth-from-T-O **discredited**; portolan photographic accuracy **overclaim**; indigenous maps childlike/mental-only **discredited**; map-is-territory **category error**; one-way European diffusion **contested**. Each row carries a reason and an anchor.

**Draft-level verdict: could-not-evaluate (no bytes).** The content needed is present in the seed; the requirement is that the assembled entry lands the status *in the body* and repeats the status at first use, not merely in a terminal shelf. The two cartography-specific traps the draft must not walk into are both seeded: the flat-earth/T-O claim must cite the neighbour's own disclaimer (`myth-symbol/cosmology-cosmography.md:102`), and the one-way-diffusion row must stay `contested`, not be resolved by assertion (`K02-gap-scout.md:297`).

### Q3 — Coupling (`corpus/QUALITY.md:13-15`)

**Requirement.** The `- couples:` line names the systems/files the entry connects; an entry that couples nothing must say so.

**Seed provision.** `K02-gap-scout.md:181-193` is a seven-row boundary table against `cosmology-cosmography.md` (symbolic T-O vs survey map), `sacred-topography-pilgrimage.md` (place/route register), `direction-symbolism.md` (orientation), `architecture-settlement-lexicon.md` (city plan/groma), `writing-media-surface-economy.md` (surfaces/reproduction), `mesoamerica-primary-sources.md` (lienzo source class), and `transport-mobility-lexicon.md` (route representation). The handoff target is mandated by the lane (`PROVINCE.md:22-25`; `worldbible-integration-contract.md:2`).

**Draft-level verdict: could-not-evaluate (no bytes); all named neighbours resolve at HEAD** (commands in §4). The `- couples:` line must be one physical line (the convention, §3.2) and every token must resolve; §7 checks both.

### Q4 — Usability (`corpus/QUALITY.md:16-17`)

**Requirement.** A worldbuilder can act on it: decision tables, typology tables, checklists, worked examples; no essays.

**Seed provision.** `K02-gap-scout.md:234-247` supplies the section spine: question → form typology → survey chain → projection/scale → symbolization → reproduction/trade → silences → calibration bank → nine-step build order → decision record + NON-CANON worked example (a river-delta cadastral tax map). Every section is specified to end in a design lever or a decision row.

**Draft-level verdict: could-not-evaluate (no bytes).** The live partition's length norm is 103–221 lines, median 149 (§3.3); an entry materially outside that band is a review flag, not automatically a fail. The structural test is that the typology, decision record, build order and NON-CANON example are present as *tables/protocol*, not prose.

### Q5 — Canon hygiene (`corpus/QUALITY.md:18-20`)

**Requirement.** No entry decides what is true in any world; canon recording and consistency verification belong to lore-shokunin; entries end at the handoff.

**Seed provision.** `K02-gap-scout.md:245-247` requires the worked example to be NON-CANON; §6.1 of the seed repeats "no canon, no real-world clearance, no lore ruling" citing `corpus/QUALITY.md:18-20` and `PROVINCE.md` "Refuses". The live convention adds `- scope:` naming "reference knowledge and craft method only … canon decisions belong to lore-shokunin" (`timekeeping-instruments.md:10`) and a handoff section (`:135-140`).

**Draft-level verdict: could-not-evaluate (no bytes).** The check is textual: `- scope:` present, a handoff section present, the worked example labelled NON-CANON, and no promotion/clearance/closure verbs. §7 scans all four; the strict token scan is the r43 audit's pattern (`reports/round-43/cov/C04-contract-audit.md:119`).

## 3. The culture-material entry convention — measured, not assumed

### 3.1 Filename, path and sort position

- Filename form: kebab-case, topic-descriptive, no numeric prefix. All 25 live culture-material basenames conform (`ls corpus/knowledge/culture-material/`).
- Proposed path `corpus/knowledge/culture-material/cartography-and-mapmaking.md` is free at HEAD and sits between `calendar-festival-systems.md` (position 5) and `costume-semiotics.md` (position 6), as measured with `ls … | nl | sed -n '5,7p'`. **PASS.**

### 3.2 Head block

The partition's head-block fields, counted from the 25 live entries:

| pattern | count | examples |
|---|---|---|
| 5 fields — `topic, sources, couples, verified-at, recheck` | 16 | `calendar-festival-systems.md:3-7` |
| 6–7 fields — adds `gap`/`gap filled`, sometimes `source` | 6 | `transport-mobility-lexicon.md:4-11`, `funerary-material-culture.md:3-7` |
| 8 fields — `topic, gap filled, sources, source, couples, verified-at, recheck, scope` | 3 (the three newest) | `timekeeping-instruments.md:3-10`, `bathing-and-body-hygiene.md:3-10` |
| 9 fields — the same plus `calibration` | 1 | `writing-media-surface-economy.md:3-5,29-33` |

The current convention for a new culture-material entry is the 8-field block, in that order, with the H1 as line 1. The `- sources:`, `- couples:` and similar fields may wrap as indented continuation lines; the *field order* is what is stable. `- topic:` is the one field the index compares (below), so it should be a single physical line.

**Draft-level status: could-not-evaluate (no bytes).** Required: all eight fields, in order; `- gap filled:` carrying a dated sweep at the landing HEAD (not the r44 baseline); `- verified-at:` carrying the ISO date and the write HEAD; `- recheck:` giving concrete triggers; `- scope:` naming reference/method-only and lore handoff.

### 3.3 Topic line ↔ README row equality

`reports/round-28/readme/sweep.py:74-82` extracts the entry's `- topic:` text and space-joins continuations; `:136-148` compares it to the README row description and records a `REWRITE` mismatch. The row regex is ``^- `([^`]+\.md)` — (.*)$`` (`:60`). Therefore:

- the README row description must equal the entry's `- topic:` text after whitespace normalization;
- a one-line topic is the safe form;
- the row must be in filename order, and the section header must match the file count (`:59`, `:149-150`).

**Draft-level status: could-not-evaluate (no bytes).** This is the highest coordination risk in the round — see F1.

### 3.4 Body shape, length and handoff

- Body sections end in decision tables or levers; the newest entries carry `DR-XX-nn` decision rows, a calibration section, a build order, and a NON-CANON worked example (`timekeeping-instruments.md:12-140`; `writing-media-surface-economy.md:29-201`).
- Length: live culture-material entries are 103–221 lines, median 149 (`wc -l corpus/knowledge/culture-material/*.md | sort -n`). The proposed entry's ten-section spine (`K02-gap-scout.md:234-247`) is consistent with that norm; it is not a licence to write an essay.
- Handoff: the `- couples:` line ends with a handoff target and a handoff section names what lore receives and what remains `(to-verify)` (`timekeeping-instruments.md:7,135-140`; `worldbible-integration-contract.md:49-70`). **PASS as a convention requirement; draft-level could-not-evaluate.**

## 4. The one-owner rule — measured at HEAD

### 4.1 Filename and topic ownership

```
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md
ls: cannot access ...: No such file or directory
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
```

The 11 topic-line hits from the broad probe, re-run at `6e9a30d`, are the same 11 K02 dispositioned (`K02-gap-scout.md:122-134`), and none names mapmaking as its subject:

| entry:line | class |
|---|---|
| `linguistics/sound-symbolism.md:3` | "map" as conceptual schema — metaphor |
| `linguistics/dialect-register-consistency.md:3` | "dialect map" — metaphor |
| `linguistics/sacred-registers-liturgical-language.md:3` | "map to" — verb |
| `myth-symbol/number-symbolism.md:3` | statistical "survey" |
| `myth-symbol/purity-pollution-boundary-systems.md:4` | "boundary map" — metaphor |
| `myth-symbol/sacred-topography-pilgrimage.md:5` | nearest neighbour: sacred-geography *diagram*, not the survey→sheet chain |
| `culture-material/ritual-garments.md:3` | "atonement map" — metaphor |
| `synthesis/dialect-faction-map-workflow.md:2` | "map features onto" — verb |
| `civilizations/finnic-sami.md:3` | "identity map" — metaphor |
| `civilizations/mesoamerica-primary-sources.md:3` | "source map" — metaphor |
| `civilizations/africa-primary-sources.md:2` | "source map" — metaphor |

K02's body-vocabulary sweep is the load-bearing demand test: the genuine cartographic footprint is seven files/nine lines, every one a by-product or an explicit handoff (`K02-gap-scout.md:151-162`), the sharpest being `myth-symbol/cosmology-cosmography.md:71` ("T-O diagrams are symbolic, not survey maps") and `:102` ("not cartographic"). **PASS: the register is unowned at HEAD, and the gap is not a carried topic** (`K02-gap-scout.md:195-207`).

### 4.2 Boundary targets resolve

All seven K02-named neighbours exist at HEAD (`test -f` on each, 8/8 including `timekeeping-instruments.md` as an instrument-side neighbour):

```
OK  myth-symbol/cosmology-cosmography.md
OK  myth-symbol/sacred-topography-pilgrimage.md
OK  myth-symbol/direction-symbolism.md
OK  culture-material/architecture-settlement-lexicon.md
OK  culture-material/writing-media-surface-economy.md
OK  civilizations/mesoamerica-primary-sources.md
OK  culture-material/transport-mobility-lexicon.md
OK  culture-material/timekeeping-instruments.md
```

**PASS.** Resolution is necessary, not sufficient: the draft must *cite* these by `path:line` and state the boundary (`K02-gap-scout.md:183-193`), not merely list them. C08 and C13 audit the boundary claims and the couples line.

### 4.3 Landing-time obligation

The one-owner result above is a measurement at `6e9a30d`, not a permanent property. Claim C's own threshold requires the gap re-verified "at landing (still unowned)" (`reports/round-47/claims.json:28,34`). C05 and V01 own that re-measurement; this seat's result is the pre-landing half of the evidence chain.

## 5. README arithmetic cross-check (C09's clause, verified here)

- Live header `corpus/README.md:234` reads `## culture-material/ (25)`; rows at `:240` (calendar) and `:241` (costume) are adjacent, so the new row goes between them.
- Live total `:544` reads `Total knowledge entries: 223.`; footer `:546-549` reads total 223, directory totals `25/26/25/29/24/94`.
- Post-landing target: culture-material 26, total 224, vector `25/26/26/29/24/94` = 224. **Arithmetic PASS.**
- The rev-2.4 prose defect is confirmed: `corpus/README.md:11` reads "the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**"; the right-hand vector sums **217**, not 223. The live footer vector sums 223. Rev 2.5 must supersede the prose with the measured vector, not propagate the 217.
- The sweep's own controls cover the topic-equality and counts paths (`reports/round-28/readme/sweep.py:287,401`); it has **no duplicate-topic test**, so a green 224 == 224 is not by itself a one-owner verdict (the r43 audit made the same point at `reports/round-43/cov/C04-contract-audit.md:62`).

## 6. Findings register

**F1 (apply-blocking if uncorrected — coordination).** The topic line can drift between the entry and the README row. `K02-gap-scout.md:224` says "C01 may refine [the topic seed]; the README row must stay byte-equal", but C09 drafts the row from the seed while C01/C04 draft the entry's `- topic:` independently. If either changes wording without the other, `sweep.py` reports `topic_mismatch` (`reports/round-28/readme/sweep.py:136-148`) and the claim's "sweep green" threshold fails. **Fix:** freeze the topic text once (the entry's `- topic:` is authoritative), then have C09 copy it byte-for-byte; run the §7 check before staging.

**F2 (major — seed contract gap).** The K02 seed's calibration bank and outline contain **no restricted-knowledge / living-practice boundary**. Cartography touches exactly the material that requires one: the lienzo/cartographic-history genre and indigenous mapping (`K02-gap-scout.md:261`), colonial-era cadastral mapping, and living communities' place knowledge. The lane's gate is explicit: "Do not expose restricted ritual knowledge to fill a table. Mark an access boundary and choose a less extractive comparison" (`corpus/knowledge/verification/myth-consistency-gate.md:34`), and every living-tradition case routes through `corpus/knowledge/verification/real-world-inspiration-boundaries.md:2,6`. **Fix:** the assembled entry must carry a boundary clause and a `- couples:`/`- recheck:` reference to both files, and must not enumerate a living tradition's restricted place knowledge. This is the clause the mission calls "living-practice flags"; the seed does not supply it, so the draft must.

**F3 (review — freshness of the gap counts).** K02's counts are dated to `c9f4eaa` (`K02-gap-scout.md:4,15-22`); the r47 baseline is `6e9a30d`. The tree is unchanged (223/25, 0 owners), and this seat re-measured the ownership counts at `6e9a30d`, but the entry's `- gap filled:` must carry the *landing-time* sweep (or explicitly name `6e9a30d` as its measurement point), not silently present the r44 count as current. This is the same defect class as r43's stale gap statement (`reports/round-43/cov/C04-contract-audit.md:77-90`).

**F4 (review — source honesty).** The Tier B shelf is large (17 works) and mostly unread in this offline lane. Every direct quotation or page-level claim must carry `(to-verify)`; no work may be described as inspected. The seed already marks Campbell's page range and al-Idrisi/Peutinger/Ortelius editions `to-verify` (`K02-gap-scout.md:273,282-284`); the entry must preserve those marks rather than launder them into assertion (`corpus/QUALITY.md:5-8`).

**F5 (review — field convention mismatch with the r43 audit).** The r43 contract audit reads a 9-field convention including `- calibration:` (`reports/round-43/cov/C04-contract-audit.md:129`). That is the *myth-symbol* convention. In culture-material, only `writing-media-surface-economy.md` carries `- calibration:`; the newest three entries use 8 fields and put calibration in the body. A draft that adds `- calibration:` is not penalized by the sweep, but it is a deviation from the partition's measured convention and should be a deliberate choice, not an inherited template.

**F6 (info — README prose defect).** See §5. Rev 2.5 must repair the rev-2.4 prose vector to sum 224; the footer vector is `25/26/26/29/24/94`.

**F7 (info — field order).** The culture-material order is `topic` first, `gap filled` second (`timekeeping-instruments.md:3-4`), not the gap-first variant found in some older myth-symbol drafts. The v2.4 README revision block and the seed's handoff notes do not override this.

No collision, duplicate-topic, or second-owner finding exists at HEAD. F1 and F2 are the two findings that can turn a structurally clean landing into a failed one.

## 7. Pre-staging check (re-runnable)

Save as `.scratch/check_c07.py` (or pipe it) and run against the assembled entry before staging. It is a read-only audit aid, **not** a durable gate — claim O owns the durable gate; this snippet converts the `could-not-evaluate` clauses above into PASS/FAIL for the integrator. It exits `0` only when every hard check passes.

```python
#!/usr/bin/env python3
"""C07 pre-staging contract check for the cartography entry. Read-only."""
import argparse, os, re, subprocess, sys

CORE = ["topic", "gap filled", "sources", "source", "couples",
        "verified-at", "recheck", "scope"]
FIELDS = CORE + ["calibration"]
PATH_RE = re.compile(r"(?:corpus|tools|reports|examples)/[A-Za-z0-9_./-]+\.(?:md|json|py|yml|yaml|txt)")
REL_RE = re.compile(r"`(\.\./[a-z-]+/[A-Za-z0-9_./-]+\.md)`")
BARE_RE = re.compile(r"`([a-z0-9][a-z0-9-]*\.md)`")
HEAD_RE = re.compile(r"^# (.+)$", re.M)
ISO_RE = re.compile(r"\b(20\d{2}-\d{2}-\d{2})\b")
SHA_RE = re.compile(r"\b[0-9a-f]{7,40}\b")
BLEED_RE = re.compile(r"\b(promoted|promotion|cleared|clearance|closed as|signed off|green-lit)\b", re.I)


def fields_of(lines):
    found = []
    for ln in lines:
        m = re.match(r"^- ([a-z][a-z -]*):", ln)
        if m and m.group(1) in FIELDS:
            found.append(m.group(1))
    return found


def section(text, name):
    """Text of a head field, including indented continuations."""
    m = re.search(rf"^- {re.escape(name)}:(.*?)(?=\n- [a-z]|\n## |\Z)", text, re.M | re.S)
    return m.group(1).strip() if m else ""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("draft")
    ap.add_argument("--root", default=".")
    ap.add_argument("--readme", default="corpus/README.md")
    ap.add_argument("--slug", default="cartography-and-mapmaking.md")
    a = ap.parse_args()
    root = os.path.abspath(a.root)
    text = open(a.draft, encoding="utf-8").read()
    lines = text.splitlines()
    fails, warns = [], []

    def ck(name, ok, detail=""):
        print(("PASS " if ok else "FAIL ") + name + (": " + detail if detail else ""))
        if not ok:
            fails.append(name)

    def warn(name, ok, detail=""):
        print(("PASS " if ok else "WARN ") + name + (": " + detail if detail else ""))
        if not ok:
            warns.append(name)

    # 1. H1 and head block
    ck("H1 exactly one", len(HEAD_RE.findall(text)) == 1, f"{len(HEAD_RE.findall(text))} found")
    end = next((i for i, l in enumerate(lines) if l.startswith("## ")), len(lines))
    fields = fields_of(lines[:end])
    ck("head fields present", all(f in fields for f in CORE), ",".join(fields))
    present = [f for f in fields if f in CORE]
    ck("head field order", present == [f for f in CORE if f in present], ">".join(present))

    # 2. topic single physical line
    topic_lines = [l for l in lines[:end] if l.startswith("- topic:")]
    ck("topic field present", len(topic_lines) == 1, f"{len(topic_lines)}")
    if topic_lines:
        topic = topic_lines[0][len("- topic:"):].strip()
        ck("topic is one physical line", " ".join(topic.split()) == topic)

    # 3. README row equality (skipped with a warning if the row is not filed yet)
    readme_path = os.path.join(root, a.readme)
    row = None
    if os.path.exists(readme_path):
        m = re.search(rf"^- `{re.escape(a.slug)}` — (.*)$", open(readme_path, encoding="utf-8").read(), re.M)
        row = m.group(1).strip() if m else None
    if row is None:
        warn("README row present", False, "row not filed yet; re-run after C09")
    elif topic_lines:
        ck("README row == topic", " ".join(row.split()) == " ".join(topic.split()),
           f"row {len(row)} chars / topic {len(topic)} chars")

    # 4. couples resolution
    couples = section(text, "couples")
    paths = sorted(set(PATH_RE.findall(couples)))
    missing = [p for p in paths if not os.path.exists(os.path.join(root, p))]
    rels = sorted(set(REL_RE.findall(couples)))
    base_dir = os.path.join(root, "corpus", "knowledge", "culture-material")
    missing += [r for r in rels if not os.path.exists(os.path.normpath(os.path.join(base_dir, r)))]
    ck("repo/relative paths in couples resolve", not missing,
       f"{len(paths)} absolute + {len(rels)} relative; missing {missing}")
    bare = sorted(set(BARE_RE.findall(couples)))
    ambiguous, zero = [], []
    for b in bare:
        hits = []
        for part in os.listdir(os.path.join(root, "corpus", "knowledge")):
            if os.path.exists(os.path.join(root, "corpus", "knowledge", part, b)):
                hits.append(part)
        if len(hits) > 1:
            ambiguous.append((b, hits))
        if not hits:
            zero.append(b)
    ck("bare .md tokens unique", not ambiguous, str(ambiguous))
    ck("bare .md tokens exist", not zero, str(zero))
    ck("couples is one physical line", couples.count("\n") == 0, f"{len(couples)} chars")

    # 5. gap-filled carries a measured sweep
    gap = section(text, "gap filled")
    ck("gap filled records a count", bool(re.search(r"\b\d+\b", gap)) and
       bool(re.search(r"(grep|find|ls |sweep|census|owner|files|total)", gap, re.I)))
    warn("gap filled not on an older baseline", not re.search(r"c9f4eaa|ac47c78|4a7aede", gap),
         "re-measure at the landing HEAD")

    # 6. provenance markers
    sources = section(text, "sources")
    ck("to-verify present in sources", "(to-verify)" in sources, f"{sources.count('(to-verify)')} marks")
    ext = [l for l in sources.splitlines()
           if re.search(r"(Press|UP\b|Routledge|Brill|University|Clarendon|Blackwell)", l)]
    unmarked = [l.strip()[:70] for l in ext if "(to-verify)" not in l and "in-corpus" not in l.lower()]
    warn("external shelf items marked", not unmarked, f"{len(unmarked)} unmarked: {unmarked[:3]}")

    # 7. verified-at and scope
    va = section(text, "verified-at")
    ck("verified-at ISO date", bool(ISO_RE.search(va)))
    shas = SHA_RE.findall(va)
    ck("verified-at names a commit", bool(shas), ",".join(sorted(set(shas))[:3]))
    scope = section(text, "scope")
    ck("scope is reference/method-only", all(w in scope.lower() for w in ("reference", "canon", "lore")))

    # 8. structure / usability
    low = text.lower()
    for name, needle in [("calibration section", "calibration"),
                         ("build order", "build order"),
                         ("decision record", "decision record"),
                         ("NON-CANON example", "non-canon"),
                         ("handoff section", "handoff")]:
        ck(name, needle in low)
    warn("length in partition band", 100 <= len(lines) <= 260, f"{len(lines)} lines")

    # 9. canon bleed scan
    hits = BLEED_RE.findall(text)
    warn("no promotion/clearance verbs (manual review; negations count)", not hits, str(hits[:5]))

    # 10. one-owner at HEAD
    target = os.path.join(root, "corpus", "knowledge", "culture-material", a.slug)
    ck("target path is free", not os.path.exists(target), target)
    owners = []
    for part in os.listdir(os.path.join(root, "corpus", "knowledge")):
        d = os.path.join(root, "corpus", "knowledge", part)
        if not os.path.isdir(d):
            continue
        for f in os.listdir(d):
            if f.endswith(".md"):
                for ln in open(os.path.join(d, f), encoding="utf-8"):
                    if re.match(r"^- topic:", ln) and re.search(r"(cartograph|mapmak|portolan|cadastr)", ln, re.I):
                        owners.append(f"{part}/{f}")
    ck("no cartography topic owner", not owners, str(owners))

    print(f"\n{len(fails)} FAIL, {len(warns)} WARN")
    print("HEAD", subprocess.run(["git", "-C", root, "rev-parse", "--short", "HEAD"],
                                  capture_output=True, text=True).stdout.strip())
    return 1 if fails else 0


if __name__ == "__main__":
    sys.exit(main())
```

What it does **not** check, and C06/C08/C13 must: whether each cited `path:line` says what the entry claims; whether the boundary table disposes each neighbour without restating it; whether the worked example is internally consistent. Those are semantic audits, not mechanical ones.

## 8. What this seat did not do

- Did not audit draft bytes that did not exist at 17:55Z; every content-clause verdict is `could-not-evaluate`, not PASS. If C01–C04 land after this cut, §7 is the conversion step and the integrator should file the result, not infer it.
- Did not run `reports/round-47/run-validation.py` (absolute rule; the file did not exist at this writing).
- Did not re-verify the claim's internal body-vocabulary counts beyond the ownership probes; K02's §3.4 demand sweep is cited as the seed's evidence and is C06/C05's to re-run.
- Did not fetch any external source (no network); no Tier B work was inspected, and no page-level claim was verified.
- Did not decide admission, promotion, clearance, or canon; this is a structural audit and ends at the handoff.

## 9. Command transcript (trimmed)

```text
$ git rev-parse HEAD
6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ find corpus/knowledge -name '*.md' | wc -l                       -> 223
$ ls corpus/knowledge/culture-material/*.md | wc -l                 -> 25
$ ls corpus/knowledge/culture-material/cartography-and-mapmaking.md -> absent
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' \
      -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l          -> 0
$ grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|\batlas\b|\bitinerar|\bsurvey\b|\btopograph|\bmap\b|\bcharts?\b)' corpus/knowledge/ | wc -l
11   # all 11 dispositioned in §4.1
$ ls corpus/knowledge/culture-material/ | nl | sed -n '5,7p'
     5  calendar-festival-systems.md
     6  costume-semiotics.md
     7  craft-artisan-lexicon.md
$ wc -l corpus/knowledge/culture-material/*.md | sort -n
min 103 / median 149 / max 221
$ grep -nE '^## culture-material/|^Total knowledge entries|^Counts checked' corpus/README.md
234:## culture-material/ (25)
544:Total knowledge entries: 223.
546:Counts checked 2026-10-19 from the repo root:
$ sed -n '11p' corpus/README.md   # rev-2.4 prose vector
the vector 25/23/25/29/24/94 -> **25/23/26/25/24/94**     # sums 217, not 223
$ python3 reports/round-28/readme/sweep.py  # not run by this seat; C10 owns the staged-tree run
$ find reports/round-47 -type f
reports/round-47/calib/Ca02-resolver-edge.md
reports/round-47/claims.json
reports/round-47/targets.json
reports/round-47/telemetry/dispatch-declared.json
```
