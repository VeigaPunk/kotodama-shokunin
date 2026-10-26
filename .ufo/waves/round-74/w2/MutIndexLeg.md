# W2 seat MutIndexLeg — ATTACK the INDEX leg and corpus/README.md (round 74 WAVE 2, falsify; hyaku run 7)

Date: 2026-10-25. Lane repo: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` (read-only for me).
Revisions: base `f7104cbce186bc2e1522abf0cfd619cc834628bb`; freeze F3 `00c408a0af2fa5ddf65af2224152ce258b26d896`; lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5`. Frozen INDEX leg (claims.json, claim C leg 13): one row per adopted entry in the culture-material section, body = the entry's own `` - `name.md` — `` row with the entry's `- topic:` text verbatim, last `Counts checked` footer total = 249 and vector = the six partition counts, "older footers are byte-identical".

## Isolation and method

- Seat clone: `D=/tmp/MutIndexLeg/r74clone` (`git init`; `git -C "$D" rev-parse --show-toplevel` printed exactly `/tmp/MutIndexLeg/r74clone`; `git clone -q <lane> "$D/lane"`; `checkout --detach <lands>`; `branch -f main <lands>`; `checkout main`). Final state: `main == HEAD == c4bf61a8d722f9168ce0fd8021a6261c000610c5`, worktree clean. The real lane tree, its jj/git state and index were never touched; no fleet file written.
- The counter materializes its own clone and grades the **committed** lands tree (its header: `worktree graded: no (leg bytes read only from the checkout and the git-archive base tree)`). Worktree edits are invisible to it, so each mutant is a **commit in the seat clone** with `main` repointed to it (branch moves inside `$D/lane` are sanctioned by the tasking), counter run at `--lands <mutant sha>`, then `git reset -q --hard <lands>`. Mutator `/tmp/MutIndexLeg/mutate.py` (byte-exact anchored edits, each asserted to change the file); raw outputs `/tmp/MutIndexLeg/out-*.txt`.
- Command template (cwd `$D/lane`):

```
python3 -B reports/round-74/accept-c.py --root . --lands <lands> --freeze 00c408a0af2fa5ddf65af2224152ce258b26d896 --fleet-root /home/vgpnk/Projects/shokunin
```

## Baseline (pristine bytes)

`corpus/README.md` sha256 `0531f7a3d16bee20329c9b042eb865be13bb6c54e4e5a158a2f864f3eae3708e`; `find corpus/knowledge -type f -name '*.md' | wc -l` = 249.

```
LEG PASS INDEX
ACCEPT-C-74: PASS legs=13/13
exit=0
```

## Mutation table (ten mandated + two bonus probes)

All runs are the baseline command with `--lands <mutant sha>`; mutant commits carry only `corpus/README.md`.

| Mutant | Change to corpus/README.md | Expected per frozen leg text | Fired | Verdict | lands sha | README sha256 |
|---|---|---|---|---|---|---|
| M1 | swap the two adopted rows inside `## culture-material/` (lines 445/446) | nothing — leg is silent on row order | no — `PASS legs=13/13`, INDEX green | **SURVIVED** | `72321398e095` | `1542e193f9dd…` |
| M2 | paraphrase adopted row body ("practitioner craft of specifying a setting" → "craft of specifying settings") | INDEX (verbatim) | yes — `index row is not the entry's \`- topic:\` text verbatim`; `FAIL legs=12/13` exit 1 | KILLED | `c78f2b4ffd38` | `2644163ae81e…` |
| M3 | duplicate the `worldbuilding-setting-practice.md` row in place | INDEX (exactly one) | yes — `worldbuilding-setting-practice.md has 2 index rows (want exactly one)` | KILLED | `0d3fbeb16f56` | `0991b3b04a04…` |
| M4 | move the amend row under `## synthesis/ (29)` | INDEX (must be in culture-material section) | yes — `worldbuilding-setting-practice.amend-2026-10-23.md index row is not inside the culture-material section` | KILLED | `1b182c57c470` | `f7cee04d1f8f…` |
| M5 | last footer `total 249 files` → `248` | INDEX | yes — `last footer total 248 != the 249 .md files at lands` | KILLED | `fd3a6c3e8be2` | `ed98a89eaa50…` |
| M6 | last footer vector `32/29/40/29/24/95` → `29/32/40/29/24/95` | INDEX | yes — `last footer vector [29, 32, 40, 29, 24, 95] != the landed partition counts [32, 29, 40, 29, 24, 95]` | KILLED | `8826cfd7ea21` | `decd55446547…` |
| M7 | pre-round-73 footer `(total 243 files; …)` → `240` | INDEX (older footers byte-identical) | yes — `an older \`Counts checked\` footer is not preserved byte-identically` | KILLED | `e8d2690a0b9f` | `b57a600dd73f…` |
| M8 | adopted row duplicated in a trailing block **after the last footer** (outside any section) | ambiguous; implementation counts rows file-wide | yes — `has 2 index rows (want exactly one)` (global uniqueness) | KILLED | `48326aeec0cf` | `0a75b679db8c…` |
| M9 | extra partition-shaped heading `## archaeology/ (0)` before Known gaps | INDEX (six partition counts) | yes — `README declares 7 partition sections (want six)` plus `last footer vector [32, 29, 40, 29, 24, 95] != … [32, 29, 40, 29, 24, 95, 0]` | KILLED | `51859c63e1f0` | `a224a57d3fd5…` |
| M10 | single trailing space appended to the adopted row line | INDEX per "verbatim" | no — `PASS legs=13/13`, INDEX green | **SURVIVED** | `8f1895592246` | `5f9e1a99814b…` |
| M7b (bonus) | the **last base footer** — the round-73 landing reading `(total 247 files; …)` — edited to `246` | INDEX per "older footers are byte-identical" (plural, unqualified) | no — `PASS legs=13/13`, INDEX green | **SURVIVED** | `d157f6a4899b` | `875fe8771227…` |
| M11 (limit probe) | heading counts made actively wrong: `## culture-material/ (36)` → `(99)`, `## linguistics/ (30)` → `(12)` | expected survive (heading numbers are unread) | no — `PASS legs=13/13`, INDEX green | LIMIT CONFIRMED | `28b3d9426d21` | `1e5a9c63686e…` |

Full lands SHAs: M1 `72321398e095108a5716fe8f82e4ce19851e4023`, M2 `c78f2b4ffd38dd9f8d7d6e9423c24b306f388aad`, M3 `0d3fbeb16f56852a408a1a8ec38f368fedd60551`, M4 `1b182c57c4709266e32856b1cd8d1ef8b843b8de`, M5 `fd3a6c3e8be23c07e83dc5ac085bb15c7f5dd09c`, M6 `8826cfd7ea21a75ad62a4abcb26d0db80061142e`, M7 `e8d2690a0b9f0c60c840bc15e55cce5fb50e557b`, M7b `d157f6a4899bfdcec752999c80b8fe8e4b8e22cb`, M8 `48326aeec0cf702f7a377aba52cab45d21c333d9`, M9 `51859c63e1f064ec29828f350cf9ac3b56bdecbe`, M10 `8f1895592246c527b832d05bade4129521d91512`, M11 `28b3d9426d2195899af5432f7a6057666d0df3eb`.

## Findings

**F1 — MEDIUM — "older footers are byte-identical" is enforced only for base footers `[:-1]`; the immediately-preceding live footer can be silently rewritten.** The counter's preservation loop is `for blk in _footer_blocks(base_text)[:-1]:` (`reports/round-74/accept-c.py:1825`). At base the README has exactly two footer blocks (243-footer at base line 734, 247-footer at base line 777), so only the pre-round-73 footer is pinned; the round-73 landing footer — the previous live reading — is exempt. Mutant M7b rewrites `(total 247 files; directory totals 32/29/38/29/24/95 …)` to `246` and INDEX stays green: `ACCEPT-C-74: PASS legs=13/13`, exit 0, lands `d157f6a4899bfdcec752999c80b8fe8e4b8e22cb`. The frozen leg text says "older footers are byte-identical" without exempting any; the landed tree keeps that footer identical, so pinning all base footers is compatible with the claim. The counter's own junk-landing selftest exercises `index_older_footer_edited` (`accept-c.py:2832`) only against the pre-round-73 footer, so its controls never see this half. Proposed fix: iterate `_footer_blocks(base_text)` without `[:-1]` (every base footer must appear byte-identically at lands; only the last lands footer may differ).
Raw output (M7b): `LEG PASS INDEX` / `ACCEPT-C-74: PASS legs=13/13` / `exit=0`.

**F2 — LOW — "verbatim" is `strip()`-lenient.** The row body is compared after stripping: `hits.append(rm.group(2).strip())` (`accept-c.py:1785`), and the entry topic is stripped too, so M10 (one trailing space on the adopted row line, lands `8f1895592246…`) passes `ACCEPT-C-74: PASS legs=13/13`. "Its body the entry's own `- topic:` text verbatim" should fail a mutated row line; fix by comparing the raw `README_ROW_RE` group(2) (only the topic read is stripped) or by rejecting row lines with trailing whitespace.

**F3 — LOW / observation — row order inside the section is unconstrained.** M1 (the two adopted rows swapped, lands `72321398e095…`) passes `ACCEPT-C-74: PASS legs=13/13`. This is a coverage note, not an implementation bug against the frozen rule: the INDEX leg text imposes no order, and the counter's selftest has no order mutant. If a later reconcile wants filename order enforced (the round-73 block narrates its rows as "in filename order", README line 785), INDEX will not catch a reorder.

**F4 — LIMIT (asked question) — the 'last Counts checked footer' rule is satisfiable by a README that is wrong elsewhere, and the landed README itself is such a README.** INDEX reads only: the adopted rows' existence/uniqueness/section/verbatim-body, the six partition heading *names* (for the vector), the last footer's total+vector vs the tree, and base footers `[:-1]` byte-identity. Nothing reads the per-heading counts or any other README prose. Concretely, at pristine lands `corpus/README.md:407` says `## culture-material/ (36)` while the live directory holds 40 files (last footer `32/29/40/29/24/95` at line 815; the landing block itself names the heading "left as filed and named as stale", lines 805-806); `corpus/README.md:344` says `## linguistics/ (30)` while linguistics holds 32 (line 785 says so); `corpus/README.md:749` still says `Total knowledge entries: 243.` — and the baseline counter run is `ACCEPT-C-74: PASS legs=13/13` on exactly those bytes. Probe M11 (headings actively renumbered to `(99)`/`(12)`, lands `28b3d9426d21…`) also passes `PASS legs=13/13`: heading numbers are decorative to INDEX. This is a declared scope limit of the leg (the landing block discloses the staleness), not a counter defect; recording it as the limit the seat was asked to decide.

## Run notes

- Two runs were inconclusive infrastructure failures, not detector verdicts, and were re-run to completion: M2 and M4 first attempts exited 2 with the single line `ERROR: materialize f7104cbce186 failed (git rc=0, tar rc=2)` while `/tmp` was at 100% capacity (wave-wide pressure; `df` showed 102M free). Re-runs produced the clean KILLED verdicts in the table. A baseline failure was never counted as a kill.
- The counter self-cleans its `TemporaryDirectory` scratch; no other seat's `/tmp` entries were touched. No web fetches were made (offline counter; fetch-hygiene N/A).

## Restoration evidence

```
== restored sha256(corpus/README.md)=0531f7a3d16bee20329c9b042eb865be13bb6c54e4e5a158a2f864f3eae3708e   # == pristine
git rev-parse main HEAD → c4bf61a8d722f9168ce0fd8021a6261c000610c5 / c4bf61a8d722f9168ce0fd8021a6261c000610c5
git status --porcelain → (empty)
final pristine run: pristine exit=0 / ACCEPT-C-74: PASS legs=13/13
```

## Tooling record

Nothing installed or upgraded (operator authorization 2026-10-19 noted; PACMAN paused host-wide — not used). Only `python3`, `git`, `tar`, `df`, `sha256sum` already on the host were used.

## Outcome

The mandated ten-way attack **killed 8/10 mutants** (M2-M9: every behavior the frozen INDEX text names — verbatim body, uniqueness, section membership, last-footer total and vector, six-section shape, pre-round-73 footer preservation — is actually detected, and the trailing-block duplicate is caught by global row uniqueness). It **failed to kill M1** (row order — outside the leg text) **and M10** (trailing space — F2). Bonus probe M7b survived (F1, the one direct leg-text vs implementation divergence). The claim's INDEX leg therefore stands at lands `c4bf61a8d722f9168ce0fd8021a6261c000610c5` with two under-enforcement findings (F1 MEDIUM, F2 LOW), one order-coverage note (F3), and the footer-rule limit confirmed against the landed tree itself (F4).
