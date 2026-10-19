# C11 — C-claim scribe: cartography evidence chain, integration-ready

- Seat: `C11` | role: scribe | claim: **C** (coverage) | round 47, loop 2
- Baseline: HEAD `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` (`6e9a30d`), equal to `reports/round-47/claims.json:7`
- Write cut: **2026-10-19T18:03Z**; every status below is what was on disk at that cut.
- Out path: `reports/round-47/cov/C11-scribe.md` (this file only). No corpus byte, instrument byte, or filed-round byte was written or staged. No `run-validation.py` executed, no commit/push/install/network.
- Canon: NON-CANON assembly and verification. This seat admits nothing and certifies no round.

**Verdict in one line:** the C premise, the README arithmetic, the topic coupling and the couples graph are all **measured green**, and an end-to-end staged apply is green — but the assembled draft is **854 lines (800 body) against P02's own 290–350 component budget (its stated >340 bloat line) and the partition's 221-line maximum**, and three factual defects remain in the head block/boundary table. **C is mechanically ready but not contract-ready: do not land until §5 D1–D5 are closed and C07 re-audits the assembled bytes.**

---

## 1. What this seat independently measured

All commands from the lane root, 2026-10-19, `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

| Check | Command | Result |
|---|---|---|
| HEAD == declared baseline | `git rev-parse HEAD` | `6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe` |
| Worktree | `git status --porcelain` | only `?? reports/round-46/review/`, `?? reports/round-47/`; no `corpus/` delta |
| Total entries | `find corpus/knowledge -name '*.md' | wc -l` | **223** |
| culture-material | `ls corpus/knowledge/culture-material/*.md | wc -l` | **25** |
| Index sweep | `python3 -B reports/round-28/readme/sweep.py` | `rows 223 files 223`, 0 missing, 0 `topic_mismatch`, 0 ghosts, `{}` drift, totals 223, footer `25/26/25/29/24/94`, `exit 0` |
| README digest | from sweep | `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` |
| Filename owners | `find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l` | **0** |
| Target path | `ls corpus/knowledge/culture-material/cartography-and-mapmaking.md` | **No such file** |
| Topic-line owners (K02 pattern) | `grep -rniE '^- topic:.*(cartograph|mapmak|portolan|cadastr|atlas|itinerar|survey|topograph|\bmap\b|\bcharts?\b)' corpus/knowledge/ | wc -l` | **11**, all metaphor/verb/handoff; 0 owners |
| `cartograph` footprint | `grep -rniF 'cartograph' corpus/knowledge/` | **2 files / 2 lines**: `myth-symbol/cosmology-cosmography.md:102`, `civilizations/mesoamerica-primary-sources.md:58` |
| Prior-round proposals | `grep -rliE '(cartograph|mapmak|portolan|cadastr|mappa mundi|stick chart|world map)' reports/ --include='*.md' | grep -vE '^reports/round-44/|^reports/supplement-opencode-1/'` | **0**; all 14 hits are r44's own chain or frozen supplement scratch copies |
| sort slot | `ls corpus/knowledge/culture-material/ | nl` | `calendar-festival-systems.md` 5, `costume-semiotics.md` 6 |
| README defect | arithmetic on `corpus/README.md:11` | `25+23+26+25+24+94 = 217`; live footer `25+26+25+29+24+94 = 223`; target rev-2.5 vector `25+26+26+29+24+94 = 224` |

The r44 K02 seed (`reports/round-44/scout/K02-gap-scout.md`, sha256 `a72fff27…f335f6`) is filed, never edited, and reproduces at this HEAD (K01 §1–§5 re-measured it independently; this seat's probes agree).

---

## 2. The assembled entry, as measured (not asserted)

Assembly order used: **C04 head block + C01 §1–4 + C02 §5–9 + C03 §10–15**, each lifted from its fenced block. Result written only to disposable `.scratch/c11-assembled.md` (removed after measurement).

| Measurement | Value |
|---|---|
| Total lines | **854** (head 51 + C01 199 + C02 424 + C03 177) |
| Body lines | **800** |
| Bytes | 132,075 |
| sha256 (assembly) | `bc12037c38f4472a5e8e7435fde95a98d3fa8f1c8305881b49f263384c1fc892` |
| H1 count | **1** |
| Numbered sections | **1–15, each exactly once, in order** (`1..15`; no duplicates) |
| Head fields, in order | `topic, gap filled, sources, source, couples, verified-at, recheck, scope` (8) |
| `- topic:` | 1 physical line, **766 chars**, sha256 `bc7274f411cc6977032ab2754ebff19def4a1f5240fe5882624fc76e744f4495`; byte-equal to the r44 seed |
| README row derived via `sweep.topic_of()` | `- \`cartography-and-mapmaking.md\` — <766 chars>` = **801 chars** |
| `- couples:` | one physical line, 4,085 chars, **21 unique tokens, 21/21 resolve** from `corpus/knowledge/culture-material/` (13 use `../`, the partition's attested style) |
| `(to-verify)` marks in sources | 20 |
| C01 §3 ↔ C02 §5 shared 5-grams | **7 of C01 §3's 1,511 5-grams = 0.5%** — no copy-paste; the redundancy is conceptual, not textual |

`reports/round-47/cov/C13-couples.md` independently confirms 21/21 direct resolution and predicts `+1 entry, +21 refs, +21 direct` in the resolver census; no dangling/ambiguous token.

### 2.1 The length fact

| Comparator | Value |
|---|---|
| P02's own budget (`plan/P02-c-plan.md:155-162`) | component sums 290–350; **>340 = bloat**; <230 = thin |
| Live culture-material range (`wc -l`, 25 files) | min 103, median 149, **max 221** |
| C07's executable band (`cov/C07-contract-audit.md` §7) | 100–260 |
| Assembled draft | **854** — 5.7× the median, **3.9× the max**, 2.5× P02's >340 bloat line |

Running C07's own extracted checker against the assembled bytes produces exactly one FAIL:

```text
PASS H1 exactly one / head fields / order / topic single line
PASS couples one physical line (4085 chars)
PASS gap filled records a count / not on an older baseline
PASS to-verify in sources (20 marks) / verified-at ISO + commit / scope
PASS calibration / build order / decision record / NON-CANON / handoff
PASS no promotion verbs / target free / no cartography topic owner
FAIL length in partition band: 854 lines
1 FAIL, 1 WARN
```

The WARN is expected (README row not filed yet). The FAIL is the draft as assembled, not a stale check: C07's audit itself predates the draft bytes and records `could-not-evaluate` on every content clause.

---

## 3. End-to-end staged integration — measured green

Method: copy `corpus/knowledge` (223 files) and `corpus/README.md` into `.scratch/c11-e2e/`, write the assembled entry at the target path, apply **C09's actual fenced diff** with `patch -p1` (rc 0), then run the filed sweep through its public `sweep(readme_text, root_override=…)` leg. The stage was deleted after measurement.

| Assertion | Measured |
|---|---|
| `patch` apply | `patching file corpus/README.md`, rc 0 |
| rows == files | **224 == 224** |
| partition vector | `civilizations 94, culture-material 26, linguistics 25, myth-symbol 26, synthesis 29, verification 24` |
| missing / ghosts / topic mismatch / drift | `[] / [] / [] / {}` |
| totals line / footer | **224** / `224` with `[25, 26, 26, 29, 24, 94]` |
| footer findings | `[]`; `ok: true` |
| rev-2.5 declared vector | `25/26/26/29/24/94` = **224** |
| repaired rev-2.4 vector | `25/26/25/29/24/94` = **223** |
| README row == entry `- topic:` | **True**, 766 == 766 chars |
| README sha256 after apply | `73985f68e48cbc7015eb00b1080796a5b93632eeb9b7ad76290074bf8de95afc` — **identical to C09's filed staged receipt** |
| corpus delta | exactly one added entry; no existing entry byte changed |

This confirms the C claim's mechanical `after_required`: **224 total, culture-material 26, sweep-green 224==224, vector sums 224, zero overwrites** — *conditional on the entry being trimmed/deduplicated to a landable size and the defects below being fixed*. The arithmetic is not at risk; the content contract is.

---

## 4. Evidence-chain status at the write cut

| Seat | Artifact | Status | Substance / verdict |
|---|---|---|---|
| K01 | `scout/K01-gap-recheck.md` | FILED | FRESH-OWNERSHIP at `6e9a30d`; 0 owners; names the "0 prior-round proposals" wording caveat (§6.3) |
| K02 | `scout/K02-seed-extract.md` | FILED | seed extracted; flags the r47 executor-mission mismatch (§9); measured entry contract |
| P01 | `plan/P01-plan.md` | FILED | F0–F6 pipeline; C order |
| P02 | `plan/P02-c-plan.md` | FILED | 15-section plan; fixed topic; **component budget sums 290–350, >340 stated as bloat** |
| C01 | `cov/C01-entry-a.md` | FILED | §1–4, 199 lines; boundary table (8 neighbours); five-condition register test; eight map forms |
| C02 | `cov/C02-entry-b.md` | FILED | §5–9, 424 lines; survey chain, scarcity/prestige, mapmaker trade, provenance, map-word etymology |
| C03 | `cov/C03-entry-c.md` | FILED | §10–15, 177 lines; build order, NON-CANON example, 14-row calibration bank, DR-CT-01..12, living-practice flags |
| C04 | `cov/C04-entry-header.md` | FILED | 8-field head block, 51 lines; topic byte-equal to seed; 21 couples |
| C05 | `cov/C05-freshness.md` | FILED | PASS at `6e9a30d`; **defect D6: wrong post-landing vector in §8/§9** |
| C06 | `cov/C06-source-audit.md` | **ABSENT** | source audit owed |
| C07 | `cov/C07-contract-audit.md` | FILED, content `could-not-evaluate` | audited pre-draft; its §7 checker now FAILs length (D1); re-audit owed |
| C08 | `cov/C08-boundary.md` | **ABSENT** | boundary adjudication owed (D4) |
| C09 | `cov/C09-readme.md` | FILED | rev 2.5 + rev-2.4 repair + 5th history hunk; staged sha `73985f68…`; `git apply --check` rc 0 |
| C10 | `cov/C10-sweep.md` | FILED | staged 224 green; control D proves sweep is blind to revision vectors; catches C05's slot swap (§5a) |
| C12 | `cov/C12-shelf.md` | **ABSENT** | external-shelf honesty owed |
| C13 | `cov/C13-couples.md` | FILED | PASS, 21/21 direct; +21 refs |
| C14 | `cov/C14-example.md` | **ABSENT** | worked-example review owed |
| V01 | `cov/V01-post-landing.md` | FILED | `staged-green / live could-not-evaluate`; §7 executable post-landing block |
| X04 | `cross/X04-coverage-critic.md` | FILED | topic real, not manufactured; **assembly volume-inflated, dedupe required**; boundary omission at `cosmology:27` |
| R03 | `review/R03-c-content.md` | **ABSENT** | non-author content judgment owed |

No C-chain artifact is silently assumed: every row marked ABSENT is `could-not-evaluate`, not a pass.

---

## 5. Defects register (blocking ones first)

**D1 — length / volume (BLOCKING).** Assembled 854 lines (800 body) vs P02's 230–290 budget and 103–221 live range; C07's own checker FAILs `854 > 260`; X04 §“assembly” calls the draft volume-inflated and requires dedupe. A 224 count with an 854-line entry is a coverage gain converted into a usability liability. **Fix:** dedupe/compress to ≤~340 lines (P02's stated bloat line) and re-measure; or obtain and file an explicit R03/C07 waiver naming the exception. Do not land silently at 854.

**D2 — conceptual duplication between C01 §3 and C02 §5.** C01 §3.2 Projection / §3.3 Scale / §3.4 Orientation / §3.5 Symbolization overlaps C02 §5.4 Project / §5.5 Scale / §5.6 Symbolize. Measured textual overlap is only 7 shared 5-grams (0.5%), so this is duplicate *coverage*, not copy-paste. **Fix:** keep one operational treatment (C02's chain) and reduce C01 §3 to the decision framing + authority claim, then re-run the length check. Orientation appears only in C01; keep it.

**D3 — false measurement in `- gap filled:` (BLOCKING for provenance honesty).** The head block says `grep -rli 'cartograph' …` → **"2 files / 3 lines"**. Measured: **2 files / 2 lines** (`cosmology-cosmography.md:102`; `mesoamerica-primary-sources.md:58`). `:71` does not contain the token "cartograph" (it says "not survey maps"). The entry must not land a miscount in its own gap statement; correct to 2/2 and re-check the other counts quoted there. X04 independently flagged this.

**D4 — boundary omission.** `myth-symbol/cosmology-cosmography.md:27` defines cosmography as "the projected, inhabited version: how the world is drawn (**maps**), named …, walked …, and built …". C01 §1.1 and C04 cite only `:71`/`:102` (the disclaimer) and never disposition `:27` (which appears to grant cosmography drawn maps). The boundary is still defensible — cosmography owns the world-model/world-diagram; the new entry owns the instrument sheet — but the table must state it, or C08/A02 will find a live contradiction. **Fix:** add a row/sentence citing `:27` and distinguishing "world drawn as cosmogram" from "surveyed, projected sheet".

**D5 — "0 prior-round proposals" wording.** Literally false at r47: r44 K02 is a prior-round scout that named cartography. The accurate statement (K01 §6.3, X04) is: **0 proposals before r44 K02; r44 K02 is the cited seed; never claimed, drafted or landed.** Record that formulation in the integration record and, if the entry repeats the phrase, in the entry.

**D6 — C05's post-landing vector is slot-swapped.** `cov/C05-freshness.md:273` and `:295` state `26/26/25/29/24/94`; slot 3 is culture-material, so the correct vector is **`25/26/26/29/24/94`**. C10 §5a measured that C05's vector fails `FOOTER_DIR_TOTALS`. C09/C10/V01 use the correct vector; the integrator must not copy C05's.

**D7 — C07 checker blind spot (not a draft defect).** C07 §7 reports `repo paths in couples resolve: 0 tokens` — a vacuous PASS because it matches only `corpus|tools|reports|examples` absolute paths, while C04 uses relative `../…` tokens. C13's resolver is the authoritative couples check (21/21). Do not cite C07's line as couples evidence.

**D8 — C07 content audit is stale.** It audited at 17:55Z with no draft bytes and recorded `could-not-evaluate` on QUALITY Q1–Q5. The `after_required` says "audits PASS"; C07 must re-run against the assembled bytes after D1–D3 are fixed.

**D9 — interpretation note on the vector threshold.** The claim's phrase "prose vector corrected to sum 224" cannot apply literally to the historical rev-2.4 line: the correct repaired rev-2.4 vector sums **223** (it describes r42's end state). "Sums 224" belongs to the rev-2.5 line. C09 encodes exactly this (rev 2.5 = 224, rev 2.4 = 223); reviewers should adopt that reading and not "fix" the repaired historical line to 224.

**D10 — pre-existing README duplicate H1** (`corpus/README.md:1` and `:3`). Out of scope; leave untouched.

---

## 6. Integrator apply order (fail-closed)

1. **Preconditions.** `git rev-parse HEAD` must be recorded; `find corpus/knowledge -name '*.md' | wc -l` = 223; `ls corpus/knowledge/culture-material/*.md | wc -l` = 25; target path ABSENT. Any deviation → stop and re-run K01/C05 freshness at the new HEAD.
2. **Close D1–D5 in the draft** (dedupe to ≤~340 lines; correct `cartograph` to 2/2; add the `cosmology:27` boundary disposition; fix the provenance wording).
3. **Re-audit.** C07 re-runs its §7 checker on the assembled bytes — must be 0 FAIL; C06/C08/C12/C14 must file PASSes; R03 must judge content. `audits PASS` is not satisfiable while any is ABSENT.
4. **Assemble in this order:** C04 head block → C01 §1–4 → C02 §5–9 → C03 §10–15. Measured pre-conditions now: 1 H1, sections 1–15 once each, 8 head fields in order.
5. **Pin the topic.** Take the row text from the **landed** entry via the sweep's own extractor, not from memory:
   ```bash
   python3 -B - <<'PY'
   import importlib.util
   s=importlib.util.spec_from_file_location("s","reports/round-28/readme/sweep.py")
   s=importlib.util.module_from_spec(s); s.loader.exec_module(s)
   print(s.topic_of("corpus/knowledge/culture-material/cartography-and-mapmaking.md"))
   PY
   ```
   Current text sha256 `bc7274f4…f4495` (766 chars). If D1/D2 edits change the topic, regenerate both the entry field and the README row in the same change.
6. **Apply the entry, then C09's diff.** Entry first, README second. C09's diff applies cleanly (`patch` rc 0); its staged README sha is `73985f68…5afc`.
7. **Post-landing assertions** (V01 §7, C10 §7, C09 §4): census 224/26; sweep `rows 224 files 224`, exit 0; footer `224` + `25/26/26/29/24/94`; rev 2.5 sums 224 and rev 2.4 repaired sums 223; row == `topic_of(entry)`; exactly one new entry and `corpus/README.md` modified; no other corpus delta; one topic owner. Predicted live receipt is §3 above.

---

## 7. Post-landing prediction (measured on the stage)

```text
parts {"civilizations": 94, "culture-material": 26, "linguistics": 25,
       "myth-symbol": 26, "synthesis": 29, "verification": 24}
rows 224 files 224
missing_from_index 0 []   topic_mismatch 0 []   orphan_rows 0 []   header_drift {}
totals_line 224 totals_ok True
footer {"total": 224, "dir_totals": [25, 26, 26, 29, 24, 94]}
footer_findings [] footer_ok True
ok True
```

These fields are unconditional given the six mechanical edits; the staged README sha is **not** a landing pin (it depends on C09's prose, which the integrator applies verbatim; this seat reproduced C09's digest exactly, so it is at least internally consistent).

---

## 8. could-not-evaluate ledger

| Item | Owner | Why not evaluated |
|---|---|---|
| Source honesty of every cited `path:line` and every Tier B item | C06, C12 | artifacts absent at the write cut; C04 self-checks 23 anchors and C02/C03 self-audit theirs, but those are author checks |
| Boundary truth for all neighbours (incl. D4) | C08 | absent; C01's table is an author draft |
| Worked-example internal consistency / declared-invented status | C14 | absent; C03 declares it NON-CANON and structurally sound |
| Contract PASS on delivered bytes | C07 re-audit | its audit predates the drafts; content clauses `could-not-evaluate` |
| Content quality vs padding | R03 | absent; X04's critic verdict is “real method, volume-inflated” |
| Tier B editions/pages | all authors | no network at seat time; every item is `(to-verify)` |

---

## 9. Handoff

- **For S01/R01/R02/Q01:** cite §1 for the verified premise, §2–§3 for the measured assembly and the green end-to-end apply, §5 for the blocking findings. The chain is **not** complete at this cut: four C verifiers and R03 are absent, and C07's content verdict is stale.
- **For the integrator:** do not land the 854-line assembly. Close D1–D5, re-run C07's checker to 0 FAIL, then apply in §6 order.
- **For W02/V01:** the landing spec's byte source is the **trimmed** four-fragment assembly; the topic row must be regenerated from the landed entry; the post-landing block is V01 §7.
- **Single largest residual risk:** a mechanically green 224 landing whose entry is 3.6× the partition maximum and carries a false count in its own gap statement — the coverage number would move while the craft contract regresses. That is exactly the trade this scribe report exists to prevent.

---

## Appendix — command transcript (trimmed)

```text
$ git rev-parse HEAD                                      -> 6e9a30dca8bff66e2aef50a8d611b01d2fe6dcfe
$ find corpus/knowledge -name '*.md' | wc -l              -> 223
$ ls corpus/knowledge/culture-material/*.md | wc -l       -> 25
$ python3 -B reports/round-28/readme/sweep.py             -> rows 223 files 223; footer 25/26/25/29/24/94; exit 0
$ find corpus/knowledge -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*' | wc -l
                                                          -> 0
$ grep -rniF 'cartograph' corpus/knowledge/               -> 2 files / 2 lines
$ grep -rliE '(cartograph|mapmak|portolan|cadastr|mappa mundi|stick chart|world map)' reports/ --include='*.md' | grep -vE 'round-44|supplement-opencode-1' | wc -l
                                                          -> 0
# assembly (scratch only)
head 51 + C01 199 + C02 424 + C03 177                      -> 854 lines / 800 body / 132,075 bytes
sections 1..15 exactly once; H1 1; 8 head fields in order; 21/21 couples resolve
topic 766 chars sha256 bc7274f4…f4495; README row 801 chars
# end-to-end stage: patch C09 diff + assembled entry, sweep(root_override)
rows 224 files 224; totals 224; footer [25,26,26,29,24,94]; ok True
rev2.5 25/26/26/29/24/94 = 224; rev2.4 25/26/25/29/24/94 = 223
row == topic True; README sha256 73985f68…5afc (matches C09 receipt)
# C07's own checker on the assembled bytes
FAIL length in partition band: 854 lines   (1 FAIL, 1 WARN)
```
