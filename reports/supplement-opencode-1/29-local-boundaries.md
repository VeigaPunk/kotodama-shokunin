# 29 — SENTINEL: local gate/assembler trust boundaries (baseline fe34faa)

- **wave:** supplement-opencode-1 (a supplemental OpenCode Go DeepSeek v4.1 Flash swarm,
  NOT a reserved numbered Z.ai round)
- **baseline_revision:** `fe34faaafbe0add59ff68827a0df6c5782a72404` (== lane `HEAD` while this
  report was written). At inspection start the tracked working tree was clean — only untracked
  `reports/` from this batch existed; later in the batch, other workers added uncommitted
  edits to tracked files (`corpus/…`, `examples/culture-d2/components/…`, `tools/assemble-d2.py`)
  and new untracked tools (`tools/replay-frozen.py`, `tools/source-audit-inventory.py`).
  Those were deliberately **not** inspected: every claim in this report pins to `fe34faa`
  byte copies extracted with `git show`.
- **role:** SENTINEL inspection of existing file access, regex handling and frozen-snapshot
  manifests in `tools/gates/*.py` and `tools/assemble-d2.py`. **Author-side evidence only: no
  SHONEN box is marked `[x]` and no rank is promoted by this fragment.**
- **scope discipline:** no configs, credentials, provider calls, installs, or sibling writes.
  All experiments ran on byte copies of `fe34faa` extracted into
  `reports/supplement-opencode-1/scratch/29-local-boundaries/`; the repository was not modified.
  The only file this lane writes is this report.
- **freshness statement:** all commands below were re-executed at write time;
  `checked_at_utc = 2026-10-17T15:42:24Z`.

## 0. Inspected bytes (sha256 at fe34faa)

| artifact | sha256 |
|---|---|
| `corpus/knowledge/verification/gate-frozen-run-standard.md` | `31f589f536a7b763f172302bcd61f91e526405b9ffb4435bd699b3396c482ad8` |
| `tools/assemble-d2.py` | `2a1cbe855c4885c66b9f2cfa36eb658327001a594f688f5a6a3fba03d5ed5e60` |
| `tools/gates/phonology-sanity-gate.py` | `fb05c644cafb0855481beb5d8bc3f619ae688d8b12787e530f01543f85372655` |
| `tools/gates/lexicon-coverage-audit.py` | `63ee4ec6b15188fefa3e997766971d66fe4d7d7bf9eed65cdcdd55f548fe8a80` |
| `tools/gates/myth-consistency-gate.py` | `26d246e9936db4375c31c6eb260545bf55051d11ec00bb1e757458399b1b55c5` |
| `tools/gates/costume-era-consistency-gate.py` | `29a9361c7b96a354c41a3994e3459a951ce0a43425b3984d6506b3e5b3a43f03` |
| `tools/gates/naming-collision-gate.py` | `8c5afb0a5abc8b00a659120e3795586ddce688bd962ccc68f7308f7bf19aa526` |
| `tools/gates/provenance-audit.py` | `4aaea6e98b9776922708692e6e0f38f76ef7323e3c748cbdf82c789eb77e1e7a` |
| `tools/gates/handoff-packet-check.py` | `e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575` |
| `tools/gates/frozen/round-3/MANIFEST.tsv` | `d5337590b343c65b42fd6e55457862fa325c138ad652e59c81b887daf9971399` |

## F1 — CONCRETE: five of seven gate selftests overwrite their committed fixtures in place; tampering those files is silently erased

Writer gates (selftest writes the committed fixture/expected files, then runs):

- `tools/gates/phonology-sanity-gate.py:1220-1225` — `open(FIXTURE_PATH,"w")`,
  `open(EXPECTED_PATH,"w")`
- `tools/gates/myth-consistency-gate.py:1036-1041` — rewrites both; its own message says
  "fixture and expected rewritten under tools/gates/fixtures/" (line 1066)
- `tools/gates/lexicon-coverage-audit.py:1401-1403` — rewrites both, then line 1425
  re-reads its own write and compares it to the same in-code constant (tautology)
- `tools/gates/costume-era-consistency-gate.py:1452-1457` — rewrites both; line 1474 reads
  back its own write
- `tools/gates/provenance-audit.py:406-413` — rewrites the whole `fixtures/provenance/` tree
  and both `.expected` files, then reads its own write (line 431)

Reader gates (selftest reads the committed pair and fails on tamper):

- `tools/gates/naming-collision-gate.py:1584-1596` — reads fixture + `.expected`, asserts
  `set(expected_ids) == set(got)` and `set(FIXTURE_EXPECTED) == set(expected_ids)`
- `tools/gates/handoff-packet-check.py:691-701` — same reader pattern

Experiment (scratch copy; commands run from the scratch tree so no live-tree write here):

```
$ touch -d '2000-01-01' .../fixtures/phonology-sanity-gate.{expected,yml}
$ printf '# TAMPER yml\n' >> .../fixtures/phonology-sanity-gate.yml
$ sha256sum .../fixtures/phonology-sanity-gate.yml
da62988025564a45e23c453c1c13071965726c88731bfce20fef5100be931af9
$ python3 tools/gates/phonology-sanity-gate.py --selftest ; echo exit=$?
selftest: fixture exit 1; 15/15 planted finding IDs present; 26 control cases passed
exit=0
$ stat -c '%n %y' .../fixtures/phonology-sanity-gate.{expected,yml}
... 2026-10-17 12:37:54  (both rewritten)
$ sha256sum .../fixtures/phonology-sanity-gate.yml
96dfa97e87c85a5c52145d6b9aa1b16572b2906b76ee6dee1591290a7ecb7421  (original bytes restored)
```

Same pattern reproduced for `myth`, `lexicon`, `costume`, `provenance` (tampered `.expected`
appended with `# TAMPER-PROBE 29`; every selftest exited 0 and restored the original digest).
**Positive control (the boundary is real):** the same tamper on
`naming-collision-gate.expected` and `handoff-packet-check.expected` fails loudly —
`AssertionError` with the tamper text in the expected-id set, `exit=1`.

Consequences (trust boundary, not style):

1. For the five writer gates, `tools/gates/fixtures/*.{yml,expected}` are **outputs of
   constants embedded in the `.py`**, not pins the selftest reads. Editing them (or losing
   them) changes nothing the battery can detect; they cannot fail a conformance run.
   The `SKILL.md` §Gates "pinned values" column therefore overstates their role for 5/7
   gates — the pin is the script bytes, the fixture is a regenerated artifact.
2. The write is a direct truncating `open(..., "w")` with no temp-file + rename. An
   interrupted run, or two concurrent selftest batteries (plausible in this swarm), can
   leave or read a truncated fixture. I did not manage to force a deterministic torn read;
   recorded as an untested race, the non-atomic write itself is line-cited.
3. Evidence language needs one honest correction: the round-4 lesson
   (`corpus/lessons/round-4-sol-fixes-and-audits.md:8-9`) and LOG round-4 entry cite
   "fixture bytes untouched — no gate was weakened ... (verified `git status` over
   tools/gates/)". Byte equality is **guaranteed** by deterministic regeneration (proved by
   the mtime experiment: bytes came back identical after a rewrite), so `git status` /
   byte comparison cannot witness that a write occurred. The "no gate weakened" half of the
   claim still matches the commit: `git show fe34faa --stat` touches no gate `.py`.

## F2 — CONCRETE: round-3 frozen manifests verify and replay, with one honest exception (provenance stdout pin)

Digest audit of both committed manifests (recompute against `gate_sha256` /
`input_sha256` / `output_sha256`): **all 14 rows × 3 columns = MATCH**, including the
`input_snapshot` byte copies and the committed `.out` files.

Frozen replay (stdlib script, `input_snapshot` as argv, cwd = snapshot root — never the
live input path): all 14 rows reproduce the recorded exit code; 5/7 rows per manifest are
**byte-identical stdout** to the committed `.out` and match `output_sha256`. The exception:

- `provenance-audit` rows (both manifests). Its stdout contains
  `INFO to-verify-count: <path>: ...` and the committed `.out` shows the freeze-time
  **relative invocation path** (`corpus/knowledge/verification/gate-frozen-run-standard.md`).
  Replaying over the snapshot path prints the snapshot path instead, so the stdout digest
  cannot match from the frozen copy alone. Exit code and INFO counts do reproduce.
- Consequence for the planned replay tool: compare **exit + finding/INFO contract**, treat
  `output_sha256` as advisory for these rows (the standard's §4 already says `stdout_sha256`
  is advisory, but the committed TSV has no such column split), or reconstruct the original
  invocation path shape. The round-3 LOG sentence "all seven final commands reproduce exact
  exit codes and output bytes" is true only from the original live paths, not from the
  committed snapshots — worth a one-line calibration note when the round-3 record is next
  amended.
- Also observed: **no committed Python file reads any `MANIFEST.tsv`** (grep over
  `tools/` for `MANIFEST|frozen/|input_sha256|snapshot` yields only the handoff gate's
  unrelated `HO-MANIFEST-DIGEST` finding id). The digests are a record awaiting the replay
  entry point this wave is building; until it lands, nothing re-verifies them.

## F3 — CONCRETE: round-4 frozen outputs carry no manifest, no input snapshots, no digests

`git show fe34faa --stat` adds exactly five files under `tools/gates/frozen/round-4/` and
nothing else: `costume-era-consistency-gate.out` (0 B), `lexicon-coverage-audit.out` (0 B),
`myth-consistency-gate.out` (0 B), `naming-collision-gate.out` (4072 B, 18 FINDING lines),
`phonology-sanity-gate.out` (654 B, 3 FINDING lines). There is no `MANIFEST.tsv`, no
`inputs/` snapshot copies, no `expected.json`, no `freeze.txt` anywhere under `frozen/`.

- The lane SCORECARD operability evidence "sha256-pinned frozen-run manifests" therefore
  holds for round-3 only; round-4 outputs are pinned by git blob hashes alone.
- Three of five round-4 files are zero bytes. Zero bytes is *consistent* with the recorded
  round-4 outcome (myth/costume fixed → clean exit prints nothing), but with no manifest
  the exit code is not recorded for them, so "clean run" and "truncated capture" are
  indistinguishable from the artifacts. No replay of round-4 is possible against a
  committed input copy (the packet is only in the live tree).

## F4 — Trust contract for the planned frozen replay tool (explicit untested limits)

Scanned all manifest path columns (`gate`, `input`, `output`, `input_snapshot`): none
absolute, none containing `..`, and **no symlinks anywhere under `tools/gates/frozen/`**.
That is the current, verified contract — repo-root-relative paths, regular files only.

- **Symlink following is real at the gate boundary:** a gate run over a symlinked argv path
  reads through it (`ln -s` probe → exit 1, 3 FINDING lines). A replay that hashes a
  pathname and later runs the gate over the same pathname has a TOCTOU gap if that path is
  a symlink or is replaced between the two operations. Requirement for the landing tool:
  refuse non-regular snapshot files (`is_symlink()` / `stat` check) or hand the gate the
  exact bytes that were verified.
- **`command` column is data, never code.** Values look executable
  (`python3 tools/gates/phonology-sanity-gate.py examples/culture-d2/packet.d2.yml`) but no
  code at baseline executes them; the replay tool must not either. A scratch copy of a
  manifest is attacker-editable; executing its `command` string would be command injection
  through repo data.
- **No self-pin.** `MANIFEST.tsv` contains no digest of itself; if a manifest row's path
  and recorded hash are both edited, internal digest checks pass. The trust root is the git
  commit, not the digests.
- **Untested limit:** no replay tool exists at `fe34faa`, so the wave's required behavior
  (tamper a scratch input → exit 2 + `snapshot_tampered`, before any gate runs) could not be
  tested here. The implementation lane owns that test; my round-3 audit above is the
  reference input for it (all digests currently match, and replay from snapshots reproduces
  14/14 exits).

## F5 — Code execution and regex surface (mostly negative, with two notes)

- No `shell=True`, `os.system`, `os.exec*`, `eval`, or `exec` anywhere under `tools/`
  (grep result: none). All subprocess sites (`phonology…:1228`, `myth…:1043`,
  `lexicon…:1406`, `handoff…:833-845`) use list-form `[sys.executable, <repo path>, <fixture>]`.
  No command-injection surface found in the existing code.
- **Assembler code-execution boundary:** `tools/assemble-d2.py:73` runs
  `runpy.run_path(tools/gates/costume-era-consistency-gate.py)` — the assembler executes
  that file's top-level code on every invocation. The path is fixed and repo-relative, and
  the packet records `reader_sha256` (visible-in-diff if the reader is swapped), but nothing
  at baseline verifies that pin. Repo write access to the named reader is code execution
  under the assembler — an accepted repo-internal trust boundary worth naming, not a defect
  by itself.
- **Regex catalog (~50 compiled patterns):** all are static string literals or `rf`-strings
  interpolating repo constants (`handoff…:289` `list_key` is a literal; `…:435` interpolates
  the `ETYM_STATUSES` constant; the one numeric interpolation, `lexicon…:755`
  `r"\bB%d\b" % index`, takes an integer loop counter, and its replacement is a callable, not
  a pattern). No pattern is assembled from input; no nested-quantifier (`(a+)+`) construction
  observed in the catalog. Untested limits: no adversarial regex/time test was run, and every
  gate reads the whole input with no size cap (`read_text`/`open().read()` only) — a huge
  packet is an unbounded local read, not a remote surface.
- **Assembler extraction-regex probe (negative):** `TOP_KEY` (`assemble-d2.py:21`) and the
  subset reader both key on column-0 `key:` lines, so they agree by construction. Crafted
  synthetic component with a column-0 duplicate `phonology:` inside a scalar → `ValueError`
  ("expected exactly one top-level 'phonology'") = fail-closed; phantom different-name line
  across a scalar slice produced the same value as the whole-file subset parse. No silent
  mis-slice found in this class. Untested limit: no differential test against a conforming
  YAML parser, and `_scalar` (`costume…:191-212`) handles quoting naively (no `''`
  de-doubling), which is a fidelity limit, not a boundary escape.

## F6 — Freshness rechecks (public sources + local claims)

Per the wave's freshness axis, three public-source rechecks of the entry that governs the
audited artifacts (`corpus/knowledge/verification/gate-frozen-run-standard.md`), plus four
local re-executions. All excerpts were actually retrieved; prohibitions on invented sources
and page numbers observed. The block is embedded here because this lane's unique scope
restricts writes to this one report; if the parent needs it as
`corpus/lessons/supplement-opencode-1/sources/29.json`, that extraction is parent-side.

```json
{
  "wave": "supplement-opencode-1",
  "baseline_revision": "fe34faaafbe0add59ff68827a0df6c5782a72404",
  "entry": "corpus/knowledge/verification/gate-frozen-run-standard.md (governs the audited gates and frozen manifests)",
  "entry_sha256_before": "31f589f536a7b763f172302bcd61f91e526405b9ffb4435bd699b3396c482ad8",
  "checked_at_utc": "2026-10-17T15:42:24Z",
  "audits": [
    {
      "id": "SR-29-01",
      "claim": "KTD-FR-S-0006: NIST (2015) FIPS PUB 180-4 Secure Hash Standard defines the SHA-256 digest construction cited for digest pinning.",
      "entry_locator": "sources KTD-FR-S-0006",
      "source_url": "https://csrc.nist.gov/pubs/fips/180-4/upd1/final",
      "retrieval_status": "retrieved (institutional landing page; the PDF at the cited nvlpubs URL failed to extract in this environment)",
      "source_locator": "csrc.nist.gov FIPS 180-4 page, abstract; Date Published August 2015",
      "source_excerpt": "This standard specifies hash algorithms that can be used to generate digests of messages. The digests are used to detect whether messages have been changed since the digests were generated.",
      "verdict": "supported",
      "basis": "Publication identity (NIST, FIPS 180-4, Secure Hash Standard, 2015) and digest purpose confirmed by the page. The extracted page text does not name SHA-256 itself.",
      "access_limit": "PDF body not retrieved; the SHA-256-specific clause is unconfirmed from the standard text in this environment."
    },
    {
      "id": "SR-29-02",
      "claim": "KTD-FR-S-0008: Reproducible Builds documents deterministic re-execution (bit-identical rebuild by a third party), which makes a recorded verdict re-checkable.",
      "entry_locator": "sources KTD-FR-S-0008",
      "source_url": "https://reproducible-builds.org/docs/definition/",
      "retrieval_status": "retrieved",
      "source_locator": "Definitions page, 'When is a build reproducible?' paragraph",
      "source_excerpt": "A build is reproducible if given the same source code, build environment and build instructions, any party can recreate bit-by-bit identical copies of all specified artifacts.",
      "verdict": "supported",
      "basis": "The definition states third-party bit-identical recreation, matching the entry's use for re-executable verdicts.",
      "access_limit": "none material"
    },
    {
      "id": "SR-29-03",
      "claim": "KTD-FR-S-0009: a full SHA-1 collision was demonstrated (2017), grounding the ban on MD5/SHA-1 pins.",
      "entry_locator": "sources KTD-FR-S-0009",
      "source_url": "https://shattered.io/",
      "retrieval_status": "retrieved",
      "source_locator": "shattered.io front page, first paragraph",
      "source_excerpt": "On 23 February 2017, researchers at CWI Amsterdam and Google showed the world the first real collision for the SHA-1 hash function.",
      "verdict": "supported",
      "basis": "The collision event and its date are confirmed on the project's own site, matching the entry's operative reading.",
      "access_limit": "The CRYPTO 2017 proceedings metadata (pages/DOI) was not retrieved; the site is the project homepage, not the peer-reviewed paper."
    },
    {
      "id": "SR-29-04",
      "claim": "SKILL.md §Gates / round-4 LOG: all seven gate selftests pass (7/7).",
      "entry_locator": "SKILL.md §Gates 'All selftests green, last verified 2026-10-17'",
      "source_url": "git:fe34faa:tools/gates/*.py",
      "retrieval_status": "re-executed (local, scratch copy of fe34faa)",
      "source_locator": "for-loop selftest battery output",
      "source_excerpt": "phonology exit=0; lexicon exit=0; myth exit=0; costume exit=0; naming exit=0; provenance exit=0; handoff exit=0",
      "verdict": "supported",
      "basis": "7/7 exit 0 re-run at write time.",
      "access_limit": "none; note F1: for 5 gates this proves the embedded constants, not the committed fixture bytes."
    },
    {
      "id": "SR-29-05",
      "claim": "SCORECARD operability: 'sha256-pinned frozen-run manifests' evidence.",
      "entry_locator": "SCORECARD.md operability row",
      "source_url": "git:fe34faa:tools/gates/frozen/**/MANIFEST.tsv",
      "retrieval_status": "re-executed (local digest audit + replay)",
      "source_locator": "14 rows x 3 columns recomputed; replay from input_snapshot",
      "source_excerpt": "round-3 + attempt-1: all gate/input/output digests MATCH; 14/14 exit codes reproduce; 5/7 stdout digests per manifest reproduce; provenance stdout does not (invocation path in INFO line)",
      "verdict": "supported (scope-corrected)",
      "basis": "The manifests that exist are internally consistent and replayable; the claim is true of round-3 only — see F3 for the unpinned round-4 outputs.",
      "access_limit": "no replay entry point exists at baseline to test tamper rejection."
    },
    {
      "id": "SR-29-06",
      "claim": "Round-4 lesson/LOG: 'fixture bytes untouched — no gate was weakened ... (verified git status over tools/gates/)'.",
      "entry_locator": "corpus/lessons/round-4-sol-fixes-and-audits.md:8-9; LOG.md round-4 entry",
      "source_url": "git:fe34faa:tools/gates/fixtures + selftest experiment",
      "retrieval_status": "re-executed (local mtime/tamper experiment)",
      "source_locator": "phonology fixture touched to mtime 2000-01-01, tampered, selftest run",
      "source_excerpt": "after --selftest: mtime 2026-10-17 12:37:54, tampered bytes reverted, exit 0; naming/handoff tamper control: AssertionError exit 1",
      "verdict": "contradicted (as evidence)",
      "basis": "Five selftests rewrite the fixture files (non-atomic), and deterministic regeneration guarantees byte equality regardless; git status cannot witness the write. The companion fact 'no gate .py changed in fe34faa' matches git show --stat.",
      "access_limit": "torn-read race not forced; stated as untested."
    },
    {
      "id": "SR-29-07",
      "claim": "Coupling audit (era/dress not bibliography): the costume-era (era <-> dress/material/rank) frozen verdict is reproducible from the committed snapshot.",
      "entry_locator": "tools/gates/frozen/round-3/MANIFEST.tsv, costume-era row",
      "source_url": "git:fe34faa:tools/gates/frozen/round-3/inputs/examples/culture-d2/packet.d2.yml",
      "retrieval_status": "re-executed (local frozen replay)",
      "source_locator": "replay output vs committed costume-era-consistency-gate.out",
      "source_excerpt": "exit=1 (want 1); stdout sha256 equals recorded output_sha256 129c4f5a...; 10 G-ERA findings on era/dress tags",
      "verdict": "supported",
      "basis": "The era/dress coupling verdict re-executes byte-identically from the frozen input, not only the isolated pipeline.",
      "access_limit": "none; the coupling itself is a design judgment, not validated here."
    }
  ]
}
```

## Untested limits carried forward (explicit)

1. No replay tool exists at `fe34faa`; its required tamper rejection (exit 2,
   `snapshot_tampered`) and its path-validation choices (symlink/traversal refusal) are
   untested until the implementation lane lands. (During this batch an untracked
   `tools/replay-frozen.py` appeared in the worktree; it was outside my baseline scope and
   was **not** inspected or tested here — its own report/owner carries that evidence.)
2. Concurrent selftest runs of the same gate can interleave truncating writes on the same
   fixture paths; the race was not forced.
3. No adversarial regex or input-size testing; no differential parse test against a
   conforming YAML parser.
4. The provenance `output_sha256` rows cannot be reproduced from the frozen copies without
   reconstructing the original invocation path.
5. Round-4 frozen outputs have no recoverable exit codes or input copies; no replay is
   possible for them from committed bytes alone.

## Handoff notes

- Corrections the parent may integrate into lane records (I did not write them, per batch
  rules): F1's fixture-pin wording (SKILL.md §Gates pinned-values column and round-4
  lesson line), F2's "reproduce exact output bytes" phrasing, F3's SCORECARD scope.
- Independently of my run, sibling fragments `01-plan-review.md`, `23-myth-coverage.md` and
  `31-promotion-readiness.md` (untracked during my inspection) reach related observations
  about the round-4 manifest gap; this fragment's evidence is independent (scratch copies,
  fresh commands).
- Scratch artifacts remain at
  `reports/supplement-opencode-1/scratch/29-local-boundaries/` (baseline copies,
  `audit-manifest.py`, `exp-selftest/`, `exp-asm/`) as the re-runnable evidence trail.
