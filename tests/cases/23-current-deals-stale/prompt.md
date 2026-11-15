---
description: "Current graphics-card deals (French): ended deals are named without price; exactly one next action."
expected_outcome: "find-deals used; no price shown for a deal older than 7 days; exactly one next action."
tags: [find-deals, current-deals, gpu, fr]
model: sonnet
runs: 1
max_turns: 50
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch, Write]
---

Quels sont les bons plans cartes graphiques en ce moment en France ? Dis-moi lesquels sont vraiment de bons prix.
