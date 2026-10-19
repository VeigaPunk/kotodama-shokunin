- Seat: R01 | reviewer | claim cross | date 2026-10-19 | baseline ac47c78

# R01 — adversarial review of both blocks (claim O false-green hunt; claim C fabrication hunt)

Mission (`reports/round-42/targets.json` seat `R01`, verbatim): *"Adversarial review of
both blocks (the fix's false-green hunt; entry fabrication hunt)."* Out:
`review/R01-review.md`.

**Method / boundary.** Every number below was re-derived by this seat with read-only
commands at HEAD `ac47c78` (lane root, `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`). No filed byte was edited; no `reports/round-*/run-validation.py`
was executed (in-tree or in a copy); no corpus byte was staged; no git/network/install
action. Where a peer already filed a finding, it is marked **CONFIRMED (peer)** and not
re-presented as mine. Where a finding is new, it is marked **NEW**.

## Verdict

**Neither block is admissible as it stands, and both fail for the same structural
reason: the round declared its own acceptance numbers, and those numbers are wrong.**

- **Claim O (operability).** The defect is real, live, and exactly located, and the
  wave's census arithmetic is sound and multiply reproduced. But the claim's
  `after_required` ("zero phantom attributions remaining or each dispositioned") is
  met only by a **reclassification**, not by a fix; the declared "owning instrument"
  candidates are both wrong; and the wave's natural fix host — `tools/gates/provenance-audit.py`
  — is a **battery gate whose byte-identity is pinned by two frozen baselines**. Editing
  it to carry the fix, which O10 recommends and O07's clause implies, would break
  `python3 tools/check-gate-battery.py` at r42 close. That is the largest unowned
  risk in this round.
- **Claim C (coverage).** The before-state is exact, the one landed entry (C02) is
  structurally clean, and no fabricated source was found. But the declared rev-2.4
  footer vector is arithmetically impossible (sums 218, not 224), and the instrument
  the claim names for its threshold — `reports/round-28/readme/sweep.py` — **has no
  filename-order leg**, so the "4 rows in filename order" contract is unenforceable by
  the claim's own counting command. The queue row that records this order gap as
  *fixed-with-evidence* rests on a reason the sweep's code contradicts.

**One-line ledger:** claim O's arithmetic verifies; claim O's after-state does not. Claim
C's before-state verifies; claim C's delta bytes do not.

## Claim O — the false-green hunt

### 1. The defect and the census arithmetic verify (independently reproduced)

The r19 extractor's single-line capture is `reports/round-19/audit/entry-audit.py:75`
(`re.search(r"^- couples:\s*(.*)$", text, re.M)`). The corpus's one wrapped couples field
is `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`. Measured this seat,
read-only:

- single-line capture → **0** `.md` tokens (the defect, confirmed live);
- the 21 linguistics files at `dfb0719` **do** include `sound-symbolism.md` and
  `writing-systems.md` (`git ls-tree -r --name-only dfb0719 corpus/knowledge/linguistics`);
  `sound-change.md` and `tone-prosody.md` do not exist at either tree.

I re-derived the r39 baseline byte-exact from `git show dfb0719:<path>` over all 212
entries: **`refs=2504 → direct=2335 fallback=163 ambiguous=0 unresolved=6`** (5 distinct),
matching `reports/round-39/calib/Ca03-basename-policy.md:35-36,268`. This is the control
that licenses every corrected number below. **The arithmetic claim is verified.**

### 2. NEW — the fix's recommended host is a digest-pinned battery gate; patching it breaks the battery

This is the finding I consider most consequential, and no r42 seat owns it.

- `tools/check-gate-battery.py:113-124` registers `provenance-audit.py` in `GATE_NAMES`,
  i.e. it is one of the seven structural gates the battery runs.
- `tools/gates/frozen/provenance-audit/r9-pre/expected.json` and `.../r18-post/expected.json`
  both pin `"gate_sha256": "8a96aaf4ccd14ef40defd4dce115e9ffa79c7a67ea3e9848cb63efbd3aa14e3a"`.
- The live gate hashes to exactly that value (`sha256sum tools/gates/provenance-audit.py`
  → `8a96aaf4…`).
- The battery's own pin leg (`tools/check-gate-battery.py:529-547`) reads: a `gate_sha256`
  that "differs from the live … re-freeze, never compare across an unnamed revision",
  and emits `BASELINE-GATE-REVISED`.

So any edit to `tools/gates/provenance-audit.py` turns both provenance baselines into
`gate_revised` findings at r42 close. **O10 §2 and §5 recommend exactly this host**
("It is the natural host for the fix — a hyphen-aware rejoin at `:255-257` — and O01's
patch should name it", `reports/round-42/op/O10-gap-fill.md:73-75,131`). K01 saw the
hazard and prescribed the opposite ("treat it as **template-only** … unless a round
explicitly owns gate tooling", `reports/round-42/scout/K01-n6-scout.md:313-318`). The
two seats give the integrator contradictory instructions, and only K01's respects the
pinned baselines. **The round's non-goals bar a re-freeze** ("no re-freeze of
`declared-in-r7`", `reports/round-42/claims.json:27`) and the shared rules bar editing
`tools/gates/frozen/**`. A copy-the-semantics route (new `tools/harness/` instrument)
is the only one consistent with both — but that leaves `tools/gates/provenance-audit.py`
carrying the defect, which O10's "the only live gate that reads a couples block
continuation carries the identical defect" makes a standing liability.

**Ask of the integrator:** rule explicitly whether `provenance-audit.py` is in or out as
the fix host, and if in, name the re-freeze round. Do not let O01 land a patch there
under an implied template-only licence.

### 3. NEW — the claim's own "owning instrument" candidates are both wrong, and one is not an instrument

`reports/round-42/claims.json:16` says the host is "likely the r39 C12 runbook's
resolver or a tools/harness couples checker". Measured:

- **C12 is a document, not a resolver.** `reports/round-35/cov/C12-audit-runbook.md` is a
  runbook; its §2 pointer family concerns backticked repo paths, not couples. K01 reached
  the same reading (`K01-n6-scout.md:20-22`). **CONFIRMED (peer).**
- **`tools/harness/` contains no couples checker** (`ls tools/harness/` →
  `packet_links.py`, `packet_uncertainty.py`, `r8_checks.py`, `receipt_guard.py`,
  `receipt_guard_adoption.py`, `round_runner_conformance.py`). **CONFIRMED (peer: O09, O06).**

The consequence the wave under-states: **the claim's `after_required` cannot be satisfied
by fixing a known host, because no eligible host exists.** Every located implementation
(`reports/round-19|27/audit/entry-audit.py`) is a filed byte under the "never edit
`reports/round-1..41/**`" rule. The fix must be *authored fresh*, and the claim's
wording ("its owning instrument identified by the wave") reads as if identification were
the hard part. It is not.

### 4. NEW — the acceptance oracle's item 6 is still inverted, and O04's correction did not reach it

`reports/round-42/op/O03-predicted.md` is the seat chartered to produce "the predicted
corrected census … the landed tool must reproduce it" — i.e. the acceptance oracle. It
contradicts itself:

- §4 (`:100,105`) declares the wrapped field's two live tokens
  (`sound-symbolism.md`, `writing-systems.md`) are **`fallback`** at `dfb0719`.
- §6 (`:127-129`) and §8 item 2 declare the same run **`direct=2337`**.

Measured: Tier 1 tests the token against `<entry dir>/<token>` and is satisfied by any
existing file regardless of the partition's entry count. Both files exist at `dfb0719`
in the entry's own directory, so both are **`direct`** and 2335+2 = 2337 is correct.
§4's reading is the wrong one. **O04 §7 "Divergence 1" (`:236-252`) already made this
correction**, and O06 §5.4 independently did too. **CONFIRMED (peer) — but the residue is
unflagged:** §8 item 6 (`:185-186`) still reads

> "Any landed tool reporting a wrapped-field count of 2, or reading
> `sound-symbolism.md`/`writing-systems.md` as `direct` at `dfb0719`, is reproducing
> C14's blank-line-blind `fields_of` rather than a corrected parser."

The first clause is a legitimate negative control. **The second clause instructs a
verifier to *fail* a correct tool.** A verifier who follows §8 item 6 literally — and §8
is the section the mission designates as the acceptance list — rejects the correct fix.
O04 corrected §4 but explicitly left item 6 standing (`O04-verify.md:251`). This is the
false-green's mirror image: a **false-red** acceptance criterion inside the oracle. The
integrator must strike clause 2 before the oracle is used.

### 5. CONFIRMED — the "obvious fix" does not reach the declared threshold

The field soft-wraps **mid-token**: `:76` ends `... sound-change.md, tone-` and `:77`
begins `prosody.md, ...`. Measured join rules over `:72-77`:

| join rule | tokens | correct? |
|---|---|---|
| single-line (r19) | `[]` | 0/4 |
| space-join / newline-join (C14 shape) | `prosody.md`, `sound-change.md`, `sound-symbolism.md`, `writing-systems.md` | **3/4** — mangles `tone-prosody.md` |
| hyphen-aware rejoin (keep `-`) | `sound-change.md`, `sound-symbolism.md`, `tone-prosody.md`, `writing-systems.md` | **4/4** |
| hyphen deleted (`-` stripped) | `toneprosody.md`, … | wrong token |

So "gain a block parser" is necessary but **not sufficient** for the claim's own
"reads 4/4 targets" threshold. Confirmed independently by O04 §4, O06 §2.5, O07 §2, O09
item 3, O10 §1, P01 anchor 7, R02 trap A/B. **CONFIRMED (many peers).** The wave handled
this well — it is the round's strongest convergence.

### 6. CONFIRMED — O07's first drafted diff was over-capturing; the landed form is correct

The version of O07 I first read carried
`re.search(r"^- couples:([\s\S]*?)(?=\n- [a-z-]+:|\Z)", text, re.M)`. Executed against
the live file it produced **227 parts / 5 tokens including `prosody.md` and ~180 lines of
body prose** — because `couples` is the last header field in all 220 entries, so the
`\Z` alternative never terminates. **O07 self-corrected before I could file it** (§5.1,
`:213-235`) and the landed regex
(`r"^- couples:(.*(?:\n(?!- [a-z-]+:|## ).*)*)"`) I re-executed returns **6 parts / the
correct 4 tokens**. Recorded as a process note, not a defect: **the draft's first form
would have shipped a fix that re-manufactured the phantom it exists to remove**, and the
only thing that caught it was running the draft. This is an argument for the round's
practice of executing fenced drafts against live bytes before landing.

### 7. NEW — the "2 phantom attributions" are dispositioned by reclassification, and the claim's threshold hides that

`claims.json:16` requires "zero phantom attributions remaining **or each dispositioned**".
O07 §4 and O10 §4 satisfy the second branch by reclassifying `sound-change.md` and
`tone-prosody.md` as **prospective seeds** (the field's own words are "prospective sibling
files:"), and O10 §4 adds a proposed fifth class `prospective` to the r39 policy's
four-class scheme (`basename-couples-policy.md:67-88`).

This is defensible and well-argued — but note what it means: **the claim's threshold is
satisfied by a reading, not a repair.** Under the fixed extractor the unresolved count
*rises* 6 → 8 (`O12` §Verdict result 2, `O06` §3 F-O06-1, `O04` §5 item 1, all confirmed).
"Zero phantom attributions remaining" is false; "each dispositioned" is true only because
the wave renamed two of them. A reviewer reading the claim's `after_required` as a
*reduction* requirement would reject the round. The integrator must state plainly that
the disposition is a classification change, and that the count moves the wrong way. O06
and O12 say this; the claim's own text does not.

### 8. CONFIRMED — the filed r39 policy is a truncated prefix

`reports/round-39/calib/basename-couples-policy.md` is 107 lines / 5832 bytes, sha256
`105dfff6…`, ending mid-§6 on the lead-in sentence, with the fenced recipe, the run output
and §7 absent (`grep -c '```'` → 0; `grep -c 2504` → 0). The authoring draft
`reports/round-39/calib/Ca03-basename-policy.md` is 359 lines and carries all of it. **NEW
in this wave (P01 anchor 10, O03 §9, O12 §1, S01 §3) — but it is not a claim-O or claim-C
defect**; it is a filed-byte landing defect from r39, and it matters here because the
claim's `after_required` says the corrected census must reproduce "the r39 policy's
arithmetic" — arithmetic that **is not in the filed policy**. The successor note cannot
cite a recipe that is not there. Route to the integrator/operator as a filed-round
correction; it is outside this round's authority to repair.

## Claim C — the fabrication hunt

### 9. NEW — the declared footer vector is arithmetically impossible

`reports/round-42/claims.json:20-22` and `reports/round-42/targets.json:163` both declare
the rev-2.4 footer vector **`25/23/27/25/24/94`** alongside "totals 224".

- The footer vector is read in README section order:
  `linguistics, myth-symbol, culture-material, synthesis, verification, civilizations`
  (`reports/round-28/readme/sweep.py:50-57`, confirmed by the live `footer_live.order`).
- Under that order the literal vector sums to **218**, not 224.
- Slot 3 is **culture-material**, not myth-symbol, so the literal vector moves the wrong
  partition — contradicting the same sentence's own "myth-symbol 27".
- The correct vector is **`25/27/25/29/24/94`** (sum 224).

**CONFIRMED (peers: C08 D1 `:139-146`; C07 §5; X01 T7 `:152-159`; K02 §6).** I re-derived
it from `sweep.py:50-57` and the live census (`25/23/25/29/24/94`, total 220) before
reading the peers. Precedent check: r39 and r40's declared vectors both summed to their
declared totals, so this is the **first self-inconsistent mission vector in the lane** —
not house convention. Disposition: apply `25/27/25/29/24/94`; the mission's `totals 224`
is correct.

### 10. NEW — the claim's counting command cannot enforce the claim's own contract

`claims.json:24` names `python3 -B reports/round-28/readme/sweep.py` as a counting
command, and `claims.json:22` requires "4 rows in **filename order**". The sweep has **no
ordering leg** — I read `sweep.py:119-212` (it checks missing/ghost/duplicate/topic-equality/
header/totals/footer) and confirmed empirically: I planted a README whose `## myth-symbol/`
rows were **swapped out of filename order** and ran the filed `sweep.sweep()` on it. It
returned `ok: True, topic_mismatch: 0, orphan_rows: 0, missing_from_index: 0,
footer_ok: True, totals_ok: True`. **A filename-order violation reads green.**

This was already filed at r40 (`reports/round-40/cov/C07-verify.md:104-113` F4: "the sweep
still read green — proof the contract's 'filename order' clause is enforceable only by an
order check"). **CONFIRMED (peer, r40).** What is *new* is the consequence for r42: claim
C's threshold is "sweep green; audits clean", and the round has **no order check in its
acceptance sequence**. The mission's "4 rows in filename order" is therefore unverifiable
by the instruments the round declares. C08 §2.3 and K02 §5.4 both re-verify the 23-row
section is `sorted()` today, which is the right *evidence* — but it is a one-time reading,
not a gate. Recommend the integrator run `rows == sorted(rows)` as a named acceptance step
and file the missing order leg as a queue row (none exists).

### 11. NEW — a queue row records the order gap as fixed on a reason its own code contradicts

`reports/round-40/op/defect-queue-v2.json:132-138` carries
`R36-README-ORDER-CONTIGUITY-REVERIFY`, class **`fixed-with-evidence`**, `next_touch`
"none — fixed", `verification` "r39 validation.json acceptance true". Its reason reads:

> "…superseded by the r39 rev-2.2 landing where the r28 sweep — an independent mechanical
> control checking **order**, contiguity, header drift, ghost and missing rows — ran green
> 216 rows == 216 files…"

**The sweep does not check order** (§10). The row was closed on a control that does not
exist, and r40's own filed C07 F4 says so in the same repository. This is a live
`fixed-with-evidence` row whose evidence basis is falsified. It is not a r42 claim defect,
but the integrator is folding the queue this round (O08 §5) and should re-open or re-reason
this row rather than carry a false fix forward. No r42 seat names it.

### 12. CONFIRMED — C02's entry is structurally clean; three count defects, one class

The only landed entry draft is `reports/round-42/cov/C02-entry-2.md` (one 3-backtick
`markdown` fence, `:13-201`, no internal fence line; staged entry 49606 bytes; head block
carries `topic/sources/couples/source/verified-at/recheck/gap filled`; all **36 couples
tokens resolve direct**). Its citations survive the hunt:

- **168 `path:line` anchors checked programmatically** for file existence and line range:
  **1 problem, and it is a false positive** — the token `REGIMEN.md` (no line number,
  a prose reference, correctly resolvable at lane root). No out-of-range citation, no
  missing file, no dangling pointer.
- **Spot-checked quoted lines all read what the entry claims:** `symbolism-synthesis-method.md:40`
  ("take the anomaly engine only"), `animal-symbolism.md:69` ("one law, two rival
  explanations"), `bathing-and-body-hygiene.md:50` ("They are different systems and must
  not be merged"), `israel-ancient-hebrew.md:150` ("intersecting classifications, not
  interchangeable labels"), `politeness-taboo-euphemism.md:73` (the Steiner/Radcliffe-Brown/
  Douglas spine), `ritual-liminality.md:57` (the piacular row). **No fabrication found.**
- **Three inflated counts, all one class** — `taboo` "122 files" (121 case-sensitive; 122
  needs `-i`), `purity` "41 files" (39 case-sensitive), `Douglas` "31 files" (**13** files;
  31 is the case-insensitive **line** count, 32 the case-sensitive line count). I measured
  all six variants to pin the unit: `grep -ril douglas corpus/knowledge/*/*.md | wc -l` →
  31 **lines**, `-rl` → 13 files. The `Douglas` claim is a line count reported as a file
  count; the other two are `-i` counts reported as case-sensitive. **CONFIRMED (peer: C07
  §6 D2, same three, same class, same fix).** The substantive leg — every zero-count that
  constitutes the gap evidence — reproduces exactly (I re-ran the topic-owner sweeps:
  `pollution`/`boundary maintenance` → 0; topic-owners `taboo` → 8, `purity` → 2).
- **The self-selected topic collides with nothing.** K02 landed after C02 and *confirms*
  rather than re-recommends the purity slot (`K02-myth-gaps.md:306-337`), verifying the
  slug `purity-pollution-systems.md` does not collide with the 23 existing names. Good
  outcome — but note C02 chose its own topic because K02 was absent at its seat time
  (`C02-entry-2.md` §Dependency status), so the de-collision was **not** designed in; it
  happened to work. With only 1 of 4 drafts landed, three more topics (K02's R1–R3:
  `mineral-stone-symbolism.md`, `dream-vision-trance.md`, `pilgrimage-sacred-geography.md`)
  are unclaimed and unaudited.

### 13. The C block's audits are largely absent at this cut

`cov/C05-audit.md` (the chartered audit of all 4 drafts), `cov/C06-delta-receipt.md`,
`cov/C01-entry-1.md`, `cov/C03-entry-3.md`, `cov/C04-entry-4.md` are all **absent**.
Claim C's `after_required` is "audits 4/4 PASS" — with one draft landed and its chartered
auditor absent, **claim C's audit leg is unestablished, and 3 of its 4 deliverables do not
exist.** C07 §6 audits C02 alone and says so; C08 §3 drew a lot (C02, C03) and delivered
neither. This is the honest state and the wave reports it honestly; it is recorded here so
the integrator does not read "audits clean" from the claim text as satisfied.

## Cross-block

### 14. The round's own counting commands are partly unrunnable or wrong

- Claim O's `counting_commands` is `["python3 reports/round-42/run-validation.py"]`
  (`claims.json:17`). That file **does not exist** at this cut, and the absolute shared
  rule forbids any seat running it in-tree. A claim whose only counting command is a file
  that does not exist and that no seat may execute is not measurable by the round's own
  definition.
- Claim C's first counting command is `ls corpus/knowledge/myth-symbol/*.md | wc -l` →
  23 today, 27 required. Sound. Its second is the order-blind sweep (§10).

### 15. Convergence quality

Where the wave converged, it converged *independently* — O03, O04, O06, O07, O10, P01 and
A01 each built their own re-parser and landed on `2504 → 2508` at `dfb0719` and
`2607 → 2611` at `ac47c78`, with the delta decomposed as **+4 refs / +2 direct / +2
unresolved** (never "-2 phantoms"). I reproduced the same numbers from `git show`. That
is genuine multi-seat verification of the arithmetic and should be recorded as such.

The weakness is the opposite: **the wave's disagreements were smoothed into the wrong
side.** O03's §4 "fallback" reading and §8 item 6's inverted clause are both outliers that
contradict O03's own §6/§8-item-2 numbers, and both survived to the oracle because the
seats that corrected them (O04, O06) filed their corrections in *their own* fragments
rather than as a named defect against O03's. A reader taking O03 §8 as the acceptance list
inherits the false-red. **Recommendation: the integrator folds a single corrected oracle
rather than letting six fragments each carry a partial correction.**

## Owed

- **Integrator — the gate-host ruling (§2).** Decide whether `tools/gates/provenance-audit.py`
  is the fix host. If yes, name the re-freeze round and the two baselines it revises
  (`tools/gates/frozen/provenance-audit/{r9-pre,r18-post}`); if no, record the copy-the-semantics
  route and the standing liability that the live gate keeps the defect. O10 and K01 give
  opposite instructions and this is not mine to settle.
- **Integrator — correct the oracle (§4).** Strike `op/O03-predicted.md:185-186` clause 2
  ("reading `sound-symbolism.md`/`writing-systems.md` as `direct` at `dfb0719`") before
  using §8 as the acceptance list. Clause 1 (wrapped count = 2 is a failure) is correct
  and should stand.
- **Integrator — apply the corrected vector (§9).** Emit `25/27/25/29/24/94`, not the
  literal `targets.json` string, into `corpus/README.md`'s counts footer.
- **Integrator — add the order check (§10) and re-reason the queue row (§11).**
  `rows == sorted(rows)` as a named acceptance step; and re-open or re-reason
  `R36-README-ORDER-CONTIGUITY-REVERIFY` (`reports/round-40/op/defect-queue-v2.json:132-138`),
  whose `fixed-with-evidence` reason asserts a control the sweep does not have.
- **Integrator — file the r39 policy truncation (§8)** as a filed-round byte defect
  (owner: operator/integrator; outside r42's authority).
- **Claim C is not admissible at this cut** — 3 of 4 drafts absent, `cov/C05-audit.md`
  absent, the declared vector wrong, and the order leg unenforceable. The one landed draft
  is clean with three named count defects (owner: C02/integrator, apply-as-is within the
  named-defects threshold).
- **Claim O is not admissible at this cut** — no durable fixed extractor exists at any
  eligible host, `run-validation.py` does not exist, and the declared threshold is met by
  reclassification rather than repair.
- **to-verify:** whether O01/O02/O05 (absent at every cut of this seat) reach a different
  fix host than O10's `provenance-audit.py` recommendation; this seat's §2 finding applies
  to whichever host is chosen if it is a battery gate.

## Citations

- **Assignment / boundary:** `reports/round-42/targets.json` seat `R01` (`:174`), shared
  rules (`:4-9`, `:8` no in-tree runner); `reports/round-42/claims.json` claims `O`
  (`:13-18`) and `C` (`:19-24`), non-goals (`:26-27`); `REGIMEN.md:27-43`.
- **Claim O defect site:** `reports/round-19/audit/entry-audit.py:31,34-42,74-96` (`:75`
  the single-line capture, `:87-95` Tier-1 bases); `reports/round-27/audit/entry-audit.py:275`;
  `reports/round-39/calib/Ca04-verify.md` D1; `reports/round-40/op/defect-queue-v2.json:362-369`
  (`N6-couples-extractor-wrapped-field`).
- **The wrapped field:** `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
  (the `tone-` / `prosody.md` break at `:76-77`); `:279` (the prose re-mention).
- **Census arithmetic:** `reports/round-39/calib/Ca03-basename-policy.md:35-36,268`
  (`212/2504 → 2335/163/0/6`); `reports/round-39/calib/basename-couples-policy.md:16-17,67-88`
  (§1 single-line rule, §2 four classes), 107 lines / sha256
  `105dfff6c667ad5b77c28be8d6070ec243b5e19029fb60ae83d6028aa2e941cf`;
  `reports/round-35/cov/C14-audit-6-10.md:208-236` (`frontmatter_block`, `fields_of`).
- **The fix-host hazard (§2):** `tools/check-gate-battery.py:113-124` (`GATE_NAMES`),
  `:529-547` (the `gate_sha256` pin leg, `BASELINE-GATE-REVISED`);
  `tools/gates/frozen/provenance-audit/r9-pre/expected.json` and `.../r18-post/expected.json`
  (`gate_sha256` `8a96aaf4ccd14ef40defd4dce115e9ffa79c7a67ea3e9848cb63efbd3aa14e3a`);
  live `sha256sum tools/gates/provenance-audit.py` → same; `tools/gates/provenance-audit.py:244-260`
  (`field_block`, `:259` the `" ".join`), `:76-77` (`FIELD_RE`/`INDENT_RE`);
  `reports/round-42/op/O10-gap-fill.md:59-75,131` (the recommendation);
  `reports/round-42/scout/K01-n6-scout.md:313-318` (the template-only counter-instruction).
- **The oracle (§4):** `reports/round-42/op/O03-predicted.md:23,100,105` (the `fallback`
  reading), `:127-129` (§6 `direct=2337`), `:185-186` (§8 item 6); `reports/round-42/op/O04-verify.md:236-252`
  (Divergence 1), `:251` (item 6 left standing); `reports/round-42/op/O06-receipt.md` §5.4
  (the same correction).
- **The join rule (§5):** `reports/round-42/op/O04-verify.md` §4; `op/O06-receipt.md` §2.5
  (F-O06-2); `op/O07-gap-fill.md` §2; `op/O09-scribe.md` item 3; `op/O10-gap-fill.md` §1;
  `plan/P01-plan.md` anchor 7; `review/R02-review.md` traps A/B.
- **O07's diff (§6):** `reports/round-42/op/O07-gap-fill.md:213-235` (§5.1, the self-correction),
  the landed regex at the ` ```diff ` block of §5.
- **Phantom disposition (§7):** `reports/round-42/op/O07-gap-fill.md` §4;
  `op/O10-gap-fill.md` §4 (the `prospective` class); `op/O12-policy-check.md` §Verdict
  result 2; `op/O06-receipt.md` §3 (F-O06-1).
- **r39 policy truncation (§8):** `reports/round-39/calib/basename-couples-policy.md`
  (107 lines, 5832 bytes, sha256 `105dfff6…`); `reports/round-39/calib/Ca03-basename-policy.md`
  (359 lines); `plan/P01-plan.md` anchor 10; `op/O03-predicted.md` §9; `op/O12-policy-check.md` §1.
- **Claim C delta (§9-§10):** `reports/round-42/claims.json:20-24`;
  `reports/round-42/targets.json:163`; `reports/round-28/readme/sweep.py:50-57` (`PARTS`),
  `:119-212` (the measurement, no ordering leg); `reports/round-42/cov/C08-verify.md:139-146`
  (D1); `reports/round-42/cov/C07-verify.md:171-218` (§5 D1); `reports/round-42/cross/X01-trades.md:152-159`
  (T7); `reports/round-42/scout/K02-myth-gaps.md:409-438` (§6); `reports/round-40/cov/C07-verify.md:104-113`
  (F4, the order gap).
- **Queue row (§11):** `reports/round-40/op/defect-queue-v2.json:132-138`
  (`R36-README-ORDER-CONTIGUITY-REVERIFY`, class `fixed-with-evidence`).
- **C02 entry (§12):** `reports/round-42/cov/C02-entry-2.md` (fence `:13-201`, staged 49606 B;
  the counts at `:16` and `:229`); `reports/round-42/cov/C07-verify.md:219-262` (§6, D2);
  `reports/round-42/scout/K02-myth-gaps.md:306-337` (the purity slot), `:212,259,303`
  (R1–R3 filenames); quoted lines verified: `corpus/knowledge/myth-symbol/symbolism-synthesis-method.md:40`,
  `myth-symbol/animal-symbolism.md:69`, `culture-material/bathing-and-body-hygiene.md:50`,
  `civilizations/israel-ancient-hebrew.md:150`, `linguistics/politeness-taboo-euphemism.md:73`,
  `myth-symbol/ritual-liminality.md:57`.
- **Command outputs (this seat, 2026-10-19, lane root, HEAD `ac47c78`, all read-only; no
  runner executed, no filed byte written, no git/network/install):**
  (a) single-line vs block capture on `phonetics-phonology.md:72-77` → `[]` vs the 4 tokens,
  and the four join rules of §5; (b) `git ls-tree -r --name-only dfb0719 corpus/knowledge/linguistics`
  → 21 files incl. `sound-symbolism.md`, `writing-systems.md`; (c) full r39-tree recount via
  `git show dfb0719:<path>` → `2504/2335/163/0/6` (single-line) and `2508/2337/163/0/8`
  (block); (d) `sha256sum tools/gates/provenance-audit.py` vs both frozen `gate_sha256`
  pins → match; (e) `python3 -B tools/check-gate-battery.py` → exit 0 at HEAD;
  (f) `python3 -B reports/round-28/readme/sweep.py` → `rows 220 files 220`, `footer_ok True`,
  exit 0, and a tampered swapped-row README → `ok: True` (the order blindness);
  (g) 168 `path:line` anchor existence/range check over `C02-entry-2.md` → 1 false positive
  (`REGIMEN.md`); (h) the six count variants for `taboo`/`purity`/`Douglas` (§12);
  (i) `python3 -B .scratch/r42-r01/census.py` (this seat's own re-parser, scratch only).
