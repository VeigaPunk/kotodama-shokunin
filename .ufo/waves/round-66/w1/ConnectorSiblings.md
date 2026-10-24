# ConnectorSiblings — round 66 sibling overlap

Seat: ConnectorSiblings. Milestone: r66-v2. Axes judged: adjacency, coverage.
Lane read-only. No install. No sibling file absorbed.

## Evidence

Prescribed literal census (2026-10-24), `grep -rliE 'scent|perfume|incense|aromatic|unguent|kyphi|attar|copal'` over `lore-shokunin`, `chousa-shokunin`, `kotoba-shokunin`: **49 files**. A word-window classifier of those 49 shows they are substring accidents, not a register:

| Class | Count | Surface |
|---|---|---|
| lore, token `descent` only | 41 | 36 under `.ufo/` or `.scratch/`; 5 tracked corpus |
| lore, token `quiescent` | 3 | `.ufo/` |
| kotoba, token `quiescent` | 2 | `.ufo/` |
| chousa, token `adolescents` | 1 | `.ufo/` |
| chousa, token `quiescent` | 1 | `.ufo/` |
| kotoba strings dump (icon / MIME / minified HTML) | 1 | `.ufo/round-44/evidence/omp-live-18.12.2-strings.txt` |

Tracked lore corpus hits, all `descent` and nothing else: `corpus/SOURCES.md`, `corpus/knowledge/reference-ledger.md`, `corpus/knowledge/r94-cross-myth-design-comparison.md`, `corpus/fixtures/r87-myth-cluster/inspiration-note.md` (ETCSL “Inana's descent”), `corpus/fixtures/r93-m2-kojiki-cluster/README.md`.

Word-boundary re-run `(^|[^A-Za-z])(scent|perfume|incense|aromatic|unguent|kyphi|attar|copal)s?([^A-Za-z]|$)`: **1 file**, the kotoba strings dump. Inside it the only scent-lexeme tokens are icon names `md-scent` / `md-scent_off` (lines 2416051–2416052) plus `white_balance_incandescent`. No `corpus/`, `SOURCES.md`, or knowledge entry in any of the three lanes matches on a word boundary. **No sibling owns a scent/perfume/incense/aromatics register entry.**

Separability outside kotodama, prescribed `grep -rliE 'check-claim-separability|separability' /home/vgpnk/Projects/shokunin/*/tools | grep -v kotodama`:

- Hit: `tsukuroi-shokunin/tools/check-revision-binding.py:15` — a comment that extra probe fields are “not C2's grade (causal separability from C1/C3)”. Not `check-claim-separability.py`. Plus its `__pycache__` sibling.
- Miss: `lore-shokunin` and `kotoba-shokunin` have no top-level `tools/`. `chousa-shokunin/tools/research-gate.sh` does not match. Kotodama keeps `tools/check-claim-separability.py` (claims.json O, round-65 R65-D4).

## Who owns what (nearest prior art)

| Owner | What they own | Nearest art to this round | Absorb? |
|---|---|---|---|
| lore-shokunin | Fictional-world records (entities, relations, timeline), consistency checks, sourced-inspiration ledger with attribution / rights / AI-training kept as three questions (`PROVINCE.md:3-7`). Canon decisions. | Reader of `kotodama-shokunin/corpus/knowledge/synthesis/worldbible-integration-contract.md`. Packet intake CM-g is **uncovered** (`PROVINCE.md:23`). Bilateral acknowledgement of contract `kotodama-lore-adjacency` 1.0.0 is **pending** (contract `:15`). The descent corpus is myth-fixture prior art for lore, not for aromatics. | No. Report only. |
| chousa-shokunin | Research-record verification (`tools/research-gate.sh`) and the knowledge notes that document it. Scope screen: report, never absorb (`corpus/README.md` row `knowledge/scope-refusal-r12.md`). | Method for evidence retrieval when a scent-entry claim is actually a source-verification task (contract §10 row “Evidence retrieval methodology → chousa”). | No. Name the route; do not copy gate records into the entry. |
| kotoba-shokunin | SKILL.md / prompt-craft audit. Explicit anti-boundary: “NOT kotodama-shokunin: kotodama owns naming and language for fictional worlds” (`SKILL.md:14-15`). | None for this register. The strings dump is omp icon-font residue. | No. |
| tsukuroi-shokunin | Revision-binding check. The separability word there is grade isolation for tsukuroi's own C2. | Not an implementation of claim separability. | No. O does not call it. |
| kotodama-shokunin | The unowned scent register (claims.json C: 0 filename owners at `94209e8f…`), the new entry, rows S777–S800, and `tools/check-claim-separability.py`. Canonical contract copy lives here; lore reads it read-only (contract `:13`). In-lane handoff pattern already used by culture-material: method tables out, canon stays with lore (`bathing-and-body-hygiene.md` §12; `agrarian-field-system-lexicon.md` §12). | This round fills the gap. Do not invent a sibling owner to cite. | n/a — this lane writes the entry. |

## One-way handoff boundary (lore-facing section)

Direction is kotodama → lore only. Lore does not write the entry, the registry rows, or the contract. Kotodama does not write lore canon, `sources.json`, or a bible receipt.

The lore-facing section of `corpus/knowledge/culture-material/scent-perfume-aromatics-codes.md` is a **negative-census stub plus a pointer**, not a second contract and not a content bridge:

1. State the sibling census above (0 word-boundary register owners; literal `scent` hits are `descent` / icon names). That sentence is what stops a later seat from promoting Inana's descent or `md-scent` into prior art.
2. Name the recipient `lore-shokunin`, contract id `kotodama-lore-adjacency`, revision `1.0.0`, path `corpus/knowledge/synthesis/worldbible-integration-contract.md`. Do not paste the contract. Contract `:13` forbids an independently edited mirror.
3. Split the payload on the contract's existing costume/material row (`:197`): kotodama may hand comparative material, process, kit lexicon, wearer/occasion *rules as method*, calibration flags, and open questions. Lore alone decides availability, enforcement, wearers, and canon artifacts.
4. Close with `not canonized`. CM-g is uncovered and the read-acknowledgement is pending, so the section must not say lore accepted, received, or canonized anything. A missing lore receipt is not a defect in C; inventing one would be.

Does not cross: S777–S800 (kotodama registry only; each cited once by the entry), chousa gate logs, kotoba skill text, tsukuroi revision-binding, any path under `lore-shokunin/corpus/fixtures/`. A `(to-verify)` source hole may *name* chousa as the method owner. It does not become a chousa record inside this entry.

## Proposed move

Put that four-point stub in the entry's lore-facing section and nowhere else. Do not open registry rows against sibling paths. Do not retarget O at tsukuroi's tool.

Improves **adjacency**: the false-owner trap (49 literal hits) is recorded and refused, and the handoff uses the contract that already exists instead of a new cross-lane copy. Does not harm **coverage**: C's premise stays “unowned at the base”; the 24 mined rows stay kotodama rows used by the entry once each. Does not harm **operability**: separability remains `tools/check-claim-separability.py` with its own budget flags.

## Risks

- Re-running the prescribed grep *without* a word boundary and treating the 49 paths as owners collapses C's unowned-register premise and drags lore's myth cluster into the entry.
- Copying contract §§4–9 field tables into the entry creates the mirror the contract forbids, and a digest drift would look like a second interface.
- Stamping the section “handed off” or “accepted by lore” while CM-g is uncovered is a false receipt. Ca's record legs must not cite such a stamp.
- Calling `tsukuroi-shokunin/tools/check-revision-binding.py` from O couples two lanes' graders. The shared word “separability” is not a shared tool.

## Verification

- Word-boundary grep over the three sibling repos returns only `kotoba-shokunin/.ufo/round-44/evidence/omp-live-18.12.2-strings.txt`; `rg -n 'md-scent' ` on that file shows icon names, not a knowledge entry.
- `grep -rliE 'check-claim-separability|separability' …/*/tools | grep -v kotodama` returns only tsukuroi's revision-binding tool and its pyc.
- After the entry exists: its lore-facing section contains `kotodama-lore-adjacency` and `not canonized`, and contains no `lore-shokunin/corpus/fixtures` path and no `S777`–`S800` row whose source path is outside kotodama.
