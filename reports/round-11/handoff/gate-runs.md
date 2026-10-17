# R11-O10..O11 — gate runs over the assembled handoff packets (isolated copies)

- seat: HANDOFF R11-O10..O11 (gate runs), round 11 (loop 1 of 3, build round 4 of 4), claim O
  (operability), 2026-10-17, observation window 22:03–22:21Z (19:03–19:21 local, UTC−3),
  worktree HEAD `e3ef171`.
- assignment (verbatim): "run tools/gates/handoff-packet-check.py over each assembled packet in
  an isolated copy; record verdicts; reports/round-11/handoff/gate-runs.md."
- files written: **this file only** (plus gitignored scratch under `.scratch/r11-o10/`, which
  holds the isolated trees and their `run.log`/`run.err`). No tool, packet, baseline, corpus or
  earlier-round byte was edited; no commit. `TMPDIR=$PWD/.scratch` was exported for every
  scratch-writing command (operator rule: `/tmp` is inode-exhausted).
- instrument: `tools/gates/handoff-packet-check.py` sha256
  `e2fa3223b2aa57382807c51099a4360c1a9cc2559d5b4bedad1b54e9ab0ad575` — unchanged from the
  revision the round-9 `r9-pre` baseline pinned (re-hashed at every sweep below).
  `--selftest` run 22:02Z: exit 0 (`fixture findings 11 across 9 ids …; clean control exit 0;
  … CLI verified from another cwd`).
- isolation method: for every run below, the packet **and** the gate were copied into their own
  scratch tree `.scratch/r11-o10/tree-<label>/` (fresh `rm -rf` + `cp` each time), and the gate
  was run as `python3 tools/gates/handoff-packet-check.py packet.md` **from that foreign
  working directory**. The live paths were never the worked paths; the gate is read-only and no
  run wrote to the repo.

## 1. Verdicts — every assembled packet graded

All runs below: gate `e2fa3223…`, isolated tree, **exit 0**, stdout exactly
`INFO scan: fields=16/16 glossary-entries=20 findings=0`, stderr empty, finding-ID set `[]`
(clean). `stdout sha256 = 7c581047…` in every clean run (the scan line is the whole stdout of a
clean packet, so it is byte-identical across packets; verdict discrimination rests on exit code
+ scan counts + finding-ID set, not on stdout alone).

| # | packet (revision graded) | sha256 at run | run (UTC) | exit | scan |
|---|---|---|---|---|---|
| 1 | `reports/round-11/handoff/packet-attempt-1.md` (O06, D3 live bytes) | `289c8ca25bbebca7708f6a15fa9b9b2b7c985d9d809693c36f47dd657c383172` | 22:07:38 | 0 | 16/16, 20/20, 0 |
| 2 | `reports/round-11/handoff/packet-attempt-1.yml` | `82ed1cb5dd2e77bbba6fdccf4f7af7551e05ca9013b8ab5eeac7d0619b2a32a9` | 22:09:25 (stdin form also 0) | 0 | 16/16, 20/20, 0 |
| 3 | `reports/round-11/handoff/packet-attempt-2.md` (O07, D2 + typed labels) | `7497c2144c0b01df945127fdc8f3c5902bace814c139ba21e658c2cf8d191fcb` | 22:15:25 | 0 | 16/16, 20/20, 0 |
| 4 | `reports/round-11/handoff/packet-attempt-2.yml` | `6702235aab275b77b3c1eae811e7156a3efc49956b821fbf9f89971adba67879` | 22:17:56 | 0 | 16/16, 20/20, 0 |
| 5 | `reports/round-11/handoff/packet-attempt-3.md` (O08, hybrid D2+D3) | `17edb438555593161c30508c7275f1c34a83285d7dc07fdc43683a5f4787b559` | 22:15:25 | 0 | 16/16, 20/20, 0 |
| 6 | `reports/round-11/handoff/packet-attempt-3.yml` | `9e7eef80e6fa43f77384c55cae77415d304464131db41df2c6b148a70e5bda87` | 22:17:56 | 0 | 16/16, 20/20, 0 |
| 7 | `reports/round-11/handoff/packet-attempt-4.md` (O09, D3 registers) | `eb7eddb56d966b233b90c68c2de5eed58b8e9d8ff57acf0a7edb2dab24ce856e` | 22:13:48 | 0 | 16/16, 20/20, 0 |
| 8 | `reports/round-11/handoff/packet-attempt-4.yml` | `65f698758192a643ac7eab421f0781215c8a33ef5da855387f41252967396350` | 22:13:48 | 0 | 16/16, 20/20, 0 |
| 9 | `reports/round-11/handoff/packet.md` — exercise packet, current revision | `6583b6bdbf5e3fe039d1eee1d9f53d63ef09a04e3eeb5c98ae4943ed1771a64f` | 22:17:56 | 0 | 16/16, 20/20, 0 |
| 10 | exercise packet, earlier revision, then at `tools/gates/expected/handoff-exercise/r11/packet.md` (path since relocated, §4.1) | `2a058f7858127b98592439594c55974d93e6e672a600dd2036b47e21e71c8a63` | 22:09:25 | 0 | 16/16, 20/20, 0 |
| 11a | `.scratch/o04/packet-d2-first-20.md` (pre-integration scratch candidate) | `4dab58aec4dc4e1d762ca6079204a9b9725df10f4909e8e3040d8c6f521b58cd` | 22:05:41 | 0 | 16/16, 20/20, 0 |
| 11b | `.scratch/o04/packet-d2-stratified-20.md` (scratch candidate) | `467052f53ed3c3cb23f2bf61aaa77abfcec5cafaf2a2a334e9d543cf8dac7b4a` | 22:05:41 | 0 | 16/16, 20/20, 0 |
| 11c | `.scratch/o04/packet-d3-all-20.md` (scratch candidate) | `137ca8dcb21bde3903ebfdb8949cb1468ba4b219ea14400364cf83d645e88877` | 22:05:41 | 0 | 16/16, 20/20, 0 |
| 11d | `.scratch/o05/packet-positive.md` (scratch candidate; byte-identical to `examples/handoff-packet.sample.md`, digest `4e24bd3b…` for both) | `4e24bd3b887cf148155d89855d3c9eb842d3e325a4fa4302fccaa6c9d23dd712` | 22:05:41 | 0 | 16/16, 20/20, 0 |

Rows 11a–11d are the pre-integration scratch candidates the assembly shards left behind; they
are recorded as graded, but they are transient (gitignored) and are not the round's deliverables —
the carried packets are rows 1–9. Row 10 is retained because it is the revision the exercise's
first freeze pinned; it was superseded by row 9 when the baseline was regenerated/relocated.

Cross-checks recorded, not assumed:

- Row 9: `reports/round-11/handoff/expected.json` (sha256 `a94f9ded…`) pins
  `packet_sha256 = 6583b6bd…`; recomputing `sha256sum` over the packet at 22:19:21Z gives the
  same bytes (match True). `freeze.txt` (`56607f29…`) and `run.log` (`60d29658…`) both carry the
  same verdict, regenerated 19:19:33 local (22:19:33Z).
- Row 2: the `.yml` passes the Markdown-shaped gate because it carries (a) a level-1-shaped
  comment `# Handoff packet — R11-O06 …` (line 1) and (b) an `envelope_markdown_view:` list of
  16 `- field: value` items (lines 21–36) — the field form the gate recognizes; the shapes of
  the other `.yml` files are analogous. Recorded so the clean `.yml` verdicts are not mistaken
  for an accident.

## 2. Revisions observed while grading (re-run discipline)

The assembly seats were still polishing their packets while this record was measured; a verdict
binds the digest named at run time, so revised bytes were re-run and superseded revisions stay
recorded here:

| path | revisions observed | verdicts |
|---|---|---|
| `packet-attempt-2.md` | `d59053a1…` → `7a042cd6…` → `7497c214…` | `d59053a1…` clean (~22:10Z); `7a042cd6…` observed 22:15:1xZ already superseded — **not graded**; `7497c214…` clean 22:15:25Z, stable ≥5 min |
| `packet-attempt-2.yml` | `f35d17ac…` → `6702235a…` | both clean (22:11:02Z; 22:17:56Z) |
| `packet-attempt-3.md` | `a5f28c20…` → `17edb438…` | both clean (~22:13Z; 22:15:25Z, stable) |
| `packet-attempt-3.yml` | `36b9b7a2…` → `9e7eef80…` | both clean (22:13:48Z; 22:17:56Z) |
| exercise packet | `2a058f78…` → `87523e3d…` → `6583b6bd…` | all three clean (22:09:25Z; 22:14:44Z; 22:17:56Z) |
| `packet-attempt-1.md`, `-1.yml`, `-4.md`, `-4.yml` | single revision | clean (times in §1) |

Final stability sweep 22:19:21Z and 22:20:56Z: every carried digest above unchanged since its
graded run; gate digest unchanged at `e2fa3223…`.

## 3. Falsifiability probes (isolated copies of the current exercise packet, `6583b6bd…`)

Two edited copies of row 9's bytes (copies only — the live bytes were never touched):

| probe | edit on the copy | observed |
|---|---|---|
| P1 | blank the `## open_questions` section body → `TBD` | exit **1**; `FINDING HO-EMPTY: FAIL … present at section heading line 139 but carries only a blank/placeholder value`; scan `fields=15/16` |
| P2 | `- canon_standing: …` → producer certification | exit **1**; `FINDING HO-CANON-CLAIM: FAIL — producer-side canon certification at line 5`; scan 16/16 |

The same probe classes fired on the previous revision (`87523e3d…`, P1 blanked at list item 34 /
P2 at line 16). The clean verdicts in §1 are therefore falsifiable on these very bytes: the gate
refuses a blank required field and a producer-issued canon certification.

## 4. Observations for the parent (reported, not absorbed)

1. **Baseline relocation.** The exercise baseline moved from
   `tools/gates/expected/handoff-exercise/r11/` (files present 22:10:54Z) to
   `reports/round-11/handoff/` (`expected.json`, `freeze.txt`, `packet.md`, `run.log` present
   22:13+; the old directory is gone). `tools/exercise-handoff-e2e.py` was revised accordingly
   (`FROZEN_DIR_DEFAULT = "reports/round-11/handoff"`; tool digests observed: `38d1cba4…` at
   22:09Z → `e74e5aea…` at 22:15Z → `a21934ad…` at 22:19Z). `run.log` is gitignored
   (`.gitignore:3: *.log`) — the committed baseline needs a forced add, as the round-9 record
   also noted.
2. **Transient E2E-DIGEST red, now resolved.** At 22:15:09Z `python3 tools/exercise-handoff-e2e.py`
   exited 1 (`FAIL input-digest: examples/culture-d2/typed-labels.d2.yml: frozen e70ba147… live
   a3aa452c…`; `packet_sha256=(not assembled)`) because the D2 typed-pipeline seat edited that
   frozen read-set input mid-window. By 22:19:21Z the owner had re-frozen: the exercise exits 0
   (`exit=0 fields=16/16 glossary=20/20 findings=0 packet_sha256=6583b6bd…`), and the regenerated
   `expected.json` pins exactly that packet. Both the incident and its resolution are recorded;
   current state is green. (The drift guard behaved as designed — it refused re-assembly rather
   than blessing changed inputs silently.)
3. Contract cross-reference verification (`worldbible-integration-contract.md` field-by-field)
   belongs to the R11-O12..O13 seat (`reports/round-11/handoff/contract-check.md`, which also
   recorded gate runs for A1/A1y/A2). This file records the envelope-gate verdicts for all four
   attempts, both serializations, and every exercise-packet revision; no finding of that seat is
   re-adjudicated here.
4. Verdict scope reminder: the gate judges the packet document (16-field envelope, non-canon
   marker, glossary-etymology presence/vocabulary). It does not judge truth, digest-vs-bytes,
   subject resolution, or canon standing; these clean verdicts are gate verdicts, not design
   PASSes or canon decisions (§6/§11 keep canon standing to lore).

## 5. Reproduction (a stranger, from the integration commit)

```bash
cd <lane>
export TMPDIR=$PWD/.scratch
T=.scratch/r11-o10/tree-handoff-attempt-4          # or any tree-<label> dir kept in scratch
python3 tools/gates/handoff-packet-check.py "$T/packet.md"
# expect: INFO scan: fields=16/16 glossary-entries=20 findings=0 ; exit 0
sha256sum "$T/packet.md"                            # equals the digest in §1 for that label
python3 tools/gates/handoff-packet-check.py --selftest   # exit 0 (fixture 11 findings / 9 IDs)
```

## 6. Limits of this record

- Verdicts bind the digest named; later revisions of the same path need re-runs (done for every
  mid-window revision, §2). The scratch trees holding the run logs are gitignored and can be
  swept; the digest-stamped tables above plus the sibling seats' records are the durable
  evidence.
- The exercise tool and its baseline were themselves being revised while this record was
  measured (tool digest chain in §4.1); re-run the exercise or re-freeze before relying on any
  state not stamped here.
- Only the envelope gate over the named bytes was exercised here; no claim is made about the
  packets' design quality, the truth of their content, or canon standing.

Measured-by: round-11 O10..O11 seat (role label only). Date: 2026-10-17.
