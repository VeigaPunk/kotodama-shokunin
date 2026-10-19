- Seat: Ca04 | verifier | claim Ca | date 2026-10-19 | baseline dfb0719

# Ca04 — verification of Ca03's basename-couples policy

Scope: `reports/round-39/calib/Ca03-basename-policy.md` checked against the filed
resolver code (`reports/round-19/audit/entry-audit.py:74-96`,
`reports/round-35/cov/C14-audit-6-10.md:249-288`, plus the r27 lineage), A12's
cross-check (`reports/round-37/adj/A12-gap-fill.md`), and P01's required shape
(`reports/round-39/plan/P01-plan.md:223-238`). Ca03's §6 script was re-run
byte-exact from the draft (sed 150,257 of the file → `python3 -B`, read-only),
and every §7 citation line was opened. Disagreements are filed as defect rows
below, per `P01-plan.md:240-246`.

## Verdict

The policy's core (§1 token grammar, §2 two-tier/four-class resolution, §4
group alignment, §5 limits, §6 recipe, §7 adoption evidence) is **verified
against code and filed evidence; adoptable**. Two defects are filed — D1
(extractor scope, live instance found) and D2 (missing disposition leg vs the
plan) — both fixable with one sentence each at integration time; neither
invalidates the 15-ref finding the policy exists to close.

## Checks performed

1. **§6 script fidelity + reproduction.** Re-ran the exact fenced script:
   Part 1 `refs=334 → direct=319 fallback=15 ambiguous=0 unresolved=0`, sacred-kingship
   `36 = 21 direct + 15 fallback`, RESULT `PASS`; Part 1b 15/15 `OK`,
   `misaligned=0` (7 linguistics / 6 culture-material / 1 verification / 1
   synthesis); Part 2 `entries=212 refs=2504 → direct=2335 fallback=163
   ambiguous=0 unresolved=6`, 5 distinct as quoted; Part 3 delta reproduced
   (`linguistics/hero-journey-variants.md` policy=unresolved,
   C14-as-written=fallback → myth-symbol). Matches the draft's quoted outputs,
   my independent probe (same numbers, written separately before the draft
   landed), A12 (`A12-gap-fill.md:9-24`), A02 (`A02-entries-bleed.md:7-23`),
   A06 (`A06-verify.md:29`), A08 (`A08-verify.md:17`), K04
   (`K04-entries-scout.md:43,56,61`).
2. **§1/§2 semantics vs code.** Token regex `entry-audit.py:31` ✓; one-level
   brace expansion `:34-42` ✓; single-line `- couples:` capture `:75` ✓; Tier-1
   candidate order entry-dir → lane-root → `corpus/knowledge/` exactly as
   `:87-95` ✓; Tier-2 index glob `corpus/knowledge/*/*.md` = C14 `:252-260` ✓;
   four-class bucketing = C14 `:271-288` ✓. Zero divergence between the policy
   text and the code it cites.
3. **§4 vs A12.** All 15 mappings and group alignments reproduce exactly
   (A12:13-24; script Part 1b; my probe). ✓
4. **§5.1 slash-gate narrowing — CONFIRMED as a decision, not an error.**
   Code fact: C14 `:281` keys `basename(ref)` for *any* Tier-1-unresolved token,
   slash-bearing included. Filed precedent FOR the narrowing that the draft
   does not cite: r27's resolver applies its partition candidates to slash-free
   tokens only (`reports/round-27/audit/entry-audit.py:129-131`). The narrowing
   is consistent with the lane's stricter lineage; recommended for adoption as
   drafted. (Suggested, optional: add the r27 citation to §7 as corroboration.)
5. **§5.4 arithmetic.** sacred-kingship 21 direct = 7 full-path refs + 14 bare
   same-partition basenames resolving via the entry-dir base ✓ (probe).
6. **Gate-consequence observation (supports the policy's own preamble).** The
   filed r19 instrument FAILs the admitted sacred-kingship entry today:
   `python3 -B reports/round-19/audit/entry-audit.py
   corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md` →
   `unresolved=[15 tokens]`, `TOTAL 0/1`, exit 2. The r27 instrument's couples
   leg is clean (36/36 via its partition fallback; overall bar=False from its
   source-locator leg, 30/31, `entry-audit.py[r27]:329` requires every bullet
   to carry a locator — a separate, pre-existing condition, not couples). The
   policy's "successor instruments implement this policy" line is therefore
   load-bearing: until one exists, the r19 gate keeps failing this entry.
7. **§7 citation audit — no fabrication found.** Every load-bearing line
   opened and confirmed: queue row `defect-queue.json:202-211`; claim/durable
   path `claims.json:19-24` (`:22` after_required); seat `targets.json:90-95`;
   `A02:7,23`; `A06:29,49` (incl. the 222-global-distinct unit note at :29);
   `A08:17,31`; `S04:38,80,109,124`; `K04:43,56,61`; `C14:69,112-119` (the 4-
   and 148-shorthand populations, 8 unresolved / 7 distinct at 201 entries);
   `language-contact.md:7` (the trio; its other two seeds exist);
   `gate-frozen-run-standard.md:15` (glob fragments);
   `label-channel-routing-verification.md:14` (X26-1 phantom, still live).
   Part 2's five distinct unresolved names each resolve to the attributed
   source line.

## Disagreements filed

- **D1 (policy vs code, live instance): §1's single-line extractor silently
  zeroes wrapped couples fields.** The corpus has exactly one wrapped field:
  `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`. The policy's
  extractor (per `entry-audit.py:75`) captures **0 tokens** there; the full
  field names 4 `.md` targets — `sound-change.md`, `tone-prosody.md`,
  `sound-symbolism.md`, `writing-systems.md` — of which 2 exist (would be
  `direct`) and 2 are phantoms. C14's block parser (`C14-audit-6-10.md:227-236`,
  continuation lines) captures them, so policy Part 2's "6 unresolved (5
  distinct)" undercounts the block-parser population; C14's 8/7-distinct count
  at 201 entries is consistent with the same mechanism (its distinct set
  includes the mangled token `prosody.md`, split from `tone-prosody.md` by the
  line break — `to-verify`, not re-derived). Note the line-break mangling is an
  extractor hazard *no* current instrument handles. Fix: §1 adopts block
  extraction through the next `- ` header field, or carries this named
  exception + re-run trigger. No effect on the 15-ref population: all eleven
  r35/r36 couples fields verified single-line (probe).
- **D2 (policy vs plan): the disposition leg P01 §2.4.4 requires is absent.**
  `P01-plan.md:237-238` requires the policy to state what an `unresolved` count
  means for an entry audit, per the runbook's pointer family — C12 row 2:
  dangling token is a **blocker** unless the same line marks it `(to-verify`,
  then documented/non-blocker (`reports/round-35/cov/C12-audit-runbook.md:37`).
  The policy's §3 has reporting rules but no blocker/document disposition
  mapping. Fix: one sentence in §3 adopting the C12-row-2 treatment for
  `unresolved` couples tokens.
- **Nits (no action required):** Part 3's C14 approximation reports
  `unresolved` where C14 would report `ambiguous` for a slash-bearing token
  with >1 index hits — not exercised by the demo token; fine for a
  demonstration, worth a footnote if the recipe is canonized.

## Owed

- Integrator: when landing the fenced document at
  `reports/round-39/calib/basename-couples-policy.md`, either apply D1+D2
  (one sentence each) or land verbatim and queue both to the successor
  instrument — an explicit recorded choice either way; then close queue row
  `basename-couples-policy` with the pointer (Ca03's Owed, unchanged).
- to-verify: a full block-parser couples recount corpus-wide (this seat's
  partial: exactly 1 wrapped field, 4 tokens, 2 phantom — commands above).

## Citations

- Verified object: `reports/round-39/calib/Ca03-basename-policy.md` (§1 `:54-65`,
  §2 `:67-88`, §4 `:100-109`, §5 `:111-142`, §6 script `:149-258`, §7 `:292-303`).
- Resolver code: `reports/round-19/audit/entry-audit.py:31,34-42,74-96,125-133`;
  `reports/round-35/cov/C14-audit-6-10.md:227-236,249-288` (`:281` slash-bearing
  basename key; `:227-236` block parser); `reports/round-27/audit/entry-audit.py:109-140`
  (`:129-131` slash-free partition loop), `:143-171`, `:274-286`, `:329`.
- r37 record: `reports/round-37/op/defect-queue.json:202-211`;
  `reports/round-37/adj/A12-gap-fill.md:9-26,38`; `A02-entries-bleed.md:7-23,43-47`;
  `A06-verify.md:29,49`; `A08-verify.md:17,31`; `S04-integration-draft.md:38,80,109,124`;
  `K04-entries-scout.md:43,56,61`.
- Plan conformance target: `reports/round-39/plan/P01-plan.md:223-246`.
- Disposition leg: `reports/round-35/cov/C12-audit-runbook.md:37`.
- D1 instance: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
  (field lines; `sound-symbolism.md` and `writing-systems.md` exist in
  `corpus/knowledge/linguistics/`, `sound-change.md` and `tone-prosody.md` do not —
  `ls` output this seat, 2026-10-19).
- Command outputs (this seat, 2026-10-19, lane root, tree at `dfb0719`,
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, all read-only):
  (a) independent probe over the eleven entries → 334/319/15/0/0, 15 mappings
  matching A12, 0 corpus-wide basename collisions across 212 unique basenames;
  (b) Ca03 §6 script re-run byte-exact → Part 1 PASS, Part 1b 15/15 OK,
  Part 2 `212/2504 → 2335/163/0/6` (5 distinct as quoted), Part 3 delta;
  (c) r19 gate on sacred-kingship → FAIL, 15 unresolved, exit 2; (d) r27 gate
  → `couples_resolved=36, couples_unresolved=[]`, `quality_bar=false` on the
  30/31 locator leg; (e) wrapped-field census → 1 field (`phonetics-phonology.md`),
  0 tokens captured single-line vs 4 named in the full field. No filed byte was
  edited; no `run-validation.py` was executed; no git, network, or install actions.
