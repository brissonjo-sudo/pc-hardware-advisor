---
description: "Graphics-card deal whose exact model is out of stock elsewhere (French): the reference falls back to the same chip in stock."
expected_outcome: "find-deals used; out-of-stock offers are not the reference; the cheapest in-stock RTX 5080 of any brand is the reference, labelled same chip; no purchase suggested on a not-verified verdict."
tags: [find-deals, reference, gpu, fr]
model: sonnet
runs: 1
max_turns: 50
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch]
---

Bon plan vu sur un site de bons plans : la Palit GeForce RTX 5080 GamingPro V1 (NE75080019T2-GB2031Y) à 1 799,99 €, vendue par Joybuy.fr, livraison gratuite. Alternate l'affiche à 2 077 € mais en rupture, et je ne la trouve pas ailleurs. C'est une bonne affaire ?
