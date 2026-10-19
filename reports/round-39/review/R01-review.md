- Seat: R01 | reviewer | claim cross | date 2026-10-19 | baseline dfb0719

# R01 — adversarial review of both blocks: fabrication hunt on the four entries; protocol soundness

Scope: the two assignments in `reports/round-39/targets.json` seat R01 — (1) a fabrication hunt on
the four coverage entry drafts, (2) a soundness review of the Ca block (protocol, replay,
basename policy, policy verification). Every claim below was re-measured by this seat from the
filed bytes; nothing is accepted from a sibling's self-audit without reproduction. Readings taken
2026-10-19 at HEAD `dfb0719711204b5943432034bd80c8dc248acddd` == declared baseline `dfb0719`;
`git status --porcelain` → `?? reports/round-39/` only; corpus verified clean this seat at
review time (0 dirty rows, `ls corpus/knowledge/verification/*.md | wc -l` → 20, total 212,
README sha256 prefix `b80274bcd24b8b6e6`). All python/grep ran with
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. **No `reports/round-*/run-validation.py`
was executed anywhere, in-tree or otherwise.** This seat wrote only this fragment plus disposable
scratch (`.scratch/r01/**`). Findings are filed for the integrator to disposition (fixed,
routed-with-owner, or recorded); none is a canon or admission verdict.

## 1. Verdict summary

**No fabrication found.** Every load-bearing citation I checked in the four entry drafts and the
Ca block resolves to real bytes that say what the drafts say they say; every pinned digest I
recomputed matches. The findings below are precision, adjudication, and completeness items — not
invented sources, not fabricated measurements, not bleed.

| fragment | fabrication hunt | findings filed here |
|---|---|---|
| C01 `worked-example-verification.md` | **clean** — all sweeps, all 31 spot-checked anchors, the sha16 pin, and the F1/F2 demonstration reproduce | R01-11 (note) |
| C02 `index-sweep-verification.md` | **clean** — staged digest byte-exact, ~20 anchors verified, instrument claims verified | R01-8 (minor) |
| C03 `contact-strata-verification-gate.md` | **clean** — 7/7 source digests, all five sweep counts, the staged digest, and the cited lines reproduce exactly | none |
| C04 `append-only-record-verification.md` | **clean** — all four absence sweeps reproduce (0/0/0/12); ~20 anchors verified incl. AGENTS.md:32-39 | R01-9 (minor) |
| Ca01 protocol | mechanics verified against filed bytes; author smoke-run claims consistent with everything this seat measured | R01-2, R01-3, R01-5, R01-6 |
| Ca02 replay | evidence strong and honestly bounded; one disposition-level conflict with Ca01 §7 | **R01-1 (the round's top finding)** |
| Ca03 policy | §6 script re-run byte-exact by this seat; anchors verified | R01-7 (minor) |
| Ca04 verify | D1 reproduced live by this seat; verdicts confirmed | none |

## 2. Fabrication hunt on the four entries — what reproduced

### 2.1 C01 — worked-example-verification (`reports/round-39/cov/C01-entry-1.md`)

- Gap sweep reproduced exactly: `grep -rl "NON-CANON" corpus/knowledge/*/*.md | wc -l` → **22**;
  `grep -ril "worked example" …` → **18**; `grep -rEc "^## .*([Ee]xample|[Ff]ixture)" … | awk sum`
  → **20**; the five absence probes → **0 0 0 0 0**. All as quoted in the entry's `- gap filled:`.
- The §10 demonstration is real, not asserted: `corpus/knowledge/culture-material/timekeeping-instruments.md`
  hashes to sha256 prefix **`9805c0b854334ed3`** as pinned; line 134 carries the verbatim label
  "Worked micro-example (NON-CANON — a demonstration, not a world decision)"; `:111` = DR-TK-3
  ("Fix the **smallest named unit**…"), `:112` = DR-TK-4 (public time source), `:113` = DR-TK-5
  (night regime/curfew) — exactly the two uncited-payload (F2) and one unanchored (F1) findings
  the entry files against that paragraph. The demonstration's line-level claims are accurate.
- All 31 exemplar `path:line` anchors in the §2 class table and the near-miss list resolve with
  the claimed shapes (spot-checked every one, including `historical-linguistics.md:55` "Grimm and
  Verner as worked examples" and the twelve distinct example-heading forms).
- Couples: 12 distinct `.md` tokens, **0 unresolved** under the r19 resolution order. The entry's
  "24/24 targets resolve" counts occurrences, not distinct tokens (12 distinct) — the substantive
  claim (nothing dangling) holds; R01-11 records the counting-unit nit.
- Literature legs (Sweller; Sweller & Cooper; Renkl; DeMillo/Lipton/Sayward; Hamlet) are carried
  `(to-verify)` with no fabricated page/DOI — the honest no-network shape.

### 2.2 C02 — index-sweep-verification (`reports/round-39/cov/C02-entry-2.md`)

- **Staged digest reproduces byte-exact**: extracting the fenced block with the round-35 stager
  regex `^```(?:markdown|md)\s*$([\s\S]*?)^```\s*$` gives 19,745 bytes,
  sha256 `eabb1d63ddc66b7c6c4c2767078aa3072cc44b1a90d290a67946f3f97481c174` — equal to the
  fragment's pinned value (a naive awk extraction gives 19,744 bytes; the pin is the stager-shape
  digest, as declared).
- Instrument claims verified: `sha256sum reports/round-28/readme/sweep.py` →
  `9b2ccac0046831fdaf48863ccd0ff6ca0fa390d044746c876e83a71c06f0cdd3`, 17,117 bytes;
  `--selftest` → "12/12 checks passed" (`:419`); r27 selftest "9/9" (`:314`); r27 ok-gate has no
  footer term (`:133`) while r28's includes `footer_findings` (`:191-194`) — the entry's central
  r27→r28 leg story is true in the code.
- README anchors verified: rev 1.8 stale-footer defect record (`corpus/README.md:43-55`),
  rev 1.5 paraphrase-rows repair (`:95-101`), the "dated record it was" line (`:52`), totals line
  (`:505`), counts footer (`:507-510`); `reports/round-19/audit/x27-coverage-readme-vs-files.md`
  `:47-49`, `:83-86`, `:132-136`, `:140-142`; `reports/round-20/readme/verify.md` `:21-30`,
  `:63-74`; `two-reader-interop-agreement.md:13` (Reproducible Builds).
- R01-8 (minor): the self-audit claims it "replicated round-19 entry-audit regexes
  (`entry-audit.py:25-31`)" yet reports `header_fields: ['Boundary', …]` — impossible under the
  filed `HEADER_RE` (`^- (topic|sources|couples|source|verified-at|recheck|status|gap):`,
  lowercase fixed alternatives; verified this seat). The inline replication was a variant, and
  its provenance label is inexact. The audit's conclusions (required fields present, tail ok,
  gap/decision matched) are unaffected under either regex; **C05 must audit with the filed
  instrument bytes, not C02's inline replication.**

### 2.3 C03 — contact-strata-verification-gate (`reports/round-39/cov/C03-entry-3.md`)

- **7/7 source digest pins match** (recomputed this seat): `verification-method-overview.md`
  `f52708d9…`, `language-contact.md` `52385e3d…`, `historical-linguistics.md` `019f28f0…`,
  `loanword-material-dating.md` `5b1d75ab…`, `contact-scenario-builder.md` `fcc71a53…`,
  `multi-culture-creole-workshop.md` `62acbaae…`, `internal-consistency-audit.md` `c3118517…`
  (full digests in the fragment's §5; all equal).
- **All five absence-sweep numbers reproduce exactly** against the clean tree: loan/contact
  strata → **19** files with exactly **1** in-partition hit (`calibration-registry.md`, the
  replacement-sequence row); gate/audit terms → **0**; strata|stratum in verification → **8**;
  contact in verification → **11**. (See R01-14 for one unreproducible anomaly in my own first
  measurement pass — resolved in C03's favor; filed against no seat.)
- Staged digest reproduces: fence extraction → 33,526 bytes, sha256
  `3fa037ae9f95de7449f4df937ed2ef0871bd85d75194c15f79c76053df3c841f`, equal to the fragment's pin.
- Cited lines verified: `language-contact.md:81` ("The adaptation freezes the donor's phonology…
  the hinge of stratigraphy"), `:45` ("tendencies, not laws"), `:53`; `historical-linguistics.md`
  `:143-145` (relative chronology as the spine); `overview:16` (manual craft-verification
  specification), `:99` (release rule); `calibration-registry.md:71`; `myth-consistency-gate.md:104`;
  `lexicon-coverage-audit.md:116` ("## 6. L — Loanword-layer coherence");
  `contact-scenario-builder.md:63`, `:158` (staged repairs), `:184` (the /sipa/ year-20 rejection);
  `examples/culture-d3/handoff.md:111` ("no real-language derivation, borrowing") and
  `examples/culture-d3/components/07-evidence.json:46`. The §12 worked reading is a faithful
  reading of the builder's declared L1–L4/C1–C4 rows.
- Topic authority is the cleanest in the wave: it is K01's G1 verbatim, claimed after K01 landed,
  with sibling disjointness asserted from landed fragments. External works are cited only at
  their in-corpus registrations with "Not consulted this round" — no invented bibliography.
- No defects filed.

### 2.4 C04 — append-only-record-verification (`reports/round-39/cov/C04-entry-4.md`)

- Absence sweeps reproduce: "closing snapshot" → **0**; "could-not-recover" → **0**;
  close-digest variants → **0**; "append-only" → **12** files. All as quoted in `- gap filled:`.
- Anchors verified: `AGENTS.md:32-39` (close-what-you-open, `could-not-recover`, SHA-256-at-close —
  grep-located at `:32`,`:36`,`:38`); `provenance-audit-ledger-format.md` §8 items 6/10 including
  the verbatim "A digest printed from a mutable file alone detects no drift";
  `verification-independence-anti-circularity.md:61` (replay-tool surface) and `:144` (IND-6,
  anchor lives outside); `header-conformance-readings.md:22` (repair vs correction);
  `two-reader-interop-agreement.md:50`, `:77`; `corpus/README.md:43-61`, `:96-99`, `:505-518`;
  `reports/round-20/readme/gaps.md:18-20`, `:54-57` (the r5/r6 in-place-edit incident);
  `reports/round-39/telemetry/dispatch-declared.json:25` (the live open record — exact);
  `tools/replay-frozen.py` exists; `hold-set-contract-in-brief.md:77`,
  `generated-artifact-lifecycle.md:81`, `finding-disposition-workflow.md:60`;
  `gate-frozen-run-standard.md:15` (the glob-fragment couples line).
- `reports/round-37/calib/recount-ledger.json:68,81,94,107` are exactly the four
  `could-not-reproduce` disposition lines (verified against the file I read in full).
- R01-9 (minor): the §Self-audit pins only the **pre-reword** staged size (24,277 bytes); the
  filed bytes are post-reword. My extraction of the current fence: 24,297 bytes, sha256
  `31cf12f028c08eaf79e77c605ba615990c4a2c69c8d3cf770b44da45852909fd`. Mitigated: C06 §6 pins the
  current whole-fragment digest (`94348f96…`) and it matches the live file — the chain is intact;
  the entry fragment itself just does not carry its own final staged digest.

### 2.5 Cross-entry checks

- **No collisions**: four distinct slugs (`worked-example-verification`,
  `index-sweep-verification`, `contact-strata-verification-gate`,
  `append-only-record-verification`), none in the existing 20; topics disjoint (C03's §1 asserts
  it from landed fragments; I confirm the four names/topics do not overlap).
- **Fence-shape heterogeneity (R01-10, note)**: C01 and C03 wrap entries in 4-backtick fences,
  C02/C04 in ` ```markdown `. The round-35 stager regex only matches the 3-backtick shape; the
  integrator's staging step (and C05's tooling) must handle both shapes or extraction will
  silently skip two of the four drafts.
- **R01-11 (note)**: C01 has no head-block `- calibration:` field (its calibration clause is body
  §8); C02/C03/C04 carry the field. The executable bar (r19: topic/sources/couples + tail) does
  not require it, so this is a checklist note for C05's reading, not a defect.
- **R01-4 (major, gate)**: `reports/round-39/cov/C05-audit.md` does not exist at this review's
  close (polled repeatedly through the wave; last poll shows `cov/` = C01,C02,C03,C04,C06 only).
  Claim C's own threshold — "entries audited before landing" (`claims.json:16,18`) — is therefore
  **unmet** at review time. My fabrication hunt is not the audit: the filed instrument run
  (families 1–6, source-pointer resolution, bleed reads) has not been executed by its assigned
  seat on the final four drafts. The integrator must not apply the entries until C05 lands (or
  its absence is recorded with owner and reason in the round record).

## 3. Protocol soundness (claim Ca)

### 3.1 The hazard, verified from filed bytes

The O12 mechanics are exactly as the Ca fragments state: r34/r35/r36/r37/r38 runners all carry
`ROOT = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"` + module-level `os.chdir(ROOT)`
(verified: r34 `:10,:26`; r35 `:9,:36`; r36 `:8,:13`; r37 `:5,:10`; r38 `:5,:13`), while r33 is
relocatable (`:23`). `--check` is parsed only after `measure()` (r34 `:522-531`), so an escaped
`--check` measures the live tree; publish mode writes `{ROUND}/validation.json` relative to the
chdir'd root, and `receipt_guard` refuses committed receipts unless `REFRESH_RECEIPTS=1`
(`tools/harness/receipt_guard.py:144-149`), strips every `GIT_*` env var from its git subprocesses
(`:48-51`), and uses a 15 s git timeout (`:55`) — all four guard claims in Ca01's §5 verified
against the file. The four c-n-r rows are `recount-ledger.json:60-111` (R37-Ca-05..08), summary
`"could-not-reproduce": 4` at `:451-455`.

### 3.2 Ca01's protocol (`reports/round-39/calib/Ca01-protocol.md`) — sound core, four findings

The three-tier design is right: Tier A (shared clone + bwrap bind **at the canonical live path**
+ in-namespace alternates rewrite) is the only mechanism that makes the hardcoded ROOT resolve
into the snapshot on unmodified bytes; the Annex A.0 discovery that a linked worktree's `.git`
pointer breaks under the bind (`fatal: not a git repository: (null)`) is a real, decisive finding
— it refutes the naive "worktree + bind" reading of the shared rules that X00-2 and K02 §4.1
both circled; Tier C (rewrite-on-copy) is correctly demoted to non-reproduction evidence. The
integrity triple-check (§3) and disposition vocabulary with named delta classes (§9) are the
right discipline, and the worked values (runner `be11ff46…`, receipt `ba2fa4dc…`) match what
K02 and I measured independently.

- **R01-2 (major — scope)**: the protocol's hazard section names **three** absolute runners
  (r34/r35/r36). The measured set is **five** (S01 §3.2; each ROOT/chdir line verified by this
  seat). r37 and r38 re-carried the O12 shape even though r38's own record rules "copy the r33
  relative-ROOT shape, never the r34/r35 absolute os.chdir shape"
  (`reports/round-38/cross/X01-trades.md:367-369`). The durable protocol text must name all five
  (or scope itself to "any runner whose pre-flight §4 finds an absolute ROOT" — which its own
  §4 already implies; make it explicit), and the round record should note the streak: the
  successor-runner requirement has been stated since r38 and not yet honored by two successive
  runners.
- **R01-3 (major — hardening)**: Tier B (worktree + sitecustomize chdir shim) has **no
  discriminating wrong-tree observable**. If `PYTHONPATH` is not honored or the shim fails to
  import, the unmodified runner chdirs to the live tree and `--check` silently measures it —
  the exact failure that produced the r37 c-n-r rows, now undetectable. P01's own plan demanded
  a discriminator ("a replay whose observable matches the live tree is **void**",
  `reports/round-39/plan/P01-plan.md:182-183`), and Ca02's evidence shows the discriminator
  exists in practice (escaped Run 1: O2 inventory 33 runners at the live tree; contained Run 2:
  green at the close-time 29 — `reports/round-34/validation.json:53-65` region). Require, in the
  protocol text for Tiers A **and** B, one recorded post-run tree-discriminator (the O2-style
  close-time-count comparison or an equivalent path-count probe), without which the replay is
  void. Annex A.3's "equals tierA modulo clock" check is an after-the-fact instance; write it
  into the recipe.
- **R01-5 (minor — declared deviation)**: Tier A's substrate is a shared **clone**, not a
  worktree, while `targets.json` shared_rules say "the Ca protocol work uses git worktrees at
  close commits only". Ca01 documents why (A.0) and preserves the rule's intent (close-commit
  tree, shared objects, zero byte edits, zero commits). The integrator should record this as a
  declared deviation with its rationale — not absorb it silently.
- **R01-6 (minor — precision)**: §5's T3 containment probe ends in `… or True`, making the assert
  vacuous as written (the real containment evidence is the bind plus T1/T2 and the measured-tree
  discriminator of R01-3 — tighten or delete the line). §3's chain-table line numbers are off by
  one or two (r34 `BASELINE_FULL` is at `run-validation.py:14`, not `:12`; r35 `:13`, not `:12`;
  r36 `:12`, not `:11` — all three verified). The commit values themselves are correct.

### 3.3 Ca02's replay (`reports/round-39/calib/Ca02-replay-verify.md`) — strong evidence, one real conflict

The evidence quality is high and honestly bounded: worktree pinned at `4a7aede`; pristine/copy
digests recorded (`be11ff46…` / `46e55b80…`, diff `10c10`); `--check` only; TMPDIR isolated; the
replayed receipt normalized-IDENTICAL to the filed receipt minus `measured_at_utc` and the X1-X3
pending-manifest note (both explained, the latter against the live MANIFEST which now carries
exactly one r34 row); `input_sha256` (10 inputs) byte-equal; the escape demonstrated as a
negative control (one live-tree scratch probe, removed, `git status` verified). The O2 contrast
between Run 1 (33 runners, live) and Run 2 (green, close-time 29) is the tree discriminator —
see R01-3. Fidelity limits (fleet inputs read as-current; mtime-only evidence for the r34 fleet
report, digest equality `to-verify`) are stated rather than hidden.

- **R01-1 (major — the round's top finding; the successor ledger must resolve it explicitly)**:
  the counted Run 2 **altered the executed bytes** (`ROOT = os.getcwd()`), and is dispositioned
  `reproduced-under-protocol`. Ca01's own protocol classes a rewrite-on-copy run as Tier C, which
  "does **not** satisfy `reproduced-under-protocol`" (§7), and filed r37 precedent excluded
  exactly this shape from recounts ("a scratch-only, altered-source diagnostic … is **not**
  counted as a recount", `reports/round-37/calib/Ca02-r34.md:20`; P01 r37 plan `:19-24`).
  Against that, `claims.json:21` declares a "relative-root requirement" as **part of the
  protocol**, which is most naturally read as sanctioning precisely this adaptation, and Ca02
  ran before Ca01's document existed (declared in its Owed). Both readings are defensible; the
  conflict is real and must not be papered over by a green verdict. Required action, consistent
  with S01 §6.3 leg Ca5 (which names this review as the adversarial input): the successor ledger
  must (a) name the mechanism that actually ran — digest-pinned one-line adapted copy — beside
  the disposition, and (b) record the integrator's ruling. Cleanest closure: one independent
  Tier A or Tier B re-run (~minutes; Ca01 Annex A.1/A.3 already shows both produce the identical
  receipt modulo clock, but Annex A is author-side, not the independent seat), after which
  `reproduced-under-protocol` rests on unmodified bytes. Alternatively the integrator rules that
  the claims-declared relative-root requirement makes the digest-pinned adaptation
  protocol-conformant — that ruling must then be written into the protocol text, not just the
  ledger. Either way: no unqualified `reproduced-under-protocol` on the Tier-C run as it stands.
- Minor (no id): the negative control wrote one scratch probe into the live tree's `.scratch`
  (removed, declared). The protocol should carry this as a known bounded side effect of escape
  demonstrations so a future seat does not discover it as a surprise.

### 3.4 Ca03's policy + Ca04's verification — verified; adopt the two one-line fixes

- I re-ran Ca03's §6 script byte-exact (extracted from the fragment's fence): Part 1
  `refs=334 → direct=319 fallback=15 ambiguous=0 unresolved=0`, RESULT `PASS (334=319+15, …)`;
  Part 1b 15/15 OK, `misaligned=0` (7 linguistics / 6 culture-material / 1 verification /
  1 synthesis); Part 2 `entries=212 refs=2504 → direct=2335 fallback=163 ambiguous=0
  unresolved=6`, 5 distinct exactly as quoted; Part 3 slash-gate delta demonstrated
  (`linguistics/hero-journey-variants.md` → policy `unresolved`, C14-as-written `fallback`).
  Every number in the filed summary reproduces.
- The declared C14 narrowing is real in the code: `reports/round-35/cov/C14-audit-6-10.md:281`
  keys `basename(ref)` for any Tier-1-unresolved token, slash-bearing included; Ca04's r27
  precedent for the narrowing (`reports/round-27/audit/entry-audit.py:129-131`, slash-free-only
  partition loop) verified.
- Ca04's **D1 verified live by this seat**: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
  is the corpus's one wrapped couples field; of its four named sibling files exactly
  `sound-symbolism.md` and `writing-systems.md` exist, `sound-change.md` and `tone-prosody.md`
  do not — the single-line extractor captures 0 tokens there. **R01-7 (minor)**: adopt D1 and D2
  at landing (Ca04's one-sentence fixes: block extraction or named exception; the C12-row-2
  blocker/`(to-verify` disposition mapping for `unresolved` couples tokens). Ca04's gate
  observation also reproduces: `python3 -B reports/round-19/audit/entry-audit.py
  corpus/knowledge/myth-symbol/sacred-kingship-mythic-charter.md` → FAIL 0/1, 15 unresolved,
  exit 2 (verified, exit code measured without a pipeline).
- **R01-7 also carries**: Ca03's Part-2 attribution for the phantom is incomplete —
  `../linguistics/phonology-sanity.md` (x2) lives in **two** fields:
  `verification/label-channel-routing-verification.md:14` (named) and
  `synthesis/typed-label-routing-workflow.md:16` (unnamed). One-line fix at landing.

## 4. Other cross-block findings

- **R01-12 (note — K01 precision)**: K01 §3's sweep table cites `grep -lic <term>` and reports
  counts; as written that flag combination prints filenames, not counts (verified). Re-measuring
  with `-li | wc -l`: loanword 4 ✓, euphemism 4 ✓, dialect 6 ✓, "translation note" 0 ✓ — but
  **taboo = 10**, not the reported 9 (the extra file:
  `verification/verification-independence-anti-circularity.md`; all ten hits are incidental —
  the conclusion "no dedicated taboo entry" stands). K01's git add-history and all six
  registered-source citations verified exactly (caf1bea / 94ca098 / c610e0a / 49ac1a5; T&K 1988,
  Haspelmath & Tadmor 2009, Durkin 2014, Allan & Burridge 2006, Chambers & Trudgill 1998,
  Siegel 1985, Appiah 1993, Campbell/Ferguson/Fishman — all present at the cited lines with the
  claimed DOIs/editions), and overview anchors `:73,:88,:114,:118,:150` all read as claimed.
- **R01-13 (note)**: K01's G2 (taboo), G3 (dialect/register), G4 (translation fidelity) remain
  unallocated — C03 took G1, the other three executors self-derived off-list topics before K01
  landed (P01's declared self-derive rule; C06 §6 and S01 §2.4 already record the deviation).
  Carry G2–G4 on the partition's gap list; not a defect.
- **R01-14 (honesty note, filed against no seat)**: in one intermediate measurement pass this
  seat's own sweep commands returned counts exactly +2 over the clean-tree values (21/3/2/10/13
  vs C03's 19/1/0/8/11). Minutes later, against the verified-clean tree (0 dirty corpus rows,
  20 verification files, 212 total, README `b80274bc…`), every C03 number reproduced exactly and
  the +2 readings could not be reproduced. I have no durable artifact of any tree state containing
  extra files and no attribution; per the lane's rules this is recorded as an unreproduced
  reviewer-side observation and **no defect is filed against any seat**. If the integrator wants
  it chased, the only durable handle is this fragment and the timestamps of my tool calls.
- Consistency checks that passed silently: C06's three fragment digest pins match the live bytes
  (C01 `91ba710d…`, C02 `788af6bc…`, C04 `94348f96…` — no post-C06 amendments); C06's README line
  map is correct (`:258` header, `:260-279` rows, `:505` totals, `:509` footer, duplicated H1 at
  `:1,:3` and duplicated rev-2.0 line at `:14,:16` — carried defects correctly inserted-around);
  C06's §8.1 negative control honestly reads RED at the before state; S01's §3.1 convergence
  table matches my independent readings on every row I checked; S01's dispatch-honesty section
  correctly keeps observed counters `null` with owner rather than inferring zeroes.

## 5. Required integrator actions (ordered)

1. **R01-4**: obtain C05's audit (or record its absence with owner+reason) before applying any
   entry; the audit must run the filed instrument bytes on all four final drafts, both fence
   shapes (R01-10).
2. **R01-1**: in the successor ledger, record the replay mechanism actually used beside each
   disposition and the explicit ruling on adapted-copy vs unmodified-source
   (S01 leg Ca5); prefer one independent Tier A/B re-run; cite the canonical queue id
   `O12-runner-isolation-hazard` once (X00-4) and carry Ca08's C/D namespace evidence forward.
3. **R01-2/R01-3**: before the protocol lands at `calib/isolation-replay-protocol.md`, amend
   Ca01: scope the hazard to all five absolute runners (or to the §4 pre-flight class), and add
   the mandatory post-run tree-discriminator to Tiers A and B; fix R01-6's vacuous assert and
   line nits in the same pass.
4. **R01-7**: apply Ca04's D1+D2 one-liners (or queue them to the successor instrument with an
   explicit recorded choice) and complete the phantom's second-carrier attribution.
5. **R01-5**: record the Tier A clone-vs-worktree substrate as a declared deviation with A.0 as
   rationale.
6. R01-8/9/11/12: fold as notes into C05's audit record and the landing receipts; none blocks.

## Owed

- `reports/round-39/cov/C05-audit.md` — never landed (R01-4). Owner: C05/integrator. My §2 hunt
  is evidence toward it, not a substitute for the filed instrument run.
- `reports/round-39/calib/isolation-replay-protocol.md` and
  `reports/round-39/calib/basename-couples-policy.md` — canonical copies of Ca01/Ca03 are
  integrator-owned (digest-pinned), with R01-2/3/6 and D1/D2 folded or queued.
- The successor recount ledger re-dispositioning R37-Ca-05..08 — integrator-owned, per R01-1.
- `to-verify` (R01-14): the transient +2 sweep anomaly, if the integrator chooses to chase it.
- This seat certifies neither claim; admission stays the integrator's per `REGIMEN.md:41-43`.

## Citations

- Contract: `reports/round-39/targets.json` seat R01 + shared_rules; `reports/round-39/claims.json:13-27`.
- Runners/guard (read, never executed): `reports/round-33/run-validation.py:23`;
  `reports/round-34/run-validation.py:10,14,21-22,26,522-538`; `reports/round-35/run-validation.py:9,13,36`;
  `reports/round-36/run-validation.py:8,12-13`; `reports/round-37/run-validation.py:5,10`;
  `reports/round-38/run-validation.py:5,13`; `tools/harness/receipt_guard.py:48-51,55,144-149`.
- r37 record: `reports/round-37/calib/recount-ledger.json:60-111,451-455`;
  `reports/round-37/calib/Ca02-r34.md:18-20`; `reports/round-37/plan/P01-ca-plan.md:19-24`;
  `reports/round-37/op/defect-queue.json:192-211`; `reports/round-37/adj/A12-gap-fill.md:9-26`.
- Peer fragments under review (all read in full): `reports/round-39/{scout/K01-verification-gaps.md,
  scout/K02-isolation.md, plan/P01-plan.md, cov/C01-entry-1.md, cov/C02-entry-2.md,
  cov/C03-entry-3.md, cov/C04-entry-4.md, cov/C06-delta-receipt.md, calib/Ca01-protocol.md,
  calib/Ca02-replay-verify.md, calib/Ca03-basename-policy.md, calib/Ca04-verify.md,
  cross/X00-connector.md, scribe/S01-integration-draft.md}`.
- Corpus/anchors verified (spot-checks quoted in §2): `corpus/knowledge/culture-material/timekeeping-instruments.md:31,55,109-113,134` (+ sha16 `9805c0b854334ed3`);
  `corpus/knowledge/linguistics/{language-contact.md:7,45,53,81, historical-linguistics.md:55,143-145}`;
  `corpus/knowledge/verification/{verification-method-overview.md:16,51,54,73,88,99,114,118,150,161,166,
  calibration-registry.md:71, myth-consistency-gate.md:104, lexicon-coverage-audit.md:116,
  label-channel-routing-verification.md:14, internal-consistency-audit.md:168,
  gate-frozen-run-standard.md:15,144, header-conformance-readings.md:22,
  verification-independence-anti-circularity.md:61,144, provenance-audit-ledger-format.md:140-155,
  two-reader-interop-agreement.md:13,50,77}`;
  `corpus/knowledge/synthesis/{contact-scenario-builder.md:63,158,184, multi-culture-creole-workshop.md:98-119,
  loanword-material-dating.md:3-23, hold-set-contract-in-brief.md:77, generated-artifact-lifecycle.md:81,
  finding-disposition-workflow.md:60, taboo-euphemism-lifecycle.md:5, dialect-faction-map-workflow.md:4,
  urban-rural-register-ecology.md:5, cultural-translation-protocol.md:4, era-language-staging.md:4,
  typed-label-routing-workflow.md:16}`;
  `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`;
  `corpus/README.md:1,3,5-12,14,16,43-61,52,95-101,258,260-279,505-518`;
  `AGENTS.md:5-6,18-25,32-39`; `examples/culture-d3/handoff.md:111`;
  `examples/culture-d3/components/07-evidence.json:46`; `reports/round-39/telemetry/dispatch-declared.json:25`;
  `reports/round-20/readme/{gaps.md:18-20,54-57, verify.md:21-30,63-74}`;
  `reports/round-19/audit/{entry-audit.py:25-31,74-96, x27-coverage-readme-vs-files.md:47-49,83-86,132-136,140-142}`;
  `reports/round-27/audit/entry-audit.py:129-131`; `reports/round-27/readme/sweep.py:133,314`;
  `reports/round-28/readme/sweep.py` (sha `9b2ccac0…`, 17,117 bytes; `:191-194,345-380,419`, selftest 12/12);
  `reports/round-35/cov/{C14-audit-6-10.md:227-236,249-288, C12-audit-runbook.md}`;
  `reports/round-37/calib/Ca08-verify.md:23-27,32`.
- Commands run by this seat (all quoted outputs above): the C01/C02/C03/C04 sweep batteries;
  sha256 over 7 C03 source files + 3 entry fragments + 2 staged extractions + r28 instrument;
  fence extraction + stager-regex digest recomputation (C02 `eabb1d63…`, C03 `3fa037ae…`);
  the r19/r27/r28 instrument selftests and the sacred-kingship gate rerun (FAIL 0/1, exit 2);
  Ca03's §6 script byte-exact rerun (Part 1/1b/2/3 outputs as quoted);
  `git log --diff-filter=A` verification add-history; `git status --porcelain` (wave-scoped);
  corpus cleanliness triple-check at review close. No filed byte touched; no runner executed;
  no network; no installs.
