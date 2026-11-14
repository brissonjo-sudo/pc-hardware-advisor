---
description: "Single deal on a direct retailer (French): the same-day reference must come from several retailers, listed in a Compared line."
expected_outcome: "find-deals used; reference chosen among at least 3 other direct retailers read (or fewer stated), each named with its price or the reason it was not read."
tags: [find-deals, reference, fr]
model: sonnet
runs: 1
max_turns: 50
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch]
---

Alternate.fr vend le Ryzen 7 9800X3D en boîte à 359 €. C'est un bon prix en ce moment en France ?
