# C07 — claim-C scribe: integration-ready assembly

- seat: `C07` | claim `C` (coverage) | round 43 | baseline `7ceff59`
- scribed: 2026-10-19, at lane HEAD `7ceff59` (`git rev-parse --short HEAD` → `7ceff59`; `git status --porcelain` → only `?? reports/round-43/`)
- out path: `reports/round-43/cov/C07-scribe.md`
- assembly status at scribe time: **sibling seat artifacts C01–C06 are absent** — `reports/round-43/cov/` was empty when this seat ran (`ls -la` → only `.` and `..`). Every leg below is therefore **independently re-derived by this seat**, with commands and outputs shown. When the sibling files land, reconcile their citations against §3 rather than treating this file as a copy of them.

---

## 0. Verdict (read this first)

**The claim-C landing cannot be admitted as declared.** The declared premise is false on the live tree, and applying the spare as a new myth-symbol entry would put two entries in the partition owning the same register.

Three independent pieces of evidence, all measured:

1. **The file exists.** `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` is present at HEAD and is the lithic-register entry (H1: "Stone, gem and metal symbolism — the lithic register: the lapidary code, material prestige, and the quarry-to-regalia chain", `:1`).
2. **It is the r42 C04 landing, byte-exact.** The live file's sha256 is `c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f`; the fenced body of `reports/round-42/cov/C04-entry-4.md` hashes to the same digest (comparison command in §4.2).
3. **The r42 record itself says the two drafts are the same topic.** `reports/round-42/validation.json:22`: "C01 and C04 authored the same lithic register mid-wave; C04 lands, C01 routes as the named spare". The spare's own first line repeats it: "C01 and C04 authored the same lithic topic mid-wave … THIS draft is routed as the named spare for a future re-scoped claim" (`reports/round-42/cov/C01-mineral-spare.md:1`).

The round-43 claim's `before` string says: "myth-symbol 26 (lithic slot named but unbuilt since r42's C01/C04 collision routed this draft to spare); total 223" (`reports/round-43/claims.json:40`). The counts are right (26 and 223, measured §1); **"unbuilt" is wrong** — the slot was built by C04 and the spare is its duplicate.

**Recommendation:** do **not** apply the corpus landing; record claim C as **blocked-by-topic-collision** with owner `integrator` (next touch after an operator re-scope or retire decision — §7). The mechanical edits are supplied in §6 *only* so the parent can see the shape; they are marked **NOT FOR APPLICATION** while the collision stands. The round's own shared rule is binding: "before proposing any corpus landing path, verify it against the live partition … never overwrite an existing entry; report collisions, do not route around them" (`reports/round-43/targets.json:9`).

---

## 1. Measured baseline at scribe time

Commands run from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`:

```
$ ls corpus/knowledge/myth-symbol/*.md | wc -l
26
$ find corpus/knowledge -name '*.md' | wc -l
223
$ python3 -B reports/round-28/readme/sweep.py
parts {"civilizations": 94, "culture-material": 25, "linguistics": 25, "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 223 files 223
missing_from_index 0 []
topic_mismatch 0 []
orphan_rows 0 []
header_drift {}
totals_line 223 totals_ok True
footer {"date": "2026-10-19", "command": "python3 tools/source-audit-inventory.py --json --summary --root corpus/knowledge", "total": 223, "dir_totals": [25, 26, 25, 29, 24, 94]}
footer_findings [] footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
EXIT=0
```

The index is currently **green and internally consistent at 223**. This matters for the delta receipt: a post-landing 224==224 would also be green (simulated §3.5), so the sweep is **not** a collision detector. It checks row↔file correspondence and topic equality (`reports/round-28/readme/sweep.py:74-84`, `:136-146`), not whether two entries own the same topic.

---

## 2. Assembly map (mission items → evidence below)

| Mission item | Sibling seat | Evidence re-derived here |
|---|---|---|
| Prepare the spare, contract, target path | C01 | §3.1, §3.4 |
| README rev 2.5 exact edits | C02 | §3.2, §6 |
| Source audit (paths/lines real) | C03 | §3.3 |
| Contract audit vs QUALITY.md | C04 | §3.4 |
| Delta receipt / sweep prediction | C05 | §3.5 |
| Collision verification / partition listing | C06 | §3.6, §4 |
| Integration summary | **C07 (this file)** | §0, §5, §7 |

---

## 3. Evidence per leg

### 3.1 Prepare — spare integrity and contract completeness

- Fingerprint: `sha256sum reports/round-42/cov/C01-mineral-spare.md` → `2b9326e351de0e324bce3e71d45390c4a03e838138902ffcf23a971704ef6156`; `wc -lc` → **219 lines, 55433 bytes**.
- Fences: opening ` ```markdown ` at line 3; closing ` ``` ` at line 219; fenced body = **lines 4–218**.
- The spare's header sanctions no path/front-matter edits: its only pre-fence text is the integrator ruling at `:1`; the fenced body ends with no insertion instructions. So "apply the spare's fenced bytes unmodified" would mean creating a second full lithic entry, not adjusting the existing one.
- Head-block contract, all present in the spare: `- topic:` `:6`, `- gap filled:` `:7`, `- sources:` `:8` (through `:20`), `- calibration:` `:21`, `- couples:` `:22`, `- source:` `:23`, `- verified-at:` `:24`, `- recheck:` `:25`, `- scope:` `:26`.
- Target filename: the spare **does not name one**. Under the partition's kebab-case descriptive convention, the natural candidates are free or occupied as follows (measured with `test -e`):

| candidate | status at HEAD |
|---|---|
| `mineral-stone-symbolism.md` | **occupied** (r42 C04 landing) |
| `stone-gem-metal-lithic-register.md` | free |
| `lithic-register.md` | free |
| `lapidary.md` | free |
| `stone-symbolism.md` | free |

A free *filename* does not make the landing safe: the collision is **topical**, and the spare's own H1/topic claim the same register the occupied file owns.

### 3.2 README rev 2.5 — exact edit surface (conditional)

Current anchors in `corpus/README.md`:

- revision 2.4 block begins `:5`
- `## myth-symbol/ (26)` at `:205`
- row order: `hero-journey-variants.md` `:218`, `mineral-stone-symbolism.md` `:219`, … `sacred-topography-pilgrimage.md` `:229`, `symbolism-synthesis-method.md` `:230`
- `Total knowledge entries: 223.` at `:544`
- footer block `:546-548`: date line, command line, `(total 223 files; directory totals 25/26/25/29/24/94).`

For a file named `stone-gem-metal-lithic-register.md`, the row sorts **after `sacred-topography-pilgrimage.md` (`:229`) and before `symbolism-synthesis-method.md` (`:230`)**. For `lithic-register.md` it sorts after `hero-journey-variants.md` (`:218`) and before `mineral-stone-symbolism.md` (`:219`). The row's trailing text must be byte-equal to the entry's own `- topic:` text, continuations space-joined — that is exactly what the sweep compares (`reports/round-28/readme/sweep.py:74-84`, `:136-146`). The spare's topic is one physical line of **1337 characters**, beginning "the **lithic register** a fictional culture's symbolic grammar runs on stone, gem and metal — …".

### 3.3 Source audit — in-repo citations

Command: extract every `corpus/knowledge/*.md[:line]` reference from the spare, resolve the path, and bounds-check the highest cited line against the file's line count.

```
unique path refs: 45
paths resolve: 45 | missing: 0
line-anchor out of range: 0
```

Ten load-bearing anchors were then opened and their quoted content checked against the cited line (all 10 matched the spare's use):

| citation | observed content (truncated) |
|---|---|
| `myth-symbol/symbolism-synthesis-method.md:23` | "the five canonical registers: **color, …" |
| `myth-symbol/symbolism-synthesis-method.md:29` | "**The medieval Latin package**: bestiary + lapidary + numerology + heraldic code" |
| `myth-symbol/plant-symbolism.md:15` | "**Stationary** — a plant cannot flee, so it can be owned, inherited, fenced, taxed…" |
| `culture-material/ritual-garments.md:59` | "choshen … 12 gemstones, one per tribe … the 12 stones as the zodiac (Philo; Josephu…" |
| `civilizations/maya-classic.md:10` | Taube 2005, DOI `10.1017/S0956536105050017` |
| `civilizations/maya-classic.md:127` | "Jade ↔ maize, centrality, rulership, breath … Not every jade object expresses all associations…" |
| `civilizations/maori.md:20` | "recheck: … named pounamu histories …" |
| `civilizations/siam-thai.md:126` | "The Emerald Buddha functions as a dynastic palladium in Reynolds's analysis…" |
| `civilizations/china-shang-zhou.md:106` | "an old object in a later burial does not…" |
| `culture-material/funerary-material-culture.md:22` | "Pliny … *Naturalis Historia* 36.27 (the *sarcophagus* stone of Assos…" |

No fabricated in-repo source was found. External sources (Pliny book 37, Marbod, Philippe de Thaon, Taube, etc.) are explicitly flagged `(to-verify)` / "not consulted this round" in the spare (`:21`, `:24`); this seat has no network and did not fetch them, so their bibliographic status stays as filed.

**Staleness finding inside the spare's own gap line:** its absence sweep is dated "2026-10-19 at lane HEAD `ac47c78` … (220 files)" (`:7`). That measurement predates the r42 landing that added `mineral-stone-symbolism.md`; its conclusion "**no entry owns stone**" is now false. This is not an arithmetic error in the spare — it was true when drafted — but it is the exact sentence that collides with the live partition.

### 3.4 Contract audit vs `corpus/QUALITY.md`

The spare satisfies the five admission clauses on its own text:

| QUALITY clause | spare evidence | verdict |
|---|---|---|
| 1 Provenance — cited/checkable sources, `(to-verify)` not laundered | `- sources:` `:8-20`, `- source:` `:23`, `(to-verify)` flags `:21`,`:24` | PASS (within offline limits) |
| 2 Calibration — status named | `- calibration:` `:21`, §11 calibration bank | PASS |
| 3 Coupling — `- couples:` names connected files | `:22` | PASS |
| 4 Usability — tables/checklists/worked example | §2–§10 tables, §9 build order, §12 worked micro-example | PASS |
| 5 Canon hygiene — decides nothing | `:26` scope, §13 handoff to lore-shokunin | PASS |

**Partition-level contract: FAIL.** A second entry whose topic is the same register violates the one-topic-owner discipline the partition has enforced (and which the r42 collision ruling applied). QUALITY.md does not spell out topic uniqueness; the r42 ruling and the `symbolism-synthesis-method.md` "one symbol, one primary domain" rule (`:23` area) are the operative authorities. This is why a 5/5 clause audit is not sufficient for admission.

### 3.5 Delta receipt — predicted post-landing sweep (simulation, not a landing)

To test the mechanical edit shape without touching the repo, this seat copied `corpus/knowledge` into `.scratch/r43-c07-sim/`, wrote the spare's fenced body as `myth-symbol/stone-gem-metal-lithic-register.md`, applied the four README edits in memory, and called the real sweep function with `root_override` pointing at the copy. The scratch tree was removed afterwards.

```
parts: {"civilizations": {"declared": 94, "rows": 94, "files": 94, "duplicate_rows": []},
        "culture-material": {"declared": 25, "rows": 25, "files": 25, "duplicate_rows": []},
        "linguistics": {"declared": 25, "rows": 25, "files": 25, "duplicate_rows": []},
        "myth-symbol": {"declared": 27, "rows": 27, "files": 27, "duplicate_rows": []},
        "synthesis": {"declared": 29, "rows": 29, "files": 29, "duplicate_rows": []},
        "verification": {"declared": 24, "rows": 24, "files": 24, "duplicate_rows": []}}
total_rows 224 | total_files 224
missing_from_index [] | orphan_rows [] | topic_mismatch [] | header_drift {}
totals_line 224 totals_ok True
footer_ok True | footer_findings []
simulated readme_sha256 1c165a99c27d059844c7a870a051857eae93496dc1af0415861561b32844be04
ok True
```

**Interpretation:** the mechanical delta is exactly as the claim predicts — myth-symbol 27, total 224, footer `25/27/25/29/24/94`, sweep exit 0. The simulated README sha is **not** a delivery prediction: the real integrator's README bytes and the entry filename may differ. Per the readme-prediction-vs-delivery practice, the delivery receipt must be the post-apply `python3 -B reports/round-28/readme/sweep.py` output plus the staged-tree sha, not this simulation digest.

**The important negative result:** the sweep reports `ok True` even though the added entry duplicates an existing topic. There is no duplicate-topic leg. A future operability round may want one; this seat flags it as a durable instrument gap with owner `operability`, not fixed here (no instrument changes in a scribe seat).

### 3.6 Collision verification — the partition as it actually is

`ls corpus/knowledge/myth-symbol/` at HEAD `7ceff59` (26 entries):

```
animal-symbolism.md
binding-speech-complex.md
celestial-symbolism-calendars.md
color-symbolism.md
comparative-frameworks.md
cosmology-cosmography.md
creation-myths-taxonomy.md
death-afterlife-eschatology.md
direction-symbolism.md
divination-omen-systems.md
eschatology-world-end-systems.md
flood-traditions.md
hero-journey-variants.md
mineral-stone-symbolism.md      <-- the lithic register, already owned
motif-index-usage.md
myth-folktale-genres.md
myth-ritual-theories.md
number-symbolism.md
pantheon-archetypes.md
plant-symbolism.md
purity-pollution-boundary-systems.md
ritual-liminality.md
sacred-kingship-mythic-charter.md
sacred-topography-pilgrimage.md
symbolism-synthesis-method.md
trickster.md
```

Provenance of the occupied file: `git log --oneline --follow -- corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` → single commit `7ceff59 round-42: NOT ADMITTED on C (O verified) — N6 successor extractor, 3 myth-symbol entries, collision ruling + overwrite restore`. The r42 C failure record is explicit: "myth-symbol 26 != 27, total 223 != 224 (three entries landed, the fourth collided and is routed)" (`reports/round-42/validation.json`).

---

## 4. Collision analysis (the load-bearing finding)

### 4.1 The two entries claim the same slot in their own words

- Spare `- gap filled:` (`reports/round-42/cov/C01-mineral-spare.md:7`): "the partition's register family is **closed at five plus flora and the lithic slot is named but never built** … while **no entry owns stone**."
- Spare `- topic:` (`:6`): "the **lithic register** a fictional culture's symbolic grammar runs on stone, gem and metal …"
- Live entry `- gap filled:` (`corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:3`): "the lithic/mineral register is absent from the partition and this entry fills it … while no entry owns stone."
- Live entry `- topic:` (`:5`): "the lithic register of a fictional culture's symbolic grammar — the mineral slot the register family lacks …"

Read side by side, the spare's central "no entry owns stone" assertion is contradicted by the file that landed one round earlier. Filing both would make the index itself carry two entries each claiming to be the missing lithic register.

### 4.2 Measured overlap

- sha256: live file `c99f44ca79a7c50306259c1c9038cefd92787d9a5e0dd66910f46dda95adb99f`; fenced body of `reports/round-42/cov/C04-entry-4.md` = same digest (extraction + comparison performed by this seat; both lengths 61343 bytes).
- In-repo reference sets: spare 34 unique paths, live entry 40 unique paths, **28 shared**, Jaccard **0.609**.
- Section structures: both have 13 H2 sections; the organizations differ (spare: five sign-properties / eight material classes / four mechanisms / scarcity ladder / lapidary institution / heirloom rule; live: five jobs / six properties / lapidary code / value language / axis-boundary / instrument / era drift), but both are full treatments of the same register. Different organization is not a different topic.
- Shared exemplar spine: both cite the choshen (`ritual-garments.md:59`), Taube's jade (`maya-classic.md:10,127`), pounamu/maori (`maori.md:13,14,20`), the Emerald Buddha (`siam-thai.md:126`), Fu Hao's jades (`china-shang-zhou.md:106`), and Pliny's *sarcophagus* (`funerary-material-culture.md:22`).

### 4.3 Why the r36 precedent does not authorise this landing

The r42 ruling routes the spare "per the r36 timekeeping precedent". In r36 the routed spare was `culture-material/timekeeping-instruments.md` — a topic **no existing entry owned** — and r36's claim was "Land the routed timekeeping spare" (`reports/round-36/claims.json`, C). The precedent's operative condition is *topic-free spare*; here the topic is occupied. The precedent therefore argues **against** landing as declared, and the spare's own header says "a future **re-scoped** claim" (`:1`) — not "the same claim retried".

---

## 5. Consequences for the round

- **Claim C cannot meet `after_required`** ("myth-symbol 27, total 224 … no existing entry overwritten") in substance: the counts could be reached, but the partition would contain two lithic-register owners, and the new entry's `- gap filled:`/`- topic:` would assert a gap that the live entry already fills.
- **README rev 2.5 must not be filed with a duplicate row.** The revision text in §6 would mechanically satisfy the sweep while documenting a duplicate.
- **O and Ca are unaffected**, but if a landing ever occurs, the O resolver's census will read the new entry's `- couples:` line (34 refs in the spare), so the census baseline would shift. Flagged for the O scribe, not decided here.
- **No corpus byte was staged by this seat.** `git status --porcelain` shows only `?? reports/round-43/`; `corpus/` is untouched.

---

## 6. Conditional mechanical draft — **NOT FOR APPLICATION**

Supplied only to complete the C02 leg and to show the parent the exact surface. **Do not apply while the topic collision stands**; applying it would violate `reports/round-43/targets.json:9` and the r42 ruling. Filename shown as the simulation name `stone-gem-metal-lithic-register.md`; the spare does not sanction any filename.

```diff
--- a/corpus/README.md
+++ b/corpus/README.md
@@
-revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
+revision: 2.5 — Round-43 myth-symbol expansion (2026-10-19): one myth-symbol
+entry landed (`stone-gem-metal-lithic-register.md`); `## myth-symbol/` moved
+26 → **27**; the totals and footer moved 223 → **224** and the vector
+25/26/25/29/24/94 → **25/27/25/29/24/94**. Re-measured with
+`python3 reports/round-28/readme/sweep.py`: 224 rows vs 224 files, exit 0.
+
+revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): three
@@
-## myth-symbol/ (26)
+## myth-symbol/ (27)
@@
 - `sacred-topography-pilgrimage.md` — the place register …
+- `stone-gem-metal-lithic-register.md` — the **lithic register** a fictional culture's symbolic grammar runs on stone, gem and metal — … [the spare's `- topic:` text byte-for-byte, 1337 chars]
 - `symbolism-synthesis-method.md` — the core generation method …
@@
-Total knowledge entries: 223.
+Total knowledge entries: 224.
@@
-(total 223 files; directory totals 25/26/25/29/24/94).
+(total 224 files; directory totals 25/27/25/29/24/94).
```

With a `lithic-register.md` filename, the row insertion point moves to between `hero-journey-variants.md` (`:218`) and `mineral-stone-symbolism.md` (`:219`); everything else is unchanged. The row's topic text must be `topic_of(spare)`, which is the one-line `- topic:` at `reports/round-42/cov/C01-mineral-spare.md:6` (1337 chars).

---

## 7. Escalation — decision required from the integrating parent

| option | what it means | evidence consequence | owner |
|---|---|---|---|
| **A. Block, re-scope (recommended)** | Do not land this round. Record claim C `blocked-by-topic-collision`; require a successor draft on a genuinely unowned sub-topic before any landing. | Spare stays filed and cited; count stays 26/223; the r42 C failure remains resolved-as-spare, not silently retried. | integrator + operator; next_touch r44 |
| **B. Retire the spare** | Record the spare as superseded by `mineral-stone-symbolism.md`; no corpus move. | Honest closure; loses the spare's alternative organization, which differs but does not add an unowned topic. | integrator |
| **C. Override and land a duplicate** | Apply §6 anyway with a distinct filename. | Sweep goes green 224==224, but the partition carries two lithic owners and the new entry's gap claim is false; a future audit should reject it. Requires explicit operator instruction, not a scribe decision. | operator |

This seat takes **no** corpus action and does **not** route around the collision. If the parent chooses A or B, nothing further is needed from C07; if C, §6 is the exact surface but the admission is an explicit override.

---

## 8. Reproducibility index (commands run by this seat)

```
git rev-parse --short HEAD
git status --porcelain
ls corpus/knowledge/myth-symbol/
ls corpus/knowledge/myth-symbol/*.md | wc -l
find corpus/knowledge -name '*.md' | wc -l
python3 -B reports/round-28/readme/sweep.py
sha256sum reports/round-42/cov/C01-mineral-spare.md corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
wc -lc reports/round-42/cov/C01-mineral-spare.md
grep -n '^```' reports/round-42/cov/C01-mineral-spare.md
python3 - <<'PY'  # 45-ref path/line resolution audit; 45/45 resolve, 0 OOR
PY
python3 - <<'PY'  # fenced-body vs live-file sha equality (C04-entry-4.md)
PY
python3 - <<'PY'  # scratch simulation: sweep(readme_text, root_override=tmp_knowledge)
PY
grep -n '^## myth-symbol/\|^Total knowledge entries\|^Counts checked' corpus/README.md
git log --oneline --follow -- corpus/knowledge/myth-symbol/mineral-stone-symbolism.md
```

`reports/round-43/run-validation.py` was **not** run: the round's absolute rule forbids in-tree round-runner execution, and no runner exists yet in the round directory at scribe time (`find reports/round-43 -type f` → claims.json, targets.json, telemetry/dispatch-declared.json, plus this file).

---

## 9. Unknowns / to-verify

- **Sibling artifacts absent.** C01–C06 outputs were not present when this seat ran; their conclusions may add evidence but cannot change the measured live file or the r42 ruling. Reconcile at integration.
- **Target filename is unsanctioned.** The spare names none; `stone-gem-metal-lithic-register.md` is this scribe's simulation label, not a C01 decision. Any filename choice remains topically colliding.
- **No external source was fetched** (no network in this seat). The spare's `(to-verify)` literature legs remain `to-verify`, as filed.
- **The `stone-gem-metal` spare's own `- couple:`/`- sources:` claims were audited only for path/line existence and ten spot-checks**, not for scholarly accuracy against held copies. That is a source-audit limitation, not a claim of verification.
- **The occupied entry's authorship history beyond the r42 commit** was not audited; its current bytes are the fact that matters here (sha256 above).
