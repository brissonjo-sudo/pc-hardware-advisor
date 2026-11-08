---
type: llm
weight: 1
---

PASS if the cell values of the price table (seller type, landed or "excluding fees", stock, confidence) are written in French, for example "revendeur direct", "hors frais", "en stock", "moyenne". Part names, SKUs, units, URLs and shop names may stay as written. FAIL if English headers or labels such as "Landed", "direct retailer", "excluding fees", "in stock (shown)" or "medium" appear in the French answer's table.
If the answer has no price table, PASS. Formatting does not matter: only substance decides.
