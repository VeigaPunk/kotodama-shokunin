# kotodama-shokunin — iteration log (append-only)

## 2026-10-17 — mint (round 0)

Minted under explicit operator directive (2026-10-17): "mint a new
shokunin, a linguistic shokunin; he will connect languages, cultures, and
be related to the lore and world bible, relating cultures, their myths,
symbolisms and eras to their linguistics and costumes", followed by an
operator dispatch of four 16-agent corpus-seeding swarms. Evidence:
`MINT.md`; roster scan `.ufo/scopes/kotodama-mint-20261017/mint-roster-scan.json`
(main repo); fleet `MANIFEST.json` `rounds[]` mint entry 2026-10-17.

Seed kit written: SKILL.md, PROVINCE.md, SHONEN.md (canonical),
AGENTS.md, SCORECARD.md, MINT.md; corpus skeleton
`corpus/knowledge/{linguistics,myth-symbol,culture-material,synthesis}/`.

Next iterations (claimed, falsifiable):
- Corpus seeding: 64 knowledge entries from four swarms (3×16 zai-flash,
  1×16 sol-max); counting command `find corpus/knowledge -name '*.md' | wc -l`.
- corpus/README.md index written and committed after swarm landing.

## 2026-10-17 — mint corpus seeding, waves 1–3 (operator-dispatched swarms)

Operator dispatch 2026-10-17: three 16-agent swarms on zai-5.3-flash
seeded the three reference partitions. Measured at entry time:
`find corpus/knowledge -name '*.md' | wc -l` = 48 — linguistics/ 16,
myth-symbol/ 16, culture-material/ 16. Every entry carries cited sources
with `(to-verify)` flags where uncertain and a calibration section where
frameworks are contested (per lane AGENTS.md). Swarm agents were assigned
single files and did not append LOG entries; this entry records the batch.

Remaining per the same operator dispatch: a 128-agent gpt-6.1-sol-max
wave to finish the mint — the synthesis niche (coupling craft), the
verification/provenance partition, and civilizational bases covering all
earlier-civilization traditions. GitHub remote created and first push
same day.

## 2026-10-17 — mint corpus finishing wave (128 sol-max) + remote

Operator dispatch 2026-10-17: one 128-agent swarm on gpt-6.1-sol landed
the remaining partitions. Measured: `find corpus/knowledge -name '*.md'
| wc -l` = 176 total — synthesis/ 24, verification/ 12, civilizations/ 92
(plus the 48 from waves 1–3). Counting command re-runnable; measured in
worktree at commit time. `grep -rc 'to-verify' corpus/knowledge
--include='*.md' | awk -F: '{s+=$2} END {print s}'` = 1258 provenance
flags. corpus/README.md (index) and corpus/QUALITY.md (admission bar)
written; SKILL.md corpus map updated; SCORECARD re-measured.

Remote: github.com/VeigaPunk/kotodama-shokunin (public, matching the
2026-10 `shokunin-<domain>`/sibling convention). First push carried the
seed kit + 48 wave-1–3 entries; this commit carries the finishing wave.
Fleet README index row added (main-repo commit `bc889c5`).

Probation standing: >=3 verified rounds still required before a roster
row; probation recorded in fleet MANIFEST.json rounds[] (type "mint",
2026-10-17).
