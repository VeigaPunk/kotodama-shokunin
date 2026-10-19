# C12 — content-quality review (claim C): is the right-sized cartography draft a real entry or filler?

- Seat: **C12** | role: verifier (content-quality reviewer) | claim: **C** (coverage) | round 48, loop 2, position 2
- Baseline: `a01405dd36367292255c2652ac0a601f4cd6a0af` (`git rev-parse HEAD`, 2026-10-19), equal to `reports/round-48/claims.json:7`
- Out path: `reports/round-48/cov/C12-content.md` (this file). I drafted no cartography byte and edited no fragment.
- Non-author statement: I wrote only this file. No `corpus/**`, `tools/**`, `README`, `LOG.md`, `reports/round-1..47/**` or fleet `.ufo/**` byte was touched or staged. No commit, install, network, or `run-validation.py`.

**Verdict.** The integrated 227-line draft (`C01-entry.md`) is a **real domain entry, not filler**, and it is **right-sized** (227 ≤ 250; 1.03× the live max 221). Its arithmetic is correct on every conversion I recomputed, its eight-form table is complete (r47 B9 fixed), its worked example states one update rule and applies it consistently (B7 fixed), and its one-owner sentence dispositions the cosmography `:27` competing definition (B8 fixed). It is **not yet landable as filed**, on five content/integration defects: (1) the `- topic:` line is **not byte-equal** to the r44 seed (1,054 vs 775 chars; different digest), so the README row built from the seed would fail the sweep; (2) the entry **contradicts itself on star charts** — §1 calls one "another register's sheet", §4 lists it as one of the eight map forms and §2 claims it; (3) the boundary table **omits `agrarian-field-system-lexicon.md`**, the parcel/claim owner C07 flagged as the sharpest under-claim; (4) two **incompatible byte sources** now exist (this integrated entry with six `DR-CM` rows; the C02/M01/M02/E01 fragment assembly with nine `DR-CT` rows) and cannot be merged blindly; (5) the living-practice screen is **one line** against a topic that touches lienzos, Pacific navigation and songlines. Fixes are specific and small; the merged best-of still fits at **244–246 lines** (§4).

---

## 1. Artifacts reviewed, pinned

| Artifact | sha256 | Lines | What it is |
|---|---|---:|---|
| `reports/round-48/cov/C01-entry.md` | `4c2815a766f12926ba14e14e2b164a8f65245a246223ae4258993e0a831c272d` | 473 (fenced entry **227** at `:70–296`, sha256 of fenced text `2a667749…`) | **the integrated entry** |
| `reports/round-48/cov/C02-header.md` | `7e5342ecf82db1818225c9407d6b27fbf92d368d347ccdd750f3ae5a8c455875` | fence 23 | alternative head block |
| `reports/round-48/cov/M01-example.md` | `04edaa4519b2d2f053dc1feefce9526ae9b27ef1b667211e63e64f312f08aaf1` | fence 27 | alternative example |
| `reports/round-48/cov/M02-calibration.md` | `bf680fbd63f0f7f5322bd1b3021b3bac87c9201c37745689095793df56825ae6` | fence 32 | alternative calibration bank |
| `reports/round-48/cov/E01-boundary.md` | `5a1288d3db1705a03ae2675aba0e66bcde71551f524ab873dba9d38011883b42` | fence 39 | 13-row boundary table |
| `reports/round-48/scout/K01-rightsized-spec.md` | `b3ac91b2a47c97064dd627482f39bc722f21cfe22e6e340c2b74739027d57a91` | — | the 230-line plan |
| `reports/round-48/cov/C14-example.md` | `3644eae43bec2211fc729954471746ae629ea2cf4a15d8760a3cf92b30a15605` | — | example gate (W1–W10) |

The fragments were still landing during my read window; every judgement is against these digests. `C01-entry.md` appeared **after** C14/C15/C16/C17 filed their `could-not-evaluate` receipts, so those verdicts do not cover it.

**Entry metrics (measured on the fenced block, `sed -n '70,296p'`):** 227 lines; 14 H2; **81 table rows** (35.7% of lines); 10 `(to-verify)` marks; 6 decision rows; 11 calibration rows; 8 forms; 7 chain links; 9 build steps; 25-line example.

---

## 2. Depth judgment — the draft does what the claim says

### 2.1 It teaches a method, not a map history

- **Master claim + four choices** (`C01:82-90`): what is measured / what is preserved / what is drawn / who may copy. Each is a design decision, not a description.
- **Five-condition register test** (`C01:91-99`): referent index, bounded notation, structural selection, conventional readability, reproducibility; "a partial pass is a fail, and the failure names what the object is instead." That is a discriminating test — field book, painting, T-O, itinerary, star chart, mental map each fail a named clause.
- **Seven-link chain** (`C01:120-138`): select → measure → control → reduce → project → symbolize → reproduce, each with artifact and failure mode, plus a weakest-link rule and a real error budget. This is production method, not vocabulary.
- **Eight forms** (`C01:139-166`) with a "structurally cannot show" column **and** a minimum credible build for all eight. r47's B9 (5 of 8) is fixed.
- **Provenance chain and silence classes** (`C01:198-220`): warrant → record → attestation → authentication → use; six silence classes, including the replaced toponym with the verbatim `naming-systems.md:70` quote.
- **Decision record and example** (`C01:235-270`): six load-bearing decisions; a one-rule worked example with a storm test and an alternative-rule cost table.

### 2.2 Arithmetic — every number I recomputed is correct

| Claim in the draft | Check | Result |
|---|---|---|
| traverse closing to 1% on 100-pace legs → ±0.75 m (pace 0.75 m) | `0.01 × 100 × 0.75` | 0.75 ✓ (`C01:135`) |
| 0.2 mm at 1:5,000 → 1 m | `0.2 × 5000 / 1000` | 1.0 ✓ |
| 0.2 mm at 1:2,500 → 0.5 m | `0.2 × 2500 / 1000` | 0.5 ✓ |
| 1 arcminute at 10 km ≈ 2.9 m | `10000 × tan(1/60°)` | 2.909 ✓ |
| 200 m closure vs 10 m graphic resolution = **20×** | `200 / 10` | 20 ✓ — r47 B1 fixed |
| Mercator scale factor sec φ = 2 at 60° | `1/cos 60°` | 2.0 ✓ |
| 1° longitude 111.3 km equator / 55.7 km at 60° | `111.3 × cos 60°` | 55.65 ✓ |
| 0.2 mm at 1:24,000 / 1:50,000 / 1:250,000 | — | 4.8 / 10 / 50 m ✓ |
| 1 cm bar at 1:50,000 / 1:250,000 | — | 500 m / 2.5 km ✓ |
| 32-point rose | `360 / 32` | 11.25° ✓ |
| centuria 2,400 Roman feet × 0.296 m ≈ 710 m ≈ 50 ha | `2400×0.296 = 710.4`; `710.4² = 504,668 m²` | ≈ 50.5 ha ✓ |

This directly answers the r47 failure class: no unverified arithmetic remains in the reviewed bytes.

### 2.3 The worked example is internally consistent

`C01:246-270`. The update rule is stated once (`C01:260`): "re-surveyed when the levy year turns; a breach … changes the **next** levy-year assessment, never the current one." The year-3 storm test applies exactly that rule: the year-3 assessment stands; the margin entry is evidence for a year-4 abatement. The "if the rule were…" table compares alternatives; it does not restate a second trigger. r47 B7/F-1 is absent. The example is declared NON-CANON in the heading and first line. The `1:5,000` and `1:25,000` scales are consistent with the same survey.

### 2.4 Depth verdict

**PASS on substance.** The draft keeps r47's load-bearing decision surfaces (same 7-link chain, same 8 forms — now complete — plus an 11-row calibration bank) at **30.7% of r47's 739-line body**, with 81 table rows against 240. It is denser, not thinner: every section ends in a rule, a table, or a decision row. It is not a map history and not filler.

---

## 3. Content defects in the integrated draft

### F1 (P1) — the `- topic:` line is not the seed line

| Source | Chars | sha256 (line + `\n`) |
|---|---:|---|
| r44 seed `K02-gap-scout.md:227` | 775 | `9424fb81c22fe8c9a468d75aa291e1b5943a268b8699320915de52d7bda3459a` |
| C02 header `:114` | 775 | `9424fb81…` (byte-equal, C16 verified) |
| **C01 entry `:73`** | **1,054** | **`1727a550259d0c97f6a5c459f1ecae8a2f4b696c78c628e8b099a064152bfd5f`** |

C01 rewrote the topic ("the map as a made instrument and a claim about space … the survey → control → projection → symbol → reproduction chain …"). Content-wise it is a good topic; **provenance-wise it breaks the round's own chain**: C16 certified byte-equality at C02, and C10's README rev 2.5 row is built from the seed text. The sweep compares the README row to the entry's `- topic:` (`reports/round-28/readme/sweep.py`, `topic_of`/`ROW_RE`), so a seed-based row against C01's entry will report `topic_mismatch`. **Fix:** either restore the seed text in C01 (`:73`) or record the topic change as an explicit act and make C10 copy C01's 1,054-char line byte-for-byte. Do not land C01's entry with C02's/seed's topic.

### F2 (P1) — star chart is both excluded and claimed

- `C01:99`: "a **star chart** indexes the sky, not the ground (**another register's sheet**)" — a failure under the five-condition test.
- `C01:149`: the form table lists "**celestial/star chart**" as one of the eight map forms.
- `C01:77` (`- couples:`): "`celestial-symbolism-calendars.md` … this entry **owns the star chart as a map form**."

One of these must change. The clean fix is to define condition 1 as a **referent space** under a stated correspondence (ground *or* sky), as r47's P3-1 already suggested ("referent-indexed", not "ground-indexed"), and let the star chart pass as "a map of a non-terrestrial referent". The alternative — dropping the celestial row from the eight forms and the celestial couples token — costs a form and contradicts the `- topic:`. Recommend the first.

### F3 (P1) — the boundary table omits the parcel/claim owner

`C01:103-117` has **12 data rows** (cosmology, sacred topography, direction, celestial, architecture, writing media, transport, naming, craft, trade, Mesoamerica, sacred kingship). It omits `culture-material/agrarian-field-system-lexicon.md`, which owns PARCEL/CLAIM and the tenure/boundary/land-measure vocabulary (`:42,:45`, read live). C07 filed this as **U1, the sharpest under-claim**, precisely because C01's cadastral form is central. `C01:77` `- couples:` also omits it. **Fix:** add E01's row (one line) and one couples token; the merged total is still under 250 (§4).

### F4 (P1) — two byte sources with incompatible decision records

The round now has two complete drafts of the same entry:

| Path | Example | Decision rows | Calibration | Boundary |
|---|---|---|---|---|
| **A: integrated** `C01-entry.md` | 25 lines (`:246-270`), one sheet/two forms | **6** `DR-CM-01..06` (`:239-244`) | 11 rows (`:271-289`) | 12 rows |
| **B: fragments** C02+M01+M02+E01 | 27 lines (`M01:28-54`), two sheets | **9** `DR-CT-01..09` (`M01:32-44`) | 10 rows (`M02:25-56`) | 13 rows (`E01:28-43`) |

Merging them section-by-section would duplicate the example, calibration and boundary, and M01's nine tags would dangle against C01's six-row record. **The integrator must choose one path.** Recommendation: **land path A**, then merge only the specific improvements that do not change its skeleton — M02's living-practice flags and E01's agrarian row. Path B's only unique content (two-sheet contrast, rule-id discipline) is already demonstrated in A's example at the 25-line ceiling.

### F5 (P2) — living-practice screen is one line

`C01:287` says only: "indigenous cartographic sovereignty — a community's map is its legal record, not a design motif. Describe the genre; do not appropriate the specific." For a topic whose real anchors are lienzos, Pacific navigation and songlines, the corpus's own gate expects routing: `real-world-inspiration-boundaries.md:97,:99,:107`, `myth-consistency-gate.md:34`, `maori.md:20`, and the `polynesia-navigation.md:71,:73` attribution rule (all re-read live; M02 quotes them). **Fix:** import M02's five flags, which occupy 5 lines (`M02:42-46`), replacing C01's one line (+4 net). The merged total is 245 (§4).

### F6 (P2) — couples path style diverges

`C01:77` names targets as `corpus/knowledge/...` rather than the partition's entry-relative `../myth-symbol/...` style used by C02 and the live entries. The basename resolver may still classify them, but a format divergence is an avoidable integration risk. **Fix:** convert to entry-relative paths, or confirm the resolver classifies all 22 tokens (C09 owns the count).

### F7 (P3) — head field divergence

C01's head has no `- source:` field (C02's has one); C01's H1 differs from C02's. The live partition uses `- source:` in only 6 of 25 entries, so its absence is not a defect — but if the integrator prefers C02's head, the two must be reconciled (F1 makes them non-interchangeable today).

### F8 (P3) — example sits exactly on the gate ceiling

The example is **25 lines** (`C01:246-270`), exactly C14's W9 hard ceiling (12–20 target, ≤25). It passes as filed, but any added sentence fails the gate. If the example is edited, compress rather than extend.

### F9 (P3) — closure vs per-leg terminology

`C01:135`: "a traverse closing to 1% on 100-pace legs carries ±0.75 m". A closure is a traverse-total quantity, not a per-leg one; the arithmetic is right under the stated convention (1% of a 75 m leg), but the sentence should say "a leg error of 1%" or "a closure of 1% over 100 paces". Content nit, not a landing blocker.

---

## 4. Right-sizing: path A fits, path B does not

**Path A (integrated):** 227 lines. Slack to 250: **23 lines**. My recommended merge — M02's bank replaces C01's 19-line bank with 32 lines (**+13**), M02's five-line living-practice block replaces C01's one line (**+4**), and E01's agrarian row (**+1**) — lands at **245**. If F2 forces a one-line redefinition of condition 1, **246**. This is the safe path: 4 lines of slack remain.

**Path B (fragments):** committed `23 (head) + 156 (other body at plan) + 32 (calibration) = 211`; the 250 ceiling leaves **39** for build order + example, and M01's 27-line example plus a 9-row build table needs ~39–40. The entry lands at **250–251 with zero slack**, and K01's 230-line target is impossible (`230 − 211 = 19`, less than the example alone). K01's budget rows are `K01:83-92`; I recomputed the sum: `27+26+18+22+22+20+20+20+33+14+8 = 230`.

Path B also carries the fragment-level defects C12 would otherwise have to report:

- **M01's 27-line example exceeds C14's 25-line W9 ceiling** by 2 (`C14:58,:84`; measured fence `M01:28-54`).
- **C02's external shelf omits Mundy, Boone, Needham and al-Idrisi**, all cited in `M02:34,:36`, while `C02:131` says the shelf *is* the external framework. C01's shelf **includes all four** (`C01:76`), which is why path A is the better base.
- **C02's `- couples:` line omits agrarian, celestial and sacred-kingship** (`C02:130`); E01's table includes all three.

---

## 5. Findings table

| ID | Severity | Finding | Evidence | Fix |
|---|---|---|---|---|
| **C12-F1** | P1 | Topic line is not byte-equal to the seed; README row would mismatch | `C01:73` (1,054 chars, `1727a550…`) vs `K02-gap-scout.md:227` and `C02:114` (775 chars, `9424fb81…`) | Restore seed text in C01, or record the change and make C10 copy C01's topic byte-for-byte |
| **C12-F2** | P1 | Star chart called "another register's sheet" yet listed/claimed as a map form | `C01:99` vs `C01:149`, `C01:77` | Define condition 1 over a referent space (ground or sky), or remove the celestial form and token |
| **C12-F3** | P1 | Boundary table and couples omit the parcel/claim owner | `C01:103-117`, `C01:77`; `agrarian-field-system-lexicon.md:42,:45`; C07 U1 | Add E01's agrarian row and one couples token |
| **C12-F4** | P1 | Two byte paths with incompatible decision IDs/examples; merging duplicates sections and dangles nine tags against six rows | §4 table; `C01:239-244`; `M01:32-44` | Land path A; merge only M02's flags and E01's row; do not merge path B's example |
| **C12-F5** | P2 | Living-practice screen is one line against a topic with restricted-living-tradition anchors | `C01:287`; `M02:42-46`; `real-world-inspiration-boundaries.md:97,:99,:107`; `myth-consistency-gate.md:34`; `maori.md:20` | Import M02's five flags (5 lines, +4 net; merged total 245) |
| **C12-F6** | P2 | Couples paths use repo-relative style, not partition-relative | `C01:77` | Convert or confirm resolver classification |
| **C12-F7** | P3 | Head field/H1 divergence between C01 and C02 | `C01:70-80`; `C02:111-135` | Choose one head; if C02's, reconcile F1 first |
| **C12-F8** | P3 | Example exactly at the 25-line gate ceiling | `C01:246-270`; `C14:84` | Any edit must compress, not extend |
| **C12-F9** | P3 | "closing to 1% on legs" is loose terminology | `C01:135` | Say "a leg error of 1%" |

**No depth defect.** No filler paragraph, no vocabulary-only typology, no fabricated source, and no unverified arithmetic in the reviewed bytes. "Real content, not landing-ready" now means "real content, five small fixes from landing".

---

## 6. What remains unverified

1. **The assembled landing file.** Path A's 227 lines are the draft; the integrator's merge (M02 flags + E01 row) must be re-measured. Target: ≤250; predicted 245–246.
2. **The README rev 2.5 row.** Depends on F1: it must equal whichever topic the landed entry carries. I did not edit or stage the README (C10 owns it).
3. **The post-apply sweep.** `sweep.py` must read 224/224, zero topic mismatch. C11 proved a staged 224 sweep green with the seed topic; if C01's topic lands, C11's stage must be re-run with that row.
4. **C01's own self-audit claims** (`C01:317-451`: contract checklist, B1–B9 audit, 40-odd anchor rows). I spot-checked the arithmetic and ~10 anchors; I did not reproduce every anchor (C04/C06 own that).
5. **External sources.** None inspected; every external date/edition remains `(to-verify)` as the entry says.

---

## 7. Commands and write surface

All commands from the lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, 2026-10-19.

```text
$ git rev-parse HEAD                                → a01405dd…cf6a0af
$ find corpus/knowledge -name '*.md' | wc -l        → 223
$ ls corpus/knowledge/culture-material/*.md | wc -l → 25
$ sha256sum reports/round-48/cov/C01-entry.md       → 4c2815a7…
$ sed -n '70,296p' reports/round-48/cov/C01-entry.md | wc -l → 227
$ python3 -c "print(0.2*5000/1000, 0.2*2500/1000)"  → 1.0 0.5
$ python3 -c "import math; print(10000*math.tan(math.radians(1/60)))" → 2.909
$ python3 -c "print(200/10, 360/32, 2400*0.296)"    → 20.0 11.25 710.4
$ python3 -c "print(0.2*24000/1000, 0.2*250000/1000)" → 4.8 50.0
$ wc -l corpus/knowledge/culture-material/*.md | sort -n → min 103 / median 149 / max 221
```

Topic digests: seed and C02 both `9424fb81c22fe8c9a468d75aa291e1b5943a268b8699320915de52d7bda3459a` (775 chars); C01 `1727a550259d0c97f6a5c459f1ecae8a2f4b696c78c628e8b099a064152bfd5f` (1,054 chars).

**Write surface:** this file only — `reports/round-48/cov/C12-content.md`. Nothing under `corpus/`, `tools/`, `LOG.md` or `README` was written or staged; no filed round was edited; no git commit/push, install, network, or `run-validation.py`.
