# ScoutJjLive — R50 falsify, claim O (operability)

**Item attacked:** O — `tools/harness/receipt_guard.py` under real jj colocation (the landed proof for O is `reports/round-50/jj-colocation-probe.py`, whose docstring says "jj is never invoked", line 7).

**Verdict: PARTIAL.**

Every state the claim names (`jj new <older>`, `jj git fetch` advance, receipt committed+pushed, REFRESH permit) behaves exactly as claimed, and no unsafe overwrite (exit 0 while a probed ref holds the receipt) was reproduced. One legitimate jj HEAD sentinel, `ref: refs/jj/root`, makes the guard abort inside `_head_state` before it ever enumerates `refs/heads/*` and `refs/remotes/*`; there it emits no `committed_sha`/`landed_sha` and refuses a brand-new receipt that no ref holds. Because the abort is exit 3 (fail-closed), this is an operability/attribution gap, not a lost-refusal regression.

## Artifact identity

- Landed commit `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`, base `4ad2683…`.
- `git -C /home/vgpnk/Projects/shokunin/kotodama-shokunin rev-parse 1c779e4a:tools/harness/receipt_guard.py` → `9f8c039a6d11835533fd8762b5966730e014fc15`.
- `git show 1c779e4a:tools/harness/receipt_guard.py | sha256sum` → `5a61c35016b61c71071d774773b329a4bb6646f9959bd3b82a15528b328cef14`; sandbox copy identical.
- jj `0.45.1-7c41cdeb16b6b321c64e789a966b6adf723816a5`; git `2.56.0`.
- `git show 1c779e4a:reports/round-50/jj-colocation-probe.py | sha256sum` → `d3fff001f8fd08133ad20b83133ca743af4d3bc792710e351c263fd7212aafa5`, matching the v2 telemetry header `reports/round-50/telemetry/jj-probe-v2.txt:1`.

## Method

Sandbox `/tmp/jjlive-scout21` (deleted after the run), `HOME`/`XDG_CONFIG_HOME` isolated, `GIT_CEILING_DIRECTORIES=/tmp`, bare remote plus `jj git init --colocate`. History: `C0` (base, no receipt) → `C1` (adds `reports/validation.json`), bookmark `main` at `C1`, pushed to the bare remote. Guard run as `python3 tools/harness/receipt_guard.py --repo-root "$PWD" reports/validation.json`. Every command below was executed against the landed bytes (copy in the sandbox), not the lane work tree.

## Required jj states — all hold

| State | Probed refs | Guard exit | committed_sha | landed_ref | landed_sha |
|---|---|---|---|---|---|
| S1 `jj new C1` (HEAD at receipt tip) | HEAD, refs/heads/main, refs/remotes/origin/main | **3** | `2437d90c…` (C1) | `refs/remotes/origin/main` | `2437d90c…` (C1) |
| S2 `jj new C0` (older, receipt only in branches) | refs/heads/main, refs/remotes/origin/main | **3** | `9bc2a660…` (C0) | `refs/remotes/origin/main` | `2437d90c…` (C1, distinct from HEAD) |
| S3 S2 + `REFRESH_RECEIPTS=1` | same | **0** | `9bc2a660…` | `refs/remotes/origin/main` | `2437d90c…` |
| S4 `jj git fetch` after external C2 (receipt retained) | refs/heads/main, origin/main at `d0051707…` | **3** | `9bc2a660…` | `refs/remotes/origin/main` | `d0051707…` |
| S5 S4 + `REFRESH_RECEIPTS=1` | same | **0** | `9bc2a660…` | `refs/remotes/origin/main` | `d0051707…` |
| S6 remote force-rewound to C0, then `jj git fetch` | refs/heads/main, origin/main at `9bc2a660…` | **0** | — | — | — |

Verbatim S2 (the claim's core case):

```
receipt_guard: refusing overwrite path=reports/validation.json committed_sha=9bc2a6608bdcd0a412ec87a102b86f4841c7d6c8
 committed_blob=none landed_ref=refs/remotes/origin/main landed_sha=2437d90cf46345414d36e27ddc8842f230ce1c78
 landed_blob=a849034dfaf2b591f70495af703e979244b8961a hit_refs=refs/heads/main,refs/remotes/origin/main;
 explicit REFRESH_RECEIPTS=1 required [RECEIPT-GUARD-COMMITTED]
exit=3
```

S6 observation (not a claim defect): jj itself moved `refs/heads/main` backwards to C0 and "Abandoned" the receipt commit on the force-rewind fetch, so no probed ref holds the receipt and exit 0 is consistent with the guard's contract; the claim's R2 fixture (receipt still committed on main and origin/main) is not this state.

Attribution rule verified independently in a remote-less repo: with the receipt only on `refs/heads/main` (S7-style `jj new` cases), the guard exits 3 with `landed_ref=none landed_sha=none hit_refs=refs/heads/main`; with HEAD at the receipt commit, `landed_ref=none hit_refs=HEAD,refs/heads/main`. `landed_*` never came from HEAD or a local branch. An uncommitted receipt snapshotted into the jj working copy (kept at `refs/jj/keep/…`) is ignored and allowed, exit 0.

## Counterexample: `HEAD -> refs/jj/root`

Reachable via `jj new 'root()'` in a colocated repo (and in a fresh `jj git init --colocate` repo after `jj bookmark create main` at the initial working-copy commit). With `refs/heads/main` and `refs/remotes/origin/main` both holding the receipt `2437d90c…`:

```
$ cat .git/HEAD
ref: refs/jj/root
$ git symbolic-ref HEAD
refs/jj/root
$ git rev-parse HEAD; echo $?
fatal: ambiguous argument 'HEAD': unknown revision or path not in the working tree.
128
$ python3 tools/harness/receipt_guard.py --repo-root "$PWD" reports/validation.json
receipt_guard: cannot determine committed status: HEAD names 'refs/jj/root', not a local branch [RECEIPT-GUARD-GIT]
exit=3
```

The same hard error occurs for a brand-new path that no ref holds (`reports/round-50/validation.json`, exit 3), i.e. the guard's documented positive behavior (new untracked receipt allowed; probe P2) is refused in this state.

Why: `_head_state` raises at `tools/harness/receipt_guard.py:83` before `_enumerate_refs` is reached (`:194-195`, `for-each-ref` at `:103`). That contradicts the module contract at `:10-11` ("The committed probe covers HEAD and every direct refs/heads/* and refs/remotes/* ref") and the claim's "reports a landed (branch/remote) sha distinct from the local HEAD". No committed_sha/landed_ref/landed_sha fields are emitted at all (`:211-214`).

`refs/jj/root` is jj's sentinel for a working copy whose parent is the root commit; `git rev-parse HEAD` cannot resolve it, and jj writes it as symbolic HEAD while real refs remain. The landed jj-colocation probe never invokes jj (`reports/round-50/jj-colocation-probe.py:7`), so its positive set cannot represent this state; its `0/4` false positives is fixture-scoped.

## Smallest fix (validated in a /tmp copy)

In `_head_state`, before line 83:

```python
if branch == "refs/jj/root":
    return None, None
```

With that copy:

- receipt path: exit 3 with `committed_sha=none landed_ref=refs/remotes/origin/main landed_sha=2437d90c… landed_blob=a849034d… hit_refs=refs/heads/main,refs/remotes/origin/main [RECEIPT-GUARD-COMMITTED]`;
- brand-new path: exit 0;
- `--selftest`: 69/69 controls pass (`selftest_passed: true`).

The selftest contains no real-jj fixture; adding one control whose `.git/HEAD` is `ref: refs/jj/root` with a receipt at `refs/remotes/origin/main` (and one with a fresh path) would lock the fix.

## Limits / notes

- Read-only attack; only this report was written under the lane. No lane files, jj state, or git index touched.
- No tool installs or updates were needed.
- Scope: jj 0.45.1, git 2.56.0. The `refs/jj/root` sentinel is jj-version-specific naming; the failure mode (symbolic HEAD outside `refs/heads`) is the general seam.
- `AUTHOR-LANE ADVICE, NOT ADMISSION.`
