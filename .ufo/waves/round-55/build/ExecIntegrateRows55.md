# ExecIntegrateRows55 — Round 55 claim C

## Axes and result

- **Operability:** adapted the round-54 integrator for round 55; it writes `rows.md`, `map.tsv`, `gate.md`, and `sentences.md` in scratch, and uses a hard error when a block lacks the `teaches` sentence required for Gate grounds.
- **Calibration:** Gate rows keep the full `teaches` sentence, one quoted source span, and no repeated locator. Quote characters embedded in the URL, locator, passage, or grounds are HTML-entity encoded so rendered text is preserved without extra raw quote spans.
- **Coverage:** the run parsed 93 eligible blocks from 40 reports, merged two repeated URLs, and produced 91 rows. The 46 old Gate entries S239–S284 all matched by primary URL; all 46 now use the full teaches sentence.

## Files and boundaries

- Scratch implementation: `/fast/scratch/hyaku/kotodama-r55/ExecIntegrateRows55/integrate-rows.py`.
- Scratch diff fixture: `/fast/scratch/hyaku/kotodama-r55/ExecIntegrateRows55/compare-round54-gates.py`.
- Scratch artifacts: `/fast/scratch/hyaku/kotodama-r55/ExecIntegrateRows55/out-round54-final/{rows.md,map.tsv,gate.md,sentences.md}`.
- This report: `.ufo/waves/round-55/build/ExecIntegrateRows55.md`.
- No lane source, registry, lesson, or tool file was edited. No git/jj writes or package installs were made. LSP was not available in the provided tool set; this standalone script work had no repository symbols to refactor.

## Final integration run

Command (run from the lane root):

```sh
python3 -B /fast/scratch/hyaku/kotodama-r55/ExecIntegrateRows55/integrate-rows.py --reports /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2 --start 239 --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md --out /fast/scratch/hyaku/kotodama-r55/ExecIntegrateRows55/out-round54-final --used-by corpus/knowledge/culture-material/masks-masquerade.md --merge-duplicates --allow-long-quotes --exclude 'CriticCalibrationMasks\.md$'
```

Output (complete stdout and stderr transcript):

```text
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutGuleWamkulu.md:22 NEW-ScoutGuleWamkulu-1 — merged into the row of NEW-ReviewSacredAccess-5 (same url https://ich.unesco.org/en/RL/gule-wamkulu-00142)
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutHaudenosauneeStatement.md:21 NEW-ScoutHaudenosauneeStatement-1 — merged into the row of NEW-ReviewSacredAccess-3 (same url http://www.nativetech.org/cornhusk/maskpoli.html)
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:18 NEW-ReviewSacredAccess-1 — assigned id S239 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:18 NEW-ReviewSacredAccess-1 — seat kind 'record (tribal government statement)' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:18 NEW-ReviewSacredAccess-1 — seat kind 'record (tribal government statement)' filed as registry kind community (a community's own statement)
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:18 NEW-ReviewSacredAccess-1 — tier A downgraded to B: the registry census treats a community row as never tier A
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:33 NEW-ReviewSacredAccess-2 — assigned id S240 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:33 NEW-ReviewSacredAccess-2 — seat kind 'web (tribal office policy page)' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:33 NEW-ReviewSacredAccess-2 — seat kind 'web (tribal office policy page)' filed as registry kind community (a community's own statement)
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:33 NEW-ReviewSacredAccess-2 — tier A downgraded to B: the registry census treats a community row as never tier A
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:47 NEW-ReviewSacredAccess-3 — assigned id S241 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:47 NEW-ReviewSacredAccess-3 — seat kind 'record (community policy statement, verbatim reproduction)' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:47 NEW-ReviewSacredAccess-3 — seat kind 'record (community policy statement, verbatim reproduction)' filed as registry kind community (a community's own statement)
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:47 NEW-ReviewSacredAccess-3 — tier A downgraded to B: the registry census treats a community row as never tier A
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:63 NEW-ReviewSacredAccess-4 — assigned id S242 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:63 NEW-ReviewSacredAccess-4 — seat kind 'web (museum collections policy)' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:77 NEW-ReviewSacredAccess-5 — assigned id S243 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:77 NEW-ReviewSacredAccess-5 — seat kind 'record (intergovernmental listing summarizing a state-party ' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:77 NEW-ReviewSacredAccess-5 — the row's cells carry the access-control marker 'bypass'; tools/check-source-access.py flags such a row as unopened, so reword the cell before the row is filed (QUALITY criterion 10)
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutGuleWamkulu.md:22 NEW-ScoutGuleWamkulu-1 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:92 NEW-ReviewSacredAccess-6 — assigned id S244 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:92 NEW-ReviewSacredAccess-6 — seat kind 'web (museum exhibition record)' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:108 NEW-ReviewSacredAccess-7 — assigned id S245 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:108 NEW-ReviewSacredAccess-7 — seat kind 'web (tribal museum statement)' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:108 NEW-ReviewSacredAccess-7 — seat kind 'web (tribal museum statement)' filed as registry kind community (a community's own statement)
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:108 NEW-ReviewSacredAccess-7 — tier A downgraded to B: the registry census treats a community row as never tier A
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:108 NEW-ReviewSacredAccess-7 — the row's cells carry the access-control marker 'bypassed'; tools/check-source-access.py flags such a row as unopened, so reword the cell before the row is filed (QUALITY criterion 10)
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:122 NEW-ReviewSacredAccess-8 — assigned id S246 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ReviewSacredAccess.md:122 NEW-ReviewSacredAccess-8 — seat kind 'web (museum research report)' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutCham.md:32 NEW-ScoutCham-1 — assigned id S247 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutCham.md:32 NEW-ScoutCham-1 — seat kind "web (magazine article by the bearer country's documentation " filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutCham.md:68 NEW-ScoutCham-2 — assigned id S248 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutCham.md:103 NEW-ScoutCham-3 — assigned id S249 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutCommedia.md:28 NEW-ScoutCommedia-1 — assigned id S250 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutCommedia.md:49 NEW-ScoutCommedia-2 — assigned id S251 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutCommedia.md:49 NEW-ScoutCommedia-2 — seat kind "record (holding museum's catalogue record for the object)" filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutDeathMasksAncient.md:20 NEW-ScoutDeathMasksAncient-1 — assigned id S252 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutDeathMasksAncient.md:20 NEW-ScoutDeathMasksAncient-1 — seat kind 'record.' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutDeathMasksAncient.md:70 NEW-ScoutDeathMasksAncient-2 — assigned id S253 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutDeathMasksAncient.md:70 NEW-ScoutDeathMasksAncient-2 — seat kind 'record.' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutDeathMasksAncient.md:70 NEW-ScoutDeathMasksAncient-2 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutEgungun.md:53 NEW-ScoutEgungun-1 — assigned id S254 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutEgungun.md:75 NEW-ScoutEgungun-2 — assigned id S255 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutEgungun.md:96 NEW-ScoutEgungun-3 — assigned id S256 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutEgungun.md:96 NEW-ScoutEgungun-3 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutEgungun.md:115 NEW-ScoutEgungun-4 — assigned id S257 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutEuropeanCarnival.md:7 NEW-ScoutEuropeanCarnival-1 — assigned id S258 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutEuropeanCarnival.md:7 NEW-ScoutEuropeanCarnival-1 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutEuropeanCarnival.md:28 NEW-ScoutEuropeanCarnival-2 — assigned id S259 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutEuropeanCarnival.md:28 NEW-ScoutEuropeanCarnival-2 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutEuropeanCarnival.md:50 NEW-ScoutEuropeanCarnival-3 — assigned id S260 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutEuropeanCarnival.md:50 NEW-ScoutEuropeanCarnival-3 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutGelede.md:15 NEW-ScoutGelede-1 — assigned id S261 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutGelede.md:15 NEW-ScoutGelede-1 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutGelede.md:15 NEW-ScoutGelede-1 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutGelede.md:47 NEW-ScoutGelede-2 — assigned id S262 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutGelede.md:47 NEW-ScoutGelede-2 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutGuleWamkulu.md:54 NEW-ScoutGuleWamkulu-2 — assigned id S263 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutGuleWamkulu.md:54 NEW-ScoutGuleWamkulu-2 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutGuleWamkulu.md:86 NEW-ScoutGuleWamkulu-3 — assigned id S264 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutGuleWamkulu.md:86 NEW-ScoutGuleWamkulu-3 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutGuleWamkulu.md:118 NEW-ScoutGuleWamkulu-4 — assigned id S265 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutGuleWamkulu.md:118 NEW-ScoutGuleWamkulu-4 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutHaudenosauneeStatement.md:43 NEW-ScoutHaudenosauneeStatement-2 — assigned id S266 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutHaudenosauneeStatement.md:43 NEW-ScoutHaudenosauneeStatement-2 — seat kind 'web (official confederacy department page)' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutHaudenosauneeStatement.md:43 NEW-ScoutHaudenosauneeStatement-2 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutKwakwakawakw.md:17 NEW-ScoutKwakwakawakw-1 — assigned id S267 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutKwakwakawakw.md:17 NEW-ScoutKwakwakawakw-1 — seat kind 'web (community-institution exhibit)' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutKwakwakawakw.md:17 NEW-ScoutKwakwakawakw-1 — seat kind 'web (community-institution exhibit)' filed as registry kind community (a community's own statement)
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutKwakwakawakw.md:17 NEW-ScoutKwakwakawakw-1 — tier A downgraded to B: the registry census treats a community row as never tier A
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutKwakwakawakw.md:39 NEW-ScoutKwakwakawakw-2 — assigned id S268 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutKwakwakawakw.md:39 NEW-ScoutKwakwakawakw-2 — seat kind "record (holding museum's catalogue record)" filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMalagan.md:10 NEW-ScoutMalagan-1 — assigned id S269 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMalagan.md:30 NEW-ScoutMalagan-2 — assigned id S270 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMalagan.md:30 NEW-ScoutMalagan-2 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMalagan.md:49 NEW-ScoutMalagan-3 — assigned id S271 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMalagan.md:68 NEW-ScoutMalagan-4 — assigned id S272 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMalagan.md:68 NEW-ScoutMalagan-4 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMalagan.md:87 NEW-ScoutMalagan-5 — assigned id S273 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMalagan.md:87 NEW-ScoutMalagan-5 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMalagan.md:106 NEW-ScoutMalagan-6 — assigned id S274 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMalagan.md:106 NEW-ScoutMalagan-6 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMaskTheory.md:51 NEW-ScoutMaskTheory-1 — assigned id S275 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMaskTheory.md:73 NEW-ScoutMaskTheory-2 — assigned id S276 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMaskVoice.md:18 NEW-ScoutMaskVoice-1 — assigned id S277 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMaskVoice.md:18 NEW-ScoutMaskVoice-1 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMaskVoice.md:41 NEW-ScoutMaskVoice-2 — assigned id S278 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMaskVoice.md:63 NEW-ScoutMaskVoice-3 — assigned id S279 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMaskVoice.md:63 NEW-ScoutMaskVoice-3 — seat kind 'web (unpublished conference draft)' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMexicaMosaic.md:22 NEW-ScoutMexicaMosaic-1 — assigned id S280 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMexicaMosaic.md:22 NEW-ScoutMexicaMosaic-1 — seat kind 'record.' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMexicaMosaic.md:76 NEW-ScoutMexicaMosaic-2 — assigned id S281 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMexicaMosaic.md:76 NEW-ScoutMexicaMosaic-2 — seat kind 'web.' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMummering.md:7 NEW-ScoutMummering-1 — assigned id S282 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMummering.md:37 NEW-ScoutMummering-2 — assigned id S283 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMummering.md:37 NEW-ScoutMummering-2 — seat kind 'record (official designation page)' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutMummering.md:37 NEW-ScoutMummering-2 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutNoh.md:14 NEW-ScoutNoh-1 — assigned id S284 already exists in the registry; the row would duplicate it
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutNoh.md:14 NEW-ScoutNoh-1 — seat kind 'web' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutNoh.md:35 NEW-ScoutNoh-2 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutNoh.md:55 NEW-ScoutNoh-3 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutNoh.md:74 NEW-ScoutNoh-4 — seat kind 'web' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutNoh.md:94 NEW-ScoutNoh-5 — seat kind 'web' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutNoh.md:115 NEW-ScoutNoh-6 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutNoh.md:115 NEW-ScoutNoh-6 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutNuo.md:83 NEW-ScoutNuo-4 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutNuo.md:104 NEW-ScoutNuo-5 — seat kind 'web' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutNuo.md:125 NEW-ScoutNuo-6 — seat kind 'web' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutNuo.md:125 NEW-ScoutNuo-6 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutParachicos.md:13 NEW-ScoutParachicos-1 — seat kind 'web (UNESCO element record)' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutParachicos.md:13 NEW-ScoutParachicos-1 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutParachicos.md:38 NEW-ScoutParachicos-2 — seat kind 'record (national intangible-heritage inventory entry)' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutParachicos.md:38 NEW-ScoutParachicos-2 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutParachicos.md:62 NEW-ScoutParachicos-3 — seat kind 'web (UNESCO element record)' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutParachicos.md:62 NEW-ScoutParachicos-3 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutParachicos.md:87 NEW-ScoutParachicos-4 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutParachicos.md:111 NEW-ScoutParachicos-5 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutPersonaProsopon.md:82 NEW-ScoutPersonaProsopon-4 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutSowei.md:51 NEW-ScoutSowei-2 — seat kind "record (holding museum's own catalogue record)" filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutSowei.md:93 NEW-ScoutSowei-4 — seat kind 'web (project glossary)' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutSriLankaKolam.md:56 NEW-ScoutSriLankaKolam-3 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutSriLankaKolam.md:77 NEW-ScoutSriLankaKolam-4 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutTalchum.md:32 NEW-ScoutTalchum-1 — seat kind 'web' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutTalchum.md:53 NEW-ScoutTalchum-2 — seat kind 'web' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutTalchum.md:72 NEW-ScoutTalchum-3 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutTalchum.md:93 NEW-ScoutTalchum-4 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutTalchum.md:114 NEW-ScoutTalchum-5 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutTalchum.md:134 NEW-ScoutTalchum-6 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutTalchum.md:154 NEW-ScoutTalchum-7 — seat kind 'web' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutTalchum.md:154 NEW-ScoutTalchum-7 — draft sentence carries no (NEW-..., locator) marker
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutVenice.md:72 NEW-ScoutVenice-2 — seat kind "record (holding museum's own collection record)." filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutYupik.md:40 NEW-ScoutYupik-2 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE_WARN /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-54/build-a2/ScoutYupik.md:62 NEW-ScoutYupik-3 — seat kind 'record' filed as registry kind 'docs'
INTEGRATE: files=40 blocks=93 groups=91 ids=S239..S329 rows=91 warnings=133
INTEGRATE_OK rows.md map.tsv gate.md sentences.md -> /fast/scratch/hyaku/kotodama-r55/ExecIntegrateRows55/out-round54-final
EXIT=0
```

Exit code: 0.

`CriticCalibrationMasks.md` was excluded because its diagnostic blocks have no teaches sentence; the tool correctly rejects such inputs rather than emit empty or truncated Grounds. The other legacy reports include a few single-quoted source passages, which the parser now accepts. Warning lines in the transcript are historical registry-ID collisions, kind mappings, merge notices, legacy marker omissions, and a carried access-marker note; these are warnings only and no lane file was changed.

## Gate diff and exact retained evidence

Comparison command:

```sh
python3 -B /fast/scratch/hyaku/kotodama-r55/ExecIntegrateRows55/compare-round54-gates.py /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/lessons/round-54.md /fast/scratch/hyaku/kotodama-r55/ExecIntegrateRows55/out-round54-final/gate.md
```

Output: `legacy_rows=46 rebuilt_rows=91 url_matches=46 missing=0 unchanged_grounds=0`; `quote_span_failures=0 locator_echoes=0`; exit 0. The complete row mapping is:

```text
S239 -> S275   S240 -> S276   S241 -> S305   S242 -> S308   S243 -> S290   S244 -> S250
S245 -> S314   S246 -> S268   S247 -> S291   S248 -> S295   S249 -> S292   S250 -> S316
S251 -> S294   S252 -> S317   S253 -> S251   S254 -> S267   S255 -> S309   S256 -> S293
S257 -> S315   S258 -> S259   S259 -> S269   S260 -> S311   S261 -> S312   S262 -> S310
S263 -> S262   S264 -> S261   S265 -> S241   S266 -> S240   S267 -> S278   S268 -> S277
S269 -> S279   S270 -> S258   S271 -> S260   S272 -> S306   S273 -> S252   S274 -> S253
S275 -> S270   S276 -> S271   S277 -> S272   S278 -> S273   S279 -> S301   S280 -> S302
S281 -> S303   S282 -> S304   S283 -> S325   S284 -> S326
```

All 46 mappings are tagged `FULL_TEACHES`; none retained the old grounds verbatim. Representative routed defects are fixed: old S239 repeated `Transformations, ¶1` inside the quote, while the rebuilt row has locator `“Power and representation”, ¶1` and only the source passage; old S240 likewise repeated its locator, while rebuilt S276 emits one source span. The comparator found zero locator echoes across all 91 rebuilt rows.

Quote-gate command (the generated file already starts with `## Gate`):

```sh
python3 -B tools/check-gate-quotes.py /fast/scratch/hyaku/kotodama-r55/ExecIntegrateRows55/out-round54-final/gate.md
```

Output: `GATE_QUOTES: 0 findings`; exit code 0.

## Superseded diagnostic runs

- Initial all-report integration, before missing-teaches became a hard error: `files=41 blocks=108 groups=105 ids=S239..S343 rows=105 warnings=157`, then `INTEGRATE_OK`; exit 0 by the tool’s success return path. This run included the integrator report present in that directory and was not used for final evidence.
- Strict-teaches run before adding support for legacy single-quoted quotes: exit 1 with two `ScoutParachicos.md:111` errors (`§EL CARNAVAL` and `§DIOSES DEL BIEN Y DEL MAL...` quote lines); this led to the single-quote parser support.
- First URL diff attempt parsed only 40/46 URLs and missed S244, S246, S254, S261, S274, S283 because report URL fields include secondary-link annotations. The comparator was corrected to compare the leading primary URL; the final comparison above matches 46/46.
- First one-span structural comparison found one exception, rebuilt S268, because its URL annotation itself contains straight quotes. `_gate_text(url)` now encodes those marks; the final structural comparison reports zero exceptions.
- The quote checker also returned zero findings on the first generated Gate before the URL annotation correction; the final run above is the retained evidence for the corrected output.

## Risks and unrun work

- The round-54 demo is a historical integration simulation, not a new registry land: `--start 239` intentionally collides with existing IDs and emits warnings. Output stayed in scratch.
- `CriticCalibrationMasks.md` is excluded only from the historical demo because those blocks lack required teaches sentences. Round-55 source blocks must provide `teaches:`; missing text is a hard error.
- Builds, linters, and the round-55 acceptance scripts were not run; this seat owns only the scoped integrator work and the requested quote checker.
- No tool was installed or upgraded; Python standard library only.

## Final integrator source

```python
#!/usr/bin/env python3
"""integrate-rows.py — kotodama round-55 claim C registry integrator.

Turns seat reports' `### NEW-<Seat>-<n>` blocks into four artefacts:

  rows.md       one corpus/SOURCES.md registry row per block, in the 11-column
                shape of the live registry (column order is read from its header)
  map.tsv       draft id -> S-id
  gate.md       one round-lesson `## Gate` line per row, grounded by the full
                `teaches` sentence and carrying one quoted source span
  sentences.md  every block's draft sentences with draft ids replaced by S-ids

In `--rewrite` mode, draft ids inside a given file are rewritten in place using
map.tsv.

Usage:
  python3 -B integrate-rows.py --reports <dir> --start 285 \
      --sources /home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/SOURCES.md \
      --out <dir>

  python3 -B integrate-rows.py --rewrite <file> --map <map.tsv> [--dry-run]

Block shape: a `### NEW-<Seat>-<n>` heading followed by `citation:`, `url:`,
`route:`, `kind:`, `tier:`, `scope:`, `quotes:` (bulleted, each `<locator>:
"<quote>"`), `teaches:`, `draft sentences:` (3-6 sentences, each ending
`(NEW-<Seat>-<n>, <locator>)`) and `unopened:`. Keys may be list items, values
may run over multiple lines, and quoted passages may contain straight quotes.

Hard errors (exit 1, nothing written): a block with no url, quotes or teaches
sentence; an unparseable quote or no quote at most 25 words; a duplicate url
unless `--merge-duplicates` is set; or a duplicate draft id. Registry id
collisions are warnings. Stdlib only. Exit codes: 0 success, 1 hard error, 2
bad invocation or unreadable input.
"""

import argparse
import os
import re
import sys

# --- block and field grammar -------------------------------------------------

BLOCK_RE = re.compile(r"^#{2,4}\s+(NEW-(?P<seat>[A-Za-z0-9_]+(?:-[A-Za-z0-9_]+)*)-(?P<num>\d+))\b")
KEY_RE = re.compile(r"^(?P<key>[A-Za-z][A-Za-z0-9 _-]{0,40}?)\s*:\s*(?!/)(?P<val>.*)$")
BULLET_RE = re.compile(r"^\s*(?:[-*+]|\d+[.)])\s+")
MARKER_RE = re.compile(r"\((?P<did>NEW-[A-Za-z0-9_]+(?:-[A-Za-z0-9_]+)*-\d+)\s*,\s*(?P<loc>[^)]*)\)")

KEY_ALIASES = {
    "citation": "citation",
    "source": "citation",
    "url": "url",
    "link": "url",
    "route": "route",
    "access": "route",
    "kind": "kind",
    "type": "kind",
    "tier": "tier",
    "scope": "scope",
    "quotes": "quotes",
    "quote": "quotes",
    "teaches": "teaches",
    "teach": "teaches",
    "lesson": "teaches",
    "draft sentences": "draft_sentences",
    "draft sentence": "draft_sentences",
    "sentences": "draft_sentences",
    "unopened": "unopened",
    "not opened": "unopened",
}

# registry column -> the value this tool computes for it
COLUMNS = ["id", "source", "kind", "tier", "scope", "anchor", "teaches",
           "status", "opened", "recheck", "used-by"]

# The registry's kind enum is spec, docs, paper, code, tool, dataset, talk,
# book, community, own-work. The wave vocabulary also uses `web` and `record`.
KIND_MAP = {
    "paper": "paper",
    "book": "book",
    "dataset": "dataset",
    "spec": "spec",
    "docs": "docs",
    "code": "code",
    "tool": "tool",
    "talk": "talk",
    "community": "community",
    "own-work": "own-work",
    "web": "docs",
    "record": "docs",
}

# A seat kind that names a community-authored source.
COMMUNITY_RE = re.compile(
    r"\bcommunity\b|\btribal\b|\bfirst nations\b|\bband council\b",
    re.IGNORECASE,
)

# QUALITY criterion 10 markers, copied from tools/check-source-access.py.
BYPASS_RE = re.compile(
    r"""\bheadless\b|\bbypass(?:ed|ing)?\b|\bsolved\s+(?:a\s+|the\s+)?(?:bot\s+)?(?:captcha|challenge)\b
| \b(?:undetected-chromedriver|flaresolverr|cloudscraper|curl-impersonate|ez-?proxy)\b
| \b(?:open|fetch|load|render|retriev|scrap|access|download|captur|driv|automat)\w*\s+(?:\S+\s+){0,2}?(?:with|via|through|using|by|in)\s+(?:a\s+|an\s+|the\s+)?(?:playwright|puppeteer|selenium|webdriver|chromedriver)\b
| \b(?:playwright|puppeteer|selenium)(?:[\s-]+webdriver)?[\s-]+(?:browser|session|script|chrom\w*|firefox|webkit)\b
| (?<!\bnot )(?<!\bno )(?<!\bnever )\b(?:bypass(?:ed|es|ing)?|by-pass(?:ed|es|ing)?|circumvent(?:ed|s|ing)|evad(?:ed|es|ing)|defeat(?:ed|s|ing)?|solv(?:ed|es|ing)?|pass(?:ed|es|ing)?|clear(?:ed|s|ing)?|g[eo]t(?:ting)?\s+(?:past|around|round|through))\s+(?:\S+\s+){0,3}?(?:pay-?walls?|log-?ins?|sign-?ins?|(?:re|h)?captchas?|turnstile|geo[\s-]?block(?:s|ed|ing)?|geo[\s-]?fenc(?:e|es|ing)?|(?:bot|js|javascript|cloudflare|waf|anti-?bot|browser|security)[\s-](?:challenges?|checks?|blocks?|walls?|tests?)|challenge\s+pages?|access\s+controls?)\b
| \b(?:pay-?wall|log-?in|(?:re|h)?captcha|geo[\s-]?block)s?\s*(?:was\s+|were\s+)?(?:bypass|by-pass|circumvent|evad|defeat|solv)\w*
| \bvpns?\b
| \blogged-in\b|\b(?:signed|logged)\s+in\s+(?:as|with|via|using|through)\b
| \b(?:subscriber|subscription|paid|member)\s+(?:account|login|credentials|session|cookie)s?\b|\b(?:institutional|personal)\s+(?:login|credentials|session|cookie)s?\b|\bsession\s+cookies?\b|\bcookies?\s+(?:from|of|my|the)\b
| \bspoof(?:ed|ing)?\s+(?:a\s+|the\s+)?(?:browser\s+)?(?:user-?agent|ip|location|referer|headers?)\b""",
    re.IGNORECASE | re.VERBOSE,
)


# --- small helpers ------------------------------------------------------------

def norm_key(key):
    key = re.sub(r"\s+", " ", key.strip().lower())
    return KEY_ALIASES.get(key)


def cell(text):
    """One table cell: single line, with literal table pipes encoded."""
    text = re.sub(r"\s+", " ", (text or "").strip())
    return text.replace("|", "&#124;")


def words(text):
    return len((text or "").split())


def strip_bullet(line):
    return BULLET_RE.sub("", line).strip()


def read_text(path):
    with open(path, encoding="utf-8-sig") as handle:
        return handle.read()


def report_files(directory, excludes):
    """Every .md file directly under a directory, in name order."""
    names = []
    for name in sorted(os.listdir(directory)):
        if not name.endswith(".md"):
            continue
        path = os.path.join(directory, name)
        if any(re.search(pat, path) for pat in excludes):
            continue
        names.append(path)
    return names


def _locator_key(text):
    """Normalize punctuation only for detecting a repeated locator echo."""
    return re.findall(r"[\w]+", text.casefold(), re.UNICODE)


def split_quote_line(line):
    """Parse a quoted source passage and discard a repeated locator echo.

    Reports usually delimit passages with double quotes, but some older reports
    use single quotes around passages that contain double-quoted words. The
    locator may itself carry quotes, and the passage may be followed by a
    bracketed or parenthesised note. A round-54 defect duplicated the locator
    inside the quoted passage; when the first double-quoted text repeats the
    locator before another `: "`, keep only the actual passage.
    """
    line = strip_bullet(line)

    single_openers = [i for i in range(2, len(line))
                      if line[i] == "'" and line[i - 2:i] == ": "]
    if single_openers:
        opening = single_openers[0]
        locator = line[:opening].rstrip()
        if locator.endswith(":"):
            locator = locator[:-1].rstrip()
        start = opening + 1
        stripped = line.rstrip()
        end = len(stripped) - 1
        if not (stripped.endswith("'") and end > start):
            end = None
            for index in range(start, len(line)):
                if line[index] == "'" and re.match(r"^\s*(\(|\[|$)", line[index + 1:]):
                    end = index
                    break
            if end is None:
                return None
        quote = line[start:end]
        if not quote.strip():
            return None
        return locator, quote, line[end + 1:].strip(), False

    if '"' not in line:
        return None
    openers = [i for i in range(2, len(line)) if line[i] == '"' and line[i - 2:i] == ": "]
    if not openers:
        first = line.find('"')
        if first < 0:
            return None
        openers = [first]

    first_opening = openers[0]
    locator = line[:first_opening].rstrip()
    if locator.endswith(":"):
        locator = locator[:-1].rstrip()

    opening = first_opening
    locator_key = _locator_key(locator)
    for next_opening in openers[1:]:
        echoed = line[first_opening + 1:next_opening]
        if locator_key and _locator_key(echoed) == locator_key:
            opening = next_opening
            break

    start = opening + 1
    stripped = line.rstrip()
    end = len(stripped) - 1
    if not (stripped.endswith('"') and end > start):
        end = None
        for index in range(start, len(line)):
            if line[index] == '"' and re.match(r"^\s*(\(|\[|$)", line[index + 1:]):
                end = index
                break
        if end is None:
            return None
    quote = line[start:end]
    if not quote.strip() or quote.count('"') % 2:
        return None
    return locator, quote, line[end + 1:].strip(), len(openers) > 1


# --- parsing ------------------------------------------------------------------

class Block(object):
    def __init__(self, draft_id, seat, num, path, line):
        self.draft_id = draft_id
        self.seat = seat
        self.num = num
        self.path = path
        self.line = line
        self.fields = {}

    def get(self, key):
        return self.fields.get(key, [])

    def text(self, key):
        return " ".join(x.strip() for x in self.get(key)).strip()

    def has(self, key):
        return key in self.fields


def parse_report(path):
    """Return the list of `### NEW-<Seat>-<n>` blocks in one report file."""
    blocks = []
    current = None
    field_key = None
    for number, raw in enumerate(read_text(path).splitlines(), 1):
        heading = BLOCK_RE.match(raw)
        if heading:
            current = Block("NEW-%s-%s" % (heading.group("seat"), heading.group("num")),
                            heading.group("seat"), int(heading.group("num")), path, number)
            blocks.append(current)
            field_key = None
            continue
        if current is None:
            continue
        if raw.lstrip().startswith("#"):
            current = None
            field_key = None
            continue
        plain = strip_bullet(raw)
        match = KEY_RE.match(plain)
        if match:
            key = norm_key(match.group("key"))
            if key:
                field_key = key
                current.fields.setdefault(key, [])
                value = match.group("val").strip()
                if value:
                    current.fields[key].append(value)
                continue
        if field_key is not None:
            current.fields[field_key].append(plain)
    return blocks


def block_quotes(block, problems):
    """Bulleted quotes of a block as (locator, quote, tail, multiple) records."""
    pairs = []
    for line in block.get("quotes"):
        plain = strip_bullet(line)
        if not plain:
            continue
        parsed = split_quote_line(line)
        if parsed is None:
            problems.append((block, "quote line carries no double-quoted passage: %r" % plain[:90]))
            continue
        pairs.append(parsed)
    return pairs


def block_sentences(block):
    """Draft sentences of a block: one unit per bullet, continuation lines folded in."""
    units = []
    buffer = []
    for line in block.get("draft_sentences"):
        plain = strip_bullet(line)
        if not plain:
            continue
        buffer.append(plain)
        if MARKER_RE.search(plain):
            units.append(" ".join(buffer))
            buffer = []
    if buffer:
        units.append(" ".join(buffer))
    return units


# --- registry reading ---------------------------------------------------------

def read_registry(path):
    """Return (column_order, existing_ids) from a corpus/SOURCES.md."""
    columns, ids = [], set()
    for line in read_text(path).splitlines():
        if not columns and re.match(r"^\|\s*id\s*\|", line):
            columns = [c.strip() for c in line.strip().strip("|").split("|")]
            continue
        match = re.match(r"^\|\s*(S\d{3,})\s*\|", line)
        if match:
            ids.add(match.group(1))
    if not columns:
        raise ValueError("no registry header found in %s" % path)
    return columns, ids


# --- integration --------------------------------------------------------------

def build_row(block, sid, args, columns):
    """Return (cells, warnings) for one registry row."""
    warnings = []
    url = block.text("url").strip()
    citation = block.text("citation").strip()
    route = block.text("route").strip()
    kind_raw = block.text("kind").strip()
    tier_raw = block.text("tier").strip()
    scope = block.text("scope").strip()
    teaches = block.text("teaches").strip()

    tier_match = re.match(r"^([ABC])\b", tier_raw)
    if tier_match:
        tier = tier_match.group(1)
    else:
        tier = ""
        warnings.append("tier cell does not start with A, B or C: %r" % tier_raw[:70])

    kind_token = re.split(r"[\s(.]", kind_raw.lower(), maxsplit=1)[0].strip()
    kind = KIND_MAP.get(kind_token, "")
    if not kind:
        kind = "docs"
        warnings.append("seat kind %r has no registry enum value; filed as docs" % kind_raw[:60])
    elif kind_token != kind:
        warnings.append("seat kind %r filed as registry kind %r" % (kind_raw[:60], kind))

    # Community-authored sources are never tier A in the registry census.
    if args.community_kind and COMMUNITY_RE.search(kind_raw):
        if kind != "community":
            warnings.append("seat kind %r filed as registry kind community (a community's own "
                            "statement)" % kind_raw[:60])
        kind = "community"
        if tier == "A":
            tier = "B"
            warnings.append("tier A downgraded to B: the registry census treats a community row as "
                            "never tier A")

    source = citation + " — " + url if citation else "—"
    if route:
        source += " (%s)" % route
    if not citation:
        warnings.append("no citation field; the source cell needs author, year, title and venue")

    quotes = block_quotes(block, [])
    anchor_parts = []
    for locator, quote, tail, multiple in quotes:
        piece = ('%s: "%s"' % (locator, quote)) if locator else ('"%s"' % quote)
        if tail:
            piece += " " + tail
        anchor_parts.append(piece)
    anchor = "; ".join(anchor_parts)

    scope_cell = scope
    if tier_raw:
        scope_cell = (scope_cell + " " if scope_cell else "") + "(tier note: %s)" % tier_raw
    if not scope_cell:
        warnings.append("no scope field; the scope cell needs the claim the tier applies to")

    bypass = BYPASS_RE.search(" ".join((source, anchor, scope_cell, teaches)))
    if bypass:
        warnings.append("the row's cells carry the access-control marker %r; "
                        "tools/check-source-access.py flags such a row as unopened, so reword the "
                        "cell before the row is filed (QUALITY criterion 10)"
                        % bypass.group(0))

    values = {
        "id": sid,
        "source": source,
        "kind": kind,
        "tier": tier,
        "scope": scope_cell,
        "anchor": anchor,
        "teaches": teaches or "—",
        "status": args.status,
        "opened": args.opened,
        "recheck": args.recheck,
        "used-by": args.used_by,
    }
    return [cell(values.get(name, "")) for name in columns], warnings


def _gate_text(text):
    """Encode nested quotation marks so a Gate row has one quoted span."""
    return ((text or "").replace("&", "&amp;")
            .replace('"', "&quot;")
            .replace("“", "&#8220;")
            .replace("”", "&#8221;"))


def gate_line(sid, url, locator, quote, teaches, seat, accessed):
    """One Gate line with one source quote and the full block teaches sentence."""
    quote = quote.strip()
    ground = teaches.strip()
    if ground and ground[-1] not in ".!?":
        ground += "."
    where = ('%s: "%s"' % (_gate_text(locator), _gate_text(quote))) if locator else ('"%s"' % _gate_text(quote))
    return '- %s — %s — accessed %s — %s. Grounds: %s Seat: %s.' % (
        sid, _gate_text(url), accessed, where, _gate_text(ground), seat)


def integrate(args):
    columns, existing = read_registry(args.sources)
    if columns != COLUMNS:
        raise ValueError("registry header %r does not match the expected columns %r"
                         % (columns, COLUMNS))

    problems, warnings = [], []
    blocks = []
    files = report_files(args.reports, args.exclude)
    for path in files:
        blocks.extend(parse_report(path))

    seen_draft = {}
    for block in blocks:
        if block.draft_id in seen_draft:
            problems.append((block, "draft id %s already used in %s:%d"
                             % (block.draft_id, seen_draft[block.draft_id][0],
                                seen_draft[block.draft_id][1])))
        else:
            seen_draft[block.draft_id] = (block.path, block.line)
        if not block.text("teaches"):
            problems.append((block, "block has no teaches sentence"))

    # One row per URL only when explicitly requested; by default duplicate URLs
    # are a hard error, so every block has one unambiguous registry row.
    groups = []
    group_of = {}
    url_seen = {}
    for block in blocks:
        url = block.text("url").strip()
        if not url:
            problems.append((block, "block has no url"))
            continue
        key = url.lower().rstrip("/")
        if key in url_seen:
            other = url_seen[key]
            if args.merge_duplicates:
                if args.merge_keep == "last":
                    other[1].append(other[0])
                    other[0] = block
                    groups[groups.index(other)] = other
                else:
                    other[1].append(block)
                group_of[block.draft_id] = other
                warnings.append((block, "merged into the row of %s (same url %s)"
                                 % (other[0].draft_id, url)))
                continue
            problems.append((block, "duplicate url %s — also in %s:%d (%s)"
                             % (url, other[0].path, other[0].line, other[0].draft_id)))
            problems.append((other[0], "duplicate url %s — also in %s:%d (%s)"
                             % (url, block.path, block.line, block.draft_id)))
        else:
            group = [block, []]
            groups.append(group)
            group_of[block.draft_id] = group
            url_seen[key] = group

    for block in blocks:
        quotes = block.get("quotes")
        if not quotes or not [x for x in quotes if x.strip()]:
            problems.append((block, "block has no quotes"))
            continue
        quote_problems = []
        parsed_quotes = block_quotes(block, quote_problems)
        problems.extend(quote_problems)
        if not parsed_quotes:
            problems.append((block, "block has no parseable quote"))
            continue
        usable_quote = False
        for locator, quote, tail, multiple in parsed_quotes:
            count = words(quote)
            if count <= args.max_quote_words:
                usable_quote = True
            else:
                message = ("quote of %d words exceeds the %d-word limit: %r"
                           % (count, args.max_quote_words, quote[:90]))
                if args.allow_long_quotes:
                    warnings.append((block, message))
                else:
                    problems.append((block, message))
        if not usable_quote:
            problems.append((block, "block has no quote of at most %d words" % args.max_quote_words))
    if problems:
        for block, message in problems:
            print("INTEGRATE_ERROR %s:%d %s — %s" % (block.path, block.line, block.draft_id, message),
                  file=sys.stderr)
        print("INTEGRATE: %d hard error(s); no output written" % len(problems), file=sys.stderr)
        return 1

    os.makedirs(args.out, exist_ok=True)

    rows, gate, mapping, sentence_sections = [], [], [], []
    for offset, group in enumerate(groups):
        block, members = group
        sid = "S%03d" % (args.start + offset)
        if sid in existing:
            warnings.append((block, "assigned id %s already exists in the registry; the row would "
                                    "duplicate it" % sid))
        cells, row_warnings = build_row(block, sid, args, columns)
        rows.append("| " + " | ".join(cells) + " |")
        for message in row_warnings:
            warnings.append((block, message))
        for member in [block] + members:
            mapping.append((member.draft_id, sid))

        url = block.text("url").strip()
        chosen = None
        for locator, quote, tail, multiple in block_quotes(block, []):
            if words(quote) <= args.max_quote_words:
                chosen = (locator, quote)
                break
        if chosen is None:
            warnings.append((block, "no quote of at most %d words; the Gate line is flagged"
                             % args.max_quote_words))
            gate.append("- %s — %s — accessed %s — NO USABLE QUOTE (every quote is over %d words). "
                        "Grounds: %s. Seat: %s." % (sid, url, args.opened, args.max_quote_words,
                                                   block.text("teaches"), block.seat))
        else:
            gate.append(gate_line(sid, url, chosen[0], chosen[1], block.text("teaches"),
                                  block.seat, args.opened))

        for member in [block] + members:
            units = block_sentences(member)
            for unit in units:
                if not MARKER_RE.search(unit):
                    warnings.append((member, "draft sentence carries no (NEW-..., locator) marker"))
            sentence_sections.append((sid, member.draft_id, units))

    id_map = dict(mapping)

    def rewrite_ids(text):
        for did in sorted(id_map, key=len, reverse=True):
            text = re.sub(r"(?<![A-Za-z0-9_.-])%s(?![A-Za-z0-9_-])" % re.escape(did),
                          id_map[did], text)
        return text

    with open(os.path.join(args.out, "rows.md"), "w", encoding="utf-8") as handle:
        handle.write("\n".join(rows) + ("\n" if rows else ""))
    with open(os.path.join(args.out, "map.tsv"), "w", encoding="utf-8") as handle:
        handle.write("draft_id\ts_id\n")
        for did, sid in mapping:
            handle.write("%s\t%s\n" % (did, sid))
    with open(os.path.join(args.out, "gate.md"), "w", encoding="utf-8") as handle:
        handle.write("## Gate\n\n")
        handle.write("\n".join(gate) + ("\n" if gate else ""))
    sentence_lines = []
    for sid, draft_id, units in sentence_sections:
        sentence_lines.append("## %s — %s" % (sid, draft_id))
        sentence_lines.append("")
        for unit in units:
            sentence_lines.append(rewrite_ids(unit))
        sentence_lines.append("")
    with open(os.path.join(args.out, "sentences.md"), "w", encoding="utf-8") as handle:
        handle.write("\n".join(sentence_lines).rstrip() + "\n")

    for block, message in warnings:
        print("INTEGRATE_WARN %s:%d %s — %s" % (block.path, block.line, block.draft_id, message),
              file=sys.stderr)
    print("INTEGRATE: files=%d blocks=%d groups=%d ids=%s..%s rows=%d warnings=%d"
          % (len(files), len(blocks), len(groups), "S%03d" % args.start,
             "S%03d" % (args.start + len(groups) - 1) if groups else "—", len(rows), len(warnings)))
    print("INTEGRATE_OK rows.md map.tsv gate.md sentences.md -> %s" % args.out)
    return 0


def rewrite(args):
    if not args.map:
        raise ValueError("--rewrite needs --map (or an --out directory holding map.tsv)")
    mapping = {}
    with open(args.map, encoding="utf-8") as handle:
        for number, line in enumerate(handle, 1):
            line = line.rstrip("\n")
            if not line.strip():
                continue
            parts = line.split("\t")
            if number == 1 and parts[0].strip() == "draft_id":
                continue
            if len(parts) != 2:
                raise ValueError("map.tsv line %d is not 'draft_id\\ts_id': %r" % (number, line))
            mapping[parts[0].strip()] = parts[1].strip()
    if not mapping:
        raise ValueError("no ids in %s" % args.map)

    original = read_text(args.rewrite)
    text = original
    counts = {}
    for did in sorted(mapping, key=len, reverse=True):
        pattern = re.compile(r"(?<![A-Za-z0-9_.-])%s(?![A-Za-z0-9_-])" % re.escape(did))
        text, count = pattern.subn(mapping[did], text)
        if count:
            counts[did] = count
    if not args.dry_run and text != original:
        with open(args.rewrite, "w", encoding="utf-8") as handle:
            handle.write(text)
    print("REWRITE %s: %d replacement(s) of %d draft id(s)%s"
          % (args.rewrite, sum(counts.values()), len(counts), " (dry run)" if args.dry_run else ""))
    for did in sorted(counts):
        print("REWRITE_ID %s -> %s x%d" % (did, mapping[did], counts[did]))
    return 0


def main():
    parser = argparse.ArgumentParser(add_help=True)
    parser.add_argument("--reports", help="directory of seat reports")
    parser.add_argument("--start", type=int, default=285, help="first S-id to assign")
    parser.add_argument("--sources", help="path to corpus/SOURCES.md")
    parser.add_argument("--out", help="directory for rows.md, map.tsv, gate.md, sentences.md")
    parser.add_argument("--rewrite", help="file whose draft ids are replaced in place")
    parser.add_argument("--map", help="map.tsv used by --rewrite")
    parser.add_argument("--dry-run", action="store_true", help="--rewrite without writing")
    parser.add_argument("--used-by", default="corpus/knowledge/myth-symbol/monsters-hybrid-beings.md",
                        help="used-by cell of every row")
    parser.add_argument("--status", default="mined", help="status cell of every row")
    parser.add_argument("--opened", default="2026-10-22", help="opened date in Gate lines and rows")
    parser.add_argument("--recheck", default="365d", help="recheck cell of every row")
    parser.add_argument("--max-quote-words", type=int, default=25,
                        help="word limit for a Gate quote; a longer quote is a hard error")
    parser.add_argument("--allow-long-quotes", action="store_true",
                        help="report a quote over the word limit as a warning instead of a hard "
                             "error (the Gate line still picks a quote within the limit)")
    parser.add_argument("--exclude", action="append", default=[],
                        help="regex; report files whose path matches are skipped")
    parser.add_argument("--merge-duplicates", action="store_true",
                        help="one registry row per distinct url: blocks that opened the same url "
                             "share the first seat's row and the same S-id (default: a duplicate "
                             "url is a hard error)")
    parser.add_argument("--no-community-kind", dest="community_kind", action="store_false",
                        help="do not file a community-authored source as kind community")
    parser.add_argument("--merge-keep", choices=("first", "last"), default="first",
                        help="with --merge-duplicates, which block's cells the shared row keeps "
                             "(default: first in report-file order)")
    parser.set_defaults(community_kind=True)
    args = parser.parse_args()

    try:
        if args.rewrite:
            if not args.map and args.out:
                candidate = os.path.join(args.out, "map.tsv")
                if os.path.isfile(candidate):
                    args.map = candidate
            return rewrite(args)
        if not args.reports or not args.sources or not args.out:
            parser.error("--reports, --sources and --out are required")
        return integrate(args)
    except (OSError, ValueError, UnicodeDecodeError) as error:
        print("INTEGRATE_INPUT_ERROR %s" % error, file=sys.stderr)
        return 2


if __name__ == "__main__":
    sys.exit(main())
```

## Comparison fixture source

```python
#!/usr/bin/env python3
"""Compare legacy round-54 Gate grounds with the rebuilt Gate by source URL."""

import html
import re
import sys


def rows(path, limit=None):
    with open(path, encoding="utf-8") as handle:
        lines = handle.read().splitlines()
    if limit is not None:
        lines = lines[limit[0] - 1:limit[1]]
    found = {}
    for line in lines:
        match = re.match(r"^-\s+(S\d+)\s+—\s+(.*?)\s+— accessed \S+\s+—\s+", line)
        if not match:
            continue
        url_match = re.match(r"https?://\S+", match.group(2))
        if not url_match:
            raise ValueError("Gate row has no leading HTTP URL: %s" % match.group(1))
        url = html.unescape(url_match.group(0))
        if " Grounds: " not in line or " Seat: " not in line:
            raise ValueError("Gate row has no Grounds/Seat fields: %s" % match.group(1))
        ground = line.split(" Grounds: ", 1)[1].rsplit(" Seat: ", 1)[0]
        found[url.lower().rstrip("/")] = (match.group(1), ground)
    return found


def main():
    old = rows(sys.argv[1], (23, 68))
    new = rows(sys.argv[2])
    shape_failures = []
    locator_echoes = []
    with open(sys.argv[2], encoding="utf-8") as handle:
        rebuilt_lines = handle.read().splitlines()
    for line in rebuilt_lines:
        row = re.match(r"^-\s+(S\d+)\b", line)
        if not row:
            continue
        if line.count('"') != 2 or len(re.findall(r'"[^"\n]*"', line)) != 1:
            shape_failures.append(row.group(1))
        anchor = line.split(" — accessed ", 1)[1].split(" — ", 1)[1].split(" Grounds: ", 1)[0]
        locator, separator, rest = anchor.rpartition(': "')
        if separator:
            quote = rest.rsplit('"', 1)[0]
            loc_words = re.findall(r"\w+", html.unescape(locator).casefold())
            quote_words = re.findall(r"\w+", html.unescape(quote).casefold())
            if loc_words and quote_words[:len(loc_words)] == loc_words:
                locator_echoes.append(row.group(1))
    matches = []
    missing = []
    same = []
    for url, (old_id, old_ground) in old.items():
        current = new.get(url)
        if current is None:
            missing.append(old_id)
            continue
        new_id, new_ground = current
        if new_ground == old_ground:
            same.append(old_id)
        matches.append((old_id, new_id, old_ground, new_ground))
    print("legacy_rows=%d rebuilt_rows=%d url_matches=%d missing=%d unchanged_grounds=%d" %
          (len(old), len(new), len(matches), len(missing), len(same)))
    print("quote_span_failures=%d locator_echoes=%d" %
          (len(shape_failures), len(locator_echoes)))
    print("bad_quote_span_ids=%s" % (", ".join(shape_failures) if shape_failures else "—"))
    print("locator_echo_ids=%s" % (", ".join(locator_echoes) if locator_echoes else "—"))
    print("missing_old_ids=%s" % (", ".join(missing) if missing else "—"))
    for old_id, new_id, old_ground, new_ground in matches:
        print("%s -> %s | old_words=%d new_words=%d | %s" %
              (old_id, new_id, len(old_ground.split()), len(new_ground.split()),
               "UNCHANGED" if old_ground == new_ground else "FULL_TEACHES"))
    return 1 if missing or shape_failures or locator_echoes else 0


if __name__ == "__main__":
    sys.exit(main())
```
