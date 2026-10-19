# R02 — second non-author review (round 44, cross-claim)

- **Seat:** `R02` — reviewer, claim `cross` (`reports/round-44/targets.json` seat `R02`).
- **Mission:** independent read of the three claims' landed evidence; focus on whether any axis is harmed — does the successor fork or shadow the r42 extractor, does C land a duplicate or overwrite, does the freshness gate actually catch a stale `before`. Per-axis verdict + named findings.
- **Baseline:** `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d` (`git rev-parse HEAD` at cut → `c9f4eaa`).
- **Review cut:** `2026-10-19T17:33:08Z` (UTC), final read of the C-seat bytes. Later seat landings are noted in §8; this file's verdicts are for the cut. R01 filed at 17:30Z and independently reached the same O/C verdicts and the same C conflict; §3 notes the agreement (and the one label difference on Ca).
- **Writes:** this file only. All probes under `.scratch/r02-*`. No corpus/tool/filed byte was edited; `git status --porcelain` at cut shows only `?? reports/round-44/`.
- **Method:** every headline number below was re-run by this seat from primary sources (byte extraction, tool runs, git object reads, per-entry folds). Where I rely on a sibling seat's measurement I say so and name the file:line. No in-tree `run-validation.py` was executed; none exists at cut.

---

## 0. Verdict summary

| Axis | Verdict at cut | Why |
|---|---|---|
| **Operability (O)** | **`unprovable-but-better`** | The r43 O09 body is byte-exact and green in isolation (27/27; 223/2730; `2556+166+0+7=2729` +1 glob), and its parity with the r42 witness is 0 unexplained diffs. But the claim's durable path `tools/harness/basename-couples-resolver.py` does **not** exist at cut, and the census artifact is **not** filed (`reports/round-44/calib/` empty). A scratch run is evidence about the body, not about the lane. **`improved` on a verified apply**; nothing observed **harms** the axis. |
| **Coverage (C)** | **`unchanged`** at cut | No corpus byte moved; 223 entries, sweep green 223==223. The current draft (`cov/C01-entry-draft.md:108-395`, 286 lines) is technically sound on the checks I ran (16/16 path anchors resolve, 15/15 couples tokens direct, no duplicate/overwrite), but there is **no C02 README, no C03 source audit, no C04 contract audit, and no landing** at cut. **`improved` only if one gap lands with the audits**; **`harmed` if both competing gaps land or an existing entry changes**. |
| **Calibration (Ca)** | **`unprovable-but-better`** | The pre-dispatch gate draft correctly refuses the r43 claims (`STALE O`, `STALE C`, `FRESH Ca`, exit 2 + REFUSE line) and its declared-probe path distinguishes true from false counts. But it is **only in `.scratch`** at cut, its `--selftest` is **red (17/19)**, and one novel-phrasing test false-positives. **`improved` on a durable, selftest-green apply**; no harm observed (read-only, no filed-byte edit). |
| Depth / adjacency / freshness | `unchanged` | Not claimed this round; `freshness_pause_in_force: true`. No packet/canon surface touched (`git status --porcelain corpus tools examples` empty; packet pins remain A01's leg, which I did not re-adjudicate). |

**Bottom line:** no axis is harmed by anything on disk at the cut. The two blocking gaps are
delivery, not damage: O's authority/census are drafted but unlanded; C's chain is split across
two competing unowned gaps and has no audits/README/landing; Ca's gate is a working scratch
prototype with a red selftest. The C candidate conflict (§3) is the most consequential finding:
the drafted entry serves the r42-carried dream/trance proposal, while the claim-named scout K02
selected a different, non-carried gap (cartography) and explicitly rejected dream as carried.

---

## 1. Independent measurement ledger

All commands from the lane root with `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`.

### 1.1 Claim O — the body, the census, the witness

Extraction (fence `:355`…`:871`; body `:356-870` = 515 lines):

```
$ sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/r02-o09/basename-couples-resolver.py
$ sha256sum .scratch/r02-o09/basename-couples-resolver.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64
$ wc -l .scratch/r02-o09/basename-couples-resolver.py
515
```

The digest equals `claims.json`'s `43ce341f…` and O09's own pin. The r43 source file digest is
`956d478bfe7abbaac6598a0d272a7cb524e3d2bc7fa70cc27be41b538e0cb341` (unchanged, read-only).

Body runs from a scratch directory whose only `corpus/knowledge` ancestor is the real repo:

```
$ cd .scratch/r02-o09 && python3 -B basename-couples-resolver.py --selftest
SELFTEST OK: 27/27 controls          # exit 0
$ python3 -B basename-couples-resolver.py --census
entries=223 refs=2730
  policy four-class: direct=2556 fallback=166 ambiguous=0 unresolved=7
  artifacts (excluded from the four-class totals): glob-fragment=1
  conservation: True (sum=2730 refs=2730)
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  fallback mappings (50 distinct): … 50 rows …
  unresolved (7 rows): … 5 declared-prospective-seed + 2 dangling-reference …
  ambiguous (0 rows):
  glob-fragment (1 rows): -gate.md … extractor-artifact c12=not-applicable
  misaligned: none
exit 0
```

Independent fold from the JSON `entries_detail` (not trusting the tool's totals):

```
entries_detail records        223
sum(len(tokens))              2730
class fold                    {'direct': 2556, 'fallback': 166,
                               'unresolved': 7, 'glob-fragment': 1}
fallback occurrences          166   (50 distinct mappings)
tool totals match the fold    True (direct/fallback/unresolved/glob)
```

Every fallback target exists on disk (50/50). Every unresolved reason is true:

- the five `declared-prospective-seed` tokens (`honorifics-and-register.md`,
  `naming-and-onomastics.md`, `phonology-basics.md`, `sound-change.md`, `tone-prosody.md`) have
  **zero** files anywhere under `corpus/knowledge/`;
- the two `dangling-reference` rows point at `../linguistics/phonology-sanity.md`, which does
  **not** exist;
- the single glob artifact traces to a real glob in `verification/gate-frozen-run-standard.md:15`
  (`corpus/knowledge/verification/*-gate.md`).

Wrapped field, identity not arity: `phonetics-phonology.md:72-77` yields exactly
`{sound-change.md, sound-symbolism.md, tone-prosody.md, writing-systems.md}` (4/4), no
`prosody.md`, no `toneprosody.md`. My per-entry run reproduced the same four.

**Blank-line fix, independently reproduced** (not just read from O03):

```
live r42 couples_block(fixture) -> ['method — `writing-systems.md`',
                                    'Indented body prose names `sound-symbolism.md` and `tone-prosody.md`.']
new  O09 couples_block(fixture) -> ['method — `writing-systems.md`']
live refs  -> ['sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']   (3, over-capture)
new  refs  -> ['writing-systems.md']                                            (1)
```

**Witness census and bytes** (read-only, same 223/2730 input):

```
$ python3 -B tools/harness/couples-reference-extractor.py --census
entries=223 refs=2730 -> direct=2556 fallback=166 unresolved=2 prospective=5 glob-fragment=1
$ sha256sum tools/harness/couples-reference-extractor.py
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1
```

The six-class witness reconciles exactly: `2556+166+2+5+1 = 2556+166+0+7+1 = 2730`. The
successor's `0/7` is the witness's `2 unresolved + 5 prospective` folded into unresolved with a
named disposition. No token is added, dropped, or guessed.

**Shadow trap, reproduced by this seat:** `.scratch/o07/` is a full pre-existing repo snapshot
with 212 corpus entries. Running the same byte-identical resolver from inside it reads the
snapshot:

```
entries=212 refs=2508
  direct=2337 fallback=163 ambiguous=0 unresolved=7 +1 glob
```

At the claim path (`tools/harness/`), the upward root walk lands on the real lane root, so the
landed tool is correct. This is a run-location trap, not a body defect. X00 additionally measured
a corpus-only scratch root at `2536 direct / 27 unresolved` because 20 tokens resolve against
lane-root files (`AGENTS.md`, `SKILL.md`, `reports/…`); the default text output does **not** print
the resolved root (`cross/X00-connector.md:72-95`). Run discipline is therefore load-bearing for
every future census.

### 1.2 Claim C — live partition and the two candidate gaps

```
$ find corpus/knowledge -name '*.md' | wc -l
223
$ python3 -B reports/round-28/readme/sweep.py     # exit 0
rows 223 files 223; missing_from_index 0; topic_mismatch 0;
orphan_rows 0; totals_line 223 totals_ok True; footer_ok True
readme_sha256 7c788a1d4c29718f6d2df446125ee2516c1c76210792f11b5a81a001ef31cdcd
```

**Dream / vision / trance candidate** (`myth-symbol/dream-vision-trance.md`):

- filename sweep: no file in any partition matches `dream|trance|vision|ecsta|shaman|incubat`;
  the exact path is absent;
- topic-line sweep: exactly two hits, both adjacent —
  `myth-symbol/divination-omen-systems.md:3` names "dream-oracles and incubation" as one of
  fourteen technique rows, and `civilizations/mongol.md:3` uses "shamanic vocabulary" as
  civilization data. Neither owns the state/induction/career system;
- heading sweep: two hits — divination's H1 (same technique framing) and
  `civilizations/australia-aboriginal.md:36` (ancestral Dreaming/Tjukurpa, a different concept);
- sort position: `10 divination-omen-systems.md / 11 dream-vision-trance.md / 12 eschatology-world-end-systems.md`;
- demand: my broad union regex finds 59 files (K04's narrower union 52; C01's 61 — regex scope,
  not ownership).

**Cartography / mapmaking candidate** (`culture-material/cartography-and-mapmaking.md`), K02's
selection:

- filename sweep: 0 hits for `cartograph|mapmaking|portolan|cadastr`;
- topic-line sweep: 11 hits, all metaphor/verb/adjacent (e.g. "dialect map", "boundary map",
  "source map", "sacred-geography mapping") and none owns map production;
- exact path absent; sort position `5 calendar-festival-systems.md / 6 cartography-and-mapmaking.md / 7 costume-semiotics.md`.

Both candidates are genuinely unowned at the topic level. They differ in **prior-round carriage**
(§3).

**The dream draft, mechanically checked** (current bytes, extracted from `cov/C01-entry-draft.md:108-395`,
286 lines / 55,575 bytes):

- 16 distinct `corpus/knowledge/...md` path references; **all 16 exist**, all cited line numbers
  and ranges are **in range**; all bare `.md` basenames resolve;
- `- topic:` is a single line (README row can be byte-equal);
- the `- couples:` block yields **15 distinct tokens, all `direct`**, zero unresolved/fallback;
  therefore a lawful landing would make the post-C census `entries=224 refs=2745 direct=2571`
  with the other classes unchanged (the tool dedupes per entry; I ran the successor's `--json`
  on the extracted draft to get this);
- no assertive canon wording, no "should work / might / presumably / obviously / assume" wording;
- it does **not** couple to `phonetics-phonology.md`, so the successor's corpus-coupled S1a
  control stays green after the landing.

### 1.3 Claim Ca — the gate draft run over r43 and over synthetic claims

The only gate on disk at cut is `.scratch/ca01/claims-freshness.py` (not durable). I ran it
read-only:

```
$ python3 -B .scratch/ca01/claims-freshness.py --claims reports/round-43/claims.json
[O]  operability -- STALE (0/2 premises hold)     # E1a + E1b both false at 7ceff59
[C]  coverage   -- STALE (2/3 premises hold)      # myth-symbol 26 + total 223 true; "lithic slot unbuilt" false
[Ca] calibration-- FRESH (1/1 premises hold)      # no disposition artifact at 7ceff59
summary: 1 fresh, 2 stale, 0 unverifiable, 2 ungrounded
REFUSE: claims O, C have a `before` already false at 7ceff59…; do not dispatch.
exit 2
```

That is the claim's required positive regression (O and C flagged) plus its negative control
(r43 Ca, a true `before`, not flagged). The gate reads the baseline commit through git plumbing,
not the worktree, and writes only stdout.

Synthetic probes I added (`.scratch/r02-ca/synthetic.json`, baseline `c9f4eaa`):

| claim | `before` | result | correct? |
|---|---|---|---|
| A | "corpus total 223 at the baseline" | FRESH | yes (negative control) |
| B | "corpus total 999 at the baseline" | STALE | yes |
| C | declared probe `count_eq 999` | STALE | yes |
| D | declared probe `count_eq 223` | FRESH | yes |
| E | "the llama-herding register slot is unbuilt" | **STALE** (topic mined as `register`; 51 "owners") | **no — false positive** |
| F | "everything is in order" | UNVERIFIABLE (refused) | yes |

The gate's own `--selftest` is **red**:

```
ok    path_absent missing passes
…
FAIL  grep_absent hit fails
ok    grep_absent hit fails (partition scan)
…
FAIL  seventeen checks collected (18)
selftest 17/19 FAIL          # exit 1
```

The production partition-scan variant of `grep_absent` passes; the failing one uses a synthetic
`corpus/knowledge/beta/*.md` fixture, so this looks like a fixture bug rather than a broken probe.
The second failure is a stale count assertion (18 checks ran, the assertion expects 17). Either
way, a red selftest is not a shippable gate without a named disposition.

### 1.4 Integrity

```
$ git rev-parse --short HEAD                 c9f4eaa
$ git status --porcelain                     ?? reports/round-44/          (only)
$ git status --porcelain corpus tools reports/round-1* reports/round-2* \
      reports/round-3* reports/round-4[0-3]   (no output)
$ find corpus/knowledge -name '*.md' | wc -l 223
$ sha256sum tools/harness/couples-reference-extractor.py
d8d23a265d12d290de69a6eb50454273af4ca699986812c6e203a030f4679cf1
```

No filed byte was edited; no corpus/tool delta exists at cut. The r42 witness bytes are unchanged
from the r43 baseline (`git show 7ceff59:…` gives the same digest).

---

## 2. Claim O — does the successor fork or shadow the witness?

**Verdict: no fork, no shadow, no overwrite; the axis is not harmed. Delivery is incomplete at cut.**

### 2.1 What the successor actually does to the witness

- **Not imported, not shelled out.** The body imports stdlib only and never executes the witness.
  The only occurrence of the witness path is the docstring line that names it the N6 witness.
- **Bytes frozen.** `d8d23a26…` before and after every seat run I made; the witness's mtime
  predates the round.
- **Parity is token-level, not totals-level.** O07 compared 2730/2730 token rows with 0 class
  shifts after the documented `prospective → unresolved` fold, 0 mapping mismatches, identical
  path sets and wrapped flags (`op/O07-parity.md` §5). My independent fold agrees on the totals
  and on every fallback/unresolved row.
- **Demotion is by record, not by edit.** The authority body's docstring, O04's witness clauses,
  O06's artifact `tool.witness` block, and O07's receipt all label the extractor "N6 regression
  witness only". That is the claim's stated mechanism (bytes untouched).

Residual risk, named but not harm: **two executable tools remain.** Nothing mechanically stops a
future operator from running `couples-reference-extractor.py --census` and quoting its six
buckets as the policy answer. The demotion is discoverable in the drafted records but not in the
live instrument index (`SKILL.md` was not edited; O04 §3.4 calls the index row optional). The
integrator's LOG entry is the load-bearing discoverability step and does not exist at cut. This is
acceptable for the claim as worded ("demoted to witness-only, bytes untouched") but should be
recorded as a residual operability risk, not presented as enforcement.

### 2.2 What is genuinely better

- The live extractor's blank-line `continue` over-capture is closed in the successor's code path
  (my fixture: 3 live refs vs 1 new ref). The honest scope is **latent trap closed**, not
  "corpus-wide miscount corrected": O03's whole-corpus differential found 0 entries where the
  witness captures a token the successor does not, 19 entries structurally exposed (couples as
  the last header field), 0 entries currently triggering the shape. Any LOG/SHONEN sentence must
  keep that qualifier.
- The ambiguous control (S3a/S3b), indented-prose control (S7c), four-class census, and the
  per-token disposition leg are genuinely new relative to the r42 selftest (8 checks, no
  ambiguous control). 27/27 is reproducible.
- Every fallback mapping is listed (50, occurrences sum 166) and every unresolved row has a real
  reason; no token is guessed.

### 2.3 Defects/limits that travel with the (unchanged) pinned body

1. **`--census --json` hardcodes `"round": 43`.** The body must land byte-exact, so the r44
   artifact must wrap it and record `tool_emit_round: 43` (O06 does; O02 §4.2, O03 §7.2, O10 §6.2).
   Do not edit the body to "fix" this.
2. **Docstring overclaims an exception the code cannot reach.** The docstring says a blank line
   terminates "unless the previous part ends in a hyphen soft wrap"; `soft_wrap` is
   `parts[-1].endswith("-") and not saw_blank`, so after a blank line it is always false. The
   behavior (blank always terminates) is the safe one; 0 live blank-separated continuations. This
   is a successor-record note, not an edit to the pinned bytes (O03 §7.1).
3. **S1a is corpus-coupled.** It asserts the embedded fixture equals the live couples block of
   `phonetics-phonology.md:72-77`; any future edit there turns `--selftest` red. The C draft does
   not touch that entry, so the landing does not break it — but "durable" does not mean
   "corpus-stable".
4. **The census artifact's `content_sha256` rule is under-specified.** The filed block's digest
   reproduces only with the generator's canonical form (`sort_keys=True`,
   `separators=(",", ":")`); the written instruction ("recompute over the body minus `date` and
   `content_sha256`") does not name the serialization, and the obvious `indent=1` form produces
   `a0a43ac5…`, not `3ee551fc…`. I confirmed the intended digest by reproducing the generator's
   canonicalization, and the artifact's own block digest `c0ee791a…` matches the fenced text. The
   rule should be written into the artifact or the integration note.
5. **The 223 denominator is only provable before C lands.** O06 pins `entries: 223`, a corpus
   fingerprint `7675c724…` (which I recomputed exactly), and a `state_note` that C is a later
   delta. That is the right shape. If the integrator re-runs `--census` after C and files the 224
   numbers under the 2729 predicate, the claim becomes unprovable. File O's artifact from the
   223 tree (or a faithful mirror with the eight lane-root targets) first.
6. **Run-location traps are real** (212 snapshot; corpus-only 2536/27). The artifact should carry
   `measured_root` (O06 carries the fingerprint and state note but not the path); the integrator's
   post-apply run must be from `tools/harness/` or the lane root and must confirm `entries=223`.

**O harm verdict:** none observed. No second durable resolver path exists (`git ls-files` has only
the witness; 19 scratch copies are gitignored and non-durable), the witness is unedited, the
corpus is untouched, and the token accounting closes. The claim is simply **not delivered at cut**
because the authority path and the calib artifact are empty.

---

## 3. Claim C — duplicate, overwrite, and the gap conflict

**Verdict: no duplicate and no overwrite on disk; the coverage axis is unchanged at cut. But the
evidence chain is split across two gaps, and the drafted gap is a carried proposal.**

### 3.1 The conflict, precisely

- The claim (`claims.json:37-46`) requires "the wave's scout names a gap with NO current owner
  (verified by a fresh absence sweep at the 223 total, **not carried from a prior round**)" and
  thresholds repeat "**(not carried)**".
- **K02, the claim-named scout, selected cartography / mapmaking**
  (`scout/K02-gap-scout.md:8`, `:85`; path `culture-material/cartography-and-mapmaking.md`), and
  explicitly screened dream/vision/trance out as **"carried — reject"** because r42's scout
  already named it (`K02-gap-scout.md:78`).
- r42's scout named the same complex and the same filename:
  `reports/round-42/scout/K02-myth-gaps.md:216` ("R2 — Dream, vision and trance") and `:259`
  (`- **Filename:** dream-vision-trance.md`). It was deferred, not landed.
- K04 independently named dream/trance and did not apply K02's carriage screen
  (`scout/K04-gap-verify.md:10`, §4). C01 drafted that entry and says, correctly, that if K02
  names a different gap the draft is "a **spare**, not the claim's landing"
  (`cov/C01-entry-draft.md:8`). K02 now exists and names a different gap.
- C06 (rewritten at 17:29Z) lays out both readings and states that "**Only the integrator can
  rule**"; it recommends Option A (cartography) as the threshold-safe default and says Option B
  (dream) is defensible only with an explicit, filed overrule of K02's screen
  (`cov/C06-scribe.md:286-307`). R01 independently reached the same conflict and the same ruling
  requirement (`review/R01-review.md` R01-44-09); our verdicts agree.

Both readings are defensible, and that is the problem: the round has not recorded which one it is
using. Under the strict reading (K02's), the drafted entry fails a stated threshold; under the
re-measurement reading (K04/C01's, documented in C06 §4.2), it passes because the premise is true
at 223. A reviewer must not
silently pick one. My position: **the dream topic is genuinely unowned and freshly measured; the
proposal is nonetheless carried from r42. If it lands, the round must say "carried proposal,
re-measured unowned at c9f4eaa" and cite r42:216/:259 — not claim it was not carried.** If the
round wants the strict predicate, it must land K02's cartography, for which **no draft, no
source audit, and no contract audit exist at cut**.

### 3.2 Does the draft duplicate or overwrite?

No, on every check I can run:

- exact path absent; no filename collision in any partition (0 hits);
- topic ownership: the only topic-line hits are divination's technique row and mongol's lexical
  data; the draft's boundary table enumerates both, plus ritual-liminality, animal-symbolism,
  music-instrument, death-afterlife, the Australian Dreaming, and the register/speech-act files;
- no existing entry is edited; the only other path is `corpus/README.md`, which is **not yet
  drafted** (C02 absent);
- the draft's own couples block is 15 direct tokens, all resolving; no fallback/unresolved rows;
- its 16 path anchors and every cited line/range resolve; no canon or "should work" wording.

If it lands, coverage improves by a real unowned entry (total 224, myth-symbol 27), and the
post-C census would be `224 / 2745 / direct 2571`. If cartography lands instead, the counts differ
(culture-material 26; its couples refs unknown until drafted) — the integrator must recompute, not
reuse the 15.

### 3.3 The README and the carried rev-2.4 defect

Live README is rev 2.4, green: 223 rows/files, totals 223, footer `25/26/25/29/24/94`. I
reproduced the pre-existing prose-vector defect:

```
revision 2.4 line: vector 25/23/25/29/24/94 → 25/23/26/25/24/94
sum(25,23,26,25,24,94) = 217      # while the live tree is 223
sum(25,26,25,29,24,94) = 223      # footer, correct
```

The sweep does not read revision prose, so this passes green. C02's rev 2.5 must not propagate the
217 vector; the landing partition's increment must use the live vector (myth-symbol 26→27 or
culture-material 25→26), and the totals/footer must move to 224. C02's absence at cut means the
"README rev 2.5 sweep-green 224==224" threshold is unmeasured.

**C harm verdict:** none on disk. The harm risks are procedural: landing both gaps (forbidden by
`+1` and the r42 duplicate-topic precedent), landing the carried proposal while claiming a fresh
gap, or landing without C03/C04 audits. All three are avoidable with an explicit integration
record; none has occurred.

---

## 4. Claim Ca — does the gate actually catch a stale `before`?

**Verdict: the method works on the required regression and on declared probes; the durable gate is
not delivered, its selftest is red, and its legacy mining is heuristic enough to false-refuse.**

### 4.1 What passes

- r43 regression: `STALE O` (both mined absence premises false at `7ceff59`; the witness exists),
  `STALE C` (counts true, ownership false: `mineral-stone-symbolism.md` exists at baseline),
  `FRESH Ca` (no disposition artifact at baseline), exit 2 + explicit REFUSE line.
- The gate reads the **baseline commit** through git plumbing, so a landed artifact does not
  retroactively stale its own `before`.
- Declared probes work: a false `count_eq` is stale, a true one is fresh, and a claim with no
  groundable premise is `unverifiable` and refused rather than greened (my synthetic A–D, F).
- It is read-only and edited no filed byte.

### 4.2 What fails or is weak

1. **Not durable at cut.** `tools/harness/claims-freshness.py` does not exist; only
   `.scratch/ca01/claims-freshness.py`. The claim allows "a tool or a documented gate", but a
   `.scratch` script is explicitly not durable ("durable not .scratch" in the thresholds). A
   fenced draft for the integrator is the lawful route; at cut no such fenced block or calib
   artifact exists in `reports/round-44/calib/`.
2. **Selftest red (17/19).** Two failures: a synthetic-`beta` `grep_absent` fixture check, and a
   check-count assertion expecting 17 when 18 ran. The production partition variant passes, so
   this looks like fixture/assertion debt, not a broken probe — but the claim's own review bar
   (S01 §4.3) asked for a green `--selftest`; a red one must be dispositioned, not ignored.
3. **Novel-slot false positive.** My synthetic "the llama-herding register slot is unbuilt"
   mines the topic as `register` (the E3a regex captures only the final hyphen word before
   "slot") and marks the claim stale against 51 "owners". A genuine fresh claim phrased with a
   multi-word modifier would be refused. The r43 C phrasing ("lithic slot") happens to work; that
   is luck of phrasing, not a general property. This is exactly the theater/fragility risk X02
   and S01 named. The fix is either a multi-word topic capture or a refusal (`unverifiable`) when
   the captured topic is a generic stop-word like "register".
4. **Family-scan false candidates.** In the r43 O run, E1a counted `tools/gates/provenance-audit.py`
   (a gate that checks for a missing `- couples:` header) among the "couples family" candidates.
   The verdict was still correct because the real extractor also exists, but the heuristic can
   inflate a family count with unrelated files. The output should label candidates with a file
   role or exclude gates; otherwise a future claim could be falsely stale on a doc mention.
5. **It cannot catch the C carriage conflict.** The gate checks ownership/counts, not whether a
   gap was proposed in a prior round. That is outside R01-43-12's stale-premise class, so it is
   not a defect in the gate — but it means the gate does not close the §3 conflict, and the
   round should not present it as doing so.
6. **Exit-code contract differs from the X00/S01 proposal.** The gate documents 0 fresh, 1 usage,
   2 stale, 3 unverifiable; X00/S01 proposed 1 for stale. The gate's own contract is coherent and
   the REFUSE is explicit; the demonstration must quote the actual codes (2/3), not the proposal.

**Ca harm verdict:** none observed (read-only, no filed edits). The axis is improved *in method*
— the required r43 positive and negative controls reproduce — but the claim is `unprovable` at
cut until a durable, selftest-green artifact is filed.

---

## 5. Named findings

| ID | Claim | Severity | Finding | Owner |
|---|---|---|---|---|
| **R02-44-01** | C | **blocking as worded** | The drafted gap (dream/vision/trance, `myth-symbol/dream-vision-trance.md`) is the r42-carried R2 proposal (`reports/round-42/scout/K02-myth-gaps.md:216,:259`). The claim-named scout K02 selected cartography instead and explicitly rejected dream as carried (`scout/K02-gap-scout.md:78`). C06 documents both readings and says "Only the integrator can rule," recommending cartography as the threshold-safe default (`cov/C06-scribe.md:286-307`); the claim text and threshold say "not carried from a prior round" (`claims.json:39,46`). The integrator must pick one reading and record it; it must not silently land the carried proposal under a "fresh gap" claim. R01-44-09 independently records the same conflict. | Integrator + C seats |
| **R02-44-02** | C | **blocking delivery** | At cut there is no C02 README draft, no C03 source audit, no C04 contract audit, and no landing. `reports/round-44/cov/` has C01/C05/C06 only; `corpus/` is untouched (223). C05's clearance is explicitly conditional on the draft and on K02's gap (`cov/C05-collision.md:10,17`). | C seats / integrator |
| **R02-44-03** | C | major (if dream lands) | The rev-2.4 prose vector sums to **217**, not 223 (`corpus/README.md:11`). The sweep does not read prose, so it passes green. Rev 2.5 must not propagate the 217 vector; use the live vector plus the landing partition increment and re-sum to 224. | C02 / integrator |
| **R02-44-04** | Ca | **blocking delivery** | The gate is `.scratch`-only at cut; no durable `tools/harness/` copy and no `reports/round-44/calib/` demonstration. The claim's own durability threshold is unmet. | Ca seats / integrator |
| **R02-44-05** | Ca | major | Gate `--selftest` is red (17/19): a synthetic `corpus/knowledge/beta` `grep_absent` fixture fails, and the check-count assertion expects 17 while 18 ran. The production partition probe passes, so this is test debt—but it must be fixed or dispositioned before the gate is called durable. | Ca01/Ca02 |
| **R02-44-06** | Ca | major | Legacy E3a topic mining false-positives on multi-word subjects: "the llama-herding register slot is unbuilt" mines `register` and refuses against 51 owners. The r43 "lithic slot" case works by phrasing luck. Add a multi-word capture or refuse generic stop-word topics as `unverifiable`. | Ca01 |
| **R02-44-07** | Ca | minor | E1a's family scan counts unrelated gates/docs (e.g. `tools/gates/provenance-audit.py`) as family candidates. The r43 verdict is unaffected, but the evidence list can mislead; label candidate roles or exclude gate files. | Ca01 |
| **R02-44-08** | O | **blocking delivery** | The authority path and the ONE census artifact are absent at cut (`tools/harness/basename-couples-resolver.py` missing; `calib/` empty). The body is byte-exact and green, but the claim's `after_required` is not met until the integrator applies it. | Integrator |
| **R02-44-09** | O | major (run discipline) | The census is root-sensitive: a 212-entry snapshot under `.scratch/o07/` yields `212/2508` (my run), and a corpus-only mirror yields `2536/27` (X00). The landed path is correct, but the artifact must pin `measured_root`/`entries` and the post-apply run must be from the lane root/tool path. O06 pins the fingerprint but not the path. | O06 / integrator |
| **R02-44-10** | O | minor | The pinned body hardcodes `round: 43`; the artifact wrapper must record `tool_emit_round: 43` and keep `tool_sha256` over the unchanged body (O06 does this; do not edit the body). | integrator |
| **R02-44-11** | O | minor | The body's docstring overclaims an unreachable hyphen-soft-wrap exception after a blank line (behavior is the safe one; 0 live cases). Record as a successor note; do not edit the pinned bytes. | successor record |
| **R02-44-12** | O | minor | `content_sha256` reproduces only under the generator's compact canonical JSON (`sort_keys=True, separators=(",", ":")`), not the written "body minus date/content_sha256" instruction. Document the canonicalization or the digest is not independently reproducible. | O06 / integrator |

No finding alleges fabrication: every number in the filed outputs that I re-measured reproduced
exactly, and the two divergences I found (the 17/19 selftest and the novel-slot false positive)
are defects in a draft, not invented evidence.

---

## 6. Per-axis verdict, in the round's vocabulary

| Axis | Verdict | Condition |
|---|---|---|
| operability | **`unprovable-but-better`** | `improved` iff the integrator lands the byte-exact body, files the 223 census + parity receipt, and the post-apply selftest/census reproduce 27/27 and `223/2730/2556+166+0+7+1`. `harmed` would require a second durable resolver path, an edited witness, or a wrong-tree census — none observed. |
| coverage | **`unchanged`** | `improved` iff exactly one gap lands with C03/C04 PASS, C02's rev-2.5 sweep is 224==224 with the vector re-summed, and no existing entry changes. `harmed` if both gaps land, a topic duplicate lands, or any baseline entry is modified. |
| calibration | **`unprovable-but-better`** | `improved` iff a durable `tools/harness/claims-freshness.py` (or documented gate) exists with a green selftest, the filed r43 demonstration shows `STALE O/C + FRESH Ca` with a non-zero refusal, and the negative control is a true `before`. `harmed` if it greens a stale claim, reds a true one, or edits `reports/round-43/**`. |
| depth / adjacency / freshness | `unchanged` | Not claimed; freshness paused; no packet/canon surface touched. |

---

## 7. What I could not evaluate (honest limits)

1. **C03/C04/C02 and the Ca filed outputs** did not exist at my cut. Their PASS/FAIL is
   `could-not-evaluate`, not green. If they land after this file, §8 records it; the integrator
   must re-run the relevant checks rather than treating this review as a substitute.
2. **The landing itself** is integrator-applied. I verified the body and the draft as artifacts,
   not the post-apply tree (the authority path, the calib JSON, and the corpus entry are absent at
   cut).
3. **The cartography candidate** has no draft, no couples block, no audits; I verified only its
   absence and topic non-ownership. Its refs/count effect is unknown.
4. **The gate's behavior on a genuinely fresh multi-word slot** is not reliable (finding 06). I
   tested one synthetic phrasing; a broader phrasing corpus would be needed to characterize the
   false-positive rate.
5. **Packet-surface pins** are A01's leg; I checked only that no packet/tool/corpus path is
   modified in `git status`. I did not re-freeze or re-hash the packet surface.
6. **The r42/r43 filed bytes** were read, never edited. My scratch copies are disposable and
   gitignored; the durable evidence is the command output quoted here.

---

## 8. Post-cut addendum

At `2026-10-19T17:33:08Z` the landing set was: `claims.json`, `targets.json`, telemetry,
`adj/A01`, `cross/X00/X01/X02`, `op/O02/O03/O04/O06/O07/O08/O09/O10`,
`scout/K01/K02/K04`, `cov/C01/C05/C06`, `scribe/S01/S02`, `review/R01`, and this file.
**Still absent:** `reports/round-44/calib/*` (O's census JSON and Ca's demonstration), `cov/C02`
(README), `cov/C03` (source audit), `cov/C04` (contract audit), `op/O01/O05/O11+`, `scout/K03`,
`plan/P01`, `scribe/S03+`. Any later file is outside this cut's verdicts; the integrator must fold
it and re-run the affected gates.

Cut-time note for the diff: C01/C05/C06 were rewritten between 17:25Z and 17:33Z. This review
uses the final bytes read at the cut (`C01` sha256 `11acfc31…`, `C06` sha256 `864ad939…`); the
draft's entry is `C01-entry-draft.md:108-395`, 286 lines / 55,575 bytes, 15 couples tokens, all
direct. R01's 17:30Z review independently
reached the same O and C verdicts and the same C conflict (R01-44-09). On Ca we differ in label
only: R01 says `unchanged`, I say `unprovable-but-better` because the scratch gate's r43 regression
is demonstrated; both of us hold that the durable deliverable is absent and no axis is harmed. No
divergence was found between the two reviewers' harm assessments.

---

## 9. Reproduce

```bash
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin

# O — body identity, selftest, census
sed -n '356,870p' reports/round-43/op/O09-scribe.md > .scratch/r02-o09/basename-couples-resolver.py
sha256sum .scratch/r02-o09/basename-couples-resolver.py   # 43ce341f…ad64
(cd .scratch/r02-o09 && python3 -B basename-couples-resolver.py --selftest)
(cd .scratch/r02-o09 && python3 -B basename-couples-resolver.py --census)

# O — witness unchanged + six-class fold
sha256sum tools/harness/couples-reference-extractor.py     # d8d23a26…
python3 -B tools/harness/couples-reference-extractor.py --census

# O — shadow trap (expect 212/2508 from this snapshot, NOT live evidence)
(cd .scratch/o07 && python3 -B basename-couples-resolver.py --census | head -2)

# C — live partition and both candidates
find corpus/knowledge -name '*.md' | wc -l                 # 223
python3 -B reports/round-28/readme/sweep.py                # 223==223, exit 0
grep -rilE -- '^- topic:.*\b(dream|trance|ecsta|shaman|incubat)' corpus/knowledge/*/*.md
find corpus/knowledge -iname '*dream*' -o -iname '*trance*' | wc -l
grep -n "R2 — Dream\|dream-vision-trance.md" reports/round-42/scout/K02-myth-gaps.md
grep -n "cartography-and-mapmaking\|carried — reject" reports/round-44/scout/K02-gap-scout.md

# C — draft mechanics
python3 - <<'PY'
import re
t=open('reports/round-44/cov/C01-entry-draft.md').read()
body=re.search(r'````markdown\n(.*?)\n````',t,re.S).group(1)
open('.scratch/r02-c01/dream-vision-trance.md','w').write(body+'\n')
PY
(cd .scratch/r02-c01 && python3 -B ../r02-o09/basename-couples-resolver.py --json dream-vision-trance.md)

# Ca — regression + selftest (scratch draft at cut)
python3 -B .scratch/ca01/claims-freshness.py --selftest       # 17/19 FAIL at cut
python3 -B .scratch/ca01/claims-freshness.py --claims reports/round-43/claims.json

# Integrity
git status --porcelain
sha256sum reports/round-43/op/O09-scribe.md                   # 956d478b…cb341
```
