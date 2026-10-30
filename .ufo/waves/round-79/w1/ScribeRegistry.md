# ScribeRegistry — round-79 W1: tool SKILL registry row fields

Seat: ScribeRegistry (scribe, leaf). Lane `/home/vgpnk/Projects/shokunin/kotodama-shokunin`, base `44f76d456c1b326a71ffdb381590af825cbf11be`.
Stage: `.ufo/waves/round-79/w1/stage/ScribeRegistry/`. Nothing shared was edited; `SKILL.md`, `tools/`, `corpus/` and the claim draft are unchanged.

## Verdict

- **Required fields defined.** A gate/probe registry row needs eight non-empty cells: name, kind, entry command, verdict map, self-test, pinned values, write scope, owner. The rules and the exact checker codes are in `stage/.../draft-registry-rows.md` §1.
- **Checker drafted and self-tested in stage.** `skill-row-check.py`. Selftest `SELFTEST: 9/9`, exit 0. Eight mutants run; seven are killed by the selftest. The unkilled one is a print-the-expected-line stub. That limit is stated in §5.
- **Base registry measured.** At `44f76d45` the first registry table has 60 rows and the D3 table has 2. Probe result: `REGISTRY-ROWS: FAIL rows=62 findings=57`. 25 rows pass, 37 carry findings. Real defects are listed in §3.
- **Candidate rows for O and Ca cannot be finalised yet.** Their entry commands, verdict lines, pinned hashes and write-scope wording depend on bytes that have not landed. Draft shapes are in `draft-registry-rows.md` §4; each cell that depends on lands is marked.
- **Nothing applied to `SKILL.md`.** Repairs to historical rows are proposed only as append-only note rows (N1, N2), following the row-709 precedent. In-place edits to rows are not proposed.

## 1. Scope read

- `/home/vgpnk/.omp/agent/RULES.md`: installs are authorised; no `pacman`.
- `.ufo/waves/round-79/CLAIMS-DRAFT.md`: O and Ca are candidates, not frozen. Ca is rejected pre-freeze unless a self-assessment mismatch is found. Freshness stays paused by L0 round-11. No new numeric axis.
- `.ufo/waves/round-79/w1/spec.json` line 151–153: this seat's work item (fields listed above).
- `SKILL.md` at base: registry table header line 648; body rows 650–709; second table 763–766 (D3, same header). Verdict rows at 686–691 and 658 are the probe's defects.
- `corpus/QUALITY.md` clauses read: 7 (separable claims), 8–9 (declared inputs run before dispatch), 11 (each clause shown able to fail, review-only clauses named), 23 (counter ships selftest receipt; red-before for each fix), 25–26 (freeze constants), 27 (artifact named per reject), 28 (leg authority pinned at freeze). Clause 11 drove the nine-rule selftest coverage; clause 28 drove the pinned-values rule.

## 2. Observed commands and receipts

All stage paths are under `.ufo/waves/round-79/w1/stage/ScribeRegistry/`.

| receipt | command (cwd = scratch `/fast/scratch/hyaku/kotodama-r79/ScribeRegistry`) | result |
|---|---|---|
| `selftest-receipt.txt` | `python3 -B skill-row-check.py --selftest fixtures/` | `SELFTEST: 9/9`, exit 0 |
| `probe-base-rows.txt` | `python3 -B skill-row-check.py --skill SKILL.base.md --root <lane> --rev 44f76d456c1b326a71ffdb381590af825cbf11be` | `REGISTRY-ROWS: FAIL rows=62 findings=57`, exit 1 |
| `base-finding-counts.txt` | row-class tally of the probe | 37 rows with findings; 20 SELFTEST-BARE; 30 PINNED-BARE |
| `probe-draft-notes.txt` | same checker over the draft note rows N1, N2 | both `ROW OK`, exit 0 |
| `mutation-receipt.txt` | eight source mutants plus a control, each run against `fixtures/` | see §5 |
| `counter-selftest-mentions-base.txt` | `git show 44f76d45:<path>` for every `reports/round-5x..76x/accept-{c,ca,o,d}.py`, counting `--selftest` | 0 mentions in every counter behind a SELFTEST-BARE row |
| `SHA256SUMS.txt` | sha256 of checker, fixtures, drafts and receipts (final, regenerated after the last rerun) | checker `dbd736b6a3cd…`; selftest receipt `09670d07…`; base probe `c9b4bd07…` |

Hashes in `SHA256SUMS.txt` match the final stage files. The base probe reads the copy `SKILL.base-44f76d45.md.copy-for-probe` (sha256 `c63d286d…`), which is the committed `44f76d45:SKILL.md` byte-for-byte.

Reads: `git cat-file`/`git show` on the base commit only. No `git` mutation. No build, lint or test runs outside the checker's own selftest, which the task asked for. Installs: none. Python 3.14.8 was already present; no tool was installed or updated.

## 3. Base registry findings

Source: `probe-base-rows.txt` at `44f76d45`, lines as cited.

| class | rows (line) | observed | repair route |
|---|---|---|---|
| SHAPE (9 cells) | accept-c-66 (686), accept-ca-66 (687), accept-o-66 (688), accept-c-67 (689), accept-ca-67 (690), accept-o-67 (691) | verdict cell `ACCEPT-*: PASS|FAIL` has an unescaped pipe, so the row splits into 9 cells in GFM | correction note N1 (draft §3); do not edit the six rows |
| VERDICT-NOCODES | uncertainty-inventory (658) | verdict map gives `0` and `2` only; exit `1` is not stated in the row | correction note N2; L1 must confirm the script's exit-1 meaning from its docstring before writing it |
| SELFTEST-BARE (20) | accept-c-53…59 (7), accept-d-59, -60, -62, accept-c-61, -63, -64, -65, -68, accept-o-62, -63, -64, accept-ca-64, -65 | the cell is a bare dash. `counter-selftest-mentions-base.txt` shows zero `--selftest` in each counter, so the dash is accurate, but the row gives no reason | correction note per row giving the reason; not drafted (see §4) |
| PINNED-BARE (30) | every counter row with a dash in pinned values (list in `probe-base-rows.txt`), e.g. accept-c-53, accept-o-55 | not yet read per counter; the pin may be in the script (QUALITY 23/25/28), but the row does not say so | correction note pointing to the pin location, after reading each script |
| row 709 `note` | accept-c-73 / accept-ca-73 correction | kind `note`, prose verdict; passes now | none |

Things the probe did **not** flag, and why that matters:

- **CMD-PATH-ABSENT: none.** Every backticked `python3 … <path>` in the tool rows names a file present at `44f76d45`. This is a presence check, not an execution check.
- **Owners: all `kotodama-shokunin`** across the 56 eight-cell rows (the six nine-cell rows were not owner-tallied). No blank owners among the 62 graded rows (the checker's OWNER-EMPTY finds none).
- **Names: unique** in both tables.

## 4. Drafted artefacts (stage only)

- `skill-row-check.py` — the checker. Read-only. Parses the exact 8-column header, grades every body row, exits 0/1/2. Last line `REGISTRY-ROWS: PASS|FAIL rows=n [findings=m]`.
- `fixtures/` — 9 cases (`expected.json` states exit, verdict and codes for each): green complete rows; green escaped pipe; red unescaped pipe; red bare self-test; red bare pinned; red absent script; red non-Python command with three blank cells; per-cell red rows (empty command, verdict with no codes, empty write scope, unknown kind, duplicate name, empty name, and a write scope of `as needed`); a control with no registry table. `fixtures/tree/tools/present.py` is a presence stub for the path check; it is never executed.
- `draft-registry-rows.md` — the field contract, the base findings, note rows N1 and N2 (checker-clean), and candidate shapes for `ledger-token-guard`, `accept-o-79` and `accept-ca-79`. Those shapes are not rows yet.
- `mutants/` — the eight mutants plus the control, as run.

Not drafted, and why: the N3 and N4 texts for the 20 SELFTEST-BARE and 30 PINNED-BARE rows. Writing them now would state pin locations and reasons that were not read per counter.

## 5. Checker self-test evidence

Each red fixture is killed only by the rule it names. Mutation run (`mutation-receipt.txt`):

| mutant | removed rule | selftest | killed by |
|---|---|---|---|
| M0 control | none | 9/9 | — |
| M1 always-pass stub (no selftest branch) | all | no summary line, exit 0 | the consumer must require the `SELFTEST:` line and exit 0 — a stub that prints nothing and exits 0 is not caught by its selftest |
| M1b print-expected-selftest-line | all | 9/9 | **not killed by its own selftest**; only an outside harness that re-runs the frozen `fixtures/` and compares the `CASE` lines refutes it |
| M2 no path check | CMD-PATH-ABSENT | 8/9 | red-absent-script |
| M3 naive split (ignores `\|`) | escape handling | 8/9 | green-escaped-pipe |
| M4 no bare-self-test check | SELFTEST-BARE | 7/9 | red-bare-selftest, red-non-python-command |
| M5 no shape check | SHAPE | 8/9 | red-unescaped-pipe-shape |
| M6 no duplicate check | NAME-DUP | 8/9 | red-per-cell-rules |
| M7 verdict accepts any number | VERDICT-NOCODES | 8/9 | red-per-cell-rules |
| M8 no empty-name check | NAME-EMPTY | 8/9 | red-per-cell-rules |

Two things the table does not show:

- `red-non-python-command` and `red-per-cell-rules` each carry several rules, so one fixture kills several mutants. Each rule is still shown able to fail by a fixture that fails only on it, except CMD-NOT-PYTHON and OWNER-EMPTY, which are covered only inside `red-multi`. That is adequate, but a reviewer should see it named.
- The selftest does not show that the checker's verdict matches a real script's exit codes, nor that a pin is correct. Those are review-only (§6).

## 6. Limits and review-only clauses

- **Not checked mechanically:** whether the verdict map matches the script's real exit codes; whether a pinned value is correct; whether a placeholder such as `pending` is absent (a `pending` cell passes the shape check). Consumers must run the counter itself.
- **Note rows are exempt** from the tool fields. Row 709 is a note inside the tool table; the rule that notes are exempt is not written in `SKILL.md`. L1 must decide whether to state it. A note with a `python3` command is not graded as a tool.
- **Kind rule:** any kind not starting with `note` is graded as a tool row. An unknown kind therefore gets the full tool checks and also a KIND finding.
- **Header:** the table header is `pinned values`, not `pinned fixtures` as the task list words it. The checker matches the header exactly. Renaming the header would break every historical row and the parser; keep the header and name the fixtures inside the pinned-values cell.
- **Cannot yet verify** the candidate O and Ca rows (draft §4). Each row is valid only when `skill-row-check.py --rev <lands> --root <lane> --rows <names>` prints `ROW OK` for it and every dependent cell is filled from landed bytes.

## 7. Recommended handling for L1

1. Decide where the checker lives (`tools/check-registry-rows.py` or elsewhere). Its selftest receipt must be committed with the checker (QUALITY 23).
2. Apply N1 and N2 as appended `note` rows. Do not edit the historical rows.
3. Decide N3 and N4 after each of the 20 + 30 counters has been read for its reason and pin location.
4. Write the O and Ca rows only after `tools/ledger-token-guard.py`, `reports/round-79/accept-o.py` and `reports/round-79/accept-ca.py` land. Each row's cells come from the landed bytes; do not copy them from the wave spec.
5. Run the checker on the landed `SKILL.md` at the lands revision, with the O and Ca rows and N1/N2 in it: `--rows ledger-token-guard,accept-o-79,accept-ca-79,<N1>,<N2>`.

## 8. Host and write-scope record

- Wrote only: this report, and `.ufo/waves/round-79/w1/stage/ScribeRegistry/` (checker, fixtures, drafts, receipts, mutants, `SHA256SUMS.txt`).
- Scratch `/fast/scratch/hyaku/kotodama-r79/ScribeRegistry/` was used for the base copy and mutant runs. Receipts were copied to stage before the scratch was removed.
- No write to `~/.local/bin`, no fleet-root file, no `git` mutation, no subagent dispatch, no waiting on peers, no model parameters.

Report: `.ufo/waves/round-79/w1/ScribeRegistry.md` (relative to `/home/vgpnk/Projects/shokunin/kotodama-shokunin`)
