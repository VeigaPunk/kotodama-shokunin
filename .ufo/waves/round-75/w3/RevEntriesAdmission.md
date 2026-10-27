# RevEntriesAdmission — round-75 wave 3 (falsify): the three landed entries as admissions

**Seat:** `RevEntriesAdmission` (leaf; no delegation, no background jobs, no `task`).
**Lane:** `/home/vgpnk/Projects/shokunin/kotodama-shokunin`. **Fleet root:** `/home/vgpnk/Projects/shokunin`.

| pin | revision |
|---|---|
| base | `f556d1049fe651d3d63975600b13acd9fb686f15` |
| freeze | `5d0167464309d8133991b30f7d7a7011a6a0fd14` |
| claim Ca lands | `012e8d3c8b92f47c734f735d58d118d574fe6a14` |
| claim C lands (the entries' landing) | `4f5e3b2535c2c06c51627dc2736c40183847cae1` |
| lane main at dispatch | `82ced5cc205a116516e40895c4241415d54dae52` (telemetry + w3 spec only; `git log --oneline 4f5e3b2..main` = 1 commit, and `git diff --stat 4f5e3b2..82ced5c -- corpus/ tools/` is empty) |

**Scope:** the three entries claim C lands — `corpus/knowledge/myth-symbol/narrative-structure-frameworks.md` ("E1"), `...amend-2026-10-23.md` ("E2"), `...amend-2026-10-23b.md` ("E3") — attacked as admissions under `corpus/QUALITY.md` criteria 1–27 and `PROVINCE.md`. Bytes reviewed at the landing; verified byte-identical at lane main (§3.9).

**Verdict: PARTIAL.** E2 **ADMIT-AS-IS**; E3 **ADMIT-AS-IS**; E1 **WITH-CUTS** (one defect, F1: two §10 calibration rows use status labels outside the vocabulary the entry itself declares — a relabel, not a refusal). Nothing rises to REFUSE.

**Tooling:** nothing installed. **Scratch:** `/fast/scratch/hyaku/kotodama-r75/RevEntriesAdmission/` (clone `lane` at `4f5e3b2` + `check_admission.py`), deleted after the receipts below were copied here; nothing citable points at it. No lane file written except this report; no fleet file, sibling lane, jj/git state, shokuknow tree or scripts/templates touched. No fixture commits were needed.

---

## 1. Receipts

### 1.1 Clone discipline

```
D=/fast/scratch/hyaku/kotodama-r75/RevEntriesAdmission; mkdir -p "$D"
git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane"
git -C "$D/lane" rev-parse --show-toplevel   → /fast/scratch/hyaku/kotodama-r75/RevEntriesAdmission/lane  (asserted equal to "$D/lane")
git -C "$D/lane" checkout -q -B main 4f5e3b2535c2c06c51627dc2736c40183847cae1
git -C "$D/lane" rev-parse HEAD              → 4f5e3b2535c2c06c51627dc2736c40183847cae1
```

### 1.2 Criterion 15 — cited-line shape (QUALITY 15), run on each entry in the clone

```
$ python3 -B $L/tools/check-cited-lines.py $L/corpus/knowledge/myth-symbol/narrative-structure-frameworks.md
CITED-LINES: 0 finding(s) in 1 file(s)          exit=0
$ ... narrative-structure-frameworks.amend-2026-10-23.md
CITED-LINES: 0 finding(s) in 1 file(s)          exit=0
$ ... narrative-structure-frameworks.amend-2026-10-23b.md
CITED-LINES: 0 finding(s) in 1 file(s)          exit=0
```

No MULTI-ID and no TABLE-ID finding on any entry: every line that cites carries exactly one distinct S-id, and no table row carries one. (The tool came from the same clone at the landing; claim C does not touch `tools/` — commit stat of `4f5e3b2` lists no `tools/` path — so the lint is not the graded object judging itself.)

### 1.3 Mechanical admission checks (script output, abridged to the decided values)

Per entry — header order, placeholders, topic single-line, README verbatim match, word counts, `(to-verify)`, S-id inventory, couples resolution:

```
===== narrative-structure-frameworks.md
header fields: [source ×5, verified-at, recheck, ground, topic, gap filled, sources, couples, scope]
all-header-lines-before-first-##: True          topic-count: 1 (single physical line)
readme-row-verbatim-match: True
words-total: 5014 | words-from-first-##: 4247 | floor-478-ok: True
(to-verify) count: 0
s-ids: [S885, S888, S889, S890, S893] | outside-S885-S893: []
couple-targets: 7 | missing: []
===== narrative-structure-frameworks.amend-2026-10-23.md
header fields: [source ×3, verified-at, recheck, ground, topic, gap filled, sources, couples, scope]
all-header-lines-before-first-##: True          topic-count: 1 (single physical line)
readme-row-verbatim-match: True
words-total: 3951 | words-from-first-##: 3401 | floor-478-ok: True
(to-verify) count: 0
s-ids: [S885, S886, S887] | outside-S885-S893: []
couple-targets: 6 | missing: []
===== narrative-structure-frameworks.amend-2026-10-23b.md
header fields: [source ×3, verified-at, recheck, ground, topic, gap filled, sources, couples, scope]
all-header-lines-before-first-##: True          topic-count: 1 (single physical line)
readme-row-verbatim-match: True
words-total: 3779 | words-from-first-##: 3135 | floor-478-ok: True
(to-verify) count: 0
s-ids: [S885, S891, S892] | outside-S885-S893: []
couple-targets: 4 | missing: []
```

No placeholder token (`TODO/TBD/FIXME/XXX/n/a/?/—`) and no `<...>` in any header value (script printed none). Every S-id cited resolves to a lane row this round added (S885–S893); no campaign-namespace (staged S9xx) id survives in any entry. Registry rows S885–S893 exist and their URL cells match the URLs named in the entries' `- source:` lines (checked id-by-id).

### 1.4 Header field spelling (`gap filled` vs the leg prose `gap-filled`)

```
$ grep -rhoE '^- (source|sources|verified-at|recheck|ground|topic|gap[ -]filled|couples|scope):' \
    $L/corpus/knowledge --include='*.md' | sort | uniq -c | sort -rn
 252 - topic:   251 - verified-at:   251 - recheck:   248 - sources:   246 - couples:
 211 - source:   55 - gap filled:    36 - scope:       9 - ground:
```

The space spelling is the live corpus convention (55×; zero hyphenated; the round-74-adopted `worldbuilding-setting-practice.md` uses it too). The counter normalizes before comparing (`accept-c.py:247-249 norm_label` strips non-alphanumerics; `:1191,1209` compare normalized labels), so `- gap filled:` satisfies the frozen `HEADER_FIELDS` (`:198-199`). Cosmetic prose-vs-file variance only; no admission consequence.

---

## 2. Per-criterion results (QUALITY 1–27 + PROVINCE)

| criterion | E1 | E2 | E3 | evidence |
|---|---|---|---|---|
| 1 provenance (cited, checkable; no laundering) | PASS | PASS | PASS | every section cites S-ids at page scope; `(to-verify)` = 0 in all three; unverifiable items are refused, not asserted (E1 §12; E2 §7; E3 §7) |
| 1 header first, field order, no placeholders | PASS | PASS | PASS | §1.3: source×n → verified-at → recheck → ground → topic → gap filled → sources → couples → scope, all before the first `## ` |
| 2 calibration vocabulary | **WITH-CUTS (F1)** | PASS | PASS (note N2) | E1:19 declares six statuses; E1:171 and E1:173 use two undeclared ones. E2 §6 and E3 §6 rows all sit in mainstream/contested/discredited (E3:108 is a refusal-of-support, not a status) |
| 2 pop-mythography flagged on first use | PASS | PASS | PASS | Campbell appears only as the coupled, not-re-opened shelf (E1 `- couples:`); the five codes are calibrated *contested* on the secondary literature's own words (E3 §3, §6); no strong-Whorf/glottochronology/Frazer anywhere |
| 3 coupling line | PASS | PASS | PASS | `- couples:` present in all three; all 17 named targets exist at the landing (0 missing) |
| 4 usability | PASS | PASS | PASS | E1: decision/do-not tables, three-axis tables, 10-step decision sequence; E2: per-cut tables, three design orders, §8 checklist; E3: ordered checklist, two decision tables, worked example. No essays-only entry |
| 5 canon hygiene | PASS | PASS | PASS | all three end at the world-bible handoff with explicit refusal lines (E1 §11 "Nothing here decides a culture's story"; E2 scope + §9.9; E3 scope + §5/§7); no line rules on rights, licence or permission (each scope line says so) |
| 10 opened by ordinary means (entry-side) | PASS | PASS | PASS | entries assert only what their rows record: plain GETs (E1 verified-at line; E2 §7) and two challenges met-and-not-passed with archive copies of the same path (E3 §7: S891 bot challenge → 2004-12-20 capture; S892 HTTP 403 → 2025-11-11 capture) — exactly criterion 10's routed-around-by-ordinary-copy shape; Persée's walled PDF endpoint is named as met-and-not-passed with no sentence resting on it (E2 §7) |
| 15 cited-line shape | PASS | PASS | PASS | §1.2: `CITED-LINES: 0 finding(s)` ×3, exit 0 |
| 16 body-scoped quotation | PASS | PASS | PASS | prose-and-table markdown only; no captions, image alt/title/aria attributes, or data-* carriers exist in any entry |
| word floor (478 = smallest base entry) | PASS | PASS | PASS | 5014 / 3951 / 3779 total words |
| `- topic:` single line | PASS | PASS | PASS | topic-count 1 ×3; each one physical line |
| README index row verbatim | PASS | PASS | PASS | the myth-symbol row text under `` - `name.md` — `` equals the entry's `- topic:` text byte-for-byte ×3 |
| PROVINCE scope fit vs lore-shokunin | PASS | PASS | PASS | entries generate/record method and stop at `synthesis/worldbible-integration-contract.md`; lore's PROVINCE (fleet root `lore-shokunin/PROVINCE.md`, "Adjacent") names exactly that contract as kotodama's handoff surface. No canon claim, no consistency-verification claim, no rights/attribution ruling is made in any entry — kotodama does not absorb lore's refusal surface, and vice versa |

---

## 3. Defects

**F1 — (minor, E1 only, WITH-CUTS trigger) Two §10 calibration rows use status labels the entry's own §1 does not declare.**
`narrative-structure-frameworks.md:19` declares the calibration vocabulary: mainstream, contested, discredited, plus three scope statuses (taught method, proposal, tier-C vocabulary), and says "The statuses are this entry's calibration". Then:

- `:171` `| 起承転結 | received compositional convention | recorded as the minimal unit of the quest layer, not as a demonstrated universal |`
- `:173` `| the narratology of narrative generation | research programme | the paper describes an area and a vision, not a settled result |`

Neither "received compositional convention" nor "research programme" is one of the six declared statuses, and neither row names mainstream/contested/discredited, so QUALITY 2's "names its status: mainstream / contested / discredited, with the reason" is unmet on those two rows. The body already carries the material for the fix: §6 and §12 call the three-layer format and the generation programme "proposals", and :158 says "step 9 rests on a research programme's self-description".
**Exact cut (E1 → ADMIT-AS-IS after cut):** relabel `:171` status to `mainstream as a received convention, contested as a demonstrated universal` and `:173` status to `proposal (a research programme's self-description, not a settled result)`. No other byte changes. (Converges with the independent finding in `.ufo/waves/round-75/w3/CritFactBase2.md` finding 1.)

**F2 — (nit, E2, no cut required) §1 line 21 states the universality harder than §6 calibrates it.** `amend-2026-10-23.md:21` ""Does this people tell stories?" is not a design variable; on this page there is no people without them" presents Barthes's page-1 assertion as operative design guidance, while `:##6` calibrates the same claim "mainstream as an observation, contested as a law … no count or sample is offered". The sentence is explicitly grounded in the page and the calibration is carried in the same file, so this is a tension, not a defect; recording it so the next revision can weld the two (e.g. "…is almost not a design variable; §6 grades the universality contested as a law").

**N2 — (note, E3, no cut) `:108` "A universal narrative grammar — outside what these pages support"** is a refusal-of-support with its reason, not a fourth calibration status; it satisfies QUALITY 2's intent (flagging universalism) and is left as-is. Related residual: `.ufo/waves/round-75/w3/ScoutReopenS891.md` flags one E3 sentence ("A design order follows: … not five stages to build in order …") as beyond the page; the sentence carries an explicit inference marker ("A design order follows"), which places it under the entry's own voice rather than under S891 — noted here so the disposition is on the record, not re-litigated.

---

## 4. Residual risk and verification gaps

- **No source was re-opened by this seat** (out of seat scope; the ScoutReopenS885–S893 siblings cover the span-level audit). Their hash/quote receipts and their row-side findings (S892 used-by mismatch; S885/S887/S893 byte-count drift between receipt and fresh fetch) are row/lesson-side defects outside these three files' admission scope and are cross-referenced, not duplicated here.
- E1's "received compositional convention" row (F1) is also load-bearing for the entry's *topic* line (`起承転結 held as the minimal completable unit of the quest layer`); the relabel does not touch the topic line, and `.ufo/waves/round-75/w3/CritFactBase2.md` finding 2 grades the underlying quest-layer claim separately.
- The claims.json ENTRIES leg prose spells the field `gap-filled` while files spell `gap filled` (§1.4); the counter's `norm_label` closes the gap today, but a future counter that compares labels verbatim would fail every entry in the corpus — one-line note for the counter's next revision, not a round-75 defect.
- LSP: not applicable (prose corpus; no language server answers these paths); all definition/reference checks above were done by git-show byte comparison and the corpus's own lint, whose outputs are quoted.

## 5. Disposition summary

| entry | verdict | exact cut |
|---|---|---|
| `narrative-structure-frameworks.md` | **WITH-CUTS** | F1: relabel §10 statuses at `:171` and `:173` into the six-status vocabulary declared at `:19` |
| `narrative-structure-frameworks.amend-2026-10-23.md` | **ADMIT-AS-IS** | none (F2 recorded as a note) |
| `narrative-structure-frameworks.amend-2026-10-23b.md` | **ADMIT-AS-IS** | none (N2 recorded as a note) |

Overall round-75 w3 admission verdict: **PARTIAL** — one minor, mechanically fixable defect across the three landed entries; provenance-header shape, criterion-15 cited-line shape, word floor, single-line topics, README verbatim rows, coupling, usability, canon hygiene, ordinary-means provenance and lore-shokunin scope fit all hold on committed bytes.

Scratch `/fast/scratch/hyaku/kotodama-r75/RevEntriesAdmission/` deleted after this report was written; the receipts above are the retained record. Nothing installed; no verification left running.
