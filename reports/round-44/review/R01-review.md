# R01 — non-author review, round 44: O verified but unlanded, C split by two scouts, Ca still owed

- Seat: `R01` | role reviewer | claim `cross` | round 44, loop 1
- Out path: `reports/round-44/review/R01-review.md` (the only write by this seat)
- Baseline: `c9f4eaa707b6e977ff6e1616463e91f4b8afea5d` (`git rev-parse HEAD`); declared baseline `c9f4eaa` (`reports/round-44/claims.json:7`)
- Review cut: **2026-10-19T17:35Z** (UTC), after K01, K02, K04, O02–O10, C01, C05 (revised to cover both C candidates), C06, X00–X02, R02, S01, S02 and A01 filed. Ca01–Ca03, C02–C04, O01, O05, K03 and P01 were absent at this cut; a **scratch-only** Ca gate draft (`.scratch/ca01/claims-freshness.py`) existed and is reviewed in §4.
- Environment for every command: `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, run from the lane root.
- Boundary: I read filed and seat bytes; I ran the extracted resolver (not the in-tree tool), the r42 witness read-only, and my own scratch probes. I did not edit a filed byte, did not stage under `corpus/`, did not run `reports/round-*/run-validation.py`, and did not run git-mutating, network or install commands. `git status --porcelain` at the cut → `?? reports/round-44/` only.

## 1. Verdict summary

| claim | named-verifier judgment at this cut | basis |
|---|---|---|
| **O — operability** | **unprovable-but-better**; **improved** on a byte-exact landing + filed artifact + parity + demotion record | The body is byte-exact, 27/27, and the four-class census reproduces; the claim-named durable path is **absent**. No live defect or count is harmed. |
| **C — coverage** | **unchanged** at this cut; **improved** only if the integrator resolves the scout conflict and lands one audited entry | Two scouts named different gaps. K02's cartography is fresh but has no draft; K04/C01's dream entry is drafted and collision-cleared but K02 rejects it as carried from r42 K02 R2. No corpus byte has moved. |
| **Ca — calibration** | **unprovable-but-better** at this cut | A scratch-only gate draft correctly flags r43 O and C and leaves r43 Ca fresh (exit 2 + REFUSE), so the method works; no durable gate or filed demonstration exists, and the draft's `--selftest` is red at 17/19. |

No axis is **harmed** by anything on disk at this cut. The harm risks are all in the not-yet-applied integration: a census filed from the wrong tree, a second census artifact, a carried-gap ruling made silently, or a freshness gate that only reproduces two known sentences.

---

## 2. Claim O — the successor authority

### 2.1 Independent reproduction (not trusting any seat)

I extracted the fenced body myself and ran it from `.scratch/r01/`, whose only `corpus/knowledge` ancestor is the real repo root:

```
$ grep -n '^````' reports/round-43/op/O09-scribe.md
355:````python
871:````
$ awk 'NR>=356 && NR<=870' reports/round-43/op/O09-scribe.md > .scratch/r01/resolver-extract.py
$ wc -l .scratch/r01/resolver-extract.py
515
$ sha256sum .scratch/r01/resolver-extract.py
43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64
```

That is the claim pin (`reports/round-44/claims.json:26`) exactly. K01 adds a binding detail: without the final LF the digest is `06ea6318…`, so the apply must end with exactly one newline (`reports/round-44/scout/K01-resolver-scout.md:50-63`).

```
$ python3 -B .scratch/r01/resolver-extract.py --selftest
... 27 PASS lines ...
SELFTEST OK: 27/27 controls          # exit 0
$ python3 -B .scratch/r01/resolver-extract.py --census
entries=223 refs=2730
  policy four-class: direct=2556 fallback=166 ambiguous=0 unresolved=7
  artifacts (excluded from the four-class totals): glob-fragment=1
  conservation: True (sum=2730 refs=2730)
  wrapped fields: 1 ['corpus/knowledge/linguistics/phonetics-phonology.md']
  fallback mappings (50 distinct): ...
  unresolved (7 rows): 5 declared-prospective-seed + 2 dangling-reference
  ambiguous (0 rows):
  glob-fragment (1 rows): -gate.md ... extractor-artifact c12=not-applicable
  misaligned: none
```

Arithmetic: `2556 + 166 + 0 + 7 = 2729`; `+1` quarantined glob = `2730` = refs. The JSON carries 50 distinct fallback rows whose occurrences sum to 166, 7 unresolved rows each with a non-empty reason, and 0 ambiguous rows (`.scratch/r01/census.json`; `--census --json`).

### 2.2 Independent token-level parity

I did not rely on O07's receipt. I loaded both modules in one process and compared every live entry:

```
entries 223
class-pair table (witness -> successor):
  direct         -> direct         2556
  fallback       -> fallback       166
  glob-fragment  -> glob-fragment    1
  prospective    -> unresolved     5
  unresolved     -> unresolved     2
total refs witness 2730 / successor 2730
diffs after prospective->unresolved mapping: 0
```

This is the strongest O fact: the two tools extract the **same 2730 token identities**; the entire delta is the documented subclass separation. O07 (`reports/round-44/op/O07-parity.md` §5), O04 (`op/O04-witness-demotion.md` §5) and K01 (§1.5) independently report the same zero, with the same five `prospective → unresolved` rows.

### 2.3 Defect fixes, with the live/latent distinction

| defect | r42 witness | successor | judgment |
|---|---|---|---|
| blank-line over-capture | `if not following.strip(): continue` (`tools/harness/couples-reference-extractor.py:64-65`), then accepts a later indented line | `saw_blank` set at body:69; indented continuation requires `not saw_blank or soft_wrap`, and `soft_wrap` is itself gated on `not saw_blank` (body:73-74), so a blank always reaches `break` | **fixed as a code path; 0 live incidence** (O03 §2, K01 D1) |
| glob precedence | `ambigu` branch at `:145` before the glob check at `:146-147` | `GLOB_FRAG_RE.search` at body:149 before the slash/one-hit/ambiguous tiers at body:158 | **fixed; S8b control** (body:422-424) |
| ambiguous control | branch exists, no selftest control (8 checks) | S3a/S3b with an injected two-hit index (body:370-371) | **present** |
| indented-prose control | over-capture fixture is non-indented and cut off by the next header (`:231-239`) | S7c blank + indented prose (body:413-415) | **present** |
| four-class census | six buckets only | `four_class_totals` + `artifact_totals` + conservation | **present** |
| disposition leg | no per-token reason, no mapping list | `_reason` + 7 unresolved rows + 50 mapping rows | **present** |

The claim's word "confirmed" is accurate only as a **code-path** statement. O03's whole-corpus differential found 0 token-level differences and 0 entries with the triggering shape; 19 entries have `couples` as the last header field, so the trap is real for future edits but not a present miscount (`op/O03-defects-verify.md:83-110`). The LOG/SHONEN sentence must say "latent trap closed", not "over-capture corrected corpus-wide".

**Residual latent regression (X01 T1b).** The successor's docstring advertises a hyphen soft-wrap exception after a blank line, but the code cannot take it. On the fixture `- couples: ... `tone-` / blank / indented `prosody.md` ...`, the witness captures 2 tokens and the successor captures **0** (`cross/X01-trades.md:114-155`; O03 §7.1 found the same unreachability with a single-token fixture). Live incidence is 0, so the live census is not harmed, but the successor is **less total than its witness** on that shape. Because the body is pinned at `43ce341f…`, this is a successor-record note for the next resolver touch, not an edit now. It also means "zero tokens dropped" is true of the live corpus, not universally true of the rule.

### 2.4 The census artifact

O06's fenced block (`op/O06-census-artifact.md:213-974`) is the exact artifact. I extracted it and verified it independently:

```
schema kotodama-couples-census-v4   round 44   entries 223   refs 2730
four {ambiguous:0, direct:2556, fallback:166, unresolved:7} + artifact {glob-fragment:1} = 2730
fallback rows 50, occurrences sum 166
unresolved 7, ambiguous 0, glob 1
missing mapping paths []
all 12 checks true
file sha256 c0ee791a89883f0958c62fb46755397a6c8f8f64f0a26e1c31227b30b4940699
content_sha256 (sorted compact JSON minus date/content_sha256) = 3ee551fca0b5c88f8dacdf37a544fcd658a23bb7619c9f38501299f773d896a9
```

Both digests match O06's claims. The artifact carries `baseline_commit`, `entries`, the partition counts, a `corpus_fingerprint`, all 50 mappings with carrier lists, 7 reasoned unresolved rows, the glob row, the conservation identity and 12 computed checks. This is the best evidence object in the round.

Two provenance findings attach to it:

1. **The corpus fingerprint does not pin 20 direct refs.** The census's `direct=2556` includes 20 occurrences that resolve only against the lane root, not `corpus/knowledge`. Measured from the resolver over all 223 entries: 8 distinct non-corpus tokens — `AGENTS.md` ×11, `SKILL.md` ×2, `LOG.md` ×1, `SCORECARD.md` ×1, `corpus/README.md` ×2, `reports/round-20/readme/gaps.md` ×1, `reconcile.md` ×1, `verify.md` ×1. O06's `corpus_fingerprint` covers only the 223 corpus entries (`op/O06-census-artifact.md:251-253`), so those 20 refs are not pinned by the artifact. X00 measured the consequence directly: a corpus-only scratch root reads `2536/166/0/27`, not `2556/166/0/7` (`cross/X00-connector.md:72-94`). The filed artifact should add `measured_root` and either a `lane_root_refs` list (8 tokens, 20 occurrences, with digests) or a digest over the full 2730-token population. Without it, a future re-run can drift by 20 and the artifact cannot tell which root produced 2556.
2. **Two "corpus fingerprint" values are both correct under different newline rules.** O06's `7675c724…` hashes rows with a trailing LF; the r43/O10 anchor `444ff801…` hashes `"\n".join(rows)` with no trailing LF over the same 223 files. I reproduced both. This is a convention difference, not a contradiction; O09 now flags it (`op/O09-scribe.md:269-271`). The integrator must name the adopted rule rather than "fix" one value to the other.

### 2.5 What is not delivered

`tools/harness/basename-couples-resolver.py` does not exist at this cut (`ls` → no such file). The claim's `after_required` says "durable", so the honest verdict is **unprovable-but-better**: the body is evidence about bytes, not about the lane. O08's floor simulation proves the landed path shape reads the same census and names itself `tools/harness/basename-couples-resolver.py` (`op/O08-negative-proof.md:160-180`), but a simulation is not the durable path.

The witness demotion is complete **by record** — the successor docstring, O04's demotion spec, O07's parity receipt, and the O06 artifact's `tool.witness` — and no byte was edited (`d8d23a26…` at every cut). It is not machine-enforced: there is no instrument index under `tools/`, and the round's runner is absent. X01's T1 is the right reading: not a live fork (0 token diffs), but a naming/authority risk that the runner should close by asserting the witness digest, the absence of an import, and the 0-diff parity (`cross/X01-trades.md:79-110`).

### 2.6 O verdict

**unprovable-but-better at this cut; improved if and only if** the integrator applies the pinned bytes (one trailing LF), runs 27/27 and the 223 census from the landed path, files exactly one artifact (O06's §5, with the root/fingerprint addition), files the parity receipt and demotion record, and leaves the witness at `d8d23a26…`. No evidence on disk supports "harmed".

---

## 3. Claim C — the coverage move

### 3.1 State at this cut

Coverage is **unchanged at 223**; no corpus byte has moved. My checks agree with every seat:

```
$ find corpus/knowledge -name '*.md' | wc -l
223
$ for d in corpus/knowledge/*/; do ...; done
civilizations=94 culture-material=25 linguistics=25 myth-symbol=26 synthesis=29 verification=24
$ python3 -B reports/round-28/readme/sweep.py
rows 223 files 223; missing 0; topic_mismatch 0; orphan_rows 0; totals 223 True; footer_ok True; exit 0
```

### 3.2 The decisive conflict: K02's cartography vs K04/C01's dream

The two claim-C scouts named **different gaps**, and the difference is not cosmetic:

- **K02** selects `corpus/knowledge/culture-material/cartography-and-mapmaking.md` and explicitly **rejects dream/vision/trance as carried**: "Dream / vision / trance | ... | **named** r42 R2 | **carried — reject**" (`reports/round-44/scout/K02-gap-scout.md:78`; selection at `:85`). Its method: "A candidate is disqualified as **carried** if any prior round's scout/gap/plan registry already named it" (`:66`).
- **K04**, which could not see K02 at write time, names the same dream/vision/trance complex at the same slug (`reports/round-44/scout/K04-gap-verify.md:10`), re-measures the absence at 223, and argues it is not carried because r42 only *ranked* it and never landed it (`:161-166`).
- **C01** drafted the dream entry (final: 484 lines, fenced entry `108-395`, complete through §15 plus a `## 5` self-audit) and says explicitly: if K02 lands a different gap, "this draft is a **spare**, not the claim's landing; the integrator must choose one gap, not land both" (`reports/round-44/cov/C01-entry-draft.md:8`).
- **C05** now clears **both** paths and refuses to choose: "Both filed candidates are collision-free ... Claim C is `+1`, so exactly one may land" (`reports/round-44/cov/C05-collision.md:1,11-20`). Candidate A (cartography) has a seed/outline/shelf but **no entry body**; candidate B (dream) has the full fenced entry (`:15-16,92`). Its earlier first cut cleared only dream; the revision supersedes that.
- **C06** argues the permissive reading: "The claim's 'not carried' condition is satisfied by the fresh measurement, not by novelty of the idea" (`reports/round-44/cov/C06-scribe.md:164-166`).

I verified the prior-round provenance: r42's scout named R2 as **"Dream, vision and trance: the altered-state complex and the institutions that license it"** with the **same filename** `dream-vision-trance.md` (`reports/round-42/scout/K02-myth-gaps.md:216-259`). So the strict reading is factually grounded: the topic and slug were named in a prior round. The claim text is `"...a gap with NO current owner (verified by a fresh absence sweep at the 223 total, not carried from a prior round)..."` (`reports/round-44/claims.json:39`). Both readings are defensible:

- **Strict (K02):** "not carried" forbids a topic already named in a prior registry. Dream fails; cartography passes.
- **Permissive (K04/C06):** "not carried" forbids reusing a prior **draft/landing/ownership claim** without fresh measurement. Dream passes because r42 never landed it and K04 re-measured at 223.

This is the r43 defect class one level up. r43 failed because the lithic *owner* existed; r44's dream candidate has no owner but a prior *proposal*. The integrator must make an explicit ruling and record it in `validation.json`/LOG — silently adopting the permissive reading is exactly the kind of process drift R01-43-12 was meant to stop.

**Consequence for deliverability:** at this cut both candidates are collision-free, but only the dream candidate has a **draft**; cartography has a seed, section outline and source shelf (`scout/K02-gap-scout.md` §4.2-§4.4), not an entry body. If the strict reading is adopted, claim C is **blocked at this cut** (not enough evidence to land a lawful entry) unless a cartography entry body, C03/C04 audits and a collision re-run are produced. If the permissive reading is adopted, the dream entry can proceed only after C03/C04 (both absent) audit the final 484-line draft. Landing both is forbidden by the +1 contract and would repeat the r42 duplicate-topic incident.

### 3.3 The dream draft, reviewed as a draft

C01's file is now complete (484 lines; fenced entry `108-395`; §1-§15 plus a `## 5` self-audit outside the fence). The head block carries the eight established fields (`- gap filled:` at 111, `- topic:` 113, `- sources:` 115, `- couples:` 123, `- source:` 125, `- verified-at:` 127, `- recheck:` 129, `- scope:` 131), calibration is an in-body §13, and the entry states a boundary table against divination, ritual-liminality, animal-symbolism, music-instrument, death-afterlife, sacred registers, register law, linguistic anthropology, and the Australian Dreaming. The worked fixture is declared invented and non-canon. I spot-checked ten load-bearing citations (divination `:3,:52,:89,:126`, ritual-liminality `:111`, animal-symbolism `:57`, music-instrument `:96`, australia-aboriginal `:36`, linguistic-anthropology `:9`, semantics-pragmatics `:88`) — all resolve to the described content. The external shelf is honestly marked: the modern specialist works are `(to-verify)` and the entry is built from the in-corpus shelf (C01 sources block at line 115; K04 §4.5). The draft's `- couples:` block yields **15 distinct tokens, all `direct`**; a lawful dream landing would therefore make the post-C census `entries=224 refs=2745 direct=2571`, with the other classes unchanged (R02 measured 14/2744/2570 on an earlier 152-line cut; the final draft adds one direct target).

Three draft-level risks remain:

1. **The gap's "zero owners" is a boundary judgment, not a grep result.** `divination-omen-systems.md`'s topic line names "dream-oracles and incubation" as one of fourteen rows, and its H1 names "dreams" among the reading technologies (`corpus/knowledge/myth-symbol/divination-omen-systems.md:1,3`). K04/C01/C05/C06 all adjudicate this as an adjacent row, not ownership. That is defensible — the entry owns the state/induction/career/institution, not the reading — but C04 must accept the boundary explicitly, and the post-landing ownership re-check must not treat the word "dream" as a collision. A strict keyword gate would call this owned; the review needs the interpretation on record.
2. **The Australian Dreaming distinction** is handled in §1/§9/§13/§14 and is the right guard; C03/C04 should confirm the final text does not use "Dreaming" for sleep in a way that reads as a second owner.
3. **No draft-level audit exists yet.** C03 (source audit) and C04 (contract audit) are absent; C05 clears both exact paths but does not certify the prose. The claim's "audits PASS" cannot be verified at this cut.

### 3.4 README arithmetic — a correction to C05

The rev-2.4 prose vector `25/23/26/25/24/94` sums to **217**, not 223 (`corpus/README.md:11`; footer at `:544-548` is the correct `25/26/25/29/24/94`). C05 says the vector "puts `23` in the linguistics slot and `25` in the culture-material slot" (`reports/round-44/cov/C05-collision.md:226-229`). That slot assignment is wrong. The vector order is `[linguistics, myth-symbol, culture-material, synthesis, verification, civilizations]` (established by rev 2.3's `21/23/25/29/24/94 → 25/23/25/29/24/94` at `corpus/README.md:20` and the sweep's `PARTS` order). In the rev-2.4 vector:

- linguistics `25` — correct;
- myth-symbol `26` — correct (it moved 23→26);
- culture-material `25` — correct;
- **synthesis `25` — wrong; live is `29`** (the 29 was overwritten by a stray 25);
- verification `24`, civilizations `94` — correct.

So the only wrong slot is synthesis, and the sum is 217 because `29` became `25` (a 4-point loss) plus the myth-symbol move was written as `23→26` (a 3-point gain) against the old 220 total: 220 + 3 − 4 = 219? Let me not over-derive; the measured fact is the live vector is `25/26/25/29/24/94` and the rev-2.4 vector is `25/23/26/25/24/94`. Wait — if the vector order is [linguistics, myth-symbol, culture-material, synthesis, ...], then the rev-2.4 vector has myth-symbol `23` (not 26) in slot 2 and synthesis `25` in slot 4. It says "moved 23 → 26" but the vector's second slot reads `23`, and the third slot reads `26`. Hmm. Let me re-read the actual text: `the vector 25/23/25/29/24/94 → **25/23/26/25/24/94**`. If the order is [linguistics, myth-symbol, culture-material, synthesis, verification, civilizations], the after vector is linguistics 25, myth-symbol 23, culture-material 26, synthesis 25, verification 24, civilizations 94. That sums 217. But the prose says "`## myth-symbol/` moved 23 → 26" — so the editor intended the second slot to be 26, but wrote 23; and moved the 26 into the culture-material slot, and changed synthesis 29→25. That is *two* errors: myth-symbol slot not updated (23 instead of 26), and culture-material slot changed 25→26 (wrong), and synthesis 29→25 (wrong). Net: 25+23+26+25+24+94 = 217; correct 25+26+25+29+24+94 = 223. The differences: myth-symbol −3, culture-material +1, synthesis −4 = −6 (223−6=217). So C05's statement that "23 is in the linguistics slot and 25 in the culture-material slot" is still wrong (23 is myth-symbol, 26 is culture-material), but its broader point "moves the myth-symbol +3 into the culture-material slot while cutting synthesis 29→25" (K02 §5 line 314) is closer: the +3 appears in the culture-material slot (26 vs 25), and myth-symbol stays 23. C05 says "23 in the linguistics slot" — definitely wrong; the first slot is 25.

Let me get this exactly right for the review:
- Live/current correct vector: 25/26/25/29/24/94 (sum 223).
- rev-2.4 written vector: 25/23/26/25/24/94 (sum 217).
- Slot-by-slot (order L, MS, CM, S, V, C): written 25,23,26,25,24,94 vs correct 25,26,25,29,24,94. Errors: MS 23 (should 26), CM 26 (should 25), S 25 (should 29).
- So the after-vector failed to update MS to 26, moved the 26 into CM, and cut S from 29 to 25. Three slot errors, net −6.
- C05's claim "23 in the linguistics slot and 25 in the culture-material slot" is wrong on both counts: 23 is in MS, 25 is in S; CM holds 26.
- K02's line 314 says "it moves the myth-symbol +3 into the culture-material slot while cutting synthesis 29→25" — correct on CM and S, but it also left MS at 23 rather than 26; "moves" is fair.
- C06 §4.5 says the second vector sums 217 and the live footer is 25/26/25/29/24/94, without slot detail — correct.
- X00 §1.4 says the stale vector is 25/23/26/25/24/94 (sums 217), correct, no slot detail.

Good. I'll state the exact slot errors and correct C05. This is a precise reviewer value-add.

For C02's rev 2.5: correct vector after dream landing (myth-symbol 27) = `25/27/25/29/24/94` sum 224. The C02 draft must show arithmetic. It's absent.

### 3.5 C findings

- C-F1 (decisive): K02 vs K04 conflict; explicit ruling required; strict reading leaves no drafted lawful candidate.
- C-F2: C03/C04 absent; C05 clears both exact paths but does not choose or certify the prose; C06 summary predates K02/C01 (it says K02/C01 absent, which is now false). The integrator must not cite C06's status table as current.
- C-F3: README vector slot correction; C05 §5 misreads; C02 must compute.
- C-F4: sweep has no ownership leg (R01-43-8); green 224==224 cannot certify "genuinely unowned". Post-landing ownership re-check required.
- C-F5: divination boundary is interpretive; C04 must accept it explicitly.
- C-F6: external shelf `(to-verify)`; C03 must not let the draft present unread works as inspected.

### 3.6 C verdict

**unchanged at this cut.** The coverage axis stays at 223; nothing is harmed. **Improved** only if (a) the integrator records a ruling on "not carried", (b) one candidate is chosen, (c) C03/C04/C05 pass against the exact draft, (d) the entry lands as `A` with README rev 2.5, and (e) the post-apply sweep is 224==224 with the ownership re-check green. If the strict reading is chosen and cartography is to be the entry, a full draft/audit chain must be produced first; it does not exist at this cut.

---

## 4. Claim Ca — the pre-dispatch freshness gate

### 4.1 State at this cut

There is no **durable** gate and no filed demonstration: `tools/harness/` has no `claims-freshness.py`, `reports/round-44/calib/` is empty, and Ca01–Ca03 have no out file. There is, however, a **scratch-only prototype** at `.scratch/ca01/claims-freshness.py` (mtime 14:23 local), which R02 ran and I re-ran read-only. It is evidence that the method works, not that the claim is delivered; the claim's own threshold says "durable not `.scratch`".

### 4.2 The regression is real and reproducible

I built a scratch-only probe (`.scratch/r01/freshness-probe.py`) with one premise per clause, measured at the r43 baseline `7ceff59` via committed bytes, and a polarity field (the claim's asserted value). Output:

```
== r43 claim O ==
  durable couples resolver exists    measured=True   claim=False -> STALE
  wrapped field tokens               measured=('True', 4) claim=0 -> STALE
  VERDICT: STALE (both premises)
== r43 claim C ==
  myth-symbol count                  measured=26     claim=26   -> fresh
  corpus total                       measured=223    claim=223  -> fresh
  lithic topic owner                 measured=True   claim=False -> STALE
  VERDICT: STALE (ownership only)
== negative control (r44 O premises at c9f4eaa) ==
  four-class census authority absent measured=True   claim=True -> fresh
  corpus total                       measured=223    claim=223  -> fresh
```

The facts behind it: at `7ceff59` the tracked `tools/harness/couples-reference-extractor.py` exists at `d8d23a26…`, selftests 8/8, and reads the wrapped field as 4 tokens; `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md` exists and its topic line owns the lithic register. r43 O's `before` (`reports/round-43/claims.json:27`) is false; r43 C's `before` (`:40`) is false in its ownership conjunct while its counts (26/223) are true. This matches R01-43-12 (`reports/round-43/review/R01-review.md:400`) and r43's validation.

**The polarity lesson is the deliverable's core.** My first probe run marked O's first premise "fresh" because I encoded `asserted=True` for "resolver exists" when the claim asserts absence. A gate cannot infer polarity from prose; each clause must declare the measured state that makes it true. X01's naive gates make the same point quantitatively: a path-existence gate and a count gate flag **0 of 2** r43 stale claims; only a capability probe and a topic-ownership probe catch them (`cross/X01-trades.md:247-320`). A gate that hardcodes "no durable instrument" → stale passes the demonstration and fails the purpose.

**The scratch prototype: method works, delivery does not.** I ran `.scratch/ca01/claims-freshness.py --claims reports/round-43/claims.json` read-only. It prints `[O] STALE (0/2 premises hold)`, `[C] STALE (2/3 premises hold)` (both counts true; the `lithic` topic has 3 owner hits, all `mineral-stone-symbolism.md`), `[Ca] FRESH (1/1)`, `summary: 1 fresh, 2 stale, 0 unverifiable, 2 ungrounded`, then `REFUSE: claims O, C have a before already false at 7ceff59…; do not dispatch.` and exit 2. That is the required positive regression plus the Ca negative control, and it reads the baseline through git rather than the worktree — the right design. But its own `--selftest` exits 1 at **17/19**: `FAIL grep_absent hit fails` (a synthetic `corpus/knowledge/beta` fixture) and `FAIL seventeen checks collected (18)` (the assertion is stale). R02 additionally found a novel-phrasing false positive: "the llama-herding register slot is unbuilt" mines the topic as `register` and refuses against 51 owners (`review/R02-review.md:207-227,424-430`). The E1a family scan also counts `tools/gates/provenance-audit.py` — a gate whose text mentions a missing `- couples:` header — as a couples-family candidate. None of these changes the r43 verdict, but a red selftest and a false-positive path mean the prototype is not the durable deliverable.

### 4.3 Minimum durable contract (what I would accept)

1. A tool under `tools/harness/` (or a documented integrator step) with a machine-readable per-claim `before_checks` list: `{clause, probe_kind, target, expect, evidence_command}` where `probe_kind` is a closed set (`path_absent|path_present|grep_absent|grep_present|count_eq|sha256_eq|topic_owner_absent|capability_present`), evaluated at the claim's own `baseline_commit` via `git ls-tree`/`git show`, never against the worktree.
2. Per-clause semantics: a claim is `STALE` if **any** declared clause mismatches; `FRESH` only if all match; `could-not-evaluate` if no checks are declared. `could-not-evaluate` must not exit 0. Exit 0 only for all-fresh; exit 1 for stale; exit 2 for malformed input.
3. The r43 positive regression: O and C flagged, each with the failing clause and the measured value; the Ca claim in the same file **not** flagged (its `before` is true at `7ceff59` — the dispositions artifact is absent from that commit).
4. A negative control from r44's own claims at `c9f4eaa`: O's "no four-class authority" (true), C's "total 223" (true), Ca's "no mechanical check" (true) must not be flagged.
5. An anti-theater test: mutate the r43 O claim's tool name to the existing witness (`couples-reference-extractor.py`) and the C claim's numeric literals to the live values; both must still flag from capability/ownership, not from the literal text.
6. The tool must not write to `reports/round-43/**` or any filed byte; the demonstration is a new `calib/` artifact naming the tool digest and baseline.

### 4.4 Ca verdict

**unprovable-but-better at this cut.** The defect class is confirmed, the scratch prototype proves the method (r43 O and C stale, Ca fresh, exit 2 + REFUSE), and the fix is mechanically feasible; the durable artifact is absent and the prototype's selftest is red. **Improved** only when a durable tool with a green selftest, the r43 demo, the r44 negative control, and the anti-theater mutation test are filed and Ca02 independently reproduces the flags. A `.scratch` prototype, a red selftest, or a two-string lookup table is not improved.

---

## 5. Axis verdicts

| axis | verdict at cut | reasoning |
|---|---|---|
| **operability** | **unprovable-but-better** | The successor is a verified improvement over the six-class witness (four-class report, disposition leg, ambiguous/indented/glob controls, 0-diff parity) but the durable path is empty. On a byte-exact landing, **improved**. |
| **coverage** | **unchanged** | 223 entries, README rev 2.4, sweep green. One draft and one conditional collision clearance exist; no landing. The scout conflict must be ruled before any landing. |
| **calibration** | **unprovable-but-better** | The r43 stale-premises defect is confirmed, and the scratch prototype correctly flags O and C while leaving Ca fresh; no durable gate/demonstration exists and the prototype's selftest is red (17/19). |
| depth / adjacency / freshness | unchanged | Not claimed; `freshness_pause_in_force: true` (`claims.json:21`). A01 found no scope violation; the only corpus delta remains prospective. |

No axis is harmed by what is on disk. The risks are integration-order and evidence-selection risks, not present data errors.

---

## 6. Integration conditions (ordered)

1. **Land O first, byte-exact, and file the 223 census before C.** Apply `reports/round-43/op/O09-scribe.md:356-870` with exactly one trailing LF; verify `43ce341f…`; run `--selftest` (27/27) and `--census` (223/2730, 2556+166+0+7+1) from `tools/harness/`; file one artifact (O06's §5) with `round:44`, `tool_body_round:43`, `baseline_commit:c9f4eaa`, `entries:223`, `measured_root`, and the lane-root ref list or a full-token digest. Do not re-run the census after C and compare it to 2730.
2. **Rule the C conflict explicitly.** Record whether "not carried" is strict (K02) or permissive (K04/C06). If strict, do not land the dream draft; either commission cartography or report C `unchanged`. If permissive, record the ruling and the r42 R2 provenance in `validation.json`/LOG, then require C03/C04 to audit the exact dream draft before landing.
3. **If C lands:** one new file + `corpus/README.md` rev 2.5; vector `25/27/25/29/24/94` (sum 224); row byte-equal to the draft's `- topic:`; sweep 224==224; post-landing ownership re-check; `git status` shows `A` not `M`.
4. **File the Ca gate or record C as `unchanged`.** If filed, use the six-part contract above and file the r43 demonstration plus the r44 negative control. Do not claim "refuses to file" unless the tool exits non-zero on a stale claim.
5. **File the telemetry close.** S02's skeletons are sound: counters stay `null` until the native extract is landed; `open-at-seat-close` is not a close; the availability-close-44 must pin the observed record's digest (fixing r43's T7).
6. **Run the round validation out-of-tree** (the in-tree runner is absent and forbidden); file the receipt; do not infer acceptance from completed seats.

---

## 7. Findings register

| ID | claim | class | finding | evidence |
|---|---|---|---|---|
| R01-44-01 | O | delivery | The claim-named durable path is absent; the body is a verified draft, not a landed instrument. | `ls tools/harness/basename-couples-resolver.py` → not found; `op/O02-verify.md` §1; O08 §5 |
| R01-44-02 | O | evidence | The census artifact's corpus fingerprint does not pin 20 lane-root direct refs (8 tokens); a corpus-only replay reads 2536/27. Add `measured_root` + lane-root digests or a full-token digest. | my resolver enumeration; `cross/X00-connector.md:72-94`; `op/O06-census-artifact.md:251-253` |
| R01-44-03 | O | provenance | The body emits `round:43`; the artifact wrapper must carry 44 + `tool_body_round:43`. Do not edit the pinned body. | body:461; `op/O06-census-artifact.md:213-220`; `cross/X00-connector.md:131-146` |
| R01-44-04 | O | artifact spec | Two wrapper shapes were specified (O06 §5 verified `c0ee791a/3ee551` vs O09's earlier `ece6ecaf`); O09 now offers A/B. File exactly one, preferably O06's verified variant A. | `op/O06-census-artifact.md:209-210`; `op/O09-scribe.md:350-353` |
| R01-44-05 | O | latent defect | A blank-separated hyphen soft-wrap continuation drops all tokens in the successor (witness captures 2); 0 live incidence. Record as a successor note; do not claim universal zero-drop. | `cross/X01-trades.md:114-155`; `op/O03-defects-verify.md:221-229` |
| R01-44-06 | O | authority | Witness-only demotion is prose-only; no instrument index or runner assertion enforces it. Assert the digest, no-import, and 0-diff parity in the runner. | `cross/X01-trades.md:79-110`; `op/O04-witness-demotion.md` §2 |
| R01-44-07 | O | ordering | O's 223 arithmetic and C's 224 landing cannot both hold on one final tree; file O's census pre-C and label C's delta separately. | `cross/X01-trades.md:324-354`; `op/O06-census-artifact.md:997-1003` |
| R01-44-08 | O | scribe accuracy | O09's scribe says 18 entries carry `AGENTS.md` (measured 11) and lists `tempfile` as an import (not imported; `json`/`__future__` are). Use O02/O03/O06/O07/O08/O10, not the scribe summary, for numbers. | `op/O09-scribe.md:61,353`; my import/entry counts |
| R01-44-09 | C | process | K02 rejects dream/vision/trance as carried from r42 K02 R2 (same slug/topic); K04/C01/C06 use the permissive reading. An explicit integrator ruling is required; do not land both gaps. | `scout/K02-gap-scout.md:66,78,85`; `reports/round-42/scout/K02-myth-gaps.md:216-259`; `cov/C01-entry-draft.md:8`; `cov/C06-scribe.md:164-166` |
| R01-44-10 | C | evidence | Only the dream candidate has an entry body; cartography has a seed/outline/shelf. C03/C04 are absent; C05 clears both exact paths but does not choose or certify the prose; C06's status table predates K02/C01. "Audits PASS" is unverified. | `cov/C05-collision.md:1,11-20,92`; `cov/C06-scribe.md:7,174-185` |
| R01-44-11 | C | README | Rev-2.4 vector `25/23/26/25/24/94` (sum 217) has three slot errors vs live `25/26/25/29/24/94`: myth-symbol 23 (should 26), culture-material 26 (should 25), synthesis 25 (should 29). C05 §5 misidentifies the slots. C02 must compute, not copy. | `corpus/README.md:11,544-548`; `cov/C05-collision.md:226-229` |
| R01-44-12 | C | ownership | "Zero owners" is true of the state complex, not of the word `dream`; divination's topic line names dream-oracles/incubation as one row. C04 must accept the boundary explicitly; the post-landing re-check must not treat the word as a collision. | `corpus/knowledge/myth-symbol/divination-omen-systems.md:1,3,89`; `cov/C01-entry-draft.md` §1 |
| R01-44-13 | C | provenance | The modern dream/trance shelf is unregistered; every external item must stay `(to-verify)`. The draft does this correctly. | `cov/C01-entry-draft.md:118`; `scout/K04-gap-verify.md:159` |
| R01-44-14 | Ca | delivery | A scratch-only gate exists and correctly flags r43 O (0/2) and C (2/3; ownership false), leaving Ca fresh (exit 2 + REFUSE), but no durable gate/filed demo exists and its selftest is red at 17/19 (`grep_absent` fixture; stale check-count). Naive path/count gates flag 0/2; the durable gate needs typed per-clause probes with declared polarity, capability + ownership legs, and `could-not-evaluate` ≠ green. | `.scratch/ca01/claims-freshness.py` run by me; `review/R02-review.md:207-227`; `cross/X01-trades.md:247-320`; my `.scratch/r01/freshness-probe.py` output |
| R01-44-15 | Ca | positive | r44's own `before` lines are fresh at `c9f4eaa`: no four-class authority, 223 entries, no freshness tool. The round does not repeat r43's stale-premises defect manually; it still lacks the durable check. | my probes; `claims.json:26-28,39-41,51-53` |
| R01-44-16 | cross | scope/telemetry | No scope violation at cut: no corpus staging, no filed-byte edit, witness digest stable, all seat writes under declared out paths. S02's telemetry draft keeps counters `null` and fixes r43's close-digest gap. | `adj/A01-scope.md` §2-§10; `scribe/S02-telemetry-draft.md` T1-T9; `git status --porcelain` |

---

## 8. Evidence read and limits

**Read in full or in the cited sections:** `reports/round-44/claims.json`, `targets.json`, `telemetry/dispatch-declared.json`; K01, K02, K04; O02, O03, O04, O06, O07, O08, O09, O10; C01, C05, C06; X00, X01, X02; R01's own prior round, R02; S01, S02; A01; `reports/round-43/claims.json`, `validation.json`, `review/R01-review.md`, `op/O09-scribe.md`; `reports/round-42/scout/K02-myth-gaps.md`; `.scratch/ca01/claims-freshness.py` (read-only); `tools/harness/couples-reference-extractor.py`; `corpus/README.md`; `corpus/knowledge/myth-symbol/divination-omen-systems.md`; `corpus/knowledge/myth-symbol/mineral-stone-symbolism.md`.

**Commands I ran (read-only except `.scratch`):** `git rev-parse`, `git status`, `git ls-tree`, `git show`, `sha256sum`, `find`, `grep`, `wc`, `python3 -B` on the extracted resolver, the r42 witness, the C01 draft block, the scratch Ca gate, and my own probes (`parity-diff.py`, `freshness-probe.py`), the sweep, and a JSON re-derivation of O06's artifact.

**Limits.** (1) The wave was in flight; Ca01–Ca03, C02–C04, O01, O05, K03 and P01 had no out file at my cut. No verdict here should be read as certifying them; the scratch Ca gate is not an out file and is not durable. (2) I did not run `reports/round-44/run-validation.py` (absent; in-tree execution forbidden) or any filed round's runner. (3) C01's draft appeared in three states (261, 393, then 484 lines); I reviewed the final 484-line version, whose fenced entry is `108-395` and whose couples block yields 15 direct tokens. If it changes again, re-run the token count and C03/C04. (4) I did not re-adjudicate the domain content of the draft beyond spot-checking ten load-bearing citations; C03/C04 own the full audit. (5) The seal on any verdict is the integrator's post-landing measurement, not this file.

**Bottom line.** The O body is the round's real asset: byte-exact, 27/27, 0-diff parity, and a complete census artifact. It is not yet durable, so O is `unprovable-but-better` until the apply. C is the round's real hazard: two scouts, two gaps, and a claim whose "not carried" clause can be read to disqualify the only drafted entry. Ca is the round's real debt: the scratch gate proves the method (r43 O/C stale, Ca fresh, exit 2 + REFUSE), but it is not durable and its selftest is red, so the claim is `unprovable-but-better`, not delivered. No axis is harmed at this cut; the integrator's ordering and selection decisions decide whether that stays true.
