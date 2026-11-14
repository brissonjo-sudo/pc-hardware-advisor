---
description: "No deal in hand (French): find the current SSD deals on a readable deal list, keep recent ones, verify on retailer pages."
expected_outcome: "find-deals used; deals taken from a readable deal list with its date; only recent deals kept; prices read on retailer pages or marked not verified."
tags: [find-deals, current-deals, fr]
model: sonnet
runs: 1
max_turns: 60
timeout_seconds: 2400
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch, Write]
---

Quels sont les bons plans SSD en ce moment en France ? Dis-moi lesquels sont vraiment de bons prix.
