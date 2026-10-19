- Seat: S01 | scribe | cross | date 2026-10-19 | baseline c9f4eaa

# S01 — round-44 integration draft: one authority, two gap candidates, one freshness gate

**Mission (`reports/round-44/targets.json`, seat `S01`):** *"Integration scribe: assemble the
whole round — all three claims' evidence chains, the per-axis verdict candidates, the SHONEN
section — into the integration draft the parent uses to land + judge."* Out path: this file only.

**Status: DRAFT, written mid-wave and finalized after the 25-file cut.** This seat wrote
**zero bytes** outside this file; all probes live under disposable `.scratch/s01/`. No
`reports/round-*/run-validation.py` was executed anywhere, in-tree or in a copy. Every figure
below was measured read-only by this seat at
`c9f4eaa707b6e977ff6e1616463e91f4b8afea5d` under
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, or is attributed to the sibling
fragment named beside it. Nothing here asserts promotion, canon, clearance or closure; those
tokens appear only as negations, quoted policy vocabulary, or routed references. The
integrator must recompute the wave census and every counter at close; the round is not
admitted on this draft.

**Wave census at this seat's first cut (2026-10-19T17:20Z):** 6 files. At the **finalization
cut** (`find reports/round-44 -type f | sort`, 25 files): `claims.json`, `targets.json`,
`telemetry/dispatch-declared.json`, `adj/A01-scope.md`, `cov/C01-entry-draft.md`,
`cov/C05-collision.md`, `cov/C06-scribe.md`, `cross/X00-connector.md`,
`cross/X01-trades.md`, `cross/X02-honesty.md`, `op/O02-verify.md`, `op/O03-defects-verify.md`,
`op/O04-witness-demotion.md`, `op/O06-census-artifact.md`, `op/O07-parity.md`,
`op/O08-negative-proof.md`, `op/O09-scribe.md`, `op/O10-census-verify.md`,
`review/R01-review.md`, `review/R02-review.md`, `scout/K01-resolver-scout.md`,
`scout/K02-gap-scout.md`, `scout/K04-gap-verify.md`, `scribe/S02-telemetry-draft.md`,
and this file. Claim O has its full evidence chain. Claim C has two scouts naming
**different** gaps, one drafted entry (the carried one), a conditional collision clearance,
and no C02/C03/C04. Claim Ca has **no filed artifact**; a scratch prototype is reviewed by
both reviewers. §8 lists the declared outs still absent; an absent seat is
`could-not-evaluate`, never green.

---

## §0 — The headline the integrator must read first

1. **The O09 successor body is real, byte-exact, and green in isolation.** Independent seats
   (O02, O03, O06, O07, O08, O10, with K01/O09/X01/X02 corroborating) plus this one extracted
   the same 515 lines and hashed them to
   `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64`:
   `--selftest` is **27/27**, exit 0; `--census` is `entries=223 refs=2730`,
   four-class `2556 direct + 166 fallback + 0 ambiguous + 7 unresolved = 2729`, plus
   **1 quarantined glob artifact = 2730**, `conservation: True`. The wrapped field reads
   **4/4 by identity** (`{sound-change.md, sound-symbolism.md, tone-prosody.md,
   writing-systems.md}`), not by arity.
2. **The successor is not yet durable.** `tools/harness/basename-couples-resolver.py` does
   **not exist** at `c9f4eaa`; `ls tools/harness/` lists only the six pre-existing tools.
   Claim O's `after_required` is therefore **not met at this cut** — the body is verified
   *as a draft*, not landed. The integrator's apply is the step that turns this into an
   operability move. Until then the honest verdict candidate is `unprovable-but-better`,
   not `improved`.
3. **Parity is measured at zero unexplained diffs.** O07 ran both tools over the same 223
   entries / 2730 refs: 50 fallback mappings, **0 mapping mismatches**, **0 token/class
   diffs** after the single documented substitution `prospective → unresolved`; the glob
   fragment is the documented §5.6 artifact separation. `2556+166+0+2+5+1 = 2556+166+0+7+1
   = 2730`. The r42 witness's bytes remain `d8d23a26…`.
4. **The blank-line defect is fixed as a code path, but it is latent, not live.** O03's
   whole-corpus differential found **0** entries where the witness captures a token the
   successor does not; **19** entries have `couples` as the last header field (future
   exposure), and **0** entries currently contain a blank line followed by an indented line
   before the next field. This seat independently reproduced the over-capture on a fixture:
   the r42 `couples_block` returns the indented prose as a second part; the successor
   returns only the field. **Do not file the fix as a present count correction** — it is a
   latent-trap closure.
5. **Claim C has two verified-unowned candidates and a freshness conflict between them.** The
   partition is **223** entries (`linguistics 25 / myth-symbol 26 / culture-material 25 /
   synthesis 29 / verification 24 / civilizations 94`), README revision **2.4**, sweep exit 0.
   - **K02 (fresh):** `culture-material/cartography-and-mapmaking.md` — no filename owner,
     zero topic-line owners among eleven dispositioned hits, not named in any prior-round
     registry (r19/r35/r39/r40/r42/r43 screened), and the partition's own
     `cosmology-cosmography.md:71,:102` explicitly disclaims the survey-map register.
   - **K04 (unowned but carried):** `myth-symbol/dream-vision-trance.md` — no filename owner,
     zero owners of the state/induction system, 52–61 demand files, but r42's K02 **R2**
     already named the same complex (`reports/round-42/scout/K02-myth-gaps.md:216-260`).
   **C01 drafted the dream entry** (it was the only path on disk at its cut), and C05/C06
   cleared/reproduced that path while explicitly noting K02 could compete. **The two scouts
   name different gaps and the claim is `+1` only.** On the claim's strict wording ("not
   carried from a prior round"), the cartography gap qualifies and the dream gap does not;
   landing the dream entry requires a named exception, not silence. **No corpus byte may
   move until the integrator chooses one gap and C03–C05 audit that exact path**; §3.2b
   states both evidence sets and the decision.
6. **Claim Ca is executable and this seat has already run its regression shape.** At r43's
   declared baseline `7ceff59`, the r42 resolver exists (`d8d23a26…`, selftest 8/8) and
   `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` exists (partition count 26), so
   r43's O and C `before` lines were **already false**; r43's Ca `before` (no per-finding
   disposition on record) was **true** at baseline. A probe-based check prints
   `STALE r43-O`, `STALE r43-C`, `FRESH r43-Ca` — the positive regression plus its negative
   control. The durable gate is still owed; §4.3 pins the contract.
7. **A freshness gate that claims to parse free prose is theater.** The `before` field is a
   sentence, not a query. The only mechanically honest shape is a per-claim probe
   declaration (`before_checks`: clause → probe → the state that makes the clause true) that
   the gate executes at the baseline commit. The r43 C `before` proves why: its first clause
   ("myth-symbol 26") was true and its second ("lithic slot named but unbuilt") was false —
   a gate that averages clauses, or greps one keyword, gets both the flag and the reason
   wrong. Ca01's design must be checked against this, not accepted on its filename.
8. **Admission candidate: NOT ADMITTED at this cut.** O can be admitted only after the body
   lands at the claim path and a post-landing `--selftest`/`--census`/parity re-run is
   filed; C has a drafted entry on the **carried** gap, a fresh gap with **no draft**, no
   C03/C04 audit and no landing; Ca has a scratch prototype with a **red selftest**, no
   durable gate and no filed demonstration. If the wave lands all three before close, the
   per-axis candidate is O improved / C improved / Ca improved with no axis harmed; if any
   artifact stays absent, the r42/r43 honest-stop template applies. §5 states both branches
   per axis.

---

## §1 — Window, state pins, and what "first-hand" means here

| pin | value | command |
|---|---|---|
| lane HEAD / declared baseline | `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d` / `c9f4eaa` | `git rev-parse HEAD`; `claims.json:7` |
| working tree | only `?? reports/round-44/` untracked; no tracked modification | `git status --porcelain` |
| corpus total | **223** | `find corpus/knowledge -name '*.md' \| wc -l` |
| partition vector | `25 / 26 / 25 / 29 / 24 / 94` (linguistics, myth-symbol, culture-material, synthesis, verification, civilizations) | `for d in corpus/knowledge/*/; do ls "$d"*.md \| wc -l; done` |
| corpus README | revision **2.4**, `Total knowledge entries: 223.`, footer `dir_totals [25,26,25,29,24,94]`, sha256 `7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd` | `grep -n '^revision:\|^Total knowledge entries' corpus/README.md`; `tail -6`; `sha256sum` |
| sweep baseline | exit 0, `rows 223 files 223`, `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, `footer_ok True` | `python3 -B reports/round-28/readme/sweep.py` |
| r42 witness | sha256 `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1`; `--selftest` 8/8; `--census` `2556/166/2/5/1` | `sha256sum`; both modes |
| r43 O09 body | 515 lines, sha256 `43ce341f…ad64`; `--selftest` 27/27; four-class `2556/166/0/7` +1 glob | `sed -n '356,870p' reports/round-43/op/O09-scribe.md`; both modes in `.scratch/s01` |
| r43 baseline probe | resolver exists at `7ceff59` (`d8d23a26…`); `myth-symbol` has 26 files incl. `mineral-stone-symbolism.md`; `reports/round-43/` absent | `git show 7ceff59:… \| sha256sum`; `git ls-tree --name-only 7ceff59 corpus/knowledge/myth-symbol/` |
| freshness tool | **absent** — `tools/harness/claims-freshness.py` does not exist; no harness/gate script performs a claims-premise check | `ls tools/harness/`; `grep -rn 'freshness' tools/harness tools/gates --include='*.py'` → only the frozen r22 projection-freshness string |
| r44 declared digests | `claims.json` `5bd54b71…`, `targets.json` `1f73f172…` (per telemetry) | `sha256sum`; `telemetry/dispatch-declared.json` |

"First-hand" means opened or executed by this seat in the window above. Sibling figures are
attributed where they appear and were not re-derived; where sibling and this seat disagree,
both are printed. The one notable divergence is already resolved: O02 and O03 both record the
D1 over-capture as a fixed code path with **zero present incidence**, which is the reading this
seat's fixture supports.

---

## §2 — Claim O (operability): the successor authority

### 2.1 What is under test, and what is actually on disk

The claim pins `reports/round-43/op/O09-scribe.md:356-870` as the body and
`tools/harness/basename-couples-resolver.py` as its target. Extraction and identity:

```
$ sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/s01/basename-couples-resolver.py
$ wc -l .scratch/s01/basename-couples-resolver.py
515
$ sha256sum .scratch/s01/basename-couples-resolver.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64
```

The fence boundaries are `:355` (````python) and `:871` (````); the extract starts with
`#!/usr/bin/env python3` and ends with `sys.exit(main())`, no backticks included. O02
independently re-extracted with `awk 'NR>=356 && NR<=870'` and got a byte-identical file
(`op/O02-verify.md:57-67`); O03 and O07 report the same digest.

**Not on disk:** `tests -e tools/harness/basename-couples-resolver.py` is false at `c9f4eaa`.
The tool is a verified draft. This is the single largest integration fact in the round: the
claim's `after_required` names a durable path, and durability is not established until the
apply. The r43 rejection was about a stale `before`; this round's O must not repeat the mirror
error by treating a scratch-verified body as a landed instrument.

### 2.2 What the body fixes — the defect matrix, with the latency qualifier

| # | live witness defect | successor behavior | verdict | evidence |
|---|---|---|---|---|
| D1 | blank line does not terminate the field (`couples-reference-extractor.py:63-65`, `continue`) | `saw_blank`; indentation branch requires `not saw_blank or soft_wrap`; blank always reaches `break` | **FIXED** (code path) | O09 `:422-433`; `op/O03-defects-verify.md` §2; this seat's fixture |
| D2 | glob fragment checked after direct/unresolved/fallback/ambiguous | `GLOB_FRAG_RE` wins before the slash, basename and ambiguous branches | **FIXED** | O09 `:499-514`; O03 §3 (injected two-hit/one-hit indexes) |
| D3 | no ambiguous selftest control | S3a/S3b, synthetic two-hit index, both candidates listed, never guessed | **PRESENT** | O09 `:724-726`; O03 §4 |
| D4 | no indented-prose control | S7c (plus S7a/S7b) | **PRESENT** | O09 `:757-770`; O03 §5 |
| D5 | six buckets, no four-class census | `four_class_totals` + `artifact_totals` + `conservation` | **PRESENT** | O09 `:609-617`; O03 §6 |
| D6 | no disposition leg | per-token `disposition` + `reason` + `c12` for unresolved/ambiguous/glob rows | **PRESENT** | O09 `:538-571,595-605`; O03 §6 |

**D1 honesty qualifier (binding on the filed prose).** This seat reproduced the over-capture
by loading the witness as a module:

```
fixture: "- couples: myth — `sound-symbolism.md`\n\n  Indented prose naming `prose-token.md`…\n- sources: …"
witness couples_block -> ['myth — `sound-symbolism.md`', 'Indented prose naming `prose-token.md` …']
witness join_parts     -> 'myth — `sound-symbolism.md` Indented prose naming `prose-token.md` …'
```

So the code path is real. But O03's whole-corpus differential shows **0** current entries
affected, **19** entries structurally exposed (couples last), and **0** entries with the
triggering shape. Any LOG/SHONEN sentence must say "latent trap closed", not "over-capture
corrected corpus-wide". The claim's own `before` says "it over-captures blank-line-separated
indented prose" — true as a code-path statement, false as a present-count statement.

### 2.3 Measured census, reproduced three ways

This seat's run (from `.scratch/s01`, which has no `corpus/` ancestor other than the real repo
root):

```
$ cd .scratch/s01 && python3 -B basename-couples-resolver.py --selftest
… 27 PASS lines …
SELFTEST OK: 27/27 controls          # RC=0

$ python3 -B basename-couples-resolver.py --census
entries=223 refs=2730
  policy four-class: direct=2556 fallback=166 ambiguous=0 unresolved=7
  artifacts (excluded from the four-class totals): glob-fragment=1
  conservation: True (sum=2730 refs=2730)
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  fallback mappings (50 distinct): … 50 rows …
  unresolved (7 rows): 5 declared-prospective-seed + 2 dangling-reference
  ambiguous (0 rows):
  glob-fragment (1 rows): -gate.md … extractor-artifact c12=not-applicable
  misaligned: none
RC=0
```

O02 independently folded the JSON `entries_detail` rather than trusting the totals
(`op/O02-verify.md` §4.1): 223 records, `sum(len(tokens)) = 2730`, class fold
`{direct 2556, fallback 166, unresolved 7, glob-fragment 1}`, fallback occurrence sum 166 =
fallback class count, 50 distinct mappings, no missing reason, no null mapping, no unknown
class, `misaligned []`. The 25 entries with zero tokens are entries with no `- couples:`
field, not dropped tokens. Determinism: three plain runs byte-identical
(`87ef57d5…`), two JSON runs identical (`f53899ea…`).

O10 went further and re-implemented the policy fold **without importing the body**
(`op/O10-census-verify.md` §2): raw `.md` matches after brace expansion **2733**, per-entry
distinct **2730**, classed **2730**; the 3-occurrence reduction is the policy §1 per-entry
dedup (three duplicated tokens listed), not a drop. Per-entry agreement with the tool:
**223/223, 0 mismatches**. **O10's caveat is binding:** the tool's `conservation: true` is
tautological (`refs = sum(totals.values())`, then `sum(four)+sum(artifacts) == refs`), so it
cannot detect a token that was never extracted. The zero-drop evidence is the independent
extraction and the 223/223 per-entry comparison, not the flag. The filed artifact should
carry `extracted_tokens: 2730` or the population digest (`444ff801…`), not only
`conservation: true`.

**Arithmetic conventions the artifact must state:** the four-class sum is **2729**; the glob
artifact is excluded by policy §5.6 and brings the conservation total to **2730**. A reader
must not have to guess why both numbers appear. The successor's `--census` text prints both;
the filed JSON must carry both `four_class_totals` and `artifact_totals` (O06 does), plus the
independent-extraction receipt O10 requires.

### 2.4 Parity with the six-class witness (O07)

Same input (223 paths, 2730 refs), both tools, one process:

```
class-pair table (witness -> successor):
  direct         -> direct        2556
  fallback       -> fallback       166
  glob-fragment  -> glob-fragment    1
  prospective    -> unresolved       5
  unresolved     -> unresolved       2
token/detail diffs after documented subclass mapping: 0
fallback mapping mismatches: 0
entries with zero couples tokens: 25
conservation witness 2730 == successor 2730
```

The only differences are the two documented separations: (a) `prospective` folds into
`unresolved` with a named disposition; (b) the glob fragment is quarantined as an artifact.
Live `ambiguous = 0` on both, so ambiguous parity is 0 = 0 and rests on the successor's
control, not on a corpus row. Wrapped-field identity: both tools return the same four tokens,
with `prosody.md` / `toneprosody.md` never appearing. `op/O07-parity.md` §5.

### 2.5 Witness demotion without touching bytes

- `sha256sum tools/harness/couples-reference-extractor.py` before and after every O-seat run:
  `d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1` — unchanged
  (also confirmed at `7ceff59` by `git show … | sha256sum`).
- Demotion is **by record**: O04 fixes five checkable clauses
  (`op/O04-witness-demotion.md` §2): (W1) the census authority is the successor only;
  (W2) the authority neither imports nor shells out to the witness; (W3) the witness digest
  is pinned in every later citation; (W4) the witness stays live as an independent
  six-bucket cross-check; (W5) its `prospective`/`glob-fragment` are witness buckets, never
  policy classes. The successor's docstring already says the predecessor "remains the N6
  regression witness" (`O09-scribe.md:362-364`), so the record and the bytes agree.
- O04 records that only filed runners invoke the witness
  (`reports/round-42/run-validation.py:94-99`, `reports/round-43/run-validation.py:64-66`),
  both uneditable; nothing under `tools/` imports it (`rg` → no hits). The demotion wording
  must appear in the r44 `LOG.md` entry, the parity receipt, and the census artifact's
  `filing.witness` field. Do not rename, delete, shim or re-export it.

### 2.6 Integration findings that must not be lost (all non-blocking for the pinned bytes)

1. **`--census --json` hardcodes `"round": 43`** (O09 `:461`; O02 §4.2, O03 §7.2, O07 §7,
   O08 N2, O10 §6.2). Landing the body byte-exact means a round-44 artifact produced by it
   carries `round: 43`. Do **not** edit the body. File a wrapper artifact whose header pins
   `round: 44`, `baseline_commit: c9f4eaa`, `entries: 223`, `tool.path:
   tools/harness/basename-couples-resolver.py`, `tool_sha256: 43ce341f…`, and
   `tool_emit_round: 43` — with the tool's verbatim JSON embedded under `tool_emit` and its
   `round` key untouched. O06's draft artifact already has this shape.
2. **Root-shadow hazard, observed twice with opposite signs.** (a) O07 ran the resolver from
   `.scratch/o07/`, a full repository snapshot with a **212-entry** corpus, and silently got
   `entries=212 refs=2508 direct=2337 fallback=163`; that run is discarded. (b) X00 measured
   the inverse: a **corpus-only** scratch root (223 entries, no lane-root files) reads
   `direct=2536 unresolved=27`, because 20 Tier-1 `${LANE}/<token>` refs (`AGENTS.md` ×11,
   `SKILL.md` ×2, `LOG.md` ×1, `corpus/README.md` ×2, `SCORECARD.md` ×1,
   `reports/round-20/readme/*.md` ×3) vanish. The selftest does **not** catch either
   (`cross/X00-connector.md` §1.2). The default text output prints no resolved root. **Rule:**
   run from the repo root after landing, or from a scratch directory whose only
   `corpus/knowledge` ancestor is the real root, and assert `KNOW == <repo>/corpus/knowledge`
   before trusting any census.
3. **S1a is corpus-coupled.** The selftest asserts its embedded fixture equals the live bytes
   of `corpus/knowledge/linguistics/phonetics-phonology.md` (`:627-638,:677-681`). Any future
   edit to that entry's couples block turns `--selftest` red. That is a deliberate drift
   alarm, but it means "durable" does not mean "corpus-stable". C's landing does not touch
   that entry; confirm the C draft's `couples:` targets before applying.
4. **Denominator ordering (binding, X00 §1.3, O08 N3).** The claim's `before` and the census
   pin 223; C's landing would make the live total 224. If the census artifact is generated
   after C lands, its `entries`/`refs` will not equal `223/2730`. Recommended order: land O,
   run and file the 223 census **before** C's corpus apply, then measure C's effect as a
   later delta: `entries=224`, `refs=2730+N` where `N` is the new entry's per-entry distinct
   couples tokens; record `post_landing_check` in the same artifact and in C03/C05's audit.
   Do not hand-edit 223→224 and do not file a second census JSON.
5. **Blueprint docstring overclaims an exception.** O09's comment says a blank line
   terminates "unless the previous part ends in a hyphen soft wrap"; `soft_wrap` is defined
   with `and not saw_blank`, so after a blank line the exception is unreachable (O03 §7.1;
   X02 §8.2; fixture `tone-` / blank / indented `prosody.md` → `[]`). Behavior is the safe
   one and the corpus has 0 blank-separated continuations. Record it in the successor record;
   do not edit the pinned body.
6. **The census payload lacks `baseline_commit`** (O10 §6.2). The tool does not emit it and
   must not be edited to add it. The filing wrapper must add `baseline_commit`, `date`,
   `measured_root`, and the `state_note` ("pre-C-landing; measurement commit c9f4eaa;
   entries 223; claim C lands 224 as a later delta"). **R01-44-02:** O06's corpus
   fingerprint does not pin the 20 lane-root direct refs (8 tokens: `AGENTS.md` ×11,
   `SKILL.md` ×2, `LOG.md` ×1, `corpus/README.md` ×2, `SCORECARD.md` ×1,
   `reports/round-20/readme/*.md` ×3), so a corpus-only replay reads 2536/27. Add
   `measured_root` plus the lane-root digests or a full-token digest.
7. **The r43 O09 integration sequence contains a forbidden path** (O08 N1): its step at
   `reports/round-43/op/O09-scribe.md:882` writes
   `reports/round-43/calib/couples-census-r43.json`. Do **not** follow that line in r44; the
   shared rule bars writes to `reports/round-1..43/**`. Retarget to
   `reports/round-44/calib/couples-census-r44.json` (O06/X00 name).
8. **The r43 O12 gate's allowlist must be re-scoped** if reused (O08 N4): it allows
   `reports/round-43/` + `tools/harness/`; an r44 reuse must allow `reports/round-44/`.
   No runtime effect on the body (zero write calls), but a copy-paste would fail or
   mis-report.
9. **The queue row `r39-ic05-resolver-durability` is closed by an r44 successor record**
   (O08 N5; O09 §7), not by editing `reports/round-40/op/defect-queue-v2.json` (tracked,
   currently clean).
10. **Do not take numbers from O09's scribe summary** (R01-44-08): it says 18 entries carry
    `AGENTS.md` (measured 11) and lists `tempfile` as an import (the body imports
    `__future__, argparse, glob, hashlib, json, os, re, sys`; no `tempfile`). Use O02, O03,
    O06, O07, O08, O10 and this draft's measured pins for figures. O09's structure and
    integration order are still useful; its arithmetic is not the authority.

### 2.7 Verdict candidate (O)

- **`improved`** only if the body is applied at `tools/harness/basename-couples-resolver.py`,
  a post-landing `--selftest` is 27/27 from that path, a post-landing `--census` reproduces
  `223/2730` and `2556+166+0+7+1`, the 50 mappings and 7 dispositions are in the filed
  artifact, the parity receipt names the witness, and the r42 digest is still `d8d23a26…`.
- **`unprovable-but-better`** at this cut: the body is verified in seven independent seats'
  copies plus this one, but the durable path is empty. A scratch run is evidence about the
  body, not about the lane.
- **`harmed`** if a second resolver path is minted, if the r42 witness is edited/renamed, or
  if the census artifact is filed with a 212/2508 shadow read or an unexplained 2729/2730
  convention.

---

## §3 — Claim C (coverage): the fresh-gap contract

### 3.1 The claim and its precondition

The claim is `+1` on a **freshly verified unowned gap** at total 223 → 224, with a new entry
under the partition's naming + entry contract, audits pre-landing, a collision check against
the live partition, README rev 2.5 sweep-green 224 == 224, and zero overwrites. The r43
lithic claim was blocked because its topic was owned; the correction is procedural, not
rhetorical: **this round must not carry a gap forward from any prior round.**

### 3.2 Live baseline, measured at this seat's cut

```
$ find corpus/knowledge -name '*.md' | wc -l
223
$ for d in corpus/knowledge/*/; do printf '%-18s %s\n' "$(basename $d)" "$(ls "$d"*.md | wc -l)"; done
civilizations      94
culture-material   25
linguistics        25
myth-symbol        26
synthesis          29
verification       24
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223
missing_from_index 0
topic_mismatch 0
orphan_rows 0
footer_ok True
readme_sha256 7c788a1d…cdcd
$ grep -n '^revision:' corpus/README.md | head -1
5:revision: 2.4 — Round-42 myth-symbol expansion (2026-10-19): …
```

At this cut **two gap artifacts and one entry draft exist; no landing does.** K02 and K04 ran
independent sweeps at 223 and named different gaps; C01 drafted K04's; C05 cleared that exact
slug; C06 reproduced the ownership tests. **C02's README diff, C03's source audit and C04's
contract audit have not landed**, and no corpus byte has moved. Naming a topic without a sweep
is the exact r43 failure mode; naming one **with** a sweep is the precondition, not the
landing — and the choice between the two named gaps is still open (§3.2b).

### 3.2b The two candidates — and why the choice is load-bearing

Two independent scouts swept the same 223 tree and named **different** gaps. The claim is
`+1` only; landing both is the r42 duplicate-topic failure. The integrator must choose, and
the choice changes the partition, the entry draft, the README delta and the post-C census
delta.

| | K02 (cartography) | K04 (dream / vision / trance) |
|---|---|---|
| path | `culture-material/cartography-and-mapmaking.md` | `myth-symbol/dream-vision-trance.md` |
| demand | tight cartographic footprint **7 files / 9 lines**; 29 files on a looser pattern, mostly metaphor | union **52** (K04) / **61** (C01's wider regex) distinct files, by-product |
| topic-owner hits | **0 owners**; 11 hits each dispositioned (metaphor, verb, or a neighbour's register) | 2 adjacent hits, both explained (`divination-omen-systems.md` reading technology; `mongol.md` lexical) |
| prior-round status | **fresh** — not named in r19/r35/r39/r40/r42/r43 registries; global report grep finds 7 hits, none a proposal | **carried** — r42 K02 R2 names the same complex (`reports/round-42/scout/K02-myth-gaps.md:216-260`) |
| filename / sort | free; sorts between `calendar-festival-systems.md` and `costume-semiotics.md` | free; sorts at position 11, between `divination-omen-systems.md` and `eschatology-world-end-systems.md` |
| draft status | **none** — C01 drafted the dream entry, not this one | **drafted** (`cov/C01-entry-draft.md`), collision-cleared (`cov/C05-collision.md`), reproduced (`cov/C06-scribe.md`) |
| claim fit | satisfies "fresh sweep, not carried"; lacks a draft/audit | satisfies the ownership test; **fails the literal "not carried" clause** unless the integrator records an exception |
| readme delta | culture-material 25 → 26; total 224; vector `[25,26,26,29,24,94]` (K02 §3, C02 arithmetic to re-derive) | myth-symbol 26 → 27; total 224; vector `[25,27,25,29,24,94]` |

**The conflict is not a collision — both topics are unowned.** It is a *freshness* conflict:
K02's registry screen rejects the dream gap as carried, while C01's draft argues "not
carried" means "not landed" (r42 ranked R2 but never wrote it). The claim's words are
"verified by a fresh absence sweep at the 223 total, not carried from a prior round" — the
safer reading is K02's, because the r42 scout already named the exact complex. If the
integrator lands the dream entry, the round record must name the exception and its reasoning;
if it lands cartography, a new entry must be drafted and audited before bytes move. **Do not
let the already-drafted path decide the claim by convenience.**

#### K04's candidate, measured

K04 (`scout/K04-gap-verify.md`, observation `2026-10-19T17:22:20Z`) proposes
`corpus/knowledge/myth-symbol/dream-vision-trance.md` and measures, at `c9f4eaa`:

| test | K04 measurement | reading |
|---|---|---|
| demand | union of `dream*`, `trance*`, `ecsta*`, `shaman*`, `incubat*`, `vision quest/visionary` → **52/223** distinct files | the corpus uses the domain widely, as by-product |
| topic-owner test | `grep -rilE -- '^- topic:.*\bdream' …` → 1 (`divination-omen-systems.md`, one of fourteen technique rows); `trance` 0; `ecsta*` 0; `vision quest/visionary` 0; `shaman*` 1 (`mongol.md`, lexical); strict possession phrases → 3 adjacent, none owning | **no owner of the state/induction system** |
| heading test | 2 hits: `divination-omen-systems.md:1` (dreams as a reading technology); `australia-aboriginal.md:36` (ancestral Dreaming, a different sense) | no section owns the experience or its institution |
| filename collision | `find corpus/knowledge -type f \| grep -iE 'dream\|trance\|vision\|ecsta\|shaman\|incubat'` → no output | slug free in every partition |
| sort position | `LC_ALL=C sort` → line 10 `divination-omen-systems.md`, **11 `dream-vision-trance.md`**, 12 `eschatology-world-end-systems.md` | README row goes between those two |
| neighbour boundaries | divination owns the *reading* (`:3,:56,:64,:89,:126,:147-158`); ritual-liminality owns the rite grammar and the permanent-specialist slot (`:5-6,:39-40,:111`); animal-symbolism owns spirit helpers (`:8,:53,:57`); music-instrument owns the drum (`:96-100`) | the entry must own the **state, induction, training and licensing**, and name the Australian Dreaming distinction |
| source shelf | in-corpus: Eliade 1951/Harner 1980 at `animal-symbolism.md:8,:57`; Artemidorus/Gardiner/Oppenheim at `divination-omen-systems.md:12`; Dodds 1951 at `:186`; van Gennep/Turner at `ritual-liminality.md:5-6`; talking drum at `music-instrument-lexicon.md:100`; restricted-knowledge rules at `myth-consistency-gate.md:34`, `real-world-inspiration-boundaries.md:97` | authorable without fabricating; modern specialists (Bourguignon, Winkelman, Lambek, Csordas, Vitebsky) are **0 files** and must be marked `(to-verify)` or omitted |
| not a carried premise (K04's reading) | r42's K02 proposed the same topic as R2 but it was not landed; the file is absent at `c9f4eaa`; the sweep is re-run at 223 | K04 reads this as fresh (**not landed ≠ not named**); K02 reads the same fact as **carried** and rejects it — the integrator must adopt one reading and record it |

**Residual risks the draft must handle:** (a) the thin modern shelf — the entry must build
from the in-corpus anchors and mark anything unretrieved `(to-verify)`; (b) the Australian
ancestral Dreaming is not the dream-state complex and the entry must say so explicitly;
(c) the entry's `couples:` block adds tokens to the census — measure, do not assume.

**Measured post-C delta for C01's draft (this seat, on the fenced body):** the body is
`cov/C01-entry-draft.md:109-394` (286 lines, sha256 `59798ff5…eb89c`); `couples_block()` returns
**1 part**, and `field_refs()` returns **15 distinct tokens**, all explicit
`corpus/knowledge/...` paths (Tier-1 direct). So if this exact draft lands:
`entries=224`, `refs=2745`, `direct=2571`, `fallback=166`, `ambiguous=0`, `unresolved=7`,
`+1 glob = 2745`, conservation true. That is a measurement of the draft, not of a landed
entry — re-run after apply. (X01's 36–44 figure was measured on r42 landings, not this draft;
do not use it as `N` here.) The cartography path has no draft, so its `N` is unknown.

#### K02's candidate, measured

K02 (`scout/K02-gap-scout.md`, same window) proposes
`corpus/knowledge/culture-material/cartography-and-mapmaking.md` and measures, at `c9f4eaa`:

| test | K02 measurement | reading |
|---|---|---|
| filename test | `find … -iname '*cartograph*' -o -iname '*mapmaking*' -o -iname '*portolan*' -o -iname '*cadastr*'` → **0** | no filename owner |
| topic-line test | 11 hits, all dispositioned as metaphor/verb/source-map: e.g. `dialect-faction-map-workflow.md` (verb), `sacred-topography-pilgrimage.md` (place register), `purity-pollution-boundary-systems.md:4` ("boundary map" metaphor), `africa-primary-sources.md:2` ("source map") | **0 owners of mapmaking as a subject** |
| heading/body footprint | tight pattern → **29 files / 35 lines**; genuine cartographic footprint **7 files / 9 lines**, all by-product or explicit handoff | low raw demand, stated not hidden |
| the partition's own charter | `cosmology-cosmography.md:71` ("T-O diagrams are symbolic, **not survey maps**"), `:102` ("not cartographic") | cosmography **explicitly disclaims** the survey-map register — the same "named but unbuilt" shape as the lithic gap |
| nearest neighbours | cosmology (world models), sacred topography (routes), direction (orientation), architecture (city plan, `:95` groma/cadastral), writing-media (surfaces), transport (routes), Mesoamerican primary sources (lienzos) | the new entry owns the **measured, projected, reproduced sheet**; it couples to, not restates, those six |
| prior-round screen | r19 gaps (no row), r35 CM-1..CM-9/MS-1..MS-9 (no row), r39 verification G1–G4 (no row), r40 linguistics E1–E4 (no row), r42 K02 R1–R4 (no row), r43 (O only); global report grep → 7 hits, none a proposal | **fresh at HEAD** |
| sort position | between `calendar-festival-systems.md` and `costume-semiotics.md` | README row order |
| risks | no draft exists; the entry must be authored and audited; the topic's raw demand is low, so the entry must justify itself structurally (the cosmology disclaimer) rather than by mention count | authoring risk, not ownership risk |

**Integration consequence:** if the integrator chooses cartography, C01's dream draft becomes
a spare (r42 precedent), C05's clearance of the dream slug does not cover the cartography
path, and C03–C05 must be re-run against the new draft. If the integrator chooses dream, the
round record must name the carried-gap exception and K02's screen as a dissent. Either way,
**one** entry lands and the other path stays absent.

### 3.3 The preconditions a lawful landing must satisfy (integrator checklist)

1. **Fresh absence sweep at 223**, run at `c9f4eaa`, with commands and outputs in the scout
   fragment. **Two scouts landed and named different gaps:** K02 (cartography) and K04
   (dream/vision/trance). Both measured ownership at 223; they tested different candidate
   sets, so they are not in conflict on any single topic — but the claim is `+1` only. The
   test is **not** "zero grep hits": adjacent by-product hits are admissible only if each is
   explained as non-owning. What must be zero is **owners of the candidate's system**. The
   integrator must choose one gap before any draft is applied; landing both repeats the r42
   duplicate-topic failure.
2. **Filename collision:** `test -e corpus/knowledge/<partition>/<slug>.md` false and
   `find corpus/knowledge -name '<slug>.md' | wc -l` → 0. A free filename is necessary, not
   sufficient; the lithic case proved that. For K04's candidate: absent, and no file in any
   partition carries `dream|trance|vision|ecsta|shaman|incubat` in its name.
3. **Topic ownership:** no existing entry's `- topic:` names the same register. If a hit
   exists, the gap is owned — report the collision, do not route around it.
4. **Draft contract:** the entry carries the established head block (`- gap filled:` with the
   sweep, `- topic:`, `- sources:` with resolvable in-repo anchors, `- couples:`, `- verified-at:`,
   `- recheck:`, `- scope:`), states calibration status for every framework it uses, makes no
   canon claim, and names the handoff target (`corpus/QUALITY.md:1-19`).
5. **Audits pre-landing:** C03's source audit (every backticked in-repo path resolves, every
   line number real), C04's contract audit (QUALITY pass/fail per clause), C05's independent
   collision verify. A post-apply audit does not satisfy the claim.
6. **Apply as `A`, not `M`:** after the integrator applies, `git status --porcelain -- corpus/`
   shows exactly one new file plus `corpus/README.md`; if a tracked entry shows `M`, stop and
   restore from HEAD (the r42 overwrite incident is the precedent).
7. **Sweep after apply:** `rows 224 files 224`, `footer_ok True`, `missing_from_index 0`,
   `topic_mismatch 0`, `orphan_rows 0`, exit 0. A predicted sweep reading is not evidence
   (`readme-prediction-vs-delivery`).

### 3.4 README rev 2.5 — the exact contract, and two carried defects

- Revision line prepended above the current `:5` rev-2.4 block, naming the round and the one
  entry; `## <partition>/ (N+1)` section header; the new row inserted in **filename order**
  with its text **byte-equal** to the entry's own `- topic:` line (continuations space-joined);
  `Total knowledge entries: 224.`; footer `(total 224 files; directory totals …)` with the
  landing partition incremented in the fixed order
  `linguistics, myth-symbol, culture-material, synthesis, verification, civilizations`.
- **For K04's candidate the concrete delta is:** `## myth-symbol/ (26)` → **`(27)`**
  (`corpus/README.md:205`), totals `223` → **`224`** (`:544`), footer
  `[25,26,25,29,24,94]` → **`[25,27,25,29,24,94]`** (`:548`), and one new row between the
  `divination-omen-systems.md` and `eschatology-world-end-systems.md` rows. The row text
  must equal the entry's `- topic:` line byte-for-byte; the sweep's `topic_mismatch` check
  is exact.
- **For K02's candidate the concrete delta is:** `## culture-material/ (25)` → **`(26)`**,
  totals `223` → **`224`**, footer `[25,26,25,29,24,94]` → **`[25,26,26,29,24,94]`**, and
  one new row between the `calendar-festival-systems.md` and `costume-semiotics.md` rows
  (K02 §4.1; re-derive against the live section before editing). The same byte-equal topic
  rule applies. `corpus/README.md:5-13` (rev 2.4) carries the wrong prose vector — see below.
- **Rev 2.4 prose defect (live):** the rev 2.4 block says
  "`## myth-symbol/` moved 23 → **26** … the vector 25/23/25/29/24/94 →
  **25/23/26/25/24/94**". That vector sums to **217**, not 223, and it moves the wrong slots;
  the live footer is `[25,26,25,29,24,94]` (sum 223). The sweep does not read revision prose,
  so the defect passes green. C02 was tasked to note it; the rev 2.5 edit should correct the
  vector it writes and may repair the 2.4 sentence **only as part of the touched block** —
  repair is optional, silence about it is not. Do not let a correct footer launder a wrong
  prose vector into the new revision.
- **Duplicated H1 (live):** `corpus/README.md:1` and `:3` both read
  `# kotodama-shokunin corpus index`. This is the carried `R36-README-DUPLICATE-HEADING`
  defect; r39/r42 precedent is **do not repair it in a coverage delta**. Leave it carried.

### 3.5 Verdict candidate (C)

- **`improved`** only if the integrator chooses **one** gap, one `A` entry lands at that
  path, the preconditions above are met for that exact path, sweep is 224 == 224, and audits
  PASS. The cleanest claim fit is **K02's cartography** (fresh, unowned, but undrafted); the
  ready-to-audit path is **K04's dream entry** (drafted, collision-cleared, but carried).
- **`unprovable-but-better`** if the dream draft is filed as a spare/integration candidate
  but the integrator withholds the landing because the carried-gap clause is unresolved.
- **`unchanged`** if no entry lands: the gap(s) are verified unowned, but no draft→audit→apply
  chain completed. The claim's `after_required` is not met; a scout result is not a coverage
  move.
- **`harmed`** if an existing entry is overwritten, **both** gaps are landed, a duplicate
  topic is landed under a new slug, or the README row is not byte-equal to the entry's topic
  (the sweep's topic check is exact). A 224-row sweep green with a carried/duplicate topic is
  the r43 failure mode repeating: the sweep checks row↔file and topic text, not
  one-owner-per-topic or freshness.

---

## §4 — Claim Ca (calibration): the pre-dispatch freshness gate

### 4.1 The defect, as filed

R01-43-12 (`reports/round-43/review/R01-review.md:400`): *"The claim texts were not
re-measured at `7ceff59` before dispatch; both stale `before` sentences must not enter
`LOG.md`/`SHONEN.md`."* The r43 validation record confirms the consequence: O FAILED as
declared because a green resolver already existed; C BLOCKED because the lithic slot was
owned. The process gap is mechanical: nothing refused the filing of a claim whose `before`
was already false.

### 4.2 The regression, re-measured by this seat

Probes (scratch script, `.scratch/s01/freshness-demo.py`; no durable status):

```
$ python3 -B .scratch/s01/freshness-demo.py 7ceff59
baseline=7ceff59 (r43 declares 7ceff59; r44 declares c9f4eaa)
STALE r43-O    clause='no durable instrument implements the policy' evidence=0
STALE r43-C    clause='lithic slot named but unbuilt (myth-symbol 26)' evidence=26
FRESH r43-Ca   clause='no per-finding disposition on record' evidence=False
FRESH r44-O    clause='no four-class census authority exists' evidence=False
FRESH r44-Ca   clause='no mechanical freshness check exists' evidence=False
GATE_RC=1
```

Supporting facts:

```
$ git show 7ceff59:tools/harness/couples-reference-extractor.py | sha256sum
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1  -
$ git ls-tree --name-only 7ceff59 corpus/knowledge/myth-symbol/ | wc -l
26
$ git ls-tree --name-only 7ceff59 corpus/knowledge/myth-symbol/ | grep -c mineral-stone-symbolism.md
1
$ git ls-tree --name-only 7ceff59 reports/round-43/
(empty)
```

Interpretation: at r43's declared baseline, the O `before` ("no durable instrument") is false
(a durable, selftest-green instrument exists), and the C `before` ("lithic slot named but
unbuilt") is false (the owner file exists). The Ca `before` is true — no pre-r43 disposition
artifact exists; the r43 artifacts live under `reports/round-43/calib/`, which the baseline
tree does not contain. That is the negative control the claim requires. The r44 O/Ca probes
are also true at `c9f4eaa`, so this round's claims are fresh at their own baseline.

X00 independently ran the same regression with typed probes (`cross/X00-connector.md` §2):
`O-p1 {absent: tools/harness/couples-reference-extractor.py}` → actual **present** (STALE);
`O-p2 {count_eq: wrapped live field tokens, expected 0}` → actual **4** (STALE);
`C-p1 {absent: corpus/knowledge/myth-symbol/mineral-stone-symbolism.md}` → actual **present**
(STALE); `Ca-p1 {absent: reports/round-43/calib/dispositions-r38-r39.json}` at `7ceff59` →
`fatal: path … exists on disk, but not in '7ceff59'` → **FRESH**. X00 also proves the r43
claims file was untracked at `7ceff59` (`git cat-file -e 7ceff59:reports/round-43/claims.json`
→ absent), so a gate must read the claims JSON from the worktree while probing the
`baseline_commit` recorded inside it. The two seats' readings agree on all three claims.

### 4.3 The gate contract (what "durable" must mean)

A gate that reads the `before` sentence and guesses is not a gate. The durable shape must be:

1. **Input:** `claims.json` + the `baseline_commit` recorded inside it. Each claim may carry
   `before_checks: [{clause, probe, assert, path/target, expected, evidence_command}]`, where
   `probe` is one of a small closed set (`absent`, `present`, `count_eq`, `sha256_eq`) and the
   probe is evaluated with `git ls-tree` / `git show` at the baseline commit, **never** against
   the working tree. If `before_checks` is absent, the gate must report **`unverifiable`** and
   exit non-zero — refusal is not a pass, and it must not infer freshness from prose.
2. **Semantics per clause, not per claim:** a claim is `stale` if **any** declared before-clause
   mismatches; `fresh` if all match; `unverifiable` if any clause has no probe. The r43 C case
   is the proof: "total 223" was true, "lithic slot unbuilt" was false, and the claim was
   stale. A gate that ANDs, averages, or greps one keyword passes a stale claim.
3. **Exit contract:** exit 0 only if every claim is `fresh`; exit 1 on any `stale` **or
   `unverifiable`**; exit 2 on a malformed declaration or usage/IO. Print per-claim
   `stale|fresh|unverifiable` with the clause, the probe, the observed value, and the baseline
   commit — so the flag names the false conjunct, not just the claim id.
4. **Durability:** lives under `tools/harness/` (the claim names
   `tools/harness/claims-freshness.py` or a documented integrator checklist step), with a
   `--selftest` over the r43 regression + a true-`before` negative control. Not `.scratch`.
   X00 recommends one probe sidecar (`reports/round-44/calib/freshness-probes-r43.json`) plus
   the run output; Ca01/Ca02 own the final names and must not file two competing sidecars.
5. **Filed demonstration:** a round-44 `calib/` artifact containing the r43 run and its
   output, plus the negative control. The artifact names the gate's sha256 and the baseline
   commit. The r43 claims file itself must not be edited.

**Honesty risk to check at review:** Ca01 may produce a gate that special-cases the r43
sentences (string matching "no durable instrument") rather than executing probes. That would
pass the demonstration and fail the purpose. The reviewer must run the gate on a *third*
claim with a different wording and a known false `before` — e.g. this seat's r44-O probe —
and confirm it flags from the probe, not the wording. X01's "theater" trap is exactly this.

**What both reviewers actually measured (R01 §4.2, R02 §0/§4).** A scratch prototype
(`.scratch/ca01/claims-freshness.py`) already exists and gets the r43 regression right:
`[O] STALE (0/2 premises hold)`, `[C] STALE (2/3)`, `[Ca] FRESH (1/1)`, `REFUSE …` and
**exit 2**, reading the baseline through git rather than the worktree. That is the required
positive + negative shape. But it is **not the deliverable**: its own `--selftest` is **red
(17/19)** (`FAIL grep_absent hit fails`; a stale `seventeen checks collected (18)` assertion),
and R02 found a **novel-phrasing false positive** — "the llama-herding register slot is
unbuilt" mines the topic word `register` and refuses against 51 owners. R01's polarity lesson
is the same class of bug: a gate cannot infer polarity from prose; each clause must declare
the measured state that makes it true. A two-string lookup table, a red selftest, or a
`register`-word false positive is **not** improved.

### 4.4 Verdict candidate (Ca)

- **`improved`** only if the durable gate exists under `tools/harness/`, its selftest is
  **green** and covers the r43 O/C stale cases, the r43 Ca / r44 fresh negative controls, an
  `unverifiable` refusal, and an anti-theater mutation (rename the r43 O tool to the existing
  witness; the gate must still flag from capability, not text). The filed demonstration must
  reproduce the reviewers' `STALE/STALE/FRESH` reading and the exit-2 refusal.
- **`unprovable-but-better`** at this cut: the method is proven by the scratch prototype, the
  durable artifact is absent, and the prototype's selftest is red. Both non-author reviewers
  reached this verdict independently.
- **`unchanged`** if the gate remains a `.scratch` script or a prose checklist with no
  executable probe.
- **`harmed`** if the gate greens a stale claim or reds a true one (false positive), or if it
  edits `reports/round-43/**` to make its regression case pass.

---

## §5 — Per-axis verdict candidates

| axis | candidate at close | before → after | evidence |
|---|---|---|---|
| operability | **improved** on byte-exact landing + filed artifact; **`unprovable-but-better`** at this cut (R01/R02 concur) | "six-class witness only; no four-class authority; no disposition leg" → "one durable four-class census authority + 50 mappings + 7 reasoned dispositions + parity receipt; witness demoted by record" | §2; O02/O03/O07/O08/O10; R01 §5; R02 §0; this seat's 27/27 + census re-run |
| coverage | **improved** only if one chosen gap lands with audits; **`unchanged`** at this cut (R01/R02 concur) | 223 → 224 (one `A` entry, README rev 2.5, sweep 224 == 224). Two unowned candidates: K02 cartography (fresh, undrafted) and K04 dream (drafted, carried). The drafted path is not automatically the claim-qualifying path | §3; K02/K04/C01/C05/C06; R01 §3/§5; R02 §3; X01 T2 |
| calibration | **improved** on durable, selftest-green gate + filed regression; **`unprovable-but-better`** at this cut (R01/R02 concur) | "no mechanical pre-dispatch check; r43 filed two stale claims" → "probe-based gate refuses a false `before`; r43 regression + negative control filed" | §4; X00 §2; R01 §4; R02 §0/§4; Ca01–Ca03 pending |
| depth | unchanged | not claimed | `claims.json:16-21` non-goals |
| adjacency | unchanged | no packet/canon/lore surface; A01 PASS at baseline and artifact level, post-landing delta gate at `adj/A01-scope.md:202-263` | `adj/A01-scope.md` §0, §7 |
| freshness | unchanged (paused) | not claimed; `freshness_pause_in_force: true` | `claims.json:21` |

**Named non-author review:** R01 and R02 independently reached the same three verdicts
(O `unprovable-but-better`, C `unchanged`, Ca `unprovable-but-better`) and both report **no
axis harmed** by what is on disk. That satisfies the "unprovable-but-better only with a named
non-author reviewer" condition for the cut; the close-time verdicts still depend on the
integrator's post-landing measurements.

**No axis is harmed by the round as it stands.** The failure mode to avoid is a "green"
coverage or census number that is not measured on the landed tree: 224 rows with a duplicate
topic, or a census filed from a shadow root. §6's legs exist to make those red.

---

## §6 — Landing checklist and runner leg spec

### 6.1 Files the integrator may commit (only when their claim verifies)

| path | source | condition |
|---|---|---|
| `tools/harness/basename-couples-resolver.py` | O09 `:356-870` byte-exact | sha256 `43ce341f…`; post-landing selftest 27/27; `--census` 223/2730 |
| `reports/round-44/calib/couples-census-r44.json` | O06 §5 (exact block) + X00 §3 header | `round: 44`, `baseline_commit: c9f4eaa`, `entries: 223`, `tool_emit_round: 43`, `tool.path` = landed path, `tool_sha256` = `43ce341f…`; four-class + artifact totals; 50 mappings; 7 dispositions; `extracted_tokens: 2730` or population digest; `post_landing_check` filled from the post-C run (never the placeholder 2730/N=0 unless measured) |
| `reports/round-44/op/O04-witness-demotion.md` (filed as-is) | O04 | five demotion clauses W1–W5; no byte edit |
| `reports/round-44/op/O07-parity.md` (filed as-is) | O07 | same input; 0 unexplained diffs; witness digest `d8d23a26…`; add a precise observation time (X02 §8.2 flag 4) |
| `reports/round-44/op/O08-negative-proof.md` (filed as-is) | O08 | 2,921-file no-diff; path-shape floor simulation; N1–N5 |
| `reports/round-44/op/O10-census-verify.md` (filed as-is) | O10 | independent 223/223 per-entry fold; 2733→2730 dedup; tautology caveat |
| `reports/round-44/calib/freshness-r43-regression.json` | Ca01/Ca03 | `stale r43-O`, `stale r43-C`, `fresh r43-Ca`; gate sha256; baseline `7ceff59`; negative control |
| `reports/round-44/calib/process-record-r01-43-12.md` | Ca03 | defect class, owner, evidence, gate as fix; no filed-byte edit |
| **one** of: `corpus/knowledge/myth-symbol/dream-vision-trance.md` (K04, drafted by C01) **or** `corpus/knowledge/culture-material/cartography-and-mapmaking.md` (K02, to be drafted) | C01 draft, audited | **exactly one**; `A` not `M`; topic unowned; audits PASS. The dream path is carried from r42 K02 R2 — landing it needs a named exception; the cartography path has no draft and needs C01+C03–C05 first |
| `corpus/README.md` rev 2.5 | C02 | one row in filename order; totals 224; footer `[25,27,25,29,24,94]` (dream) or `[25,26,26,29,24,94]` (cartography); sweep 224 == 224 |
| `reports/round-44/run-validation.py` | integrator | §6.3 legs; close-time only |
| `reports/round-44/validation.json` | runner (isolated copy) | honest `acceptance_checks_passed` |
| `reports/round-44/telemetry/observed-dispatch.json`, `availability-close-44.json` | S02/integrator | observed route/counts; closing snapshot pinning the declared file's sha256 |

### 6.2 Do not commit

- Any second resolver path, any edit/rename/chmod of
  `tools/harness/couples-reference-extractor.py` (digest must stay `d8d23a26…`).
- Any `corpus/**` change other than the single C entry + `corpus/README.md`; any README bump
  without a landed entry; any repair of the duplicated H1 in this delta.
- Any edit to `reports/round-1..43/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**`,
  fleet `.ufo/**`; any re-freeze of `declared-in-r7`; any packet-surface change.
- Any census artifact generated from a directory with a snapshot `corpus/` ancestor; any
  artifact that omits the 2729/2730 convention.

### 6.3 Runner legs (spec — never executed in-tree by a seat)

- **CO (identity):** `round == 44`, `baseline_commit == "c9f4eaa"`, `seat_count == 32 ==
  len(seats)`, `dispatch.model == "deepseek-v4.1-flash"`, `batched_calls == 1`; record the
  named antigravity→opencode-go deviation with both declared and observed routes.
- **O1 (durability):** the resolver exists at the claim path, has a shebang, imports stdlib
  only, contains no `.scratch` path, does not import or patch the r42 witness or any filed
  r19/r27/r28 instrument; sha256 == `43ce341f…`.
- **O2 (selftest):** exit 0; 27 `^PASS` lines; the wrapped positive is **by identity**
  (`tone-prosody.md` present, `prosody.md`/`toneprosody.md` absent); ambiguous two-hit control
  present; blank+indented prose excluded.
- **O3 (census):** parse the artifact/JSON, not stdout prose. Assert `round == 44`,
  `baseline_commit == "c9f4eaa"`, `entries == 223`, `refs == 2730`, `direct 2556`,
  `fallback 166`, `ambiguous 0`, `unresolved 7`, `glob-fragment 1`, `conservation true`,
  `len(fallback_mappings) == 50`, fallback occurrence sum 166, 7 non-empty dispositions,
  `misaligned == []`, `tool_emit_round == 43`, `tool_sha256 == 43ce341f…`, and either
  `extracted_tokens == 2730` or the independent population digest. Fail if the artifact's
  `tool.path` is not the landed path, if `entries` is 212/224, or if `conservation` is the
  only zero-drop evidence cited.
- **O3b (root identity):** before filing, assert the resolver's `KNOW` resolves to
  `<repo>/corpus/knowledge`; reject a 212/2508 (snapshot) or 2536/27 (corpus-only) census as
  a measurement of the wrong root. The text output prints no root; use the JSON `tool` field
  plus a one-line path assertion (X00 §1.2, O07 §2).
- **O4 (filed-byte guard):** r42 witness `d8d23a26…`, r19 `e7992c32…`, r27 `fb589b28…`, r28
  `9b2ccac0…`, full policy `8c3d7c35…` unchanged.
- **C1 (one lawful entry):** exactly one new file under `corpus/knowledge/<partition>/`;
  zero `M`/`D` under `corpus/knowledge/`; the chosen scout's sweep commands are in the
  artifact and the topic-owner test explains every adjacent hit; `find corpus/knowledge
  -name '*.md' | wc -l` → 224. If the dream path is chosen: `myth-symbol 27`, file
  `dream-vision-trance.md`, no other partition moved, **and the record names the r42 R2
  carry + K02's dissent**. If cartography is chosen: `culture-material 26`, file
  `cartography-and-mapmaking.md`, a fresh C01 draft exists, and C05's clearance has been
  re-run against that exact path.
- **C2 (README):** `revision: 2.5`, the chosen section header (`## myth-symbol/ (27)` or
  `## culture-material/ (26)`), totals line 224, footer `[25,27,25,29,24,94]` or
  `[25,26,26,29,24,94]`, the new row byte-equal to the entry's `- topic:` text and in
  filename order; post-apply sweep `rows 224 files 224`, `footer_ok True`,
  `missing_from_index 0`, `topic_mismatch 0`, `orphan_rows 0`, exit 0.
- **C3 (post-C census delta):** after C lands, re-run the resolver over the 224 tree; assert
  `entries == 224`, `refs == 2730 + N`, and the four-class fold gained exactly `N`, where `N`
  is the new entry's per-entry distinct couples tokens. For C01's current dream draft this
  seat measured **N = 15, all direct** → expected `refs = 2745`,
  `four-class 2571+166+0+7 = 2744`, `+1 glob = 2745`; re-run, do not assert the draft's
  number as the landed number. Record it as `post_landing_check` in the same artifact; do
  not rewrite the 223 identity or file a second census JSON. The cartography path has no
  draft, so its `N` is `to-verify`.
- **Ca1 (freshness):** the gate exists under `tools/harness/`; its selftest is green; run over
  `reports/round-43/claims.json` at `7ceff59` it prints **stale for O and C** and **fresh for
  Ca**; run over a true-`before` claim it does not flag; a prose-only claim with no probes
  prints `unverifiable` and exits 1; the filed demonstration's output matches a re-run.
- **P1 (filed bytes):** compare `corpus/knowledge/**` (except the one C entry),
  `reports/round-1..43/**`, `corpus/lessons/*.md`, `tools/gates/frozen/**` to the baseline;
  any change fails.
- **X1–X4 (governance):** L1 bleed scan (no unnegated promotion/canon/clearance/closure);
  no seat out is 0 bytes; telemetry `declared_artifacts` digests match `claims.json`
  (`5bd54b71…`) and `targets.json` (`1f73f172…`); receipt idempotence (two builds equal).

### 6.4 One-command re-checks the integrator can paste

```
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
git rev-parse HEAD; git status --porcelain
find corpus/knowledge -name '*.md' | wc -l                  # 223 before C; 224 after
python3 -B reports/round-28/readme/sweep.py                  # 223==223; 224==224 after C
sha256sum tools/harness/basename-couples-resolver.py         # 43ce341f… after landing
python3 -B tools/harness/basename-couples-resolver.py --selftest   # 27/27
python3 -B tools/harness/basename-couples-resolver.py --census     # 223/2730
python3 -B tools/harness/couples-reference-extractor.py --selftest # 8/8, bytes untouched
sha256sum tools/harness/couples-reference-extractor.py       # d8d23a26…
```

---

## §7 — SHONEN section (draft for the fleet report)

**What this round actually teaches.**

1. **A verified body is not a landed instrument.** The O09 draft is reproducibly green in
   seven independent seats' copies, but the claim's target path was empty at dispatch. The
   distinction belongs in the record: "verified draft" is evidence about bytes; "durable" is
   evidence about the lane. A claim that names a path must be judged on the path, not on the
   scratch.
2. **Latent defects need latent language.** The blank-line over-capture is a real code path
   and a zero-incidence corpus condition. The successor's value is closing a trap before it
   fires; filing it as a present count correction would import a false measured claim. The
   same discipline applies to the ambiguous control: the corpus has 0 duplicates, so the
   control is the coverage, not a live row.
3. **Parity is a substitution table, not a vibe.** Two tools with different class vocabularies
   agree only when the mapping is written down (`prospective → unresolved`, glob quarantined).
   With that table, the diff is 0; without it, a reader sees 2 vs 7 and calls it a
   regression. File the table.
4. **A freshness gate must execute probes, not read prose.** The r43 C `before` mixes a true
   clause ("total 223") with a false one ("lithic slot unbuilt"). Any gate that averages,
   keyword-matches, or trusts the sentence will mis-flag. The durable shape is a declared
   probe per clause (`absent|present|count_eq|sha256_eq`, evaluated at the recorded baseline
   commit), with `unverifiable` — and a non-zero exit — when no probe is declared, plus a
   negative control that proves the gate can stay green.
5. **The census denominator and the measurement root are part of the census.** 223 vs 224,
   2729 vs 2730, 212/2508 (a snapshot root), and 2536/27 (a corpus-only root) are four
   different truths. Every artifact must pin its tree, its root, its convention, its tool
   digest, and its artifact name, or the next round inherits an argument instead of a
   measurement. One artifact name; a second JSON is a fork.
6. **Carried defects survive correct work.** The README's rev-2.4 prose vector sums to 217
   while the footer sums to 223, and the H1 is duplicated; the sweep is green because it
   reads the footer. A coverage delta must not launder the prose defect just because the
   checked number is right.
7. **A conservation boolean can be tautological.** The tool computes `refs` from the same
   class totals it then sums, so `conservation: true` cannot prove no token was dropped.
   The proof is an independent extraction and a per-entry comparison (O10: 2733 raw →
   2730 deduped → 223/223 entries agree). File the independent count, not just the flag.
8. **A drafted gap is not automatically the claim's gap.** The wave produced two verified
   unowned topics: one fresh (cartography, undrafted) and one carried from a prior scout
   (dream/vision/trance, fully drafted). The draft was ready because it was written first,
   not because it fit the claim; the fresh gap fit the claim but had no draft. A `+1`
   coverage claim needs the freshness clause and the draft to meet on the same topic —
   otherwise the round must name an exception or withhold the landing. Convenience is not
   a selection criterion.

**Honest stop.** At this cut the round is **not admissible**: O is verified but unlanded, C
has a drafted entry on a *carried* gap and a fresh gap with no draft (the integrator must
choose one and audit it), and Ca has a scratch demonstration only. If the integrator lands
the O body and its census artifact, the O axis is improved; C and Ca decide their own axes.
No axis is harmed by what is on disk — but a green 224 sweep over the carried gap would be a
false green, and a dream landing without the named exception would enter `LOG.md` with an
unmeasured premise.

---

## §8 — Owed / to-verify

- **Landed at this seat's final cut** (`find reports/round-44 -type f`, 25 files):
  `adj/A01-scope.md`, `cov/C01-entry-draft.md`, `cov/C05-collision.md`,
  `cov/C06-scribe.md`, `cross/X00-connector.md`, `cross/X01-trades.md`,
  `cross/X02-honesty.md`, `op/O02-verify.md`, `op/O03-defects-verify.md`,
  `op/O04-witness-demotion.md`, `op/O06-census-artifact.md`, `op/O07-parity.md`,
  `op/O08-negative-proof.md`, `op/O09-scribe.md`, `op/O10-census-verify.md`,
  `review/R01-review.md`, `review/R02-review.md`, `scout/K01-resolver-scout.md`,
  `scout/K02-gap-scout.md`, `scout/K04-gap-verify.md`, `scribe/S02-telemetry-draft.md`,
  plus `claims.json`, `targets.json`, `telemetry/dispatch-declared.json` and this file.
- **Still absent at the final cut** (declared outs): `plan/P01`, `op/O01`, `op/O05`,
  `cov/C02`, `cov/C03`, `cov/C04`, `calib/Ca01`–`Ca03`. The integrator recomputes
  `find reports/round-44 -type f` at close; an absent file is `could-not-evaluate`, never
  green. Both reviewers require an explicit integrator ruling on the scout conflict; neither
  review substitutes for it.
- **O:** post-landing re-run owed (selftest, census, parity) from `tools/harness/`; the census
  artifact's filing (O06 §5 block + X00 §3 header) owed; O07's receipt needs a precise
  observation time (X02 §8.2 flag 4); the shadow-root guard must be stated in the artifact.
  O06's artifact draft is not yet on disk (`reports/round-44/calib/` is empty).
- **C:** two gaps are verified unowned but the round has **one** slot. K02's
  cartography (`culture-material/cartography-and-mapmaking.md`) is fresh and **undrafted**;
  K04's dream/vision/trance (`myth-symbol/dream-vision-trance.md`) is **drafted** by C01,
  collision-cleared by C05 and reproduced by C06, but **carried** from r42 K02 R2. The
  integrator must choose one, record the choice and (if dream) the carried-gap exception.
  C02's README diff, C03's source audit, C04's contract audit and a C05 re-run against the
  chosen path are all owed. No corpus byte may move before those land; the entry's
  `couples:` tokens set the post-C census delta — measured **N = 15** for C01's current
  dream draft (all direct; expected `refs 2745`), not the placeholder 0; the cartography
  path's `N` is unknown until a draft exists.
- **Ca:** Ca01's durable gate, Ca02's independent run and Ca03's R01-43-12 process record are
  all owed. The filed demonstration must include the true-`before` negative control and an
  `unverifiable` refusal case, not only the r43 stale cases.
- **`to-verify`:** whether the successor's census JSON should gain a `--round` flag in a later
  round (it is pinned now and must not be edited); whether the r43 `D1c` unreachable-exception
  comment warrants a queue row (O03 §7.1); whether the 5 declared-prospective rows should
  stay `c12=blocker` or get a non-blocker code (O06 §7); whether O07's `conservation … ==`
  line is vacuous (X02 §8.2 flag 5) and should be reworded in a successor receipt.
- **Close-time, integrator-owned:** `reports/round-44/run-validation.py`, `validation.json`,
  `telemetry/observed-dispatch.json`, `telemetry/availability-close-44.json`, the fleet
  report, the `LOG.md` entry, the `SCORECARD.md` per-axis rows. This seat ran no runner.

---

## §9 — Citations

- Contract: `reports/round-44/claims.json:1-70` (claims O/C/Ca, dispatch, non-goals);
  `reports/round-44/targets.json:1-45` (shared rules, seat S01 at `:42`).
- Pins: `git rev-parse HEAD` → `c9f4eaa…`; `corpus/README.md:5,544` and footer;
  `reports/round-28/readme/sweep.py` output (this seat).
- O body: `reports/round-43/op/O09-scribe.md:355` (fence open), `:356-870` (body), `:871`
  (fence close); sha256 `43ce341f…`; `op/O02-verify.md` §§1-7; `op/O03-defects-verify.md`
  §§0-7; `op/O04-witness-demotion.md` §§1-5 (W1-W5); `op/O06-census-artifact.md` §§1-7
  (artifact block, 12 invariants, filing order); `op/O07-parity.md` §§1-8;
  `op/O08-negative-proof.md` §§1-6 (2,921-file no-diff; N1-N5); `op/O09-scribe.md` §§0-8;
  `op/O10-census-verify.md` §§1-6 (independent fold, tautology caveat); `scout/K01-resolver-scout.md`
  §§0-5 (landing spec, demotion rules).
- C gaps: `scout/K02-gap-scout.md` §§0-4 (cartography; registry screen; 11 hits dispositioned;
  fresh), `scout/K04-gap-verify.md` §§0-9 (dream/vision/trance; 52/223 demand; 2 explained
  adjacent owners; filename free; sort position 11; shelf and risks),
  `reports/round-42/scout/K02-myth-gaps.md:216-260` (the r42 R2 dream proposal — the carry).
  Draft/clearance: `cov/C01-entry-draft.md` §§1-2 (dream entry, head block, 15-token couples
  block; entry body `:109-394`), `cov/C05-collision.md` §§1-7 (dream slug PASS; target-drift
  caveat; `+1` rule), `cov/C06-scribe.md` §§0-2 (independent reproduction; conditional
  verdict).
- Cross-claim: `cross/X00-connector.md` §1.2-1.5 (root sensitivity, ordering, wrapper),
  §2.1-2.5 (typed probes, r43 regression, negative control), §3 (artifact name), §4 (order);
  `cross/X01-trades.md` §1 T1-T5 (fork, latent D1, round stamp, ownership/freshness, ordering,
  README vector), §2 (token-level anti-fork), §3-4 (theater risk, C ordering); 
  `cross/X02-honesty.md` §§1-4, §8.2 (honesty ledger, flags); `adj/A01-scope.md` §0, §7
  (scope PASS; exact-delta gate; packet digests); `review/R01-review.md` §1/§5 (verdicts),
  §4 (freshness prototype), §6 (integration conditions), §7 (R01-44-01..15);
  `review/R02-review.md` §0 (verdicts), §3.1 (C conflict), §3.2 (draft checks, N=15),
  §8 (late landings); `scribe/S02-telemetry-draft.md`.
- Witness: `tools/harness/couples-reference-extractor.py:63-70` (blank-line `continue`),
  `:134-150` (branch order), `:231-239` (over-capture control); sha256 `d8d23a26…`.
- Policy: `reports/round-42/calib/basename-couples-policy-full.md:24-25,41,58,98-102`
  (four classes, mapping listing, §5.6 glob exclusion).
- Wrapped field: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`;
  `verification/gate-frozen-run-standard.md` (glob token `-gate.md`).
- r43 defect: `reports/round-43/review/R01-review.md:400` (R01-43-12), `:366` (stale
  premises); `reports/round-43/validation.json` (`verdict: rejected-honest-stop`);
  `reports/round-43/claims.json` (O/C/Ca `before`); `LOG.md` r43 entry.
- Regression probes: `git show 7ceff59:tools/harness/couples-reference-extractor.py |
  sha256sum` → `d8d23a26…`; `git ls-tree --name-only 7ceff59 corpus/knowledge/myth-symbol/`
  → 26 incl. `mineral-stone-symbolism.md`; `git ls-tree --name-only 7ceff59
  reports/round-43/` → empty; `.scratch/s01/freshness-demo.py` output (this seat); X00 §2
  typed-probe outputs (independent agreement).
- Corpus contract: `corpus/QUALITY.md:1-19`; `corpus/README.md:1,3` (duplicate H1),
  `:5-13` (rev 2.4 prose vector defect), `:177-320` (partition sections), `:544`
  (totals line); `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md:3-19` (the entry
  contract fields).
- State pins measured this seat (2026-10-19, `c9f4eaa`, `PYTHONDONTWRITEBYTECODE=1`):
  `find corpus/knowledge -name '*.md' | wc -l` → 223; partition loop → 25/26/25/29/24/94;
  `sweep.py` → rows 223 files 223, footer_ok True, exit 0; O09 extract → 515 lines /
  `43ce341f…`; `--selftest` → 27/27; `--census` → 2556/166/0/7 + 1 glob / 2730;
  witness `--selftest` → 8/8, `--census` → 2556/166/2/5/1 / 2730; `ls tools/harness/` → no
  `basename-couples-resolver.py`, no `claims-freshness.py`; `ls reports/round-44/calib/` →
  empty at the final cut.
