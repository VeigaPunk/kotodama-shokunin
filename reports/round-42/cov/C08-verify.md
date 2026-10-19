- Seat: C08 | verifier | claim C | date 2026-10-19 | baseline ac47c78

# C08 — third verifier: lot-drawn spot-audit of 2 of 4 entries + the README row bytes

Round 42 (regimen 2, loop 1, position 10), seat **C08**, role **verifier**, claim **C**. Mission
(verbatim, `reports/round-42/targets.json` → `seats[id=C08].mission`): *"Third verifier: spot-audit
2 of 4 entries by lot + the README row bytes."* Out path: this file only.

**Dependency status: the claim-C block landed DURING this seat's polling window, and both lot-drawn
fragments were audited.** At seat open the tree held only `claims.json`, `targets.json`,
`telemetry/dispatch-declared.json` and `op/O09-scribe.md`; over the window C02, C03, C01, C06, K02 and
the review/cross files landed (§4 poll log). The lot drew **C02 and C03** (§3), and **both were
audited from their current bytes** — delivered in **§8 (C02)** and **§9 (C03)** — plus the mission's
second half, the **README row-bytes leg**, delivered in **§10**. Because the drafts were absent for the
first part of the window, the file is written so that the early sections state the pinned before-state
and the draw rule, and the delivered sections carry the verdicts.

One finding is this seat's own and predates the drafts: **FINDING D1 (§5)** — the round's declared
README footer vector is arithmetically wrong and, applied literally, makes claim C's `sweep-green`
threshold unreachable. It is independently reproduced by three other seats (§5). A second finding,
**D3 (§11)**, is count-blocking: the four entries declare only **three distinct landing paths** because
C01 and C04 both claim `mineral-stone-symbolism.md`.

- Lane root `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; `git rev-parse HEAD` →
  `ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4` (== declared baseline `ac47c78`,
  `reports/round-42/claims.json:7`). At close `git status --porcelain` → `?? reports/round-42/` only.
- **Writes**: this file only, plus gitignored `.scratch/c08/` (instruments, simulation trees). No
  `corpus/**` byte, no `tools/**` byte, no `README` byte, no filed round-1..41 byte touched.
- **Runner ban honored**: no `reports/round-*/run-validation.py` was executed anywhere, in-tree or
  in a copy. Filed code executed read-only: `reports/round-28/readme/sweep.py` (live + imported with
  `root_override`), `tools/source-audit-inventory.py`, and the r35 C12 runbook instrument installed
  from its own filed awk. No network, no install, no commit, no push.
- **Canon: NON-CANON.** This seat audits bytes and files defects; it admits no entry, certifies no
  round, promotes nothing, and clears nothing (`PROVINCE.md`; `corpus/QUALITY.md`). A green reading
  is a structural reading of named digests, never a verdict on the scholarship.

---

## 1. Baseline pins — re-measured, not inherited

| object | sha256 | cross-check |
|---|---|---|
| `reports/round-42/claims.json` | `513ae21042c7516e028ff21675a48590b75f69dbb321da715efd7c49f3131b58` | **equals** the `durable_sources[0].sha256` pin in `reports/round-42/telemetry/dispatch-declared.json` |
| `reports/round-42/targets.json` | `6db0a9ebcde81d555c48e80e75958f616d0990591357ee0421332b0c3c3b7b23` | **equals** the `durable_sources[1].sha256` pin, same file |
| `reports/round-42/telemetry/dispatch-declared.json` | `50d29b3f60e3cff471842796798507fc8c0df321893988eccf6dbec70713aff4` | this seat's own read |
| `corpus/README.md` | `d2eed26b30e8e62189d95446dae7d5503b6c6a398bb8e77348f878c947a5ac4f` | live sweep's own `readme_sha256`, identical |
| `reports/round-28/readme/sweep.py` | `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3` | **equals** the pin filed at `reports/round-39/cov/C06-delta-receipt.md:31` and `reports/round-40/cov/C06-delta-receipt.md` §1 |
| `reports/round-35/cov/C12-audit-runbook.md` | `06dd08eb704bdeb2269f962fd315541f9b6c0389fd3b319739210d70bcad2bde` | this seat's own read; §5 instrument extracted from it digests `973610275404e9e3183d46e33e5352562265e6c2e397c92291e63c401ed7562d` (663 lines) == the pin filed in that runbook's §4 step 0 |

Claim C's **before-state is confirmed**: `ls corpus/knowledge/myth-symbol/*.md | wc -l` → **23**;
`find corpus/knowledge -name '*.md' | wc -l` → **220**; partition census
`25/23/25/29/24/94` (linguistics / myth-symbol / culture-material / synthesis / verification /
civilizations), reproduced by two methods — `ls corpus/knowledge/<p>/*.md | wc -l` per partition and
`tools/source-audit-inventory.py --json --summary --root corpus/knowledge` (`totals.files 220`).

## 2. The README row bytes — measured on the pinned tree (two readers, one reading)

### 2.1 The filed instrument

`python3 -B reports/round-28/readme/sweep.py` at `ac47c78`, README `d2eed26b…`, **exit 0**:

```
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 23,
       "synthesis": 29, "verification": 24}
rows 220 files 220
missing_from_index 0 []      topic_mismatch 0 []      orphan_rows 0 []
header_drift {}              totals_line 220 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge",
        "total": 220, "dir_totals": [25, 23, 25, 29, 24, 94]}
footer_live {"total": 220, "dir_totals": [25, 23, 25, 29, 24, 94],
             "order": ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]}
footer_findings [] footer_ok True
readme_sha256 d2eed26b30e8e62189d95446dae7d5503b6c6a398bb8e77348f878c947a5ac4f
```

`--selftest` → `selftest: 12/12 checks passed`, exit 0.

### 2.2 This seat's own second reader

`.scratch/c08/rows.py` — an **independent implementation** (it does not import `sweep.py`) of the
same row contract: section headers `^## <part>/ (<n>)$`, rows ``- `<file>.md` — <text>``, and
`<text>` compared byte-wise against the entry's own `- topic:` head-block text with continuation
lines space-joined (terminated by the next `- <field>:` line, matching `sweep.py:61` `TOPIC_RE`).
Reading: **rows 220, missing 0, topic_mismatch 0, duplicate rows 0, filename-order violations 0** —
agreement with §2.1, one reading. *(First run of this reader reported 20 mismatches; the cause was
this reader's own topic-terminator regex, not the corpus — the two-`- topic:`-shaped cases where the
next head field is `- gap filled:`. Recorded because a "mismatch" that is the checker's bug is not a
finding; the corrected implementation is the one reported above.)*

### 2.3 Row-byte contract and insertion geometry (what the C06 delta must satisfy)

An index row is ``- `<file>.md` — <topic-text>``, byte-equal to the landed entry's own `- topic:`
text (continuations space-joined). Measured on the pinned myth-symbol section
(`corpus/README.md:196-220`):

- section header `## myth-symbol/ (23)` at **line 196**; rows at **lines 197–219** (23 rows);
- the 23 row filenames are **exactly** `sorted(os.listdir('corpus/knowledge/myth-symbol'))`, in the
  same order — so the 4 new rows insert in **filename order** inside that run, and the header moves
  to `## myth-symbol/ (27)`.

## 3. The lot — pre-registered draw rule and result

Rule (fixed before any draft lands, so it cannot be tuned to the drafts): for each of the four
entry seats named in `reports/round-42/targets.json` (`C01`, `C02`, `C03`, `C04`), compute
`sha256("round-42|<seat-id>")`; sort ascending by that hex; the mission's *"2 of 4"* are the
**first two**. Command: `printf 'round-42|%s' "$s" | sha256sum`.

| rank | seat | sha256[:12] |
|---|---|---|
| 1 | **C02** | `165cc1fa1a9f` |
| 2 | **C03** | `41a5e24037ce` |
| 3 | C01 | `7b80f046bdc1` |
| 4 | C04 | `b3a6e2854b2a` |

**Lot draw → C02 (`cov/C02-entry-2.md`) and C03 (`cov/C03-entry-3.md`).** Both were **absent when the
lot was drawn** (the draw is registered here precisely so it could not be tuned once drafts arrived);
both then landed inside this seat's window and are **audited on their current bytes in §8 and §9**.
Nothing in this file quotes, confirms, or corrects any *other* seat's verdict on either draft.

## 4. Poll log (the dependency timeline — drafts absent at open, all landed by close)

`find reports/round-42 -type f | sort` at seat open returned 4 files:

```
reports/round-42/claims.json
reports/round-42/op/O09-scribe.md
reports/round-42/targets.json
reports/round-42/telemetry/dispatch-declared.json
```

`ls reports/round-42/cov` → no such directory. `op/` held only `O09-scribe.md`, which itself records, at
its `:8-16`, that every claim-O implementation and verification output was absent at its cut —
independent corroboration of the parallel-batch timing. **Over the polling window the block landed**:
`cov/C02-entry-2.md`, `cov/C03-entry-3.md`, `cov/C01-entry-1.md` (then revised and re-slotted),
`cov/C06-delta-receipt.md`, `cov/C07-verify.md`, `scout/K02-myth-gaps.md`, `cross/X00`, `cross/X01`,
`cross/X02`, `review/R02`, `plan/P01` and the `op/` set. This seat is therefore in the position r40's C07
was in (`reports/round-40/cov/C07-verify.md:9-11`) — it re-measures the whole verifiable surface itself —
**but unlike r40's C07, both lot-drawn fragments arrived in time and are audited (§8, §9).** Only
`cov/C04-entry-4.md` never appeared.

---

## 5. FINDING D1 — the round's declared README footer vector is arithmetically wrong and, applied literally, fails the sweep

**Statement.** `reports/round-42/targets.json` → `seats[id=C06].mission` declares the README rev-2.4
delta as *"myth-symbol 27, totals 224, vector 25/23/27/25/24/94, 4 rows in filename order"*. That
declared vector is internally inconsistent with its own declared total, and its moved slot is the
wrong partition.

**Evidence 1 — arithmetic.** The footer vector is read in **README section order**, not
alphabetical and not by "partition that changed":

```
order = ["linguistics", "myth-symbol", "culture-material", "synthesis", "verification", "civilizations"]
```

(`reports/round-28/readme/sweep.py:50-57` `PARTS`, confirmed live by the `footer_live.order` field in
§2.1). Under that order:

- declared literal `25/23/27/25/24/94` sums to **218**; the same mission declares `totals 224`
  (and 220 + 4 = 224). **Sum mismatch.**
- slot 3 is **culture-material**, not myth-symbol; the literal vector moves culture-material 25 → 27
  and leaves myth-symbol at 23 — i.e. it names the wrong partition and contradicts the same
  sentence's *"myth-symbol 27"*.
- the section-order-correct vector is `25/27/25/29/24/94`, which sums to **224**.

**Evidence 2 — measured, not argued.** On a copy of `corpus/knowledge` with four synthetic
myth-symbol entries staged (tree = **224 files**), the **unmodified filed sweep** imported with
`root_override` returns:

| footer bytes applied | `footer_findings` | `footer_ok` | `totals_ok` | `ok` |
|---|---|---|---|---|
| `total 224` + vector `25/23/27/25/24/94` (**C06 literal**) | `[{"class":"FOOTER_DIR_TOTALS","declared":[25,23,27,25,24,94],"live":[25,27,25,29,24,94],"order":[...]}]` | **False** | True | **False** |
| `total 224` + vector `25/27/25/29/24/94` (section order) | `[]` | **True** | True | **True** |
| control: stale before-vector `25/23/25/29/24/94` | `[FOOTER_DIR_TOTALS …]` | False | True | False |

So the literal declared bytes produce a red sweep; the corrected vector produces the green reading
claim C's threshold requires (*"README rev 2.4 sweep-green 224==224"*). The third row is the
**negative control**: the instrument does flag a footer that names the wrong myth-symbol slot, so
row 1 is a real rejection and not an instrument that never fires.

**Precedent that this is a new slip, not house convention.** r39's C06 mission declared
`21/23/25/29/24/94` (sums 216 == its declared totals 216) and r40's declared
`21/23/25/29/24/94 → 25/23/25/29/24/94` (sums 220 == its totals 220) — both self-consistent, both in
section order, both correct at their rounds. r42 is the first mission vector whose slots do not sum
to its own declared total. (The lane has prior form for mission text carrying stale figures which
the executor must correct: r40's C06 mission read "totals 212→216→220" while the true delta leg was
216→220, noted at `reports/round-40/cov/C06-delta-receipt.md:20-22`.)

**Disposition requested of the integrator.** Treat C06's vector token as **`25/27/25/29/24/94`**
(slot 2, myth-symbol) and its `totals 224` as correct; do not apply `25/23/27/25/24/94` to
`corpus/README.md`'s counts footer. The remaining rev-2.4 legs the mission names are unaffected and
verified: header `## myth-symbol/ (23)` → `(27)`, totals line `220` → `224`, and 4 rows inserted in
filename order (§2.3). **The post-apply sweep reading remains the integrator's to measure** — this
seat's 224-file reading is a **simulation on synthetic entries**, never a reading of a delivered
revision (the `readme-prediction-vs-delivery` rule, `reports/round-37/op/defect-queue.json:242-251`).

**Severity: S2 (blocker for claim C's sweep-green threshold if applied literally).** It is not a
defect of any landed byte — the pinned README is clean (§2.1) — and it is not a defect of C06's
authoring, which has not happened yet; it is a defect in the round's own declared target.

## 6. Structural-contract calibration for the entry drafts (the reader §8/§9 audits with)

The delivered audits (§8/§9) run the r35 C12 runbook instrument. To prove that reader is live and
calibrated on this tree, it was run here on the **four round-40 template entries** — the exact
authoring shape the round-42 drafts copy:

| entry | contract `pass` | `clean` | contract defects | review observations |
|---|---|---|---|---|
| `linguistics/taboo-strata-lifecycle.md` | True | **True** | 0 | 0 |
| `linguistics/dialect-register-consistency.md` | True | False | 0 | 1 |
| `linguistics/translation-protocol-fidelity.md` | True | False | 0 | 3 |
| `linguistics/sacred-registers-liturgical-language.md` | True | False | 0 | 1 |

Instrument digest `97361027…` == the filed pin; `--selftest` → `SELFTEST PASS` exit 0;
`--census --json` over the live corpus → `{"total": 220, "pass": 40, "clean": 15}` (this seat's own
calibration reading, not the runbook's 201-entry baseline). The review observations are ordinary-word
artefacts of the bleed word-list (`closure`, `canon`/`canonical`) and are **review tier**, never
contract failures — the runbook's own limit (`reports/round-35/cov/C12-audit-runbook.md:46-49, §8
limit 4`). **Reading to carry:** `pass` = families 1–4; `clean` = `pass` **and** zero review items.
The claim-C threshold is *"audits 4/4 PASS"*, so review-tier items do not fail it.

This seat's **own** second reader (`.scratch/c08/legs.py`, independent implementation of families
1a/1b/1c/4 + decision-record + pointer resolution) agrees on all four templates:
`R35-4F-1` 4/4 True, round-10 5-field set True, `verified_at_iso` True, gap named True,
decision record True, and **0 unresolved pointers** other than the glob token
`corpus/knowledge/*/*.md` (a grep pattern, not a file path — reported as an instrument limit, not a
dangling pointer). Two readers, one verdict on the calibration set.

## 7. The check set the delivered audits (§8/§9) were run under

This is the protocol **as executed**, kept verbatim so the readings can be re-derived:

1. `awk '/^```python$/{f=1;next} /^```$/{f=0} f' reports/round-35/cov/C12-audit-runbook.md > .scratch/c08/entry-audit-runbook.py`
   and verify `sha256sum` == `97361027…` (663 lines) **before** using it. — **done**: digest matched.
2. Stage the lot-drawn fragment **alone** into a directory containing only it, then
   `--fragments <dir> --stage <stage>`; read `pass`/`clean` per entry and every `contract_defect`.
   — **done for both**, and the stager's target guess was **overridden** by the fragment's own declared
   path (see the hazard note below).
3. Re-run the round-35 check families **1–4** (frontmatter `R35-4F-1`, resolving pointers with
   brace expansion one level, decision record, gap statement) plus **5a–5c** as review tier. — **done**.
4. **Fabrication hunt, independent of C05/C07:** for each cited `path:line` and each quoted
   `- topic:`/`- sources:` string in the draft, resolve the target and read the cited line;
   every count the draft states must be reproduced by this seat's own command, not quoted. — **done**:
   9 anchors for C02, 8 for C03, and the absence-sweep counts re-run (§8 D2-a/b/c).
5. Cross-check the declared landing filename against the README row bytes (§2.3) and the
   filename-order insertion; a declared name that does not sort where the row is placed is a finding.
   — **done** for C02, C03 and (row-leg corroboration) C01's re-slotted deliverable.
6. Report verdicts as `pass`/`clean` separately; **no C05 or C07 claim may be quoted, confirmed, or
   corrected** — this seat re-measures from primary bytes (the r40 C07 protocol,
   `reports/round-40/cov/C07-verify.md:9-11`). — **done**: no C05 claim is available or used; R01's
   count finding is cited only as *independent corroboration* of this seat's own measurement.

**Stager hazard found and worked around (recorded for the integrator).** The r35 C12 stager derives a
fragment's target path from the **first `corpus/knowledge/...` token it finds**, so on C02 it mapped the
fragment to `corpus/knowledge/myth-symbol/animal-symbolism.md` — a *cited exemplar*, not the landing
target (C02's fragment opens with a cited path list before its own declared-path line). This seat
therefore staged from the **declared path** (`purity-pollution-systems.md`) after extracting the fence
by line range, and audited those bytes. Any integrator using that stager on a fragment whose citations
precede its declared path will silently overwrite an existing entry.

## 8. DELIVERED — spot-audit 1 of 2 by lot: C02 (`cov/C02-entry-2.md`)

**Both lot-drawn fragments landed during this seat's polling window**, so the spot-audit is delivered
on the current bytes rather than owed. C02 landed first (fragment sha256
`474c7fac52f4f6ef239e206f1e309df255306fe11c880b98df83625f46740938`, 236 lines / 61,553 bytes).

**Audited bytes.** Fence run at lines **13/201**; the entry block is lines 14–200 = **187 lines /
49,976 bytes**, sha256 `02b3536cf118c7dc322b3a1839b5533f9e5abc6953efcb310dafd80cae0b60a7`.
Declared landing path `corpus/knowledge/myth-symbol/purity-pollution-systems.md` — **verified new**:
the slug does not exist at `ac47c78` (`ls` → no such file), so this is an addition, not a collision
with an existing name.

**Contract verdict: `pass` = True, `clean` = False, contract defects = 0.**

| leg | reading |
|---|---|
| `R35-4F-1` frontmatter 4/4 (`sources`, `verified-at`, `recheck`, `couples`) | **True**, `frontmatter_4of4_missing []` |
| round-10 5-field set | **True** |
| `verified_at_iso`, no empty scalar field | **True** |
| gap statement | **True** (`- gap filled:`) |
| decision record | **True** (`## 13. Decision record`; ids `DR-PP-01`…`DR-PP-15`, 15 distinct) |
| resolving pointers | **0 unresolved** |
| `- couples:` targets | **36/36 resolve** (resolver bases: entry dir, `corpus/knowledge/`, lane root) |
| review-tier observations | `bleed-candidate:closure,promote,promoted`; `canon-mention-unnegated:canon,canonical` |

The two review items are ordinary-word artefacts of the runbook's bleed list
(`reports/round-35/cov/C12-audit-runbook.md:46-49`, §8 limit 4) and are **review tier, never contract
failures** — the same class the four r40 template entries produce (§6). Structure: 14 `##` sections,
incl. §12 NON-CANON worked micro-example and §14 canon-boundary/handoff.

**Content spot-checks (this seat's own reads, all reproduce).** Nine cited `path:line` anchors read at
their cited lines: `symbolism-synthesis-method.md:40` (the Douglas row), `:68` (anomaly picks your
taboo), `animal-symbolism.md:69` (pig taboo, Douglas-anomaly vs Harris-cost), `plant-symbolism.md:20`
(the machinery transferred, "do not re-derive"), `death-afterlife-eschatology.md:49` (corpse status a
separate variable), `ritual-liminality.md:57` (piacular row), `bathing-and-body-hygiene.md:50` (the
status/contamination split), `israel-ancient-hebrew.md:150` (intersecting classifications),
`eschatology-world-end-systems.md:105` (the purity-movement row) — **every one matches the claim it is
cited for**. The absence sweep that constitutes the gap evidence reproduces exactly:
`pollution`/`impurity`/`defilement`/`contagion`/`purification`/`lustration`/`abomination` as
`^- topic:` owners → **0 each**; `boundary maintenance` → **0**; `taboo` topic-owners → **8**.

**Defects found — three stated counts carry the wrong unit or flag (D2-a/b/c).** This seat measured
every variant to pin the unit:

| C02 claim | this seat's measurement | verdict |
|---|---|---|
| `taboo` appears in **122 files** | `grep -rl` → **121**; `grep -ril` → **122** (the one extra file is `corpus/knowledge/civilizations/celts.md`, matched only case-insensitively) | **case-insensitive count reported as case-sensitive** |
| `Douglas` carried by **31 files** | `grep -rl Douglas corpus/knowledge/*/*.md \| wc -l` → **13 files**; **31** is the case-insensitive **line** count, 32 the case-sensitive line count, 33 case-insensitive occurrences | **line count reported as a file count** |
| `purity` **41 files** | `grep -rl` → **39** case-sensitive | **case-insensitive count reported as case-sensitive** |

**Severity S3** — none of the three is load-bearing: the gap argument rests on the **zero** counts, and
every zero reproduces. **Independent corroboration:** `reports/round-42/review/R01-review.md:275-283`
records the same three, same class, same fix, measured independently — a second reader reaching the
same unit diagnosis.

**Digest-pin defect (D2-d).** C02's fragment pins the staged block as sha256
`14455ddce6deb33a2ccf3b78cc2fd8590bc43f8faf9f3cab9cb7e7854c35b942` (`49,977` bytes, `188` lines) and a
superseded pre-amendment block as `10a60568…`. **Neither reproduces on the current fragment.** This
seat searched 8 block starts × 41 block ends × 3 join conventions (LF, LF+trailing, CRLF) and found
**no convention** yielding `14455ddc…`; the current block is 187 lines / 49,976 bytes / `02b3536c…`.
The fragment itself discloses the revision sensitivity ("re-run if the fragment is revised"), so this
is a **stale revision-bound pin, not a fabricated digest** — but it is unreproducible and any auditor
reading that pin against the current bytes gets a mismatch. **Disposition:** audit the current block at
`02b3536c…` (this seat's reading); the pin needs a re-stamp with the fragment's current bytes. Severity
S3.

**Boundary.** C02's own `- topic:` line is **single-line** (row-emittable byte-equal, §10). This audit
certifies structure and reproducibility of cited bytes only — **never** the scholarship, never canon.

## 9. DELIVERED — spot-audit 2 of 2 by lot: C03 (`cov/C03-entry-3.md`)

C03 landed after C02, and was **revised once more before this seat's close** — the readings below are
re-measured on the **current** revision. Current fragment sha256 (this seat's own read, prefix as
measured) `d7daa54b313233ed…`; 226 lines / 72,611 bytes. Fence run at lines **14/196**; the entry block
is lines 15–195 = **181 lines / 63,164 bytes**, sha256 `241113b5a1259b04…`. Declared landing path
`corpus/knowledge/myth-symbol/sacred-topography-pilgrimage.md` (fragment `:9`) — **verified new** and
**sort-clean**: it sorts between `sacred-kingship-mythic-charter.md` and `symbolism-synthesis-method.md`,
inside the existing 23-name run. The current row is **1603 chars**, sha256 `6a3062834e5e8ab9…`.
*(The revision moved the block's `- topic:` text: the earlier reading was 181 lines / 62,848 bytes /
`710749794a380839…`. Both revisions pass every contract leg — the pins here are the current ones.)*
**Caveat on slugs:** the block's `- couples:`/anchor prose cites many `myth-symbol/*.md` paths, so any
regex that takes the *first* `myth-symbol/<slug>.md` token in the fragment resolves to a **cited
exemplar** (`plant-symbolism.md` for C03) rather than the landing path; the declared path must be read
from the fragment's own `Proposed landing path` line, never inferred (§7 stager hazard).

**Contract verdict: `pass` = True, `clean` = False, contract defects = 0.**

| leg | reading |
|---|---|
| `R35-4F-1` frontmatter 4/4 | **True** (`fields`: gap, topic, sources, couples, source, verified-at, recheck, scope) |
| round-10 5-field set | **True** |
| `verified_at_iso`, no empty scalar field | **True** |
| gap statement | **True** |
| decision record | **True** (`## 10. Decision record`; `DR-ST-01`…`DR-ST-12`, 12 distinct, plus one cross-reference `DR-TR-02` to another entry's id — noted, not a defect) |
| resolving pointers | **0 unresolved** |
| `- couples:` targets | **39/39 resolve** |
| review-tier observations | `canon-mention-unnegated:canon` (1) |

Structure: 12 `##` sections, incl. §11 the `(to-verify)` census and §12 handoff note. Content
spot-checks reproduce: `cosmology-cosmography.md:25` (§1 frame), `direction-symbolism.md:25` (valence
axis), `ritual-liminality.md:32` (death row), `architecture-settlement-lexicon.md:1` (title),
`divination-omen-systems.md:100` (procedural escape), `greece-classical.md:71` (Apollo/Artemis row),
`india-vedic.md:126` (purification precedes changed status), `calendar-festival-systems.md:1` (title) —
each matches the claim it is cited for.

**Note on the fence shape.** C03's fragment carries **one** ` ```markdown ` fence at `:14` closed at
`:196` (unlike r40's C03, which shipped an entry fence plus a receipt fence). No staging hazard of that
class here.

**Note on `DR-TR-02`.** C03's decision record cites one id outside its own `DR-ST-` series. Read at the
cited line it is a cross-reference to a sibling entry's decision row, not a mis-numbered local rule.
Recorded as an observation, not a defect — the r35 check family for decision records is presence-based
(`reports/round-35/cov/C12-audit-runbook.md:39`).

## 10. DELIVERED — the README row-bytes leg (the mission's second half)

C06's delta receipt (`cov/C06-delta-receipt.md`) landed during this window and pins row bytes for the
two fragments that had landed at its cut. **This seat reproduced both of C06's pins from the fragments
independently** at the revision C06 measured, using its own implementation of the row contract
(`` - `<file>.md` — <topic-text> ``, `- topic:` continuations space-joined, terminated at the next
`- <field>:` line — the `sweep.py:61` `TOPIC_RE` semantics):

| fragment | declared path | C06 row sha256[:16] | C06 row chars | this seat's row sha[:16] | this seat's chars | verdict |
|---|---|---|---|---|---|---|
| `cov/C01-entry-1.md` | `myth-symbol/purity-pollution-codes.md` | `40352909f5e02042` | 1232 | `40352909f5e02042` | 1232 | **MATCH** |
| `cov/C02-entry-2.md` | `myth-symbol/purity-pollution-systems.md` | `5102fb21aa45c558` | 2091 | `5102fb21aa45c558` | 2091 | **MATCH** |

**Both fragments were then revised again, and C01 re-slotted — so C06's C01 row is now stale, and that
is the correct outcome.** C01's current fragment (sha256 `b7140ce069ee55382c61326f4c6fa74a6f02d458506e1b2f60623f5f3d43faa3`,
538 lines / 129,691 bytes) declares **`mineral-stone-symbolism.md`** as its deliverable and retains the
purity draft as a **marked spare** in a second fence (`:291-516`) — it says so at its `:1` and `:13-27`.
The **collision C06 raised as D2 is therefore resolved by the wave's own record**, not left to the
integrator: C02 filed first, K02 §R4 dispositioned the slot to C02, and C01 moved to K02's **R1**
(`mineral-stone-symbolism.md`). This seat's readings on the current C01:

- **deliverable block** (4-backtick fence `:50-267`, i.e. lines 51–266): **216 lines / 55,102 bytes**,
  sha256 `7f102a5e376ec0e5644bf862a76c9aa0a8398e5bacab7ff495579b674d8b4755`; its `- topic:` yields the row
  ``- `mineral-stone-symbolism.md` — <text>`` at **1370 chars**, sha256 `522e5ae5b83c78f8…`;
- **spare purity block** (5-backtick fence `:291-516`): **224 lines / 57,900 bytes**, sha256
  `97efd923f6677c8be48223cccbceb35dca13b89904fe0b2d38b6714c36790cb2` — **the integrator must not stage
  this block as a second myth-symbol entry** (it would re-create the duplicate-topic collision D2);
- **sort position of the deliverable is clean**: `mineral-stone-symbolism.md` does not exist at `ac47c78`
  and sorts between `hero-journey-variants.md` and `motif-index-usage.md`.
- contract reading on the deliverable (row-leg corroboration, since C01 was **not** in this seat's lot):
  `pass` True, **0 contract defects**, `4of4` True, gap True, decision record True, pointers unresolved 0,
  one review item (`canon-mention-unnegated:canon,canonical`).

**Fence digests, by contrast, do not match C06's pins — and the reason is structural, not a defect.**
C06 pins the C01 fence at `9cd81b0d5c1c5cab…` and the C02 fence at `2d184a2159b4412e…`; at the revision
C06 measured, this seat extracts different fence digests, and after the later C01 re-slot they differ
again. The reading to carry: **the row pins reproduced byte-for-byte at C06's revision, while the
whole-fence digests moved** — a row pin is the more durable artifact than a fence pin, which is exactly
why the row, not the fence, is what lands in the index. The integrator's generator re-emits from landed
bytes at apply time regardless.

**Insertion geometry re-confirmed.** Header `## myth-symbol/ (23)` → `(27)`; totals line `220` → `224`;
the four rows insert in filename order inside the existing run at `corpus/README.md:197-219` (§2.3).

**Slot arithmetic after the re-slot.** The three distinct slots are `purity-pollution-systems.md` (C02,
after `plant-symbolism.md`), `sacred-topography-pilgrimage.md` (C03, between
`sacred-kingship-mythic-charter.md` and `symbolism-synthesis-method.md`), and `mineral-stone-symbolism.md`
(claimed by **both** C01 and C04, between `hero-journey-variants.md` and `motif-index-usage.md`). **Four
entries, three distinct paths** — see **D3 (§11)**, which is count-blocking for the 23 → 27 move.

## 11. FINDING D3 — the four entries declare only three distinct landing paths (C01 and C04 collide)

`cov/C04-entry-4.md` landed at the very end of this seat's window (fragment sha256
`3947fd45580538bf4d909fe8eeb1667504af8d749e47ed245e606967e5acab4b`). It declares, at its `:5`, the
landing path **`corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`** — the **identical path C01
re-slotted to** (§10). The four entries therefore declare **three distinct targets**:

| seat | declared landing path | distinct? |
|---|---|---|
| C02 | `myth-symbol/purity-pollution-systems.md` | yes |
| C03 | `myth-symbol/sacred-topography-pilgrimage.md` | yes |
| C01 | `myth-symbol/mineral-stone-symbolism.md` | **collides with C04** |
| C04 | `myth-symbol/mineral-stone-symbolism.md` | **collides with C01** |

**Cause: a write-order race, visible in the fragments themselves.** C04's slot map (`C04-entry-4.md:17`)
records *"C01 → `purity-pollution-codes.md`"* — C01's **superseded** revision — and its collision check
(`:23`) measured only that no `mineral*`/`ston*` file existed yet, which was true. C04 could not see
C01's later re-slot because C01 re-slotted after C04's read. **C04 is not at fault; the wave's own
write order produced the collision.**

**C01 anticipated its own disposability and C04 did not.** C01's fragment keeps the purity draft as a
**marked spare** in a second fence and says so at its `:1` and `:21` ("the integrator may re-slot it"),
so C01 has a stated fallback. C04 ships **one** three-backtick block and no alternate. **If the
integrator applies both declared paths, C04's bytes silently overwrite C01's** — the exact hazard class
recorded in §7 (the stager takes the first `corpus/knowledge/...` token as the target).

**C04's own bytes, measured (row-leg corroboration only — C04 was not in this seat's lot).** Fence run
`:53/246`; block = lines 54–245 = **192 lines / 61,884 bytes**, sha256 `c99f44ca79a7c503…` on the
revision current at this seat's close; its `- topic:` yields the row ``- `mineral-stone-symbolism.md` —
<text>`` at **2110 chars**, sha256 `125fc4ffed95401d…`. Contract reading: `pass` True, **0 contract
defects**, `4of4` True, gap True, decision record True (`DR-MS-01`…`DR-MS-10`), pointers unresolved 0,
one review item (`canon-mention-unnegated:canon,canonical`). **C04 churned heavily during this window**
(four distinct fragment digests observed: `3947fd45…` → `1e616b76…` → `09ca1841…` → `540c5653…`), but
its **block digest `c99f44ca…` and its row bytes `125fc4ff…` / 2110 chars were stable across every
revision after the first** — re-verified against the live fragment at this seat's close. That is the
same lesson as §10: the row is the durable artifact and the whole-file digest is not. **Every C04 pin
must still be re-taken at apply time**, since the fragment is plainly still being edited.

**Disposition requested of the integrator.** Admit **exactly one** of C01's deliverable and C04's
deliverable for the `mineral-stone-symbolism.md` slot, and land the other seat's entry at a different
distinct slug (or drop it). The round needs **four distinct new myth-symbol files** to reach 27; three
distinct paths plus a duplicated fourth gives 26, not 27, and the sweep's header leg would read
`## myth-symbol/ (27)` against 26 files. **This is a count-blocking defect for claim C** (severity S2),
and it is the wave's write order, not either seat's scholarship, that produced it.

## Owed

- **`cov/C04-entry-4.md`** was not in this seat's lot draw (§3), so this seat owes no audit of it; the
  chartered 4/4 audit is C05's (`cov/C05-audit.md` was absent at this cut). Its contract reading and row
  bytes are nevertheless measured in §11 (row-leg corroboration), and its path collision with C01 is
  filed there as **D3**.
- **The C06 delta's C03, C01 and C04 rows.** C06's delta landed **before C03 and before C01's re-slot**,
  so its §7 table records C03's row as `owed` and pins C01's row to the retired `purity-pollution-codes.md`
  slot. C03 has since landed (`sacred-topography-pilgrimage.md`, §9), C01 has re-slotted to
  `mineral-stone-symbolism.md` (§10), and C04 has landed declaring that **same** path (§11, D3), so
  **all four rows must be regenerated from landed bytes at apply time**; only C02's row is current.
- **The C01/C04 path collision (D3).** Both declare `mineral-stone-symbolism.md` (§11). One must be
  re-slotted or dropped before apply, or the round lands 26 files against a `(27)` header.
- **Post-apply sweep reading.** §5's green reading is a **224-file simulation on synthetic entries**,
  not a reading of a delivered revision. The real `sweep.py` exit 0 at `224 == 224` on the post-landing
  tree is the integrator's measurement and is the only reading that can satisfy claim C's threshold.
- **Re-stamp of C02's staged digest pin.** The fragment's `14455ddc…` does not reproduce on the current
  bytes (§8, D2-d); the current block is `02b3536c…`.
- **`reports/round-42/run-validation.py`** did not exist at this seat's cut. Claim C's declared counting
  command `python3 reports/round-42/run-validation.py` therefore cannot be run — and per the absolute
  shared rule it must never be run in-tree by this seat even once it exists.

## Citations

- Assignment and boundaries: `reports/round-42/targets.json` (seat `C08`, out `cov/C08-verify.md`;
  `shared_rules` incl. the in-tree run-validation ban and the filed-byte rule); `reports/round-42/claims.json`
  (claim C, before-state `myth-symbol 23`, total 220; thresholds *"sweep green; audits clean"*; non-goals).
- Baseline and dispatch: `git rev-parse HEAD` → `ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4` (== `claims.json:7`);
  `reports/round-42/telemetry/dispatch-declared.json` (`baseline_commit ac47c78`, devin/`deepseek-v4-1-flash-high`,
  32 requested, 1 batched call, `closing_snapshot: open-at-seat-close`); `git status --porcelain` → `?? reports/round-42/`.
- Instrument and pins: `reports/round-28/readme/sweep.py` (digest `9b2ccac0…`; `PARTS` order `:50-57`;
  `ROW_RE :60`; `TOPIC_RE :61`; `topic_of :74-82`; footer leg `:163-189`; `main :411-427`; selftest `:394-401`).
- Row contract and insertion geometry: `corpus/README.md:196` (section header), `:197-219` (23 rows),
  `:532` (totals line), `:534-536` (counts footer); `corpus/README.md` sha256 `d2eed26b…`.
- Defect D1: `reports/round-42/targets.json` → `seats[id=C06].mission` (vector `25/23/27/25/24/94`, totals 224);
  `reports/round-40/targets.json:86` and `reports/round-39/targets.json:72` (the two prior, self-consistent vectors);
  `reports/round-40/cov/C06-delta-receipt.md:20-22` (precedent that mission arithmetic needs executor correction);
  `reports/round-37/op/defect-queue.json:242-251` (`readme-prediction-vs-delivery`). Independently
  reproduced: `reports/round-42/cross/X00-connector.md:145-158` (§C4, "C06 must use
  `25/27/25/29/24/94`"), `reports/round-42/cov/C06-delta-receipt.md:22-31` (§2),
  `reports/round-42/scout/K02-myth-gaps.md:539-541`.
- Calibration reader: `reports/round-35/cov/C12-audit-runbook.md` (digest `06dd08eb…`; check families §1 `:26-44`;
  reading rule §2 `:51-63`; recipe §4 `:85-122`; instrument §5; limits §8) and its four template readings
  `corpus/knowledge/linguistics/{taboo-strata-lifecycle,dialect-register-consistency,translation-protocol-fidelity,sacred-registers-liturgical-language}.md`.
- Row-byte leg: `reports/round-42/cov/C06-delta-receipt.md` §7 table (`40352909f5e02042…` / 1232 chars;
  `5102fb21aa45c558…` / 2091 chars; fence pins `9cd81b0d…`, `2d184a21…`), §7 FINDING D2 (the C01/C02 collision),
  §5.2 (same-slot geometry); `reports/round-42/scout/K02-myth-gaps.md:306-337` (§R4 disposition and R1–R3
  candidates); `reports/round-42/cov/C01-entry-1.md:1,:13-27` (the re-slot note and its retained spare);
  `reports/round-42/plan/P01-plan.md` (the candidate ranking C01 cites).
- Collision D3: `reports/round-42/cov/C04-entry-4.md:5` (declared `mineral-stone-symbolism.md`), `:17` (its
  slot map naming C01's superseded `purity-pollution-codes.md`), `:23` (its collision check), `:259`
  (its own report of the C01+C02 purity pair); `reports/round-42/cov/C01-entry-1.md:3` (the same slug).
- Audited fragments (pins re-measured at this seat's close; **several moved during the window**, so each
  is stated with its current value and the churn noted in §9/§11): `reports/round-42/cov/C02-entry-2.md`
  (whole `474c7fac52f4f6ef…`; block lines 14–200, 187 lines / 49,976 bytes /
  `02b3536cf118c7dc322b3a1839b5533f9e5abc6953efcb310dafd80cae0b60a7`; declared path
  `purity-pollution-systems.md`); `reports/round-42/cov/C03-entry-3.md` (whole `d7daa54b313233ed…`;
  block lines 15–195, 181 lines / 63,164 bytes / `241113b5a1259b04…`; row `6a3062834e5e8ab9…` / 1603
  chars; declared path `sacred-topography-pilgrimage.md`); `reports/round-42/cov/C01-entry-1.md` (whole
  `b7140ce069ee5538…`; re-slot note `:1,:13-27`; deliverable 4-backtick fence `:50-267` → block
  `7f102a5e376ec0e5…`, 216 lines / 55,102 bytes, row `522e5ae5b83c78f8…` / 1370 chars; spare 5-backtick
  fence `:291-516` → `97efd923f6677c8b…`, 224 lines / 57,900 bytes); `reports/round-42/cov/C04-entry-4.md`
  (block lines 54–245, 192 lines / 61,884 bytes / `c99f44ca79a7c503…`, row `125fc4ffed95401d…` / 2110
  chars; declared path `mineral-stone-symbolism.md`; fragment digest churned
  `3947fd45…`→`1e616b76…`→`09ca1841…`).
- Independent corroboration of the count defects: `reports/round-42/review/R01-review.md:275-283` (§12, same
  three counts, same class) and its `:288-296` (the "three more topics unclaimed and unaudited" note).
- Poll/absent-dependency evidence: the early `find reports/round-42 -type f | sort` → 4 files;
  `reports/round-42/op/O09-scribe.md:8-16`; the r40 third-verifier precedent `reports/round-40/cov/C07-verify.md:9-11`.
- Command outputs (this seat, 2026-10-19, lane root, all read-only under `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`;
  no `run-validation.py` executed, no git mutation, no network, no install): `python3 -B reports/round-28/readme/sweep.py`
  → the §2.1 block, exit 0; `--selftest` → `12/12`, exit 0; `.scratch/c08/rows.py` → 220 rows / 0 mismatches;
  `.scratch/c08/legs.py` and `.scratch/c08/entry-audit-runbook.py --json` → §6 table, §8/§9 readings, and the
  C01-deliverable row-leg reading in §10; `--census --json` → `{"total":220,"pass":40,"clean":15}`; the 224-file
  simulation → §5 table (literal vector `FOOTER_DIR_TOTALS`, section-order vector `footer_findings []`); the row
  generator → §10 table (both C06 row pins reproduced byte-for-byte at C06's revision); `grep` count variants →
  §8 D2-a/b/c table.
