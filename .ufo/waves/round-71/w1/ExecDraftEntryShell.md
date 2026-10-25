# ExecDraftEntryShell — round 71, wave 1 (claim C coverage entry shell)

Seat: L1Kotodama71.ExecDraftEntryShell (leaf; no delegation, no background jobs, no labrat needed — no falsifiable hypothesis was open that required one; all facts read directly from the repo).

## Deliverable

Scratch structure draft (NOT final text, corpus path never written): **`/tmp/round71-claimC-entry-shell.md`** (13,746 bytes, written 2026-10-25).

Target (per claim C): `corpus/knowledge/culture-material/dance-performance-movement-codes.md` — verified absent at base `b94a543c70f40dba7e49fff96d05bfb8bbd8c678` (`ls` → no such file; partition census = 35 files).

## What the shell contains (claim-predicate-faithful)

1. **Provenance trio**:
   - `- source:` authority line — every cited bullet carries exactly one S id, restating only that row's quoted passage (matches `tools/check-cited-lines.py` single-id-per-line discipline; I read the tool: `SID = \bS\d{3,}\b`, line scan returns single/multi/table kinds).
   - `- verified-at:` line — drafted with base revision and the measured readings (partition census 35, absence sweeps); M11 final sweep marked `<FILL>` until rows land.
   - `- recheck:` line — dated-practice/etymology/occasion triggers.
2. **`- gap filled:` line** — embeds the two claim-before sweeps verbatim (`find corpus/knowledge/culture-material -maxdepth 1 -type f -name '*danc*'` → nothing; `grep -rniE '^- topic:.*(danc|choreograph|movement culture)' corpus/knowledge/culture-material/*.md` → nothing) plus the culture-material=35 census, and names partial owners cited one-way (music-instrument-lexicon.md via bugaku; calendar-festival-systems.md; games-play-sport-contests.md; masks-masquerade.md; costume-semiotics.md; sumptuary-law-rank-display.md; civilization-level owners siam-thai khon / maori haka / taino batey).
3. **`- topic:`** one line covering all seven axes, "reference and generative method, not fictional canon".
4. **`- sources:` bullet list** — in-corpus anchors block + external-shelf block with 19 named row slots, each literal `<S###>`.
5. **`- couples:`** — 13 targets, all verified to exist at this HEAD: music-instrument-lexicon.md, calendar-festival-systems.md, games-play-sport-contests.md, masks-masquerade.md, costume-semiotics.md, ritual-garments.md, sumptuary-law-rank-display.md, material-culture-inference-method.md, linguistics/gesture-co-speech-pointing.md, linguistics/speech-surrogates-whistled-drummed.md, linguistics/orality-formulaic-language.md, myth-symbol/ritual-liminality.md, synthesis/worldbible-integration-contract.md.
6. **Scope/refuses lines** — `- scope:` (partition-only, no canon, ends at handoff) and `- refuses:` (deliberate non-decisions + one-way non-restatement boundaries).
7. **Section headings** exactly as assigned: §1 movement vocabulary, §2 space & stage types, §3 choreographic codification, §4 music-dance-voice coupling, §5 festival-ritual performance, §6 power-and-social roles of performance, §7 worldbuilding application; plus standard corpus tail sections §8 calibration shelf, §9 limits and evidence, §10 handoff. Each section carries a register-framing line and per-slot bullets.
8. **Placeholders**: every evidence slot uses literal `<S###>` (the exact placeholder required), distinguished by bracketed slot labels (MV/SP/CH/MD/FR/PR/WB/CB); 19 slots ≥ the claim's 12-row minimum. Each slot is a one-row-per-bullet citation site.

## Evidence/observations feeding the shell

- SOURCES registry read: current max row **S860** (tails of `corpus/SOURCES.md`), so claim-C rows opened this round will land at **S861+** (scout-assigned; shell does not presume exact ids — placeholders cover them).
- Row shape confirmed from registry (id | source | type | tier | scope | quote | summary | status | opened | recheck | used-by): every new row needs tier A/B, status `mined`, opened 2026-10-25, and used-by cell listing the entry path — the shell's sources block states this contract.
- `tools/check-cited-lines.py` read: exit 0 requires S-id citations in the entry; one id per line is the safest shape (multi-id lines are flagged as MULTI-ID by the tool), hence the one-row-per-bullet discipline encoded in the shell.
- Claim C "before" sweeps and the partition-count target (35 → 36) taken directly from `reports/round-71/claims.json` (frozen).

## Risks / things the executor must close

- **ScoutOpenSourcesC must actually open ≥12 tier A/B rows** (status mined, used-by this entry) — the claim's kill rule fails on fewer. The shell's 19 slots exceed the minimum, so a 12–19-row landing is sufficient.
- Final fill must replace every `<S###>` with a real S id **and** keep one-row-per-bullet; then run `python3 -B tools/check-cited-lines.py corpus/knowledge/culture-material/dance-performance-movement-codes.md` (must exit 0).
- The round lesson Gate must quote each cited row (claim C predicate), and the registry used-by cells must list the entry path.
- `- verified-at:` needs its final M11 sweep after the rows land (couples resolution count, live spot-check per row).

## Tooling record

No tools installed/updated (nothing new was needed; reads used existing repo files). pacman untouched (paused host-wide); no uv/npx/cargo installs performed.

## Scope compliance

Leaf seat: no subagent dispatch, no background jobs, no repo mutation. Wrote only: the scratch draft in /tmp and this report at `.ufo/waves/round-71/w1/ExecDraftEntryShell.md`. Nothing else touched; no frozen files edited; no git/jj operations.
