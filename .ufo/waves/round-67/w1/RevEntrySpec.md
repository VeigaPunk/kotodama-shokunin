# RevEntrySpec — claim-C entry spec + row-fragment review (r67 wave 1)

Seat: RevEntrySpec (reviewer, read-only). Lane: kotodama-shokunin, base `ad5b52b0`.
Reviewed at 2026-10-24 ~09:38Z. Method: read the frozen counter `reports/round-67/accept-c.py`
and executed its own functions (`cells`, `anchor_quote`, `content_words`, `ordered_hits`,
`in_order_coverage`) against the artifacts on disk — the RESTATE verdicts below are the
counter's arithmetic, not my paraphrase. No `lsp` server answers Markdown/Python here, so
semantic claims are proved by executing the frozen instrument, not by grep.

## Artifact state (dependency finding, blocks full review)

| artifact | state |
|---|---|
| `.ufo/waves/round-67/stage/entry-spec.md` | **ABSENT** (`ls .ufo/waves/round-67/stage/` at 09:38 shows `gate-rows.md`, `lesson-draft.md`, `log-r66.md`, `mut-c/`, `mut-entry/`, `mut-o/`, `quality-c19.md`, `readme-row.txt`, `scorecard-r66.md`) |
| `.ufo/waves/round-67/rows/ScoutRow*/row-*.txt` | **2 of 24 present**: `ScoutRow11/row-S825.txt`, `row-S826.txt` (+ `rejects.txt`). `ScoutRow01..12` other than 11 absent; `rows/` otherwise holds only `ScoutGapMed/gap.md` |
| `stage/gate-rows.md` | present but **stale**: 24 claim-id lines, **22 marked MISSING** |
| `stage/readme-row.txt` | present and internally correct (verified below) |

Consequence: the section plan cannot be reviewed; only the two landed fragments can be
graded, and the README/topic interlock can be reviewed only from the README side.

---

## HIGH

### H1 — S826 fails RESTATE as written (2 in-order quote words, floor is 3)
`rows/ScoutRow11/row-S826.txt`, executed through accept-c's functions:

```
quote  "After Chiso brought acupuncture to Japan from Wu (China) in the sixth century"
qw     [after, chiso, brought, acupuncture, japan, china, sixth, century]
bullet "Chiso's sixth-century import seeded Japan's distinct lineages of needle and moxa practice."
bw     [chiso, sixth, century, import, seeded, japan, distinct, lineages, needle, moxa, practice]
ordered_hits(qw,bw) = 2        # chiso, japan
teaches_cov=0.000  q_to_t=0.000  novel=10  teaches_cw=19
=> RESTATE FAIL (inq < 3)
```
Two independent causes, both reusable lessons for the other 22 seats:
1. **Paraphrase loses the token.** `brought` became `import`; `acupuncture` vanished.
   `content_words` is exact-token, no stemming (`NONWORD.sub` + stopword list only).
2. **Reordering loses the match.** The bullet puts `sixth-century` *before* `Japan`;
   `ordered_hits` walks the quote forward through the bullet, so a word already passed is
   dead (`j` never rewinds).
Fix shape (preserves order, keeps teaches coverage low, adds a novel word):
`Chiso brought acupuncture into Japan in the sixth century; later lineages split needle and moxa craft.`
→ inq 6 (`chiso, brought, acupuncture, japan, sixth, century`), novel `later/craft`, run copied < 12 words.

### H2 — 22 of 24 Gate rows are MISSING; cutting the lesson from this draft fails ACCEPT-CA-67
`stage/gate-rows.md`: of the 24 claim ids, only S825/S826 carry a line; S805–S824, S827, S828
are `MISSING (expected …; absent at 12:37Z)`. `accept-ca.py` QUOTES leg:
`gate_ids = set(re.findall(r"\bS(8[0-2]\d)\b", lesson_text)) & {S805..S828}`, `len(gate_ids) >= 20`.
From this draft `gate_ids = 2` → **QUOTES FAIL**. The Gate draft must be regenerated after the
remaining fragments land (it was also already stale for S825/S826: the fragments exist now).

### H3 — Registry placement: the 24 rows must land *inside* `## Registry`, and the frozen C counter cannot see the difference
Measured on the base registry (`corpus/SOURCES.md`, 852 lines, 724 row lines):
`## Registry` header at :26, last registry row `S775` at :731, `## Paths` at :733,
`## Leads (unopened)` at :780, and `S776, S779–S800` sit at :830–:852 **under `## Leads`**
(this is exactly the `E12` census output in `reports/round-67/telemetry/census-start.txt`).
- `accept-c.py` `ROW_RE` scans **every** line, and `SET`/`ROWS`/`ONEID`/`CAPTURE` never check
  section membership → 24 rows appended after the file tail (under `## Leads`) would still
  print `ACCEPT-C-67: PASS`.
- `accept-ca.py` D2 runs `sources-census.sh validate`, which flags `E12 row outside Registry
  section` → 24 new `E12` findings → **ACCEPT-CA-67 FAIL** at lands.
Required integration rule: insert S805–S828 immediately after the `S800` row **once Ca has
moved S776/S779–S800 into `## Registry`** (i.e. before `## Paths`), never at end of file.
Recommended pre-data change (frozen-predicate rule allows revision before data): scope
`SET/ROWS` to the `## Registry` table so C and Ca cannot disagree about what a registry row is.

### H4 — ONEID forbids the entry from citing any pre-existing row id
`accept-c.py`: `foreign = sorted({s for s in cited if s not in NEW_IDS})` → any `(S791)` /
`(S400)` / `(S001)` anywhere in `medicine-healing-codes.md` **fails ONEID** (`out_of_claim_set`).
The editor's natural move for the plague-costume row (S813) is to write “(S791, pomander,
plague-era scent prophylaxis)” — that is an instant FAIL. Boundary/adjacency sentences must
cite **paths**, never base ids. Also: `ENTRY` bullets are collected by `re.search(r"\((S\d{3,})\)", l)`
on *any* line, so a prose sentence citing an id becomes that id's “bullet” and drags prose into
RESTATE; every citation must sit on its own bullet line, one id per line (two ids on one line
leaves the second id with `bullets=0`).

## MEDIUM — duplicate / overlap map for the 24 topics (counter-blind; the L1 must rule)

No claim-C leg tests semantic duplication: `LINK` only compares normalized live URLs. Every
collision below can produce a green counter and a duplicate register. Evidence is line-cited.

| row / topic | owner already in corpus | evidence | verdict |
|---|---|---|---|
| **S828** medical amulets, charms, materia of protection | `myth-symbol/amulets-talismans-apotropaic-marks.md` | topic line :3 owns “amulets, talismans, charms and apotropaic marks … the danger a protective object answers (evil eye, named demons, childbirth and infant death, **plague, illness** …), materials and forms, who makes/blesses/sells it” | **Severe duplicate.** Narrow S828 to medical-materia logic inside a *medical* text/treatise, or expect a duplicate; the entry's “protective dress, amulets and the materia of prophylaxis” bullet (already in `readme-row.txt`'s topic) restates the owner |
| **S825** asklepieia + incubation | `myth-symbol/divination-omen-systems.md` (:126), `myth-symbol/sacred-topography-pilgrimage.md` (:52, :77) | divination :126 “Dream-sanctuary \| Asclepieia; incubation shrines \| … a healing institution with a case archive (the *iamata*)”; topography :52 row “healing / incubation shrine … Asclepieia and the *iamata*”, :77 “The archive is the byproduct … kept votive inscriptions and case records” | **Duplicate content.** The landed `row-S825` teaches cell (“iamata stelae stood in the stoa-abaton … dream incubation … sanctuary”) is the owned claim in other words. Row may stand as a *source*; the entry bullet must claim the **therapy/cure-record** object (iamata as clinical case series, abaton as ward) and point one-way to both paths |
| **S817** medicine lodge / sweat-lodge therapy | `culture-material/bathing-and-body-hygiene.md` (:27, :98) | :27 table row “Sweat-lodge family (Mesoamerican *temazcalli*, North American sweat lodge, Finnish sauna, Russian banya)”; :98 “Some real sweat-lodge and purification traditions are not public property” | **Duplicate + calibration gap.** The bath entry owns the sweat-lodge *regime* and already carries the permission-bound rule; S817 must be the *healing* office (who officiates, what is treated) and must repeat the restriction note |
| **S824** sangoma / nganga | `myth-symbol/divination-omen-systems.md` (:119–:122, :193), `purity-pollution-boundary-systems.md` (:58, :140) | divination §5 specialist slots (“Court diviner … the king's monopoly on asking”), :193 “Do not label every diviner a shaman”; purity :58 miasma/pharmakos, :140 “Discredited — hygienic reductionism” | **Duplicate of the diviner slot**, not of a “myth-symbol healing” file (no such owner exists). Entry must scope to the *therapeutic* role and cite both paths; neither row may re-run the specialist typology |
| **S821** Kampo vs **S826** moxibustion/acupuncture | each other (transmission chain) | landed `row-S826` teaches: “transmission from Wu via Korea in 562, the 701 Ishitsu-rei medical code, Ishinpo, Sugiyama's needle-tube method … household moxibustion” | **Highest-value overlap after S828.** The 6th–8th c. entry of Chinese medicine via Korea, the *Ishitsu-rei* (701) and the *Ishinpo* are the standard Kampo origin story too. If S821 is written as “Japanese reception of Chinese medicine” the two rows teach the same chain. Force disjoint scope cells: S821 = herbal formulary/pharmacy institutions; S826 = needling/moxa technique + blind-practitioner lineage |
| **S826** vs **S807** (assignment's hypothesis) | S807 TCM foundations | — | **Manageable**: classical theory (Huangdi Neijing, qi, meridians) vs Japanese technique transmission. Acceptable only if the two scope cells (≤60 chars) stay disjoint and the entry bullets do not both open on “meridians” |
| S813 / S820 / S827 plague triad + base row S791 | `scent-perfume-aromatics-codes.md` (:3 “status and disease codes”), registry `S791` pomander “plague-era scent prophylaxis” | `S791` row at `corpus/SOURCES.md:843` | Three plague rows out of 24 is defensible (costume / institution / advice literature) but the entry must not re-explain scent prophylaxis — and cannot cite `S791` (H4). State it by path |
| S805 humoral canon vs S812 Galen; S819 Vesalius vs S812 | each other | — | Cluster, not duplicate: keep humoral doctrine in S805 only, Roman/Alexandrian system + anatomy-in-error in S812, the *Fabrica* rupture in S819 |

Checked and **not** duplicated (hypotheses killed by evidence, so nobody spends a seat on them):
- `masks-masquerade.md` contains **no** `plague|physician|beak` match — the plague-doctor mask is not owned there.
- `warrior-material-culture.md` contains **no** `wound|surgery|surgeon` match — battlefield surgery is unowned (S823 is safe).
- `cuisine-food-lexicon.md` owns dietary *law* (kashrut/halal) and the meal grammar, not humoral dietetics — S805's regimen has no owner.

## MEDIUM — RESTATE mechanics the entry spec must state explicitly

Executed thresholds (`accept-c.py` RESTATE block): per id exactly one bullet line;
`ordered_hits(quote_content_words, bullet_content_words) >= 3`; `in_order_coverage(teaches_content_words, bullet) < 0.8`;
`>= 1` bullet word absent from teaches; teaches `>= 4` content words; `q_to_t < 0.8`.
Content word = NFKC-casefold, split on non-word, `len >= 4`, alphabetic, not in the 100-word
stopword list — so **no stemming** (`incubations` ≠ `incubation`, `moxa` ≠ `moxibustion`),
`wu`/`qi`/`li` are too short to count, and hyphenated forms split (`stoa-abaton` → `stoa`,`abaton`).

Calibration that the risk is bullet-craft, not the source archetype: run over all 39 base rows
`S760–S800`, **0** fail the teaches-quality checks (`teaches_thin`, `teaches_echoes_quote`) and
**0** have `<3` quote content words. So museum-label / article rows are fine as rows; the two
failure modes are (a) paraphrase/reorder in the bullet (H1), (b) a title-shaped anchor.

Title anchors that are **unfixable** (measured with the counter's own `content_words`):
`The Canon of Medicine` → `[canon, medicine]` = 2 (S808); `On the Nature of Man` → `[nature]` = 1 (S805);
`The Four Tantras` → `[four, tantras]` = 2 (S816). `De humani corporis fabrica` → 3 exactly
(`humani, corporis, fabrica`, S819) and passes only if the bullet keeps those three tokens in order.
Seats must quote body prose, never a work title.

## LOW / defects found in artifacts that do exist

- **L1 — `rows/ScoutGapMed/gap.md` off-by-one.** “Culture-material has 34 files” — measured
  **33** at base and 33 live (`git ls-tree -r --name-only <base> -- corpus/knowledge/culture-material | grep -c '\.md$'`
  → 33; `find corpus/knowledge/culture-material -name '*.md' | wc -l` → 33). The 34 is the
  *post-landing* README count; as written it reads as a base-state assertion.
- **L2 — gap.md's registry-boundary block under-describes the base.** It says “S793–S800
  (base ends at S800)”, true, but omits that `S776` and `S779–S800` sit under `## Leads`
  (`:830–:852`) and that **`S777`/`S778` do not exist at all** (grep finds no such rows).
  A reader following that block could append the new rows at the file tail (see H3).
- **L3 — both landed anchors are abstract quotes.** `row-S825` VERIFY: “quote in body text: Y
  (English abstract section; article body in Italian)”; `row-S826` VERIFY: “quote in body text:
  Y (abstract)”. Not a counter failure (nothing in accept-c reads the body), but `ScoutRow11`'s
  own `rejects.txt` rejects the JJSAM source for precisely “an English-bodied anchor quote …
  could not be confirmed via the English abstract alone”. Either the abstract is admissible or
  it is not — the wave needs one rule before 22 more rows adopt the same pattern.
- **L4 — fragment→registry fidelity.** Both fragments are single-line `ROW=` with exactly
  **11 cells**, `used-by` = the entry path, scope 52/58 chars, quote 16/13 words — shape is
  correct. Copy cells byte-for-byte when landing: `anchor_quote` takes the **first** quoted span
  in cell 6, so reformatting the anchor (or letting a second quoted span precede it) silently
  changes the RESTATE anchor; any added `|` makes `cells() != 11` and fails ROWS.
- **L5 — README side is correct (verified, no action).** `stage/readme-row.txt` row is one
  physical line, 774 chars, ends “…universal history of medical practice.”, uses the
  backticked basename, and sits between `material-culture-inference-method.md` (:403) and
  `music-instrument-lexicon.md` (:404). `## culture-material/ (33)` is :381, `Total knowledge
  entries: 240.` is :703, footer `(total 240 files; directory totals 30/29/33/29/24/95)` is
  :707 — live counts match exactly (30/29/33/29/24/95). Its blocking interlock stands: the
  entry's `- topic:` text must be byte-identical to this row's topic string (sweep compares
  with **equality**; accept-c TOPIC is substring-only and is the weaker check). Since
  `entry-spec.md` is absent, the topic string exists in exactly one place today — derive the
  entry head block **from** `readme-row.txt`, never the reverse.

## Residual risk / verification gaps

1. 22 of 24 fragments and the entire `stage/entry-spec.md` are absent from this snapshot;
   H1 is proved for S826 and S825 only, and neither the section plan nor the `≤16 H2 / 0 H3 /
   ≤250 lines` leg can be pre-checked. Rows S805–S824/S827/S828 remain ungraded.
2. No fragment→registry round trip exists yet; H3/H4 and L4 land at integration and are
   currently unproven by any seat.
3. I did not re-fetch any URL (desk review by design; `RevSourceSupport1–4` own fetch+capture).
   HOSTS ≥10 and LINK uniqueness therefore remain unmeasured for the real 24.
4. Duplicate verdicts in the table are register-level readings of topic lines and body claims;
   the L1 decides whether a row is re-scoped or replaced. No counter will record that decision.

## Addendum — cross-counter check: C-APPEND vs Ca-D4 (L1 resolution verified), and two live defects

CriticFrontier alerted that `accept-c.py` APPEND (`allowed_new = NEW_IDS ∪ {S801..S804}`) and
`accept-ca.py` D4 (`rej_opened_today >= len(R66_REJECTS) + 2` = 6) are jointly unsatisfiable.
Facts I verified:
- Base/worktree has **22 rejected rows, none opened `2026-10-24`** → `rej_opened_today` starts at
  0; D4 therefore requires six today-dated rejected rows (S801–S804 + two more).
- C's own statement fixes the arithmetic: “registry 724 -> 752 rows (S805–S828 plus … S801–S804)”.

The L1 resolution (per-claim lands: A_r with S801–S804, A_c with S805–S828 only, A_ca with the
S829+ rejects and the lesson) **does satisfy both counters as written**, because APPEND compares
base→tip inside the clone at `--lands`: at A_c the appended set is exactly S805–S828 ∪ S801–S804,
so `extra_ids` is empty. No counter revision is needed. Consequences the L1 must hold to:
1. **A_r must land at or before A_c**, or C's own “724 -> 752” is false at its receipt (748 rows).
2. **The S829+ reject rows must sit inside `## Registry` at A_ca.** D4's `ROW_RE` is section-blind,
   but D2's census is not: `dry-run-ca.txt` already prints `outside_registry` findings for
   S776/S779–S800, and the new rejects would join them (E12) → D2 FAIL. Same rule as H3.
3. D4 checks uniqueness only for `R66_REJECTS`; a duplicated S829–S832 id passes D4 unnoticed.

Two defects found while checking this:
- **Ca's pre-data control receipt is stale (MEDIUM).** `telemetry/dry-run-ca.txt:1` records
  `# counter sha256 (self): 5e8915ac…`; the current `reports/round-67/accept-ca.py` hashes
  `5382ffed…`. The QUOTES edit therefore invalidated the base control after it ran; under this
  round's own criterion-19 discipline a receipt pinning a different counter proves nothing.
  `dry-run-c.txt` (`3e5f1a58…`) and `dry-run-o.txt` (`f21e9b43…`) both match their live files.
  Re-run the Ca control on base (verdict must stay FAIL) and overwrite the receipt before data.
- **The QUOTES leg was unsatisfiable before the fix (HIGH, now repaired).** The dry-run receipt
  was produced by `re.findall(r"\bS(8[0-2]\d)\b", …)` — `findall` returns the bare group
  (`805`…), intersected with `{"S805"…}` → always empty, so QUOTES could never PASS at *any*
  lands revision. Current code reads `r"\b(S8[0-2]\d)\b"` (verified at `:272`) and is correct.
  Note the base control's Ca FAIL was partly for this wrong reason; the re-run above removes the
  ambiguity.

Tooling: no installs or upgrades were performed (none needed). No lane files were modified;
this report is the only write.
