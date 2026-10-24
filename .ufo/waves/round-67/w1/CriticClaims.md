# CriticClaims — attack on claims.json itself (round 67, w1)

Scope: the frozen predicates vs the counter code; 'register unowned' census gaming;
'exactly 24' vs EXTRA_IDS; NOHARM allowlist leakage; counter-code drift. Attacked:
`reports/round-67/claims.json`, `accept-c.py`, `accept-o.py`, `accept-ca.py`,
`tools/check-receipt-seq.py`. All line refs verified at lane tip; instruments commit
`b78f8b8`. No tool installs needed (read-only git + grep sufficed).

---

## F0 — BLOCKER: ACCEPT-C and ACCEPT-CA are mutually unsatisfiable through the front door; the only satisfying path is a duplicate-id cheat

This is the strongest counterexample and it is structural, not hypothetical.

- Ca leg **D4** requires `rej_opened_today >= len(R66_REJECTS) + 2` i.e. **≥6 rows** with
  `status=rejected` AND `opened=2026-10-24` (accept-ca.py:226–236). Only S801–S804 may
## F0 — RESOLVED BY L1 RULING → residual design finding: joint satisfiability REQUIRES an undeclared per-claim lands topology

Original attack (convergent with CriticFrontier/CriticSizing/RevWaveShape/ScribeGateRows):
Ca leg **D4** requires `rej_opened_today >= len(R66_REJECTS) + 2` = ≥6 rows with
`status=rejected` AND `opened=2026-10-24` (accept-ca.py:226–236), with S801–S804 each
exactly once; C leg **APPEND** bounds appended ids to `set(NEW_IDS)|EXTRA_IDS` =
S801–S828 (accept-c.py:356–358,372); S805–S828 are pinned `status=mined` (267); base
rows can't be re-opened (`oc[8]==nc[8]`, 369). At any SINGLE lands commit no legal id
exists for the 2 mandatory new gate rejects → APPEND FAIL `extra=[S829,…]`; claims.json
itself states "724 → 752" (C) while Ca implies ≥754.

**L1 ruling (w1, recorded): no counter/claims revision.** Per-claim lands separation —
A_r (S801–S804 + r66 dispositions) → A_c (C's receipt stamped where only S805–S828
append over base+A_r) → A_ca (carries S829+ rejects + round-67 lesson; D4 sees ≥6
today-dated rejects). APPEND stays bound to NEW_IDS∪EXTRA_IDS. Ruling verified sound:
each counter is evaluated inside a materialized clone at its own stamped commit, so
C never sees A_ca bytes and Ca never sees a bounded id space. The joint predicate IS
satisfiable as sequenced — my "unsatisfiable" framing is withdrawn.

Residual defects that survive the ruling:
- **Undeclared dependency**: the frozen text never states that C and Ca need DIFFERENT
  lands commits. The `note` field describes "a third lane commit" (post-records),
  implying one lands; an honest single-commit landing of all rows FAILs C. The
  sequencing A_r → A_c → A_ca is load-bearing but exists only in L1 resolution, not in
  claims.json, the counters, or the wave spec as frozen bytes. Correction: record the
  lands topology in the closure manifest/lesson so an auditor replaying "one lands"
  doesn't derive FAIL.
- **"registry 724 → 752" is tip-false**: at A_ca and at round tip the registry holds
  ≥754 physical rows (752 + ≥2 rejects). C's statement is true only at A_c. Correct
  the arithmetic wording in the r67 lesson/manifest, or annotate "at C's lands".
- **The cheat path is still open, merely no longer forced** (see F1): shadow rows
  duplicating BASE ids placed before the genuine rows still satisfy D4's
  rows-not-ids `rej_opened_today` count while invisible to APPEND's last-writer-wins
  `tip_set`. With honest S829+ now legal the cheat isn't needed — but nothing detects
  it, and at A_c the same trick can smuggle unbounded registry mass. Global id
  uniqueness + line-count-delta assertions remain the smallest fix.
Impacted axes (under the sequencing ruling): **calibration** — D4's "first-class
rejected rows" is enforced as a count, not an identity; **coverage** — APPEND's
added-set bound remains ineffective against duplicate ids at A_c.


## F1 — APPEND is not a diff: last-writer-wins dedup + no total-count check

Independent of F0: `tip_set`/`base_set` dicts (accept-c.py:353–354) collapse duplicate
ids to their last occurrence; `missing_old`/`extra_ids`/`mutable_bad` are computed over
that collapsed view. Consequences:
- Unlimited shadow rows under any pre-existing id, zero legs see them (no leg asserts
  per-id uniqueness outside S805–S828/S801–S804).
- One in-place rewrite of any single base row is masked: a shadow *identical* to the
  base row placed before a *mutated* genuine row makes `tip_set[id]` hold the shadow →
  compared equal to base → the real mutation vanishes (inverse ordering of the F0 trick).
- "registry 724 → 752 rows" is asserted nowhere: no leg counts lines. Base verified at
  724 rows, 0 duplicate ids; the claim's own arithmetic cannot be checked as written.
Correction: enforce id uniqueness globally + line-count delta == declared count.

## F2 — counter-sha pin reads the WORKTREE, not the stamped/lands revision

`check_counter_sha` does `blob = read_worktree(root, cpath)` and only falls back to
`read_rev(root, "main", …)` (tools/check-receipt-seq.py:168–170). In `--lands` mode the
receipts themselves are read at the stamped rev, but the counter they are pinned
against is whatever sits in the verifier's checkout. Net guarantee: receipt ↔ worktree
self-consistency only. A counter whose committed bytes at `lands` differ from the
evaluated copy is undetectable; conversely an honest receipt FAILs if the verifier's
worktree copy drifted. Correction: hash `read_rev(root, h["stamped"], cpath)` first,
worktree only as documented fallback.

## F3 — 'frozen' is social: no sha pin for instruments anywhere; SEQ leg is greppable text

- claims.json and the counters record no expected sha256 for the counter files
  (self-sha is *reported*, never *asserted*). `git log` shows the instruments
  (claims.json + 3 counters + tool + mutants + controls) committed at `b78f8b8`, but no
  leg asserts `git diff b78f8b8..lands -- reports/round-67/*.py tools/check-receipt-seq.py`
  is empty. A post-freeze weakening edit to any counter keeps every receipt internally
  consistent (the recorded self-sha just changes).
- Ca leg **SEQ** checks only literal substrings: `"--lands" in text`,
  `"required=True" in text`, `"mv_rev == lands" in text` (accept-ca.py:243–250). A
  rewritten counter can carry all three inside a comment while deleting the gate.
  Correction: pin the three frozen shas in claims.json (or assert empty diff vs
  `b78f8b8`) inside the SEQ leg; keep the textual checks as lint only.

## F4 — 'register unowned' census: TRUE at base, but it's a filename-only claim with a plural hole, never re-asserted

Ran the frozen pattern at base: `git ls-tree -r --name-only ad5b52b0… -- corpus/knowledge |
grep -ciE '(^|[^a-z])(medicin|healing|…)([^a-z]|$)'` → **0** (exit 1). Broadened stem
sweep (medic/heal/remed/surg/hospit/herbal/materia/therap/clinic/tonic/elixir/pharmac/
midwif/barber…) matches only `material` inside "…-material-culture" names — no evasive
owner exists at base. So the premise is honest TODAY. Two residual weaknesses:
- The pattern cannot see English plurals: `remedies`, `medicines`, `hospitals`,
  `surgeries`, `leeches` all evade `(…)([^a-z]|$)`. The premise is literally "0
  *filename* owners under this grep" — a future `folk-remedies.md` owner would not have
  tripped it. Statement is true but narrower than "register unowned" reads; the claim
  honestly defers this to `review_only`.
- No leg re-runs the census or any ownership check at lands — the unowned premise is
  preamble, not predicate. If the register were actually owned (semantically), ACCEPT-C
  still passes; calibration is unaffected but **coverage** gets credit for opening a
  register that was already held.

## F5 — NOHARM enforces 'one new entry' only inside corpus/knowledge; .md-only sweep + symlink re-point

- `git diff --name-status BASE -- corpus/knowledge` allowlists `[ENTRY]`
  (accept-c.py:378–384) — good as far as it goes. But the claim sentence says "one new
  entry" / "corpus 240 → 241" while nothing forbids additional new knowledge files
  *outside* `corpus/knowledge` (e.g. `corpus/references/healing-notes.md`), and SWEEP's
  `disk_files` counts only `*.md` inside `corpus/knowledge` (sweep.py:97–102) — a
  non-.md companion inside corpus/knowledge is invisible to both legs.
- Re-point leak: ENTRY itself can be a symlink out of the diffed tree — `diff
  --name-status` shows `A corpus/knowledge/…/medicine-healing-codes.md` (allowed), FILE
  follows the link via `open()`. The "new file" is a pointer; content lives outside the
  audited path. Cheap fix: assert `git ls-tree -s` mode for ENTRY is `100644`, not
  `120000`, or `test -f && ! -L`.
- Disposition lands do NOT leak the allowlist: all Ca lands are outside
  corpus/knowledge (SOURCES.md, LOG, SCORECARD, QUALITY, lessons, .ufo, reports) — that
  part of the design holds.

## F6 — Facade mutants / facade selftest: O legs verify printed output, not mechanism

- MUT runs each committed mutant and requires `rc==1` + exactly the pinned `FAIL <name>`
  lines (accept-o.py:249–256). A mutant need not be a mutation of the tool at all — a
  stub printing `FAIL moved-receipt-fail` satisfies it; nothing asserts the mutants
  diff from `tools/check-receipt-seq.py` by bounded edit distance.
- SELFTEST asserts `"14/14" in stdout` of the tool's own print (accept-o.py:165–167) —
  a self-graded exam. Combined with F3 (tool bytes unpinned), claim O's "14/14 selftest
  fixtures pin every failure class" is unfalsifiable from the receipt alone. The only
  externally-grounded O legs are R66 (real git topology vs hardcoded
  4589ebdd/65fe8572 — verified the check uses committed bytes via `main:` show + log)
  and the fixture-driven LANDS/TOPO/HEADERS, which DO exercise the real tool — those
  legs are sound and would catch a pure facade. Residual hole: counter-sha/tree pins
  (F2's drift) have no fixture/mutant covering them.
  Correction: MUT should assert each mutant is a ≤N-line diff of the tool; add a
  counter-sha fixture (receipt sha ≠ lands-committed counter sha → named fail).

## F7 — predicate sentence vs code drift (stricter-than-claim legs that can fail honest work)

- **CAPTURE**: leg text says "a same-page capture **or an explicit no-capture
  reason**"; code unconditionally requires `CAPTURE_RE.search(src)`
  (accept-c.py:409–411) — the no-capture-reason branch does not exist. An honest row
  with a documented no-capture reason fails.
- **ONEID**: `foreign` bans ANY parenthesized S-id outside S805–S828
  (accept-c.py:287–289): citing `(S753)` or `(S801)` for context fails
  `out_of_claim_set`. The claim only says each of the 24 is cited exactly once — the
  foreign-citation ban is an unadvertised constraint on the entry's prose.
- **SWEEP**: `"topic_mismatch" not in sw.stdout.replace("topic_mismatch 0","")`
  (accept-c.py:393) — a sweep printing `topic_mismatch: 0`/`topic_mismatch=0` fails the
  honest lane; format-brittle negative check.
- **D3/D4 label drift** (cosmetic): claims leg "D3" tests R66-D4 (LOG/SCORECARD), "D4"
  tests R66-D5 (rejected rows); R66-D3 is covered by SEQ. Auditors reading "D3 PASS"
  will misroute it to the receipt-sequencing defect.

## F8 — provenance leaks and minor holes

- `CENSUS = "/home/vgpnk/Projects/shokunin/scripts/sources-census.sh"` (accept-ca.py:54):
  absolute HOST path outside `--root`/lands — the evaluated verdict depends on an
  unpinned, uncommitted script living outside the clone. Same class of defect the
  receipt protocol exists to kill. Fix: copy the census into tools/ or resolve it
  relative to root.
- D1 manifest has no completeness leg: `cat-file -e` verifies listed paths exist at
  lands, but nothing checks coverage against `git ls-tree .ufo/waves/round-66` — 8 seat
  reports + 1 EXCLUDE line satisfies D1 while ~18k files stay undurable. "Dispositions
  the r66 wave tree" is curated-subset by construction; `review_only` admits this.
- STAMP trusts `git rev-parse main` — the protocol hard-assumes the clone's branch is
  named `main`; `dirty_tracked` is printed but never asserted.
- ROWS `ENTRY not in c[10]` is substring containment — `used-by` naming the entry plus
  junk passes (weak, low impact).
- `check_topo` finds carriers via `git log -1 main -- rpath`
  (check-receipt-seq.py:188) — main-relative, fine post-records under STAMP, but not
  stamp-relative; an old receipt file touched in a later commit re-parents cleanly.

## What holds (no attack found)

- Census result at base is genuinely 0; "culture-material 33" and "corpus 240" match
  `ls-tree` counts; 724→752 arithmetic is self-consistent given declared +28.
- SET/ROWS/ONEID/RESTATE/HOSTS/LINK legs are real per-row gates; the CAPTURE
  target-mismatch comparison pins capture↔live URL same-page identity.
- LANDS/TOPO/HEADERS/R66 legs in accept-o exercise actual git topology and committed
  bytes; moved_past, wrong-parent, missing_headers are not greppable facades.
- D4's "+2" cannot be satisfied by re-opening S801–S804 (each must be unique) — the
  arithmetic intent is right; the missing id space is what the L1 lands-sequencing
  ruling resolved (F0).

## Ranked asks to the L1 (smallest safe corrections)

1. **F0 (post-ruling)**: the round passes honestly ONLY under the A_r → A_c → A_ca
   lands sequence — write that topology into the closure manifest/lesson (the frozen
   text never declares it), and annotate C's "724 → 752" as at-A_c or fix to ≥754.
   The counter revision itself is ruled out; sequencing is the fix.
2. **F1**: multiset compare in APPEND + global id-uniqueness + line-count-delta
   == declared additions — kills the shadow-row channel at every lands commit.
3. **F3**: pin the three frozen counter shas (and tool sha) in claims.json or assert
   empty diff vs `b78f8b8` in the SEQ leg.
4. **F2**: hash the counter at `stamped`, not the worktree.
5. **F6**: bounded-diff check that mutants derive from the tool.
6. **F8**: replace the absolute CENSUS path; add ENTRY symlink/mode check to NOHARM.
7. **F7**: implement the no-capture-reason branch or strike it from the leg sentence;
   scope ONEID's foreign ban to S-ids in registry (or document it); fix D3/D4 labels.

Report: .ufo/waves/round-67/w1/CriticClaims.md
