# R4 Addendum: AMD platforms (AM4, AM5)
Collected: 2026-11-07 · Model: sonnet

Scope: fills the AMD gaps of `r4-platforms-memory.md`. All source dates checked 2026-11-07. Confidence: high = vendor or amd.com page read this session; medium = reputable press or vendor page read for one board only; low = search summary, forum, recall. **amd.com blocked: timeout (2 tries each, 60 s) on: chipsets/am4.html, chipsets/am5.html, the Computex 2026 blog, Ryzen 9800X3D product page, EXPO page, partner article ryzen-9000-series-processors.html, FAQ cpu-99.** No cache, archive or mirror was used. Where amd.com was unreachable, vendor pages (ASUS) and press are used and marked.

## AM4 support matrix (table)

The AMD AM4 chipset page could not be read, so no AMD-published matrix is reproduced. Matrix below is built from AMD's announced policy (via press) and the ASUS per-board CPU lists. Per-board BIOS is the authority; chipset alone does not guarantee support.

| Chipset | Ryzen 1000/2000 | Ryzen 3000 | Ryzen 5000 (incl. 5000X3D) | BIOS / AGESA notes | Source | Conf. |
|---|---|---|---|---|---|---|
| A320 | Yes | Not official on A320 (mostly works) | Only "selective beta BIOS", board maker's choice; needs AGESA 1.2.0.7 | Earlier AGESA deliberately blocked Zen 3 on 300 series. AMD announcement 2022-03-15 | [1] [2] | medium |
| B350 / X370 | Yes | Yes (selective) | Same as A320: selective beta BIOS, AGESA 1.2.0.7 required, vendor by vendor. Press: 5800X3D needs AGESA 1.2.0.6B and "wait for explicit confirmation" | ASUS planned 300-series BIOS from 2022-03-25; ASRock beta BIOS on 16 boards | [1] [3] | medium |
| B450 / X470 | Yes | Yes | Yes (per vendor BIOS). ASUS PRIME B450M-A II: 5000 from BIOS 2409 (5600X/5800X/5900X/5950X listed), 5800X3D from BIOS 3211 | Launch-era (Oct-Dec 2020): AMD said 400-series beta BIOS due January 2021; MSI/ASUS prepared AGESA 1.2.0.0 for 400 and 500 | [4] [5] | high (one ASUS board), low (history) |
| A520 | Yes (board dependent) | Yes | Yes. ASUS PRIME A520M-K: 5600X/5800X/5900X/5950X from BIOS 1004; 5600/5700X from 2423; 5800X3D from 2423; 5700X3D and 5600X3D from 2803 | 500 series launched with Zen 3 support; AMD required AGESA 1.0.8.0+ to boot Zen 3, 1.1.0.0 recommended (launch press, Oct 2020) | [6] [7] | high (one ASUS board), medium (AGESA) |
| B550 / X570 | Yes | Yes | Yes (500 series); X3D needs a BIOS that lists it, check board | Same AGESA 1.0.8.0 boot minimum (press) | [7] [8] | medium |

Ryzen 3000 on ASUS A520M-K: desktop mostly BIOS 0403, 3100/3300X 0305; 3000G APUs mostly 2803. [6] (high, one board)

AGESA 1.2.0.7 per press: "all Zen 3 CPUs on all AM4 chipsets, A320 through X570" (ComputerBase 2020-12-04, page updated to 2022-07). [8] (medium). Gigabyte only had beta BIOS in that table at the 2022-07-03 update. [8]

BIOS flashback as a board feature (names, per board, not per chipset): ASUS "BIOS FlashBack" (named on ASUS page, 2026) [9] (high). MSI "Flash BIOS Button", Gigabyte "Q-Flash Plus", ASRock "BIOS Flashback" are carried over from the prior note [10] (medium, not re-read here). Not guaranteed on any chipset tier; check the board spec page. AMD's own guidance (flash with an older CPU or use USB BIOS Flashback if present) is only a search summary of FAQ cpu-99, amd.com blocked. [11] (low)

## AM5 chipset capabilities (table)

AMD chipset page blocked. Values are from ASUS (high for ASUS products, medium as chipset rule), HWCooling (pre-launch, 2024-08-28/09-05), and a Corsair comparison table that appears to mirror AMD's. Conflicts are shown.

| Chipset | CPU OC | Memory OC | GPU slot (CPU lanes) | M.2 (CPU lanes) | USB4 | Notes | Source | Conf. |
|---|---|---|---|---|---|---|---|---|
| A620 / A620A | No (per prior note and press) | Yes (EXPO) | PCIe 4.0 (unverified here) | PCIe 4.0 (unverified here) | not required | Entry level. Not re-verified this session | [12] | low |
| B650 | Yes | Yes | 5.0 optional (vendor choice) | one 5.0 M.2 required (recalled) | optional | Not re-verified this session | [12] | low |
| B650E / X670E | Yes | Yes | 5.0 mandatory | 5.0 mandatory | optional on 600 series (HWCooling: "USB4 was optional on 600-series boards") | X670/X670E use two chipset dies, B650/B650E one | [13] | medium |
| X670 | Yes | Yes | 5.0 optional | 5.0 M.2 | optional | two dies | [13] | low |
| B840 | No (Corsair table; HWCooling: reportedly not) | Yes (EXPO/XMP/manual) | **Conflict:** Corsair table PCIe 4.0 x16 or 2x8; HWCooling pre-launch "PCIe 3.0 x16 only"; ASUS microsite "B840 boards are limited to PCIe 4.0 slots and PCIe 4.0 and 3.0 M.2" | PCIe 4.0 x4 (Corsair); 3.0/4.0 (ASUS) | optional, needs extra chip; ASUS B840 boards listed have none | Corsair: 34 total chipset lanes, 0 PCIe 5.0; 2x USB 10G, 2x USB 5G, 4 SATA | [14] [13] [15] | medium |
| B850 | Yes (Corsair); ASUS: AI OC features only on some B850 models | Yes | **Conflict:** Corsair table says PCIe 4.0 x16/2x8; HWCooling pre-launch says PCIe 5.0 x16 optional (x8/x8 supported); ASUS says B850 boards have PCIe 5.0 M.2 and, in the X870 context, 5.0 x16 is stated only for X870/X870E | PCIe 5.0 x4 (Corsair, HWCooling, ASUS: 1 to 3 slots) | optional, extra chip required; "no longer mandatory" | Corsair: 36 chipset lanes/4 PCIe 5.0; 1x USB 20G, 6x 10G, 1x 5G, 4 SATA | [14] [13] [15] | medium |
| X870 | not stated by HWCooling; ASUS lists AI OC on most | Yes | PCIe 5.0 x16 | PCIe 5.0 (ASUS: two or more 5.0 M.2) | **Required** (HWCooling: "should always be present"); ASUS PRIME X870-P WIFI has two rear USB4 | One Promontory 21 die + USB4 controller | [13] [15] [16] | medium |
| X870E | same as X870 | Yes (boards expected to reach DDR5-8000, HWCooling) | PCIe 5.0 x16 (or x8/x8) | PCIe 5.0 x4 | **Required** | Two Promontory 21 dies + ASM4242 USB4 controller; more PCIe 4.0 lanes, SATA and USB than X870 | [13] [15] | medium |

Rule for the plugin: do not encode B850 GPU-slot generation or any 600-series GPU/M.2 rule as fact until AMD's chipset page is read. CPU-side limits dominate: the slot generation on the board also depends on the CPU (below).

CPU lane counts. ASUS PRIME X870-P WIFI spec page [16] (high, one board): Ryzen 9000 and 7000 give one PCIe 5.0 x16 slot (x16 mode); **Ryzen 8000 gives one PCIe 4.0 x16 slot running x8/x4 mode** (reduced lanes and PCIe 4.0); the X870 chipset adds three PCIe 4.0 slots. Search results also state Ryzen 7000 has 28 PCIe 5.0 lanes (24 usable, 4 to chipset) and 8700G has 20 PCIe 4.0 lanes. Those two claims come from press/search (low); the 28/24 figure was not confirmed on an AMD page. [17]

## AM5 CPU support and BIOS

AMD's own statement (chipset page, via the prior note's search summary): all AM5 600/800 boards work with all AM5 processors, a BIOS update may be needed. Not re-read. [12] (low).

Vendor "Validated since BIOS" columns (ASUS codes are vendor-specific; they say nothing about AGESA version):

| CPU family | 600-series (ASUS PRIME B650M-A WIFI II) [18] | 800-series (ASUS PRIME X870-P WIFI) [19] |
|---|---|---|
| Ryzen 7000 | 0602 for most; 7800X3D/7900X3D/7950X3D 1409; 7700X3D 3263; 7500X3D "ALL" | "all" for most; 7400 1063, 7500 1402, 7700X3D 1066 |
| Ryzen 8000G / 8000F | 1807 | 8000G: "all" |
| Ryzen 9000 | 2613 for most incl. 9600X, 9800X3D, 9950X3D; 3263 for e.g. 9500F and 9850X3D | "all" for 9600, 9600X, 9700X, 9900X, 9900X3D, 9950X, 9950X3D and **9800X3D**; 9500F, 9700F 1063; 9850X3D, 9950X3D2 and some PRO 1066 |

Conclusion (high for these two ASUS boards, medium as a rule): on 600-series boards a BIOS update is needed for Ryzen 9000, 8000G/F and some 7000X3D, so out-of-box boards may need flashback or an older CPU. On 800-series boards, 7000/8000G/most 9000 including 9800X3D are validated from the first BIOS, but newer SKUs (9850X3D, 9950X3D2, some PRO) need a later BIOS. Press (prior note): AGESA 1.1.7.0 first enabled Ryzen 9000 boot on some 600 boards, 1.2.0.0 broader (mid-2024). [20] (medium, old). No AGESA mapping per SKU was found on any primary page; **do not state AGESA minimums as rules**.

## AMD memory support (official)

amd.com product and EXPO pages blocked (timeout). Nothing here is read from an AMD spec table this session.

- ASUS X870 spec page [16] (high, vendor): four DDR5 DIMM slots, up to **256 GB** total; overclocked speeds 8000+ MT/s with Ryzen 7000/8000/9000; ECC and non-ECC UDIMM; profiles AMD EXPO and ASUS AEMP; "supported memory types, speeds and module counts vary by CPU and configuration".
- Rated speeds per DIMM configuration (carried from prior note, search-summary of AMD pages): Ryzen 7000 2 DIMMs (1R/2R) DDR5-5200, 4 DIMMs DDR5-3600; Ryzen 9000 2 DIMMs DDR5-5600, 4 DIMMs DDR5-3600; max capacity differs by SKU page (128 GB / 192 GB / 256 GB seen). [21] (low-medium, not confirmed).
- AMD EXPO page (via search listing, not opened): AMD's own March 2026 performance test used a Ryzen 7 9700X with 32 GB DDR5-6000 EXPO at CL28/30/36. Shows DDR5-6000 as AMD's reference test point, not a stated recommendation on UCLK:MEMCLK 1:1 or FCLK. [22] (low)
- DDR5-6000 / 1:1 / FCLK statement: **no AMD-published page found**. Remains press-relayed (2022 AMD staff Discord AMA, see prior note [38], [39]). Medium.
- 64 GB DIMMs and 256 GB BIOS version: not found. Gap.

## XMP kits on AM5

- **ASUS (high, official support FAQ 1042256, last updated 2026-09-10):** "AMD AM5 and newer" + EXPO kit: BIOS option "EXPO I"; "AMD AM5 and newer" + XMP kit: BIOS option **"DOCP"**; AMD before AM5 + XMP: DOCP (no EXPO). Steps: if the DRAM supports XMP, set Ai Overclock Tuner to DOCP. "Not all ASUS motherboards or RAM kits will support XMP Tweaked". Advice: use DRAMs in the QVL. [23]
- ASUS also lists **AEMP** (ASUS Enhanced Memory Profile) for kits without EXPO/XMP; positioned as an ASUS feature, not an AMD one. XMP is not named on the PRIME X870-P spec page, though FAQ [23] shows XMP kits via DOCP. [16] [24] (medium/high)
- **Gigabyte (medium, press of company release, PCGH 2022-09-17):** all AM5 boards support EXPO; company will "continue to offer XMP support" ("Zeitgleich wird das Unternehmen aber auch weiterhin einen XMP-Support anbieten"). [25]
- Names to verify: MSI option appears as "EXPO" under OC in a guide (low); "A-XMP" and "XMP Booster" not verified, do not use. Search results suggest Gigabyte shows a combined XMP/EXPO option. [26] (low)
- AMD statement on XMP-only kits: none found (amd.com blocked).
- Rule for the plugin: an XMP-only DDR5 kit generally can run on AM5 via the board's XMP-compatibility option (ASUS: DOCP), but speed is not guaranteed and the QVL decides.

## AM5 longevity statement

- AMD blog, "AMD Computex 2026: 10 Years of AM4, AM5 Support Through 2029 and Expanded RDNA 4 Gaming", English version dated **2026-05-31** (Chinese version 2026-06-01) per search summary. Wording as relayed: "With the launch of the Ryzen 7 7700X3D processor, we are extending support for the Socket AM5 platform through 2029." A second quote attributed to AMD: "Today, we are announcing continuous support through 2029 on Socket AM5." Previous commitment: "through 2027+" (press: Tom's Hardware, which stresses the new window is "2029", no plus). amd.com fetch blocked: timeout (2 tries). Tom's Hardware article body truncated on fetch. [27] (medium: quotes via search summary, not read on amd.com)
- Extension does not name CPUs; Zen 6 not confirmed by AMD in this statement (press). [27]

## Not verified / gaps

- amd.com unreachable (timeout): AM4 and AM5 chipset pages, Computex blog, product spec pages for 9800X3D and other CPUs, EXPO page, FAQ cpu-99, partner article. All AMD-primary items are still open.
- AM4 matrix has per-board ASUS data only (B450M-A II, A520M-K); X370/B350/A320 pages on ASUS returned no CPU list; MSI page returned HTTP 403 (not bypassed). No per-chipset official AMD matrix.
- AGESA minimums for Ryzen 9000/9800X3D on 600 series: not found on a primary page.
- AM5 chipset table: 600-series values, A620 and B650, and B650E GPU rules not re-read; B840/B850 GPU slot generation conflicts between Corsair, HWCooling and ASUS.
- CPU lane totals (28/24 on Ryzen 7000/9000; 8000G 20 lanes) not confirmed on an AMD page.
- AMD rated memory speed table per SKU and the DDR5-6000, FCLK, UCLK:MEMCLK 1:1 statement: not found from AMD. Max capacity 192/256 GB with 64 GB DIMMs and BIOS: not found.
- MSI, Gigabyte and ASRock option names for XMP kits on AM5, and MSI/Gigabyte/ASRock flashback feature names: not re-read.
- 2022 AMD announcement of Ryzen 5000 on 300-series was read only through HWCooling (2022-03-18).

## Sources (numbered)

All checked 2026-11-07.

1. HWCooling, Official Ryzen 5000 support finally coming to B350/X370 boards (2022-03-18; AMD announcement 2022-03-15) — https://www.hwcooling.net/en/official-ryzen-5000-support-finally-coming-to-b350-x370-boards/
2. HWCooling, 300 generation chipsets allowed Zen 3 upgrade (search listing) — https://www.hwcooling.net/en/?p=93306
3. Wccftech, ASUS and Gigabyte roll out Ryzen 5000/5800X3D support for X370/B350/A320; ASRock beta BIOS (search summary) — https://wccftech.com/asus-gigabyte-roll-out-amd-ryzen-5000-ryzen-7-5800x3d-cpu-support-for-x370-b350-a320-motherboards/ ; https://wccftech.com/asrock-amd-ryzen-5000-cpu-bios-support-on-x370-b350-a320-motherboards/
4. ASUS PRIME B450M-A II CPU support list — https://www.asus.com/motherboards-components/motherboards/prime/prime-b450m-a-ii/helpdesk_cpu/?model2Name=PRIME-B450M-A-II
5. PureP C / Tom's Hardware, 400-series Zen 3 BIOS history (search summary) — https://www.purepc.pl/msi-i-asus-szykuja-bios-z-agesa-1-2-0-0-dla-plyt-glownych-amd-z-serii-400-i-500-lepsza-kompatybilnosc-z-ryzenami-5000 ; https://www.tomshardware.com/news/ryzen5000-support-early-B450-biostar-asrock-gigabyte
6. ASUS PRIME A520M-K CPU support list — https://www.asus.com/motherboards-components/motherboards/prime/prime-a520m-k/helpdesk_cpu/?model2Name=PRIME-A520M-K
7. PCWorld / TheFPSReview, 500-series Zen 3 BIOS (AGESA 1.0.8.0 / 1.1.0.0, Oct 2020; search summary) — https://www.pcworld.com/article/393623/how-to-make-sure-your-motherboard-is-ready-for-amd-ryzen-5000.html ; https://www.thefpsreview.com/2020/10/11/heres-a-big-list-of-amd-motherboards-that-already-support-ryzen-5000-zen-3-cpus-and-their-required-bioses
8. ComputerBase, AGESA ComboAM4v2PI 1.2.0.7 (2020-12-04, updated to 2022-07-03) — https://www.computerbase.de/2020-12/amd-ryzen-5000-zen-3-bios-updates-agesa-combo-b450-x470-a520-b550-x570/
9. ASUS microsite X870E/X870/B850/B840 (BIOS FlashBack named; chipset notes) — https://www.asus.com/microsite/motherboard/amd-am5-ryzen-9000-x3d-x870e-x870-b850-b840/
10. Prior note r4-platforms-memory.md, source 31 (flashback names, medium) — https://evezone.evetech.co.za/deep-dives/bios-flashback-explained-when-it-helps-on-an-am5-motherboard-and-why-it-matters
11. AMD FAQ cpu-99 (blocked: timeout; search summary only) — https://www.amd.com/en/resources/support-articles/faqs/cpu-99.html
12. AMD AM5 chipsets page (blocked: timeout) — https://www.amd.com/en/products/processors/chipsets/am5.html ; AM4 page (blocked) https://www.amd.com/en/products/processors/chipsets/am4.html
13. HWCooling, X870/X870E/B850/B840 (published 2024-08-28, updated 2024-09-05; pre-launch) — https://hwcooling.net/en/x870-x870e-b850-and-b840-boards-for-amd-differences-and-release-dates
14. Corsair, B850 vs B840 (undated; table only; footer 2026) — https://corsair.com/explorer/gamer/gaming-laptops/b850-vs-b840-which-chipset-should-you-choose
15. Search listing EatYourBytes / PurePC B840 vs B850 (not opened) — https://www.eatyourbytes.com/chipset-comparison/amd_b840&amd_b850/ ; https://www.purepc.pl/gigabyte-amd-ryzen-b840-b850-chipset-overclocking-pcie-50
16. ASUS PRIME X870-P WIFI tech specs — https://www.asus.com/motherboards-components/motherboards/prime/prime-x870-p-wifi/techspec/
17. Search results on Ryzen 7000 lane counts (TechPowerUp 295394 returned HTTP 403, not bypassed) — https://techpowerup.com/295394/amd-zen-4-socket-am5-explained-pcie-lanes-chipsets-connectivity
18. ASUS PRIME B650M-A WIFI II CPU support list — https://www.asus.com/motherboards-components/motherboards/prime/prime-b650m-a-wifi-ii/helpdesk_cpu/?model2Name=PRIME-B650M-A-WIFI-II
19. ASUS PRIME X870-P WIFI CPU support list — https://www.asus.com/motherboards-components/motherboards/prime/prime-x870-p-wifi/helpdesk_cpu/?model2Name=PRIME-X870-P-WIFI
20. Wccftech, Gigabyte AGESA 1.2.0.0a for Ryzen 9000 on AM5 (mid-2024; via prior note) — https://wccftech.com/gigabyte-agesa-1-2-0-0a-bios-am5-motherboards-amd-ryzen-9000-cpus/
21. AMD Ryzen 7 7700X / 9950X pages (via prior note, search summary) — https://www.amd.com/en/products/processors/desktops/ryzen/9000-series/amd-ryzen-9-9950x.html
22. AMD EXPO page (blocked: timeout; search snippet only) — https://www.amd.com/en/products/processors/technologies/expo.html
23. ASUS support FAQ 1042256, XMP/EXPO/DOCP (last update 2026-09-10) — https://www.asus.com/support/faq/1042256/
24. ASUS Edge Up, XMP vs EXPO vs AEMP (search summary) — https://edgeup.asus.com/2026/xmp-vs-expo-vs-aemp-unlock-your-rams-potential-with-memory-profiles-and-more/
25. PC Games Hardware, Gigabyte EXPO support (2022-09-17) — https://www.pcgameshardware.de/Mainboard-Hardware-154107/News/Gigabyte-EXPO-Support-DDR5-1403588/
26. Guide listing BIOS option names per vendor (search summary) — https://rampricesusa.com/guides/xmp-expo-bios-guide
27. AMD blog Computex 2026 (blocked: timeout; search summary, English version dated 2026-05-31) — https://amd.com/en/blogs/2026/amd-computex-2026-10-years-of-am4-am5-support-through.html ; Tom's Hardware (body truncated) — https://tomshardware.com/pc-components/cpus/amd-confirms-am5-support-through-2029-zen-4-and-5-platform-will-likely-see-two-more-generations-at-least
