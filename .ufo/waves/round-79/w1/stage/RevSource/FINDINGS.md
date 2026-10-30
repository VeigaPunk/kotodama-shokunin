# RevSource — own-work S897 provenance tier / quote / source benefit (round 79 W1)

Seat: RevSource (leaf, reviewer). Lane base `44f76d456c1b326a71ffdb381590af825cbf11be`.
No git/jj mutation anywhere. All probes read-only against committed bytes; the only
writes are this stage dir and `/fast/scratch/hyaku/kotodama-r79/RevSource/`
(scratch, removed after receipt copy). Raw probe output preserved under `probes/`.

## 1. What the draft asks

`.ufo/waves/round-79/CLAIMS-DRAFT.md` (O paragraph): "Own-work source S897 will
cite the opened R77 mismatch evidence; no external-source or new knowledge coverage
claim." Peer seat ScribeLesson drafted the row at
`.ufo/waves/round-79/w1/stage/ScribeLesson/s897-row.draft.md`. This seat owns the
tier, the quote, and the source-benefit review of that draft (per RevOContract
o-clause-map.md:28, "RevSource seat owns the tier").

## 2. Evidence opened (all committed at base, all re-verified by this seat)

Document cited by the drafted row:
`.ufo/waves/round-77/w2/stage/ExecCaPass/graded-legs.txt`
- committed at base: `git cat-file -e 44f76d45…:.ufo/waves/round-77/w2/stage/ExecCaPass/graded-legs.txt` OK (probe-p-s.txt)
- blob sha256 at base: `6e97b121e98120f7d5fa6378f7cb5eebe6f8e0c520e90bd7c13503b3e124e52b` — byte-equal to the sha256 the draft row pins in its source cell (probe-p-s.txt)
- line 1 `LEG FAIL BASEMISMATCH`; line 2 carries exactly 10 occurrences of `recorded-observed-at-base='1'!='149'` (probe-p-s.txt PROBE Q/R)
- full 6-line body shows `BASEMISMATCH_PASSED=False`, `LEG FAIL REPAIR`, `REPAIR_PASSED=False`, `green-at-base=['D11']`

Corroborating record (R78-M1's other evidence pointer):
`.ufo/waves/round-77/w2/ScoutLogPairs.md`
- verdict at `:14-16` (20 words, ≤25): "Pairs D01–D10 are each invalid (fabricated
  recorded observation): `observed_at_base` records `"1"` while the real
  `observe_cmd` output parses to token `"149"`."
- per-pair row at `:47`: `| D01 | ANNOTATE | LOG.md:3 | yes | 2026 | 149 | yes | "1" | **NO** | [] | invalid: recorded obs "1" ≠ actual "149" |`
- raw re-run output at `:133`: `211f9526800906e0c585d878d265c37e5e090c15:LOG.md:149`
- blob sha256 at base: `d9e7224baa55afe985bbbb2dac19482470131a2b4b753d26baebb9003b9682e3` (probe-a-d.txt PROBE B)

The recorded lesson: `corpus/lessons/round-78.md:11` (R78-M1) names the red-before
as "W2's executed BASEMISMATCH failure on the recorded 11-pair probe".

Independent re-derivation by this seat (read-only, pinned r77 base):
- `git -C <lane> grep -c -E '^#' 211f9526800906e0c585d878d265c37e5e090c15 -- LOG.md`
  → `211f9526800906e0c585d878d265c37e5e090c15:LOG.md:149`, exit 0 (probe-e-g.txt PROBE E)
- probe ledger at base records `observed_at_base:"1"` ×10 (D01–D10), D11 `null`
  (probe-e-g.txt PROBE F/G) → recorded "1" ≠ actual "149" confirmed, D11
  `grep -o 'Total knowledge entries: [0-9]+'` emits five matches, first 243 ==
  stated 243 → green at base confirmed (probe-h-j.txt PROBE H)

Re-runnability of the receipt (tier-A grounding): copied
`graded-legs.py` + `ledger.json` (w2 stage) + `accept-ca.py`
(w1 stage, sha256 `ac2bc93d…89b2e`) into scratch and re-executed
`python3 graded-legs.py`; stdout sha256 `6e97b121…4e52b` — **byte-identical** to the
committed receipt (rerun/graded-rerun.txt vs rerun/graded-committed.txt,
`diff` clean). Tier-A's contract phrase "the lane's own re-runnable gate output"
is observed, not assumed.

## 3. Tier finding — A is correct, with the scope string doing the work

- SOURCES.md tier definition: "**A** — primary or authoritative for that scope
  (spec, official docs, source code, original paper, maintainer statement,
  **the lane's own re-runnable gate output**)."
- Precedent: rows S859/S860 (kind `own-work`, tier A) cite
  `tools/check-supersession-settlement.py` the same way — repo path + re-runnable
  command + anchor with blob sha + revision.
- The drafted row's tier A is grounded because the receipt reproduces byte-identical
  from committed bytes (§2). If L1 wants the conservative reading, tier B also
  passes census, but nothing observed supports downgrading: the run is pinned
  (base 211f9526…), the inputs are committed, the output reproduces.
- The scope cell's own qualifiers ("not an external source, not a freeze verdict,
  not knowledge") are honest and load-bearing: the receipt grades the W1 *probe*
  ledger, not any frozen round ledger, and O's CLAIMS-DRAFT disclaims "historical
  truth certification".

## 4. Quote finding — ≤25 words, exact path/line, date 2026-10-30

- Drafted anchor quotes: `:1` 「LEG FAIL BASEMISMATCH」 (4 words); `:2`
  「recorded-observed-at-base='1'!='149'」 — both `grep -n -F` located on the
  committed bytes (probe-x-y.txt PROBE Y: counts 1 and 1).
- Corroborating located quote (if L1 prefers the audit prose): ScoutLogPairs.md
  `:14-16`, 20 words (probe-x-y.txt).
- Both are body text of committed lane records — no caption/attribute re-scoping
  issue (QUALITY 16's scope is live-fetch rows; irrelevant here, URL=(none)).
- opened date 2026-10-30 = today; census E08 accepts present-date.

## 5. Source benefit — what S897 buys the lane

1. **Red-before stability for O.** The O guard's red fixture cites one registry
   id instead of inline `.ufo/...` paths. Under QUALITY 7, a claim's added lines
   may not name paths another claim lands; a registry row is the sanctioned way
   for the round-79 lesson/tool registry to point at pre-existing wave records.
2. **Census integration / discoverability.** Row lands at S897 (next free id,
   verified: 0 occurrences of S897 in `corpus/SOURCES.md` at base, last id S896 —
   probe-j2-l.txt PROBE J2). Mirror probe: rows 820→821, tier.A 493→494,
   status.queued 58→59, `validate --file` exit 0, **zero** E-codes, no S897
   findings (probe-v2-w2.txt).
3. **Honest provenance at the schema level.** kind `own-work` is a census enum
   value (E05 accepts it); URL=(none) in the source cell (probe-x-y.txt PROBE X),
   so QUALITY 10/16/18 live-fetch obligations do not bind; used-by will point at
   the lesson and the SKILL.md tool registry, never into corpus/knowledge — no
   knowledge-coverage claim rides on it (QUALITY 15 not triggered; it is a
   registry row, not a cited-line entry).
4. **The id reuse is legal but must be minuted.** The round-77 external-source
   candidate S897 (魏斌, CSSN page) never landed — round 77 honest-stopped; the
   staged row still exists read-only at
   `/home/vgpnk/Projects/shokuknow/merge/kotodama/SOURCES.append.md:45`
   (probe-m-o.txt PROBE N). If that naming-systems theme is ever revived, the
   staged S897 must be renumbered or adopted with a supersession note to avoid an
   E03 duplicate id. The round-79 lesson Gate should record that lane S897 is now
   the own-work row.

## 6. Census controls run by this seat (scratch mirrors, row inserted after S896)

| control | S897 finding | exit |
|---|---|---|
| as drafted (queued, used-by `—`) | none | 0 |
| tier `D` | `E06 S897 tier=D` | 1 |
| `mined` + used-by `—` | `W03 S897 mined but unused` | 1 |
| `mined` + used-by `corpus/lessons/round-79.md`, file absent | `E11 S897 missing used-by corpus/lessons/round-79.md` | 1 |
| `mined` + used-by `corpus/lessons/round-79.md`, stub present | none | 1* |

* residual exit 1 is S859/S860's used-by `corpus/lessons/round-69.md` /
  `round-70.md` missing in the fixture's empty lessons dir — fixture noise, not
  S897. First mirror attempt that appended the row at file end tripped
  `E12 S897 row outside Registry section` — the row must be inserted after S896
  inside `## Registry`, not appended at EOF (probe-v-w.txt).

Implication for the freeze: `queued` + used-by `—` is the only census-clean
pre-land shape (W03 would fire on `mined`+`—`; E11 on `mined`+missing path). The
flip to `mined` with used-by `corpus/lessons/round-79.md` must land in the same
commit as the lesson — exactly ScribeLesson's plan, now control-verified.

## 7. Boundaries / not claimed

- No external source was opened; no live fetch; no knowledge admission.
- The re-grade re-run exercised the W2 probe bytes only; the round-79 guard tool
  itself is `[PENDING-TOOL-PROOF]` by design (this seat ran no implementation
  check of it).
- Ca separability: the Ca correction record must not cite S897 (J7 class); the
  drafted row is O-side only.
