# C03 — arithmetic verification of the cartography draft (claim C)

- Seat: `C03` | role: verifier | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7` (`"baseline_commit": "a01405d"`).
- Out path: `reports/round-48/cov/C03-arithmetic.md` (this file).
- Non-author statement: I drafted no entry fragment and edited no corpus byte. Every number below is recomputed from the file or command named beside it; commands are in §10.

**Verdict.** The **r48 right-sized draft is arithmetically clean**: every scale, ratio, count and vector I could recompute is correct, B1 is fixed (`20×`, not "ten times"), B2 is fixed (`2 lines in 2 files`), and none of r47's failing strings survive. Two count/statement defects remain, both in metadata rather than the entry body: **N4**, C01 calls its head an "11-field" block but it has **7 fields** (`- source:` is absent; 11 is the line count), and **N5**, the claimed "227-line entry" holds only with C01's own head — assembled with C02's 23-line head the entry is **238 lines**, still under the 250 ceiling but 17 over the 221 live maximum. One wording risk (**N6**): "area by cos φ" in the equirectangular row can be read as multiplying by cos φ; the area scale is `1/cos φ`. The r47 audit is retained in §3 as the baseline the r48 draft improved on.

---

## 0. What exists at this read

| Draft | Source | Fence | Lines | Use |
|---|---|---|---:|---|
| r47 assembled entry | `reports/round-47/cov/C04-entry-header.md` + `C01-entry-a.md` + `C02-entry-b.md` + `C03-entry-c.md` | head 51 + body `201+361+177` | **790** | baseline audit (§3) |
| r48 C01 body | `reports/round-48/cov/C01-entry.md` | 228 content lines incl. one trailing blank = **227** | 227 (215 body) | assembly A |
| r48 C02 head | `reports/round-48/cov/C02-header.md` | 23 lines | 23 | assembly B head |

Two legitimate assemblies exist because the two executors each wrote a head:

- **A — C01's own head + C01 body: 227 lines** (`12`-line head incl. separator + `215` body). This is the number C01 claims.
- **B — C02's 23-line head + C01's 215-line body: 238 lines.** This is what the integrator gets if the C02 header (the seat assigned the header) is applied.

Both are `<= 250`; both are `> 221` (the live partition maximum). Which head is authoritative is C05/C13's contract call; the arithmetic consequence is mine and is stated in §2.1 and §2.4 (N5).

---

## 1. Live census at `a01405d` (measured, not carried)

| Quantity | Command | Output | Verdict |
|---|---|---|---|
| Total `.md` entries | `find corpus/knowledge -name '*.md' \| wc -l` | `223` | matches claim |
| Partitions | per-directory `find … -maxdepth 1 -name '*.md' \| wc -l` | `civilizations 94, culture-material 25, linguistics 25, myth-symbol 26, synthesis 29, verification 24` | `94+25+25+26+29+24 = 223` ✓ |
| culture-material length | `wc -l corpus/knowledge/culture-material/*.md` + Python `statistics` | `n 25, min 103, max 221, median 149, mean 150.2, sum 3756` | min/max/median match the claims |
| README | `wc -l`, `wc -c`, `sha256sum corpus/README.md` | `575` lines, `143866` bytes, `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` | same digest as r47's baseline and C02's `verified-at` |
| Duplicate H1 | `grep -c '^# kotodama-shokunin corpus index' corpus/README.md` | `2` (lines 1 and 3) | Ca defect live |
| Landing slug | `ls corpus/knowledge/culture-material/cartography-and-mapmaking.md` | `No such file or directory` | free; gap unowned |

Sweep: `rows 223 files 223`, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`, `totals_line 223`, `footer {"total":223,"dir_totals":[25,26,25,29,24,94]}`, `exit=0`. Footer slot order: `["linguistics","myth-symbol","culture-material","synthesis","verification","civilizations"]` — every vector assertion below uses that order.

---

## 2. The r48 draft: every number recomputed

### 2.1 Size arithmetic

| Quantity | Measured | Draft claim | Verdict |
|---|---:|---|---|
| C01 fence content lines (excl. trailing blank) | 227 | "227-line entry" (`C01-entry.md` summary) | ✓ under C01's head |
| C01 head | 12 lines including the separator (11 head lines: H1, blank, 7 fields, 2 shelf sub-lines; line 12 is the blank) | "11-field head block" | **✗ N4** (7 fields) |
| C01 body | 215 lines | "215 body lines" | ✓ (`227 − 12 = 215`) |
| C02 head | 23 lines | "23-line head block" | ✓ |
| Assembly A | 227 | 227 | ✓ |
| Assembly B | **238** (`23 + 215`) | — | **N5**: not 227 |
| r47 → r48 reduction | `790 → 227` = `−563` (`−71.3%`); `790 → 238` = `−552` (`−69.9%`) | — | computed |

C01's non-empty line count is 177 (the entry is table-dense), and the fence has one trailing blank; neither affects the 227/215 claim.

### 2.2 Numeric claims in the r48 body — all recompute

| # | Location | Claim | Recomputation | Verdict |
|---|---|---|---|---|
| 1 | `C01-entry.md` §3 (line 66 of the fence) | traverse closing to 1% on 100-pace legs = ±0.75 m at 0.75 m/pace | `0.01 × 100 × 0.75 = 0.75 m` | ✓ |
| 2 | §3 line 66 | 1:5,000 sheet, 0.2 mm line = 1 m ground | `0.2 mm × 5,000 = 1,000 mm = 1 m` | ✓ |
| 3 | §3 line 66 | at 1:2,500, 0.2 mm = 0.5 m | `0.2 × 2,500 = 500 mm = 0.5 m` | ✓ |
| 4 | §3 line 66 | 1 arcminute at 10 km ≈ 2.9 m | `10,000 × tan(1/60°) = 2.9089 m` | ✓ |
| 5 | §3 line 66 | 200 m closure vs 0.2 mm @1:50,000 (=10 m) = **20×** | `0.2 × 50,000 = 10,000 mm = 10 m`; `200/10 = 20` | ✓ **B1 fixed** |
| 6 | §4 table (line 77) | centuria ≈ 710 m square ≈ 50 ha | `710² = 504,100 m² = 50.41 ha` | ✓ |
| 7 | §4 table (line 80) | Dunhuang star chart c. 700 CE | external date | `(to-verify)`; not arithmetic |
| 8 | §5 table (line 102) | degree of longitude 111.3 km at equator, 55.7 km at 60° | `111.3 × cos 60° = 55.65 ≈ 55.7` | ✓ |
| 9 | §5 table (line 102) | equirectangular "area by cos φ" | local area scale is `1/cos φ` (areas exaggerated by `sec φ`), not `× cos φ` | **N6 wording** |
| 10 | §5 table (line 103) | Mercator `sec φ = 2` at 60°, so 1:1,000,000 is effectively 1:500,000 | `1/cos 60° = 2`; `1,000,000 ÷ 2 = 500,000` | ✓ |
| 11 | §5 (line 108) | 0.2 mm at 1:24,000 = 4.8 m; 1:50,000 = 10 m; 1:250,000 = 50 m | `0.2×24,000 = 4,800 mm`; `×50,000 = 10 m`; `×250,000 = 50 m` | ✓ |
| 12 | §5 (line 108) | 1 cm bar: 500 m at 1:50,000; 2.5 km at 1:250,000 | `10 mm × 50,000 = 500 m`; `× 250,000 = 2,500 m` | ✓ |
| 13 | §5 (line 110) | 32-point compass rose = 11.25° per point | `360/32 = 11.25` | ✓ |
| 14 | §11 (line 185) | 1:25,000, 0.2 mm = 5 m | `0.2 × 25,000 = 5,000 mm = 5 m` | ✓ |
| 15 | §11 (line 184) | ±1% on 100-pace legs = ±0.75 m per leg | `0.01 × 100 × 0.75 = 0.75 m` | ✓ |
| 16 | §11 (line 186) | delta ≈ 20 km across | design value, no derivation claimed | — |
| 17 | §13 (line 223) | 2,400 Roman feet at 0.296 m ≈ 710 m ≈ 50 ha | `2,400 × 0.296 = 710.4 m`; `710.4² = 50.47 ha` | ✓ |
| 18 | §13 line 223 | chart dates (Carte Pisane late 13th c.; Dunhuang c. 700; Hereford c. 1300) | external dates | `(to-verify)`; correctly excluded from the arithmetic claim |
| 19 | §1 (head gap statement) | 0 filename owners, 0 topic-line owners; `cartograph` 2 lines in 2 files; four vocabulary probes 0 files each | measured: filename 0; topic-owner 0; `grep -rni cartograph` 2/2; `mapmaking/portolan/graticule/theodolite` 0 each | ✓ |

No other numeric claim appears in the body. The draft deliberately states no projection-distortion percentage, portolan accuracy figure, price or print run (the `(to-verify)` shelf is explicit).

### 2.3 Count labels — every one matches its structure

| Claim (C01 summary / section) | Location | Counted | Verdict |
|---|---|---|---|
| "12-row one-owner boundary" | §2 table | 12 data rows | ✓ |
| "seven-link survey chain" | §3 table | 7 rows | ✓ |
| "eight map forms" | §4 heading + table | 8 rows | ✓ |
| "five-condition test" | §1 numbered list | 5 items | ✓ |
| "five-link warrant chain" | §7 table | 5 rows | ✓ |
| "six silence classes" | §8 lead sentence | 6 numbered clauses | ✓ |
| "nine-step build order" | §9 heading + list | 9 items | ✓ |
| "six-row decision record" | §10 table | 6 rows | ✓ |
| "11-row calibration bank" | §12 table | 11 rows | ✓ |
| "four choices every map makes" | §1 | 4 numbered items | ✓ |
| "three claims" | §5 heading | projection, scale, orientation = 3 (the blank is a fourth bullet, not counted) | ✓ |
| "23 path:line assertions" / "19 couples" | `C02-header.md` summary | 19 backticked `.md` tokens in the couples line | 19 ✓ (assertion count is C04's to re-read) |
| "eleven load-bearing files" | `C02-header.md` head | 11 anchor-file sha256 pins (+1 README pin in `verified-at` = 12 occurrences) | ✓ |

### 2.4 Remaining defects in the r48 bytes

| ID | Location | Finding | Fix |
|---|---|---|---|
| **N4** | `reports/round-48/cov/C01-entry.md` summary | "a **227-line** entry (215 body lines after the **11-field** head block)". The head has **7 fields** — `gap filled`, `topic`, `sources`, `couples`, `verified-at`, `recheck`, `scope` — and **no `- source:` field**. 11 is the head's *line* count, not its field count. | Say "11-line head block" or "7-field head"; if this head is the one applied, add `- source:` for the 8-field contract. (Contract leg: C05/C13.) |
| **N5** | `C01-entry.md` summary vs `C02-header.md` | "227-line entry" is true only for assembly A. C02's header is 23 lines, so assembly B is `23 + 215 = 238`. | State the assembled number after the head is chosen. Both are under 250; both exceed the 221 live max by 6 and 17. |
| **N6** | `C01-entry.md` §5 table, equirectangular row | "Distorts: **area by cos φ**". The equirectangular area scale at latitude φ is `1/cos φ` (areas exaggerated by `sec φ`); "area by cos φ" reads as multiplication by cos φ, the inverse. | "area scale `1/cos φ`" or "areas exaggerated by `sec φ`". The neighbouring numbers in the same cell (111.3/55.7 km) are correct. |

The B-series fixes are present and correct: B1 → `20×` (§2.2 row 5), B2 → `2 lines in 2 files` (§2.2 row 19), B9 → "(the eight forms above, not a sample)" with 8 rows (§2.3). B3/B4/B5/B6/B7/B8 are citation/text fixes outside arithmetic (C04's leg); the r48 head cites the ladder at `craft-artisan-lexicon.md:54-65` as B4 required.

---

## 3. The r47 baseline audit (what the r48 fixed)

### 3.1 Size — reproduces exactly

Head fence `C04:111-163` = **51** lines, 2,522 words, 20,944 chars, 22 `(to-verify)` marks on 21 lines, 9 sha256 pins, 21 couples tokens. Body = `C01 201 + C02 361 + C03 177` = **739** lines, 17,601 words, 106,997 chars, 15 H2, 240 table rows, 29 `(to-verify)`. Total `51 + 739 = 790`.

R03's ratios are body-based and correct: `739/149 = 4.96 ≈ 5.0×` median; `739/221 = 3.34 ≈ 3.3×` max. On the total: `790/149 = 5.30×`; `790/221 = 3.57×`.

### 3.2 Six failing values (all absent from the r48 draft)

| ID | r47 location | What it said | Recomputation | Required fix | r48 status |
|---|---|---|---|---|---|
| ARITH-1 (B1) | `C02-entry-b.md:98` | 0.2 mm @1:50,000 = 10 m; 200 m closure = "ten times" | `200/10 = 20` | "twenty times" or 200→100 m | **fixed** (`20×`) |
| ARITH-2 (B2) | `C04-entry-header.md:59`, `:115` | `cartograph` = "2 files / 3 lines"; `:71` counted as a hit | `grep -rli` 2; `grep -rni` 2; `:71` has no token | "2 files / 2 lines" | **fixed** (`2 lines in 2 files`) |
| ARITH-3 (N1) | `C02-entry-b.md:218` | "five roles" | §7.1 table `:224-231` = 6 rows | "six roles" or drop the number | **absent** (r48 has no role-count claim) |
| ARITH-4 (P2-2) | `C04-entry-header.md:117` | "six load-bearing anchors" | 9 sha256 pins (`:118-125`, `:134`) | "nine" | **absent** (r48 says "eleven files", counted 11) |
| ARITH-5 (N3) | `C10-sweep.md:84-87` | staged README 145,595 bytes; footer `:562`; vector `:24` | applying C09's final diff yields 602 lines / 146,542 bytes; vector `:32`; footer `:570` | recompute from the staged file | **n/a** (r48 C10 drafts fresh) |
| ARITH-6 (B9) | `C03-entry-c.md:97-103` | "per form", 5 rows | 5 vs 8 forms (`C01:242-249`) | retitle or add 3 rows | **fixed** ("eight forms … not a sample", 8 rows) |

### 3.3 r47 counts that were already correct

Five conditions (`C01:116-120`), six mechanisms (§3.1–3.6), eight questions (`C01:225-232`), eight forms (`C01:242-249`), seven links (`C02:49-55`), five warrant links (`C02:286-290`), four products (`C02:254-261`), three customers (`C02:265`), eight decisions (`C02:332-336`), 13 etymology rows (`C02:355-367`), three consequences (`C01:140-145`), nine steps (`C03:79-87`), twelve decision rows (`C03:195-206`), fourteen calibration rows (`C03:160-173`), 18 shelf entries (`C04:139-157`), 23 enumerated anchor assertions (`C04:231-239`, sum `= 23`), 21 couples tokens (`C04:174`, `:243-244`).

ARITH-7 nuance: `C04:206` "topic byte_equal: True len: 775 775" — 775 is **characters**; the UTF-8 length is **783 bytes**. Equality holds.

---

## 4. README arithmetic for the r48 edit

Live README is rev **2.4** only (`grep -n '^revision:' corpus/README.md` → first hit `:5`; no 2.5). The rev-2.4 prose vector is defective:

- `corpus/README.md:11` reads `25/23/25/29/24/94 → **25/23/26/25/24/94**`.
- Filed after-vector sums `25+23+26+25+24+94 = 217`; true live vector `25/26/25/29/24/94 = 223` (`README:548`; sweep `footer_live`). Slot deltas against correct: `0 −3 +1 −4 +0 +0 = −6`.
- Repair (rev 2.4 prose): `… → **25/26/25/29/24/94**`.
- Post-landing (rev 2.5): culture-material `25 → 26`, vector `25/26/26/29/24/94 = 224`, totals `223 → 224`.

The per-category phrasing in `claims.json` ("synthesis 25->29, myth-symbol 23->26, culture-material 26->25") is the same repair by slot and yields `223` before the landing; the landing then makes culture-material 26 for `224`.

Edit-size arithmetic, if C09's final block is reused: a 21-line revision block + 1 inserted row + 5 net appended history lines (6 added, 1 replaced) = net `+27` lines, `575 → 602`, bytes `143,866 → 146,542`; the single-line fixes (rev-2.4 vector, section header, totals, footer vector) are net 0. r48 must recompute after staging its own block. A green sweep at 224 does **not** validate the prose vector (the sweep never parses revision prose — C10's control D, `C10-sweep.md:128`); the vector must be summed by hand or by the gate (§8).

---

## 5. Budget arithmetic for the right-sized entry

| Target | Total lines | Actual r48 | Margin |
|---|---:|---:|---|
| Claim ceiling `<= ~250` | 250 | 227 (A) / 238 (B) | −23 / −12 |
| Live partition max | 221 | 227 (A) / 238 (B) | **+6 / +17 over** |
| r47 over-build | 790 | — | −563 / −552 lines (−71.3% / −69.9%) |

The claim's ceiling is met; the live-max discipline is not. A 238-line entry is 17 lines over the longest existing culture-material entry (`funerary-material-culture.md`, 221) and 89 over the median (149). If the round wants to honour the live max rather than only the 250 ceiling, the cut needed is 17 lines (assembly B) or 6 (assembly A) — X03/C05 should name which discipline binds.

---

## 6. Verified constants the draft may use

| Constant | Value |
|---|---|
| Census before / after | `223` (`94/25/25/26/29/24`) → `224`; culture-material `26`; vector `25/26/26/29/24/94` |
| culture-material length | min 103, median 149, max 221, mean 150.2 |
| Scale arithmetic | 1 mm @1:50,000 = 50 m; 1 mm @1:1,000,000 = 1 km; 0.2 mm @1:50,000 = 10 m; 200 m closure = 4 mm on sheet = **20×**; 1 arcmin @10 km = 2.909 m |
| Mercator | `sec 60° = 2`; effective RF `1:1,000,000 → 1:500,000` at 60° |
| Longitude | 111.3 km/° at equator; 55.65 km/° at 60° |
| Centuria | `2,400 × 0.296 = 710.4 m`; `710.4² = 50.47 ha` |
| README | rev 2.4 prose `217`; live footer `223`; repaired rev 2.4 `223`; landing `224`; duplicate H1 count `2` |
| Seed topic line | 775 characters / 783 UTF-8 bytes, equal to `K02-gap-scout.md:227` |
| Gap probes | filename 0; topic-owner 0; `mapmaking`/`portolan`/`graticule`/`theodolite` 0; `cartograph` 2 files / **2** lines; `cadastr` 2 files; broad probe 28 files / 31 lines |

**Must not use:** r47's `"ten times"` + `200 m`; `"2 files / 3 lines"`; `:71` as a `cartograph` hit; `"five roles"`; `"six load-bearing anchors"`; `"11-field head block"` (7 fields); C10's `:24/:247/:254/:558/:562`; `775` called bytes; `"area by cos φ"` unless it means `1/cos φ`.

External dates (Snyder 1987, Mercator 1569, Ortelius 1570, al-Idrisi 1154, Dunhuang c. 700, Hereford c. 1300, Carte Pisane) are **not** arithmetic-verified here and remain `(to-verify)`; no network was used.

---

## 7. What the numbers imply for risk

The r48 draft fixed the r47 arithmetic: the one computation (B1) is now right, the gap count is reproducible, and every retained count label matches its table. The remaining risk is **metadata drift**: a summary number ("227", "11-field") that is true for one assembly and false for another. The integrator should treat the line count and head-field count as derived values of the *applied* assembly, not as properties of either fragment.

---

## 8. Re-runnable gate (read-only; no corpus writes)

Save as `.scratch/c03/arith-gate-v2.py`; run on an assembled entry.

```python
#!/usr/bin/env python3
"""Arithmetic gate for a cartography entry draft (read-only)."""
import re, sys

WORD = {'one':1,'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
        'nine':9,'ten':10,'eleven':11,'twelve':12,'thirteen':13,'fourteen':14,'fifteen':15}
NUM = dict(WORD); NUM.update({str(i):i for i in range(1,16)})
NOUN = {'form','role','link','step','row','question','condition','consequence',
        'product','customer','decision','currency','regime','rule','class','field','anchor'}

def load(path):
    lines = open(path, encoding='utf-8').read().split('\n')
    return lines[:-1] if lines and lines[-1] == '' else lines

def tables(lines):
    out, i = [], 0
    while i < len(lines):
        if lines[i].startswith('|'):
            j = i
            while j < len(lines) and lines[j].startswith('|'): j += 1
            block = lines[i:j]
            if len(block) >= 2 and re.match(r'^\|[\s:-]+\|', block[1]):
                out.append((i, block[0], len(block) - 2))
            i = j
        else:
            i += 1
    return out

FAIL = []
def check(ok, msg):
    print(('PASS ' if ok else 'FAIL ') + msg)
    if not ok: FAIL.append(msg)

path = sys.argv[1]
lines = load(path); text = '\n'.join(lines)
print(f'# {path}\nlines {len(lines)}')
check(len(lines) <= 250, f'length <= 250 lines (got {len(lines)})')
check(len(lines) <= 221, f'length <= live partition max 221 (got {len(lines)})')

if re.search(r'0\.2\s*mm', text) and re.search(r'200\s*m\b', text) and re.search(r'ten times', text, re.I):
    check(False, 'false-precision: 0.2 mm @1:50,000 = 10 m; 200 m = 20x, text says ten')
elif re.search(r'0\.2\s*mm', text) and re.search(r'100\s*m\b', text) and re.search(r'ten times', text, re.I):
    check(True, 'false-precision: 100 m closure = 10x (correct)')
elif re.search(r'0\.2\s*mm', text) and re.search(r'twenty times|20×', text, re.I):
    check(True, 'false-precision: 200 m closure stated as 20x')
else:
    check(True, 'no false-precision sentence to contradict')

tbl = tables(lines); checked = issues = 0
pat = r'(?<![\d.])(' + '|'.join(sorted(NUM, key=len, reverse=True)) + r')[\s-]+(?:[A-Za-z-]+[\s-])?(' + '|'.join(sorted(NOUN, key=len, reverse=True)) + r')(?:s)?\b'
for m in re.finditer(pat, text, re.I):
    n, noun = NUM[m.group(1).lower()], m.group(2).lower()
    pos = text[:m.start()].count('\n'); ln = lines[pos]
    if ln.startswith('#'):
        segment = ln
    else:
        mm = re.search(r'\*\*(.+?)\*\*', ln)
        if not mm: continue
        segment = mm.group(1)
    if not re.search(r'\b' + re.escape(m.group(1)) + r'[\s-]+(?:[A-Za-z-]+[\s-])?' + re.escape(noun), segment, re.I):
        continue
    cand = [t for t in tbl if 0 <= t[0] - pos <= 14 and (noun == 'row' or re.search(noun, t[1], re.I))]
    if not cand: continue
    t = min(cand, key=lambda x: x[0] - pos); checked += 1
    if t[2] != n:
        issues += 1; check(False, f"label '{m.group(0)}' vs table at line {t[0]+1}: {t[2]} rows")
print(f'label-table checks performed: {checked}')
if issues == 0: check(True, 'all label counts match their tables')

for s, why in {'2 files / 3 lines':'B2 (cartograph = 2 files / 2 lines)',
               'six load-bearing anchors':'P2-2 (nine sha256 pins exist)',
               'five roles':'N1 (six role rows)'}.items():
    if s in text: check(False, f"forbidden string '{s}' — {why}")
check(True, 'forbidden-string sweep complete')

for vec, want in [('25/23/26/25/24/94',217), ('25/26/25/29/24/94',223), ('25/26/26/29/24/94',224)]:
    got = sum(int(x) for x in vec.split('/'))
    check(got == want, f'vector {vec} sums {got} (want {want})')
check(94+25+25+26+29+24 == 223, 'partition 94+25+25+26+29+24 == 223')
check(223+1 == 224 and 25+1 == 26, 'landing +1: total 223->224, culture-material 25->26')

print('\nRESULT', 'FAIL' if FAIL else 'PASS', f'({len(FAIL)} failures)')
sys.exit(1 if FAIL else 0)
```

**On the r48 draft (assembly A, 227 lines):**

```
lines 227
PASS length <= 250 lines (got 227)
FAIL length <= live partition max 221 (got 227)
PASS false-precision: 200 m closure stated as 20x
label-table checks performed: 1
PASS all label counts match their tables
PASS forbidden-string sweep complete
PASS vector 25/23/26/25/24/94 sums 217 (want 217)
PASS vector 25/26/25/29/24/94 sums 223 (want 223)
PASS vector 25/26/26/29/24/94 sums 224 (want 224)
PASS partition 94+25+25+26+29+24 == 223
PASS landing +1: total 223->224, culture-material 25->26

RESULT FAIL (1 failures)
```

**On the r47 baseline (790 lines):** 7 failures — length (790 > 250 and > 221), B1, `five roles` vs 6 rows, `2 files / 3 lines`, `six load-bearing anchors`, `five roles`; all vector legs pass. (Assembly B, 238 lines, produces the same one length failure at 221.)

Limits: the label leg binds only a heading or leading bold phrase to the nearest noun-matching table within 14 lines; `row` labels accept the next table of any header. Counts carried only in prose (e.g. "six silence classes", "nine steps") are manual and were checked in §2.3. Run the gate on the **assembled** file, because a label and its table can live in different fragments.

---

## 9. What I did not verify

- **Every `path:line` assertion.** C04 owns the exhaustive re-read; I verified the numeric claims and the gap probes, and counted the assertion list (23) without re-reading all 23 anchors.
- **External dates and bibliographic figures.** No network; every Tier B item is `(to-verify)`.
- **The C10 (r47) staged tree** (145,595 bytes, sha `0ab794d8…`): its `.scratch` path is gone. I verified only that C09's final diff cannot produce that byte count or those line positions; the digest is `could-not-evaluate`.
- **C04's / C02's sha256 pins against live files**: not recomputed (C06's leg); my counts are counts of pins, not digest checks.
- **Which head the integrator will apply** (A vs B): the arithmetic for both is stated in §2.1 and §5.

---

## 10. Commands and write-surface statement

All commands from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ find corpus/knowledge -name '*.md' | wc -l                         # 223
$ for p in $(ls -d corpus/knowledge/*/ | xargs -n1 basename); do …   # 94/25/25/26/29/24
$ python3 -B reports/round-28/readme/sweep.py                        # rows 223 files 223, exit 0
$ wc -l corpus/knowledge/culture-material/*.md | sort -n             # min 103 / median 149 / max 221
$ wc -l corpus/README.md; wc -c corpus/README.md                     # 575 / 143866
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md       # 2
$ grep -rli 'cartograph' corpus/knowledge/ | wc -l                   # 2
$ grep -rni 'cartograph' corpus/knowledge/ | wc -l                   # 2
$ sed -n '71p' corpus/knowledge/myth-symbol/cosmology-cosmography.md # no 'cartograph'
$ python3 (fence extraction + counts)                                # r47: 51 head + 739 body = 790
$ python3 (r48 fence counts)                                         # C01: 227/215; C02 head 23; B: 238
$ python3 (apply C09 fenced diff to live README)                     # 602 lines, 146542 bytes, footer :570
$ python3 -B .scratch/c03/arith-gate-v2.py .scratch/c03/r48-assembled-c01.md   # 1 FAIL (221 max)
$ python3 -B .scratch/c03/arith-gate-v2.py .scratch/c03/r47-assembled.md       # 7 FAIL
```

**Write surface:** this file only, plus the disposable instruments `.scratch/c03/arith-gate-v2.py`, `.scratch/c03/r47-assembled.md`, `.scratch/c03/r48-assembled-c01.md`, `.scratch/c03/r48-assembled-c02.md`, `.scratch/c03/r48-c01-block.txt`, `.scratch/c03/r48-c02-head.txt` (all outside `reports/` and `corpus/`). No `corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..47/**`, `reports/round-48/**` other than this file, `tools/gates/frozen/**`, or fleet `.ufo/**` byte was edited or staged. No git commit/push, no install, no network. No `reports/round-*/run-validation.py` was executed.
