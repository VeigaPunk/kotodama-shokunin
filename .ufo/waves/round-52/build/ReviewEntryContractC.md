# ReviewEntryContractC — round 52, claim C: entry contract checklist for speech-surrogates-whistled-drummed.md

- Seat: KotodamaR52.ReviewEntryContractC (leaf; no delegation, no background jobs).
- Date: 2026-10-22. Read-only seat; nothing in the lane was edited, staged or landed except this report.
- Lane state measured: head `dea5ece63ca4372c41766ab242df1e26c2e6898a` (claim D landed on top of base `147cfde8…`); `find corpus/knowledge -name '*.md' | wc -l` → **227**; `test -e corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` → absent; sign entry `awk '/S094/…'` → **0** (D's target holds).
- Contract source: `.ufo/waves/round-50/build/ReviewEntryContract.md` §2, adapted to round 52. Models: `corpus/knowledge/linguistics/sign-languages-manual-modality.md` (224 lines) and `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md` (214 lines) — both PASS the §9 mechanical checker below, validated live this session, and three synthetic breakages (stray `###`, H2 renumber, bad partition label) all FAIL it.
- Axes judged: coverage (checklist completeness), operability (every command run or marked unrun), calibration (no invented requirement).

## 0. Result

The checklist in §1–§10 is the L1's pass/fail list for the entry. Every command was either run today with its measured result recorded, or is listed in §12 as unrun. No blocker found: base state supports the claim (gap fresh, DR-SRG unused, gate green on models, partial owners intact and untouched by D).

## 1. Preconditions (verify before accepting the draft)

| # | check | command | expected | measured today |
|---|---|---|---|---|
| P1 | target absent | `test -e corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` | false (never overwrite; round-42 incident) | absent ✓ |
| P2 | count before | `find corpus/knowledge -name '*.md' \| wc -l` | 227 | 227 ✓ |
| P3 | linguistics count before | `ls corpus/knowledge/linguistics/*.md \| wc -l` | 26 | 26 ✓ |
| P4 | DR prefix unused | `grep -rn 'DR-SRG' corpus/ reports/ \| wc -l` | 0 before landing | 0 ✓ |
| P5 | D landed, C separable | `git rev-parse HEAD` and sign-entry S094 count | D commit present; 0 | `dea5ece`, 0 ✓ |

## 2. Path and length

- File exactly `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md`. Any other path fails the claim.
- `wc -l` ≤ **250** (claim bound, harder than the r50 "≤~250"). Models are 224 and 214 lines with 15 H2s; C plans 14 H2s — the budget is real, watch §11–§14, which cost the models ~60 lines.
- Length is measured on the final landed bytes, after L1 renumbers `NEW-…` ids to `S134+` (renumbering must not push lines over 250).

## 3. Head: eight fields, this exact order, keys at column 0

Required key sequence (regex-checked): `topic, gap filled, sources, couples, source, verified-at, recheck, scope`. Both models conform; the gate (`tools/gates/provenance-audit.py:61` `FIELD_RE`) only requires `topic|sources|couples` presence, so order is a contract matter, checked by the §9 script.

| # | key | round-52 rules |
|---|---|---|
| 1 | `- topic:` | Exactly one such line in the head block; single logical field; continuations (if any) indented and never starting with `- ` + word char (`reports/round-28/readme/sweep.py:61`, `topic_of` at `:74-82` space-joins continuations). MUST contain, as findable stems: **speech surrogate(s), whistled, drummed, talking drum / drum language, signal code** — future freshness probes read topic lines only, and the claims gate matches topic lines word-mode (`claims-freshness.py` whole-token aliases). Without the stems the entry becomes invisible to its own recheck sweep. |
| 2 | `- gap filled:` | Sweeps **re-run at landing** with measured results, not quoted from the declaration. Three verified forms (measured today at `dea5ece`): filename `find corpus/knowledge \( -iname '*whistl*' -o -iname '*drum*' -o -iname '*surrogat*' \) \| wc -l` → **0**; claim's substring form `grep -rliE '^- topic:.*(whistl\|surrogat\|drum language\|talking drum)' corpus/knowledge` → **1** file, the non-owner `culture-material/music-instrument-lexicon.md:3` (its topic lists talking drums under music–myth links); word-bounded `grep -rniP '^- topic:.*\b(whistl\|drumm\|surrogat)' corpus/knowledge/` → **0**. Name each partial owner with a boundary sentence and `path:line` (the four in §5 row 2 below). Keep evidence and target needles in the same form (r50 D2 lesson). State the landing sha and date 2026-10-22. MUST NOT name `corpus/lessons/round-52.md`. |
| 3 | `- sources:` (plural) | Gate-checked field (`provenance-audit.py:61,75`). Nested, two-space indent: `  - In-corpus anchors (…re-read at <landing sha> on 2026-10-22…):` listing the partial-owner `path:line` set; then `  - External shelf — opened this round (2026-10-22), registered in corpus/SOURCES.md rows S134–S0nn…`. **Ban:** the r50 models write "the round lesson's Gate holds a located quote" — C must NOT name `corpus/lessons/round-52.md`, so say instead that each row carries its URL, access date, tier scope and located quote in the registry itself (pattern: S133's `anchor` and `teaches` columns, `SOURCES.md:162`). Draft rows are `NEW-<SeatName>-<n>`; L1 renumbers before landing (§8). |
| 4 | `- couples:` | Exactly one line; each `;`-group opens with a partition label + em dash; labels are exactly `linguistics, myth-symbol, culture-material, civilizations, verification, synthesis` (regex `tools/harness/couples-reference-extractor.py:41`, `tools/harness/basename-couples-resolver.py:42`). Same-directory neighbours as bare basenames; cross-partition as `../<partition>/<file>.md`. Every `*.md` token must resolve; ends with a period. Minimum content: the four declared partial owners (phonetics-phonology, orality-formulaic-language, sound-symbolism same-dir; `../culture-material/music-instrument-lexicon.md` cross-partition). Optional, if a seam is drawn: `sign-languages-manual-modality.md` (bare basename) and `writing-systems.md` for the signal-code-vs-script edge. |
| 5 | `- source:` (singular) | Required by the 8-field head (satisfies all three header-conformance readings; r50 report §3). Names the in-corpus anchor list plus the S134+ rows with URL, access date 2026-10-22 and tier scope; ends with one design-method sentence (models' pattern: "fix X first, then Y — never Z"). |
| 6 | `- verified-at: 2026-10-22 — …` | Names checks **actually run** at the landing sha: pre/post `find … \| wc -l` → **227 → 228**, `ls corpus/knowledge/linguistics/*.md \| wc -l` → **26 → 27**; the sweep render line `rows 228 files 228` may be named only if that seat's README leg has landed (it is a C.lands co-check, run at integration). No template dates (`header-conformance-readings.md:140`, DR-4 per r50 report). |
| 7 | `- recheck: before <trigger> — …` | Trigger first ("before any in-world speech surrogate becomes load-bearing"), then: re-run the two gap sweeps; re-open each cited S134+ row before quoting a figure or quote; re-read each partial-owner `path:line` before re-drawing a seam; re-open a tier-B/C row before upgrading any claim it supports. |
| 8 | `- scope:` | "Reference method and lane policy for the linguistics partition. This entry owns … It does not own … It decides nothing about any world …" + explicit `Handoff: lore-shokunin owns …` (also mirrored in §14 body). |

## 4. Heading rules

- Line 1: exactly one H1, `# <Title> — <subtitle>`, em dash U+2014 with one space each side. Line 2 blank.
- H2s: `## 1. …` through `## 14. …`, consecutive from 1, every H2 numbered; **last H2 = Scope**; **Recheck immediately precedes it** (plans: §13 Recheck, §14 Scope). Zero `###`/`####` lines anywhere.
- Every `§N` cross-reference ≤ 14 (the highest H2 number).
- The §9 script enforces all of the above and was shown to bite (renumber breakage → FAIL).

## 5. Body plan and per-section binding rules

Planned H2s (claim): 1 register property · 2 one-owner boundary · 3 typology (all channels — horns, reed pipes, jaw harps, xylophones, gongs — plus the signal-code boundary) · 4 whistled speech · 5 drummed speech · 6 encoding and ambiguity · 7 ecology and function · 8 who may speak (social control) · 9 transmission, learning and decline (including perception) · 10 decision table and build order · 11 NON-CANON worked example · 12 calibration bank · 13 recheck · 14 scope.

| section | binding rules (model-derived) |
|---|---|
| 1 | Bold **Master claim.**; the register's load-bearing choices in a fixed order; a test table `| Test | Pass when | Fails as (owner) |` naming which neighbouring register fails which condition; status codes inline. |
| 2 | One sentence + `| Neighbour (anchor) | What it owns | This entry's boundary |`. **Required rows** (the claim's declared partial owners, cited one-way, never restated): `linguistics/phonetics-phonology.md:197-199` (whistled/drummed couplings under environment→inventory), `culture-material/music-instrument-lexicon.md:98-100` (the "talking drum is this lane's centerpiece coupling… language phenomena, not merely music phenomena" handoff), `linguistics/orality-formulaic-language.md:114` (media extensions: drums/whistles as broadcast layer) and `:124` (drum layer in the worked example), `linguistics/sound-symbolism.md:121` (music hook row). A sign-entry row is optional; if used, never anchor at `:83,:87,:90,:92,:93` (D-changed lines, claim `must_not_cite`). |
| 3–9 | Each domain section carries **at least one pipe table**; every factual claim cites `path:line`, an S134+ id, or carries inline `(to-verify)`. No essays (QUALITY 4). The typology table must include the instrument-borne channels named in the plan and an explicit signal-code boundary row (who owns Morse-like codes: this entry draws the boundary; scripts stay with `writing-systems.md`). |
| 10 | Decision table `| If your culture… | then … | and check |`; numbered build order, each step ending `*Artifact: …*`; decision-record table `| ID | Decision | Trigger | Failure if skipped |` with ids `DR-SRG-01`… (§7). |
| 11 | First paragraph begins exactly `**NON-CANON.**` and states culture, place and numbers are invented, canon belongs to lore-shokunin. A worked example table is the model pattern. |
| 12 | `| Claim | Status | What to say instead |`; Status ∈ {R, C, B, H, T} per `calibration-registry.md:35-39` (verified: R,C,B,H,T rows at :35–39). Followed by bold **Living-practice flag** and **Precision traps** paragraphs (both models carry them). |
| 13–14 | Recheck paragraph (row-level, names ids and anchors); Scope paragraph containing `Handoff: lore-shokunin owns …`. |

- Pipe tables: `|---|` separator row, blank line before and after.
- Forbidden anywhere: `TODO, TBD, placeholder, scaffold, MVP` (case-insensitive; script-checked); emoji; naming `corpus/lessons/round-52.md`; naming any S-id ≥ S134 before L1 renumbering (drafts use `NEW-…`), and after landing any S-id **below** S134 among the external rows (in-corpus `path:line` anchors are the only base citations).

## 6. Calibration and sourcing rules that bind this entry (QUALITY items 1–6, 10)

- **Item 1:** every unopened/unverified claim carries inline `(to-verify)`; the gate counts marks as inventory, not findings (observed: sign entry reports `15 mark(s) on 14 line(s)` with `findings=0`, §8).
- **Item 2:** every framework claim carries a registry code + reason; codes are R/C/B/H/T from `calibration-registry.md:35-39` (the models' convention, not QUALITY's prose words).
- **Item 3:** `- couples:` non-empty and partition-labelled (gate enforces non-emptiness; labels enforced by §9 script).
- **Item 4:** decision/typology tables and a NON-CANON worked example; no essays.
- **Item 5:** canon hygiene; handoff in §14.
- **Item 6:** tiers scoped per claim; publisher description/abstract = B for claims about a work; `community` never A; C is a lead, never sole support (`SOURCES.md` tier definitions; QUALITY.md:6).
- **Item 10:** every cited row opened by ordinary means this round; `python3 -B tools/check-source-access.py` exits 0 today (verified) and must still exit 0 after C's rows land. A row reached past any access control is `rejected` via superseding row and cannot be cited (the S094/S132 precedent is the mined mistake of the round).
- **Item 7 (separability):** `C.lands` = entry + `corpus/README.md` + `corpus/SOURCES.md` (claims.json) — the r49 REJECTED-HONEST-STOP pattern (C citing a registry another claim creates) cannot recur because the registry rows are inside C's own lands. The entry must not name `corpus/lessons/round-52.md` and must not cite D-changed sign-entry lines (§5 row 2).

## 7. Decision-record prefix `DR-SRG`

- Format `DR-SRG-NN` (two digits, zero-padded from 01), used only in the §10 table's ID column and any in-body references to those ids.
- Unused prefix confirmed today: `grep -rn 'DR-SRG' corpus/ reports/` → **0 hits**. Existing families nearby (`DR-SGN-…` in the sign entry, `DR-PA-…` in pastoralism) must not be reused or extended.
- After landing, the only permitted hits are inside the new entry; a hit anywhere else fails this checklist.

## 8. Sources rows (L1 integration step for C's citations)

- Seats draft rows `NEW-<SeatName>-<n>`; L1 assigns `S134` upward at integration. Registry tail verified today: last row `S133` at `corpus/SOURCES.md:162`, `## Paths` at `:164` — new rows append between them.
- Row shape: the 11 columns of `corpus/SOURCES.md:28` (`id, source, kind, tier, scope, anchor, teaches, status, opened, recheck, used-by`); `opened` = `2026-10-22`; `status` = `mined` once the entry cites it; `used-by` = `corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` (repo-relative, S031–S043 pattern).
- Quote ≤ 25 words verbatim with exact location; never invent a source, quote, page or date.
- Post-renumber check on the entry text: `grep -oE '\bNEW-[A-Za-z]+-[0-9]+\b' <entry> | wc -l` → 0, and every cited S-id ≥ S134 (§9 Part B enforces the row+used-by half).

## 9. Mechanical checker (validated this session; run from lane root)

Part A — head order, headings, length, partition labels, placeholder words, §-refs. PASS expected; both models pass; the three breakages below were shown to fail.

```python
import re, pathlib
CANON = ['topic', 'gap filled', 'sources', 'couples', 'source', 'verified-at', 'recheck', 'scope']
TOPIC_RE = re.compile(r"^- topic:(.*?)(?=\n- \w)", re.M | re.S)
RE_KEY = re.compile(r'^- ([a-z][a-z \-]*?):')
PARTS = r'(linguistics|myth-symbol|culture-material|civilizations|verification|synthesis)'
def topic_of(text):
    m = TOPIC_RE.search(text)
    return None if not m else ' '.join(p.strip() for p in m.group(1).strip('\n').splitlines() if p.strip())
def check(text, readme_topic=None):
    f = []; lines = text.rstrip('\n').split('\n')
    if len(lines) > 250: f.append('length %d > 250' % len(lines))
    h1 = [l for l in lines if l.startswith('# ')]
    if not (len(h1) == 1 and lines[0].startswith('# ') and ' \u2014 ' in lines[0]):
        f.append('H1 not single line-1 "# T \u2014 s"')
    if any(re.match(r'^#{3,} ', l) for l in lines): f.append('H3+ present')
    first_h2 = next((i for i, l in enumerate(lines) if l.startswith('## ')), None)
    if first_h2 is None: return f + ['no H2']
    head = lines[:first_h2]
    keys = [m.group(1) for l in head for m in [RE_KEY.match(l)] if m]
    if keys != CANON: f.append('head keys %s' % keys)
    if sum(l.startswith('- topic:') for l in head) != 1: f.append('topic line count != 1')
    if sum(l.startswith('- couples:') for l in head) != 1: f.append('couples line count != 1')
    h2 = [l for l in lines if l.startswith('## ')]
    nums = [re.match(r'^## (\d+)\. ', l) for l in h2]
    if any(m is None for m in nums) or [int(m.group(1)) for m in nums] != list(range(1, len(h2) + 1)):
        f.append('H2 not numbered 1..N')
    if 'Scope' not in h2[-1]: f.append('last H2 not Scope')
    if not any('Recheck' in l for l in h2): f.append('no Recheck H2')
    if not any('Calibration' in l for l in h2): f.append('no Calibration H2')
    if not any(l.startswith('**NON-CANON') for l in lines): f.append('no **NON-CANON** paragraph')
    if not re.search(r'^\|[\s:\-|]+\|\s*$', text, re.M): f.append('no pipe-table separator')
    if readme_topic is not None and topic_of(text) != readme_topic: f.append('README topic not byte-equal')
    if re.search(r'^- couples: (?!%s \u2014 )' % PARTS, text, re.M): f.append('couples not partition-labelled')
    secs = [int(x) for x in re.findall(r'\u00a7(\d+)', text)]
    if secs and max(secs) > len(h2): f.append('section ref %d > H2 count %d' % (max(secs), len(h2)))
    if re.search(r'\b(TODO|TBD|placeholder|scaffold|MVP)\b', text, re.I): f.append('forbidden placeholder word')
    return f
rel = 'corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md'
text = pathlib.Path(rel).read_text(encoding='utf-8')
print(check(text) or 'PASS')
```

Validated: both models `PASS` (224 and 214 lines); synthetic `### 15. Scope` → FAIL (3 findings); `## 16. Scope` renumber → FAIL; `couples: semiotics — …` → FAIL.

Part B — S-ids resolve to rows whose `used-by` names the entry, with the round-52 lower bound:

```python
import re, pathlib
REG = {m.group(1): m.group(0) for m in re.finditer(r'^\| (S\d{3}) \|.*$', pathlib.Path('corpus/SOURCES.md').read_text(encoding='utf-8'), re.M)}
REL = 'corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md'
cited = sorted(set(re.findall(r'\bS\d{3}\b', pathlib.Path(REL).read_text(encoding='utf-8'))))
print([(i, 'no-row' if i not in REG else 'used-by-missing') for i in cited if i not in REG or REL not in REG[i]],
      'below-S134:' , [i for i in cited if int(i[1:]) < 134] or 'none')
```

Validated on the sign entry (adapted REL): 51 cited ids, 0 bad — the resolver logic works on real registry bytes.

## 10. Provenance gate expectations (observed, not assumed)

Run from lane root:

```
TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1 python3 -B tools/gates/provenance-audit.py corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md
```

- **Observed on the sign entry today:** two INFO lines —
  `INFO to-verify-count: …: 15 mark(s) on 14 line(s)` and
  `INFO scan: files=1 marks=15 mark-lines=14 findings=0 blocked=0` — then **exit 0**.
- **How to read it:** `to-verify-count` is inventory, never a defect (QUALITY 1 requires the marks). `findings` are the six defect ids (`missing-topic`, `missing-sources`, `empty-sources`, `missing-couples`, `empty-couples`, `missing-calibration`; `provenance-audit.py:77-84`). `blocked` lists argv paths that could not be read. Any `finding` or `blocked` line → exit 1; missing path → exit 2; clean → exit 0.
- **Expectation for the new entry:** exit 0, `findings=0 blocked=0`; any number of INFO mark lines is fine; a `calibration-prose-only` INFO is fine (finding fires only if the word `calibrat*` is absent entirely, `provenance-audit.py:101-104`). Placeholder-valued fields (`none`, `tbd`, `(to-verify)` as a whole value…) read as empty (`provenance-audit.py:66-74`).
- The gate is read-only and git-free; `--selftest` regenerates/asserts its fixture expectations if a deeper check is wanted.

## 11. Acceptance table (entry-scoped; run at integration from lane root)

| check | command | expected |
|---|---|---|
| head/headings/length/labels | §9 Part A | `PASS` |
| S-ids + lower bound | §9 Part B | `[]` and `below-S134: none` |
| provenance gate | §10 command | exit 0, `findings=0 blocked=0` |
| couples resolution | `python3 -B tools/harness/basename-couples-resolver.py corpus/knowledge/linguistics/speech-surrogates-whistled-drummed.md` | zero unresolved, zero ambiguous |
| DR prefix isolation | `grep -rn 'DR-SRG' corpus/ reports/` | hits only inside the new entry, all `DR-SRG-NN` |
| counts | `find corpus/knowledge -name '*.md' \| wc -l` → 228; `ls corpus/knowledge/linguistics/*.md \| wc -l` → 27 | exact |
| length | `wc -l <entry>` | ≤ 250 |
| lesson ban | `grep -n 'round-52' <entry>` | no `corpus/lessons/round-52.md` hit |
| D-line ban | cited sign-entry anchors (if any) | none of `:83,:87,:90,:92,:93` |
| dry-run receipt (criterion 9) | `python3 -B reports/round-52/dry-run.py --check` | receipt ↔ declarations both ways; every C command present |
| claims agreement | `python3 -B reports/round-52/claims-agree.py` | exits 0 |
| separability | `python3 -B tools/check-claim-separability.py reports/round-52/separability-manifest.json` | exits 0 |
| source access (criterion 10) | `python3 -B tools/check-source-access.py` | exits 0 after C's rows land |
| corpus sweep (integration-level, shared with README seat) | `python3 -B reports/round-28/readme/sweep.py` | exit 0; `rows 228 files 228`; `topic_mismatch 0 []`; `footer_ok True` |

Notes: the sweep takes no positional arguments — run it bare and read the render lines (r50 D1). `run-validation.py` is never run in-tree (`reports/round-49/targets.json:8`).

## 12. Cross-seat boundaries (explicitly out of this checklist's scope)

- `corpus/README.md` indexing, the `(27) → (28)` section count, the row string byte-equal to `topic_of()`, the totals footer, and the revision line belong to the README seat; this checklist only notes the sweep row above because it is C.lands-wide.
- `corpus/SOURCES.md` rows S134+ and the `NEW-…` renumbering are the L1's integration step (§8 records the verified insertion point and row shape).
- `corpus/lessons/round-52.md` is a record, not a claim; the entry must not name it.

## 13. Evidence index (all re-read at `dea5ece` this session)

- Contract: `.ufo/waves/round-50/build/ReviewEntryContract.md` §2 (head order §2.3, body §2.4, acceptance §2.8-2.9).
- Models: `sign-languages-manual-modality.md` (224 lines, PASS; sources field pattern lines 5-9), `pastoralism-animal-husbandry.md` (214 lines, PASS).
- Claims: `reports/round-52/claims.json` (C: lands, before 227/after 228, must_not_cite, falsifier; dry_run_rule).
- Registry codes: `corpus/knowledge/verification/calibration-registry.md:34-40` (header + R/C/B/H/T rows; the contract cites :35-39).
- Registry tail: `corpus/SOURCES.md:28` (11 columns), `:162` (S133 last), `:164` (`## Paths`).
- Partial owners (content verified): `linguistics/phonetics-phonology.md:197-199`; `culture-material/music-instrument-lexicon.md:98-100`; `linguistics/orality-formulaic-language.md:114,:124`; `linguistics/sound-symbolism.md:121`.
- Gate internals: `tools/gates/provenance-audit.py:61,66-84,101-104,290-348`; partition labels: `tools/harness/couples-reference-extractor.py:41`, `tools/harness/basename-couples-resolver.py:42`; topic continuation rule: `reports/round-28/readme/sweep.py:61,74-82`.
- QUALITY: `corpus/QUALITY.md` items 1-10 as quoted there (tier rule :6, separability :7, receipts :9, ordinary access :10 with `tools/check-source-access.py`).
- D diff: `git show dea5ece --unified=0` → changed sign-entry lines 83, 87, 90, 92, 93 (5 insertions, 5 deletions).

## 14. Unrun checks and limits

- No entry, README row, SOURCES row, clone or receipt was created; no landing gate ran in a counterfactual tree.
- `dry-run.py --check`, `claims-agree.py` and the sweep were not run by this seat (they need landed bytes; listed in §11 for the L1).
- No external source was opened by this seat; tier judgments for C's rows are the sourcing seats' and the L1's.
- The §9 checker is a byte-level conformance script, not a semantic review: factual claims, one-way-citation behaviour and quote accuracy still need a reading reviewer.
