# ReviewGateQuoteTool — residual falsify check of `check-gate-quotes.py` (round 54 a2)

Scope: attack only. Target `/fast/scratch/hyaku/kotodama-r54-a2/ExecGateQuoteCheck/check-gate-quotes.py`
(sha256 `81bbef86b3bc4a7424f34cd1560f84c31e8be2aa90c503daa88d668d31bff2bf`, matches the sha declared in
`.ufo/waves/round-54/build-a2/ExecGateQuoteCheck.md`). Working copy, mutants and fixtures live in
`/fast/scratch/hyaku/kotodama-r54-a2/ReviewGateQuoteTool/`. No lane file outside this report was written.
Read-only `git`/`jj`: none needed. No source was re-opened from the web (this seat attacks tool behavior, not
row fidelity); Python 3.14.8 stdlib only; **no installs**.

## Verdict

**ABLE TO FAIL: YES.** All three mutants are killed by the selftest, by the build seat's red fixtures, and by
real lesson lines; the named round-53 findings reproduce byte-for-byte. The tool is a real check, not a
no-op. Residual gaps exist (5 adversarial escape classes, below) but none affects the findings it already
reports on the lane's lessons.

## 1. Selftest — CARRIED

`python3 -B check-gate-quotes.py --selftest` → 12/12 PASS, exit 0 (case list identical to the build
report's transcript). Copy verified against the declared sha256 before running.

## 2. Real lessons, named findings — CARRIED

Command: `python3 -B check-gate-quotes.py corpus/lessons/round-53.md round-52.md round-51.md` (absolute
paths). 21 findings, exit 1, byte-identical to the build report's tables:

- round-53.md:42 S187=28, :49 S189=28, :58 S192=40, :62 S194=28, **:84 S200=27, :109 S205=36, :110 S205=30,
  :111 S205=26, :128 S214=27, :133 S217=11 (ellipsis-joined), :160 S224=28, :181 S236=29** — the routed five
  (S200, S205 ×3, S214, S224, S236) all present at the exact lines the report names.
- round-52.md:34 S096=23 (ellipsis-joined), :59 S139=26, :66 S140=27, :68 S142=34, :87 S155=31, :94 S159=30,
  :99 S164=29.
- round-51.md:33 S076=34, :78 S121=30.

## 3. Three new mutants — all killed (CARRIED)

Mutants + runs under `/fast/scratch/hyaku/kotodama-r54-a2/ReviewGateQuoteTool/` (`orig.out`, `mutant-*.out`).

| mutant | one-line change | selftest kill | fixture kill | real lesson kill (diff vs original) |
|---|---|---|---|---|
| `mutant-cap26.py:67` | `MAX_WORDS = 25` → `26` | `26-words` and `curly-26-words` FAIL (want=1 got=0) | `fixtures/red-26-words.md`: 0 findings, exit 0 | `round-53.md:111 S205 words=26` and `round-52.md:59 S139 words=26` vanish (21→19) |
| `mutant-nocurly.py:74` | `QUOTE` drops the `“...”` alternative | `curly-26-words` FAIL | `fixtures/red-curly-26.md`: 0 findings, exit 0 | `round-53.md:133 S217 words=11` vanishes — that row is curly-quoted (`“The first two … have recognition as 'quotable gestures' or 'emblems'”`), so curly handling is load-bearing on a real line |
| `mutant-noellipsis.py:78` | `ELLIPSIS` → `(?!)` (never matches) | `ellipsis-joined` FAIL | `fixtures/red-ellipsis.md`: 0 findings, exit 0 | `round-53.md:133 S217 words=11` and `round-52.md:34 S096 words=23` vanish (21→19) |

Every mutant: selftest exit 1, fixture exit 0, and at least one real finding lost. The selftest is not
decorative — it catches two of the three mutants by name.

## 4. Adversarial Gate lines the tool misses — CARRIED (misses exist)

Fixture `adversarial.md` (five rows in a `## Gate` section): the original tool reports **0 findings, exit 0**.
All five escape:

1. `adversarial.md:5-6` (S901) — quote hard-wrapped across two physical lines (26 words): `QUOTE` forbids
   `\n` inside a span and the continuation line is not a `- S### ` row, so the whole quote is invisible.
   Smallest fix: in `gate_section`, merge a non-row, non-heading continuation line into the previous row
   before scanning.
2. `adversarial.md:7` (S902) — 26-word guillemet quote `«...»`: no span class matches guillemets. Fix: add
   `«[^«»\n]*»` to `QUOTE`.
3. `adversarial.md:8` (S903) — 25 whitespace tokens containing `mother-in-law` and `twenty-six` (= 28 words
   by a hyphen-splitting count): passes at 25. Counting-convention gap; fix is documentation, or split
   hyphenated tokens if the lane's word definition says so.
4. `adversarial.md:9` (S904) — `"eight words" … "fourteen words"` (22 words total): the ellipsis sits
   *between* two spans, so `ellipsis_joins` (which looks inside one span) never fires, and the run is under
   cap — two fragments joined by an omission marker presented as one continuous quotation go unreported.
   Fix: apply the both-sides-of-ellipsis test to the run's joined text, not only inside single spans.
5. `adversarial.md:10` (S905) — `* S905 — ...` row: `ROW` only matches `- `; an asterisk bullet is never
   scanned. Fix: widen `ROW` to `^[-*+]\s+` or document the `- ` requirement.

None of the five changes today's findings on rounds 51–53 (no wrapped rows, guillemet quotes, inter-span
ellipsis joins or `*` bullets in those Gates — verified by eye over the flagged lines; the guillemet/
asterisk shapes appear nowhere in the three lessons' Gate sections).

## 5. Round-54 Gate lines (`gate-lines.md` wrapped as `## Gate`) — 3 over-cap rows

`gate-lines-wrapped.md` (46 rows) → exit 1:

- `gate-lines-wrapped.md:21` **S255 words=38** — the row quotes the same 19-word passage twice (as locator
  and as quote); the `": "` gap has no word character, so the two copies join into one 38-word run.
- `gate-lines-wrapped.md:25` **S259 words=31** — same shape: `"I did not know of firam"` twice + a 19-word
  quote, joined by `": "` gaps.
- `gate-lines-wrapped.md:28` **S262 words=26** — `"My focus on the carved headpiece"` twice + the 14-word
  Mende quote = 26, over cap by 1.

This is the tool's documented anchor-join rule applied consistently (same shape it flags as S200/S214 in
round-53), not a false positive of the regex — but it is a calibration fact the L1 should see: **three rows
of the round-54 Gate as currently drafted will keep the tool red**, and the smallest fix is on the rows, not
the tool: quote the locator title once (or put any word-bearing character between locator and quote), and
for S262 trim or split the 14-word quote.

## Counts

- Selftest 12/12 PASS; lesson runs 21 findings (r53 12, r52 7, r51 2), exit 1 — all named findings confirmed.
- Mutants 3/3 killed (selftest + red fixture + ≥1 real lesson line each).
- Adversarial escape classes confirmed 5/5 (tool exit 0 on the fixture).
- Round-54 gate-lines scan: 3 findings (S255=38, S259=31, S262=26).
- Installs/upgrades: none. Writes outside this report: only under
  `/fast/scratch/hyaku/kotodama-r54-a2/ReviewGateQuoteTool/`.

## Unrun checks

- No web source re-opened (out of this seat's scope; quote fidelity untouched by this tool by design).
- Single-quote (`'…'`) span behavior not independently re-measured — I only note the build seat's claim that
  adding curly singles flags nothing new; my mutants did not touch it.
- Sweep of all 41 lesson files not repeated (build report's table not re-verified beyond rounds 51–53).
- No CRLF/BOM, `### Gate` (h3 heading), or `>`-blockquote row probes; no fuzzing beyond the five classes.
- gate-lines.md rows were not re-opened against their sources (row fidelity is the other residual seats' job).
