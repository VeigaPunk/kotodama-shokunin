import { SWARM_ROLES, planSwarmWave, SwarmWaveError } from "/home/vgpnk/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs";
import fs from "node:fs";
console.log("SWARM_ROLES size=", SWARM_ROLES.size, "has(planner)=", SWARM_ROLES.has("planner"));
const specPath = "/home/vgpnk/Projects/shokunin/kotodama-shokunin/.ufo/waves/round-77/w1/spec.json";
const spec = JSON.parse(fs.readFileSync(specPath, "utf8"));
const clone = JSON.parse(JSON.stringify(spec));
console.log("control: real spec items=", clone.items.length, "roles=", [...new Set(clone.items.map(i=>i.role))].join(","));
try {
  const plan = planSwarmWave(clone);
  console.log("control: planSwarmWave(real spec) OK agents=", (plan.agents||plan.items||[]).length);
} catch (e) {
  console.log("control: planSwarmWave(real spec) THREW", e.constructor.name, e.code || "", String(e.message).slice(0,200));
}
const mut = JSON.parse(JSON.stringify(spec));
mut.items[0].role = "planner";
try {
  planSwarmWave(mut);
  console.log("mutant: planSwarmWave(items[0].role=planner) ACCEPTED (no refusal)");
} catch (e) {
  console.log("mutant: planSwarmWave(items[0].role=planner) REFUSED", e.constructor.name, "code=" + (e.code || ""), "|", String(e.message).slice(0,160));
}
