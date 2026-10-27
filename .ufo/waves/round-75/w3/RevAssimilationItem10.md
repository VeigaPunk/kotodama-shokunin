# RevAssimilationItem10 — WAVE 3 falsification of prompt §6 item 10 (claim C bytes)

Seat: RevAssimilationItem10 (leaf; no delegation, no background jobs).
Range attacked: `git diff f556d1049fe651d3d63975600b13acd9fb686f15 4f5e3b2535c2c06c51627dc2736c40183847cae1`
(freeze 5d01674 → claim Ca 012e8d3 → claim C 4f5e3b2; lane main is one commit further, 82ced5c, telemetry/report-side only — verified by `git log --oneline 4f5e3b2..main` = 82ced5c alone, which touches no claim-C byte).
Method: every obligation walked against the landed bytes; frozen bytes read via `git show <rev>:<path>`; counters and the guard proof re-run inside my own scratch clone (`/fast/scratch/hyaku/kotodama-r75/RevAssimilationItem10/lane`, toplevel asserted before use). No LSP device is mounted in this seat's tool inventory (recorded unavailable); this is a git-bytes review, so git/tree-level evidence is the primary instrument. No tools were installed.

## VERDICT: HOLDS — all seven obligations MET, no defect found

Independent counter run at the landing:

```
$ python3 -B reports/round-75/accept-c.py --root . --lands 4f5e3b2535c2c06c51627dc2736c40183847cae1 \
    --freeze 5d0167464309d8133991b30f7d7a7011a6a0fd14     # in scratch clone
ACCEPT-C-75: PASS legs=13/13   exit=0
```
(First attempt printed 12/13 with `CENSUS: census script not found` — my scratch lacked the fleet `scripts/` dir the counter resolves next to the lane root; after staging the read-only fleet script the run is 13/13 and matches the frozen telemetry `reports/round-75/telemetry/measures-c.txt` line for line, same counter sha256 315c5f3f…, same tree 43a96e73….)

---

## Obligation 1 — Source repo untouched: MET

- `git -C /home/vgpnk/Projects/shokuknow status --porcelain` = **1919 lines** — the ambient campaign dirty state (other lanes' staging, pre-existing). **0 lines match `round-75`**; the 127 kotodama-theme lines are the pre-existing staging (untracked `merge/kotodama/**` from corpus-expansion-1, mtimes below).
- In-round write check: `find /home/vgpnk/Projects/shokuknow/merge/kotodama -newermt '2026-10-26 00:00:00' -type f` → **0 files**. `SOURCES.append.md` mtime `2026-10-24 23:33:20`; all five staged `narrative-structure-frameworks*.md` files mtime `2026-10-24 23:33:20` (staged before the round; the round opened 2026-10-27).
- The adopted footprint — **one theme (myth-symbol / narrative-structure-frameworks), three entries** — exists only in the lane at 4f5e3b2 (`corpus/knowledge/myth-symbol/narrative-structure-frameworks{,.amend-2026-10-23,.amend-2026-10-23b}.md`). shokuknow holds only the pre-existing staged copies (five files; `amend-2026-10-23c` and `amend-2026-10-24` refused as separate paths per `rejects.refused_files_pending_triage`, their Barthes material folded into amend-23b).
- I ran no campaign tool in shokuknow; all reads were `cat`/`git`/`stat`/`find` (read-only). Guard scripts read `SOURCES.append.md` and the register read-only only.

## Obligation 2 — Every cited source re-opened in-round: MET

- Nine fetch records at `.ufo/waves/round-75/assimilation/validate-fetch/` (S885–S890, S892, S893, plus `W891.meta` for the S891 document — see Observation 4), each `<id>\t<HTTP status> <bytes> <content-type> <effective url>\t<sha256>`, all HTTP 200 on 2026-10-27, README binding one UA to all responses (QUALITY 22).
- Lesson `corpus/lessons/round-75.md` `## Gate`: all nine rows carry access date **2026-10-27**, a located quote within both caps (measured per row, e.g. S885 38 chars/6 tokens … S890 77 chars/12 tokens), and a locator.
- `reports/round-75/evidence/S885.txt … S893.txt` all exist **at the landing commit** (ls-tree verified), each with fetch line, UA, HTTP status, bytes, body sha256, `--- window ---` and its own recomputable `window-sha256:`; `quote-found: yes` / `quote-found-verbatim: yes` (spot-read S893, S888).
- **My own independent refetches** (plain requests, browser-shaped UA `Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0 Safari/537.36`, no challenge passed):
  - S893 `https://www.chinawriter.com.cn/n1/2023/0922/c404024-40083104.html` → HTTP 200, **45238 bytes, sha256 `51251e22c617617af797d164684e8927dc792a06140ff35fbaebc158515415f0` — byte-identical to `S893.meta` and `evidence/S893.txt`**; fresh quote `网络小说中的世界观，指的是故事设定中世间万物运转的方式` present (1 hit).
  - S885 `https://www.persee.fr/doc/comm_0588-8018_1966_num_8_1_1113` → HTTP 200, 111487 bytes (page not byte-stable, as the receipts disclose — three stored observations all differ); Gate quote `Innombrables sont les récits du monde` present (1 hit).
- Access discipline holds: the Persée `docAsPDF` endpoint (altcha CAPTCHA), the live unige page (bobcmn challenge) and the live unipa deposit (Cloudflare 403) were all **met and not passed**, refused as anchors, and replaced by public ordinary routes (per-page transcription service, Wayback captures) — QUALITY 10 compliant.

## Obligation 3 — Only cited rows appended: MET

- `git diff --numstat f556d1 4f5e3b2 -- corpus/SOURCES.md` = **9 0** (9 added, 0 removed); the single hunk appends exactly `| S885 |` … `| S893 |` after S884. No pre-existing row changed (counter ROWS leg: byte-identical; PASS).
- The three landed entries' `source:` lines cite exactly the nine: frameworks.md → S885, S888, S889, S890, S893; amend-2026-10-23.md → S885, S886, S887, S891, S892; amend-2026-10-23b.md → S885, S891, S892. Union = {S885..S893}; CITEDLINES leg = `0 finding(s) in 3 file(s)`.
- Nothing else of the 132-row staged package landed: 12 staged rows collapse onto the nine by document; the other 123 rows and 37 of 40 staged knowledge files are refused (`3 adopted / 6 path-present / 31 refused`, sums to 40, REJECTS leg PASS).

## Obligation 4 — Nine appended rows vs staged rows, by document: MET (normalizations documented; lossless at round level)

Join (my independent parse of `SOURCES.append.md` vs landed registry, agreeing with the frozen map's `cross_check`): S885 ← staged S876/S885/S917/S921; S886 ← S902; S887 ← S904; S888 ← S864; S889 ← S865; S890 ← S866; S891 ← S905; S892 ← S919; S893 ← S870. Ten distinct numeric offsets across twelve assignments — not arithmetic.

Cells normalized, per cell:

| cell | staged → landed | lossless? |
|---|---|---|
| id | staged campaign id → lane next-free id **by normalized document URL** (persee `/doc/page/…` transcription collapsed to `/doc/…`; wayback wrapper stripped) | yes — mapping is the pinned map (sha256 778068a4…, FROZENCFG-verified) |
| recheck | prose command cells (`180d — curl … \| grep … -> N (ran 2026-10-23)`) → cadence-only `180d` | yes at round level — stripped prose recorded in the lesson (substitution table, recheck rows), and this removes the literal pipes that made staged rows 12–13 cells instead of 11 |
| used-by | staged grep-command provenance → exactly the citing admitted entries | yes — counter-verified equality |
| opened | 2026-10-23/24 → **2026-10-27** | yes — the in-round re-open is the claim's substance; staged dates remain in the staging file |
| status | mined (value unchanged) | yes |
| source | expanded with in-round fetch provenance (HTTP 200/bytes/dates; wayback carriers named where live was challenged); document URL carried verbatim in 10/12 rows | yes, with one abbreviation: S885's cell writes p.6/p.11 transcription URLs elided (`…_T1_0006_0000`) — fully recoverable from the p.5 full URL prefix; join key intact (see Observation 5) |
| kind/tier | all unchanged EXCEPT staged S876 **B → A**: superseded by the in-round full-text open (staged B-reason "JS-viewer only" overtaken by the public per-page transcription service); the staged caveat "not claimed for the five-code enumeration" **is carried** into the landed S885 row (grep hit verified) | yes — upgrade justified and the caveat preserved |
| anchor | relocated to quotes located in-round; S870's staged anchor replaced by the fresh quote **plus the explicit refusal note** | yes — refusal reason + flip recorded in the row itself and the lesson |
| teaches/scope | rewritten into lane register; staged tier-justification prose dropped where superseded (correct, not information loss) | yes |
| S892 filename | map carries the %20-encoded form; landed row uses %20; both listed in `url_variants` so row and map cannot diverge | yes |

## Obligation 5 — Collision guard, 0–3-space pattern proved: MET (reproduced independently)

- Committed at freeze: `guard-proof/{README.md,make-fixtures.py,run-guard.sh,proof.txt,out/*}`. Fixtures = real base registry (808 rows, sha256 `c8da0a5a…` — matches my `git show f556d1:corpus/SOURCES.md | sha256sum`) + ONE planted staged id (S985–S989, clone of real S884, example.invalid URLs) at indents 0/1/2/3 spaces/4 spaces/tab; extractor `^ {0,3}\|[[:space:]]*S[0-9]{3,}` vs control `^\|[[:space:]]*S[0-9]{3,}`.
- **I rebuilt the fixtures from git and re-ran the entire matrix in my own scratch.** Results identical to the committed `out/*.summary.txt`:
  - control: 808 ids, 0 plant, collisions 26;
  - 1sp/2sp/3sp: **809 ids, plant seen, collisions 27 naming the plant, COLZERO misses it (0)** — the guard sees every row shape the census parser sees (census rows 809, no new finding);
  - 4sp and tab: **not seen by either** (4+ spaces = indented code per the census parser note; tab is not a table row) — correct, not a false green;
  - the column-zero-only false-green is reproduced exactly as the contract warns.
- Real registry at base: 808 ids vs 132 staged ids → **26 collisions (S859–S884), 0 same-document pairs, adopted S885–S893 free at base** — re-verified by my counter run's COLLCHECK leg (`ids=808 staged=132 collisions=26 map=12`).
- Renumber executed in scratch only, single simultaneous pass (staged ids themselves contain S885–S893 — a sequential sweep would corrupt; rule documented in the map). Post-landing, the 26 collisions resolve by document, not by number.
- Observation 3 below on `run-guard.sh`'s time-sensitive `real` section.

## Obligation 6 — Scratch-mirror receipt committed BEFORE the append: MET

```
git log --format='%h %ci %s' f556d1..4f5e3b2 -- .ufo/waves/round-75/assimilation/validate-receipt.txt
→ 5d01674 2026-10-27 17:43:38 -0300  round-75: freeze …
git log --format='%h %ci %s' f556d1..4f5e3b2 -- corpus/SOURCES.md
→ 4f5e3b2 2026-10-27 17:44:45 -0300  round-75: claim C landing …
```
Receipt commit precedes the registry-append commit (67 s; freeze is a first-parent ancestor of the landing — FROZENCFG `first-parent-chain=yes`). The receipt's **mirror registry sha256 `c1f9f1e0…` equals the sha256 I computed for the landed `git show 4f5e3b2:corpus/SOURCES.md`**, base sha256 `c8da0a5a…` matches, and all three entry sha256s in the receipt match the landed files — the rehearsed mirror bytes are the landed bytes. SCRATCHMIRROR leg: `receipt@0 append@2 rows=9 entries=3`, PASS.

## Obligation 7 — Staged S870 quote refused; S893 re-opened with a fresh quote: MET (verified live)

- Lesson rejection row: staged quote `作品中的人物名字和地名也一样…` **0 hits** on the 45238-byte body, and the three shorter fragments `人物的名字` / `名字和地名` / `地名也一样` also 0, while the page's own 世界观 passage returns 1; flip = a fresh located quote on the same page; verdict "refused as staged; the document re-opened as S893".
- The landed S893 row's anchor cell itself carries the refusal ("the staged round-72 quote span … is absent from this page and stays rejected"); the map marks S870→S893 **CONDITIONAL** on the Gate locating a fresh quote; the kill rule fails the claim had the staged quote been treated as located.
- **My independent live refetch** (2026-10-27, plain request, browser-shaped UA): HTTP 200, 45238 bytes, **sha256 `51251e22…` byte-identical to the recorded fetch**; fresh quote 1 hit; refused span **0 hits**. The refusal is factually true of the live page today, and the re-open quote is where the row says it is.
- Register bridging is read-only and by document only: register S787 ↔ staged S870 ↔ lane S893 recorded in the lesson's Quarantine; the register was never edited.

---

## Observations (none rises to a defect)

1. **UA string form.** `validate-fetch/README.md` binds `Chrome/130.0.0.0 Safari/537.36` while the lesson Gate, the `evidence/*.txt` `ua:` fields and the round dispatch write `Chrome/130.0 Safari/537.36`. Same client version (130); my refetch using the `130.0` form reproduced the `130.0.0.0`-fetched S893 body byte-for-byte. QUALITY 22 binding is present either way.
2. **Lesson Gate note 5 is stale at the landing, honestly so.** It says S891/S893 "have no probe receipt … at this wave" — `counters/probe-receipts/` indeed does not exist at 4f5e3b2, but the claim's actual requirement (`reports/round-75/evidence/S891.txt`, `S893.txt` with windows containing the Gate quotes) **is satisfied at the landing** (ls-tree + spot-read verified). The note describes the w2 stage at which it was written; the landing supersedes it.
3. **`run-guard.sh`'s `real` section reads the live worktree**, so a post-landing rerun prints 817 ids / 35 collisions / adopted-ids-present 9 instead of the committed pre-landing 808/26/0. Benign (the fixture matrix — the actual guard proof — is base-pinned via `git show` and reproduces exactly), but the script carries no drift guard or note.
4. **`W891.meta` id label.** The S891 document's fetch record is labeled W891; the bridge to landed row S891 is README prose only, no field in the record.
5. **S885's source cell abbreviates two of three transcription URLs** (`p. 6, ..._T1_0006_0000; p. 11, ..._T1_0011_0000`); recoverable from the p.5 full URL prefix, join key unaffected, staged full URLs remain in the staging file.

## Environment notes

- Counter scratch: the frozen counter materializes its clones under `/fast/scratch/hyaku/kotodama-r75/counter/r75-lands-*/` (its own committed convention, outside my seat dir — left in place). My seat scratch `/fast/scratch/hyaku/kotodama-r75/RevAssimilationItem10/` is deleted before yield; all receipts are quoted above.
- No pacman (paused host-wide); no tools installed; no fleet-repo, sibling-lane, lane-tracked-file, `.ufo/state`, or shokuknow writes. Lane side wrote only this report file at the seat-named path.
