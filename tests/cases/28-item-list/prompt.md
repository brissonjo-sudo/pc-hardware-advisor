---
description: "A list of three parts, one in white (French): hunt-prices keeps the named variant, one seller per row and a total on a stated basis."
expected_outcome: "A best-offer-per-item table with the white Crucial kit (U5W) or no RAM row, one seller per row, and any total saying what it includes."
tags: [hunt-prices, list, variant, fr]
model: sonnet
runs: 1
max_turns: 80
timeout_seconds: 2400
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch]
---

Trouve le meilleur prix livré en France, en neuf, pour cette liste :
1. Crucial Pro 2x16 Go DDR5-6000 CL36 blanche (CP2K16G60C36U5W)
2. Kioxia Exceria Plus G3 2 To
3. Lian Li DAN A3 noir
