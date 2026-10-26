#!/usr/bin/env python3
"""Fifth pre-freeze correction: pin map.sha256; LEDGER wording states the pattern-operand reading ExecCaFix implemented (7.3)."""
import json, hashlib
L = "/home/vgpnk/Projects/shokunin/kotodama-shokunin"
P = f"{L}/reports/round-75/claims.json"
c = json.load(open(P)); C, A = c["claims"]
C["map"]["sha256"] = hashlib.sha256(open(f"{L}/.ufo/waves/round-75/assimilation/id-renumber-map.json", "rb").read()).hexdigest()
i = next(k for k, l in enumerate(A["legs"]) if l.startswith("LEDGER:"))
old = "and shell metacharacters;"
assert A["legs"][i].count(old) == 1, A["legs"][i][:900]
A["legs"][i] = A["legs"][i].replace(old, "and shell metacharacters in any argv element other than a regex-pattern operand (the argv is never shell-parsed, so a backtick or `\\|` inside a `-E` pattern is data; a metacharacter in the executable position or in a non-pattern operand fails);")
c["pre_data_corrections"].append({"id": "W2-F5", "by": "ExecCaFix 7.3, ScribeScorecardFinal", "fix": "LEDGER states the pattern-operand reading (pairs L75-04..07 carry a backtick or an escaped pipe inside a -E pattern); map.sha256 pinned."})
json.dump(c, open(P, "w"), ensure_ascii=False, indent=1); print(C["map"])
