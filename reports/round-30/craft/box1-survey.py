#!/usr/bin/env python3
"""Box-1 landed-mode executable inventory: scripts named in SKILL.md must resolve."""
import json, pathlib, re, sys
ROOT = pathlib.Path(__file__).resolve().parents[3]
skill = (ROOT / "SKILL.md").read_text()
named = sorted(set(re.findall(r"tools/[\w./-]+\.py", skill)))
resolvable = [s for s in named if (ROOT / s).is_file()]
out = {"date": "2026-10-18", "named": len(named), "resolvable": len(resolvable),
       "unnamed_in_skill": [s for s in named if not (ROOT / s).is_file()],
       "skill_sha256": __import__("hashlib").sha256((ROOT/"SKILL.md").read_bytes()).hexdigest()}
print(json.dumps(out, indent=1))
sys.exit(0 if len(resolvable) == len(named) else 1)
