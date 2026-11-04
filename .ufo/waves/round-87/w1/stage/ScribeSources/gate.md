# Gate — ScribeSources round-87 w1

## Access and provenance

Access date for all opened bodies: **2026-11-04**. No search engine and no external URL were opened by this seat; no credentials or access-control bypass were used. All reads of production and sibling artifacts were read-only; no git/jj mutation, index change, commit, install, delegation or background job occurred. No tools were installed (RULES.md read first; existing tools sufficient).

- **r86 craft packet (S929 source body).** Path `.ufo/waves/round-86/w1/stage/ExecCraftLedger/craft.json`, opened at immutable revision base `83846a22ee1e9da7aa52ac505ccebf4455169247` via read-only `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin show 83846a22…:.ufo/waves/round-86/w1/stage/ExecCraftLedger/craft.json`. Observed: revision blob sha256 `4f631b60b5ea5d5cf42b2ef394d548ff557e4ccaa52f176d7327fead8f34c982`; worktree copy of the same path hashes identically (91 lines). Receipt copy: `receipts/craft-r86-base83846a22.json`.
- **Reopened knowledge entry.** Path `corpus/knowledge/linguistics/proverbs-riddles-attestation-solutions.md`, opened as actual worktree bytes (101 lines, head through §4 read); sha256 `578c1ae2ab4a39ff9cc270fc70a6bf63ba5e1f30b69b86bcc98bfc45ff95a1f5`, byte-identical to `git show 83846a22…:corpus/knowledge/linguistics/proverbs-riddles-attestation-solutions.md`. Its `source:` line names S924; §3 records the S924–S926 anchors and their retained captures under `reports/round-86/evidence/`. This seat did not reopen the S924–S926 external bodies and opens no new external URL for them; their citations stand on the round-86 record. Receipt copy: `receipts/proverbs-riddles-attestation-solutions-opened-2026-11-04.md`.
- **Rejected candidate (S930 source body).** Path `.ufo/waves/round-87/w1/stage/CriticCounter/constant-pass.py`, opened read-only this round (sibling CriticCounter stage artifact, uncommitted). Observed: 4 lines; sha256 `78b66e106bb4a149849a09d92c02fc0b7dd43316fa66a680a22ec07eef01567d` pinned at open time. Receipt copy: `receipts/constant-pass-opened-2026-11-04.py`.

## Quote locators and word counts

- **S929 anchor quote** — craft packet line 5, `boundary` field, first sentence, exactly: 「All wording, people, documents and historical dates below are newly authored hypothetical exercises, not quotations, source evidence or lore proposals.」 Counted: 20 words (≤25). Packet states `status: NON-CANON` (line 3) and `No source IDs are consumed.` (same field), which is why the scope cell says never historical truth.
- **S930 anchor quote** — constant-pass.py line 2, module docstring content, exactly: 「Counterfeit non-reader: must not satisfy the finite battery.」 Counted: 8 words (≤25). Secondary located observation for the refusal reason: line 4, verbatim `print(json.dumps({'records': 6, 'findings': []}))` — constant output, subject-blind.

## Decisions

- **S929 — ADMIT as own-work A, mined, additive.** Tier A is the registry's own category for "the lane's own re-runnable gate output"; precedents S859/S860/S897 fix the cell conventions (kind `own-work`, revision-pinned anchor, recheck 90d–180d, used-by naming lessons). Scope is the packet's fictional attestation-record interface only; the packet's own boundary sentence refuses historical truth. Nearest dossier: S924 (EB1911 Proverb), S925 (Apperson), S926 (Tupper) — cited as rows, not reopened.
- **S930 — REJECT as C, kept with reason and flip.** A probe whose output is a fixed literal can never fail and never depends on a subject, so it cannot carry evidence for or against any claim; its own docstring declares the intent to be a counterfeit. Flip: output computed from input with demonstrated failure on defective subjects. Recheck 180d per rejected-row precedent (S928).

## Bounded search/path note

Search bound: this seat ran no web or corpus-wide claim search. Path-bound reads only: (1) registry tail of `corpus/SOURCES.md` (lines 875–948 read; table ends line 884; `## Search log` at 924) to fix next unused ids and own-work cell conventions via S859/S860/S897 and the S924–S928 rows; (2) the two reopened bodies above; (3) the constant-pass.py candidate; (4) round-87 dispatch/spec hits for this seat's own bounds. Unresolved, not negative findings: whether sibling seats mutate or commit `constant-pass.py` after open time — identity is pinned by the sha256 above, not by path stability. Wave-level counter history, frozen `reports/round-87/claims.json` and `measure87.py` were not opened, run or modified by this seat; the single wave operability claim is not rescored here.

## Integration boundaries

Append the two fragment rows from `rows-sources.md` only with the Gate retained in `corpus/lessons/round-87.md`. Do not rewrite S924–S928 or any historical row, lesson, report or capture byte; do not edit the frozen counter, claims or measure87.py; no admission outside the lane is claimed — these are author-side drafts, and claim admission stays in QUALITY.md. No production append was made by this seat.

## Receipts

`receipts/craft-r86-base83846a22.json`, `receipts/proverbs-riddles-attestation-solutions-opened-2026-11-04.md`, `receipts/constant-pass-opened-2026-11-04.py` — copied from this seat's scratch before scratch removal; hashes above.
