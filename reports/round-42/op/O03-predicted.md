- Seat: O03 | executor | claim O | date 2026-10-19 | baseline ac47c78

# O03 — predicted corrected couples census (read-only, synthetic re-parse)

Mission (`reports/round-42/targets.json`, seat `O03`): "Predicted corrected census:
your own read-only recount with the fixed logic (synthetic re-parse, no filed
edits) — the landed tool must reproduce it."

Method: a standalone read-only re-parser (`.scratch/o03/recount.py`, written this
seat, never staged under `corpus/`, never editing a filed byte, no
`run-validation.py` executed anywhere). It reads the r39 close tree through
`git show dfb0719:<path>` and the live tree from disk, and runs five extractor
variants over the same 212/220-entry population. Baseline `ac47c78`; the r39
tree measured is the declared r39 baseline `dfb0719`
(`reports/round-39/claims.json`, `REGIMEN.md:19`).

## Verdict

The corrected census is **`refs 2504 -> 2508` and the r39 arithmetic becomes
`2508 = 2337 + 163 + 0 + 8`** — and the eight unresolved tokens are **not** the
phantoms Ca04 D1 named. Ca04's "2 phantom attributions" reading of the wrapped
field does not survive measurement at `dfb0719`: both live tokens in that field
are `fallback`, not `direct`, because `corpus/knowledge/linguistics/` held only
21 entries at r39 close (24 at HEAD) and neither `sound-change.md` nor
`tone-prosody.md` exists anywhere in the repo at either revision.

## 1. Control — variant A reproduces the filed r39 numbers exactly

The single-line extractor (r19 `entry-audit.py:75`, restated as policy §1 of
`reports/round-39/calib/basename-couples-policy.md:16-17`) run at `dfb0719`:

```
A  single-line (r19/r39 policy §1)  entries=212 fields=212 refs=2504
   -> direct=2335 fallback=163 ambiguous=0 unresolved=6   (5 distinct)
```

Byte-identical to the filed policy's arithmetic (`claims.json:14`
"the r39 policy's 2504 = 2335 + 163 + 0 + 6") and to Ca04 §1
(`reports/round-39/calib/Ca04-verify.md:29-32`). This is the control that makes
the corrected numbers below comparable: same population, same classifier, only
the extractor changed.

## 2. Wrapped-field census — exactly ONE field, not two

With a blank-line stop (the only defensible continuation rule; see §3), the
wrapped-field population at `dfb0719` is **1**:

- `corpus/knowledge/linguistics/phonetics-phonology.md:72-77` — the `- couples:`
  head line plus **5** continuation lines. Confirms Ca04 D1's instance exactly.
- The other candidate, `corpus/knowledge/linguistics/conlang-methodology.md:7`,
  is a **false positive**: line 7 is a single physical line and line 8 is blank
  (measured; §3). It only looks wrapped under C14's blank-line-blind `fields_of`.

## 3. Extractor semantics — C14's `fields_of` is not a safe block parser

`reports/round-35/cov/C14-audit-6-10.md:225-236` builds the frontmatter block and
then appends every non-blank line to the current field with
`elif cur and line.strip():` (`:234`) — **there is no blank-line terminator**;
the block ends only at a `## ` heading (`:218`). Two measured consequences:

1. It mis-identifies `conlang-methodology.md` as wrapped (above), because after
   the blank line 8 it keeps appending body prose (line 9 onward) into the
   `couples` field.
2. `C14-audit-6-10.md:208-214`'s `frontmatter_block` additionally ends the block
   at the first `## `, so a field wrapping across a heading boundary is
   truncated.

Measured contrast at `dfb0719` (whole corpus): my blank-line-stop parser yields
`wrapped=1`; C14's literal `fields_of` yields `wrapped=2`. The landed instrument
must therefore adopt an **explicit blank-line terminator** — reusing C14's
`fields_of` as-is would inflate the wrapped-field count by one false positive.

## 4. The wrapped field reads 4/4 tokens under block extraction

```
corpus/knowledge/linguistics/phonetics-phonology.md
  A single-line                          n=0   []
  B block, newline-join (C14 shape)      n=4   prosody.md, sound-change.md,
                                               sound-symbolism.md, writing-systems.md
  C block, space-join                    n=4   (same four)
  D block, space-join + de-hyphenation   n=4   sound-change.md, sound-symbolism.md,
                                               tone-prosody.md, writing-systems.md
```

Classes at `dfb0719` (entry dir `corpus/knowledge/linguistics/`):

| token | class | reason |
|---|---|---|
| `sound-symbolism.md` | **fallback** | exists, but Tier 1 fails at r39 (linguistics held 21 entries; the file was not among them) |
| `writing-systems.md` | **fallback** | same |
| `sound-change.md` | **unresolved** | no such file anywhere in the repo |
| `prosody.md` (B/C) / `tone-prosody.md` (D) | **unresolved** | no such file anywhere in the repo |

`git ls-tree -r --name-only HEAD` over the whole repo returns only
`corpus/knowledge/linguistics/sound-symbolism.md` and
`corpus/knowledge/linguistics/writing-systems.md` among the four candidate names
— `sound-change.md`, `tone-prosody.md` and `prosody.md` exist nowhere. The
existing file count in `corpus/knowledge/linguistics/` is 21 at `dfb0719` and
**24** at HEAD, i.e. it has grown since — which is exactly why the two live
tokens were `fallback` at r39 and are `direct` at HEAD (below).

So the "2 phantom attributions" of `claims.json:14` are real as *unresolved*
tokens (`sound-change.md`, and the mangled `prosody.md`), but Ca04 D1's
"of which 2 exist (would be `direct`)" is wrong for `dfb0719`: at the tree the
census is taken on, both live tokens are `fallback`, not `direct`.

## 5. The hyphen-wrap hazard is real and is a token-identity choice

`phonetics-phonology.md:76` ends `... sound-change.md, tone-` and `:77` begins
`  prosody.md, sound-symbolism.md, writing-systems.md` (both bytes read this
seat). A line-break join that merely concatenates yields the **mangled**
`prosody.md`; only de-hyphenation recovers the intended `tone-prosody.md`.
Measured three ways:

```
nl-join (no merge)   -> prosody.md
dehyphen (drop "-")  -> toneprosody.md     # over-merge
dehyphen (keep "-")  -> tone-prosody.md    # intended name
```

The landed tool must pick and document one. **Recommendation: drop the hyphen
and merge (`tone-prosody.md`)**, so the token names the intended sibling the
corpus entry itself declares — the entry's own prose reads "prospective sibling
files: sound-change.md, tone-prosody.md, sound-symbolism.md, writing-systems.md"
(`corpus/knowledge/linguistics/phonetics-phonology.md:76-77`). Note this
recommendation is **this seat's judgement, not a landed rule**: the policy's §5.5
does *not* name `tone-prosody.md` (this seat's grep of
`reports/round-39/calib/basename-couples-policy.md` and the Ca03 draft for
`tone-prosody` returns no match; the only `sibling` match in the draft is
`Ca03-basename-policy.md:277`, listing `phonology-basics.md`,
`naming-and-onomastics.md`, `honorifics-and-register.md` as seeds from
`language-contact.md:7`). The count is **4 either way** — this choice moves which
*token string* is unresolved, not the number, so it cannot be used to make the
census look better.

## 6. Predicted corrected census — the numbers the landed tool must reproduce

**At `dfb0719` (r39 close tree, 212 entries)** — the comparable revision:

| extractor | refs | direct | fallback | ambiguous | unresolved | distinct |
|---|---|---|---|---|---|---|
| A single-line (filed) | 2504 | 2335 | 163 | 0 | 6 | 5 |
| **B block (predicted)** | **2508** | **2337** | 163 | 0 | **8** | **7** |

Delta: **+4 refs, +2 direct, +2 unresolved, +2 distinct**. Arithmetic:
`2508 = 2337 + 163 + 0 + 8`. The r39 policy's `2504 = 2335 + 163 + 0 + 6`
becomes `2508 = 2337 + 163 + 0 + 8` on the same tree.

**At HEAD (220 entries, `ac47c78`)** — the current live tree:

| extractor | refs | direct | fallback | ambiguous | unresolved |
|---|---|---|---|---|---|
| A single-line | 2607 | 2435 | 166 | 0 | 6 |
| **B block (predicted)** | **2611** | **2437** | 166 | 0 | **8** |

Corpus growth from 212 to 220 entries adds +103 refs, +100 direct, +3 fallback
and leaves the unresolved population unchanged at 6 (A) — all six pre-existing
tokens are unrelated to this fix.

## 7. Unresolved token ledger (variant B, `dfb0719`) — all 8, all dispositioned

| token | n | class | disposition |
|---|---|---|---|
| `-gate.md` | 1 | glob fragment | policy §5.6 artifact (`gate-frozen-run-standard.md:15`); policy forbids counting it as a finding |
| `../linguistics/phonology-sanity.md` | 2 | dangling | the r19 X26-1 phantom, still live at `corpus/knowledge/verification/label-channel-routing-verification.md:14` |
| `honorifics-and-register.md` | 1 | never-written seed | `corpus/knowledge/linguistics/language-contact.md:7` |
| `naming-and-onomastics.md` | 1 | never-written seed | same line |
| `phonology-basics.md` | 1 | never-written seed | same line |
| `sound-change.md` | 1 | never-written seed | **new under block extraction** — `phonetics-phonology.md:76` |
| `prosody.md` (B/C) | 1 | mangled artifact | **new under block extraction** — `phonetics-phonology.md:76-77` line break; resolves to `tone-prosody.md` under de-hyphenation (variant D) |

All 8 carry a named disposition; **none is an unexplained phantom**. The five
pre-existing tokens reproduce the filed r39 distinct set exactly, so the fix is
additive and does not disturb the r39 population.

## 8. What the landed tool must reproduce (acceptance for O04/O05)

1. Single-line control at `dfb0719` = `2504 / 2335 / 163 / 0 / 6` (5 distinct).
2. Block extraction at `dfb0719` = `2508 / 2337 / 163 / 0 / 8` (7 distinct).
3. Wrapped-field census = **1**, named `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`.
4. `phonetics-phonology.md` couples tokens = **4** (0 under the single-line extractor).
5. `conlang-methodology.md` is **not** wrapped (blank-line stop required).
6. The de-hyphenation choice is declared; the token count stays 4 either way.

Any landed tool reporting a wrapped-field count of 2, or reading
`sound-symbolism.md`/`writing-systems.md` as `direct` at `dfb0719`, is
reproducing C14's blank-line-blind `fields_of` rather than a corrected parser.

## 9. Second finding (outside claim O's scope, filed for the integrator)

**The landed r39 policy is truncated.** `reports/round-39/calib/basename-couples-policy.md`
is **108 lines / 5832 bytes** and its last bytes are
`...\n(\`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1\`):\n` — it ends on
§6's lead-in sentence with the fenced recipe, the filed-run output and §7
entirely absent. Measured: `grep -c '```'` = 0, `grep -c RESULT` = 0,
`grep -c 2504` = 0. The authoring draft
`reports/round-39/calib/Ca03-basename-policy.md` is **360 lines / 19409 bytes**
and carries all of them. The policy landed in one commit (`fd55e1f`), so the
truncation is a landing defect, not a later edit.

Consequence for this round: the policy's §6 recipe — the artifact claim O's
`after_required` calls "the r39 C12 runbook's resolver or a tools/harness couples
checker" — **is not in the landed bytes at all**. There is no durable script to
patch; a successor instrument must be authored fresh (which is what queue row
`r39-basename-successor-instrument` already routes to r43/r44). This is a
correction record, not an edit: filed bytes stay untouched.

## 10. Independent convergence with O04 (read after this seat's §1-§6 were computed)

This seat's §1-§6 were computed before reading any peer fragment. On reading
`reports/round-42/op/O04-verify.md` afterwards, its independently produced
numbers agree with mine exactly:

| quantity | O03 (this seat) | O04 (`O04-verify.md:127-129`) |
|---|---|---|
| `dfb0719` single-line | 2504 / 2335 / 163 / 0 / 6 (5 distinct) | 2504 / 2335 / 163 / 0 / 6 (5 distinct) |
| `dfb0719` block | **2508 / 2337 / 163 / 0 / 8** (7 distinct) | **2508 / 2337 / 163 / 0 / 8** (7 distinct) |
| wrapped fields | 1 | 1 |
| continuation lines | 5 | 5 |

O04 reached the same substantive conclusion independently: the census is **not**
"2504 minus the phantoms" (`O04-verify.md:142,196`), and the wrapped field's two
absent names are `sound-change.md` and `tone-prosody.md` (`:139`). Two seats
built separately and agreed on every number, which satisfies the claim's "two
independent verifiers" threshold for the census arithmetic.

Two points where O04 adds evidence this seat did not produce, recorded here
because they bear on §6's acceptance items:

- O04 measured the filed r19 instrument on the affected entry
  (`O04-verify.md:168`): `couples=0 unresolved=[]`, `TOTAL 0/1`, `exit 2` — the
  single-line extractor reports a **clean-looking zero**, which is the concrete
  false-green the fix must eliminate.
- O04 files a control requirement against O02/O05 (`:173-176`): the wrapped-field
  control must be built by hand, because a control whose wrapped field is
  auto-generated would inherit the same extractor. This seat's §6 items 3-5 are
  the measurement counterpart of that requirement.

## Owed

- **O04/O05 (verifiers):** reproduce §6's six acceptance items on an isolated
  copy; in particular confirm the `2508 = 2337 + 163 + 0 + 8` arithmetic and the
  `wrapped=1` census independently. My recount is a read-only synthetic
  re-parse, not a landed-tool run.
- **The landed tool's host is still unconfirmed** (K01's mission). My recount
  does not identify it; no `tools/harness/` couples checker exists in the tree
  (this seat's read). If K01 finds a different host, §6's numbers are the target
  but §3's blank-line terminator requirement applies to that host's parser too.
- **Integrator (new record, never an edit):** file the r39 policy truncation
  (§9) as a defect row, and amend queue row `r39-basename-successor-instrument`
  to say the policy's §6 recipe is absent from the landed bytes — the successor
  instrument's spec cannot cite a recipe that is not there.
- **`.scratch/o03/recount.py` is ephemeral** (gitignored). If the round wants a
  durable re-runner, it must be re-authored under the landing round's own
  instrument path; this seat's out path is a fragment only.
- **to-verify:** the `prosody.md` line-break mangling's presence in C14's own
  historical distinct set was not re-derived by this seat (Ca04 flagged the same
  item `to-verify`); I measured only the current tree.

## Citations

- Mission and binding rules: `reports/round-42/targets.json` (seat `O03`);
  `reports/round-42/claims.json:12-24` (claim O before/after, counting command,
  thresholds); `REGIMEN.md:19` (position 10 provider/model), `:25-43` (per-round
  contract).
- Extractor hosts: `reports/round-19/audit/entry-audit.py:31,34-42,74-96`
  (`:75` the single-line capture, `:80` MDREF scan, `:92` `os.path.isfile`);
  `reports/round-35/cov/C14-audit-6-10.md:208-214` (`frontmatter_block`, `## `
  terminator), `:225-236` (`fields_of`, `:234` the blank-line-blind append),
  `:249-260` (`basename_index`, glob `corpus/knowledge/*/*.md`), `:263-288`
  (`couples_refs`).
- Policy: `reports/round-39/calib/basename-couples-policy.md:14-25` (§1 token
  extraction), `:27-48` (§2 two-tier/four-class), `:71-102` (§5 limits incl.
  §5.6 glob fragments), `:104-108` (§6 lead-in, **file ends here**);
  authoring draft `reports/round-39/calib/Ca03-basename-policy.md:1-360`.
- Ca04 D1: `reports/round-39/calib/Ca04-verify.md:78-93` (D1 text), `:107-115`
  (Owed incl. the to-verify full block-parser recount), `:131-134` (D1 instance).
- Queue rows: `reports/round-40/op/defect-queue-v2.json:362-369`
  (`N6-couples-extractor-wrapped-field`), `:322-331`
  (`r39-basename-successor-instrument`), `:204-210`
  (`O12-runner-isolation-hazard`).
- Corpus instance: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
  (head line + 5 continuations; `:76` ends `tone-`, `:77` begins `prosody.md`);
  `corpus/knowledge/linguistics/conlang-methodology.md:7-9` (single line, blank
  line 8, prose from line 9 — the C14 false-positive); `corpus/knowledge/linguistics/language-contact.md:7`
  (three never-written seeds); `corpus/knowledge/verification/label-channel-routing-verification.md:14`
  (`../linguistics/phonology-sanity.md`); `corpus/knowledge/verification/gate-frozen-run-standard.md:15`
  (`-gate.md` glob fragment).
- Command outputs (this seat, 2026-10-19, lane root at `ac47c78`,
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, all read-only; script
  `.scratch/o03/recount.py`, raw logs `.scratch/o03/out-r39.txt`,
  `.scratch/o03/out-head.txt`):
  (a) `python3 -B .scratch/o03/recount.py dfb0719` -> variant A
  `212 fields, 2504 refs, 2335/163/0/6, 5 distinct` = **MATCH-FILED: True**;
  variant B `wrapped=1, 2508 refs, 2337/163/0/8, 7 distinct`;
  (b) `... HEAD` -> A `2607 / 2435/166/0/6`; B `wrapped=1, 2611 / 2437/166/0/8`;
  (c) `git ls-tree -r --name-only dfb0719 -- corpus/knowledge | grep -c '\.md$'`
  -> `212`; `ls corpus/knowledge/*/*.md | wc -l` -> `220`; per-partition at HEAD
  `civilizations 94, culture-material 25, linguistics 25, myth-symbol 23,
  synthesis 29, verification 24`; at `dfb0719` `linguistics 21`;
  (d) `git ls-tree -r --name-only HEAD | grep -E 'sound-change|tone-prosody|prosody|sound-symbolism|writing-systems'`
  -> only `sound-symbolism.md`, `writing-systems.md`;
  (e) `grep -rn 'couples:' corpus/knowledge/*/*.md | wc -l` -> `239`;
  blank-line-stop wrapped-field scan -> `wrapped fields: 1`;
  (f) truncation probe -> landed `bytes=5832 lines=108`, draft
  `bytes=19409 lines=360`, `has '```': False`, `has 'RESULT': False`,
  `has '2504': False`;
  (g) de-hyphenation probe -> `nl-join: prosody.md`, `drop '-': toneprosody.md`,
  `keep '-': tone-prosody.md`.
- No filed byte was edited; no `run-validation.py` was executed in-tree or in a
  copy; nothing was staged under `corpus/`; no git, network, or install action.
