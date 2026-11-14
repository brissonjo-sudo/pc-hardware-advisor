---
description: "Compatibility check with a single 16 GB DDR5 module on LGA1851 (French)."
expected_outcome: "check-compatibility used; the single module is flagged as single channel with a sourced penalty, and two modules are recommended."
tags: [check-compatibility, memory, fr]
model: sonnet
runs: 1
max_turns: 40
timeout_seconds: 1500
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, Write, ToolSearch]
---

Vérifie la compatibilité de ma config jeu : Core Ultra 5 250K Plus, carte mère B860 ATX, une seule barrette DDR5 16 Go 5600 MT/s (je rajouterai une deuxième plus tard), RTX 5070 et alimentation 750 W. Je joue en 1080p. Tout est bon ?
