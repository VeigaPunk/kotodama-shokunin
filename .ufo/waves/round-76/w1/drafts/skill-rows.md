# Round-76 gate-registry rows — DRAFT (stage only, not installed)

Seat `ScribeSkillRows` (round 76 / hyaku run 10 / wave 1). Lane `kotodama-shokunin`, base
`98c486bdb4650ba5b8e651d332910e8ee60ad121`. Everything below is a DRAFT for the L1 to install at the
freeze; no lane, fleet or shokuknow byte was written by this seat.

Read for this draft: `.ufo/waves/round-76/CLAIMS-DRAFT.md`; `.ufo/waves/round-75/skill-rows.md`;
`SKILL.md` gate table (:648 header, :707-:708 the round-75 rows, :709 the round-73 correction note);
`SHONEN.md:6`; `reports/round-75/accept-c.py` + `reports/round-75/accept-ca.py`;
`.ufo/waves/round-76/w1/spec.json` items `ExecAdaptC` / `ExecAdaptCa` (the counter contracts).

## 0. Install gate — what is contract and what is unmeasured

The round-76 counters do not exist yet (`git ls-tree 98c486b reports/round-76/` prints nothing;
the working tree holds only `reports/round-76/telemetry/census-start.txt`). The rows below are therefore
written from the counter *contract*, and every token in the table below is either contract-derived (the
landed counter must match it or the counter is wrong) or inherited from round 75 and still to be
re-confirmed against the landed bytes.

| token in the row | source | status |
|---|---|---|
| `ACCEPT-C-76` / `ACCEPT-CA-76` | `spec.json` → `ExecAdaptC` / `ExecAdaptCa` | contract |
| `legs=13` (C) / `legs=12` (Ca) | draft claim C (13-leg table kept, leg names listed verbatim) and claim Ca (`legs[12]`) | contract; self-enforcing — a wrong table is refused by the counter's own LEGCOUNT against the frozen `claims.json` |
| `--combined <C-lands>` required; missing flag = REFUSAL exit 2 | `ExecAdaptCa`: "make a missing flag a REFUSAL (exit 2) not a leg FAIL that reads as a red claim" | contract (round-75 behaviour was the opposite: leg FAIL `11/12`) |
| `--work` / `$TMPDIR` / `$HYAKU_SCRATCH`, no literal `/tmp` | `ExecAdaptC`/`ExecAdaptCa` prompt §7.4; draft claim Ca ("routed defect") | contract — with one tension to reconcile at landing: honouring `$TMPDIR` and refusing "the system temporary directory" collide when `$TMPDIR` is unset (round-75 `accept-c.py:6021-6028` bans `tempfile.gettempdir()` itself). The rows say `/tmp`, not "whatever `$TMPDIR` names"; the landed counter must do the same or the row changes |
| pinned local `main` for the `# measured revision (lane main)` header | `reports/round-75/accept-ca.py:2736-2747`; routed by `.ufo/waves/round-75/w3/…` (spotcheck item 2) | inherited; re-confirm at landing |
| the refusal/ERROR enumerations in the verdict cells | round-75 rows (`skill-rows.md:1-2`) + `accept-c.py:6089-6111`, `accept-ca.py:2669-2719`, `:2806` | inherited; re-confirm at landing |
| selftest count and counter sha256 | only knowable after landing | `<AT-INSTALL: …>` placeholders; fill from the receipt, never from a pre-freeze run |

Round-75's own lesson (`corpus/lessons/round-75.md:463`, F1) is exactly the failure mode a pre-freeze
selftest stamp causes. The `:707` repair below is the correction of that instance; the `<AT-INSTALL>`
placeholders keep round 76 from repeating it.

## 1. SKILL.md — two new rows

Placement: into the gate/probe registry whose header is `SKILL.md:648`
(`| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |`),
immediately after the `accept-ca-75` row (`:708`) and before the `accept-c-73 / accept-ca-73 correction`
note row (`:709`), so rounds stay in ascending order. Eight cells each, single line each.

```
| accept-c-76 | gate | `python3 -B reports/round-76/accept-c.py --root . --lands <40-hex> --freeze <40-hex> [--fleet-root /home/vgpnk/Projects/shokunin] [--work <dir>]` (`--work` wins, else `$HYAKU_SCRATCH/kotodama-r76/counter`, else `$TMPDIR` only when it is not the system temporary directory; a root inside `/tmp` is refused with the counter's own token `QUALITY 14 / prompt §7.4`) | Output ends `ACCEPT-C-76: PASS legs=13/13` (exit 0) or `: FAIL legs=<n>/13` (exit 1, n = passing legs), after one `LEG PASS` or `LEG FAIL` line per leg. A refusal prints `ACCEPT-C-76: FAIL legs=0/13 (refused: …)` and exits 2: `--lands` equal to the frozen claims base, an unreadable or malformed frozen `claims.json`, a frozen leg table that is not exactly the thirteen implemented legs (LEGCOUNT), a map whose sha256 differs from the frozen pin, or a scratch root inside the system temporary directory (`/tmp`). `--lands == --freeze` is graded, not refused (data legs red, FROZENCFG green). Input errors print `ERROR: …` on stderr, exit 2 (missing or non-40-hex `--lands` or `--freeze`; `--root` without `.git`; a frozen base that is not a commit). | `python3 -B reports/round-76/accept-c.py --selftest` — one `CASE <name>: PASS` or `CASE <name>: FAIL` line per case, ends `SELFTEST: <p>/<n>`; measured at the landing commit (counter sha256 <AT-INSTALL: `sha256sum reports/round-76/accept-c.py`>): `<AT-INSTALL: SELFTEST: p/n>`, exit 0 (clean landing 13/13, one single-edit mutant per leg red on its named leg, lands==base refused, lands==freeze graded; receipt `reports/round-76/telemetry/selftest-c.txt`). | frozen claim C leg set (13: ENTRIES, ROWS, REPOINTED, GATE, EVIDENCE, REJECTS, GROUND, CITEDLINES, CENSUS, SCRATCHMIRROR, COLLCHECK, FROZENCFG, INDEX); constants read at `--freeze`; entries declared as `candidates[]` with `min_admitted: 2` over the four staged paths, one registry row per distinct document; GROUND sweeps `GB/T 33661` and `digital.archives.go.jp` (absent at base `98c486b`, present in at least one admitted entry); registry rows 817 -> 817+k; `lands == base` refused; by-document citation map hash-pinned in the frozen claims | read-only — clone plus `git archive` materialized under `<--work>` (default `$HYAKU_SCRATCH/kotodama-r76/counter`, else a non-`/tmp` `$TMPDIR`); the fleet census script is executed, never written; nothing under a literal `/tmp` | kotodama-shokunin |
| accept-ca-76 | gate | `python3 -B reports/round-76/accept-ca.py --root . --lands <40-hex> --freeze <40-hex> --fleet-root /home/vgpnk/Projects/shokunin --combined <C-lands 40-hex> [--main main] [--work <dir>]` — the FULL measuring command: `--combined` is required (the COMBINED leg re-evaluates APPENDONLY at the tree carrying both landings) and the lane's local `main` MUST be pinned to the `--lands` revision (`git branch -f main <lands>`, or `--main` names a ref that resolves to it) so the `# measured revision (lane main)` header equals `--lands` | Output ends `ACCEPT-CA-76: PASS legs=12/12` (exit 0) or `: FAIL legs=<n>/12` (exit 1, n = passing legs), after one `LEG PASS` or `LEG FAIL` line per leg. A refusal prints `ACCEPT-CA-76: FAIL legs=0/12 (refused: …)` and exits 2: a frozen leg table that is not exactly the twelve implemented legs (LEGCOUNT), `--lands` equal to the frozen claims base, `freeze == lands` with every leg green, a missing or non-40-hex `--combined` (round 76 raises round 75's leg FAIL to a refusal), or a scratch root inside the system temporary directory (`/tmp`). Input errors print `ERROR: …` on stderr, no verdict line, exit 2: missing `--lands`, `--freeze` or `--fleet-root`; a non-40-hex `--lands`, `--freeze` or `--combined`; a `--fleet-root` that is not a directory; an absent `--lands`, `--freeze` or `--combined` commit; an unreadable frozen `claims.json`; a frozen base that is not a commit. A `--freeze` off the lands first-parent chain is a leg FAIL (FROZENCFG), not a refusal. | `python3 -B reports/round-76/accept-ca.py --selftest` — the green form prints `SELFTEST OK: <n> checks across <m> scenarios reported-fail=0: <labels>` then `SELFTEST: <n>/<n>`, exit 0; measured at the landing commit (counter sha256 <AT-INSTALL: `sha256sum reports/round-76/accept-ca.py`>): `<AT-INSTALL: SELFTEST: n/n>`, receipt `reports/round-76/telemetry/selftest-ca.txt`. | frozen pair floor 10; twelve legs (LEDGER, BASEMISMATCH, REPAIR, ANNOTATE, APPENDONLY, R1EXEMPT, NOSTUB, SEPARABLE, RECEIPTS, COMBINED, FROZENCFG, STAMP); nine-executable observe allowlist git, grep, wc, sha256sum, ls, cat, head, tail, cut; claims and ledger read at `--freeze` only; ledger `reports/round-76/ledger.json`; ANNOTATE rows under `## Corrections — round 76` in `SCORECARD.md`; `--main` defaults to `main`; the round-75 lands/freeze pair for RECEIPTS read from the frozen claims | read-only — `git show` plus `git archive`/clone materialized under `<--work>` (default `$HYAKU_SCRATCH/kotodama-r76/counter`, else a non-`/tmp` `$TMPDIR`); `observe_cmd` argv only, never a shell; nothing under a literal `/tmp` | kotodama-shokunin |
```

## 2. SHONEN.md:6 — registry summary edit text

Current line 6 (`sed -n '6p' SHONEN.md`, single line, 643 characters) carries the round-75 summary:

```text
  asserted: `SKILL.md:20` (Decision table), `:505` (Error patterns), `:564` (Checklist); sources registered in `corpus/SOURCES.md` (Registry counts at round 75 Ca landing — rows: 808, mined: 713, queued: 58, rejected: 37; census exit 0 in `reports/round-75/telemetry/census-start.txt`; the coverage landing updates the close counts to 817 rows / 722 mined / 58 queued / 37 rejected, re-derived at `reports/round-75/telemetry/census-end.txt`); no non-author verifier on record.
```

The four numbers that stay true at base (measured — see §4): 817 rows, 722 mined, 58 queued, 37 rejected;
`reports/round-76/telemetry/census-start.txt` ends `exit=0`. Round 76 changes only the round label and the
after-state, because claim C adds rows and claim Ca adds none.

Proposed replacement of the parenthetical (byte-level `str.replace` on the exact text above; leave the
`asserted:` prefix, the pointers sentence and the rest of the line untouched):

```text
(Registry counts at round 76 Ca landing — rows: 817, mined: 722, queued: 58, rejected: 37; census exit 0 in `reports/round-76/telemetry/census-start.txt`; the round-76 coverage landing updates the close counts to 817+k rows / 722+k mined [k = distinct documents newly cited by the n>=2 admitted candidate entries, k>=1], 58 queued / 37 rejected unchanged, re-derived at `reports/round-76/telemetry/census-end.txt`)
```

**Conditional — append-only compatibility.** `accept-ca-76`'s APPENDONLY leg accepts a changed line only
when it is a REPAIR pair's `stated_at` line or an appended line (`accept-ca.py:51-60`, leg text "every
changed line elsewhere is a REPAIR pair's stated_at line or an appended line"). So:

1. If `reports/round-76/ledger.json` (frozen) carries a REPAIR pair with `stated_at.path: SHONEN.md` and
   line 6, apply that pair's `statement_after` **byte for byte** instead of the sentence above; the pair's
   observed token must be one of the four numbers or the round label. Only one edit to the line.
2. If no such pair exists, do **not** rewrite line 6 in place — append a new line after it:

```text
  round 76 registry after-state: rows 817+k / mined 722+k (k = distinct documents newly cited by the n>=2 admitted candidate entries), queued 58 / rejected 37 unchanged; re-derived at `reports/round-76/telemetry/census-end.txt`.
```

Both forms keep the submitted claim C declaration ("registry rows 817 -> 817+k") in front of a reader of
the promotion checklist, and both are inside what the frozen legs grade.

## 3. SKILL.md:707 — repair of the pre-freeze sha defect

**Which is which** (both verified in §4):

- `315c5f3f27fd36b7ee92cb5bff9c34c27a5013e28218d9481ee7f74b5c7ce261` — the sha256 of the **committed**
  `reports/round-75/accept-c.py`. Identical in three ways: the working-tree file, the only blob that ever
  existed at that path (one revision, `11d4413e`), and a fresh reassembly from
  `.ufo/waves/round-75/w2/parts/*.py` through `.ufo/waves/round-75/w2/assemble.sh` (byte-identical to the
  committed file).
- `fa5060b91bdb6e76947aa7a0daab6d037b40a3be9f978e257783c7180c314d3f` — the **pre-freeze stamp** written
  `reports/round-75/telemetry/selftest-c.txt:2` (`# counter sha256 fa5060b9…`, line 1 says "run from
  the lane, 2026-10-27, before the freeze"). No file in the lane working tree hashes to it, and the path
  had only the one committed blob. The 64-hex token occurs as text in exactly one pre-existing file (that
  receipt; `SKILL.md:707` carries only the abbreviation `fa5060b91bdb…`, as do the round-75 wave reports).
  So `SKILL.md:707` cites bytes that exist in no commit.

**Repair** — replace this unique substring in `SKILL.md:707` (self-test cell; `old` verified present
exactly once, `line.count(old) == 1`):

old:

```text
Measured 2026-10-27 at counter sha256 `fa5060b91bdb…`: `SELFTEST: 85/85`, exit 0 (clean landing 13/13, 78 single-edit mutants each red on its named leg, lands==base refused, lands==freeze graded; receipt `reports/round-75/telemetry/selftest-c.txt`).
```

new:

```text
Measured 2026-10-27 at counter sha256 `315c5f3f27fd…`: `SELFTEST: 85/85`, exit 0 (clean landing 13/13, 78 single-edit mutants each red on its named leg, lands==base refused, lands==freeze graded); re-run at the landed bytes reproduces 85/85 with the same stamp (`.ufo/waves/round-75/w3/ExecRerunBoth.md` §3), while the committed receipt `reports/round-75/telemetry/selftest-c.txt` still carries the pre-freeze `fa5060b9…`, which names no byte in the repository.
```

The count (`85/85`) is the one already in the row; it was re-measured at the landed bytes by
`ExecRerunBoth.md` §3 ("`accept-c.py --selftest` → `SELFTEST: 85/85`, exit 0 … it reports `315c5f3f…ce261`,
the frozen hash"). **This seat did not re-run the selftest** (scribe discipline: no re-run to decorate a
report), so the sentence cites that receipt rather than claiming a fresh measurement.

Same conditional as §2: if the frozen ledger carries a REPAIR pair on `SKILL.md:707`, take its
`statement_after` verbatim (the observed token it must carry is `315c5f3f…`, not `fa5060b9…`). The
receipt is a round-75 artifact and is never edited; if the L1 wants the receipt stamped too, that is an
ANNOTATE row under `## Corrections — round 76` in `SCORECARD.md`, not a rewrite of round-75 evidence.

## 4. Evidence for the numbers in this draft

All run in the lane at base `98c486bdb4650ba5b8e651d332910e8ee60ad121`; scratch under
`/fast/scratch/hyaku/kotodama-r76/ScribeSkillRows/` (deleted before yield).

```text
$ sha256sum reports/round-75/accept-c.py reports/round-75/accept-ca.py
315c5f3f27fd36b7ee92cb5bff9c34c27a5013e28218d9481ee7f74b5c7ce261  reports/round-75/accept-c.py
98d8e7974c82d048db67fe8eebd06cd78308bc0e3233c922ec16f527fd1ac235  reports/round-75/accept-ca.py

$ git show 98c486b:reports/round-75/accept-c.py | sha256sum
315c5f3f27fd36b7ee92cb5bff9c34c27a5013e28218d9481ee7f74b5c7ce261  -

$ git show 98c486b:reports/round-75/accept-ca.py | sha256sum
98d8e7974c82d048db67fe8eebd06cd78308bc0e3233c922ec16f527fd1ac235  -

$ for rev in $(git rev-list --all -- reports/round-75/accept-c.py); do printf '%s %s\n' "$rev" "$(git show $rev:reports/round-75/accept-c.py | sha256sum | cut -d' ' -f1)"; done | sort -u -k2
11d4413e77394f3857d7c6196dd508dd9e9728a3 315c5f3f27fd36b7ee92cb5bff9c34c27a5013e28218d9481ee7f74b5c7ce261

$ sh .ufo/waves/round-75/w2/assemble.sh /fast/scratch/.../assembled-c.py && sha256sum …/assembled-c.py
315c5f3f27fd36b7ee92cb5bff9c34c27a5013e28218d9481ee7f74b5c7ce261  …/assembled-c.py
$ cmp -s …/assembled-c.py reports/round-75/accept-c.py && echo IDENTICAL_TO_COMMITTED
IDENTICAL_TO_COMMITTED

$ sed -n '1,2p' reports/round-75/telemetry/selftest-c.txt
# selftest-c.txt — python3 -B reports/round-75/accept-c.py --selftest (run from the lane, 2026-10-27, before the freeze)
# counter sha256 fa5060b91bdb6e76947aa7a0daab6d037b40a3be9f978e257783c7180c314d3f

$ find . -path ./.git -prune -o -type f -print0 | xargs -0 sha256sum 2>/dev/null | grep -c '^fa5060b91bdb'
0

$ grep -rl 'fa5060b91bdb6e76947aa7a0daab6d037b40a3be9f978e257783c7180c314d3f' . --exclude-dir=.git
./reports/round-75/telemetry/selftest-c.txt
./.ufo/waves/round-76/w1/drafts/skill-rows.md      # this draft quotes it; it is the only other hit

$ grep -rc 'fa5060b9' SKILL.md reports/round-75/telemetry/selftest-c.txt
SKILL.md:1
reports/round-75/telemetry/selftest-c.txt:1

$ git show 98c486b:corpus/SOURCES.md | grep -cE '^ {0,3}\|[[:space:]]*S[0-9]{3,}[[:space:]]*\|'
817
$ for st in mined queued rejected; do printf '%s %s\n' "$st" "$(git show 98c486b:corpus/SOURCES.md | grep -cE "\|[[:space:]]*$st[[:space:]]*\|")"; done
mined 722
queued 58
rejected 37
$ git ls-tree -r --name-only 98c486b corpus/knowledge | grep -c '\.md$'
252
$ tail -1 reports/round-76/telemetry/census-start.txt
exit=0

$ git show 98c486b:SKILL.md | sed -n '648p'
| name | kind | entry command | verdict map | self-test | pinned values | write scope | owner |
$ git -C … grep -n 'accept-c-75\|accept-ca-75' 98c486b -- SKILL.md
98c486b…:SKILL.md:707: … ; 98c486b…:SKILL.md:708: …
```

## 5. Checks the L1 must run at install (not run by this seat)

1. `grep -c '^| accept-c-76 | gate |' SKILL.md` → 1 and `grep -c '^| accept-ca-76 | gate |' SKILL.md` → 1.
2. Eight cells per new row: `awk -F' \\| ' '/^\| accept-c-76 \|/{print NF}' SKILL.md` → 8 (same for ca).
3. `python3 -B reports/round-76/accept-c.py --selftest` and `…accept-ca.py --selftest` at the landed bytes;
   paste the verdict and `sha256sum` into the `<AT-INSTALL>` slots (§1) and into the receipt names.
4. `grep -nE '"/tmp|/tmp/' reports/round-76/accept-c.py reports/round-76/accept-ca.py` → no match.
5. The graded Ca command as written in the row (§1, cell 3) must reproduce `ACCEPT-CA-76: PASS legs=12/12`
   with the local `main` pinned to the Ca lands and `--combined` the C lands; and the same command with
   `--combined` dropped must print `legs=0/12 (refused: …)` exit 2.
6. `SHONEN.md:6` after-state: the four regeneration commands in §4 print `817+k`, `722+k`, `58`, `37`
   at the lands revision.
7. Decide §2 and §3 against the frozen `reports/round-76/ledger.json` (REPAIR pair present → use its
   `statement_after`; absent → append-only form).
