# RevSeparability2 — round 77 W2, claim C × Ca separability matrix (attack)

Seat: RevSeparability2 (leaf, wave 2, attack-only). Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin.
Base: `211f9526800906e0c585d878d265c37e5e090c15`.
Grounding W1 artifact: `.ufo/waves/round-77/w1/RevSeparability.md` (rev B review; its F1–F8 are re-derived here against the staged bytes).
Draft reviewed: sha256 `5f791d3aa94eef50d0eae6e9f53d391f9134f4e5fea79770cf4c220bd43ccc67` (8768 bytes) — `python3 -c "import hashlib;print(hashlib.sha256(open('.ufo/waves/round-77/CLAIMS-DRAFT.md','rb').read()).hexdigest())"`. The draft changed again after W1 (W1 reviewed `ed249cdf…`); this seat re-runs the matrix on the current bytes, per W1 F8.

Freeze state at review time: `reports/round-77/` holds only `telemetry/census-start.txt` (`glob reports/round-77/**` → 1 file). The frozen claims/counters do not exist yet, so the matrix below is built from (a) the current CLAIMS-DRAFT.md and (b) the actual staged W1 counter/ledger files under `.ufo/waves/round-77/w1/stage/`. Re-check pointers for the L1 are marked **[L1]**.

## Verdict

The two claims are separable in their machinery and in their staged data — **except on one file**: `corpus/README.md`. Three concrete defects are live in the staged bytes:

- **F1 (HIGH)** — `claims-C.skeleton.json` carries `"owned_inplace": ["corpus/README.md"]` (a bare string). The Ca counter silently drops non-dict entries (`accept-ca.py:962-964`), so the C-owned README heading edit at line 344 would be un-exempted at the combined probe → COMBINED red, exactly the r76 routed defect. The selftest cannot catch this shape (its mutant assumes a dict), and the shape originates in the C counter's own selftest fixture.
- **F2 (HIGH)** — the draft (line 31) and the frozen REPAIR allowlist permit README REPAIRs on any line, but the C counter's INDEX structurally rejects every in-place README edit except a `## <partition>/ (N)` heading parenthetical. All six staged README REPAIR candidates (755, 791, 811, 812, 830, 832) collide; the D-set already passes Ca's own gate (`LEDGER-CHECK-77: PASS pairs=11`), so nothing on the Ca side stops them. In the canonical order one such pair ⇒ ACCEPT-C-77 FAIL (INDEX red) at C-lands.
- **F3 (MEDIUM)** — the draft's Ca leg order (line 29) puts RECEIPTS before COMBINED; the counter table and `--emit-legs` put COMBINED before RECEIPTS. Transcribing the draft verbatim ⇒ LEGCOUNT refusal (exit 2) at Ca acceptance. The CHECKLIST Step 2 gate catches it if run.

---

## 1. The matrix (staged bytes, path by path)

Legend: **lands** = bytes the claim's landing adds/edits; **reads** = bytes the counter opens. C counter = `.ufo/waves/round-77/w1/stage/ExecAdaptC/accept-c.py` (3303 ln); Ca counter = `.ufo/waves/round-77/w1/stage/ExecAdaptCa/accept-ca.py` (4040 ln).

| path | C lands | Ca lands | C counter reads | Ca counter reads | collision? |
|---|---|---|---|---|---|
| `corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md` | NEW (C entry) | — | ENTRIES/INDEX/CITEDLINES | forbidden as stated_at (`corpus/knowledge/**`, SEPARABLE leg text) | no |
| `corpus/SOURCES.md` | +2 rows (S897, S898) + rule-2 cells + 2 non-row sections (Paths, Search log) | — | ROWS/INDEX/COLLCHECK | forbidden as stated_at (`corpus/SOURCES.md`); semantic grader reads base rows only | no (appends pass APPENDONLY as appended lines; rule-2 via R1EXEMPT fixtures) |
| `corpus/README.md` | heading 344 in-place `(32)`→`(33)`; +1 index row; new footer block at EOF | REPAIR allowed (mutable set) | INDEX — exempt set = last footer block + partition headings + adopted/base index rows + blanks; removed-side forgives **only** headings/blanks | APPENDONLY changed-line rule + COMBINED probe (owned_inplace record) | **YES — F1, F2, F4** |
| `corpus/lessons/round-77.md` | NEW (Gate) | — | GATE | not at base ⇒ cannot be stated_at; not in allowlists | no |
| `reports/round-77/evidence/S897.txt`, `S898.txt` | NEW | — | EVIDENCE | forbidden stated_at (`reports/round-77/evidence/**`) | no |
| `reports/round-77/telemetry/*` | census-start (freeze), census-end (C-lands) | r1exempt receipts, controls-ca, measures-ca-head | CENSUS | RECEIPTS/R1EXEMPT/COMBINED | no byte overlap (distinct names) |
| `SCORECARD.md` | — (zero reads: `grep -c -E 'ledger\.json\|SCORECARD' accept-c.py` → `0`) | appends `## Corrections — round 77` | — | ANNOTATE appends; `_carries_both_landings` reads the section at combined | no |
| `LOG.md`, `SKILL.md`, `SHONEN.md`, lessons ≤ r76 | — (`grep -c -E 'LOG\.md' accept-c.py` → `0`) | ANNOTATE stated_at (LOG/SCORECARD/lessons) + REPAIR (SKILL/SHONEN) | — | REPAIR/APPENDONLY/ANNOTATE | no (C reads none of them) |
| freeze artifacts (`claims.json`, `ledger.json`, counters, fixtures) | FROZENCFG (byte-identical) | FROZENCFG/LEDGER/RECEIPTS | reads claims.json@freeze; **never** `ledger.json` (grep → 0) | reads claims.json claim-C section + ledger@freeze | shared freeze, by design |
| `.ufo/waves/round-77/assimilation/**` | C scratch mirror | forbidden stated_at family (`.ufo/waves/round-77/assimilation/**`) | SCRATCHMIRROR | — | no |

Declared read-crossings (both by design): Ca reads C's bytes via the `--combined` tree and claims.json's claim-C section; C reads no Ca artifact anywhere (`ledger.json`, `SCORECARD`, `LOG.md` greps in accept-c.py all → `0`).

## 2. Does C depend on Ca land? — NO (verified)

1. **No flag**: `accept-c.py` argparse (`:3182-3197`) defines `--root --lands --freeze --fleet-root --work --selftest --emit-legs` — no `--combined`, no `--main`. C's acceptance input set contains no Ca handle.
2. **No Ca artifact reads**: `grep -c -E 'ledger\.json|SCORECARD' …/ExecAdaptC/accept-c.py` → `0`; `grep -c -E 'LOG\.md' …/ExecAdaptC/accept-c.py` → `0`. The 13 C legs (legs-generated.txt = `ENTRIES, ROWS, REPOINTED, GATE, EVIDENCE, REJECTS, GROUND, CITEDLINES, CENSUS, SCRATCHMIRROR, COLLCHECK, FROZENCFG, INDEX`) read only claims.json@freeze, base/lands trees, the entry, SOURCES, evidence, the Gate lesson, the assimilation mirror, and census receipts (SCHEMA-NOTE.md table).
3. **C lands cleanly without Ca**: INDEX grades the C-lands tree; with no Ca bytes present, no unexpected README diffs exist. The only C×Ca coupling is incidental (Ca's REPAIR bytes *inside C's graded tree* when stacked — §4).
4. The reverse dependency is declared and intentional: `--combined <C-lands>` is REQUIRED (refusal exit 2 otherwise) — `accept-ca.py:39-44`: *"`--combined <C-lands>` is REQUIRED — claim C lands after claim Ca in round 77 and the COMBINED leg grades the tree carrying both landings; a missing flag is a REFUSAL (exit 2)"*. So the dependency arrow points Ca→C, never C→Ca. **[L1]** keep it that way; W1 F6 (no C leg may read `ledger.json`/SCORECARD) holds in the staged C counter.

## 3. Does Ca cite new C source ids/paths? — NO (machinery + staged data verified)

**Machinery** (accept-ca.py): `lane_row_ids` derives `{897, 898}` from claim C's `row_set` (skeleton `:18-27`: S897←staged S897 cssn, S898←staged S903 onomastica; base SOURCES has neither: `git show 211f9526…:corpus/SOURCES.md | grep -c -E '^\| S(897|898) \|'` → `0`). The SEPARABLE leg then scans Ca's entire declared read set (ledger raw, corrections rows, named telemetry receipts, every stated_at line) for `S(\d{3,})` ∈ lane ids (`:2410-2413`) and for the frozen family literal `naming-systems*` (`:2415-2417`); `_path_matches_forbidden` (`:2343-2352`) rejects any stated_at in `corpus/SOURCES.md`, `corpus/knowledge/**`, `reports/round-77/evidence/**`, `.ufo/waves/round-77/assimilation/**` — all parsed from the frozen leg text itself (`:393-400`, `:930-939`).

**Staged data** — every candidate set scanned:
- `grep -rn -E 'S897|S898|naming-systems\.amend-2026-10-23'` over `ScoutLedger{A,B,C}/pairs.json`, `ExecAdaptCa/probe-real-ledger.json`, `probe-no-readme-overlap.json` → **no match** (exit 1).
- Every stated_at line at base, scanned for `S(897|898)|naming-systems`: LOG.md lines 3/447/826/1234/1655/2036/2611/3078/3457/3787 (D-set), lessons/round-75.md 35/44/245/251 (B-set), SCORECARD.md 1559 (A-set) → **no match** (all grep exits 1).
- B-set observe/rederive commands read `corpus/SOURCES.md` / `corpus/knowledge/myth-symbol/…b.md` **at the pinned base rev** (`211f9526…` in argv) — base bytes only; their stated_at sites (lessons/round-75.md) are in the ANNOTATE allowlist (LEDGER leg text, emit-legs.json). No forbidden stated_at, no C-added id.

One dead datum: ScoutLedgerA's `A-01` has **no `disposition` key** (pairs.json, raw read) and the staged receipt records `LEDGER-CHECK-77: FAIL pairs=11 problems=1 — A01: stated_text not found in LOG.md at base` (selftest-ca.txt tail). A-set as staged cannot enter the ledger; no separability impact, noted so the L1 does not mine it.

**[L1]** after freeze, re-run the two greps above against the frozen `ledger.json` + `claims.json` bytes; the counter enforces the same property at run time (SEPARABLE leg).

## 4. README line exemptions — the one real collision surface

**C-side INDEX exemption set, exactly** (accept-c.py `leg_index`, `:1824-1878`):
- exempt = lines of the **last** `Counts checked` block: forward over non-blank lines, backward over one blank + one `Total knowledge entries:` line + one blank. On base bytes that is lines **833–836** (`830: Total knowledge entries: 252.` / `832: Counts checked …(total 252 files; …32/32/40/29/24/95)` / `834: …253.` / `836: Counts checked …(total 253 files; …32/32/41/29/24/95)`).
- added-line check forgives: exempt positions, `## <partition>/ (N)` headings (parsed partitions), adopted/base-knowledge index rows (`README_ROW_RE`), blanks.
- **removed/edited check forgives only blanks and `## <partition>/ (N)` heading lines** (`:1869-1878`: every base line whose text disappears is bad unless blank or section-matched). Exempt positions do NOT shelter removals.

Consequence: **the only README line class a Ca REPAIR can edit without turning C's INDEX red at C-lands is a partition heading parenthetical** — and its new value must equal the live `.md` count at C-lands (`:1813-1817` live-count check). Everything else (old footer totals, prose) fails either the removed-side check or the older-footer byte-identity check (`:1806-1811`).

**Candidate classification** (all stated_texts verified present at the named base lines):

| pair | stated_at | base line text (verified) | C-INDEX verdict at C-lands |
|---|---|---|---|
| D11 (probe-real-ledger.json) | `corpus/README.md:755` | `Total knowledge entries: 243.` | **COLLIDES** (old footer line; removed-side + older-block identity) |
| LC77-C-01 | `corpus/README.md:811` | `` `## culture-material/ (36)` heading is left as filed and named as stale: the `` | **COLLIDES** (prose, not a heading line) |
| LC77-C-02 | `corpus/README.md:812` | `live directory holds 40 files and the section 38 rows. Registry: 804 -> 808` | **COLLIDES** (prose) |
| LC77-C-03 | `corpus/README.md:830` | `Total knowledge entries: 252.` | **COLLIDES** (older footer block; exempt block starts at 833) |
| LC77-C-04 | `corpus/README.md:832` | `Counts checked 2026-10-27 …(total 252 files; …)` | **COLLIDES** (older footer block) |
| LC77-C-05 | `corpus/README.md:791` | `Two linguistics entries landed (claim C; …) The ## linguistics/ (30) heading … stay as filed …` | **COLLIDES** (prose) |
| E11 (probe-no-readme-overlap.json) | `SHONEN.md:6` | round-75 tuple continuation line | separable — C never reads SHONEN.md |
| D01–D10 | `LOG.md:*` | verified | separable — append-only ANNOTATE, zero C reads of LOG.md |

Proof that the Ca side will NOT stop the colliding pairs: both staged ledger-check receipts print `LEDGER-CHECK-77: PASS pairs=11` — including the D-set whose 11th pair is the colliding README:755 REPAIR. README is in `REPAIR_MUTABLE` (`accept-ca.py:301`); the only line-level guard is `_c_appended_line` (`:1885-1902`), which checks collisions against claim-C `owned_inplace` **record** lines — with F1's empty record set it guards nothing, and even with the correct record (line 344) it would not see 755/791/811/812/830/832. The draft pins no constraint either: line 31 says only *"REPAIR may touch only frozen mutable {corpus/README.md, SKILL.md, SHONEN.md}, and only when a true base mismatch is proven"* — no line-shape rule. W1 F3 demanded exactly this pin; it is still missing.

**Value trap for the "safe" shape**: `## culture-material/` heading is base line **410** (`git show 211f9526…:corpus/README.md | grep -n '^## culture-material/'` → 410) and reads `(36)`; the live culture-material `.md` count at base is **41** (`git ls-tree -r --name-only 211f9526… -- corpus/knowledge/culture-material | grep -c '\.md$'` → 41; corroborated by the last footer vector `…/41/…` at line 836). The staged prose (line 812) and any repair value of **40** are wrong at base and would still fail C's INDEX live-count check at C-lands (`heading (40) != the 41 live .md files`). A heading repair is separable only as `(41)` — the live count, not the prose's stale claim. Linguistics: live 32 = heading 344 `(32)` ✓ true at base; C's own in-place edit makes it `(33)` = live 33 ✓.

**[L1]** required freeze pins (any one is insufficient alone): (a) zero README REPAIR pairs, or restrict README REPAIRs to `## <partition>/ (N)` heading parentheticals whose value equals the live count; (b) route LC77-C-01..05 and D11 to ANNOTATE (SCORECARD rows) — all are append-only-safe; (c) keep the §5 `owned_inplace` record so the combined probe exempts line 344.

## 5. Exact commit order

Required order (all four sources agree): **freeze → Ca-lands → C-lands (= the `--combined` tree, stacked)**.

1. `accept-ca.py:39-44` — *"claim C lands after claim Ca in round 77"*; missing `--combined` is a REFUSAL (exit 2), `:2875-2876`.
2. `_carries_both_landings` (`:2678-2712`): the combined rev must contain C's rows (S897/S898 in SOURCES), C's entries, and Ca's corrections rows — i.e. C's tree ⊇ Ca's bytes.
3. `combined_exemptions` is armed **only** inside `leg_combined` (`:2743-2745`) before re-running APPENDONLY; the main Ca-lands run never arms it — C bytes in Ca-lands ⇒ main APPENDONLY red (the r75 measured inversion, quoted in W1 §4).
4. Precedent receipt, `reports/round-76/telemetry/measures-ca.txt:1` (re-verified): `$ python3 -B reports/round-76/accept-ca.py --root . --lands a43ed807… --freeze df0f0309… --fleet-root /home/vgpnk/Projects/shokunin --combined 722e69ff… --main a43ed807… --work /fast/scratch/hyaku/kotodama-r76/final-ca-counter` — Ca-lands first, C-lands as combined.
5. C's counter has no order input at all (§2) — C is order-blind by construction; the order exists to protect *Ca's* combined probe and *C's* INDEX view of the README.

**F3 — exact-order defect in the draft**: CLAIMS-DRAFT.md line 29 orders the Ca lineage `…, SEPARABLE, RECEIPTS, COMBINED, FROZENCFG, STAMP`; the counter table (`LEG_SPECS`, `:334-421`) and `--emit-legs` (emit-legs.json, verified this seat) order `…, SEPARABLE, COMBINED, RECEIPTS, FROZENCFG, STAMP`. LEGCOUNT refuses a frozen `legs[]` that differs in order (`accept-ca.py:48-50`, docstring "the frozen leg table is not exactly the twelve implemented legs in table order"). The CHECKLIST Step 2 gate (`legcount.py --claim Ca`, "regenerate legs[] from the counter") is the designed catch — it must actually run before the freeze commit. Claim C's draft order matches legs-generated.txt exactly (13/13) ✓.

## 6. Findings by severity

- **F1 (HIGH — blocks Ca's COMBINED leg at acceptance if installed as-is):** `claims-C.skeleton.json` `owned_inplace` is the bare string `["corpus/README.md"]`. The Ca counter's constructor keeps dicts only (`accept-ca.py:962-964`: `[x for x in … if isinstance(x, dict)]`), so the record silently vanishes; the combined probe then reports `corpus/README.md: changed lines outside REPAIR stated_at lines [344]` → COMBINED red — the r76 failure ("the `owned_inplace` config has no valid line number") reintroduced through the skeleton. Nothing catches it earlier: `_readme_exemption_problems` (`:2648-2680`) only inspects surviving dicts; the selftest mutant `readme-exemption-no-line` (`:3784-3797`) does `dict(claim["owned_inplace"][0])` — it presumes a dict (and would itself crash on the skeleton's value) — so `SELFTEST: 199/199` is green on exactly the wrong shape. The shape propagates from the C counter's own fixture (`accept-c.py:2727` also `"owned_inplace": ["corpus/README.md"]`; harmless there because C never consumes the key — SCHEMA-NOTE.md: "loadable, not graded"). **Fix for the L1:** freeze the W1 §5 record — `{"path": "corpus/README.md", "base_line": 344, "base_text": "## linguistics/ (32)", "after_text": "## linguistics/ (33)"}` — with `base_text` re-measured at the freeze bytes (any insertion above line 344 invalidates it), and add a bare-string `owned_inplace` mutant to the Ca selftest so the class cannot ship twice (W1 §5's selftest requirement, only half-implemented).
- **F2 (HIGH — one valid Ca pair breaks C in the canonical order):** draft line 31 + the REPAIR allowlist admit README REPAIRs on any line; C's INDEX structurally rejects all but heading parentheticals (§4). All six staged README candidates collide; the D-set already passes Ca's gate. Pin "zero README REPAIR pairs (or heading-parenthetical-only, value = live count)" in the frozen claim text and route the six candidates to ANNOTATE.
- **F3 (MEDIUM):** draft Ca legs[] order `RECEIPTS, COMBINED` ≠ counter/emit-legs `COMBINED, RECEIPTS` → LEGCOUNT refusal if transcribed; run CHECKLIST Step 2 and regenerate legs[] from `--emit-legs`.
- **F4 (MEDIUM — trap inside the only safe shape):** the culture-material heading lives at line **410** (not at the prose lines 811/812 the candidates target) and its separable repair value is **41** (live), not the 40 the staged prose claims; a `(40)` repair fails C's INDEX live-count check at C-lands.
- **F5 (INFO):** ScoutLedgerA's A-01 lacks `disposition` and its ledger-check receipt is FAIL — dead candidate; do not mine. Freeze-blocker records FMB-1/FMB-2 (manifest.json) quote the pre-rev-B draft (`LEDGELIST?` at "line 62"); the current draft has zero `LEDGELIST` occurrences (verified: byte count 0) and its C/Ca leg lists match the counters exactly — the blocker list is stale, not the draft.
- **F6 (INFO — C read hygiene re-verified):** accept-c.py greps for `ledger.json`/`SCORECARD`/`LOG.md` → 0 each; no `--combined`; W1 F6/F7 hold in the staged bytes. SEPARABLE's forbidden stated_at set and family/id scans are frozen in the leg text and enforced at `:2343-2422`.

## 7. Residual risk / not run

- No counter was executed against any landing (none exists; leaf scope, attack-only). Every collision claim above is textual proof from the staged code (cited line numbers) plus verified base bytes — the L1 should confirm empirically at acceptance time by running accept-ca with `--combined <C-lands>` after both landings, in the §5 order.
- The INDEX exempt-block arithmetic was applied by hand to the base bytes (836 lines; last block 833–836); if any landing inserts a README line above 344 the byte-exact record check shifts (W1 §4 invariant) — freeze the "no insertion above 344" invariant.
- Untracked-scratch discipline: no fixture git repos and no scratch writes were needed; `/fast/scratch/hyaku/kotodama-r77/RevSeparability2` was never created (`ls | grep -c RevSeparability2` → 0). Lane git/jj/index untouched; only this Report file written. Tool installs: none; pacman untouched.
- **[L1] post-freeze re-checks:** (1) sha256 of the final CLAIMS-DRAFT/claims.json and re-verify line 344 + the §5 record against the freeze bytes; (2) re-run the §3 greps against the frozen ledger.json; (3) run `legcount.py --claim C --claim Ca` before the freeze commit; (4) rehearse both counters in the §5 order against rehearsal landings before installing.
