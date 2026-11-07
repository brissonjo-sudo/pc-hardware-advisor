# Memory (RAM) compatibility

Last checked: 2026-11-07. Values change: verify online before concluding.

Use this file to judge RAM-board-CPU compatibility for the `check-compatibility` and `build-config` skills. All tables are dated 2026-11-07. Confidence: high = primary page (Intel ARK, Intel guide, ASUS support page) read; medium = reputable press, vendor page for one product, or an AMD page seen only through a search summary; low = forum or single mention.

## Rules for Claude

- amd.com pages (CPU spec tables, EXPO page) could not be read automatically on 2026-11-07 (timeouts). Try once. If blocked, record `blocked (timeout)`, rely on the board vendor's pages, or ask the user for a screenshot of the AMD spec table. Do not circumvent.
- The board vendor's memory QVL (qualified vendor list) and CPU support list decide real behaviour, including 4-DIMM speeds and capacity. Send Claude there for the final word. Official CPU speeds are the ceiling for guaranteed operation; XMP/EXPO speeds above them are overclocks.
- Show conflicting values side by side with sources. Do not pick one.

## DDR4 and DDR5 per platform (checked 2026-11-07)

| Platform | Memory type | Rule | Source | Confidence |
|---|---|---|---|---|
| LGA1700 (12th/13th/14th gen) | DDR4 or DDR5, fixed per board | The CPU supports both; each board has only one slot type. Treat DDR4 and DDR5 as incompatible with each other on a board; read the board's spec page | [1] [2] | high for CPU limits; medium for "never both" (slot keying and board design, recalled, not read on an Intel page) |
| LGA1851 (Core Ultra 200S / 200S Plus) | DDR5 only | A DDR4 kit is incompatible | [3] [4] | high |
| AM4 | DDR4 only | A DDR5 kit is incompatible. AMD official max speed per generation not captured | - | medium |
| AM5 | DDR5 only (UDIMM) | A DDR4 kit or an RDIMM kit is incompatible | [13] [14] | high (DDR5), medium (UDIMM only) |

## Official supported speeds

### Intel LGA1700
- 12th gen: DDR5-4800 or DDR4-3200. 13th/14th gen: DDR5 up to 5600 MT/s, DDR4 up to 3200 MT/s [1] [2] (high). Intel's compatibility page shows "4800/5600" for DDR5 because i3/Pentium-class parts differ.
- Max capacity 192 GB (Core i9-14900K ARK), 2 channels. The ARK ECC flag needs an ECC-capable chipset and board (Z790 ARK: ECC not supported) [1] [12] (high).
- 1DPC vs 2DPC reductions for LGA1700: not captured from an Intel page. Gap; use the board QVL.

### Intel LGA1851
- Core Ultra 7 265 (original 200S, ARK): DDR5 up to 6400 MT/s, 256 GB, 2 channels, ECC flag [3] (high).
- Core Ultra 7 270K Plus (200S Plus, ARK, launch Q1 2026): DDR5 up to 7200 MT/s, 256 GB, 2 channels, ECC flag [4] (high).
- Intel quick reference guide: "Maximum memory speeds are associated with 1DPC. Additional DIMM loading on any channel may impact maximum memory speed." Up to DDR5-7200 at 1DPC with CUDIMM 1Rx8, 1Rx16, 2Rx8. Max capacity needs 2DPC [5] (high).
- Kingston Z890 listings citing Intel population rules for the original 200S (vendor secondary, medium) [7]: 1DPC 1R/2R up to 5600 MT/s; 2DPC 1R up to 4800; 2DPC 2R up to 4400; DDR5-6400 CUDIMM at 1DPC requires a K-class CPU, non-K CPUs fall to 5600 or lower. These are original-200S values; Intel's own 2DPC table for 200S and 200S Plus was not read (gap).
- Conflict to note: Intel ARK gives 6400 (265) and 7200 (270K Plus) as maximums [3] [4], while the Kingston-cited population rules give 5600 / 4800 / 4400 depending on ranks and DIMMs per channel [7]. The ARK maximum is the 1DPC best case.

### Intel chipset memory features
- Z890 and B860 allow memory OC; H810 does not and has one DIMM per channel (two slots total) [9] [10] [11]. H610 memory OC is blank on ARK [9].
- "200S Boost" requires a Z890 board plus XMP memory [5].

### AMD AM4
- DDR4 only. AMD's official max speed per generation was not captured. Gap. Use the board QVL and CPU page, and tell the user the value is not verified.

### AMD AM5 (medium: AMD spec pages seen through search summaries)
AMD lists "2x1R, 2x2R, 4x1R, 4x2R" with the DIMM count, not 1DPC/2DPC [14].

| CPU | 2 DIMMs (1R or 2R) | 4 DIMMs | Max capacity listed | Source |
|---|---|---|---|---|
| Ryzen 7 7700X | DDR5-5200 | DDR5-3600 | 128 GB | [13] |
| Ryzen 7 8700G | DDR5-5200 | DDR5-3600 | 256 GB | [13] |
| Ryzen 9 9950X | DDR5-5600 | DDR5-3600 | 256 GB on the 9950X page | [14] |
| Ryzen AI 7 450GE (OEM) | DDR5-5600 | DDR5-3600 | 256 GB, ECC "with motherboard support" | [15] |

Capacity conflict within one family: AMD shop pages for the 9950X3D and 9900X3D show 192 GB while the 9950X page shows 256 GB [14]. Capacity depends on the SKU page; read the specific SKU. ASUS PRIME X870-P WIFI spec page (high, vendor): four DDR5 DIMM slots, up to 256 GB total, overclocked speeds 8000+ MT/s with Ryzen 7000/8000/9000, ECC and non-ECC UDIMM, profiles AMD EXPO and ASUS AEMP; "supported memory types, speeds and module counts vary by CPU and configuration" [20].

## 1DPC vs 2DPC and 4-DIMM speed drops

- Intel: the stated maximum applies to 1DPC; extra loading reduces it [5]. Intel ARK says to refer to ark.intel.com for 2DPC; the official table was not read.
- AMD: 4 DIMMs are listed at DDR5-3600 on the spec pages above [13] [14]. Real-world reports of 4 DIMMs landing at 3200-3600 on Ryzen 9000 exist in an AMD community forum thread (low) [14].
- Verdict rule: for a 4-DIMM build, never promise the kit's rated speed. State the official 4-DIMM speed (AMD 3600) or Intel's "may impact" wording and ask the user to check the board QVL. For maximum speed, recommend 2 DIMMs (AM5) or 1DPC (LGA1851).

## CUDIMM on Intel 800 series

- Intel: DDR5-7200 at 1DPC with CUDIMM 1Rx8, 1Rx16, 2Rx8 on the 200S Plus [5]. The 4-rank CUDIMM is "emerging, supported on select 800-series boards" [5].
- HWCooling (press, medium): the official 7200 applies to CUDIMM; quad-rank support expected, up to 128 GB per module and 512 GB total on some boards [6].
- Corsair support page (medium): on Z890 the CUDIMM clock driver can run in PLL mode; on older platforms CUDIMM works only in bypass mode [8]. A CUDIMM kit on an older platform therefore runs without its clock-driver benefit; say so as a condition.
- Verdict rule: a CUDIMM kit on LGA1851 at 1DPC is compatible; DDR5-7200 is the official 200S Plus maximum at 1DPC, and the original 200S maximum is 6400 [3] [4] [5]. A rated speed above the CPU maximum is an overclock: conditional.

## AM5 memory controller ratio and the DDR5-6000 sweet spot

- Source: a 2022 AMD staff Discord AMA relayed by Wccftech, TechSpot and Igor's Lab. No AMD-published page was found; TechPowerUp returned 403. Confidence: medium [16] [17].
- As relayed: DDR5-6000 is the best balance of cost, stability and performance on Ryzen 7000. EXPO DDR5-6000 runs UCLK:MCLK 1:1 with FCLK on auto (default 1733 MHz on Ryzen 7000 at that time). Above 6000 the controller runs UCLK:MCLK 2:1. Igor's Lab: EXPO 6000 with FCLK 2000 MHz is the best compromise [16] [17].
- AMD's EXPO page (search listing, not opened, low): AMD's own March 2026 test used a Ryzen 7 9700X with 32 GB DDR5-6000 EXPO at CL28/30/36. This shows 6000 as a reference test point, not a stated recommendation [24].
- Rule: describe DDR5-6000 as "commonly cited sweet spot, from 2022 press relaying AMD, medium confidence". Do not call it an AMD specification, and do not extend the 1:1 claim to Ryzen 9000 without a source.
- AMD announced EXPO "Ultra Low Latency" profiles at Computex 2026, no date [25] (medium).

## XMP vs EXPO on AM5

- ASUS support FAQ 1042256, last updated 2026-09-10 (high) [19]: AM5 and newer with an EXPO kit uses the BIOS option "EXPO I"; AM5 and newer with an XMP kit uses **DOCP**; AMD before AM5 with XMP uses DOCP (no EXPO). If the DRAM supports XMP, set Ai Overclock Tuner to DOCP. "Not all ASUS motherboards or RAM kits will support XMP Tweaked". ASUS advises using DRAMs in the QVL.
- ASUS also offers AEMP (ASUS Enhanced Memory Profile) for kits with neither EXPO nor XMP; it is an ASUS feature, not an AMD one [20] [21] (medium/high).
- Gigabyte (medium, press of a company release, PCGH 2022-09-17): all AM5 boards support EXPO and the company "will continue to offer XMP support" [22].
- Press (medium/low) [18]: XMP-only kits usually work on AM5 but may need the profile enabled manually, may not reach rated speed, and default to JEDEC (for example DDR5-4800) until a profile is enabled. MSI and Gigabyte say their boards read both XMP and EXPO. Option names for MSI, Gigabyte and ASRock were not verified; do not quote them. No AMD statement on XMP-only kits was found (amd.com blocked).
- Verdict rule for a high-speed XMP-only kit (for example DDR5-7200) on AM5: **compatible with conditions**. It works physically; it boots at default JEDEC speed; enable the profile (ASUS: DOCP) or set manual values, expect to run around 6000 for 1:1 controller operation; the rated speed is not guaranteed because above 6000 the controller runs 2:1 and is less efficient, and the QVL decides. Never give "compatible" without the speed condition. A kit with EXPO is the lower-risk match for AM5; an EXPO-only kit on Intel is the mirror case (check the board's profile support, not verified here).

## Capacity limits and non-binary DIMMs

- Capacity only as sourced above: LGA1700 192 GB (14900K ARK) [1]; LGA1851 256 GB (265 and 270K Plus ARK) [3] [4]; AM5 128, 192 or 256 GB depending on the SKU page [13] [14]; ASUS X870 board up to 256 GB [20].
- Intel 4-rank CUDIMM and up to 128 GB per module / 512 GB total are press/Intel statements limited to select 800-series boards [5] [6].
- 64 GB DIMMs on AM5 and the BIOS needed for 256 GB: not found. Non-binary 24 and 48 GB DIMM support per platform: not verified. For both, state "not verified", point to the board QVL and the vendor's BIOS notes.

## ECC on AM5 (medium/low)

AM5 takes UDIMM only. Ryzen CPU pages list ECC "supported with motherboard support". Board support varies: ASUS lists ECC and non-ECC UDIMM on the X870 spec page [20]; ASRock spec pages vary and changed over time (forum evidence); ASRock and Level1Techs threads exist [23]. DDR5 on-die ECC is not full ECC. Rule: ECC works only if the CPU, board and DIMMs all support it; require the board's spec page or QVL to say so, otherwise "not verified".

## Verdict rules for RAM pairs

1. Different generation (DDR4 vs DDR5), or RDIMM on a UDIMM board: **incompatible**. Source: board spec page and the CPU's ARK/AMD page.
2. Same type, kit speed at or below the CPU's official speed for the DIMM configuration: **compatible**, confidence per the table above. Name the DIMM count assumed.
3. Kit rated above the official speed: **compatible with conditions**. Condition: enable XMP/EXPO (or ASUS DOCP/AEMP) in BIOS; the speed is an overclock and is not guaranteed; check the QVL.
4. Four DIMMs: **compatible with conditions**; speeds drop (AMD 3600 listed; Intel 1DPC maximum). Check the QVL.
5. XMP-only kit on AM5: see the rule above. CUDIMM on LGA1851: see the CUDIMM section. CUDIMM on an older platform: conditions (bypass mode only).
6. Capacity above the CPU or board maximum, or non-binary DIMMs not listed by the vendor: **cannot conclude** until the QVL or BIOS notes confirm.
7. ECC: **cannot conclude** unless the board page states ECC support.
8. Never give a final verdict from this file alone; cite the board QVL or spec page when available.

## Not verified

- amd.com blocked (timeout): all AMD CPU spec tables, the EXPO page, the AM4/AM5 chipset pages. AMD memory speeds above come from search summaries (medium).
- AM4 official max memory speed per generation.
- LGA1700 1DPC/2DPC official table; Intel's 2DPC table for 200S and 200S Plus (only Kingston values for the original 200S).
- Non-binary 24/48 GB DIMM support; 64 GB DIMM support on AM5 and the BIOS needed for 256 GB.
- A primary AMD statement for the DDR5-6000 sweet spot, and for UCLK:MCLK 1:1 and FCLK behaviour on Ryzen 9000.
- Vendor statements on XMP-only kits other than ASUS (high) and Gigabyte (medium); MSI, Gigabyte and ASRock option names; behaviour of a DDR5-7200 XMP kit on AM5 beyond press (low-medium).
- EXPO-only kits on Intel boards.
- JEDEC pages (JESD79-5 speeds) not read.
- Intel ARK pages for i5-12400 and i5-13500 redirected to other SKUs; 12th gen figures come from Intel's compatibility article [2].

## Sources

All checked 2026-11-07.

1. Intel ARK Core i9-14900K: https://www.intel.com/content/www/us/en/products/sku/236773/intel-core-i9-processor-14900k-36m-cache-up-to-6-00-ghz/specifications.html
2. Intel, Compatibility of Intel Core Desktop Processors (12th, 13th, 14th gen), article 000092149: https://www.intel.com/content/www/us/en/support/articles/000092149/processors.html
3. Intel ARK Core Ultra 7 265 (6400 MT/s): https://www.intel.com/content/www/us/en/products/sku/241068/intel-core-ultra-7-processor-265-30m-cache-up-to-5-30-ghz/specifications.html
4. Intel ARK Core Ultra 7 270K Plus: https://www.intel.com/content/www/us/en/products/sku/245692/intel-core-ultra-7-processor-270k-plus-36m-cache-up-to-5-50-ghz/specifications.html
5. Intel Core Ultra 200S Plus quick reference guide (PDF): https://cdrdv2-public.intel.com/874112/intel-core-ultra-200s-plus-series-processors-quick-reference-guide-ph2-public.pdf
6. HWCooling, Arrow Lake Refresh launched: https://www.hwcooling.net/en/arrow-lake-refresh-intel-desktop-cpus-launched-models-and-pricing/
7. Kingston Z890 compatibility listings quoting Intel population rules (via search): https://kingston.com/de/memory/search/model/110147/asus-rog-maximus-z890-extreme
8. Corsair, CUDIMM on chipsets earlier than Z890 (via search): https://help.corsair.com/hc/en-us/articles/31013025623313-Memory-CUDIMM-on-chipsets-earlier-than-Z890
9. Intel ARK Desktop Chipsets table: https://www.intel.com/content/www/us/en/ark/products/series/46645/desktop-chipsets.html
10. Intel ARK B860 chipset: https://www.intel.com/content/www/us/en/products/sku/241152/intel-b860-chipset/specifications.html
11. Intel ARK H810 chipset: https://www.intel.com/content/www/us/en/products/sku/241150/intel-h810-chipset/specifications.html
12. Intel ARK Z790 chipset: https://www.intel.com/content/www/us/en/products/sku/229721/intel-z790-chipset/specifications.html
13. AMD Ryzen 7 7700X / 8700G pages (search summary; amd.com timeouts): https://www.amd.com/en/products/processors/desktops/ryzen/7000-series/amd-ryzen-7-7700x.html ; https://www.amd.com/en/products/processors/desktops/ryzen/8000-series/amd-ryzen-7-8700g.html
14. AMD Ryzen 9 9950X page and AMD community thread on 4-DIMM speed (search summary): https://www.amd.com/en/products/processors/desktops/ryzen/9000-series/amd-ryzen-9-9950x.html ; https://pcforum.amd.com/s/question/0D5Pd00001hf0kOKAQ/ryzen-9-9950x-4dimm-ram-speed-drops-to-3200-mhz-any-hope-for-zen-6
15. AMD Ryzen AI 7 450GE page (timeout; search summary): https://www.amd.com/en/products/processors/desktops/ryzen/ai-400-series/amd-ryzen-ai-7-450ge.html
16. Wccftech, AMD confirms DDR5-6000 sweet spot for Ryzen 7000 (2022): https://wccftech.com/amd-confirms-ryzen-7000-ddr5-6000-memory-sweet-spot-auto-fclk-recommended-for-overclocking/
17. Igor's Lab, Ryzen 7000 tuning guide; TechPowerUp (403, not read): https://igorslab.de/en/ryzen-7000-tuning-guide-infinity-fabric-expo-dual-rank-samsung-and-hynix-ddr5-in-practice-test-with-benchmarks-recommendations/10 ; https://techpowerup.com/298436/amd-confirms-ddr5-6000-as-sweetspot-memory-oc-frequency-for-ryzen-7000
18. HotHardware, EXPO explained; Corsair, XMP vs EXPO; Wccftech on MSI EXPO/XMP (via search): https://hothardware.com/news/amd-expo-ddr5-memory-hype ; https://www.corsair.com/de/cs/explorer/diy-builder/memory/xmp-vs-expo-whats-the-difference/
19. ASUS support FAQ 1042256, XMP/EXPO/DOCP (last update 2026-09-10): https://www.asus.com/support/faq/1042256/
20. ASUS PRIME X870-P WIFI tech specs: https://www.asus.com/motherboards-components/motherboards/prime/prime-x870-p-wifi/techspec/
21. ASUS Edge Up, XMP vs EXPO vs AEMP (search summary): https://edgeup.asus.com/2026/xmp-vs-expo-vs-aemp-unlock-your-rams-potential-with-memory-profiles-and-more/
22. PC Games Hardware, Gigabyte EXPO support (2022-09-17): https://www.pcgameshardware.de/Mainboard-Hardware-154107/News/Gigabyte-EXPO-Support-DDR5-1403588/
23. ASRock forum AM5 ECC thread; Level1Techs ECC AM5 threads: https://forum.asrock.com/am5-ecc-supportpound_topic24901.html ; https://forum.level1techs.com/t/ecc-capable-verified-motherboards-for-ryzen-7000/197891
24. AMD EXPO page (blocked: timeout; search snippet only): https://www.amd.com/en/products/processors/technologies/expo.html
25. AMD blog, Computex 2026 (blocked: timeout; search summary): https://amd.com/en/blogs/2026/amd-computex-2026-10-years-of-am4-am5-support-through.html
