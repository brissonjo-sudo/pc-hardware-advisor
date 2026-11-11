# Price-history sources (checked 2026-11-11)

Used by `find-deals` for the Context line only. History figures are context, never an offer price, never in a price table, the verdict or the gap (`research-method.md` section 11, item 8 exception).

## Usable

| Site | Category | What it shows | Scope | Access | Limits | Confidence | Source |
|---|---|---|---|---|---|---|---|
| GPUPrix | Graphics cards | Used: 3-month and 12-month medians, 12-month low, update date. Never used: its current lowest price and its offers (they can come from Amazon) | Per chip, not per exact model; history "aggregated from listings tracked at Alternate and LDLC" (page text, France) | Statistics in the page text; robots.txt allows product pages (disallows /api/, /admin/) | Affiliate site; its daily offers can come from Amazon, so read only the history statistics, never its offers (Amazon is read only through the browser fallback, D50). No terms of use found, which is not a permission. Do not repeat its editorial advice ("good time to buy"). | medium | [1], [2] |

How to read it: open `https://gpuprix.com/fr/france/gpus/<chip-slug>` for France (for example `geforce-rtx-5070`). Record the 3-month median, the 12-month median, the 12-month low, the update date and the retailers named. Never record its current lowest price. If the page is blocked or the figures are missing, write "history not available" and continue: the answer works without it.

## Not usable

| Site | Reason | Source |
|---|---|---|
| leDénicheur (PriceSpy France) | Terms of use, art. 4.3 d: using a robot or any means to retrieve or index the site's content is forbidden without the prior express authorisation of Prisjakt France (read 2026-11-11) | [3] |
| Keepa, CamelCamelCamel, Dealabs | robots.txt: `User-agent: ClaudeBot`, `Disallow: /` (read 2026-11-10 and 2026-11-11). Dealabs deals pasted by the user are read as pasted text only. | [4], [5], [6] |
| The Ramageddon (memory) | History starts 2026-10-13, under 3 months: not used before mid-January 2027 | [7] |
| Idealo | Not verified: the fetch tool refused the site | n/a |

## Not verified

- GPUPrix terms of use: none found. Whether its 12-month statistics include Amazon offers is not stated on the France page (it names Alternate and LDLC).
- No history source found for processors, memory, SSDs or monitors in France.

## Sources

1. GPUPrix, GeForce RTX 5070, France (read in the browser 2026-11-11): https://gpuprix.com/fr/france/gpus/geforce-rtx-5070
2. GPUPrix robots.txt (read 2026-11-11): https://gpuprix.com/robots.txt
3. leDénicheur, conditions générales d'utilisation, art. 4.3 d (read in the browser 2026-11-11): https://ledenicheur.fr/information/conditions-generales-dutilisation
4. Keepa robots.txt (read 2026-11-11): https://keepa.com/robots.txt
5. CamelCamelCamel France robots.txt (read 2026-11-11): https://fr.camelcamelcamel.com/robots.txt
6. Dealabs robots.txt (read 2026-11-11): https://www.dealabs.com/robots.txt
7. The Ramageddon (read 2026-11-11): https://theramageddon.com/
