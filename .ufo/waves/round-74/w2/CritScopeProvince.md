# CritScopeProvince — round 74, wave 2 — province fit and adjacency of the landed entries

Seat: `CritScopeProvince` (leaf). Attack: PROVINCE fit and adjacency of the two landed
entries — do they stay generative/coupling craft, or drift into lore's world-bible
record keeping / narrative craft; is any sentence a canon decision or rights ruling;
is the handoff obligation stated as pull-based and not active. Verdict per entry with
path:line.

Revisions read: base `f7104cbce186bc2e1522abf0cfd619cc834628bb`, operative freeze
`00c408a0af2fa5ddf65af2224152ce258b26d896` (F3), claim Ca lands
`5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3`, claim C lands and its fix
`c4bf61a8d722f9168ce0fd8021a6261c000610c5`, lane main at dispatch
`1d7add3f7b9eaf6f3349c56c36f6d06325d74236`. Both entry files at the working tree are
byte-identical to `c4bf61a8d` (`git diff --stat c4bf61a8d -- <both entries>` → empty output),
so every line number below is a landed-bytes line number.

Axes this seat walked: **(A1)** province fit of each entry against
`kotodama-shokunin/PROVINCE.md` and `lore-shokunin/PROVINCE.md`; **(A2)** correctness of the
adjacency statements (direction of the handoff, payload types); **(A3)** coherence of the
lane's own boundary/routing documents after the landing; **(A4)** whether any acceptance leg
guards A1–A3. I did not grade quotes, evidence windows, registry rows or counters — those
belong to the citation/evidence/counter seats.

## 0. Run conditions (counters were run only inside my own clone)

```
D=$(mktemp -d /tmp/CritScopeProvince/XXXX)
git -C "$D" init -q && git -C "$D" rev-parse --show-toplevel   # /tmp/CritScopeProvince/GkFW
git clone -q /home/vgpnk/Projects/shokunin/kotodama-shokunin "$D/lane"
git -C "$D/lane" checkout --detach
git -C "$D/lane" branch -f main <lands>
```

Measured:

```
# main = c4bf61a8d (claim C lands)
$ python3 -B reports/round-74/accept-c.py --root . --lands c4bf61a8d... --freeze 00c408a0af2f... --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS ENTRIES … LEG PASS INDEX
ACCEPT-C-74: PASS legs=13/13

# main = 5e4796c0c (claim Ca lands)
$ python3 -B reports/round-74/accept-ca.py --root . --lands 5e4796c0c... --freeze 00c408a0af2f... --fleet-root /home/vgpnk/Projects/shokunin
LEG PASS LEDGER … LEG PASS STAMP
ACCEPT-CA-74: PASS legs=11/11
```

No leg among the 13 (C) or 11 (Ca) reads `PROVINCE.md`, a lane's sibling boundary document,
the handoff contract's direction, or entry prose beyond header shape / `- topic:` text / S-ids /
`source:` lines (the Gate and EVIDENCE legs read the lesson and evidence files, not entry
prose). Measured on the frozen counter bytes:

```
$ for c in reports/round-74/accept-c.py reports/round-74/accept-ca.py; do
    echo "$c PROVINCE=$(grep -c PROVINCE $c) worldbible=$(grep -c worldbible $c) contract=$(grep -c contract $c)"
  done
reports/round-74/accept-c.py PROVINCE=0 worldbible=0 contract=0
reports/round-74/accept-ca.py PROVINCE=0 worldbible=0 contract=0
# the only 'disclos|reveal' matches in accept-c.py are lines 27, 1885, 2872 — the printed
# "lane worktree HEAD (disclosure only)" note and a fixture-receipt message, not entry text
```

So **everything in F1–F3 below is unguarded by the claim's own counters** — the legs can be
green over a province misstatement. Confirmed by the two runs above, not inferred.

**INFO (for the Ca counter seat, not scored against the claim).** The documented run condition
("the clone's local `main` must equal `<lands>`") is load-bearing for Ca. With `main` at a
later commit (`c4bf61a8d`) and `--lands 5e4796c0c`, all data legs and LEDGER…TRACKED passed, but:

```
LEG FAIL RECEIPTS
     rev=2d1cd9140d3a receipts=['accept-c-73=50c60bb67f16', 'accept-ca-73=864c94192854']
     problems=['accept-ca-73 re-run exit=2 (want 0)', "accept-ca-73 re-run did not print 'ACCEPT-CA-73: PASS legs=9/9'",
     'reports/round-74/telemetry/accept-ca-73-at-lands.txt: committed stdout differs from the re-run (55544779204d vs e3b0c44298fc)']
LEG FAIL STAMP
     stamped=evaluated=measured=5e4796c0cb6a tree=83257915923c counter=8052f1e25c36 clone=/tmp/r74-ca-2ttvlqxa/lands
     problems=['measured c4bf61a8d722f9168ce0fd8021a6261c000610c5 != lands 5e4796c0cb6ae56e36a90f6c3b053e91d31a74b3']
ACCEPT-CA-74: FAIL legs=9/11
```

Two things there deserve the counter owner's eye, both **observations**, not verdicts: the
STAMP leg's own header prints `measured=5e4796c0cb6a` while its failure message says
`measured c4bf61a8d…`, i.e. the leg derives "measured" from the **caller's `main`**, not from
the materialized checkout; and the leg text says "produced inside a clone materialized at
`<lands>`". If the intent is that the graded bytes alone fix `measured`, the derivation and
the leg text disagree. My passing Ca run met the documented pin, so the claim's "after" line
is reproducible exactly as the assignment states.

## 1. Verdicts per entry

| Entry | Verdict | Basis (path:line) |
|---|---|---|
| `corpus/knowledge/culture-material/worldbuilding-setting-practice.md` | **IN-LANE** (two residuals, F4/F5) | `PROVINCE.md:9-11` owns "the generative/coupling craft"; the whole entry is reported practitioner method with attribution; `:267` keeps the guard ("No layer assignment, no element count, no depth target and no document layout is fixed for a setting by this entry"); `:13-14` refuse canon and authority; `:265` assigns the decision to lore |
| `corpus/knowledge/culture-material/worldbuilding-setting-practice.amend-2026-10-23.md` | **PARTIAL** — §1–§3 in-lane, §4–§5 partial, §6 defective | in-lane `:15-48` (derivation order = generative craft); **contested slice** `:49-63`, `:65-83` (reader-facing disclosure order: generative half unopposed, verification half is lore's named uncovered method CM-f — F1); defective `:91` and `:12` (handoff stated as active and with a payload type the contract does not define — F2) |

The assignment's direct question — *is the handoff obligation correctly stated as pull-based
and not active?* — answers:

- Base entry `:265`: **not false, but incomplete.** It says "Hand off under
  `synthesis/worldbible-integration-contract.md`: this entry supplies …; lore decides which of
  them a given world adopts, records the canon, and verifies consistency." The decision is
  correctly lore's (the pull side), but the contract's activation gates (lore's scoped brief;
  bilateral acknowledgement pending) are absent. No active delivery is claimed.
- Amendment `:91` and `:12`: **wrong direction.** See F2.

## 2. Findings

### F1 — MEDIUM — the amendment lands the reader-facing side of an axis that only lore's boundary document names, with no scope report

**Attack.** Amendment §4 (":49 One practitioner's stated tolerance…") and §5 (":65 What to do
with it", table `:77-81`) record and turn into design prompts a *release schedule for the
world's rules to the reader* — "is the world's information delivered inside roughly the first
twenty chapters" (`:80`) and the entry's own, unsourced third prompt "is each released rule
attached to a scene that needs it?" (`:81`, acknowledged as "this entry's extension of 逐渐地"
at `:75`). That axis — reveal order — is named as **lore's** uncovered method area in lore's
own boundary document, and by **no** other lane's.

**Evidence.**

1. Fleet-wide ownership sweep — the only PROVINCE in the fleet that mentions this axis is
   lore's, and there it is a debt, not a claim:

```
$ cd /home/vgpnk/Projects/shokunin && grep -rniE 'pacing|reveal order|narrative order|story structure' */PROVINCE.md
lore-shokunin/PROVINCE.md:19:- CM-d in-world source reliability stays `partial` …; CM-f reveal order vs chronology and CM-g kotodama packet intake stay `uncovered`.
lore-shokunin/PROVINCE.md:23:- Pointed at corpus/README.md `## Frontier` (round 103): reveal order vs chronology, …
```

```
$ grep -rn 'reveal' lore-shokunin/corpus/README.md
corpus/README.md:72:| CM-f | reveal (narrative) order vs chronology | uncovered | none — zero governing hits for spoiler/reveal order/narrative order/fabula/syuzhet in knowledge or SKILL (before r103: uncovered) | …
corpus/README.md:78:- CM-f reveal order vs chronology is uncovered: the schema encodes integer ticks only; zero durable-surface hits for narrative/reveal-order terms.
corpus/README.md:90:| reveal (narrative) order vs chronology (fabula/syuzhet) | the schema encodes integer event ticks only; nothing separates reader-facing reveal order from event order, so spoiler/discourse-order errors are uncheckable (CM-f, uncovered) | …
```

   `lore-shokunin/PROVINCE.md:3` is "Owns: fictional-world records — entities …, relations,
   timeline events — with consistency verification"; `:23` is explicitly lore's *frontier*.
   Kotodama's own `PROVINCE.md:3-7` enumerates conlang, myth/symbol, era models, costume &
   material-culture terminology, naming systems — not reader-facing pacing.

2. No scope report exists. `PROVINCE.md:22-25` says "Contested scope → report to the
   integrator, never absorb", and the round's own record has none:

```
$ grep -rn 'scope report\|integrator' corpus/lessons/round-74.md reports/round-74/
(no output)
```

3. The amendment's handoff (`:91`) files the disclosure plan straight into the world bible
   and stops ("this entry ends at that handoff"), naming no receiving method and no dispute.

**Impact.** Kotodama now holds a method slice that lore's boundary document records as its own
uncovered method (CM-f), without the contested-scope report `PROVINCE.md:25` requires. The
harm is bounded, and I record the counterevidence honestly: the amendment refuses the strong
readings (`:13` "asserts no law of the genre" and refuses "a reading of either interview as
evidence about readers"; `:88` "never quotable as a rule of serial fiction"; `:87` "Nothing
here measures readers"), and `:51` frames §4 as a lead. So the defect is **where the recorded
lead is routed**, not that it is stated as a rule — the E1 pre-correction ("worded as one
practitioner's tolerance … not a rule") did land as claimed. Also note the defensible split:
authoring a disclosure plan is generative craft (kotodama), verifying reveal order against
chronology is consistency verification (lore, CM-f, uncovered). The entries state neither
side of that split.

**Smallest safe correction.** One sentence appended to §6 `:91`, no quote or table changed:
"Reveal order against chronology is lore's verification method (its boundary records it as
CM-f, `lore-shokunin/corpus/README.md:72`, still uncovered); a disclosure plan made from this
material is a contested-scope question for the integrator under `PROVINCE.md:25`, not a rule
this lane supplies." Optionally qualify `:81` (the unsourced prompt) as "the entry's own
question, outside the source's say-so".

### F2 — MEDIUM — amendment `:12` and `:91` state the handoff as active and name a payload type the contract does not define

**Attack.** `:91` — "…are records for a world bible, **which
`synthesis/worldbible-integration-contract.md` hands to lore**; this entry ends at that
handoff…" — makes the contract the active hander. Under the contract the transfer is
lore-initiated, gated, and not yet activated. `:12` — "…`synthesis/worldbible-integration-
contract.md` (where a derived ladder and **a disclosure plan become world-bible records** that
lore owns)" — asserts a record slot for a disclosure plan that the contract's payload table
does not have.

**Evidence.**

```
# selected lines from `sed -n '1,20p'` of the contract, annotated (full 20 lines read; quotes verbatim)
:2  - topic: The shared adjacency interface by which kotodama-shokunin hands linguistic-cultural systems to lore-shokunin …   <- the counterexample; same verb
:13 - Canonical contract copy: this file in kotodama-shokunin; lore reads it read-only.
:15 - Initial bilateral acknowledgement is **pending** until those records exist; writing this file is not a substitute for lore's read.
:19 - This contract defines a handoff, not permission to bypass an operator gate.

$ grep -n 'brief\|acknowledg' corpus/knowledge/synthesis/worldbible-integration-contract.md   # output trimmed to the five cited lines
:57 | `producer`, `recipient`, `request_ref` | Kotodama author, lore recipient, and scoped brief or request pointer |
:99 | Workflow state | Draft → submitted → … | Kotodama submits; lore issues disposition; each records its own actions |
:126 1. Lore supplies a scoped brief, baseline bible reference, existing entity/era keys, constraints, canon policy, and the actual authorized receipt surface; …
:129 4. Kotodama submits immutable bytes and a digest manifest, naming lore as recipient. Submission, delivery, and silence are never acceptance.
:136 A transport acknowledgement means only “bytes received”; …
:200 1. Begin with lore's brief; fill each component above …
```

```
$ grep -ci 'disclos' corpus/knowledge/synthesis/worldbible-integration-contract.md
1                      # the only hit is :180 "must disclose which languages …", not a payload type
$ grep -ci 'ladder'  corpus/knowledge/synthesis/worldbible-integration-contract.md
1                      # the only hit is :108 "## 7. Era staging: align records without a universal ladder"
# §5's payload table, 7 artifact rows, compressed (row cells abbreviated; all seven read in full):
## 5. Artifact payloads: systems, lexica, naming ledgers
  System specification | Diachronic specification | Lexicon | Naming ledger | Myth-symbol register | Era-costume matrix | Coupling register
```

So the **derived ladder** has a home (a System specification, `:76`); a **disclosure plan**
does not appear in the payload table at all, and adding one would be a contract-version change
under §9, not an existing slot. And the contract's activation state is lore's own recorded
debt: `lore-shokunin/PROVINCE.md:28` — "`…/worldbible-integration-contract.md` (exists; digest
**unacknowledged by lore** — coverage row CM-g)".

**Impact.** The lane's only boundary statement for this entry tells a reader that the contract
transfers these records to lore now, when the acknowledgement is pending and the intake is
uncovered on lore's side (CM-g). That is the exact active/push reading the contract's §1 and
§8 exist to prevent, and it invents a receiving record type. Severity is not HIGH because the
contract's own `- topic:` (`:2`) uses the same verb "hands", so the sentence is defensible as
title-echo; the omission of the brief/acknowledgement gates is the actual defect.

**Smallest safe correction.** Rewrite `:91` to the contract's own vocabulary: "…are records a
world bible may hold; they are submitted under `synthesis/worldbible-integration-contract.md`
only on lore's scoped brief (§8.1) and its bilateral acknowledgement is still pending
(`lore-shokunin/PROVINCE.md:28`, CM-g); the ladder is a System specification (contract §5). This
entry ends there and records no canon." And in `:12` either drop "a disclosure plan" or say
"a disclosure plan for which the contract currently defines no payload type". Base `:265` can
take the same one-clause addition ("on lore's scoped brief") but is not itself false.

### F3 — LOW — the lane's boundary and routing documents were not updated by the landing, so the lane now holds a method its own province does not name

**Attack.** The claim's own before-gloss is the yardstick: "README.md:6 and SKILL.md:3 frame the
lane domain as linguistic-cultural worldbuilding … but **no file or index row governs setting
practice**". After the landing, that is still true of `PROVINCE.md` and `SKILL.md`.

**Evidence.**

```
$ git diff --stat f7104cbc..c4bf61a8d -- PROVINCE.md
(empty — PROVINCE.md is byte-identical base..C-lands)

$ echo "PROVINCE 'setting' hits: $(grep -ci 'setting' PROVINCE.md)"
PROVINCE 'setting' hits: 0
$ echo "SKILL setting-practice hits: $(grep -ci 'worldbuilding-setting' SKILL.md)"
SKILL setting-practice hits: 0
$ echo "SKILL 'settings note' hits: $(grep -ci 'settings note' SKILL.md)"
SKILL 'settings note' hits: 0
$ git diff f7104cbc..c4bf61a8d -- SKILL.md | grep '^[+-]' | grep -v '^[+-][+-]'
-  `corpus/knowledge/civilizations/` — 94 entries: 92 earlier-civilization
+  `corpus/knowledge/civilizations/` — 95 entries: 93 earlier-civilization
+ | accept-c-74 | gate | …                       # counter rows only
+ | accept-ca-74 | gate | …
+ | accept-c-73 / accept-ca-73 correction | note | …
```

`PROVINCE.md:3-7` enumerates the craft areas (conlang, myth/symbol, era, costume/material
terminology, naming); `PROVINCE.md:9-11` admits the culture-material partition, which is why
the landing is *permitted*; and `SKILL.md:20-29`'s Decision table has no row that would route
"specify my setting / build order / settings note" (rows cover design a language, mythology,
naming, era staging, dress, consistency check only). `README.md:6`'s domain string likewise
lists no setting craft.

**Impact.** The lane's declarations and its contents disagree about what the lane does; a future
round (or a dispatcher reading SKILL.md) cannot route the new capability. This is a documentation-
coherence defect, not an authority grab, and lore already handles it the other way — its
`PROVINCE.md` carries a dated "Province map" section (`lore-shokunin/PROVINCE.md:11`ff) that
lists admitted method coverage per round.

**Smallest safe correction.** Append to `PROVINCE.md` a dated "Province map (round 74,
2026-10-25 — appended)" bullet naming setting-practice in culture-material, citing the two
entries and `corpus/README.md:445-446`, plus the CM-f-adjacent limit from F1; add one
Decision-table row to `SKILL.md` (`Specify a setting | worldbuilding-setting-practice →
couples/gates | prescribing a world's canon | a build order, note tables and a single-source
discipline, reported not fixed`). Both are outside my write path; proposed, not applied.

### F4 — LOW — base `:255` asserts an intake that the cited entry does not state

**Attack.** "Verification is not this entry's business: the checklist that owns conflict and
variant statuses **takes a note like this as its input** and hands findings to lore."

**Evidence.**

```
$ grep -ci 'settings note' corpus/knowledge/synthesis/consistency-verification-checklist.md
0
$ grep -c '設定' corpus/knowledge/synthesis/consistency-verification-checklist.md
0
$ sed -n '3p;20p' corpus/knowledge/synthesis/consistency-verification-checklist.md
- topic: a reference-only preflight for the coupling of language, myth, symbol, era, costume, and material practice; …
1. Freeze the input revision/version, recipient, requested scope, and coverage roster; enumerate culture–era units and their known contact edges. …
```

The checklist's frozen inputs are "culture–era units and their known contact edges", not a
settings note, and its topic says nothing about note documents. The direction of the sentence is
right (findings → lore, `checklist:3`), but the ingestion claim is asserted rather than stated
by the cited file.

**Impact.** A cross-file adjacency claim that no leg checks; small, but it is the same class the
contract guards at `:68` ("Do not invent a sibling path or tool and call it established").

**Smallest safe correction.** Change "takes a note like this as its input" to "applies to a note
like this" (one word-class), or add the intake line to the checklist's step 1 in a later
calibration round.

### F5 — LOW (in-lane note, not drift) — internal strength mismatch inside the base entry

Two places where the entry's own tables are stronger than its `- refuses:` line, which are
craft prescriptions (in-lane under `PROVINCE.md:9-11`) but read as lane rules:

- `:14` refuses "a universal build order", while `:86` recommends one merged order for every
  builder ("use the layer chain; it is the difference between detail and design") in a column
  headed "What to do". `synthesis/coupling-model.md:82` keeps the opposite discipline for its
  own axis ("Their order is a design choice, not a fixed timetable"), so this is not a
  contradiction with the master method — only within the entry.
- `:237`/`:247` report the page's "one authoritative document … treats it as the **authoritative
  copy**" (正本) with `:247`'s "Applies to: **any work**, one author or many", widening the
  page's shared-project rule to all works. This is the closest the entry comes to lore's
  record-governance vocabulary; it is guarded by `:267` and by the `(to-verify)` marking at
  `:253`, so it is not a canon decision today.

**Smallest safe correction.** Put the source frame into the two table headers ("the page's
practice, reported") or restore the narrowed "for a shared project" in `:247`; add "as
reported" to `:86`. No structural change.

## 3. Attacks that FAILED (the claim survived), with the evidence

1. **"The entries decide canon or rule on rights."** FAILED. Both headers refuse it
   (`base:13-14`, `amend:13`), the closing guards hold verbatim (`base:267` "Nothing here rules
   on any world. No layer assignment, no element count, no depth target and no document layout
   is fixed…"; `amend:91` "records no canon"), the worked example is marked "hypothetical and
   canon-free" (`amend:83`), and no sentence claims permission, licence, fair use or
   AI-training rights — `grep -niE 'rights|licen|permission|copyright'` over both entry files
   returns no output (zero hits each). Every quoted span is likewise within the
   ≤25-whitespace-token bound (longest 15 tokens; CJK spans are 1 token each, longest 56
   characters in the base and 37 in the amendment), so nothing here over-claims a source.
2. **"The setting ground is lore's outright."** FAILED, same ground as `CritTrendFinal.md:178`:
   `PROVINCE.md:9-11` owns the generative craft and `lore-shokunin/PROVINCE.md:3` owns records
   and verification; design method → kotodama, recorded instance + verification → lore. The
   base entry is **in-lane**.
3. **"The base entry drifts into world-bible record keeping by prescribing the bible's
   layout."** FAILED. The schemas are attributed to the pages and the layout is explicitly
   not fixed (`base:267`, verified landed, not just in the draft `SentinelScope.md:272,292-331`
   reviewed); `base:255` hands verification out. Residual only (F5).
4. **"The base entry duplicates `synthesis/coupling-model.md`'s authority."** FAILED.
   `coupling-model.md:3` is declared "the lane's master method"; `base:265` couples sideways to
   it and fixes no order that contradicts `coupling-model.md:82`.
5. **"Because no lane's PROVINCE claims narrative pacing, kotodama may keep it."** FAILED as a
   defense of the amendment — an unowned slice is not a grant, and `PROVINCE.md:22-25` requires
   contested scope to be reported. This is the reason F1 is MEDIUM, not a pass.
6. **"The amendment states its tolerance as a rule of serial fiction."** FAILED — the E1 fix
   landed: `amend:51` ("It is a lead … not a rule of serial fiction"), `:88` ("never quotable as
   a rule of serial fiction"), `:80` ("roughly"), `:63` (the interviewer's "dozens of chapters"
   bound stated against the author's twenty). F1 attacks the routing, not the hedging.

## 4. Not run / not claimed

- No network fetch in this seat: a province/adjacency attack needs none, and I make no capture,
  no-capture or reachability ruling. All source-facing facts above are quoted from the landed
  tree or from lore's read-only tree.
- No mutation anywhere: I wrote only this file; `PROVINCE.md`, `SKILL.md`, the entries, the
  contract and the counters are untouched. Read-only `git show/diff/log` on the lane repo and
  `grep`/`sed` reads on the fleet and `lore-shokunin` were the only fleet access.
- I did not grade quote fidelity, evidence windows, the S877 used-by cell, the README index
  rows, `claims.json`/`ledger.json` bytes, or either counter's internals beyond the two runs
  reported in §0; the INFO in §0 is an observation for the Ca counter seat, not a finding.
- No counter `--selftest` was run; no `souji`, `jj`, or fleet write was attempted.
- No tool was installed or upgraded in this seat (nothing was needed), so the operator's
  install-record obligation is empty.

## 5. Bottom line for the integrator

The base entry is in province. The amendment is **partial**: its disclosure-order material
records the generative half of an axis that lore's boundary document names as its own uncovered
verification method (CM-f) and routes it with no contested-scope report (F1), and its handoff
clause states the contract as an active hander and invents a disclosure payload type (F2). Both
are one-sentence fixes — the `couples:` header `:12` and §6 `:91` — none touching a quote, a row,
an evidence window or a leg — and the lane's own boundary documents should then be appended to
name the new coverage (F3). No finding here touches claim C's or claim Ca's declared legs; both counters pass as
declared under the documented pin, and no leg would have caught any of F1–F3.
