- Seat: O05 | verifier | claim O | date 2026-10-19 | baseline ac47c78

# O05 — second isolated verification + adversarial fixture battery (claim O)

Assignment (verbatim, `reports/round-42/targets.json:69-73`): "Second isolated
verification + adversarial fixture (a hand-crafted wrapped field with a planted
phantom)." Out: `op/O05-traps.md`.

**Status: verification performed; claim O's threshold is met only under one
unwrap rule, and as literally written ("4/4 targets") the threshold is
under-specified — a false green.** At this seat's cut the wave had landed no
implementation (`reports/round-42/op/` holds only `O09-scribe.md`,
`O10-gap-fill.md`), so this seat verified the *defect* and the *candidate rules*
independently rather than verifying a sibling's patch. Everything below is
measured on the live tree and on a `git archive` copy at `ac47c78`.

## 1. Independent reproduction of the N6 defect (D1)

Read-only, from the lane root, `export TMPDIR=$PWD/.scratch
PYTHONDONTWRITEBYTECODE=1`. Two independent evidence paths were used: a
from-scratch harness (`.scratch/o05/verify-n6.py`, this seat) and the *filed*
r19 instrument loaded by path.

**(a) The filed extractor returns nothing.** Loading
`reports/round-19/audit/entry-audit.py` (sha256
`e7992c325a479aa7415c42722a034a95a9ea342a58367ead9cd2636a5a62830c`) and calling
its own `couples_targets()` on the live entry returns
`resolved=[] unresolved=[]` — **zero tokens**, exactly D1. Its capture regex is
`re.search(r"^- couples:\s*(.*)$", text, re.M)` at `:75`: single physical line,
no continuation. The captured string is
`'language (this file, core method); myth (divine/true names, taboo'` — no
`.md` token at all.

**(b) The field names four targets.** `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
(sha256 `b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b`),
six physical lines. Its last two lines read:

```
:76  ... prospective sibling files: sound-change.md, tone-
:77  prosody.md, sound-symbolism.md, writing-systems.md
```

The four named `.md` targets are `sound-change.md`, `tone-prosody.md`,
`sound-symbolism.md`, `writing-systems.md`. **The line break falls inside a
filename**: `tone-` + `prosody.md` is one token, `tone-prosody.md`. Existence:
`sound-symbolism.md` and `writing-systems.md` exist in
`corpus/knowledge/linguistics/`; `sound-change.md` and `tone-prosody.md` do not
(`ls`, this seat). The real name is confirmed by the entry's own body at
`phonetics-phonology.md:279` — "Natural partners: `sound-change.md` (diachrony →
§5), `tone-prosody.md`".

**(c) The wrapped field is singular — Ca04's owed corpus census.** Scanning all
220 `corpus/knowledge/*/*.md` for a `- couples:` line followed by indented
non-blank continuations: **exactly 1** entry has one
(`linguistics/phonetics-phonology.md:72-77`, 5 continuation lines). Ca04 left
this `to-verify` (`reports/round-39/calib/Ca04-verify.md:114`); it is now
measured. 220 entries also have exactly one `^- couples:` line each — no entry
has a second, in-body or fenced `couples` line that a naive parser could
mistake for the header field.

## 2. The unwrap rule decides the token — and the count cannot tell them apart

Five candidate rejoin rules were run over the same live block. All are
in-memory; none writes.

| rule | definition | tokens from `:72-77` | verdict |
|---|---|---|---|
| A | r19 single line | `[]` | **the defect** |
| B | space-join (`" ".join`) | `prosody.md`, `sound-change.md`, `sound-symbolism.md`, `writing-systems.md` | 4 tokens, **1 phantom** |
| C | newline-join (C14 `:236` `"\n".join`) | same as B | **same phantom** |
| D | **plain-concat** (`"".join`) | `sound-change.md`, `sound-symbolism.md`, **`tone-prosody.md`**, `writing-systems.md` | **4/4 real — correct** |
| E | de-hyphen join (drop `-`) | `toneprosody.md`, … | fabricates a token |

**The false green, stated precisely.** Under B/C and under D the field reads
**4 tokens**, of which **2 are `direct` and 2 `unresolved`** — *identical
tallies, different token sets*. Corpus-wide the two rules are
indistinguishable by count too:

```
space-join   : direct=2337 fallback=163 ambiguous=0 unresolved=8  refs=2508
plain-concat : direct=2337 fallback=163 ambiguous=0 unresolved=8  refs=2508
```

Both are green on every count threshold claim O states. The difference is a
token *identity*: `prosody.md` (a phantom split off the real name) versus
`tone-prosody.md`. **Claim O's acceptance test as written — "the wrapped field
reads 4/4 targets" — passes on the wrong fix.** The landed verification must
assert the token *set* (or that `prosody.md` is absent and `tone-prosody.md`
present), never a count.

## 3. The live gate carries the identical defect (stronger than "a filed tool is wrong")

Claim O leaves the host to the wave. There are **three** single-line hosts, not
one, and the load-bearing one is **live**:

| host | line | capture |
|---|---|---|
| `reports/round-19/audit/entry-audit.py` | `:75` | single line |
| `reports/round-27/audit/entry-audit.py` (sha256 `fb589b28…`) | `:275` | single line |
| **`tools/gates/provenance-audit.py`** (sha256 `8a96aaf4…`, **live**) | `:244-260` | block, joined `" ".join(...)` at `:259` = **rule B** |

Running the live gate's own `field_block()` on the live entry (imported by path,
read-only) emits the corrupted value:

```
... prospective sibling files: sound-change.md, tone- prosody.md, sound-symbolism.md, writing-systems.md
```

`tone- prosody.md` → the same `prosody.md` phantom. So the corpus's only
**live** gate that reads a `couples` continuation block carries the defect the
queue row attributes to an archived instrument. Scope note, so this is not
over-claimed: the live gate does not tokenize `couples` — its finding vocabulary
is `missing-couples`/`empty-couples` only (`tools/gates/provenance-audit.py:102-103`),
so the defect is **latent, not currently mis-gating**. Confirmed live:
`python3 -B tools/gates/provenance-audit.py --selftest` → exit 0, `SELFTEST OK`
(7 fixtures); `python3 -B tools/gates/provenance-audit.py
corpus/knowledge/linguistics/phonetics-phonology.md` → exit 0, `findings=0`.
`tools/harness/` and `tools/` carry no other couples resolver.

## 4. Adversarial fixture battery — 16 fixtures × 3 extractors

Synthetic, in-memory; every fixture's sha256 recorded below. Each is a complete
minimal entry header so a parser can be exercised unmodified. `r19` = single
line, `B` = space-join, `D` = plain-concat.

| # | fixture | sha256[:16] | r19 | B (space-join) | D (plain-concat) | expected | B honest? | D honest? |
|---|---|---|---|---|---|---|---|---|
| F1 | live field verbatim | `b4f9b00384bc6840` | `[]` | `prosody.md`, sound-change, sound-symbolism, writing-systems | sound-change, sound-symbolism, **tone-prosody**, writing-systems | 4 real | **no (phantom)** | **yes** |
| F2 | same field unwrapped | `a88f9991143d4df4` | `[]` | 4 real | 4 real | 4 real | yes | yes |
| F3 | planted phantom, wrapped | `b932edaf14b62c79` | 2 (misses 2) | 4 | 4 | 4 (2 real, 2 phantom) | yes | yes |
| F4 | planted phantom, single line | `331c44f835865df7` | 4 | 4 | 4 | 4 | yes | yes |
| F5 | wrapped token, live shape | `1a189422222f6089` | 1 | 3 (1 phantom) | 3 real | 3 real | **no** | yes |
| F6 | `writing-` + `systems.md` | `825ea2161bd1b7be` | `[]` | `systems.md` | `writing-systems.md` | 1 real | **no** | **yes** |
| F7 | glob fragments `*-gate.md` | `d7c0f4bc8d23e8a4` | `-gate.md` | `-gate.md` | `-gate.md` | not a couples finding (policy §5.6) | must not count | must not count |
| F8 | sub-bullet after field | `69485cdd10dedce3` | 1 | 1 | 1 | 1 (no over-capture) | yes | yes |
| F9 | brace across wrap | `a0df6d5ff1f5d6ea` | 2 | 3 (`beta}.md` broken) | 4 (`alpha.md`,`beta.md` expanded) | 4 | **no** | yes |
| F10 | empty field | `e8a286dab2ef2dd1` | `[]` | `[]` | `[]` | `[]` | yes | yes |
| F11 | hyphen-led continuation | `bd16a6cefec7aed8` | 1 | 2 | 2 | 2 | yes | yes |
| F12 | deep wrap, phantom mid-block | `193441f12b06b935` | `[]` | 1 | 1 | 1 | yes | yes |
| F13 | wrap **inside** a name | `52adec384714a7a5` | 1 | 2 (1 phantom) | 2 real | 2 real | **no** | yes |
| F14 | wrap **at a word boundary** between two real filenames | `2ccf2c364a83d6de` | 1 | 2 (`systems.md` phantom) | 2 real | 2 real | **no** | yes |
| F15 | blank line then indented prose | `302dad7e97ce4305` | 1 | 1 | 1 | 1 (no over-capture) | yes | yes |
| F16 | tab-indented continuation | `550754f243b388b8` | 1 | 2 | 2 | 2 | yes | yes |

**The planted-phantom negative (F3) behaves as required.** A hand-crafted
wrapped field naming `./planted-phantom.md` on the first line and
`./also-phantom.md` / `../nowhere/ghost.md` on continuations: the r19 extractor
finds only the **2 tokens on line 1** and silently loses both continuation
phantoms; B and D both recover all 4. F4 is the single-line control — all three
rules agree at 4, so the fixture battery is sensitive to the wrap and not to the
phantom strings alone.

**D is the better rule, but the corpus cannot prove it — and the wrap convention
is *not* recoverable from the text.** D (plain-concat) is correct on every
fixture where B fails (F1, F5, F6, F13, F14), so the rule choice is not a coin
flip. What the corpus cannot do is *establish the convention*. Two facts, both
measured:

- **D happens to be right on F14** (the break at a word boundary between two
  real adjacent filenames, `sound-symbolism.md` + `writing-` + `systems.md`):
  concat reads `['sound-symbolism.md', 'writing-systems.md']`, space-join reads
  `['sound-symbolism.md', 'systems.md']`. But D is right here only because the
  trailing `-` of `writing-` *belongs to* the name. **A genuine two-token list
  wrapped after a hyphen would be mis-merged by D** — no fixture in this corpus
  exercises that, and the corpus's 220 basenames contain **zero** hyphen-stem
  names and **zero** hyphen-suffix pairs, so nothing in the data adjudicates it.
- **Resolve-disambiguation agrees with D here, but is not a decision procedure.**
  The natural repair — "prefer the join whose tokens resolve" — was tested. On
  the corpus today it selects D: on F13, space-join resolves 1/2
  (`register-consistency.md` is not a basename) and concat 2/2; on F14,
  space-join resolves 1/2 (`systems.md` is not a basename) and concat 2/2. So it
  is *consistent* with D on every fixture. It is still not a decision procedure:
  its verdict is a function of the basename index, not of the text. **Make
  `systems.md` a corpus basename and F14 flips to 2/2 for space-join too**, at
  which point the heuristic has no basis to prefer the correct join. The
  heuristic's correctness is contingent on the corpus's accidental basename
  inventory, which is exactly the kind of dependency a stated rule exists to
  remove.

**Recommendation (revised):** adopt D as the stated rule, and state its
assumption explicitly — *a soft wrap in a `couples` field occurs inside a
hyphenated token, so the break's hyphen is part of the token and the two halves
join with no separator*. Do **not** present resolve-disambiguation as the
discriminator. Add a re-run trigger: if a `couples` field ever wraps at a
boundary between two adjacent tokens, the rule must be re-adjudicated. With one
wrapped field corpus-wide, this is a *policy* choice recorded as such, not an
empirically forced inference — and the landed tool's selftest must carry F13 and
F14 so a future rule change that re-introduces the space-join split is caught.

**Over-capture.** The live gate skips blank lines (`tools/gates/provenance-audit.py:250-251`
`if not following.strip(): continue`), so indented prose separated from the
field by a blank line is absorbed into the field value (F15, verified against
the live `field_block`). The C14-shaped parser (stop at blank) does not. On the
real corpus this changes nothing today (0 entries differ — measured), but it is
a latent over-capture for a future entry. The fix's block parser should stop at
a blank line, not skip it.

## 5. Isolated second verification (git-archive copy, `ac47c78`)

Per the isolation-replay protocol's shape (`reports/round-39/calib/isolation-replay-protocol.md`
§2 I2/I3) — never a filed runner, never in-tree:

```
git archive HEAD | tar -x -C .scratch/o05/iso     # iso tree at ac47c78, 220 entries
```

Run inside the copy with `TMPDIR=$PWD/.. PYTHONDONTWRITEBYTECODE=1`:

- **Filed r19 instrument in isolation** reproduces the defect: on the live
  wrapped field `couples_targets → resolved=[] unresolved=[]`; full corpus
  `entries=220 resolved=2435 unresolved=172 refs=2607` (the 172 = 166 fallback
  + 6 unresolved under the documented-only resolver, i.e. no basename fallback
  — consistent with r19 semantics).
- **This seat's reference implementation** of the block parser + rule D
  (`.scratch/o05/ref-fix.py`, plain-concat, stops at a blank line) run in the
  copy returns:
  `entries=220 refs=2611 -> direct=2437 fallback=166 ambiguous=0 unresolved=8`,
  arithmetic `2611 = 2437 + 166 + 0 + 8 OK`, and the wrapped field reads
  `['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']`
  (2 direct, 2 unresolved). The same fixtures were re-run against it inside the
  copy: F1/F5/F6/F13/F14 read the real tokens, F3 reads all 4 phantoms, F8/F15
  do not over-capture.
- **The iso copy produced the identical numbers as the live tree**, so the
  result is not an artifact of the live checkout's state.
- Sentinels after all runs: live `git status --porcelain` → only
  `?? reports/round-42/`; filed bytes re-hashed unchanged —
  `reports/round-39/calib/Ca03-basename-policy.md` `125ede77…`,
  `reports/round-19/audit/entry-audit.py` `e7992c32…`,
  `reports/round-27/audit/entry-audit.py` `fb589b28…`,
  `tools/gates/provenance-audit.py` `8a96aaf4…`,
  `corpus/knowledge/linguistics/phonetics-phonology.md` `b4f9b003…`. No
  `reports/round-42/run-validation.py` exists and none was executed.

## 6. The corrected census and its arithmetic — closes against r39 exactly

Claim O asks for "the r39 policy's 2504 = 2335 + 163 + 0 + 6 becomes the
corrected baseline". The r39 figure is at 212 entries
(`reports/round-39/calib/Ca03-basename-policy.md:268`). This seat recomputes at
**the same 212-entry scope** by excluding the 8 entries added since
`dfb0719` (`git log --diff-filter=A dfb0719..HEAD -- corpus/knowledge` → 8 files,
0 deletions, 0 renames):

```
212 entries, rule D (plain-concat): direct=2337 fallback=163 ambiguous=0 unresolved=8  refs=2508
```

Every delta is attributable, and the arithmetic closes:

```
2335 + 2 = 2337 direct       (the wrapped field's 2 existing targets)
 163 + 0 =  163 fallback     (unchanged — the field names no basename)
   6 + 2 =    8 unresolved   (sound-change.md, tone-prosody.md)
2504 + 4 = 2508 refs
```

**The wrapped field contributes exactly 4 tokens: 2 direct + 2 unresolved**, so
the r39 policy's filed Part-2 numbers are under-counts by exactly that field —
which is the mechanism D1 named. The 8 unresolved are 7 distinct:
`-gate.md` ×1 (policy §5.6 glob fragment), `../linguistics/phonology-sanity.md`
×2 (the r19 X26-1 phantom, still live in two entries — a **wrong-path corpus
defect**, since `corpus/knowledge/verification/phonology-sanity-gate.md` exists
and is already cited on the same line), and the 5 prospective seeds
(`phonology-basics.md`, `naming-and-onomastics.md`, `honorifics-and-register.md`
from `language-contact.md:7`; `sound-change.md`, `tone-prosody.md` from the
wrapped field). **Zero phantom attributions remain under D** — the two tokens
the count-equal B/C rules invent (`prosody.md`) and the delete-hyphen rule
invents (`toneprosody.md`) are both absent.

The full current-tree count (220 entries) is
`2611 = 2437 + 166 + 0 + 8`; the 103-token growth from 2508 decomposes cleanly
into the 8 new entries (100 direct + 3 fallback), so no third source of change
exists.

## 7. Verdicts for claim O's threshold

| claim O element | verdict | basis |
|---|---|---|
| "the wrapped field reads 4/4 targets" | **met only under rule D; the test as written is a false green** | §2 — B/C also read 4/4 |
| "the corrected census reproduces the r39 policy's arithmetic minus the phantoms" | **met** | §6 — `2508 = 2337+163+0+8`, closes exactly |
| "zero phantom attributions remaining or each dispositioned" | **met** | §6 — 0 phantoms under D; all 8 unresolved dispositioned |
| "two independent verifiers" | **this seat is the second evidence path**; O04 is the first | §1/§5 — independent harness + filed instrument, live + iso |
| "selftest green" | **cannot evaluate** | no landed tool at this cut (§Status) |

The claim is **admissible only with the acceptance test amended** to assert the
token set, and only if the landed parser breaks at a blank line and states its
wrap rule. Under the rule the wave is most likely to reach for (space-join, the
live gate's current behaviour) the claim's own threshold passes while the census
is wrong.

## Owed

- **Integrator — amend claim O's threshold.** Replace "reads 4/4 targets" with
  an identity assertion: the wrapped field's token set equals
  `{sound-change.md, tone-prosody.md, sound-symbolism.md, writing-systems.md}`
  and `prosody.md` is absent. A count assertion cannot distinguish the correct
  fix from the wrong one (§2). This is a `reports/round-42/claims.json:18`
  wording matter, which only the integrator may change.
- **Integrator — state the wrap rule and its assumption.** Rule D
  (plain-concat) is the correct rule and is right on every fixture where
  space-join fails, but it is **not empirically forced** by a corpus with one
  wrapped field. The landed tool must state the assumption explicitly (a soft
  wrap occurs inside a hyphenated token; the break's hyphen belongs to the
  token) and carry the F13/F14 controls so a boundary-break regression is caught.
  Resolve-disambiguation is **not** a decision procedure: it agrees with D on
  today's corpus only because `systems.md` is not a basename; add one and F14
  scores 2/2 for both joins (§4).
- **Integrator — the block parser must stop at a blank line**, not skip it, or
  the live gate's over-capture (F15) is carried into the fix
  (`tools/gates/provenance-audit.py:250-251`).
- **Integrator — the live host.** `tools/gates/provenance-audit.py:259` is a live
  `" ".join` and is the natural fix site; the two filed instruments
  (`reports/round-19|27/audit/entry-audit.py`) are archived readings the
  non-goal bars editing in place. Whether the fix lands at the live gate, a new
  `tools/harness` checker, or a successor resolver is the wave's/integrator's
  choice — this seat confirms all three hosts and their exact lines.
- **to-verify — the fifth class.** The r39 policy's four classes cannot hold the
  5 prospective seeds (`language-contact.md:7` "sibling knowledge files **to
  seed**"; the wrapped field's "**prospective** sibling files"). Neither
  `unresolved`-as-defect nor `direct` is honest for a declaration the corpus
  intends to grow. Independently observed here; disposition is the policy
  successor's, not this seat's.
- **to-verify — the `../linguistics/phonology-sanity.md` wrong-path defect** is
  a *corpus byte* matter (two entries). Drafted, not staged — this seat never
  stages under `corpus/`.

## Citations

- Claim + thresholds: `reports/round-42/claims.json:13-18` (`:14` the fix and
  census wording, `:18` the 4/4 threshold); seat + out `reports/round-42/targets.json:69-73`.
- Defect origin: `reports/round-39/calib/Ca04-verify.md:78-93` (D1), `:114`
  (the owed full recount), `:123` (C14 block parser pointer), `:131-133` (D1
  instance). Queue row: `reports/round-40/op/defect-queue-v2.json:361-369`.
- Policy: `reports/round-39/calib/Ca03-basename-policy.md:54-65` (§1 extraction,
  `:56-57` single physical line), `:67-88` (§2 four classes), `:137-143` (§5.6
  glob fragments), `:268` (the filed Part-2 numbers).
- Hosts: `reports/round-19/audit/entry-audit.py:31,74-96` (`:75` single-line
  capture); `reports/round-27/audit/entry-audit.py:274-286` (`:275` same);
  `tools/gates/provenance-audit.py:244-260` (`:250-251` blank-line skip, `:256`
  continuation append, `:259` `" ".join`), `:102-103` (finding vocabulary).
  C14 lineage: `reports/round-35/cov/C14-audit-6-10.md:227-236` (`:236`
  `"\n".join`), `:249-288`.
- Field: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`
  (sha256 `b4f9b00384bc6840bdd1d7d7e7ae9bbb127a2fd1f5010c98d5b253df65d7776b`),
  `:279` (the body's own `tone-prosody.md` confirmation);
  `corpus/knowledge/linguistics/language-contact.md:7` (the 3 prospective seeds);
  `corpus/knowledge/synthesis/typed-label-routing-workflow.md:16` and
  `corpus/knowledge/verification/label-channel-routing-verification.md:14` (the
  `../linguistics/phonology-sanity.md` wrong-path, ×2);
  `corpus/knowledge/verification/gate-frozen-run-standard.md:15` (glob fragment).
- Isolation protocol shape: `reports/round-39/calib/isolation-replay-protocol.md:26-40`
  (§2 I2/I3 invariants).
- Commands (this seat, 2026-10-19, lane root unless noted, all read-only,
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):
  (a) `python3 -B .scratch/o05/verify-n6.py` — Part 0 the 5 rules on the live
  block; Part 1 the 16-fixture battery × 3 extractors; Part 2 the 4 corpus-wide
  recounts (captured `.scratch/o05/verify-n6.out`, `.scratch/o05/final-battery.out`);
  (b) the filed r19 instrument loaded by path, `couples_targets` on the live
  entry → `resolved=[] unresolved=[]`; full corpus → `220 / 2435 / 172 / 2607`;
  (c) `git archive HEAD | tar -x -C .scratch/o05/iso`, then
  `python3 -B ref-fix.py` inside the copy → `220 refs=2611 -> direct=2437
  fallback=166 ambiguous=0 unresolved=8`, arithmetic OK;
  (d) `python3 -B tools/gates/provenance-audit.py --selftest` → exit 0,
  `SELFTEST OK: 7 fixture file(s) …`;
  (e) `python3 -B tools/gates/provenance-audit.py
  corpus/knowledge/linguistics/phonetics-phonology.md` → exit 0, `findings=0`;
  (f) the live `field_block` imported by path on the live entry → the
  `tone- prosody.md` corrupted value;
  (g) corpus scans: 220 entries, exactly 1 with a wrapped `couples` field,
  exactly 1 `^- couples:` line per entry, 0 hyphen-suffix basename collisions,
  0 entries ending a couples line in `-` other than the `tone-` split;
  (h) `git log --diff-filter=A dfb0719..HEAD -- corpus/knowledge` → 8 added,
  0 deleted, 0 renamed; (i) sentinels §5. No filed byte was edited; no
  `reports/round-*/run-validation.py` was executed in-tree; no git, network, or
  install action.
