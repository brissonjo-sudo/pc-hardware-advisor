---
description: "Resale of an owned part (French): the estimate rests on sold prices of the user's region, asks for a screenshot when sites are tier B, and never uses a new price as a used value."
expected_outcome: "A dated range labelled sold or asking with its source and confidence, or a plain statement that no sold data was read with a request for a screenshot; no new-retail price presented as the used value."
tags: [plan-upgrade, resale, used, fr]
model: sonnet
runs: 1
max_turns: 50
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch]
---

Je remplace ma carte graphique et je veux revendre l'ancienne : une NVIDIA GeForce RTX 3070 Founders Edition achetée en 2021, avec sa boîte, jamais utilisée pour miner. Combien je peux en espérer en France ?
