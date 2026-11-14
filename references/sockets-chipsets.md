# Sockets, chipsets and BIOS

Last checked: 2026-11-07. Values change: verify online before concluding.

Use this file to judge CPU-board compatibility (socket, chipset, BIOS) for the `check-compatibility` and `build-config` skills. Every table below is dated 2026-11-07. Confidence levels come from research: high = primary page (Intel ARK, Intel support article, ASUS page) read; medium = reputable press, vendor page for one board, or a primary page seen only through a search summary; low = leak, forum, recall.

## Rules for Claude

- amd.com pages could not be read automatically on 2026-11-07 (HTTP timeouts, 2 tries each, on the AM4 and AM5 chipset pages, the Computex 2026 blog, CPU spec pages, the EXPO page and FAQ cpu-99). Try an amd.com page once. If it times out or is blocked, record it as `blocked (timeout)`, do not use caches, mirrors or archive copies, then rely on the board vendor's pages (ASUS, MSI, Gigabyte, ASRock) or ask the user for a screenshot or pasted text of the AMD page.
- The board vendor's CPU support list is the final word on whether a CPU boots on a board and from which BIOS. Chipset tables and this file only tell you where to look.
- When sources disagree, show both values with their sources and lower the confidence. Do not pick one silently.
- Never state a leak or rumour as a product fact.

## Platform overview (checked 2026-11-07)

| Socket | CPU families | Chipsets | Memory | Status 2026 | Source | Confidence |
|---|---|---|---|---|---|---|
| LGA1700 | Core 12th gen (Alder Lake), 13th gen (Raptor Lake), 14th gen (Raptor Lake Refresh). Not 6th-11th gen | 600 series (Z690, H670, B660, H610) and 700 series (Z790, H770, B760) | DDR4 or DDR5, fixed per board | Mature, end of line for retail. 12th/13th/14th gen all listed as compatible by Intel | [1] [2] | high (socket, chipsets, speeds); medium ("DDR4 or DDR5 per board, never both") |
| LGA1851 | Core Ultra 200S (Arrow Lake-S, launched Q1 2025) and Core Ultra 200S Plus (Arrow Lake Refresh: Core Ultra 7 270K Plus, Core Ultra 5 250K Plus, retail 2026-03-26) | 800 series: Z890, B860, H810 (also Q870, W880 workstation/pro) | DDR5 only | Current Intel mainstream desktop platform. Intel: all existing 800-series boards support the 200S Plus | [3] [4] [5] [6] [36] | high |
| AM4 | Ryzen 1000 to 5000, plus 5000G/4000G APUs | A320, B350, X370, B450, X470, B550, X570, A520 | DDR4 | Legacy. AMD marked "10 years of AM4" at Computex 2026 | [9] [10] | medium |
| AM5 | Ryzen 7000, 8000G, 9000 (incl. 9000X3D, 9950X3D2 Dual Edition, 7700X3D); Ryzen AI 400 desktop APUs (OEM only, 2026) | 600 series: A620 (A620A), B650, B650E, X670, X670E. 800 series: B840, B850, X870, X870E | DDR5 only (UDIMM) | Current AMD platform. AMD states support "through 2029" (see longevity section) | [9] [10] [37] | high (chipset list); medium (2029 statement, quotes relayed) |
| LGA1954 (Nova Lake-S, "Core Ultra 400" expected) | Not released | 900 series reported (Z990, Z970, B960...) | DDR5 (reported) | LEAK-ONLY. Not released as of 2026-11-07. Intel only said "end of 2026" (Q4 2025 earnings call, via press). Leaks: mass production Q4 2026, first CPUs Q1 2027. No ARK page, no retail | [7] [8] | low (socket, chipset names); medium (Intel timing statement) |
| AM5 with Zen 6 (Olympic Ridge desktop, Medusa1 APU) | Not launched | Existing AM5 boards | DDR5 | Press says AMD web documentation names these products for AM5 (2026-08). No AMD launch date. Press expects early 2027. Do not state a Zen 6 CPU is compatible with a given board | [11] | medium (existence on AM5); low (timing) |

LGA1700 memory note: Intel's compatibility page gives DDR5 and DDR4 limits per generation but does not say "one board = one type". The rule that a board is DDR4 or DDR5 and never both comes from DIMM slot keying and board design (recalled, widely known, not read on an Intel page). Treat as medium and confirm on the board's spec page.

## Intel chipset capabilities (checked 2026-11-07)

CPU OC and memory OC from Intel ARK desktop chipsets table [14]. Lane counts are chipset lanes unless stated.

| Chipset | CPU OC | Memory OC | PCIe (CPU / chipset) | Notes | Source |
|---|---|---|---|---|---|
| Z790 | Yes | Yes | CPU: PCIe 5.0 1x16 or 2x8, plus PCIe 4.0 1x4. Chipset: up to 28 lanes, PCIe 3.0/4.0, DMI 4.0 x8 | 2 DIMMs per channel, no ECC. Launch Q4 2022 | [14] [15] |
| H770 | No | Yes | PCIe 3.0/4.0; lane count not verified | | [14] |
| B760 | No | Yes | CPU: PCIe 5.0 1x16, PCIe 4.0 1x4. Chipset: 14 lanes max per ARK; the datasheet gives 4 Gen3 + 10 Gen4 and is internally inconsistent. DMI 4.0 x4 | Quote 14 as "per ARK", flag the inconsistency | [14] [16] |
| Z690 | Yes | Yes | PCIe 3.0/4.0; lane count not verified | | [14] |
| H670 / B660 | No | Yes | PCIe 3.0/4.0; lane counts not verified | | [14] |
| H610 | No (nothing listed) | Not listed (blank on ARK) | Chipset PCIe 3.0 only | | [14] |
| Z890 | Yes (IA, BCLK, Memory) | Yes | CPU: PCIe 5.0 1x16+1x4, 2x8+1x4 or 1x8+3x4; PCIe 4.0 1x4. Chipset: 24 lanes PCIe 4.0, DMI 4.0 x8 | 2 DPC; launch Q4 2024. Only 800-series chipset with CPU OC and "200S Boost" | [3] [14] |
| B860 | No | Yes | CPU: PCIe 5.0 1x16+1x4. Chipset: 14 lanes PCIe 4.0, DMI 4.0 x4 | 2 DPC; launch Q1 2025 | [14] [17] |
| H810 | No | No | CPU: PCIe 5.0 x16 only. Chipset: 8 lanes PCIe 4.0, DMI x4 | 1 DIMM per channel (boards have 2 slots total); launch Q1 2025 | [14] [18] |

"200S Boost" (Intel) requires a Z890 board plus XMP memory [4].

## AMD chipset capabilities (checked 2026-11-07, amd.com blocked)

AMD's chipset pages could not be read. The table mixes ASUS (high for ASUS products, medium as a chipset rule), HWCooling (pre-launch, 2024-08-28 / 2024-09-05), and a Corsair comparison table that appears to mirror AMD's. Anything marked "not re-verified" is recalled or from a search summary.

| Chipset | CPU OC | Memory OC | GPU slot (CPU lanes) | M.2 (CPU lanes) | USB4 | Notes | Source | Confidence |
|---|---|---|---|---|---|---|---|---|
| A620 / A620A | No (press) | Yes (EXPO) | PCIe 4.0, not verified | PCIe 4.0, not verified | not required | Entry level | [12] | low |
| B650 | Yes | Yes | 5.0 optional (vendor choice) | one 5.0 M.2 required (recalled) | optional | Not re-verified | [12] | low |
| B650E / X670E | Yes | Yes | 5.0 mandatory | 5.0 mandatory | optional on 600 series (HWCooling) | X670/X670E use two chipset dies; B650/B650E one | [19] | medium |
| X670 | Yes | Yes | 5.0 optional | 5.0 M.2 | optional | two dies | [19] | low |
| B840 | No (Corsair; HWCooling: reportedly not) | Yes (EXPO/XMP/manual) | PCIe 4.0 per Corsair and the ASUS board page (see below) | PCIe 4.0 x4 (Corsair); 3.0/4.0 (ASUS) | optional, needs extra chip | Corsair: 34 total chipset lanes, 0 PCIe 5.0 | [19] [20] [21] | medium |
| B850 | Yes (Corsair); ASUS: AI OC features only on some models | Yes | CONFLICT, see below | PCIe 5.0 x4 (Corsair, HWCooling; ASUS: 1 to 3 slots) | optional, extra chip required | Corsair: 36 chipset lanes, 4 PCIe 5.0 | [19] [20] [21] | medium |
| X870 | not stated by HWCooling; ASUS lists AI OC on most | Yes | PCIe 5.0 x16 | PCIe 5.0 (ASUS: two or more 5.0 M.2) | Required (HWCooling); ASUS PRIME X870-P WIFI has two rear USB4 | One Promontory 21 die + USB4 controller | [19] [21] [22] | medium |
| X870E | same as X870 | Yes (HWCooling: boards expected to reach DDR5-8000) | PCIe 5.0 x16 (or x8/x8) | PCIe 5.0 x4 | Required | Two Promontory 21 dies + ASM4242 USB4 controller; more PCIe 4.0 lanes, SATA, USB than X870 | [19] [21] | medium |

Conflicts, shown side by side:
- B840 GPU slot generation: Corsair table says PCIe 4.0 x16 or 2x8 [20]; the ASUS board page (PRIME B840-PLUS WIFI techspec, read 2026-11-08) says "1 x PCIe 4.0 x16 slot (supports x16 mode)"; the ASUS microsite says B840 is "PCIe 4.0 ready" and lists PCIe 4.0 and 3.0 M.2 [21]. A HWCooling pre-launch value of 3.0 is not supported by either and is dropped.
- B850 GPU slot generation: Corsair table says PCIe 4.0 x16/2x8 [20]; HWCooling pre-launch says PCIe 5.0 x16 optional, x8/x8 supported [19]; the ASUS microsite (read 2026-11-08) says B850 boards are "PCIe 5.0 ready", X870/X870E offer up to two PCIe 5.0 x16 slots, and B850 has PCIe 5.0 M.2 [21]. ASUS and HWCooling agree on 5.0 per board; Corsair says 4.0.

Do not state the B840 or B850 GPU-slot generation, or any 600-series GPU/M.2 rule, as fact. Read the specific board's spec page and quote it.

AMD's own rule, as relayed through a search summary of its chipset page (low): all AM5 boards with 600 or 800 series chipsets work with all AM5 processors, but a BIOS update may be needed for some Ryzen 8000/9000 on 600-series boards [12].

## CPU lane counts (as researched)

- Intel Core i9-14900K: 20 CPU lanes, PCIe 5.0/4.0 (ARK) [1] (high). Core Ultra 7 265: 24 lanes, PCIe 5.0/4.0 [3] (high).
- ASUS PRIME X870-P WIFI spec page, one board (high) [22]: Ryzen 9000 and 7000 give one PCIe 5.0 x16 slot (x16 mode). Ryzen 8000 gives one PCIe 4.0 x16 slot running x8/x4 mode (reduced lanes and PCIe 4.0). The X870 chipset adds three PCIe 4.0 slots. Warn the user that an 8000G APU lowers GPU slot lanes and generation.
- Press/search claims of 28 PCIe 5.0 lanes (24 usable) on Ryzen 7000 and 20 PCIe 4.0 lanes on the 8700G are unconfirmed on an AMD page (low) [39]. Do not quote them as AMD facts.

## BIOS requirements (checked 2026-11-07)

### Intel LGA1700 with 13th/14th gen
- Intel (support article 000092294, reviewed 2026-02-05, high): 600 and 700 series boards require a BIOS update to boot 13th/14th gen CPUs. An update may also be needed when moving between 12th, 13th and 14th gen. Contact the board maker for the BIOS [30].
- ASUS 600-series boards: Intel notes the ME firmware may need updating before the BIOS; see Intel article 000092983 (not read) [30].
- Intel compatibility page: 12th/13th/14th gen all use LGA1700 with 600 or 700 series. Not compatible with 500 series and older, nor with 800 series [2] (high).

### Intel LGA1851 with 200S Plus
- Intel (quick reference guide): all existing 800-series boards support the 200S Plus [4] (high). HWCooling: it should boot without a BIOS update, but an update is recommended [5] (medium). Tell the user to update the BIOS anyway when possible and to check the board's CPU list.

### AM4 (5000 and 5000X3D)
AMD's matrix was not read. The table is built from AMD's announced policy (via press) and ASUS per-board CPU lists. Chipset alone does not guarantee support; the per-board BIOS decides.

- A320, B350, X370: Ryzen 5000 only via "selective beta BIOS", board maker's choice, AGESA 1.2.0.7 required; earlier AGESA deliberately blocked Zen 3. AMD announcement 2022-03-15; press: 5800X3D needs AGESA 1.2.0.6B and explicit confirmation [27] [40] (medium).
- B450, X470: Ryzen 5000 per vendor BIOS. ASUS PRIME B450M-A II: 5000 from BIOS 2409 (5600X/5800X/5900X/5950X), 5800X3D from BIOS 3211 [25] (high, one board).
- A520: ASUS PRIME A520M-K: 5600X/5800X/5900X/5950X from BIOS 1004; 5600/5700X and 5800X3D from 2423; 5700X3D and 5600X3D from 2803 [26] (high, one board). 500 series launched with Zen 3 support; AGESA 1.0.8.0+ to boot Zen 3, 1.1.0.0 recommended (launch press, Oct 2020) [29] (medium).
- B550, X570: Ryzen 5000 yes; X3D needs a BIOS that lists it [28] [29] (medium).

- ASUS A520M-K, Ryzen 3000: mostly BIOS 0403; 3100/3300X 0305; 3000G APUs mostly 2803 [26] (high, one board).
- ComputerBase: AGESA 1.2.0.7 covers all Zen 3 CPUs on all AM4 chipsets, A320 through X570 (2020-12-04, updated to 2022-07). Gigabyte had only beta BIOS in that table at 2022-07-03 [28] (medium).
- AMD guidance (search summary of FAQ cpu-99, amd.com blocked, low-medium): check the maker's support page for the BIOS that supports the CPU; if the board cannot boot, flash with an older supported CPU, use USB BIOS Flashback if present, or contact the maker [33]. AMD AM4 chipset page (search summary): not all processors are supported on every chipset; some combinations are marked "Selective Beta BIOS update" [13].
- Use the ASUS minimums above as examples only. Never generalize one ASUS BIOS number to another board or vendor.

### AM5
Vendor "validated since BIOS" columns (ASUS codes are vendor-specific and say nothing about the AGESA version) [23] [24], high for these two boards:

| CPU family | 600-series: ASUS PRIME B650M-A WIFI II | 800-series: ASUS PRIME X870-P WIFI |
|---|---|---|
| Ryzen 7000 | 0602 for most; 7800X3D/7900X3D/7950X3D 1409; 7700X3D 3263; 7500X3D "ALL" | "all" for most; 7400 1063, 7500 1402, 7700X3D 1066 |
| Ryzen 8000G / 8000F | 1807 | 8000G: "all" |
| Ryzen 9000 | 2613 for most incl. 9600X, 9800X3D, 9950X3D; 3263 for e.g. 9500F and 9850X3D | "all" for 9600, 9600X, 9700X, 9900X, 9900X3D, 9950X, 9950X3D and 9800X3D; 9500F, 9700F 1063; 9850X3D, 9950X3D2 and some PRO 1066 |

Conclusion (high for these two boards, medium as a rule): on 600-series boards a BIOS update is needed for Ryzen 9000, 8000G/F and some 7000X3D, so an out-of-box board may need flash-without-CPU or an older CPU. On 800-series boards, 7000, 8000G and most 9000 including the 9800X3D are validated from the first BIOS, but newer SKUs (9850X3D, 9950X3D2, some PRO) need a later BIOS.

AGESA policy (medium): press (mid-2024) says AGESA 1.1.7.0 first enabled Ryzen 9000 boot on some 600-series boards and 1.2.0.0 broader [35]. No AGESA-per-SKU mapping was found on any primary page. Do not state AGESA minimums as rules; quote the vendor BIOS version from the board's CPU list instead.

## Flash-without-CPU features

Vendor names: ASUS BIOS FlashBack (named on an ASUS page, 2026, high) [21]; MSI Flash BIOS Button, Gigabyte Q-Flash Plus, ASRock BIOS Flashback (medium, from an explainer, not re-read) [34]. The feature needs only PSU connectors and a USB drive. It is a board feature, not a chipset feature. No reliable cross-vendor list of AM5 or LGA1851 boards with it exists. Check each board's spec page for the feature name; if absent, write "not verified" and do not assume. A forum report exists of an ASRock A620I where flashback failed (single case, low) [34].

## Intel 13th/14th Gen Vmin Shift instability

Source: Intel support article 000102331, last reviewed 2026-07-21 (high) [31].
- Affected scope as Intel states it: 13th and 14th Gen desktop processors, named in the article as i9, i7 and i5. The page names no SKU list.
- Intel's advice: run a BIOS with microcode 0x12F or later, and use "Intel Default Settings".
- Warranty: extended by 2 years, up to 5 years from the original purchase date, for eligible processors. Say "eligible" and send the user to Intel's article for eligibility; the terms were last reviewed 2026-07-21.
- Microcode timeline (Intel Community post by Intel staff, 2025-05-01, high for these two): 0x12B released September 2024; 0x12F supplements 0x12B, no change to the root cause, no measurable performance impact on the i9-14900K per Intel testing [32]. A separate Intel Community topic dated 2025-04-17 mentions 0x129 (content not read); 0x125 not checked (low).
- A community moderator claim that only K/KF/KS models are affected is NOT an Intel statement. Do not state a K-only scope as fact; say Intel lists i9, i7, i5 and names no SKU list [31] [32].
- For a used 13th/14th Gen CPU, the warranty depends on the original purchase date; ask for it.

## AM5 longevity statement

AMD blog "AMD Computex 2026: 10 Years of AM4, AM5 Support Through 2029 and Expanded RDNA 4 Gaming", English version dated 2026-05-31 per search summary. Wording as relayed: "With the launch of the Ryzen 7 7700X3D processor, we are extending support for the Socket AM5 platform through 2029." Previous commitment: "through 2027+". Confidence: medium, because the quotes come from search summary and Tom's Hardware (body truncated), and amd.com was blocked [9] [10]. The statement names no CPUs and does not confirm Zen 6 compatibility with any board. Phrase it as "AMD says it will support AM5 through 2029", not as a guarantee for a given board or CPU.

## LGA1851 future (checked 2026-11-14)

Intel has announced no CPU generation for LGA1851 after the 200S Plus refresh. Intel (VP John Pitzer, Goldman Sachs conference, 2025-09-10) named the Arrow Lake refresh and then Nova Lake, with no socket [41] (high for the quote). That Nova Lake uses a new socket, LGA1954, comes from press inference and leaks [41] [42] and from an Intel validation-tool listing named "LGA1954 NVL-Interposer" relayed by press [43] (medium). Phrase it as "no further CPU is announced for LGA1851; press reports a new socket for the next Intel generation", never as an Intel statement.

Use: when the user plans to upgrade only the CPU later, compare this with the AM5 statement above; for a full replacement later, the socket's future matters little.

## How to verify for a specific board

1. Read the board's exact model on the vendor product page (not the chipset name alone).
2. Open the vendor's CPU Support List for that board. Find the CPU's exact model and the minimum BIOS. Quote the BIOS version and the date of the page.
3. Compare with the BIOS the board ships with, if known (retail boards often ship older). If unknown, say so.
4. If the BIOS is too old, check the spec page for a flash-without-CPU feature (names above). If absent, the condition is an older supported CPU or vendor help.
5. For LGA1700 with 13th/14th Gen, state Intel's requirement of a BIOS update on 600/700 boards [30]; for instability, add microcode 0x12F or later and Intel Default Settings [31].
6. Intel Product Compatibility Tool (https://compatibleproducts.intel.com/, cited by a search summary, not opened) can be offered as a second check.
7. If the vendor page is blocked or JavaScript-only, record `blocked (<reason>)`, do not circumvent, and ask the user for a screenshot.

## Not verified

- amd.com blocked (timeout) on 2026-11-07: AM4 and AM5 chipset pages, Computex blog, CPU spec pages, EXPO page, FAQ cpu-99. All AMD-primary items remain open. Try once, then use board-vendor pages or a user screenshot.
- AM5 chipset tables for 600 series (A620, B650, B650E GPU/M.2 rules) not re-read on an AMD page; B840/B850 GPU slot generation in conflict (above).
- Full AM4 official matrix not captured; only ASUS B450M-A II and A520M-K lists. ASUS X370/B350/A320 pages returned no CPU list; an MSI page returned HTTP 403 (not bypassed).
- AGESA minimum per SKU (Ryzen 9000, 9800X3D on 600 series): not found on a primary page.
- CPU lane totals for Ryzen 7000/9000 (28/24) and 8000G (20): not confirmed on an AMD page.
- Intel lane counts for H770, Z690, H670, B660, H610; B760 datasheet inconsistent (14 vs other values).
- Whether Intel's Vmin scope is K-only or not: Intel names no SKU list. Microcode 0x129 and 0x125 content not read.
- Intel article 000092983 (ME firmware on ASUS 600 boards) not read.
- Nova Lake: nothing official beyond "2026" guidance; product, socket and chipset names are leaks. Zen 6 status relies on press.
- Two Intel tool redirects pointed to unrelated SKUs (suspicious) and were not followed.

## Sources

All checked 2026-11-07.

1. Intel ARK Core i9-14900K: https://www.intel.com/content/www/us/en/products/sku/236773/intel-core-i9-processor-14900k-36m-cache-up-to-6-00-ghz/specifications.html
2. Intel, Compatibility of Intel Core Desktop Processors (12th, 13th, 14th gen), article 000092149: https://www.intel.com/content/www/us/en/support/articles/000092149/processors.html
3. Intel ARK Z890 chipset and Core Ultra 7 265: https://www.intel.com/content/www/us/en/products/sku/237777/intel-z890-chipset/specifications.html ; https://www.intel.com/content/www/us/en/products/sku/241068/intel-core-ultra-7-processor-265-30m-cache-up-to-5-30-ghz/specifications.html
4. Intel Core Ultra 200S Plus quick reference guide (PDF): https://cdrdv2-public.intel.com/874112/intel-core-ultra-200s-plus-series-processors-quick-reference-guide-ph2-public.pdf
5. HWCooling, Arrow Lake Refresh launched: https://www.hwcooling.net/en/arrow-lake-refresh-intel-desktop-cpus-launched-models-and-pricing/
6. Windows Central / heise coverage of 200S Plus (via search summary): https://www.windowscentral.com/hardware/intel/announces-new-core-ultra-200s-plus-series-desktop-processors ; https://www.heise.de/en/news/Core-Ultra-200S-Plus-Intel-gives-mid-range-CPUs-more-cores-11207720.html
7. Tom's Hardware, Nova Lake launch schedule leak (headline only readable): https://www.tomshardware.com/pc-components/cpus/intels-core-ultra-400-nova-lake-launch-schedule-leaks-out-mass-production-in-q4-first-nova-lake-cpus-in-q1-2027
8. TechSpot (via search) and Wccftech on Nova Lake: https://www.techspot.com/news/111047-intel-confirms-nova-lake-core-ultra-400-cpus.html ; https://wccftech.com/intel-nova-lake-core-ultra-400-q1-2027-launch-lga-1954-razor-lake-hammer-lake-desktop-cpus/
9. AMD blog, Computex 2026 (blocked: timeout; search summary): https://amd.com/en/blogs/2026/amd-computex-2026-10-years-of-am4-am5-support-through.html
10. Tom's Hardware, AMD confirms AM5 support through 2029 (body truncated): https://tomshardware.com/pc-components/cpus/amd-confirms-am5-support-through-2029-zen-4-and-5-platform-will-likely-see-two-more-generations-at-least
11. Guru3D / HotHardware, Zen 6 Olympic Ridge and Medusa1 on AM5 (HotHardware 403; via search): https://www.guru3d.com/story/amd-confirms-zen-6-olympic-ridge-and-medusa1-processors-for-socket-am5/
12. AMD AM5 chipsets page (blocked: timeout; search summary): https://www.amd.com/en/products/processors/chipsets/am5.html
13. AMD AM4 chipsets page (blocked: timeout; search summary): https://www.amd.com/en/products/processors/chipsets/am4.html
14. Intel ARK Desktop Chipsets table: https://www.intel.com/content/www/us/en/ark/products/series/46645/desktop-chipsets.html
15. Intel ARK Z790 chipset: https://www.intel.com/content/www/us/en/products/sku/229721/intel-z790-chipset/specifications.html
16. Intel ARK B760 chipset (via search) and 700 series PCH datasheet: https://www.intel.com/content/www/us/en/products/sku/229719/intel-b760-chipset/specifications.html ; https://cdrdv2-public.intel.com/743835/743835-004.pdf
17. Intel ARK B860 chipset: https://www.intel.com/content/www/us/en/products/sku/241152/intel-b860-chipset/specifications.html
18. Intel ARK H810 chipset: https://www.intel.com/content/www/us/en/products/sku/241150/intel-h810-chipset/specifications.html
19. HWCooling, X870/X870E/B850/B840 (published 2024-08-28, updated 2024-09-05, pre-launch): https://hwcooling.net/en/x870-x870e-b850-and-b840-boards-for-amd-differences-and-release-dates
20. Corsair, B850 vs B840 (undated, table only): https://corsair.com/explorer/gamer/gaming-laptops/b850-vs-b840-which-chipset-should-you-choose
21. ASUS microsite X870E/X870/B850/B840 (BIOS FlashBack named): https://www.asus.com/microsite/motherboard/amd-am5-ryzen-9000-x3d-x870e-x870-b850-b840/
22. ASUS PRIME X870-P WIFI tech specs: https://www.asus.com/motherboards-components/motherboards/prime/prime-x870-p-wifi/techspec/
23. ASUS PRIME B650M-A WIFI II CPU support list: https://www.asus.com/motherboards-components/motherboards/prime/prime-b650m-a-wifi-ii/helpdesk_cpu/?model2Name=PRIME-B650M-A-WIFI-II
24. ASUS PRIME X870-P WIFI CPU support list: https://www.asus.com/motherboards-components/motherboards/prime/prime-x870-p-wifi/helpdesk_cpu/?model2Name=PRIME-X870-P-WIFI
25. ASUS PRIME B450M-A II CPU support list: https://www.asus.com/motherboards-components/motherboards/prime/prime-b450m-a-ii/helpdesk_cpu/?model2Name=PRIME-B450M-A-II
26. ASUS PRIME A520M-K CPU support list: https://www.asus.com/motherboards-components/motherboards/prime/prime-a520m-k/helpdesk_cpu/?model2Name=PRIME-A520M-K
27. HWCooling, Official Ryzen 5000 support for B350/X370 (2022-03-18; AMD announcement 2022-03-15): https://www.hwcooling.net/en/official-ryzen-5000-support-finally-coming-to-b350-x370-boards/
28. ComputerBase, AGESA ComboAM4v2PI 1.2.0.7 (2020-12-04, updated 2022-07-03): https://www.computerbase.de/2020-12/amd-ryzen-5000-zen-3-bios-updates-agesa-combo-b450-x470-a520-b550-x570/
29. PCWorld / TheFPSReview, 500-series Zen 3 BIOS (Oct 2020; search summary): https://www.pcworld.com/article/393623/how-to-make-sure-your-motherboard-is-ready-for-amd-ryzen-5000.html ; https://www.thefpsreview.com/2020/10/11/heres-a-big-list-of-amd-motherboards-that-already-support-ryzen-5000-zen-3-cpus-and-their-required-bioses
30. Intel, Required BIOS updates for 600 and 700 series with 13th/14th gen, article 000092294 (reviewed 2026-02-05): https://www.intel.com/content/www/us/en/support/articles/000092294/processors.html
31. Intel, 13th and 14th Gen Desktop Processor Vmin Shift Instability Issue, article 000102331 (reviewed 2026-07-21): https://www.intel.com/content/www/us/en/support/articles/000102331/processors.html
32. Intel Community, Vmin Shift update, microcode 0x12F (2025-05-01): https://community.intel.com/t5/Mobile-and-Desktop-Processors/Intel-Core-13th-and-14th-Gen-Vmin-Shift-Instabilty-Update-New/m-p/1686948
33. AMD FAQ cpu-99, BIOS updates for Ryzen desktop (blocked: timeout; search summary): https://www.amd.com/en/resources/support-articles/faqs/cpu-99.html
34. BIOS Flashback explainer and forum reports (via search): https://evezone.evetech.co.za/deep-dives/bios-flashback-explained-when-it-helps-on-an-am5-motherboard-and-why-it-matters
35. Wccftech, Gigabyte AGESA 1.2.0.0a for Ryzen 9000 on AM5 (mid-2024): https://wccftech.com/gigabyte-agesa-1-2-0-0a-bios-am5-motherboards-amd-ryzen-9000-cpus/
36. Intel ARK Core Ultra 7 270K Plus: https://www.intel.com/content/www/us/en/products/sku/245692/intel-core-ultra-7-processor-270k-plus-36m-cache-up-to-5-50-ghz/specifications.html
37. AMD Ryzen AI 7 450GE page (timeout; search summary) and Tom's Hardware on Ryzen AI 400 desktop: https://www.amd.com/en/products/processors/desktops/ryzen/ai-400-series/amd-ryzen-ai-7-450ge.html
39. Search results on Ryzen 7000 lane counts (TechPowerUp returned HTTP 403, not bypassed): https://techpowerup.com/295394/amd-zen-4-socket-am5-explained-pcie-lanes-chipsets-connectivity
40. Wccftech, ASUS and Gigabyte Ryzen 5000 support for X370/B350/A320; ASRock beta BIOS (search summary): https://wccftech.com/asus-gigabyte-roll-out-amd-ryzen-5000-ryzen-7-5800x3d-cpu-support-for-x370-b350-a320-motherboards/ ; https://wccftech.com/asrock-amd-ryzen-5000-cpu-bios-support-on-x370-b350-a320-motherboards/
41. Club386, Intel confirms Arrow Lake refresh and Nova Lake (2025-09-10, read 2026-11-14; Intel quote via Seeking Alpha, socket line is the writer's): https://www.club386.com/intel-confirms-arrow-lake-refresh-and-nova-lake-will-arrive-in-2026/
42. PC Games Hardware, LGA1851 and Nova Lake-S socket leak (2025-06-02, read 2026-11-14; Intel did not confirm): https://www.pcgameshardware.de/Arrow-Lake-S-Codename-280890/News/LGA1851-Desktop-CPU-Intel-Bestaetigung-1474085/
43. Pause Hardware, LGA1954 for Nova Lake-S from an Intel validation-tool listing (updated 2026-08-29, read 2026-11-14 via summary): https://pausehardware.com/lga1954-intel-nova-lake-s/
