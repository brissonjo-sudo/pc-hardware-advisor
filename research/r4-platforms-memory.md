# R4 Platforms, chipsets, BIOS and memory
Collected: 2026-11-07 · Model: sonnet

Conventions: every source is numbered in "Sources" with the date checked (all 2026-11-07). Confidence: high = read on a primary page (intel.com/amd.com) during this session; medium = reputable press or vendor blog, or a primary page seen only through a search summary; low = leak, forum or unverified recall. Items marked UNVERIFIED are recalled, not checked, and must not be used as rules before confirmation.

## Platform overview

| Socket | CPU families | Chipsets | Memory type | Status 2026 | Source | Confidence |
|---|---|---|---|---|---|---|
| LGA1700 | Core 12th gen (Alder Lake), 13th (Raptor Lake), 14th (Raptor Lake Refresh); not 6th-11th gen | 600 series (Z690/H670/B660/H610) and 700 series (Z790/H770/B760) | DDR4 OR DDR5, fixed per board (see note) | Mature, end of line for retail; 12th/13th/14th gen all still listed as compatible | [1], [2] | high (socket, chipsets, speeds); medium ("DDR4 or DDR5 per board, never both") |
| LGA1851 | Core Ultra 200S (Arrow Lake-S, launched Q1'25) and Core Ultra 200S Plus (Arrow Lake Refresh: Core Ultra 7 270K Plus, Core Ultra 5 250K Plus, retail 2026-03-26) | 800 series: Z890, B860, H810 (also Q870, W880 workstation/pro) | DDR5 only | Current Intel mainstream desktop platform. All existing 800-series boards support the 200S Plus. | [3], [4], [5], [6], [7] | high |
| LGA1954 | Nova Lake-S (expected "Core Ultra 400") | 900 series reported (Z990, Z970, B960...) | DDR5 (reported) | NOT RELEASED as of 2026-11-07. Intel only said "end of 2026" (Q4 2025 earnings call, via press); leaks say mass production Q4 2026, first CPUs Q1 2027 | [8], [9] | low (socket/chipset names), medium (Intel timing statement) |
| AM4 | Ryzen 1000 to 5000 (and 5000G/4000G APUs) | A320, B350, X370, B450, X470, B550, X570, A520 | DDR4 | Legacy. AMD marked "10 years of AM4" at Computex 2026 with a 5800X3D anniversary edition | [10], [11] | medium (platform), see gaps for support matrix |
| AM5 | Ryzen 7000, 8000G, 9000 (incl. 9000X3D, 9950X3D2 Dual Edition, 7700X3D), Ryzen AI 400 desktop APUs (OEM only, 2026) | 600 series: A620 (A620A), B650, B650E, X670, X670E. 800 series: B840, B850, X870, X870E | DDR5 only (UDIMM) | Current AMD platform. AMD states AM5 support "through 2029". Zen 6 (Olympic Ridge desktop, Medusa1 APU) confirmed for AM5 by AMD documentation, not yet launched. | [10], [12], [13], [14], [15] | high (support to 2029 via AMD blog as relayed; chipsets list), medium (Zen 6 timing) |

Note LGA1700 memory: Intel's compatibility page gives DDR5 and DDR4 limits per CPU generation but does not state "one board = one type". The "board is DDR4 or DDR5, never both" rule comes from DIMM slot physical keying and board design (recalled, widely known, not read on an Intel page). Treat as medium.

## Chipset capabilities

CPU OC and memory OC columns come from Intel ARK desktop-chipsets table [16] and AMD CPU pages / press [13]. PCIe lane counts are chipset lanes (not CPU lanes) unless noted.

| chipset | CPU OC | memory OC | PCIe gen CPU / chipset lanes | notes | source |
|---|---|---|---|---|---|
| Intel Z790 | Yes (IA, BCLK, Memory) | Yes | CPU: PCIe 5.0 1x16 or 2x8, + PCIe 4.0 1x4. Chipset: up to 28 lanes, PCIe 3.0/4.0, DMI 4.0 x8 | 2 DIMMs/channel, no ECC; launch Q4'22 | [16], [17] |
| Intel H770 | No | Yes | PCIe 3.0/4.0; lane count UNVERIFIED | | [16] |
| Intel B760 | No | Yes | CPU: PCIe 5.0 1x16, PCIe 4.0 1x4. Chipset: 14 lanes max (ARK; datasheet gives 4 Gen3 + 10 Gen4 and is internally inconsistent), DMI 4.0 x4 | | [16], [18] |
| Intel Z690 | Yes | Yes | PCIe 3.0/4.0; lane count UNVERIFIED | | [16] |
| Intel H670 / B660 | No | Yes | PCIe 3.0/4.0; lane counts UNVERIFIED | | [16] |
| Intel H610 | No (nothing listed) | Not listed (blank on ARK) | PCIe 3.0 only (chipset) | | [16] |
| Intel Z890 | Yes (IA, BCLK, Memory) | Yes | CPU: PCIe 5.0 1x16+1x4, 2x8+1x4 or 1x8+3x4; PCIe 4.0 1x4. Chipset: 24 lanes PCIe 4.0, DMI 4.0 x8 | 2 DPC; launch Q4 2024. Only 800 chipset with CPU OC and "200S Boost" | [16], [19], [3] |
| Intel B860 | No | Yes | CPU: PCIe 5.0 1x16+1x4. Chipset: 14 lanes PCIe 4.0, DMI 4.0 x4 | 2 DPC; launch Q1'25 | [16], [20] |
| Intel H810 | No | No | CPU: PCIe 5.0 x16 only. Chipset: 8 lanes PCIe 4.0, DMI x4 | 1 DIMM per channel (boards have 2 slots total); launch Q1'25 | [16], [21] |
| AMD A620 / A620A | No | Yes (EXPO) | Per press/AMD table snippets: PCIe 4.0 for GPU and M.2 (not confirmed on full AMD table) | Entry; 600 series | [13] (partial), [22] |
| AMD B650 | Yes | Yes | CPU lanes PCIe 5.0 on M.2 mandatory; GPU slot 5.0 optional (vendor choice) UNVERIFIED on AMD table | 600 series | [13] (partial) |
| AMD B650E / X670E | Yes | Yes | PCIe 5.0 mandatory for GPU and M.2 | E = Extreme PCIe | UNVERIFIED on AMD table; recalled |
| AMD X670 | Yes | Yes | PCIe 5.0 M.2 mandatory, GPU 5.0 optional; dual chipset die | | UNVERIFIED; recalled |
| AMD B840 | No CPU multiplier OC (per press) | Yes (EXPO, DDR5 tuning) | PCIe 4.0 per Guru3D/Corsair; TechPowerUp says GPU slot PCIe 3.0: conflicting | Entry-level successor to A620/A620A | [22], [23] |
| AMD B850 | Yes | Yes | PCIe 5.0 for NVMe; GPU PCIe 5.0 optional; USB4 optional | Replaces B650 | [22], [23] |
| AMD X870 | Yes | Yes | PCIe 5.0 GPU and NVMe mandatory, USB4 mandatory; up to 36 usable downstream lanes (single chipset die) | | [22] |
| AMD X870E | Yes | Yes | Same as X870, more downstream connectivity (up to 44 lanes) | | [22] |

AMD compatibility rule (AMD chipset page, via search summary): all AM5 boards with 600 or 800 series chipsets work with all AM5 processors, but a BIOS update may be needed for some Ryzen 8000/9000 on 600-series boards [13].

## BIOS requirements and known issues

**LGA1700 and 13th/14th gen**
- Intel: 600 and 700 series boards "require a BIOS update to boot" 13th/14th gen CPUs; may also be needed when moving between 12th, 13th and 14th gen. Contact board maker for the BIOS. Page last reviewed 2026-02-05. [24] (high)
- Intel compatibility page: 12th/13th/14th gen all on LGA1700 with 600 or 700 series; not compatible with 500 series and older, nor 800 series. Memory: 12th gen DDR5-4800 / DDR4-3200; 13th/14th gen DDR5-5600 (page shows "4800/5600" because of i3/Pentium-class) / DDR4-3200. [2] (high)
- Intel ARK Core i9-14900K: FCLGA1700, DDR5 up to 5600 MT/s, DDR4 up to 3200 MT/s, max 192 GB, 2 channels, ECC "supported" (footnoted, depends on platform), PCIe 5.0/4.0, 20 CPU lanes, launch Q4'23. [1] (high)
- Vmin Shift Instability (13th and 14th gen desktop i9/i7/i5; page names no SKU list): Intel support article 000102331, last reviewed 2026-07-21, gives: warranty extended by 2 years, up to 5 years from original purchase date for eligible processors; run a BIOS with microcode 0x12F or later and use "Intel Default Settings". [25] (high)
- Microcode timeline (Intel Community post by Intel staff, 2025-05-01): 0x12B released September 2024; 0x12F supplements 0x12B, no change to root cause, no measurable performance impact on i9-14900K per Intel testing. 0x129 appears as a separate Intel Community topic dated 2025-04-17 (content not read). 0x125 not checked. [26] (high for 0x12B/0x12F, low for 0x129/0x125)
- Community moderator claim that only K/KF/KS models are affected is NOT an Intel statement; Intel's article lists only "i9, i7, i5" 13th/14th gen desktop. Do not state the K-only scope as fact. [25], [26]
- ASUS 600-series boards: Intel notes ME firmware may need updating before BIOS; see Intel article 000092983 (not read). [24]

**LGA1851**
- Intel says 200S Plus boots on existing 800-series boards; per HWCooling, "should boot without BIOS update, but update recommended". Intel (quick reference guide): all existing 800-series motherboards support 200S Plus. [5], [7] (medium/high)

**AM4**
- AMD guidance (search summary of AMD FAQ cpu-99): check the motherboard maker's support page for the BIOS that supports the CPU; if the board cannot boot, flash with an older supported CPU, use USB BIOS Flashback if present, or contact the maker. [27] (medium: page not directly fetched)
- AMD AM4 chipset page (search summary): "not all processors are supported on every chipset", some combinations marked "Selective Beta BIOS update". [11] (medium)
- Ryzen 5000 on A320/B350/X370: allowed only on select boards via vendor beta BIOS; AGESA 1.2.0.x era; vendor-by-vendor. [28], [29] (medium)

**AM5**
- Ryzen 9000 on 600-series boards needs a Zen 5-capable BIOS (AGESA 1.1.7.0 enabled boot on some boards; 1.2.0.0 broader; mid-2024 press). Check current board BIOS. [13], [30] (medium)
- Ryzen 8000G on 600 boards: "BIOS update may be needed" per AMD AM5 chipset page. [13] (medium)

**How to find the minimum BIOS**
1. Open the board's CPU Support List on the vendor product page (ASUS, MSI, Gigabyte, ASRock, Biostar). The list gives the minimum BIOS per CPU model; this is the authoritative source (recommended by Intel [24] and AMD [27]).
2. Use Intel Product Compatibility Tool (https://compatibleproducts.intel.com/, URL cited by search summary; not opened). [24]
3. If the BIOS on the board is too old: BIOS Flashback / Q-Flash Plus / Flash BIOS Button flashes from USB with no CPU or RAM; only PSU connectors needed. Names: ASUS BIOS FlashBack, MSI Flash BIOS Button, Gigabyte Q-Flash Plus, ASRock BIOS Flashback. [31] (medium)
4. No reliable cross-vendor list of AM5/LGA1851 boards with flashback was found. Check each board's spec page for the feature name. A forum report exists of an ASRock A620I where flashback failed (single case, low). [31]

## Memory rules per platform

**Intel LGA1700**
- 12th gen: DDR5-4800 or DDR4-3200. 13th/14th gen: DDR5 up to 5600, DDR4 up to 3200. [1], [2] (high)
- Max 192 GB (i9-14900K ARK). ECC flag exists on ARK but needs ECC-capable chipset and board (Z790 ARK: ECC not supported). [1], [17] (high)
- 1DPC vs 2DPC reductions for LGA1700: not captured from an Intel page. Gap.

**Intel LGA1851 (Core Ultra 200S)**
- ARK Core Ultra 7 265: DDR5 up to 6400 MT/s, 256 GB max, 2 channels, ECC flag, PCIe 5.0/4.0, 24 lanes, Q1'25. [32] (high). Note the ARK URL tied to a 265 page; the "6400" figure also matches the Intel quick reference guide statement of 6400 for the original 200S. [5]
- 200S Plus (270K Plus / 250K Plus): DDR5 up to 7200 MT/s, 256 GB, 2 channels, ECC flag, launch Q1'26. [33] (high)
- Intel quick reference: "Maximum memory speeds are associated with 1DPC. Additional DIMM loading on any channel may impact maximum memory speed." Up to DDR5-7200 at 1DPC with CUDIMM 1Rx8, 1Rx16, 2Rx8. Max capacity needs 2DPC. 4-rank CUDIMM is "emerging, supported on select 800-series boards". [5] (high)
- Per HWCooling: official 7200 applies to CUDIMM; quad-rank support expected, up to 128 GB per module and 512 GB total on some boards (press, medium). [7]
- Kingston Z890 listings citing Intel population rules for Core Ultra Series 2 (original 200S): 1DPC 1R/2R up to 5600 MT/s; 2DPC 1R up to 4800; 2DPC 2R up to 4400; 6400 CUDIMM at 1DPC requires a K-class CPU, non-K CPUs fall to 5600 or lower. Vendor secondary, medium. [34]
- CUDIMM: on Z890, clock driver can run in PLL mode; on older platforms CUDIMM works only in bypass mode (Corsair support page, medium). [35]
- "200S Boost" (Intel): requires Z890 board plus XMP memory. [5]
- Z890 and B860 allow memory OC; H810 does not and has 1 DIMM per channel. [16], [20], [21]

**AMD AM4**
- DDR4 only. AMD official max speed per generation not captured this session. Gap.

**AMD AM5**
- AMD spec pages (Ryzen 7 7700X, 8700G): DDR5-5200 with 2 DIMMs (1R or 2R), DDR5-3600 with 4 DIMMs. 7700X max 128 GB; 8700G listed 256 GB. [36] (medium, seen via search summary of amd.com pages)
- Ryzen 9 9950X: 2 DIMMs (1R/2R) DDR5-5600; 4 DIMMs DDR5-3600; max listed 256 GB on the 9950X page; AMD shop pages for 9950X3D/9900X3D show 192 GB (conflict between pages for the same family, capacity depends on the SKU page; read the specific SKU). [37] (medium)
- Ryzen AI 7 450GE (OEM): same 5600 / 3600 table, 256 GB, ECC "with motherboard support". [15] (medium)
- AMD does not use "1DPC/2DPC", it lists "2x1R, 2x2R, 4x1R, 4x2R" with the DIMM count. [37]
- 4-DIMM operation: real-world reports of 4 DIMMs landing at 3200-3600 on Ryzen 9000 (AMD community forum thread, low). [37]
- DDR5-6000 sweet spot: reported from an AMD (Robert Hallock) Discord AMA in 2022, relayed by Wccftech, TechSpot and Igor's Lab: best balance of cost, stability and performance; EXPO DDR5-6000 runs UCLK:MCLK 1:1 with FCLK on auto (FCLK default 1733 MHz on Ryzen 7000 at that time); above 6000 the controller runs UCLK:MCLK 2:1. Igor's Lab: EXPO 6000 with FCLK 2000 MHz is the best compromise. I did not find an AMD-published page for this; TechPowerUp article returned 403. [38], [39] (medium)
- XMP on AM5: press says kits with XMP only usually work on AM5 but may need manual enabling (ASUS labels it D.O.C.P.), may not hit rated speed, and default to JEDEC (e.g. DDR5-4800) until a profile is enabled. Board makers (MSI, Gigabyte) say their boards read both XMP and EXPO. A DDR5-7200 XMP kit on AM5 is not guaranteed; above 6000 runs 2:1 and is less efficient. No primary vendor page captured. [40] (medium/low)
- ECC: AM5 takes UDIMM only. Ryzen CPU pages list ECC "supported with motherboard support". Board support varies (ASUS reported on top boards, ASRock spec pages vary and changed over time, forum evidence). On-die ECC of DDR5 is not full ECC. [36], [41] (medium/low)
- AMD announced EXPO "Ultra Low Latency" profiles at Computex 2026 (no date). [10]

**Non-binary DIMMs (24/48 GB)**: not verified on a primary page this session; Intel 4-rank/CUDIMM and capacity per module claims above are the only DIMM-size data. Gap.

**4 DIMMs vs 2 DIMMs**: Intel says max speed is for 1DPC and extra loading reduces it [5]; AMD lists 3600 for 4 DIMMs [36], [37]. Vendors' QVL decides real behaviour.

## 2025-2026 changes and announced platforms

- 2026-03-11/13 (sources differ: Windows Central/heise mention 11 March; HWCooling says 13 March): Intel announced Core Ultra 200S Plus (Arrow Lake Refresh); retail 2026-03-26. Two SKUs: Core Ultra 7 270K Plus (8P+16E, 5.5 GHz, 250 W max turbo, $299) and Core Ultra 5 250K Plus (6P+12E, 159 W max turbo, $199). Official DDR5-7200 (CUDIMM). Same LGA1851 boards. A KF variant of the 250K Plus is mentioned by one outlet; HWCooling says KF versions not officially announced. [5], [6], [7], [33] (high/medium)
- LGA1851 remains the platform for the 2026 desktop lineup. No B860/H810 successor announced; B860 and H810 launched Q1'25. [20], [21]
- 2026 Computex (AMD): AM5 support extended through 2029 (AMD blog, reported by Tom's Hardware, PC Gamer, TweakTown). Ryzen 7 7700X3D announced (available July 16, 2026, $329 per AMD blog summary). Ryzen 9 9950X3D2 Dual Edition exists on AMD site. No Zen 6 desktop shown. [10], [12], [37]
- 2026-08: AMD web documentation names Olympic Ridge (desktop) and Medusa1 (APU) as Zen 6 products for Socket AM5 (press). No launch date from AMD. Press expects early 2027 (CES 2027). [14] (medium)
- Ryzen AI 400 desktop (Ryzen AI 7 450G/GE, Ryzen AI 5 435GE, etc.): AM5 APUs, Zen 5, Radeon 860M, OEM-only, prebuilts from Q2 2026. [15] (medium)
- Intel Nova Lake-S (Core Ultra 400): LGA1954, 900-series chipsets reported. Intel's own statement (Q4 2025 earnings, CEO Lip-Bu Tan, via press): desktop by end of 2026. Computex-era reports say slip to early 2027; a leaked partner slide says mass production Q4 2026 and first 28-core unlocked chip Q1 2027, 52-core later. No Intel ARK page, no retail availability as of 2026-11-07. A press item claims Intel confirmed LGA1954 "via internal tools", which is not an Intel statement. [8], [9] (low/medium)
- Intel Bartlett Lake-S (Core 200E): LGA1700 P-core-only embedded/edge parts (up to 12 P-cores), not retail; a "Core 5 120F" desktop name appears in leaks only. [42] (low)
- Intel instability warranty extension reviewed again 2026-07-21 (still 5 years max). [25]

## Not verified / gaps

- AMD's AM5 and AM4 chipset comparison pages and most AMD CPU spec pages timed out on direct fetch (HTTP timeout at 60 s, repeated). I did not use any workaround to bypass the site. AM5 chipset details marked UNVERIFIED above come from search-result summaries, press or recall.
- Full AM4 support matrix (A320/B350/X370/B450/X470/B550/X570/A520 vs Ryzen 1000-5000) was not captured as a table from AMD. Only the principle (BIOS needed, selective beta for 300-series, Ryzen 5000 on 300-series limited to select boards) was captured. Do not encode the matrix until AMD's page is read.
- AM4 official max memory speeds per generation: not captured.
- LGA1700 lane counts for H770/Z690/H670/B660/H610; datasheet inconsistencies for B760 (14 vs other values).
- LGA1700/LGA1851 1DPC/2DPC official table from ARK (Intel ARK says "refer to ark.intel.com" for 2DPC); only the secondary Kingston values for the original 200S were found. Needs verification on Intel's memory specification document for 200S and 200S Plus 2DPC speeds.
- Non-binary 24/48 GB DIMM support per platform: not verified.
- AM5 BIOS minimums per 9000-series SKU (exact AGESA by vendor): only mid-2024 press, old.
- A primary AMD statement for DDR5-6000 sweet spot: not found; only Discord-AMA-based press (2022). Check AMD EXPO page.
- XMP on AM5 vendor statements and "7200 XMP kit on AM5" behaviour: no primary vendor page; low-medium.
- Zen 6 exact status: AMD web page not read directly; relies on press.
- Intel microcode 0x129 and 0x125 content not read. Intel's article names no SKU list, so SKU scope (K only vs non-K) not settled.
- Nova Lake: nothing official beyond "2026" guidance; product, socket, chipset all leaks.
- JEDEC: no JEDEC page read (JESD79-5 speeds). Skip for now.
- Intel ARK page for i5-12400 and i5-13500 returned redirects to other SKUs; 12th gen figures taken from the Intel compatibility article [2].
- Two Intel tool redirects pointed to unrelated SKUs (suspicious); not followed.

## Sources

Date checked for all: 2026-11-07.

1. Intel ARK Core i9-14900K — https://www.intel.com/content/www/us/en/products/sku/236773/intel-core-i9-processor-14900k-36m-cache-up-to-6-00-ghz/specifications.html
2. Intel, Compatibility of Intel Core Desktop Processors (12th, 13th, 14th gen), article 000092149 (reviewed 02/06/2025 on page) — https://www.intel.com/content/www/us/en/support/articles/000092149/processors.html
3. Intel ARK Z890 chipset — https://www.intel.com/content/www/us/en/products/sku/237777/intel-z890-chipset/specifications.html
4. Intel ARK Core Ultra Processors (Series 2) — https://www.intel.com/content/www/us/en/ark/products/series/241071/intel-core-ultra-processors-series-2.html (seen via search only)
5. Intel Core Ultra 200S Plus quick reference guide (PDF, text extracted locally) — https://cdrdv2-public.intel.com/874112/intel-core-ultra-200s-plus-series-processors-quick-reference-guide-ph2-public.pdf
6. Windows Central / heise coverage of 200S Plus (via search summary) — https://www.windowscentral.com/hardware/intel/announces-new-core-ultra-200s-plus-series-desktop-processors ; https://www.heise.de/en/news/Core-Ultra-200S-Plus-Intel-gives-mid-range-CPUs-more-cores-11207720.html
7. HWCooling, Arrow Lake Refresh launched — https://www.hwcooling.net/en/arrow-lake-refresh-intel-desktop-cpus-launched-models-and-pricing/
8. Tom's Hardware, Nova Lake launch schedule leak (headline only readable) — https://www.tomshardware.com/pc-components/cpus/intels-core-ultra-400-nova-lake-launch-schedule-leaks-out-mass-production-in-q4-first-nova-lake-cpus-in-q1-2027
9. TechSpot, Intel confirms Nova Lake late 2026 (via search); Wccftech Nova Lake Q1 2027 — https://www.techspot.com/news/111047-intel-confirms-nova-lake-core-ultra-400-cpus.html ; https://wccftech.com/intel-nova-lake-core-ultra-400-q1-2027-launch-lga-1954-razor-lake-hammer-lake-desktop-cpus/
10. AMD blog, Computex 2026: 10 Years of AM4, AM5 Support Through 2029 (direct fetch timed out; content via search summary) — https://amd.com/en/blogs/2026/amd-computex-2026-10-years-of-am4-am5-support-through.html
11. AMD Socket AM4 chipsets page (direct fetch timed out; search summary) — https://www.amd.com/en/products/processors/chipsets/am4.html
12. Tom's Hardware, AMD confirms AM5 support through 2029 — https://tomshardware.com/pc-components/cpus/amd-confirms-am5-support-through-2029-zen-4-and-5-platform-will-likely-see-two-more-generations-at-least
13. AMD Socket AM5 chipsets page (direct fetch timed out; search summary) — https://www.amd.com/en/products/processors/chipsets/am5.html
14. HotHardware / Guru3D, AMD docs confirm Zen 6 Olympic Ridge and Medusa1 on AM5 (HotHardware 403; via search) — https://hothardware.com/news/amd-docs-confirm-am5-zen6-upgrade ; https://www.guru3d.com/story/amd-confirms-zen-6-olympic-ridge-and-medusa1-processors-for-socket-am5/
15. AMD Ryzen AI 7 450GE page (fetch timed out; search summary) and Tom's Hardware Ryzen AI 400 desktop — https://www.amd.com/en/products/processors/desktops/ryzen/ai-400-series/amd-ryzen-ai-7-450ge.html
16. Intel ARK Desktop Chipsets table — https://www.intel.com/content/www/us/en/ark/products/series/46645/desktop-chipsets.html
17. Intel ARK Z790 chipset — https://www.intel.com/content/www/us/en/products/sku/229721/intel-z790-chipset/specifications.html
18. Intel ARK B760 chipset (via search) and 700 series PCH datasheet — https://www.intel.com/content/www/us/en/products/sku/229719/intel-b760-chipset/specifications.html ; https://cdrdv2-public.intel.com/743835/743835-004.pdf
19. Intel Z890 datasheet notes (via search) — https://cdrdv2-public.intel.com/833778/833778-003.pdf
20. Intel ARK B860 chipset — https://www.intel.com/content/www/us/en/products/sku/241152/intel-b860-chipset/specifications.html
21. Intel ARK H810 chipset — https://www.intel.com/content/www/us/en/products/sku/241150/intel-h810-chipset/specifications.html
22. HWCooling, X870/X870E/B850/B840 features (via search) — https://hwcooling.net/en/x870-x870e-b850-and-b840-boards-for-amd-differences-and-release-dates
23. Guru3D / Corsair B850 vs B840 / TechPowerUp 9600X review (via search) — https://www.corsair.com/explorer/gamer/gaming-laptops/b850-vs-b840-which-chipset-should-you-choose/
24. Intel, Required BIOS Updates for 600 and 700 Series with 13th/14th gen (reviewed 02/05/2026) — https://www.intel.com/content/www/us/en/support/articles/000092294/processors.html
25. Intel, 13th and 14th Gen Desktop Processor Vmin Shift Instability Issue, article 000102331 (reviewed 07/21/2026) — https://www.intel.com/content/www/us/en/support/articles/000102331/processors.html
26. Intel Community, Vmin Shift update, microcode 0x12F (posted 2025-05-01) — https://community.intel.com/t5/Mobile-and-Desktop-Processors/Intel-Core-13th-and-14th-Gen-Vmin-Shift-Instabilty-Update-New/m-p/1686948
27. AMD FAQ, BIOS Updates for AMD Ryzen Desktop Systems (fetch timed out; search summary) — https://www.amd.com/en/resources/support-articles/faqs/cpu-99.html
28. HWCooling, Official Ryzen 5000 support for B350/X370 — https://www.hwcooling.net/en/official-ryzen-5000-support-finally-coming-to-b350-x370-boards/
29. PCWorld, Is your X370/B350/A320 board compatible with Ryzen 5000 — https://www.pcworld.com/article/702539/is-your-amd-x370-b350-or-a320-motherboard-compatible-with-ryzen-5000-heres-how-to-find-out.html (via search)
30. Wccftech / KitGuru, AGESA 1.2.0.0 for Ryzen 9000 on 600 series (mid-2024) — https://wccftech.com/gigabyte-agesa-1-2-0-0a-bios-am5-motherboards-amd-ryzen-9000-cpus/
31. BIOS Flashback explainers and forum reports (via search) — https://evezone.evetech.co.za/deep-dives/bios-flashback-explained-when-it-helps-on-an-am5-motherboard-and-why-it-matters
32. Intel ARK Core Ultra 7 265 (page fetched was the 265, 6400 MT/s) — https://www.intel.com/content/www/us/en/products/sku/241068/intel-core-ultra-7-processor-265-30m-cache-up-to-5-30-ghz/specifications.html
33. Intel ARK Core Ultra 7 270K Plus — https://www.intel.com/content/www/us/en/products/sku/245692/intel-core-ultra-7-processor-270k-plus-36m-cache-up-to-5-50-ghz/specifications.html
34. Kingston Z890 compatibility listings quoting Intel population rules (via search) — https://kingston.com/de/memory/search/model/110147/asus-rog-maximus-z890-extreme
35. Corsair, CUDIMM on chipsets earlier than Z890 (via search) — https://help.corsair.com/hc/en-us/articles/31013025623313-Memory-CUDIMM-on-chipsets-earlier-than-Z890
36. AMD Ryzen 7 7700X / 8700G pages (via search summary) — https://www.amd.com/en/products/processors/desktops/ryzen/7000-series/amd-ryzen-7-7700x.html ; https://www.amd.com/en/products/processors/desktops/ryzen/8000-series/amd-ryzen-7-8700g.html
37. AMD Ryzen 9 9950X page and AMD community thread on 4-DIMM speed (via search summary) — https://www.amd.com/en/products/processors/desktops/ryzen/9000-series/amd-ryzen-9-9950x.html ; https://pcforum.amd.com/s/question/0D5Pd00001hf0kOKAQ/ryzen-9-9950x-4dimm-ram-speed-drops-to-3200-mhz-any-hope-for-zen-6
38. Wccftech, AMD confirms DDR5-6000 sweet spot for Ryzen 7000 — https://wccftech.com/amd-confirms-ryzen-7000-ddr5-6000-memory-sweet-spot-auto-fclk-recommended-for-overclocking/
39. Igor's Lab, Ryzen 7000 tuning guide — https://igorslab.de/en/ryzen-7000-tuning-guide-infinity-fabric-expo-dual-rank-samsung-and-hynix-ddr5-in-practice-test-with-benchmarks-recommendations/10 ; TechPowerUp (403) https://techpowerup.com/298436/amd-confirms-ddr5-6000-as-sweetspot-memory-oc-frequency-for-ryzen-7000
40. HotHardware, EXPO explained; Corsair XMP vs EXPO; Wccftech MSI EXPO/XMP (via search) — https://hothardware.com/news/amd-expo-ddr5-memory-hype ; https://www.corsair.com/de/cs/explorer/diy-builder/memory/xmp-vs-expo-whats-the-difference/
41. ASRock forum AM5 ECC thread; Level1Techs ECC AM5 threads — https://forum.asrock.com/am5-ecc-supportpound_topic24901.html ; https://forum.level1techs.com/t/ecc-capable-verified-motherboards-for-ryzen-7000/197891
42. Tom's Hardware / heise / Notebookcheck, Bartlett Lake-S Core 200E — https://www.tomshardware.com/pc-components/cpus/intel-bartlett-lake-s-cpus-reportedly-wield-12-blazing-p-cores-and-5-8-ghz-boost-turbocharged-chips-that-will-not-make-it-to-retail
