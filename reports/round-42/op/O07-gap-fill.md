- Seat: O07 | executor | claim O | date 2026-10-19 | baseline ac47c78

# O07 — spare gap-fill: the wrapped-field census, the join-separator hazard, and the phantom disposition

Spare gap-fill for claim O (operability, the N6 fix). No other seat owns this
work: K01 scouts the extractor host, O01 drafts the patch, O02 the controls, O03
the predicted census, O04/O05 verify. The gap I fill is the one Ca04 filed
`to-verify` — *"a full block-parser couples recount corpus-wide (this seat's
partial: exactly 1 wrapped field, 4 tokens, 2 phantom)"*
(`reports/round-39/calib/Ca04-verify.md:115`) — plus the disposition the claim's
`after_required` demands for the two phantom attributions
(`reports/round-42/claims.json:16`). Read-only throughout: no filed byte edited,
no `run-validation.py` executed, no git/network/install. All commands from the
lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

## 1. Corpus-wide wrapped-field census (closes Ca04's `to-verify`)

Ca04 asserted "the corpus has **exactly one** wrapped field" from a single-file
observation. I enumerated all 220 entries (`corpus/knowledge/*/*.md`, 6
partitions) over the seven header fields, testing each field line for an indented
non-field continuation:

| field | present | wrapped |
|---|---|---|
| topic | 220 | 2 |
| sources | 220 | 104 |
| **couples** | **220** | **1** |
| source | 152 | 0 |
| verified-at | 220 | 1 |
| recheck | 220 | 0 |
| gap | 7 | 0 |

**Result: Ca04's claim is confirmed and now measured, not assumed.** 108 header
fields wrap corpus-wide, but exactly **one** of them is a `couples` field:
`corpus/knowledge/linguistics/phonetics-phonology.md:72-77`. The exposure is
narrow but real — and note the 104 wrapped `sources` fields are untouched only
because the `sources` leg is read block-wise already
(`reports/round-19/audit/entry-audit.py:57-73`), which is precisely the shape
the `couples` leg lacks.

## 2. The defect is two independent rules, and Ca04 named only one

Ca04's D1 describes one rule ("single-line extractor zeroes wrapped fields"). The
enumeration above shows the hazard is **two** rules, and the second one is the
subtler:

1. **Block extent.** `couples_targets` captures one physical line
   (`re.search(r"^- couples:\s*(.*)$", text, re.M)` —
   `reports/round-19/audit/entry-audit.py:75`), so the 5 continuation lines at
   `:73-77` are never read. Fix: read through the next `- <field>:` line, as the
   `sources` leg and C14's `frontmatter_block`
   (`reports/round-35/cov/C14-audit-6-10.md:208-222`) already do.
2. **Join separator.** This one is *not* fixed by adding a block parser. C14 has
   a block parser and still reads the field wrong: its `fields_of` joins
   continuations with `"\n"` (`C14-audit-6-10.md:229-234`). Applied to
   `:76-77`, where the physical line break falls **inside** the filename
   `tone-prosody.md` (`… sound-change.md, tone-` / `prosody.md, …`), the newline
   splits the token. Measured on the live bytes:

   | join rule | tokens from `:72-77` | correct? |
   |---|---|---|
   | single-line (r19) | `[]` | no — 0 captured |
   | `"\n"` (C14 as filed) | `prosody.md`, `sound-change.md`, `sound-symbolism.md`, `writing-systems.md` | no — mangled |
   | `" "` (space join) | identical to the newline row | no — mangled |
   | `""` (empty join) | the correct 4 | works here, but merges at *every* wrap |
   | hyphen-preserving (`s+n` when `s` ends `-`) | the correct 4 | **yes** |

   Space and newline join fail identically: neither can bridge `tone-` to
   `prosody.md`, and `MDREF` needs the `.md` in the same match, so both yield
   the mangled `prosody.md`. The empty join happens to recover the right tokens
   on *this* field only because no other wrap point falls inside a token — it
   would fuse the last word of one continuation with the first of the next
   everywhere else, so it is not a general rule. The hyphen-preserving rule is
   the principled one: space normally, no separator only across a soft wrap.

   So C14's parser **manufactures a phantom token** (`prosody.md`) and **hides a
   real one** (`tone-prosody.md`). Ca04 called the mangling
   "an extractor hazard *no* current instrument handles"
   (`Ca04-verify.md:89-90`) and left `prosody.md` `to-verify`; this table is that
   derivation. **The block extent and the join rule must land together** or the
   fix trades one wrong census for another. Scope note: this is the *only*
   hyphen-boundary continuation in the whole corpus (2 hits corpus-wide, both in
   `phonetics-phonology.md` — `:76` and a prose line at `:90` that yields no
   `.md` token), so the hazard is one field wide today but the rule is
   corpus-general.

   **Correction to K01 §4** (`K01-n6-scout.md:138-141`), for O04/O05: K01's
   join table lists `" ".join` → "`tone-` and `prosody.md` (two tokens)" and
   `"".join` → "`toneprosody.md`". Both labels are wrong — I measured the same
   two rules on the same bytes and got the newline-join result for space, and
   the correct 4 for empty join. K01's own command output two lines later
   (`K01-n6-scout.md:146-147`) contradicts its own table:
   `MDREF empty-join : ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']`.
   The *conclusion* K01 draws (de-hyphenation is required) is unaffected; only
   the two intermediate rows are mislabelled, and the `toneprosody.md` failure
   mode K01 describes is not reachable by `"".join` — it would require
   deleting the hyphen *after* joining, which no candidate rule does.

## 3. Corrected recount — calibrated against the filed policy

My re-implementation reproduces the filed r39 arithmetic **exactly** under the
policy's own extractor, which is what licenses the corrected numbers beside it.
Both trees are read from git (`git ls-tree` / `git show`), never the worktree, so
existence and the basename index are judged on the same revision.

| tree | extractor | refs | direct | fallback | ambiguous | unresolved | distinct |
|---|---|---|---|---|---|---|---|
| `dfb0719` (r39) | r19 single-line | 2504 | 2335 | 163 | 0 | 6 | 5 |
| `dfb0719` (r39) | C14 `"\n"` join | 2508 | 2337 | 163 | 0 | 8 | 7 |
| **`dfb0719` (r39)** | **fixed (de-hyphen)** | **2508** | **2337** | **163** | **0** | **8** | **7** |
| `ac47c78` (r42) | r19 single-line | 2607 | 2435 | 166 | 0 | 6 | 5 |
| `ac47c78` (r42) | C14 `"\n"` join | 2611 | 2437 | 166 | 0 | 8 | 7 |
| **`ac47c78` (r42)** | **fixed (de-hyphen)** | **2611** | **2437** | **166** | **0** | **8** | **7** |

The first row is Ca03's filed Part 2 line `212/2504 → 2335/163/0/6`
(`reports/round-39/calib/Ca03-basename-policy.md:35-36,268,355`) and Ca04's
independent re-run (`Ca04-verify.md:29-31`) — **reproduced to the integer**. The
policy's own arithmetic therefore holds: `2504 = 2335 + 163 + 0 + 6`. The
corrected baseline is `2508 = 2337 + 163 + 0 + 8`.

**The whole delta is the one wrapped field, and it is monotone.** +4 refs, +2
direct, +2 unresolved; `fallback` and `ambiguous` are unchanged at *every* tree
and under *every* rule. That is the property the fix must preserve and the reason
it cannot false-green: the +4 tokens cannot enter the fallback class (the two
existing ones resolve direct; the two prospective ones have no basename hit
anywhere), so no entry's fallback count can move. `entries` and `fallback` are
bit-identical across all six runs.

Caveat, stated plainly: my Part-1-style eleven-entry cross-check is **not**
re-derived here (I did not reproduce `334 = 319 + 15`); this fragment covers the
corpus-wide leg only, which is the leg Ca04 left owed.

## 4. Disposition of the two phantom attributions (the claim's `after_required`)

The corrected unresolved set is 8 refs / 7 distinct. Four of the seven are
**not dangling pointers at all** — they are names introduced under a literal
"future file" marker inside the same field:

| # | token | refs | class | citation |
|---|---|---|---|---|
| 1 | `-gate.md` | 1 | glob fragment | `corpus/knowledge/verification/gate-frozen-run-standard.md:15`; policy §5.6 already forbids counting it |
| 2 | `../linguistics/phonology-sanity.md` | 2 | **real phantom** | `label-channel-routing-verification.md:14`, `typed-label-routing-workflow.md:16`; r19 X26-1, still live |
| 3 | `honorifics-and-register.md` | 1 | prospective seed | `language-contact.md:7` |
| 4 | `naming-and-onomastics.md` | 1 | prospective seed | `language-contact.md:7` |
| 5 | `phonology-basics.md` | 1 | prospective seed | `language-contact.md:7` |
| 6 | `sound-change.md` | 1 | **prospective seed** | `phonetics-phonology.md:76` |
| 7 | `tone-prosody.md` | 1 | **prospective seed** | `phonetics-phonology.md:76` |

**Finding — the two "phantom attributions" the claim names are prospective
seeds, not phantoms.** Ca04 filed `sound-change.md` and `tone-prosody.md` as
"2 phantom" targets. They are named under the literal marker *"prospective
sibling files:"* at `phonetics-phonology.md:76`, in the same field as two
siblings that *were* written (`sound-symbolism.md`, `writing-systems.md`). This
is the **same marker class** as the three never-written seeds at
`language-contact.md:7` ("sibling knowledge files to seed: `phonology-basics.md`,
… `naming-and-onomastics.md`, `honorifics-and-register.md`, …") — and the policy
already dispositions those three as non-blocking named seeds
(`Ca03-basename-policy.md:271-278`). So the corpus's 8 corrected unresolved refs
disposition cleanly and consistently as:

- 1 glob fragment — policy §5.6, forbidden to count;
- 2 real phantoms — the r19 X26-1 mis-prefix `../linguistics/phonology-sanity.md`
  (the successor fix route is the next re-freeze, `claims.json:27`);
- 5 prospective seeds under an explicit future-file marker — 3 in
  `language-contact.md`, 2 in `phonetics-phonology.md`.

Zero unexplained dangling couples pointers remain. This satisfies the claim's
"zero phantom attributions remaining or each dispositioned" via the second
branch.

Note this finding is *new relative to the filed record*: Ca04 had the field's
text available and still read the two names as phantoms
(`Ca04-verify.md:81-84`), so the disposition is not merely a re-citation — it
reclassifies two filed attributions on the strength of the marker at `:76`.

## 5. Drafted policy clause (integrator-applied; the r39 document stays filed)

Fenced for the integrator per `shared_rules` — corpus/instrument changes are
drafted, never staged. This amends `reports/round-39/calib/Ca03-basename-policy.md`
§1 as a successor revision; the filed bytes are not edited here.

```markdown
## 1. Token extraction (fixed, so every audit counts the same population)

- Field: the `- couples:` **field**, not one physical line — the value runs from
  the `- couples:` line through the last indented continuation line, stopping at
  the first blank line, the next `- <field>:` line, or the first `## ` heading
  (whichever comes first). Both a blank-line stop and a `##` stop are
  load-bearing: `couples` is the *last* header field in all 220 entries, so a
  next-field-only bound runs to EOF — see §5.1. Block extent per
  `reports/round-35/cov/C14-audit-6-10.md:208-222`; the blank-line stop is
  `tools/gates/provenance-audit.py:244-261` `field_block()`, already correct
  in-repo (K01 §3), and numerically identical to the `##` bound on both trees.
  Measured corpus-wide: 108 header fields wrap; exactly one is a `couples`
  field (`corpus/knowledge/linguistics/phonetics-phonology.md:72-77`).
- Continuations are joined with a **single space**, except that a continuation
  is concatenated with **no separator** when the preceding text ends in `-`.
  Rationale: physical line breaks fall inside filenames (`tone-` / `prosody.md`,
  `phonetics-phonology.md:76-77`); a `"\n"` join (C14 as implemented,
  `C14-audit-6-10.md:229-234`) manufactures the phantom `prosody.md` and hides
  `tone-prosody.md`. Exactly one such boundary exists corpus-wide.
- Tokens: every match of `[A-Za-z0-9_./{},\-]+\.md` in the joined field value
  (`entry-audit.py:31`), brace-expanded one level (`entry-audit.py:34-42`),
  deduplicated per entry. A `:NN` anchor after a token is not part of the token.
- Unit: per-entry deduplicated tokens. Cross-entry repeats count once per entry;
  a global-distinct total may be cited alongside it.
- Prospective seeds: a token named under a literal future-file marker inside the
  field ("prospective sibling files:", "sibling knowledge files to seed:") is a
  **documented prospective seed**, not an unresolved couples finding, and is not
  a blocker (C12 row 2 treatment, `reports/round-35/cov/C12-audit-runbook.md:37`).
  Current population: 5 — `sound-change.md`, `tone-prosody.md`
  (`phonetics-phonology.md:76`); `phonology-basics.md`,
  `naming-and-onomastics.md`, `honorifics-and-register.md` (`language-contact.md:7`).
```

Drafted tool change for the successor instrument (the r19 instrument stays as
filed; `reports/round-19/audit/entry-audit.py:74-77`). The stop condition is not
optional (see §5.1). Three seats converged on this shape independently — K01 §3
via `tools/gates/provenance-audit.py:244-261` `field_block()`, O04 §1, O05 §1(c)
— and all three use the **indent rule** ("a continuation is an indented non-blank
line"), which I verified agrees with my blank-line/`##` rule on all 220 entries
(zero divergence, both trees):

```diff
 def couples_targets(text, path):
-    m = re.search(r"^- couples:\s*(.*)$", text, re.M)
-    if not m:
-        return [], []
-    line = m.group(1)
+    lines = text.splitlines()
+    start = next((i for i, l in enumerate(lines) if re.match(r"^- couples:", l)), None)
+    if start is None:
+        return [], []
+    # block extent: keep only indented, non-blank continuation lines
+    # (the field always ends at the first non-indented line; `couples` is the
+    # last header field in all 220 entries, so nothing else bounds it)
+    parts = [lines[start].split(":", 1)[1].strip()]
+    for l in lines[start + 1:]:
+        if not re.match(r"^[ \t]+\S", l):
+            break
+        parts.append(l.strip())
+    # join continuations; no separator after a hyphen (a line break can fall
+    # inside a filename: "tone-" + "prosody.md" -> "tone-prosody.md")
+    line = parts[0]
+    for nxt in parts[1:]:
+        line = line + nxt if line.endswith("-") else line + " " + nxt
     refs = set()
```

### 5.1 Two pitfalls a successor implementer will hit (both observed in this seat's own drafts)

Both were found by running the draft against the live corpus, not by reading it.
They are recorded because each one *re-manufactures the phantom the fix exists to
remove*, so a fix that looks correct on `tone-prosody.md` can still emit
`prosody.md`.

1. **A next-field-only bound runs to EOF.** `couples` is the *last* header field
   in all 220 entries (no `- status:`, no field after it — the header census in
   §1). A bound of `(?=\n- [a-z-]+:|\Z)` therefore never terminates on
   `phonetics-phonology.md:72-77` and captures the whole body. The `:279` prose
   line then re-supplies `sound-change.md` and `tone-prosody.md` *and* the
   mangled `prosody.md` from the `:76-77` pair. Measured: that bound yields 5
   tokens including `prosody.md`, vs the correct 4. **The stop condition is
   load-bearing** — a blank line or a `## ` heading must end the block — which is
   why §1's clause states it explicitly and why the diff walks lines rather than
   relying on a lookahead alone.
2. **A capture that spans newlines must not then re-append them.** This pitfall
   bites the *regex-capture* form of the fix (the one I first drafted): with
   `m = re.search(r"^- couples:(.*(?:\n(?!- [a-z-]+:|## ).*)*)", …)`, `m.group(1)`
   already spans the continuations and `group(1).strip()` keeps the internal
   newlines. Taking `[group(1).strip()] + splitlines()[1:]` then appends
   continuations that are *already inside* element 0, so the joined string holds
   the field twice and the duplicate copy re-supplies `prosody.md`. Measured:
   `refs=2612, unresolved=9, distinct=8` vs the correct `2611 / 8 / 7`. The
   line-walking form in the diff above makes this structural — it never has a
   multiline capture to mis-split — but any implementer who prefers the regex
   must split on *all* lines of the capture, never skip the first.

Both drafts were discarded; the diff above is the corrected one, and §6's
numbers are from the exact code as written there.

### 5.2 Convergence with the sibling seats (independent derivations)

This fragment was written in parallel with K01 and O03 and cross-checked after
they landed. Three seats, three implementations, the same arithmetic:

| seat | r39 `dfb0719` | r42 `ac47c78` |
|---|---|---|
| this seat (§3) | `2508 → 2337/163/0/8` | `2611 → 2437/166/0/8` |
| `scout/K01-n6-scout.md:170` | — | `2611 → 2437/166/0/8` |
| `op/O03-predicted.md:143-154` | `2508 → 2337/163/0/8` | `2611 → 2437/166/0/8` |
| `op/O04-verify.md:36-56` | 1 wrapped field (census) | 1 wrapped field (census) |
| `op/O05-traps.md:52-58,80-81` | `2508 → 2337/163/0/8` | — |

K01 §3 names a better host than my first regex: `tools/gates/provenance-audit.py:244-261`
`field_block()` is already-correct indentation-bounded extraction, and the drafted
diff above now uses its indent-stop semantics. I verified the indent rule, the
blank-line stop, and the `##` stop all agree on all 220 entries (zero divergence,
both trees) — the *extent* rule is not the load-bearing part; the *join* rule is.

**Three corrections to sibling seats, for O04/O05 to adjudicate.**

1. **O03's r39 per-token attribution.** `op/O03-predicted.md:89-90` reports the
   wrapped field's two existing targets as `fallback` at `dfb0719`, "because
   `corpus/knowledge/linguistics/` held only 21 entries; the file was not among
   them". That mechanism is wrong: both files **do** exist at that revision —
   `git cat-file -e dfb0719:corpus/knowledge/linguistics/sound-symbolism.md` and
   `…/writing-systems.md` both succeed (the partition held 21 *entries*, and both
   are among them). Tier-1 candidate `<entry-dir>/sound-symbolism.md` therefore
   resolves, so the two are `direct`, not `fallback` — consistent with this
   seat's §3 `direct` rising by exactly +2. O03's *counts* match mine; only its
   per-token attribution differs, and the `direct` reading is the correct one.
2. **K01's §4 join table.** `K01-n6-scout.md:138-141` labels `" ".join` as
   producing "`tone-` and `prosody.md` (two tokens)" and `"".join` as producing
   `toneprosody.md`. Both are wrong — measured on the same bytes, `" ".join`
   gives the mangled `prosody.md` (like the newline join) and `"".join` gives the
   correct 4. K01's own command output two lines later (`:146-147`) contradicts
   its table. **O05 independently reached the same correction**
   (`op/O05-traps.md:66-73`, its rows B/C/D), so this is two seats against one.
3. **O04's false start is a real rule constraint.** `op/O04-verify.md:47-56`
   records that a `## `-only bound reported 2 wrapped fields, swallowing an
   unindented prose line at `conlang-methodology.md:9`. My first diff had exactly
   that shape, which is why the drafted diff above now uses the indent rule
   rather than a heading bound.

**Agreement is exact on the numbers** — four seats, four implementations,
`2508 → 2337/163/0/8` and `2611 → 2437/166/0/8`, and the `+4 / +2 direct / +2
unresolved` delta with `fallback` and `ambiguous` pinned. The disagreements are
all in per-token labelling, not arithmetic.

**The false-green O05 found, which changes the acceptance test.** Space-join and
plain-concat produce *identical tallies* (`2508 → 2337/163/0/8`) with *different
token sets* — so claim O's stated threshold "the wrapped field reads 4/4 targets"
(`reports/round-42/claims.json:18`) **passes on the wrong fix**. The landed check
must assert token identity: `prosody.md` absent, `tone-prosody.md` present (§6).

## 6. What the landed instrument must reproduce

These are the falsifiable numbers the delivered extractor has to match, so O03's
prediction and O04/O05's verification have a target:

- r39 tree `dfb0719`: `refs=2508 -> direct=2337 fallback=163 ambiguous=0 unresolved=8` (7 distinct).
- r42 tree `ac47c78`: `refs=2611 -> direct=2437 fallback=166 ambiguous=0 unresolved=8` (7 distinct).
- Wrapped-field positive control: `couples_targets` over
  `phonetics-phonology.md` returns exactly
  `{sound-change.md, sound-symbolism.md, tone-prosody.md, writing-systems.md}`
  and **never** `prosody.md`.
- Invariants: `fallback` and `ambiguous` must be *unchanged* by the fix at both
  trees (163 / 0 and 166 / 0); `direct + fallback + ambiguous + unresolved == refs`.
- **Assert the token set, never a count.** O05 (`op/O05-traps.md:66-86`) measured
  that space-join and plain-concat give *identical tallies* at both trees
  (`2508 → 2337/163/0/8`) with *different token sets* — `prosody.md` versus
  `tone-prosody.md`. So a count-only threshold cannot distinguish the correct fix
  from the mangled one; the check must be
  `prosody.md not in tokens and tone-prosody.md in tokens`. This seat's §2 table
  and O05's table B/C/D agree on that; K01's §4 labels do not (§2 correction).

## Owed

- **Integrator**: the fenced §1 clause and the tool diff are unapplied drafts.
  Land the clause as a successor revision to the r39 policy (filed bytes
  untouched), or record an explicit refusal; either way close queue row
  `N6-couples-extractor-wrapped-field` (`reports/round-40/op/defect-queue-v2.json:362-368`)
  against the landed instrument's own output, not against this draft.
- **O03/O04/O05**: my §6 targets are the numbers to compare against. My
  re-implementations were throwaway scratch scripts (now deleted), so they are
  not durable evidence — the landed tool must reproduce these numbers
  independently. §5's drafted diff is the one piece of code in this fragment I
  re-ran verbatim from the filed bytes: its added lines were extracted from this
  document, compiled, and run against the live corpus, yielding the wrapped
  field's 4/4 targets and the r42 tally `2611 → 2437/166/0/8` asserted in §6.
- **O03 and K01 carry two mechanism errors** for O04/O05 to judge on: O03's r39
  per-token `fallback` attribution (§5.2) and K01's §4 join-table rows (§2). Both
  seats' *counts* agree with mine; only the per-token labels differ, and the
  corrected labels are given here with measured commands.
- **Not re-derived here** (still owed to another seat): the eleven-entry Part 1
  leg (`334 = 319 + 15`), the §4 group-alignment leg, and the *policy's* §5.1
  C14-delta leg (my §5 is a different section — the drafted clause).
- to-verify: whether any *other* round's filed runner embeds the same
  single-line `couples` regex; I checked only the r19 instrument and C14's
  recipe, not every runner in `reports/round-*/`.

## Citations

- Claim/seat: `reports/round-42/claims.json:16` (O `after_required`, the
  disposition demand), `:18` (two independent verifiers), `:27` (no re-freeze);
  `reports/round-42/targets.json:83-87` (O07 row).
- Defect row: `reports/round-40/op/defect-queue-v2.json:362-368`
  (`N6-couples-extractor-wrapped-field`).
- D1 finding + owed census: `reports/round-39/calib/Ca04-verify.md:78-93`
  (D1), `:89-90` (mangling "no instrument handles"), `:113` (owed recount),
  `:115` (the `to-verify`), `:131-134` (the instance).
- Policy: `reports/round-39/calib/Ca03-basename-policy.md:16-25` (§1),
  `:35-38` (Part 2 arithmetic), `:98-102` (§5.6 glob fragments),
  `:271-278` (the three named seeds), `:268,355` (filed Part 2 line).
- Extractors: `reports/round-19/audit/entry-audit.py:31` (MDREF), `:34-42`
  (brace expansion), `:57-73` (block-wise `sources` leg), `:74-96`
  (`couples_targets`; `:75` the single-line regex);
  `reports/round-35/cov/C14-audit-6-10.md:188,199` (MDREF/FIELD),
  `:208-222` (`frontmatter_block`), `:229-234` (`fields_of`, the `"\n"` join),
  `:252-260` (basename index), `:281` (slash-bearing key).
- The wrapped field: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
  (field), `:76` (the `tone-` / `prospective sibling files:` line), `:77`
  (`prosody.md, …`); `:279` (a *prose* mention of the same two names, outside the
  field — not a couples ref).
- Prospective seeds: `corpus/knowledge/linguistics/language-contact.md:7`.
- Real phantom: `corpus/knowledge/verification/label-channel-routing-verification.md:14`;
  `corpus/knowledge/synthesis/typed-label-routing-workflow.md:16`.
- Glob fragment: `corpus/knowledge/verification/gate-frozen-run-standard.md:15`.
- Disposition rule: `reports/round-35/cov/C12-audit-runbook.md:37` (row 2:
  dangling token is a blocker unless the same line marks it `(to-verify`).
- Digests at baseline `ac47c78` (`sha256sum`, this seat, 2026-10-19):
  `corpus/knowledge/linguistics/phonetics-phonology.md`
  `b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b`;
  `corpus/knowledge/linguistics/language-contact.md`
  `52385e3d81f7d8f8eb1423d408a47bd12c968f1444fd9fc5d77a9c3e691cd409`;
  `reports/round-39/calib/Ca03-basename-policy.md`
  `125ede77e3f50e3c58af61fb2fad246c8378b4dcfc4ee5d1749da8dd53a17850`;
  tree `dfb0719` = `dfb0719711204b5943432034bd80c8dc248acddd`.
- Command outputs (this seat, 2026-10-19, lane root, read-only):
  (a) wrapped-field census over 220 entries → 108 wrapped fields, 1 `couples`
  (§1 table); (b) token set for `:72-77` under the three join rules (§2 table);
  (c) hyphen-boundary scan → 2 corpus-wide, both `phonetics-phonology.md`
  (`:76` yields tokens, `:90` yields none); (d) the six-run recount table in §3,
  r19 extractor on `dfb0719` → `2504/2335/163/0/6` matching the filed line;
  (e) disposition table in §4 from `grep -n` on the named files.
  No filed byte edited; no `run-validation.py` executed; no git/network/install.
