---
description: "Airflow layout on request (French): check-compatibility places fans and a 360 mm AIO from the case manual, keeps the pump below the radiator top and presents case pressure as a trade-off."
expected_outcome: "One row per position with intake or exhaust and a sourced reason; the case's supported positions come from its manual or are marked not verified; no bottom-mounted radiator; pressure given as a trade-off without figures."
tags: [check-compatibility, airflow, cooling, fr]
model: sonnet
runs: 1
max_turns: 50
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch]
---

J'ai un boîtier Fractal Design North, un watercooling Arctic Liquid Freezer III 360 et six ventilateurs 140 mm en plus de ceux du radiateur. Où je mets le radiateur et dans quel sens je monte chaque ventilateur ? Mieux vaut une pression positive ?
