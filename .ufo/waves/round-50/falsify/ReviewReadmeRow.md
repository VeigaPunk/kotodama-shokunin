# ReviewReadmeRow — falsify of `corpus/README.md` @ 1c779e4a

**Item attacked:** the `corpus/README.md` change landed in round 50 (commit
`1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`, base `4ad26836552462d28a946ca3b067cab0b5ce3532`),
specifically: the `revision: 2.7` block, the new row's placement and topic byte-equality, the
counts `28/226`, and the footer vector.

**Verdict: PARTIAL.** Every *measured* property of the landed change holds and reproduces at the
pin (row placement, topic byte-equality, header count 28, totals 226, footer vector, three gates
green). Two defects survive the attack:

* **S1 (medium) — prose overclaim in the revision block:** the `revision: 2.7` block asserts the
  partial owners are "cited one-way in its §2"; one of the seven enumerated partial owners is
  **not** cited in §2.
* **S2 (medium) — the acceptance criterion is unenforced:** nothing in the repo measures
  "README index row in filename order" or row-set uniqueness. `sweep.py` prints `rows`/`files`
  but does not fail on a duplicate or an out-of-order row. The property holds today, but it is
  unverified by any gate and the block's "226 rows vs 226 files, exit 0" reading is a *printed*
  number, not an enforced invariant.

---

## Reproduction environment

Read-only attack seat. All bytes read from the landed commit, never the lane working tree.

```
git clone -q --shared /home/vgpnk/Projects/shokunin/kotodama-shokunin /tmp/r50rv/clone
git -C /tmp/r50rv/clone checkout -q 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0
git -C /tmp/r50rv/clone rev-parse HEAD   → 1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0
```

No tool was installed: `python3` from the host interpreter was sufficient for every command
below, so no pacman/uv/npm transaction was made (tooling directive: prefer no installs).

## The landed diff (landed bytes only)

```
$ git -C <lane> diff 4ad2683 1c779e4 -- corpus/README.md
 corpus/README.md | 20 ++++++++++++++++----
 1 file changed, 16 insertions(+), 4 deletions(-)
```

Four hunks: (1) new `revision: 2.7` block at lines 3–12; (2) `## culture-material/ (27)` → `(28)`
(line 277); (3) new row for `pastoralism-animal-husbandry.md` (line 297); (4) totals line
225 → 226 (line 590), `Counts checked` date 2026-10-19 → 2026-10-21 (line 592), footer vector
`(total 225 files; directory totals 25/26/27/29/24/94)` → `(total 226 files; directory totals
25/26/28/29/24/94)` (line 594). No other README bytes changed.

---

## 1. Row placement — HOLDS (manually; not gate-enforced → see S2)

`corpus/README.md:277` header `## culture-material/ (28)`; row at `corpus/README.md:297`.

```
$ awk '/^## culture-material\/ \(/{f=1;next} /^## /{f=0} f&&/^- `/{print}' corpus/README.md \
    | sed 's/^- `\([^`]*\)`.*/\1/' > cm.txt
$ wc -l < cm.txt                              → 28
$ diff cm.txt <(sort cm.txt)                 → (no output)  CM_SECTION_SORTED
$ grep -n 'pastoralism-animal-husbandry\|music-instrument-lexicon\|ritual-garments' cm.txt
18:music-instrument-lexicon.md
19:pastoralism-animal-husbandry.md
20:ritual-garments.md
```

The claim at `corpus/README.md:5` ("its row added in filename order between
`music-instrument-lexicon.md` and `ritual-garments.md`") is **true**, and the whole
`culture-material/` section is in filename order (28/28 sorted, C locale and default locale).

## 2. Topic byte-equality — HOLDS

Independent byte comparison (not the sweep's own comparison):

```
$ python3 - <<'PY'   # entry '- topic:' text vs README row text after the "— "
entry topic bytes: 546 sha dbc90c9e64eace8a
readme row bytes: 546 sha dbc90c9e64eace8a
EQUAL: True
PY
```

`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:3` (`- topic:`) and
`corpus/README.md:297` (row body) are byte-identical, 546 bytes, same SHA-256 prefix. The sweep
independently reports `topic_mismatch 0 []`.

## 3. Counts 28/226 and the footer vector — HOLD

```
$ ls corpus/knowledge/culture-material/*.md | wc -l        → 28     (header says 28, line 277)
$ find corpus/knowledge -name '*.md' | wc -l                → 226    (totals line 590 says 226)
$ python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge
  "totals": { "files": 226, … }
```

Footer vector order is the README's own section order
(`linguistics 25, myth-symbol 26, culture-material 28, synthesis 29, verification 24,
civilizations 94`) = `25/26/28/29/24/94`, which is what `corpus/README.md:594` now reads and what
the sweep's `footer_live.order` confirms. Base commit re-measured for the delta:
`find corpus/knowledge -name '*.md' | wc -l` → 225, `ls corpus/knowledge/culture-material/*.md | wc -l`
→ 27 — so 27 → 28 and 225 → 226 are the true deltas.

## 4. The three gates — GREEN at the pin (in the clone)

```
$ python3 reports/round-28/readme/sweep.py
rows 226 files 226
missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []   header_drift {}
totals_line 226 totals_ok True
footer {date 2026-10-21, total 226, dir_totals [25,26,28,29,24,94]}   footer_findings [] footer_ok True
readme_sha256 3ea247db6ae3719f1391a45072f3169b756a5e756d8cec609efa46ffa675d78c
exit=0

$ python3 tools/check-readme-heading.py
h1_lines [1]   headings {"1": 1, "2": 7}   findings 0    exit=0

$ python3 tools/check-readme-revisions.py
revision_lines [3, 14, 35, 47, 59, 69, 78, 87, 114, 134, 146, 166, 192, 202]
labels ["2.7","2.6","2.5","2.4","2.3","2.2","2.1","2.0","1.8","1.7","1.6","1.5","1.4","1.3"]
findings 0
warnings 1
  REVISION-ORPHAN lines=[101, 112] unheaded paragraph inside revisions span
exit=0
```

The one warning is the residual the `revision: 2.7` block explicitly carries
(`corpus/README.md:11-12`: "The routed rev-1.9 `REVISION-ORPHAN` residual is carried, not
repaired."), and it matches `revision: 2.6`'s routing note at `corpus/README.md:30-33`. Honest.

**Gate liveness (mutation controls, run in the private clone, restored after each):**

| mutation | sweep result |
|---|---|
| M0 unmodified | exit 0, rows 226 files 226 |
| M3 row topic rewritten (`liquid` for `living`) | **exit 1**, `topic_mismatch 1 ['culture-material/pastoralism-animal-husbandry.md']` |
| M4 stale footer dir vector (`25/26/27/29/24/94`) | **exit 1**, `footer_findings [{"class":"FOOTER_DIR_TOTALS", declared [25,26,27,29,24,94], live [25,26,28,29,24,94]}]` |
| M1 **duplicate the pastoralism row** | **exit 0** ← blind spot (S2) |
| M2 **move the row out of filename order** | **exit 0** ← blind spot (S2) |
| M5 footer date drift only (2026-10-21 → 2026-10-19) | exit 0 (nit, see S3) |

So the topic leg and the footer leg are live; the *row-set* and *ordering* legs are not.

## 5. The gap-sweep claims in the revision block — HOLD

`corpus/README.md:4-6` claims "before it, 0 filename owners and 0 word-bounded topic owners".
Re-run at the base commit (`4ad2683`), exactly as the entry's `- gap filled:` line specifies:

```
$ git checkout -q 4ad2683 && find corpus/knowledge -iname '*pastoral*' -o -iname '*husband*' -o -iname '*herd*' | wc -l
0
$ grep -rniP '^- topic:.*\b(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/ | wc -l
0
$ grep -rniP '^- topic:.*(pastoral|herd|husbandr|transhuman|livestock)' corpus/knowledge/   # un-bounded
corpus/knowledge/culture-material/writing-media-surface-economy.md:3   ← "sherd", a non-owner
```

Reproduces the block's numbers exactly, including the "sherd" non-owner that the entry discloses.

---

# Findings

## S1 (medium) — `revision: 2.7` overstates where the partial owners are cited

**Where:** `corpus/README.md:5-6` (the revision block) and
`corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:4` (`- gap filled:`).

Block text (`corpus/README.md:5-6`):

> "…before it, 0 filename owners and 0 word-bounded topic owners, **with partial owners cited
> one-way in its §2**), …"

Entry `- gap filled:` enumerates **seven** partial owners as "cited one-way in §2": the agropastoral
row (`agrarian-field-system-lexicon.md:62`), the pastoral vocabulary field
(`semantic-fields-lexicon-building.md:70,:105`), cattle-root money words (`trade-economy-lexicon.md:69`),
dung fuel (`fire-fuel-light.md:37`), wool (`textile-technology.md:27`), draught and pack animals
(`transport-mobility-lexicon.md:95`), and **livestock-as-wealth idiom (`animal-symbolism.md:73,:110`)**.

§2 of the entry is `corpus/knowledge/culture-material/pastoralism-animal-husbandry.md:27-39`
("## 2. One-owner boundary") and its nine table rows are: agrarian, hunting, cuisine, transport,
trade, textile, semantic-fields, fire-fuel, `civilizations/`. **`animal-symbolism.md` is not among
them.** The only citations of it are:

```
$ grep -n 'animal-symbolism' corpus/knowledge/culture-material/pastoralism-animal-husbandry.md
4:  - gap filled: … (the enumeration above)
6:  - In-corpus anchors: … `myth-symbol/animal-symbolism.md:73,:110`; …
8:- couples: … (line 8 holds the couples cell)
145:The herd's signs belong to `animal-symbolism.md:73,:110`; this entry supplies the ledger they rest on.
```

Line 145 sits under `## 10. Ritual, myth and symbol of the herd` (heading at line 133), i.e. §10,
not §2.

**Why it matters:** the *substance* survives — every partial owner is cited one-way (the older
entries cannot cite back a file written after them), and all nine cited anchors resolve at the
base commit to the claimed content (checked: `agrarian-field-system-lexicon.md:62` = the agropastoral
row; `semantic-fields-lexicon-building.md:70` = "Pastoral wealth vocabulary …"; `:105` = "steppe
pastoral"; `trade-economy-lexicon.md:69` = *pecus* 'cattle' / "Nuer cattle as the idiom of all
value"; `fire-fuel-light.md:37` = "Dried dung | the herds' output"; `textile-technology.md:27` = "Wool
technology is the fork that matters"; `transport-mobility-lexicon.md:95` = the Draft row;
`animal-symbolism.md:73` = "Nuer 'cattle of money'"; `:110` = "Faunal economy writes the idiom").
What fails is the *locator* the README block publishes.

**Smallest fix (either, one line):**
* add a row to §2 — `` | `animal-symbolism.md:73,:110` | livestock-as-wealth idiom | herd facts the idiom verbalises | `` — **or**
* reword `corpus/README.md:6` to "…with partial owners cited one-way (§2, and the herd-sign owner
  in §10)" and the matching clause of the entry's `- gap filled:` line to match.

Author-lane advice only; no edit made by this reviewer.

## S2 (medium) — "row in filename order" and row-set uniqueness are asserted, never measured

**Where:** the acceptance criterion lives in `reports/round-50/claims.json` (claim **C**,
`after_required`: "…README index row in filename order; sweep green.") and is echoed by
`corpus/README.md:5` ("its row added in filename order …") and
`corpus/README.md:13` ("Re-measured with `python3 reports/round-28/readme/sweep.py`: 226 rows vs 226
files, exit 0").

**Evidence that nothing measures it:**

1. `reports/round-28/readme/sweep.py:131` computes duplicates into `dup` and stores them at
   `:155` as `parts[part]["duplicate_rows"]`, but the `ok` predicate at `:191-196` is
   `not (missing or ghosts or mismatches or drift or footer_findings) and totals_line == total_files`
   — `dup` is **never** in it, and `total_rows == total_files` is never compared either (the
   *selftest* does compare them, at `:288`, but only on the live tree — the fixture controls at
   `:343` assert duplicates are "reported", never that they fail).
2. `sweep.py` never compares a section's row list to `sorted(...)` — ordering is not a concept in
   the instrument.
3. `tools/check-readme-heading.py` counts `#`/`##` lines only; it sees rows not at all.
4. `tools/check-readme-revisions.py` reads the revision block only.
5. `reports/round-50/run-validation.py:94-109` (the round-50 measurement runner) expects
   `sweep_rc 0`, `sweep_rows 226`, `sweep_files 226`, `sweep_topic_mismatch 0` — **no** ordering
   expectation and no duplicate expectation.

**Mutation evidence (private clone, restored after each run):** see the M1/M2 rows of the table in
§4 above — duplicating the `pastoralism-animal-husbandry.md` row yields `rows 227 files 226`
with **exit 0**, and moving it out of filename order yields **exit 0**. A reader who only looks at
`exit=0` would accept a broken index; the block's "226 rows vs 226 files" is a printed line
(`sweep.py:222` `f"rows {inv['total_rows']} files {inv['total_files']}"`), not an enforced invariant.

**Why it matters:** the placement property is the one README claim in this round that *no*
instrument can regress, and the round-28 sweep's own selftest asserts only that duplicates are
*reported* (`reports/round-28/readme/sweep.py:337-343`, "control: duplicate row reported"), never
that they *fail*. A future round that adds a row in the wrong position, or adds it twice, lands
green.

**Smallest fix (author lane, two options, both local to `reports/round-28/readme/sweep.py`):**
* add `and total_rows == total_files` and `and not any(p["duplicate_rows"] for p in parts.values())`
  to the `ok` predicate at `sweep.py:191-196`; **or**
* add a per-section ordering leg — `if [f for f, _ in sec["rows"]] != sorted(f for f, _ in sec["rows"]):
  drift[f"{part}:order"] = …` — and keep it inside `drift`, which is already inside `ok`.

Either restores the ability of the instrument to catch exactly the defect class this round's
revision block claims.

## S3 (nit) — the footer's date moved but no block sentence and no gate records it

`corpus/README.md:592` changed `Counts checked 2026-10-19` → `2026-10-21` in the same commit, and
the `revision: 2.7` block mentions only the footer's *vector* move, never its date. The sweep's
footer leg compares `total` and `dir_totals` only (`sweep.py:165-186`); the date is parsed
(`FOOTER_RE` group 1) and reported but never checked — mutation M5 (date drift alone) exits 0.
Not a false claim (the block does not assert the date), and rev 2.5/2.6 are equally silent about
their date moves, so this is a convention-level nit, not a defect in this round's change.

---

## What the change gets right (verified, not inferred)

* Row placement (S2 caveat notwithstanding): `corpus/README.md:297` sits between
  `music-instrument-lexicon.md` and `ritual-garments.md`; the whole section is filename-sorted.
* Topic byte-equality: 546 bytes, identical SHA-256 (`dbc90c9e64eace8a…`), independent of the sweep.
* `corpus/README.md:277` `(28)` = 28 files; `:590` `226` = 226 files; `:594` vector = live counts in
  the README's section order.
* The `revision: 2.7` block's gap-sweep numbers (0 filename owners, 0 word-bounded topic owners,
  "sherd" non-owner) reproduce exactly at base `4ad2683`.
* The block's residual disclosure ("the routed rev-1.9 `REVISION-ORPHAN` residual is carried, not
  repaired") matches `tools/check-readme-revisions.py`'s actual warning (`lines=[101, 112]`) and the
  routing note in `revision: 2.6` (`corpus/README.md:30-33`).
* The three named gates are green at the pin, and the two legs this change leans on (topic equality,
  footer vector) are proven live by mutation (M3, M4 → exit 1).
* The landed commit adds exactly one corpus entry (199 lines) plus the README/QUALITY/SOURCES/lesson
  changes — the "one culture-material entry landed" claim in the block is exact.

## Residual risk / verification gaps (mine)

* I did not re-verify S048–S069 URLs, the §3–§15 body of the entry, or `corpus/QUALITY.md` /
  `corpus/SOURCES.md` — other falsify seats own those. My §1 anchor spot-check only proves the
  nine cited anchors *resolve to the claimed content*, not that the whole entry is sound.
* `reports/round-50/validation.json` (named in the assignment as the receipt) **does not exist** at
  the landed commit; the round-50 measurement runner is `reports/round-50/run-validation.py` and its
  output is not committed. I did not run it (it exercises the O/Ca legs — `receipt_guard`,
  `check-readme-revisions --selftest` — and the jj-colocation probe, which are other seats'). The
  README numbers I report are from independent re-measurement, so this does not weaken §1–§4.
* The duplicate-row and out-of-order mutations were run in the private clone only; the lane working
  tree and the lane git/jj state were never touched (no `git add/commit/stash/checkout/reset`, no
  mutating `jj` command in the lane repo). Temp clone removed after the run.

## Smallest fixes, collected

1. **S1** — `corpus/README.md:6` (+ entry `:4`): either add `animal-symbolism.md:73,:110` to the §2
   boundary table (`…/pastoralism-animal-husbandry.md:29-39`) or reword "in its §2" → "in §2 and
   §10".
2. **S2** — `reports/round-28/readme/sweep.py:188-196`: put `total_rows == total_files` and
   per-part `duplicate_rows` into the `ok` predicate, and/or add a per-section ordering leg inside
   `drift`.

## Tooling record

No installs. Every command ran on the host `python3` (`python3` from PATH; no virtualenv, no new
package). Reason: the three gates, the inventory and all mutations are plain stdlib Python, so the
"prefer no installs" branch of the tooling directive applied. Nothing was installed, upgraded or
downgraded on this host during this seat.
