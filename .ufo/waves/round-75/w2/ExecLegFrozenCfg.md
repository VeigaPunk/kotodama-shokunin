# ExecLegFrozenCfg — round 75, wave 2: FROZENCFG leg of the claim-C counter

Seat: executor (leaf). Lane: `/home/vgpnk/Projects/shokunin/kotodama-shokunin` at
base `f556d1049fe651d3d63975600b13acd9fb686f15`. Frozen leg text read from
`reports/round-75/claims.json` claim `C`, `legs[11]` (status then: "FINAL — wave-1 and
wave-2 attacks applied"; the leg text is byte-identical to the wave-1 draft for this leg).
Fixture git work happened only in `/fast/scratch/hyaku/kotodama-r75/ExecLegFrozenCfg/`
(removed before yield, every fixture asserted `rev-parse --show-toplevel` == itself before
its first commit). No lane/fleet/index mutation, no network, no tool installs
(`python3`, `git` already present; pacman not used). `reports/round-75/accept-c.py` was not
touched. `part-cfg.py` did not exist in `w2/parts/` when this leg was built, so the first
pass used a hand-built cfg exactly per `CFG-CONTRACT.md` (§ "cfg"); the real loader landed
during the build and every scenario was re-graded through it (§5.3), so the shipped part is
validated against ExecCtrCfgMain's `load_frozen_config`, not only against a stand-in.

**Files written:**

| path | sha256 | lines |
|---|---|---|
| `.ufo/waves/round-75/w2/parts/leg-frozencfg.py` | `97093e8208da170bd3fce24071d1b1162c55b8f12b87f34683fdf8b6c1e410ba` | 572 |
| `.ufo/waves/round-75/w2/ExecLegFrozenCfg.md` | this report — its digest cannot live inside itself; it is stated in the seat's yield summary | — |

AST check: the file's top-level nodes are **FunctionDefs only** (11 functions; no module
statements, no imports). Helpers are `_frozencfg_ids _frozencfg_paths
_frozencfg_strings _frozencfg_counts _frozencfg_blob _frozencfg_ledger_path
_frozencfg_rows _frozencfg_staged_map _frozencfg_compare _frozencfg_detail`; the leg is
`leg_frozencfg(ctx)`. No shared helper from PART A / part-cfg is redefined; PART A's
`git git_bytes is_ancestor leg dedupe counter_sha256 TOKEN_RE CLAIMS ROUND hashlib json re`
are called as-is. `python3 -B -m py_compile` is clean both for the part alone and for
PART A (lines 1-510) + the part concatenated (46961 bytes).

## 1. The leg wording as I read it (verbatim from claims.json)

> FROZENCFG: row set, entry paths, fragments, reject counts and every constant are read
> from `git show <freeze>:reports/round-75/claims.json`; the by-document map is read from
> `git show <freeze>:<map.path>` whose sha256 equals map.sha256; never from the graded
> tree; `<freeze>` is an ancestor of `<lands>` on its first-parent chain (`<lands>` ==
> `<freeze>` is graded, not refused); claims.json at `<lands>` is byte-identical to the
> freeze blob

Wave-2 dispatch adds two limbs that the wording does not name, and this build carries
them as instructed (both are marked in the file and flagged in §6.1):
`sha256(the running counter) == the committed reports/round-75/accept-c.py at <lands>`
when that path exists; and `ledger.json` at `<lands>` byte-identical to its freeze blob
(claim Ca's pin).

## 2. Ambiguities and how they were resolved

Every reading is also a comment in the part file (R1-R9), so a later reader of the counter
sees the same reasoning at the check that enforces it.

| # | Ambiguity | Resolution |
|---|---|---|
| R1 | "read from `git show <freeze>:…`; never from the graded tree" is not observable from inside a leg (cfg is handed in) | **Re-derivation**: `_frozencfg_compare` re-reads the frozen blob and re-derives *every* cfg constant it can name — base, rows (order), `row_staged`/`reused_staged` (per lane id, as id sets so a "/"-composite like `S876/S885/S917/S921` is handled), reused, entries, fragments, terms, refused staged ids, refused file specs, counts, map path/sha256, frozen leg names, `claim_keys`, access date, `allowed_ids`, `forbidden_ids`, `row_doc` and `owned_inplace` (the last two when the loader exposes them). Any cfg value not derivable from the frozen bytes fails. |
| R2 | "ancestor … on its first-parent chain" — plain ancestry also admits a merge-side freeze | Membership in `git rev-list --first-parent <lands>`. A freeze reachable only through a merge parent gets its own reason ("reachable … but not on its first-parent chain (merge-side freeze)") rather than the generic "not an ancestor". |
| R3 | `<lands> == <freeze>` "is graded, not refused" | No special case: the freeze is the first element of its own first-parent chain, and every byte comparison degenerates to the freeze blob against itself. Verified green (P1) — exactly the do-nothing control's expectation. |
| R4 | "byte-identical" vs. equal hashes | Literal **byte** comparison of `git show <lands>:<path>` against `git show <freeze>:<path>`; the hash is used only where the wording names a sha256 (map pin, counter self-pin, cfg `frozen_sha256`). |
| R5 | self-pin "when that path exists" (dispatch) | Path derived from PART A's `ROUND` (`reports/round-%d/accept-c.py`), never hardcoded. If absent at lands: no failure, state `counter=absent` in the detail (P2). At `<lands> == <freeze>` the limb reduces to "the bytes at the freeze are the bytes of the counter that is grading", i.e. it proves the freeze-pinned counter is the one running; it stays green when the run is the committed counter (P1). |
| R6 | ledger.json is not in claim C's leg text (dispatch: "and ledger.json too — claim Ca's pin") | The ledger path is read from the **frozen config itself** (the claim that declares a `ledger`), then both blobs are compared byte-wise. Kept because the ledger is part of the round's frozen constant surface and because Ca's own FROZENCFG pins the same bytes, so a combined tree that grades green cannot be failed by it. If the L1 judges the limb outside claim C's wording, deleting the single R6 block leaves the rest intact. |
| R7 | "reject counts"; the L1 moved to an integer-only `counts` (`{adopted 3, path_present 6, refused 31, total_staged_files 40}`) with the prose in the sibling `counts_note` | The frozen `counts` is treated as an **integer surface**: both sides are reduced to their integer keys (`key -> int`), so int-vs-str rendering and a prose sibling *inside* the object are not tests, while a drifted or dropped count is (S2/S3 below). When the freeze declares no counts there is no frozen referent, so no failure (CFG-CONTRACT allows `{}`). |
| R8 | "every constant" and vacuity | Empty frozen row set / entry list / fragments / terms is a FAIL: those are exactly the values that would make the data legs vacuous (carried from the round-74 leg). |
| R9 | a map that is pinned but unreadable | The map blob must also parse as JSON: an unparseable map is not a by-document map that COLLCHECK could read. Records/semantics stay COLLCHECK's. |
| — | `map.sha256` null (draft state) | Treated as **uncheckable and therefore red** ("the frozen map.sha256 is empty"): the map pin is the leg's own subject (F14 in `RevClaimsFidelity.md`; `ExecRenumber.md` §3 supplies `778068a431db1f82e9492007f0f4ecf03af21c46679695e91f9981dff56d5155`). The freeze **must** fill it. |
| — | `claim_keys` shape (claim object vs. round document) | Accept either `sorted(claim.keys())` (round-74's loader shape) or `sorted(doc.keys())`; both are freeze-derived, so the test still proves "not from the graded tree". |
| — | `refused_staged` shape (ids vs. raw prose) | Containment rule: every cfg id must occur in the frozen rejects prose, and every prose id that is not an adopted lane id must be recorded. This accepts both the contract's `["S870"]` and a loader that keeps the raw string (P3), while an invented id fails (M8e) and S893 (a lane id mentioned in the prose) needs no recording. |
| — | "contiguous ids" | Deliberately **not** in this leg: contiguity is the ROWS leg's clause ("adds exactly the frozen row_set (contiguous ids)"); FROZENCFG grades the frozen row set only, so a non-contiguous freeze is ROWS's red, not a double red here. |
| — | ORDER of detail lines | PART A prints the whole detail; the contract caps the **first** line at 300 chars. First line is the first failure reason (truncated at 300) or the frozen-constant summary when green; further reasons are indented continuation lines. Measured: max first line in the run below = 300 chars. |

## 3. Interface with the sibling parts (for ExecCtrCfgMain / the L1)

- **Signature**: `leg_frozencfg(ctx)`; returns PART A's `leg("FROZENCFG", ok, detail)`
  (bool). Reads only `ctx["root"]`, `ctx["lands"]`, `ctx["cfg"]` — never `mat`/`mat_base`,
  no network, no scratch writes.
- **cfg keys required** (absent ⇒ FAIL with "cfg lacks the frozen constant …"):
  `freeze frozen_sha256 base access_date rows row_staged entries fragments terms
  refused_staged refused_files counts map_path map_sha256 frozen_legs allowed_ids
  forbidden_ids claim_keys` (all in CFG-CONTRACT § cfg).
- **cfg keys used when present** (tolerant, never required): `reused reused_staged
  row_doc owned_inplace`.
- **Exactness expectations**: `freeze`, `frozen_sha256`, `base`, `map_path`,
  `map_sha256`, `access_date` are compared as strings; `counts` as integer keys only;
  `rows` order-sensitive;
  `frozen_legs` order-sensitive, case-insensitive; entries/fragments/terms/file specs
  compared as sets of stripped strings; staged ids compared as sets.
- **No help needed from part-cfg's leg helpers**: none of `_row_url_keys _gate_admit_row
  _min_entry_words _evidence _window _entry_citations` is used, so no ordering hazard
  between part-cfg and this part.
- `access_date`: if the frozen claim/document declares it, it must equal cfg's; otherwise
  it must occur **in the frozen bytes** (the contract's "derived from the frozen
  legs/after text"); a date invented by the loader fails (M8c).
- Frozen base and lands must both be 40-hex; the base must be a **strict** ancestor of
  lands (`is_ancestor` is strict, so lands == base is red here too — the counter's own
  refusal normally catches it earlier).

## 4. Test rig (reproducible, scratch-only)

`D=$(mktemp -d -p /fast/scratch/hyaku/kotodama-r75/ExecLegFrozenCfg)`; `git -C "$D" init -q`;
`test "$(git -C "$D" rev-parse --show-toplevel)" = "$D"` asserted before the first commit;
every commit built with `git -C "$D" -c user.name=fx -c user.email=fx@example.invalid commit`.

The fixture repo is a real three-commit history built exactly like the round's shape:

1. **base** — `README.md` + `corpus/SOURCES.md` (a 1-row registry).
2. **freeze** — adds, with identical bytes to the running test counter,
   `reports/round-75/accept-c.py`, plus `reports/round-75/claims.json`,
   `reports/round-75/ledger.json` and
   `.ufo/waves/round-75/assimilation/id-renumber-map.json`.
   The frozen claims document is the **live lane draft** with only two writes:
   top-level `base` ← the fixture's base commit, and `claims[C].map.sha256` ←
   `778068a431db1f82e9492007f0f4ecf03af21c46679695e91f9981dff56d5155` (the real map blob's
   digest at `.ufo/waves/round-75/assimilation/id-renumber-map.json`) — a faithful stand-in
   for the freeze the L1 will make. Everything else (9 rows S885-S893 with the 4-id
   `S876/S885/S917/S921` composite, 3 entries, 9 fragments, 2 terms, the S870 refusal
   prose, the 13 leg texts, `owned_inplace`) is the draft's own bytes.
3. **lands** — a legal landing: adds the entry and one registry row; leaves the claims,
   ledger, map and counter untouched.

The counter under test is `PART A (lines 1-510) + leg-frozencfg.py` plus a **scratch-only
driver** appended after the leg that (a) builds the cfg dict per CFG-CONTRACT from
`git show <rev>:reports/round-75/claims.json`, (b) applies at most one named mutation to
that dict, (c) calls `leg_frozencfg` with `ctx = {root, lands, cfg, mat: None, …}`. The
driver is not part of the delivered part file and never enters the lane.

Each mutant is its own commit whose parent is the lands commit (one edit per commit, so
each red has a single cause); mutants that must be frozen-state have their own freeze
commit. Command per scenario:
`LE_ROOT=$D LE_FREEZE=<rev> LE_LANDS=<rev> LE_BASE=<rev> [LE_CFG_SRC=<rev>]
[LE_CFG_MUTATE=<name>] python3 -B build/accept-c.py` (the counter's `__file__` is the
committed copy, so `counter_sha256()` is the real self-pin input).

## 5. Positive control and mutants — measured results

Exit code 0 = leg green, 1 = leg red (the driver returns the leg's bool). `rc` below is the
process exit. All ids below come from **one** run; the harness is deterministic — commits
carry pinned author/committer dates, and two consecutive runs produced byte-identical logs
(`diff -q run1.log run2.log` empty), so the table can be reproduced exactly with the recipe
in §4. Fixture commit ids are fixture-local and name nothing in the lane.

### 5.1 Positive (must PASS)

The full positive receipt (P0), verbatim:

```
LEG PASS FROZENCFG
     freeze 540e8bdc6d2c: constants from git show 540e8bdc6d2c:reports/round-75/claims.json (sha256 c412b2e95a3983d3); rows S885 S886 S887 S888 S889 S890 S891 S892 S893; entries 3; fragments 9; terms 2; refused S870; access 2026-10-27
  lands 23a08395c8aa: lands==freeze=no first-parent-chain=yes claims@lands=frozen-bytes map=.ufo/waves/round-75/assimilation/id-renumber-map.json(sha256-match) ledger=frozen-bytes counter=self-pinned
MOCK RESULT: PASS
```

P1 (the do-nothing shape `<lands> == <freeze>`) prints `lands==freeze=yes` and still
**PASSES** — `lands==freeze` is graded, not refused, and FROZENCFG is green, which is what
the claim's `do_nothing_control` requires.

### 5.2 Mutants and tolerance probes

| # | scenario | rc | first detail line (the reason / summary) |
|---|---|---|---|
| P0 | legal landing, lands > freeze | 0 | `freeze …: constants from git show …` (summary) — **PASS** |
| P1 | lands == freeze (do-nothing) | 0 | summary + `lands==freeze=yes … counter=self-pinned` — **PASS** |
| M1 | **claims.json edited at lands** (one extra space in a frozen term) | 1 | `reports/round-75/claims.json at lands 51bea0283d92 differs from the freeze blob (counter config edited in the graded tree)` |
| M2 | **map edited at lands** (one trailing byte) | 1 | `the map .ufo/waves/round-75/assimilation/id-renumber-map.json at lands 447779f6694f differs from the freeze blob` |
| M3 | **counter edited at lands** (one appended comment) | 1 | `the counter's own sha256 bf4736e92848932f is not b58b857b43c4's committed reports/round-75/accept-c.py (685ba9ed2ab37c5d), so this run is not the frozen counter` |
| M4 | **map hash drift at the freeze** (map content changed, `map.sha256` kept) | 1 | `the map … at freeze hashes to fc6a7c4ccee609f0, the frozen map.sha256 is 778068a431db1f82` |
| M5 | **cfg read from the graded tree** (cfg built from the edited lands blob) | 1 | `reports/round-75/claims.json at freeze hashes to c412b2e95a3983d3, cfg says 1e93984442e20a93` + `cfg ground terms [narrative  structure, narratology] are not the frozen terms [narrative structure, narratology]` + claims byte identity red |
| M6 | **frozen map.sha256 null** | 1 | `the frozen map.sha256 is empty: the by-document map is uncheckable at this freeze` |
| M7 | **non-first-parent freeze** (freeze on a merge side branch, lands = the merge) | 1 | `freeze 79a88e807111 is reachable from lands 67f0e0f34adb but not on its first-parent chain (merge-side freeze)` |
| M8a | cfg row set has an extra id S894 (all bytes frozen) | 1 | `cfg row set S885 … S893 S894 is not the frozen row set S885 … S893` |
| M8b | cfg entry list drops one path | 1 | `cfg entry paths [...] are not the frozen entry paths [...]` (300 chars, truncated) |
| M8c | cfg access date invented (`2026-10-28`) | 1 | `cfg access_date 2026-10-28 does not occur in the frozen claims.json` |
| M8d | cfg `map.sha256` replaced by zeros | 1 | `cfg map.sha256 0000000000000000 is not the frozen map.sha256 778068a431db1f82` (+ map drift line) |
| M8e | cfg `refused_staged` gains S899 | 1 | `cfg refused_staged S899 names ids the frozen rejects prose does not` |
| M8f | cfg ground terms dropped | 1 | `cfg ground terms [-] are not the frozen terms [narrative structure, narratology]` |
| M8g | cfg `row_doc[S886]` names a different document | 1 | `cfg row_doc[S886] 'https://example.invalid/unrelated-document' is not the frozen document 'https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1120 ('` |
| M8h | cfg `owned_inplace` after_text `(33)` instead of `(32)` | 1 | `cfg owned_inplace [...] is not the frozen owned_inplace [...]` |
| M9 | claims.json not committed at the freeze | 1 | `cannot read reports/round-75/claims.json at freeze d159fb12767d` (no traceback: the leg fails, it does not crash) |
| P2 | counter **not** committed at lands (path absent) | 0 | `… counter=absent` — **PASS** (the limb is conditional, per R5) |
| P3 | cfg `refused_staged` holds the raw prose string | 0 | summary with `refused S870's staged quote (…)` — **PASS** (R: tolerance for the loader shape) |

M1-M4 are the four mutants the dispatch named (edited claims at lands, edited map at
lands, non-first-parent freeze, map hash drift); M5-M9 and the M8 series additionally
prove that the *constants* limb is not decorative: with every graded byte frozen-identical
(M8a-M8h), a cfg value that the freeze does not declare is the only failing input, and it
is caught in each case.

Each red prints exactly one reason except where two independent limbs genuinely fire
(M5: cfg shipped from the wrong blob + the graded bytes differ; M8d: the cfg pin *and* the
blob hash disagree with it). No scenario produced a traceback. M6 exercises the leg's own
defence for an unusable map pin; in the *shipped* assembly that state never reaches a leg,
because `load_frozen_config` refuses first (see 5.3, R7).

### 5.3 Integration with the real `part-cfg.py` (delivered after this leg was built)

`w2/parts/part-cfg.py` (ExecCtrCfgMain) landed while this seat was testing. The same
fixtures were re-graded with the **real** loader in place of the hand-built cfg:
`PART A (1-510) + part-cfg.py + leg-frozencfg.py` assembles to 71115 bytes, `py_compile`
clean, and the driver calls `load_frozen_config(root, freeze)` before `leg_frozencfg`.

| # | scenario | rc | result |
|---|---|---|---|
| R0 | legal landing, lands > freeze | 0 | **PASS**, `refused_staged=['S870']`, `forbidden=S864 S865 S866 S870 S876 S902 S904 S905 S917 S919 S921`, `access_date=2026-10-27`, all 23 CFG-CONTRACT cfg keys present |
| R1 | lands == freeze | 0 | **PASS** (`lands==freeze=yes … counter=self-pinned`) |
| R2 | claims.json edited at lands | 1 | `reports/round-75/claims.json at lands 0ecdca06d7bc differs from the freeze blob (counter config edited in the graded tree)` |
| R3 | map edited at lands | 1 | `the map … at lands ed5a60e5061e differs from the freeze blob` |
| R4 | counter edited at lands | 1 | `the counter's own sha256 dceb2e24e2a4dba1 is not 03fbcbf93d46's committed reports/round-75/accept-c.py (1e5960a737f0cc7b) …` |
| R5 | map hash drift at freeze | 1 | `the map … at freeze hashes to fc6a7c4ccee609f0, the frozen map.sha256 is 778068a431db1f82` |
| R6 | cfg read from the graded tree | 1 | `… at freeze hashes to c412b2e95a3983d3, cfg says 1e93984442e20a93` + `cfg ground terms [narrative  structure, narratology] are not the frozen terms […]` + claims byte identity red |
| R7 | frozen map.sha256 null (loader path) | 2 | `MOCK REFUSED (ConfigError): claim map.sha256 at freeze is not a 64-hex digest (the by-document map cannot be pinned): None` — **no leg ran**: the counter refuses, matching PART A's documented exit 2 |
| R8 | non-first-parent freeze | 1 | `freeze 8ee4a3c724a3 is reachable from lands 3e885bebca75 but not on its first-parent chain (merge-side freeze)` |
| R9a | cfg row set gains S894 | 1 | `cfg row set … S894 is not the frozen row set …` |
| R9b | cfg access date invented | 1 | `cfg access_date 2026-10-28 does not occur in the frozen claims.json` |
| R9c | cfg `row_doc[S886]` wrong document | 1 | `cfg row_doc[S886] 'https://example.invalid/unrelated-document' is not the frozen document …` |
| R9d | cfg `refused_staged` = the frozen prose (`refused_staged_text`) | 0 | **PASS** — the real loader's id-extraction shape (`['S870']`) and the prose shape both grade green |

Full-assembly check: `PART A (1-510) + part-cfg.py + the ten leg parts in the contract's
order + part-selftest-run.py + part-main.py` (13 of the 14 files; `part-selftest-fixtures.py`
had not been delivered yet) concatenates and `python3 -B -m py_compile`s clean, and
`part-main.py`'s `LEGS` already binds `("FROZENCFG", leg_frozencfg)` at position 12 of 13.

Re-test after the L1's `rejects.counts` change (integer-only counts + the prose moved to
the sibling `rejects.counts_note`; claims.json then `b7923cd6780ee54401140f2b33de0e56a1fdc26ec0e30383d8ef65cdb2d8c669`),
run through the real `load_frozen_config` on fresh deterministic fixtures:

| # | scenario | rc | result |
|---|---|---|---|
| S0 | legal landing, integer counts | 0 | **PASS**; cfg counts `{'adopted': 3, 'path_present': 6, 'refused': 31, 'total_staged_files': 40}` |
| S1 | lands == freeze | 0 | **PASS** — FROZENCFG green on the frozen tree, as required |
| S2 | cfg `counts.adopted` drifted to 4 | 1 | `cfg reject counts [('adopted', '4'), …] are not the frozen counts [('adopted', '3'), …]` |
| S3 | cfg drops `refused` | 1 | `cfg reject counts [('adopted', '3'), ('path_present', '6'), ('total_staged_files', '40')] are not the frozen counts […]` |
| S4 | claims.json edited at lands | 1 | `reports/round-75/claims.json at lands b8314655d58d differs from the freeze blob …` |
| S5 | frozen `counts` also carries a prose sibling inside the object | 0 | **PASS** — non-integer values are dropped on both sides (the tolerance the L1 asked for) |
| S6 | S5 fixture at lands == freeze | 0 | **PASS** |

Conclusion for assembly: the leg agrees with ExecCtrCfgMain's loader on every cfg key
(`rows` order, `row_staged` lists, `refused_staged=['S870']`, `forbidden_ids` of 11 staged
ids, `claim_keys`, `owned_inplace`, `row_doc`, `terms`, `counts` = the four frozen integers), grades green on the
legal landing and on `lands == freeze`, and is red on every junk path with one-line
reasons. No change to `leg-frozencfg.py` was required by the integration run.

## 6. Risks, blockers and notes for the L1

1. **Dispatch-added limbs vs. claim wording.** Claim C's FROZENCFG text names
   `claims.json` only; the ledger limb (R6) and the counter self-pin (R5) come from the
   wave-2 dispatch (and, for the ledger, from claim Ca's own FROZENCFG). Ca's leg pins the
   same ledger bytes, so no legal combined tree is failed by either limb — but if the L1
   decides claim C must not be *stronger* than its frozen text, they are two isolated
   blocks (marked `R5`/`R6`) and can be deleted without touching anything else.
2. **`map.sha256` must not freeze as null.** As drafted, claim C's `map.sha256` is `null`.
   Two consequences, both measured: the shipped loader refuses outright
   (`ConfigError: claim map.sha256 at freeze is not a 64-hex digest`, exit 2 — R7), and if
   a cfg with an empty pin ever reached this leg it would be red ("the frozen map.sha256 is
   empty", M6). Either way the do-nothing control's "FROZENCFG green at `lands == freeze`"
   is unattainable until the freeze fills the pin. ExecRenumber supplies
   `778068a431db1f82e9492007f0f4ecf03af21c46679695e91f9981dff56d5155` for the map blob as
   it exists today; re-hash if the map is edited again before the freeze.
3. **Assembly compatibility.** Built before `part-cfg.py` existed, so the first pass was
   validated against a hand-built cfg per CFG-CONTRACT § cfg; `part-cfg.py` then landed and
   §5.3 re-ran every scenario through the real `load_frozen_config` — green where it must
   be, red where it must be, no change needed. The comparisons stay tolerant about *shape*
   (sets for entries/fragments/terms, id extraction for staged/refused values, `claim_keys`
   from either object, `row_doc`/`owned_inplace` only when exposed) and strict about
   *content*; any future loader change that breaks a key prints the exact key in the reason.
4. **Self-pin and the worktree.** The run must be the committed counter: if the lane
   worktree's `reports/round-75/accept-c.py` has uncommitted edits while lands carries the
   frozen blob, FROZENCFG goes red with "this run is not the frozen counter". That is the
   intended reading of H1; the do-nothing receipt must be produced by the committed file.
5. **Vacuity left to other legs (deliberately):** row contiguity (ROWS), the map's
   records/document join (COLLCHECK), the *content* of the frozen constants as data
   (ENTRIES/ROWS/…). This leg grades only that the constants are the freeze's and that the
   freeze is what sits at `<lands>`.
6. **No blockers.** Everything the leg reads exists at the freeze by construction
   (`claims.json`, `ledger.json`, the map and the counter are all named in the claim's
   freeze surface); if any of them is missing the leg says which one and where.

## 7. Scope and hygiene

- Wrote exactly two files — the part above and this report. Read-only use of the lane's
git objects; no
  `git add/commit/checkout/stash/reset`, no jj, no writes under the fleet root, `scripts/`,
  `templates/`, `.ufo/state`, the lane tree outside `w2/`, or `shokuknow`.
- Scratch `/fast/scratch/hyaku/kotodama-r75/ExecLegFrozenCfg/` (build copies, three
  fixture repos, `run.log`) deleted before yielding; every number and receipt quoted above
  is reproduced in this file.
- No tools installed, no network fetches, no pacman.
