---
description: "Fans on a named motherboard (French): check-compatibility checks the current per header against the board manual, not only the header count."
expected_outcome: "The answer compares the fans' rated current or power on each header with the per-header limit of the exact board (or marks that limit not verified), and gives a PSU-powered option for a group over the limit."
tags: [check-compatibility, fans, power, fr]
model: sonnet
runs: 1
max_turns: 50
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch]
---

J'ai une carte mère ASUS ROG Strix B850-G Gaming WiFi. Je veux brancher 3 ventilateurs Lian Li UNI FAN TL Wireless Reverse en chaîne sur un seul connecteur CHA_FAN, et 2 Lian Li UNI FAN TL120 sur un autre. Ma carte mère les supporte ?
