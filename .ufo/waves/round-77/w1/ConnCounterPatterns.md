# ConnCounterPatterns — round 77, wave 1 (connector, leaf, read-only)

Seat: ConnCounterPatterns-2 · Lane: kotodama-shokunin · Lane base: 211f9526800906e0c585d878d265c37e5e090c15
Scope: leg-name lineage across `reports/round-73..76/accept-c.py` and `accept-ca.py`; recommended frozen `legs[]` for both round-77 counters.
Evidence: committed blobs in the lane repo (`reports/round-7x/*`, `.ufo/waves/round-76/*`, `corpus/lessons/round-76.md`), read-only. No counter was executed. Receipts: `.ufo/waves/round-77/w1/stage/ConnCounterPatterns/lineage-receipt.txt`, `lineage.json`, `gen_legs.py`.

## Verdict

1. **The premise is inverted.** No leg is r76-only. SCRATCHMIRROR existed in the C counter and frozen list for r73, r74 and r75, and was **removed** in r76. COLLCHECK exists r73–r76. FROZENCFG and INDEX entered at r74 and are not r76-only. The r76 C changes were one removal (SCRATCHMIRROR) and one duplication (INDEX listed twice); the one Ca removal (TRACKED) happened in r75, and the Ca legs R1EXEMPT and COMBINED were added in r75.
2. **The r76 C counter's "11/13" double-counts INDEX.** Its frozen table is 13 slots but 12 distinct checks. `measures-c-final.txt` prints `LEG PASS INDEX` twice (lines 36 and 43), so the 11 PASS lines contain one duplicated pass.
3. **Both drafts need edits before freeze.** Draft C drops REPOINTED and CITEDLINES without a stated reason, adds five names with no lineage (STAMP, COUNTS, APPENDONLY, RECEIPTS, and `LEDGELIST?` with a literal question mark), and so cannot match a generated table. Draft Ca drops NOSTUB, which is the guard that caught L76-19/20/21, and adds `LEDGELIST`, which no round implements.
4. **Recommended frozen legs** (generated from the r75 table shape, which is the last table with 13 distinct C names): C = 13 names with SCRATCHMIRROR restored; Ca = the r76 12-name table unchanged. See §3.
5. **Stability caveat.** Leg *names* are stable across rounds; leg *bodies* are not. Of the 13 functions in the r75 C table, 6 are AST-identical in r76 (CENSUS, CITEDLINES, COLLCHECK, EVIDENCE, GATE, REJECTS); of the 12 in the r75 Ca table, 5 are (ANNOTATE, BASEMISMATCH, NOSTUB, R1EXEMPT, STAMP). "Stable" below means name-stable.

## 1. Commands and raw outputs (summary)

- Counter leg tables: `grep -n 'LEGS = (' -A14 reports/round-76/accept-c.py` shows `ENTRIES…CENSUS, INDEX, COLLCHECK, FROZENCFG, INDEX` (lines 6381–6394). `round-74/accept-c.py` and `round-75/accept-c.py` (lines 1832–1846, 5917–5931) show `…CENSUS, SCRATCHMIRROR, COLLCHECK, FROZENCFG, INDEX`.
- Frozen lists: `python3 -B` reading `reports/round-7{3,4,5,6}/claims.json` `claims[].legs[]`, name = text before the first colon (output in `lineage-receipt.txt`). Output: r73 C 11 names (incl. SCRATCHMIRROR), r76 C 13 entries with INDEX twice and no SCRATCHMIRROR.
- Table-vs-frozen cross-check: `lineage.json` matches every claims.json list: `lineage matches claims.json: True` (`lineage-receipt.txt`).
- Body identity: `ast.dump` of each `leg_*`/`_leg*` function, docstring removed, consecutive rounds. Output summarized in §2 notes.
- Generator check: `python3 -B .ufo/waves/round-77/w1/stage/ConnCounterPatterns/gen_legs.py reports/round-76/accept-c.py` → `REFUSED duplicate legs in table: INDEX`, exit 2. The same script on round-74 and round-75 accept-c.py and round-75 and round-76 accept-ca.py returns `distinct=13`, `distinct=13`, `distinct=12`, `distinct=12` with exit 0.
- r76 measured output: `reports/round-76/telemetry/measures-c-final.txt` — `ACCEPT-C-76: FAIL legs=11/13` (line 45); the PASS lines are at 24, 27–32, 34, 36, 40, 43 (11 lines, INDEX at 36 and 43).
- r76 repair receipt: `.ufo/waves/round-76/w1/stage/L1/freeze-control-legcount-redbefore.txt` — before repair the counter REFUSED with `LEGCOUNT … this counter implements 13 (…,SCRATCHMIRROR,…)`; `pre-data-counter-repair.txt` line 3: the counter was "repaired to implement the exact frozen 13-slot sequence; both INDEX slots run the same README predicate", and "the frozen C counter does not claim a scratch-mirror leg."
- Lesson record: `corpus/lessons/round-76.md:89` R76-M2 — "frozen C leg names did not match the implemented leg table (duplicated INDEX, omitted SCRATCHMIRROR)… Counter leg implementation repaired to match the already-frozen 13-leg list before data." `corpus/lessons/round-76-verifier-spotcheck.md` item 5: "Next freeze should regenerate the leg list from the leg table."
- LEGCOUNT is list equality only: `reports/round-76/accept-c.py:6574` (`if len(frozen_legs) != len(ours) or frozen_legs != ours`); `reports/round-76/accept-ca.py` ~2719 (`frozen_names != list(REQUIRED_LEGS)`). Neither refuses duplicates, so a duplicate in both table and claims passes silently.

## 2. Leg-lineage table

Key: ✔ present in the counter and in the frozen list; — absent. "AST r75→r76": body identity between the two last rounds (ast.dump, docstring stripped).

### accept-c.py (claim C)

| leg | r73 | r74 | r75 | r76 | r77 DRAFT | AST r75→r76 | recommendation |
|---|---|---|---|---|---|---|---|
| ENTRIES | ✔ | ✔ | ✔ | ✔ | ✔ | changed | keep |
| ROWS | ✔ | ✔ | ✔ | ✔ | ✔ | changed | keep (draft's scope fix lives inside ROWS) |
| REPOINTED | ✔ | ✔ | ✔ | ✔ | **—** | changed | keep; draft drops it without stated reason |
| GATE | ✔ | ✔ | ✔ | ✔ | ✔ | same | keep |
| EVIDENCE | ✔ | ✔ | ✔ | ✔ | ✔ | same | keep |
| REJECTS | ✔ | ✔ | ✔ | ✔ | ✔ | same | keep |
| GROUND | ✔ | ✔ | ✔ | ✔ | ✔ | changed | keep |
| CITEDLINES | ✔ | ✔ | ✔ | ✔ | **—** | same | keep; draft drops it without stated reason |
| CENSUS | ✔ | ✔ | ✔ | ✔ | ✔ | same | keep |
| SCRATCHMIRROR | ✔ | ✔ | ✔ | **— (removed)** | — | function deleted | **restore**; rename the receipt constant to round 77, keep the leg name |
| COLLCHECK | ✔ | ✔ | ✔ | ✔ | ✔ | same | keep |
| FROZENCFG | — | ✔ | ✔ | ✔ | ✔ | changed each round (3 distinct bodies r74/r75/r76) | keep; regenerate from the freeze blob |
| INDEX | — | ✔ | ✔ | ✔ **×2** | ✔ | changed | keep **once** |
| STAMP | — | — | — | — | ✔ | — | no C lineage (STAMP is a Ca leg r73–r76); add only as a new, implemented leg, else drop |
| APPENDONLY | — | — | — | — | ✔ | — | no C lineage (Ca-only r73–r76); same as above |
| RECEIPTS | — | — | — | — | ✔ | — | no C lineage (Ca-only r74–r76); same as above |
| COUNTS | — | — | — | — | ✔ | — | no lineage in any round; define or drop |
| LEDGELIST? | — | — | — | — | ✔ | — | no lineage; the `?` makes the name unmatchable by the generator; drop or define |

Counts: r73 11 legs (= 11 distinct), r74 13, r75 13, r76 13 slots / 12 distinct / 11 PASS lines.
Stable in all four rounds: ENTRIES, ROWS, REPOINTED, GATE, EVIDENCE, REJECTS, GROUND, CITEDLINES, CENSUS, COLLCHECK.

### accept-ca.py (claim Ca)

| leg | r73 | r74 | r75 | r76 | r77 DRAFT | AST r75→r76 | recommendation |
|---|---|---|---|---|---|---|---|
| LEDGER | ✔ | ✔ | ✔ | ✔ | ✔ | changed | keep |
| BASEMISMATCH | ✔ | ✔ | ✔ | ✔ | ✔ | same | keep |
| REPAIR | ✔ | ✔ | ✔ | ✔ | ✔ | changed | keep |
| ANNOTATE | ✔ | ✔ | ✔ | ✔ | ✔ | same | keep |
| APPENDONLY | ✔ | ✔ | ✔ | ✔ | ✔ | changed | keep |
| NOSTUB | ✔ | ✔ | ✔ | ✔ | **—** | same | **keep**; draft drops it while listing it as a routed r76 failure |
| SEPARABLE | ✔ | ✔ | ✔ | ✔ | ✔ | changed | keep |
| TRACKED | ✔ | ✔ | — | — | — | — | removed r75; no removal rationale found (see §5) — optional re-add |
| RECEIPTS | — | ✔ | ✔ | ✔ | ✔ | changed | keep |
| FROZENCFG | — | ✔ | ✔ | ✔ | ✔ | changed (r74 = r75 body, r76 differs) | keep |
| R1EXEMPT | — | — | ✔ | ✔ | ✔ | same | keep |
| COMBINED | — | — | ✔ | ✔ | ✔ | changed | keep |
| STAMP | ✔ | ✔ | ✔ | ✔ | ✔ | same | keep |
| LEDGELIST | — | — | — | — | ✔ | — | no lineage; define or drop |

Counts: r73 9 (docstring lists 8; TRACKED is in the call sites and claims.json but not in the docstring LEGS(8) block — `accept-ca.py:45`), r74 11, r75 12, r76 12.
Stable in all four rounds: LEDGER, BASEMISMATCH, REPAIR, ANNOTATE, APPENDONLY, NOSTUB, SEPARABLE, STAMP.

## 3. Recommended frozen legs[] for the round-77 counters (generated-from-table rule)

**accept-c.py (claim C), 13 distinct, = the r75 table exactly:**
```
ENTRIES, ROWS, REPOINTED, GATE, EVIDENCE, REJECTS, GROUND, CITEDLINES, CENSUS, SCRATCHMIRROR, COLLCHECK, FROZENCFG, INDEX
```
Target verdict: `ACCEPT-C-77: PASS legs=13/13`.

**accept-ca.py (claim Ca), 12 distinct, = the r75 and r76 table:**
```
LEDGER, BASEMISMATCH, REPAIR, ANNOTATE, APPENDONLY, R1EXEMPT, NOSTUB, SEPARABLE, RECEIPTS, COMBINED, FROZENCFG, STAMP
```
Target verdict: `ACCEPT-CA-77: PASS legs=12/12`.

Why these lists:
- C restores SCRATCHMIRROR, which was dropped in r76 to satisfy LEGCOUNT, not retired by a recorded decision. Its receipt concept still applies (the r72 receipt exists at base at `.ufo/waves/round-72/assimilation/validate-receipt.txt`, and an r76 receipt exists at `.ufo/waves/round-76/assimilation/validate-receipt.txt`), so the round-77 receipt path is the only thing to rename.
- C lists INDEX once. The duplicate is what made r76 read 11/13.
- Ca's table is already in the frozen form; the r77 draft's changes (drop NOSTUB, add LEDGELIST) are not supported by lineage.
- Draft names with no lineage (C: COUNTS, LEDGELIST, STAMP, APPENDONLY, RECEIPTS; Ca: LEDGELIST) are excluded from the recommended lists. Add one only with its own implemented leg function, selftest scenario, and junk/do-nothing control.

**Procedure to make the frozen list generated (the r76 failure mode, R76-M2 and round-76 spotcheck item 5):**
1. Implement the final leg table in the counter (name + leg function, in order).
2. Produce `legs[]` by running the table through `lineage/gen_legs.py`-style extraction (`.ufo/waves/round-77/w1/stage/ConnCounterPatterns/gen_legs.py`) or an equivalent `--print-legs` mode in the counter; each entry is `NAME: <leg text>`, the leg text taken from that leg's docstring. Do not hand-type the names.
3. Add a duplicate refusal to LEGCOUNT in both counters: `if len(set(ours)) != len(ours): refuse`. Today `accept-c.py:6574` and `accept-ca.py:2719` compare lists only, so a duplicate passes.
4. Count distinct names in the verdict (`legs=<distinct pass>/<distinct total>`), so a duplicate cannot inflate the numerator.
5. Keep the freeze blob's leg text free of `?` and of names the table does not contain. `LEDGELIST?` would fail the match on the first character.

## 4. Draft-level findings for the L1 (per round-77 CLAIMS-DRAFT.md)

- **C**: the draft's "Leg list (generated from the counter's own leg table at freeze…)" is hand-typed; no counter table for r77 exists yet, and the list contains five names with no lineage plus a literal `LEDGELIST?`. Two lineage-backed legs (REPOINTED, CITEDLINES) are missing and SCRATCHMIRROR is missing. REPOINTED is the leg that ties each `source:` line to its adopted row URL, which the draft's kill rule ("an admitted entry citing an unmined or unopened row") depends on. Restore REPOINTED and CITEDLINES unless the L1 records an explicit retirement.
- **Ca**: "Legs … LEDGER, BASEMISMATCH, REPAIR, ANNOTATE, APPENDONLY, R1EXEMPT, SEPARABLE, COMBINED, RECEIPTS, FROZENCFG, STAMP, LEDGELIST" omits NOSTUB. The draft's own routed-defect list names NOSTUB as a red r76 leg, so dropping it removes a guard without a replacement. Restore it.
- Draft C's ROWS scope fix and COLLCHECK document-identity fix sit inside existing legs (ROWS, COLLCHECK), so no new leg is needed for them. The draft's `required_sections[]` is checked by INDEX, which is also inside the existing table.
- RECEIPTS in Ca r74–r76 re-executes a previous round's counter at its lands. r76's RECEIPTS leg re-ran the r75 Ca counter (`reports/round-76/telemetry/measures-ca.txt`: "round-75 Ca PASS receipt re-ran at frozen lands"). The r77 RECEIPTS leg must name its target round explicitly in the frozen text. The r76 Ca counter itself failed (`ACCEPT-CA-76: FAIL legs=5/12`), so it is not a PASS receipt to re-run.

## 5. Caveats and what was not checked

- Name-stable is not body-stable. Every counter round rewrote most leg bodies (§2 AST columns). A leg's presence in the table does not show the check is the same check.
- TRACKED's removal in r75: a narrow search (`grep -n TRACKED corpus/lessons/round-75.md LOG.md reports/round-75/*.md`, plus round-74 lessons) found no removal rationale for r75. A wider grep over `corpus/`, `.ufo/` and `reports/` was truncated at 48 files, so the reason is unlocated, not confirmed absent.
- No counter was executed. The recommended lists are derived from frozen text and committed table code only; the round-77 counters do not exist yet, so the generator output is a preview, not an acceptance run.
- `COUNTS` is not a leg name in any round (the only hit is a comment at `reports/round-76/accept-c.py:1556`). `LEDGELIST` is not in any round either; a sibling round-77 stage (`.ufo/waves/round-77/w1/stage/ExecAdaptCa/accept-ca.py` lines 428–429) defines it as a meta-leg asserting that `legs[]` equals the counter's own table. That matches §3 step 2 and is worth keeping as a *13th* Ca leg only if implemented with its own selftest; it does not change the 12 recommended names. I did not audit the sibling's implementation.
- Per-round scoring: r76 C's 11/13 is quoted from `measures-c-final.txt`; the "12 distinct" count is derived from the frozen list, not re-run.

## 6. Installs, scratch, writes

- Tools installed or updated: none (python3 stdlib only).
- Scratch: `/fast/scratch/hyaku/kotodama-r77/ConnCounterPatterns-2/` used for the generator copy; removed before yield.
- Writes: this report; `.ufo/waves/round-77/w1/stage/ConnCounterPatterns/{lineage.json, gen_legs.py, lineage-receipt.txt}`. Nothing under `reports/**`, `corpus/**`, the fleet root, `scripts/`, `templates/`, git state, or sibling lanes was written.

## 7. Checks the L1 should run after the r77 counters land (not run here)

- `python3 -B .ufo/waves/round-77/w1/stage/ConnCounterPatterns/gen_legs.py reports/round-77/accept-c.py` → 13 names, `distinct=13`, exit 0.
- Same for `reports/round-77/accept-ca.py` → 12 names, `distinct=12`, exit 0.
- Compare each output with the frozen `legs[]` list and with §3 before the freeze commit.
