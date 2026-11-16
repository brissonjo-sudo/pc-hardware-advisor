---
type: llm
weight: 2
---

Look only at deals that get a price verdict (good price, market price, dearer) against a reference labelled same chip / other brand. For each such deal, PASS if the answer shows (in the Compared line, the notes or the Sources) that the chip's listing, meaning a category or filter page for that chip such as an "RTX 5080" list, was read at at least 3 retailers, or states that fewer retailers sell the chip. Product pages of single models do not count as listings. Listings of other retailers that were not read do not matter once 3 were read. Also PASS if no deal gets a price verdict against a same-chip reference (for example all are marked not verified). FAIL if such a verdict is given while fewer than 3 chip listings were read (without saying fewer retailers sell the chip), or while the answer says the chip listings were not read.
Formatting does not matter: only substance decides.
