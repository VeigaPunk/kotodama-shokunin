# X02 — honesty critic: every number measured, every "should work" flagged

- Seat: `X02` | role: critic | claim: **cross** (C and Ca) | round 48, loop 2, position 2
- Baseline: `git rev-parse HEAD` → `a01405dd36367292255c2652ac0a601f4cd6a0af` (2026-10-19 16:34:48 -0300), equal to `reports/round-48/claims.json:7` (`"baseline_commit": "a01405d"`).
- Observation window: `2026-10-19T19:38:39Z`–`19:42:50Z` (`date -u`). The write surface moved during the window; §5 names the census time.
- Out path: `reports/round-48/cross/X02-honesty.md` (this file). I wrote nothing else in-tree; scratch probes are under `.scratch/x02/`.
- Non-author statement: I drafted no entry body, header, README edit, control or verifier fragment. Every judgement below is from bytes read at the baseline or from a command quoted with its output. I wrote only this file.

**One-line judgment.** No fabricated number and no invented source were found. The headline counts are true and independently reproducible — 223 entries, culture-material 25, cartography 0 owners, README H1 count 2, rev-2.4 prose vector summing 217 — and the staged 224 tree sweeps green. But **three provenance defects in the declaration** (the filed freshness result does not reproduce from the filed inputs; the declaration is future-dated; a seat instruction's vector arithmetic sums to 223 while calling it 224) and **three landing-integrity defects in the C assembly** (three different topic texts, two different head blocks, and a 227-line draft against a measured 221-line partition maximum) mean the round cannot honestly record C as landed until those are resolved. Ca's defect and fix are measured; its control is verified working.

---

## 1. Measured baseline (command → output)

All run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

```
$ git rev-parse HEAD
a01405dd36367292255c2652ac0a601f4cd6a0af
$ find corpus/knowledge -name '*.md' | wc -l
223
$ git ls-tree -r --name-only HEAD corpus/knowledge | grep -c '\.md$'
223
$ ls corpus/knowledge/culture-material/*.md | wc -l
25
$ for d in corpus/knowledge/*/; do ...; done
civilizations 94 | culture-material 25 | linguistics 25 | myth-symbol 26 | synthesis 29 | verification 24
```

Sum: 94+25+25+26+29+24 = **223**. Two independent counts agree.

```
$ python3 -B reports/round-28/readme/sweep.py          # exit 0
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223 | missing_from_index 0 | topic_mismatch 0 | orphan_rows 0
totals_line 223 totals_ok True | footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
```

```
$ grep -c '^# kotodama-shokunin corpus index' corpus/README.md
2
$ grep -n '^# ' corpus/README.md
1:# kotodama-shokunin corpus index
3:# kotodama-shokunin corpus index
$ grep -c '^revision: 2\.0' corpus/README.md
2
```

```
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
0
$ grep -rniE '^- *topic:.*(cartograph|mapmak|portolan|survey map|world map|atlas)' corpus/knowledge/ | wc -l
0
$ grep -rni 'cartograph' corpus/knowledge/ | wc -l
2
corpus/knowledge/myth-symbol/cosmology-cosmography.md:102
corpus/knowledge/civilizations/mesoamerica-primary-sources.md:58
```

Culture-material length distribution (the only measured band the draft can be judged against):

```
min 103 (textile-technology.md) | median 149 | max 221 (funerary-material-culture.md) | mean 150.2 | n = 25
```

## 2. Claim C — number-by-number verdict

| Claimed number | Measured | Verdict |
|---|---|---|
| total 223 → 224 | 223 measured; +1 arithmetic | **honest** (224 is a prediction until landing) |
| culture-material 25 → 26 | 25 measured | **honest** |
| cartography 0 owners | 0 filenames, 0 topic lines, 2 incidental token hits | **honest** |
| "live max is 221" | max 221 measured (n=25) | **honest as a number**; see H6 for the draft's relation to it |
| entry ≤ ~250 lines | C01's draft = **227 lines** | under 250, **over the live max** (H6) |
| "avoids every R03 blocking defect" | all nine answered; B1–B8 independently re-checked, B9 counted | **honest** (§2.4) |
| staged sweep 224==224 | measured, exit 0 — **on C11's fixture**, not C01's draft | **true but not the claim's certificate** (§2.2) |
| README rev 2.5, 224 | drafted in C10/D01; not landed | **prediction, correctly labelled** |

### 2.1 What actually exists now

At `19:42:50Z`, `reports/round-48/` held **58 of 64** declared out paths, **0 undeclared** `.md` files, and **6 not yet filed** (`cov/C05-length-contract.md`, `review/R03-c-content.md`, `cross/X01-trades.md`, `cross/X03-overbuild.md`, `cross/Q01-final-gate.md`, `op/O03-next-o.md`). Three relevant C artifacts:

- `cov/C01-entry.md` — the actual draft: a fenced **227-content-line** entry (my extraction: `body.split('\n')` = 229 with two trailing empties → 227 lines; `splitlines()` = 228). C01's self-report of "227-line entry (215 body lines after the 11-field head block)" is **arithmetically consistent**: 227 − 11 head − 1 blank = 215.
- `cov/C02-header.md` — a separate 23-line head block.
- `.scratch/r48-c11/stage/.../cartography-and-mapmaking.md` — a **136-line verification fixture** that C11 explicitly discloses is "written by me to exercise the sweep, **not C01's draft**" (`cov/C11-sweep.md:6`).

### 2.2 The 224 sweep green is measured — on the fixture

```
$ python3 -B .scratch/r48-c11/stage/reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 26, "linguistics": 25, ...}
rows 224 files 224 | missing_from_index 0 | topic_mismatch 0 | orphan_rows 0
totals_line 224 totals_ok True | footer {"total": 224, "dir_totals": [25, 26, 26, 29, 24, 94]}
exit=0
```

This certifies the **sweep mechanics and the 224 census**, and it is the strongest available pre-landing evidence. It does **not** certify C01's bytes: the staged entry is a different 136-line fixture with a different `- topic:` line (see H4). C11's own caveat is correct (`cov/C11-sweep.md:123-124`): the sweep depends on filename, exact topic text, and exactly one added file; if C01's topic differs, the row must be regenerated and the recipe re-run. It does.

The in-tree command still says 223 and will keep saying so until the integrator applies bytes. Any fragment that prints "224" from the in-tree root before the apply is quoting a prediction as a certificate.

### 2.3 C01's arithmetic and countable claims (all recomputed)

Every number I could recompute from C01's body checks out:

| Assertion | Recompute | Verdict |
|---|---|---|
| 0.2 mm line at 1:5,000 = 1 m | 0.2 × 5000 / 1000 = 1.0 | correct |
| 0.2 mm at 1:2,500 = 0.5 m | 0.2 × 2500 / 1000 = 0.5 | correct |
| 1 arcmin at 10 km ≈ 2.9 m | 10,000 × tan(1/60°) = 2.909 m | correct |
| 200 m closure vs 10 m sheet = 20× | 200 / 10 = 20 | correct (B1's fix is right) |
| 1:24,000 at 0.2 mm = 4.8 m | 0.2 × 24000 / 1000 = 4.8 | correct |
| 1:50,000 at 0.2 mm = 10 m | 0.2 × 50000 / 1000 = 10.0 | correct |
| 1:250,000 at 0.2 mm = 50 m | 0.2 × 250000 / 1000 = 50.0 | correct |
| 1 cm at 1:50,000 = 500 m | 1 × 50000 / 100 = 500 | correct |
| 1 cm at 1:250,000 = 2.5 km | 1 × 250000 / 100 = 2500 m | correct |
| 32-point rose = 11.25° | 360 / 32 = 11.25 | correct |
| 1% on 100 pace at 0.75 m/pace = ±0.75 m | 75 m × 1% = 0.75 m | correct |

Countable structures, counted from the fenced body rather than trusted from prose:

| Claim | Measured |
|---|---|
| eight map forms | **8** data rows (table has 10 lines incl. header + separator) |
| seven-link chain | **7** data rows in §3 |
| 12-row boundary | **12** data rows in §2 |
| six-row decision record | **6** data rows in §10 |
| 11-row calibration bank | **11** data rows in §12 |
| nine-step build order | **9** numbered items |

No arithmetic defect of R03's B1 class is present in C01's draft. The two defects I found in C11's **fixture** — "a portolan passes all five and fails 5" (self-contradiction) and "near half-quarter (11.25°)" (11.25° is one point) — **do not appear in C01's draft**: C01 writes "11.25° per point" and has no "passes all five" sentence. They are fixture-only and must not be reported as draft defects.

### 2.4 B1–B9: C01 answers all nine

| R03 defect | C01's answer, verified | Verdict |
|---|---|---|
| B1 arithmetic | 20× recomputed at `:348`; the wrong "10×" is gone | **clear** |
| B2 unreproducible gap count | "2 lines in 2 files", `:102` + `mesoamerica:58`, `:71` named as a disclaimer *without* the token (`:72`) | **clear** — my `grep -ril cartograph` returns exactly those 2 files |
| B3 false quote accusation | "archive of coups" quoted verbatim from `naming-systems.md:70`; no correction proposed | **clear** — `grep -n` returns the phrase at `:70` |
| B4 ladder anchor | cites `craft-artisan-lexicon.md:54-65`, explicitly not `:44` (`:75`) | **clear** — `:44` is the Steel row; the ladder is `:54-65` |
| B5 cross-refs | "the typology is §4"; four `§N` references resolve | **clear** |
| B6 section numbering | provenance/charter is §7 and the heading agrees | **clear** |
| B7 worked example | one rule stated once; no second update rule | **clear** (same one-rule structure as the fixture, without the fixture's contradiction) |
| B8 competing ownership | `cosmology-cosmography.md:27` is quoted and answered at `:72`, `:75`, `:77`, `:103` | **clear** — the fix R03 required is present |
| B9 per-form coverage | "the eight forms above, not a sample"; 8 forms counted | **clear** |

So the claim's "avoid every one of R03's blocking defects" is **evidence-backed** for C01's draft. This is the part of C that is genuinely done.

### 2.5 H4 (S1) — three different topic texts and two head blocks

The same entry exists in three versions with **three different `- topic:` strings**:

| Source | Topic length | sha256 prefix |
|---|---:|---|
| `cov/C01-entry.md` fenced body | 1054 chars | `aed27f526727bef2` |
| `cov/C02-header.md` fenced head | 775 chars | `a42926b1d0fe5ac5` |
| C11's staged fixture | 1279 chars | `3b3ab9ff52a620c7` |

They also have **different H1s**: C01's is "…the survey-to-sheet register: the map as an argument about space…"; C02's is "…the map as an argument about space: the survey chain, projection and scale, symbol grammar"; the fixture's is "…the Survey-to-Symbol Chain, Forms by Question…". And C01's fenced body is **self-contained** — it already carries its own H1 + head (11 lines) — so concatenating C02's head in front of it would produce two H1s and two head blocks inside one entry.

Consequences, all measurable:

1. The measured 224 sweep green used the **fixture's** topic; it does not prove that a row built from C01's 1054-char topic will be byte-equal. C11 says this itself.
2. The integrator cannot apply "C01 + C02" without picking one H1 and one topic text. There is no filed decision naming which.
3. The README row must be regenerated from the chosen topic and the sweep re-run; the row length and, therefore, `readme_sha256` will change.

**This is the single highest landing risk in the round**, and it is not in any of the defect lists I read.

### 2.6 H5 (S2) — C01's head deviates from the entry contract

Sampled live entries all order the head as `- topic:` first, then `- sources:`, `- couples:`, `- source:`, `- verified-at:`, `- recheck:`, `- scope:`:

```
timekeeping-instruments.md: - topic: - sources: - source: - couples: - verified-at: - recheck: - scope:
trade-economy-lexicon.md:   - topic: - sources: - couples: - verified-at: - recheck:
direction-symbolism.md:     - topic: - sources: - couples: - source: - verified-at: - recheck:
dialect-faction-map-workflow.md: - topic: - sources: - couples: - source: - verified-at: - recheck:
```

C01's head order is `- gap filled:`, **then** `- topic:`, and it has **no `- source:` field** at all. C02's head has `- topic:` first and includes `- source:`. The claim requires "the entry contract"; whichever head lands, one contract field set is being silently dropped. This is a one-line fix, but it must be decided before the bytes are called assembled.

### 2.7 H6 (S2) — 227 lines is over the measured partition maximum

- C01's draft: **227 lines**.
- Live culture-material band: **103–221** (median 149, max 221).
- 227 is **+6 over the max** (1.03×), **1.52× the median**.

The claim's threshold is "<=~250 lines (the partition discipline, not a hard cap)", and its own parenthetical says "the live max is 221 — NOT r47's 790-line over-build". Those two statements are inconsistent: 250 is not the partition discipline, and a 227-line landing creates a **new partition maximum**. This is nowhere near r47's 790, and I would not call it an over-build — but the round must not describe 227 as "inside the band" or "right-sized to the live max". Either trim to ≤221, or record the +6 as a declared, reviewed exception with the reason (12 boundary rows + 11 calibration rows + 8 forms are load-bearing). Either is honest; silence is not.

## 3. Claim Ca — number-by-number verdict

| Claimed number | Measured | Verdict |
|---|---|---|
| README H1 count 2 | 2, at `:1` and `:3` | **honest** |
| removal → count 1 | simulated: delete `:3` → 1; delete `:3-4` → 1 | **measured** |
| sweep stays green after | both variants exit 0 | **measured** |
| rev-2.4 prose vector sums 217 | `25/23/26/25/24/94` = **217** | **honest** |
| repair → 224 | the seat instruction's repair sums to 223 (H3) | **instruction defect, not a README defect** |
| heading-count control | drafted and independently executed (§3.4) | **verified working** |
| over-build disposition | row drafted (`Ca02`), JSON not yet landed | **pending apply** |

### 3.1 The removal, simulated on byte-exact copies

```
$ cp corpus/README.md .scratch/x02/README-nodup.md && sed -i '3d' ...
  575 → 574 lines | H1 count 1 | sweep exit 0 | sha256 84e16f566e170ac4be9d7f01d90ca1743640d36c899d9c81808c5dc8c0065633
$ cp corpus/README.md .scratch/x02/README-del34.md && sed -i '3,4d' ...
  575 → 573 lines | H1 count 1 | sweep exit 0 | sha256 d407260dfd8cae9a6e5528aa86411f8998eb2b9cfce3b565f7d0e892b3190079
```

Deleting only `:3` leaves a double blank line (`:2` and `:3` both empty). Deleting `:3-4` (the H1 and its following blank) leaves exactly one blank separator:

```
1: # kotodama-shokunin corpus index
2:
3: revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
```

**Recommend `:3-4`.** Both satisfy "remove the redundant second H1" and both sweep green; `:3-4` is the cleaner byte result. Pin the original digest `7c788a1d…` in the landing wire.

### 3.2 H3 (S2) — the rev-2.4 prose defect and the arithmetic error in the instruction

`corpus/README.md:11` prints:

```
the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**
```

- before: 25+23+25+29+24+94 = **220** (correct for the pre-r42 total)
- after: 25+23+26+25+24+94 = **217** (should be 223)

The live vector (`README:548` and the sweep) is `25/26/25/29/24/94` = **223**. Three positions are wrong: myth-symbol 23→26, culture-material 26→25, synthesis 25→29.

`targets.json` (C10) states the repair as "synthesis 25→29, myth-symbol 23→26, culture-material 26→25 = 224". Those changes produce `25/26/29/25/24/94` = **223**, not 224. Correct strings:

- **repaired rev-2.4 (current corpus):** `25/26/25/29/24/94` = 223
- **rev-2.5 after the landing:** `25/26/26/29/24/94` = 224

C10's staged README uses exactly these strings, so the staged bytes are right and the instruction text is wrong. Do not copy the instruction's `= 224`.

### 3.3 H9 (S3) — a second sweep-blind duplicate, outside Ca's scope

`corpus/README.md:42` is a dangling duplicate of the `revision: 2.0` first line (byte-identical to the opening of `:44`; `:42` has no body):

```
$ sed -n '42p;44p' corpus/README.md
revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten
revision: 2.0 — Round-35 thin-partition expansion landing (2026-10-19): the ten
$ grep -c '^revision: 2\.0' corpus/README.md
2
```

It is the same defect class as the duplicate H1 (a sweep-blind duplicate title line), it remains live after this round because Ca's `before` names only the H1, and Ca03 explicitly says the edit must not absorb it. X05 flagged it independently; I confirm the bytes. It should be a named Ca successor, not silently left.

### 3.4 The heading-count control is verified, not asserted

Ca05 drafts `tools/check-readme-heading.py` inside a four-backtick fence (necessary because the control's own selftest contains triple-backtick fixtures). I extracted the fence by delimiter and ran it:

```
$ python3 -B check-readme-heading.py --selftest        # exit 0
... selftest: 8/8 checks passed
$ python3 -B check-readme-heading.py --readme corpus/README.md   # exit 1
h1_lines [1, 3] | headings {"1": 2, "2": 7}
findings 1  H1-COUNT lines=[1, 3] expected exactly 1 level-1 heading, found 2
$ python3 -B check-readme-heading.py --readme .scratch/x02/README-del34.md   # exit 0
h1_lines [1] | findings 0
```

So the control detects the live defect, exits non-zero on it, and passes on the fixed variant. This satisfies Ca's "control added or a durable note filed" **once the integrator lands the tool** — the draft is in a report fragment today, not in `tools/`.

The staged tree also demonstrates the premise directly: it sweeps **green while carrying two H1s** (`grep -c` on the staged README = 2; sweep exit 0). That is the strongest possible proof that the sweep is blind to this defect.

### 3.5 The disposition exists as a draft, not as a landed row

`calib/Ca02-overbuild.md` defines the class correctly — "an out-of-band draft whose defect surface was never measured on the assembled artifact", not "long entries" — preserves B1–B9 as instances, and names an apply path `reports/round-48/calib/queue-successor-r48.json`. That file does **not** exist at my census (non-md files under `reports/round-48/`: `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`). So the claim's "a queue-successor row filed" is **pending apply**, and N02's integrity check cannot run until it lands. I verified three of the cited instance defects independently (B1, B3, B4 above), so the row's evidence is sound.

## 4. Provenance defects in the declaration itself

### 4.1 H1 (S1) — the filed freshness result does not reproduce from the filed inputs

The declaration says the gate returned `C FRESH`, `Ca FRESH`, `O STALE`. Reproduced three ways:

```
# (a) filed claims.json alone
$ python3 tools/harness/claims-freshness.py --claims reports/round-48/claims.json --root . --no-exec
[C] COULD-NOT-EVALUATE no before_checks declared ...
[Ca] COULD-NOT-EVALUATE no before_checks declared ...
exit 3  REFUSE

# (b) filed claims.json + the only overlay on disk
$ python3 tools/harness/claims-freshness.py --claims reports/round-48/claims.json \
      --checks .scratch/r48-freshness-check.json --root .
error: .scratch/r48-freshness-check.json: overlay names claim 'O', absent from the claims file
exit 2  REFUSE (malformed)

# (c) the pre-drop skeleton + the overlay
$ python3 tools/harness/claims-freshness.py --claims .scratch/r48-claims-skel.json \
      --checks .scratch/r48-freshness-check.json --root .
[C] FRESH 2/2 | [O] STALE 1/1 (capability_present measured=False expected=True) | [Ca] FRESH 1/1
exit 1  REFUSE: O has a `before` already false
```

The **result is true** — I reproduced it exactly, including O STALE for the declared reason. But it reproduces only against a scratch file that was never filed. As filed, `claims.json` dropped O while the overlay still names it, and the gate refuses. Fix:

1. Land the overlay and the pre-drop skeleton under `reports/round-48/telemetry/` (AGENTS.md: telemetry under `reports/round-<N>/telemetry/`, "never only `.scratch`").
2. Record the exact `--claims` input used and file the gate JSON output (`--json`). The current command line shows placeholders (`--claims <candidates> --checks <overlay>`), which is not a reproducing command.

### 4.2 H8 (S3) — the gate's C probe is narrower than the claim

The overlay's C ownership probe is scoped to `"partition": "culture-material"`. The claim says cartography is unowned **corpus-wide**. The gate proves only the partition half. My global probes (0 filenames; 0 topic lines in all six partitions; 2 incidental body hits) supply the missing half — but the gate should be widened, or the split stated in the telemetry note.

### 4.3 H2 (S1/S2) — the declaration timestamp is future-dated

```
$ stat -c '%y' reports/round-48/claims.json
2026-10-19 16:36:19.844155825 -0300   → 19:36:19Z
$ date -u +%FT%TZ
2026-10-19T19:39:07Z
$ jq -r .declared_at_utc reports/round-48/claims.json
2026-10-19T19:45:00Z
```

The declared time is ~9 minutes after the file that carries it was written and ~6 minutes after this observation. Either the timestamp was pre-committed or a clock is skewed. A declaration cannot honestly be dated after its own evidence. Annotate or correct it (`to-verify` which side is authoritative); do not leave both numbers filed.

### 4.4 H7 (S3) — 790 vs 739 vs 797 is a unit mismatch, not a contradiction

R47's assembly was **790 lines = 51 head + 739 body** (`reports/round-47/cross/Q01-final-gate.md:87`); R03 measured the **739-line body** (`reports/round-47/review/R03-c-content.md:1,8`); Q01 later records a corrected **797-line** assembly (`Q01-final-gate.md:368`). All three are correct about different objects. Claims and dispositions must state the unit, or a reader will treat them as a conflict.

## 5. Write-surface census (snapshot at `2026-10-19T19:42:50Z`)

```
$ python3 ... # declared out paths vs filed .md
md filed 58 of 64 | undeclared [] | missing 6
missing: cov/C05-length-contract.md, review/R03-c-content.md, cross/X01-trades.md,
         cross/X03-overbuild.md, cross/Q01-final-gate.md, op/O03-next-o.md
$ git status --porcelain -- corpus tools
(empty)
```

- 64 seats declared, 64 seat objects, 64 unique ids, 64 unique out paths; none absolute, none containing `..` (`targets.json` checked programmatically).
- **No undeclared fragment and no write outside a declared out path** at this census. Six seats had not filed at the census time; their absence is not a violation, but Q01/A03 must re-run this census at close.
- The only untracked item outside round 48 is `reports/round-46/review/R01-review.md`, mtime `2026-10-19 14:48:54 -0300` — hours before the r48 declaration. It is pre-existing repo dirt, not a round-48 write.
- Scratch-only evidence that must be promoted: `.scratch/r48-freshness-check.json`, `.scratch/r48-claims-skel.json`, `.scratch/r48-c11/stage/`. Scratch is allowed; being the *only* copy is not (H1).

Telemetry digests match the filed bytes:

```
bf8df21b641c1a49a7b71eb46504210a58096dda3f2cefa6c7618b1200535292  reports/round-48/claims.json
d029eaa1e37481918c10c20bb7ced3e3e31a8886a207cca05cb55ee3aaa20446  reports/round-48/targets.json
```

## 6. "Should work" register — measured vs asserted

| Statement | Status |
|---|---|
| 223 → 224 / 25 → 26 | 223 and 25 measured; 224/26 measured **only in the staged fixture tree** |
| README 2 → 1 headings | measured by simulation on byte-exact copies |
| sweep green at 224 | **measured on the fixture** (exit 0); **not** measured on C01's bytes or in-tree |
| prose vector repairs to 223/224 | measured strings; the C10 instruction's arithmetic is wrong (H3) |
| "entry ≤ ~250" | 227 measured; the live band is 103–221 (H6) |
| "avoids all B1–B9" | independently verified clear for C01 (§2.4) |
| "the gate flagged O stale" | true, but only reproducible against a scratch input (H1) |
| heading-count control works | **verified by execution** (§3.4) |
| over-build disposition row | drafted; JSON **not landed** — pending apply |
| observed worker launches/completions | **null** — `dispatch-declared.json` records `requested_workers: 64` but no observed counter; the closing snapshot must fill launches/completions/failures/concurrency/route or `null` with owner + reason |

## 7. Honesty verdict and conditions

**C — numbers honest; assembly not yet landable as one object.** The premise is measured fresh, C01's arithmetic and every countable claim check out, B1–B9 are answered, and the staged 224 sweep is green. Not yet honest to record as landed because:

1. **H4**: pick one topic text and one head block (C01's 1054-char self-contained head, or C02's 775-char head plus a body-only C01 section). A concatenation produces two H1s and two heads.
2. **H5**: restore the contract head order (`- topic:` first) and the missing `- source:` field.
3. **H6**: trim 227 → ≤221, or file the +6 as a declared exception. Do not call 227 "inside the band".
4. Regenerate the README row from the chosen topic, re-run the sweep **in-tree** after apply, and record 224==224 from the landed tree — the fixture result is not the certificate.
5. Keep the absence probe anchored to `a01405d`; after landing, `ls …cartography-and-mapmaking.md` succeeds and must not be "updated" to hide that it was pre-landing evidence.

**Ca — defect and fix measured; control verified; disposition pending.** Honest to record once:

1. Apply the `:3-4` removal, pin `7c788a1d…`, re-run the sweep.
2. Land the overlay + gate output under `reports/round-48/telemetry/` (H1).
3. Land `tools/check-readme-heading.py` and the `queue-successor-r48.json` row; fix the `= 224` instruction arithmetic (H3); give `README:42` a named successor (H9).

**No fabricated source, no invented citation, and no unmeasured number presented as measured was found.** The defects are provenance, instruction-arithmetic and assembly-integrity defects — not data fabrication.

---

## 8. Commands run (reproduction)

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git rev-parse HEAD
find corpus/knowledge -name '*.md' | wc -l
ls corpus/knowledge/culture-material/*.md | wc -l
git ls-tree -r --name-only HEAD corpus/knowledge | grep -c '\.md$'
python3 -B reports/round-28/readme/sweep.py
grep -c '^# kotodama-shokunin corpus index' corpus/README.md
grep -c '^# ' corpus/README.md
grep -c '^revision: 2\.0' corpus/README.md
sed -n '11p;42p;44p;234p;240,241p;544p;548p' corpus/README.md
grep -rni 'cartograph' corpus/knowledge/
grep -ril cartograph corpus/knowledge/*/*.md
grep -ril cadastr corpus/knowledge/*/*.md
wc -l corpus/knowledge/culture-material/*.md | sort -n
cp corpus/README.md .scratch/x02/README-del34.md && sed -i '3,4d' .scratch/x02/README-del34.md
python3 -B reports/round-28/readme/sweep.py --readme .scratch/x02/README-del34.md
python3 -B .scratch/r48-c11/stage/reports/round-28/readme/sweep.py
python3 tools/harness/claims-freshness.py --claims reports/round-48/claims.json --root . --no-exec
python3 tools/harness/claims-freshness.py --claims reports/round-48/claims.json --checks .scratch/r48-freshness-check.json --root .
python3 tools/harness/claims-freshness.py --claims .scratch/r48-claims-skel.json --checks .scratch/r48-freshness-check.json --root .
# Ca05 control: extract the four-backtick ``python fence, then:
python3 -B .scratch/x02/check-readme-heading.py --selftest
python3 -B .scratch/x02/check-readme-heading.py --readme corpus/README.md        # exit 1
python3 -B .scratch/x02/check-readme-heading.py --readme .scratch/x02/README-del34.md  # exit 0
sha256sum reports/round-48/claims.json reports/round-48/targets.json
stat -c '%y %n' reports/round-48/claims.json && date -u +%FT%TZ
```

Exit codes above were read after redirecting stdout/stderr to files, not through a pipe.

Write-surface statement: this file is the only durable write I made. Scratch outputs are `.scratch/x02/` (`README-nodup.md`, `README-del34.md`, `overlay-noO.json`, `c01-body.md`, `check-readme-heading.py`). No `git`, no network, no package installs, no execution of any `reports/round-*/run-validation.py`.
