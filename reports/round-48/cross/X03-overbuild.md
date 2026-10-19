# X03 — over-build critic (claim C): is the r48 draft r47's bloat renamed?

- Seat: `X03` | role: critic | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: `git rev-parse HEAD` → `a01405dd36367292255c2652ac0a601f4cd6a0af` (`a01405d`), equal to `reports/round-48/claims.json:7`
- Read cut: `2026-10-19T19:42Z`, 48 files under `reports/round-48/`; at that cut **no entry body existed** (`find reports/round-48 -name 'C01*' -o -name '*entry*'` → 0). The body landed between the cuts and was measured at the second cut, `2026-10-19T19:46Z` (`reports/round-48/cov/C01-entry.md`, sha256 `4c2815a766f12926ba14e14e2b164a8f65245a246223ae4258993e0a831c272d`, fenced entry `:70-297`). Both measurements are reported; where they differ, the filed entry governs.
- Out path: `reports/round-48/cross/X03-overbuild.md` (this file only). I drafted no cartography bytes in r47 or r48 and edited no fragment.

**Verdict in one line.** **No — the r48 entry is not r47 renamed.** The fenced entry is **227 lines / 4,545 words / 14 H2 / 0 H3 / 81 table rows**: 0.95× the partition's median word count (4,768), 1.03× its longest entry (221), and **zero H3** against r47's 44 (which were 81.5% of all H3 in the 223-entry corpus). Every arithmetic claim recomputes, 25/25 in-corpus anchors resolve, there are no duplicate bullets, and the detector's B1/B2/B5/B7/B8/B9 legs are clean. The over-build risk has **migrated from length to duplication at integration**: the round now holds two headers (topics of 775 and 1,054 characters), two boundary tables (13 vs 12 rows), two calibration banks (10 vs 11 rows) and two examples (27 vs 25 lines). Appending instead of choosing yields **341 lines**; and C01's 1,054-character `- topic:` does **not** equal the r44 seed (766-character value) that the README row carries, so using it would fail the sweep with `topic_mismatch`.

---

## 1. The envelope, measured (not carried)

All commands from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

| Metric | Live value at `a01405d` | How measured |
|---|---|---|
| corpus entries | **223** | `find corpus/knowledge -name '*.md' \| wc -l` |
| culture-material entries | **25** | `ls corpus/knowledge/culture-material/*.md \| wc -l` |
| partition lines | min **103**, median **149**, max **221**, mean **150.2** | `wc -l` over the 25 files; 3,756 / 25 = 150.24 |
| partition words per entry | min 2,914, median **4,768**, max **12,504**; next highest **7,047** (`fire-fuel-light.md`), then 6,895, 6,023, 5,786 | `len(text.split())` per file |
| partition words per line | median **33.5** | derived per file, median of the 25 ratios |
| partition H2 sections | **265** | count of `^## ` |
| partition H3 subsections | **3**, all in `ritual-garments.md` | count of `^### ` |
| H3 across all 223 entries | **54** | count of `^### ` over `corpus/knowledge/*/*.md` |
| header block (lines before first `## `) | lines median **12**, max **42**; words median **1,002**, Q3 **1,650**, max 6,451 | line scan per file |

The envelope is the test — and it must read **words as well as lines**, because a line count can be compressed without cutting content (the r48 header: 23 lines but 1,827 words, §7) while a genuine cut reduces both (the entry: 227 lines and 4,545 words, §3.1).

---

## 2. r47 re-measured, sha-pinned

Fence extraction (longest ```markdown block per fragment, opening and closing fences dropped):

| Fragment | Body lines | Words | Table rows | sha256 (file) |
|---|---:|---:|---:|---|
| `reports/round-47/cov/C04-entry-header.md:111-163` | 51 | 2,522 | 0 | `cb5a7489676de47e…` |
| `reports/round-47/cov/C01-entry-a.md:85-287` | 201 | 5,455 | 65 | `cfb429556173734…` |
| `reports/round-47/cov/C02-entry-b.md:40-402` | 361 | 7,396 | 115 | `5f5683a72ea06d4e…` |
| `reports/round-47/cov/C03-entry-c.md:72-250` | 177 | 4,750 | 60 | `4b699e0653711527…` |
| **assembled** | **790** | **20,123** | **240** | — |

Body only (head excluded): 739 lines / 17,601 words — reproduces R03 (`reports/round-47/review/R03-c-content.md:96`) and Ca02 (`reports/round-48/calib/Ca02-overbuild.md:38`). Structure: **1 H1 / 15 H2 / 44 H3**. The 44 H3 are **81.5% of the 54 H3 in the entire 223-entry corpus** (44/54); the culture-material partition has 3. This is the sharpest single over-build indicator in r47: the draft did not merely run long, it **fragmented into subsections no house entry uses**.

### 2.1 Section ledger — does each section earn its place?

Density = table rows per line (decision content per line). Verdict uses three tests: decision density, unique content, and contract necessity.

| r47 § | Lines | Words | Tbl | Density | Verdict |
|---|---:|---:|---:|---:|---|
| head | 51 | 2,522 | 0 | 0.00 | keep the fields, cut the 18-bullet shelf and sha digests |
| 1 frame | 23 | 861 | 10 | 0.43 | keep (boundary argument is contract) |
| 2 register test | 45 | 1,237 | 18 | 0.40 | keep; cut per-object commentary |
| 3 mechanisms | 80 | 2,014 | 17 | 0.21 | **cut ~60%** — §10 re-describes it |
| 4 typology/trade | 53 | 1,343 | 20 | 0.38 | keep; 8-form table is load-bearing |
| 5 chain | 108 | 2,509 | 27 | 0.25 | **cut ~70%** — instrument history, not method |
| 6 scarcity | 69 | 1,277 | 18 | 0.26 | merge into trade |
| 7 mapmaker trade | 60 | 1,166 | 27 | 0.45 | keep (highest density in the body) |
| 8 provenance | 69 | 1,205 | 19 | 0.28 | keep warrant chain + failures |
| 9 word fossils | 55 | 1,239 | 24 | 0.44 | keep or cut whole; do not keep at half length |
| 10 build order | 34 | 1,009 | 18 | 0.53 | keep; sequence, do not re-describe |
| 11 example | 47 | 1,140 | 12 | 0.26 | keep; state one rule |
| 12 calibration | 35 | 1,086 | 16 | 0.46 | keep |
| 13 decision record | 21 | 683 | 14 | 0.67 | fold into §7/§8; no standalone |
| 14 recheck | 21 | 430 | 0 | 0.00 | compress to the header field |
| 15 scope | 19 | 402 | 0 | 0.00 | compress to 2 lines |

Five sections (§3+§5+§6+§7+§8) hold **386 of 790 lines (48.9%)**; §5 alone is 13.7%. The tables are not the problem (240 rows over 790 lines is house-normal density); the prose around them is. Two measured duplicate pairs survive assembly: assembled `:130` vs `:321` ("the blank has three readings") and `:170` vs `:322` ("the boundary line is the most political stroke") — the same rule stated twice in two fragments' registers, exactly the seam R03 flagged (`R03-c-content.md:94`).

### 2.2 Defect density

Nine blocking defects (B1–B9) over 790 lines = **1 per 87.8 lines**. Origin split, from the filed bytes:

- **Body-surface (7):** B1 arithmetic, B2 gap count, B4 ladder anchor, B5 section pointers, B7 worked-example rule, B8 competing ownership, B9 5-of-8 table. These would have landed in corpus bytes.
- **Assembly-surface (2):** B3 (C02's false accusation against C01's quote) and B6 (C01's handoff says §9 for §8). Both are cross-fragment artifacts; a single-author draft has no surface on which they can form.

That split is the argument for right-sizing: **the over-build and the assembly seam are the same failure** — four seats each wrote a complete mini-entry, and no one measured the concatenation until review.

---

## 3. The r48 entry as filed — measured, and the counterfactual

### 3.1 The entry, four dimensions

`reports/round-48/cov/C01-entry.md`, fenced block `:70-297`, sha256 `4c2815a7…`:

| Metric | r48 entry | r47 entry | Partition reference |
|---|---:|---:|---|
| lines | **227** | 790 | median 149, max 221 |
| words | **4,545** | 20,123 | median 4,768, max 12,504 |
| words/line | **20.0** | 25.5 | median 33.5 |
| H1 / H2 / H3 | **1 / 14 / 0** | 1 / 15 / 44 | H3 total 3 (partition), 54 (corpus) |
| table rows | **81** | 240 | — |
| table density | **0.36** | 0.30 | — |

Against r47: **−71.3% lines, −77.4% words**. Against the partition: **1.52× the median lines but 0.95× the median words** and 1.03× the longest entry. The word count being *below* the median is the decisive result: the draft did not just compress lines, it cut content.

Per-section ledger (H2 sections; the head is 12 lines / 1,003 words):

| § | Lines | Words | Tbl | | § | Lines | Words | Tbl |
|---|---:|---:|---:|---|---|---:|---:|---:|
| 1 register property | 19 | 311 | 0 | | 8 silences/legal | 7 | 133 | 0 |
| 2 boundary | 19 | 320 | 14 | | 9 build order | 14 | 127 | 0 |
| 3 chain | 19 | 386 | 9 | | 10 decision record | 11 | 150 | 8 |
| 4 eight forms | 28 | 401 | 10 | | 11 example | 25 | 464 | 5 |
| 5 projection/scale | 15 | 290 | 7 | | 12 calibration | 19 | 323 | 13 |
| 6 material/trade | 16 | 244 | 8 | | 13 recheck | 4 | 89 | 0 |
| 7 provenance | 16 | 254 | 7 | | 14 scope | 3 | 50 | 0 |

Every section is 3–28 lines; none dominates; there is no H3 fragmentation. This is the shape K01's spec asked for (`K01-rightsized-spec.md:79-94`), reached without appending the fragment blocks.

### 3.2 B1–B9 on the entry bytes: all nine shapes absent

| Defect | Check on the filed entry | Result |
|---|---|---|
| B1 arithmetic | 10 recomputations: 0.2 mm at 1:5,000 = 1 m; 1:25,000 = 5 m; 1:24,000 = 4.8 m; 1:50,000 = 10 m; 1:250,000 = 50 m; 1 cm bar at 1:50,000 = 500 m; at 1:250,000 = 2.5 km; 1% of 100 paces × 0.75 m = 0.75 m; centuria 710 m square = 50.4 ha; sec 60° = 2 | **pass** |
| B2 gap count | `grep -rni 'cartograph'` → 2 lines / 2 files, stated as such; `:71` named as the disclaimer without the token | **pass** |
| B3 quote | `naming-systems.md:70` quoted verbatim, "not corrected" stated in the sources line | **pass** |
| B4 anchor | ladder cited `:54-65`; `:44` explicitly called the material-grading row | **pass** |
| B5/B6 pointers | §3, §5, §12, §13 pointers resolve to the sections they name; one draft, no cross-fragment handoff | **pass** |
| B7 one rule | "Update rule (stated once)" plus a storm test; the "if the rule were…" table is a labelled counterfactual, not a second rule | **pass** |
| B8 competing ownership | `cosmology-cosmography.md:27` quoted and dispositioned in `- gap filled:` and §2 | **pass** |
| B9 form table | one table, **eight** rows, matching the eight forms named in `- topic:` | **pass** |

Also: 25/25 in-corpus anchors resolve with no out-of-range line; 14 `couples:` paths resolve; 0 duplicate-bullet pairs at the 4-word-shingle Jaccard ≥0.35 screen.

### 3.3 The counterfactual — what assembling the fragments would have produced

Before the body landed, the filed blocks measured 114 lines / 5,021 words (header 23/1,827; E01 boundary 32/893; M02 calibration 32/1,349; M01 example 27/952). At K01's allocations for the unwritten sections, that composes to **253 lines** (3 over the ≤250 tolerance) and, at the partition median density, **≈9,376 words** — above every culture-material entry except the funerary outlier. That projection did **not** materialize because C01 wrote an integrated body rather than concatenating the blocks. The counterfactual is kept here for one reason: it shows the composition mechanism is still live, and §3.4 shows the fragments are still in the round.

### 3.4 The live risk is duplication, not length

The round now holds two versions of four sections. They are alternatives, not complements:

| Section | Fragment (filed) | C01 entry (filed) | If appended |
|---|---|---|---|
| head / `- topic:` | C02: 23 lines, topic **775 chars** (seed, sha `9424fb81…`) | C01: 12 lines, topic **1,054 chars** (sha `1727a550…`) | duplicate H1 and `- topic:` |
| boundary | E01: 32 lines, **13** rows | §2: 19 lines, **12** rows | duplicate table |
| calibration | M02: 32 lines, **10** rows | §12: 19 lines, **11** rows | duplicate bank |
| example | M01: 27 lines | §11: **25** lines | duplicate example |

Appending all four to C01's 227-line entry yields **341 lines** (1.54× the partition max) and duplicate sections. Replacing C01's head with C02's yields **238 lines / ≈5,369 words** — still inside both the line tolerance and the word envelope. The integrator must therefore **choose C01's integrated entry and use C02's head block as the header replacement**, treating E01/M02/M01 as verification cross-checks, not as content to append.

### 3.5 The topic collision is a hard integration condition

The sweep compares the README row description to the entry's `- topic:` text (`reports/round-28/readme/sweep.py:60-61,139-146`, class `REWRITE`). Measured:

- r44 seed (`reports/round-44/scout/K02-gap-scout.md`, the `- topic:` line): 775 chars, sha256 `9424fb81…`; value 766 chars.
- C02 header (`C02-header.md:114`): **byte-equal to the seed** (775 chars, same sha).
- C10 README row (`C10-readme.md:132`): description **byte-equal to the seed value** (766 chars, verified against the row regex).
- C01 entry (`C01-entry.md`, head): a rewritten **1,054-char** topic, sha `1727a550…`, **not** the seed.

Using C01's topic with C10's row would fail the sweep with `topic_mismatch` on the new entry. The entry must carry the seed text (C02's line) verbatim; C01's expanded topic is the best material to lose.

### 3.6 Example length, re-checked against C14

C14's W9 is "12–20 lines target, ≤25 hard ceiling" (`C14-example.md:84`). C01's §11 is **25 lines** — at the ceiling, inside it, above the target. M01's block is **27** — 2 over the ceiling. If the integrator keeps C01's §11 (recommended, since it is the one inside the entry), W9 passes on the hard ceiling and the target miss is a note, not a blocker; M01's block then has no landing surface and should remain a review artifact.

---

## 4. The B1–B9 recurrence detector, validated on r47

The detector is a single script (below). It reads a draft path, extracts the fenced entry if present, and writes JSON with one leg per defect shape. It must be run on the **assembled** entry at apply time.

```python
#!/usr/bin/env python3
# usage: python3 check.py <assembled-entry.md>
import re, sys, subprocess, json, hashlib
from pathlib import Path
D = Path(sys.argv[1]); L = D.read_text().splitlines()
def fence(lines):
    for i,l in enumerate(lines):
        if re.match(r'^```+markdown\s*$', l):
            for j in range(i+1,len(lines)):
                if re.match(r'^```+\s*$', lines[j]): return lines[i+1:j], i+1
    return lines, 0
body, off = fence(L); T = '\n'.join(body); R = {}
heads=[(i,len(m.group(1)),m.group(2)) for i,l in enumerate(body) for m in [re.match(r'^(#{1,3}) +(.+)$',l)] if m]
secs=[]
for j,(i,lvl,t) in enumerate(heads):
    if lvl>2: continue
    end=next((i2 for (i2,l2,_) in heads[j+1:] if l2<=lvl), len(body)); seg=body[i:end]
    secs.append(dict(title=t,lines=len(seg),words=len(' '.join(seg).split()),tbl=sum(1 for x in seg if x.strip().startswith('|'))))
R['len']=dict(lines=len(body),words=len(T.split()),h2=sum(1 for h in heads if h[1]==2),h3=sum(1 for h in heads if h[1]==3),
              table_rows=sum(1 for x in body if x.strip().startswith('|')),over_250=len(body)>250,
              over_7000_words=len(T.split())>7000,sections=secs)
# B1: 0.2 mm x 1:50,000 vs "ten/twenty times"
R['B1']=[]
for i,l in enumerate(body):
    m=re.search(r'(\d+(?:\.\d+)?)\s*mm',l); s=re.search(r'1\s*:\s*([\d,]+)',l); c=re.search(r'(ten|twenty|thirty|\d+)\s*(?:times|×)',l)
    if m and s and c:
        g=float(m.group(1))*int(s.group(1).replace(',',''))/1000
        cl=re.search(r'closed at\s*(\d+(?:\.\d+)?)\s*m\b',l); w={'ten':10,'twenty':20,'thirty':30}
        got=w.get(c.group(1),None) or (int(c.group(1)) if c.group(1).isdigit() else None)
        if cl and got: R['B1'].append(dict(line=i+off,ground_m=g,true_ratio=round(float(cl.group(1))/g,2),asserted=got,ok=abs(float(cl.group(1))/g-got)<0.5))
# B2: "**N files / M lines**" vs measured (splitlines, not split)
terms=['cartograph','mapmaking','portolan','cadastr','graticule','theodolite']
def n(path,t): return len(subprocess.run(['grep',path,t,'corpus/knowledge'],capture_output=True,text=True).stdout.splitlines())
meas={t:(n('-rli',t),n('-rni',t)) for t in terms}
R['B2']=[]
for i,l in enumerate(body):
    for m in re.finditer(r'\*\*(\d+)\s*files?\s*/\s*(\d+)\s*lines?\*\*',l):
        pre=l[:m.start()].lower()
        cand=[(pre.rfind(x),x) for x in terms if pre.rfind(x)>=0 and m.start()-pre.rfind(x)<=140]
        if not cand: continue   # assertion not tied to a term command (e.g. a broad probe)
        t=max(cand)[1]
        R['B2'].append(dict(line=i+off,term=t,asserted=[int(m.group(1)),int(m.group(2))],measured=list(meas[t]),
                            ok=[int(m.group(1)),int(m.group(2))]==list(meas[t])))
# B4: anchored line must share a content word with the citing clause
R['B4']=[]
for i,l in enumerate(body):
    for m in re.finditer(r'`?([\w./-]+\.md):(\d+)',l):
        p,a=m.group(1),int(m.group(2)); cand=[Path(p)] if Path(p).exists() else list(Path('corpus/knowledge').rglob(Path(p).name))
        if not cand: R['B4'].append(dict(line=i+off,path=p,status='missing')); continue
        fl=cand[0].read_text().splitlines()
        if a>len(fl): R['B4'].append(dict(line=i+off,path=p,status='oob')); continue
        st=max(l.rfind(';',0,m.start()),l.rfind('—',0,m.start()),l.rfind('(',0,m.start()))
        ctx=l[st+1 if st>0 and m.start()-st<120 else 0:m.start()].lower(); cited=fl[a-1].lower()
        sh=set(re.findall(r'[a-z]{5,}',ctx))&set(re.findall(r'[a-z]{5,}',cited))
        R['B4'].append(dict(line=i+off,path=p,anchor=a,shared=sorted(sh)[:5],ok=bool(sh)))
# B5: "the X in §N" must match a section title containing X
titles={int(m.group(1)):m.group(2) for _,_,t in heads for m in [re.match(r'^(\d+)\. (.+)$',t)] if m}
R['B5']=[dict(line=i+off,wants=m.group(1),ref=m.group(2),ok=m.group(1).split()[0] in titles.get(int(re.match(r'\d+',m.group(2)).group()),'').lower())
         for i,l in enumerate(body) for m in re.finditer(r'(?:the|this)\s+([a-z][\w -]{2,25})\s+in\s+§\s?([\d.–-]+)',l)]
# B7: normative update statements
R['B7']=[dict(line=i+off,text=l.strip()[:180]) for i,l in enumerate(body)
         if re.search(r're-?survey|every breach|per levy year|not due until',l,re.I) and re.search(r'after|every|until|due|per\b',l,re.I)]
# B8: competing-definition citation
R['B8']=dict(c27='cosmology-cosmography.md:27' in T, c71='cosmology-cosmography.md:71' in T, c102='cosmology-cosmography.md:102' in T)
# B9: form-typology row parity
R['B9']=[]
for i,l in enumerate(body):
    if l.strip().startswith('|') and re.match(r'^\|\s*\**\s*form',l.strip(),re.I):
        n=next((k for k,x in enumerate(body[i+2:]) if not x.strip().startswith('|')),None)
        R['B9'].append(dict(line=i+off,header=l.strip()[:90],rows=n))
R['sha256']=hashlib.sha256(D.read_bytes()).hexdigest()
print(json.dumps(R,indent=1,ensure_ascii=False))
```

**Validation — a detector that fires nothing on r47 is broken.** Run on the r47 assembly (`790` lines, sha `e0c8ae56…`):

| Defect | Detector leg | r47 result | Fires? |
|---|---|---|---|
| B1 | `B1` | 0.2 mm × 1:50,000 = 10 m ground; 200 m survey → true ratio **20**, asserted **10** | **yes** |
| B2 | `B2` | asserts `**2 files / 3 lines**` for `cartograph`; measured **2 files / 2 lines** | **yes** |
| B4 | `B4` | `craft-artisan-lexicon.md:44` shares **0** content words with the Steel row — but 84 rows raise the same flag | **yes, low precision** |
| B5 | `B5` | "the typology in §1–3" → §1 frame; "the typology in §2" → register test; both `ok:false` | **yes** |
| B7 | `B7` | 3 statements; `:664` "after any storm that breaches a dike", `:678` "not due until the levy year turns", `:691` "after a dike breach, per levy year" | **yes** |
| B8 | `B8` | `c27:false`, `c71:true`, `c102:true` | **yes** |
| B9 | `B9` | 8-row typology table vs **5**-row "per form" table | **yes** |
| B3 | — | false accusation lives in C02's seat prose (`C02-entry-b.md:36,:501`), not the fenced body | **no — by design** |
| B6 | — | handoff note lives in C01's seat prose (`C01-entry-a.md:298`), not the fenced body | **no — by design** |

Sensitivity: **7 of 9 blocking defects are mechanically detectable on assembled bytes.** B3 and B6 require a fragment-level read or the single-author draft that removes the surface. Limits, stated plainly: `B2` pairs a count only with a term found within 140 characters of it, so a broad-probe row is skipped rather than mispaired; `B4`'s overlap test is a **locator, not a verdict** — on r47 it raises 84 review rows for one true defect (the long single-line fields dilute the clause window), so use it to rank anchors for a human read; `B7` counts statements and cannot decide whether they conflict — a reader must compare triggers.

Run on the r48 blocks as controls:

- **Header** (`C02-header.md`): `len` = 23 lines / 1,827 words / 0 H2 / 0 H3 / 0 table rows; `B1` none; `B2` two assertions (`cartograph` 2/2, `cadastr` 2/2), both `ok:true`; `B8` all three true; `B4` 18 anchors, 0 missing, 0 out-of-range.
- **Entry** (`C01-entry.md`, the filed body): `len` = 227 lines / 4,545 words / 14 H2 / **0 H3** / 81 table rows; `B1` none fired (the scale arithmetic is a set of exact conversions, not a ratio claim); `B2` none (the gap line uses "2 lines in 2 files", a different form the leg does not parse — verified by hand, §3.2); `B5` none; `B7` one statement; `B8` `c27:true`; `B9` one form table with **8** rows.

The entry passes every structural leg. The detector's remaining value is at apply time: it re-checks the **assembled** bytes after the header substitution and any integration edit, which is where r47's defects formed.

---

## 5. Integration recommendation — choose one composition

The entry is right-sized; the remaining decision is which bytes compose it. Recommendation: **C01's entry as the body, with C02's head block substituted for C01's head.**

| Composition | Lines | Words | Verdict |
|---|---:|---:|---|
| C01 entry as filed | 227 | 4,545 | inside every envelope, but the 1,054-char topic fails the sweep |
| **C01 body + C02 head (recommended)** | **238** | **≈5,369** | inside; topic = seed; one H1; contract fields restored |
| fragments appended to C01 | 341 | — | duplicate sections; reject |
| K01 allocations from the fragments (§3.3) | 253 | ≈9,376 | over the line tolerance and word-heavy; reject |

The recommended composition is 238 lines (1.08× the partition max, 1.60× the median) and ≈5,369 words (1.13× the median, 0.76× the 7,047 non-outlier max) with **0 H3** — the word ceiling is met without cutting content, which the fragment path could not do (it needed 17.9 w/line across the unwritten sections). Implementation: take `C02-header.md:111-135` as the file head; take C01's body from its first `## 1.` onward; drop C01's head; do not append E01/M02/M01. Substituting the head also restores the missing `- source:` field (C01's head has 7 fields, C02's 8).

## 6. Conditions for apply (all measurable on the assembled bytes)

1. **Topic byte-equality.** The landed `- topic:` value must equal the r44 seed value (766 chars, sha `9424fb81…` at the line level) and C10's README row description. C01's 1,054-char topic must not land.
2. **One head.** Exactly one H1 and one `- topic:` line; the C02 head replaces C01's, never precedes it.
3. **Composition audit.** No section appears twice. The count of `## N.` headings is 14 and the head has 8 fields; if E01/M02/M01 were appended, the duplicate tables will show as repeated `| Neighbour |` / `| Claim |` / `NON-CANON` headers.
4. **Length, two dimensions.** `wc -l` ≤ 250 **and** `wc -w` recorded; projected 238 / ≈5,369. If > 7,500 words (1.57× the median), the round record names the exception.
5. **H3 budget.** ≤ 4 against the partition's 3; the filed entry has 0.
6. **Detector clean.** `python3 check.py <assembled>` → `B1` all `ok:true`; `B2` no `ok:false`; `B5` no `ok:false`; `B7` one trigger set; `B8.c27:true`; `B9` the form table has 8 rows. `B4` review rows are triaged by hand (locator, not verdict).
7. **Example.** C01's §11 (25 lines) is inside C14's hard ceiling; M01's 27-line block is not landed.
8. **Single assembler.** B3/B6 cannot be detected on bytes; one named author performs the head substitution and records the diff.

## 7. What I did not verify, and the write surface

- **The 238-line assembled file.** I measured the two components (C01 entry, C02 head) but did not build the file; 238 and ≈5,369 are arithmetic on measured parts, not a delivery. The post-apply `wc`/sweep is the certificate.
- **External sources.** No network; every shelf item remains `(to-verify)` and none was inspected.
- **Couples semantics.** C09 owns resolution; I checked that all 14 paths in C01's `couples:` line exist (they are repo-relative, not entry-relative).
- **The `B4` screen's precision.** It raises 84 review rows on r47 for one true defect; on the r48 entry the anchors resolve and the one historically-miscited site (`:44`) is correctly labelled. It is a locator.
- **The Ca claim.** Ca02's disposition row correctly classes this defect, but its `proposed_control` is **line-only** (`Ca02-overbuild.md:139`). The counter-example stands even though the entry passes: C02's 23-line header carries 1,827 words (79.4 w/line) against a partition header median of 1,002. A line-only control would certify it. The control needs the word leg.
- **No axis harm claimed from this seat.** The r48 entry is a genuine coverage improvement at partition-normal length and word count; the residual risk is the duplicate-composition/topic collision in §3.4–§3.5, which is a delivery hazard, not a content defect.

**Write surface:** this file only — `reports/round-48/cross/X03-overbuild.md`. No `corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..47/**`, `corpus/lessons/**`, `tools/gates/frozen/**` or fleet `.ufo/**` byte was edited or staged. No git mutation, install, or network. No `reports/round-*/run-validation.py` was executed. The detector and extraction scripts lived under `.scratch/x03/` and are reproduced inline in §4 for re-running; nothing was written under `corpus/`.
