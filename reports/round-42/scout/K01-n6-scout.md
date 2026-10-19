- Seat: K01 | scout | claim O | date 2026-10-19 | baseline ac47c78

# K01 — N6 scout: the wrapped-couples extractor defect, its host, its bytes, its fix surface

**Mission** (`reports/round-42/targets.json` seat `K01`, verbatim): *"N6 scout: locate the exact
extractor implementation the r39 Ca04 D1 finding names (read calib/Ca04-verify.md first), its parse
code, the wrapped field's exact bytes at phonetics-phonology.md:72-77, and the fix surface."*

**Method / boundary.** All measurements read-only, lane root, HEAD `ac47c78`,
`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`. No filed byte edited; no
`reports/round-*/run-validation.py` executed; no corpus byte staged; no git/network/install action.
The r19 instrument was run only as a **read-only gate** on a single corpus entry
(`python3 -B reports/round-19/audit/entry-audit.py <entry>`), which is not a round runner.

**Verdict.** The defect is **confirmed, live, and measured corpus-wide**. Host, parse code, exact
bytes, fix surface and the corrected census are all pinned below. Four scout findings are filed
beyond Ca04's D1: **D1b** (the C14 block parser over-captures prose — a second, unrecorded hazard),
**D1c** (the hyphen soft-wrap join rule is a decision that must be stated), **D1d** (three instruments
carry the same parse), and **D1e** (a materially larger finding — the *landed* policy document is a
byte-exact **truncation** of its draft, with its §6 body and all of §7 missing and three now-dangling
cross-references; r39's own gate could not catch it). D1e is the highest-value item in this fragment
and it is **not** in the queue.

## 1. The owning instrument (Ca04's "likely the r39 C12 runbook's resolver" — that guess is wrong)

The defect is **not** in C12's runbook. C12 (`reports/round-35/cov/C12-audit-runbook.md`) is a runbook
*document*; its pointer family §2 (`:37`) is about backticked repo paths, not couples. The actual
implementation carrying the single-line extractor is:

- **`reports/round-19/audit/entry-audit.py:74-96`** — `def couples_targets(text, path)`.
  - **`:75`** `m = re.search(r"^- couples:\s*(.*)$", text, re.M)` ← **the defect site.** `$` with
    `re.M` stops at the first newline, so the capture is exactly the first physical line.
  - `:80-82` `MDREF_RE.findall(line)` over that one line, brace-expanded one level (`:34-42`).
  - `:87-95` Tier-1 resolution (entry dir → lane root → `corpus/knowledge/`), no fallback.
- **`:105,118-119,130`** — the call site: `resolved, unresolved = couples_targets(text, path)`; the
  result feeds `couples_resolved` / `couples_unresolved` and the `quality_bar` conjunction (`:130`
  `and not unresolved`). The zeroed field is therefore not a cosmetic count — it silently *removes*
  tokens from the gate's input.

**Second and third copies of the same parse** (see D1d, §6): `reports/round-27/audit/entry-audit.py`
(480 lines) and `reports/round-28/audit/entry-audit.py` (294 lines, `couples_unresolved` exposed at
`:251,264-268`).

**Code fact (the exact failure mode), reproduced by command:**

```
$ python3 -B reports/round-19/audit/entry-audit.py corpus/knowledge/linguistics/phonetics-phonology.md
FAIL corpus/knowledge/linguistics/phonetics-phonology.md src=15/15 couples=0 unresolved=[] gap=False dec=True
TOTAL 0/1 clear the bar
exit=2
```

`couples=0 unresolved=[]` is the signature: **the field is not reported as dangling, it is reported as
empty.** Zero tokens captured means the entry looks like it couples nothing — exactly the
`empty-couples` condition `tools/gates/provenance-audit.py:16-18` treats as a *reference-not-craft*
defect. A silent zero is worse than a visible failure.

The r19 instrument's own selftest **does not cover the wrapped case** — it is green today:

```
$ python3 -B reports/round-19/audit/entry-audit.py --selftest
PASS braces / PASS braces nested / PASS selftest entry quality / PASS selftest source locator
PASS selftest gap / PASS selftest decision / PASS selftest couples resolve
PASS negative control (no sources fails)
exit=0
```

`selftest()` is `:151-182`; its fixture (`:168-170`) writes a **single-line** `- couples:` only. The
negative control (`:177-181`) drops the *sources* field, not the couples wrap. So O02's required
controls are genuinely new coverage, not a re-run: the wrapped-field positive and the phantom negative
do not exist in the filed selftest.

## 2. The wrapped field's exact bytes (`corpus/knowledge/linguistics/phonetics-phonology.md:72-77`)

Six physical lines, `- couples:` at `:72`, continuations indented two spaces:

```
72	- couples: language (this file, core method); myth (divine/true names, taboo
73	  naming, onomatopoeic etiologies); symbol (sound symbolism, name-shape,
74	  bouba/kiki iconography); era (Neolithic bite → f/v, sound-change dating of
75	  strata); costume (masks/mouthgear vs articulation, whistle & drum channels);
76	  environment/anatomy design; prospective sibling files: sound-change.md, tone-
77	  prosody.md, sound-symbolism.md, writing-systems.md
```

Line 78 is blank and line 79 is `## 1. Two levels: phonetics vs phonology` — the field is bounded on
**both** sides by a blank line and a `## ` heading. This matters for the fix (§3).

The 4 named `.md` targets and their live status (`ls corpus/knowledge/linguistics/`, this seat):

| token | exists? | class |
|---|---|---|
| `sound-change.md` | ABSENT | unresolved (phantom) |
| `tone-prosody.md` | ABSENT | unresolved (phantom) |
| `sound-symbolism.md` | EXISTS | direct |
| `writing-systems.md` | EXISTS | direct |

This reproduces Ca04's D1 count exactly: **4 named, 2 exist, 2 phantoms.** The phantoms are
`to-verify` in the field's own words — the line reads *"prospective sibling files:"*, i.e. the field
itself declares these are planned, not present. That is the disposition material for the two phantom
attributions the claim asks to disposition (§6).

## 3. Fix surface — three candidate hosts, one already correct in-repo

**(a) The precedent that is already right — `tools/gates/provenance-audit.py:244-261`** `field_block()`.
The best host/template. It accumulates continuation lines only while `INDENT_RE` (`:77`
`^[ \t]+\S`) matches, stops at the next `FIELD_RE` line (`:76`), and stops at a non-indented line.
That is indentation-bounded block extraction with the correct stop semantics. It currently uses the
block only for a *presence/emptiness* check (`:318-324`) and never extracts `.md` tokens — so it is a
template, not yet a couples resolver.

**(b) The C14 block parser — `reports/round-35/cov/C14-audit-6-10.md:225-236`** `fields_of()` +
`:263-288` `couples_refs()`. This is the parser Ca04 cites as capturing the wrapped tokens, and it
does. But see **D1b** (§6): its continuation rule is `elif cur and line.strip()` with **no indentation
test and no blank-line test**, so it appends the prose paragraph that follows the frontmatter. It is
correct-by-accident on this corpus, not correct-by-construction.

**(c) The exact diff shape for r19.** Replace `:75`'s single-line capture with a field-bounded block
read; everything downstream (`:80-95`) then works unchanged because it already operates on a string.
The minimal, semantics-correct rule, in precedence order:

1. start at the `- couples:` line, take its value;
2. keep appending following lines while they are **indented continuations** (`^[ \t]+\S`) **and** are
   not a new `- field:` line;
3. **stop** at the first blank line (the frontmatter block ends) **and** at the first `## ` heading —
   the entry shape always separates the header block this way (measured: the `## ` heading closes the
   block in every entry; C14's `frontmatter_block():208-222` already uses `## ` as the terminator);
4. join the parts, resolving soft wraps (§4), then run the **unchanged** `MDREF_RE.findall` +
   `expand_braces` over the joined string.

## 4. The hyphen soft-wrap mangling — real, and a *join-rule* decision, not an extractor bug

Ca04 recorded the mangling as `to-verify`. It is now measured. The wrap splits `tone-prosody.md`
across lines 76/77 as `tone-` + `prosody.md`. The join rule decides the token:

| join rule | token produced | correct? |
|---|---|---|
| `"\n".join(parts)` (C14 as filed) | `prosody.md` | NO — mangled |
| `" ".join(parts)` | `tone-` and `prosody.md` (two tokens) | NO — split |
| `"".join(parts)` (hyphen stripped) | `toneprosody.md` | NO — over-stripped |
| de-hyphen on soft wrap: `"tone-"` + `"prosody"` → `"tone-prosody"` | `tone-prosody.md` | **YES** |

Commands (this seat, read-only, exact):

```
MDREF newline-join: ['prosody.md', 'sound-change.md', 'sound-symbolism.md', 'writing-systems.md']
MDREF empty-join  : ['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
```

The rule that recovers the intended token: **if a part ends in `-`, concatenate the next part
directly (de-hyphenating the wrap); otherwise join with a space.** Two consequences the executor and
verifiers must not miss:

- `"".join` (naive de-hyphen) is **wrong** and produces `toneprosody.md`. The fix is not "strip the
  hyphen", it is "treat a trailing hyphen as a soft-wrap indicator".
- Without the de-hyphen rule the corrected census still shows a phantom `prosody.md` token — the fix
  would *appear* to work (4 tokens, not 0) while still mis-naming one. O05's adversarial fixture
  should include a hyphen-wrap split mid-token.

## 5. Corrected census — the numbers O03 must predict and O04/O05 must reproduce

Corpus-wide over **all 220** `corpus/knowledge/*/*.md`, per-entry deduplicated tokens, policy
classification (Tier-1 direct / slash-free unique-basename fallback / ambiguous / unresolved;
`reports/round-39/calib/basename-couples-policy.md:27-48`). Four extractors, same classifier:

```
A. single-line (r19:75)             refs=2607 -> direct=2435 fallback=166 ambiguous=0 unresolved=6
     unresolved distinct=5: -gate.md(x1), ../linguistics/phonology-sanity.md(x2),
       honorifics-and-register.md(x1), naming-and-onomastics.md(x1), phonology-basics.md(x1)
B. indent-bounded + de-hyphen (FIX) refs=2611 -> direct=2437 fallback=166 ambiguous=0 unresolved=8
     unresolved distinct=7: -gate.md(x1), ../linguistics/phonology-sanity.md(x2),
       honorifics-and-register.md(x1), naming-and-onomastics.md(x1), phonology-basics.md(x1),
       sound-change.md(x1), tone-prosody.md(x1)
C. C14 fields_of block (as filed)   refs=2611 -> direct=2437 fallback=166 ambiguous=0 unresolved=8
     (same token multiset as B on this corpus — see D1b for why that is luck, not correctness)
D. indent-bounded, hyphen STRIPPED  refs=2611 -> ... unresolved distinct=7 incl. toneprosody.md  [WRONG]
```

**The arithmetic.** `A + 4 = B`: the wrapped field contributes exactly 4 tokens, taking `direct`
2435→2437 (+2: `sound-symbolism.md`, `writing-systems.md`) and `unresolved` 6→8 (+2:
`sound-change.md`, `tone-prosody.md`). `fallback` is unchanged at 166 and `ambiguous` unchanged at 0 —
the fix touches **only** the wrapped field.

**Blast radius is exactly one entry.** Diffing the token set of every entry under A vs B:

```
entries where FIX changes the token set: 1 / 220
   corpus/knowledge/linguistics/phonetics-phonology.md
      dropped:[]
      added  :['sound-change.md', 'sound-symbolism.md', 'tone-prosody.md', 'writing-systems.md']
```

**Entries with a multi-line couples field: 1 / 220** (`phonetics-phonology.md`, 6 parts). This is the
strongest available control: the fix is a strict superset operation on a single entry, so a regression
in any *other* entry's count is a hard failure signal for O04/O05.

**Relation to the r39 policy's 2504 census.** The policy's Part 2 figure was measured at 212 entries:
`entries=212 refs=2504 -> direct=2335 fallback=163 ambiguous=0 unresolved=6`
(`reports/round-39/calib/Ca03-basename-policy.md:268-269`). The live corpus is **220** entries —
r40/r41 added 8 — so `2504` is not directly comparable and must **not** be "corrected" by
subtraction. Re-running the policy's own §6 script byte-exact today (extracted from the fenced block
at `Ca03-basename-policy.md:149-258`, run read-only) reproduces:

```
== Part 2: corpus-wide current scan ==
  entries=220 refs=2607 -> direct=2435 fallback=166 ambiguous=0 unresolved=6
  unresolved distinct=5: -gate.md(x1), ../linguistics/phonology-sanity.md(x2),
    honorifics-and-register.md(x1), naming-and-onomastics.md(x1), phonology-basics.md(x1)
RESULT: PASS (334=319+15, 0 ambiguous, 0 unresolved, 0 misaligned)
```

That is line-for-line extractor A. **So the policy's §6 recipe still carries the N6 defect** — Ca04's
D1 fix (block extraction) was not applied. The corrected baseline the claim asks for is therefore B:
**`220 entries, 2611 refs → 2437 direct / 166 fallback / 0 ambiguous / 8 unresolved (7 distinct)`**,
and the two phantoms `sound-change.md`, `tone-prosody.md` are the census's phantom attributions.

## 6. Findings filed beyond Ca04 D1

**D1b — the C14 block parser over-captures prose (NEW, unrecorded in the queue).**
`fields_of()` (`C14-audit-6-10.md:225-236`) appends a following line whenever it is non-blank
(`elif cur and line.strip(): out[cur].append(line.strip())`) — **no indentation test, no blank-line
test.** On this corpus the frontmatter is separated from the body by a blank line, so the append
happens for the blank-stripped body paragraph too. Live case measured:

```
corpus/knowledge/linguistics/conlang-methodology.md  single=19 block=19
    block field lines: 2  (the `- couples:` line + the following body paragraph)
```

`fields_of` returns the couples value as *field line + body prose paragraph joined*. It produces the
same 19-token multiset as the single-line extractor **only because that prose carries no `.md` token**.
Add one `.md` mention to any entry's opening paragraph and C14's parser attributes it to `couples:` —
a false couples reference. **A successor instrument that adopts C14's `fields_of` verbatim inherits a
false-positive generator.** The correct rule is §3(c) steps 2–3: indentation-bounded, blank-line- and
heading-terminated. (Cross-check: `tools/gates/provenance-audit.py:244-261` already does it correctly
with `INDENT_RE`; C14 should have copied that.) Not in `reports/round-40/op/defect-queue-v2.json` —
its rows cover only `basename-couples-policy`, `r39-basename-successor-instrument` and
`N6-couples-extractor-wrapped-field`, and none mentions over-capture.

**D1c — the hyphen soft-wrap join rule is a decision the fix must state.** §4. Ca04's `tone-prosody.md`
was `to-verify`; it is now measured and the correct rule named. The executor must not leave the join
rule implicit: two of the four plausible rules produce a *plausible-looking but wrong* token.

**D1d — the fix must name which copies it patches.** `reports/round-19/audit/entry-audit.py`,
`reports/round-27/audit/entry-audit.py` and `reports/round-28/audit/entry-audit.py` are three
instruments; r19 and r27 both carry a couples leg. A fix landed in one copy leaves the others
divergent, and the claim's `after_required` says "the fixed extractor durable" (singular). The wave
must state the host set and whether successors are patched, aliased, or declared superseded.

**D1e — the landed policy is a byte-exact TRUNCATION of its draft (NEW; the largest finding here).**

`reports/round-39/calib/basename-couples-policy.md` is **107 lines / 5832 bytes**, and its final bytes
are:

```
b'...Run from the lane root; no writes, no runner invocation\n(`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`):\n'
```

The file ends **inside §6**, immediately after the lead-in colon, with the code fence, the filed-run
summary and **all of §7** absent. The proof is an exact prefix test against the draft's fenced
document:

- The draft `reports/round-39/calib/Ca03-basename-policy.md` opens a four-backtick fence at `:40`
  (```` ````markdown ````) and closes it at `:304` (```` ```` ````); the drafted document inside is
  **263 lines** (draft lines 41–303).
- `fenced_doc[:107] == landed` → **True** (measured, byte-exact).
- The landed file therefore **stops at fenced-document line 107** and **drops fenced-document lines
  108–263 (156 lines)** — which is precisely §6's ```` ```python ```` fence (drafted doc `:109-218`),
  the "Filed run of this exact script" summary, and §7 "Adoption evidence" (`:252`).

Consequences, all measured:

- **Three cross-references now dangle.** The landed file cites `§6` at `:69` ("re-verified with full
  coverage by §6"), `:81` ("§6, Part 3") and `:96` ("re-run §6 and re-adjudicate") — pointing at a
  section whose body no longer exists. `§7` is referenced nowhere and does not exist.
- **The recipe is gone.** §6 was the *only* read-only reproduction recipe the policy offered, and the
  policy's §5.5 makes it load-bearing: *"re-run §6 and re-adjudicate before relying on the fallback"*
  (`:93-96`). With §6 truncated, the policy's own required re-run trigger has no script.
- **r39's own gate could not catch it.** The Ca1 leg is a **marker-substring test**:
  `reports/round-39/run-validation.py:117-121` reads the policy and appends a failure only if the file
  is absent or lacks the literal string `"fallback"`. A truncated file passes trivially. The Ca3 leg
  (`:129-130`) checks `"334"` in `Ca04-verify.md`, not the policy. `reports/round-39/validation.json`
  does not mention `basename-couples-policy`, `Ca03` or `Ca04` anywhere (measured), and
  `SCORECARD.md:774` records the policy as delivered, citing it as the Ca row's artifact. So the
  truncation was **admitted and never detected**.
- **It is committed, not a working-tree artifact.** `git log -- reports/round-39/calib/
  basename-couples-policy.md` → a single commit `fd55e1f` ("round-39: admit C/Ca … basename-couples
  policy"), and the file is clean in `git status`. The truncation is in filed, frozen bytes.
- **No later round noticed.** `grep -rn 'basename-couples\|basename_couples' reports/round-41/` → no
  match; `grep -rn 'truncat'` across `reports/round-40/`, `reports/round-41/`, `LOG.md`,
  `SCORECARD.md` finds nothing about the policy. r40's queue (`defect-queue-v2.json`) has no row for
  it — it records the policy as `fixed-with-evidence`.

**Why this belongs in the N6/O scope and what it changes.** The claim's `after_required` includes
"the corrected census filed" and the policy is the document that *defines* the census's counting rule.
A truncated policy means the counting rule's own reproduction recipe is unverifiable, and the
`r39-basename-successor-instrument` row's plan ("the successor instrument implements this policy")
is being built against a document that is missing its recipe and its adoption-evidence section. The
integrator must decide, and record, one of: (i) the truncation is repaired (a **new** file or a
successor revision — the r39 path is filed bytes and must not be edited in place); (ii) the truncated
policy is accepted as-is and §6/§7 are re-homed into the successor instrument; or (iii) the queue row
`r39-basename-successor-instrument` is amended to name the truncation. **This seat does not
disposition it** — it is named with evidence so the wave does not build on it silently.

**Caveat, stated plainly.** This seat read the landed file and the draft file and proved the prefix
relation by command. It did **not** read the r39 integrator's own landing record to learn *why* the
copy stopped at 107 lines, and it does not claim intent (accidental truncation, deliberate
partial-landing, or a copy step that hit a size/line boundary are all consistent with the bytes). The
fact is the byte-level relation; the cause is `to-verify` for whoever owns the r39 landing.

## 7. Boundaries the executor must respect (read from filed bytes, not assumed)

- **`tools/gates/frozen/**` is off-limits** (`shared_rules`). `tools/gates/provenance-audit.py` is
  **not** under `frozen/`, but it is a gate with frozen input snapshots
  (`tools/gates/frozen/provenance-audit/r9-pre/`, `.../r18-post/`) and a fixture suite
  (`tools/gates/fixtures/provenance/defect-empty-couples.md`, `defect-missing-couples.md`). Any edit
  must keep those fixtures green; the wave should treat it as **template-only** (copy the
  `field_block` semantics into the resolver) unless a round explicitly owns gate tooling.
- **`corpus/**` is never staged directly** — a corrected policy text is drafted as a fenced block and
  the integrator applies it (`shared_rules`).
- **`reports/round-19/**`, `reports/round-35/**` and `reports/round-39/**` are filed bytes**
  (`shared_rules`: never edit `reports/round-1..41/**`). The fix therefore **cannot** be a patch to
  `reports/round-19/audit/entry-audit.py` in place, and the truncated `basename-couples-policy.md`
  **cannot** be repaired in place either. Both must land as new bytes under `reports/round-42/` (or a
  wave-owned path). This is the single most important constraint for O01: the "fix patch against the
  confirmed host" can only be a *fenced draft of a new file*, never an edit to a r19/r39 path.

## 8. What the executor/verifier seats need from this fragment (handoff)

- **O01 (fix draft):** host set per §1 and D1d; the block rule per §3(c); the join rule per §4; the
  fenced diff shape per §3(c) ("everything downstream unchanged"). Must NOT propose an in-place edit
  of `reports/round-19/**`.
- **O02 (controls):** the filed selftest (`:151-182`) has no wrapped-field positive and no phantom
  negative — §1. Fixtures should be the literal bytes of §2 (or an equivalent), a hyphen-wrap case per
  §4, and the over-capture trap per D1b (a `.md` mention in the paragraph *after* the field).
- **O03 (predicted census):** reproduce §5 row B — `220 / 2611 → 2437 / 166 / 0 / 8 (7 distinct)`.
  Do not target the policy's `2504` (212-entry era).
- **O04/O05 (verifiers):** the one-entry blast radius (§5) is the regression oracle — any change to
  another entry's token set is a failure. O05's adversarial fixture per §4 and D1b.
- **Integrator (D1e):** decide and record the truncated-policy disposition (§6 D1e) before the
  successor instrument is authored against it.

## Owed

- **Owed (to the wave, not this seat):** the fix must land as a **new** instrument under
  `reports/round-42/**` (or a wave-owned tools path); `reports/round-19/audit/entry-audit.py` stays
  byte-identical (sha256 `e7992c325a479aa7415c42722a034a95a9ea342a58367ead9cd2636a5a62830c`), and
  `reports/round-39/calib/basename-couples-policy.md` stays byte-identical (sha256
  `105dfff6c667ad5b77c28be8d6070ec243b5e19029fb60ae83d6028aa2e941cf`).
- **Owed (to-verify, carried):** whether `reports/round-27/audit/entry-audit.py` carries the same
  single-line parse at its own couples line. This seat confirmed the r19 site by line and the
  r27/r28 call sites by grep, but did **not** read r27's extractor line. The executor should confirm
  before claiming "the extractor" is singular.
- **Owed (to-verify, D1e cause):** the r39 landing record does not explain why the copy stopped at
  107 lines; this seat proved the byte relation only. Owner: whoever holds the r39 landing record.
- **Owed (queue):** D1b (C14 over-capture) and D1e (policy truncation) are **new** findings with no
  queue row; the round's queue-update seat should file them or record why not. D1c and D1d are
  fix-shape decisions, not new defects.
- **Owed (full recount under the fixed parser):** §5 row B is this seat's independent read-only
  recount; Ca04's `to-verify` "full block-parser couples recount corpus-wide" is discharged for the
  *token counts*. The *landed* tool's reproduction remains O03/O04's job.

## Citations

- **Defect site / host:** `reports/round-19/audit/entry-audit.py:75` (single-line capture), `:74-96`
  (`couples_targets`), `:31,34-42` (token regex, brace expansion), `:80-82` (findall over the captured
  line), `:87-95` (Tier-1 resolution), `:105,118-119,130` (call site, `quality_bar` conjunction),
  `:151-182` (`selftest`; single-line fixture `:168-170`; negative control `:177-181`), `:185-217`
  (`main`, read-only CLI). Successors: `reports/round-27/audit/entry-audit.py` (480 lines),
  `reports/round-28/audit/entry-audit.py:251,264-268`.
- **Wrapped field bytes:** `corpus/knowledge/linguistics/phonetics-phonology.md:72-77` (blank at
  `:78`, `## ` heading at `:79`); the four targets' existence measured by
  `ls corpus/knowledge/linguistics/` (this seat, 2026-10-19).
- **Fix-surface precedents:** `tools/gates/provenance-audit.py:76-77` (`FIELD_RE`, `INDENT_RE`),
  `:244-261` (`field_block`, the correct indentation-bounded rule), `:263-265` (`is_empty_value`),
  `:318-324` (couples presence/emptiness check), `:16-18` (the `empty-couples` rationale);
  `reports/round-35/cov/C14-audit-6-10.md:199` (`FIELD_RE`), `:208-222` (`frontmatter_block`, `## `
  terminator), `:225-236` (`fields_of`, the over-capture rule — D1b), `:239-246` (brace expansion),
  `:249-260` (basename index), `:263-288` (`couples_refs`), `:281` (slash-bearing basename key).
- **LANDED policy** (`reports/round-39/calib/basename-couples-policy.md`, 107 lines, 5832 bytes,
  committed `fd55e1f`): §1 token extraction `:14-25` (single-line rule + `entry-audit.py:75` citation
  `:16-17`); §2 tiers/classes `:27-48`; §3 reporting rules `:50-58`; §4 group alignment `:60-69`
  (dangling `§6` ref `:69`); §5 limits `:71-102` (§5.1 slash-gate `:73-81`, dangling `§6` ref `:81`;
  §5.5 re-run trigger `:93-96`, dangling `§6` ref `:96`; §5.6 glob fragments `:97-102`); §6 heading +
  lead-in only `:104-107` (**body absent**); §7 **absent**.
- **DRAFT** (`reports/round-39/calib/Ca03-basename-policy.md`, 359 lines): design decisions `:1-38`;
  four-backtick fence open `:40`, close `:304`; drafted document `:41-303` (263 lines); §6 ```` ```python ````
  fence `:149-258`; filed-run summary `:260-290`; §7 adoption evidence `:292-303`; `## Owed` `:306`;
  `## Citations` `:326`; the 212-entry figure `:35-38` and `:268-269`.
- **D1e gate-blindness:** `reports/round-39/run-validation.py:117-121` (Ca1 marker-substring test on
  the policy), `:129-130` (Ca3 `"334"` in `Ca04-verify.md`); `reports/round-39/validation.json` (no
  mention of `basename-couples-policy`/`Ca03`/`Ca04`; `acceptance_checks_passed: true`);
  `SCORECARD.md:774` (Ca row, cites the policy as delivered); `LOG.md:3755-3761` (r39 Ca admitted
  record); `git log -- reports/round-39/calib/basename-couples-policy.md` → `fd55e1f`.
- **Ca04 D1:** `reports/round-39/calib/Ca04-verify.md` — D1 row ("§1's single-line extractor silently
  zeroes wrapped couples fields", 0 tokens vs 4 named, 2 phantoms), and its `to-verify` block (full
  block-parser recount).
- **Queue:** `reports/round-40/op/defect-queue-v2.json` rows `N6-couples-extractor-wrapped-field`
  (owner "future resolver round"), `r39-basename-successor-instrument` (records the policy landed
  verbatim without D1/D2, and that the filed r19 instrument FAILs sacred-kingship today),
  `basename-couples-policy` (now `fixed-with-evidence`); `reports/round-37/op/defect-queue.json:202-211`
  (origin row); `reports/round-40/calib/Ca01-queue-v2.md:52-54` (r39 rows' provenance text).
- **Command outputs (this seat, 2026-10-19, lane root, HEAD `ac47c78`,
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, all read-only):**
  (a) `python3 -B reports/round-19/audit/entry-audit.py corpus/knowledge/linguistics/phonetics-phonology.md`
  → `couples=0 unresolved=[]`, `TOTAL 0/1`, exit 2; (b) `... --selftest` → all PASS, exit 0;
  (c) four-extractor census over 220 entries → §5 rows A/B/C/D (scratch script only);
  (d) per-entry token-set diff → 1/220 entries changed, listed in §5; (e) multi-line-field census →
  1/220 (`phonetics-phonology.md`, 6 parts); (f) policy §6 script extracted from
  `Ca03-basename-policy.md:150-257` and re-run byte-exact → Part 2
  `entries=220 refs=2607 -> 2435/166/0/6`, `RESULT: PASS`; (g) prefix test
  `fenced_doc[:107] == landed` → `True`, fenced doc 263 lines, landed 107 lines / 5832 bytes,
  `endswith(b'\n')` True; (h) `sha256sum`: r19 instrument `e7992c32…`, phonetics-phonology
  `b4f9b003…`, C14 `bf402bc6…`, provenance-audit `8a96aaf4…`, landed policy `105dfff6…`.
- **Regimen/seat:** `reports/round-42/targets.json` seat `K01`; `reports/round-42/claims.json` claim
  `O` (`after_required`: fixed extractor durable, wrapped field read whole, corrected census filed,
  selftest green, phantoms dispositioned); `REGIMEN.md` per-round contract.
