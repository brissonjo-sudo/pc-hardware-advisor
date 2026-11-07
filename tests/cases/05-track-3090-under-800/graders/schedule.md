---
type: llm
weight: 3
---

PASS if the answer creates a scheduled/recurring task (daily) using an available scheduling tool, OR clearly states that no scheduler is available in this environment and gives the exact task definition to create (frequency, query, threshold, notification rule). FAIL if it claims a task was created without having used a tool to do so.
Formatting does not matter: only substance decides.
