# Round 50 FALSIFY — receipt guard symbolic-ref bypass

**Item attacked:** O operability — `tools/harness/receipt_guard.py` at `1c779e4a316efcbfbcba54cb8b2a1e0dda2353d0`  
**Verdict:** **BROKEN**  
**Severity:** **MEDIUM** — a valid symbolic ref in either protected namespace lets a caller using the guard overwrite a committed receipt without the required explicit refresh setting.

## Exploit path

`_enumerate_refs` documents that symbolic refs are skipped because they duplicate their targets (`tools/harness/receipt_guard.py:99-101`), then unconditionally skips every listed ref with a nonempty `symref` (`:122-124`). A `refs/heads/*` or `refs/remotes/*` symbolic ref can instead point outside both enumerated namespaces, e.g. to `refs/tags/filed`. The target commit is not independently enumerated, so the receipt-bearing commit is omitted from `tips` and the guard allows the write.

A caller can create the state with `git symbolic-ref refs/remotes/origin/main refs/tags/filed` (or `git symbolic-ref refs/heads/sneaky refs/tags/filed`). The detached `HEAD` is at a commit with no receipt; the tag target is a commit containing `validation.json`. The symbolic ref resolves successfully and is listed by Git, but is discarded by the guard.

## Evidence

All reproductions used a disposable `/tmp` clone checked out at the exact landed commit, with `GIT_CEILING_DIRECTORIES=/tmp`; synthetic commits/refs and writes were confined to that clone. `REFRESH_RECEIPTS` was explicitly absent in the clean-environment attack runs. The private clones were removed afterward; no lane files or Git metadata were changed.

- Landed selftest: `python3 tools/harness/receipt_guard.py --selftest` → **exit 0**, **69/69 controls passed**. The suite does not cover a scoped symbolic ref targeting a commit outside `refs/heads/*` and `refs/remotes/*`.
- Direct-ref control: a direct `refs/remotes/origin/main` to the receipt-bearing commit → **guard exit 3**, stderr included `RECEIPT-GUARD-COMMITTED`, `landed_ref=refs/remotes/origin/main`, and `landed_sha=457cfb32cb8f3fbaa310b7530eb514711d75b112`.
- Symbolic-ref attack: `git symbolic-ref refs/remotes/origin/main refs/tags/filed` → **exit 0**. `for-each-ref` reported `refs/remotes/origin/main\0 457cfb32cb8f3fbaa310b7530eb514711d75b112 \0 commit \0 refs/tags/filed`. The detached HEAD was `9489a228e7ba5f9fec3febe81277204e03cd9ff4` and had no `validation.json`; the target commit had `100644 blob 203e7040e2403ebf33b440ca1c851cb8f744893f validation.json`.
- With that state, the landed CLI `receipt_guard.py --repo-root <fixture> <fixture>/validation.json` returned **exit 0**, empty stderr. The same result occurred with `refs/heads/sneaky` symbolic to `refs/tags/filed`.
- End-to-end runner attack, still with no `REFRESH_RECEIPTS`: `round_runner_main(measure, path, repo_root=fixture, write_receipt=publish)` returned the publisher's **exit 7**, stdout `MEASURED\nPUBLISHED`, empty stderr, and the receipt bytes became `replacement\n`. Both guard checks therefore passed before publication.

## Impact and smallest remediation

A committed receipt held only through a symbolic ref in either protected namespace can be overwritten by the normal guarded runner, bypassing the intended `REFRESH_RECEIPTS=1` gate. This is an operability/integrity defect; no live repository access, credentials, or network were involved.

Resolve and account for every in-scope symbolic ref's commit target. Skip it as a duplicate only after establishing that its resolved target is already covered by the enumerated protected refs; otherwise include its resolved commit in the receipt check (and fail closed on unresolved targets where their safety cannot be established). Add regression cases for both remote-tracking and local-branch symrefs pointing to a receipt-bearing tag/out-of-scope ref, including the `round_runner_main` publication path.
