# Round 3 lessons (2026-10-17) — D2 end-to-end build + direct triage

## End-to-end domain task (SHONEN box 2) — depth

The lane designed a second miniature culture (D2, highland pastoralists,
verticality+wind spine) from its own corpus: 14 components written by a
34-agent token-plan swarm, the missing 15th (13-naming) authored at assembly,
merged by `tools/assemble-d2.py` into `examples/culture-d2/packet.d2.yml`,
and graded by five culture gates + two provenance runs with frozen outputs
under `tools/gates/frozen/round-3/` (MANIFEST.tsv pins gate/input/output
sha256s). Gate verdicts on the v1 design: phonology 3 REVIEW (declared
allophones), lexicon clean, myth 1 (symbols lack `medium`), costume 10
G-ERA (E0/E1/E2 tags vs nine named eras), naming 20 (one real inventory
violation — Humweha's coda — plus English-garment-description noise and
derivation-adapter holds). Findings are the product: the gates grade the
design, they do not certify it.

Lessons: (1) component writers must share an ID registry BEFORE writing —
the brief agent renumbered the registry mid-flight and two reviewers
reviewed ABSENT files; cross-reference-by-ID, never-by-file, saved the
merge. (2) A deterministic merger script beats manual stitching; gates
caught one real assembly bug (era_dates vs open bounds, exit 2) that a
hand merge would have silently shipped. (3) Gate exit-2 is a tool/assembly
contract failure, not a design finding — separate the two when reading
verdicts. (4) The opencode-go lane failed routing ("missing
x-opencode-session") twice; the assembly moved to codex sol-high — record
lane outages as lessons, they are fleet-relevant.

## Freshness — orchestrator-direct triage + counting caveat

The 7 provider-filter-blocked files: after three content-filter strikes on
the alibaba lane, the orchestrator triaged the two non-civilization files
directly (12 flag-lines: 9 resolved — Jay & Jay 2015 exact title confirmed
(Language Sciences 52:251–259), Carol Leigh 1979 coinage confirmed (Leigh
1997:229; AP obit 2022), loo etymology marked uncertain per OED, swearing
periodization sourced (Hughes 1991; Mohr 2013), Martin of Braga marked
conventional attribution, bìhuì renamed-title cases downgraded; 3 lines are
policy mentions of the flag convention, not claims). The 5 civilization
files (39 flags: ottoman, slavs-early, sogdian-silk-road, tibet,
turkic-steppe) carry to round 5 on the zai lane — a different provider
without the alibaba filter.

Counting caveat (calibration): the grep flag-sum counts convention
mentions ("flag every to-verify before it touches the bible") as if they
were claim flags. From round 4 the freshness counting command excludes
policy mentions (count lines matching `(to-verify)` NOT in convention/
checklist contexts); the raw sum stays recorded alongside.
