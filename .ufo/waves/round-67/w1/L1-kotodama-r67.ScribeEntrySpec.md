# ScribeEntrySpec — claim-C entry design (medicine-healing-codes.md)

Seat: `L1-kotodama-r67.ScribeEntrySpec` (scribe, round 67, claim C drafting support).
Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (read-only; no git/jj writes, no commits).
Observation window: 2026-10-24T12:37Z–12:43Z (live wave; fragments were being rewritten while read).

## Behavior

Drafted the claim-C entry skeleton at `.ufo/waves/round-67/stage/entry-spec.md` (281 lines,
9 plan-level `##`). It is a **plan, not the entry**: it fixes the section skeleton, the 24-row →
section assignment, the medicine-as-code taxonomy, one-way Boundaries and lore-handoff text, and
the bullet template. Every cited bullet is explicitly deferred to the row fragments' `BULLET=`
lines; no claim text was invented.

Design delivered:

- **Register map** — owned: the code a culture writes onto sickness (aetiology, authority/canon,
  practitioner roles, institutions, materia, technique, crisis response, medical text genres).
  Table of six partial owners with the exact section each retains.
- **Medicine-as-code classes A–H** — aetiology, authority/canon, practitioner role, institution,
  materia, technique, transmission, crisis; each with the design question it answers and its rows.
  Analytic classes are multi-valued (S819 in B+F, S826 in F+G, S813 in C+H) but the **section
  assignment is single-valued** because ONEID forbids a second citation.
- **Section plan (10 H2, ≈79 physical lines vs the 250 cap)**: §1 owns/register map; §2 aetiology
  S805/S806/S807/S816; §3 canon S811/S808/S812; §4 practitioners S818/S823/S824; §5 institutions
  S810/S809/S822/S825; §6 materia S815/S828/S817; §7 technique+transmission S819/S826/S821/S814;
  §8 crisis S820/S813/S827; §9 Boundaries; §10 lore handoff.
- **Boundaries** — seven bullets, zero registry ids, file+section precision:
  `bathing-and-body-hygiene.md` (§8 therapy doctrine, five regimes incl. sweat-lodge family),
  `scent-perfume-aromatics-codes.md` (§3–§4 pomander/prophylaxis), `myth-symbol/purity-pollution-
  boundary-systems.md` (§2 boundary map, §5 attribution regimes), `culture-material/funerary-
  material-culture.md` (§2–§6 disposal/assemblage/monument/mourning/death register), plus the two
  duplicate-risk neighbours the review seat will test — `amulets-talismans-apotropaic-marks.md`
  (§4 danger-to-remedy, §9 prescriber classes) and `sacred-topography-pilgrimage.md` (§5 votive
  economy/incubation archive) — and a living-tradition restraint line.
- **Lore handoff** — five bullets, one-way, never canon: recipient, what is supplied, the questions
  handed over *unanswered*, the direction rule (lore may cite the entry; the entry never cites
  lore), and the rights caveat for real-world/living-tradition sources.
- **Bullet template** — `- <clause> (S<id>)` with ten hard rules: one line/one id; fragment
  `BULLET=` verbatim unless it fails the arithmetic; 6–25 content words; ≥3 in-order content
  words from the row's first quoted span; no >12-word verbatim run; in-order coverage of
  `teaches` <80% plus ≥1 novel word; fact+consequence, no padding openers; id nowhere else in the
  file; section order fixed.
- **Preflight** — an exact per-row snippet that loads `reports/round-67/accept-c.py` by path and
  reuses its own `cells`, `anchor_quote`, `content_words`, `ordered_hits`, `in_order_coverage`.
  Smoke-tested on base row S783 with the landed r66 scent bullet: `count 22 hits 6 cov 0.00
  novel 7` — runs clean (this is a mechanics test, not claim evidence).

## Gates

Not run, deliberately: `accept-c.py`, any frozen counter, `sweep.py`, `--selftest`, builds,
linters. The entry does not exist and the row set is incomplete, so any run would be a partial-leg
or worktree claim — forbidden by the claim's receipt discipline. **No PASS is claimed anywhere.**

Run (read-only, provenance):

| command | result |
|---|---|
| `git ls-tree -r --name-only ad5b52b0 -- corpus/knowledge \| wc -l` | 240 |
| `git ls-tree -r --name-only ad5b52b0 -- corpus/knowledge/culture-material \| wc -l` | 33 |
| `git show ad5b52b0:corpus/SOURCES.md \| grep -cE '^\| *S[0-9]+'` | 724 |
| tail ids at base | S797–S800 (`S801`–`S804` count 0) |
| base-tree filename census (claim's regex) | 0 files (grep exit 1) |
| `git rev-parse main` | `b78f8b8e61c273a6bd2321f0962d9d0bc1c92d21` (lane tip ≠ base; `git diff base -- corpus/knowledge` empty) |
| fragment preflight (accept-c functions, 20 `row-S*.txt`) | see findings |

## Findings (attacks / defects in the drafts, not the instruments)

1. **Out-of-set registry ids — sequenced, not banned (L1 ruling).**
   `rows/ScoutReject1/row-S829.txt`, `row-S830.txt`, `rows/ScoutReject2/row-S831.txt`,
   `row-S832.txt` carry ids **S829–S832**. In `accept-c.py`, `NEW_IDS` is S805–S828 and
   `EXTRA_IDS = {"S801","S802","S803","S804"}` (`C-APPEND`: `allowed_new = set(NEW_IDS) |
   EXTRA_IDS`), so if they sit in the tree when claim C's receipt is taken, APPEND reports each as
   `extra=<id>` → FAIL. I independently verified the Ca side of the conflict: `accept-ca.py`
   `R66_REJECTS = [S801..S804]` and its D4 leg fails unless `rej_opened_today >= len(R66_REJECTS)
   + 2` (i.e. 6 today-dated rejected rows), while C's APPEND forbids new ids outside its set — the
   two frozen counters are jointly satisfiable only by the L1's per-claim lands sequencing:
   A_r (S801–S804 dispositions) → A_c (claim C receipt; tree carries only S805–S828 over base) →
   A_ca (S829+ reject rows and the lesson). **Integration constraint: never commit S829–S832
   before A_c's stamped receipt exists.** All four are tier `C`, status `rejected`, used-by `—`.
2. **`BULLET=` id-suffix inconsistency.** S805 and S806 end with `(S805)`/`(S806)`; S811–S826 do
   not. Pasting as-is and appending the id yields two citations on one line → ONEID FAIL
   (`S805:citations=2`). The spec now mandates stripping any trailing `(S###)` before appending.
3. **S824 row-cell defect — no bullet can fix it.** `teaches` in-order coverage of the anchor
   quote is **1.00 ≥ 0.80** → RESTATE `S824:teaches_echoes_quote=1.00`. The teaches cell must add
   analysis, not repeat “isangoma [diviner], inyanga [herbalist] and umthandazi [faith healer]”.
4. **Clause quote-word floor failures.** S813 = 2 and S826 = 2 in-order quote content words
   (< 3 required) at the final snapshot. S818 was 2 at 12:40Z and was rewritten to 3 by 12:42Z.
   S811 passes at the floor (novel = 1) and is fragile. All other present fragments pass the
   arithmetic at the final snapshot (11 cells, tier A/B, mined, 2026-10-24, used-by the entry,
   live URL + same-page capture).
5. **4 of 24 target rows absent** at 12:43:19Z: S807, S808, S827, S828. 20 present: S805, S806,
   S809–S820, S823–S826, S821, S822 (the last two landed late and pass). The entry cannot be
   assembled yet.
6. **Fragments are live-churning**: S806 moved 2 → 7 in-order quote hits, S817 2 → 3, S818 2 → 3
   between 12:39Z and 12:43Z. Any audit (mine included) is a timestamped snapshot; re-run the
   preflight after the last row lands.
7. **Conflict, reported verbatim.** `rows/ScoutGapMed/gap.md` states: “(0 files; grep exit 1 = no
   match. `git show <base> -- corpus/knowledge/culture-material/medicine-healing-codes.md` fails —
   entry absent. Culture-material has 34 files, none medicine-named.)” — the base tree measures
   **33** (`git ls-tree` above). No counter leg reads this number, so the claim is unaffected, but
   do not copy “34” into the README revision note; the correct landing is 33 → 34 and 240 → 241.
8. **Integration traps recorded in the spec**: the entry's `- topic:` must be one physical line and
   must appear verbatim in the README row (`TOPIC` leg compares the first-line text as a substring
   of the row; `sweep.py` requires the row shape `` - `medicine-healing-codes.md` — <topic> ``
   with a real em dash); `- verified-at:` must be filled from the observed clone/lands run, never
   pre-written; ids must appear nowhere except bullet suffixes (ONEID also rejects foreign ids, so
   Boundaries/handoff/metadata must stay id-free).

## Touched surfaces

- Created: `.ufo/waves/round-67/stage/entry-spec.md`.
- Created: `.ufo/waves/round-67/w1/L1-kotodama-r67.ScribeEntrySpec.md` (this report).
- Nothing else written; no registry, corpus, README, LOG, SCORECARD, tools or counter files
  touched; no git/jj state changed.

## Out of scope / dependencies

- The entry itself, the 24 registry rows, the README row, `corpus/lessons/round-67.md` and the
  `- verified-at:` text are other seats' artifacts.
- Fragment defects 2–4 belong to the row owners; I did not edit their files.
- No tool install or upgrade was performed (nothing was needed), so nothing is recorded under the
  tooling directive; no pacman transaction was attempted.

## Artifacts

- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-67/stage/entry-spec.md`
- `/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-67/w1/L1-kotodama-r67.ScribeEntrySpec.md`

Report: /home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-67/w1/L1-kotodama-r67.ScribeEntrySpec.md
