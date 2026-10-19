- Seat: C05 | executor (claim C) | delta receipt + staged-sha prediction | date 2026-10-19 | baseline `7ceff59`

# C05 — post-landing sweep prediction, staged-tree sha, and the claim-C delta receipt

**Assignment** (`reports/round-43/targets.json:32`, verbatim): *"Delta receipt: predict the
post-landing sweep state (224==224) and author the staged-sha prediction note per the
readme-prediction-vs-delivery durable practice — predict by staged-tree sha, cite post-apply
sweep."* Out path: this file only. Claim C read at `reports/round-43/claims.json:36-48`
(`:39` claim, `:40` before, `:41` after_required, `:42-46` counting commands, `:47` thresholds). Shared rules read at
`reports/round-43/targets.json:4-10`; the ABSOLUTE runner ban at `:8`.

**Status: DRAFT — integrator-applied, and one finding blocks the claim as declared.** This seat
wrote **zero** bytes outside this file and disposable scratch under `.scratch/c05/`: no corpus
entry, no README byte, no tool byte, no filed-round byte, no git operation. No
`reports/round-*/run-validation.py` was executed in-tree or in any copy
(`reports/round-43/targets.json:8`; the only filed code executed is the read-only
`reports/round-28/readme/sweep.py`, live and as read-only copies pointed at staged trees).

**Two results, kept separate.**

1. **The arithmetic is proven reachable on a staged tree**: 224 rows vs 224 files, 0 missing,
   0 ghosts, 0 topic mismatches, 0 header drift, totals 224, footer `[25, 27, 25, 29, 24, 94]`,
   exit 0 (§3.4). The staged README digest is `3128ec38…` and the staged knowledge-tree manifest
   digest is `be269bb6…` (§3.3) — the prediction, not the delivery.
2. **Finding D-C1**: the claim's *before* premise — "lithic slot named but unbuilt"
   (`claims.json:40`) — is false against the live tree. The r42 C04 lithic register **is landed**
   at `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` (61,884 B, sha256
   `c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f`). Landing the r42 C01
   spare as *the* stone/gem/metal register entry therefore creates a **second owner of the same
   topic**, which the r42 audit's own D1 disposition forbids ("Do **not** land both",
   `reports/round-42/cov/C05-audit.md:271-274`). The sweep goes green anyway (§4.4) because it
   counts rows and compares topic bytes; it has **no ownership leg**. §2 states the evidence and
   leaves the disposition to the integrator.

---

## 0. Verdict at a glance

| # | reading | class |
|---|---|---|
| 1 | before state: 223 files / 223 rows; myth-symbol 26; README sha `7c788a1d…`; sweep exit 0 | measured (§1) |
| 2 | the C01 spare's fenced entry is intact: 55,101 B, sha256 `6999a912…`, 9 head fields incl. `- gap filled:` | measured (§1.3) |
| 3 | **D-C1**: the lithic slot is already owned by the landed r42 C04 entry (sha `c99f44ca…`) | measured (§2) |
| 4 | staged collision-blind target `stone-gem-metal-register.md`: entry sha `6999a912…`; README 582 newlines / 583 split lines / 145,673 B / sha `3128ec38…`; tree manifest `be269bb6…` | measured on the staged tree (§3) |
| 5 | staged sweep: **rows 224 files 224**, 0 missing, 0 topic mismatches, 0 ghosts, `header_drift {}`, totals 224, footer `[25,27,25,29,24,94]`, exit 0 | measured on the staged tree, **prediction only** (§3.4) |
| 6 | controls: staged README against the live tree → exit 1; footer vector reverted → exit 1; row deleted → exit 1; duplicate-topic probe → 2 owners while the sweep is green | measured (§4) |
| 7 | the delivered state is certified by the **post-apply sweep on the landed tree**, never by §3's digest | rule, cited (§5) |

---

## 1. Before state — measured at HEAD `7ceff59`

### 1.1 Commands and verbatim output (lane root, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`)

```sh
$ git rev-parse HEAD
7ceff59a0216a8ea21ee43262d9fc72abf770cee
$ git status --porcelain
?? reports/round-43/
$ ls corpus/knowledge/myth-symbol/*.md | wc -l
26
$ find corpus/knowledge -name '*.md' -type f | wc -l
223
$ for p in linguistics myth-symbol culture-material synthesis verification civilizations; do \
    printf '%s ' "$(ls corpus/knowledge/$p/*.md | wc -l)"; done; echo
25 26 25 29 24 94
$ wc -lc corpus/README.md
575 143866 corpus/README.md
$ sha256sum corpus/README.md reports/round-28/readme/sweep.py
7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd  corpus/README.md
9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3  reports/round-28/readme/sweep.py
```

```sh
$ python3 -B reports/round-28/readme/sweep.py            # exit 0
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_live {"total": 223, "dir_totals": [25, 26, 25, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
```

The before state is green: the live README and the live tree already reconcile at 223. Any red
below is therefore caused by the delta, not carried.

### 1.2 Pins (recoverable from git + this file)

| pin | value | command |
|---|---|---|
| baseline commit | `7ceff59a0216a8ea21ee43262d9fc72abf770cee` | `git rev-parse HEAD` |
| corpus tree object | `675207b48d89688d7f9198c663bc0c2a8bcb30de` | `git rev-parse HEAD:corpus/knowledge`; the tree is clean per §1.1 |
| README | 575 lines / 143,866 B / sha256 `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` | `wc -lc`, `sha256sum` |
| index instrument | sha256 `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3` (identical to the r39/r40/r42 pins) | `sha256sum` |
| README anchors (live) | rev 2.4 block `:5-12`; `## myth-symbol/ (26)` `:205`; `sacred-topography-pilgrimage.md` row `:229`; `Total knowledge entries: 223.` `:544`; footer total/vector `:548` | `grep -n` |
| spare fragment | `reports/round-42/cov/C01-mineral-spare.md`, 55,433 B whole file; fence opens `:3`, closes `:219` | `ls -l`, read |
| spare entry bytes | **55,101 B**, sha256 `6999a9123578bf8fbae4ecfdcef5e811eb764f3aef7522830029dfc8f74dbd89` | extracted fence, hashed (§1.3) |
| live lithic owner | `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`, 61,884 B, sha256 `c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f` | `sha256sum`, `wc -c` |

The spare's entry digest `6999a912…` is the same fence digest pinned by the r42 audit for C01's
deliverable block (`reports/round-42/cov/C05-audit.md:51`), and the live lithic entry's digest
`c99f44ca…` is the content digest that audit pins for C04's fence (`:54`). The two fragments are
therefore byte-identical to the audited bytes; this seat re-extracted them independently.

### 1.3 The spare's fence (extraction)

`reports/round-42/cov/C01-mineral-spare.md` line 1 is the integrator ruling, line 3 opens
```` ```markdown ````, line 219 closes. The fenced content (lines 4–218, newline-terminated) is
55,101 B, sha256 `6999a9123578bf8fbae4ecfdcef5e811eb764f3aef7522830029dfc8f74dbd89`. Head fields
present: `- topic:`, `- gap filled:`, `- sources:`, `- calibration:`, `- couples:`, `- source:`,
`- verified-at:`, `- recheck:`, `- scope:` — 9 fields, matching the r42 audit's head-field reading.

The spare's own line 1 states its routing condition, and it is the load-bearing sentence for §2:
*"C04 lands (ownership-first structure, house convention); THIS draft is routed as the named spare
for a **future re-scoped claim**"* (`reports/round-42/cov/C01-mineral-spare.md:1`, emphasis added).

---

## 2. FINDING D-C1 — the claim's "before" is contradicted: the lithic slot is already owned

**Statement.** `reports/round-43/claims.json:40` asserts `"before": "myth-symbol 26 (lithic slot
named but unbuilt since r42's C01/C04 collision routed this draft to spare); total 223"`. The live
partition has 26 myth-symbol entries **including the lithic register**: r42's C04 entry landed as
`mineral-stone-symbolism.md` (README rev 2.4, `corpus/README.md:5-12`, and the file itself). So the
slot is *built*, not unbuilt; the spare is a second realization of the **same topic**, not a
completion of a vacant one.

**Evidence.**

1. **The live file exists and is C04's bytes.** `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`
   is 61,884 B, sha256 `c99f44ca…` — the exact content digest the r42 audit pins for C04's fence
   (`reports/round-42/cov/C05-audit.md:54`: fence match `e88cb167…`, staged content `c99f44ca…`,
   61,884 B). It is tracked and clean at HEAD (`git status --porcelain` → only `?? reports/round-43/`).
2. **Its own head claims the slot.** `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:3`
   reads *"the lithic/mineral register is absent from the partition and this entry fills it"* and
   cites the same charter sentence (`symbolism-synthesis-method.md:23,:29`) the spare cites.
   `:5` begins *"the lithic register of a fictional culture's symbolic grammar — the mineral slot
   the register family lacks"*. The spare's `- topic:` (`C01-mineral-spare.md:6`) begins *"the
   **lithic register** a fictional culture's symbolic grammar runs on stone, gem and metal"*.
   Same topic, same gap claim, two files.
3. **The r42 ruling already decided this collision.** The spare's own header says C04 lands and the
   spare is held for a *future re-scoped claim* (`C01-mineral-spare.md:1`). The r42 audit's D1
   disposition is explicit: *"Admit **one** lithic entry; either re-topic the other to the
   unclaimed R2 (dream/vision/trance) as new bytes, or drop it… Do **not** land both"*
   (`reports/round-42/cov/C05-audit.md:271-274`). The r42 LOG records the same ruling: C04 lands,
   C01 is the named spare (`LOG.md:3804-3822`, round-42 entry).
4. **The claim does not re-scope.** `claims.json:39` lands the spare *"as the partition's
   stone/gem/metal register entry"* — the same register, at a second path. The claim's own
   threshold *"no existing entry overwritten"* is satisfiable only by choosing a new filename; the
   r42 disposition is violated either way when two lithic entries exist at two filenames
   (`reports/round-42/cov/C05-audit.md:269-271`: *"two files at two slugs give 27 files but still
   only three distinct topics, and would leave the lithic register owned twice — the partition's
   one-owner rule is violated either way"*).
5. **Measured on the staged tree**: `grep -rl '^- topic:.*lithic register'` over
   `myth-symbol/` returns **2 files** with the spare staged (`mineral-stone-symbolism.md`,
   `stone-gem-metal-register.md`), **1 file** on the live tree. The staged sweep is green while
   both exist (§4.4) — the blind spot is demonstrated, not inferred.

**Consequence for claim C.** The count move 223 → 224 is arithmetically available and provable
(§3). The *coverage* move as declared — "completing myth-symbol's named lapidary slot"
(`claims.json:41`) — is not: the slot is completed by C04, and landing the spare adds a duplicate
owner. This is a **report**, not a re-route: the disposition options belong to the integrator (and
the C-scout/C06 collision seats), not to this receipt. The options visible from the evidence are:

- (a) **record the slot as already covered** by the r42 C04 landing (myth-symbol stays 26; the
  claim's count target is not pursued by this route);
- (b) **re-scope the spare** to a genuinely unowned topic as new bytes — exactly the r42 D1
  disposition's own first option (`C05-audit.md:272-273`), which is a new authoring act, not a
  byte-apply of the existing fence;
- (c) **land the duplicate anyway** and record the one-owner violation — the sweep will be green
  (§3.4), so a green sweep cannot be used as the justification.

This seat drafts §3 under a **labeled candidate path** solely to exercise the arithmetic and the
instrument; §3 is **not** a landing proposal and must not be read as choosing (c).

---

## 3. The staged-tree prediction (`readme-prediction-vs-delivery`)

### 3.1 The durable practice

`reports/round-37/op/defect-queue.json:243-249` (row `readme-prediction-vs-delivery`, class
`carried-with-owner`, owner `integrator`): *"delivered README digest differed from the audit's
staged prediction while the sweep was green; staging nuance, not a defect"*; its `next_touch`
is exactly this receipt's rule — *"note for future delta audits: **predict by staged-tree sha,
cite post-apply sweep**"* (`:248`). Evidence pinned to `reports/round-36/cov/C02-audit-delta.md`.

Accordingly §3 pins the digest of the artifact this seat **actually staged**, and §5 makes the
**post-apply sweep on the landed tree** the only certificate. A predicted digest that differs from
the delivered one while both sweeps are green is a staging nuance, recorded — not a defect and not
a delivery certificate.

### 3.2 Staged artifact recipe (disposable, `.scratch/c05/`)

- **Candidate filename**: `corpus/knowledge/myth-symbol/stone-gem-metal-register.md` — a *labeled
  arithmetic probe* chosen because it follows the partition's lowercase-hyphen convention and is
  free in the live partition (`ls corpus/knowledge/myth-symbol/` — 26 names, no such file). **The
  integrator's/C01-scout's final filename governs**; the row is re-derived mechanically from the
  landed bytes (r42 C06 rule). A different filename changes the staged README digest below and the
  row's insertion line, but **not** the four-class totals, the header, the totals line or the
  footer vector — those are partition-level.
- **Entry bytes**: the spare fence extracted as in §1.3, written unmodified.
- **README edits** (the rev 2.5 delta, applied in this order):
  1. insert the rev 2.5 block after the duplicated H1 (after live line 3), followed by a blank
     separator line — bytes staged:
     ```
     revision: 2.5 — Round-43 lithic-register spare landing (2026-10-19): the r42
     C01 lithic-register spare (routed by the round-42 integrator ruling) landed as
     `stone-gem-metal-register.md`; `## myth-symbol/` moved 26 → **27**; the totals and
     footer moved 223 → **224** and the vector 25/26/25/29/24/94 → **25/27/25/29/24/94**.
     Re-measured with `python3 reports/round-28/readme/sweep.py`: 224 rows vs 224 files, exit 0.
     ```
     (The block is displayed at list indentation; the staged bytes carry no leading spaces. The
     pinned README digest in §3.3 is authoritative.)
  2. `## myth-symbol/ (26)` → `## myth-symbol/ (27)` (live `:205`);
  3. insert the new row after the `sacred-topography-pilgrimage.md` row (live `:229`) — ASCII
     order `sacred-… < stone-… < symbolism-…`; row text is the entry's own continuation-joined
     `- topic:` (1,371 chars, newline-terminated sha256
     `0585274a97d3166f43904116e0dc0fa7b4c1aaab688fd2f34c1e64bbbc60a8ae`);
  4. `Total knowledge entries: 223.` → `224.` (live `:544`);
  5. `(total 223 files; directory totals 25/26/25/29/24/94).` →
     `(total 224 files; directory totals 25/27/25/29/24/94).` (live `:548`).
- **Not staged**: the optional dated index paragraph (r42 C06 E5 shape) — its sha must name the
  landed commit, which does not exist until delivery; and any edit to the superseded-reading
  paragraph or the carried H1/rev-2.0 defects.
- **Honesty condition on the staged prose**: the rev block's final sentence ("224 rows vs 224
  files, exit 0") is a *prediction*. It may be written only if the post-apply sweep is green; if
  the landing is not made or the sweep is red, the block must not land (the r35 placeholder lesson
  and the r42 C06 E5 rule).

### 3.3 Staged pins (the prediction)

| artifact | value |
|---|---|
| staged entry | `myth-symbol/stone-gem-metal-register.md`, 55,101 B, sha256 `6999a9123578bf8fbae4ecfdcef5e811eb764f3aef7522830029dfc8f74dbd89` (== the spare fence, unmodified) |
| staged `corpus/README.md` | **582 newlines / 583 split lines / 145,673 B / sha256 `3128ec386c320fa8d427a8f504ead263e026a2c851df72e7a46dca2545665781`** (no trailing newline) |
| staged knowledge tree | 224 `*.md` files; content-manifest sha256 **`be269bb695ad72fe3eb8d1d64c073bc00af7ee8b4e9b929ca3f206c49ae84978`** |
| manifest recipe | `sha256` over sorted lines `"<file sha256>  <partition>/<name>.md\n"` rooted at `corpus/knowledge/` |

The manifest digest is the "staged-tree sha" in the practice's sense: it pins the exact staged
tree the prediction was measured on, independent of the README's prose digest. The README digest
is conditional on §3.2's prose bytes (the C02 seat's draft may supersede them); if it differs on
delivery while the sweep is green, record the staging nuance — do not edit filed bytes to chase
the digest.

### 3.4 Staged sweep — the predicted post-landing state (measured on the staged tree)

```sh
$ python3 -B .scratch/c05/staged/reports/round-28/readme/sweep.py     # exit 0
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 27, "synthesis": 29, "verification": 24}
rows 224 files 224
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 224 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 224, "dir_totals": [25, 27, 25, 29, 24, 94]}
footer_live {"total": 224, "dir_totals": [25, 27, 25, 29, 24, 94], "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 3128ec386c320fa8d427a8f504ead263e026a2c851df72e7a46dca2545665781
```

Staged inventory cross-check:

```sh
$ python3 -B tools/source-audit-inventory.py --json --summary --root .scratch/c05/staged/corpus/knowledge
read_only True  totals.files 224
```

**Prediction stated plainly**: if the integrator lands the spare at a new myth-symbol path with
the §3.2 README delta, **the sweep will read 224 rows vs 224 files, exit 0, myth-symbol 27, footer
`25/27/25/29/24/94`.** This is measured on a staged tree and is a prediction; it is **not** a
delivery reading, and it does **not** address D-C1.

---

## 4. Controls — the staged green is informative, not green-by-construction

### 4.1 Pre-landing control: staged README against the live tree (entry absent)

```sh
$ python3 -B .scratch/c05/neg1/reports/round-28/readme/sweep.py    # exit 1
rows 224 files 223
missing_from_index 0 []
orphan_rows 1 ['myth-symbol/stone-gem-metal-register.md']
header_drift {'myth-symbol': {'declared': 27, 'files': 26}}
totals_line 224 totals_ok False
footer_findings [{"class": "FOOTER_TOTAL", "declared": 224, "live": 223, ...},
                 {"class": "FOOTER_DIR_TOTALS", "declared": [25,27,25,29,24,94], "live": [25,26,25,29,24,94], ...}]
footer_ok False
```

The delta is red until the entry lands; the staged green in §3.4 requires **both** halves.

### 4.2 Footer-vector negative control

Reverting only the staged footer vector to the before value `25/26/25/29/24/94`:
`footer_findings [{"class": "FOOTER_DIR_TOTALS", "declared": [25,26,25,29,24,94], "live":
[25,27,25,29,24,94], ...}]`, `footer_ok False`, **exit 1**. The footer leg has teeth.

### 4.3 Row-deletion negative control

Deleting only the new row from the staged README: `rows 223 files 224`,
`missing_from_index 1 ['myth-symbol/stone-gem-metal-register.md']`, **exit 1**. The row leg has
teeth, and `topic_mismatch 0` in §3.4 is therefore a real byte-equality reading (the row was
generated with the sweep's own `topic_of` semantics: each continuation line stripped, then
space-joined).

### 4.4 Ownership probe — the sweep's blind spot, measured

```sh
$ grep -rl '^- topic:.*lithic register' .scratch/c05/staged/corpus/knowledge/myth-symbol/ | sort
.scratch/c05/staged/corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
.scratch/c05/staged/corpus/knowledge/myth-symbol/stone-gem-metal-register.md
$ grep -rl '^- topic:.*lithic register' corpus/knowledge/myth-symbol/ | sort
corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
```

Two topic-owners on the staged tree, one on the live tree, **while §3.4's sweep is green**. A green
`224==224` sweep is a count/text reconciliation, not a one-owner certificate. This is the
instrument-level statement of D-C1 and the reason §0 row 5 cannot be quoted as coverage evidence.

### 4.5 Reader calibration

The live run at §1.1 is green at 223/223 with the same instrument digest `9b2ccac0…`; the staged
green is therefore a state change, not a different reader.

---

## 5. Post-apply acceptance sequence (the only certifier)

For the integrator, **on the landed tree**, after the entry and the README delta are applied in one
motion:

1. `ls corpus/knowledge/myth-symbol/*.md | wc -l` → **27**; `find corpus/knowledge -name '*.md'
   -type f | wc -l` → **224**.
2. `python3 -B reports/round-28/readme/sweep.py` → **must** read `rows 224 files 224`,
   `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `header_drift {}`,
   `totals_line 224 totals_ok True`, footer `{total 224, dir_totals [25, 27, 25, 29, 24, 94]}`,
   `footer_ok True`, **exit 0**.
3. `python3 -B tools/source-audit-inventory.py --json --summary --root corpus/knowledge` →
   `totals.files 224` (read-only).
4. `sha256sum corpus/README.md` — compare to §3.3's `3128ec38…`. **If it differs while step 2 is
   green, record the staging nuance** (C02's prose/filename choice), then record the delivered
   digest as a new reading; do not edit filed bytes and do not call the prediction a delivery
   certificate (`reports/round-37/op/defect-queue.json:248`).
5. Re-run §4.4's ownership probe on the landed tree. **If it returns 2**, register D-C1 as an open
   one-owner violation and route it to the integrator/reviewer — a green step 2 does not close it.
6. Count the final landing set: the sweep counts rows, so confirm the new row's filename is the
   one the integrator fixed (the generator re-derives the row from the landed bytes; a stale
   candidate row is a ghost/mismatch, not a silent pass).

If step 2 is not green, **no after-count in this fragment may be quoted as measured**, and the
rev 2.5 block's final sentence must not be written.

---

## 6. What this receipt does not certify

- **Not entry quality, source resolvability, or canon.** Those are C03/C04/C05-audit and R01/R02;
  this receipt owns counts, the staged digest and the reconciliation rule.
- **Not the collision disposition.** D-C1 is reported with evidence; the choice among §2 (a)/(b)/(c)
  is the integrator's, not this seat's.
- **Not the delivered README digest.** §3.3 is a staged artifact; §5's post-apply sweep is the
  certificate.
- **No write outside this file + `.scratch/c05/`.** No corpus staging in-tree, no tool byte, no
  filed-round byte, no `run-validation.py`, no freeze, no commit/push/install/network.

## 7. Owed

- **Integrator**: dispose of **D-C1** before applying the C landing — record the slot as covered,
  re-scope the spare to a new topic, or knowingly file the one-owner violation (§2). The count
  arithmetic does not decide this.
- **C02 (README draft)**: reconcile the rev 2.5 prose with §3.2; the staged README digest
  `3128ec38…` is conditional on those bytes. The mechanical legs (header/totals/footer/row) are
  the ones the sweep checks.
- **C01/C06/K02**: fix the final target filename and confirm it is free at apply time. This receipt
  used `stone-gem-metal-register.md` as a labeled probe only; if the final name differs, re-derive
  the row (mechanical) and re-hash the staged README (the tree manifest is unchanged).
- **Post-apply**: the §5 sequence, filed with the delivered digests and the sweep output.

## Citations

- `reports/round-43/targets.json:32` (this seat's mission and out path), `:4-10` (shared rules,
  `:8` runner ban); `reports/round-43/claims.json:36-47` (`:39` claim C, `:40` the contradicted
  before, `:41` after_required, `:42-46` counting commands/thresholds)
- `corpus/README.md` live bytes: `:5-12` rev 2.4, `:205` myth-symbol header, `:229`
  sacred-topography row, `:544` totals, `:548` footer vector; 575 lines / 143,866 B / sha
  `7c788a1d…`
- `reports/round-28/readme/sweep.py` (read-only; `:28-30` docstring, `:45-57` `PARTS`, `:74`
  `topic_of`, `:106` `footer_reading`, `:119` `sweep`); sha `9b2ccac0…`
- `reports/round-42/cov/C01-mineral-spare.md:1` (routing condition: "future re-scoped claim"),
  `:3` fence open, `:219` fence close; entry 55,101 B sha `6999a912…`
- `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:3` (r42 C04 gap claim), `:5` (topic
  line); 61,884 B sha `c99f44ca…`
- `reports/round-42/cov/C05-audit.md:51` (C01 fence digest `6999a912…`), `:54` (C04 content digest
  `c99f44ca…`, 61,884 B), `:262-274` (D1: same topic/path; "Do **not** land both")
- `LOG.md:3804-3822` round-42 entry (C failed as declared; C04 lands, C01 spare; 26/223)
- `reports/round-37/op/defect-queue.json:243-249` (`readme-prediction-vs-delivery`; `:248` "predict
  by staged-tree sha, cite post-apply sweep"); evidence `reports/round-36/cov/C02-audit-delta.md`
- Commands run 2026-10-19 at HEAD `7ceff59` (`export TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`): `git rev-parse HEAD`; `git status --porcelain`; the §1.1 census
  loop; `find … | wc -l`; `wc -lc corpus/README.md`; `sha256sum corpus/README.md
  reports/round-28/readme/sweep.py`; `python3 -B reports/round-28/readme/sweep.py` (green);
  fence extraction + hashing; staged tree build under `.scratch/c05/staged/`; the redirected sweep
  copy (LANE = staged root); `--json --summary` inventory on the staged root (224); negative
  controls neg1/neg2/neg3 (exit 1 each); the ownership `grep` probes (§4.4)
- Scratch (disposable, not evidence): `.scratch/c05/spare-entry.md`, `.scratch/c05/staged/`,
  `.scratch/c05/neg1/`, `.scratch/c05/neg2/`, `.scratch/c05/neg3/`
