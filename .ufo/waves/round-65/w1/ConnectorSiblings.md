# ConnectorSiblings — round 65, claim C: sibling overlap and one-way lore handoff

Seat: `kotodama-r65.ConnectorSiblings` (leaf; no delegation). Lane: kotodama-shokunin, base `17c32302c6845c8f164b985a8cb312d3181c8788`. Read-only over sibling lanes. No production file edited. No git/jj write. **No tool installed or updated.** Draft advice for L1; not admission.

Axes named: **coverage** (who owns the games register), **operability** (which reopen/fragment tool is whose), **calibration** (handoff honest about pending lore intake). A move is kept only if it improves one and harms none.

## Evidence

### Assigned sweeps (exercised this seat)

1. `grep -rliE 'mancala|senet|astragal|tug.of.war|hnefatafl|patolli|kubb'` over `lore-shokunin`, `chousa-shokunin`, `kotoba-shokunin`.

   Three hits, all under `.ufo`, all false tokens:

   | File | Token | What it actually is |
   |---|---|---|
   | `lore-shokunin/.ufo/interactive-sessions/20261015T050057Z/…855.jsonl:223` | `KUBb` | base64 blob inside a session tool-call |
   | same session `__advisor.jsonl:102` | `KUBb` | same class |
   | `chousa-shokunin/.ufo/waves/round-35/w2/ScoutManBash/bash.1:13440` | `senet` | substring of bash man page "the Usenet" |
   | `kotoba-shokunin/.ufo/round-44/evidence/omp-live-18.12.2-strings.txt` | `senet`, `kubb` | substrings inside an omp binary strings dump (`usenetwork`, base64) |

   Repeat with `--exclude-dir=.ufo --exclude-dir=.git`: **(none)**. lore `corpus/`, chousa `corpus/`, and kotoba durable tree: zero matches for those tokens and zero matches for `games-play|games register|sport-contest|S750`.

2. `grep -rliE 'check-row-fragments|reopen-row' /home/vgpnk/Projects/shokunin/*/tools | grep -v kotodama`: **(none)**. Those two names exist only under `kotodama-shokunin/tools/`.

### Who owns what (tools)

Confirmed nearest prior art: `chousa-shokunin/tools/quote-reopen.py` (556 lines, shebang, docstring at lines 1–33). It is real. It is **not** a drop-in for either kotodama tool.

| Surface | Owner | Contract (from the file head) | Not this |
|---|---|---|---|
| `chousa-shokunin/tools/quote-reopen.py` | chousa | `verify --items` TSV `id source_id quote`; default registry `corpus/SOURCES.md` of the **chousa** lane; verdicts `NO_SOURCE / TOO_LONG / UNREACHABLE / VERBATIM / ABSENT`; `MAX_WORDS = 25`; summary `QUOTE_REOPEN_SUMMARY`; exit 0 only if every item is `VERBATIM` | not a markdown-row scanner; not caption-vs-body; not teaches-length; not query-aware URL identity |
| `kotodama-shokunin/tools/reopen-row.py` | kotodama | row ids against a markdown `\| Snnn \|` table; verdicts include `LOCATED`, `CAPTION_ONLY`, `ABSENT`, `TRUNCATED`, `REFUSED`, `NO_QUOTE`; NFKC+casefold whole-word run; body vs caption split | not chousa's items-TSV verbatim gate |
| `kotodama-shokunin/tools/check-row-fragments.py` | kotodama | round-65 pre-integration fragment checker; `TEACHES_MAX = 240`; `norm_url` drops query and fragment; findings `teaches-length`, `dup-url`, `capture-url-mismatch`; pinned `ENTRY = …/games-play-sport-contests.md` | not a live-page reopener at all |

Sibling `tools/` directories that exist and do **not** contain those strings: chousa (above), kaidoku, kama, mado, mori, souji, tameshi, tsukuroi. lore and kotoba have no `tools/` directory on this sweep (kotoba instruments live under `verifiers/`, prompt-craft only).

Contradiction, stated not scored: the shared verb "reopen a quote against a registry URL" makes `quote-reopen.py` the nearest prior art, and the verdict algebras are incompatible. Substituting one for the other would false-stamp both C (quote support) and O (the frozen `FRAG` / `RESTATE` counters). `check-row-fragments.py` shares neither the verb nor the input shape with `quote-reopen.py`; calling it prior art for the fragment checker would be the smoothing this seat refuses.

### Games register: adjacency, not ownership

No sibling owns a culture-material games / play / sport / contests **register entry**. Claim C's own frozen statement (`reports/round-65/claims.json` C) already records 0 filename owners inside kotodama `corpus/knowledge` at base `17c32302`. Outside that lane:

| Lane | What the filename or province actually owns | Absorb? |
|---|---|---|
| lore-shokunin | fictional-world records (`PROVINCE.md:3`); refuses game-mechanics verification (`:9`); CM-g kotodama packet intake stays `uncovered` (`:19`) | no — recipient of canon decisions, not a register author |
| chousa-shokunin | research method: question framing, source hierarchy, claim-vs-source (`PROVINCE.md:3-8`); "Out of province → report, never absorb." (`:17`) | no |
| kotoba-shokunin | prompt and skill craft (`PROVINCE.md:3-6`) | no |
| game-dev-2d-shokunin | 2D production verified by headless fixtures (`PROVINCE.md:3`); refuses narrative canon (`:10`). Durable `*game*` hits are pygame probes/batteries, not a register | report only |
| game-dev-3d-shokunin | 3D production fixtures (`PROVINCE.md:3-6`); same canon refusal | report only |
| audio-shokunin | `corpus/knowledge/2026-10-19-game-loudness-whole-mix-protocol.md` — whole-mix LKFS/LUFS targets (ASWG, EBU R 128, BS.1770), not play/sport ethnography | report only |
| kaidoku-shokunin | `*replay*` filenames are toolchain replays (`swiss-map-replay`, `go125-toolchain-replay`), not games of contest | do not cite as a games owner |

The assigned three-lane token sweep does not see game-dev or audio. Those rows are adjacency from a filename pass outside `.ufo`, not an invitation to import their text.

A later fleet `find` for `quote-reopen.py` and for names matching `*fragment*` / `*reopen*` does not add an owner. The only durable script is `chousa-shokunin/tools/quote-reopen.py`. Copies under `chousa-shokunin/.ufo/waves/round-29/` and `round-30/build/` are that lane's own wave drafts. Other hits are name collisions, not `check-row-fragments` or `reopen-row`: kaidoku `source-reopen/` notes, kake URL-fragment fixtures, kama grid fragments, kumitate reopen logs, kagi `caniuse` media-fragments, game-dev-2d `r102-E3-m3_fragment_mutation.sh`, audio `r97b-cell-B3_no_fragment`. `kengaku-shokunin/corpus/evidence/round28-calibration/prior-art-reopen.txt` is an evaluation-calibration access note (OpenAI SWE-bench quotes, 21 and 22 words), not a games register and not a quote tool.

## One-way handoff boundary (lore-facing section)

Model already in force: `corpus/knowledge/culture-material/hunting-foraging-subsistence.md:205` — the entry owns a comparative register, decides nothing about any world, and names lore as the owner of in-world existence. Contract: `corpus/knowledge/synthesis/worldbible-integration-contract.md:4` (lore owns canon, chousa owns research method), `:18-19` (a receipt does not delegate canon), `:68` (do not invent a sibling path or tool), `:189-203` (handoff drill, not canon), `:209` (kotodama proposes; lore selects). Lore's own map: `lore-shokunin/PROVINCE.md:28` (packet intake; digest unacknowledged; CM-g).

Boundary for `## lore handoff` of `games-play-sport-contests.md`. One direction only. C's lands are the entry, `corpus/SOURCES.md`, and `corpus/README.md` (`claims.json` C.lands). No sibling file is edited.

1. **Kotodama owns** the comparative register: classification (chance / physical / skill and the round's game classes), source-grounded mechanism, calibration, and the S750–S775 rows. It does not own which games exist in-world, who may play, what stakes are real, or which contests are sacred.
2. **Lore owns** those canon decisions, and only once a reviewed packet is accepted on lore's own surfaces. This round the packet is a **candidate**. CM-g is uncovered and the contract digest is unacknowledged (`PROVINCE.md:19,28`). Do not write "lore will record" or "lore accepts".
3. **Chousa owns** research method and `quote-reopen.py`. The entry does not cite that tool as having verified S750–S775, and it does not hand the tool across. Quote support for these rows stays on kotodama's `reopen-row.py` and the frozen accept-c legs.
4. **game-dev-2d / game-dev-3d own** executable mechanics. A rule for how a contest is played in fiction is not a pygame fixture and is not imported from one. audio owns loudness measurement, not the register.
5. **No reciprocal edit and no invented path.** Do not add a games row to lore, chousa, kotoba, or game-dev. Do not name a sibling games-register path: none exists. The only sibling tool this seat confirms as prior art is `chousa-shokunin/tools/quote-reopen.py`, and it stays on that lane.

## Proposed move (one)

In the entry's final lore-facing section, three sentences and no tool citation:

(i) fleet sweep of lore, chousa, and kotoba shows 0 durable owners of mancala / senet / astragal / tug-of-war / hnefatafl / patolli / kubb, and 0 sibling `tools/` hits for `check-row-fragments` or `reopen-row`; nearest prior art `quote-reopen.py` is chousa's items-TSV verbatim gate and is not a verifier of this entry;

(ii) lore-shokunin owns which contests exist in-world, who plays, and which stakes are real, but CM-g intake is uncovered, so this section is a candidate method handoff naming the recipient and the open questions, not an import;

(iii) game-dev-2d/3d (mechanics fixtures) and audio (whole-mix loudness) are adjacent and are not absorbed.

That improves coverage (no false sibling owner) and calibration (pending intake stated) and leaves operability untouched: O's lands stay `accept-*.py` and `tools/check-row-fragments.py`.

## Risks

- A later seat treats `quote-reopen.py`'s 25-word `TOO_LONG` as the same rule as accept-c `RESTATE` (≥80% in-order token coverage of the teaches cell) or as `check-row-fragments.py`'s 240-char teaches cap. They are three different counters. The handoff must not cite the chousa tool.
- Filename greps for `game` will surface pygame batteries and the audio loudness protocol. Those are not register entries; citing them as partial owners would invent a coupling.
- Writing the handoff as if lore had acknowledged the contract digest would contradict `PROVINCE.md:19` and `worldbible-integration-contract.md:15` (bilateral acknowledgement pending). That harms calibration.
- C.lands does not include any sibling path. A "helpful" edit to lore or to `quote-reopen.py` would be a new claim and would break separability (`claims.json` separability note: accept-c does not read O/Ca lands; it also must not start reading chousa).

## Verification

Exercised here: both assigned greps; the `.ufo`-excluded repeat; `test -f` + line count of `quote-reopen.py`; heads of `quote-reopen.py`, `reopen-row.py`, `check-row-fragments.py`; `PROVINCE.md` lines cited above; contract `:4,18-19,68,189-209`; hunting entry `:205`; `claims.json` C.lands. Not run: accept-c/o/ca, fragment selftest, live URL reopen (other seats). L1, after the entry exists, should check that `## lore handoff` names lore as recipient, says candidate/uncovered, and does not mention `quote-reopen.py`, `reopen-row.py`, or `check-row-fragments.py`.
