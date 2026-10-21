# ReviewSepFixtureFacts — round-49 facts the r50 separability fixture will freeze

- Seat: ChousaR27R2.ReviewSepFixtureFacts-4 (reviewer, leaf; no delegation).
- Claim: r50 **Ca** (calibration). Fixture `reports/round-50/separability/r49-fixture.json` (absent at base).
- Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin`; r50 base `4ad26836552462d28a946ca3b067cab0b5ce3532`.
- Method: read-only git (`show`, `cat-file`, `log`, `rev-parse`, `rev-list`, `merge-base --is-ancestor`, tree-to-tree `diff`, `ls-tree`), `sha256sum`, `awk`, `grep`. Scratch copies under `/tmp` only, removed afterward. One lane `git status` probe was run in error (§9).
- Notation: `path@commit:Lnn` = line nn of that commit's blob.

## 0. Verdict

Commits, the S-id range, the SOURCES row set and the receipt's input shas all match the assignment. The fixture cannot be frozen as the r50 claim text describes ("exits 1 naming the C->S dependency, 1/1 detected") until three things are decided:

1. **The r49 receipt's two separability legs both pass, and both are vacuous.** S→C is a real dependency that the receipt reports as absent (F1).
2. **The dependency set is more than one edge.** At `8c78e6b`, name and export rules yield at least four directed edges (F2).
3. **`corpus/README.md` is co-landed by C and Ca in one commit.** No commit holds a Ca-only README, so per-claim trees cannot be read from git history (F3).

Axis impact: calibration (F1, F2: the r49 receipt overstates separability); operability (F3, F5: per-claim freezing needs synthetic blobs; the base lessons-index pin is stale); coverage: none.

## 1. Commits (verified; history is linear)

| commit | parent | subject (abridged) | paths |
|---|---|---|---|
| `c42d675be96b6b3957e6e5c00ab192080cb70083` | `78f77a6965f8595bc24d013b90a3d146868b31d5` | round-49 framing | 4 A: `reports/round-49/{claims.json,targets.json,calib/r49-checks.json,telemetry/dispatch-declared.json}`; declarations, no landed claim bytes |
| `c6a174dd4830929e0f8f0de478bb8be29dfb803b` | `c42d675` | round-49: C entry (225), Ca stub removal + control, S SOURCES + lesson | 17 files, +2090/−6 (§2) |
| `8c78e6bee93a5b1a257d8b98e3d70b2281b35d71` | `c6a174d` | entry shelf note names only cited rows (C-without-S leg) | 1 M: entry, +1/−1 |
| `3596e2bb326be4aa1f3477efc07e8884939964fc` | `8c78e6b` | ledgers: validation receipt measured at 8c78e6b | M `LOG.md`, `SCORECARD.md`, `SHONEN.md`; A `reports/round-49/validation.json` |
| `8cee75561cab92c8da7edc501d6221b9f9b5cde8` | `3596e2b` | post-review fixes (1) | M `LOG.md`, `corpus/QUALITY.md` (+2, criterion 6), `corpus/SOURCES.md` (+4 rows S044–S047), `corpus/lessons/round-49.md` (+20) |
| `d91c632fe71515acc8e133a804ed2fcfbbe31264` | `8cee755` | post-review fixes (2) | M `LOG.md` (+6), `corpus/lessons/round-49.md` (+4) |
| `4ad26836552462d28a946ca3b067cab0b5ce3532` (r50 base) | `d91c632` | round-49 verifier spot-check | A `corpus/lessons/round-49-verifier-spotcheck.md` only |

`d91c632`'s parent is `8cee755`, not `8c78e6b`; `8c78e6b` is an ancestor. Base = `d91c632` + one commit.

## 2. Landed paths per claim

r49 `reports/round-49/claims.json@c42d675` declares **no `lands`**. Attribution below is inferred from `LOG.md@d91c632` (ADMITTED entry), `reports/round-49/claims-addendum-kaika.json@c6a174d` (S), `reports/round-49/integration/Ca-evidence.md@c6a174d` (Ca) and `reports/round-49/integration/merge.py@c6a174d` (S integration).

| path (landed at c6a174d unless noted) | numstat | claim | evidence / note |
|---|---|---|---|
| `corpus/knowledge/culture-material/hunting-foraging-subsistence.md` | +205 | C | `8c78e6b` changes one line (shelf note) |
| `corpus/README.md` | +25/−5 | **C and Ca** | Ca: −2 (`c42d675` L55–56, stub + blank; Ca-evidence L8–12, L56). C: +25/−3 (rev-2.6 block +21, row +1, `26→27` ±1, `224→225` and footer ±2). Shared file (F3). |
| `tools/check-readme-revisions.py` | +388 | Ca | the sibling control; names no C or S path |
| `reports/round-49/integration/Ca-evidence.md` | +134 | Ca | evidence |
| `corpus/SOURCES.md` | +165 | S | `8cee755` adds S044–S047 |
| `corpus/QUALITY.md` | +4 | S | pointer paragraph; `8cee755` adds criterion 6 (+2) |
| `SKILL.md` | +2 | S | pointer line |
| `corpus/lessons/round-49.md` | +293 | S | Gate; post-review +20 (`8cee755`) and +4 (`d91c632`) |
| `reports/round-49/claims-addendum-kaika.json` | +27 | S | declares S (depth, capability acquisition) |
| `reports/round-49/integration/{E1-sources.md,E2-sources.md,E4-sources.md}` | +64 / +107 / +91 | S | seat fragments |
| `reports/round-49/integration/{README.md,idmap.json,merge.py}` | +16 / +45 / +117 | S | `merge.py` rewrites the entry (F7) |
| `corpus/lessons/README.md` | +20/−1 | **undeclared** | round-49 row (L104) and Revision 4 block |
| `reports/round-49/run-validation.py` | +387 | **undeclared** | runner: verdicts for C, Ca, S and the separability legs |
| `LOG.md`, `SCORECARD.md`, `SHONEN.md`, `reports/round-49/validation.json` | — | ledger / receipt | `3596e2b`, `8cee755`, `d91c632` |

Count check: 17 files at `c6a174d`, matching `git show --stat`.

## 3. S-id range cited by the r49 entry

- `grep -o 'S0[0-9][0-9]'` on `hunting-foraging-subsistence.md@8c78e6b`: **66 tokens, 12 distinct, S031–S042** (contiguous, no S001–S030). Counts: S031 12, S032 8, S033 5, S034 7, S035 8, S036 3, S037 3, S038 4, S039 3, S040 5, S041 4, S042 4.
- L18 names `corpus/SOURCES.md` rows S031–S042; `corpus/SOURCES.md` is also named at L201.
- At `c6a174d` the same grep gives 13 distinct, S031–S043. S043 occurs once, at L18 ("S031–S043 (S043 is the rejected, uncited ScienceDaily item)"). `8c78e6b` removes it.
- Provenance: `idmap.json@c6a174d` maps E1 temp ids S101→S031 … S113→S043. `merge.py@c6a174d:L116` rewrites the entry's `\bS1\d\d\b` tokens through that map (F7).
- Each of the 12 ids resolves to a SOURCES row whose `used-by` names the entry (12/12, §4). That bidirectional link is the S→C edge in F1 and F2.

## 4. SOURCES rows defined at 8c78e6b

- **43 rows, S001–S043**, contiguous, no duplicate ids. Table lines `corpus/SOURCES.md@8c78e6b:L30–L72`; S031–S042 at L60–L71, S043 at L72.
- Status: mined 20, queued 19, rejected 4 (S028, S029, S030, S043).
- Tier: A 34, B 3, C 6.
- `used-by` names `corpus/knowledge/culture-material/hunting-foraging-subsistence.md` in **12 rows** (S031–S042, all mined). S043 has `used-by` `—`.
- Post-review growth (`8cee755`, carried to `d91c632` and base): S044–S046 (tier B, queued, `supersedes` S034/S038/S039, used-by `—`) and S047 (tier C, rejected, supersedes S029, used-by `—`). Base: 47 rows; mined 20, queued 22, rejected 5; A 34, B 6, C 7.

## 5. Receipt and runner facts

- `reports/round-49/validation.json@3596e2b`: all 10 `input_sha256` entries match the `8c78e6b` blobs exactly (README `666fb794…`, SOURCES `933013a1…`, entry `64cb0d55…`, lesson `272eab2e…`, addendum `7171f5f1…`, claims.json `501eb760…`, run-validation.py `9f5f7a2e…`, targets.json `6b1bb4c5…`, check-readme-heading.py `d4b4ff2a…`, check-readme-revisions.py `d49fdf1c…`). The receipt therefore measured **8c78e6b**.
- `separability.c_without_s.passed` = true (L257). `separability.s_without_c.passed` = true (L323). `verdict` = admitted (L352).
- The post-review commits `8cee755` and `d91c632` changed SOURCES and the lesson after this receipt. The receipt was not regenerated.

## 6. Findings

### F1 — HIGH — The receipt's separability legs are vacuous; S→C is real

- `c_without_s` (`run-validation.py@8c78e6b:L264–274`): `url_ids` are S-ids with an inline `**Sxxx** (https://` in the entry's `- source:` line. `no_inline_url = cited − url_ids`, and `passed = not no_inline_url`. It never consults the registry, so it cannot detect C→S. `LOG.md@d91c632:L4001` concedes this.
- `s_without_c` (`L276–289`, `L301–305`, `L322–324`): before running the census, the runner removes the entry path from every `used-by` cell and rewrites each row left with no `used-by` from `mined` to `queued`. The 12 rows S031–S042 therefore leave the census check, because census command 7 (index 6) inspects only `mined` rows. The `ENTRY` exemption at L303–305 then has nothing left to act on. The counterfactual is a temp file under the lane's `.scratch/` (L295–299) that the runner deletes afterward; the lane's `corpus/SOURCES.md` is not modified.
- Honest counterfactual (my scratch run, not a lane run): materialize the 25 non-entry `used-by` paths of mined rows from `8c78e6b` blobs, keep `corpus/SOURCES.md@8c78e6b` unmodified, leave the entry absent, and run census command 7 verbatim. Output: exactly 12 lines, `missing: corpus/knowledge/culture-material/hunting-foraging-subsistence.md`, one per S031–S042 row. **S→C fails the census.**
- Consequence: the r50 statement "c_without_s passed (0/1 known inseparable pair detected)" is confirmed as fact. The same pair is 0/2 under the r49 runner, and the receipt cannot serve as an oracle.

### F2 — HIGH — The static dependency set at 8c78e6b is at least four edges, not one

Rule: `X→Y` if X's landed bytes name a Y land path or match a Y export. Lands as in §2; all trees at `8c78e6b`.

| edge | evidence | rule |
|---|---|---|
| C→S | entry L18 (`corpus/SOURCES.md`, S031–S042), L201 (`corpus/SOURCES.md`) | land-path name; S-id export |
| S→C | SOURCES L60–L71 (12 `used-by` cells); `merge.py@c6a174d:L16` and `:L116` (writes into the entry); `run-validation.py@8c78e6b:L48` | entry-path name. The `merge.py` and runner edges depend on attribution (F6). |
| C→Ca | entry L21 (`corpus/README.md`, pinned sha `097c2910…`) | land-path name (README co-landed, F3) |
| S→Ca | lesson@8c78e6b L12 and 9 occurrences of `tools/check-readme-revisions.py`; 28 of `corpus/README.md` | Ca-tool path name |
| Ca→C (rule-dependent) | `Ca-evidence.md@c6a174d` L127 and L130 cite `culture-material/hunting-foraging-subsistence.md` (suffix only); the landed README (read at Ca's tree) names basename `hunting-foraging-subsistence.md` | suffix or basename rule only, or an export `hunting-foraging-subsistence\.md` applied to Ca's README bytes |

- Non-edges checked: entry L21 names `reports/round-49/claims.json`, which is declared bytes that no claim lands. `integration/README.md@c6a174d` L15 names `Ca-evidence.md` by basename only. Ca's tool and Ca-evidence name no S land.
- Export note: the contract example `\bS0(3[1-9]|4[0-3])\b` matches exactly S031–S043. That covers C's citations (S031–S042) and leaves S001–S030 uncovered, which does not affect detection.
- The r50 wording "1/1 detected" should become an exact expected edge set.

### F3 — HIGH — `corpus/README.md` is co-landed; git holds no per-claim tree for it

- `git log c42d675..4ad2683 -- corpus/README.md` returns only `c6a174d`.
- Ca's edit is −2 lines and C's is +25/−3. Ca's post-state is reproducible but never committed: `git show c42d675:corpus/README.md | awk 'NR!=55 && NR!=56' | sha256sum` = `097c2910e91d72d98cd98c167dc2c3e2ef50b11e9a0b7c8271441c261f44c5d7`, which matches Ca-evidence L48.
- The contract's file-level model (`X.tree` plus `lands`) cannot express hunk-level co-ownership. Reading Ca's bytes from `c6a174d` brings C's rev-2.6 block and row along.

### F4 — MEDIUM — C's verified-at pin names a README state that no commit contains

- `hunting-foraging-subsistence.md@8c78e6b` L21: "written at HEAD `c42d675…`", with "`corpus/README.md` sha256 `097c2910…`".
- `c42d675:corpus/README.md` = `756647a0…`. The README at every commit from `c6a174d` onward = `666fb794…` (the receipt input sha). `097c2910…` is F3's Ca-only reconstruction, which existed only in a working tree.
- So C's provenance pin depends on Ca's uncommitted edit.

### F5 — MEDIUM — Post-receipt drift and a stale base index pin

- After the receipt, `8cee755` changed SOURCES (+4 rows), QUALITY (+2) and the lesson (+20), and `d91c632` changed the lesson (+4). The receipt's SOURCES and lesson input shas no longer match HEAD.
- `corpus/lessons/README.md@4ad2683` L104 pins `round-49.md` as `bytes=35993 lines=293 sha8=272eab2e`. The base blob is 39223 bytes with sha256 prefix `51ab6a5c`. `round-49-verifier-spotcheck.md` (added by `4ad2683`) has no index row (0 matches).

### F6 — MEDIUM — Lands are inferred, not declared

- r49 `claims.json@c42d675` declares no `lands`. The addendum declares only S, and says S "verifies on corpus/SOURCES.md + corpus/lessons/round-49.md alone". F1 (the census needs `used-by` paths) and F2 (the lesson names the Ca tool) contradict that.
- Undeclared landed files: `corpus/lessons/README.md` (+20/−1) and `reports/round-49/run-validation.py` (+387, verdicts for all three claims). Ledger and receipt files: `LOG.md`, `SCORECARD.md`, `SHONEN.md`, `validation.json`.

### F7 — MEDIUM — S's integration tool rewrote C's landed entry

- `merge.py@c6a174d` L9 ("applies the E1 id map to the hunting entry"), L16 (ENTRY path), L116 (`ENTRY.write_text(re.sub(r"\bS1\d\d\b", …idmap…))`). The entry's S-ids are S's integration output, not C's own. A C-only tree must be built from `8c78e6b`, not from the pre-merge E1 draft.

### F8 — LOW — Naming collision and r50 before-checks

- "Ca" means different things in r49 (README revision stub and revisions control) and in r50 (separability). Fixture labels should be distinct, e.g. `r49-Ca`.
- The r50 before-checks hold at base: no `*separab*` file under `tools/` (0 matches); no "separab" in `corpus/QUALITY.md` (0); QUALITY has 6 criteria (criterion 6 at L29), so criterion 7 is the next number.

## 7. Fixture-author advice (not an admission)

1. **Trees.** Freeze C, Ca and S all at `8c78e6b`. It is receipt-consistent: 10 of 10 input shas match. If S is frozen at `d91c632`, record the delta: S044–S047 appended, none cited by C, exports widen to S001–S047, and the edge set is unchanged.
2. **README.** Either store two synthetic blobs with pinned shas (Ca-only = `c42d675` minus L55–56, sha `097c2910…`; C-only = `8c78e6b` README without Ca's hunk), or declare README co-owned and expect C↔Ca edges. Do not leave it implicit.
3. **Declare every landed file.** `corpus/lessons/README.md` (S), `run-validation.py` (harness, or explicitly S), ledgers (excluded). Record F7.
4. **Expected output.** Assert the full F2 edge set by set equality, not a count.
5. **Dynamic S-only leg (if run).** Base plus S.lands with the entry absent must fail census command 7 with 12 `missing:` lines. Treat that as the expected failure.
6. **Oracle.** Do not use the r49 receipt's `c_without_s` or `s_without_c` legs as an oracle.

Suggested exports (the fixture author decides): S = ids from `^\| (S\d{3}) \|` rows (S001–S043 at `8c78e6b`); C = `hunting-foraging-subsistence\.md`; Ca = `check-readme-revisions\.py`.

## 8. Unrun checks and gaps

- Not run: `check-claim-separability.py` (absent at base; r50 work), `run-validation.py` (writes `.scratch` and runs `git status`), `reports/round-28/readme/sweep.py`, `check-readme-revisions.py --selftest`, the lesson-index audit.
- The honest S→C result comes from my scratch tree of blobs, not from a lane run. The 25 `used-by` files were materialized with `git show 8c78e6b:<path>`.
- Static edges depend on a matching rule not yet implemented (full path versus suffix or basename) and on lands attribution (F6). Ca→C and the `merge.py` and runner S→C edges are attribution- or rule-dependent.
- Not verified: external sources, quotes and tiers (out of scope); the lesson's 23-row Mistakes count.

## 9. Tooling and lane hygiene

- Installs or updates: none. Tools used: git (read-only subcommands above), coreutils, `awk`, `grep`, `sha256sum`.
- Disclosure: near the end I ran `git -C <lane> status --porcelain=v1 -- corpus tools reports SKILL.md`. That was a mistake. `git status` can refresh the index stat cache, and I did not pass `--no-optional-locks`. It printed only `?? reports/round-50/`, which is untracked and not mine. I ran no other git write-capable command, no jj, and wrote nothing in the lane except this report. Scratch under `/tmp/r50rev` was removed.
