#!/usr/bin/env bash
# Round-69 wave dispatcher (kotodama r69-w1).
#
# The Kimi L1 seat exposes no AgentSwarm/task tool, so the validator's ONE
# rendered taskCall (32 spawn lanes) is dispatched as 32 concurrent headless
# `kimi --prompt` sessions. Each seat receives taskCall.context followed by
# its own task text verbatim; the only edit is the insertion of the godspeed
# directive bytes after the renderer-injected `/skill:godspeed` line (the
# documented host substitution for substrates that inject nothing).
#
# The parent stays alive until every seat settles: this script waits for all
# children and writes a settlement receipt. Never use `--auto`.
set -u

LANE=/home/vgpnk/Projects/shokunin/kotodama-shokunin
W1="$LANE/.ufo/waves/round-69/w1"
TASKCALL="$LANE/.ufo/waves/round-69/taskcall-v1.json"
DIRECTIVE=/home/vgpnk/.agents/skills/godspeed/directive.md
SEAT_TIMEOUT=${SEAT_TIMEOUT:-1500}

mkdir -p "$W1/stdout" "$W1/prompts"

python3 - "$TASKCALL" "$W1/prompts" "$DIRECTIVE" <<'PY'
import json, sys, os
tc = json.load(open(sys.argv[1]))
outdir = sys.argv[2]
directive = open(sys.argv[3], encoding="utf-8").read().strip()
ctx = tc["taskCall"]["context"]
for t in tc["taskCall"]["tasks"]:
    task = t["task"]
    if task.startswith("/skill:godspeed"):
        task = "/skill:godspeed\n\n" + directive + "\n\n" + task[len("/skill:godspeed"):].lstrip("\n")
    prompt = ctx + "\n\n---\n\n" + task
    with open(os.path.join(outdir, t["name"] + ".txt"), "w", encoding="utf-8") as fh:
        fh.write(prompt)
print("prompts_written", len(tc["taskCall"]["tasks"]))
PY

start=$(date +%s)
pids=()
for f in "$W1"/prompts/*.txt; do
    name=$(basename "$f" .txt)
    (
        cd "$LANE" || exit 2
        timeout --signal=TERM "$SEAT_TIMEOUT" kimi --prompt "$(cat "$f")" \
            > "$W1/stdout/$name.txt" 2> "$W1/stdout/$name.err"
        echo "$?" > "$W1/stdout/$name.rc"
    ) &
    pids+=("$!")
done
echo "dispatched ${#pids[@]} seats at $(date -Iseconds)"

for p in "${pids[@]}"; do
    wait "$p" || true
done
end=$(date +%s)
settled=$(ls "$W1"/stdout/*.rc 2>/dev/null | wc -l)
alive=$(ls "$W1"/*.md 2>/dev/null | wc -l)
{
    echo "wave=kotodama-r69-v1 seats=${#pids[@]} settled=$settled reports=$alive"
    echo "start=$start end=$end wall_seconds=$((end-start))"
    for f in "$W1"/stdout/*.rc; do
        n=$(basename "$f" .rc)
        printf '%s rc=%s report=%s\n' "$n" "$(cat "$f")" \
            "$( [ -f "$W1/$n.md" ] && echo yes || echo no )"
    done
} > "$W1/settle.tsv" 2>&1
echo "settled: $(cat "$W1/settle.tsv" | head -2)"
