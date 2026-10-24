# CriticRegistry — registry attack on the E12/E11 repair (round 67)

Seat `L1-kotodama-r67.CriticRegistry` (UFO-FSD critic, leaf). Read-only over the lane;
no git/jj writes; nothing installed or upgraded (python3, git, gawk via the frozen
instruments only). Base revision `ad5b52b0…`; instruments read:
`reports/round-67/accept-c.py` (APPEND leg `:349-375`), `reports/round-67/accept-ca.py`
(D2 leg `:157-190`, D4 `:207-239`), `scripts/sources-census.sh` (`usedby_findings`
`:538-571`, `row_pass` E12/E04 `:580-694`, `--file` dir resolution `:497-504`),
`reports/round-67/telemetry/dry-run-ca.txt`, `claims.json` Ca statement.

Sibling convergence noted: `RevCensusE12` (same wave) already executed the move variants
and shows the census-clean disposition is V4 = move + S753 `—` + **S753 `mined→rejected`**
(V2 leaves `E04 S776 dup of S753`). My attacks below are on the *frozen predicate's
enforcement surface*, which that verification did not probe: the rename shortcut, the
dead S753 check, and the universal mutable-cell clause.

## Direct answers to the assignment

**Q: does moving S776/S779–S800 into `## Registry` break APPEND? — No; the move is
legally allowed and APPEND cannot see it.** APPEND is **id-keyed, never positional**:
`base_set`/`tip_set` are `{sid: line.rstrip()}` dicts (`accept-c.py:353-354`);
`missing_old`, `extra_ids`, `mutable_bad` all iterate ids (`:355-371`). A byte-identical
row relocated from `## Leads (unopened)` (base line 830-852) to `## Registry` keeps the
same dict value → invisible to APPEND. Residuals: `ROW_RE = ^\|` anchors at column 0
(`:73`), so re-indenting a moved row (up to 3 spaces is census-legal, `sources-census.sh:541`)
drops it from `tip_set` → `missing_old` FAIL (fail-closed, good); trailing whitespace is
normalized by `.rstrip()` (`:353`) — a cosmetic slip-through, harmless.

**Q: can the S753 `'-' → '—'` flip carry an anchor or tier change? — No.** Anchor is
cell 5, tier cell 3; both the S753 clause (`oc[:10] == nc[:10]`, `:365-367`) and the
general mutable clause (`oc[:7] == nc[:7] and oc[8] == nc[8]`, `:368-370`) freeze cells
0–6. What the flip *can* carry is worse — see CE2.

## Sequencing note — L1 resolution (received mid-write, recorded verbatim effect)

Per L1: per-claim lands separation. A_r (S801–S804 + r66 dispositions) lands before
A_c; claim C's receipt runs at A_c where APPEND sees only NEW_IDS∪EXTRA_IDS appended
over base. The >=2 extra rejects (drafted S829+) land between A_c and A_ca, so Ca's D4
counts them at A_ca while C's APPEND never sees them. The joint predicate is
satisfiable as sequenced — no counter revision. **Effect on my findings:** CE1/CE2 are
evaluated at A_ca and stand unchanged. CE3 stands, sharpened: at A_c, APPEND must
absorb the r66 dispositions as *base-diff* (move + S753 `—` + status flips — all legal
only because of the universal mutable clause); and at A_ca, D4's
`rejected_opened_today` still cannot distinguish appended S829+ gate rejects from
status-flipped `opened 2026-10-24` base rows (S753/S776 and the 21 other moved rows all
carry that date), so "gate reject" provenance remains unenforced either way.

## CE1 (strongest): the E12 repair can be faked by renaming the section

**Counterexample:** instead of moving the 23 rows, edit line 780 from
`## Leads (unopened)` to `## Registry`. Then:

- `accept-ca.py` D2 placement passes: `reg_pos` = first heading *containing* the
  substring "Registry" (`:172-175`, base `## Registry` at line 26);
  `leads_pos` falls back to `len(reg)` because no heading contains "Leads" anymore
  (`:175`); every R66 row satisfies `reg_pos <= m.start() < leads_pos` (`:180`).
- Census E12 passes: `row_pass`/`usedby_findings` gate on `in_registry`, set by
  `trim(substr(line,3)) == "Registry"` exact-match (`sources-census.sh:611`, `:547`);

  the renamed heading turns `in_registry=1` for lines 830-852, so the rows validate as
  registry rows (E04 S776-vs-S753 still needs the status flip — same as any variant).
- APPEND passes untouched (id-keyed, CE-independent).
- Non-row Leads bullets are ignored by every leg (ROW_RE only).

Result: **zero bytes of any S-row move**; the claim statement "S776/S779–S800 moved into
## Registry" is technically satisfied (there is a `## Registry` containing them) while the
file now carries **two `## Registry` headings** — the section identity the disposition was
meant to restore is duplicated, and future appends have two candidate tails. D2's heading
scan uses substring `"Registry" in t` / `"Leads" in t` and takes the *first* match only,
so it is weaker than the census semantics it pairs with.

**Impacted axes:** calibration (receipt says repaired; section structure is degraded),
provenance (identity of the registry section).

**Smallest safe correction (D2, ~4 lines):** collect `reg_heads = [s for t,s in heads if
t.strip() == "## Registry"]`, require `len(reg_heads) == 1`, set `end` = position of the
next `## ` heading after `reg_heads[0]` (or `len(reg)`), assert each R66 row's `m.start()`
inside — mirroring census `in_registry` exactly. That kills both the substring match and
the duplicate-heading shortcut; a real move still passes.

## CE2: the S753 `'—'` check in D2 is dead code — any mined-exempt disposition passes

`accept-ca.py:183-186`: `m753.group(0)` is only the match `| S753 |` (the regex
`^\|\s*S753\s*\|` does not extend to end-of-line), so
`c753 = [x.strip() for x in m753.group(0).split("|")[1:-1]]` is `['S753']`, `len == 1`,
and the guard `len(c753) == 11 and c753[10] != "—"` **can never fire**. The only
enforcement of the flip is therefore census E11, and E11 is **mined-gated**
(`usedby_findings` continues unless `status == mined`, `sources-census.sh:559`). Two
predicate-clean dispositions follow:

- **Demotion (already the executed plan):** S753 `mined→rejected` — sibling V4's
  census-clean variant — leaves `used-by: -` byte-present forever and still satisfies
  `status` validity (E07), D2 placement, APPEND's general mutable clause, and D2's dead
  cell check. QUALITY criterion 18 independently names S753 a durability failure, so the
  flip is *defensible* — but the predicate certifies "S753's used-by is '—'" while the
  cell stays `-`. Receipt **overclaim**, not caught.
- **False provenance:** keep `mined`, set `used-by` to any existing path (e.g. the
  games-play entry): E11 passes (file exists), APPEND allows cell-10 flip on S753, dead
  check silent → a fabricated citation link lands in the registry. Only `review_only`
  eyes would catch it.

**Impacted axes:** calibration (the named disposition is unverified), false provenance.

**Smallest safe correction (D2, ~3 lines):** match the full row —
`re.search(rf"(?m)^\|[^|\n]*S753[^|\n]*\|.*$", reg)` or capture `m753 = re.search(
r"(?m)^\|\s*S753\s*\|[^\n]*$", reg)` — then split `m753.group(0)`, require
`len(c753) == 11 and c753[10] == "—"`, and also assert `c753[7] in ("mined","rejected")`
*plus* the disposition actually taken is the one claimed (if status flips, require it be
recorded — e.g. require `c753[7] == "rejected" and "REJECTED:" in c753[6]`, or keep mined
and require `—`). Either pins one declared shape instead of "whatever makes E11 quiet".

## CE3 (surface, not a single exploit): APPEND's mutable clause is universal

`accept-c.py:368-370` lets **every** one of the 724 base rows flip status / recheck /
used-by in place, unrestricted — the comment admits it ("Status/recheck/used-by cells are
mutable in place"). The S753 `ALLOWED_FLIP` adds nothing beyond it (its cell-0-9 freeze is
the *stricter* case). Consequences the predicate cannot see:

- Any base row's `used-by` can be rewritten to point at any entry — citation provenance
  is rewritable wholesale under a "registry grows append-only" claim (accept-c docstring
  `:11`).
- Any base row can be demoted `mined→queued/rejected`, exempting it from E11/W01/W03 —
  the exact mechanism CE2 needs for S753 is available for *all* rows.
- D4's `rejected_opened_today` (accept-ca.py:226-235) counts rows whose *current* status
  is rejected with `opened == 2026-10-24` — the 23 moved rows all carry
  `opened 2026-10-24`, so flipping any two of them to `rejected` inflates the "round-67
  gate rejects" count without a gate ever firing. (The claim's intent is gate rejects.)

Anchor/tier/kind/scope/teaches stay frozen (cells 0–6), so this is a provenance surface,
not content mutability. **Impacted axes:** calibration, hidden regression on used-by
graph. **Smallest safe correction:** bound the general clause to a declared set
(`ALLOWED_FLIP`-style `MUTABLE_IDS = {"S753", "S776"}` or whichever dispositions the wave
declares) — new rows don't need it and undocumented base-row flips should be
`mutable_bad`. If the fleet convention is that these cells are legitimately mutable any
round, the alternative correction is a `review_only` line: "every base-row status/
recheck/used-by diff is printed for review" — one line in the APPEND detail printing the
`mutable_bad`-adjacent allowed flips by id.

## CE4 (weaker, recorded): D2 placement interval is overshot on the right

With `## Leads` intact, `leads_pos` = its position, so rows dropped into `## Search log`
or `## Paths` (between Registry-start and Leads) satisfy the leg's interval — they still
fail census E12, so the leg's own placement test adds no signal beyond the census call it
duplicates. Fail-closed today, but the leg as written certifies nothing census doesn't;
fixing per CE1 makes it exact.

## What holds

- STAMP discipline: `mv_rev == lands` pinned via clone whose `main` is reset to the stamp
  (dry-run-ca.txt shows `stamped==evaluated==ad5b52b0`, exit 1 on base bytes — control
  healthy). `--file` mode resolves `dir` = registry's parent-of-corpus via realpath
  (`sources-census.sh:497-504`), so E11 path checks run against the **clone**, not the
  caller's CWD — no moved-worktree path leak in D2.
- E04 duplicate-authority detection is order-agnostic (`url_scope_nonrejected` keyed by
  url+scope, `:643-654`): neither row order nor relocation dodges it; one of S753/S776
  must be rejected (or teaches rewritten — impossible, cell 6 immutable). The "just move
  rows" minimal repair provably cannot reach census exit 0 — sibling V2 census shows
  `E04 S776` exactly.
- Truncated/extended rows: APPEND `missing_old` catches deletion; `cells() != 11`
  catches field drift; census E01 catches NF!=13.
- `opened`/`opened_epoch` validation (E08) applies to moved rows for the first time —
  all 23 carry `2026-10-24`, today, so clean.

## One-line summary

The row move is APPEND-legal and cannot ride anchor/tier changes, but the frozen legs
under-specify the repair they certify: **a `## Leads → ## Registry` rename fakes the move
(CE1), and D2's S753 `'—'` assertion is dead code that both the mined-demotion and
false-provenance dispositions walk through (CE2)** — while APPEND's universal mutable-cell
clause (CE3) makes every base row's status/recheck/used-by silently rewritable under an
"append-only" claim. Two ~4-line counter patches (exact-heading + real row match) close
CE1+CE2; bounding `MUTABLE_IDS` closes CE3.
