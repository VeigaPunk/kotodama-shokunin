# ReviewEntryContract — round 50, claim C: pastoralism-animal-husbandry entry contract

- Seat: ChousaR27R2.ReviewEntryContract-4 (leaf; no delegation, no background jobs).
- Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin, branch main, base `4ad26836552462d28a946ca3b067cab0b5ce3532`.
- Read-only. Nothing in the lane was edited, staged or landed. Checks ran from stdin, in memory, or as read-only lane tools.
- Corpus identity: working tree is byte-identical to base for all 225 `corpus/knowledge/**/*.md`, `corpus/README.md`, `corpus/SOURCES.md` and `corpus/QUALITY.md` (sha256 against `git show <base>:<path>`). Every line reference below is therefore valid at base.
- Axes judged: coverage, operability, calibration.

## 0. Result

- **Contract = the r48/r49 eight-field head plus body shape.** Templates: `culture-material/hunting-foraging-subsistence.md` (205 lines) and `culture-material/cartography-and-mapmaking.md` (239 lines). Both pass the checker in §2.9 (`PASS`). Only 2 of 225 entries carry this head exactly. No written checklist exists in the lane; the contract is implicit in those two entries and in the round-48/49 claim declarations.
- **Coverage is fresh.** Filename probes `*pastoral*`, `*husband*`, `*herd*` return 0. Word-bounded topic probe returns 0 owners. 27 corpus files mention `pastoral|husbandr|transhuman|livestock|nomad` in body text. A 23-row neighbour inventory with verified line references is in §4.
- **Declared checks need fixes before landing (§5):**
  - D1: the `after_required` sweep string exits 2.
  - D2: the `pastoral-unowned` evidence command false-positives on `sherd`.
  - D3: `C.lands` omits `corpus/SOURCES.md`, so C's S-ids cannot resolve in its own counterfactual tree (the r49 REJECTED-HONEST-STOP pattern).
  - D4: no tool checks S-id resolution or `used-by`.
  - D5: base README prose names O's and Ca's land paths; a whole-file separability scan would read that as a C dependency.
- Claims gate at base, read-only (`tools/harness/claims-freshness.py --no-exec`): C 4/4, O 2/2, Ca 2/2 clauses hold.
- No blocker to writing the entry.

## 1. Axes

| axis | state | evidence |
|---|---|---|
| coverage | gap fresh; neighbour inventory ready; frontier format fixed | §4; claims gate C 4/4 hold |
| operability | sweep, heading, revisions, provenance gate, couples resolver all green at base; S-id check missing; sweep argv wrong; `C.lands` incomplete | §2.8, D1, D3, D4 |
| calibration | probe evidence string false-positive; "established" overstates a 2/225 head; contract reading conflict DR-1 | D2, §3 |

## 2. Contract checklist (apply in order)

### 2.1 Path and length

- File: `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md`. Run `test ! -e <path>` first; never overwrite an existing entry (round-42 incident, LOG.md:3814, recorded in `corpus/lessons/round-49.md` Mistakes).
- Length: `wc -l` ≤ 250 (claims: "≤~250"). Culture-material range in this census: 103–239 lines.

### 2.2 Headings

- Line 1: `# <Title> — <subtitle>`. Exactly one H1, em dash U+2014 with one space each side. Models: line 1 of both.
- Line 2: blank. Opening block = every line before the first `## ` line.
- H2s: `## 1. …` through `## N. …`, consecutive from 1, every H2 numbered. Zero `###` lines and zero `####`+ lines (both models; `culture-material/ritual-garments.md` has 3 H3 and is not a precedent).
- Last H2 = `Scope`. `Recheck` immediately precedes it.

### 2.3 Opening block: eight fields, this order, column 0

| # | line | format and rules |
|---|---|---|
| 1 | `- topic: <text>` | exactly one such line; single line; no trailing period; no continuation line may begin with `- ` + word character (`sweep.py:61`). Must contain the register words as whole words: pastoralism, herding, husbandry, transhumance, livestock. Without them future freshness probes miss this entry. |
| 2 | `- gap filled: <absence sweep>` | commands as run at landing with measured results (`→ **0**`); base sha; boundary sentences with `path:line`. Re-run at landing, not only at declaration (round-49 Mistakes, r42 row). |
| 3 | `- sources:` (plural) | gate-checked (`provenance-audit.py:75-76, 310-318`). Nested, two-space indent: `  - In-corpus anchors (repo-relative path:line, each re-read at HEAD <base sha> on 2026-10-21; sha256 pinned for load-bearing files):` then `    - \`path\` (sha256 \`<64 hex from sha256sum at base>\`): \`:line\` <needle>; …`. Then `  - External shelf — opened this round (2026-10-21), registered in corpus/SOURCES.md rows S048–S0nn; full locators and quotes in the round lesson's ## Gate: S0nn <citation> — <locator>; …`. |
| 4 | `- couples: <partition> — \`<path>\` (<owns …>; this entry owns <…>); <partition> — …` | ends with a period. Each `;`-group starts with a partition label and em dash (`couples-reference-extractor.py:40-42`). Labels: linguistics, myth-symbol, culture-material, civilizations, verification, synthesis. Cross-partition: `../<partition>/<file>.md`. Same directory: bare basename (both models). Every `*.md` token in the value, including inside parentheses, must resolve. Exactly one `- couples:` line. |
| 5 | `- source: lane-side authority is …` | singular key, required by the 8-field head (§3). Names the in-corpus anchors and the S-ids with URL and locator; ends with one design-method sentence. |
| 6 | `- verified-at: 2026-10-21 — …` | written at base sha `4ad2683…`; `Measured with \`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1\`:` then each command → **value**; needle-check tally; sha256 pin tally; `not claimed:` list. Must name checks actually run; no template date (`header-conformance-readings.md:140`, DR-4). |
| 7 | `- recheck: before <trigger> — …` | trigger first; then re-read/re-run list with path:line and S-ids; re-open each URL before citing a number ("edition churn"). |
| 8 | `- scope: reference method and lane policy for the culture-material partition. This entry owns … It does not own … It decides nothing about any world …; lore-shokunin owns <…>.` | scope and handoff. |

Required key sequence, exact: `topic, gap filled, sources, couples, source, verified-at, recheck, scope`.

### 2.4 Body (order and roles, both models)

1. **Register property.** Bold master claim; four load-bearing choices in order; N-condition test as a numbered list; diagnostic failures paragraph (a neighbouring register fails which condition).
2. **One-owner boundary.** One sentence, then `| Neighbour | What it owns (live anchor) | This entry's boundary |`, 15 or more rows (§4 is the candidate set).
3. **Domain sections (3…k).** Each with at least one pipe table. Every factual claim cites `path:line`, an S-id, or carries `(to-verify)`.
4. Optional decision table `| If your culture… | then the register needs… | and check |`.
5. **Build order.** Numbered; each step ends with `*Artifact: …*`.
6. **Decision record.** `| ID | Decision | Trigger | Failure if skipped |`. IDs `DR-PA-01…` (prefix unused: 0 hits in `corpus` and `reports`).
7. **NON-CANON worked micro-example.** Paragraph begins `**NON-CANON.**` and states that culture, place and numbers are invented.
8. **Calibration bank.** `| Claim | Status | What to say instead |`. Status ∈ {R, C, B, H, T} per `calibration-registry.md:35-39`. Then bold **Living-practice flag** and **Precision traps** paragraphs (both models).
9. **Recheck** paragraph. **Scope** paragraph containing `Handoff: lore-shokunin owns …`.
- Every `§N` reference must be ≤ the highest H2 number.
- Pipe tables: `|---|` separator row, blank line before and after.
- No TODO, TBD, placeholder, scaffold, MVP. No emoji.

### 2.5 Calibration and sourcing (QUALITY.md items 1–6)

- **Item 1:** `(to-verify)` inline for every unopened claim. The provenance gate counts marks as inventory, not findings (`provenance-audit.py:31`).
- **Item 2:** each framework claim gets a registry code and a reason; pop-mythography flagged on first use. Registry rows to cite where relevant: CAL-04 (`calibration-registry.md:51`, stage ladder, R). Code definitions: `calibration-registry.md:33-41`.
- **Item 3:** `- couples:` non-empty, labelled per §2.3.
- **Item 4:** decision/typology tables and a worked example; no essays.
- **Item 5:** canon hygiene; handoff in Scope.
- **Item 6:** tiers A/B/C scoped per claim; publisher abstract = B for substantive claims; `community` never A; C is a lead only (`SOURCES.md:14-18`).
- Do not cite "QUALITY criterion 7" (Ca lands it; see D5).

### 2.6 Frontier: SOURCES rows and round lesson (append-only; not a claim)

- Columns, exact: `| id | source | kind | tier | scope | anchor | teaches | status | opened | recheck | used-by |` (`SOURCES.md:28`). Observed kinds: docs, dataset, paper, spec, book, tool, community. Recheck: `90d`, `180d`, `365d`, `on-release`. Status: `queued | mined | rejected`.
- Ids S048 upward. Append after the last registry row `S047` (`SOURCES.md:76`) and before `## Paths` (line 78). `opened` = `2026-10-21`. `status` = `mined` once the entry cites it. `used-by` = `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` (repo-relative, as in S031–S043).
- Only URLs actually opened this round. Quote ≤25 words, verbatim, with location. Registry header: no row without an opened source.
- Round lesson `corpus/lessons/round-50.md` (does not exist yet). Head lines `source:`, `verified-at:`, `recheck:`, `scope:` (as `round-49.md:3-6`). `## Gate` entries: `- S0nn — <URL> — accessed 2026-10-21 — <locator>: "<quote>". Grounds: <one line>.` (`round-49.md:27-31`). Optional Search-log paragraph (`SOURCES.md:112-118` pattern).

### 2.7 README (`corpus/README.md`; C-owned edits only)

1. Line 266: `## culture-material/ (27)` → `(28)`.
2. Insert between line 285 (`music-instrument-lexicon.md`) and line 286 (`ritual-garments.md`): `` - `pastoralism-animal-husbandry.md` — <topic> `` with `<topic>` byte-equal to `topic_of()` (`sweep.py:74-82`).
3. Line 578: `Total knowledge entries: 225.` → `226.`
4. Footer, lines 580–582: `Counts checked 2026-10-21 from the repo root:` / command line unchanged / `(total 226 files; directory totals 25/26/28/29/24/94).` Keep line 583 and the superseded-reading history (584–591). Add the new reading; do not delete earlier ones.
5. Insert `revision: 2.7 — Round-50 culture-material landing (2026-10-21): …` directly above `revision: 2.6` (line 3). The label line must be followed by a non-blank body (`REVISION-STUB`, `check-readme-revisions.py:125`). Labels must be unique and non-increasing (`:112`, `:138`).
6. Append an `Index rows re-measured 2026-10-21 …` paragraph at the end (convention at lines 593–609).
7. Do not change line 1 (the only H1), the Known-gaps section (451+), or any other row.

### 2.8 Acceptance (run in the integrator's clone; all read-only; never `run-validation.py` in-tree)

| check | command | expected (observed at base where marked ✓) |
|---|---|---|
| sweep ✓ | `python3 -B reports/round-28/readme/sweep.py` | exit 0; `rows 226 files 226`; `topic_mismatch 0 []`; `footer_ok True`. Base ✓: rows 225 files 225, exit 0. |
| heading ✓ | `python3 -B tools/check-readme-heading.py` | exit 0. Base ✓: H1 count 1, H2 count 7. |
| revisions ✓ | `python3 -B tools/check-readme-revisions.py` | exit 0; top label 2.7. Base ✓: exit 0, one pre-existing `REVISION-ORPHAN` warning (lines 90, 101). |
| provenance ✓ | `python3 -B tools/gates/provenance-audit.py <entry>` | exit 0; `findings=0`. Base ✓ on both models. |
| couples ✓ | `python3 -B tools/harness/basename-couples-resolver.py <entry>` | every token `direct` or fallback; zero unresolved, zero ambiguous. Base ✓: 22 and 21 tokens, all direct. |
| head and headings | §2.9-A | `PASS`. Validated: both models PASS; `ritual-garments.md`, `writing-media-surface-economy.md`, `bathing-and-body-hygiene.md` FAIL with specific reasons; two synthetic breakages (stray `###`, H2 renumbered) FAIL. |
| S-ids | §2.9-B, run from lane root | empty list. Validated on hunting: 12 cited ids, 0 bad. |
| counts | `find corpus/knowledge -name '*.md' \| wc -l` → 226; `ls corpus/knowledge/culture-material/*.md \| wc -l` → 28 | — |
| length | `wc -l <entry>` | ≤ 250 |
| freshness | `python3 -B tools/harness/claims-freshness.py --claims reports/round-50/claims.json --root . --no-exec` | Base ✓: C 4/4, O 2/2, Ca 2/2 FRESH. |

Notes:
- The claims' `after_required` string `python3 -B reports/round-28/readme/sweep.py rows 226 files 226 topic_mismatch 0` exits 2 (`unrecognized arguments`; base ✓). Use the bare command and read the render lines.
- Git use: sweep, heading, revisions (default mode), provenance gate and resolver are git-free. `check-readme-revisions.py` uses git only in its selftest fixture leg (`:304–306`). Ca's counterfactual trees are git-free, so these five are safe there. `claims-freshness.py` and `receipt_guard.py` are git-bound.
- `reports/round-49/targets.json:8`: "ABSOLUTE: never run reports/round-*/run-validation.py in-tree".

### 2.9 Mechanical checker (validated this seat, in memory, no file written)

Part A — head order, headings, README topic equality. Run from lane root:

```python
import re, pathlib
CANON = ['topic', 'gap filled', 'sources', 'couples', 'source', 'verified-at', 'recheck', 'scope']
TOPIC_RE = re.compile(r"^- topic:(.*?)(?=\n- \w)", re.M | re.S)
RE_KEY = re.compile(r'^- ([a-z][a-z \-]*?):')
PARTS = r'(linguistics|myth-symbol|culture-material|civilizations|verification|synthesis)'

def topic_of(text):
    m = TOPIC_RE.search(text)
    if not m:
        return None
    parts = [ln.strip() for ln in m.group(1).strip('\n').splitlines()]
    return ' '.join(p for p in parts if p)

def check(text, readme_topic=None):
    f = []
    lines = text.rstrip('\n').split('\n')
    if len(lines) > 250:
        f.append('length %d > 250' % len(lines))
    h1 = [l for l in lines if l.startswith('# ')]
    if not (len(h1) == 1 and lines[0].startswith('# ') and ' \u2014 ' in lines[0]):
        f.append('H1 not single line-1 "# T \u2014 s"')
    if any(re.match(r'^#{3,} ', l) for l in lines):
        f.append('H3+ present')
    first_h2 = next((i for i, l in enumerate(lines) if l.startswith('## ')), None)
    if first_h2 is None:
        return f + ['no H2']
    head = lines[:first_h2]
    keys = [m.group(1) for l in head for m in [RE_KEY.match(l)] if m]
    if keys != CANON:
        f.append('head keys %s' % keys)
    if sum(l.startswith('- topic:') for l in head) != 1:
        f.append('topic line count != 1')
    if sum(l.startswith('- couples:') for l in head) != 1:
        f.append('couples line count != 1')
    h2 = [l for l in lines if l.startswith('## ')]
    nums = [re.match(r'^## (\d+)\. ', l) for l in h2]
    if any(m is None for m in nums) or [int(m.group(1)) for m in nums] != list(range(1, len(h2) + 1)):
        f.append('H2 not numbered 1..N')
    if 'Scope' not in h2[-1]:
        f.append('last H2 not Scope')
    if not any('Recheck' in l for l in h2):
        f.append('no Recheck H2')
    if not any('Calibration' in l for l in h2):
        f.append('no Calibration H2')
    if not any(l.startswith('**NON-CANON') for l in lines):
        f.append('no **NON-CANON** paragraph')
    if not re.search(r'^\|[\s:\-|]+\|\s*$', text, re.M):
        f.append('no pipe-table separator')
    if readme_topic is not None and topic_of(text) != readme_topic:
        f.append('README topic not byte-equal')
    if re.search(r'^- couples: (?!%s \u2014 )' % PARTS, text, re.M):
        f.append('couples not partition-labelled')
    secs = [int(x) for x in re.findall(r'\u00a7(\d+)', text)]
    if secs and max(secs) > len(h2):
        f.append('section ref %d > H2 count %d' % (max(secs), len(h2)))
    if re.search(r'\b(TODO|TBD|placeholder|scaffold|MVP)\b', text, re.I):
        f.append('forbidden placeholder word')
    return f

entry = pathlib.Path('corpus/knowledge/culture-material/pastoralism-animal-husbandry.md')
readme = pathlib.Path('corpus/README.md').read_text(encoding='utf-8')
row = re.search(r'^- `pastoralism-animal-husbandry\.md` — (.*)$', readme, re.M)
text = entry.read_text(encoding='utf-8')
print(check(text, row.group(1) if row else None) or 'PASS')
```

Part B — S-ids cited by the entry resolve, and each row's `used-by` names the entry:

```python
REG = {m.group(1): m.group(0) for m in re.finditer(r'^\| (S\d{3}) \|.*$', pathlib.Path('corpus/SOURCES.md').read_text(encoding='utf-8'), re.M)}
REL = 'corpus/knowledge/culture-material/pastoralism-animal-husbandry.md'
cited = sorted(set(re.findall(r'\bS\d{3}\b', pathlib.Path(REL).read_text(encoding='utf-8'))))
print([(i, 'no-row' if i not in REG else 'used-by-missing') for i in cited if i not in REG or REL not in REG[i]])
```

## 3. Contract facts and conflicts

- **Why the singular `- source:` line is required.** The fleet sentence (quoted at `header-conformance-readings.md:28`; the fleet file itself was not re-read here) requires `source:`, `verified-at:` and `recheck:` to open each entry. The lane gate profile (`provenance-audit.py:75`) checks `topic`, `sources`, `couples`. The 8-field head satisfies reading A (singular `source:` in the opening block), reading B (plural `sources:` present), and reading C at once. Both models satisfy all three readings.
- **Conflict, not a blocker.** `header-conformance-readings.md:137` (DR-1) and the round-8 protocol (`:4`) name a plural-only profile for new entries ("no separate singular line"). The C claim's 8-field head includes the singular line; follow the claim. Escalation stays with the integrator (`header-conformance-readings.md` §10).
- **"Established" is the r48/r49 generation, not the partition norm.** Culture-material key sets in this census: exact 8 in order: 2 (hunting, cartography); 8 keys out of order: 2 (bathing, timekeeping); 9 keys with a `calibration:` key: 1 (writing-media); 7 keys: 3; 6 keys: 2 (furniture, transport); 5 keys (`topic, sources, couples, verified-at, recheck`): 17. Do not bulk-rewrite older headers (`header-conformance-readings.md` §7).
- **Calibration status vocabulary.** The models use registry codes R/C/B/H/T in a Status column, not QUALITY's "mainstream/contested/discredited" words. Follow the models.

## 4. Coverage inventory: candidate one-owner boundary and couples (all verified at base)

Probe results: filename `*pastoral*|*husband*|*herd*` = 0; word-bounded topic probe (`\b(pastoralism|pastoral|herding|husbandry|transhumance|livestock)\b`) = 0; the claims' own substring probe = 1, a false positive on `sherd` (see D2).

| neighbour (path) | live anchor (line; quoted fragment) | boundary for the new entry |
|---|---|---|
| culture-material/hunting-foraging-subsistence.md | :36 "not planted, herded or owned as a standing crop" (wild-source test; dominant-mode rule) | herding is the complement; cite the test; do not own wild capture |
| culture-material/agrarian-field-system-lexicon.md | :62 agropastoral "fields + pasture + transhumance routes"; :47, :56 herd calendar, communal herding | mixed field-pasture systems named there; herd management and transhumance here |
| culture-material/transport-mobility-lexicon.md | :4 topic DRAFT "(human porterage, ox, horse, camelid, dog, wind)"; :70 "llama herds rather than carts" | draft and pack use stays there; breeding, herd structure and products here |
| culture-material/fire-fuel-light.md | :37 dried dung "the herds' output" | dung as herd product cited; the fire stays there |
| culture-material/writing-media-surface-economy.md | :47 "parchment consumes a herd over years"; :138 scriptorium "herd, lime pits" | hide supply cited as input; surface economy stays |
| culture-material/ritual-garments.md | :80 wool office "re-manufactured out of livestock and calendar" | livestock input cited; the rite stays |
| culture-material/music-instrument-lexicon.md | :87 Jabal "(tents/livestock)" | ancestry myth stays |
| culture-material/calendar-festival-systems.md | :79 husbandry-keyed month names | calendar stays |
| linguistics/semantic-fields-lexicon-building.md | :70 "Pastoral wealth vocabulary (herd-age, herd-color, herd-condition terms)"; :105 steppe bundle "subsistence (herd wealth)" | lexicon stays; herd facts supplied |
| myth-symbol/animal-symbolism.md | :73 "a livestock culture"; :110 "the Mongol five livestock"; :122 fauna list | livestock economy cited; the sign and idiom stay |
| myth-symbol/sacred-kingship-mythic-charter.md | :21 "the king as sipa, shepherd"; :65 "tenant, servant, or shepherd" | herd-keeping labour cited; the charter stays |
| myth-symbol/hero-journey-variants.md | :51–53 shepherd foundlings; :110 "steppe/pastoral → inherited slaying-formula" | herd-labour facts cited; the myth stays |
| myth-symbol/celestial-symbolism-calendars.md | :28 "pastoralists on milky/river figures" | sky stays |
| civilizations/turkic-steppe.md | :26 mobile pastoralism need not replace other modes; :148 "Do not make pastoral production synonymous with economic isolation" | regional case cited, not restated |
| civilizations/mongol.md | :40 "Mobile pastoralism, urban production, and documentary administration" | regional case cited |
| civilizations/scythian-saka.md | :70 "Do not equate pastoralism with total absence of farming" | regional case cited |
| civilizations/finnic-sami.md | :140 "Do not map herding status directly onto Sámi identity"; :150 "not the eternal condition" | regional case; living-practice flag |
| civilizations/dine-navajo.md | :125 "do not stage wool pastoralism as unchanged from remote antiquity" | regional case; living-practice flag |
| civilizations/inca.md | :128 "Connect herding and cultivation to specialist vocabulary" | regional case cited |
| synthesis/source-discipline-calibration.md | :96 "pastoralism → one hero pattern" as a forbidden empirical law | calibration cross-reference |
| synthesis/coupling-model.md | :150 "imported wool does not require local sheep husbandry" | coupling rule cited |
| verification/costume-era-consistency-gate.md | :65 MAT-02 "cultivation/herding/collection or an external supplier" | gate rule cited |
| verification/calibration-registry.md | :51 CAL-04 (stage ladder, R); :35–39 codes | status vocabulary |

- Corpus body mentions: 27 files for `pastoral|husbandr|transhuman|livestock|nomad`; 0 topic owners.
- All 23 target paths in §4 exist at base: 15 confirmed by a file-existence probe; the other 8 appear in grep output above, which reads only `corpus/knowledge` at base.

## 5. Defects in the declared checks and fixes

- **D1 (operability).** `after_required` for C contains `python3 -B reports/round-28/readme/sweep.py rows 226 files 226 topic_mismatch 0`. The sweep takes no positional arguments and exits 2 (`unrecognized arguments`; verified). Fix: run the bare command and check the render lines (`rows 226 files 226`, `topic_mismatch 0 []`, `footer_ok True`, exit 0).
- **D2 (calibration).** The `pastoral-unowned` evidence command `grep -rniE '^- topic:.*(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/` returns one line: `culture-material/writing-media-surface-economy.md:3`, where `herd` matches inside `sherd`. The freshness gate is correct and holds the clause (word mode, whole-token aliases, `claims-freshness.py:749-762`). Fix: use `grep -rniE '^- topic:.*\b(pastoralism|pastoral|herding|husbandry|transhumance|livestock)\b' corpus/knowledge/` (verified: 0 lines). Keep the claim's target aliases as whole words. Stems such as `husbandr` never match a whole token in word mode, so evidence and target must use the same full words.
- **D3 (separability, operability).** `C.lands` = entry + `corpus/README.md`. C's entry must cite S048+ rows, which live in `corpus/SOURCES.md`, outside `C.lands`. C's counterfactual tree (base + C.lands) cannot resolve them. This is the pattern in `corpus/lessons/round-49-verifier-spotcheck.md:17` (REJECTED-HONEST-STOP: "C cites the registry S creates"). Fix: add `corpus/SOURCES.md` to `C.lands` (append-only rows; `used-by` changes logged in the round lesson). If the entry cites the lesson's `## Gate`, add `corpus/lessons/round-50.md` too. Do not treat the frontier as a non-claim: Ca's checker cannot see it.
- **D4 (operability).** No tool in `tools/` references `SOURCES.md` or `used-by` (search at base: no matches), so the after_required clause "every cited S-id resolves to a SOURCES row whose used-by names the entry" has no executable check. Fix: run §2.9-B in acceptance. Validated on hunting (12 ids, 0 bad).
- **D5 (separability design hazard for Ca; constrains C's text).** Base prose already names other claims' land paths. `corpus/README.md:18` names `tools/check-readme-revisions.py` (O.lands; the file exists at base). `corpus/README.md:207` names `QUALITY.md` (Ca.lands is `corpus/QUALITY.md`). C lands `corpus/README.md`. A whole-file name scan (`X.lands` bytes match `Y.land` path) would report C→O, and possibly C→Ca on a basename match, though C adds no such text. Fix for Ca: scan only the claim's added or changed lines (diff against base, restricted to `X.lands`), or exclude paths that already exist at base. Constraint for C: the entry and the 2.7 revision text must not name any O or Ca land path, nor their exports, nor "criterion 7". The revision text should describe only the culture-material landing.
- **D6 (filename probes, minor).** `find corpus/knowledge -iname '*herd*'` and the `count_eq` glob `**/*herd*.md` would match any future filename containing `herd`, such as `sherd`. None exists today (0). Prefer `*[!s]herd*` or a word-bounded test before a `sherd` filename lands. The pastoral-unowned clause itself holds (see D2).

## 6. Unrun checks and limits

- No external source opened. Frontier rows are not drafted and no quote is verified. The S-id check was validated only on in-corpus rows.
- No entry, README, SOURCES row, lesson, clone or receipt was created. No landing gate was run in a clone. `run-validation.py` was not run.
- Fleet files were not read; the fleet sentence is quoted from `header-conformance-readings.md:28`.
- O and Ca changes were not verified. D5 is a design note for Ca's checker, not a test of it.
- The claims' `before` clause for C ("total 225; culture-material 27") was confirmed at base (225/27).

## 7. Tooling record

- No installs or updates. Every check used the system `python3` and existing lane tools in read mode.
- Read-only commands only: `git cat-file`, `git show`, `git ls-tree`, `git diff-index` (plumbing), and lane gates `sweep.py`, `check-readme-heading.py`, `check-readme-revisions.py`, `provenance-audit.py`, `basename-couples-resolver.py`, `claims-freshness.py --no-exec`. Stdout captures went to `/tmp` and were removed; no lane file was written except this report.
