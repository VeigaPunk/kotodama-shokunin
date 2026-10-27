#!/bin/sh
cd /home/vgpnk/Projects/shokunin/kotodama-shokunin && UFO_CONFIG_PATH=/home/vgpnk/Projects/shokunin/scripts/hyaku/ufo-wave-policy.json UFO_FLEET_ALLOW_EXTERNAL_TOOLS=1 UFO_PROJECT_ROOT=/home/vgpnk/Projects/shokunin/kotodama-shokunin node ~/Projects/ufo-fsd-alpha/scripts/ufo-swarm-wave.mjs "$@"
