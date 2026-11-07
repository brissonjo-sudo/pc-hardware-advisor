# R4 Power, connectors, form factors, physical fit, PCIe lanes
Collected: 2026-11-07 · Model: sonnet

Conventions: "checked" date is 2026-11-07 for every source below. Confidence: high = vendor/standard primary page read directly; medium = secondary or vendor explainer or Wikipedia; low = aggregator/forum/retailer. Numbers in [n] refer to the Sources list. AMD (amd.com) pages all timed out (60 s, 4 attempts) and several motherboard/GPU vendor pages returned 403/404/429: recorded as "blocked/unavailable", not bypassed.

## Connectors and standards

| Item | Value | Source | Confidence |
|---|---|---|---|
| PCIe x16 slot power | up to 75 W combined (5.5 A at +12 V = 66 W, plus 3.3 V up to 3 A = 9.9 W) after configuration as high-power device | [1] (cites PCIe CEM) | medium |
| PCIe 6-pin (2x3) | +75 W | [1] | medium |
| PCIe 8-pin (2x4) | +150 W; sense pins distinguish 6-pin vs 8-pin; 6-pin plugged in 8-pin receptacle limits card to 75 W | [1] | medium |
| Max pre-CEM 5.0 card | 300 W (75 slot + increments of 75/150 W via 2x3 / 2x4). Two 8-pin cards (375 W) used in practice since PCIe 4.0 CEM | [2] section 3, [1] | high (Intel guide), medium (wiki) |
| Real draw of an 8-pin plug | a 2x4 PCIe plug draws no more than 13.5 A (about 162 W at 12 V) over 3 power pins; 2x3 no more than 6.75 A (about 81 W) | [2] section 2.1 | high |
| EPS12V CPU connector (2x4, 8-pin) | Intel guide recommends PSU support 24-32 A on a 2x4 (8-pin) 18 AWG connector and 12-16 A on a 2x2 (4-pin); mobo may have 1 or 2 (4+4 / 8-pin) CPU connectors, EPS12V as reference | [2] section 2.1 | high |
| 12VHPWR (CEM 5.0) -> 12V-2x6 (CEM 5.1) | 12V-2x6 replaces 12VHPWR "to address reliability concerns"; "New power supply designs should mount only the 12V-2x6 connector and the 12VHPWR connector should be deprecated" | [2] | high |
| 12V-2x6 rating | 600 W on 12V rail, 16 AWG wire, 9.2 A per pin; four sideband signals (CARD_PWR_STABLE, CARD_CBL_PRES#, SENSE0, SENSE1). Max single card power raised to 675 W (e.g. 75 W slot + 600 W cable) | [2] sections 2.1, 3, 5.2.2.4.3 | high |
| SENSE0/SENSE1 table (initial / sustained W) | Ground+Ground 375 / 600; Open+Ground 225 / 450; Ground+Open 150 / 300; Shorted to each other 100 / 150; Open+Open 0 / 0 (card may draw nothing via the connector) | [2] Table 3-6 | high |
| Physical difference 12VHPWR vs 12V-2x6 | The connector changes are on the GPU/PSU sockets (sense pins shorter, power terminals longer); cables and plugs are unchanged. Sense pins only make contact when the power pins are fully seated. Markings: "H+" = 12VHPWR, "H++" = 12V-2x6. Exact pin length values vary by secondary source (sense pin 1.5 mm shorter vs 4 -> 2.75 mm; terminal +0.25 mm): not verified in the PCI-SIG spec | [3], [4], [5], [6] | medium (qualitative), low (mm values) |
| Cable interchangeability | Corsair: a 12VHPWR cable can be kept with a 12V-2x6 GPU; difference is not in the cable. An ATX 3.1 PSU cable on a GPU with an old 12VHPWR socket does not give the shorter-sense-pin protection | [7], [8] | medium |
| ATX 3.0 vs ATX 3.1 | 3.1 = 12V-2x6 replaces 12VHPWR (>450 W PSUs); hold-up time REQUIRED 12 ms at 100 % load (was 17 ms), RECOMMENDED 17 ms at 80 % load; ATX 3.1 guide aligned to PCIe CEM 5.1. Rev 2.1a of Intel guide, Nov 2023 | [2] Table 4-8, [9], [10] | high |
| PSU power excursion (Intel Table 3-3) | PSU >450 W with 12V-2x6: 200 % of rated for 100 us, 180 % for 1 ms, 160 % for 10 ms, 120 % for 100 ms, 100 % continuous. PSU <=450 W or without 12V-2x6: 150 % / 145 % / 135 % / 110 % / 100 % | [2] Table 3-3 | high |
| Card-side excursion (CEM 5.1 via Intel guide Table 3-1) | up to 2.5x sustained power on the +12 V connector rail and 3x total card power for <=100 us; ratio decays logarithmically to 1x at 1 s | [2] Table 3-1 | high |
| Intel PSU sizing example (test budget, not a buying rule) | 300 W card + 300 W CPU + 150 W rest -> 750 W PSU; 450 W card -> 1000 W; 600 W card -> 1200 W (Table 3-2, CPU 125 W TDP class) | [2] Table 3-2 | high |
| Insertion durability | Intel guide test: LLCR (contact resistance) criteria after 30 insertion-removal cycles; Wikipedia states reliability may fall after roughly 30-40 mating cycles | [2], [3] | medium |
| Melting reports | 4090 (2022, partly not fully seated); CableMod adapter recall Feb 2024 (CPSC, 272 reports, ~25,300 units); RTX 5090 FE cases reported; RX 9070 XT partner-card cases reported Aug 2025 incl. Sapphire Nitro+ owners using non-ATX 3.1 PSUs. Wikipedia is the aggregation; not verified individually | [3] | medium |
| Seating/bend guidance | Consensus advice: click/latch fully, no gap, no bending right at the connector; "at least 35 mm straight before a bend" comes from cable makers (CableMod, Corsair listing), NOT from NVIDIA. NVIDIA reported to say "fully and evenly seated". No PCI-SIG/NVIDIA published bend radius found. Intel guide has a "12V-2x6 Cable Plug Connection Recommendation" figure (Fig 5-10, image only). Check card/PSU maker manual | [11], [12], [2] | medium / low |
| Adapters | NVIDIA ships a 3x or 4x 8-pin -> 12V-2x6 adapter ("adapter in box") with FE and many cards; 5090 FE accepts 4x 8-pin or one >=450 W PCIe Gen5 cable (listed 600 W in spec table); the card needs the number of 8-pin plugs matching the adapter | [13], [14] | high |
| Corsair claim "all RTX 50 use 12V-2x6" | NVIDIA lists 5060 Ti / 5060 as "1x 8-pin OR 300 W Gen5 cable (adapter in box)" for FE/reference; partner models vary per model | [7], [15] | medium: do not generalise |

## GPU power and recommended PSU

NVIDIA "Required System Power" is a minimum assuming a stated reference CPU (Ryzen 9 9950X for 50 series; Ryzen 9 5900X for the 4080 page) and a PCIe CEM 5.1 compliant PSU; NVIDIA states it can differ per system. Partner cards often ask for more (examples below).

| GPU | Board power | Vendor-recommended PSU | Connector | Source | Confidence |
|---|---|---|---|---|---|
| RTX 3090 (FE) | 350 W | 750 W | 2x 8-pin (adapter to 1x 12-pin included) | [16] | high |
| RTX 3090 Ti (FE) | 450 W | 850 W | 3x 8-pin adapter or 450 W+ Gen5 cable (16-pin) | [16] | high |
| RTX 4070 | 200 W | 650 W | 2x 8-pin adapter or 300 W Gen5 cable; some partner models 1x 8-pin | [17] | high |
| RTX 4070 SUPER | 220 W | 650 W | same as 4070 | [17] | high |
| RTX 4070 Ti / Ti SUPER | 285 W | 700 W | 2x 8-pin adapter or 300 W Gen5 cable | [17] | high |
| RTX 4080 | 320 W | 750 W (Ryzen 9 5900X reference) | 3x 8-pin adapter or 450 W+ Gen5 cable | [18] | high |
| RTX 4080 SUPER | 320 W | 750 W | same | [18] | high |
| RTX 4090 (FE) | 450 W | 850 W | 3x 8-pin adapter or 450 W+ Gen5 cable | [19] | high |
| RTX 5060 Ti | 180 W | 600 W | 1x 8-pin OR 300 W Gen5 cable (adapter in box); partner models vary | [15] | high |
| RTX 5060 | 145 W | 550 W | same | [15] | high |
| RTX 5070 | 250 W | 650 W | 2x 8-pin adapter or 300 W+ Gen5 cable | [20] | high |
| RTX 5070 Ti | 300 W | 750 W | 2x 8-pin adapter or 300 W+ Gen5 cable | [20] | high |
| RTX 5080 | 360 W | 850 W | 3x 8-pin adapter or 450 W+ Gen5 cable | [14] | high |
| RTX 5090 (FE) | 575 W | 1000 W (spec table); page also says "Minimum PSU 850 W, higher may be needed" | 4x 8-pin adapter or 1x 600 W Gen5 (12V-2x6) | [13] | high |
| RX 7800 XT | not retrieved (amd.com timeout) | not retrieved | not retrieved | - | gap |
| RX 7900 XTX | not retrieved (amd.com timeout) | not retrieved | not retrieved | - | gap |
| RX 9060 XT | not retrieved (amd.com timeout) | not retrieved | not retrieved | - | gap |
| RX 9070 | 220 W (Corsair, not attributed to AMD) | 650 W (Corsair) | 2x 8-pin (reference spec table in Corsair article; partner cards may differ) | [21] | medium |
| RX 9070 XT | 304 W (Corsair; Tom's Hardware repeats 304 W) | "a little over 750 W" (Corsair); other sites 700-800 W; partner Red Devil box says 900 W | 2x 8-pin typical; some AIB models use 3x 8-pin or 12V-2x6 | [21], [22] | medium |
| Intel Arc B580 | 190 W TBP | min PSU 600 W (listed as minimum) | 1x 8-pin; 272 x 115 mm, 2 slots (Limited Edition) | [23] | high |
| Intel Arc B770 | official spec not verified (reports 225-300 W) | - | - | - | low / gap |

2025-2026 status check: NVIDIA's 50-series page (checked 2026-11-07) lists RTX 5090, 5080, 5070 Ti, 5070, 5060 Ti, 5060, 5050 and no SUPER models [24]. Press reports say 50 Super was postponed to Q3 2026 (TweakTown), but I found no confirmation that any shipped. Treat 50 Super as "not on NVIDIA's page as of today".

Partner model recommendations differ from NVIDIA reference: ASUS ROG Astral RTX 5090 OC recommends 1000 W "assuming fully overclocked GPU and CPU" [25]; MSI RTX 4090 Gaming Trio listings mostly say 850 W (one retailer says 1000 W, unverified) [26].

Transient spike / margin rule: the primary reference is the Intel ATX 3.1 guide: cards may spike to 2.5x (connector) / 3x (total) sustained power for 100 us, and a >450 W ATX 3.1 PSU must tolerate 200 % for 100 us [2]. A "keep 20-30 % margin over vendor-required wattage" rule of thumb is common but I did not obtain a reputable source for a specific percentage: marked "not verified". Practical rule consistent with sources: use the vendor "required system power" as the floor and prefer ATX 3.1 / PCIe 5.1 PSUs for >=300 W cards (MSI and Corsair advise ATX 3.1 for 9070 XT; secondary).

## CPU power

| CPU | Base / TDP | Max turbo / PPT | Platform | Source | Confidence |
|---|---|---|---|---|---|
| Core i7-14700K / KF | Processor Base Power 125 W | Maximum Turbo Power 253 W | LGA1700; 20 PCIe lanes (5.0 and 4.0) | [27] | high |
| Core i9-14900K | Base 125 W | Max Turbo 253 W | LGA1700; 20 lanes; configs 1x16+4 or 2x8+4 | [28] | high |
| Core Ultra 9 285K | Base 125 W | Max Turbo 250 W | LGA1851; 24 lanes (PCIe 5.0 and 4.0); configs up to 1x16+2x4, 2x8+2x4, 1x8+4x4 | [29] | high |
| Ryzen 7 9800X3D | TDP 120 W | PPT 162 W | AM5 | [30] (secondary reviews) | medium (amd.com blocked) |
| Ryzen 9 9950X | TDP 170 W | PPT 230 W per TechPowerUp; ComputerBase reports 200 W: conflicting | AM5 | [30] | medium / low on PPT |

Note: motherboard BIOS defaults (e.g. unlimited PL2 / "Intel default" vs "performance" profiles) can exceed these; Intel values above are the spec ones. 14th gen board EPS requirement not stated by Intel pages: check board manual (many Z790 boards have 8+4 or 8+8-pin).

## Motherboard and PSU form factors

| Form factor | Dimensions | Notes | Source | Confidence |
|---|---|---|---|---|
| ATX motherboard | 305 x 244 mm (12 x 9.6 in), 7 slot positions | | [31] | medium (wiki, no inline citation for the row) |
| microATX | 244 x 244 mm | | [31] | medium |
| Mini-ITX | 170 x 170 mm, 1 slot | | [31], [32] | medium |
| E-ATX | true E-ATX 305 x 330 mm; many "E-ATX" boards are 305 x 257-272 mm; wiki marks accuracy disputed | check each board and case spec | [31] | low-medium |
| Mini-DTX | 203 x 170 mm | | [32] | medium |
| ATX PSU | 150 x 86 x 140 mm (depths 160/180/200/230 also used) | wiki cites Intel ATX12V design guide v1.1 | [31] | medium |
| SFX PSU | 125 x 63.5 x 100 mm | | [31], [33] | medium |
| SFX-L PSU | 125 x 63.5 x 130 mm (fits 120 mm fan) | Corsair explainer agrees | [31], [33] | medium |
| ATX12VO | 12 V only, 10-pin mobo connector | not compatible with standard ATX boards/PSUs | [31] | medium |

Official formfactors.org / Intel SFX design guide was not retrieved: SFX and mobo dimensions remain secondary.

## GPU dimensions

| Model | Length | Slots/thickness | Source |
|---|---|---|---|
| RTX 3090 FE | 313 mm (12.3 in) x 138 mm wide | 3-slot | [16] (NVIDIA) |
| RTX 3090 Ti FE | 313 mm x 138 mm | 3-slot | [16] |
| RTX 4090 FE | 304 mm x 137 mm | 3-slot (61 mm) | [19] |
| RTX 4080 / 4080 SUPER FE | 304 mm x 137 mm | 3-slot (61 mm) | [18] |
| RTX 4070 / 4070 SUPER FE | 244 mm x 112 mm | 2-slot | [17] |
| RTX 5070 FE | 242 mm x 112 mm | 2-slot | [20] |
| RTX 5080 FE | 304 mm x 137 mm | 2-slot (spec table); same page also says plan for a "3-slot card (61 mm)": inconsistent, treat as up to 61 mm | [14] |
| RTX 5090 FE | 304 mm x 137 mm | 2-slot (spec table); same page text says 3-slot 61 mm: inconsistent | [13] |
| RTX 5070 Ti, 5060 Ti, 5060, 4070 Ti | "varies by manufacturer" | varies | [15], [17], [20] |
| Intel Arc B580 Limited Edition | 272 x 115 mm | 2 slots | [23] |
| ASUS ROG Astral RTX 5090 | 357.6 x 149.3 mm | 76 mm thick, 3.8 slot | [25] |
| MSI RTX 4090 Gaming (X) Trio | 337 x 140 x 77 mm | about 3.5 slot | [26] (retailer + ocinside table; MSI page 403) |
| Sapphire Pulse RX 9070 XT | 320 x 121 x 62 mm per Newegg; 3 slots | | [34] (retailer, low) |

Partner models of RX 9070 XT, 3090 and 5090 vary widely (about 300-360 mm, 2.5-4 slots); always read the model's own spec page. Official ASUS, MSI and Sapphire pages were mostly 403/404 during collection.

## Small-case limits

| Case | Max GPU length/thickness | Max cooler height | PSU type | Source |
|---|---|---|---|---|
| Fractal Terra | 322 mm long, 145 mm wide, 72 mm thick, 2 expansion slots | 48 mm | SFX / SFX-L, max PSU length 130 mm; Mini-ITX only; 10.4 L | [35] (Fractal, high) |
| Cooler Master NR200P MAX | 336 mm incl. power connector, 75 mm thick (triple slot); page shows conflicting heights (160 vs 140 mm) | 67 mm | SFX (850 W SFX included); SFX-L supported, 130 mm clearance; Mini-ITX max 170 x 180 mm | [36] (high, with conflict noted) |
| Cooler Master NR200P (original) | 330 mm long incl. connector, 156 mm high, 60 mm wide (triple slot) | 155 mm (vented panel) / 153 mm (glass); 76 mm with vertical GPU | SFX / SFX-L, 130 mm clearance | [37] (search snippet of vendor page, medium) |
| Cooler Master NR200P V2 / MAX V2 | 357 mm incl. connector, 160 mm H, 73 mm W (triple) | 67 mm | - | [37] (snippet, medium) |
| Cooler Master NR200P V3 | up to 361.5 x 160 mm | 70 mm | - | [37] (snippet, medium) |
| Lian Li A4-H2O (x DAN Cases) | 322 mm, triple-slot | 55 mm (also radiator + fans thickness 55 mm); 240 mm top radiator; 11 L, 326 x 140 x 244 mm | SFX / SFX-L only (no ATX) | [38] (retailer-consolidated; lian-li.com page 404; one review disagrees with 330 mm / ATX: discounted) |
| SSUPD Meshroom S (V1/V2) | vertical GPU up to 4 slots (82 mm) or horizontal 3 slots (63 mm); length 332 mm (ITX, rear vertical, 353 mm with extra feet) or 314 mm (front vertical in ATX/mATX, 325 mm with feet); some listings 336/343 mm; excludes GPU baffle in some figures | 74 mm (3-slot GPU mode) / 54 mm (4-slot mode); some sources 73/53 | SFX, SFX-L, ATX up to 150-170 mm depending on config/version; supports ITX, mDTX, mATX, ATX boards | [39] (ssupd.co snippet + retailers; medium, version differences) |
| FormD T1 (V2.1) | official page unreachable (DNS failure); BuildCores 325 mm; TechBenchPro 295 mm; NCASE Sandwich Kit spec: max GPU 140 x 325 mm, 3.25 slot | NCASE T1 Sandwich table: 73 mm with 2-slot GPU, 63 mm with 2.5-slot, 53 mm with 3-slot GPU | SFX / SFX-L (not verified from official page) | [40] (low-medium) |

How to read specs: "max GPU length" is usually measured including the power plug/bracket and sometimes with fan or baffle blocking; thickness (slots) interacts with cooler height in many ITX cases (Terra, Meshroom, T1 and others trade cooler height for GPU thickness); vertical vs horizontal GPU orientation changes the figures (Meshroom). Cable bend space for 12V-2x6 is not counted in case specs: add roughly 35 mm beyond the plug (cable-maker guidance) for the connector side-panel gap, e.g. NVIDIA tells users to plan 36 mm extra for cables on FE pages [13], [14]. Not verified: ITX board-specific constraints (single M.2 on back, VRM height, ITX 4-slot DIMM): no primary source collected; see gaps.

## PCIe lanes and sharing

CPU lanes (official sources):
- Intel LGA1700 (14700K, 14900K): 20 CPU lanes, PCIe 5.0 and 4.0; configs 1x16+4 or 2x8+4, i.e. 16 Gen5 for GPU + 4 Gen4 (M.2) [27], [28].
- Intel LGA1851 (Core Ultra 285K): 24 lanes (5.0 and 4.0); configs up to 1x16+2x4, 2x8+2x4, 1x8+4x4 [29].
- Intel Z790 chipset: up to 28 PCIe lanes (max 20 Gen4, rest Gen3), 8 SATA ports, DMI 4.0 x8; the CPU lanes are separate [41], [42].
- AMD AM5 X870E (secondary sources only): 24 PCIe 5.0 lanes from the CPU (16 GPU + 4 M.2 + 4 general); chipset adds PCIe 4.0 / 3.0 downstream lanes; AMD total "44 lanes" figure is unverified (AMD page blocked); AM5 "24 usable" is the common figure. Confidence medium [43].

Examples of sharing (all board-specific; read the exact manual):
- MSI MAG Z790 Tomahawk Max WiFi: "SATA_1~2 will be unavailable when installing M.2 SSD in the M2_3 slot" (manual excerpt via search summary of manualowl.com; page 403 for direct fetch). Medium [44].
- Gigabyte Z790 Aorus Elite AX: "M2M_SB connector shares bandwidth with the SATA3 2, 3 connector"; Gigabyte notes SATA availability may depend on M.2 device type (SATA vs NVMe). Medium [44].
- ASUS ROG Maximus Z790 Extreme: M.2_1 shares bandwidth with PCIEX16(G5)_2 (a PCIe slot conflict, not SATA). Medium [44].
- X870E/X870: MSI states per-model sharing: MPG X870E Carbon WiFi PCI_E1 shares bandwidth with PCI_E2 and M2_2; MAG X870E Tomahawk WiFi M2_2 shares with rear USB4. Gigabyte: CPU-linked M.2 sockets (M2B_CPU / M2C_CPU) share bandwidth with the main x16 slot, up to x8 when populated. ASUS: ProArt X870E-Creator reportedly drops top x16 to x8 when M.2_2 used; ROG Crosshair X870E Hero reportedly keeps x16. All from search summaries of MSI/Gigabyte/ASUS pages and forums, not read first-hand (MSI blog 403). Low-medium [45].
- Generic rule that "third/fourth M.2 share lanes with SATA ports 4-6": unverified, board dependent.

How to check in a manual: find the "Expansion slots" / "Storage" tables in the spec sheet and the footnotes under each M.2 socket; in the manual look for the "PCIe/M.2/SATA configuration" or "lane sharing" table (rows by slot, columns by combination); verify whether x16 slot falls to x8 (bifurcation) and whether specific SATA ports are disabled when an NVMe SSD (not SATA SSD) populates a socket.

## Not verified / gaps

- amd.com pages (RX 7800 XT, 7900 XTX, 9060 XT, 9070, 9070 XT, Ryzen 9800X3D/9950X) timed out repeatedly: AMD TBP, AMD recommended PSU and AMD CPU TDP/PPT are not primary-verified. Values shown for RX 9070/9070 XT and AMD CPUs are secondary.
- RX 7800 XT / 7900 XTX / 9060 XT power and PSU: no data collected; do not infer.
- Intel Arc B770 and B-series other than B580: no official spec found; B770 reports conflict (225 W vs 300 W).
- 12V-2x6 exact pin lengths, official bend radius, NVIDIA melting guidance: not found in primary documents; PCI-SIG CEM 5.1 spec itself is paywalled/not read. Intel ATX 3.1 guide (Rev 2.1a) was read in full text for sideband table, excursion and hold-up.
- Margin rule-of-thumb percentage: no reputable source gathered.
- Motherboard dimension sources (ATX, mATX, ITX, E-ATX) and SFX/SFX-L dimensions: Wikipedia/Corsair only; formfactors.org not retrieved.
- Case specs: lian-li.com (404), formdworks/ssupd (429/DNS), Cooler Master NR200P original page (404 on one URL): limits come from vendor snippets or retailers; check version (V1/V2/V3, MAX).
- ITX board constraints (single M.2 on back, VRM, DIMM) and ITX-specific PCIe layouts: nothing collected.
- Motherboard manuals for lane sharing: manualowl, MSI, Gigabyte pages returned 403: examples come from search summaries only.
- RTX 50 Super: status unconfirmed beyond NVIDIA 50-series page showing none; Q3 2026 timing is rumor.
- Partner GPU dimensions: only ASUS Astral 5090 read first-hand from vendor page; others retailer-level.

## Sources

1. https://en.wikipedia.org/wiki/PCI_Express (checked 2026-11-07; cites PCI-SIG CEM) medium
2. https://cdrdv2-public.intel.com/336521/336521_Rev2p1a.pdf (Intel ATX Version 3 Multi Rail Desktop Platform PSU Design Guide, Rev 2.1a, Nov 2023; text extracted locally) high
3. https://en.wikipedia.org/wiki/12VHPWR (2026-11-07) medium
4. https://knowledge.seasonic.com/article/79-comparison-atx-3-0-vs-atx-3-1-standards (2026-11-07) medium
5. https://www.corsair.com/us/en/explorer/diy-builder/power-supply-units/atx-30-vs-atx-31-whats-the-difference/ (2026-11-07) medium
6. https://hwbusters.com/gpu/will-my-atx-v3-0-psu-or-my-gpu-be-compatible-with-12v-2x6-do-i-need-a-new-cable-psu-gpu-everything-you-need-to-know/ (via search summary, 2026-11-07) low
7. https://www.corsair.com/eu/nl/explorer/diy-builder/power-supply-units/does-the-50-series-need-a-12v-2x6-cable/ (2026-11-07) medium
8. same as [6] re. compatibility gap (low)
9. https://en.wikipedia.org/wiki/ATX (2026-11-07) medium
10. https://www.intel.com/content/www/us/en/content-details/336521/atx-version-3-multi-rail-desktop-platform-power-supply-design-guide.html (listing, via search) high
11. https://www.tomshardware.com/pc-components/gpus/nvidia-confident-that-rtx-50-series-power-connectors-unlikely-to-melt-despite-higher-tdp (search summary only) medium
12. https://guru3d.com/story/our-findings-12vhpwr-power-connectors-issues-likely-die-to-bending (search summary only; 35 mm CableMod guidance) low
13. https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/ (2026-11-07) high
14. https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5080/ (2026-11-07) high
15. https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/ (2026-11-07) high
16. https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/ (2026-11-07) high
17. https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4070-family/ (2026-11-07) high
18. https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4080-family/ (2026-11-07) high
19. https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/ (2026-11-07) high
20. https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/ (2026-11-07) high
21. https://www.corsair.com/explorer/gamer/gaming-pcs/amd-rx-9070-and-9070-xt-everything-you-need-to-know/ (2026-11-07) medium
22. https://www.tomshardware.com/pc-components/gpus/rx-9070-xt-red-devil-packaging-recommends-a-900w-power-supply-amds-frank-azor-confirms-custom-cards-with-lower-wattage-requirements (search summary, 2026-11-07) medium
23. https://www.intel.com/content/www/us/en/products/sku/241598/intel-arc-b580-graphics/specifications.html (2026-11-07) high
24. https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/ (2026-11-07) high
25. https://rog.asus.com/us/graphics-cards/graphics-cards/rog-astral/rog-astral-rtx5090-o32g-btf-gaming/spec/ (2026-11-07) high
26. https://www.memoryexpress.com/Products/MX00122975 and https://www.ocinside.de/review/msi_rtx_4090_gaming_x_trio_24g/2 (via search summaries) low-medium
27. https://www.intel.com/content/www/us/en/products/sku/236783/intel-core-i7-processor-14700k-33m-cache-up-to-5-60-ghz/specifications.html (via search summary quoting Intel; plus Intel support article 000006778) high-medium
28. https://www.intel.com/content/www/us/en/products/sku/236773/intel-core-i9-processor-14900k-36m-cache-up-to-6-00-ghz/specifications.html (2026-11-07) high
29. https://www.intel.com/content/www/us/en/products/sku/241060/intel-core-ultra-9-processor-285k-36m-cache-up-to-5-70-ghz/specifications.html (2026-11-07) high
30. TechPowerUp 9950X3D review https://techpowerup.com/review/amd-ryzen-9-9950x3d/single-page.html; ComputerBase https://www.computerbase.de/2024-08/amd-ryzen-9-9900x-9950x-test/2/; TheFPSReview 9800X3D https://www.thefpsreview.com/2024/11/06/amd-ryzen-7-9800x3d-cpu-review/7 (search summaries only, 2026-11-07) medium-low
31. https://en.wikipedia.org/wiki/ATX (dimensions section) medium
32. https://en.wikipedia.org/wiki/Mini-ITX (2026-11-07) medium
33. https://www.corsair.com/explorer/diy-builder/power-supply-units/power-supply-form-factors-and-sizes-explained/ (search summary) medium
34. https://www.newegg.ca/sapphire-tech-pulse-9070-xt-16g-d6-oc-radeon-rx-9070-xt-16gb-video-cards-triple-fans/p/27N-0005-002A6 (search summary) low
35. https://www.fractal-design.com/products/cases/terra/terra/graphite/ (2026-11-07) high
36. https://www.coolermaster.com/en-global/products/nr200p-max/ (2026-11-07) high
37. https://www.coolermaster.com/en-global/products/masterbox-nr200p.html, .../nr200p-v3.html, .../masterbox-nr200p-v2.html (search summaries) medium
38. https://www.adorama.com/lia4h2o.html and https://www.skroutz.mt/s/37211014/Lian-Li-A4-H2O-X4-Mini-Tower-Computer-Case-Black.html (via search summary; Lian Li site 404) medium-low
39. https://www.ssupd.co/products/new-meshroom-s, https://ssupd.co/products/cases-meshroom-s-v1, https://techpowerup.com/review/ssupd-meshroom-s (search summaries) medium
40. https://ncased.com/pages/specs-t1sw (NCASE T1 Sandwich Kit), https://www.buildcores.com/products/PCCase/rf2911gfd/FormD-T1-V2.1-Mini-ITX-Desktop-Silver-Steel-Coated-Mesh-Side-Panel (search summaries) low-medium
41. https://www.intel.com/content/www/us/en/products/sku/229721/intel-z790-chipset/specifications.html (search summary) high-medium
42. https://cdrdv2-public.intel.com/743835/743835-004.pdf (Intel 700 Series chipset datasheet, via search summary) medium
43. https://www.guru3d.com/review/colorful-igame-x870e-vulcan-w-oc-v14-review/page-2/ and https://www.digitalcitizen.life/x670e-x670-b650e-b650-chipsets/ (search summaries) low-medium
44. https://www.manualowl.com/m/MSI/MAG-Z790-TOMAHAWK-MAX-WIFI/Manual/723726?page=30 ; .../Gigabyte/Z790-AORUS-ELITE-AX/Manual/683762?page=28 ; .../Asus/ROG-MAXIMUS-Z790-EXTREME/Manual/683478?page=25 (search summaries; direct fetch 403) medium
45. https://www.msi.com/blog/pcie-lane-bifurcation-and-bandwidth-sharing-on-msi-x870e-x870-motherboards (403 on fetch; search summary), ASUS ROG forum threads and elevenforum (low) low-medium
