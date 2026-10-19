- Seat: O12 | verifier | claim O | date 2026-10-19 | baseline ac47c78

# O12 — does the r39 policy's arithmetic still hold under the corrected census?

Assignment (verbatim, `reports/round-42/targets.json` seat `O12`): "Verify the r39
policy document's arithmetic still holds under the corrected census (the policy doc
itself stays filed; the correction is a successor note)." Out:
`op/O12-policy-check.md`.

## Verdict

**The filed policy document carries no arithmetic at all — it is a truncated
prefix of the r39 draft, and the 2504 census lives only outside it.** The
arithmetic itself is **reproduced exactly** at the r39 tree and **does move** under
the N6 fix. Three results, each with its own disposition:

1. **Baseline arithmetic: VERIFIED, but not in the filed object.** Re-run of the
   draft's §6 recipe against a full `git archive dfb0719` gives `entries=212
   refs=2504 -> direct=2335 fallback=163 ambiguous=0 unresolved=6` (5 distinct) —
   byte-for-byte the r39 filed reading. The *filed* policy
   (`calib/basename-couples-policy.md`) contains none of it: `grep -c
   '2504\|2335\|163'` → **0**.
2. **Corrected census: the r39 arithmetic does NOT survive, and the fix moves the
   numbers the opposite way from the claim's wording.** At the r39 tree the
   corrected census is `2508 = 2337 + 163 + 0 + 8`; at the live tree
   `2611 = 2437 + 166 + 0 + 8`. Unresolved **rises** 6 → 8; it does not fall.
3. **The `2 phantom attributions` are real and now fully located:** two carriers
   of the X26-1 phantom path (the draft names one). The two *new* unresolved
   tokens the fix exposes are the wrapped field's never-written seeds.

The correction belongs in a successor note, as the mission says; **no filed byte
was edited by this seat**, and the policy document stays exactly as filed.

## 1. The filed object is a truncated prefix (new finding, O12-F1)

| surface | reading | command |
|---|---|---|
| filed policy | 107 lines / 5832 bytes, sha256 `105dfff6…e941cf` | `wc -l -c`; `sha256sum` |
| r39 draft | 359 lines, sha256 `125ede77…a17850` | `sha256sum` |
| relation | filed == draft lines **41–147**, byte-identical | `diff <(sed -n '41,147p' draft) filed` → no output |

The landed file ends mid-sentence at `…no runner invocation
(\`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1\`):` — i.e. it stops at
the exact line where the §6 code fence opens (`Ca03-basename-policy.md:149`) and
therefore omits **§6 (the recipe) and §7 (adoption evidence)** entirely. §1–§5
(extraction, two-tier/four-class resolution, reporting rules, group alignment,
limits) landed complete.

**Why the r39 gate did not catch it.** `reports/round-39/run-validation.py:117-121`
checks the filed policy for exactly one marker, the string `fallback`, which
occurs in the landed §2 (`:36-48`) and §5.1. Nothing in the gate opens the §6
fence or looks for a number. `Ca04-verify.md` verified the *draft* (§6 script run
byte-exact from `Ca03-basename-policy.md:149-258`), so the "policy verified"
verdict is sound about the draft and silent about the truncation. This is a
gate-coverage defect, not a false verification — but the durable object and the
verified object are not the same bytes.

## 2. Baseline arithmetic — reproduced exactly (O12-C1)

Run on a complete r39 tree (`git archive dfb0719 | tar -x -C .scratch/r39full`;
`212` entries), §6 recipe extracted byte-exact from `Ca03-basename-policy.md:150-257`
and executed read-only:

```
== r39 tree dfb0719 (212), policy single-line ==
  entries=212 refs=2504 -> direct=2335 fallback=163 ambiguous=0 unresolved=6
  unresolved distinct=5: -gate.md(x1), ../linguistics/phonology-sanity.md(x2),
    honorifics-and-register.md(x1), naming-and-onomastics.md(x1), phonology-basics.md(x1)
```

This is `MATCH-FILED` on all five numbers against the draft's Part 2
(`Ca03-basename-policy.md:268-269`) and against `Ca04-verify.md:29`. Part 1 and
Part 1b also reproduce exactly: `refs=334 -> direct=319 fallback=15 ambiguous=0
unresolved=0`, `misaligned=0`, `RESULT: PASS`.

**Method note (worth recording).** My first attempt extracted only
`corpus/knowledge` into the r39 scratch tree and read `2335` as `2324`, with
bogus unresolved tokens `AGENTS.md(x7)`, `SCORECARD.md(x1)`, `SKILL.md(x2)`,
`corpus/README.md(x1)`. Cause: Tier 1's lane-root and `corpus/knowledge/` bases
need the lane-root files that the partial extraction omitted, so real `direct`
refs misclassify as `unresolved`. A census re-run must extract the **whole tree**,
not the corpus subtree — the refs are lane-root-relative.

## 3. Corrected census under the N6 fix (O12-C2)

N6 (queue-v2 row `N6-couples-extractor-wrapped-field`, `reports/round-40/op/defect-queue-v2.json`)
is: the single-line extractor silently zeroes the corpus's one wrapped `couples:`
field. Corpus-wide wrapped-field census, both trees:

```
live ac47c78     entries=220 wrapped-couples-fields=1
r39 dfb0719      entries=212 wrapped-couples-fields=1
  → corpus/knowledge/linguistics/phonetics-phonology.md  6 physical lines (:72-77)
```

With block extraction through the next `- field:` and the hyphen continuation
joined (`re.sub(r"-\n\s*", "-", …)`):

| tree | mode | entries | refs | direct | fallback | ambiguous | unresolved | distinct |
|---|---|---|---|---|---|---|---|---|
| `dfb0719` | policy single-line (filed) | 212 | 2504 | 2335 | 163 | 0 | 6 | 5 |
| `dfb0719` | **N6-fixed block** | 212 | **2508** | **2337** | 163 | 0 | **8** | **7** |
| `ac47c78` | policy single-line | 220 | 2607 | 2435 | 166 | 0 | 6 | 5 |
| `ac47c78` | **N6-fixed block** | 220 | **2611** | **2437** | 166 | 0 | **8** | **7** |

So the r39 arithmetic `2504 = 2335 + 163 + 0 + 6` becomes, on the same tree,
**`2508 = 2337 + 163 + 0 + 8`**; on the delivered tree **`2611 = 2437 + 166 + 0 + 8`**.

Delta at fixed tree: **+4 refs, +2 direct, +2 unresolved, +2 distinct**.

**The join rule is load-bearing and must be specified.** Four plausible
continuation joins all yield 4 tokens, but two of them are wrong:

| join rule | tokens recovered | matches the 4 named targets? |
|---|---|---|
| `"\n".join(parts)` (C14's shape) | `sound-change.md`, `prosody.md`, `sound-symbolism.md`, `writing-systems.md` | **no** — splits `tone-prosody.md` |
| `" ".join(parts)` | same as above | **no** |
| `re.sub(r"-\n\s*","",…)` | `sound-change.md`, `toneprosody.md`, … | **no** — drops the hyphen |
| `re.sub(r"-\n\s*","-",…)` | `sound-change.md`, **`tone-prosody.md`**, `sound-symbolism.md`, `writing-systems.md` | **yes, 4/4** |

Only the hyphen-preserving join recovers the field's 4 named prospective siblings.
A block parser that joins with `\n` or a space silently mangles
`tone-` + `prosody.md` into a token that never existed; the zero-hyphen variant
mints `toneprosody.md`. **The fix must therefore be specified as "continuation
lines de-hyphenated, hyphen retained"**, not merely "read the block". My §5.1
census uses that rule; O03/O04 should state which rule their `2508`/`2611` uses.

**Glob-fragment treatment changes the unresolved count by one.**
`gate-frozen-run-standard.md:15` contributes `-gate.md`, which policy §5.6 forbids
counting as a finding. Under §5.6-conformant extraction (drop tokens containing
`*`, and their partial fragments) the N6-fixed census is `2507 = 2337 + 163 + 0 +
7` at r39 and `2610 = 2437 + 166 + 0 + 7` live, 6 distinct. So the "corrected
unresolved" number is **8 (raw) or 7 (§5.6-conformant)** — a successor note must
say which, since §5.6 already rules the token out of the finding population.

## 4. The claim's wording is wrong about direction and about the phantoms (O12-C3)

`reports/round-42/claims.json:14` says the policy's `2504 = 2335 + 163 + 0 + 6`
"becomes the corrected baseline with the 2 phantom attributions dispositioned",
and the `after_required` says "the corrected census reproduces the r39 policy's
arithmetic minus the phantoms". **Two corrections:**

1. **Direction.** The corrected census does not *minus* anything: refs go 2504 →
   2508 and unresolved go 6 → 8. Nothing was removed; the fix *adds* 4 refs (2
   resolving, 2 not). A successor note must not present a subtraction.
2. **The `2 phantom attributions` are the X26-1 path's two carriers, and the
   draft named only one.** The draft says `../linguistics/phonology-sanity.md` is
   "still live in `corpus/knowledge/verification/label-channel-routing-verification.md:14`"
   (`Ca03-basename-policy.md:272-275`). Live scan finds **two** carriers:
   - `corpus/knowledge/verification/label-channel-routing-verification.md:14`
   - `corpus/knowledge/synthesis/typed-label-routing-workflow.md:16` — `linguistics
     — \`../linguistics/language-contact.md\`, \`../linguistics/phonology-sanity.md\``

   That is exactly the `x2` in the census, so the count is right and the
   attribution was single-carrier. `reports/round-42/calib/Ca01-gap-fill.md:267-274`
   independently names the same second carrier and routes it to this seat; I
   confirm it live and fold it here. The phantom is a *never-written* path: no
   `phonology-sanity.md` exists anywhere under `corpus/knowledge/` (only
   `phonology-sanity-gate.md` in `verification/`).

The **two genuinely new** unresolved tokens are the wrapped field's
never-written seeds `sound-change.md` and `tone-prosody.md`; neither exists
anywhere in the repo (`find . -name 'sound-change.md' -o -name 'tone-prosody.md'`
→ empty). The field's other two named targets `sound-symbolism.md` and
`writing-systems.md` exist and classify `direct`.

Full N6-fixed live unresolved population (7 distinct): `../linguistics/phonology-sanity.md`
×2 (X26-1, 2 carriers), `-gate.md` ×1 (§5.6 glob fragment),
`honorifics-and-register.md`, `naming-and-onomastics.md`, `phonology-basics.md`
×1 each (`language-contact.md:7` never-written seeds), `sound-change.md`,
`tone-prosody.md` ×1 each (N6). **Zero of the seven has a repair disposition on
record** — each is a live `couples:` target that does not exist.

## 5. Tree-growth delta is cleanly separable (O12-C4)

The r39→live growth is fully accounted for by the 8 entries `dfb0719..ac47c78`
added to `corpus/knowledge/` (`git diff --name-status`: 4 linguistics, 4
verification):

- **refs 2504 → 2607 = +103**, and the 8 new entries contribute exactly **103**
  per-entry-deduplicated couples refs (10+12+10+11+16+12+12+20). No pre-existing
  entry's refs moved.
- **fallback 163 → 166 = +3**, all from one new entry:
  `corpus/knowledge/linguistics/sacred-registers-liturgical-language.md` (3).
  The other 20 fallback-contributing entries are byte-identical between trees.
  This answers Ca01's `to-verify (a)` (the fallback delta's per-entry split).
- **unresolved 6 → 6** (single-line) and **8 → 8** (N6-fixed): the new entries
  introduce no dangling token. The single-line unresolved set is *identical*
  across trees, including the `×2` phantom.
- **direct 2335 → 2435 = +100**, consistent with +103 refs of which +3 fallback.

Basename uniqueness holds at both trees: 220 entries / 220 distinct basenames /
**0 collisions**, so the Tier-2 uniqueness assumption is intact (policy §5.5).

## 6. What the successor note should say (drafted for the integrator; not applied)

1. The arithmetic is **`2508 = 2337 + 163 + 0 + 8`** at `dfb0719` and
   **`2611 = 2437 + 166 + 0 + 8`** at `ac47c78`, with the extractor, join rule and
   glob-fragment treatment each named (block, hyphen-retained, §5.6 raw).
2. The direction is **additive**: the fix exposes 4 refs the single-line extractor
   dropped; it does not subtract phantoms.
3. The `2 phantom attributions` = the X26-1 path at **two** carriers, both named.
4. The filed policy is a **truncated prefix**; the note should either state that
   §6/§7 are absent from the durable object or that the draft
   `Ca03-basename-policy.md` is the arithmetic's home.
5. Seven unresolved tokens remain undispositioned; the N6 fix adds two.

## Owed

- **Integrator (corpus owner):** the policy document is a truncated prefix
  (O12-F1). Repairing it means editing filed r39 bytes, which is outside every
  seat's write scope — record the truncation as a defect row with an owner and a
  repair route (successor-instrument round r43/r44, per queue-v2
  `r39-basename-successor-instrument`). Do not land the successor *note* at the
  policy's own path; the mission says the policy stays filed.
- **Integrator:** fold O12-F1 into the r39 gate-coverage record —
  `run-validation.py:117-121` verified a marker, not the document.
- **O01/O03/O04 (N6 fix block):** the fix must specify **hyphen-retained block
  extraction**. A `\n`- or space-joining block parser reproduces the count
  `2508`/`2611` while mis-reading `tone-prosody.md` as `prosody.md`; a
  hyphen-stripping join mints `toneprosody.md`. Both false readings are silent —
  they produce the same totals. O03's predicted census and O04's isolated
  verification should state the join rule and assert the token **set**, not only
  the totals.
- **Integrator (disposition leg):** seven unresolved tokens, zero dispositions.
  X26-1's second carrier is confirmed at
  `corpus/knowledge/synthesis/typed-label-routing-workflow.md:16` (Ca01's
  handoff). `honorifics-and-register.md`, `naming-and-onomastics.md`,
  `phonology-basics.md` are `language-contact.md:7` seeds; `sound-change.md` and
  `tone-prosody.md` are N6-exposed seeds. Repair (author the files or reword the
  fields) needs a corpus-owning round — seats never stage under `corpus/`.
- **to-verify:** whether the successor instrument should treat `AGENTS.md`,
  `SKILL.md`, `SCORECARD.md`, `corpus/README.md` (lane-root files, all present)
  as Tier-1 resolvable when the census runs from a corpus-subtree root; the
  lane-root base is what makes them `direct` in-tree.
- **to-verify:** no `ambiguous` instance exists in either tree, so the class is
  untested live — O05's synthetic fixture is the only coverage.

## Citations

- Assignment: `reports/round-42/targets.json` seat `O12` (role verifier, claim O,
  out `op/O12-policy-check.md`); claim O `after_required`
  ("the corrected census reproduces the r39 policy's arithmetic minus the
  phantoms") and `before` at `reports/round-42/claims.json:14-16`.
- Verified object, filed: `reports/round-39/calib/basename-couples-policy.md`
  (107 lines, 5832 bytes, sha256 `105dfff6c667ad5b77c28be8d6070ec243b5e19029fb60ae83d6028aa2e941cf`);
  §1 `:14-25`, §2 `:27-48`, §3 `:50-58`, §4 `:60-69`, §5 `:71-102`, §5.6
  `:97-102`, §6 opening `:104-107`.
- The draft it is a prefix of: `reports/round-39/calib/Ca03-basename-policy.md`
  (359 lines, sha256 `125ede77e3f50e3c58af61fb2fad246c8378b4dcfc4ee5d1749da8dd53a17850`);
  arithmetic `:35-38`; §6 recipe `:149-258`; filed-run block `:260-290`; §7
  `:292-303`; Owed `:306-324`; Citations `:326-359`.
- Arithmetic as verified: `reports/round-39/calib/Ca04-verify.md:20-30` (§6
  re-run), `:29` (Part 2 line).
- Gate that passed the truncated file: `reports/round-39/run-validation.py:116-131`
  (marker `fallback` `:118`; marker `334` `:130`).
- N6 defect row: `reports/round-40/op/defect-queue-v2.json` rows
  `N6-couples-extractor-wrapped-field` and `r39-basename-successor-instrument`
  (owner "successor-instrument author … r43/r44").
- N6 provenance: `reports/round-39/calib/Ca04-verify.md:78-105` (D1, live
  instance `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`).
- Extractor code: `reports/round-19/audit/entry-audit.py:31,34-42,74-96` (single-line
  capture `:75`); `reports/round-35/cov/C14-audit-6-10.md:207-236` (block parser),
  `:249-288` (basename index `:252-260`, classes `:271-288`, slash-bearing key
  `:281`), `:112-119` (201-entry reading, 8 unresolved / 7 distinct).
- Wrapped field: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
  (6 physical lines; raw bytes quoted in §3's join table).
- X26-1 phantom carriers: `corpus/knowledge/verification/label-channel-routing-verification.md:14`;
  `corpus/knowledge/synthesis/typed-label-routing-workflow.md:16`; provenance
  `reports/round-35/cov/C14-audit-6-10.md:114-119`; second-carrier handoff
  `reports/round-42/calib/Ca01-gap-fill.md:267-274`.
- Language-contact seeds: `corpus/knowledge/linguistics/language-contact.md:7`.
- Glob fragment: `corpus/knowledge/verification/gate-frozen-run-standard.md:15`.
- Sacred-kingship fallback field: `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md:37`.
- Independent agreement (same wave, separate seats, separate instruments):
  `reports/round-42/op/O03-predicted.md:142-146,151-157,216-217` (both trees,
  both modes, identical to my table); `reports/round-42/op/O04-verify.md:125-132`
  (same six-row table); `reports/round-42/calib/Ca01-gap-fill.md:265-274`
  (`2607 = 2435 + 166 + 0 + 6` single-line, `2611 = 2437 + 166 + 0 + 8` block,
  plus the second-carrier handoff). Four seats, one reading.
- Command outputs (this seat, 2026-10-19, lane root, `export TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`, all read-only, HEAD `ac47c7861b0b2cdb8e3c2f985c2220406d3ba0b4`):
  - truncation: `diff <(sed -n '41,147p' reports/round-39/calib/Ca03-basename-policy.md)
    reports/round-39/calib/basename-couples-policy.md` → identical;
    `grep -c '2504\|2335\|163' reports/round-39/calib/basename-couples-policy.md` → `0`.
  - r39 tree: `git archive dfb0719 | tar -x -C .scratch/r39full` → 212 entries.
  - §6 recipe: `sed -n '150,257p' Ca03-basename-policy.md > .scratch/o12-policy-s6.py;
    python3 -B .scratch/o12-policy-s6.py` → Part 1 `refs=334 -> direct=319 fallback=15
    ambiguous=0 unresolved=0`, `RESULT: PASS`; Part 1b 15/15 OK `misaligned=0`;
    Part 2 `entries=220 refs=2607 -> direct=2435 fallback=166 ambiguous=0 unresolved=6`
    (live tree) — the r39-tree variant of the same script is the `dfb0719`
    single-line row of §3.
  - census/join/wrapped scripts: `.scratch/o12-census.py`, `.scratch/o12-final.py`,
    `.scratch/o12-wrapped.py`, `.scratch/o12-dehyphen.py` (scratch is disposable;
    the commands are the durable evidence; outputs also in `.scratch/o12-*-out.txt`).
  - basename uniqueness: 220 entries / 220 distinct basenames / 0 collisions.
  - no `run-validation.py` was executed anywhere; no filed byte edited; no git,
    network or install action.
