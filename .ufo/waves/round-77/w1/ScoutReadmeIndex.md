# ScoutReadmeIndex — README integration recon

- **Observed:** the round-77 DRAFT claim C names one entry, `corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md`, and requires a README index row + footer (`.ufo/waves/round-77/CLAIMS-DRAFT.md:22-25,53-59`). The staged source is `/home/vgpnk/Projects/shokuknow/merge/kotodama/knowledge/corpus/knowledge/linguistics/naming-systems.amend-2026-10-23.md`; its topic is the multi-line text captured in plan artifact.
- **Observed:** README at base has `## linguistics/ (32)` and 30 rows within that section; two extra linguistics rows are under `## Round 73 additions` (`corpus/README.md:344-374,789-795`). Existing sections/footer end at 836.
- **Observed:** base per-partition `.md` counts, measured with `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree --name-only 211f9526800906e0c585d878d265c37e5e090c15 corpus/knowledge/<dir>/ | grep -c '\.md$'`:
  - 95 — `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree --name-only 211f9526800906e0c585d878d265c37e5e090c15 corpus/knowledge/civilizations/ | grep -c '\.md$'` → `95`
  - 41 — `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree --name-only 211f9526800906e0c585d878d265c37e5e090c15 corpus/knowledge/culture-material/ | grep -c '\.md$'` → `41`
  - 32 — `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree --name-only 211f9526800906e0c585d878d265c37e5e090c15 corpus/knowledge/linguistics/ | grep -c '\.md$'` → `32`
  - 32 — `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree --name-only 211f9526800906e0c585d878d265c37e5e090c15 corpus/knowledge/myth-symbol/ | grep -c '\.md$'` → `32`
  - 29 — `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree --name-only 211f9526800906e0c585d878d265c37e5e090c15 corpus/knowledge/synthesis/ | grep -c '\.md$'` → `29`
  - 24 — `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree --name-only 211f9526800906e0c585d878d265c37e5e090c15 corpus/knowledge/verification/ | grep -c '\.md$'` → `24`
- **Observed:** total 253 — `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree --name-only -r 211f9526800906e0c585d878d265c37e5e090c15 corpus/knowledge/ | grep -c '\.md$'` → `253`.
- **Inference:** a single new linguistics file yields 254 total and vector 33/32/41/29/24/95 in README section order. Thus `## linguistics/ (32)` must become `(33)` for the r76 INDEX rule.
- **Observed:** r76 INDEX frozen contract in `reports/round-76/accept-c.py:4301-4312`, implemented at `4393-4621`: row must be in matching partition section and topic-verbatim; all headings equal live `.md` counts; last footer equals live total/vector; base footer blocks preserved; only rows, heading count parentheticals, and appended total/footer block are exempt. **Inference:** r77 likely inherits this unless its not-yet-frozen counter changes it. Do not add a new revision paragraph/section.
- **Observed:** `_entry_topic` at `reports/round-76/accept-c.py:4375-4386` reads the single physical `- topic:` line only. Landed `conlang-scholarship.amend-2026-10-23.md` has one-line topic (`git show 211f952…:corpus/knowledge/linguistics/conlang-scholarship.amend-2026-10-23.md | grep -n 'topic:'` → line 13). **Inference/risk:** new landed amendment must have one-line topic matching the full row body; a folded topic will fail that implementation.
- **Inference:** place row in the linguistics section, between `morphological-typology.md` and `naming-systems.md`, in filename order. Footer block:
  `Total knowledge entries: 254.`
  `Counts checked 2026-10-27 from the repo root: \`find corpus/knowledge -type f -name '*.md' | wc -l\` (total 254 files; directory totals 33/32/41/29/24/95).`

**Stale-line forecast:** L344 heading `(32)` requires update to `(33)`; L755/757–768 (243 total/footer), L798/800 (247), L819/821 (249), L830/832 (252), L834/836 (253) are older count/footer blocks preserved as history, not rewritten. L791's dated “partition holds 32 files” becomes historical/stale; the dated block itself must remain unchanged under append-only INDEX. Other partition headings remain correct. The full proposed row/footer and risk notes are in `.ufo/waves/round-77/w1/stage/ScoutReadmeIndex/readme-plan.md`.

**Unrun:** no r77 INDEX counter is frozen yet, so the inherited r76 exemption assumptions are not validated against final r77 machinery. No tests/builds run. No tools installed.

Report: `.ufo/waves/round-77/w1/ScoutReadmeIndex.md`
