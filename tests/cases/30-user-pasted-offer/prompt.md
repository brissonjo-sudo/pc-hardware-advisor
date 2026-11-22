---
description: "Offer text pasted by the user (French): hunt-prices keeps it at medium confidence at best, never adds to a cart to read shipping, and gives no guessed URL."
expected_outcome: "The pasted Amazon UK offer is cited as user-supplied text with medium confidence at best; shipping of other offers comes from pages read, never from a cart."
tags: [hunt-prices, confidence, user-supplied, fr]
model: sonnet
runs: 1
max_turns: 50
timeout_seconds: 1800
allowed_tools: [Read, Glob, Grep, Skill, Agent, WebSearch, WebFetch, ToolSearch]
---

J'ai copié ce matin le texte de l'offre sur Amazon.fr : « Lian Li UNI FAN CL Wireless Reverse Blade 120 mm blanc, pack de 3 avec contrôleur. 64,12 €. Livraison GRATUITE vendredi 27 novembre. Expéditeur : Amazon UK. Vendeur : Amazon UK. Le prix d'expédition comprend les frais d'importation et de manutention douanière. » Trouve-moi le meilleur prix livré en France pour ce pack.
