# Report — ScoutSurface (round 91, kotodama, w1)

Seat: ScoutSurface (read-only scout). Lane: /home/vgpnk/Projects/shokunin/kotodama-shokunin.
Date: 2026-11-05. No URL fetched by this seat; no tool installed or upgraded; no lane file outside
my stage dir and this trailer was written.

## Files written

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/stage/ScoutSurface/surface.md`
  (21,264 bytes) — the full coverage surface (items 1–5 with commands, rc, and counts).
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-91/w1/ScoutSurface.md` — this trailer.
- Scratch (deleted before yield): `/fast/scratch/hyaku/kotodama-r91/ScoutSurface/`.

## Bytes used

Base coverage read from committed bytes at base `d39434b3bc8458e1b66edd2d0d0fea9ea32f3331`
(materialized with `git archive d39434b3 corpus | tar -x -C <scratch>/base-tree`, rc 0). Working-tree
coverage read from the working tree at freeze `691aebf247ebea4dd50577bb64ac99d12fa1145a` plus the
untracked/modified lane files. `git diff --stat d39434b3 -- corpus/knowledge` → empty (rc 0);
`git diff --stat d39434b3 691aebf -- corpus/knowledge` → empty (rc 0). The two trees differ in
`corpus/knowledge` only by the untracked pending entry.

## Numbers measured

1. Heading/topic-line matches naming a register term, term set = argot, cant, anti-language, ludling,
   Pig Latin, verlan, backslang, Polari, rhyming slang, secret language, jargon, slang, reversal
   (case-insensitive, non-alphabetic boundaries):
   **base 12 lines / 7 files; working tree 19 lines / 8 files.**
   Command: `grep -rnEi '^(#{1,6} |- topic:)' corpus/knowledge | grep -Ei '(^|[^a-z])(argot|anti-language|ludling|cants?|pig latin|verlan|backslang|polari|rhyming slang|secret languages?|jargon|slang|reversals?)([^a-z]|$)'` (rc 0).
   Base owners: `linguistics/dialect-register-consistency.md` (:1, :3, :71),
   `linguistics/linguistic-anthropology.md` (:3, :115), `linguistics/register-lexicon-ceilings.md` (:3),
   `linguistics/sociolinguistics-registers.md` (:110), `myth-symbol/ritual-liminality.md` (:3),
   `synthesis/dialect-faction-map-workflow.md` (:2, :116), `synthesis/religion-language-co-evolution.md` (:3, :79).
   Working tree adds the pending entry `corpus/knowledge/linguistics/secret-and-ludic-languages.md` (:1, :3, :12, :61, :77, :95, :109).
   Excluded as substring artefacts: *polarity* (`calendar-festival-systems.md:3`, `purity-pollution-boundary-systems.md:4,23`), *overland* (`transport-mobility-lexicon.md:4`).

2. `corpus/SOURCES.md` rows whose `scope` or `teaches` cell names one of those terms:
   **working tree 5 rows (S414 tier A mined; S952 B mined; S953 B mined; S954 A mined; S955 B mined); base 1 row (S414 only).**
   Command: `awk -F'|' '/^\| S/ {s=tolower($6" "$8); if (s ~ /(^|[^a-z])(argot|anti-language|ludling|cants?|pig latin|verlan|backslang|polari|rhyming slang|secret languages?|jargon|slang|reversals?)([^a-z]|$)/) print $2" tier="$5" status="$9}' corpus/SOURCES.md` (rc 0).
   Registry size: base 875 rows (last id S951), working tree 880 rows (last id S956, +S952–S956).
   S956 (rejected, tier C) is **not** counted: its scope/teaches cells name no register term; only its source cell reads "Wikipedia, Argot". S414's "reversal" is heraldic, a lexical false positive.

3. Duplication check for the four captures: at base **no** registry row covers Polari, verlan, Harman's
   *A Caveat for Common Cursitors*, or any argot/anti-language work — measured hits in the base
   `corpus/SOURCES.md`: Halliday 0, Baker 2002 / "Lost Language" 0, Polari 0, "Caveat for Common" 0,
   Gotowski 0, Maurer 0, "Big Con" 0, Grose 0, LEME lex 109 0, lancaster Baker Polari page 0,
   taylorfrancis 10.4324/9780203167045 0, openedition cdlm/729 0. So S952–S955 are net-new rows over
   sources the corpus already cites in prose but never registered. The duplication risk sits in the two
   adjacent owners named in the frozen bounds — `linguistics/linguistic-anthropology.md` §5.3/§5.4 and
   `synthesis/religion-language-co-evolution.md` §6 — plus `linguistics/register-lexicon-ceilings.md`
   (verlan as a mechanical operation) and `linguistics/sociolinguistics-registers.md` (:35, :84).
   The pending entry handles the first (it names `linguistic-anthropology.md` §5.3 as the adjacent owner
   at `:16` and states it does not reproduce that mechanism list), but it does not cite
   `religion-language-co-evolution.md`, `register-lexicon-ceilings.md`, `sociolinguistics-registers.md`,
   `dialect-register-consistency.md` or `trade-economy-lexicon.md` anywhere (0 grep hits for each).

4. Verdict: **no dedicated entry at base.** The mandated command
   `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin ls-tree -r --name-only d39434b3bc8458e1b66edd2d0d0fea9ea32f3331 corpus/knowledge | grep -Ei 'argot|slang|secret|ludic|cant|jargon|pig|verlan|polari'`
   produced **no output (zero lines)**, grep rc 1. Supporting: `git ls-tree -r --name-only d39434b3 corpus/knowledge | grep -Eic '(secret|ludic|argot|slang|cant|jargon)'` → 0 (rc 1);
   linguistics partition at base = 35 files (`git ls-tree -r --name-only d39434b3 corpus/knowledge/linguistics | wc -l`);
   `git cat-file -e d39434b3:corpus/knowledge/linguistics/secret-and-ludic-languages.md` → rc 128 ("exists on disk, but not in d39434b3").

## What I could not measure / unresolved

- The frozen claim's "Topic lines name the register in 13 linguistics entries" is **not reproducible** from
  the narrow term set: the claim's own `topic_phrases` (argot;anti-language;backslang;ludling;cant;in-group concealment)
  match 3 linguistics topic lines at base (4 corpus-wide); a register-family set reaches 12, and 13 only when
  pun/riddle/word-play/child vocabulary is added. The narrow-set figure (3) is what the frozen list yields.
- **Date divergence flagged, not fixed (no write by this seat):** base corpus dates Harman **1566**
  (`linguistics/linguistic-anthropology.md:125`, `culture-material/trade-economy-lexicon.md:103`), while the LEME
  capture (`reports/round-91/evidence/S954.txt`, `LEMEdate:"1567"`, `lextitle:"... (1567)"`), the manifest and the new
  registry row S954 give **1567**. Base rows are append-only, so the L1 should decide whether the entry names the divergence.
- I did not verify the scholarly truth of any statement in the pending entry; this seat measured coverage only.

## Tooling

No tool installed or upgraded; no pacman/uv/npm transaction; no sysctl touched. Nothing to record beyond that.
