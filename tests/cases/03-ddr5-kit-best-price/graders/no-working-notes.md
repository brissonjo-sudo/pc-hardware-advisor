---
type: llm
weight: 1
---

PASS if the final answer starts with the result (a price, a verdict, or a clear statement that nothing usable was found) and has none of the failures below.

These are allowed and do not cause a FAIL: saying which pages were read, not read or blocked; saying why the search stopped, in plain words ("I stopped after reading the French retailers on the list"); first-person explanations of a gap or a check ("I read LDLC twice and no seller line appears"); stated assumptions; the Sources list, including the plugin's reference files.

FAIL only if one of these appears:
- a progress or waiting message, in any language, such as "two batches of three are back", "waiting for the last batch", "I am loading the skill", "the second agent has finished";
- an internal rule cited by its number instead of its meaning, such as "condition 3" or "stopping rule 2";
- an amount without a currency, such as "149,90" alone.

Formatting does not matter: only substance decides.
