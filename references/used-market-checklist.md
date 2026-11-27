# Used-market checklist

Last checked: 2026-11-07 (resale method: 2026-11-26). Values change: verify online before concluding.

Use this file to price and vet used parts. All figures below are a dated snapshot from research on 2026-11-07: re-check before quoting. Never quote a range older than about 60 days as current; re-read the source or flag it as stale.

## 1. Market context 2025-2026 (dated 2026-11-07)

- Memory cost surge (fact, fetched): TrendForce (2 Feb 2026) raised its 1Q26 forecast for conventional DRAM contract prices to +90-95% QoQ, NAND to +55-60% QoQ, PC DRAM to more than +100% QoQ. DDR4 and DDR5 are not split. [17] High.
- Later forecast (snippet): Q2 2026 DRAM contract +58-63% QoQ, NAND +70-75% QoQ. [19] Low.
- NAND wafer costs up about 25% in Feb 2026 (snippet). [18] Low.
- Europe (snippet, conflicting): retail DDR5 slowly dropping in Europe; a tracker reported US prices dipping about 20% then reversing through summer. Direction not settled. [23][22] Low.
- Used knock-on (snippet): used AM4 CPUs and DDR4 demand rose; used Ryzen 7 5800X3D reported up to about 800 USD, above a new 9800X3D (undated mirror). [22] Low.
- GPU market (snippet): JPR via heise put quarterly graphics card sales just under 11.5 million units, down 4.5%, about 10% decline expected for 2026; Nvidia reportedly will not launch a new desktop generation until 2028. [21] Low (heise URL 404).
- Tariffs: exclusions from the 25% Section 301 duty on listed lines extended to 2027-01-09 (USTR notice 2026-11-06, read 2026-11-08); whether GPU and motherboard lines are in scope: unconfirmed. Low. Verify on USTR or the Federal Register.
- Trend: used high-end NVIDIA prices rose from spring to autumn 2026 (RTX 3090 about 700-850 USD in March to about 1,200-1,600 USD in autumn across trackers). Trend medium, levels low. Memory costs are the main driver (medium).

## 2. Estimating a fair used price

1. Use sold prices as the basis for "used price" (completed / sold filter of a classifieds or auction site). Asking prices run higher; one snippet says 20-40%, unverified, a rough guess only. Label any asking-based range "asking".
2. Trackers mix asking and sold. Record the tracker's own wording and the listing count it states. Do not call it sold data unless it says so.
3. Sample size (inference, not sourced): at least 10 sold items in the last 60 days before stating a range. Below 10, mark `low` and say so.
4. Outliers: drop the top and bottom 10% of sold prices and any listing with "for parts", "not working", "untested", bundles or whole systems. ResalePrices says it filters these; rules not documented in detail [1].
5. Period: headline range from the last 60 days only; show an older median as context.
6. Shipping: compare shipped with shipped. Record whether shipping is included (GPUDojo P40 figures include it [11]; Amazon figures may not).
7. Region: price EU and US separately. Never convert USD to EUR for a used range. Use local sold data (for example eBay.de sold, local classifieds closed listings where accessible).
8. Blocked sources: eBay US returned HTTP 403 to automated fetch. Record as `blocked`; never work around it; ask the user for a screenshot of sold results.
9. Date-stamp every row: region, currency, source URL, date, sample size, basis.
10. Re-check cadence: monthly, weekly for GPUs during fast moves (3080 and 3090 moved 10-25% in 30-90 days per trackers).

## 3. Price ranges: dated snapshot, verify before use

Basis column states what the source says. No row meets the 10-sold-items rule. Currency is as published.

| Item | Region | Range | Cur. | Basis | Src | Date | Conf. |
|---|---|---|---|---|---|---|---|
| RTX 3090 24GB | US | Avg 1,596; median 1,599; fair 1,542-1,656; observed 1,300-1,900 | USD | Tracker, 328 eBay US listings; basis unclear (says both asking and sold) | [1] | 2026-11-07 | medium |
| RTX 3090 24GB | US | Lowest-3 daily avg Sep 2026: 1,355 (day range 1,242-1,395); prior 3 months 1,158 | USD | Lowest-3 daily avg; sample and basis not stated | [2] | Sep 2026 | low |
| RTX 3090 24GB | DE/EU | 800-950 "currently trade" | EUR | Cited from eBay; no count; basis not stated; stale (over 60 days): never quoted as a price, not even as "my reference" | [3] | 2026-03-14 | low |
| RTX 3090 Ti 24GB | US | Avg 1,752; median 1,717; fair 1,642-1,793; observed 1,450-2,200 | USD | Tracker, 54 listings, mostly asking | [4] | 2026-11-07 | medium |
| RTX 4090 24GB | US | Avg 3,490; median 3,424; fair 3,247-3,602; observed 2,850-4,500 | USD | Tracker, 44 listings, mostly asking; 90-day low 2,500 | [5] | 2026-11-07 | medium |
| RTX 3080 10GB | US | Avg 438; median 430; fair 406-454; observed 325-585 | USD | Tracker, 171 listings; 10GB only | [6] | 2026-11-07 | medium |
| RTX 4070 (non-Super) | US | Avg 637; median 638; fair 609-667; observed 490-775 | USD | Tracker, 75 listings, mostly asking | [7] | 2026-11-07 | medium |
| RTX 4060 Ti 16GB | US | Avg 676; median 662; fair 642-683; observed 610-780 | USD | Tracker, 30 listings (small); 8GB not covered | [8] | 2026-11-07 | low |
| RX 7900 XTX | US | Avg 1,165; median 1,167; fair 1,081-1,253; observed 825-1,600 | USD | Tracker, 82 listings, labelled asking | [9] | 2026-11-07 | medium |
| RX 6800 XT | US | Avg 462; median 455; fair 430-480; observed 385-600 | USD | Tracker, 58 listings; basis unclear | [10] | 2026-11-07 | medium |
| Tesla P40 24GB | US | About 240-350 shipped; 349 incl. shipping on 9 Oct 2026; 239-292 in Apr 2026 | USD | eBay listings, mostly shipped; sold/asking unclear; affiliate-run site | [11] | Oct 2026 | low |
| Instinct MI50 32GB | US | Appraisal about 500-540 (12-month sales); live about 580-630 (Aug 2026) | USD | Appraisal claims sold basis, method not stated | [12] | Aug 2026 | low |
| Ryzen 7 5800X3D | US | Amazon 3rd-party used 359.99 (24 Jul 2026); eBay roughly 500-600 (mirror, undated) | USD | Amazon snapshot; eBay range unverified | [13][22] | Jul 2026 | low |
| Ryzen 7 5800X3D | UK | 249.20 low (16 Apr 2026); 279.00 (2 Jul 2026) | GBP | Price-history snapshot, 3rd-party | [13] | Jul 2026 | low |
| Ryzen 7 7800X3D | US | Used resale deal posts 265-280 (Jun 2026); new 299 (15 Jul 2026) | USD | Deal posts, not sales | [14] | Jun-Jul 2026 | low |
| Ryzen 7 7800X3D | UK | 3rd-party used 249.20 low; 279.00 (2 Jul 2026) | GBP | Price-history snapshot | [14] | Jul 2026 | low |
| DDR4 32GB kit (2x16) | US | Used: one sale 138.99 incl. shipping; new cheapest 191-198 | USD | One used sale, not a sample | [15] | Sep-Oct 2026 | low |
| DDR5 32GB kit (new) | US | Lowest tracked 479.99 (2 Nov 2026); median 554.99 over 22 listings; others 375-578 (Jul 2026) | USD | New retail, not used; tracker unnamed | [16] | Nov 2026 | low |

Gaps (no data found): RTX 4070 Super (US); RTX 4060 Ti 8GB; DDR5 32GB (EU); every EU row except RTX 3090 (3090 Ti, 4090, 4070, 6800 XT, 7900 XTX, P40, MI50, CPUs, DDR4/5).

Conflict note: the RTX 3090 US figure differs by date (about 1,343 USD in a Sep 2026 snippet of ResalePrices vs 1,596 USD on 7 Nov 2026). Do not blend; use the latest dated page.

## 4. Test checklists by part type

### GPU
- Identify the model with GPU-Z: name, device ID, BIOS version, memory size and type; compare with the listing and photos. Tool detail not verified in a primary source.
- Compare BIOS version with the vendor's release list; note an unknown BIOS.
- VRAM test: `memtest_vulkan` (official repo) [24]. Standard test 5 minutes; wait at least 6 minutes, stop with Ctrl+C. Rare errors may need 2-3 hours. Any error means hardware problems; the README says it is hard to tell VRAM chips from GPU or memory controller. Some AMD cards show low load; try toggling Resizable BAR.
- Stress test for crashes, artifacts, throttling (tool choice not verified).
- Temperatures (core, hotspot, memory junction under load):
  - AMD RDNA4 BIOS limits: 110 C edge and hotspot; 108 C (Hynix) or 105 C (Micron) memory. These are throttle limits, not sustained targets [25]. AMD said 110 C hotspot was within spec for RX 5700 series [26]. No AMD memory-junction spec published [25].
  - NVIDIA: no single limit found; read the model's own figure. GDDR6X limits of 95 C or 105 C come from one unverified forum post [25].
  - Rule of thumb (low-quality source): memory junction above about 100 C in gaming suggests degraded pads or paste [27].
- Fans: listen for click, grind, rattle; check smooth speed scaling. Dual-ball bearings outlast sleeve (general guides, low) [27].
- Physical: burned or discoloured PCB or backplate near VRM, bent fins, loose screws, burn marks or bent pins on PCIe connector, yellowed or compressed pads [27].
- Mining history: not automatically bad; check fans, pads, backplate, power connector. Ask if opened or repasted. Budget about 20-40 USD for paste and pads (one low-quality source) [27].
- Warranty transfer: get the brand policy in writing. Example: Corsair lifetime warranty does not transfer to secondhand buyers (Engadget, for RAM; GPU brands not checked) [15].

### CPU
- Inspect every pin (AM4/AM5) with light and magnifier; bent pins are a repeated complaint in deal threads (low) [14].
- Check socket and IHS for scratches, discoloration, heat marks.
- Load test 15-30 minutes, watch temperature and throttling (standard practice, no source fetched).
- Delid signs: lifted or re-glued IHS, uneven TIM residue, seal mark (inference, no source).

### RAM
- MemTest86 (paid/official) or Memtest86+ (free): separate products; boot from USB, not Windows [29].
- Test one stick at a time, at least 4 passes per stick (one guide says 8 overnight); any error = fail [29].
- TestMem5 on Windows for XMP/EXPO stability after a default-speed pass [29].
- Check XMP/EXPO profile and module markings (IC, PCB) against the claim.
- Used RAM is generally lower risk than a PSU; still test [30].

### Motherboard
- Confirm BIOS version; board boots and POSTs with the listed CPU and memory.
- Check socket for bent or missing pins and VRM heatsinks for looseness.
- Check SATA, PCIe slots, USB ports (inference, no source fetched).

### SSD
- CrystalDiskInfo: SMART health, power-on hours, total host writes vs rated TBW (tool details not verified).
- Fake capacity: h2testw (write and verify; overwrites the drive; hours) or ValiDrive (fast sampling). Run only on a drive you can overwrite [28].
- Price under 60% of the lowest legitimate retailer is suspect (one low-quality source; heuristic) [28].

### PSU
- No easy consumer test; a dedicated tester is needed [30].
- Age and history matter most; electrolytic capacitors age with heat regardless of hours [30].
- Most guides advise buying new PSUs; one forum view says roughly 3-year-old quality units can be good [30].
- Warranty is usually not transferable [30].

## 5. Listing red flags

- Generic or stock photos; GPU-Z screenshot not matching model or serial.
- Price far below the 60-day sold range.
- Refusal of an in-person test or a test on the seller's or buyer's PC.
- Deposit or payment off-platform; "friends and family" payment request.
- "For parts", "untested", "not working" or "as is" at full price.
- "Mining card, works fine" with no photos of fans, backplate, power connector.
- "Warranty" claimed without proof of purchase or a transfer policy.
- Bundles or systems that hide the GPU's true price.

## 6. Seller questions

1. Purchase date and proof of purchase? Original box and accessories?
2. Why selling? How long used, and for what workload (gaming, mining, rendering, AI)?
3. Ever opened, repasted, repadded, flashed or overclocked? Which BIOS?
4. Live test allowed (GPU-Z, memory test, benchmark) before payment, or a returns window?
5. Any warranty left, and is it transferable in writing?
6. Photos of serial, connectors, backplate, fans? Pet and smoke exposure?
7. Payment and shipping through the platform's protected method only?

## 7. Negotiation levers

- Cite dated sold prices (not asking) from section 2.
- Missing box, proof of purchase, or warranty transfer.
- Known issues: fan noise, thermal pad age, high hotspot, dust, cosmetic damage.
- Cost of repaste and pads (about 20-40 USD, low-quality source [27]).
- Shipping and fees included, buying several parts together, pickup and in-person test.
- Seller's listing age and number of watchers (stale listings favour the buyer; inference).

## 8. Resale estimate (selling your own parts)

Use this when the user wants to sell a part they own (often the one an upgrade replaces). The method is section 2, applied to the user's region; nothing here is a sourced price.

1. Basis: sold prices of the same model and variant (section 2), at least 10 sold in the last 60 days, outliers dropped, shipped compared with shipped, the user's region only. Never convert a US range into euros.
2. Access: eBay France and Germany and Leboncoin are tier B (`source-access-policy.md`, `retailers-by-country.md`): never read them automatically, nor through the browser, even on the user's yes (tier B: `source-access-policy.md`), and never offer to. Ask the user for a screenshot or pasted text of sold results (or of current listings, labelled "asking"). A value the user supplies is `medium` confidence at best (`research-method.md` section 4). Search-result snippets of these sites are not that data: undated and unread, they never give a range, a count or a net cost.
3. The dated ranges of section 3 are mostly US and some are stale: never quote them as a resale price in another region; give one only as context, with its date and region.
4. A new price is never a used value: GPUPrix figures and retailer prices are new-retail prices (`skills/find-deals/references/price-history-sources.md`). The cheapest new price of the same model and variant (same memory size and core count: an RX 580 2048SP is not an RX 580), read today, is only an upper bound a buyer would compare against (plugin heuristic: say so).
5. Factors to state without a percentage (no source): original box and invoice, remaining maker warranty and whether the maker lets it transfer (read the maker's warranty page), visible wear, mining or heavy use declared.
6. Answer: a range labelled "sold" or "asking", the count of items, the period, the region, the date read, the source, the confidence. Selling fees and shipping are deducted only when the user gives them or the platform's own fee page was read today. With no data, say so and ask for the screenshot rather than giving a figure.

## Not verified

- eBay sold listings: eBay US returned HTTP 403 to automated fetch; recorded as blocked, not bypassed; no sold data included.
- Kleinanzeigen, leboncoin, eBay.de sold not fetched. EU data is one German article (3090, March 2026, basis unclear).
- PCPartPicker price history and r/hardwareswap price-check threads not checked. ComputerBase used market not found.
- Tom's Hardware used-GPU article and tracker returned title only; not used for figures. heise GPU sales URL returned 404.
- Primary tool docs not fetched: GPU-Z, OCCT, CrystalDiskInfo, h2testw, MemTest86, TestMem5. Tool claims are general practice or snippets.
- No official AMD or NVIDIA spec sheet for temperature limits; figures are secondary (IgorsLab, TechPowerUp).
- Sample sizes are tracker listing counts, not sold counts; none meet the 10-sold rule.
- Motherboard BIOS/socket checks and PSU tier list: no source. Tariff status after 2027-01-09: not found (exclusions extended to that date by USTR notice 2026-11-06).
- Asking-vs-sold gap (20-40%) and 60-day / 10-sample rules are unsourced inference.
- Resale (section 8): no French sold-price source is readable automatically (eBay and Leboncoin are tier B); estimates rest on the user's screenshots. No source for the effect of box, invoice or warranty on a resale price.

## Sources

1. ResalePrices RTX 3090 (fetched 2026-11-07): https://resaleprices.com/gpu/nvidia-rtx-3090
2. GPUpoet RTX 3090 Sep 2026 (fetched): https://gpupoet.com/gpu/learn/price/september-2026/nvidia-geforce-rtx-3090
3. Borncity, RTX 3090 used market (14 Mar 2026): https://borncity.com/news/nvidia-rtx-3090-der-ungekroente-ki-koenig-des-gebrauchtmarkts/
4. ResalePrices RTX 3090 Ti: https://resaleprices.com/gpu/nvidia-rtx-3090-ti
5. ResalePrices RTX 4090: https://resaleprices.com/gpu/nvidia-rtx-4090
6. ResalePrices RTX 3080 10GB: https://resaleprices.com/gpu/nvidia-rtx-3080
7. ResalePrices RTX 4070: https://resaleprices.com/gpu/nvidia-rtx-4070
8. ResalePrices RTX 4060 Ti 16GB: https://resaleprices.com/gpu/nvidia-rtx-4060-ti-16gb
9. ResalePrices RX 7900 XTX: https://resaleprices.com/gpu/amd-rx-7900-xtx
10. ResalePrices RX 6800 XT: https://resaleprices.com/gpu/amd-rx-6800-xt
11. GPUDojo Tesla P40 (snippet): https://gpudojo.com/tesla-p40
12. AMCompute MI50 appraisal (snippet): https://www.amcompute.com/appraisals/instinct-mi50-32gb
13. camelcamelcamel 5800X3D (snippet): https://camelcamelcamel.com/product/B09VCJ2SHD ; UK: https://uk.camelcamelcamel.com/product/B0BTZB7F88
14. Slickdeals 7800X3D resale (snippet): https://slickdeals.net/f/19664712-amd-ryzen-7-7800x3d-amazon-resale-used-like-new-265-23
15. Engadget RAM 2020 vs 2026 (snippet): https://engadget.com/2300341/how-much-ram-cost-2020-vs-2026 ; DataCenterDisk DDR4: https://datacenterdisk.com/ram/ddr4/32gb
16. Digital Citizen DDR5 prices (snippet; tracker unnamed): https://www.digitalcitizen.life/ddr5-ram-prices-surge-in-2026-as-32gb-kits-reach-450-amid-global-memory-shortage/
17. TrendForce press release, 2 Feb 2026 (fetched): https://www.trendforce.com/presscenter/news/20260202-12911.html
18. Tom's Hardware NAND wafer costs (snippet): https://www.tomshardware.com/tech-industry/memory-spot-prices-climbed-again-in-february-nand-wafer-costs-surge-25-percent
19. TweakTown Q2 2026 forecast (snippet): https://www.tweaktown.com/news/110829/dram-prices-to-increase-by-up-to-63-percent-in-q2-nand-flash-by-up-to-75-percent-new-report-says/
20. Tom's Hardware Section 301 delay (snippet): https://www.tomshardware.com/pc-components/gpus/gpu-prices-are-threatening-to-climb-but-at-least-tariffs-wont-make-it-worse-25-percent-import-tax-on-chinese-made-electronics-suspended-once-again
21. heise, JPR GPU market (snippet): https://heise.de/-11200825
22. Tom's Hardware via mirror, 5800X3D used prices (undated): https://hn.jakechampion.name/reader/https://www.tomshardware.com/pc-components/cpus/amds-legacy-ryzen-7-5800x3d-chips-now-sell-for-up-to-usd800-more-than-a-new-9800x3d-am4-chip-costs-twice-as-much-as-msrp-as-enthusiasts-flock-to-old-ddr4-memory
23. Tom's Hardware, DDR5 prices Europe (snippet): https://www.tomshardware.com/pc-components/dram/retail-ddr5-memory-prices-slowly-drop-in-europe
24. memtest_vulkan official repo (fetched): https://github.com/GpuZelenograd/memtest_vulkan
25. IgorsLab RDNA4 memory temperatures (search snippet): https://www.igorslab.de/en/high-memory-temperatures-on-many-rdna4-cards-and-what-exactly-is-behind-it-cause-research-and-reasons/
26. TechPowerUp, RX 5700 hotspot (13 Aug 2019): https://www.techpowerup.com/258228/110-c-hotspot-temps-expected-and-within-spec-amd-on-rx-5700-series-thermals
27. Gearverify used GPU checklist 2026 (low-quality SEO source): https://gearverify.pages.dev/guides/used-gpu-checklist-2026.html
28. Industrial Monitor Direct, h2testw and ValiDrive (low quality): https://industrialmonitordirect.com/blogs/knowledgebase/detecting-counterfeit-ssd-capacity-with-h2testw-and-validrive
29. Corsair, how to test RAM: https://www.corsair.com/zh/en/explorer/diy-builder/memory/how-to-test-ram/
30. EveZone used vs new PSU: https://evezone.evetech.co.za/ez/used-vs-new-psu-south-africa-safety ; MaxMyBuild: https://www.maxmybuild.com/guides/choosing-parts/new-vs-used-pc-parts
