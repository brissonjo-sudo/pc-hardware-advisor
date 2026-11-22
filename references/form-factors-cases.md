# Form factors, case fit and PCIe lanes

Last checked: 2026-11-07. Values change: verify online before concluding.

Use this file to check board and PSU form factors, GPU and cooler fit in a case, and PCIe lane sharing for `check-compatibility`. Confidence scale: high = vendor primary page read directly; medium = secondary, Wikipedia or vendor search snippet; low = retailer, forum, aggregator. All rows checked 2026-11-07. Sockets, chipsets and memory are in `sockets-chipsets.md`; power is in `power-supplies-connectors.md`.

## 1. Motherboard form factors

| Form factor | Dimensions | Notes | Source | Confidence |
|---|---|---|---|---|
| ATX | 305 x 244 mm (12 x 9.6 in), 7 slot positions | | [31] | medium |
| microATX | 244 x 244 mm | | [31] | medium |
| Mini-ITX | 170 x 170 mm, 1 slot | | [31], [32] | medium |
| Mini-DTX | 203 x 170 mm | | [32] | medium |
| E-ATX | True E-ATX 305 x 330 mm. Many "E-ATX" boards are 305 x 257-272 mm | Wikipedia marks accuracy disputed: read each board and case spec | [31] | low-medium |

Instruction: a smaller board fits a case that lists a larger one, only if the case spec lists it (for example the SSUPD Meshroom S lists ITX, mDTX, mATX and ATX [39]). Do not assume. For "E-ATX" say "varies by model: check the exact board page".

## 2. PSU form factors

| Type | Dimensions (W x H x D) | Notes | Source | Confidence |
|---|---|---|---|---|
| ATX | 150 x 86 x 140 mm (depths 160/180/200/230 mm also used) | Wikipedia cites Intel ATX12V design guide v1.1 | [31] | medium |
| SFX | 125 x 63.5 x 100 mm | | [31], [33] | medium |
| SFX-L | 125 x 63.5 x 130 mm (fits a 120 mm fan) | Corsair explainer agrees | [31], [33] | medium |
| ATX12VO | 12 V only, 10-pin motherboard connector | Not compatible with standard ATX boards or PSUs | [31] | medium |

Official formfactors.org / Intel SFX guide was not retrieved. SFX and board dimensions stay secondary.

Instructions:
- Match PSU type to the case spec: small cases state SFX only, SFX / SFX-L with a maximum PSU length (e.g. Fractal Terra: max PSU length 130 mm [35]), or ATX up to a stated depth.
- An SFX-L unit needs the 130 mm clearance the case lists. Do not place an SFX-L in a case that lists SFX only (Lian Li A4-H2O: "SFX / SFX-L only" per retailer data [38]).
- Wattage and connector count of SFX units belong to the power file; flag that SFX models often cap lower than ATX (the research gives no figure: do not state one).

## 3. GPU dimensions

Rows are reference/Founders Edition unless a partner model is named. Partner models vary widely (about 300-360 mm, 2.5-4 slots for 9070 XT, 3090 and 5090 class): say "varies by model: check the exact model page".

| Model | Length x height | Slots / thickness | Source | Confidence |
|---|---|---|---|---|
| RTX 3090 FE / 3090 Ti FE | 313 mm x 138 mm | 3-slot | [16] | high |
| RTX 4090 FE | 304 mm x 137 mm | 3-slot (61 mm) | [19] | high |
| RTX 4080 / 4080 SUPER FE | 304 mm x 137 mm | 3-slot (61 mm) | [18] | high |
| RTX 4070 / 4070 SUPER FE | 244 mm x 112 mm | 2-slot | [17] | high |
| RTX 5070 FE | 242 mm x 112 mm | 2-slot | [20] | high |
| RTX 5080 FE | 304 mm x 137 mm | 2-slot in spec table; same page says plan for a 3-slot (61 mm) card: inconsistent, treat as up to 61 mm | [14] | high, internally inconsistent |
| RTX 5090 FE | 304 mm x 137 mm | 2-slot in spec table; page text says 3-slot 61 mm: inconsistent | [13] | high, internally inconsistent |
| RTX 5070 Ti, 5060 Ti, 5060, 4070 Ti | varies by manufacturer | varies | [15], [17], [20] | high |
| Intel Arc B580 Limited Edition | 272 x 115 mm | 2 slots | [23] | high |
| ASUS ROG Astral RTX 5090 | 357.6 x 149.3 mm | 76 mm thick, 3.8 slot | [25] | high |
| MSI RTX 4090 Gaming (X) Trio | 337 x 140 x 77 mm | about 3.5 slot | [26] | low-medium (retailer; MSI page 403) |
| Sapphire PULSE RX 9070 XT (11348-03-20G) | 320 mm L x 120.25 W x 61.6 H (vendor wording) | 3 slots | [S3] | high |
| Sapphire NITRO+ RX 9070 XT | 330.8 mm L x 128.5 W x 65.68 H | 3.2 slots | [S4] | high |
| Sapphire PULSE RX 9070 (11349-03-20G) | 280 x 120.25 x 51.5 mm | 2.5 slots | [S5] | high |
| Sapphire PULSE RX 9060 XT 16G | 240 x 111.25 x 46.08 mm | 2.3 slots | [S6] | high |
| Sapphire PULSE RX 7900 XTX 24G | 313 x 133.75 x 52.67 mm | 2.7 slots | [S7] | high |
| Sapphire PULSE RX 7800 XT | 280 x 128.75 x 52.57 mm | 2.5 slots | [S8] | high |
| Sapphire PULSE RX 9070 XT (retailer figures) | 320 x 121 x 62 mm | 3 slots | [34] | low (retailer; agrees with [S3]) |

Sapphire page axis labels are copied as written ("W" and "H" in the research); the third dimension is the card thickness. Confirm which axis is thickness against the slot count before comparing to a case limit.

## 4. Small-case limits

Case specs differ between versions (V1, V2, V3, MAX): ask for the exact version.

| Case | Max GPU length / thickness | Max cooler height | PSU type | Source | Confidence |
|---|---|---|---|---|---|
| Fractal Terra | 322 mm long, 145 mm wide, 72 mm thick, 2 expansion slots | 48 mm | SFX / SFX-L, max PSU length 130 mm; Mini-ITX only; 10.4 L | [35] | high |
| Cooler Master NR200P MAX | 336 mm incl. power connector, 75 mm thick (triple slot). Page shows conflicting heights (160 vs 140 mm) | 67 mm | SFX (850 W SFX included); SFX-L supported, 130 mm clearance; Mini-ITX max 170 x 180 mm | [36] | high, conflict noted |
| Cooler Master NR200P (original) | 330 mm incl. connector, 156 mm high, 60 mm wide (triple slot) | 155 mm (vented) / 153 mm (glass); 76 mm with vertical GPU | SFX / SFX-L, 130 mm clearance | [37] | medium (snippet) |
| Cooler Master NR200P V2 / MAX V2 | 334 mm GPU length and 80 mm thickness with the standard bracket (357 mm with the alternative bracket), 160 mm H | 67 mm | SFX or SFX-L, up to 130 mm | [37]; coolermaster.com, 2026-11-08 | medium |
| Cooler Master NR200P V3 | up to 361.5 x 160 mm; thickness 78.5 mm (3.8 slots) | 70 mm | SFX or SFX-L | [37]; coolermaster.com, 2026-11-08 | medium |
| Lian Li A4-H2O (x DAN Cases) | 322 mm, triple-slot | 55 mm (also radiator + fans thickness 55 mm); 240 mm top radiator; 11 L, 326 x 140 x 244 mm | SFX / SFX-L only | [38] | low (retailers; lian-li.com returned 404 on 2026-11-08; PSU rule unverified; one review disagrees with 330 mm / ATX and is discounted) |
| SSUPD Meshroom S (V1/V2) | Vertical GPU up to 4 slots (82 mm) or horizontal 3 slots (63 mm). Length 332 mm (ITX, rear vertical; 353 mm with extra feet) or 314 mm (front vertical in ATX/mATX; 325 mm with feet). Some listings say 336/343 mm; some figures exclude the GPU baffle | 74 mm (3-slot GPU mode) / 54 mm (4-slot mode); some sources 73/53 | SFX, SFX-L, ATX up to 150-170 mm depending on config/version; ITX, mDTX, mATX, ATX boards | [39] | medium (version differences) |
| FormD T1 (V2.1) | Official page unreachable. BuildCores 325 mm; TechBenchPro 295 mm; NCASE Sandwich Kit spec: max GPU 140 x 325 mm, 3.25 slot | NCASE T1 Sandwich table: 73 mm with 2-slot GPU, 63 mm with 2.5-slot, 53 mm with 3-slot | SFX / SFX-L (not verified from official page) | [40] | low-medium |

## 5. Reading case specs

- Length: "max GPU length" is usually measured including the power plug or bracket, and sometimes with a fan or baffle that blocks part of it. Compare the case length to the card length plus the plug if the case spec excludes the plug. If unclear, label the result "compatible with conditions".
- Thickness: compare card thickness or slot count to the case thickness limit. Treat marketing slot counts (2.5, 3.2) as approximate; use millimetres when both sides give them.
- Height: card height against case width or height limits where the spec lists one (NR200P 156 mm high vs 160 mm [37]).
- Cooler vs GPU trade-off: several ITX cases trade cooler height for GPU thickness (Terra, Meshroom S, T1). Check the two limits together, not separately. The Meshroom S and T1 tables above show the cooler limit dropping as GPU thickness rises [39], [40].
- Orientation: vertical vs horizontal GPU changes the figures (Meshroom S) [39]. Ask the user which layout they use.
- Radiator vs GPU: the A4-H2O states a 55 mm figure covering radiator plus fans, and a 240 mm top radiator [38]. Where a case lists a radiator and a GPU at once, confirm both limits with the exact variant of the case. The research does not give other radiator-versus-GPU conflicts: do not invent them.
- 16-pin cable clearance: case specs do not count the bend space of the 12V-2x6 plug. Cable makers advise at least 35 mm straight cable before a bend (not an NVIDIA rule) [12]; NVIDIA FE pages tell users to plan about 36 mm extra for cables [13], [14] (space planning, not a bend radius; medium). Add this to a tight case as a condition, labelled with who says it.
- Mini-ITX board constraints (single M.2 on the back, VRM height, 4-slot DIMM layouts) were not found in any primary source. Say so; do not state them as facts. The only sourced ITX facts are the 170 x 170 mm size and the single slot [31], [32].

## 6. PCIe lanes and sharing

### CPU lane counts

| Platform | CPU PCIe lanes | Configurations | Source | Confidence |
|---|---|---|---|---|
| Intel LGA1700 (Core i7-14700K, i9-14900K) | 20 lanes, PCIe 5.0 and 4.0 | 1x16+4 or 2x8+4: 16 Gen5 for the GPU + 4 Gen4 (M.2) | [27], [28] | high |
| Intel LGA1851 (Core Ultra 9 285K) | 24 lanes (PCIe 5.0 and 4.0) | Up to 1x16+2x4, 2x8+2x4, 1x8+4x4 | [29] | high |
| Intel Z790 chipset | Up to 28 PCIe lanes (max 20 Gen4, rest Gen3), 8 SATA ports, DMI 4.0 x8 | CPU lanes are separate | [41], [42] | high-medium |
| AMD AM5 (X870E) | 24 PCIe 5.0 lanes from the CPU (16 GPU + 4 M.2 + 4 general); chipset adds downstream PCIe 4.0 / 3.0 | The AMD "44 lanes" total is unverified | [43] | medium (secondary only) |

### Sharing examples (board-specific: read the exact manual)

| Board | Sharing | Source | Confidence |
|---|---|---|---|
| MSI MAG Z790 Tomahawk Max WiFi | "SATA_1~2 will be unavailable when installing M.2 SSD in the M2_3 slot" | [44] | medium (search summary of manual) |
| Gigabyte Z790 Aorus Elite AX | M2M_SB shares bandwidth with SATA3 2 and 3; SATA availability can depend on the M.2 device type (SATA vs NVMe) | [44] | medium |
| ASUS ROG Maximus Z790 Extreme | M.2_1 shares bandwidth with PCIEX16(G5)_2 (a slot conflict, not SATA) | [44] | medium |
| MSI MPG X870E Carbon WiFi | PCI_E1 shares bandwidth with PCI_E2 and M2_2 | [45] | low-medium |
| MSI MAG X870E Tomahawk WiFi | M2_2 shares with rear USB4 | [45] | low-medium |
| Gigabyte X870E boards | CPU-linked M.2 sockets (M2B_CPU / M2C_CPU) share bandwidth with the main x16 slot, up to x8 when populated | [45] | low-medium |
| ASUS ProArt X870E-Creator | Reportedly drops the top x16 to x8 when M.2_2 is used | [45] | low |
| ASUS ROG Crosshair X870E Hero | Reportedly keeps x16 | [45] | low |

A generic rule that "third and fourth M.2 share lanes with SATA ports 4-6" is unverified and board dependent: do not state it as fact.

### How to check lane sharing

1. Open the board manual (where to find it: `source-access-policy.md` section 5, Manuals) at its spec sheet: read the "Expansion slots" and "Storage" tables and the footnotes under each M.2 socket.
2. Find the manual's "PCIe / M.2 / SATA configuration" or "lane sharing" table (rows by slot, columns by combination).
3. Check whether the x16 slot falls to x8 (bifurcation) when a CPU-linked M.2 socket is populated.
4. Check which SATA ports are disabled when an NVMe SSD (not a SATA SSD) populates a socket.
5. Report the result as: slot or socket populated, effect (x16 to x8, SATA n disabled), manual page, confidence. If the manual is unreachable, say "from search summary" and lower the confidence.

## 7. Verdict rules for physical fit

| Verdict | Condition |
|---|---|
| Incompatible | Card length (with plug if the case counts it) exceeds the case maximum. Card thickness exceeds the case limit. PSU type not listed by the case (ATX in an SFX-only case). Board form factor not listed by the case. |
| Compatible with conditions | Dimensions differ by version or orientation of the case, or the spec is a snippet or retailer figure. GPU thickness forces a lower cooler limit (check both). A 16-pin cable needs bend clearance (state cable makers' 35 mm and NVIDIA's 36 mm planning figure with attribution). A listed dimension varies by partner model. Lane sharing disables a port or drops a slot to x8. |
| Compatible | All dimensions inside the case limits from a high or medium source, PSU type listed, lane sharing documented as not conflicting. |

Margin: the research gives no sourced clearance margin between card and case limit. If you recommend one, label it "plugin heuristic, not sourced". Without a margin, say how many millimetres remain and let the user judge.

## Not verified

- Official form-factor dimensions (formfactors.org, Intel SFX guide): board and SFX/SFX-L sizes are Wikipedia/Corsair only.
- E-ATX actual sizes vary; Wikipedia marks accuracy disputed.
- Case limits: lian-li.com (404), formdworks and ssupd (429/DNS), Cooler Master NR200P original page (404 on one URL). Values come from snippets or retailers; check the version (V1/V2/V3, MAX).
- FormD T1 official dimensions: unreachable; three sources conflict (325 / 295 / 325 x 140 mm).
- NR200P MAX page shows conflicting heights (160 vs 140 mm).
- Mini-ITX board constraints (single M.2, VRM height, DIMM layout) and ITX PCIe layouts: nothing collected.
- Partner GPU dimensions: only the ASUS Astral 5090 and the Sapphire pages were read first-hand; MSI and others are retailer-level. Other Radeon partners were not checked.
- AM5 CPU lane total and the AMD "44 lanes" figure: amd.com blocked.
- Lane sharing examples come from search summaries (manualowl, MSI, Gigabyte pages returned 403), not first-hand manual reads.
- 12V-2x6 bend radius: not published by NVIDIA or PCI-SIG in anything found; the 36 mm NVIDIA figure is space for cables, not a bend radius.
- RTX 5080 / 5090 FE thickness: the NVIDIA pages disagree internally (2-slot vs 61 mm).

## Sources

Numbers follow `research/r4-power-form-factors.md`; S-numbers follow `research/r4-radeon-addendum.md`. All checked 2026-11-07.

- 12. https://guru3d.com/story/our-findings-12vhpwr-power-connectors-issues-likely-die-to-bending (search summary, low)
- 13. https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5090/ (high)
- 14. https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5080/ (high)
- 15. https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5060-family/ (high)
- 16. https://www.nvidia.com/en-us/geforce/graphics-cards/30-series/rtx-3090-3090ti/ (high)
- 17. https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4070-family/ (high)
- 18. https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4080-family/ (high)
- 19. https://www.nvidia.com/en-us/geforce/graphics-cards/40-series/rtx-4090/ (high)
- 20. https://www.nvidia.com/en-us/geforce/graphics-cards/50-series/rtx-5070-family/ (high)
- 23. https://www.intel.com/content/www/us/en/products/sku/241598/intel-arc-b580-graphics/specifications.html (high)
- 25. https://rog.asus.com/us/graphics-cards/graphics-cards/rog-astral/rog-astral-rtx5090-o32g-btf-gaming/spec/ (high)
- 26. https://www.memoryexpress.com/Products/MX00122975 and https://www.ocinside.de/review/msi_rtx_4090_gaming_x_trio_24g/2 (search summaries, low-medium)
- 27. https://www.intel.com/content/www/us/en/products/sku/236783/intel-core-i7-processor-14700k-33m-cache-up-to-5-60-ghz/specifications.html (high-medium)
- 28. https://www.intel.com/content/www/us/en/products/sku/236773/intel-core-i9-processor-14900k-36m-cache-up-to-6-00-ghz/specifications.html (high)
- 29. https://www.intel.com/content/www/us/en/products/sku/241060/intel-core-ultra-9-processor-285k-36m-cache-up-to-5-70-ghz/specifications.html (high)
- 31. https://en.wikipedia.org/wiki/ATX (dimensions section, medium)
- 32. https://en.wikipedia.org/wiki/Mini-ITX (medium)
- 33. https://www.corsair.com/explorer/diy-builder/power-supply-units/power-supply-form-factors-and-sizes-explained/ (search summary, medium)
- 34. https://www.newegg.ca/sapphire-tech-pulse-9070-xt-16g-d6-oc-radeon-rx-9070-xt-16gb-video-cards-triple-fans/p/27N-0005-002A6 (search summary, low)
- 35. https://www.fractal-design.com/products/cases/terra/terra/graphite/ (high)
- 36. https://www.coolermaster.com/en-global/products/nr200p-max/ (high)
- 37. https://www.coolermaster.com/en-global/products/masterbox-nr200p.html, .../nr200p-v3.html, .../masterbox-nr200p-v2.html (search summaries, medium)
- 38. https://www.adorama.com/lia4h2o.html and https://www.skroutz.mt/s/37211014/Lian-Li-A4-H2O-X4-Mini-Tower-Computer-Case-Black.html (search summary, medium-low)
- 39. https://www.ssupd.co/products/new-meshroom-s, https://ssupd.co/products/cases-meshroom-s-v1, https://techpowerup.com/review/ssupd-meshroom-s (search summaries, medium)
- 40. https://ncased.com/pages/specs-t1sw and https://www.buildcores.com/products/PCCase/rf2911gfd/FormD-T1-V2.1-Mini-ITX-Desktop-Silver-Steel-Coated-Mesh-Side-Panel (search summaries, low-medium)
- 41. https://www.intel.com/content/www/us/en/products/sku/229721/intel-z790-chipset/specifications.html (search summary, high-medium)
- 42. https://cdrdv2-public.intel.com/743835/743835-004.pdf (Intel 700 Series chipset datasheet, search summary, medium)
- 43. https://www.guru3d.com/review/colorful-igame-x870e-vulcan-w-oc-v14-review/page-2/ and https://www.digitalcitizen.life/x670e-x670-b650e-b650-chipsets/ (search summaries, low-medium)
- 44. https://www.manualowl.com/m/MSI/MAG-Z790-TOMAHAWK-MAX-WIFI/Manual/723726?page=30 ; .../Gigabyte/Z790-AORUS-ELITE-AX/Manual/683762?page=28 ; .../Asus/ROG-MAXIMUS-Z790-EXTREME/Manual/683478?page=25 (search summaries, direct fetch 403, medium)
- 45. https://www.msi.com/blog/pcie-lane-bifurcation-and-bandwidth-sharing-on-msi-x870e-x870-motherboards (403; search summary), ASUS ROG forum threads, elevenforum (low-medium)
- S3. https://www.sapphiretech.com/en/consumer/pulse-radeon-rx-9070-xt-16g-gddr6 (high)
- S4. https://www.sapphiretech.com/en/consumer/nitro-radeon-rx-9070-xt-16g-gddr6 (high)
- S5. https://www.sapphiretech.com/en/consumer/pulse-radeon-rx-9070-16g-gddr6 (high)
- S6. https://www.sapphiretech.com/en/consumer/pulse-radeon-rx-9060-xt-16g-gddr6 (high)
- S7. https://www.sapphiretech.com/en/consumer/pulse-radeon-rx-7900-xtx-24g-gddr6 (high)
- S8. https://www.sapphiretech.com/en/consumer/pulse-radeon-rx-7800-xt-16g-gddr6 (high)
