# MutationTesterV4 — r93-v1 report

Ten NEW single-line mutants of `tools/check-advance-evidence.py` (sha256 `9799a96c…aae7`, verified before and after,
unchanged), none overlapping the 77 pairs in `reports/round-93/mutants.py`. Detector: each mutant's own
`--selftest --work <scratch dir>`. Baseline pristine run first: rc 0, `SELFTEST PASS 114/114` — all verdicts conclusive.

**Counts: 5 KILLED / 5 SURVIVED / 0 inconclusive.**

Killed (rc 1, selftest catches them): head-floor-3 (L576 `>= 2`→`>= 3`, 90/114), gate-extra-slice-2 (L736 `[1:]`→`[2:]`,
113/114), gradednorm-key-sha (L524 build key → sha256, 113/114), archive-year-le (L357 `<`→`<=`, 113/114),
manifest-msg-reword (L507 refusal message reworded, 113/114).

Survivors (rc 0, PASS 114/114) — coverage findings, entry-mode behaviour each would let through:

1. **script-strip-off** (L291 script/style strip removed): a capture quote existing only inside a `<script>`/`<style>`
   block still counts as located body text (generic tag stripping keeps block content). Counterfeit-exploitable: yes —
   paywalled body + quote only in embedded JSON-LD passes CAPTURE. The A6e fixture only exercises a `<meta>` attribute.
2. **comment-strip-off** (L292 comment strip removed): a quote existing only in an HTML comment counts as located.
   Counterfeit-exploitable: yes — `<!-- quote -->` on an empty page passes CAPTURE. No comment fixture exists.
3. **unescape-off** (L294 `unescape` removed): entity-encoded captures are falsely refused (strict direction; not a
   counterfeit channel). The decode step is unpinned in both directions.
4. **dispo-any-casei** (L113 `re.I` added, survives): shows the documented case-sensitivity of the unanchored
   disposition scanner (lines 111-112) is unpinned; pristine bytes never read lowercase unanchored verdict tokens, so
   a disposition flip written lowercase/unanchored (`s002 not located …`) evades APPENDONLY. Counterfeit-exploitable: yes,
   as an evasion channel.
5. **baserows-drop-cell8** (L676 cell 8 `opened` dropped): no fixture moves a base row's `opened` identity cell;
   OTHERCELLS guards population rows only, so `opened` rewrites on non-population base rows leave BASEROWS green.
   Counterfeit-exploitable: yes — provenance backdating/forward-dating of a base row.

Full rows with target lines, changes, rc, SELFTEST lines and survivor analysis:
`.ufo/waves/round-93/w1/stage/MutationTesterV4/mutants.md` (raw outputs alongside in `mutants-raw.json`).

Evidence hygiene: one driver run (`python3 driver.py`, rc 0, ~47 s) executed baseline + 10 mutant selftests; lane tool
sha256 before = after = `9799a96cf473278a75d19f51d93c4552cc94a611f7b008b36ef928c914ffaae7` (restoration evidence; bytes
never written). Scratch `/fast/scratch/hyaku/kotodama-r93/MutationTesterV4/` deleted on exit. No pacman/sysctl/network;
writes confined to the two stage files and this report.

Report: .ufo/waves/round-93/w1/MutationTesterV4.md
