---
description: "Slot placement on a named board (French): check-compatibility maps each part to a CPU or chipset slot, sourced from the manual first."
expected_outcome: "One row per part with its slot or socket, CPU or chipset link, effect on other ports and source; the GPU x8 trade is stated without an unsourced loss figure."
tags: [check-compatibility, lanes, placement, fr]
model: sonnet
runs: 1
max_turns: 50
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch]
---

J'ai une ASUS ROG Crosshair X870E Hero, une RTX 4080 et deux SSD NVMe PCIe 4.0 (un pour Windows et les jeux, un pour le stockage). Sur quels slots je mets chaque pièce pour ne rien perdre ?
