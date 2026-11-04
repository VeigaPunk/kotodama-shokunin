# SentinelScope — round 86 v1

Axes: **depth + operability**. Review-only lane seat, not external admission. Inherited freshness pause unchanged. L1 remains canonical planner under explicit validator-role prohibition; this report does not adjudicate an exception.

## Audited surface and evidence

Read frozen `reports/round-86/claims.json` and `measure86.py`, source-map.json, five evidence captures, and staged `ExecParagraph/check-paragraph-locator.py` lines 1–206. Candidate SHA-256: `85c8c70f7959e4e4059b1421f06337ecfa898a0cf30a43364e63c2a98e43a61f`.

Receipts in this directory: `cli-probes.json` (14 observed subprocess results, plus one harness-refused unexecuted case), `capture-audit.json` (five capture hashes/strict UTF-8/credential-pattern scan), `capture-notes.md` (provenance limitations).

## Findings

### Low — unbounded/non-regular local input can stall invocation

- Exploit path: an operator supplies a named pipe as `--html`, or a disproportionately large local HTML file. No pipe/resource-exhaustion scenario was executed.
- Evidence: candidate line 190 calls `Path.read_text(encoding='utf-8')` directly; there is no regular-file/size check or normal-mode read deadline. The CLI contains no network retrieval; this requires control of a locally supplied path.
- Impact: [INFERENCE] waiting on a pipe or excessive memory/time, not remote code execution or filesystem mutation. Relevant only if callers treat untrusted path records as safe batch work. Frozen specification has no size ceiling; this is a residual operability limitation, not an asserted frozen predicate failure.
- Smallest remediation: document trusted regular-file input; if untrusted-path operation is intended, open nonblocking, verify the opened descriptor is regular, then enforce a documented byte cap. Do not claim a security sandbox around arbitrary paths.

### Informational — local path access is unrestricted by design

- Exploit path: a caller passes an accessible path or symlink outside its intended capture directory.
- Evidence: candidate lines 169, 190 accept a Path and read it without confinement. An own-scratch symlink to own-scratch HTML passed with exit 0. Errors for missing/directory inputs include the supplied absolute path.
- Impact: [INFERENCE] a service wrapper accepting remote path input would expose existence/error details and quote-containment verdicts about caller-accessible files. This local CLI is not such a service, does not print file contents, and is not advertised as confined.
- Smallest remediation: no mandatory CLI change for the present local interface; any future wrapper must constrain inputs before calling it. Never route private targets into capture jobs.

## Observed path/refusal/UTF-8/error behavior

Fourteen bounded real CLI invocations completed with expected exits: normal and own-scratch symlink input 0; wrong ordinal and absent quote 1; missing path, directory input, invalid UTF-8, empty quote, invalid ordinal, unknown option, mixed modes, missing/non-directory work, and locator-with-work 2. All observed input/argument failures had `PARAGRAPH_ERROR`, no traceback. Every invocation preserved the exact own-scratch file/directory/symlink content snapshot. This is scoped mutation evidence, not whole-host syscall tracing.

The embedded-NUL argv scenario never reached the candidate: Python's subprocess layer refused it before launch. The harness initially raised `ValueError: embedded null byte`; remaining cases were then completed without rerunning the seven already completed cases. Receipt explicitly records this limitation, not a candidate pass.

Static review: ordinary mode has no write call, subprocess, shell execution, git operation or network import. HTML scripts/URLs are parsed as data, not evaluated or fetched. Quotes are argv entries, not command fragments; verdict quotes use repr. `--selftest` is the explicit write mode: temporary directory below supplied existing `--work`, sequential subprocess argv with `-B`, own case cwd, 10-second child timeout, context-managed cleanup (lines 107–163). I did not run selftest, induce permission failures, kill processes, or exercise races/non-regular input. No build/lint/formatter/counter execution occurred.

## Capture credentials and ordinary access

All five local captures decoded strictly as UTF-8. Bounded scans found no authorization/cookie headers, credential assignments, or localhost/private-IPv4 URL targets. Three HTML captures contain `wgUserName:null` and anonymous MediaWiki token placeholders `+\\`, not observed authenticated credentials. Historical `bearer` words in book OCR are not authorization tokens. Source-map URLs are public HTTPS Wikisource pages and archive.org download endpoints; HTTPS here is ordinary public HTTP access, not a private transport exception.

No network request, login, CAPTCHA/paywall bypass, credential read, install/update, or private-target probe was attempted. Existing public-page captures cannot independently establish original redirect/authentication history; this seat does not fabricate that provenance. Scan absence is not an exhaustive proof that arbitrary personal data is absent.

## Contract boundaries

No production/frozen/counter/git/index/fleet/sibling file was changed. Only own stage, explicit report trailer, and own scratch were written. Frozen counter selftest visibly initializes/configures/commits fixtures (measure86.py:118–145), so it was not run. Normal counter evaluates executable tool bytes; its success would not itself establish confinement. No `resume_continuity_v1` implementation or rejection surface exists in the assigned CLI/capture slice; no continuity behavior is certified.

No remediation edits were authorized or made. Main should retain these limitations when integrating the candidate and separately assess semantic paragraph scope; the frozen acceptance/authority judgment remains outside this seat.

Self-evaluation: accuracy 4 (static risks explicitly inferred); completeness 4 (no syscall trace or permission/race probe); clarity 4 (findings separated from observations); actionability 4 (minimal containment boundary stated); conciseness 4 (receipts hold raw outputs). Mean 4.0. Most valuable improvement is a caller-level regular-file policy if this local CLI is ever exposed to untrusted paths; current findings do not justify extra network/security machinery.

Report: .ufo/waves/round-86/w1/SentinelScope.md
