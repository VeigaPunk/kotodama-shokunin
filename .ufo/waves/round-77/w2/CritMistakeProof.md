# CritMistakeProof — wave-2 falsification of `ScribeMistakes` + lesson `## Mistakes`

Seat: `CritMistakeProof` (critic, leaf — no subagents, no background jobs). Round 77 wave 2,
lane `kotodama-shokunin`, base `211f9526800906e0c585d878d265c37e5e090c15`. Attacked item:
`.ufo/waves/round-77/w1/ScribeMistakes.md` + `w1/stage/ScribeMistakes/mistakes.md`, and the
merged rows in `w1/drafts/corpus/lessons/round-77.md`. Writes: this file +
`w2/stage/CritMistakeProof/` only. Scratch `/fast/scratch/hyaku/kotodama-r77/CritMistakeProof`
deleted on yield. No installs; pacman not run.

**Verdict, one line:** ScribeMistakes' *defect claims* all re-verify against the named
receipts, but its "ten owed / two shown" tally is **stale**: the wave-1 counters execute the
exact red demonstrations its rows name as owed (I ran the r77 `LEDGER` predicate over the real
r76 ledger — red, exit 1, with the named problems). Three new counterexamples survive: (A)
`legcount.py` PASSes the convergent-bad r76 terminal pair — the actual r76 end-state is green
under the freeze-side gate; (B) `_doc_url_key` drops the whole query string, so two distinct
records differing only in `?hcno=` fold to one document — the draft's "query-aware record
keys" is not what the counter does; (C) the lesson's own tally is self-inconsistent (M15 says
"yes, demonstrated" while the same file's intro and §5 merge both say exactly two rows have an
executed red proof — M15's is the weakest kind).

Legend: **VERIFIED-R76** = defect re-confirmed on committed r76 bytes; **VERIFIED-FIXTURE** =
the new guard was observed red on a bad input and green on a clean input inside a W1 receipt;
**VERIFIED-REAL** = the new guard was executed by me on the real r76 artifact and produced the
named red; **OWED** = no red run of the fix exists; **MISCLASSIFIED** = the stated verdict is
wrong regardless of underlying evidence.

## Per-row classification

### ScribeMistakes rows R77-M1…M12

| row | defect verdict | fix verdict | evidence |
|---|---|---|---|
| M1 ROWS scope | VERIFIED-R76 (`controls-c.txt:30`/`measures-c-final-c28ea.txt:25` identical diagnostics; `accept-c.py:1588-1605` whole-file multiset diff vs frozen text "adds exactly S894-S896") | **VERIFIED-FIXTURE** (mistakes.md says `owed`) — `selftest-receipt.txt:12` `row-extra` → `FAIL legs=12/13` ROWS-only; `:23` `index-required-section` (required non-row lines removed) → ROWS stays green, INDEX-only red; `:15` `pre-row-rule2-cell` → PASS. Caveat: the *real* r76 landing can never be graded by ACCEPT-C-77 (`redbefore.txt`: refused — r76 freeze carries no `reports/round-77/claims.json`), so the demonstration is fixture-level by construction, not a defect | |
| M2 COLLCHECK | VERIFIED-R76 (`controls-c.txt:48`; `ExecMapAudit.md:60-61` showGb vs newGbInfo) | **VERIFIED-FIXTURE** + contract shift (says `owed`) — `collcheck-map-alias` → `FAIL legs=12/13` COLLCHECK-only; `collcheck-archive-identity` → PASS. **But the actual r76 red input is still red**: my probe shows `showGb` ≠ `newGbInfo` keys, so the map record must hold the *canonical* doc URL — a data obligation the draft phrase "query-aware record keys" misdescribes; the counter key is query-*ignoring*. Counterexample B below | |
| M3 freeze-over-red-control | VERIFIED-R76 (`controls-ca.txt:40` vs `:67`, re-run: 7× `LEG FAIL`; LEDGER red while expected PASS) | **OWED — accurate.** `ExecGapSweep/run-controls.sh` is a post-freeze harness (hard per-leg expectations, exit 1 on deviation — stronger than r76's prose expectation) but its receipts cannot gate the freeze itself (`README` admits the receipts "cannot be committed *in* the freeze commit"). No `manifest-check` leg compares control verdicts to expectations. The r77 freeze can still stand over a red `controls-ca.txt` | |
| M4 L76-13 allowlist | VERIFIED-R76 | **VERIFIED-REAL (this seat) — the "owed" is discharged.** `--ledger-check reports/round-76/ledger.json` → `LEDGER-CHECK-77: FAIL pairs=20 problems=24`, exit 1, including `L76-13: stated_at path corpus/knowledge/… is not in the frozen ANNOTATE allowlist` — the exact problem the row names | |
| M5 L76-19 stated_text | VERIFIED-R76 | **VERIFIED-REAL (this seat).** Same run; isolated L76-19 → `stated_text not found in corpus/lessons/round-75.md at base` (receipt `stage/…/ledger-check-l76-19-21.txt`) | |
| M6 unexecutable rederive | VERIFIED-R76 | **VERIFIED-REAL (this seat), with one diagnostic shift.** r77 `observe_problem` refuses all 19 git `observe_cmd`s (`git argv must open with -C <dir>`), and because `pair_problems` skips the exec block once `why` is set (`accept-ca.py:1724`), the r76 `chars=`/`98c486bd…` *path-operand* diagnostics never print on the real ledger — the class still reds (via `rederive … -C` refusal once observe_cmd is patched; `ledger-check-l76-rederive.txt`), but not with the r76 problem text. ScribeQuality30's checker *does* print operand codes (`receipt-r76-ledger.txt`: NO-C=19, REDERIVE-STRING=20) | |
| M7 uncommitted receipts | VERIFIED-R76 (corrected version: RECEIPTS red at F0 `freeze-ca-control-ledger-redbefore.txt:56`, R1EXEMPT red at `controls-ca.txt:52`) | **VERIFIED-FIXTURE** (`selftest-ca.txt:44` `uncommitted-receipt` → RECEIPTS=FAIL; `:45` `fixtures-absent` → R1EXEMPT=FAIL) — the class is covered; the exact "receipt absent at graded revision" shape is fixture-red, real-input unrun | |
| M8 COMBINED no line number | VERIFIED-R76 (`measures-ca.txt:13`) | **VERIFIED-FIXTURE** (`selftest-ca.txt:46` `readme-exemption-no-line` → COMBINED=FAIL, clean → PASS) — exactly the fixture the row asks for | |
| M9 map residue | VERIFIED-R76 (`ExecMapAudit.md:195-198`) | **OWED — and now confirmed against code, not just prose.** `accept-c.py:_map_pairs` (1617-1646) only indexes records for the *adopted* staged ids inside `leg_collcheck`; map entries for other staged ids (the r76 `S859`-absent class) are never iterated. `rowset-only-map-absent` selftest → PASS, so an absent/irrelevant map is green by design. The gap is real and correctly labeled | |
| M10 leg-list hygiene | VERIFIED-R76 (`accept-c.py:6381-6397` INDEX twice; refusal receipt `freeze-control-legcount-redbefore.txt` exit 2) | **VERIFIED-FIXTURE with a live residual.** r77 counter: `legcount-duplicate` selftest → `FAIL legs=0/13 (refused: LEGCOUNT … repeats INDEX)`, `--emit-legs` generates the list (LEGS tuple is single authority). **Counterexample A**: `legcount.py` — the freeze-side assert the row's fix "keeps" — prints `NOTE … PASS (order and set equal)` on the *actual* r76 terminal pair (claims.json dup INDEX ↔ accept-c.py dup INDEX; my re-run, exit 0). The guard that would have caught r76's end-state (convergent bad list) is the counter's own duplicate refusal, not `legcount.py`; the checklist should treat a frozen duplicate as FAIL even when both sides converge | |
| M11 in-place report rewrite | VERIFIED-R76 (fleet `1cd8e33c` numstat `1 1` on `.ufo/reports/round-76/kotodama.md`, diff shows the `--work` path string replaced inside the filed sentence) | **OWED — correctly labeled.** The proposed numstat-0 check is sound: applying it retroactively to `1cd8e33c` flags the r76 defect; an erratum-append prints `0` deletions. Uninstalled (proposed homes are outside all seats' write scope) | |
| M12 planner role + route map | VERIFIED — validator `SWARM_ROLES` (10, no `planner`) + `unknown_role` at `ufo-swarm-wave.mjs:988-989`; the executed probe (`probe-roles.txt`) is real | **Partially misread.** "Executed red-before" here means the *defect* (validator refusing `planner`), not a *fix* shown able to fail: the fix is a procedural note (L1 records the planner→§3 mapping), which has no guard. Also worth stating plainly: the r77 dispatch complied — `w2/spec.json` items carry no `planner` role, so the conformance outcome is verified, the "guard" framing is not | |

### ScribeLesson rows R77-M13…M16

| row | verdict | evidence |
|---|---|---|
| M13 staged row contradicts its capture | VERIFIED-R76 (S934 staged `Słon … Onomastica 68` vs capture serving Kałużyńska LXIX; corroborated by `receipt-05` and `ScribeQuality30`) | fix ("document-identity comparison per entry source") **partially exists**: `leg_repointed` (`accept-c.py:1256+`) requires each `source:` line's URL to name the cited row's document — the lane side — but nothing compares the *staged* row's document cell with its capture; `owed` is accurate |
| M14 D2 locator one page off + cut attribution | VERIFIED-R76-CLASS (phrase once, on PDF p.4/journal p.114; `d2-locator-sweep.txt` + `receipt-05` agree) | **the data fix landed** — current `CLAIMS-DRAFT.md` (sha256 `5f791d3a…`, 8768 B — a revision *after* ScribeLesson's `ac5aead4`, same content on this point) reads `journal p. 114 / PDF p. 4`, 17-word form, "reported from the cited 2008 work". Residual: no leg grades the locator; EVIDENCE only checks the quote sits in the committed window (`ExecAdaptC` finding 5 confirms) — a stale p.115 locator paired with a p.4-reaching window still passes. "Owed" accurate |
| M15 one status for two request shapes | VERIFIED in substance (22:22→22:33 correction recorded; probes: plain 403/browser 200) | **MISCLASSIFIED — "yes, demonstrated" is overstated.** The red bytes are *unrecoverable* (ScribeLesson's own note: untracked file overwritten); what is demonstrated is the corrected record and the per-UA probes — no guard can fail. The draft's own §5 says "only R77-M10 and R77-M12 have executed red proofs", contradicting this row in the same file |
| M16 entry rewrite uncontrolled | defect premise **STALE-FALSE** | `leg_repointed` exists: exactly one id per `source:` line, `removed_ids` refused, every cited id must resolve and its line URL must name the row's document — i.e. S903 (no lane row) and S886/S888–S891/S896 are all red under REPOINTED, fixture-proven (`repointed-legacy-id`, `repointed-source-no-url` selftests). The residual is integration, not absence: `removed_ids`/`staged_universe` must come from the frozen claim config, and REPOINTED reads `source:` fields — a bare inline `S###` citation outside a `source:` line is ungraded |

## Counterexamples (the strongest available)

**A — LEGCOUNT gate passes r76's actual end-state.** Command:

```
$ cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && python3 -B \
  .ufo/waves/round-77/w1/stage/ExecFreezeChecklist/legcount.py \
  --claim C --claims reports/round-76/claims.json --counter reports/round-76/accept-c.py
LEGCOUNT C: frozen (13): ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,CENSUS,INDEX,COLLCHECK,FROZENCFG,INDEX
LEGCOUNT C: counter (13): ENTRIES,ROWS,REPOINTED,GATE,EVIDENCE,REJECTS,GROUND,CITEDLINES,CENSUS,INDEX,COLLCHECK,FROZENCFG,INDEX
LEGCOUNT C: NOTE frozen lists 'INDEX' more than once (the counter's order decides the position)
LEGCOUNT C: PASS (order and set equal)      EXIT=0
```

`duplicates()` feeds a NOTE, and `frozen_table` only problems non-strings/missing `NAME:`/
non-UPPER_SNAKE (`legcount.py:154-207`). The r76 failure mode is precisely *convergent* (the
counter was edited to match the bad frozen list), so the "new guard" blesses it. `n5` (the
`LEDGELIST?` placeholder) fails for a different reason (name not UPPER_SNAKE), and the draft's
own clause — "LEGCOUNT compares distinct ordered names and refuses duplicates" — is therefore
only half-implemented on the freeze side. Fixable: hard-fail on `duplicates(frozen)` in
`legcount.py` (one-line change; `manifest-check.py` inherits).

**B — COLLCHECK folds different records to one document.** Command:

```
$ cd …/ExecAdaptC && python3 -B -c 'import importlib.util; m=…accept-c.py…;
  m._doc_url_key("…/newGbInfo?hcno=E107EA…")  → ("openstd.samr.gov.cn","/bzgk/std/newGbInfo")
  m._doc_url_key("…/newGbInfo?hcno=DEADBEEF") → identical key
  m._doc_url_key("…/newGbInfo")               → identical key
  m._doc_url_key("…/showGb?type=online&hcno=E107EA…") → ("/bzgk/std/showGb") ≠ row key
  m._doc_url_key("web.archive.org/web/20260424031027id_/…/newGbInfo?hcno=E107EA…") → row key'
```

`norm_url` keeps `(netloc, path)` only (`accept-c.py:222-226`); `?hcno=` is dropped. For this
registry host the record lives *in* the query: a frozen map naming `newGbInfo?hcno=DEADBEEF`
(a different GB record) against a row citing the true record is **green** under r77 COLLCHECK —
the mirror-image defect of r76's (over-separation then, under-separation now). The r77 sources
are unaffected (D1/D2 carry no discriminating query), so this is a fixable gap, not a kill.
Smallest correction: keep a host-config allowlist of query keys (`hcno` for openstd.samr.gov.cn)
inside `_doc_url_key`, or restrict the query-drop to `web.archive.org` wrappers and `id_` mods.

**C — ledger-check display cap hides the tail problems.** `--ledger-check` prints `problems[:20]`
(`accept-ca.py:3965`); on the real r76 ledger the count is 24 but the printed list stops at
L76-18 — L76-19/20/21's entries are invisible in the receipt, which a reader could misread as
"the check missed them". Cosmetic but report-affecting (this seat almost misread it).

## Evidence — commands and raw outputs (this seat's runs)

```
$ python3 -B .ufo/waves/round-77/w1/stage/ExecAdaptCa/accept-ca.py \
    --ledger-check reports/round-76/ledger.json --root . \
    --base 211f9526800906e0c585d878d265c37e5e090c15 --work <scratch>/lc
LEDGER-CHECK-77: FAIL pairs=20 problems=24                       COUNTER_EXIT=1
     round=76 != 77
     base='98c486bdb4650ba5b8e651d332910e8ee60ad121' != --base 211f952…
     L76-01..18×: observe_cmd git argv must open with `-C <dir>` … refused
     L76-13: stated_at path corpus/knowledge/… is not in the frozen ANNOTATE allowlist […]
     L76-16: stated_text not found in SKILL.md at base
   (receipt: w2/stage/CritMistakeProof/ledger-check-r76.txt — 21 lines, cap at 20 shown)

$ # isolated L76-19/20/21, meta retargeted to round 77 (scratch file):
LEDGER-CHECK-77: FAIL pairs=3 problems=5                         EXIT=1
     L76-19: observe_cmd … -C … refused
     L76-19: stated_text not found in corpus/lessons/round-75.md at base
     L76-20/21: observe_cmd … refused
   (receipt: ledger-check-l76-19-21.txt)

$ # same 3 pairs, observe_cmd patched to the r77 -C form, rederive untouched:
LEDGER-CHECK-77: FAIL pairs=3 problems=5                         EXIT=1
     L76-19: stated_text not found …
     L76-19/20/21: rederive git argv must open with `-C <dir>` … refused
   (receipt: ledger-check-l76-rederive.txt — the rederive class reds independently)
```

Re-verifications (read-only, all reproduced): `controls-c.txt:30/48/55/57` and
`controls-ca.txt:40/67` + `grep -c '^LEG FAIL'` → 7; fleet `git show --numstat 1cd8e33c` →
`1 1 .ufo/reports/round-76/kotodama.md`; `SWARM_ROLES` 10-member Set and `unknown_role` at
`ufo-swarm-wave.mjs:265,988-989`; base QUALITY `29` numbered criteria, `0` "lane report", `0`
`^30.`; `PROTOCOL.md:134-137` append-only clause present; `considerthese` absent; frozen r76
ROWS text "adds exactly S894-S896" vs whole-file `Counter` diff at `accept-c.py:1588-1605`;
`selftest-ca.txt` line 51 `SELFTEST: 199/199`; `selftest-receipt.txt` `row-extra`,
`index-required-section`, `collcheck-map-alias`, `collcheck-archive-identity`,
`legcount-duplicate` all printing their named red/green sets; lane HEAD = base `211f952`;
`reports/round-77/` holds `telemetry/` only (no counters, claims or ledger installed yet —
consistent with every "unrun end-to-end" caveat).

## Findings routed to the L1

1. **Reclassify the owed rows.** M4/M5/M6 are no longer owed — the `--ledger-check` run above
   is the named demonstration; M1/M2/M7/M8 are fixture-verified, not merely asserted. The
   lesson's tally "exactly two rows have an executed red proof" should become: defect-evidence
   verified × all; fix-shown-able-to-fail × M1,M2,M4,M5,M6,M7,M8,M10 (+M13/M16 partially via
   REPOINTED); truly owed: M3, M9, M11, M14, M15.
2. **`legcount.py`: a frozen duplicate must FAIL**, not NOTE — Counterexample A. One-line
   change in the checklist seat's tool before the freeze.
3. **`_doc_url_key` drops `?query`** — Counterexample B. Either document-level keys must keep
   host-declared discriminating params, or the draft's "query-aware record keys" must be
   rewritten to say what it does. Not a blocker for D1/D2.
4. **M3's gate still does not exist at freeze time.** `run-controls.sh` can only detect a bad
   freeze after it is committed; if the L1 wants the expectation-check as a *freeze refusal*,
   it must live in `manifest-check.py` or the counters' LEGCOUNT/FROZENCFG, not in a
   post-commit harness.
5. **M9 confirmed absent by construction** — nothing reads map records for non-adopted staged
   ids. Correctly labeled `owed`; either accept review-only or add a closure limb.
6. **Lesson table self-consistency** — M15's "yes, demonstrated" contradicts the intro/§5
   tally and is the weakest possible basis (unrecoverable red bytes, no guard); downgrade to
   "defect verified, fix owed" like M14.
7. **M16's premise is stale** — REPOINTED does read the landed entry's `source:` ids; the
   honest residual is "config must freeze `removed_ids`/`staged_universe`" plus
   "bare inline citations outside `source:` lines are ungraded".
8. **Ledger-check visibility** — `problems[:20]` cap hid L76-19/20/21; print all or the tail.
9. **M6's red surface moved** — r77 refuses `-C`-less argv at `observe_problem`, so the
   `chars=`/rev-as-path diagnostics never print on the r76 ledger (exec block short-circuit,
   `accept-ca.py:1724`). Class still reds; if the lesson names the diagnostic text, name the
   new one or note the two-level guard.
10. **CLAIMS-DRAFT moved a third time** — sha `5f791d3a…` (8768 B) vs ScribeLesson's recorded
    `ac5aead4`; on the checked cells (D2 locator, leg lists, triage) the 22:49 content holds,
    but every "closed by the 22:49 revision" claim should re-verify against the bytes that
    actually freeze.
