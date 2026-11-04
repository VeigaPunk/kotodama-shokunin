# Round 87 — lesson draft (ScribeLesson seat, author-side, NOT FILED)

Status: NON-CANON engineering evidence. Draft for L1 integration only; this seat writes no lesson under `corpus/lessons/`, no QUALITY entry, no SOURCES row, no SCORECARD line.

Pins: base `83846a22ee1e9da7aa52ac505ccebf4455169247`; prefreeze controls `732c45394c73fcffd9fc623b939d446c7b11a9db`; frozen claims and counter `2a3b5643899c3520867ae930593cafef6ef19cad`. Claim: O only (operability, capability acquisition). Not all-green.

## 1. What the O claim does and does not add

Frozen predicate (`reports/round-87/claims.json`): the committed `tools/check-attestation-packet.py` scores exactly 12/12 on `reports/round-87/measure87.py` through its public `--packet PATH --json` CLI.

Correction of the frozen wording, by text only, no edit to frozen bytes. The frozen `bounds` field says the acquisition is "a production CLI with the newly enumerated integrity relationships". That overstates novelty. The r86 stage checker already checks those relationships. Receipt: `receipts/check-craft-r86-stage.py` (sha256 `b13f7338987270379fac259256e7c45843ae999ba3ddedb9db3874b6943b9da6`, from `.ufo/waves/round-86/w1/stage/ExecCraftLedger/check-craft.py` at base). It contains:

- fixed population: `records: exactly six required` (line 148);
- duplicate record id: `id: duplicate` (line 154);
- selected solution in an unresolved riddle: `solutions: no selected answer permitted` (line 106);
- conjecture promoted to wording: `editorial: transmitted and conjectured wording must remain separate` (line 125);
- translation backdating and wording conflation: `translation: source/target clocks conflated` (line 134) and its wording check (line 137);
- clock presence: `explicit value or null required` (line 67);
- duplicate JSON keys refused: `duplicate JSON key` (line 168).

So what round 87 can add is: a public CLI with a JSON findings report (`{records, findings:[{id,record,detail}]}`), exit codes 0/1/2, a population that is not fixed at six, and an isolated selftest path that runs the actual CLI. The first detection of the four relationships is not new, and neither is first packet completeness checking. The r86 checker prints `CRAFT: PASS/FAIL` text and has no `--json` output and no `--packet` option. Whether ExecAuditor's production bytes deliver a variable population or the selftest path is an open question until L1 inspects the committed revision. This draft claims neither.

## 2. Mistakes that can fail (grounded)

**M1 — r86 absent-tool control did not kill a present fake tool.** The r86 frozen O counter's controls were framed around absence. The lane probe `.ufo/waves/round-86/w1/stage/CriticPredicate/probe.txt` ran `O-nonreader-fake-selftest-and-bare-registry` and printed `LEG PASS TOOL` and `ACCEPT-O-86: PASS legs=8/8`. The probe is a transport overlay on synthetic lands, so it is evidence that the counter accepted a non-reader, not that a live CLI passed. The failure mode is a control that tests the wrong direction. Carried as QUALITY 34(i).

**M2 — the prefreeze counterfeit set was too narrow to show the frozen 12/12 is weak.** The round-87 prefreeze controls contain a constant non-reader and an absent tool (`reports/round-87/no-work.json`, `TOOL_ABSENT`, 0/12). They do not contain a filename-keyed or label-echo forgery. CriticCounter then built one: `filename-spoof.receipt.json` scores 12/12, rc 0, against the frozen counter (candidate `1490943f11414eb025e2f55f966f5b6c4c7bd8bd9c03d38527db71d727595d2b`). It answers from the packet's basename and never opens the body; the counter's own transport oracle does the same thing at `measure87.py` (the selftest oracle reads expectations from fixture names). A second forgery, `all-labels-wrong-record.receipt.json`, also scores 12/12 by emitting every label with invented record identifiers and `records=-999`. Author-side repeat by ScribeLesson, after the lead asked for no further probes: `receipts/forge-filename-keyed-measure87.json` (candidate sha256 `ef1fd47c1ef0ff75c2662e4c80891d5fd5c25af6a3442654efdf47d09b509334`, `passed 12/12`, exit 0). The consequence for O: 12/12 binds to the finite frozen battery, not to packet-sensitive correctness. Carried as QUALITY 34(iii).

**M3 — a candidate that returns `findings: null` leaves no receipt.** `null-findings.receipt.json`: rc 1, traceback at the counter's iteration over findings, no aggregate measurement. The counter handles only JSON `ValueError` and `TimeoutExpired`. Carried as QUALITY 34(iv).

**M4 (question for L1, not decided here) — scratch paths in committed receipts.** `reports/round-87/no-work.json`, `constant-pass.json` and `counter-selftest.json` each carry `/fast/scratch/hyaku/kotodama-r87/L1` in their `command` array as the `--work` argument. `measure87.py`, `controls/constant-pass.py` and the `stdout` fields carry no scratch root. QUALITY 31(ii) forbids scratch as cited evidence and allows scratch as where a run happens. Whether a `--work` argv is "cited evidence" is a scanner-shape question: this seat does not run `tools/check-cited-records.py` and does not call the freeze red or green. Frozen bytes are not edited.

## 3. Measured control receipts (author-side copies, sha256)

Copies in `receipts/`, taken with `git show <rev>:<path>` from the frozen revision and not edited:

| receipt | sha256 | what it shows |
|---|---|---|
| `measure87.py` (frozen counter) | `131b29e84d39c2cbd22993aaadd469b5a96602651927730c980503cc74738e62` | counter bytes, matches claims |
| `claims.json` (frozen) | `bfc2de174261ad410a63abb3949385d8be76fe29ef8aaa528ec8d0f9feb43264` | predicate and bounds |
| `no-work.json` | `fdf9dcec61f569971ddb503644c2683646485f7d028b170f4d840160c068668e` | base has no CLI: `TOOL_ABSENT`, 0/12, rc 1 |
| `constant-pass.json` | `5dabfd5dbfe130f1a888705bbe8d0f708a1c560029bad649949cd9d8f30eb676` | constant non-reader: 3/12, rc 1. Passing cases: `positive-six`, `unknown-explicit`, `reordered-records`. Failing: the other nine, including `invalid-json` (rc 0 where 2 is required) |
| `controls/constant-pass.py` | `78b66e106bb4a149849a09d92c02fc0b7dd43316fa66a680a22ec07eef01567d` | the constant non-reader source |
| `counter-selftest.json` | `6f7474dd9a66c5c394220248dd767df097ac3173191616bc60580240c14cac9e` | transport selftest: `clean-transport` 12, `constant-pass` 3, `constant-reject` 1, `non-json` 0; all `passed: true`, rc 0 |
| `check-craft-r86-stage.py` | `b13f7338987270379fac259256e7c45843ae999ba3ddedb9db3874b6943b9da6` | the r86 stage checker (section 1) |
| `forge-filename-keyed.py` | `ef1fd47c1ef0ff75c2662e4c80891d5fd5c25af6a3442654efdf47d09b509334` | author-side forgery source (filename-keyed) |
| `forge-filename-keyed-measure87.json` | see `receipts/SHA256S.txt` | author-side run result: 12/12, rc 0 |

The draft check `check34-draft.py` was run twice in scratch: green on the frozen receipts (`COUNTERFEIT-KILL: PASS non-reader=3/12 rc=1 blanket-refusal=1/12`, exit 0) and red on a manufactured 12/12 receipt (`COUNTERFEIT-KILL: FAIL non-reader=12/12 rc=0 blanket-refusal=1/12`, exit 1). Scratch was removed after both.

Timing (R86-C3): the commit `732c45394` adds `constant-pass.json`, `controls/constant-pass.py`, `counter-selftest.json`, `measure87.py` and `no-work.json`, all absent at base. The freeze commit `2a3b5643` adds only `claims.json`. The receipts record argv, rc, stdout and digests; they carry no wall-clock run time. "Before declaration" therefore means commit order, not execution time, and the lesson says so.

## 4. Carried debts (preserved, not repaired)

- **C1 numeric and lowest-axis.** No numeric 0–10 score is asserted. Freshness stays the historically lowest axis, paused by the round-11 L0 question. Carried from R86-C1 unchanged.
- **C2 counter debts not repaired by the packet auditor.** `measure87.py` tests packet records only. It has no duplicate-source-id leg and no empty-decision-cell leg, so ExecAuditor's packet work does not repair the D-counter debts (R86-C2; R85-C2 remains partial). Measured: no `S\d{3}` or decision-cell logic in `measure87.py`.
- **C3 prefreeze timing.** See section 3. Satisfied by commit order for round 87 only; the r86 receipts remain as they were.
- **C4 planner policy conflict.** The round uses L1 canonical planning. The L2 planner-policy requirement conflicts with it and is unresolved; disclosed, not waived (R86-C4).
- **C5 non-author cited-record red.** Two scratch references in the unchanged non-author r84 spotcheck remain. The lane does not rewrite verifier-authored history (R86-C5).
- **C6 unresolved archives.** S925 and S926 same-page Wayback coverage: 429/403 responses with a positive control, recorded as unavailability, not absence (R86-C6). S927/S928 inherited Wayback links are not reopened here.

## 5. Exact future bindings (not universal claims)

B1. Any sentence about O cites `reports/round-87/measure87.py` at `2a3b5643899c3520867ae930593cafef6ef19cad` and says "frozen finite battery 12/12". It also cites the filename-keyed 12/12 survivor (`filename-spoof.receipt.json`), so no reader takes 12/12 as anti-forgery evidence.

B2. Production acceptance runs without `--candidate` on the committed production revision, and its receipt records the candidate sha256 and the revision. The frozen forgery receipts used `--candidate` and their `revision` field is the freeze revision, not provenance for forged bytes. L1 owns this run.

B3. No lesson or QUALITY sentence says the battery rejects counterfeits in general. The round-87 scope is: constant non-reader killed (3/12), blanket refusal killed (1/12), filename-keyed non-reader survives (12/12), label-echo with wrong record survives (12/12), `findings: null` crashes without a receipt.

B4. A future counter that claims forgery resistance freezes filename-keyed and label-echo forgeries before its claims freeze, under QUALITY 34(ii). Not done for round 87.

B5. A counter that crashes on candidate output fails closed with a receipt (QUALITY 34(iv)). Round 87's counter does not yet do this; it is recorded as a defect.

B6. `check34-draft.py` is a draft in this seat's stage. L1 decides whether it is filed under `tools/` and whether the check line in QUALITY 34 names it.

B7. Pre-dispatch timing claims are stated as commit order (section 3), never as execution time.

## 6. Gate

Not in this draft. The Source Gate is supplied by a separate seat and integrated by L1. This draft opens no source row and cites no URL.
