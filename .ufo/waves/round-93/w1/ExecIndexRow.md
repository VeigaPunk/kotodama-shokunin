# ExecIndexRow — corpus index row + count updates for round-93 greeting entry

Stage: `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-93/w1/stage/ExecIndexRow/`
Lane untouched: no write under `corpus/`, `tools/`, `reports/`, no git commands run.

## Files written (stage)

- `README.new.md` — full patched README (1011 lines; base 997).
- `README.diff` — `diff -u` base→patched, 3 hunks, 15 insertions / 1 deletion.

## Index-tool result on the scratch tree

Command: `python3 -B /home/vgpnk/Projects/shokunin/kotodama-shokunin/tools/check-corpus-index.py --root /fast/scratch/hyaku/kotodama-r93/ExecIndexRow/tree` (2026-11-05) → rc 0

Final line: `CORPUS-INDEX: OK files=265 rows=265 findings=0`

Tree: byte-copy of lane `corpus/` + stub entry `corpus/knowledge/linguistics/greeting-leave-taking-formulae.md` + patched `corpus/README.md`; linguistics dir listing counted 38 files (`ls | wc -l` → 38).

## Exact topic-line form the tool requires

Entry file: one `- topic:` line; the index tool (`tools/check-corpus-index.py` TOPIC_RE `^- topic:(.*?)(?=\n- \w)`) normalizes it to the line's stripped text and requires byte-equality with the README row's text after `` ` — ` `` (ROW_RE `^- \`([^`]+\.md)\` — (.*)$`). Stub entry line, exactly:

```
- topic: greeting and leave-taking formulae: the speech acts of greeting and farewell, their politeness and access rituals, their contact-driven shift, and the design procedure for a fictional greeting register
```

README row (single line, inside the `## linguistics/` span), exactly:

```
- `greeting-leave-taking-formulae.md` — greeting and leave-taking formulae: the speech acts of greeting and farewell, their politeness and access rituals, their contact-driven shift, and the design procedure for a fictional greeting register
```

## The four patches

1. Revision note prepended after the title, in the `revision: 2.NN` house style (2.21 stays below it): entry filename, placement between `gesture-co-speech-pointing.md` and `historical-linguistics.md` (filename order), `` `## linguistics/` moved 37 → **38**``, totals and footer moved 264 → **265**. No claims beyond the counts.
2. `## linguistics/ (37)` → `## linguistics/ (38)` (tool check HEADER_DRIFT: declared vs files on disk).
3. New row inserted between the `gesture-co-speech-pointing.md` and `historical-linguistics.md` rows.
4. New dated block appended after the round-92 footer (kept byte-identical, per the repo's append-only footer convention): `Total knowledge entries: 265.` + footer `(total 265 files; directory totals 38/36/43/29/24/95)` dated 2026-11-05, command `` `python3 -B tools/check-corpus-index.py --root .` `` — the tool reads only the LAST totals line and LAST footer.

## Numbers measured

- linguistics 37 → 38 (files on disk in tree: 38).
- knowledge total 264 → 265; footer vector 37/36/43/29/24/95 → 38/36/43/29/24/95.
- Diff: 3 hunks, +15/-1.

## Commands run (rc)

- `mkdir -p` stage + scratch dirs — rc 0
- `cp` lane README → stage — rc 0
- tree build (`cp -a corpus`, stub `printf`, `cp` patched README) — rc 0
- `ls tree/corpus/knowledge/linguistics | wc -l` → 38 — rc 0
- index tool on tree — rc 0
- `diff -u` base vs patched → `README.diff` — rc 1 (differences found; expected)
- scratch removal: `rm -rf /fast/scratch/hyaku/kotodama-r93/ExecIndexRow` — rc 0

No tools installed or upgraded (pacman transactions paused host-wide; nothing needed). No sysctl touched. No blockers.
