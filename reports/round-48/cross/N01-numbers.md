# N01 — number-facts verifier (cross-claim)

- Seat: `N01` | role: verifier | claim: **cross** | round 48, loop 2, position 2
- Out path: `reports/round-48/cross/N01-numbers.md` (this file)
- Observed at: `2026-10-19T19:38:39Z`–`19:39:14Z` (UTC, `date -u`)
- Baseline: HEAD `a01405dd36367292255c2652ac0a601f4cd6a0af`; `reports/round-48/claims.json` says `a01405d`. **Match, no drift at my read.** (`X04` owns drift; this is the number I checked.)
- Mission: independently recount the partition census, the entry line count, the README heading count, the sweep totals — and recompute every arithmetic claim in `claims.json` rather than trusting it.
- Statement: I read corpus bytes and the filed r47 review/scratch assembly only. I wrote this file only. Commands are in §8.

---

## 1. Verdict in one line

Every census and arithmetic number in claim C is **reproducible at HEAD** (223 total, culture-material 25, post-landing 224/26, rev-2.4 vector defect = 217, sweep 223==223 exit 0), and the r47 over-build number **790 is exact**; but two live README duplication facts are **not** in any claim — the duplicate H1 is real at `:1`/`:3`, and there is a **second, unreported dangling duplicate `revision: 2.0` header at `corpus/README.md:42`** — and the entry line count is `could-not-evaluate` because no r48 draft exists at my read cut.

---

## 2. Number ledger — measured, not carried

| Number | Measured value | Command / evidence | Verdict |
|---|---:|---|---|
| Total knowledge entries | **223** | `find corpus/knowledge -name '*.md' \| wc -l` | confirmed |
| civilizations | **94** | `ls corpus/knowledge/civilizations/*.md \| wc -l` | confirmed |
| culture-material | **25** | `ls corpus/knowledge/culture-material/*.md \| wc -l` | confirmed |
| linguistics | **25** | ditto | confirmed |
| myth-symbol | **26** | ditto | confirmed |
| synthesis | **29** | ditto | confirmed |
| verification | **24** | ditto | confirmed |
| partition sum | **223** | `ls corpus/knowledge/{...}/*.md \| wc -l` | equals total |
| culture-material lines: min / median / max | **103 / 149 / 221** | `wc -l corpus/knowledge/culture-material/*.md` | confirmed; mean 150.24, sum 3,756 |
| corpus-wide lines: min / median / max | **75 / 190 / 436** | `wc -l corpus/knowledge/*/*.md` | **the 221 figure is partition-scoped, see §4.2** |
| corpora entries > 250 lines | **6** (4 linguistics, 1 myth-symbol, 1 verification) | `wc -l \| awk '$1>250'` | **see §4.2** |
| README H1 count | **2** | `grep -c '^# kotodama-shokunin corpus index' corpus/README.md` | confirmed; at `:1` and `:3`, byte-identical |
| README total lines | **575** | `wc -l corpus/README.md` | confirmed |
| README index rows | **223** | sweep `rows 223 files 223` | confirmed |
| README section headers | **25 / 26 / 25 / 29 / 24 / 94** at `:177/:205/:234/:261/:293/:320` | `grep -n '^## '` | headers match live partition |
| README section row counts | **25 / 26 / 25 / 29 / 24 / 94** (sum 223) | per-section `^- \`` count | each header == its row count |
| `Total knowledge entries:` line | **223** at `:544` | `grep -n 'Total knowledge entries'` | confirmed |
| Footer vector | **25/26/25/29/24/94** at `:548` | `sed -n '548p'` | confirmed |
| `readme_sha256` | **`7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd`** | `sha256sum corpus/README.md`; sweep receipt agrees | confirmed |
| Sweep result | `rows 223 files 223`, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`, `totals_ok True`, `footer_ok True`, **exit 0** | `python3 -B reports/round-28/readme/sweep.py` | confirmed |
| Cartography filename owners | **0** | `find ... -iname '*cartograph*' -o -iname '*mapmaking*' ... \| wc -l` | confirmed |
| Cartography topic-line owners | **0** | `grep -rniE '^- *topic:.*(cartograph\|mapmak\|portolan\|cadastr\|graticule\|theodolite)'` | confirmed |
| Target slug | **absent** | `ls corpus/knowledge/culture-material/cartography-and-mapmaking.md` → No such file | confirmed |
| `cartograph` files / lines | **2 / 2** | `grep -rli` / `grep -rni` | confirmed (r47 B2 corrected count) |
| r47 assembled draft | **790 lines** (`e0c8ae56a6a9a67b142af54317363013ac08e03cb7611058c65ca5189e9913aa`), 1 H1, 15 H2, 601 non-blank | `wc -l` + `sha256sum` on `.scratch/q01-assembled.md` | **exact**; `reports/round-47/cross/Q01-final-gate.md:87` claims 51 head + 739 body → 51+739 = 790 ✓ |
| r48 entry draft length | **`could-not-evaluate`** | `find reports/round-48 -type f` → only `claims.json`, `targets.json`, `telemetry/dispatch-declared.json` | no draft exists at my read cut |

---

## 3. Arithmetic recomputation

### 3.1 Partition vector and the landing delta

```
live footer     25/26/25/29/24/94  = 223   ✓ (matches total)
post-landing    25/26/26/29/24/94  = 224   ✓ (culture-material +1)
delta: total +1, culture-material +1, all other slots 0
```

`25+26=51; +25=76; +29=105; +24=129; +94=223`. Post: `... +26+26 ... = 224`. The claim's `223 -> 224`, `25 -> 26` are arithmetically sound.

### 3.2 The rev-2.4 prose-vector defect — reproduced

`corpus/README.md:11`:

```
the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**
```

| Vector | Sum | Truth test |
|---|---:|---|
| stated "before" `25/23/25/29/24/94` | **220** | matches rev 2.3's after-vector at `:20` (`25/23/25/29/24/94 = 220`) and the "totals moved 220 → 223" clause — consistent |
| stated "after" `25/23/26/25/24/94` | **217** | **wrong by −6**; the true after-vector is `25/26/25/29/24/94 = 223` |
| correct after `25/26/25/29/24/94` | **223** | matches live footer `:548` |

Per-slot error, stated-after vs true: myth-symbol `23` vs `26` (**−3**), culture-material `26` vs `25` (**+1**), synthesis `25` vs `29` (**−4**); net **−6**. The rev-2.4 text moved myth-symbol's +3 into the wrong slot and cut synthesis by 4. Confirmed defect; claim Ca/C's "sums 217 not 223" is exact.

### 3.3 Row order and insertion point (culture-material)

`corpus/knowledge/culture-material/` rows are in filename order at `README.md:236-260`. Alphabetical comparison: `calendar-festival-systems.md` (`:240`) < `cartography-and-mapmaking.md` < `costume-semiotics.md` (`:241`) — `cal` < `car` < `cos`. **Insert between lines 240 and 241**; header `:234` `(25)` → `(26)`.

### 3.4 r47 over-build ratios (numbers used in the claim and evidence)

| Ratio | Value | Basis |
|---|---:|---|
| 790 / 221 (partition max) | **3.57×** | `790-line over-build` vs live cm max |
| 790 / 149 (partition median) | **5.30×** | same |
| 790 / 250 (this round's discipline) | **3.16×** | — |
| 250 / 221 | **1.13×** | the discipline allows a 13% overshoot of the live cm max |
| 250 / 149 | **1.68×** | — |

The claim's "790-line over-build" is correct as measured; R03's "739 body lines = 5.0× median / 3.3× longest" is also correct for its own numerator (739/149 = 4.96, 739/221 = 3.34). The two reports differ in numerator, not in fact.

---

## 4. Discrepancies and precision corrections

### 4.1 A second live duplicate — `revision: 2.0` at `:42` (not in any claim)

```
$ sed -n '40,46p' corpus/README.md
40: Non-canon examples and passing structural gates do not certify historical truth.
41:
42: revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten
43:
44: revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten
45: round-35 entries landed — culture-material six (...
```

`sed -n '42p'` and `sed -n '44p'` are **byte-identical on that first line** (`diff` → no output; `cat -A` shows both end `the ten$`). `:42` is a **dangling orphan header with no body**: the revision text resumes at `:44` and runs to `:56`. `grep -o '^revision: [0-9.]*' | sort | uniq -c` reports `2 revision: 2.0` and 1 each of 2.4/2.3/2.2/2.1.

This is the **same defect class as the duplicate H1** — a stale duplicate line left by an edit — and claim Ca does not name it. It must be either (a) explicitly added to Ca's fix (remove `:42` and one adjacent blank), or (b) filed as a queue-successor row with its own `path:line`. I do not decide which; I record that the claim's `before` ("README carries a duplicate H1") is true but **incomplete**: the README carries two duplicate-line defects, one H1 and one revision header.

### 4.2 "The live max is 221" is partition-scoped, not corpus-wide

`claims.json` C says "<= ~250 lines / the live max is 221". Measured:

- culture-material max: **221** (`funerary-material-culture.md`) ✓
- corpus-wide max: **436** (`linguistics/register-strata-attestation.md`)
- entries > 250 lines corpus-wide: **6** (4 linguistics, 1 myth-symbol, 1 verification)

So 250 is **not** a corpus invariant; it is a target above this partition's own maximum. The claim's `after_required` ("entry length <=~250 lines") remains checkable, but the parenthetical "the live max is 221" should be read as "the landing partition's max", or corrected. Landing at 250 would be 1.13× the longest existing culture-material entry and 1.68× its median. I flag the framing, not the threshold.

### 4.3 Entry line count is not yet measurable

At my read cut `reports/round-48/` contains only `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`. **No C draft exists**, so "entry line count" is `could-not-evaluate` here — not 0, not a guess. When a draft lands, the integrator must measure the **assembled fenced body**, not the fragment files: in r47 the four fragments summed to 1,453 file lines (359+504+288+302) but the body was 739. Re-measure with:

```
# per fragment (file lines, not body lines)
wc -l reports/round-48/cov/C01-entry.md
# body: extract the entry fence, then count
python3 - <<'PY'
import re
t=open('reports/round-48/cov/C01-entry.md').read()
b=max(re.findall(r'```[A-Za-z0-9_-]*\n(.*?)```',t,re.S),key=len)
print(len(b.rstrip('\n').split('\n')))
PY
```

### 4.4 The duplicate H1 fix: counts, and the blank-line detail

`:1` and `:3` are byte-identical (`od -c` and `diff`). Removing `:3` alone gives `grep -c` = **1** (the claim's threshold) but leaves blank lines at `:2` and `:4` (a double blank). Removing `:3-4` (or `:2-3`) also gives count 1 and keeps the single-blank separation between the H1 and `revision: 2.4` at `:5`. The claim only requires the count, so either satisfies it; the tighter edit is `:3-4`.

### 4.5 Neither README defect is guarded by the sweep

`reports/round-28/readme/sweep.py`: the only "duplicate" leg is `duplicate_rows` (`:155`), which compares **index row filenames within a partition**, with its selftest control at `:337-343`. There is no H1 count, no heading-count assertion, and no revision-label uniqueness check. Running the sweep on the current README returns **exit 0 with both defects live** — measured, above. This confirms claim Ca's premise: a heading-count control does not exist.

---

## 5. Predicted post-landing numbers (and which are certifiable)

| Quantity | Predicted post-apply | Certifiable by |
|---|---:|---|
| `find corpus/knowledge -name '*.md' \| wc -l` | **224** | direct command |
| `ls corpus/knowledge/culture-material/*.md \| wc -l` | **26** | direct command |
| sweep `rows` / `files` | **224 / 224** | sweep exit 0 |
| `## culture-material/ (N)` | **26** | sweep `header_drift {}` |
| `Total knowledge entries:` | **224** | sweep `totals_ok True` |
| footer vector | **25/26/26/29/24/94** (= 224) | sweep `footer_ok True` |
| README H1 count | **1** | `grep -c` (no sweep leg) |
| `revision:` 2.0 labels | **2 -> 1** *if* §4.1 is adopted | `grep -o ... \| uniq -c` (no sweep leg) |
| `readme_sha256` | **not predictable here** | only the post-apply sweep receipt (`D01`'s delivery certificate) |
| README line count | **not asserted by any claim** | — |

The sweep's `footer_live.order` is `[linguistics, myth-symbol, culture-material, synthesis, verification, civilizations]`; post-landing it must read `[25, 26, 26, 29, 24, 94]`. If the integrator writes `(total 224 files; directory totals 25/26/26/29/24/94)` and the tree is 224 with cm 26, all six numbers agree; a single-slot slip (the r48 analogue of the 217 vector) would sum to 223 and the sweep's `footer_ok` would catch it — but only because it compares against the live tree, not because it sums.

---

## 6. Could-not-evaluate / to-verify

- **C entry line count** — no draft exists at `19:39Z`; see §4.3. Re-measure at landing.
- **Post-apply README sha256** — depends on exact bytes not yet drafted; not predicted (D01 owns the receipt).
- **r47's 790-line assembly provenance** — I measured `.scratch/q01-assembled.md` (a scratch artifact, sha `e0c8ae56…` matching `Q01-final-gate.md:87`), not a filed entry byte. The number reproduces; the file is not a durable corpus artifact.
- **`X04` baseline drift beyond my read** — HEAD matched at `19:38Z`; a later commit would invalidate my census. My numbers are pinned to `a01405d` and the README sha above.
- **External sources** — none checked; out of scope for this seat and no network.

---

## 7. What this means for the two claims

- **C (coverage):** every count it asserts before landing is true (223 / 25 / 0 owners / target absent / vector arithmetic). Its `after_required` numbers (224 / 26 / sweep 224==224 / vector 224) are internally consistent and checkable. The one number it cannot yet show is the entry length — no draft — so "right-sized" is unverified at my read cut. The 790-line counterexample is exact.
- **Ca (calibration):** the duplicate H1 is real (`:1`/`:3`, count 2), the rev-2.4 defect is real (217, −6), and the sweep has no heading-count leg. **But** the README's duplication is broader than the claim states: `:42` is a second duplicate (`revision: 2.0`), unfixed and unguarded. If Ca closes on the H1 alone, the same defect class remains live in the same file.

---

## 8. Commands and write-surface statement

All commands run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ git status --porcelain
?? reports/round-46/review/
?? reports/round-48/
$ find corpus/knowledge -name '*.md' | wc -l
223
$ for p in civilizations culture-material linguistics myth-symbol synthesis verification; do ...; done
94 / 25 / 25 / 26 / 29 / 24
$ wc -l corpus/knowledge/culture-material/*.md | awk '$2!="total"{s+=$1;n++} END{...}'
n=25 sum=3756 mean=150.24   (min 103 median 149 max 221)
$ wc -l corpus/knowledge/*/*.md | awk '$2!="total"{print $1}' | sort -n | ...
n=223 min=75 p50=190 max=436
$ wc -l corpus/knowledge/*/*.md | awk '$1>250' | wc -l
6
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
$ grep -n '^# ' corpus/README.md
1:# kotodama-shokunin corpus index
3:# kotodama-shokunin corpus index
$ diff <(sed -n '1p' corpus/README.md) <(sed -n '3p' corpus/README.md) && echo IDENTICAL
IDENTICAL
$ diff <(sed -n '42p' corpus/README.md) <(sed -n '44p' corpus/README.md) && echo IDENTICAL_FIRSTLINE
IDENTICAL_FIRSTLINE
$ grep -o '^revision: [0-9.]*' corpus/README.md | sort | uniq -c | sort -rn
2 revision: 2.0 ; 1 each of 2.4 2.3 2.2 2.1 1.8 1.7 ...
$ python3 -c "print(sum([25,26,25,29,24,94]), sum([25,23,26,25,24,94]), sum([25,26,26,29,24,94]))"
223 217 224
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223; missing 0; topic_mismatch 0; orphan_rows 0; header_drift {}; totals 223 True; footer_ok True; exit 0
$ sha256sum corpus/README.md
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
$ wc -l .scratch/q01-assembled.md && sha256sum .scratch/q01-assembled.md
790 .scratch/q01-assembled.md
e0c8ae56a6a9a67b142af54317363013ac08e03cb7611058c65ca5189e9913aa
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ grep -rni 'cartograph' corpus/knowledge/ | wc -l ; grep -rli 'cartograph' corpus/knowledge/ | wc -l
2 ; 2
```

**Write surface:** this file only — `reports/round-48/cross/N01-numbers.md`. No `corpus/**` byte was edited or staged; no `tools/**`, `LOG.md`, `reports/round-1..47/**`, `tools/gates/frozen/**`, or fleet `.ufo/**` write. No git commit/push, no install, no network. No `reports/round-*/run-validation.py` executed. `git status --porcelain` shows only the pre-existing untracked `reports/round-46/review/` and `reports/round-48/`.
