# Ca02 — resolver latent-edge successor row

- Seat: `Ca02` (claim **Ca**, calibration)
- Out: `reports/round-47/calib/Ca02-resolver-edge.md`
- Baseline: `6e9a30d` (`git rev-parse --short HEAD` → `6e9a30d`)
- Disposition: **recorded** successor defect — no fix claimed this round; the
  resolver body is byte-identical to its landed pin.

## 1. Measured facts

| # | check | command | output |
|---|---|---|---|
| 1 | lane HEAD | `git rev-parse --short HEAD` | `6e9a30d` |
| 2 | resolver digest | `sha256sum tools/harness/basename-couples-resolver.py` | `43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64` |
| 3 | parent queue digest | `sha256sum reports/round-40/op/defect-queue-v2.json` | `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907` (matches the r43 successor pin at `reports/round-43/calib/defect-queue-v2-successor-r43.json:7`) |
| 4 | resolver selftest | `python3 tools/harness/basename-couples-resolver.py --selftest` | `SELFTEST OK: 27/27 controls`, exit 0 |
| 5 | defect reproduced | import live resolver; `couples_block` / `couples_field` / `field_refs` on the fixture below | block `['language — \`tone-']`; joined `'language — \`tone-'`; refs `[]` |
| 6 | witness control | `python3 tools/harness/couples-reference-extractor.py .scratch/ca02-r47/hyphen_blank.md` | `wrapped=True tokens=2` → `tone-prosody.md` (unresolved), `writing-systems.md` (fallback) |
| 7 | live incidence | scan of all `corpus/knowledge/*/*.md` for a blank-separated indented continuation after a trailing-hyphen part | entries scanned `223`; hits `0`; same scanner on a scratch copy of the fixture (`positive` control) → `1` hit at lines 4/6, so the zero is a measured zero, not a blind scanner |
| 8 | control coverage | `grep -n "hyphen" tools/harness/basename-couples-resolver.py`; S7c fixture | `:56,:58` (docstring), `:84,:86,:88` (`join_parts` docstring), `:359` (S2b: non-blank hyphen wrap); S7c at `:411-415` is a blank line **without** a hyphen — no control combines blank + hyphen + indented continuation |
| 9 | exception is one branch away | local simulation with `soft_wrap = parts[-1].endswith("-")` (the `and not saw_blank` removed) on the same fixture | block `['language — \`tone-', 'prosody.md`; method — \`writing-systems.md']` — i.e. the documented behavior is implementable, the landed code just cannot reach it |

Fixture (`reports/round-47/calib/Ca02-resolver-edge.md` is the durable copy; the
scratch file `.scratch/ca02-r47/hyphen_blank.md` is not durable):

```markdown
# Fixture — hyphen soft-wrap after a blank line inside the couples field

- topic: fixture
- couples: language — `tone-

  prosody.md`; method — `writing-systems.md`
- verified-at: 2026-10-19
```

The live-incidence scanner, inlined for replay (run from the lane root; it
prints `live hits` and, if a fixture copy is placed under
`.scratch/ca02-r47/positive/`, `positive-control hits`):

```python
import glob, re
FIELD = re.compile(r"^- ([a-z][a-z-]*):[ \t]*(.*)$")
INDENT = re.compile(r"^[ \t]+\S")

def scan(pattern):
    hits = []
    for f in sorted(glob.glob(pattern)):
        lines = open(f, encoding="utf-8").read().splitlines()
        for i, line in enumerate(lines):
            m = FIELD.match(line)
            if not (m and m.group(1) == "couples"):
                continue
            parts = [m.group(2).strip()]
            blanks = 0
            for j in range(i + 1, len(lines)):
                f2 = lines[j]
                if not f2.strip():
                    blanks += 1
                    continue
                if FIELD.match(f2):
                    break
                if INDENT.match(f2) and blanks and parts[-1].endswith("-"):
                    hits.append((f, i + 1, j + 1))
                if INDENT.match(f2):
                    parts.append(f2.strip())
                    blanks = 0
                    continue
                break
    return hits

print("live hits:", len(scan("corpus/knowledge/*/*.md")))
print("positive-control hits:", len(scan(".scratch/ca02-r47/positive/*.md")))
```

The defect site in the live body:


- `tools/harness/basename-couples-resolver.py:55-59` — docstring: a blank line
  "terminates the block unless the previous part ends in a hyphen soft wrap and
  the next line is indented".
- `tools/harness/basename-couples-resolver.py:73` — `soft_wrap = parts[-1].endswith("-") and not saw_blank`.
- `tools/harness/basename-couples-resolver.py:74` — `if INDENT_RE.match(following) and (not saw_blank or soft_wrap):`;
  with `:73`, the second disjunct is unreachable whenever `saw_blank` is true, so
  the branch is exactly `not saw_blank`. The exception promised at `:55-59`
  cannot fire, and a genuine hyphen-wrapped continuation after a blank line is
  dropped together with every token on that continuation.

Live-impact statement, stated exactly: **0 live incidence in the 223-entry
corpus at `6e9a30d`**. "Zero tokens dropped" is true of the live corpus, not
universally true of the rule; the 27/27 selftest green does not exercise this
shape.

## 2. Fenced successor row

Schema-compatible with `reports/round-43/calib/defect-queue-v2-successor-r43.json`
(row fields: `id`, `origin`, `class`, `v2_class_equivalent`, `owner`, `reason`,
`next_touch`, `evidence`, `verification`). Ca06 copies this object verbatim into
the loop-1 queue successor; the id may be namespaced if that artifact uses a
different prefix, but the evidence and commands must not be reworded.

```json
{
  "id": "r44-resolver-hyphen-after-blank",
  "origin": "r44 R01-44-05 (reports/round-44/review/R01-review.md:290) and R02-44-11 (reports/round-44/review/R02-review.md:468); measured in r44 cross/X01-trades.md:114-155 (T1b, table row :26) and op/O03-defects-verify.md:221-229; carried in reports/round-46/loop-1-retrospective.md:49-50. Dedupe aliases: R01-44-05, R02-44-11, T1b.",
  "class": "recorded",
  "v2_class_equivalent": "carried-with-owner",
  "owner": "next resolver touch - tools/harness maintainer (r47+); the r47 O claim (freshness gate) is not the resolver owner and does not edit the pinned body",
  "reason": "Measured at HEAD 6e9a30d: the docstring at tools/harness/basename-couples-resolver.py:55-59 promises that a blank line does not terminate the couples block when the previous part ends in a hyphen soft wrap and the next line is indented. The code cannot take that branch: soft_wrap = parts[-1].endswith('-') and not saw_blank (:73) makes the second disjunct of :74 redundant, so after a blank line the block always breaks. On the inline fixture, couples_block returns only 'language — `tone-' and field_refs returns [] - both tone-prosody.md (captured by the r42 witness) and writing-systems.md are dropped. Live incidence at 6e9a30d is 0/223 entries, so 'zero tokens dropped' holds for the live corpus only, not universally for the rule; the 27/27 selftest green does not cover the shape (S2b :359 is a non-blank hyphen wrap; S7c :411-415 is a blank line without a hyphen). The body is pinned at sha256 43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64 and must not be edited in place; no fix is claimed this round.",
  "next_touch": "At the next resolver touch (r47+ tools/harness maintainer), choose and pin one behavior: (a) correct the docstring at :55-59 to 'a blank line always terminates the block' and add a selftest control asserting the fixture yields 0 refs (documents the limit), or (b) implement the documented exception (drop 'and not saw_blank' from :73) and add a control asserting the fixture yields tone-prosody.md + writing-systems.md. Do not leave docstring and code divergent. Any future 'zero tokens dropped' claim must be scoped to the measured corpus, never stated as a property of the rule.",
  "evidence": "tools/harness/basename-couples-resolver.py:55-59 (claim), :73-74 (unreachable branch), :359 (S2b), :411-415 (S7c); sha256 43ce341f783041cfa4af538a2ce9275729daf13fb6e118f0b5ac66308ab5ad64; reports/round-44/cross/X01-trades.md:26,114-155 (fixture measurement and live scan); reports/round-44/review/R01-review.md:290; reports/round-44/review/R02-review.md:468; reports/round-44/op/O03-defects-verify.md:221-229; reports/round-44/op/O10-census-verify.md:95 (soft-wrap identity: hyphen kept); reports/round-46/loop-1-retrospective.md:49-50.",
  "verification": "Commands run this seat at 6e9a30d: (1) import the live resolver, couples_block(fixture) -> ['language — `tone-'], field_refs(fixture) -> [] (2 tokens dropped); (2) python3 tools/harness/couples-reference-extractor.py .scratch/ca02-r47/hyphen_blank.md -> 'wrapped=True tokens=2' with tone-prosody.md unresolved and writing-systems.md fallback; (3) scan all 223 corpus/knowledge/*/*.md for a blank-separated indented continuation after a trailing-hyphen part -> 0 hits; (4) python3 tools/harness/basename-couples-resolver.py --selftest -> SELFTEST OK: 27/27 controls, exit 0; (5) sha256sum of the resolver and of reports/round-40/op/defect-queue-v2.json -> 43ce341f... and dfc9265d... respectively. Exact strings and the inline fixture are in section 1 of reports/round-47/calib/Ca02-resolver-edge.md."
}
```

## 3. Classing rationale (for Ca05 / Ca07)

`class: recorded` is deliberate. This round's deliverable is the durable record
of a measured limitation; no landed artifact closes the defect, and the pinned
body may not be edited, so `fixed-with-evidence` is false. The mission and the
r44 reviews (`R01-44-05`, `R02-44-11`) call for a successor note, not an edit
now. `v2_class_equivalent: carried-with-owner` keeps the owner + next_touch
visible in the v2 vocabulary, where only `carried-with-owner` and
`fixed-with-evidence` exist. `routed-with-owner` was considered and rejected as
the primary class: no fix work is owed inside r47, and no r47 seat owns the
resolver; the next_touch is advisory for the next resolver touch, not a claim
that this round routes work to a seat.

The row does **not** claim the resolver is broken for the live corpus. It
claims the opposite and pins the scope: 0/223 live incidence, with a rule-level
drop proven by fixture.

## 4. Integration instructions

- Ca06: copy the fenced object into the loop-1 queue successor. Keep the row's
  `evidence` and `verification` strings byte-identical; if the successor schema
  requires a different id prefix, change only `id` and record the alias in
  `origin` (already present).
- The parent `reports/round-40/op/defect-queue-v2.json` must remain
  byte-identical at `dfc9265d094aad50c3dedaadc301eda5b1a3aa3e557ed2c67f3833f0a3253907`.
  Re-run `sha256sum` before and after assembly; a mismatch means the parent was
  edited in place, which this successor forbids.
- No `corpus/` or `tools/` file is changed by this seat. The fixture lives in
  this artifact and in non-durable `.scratch/ca02-r47/` only.

## 5. Boundary and provenance

Only `reports/round-47/calib/Ca02-resolver-edge.md` was written. No filed byte
was edited or staged; no round runner was executed; no corpus staging; no git
mutation, network, or install. Scratch fixture under `.scratch/ca02-r47/` is
ephemeral and its content is inlined in section 1.

Commands run (full list):

```
git rev-parse --short HEAD
sha256sum tools/harness/basename-couples-resolver.py reports/round-40/op/defect-queue-v2.json
python3 tools/harness/basename-couples-resolver.py --selftest
python3 tools/harness/couples-reference-extractor.py .scratch/ca02-r47/hyphen_blank.md
grep -n "soft_wrap = \|not saw_blank or soft_wrap" tools/harness/basename-couples-resolver.py
grep -n "hyphen" tools/harness/basename-couples-resolver.py
# scanner: all corpus/knowledge/*/*.md for blank-separated indented continuation after a trailing-hyphen part
# import of the live resolver on the inline fixture (couples_block / couples_field / field_refs)
# local simulation of the documented exception (drop `and not saw_blank`)
```
