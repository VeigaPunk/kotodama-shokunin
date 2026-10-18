# R27-D20 — review 4 of 4: the round-26 named gaps, closed or the delta named

- **Seat:** R27-D20 (reviewer 4 of 4), round 27, loop 3 build 3 of 4, claim **D**
  `register-law` (`reports/round-27/claims.json`).
- **Date:** 2026-10-18. Declared baseline `4f09c990d4c17f23b5e2cda0871f81db875635fc`
  (round-26 admit); lane HEAD `b95fca1e40f32f7346937ab6426f9ccca60e319f`.
  Measurement stamp **2026-10-18T19:33:47Z** (`date -u +%FT%TZ`).
- **Review target:** the **two gaps round 26 named** and the round-27 claim's
  closure of them, against the delivered bytes:
  - **`RD-5c` / `RL-6`** — "the delivered tree has **no component that owns a
    register law** … someone must own it" (`reports/round-26/register/review.md`
    §6.3, `reports/round-26/register/design.md:232`).
  - **`RD-4` / `RL-3`** — "the delivered gate's `syllabify` disagrees with
    `design-language.md:191-196`'s stated maximal-onset algorithm on **15 of 62**
    delivered forms" (`reports/round-26/register/review.md` §5,
    `reports/round-26/register/design.md:229`).
- **Write scope:** this file only, plus gitignored scratch under
  `.scratch/r27-d20/`. `export TMPDIR=$PWD/.scratch` preceded every scratch
  write. **No component, packet, tool, gate, fixture, pin or filed rounds 8–26
  byte was written; no commit, no push.**
- **Canon:** NON-CANON engineering evidence. A closure recorded here is a
  **measurement**, not an acceptance; the parent owns admission.

**Assignment.** Reviewer 4 of 4: *the round-26 named-gap closure recorded.* This
file states the closure condition per gap, tests it against the delivered bytes,
records the closure with its evidence, and names every **residual delta** so the
round cannot close on wording. It also states what would be a **false closure**,
because a gap can be "closed" by re-wording the gap rather than by landing the
thing.

**Verdict in one line.** `RD-5c`/`RL-6` is **closed** — the law now has an owning
component, is wired deterministically, reaches the packet field-for-field, and
the closure is **recorded in three round-27 artifacts** (`law/design.md:39`,
`law/impl-1.md:28`, `law/review.md`) — while `RD-4`/`RL-3` is **partly closed**:
the cluster class is fixed and the design's named trap is rejected, but the
diphthong class survives, so the correct closure for it is **"delta named"**, not
"delta zero". A closure that read the second as complete would be a false
closure, and §4 says why.

## 1. The closure condition, stated so it can fail

| gap | closure condition | what would be a **false** closure |
|---|---|---|
| `RD-5c`/`RL-6` | a component **declares** the law block in its own `packet_keys`, **carries** the rows, and the packet's rows are that component's rows **field for field**; the round-27 artifact **records** the closure by id | the law block exists but is assembled from the assembler's global key list (not a component), or the packet's rows differ from the component's, or the closure is asserted in prose while no component owns it |
| `RD-4`/`RL-3` | **one algorithm**: the gate agrees with the design's stated algorithm on **every** delivered form, and a form the design calls correct is not graded red | the disagreement count drops but a residual class remains; or the fix is verified only against an instrument that shares the residual reading |

## 2. `RD-5c` / `RL-6` — CLOSED

**Measured, lane root, `TMPDIR=$PWD/.scratch`, 2026-10-18T19:33:47Z.**

| leg | command | result |
|---|---|---|
| a component owns the block | `grep -n "packet_keys" examples/culture-d4/components/13-register-law.yml` | `packet_keys: [register_law]` at `:18`; the block at `:29` |
| the runner names the owner | `python3 reports/round-27/run-validation.py --check` → `law_blocks.declaring_components` | `[{block: registers, path: …/04-lexicon.yml, rows: 4}, {block: register_law, path: …/13-register-law.yml, rows: 5}]` |
| the packet's rows **are** the component's | same runner → `component_ownership` | `register_law`: `component_rows: 5`, `ids_equal: true`, `rows_equal: true`; `registers`: `component_rows: 4`, `ids_equal: true`, `rows_equal: true` |
| the contract declares the block | `grep -n "register_law" examples/culture-d4/components/01-brief.yml` | `C-13` at `:161`; `record_fields.register_law: [id, register, axis, kind, act, speaker, holder, force, consequence, design_row, evidence, follows]` at `:183` |
| every landed row carries every declared field | this seat's own field check | `declared but absent: []`; `landed but undeclared: ['cite']` (an extra, harmless) |
| the closure is **recorded** | `grep -rn "RL-6" reports/round-27/law/*.md` | `law/design.md:39` ("**This design closes RD-5c / RL-6**"), `law/impl-1.md:28`, `law/review.md:98,336` |
| the runner's own token gate agrees | `artifact_tokens` | `names_rl6: true`, `names_law: true` |

**The law is not merely re-stated prose.** Each row carries
`act` / `holder` / `force` / `consequence` / `axis` / `kind` / `evidence` /
`follows` / `cite` / `design_row`, so the five round-26 design statements became
machine-readable records:

```
register_law RGL-01..05   kind ∈ {admissibility, exclusion, asymmetry, no-segment, era}
                          keys = [act, axis, cite, consequence, design_row, evidence,
                                  follows, force, holder, id, kind, register, speaker]
```

### 2.1 The residual delta on `RD-5c` — the law has no teeth (named, not hidden)

The gap round 26 named was **ownership**, and ownership is closed. A **second,
smaller gap** is exposed by closing it, and this review names it so the round
cannot read "closed" as "enforced":

- **no delivered gate replays the law rows.** Four planted violations (an oath
  in-register, an out-of-slot stamp form, a guest-roll erasure, a widened
  holder) each produce **zero** new findings in every delivered gate; the argot
  gate reads `exit 0, violations=0` on all four, identical to the clean packet
  (`D17` §1).
- **the assembler does not validate the block.** Measured A/B in isolated
  copies: stripping the `id` from a `register_law` row assembles **exit 0**;
  the same edit to a `lexicon` row refuses **exit 2** (`D17` §3). `register_law`
  is in neither `PACKET_KEYS` nor `RECORD_FIELDS`.
- **the independent law instrument cannot distinguish by exit code.** `x59`
  reports two holds on the **clean** packet (`L6b-HOLD`, `L9-HOLD`) and exits 1
  on the clean tree, so its exit code is `1` both clean and tampered; only the
  era plant moves the finding set (`L4-FAIL`).

**This is a declared limit, not a hidden one.** The component says so in its own
`law_binding.enforcement`: *"no gate executes these rows … The rows are a
declared law with named non-execution, not a claim of enforcement."* That is the
standard this lane holds, and this review **confirms** the statement rather than
contesting it.

## 3. `RD-4` / `RL-3` — PARTLY CLOSED; the delta is named

**The cluster class is fixed.** The gate moved `5b5abe78…` (840 lines, selftest
21/21, **no** legality predicate) → `b5406bcdaf41c595…` (928 lines, selftest
**27/27**, `is_legal_syllable` at `:217`). Measured before → after:

| form | pre-fix | landed | design |
|---|---|---|---|
| `tikmes` | `['ti','kme','s']` | **`['tik','mes']`** | `['tik','mes']` |
| `ker` | `['ke','r']` | **`['ker']`** | `['ker']` |
| `saalumi` | `['saa','lu','mi']` | `['saa','lu','mi']` | `['saa','lu','mi']` |

The design's named trap (`saalum` as `head2(saalumi)`) is rejected under every
reading, and the **verdict inversion round 26 measured on the cluster class is
corrected**: at `5b5abe78…` a design-correct form read `violations=1`; at
`b5406bcd…` it reads `violations=0` and the wrong form reads `violations=1`
(`D18` §2, Pair A).

**The diphthong class survives.** `ai`/`au` are still two nuclei:

```
head2 disagreements (gate vs the design's stated algorithm):  3 of 70
   L-48 haitun  gate=hai    design=haitun
   NM-01 tumhai gate=tumha  design=tumhai
   NM-05 haitik gate=hai    design=haitik
full-split disagreements: 6 of 70 (the same three forms plus sau, dau, hai)
gate vs the packet's own `syllables:` field:  6 of 8 agree, 2 disagree
```

And the inversion is still live on that residue: `diph-design-correct.yml`
(`head2(tumhai) = tumhai`, the design's reading) → **exit 1, `violations=1`**;
`diph-gate-reading.yml` (`= tumha`) → **exit 0, `violations=0`** (`D18` §2,
Pair B).

**So the correct closure for `RD-4` is "delta named".** The round-26 text said
"15 of 62"; the faithful count on the round-26 surface was **12 of 62** (round-27
X54 measured the 3-row inflation: the three vowel-final diphthong forms `sau`,
`dau`, `hai`, on which the gate is right and the round-26 probe was wrong). On
the round-27 surface the head2 count is **3 of 70**. Either way the residual is
**one class**, and it is the diphthong.

## 4. Why a "closed" reading of `RD-4` would be false

The claim's `after_required` reads "the syllabify disagreement fixed (**one
algorithm**, forms re-verified)". Three readings make "closed" false:

1. **Two algorithms remain.** The gate and the design disagree on 3 of 70
   delivered forms, and the packet's own author-declared `syllables:` field —
   the third witness, carried since round 17 — disagrees with the gate on 2 of 8.
   "One algorithm" is not met.
2. **The fix was verified against an instrument that shares the residual.**
   The round-27 acceptance runner's own lawful syllabifier splits the diphthong
   too: `SYLLABLE_CONTROLS` pins `("tumhai", ["tum","ha","i"])` and
   `("haitun", ["ha","i","tun"])` (`run-validation.py:133-135`). Its syllabify
   leg therefore reads `disagreements: 0 of 70` — **agreement between two
   instruments that make the same reading error**, not agreement with the
   artifact both check. That is the round-26 failure mode (`X54-F7`: an
   instrument that cannot see the divergence reports it absent) one round later,
   and it is why this file does not accept the runner's `0` as closure.
3. **A verdict inversion survives.** A form the design and the packet both call
   correct is graded **red** on a diphthong-bearing base (§3). A gap whose
   closure condition is "one algorithm" cannot be closed while the algorithm
   still grades the right answer wrong.

## 5. The closure record — one line per gap

| gap | round-26 wording | round-27 disposition | recorded where | residual delta |
|---|---|---|---|---|
| `RD-5c` / `RL-6` | the tree has no component owning the register law | **CLOSED** | `13-register-law.yml` (new component, `packet_keys: [register_law]`, 5 rows); `law/design.md:39`; `law/impl-1.md:28`; runner `component_ownership.rows_equal: true` | the law is unenforced and the assembler does not validate the block — **declared** in the component's own `law_binding.enforcement` and in `D17` |
| `RD-4` / `RL-3` | the gate's `syllabify` disagrees on 15 of 62 forms | **PARTLY CLOSED — delta named** | the cluster class fixed (`5b5abe78…` → `b5406bcd…`, selftest 21/21 → 27/27, `is_legal_syllable`); `law/impl-1.md:29`, `law/impl-3.md:26`; `D18` | the **diphthong class**: 3 of 70 head2, 6 of 70 full-split, 2 of 8 vs the packet's own field; a verdict inversion survives on that residue |
| `RL-8` / the era leg | `REGISTER-ERA-01` specified, unimplemented | **still open, carried** | `reports/round-26/register/rules.md` §5; `13-register-law.yml` `RGL-05`; `x59` catches the era plant (`L4-FAIL`) but no delivered gate does | the era act is caught by the **audit** instrument only |
| `RD-5a` / the typing leg | glosses pass the argot leg | **still open, carried** | `D19` §1–§2 | the leg still has no label kind; the round-27 law landing did not add one |

## 6. Named limits of this review

| id | limit | statement |
|---|---|---|
| **D20-L1** | a closure recorded here is a **measurement**, not an acceptance | the parent owns admission; this file names what the bytes do at its stamp |
| **D20-L2** | the round-26 ids are **quoted from the filed files**, not restated from memory | `review.md` §5/§6.3, `design.md:229,232`, `rules.md` §5 — read this round |
| **D20-L3** | the runner's `0 of 70` is **not** treated as independent confirmation | §4.2: the runner's reference shares the residual reading; the packet's own field is the tie-breaker, and it disagrees with both |
| **D20-L4** | no filed rounds 8–26 byte was written | the round-26 gap texts are quoted; their files are byte-unchanged (`git status` over `reports/round-26/**` shows no modification by this seat) |

## 7. Counting commands for this file

```sh
export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1
grep -n "packet_keys" examples/culture-d4/components/13-register-law.yml          # [register_law]
grep -n "register_law" examples/culture-d4/components/01-brief.yml               # C-13, record_fields
grep -rn "RL-6" reports/round-27/law/*.md                                        # the closure record
sha256sum tools/gates/argot-derivation-gate.py                                   # b5406bcdaf41c595…
python3 -B tools/gates/argot-derivation-gate.py --selftest | tail -1             # 27/27
python3 -B .scratch/r27-d18/final-census.py                                      # 3 of 70 head2
python3 -B reports/round-27/run-validation.py --check | python3 -c \
  "import json,sys; m=json.load(sys.stdin)['claims']['D']['measurement']; \
   print(m['component_ownership']); print(m['artifact_tokens'])"
```
