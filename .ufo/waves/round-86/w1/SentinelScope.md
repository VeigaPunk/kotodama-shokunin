# SentinelScope — r86-v1

Axes: depth + operability. Lane review only; freshness pause unchanged; no planner/validator exception adjudicated.

Full scoped findings: `.ufo/waves/round-86/w1/stage/SentinelScope/sentinel.md`.
Receipts: same directory `cli-probes.json`, `capture-audit.json`, `capture-notes.md`.

Candidate reviewed: `stage/ExecParagraph/check-paragraph-locator.py`, SHA-256 `85c8c70f7959e4e4059b1421f06337ecfa898a0cf30a43364e63c2a98e43a61f`.

- **Low:** local non-regular or oversized `--html` input can stall/exhaust resources [INFERENCE]; direct unbounded `read_text` at line 190. Not operationalized. Smallest mitigation: document trusted regular-file input; constrain opened file type/size if untrusted-path operation is intended.
- **Informational:** caller-chosen local paths/symlinks are not confined; own-scratch symlink reads successfully, missing/directory errors expose supplied path. Not a remote service or sandbox. Future wrappers must constrain input paths.
- **Observed:** 14 bounded subprocess checks returned expected exits without tracebacks; all preserved own-scratch snapshots. Missing/directory/invalid-UTF8 and argument/work refusals produce `PARAGRAPH_ERROR` exit 2; normal/symlink 0; mismatch/absent 1. Embedded NUL was refused by subprocess before candidate launch and is not counted as a pass.
- **Capture boundary:** five capture hashes recorded, strict UTF-8 OK; bounded scan found no credential headers/assignments or private IPv4/localhost URL targets. Anonymous MediaWiki token placeholders are not observed authenticated credentials. Public capture content is not proof of original fetch redirects/authentication; no bypass/provenance assertion made.
- **Static:** normal CLI has no mutation/network/shell/git behavior; selftest is explicit temporary write mode with argv subprocesses and cleanup. Selftest/counter/build/lint/formatters not run. Counter selftest commits fixtures, prohibited here.

No remediation, production edits, commits, installs, network requests, private-target probes or continuity certification. Own scratch removed after receipts copied to stage. Main retains semantic-scope and acceptance/authority judgment.

Report: .ufo/waves/round-86/w1/SentinelScope.md
