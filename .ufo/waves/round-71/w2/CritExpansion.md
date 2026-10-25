# CritExpansion — round 71 wave 2 (falsify seat)

Scope: is claim C a genuine **expansion** under `LEARNING.md` (trend table, row
"expansion": "admitted `knowledge/` entries on ground the coverage map did not
hold, each `source:` citing a `mined` `corpus/SOURCES.md` row … net new admitted
entries on uncovered ground, each citing its coverage-map row")? Base =
`b94a543` (claims.json `base_revision`), measured at lane HEAD `14c88d9`.
Read-only; no lane bytes written except this file. No tools installed.

## Verdict

**PASS. Claim C is a genuine expansion.** The coverage map had no dance row
before. README now lists the dance entry. The entry cites 13 new, mined rows on
ground no file or sibling lane owned.

There are four non-blocking defects, F1–F4 below. None changes the
ACCEPT-C-71 result.

## Legs (PASS/FAIL with exact commands)

| # | Leg | Command | Result |
|---|---|---|---|
| 1 | Base coverage map had no dance row | `git show b94a543:corpus/README.md \| rg -n -i "danc\|choreo\|movement\|performance\|perform"` | **PASS.** The only hits are instance mentions inside other rows. In `civilizations/`: `lakota-plains.md` ("Sun Dance structure"), `maori.md` (haka), `siam-thai.md` (khon), `taino.md` (batey), `amazigh-berber.md` (asefru), `java-majapahit.md` (court performance). In `linguistics/`: `orality-formulaic-language.md`. No row owns dance or movement as a register, and no filename contains `danc`. |
| 2 | Base Known-gaps (frontier) list | `git show b94a543:corpus/README.md \| sed -n '592,722p' \| rg -i "danc\|perform\|movement"` | **PASS**, though dance was **not** on the frontier list; see F1. |
| 3 | README now lists it | `rg -c '^- \`dance-performance-movement-codes.md\`' corpus/README.md` → 1 | **PASS.** The row sits under `## culture-material/ (36)` between `cuisine-food-lexicon.md` and `dress-through-eras.md`. The README row text is byte-identical to the entry's `- topic:` line (`cmp` → MATCH). |
| 4 | README reconcile | `python3 -B reports/round-28/readme/sweep.py` | **PASS.** Exit 0, `header_drift {}`, totals 243, footer dir_totals 30/29/36/29/24/95 equal live. |
| 5 | Partition and corpus counts | `find corpus/knowledge/culture-material -maxdepth 1 -type f \| wc -l` → 36; `find corpus/knowledge -type f -name '*.md' \| wc -l` → 243. Base: `git ls-tree -r --name-only b94a543 corpus/knowledge/culture-material \| awk -F/ 'NF==4' \| wc -l` → 35; corpus → 242. | **PASS** (35→36, 242→243). |
| 6 | Registry growth equals the new rows | `grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}' corpus/SOURCES.md` → 797; base → 784 | **PASS** (+13 = S861–S873). `git diff b94a543 HEAD -- corpus/SOURCES.md` shows only the 13 additions plus the S860 Ca repair. |
| 7 | Rows are new sources, not re-cited old ones | URL check on base `SOURCES.md` for all 13 URLs (tango, mevlevi, chhau, oruro, flamenco, talchum, kabuki, abt.org, royalacademyofdance, ickl.org, natyashastra, mirror-of-gesture, plato…/dance) | **PASS.** All 0 at base. |
| 8 | Each row is mined, used-by the entry, and the path exists | `python3 -B reports/round-71/accept-c.py` | **PASS.** All 7 legs pass; `ACCEPT-C-71: PASS`, exit 0. ROWS leg: `missing=[] not-mined=[] usedby-missing=[]`. |
| 9 | check-cited-lines | `python3 -B tools/check-cited-lines.py corpus/knowledge/culture-material/dance-performance-movement-codes.md` | **PASS.** 0 findings, exit 0. |
| 10 | Corpus-wide owner sweep (stronger than the partition-scoped declared sweep) | `git ls-tree -r --name-only b94a543 corpus/knowledge \| rg -i "danc\|perform\|choreo\|movement\|theat\|kinesi"` → nothing. `git grep -n -i -E '^- topic:.*\b(danc\|dance\|dances\|dancing\|choreograph\|performance\|movement culture)' b94a543 -- corpus/knowledge` → 5 civilization topic lines (instances only). | **PASS.** No register-level owner anywhere in the corpus. The heaviest base holder is `lakota-plains.md` with 12 word-bounded dance tokens, all about the Sun Dance. |
| 11 | Content overlap with neighbors | `git grep -l -i -E '<term>' b94a543 -- corpus/knowledge` for Labanotation/Kinetography, Benesh, aṅgahāra, abhinaya, flamenco, chhau, talchum, Oruro | **PASS.** All 0 at base. Some anchors were partially held: Nāṭyaśāstra in 2 files (`india-classical-sanskrit.md`, `music-instrument-lexicon.md`), kabuki in 1, aragoto/wagoto/onnagata in `dress-through-eras.md`, tango in 1. Notation systems and the movement-unit hierarchy are new ground. |
| 12 | Sibling ownership (contested scope) | `rg -l -i -w "dance\|choreography" --glob '*-shokunin/*.md' --max-depth 2 /home/vgpnk/Projects/shokunin` → nothing | **PASS.** No sibling province owns dance. `PROVINCE.md` owns `culture-material/`, so this is in-province growth. |
| 13 | Quote spot-check (two rows, Wayback captures named in the Gate) | `curl -sL` on the S865 and S864 captures, tags stripped | **PASS.** S865: "Flamenco is an artistic expression fusing song (cante), dance (baile) and musicianship (toque)." This supports the triad sentence in the entry. S864: "the dancers walk the four kilometres of the processional route and repeat the journey for a full twenty hours without interruption." This matches the entry verbatim. |

## Findings (non-blocking)

**F1 — the claim's provenance label is wrong ("frontier → core").**
- **Counterexample:** `claims.json` labels claim C `type: "knowledge entry (sourced, frontier -> core)"`. But the base README `## Known gaps (frontier)` has no dance, performance, or movement item (leg 2), and `PROVINCE.md` has no Frontier list mentioning dance.
- **What actually happened:** the ground was un-mapped, and the entry moves it straight into core. It was never on the frontier.
- **Impacted axis:** coverage provenance and the expansion observable "frontier areas entered". That observable cannot be credited, because no frontier item existed.
- **Smallest correction:** in the round-71 report or lesson, describe the claim as "un-mapped → core", not "frontier → core". `claims.json` is frozen, so record the correction rather than editing it.

**F2 — S873 (SEP, "The Philosophy of Dance") is marked `mined` but supports no claim in the entry.**
- **Evidence:**
  - Counting S-ids after the header (`awk 'NR>18' <entry> | grep -c S873`) gives 0. Every other row has 1–2 body citations.
  - The only body trace is the unattributed calibration bullet "SEP's entry is tier B: a framing source…".
  - The Gate quote, "This is a vexed methodological question", supports no sentence in the entry.
- **Impacted axes:** source-status honesty, and the expansion observable "each `source:` citing a `mined` row". It would also hurt the claim's ≥12 margin if mined-status were audited strictly.
- **Not a kill:** the 12 body-cited rows (S861–S872) still meet the ≥12 target on their own.
- **Smallest correction:** either add one sourced sentence to the Calibration shelf that uses the SEP ephemerality or definition point, citing `(S873)`, or downgrade S873 from `mined` to `opened`/`studied` in a later round. A status change counts as an append-only correction row, per the lane's supersession rule.

**F3 — no "Known gaps" neighbor line for round 71, unlike rounds 64–67.**
- **Evidence:** in `git diff b94a543 HEAD -- corpus/README.md`, the Known-gaps section gains no line. Rounds 64, 65, 66 and 67 each added "Round N adds … Partial-scope neighbors remain …". Round 68 also skipped it, so the convention is drifting.
- **Related gap in the entry:** its `- gap filled:` line names four partial owners (`masks-masquerade`, `dress-through-eras`, `gesture-co-speech-pointing`, `transport-mobility-lexicon`). It omits the five base civilization topic-line owners (leg 10: `lakota-plains`, `siam-thai`, `taino`, `amazigh-berber`, `java-majapahit`). It also omits `music-instrument-lexicon.md`, which already cited the Nāṭyaśāstra. Round 65 counted `civilizations/taino.md` as a partial scope in its own line.
- **Impacted axis:** coverage-map completeness. LEARNING requires each entry to cite its coverage-map row. The README row exists, but the map does not record the partial owners.
- **Smallest correction:** in a later round, add one README Known-gaps line: "Round 71 adds `dance-performance-movement-codes.md` … partial-scope neighbors remain `masks-masquerade.md`, `music-instrument-lexicon.md`, `civilizations/{lakota-plains,siam-thai,taino}.md`".

**F4 — the README footer date is stale.**
- **Evidence:** the footer still reads "Counts checked 2026-10-24 …". Its totals were changed to 243 and 36 on 2026-10-25 (diff hunk `@@ -720,11 +729,11 @@`).
- **Impacted axis:** freshness of the coverage-map record. This is cosmetic, and the sweep's `footer_ok True` does not check the date.
- **Smallest correction:** change the footer date to 2026-10-25 in the next README touch.

**Minor churn (no harm, noted for the NOHARM leg):** the README diff includes four blank-line-only hunks: +1 after revision 2.8, and −1 before each of `## myth-symbol/`, `## culture-material/` and `## civilizations/`. These are whitespace inside the README, which the NOHARM allowance already covers.

## Strongest counterexample tested

The argument against expansion was: "dance ground was already held in
`civilizations/` and `masks-masquerade.md`, so the entry re-covers held ground."

It is **refuted at register level**:
- No base file or README row owns dance or movement as a cross-cultural register (legs 1, 10).
- The entry's two core novelties have zero base hits: movement notation (Labanotation, Benesh, ICKL) and the movement-unit hierarchy (karaṇa → aṅgahāra).
- All 13 source URLs are new to the registry (leg 7).

The counterexample does **survive at instance level**: Sun Dance, khon, haka and batey were already held as civilization instances. That is why F3 asks the map to name them as partial neighbors.
