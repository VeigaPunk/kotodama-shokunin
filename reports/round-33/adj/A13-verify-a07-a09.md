- Seat: A13 | verifier | claim A | date 2026-10-19 | baseline 139e3b6

# A13 — independent re-run of the A07–A09 check classes

## Status of the dependencies, and what this seat did instead of waiting

A07 (`adj/A07-history.md`), A08 (`adj/A08-language.md`) and A09 (`adj/A09-pins.md`)
were **not on disk** at every read this seat made (first check 2026-10-19T03:52:59Z,
last 2026-10-19T03:55:05Z; `ls reports/round-33/adj/` returned only
`A16-shonen-material.md`). The whole 64-seat wave is still running.

Per `targets.json` `shared_rules[4]` ("if a dependency fragment is missing, do what you
can, record the owed path, finish; the integrator completes") this seat did **not** idle.
It executed, at the round-33 tree, the **check classes A07/A08/A09 are defined to
perform**, and recorded the results as the differential baseline the integrator compares
A07–A09 against. Every result below is a live measurement at HEAD `139e3b6`, not a
restatement of a filed value. Nothing in this fragment verifies A07/A08/A09 themselves —
that comparison is the owed work.

Independent-work window: **2026-10-19T03:52:59Z – 2026-10-19T03:55:05Z**. Working tree at
that window: `git status --porcelain` = 3 rows (` M LOG.md`, `?? REGIMEN.md`,
`?? reports/round-33/`), `git rev-parse HEAD` = `139e3b662900557afe54f632b468619593dc9fcb`.
Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

## A07 class — adjacency-history consistency: filed commands re-run at HEAD

A07's mission is "re-run 2-3 filed commands from the r21/r29 adjacency audits and confirm
their filed verdicts still hold at HEAD". This seat re-ran **five**, chosen to cover both
audits and both command kinds (inventory, digest, ledger assertion, content sweep).

| # | filed command (source) | filed value | A13 re-run at 2026-10-19 | verdict |
|---|---|---|---|---|
| 1 | r21 A01 inventory `python3 -B -c '…'` (`reports/round-21/adjacency/entries.md:7-9`) | `R19 corpus: 10 10` / `R19 author fragments: 10 10` / `R20 author fragments: 4 4` | identical three lines, exit 0, 03:53:22Z | **holds — exact** |
| 2 | r21 `sha256sum PROVINCE.md` (`entries.md:4`) | `05b34a579c5d…` | `05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6` | **holds — exact** |
| 3 | r29 `git diff --quiet -- PROVINCE.md; sha256sum PROVINCE.md` (`reports/round-29/adjacency/A09-A12-handoff.md:20,52-57`) | exit 0; full digest as above | exit 0; identical digest, 03:52:59Z | **holds — exact** |
| 4 | r29 final ledger census, read-only asserts over `reports/round-29/adjacency/ledger.json` (`A09-A12-handoff.md:116-139`) | `ledger_paths=6 entries=2 rows=0 audits=4 bleed=0 unfiled_bleed=0 filed_non_bleed_findings=1 sweep_dispositions=4` | identical line, exit 0, 03:52:59Z | **holds — exact** |
| 5 | r29 four reconstructed absence sweeps (`A09-A12-handoff.md:64-96`) | four `baseline=/current=` lines, `A29-ADJ-EVID-01` basis | byte-identical output, 03:54:21Z | **holds — exact** |

Reproduction 1 also confirms the r21 inventory's *inputs* still exist, i.e. the r21 A01
`PASS` verdict has not been falsified by later tree drift. Reproduction 5 re-derives the
`A29-ADJ-EVID-01` basis (`register-lexicon-ceilings.md:4` claims zero for
`which semantic fields` while baseline `sound-symbolism.md:106` already carries it) and
still shows the other three sweeps as time-scoped sibling landings — the r29 disposition
is unchanged at HEAD.

**A07-class named finding (F3, below):** the one filed r21 *finding*,
`A21-D4-XF-01`, no longer reproduces its own cited evidence at HEAD. Detail in Findings.

## A08 class — language audit over round-33 artifacts

A08's mission is a grep of all round-33 fragments for promotion/canon/closure/
verified-without-verifier claims. A13 ran the scan at **2026-10-19T03:54:52Z** over the
seven files then present (`claims.json`, `targets.json`, `telemetry/dispatch-declared.json`,
`adj/A16-shonen-material.md`, `op/K01-falsifier-scout.md`, `op/O01-row-drafts.md`,
`op/O07-baseline-receipt.md`).

Term counts: `promot` 16, `canon` 16, `clearance` 6, `closure` 13, `certif` 0,
`verified` 21, `PASS` 26.

Every hit is a **negation, a requirement statement, a mission-text occurrence, or a
quoted historical verdict** — none asserts a round-33 promotion/canon/clearance/closure
verdict:

- `reports/round-33/claims.json:59` states the requirement ("no promotion/canon/closure
  language anywhere in round-33 artifacts"); `:68` is the `non_goals` negation
  ("no promotion, canon, clearance, or closure verdicts (operator-owned)"). `:44` and
  `:46` are the word "canonicalize"/"canonicalized" describing K03's item enumeration.
- `reports/round-33/targets.json:15,31,51,52,55,69` — mission text, including the
  instruction to grep *for* this language.
- `reports/round-33/adj/A16-shonen-material.md:9,11,63,152` are explicit negations
  ("no promotion/canon/clearance/closure verdict", "Canon: NON-CANON engineering
  evidence", "round 33 awards no promotion, canon, clearance or closure verdict");
  `:44,68,90,115` quote r24's filed `verified-with-conditions` verdict with its source
  pointer `reports/round-24/promotion-review.md` — a routed historical reference, not a
  round-33 claim.
- `reports/round-33/op/K01-falsifier-scout.md:23,32,48,104` use "closure test" and
  "promotion-checklist falsifier" as **property names** of the `SKILL.md:715` audit
  artifact, not as verdicts.

**A08-class verdict at this instant: clean, zero un-negated verdict language.** This is a
partial scan by construction: 57 of 64 seats had filed nothing yet. The full A08 scan must
be re-run against the final fragment set — recorded under Owed.

## A09 class — pin-cascade exposure, measured independently

A09's mission asks which frozen baselines/pins reference the shared files the integrator
may edit (the lessons README and SKILL.md lines). A13 measured this directly.

**`corpus/lessons/README.md` is pinned twice; both pins are currently intact:**

- `reports/round-26/run-validation.py:97` — `README_BASELINE_BLOB =
  "a31870556c733498243b56697896504a2fb3679a"`; `:1491-1501` computes the live Git blob
  and fails when it differs: *"the filed lessons index was edited in place (blob … !=
  declared baseline …); the claim requires a new revision file, not an in-place edit"*.
  Live `git rev-parse HEAD:corpus/lessons/README.md` = `a31870556c733498243b56697896504a2fb3679a` — **matches**.
- `reports/round-25/validation.json` `input_sha256["corpus/lessons/README.md"] =
  "ec7469dadf87df3e13cdc2b53445810840d22b9c003a6407e5a449e8f44b3f4c"`, recorded by the
  runner at `reports/round-25/run-validation.py:1097`, with a coherence leg at
  `:1063-1083` that reports "Evidence changed while being measured". Live
  `sha256sum corpus/lessons/README.md` = the **same digest** — currently intact.

**`SKILL.md` is pinned nowhere.** `git grep '79460eb6ada5682d'` (its current blob) is
empty; zero rows in any `tools/gates/frozen/**/MANIFEST.tsv` mention SKILL; the blob has
moved freely across rounds (`4f09c99`→`63bf9061`, `11df1fd`→`0e643c7b`, HEAD→`79460eb6`).
Live `sha256sum SKILL.md` = `79fe91d3d42917a166492d1d1159676f12aa2ac4bb5688ecfccd496413d5b04d`,
715 lines. The seven `tools/gates/frozen/` hits for the string `SKILL.md`
(e.g. `tools/gates/frozen/round-3/inputs/corpus/knowledge/verification/gate-frozen-run-standard.md:5,15,28,243`;
`tools/gates/frozen/handoff-packet-check/r9-pre/freeze.txt:2,110,119`) are **prose inside
input snapshots and freeze notes, not hashed rows** — a SKILL.md edit breaks no pin.

**A09-class named finding (F1, below):** claim O's required after-state cannot be reached
without breaking the round-26 README pin. Detail in Findings.

## Findings

**F1 — material, A09 class: claim O's after-state and the round-26 README pin are mutually
exclusive as written. Owner: integrator (round-33).**

Claim O's `after_required.a_lessons` (`claims.json:29`) requires the lessons README to
carry 33/33 rows and prose arithmetic 33, and its counting command
(`claims.json:33`) is `python3 -B reports/round-25/audit/c31-lessons-index-audit.py`
exiting 0 with zero findings. That tool hardcodes its subject:
`reports/round-25/audit/c31-lessons-index-audit.py:36` `INDEX = os.path.join(LESSONS, "README.md")`,
and its CLI accepts only `--selftest` and `--json` (`:436-438`) — there is **no path
override**. Measured at declaration (03:53:32Z): `lesson files: 33`, `index rows: 26`,
`FAIL C31_index_rows_eq_files`, `FAIL C34b_prose_arithmetic`, findings
`C31-1` (the seven files round-26..32) and `C34-2` (`{stated [26,26], measured [26,33]}`),
exit 1.

So the only way to make that counting command pass is to change the bytes of
`corpus/lessons/README.md`. Doing so:

1. fails `reports/round-26/run-validation.py:1498-1501` (`filed_blob != README_BASELINE_BLOB`),
   the r26 claim's explicit "new revision file, not an in-place edit" leg; and
2. stales the `reports/round-25/validation.json` `input_sha256` row for that path.

Filed lessons record the standing rule in the other direction:
`corpus/lessons/round-31.md:53` — "README rows are parent-owned **additions**, never edits
of filed rows"; `corpus/lessons/round-32.md:45` — "rows are parent-owned additions, never
edits." The r25/r26 precedent (`reports/round-26/zzz-lessons-index-revision-3.md` as a
**new file**; `reports/round-26/lessons/C51-C52.md:26,139`) is a new revision file with the
filed index byte-frozen.

This is a trade, not a defect in either claim: claim O asks for a green c31; the pin asks
for a frozen index. A13 does not resolve it (integration is not a verifier's call) and
files it for the integrator/operator with three named options:

- **(a) Declared repin** (r20 precedent `35b6797`, recorded as a projector re-pin with
  before/after digests): edit the README, record the old/new blob + sha256 in the round-33
  telemetry/validation record, and restate the r25 input pin and r26 `README_BASELINE_BLOB`
  as superseded-with-evidence. Satisfies claim O's literal counting command; costs two
  recorded pin supersessions.
- **(b) New revision file, c31 leg re-scoped**: land `reports/round-33/<revision>.md` and
  accept that c31's C31/C34b stay red, dispositioned as an index-vs-live-partition
  time-scope reading (the r25/r26/r27/r28 pattern). Keeps every pin intact; **does not**
  meet claim O's stated threshold ("C31/C34b PASS + findings == 0").
- **(c) Split**: new revision file now, plus a separate, operator-approved in-place index
  update as its own dated act with the repin record from (a).

Whichever is chosen, the *decision and its evidence* must be in the round record; a silent
in-place edit that leaves r26's leg red with no disposition is the failure mode to avoid.

**F2 — naming, A07/A03 class: two different "tracked path" baselines are in play. Owner:
integrator/A03.**

`claims.json:57` declares the regimen-2 opening baseline as `git ls-files | wc -l = 2655`.
A13 measured `git ls-files | wc -l` = **2655** at HEAD and `git ls-files --with-tree=139e3b6
| wc -l` = **2655** — the claim is correct for the whole tracked tree. But
`reports/round-32/scope.md:12,33-36` reports **1,870** "primary tracked paths", which is a
*scoped* surface: 1,735 paths under `reports/round-{8..31}` plus 135 round-tagged frozen
paths. The whole `tools/gates/frozen/` tree alone is 237 tracked paths
(`git ls-files -- tools/gates/frozen/ | wc -l` = 237), so 1,870 is not "all tracked paths"
and 2,655 is not "the protected surface". A03's comparison "vs the 2655-file baseline"
must state which surface it counts, or it will report a spurious 785-path delta.

**F3 — evidence currency, A07 class: the r21-filed finding's cited evidence no longer
reproduces at HEAD. Owner: O/D4 projector owner (already routed); consumer caution for A07.**

`reports/round-21/adjacency/ledger.json` (finding `A21-D4-XF-01`) cites
`examples/culture-d4/typed-labels.d4.yml:28,329` as D2 metadata and a D2 rank block at
`:335-649,853-966`. At HEAD:

- `:28` reads `"canon": "not canonized (D4 design drill); derived view of examples/culture-d4/packet.d4.yml"` — no D2;
- `:329` reads `"E2"` — no D2;
- the live file's sha256 is `c23b0ab532cfb9d4bb403405c6996982a447098048e08facbbc9f341ea13f82e`, against the r22 analysis baseline `cbcf997f5f38fac89b0fb1b6a6841ec42c9041a2599df44083ddefc5c22cfb4f` (`reports/round-22/bleed/analysis.md:16`).

The repair trail is filed: `reports/round-22/bleed/analysis.md:9-16` (census + "filed but
unfixed" at that revision), commit `0e81d9d99514631d6717e1ff354d5a5a759aa980` ("round-22:
O/C verified; D rejected (bleed-fix impl interrupted; routed to r25 with recipe)"),
`reports/round-24/box4-bleed.md:108-116` (implemented in the r22 window, append-only
correction), and the live digest matches the r30 pins
(`reports/round-30/audit/x38-law-gate-clean-state.json:16` and
`examples/culture-d4/expected-holds.json:4`). `reports/round-29/validation.json:82` states
"A21-D4-XF-01 remains outside this slice."

Consequence for A07's method: re-running a filed *command* reproduces a filed *value*, but
a filed *finding* can be superseded by a later round without the filing row changing
(append-only). A07 must pair each re-run with a currency read of the finding, or it will
report a repaired bleed as live. A13 files no repair and proposes no edit here.

## Cross-check against `adj/A10-receipt.md` (landed after this seat's first write)

`reports/round-33/adj/A10-receipt.md` landed while this fragment was being written. Its
rows A07/A08/A09 are the stand-in for the missing fragments — A10-F5 itself records that
"this receipt's nine rows are seat-executed provisional" and that "if a landed fragment's
verdict differs from a row here, the fragment wins and this row is errata". A13 therefore
verified A10's three rows independently, as part of its A07–A09 mission.

**A10-F1 — verified.** Live `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml`
→ `summary: 20/20 legs passed`, exit 0, 03:56:59Z; r21's filed line
(`reports/round-21/adjacency/A11-A12-handoff.md:46`) reads **19/19**. The drift is real and
the r21 *verdict* (green) holds.

**A10-F2 — verified, pointer off by one.** `sha256sum AGENTS.md` =
`1afaf106f20b440ad263ab231c215773436c7f42ab106848f5550b87ecf41035`; the r29 filed value
`be3a9477ed28ba401352ebce7c182d529223e552d0dba0d75f3b97b956be2c8b` is at
`reports/round-29/adjacency/province-entries.md:15`, not `:14` as A10 cites. Commit trail
`17e90b9` → `11df1fd` → `c53782a` confirmed with `git log --oneline -3 -- AGENTS.md`.

**A10 row A07 — one row verified, one row has a defect.**

- Row A07(2) (`git rev-parse HEAD:PROVINCE.md` → `313b182f…`) — **verified**, but the cited
  pointer is `reports/round-21/adjacency/province.md:19`; the blob is on **`:17`** (and in
  `ledger.json:89`, `A11-A12-handoff.md:48`). Off by two.
- Row A07(1) — **defect, two parts.** A10 states the live v3 exercise packet sha256
  `6ced88ad…` is "identical to the r21 filed receipt
  (`reports/round-21/adjacency/A11-A12-handoff.md:41`)". (i) That line carries **no packet
  digest at all** — it lists counts only; the r21-filed digest lives at
  `reports/round-21/adjacency/ledger.json:81`. (ii) The digests are **not identical**:
  r21 filed `e92f5e6775b657c24fa6260e340e4e7a04cf6c3777188cba80678bed079ae43b`, live is
  `6ced88ad009f1cfc94f7fc9e5656555f7da6682ce8f7afc3eb16734272f0f0bb` (`grep -rn '6ced88ad'
  reports/round-21/` → zero hits). The **count fields do reproduce exactly** (fields 16/16,
  glossary 20/20, findings 0, links 105/105, claims 27, statuses 16/7/4, exit 0), so the
  row's *verdict* survives but its *identity claim* must be corrected to: counts identical,
  packet digest drifted (the packet is regenerated; r28 pins the v3.1.1 assembly,
  `reports/round-28/pinsweep/v3-baseline-r28/packet.md:14`).

**A10 row A08 — agrees with this seat's partial scan** (declaration-surface hits only,
each a negation, mission text or routed reference). Both scans are pre-wave and both must
be re-run.

**A10 row A09 — refuted in scope; this is the material defect.** A10's grep is correct as
run — A13 reproduced it: `grep -rl` for either the SKILL.md digest `79fe91d3…` or the
README digest `ec7469da…` under `tools/gates/frozen/` returns **0 files**, and no
`MANIFEST.tsv` row pins either path. But its scope stops at `tools/gates/frozen/`, and the
README pins are **not there**: they are `reports/round-26/run-validation.py:97`
(`README_BASELINE_BLOB = "a3187055…"`, failing leg at `:1498-1501`) and
`reports/round-25/validation.json` `input_sha256["corpus/lessons/README.md"] =
"ec7469dadf87df3e…"` (runner leg `reports/round-25/run-validation.py:1063-1083`). A13's F1
above is the measurement. A10's conclusion — "the integrator-applied edits to
`corpus/lessons/README.md` … break no frozen baseline and owe no re-pin" — is **true about
frozen baselines and false about pins**. Corrected form: the SKILL.md half of the row
stands (no pin anywhere); the lessons-README half owes a pin decision (F1's options a/b/c).

Per A10-F5's own rule, this fragment's A09-class measurement wins over A10's A09 row, and
the row is errata rather than a second vote. Owner of the correction: A10/integrator, at
`adj/audit-assembled.md` time.

## Verification limits

- This fragment verifies **the round-33 tree's behaviour on re-run commands**, not the
  correctness of the r21/r29 audits' own reasoning, and not A07/A08/A09 (unfiled).
- A10's rows are *provisional seat-executed* stand-ins, not fragments; A13's cross-check
  above is a verification of those rows, and A14's row-for-row fragment match remains owed.
- The A08 scan is a **time-stamped partial**: 57 seats had filed nothing at 03:54:52Z.
- The pin measurement is a **point reading**. The integrator's edits happen after it;
  F1's whole point is that the pins are live surfaces, so a post-integration re-measure is
  required (see Owed).
- No historical validator was executed; no filed byte was changed by this seat; no git
  command beyond read-only queries was run. This seat writes only
  `reports/round-33/adj/A13-verify-a07-a09.md`.

## Owed

- `reports/round-33/adj/A07-history.md` — differential comparison against this fragment's
  A07-class table (items 1–5), plus F3's currency caution.
- `reports/round-33/adj/A08-language.md` — the full-fragment-set language scan; this
  fragment's scan covers only the 7 files present at 2026-10-19T03:54:52Z.
- `reports/round-33/adj/A09-pins.md` — differential comparison against this fragment's
  A09-class measurements and a ruling on F1's three options.
- **Errata owed on `adj/A10-receipt.md`** (owner: A10/integrator, at
  `adj/audit-assembled.md` time): row A09's "no re-pin owed" is false for the
  lessons-README half (see the cross-check section); row A07(1) must restate its identity
  claim as counts-identical / digest-drifted; row A07(2)'s pointer is `province.md:17`
  (not `:19`) and A10-F2's pointer is `province-entries.md:15` (not `:14`).
- Post-integration re-measure (integrator): re-run the five A07-class commands **and**
  `git rev-parse HEAD:corpus/lessons/README.md` + `sha256sum corpus/lessons/README.md`
  after any lessons-README edit, to confirm the pin state matches whatever F1 decision was
  recorded.

Differential command for the integrator (one block, read-only, no writes):

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git rev-parse HEAD
git diff --quiet -- PROVINCE.md; echo "province_exit=$?"
sha256sum PROVINCE.md
git rev-parse HEAD:corpus/lessons/README.md
sha256sum corpus/lessons/README.md
python3 -B reports/round-25/audit/c31-lessons-index-audit.py; echo "c31_exit=$?"
python3 -B -c 'from pathlib import Path; v=["label-channel-routing-verification.md","pre-declared-hold-set-reconciliation.md","generated-artifact-roundtrip-verification.md","gate-battery-surface-verification.md","two-reader-interop-agreement.md"]; s=["typed-label-routing-workflow.md","generated-artifact-lifecycle.md","hold-set-contract-in-brief.md","era-material-scoped-reconciliation.md","finding-disposition-workflow.md"]; r=[Path("corpus/knowledge/verification")/p for p in v]+[Path("corpus/knowledge/synthesis")/p for p in s]; a=[Path("reports/round-19/entries")/f"R19-C{i}.md" for i in range(11,21)]; b=[Path("reports/round-20/entries")/f"R20-D{i}.md" for i in range(21,25)]; print("R19 corpus:",len(r),sum(p.is_file() for p in r)); print("R19 author fragments:",len(a),sum(p.is_file() for p in a)); print("R20 author fragments:",len(b),sum(p.is_file() for p in b))'
```

Expected at the pre-integration tree (all five A07-class values, 2026-10-19): `province_exit=0`;
`05b34a579c5d4f4ec78957cdedb658246ff292df3e21181c66186403f2b942d6  PROVINCE.md`;
`a31870556c733498243b56697896504a2fb3679a`; `ec7469dadf87df3e…b3f4c  corpus/lessons/README.md`;
`c31_exit=1` with the two findings; `R19 corpus: 10 10` / `R19 author fragments: 10 10` /
`R20 author fragments: 4 4`. Any post-integration deviation is the pin cascade F1 predicts
and must be matched to the recorded decision.

## Citations

- `reports/round-33/claims.json:16,19-64,25-26,29,33,37,57,59,68`
- `reports/round-33/targets.json:5-11,54,56,60` (`shared_rules`, A07/A08/A09 missions)
- `reports/round-21/adjacency/entries.md:4,7-9`
- `reports/round-21/adjacency/ledger.json` (`A21-D4-XF-01`, `verdict`, `province_accuracy`, `unfiled_bleed`, `inventory`)
- `reports/round-29/adjacency/A09-A12-handoff.md:20,52-57,64-96,100-106,116-139,142,146`
- `reports/round-29/validation.json:82`
- `reports/round-22/bleed/analysis.md:9-16`; `reports/round-24/box4-bleed.md:108-116`
- `reports/round-25/run-validation.py:88,1063-1083,1097`; `reports/round-25/validation.json` (`input_sha256["corpus/lessons/README.md"]`)
- `reports/round-25/audit/c31-lessons-index-audit.py:36,436-438`; `reports/round-25/audit/c31-lessons-index-audit.md:60-67`
- `reports/round-26/run-validation.py:97,1491-1501`; `reports/round-26/lessons/C51-C52.md:26,139`
- `reports/round-30/audit/x38-law-gate-clean-state.json:16`; `examples/culture-d4/expected-holds.json:4`
- `reports/round-32/scope.md:12,33-36`; `corpus/lessons/round-31.md:53`; `corpus/lessons/round-32.md:45`
- `corpus/knowledge/linguistics/register-lexicon-ceilings.md:4`; `corpus/knowledge/linguistics/sound-symbolism.md:106`
- `tools/gates/frozen/round-3/inputs/corpus/knowledge/verification/gate-frozen-run-standard.md:5,15,28,243`; `tools/gates/frozen/handoff-packet-check/r9-pre/freeze.txt:2,110,119`
- `reports/round-21/adjacency/province.md:17`; `reports/round-21/adjacency/ledger.json:81,89`; `reports/round-21/adjacency/A11-A12-handoff.md:41,46,48`
- `reports/round-29/adjacency/province-entries.md:15`; `reports/round-28/pinsweep/v3-baseline-r28/packet.md:14`
- `reports/round-33/adj/A10-receipt.md` (rows A01–A09, findings A10-F1/F2/F4/F5, Owed list)
- Commands run (all read-only, lane root, 2026-10-19T03:52:59Z–03:57:30Z):
  `git rev-parse HEAD`; `git status --porcelain`; `git ls-files | wc -l` (2655);
  `git ls-files --with-tree=139e3b6 | wc -l` (2655); `git ls-files -- tools/gates/frozen/ | wc -l` (237);
  `git diff --quiet -- PROVINCE.md` (0); `sha256sum PROVINCE.md SKILL.md corpus/lessons/README.md AGENTS.md corpus/knowledge/synthesis/worldbible-integration-contract.md`;
  `git rev-parse HEAD:corpus/lessons/README.md HEAD:SKILL.md HEAD:PROVINCE.md`;
  `python3 -B reports/round-25/audit/c31-lessons-index-audit.py` (exit 1, 2 findings) and `--selftest` (28/28, exit 0);
  the r21 A01 inventory one-liner (exact reproduction);
  the r29 ledger-census assertion block (exact reproduction);
  the r29 four-sweep reconstruction block (byte-identical output);
  `python3 tools/gates/typed-pipeline-gate.py examples/culture-d4/packet.d4.yml` (exit 0, 20/20);
  `python3 tools/exercise-handoff-e2e.py --profile v3 --quiet` (exit 0, packet_sha256=6ced88ad…);
  `git log --oneline -4 -- examples/culture-d4/typed-labels.d4.yml`; `git log -1 0e81d9d`; `git log --oneline -3 -- AGENTS.md`;
  `git grep -n '79460eb6ada5682d'` (empty); `git grep -n 'c23b0ab532cfb9d4'`;
  `grep -rl` for both shared-file digests under `tools/gates/frozen/` (0 files);
  `grep -rn '6ced88ad' reports/round-21/` (0 hits); `grep -rn '313b182f'|'be3a9477'|'e92f5e6775b6'` in the r21/r29 filings;
  `grep -r -i -c` term scan over `reports/round-33/`.
