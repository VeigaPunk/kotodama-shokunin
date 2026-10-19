- Seat: A14 | verifier | claim A | date 2026-10-19 | baseline 139e3b6

# A14 — row-for-row verification of A10's receipt table against the A01–A09 fragments

**Mission** (`reports/round-33/targets.json:61`): "Verify A10's receipt table matches its
fragments row-for-row; flag any verdict not backed by a fragment."

**Bound artifact.** `reports/round-33/adj/A10-receipt.md` at **36,683 bytes, sha256
`df5e42de84784e587e33ded9622841fa8a5c0fd611d13a7d8bd9f54b08f8defb`** (revision 5, mtime
`2026-10-19 01:04:05 -0300`). A10 was rewritten at least five times during the wave
(rev1 16,915 B at 03:55Z → rev2 26,705 B → rev3 27,183 B → rev4 33,178 B → rev5 36,683 B);
this verification covers the rev5 bytes only. §5 is the re-check block for a later revision.

**Binding snapshot.** `2026-10-19T04:08:28Z` (UTC). Lane HEAD
`139e3b662900557afe54f632b468619593dc9fcb` (== `claims.json:8`); working tree 3 rows
(`M LOG.md`, `?? REGIMEN.md`, `?? reports/round-33/`). All nine A01–A09 fragments and A10
were on disk; their digests at this instant are §4. A07 and A08 were revised *during* my
verification (A07 `dbf8deb3` → `6a2a1640`; A08 `b42c16e6` → `469ca910`); every line I cite
from them was re-read at the snapshot digests in §4, and both revisions agree on the
verdicts I compare.

**What this seat owns.** A *correspondence* check: for each of A10's nine rows — does the
fragment exist, does the fragment's own stated verdict match the row's verdict cell, and is
the row's evidence drawn from the fragment rather than from A10's own re-runs? It is **not**
an independent re-run of the cited commands: A11 (A01–A03), A12 (A04–A06) and A13 (A07–A09)
own that (`targets.json:58-60`). I ran a bounded corroboration set of my own (§3) because
several of A10's rows carried claims that no fragment supported when first filed; each run is
labelled as mine, not as verification of a fragment.

## 1. Row-for-row table (A10 rev5, bound `df5e42de`)

| row | A10 rev5 verdict cell | fragment verdict (path:line, §4 digests) | match | notes |
|---|---|---|---|---|
| A01 | "GREEN — fragment-backed (`adj/A01-province.md`): 'Net: `PROVINCE.md` needs no edit at HEAD' (A01:154), all four sub-checks PASS" | `adj/A01-province.md:154` "**Net: `PROVINCE.md` needs no edit at HEAD.**"; `:33` "**Verdict: PASS**"; verdict table `:148-152` (four PASS + A01-5 named finding) | **yes** | A10 also adopts A01's precision correction (pre-round-5, not merely pre-round-8; `A01:37-48`). A01's own finding id **A01-5** is not named in rev5 (`grep -c 'A01-5'` → 0); its substance is carried as A10-F7. |
| A02 | "PASS with one named content finding — fragment-backed (`adj/A02-handoff.md:88-90`)" | `adj/A02-handoff.md:88` "**Adjacency verdict for the handoff boundary: PASS with one named content finding (§4).**"; A02-H1 at `:92-147` | **yes** | rev1 read "GREEN — zero findings" on the sample/`packet-v3-16` surfaces; rev5 adopts the fragment's current-pair determination (`declared-in-r6`) and A02-H1. |
| A03 | "PASS with one named finding — fragment-backed" | `adj/A03-scope.md:13` "**PASS at the final reading (2026-10-19T03:57:47Z) with one named finding.**"; A03-F1 `:74-147` | **yes** | A10's row additionally carries A10-F8 (empty `kotodama-shokunin/reports/round-29/defects/` tree) and A10-F12 (protected surface 1,905) — A10's own measurements, attributed to A10 in its text; both reproduce (§3 #9). |
| A04 | "Zero unfiled bleed — fragment-backed (`adj/A04-bleed.md:13-20`)" | `adj/A04-bleed.md:15` "**Zero unfiled bleed** on the scanned surfaces…"; §4 findings F-A04-1 `:126-148`, F-A04-2 `:150-158` | **yes** | The two fragment findings are carried under A10's own ids (A10-F7, A10-F6). |
| A05 | "PASS on all six sub-checks — fragment-backed" | `adj/A05-corpus.md` A05-1 `:19` (verdict `:34` PASS), A05-2 `:46` (`:60` CONFIRMED), A05-3 `:83` (`:140` PASS), A05-4 `:146` (`:167` PASS), A05-5 `:175` (`:186` PASS), A05-6 `:189` (`:206` PASS) | **yes** | A05-6 explicitly closes A01's stale-prose item (`corpus/README.md:95` = revision 1.4 block), which is the "prose observation resolved" element of A10's row. |
| A06 | "RESTATED — ROUTED, NOT ABSORBED; one stale-pointer finding — fragment-backed" | `adj/A06-contested.md:22` "**CONTESTED-SCOPE POSTURE RESTATED — ROUTED, NOT ABSORBED.**"; verdict `:99`; §4 stale-pointer finding `:149-…` | **yes** | The stale-pointer finding (superseded contract digest `50c4c2f2…` on lane-owned example surfaces) is carried by A10 (3 references to `50c4c2f2`). |
| A07 | "9 of 11 filed verdicts hold exactly; 2 partially superseded — fragment-backed" | `adj/A07-history.md:27` "Net: **9 of 11 filed verdicts hold exactly at HEAD; 2 are partially superseded, both by later filed rounds, neither by drift.**"; D1 `:29-33`, D2 `:35-58`, F1 `:60-72`, F2 `:74-…` | **verdict yes; the same row carries two refuted citation defects** | See §2 F2 (packet-digest identity claim) and §2 F3 (r29 pointer off by one) — both are in this row's evidence cells and are unfixed at rev5. |
| A08 | "GREEN (partial by construction) — zero un-negated verdict language on the fragments present; full-set scan owed" — **no `fragment-backed` tag**; evidence is A10's own 03:56Z scan plus A13's | `adj/A08-language.md:7` "**Clean at the frozen snapshot.** Zero un-negated, un-routed, uncited promotion / canon / closure / verification claims in the 57/64 seat fragments present at 2026-10-19T04:06:54Z"; class totals `:75-83`; Owed `:441-…` | **substance yes; not fragment-backed** | The only row of the nine with no fragment-backed tag. A10's row cites neither `A08-language.md` nor its coverage (57/64), its 2,371 pass-1 occurrences or its 9 adjudicated residuals. Flag **F1**. |
| A09 | "GREEN on the frozen surface; three named non-frozen exposures — fragment-backed" | `adj/A09-pins.md:23-27` "**Verdict:** **GREEN on the frozen surface; three named non-frozen exposures with owners.** No frozen manifest row or baseline needs a re-pin"; findings A09-F1..F5 `:122-126` | **yes** | rev1's "zero digest-pin exposure; no re-pin owed" was refuted by A13 (`A13-verify-a07-a09.md:89-161`) and by the fragment; corrected from rev2 (A10-F10). |

**Count:** 8 of 9 rows fragment-backed and verdict-consistent; 1 row (A08) verdict-compatible
but not yet fragment-backed.

## 2. Flags

**F1 — row A08 is not backed by a fragment at the bound digest (reconciliation owed).**
A10 rev5's A08 cell and evidence cite only A10's own 03:56Z scan and A13's partial scan. The
fragment `adj/A08-language.md` (snapshot digest `469ca910`, 52,723 B) landed after rev5's
write (01:04:05 local) and now carries the fuller scan: 57/64 seat out-paths, 60 files,
2,371 pass-1 term occurrences (943 negation / 129 routed / 1,190 mention / 100 cited),
9 residual rows all hand-adjudicated, **0 genuine violations**, and its own owed full-wave
re-run (`A08-language.md:7,75-83,441`). The two agree in substance and both call themselves
partial by construction, so this is a *reconciliation gap, not a contradiction*: the
integrator should re-point the A08 row's evidence at the fragment and keep A08's own owed
re-run. Until then the row's verdict is not backed by a fragment, which is precisely the
condition this seat was sent to flag. A10 states the same of itself in its revision-3 note:
"fragment-backed** (A01, A02, A03, A04, A05, A06, A07, A09); **A08 alone remains"
(`A10-receipt.md:12`).

**F2 — row A07's packet-digest identity claim is refuted by the filed bytes (unfixed at rev5).**
A10 rev5 states: live `packet sha256 6ced88ad…` — "identical to the r21 filed receipt
(`reports/round-21/adjacency/A11-A12-handoff.md:41`)". My own commands at the snapshot:

- `sed -n '41p' reports/round-21/adjacency/A11-A12-handoff.md` → the **counts line only**
  (`16/16` fields, `20/20` glossary, `0` findings, `105/105` links, `27` claims, `16/7/4`) —
  **no digest appears on that line**.
- r21's filed digest is `e92f5e6775b657c24fa6260e340e4e7a04cf6c3777188cba80678bed079ae43b`,
  at `reports/round-21/adjacency/ledger.json:81` (also `reports/round-21/validation.json:1640`).
- live `sha256sum reports/round-30/handoff/declared-in-r6/packet.md` → `6ced88ad009f1cfc…`.

So the **counts** reproduce and the **digest does not**. The identity claim must be corrected
to "counts identical; packet digest drifted (the packet is regenerated)". A13 filed the same
defect independently (`A13-verify-a07-a09.md:209-224`). Verdict unaffected; evidence cell is
false as written.

**F3 — the r29 pointer is off by one (unfixed at rev5).** A10 rev5 cites
`reports/round-29/adjacency/province-entries.md:14` three times (row A07 and A10-F2). The
three-file digest triple A10 is matching against is on **:15** —
`grep -n 'be3a9477' reports/round-29/adjacency/province-entries.md` → `15:`. A13 recorded the
same off-by-one, and A07's own fragment cites `:15` (`A07-history.md:35`, `:81`). Pointer
only; the underlying measurement (AGENTS.md live `1afaf106…` ≠ r29 filed `be3a9477…`) is
correct and I reproduced it (§3 #5).

**F4 — superseded revision-1 claims (closed; recorded so the integrator binds rev5, not rev1).**
- rev1 row A09 ("GREEN — zero digest-pin exposure; no re-pin owed") was refuted by
  `A13-verify-a07-a09.md:89-161` and by `adj/A09-pins.md:23-27`; corrected from rev2 (A10-F10).
- rev1 A10-F3 ("the c31 audit exits 0 while reporting failures") was contradicted by
  `A13-verify-a07-a09.md:125-128`, by `A12-verify-a04-a06.md:163-175` (A12-DEF-02) and by my
  own run (§3 #6); A10 retracted it in rev2 with the pipeline-exit-status cause. **My run
  confirms the retraction; it did not discover it.**
Neither claim survives in rev5. No propagation owed.

**F5 — finding-id coverage (note, no action).** rev5 references A02-H1 (4 hits), A03-F1 (5),
F-A04-1 (4), F-A04-2 (3), `50c4c2f2` (3), A07's `orphan` (1) and `A29-ADJ-EVID-01` (2),
A09-F2 (1), A09-F3 (1). The only fragment finding id absent by name is A01's **A01-5**
(0 hits), whose substance is carried as A10-F7 (the transient in-place rewrite of
`reports/round-5/validation.json` and `reports/round-7/validation.json`).

**F6 — A10's rows carry A10's own measurements alongside fragment elements (no defect).**
Examples: A10-F8 (empty `kotodama-shokunin/reports/round-29/defects/` tree), A10-F12
(protected surface 1,905 = 1,770 + 135), A10's 1,905/2,655 labelling caution. Each is
attributed to A10 in its own text and reproduces (§3 #2, #9), so they do not make a row
unbacked — but they are not fragment elements and should not be cited as if they were.

## 3. My independent corroboration (bounded; not a substitute for A11–A13)

All commands at the lane root on 2026-10-19 between 03:52Z and 04:08Z, read-only, with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

| # | command | result | supports |
|---|---|---|---|
| 1 | `git log --oneline -3 -- PROVINCE.md`; `git rev-parse HEAD:PROVINCE.md`; `sha256sum PROVINCE.md`; `git rev-list --count c53782a..HEAD`; `wc -l -c PROVINCE.md` | `c53782a`; `313b182f251564b7997b06996b4f063370778f11`; `05b34a579c5d4f4e…`; **79**; 31 lines / 1636 bytes | rows A01/A07, A10-F2 |
| 2 | `git ls-files \| wc -l` | **2655** | row A03 |
| 3 | `python3 tools/gates/handoff-packet-check.py examples/handoff-packet.sample.md`; `… reports/round-20/handoff/packet-v3-16.md`; `… reports/round-30/handoff/declared-in-r6/packet.md` | each: `INFO scan: fields=16/16 glossary-entries=20 findings=0`, exit **0** | row A02 (current pair `declared-in-r6` green in my own run) |
| 4 | `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` | `summary: 20/20 legs passed`, exit 0; r21 filed `19/19` (`reports/round-21/adjacency/A11-A12-handoff.md:46`) | A10-F1 |
| 5 | `sha256sum AGENTS.md`; `grep -n 'be3a9477' reports/round-29/adjacency/province-entries.md` | `1afaf106f20b440a…`; r29 filed value at **:15** | A10-F2, and F3's pointer |
| 6 | `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` | exit **1**; `FAIL C31_index_rows_eq_files`, `FAIL C34b_prose_arithmetic`, `findings: 2`; source `:460` = `return 0 if not res["findings"] else 1`; a piped invocation (`\| head`) returns 0 — the rev1 instrument error | A10-F3 retraction |
| 7 | `sha256sum SKILL.md corpus/lessons/README.md`; `grep -rl` each digest under `tools/gates/frozen/`; `grep -rl 'lessons/README' tools/gates/frozen/` | `79fe91d3…`, `ec7469da…`; **0** files; **0** files | row A09 |
| 8 | per-partition `find corpus/knowledge/<p> -name '*.md' \| wc -l` | 94 / 18 / 21 / 19 / 29 / 20 = **201** | row A05 |
| 9 | `git ls-files 'reports/round-*' \| grep -cE 'round-(8\|9\|[12][0-9]\|3[0-2])/'`; same for `tools/gates/frozen/round-*` | **1770** + **135** = **1905** | A10-F12 |
| 10 | `sed -n '3,12p;95p' corpus/README.md` | current revision **1.9** (footer `201` / `21/19/18/29/20/94`); line 95 is the **revision 1.4** historical block | row A05's "prose observation resolved" |
| 11 | `grep -rn '50c4c2f2' examples/`; `sha256sum corpus/knowledge/synthesis/worldbible-integration-contract.md` | 5 hits (`examples/handoff-packet.sample.md:21`, `examples/handoff-packet.sample.yml:45,78`, `examples/culture-d3/handoff.md:27,74`; plus a README echo at `examples/culture-d3/README.md:104`); live contract `5f4c02bf…` | row A06's stale-pointer finding |
| 12 | `git status --porcelain` sampled 04:0xZ; `stat -c '%y' reports/round-{5,7}/validation.json`; live `sha256sum` vs `git show HEAD:<path>` | round-5/7 receipts showed `M` with mtimes `00:54:32.592` / `00:54:18.608`, then both **byte-identical to HEAD** (mtime `00:55:27.940`) | A10-F7 / A03-F1 / F-A04-1 (see §6) |

## 4. Fragment digests at the binding snapshot (2026-10-19T04:08:28Z)

| fragment | bytes | sha256 (8) |
|---|---:|---|
| `adj/A01-province.md` | 13,684 | `e22f2d03` |
| `adj/A02-handoff.md` | 17,040 | `41c3a749` |
| `adj/A03-scope.md` | 16,009 | `bf653d23` |
| `adj/A04-bleed.md` | 14,219 | `c7156e55` |
| `adj/A05-corpus.md` | 22,349 | `a1d8a255` |
| `adj/A06-contested.md` | 22,536 | `21b6099f` |
| `adj/A07-history.md` | 21,829 | `6a2a1640` |
| `adj/A08-language.md` | 52,723 | `469ca910` |
| `adj/A09-pins.md` | 24,703 | `98e3502e` |
| `adj/A10-receipt.md` (bound) | 36,683 | `df5e42de` |

These are read-instant digests, not final pins; A07 and A08 in particular were still moving
(`dbf8deb3` and `b42c16e6` respectively earlier in the same verification). **A11
(`adj/A11-verify-a01-a03.md`) was not on disk at the snapshot**, so the independent re-run of
A01–A03's commands remains owed to that seat (A12 covers A04–A06, A13 covers A07–A09).

## 5. Re-check block (for a later A10 revision)

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
sha256sum reports/round-33/adj/A10-receipt.md                       # df5e42de… = the verified revision
grep -c 'fragment-backed' reports/round-33/adj/A10-receipt.md       # 9 hits at rev5 = 8 row tags + A10's own rev-3 note; A08's row is the untagged one
grep -c 'identical to the r21 filed receipt' reports/round-33/adj/A10-receipt.md   # 1 = F2 unfixed
grep -o 'province-entries.md:1[45]' reports/round-33/adj/A10-receipt.md | sort | uniq -c   # F3
sed -n '41p' reports/round-21/adjacency/A11-A12-handoff.md          # counts only, no digest
grep -n 'e92f5e67' reports/round-21/adjacency/ledger.json           # r21's filed digest
python3 -B reports/round-25/audit/c31-lessons-index-audit.py >/dev/null 2>&1; echo c31_exit=$?   # 1
```

## 6. Scope observation I owe the record (filed-byte mutation, independently corroborated)

Independent of any fragment, my own sampling saw `reports/round-5/validation.json` and
`reports/round-7/validation.json` modified in the worktree (`M`) during the wave and restored
to their committed bytes minutes later (§3 #12). My round-5 mtime reading (`00:54:32.592`) is
later than the one A01 recorded (`00:54:15.802`), so round-5 was written **at least twice**
before the restore. Mechanism and probable writer are filed by A03-F1
(`adj/A03-scope.md:74-147`; probable writer **C05**, `to-verify`) and F-A04-1
(`adj/A04-bleed.md:126-148`: both runners write their own receipt in place —
`reports/round-5/run-validation.py:194`, `reports/round-7/run-validation.py:1171`). Current
state is clean; this is a carried finding for A03/X02 and the integrator, not a live defect.
I wrote nothing outside this fragment.

## 7. What this verification does not establish

- It does not re-run A10's commands (A11–A13 own that), does not re-run A01–A09's commands,
  and does not verify any fragment's content against its sources.
- It binds A10 at `df5e42de` and the fragments at §4's digests; any later revision invalidates
  the match and needs §5 re-run. A10's own rows for A08 remain provisional by its own F4/F5.
- It is not round acceptance, an axis verdict, or a promotion/canon/closure statement
  (`claims.json:68`).

## Owed: none

Nothing is owed from this seat: all nine A01–A09 fragments and A10 were present at the binding
snapshot, and the row-for-row match is complete. Two items belong to others and are flagged
above: **F1** (A10 row A08 reconciliation, integrator) and the **A11** fragment (A01–A03
independent re-run, that seat).

## Citations

- `reports/round-33/adj/A10-receipt.md` (bound `df5e42de`, rev5) — rows A01–A09 (`:49-57`), revision-3 note (`:12`), findings A10-F1..A10-F16 (`:57-…`).
- `reports/round-33/adj/A01-province.md:33,37-48,148-154` (`e22f2d03`).
- `reports/round-33/adj/A02-handoff.md:88,92-147` (`41c3a749`).
- `reports/round-33/adj/A03-scope.md:13,74-147` (`bf653d23`).
- `reports/round-33/adj/A04-bleed.md:13-20,124-158` (`c7156e55`).
- `reports/round-33/adj/A05-corpus.md:19,34,46,60,83,140,146,167,175,186,189,206` (`a1d8a255`).
- `reports/round-33/adj/A06-contested.md:22,99,149-…` (`21b6099f`).
- `reports/round-33/adj/A07-history.md:27,29-33,35-58,60-72,74-…,81` (`6a2a1640`).
- `reports/round-33/adj/A08-language.md:7,75-83,441-…` (`469ca910`).
- `reports/round-33/adj/A09-pins.md:23-27,122-126` (`98e3502e`).
- `reports/round-33/adj/A12-verify-a04-a06.md:163-175` (A12-DEF-02, A10-F3 contradiction).
- `reports/round-33/adj/A13-verify-a07-a09.md:31-44,89-161,125-128,209-224`.
- `reports/round-33/claims.json:8,18,29,33,59,68`; `reports/round-33/targets.json:10,51-61`.
- `reports/round-21/adjacency/A11-A12-handoff.md:41,46`; `reports/round-21/adjacency/ledger.json:81`; `reports/round-21/adjacency/province.md:17`; `reports/round-21/validation.json:1640`.
- `reports/round-29/adjacency/province-entries.md:15`.
- `reports/round-25/audit/c31-lessons-index-audit.py:460`; `reports/round-25/validation.json` (`input_sha256`).
- `reports/round-26/run-validation.py:97,1494-1500`; `reports/round-5/run-validation.py:194`; `reports/round-7/run-validation.py:1171`.
- `corpus/README.md:3-12,95`; `corpus/knowledge/synthesis/worldbible-integration-contract.md` (live `5f4c02bf…`).
- `examples/handoff-packet.sample.md:21`; `examples/handoff-packet.sample.yml:45,78`; `examples/culture-d3/handoff.md:27,74`; `examples/culture-d3/README.md:104`.
- Commands: `sha256sum`/`stat` over the ten artifacts (snapshot 2026-10-19T04:08:28Z); `git log --oneline -3 -- PROVINCE.md`; `git rev-parse HEAD:PROVINCE.md`; `git rev-list --count c53782a..HEAD`; `wc -l -c PROVINCE.md`; `git ls-files | wc -l`; `git status --porcelain`; `python3 tools/gates/handoff-packet-check.py` (three packets); `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`; `python3 -B reports/round-25/audit/c31-lessons-index-audit.py`; `find corpus/knowledge/<partition> -name '*.md' | wc -l`; `grep -rn '50c4c2f2' examples/`; `grep -rl` digest/path scans under `tools/gates/frozen/`; `sed -n` reads of the fragments and filed receipts cited above.
