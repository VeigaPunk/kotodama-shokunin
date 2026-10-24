# CriticSizing — round 67 claim-sizing attack (w1)

Attack target: claim sizing — (a) is C provable by a do-nothing control / does the census
pattern cover the entry filename; (b) is 24 rows right-sized or padding; (c) are the 3
claims separable — is Ca's SEQ counter-read a record-dependency or real coupling.

## FINDING 1 — C vs Ca id budget: hard conflict under a single-lands reading; RESOLVED by L1 per-claim-lands ruling (recorded as design finding)

Counterexample: Ca-D4 (`accept-ca.py:226-236`) counts rejected rows by
`c[7] == "rejected" and c[8] == "2026-10-24"` over **every** `ROW_RE`-matching line in
`corpus/SOURCES.md` and requires `rej_opened_today >= 6`. Only 4 ids are available inside
C's allowed-added set for rejects (S801-S804, all required present). Base contains **zero**
rejected rows dated 2026-10-24 (`git show base:corpus/SOURCES.md | grep rejected`: opened
dates are only 10-19 x5, 10-22 x10, 10-23 x7). Therefore D4 needs >=2 brand-new row lines
with fresh ids (S829+). But C-APPEND (`accept-c.py:353-358`) collects every
`ROW_RE`-matching line anywhere in SOURCES.md — `reg_lines`/`tip_set` are not scoped to the
`## Registry` section — and fails `extra_ids=[sid not in NEW_IDS|EXTRA_IDS]`. So:

- land S829/S830 rejected rows anywhere in SOURCES.md → C-APPEND FAIL (extra_ids);
- withhold them → Ca-D4 FAIL (rejected_opened_today <= 4 < 6);
- re-use S801-S804 with duplicate rows → D4 `nonunique` FAIL and C-SET-adjacent dup;
- give a new reject an id inside S805-S828 → C-ROWS FAIL (`status=rejected` vs 'mined').

There is no single tree that satisfies both counters simultaneously — even the
`## Leads` section fails because C's APPEND scans the whole file, while a second file is
invisible to D4 (`REGISTRY = "corpus/SOURCES.md"` only). The claim statement's own sizing
arithmetic ("registry 724 -> 752") confirms no id budget was reserved for the D5 gate
rejects. Impacted axes: coverage + calibration.

**L1 RESOLUTION (r67 w1, this wave): no counter/claims revision.** Per-claim lands
separation — C's receipt is evaluated at its own lands commit `A_c` (materialized clone,
`stamped == evaluated == A_c`) where only S805-S828 append over base; Ca's lands `A_ca`
lands later and carries the S829+ rejects plus the round-67 lesson; `A_r` (S801-S804 +
r66 dispositions) lands before `A_c` so EXTRA_IDS still covers them. APPEND stays bound
to NEW_IDS∪EXTRA_IDS; D4 sees >=6 today-dated rejects at `A_ca`. The joint predicate IS
satisfiable **as sequenced** — the receipt protocol (`--lands` + stamped==evaluated in a
materialized clone) is exactly the machinery that makes per-claim lands commits sound.

Residual design notes (kept on record, non-blocking):
- The ordering is now load-bearing: C's evaluation MUST be stamped before any S829+ row
  lands, and `A_r` before `A_c`. If integration lands the reject rows first (or in the
  same commit as C's lands tree), C-APPEND fails with no recourse — the sequencing is an
  operational constraint, not enforced by any counter. Worth one line in the integration
  runbook / lane lessons: claim lands order `A_r < A_c-eval < A_ca`.
- C's committed statement arithmetic ("724 -> 752") is true at `A_c` but the tip registry
  ends at >=754 after `A_ca` — a tip-vs-lands divergence the re-derivation at closure
  must keep straight (the claim is about the lands tree, not tip; auditors diffing tip
  will see S829+ rows outside the declared set).
- The alternative fix (widening EXTRA_IDS / declaring S829+ in claims.json) remains the
  more robust shape for future rounds — per-claim lands works here only because the
  conflicts are strictly ordered (C's allowed set is a subset-closed prefix of Ca's).

## FINDING 2 — the stated attack vector is REFUTED: the census pattern does cover the entry filename, and the control fails correctly

- `grep -ciE '(^|[^a-z])(medicin|healing|...)([^a-z]|$)'` over base `corpus/knowledge`
  prints **0** — the premise ("0 filename owners") is true at base; my wider sweep
  (`health|heal|medic|remed|physic|doctor|surg|apothec|hospit|leech|shaman|curander|herbal|
  midwif|nurs|disease|illness|cure|therap|drug|pharmac|hygien|body`) over all base
  knowledge filenames finds only `adornment-body-codes.md`, `bathing-and-body-hygiene.md`,
  `phonology-sanity-gate.md` — all already hedged in the claim text as partial-scope.
- `medicine-healing-codes.md` IS matched by the pattern ('medicine' at path segment start
  after `/`; 'healing' flanked by `-`); a hypothetical `health-and-healing.md` is also
  matched ('healing' again). `leeches-and-physick.md` matches ('physick').
- Do-nothing: `dry-run-c.txt` exits 1 with FILE/SET/ONEID/RESTATE/HOSTS/CAPTURE/TOPIC all
  FAIL — the predicate is not reachable with zero data. C cannot be proven by doing nothing.

## FINDING 3 — MEDIUM: the census alternation is a *mechanically missable* register detector, and no leg re-checks the premise at lands

Right-side boundary `([^a-z]|$)` makes every alternation atom effectively singular and
non-derivational. Concrete misses on filenames a lane could choose:

- the whole 'health' family: `mental-health.md`, `health-practices.md` (only 'healing' is an
  atom; 'health' alone never matches);
- plurals/derivations: `home-remedies.md`, `plague-doctors.md`, `hospitals-x.md`,
  `physicians-x.md` (atoms are `remedy|remedie|doctor|hospital|physician`, not stems);
- `midwifery.md`, `herbalism.md`, `curandera-codes.md`, `apothecary.md` ('apothec' followed
  by 'a' fails the boundary), `leeching.md`, `shamanic.md`, `nursing.md`, `surgery` variants
  like `surgeons.md`.

Verified empirically: 3/10 register-named candidates matched. Base happens to contain none
of these, so the claim's 0-count premise is currently true — but the census is not itself a
frozen *leg*; no counter leg re-verifies "0 owners" at lands. Consequence: if the lane (or a
sibling in this wave) ever adds a `midwifery-codes.md`-style owner, ACCEPT-C-67 still passes
unchanged — an overlap the instrument cannot see. `review_only` discloses "semantic register
ownership beyond filename/topic-line census", so the fixable part is smaller than it looks:
name the census a premise, or (better) extend the atoms to stems (`health`, `remed|medic`,
plural/derivation suffixes) in a claims.json revision. Same-cost hardening: make APPEND or a
new leg re-run the census over the lands tree.

## FINDING 4 — MEDIUM: claims.json's separability_note mislabels SEQ — Ca executes O's tool (functional coupling), while the counter-text checks are greppable-dead-code weak

`accept-ca.py:243-255` SEQ does two things of opposite defect class:

1. **Over-coupled (real, not record-dependency):** it *runs*
   `tools/check-receipt-seq.py --selftest` and requires `14/14` in stdout. That is asserting
   the O claim's measured output — exactly what `claims.json` separability_note denies
   ("Ca asserts the counters' structure, never their measured outputs"). If O's tool ships
   with a failing fixture, Ca fails though every Ca record is right. Expected Ca->O edge is
   therefore functional, not record-only; the manifest should classify it so.
2. **Under-coupled (weaker than labeled):** the per-counter checks are source greps —
   `'--lands' in text`, `'required=True' in text`, `'stamped revision'/'evaluated revision'`
   in text, `'mv_rev == lands'` in normalized text. A counter with those strings in a comment
   or dead branch, and no executed equality assertion, PASSES SEQ. SEQ proves the strings are
   on disk, not that any counter enforces stamped==evaluated. (Mitigation in place: each
   counter's own STAMP leg is independently evaluated by its own run; and O's tool checks
   receipts behaviorally. So the SEQ text-checks are belt-and-braces — but as written they
   are satisfiable by decoration.)

Also QUOTES (`accept-ca.py:268-279`) runs `tools/check-gate-quotes.py` (exists at base) and
requires `>=20` of S805-S828 named in `lessons/round-67.md` — a true Ca->C data edge
(disclosable as record-dependency) but note it is satisfiable by *naming* 20 ids; the quote
checker only finds quote-format findings, not semantic use.

## FINDING 5 — LOW: `separability-real.txt` — declared deliverable with no enforcing leg

`claims.json` separability_note promises "a complete run is filed at
reports/round-67/telemetry/separability-real.txt via the bounded checker" — the file is
absent at base (expected), is in **no claim's `lands` array**, and no leg greps for it.
`tools/check-claim-separability.py` exists at base, so the capability exists; the evidence
simply has no predicate. A complete pass leaves the promise unkept and unflagged — same
class as r66's unforced records. Correction: add a Ca leg asserting the file exists and
names all three claims, or demote the note from promise to intent.

## FINDING 6 — LOW: recurring one-round-late evidence durability

D1 (R66 defect) required a manifest because `.ufo/waves/round-66/` was untracked. This wave
writes ~64 seat reports under `.ufo/waves/round-67/`, and r67's only tracked `.ufo` landing
is the small `stage/mut-o/` subset — the r67 wave tree is again untracked at lands,
guaranteeing an R67-Dx echo next round. Sizing note: the D1 fix is per-round, not protocol;
a claims-template rule ("wave manifests must cover their own round") would amortize it.

## FINDING 7 — 24 rows: defensible arithmetic, disclosed padding incentive

Not a counter defect. 12 scout seats x 2 rows = 24 distinct traditions (Hippocratic,
Ayurveda, TCM, Ibn Sina, monastic, Roman military, Egyptian, Galen, plague-costume,
Paracelsus, Mesoamerican, Tibetan, sweat-lodge, apothecary, Vesalius, lazaretto, Kampo,
bimaristan, barber-surgeons, sangoma, asklepieia, moxibustion, consilia, medical amulets)
with HOSTS>=10 diversity and per-row RESTATE/CAPTURE checks — historically consistent with
prior batches (masks 46, footwear 41, headgear 24, games 26, scent 22, pastoralism 22).
Sizing is plausible. Residual, disclosed in review_only ("blind per-row support"): an exact
quota of 24 means if a scout returns weak material the incentive is to land it anyway
(tier-B inflation) rather than shrink the claim — the counter cannot detect padding-by-
inclusion; only the L1's judgment can. Also note `claims.json`'s alternation lists 'medicin'
AND 'medicine' (redundant, harmless).

## Cosmetic

- `accept-ca.py:232` computes `new_rejects` and never uses it (dead variable).
- D4's ">=2" is implemented as `rej_opened_today < len(R66_REJECTS)+2` — correct but silently
  assumes S801-S804 themselves land dated 2026-10-24; if the dispositions date them
  2026-10-23 (their r66 provenance), D4 needs **4** new rejects while the text says ">=2".
  Worth a one-line comment in the counter.

## Verdict

- Do-nothing attack on C: **refuted** (control exits 1; census premise true at base; entry
  filename is covered by the pattern).
- Census instrument: **true but unsound-by-construction** — misses plural/derivational and
  the 'health' stem family (FINDING 3).
- Separability: C-APPEND vs Ca-D4 is a hard id-budget contradiction on any single tree
  (FINDING 1) — **RESOLVED by L1 ruling: per-claim lands commits, no counter revision;
  ordering A_r < A_c-eval < A_ca is now load-bearing**; SEQ is
  functionally coupled to O's selftest while being greppable-weak on counter text
  (FINDING 4); `separability-real.txt` unenforced (FINDING 5).
- 24 rows: right-sized for the topic map; padding risk is incentive-level, disclosed
  (FINDING 7).

Report: .ufo/waves/round-67/w1/CriticSizing.md

## Addendum — post-filing resolution

L1 ruled (this wave): the FINDING-1 conflict is resolved without counter revision via
per-claim lands commits (`A_r` → `A_c` eval → `A_ca`); the joint predicate is satisfiable
as sequenced. FINDING 1 updated in place to a design finding with the load-bearing
ordering constraint and tip-vs-lands arithmetic caveat recorded. Verdict text below
retained as the pre-ruling severity assessment — superseded.
