---
description: "Upgrade advice for an owned PC (French): plan-upgrade names the limiting part with evidence, checks the upgrade against the parts kept, and states what the platform allows."
expected_outcome: "The GPU (or the part shown by the evidence) is named as the limit with its evidence and confidence; the proposed upgrade is checked against the board, PSU and case; the LGA1200 platform limit is stated; no unsourced fps gain."
tags: [plan-upgrade, upgrade, bottleneck, fr]
model: sonnet
runs: 1
max_turns: 50
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch]
---

J'ai un PC avec un Intel Core i5-10400F, une carte mère MSI B460M-A PRO, 16 Go de DDR4-2666 (deux barrettes), une GTX 1660 Super, une alimentation be quiet! System Power 10 550 W et un boîtier Cooler Master MasterBox Q300L. Je joue en 1440p et ça rame. Je change quoi en premier ?
