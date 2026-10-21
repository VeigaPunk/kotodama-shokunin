# CriticProbeV2 — round 50 falsify, claim O counting probe amendment (v1 → v2 R1 predicate)

Seat: `KotodamaR50-2.CriticProbeV2-21` (critic, leaf). Axis judged: operability.
Landed commit `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`, base `4ad26836552462d28a946ca3b067cab0b5ce3532`.
All runs in a private `git clone --shared` under `/tmp` checked out at the landed commit,
`GIT_CEILING_DIRECTORIES=/tmp`; clone deleted afterwards. No installs. No lane writes except this report.

## Verdict: PARTIAL

The v2 amendment is a **faithful reading of claim O's declared `after_required`**, not goalpost-moving,
and it reproduces exactly: base 3/3, landed 0/3, `landed_sha=<HEAD>` still flagged. But the v2 R1
predicate is **weaker than the claim it encodes**. It accepts *any* ancestor of `origin/main`, and the
R1 fixture places `origin/main` exactly one commit under `HEAD`. So a positional fake
(`landed_sha=<HEAD^>` or `landed_sha=<root commit>`) scores 0/3. The landed probe also still carries
the v1 R1 contract in its docstring. The amendment is undisclosed in the lesson and receipt.

## Inputs (byte identity)

| bytes | source | sha256 |
|---|---|---|
| probe v1 | `git apply .ufo/waves/round-50/patches/ExecProbe-4.patch` | `276eff71eb90edd4de3954be88e09622853eae446ae13a3a738c0235102e7d31` (matches `telemetry/jj-probe-v1.txt:1`) |
| probe v2 | `1c779e4:reports/round-50/jj-colocation-probe.py` | `d3fff001f8fd08133ad20b83133ca743af4d3bc792710e351c263fd7212aafa5` (matches `telemetry/jj-probe-v2.txt:1`) |
| base tools | `git archive 4ad2683 tools` | — |
| landed tools | `1c779e4:tools/` | — |

`diff v1 v2` is confined to the R1 predicate (`case_r1`, landed lines 241–265). v2 counts only labels
containing `landed`, and flags R1 when no such label is present or one is not an ancestor of
`refs/remotes/origin/main`. `committed_sha=<HEAD>` moves to the informational field `committed_local_only`.

## Re-run results (both versions, landed bytes; `--history-repo` = landed clone)

| tools | v1 FN / FP | v2 FN / FP | v2 R1 |
|---|---|---|---|
| base 4ad2683 | 3/3 · 0/4 | **3/3** · 0/4 | flagged: "guard reports no landed sha distinct from the local HEAD" |
| landed 1c779e4 | 1/3 · 0/4 | **0/3** · 0/4 | not flagged: "every landed-labelled sha is an ancestor of refs/remotes/origin/main" |
| F1 fake `landed_sha=<HEAD>` | 1/3 | **1/3** (caught) | `landed_sha=<HEAD>` "is not an ancestor of refs/remotes/origin/main" |
| F2 fake `landed_sha=<HEAD^>` | 1/3 | **0/3 (missed)** | "every landed-labelled sha is an ancestor…" |
| F5 fake `landed_sha=<root commit>` | — | **0/3 (missed)** | same |
| F3 correct guard, label renamed `remote_sha` | 1/3 | 1/3 (over-strict) | "guard reports no landed sha…" |

These match `telemetry/jj-probe-v1.txt:10,21` and `jj-probe-v2.txt:10,21` (1/3 → 0/3 on the landed
tools, 3/3 on base under both). The telemetry measured "working tree copies"; the landed bytes give
the same counts.

Each fake (F1, F2, F5) changes only the `landed_sha=` f-string in the landed
`_check_receipt` (`receipt_guard.py:212`). F1 uses `{head}`, F2 uses `rev-parse HEAD^`, and F5 uses
`rev-list --max-parents=0 HEAD`.

## Q1 — faithful or goalpost-moving? Faithful to the declared claim; v1 was stricter than the claim.

- Claim O (`claims.json:34`) asks the guard to report "a landed (branch/remote) sha distinct from the
  local HEAD". The claim is additive and does not require dropping `committed_sha`.
- The fleet audit offers the same remediation. `JjAuditKotodama.md:224` recommends to "print the
  `origin` commit as `committed_sha` (**or a separate `landed_sha`**)". The landed guard took the
  second option, and the guard docstring (`receipt_guard.py:13-15`) documents it.
- The round-14 design contract (`reports/round-14/guard/design.md:125-134`) fixes
  `committed_sha` as "the exact committed snapshot checked" (HEAD). Field labels "may be extended,
  not omitted". So v1's demand that `committed_sha` be landed contradicts a standing contract.
- Pre-registration holds. `claims.json` mtime is 12:09:21 -03 (15:09Z). The v1 patch lands at 12:45, the v1
  telemetry at 12:59:30, the v2 probe at 12:59:38 and the commit at 13:03. The claim sentence was not
  rewritten after the v1 result.
- Counter-evidence (the strongest available): the build spec that commissioned the probe
  (`.ufo/waves/round-50/build-spec.json:31`, mtime 12:12) defines R1 as "receipt guard cites a
  local-only HEAD as the **committed/landed** sha". The landed guard still prints
  `committed_sha=<local-only HEAD>` in R1, and in R2 it prints `committed_sha=<HEAD> committed_blob=none`.
  That is the audit's residual copy-paste risk (`JjAuditKotodama.md:91-95`), now beside a correct
  `landed_sha`. Under the build-spec wording, v1 was the literal reading. v2 is the claim's reading,
  and the claim is the declared judge. This is a tradeoff, not a defect, but it was resolved post hoc,
  8 seconds after the v1 run.

## Q2 — does base still score 3/3 under v2? Yes.

Re-run: `JJ_COLOCATION_FALSE_NEGATIVES=3/3`, `FALSE_POSITIVES=0/4`. The base guard emits no
`landed`-labelled token, so `flagged = not landed` fires.

## Q3 — is a fake fix `landed_sha=<HEAD>` still flagged? Yes. But neighbouring fakes are not.

- F1 (`landed_sha=<HEAD>`) is flagged: HEAD is local-only, so it is not an ancestor of `origin/main`.
- **Counterexample F2/F5.** The predicate at `jj-colocation-probe.py:248-249` (landed) is
  `not box.is_ancestor(repo, sha, "refs/remotes/origin/main")`. It accepts any ancestor, and the
  R1 fixture (`:228-233`) commits the receipt in the only commit C0, sets `origin/main` = C0 and adds
  exactly one local commit. So `HEAD^` = root = the `origin/main` tip, and both fakes score 0/3 with
  "every landed-labelled sha is an ancestor". The probe therefore cannot tell "reports the remote
  holder" apart from "reports HEAD's parent".
- **Mitigation (the combined claim check still holds).** Claim O also requires `receipt_guard --selftest` to
  pass. On the landed bytes it exits 0. F1 exits 1 (failing `r50-detached-below-remote`,
  `r50-local-over-remote`, `r50-unborn-remote`, `r50-local-branch-not-landed`, `r50-refresh-landed`),
  and F2 and F5 exit 1 as well (5 and 7 failed controls). But those controls ship in the same file as
  the guard, so a fixer who fakes `landed_sha` can edit them too. The probe is the independent oracle,
  and on its own it does not catch positional fakes.

## Further findings

1. **Stale contract text (fixable).** The landed probe docstring
   `jj-colocation-probe.py:10-12` still says R1 is "Flagged when receipt_guard presents a sha as
   committed or landed that is not an ancestor of refs/remotes/origin/main". That is the v1 predicate,
   and v2's code (`:247-252`) contradicts it. The "presented sha" definition at `:28-31` is also
   unchanged, although v2 ignores non-`landed` labels for the count.
2. **Undisclosed amendment (fixable).** The amendment is recorded only in the telemetry header
   (`jj-probe-v1.txt:1`, "superseded by v2 (see report)") and in the code comment `:241-246`.
   `corpus/lessons/round-50.md` (landed) and the working-tree receipt `reports/round-50/validation.json`
   contain no mention of v1, the amendment, or the 1/3 result (grep for
   `superseded|amend|jj-probe-v1|predicate` returns 0 hits relevant to the probe). "see report" points nowhere.
3. **Label coupling (minor, conservative direction).** F3 is a correct guard that prints
   `remote_ref/remote_sha`. v2 flags it, because the count keys on the substring `landed` in the label
   rather than on the commit identity. This only produces over-reporting, so it cannot inflate the
   claim, but the predicate is tied to the implementation's naming.

## Impacted axes

operability: the claim O probe's claim "0/3 on landed" stands, but the oracle's discriminating power
is overstated. No coverage or calibration impact.

## Smallest safe correction (verified in /tmp, not applied)

A two-hunk change to `case_r1` (sha256 of the corrected probe `38e8d902…20873644`):

```diff
-    write(repo, RECEIPT, "R1 receipt\n")
-    box.commit(repo, "C0: receipt committed on main")
+    write(repo, "base.txt", "base\n")
+    box.commit(repo, "C0: base")
+    write(repo, RECEIPT, "R1 receipt\n")
+    box.commit(repo, "C1: receipt committed on main")
     ...
-    box.commit(repo, "C1: local-only working-copy commit", empty=True)
+    box.commit(repo, "C2: local-only working-copy commit", empty=True)
+    box.commit(repo, "C3: local-only working-copy commit", empty=True)
 ...
-    stray = [(label, sha) for label, sha in landed
-             if not box.is_ancestor(repo, sha, "refs/remotes/origin/main")]
+    tip = box.rev(repo, "refs/remotes/origin/main")
+    stray = [(label, sha) for label, sha in landed if sha != tip]
```

Results with the corrected probe: base 3/3 (unchanged), landed 0/3 (unchanged), F1 1/3, F2 1/3, F5 1/3
(all fakes now caught), F3 1/3. FP stays 0/4 everywhere. Also needed:

- Rewrite the docstring at `:10-12` to state the v2 predicate (an exact remote-holder tip, and
  `committed_sha` kept by design and reported in `committed_local_only`).
- Add one line to the lesson or receipt disclosing the v1 run (1/3), the amendment and its basis
  (`claims.json:34`, `JjAuditKotodama.md:224`, `design.md:125-134`).

Author-lane advice, not admission.
