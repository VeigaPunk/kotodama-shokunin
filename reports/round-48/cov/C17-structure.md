# C17 — structure diff: r47's 790-line over-build vs the right-sized 239-line assembly

- Seat: `C17` | role: verifier | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7` (`baseline_commit: "a01405d"`)
- Out path: `reports/round-48/cov/C17-structure.md` (this file; the only path this seat wrote)
- Mission (`reports/round-48/targets.json`, seat C17): diff the right-sized draft's section skeleton against r47's 790-line over-build — confirm it kept the load-bearing sections and cut the padding; measure line delta.

**One-line judgment.** The r47 over-build's skeleton is **15 H2 / 44 H3 / 240 table rows / 790 lines**, and its distinctive defect is not prose volume but **subsection fragmentation**: 44 H3 headings against a partition-wide total of **3** across all 25 live entries (median 0, max 3). The r48 assembly is **239 lines / 14 H2 / 0 H3 / 81 rows** (C02's 23-line head + a blank + C01's 215-line body), and I independently reproduced its exact bytes — **37,592 bytes, sha256 `d1de5db512de1ab2fb526012ac83ec67e7f3105e7aaf934302e16f2f2522a3d1`**, matching C13's figure. Every load-bearing block survives; the word-fossil section and the duplicated build-order/decision lists are cut. **Structural verdict PASS — with one assembly condition: C01's own head block is non-conforming (7 fields, no `- source:`), so it must be stripped, not concatenated.**

---

## 1. What I measured, and how

r47 filed the entry as four fenced fragments. I extracted each fence body mechanically (opening fence line +1 through closing fence line −1) and concatenated in the contract order C04 header → C01 → C02 → C03:

| Fragment | Fence (file:line) | Body lines | Body range in assembled file |
|---|---|---:|---|
| C04 header | `reports/round-47/cov/C04-entry-header.md:111-163` | 51 | 1–51 |
| C01 §§1–4 | `reports/round-47/cov/C01-entry-a.md:85-287` | 201 | 52–252 |
| C02 §§5–9 | `reports/round-47/cov/C02-entry-b.md:40-402` | 361 | 253–613 |
| C03 §§10–15 | `reports/round-47/cov/C03-entry-c.md:72-250` | 177 | 614–790 |
| **assembled** | | **790** | sha256 `e0c8ae56a6a9a67b142af54317363013ac08e03cb7611058c65ca5189e9913aa` |

This reproduces R03's independent measurement exactly — **739 body lines, 15 H2, 240 table rows, 790 with the head block** (`reports/round-47/review/R03-c-content.md:23-30`) — and differs from the *landable* byte source only by the 7 correction lines W02's assembler adds: **797 lines, sha256 `8fdb8bd7…`** (`reports/round-47/cov/W02-landing-spec.md:121-122`). Deltas below use 790 as the denominator and note the 797 figure where it moves the result.

The r48 bytes were measured the same way: the 23-line head at `reports/round-48/cov/C02-header.md:111-135` (sha256 `708dec15e0fb2563c258a680800e20892719c1480b0c364507c5799edf849816`, 8 fields) and the body at `reports/round-48/cov/C01-entry.md:69-298` (sha256 `e52556572341bd82545f841cee01e7bf2c581c268910ff2a6f0c2f087cf44f84`, 12-line internal head + 216 body lines). Splicing head + one blank + the body from `## 1.` with its trailing blank trimmed reproduces C13's merged entry **byte for byte**: 239 lines, 37,592 bytes, `d1de5db5…`.

Section and subsection weights were counted from H2/H3 boundaries in the assembled file; table rows = lines starting `|`; prose = non-empty lines that are not table rows or list items.

---

## 2. r47 baseline skeleton — measured

| # | Section (`## ` title, trimmed) | Lines | Prose | Table rows | H3 |
|---|---|---:|---:|---:|---:|
| 1 | The frame: what this entry owns … | 23 | 1 | 10 | 1.1 |
| 2 | What makes a map a register — five-condition test | 45 | 7 | 18 | 2.1–2.2 |
| 3 | The map-meaning mechanisms — six decisions | 80 | 8 | 17 | 3.1–3.8 (8) |
| 4 | Material and trade classes — map-object typology | 53 | 4 | 20 | 4.1–4.4 (4) |
| 5 | The survey-to-symbol chain — seven links | 108 | 26 | 27 | 5.1–5.8 (8) |
| 6 | Scarcity and prestige — the survey is expensive | 69 | 18 | 18 | 6.1–6.6 (6) |
| 7 | The mapmaker trade — five roles | 60 | 10 | 27 | 7.1–7.5 (5) |
| 8 | Provenance and charter — how a sheet becomes authority | 69 | 21 | 19 | 8.1–8.6 (6) |
| 9 | The container-name fossil | 55 | 12 | 24 | 9.1–9.4 (4) |
| 10 | Build order — question → chain → sheet → copy → warrant | 34 | 4 | 18 | 0 |
| 11 | Worked micro-example (NON-CANON) | 47 | 6 | 12 | 0 |
| 12 | Calibration bank | 35 | 4 | 16 | 0 |
| 13 | Decision record | 21 | 2 | 14 | 0 |
| 14 | Recheck triggers and known limits | 21 | 2 | 0 | 0 |
| 15 | Scope and handoff | 19 | 12 | 0 | 0 |
| | **body** | **739** | 137 | 240 | **44** |
| | head block (before §1) | **51** | 8 field lines + 41 continuation | — | — |

Subsection weight is concentrated: §5.1–5.8 alone is 108 lines; §3.1–3.8 is 80; §6–§8 are 198 combined. The eight subsections of §5 average 13.5 lines each — a full heading plus a blank line for every ~13 lines of content.

---

## 3. The over-build signature, measured against the live partition

All live figures are from the 25 files in `corpus/knowledge/culture-material/` at `a01405d`:

```
$ wc -l corpus/knowledge/culture-material/*.md | sort -n
min 103 / median 149 / max 221 (25 files; total 3756; mean 150.2)
$ python3 (H3 census over the same 25 files)
H3 count: min 0 / median 0 / max 3 / total 3
$ python3 (table-row census)
table rows per entry: median 47 / max 89 (funerary-material-culture.md)
$ python3 (header census: lines before the first `## `)
header lines: min 7 / median 12 / max 42
H2 count: min 7 / median 11 / max 14
```

| Signature | r47 | live partition | multiple |
|---|---:|---:|---:|
| File lines | 790 (797 landable) | median 149, max 221 | **5.3× median**, 3.6× max |
| H2 sections | 15 | median 11, max 14 | 1.4× median, 1.07× max |
| **H3 subsections** | **44** | **total 3 across 25 entries**, median 0 | **14.7× the whole partition** |
| Table rows | 240 | median 47, max 89 | **5.1× median**, 2.7× max |
| Head block lines | 51 | median 12, max 42 | 4.3× median |
| Source sub-bullets in the head | 39 (21 in-corpus + 18 external) | — | (see §4) |

The H3 figure is the finding R03 did not quantify. Subsection fragmentation is the mechanism by which the draft became long without becoming an essay: 44 headings and blanks consume ~88 lines (11% of the file) before any content, and each subsection is short enough to escape a per-section length check. A structure verifier should therefore test **H3 count and mean body-lines-per-heading**, not only total lines.

---

## 4. Load-bearing vs padding — section-by-section ruling

The claim's own section contract (from `reports/round-48/targets.json`, C01/C17 missions and `reports/round-44/scout/K02-gap-scout.md:220-244`) names ten load-bearing blocks: the register property, the survey-to-symbol chain, material/form classes, the mapmaker trade, provenance/charter, build order, the NON-CANON worked example, the calibration bank, recheck, and scope. r47 carries all ten; two blocks are *additional* (§6 scarcity/prestige, §9 word-fossil).

| r47 § | Ruling | Forecast cut | Evidence |
|---|---|---:|---|
| 1 frame + 1.1 boundary (23) | **keep**, compress prose; the 8-neighbour-row table is the one-owner proof | −9 | 8 rows over 10 table lines (`reports/round-47/cov/C01-entry-a.md:94-103`) |
| 2 register test (45) | **keep** the five-condition test + object table; reduce 2.2 to 3 bullets | −29 | 2.2 restates the five questions as an audit (`C01:140-152`) |
| 3 mechanisms (80) | **keep six mechanisms as tables**; cut 3.7 (4) and 3.8 (13) | −48 | 3.7 "the mechanisms are one system" is a 4-line restatement; 3.8's eight reader questions overlap 2.2's five audit questions |
| 4 form + trade classes (53) | **keep**; 4.1's "what it cannot show" column is the best anti-typology move in the draft | −33 | 8 forms at `C01:238-249`; 4.4 design rules (7) fold into one line |
| 5 survey chain (108) | **keep the 7-link table**; collapse 5.1–5.6 per-link prose into it; **cut 5.8** (14) | −82 | 5.8 `assembled:347-360` is the build order again, mapping step-for-step onto §10 `assembled:614-647` |
| 6 scarcity/prestige (69) | **compress hard** — cost stack + regimes + prestige + working/monument in ~18 lines | −51 | four tables already carry it (`assembled:365-412`); 6.5 (11) and 6.6 (6) fold into §12 |
| 7 mapmaker trade (60) | **compress** to roles + products + organization (~12 lines) | −48 | 7.5 licences/customers (13) and 7.2 org models (11) are the fat |
| 8 provenance/charter (69) | **keep** the warrant chain, authority ladder, failure modes; **cut 8.6** (15) | −49 | 8.6's "eight decisions" `assembled:544-558` duplicate §13's DR-CT-01..09 `assembled:730-750` |
| 9 word fossil (55) | **compress** — 7-row word bank + one method line + design rule; drop 9.3's 7-row ur-medium table | −44 | 13-row bank `assembled:563-582`; §9.3 repeats it as an in-world builder |
| 10 build order (34) | **keep** all 9 steps; fold the three consequences into 2 lines | −21 | `assembled:614-647` |
| 11 worked example (47) | **keep**, one update rule | −20 | r48's binding shape is 27 lines (`reports/round-48/cov/M01-example.md:27-55`) or 18 (`reports/round-48/cov/C14-example.md:128-147`) |
| 12 calibration (35) | **keep 12–14 rows**; living-practice flags to 4 lines | −17 | `assembled:695-729` |
| 13 decision record (21) | **keep 8–12 rows** | −13 | `assembled:730-750` |
| 14 recheck (21) | **compress** to 4–5 lines | −16 | `assembled:751-771` |
| 15 scope (19) | **compress** to 4–5 lines | −14 | `assembled:772-790` |
| head block (51) | **compress to 23** — one in-corpus bullet per load-bearing file, one external shelf line | −28 | r48's filed header is exactly 23 lines (`reports/round-48/cov/C02-header.md:111-135`); r47 used 39 source sub-bullets (`assembled:6-46`) |

Four blocks are **duplicates, cut outright, 31 lines total** (measured, not inferred):

1. `assembled:130` (C01:164) "The blank has three readings" ≈ `assembled:321` (C02:109) — same rule, near-verbatim. (1 line)
2. `assembled:170` (C01:204) "The boundary line is the most political mark/stroke" ≈ `assembled:322` (C02:110) — same three meanings of the stroke. (1 line)
3. `assembled:347-360` (§5.8, 14 lines) is the §10 build order in list form.
4. `assembled:544-558` (§8.6, 15 lines) is the §13 decision record in list form.

Add §3.8's 13-line reader protocol (`assembled:187-199`), which overlaps §2.2's five-question audit, and the cut-first set is **44 lines** that add no decision surface.

These per-section cuts are a **forecast**, and they do not sum to the §5 envelope: they total −522 including the 28-line head cut, which would leave 268 lines — 18 over the ceiling. That is why the §5 forecast merges section pairs and compresses §9 rather than keeping all 15. The filed draft resolves the same gap differently and better: it cuts r47 §9 (55 lines) outright instead of compressing every section, and reaches 215 body lines (§7.1). The measured draft, not this forecast, is the reference.

**Zero table rows are duplicates.** The tables earn their place; the padding is prose, subsection headings, duplicated lists, and a 39-bullet source shelf. This matters for the drafter: cutting tables to hit 250 would remove the entry's value; cutting the four duplicate blocks and the 32 excess H3 headings does not.

---

## 5. The skeleton that fits 250 lines — forecast, now validated

Constraint: **≤250 total**, with the filed r48 header at 23 lines ⇒ **body ≤227 lines**. The budget below keeps every load-bearing block and both extra blocks in compressed form, and is arithmetically exact:

| # | Target section | Lines | Table rows | Built from r47 |
|---|---|---:|---:|---|
| — | head block | 23 | — | C02 (filed) |
| 1 | Frame, one-owner rule, boundary table | 16 | 7 | §1 + §1.1 |
| 2 | The register test — five conditions, objects | 16 | 6 | §2 |
| 3 | The six meaning mechanisms | 26 | 10 | §3 (less 3.7, 3.8) |
| 4 | Form typology + trade classes | 19 | 12 | §4 |
| 5 | The survey-to-symbol chain | 24 | 13 | §5 (less 5.8) |
| 6 | Scarcity, prestige and the mapmaker trade | 18 | 10 | §6 + §7 merged |
| 7 | Provenance and warrant | 20 | 11 | §8 (less 8.6) |
| 8 | The container-name fossil | 11 | 7 | §9 (8-row bank) |
| 9 | Build order | 13 | 9 | §10 |
| 10 | Worked micro-example (NON-CANON) | 27 | 4 | §11 (M01 shape) |
| 11 | Calibration bank | 18 | 11 | §12 |
| 12 | Decision record + recheck + scope | 19 | 7 | §13–§15 merged |
| | **body** | **227** | **107** | |
| | **total** | **250** | **107** | |

Arithmetic check (recomputed, not asserted): `16+16+26+19+24+18+20+11+13+27+18+19 = 227`; `227+23 = 250`. Row check: `7+6+10+12+13+10+11+7+9+4+11+7 = 107`.

Two structural consequences the drafter must accept, or record as an exception:

- **12 H2 sections, not 15, and ≤4 H3 in the whole file.** The merge set is §6+§7 and §13+§14+§15. Because the live partition carries 3 H3 in 25 entries, any H3 above ~4 is a signal to merge, not a style choice.
- **Table density rises to 43% of the file (47% of the body)**, above the partition maximum (funerary 89/221 = 40%). That is the cost of a method entry at 250 lines. A draft at ~95 rows (38%) with a 255–265 total is the honest alternative; 240 rows at 250 lines is impossible.

**This budget was a forecast; the filed draft validates the envelope and improves on the map.** The assembled entry is 239 lines: 23 head + 1 splice blank + 215 body, with **14 H2 / 0 H3 / 81 rows**. That is 11 lines under the 250 ceiling and 12 under my 227-line body forecast, and its density (81/239 = 33.9%) is *inside* the partition maximum rather than above it — better than the forecast on both counts. The forecast's specific merge set (§6+§7, §13–§15) is **not** what the draft chose: it merges r47 §1+§2 instead and cuts r47 §9 outright, which is the better trade (remove the least load-bearing block rather than compress everything). The envelope is the contract; the section map in §7.1 supersedes the forecast's map.

---

## 6. Measured delta

| Metric | r47 raw | r47 landable | C01 fragment | **assembled r48** |
|---|---:|---:|---:|---:|
| Total lines | 790 | 797 | 228 | **239** |
| Head block | 51 (8 fields, 39 source bullets) | 51 | 12 (**7 fields — no `- source:`**) | **23 (8 fields)** |
| Body lines | 739 | 746 | 216 (215 + trailing blank) | **215** |
| H2 sections | 15 | 15 | 14 | **14** |
| **H3 subsections** | **44** | **44** | **0** | **0** |
| Table rows | 240 | 240 | 81 | **81** |
| Table density (rows/lines) | 30.4% | 30.1% | 35.5% | **33.9%** |
| Delta vs raw 790 | — | — | −562 (−71.1%) | **−551 (−69.7%)** |
| Multiple of partition max 221 | 3.6× | 3.6× | 1.03× | **1.08×** |
| Multiple of partition median 149 | 5.3× | 5.3× | 1.53× | **1.60×** |

Against the landable 797 the assembled delta is **−558 (−70.0%)**. The assembled entry stays inside the claim's ~250 ceiling and inside W01's hard `expected_lines_max: 250`; it is 18 lines above the live partition maximum, all of it in the multi-line head (the body at 215 is *below* the 221 maximum). The r47 signature is gone on every axis I measure: H3 44 → 0, rows 240 → 81, source bullets 39 → 12, duplicated blocks 0.

---

## 7. Live r48 draft — measured diff

Three states were measured; the third is the deliverable.

| State | Where | Lines | sha256 | Note |
|---|---|---:|---|---|
| C01 fragment (as filed) | `reports/round-48/cov/C01-entry.md:69-298` | 228 | `e5255657…` | 12-line **non-conforming** internal head + 216 body |
| C02 head (as filed) | `reports/round-48/cov/C02-header.md:111-135` | 23 | `708dec15…` | 8 fields, `- sources:` and `- source:` both present |
| **Assembled** | C02 head + blank + C01 body from `## 1.` | **239** | **`d1de5db5…`** | 37,592 bytes; 14 H2, 0 H3, 81 rows; matches C13's independent build (`C13-scribe.md:31-42`) |

C13's first-pass 181-line candidate was **discarded by its own author** (`C13-scribe.md:6` records the placeholder as discarded; the block is no longer present in the current bytes at sha `6e91dfc9…`). It is not a competing byte source and is not measured here.

### 7.1 Section-by-section: did it keep the load-bearing blocks and cut the padding?

The assembled entry's 14 sections (`C01-entry.md:82-297`, counted from the fragment body):

| § | Lines | Built from r47 | Ruling |
|---|---:|---|---|
| 1 The register property + five-condition test | 19 | §1 (23) + §2 (45), merged | **kept**, 68 → 19: the four choices and five conditions survive, the audit bullets do not |
| 2 One-owner boundary | 19 | §1.1 (17) | **kept and extended**: a **12-row** table (`C01-entry.md:105-118`) — r47's 8 neighbours plus `celestial-symbolism-calendars`, `craft-artisan-lexicon`, `trade-economy-lexicon`, `sacred-kingship-mythic-charter` — with the `:27` sentence stated in prose above it, so r47 B8 cannot recur |
| 3 The survey-to-symbol chain | 19 | §5 (108) | **kept**, 108 → 19: the seven links survive as a table; 5.2–5.6 per-link prose, 5.7 failure table and 5.8 restatement are cut. The error-budget bullet states the 200 m / 10 m comparison as **20×** (`C01-entry.md:135`), so r47 B1 is not carried |
| 4 Form follows the question — eight forms | 28 | §4.1 (16) + §4.2–4.4 (37) | **kept**; all 8 forms retained (r47 B9's 5-of-8 defect cannot recur) |
| 5 Projection, scale, orientation | 15 | §3.2–3.4 (33) | **kept and compressed**; the "three claims" framing merges three mechanisms without dropping any |
| 6 Material, reproduction, map trade | 16 | §6 (69) + §7 (60) | **merged**; both blocks survive at 12% of their r47 volume (129 → 16) |
| 7 Provenance and charter | 16 | §8 (69) | **kept**, 69 → 16; the warrant chain survives, 8.6's duplicate decision list is cut |
| 8 The map's silences and legal instrument | 7 | §3.1 + §10 step 6, elevated | **kept as its own section** — the political payoff gets a heading instead of a bullet |
| 9 Build order (nine steps) | 14 | §10 (34) | **kept**, 34 → 14; the nine steps and their artifacts survive |
| 10 Decision record | 11 | §13 (21) | **kept**, 21 → 11 |
| 11 NON-CANON worked example | 25 | §11 (47) | **kept**, 47 → 25; within M01's 27-line shape (`M01-example.md:27-55`) |
| 12 Calibration bank | 19 | §12 (35) | **kept**, 35 → 19 |
| 13 Recheck | 4 | §14 (21) | **kept**, compressed to triggers |
| 14 Scope | 4 | §15 (19) | **kept**, compressed to the boundary + handoff |
| — | — | **§9 word-fossil (55) — cut entirely** | **correct cut**: the 13-row etymology bank is the least load-bearing block for a 250-line method entry; the map-word fossils survive only as the `- topic:` promise, not as a section |

Section lines sum to 216 with the trailing blank, 215 without — matching the assembled body count. **All ten contract blocks named in `reports/round-48/targets.json` (C01 mission) are present: register property, survey chain, material/form classes, mapmaker trade, provenance/charter, build order, NON-CANON example, calibration bank, recheck, scope. None of the four duplicate blocks identified in §4 survives.**

### 7.2 The assembly rule, and the two places it must be applied exactly

1. **C01's own head block is non-conforming and must be stripped.** The fragment opens with a 12-line head containing only **7** field lines — `- gap filled:`, `- topic:`, `- sources:`, `- couples:`, `- verified-at:`, `- recheck:`, `- scope:` — and **no `- source:`** (measured; `C01-entry.md:70-81`). The settled header (`C02-header.md:111-135`, 23 lines) carries all **8** fields including both `- sources:` and `- source:`. C13 reaches the same ruling for two further reasons — the embedded topic line is 1,045 chars, not the 766-char seed (`C13-scribe.md:39`). Concatenating C02's head **plus** C01's internal head would produce two H1s and 251 lines.
2. **The splice must trim the body's trailing blank and insert exactly one blank separator.** Two byte-level variants were measured:
   - head + `""` + body-with-trailing-blank → **240 lines**, 37,593 bytes, sha `6fa8e3aa…` (does **not** match C13);
   - head + `""` + body-with-trailing-blank-trimmed → **239 lines**, 37,592 bytes, sha **`d1de5db5…`** (matches C13's figure).
   The difference is one line and one byte; an assembler that concatenates naively lands at 240 and drifts the pin. This is a structural requirement, not a cosmetic one, because W01's manifest pins the sha.

### 7.3 Canonical byte source — resolved, with the pin

C13's §2 (`C13-scribe.md:31-42`) and my independent reproduction agree: **C02 head + C01 body**, and the merged bytes are **239 lines / 37,592 bytes / sha256 `d1de5db512de1ab2fb526012ac83ec67e7f3105e7aaf934302e16f2f2522a3d1`**. That resolves the canonical-source question this seat would otherwise have filed as `to-verify`. The integrator must pin this sha and must **not** append the component fragments (M01's example, M02's calibration, E01's boundary): C01's body already integrates those three sections, and appending would duplicate them and break the length budget (`C13-scribe.md:41`).

**Re-run recipe (copy-paste, from the lane root).** It reproduces the assembled skeleton and sha from the two filed fragments.

```bash
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
python3 - <<'PY'
import re,hashlib
def blocks(p):
    src=open(p,encoding='utf-8').read().splitlines();out=[];inb=False
    for i,l in enumerate(src,1):
        if re.match(r'^`{3,}',l):
            if not inb: inb=True;s=i;lang=l.lstrip('`').strip();buf=[]
            else:
                inb=False
                if lang in ('markdown','md'): out.append((s,i,buf))
        elif inb: buf.append(l)
    return out
head=[b for b in blocks('reports/round-48/cov/C02-header.md') if len(b[2])<40][0][2]
c1=blocks('reports/round-48/cov/C01-entry.md')[0][2]
i=[k for k,l in enumerate(c1) if l.startswith('## 1.')][0]
body=c1[i:]
while body and body[-1]=='': body.pop()
merged=head+['']+body
txt='\n'.join(merged)+'\n'
h2=[l for l in merged if l.startswith('## ')]
h3=[l for l in merged if l.startswith('### ')]
rows=[l for l in merged if l.startswith('|')]
print('lines',len(merged),'bytes',len(txt.encode()),'H2',len(h2),'H3',len(h3),'rows',len(rows))
print('sha256',hashlib.sha256(txt.encode()).hexdigest())
print('PASS length' if len(merged)<=250 else 'FAIL length >250',
      '| PASS H3' if len(h3)<=4 else '| FAIL H3 >4',
      '| body',len(body),'<= 221' if len(body)<=221 else '> 221')
PY
```

The 250 threshold is not this seat's invention: the r48 landing spec makes it a hard assembler failure — `"expected_lines_max": 250` (`reports/round-48/cov/W01-landing-spec.md:101`) and `if body > manifest["expected_lines_max"]: fail(... "partition discipline")` (`W01-landing-spec.md:171-172`), with a WARN above the live max of 221 (`W01:214`). The assembled 239 is a **WARN on the 221 band, PASS on the 250 gate** — 11 lines of headroom, no manifest change needed.

Two filed artefacts are **not** evidence about the assembled bytes: C11 staged a **136-line fixture** to prove the sweep is green at 224 (`reports/round-48/cov/C11-sweep.md:52`) — inside the live band, and not C01's bytes by its own statement (`C11-sweep.md:6`); W02's README diff leaves the entry length untouched (`reports/round-48/cov/C10-readme.md:9`).

---

## 8. What I did not verify

- **Whether the compressed sections preserve content.** A 239-line shape can keep every decision surface in principle; whether a section's compression drops a rule is C12's depth judgment and R03's content review, not a line count. I verified section presence and line weight, not section adequacy.
- **Whether every boundary row and citation resolves.** Measured: 12 rows (`C01-entry.md:105-118`), the `:27` prose sentence present. C04/C15/C07 own the per-row anchor check; I did not re-read every row's cited line.
- **The per-section truth of `C13`'s B1–B9 table.** I confirmed the structural places where B1 (20×), B5/B6 (cross-refs) and B9 (8-of-8 forms) would appear and that the draft's bytes have the right shape; C03/C14 own the arithmetic and example verdicts on the assembled bytes.
- **The landable 797-byte correction set.** I used W02's reported 797/`8fdb8bd7…` (`reports/round-47/cov/W02-landing-spec.md:121-122`) as a second delta denominator; I did not rebuild the corrected bytes.
- **Any external source.** No network; no bibliographic claim is made here.

---

## 9. Commands and write surface

All commands run 2026-10-19 from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ find corpus/knowledge -name '*.md' | wc -l
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ wc -l corpus/knowledge/culture-material/*.md | sort -n
min 103 / median 149 / max 221
$ python3 (H3 census, 25 files)   -> total 3, median 0, max 3
$ python3 (table-row census)      -> median 47, max 89
$ python3 (header census)         -> median 12, max 42; H2 median 11, max 14
$ python3 (fence extraction, r47) -> header 51; C01 201; C02 361; C03 177; assembled 790
$ sha256sum .scratch/c17/r47-assembled.md
e0c8ae56a6a9a67b142af54317363013ac08e03cb7611058c65ca5189e9913aa
$ python3 (skeleton)              -> 15 H2, 44 H3, 240 table rows, 739 body lines
$ python3 (r48 extraction)
  C02-header.md:111-135  lines=23  fields=8 sha=708dec15…
  C01-entry.md:69-298    lines=228 header=12 body=216 H2=14 H3=0 rows=81
                         fields=7 (no `- source:`) sha=e5255657…
$ python3 (assembly reproduction)
  head+blank+trimmed body -> lines 239 bytes 37592
  sha256 d1de5db512de1ab2fb526012ac83ec67e7f3105e7aaf934302e16f2f2522a3d1
$ python3 (delta)                 -> assembled −551 (−69.7%) vs 790; C01 fragment −562 (−71.1%)
```

**Write surface:** this file only — `reports/round-48/cov/C17-structure.md`, plus disposable analysis output under `.scratch/c17/`. No `corpus/**`, `tools/**`, `reports/round-1..47/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was edited or staged. No git commit/push, no install, no network, and no `reports/round-*/run-validation.py` execution.
