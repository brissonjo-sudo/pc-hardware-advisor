# Power supplies and connectors

Last checked: 2026-11-07 (running cost: 2026-11-26). Values change: verify online before concluding.

Use this file to check PSU wattage, PSU connectors and CPU/GPU power for `check-compatibility`. Every table row carries a source `[n]` and a confidence. Confidence scale: high = vendor or standard primary page read directly; medium = secondary, vendor explainer, Wikipedia or search summary of a vendor page; low = aggregator, forum, retailer, snippet. Report the confidence with the verdict. When a value is missing here, say so and ask for the exact model page; never infer it.

Table date: all rows checked 2026-11-07.

## 1. Connectors and standards

| Item | Value | Source | Confidence |
|---|---|---|---|
| PCIe x16 slot power | Up to 75 W (12 V up to 5.5 A = 66 W, plus 3.3 V up to 3 A = 9.9 W) once configured as high-power device | [1] | medium |
| PCIe 6-pin | +75 W | [1] | medium |
| PCIe 8-pin | +150 W. Sense pins distinguish 6-pin from 8-pin; a 6-pin plug in an 8-pin socket limits the card to 75 W | [1] | medium |
| Real draw of a plug | A 2x4 PCIe plug draws at most 13.5 A (about 162 W at 12 V) over 3 power pins; a 2x3 at most 6.75 A (about 81 W) | [2] | high |
| Card ceiling before CEM 5.0 | 300 W (75 W slot + 75/150 W increments). Cards with two 8-pin (375 W) exist in practice | [2], [1] | high / medium |
| EPS12V CPU (2x4, 8-pin) | Intel guide recommends the PSU support 24-32 A on a 2x4 18 AWG connector and 12-16 A on a 2x2 (4-pin). A board may have one or two CPU connectors (4+4 / 8-pin) | [2] | high |
| 12VHPWR (CEM 5.0) to 12V-2x6 (CEM 5.1) | 12V-2x6 replaces 12VHPWR "to address reliability concerns". Intel: new PSU designs should mount only 12V-2x6; 12VHPWR should be deprecated | [2] | high |
| 12V-2x6 rating | 600 W on the 12 V rail, 16 AWG wire, 9.2 A per pin, four sideband signals (CARD_PWR_STABLE, CARD_CBL_PRES#, SENSE0, SENSE1). Max single-card power raised to 675 W (75 W slot + 600 W cable) | [2] | high |
| 12VHPWR vs 12V-2x6, physical | Changes are on the GPU/PSU sockets (shorter sense pins, longer power terminals); cable and plug are unchanged. Sense pins make contact only when the power pins are fully seated. Markings: "H+" = 12VHPWR, "H++" = 12V-2x6. The exact pin-length values differ between secondary sources | [3], [4], [5], [6] | medium (qualitative), low (mm values) |
| Cable reuse | Corsair: a 12VHPWR cable can stay in use with a 12V-2x6 GPU, the difference is not in the cable. An ATX 3.1 PSU cable on a GPU with an old 12VHPWR socket does not give the shorter-sense-pin protection | [7], [8] | medium |
| Adapters | NVIDIA ships a 3x or 4x 8-pin to 12V-2x6 adapter with FE and many cards. RTX 5090 FE: "4x PCIe 8-pin cables (adapter in box) OR 1x 600 W PCIe Gen 5 cable" (nvidia.com RTX 5090 page, read 2026-11-08). The number of 8-pin plugs used must match the adapter | [13], [14] | high |
| "All RTX 50 use 12V-2x6" (Corsair) | Do not generalise. NVIDIA lists 5060 Ti / 5060 as "1x 8-pin OR 300 W Gen5 cable (adapter in box)" for FE/reference; partner models vary | [7], [15] | medium |

### Sense-pin power table (12V-2x6, Intel guide Table 3-6)

Read SENSE0/SENSE1 as a PSU-side declaration of what the cable may deliver.

| SENSE0 / SENSE1 | Initial W | Sustained W |
|---|---|---|
| Ground / Ground | 375 | 600 |
| Open / Ground | 225 | 450 |
| Ground / Open | 150 | 300 |
| Shorted to each other | 100 | 150 |
| Open / Open | 0 | 0 (card may draw nothing via the connector) |

Source [2], confidence high. Use it to explain "300 W Gen5 cable" vs "450 W+" vs "600 W" wording on NVIDIA pages: the wattage tier of the cable or PSU port must be at least the card requirement.

### ATX 3.0 vs ATX 3.1

| Topic | ATX 3.0 | ATX 3.1 | Source | Confidence |
|---|---|---|---|---|
| GPU connector (PSUs above 450 W) | 12VHPWR | 12V-2x6 | [2], [9] | high / medium |
| Hold-up time | 17 ms required at 100 % load (as in the research: "was 17 ms") | 12 ms required at 100 % load; 17 ms recommended at 80 % load | [2] Table 4-8, [9], [10] | high |
| Alignment | | Guide aligned to PCIe CEM 5.1 (Intel guide Rev 2.1a, Nov 2023) | [2] | high |

Power excursion tolerance of the PSU (Intel Table 3-3), percent of rated power:

| PSU | 100 us | 1 ms | 10 ms | 100 ms | Continuous |
|---|---|---|---|---|---|
| Above 450 W with 12V-2x6 | 200 % | 180 % | 160 % | 120 % | 100 % |
| 450 W or less, or without 12V-2x6 | 150 % | 145 % | 135 % | 110 % | 100 % |

Source [2], high. Card side (CEM 5.1 via Intel Table 3-1): up to 2.5x sustained power on the +12 V connector rail and 3x total card power for 100 us or less, decaying to 1x at 1 s [2], high.

Instruction: when a card is rated 300 W or more, prefer an ATX 3.1 / PCIe 5.1 PSU. This follows the Intel excursion tables; MSI and Corsair advise ATX 3.1 for the RX 9070 XT (secondary, medium) [22]. An ATX 3.0 or older PSU is not automatically incompatible: report "compatible with conditions" and name the missing ATX 3.1 features.

## 2. Safe use of 16-pin connectors (12VHPWR / 12V-2x6)

State who says what; do not present one party's advice as a standard.

| Advice | Who says it | Confidence |
|---|---|---|
| Click/latch fully, no gap, evenly seated | Consensus advice; NVIDIA is reported to say "fully and evenly seated" | medium [11] |
| No bending right at the connector; "at least 35 mm straight before a bend" | Cable makers (CableMod, Corsair listing). NOT from NVIDIA | low-medium [12] |
| Plan about 36 mm of extra space for cables | NVIDIA FE product pages, as recorded in the research (space planning, not a bend radius) | medium [13], [14] |
| Cable plug connection recommendation | Intel guide Fig 5-10, image only, not extracted | [2] |
| Insertion durability | Intel guide tests contact resistance after 30 insertion-removal cycles; Wikipedia says reliability may fall after about 30-40 mating cycles | medium [2], [3] |

Incident record (Wikipedia aggregation, not verified individually) [3], medium: RTX 4090 (2022, partly not fully seated); CableMod adapter recall Feb 2024 (CPSC, 272 reports, about 25,300 units); RTX 5090 FE cases; RX 9070 XT partner-card cases in Aug 2025, including Sapphire Nitro+ owners using non-ATX 3.1 PSUs.

Instructions for Claude:
- Tell the user to seat the plug fully until the latch clicks and to leave straight cable before any bend; attribute the 35 mm figure to cable makers.
- State that no PCI-SIG or NVIDIA bend radius was found. Do not present 35 mm as an official limit.
- Warn about third-party angled adapters (the CableMod recall is the sourced example) and tell the user to check the card and PSU maker manuals.
- In a small case, count cable space as a case-fit condition (see `form-factors-cases.md`).

## 3. GPU power and recommended PSU

NVIDIA "Required System Power" is a minimum, assuming a stated reference CPU (Ryzen 9 9950X for the 50 series; Ryzen 9 5900X on the 4080 page) and a PCIe CEM 5.1 compliant PSU. NVIDIA says it can differ per system. Partner cards often ask for more. All rows checked 2026-11-07.

### NVIDIA official data

| GPU | Board power | Vendor-recommended PSU | Connectors | Source | Confidence |
|---|---|---|---|---|---|
| RTX 3090 (FE) | 350 W | 750 W | 2x 8-pin (adapter to 1x 12-pin included) | [16] | high |
| RTX 3090 Ti (FE) | 450 W | 850 W | 3x 8-pin adapter or 450 W+ Gen5 cable (16-pin) | [16] | high |
| RTX 4070 | 200 W | 650 W | 2x 8-pin adapter or 300 W Gen5 cable; some partner models 1x 8-pin | [17] | high |
| RTX 4070 SUPER | 220 W | 650 W | same as 4070 | [17] | high |
| RTX 4070 Ti / Ti SUPER | 285 W | 700 W | 2x 8-pin adapter or 300 W Gen5 cable | [17] | high |
| RTX 4080 | 320 W | 750 W (5900X reference) | 3x 8-pin adapter or 450 W+ Gen5 cable | [18] | high |
| RTX 4080 SUPER | 320 W | 750 W | same | [18] | high |
| RTX 4090 (FE) | 450 W | 850 W | 3x 8-pin adapter or 450 W+ Gen5 cable | [19] | high |
| RTX 5060 | 145 W | 550 W | 1x 8-pin OR 300 W Gen5 cable (adapter in box); partner models vary | [15] | high |
| RTX 5060 Ti | 180 W | 600 W | same | [15] | high |
| RTX 5070 | 250 W | 650 W | 2x 8-pin adapter or 300 W+ Gen5 cable | [20] | high |
| RTX 5070 Ti | 300 W | 750 W | 2x 8-pin adapter or 300 W+ Gen5 cable | [20] | high |
| RTX 5080 | 360 W | 850 W | 3x 8-pin adapter or 450 W+ Gen5 cable | [14] | high |
| RTX 5090 (FE) | 575 W | 1000 W (spec table); the page also says "Minimum PSU 850 W, higher may be needed" | 4x 8-pin adapter or 1x 600 W Gen5 (12V-2x6) | [13] | high |

Status: NVIDIA's 50-series page lists 5090, 5080, 5070 Ti, 5070, 5060 Ti, 5060 and 5050, with no SUPER models as of 2026-11-07 [24]. Press reports of a delayed 50 Super (TweakTown) are unconfirmed. Treat 50 Super as "not on NVIDIA's page".

Partner examples: ASUS ROG Astral RTX 5090 OC recommends 1000 W "assuming fully overclocked GPU and CPU" [25] (high). MSI RTX 4090 Gaming Trio listings mostly say 850 W; one retailer says 1000 W, unverified [26] (low-medium).

### Radeon and Intel Arc

AMD reference TBP and AMD recommended PSU were NOT reachable (amd.com timeouts; TechPowerUp 403). Do not present a figure below as an AMD reference. The rows are labelled by partner model. "Minimum PSU" is the partner's own wording on its spec page.

| Model | Board power | PSU | Connectors | Source | Confidence |
|---|---|---|---|---|---|
| Sapphire PULSE RX 9070 XT (11348-03-20G) | 304 W typical | Minimum 750 W | 2x 8-pin | [S3] | high (vendor page) |
| Sapphire NITRO+ RX 9070 XT | 330 W typical | Minimum 850 W | 12V-2x6 (H++); 3x 8-pin adapter included | [S4] | high (vendor page) |
| Sapphire PULSE RX 9070 (11349-03-20G) | 220 W typical | Minimum 650 W | 2x 8-pin | [S5] | high (vendor page) |
| Sapphire PULSE RX 9060 XT 16G | 170 W typical | Minimum 450 W | 1x 8-pin | [S6] | high (vendor page) |
| Sapphire PULSE RX 7900 XTX 24G (11322-02-20G) | 370 W total | Minimum 800 W | 3x 8-pin | [S7] | high (vendor page) |
| Sapphire PULSE RX 7800 XT (11330-02-20G) | 266 W total | Minimum 700 W | 2x 8-pin | [S8] | high (vendor page) |
| RX 9070 XT, generic (Corsair, Tom's Hardware) | 304 W | "a little over 750 W" (Corsair); other sites 700-800 W; a partner Red Devil box says 900 W | 2x 8-pin typical; some partner models 3x 8-pin or 12V-2x6 | [21], [22] | medium |
| RX 9070, generic (Corsair) | 220 W (not attributed to AMD) | 650 W | 2x 8-pin; partner cards may differ | [21] | medium |
| Radeon AI PRO R9700 | 300 W (search snippet citing Tom's Hardware) | 750 W minimum, single 16-pin (PowerColor snippet) | | [S10], [S11] | low |
| Intel Arc B580 Limited Edition | 190 W TBP | Minimum 600 W | 1x 8-pin | [23] | high |
| Intel Arc B770 | Official spec not verified (reports 225-300 W conflict) | | | | gap |

Instructions:
- Board power is per model: the NITRO+ 9070 XT (330 W) differs from the PULSE (304 W). Say "varies by model: check the exact model page" for any other Radeon partner (XFX, PowerColor, ASRock, ASUS, Gigabyte were not checked).
- A snippet claiming 220 W for the PULSE 9070 XT conflicts with the Sapphire page and is rejected [S3].
- For a Radeon model not in the table, give no wattage; request the partner's spec page.

## 4. CPU power

| CPU | Base / TDP | Max turbo / PPT | Platform | Source | Confidence |
|---|---|---|---|---|---|
| Core i7-14700K / KF | Processor Base Power 125 W | Maximum Turbo Power 253 W | LGA1700 | [27] | high |
| Core i9-14900K | Base 125 W | Max Turbo 253 W | LGA1700 | [28] | high |
| Core Ultra 9 285K | Base 125 W | Max Turbo 250 W | LGA1851 | [29] | high |
| Ryzen 7 9800X3D | TDP 120 W | PPT 162 W | AM5 | [30] | medium (reviews; amd.com blocked) |
| Ryzen 9 9950X | TDP 170 W | PPT 230 W (TechPowerUp) vs 200 W (ComputerBase): conflict | AM5 | [30] | medium; low for PPT |

Instructions: use max turbo (Intel) or PPT (AMD) as the CPU term in the sizing sum, not base power. BIOS defaults (unlimited PL2, "performance" profiles) can exceed these; Intel values are spec values. The research gives no EPS connector requirement for 14th-gen boards: read the board manual (many Z790 boards have 8+4 or 8+8-pin). Check that the PSU has at least as many EPS 8-pin/4+4 connectors as the board requires.

## 5. PSU sizing method

1. Take the GPU vendor's recommended PSU (NVIDIA page for NVIDIA reference; the partner model page for partner and Radeon cards). Use it as the floor.
2. Cross-check: CPU max power + GPU board power + rest-of-system allowance. The only sourced allowance is Intel's example budget: 300 W card + 300 W CPU + 150 W rest = 750 W PSU; 450 W card = 1000 W; 600 W card = 1200 W (Table 3-2, 125 W TDP class CPU). It is a test budget, not a buying rule [2], high. Quote it as such.
3. Take the higher of steps 1 and 2 as the requirement, and say which step set it.
4. Margin: no reputable source gave a percentage. Any margin applied is a **plugin heuristic, not sourced**; label it so and let the user ignore it. A suggestion such as "stay at or above the vendor figure, and do not run exactly at the minimum with a high-power CPU" is acceptable, labelled that way.
5. Check connectors: count PCIe 8-pin (or 12V-2x6) ports against the GPU requirement, EPS against the board.
6. Check transient tolerance for cards of 300 W or more: prefer ATX 3.1 (Intel excursion tables).

## 6. Verdict rules

| Verdict | Condition |
|---|---|
| Incompatible | The PSU lacks the required connector type or count and no adapter option is documented for that card. The PSU wattage is below the vendor-recommended figure for that exact model. The PSU lacks the EPS connector the board requires. |
| Compatible with conditions | An adapter is needed (e.g. 3x or 4x 8-pin to 12V-2x6; state the plug count the adapter requires). The PSU equals the vendor recommendation (at the edge: say it, and apply the labelled heuristic if used). The PSU is ATX 3.0 or older with a 300 W+ card (missing ATX 3.1 hold-up and 12V-2x6 socket). The unit is SFX or SFX-L: check wattage and that the case accepts the type (see `form-factors-cases.md`). The partner model's recommendation differs from the NVIDIA/AMD reference: use the partner figure. |
| Compatible | Wattage at or above the higher of the vendor figure and the cross-check, connectors present with correct count, no unverified input. |

Always state the exact condition, the source `[n]` and the confidence. If an input is missing (Radeon reference data, a partner model not checked), return "cannot conclude" for that item and name the page to check.

## 7. Running cost

1. Formula: energy (kWh) = average power at the wall (W) x hours / 1000; cost = energy x price per kWh. Show each step and label the result `estimate`.
2. Hours: ask the user for hours under load (gaming, rendering) and hours at idle or on the desktop per day, and the days per year. Never assume them.
3. Price per kWh: the user's own contract price comes first. If they have none, EDF's regulated Tarif Bleu can be quoted as a dated reference: option Base 0.2001 EUR incl. tax per kWh, "Prix applicable à compter du 1er août 2026 pour toute nouvelle souscription" [31]. Re-read the page before quoting it. CRE's page showed the 1 February 2026 grid (Base 6 kVA: 19.40 c EUR/kWh) and is older [32]. The monthly subscription is a fixed fee: leave it out of the PC's cost.
4. Power: a plug-in meter reading at the wall by the user is best. Otherwise, dated measurements of the same parts in a review (secondary, with conditions). GPU board power and CPU TDP or PPT (sections 3 and 4) are rated maximums, never an average: when they are the only figure, label the result "upper bound".
5. PSU losses: power at the wall = power drawn by the parts / efficiency. 80 PLUS minimum efficiency, 230 V EU internal, at 20 / 50 / 100 % load [33]: Bronze 85 / 88 / 85 %; Silver 87 / 90 / 87 %; Gold 90 / 92 / 89 %; Platinum 92 / 94 / 90 %; Titanium 93 / 95 / 91 % (and 90 % at 10 %). These are certification floors, not the unit's curve. A wall reading already includes the losses: never apply them twice.
6. Cybenetics publishes efficiency levels, but its notice says that automated data collection, "including by AI agents, requires prior written permission" [34]: never read it automatically; use a figure only from the user's screenshot.
7. Upgrade: compare the old and the new part on the same hours and the same price, and give the yearly difference.

## Not verified

- AMD reference TBP and AMD recommended PSU for RX 7800 XT, 7900 XTX, 9060 XT, 9070, 9070 XT: amd.com timed out and TechPowerUp returned 403. Only Sapphire partner values and secondary sources exist.
- AMD memory bandwidth figures, out of scope here.
- Ryzen 9 9950X PPT: 230 W vs 200 W conflict. AMD CPU TDP/PPT rest on review sites.
- Intel Arc B770 and other B-series cards: no official spec.
- Origin of the 35 mm bend rule: cable makers only. No PCI-SIG or NVIDIA bend radius found. The PCI-SIG CEM 5.1 spec is paywalled and unread; the Intel ATX 3.1 guide was read in full text for sideband, excursion and hold-up.
- Exact 12V-2x6 pin lengths: secondary sources disagree.
- Margin percentage: no reputable source.
- Running cost (section 7): the EDF price of 1 August 2026 was not cross-checked on a CRE deliberation or the tariff order; idle and gaming power per part not stored (no measurement source read).
- Radeon AI PRO R9700 power, PSU, connector: snippets only. R9700 partner dimensions not checked.
- Other Radeon partners (XFX, PowerColor, ASRock, ASUS, Gigabyte): not checked. The Sapphire spec pages carry no publication date; the live page may differ from the indexed copy.
- RTX 50 Super status: only NVIDIA's current page, which lists none.
- Melting-incident counts are from Wikipedia, not verified individually.
- Board EPS requirements for 14th-gen and AM5 boards.

## Sources

Numbers [1]-[30] follow the research file `r4-power-form-factors.md`; [S3]-[S11] follow `r4-radeon-addendum.md`. All checked 2026-11-07.

1. https://en.wikipedia.org/wiki/PCI_Express (medium)
2. https://cdrdv2-public.intel.com/336521/336521_Rev2p1a.pdf, Intel ATX Version 3 Multi Rail Desktop Platform PSU Design Guide, Rev 2.1a, Nov 2023 (high)
3. https://en.wikipedia.org/wiki/12VHPWR (medium)
4. https://knowledge.seasonic.com/article/79-comparison-atx-3-0-vs-atx-3-1-standards (medium)
5. https://www.corsair.com/us/en/explorer/diy-builder/power-supply-units/atx-30-vs-atx-31-whats-the-difference/ (medium)
6. https://hwbusters.com/gpu/will-my-atx-v3-0-psu-or-my-gpu-be-compatible-with-12v-2x6-do-i-need-a-new-cable-psu-gpu-everything-you-need-to-know/ (search summary, low)
7. https://www.corsair.com/eu/nl/explorer/diy-builder/power-supply-units/does-the-50-series-need-a-12v-2x6-cable/ (medium)
8. Compatibility gap, same as [6] (low)
9. https://en.wikipedia.org/wiki/ATX (medium)
10. https://www.intel.com/content/www/us/en/content-details/336521/atx-version-3-multi-rail-desktop-platform-power-supply-design-guide.html (listing, high)
11. https://www.tomshardware.com/pc-components/gpus/nvidia-confident-that-rtx-50-series-power-connectors-unlikely-to-melt-despite-higher-tdp (search summary, medium)
12. https://guru3d.com/story/our-findings-12vhpwr-power-connectors-issues-likely-die-to-bending (search summary, low)
13. https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/ (high)
14. https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5080/ (high)
15. https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/ (high)
16. https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/ (high)
17. https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4070-family/ (high)
18. https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4080-family/ (high)
19. https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/ (high)
20. https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/ (high)
21. https://www.corsair.com/explorer/gamer/gaming-pcs/amd-rx-9070-and-9070-xt-everything-you-need-to-know/ (medium)
22. https://www.tomshardware.com/pc-components/gpus/rx-9070-xt-red-devil-packaging-recommends-a-900w-power-supply-amds-frank-azor-confirms-custom-cards-with-lower-wattage-requirements (search summary, medium)
23. https://www.intel.com/content/www/us/en/products/sku/241598/intel-arc-b580-graphics/specifications.html (high)
24. https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/ (high)
25. https://rog.asus.com/us/graphics-cards/graphics-cards/rog-astral/rog-astral-rtx5090-o32g-btf-gaming/spec/ (high)
26. https://www.memoryexpress.com/Products/MX00122975 and https://www.ocinside.de/review/msi_rtx_4090_gaming_x_trio_24g/2 (search summaries, low-medium)
27. https://www.intel.com/content/www/us/en/products/sku/236783/intel-core-i7-processor-14700k-33m-cache-up-to-5-60-ghz/specifications.html (high-medium)
28. https://www.intel.com/content/www/us/en/products/sku/236773/intel-core-i9-processor-14900k-36m-cache-up-to-6-00-ghz/specifications.html (high)
29. https://www.intel.com/content/www/us/en/products/sku/241060/intel-core-ultra-9-processor-285k-36m-cache-up-to-5-70-ghz/specifications.html (high)
30. TechPowerUp 9950X3D review, ComputerBase 9900X/9950X test, TheFPSReview 9800X3D review (search summaries, medium-low)

Radeon addendum:
- S3. https://www.sapphiretech.com/en/consumer/pulse-radeon-rx-9070-xt-16g-gddr6 (high, vendor)
- S4. https://www.sapphiretech.com/en/consumer/nitro-radeon-rx-9070-xt-16g-gddr6 (high, vendor)
- S5. https://www.sapphiretech.com/en/consumer/pulse-radeon-rx-9070-16g-gddr6 (high, vendor)
- S6. https://www.sapphiretech.com/en/consumer/pulse-radeon-rx-9060-xt-16g-gddr6 (high, vendor)
- S7. https://www.sapphiretech.com/en/consumer/pulse-radeon-rx-7900-xtx-24g-gddr6 (high, vendor)
- S8. https://www.sapphiretech.com/en/consumer/pulse-radeon-rx-7800-xt-16g-gddr6 (high, vendor)
- S10. https://www.tomshardware.com/pc-components/gpus/amd-launches-radeon-ai-pro-r9700-to-challenge-nvidias-ai-market-dominance (snippet only, low)
- S11. https://powercolor.com/product-detail255.htm (TLS error, snippet only, low)
31. EDF, Tarif Bleu, "Prix de l'offre d'électricité Tarif Bleu (TTC)", option Base: https://particulier.edf.fr/fr/accueil/electricite-gaz/offres-electricite/tarif-bleu.html (redirects to /fr/accueil/electricite-gaz/tarif-bleu.html), read 2026-11-26 in the browser: full
32. CRE, "Comprendre les tarifs réglementés de vente d'électricité" (page updated 20/01/2026): https://www.cre.fr/consommateurs/comprendre-les-tarifs-reglementes-de-vente-delectricite-trve.html, read 2026-11-26: full
33. CLEAResult 80 PLUS, "What do the different PSU ratings mean?", 230V EU Internal Non-Redundant table: https://www.clearesult.com/80plus/80plus-psu-ratings-explained, read 2026-11-26 in the browser: full (no date shown)
34. Cybenetics, ETA levels page (notice on automated collection): https://www.cybenetics.com/index.php?option=eta_9-51-40, read once 2026-11-26: full; values not stored (terms)
