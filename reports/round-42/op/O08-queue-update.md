- Seat: O08 | verifier | O | date 2026-10-19 | baseline ac47c78

# O08 — queue-v2 N6 row re-class draft

Scope: the `N6-couples-extractor-wrapped-field` row in the queue artifact at
`reports/round-40/op/defect-queue-v2.json` (row index 34, `:362-369`). This
fragment is a **re-class draft plus an independent reproduction**, not an
applied change: the queue file is integrator-applied, and it was already edited
once outside this seat's boundary (see Observation 3). Nothing here was written
outside `reports/round-42/op/`.

## 1. The row as it stands at baseline ac47c78

```json
{
  "id": "N6-couples-extractor-wrapped-field",
  "origin": "r39 Ca04 D1",
  "class": "carried-with-owner",
  "owner": "future resolver round",
  "reason": "the single-line couples extractor silently zeroes the corpus's one wrapped couples field (phonetics-phonology.md:72-77): 0 tokens captured vs 4 named, 2 phantom",
  "next_touch": "a resolver fix round",
  "evidence": "reports/round-39/calib/Ca04-verify.md"
}
```

Read byte-exact at HEAD: `sed -n '362,369p' reports/round-40/op/defect-queue-v2.json`.
The row carries no `verification` key and no `fixed_at` — the two fields every
`fixed-with-evidence` row in this file carries (`:53,64,84`; `:373-379` is the
r41-written shape). Class census at HEAD: 38 rows = 28 `carried-with-owner` +
10 `fixed-with-evidence`.

## 2. Independent reproduction of the defect (claim O, the row's premise)

**2.1 The wrapped field.** Exactly one wrapped `couples:` field exists in the
corpus. My scan of all 220 entries (`glob corpus/knowledge/*/*.md`) found 1:
`corpus/knowledge/linguistics/phonetics-phonology.md:72-77` — one `- couples:`
header plus 5 continuation lines. Matches Ca04 D1 (`reports/round-39/calib/Ca04-verify.md:80-81`).

**2.2 The live extractor reads 0 there.** The r19 instrument's parser is a
single-line capture (`reports/round-19/audit/entry-audit.py:74-80`: `re.search(r"^- couples:\s*(.*)$", text, re.M)` then `MDREF_RE.findall(line)` on that one line). Run live, read-only, on the entry:

```
python3 -B reports/round-19/audit/entry-audit.py corpus/knowledge/linguistics/phonetics-phonology.md
FAIL corpus/knowledge/linguistics/phonetics-phonology.md src=15/15 couples=0 unresolved=[] gap=False dec=True
TOTAL 0/1 clear the bar
```

`--json` gives `"couples_resolved": 0, "couples_unresolved": []`. **The row's
"0 tokens captured" is confirmed live, not merely inherited from Ca04.**

**2.3 The full field names 4 targets, 2 of them phantoms.** Block-parsing
through the next field yields exactly 4 `.md` tokens. Resolved against the
entry dir, lane root and `corpus/knowledge/`:

| token | status |
|---|---|
| `sound-change.md` | phantom (no such file corpus-wide) |
| `tone-prosody.md` | phantom (no such file corpus-wide) |
| `sound-symbolism.md` | exists (`corpus/knowledge/linguistics/`) |
| `writing-systems.md` | exists (`corpus/knowledge/linguistics/`) |

**The row's "4 named, 2 phantom" is confirmed.**

**2.4 A naive block parser does NOT satisfy "4/4" — new measured finding.**
The field is hyphen-wrapped: line 76 ends `…sound-change.md, tone-` and line 77
begins `prosody.md, …`. Any extractor that captures continuation lines but
joins them on the newline gets the **mangled** token `prosody.md`, not
`tone-prosody.md`:

- block, newline-join → `['prosody.md', 'sound-change.md', 'sound-symbolism.md', 'writing-systems.md']`
- block, hyphen-continuation rejoined → `['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']`

This is the hazard Ca04 named as *unhandled by any current instrument* and
marked `to-verify` (`Ca04-verify.md:86-88`). **I measured it: block extraction
alone is necessary but not sufficient for the row's own `after_required`
("the wrapped field reads 4/4 targets").** The landed fix must also rejoin a
token broken at a trailing hyphen, or the 4-token population reads
`sound-change.md / tone-prosody.md` as `sound-change.md / prosody.md` — same
count, different token, different disposition.

## 3. Corpus-wide recount (my own, read-only, synthetic re-parse)

Same resolver semantics as the r19 instrument (entry dir → lane root →
`corpus/knowledge/`), plus the policy's Tier-2 unique-basename fallback over
`corpus/knowledge/*/*.md` (`basename-couples-policy.md` §2). No filed byte was
touched; this is a synthetic re-parse.

| extractor | refs | direct | fallback | ambiguous | unresolved |
|---|---|---|---|---|---|
| single-line (r19 as implemented) | 2607 | 2435 | 166 | 0 | 6 |
| block, newline-join (C14 style) | 2611 | 2437 | 166 | 0 | 8 |
| block, hyphen-rejoined | 2611 | 2437 | 166 | 0 | 8 |

Both partitions sum exactly (`2435+166+0+6 = 2607`; `2437+166+0+8 = 2611`).

**The unresolved set reproduces the r39 policy's "6 unresolved (5 distinct)"
exactly** under the single-line extractor: `honorifics-and-register.md`,
`naming-and-onomastics.md`, `phonology-basics.md` (all three in
`language-contact.md`), `../linguistics/phonology-sanity.md` ×2
(`typed-label-routing-workflow.md`, `label-channel-routing-verification.md`),
`-gate.md` (`gate-frozen-run-standard.md:15`). This is Ca03's Part 2 population
(`Ca03-basename-policy.md:35-36,268`), measured independently here.

**Reconciliation of the row's citation with the policy's arithmetic — one
discrepancy, dispositioned.** The row and Ca04 cite the policy's `2504 = 2335
+ 163 + 0 + 6` figure. That figure was measured at **212 entries** and its
script lives in Ca03 (`Ca03-basename-policy.md:35-36,232-242,268`); the landed
policy file (`basename-couples-policy.md`, 107 lines, sha `105dfff6…`) carries
no script and no such totals. At today's **220 entries** my recount gives
`2607 = 2435 + 166 + 0 + 6` under the same single-line semantics. The
fallback count therefore moved 163 → 166 (+3) while the unresolved count held
at 6 (same 5 distinct names). **The "+3" is not explained by the extractor
defect** — it tracks the 212→220 entry growth, and I have not decomposed it.
Recorded as `to-verify` below; I do not claim it is only corpus growth.

## 4. Why the row must NOT be re-classed `fixed-with-evidence` at r42

The r42 claim's `after_required` has five parts (`reports/round-42/claims.json:16`):
fixed extractor durable with its owning instrument identified; wrapped field
read whole on the live corpus; corrected census filed; selftest green; zero
phantom attributions or each dispositioned. Measured against the tree at
ac47c78:

- **Owning instrument: none.** `grep -rln couples tools/ --include='*.py'`
  returns only `tools/gates/provenance-audit.py` and
  `tools/source-audit-inventory.py`; neither is a couples resolver, and no
  `tools/harness/` couples checker exists. The durable couples instruments
  remain the **filed** `reports/round-19/audit/entry-audit.py` (reads 0, above)
  and `reports/round-27/audit/entry-audit.py` (`couples_unres=0`, `bar=False`
  — its failure is the unrelated source-locator leg). Both are filed bytes,
  never editable.
- **Wrapped field: still zeroed live.** §2.2.
- **Corrected census: not filed.** My §3 recount is this fragment, a draft.
- **Selftest: no landed fix, so no fix selftest.** The r19 instrument's own
  `--selftest` (`entry-audit.py:151-182`) exercises brace expansion, one
  synthetic entry and a no-sources negative control; its couples check is
  `couples_unresolved == []` on a synthetic single-line field
  (`:171,176`). It has no wrapped-field case and no phantom control, so it
  cannot be the required control.
- **Phantoms: 2 remain, neither dispositioned.** `sound-change.md` and
  `tone-prosody.md` do not exist corpus-wide.

The r41 lesson applies verbatim: `fixed-with-evidence` requires a landed
artifact plus a verifier's measured output — r41's own O12 refused to apply
O06's proposed re-class for exactly this reason ("Do not claim either row
fixed", `reports/round-41/op/O12-final.md:14`), and the integrator's landed
form carries a populated `verification` string, which N6 cannot supply today.

### Verdict

**N6 stays `carried-with-owner` at r42.** The row's premise is reproduced and
strengthened (the defect is live, the 4/2 split is exact, and the mangling
hazard is now measured rather than `to-verify`), but no landed fix exists, so
no re-class is admissible. The row is upgraded in *content*, not in *class*.

## 5. Row delta to apply at r42 integration (conditional; do not apply if any gate below fails)

Retain `id` and `origin`; keep `class` unchanged. This is a status/handoff
refresh, not a fix claim:

```json
{
  "id": "N6-couples-extractor-wrapped-field",
  "origin": "r39 Ca04 D1",
  "class": "carried-with-owner",
  "owner": "successor-instrument author (r43/r44) — same owner as r39-basename-successor-instrument, one instrument fixes both",
  "reason": "REPRODUCED LIVE at ac47c78, not merely inherited: the r19 single-line extractor returns couples_resolved: 0 on corpus/knowledge/linguistics/phonetics-phonology.md:72-77 while the block-parsed field names 4 targets, of which sound-symbolism.md and writing-systems.md exist and sound-change.md and tone-prosody.md are phantoms — the row's '0 vs 4 named, 2 phantom' is exact. NEW measured finding: the field is hyphen-wrapped ('tone-' / 'prosody.md'), so a block parser that joins continuations on the newline yields the mangled token prosody.md, not tone-prosody.md; block extraction alone does not satisfy '4/4'. The fix must be block extraction THROUGH the next header field PLUS hyphen-continuation rejoin. Corpus-wide recount by this seat: single-line 2607 = 2435 direct + 166 fallback + 0 ambiguous + 6 unresolved (the 6 are exactly the policy's 6/5-distinct population); block 2611 = 2437 + 166 + 0 + 8, distinct 7 either way (prosody.md vs tone-prosody.md — both phantoms, so the total is insensitive to the mangling while the token identity is not). The policy's cited 2504 = 2335 + 163 + 0 + 6 is a 212-entry measurement (its script lives in Ca03, not in the landed 107-line policy file); the fallback count is 166 at 220 entries, +3 undecomposed.",
  "next_touch": "r43 or r44 (the successor-instrument round): author the durable couples resolver under tools/harness/ — block extraction to the next '- <field>:' header, hyphen-continuation rejoin, the Tier-2 unique-basename fallback, and the C12-row-2 disposition leg (unresolved = blocker unless the same line marks it '(to-verify') — then re-run corpus-wide and dispose the 2 wrapped-field phantoms. N6 and r39-basename-successor-instrument close together; one instrument, two filed rows. The r19/r27 instruments are filed bytes and are never edited.",
  "evidence": "reports/round-42/op/O08-queue-update.md §2-§4 (this seat's live reproduction, the 4/2 split, the mangling measurement, and the recount), corroborated independently by reports/round-42/scout/K01-n6-scout.md §4-§5 and reports/round-42/op/O04-verify.md §2-§4; reports/round-39/calib/Ca04-verify.md:78-105; reports/round-39/calib/Ca03-basename-policy.md:35-36,232-242,268; reports/round-19/audit/entry-audit.py:74-80 (single-line capture) and live run output; reports/round-27/audit/entry-audit.py live run output",
  "verification": "this seat's live read-only runs at ac47c78: the r19 instrument prints couples=0 / couples_resolved: 0 on the wrapped entry; the r27 instrument prints couples_unres=0 with bar=False; my synthetic recount reproduces the policy's 6-unresolved set exactly. Independently reproduced by K01 (scout) and O04 (isolated git-archive copy): both measured the hyphen-wrap mangling and the same corrected totals. NO landed fix exists to verify — hence the class is unchanged."
}
```

### Gate: do not write the above until all five hold

1. The integrator accepts §2.2's live reproduction as sufficient for the
   `reason`/`verification` upgrade (no landed artifact is claimed).
2. A second seat independently reproduces the mangling measurement in §2.4
   (O04/O05 are the natural hosts; a hand-crafted `tone-` / `prosody.md`
   fixture is the clean control).
3. O12 (policy-check) confirms the 2504→2607 / 163→166 reconciliation in §3
   and does not object to the `to-verify` framing of the +3.
4. The `owner` change is accepted as an alias of the existing
   `r39-basename-successor-instrument` owner, not a new owner class.
5. The integrator rules on Observation 3 below before touching this file again.

If gate 1 or 2 fails, apply nothing and record `could-not-evaluate` for the
row's upgrade — the row as filed at `:362-369` remains correct as written.

## 6. Observations (reported, not adjudicated — integrator's call)

1. **The successor queue still does not exist.** r41's X00 required "a new
   round-41 successor artifact" and named the filed r40 queue immutable
   (`reports/round-41/cross/X00-connector.md`, "Hard integration conflict" row
   and Owed). No `defect-queue-v3` exists: `find . -name '*defect-queue*'`
   returns only the r37 and r40 files. So this r42 delta has no designated
   successor target; the integrator must either create one or rule.
2. **`N6` and `r39-basename-successor-instrument` are one lifecycle.**
   `r39-basename-successor-instrument` (`:323-331`) already carries D1, the
   same live instance, and the same r43/r44 owner. Its `next_touch` asks for
   "block extraction through the next header field" — which §2.4 shows is
   insufficient on its own. Both rows should move together; consider whether
   N6 is the census alias of the successor-instrument row, in the style of the
   file's existing `O12`/`R36-ABSOLUTE-ROOT` and
   `r37-A01`/`R36-R7-READSET-13` alias pairs (`:8`).
3. **r41 edited the filed r40 queue in place.** The r40 queue was committed at
   `13a1657` with sha256 `fe596a9d13d48401f87d545964ed1d969cf64bac65f3ce90522f68ebd6ae4b98`;
   `ac47c78` then modified it (20 lines changed) to flip
   `N7-receipt-fidelity` and `r39-runner-root-regression` to
   `fixed-with-evidence` and append an `r41_update` block; the file now hashes
   `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`. The
   same commit's r41 fragments state that file is immutable and a successor is
   required. This is outside my scope to adjudicate and I changed nothing; I
   report it because my own delta targets that file, and because a re-class
   written into a mutable filed path is not durable the way the queue's own
   notes assume ("original filed bytes are untouched", `:8`).
4. **Independent corroboration arrived mid-round; gate 2 is satisfied.** After
   this seat's measurements were taken, two sibling fragments reported the same
   results from separately built evidence:
   `reports/round-42/scout/K01-n6-scout.md` §4 measured the hyphen soft-wrap
   join-rule table (newline-join → `prosody.md`, naive de-hyphen →
   `toneprosody.md`, hyphen-rejoin → `tone-prosody.md`) and its §5 corrected
   census `2611 → 2437 + 166 + 0 + 8`; `reports/round-42/op/O04-verify.md` §4
   reached the identical "block extraction is necessary but not sufficient"
   negative result in an isolated `git archive` copy and rated space-join
   **3/4** vs hyphen-join **4/4**. Three seats, independent methods, same
   numbers — the §2.4 finding is no longer single-source. K01 additionally
   locates the defect at `entry-audit.py:75` (`$` under `re.M` stopping at the
   first newline) and notes two further copies of the same parse (r27, r28),
   which the successor-instrument row must dispose of.

## Owed

- **Integrator:** create or designate the queue successor artifact (Obs. 1),
  rule on Obs. 3, and apply §5 only if all five gates hold. This seat does not
  write the queue.
- **Independent verifier (O04/O05):** SATISFIED at the reproduction level —
  O04 §4 and K01 §4 both measured the hyphen-continuation mangling
  independently (Obs. 4). What remains open is the *planted* adversarial
  fixture (a hand-crafted `tone-` / `prosody.md` break plus a
  `prosody.md`-must-not-appear negative control, O04 §4's own recommendation);
  a natural-corpus reproduction is not a synthetic trap.
- **O12 / policy check:** confirm the 2504→2607 and 163→166 reconciliation,
  and the 212-vs-220 entry-count attribution.
- `to-verify`: the fallback count's 163 → 166 movement (+3) is measured but not
  decomposed; I do not attribute it to the extractor defect.
- `to-verify`: the "2 phantom attributions in the census" phrasing in
  `reports/round-42/claims.json:16` — I could not locate a filed census
  artifact that counts phantom *attributions* as a quantity; what I measured
  is 2 phantom tokens in the one wrapped field (§2.3) plus the policy's
  pre-existing `-gate.md` and `../linguistics/phonology-sanity.md` phantoms.
  If the claim means something narrower, it is unverified by me.

## Citations

- Row under review: `reports/round-40/op/defect-queue-v2.json:362-369`
  (read byte-exact at ac47c78); class census and the `fixed-with-evidence`
  shape at `:8,53,64,84,373-379`; one-lifecycle sibling
  `r39-basename-successor-instrument` at `:323-331`.
- The defect's origin: `reports/round-39/calib/Ca04-verify.md:78-105`
  (D1, the live instance, the 4-token/2-phantom split, and the mangling
  hazard marked `to-verify` at `:86-88`).
- Policy arithmetic: `reports/round-39/calib/Ca03-basename-policy.md:35-36,232-242,268`
  (the 212-entry `2504 = 2335 + 163 + 0 + 6` measurement and its script);
  the landed policy at `reports/round-39/calib/basename-couples-policy.md`
  (107 lines, sha `105dfff6c667ad5b77c28be8d6070ec243b5e19029fb60ae83d6028aa2e941cf`,
  §2 Tier-2 fallback, §3 reporting rules, §6 glob-fragment rule).
- The extractor: `reports/round-19/audit/entry-audit.py:74-80` (single-line
  capture, `MDREF_RE` at `:31`), `:151-182` (its selftest, couples check at
  `:171,176`); live runs of the r19 and r27 instruments recorded in §2.2
  and §4.
- The wrapped field's bytes: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
  (header at `:72`; the `tone-` / `prosody.md` break at `:76-77`).
- Disposition rule for unresolved tokens: `reports/round-35/cov/C12-audit-runbook.md:37`
  (row 2 — blocker unless marked `(to-verify`).
- r41's own refusal precedent: `reports/round-41/op/O12-final.md:14`;
  the immutability requirement: `reports/round-41/cross/X00-connector.md`
  (collision-matrix row "N7 and r39 root-regression queue rows", and Owed).
- Boundary: `reports/round-42/targets.json:6` (filed bytes r1-r41 never
  edited); `reports/round-42/claims.json:16` (the O claim's `after_required`).
- Commands (all read-only, no round runner executed, no filed byte written):
  `sed -n '362,369p' reports/round-40/op/defect-queue-v2.json`;
  `python3 -B reports/round-19/audit/entry-audit.py corpus/knowledge/linguistics/phonetics-phonology.md`
  (and `--json`); `python3 -B reports/round-27/audit/entry-audit.py corpus/knowledge/linguistics/phonetics-phonology.md`;
  `grep -rln couples tools/ --include='*.py'`; `find . -name '*defect-queue*'`;
  `git show 13a1657:reports/round-40/op/defect-queue-v2.json | sha256sum`;
  `sha256sum reports/round-40/op/defect-queue-v2.json`; `git show ac47c78 --stat`;
  `git show ac47c78 -- reports/round-40/op/defect-queue-v2.json`; and the
  synthetic recount scripts in §2-§3 (heredoc, read-only).
