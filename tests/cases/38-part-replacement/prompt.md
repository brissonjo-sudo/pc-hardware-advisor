---
description: "Replacement and competitor question for a planned part (French): build-config handles it, compares against the planned variant and lists a competitor as equal or better only with figures read for it."
expected_outcome: "build-config is used; the candidate is compared with the reverse TL figures (or the answer says they were not found); every fan called as good as or better than the TL carries its airflow or pressure figures with a cited source."
tags: [build-config, replacement, variants, citations, fr]
model: sonnet
runs: 1
max_turns: 60
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch]
---

Ma config en projet prévoit 6 ventilateurs Lian Li UNI FAN TL reverse blancs (2 packs de 3), livrés en France.
Est-ce que l'AsiaHorse DAWN reverse blanc (pack de 3, 120 mm) peut les remplacer ?
Et en partant du Lian Li TL, quel concurrent est aussi performant ou plus ?
