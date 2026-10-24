# ConnectorSiblings — round 67 wave 1

Seat: ConnectorSiblings. Read-only fleet scan. No tools installed. No lane files mutated.

## Evidence

### Medicine / healing register — no sibling owner

Filename walk of `*-shokunin/corpus` (skip `.git`) for medicine, healing, physician, surgery, apothecary, hospital, leech, physick, shaman, curandero, herbal, remedy, bath, hygiene, scent, perfume, prophylaxis, purity: the only knowledge entries are inside kotodama.

- `kotodama-shokunin/corpus/knowledge/culture-material/bathing-and-body-hygiene.md`
- `kotodama-shokunin/corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md`
- `kotodama-shokunin/corpus/knowledge/myth-symbol/purity-pollution-boundary-systems.md`

Sibling `PROVINCE.md` files do not claim this register. Content hits in other lanes' `corpus/knowledge` are homonyms, not partial owners:

| Hit | What it actually is |
|---|---|
| `kumitate-shokunin/corpus/knowledge/ops-watchers.md:114` | `healing = --rebind \|\| --settle \|\| --repair` — dispatcher queue repair |
| `kaidoku-shokunin/PROVINCE.md` / `corpus/knowledge/2026-10-13-doctor-taxonomy.md` | `rea doctor` environment verdict |
| `audio-shokunin/corpus/live/r88-reviewer/r88r_surgery.py` | audio live-script name |
| `game-dev-2d-shokunin/corpus/live/r93-*/**/*purity*` | animation-purity probe logs |
| kagi / souji / kake / tabi "hygiene" | credential, repo, crawl, or sweep hygiene |
| "remedy" in kake, kama, kotoba, kengaku, mado, souji, tabi, tameshi, tsukuroi | a bugfix sentence, not a physician code |

### Nearest partial owners (all intra-lane)

1. **Bathing** (`bathing-and-body-hygiene.md`). Owns the water-and-body institution (`:14`). States the load-bearing split at `:50`: ritual purity is status, hygiene is contamination, "must not be merged." §8 (`:86-102`) already owns bathing-as-therapy, Semmelweis/Snow, and spa-town medicine-as-business. `:52` uses "a doctor who scoffs" as the leak's scene role, not as a register. Handoff is §12 (`:138-141`): lore receives regime, split, infrastructure, schedule, kit; this entry decides nothing about a world.
2. **Scent prophylaxis** (`scent-perfume-aromatics-codes.md`). Topic line (`:3`) includes "status and disease codes." The prophylaxis claim is one bullet, not a medicine file: `:31` pomander "ward off plague and other diseases" (S791), inside §3 containers. Ownership close (`:52`): scent/perfume/aromatics/incense register; neighbors keep their ground; "Hands off to lore-shokunin for canon."
3. **Myth-symbol purity** (`purity-pollution-boundary-systems.md`). Owns the boundary map and status, not matter-dirt. Axis 7 (`:35`) is "deliberately not this entry's" and points at bathing `:50`. Antisepsis trap (`:109`, DR-PP-08 at `:173`): status-pollution and hygiene-contamination stay separate; conflation is only an in-world belief. Proximity/air carrier (`:58`) names Greek miasma and a plague reading marked `to-verify` — pollution radius and fumigation, not a physician code. Handoff §14 (`:182-186`): canon is lore's; route is the worldbible contract; washing stays bathing's.

### One-way handoff rules (do not edit the three files)

- Kotodama proposes; lore records canon (`kotodama-shokunin/PROVINCE.md:16-25`). Lore's CM-g packet intake is still `uncovered`, and the contract digest is unacknowledged (`lore-shokunin/PROVINCE.md:19`, `:28`). `worldbible-integration-contract.md:15` — writing the contract is not lore's read. `:18` — a receipt does not delegate canon. `:68` — do not invent a sibling path. `:100` — canon standing is lore only. `:136` — transport ack is not a disposition.
- Therefore the new entry's handoff line is a **candidate packet**: recipient lore-shokunin, open question "which healing system exists in-world," status pending, never "lore will accept."
- No reciprocal edit of bathing, scent, or purity. Claim C's lands are the new entry plus registry rows; a patch into those three files is a new claim and dirties Ca's separability read of `lands` (same rule as round-50 `ConnectSiblingPastoral.md`).
- Chousa owns research method (`kotodama-shokunin/PROVINCE.md:19`; contract `:166`). Game-dev owns mechanics. Do not add a source-method rule or a hit-point/healing-spell rule.
- What the new entry may own, and only by citation: the physician / surgery / apothecary / remedy **code** (who practices, what the remedy is called, how the office is staffed). It must point at bathing §8, scent `:31`, and purity `:109` and stop. Restating Semmelweis, the pomander, or the purity/hygiene split is double ownership.

### Receipt-sequencing gate — no sibling owns it

`tools/check-receipt-seq.py` (header equality of stamped/evaluated/measured + tree + counter sha; `--lands` via `git show`; `--topo` carrier parent) has no sibling duplicate. Adjacent tools are different objects:

| Tool | Object it gates | Not this gate because |
|---|---|---|
| `chousa-shokunin/tools/quote-reopen.py` | live-URL quote reopen (VERBATIM/ABSENT/…) | quote liveness, not revision sequencing. Kotodama already has its own `tools/reopen-row.py` (round-62 adjacency). `argv-witness.py` / `mechanism-witness.py` witness a matcher argv, a different anti-shortcut |
| `tsukuroi-shokunin/tools/run-receipt.py:6-7` | runs a tool inside `git clone --no-local` at a named rev and writes a receipt naming that rev + tool sha | a **runner**. Kotodama's checker must not become one |
| `tsukuroi-shokunin/tools/check-report-receipts.py` | a report's "Gates at \<rev\>" has a committed receipt file | report-citation presence, not header equality |
| `tameshi-shokunin/tools/receipt-window.py:2-10` | receipt id + instrument sha + measurement interval vs a frozen edit window | fixture-craft window, not lands-stamp equality |
| `kama-shokunin/tests/llamacpp-live/check-receipt.py` and `tools/round33-gate-receipts.py` | llama-server probe receipts and one registry-gate audit | endpoint-health province |
| `souji-shokunin/PROVINCE.md:3-4,10-13,25-28` | a preservation/push receipt that authorizes deletion | "receipt" here means permission to remove files. Also: on jj-colocated lanes HEAD is normally detached and `refs/jj/keep/*` are not durable receipt roots |

## Affected axes

- **C (coverage):** improved if the medicine entry cites the three partials and does not absorb them. Harmed if it restates bathing §8, scent `:31`, or purity `:109`, or if a homonym (kumitate healing, kaidoku doctor) is cited as an owner.
- **O (operability):** not owned elsewhere, so landing `check-receipt-seq.py` does not collide. Harmed if the checker is implemented by calling tsukuroi's clone runner, tameshi's window, or chousa's quote reopen — those contracts do not grade stamped==evaluated==measured.
- **Ca (calibration):** the protocol Ca asserts ("never a moved worktree") is currently false for one leg of the draft checker. See the move. No axis trade: the fix does not touch the medicine entry.

## Proposed move

One change, in `check_counter_sha` only.

Today (`tools/check-receipt-seq.py:168-170`), even when `--lands` is set, the counter sha is `sha256` of the **worktree** file, and only if that file is missing does it fall through to `git show main:<counter>`. Receipt bytes under `--lands` already come from `git show <lands>:` (`:236`). The counter does not.

`accept-o.py` does not catch this. Its LANDS leg (`reports/round-67/accept-o.py:194`) passes a receipt and no counter, so `check_counter_sha` returns before the read (`:166`). Its TOPO leg pairs `tools/x.py` but does not pass `--lands`, and the fixture never dirties that file, so worktree bytes equal the pin. A repo whose counter changed after the lands commit — the r65/r66 shape, main moved past the stamp — will FAIL a correct lands pin, or PASS a pin that matches the dirty worktree and not the lands blob. The docstring (`tools/check-receipt-seq.py:13-17`) says `moved_past` is a flag, never a verdict change. This SHA read makes it a verdict.

Do **not** fix it by cloning the way `tsukuroi-shokunin/tools/run-receipt.py` does. That imports a sibling runner and hides the bug by making the worktree equal the rev. The checker already promised `git show`.

When `--lands` is set and a counter path is paired, hash `git show <lands>:<counter>` (the same committed-bytes read as the receipt). Leave the worktree-then-`main` read for the no-`--lands` default, which is what TOPO/HEADERS exercise. Do not retarget `--topo`'s `git log -1 main` (`:188-189`): `accept-o.py` R66 and TOPO legs pin that branch name, and souji's detached-HEAD note is a closure hazard to record, not a predicate change.

Medicine entry, separately and without editing the three neighbors: one handoff paragraph — candidate to lore, CM-g pending, cite bathing `:50` and `:86`, scent `:31`, purity `:109`, own only the practitioner/remedy code.

## Risks

- Hashing `<lands>:<counter>` changes a SHA result only when the counter blob at lands differs from the worktree. Current ACCEPT-O fixtures do not construct that case, so STAMP/SELFTEST/LANDS/TOPO/HEADERS stay as they are. A new selftest case that does construct it is the verification, not a frozen-leg edit.
- `check_counter_sha` re-encodes the blob as UTF-8 (`:174`). Fine for the ASCII counters this round ships; a non-UTF-8 counter would not match a raw sha256. Out of scope for this move.
- Treating kumitate "healing" or kaidoku "doctor" as overlap would shrink C's gap falsely and is the census error this note exists to block.
- Editing bathing, scent, or purity "to point back" would harm Ca separability and is refused.

## Verification

- Re-read `check_counter_sha` after the patch: under `--lands`, the hashed bytes are `git show <lands>:<counter>`; the worktree is not opened on that path.
- Existing `accept-o.py` LANDS invocation (receipt only) still prints `moved_past=True` and FAIL unreadable; TOPO still passes on the healthy fixture. Those legs do not need new flags.
- Add one selftest the frozen 14 do not cover: lands commit has counter bytes A and a receipt pinning sha(A); a later commit changes the counter to B; `--lands <lands> receipt counter` still PASS on sha(A). The same command without `--lands` FAIL (worktree is B). That is the moved-worktree class.
- Medicine draft: grep the new entry for Semmelweis, pomander, and "must not be merged" — those sentences stay in the neighbor files; the new entry only cites the path:line.

## Adjacency verdict

No sibling owns the medicine/healing/physician/surgery register, and no sibling owns a receipt-sequencing gate. Nearest culture owners are the three kotodama partials above, handed off one way. Nearest receipt prior art is tsukuroi's clone runner, which this checker must not become.

## Contradiction recorded (not a second move)

CriticFrontier: `accept-c.py` APPEND allows new ids only in S805–S828 ∪ S801–S804, while `accept-ca.py` D4 requires `rejected_opened_today >= len(R66_REJECTS)+2`. On one tip those predicates cannot both pass. Base `ad5b52b0` has 49 rows opened 2026-10-24 (S750–S800), every one `mined`, and 0 rejected rows opened that day. APPEND cell 8 (`opened`) is immutable, so flipping an old row's status cannot mint a 2026-10-24 open date.

L1 resolution (this round, no counter or claims revision): the predicates are sequenced, not co-stamped. A_r lands S801–S804 first (still inside EXTRA_IDS). C's receipt is stamped at A_c, where the only further appends are S805–S828. Ca's receipt is stamped later at A_ca, which carries the S829+ gate rejects and the round-67 lesson. Same-tip evaluation would fail APPEND; per-claim lands does not. This seat does not edit EXTRA_IDS.
