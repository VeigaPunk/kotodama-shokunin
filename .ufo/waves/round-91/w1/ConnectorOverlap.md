# Round-91 w1 — ConnectorOverlap report (sibling-overlap scan)

Seat: ConnectorOverlap, kotodama lane, leaf member (no subagents). Read-only seat: production files
untouched; writes limited to stage dir + this report. Date: 2026-11-05. Freeze HEAD `691aebf2`,
base `d39434b3`.

## Inputs read first (per Goal)

- `reports/round-91/claims.json` — frozen; C topic matches the planned sub-topics verbatim; C bounds
  name `linguistic-anthropology.md` §5.3 as adjacent owner and `synthesis/religion-language-co-evolution.md`
  §6; `assimilation` records "kotodama has no considerthese directory".
- `reports/round-91/measure91.py` — frozen counter (read; not executed; execution not in this seat's scope).

## Findings

Full table with per-row path:line evidence and commands: stage copy
`.ufo/waves/round-91/w1/stage/ConnectorOverlap/connector.md`. Summary:

| sub-topic | verdict |
|---|---|
| argot and cant as closed in-group vocabularies | held — `linguistics/linguistic-anthropology.md:115-125` (§5.3 dedicated); also `sociolinguistics-registers.md:84`, `synthesis/religion-language-co-evolution.md:15,:88-90`, `culture-material/trade-economy-lexicon.md:103` |
| anti-languages (Halliday) as social structure maintained through conversation | held — §5.3 `:115-123` + `linguistics/dialect-register-consistency.md:71-77` + `register-lexicon-ceilings.md:182`; the specific conversation-maintenance design test is unowned anywhere |
| backslang and reversal games | partial — backslang only passing (`linguistic-anthropology.md:121`); reversal operations held as ceiling material (`register-lexicon-ceilings.md:180,:183`; `register-strata-attestation.md:390-402`), not as backslang/register design |
| ludling and Pig Latin style word play | partial — `linguistic-anthropology.md:136,:146` (decision-table row + checklist), `register-lexicon-ceilings.md:183`; no dedicated section |
| in-group concealment and identity functions | partial — `dialect-faction-map-workflow.md:121-123`, `sociolinguistics-registers.md:126,:86`, `speech-surrogates-whistled-drummed.md:26,:42`, `civilizations/australia-aboriginal.md:66`; no dedicated section |
| design procedure for a fictional secret register | partial (distributed) — `linguistic-anthropology.md:139-149`, `sociolinguistics-registers.md:135-136`, `register-lexicon-ceilings.md` §3, `dialect-faction-map-workflow.md:123`; no unified owner |

## PROVINCE.md

Read in full. It contains no Core/Frontier/Adjacent headings — sections are Domain / Owns / Refuses /
Adjacent contract. The planned entry falls in **Owns** (the `corpus/knowledge/linguistics` partition is
listed verbatim). No sibling owner is named in PROVINCE.md for this entry; boundary parties named are
lore-shokunin (Adjacent contract, canon/world bible; Refuses), chousa (research method, Refuses),
kotoba, kake, game-dev (Refuses). The frozen claim's in-corpus adjacent owners (§5.3 and
religion-language-co-evolution §6) are exactly where the `held` verdicts land.

## considerthese (expected absent)

```
$ ls -la /home/vgpnk/Projects/shokunin/kotodama-shokunin/considerthese
ls: cannot access '/home/vgpnk/Projects/shokunin/kotodama-shokunin/considerthese': No such file or directory
rc=2
```

Matches frozen `claims.json` assimilation note.

## Material state observation

The planned entry already exists as an **untracked working-tree draft**:
`git status --porcelain` → `?? corpus/knowledge/linguistics/secret-and-ludic-languages.md`;
`wc -c` → 21,472 bytes; `ls corpus/knowledge/linguistics | wc -l` → 36 vs
`git ls-files -- corpus/knowledge/linguistics | wc -l` → 35 tracked; `git ls-files --error-unmatch`
on the entry → rc=1. The "planned, not yet written" premise holds at git level (frozen surface reads
commits, and the freeze/base commits lack the file), but sibling seats scanning the working tree will
see the draft. My overlap table deliberately excludes the draft and judges only the 35 committed
entries. Also untracked: `.ufo/waves/round-91/`, `corpus/lessons/round-91.md`, `reports/round-91/{controls/at-freeze-C-do-nothing.txt,evidence/,quarantine/}`, and `M corpus/README.md`, `M corpus/SOURCES.md` — normal mid-wave landing state, no action from this seat.

## Evidence: commands run and rc

| command | rc | result |
|---|---|---|
| `ls -la …/kotodama-shokunin/considerthese` | 2 | absent, as expected |
| `git status --porcelain \| head -30` (lane repo) | 0 | untracked entry draft + wave dirs; README/SOURCES modified |
| `git log --oneline -2` (lane repo) | 0 | `691aebf2` freeze, `d39434b3` base |
| `git ls-files -- corpus/knowledge/linguistics \| wc -l` | 0 | 35 |
| `ls corpus/knowledge/linguistics \| wc -l` | 0 | 36 (untracked draft inflates by 1) |
| `wc -c corpus/knowledge/linguistics/secret-and-ludic-languages.md` | 0 | 21472 |
| `git ls-files --error-unmatch corpus/knowledge/linguistics/secret-and-ludic-languages.md` | 1 | not tracked |
| grep tool, case-insensitive, over `corpus/knowledge`: `argot`; `\bcant\b`; `backslang\|back-slang\|reversal`; `verlan`; `pig latin\|ludling\|ludic`; `anti-language\|antilanguage\|halliday`; `polari\|parlyaree`; `in-group\|ingroup\|covert\|secret language\|secret register\|conceal` | 0 | hits mapped in the table; not-new claims located, open cells listed |

Grep run via the harness `grep` tool (rg-backed) with `path=/home/vgpnk/Projects/shokunin/kotodama-shokunin/corpus/knowledge`, `case=false`; counts are hit sets, quoted in the stage `connector.md`.

Not measurable here / not in scope: quality of the draft's prose; whether the writer seat's own
overlap notes exist (not required of this seat); measure91.py execution (frozen counter, not a
connector concern). No sources were fetched (none needed: overlap scan is repo-internal). No tool
installs (nothing beyond built-ins required; pacman guard moot). Scratch
`/fast/scratch/hyaku/kotodama-r91/ConnectorOverlap/` created, used for nothing (TMPDIR unset in the
one bash call; no --work tools run), deleted before yield.

## Risks

1. Duplicate-restatement hazard concentrates on `linguistic-anthropology.md` §5.3 (mechanism list +
   catalogue) and second on `register-lexicon-ceilings.md`'s operation-ceiling procedure — both are
   the frozen claim's own named boundaries, so the hazard is already contract-encoded; this seat adds
   only the exact line anchors.
2. The untracked draft inflates naive working-tree counts (35 → 36 files in the partition); any seat
   measuring "entry absent" from the working tree instead of git will misread.
3. Sub-topic verdicts are state reports as of 2026-11-05 at `691aebf2`; they go stale if another seat
   lands edits mid-wave.

## Verification (what Main can re-run)

- `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin status --porcelain` (entry still untracked?)
- the eight greps above against `corpus/knowledge` (case-insensitive) — expect the quoted path:line sets
- `ls /home/vgpnk/Projects/shokunin/kotodama-shokunin/considerthese` — expect rc=2
