- Seat: O04 | verifier | claim O | date 2026-10-19 | baseline ac47c78

# O04 — isolated verification of the N6 couples-extractor fix

Mission (`reports/round-42/targets.json:62-66`): "apply the fix in a git-archive
copy, run selftest + the recount; compare to O03." **The fix under test does not
exist** — `op/O01-fix-draft.md` and `op/O02-controls.md` were absent at every cut
of this seat (`ls reports/round-42/op` → `O03/O04/O06/O07/O08/O09/O10`, latest
2026-10-19T16:00Z). So this seat verifies the two things it *can* verify without
a landed patch: (1) the defect's real population and arithmetic, reproduced in
isolation; and (2) whether the obvious repair (block/continuation parsing)
actually satisfies the claim's stated threshold. (2) is the load-bearing result,
and it is negative. `op/O03-predicted.md` **did** land mid-run, so the mission's
"compare to O03" leg is executed in §7.

All commands below ran read-only inside `git archive` copies; no filed byte was
edited, no `reports/round-*/run-validation.py` was executed, no git/network/install.

## 1. Isolation setup (fidelity checked, not assumed)

- `git archive ac47c78 | tar -x -C .scratch/o04` (live baseline, 220 entries).
- `git archive dfb0719 | tar -x -C .scratch/o04-r39` (the r39 policy's own
  adoption commit, 212 entries).
- Archive fidelity: SHA-256 of the working tree equals the archive copy for the
  three load-bearing files — `corpus/knowledge/linguistics/phonetics-phonology.md`
  `b4f9b003…`, `reports/round-19/audit/entry-audit.py` `e7992c32…`,
  `reports/round-35/cov/C14-audit-6-10.md` `bf402bc6…` (SAME/SAME/SAME).
- `TMPDIR=$PWD/.scratch`, `PYTHONDONTWRITEBYTECODE=1` exported before Python
  started, per the round's shared rules and `isolation-replay-protocol.md:§2 I3`.
  No runner was invoked, so Tier A/B containment does not apply here.

## 2. The defect's population — reproduced, and narrower than the queue row

The queue row says "the corpus's one wrapped couples field"
(`reports/round-40/op/defect-queue-v2.json:362`). An **indent-based** continuation
rule (a following line that is non-blank and starts with space/tab) finds exactly
that, at both trees:

| tree | entries | `- couples:` fields | wrapped fields | continuation lines |
|---|---|---|---|---|
| `ac47c78` | 220 | 220 | **1** | 5 |
| `dfb0719` | 212 | 212 | **1** | 5 |

The single wrapped field is `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`.
The per-file token-set diff (single-line vs continuation-joined) over all 220
files diverges for **exactly one file** — the same one — so the extractor delta
is 4 tokens and nothing else. This reproduces r39 Ca04 D1's "exactly 1 wrapped
field" (`reports/round-39/calib/Ca04-verify.md`, D1) and O09's item 1.

**Method note (my own false start, recorded).** A first pass of mine scanned
"the header block through the next `## `" and reported **2** wrapped fields
(adding `corpus/knowledge/linguistics/conlang-methodology.md:9`). That was my
scanner's boundary bug: `conlang-methodology.md`'s body opens with an unindented
prose line before its first `## `, which that rule swallowed. The indent rule
and the token-set diff agree on 1. The token-level detector is the reliable one;
the structural rule must be "continuation = indented following line," not
"anything up to the next heading."

## 3. r39 baseline arithmetic — reproduced byte-exact at its own commit

At `dfb0719` (212 entries), the r39 policy's Tier-1/Tier-2 resolver
(`basename-couples-policy.md:§2`) under the **single-line** extraction yields:

    refs=2504  direct=2335  fallback=163  ambiguous=0  unresolved=6

matching `basename-couples-policy.md` Part 2 (`2504 = 2335 + 163 + 0 + 6`) and
Ca04 check 1 exactly. The 6 unresolved rows, enumerated (this seat, full row set
printed, not sampled):

| entry | token | class |
|---|---|---|
| `linguistics/language-contact.md` | `honorifics-and-register.md` | no-hit |
| `linguistics/language-contact.md` | `naming-and-onomastics.md` | no-hit |
| `linguistics/language-contact.md` | `phonology-basics.md` | no-hit |
| `synthesis/typed-label-routing-workflow.md` | `../linguistics/phonology-sanity.md` | no-hit |
| `verification/gate-frozen-run-standard.md` | `-gate.md` | no-hit (glob fragment) |
| `verification/label-channel-routing-verification.md` | `../linguistics/phonology-sanity.md` | no-hit |

**5 distinct** tokens, exactly as the policy states. The two non-seed entries are
the X26-1 phantom (`../linguistics/phonology-sanity.md` cited twice —
`label-channel-routing-verification.md:14` and the synthesis entry) and the
`-gate.md` glob artifact (`gate-frozen-run-standard.md:15`). Neither is touched
by the wrapped field.

## 4. The decisive result — the obvious fix does NOT reach the threshold

Claim O's threshold is "the wrapped field reads 4/4 targets"
(`reports/round-42/claims.json`, claim O). The field names four `.md` targets
across `:76-77`:

    ... prospective sibling files: sound-change.md, tone-
    prosody.md, sound-symbolism.md, writing-systems.md

A C14-style block parser — the fix O01 was chartered to draft — folds
continuation lines into the field value. But the wrap **splits a token**:
`tone-prosody.md` is written as `tone-` at the end of `:76` and `prosody.md` at
the start of `:77`. Joining continuations with a space (the C14 pattern,
`C14-audit-6-10.md:213-236`) therefore yields `prosody.md`, not
`tone-prosody.md`:

| extraction | wrapped-field tokens | of the 4 named |
|---|---|---|
| single-line (r19/r27) | `[]` | 0/4 — 2 phantoms |
| block, space-join (C14) | `[prosody.md, sound-change.md, sound-symbolism.md, writing-systems.md]` | **3/4** — `tone-prosody.md` mangled |
| block, hyphen-aware join | `[sound-change.md, sound-symbolism.md, tone-prosody.md, writing-systems.md]` | **4/4** |

The mangling is not confined to the wrapped field's own resolution: under
space-join, `prosody.md` is a *new* distinct unresolved token that did not exist
before, so a naive "fix" **increases** the phantom population (see §5). A
hyphen-aware join is not optional polish; it is required to meet the claim's own
4/4 threshold, and it is a *second* repair beyond "gain a block parser."

**Corroboration, independent of this seat:** O09 reached the same conclusion
from the read-only side — "a naive block join that does not undo the soft wrap
produces `prosody.md` rather than `tone-prosody.md` … A fix that only
concatenates continuations without de-hyphenating the wrap will still
mis-tokenise this field" (`reports/round-42/op/O09-scribe.md`, item 3). Two
seats, different methods (structural census vs token-set diff), same finding.

## 5. The corrected census (the comparison basis O03 must reproduce)

Full recount at **both** trees, r39-policy resolution, three extraction modes
(`refs = direct + fallback + ambiguous + unresolved`, brace-expanded, per-entry
deduped):

| tree | mode | refs | direct | fallback | ambiguous | unresolved | distinct unresolved |
|---|---|---|---|---|---|---|---|
| `dfb0719`/212 | single-line (filed) | 2504 | 2335 | 163 | 0 | 6 | 5 |
| `dfb0719`/212 | block, space-join | 2508 | 2337 | 163 | 0 | 8 | 7 |
| `dfb0719`/212 | block, hyphen-join | 2508 | 2337 | 163 | 0 | 8 | 7 |
| `ac47c78`/220 | single-line (live) | 2607 | 2435 | 166 | 0 | 6 | 5 |
| `ac47c78`/220 | block, space-join | 2611 | 2437 | 166 | 0 | 8 | 7 |
| `ac47c78`/220 | block, hyphen-join | 2611 | 2437 | 166 | 0 | 8 | 7 |

Read this against claim O's `after_required` ("the corrected census reproduces
the r39 policy's arithmetic minus the phantoms"), and note three things the
integrator must not smooth:

1. **The delta is +4 refs, +2 direct, +2 unresolved — never "-2 phantoms."**
   The wrapped field's two absent names (`sound-change.md`, `tone-prosody.md`)
   are *not* removed from a count; they are *added* to it as unresolved. Before:
   the field contributed 0 refs and 0 findings (silently). After: it contributes
   4 refs, 2 of them resolving. So "2504 minus the phantoms" is the wrong
   arithmetic direction: the corrected live total is **2611**, and unresolved
   rises **6 → 8**.
2. **Both join modes land on 8 unresolved; only the identity of the extra
   phantoms differs.** Space-join's two new phantoms are `sound-change.md` +
   `prosody.md`; hyphen-join's are `sound-change.md` + `tone-prosody.md`.
   `sound-change.md` is a genuine never-written seed either way. The distinguishing
   token is `prosody.md` (artifact) vs `tone-prosody.md` (intended name) — which
   is exactly why the control set must exercise the hyphenated bytes (§6).
3. **The denominator moved, so no subtraction is admissible.** `dfb0719` is 212
   entries, live `ac47c78` is 220; the `+2` refs from the wrapped field sit on a
   `+103` refs / `+3` fallback corpus-wide change from entries landed in r40/r41.
   Any census text must state its entry denominator and its commit (this agrees
   with O09 item 5).

## 6. Selftest / control status

- The filed r19 instrument's own selftest, run in the archive copy (never
  in-tree), is **green**: `python3 -B .scratch/o04/reports/round-19/audit/entry-audit.py
  --selftest` → `PASS braces`, `PASS braces nested`, `PASS selftest entry quality`,
  `PASS selftest source locator`, `PASS selftest gap`, `PASS selftest decision`,
  `PASS selftest couples resolve []`, `PASS negative control (no sources fails)`,
  `exit=0`. **Its control set has no wrapped-field case**, which is why it is
  green while the defect is live.
- Gate-level consequence, reproduced in the copy: `entry-audit.py
  corpus/knowledge/linguistics/phonetics-phonology.md` →
  `FAIL … src=15/15 couples=0 unresolved=[] gap=False dec=True`, `TOTAL 0/1`, exit 2.
  The entry's couples leg reports **`couples=0 unresolved=[]`** — a clean-looking
  zero produced by reading nothing. A "zero unresolved" couples result on this
  entry is currently a false green, and any selftest that asserts on
  `couples_unresolved == []` would pass while the field is still invisible.
- **Control requirement this seat files against O02/O05:** the wrapped-field
  positive control must be built from the **real hyphenated wrap bytes**
  (`tone-` at line end, `prosody.md` at next-line start), not from a
  hand-wrapped field with whole tokens on each line. A control whose wrapped
  field wraps *between* tokens will pass a space-join parser that still mangles
  `tone-prosody.md`, i.e. it will green-light exactly the fix §4 shows to be
  insufficient. State the expected token as `tone-prosody.md` (4/4), and add a
  negative control asserting `prosody.md` is **not** emitted.
- `reports/round-42/run-validation.py` does not exist at this cut
  (`ls` → no such file), so the claim's `counting_commands` entry
  (`python3 reports/round-42/run-validation.py`) is not yet runnable — by any
  seat, in-tree or isolated.

## 7. Comparison to O03 (the mission's second leg)

`op/O03-predicted.md` landed during this seat's run. The mission's "compare to
O03" leg is therefore executed here. O03 derives its figures with its own
`.scratch/o03/recount.py`; this seat used `.scratch/o04/*.py`. Two separate
implementations.

**Agreements — every load-bearing figure reproduces independently:**

| figure | O03 | O04 |
|---|---|---|
| `dfb0719` single-line control | 2504 / 2335 / 163 / 0 / 6 (5 distinct) | same |
| `dfb0719` block | 2508 / 2337 / 163 / 0 / 8 (7 distinct) | same |
| HEAD single-line | 2607 / 2435 / 166 / 0 / 6 | same |
| HEAD block | 2611 / 2437 / 166 / 0 / 8 | same |
| wrapped-field census | 1 (`phonetics-phonology.md:72-77`) | same |
| wrapped tokens under single-line | 0 | same |
| delta | +4 refs / +2 direct / +2 unresolved / +2 distinct | same |

O03's §9 truncation finding is independently confirmed (§8 below). Agreement on
all of the above is the strongest result available without a landed tool.

**Divergence 1 — O03 §4's class labels contradict O03's own arithmetic, and §4 is
the side that is wrong.** O03 §4 asserts both live wrapped-field tokens are
`fallback` "because `corpus/knowledge/linguistics/` held only 21 entries at r39
close (24 at HEAD) and neither `sound-change.md` nor `tone-prosody.md` exists
anywhere in the repo." Measured at `dfb0719`:

- `git ls-tree -r --name-only dfb0719 -- corpus/knowledge/linguistics | grep -c '\.md$'`
  → **21** ✓ (O03's count is right)
- `git ls-tree -r --name-only dfb0719 | grep -E 'linguistics/(sound-symbolism|writing-systems|sound-change|tone-prosody|prosody)\.md'`
  → **`sound-symbolism.md`, `writing-systems.md`** — both **exist at `dfb0719`**,
  in the entry's own directory.
- This seat's archive copy: `os.path.isfile(.../linguistics/sound-symbolism.md)`
  → `True`; `writing-systems.md` → `True`.

Tier 1 (`basename-couples-policy.md:§2`) tests the token against `<entry
dir>/<token>` and is satisfied by **any** existing file, whatever the partition's
entry count. Both live tokens therefore resolve `direct` — which is exactly what
O03's own §6 table (`direct=2337`) and its own §8 acceptance item 2 report. So
the `dfb0719` block classes are **`direct` 2** (`sound-symbolism.md`,
`writing-systems.md`) + **`unresolved` 2** (`sound-change.md`,
`prosody.md`/`tone-prosody.md`), matching this seat's §4/§5. O03's §6/§8 numbers
are correct; its §4 prose is not, and the 21-entry count is a red herring for the
`direct`/`fallback` split.

O03 §4 further says "24 at HEAD"; the live partition is **25**
(`ls corpus/knowledge/linguistics/*.md | wc -l` → 25; `ac47c78` tree → 25), which
is what O03's own §7 output prints. Minor, but it sits in the same paragraph.

**Divergence 2 — O03 §8 acceptance item 6 is a false-green test.** It reads: "Any
landed tool reporting a wrapped-field count of 2, **or reading
`sound-symbolism.md`/`writing-systems.md` as `direct` at `dfb0719`**, is
reproducing C14's blank-line-blind `fields_of` rather than a corrected parser."
The second clause is inverted: reading those two as `direct` at `dfb0719` is the
**correct** result (they exist in the entry directory there), so a verifier
applying O03 §8 literally would **fail a correct tool**. Its first clause
(`wrapped=2` ⇒ C14's blank-line-blind parser) is right and useful. Fix: keep
clause 1, drop clause 2, and state the class expectation as `direct 2 +
unresolved 2`.

**Status of these two divergences at this seat's close.** O03 was revised during
the run (it gained a §10), and its §4/§8 were **not** corrected — §4 still reads
"both live tokens are `fallback`, not `direct`" (`O03-predicted.md:23-24,89-90`)
and §8 item 6 still carries the inverted clause (`:185-186`). O03's new §10
records this seat's numbers as convergent and attributes the `couples=0
unresolved=[]` false-green observation to `O04-verify.md:168`; it does not
mention the §4/§8 disagreement. Both corrections remain owed to the integrator.

**On O03 §10's convergence claim:** this seat's own §1–§6 were likewise computed
before reading any peer fragment, so the agreement in §10 is genuine
two-implementation agreement, not shared arithmetic. Note that O03 §10 cites
`O04-verify.md:127-129` and `:139,:142,:168,:173-176,196` — those line numbers
were accurate against the earlier revision of this file; this seat has since
inserted §7/§8, so the same content now sits at `:121-157`, `:85-119` and
`:158-186`. The cited *content* is unchanged; only the offsets moved.

## 8. Independent confirmation of O03 §9 — the landed r39 policy is truncated

O03 §9 reports the landed policy is truncated. Confirmed here on separate
commands, and **independently confirmed by O12** (`op/O12-policy-check.md` §1,
finding O12-F1) which goes further and pins the relation: the filed file is
**byte-identical to draft lines 41–147**. This seat re-ran that test:
`diff <(sed -n '41,147p' reports/round-39/calib/Ca03-basename-policy.md)
reports/round-39/calib/basename-couples-policy.md` → no output (**identical**).

Measurements: `reports/round-39/calib/basename-couples-policy.md` is **107 lines /
5832 bytes**, sha256
`105dfff6c667ad5b77c28be8d6070ec243b5e19029fb60ae83d6028aa2e941cf`;
`grep -c '```'` → **0**; `grep -c RESULT` → **0**; `grep -c 2504` → **0**; the
file's last bytes are `…(export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1):\n` — it ends on §6's lead-in sentence. The authoring
draft `reports/round-39/calib/Ca03-basename-policy.md` is **359 lines / 19409
bytes**, sha256
`125ede77e3f50e3c58af61fb2fad246c8378b4dcfc4ee5d1749da8dd53a17850`, and carries
the fenced recipe (`:149-258`), the `RESULT` line and §7 (`:355` the
`2504 = 2335 + 163 + 0 + 6` arithmetic). Both line counts are exact — `wc -l` and
`python3 -c "len(f.read().splitlines())"` agree on 107 and 359 — so O03's "108
lines" / "360 lines" is off by one (immaterial to the finding), while O12's
107/359 is right. Digests above are this seat's own `sha256sum`; O12 lists the same
two values correctly (`op/O12-policy-check.md:38-39,246,250`).

**Consequence for claim O, which O03 flags and this seat endorses:** the policy's
§6 recipe — the artifact the claim's `after_required` gestures at — **is not in
the landed bytes**. There is no durable script to patch there; a successor
instrument must be authored fresh. The `2504 = 2335 + 163 + 0 + 6` arithmetic
that claim O calls "the r39 policy's" survives only in the authoring draft
(`Ca03-basename-policy.md:35,268,355`), in Ca04's verification
(`reports/round-39/calib/Ca04-verify.md:29,140`) and in `reports/round-42/claims.json:14`
— **not** in the filed policy. A corrected census must cite one of those, not the
policy, for its baseline.

## 9. Corroboration from O02's controls, and the de-hyphenation reading

`op/O02-controls.md` landed during this seat's run and independently confirms the
§4 result from the control side. Its control 1 (`wrapped-field-positive`) asserts
exactly what this seat measured: the live field's bytes must yield
`{sound-change.md, tone-prosody.md, sound-symbolism.md, writing-systems.md}` and
must **not** yield `{prosody.md, toneprosody.md, "tone- prosody.md"}` — i.e. the
naive space-join and both over-eager de-hyphenations are all excluded
(`O02-controls.md:24,168-169`). O02's executed evidence shows the same three-way
split this seat's §4 table reports, and its `--against` run on its own fixed
scaffold produces `couples=2 unresolved=['sound-change.md', 'tone-prosody.md']`
(`:341,400`) — the same two unresolved tokens this seat's §5 finds under the
hyphen-join mode.

**New independent corroboration for the de-hyphenation reading (this seat).** My
§4 could only say the space-join emits `prosody.md` and that `tone-prosody.md`
was a *reading* of the wrapped bytes. The entry supplies direct internal
evidence: `corpus/knowledge/linguistics/phonetics-phonology.md:279` writes the
name **in full, unwrapped** — `Natural partners: \`sound-change.md\` (diachrony →
§5), \`tone-prosody.md\`,` — while the wrapped header field at `:76-77` spells the
same two files as `sound-change.md, tone-` / `prosody.md`. The token
`tone-prosody.md` therefore appears verbatim elsewhere in the same file, and
`prosody.md` appears nowhere in the repo. That upgrades the de-hyphenation
choice from "this seat's judgement" to evidence-backed; it is still a *reading*
(no filed rule names the token), but the reading now has an in-file witness.
O02 reached the same reading from the same bytes (`O02-controls.md:433-436`) and
O03 from its own probe (`O03-predicted.md:107-135`); three seats, three methods.

O02 §5 additionally files a **third defect class** (new, not in the r39 D1 row):
C14's `fields_of` ignores blank lines, so `conlang-methodology.md`'s single-line
field over-captures body prose (`O02-controls.md:404-423`). This seat's §2 method
note is the same phenomenon seen from the census side — my first scanner
reported `wrapped=2` for exactly that file, and the indent rule corrected it.
Independent agreement again.

## Verdict (this seat, on what exists)

- **Baseline arithmetic: verified** — `2504 = 2335 + 163 + 0 + 6`, 5 distinct,
  at `dfb0719`, byte-exact against the r39 policy.
- **Defect population: verified and narrowed** — exactly 1 wrapped field
  (indent rule + token-set diff agree), 4 named targets, 2 existing, 2 phantoms,
  1 of them a wrap artifact.
- **Claim O's threshold: NOT met by the fix the wave was chartered to draft.**
  A block parser alone reads 3/4; only a hyphen-aware join reads 4/4. The claim's
  `after_required` is currently unachievable by O01 as scoped, and the corrected
  census is **not** "2504 minus 2 phantoms."
- **O03's §6/§8 numbers and §9 truncation finding: independently reproduced.**
  Its §4 class labels and §8 item 6's second clause are wrong and are owed
  correction (§7).
- **Cannot verify the fix itself**: `op/O01-fix-draft.md` does not exist at this
  cut. This is a pre-landing verification of the *repair surface* plus the
  corrected census, not a verdict on a patch.

## Owed

- **`op/O01-fix-draft.md`** (the patch under test) was absent at every cut
  (`2026-10-19T15:57Z`–`16:00Z`); `op/O02-controls.md` landed at ~16:00Z and is
  folded into §9. This seat's verification of a landed fix's *behaviour* is
  therefore owed a re-run once O01 lands; the §4/§5 tables are the fixtures it
  must move. O02's `--against <host>` battery is the harness that re-run should
  use.
- **`op/O03-predicted.md` landed mid-run and was compared in §7.** The comparison
  found two divergences, both filed above: O03 §4's `fallback` labels for the two
  live wrapped-field tokens are wrong (they are `direct` at `dfb0719`; O03's own
  `direct=2337` agrees with this seat), and O03 §8 item 6's second clause would
  fail a correct tool. O03 was revised during the run (gaining §10) and **neither
  point was corrected** — §4 still reads `fallback` (`O03-predicted.md:23-24,89-90`),
  §8 item 6 still carries the inverted clause (`:185-186`). The integrator should
  apply both before using O03's §8 list as an acceptance gate. **O03's §6/§8
  numeric tables and its §9 truncation finding are correct and independently
  reproduced here.**
- **The de-hyphenation choice is evidence-backed but still a reading.** What is
  proven: the space-join parser emits `prosody.md`, which names no file and
  appears nowhere in the repo. What is now *corroborated* (this seat, §9): the
  entry's own body prose at `phonetics-phonology.md:279` writes `tone-prosody.md`
  in full, so the intended name has an in-file witness. Still `to-verify` as an
  *authorial-intent* claim — no filed rule names the token, and O02's control
  encodes the reading rather than proving it (`O02-controls.md:433-436`).
- **The fix's durable host is unresolved** and is not this seat's to choose: both
  located extractors are filed bytes (`reports/round-19/audit/entry-audit.py:75`,
  `reports/round-27/audit/entry-audit.py:275`, each
  `re.search(r"^- couples:\s*(.*)$", text, re.M)`), and `tools/` carries no couples
  resolver (my grep for `couples` in `tools/**/*.py` hits only the
  `provenance-audit.py:76` field-presence regex and fixture text in
  `source-audit-inventory.py` — the `provenance-audit.py` regex
  `^- (topic|sources|couples):[ \t]*(.*)$` is also single-line and also blind to
  continuations). A `tools/harness/` checker is the only route consistent with
  "no filed byte rewrites."
- **Corrected census denominators**: any census text must cite its commit and its
  entry count; the live number is 220 entries / 2611 refs, the r39-policy number
  is 212 / 2504, and they are different units at different trees.

## Citations

- Assignment: `reports/round-42/targets.json:62-66` (seat O04, out `op/O04-verify.md`);
  `:4-9` (shared rules); claim + thresholds: `reports/round-42/claims.json` (claim O,
  `after_required`, `counting_commands`, `non_goals`).
- Defect row: `reports/round-40/op/defect-queue-v2.json:362-369`
  (`N6-couples-extractor-wrapped-field`, sha256 `dfc9265d…`); origin r39 Ca04 D1
  (`reports/round-39/calib/Ca04-verify.md`, sha256 `e5d1226e…`).
- Policy under test: `reports/round-39/calib/basename-couples-policy.md`
  (§2 tiers, §5.6 glob fragments; sha256
  `105dfff6c667ad5b77c28be8d6070ec243b5e19029fb60ae83d6028aa2e941cf`). The
  authoring draft `reports/round-39/calib/Ca03-basename-policy.md` carries the
  same §1–§5 text and the rest (sha256
  `125ede77e3f50e3c58af61fb2fad246c8378b4dcfc4ee5d1749da8dd53a17850`).
- Extractor hosts: `reports/round-19/audit/entry-audit.py:31,34-42,74-96` (sha256
  `e7992c32…`); `reports/round-27/audit/entry-audit.py:275` (sha256 `fb589b28…`).
- C14 block parser: `reports/round-35/cov/C14-audit-6-10.md:213-236,249-288`
  (sha256 `bf402bc6…`).
- Defect instance: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
  (sha256 `b4f9b003…`); existence check `ls corpus/knowledge/linguistics/` →
  `sound-symbolism.md` ✓, `writing-systems.md` ✓, `sound-change.md` ✗,
  `tone-prosody.md` ✗, `prosody.md` ✗ (this seat, 2026-10-19).
- Corroboration: `reports/round-42/op/O09-scribe.md` items 1, 3, 5;
  `reports/round-42/op/O03-predicted.md` §1 (control match), §2 (wrapped=1),
  §3 (C14 blank-line-blind `fields_of`), §5 (de-hyphenation probe), §6 (tables),
  §9 (truncation), §10 (convergence) — agreed; §4 (class labels, `:23-24,89-90`)
  and §8 item 6 clause 2 (`:185-186`) — corrected in §7 above;
  `reports/round-42/op/O02-controls.md` control 1 (`:24,168-169`), §3 executed
  evidence (`:298,304,341,400`), §4 join table (`:392-394`), §5 third defect
  class (`:404-423`), §6 de-hyphenation `to-verify` (`:433-436`).
- In-file witness for the de-hyphenation reading:
  `corpus/knowledge/linguistics/phonetics-phonology.md:279` (`\`tone-prosody.md\``
  written in full, unwrapped) vs `:76-77` (`tone-` / `prosody.md`).
- Policy truncation: `reports/round-39/calib/basename-couples-policy.md` (107
  lines / 5832 bytes; `grep -c '```'`=0, `RESULT`=0, `2504`=0; ends mid-§6);
  authoring draft `reports/round-39/calib/Ca03-basename-policy.md` (359 lines /
  19409 bytes; `:35,268,355` carry the 2504 arithmetic, `:257` the RESULT line).
- Isolation protocol: `reports/round-39/calib/isolation-replay-protocol.md:§2`.
- Command outputs (this seat, 2026-10-19, `TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`, read-only, no runner executed, no git/network/install):
  (a) `git archive ac47c78 | tar -x -C .scratch/o04` → 220 entries;
  `git archive dfb0719 | tar -x -C .scratch/o04-r39` → 212 entries; archive-vs-tree
  sha256 SAME for the three load-bearing files.
  (b) indent-rule census → `ac47c78`: 220 fields / 1 wrapped / 5 continuation
  lines; `dfb0719`: 212 fields / 1 wrapped / 5 continuation lines; token-set diff
  → 1 differing file (`phonetics-phonology.md`), `single=[]` vs
  `block=[prosody.md, sound-change.md, sound-symbolism.md, writing-systems.md]`.
  (c) r39-policy recount, six rows as tabulated in §5 (the `dfb0719` single-line
  row is the r39 baseline `2504/2335/163/0/6`).
  (d) wrapped-field resolution → single-line `[]`; space-join 3/4
  (`tone-prosody.md` mangled to `prosody.md`); hyphen-join 4/4.
  (e) `entry-audit.py --selftest` in the copy → 8 PASS, exit 0.
  (f) `entry-audit.py corpus/knowledge/linguistics/phonetics-phonology.md` in the
  copy → `FAIL … couples=0 unresolved=[] gap=False dec=True`, `TOTAL 0/1`, exit 2.
  (g) `ls reports/round-42/op` → `O03/O04/O06/O07/O08/O09/O10` at 16:00Z;
  `O01`/`O02` absent; `ls reports/round-42/run-validation.py` → absent.
  (h) `grep -rn couples tools/*.py tools/gates/*.py tools/harness/*.py` → no
  couples resolver; `provenance-audit.py:76` single-line field regex only.
  (i) comparison commands (§7–§8): `git ls-tree -r --name-only dfb0719 --
  corpus/knowledge/linguistics | grep -c '\.md$'` → 21;
  `git ls-tree -r --name-only dfb0719 | grep -E
  'linguistics/(sound-symbolism|writing-systems|sound-change|tone-prosody|prosody)\.md'`
  → `sound-symbolism.md`, `writing-systems.md` only; `git ls-tree -r --name-only
  ac47c78 -- corpus/knowledge/linguistics | grep -c '\.md$'` → 25;
  `ls corpus/knowledge/linguistics/*.md | wc -l` → 25; `wc -lc
  reports/round-39/calib/basename-couples-policy.md` → `107 5832`;
  `wc -lc reports/round-39/calib/Ca03-basename-policy.md` → `359 19409`.
