- Seat: P01 | planner | cross | date 2026-10-19 | baseline ac47c78

# Round-42 plans — both claims (O and C)

Planner's note: the two scouts (K01 N6-host, K02 myth-gaps) run concurrently and
their fragments were **not landed at plan time** (measured: `reports/round-42/`
contained only `claims.json`, `targets.json`, `telemetry/dispatch-declared.json`
— `find reports/round-42 -maxdepth 2`). Every plan below consumes them by
CONTRACT (their `out` paths + target missions), with a stated fallback. Nothing
below asserts scout fragment contents. Everything marked **MEASURED** was
re-measured by this seat at `ac47c78` with read-only commands; the command and
its output are quoted so a verifier can reproduce it.

Scope: claim **O** (operability, the N6 wrapped-couples-field fix + corrected
census) and claim **C** (coverage, myth-symbol 23 → 27). Freshness stays paused;
no canon, promotion, clearance, closure, filed-byte rewrite, packet-surface
change, or `declared-in-r7` re-freeze is in scope (`reports/round-42/claims.json:26-27`;
`REGIMEN.md:27-43`). P01 plans both claims and implements neither
(`reports/round-42/targets.json` → `seats[id=P01]`).

---

## 0. Anchors measured at plan time (baseline `ac47c78`, tree clean but `?? reports/round-42/`)

**MEASURED** — the N6 defect is live and its mechanism is confirmed end to end:

1. The filed extractor is single-physical-line. `reports/round-19/audit/entry-audit.py:75`
   is `m = re.search(r"^- couples:\s*(.*)$", text, re.M)` — `$` without `re.M`
   multiline-block semantics and `.` never crossing a newline, so the match ends
   at the first line break. Token regex `MDREF_RE` at `:31`; brace expansion at
   `:34-42`; the three-base direct rule at `:87-95`.
2. The one wrapped field. `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
   is `- couples:` followed by **5** continuation lines (all indented two spaces,
   the 6th line is blank then `## 1. Two levels`). Its full field names four `.md`
   targets: `sound-change.md`, `tone-prosody.md`, `sound-symbolism.md`,
   `writing-systems.md`.
3. Live consequence. `python3 -B reports/round-19/audit/entry-audit.py corpus/knowledge/linguistics/phonetics-phonology.md`
   → `FAIL … src=15/15 couples=0 unresolved=[] gap=False dec=True` / `TOTAL 0/1 clear the bar`, **exit 2**. The instrument silently reports **0 couples tokens** where the field names 4.
4. Corpus-wide wrapped-field census (all 220 entries, header-field scan): **exactly 1** wrapped `couples:` field, the one above. No other entry has a continuation line after `- couples:`.
5. Corrected vs filed census, same tree, both runs by this seat:

   | parser | entries | refs | direct | fallback | ambiguous | unresolved |
   |---|---|---|---|---|---|---|
   | single-line (r19/r39-policy rule) | 220 | 2607 | 2435 | 166 | 0 | 6 |
   | block parser (C14 `fields_of`) | 220 | 2611 | 2437 | 166 | 0 | **8** |

   The block parser adds exactly the 4 wrapped tokens: `sound-symbolism.md` and
   `writing-systems.md` resolve **direct**, `sound-change.md` and `prosody.md` are
   **unresolved**. `prosody.md` is the line-break mangling of `tone-prosody.md`
   (`tone-` ends line 76, `prosody.md` opens line 77) — a hazard no current
   instrument handles (`reports/round-39/calib/Ca04-verify.md:88-92`).
6. **The r39 policy's 2504 baseline is reproduced exactly** from filed bytes at
   `dfb0719` (`git show dfb0719:<path>` over the 212 entries): single-line →
   `2504 = 2335 + 163 + 0 + 6`; block → `2508 = 2337 + 163 + 0 + 8`. So the
   "corrected baseline" is **2508/2337/163/0/8** at the r39 tree, and the two
   added unresolved names are precisely the two phantoms. `sound-symbolism.md`
   and `writing-systems.md` exist in `corpus/knowledge/linguistics/` at **both**
   `dfb0719` and `ac47c78` — `git ls-tree -r dfb0719 --name-only
   corpus/knowledge/linguistics/` lists both and `git cat-file -e` on each
   returns exit 0, so both are Tier-1 **direct** at both trees; `sound-change.md`
   and `tone-prosody.md` exist nowhere in the repo at either revision (the
   second is not even spelled in the field — the extractor sees `prosody.md`).
   **Contested, resolved by measurement:** O03 §4 (`op/O03-predicted.md:78-108`)
   and O04 §2 assert these two live tokens are `fallback`, "because
   `corpus/knowledge/linguistics/` held only 21 entries at r39 close". That
   reasoning is falsified: the directory held 21 entries, but `sound-symbolism.md`
   and `writing-systems.md` were **among** those 21. O03's own §6 table and
   K01's §table (`scout/K01-n6-scout.md:92-93`, `:166-173`) both give
   `2337/163` — the same numbers I measure — so only O03's/O04's explanatory
   prose is wrong, not their arithmetic. The integrator should have O03/O04
   correct that sentence, or file it as a named disagreement.
7. The hyphen-join question (resolves an ambiguity O03/O05 must decide
   deliberately). Joining continuation lines with `" "` or `"\n"` both yield
   `['prosody.md', 'sound-change.md', 'sound-symbolism.md', 'writing-systems.md']`
   (the phantom `prosody.md` survives). A **soft-wrap join** — concatenate the
   next line with **no separator**, keeping any trailing hyphen — yields
   `['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md',
   'writing-systems.md']`, i.e. **4/4 named, 2 direct + 2 unresolved**. Note the
   exact rule: **keep** the hyphen and concatenate (`tone-` + `prosody.md` →
   `tone-prosody.md`). Stripping the hyphen before concatenating over-merges to
   `toneprosody.md` (O03 §5 measured all three variants,
   `op/O03-predicted.md:110-125`). The claim's threshold is "the wrapped field
   reads **4/4 targets**"; a naive whitespace join reaches the same *count* of 4
   but the **wrong 4th token**, so the fix must specify the join rule or the
   phantom survives. See §1.2 step 2 and Hazard H2.
8. Coverage anchors. `ls corpus/knowledge/myth-symbol/*.md | wc -l` → **23**;
   corpus total **220**; partitions `civilizations 94 / culture-material 25 /
   linguistics 25 / myth-symbol 23 / synthesis 29 / verification 24`.
   `corpus/README.md:5` is `revision: 2.3`; `:196` is `## myth-symbol/ (23)`;
   `:532` is `Total knowledge entries: 220.`; `:536` footer
   `(total 220 files; directory totals 25/23/25/29/24/94)`.
   `python3 -B reports/round-28/readme/sweep.py` → `rows 220 files 220`,
   `footer_ok True`, **exit 0**.
9. Instrument/contract anchors. Entry structural contract =
   `reports/round-35/cov/C12-audit-runbook.md:28-44` (the six check families);
   the runbook instrument is installed from its own §5 (`:182-184`, sha256
   `973610275404e9e3183d46e33e5352562265e6c2e397c92291e63c401ed7562d`, 663
   lines). Precedent audits: `reports/round-39/cov/C05-audit.md:44-49`,
   `reports/round-40/cov/C05-audit.md:24-31` (`4/4 PASS` verdict wording is the
   needle the runner greps).
10. **MEASURED — a filing defect in the round-39 policy.** The **filed**
    `reports/round-39/calib/basename-couples-policy.md` is **107 lines** and its
    `## 6. Verification recipe` (opening `:104`) ends at `:107` with the prose
    lead-in and **no fenced script** — the recipe body was not landed. The draft
    the verifier actually checked, `reports/round-39/calib/Ca03-basename-policy.md`,
    is **359 lines** with `## 6` at `:144`, `## 7. Adoption evidence` at `:292`,
    and the script present. `Ca04-verify.md:10-12,25-36` verifies against the
    **draft's** §6/§7. So the filed artifact is a truncated sibling of the
    verified draft. This is a **new planner finding** (name it `P01-1`), it does
    not touch the N6 substance (the `fallback` marker the r39 runner greps is at
    `:36`), and it is routed in §1.7 — it is not repaired here (filed bytes).

**Reading of the anchors.** Claim O is a real, exactly-located, reproducible
defect with a known cure shape (the C14 block parser) and two prior filed
carriers of the fix intent (the r39 policy's own §1 rule and the queue row's
`next_touch`). Claim C is a clean partition expansion on the thinnest partition
with a well-worn entry contract and a green sweep. Both are landable; neither
requires an invented source.

---

## 1. Plan — claim O (operability): the N6 block-parser fix + corrected census

Claim contract (`reports/round-42/claims.json:13-18`): the couples-reference
extractor gains a block parser so the one wrapped field is read whole (4 named
targets, not 0); the corpus-wide recount re-derives the reference census (the
r39 policy's `2504 = 2335 + 163 + 0 + 6` becomes the corrected baseline with the
2 phantom attributions dispositioned); selftest controls incl. the wrapped-field
positive + a synthetic phantom negative. After: the fixed extractor durable on
the live corpus, the corrected census filed, selftest green, zero phantom
attributions remaining or each dispositioned.

### 1.1 Host identification — the wave's first job, and the sharpest open question

The claim itself says the host is *"likely the r39 C12 runbook's resolver or a
tools/harness couples checker; the wave confirms the host"*
(`reports/round-42/claims.json:16`). **My plan-time read of the tree says
neither of those two hosts exists in the lane root**, so K01/O01 must resolve
this before writing a patch:

- `grep -rn couples tools/ --include=*.py` hits only `tools/gates/provenance-audit.py`
  and `tools/source-audit-inventory.py`, and both are **different checks**:
  `provenance-audit.py:75-76,315-320` tests couples *presence/emptiness*
  (`missing-couples` / `empty-couples`), never resolves tokens; the
  source-audit hits are fixture strings.
- The r39 C12 runbook is a **markdown runbook**, not a shipped resolver; its
  instrument is installed at audit time from `C12-audit-runbook.md` §5
  (`:182-184`), i.e. it is an auditor-side tool, not a durable lane instrument.
- The only **filed** resolver code with the single-line defect is
  `reports/round-19/audit/entry-audit.py:75` (and its r27 successor
  `reports/round-27/audit/entry-audit.py`), plus the C14 fragment's inline
  recipe (`reports/round-35/cov/C14-audit-6-10.md:263-288`).
- **K01 landed while this plan was being written and agrees** (`reports/round-42/scout/K01-n6-scout.md:21-45`):
  the host is `reports/round-19/audit/entry-audit.py:74-96`, C12's runbook is
  "that guess is wrong", and K01 adds two scout findings — the defect is also
  carried by the **r27 and r28 successor copies** (`reports/round-27/audit/entry-audit.py`,
  `reports/round-28/audit/entry-audit.py:251,264-268`), so a fix landing in r19
  alone leaves its successors carrying the same defect; and the filed r19
  selftest (`:151-182`) is green today because its fixture is single-line only.
  So O01 must state **which copies** it patches, and O02's controls are genuinely
  new coverage, not a re-run.
- The **landed policy** is prose that names the successor instrument as owed
  (`reports/round-39/calib/basename-couples-policy.md:7-9`: "successor audit
  instruments implement this policy").

So the honest host decision has three branches, and the wave must **record which
one it took**:

- **Host A (recommended): a new durable lane instrument** —
  `tools/harness/couples-resolver.py` (path chosen to sit beside the existing
  `tools/harness/` instruments, none of which touch couples). It implements the
  landed policy (four classes, two tiers) **plus** the D1 block parser and the
  D2 disposition leg, and it is the successor instrument the policy names as
  owed. Rationale: it is durable, it is not a filed round byte, it is the
  artifact the queue row's `next_touch` ("author the successor instrument … and
  re-run corpus-wide") asks for, and it satisfies the claim's "the fixed
  extractor durable". Cost: a new tool, so it needs a selftest and a
  registered-or-explicitly-out-of-battery note.
- **Host B: fix in place** `reports/round-19/audit/entry-audit.py` — **REJECTED
  by plan**: it is a filed round-19 byte and the hard boundary forbids editing
  `reports/round-1..41/**`. Also the policy already declares the r19 instrument
  stays "as filed" (`basename-couples-policy.md:7-8`).
- **Host C: the C14 recipe only** — **REJECTED**: a fragment's inline script is
  not a durable instrument and does not close N6's "durable" leg.

O01 must therefore **not** present the patch as "a diff against a confirmed
host" if the host is new; it should present the **full new file** (fenced) with
the block parser as the delta and the policy semantics as the carried contract,
and it must state which branch it took and why. If K01 instead finds a durable
lane-root couples resolver I did not find, O01 patches that and names it; the
two branches are exclusive and the choice must be recorded.

### 1.2 The patch spec (what the block parser must do)

1. **Block extraction.** Replace the single-line capture with a block read: from
   the `- couples:` line, consume following lines while they are non-blank and
   are not themselves a header field (`^- [A-Za-z0-9_-]+:`). **Do not reuse
   C14's `fields_of` as-is** — O03 measured that it has no blank-line terminator
   (`reports/round-35/cov/C14-audit-6-10.md:234`) and so falsely reports a second
   wrapped field, `corpus/knowledge/linguistics/conlang-methodology.md`
   (`op/O03-predicted.md:60-67`); **MEASURED** here: `conlang-methodology.md:7`
   is a single physical line, `:8` is blank, `:9` is unindented body prose, `:11`
   is `## Pipeline at a glance`. The continuation rule must be **"following line
   is indented"** (or blank-terminated), which O04 independently found agrees on
   **1** wrapped field (`op/O04-verify.md:26-45`). Record which entries used the
   block path (expect exactly one) so the census can name it.
2. **Join rule.** Join continuation lines with **no separator** (soft-wrap
   concatenation), **keeping** any trailing hyphen: `tone-` + `prosody.md` →
   `tone-prosody.md`. **MEASURED** (§0.7): this is the only join that yields the
   intended token; a plain whitespace/newline join yields the phantom
   `prosody.md` and would pass a naive 4-token count while leaving the defect in
   place, and stripping the hyphen over-merges to `toneprosody.md` (O03 §5
   measured all three, `op/O03-predicted.md:110-125`). The rule must be stated
   and controlled (Hazard H2).
3. **Preserve the policy semantics unchanged.** Token regex, one-level brace
   expansion, per-entry dedup, the three-base direct tier, the slash-free-only
   unique-basename fallback, the four classes, and the group-alignment leg
   (`reports/round-39/calib/basename-couples-policy.md:14-69`). The fix changes
   **extraction only**; it must not silently relax or widen resolution.
4. **Adopt the D2 disposition leg** (Ca04's other one-sentence fix,
   `reports/round-39/calib/Ca04-verify.md:94-101`): an `unresolved` couples token
   is a **blocker** unless the same line marks it `(to-verify`, in which case it
   is reported as documented and is not a blocker — the C12-row-2 treatment
   (`reports/round-35/cov/C12-audit-runbook.md:37`). This makes the new
   instrument's verdict on `phonetics-phonology.md` interpretable (its 2
   unresolved tokens carry no `(to-verify`, so they are blockers).
5. **Glob fragments** (§5.6 of the policy, `basename-couples-policy.md:97-102`):
   the successor instrument should **skip or separately class** glob fragments
   (`corpus/knowledge/verification/gate-frozen-run-standard.md:15` yields
   `-gate.md`) rather than count them unresolved. **MEASURED**: `-gate.md` is one
   of the 8 block-mode unresolved tokens. Whether the fix implements this is a
   scope call for O01 — if it does, the census must report the fragment class
   separately, not fold it into `unresolved`; if it does not, say so and keep it
   in `unresolved` with a named disposition. Either way it must be stated, and
   the count must match the stated rule.

### 1.3 Controls (O02, fenced; the claim requires these)

- **Wrapped-field positive.** A fixture whose `couples:` field wraps across ≥3
  lines, including a hyphen-split token, asserting **4/4** named targets and the
  exact token set `{sound-change.md, tone-prosody.md, sound-symbolism.md,
  writing-systems.md}` — **not merely a count of 4** (H2).
- **Synthetic phantom negative.** A fixture whose wrapped field names a token
  that does not exist anywhere, asserting it lands in `unresolved` (and is a
  blocker absent `(to-verify`).
- **Unwrapped regression.** The 219 single-line entries' census is **unchanged**
  by the fix (MEASURED basis: single-line 2607/2435/166/0/6 at the round-42 tree;
  the fix must reproduce those numbers for every entry except
  `phonetics-phonology.md`).
- **De-hyphenation control.** A fixture with `tone-\nprosody.md` asserting the
  token is `tone-prosody.md` and that `prosody.md` never appears (the trap the
  naive join fails), plus the over-merge control (`toneprosody.md` must not
  appear either).
- **No-relaxation control.** A slash-bearing token that would fallback-resolve
  under C14-as-written (`linguistics/hero-journey-variants.md`) stays
  `unresolved` under the new instrument (the policy's §5.1 declared narrowing,
  `basename-couples-policy.md:73-81`).
- **Selftest must be self-contained** (fixtures inline or in a scratch dir) so it
  runs in an isolated copy; no filed byte is read for writing.

### 1.4 The corrected census (O03 predicts, O04/O05 verify)

O03's deliverable is a **read-only recount with the fixed logic**, which the
landed tool must reproduce. Two things must be pinned:

- **The tree.** **MEASURED** at `ac47c78`: block-mode = `2611 refs / 2437 direct
  / 166 fallback / 0 ambiguous / 8 unresolved` over 220 entries; single-line =
  `2607 / 2435 / 166 / 0 / 6`. At the r39 tree (`dfb0719`, 212 entries):
  block = `2508 / 2337 / 163 / 0 / 8`, single-line = `2504 / 2335 / 163 / 0 / 6`
  — the policy's filed baseline. **Both** should be in O03: the r39-tree pair
  (because the claim says the policy's 2504 "becomes the corrected baseline")
  and the round-42-tree pair (because the landed tool runs there).
- **The C/O interaction.** Claim C lands **4 new myth-symbol entries in the same
  round**, each with a `- couples:` line, so the round-42-**close** census is
  *not* 2611 — it is 2611 plus the new entries' refs. O03 must therefore either
  (a) state the census at a **named pre-C state** (the `ac47c78` figures above)
  and separately predict the delta the 4 new entries add once C06's drafts are
  readable, or (b) re-run at close and let the delta be measured. Do not file a
  close-tree number as if it were the pre-C number (Hazard H3).

### 1.5 Phantom disposition (the claim's "2 phantom attributions dispositioned")

The two phantoms are `sound-change.md` and `tone-prosody.md`, both in
`phonetics-phonology.md:72-77`, both **named in the field as "prospective
sibling files"** — i.e. the entry itself declares them as not-yet-built. The
disposition is therefore *documented-absence, not defect*, and it must be stated
in the census note: the field's own words ("prospective sibling files") mark them
intentional; the successor instrument reports them `unresolved`; they are **not**
a blocker because the field says prospective. If O01 prefers the strict D2
reading (unresolved = blocker unless `(to-verify`), then the honest output is
"2 blockers on one entry, dispositioned as prospective-sibling declarations" —
either is admissible **if stated**. Note the mangled token `prosody.md` is
**not** a legitimate phantom: it is an extractor artifact, and after the
soft-wrap join fix it must disappear entirely (that is the fix's cleanest
positive).

### 1.6 Verification (O04, O05, O12, O08)

- **O04** (isolated): `git archive` a copy of the tree into `.scratch`, apply the
  patch, run `--selftest` and the recount, compare row-for-row to O03. The copy
  must not be under `reports/round-42/` write paths that collide, and it must not
  be a filed round dir.
- **O05** (second isolated + adversarial): hand-craft a wrapped field with a
  **planted phantom** and a hyphen-split real token; assert the instrument
  catches the phantom and joins the split token into `tone-prosody.md`. Also test
  a field wrapped *twice* and a field with a blank line mid-continuation (must
  terminate).
- **O12** (policy arithmetic): the r39 policy doc stays filed; the correction is
  a **successor note**. O12 confirms the policy's §2 arithmetic still holds under
  the corrected census — i.e. `direct + fallback + ambiguous + unresolved` totals
  the ref count, and the r39 figures are reproducible (MEASURED: they are), and
  files the successor note as a new artifact.
- **O08** (queue row): re-class `N6-couples-extractor-wrapped-field` to
  `fixed-with-evidence` **only if** the landed instrument + selftest + census
  actually demonstrate it, mirroring how N7 was closed (`reports/round-40/op/defect-queue-v2.json`
  N7 row). Also update `r39-basename-successor-instrument` (D1 leg) and note that
  D2 is closed by the same landing. Do not claim the r19 filed instrument is
  repaired — it is not, by design.
- **ABSOLUTE**: no seat executes any `reports/round-*/run-validation.py`, in-tree
  or otherwise. The round-42 acceptance is the integrator's isolated-copy run
  (the r39 isolation-replay protocol precedent, `reports/round-39/calib/isolation-replay-protocol.md`).

### 1.7 Owed by O (plan-level, named so nothing is dropped)

- **P01-1 (new finding, routed):** the filed `basename-couples-policy.md` §6 is a
  107-line stub whose recipe body never landed, while Ca04 verified the 359-line
  draft (§0.10). Filed bytes are never rewritten, so this is routed as a
  **successor note** (O12's natural home) recording the truncation and pointing
  at `Ca03-basename-policy.md:144-290` for the recipe bytes. Do not silently
  re-land the policy.
- The `prosody.md`/`tone-prosody.md` split is a **general** extractor hazard, not
  just this one field; the fix's join rule must be tested as such (O05).
- Whether the new instrument enters the gate battery is a scope decision; if it
  does not, say so explicitly rather than leaving it ambiguous.

---

## 2. Plan — claim C (coverage): myth-symbol 23 → 27 + README rev 2.4

Claim contract (`reports/round-42/claims.json:19-24`): +4 sourced myth-symbol
entries (23 → 27; total 220 → 224) on gap-named topics per the wave's scout, each
with the established entry contract; README rev 2.4 (224 total); audits
pre-landing. After: myth-symbol 27, total 224; README rev 2.4 sweep-green
224 == 224; audits 4/4 PASS. Counting commands:
`ls corpus/knowledge/myth-symbol/*.md | wc -l` and
`python3 -B reports/round-28/readme/sweep.py`.

### 2.1 Topic slot map (K02 owns the final choice; this is the planner's ranked set)

The partition's own gap statements show the method: each new entry names, in a
`- gap:` / `- gap filled:` field, **what the partition carries as by-product and
what it leaves unbuilt**, with a bounded absence sweep
(`plant-symbolism.md:3`; `eschatology-world-end-systems.md:4`;
`sacred-kingship-mythic-charter.md:4`). Four ranked candidates, each with a
one-line gap thesis and a seed source (the entry contract requires real, citable
sources — `corpus/QUALITY.md:6-8`):

1. **`stone-symbolism.md` — the lithic/gem register.** *Strongest candidate.*
   The register family is closed at color/animal/number/celestial/direction
   (`symbolism-synthesis-method.md:1`) plus flora (`plant-symbolism.md:3`), and
   the method file explicitly names the **lapidary** as part of "the medieval
   Latin package" that the lane imitates (`symbolism-synthesis-method.md:29`) —
   yet **no entry owns stone**. **MEASURED**: lapidary content is scattered and
   never owned — `culture-material/ritual-garments.md:59` (choshen, 12 gems),
   `culture-material/sumptuary-law-rank-display.md`,
   `culture-material/vessel-container-lexicon.md`,
   `culture-material/funerary-material-culture.md`, `civilizations/china-song.md`,
   `civilizations/maori.md`, `civilizations/siam-thai.md:126` (Emerald Buddha as
   dynastic palladium); and `civilizations/rome.md:33` is a false positive
   (epigraphic "lapidary capitals"). Seed sources: Pliny *Naturalis Historia*
   37 (the lapidary spine), the medieval lapidaries, jade/turquoise/obsidian
   prestige systems, Moorey/Melikian on Near Eastern stone. Mirrors
   `plant-symbolism`'s own gap statement exactly.
2. **`purity-pollution-codes.md` — purity, pollution and the category-break
   machinery.** The lane already *uses* Douglas but never *owns* the system:
   **MEASURED** `symbolism-synthesis-method.md:19,68` cite Douglas (1966) and
   "the anomaly picks your taboo … carries the pollution load", and
   `plant-symbolism.md:20` extends it ("do not re-derive the machinery") — while
   no entry builds the purity-code system itself (no `myth-symbol` file owns
   purity/pollution; the hits are `linguistics/politeness-taboo-euphemism.md`,
   `culture-material/bathing-and-body-hygiene.md`, `cuisine-food-lexicon.md`,
   `funerary-material-culture.md`). This is exactly the "machinery everyone
   couples to and nobody owns" shape the partition's other gap entries fill.
3. **`marriage-alliance-symbolism.md` — marriage as an alliance system.** The
   *terms* are owned (`linguistics/kinship-terminology.md`) and kingship touches
   alliance (`sacred-kingship-mythic-charter.md` "marriage-alliance into the
   divine line") but no entry owns marriage as a myth-symbolic/alliance
   institution (exogamy rules, bride-price as symbol, affinal taboos, wedding
   rite grammar, lineage charters).
4. **`sacred-topography-place-symbolism.md` — the place register.** The partition
   has direction and celestial *codes* and groves-as-objects
   (`plant-symbolism.md`) but no entry owns **place** as a register — the
   holy-site typology, pilgrimage institutions, boundary/pillar marks, the
   place-name-as-charter. **MEASURED**: `pilgrimage` appears in 10 files, none
   `myth-symbol` owning place.

**MEASURED guard:** the four `*`-symbolism filenames already taken are
`animal-symbolism.md`, `color-symbolism.md`, `direction-symbolism.md`,
`number-symbolism.md`, `plant-symbolism.md`, plus `celestial-symbolism-calendars.md`.
None of the four proposed slugs collides.

**Fallback if K02 is late:** C01–C04 may start from this ranked set under the
round-39 self-derive rule (r39's own plan permitted entries to start before the
scout landed, `reports/round-39/plan/P01-plan.md:263`); C04 must redo K02's
collision check locally. If K02 names a different fourth topic, its landing
supersedes the slug choice only if the topic is genuinely unbuilt — verify with
an absence sweep, not by assertion.

### 2.2 Entry contract (each of C01–C04)

Per `reports/round-35/cov/C12-audit-runbook.md:28-44` and the r39/r40 audits
(`reports/round-39/cov/C05-audit.md:44-49`; `reports/round-40/cov/C05-audit.md:24-31`):

- Head block: `# Title`, then `- gap:` / `- gap filled:`, `- topic:` (matching
  the README index row **byte-for-byte**), `- sources:` (block or inline), plus
  `- source:` / `- verified-at:` (ISO `YYYY-MM-DD`) / `- recheck:` / `- couples:`
  / `- scope:`. **MEASURED**: the r39/r40 entries carry a literal `- scope:`
  field (e.g. `corpus/knowledge/verification/worked-example-verification.md`),
  while older entries satisfy the scope leg with `- couples:`; new drafts should
  carry **both** `- scope:` and `- couples:` to be safe (family 1a accepts either).
- Body: decision tables / typology tables / build protocol / **decision record**
  (`## N. Decision record`, heading + body, ids recommended —
  `reports/round-40/cov/C05-audit.md` F4) / **calibration** of contested and
  discredited readings (`corpus/QUALITY.md:9-11`).
- **Every backticked repo-path pointer must resolve on disk**, brace groups
  expanded one level, or be marked `(to-verify` on the same line (family 2,
  blocker) — `reports/round-35/cov/C12-audit-runbook.md:37`.
- **Couples field must be single-line** — no wrapped field (Hazard H1).
- No canon: entries end at the handoff; `lore-shokunin` owns canon
  (`corpus/QUALITY.md:15-16`; `PROVINCE.md`).
- **Fenced drafts only.** C01–C04 write `.md` fragments under
  `reports/round-42/cov/` containing a fenced block; the integrator stages the
  bytes into `corpus/knowledge/myth-symbol/`. No seat stages under `corpus/`
  (`reports/round-42/targets.json` shared_rules).

### 2.3 Audit, README delta, verification

- **C05** audits all 4 drafts against the C12 runbook (families 1–4 + review
  tiers), source-pointer resolution, and a fabrication hunt (each factual
  assertion traceable to a cited source; invented sources are a conformance
  defect, not style — `corpus/QUALITY.md:6-8`). Verdict needle must be the
  literal `4/4 PASS` (the runner greps it —
  `reports/round-39/run-validation.py:104-110`, `reports/round-40/run-validation.py:24-31`).
  Defects are filed with ids, not smoothed.
- **C06** drafts the README rev 2.4 delta: new revision block above rev 2.3
  (`corpus/README.md:5`), `## myth-symbol/` 23 → 27 (`:196`), the totals line
  220 → 224 (`:532`), the counts footer `(total 224 files; directory totals
  25/27/25/29/24/94)` (`:536`), plus the four new index rows **in filename
  order** (the index is filename-ordered per section). **MEASURED** current
  vector to change: `25/23/25/29/24/94` → `25/27/25/29/24/94`; total `220` →
  `224`. The `revision:` line becomes `2.4` and the runner needles must be
  updated accordingly (`## myth-symbol/ (27)`, `Total knowledge entries: 224.`,
  `directory totals 25/27/25/29/24/94`, `revision: 2.4`).
- **C07 / C08** independently verify the audit and the delta numbers; **C08**
  spot-audits 2 of 4 entries by lot plus the README row bytes.
- **A01** (adjacency ride-along) runs the 4 new entries' couples/bleed scan,
  mirroring the r37 entries-bleed precedent. **MEASURED** the four
  current new-entry couples fields resolve (all 25 linguistics and all 24
  verification entries carry a single-line `- couples:`), so a clean scan is
  expected but must be measured, not asserted.
- **Sweep must be re-run on the delivered tree**: `python3 -B reports/round-28/readme/sweep.py`
  → rows 224 == files 224, `footer_ok True`, exit 0. Sweep green is a **structural**
  reading; it is not a scholarship verdict (`reports/round-28/readme/sweep.py:22-35`).

---

## 3. Integration order + collision matrix (input to X00)

1. **K01, K02 scouts** land first (host identity for O; topic choice for C).
   O01–O12 and C01–C04 may start concurrently under the self-derive rule with the
   stated fallbacks; their landing supersedes only the specific choice each
   scout owns (host / slug), never the contract.
2. **O01 (patch) ∥ O02 (controls) ∥ O03 (predicted census)** — disjoint `out`
   paths. O03 needs O01's **join rule** (§1.2 step 2) to be fixed; if O01 has not
   landed, O03 states its own join rule and flags the coupling (H2).
3. **O04, O05** (isolated verification) need O01+O02. **O12** needs O03. **O08**
   needs the landed evidence. **O06/O09/O11** fold receipts after the reviews.
4. **C01–C04 (entries) ∥ C06 (README delta draft)**; C05 audits the 4 drafts;
   C06's row bytes freeze only after C05 passes; C07/C08 verify.
5. **A01** needs the 4 landed entries' bytes (it may run on the fenced drafts).
6. **R01, R02** adversarial review of both blocks (false-green hunt on the fix;
   fabrication hunt on the entries). **X01** trade hunter; **X02** honesty critic.
7. **S01** integration dossier + validation-leg spec; **S02** telemetry draft.
8. **Integrator**: applies O01's instrument + C's 4 corpus entries + the README
   delta; re-runs the sweep; runs the round-42 acceptance in an **isolated copy**;
   files the closing telemetry snapshot with the digest pin.

**Collision risks, all named:**

- **Shared path risk: none** — every seat has a disjoint `out` under
  `reports/round-42/`. The **single** integrator-applied corpus touch is C06's
  README delta plus the four new entry files.
- **C↔O census coupling** (H3): the corrected census is tree-dependent; claim C
  moves the tree in the same round. Pin the census state explicitly.
- **C06 row bytes vs late entry edits** (r39's own hazard): entries freeze at C05
  pass; the README rows are copied after freeze.
- **O01's new tool** must not collide with any existing `tools/harness/*` name
  (checked: no `couples*` there today).

---

## 4. Named hazards (for X00/X01 and the reviewers)

- **H1 — the new myth-symbol entries could *reintroduce* N6.** If any C01–C04
  draft wraps its `- couples:` field, the corpus gains a second wrapped field and
  the fixed extractor must handle it. **Requirement:** the four new entries carry
  **single-line** couples fields; C05 must check this explicitly, and O05's
  adversarial fixture should include a *new-entry-shaped* wrapped field to prove
  the fix generalizes.
- **H2 — the false 4/4.** A naive whitespace join yields 4 tokens including the
  phantom `prosody.md`. A fix that passes "4 tokens" while leaving the mangling
  is a **false green** (rounds 11/17/22 precedent). The controls must assert the
  **token set**, not the count, and the soft-wrap join rule (keep the hyphen,
  concatenate with no separator) must be stated.
- **H3 — tree-dependent census.** The corrected census at close ≠ at `ac47c78`
  because C lands 4 entries. O03 must name its tree; the runner must not compare
  a close-tree number to a pre-C prediction.
- **H4 — host ambiguity.** §1.1: the claim's named hosts do not exist as durable
  lane instruments; the wave must record which branch it took, or O01 will file a
  patch "against a confirmed host" that is actually a new file.
- **H5 — P01-1 policy truncation.** The filed policy's §6 recipe body is missing
  (107 lines vs the draft's 359). Any seat citing the filed policy's §6 for the
  recipe will find prose, not a script. Cite the draft (`Ca03-basename-policy.md:144-290`)
  for the recipe bytes; route the truncation as a successor note (do not re-land).
- **H6 — coverage topic must be genuinely unbuilt.** The four candidates are
  ranked on my absence reads; K02 must confirm each with a bounded sweep and
  name the neighbours the entry *extends* rather than restates (the partition's
  own convention). A restatement would be a fabricated-gap defect.
- **H7 — no runner execution.** No seat runs any `reports/round-*/run-validation.py`.
  The r39 isolation-replay protocol is the precedent for the integrator's run.

---

## Owed

- K01: the confirmed host identity + the patch surface (§1.1) — the single
  blocking input for O01. **Landed during this plan's write**
  (`reports/round-42/scout/K01-n6-scout.md`); the integrator should reconcile its
  two extra scout findings (r27/r28 successor copies; the green single-line-only
  r19 selftest) with §1.1/§1.3.
- K02: the final four topics with sources + collision check (§2.1) — the single
  blocking input for C04's fourth slug.
- O01: the patch (§1.2), including the explicit host-branch record, which copies
  it patches, and the soft-wrap join rule.
- O03: the corrected census **with its tree named** (§1.4) and the phantom
  dispositions (§1.5); also **correct or file as contested** the §4 claim that
  `sound-symbolism.md`/`writing-systems.md` are `fallback` at `dfb0719` — they
  are `direct` (see §0.6; `git ls-tree -r dfb0719 --name-only
  corpus/knowledge/linguistics/` lists both, `git cat-file -e` exits 0).
- O04: same correction (its §2 repeats the claim) — the numbers in its tables
  agree with mine; only the sentence disagrees.
- O12: the successor note carrying both the corrected census and the **P01-1**
  policy-truncation record (§1.7).
- C06: the README rev 2.4 delta with the runner needles updated (§2.3).
- Integrator: the isolated-copy acceptance run, the closing telemetry snapshot
  (digest-pinned, per `AGENTS.md`), and the LOG entry.
- P01 does not implement, run, or verify anything; this plan is its only output.

## Citations

- Claims/targets: `reports/round-42/claims.json:13-27`; `reports/round-42/targets.json`
  (`seats[id=P01]`, `shared_rules`, `seat_count 32`).
- Regimen contract: `REGIMEN.md:27-58`.
- N6 defect and cure shape: `reports/round-39/calib/Ca04-verify.md:78-93` (D1),
  `:94-101` (D2), `:107-115` (owed); queue rows
  `reports/round-40/op/defect-queue-v2.json` (`N6-couples-extractor-wrapped-field`,
  `r39-basename-successor-instrument`, `basename-couples-policy`, `N7-receipt-fidelity`).
- Host code: `reports/round-19/audit/entry-audit.py:31,34-42,75,87-95`;
  `reports/round-35/cov/C14-audit-6-10.md:225-236,252-260,263-288,281`;
  `tools/gates/provenance-audit.py:75-76,315-320` (presence-only, different check).
- Landed policy: `reports/round-39/calib/basename-couples-policy.md:7-9,14-25,36-48,50-58,60-69,71-102,104-107`.
- Verified draft (the 359-line sibling): `reports/round-39/calib/Ca03-basename-policy.md:54,67,90,100,111,144,292,306,326`.
- Wrapped field: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`.
- Disposition leg: `reports/round-35/cov/C12-audit-runbook.md:37`; entry contract
  `:28-44`; instrument install `:182-184`.
- Coverage contract and precedent audits: `corpus/QUALITY.md:6-16`;
  `reports/round-35/cov/C12-audit-runbook.md:28-44`;
  `reports/round-39/cov/C05-audit.md:44-49`; `reports/round-40/cov/C05-audit.md:24-31`.
- README state: `corpus/README.md:5,196,222,532,536`; instrument
  `reports/round-28/readme/sweep.py:22-35`.
- Gap-statement convention: `corpus/knowledge/myth-symbol/plant-symbolism.md:3`;
  `corpus/knowledge/myth-symbol/eschatology-world-end-systems.md:4`;
  `corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md:4`;
  `corpus/knowledge/myth-symbol/binding-speech-complex.md:3`.
- Register-family gap: `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:1,29,68`;
  scattered lithic content `corpus/knowledge/culture-material/ritual-garments.md:59`,
  `corpus/knowledge/civilizations/siam-thai.md:126`,
  `corpus/knowledge/civilizations/rome.md:33` (false positive).
- Runner needles / isolation precedent: `reports/round-39/run-validation.py:104-110,115-125`;
  `reports/round-40/run-validation.py:110-112,124`;
  `reports/round-39/calib/isolation-replay-protocol.md`; `templates/round-runner-template.py:11-19`.
- Command outputs (this seat, 2026-10-19, lane root, `export TMPDIR=$PWD/.scratch
  PYTHONDONTWRITEBYTECODE=1`, all read-only): (a) r19 gate on
  `phonetics-phonology.md` → `couples=0 unresolved=[]`, `TOTAL 0/1`, exit 2;
  (b) header-field census → 220 couples fields, exactly 1 wrapped
  (`phonetics-phonology.md:72`, 5 continuation lines); (c) block vs single-line
  census at `ac47c78` → `2611/2437/166/0/8` vs `2607/2435/166/0/6`; (d) the same
  over `git show dfb0719:` for the 212 r39 entries → `2508/2337/163/0/8` vs
  `2504/2335/163/0/6` (the filed policy baseline reproduced); (e) join-rule probe
  → space/newline join yields `prosody.md`, soft-wrap (keep hyphen) yields
  `tone-prosody.md`, hyphen-strip yields `toneprosody.md`; (f) `ls
  corpus/knowledge/myth-symbol/*.md | wc -l` → 23; partition census
  94/25/25/23/29/24 = 220; (g) `python3 -B reports/round-28/readme/sweep.py` →
  `rows 220 files 220`, `footer_ok True`, exit 0; (h) `wc -l` on the policy
  (107) vs the draft (359) and `grep -n '^## '` on both; (i) `git ls-tree -r
  dfb0719 --name-only corpus/knowledge/linguistics/` → 21 files including
  `sound-symbolism.md` and `writing-systems.md`, and `git cat-file -e
  dfb0719:corpus/knowledge/linguistics/sound-symbolism.md` → exit 0 (settles the
  O03/O04 `fallback`-vs-`direct` dispute in favour of `direct`); (j) byte-level
  read of `corpus/knowledge/linguistics/conlang-methodology.md:5-11` (line 7
  single, 8 blank, 9 unindented prose, 11 `## Pipeline at a glance`) refuting the
  C14-`fields_of` false second wrapped field. No filed byte was edited;
  no `run-validation.py` was executed; no git, network, or install actions.
- Landed sibling fragments reconciled by this plan: `reports/round-42/scout/K01-n6-scout.md:21-45,92-93,166-173`;
  `reports/round-42/op/O03-predicted.md:60-67,78-108,110-125,130-175`;
  `reports/round-42/op/O04-verify.md:26-45,60-110`; `reports/round-42/adj/A01-entries-bleed.md:1-25`
  (A01 records the r40 mirror-target correction: `reports/round-40/adj/A02-province.md`
  is the PROVINCE seat, not an entries scan — the entries-bleed precedent is
  `reports/round-37/adj/A02-entries-bleed.md`; §2.3 of this plan should be read
  with that pointer correction).
