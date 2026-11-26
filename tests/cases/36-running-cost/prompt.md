---
description: "Yearly electricity cost of an owned PC (French): plan-upgrade shows the formula, takes hours and price from the user or a dated official tariff, and never treats rated power as an average."
expected_outcome: "The answer shows watts x hours / 1000 x price, sources the price per kWh (user or dated regulated tariff), labels rated GPU or CPU power as an upper bound, and gives an estimate."
tags: [plan-upgrade, power, cost, fr]
model: sonnet
runs: 1
max_turns: 50
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch]
---

Mon PC : Ryzen 7 7800X3D, RTX 4070 Super, alimentation Corsair RM750e (80 PLUS Gold). Je joue environ 4 heures par jour, tous les jours. Combien ça me coûte par an en électricité ?
