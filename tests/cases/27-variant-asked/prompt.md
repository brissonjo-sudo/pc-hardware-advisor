---
description: "A chip sold in two memory sizes, named without the size (French): hunt-prices asks which variant before searching."
expected_outcome: "The answer asks whether the V100 wanted is 16 GB or 32 GB (one grouped question), with no price table built on both."
tags: [hunt-prices, question, variant, fr]
model: sonnet
runs: 1
max_turns: 50
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch]
---

Trouve moi une carte Nvidia V100 reconditionnée ou d'occasion. Je suis en France.
