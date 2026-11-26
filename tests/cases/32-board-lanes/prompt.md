---
description: "Board choice by lanes (French): build-config picks an AM5 board for one GPU and three NVMe drives with the Board lanes criteria, confirmed in the manual."
expected_outcome: "The answer compares candidate boards on CPU-linked M.2 without GPU loss, M.2 total and chipset link, cites the manual (or marks it not verified), and never presents PCIe Simulator as the maker's data."
tags: [build-config, lanes, motherboard, fr]
model: sonnet
runs: 1
max_turns: 50
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch]
---

Je monte un PC AM5 avec un Ryzen 7 9800X3D, une RTX 5080 et trois SSD NVMe. Quelle carte mère choisir pour que la carte graphique reste en x16 et que les trois SSD tournent à pleine vitesse ? Je ne veux pas de prix, juste le choix de la carte.
