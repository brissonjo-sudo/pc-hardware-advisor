---
description: "Graphics-card deal whose exact model is out of stock elsewhere (French): the same-chip reference comes from each retailer's chip listing; Sources hold pages, not plugin files."
expected_outcome: "find-deals used; the same-chip reference is the cheapest in-stock RTX 5080 found from retailers' chip listings; Sources list pages read and no bare list of plugin reference files."
tags: [find-deals, reference, gpu, fr]
model: sonnet
runs: 1
max_turns: 50
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch]
---

Bon plan repéré : la Zotac GeForce RTX 5080 SOLID CORE OC (ZT-B50800Q-10P) à 1 799,99 € chez Joybuy.fr. Je ne la trouve en stock nulle part ailleurs en France. Est-ce vraiment un bon prix ?
