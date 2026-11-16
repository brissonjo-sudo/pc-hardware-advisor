---
description: "Short fitness-for-AI question with an eBay listing link (French): review-used-listing is used, not only size-local-ai; the tier B listing is not read; the verdict template is kept."
expected_outcome: "review-used-listing used; the eBay listing is not fetched nor opened in the browser; the answer asks for the listing text or a screenshot and gives dated market prices."
tags: [review-used-listing, trigger, ebay, ai, fr]
model: sonnet
runs: 1
max_turns: 50
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch]
---

Que penses-tu de cette carte pour un projet IA ? https://www.ebay.fr/itm/128179198855
