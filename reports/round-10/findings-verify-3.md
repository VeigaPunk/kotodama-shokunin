# R10-O12 — verifier: O06 (idx 4, 12) and O07 (idx 5, 13)

- seat: **R10-O12** (findings verifier), round 10 (loop 1 of 3, build round 3 of 4), 2026-10-17
- assignment (verbatim): "FINDINGS R10-O12 (verifier): O06+O07. reports/round-10/findings-verify-3.md."
- write scope: **this file only**. No tracker row, fixer fragment, tool, pin, packet, corpus or SCORECARD byte was written by this seat. Scratch: in-lane `.scratch/r10o12/` (`export TMPDIR=$PWD/.scratch` before every scratch-writing command; `/tmp` never used). No commit made.
- worktree at verification: HEAD `e3a1ec9435787328ac9f828f96cb6390e4916b8f` + concurrent round-10 worker edits (`M SKILL.md`, `M corpus/README.md`, `M reports/round-8/run-validation.py`, `M reports/round-9/validation.json`, untracked round-10 fragments/corpus entries); verification window 21:26Z–21:42Z.
- method: read both fixer fragments, then **re-ran every control they cite** on the live tree and re-measured every digest/token/fixture independently (no fragment value accepted by quotation). Where a fixer's number and mine disagreed I report the disagreement rather than smoothing it.
- canon: NON-CANON engineering evidence. Nothing here adjudicates canon, real-world rights, or game mechanics.

## 0. Rows verified, and how the seat→row mapping was established

| fixer | fragment | tracker rows verified |
|---|---|---|
| R10-O06 | `reports/round-10/fix-06.md` | **idx 4** = R8-D16 S6 (supplied `native_form` not read) · **idx 12** = R9-D09 S4 (freeze unpinned by construction) |
| R10-O07 | `reports/round-10/fix-07.md` | **idx 5** = R8-D16 S10 (rank coverage ratio) · **idx 13** = R9-D09 S5 (`--selftest` outside exit-2 envelope) |

The mapping formula `O(2+j) → idx j, j+8` (0-based) is the one already established by the sibling
verifier (`reports/round-10/findings-verify-2.md` §0) and is stated in both fragments' own headers
(`fix-06.md:8` "rows fixed here: idx 4 … and idx 12 …"; `fix-07.md:9` "tracker idx 5 … and idx 13").

Tracker state at verification close (`reports/round-10/findings-tracker.json`, sha256
`151217d7fd98965f8f7225de5c91d4b100e89eea3aa2289e8fb0de10b0dcb5ff`):

- rows **5** and **13** are merged (`disposition: fixed-with-control`, `disposition_by: R10-O07`);
- rows **4** and **12** are still `disposition: pending` — O06's §3 patch payload is ready in its
  fragment and awaits the scribe (R10-O14); see §3.

## 1. O06 — `reports/round-10/fix-06.md`

### 1.1 idx 4 (R8-D16 S6) — disposition claimed `wrong`: **VERIFIED, controls A–D reproduced**

Claim: the D16 observation reproduces but the defect claim and its premise are wrong — the spec
never declares a record-level `native_form` channel; the declared typed-label channel is read and
enforces R1/R3/R4 + L2, live at the delivered revision **and at the reviewer's own newest-tested
`e9209f28`**.

| # | O06 claim | my independent re-run (2026-10-17) | verdict |
|---|---|---|---|
| 1 | spec bytes unchanged since review: `84e4b4c1…` = D16's pin = `e1694ba` = live | `sha256sum reports/round-8/depth/design-spec.md` → `84e4b4c19b03…4cc751`; `git show e1694ba:…` → same; `findings.md:7` pins the same value | match |
| 2 | §1.5 states GAR records carry "no `native_form`" | `design-spec.md:231` (sed 229–233): "Every GAR record carries an English `garment` string, a `form_slot` (LEX-GAR-01..10), and no `native_form`" | match |
| 3 | the channel existed at `e9209f28`: `typed_labels` pass-through at `:594-598` | reviewer mirror `/home/vgpnk/.r8d16/mirror3/tools/d2-typed-labels.py` sha256 `e9209f28…f4a282`; `grep typed_labels` → `:594-598` present; `mirror2` (`623b5b1f`) → **0** occurrences | match |
| 4 | Control A — field injection: byte-identical finding set to baseline | re-ran on `.scratch/fix06/packet-A-field.yml` (sha `c2754899…2785ba`): exit 1, `stats {fail:0, hold:15, labels:58, note:1}`; diff vs captured `out-current-A-field.json` = packet-path line only | match |
| 5 | Control B — declared channel: `labels 59`, `fail 2`, `D2L-NATIVE` FAIL ×2 on `TL-GAR-01`, GAR-01 hold gone | re-ran on `packet-B-label.yml` (sha `b4c59346…5e02a8`): exactly that; `D2L-NATIVE: supplied form 'vinter' carries symbols outside the declared inventory: ['v']` ×2; no GAR-01 hold | match |
| 6 | Control C — same on the reviewer's own `e9209f28` file | re-ran `.scratch/fix06/oldrun/tools/d2-typed-labels.py` (sha = `e9209f28…f4a282`): `labels 59`, `fail 2`, identical `D2L-NATIVE` ×2, GAR-01 hold gone | match |
| 7 | Control D — §1.2 L2: two supplied forms → exit 2, `D2L-DATA` | re-ran on `packet-D-two.yml` (sha `75248eb2…a04ccb`): exit 2, `D2L-DATA — two supplied sound forms on one record (11-costumes LEX-GAR-01): identity collision` | match |
| 8 | selftest 39/39 | my run: `39/39 checks passed`, exit 0 | match |

**Disposition judgment.** `wrong` is the correct shape, with the nuance the fixer itself states:
the *observation* reproduces (Control A) and is correct behavior — the injected record-level
`native_form` is an undeclared field per the spec's own bytes, which D16 itself pinned; and the
capability's declared input path (a supplied typed-label record) was already read and enforced at
the reviewer's newest-tested revision (Control C), so the finding's premise ("the only native-form
sources are the lexicon and the unresolved form slots" / the spec "assume[s] the tool reads a
supplied `native_form` [record field]") is contradicted by the artifacts. The design question D16
explicitly left open (`findings.md:133`) remains open and is not adjudicated here.

### 1.2 idx 12 (R9-D09 S4) — disposition claimed `fixed-with-control`: **VERIFIED**

Claim: the actionable recommendation (ledger/admission carries the freeze's sha256 pre/post re-pin)
is implemented; the in-tool self-exclusion gap remains by design (the source row itself says
"documented design, residual only").

| # | O06 claim | my independent re-run (2026-10-17) | verdict |
|---|---|---|---|
| 1 | pre anchor in the D12 ledger: `scribe.md:208-216` carries `74496aa8…` + the verbatim "This ledger carries the pre-refresh anchor (D09 S4 requests exactly that); the post-refresh `expected.json` sha256 must be recorded at admission." | `sed -n '208,216p'` confirms both the token and the sentence verbatim | match |
| 2 | post anchor in the admission record: `validation.json:24` (`claims.D.measurement.expected_sha256`) and `:991` (`input_sha256[…]`) = `562b76cb…90fc` | both lines confirmed; `git log --oneline -1 -- examples/culture-d3/expected.json` → `9dc18ec` | match |
| 3 | bracket assertion `recorded == input == live` prints True | my run: `True`; `git show 57c3ce6:examples/culture-d3/expected.json \| sha256sum` → `74496aa8…d5080`; live → `562b76cb…f90fc` | match |
| 4 | frozen leg green at the recorded pair | `check-evidence-coupling.py … --frozen …` → exit 0, `counts.total 0`, `findings []` | match |

**Disposition judgment.** Accept. The recommendation was the actionable part of a row the source
itself labels "documented design, residual only"; the pre/post pair now lives in durable records
bracketing the live bytes, asserted by command, and the frozen replay is green at the recorded
value. No in-tool witness of an in-place `expected.json` edit can exist without breaking the
freeze's own design — that residual is correctly left documented.

## 2. O07 — `reports/round-10/fix-07.md`

### 2.1 idx 5 (R8-D16 S10) — disposition claimed `fixed-with-control`: **VERIFIED (control reproduced; landing deferred — caveat below)**

| # | O07 claim | my independent re-run (2026-10-17) | verdict |
|---|---|---|---|
| 1 | control `check_s10.py SCORECARD.md SCORECARD.patched.md` → FAIL on filed, PASS on patched | re-ran verbatim: identical output (FAIL: ratio `5/21` absent + 4 counts absent; PASS), exit 0 | match |
| 2 | ratio absent from SCORECARD: `grep -c '5/21'` → 0; capability row silent; the adjective survives only at `:182` (historical declaration) | `grep -c` → 0; `sed -n 128p` → row carries no rank coverage; `grep -n rank` → `:182` only | match |
| 3 | patch = 1-line row replacement at `SCORECARD.md:128` (+ratio and 4 counts) | `diff` filed vs patched = 1 changed line (4 diff lines); patched row: "…emits typed projection; rank-rule adapter coverage 5/21 records gate-projected (9/21 normalized, 13 unresolved items, 3 quarantine handles) — not full rank semantics…" | match |
| 4 | ratio grounded in the live build (`21/5/9/13/3`, 4 × `D2L-RANK`) | my own live emit (`.scratch/r10o12/live.yml`): `coverage` `{rank_rules_component: 21, rank_rules_gate_projected: 5, rank_rules_normalized: 9, rank_rules_unresolved_items: 13, rank_quarantine_handles: 3}`, 4 × `D2L-RANK`; committed artifact `:40-44` carries the same numbers | match |

**Caveat (not a defect in the control).** This is a *verified patch + demonstrated control*, not a
landed fix: the tracker row's own `residual` says "row patch not applied by this shard (SCORECARD.md
outside the assigned write scope); fix-07.md §1.3 replacement is ready for the integration step."
Verified as stated; whether the O acceptance requires the row landed (vs a ready, verified patch)
is the orchestrator's/scribe's call — the disposition is honest about it.

### 2.2 idx 13 (R9-D09 S5) — disposition claimed `fixed-with-control`: **VERIFIED (landing deferred with a verified reason)**

| # | O07 claim | my independent re-run (2026-10-17) | verdict |
|---|---|---|---|
| 1 | `probe_s5.py`: fail-before = OSError escapes `main()`, 4-frame traceback, empty stderr; pass-after = `rc=2` + `selftest error: [Errno 28] …` | re-ran verbatim: identical output (`filed assembler sha256: ba8d19d5…`, both verdict lines) | match |
| 2 | filed assembler = HEAD bytes `ba8d19d5…` | `sha256sum tools/assemble-culture-d3.py` = `ba8d19d5855fe670e5a828f0aca8133fb2cbf54ee865927917c9f20d5d17f014` = `git show HEAD:…` | match |
| 3 | no regression, filed bytes: `--selftest` 85/85, `--check` byte-identical | re-ran: `85/85 checks passed` exit 0; "packet.json: byte-identical …; packet.gates.yml: byte-identical …" exit 0 | match |
| 4 | no regression, patched copy: same | re-ran in `.scratch/fix07/tree/`: `85/85` exit 0; byte-identical exit 0 (patched file sha `a18371dd…93ff5`) | match |
| 5 | landing blocker: pin == live; landing the patch turns the green frozen replay red with exactly 1 × `D3-SNAPSHOT` | `pin == live: True`; patched tree frozen run → exit 2, `counts {D3-SNAPSHOT: 1, total: 1}` — "declared `ba8d19d5…`, actual `a18371dd…`", no collateral mismatch | match |

**Caveat (same class as §2.1).** The patch is verified but deliberately not landed; the row's
`residual` carries the freeze-pin reason, and my re-run confirms the reason's premise (exactly one
new mismatch, only the patched file; `--check` byte-identical so a re-pin would move one digest
with no D3 verdict change). A re-pin record per R9-D09 S1 is the orchestrator's act.

## 3. Cross-cutting notes (observed, not adjudicated)

1. **Tracker merge state.** Rows 5/13 are merged (O07 wrote them under `flock`, tracker sha
   `151217d7…`); rows 4/12 remain `pending` with O06's §3 patch payload ready. If the scribe does
   not merge them, claim O's zero-undispositioned check fails on rows 4/12 even though both fixes
   are verified here. O06 cites `AGENTS.md` ("workers never race to append shared bookkeeping") for
   not merging; either way the merge is a required, outstanding step at verification close.
2. **Filed-byte edit adjacent to idx 13/idx 9.** `reports/round-8/run-validation.py` is modified in
   the worktree (48+/14−, `replay_isolated` pin repair via `gate_blob_for_pin`). It is claimed by a
   drift worker (`reports/round-10/drift/fix-20.md` §"Fix applied (in place, …)"), and O03's
   fragment records it as a peer edit while stating the no-rewrite rule for itself. The lane rule
   "never rewrite filed report bytes — corrections are new entries" (F15–F18 scope) and the
   documented in-place repair are for the scribe/auditor to reconcile; not adjudicated here.
3. **O06 adjacent A1 verified by me**: `examples/culture-d3/README.md:34,91` and
   `handoff.md:65,242,278` still print the pre-re-pin token `74496aa8…` while the live freeze is
   `562b76cb…`; both files last touched by `57c3ce6` — a real documentation drift outside every
   tracker row (the docs are freeze-excluded, so the guard never sees it).
4. **O06 adjacent A2 verified by me**: `python3 tools/d2-typed-labels.py --check` exits 1
   (committed artifact pins `packet_sha256 8da90b07…`; live packet `e0f21509…`), pre-existing at
   `e1694ba`; independently diagnosed by round-9 `d3/interop.md` §4 (validated repair, not applied).
5. **O06 adjacent A3 seen in my re-runs**: Control B/D outputs emit `D2L-NATIVE` twice for
   `TL-GAR-01` with identical detail (count inflation only when the channel is used).

## 4. Limits

- Re-runs used the fixers' own scratch fixtures (packet copies, patched trees) where those are the
  control's subject; each fixture's sha256 was re-measured and matches the fragment. I did not
  re-derive the packet mutations from scratch.
- The `3548185c` revision is unavailable to me too (worktree stamp; no git object, no mirror);
  Control C substitutes `e9209f28`, the reviewer's own newest-tested revision — agreement with
  O06's own limit.
- `probe_s5.py`'s monkeypatch measures the shipped `main()` structure, not a real ENOSPC event
  (method limit disclosed by the fixer and by R9-D09).
- This verification does not adjudicate the six resolved-at-source rows (18–23), the drift-ledger
  claims, or any canon/rights/game-mechanics question.

## 5. Receipts (all 2026-10-17, lane root; scratch `.scratch/r10o12/`)

```sh
sha256sum reports/round-8/depth/design-spec.md            # 84e4b4c1…4cc751 (also git show e1694ba:…)
sed -n '229,233p' reports/round-8/depth/design-spec.md    # "…and no `native_form`"
sha256sum /home/vgpnk/.r8d16/mirror3/tools/d2-typed-labels.py   # e9209f28…f4a282
python3 tools/d2-typed-labels.py --packet .scratch/fix06/packet-A-field.yml --json   # == baseline
python3 tools/d2-typed-labels.py --packet .scratch/fix06/packet-B-label.yml --json   # 59 labels, 2 fail
python3 .scratch/fix06/oldrun/tools/d2-typed-labels.py --packet …/packet-B-label.yml --json  # same
python3 tools/d2-typed-labels.py --packet .scratch/fix06/packet-D-two.yml --json     # exit 2, D2L-DATA
git show 57c3ce6:examples/culture-d3/expected.json | sha256sum                       # 74496aa8…
python3 -c "…recorded==input==live…"                                                 # True
python3 .scratch/fix07/check_s10.py SCORECARD.md .scratch/fix07/SCORECARD.patched.md # FAIL then PASS
python3 .scratch/fix07/probe_s5.py                                                   # fail-before + pass-after
(cd .scratch/fix07/tree && python3 tools/check-evidence-coupling.py examples/culture-d3/packet.json --frozen examples/culture-d3/expected.json)  # 1 × D3-SNAPSHOT
sha256sum reports/round-10/findings-tracker.json          # 151217d7… (rows 5/13 merged; 4/12 pending)
```

Captured by this seat: `.scratch/r10o12/A.json`, `B.json`, `C.json`, `D.json`, `live.yml`.

FILES: reports/round-10/findings-verify-3.md | SUMMARY: Verified O06 (idx 4 = R8-D16 S6, disposition `wrong` — controls A–D reproduced: the injected record-level `native_form` is an undeclared field per the spec's own pinned bytes, while the declared typed-label channel fires `D2L-NATIVE` at both the delivered revision and the reviewer's own newest-tested `e9209f28`; idx 12 = R9-D09 S4, `fixed-with-control` — pre token `74496aa8` in the round-9 ledger, post token `562b76cb` in the admit record, `recorded==input==live` True, frozen replay green) and O07 (idx 5 = R8-D16 S10 and idx 13 = R9-D09 S5, both `fixed-with-control` — every cited control re-ran identical: FAIL→PASS ratio check on the SCORECARD row patch, traceback→exit-2 on the assembler patch, filed/patched no-regression 85/85 + byte-identical, and the 1 × `D3-SNAPSHOT` landing-blocker demonstration reproduced; both O07 fixes are verified patches with landing explicitly deferred in the tracker residuals), with the caveat that tracker rows 4/12 remain `pending` for the scribe's merge and the filed `reports/round-8/run-validation.py` in-place repair is flagged for the scribe/auditor.
