---
description: "Pasted deal list (French) with the largest discounts on Amazon and AliExpress: keep by claimed discount, not by readability; no verdict on a processor of unknown packaging."
expected_outcome: "Amazon and AliExpress offers kept (read through the browser or listed as unreadable with a browser offer); lower-discount offers not checked; no good-price verdict on the Ryzen without its packaging read."
tags: [find-deals, list, selection, fr]
model: sonnet
runs: 1
max_turns: 60
timeout_seconds: 2400
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch, Write]
---

Voici une sélection Black Friday copiée d'un site de bons plans. Analyse les deals.

« - Boîtier NZXT H9 Flow à 109,90 € au lieu de 179,90 € sur Amazon (-39 %)
- Processeur AMD Ryzen 7 5700X à 139 € au lieu de 309 € sur AliExpress (-55 %)
- Watercooling MSI MAG Coreliquid I240 à 59,99 € au lieu de 109,99 € sur Amazon (-45 %)
- Alimentation Cooler Master Elite Gold 750 à 69,99 € au lieu de 84,99 € chez Fnac (-18 %)
- Boîtier Lian Li Lancool 217 à 103,99 € au lieu de 129,99 € chez Cdiscount (-20 %)
- SSD Crucial P310 1 To à 59,99 € au lieu de 69,99 € chez LDLC (-14 %)
- Mémoire Corsair Vengeance 2 x 16 Go DDR5 à 99,99 € chez Fnac »
