# ConnectSiblingGuard — round 50 falsify: claim O ref-probing vs the fleet's landed/pushed patterns

Seat: `KotodamaR50-2.ConnectSiblingGuard-21` (connector, leaf). Axis judged: **operability**.
Landed commit `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`, base `4ad26836552462d28a946ca3b067cab0b5ce3532`.
Method: landed bytes only, via a private `git clone --shared` checked out at the landed commit under
`/tmp/kr50-falsify-Hpuk`, `GIT_CEILING_DIRECTORIES=/tmp`; read-only against the lane; no installs; the
clone is deleted after this report. This is author-lane advice, not admission.

Byte identity of what was measured:

| bytes | sha256 |
|---|---|
| landed `tools/harness/receipt_guard.py` | `5a61c35016b61c71071d774773b329a4bb6646f9959bd3b82a15528b328cef14` |
| landed `reports/round-50/jj-colocation-probe.py` | `d3fff001f8fd08133ad20b83133ca743af4d3bc792710e351c263fd7212aafa5` (matches `telemetry/jj-probe-v2.txt:1`) |
| landed `tools/check-readme-revisions.py` | `54217e0e31e9c2c3650d169e2857c1b0e8c9ff05c8836deebec9ffcf0f9f13d4` |
| base `4ad2683 tools/harness/receipt_guard.py` | `d2297da4e6ceabb2eab84bb6e3beab16d82132aca0e313f0bdf21243304123a1` |

## Item attacked and verdict

**Item:** claim O's `receipt_guard` ref-probing and the identity it reports (`landed_ref`/`landed_sha`/
`landed_blob`), cross-read against the sibling patterns in
`.ufo/waves/round-50/build/ConnectSiblingJj.md` (souji S1, tsukuroi S4, kaidoku S5).

**Verdict: PARTIAL.** Detection/refusal holds and the claim's measured `after_required` reproduces
exactly (base 3/3, landed 0/3, 0/4 false positives, guard 69/69, prior 45 controls byte-identical in
name and order). The **landed-identity clause does not generalize**: `landed_*` is the
alphabetically first `refs/remotes/*` **holder**, with no ancestry test and no relation to the branch
being written (`receipt_guard.py:207`). In a multi-remote repository it can name a divergent side
branch as landed — a value the probe's own R1 predicate would flag — and the probe's fixtures cannot
see this because each builds exactly one remote ref. `refs/tags/*` is not probed at all; the wave
recorded that exclusion with an unverified inference (`ReviewGuardSemantics.md:87`), and I verified
the inference (0 tags, no lane tool creates tags), so the exposure is latent, not live.

## Evidence

### 1. The claim's mechanical acceptance reproduces

```text
$ python3 -B tools/harness/receipt_guard.py --selftest          # landed tree
exit=0  controls_passed=69 / 69
$ python3 -B tools/harness/receipt_guard.py --selftest          # base tree
exit=0  controls_passed=45 / 45
base prefix == landed prefix: True (len 45); 24 appended r50-*/attached-*/unborn-*/other-* controls
```

`check-readme-revisions.py --selftest` (landed): every control PASS, `selftest: all checks passed`,
exit 0, including `PASS control: base c42d675 README flagged (r49 defect)` and
`ERROR control: git-free tree fails closed` / `shallow clone with unreachable pin fails closed`.

Probe, landed tools: `JJ_COLOCATION_FALSE_NEGATIVES=0/3`, `JJ_COLOCATION_FALSE_POSITIVES=0/4`.
Probe, `git archive 4ad2683 tools`: `JJ_COLOCATION_FALSE_NEGATIVES=3/3`,
`JJ_COLOCATION_FALSE_POSITIVES=0/4`. The v1→v2 amendment is faithful to the declared `after_required`
(see `CriticProbeV2.md`, which covers the fake-sha weakness of v2; this report covers a different gap).

### 2. Cross-lane: kotodama reports a *holder*, the fleet reports branch/landed + pushed

The fleet's converged invariant (`ConnectSiblingJj.md:31`, P1) is three values: tree source,
on-branch/landed, pushed. Its guards make pushedness an ancestry test, not a name lookup:
`souji-shokunin/tools/souji-rev-pin.py:37` declares
`DURABLE_NAMESPACES = ("refs/heads", "refs/tags", "refs/remotes")` and `:216` accepts a commit only if
`merge-base --is-ancestor <rev> <tip>` succeeds against one of those tips; tsukuroi S4 returns
`Binding(sha, branch, branch_tip, origin_tip)`; kaidoku S5 keeps HEAD compare-only.

The landed kotodama guard instead:

- classifies **every** `refs/heads/*` and `refs/remotes/*` ref as a receipt holder
  (`receipt_guard.py:103-105`) — deliberately broader than the build spec's
  "refs/heads/<branch> AND refs/remotes/origin/<branch>" (`gen-build-spec.py:39`;
  `ReviewGuardSemantics.md:70`, C-4b), which is a strict improvement for *detection*;
- then selects `landed = first(hit for hit in hits if hit[0].startswith("refs/remotes/"))`
  (`receipt_guard.py:207`) and prints it as `landed_*` (`:209-214`);
- never proves ancestry and never reports the branch tip. A receipt committed only on
  `refs/heads/main` reports `landed_ref=none landed_sha=none` (control
  `r50-local-branch-not-landed`, `:428-434`) even though, in this lane's own vocabulary, it is landed.
  S4 would call that value `branch_tip` and set `pushed=false`.

The docstring is honest about the contract (`receipt_guard.py:13-16`: "landed_ref and landed_sha name
only a refs/remotes/* holder"), so the tool does not lie about what it measures. The defect is that
"landed" is a three-way overload: claim O/probe mean *pushed to origin/main*, the fleet's S4 means
*branch tip*, and the tool means *any remote holder*.

### 3. Falsifying fixture: the R1 shape plus one divergent remote

Built the probe's R1 state exactly (receipt on main and `refs/remotes/origin/main`, HEAD a local-only
empty commit above the tip) and added one extra remote-tracking ref `refs/remotes/origin/aaa` holding
a stale copy of the same path:

```text
receipt_guard: refusing overwrite path=reports/validation.json
  committed_sha=812000b2… committed_blob=dfb04a89…
  landed_ref=refs/remotes/origin/aaa landed_sha=48820fb6… landed_blob=8b979df6…
  hit_refs=HEAD,refs/heads/main,refs/heads/side,refs/remotes/origin/aaa,refs/remotes/origin/main
exit=3
```

`landed_sha` is **not** an ancestor of `refs/remotes/origin/main` (verified with
`merge-base --is-ancestor`); `landed_blob` is a different receipt revision than `committed_blob`. Under
the probe's own v2 R1 definition (`jj-colocation-probe.py:247-252`: "a landed-labelled sha that is not
an ancestor of refs/remotes/origin/main") this row is a false negative, but the probe's R1 fixture
(`:227-239`) constructs only `origin/main`, so the measurement scores 0/3. Two smaller reproductions of
the same selection rule:

- two remote holders with different blobs (`origin/aaa` orphan, `origin/main`): `landed_ref` names
  `origin/aaa` and `landed_blob` is the orphan copy while HEAD and `origin/main` hold another blob;
- a receipt held only by a divergent `refs/remotes/origin/cursor/old`: the guard refuses correctly but
  reports `landed_ref=refs/remotes/origin/cursor/old` for an orphan root unrelated to `origin/main`.

### 4. Tags: unprobed, and the wave's inference is now verified

`receipt_guard.py:103-105` enumerates only `refs/heads` and `refs/remotes`. A receipt committed only on
a tag (lightweight and annotated fixtures) yields `exit=0` — the overwrite is allowed. The wave knew:
`ReviewGuardSemantics.md:87` lists `refs/tags/*` as an excluded, documented limit, with
"[INFERENCE] no lane tool creates tags; not grepped". I grepped the lane: `git for-each-ref refs/tags`
= 0, and no tool or round runner creates tags. So the exclusion is safe **today**, but it contradicts
the fleet's durable-root rule (`souji-rev-pin.py:37`) and is absent from the tool's own docstring.

### 5. `check-readme-revisions`: existence, not durable reachability (lower severity)

The base pin is accepted on `git cat-file -e <pin>^{commit}` (`check-readme-revisions.py:274`). A commit
present only as an unreferenced object (all refs deleted) still yields
`PASS control: base … README flagged` and `selftest: all checks passed`, exit 0. The sibling rule
(`ConnectSiblingJj.md:44`, S1) treats plain existence as insufficient durability. Severity is lower
than the guard's tag gap: the fetched bytes are genuine (replace refs are disabled by
`GIT_NO_REPLACE_OBJECTS=1`), and a later `gc`/prune makes the pin unresolvable, which flips the
control to ERROR/exit 2 — it fails closed rather than passing on wrong bytes.

### 6. Live-lane exposure today is latent, not active

- 44 `reports/**/validation.json` paths, every one present only on `refs/heads/main`,
  `refs/remotes/origin/main` and symref `origin/HEAD` — no divergent ref holds one.
- 7 divergent `refs/remotes/origin/cursor/*` refs; each holds 0 `reports/` paths. One extra remote
  (`origin/devin/wiki-link`) is an ancestor of `origin/main`.
- 0 tags; 0 tag-creating tools.
So neither the multi-remote misattribution nor the tag gap can bite in this lane's current ref state;
they are one agent branch committing a report receipt away from doing so.

## Contradictions (stated, not scored)

1. **Ancestry rejected by the tool, required by the measurement.** `ReviewGuardSemantics.md:187`
   (FO-19) says "do not use ancestry" because `merge-base` failures are not disabled by
   `GIT_NO_REPLACE_OBJECTS` in shallow/grafted repos; `receipt_guard.py` has no `merge-base` at all
   (grep: none). The probe then uses `merge-base --is-ancestor` as its correctness predicate
   (`jj-colocation-probe.py:136-140`), mapping any nonzero rc to "not ancestor". The tool and its
   judge are built on opposite robustness assumptions; the judge's failure mode is a false R1 flag
   (over-count), while the tool's is a mislabelled identity (under-information).
2. **The connector's durable-reachability recommendation was not adopted.** `ConnectSiblingJj.md:53`
   (proposal 3) asks for heads|tags|remotes reachability before `git show`; the landed readme gate uses
   `cat-file -e`, and the guard excludes tags. C-4b (`ReviewGuardSemantics.md:70`) accepted the
   broadened probe but never scoped the `landed_*` selection back to the branch's origin.
3. **"Landed" means three different things** in the claim, the probe, and the tool (see §2). The
   claim's parenthetical "(branch/remote)" does not disambiguate; the build spec's original wording
   ("the branch/remote commit", `gen-build-spec.py:39`) is the only one that matches the intended
   semantics, and the implementation does not implement it.
4. **The `hit_refs` docstring claim is absolute** ("lists every holder", `receipt_guard.py:15`), but
   symbolic remote refs are skipped (`:123-124`), so a `refs/remotes/origin/HEAD` that aliases a holder
   is absent from the list. Cosmetic; no decision changes.

## One bounded proposal

Keep the broad probe (it is the detection fix; do not regress it) and make the identity honest:

1. In `receipt_guard.py`, resolve the branch once — `symbolic-ref --quiet HEAD` when attached, else the
   target of `refs/remotes/origin/HEAD`, else `main` — and set
   `landed = first(hit for hit in hits if hit.name == f"refs/remotes/origin/{branch}")`; when that ref
   is not a holder, print `landed_ref=none landed_sha=none landed_blob=none` and add
   `remote_holders=<comma-separated refs>` for every other `refs/remotes/*` hit. Refusal, `hit_refs`,
   `committed_sha` and `committed_blob` keep their current values and order. Decision outcomes do not
   change; every one of the 24 appended controls still refuses/permits identically except
   `r50-other-remote` (`:422-426`) and `r50-other-branch-remote` (`:414-420`), whose `landed_ref`
   expectation becomes `none` plus `remote_holders=` (their stated purpose — non-origin remotes are
   probed and refused — is preserved).
2. Add one guard control `r50-multi-remote-holder` (the §3 fixture: `origin/aaa` divergent + stale blob,
   `origin/main` current) asserting `landed_ref=refs/remotes/origin/main` and
   `landed_blob=<origin/main blob>`, and one probe case `R1b` with the same two refs so the metric
   covers the shape (defects become n/4; update claim/validation/lesson numbers).
3. For tags, either probe `refs/tags` with peel (`%(objectname) %(*objectname)`; an annotated tag lists
   `objecttype=tag`, so a naive add fails every write closed) or state the exclusion in the
   `receipt_guard.py` docstring and the probe's `limits`. Given 0 tags and 0 tag-creating tools, the
   docstring line is the honest minimum; the code change is the fleet-consistent option.

## Risks

- The two updated control expectations are the only semantic regression surface; a solution that keeps
  "first remote holder" and merely renames the fields would break the probe's `landed`-label detection
  (`jj-colocation-probe.py:203-213`) and needs its own predicate update — prefer re-scoping over renaming.
- Under jj colocation HEAD is normally detached, so "else `main`" is a convention. Using the
  `refs/remotes/origin/HEAD` symref target is more faithful than hard-coding `main`; if origin/HEAD is
  dangling, fall back to `main` and record it, do not fail closed (matches control
  `r50-dangling-origin-head`).
- `remote_holders` must not be parsed by the probe as a landed sha: it is a ref-name list; the existing
  `TOKEN_RE` would ignore it, but the probe's `presented()` should be re-read if any hex ever appears.
- Ancestry is still absent; this proposal removes the concrete false attribution but does not give the
  fleet's `pushed` bit. Adding it later needs an explicit rc-2/128 fail-closed path (FO-19), which the
  wave deliberately avoided.
- Probe/claim numbers change 3→4 defects; `reports/round-50/validation.json`, `claims.json`,
  `corpus/lessons/round-50.md` and the telemetry notes all cite the current 0/3 and must be restated.

## Verification (author lane, not run here)

```text
python3 -B tools/harness/receipt_guard.py --selftest     # 69+1 controls, all pass; prior 45 names unchanged
python3 -B tools/check-readme-revisions.py --selftest    # unchanged, exit 0
python3 -B reports/round-50/jj-colocation-probe.py --tools-root <landed> --history-repo <history>
  # expect 0/4 false negatives, 0/4 false positives after R1b is added
python3 -B reports/round-50/jj-colocation-probe.py --tools-root <base-tree> --history-repo <history>
  # expect 4/4 false negatives (the tag case is not part of R1-R3; keep it a guard control)
```

Fixtures already exercised in this seat that a fix must still satisfy: tag-only allow/refuse decision,
annotated-tag `objecttype=tag` peel, `origin/aaa`+`origin/main` collision, orphan-root remote holder,
unpushed branch reporting `landed=none`, and the R1/R2 probe shapes.

## Unrun / limits

- No `jj` command was run and no live runner was invoked; the lane's ref state was read with
  `for-each-ref`/`ls-tree` only. No sibling selftest was run; sibling claims are cited from their
  source lines, not re-executed here.
- Shallow/grafted ancestry failure modes (FO-19) were not reproduced; the proposal avoids ancestry, so
  no claim depends on them.
- The private clone was removed after this report; no lane file was edited, and no tool was installed.
