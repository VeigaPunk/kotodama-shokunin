- Seat: O10 | executor | claim O | date 2026-10-19 | baseline ac47c78

# O10 — spare gap-fill #2 (claim O): the unwrap rule, the live host, the corpus census

Assignment (verbatim, `reports/round-42/targets.json` seat `O10`): "Spare gap-fill
#2." Out: `op/O10-gap-fill.md`. Claim O (`reports/round-42/claims.json:13-18`).

The seats around me split the N6 fix three ways: K01 scouted the host, O01 drafts
the block parser, O02 the controls, O03 the predicted census. Nothing in the wave
owns the **soft-wrap unwrap rule** — how a multi-line field is rejoined before
tokenization — and nothing owns the **corpus-wide wrapped-field census** that Ca04
explicitly left `to-verify` (`reports/round-39/calib/Ca04-verify.md:114`). Both are
load-bearing for claim O: the "4 named targets, not 0" threshold is false under a
wrong unwrap rule. This fragment closes both, and in doing so finds two things the
wave's scout did not name.

## 1. The finding that changes the fix: unwrap rule decides the token

`corpus/knowledge/linguistics/phonetics-phonology.md:72-77` is the corpus's one
wrapped `couples` field (confirmed corpus-wide, §3). The line break falls **inside**
a filename:

```
:76  ... prospective sibling files: sound-change.md, tone-
:77  prosody.md, sound-symbolism.md, writing-systems.md
```

So `tone-` + `prosody.md` is one token, `tone-prosody.md`. Measured four rules over
that block (`export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, read-only
probe, commands in Citations):

| rule | rejoin | tokens produced |
|---|---|---|
| A | single physical line (r19 `entry-audit.py:75`) | **0** |
| B | block, lines joined with `\n` (r39 C14 `C14-audit-6-10.md:225-236`) | 4: `prosody.md` *(phantom)*, `sound-change.md`, `sound-symbolism.md`, `writing-systems.md` |
| C | block, soft break → single space | 4: identical to B — **still `prosody.md`** |
| D | block, hyphen-terminated line → join **keeping** the hyphen | 4: `sound-change.md`, `sound-symbolism.md`, **`tone-prosody.md`**, `writing-systems.md` |

B and C fabricate the token `prosody.md`, which exists nowhere; the intended token
`tone-prosody.md` is confirmed by the entry's own body
(`phonetics-phonology.md:279`: "Natural partners: `sound-change.md` (diachrony → §5),
`tone-prosody.md`"). A third wrong variant — healing the hyphen by *deleting* it —
fabricates `toneprosody.md`. Ca04 named this mangling "an extractor hazard *no*
current instrument handles" and left it `to-verify` (`Ca04-verify.md:88-93`); it is
now reproduced and the correct rule is measured: **D**.

Consequence for claim O's threshold: the wrapped field reads **4/4 targets** only
under rule D. Under the rule the wave is most likely to reach for (C, the obvious
"join wrapped lines with a space") the field reads 4 tokens but **one is a
phantom**, so a naive 4/4 count is a false green. This is the trap O02's synthetic
phantom negative must mirror (§5).

## 2. The host is live, and it has the same defect

The claim leaves the owning instrument to the wave ("likely the r39 C12 runbook's
resolver or a tools/harness couples checker; the wave confirms the host"). The host
that matters is not in `reports/` — it is **live**:

`tools/gates/provenance-audit.py:244-260` (`field_block`) reads a `- couples:`
header plus its indented continuations and joins them with `" ".join(...)`
(`:259`) — i.e. rule C. Run against the wrapped field it emits:

```
$ python3 -B -c "... field_block(lines,'couples') ..."   # tools/gates/provenance-audit.py
present= True
content= '... prospective sibling files: sound-change.md, tone- prosody.md, sound-symbolism.md, writing-systems.md'
empty? False
```

`tone- prosody.md` → the same `prosody.md` phantom as B/C. So the corpus's **only
live gate that reads a `couples` block continuation** carries the identical defect.
That is a stronger statement than "a filed r19 instrument is wrong": the r19
instrument is archived, `provenance-audit.py` runs. It is the natural host for the
fix — a hyphen-aware rejoin at `:255-257` — and O01's patch should name it.

(Note the live gate does *not* tokenize `couples`; its finding is `empty-couples`
only. The defect is latent, not currently mis-gating. Recorded so the integrator
does not over-claim a live failure.)

## 3. Corpus-wide wrapped-field census (Ca04's owed `to-verify`)

Every header field over all 220 `corpus/knowledge/*/*.md`, classifying continuation
lines as indented sub-bullet (intended block structure) vs indented prose
(true soft-wrap):

| field | files w/ soft-wrap | soft-wrapped lines |
|---|---|---|
| `couples` | **1** (`linguistics/phonetics-phonology.md`) | 5 (lines 73-77) |
| `sources` | 1 (`linguistics/phonetics-phonology.md`) | 48 (lines 8-69) |
| `topic` | 2 (`linguistics/numerals-and-measures.md:4-16`, `linguistics/phonetics-phonology.md:4-5`) | 15 |

No other field soft-wraps. Column-0 continuations under `recheck` (36 lines),
`source` (1), `topic` (26) are **bullet blocks** (`- ...` at column 0), a different
construct, not soft-wraps. This answers Ca04's `to-verify` at line 114: **exactly
one wrapped `couples` field, 5 continuation lines, 4 tokens under rule D** — Ca04's
partial ("1 wrapped field, 4 tokens, 2 phantom") is confirmed and the phantom
mechanism is now named (`prosody.md`, not the mangled-string reading).

## 4. Corrected census + disposition of every unresolved token

Recount with rule D at baseline `ac47c78` (220 entries, four-class per
`reports/round-39/calib/basename-couples-policy.md` §2):

```
entries=220 tokens=2611 direct=2437 fallback=166 ambiguous=0 unresolved=8
```

All 8 unresolved tokens, dispositioned (none left dangling):

| # | entry | token | class | evidence |
|---|---|---|---|---|
| 1-3 | `linguistics/language-contact.md:7` | `phonology-basics.md`, `naming-and-onomastics.md`, `honorifics-and-register.md` | **prospective** | line reads "sibling knowledge files **to seed**"; all 3 absent |
| 4-5 | `linguistics/phonetics-phonology.md:76-77` | `sound-change.md`, `tone-prosody.md` | **prospective** | line reads "prospective sibling files"; both absent |
| 6-7 | `synthesis/typed-label-routing-workflow.md:16`, `verification/label-channel-routing-verification.md:14` | `../linguistics/phonology-sanity.md` | **wrong-path (defect)** | `corpus/knowledge/linguistics/phonology-sanity.md` is **ABSENT**; the file is `verification/phonology-sanity-gate.md`, which the same line already cites |
| 8 | `verification/gate-frozen-run-standard.md:15` | `-gate.md` | **glob fragment** | inside `corpus/knowledge/verification/*-gate.md`; policy §5.6 (`basename-couples-policy.md:97-102`) forbids counting it |

The r39 policy's four classes cannot hold rows 1-5: a prospective declaration names
a file the corpus *intends* to grow, which is neither a dangling reference nor a
resolution. The policy needs a fifth class, **`prospective`**, with its own
non-blocker disposition. Rows 6-7 are a **real corpus defect** — a couples path to
a non-existent `phonology-sanity.md` in two entries, while the existing
`phonology-sanity-gate.md` sits in the same field. That is a *new finding*, not a
phantom, and it is owed to the integrator (corpus byte change — drafted below).

Zero phantom attributions remain: the only two tokens the old parsers invented
(`prosody.md`, and `toneprosody.md` under a delete-hyphen heal) are gone under
rule D, and the 8 real unresolved tokens each carry a disposition.

## 5. Fenced drafts for the integrator (never staged by this seat)

**D1 — unwrap rule + block parser (host: `tools/gates/provenance-audit.py:244-260`;
the same rejoin belongs in the r19/C14 successor resolver).** Replace the
`" ".join(part for part in parts if part)` at `:259` with:

```python
# --- draft: hyphen-aware field rejoin (rule D) -----------------------------
def _rejoin(parts):
    """Join a field line with its continuation lines.

    A continuation appended to a line that already ends in '-' is the second
    half of a hyphenated word broken across the wrap (the house style breaks
    long fields at existing hyphens): join with the hyphen kept and no space.
    Every other soft break becomes a single space.
    """
    out = ""
    for part in parts:
        part = part.strip()
        if not part:
            continue
        if out and out.endswith("-"):
            out += part          # keep the hyphen: 'tone-' + 'prosody.md'
        elif out:
            out += " " + part
        else:
            out = part
    return out
# then, at the old join site:
#     return True, _rejoin(parts)
# ---------------------------------------------------------------------------
```

**D2 — successor resolver token extraction (r19/C14 lineage).** Where the block is
currently `"\n".join(...)` (C14 `C14-audit-6-10.md:236`) or the single line (r19
`entry-audit.py:75`), extract from `_rejoin(block_lines)` before applying
`MDREF_RE` / brace expansion.

**D3 — selftest controls (O02 owns the landed copy; these are the exact fixtures).**

```text
POSITIVE  wrapped field, hyphen at the break:
  - couples: prospective sibling files: sound-change.md, tone-
    prosody.md, sound-symbolism.md
  expect (rule D): tokens {sound-change.md, tone-prosody.md, sound-symbolism.md}
  expect (rule C): {sound-change.md, prosody.md, sound-symbolism.md}   <- MUST FAIL the positive
NEGATIVE  synthetic phantom:
  a fixture whose only "target" is the string 'prosody.md' appearing solely as
  the tail of a hyphenated wrap; assert 'prosody.md' is NOT in the token set and
  'tone-prosody.md' IS.
REGRESSION  unwrapped single-line field (e.g. sacred-kingship:37): token set
  unchanged under rules A and D (36 tokens) — the rejoin must be a no-op there.
```

**D4 — corpus wrong-path fix (rows 6-7; corpus byte change, integrator applies).**

```diff
--- corpus/knowledge/synthesis/typed-label-routing-workflow.md:16
-  linguistics — `../linguistics/language-contact.md`, `../linguistics/phonology-sanity.md`;
+  linguistics — `../linguistics/language-contact.md`; verification — `../verification/phonology-sanity-gate.md`;
--- corpus/knowledge/verification/label-channel-routing-verification.md:14
-  linguistics — `../linguistics/phonology-sanity.md`, `../linguistics/language-contact.md`, ...
+  linguistics — `../linguistics/language-contact.md`, ...  (phonology-sanity-gate.md already cited above in the same line)
```

Flagged, not decided: whether `phonology-sanity.md` was an intended future sibling
(→ prospective) or a typo for `phonology-sanity-gate.md` (→ fix). The same line's
existing citation of `phonology-sanity-gate.md` argues for typo. Owner: integrator.

## 6. Predicted corrected census (the landed tool must reproduce §4)

```
entries=220 tokens=2611 direct=2437 fallback=166 ambiguous=0 unresolved=8
unresolved breakdown: prospective 5, wrong-path 2, glob-fragment 1, dangling 0
wrapped-field leg: 1 field, 4 tokens, 2 direct (sound-symbolism, writing-systems),
                   2 prospective-unresolved (sound-change, tone-prosody), 0 phantom
```

Delta vs the r39 policy's filed arithmetic (212 / 2504 / 2335 / 163 / 0 / 6,
`basename-couples-policy.md` §6 Part 2 / `Ca04-verify.md:29-31`): +8 entries, +107
tokens, +102 direct, +3 fallback, +2 unresolved — consistent with the r40/r41
additions, but the per-entry attribution of the +107 is **`to-verify`** (O03 owns
the reconciliation; do not read this as a re-derivation of r39's number, which was
produced by a different extraction and must stay filed).

## Owed

- Integrator: apply D1 to the live host `tools/gates/provenance-audit.py:259`
  (and to the successor resolver named by O01); land D3's controls where O02
  places them; adjudicate D4 (corpus wrong-path, rows 6-7).
- O12 (policy-check): the r39 policy needs a fifth class `prospective` (§4 rows
  1-5) and a note that §5.6's glob-fragment rule now has one live instance
  (`-gate.md`). Successor note only — the filed policy stays as filed.
- O03/O04/O05: reproduce §6's numbers under rule D; if your recount uses rule C
  you will report the `prosody.md` phantom — treat that as a control failure, not
  a finding.
- to-verify: per-entry attribution of the +107 token delta vs r39's 2504.
- to-verify: whether `phonology-sanity.md` is a typo or an intended sibling (D4).

## Citations

- Claim/seat: `reports/round-42/claims.json:13-18`; `reports/round-42/targets.json`
  seat `O10` (`:103-109`).
- Defect origin: `reports/round-39/calib/Ca04-verify.md:78-93` (D1, wrapped field,
  the mangling left `to-verify`), `:114` (owed full recount), `:29-31` (filed
  arithmetic).
- Filed extractors: `reports/round-19/audit/entry-audit.py:31,74-96` (single line,
  rule A); `reports/round-35/cov/C14-audit-6-10.md:225-236` (block, `\n`, rule B);
  **`tools/gates/provenance-audit.py:76,244-260`** (live block, `" ".join`, rule C).
- Wrapped field: `corpus/knowledge/linguistics/phonetics-phonology.md:72-77`;
  intent confirmed `:279`.
- Policy: `reports/round-39/calib/basename-couples-policy.md:14-48` (§1-§2 classes),
  `:97-102` (§5.6 glob fragments).
- Command outputs (this seat, 2026-10-19, lane root, tree at `ac47c78`,
  `export TMPDIR=$PWD/.scratch PYTHONDONTWRITEBYTECODE=1`, all read-only, no filed
  bytes edited, no `run-validation.py` executed, no git/network/install):
  (a) `.scratch/o10_field_tokens.py` → wrapped-block tokens A=0, B=4 {prosody.md,…},
  C=4 {prosody.md,…}, D=4 {tone-prosody.md,…};
  (b) `.scratch/o10_rules3.py` → corpus totals A=2607, C=2611, D=2611; exactly one
  entry differs (phonetics-phonology); four-class D census
  `220/2611 → 2437/166/0/8`;
  (c) `.scratch/o10_census.py` → soft-wrap counts couples 1 field/5 lines,
  sources 48 lines, topic 15 lines; sub-bullet continuations sources 1358,
  verified-at 4;
  (d) `importlib` of `reports/round-19/audit/entry-audit.py` →
  `couples_targets` on the wrapped file = `([], [])`;
  (e) `importlib` of `tools/gates/provenance-audit.py` → `field_block(...,'couples')`
  = present True, content `...tone- prosody.md...`, empty False;
  (f) `ls`/`find` existence: `phonology-sanity.md` ABSENT,
  `phonology-sanity-gate.md` present, `sound-change.md`/`tone-prosody.md`/
  `phonology-basics.md`/`naming-and-onomastics.md`/`honorifics-and-register.md` ABSENT.
