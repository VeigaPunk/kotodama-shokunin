# RevSeparability — round 77 W1, claim separability attack (C × Ca)

Seat: RevSeparability (leaf). Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin.
Base: 211f9526800906e0c585d878d265c37e5e090c15. Reference machinery: reports/round-76/{accept-c.py, accept-ca.py, claims.json, ledger.json, telemetry/} and .ufo/waves/round-76/ (read-only).

Draft reviewed: sha256 `ed249cdf9a089eb201b6e2411c77662748df789f42b140b3fd424e43c392fa8b` — `sha256sum .ufo/waves/round-77/CLAIMS-DRAFT.md` (untracked: `git status --porcelain` → `?? .ufo/waves/round-77/CLAIMS-DRAFT.md`). NOTE: the draft changed mid-review. Rev A (first read) named C legs "FROZENCFG, STAMP, LEDGELIST?, COUNTS, …, APPENDONLY, …, RECEIPTS"; rev B (37 lines, reviewed here) names the 13 lineage legs "ENTRIES, ROWS, REPOINTED, GATE, EVIDENCE, REJECTS, GROUND, CITEDLINES, CENSUS, SCRATCHMIRROR, COLLCHECK, FROZENCFG, INDEX". Findings below are against rev B; the rev-A-only hazards are recorded in F6 in case the L1 reintroduces those legs.

## Verdict

Separable, with four conditions the freeze must pin. The one r76 routed defect this seat owns — the COMBINED README exemption — is real and reproducible from r76's own run receipt; the exact record shape for r77 is in §5 with line number **344**.

---

## 1. Enumerated landed paths

Claim C lands (from rev B after-state; every path verified against base bytes):

| # | path | change kind |
|---|---|---|
| C1 | `corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md` | NEW file |
| C2 | `corpus/SOURCES.md` | +2 appended rows (S897, S898) + optional rule-2 cell edits on pre-existing rows (used-by/status/recheck only) + required non-row section appends (Paths, Search log; INDEX-checked, ROWS-exempt) |
| C3 | `corpus/README.md` | owned_inplace heading parenthetical at base line 344; +1 index row inside the linguistics section (line >344); appended new footer block at EOF |
| C4 | `corpus/lessons/round-77.md` | NEW file (## Gate incl. ≥1 admit + ≥1 reject; search log) |
| C5 | `reports/round-77/evidence/S897.txt`, `S898.txt` | NEW files (window grammar) |
| C6 | `reports/round-77/telemetry/census-start.txt` (freeze), census-end receipt (C-lands) | NEW files |
| C7 | freeze: `reports/round-77/accept-c.py`, `accept-ca.py`, `claims.json`, `ledger.json`, fixtures, r1exempt green/red receipts | frozen strictly before both landings |

Claim Ca lands:

| # | path | change kind |
|---|---|---|
| A1 | `SCORECARD.md` | appended `## Corrections — round 77` rows, first cell = pair id (ANNOTATE) |
| A2 | `corpus/README.md`, `SKILL.md`, `SHONEN.md` | in-place REPAIR edits at frozen stated_at `path:line` (mutable set, red-at-base only) |
| A3 | `reports/round-77/telemetry/` | r1exempt-green.txt, r1exempt-red.txt, controls-ca.txt (freeze), measures-ca-head.txt (Ca-lands/combined receipt) |
| A4 | freeze: ledger.json etc. | shared with C7 |

Base facts the matrix rests on:

- `## linguistics/ (32)` is base README line **344** — `git show 211f9526…:corpus/README.md | sed -n '344p'` → `## linguistics/ (32)`; file has 836 lines — `| wc -l` → 836.
- Registry 820 rows — `git show 211f9526…:corpus/SOURCES.md | grep -cE '^\| S[0-9]+ \|'` → 820; last id S896 — `… | grep -E '^\| S[0-9]+ \|' | tail -3` → S894, S895, S896. Knowledge files 253 — `git ls-tree -r --name-only 211f9526… -- corpus/knowledge | grep -c '\.md$'` → 253. Matches the draft's 820→822 / 253→254.
- Stale README footer totals (the only red-at-base README statements): lines 755 (`…243.`), 798 (`…247.`), 819 (`…249.`), 830 (`…252.`) — `git show 211f9526…:corpus/README.md | grep -n 'Total knowledge entries'` (output above; line 834 `…253.` is true at base).

## 2. Separability matrix

Legend: lands = bytes the claim's landing commit adds/edits; reads = bytes the counter opens. "APPENDONLY-set" = the files the frozen Ca APPENDONLY leg protects (parsed from the leg text; r76 frozen set: LOG.md, SCORECARD.md, corpus/lessons/round-75.md, corpus/QUALITY.md, SHONEN.md mark lines; corpus/SOURCES.md graded semantically; corpus/README.md deliberately NOT protected — REPAIR-only).

| path | C lands | Ca lands | C counter reads | Ca counter reads | collision? |
|---|---|---|---|---|---|
| corpus/SOURCES.md | appends + rule-2 cells | — | ROWS/INDEX/COLLCHECK | semantic grader (base rows only) | no — see §3a |
| corpus/README.md | C3 (heading 344 + index row + new footer) | A2 possible (REPAIR) | INDEX (R4/R5/R7 embedding) | APPENDONLY changed-line rule + COMBINED probe | **YES — §3c, §4, §5** |
| SCORECARD.md | — | appends only | — (0 reads — `grep -c 'SCORECARD' reports/round-76/accept-c.py` → 0) | ANNOTATE (append-only file) | no |
| SKILL.md / SHONEN.md | — | A2 (REPAIR, non-mark lines) | — | REPAIR + APPENDONLY | no (SHONEN edge: F4) |
| LOG.md, lessons round-75/76, QUALITY.md, SHONEN mark lines | — | — (stated_at only, no bytes land) | — | protected, zero removed lines | no |
| corpus/lessons/round-77.md | C4 NEW | — (not at base ⇒ cannot be stated_at; not in ANNOTATE allowlist) | GATE | — | no |
| knowledge entry, evidence/, .ufo/waves/round-77/** | C1, C5 | — | C legs | forbidden stated_at (SEPARABLE) | no |
| reports/round-77/telemetry/ | C6 census-* | A3 r1exempt-*, measures-ca-head | CENSUS | RECEIPTS/R1EXEMPT/COMBINED | no byte overlap (shared dir, distinct names) |
| claims.json / ledger.json / counters / fixtures | freeze | freeze | FROZENCFG (byte-identical at lands) | FROZENCFG/LEDGER | shared freeze, by design |

Read-crossings (declared, both fine): accept-ca reads C's bytes exactly twice — the frozen claims.json claim-C section (row_set/entries/owned_inplace) and the COMBINED probe tree. accept-c reads no Ca artifact in r76: `grep -c 'SCORECARD' reports/round-76/accept-c.py` → 0; `grep -c 'ledger\.json' reports/round-76/accept-c.py` → 0. Rev B's C leg list contains no ledger-reading leg — keep it that way (F6).

## 3. The three asked questions

**(a) Does Ca's APPENDONLY file set intersect C's appended files?** NO. C lands none of the protected files; its Gate file (round-77.md) does not exist at base and is outside both the protected set and the ANNOTATE allowlist. C's bytes enter Ca's grading only through the COMBINED probe, where the changed-line rule ("every changed line elsewhere is a REPAIR pair's stated_at line or an appended line") sees C's heading edit — that is what §5's exemption record is for. Evidence of the mechanism: `grep -n 'combined_exemptions' reports/round-76/accept-ca.py` → 1913 (consumed in leg_appendonly), 2570 (armed only inside leg_combined before re-running leg_appendonly at the combined rev). Consequence: **armed nowhere else** — so a Ca-lands tree that already contains C's bytes fails main APPENDONLY (that is the r75 measured failure, §4).

**(b) C appends NEW SOURCES rows — inside the rule-2 exemption?** NO, and it does not need to be. Rule 2 (status/recheck/used-by cells) governs only rows PRESENT AT BASE: sources_diff iterates base rows only (`for rid, (_bln, bcells) in sorted(base_rows.items())`, reports/round-76/accept-ca.py:577) and the leg text says "changed line on a PRE-EXISTING row". S897/S898 are added lines; they pass APPENDONLY under the general appended-lines allowance, not under R1. Added non-row lines (Paths/Search-log appends) also pass: sources_diff's non-row check collects only base lines whose text no longer appears at lands (removed-side hunks, accept-ca.py:601-620) — appends are invisible to it. The only genuine rule-2 usage available to C is an optional used-by re-point of a pre-existing row onto the admitted entry — exempt iff the edited cell set ⊆ {status, recheck, used-by} (the r76 r1-mixed-red fixture proves a teaches edit alongside a used-by edit fails). Rev B's C kill rule already carries "changed pre-existing row outside rule-2 cells" and "non-admitted `used-by`" — correct; freeze them verbatim into the ROWS/INDEX leg texts.

**(c) Does C's README index/footer edit collide with Ca's README REPAIR pair?** Three distinct collisions live on this file:

- **C-heading × Ca-APPENDONLY (combined tree)** — the r76 routed defect; fixed by the §5 record.
- **Ca-REPAIR × C-INDEX (C-lands tree)** — C lands LAST (§4), so C's INDEX grades a README already carrying Ca's bytes. C's INDEX freezes every base line except partition-count heading parentheticals and exempts only the appended new footer block (reports/round-76/accept-c.py:4524-4549: exemption set = adopted index rows + last-footer block; R4 "an older `Counts checked` footer is not preserved byte-identically" fires otherwise). The stale totals at base lines 755/798/819/830 are exactly red-at-base REPAIR targets — and exactly INDEX-frozen lines. **One README REPAIR pair on any old-footer line and C's INDEX is red at C-lands in the canonical order.** Rev B says "REPAIR may touch only frozen mutable {corpus/README.md, SKILL.md, SHONEN.md}" — it does not carry the r76 INDEX-side carve-out. Required at the freeze: EITHER pin "zero corpus/README.md REPAIR pairs" in the ledger contract (r76 shipped exactly this shape: 1 REPAIR, on SKILL.md:707 — `python3 -c "json.load(…)"` sweep → only L76-16, SKILL.md:707), OR freeze an explicit C-side INDEX exemption record `{"path": …, "line": N}` inside claims.json (shared freeze — keeps C's counter ledger-blind). Anything else re-runs the r75 class.
- **Ordering inversion** — if C landed first and Ca-lands contained C's bytes, main APPENDONLY reds on the un-exempted heading edit (combined_exemptions is not armed in the main run). See §4.

## 4. Required ordering

**freeze → Ca-lands (Ca bytes only) → C-lands = the combined tree (C stacked on Ca).** The Ca counter grades main legs at Ca-lands and re-grades APPENDONLY only at `--combined <C-lands>`; the C counter takes no `--combined` (round-76 precedent: run-controls.sh:136-137 "The C counter takes no --combined; the Ca counter requires it").

Measured precedent (r76 run receipt, `tail -30 reports/round-76/telemetry/measures-ca.txt`): `--lands a43ed807ea38b5fc5a7875a839d576cea73aba7c --freeze df0f0309d61e5485bb17035d3f8791b1e6a11d40 --combined 722e69ff6361aadf148cb46acbf6ac8fd147f59a` — Ca first, C second, combined = C-lands. The reverse order was measured red in r75 (quoted in .ufo/waves/round-76/w1/ConnectorSeparability.md:16): "Ca passes only with `--combined` and Ca-first, and Ca-second fails `APPENDONLY` on `corpus/README.md:376`".

Line-number invariant that makes the combined probe deterministic: **neither landing may insert or delete a README line above base line 344.** C's index row inserts inside the linguistics section (after 344), C's footer appends at EOF, and any README REPAIR target (old footers ≥755) sits below — all satisfied by construction; freeze the invariant anyway, since one insertion above 344 shifts the byte-exact §5 check off.

## 5. COMBINED leg — exact exemption record shape (with line number)

Rev B (line 29) says "COMBINED README exemptions carry actual path+line". The counter contract (r76 reference implementation, accept-ca.py:1913-1930, armed at :2570) requires, in the FREEZE's `reports/round-77/claims.json`, claim C:

```json
"owned_inplace": [
  {
    "path": "corpus/README.md",
    "base_line": 344,
    "base_text": "## linguistics/ (32)",
    "after_text": "## linguistics/ (33)"
  }
]
```

Enforced checks: `base_line` must be an int with `1 ≤ 344 ≤ len(base README lines)` and `344 ≤ len(lines at the combined tree)`; `base_lines[343] == "## linguistics/ (32)"` and combined-tree `lines[343] == "## linguistics/ (33)"`, byte-exact; only then is line 344 added to `c_exempt_lines` and the combined APPENDONLY probe can pass. Line number **344** — `git show 211f9526800906e0c585d878d265c37e5e090c15:corpus/README.md | sed -n '344p'` → `## linguistics/ (32)`.

The r76 defect, on the record: r76's claims.json owned_inplace (lines 170-176) carries only path/base_text/after_text — `grep -c 'base_line' reports/round-76/claims.json` → 0 — and the r76 run receipt says verbatim: `LEG FAIL COMBINED — the C-owned README heading change at line 410 is outside Ca's frozen APPENDONLY exemption; the `owned_inplace` config has no valid line number.` (reports/round-76/telemetry/measures-ca.txt). The companion receipt was never committed either: `ls reports/round-76/telemetry/measures-ca-head.txt` → `No such file or directory`, while the frozen COMBINED leg names it. Both fixes are already in rev B's kill rule ("uncommitted fixture receipt") and line 29 ("actual path+line") — this section is the concrete shape the L1 should freeze.

Selftest requirement (so the class cannot ship twice): the r76 selftest passed 170/170 while the config was defective — no scenario exercised a missing `base_line`. The r77 selftest must add an `owned-inplace-no-line` mutant (drop `base_line` from the record, expect the COMBINED leg red) and an `owned-inplace-shifted` mutant (insert a README line above 344 at the combined tree, expect red on the byte-exact check).

## 6. Findings by severity

- **F1 (HIGH — blocks Ca's COMBINED leg at freeze if omitted):** the §5 record with `base_line: 344`; without it the combined probe fails exactly as r76's did.
- **F2 (HIGH — order):** Ca-first/C-second stacked; reverse order red by construction (combined_exemptions armed only in the probe). Freeze the order in the claim text and rehearse both counters in that order.
- **F3 (HIGH — ledger admission rule):** no REPAIR pair may target any corpus/README.md line outside C's INDEX-exempt shapes (old-footer totals 755/798/819/830 are the attractive targets and all are INDEX-frozen). Pin "zero README REPAIR pairs" or the claims.json INDEX-exemption record; ScoutLedger seats' README candidates must be routed to ANNOTATE-eligible files or dropped.
- **F4 (MEDIUM — SHONEN edge):** the protected "mark lines" scope is exactly `^\s*[-*+]\s*\[[ ~xX]\]` lines + the `Marks:` legend block (`_shonen_mark_lines`, reports/round-76/accept-ca.py:677-690). Base SHONEN.md has 4 checklist items — `git show 211f9526…:SHONEN.md | grep -cE '^- \[.\]'` → 4. The stale round-75 tuple lives on the INDENTED CONTINUATION line 6 (`  asserted: …`), which is NOT a mark line, so a REPAIR of line 6 is landable — but the `- [~]` item lines themselves are unrepairable (and SHONEN.md is not in the ANNOTATE allowlist). Ledger verification must reject any pair whose stated_at resolves to a mark line.
- **F5 (MEDIUM — receipts at freeze):** r1exempt-green/red.txt and census-start.txt must be committed AT THE FREEZE; r76's R1EXEMPT failed on exactly this ("green/red receipts … are not committed at Ca-lands", measures-ca.txt) and measures-ca-head.txt was never committed at all. The Ca counter's RECEIPTS/R1EXEMPT legs must check the freeze blob, not the lands tree.
- **F6 (LOW — keep C Ca-blind):** rev A briefly gave C "STAMP, LEDGELIST?, COUNTS, APPENDONLY, RECEIPTS". Any C leg that reads reports/round-77/ledger.json or SCORECARD.md is an undeclared read-crossing (nothing polices C's read set symmetrically — SEPARABLE polices only Ca's). Rev B's 13-lineage list is clean; if LEDGELIST ever returns, scope it to claims.json's legs[] table, never ledger.json. Likewise C's ROWS/INDEX must not import Ca's "changed lines elsewhere" APPENDONLY clause — C-lands contains Ca's SKILL/SHONEN repairs, which no ledger-free C exemption can explain.
- **F7 (INFO — SEPARABLE forbidden set):** rev B says "no C-added path or S-ID may enter Ca's read set" but does not enumerate the forbidden stated_at paths. Freeze the r76 shape re-spelled for r77: corpus/SOURCES.md, corpus/knowledge/**, reports/round-77/evidence/**, .ufo/waves/round-77/**.
- **F8 (INFO — draft mutability):** the draft changed during this review (rev A → rev B; both hashed only in prose — rev A's bytes were not hashed before replacement, so only its leg-list difference is recorded here). The L1 should re-run this matrix against the final bytes at freeze; the §5 line number must be re-verified if anything inserts above README line 344 before the freeze.

## 7. Residual risk / unrun checks

- Not run (out of leaf scope, named for the L1): executing either counter against any landing; the census tier split (draft says "820 rows, A493/B311/C16, mined725/queued58/rejected37" — the 820 re-derived here — `grep -cE '^\| S[0-9]+ \|'` → 820 — the tier/status splits are UNRUN by this seat); the S897/S898 document identity and capture byte-identity claims (ScoutDoc/Capture seats' territory); no fixture repos were created (no git mutation anywhere; scratch dir /fast/scratch/hyaku/kotodama-r77/RevSeparability held only reads and is removed before yield).
- Residual: the combined tree is assumed to be C-lands itself (r76 shape, measures-ca.txt) rather than a separate merge commit; if r77 instead materializes a merge, the §5 check runs against that tree and the line-344 invariant must hold there. Tool installs: none.
