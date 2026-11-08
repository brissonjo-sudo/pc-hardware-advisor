---
description: "Schedule tracking of used RTX 3090 below 800 EUR (French)."
expected_outcome: "Scheduled task created or exact setup given, history initialised, no purchase action."
tags: [track-price, fr]
model: sonnet
runs: 2
max_turns: 40
timeout_seconds: 1500
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, Write, ToolSearch, CronCreate, CronList]
---

Surveille le prix des RTX 3090 d'occasion en France et préviens-moi dès qu'on en trouve une sous 800 €. Vérifie une fois par jour.
