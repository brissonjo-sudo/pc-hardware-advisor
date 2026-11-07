---
type: llm
weight: 2
---

PASS if the answer gives a tokens/s estimate for a 32B Q4 model on an RTX 3090, explains that decode speed is driven mainly by memory bandwidth (about 936 GB/s), labels the figure as an estimate, and the figure is plausible (roughly 15 to 40 tok/s decode). FAIL if no estimate, or a figure presented as measured without source.
Formatting does not matter: only substance decides.
