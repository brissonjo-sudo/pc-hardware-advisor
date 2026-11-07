# Graph Report - E:\Claude code\Projects\pc-hardware-advisor  (2026-11-07)

## Corpus Check
- Large corpus: 135 files · ~812,968 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder, or use --no-semantic to run AST-only.

## Summary
- 661 nodes · 866 edges · 62 communities (44 shown, 18 thin omitted)
- Extraction: 80% EXTRACTED · 18% INFERRED · 2% AMBIGUOUS · INFERRED: 157 edges (avg confidence: 0.78)
- Token cost: 1,383,527 input · 0 output

## Community Hubs (Navigation)
- [[_COMMUNITY_Price Hunt Method|Price Hunt Method]]
- [[_COMMUNITY_APIs and Data Feeds|APIs and Data Feeds]]
- [[_COMMUNITY_Power Connectors and PSU|Power Connectors and PSU]]
- [[_COMMUNITY_Import Fees and Duties|Import Fees and Duties]]
- [[_COMMUNITY_Retailers France and Benelux|Retailers France and Benelux]]
- [[_COMMUNITY_Memory Rules per Platform|Memory Rules per Platform]]
- [[_COMMUNITY_China and Japan Stores|China and Japan Stores]]
- [[_COMMUNITY_AM5 Platform and Chipsets|AM5 Platform and Chipsets]]
- [[_COMMUNITY_Retailers Germany Spain Italy|Retailers Germany Spain Italy]]
- [[_COMMUNITY_International Buying Rules|International Buying Rules]]
- [[_COMMUNITY_GPU Inference and Scams|GPU Inference and Scams]]
- [[_COMMUNITY_Local AI Sizing|Local AI Sizing]]
- [[_COMMUNITY_Compatibility and Physical Fit|Compatibility and Physical Fit]]
- [[_COMMUNITY_Retailers UK US Canada Australia|Retailers UK US Canada Australia]]
- [[_COMMUNITY_Plugin Skills and Eval Suite|Plugin Skills and Eval Suite]]
- [[_COMMUNITY_Blocked Pages and AM4|Blocked Pages and AM4]]
- [[_COMMUNITY_Benelux Retail Reference|Benelux Retail Reference]]
- [[_COMMUNITY_Plugin Manifest|Plugin Manifest]]
- [[_COMMUNITY_France and Italy Retail Reference|France and Italy Retail Reference]]
- [[_COMMUNITY_Japan Retail and Proxies|Japan Retail and Proxies]]
- [[_COMMUNITY_Connectors and Tool Categories|Connectors and Tool Categories]]
- [[_COMMUNITY_Price Scout Agent|Price Scout Agent]]
- [[_COMMUNITY_Project Conventions|Project Conventions]]
- [[_COMMUNITY_Used Market Pricing|Used Market Pricing]]
- [[_COMMUNITY_Orchestration and Phases|Orchestration and Phases]]
- [[_COMMUNITY_Germany and Canada Retail|Germany and Canada Retail]]
- [[_COMMUNITY_US Marketplaces and APIs|US Marketplaces and APIs]]
- [[_COMMUNITY_License and Contributions|License and Contributions]]
- [[_COMMUNITY_Classifieds and Spain Retail|Classifieds and Spain Retail]]
- [[_COMMUNITY_Content Check Script|Content Check Script]]
- [[_COMMUNITY_Marketplace Manifest|Marketplace Manifest]]
- [[_COMMUNITY_EU Consumer Rights|EU Consumer Rights]]
- [[_COMMUNITY_No-Circumvention Rule|No-Circumvention Rule]]
- [[_COMMUNITY_Packaging and Delivery|Packaging and Delivery]]
- [[_COMMUNITY_China Brand Stores|China Brand Stores]]
- [[_COMMUNITY_UK Retail Reference|UK Retail Reference]]
- [[_COMMUNITY_Radeon Power Data|Radeon Power Data]]
- [[_COMMUNITY_Used Part Testing|Used Part Testing]]
- [[_COMMUNITY_GPU and RAM Test Limits|GPU and RAM Test Limits]]
- [[_COMMUNITY_AMD ROCm and Radeon AI|AMD ROCm and Radeon AI]]
- [[_COMMUNITY_Market Context 2026|Market Context 2026]]
- [[_COMMUNITY_Build Script|Build Script]]
- [[_COMMUNITY_Review Manipulation|Review Manipulation]]
- [[_COMMUNITY_Price Reduction Rules|Price Reduction Rules]]
- [[_COMMUNITY_Community 44|Community 44]]
- [[_COMMUNITY_Community 45|Community 45]]
- [[_COMMUNITY_Community 46|Community 46]]
- [[_COMMUNITY_Community 47|Community 47]]
- [[_COMMUNITY_Community 48|Community 48]]
- [[_COMMUNITY_Community 49|Community 49]]
- [[_COMMUNITY_Community 50|Community 50]]
- [[_COMMUNITY_Community 51|Community 51]]
- [[_COMMUNITY_Community 52|Community 52]]
- [[_COMMUNITY_Community 53|Community 53]]
- [[_COMMUNITY_Community 54|Community 54]]
- [[_COMMUNITY_Community 55|Community 55]]
- [[_COMMUNITY_Community 56|Community 56]]
- [[_COMMUNITY_Community 57|Community 57]]
- [[_COMMUNITY_Community 58|Community 58]]
- [[_COMMUNITY_Community 59|Community 59]]
- [[_COMMUNITY_Community 60|Community 60]]
- [[_COMMUNITY_Community 61|Community 61]]

## God Nodes (most connected - your core abstractions)
1. `R2 APIs and data feeds` - 36 edges
2. `R1 Retailers: France, Belgium, Netherlands, Luxembourg` - 30 edges
3. `R1 Retailers: China official stores and Japan` - 26 edges
4. `R1 Retailers: Germany, Spain, Italy` - 25 edges
5. `R2 International buying: taxes, duties, fees, warranty` - 21 edges
6. `R1 Retailers: UK, US, Canada, Australia` - 16 edges
7. `REPORT.md (v0.1.0 end-of-mission report)` - 11 edges
8. `Eval pass 1 (score 0.75)` - 11 edges
9. `France (retail and comparator sites)` - 10 edges
10. `Japan (domestic delivery seen on pages, overseas not verified)` - 10 edges

## Surprising Connections (you probably didn't know these)
- `Never circumvent a block (agent rule)` --semantically_similar_to--> `No-circumvention rule (connectors)`  [INFERRED] [semantically similar]
  E:/Claude code/Projects/pc-hardware-advisor/agents/price-scout.md → E:/Claude code/Projects/pc-hardware-advisor/CONNECTORS.md
- `v0.2 limitations and next steps` --conceptually_related_to--> `AM5 X870E 24 CPU PCIe 5.0 lanes (AMD total unverified)`  [INFERRED]
  E:/Claude code/Projects/pc-hardware-advisor/REPORT.md → E:/Claude code/Projects/pc-hardware-advisor/references/form-factors-cases.md
- `AM4 chipset and Ryzen 5000 support matrix (partial)` --conceptually_related_to--> `AMD AM5 platform (DDR5 only)`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/research/r4-platforms-amd-addendum.md → E:/Claude code/Projects/pc-hardware-advisor/research/r4-platforms-memory.md
- `Blocked sites never circumvented principle` --conceptually_related_to--> `No-circumvention rule (connectors)`  [INFERRED]
  E:/Claude code/Projects/pc-hardware-advisor/README.md → E:/Claude code/Projects/pc-hardware-advisor/CONNECTORS.md
- `Nothing that circumvents a site (contributions)` --semantically_similar_to--> `Blocked sites never circumvented principle`  [INFERRED] [semantically similar]
  E:/Claude code/Projects/pc-hardware-advisor/CONTRIBUTING.md → E:/Claude code/Projects/pc-hardware-advisor/README.md

## Hyperedges (group relationships)
- **Plugin skills and sub-agent** — readme_hunt_prices, readme_check_compatibility, readme_build_config, readme_size_local_ai, readme_review_used_listing, readme_track_price, readme_price_scout [EXTRACTED 1.00]
- **No-circumvention rule across plugin and contribution files** — readme_blocked_sites_principle, connectors_no_circumvention, agents_price_scout_no_circumvention, contributing_nothing_circumvents [EXTRACTED 1.00]
- **Decode speed estimation chain** — references_gpu_bandwidth_ai_bandwidth_table, references_gpu_bandwidth_ai_decode_estimation_method, references_gpu_bandwidth_ai_mbu_planning_factors, references_gpu_bandwidth_ai_efficiency_table [INFERRED 0.85]
- **RAM pair verdict chain** — references_memory_ram_pair_verdict_rules, references_memory_board_qvl_authority, references_memory_xmp_only_kit_am5_verdict, references_memory_capacity_limits, references_memory_ecc_am5 [INFERRED 0.75]
- **PSU verdict chain** — references_power_supplies_connectors_psu_sizing_method, references_power_supplies_connectors_psu_verdict_rules, references_power_supplies_connectors_atx30_vs_atx31, references_power_supplies_connectors_nvidia_psu_table, references_power_supplies_connectors_excursion_tolerance [INFERRED 0.75]
- **Landed price pipeline** — references_international_buying_landed_price_formula, references_international_buying_eu_flat_duty_eur3, references_international_buying_eu_handling_fee, references_international_buying_carrier_handling_fees, references_international_buying_card_fx_fee, references_international_buying_rate_lookup_sources [INFERRED 0.75]
- **AM5 chipset family** — references_sockets_chipsets_am5, references_sockets_chipsets_b650, references_sockets_chipsets_x870, references_sockets_chipsets_x870e, references_sockets_chipsets_b840, references_sockets_chipsets_b850 [EXTRACTED 1.00]
- **Intel 13th and 14th gen stability chain** — references_sockets_chipsets_lga1700, references_sockets_chipsets_intel_bios_update_600_700, references_sockets_chipsets_intel_vmin_shift [INFERRED 0.75]
- **UK and US price comparators** — research_r1_retailers_anglophone_pricespy_uk, research_r1_retailers_anglophone_pcpartpicker, research_r1_retailers_anglophone_staticice, research_r1_retailers_anglophone_google_shopping [INFERRED 0.75]
- **Chinese PC-component brand sites with no verified foreign store** — research_r1_retailers_asia_thermalright, research_r1_retailers_asia_lexar, research_r1_retailers_asia_asgard, research_r1_retailers_asia_montech, research_r1_retailers_asia_fanxiang [INFERRED 0.65]
- **Price comparators blocked or unverified in DE, ES, IT** — research_r1_retailers_europe_south_central_geizhals, research_r1_retailers_europe_south_central_idealo, research_r1_retailers_europe_south_central_billiger, research_r1_retailers_europe_south_central_trovaprezzi [INFERRED 0.75]
- **Belgian price comparators (candidates, not fetched)** — research_r1_retailers_europe_west_hardware_info, research_r1_retailers_europe_west_beslist_be, research_r1_retailers_europe_west_bstore_be [INFERRED 0.65]
- **Free official and reference exchange-rate sources** — research_r2_apis_feeds_ecb_reference_rates, research_r2_apis_feeds_frankfurter_api, research_r2_apis_feeds_open_er_api, research_r2_apis_feeds_exchangerate_host, research_r2_apis_feeds_bank_of_canada_valet, research_r2_apis_feeds_us_fed_h10, research_r2_apis_feeds_boe_iadb [INFERRED 0.85]
- **Official tariff and tax lookup sources** — research_r2_apis_feeds_uk_trade_tariff_api, research_r2_apis_feeds_eu_taric, research_r2_apis_feeds_eu_tedb_vat, research_r2_apis_feeds_us_hts_usitc, research_r2_apis_feeds_canada_cbsa_tariff [INFERRED 0.85]
- **US tariff and de minimis changes 2025-2026** — research_r2_international_buying_us_de_minimis_suspension, research_r2_international_buying_us_ieepa_ruling, research_r2_international_buying_us_section_301_exclusions [INFERRED 0.85]
- **Low-value import regimes by destination** — research_r2_international_buying_eu_low_value_regime, research_r2_international_buying_uk_low_value_regime, research_r2_international_buying_canada_cad20_rule, research_r2_international_buying_australia_gst_low_value, research_r2_international_buying_japan_jpy10000_rule [INFERRED 0.75]
- **Local LLM sizing inputs (bandwidth, memory capacity, KV cache, quantisation)** — research_r4_gpu_ai_decode_bandwidth_rule, research_r4_gpu_ai_kv_cache_formula, research_r4_gpu_ai_quant_sizing_table [EXTRACTED 1.00]
- **Fake-shop and fake-hardware red flags** — research_r3_retailer_criteria_bank_transfer_only, research_r3_retailer_criteria_fake_reviews, research_r3_retailer_criteria_relabelled_gpu [INFERRED 0.75]
- **12V-2x6 power connector family** — research_r4_power_form_factors_12vhpwr, research_r4_power_form_factors_12v_2x6, research_r4_power_form_factors_atx_3_1, research_r4_power_form_factors_sense_pins, research_r4_power_form_factors_excursion_limits [INFERRED 0.75]
- **Compatibility check flow** — skills_check_compatibility_skill_check_compatibility, skills_check_compatibility_skill_verdict_rules, skills_check_compatibility_skill_bios_guidance, skills_check_compatibility_references_pair_checklist_pair_matrix [INFERRED 0.75]
- **hunt-prices method cluster** — skills_hunt_prices_skill_overview, skills_hunt_prices_references_search_playbook_overview, skills_hunt_prices_skill_seller_typing, skills_hunt_prices_references_search_playbook_stopping_rule, skills_hunt_prices_skill_landed_price, skills_hunt_prices_skill_blocked_sources [INFERRED 0.85]
- **Eval passes 1 to 7 (iterative correction cycle)** — tests_results_run1_overview, tests_results_run2_overview, tests_results_run3_4_overview, tests_results_run5_overview, tests_results_run6_7_overview [INFERRED 0.85]
- **Memory and speed formula cluster** — skills_size_local_ai_skill_memory_formula, skills_size_local_ai_skill_decode_speed_estimate, skills_size_local_ai_references_sizing_worksheet_example_a_32b_q4, skills_size_local_ai_references_sizing_worksheet_example_b_70b [INFERRED 0.85]

## Communities (62 total, 18 thin omitted)

### Community 0 - "Price Hunt Method"
Cohesion: 0.1
Nodes (43): Comparator listings are discovery only, Search playbook, price-scout brief template, Stopping rule for price search, Never circumvent blocked sources, Landed price computation, hunt-prices skill, Canonical seller typing (+35 more)

### Community 1 - "APIs and Data Feeds"
Cohesion: 0.08
Nodes (37): R2 APIs and data feeds, AliExpress affiliate API, Amazon Creators API (PA-API successor), Amazon PA-API 5.0 (deprecated, returns 403), AMD spec pages (no API found), Bank of Canada Valet API, Best Buy Developer API, Bank of England IADB (not official reference rates) (+29 more)

### Community 2 - "Power Connectors and PSU"
Cohesion: 0.07
Nodes (35): 12V-2x6 connector (PCIe CEM 5.1), 12VHPWR connector, Intel Arc B580, ATX 3.1 PSU standard, ATX motherboard form factor, Cable bend space for 12V-2x6, Intel Core i9-14900K, Intel Core Ultra 9 285K (+27 more)

### Community 3 - "Import Fees and Duties"
Cohesion: 0.07
Nodes (33): AliExpress Choice and IOSS source conflict, Canada CAD 20 postal exemption and CLVS, Card FX fee (assumption, no official level), Carrier and postal handling fees, EU EUR 3 flat duty per item category, EU general import rules (non-EU seller), EU Union handling fee EUR 2 per item, EU 2-year legal guarantee (Directive 2019/771) (+25 more)

### Community 4 - "Retailers France and Benelux"
Cohesion: 0.08
Nodes (31): R1 Retailers: France, Belgium, Netherlands, Luxembourg, 2dehands.be, Alternate (BE), Alternate (NL), Azerty.nl, Back Market (FR, BE, NL), Beslist.be, bol.com (retailer and marketplace) (+23 more)

### Community 5 - "Memory Rules per Platform"
Cohesion: 0.09
Nodes (29): AMD AM4 DDR4 only, AM5 four-DIMM speed (DDR5-3600), DDR5-6000 sweet spot on AM5 (2022 press, medium), AMD AM5 DDR5 UDIMM only, Board QVL decides real memory behaviour, Memory capacity limits per platform, CUDIMM on Intel 800 series, ECC support on AM5 (+21 more)

### Community 6 - "China and Japan Stores"
Cohesion: 0.11
Nodes (27): R1 Retailers: China official stores and Japan, AliExpress (platform), AliExpress Lian Li store, Amazon.co.jp, Asgard, ASUS China store, AliExpress Choice and IOSS VAT rule (sources conflict, unverified), Dospara (+19 more)

### Community 7 - "AM5 Platform and Chipsets"
Cohesion: 0.09
Nodes (26): AM5 (Ryzen 7000, 8000G, 9000; DDR5 only), AM5 BIOS validation: 600 series needs update for Ryzen 9000, 800 series validated from first BIOS, AMD statement: AM5 support through 2029 (medium confidence), AM5 with Zen 6 (existence stated by press, no launch date), ASUS PRIME B650M-A WIFI II (CPU list, high), ASUS PRIME X870-P WIFI (spec and CPU list, high), AMD B650 chipset (CPU OC yes, one 5.0 M.2 recalled), Intel B760 chipset (no CPU OC, lane count inconsistent) (+18 more)

### Community 8 - "Retailers Germany Spain Italy"
Cohesion: 0.11
Nodes (26): R1 Retailers: Germany, Spain, Italy, Alternate.de, Amazon DE, ES, IT (marketplace), Back Market (DE, ES, IT), Billiger.de, Caseking.de, Computeruniverse.net, Coolmod.com (+18 more)

### Community 9 - "International Buying Rules"
Cohesion: 0.18
Nodes (22): R2 International buying: taxes, duties, fees, warranty, Australia: GST collected at checkout for goods up to AUD 1,000, Canada: mailed items up to CAD 20 exempt from duty and tax, Regulation (EU) 2019/518 card FX and DCC disclosure, DHL Express Germany duty processing fee (2% min EUR 12.50, low-medium confidence), EU intra-EU VAT: seller VAT under EUR 10,000 EU-wide distance sales, destination VAT above, Directive (EU) 2019/771: 2-year seller legal guarantee, EU low-value regime: EUR 150 exemption abolished 2026-07-01, EUR 3 flat duty per item, EUR 2 handling fee from 2026-11-01 (+14 more)

### Community 10 - "GPU Inference and Scams"
Cohesion: 0.09
Nodes (22): GPU-Z identification check, Relabelled older GPU scam, CUDA software stack and compute capability limits, Decode speed bounded by bandwidth x MBU / bytes per token, eGPU links (OCuLink, Thunderbolt, USB4) effect on decode, llama.cpp multi-GPU split modes (layer, tensor), Apple M5 Ultra (512 GB unified, about 1228 GB/s), RTX 3090 (24 GB, 936 GB/s, NVLink 2-way) (+14 more)

### Community 11 - "Local AI Sizing"
Cohesion: 0.14
Nodes (19): size-local-ai skill, 2x RTX 3090 Llama 3.3 70B measurement, 70B Q4_K_M at 32k worked example, Apple M5 Max and M5 Ultra status (2026), Memory bandwidth table (GPUs and APUs), Decode tok/s ceiling formula, Measured efficiency from llama.cpp tg128, eGPU decode overhead estimate (about 2-6 percent) (+11 more)

### Community 12 - "Compatibility and Physical Fit"
Cohesion: 0.15
Nodes (17): check-compatibility skill, 16-pin cable bend clearance (35 mm cable makers, 36 mm NVIDIA planning), Cooler height versus GPU thickness trade-off, references/form-factors-cases.md, Physical fit verdict rules, FormD T1 case limits (official page unreachable), Fractal Terra case limits, AM5 X870E 24 CPU PCIe 5.0 lanes (AMD total unverified) (+9 more)

### Community 13 - "Retailers UK US Canada Australia"
Cohesion: 0.17
Nodes (17): R1 Retailers: UK, US, Canada, Australia, Amazon Product Advertising API 5.0, Back Market (US), Best Buy, Blocked and rate-limited domains recorded as untested, not bypassed, camelcamelcamel, Canada Computers and Electronics, eBay (US and UK) (+9 more)

### Community 14 - "Plugin Skills and Eval Suite"
Cohesion: 0.16
Nodes (16): Seven-case eval suite, D17: track-price test uses session scheduler only, D20: prices corrector aligned with honesty rule, D9: plugin name kept despite homonym repo, build-config skill, PC Hardware Advisor plugin, review-used-listing skill, track-price skill (+8 more)

### Community 15 - "Blocked Pages and AM4"
Cohesion: 0.17
Nodes (16): Blocked page policy, AM4 (Ryzen 1000 to 5000, legacy), AM4 Ryzen 5000 selective beta BIOS on A320, B350, X370, amd.com blocked policy (try once, no mirrors, use board vendor pages), ASUS PRIME A520M-K (CPU list, high), ASUS PRIME B450M-A II (CPU list, high), Common brief for writers (canonical row, rules, shared references), Confidence scale: high, medium, low (+8 more)

### Community 16 - "Benelux Retail Reference"
Cohesion: 0.16
Nodes (15): Alternate (BE), Alternate (NL), Back Market (refurbisher marketplace, same platform in FR, BE, NL, IT, US, DE, ES), Belgium (retail and comparator sites), bol.com (marketplace, mixed sellers), Bstore.be (comparator), Coolblue (BE and NL; selective partner programme), Cross-border shipping is not inferred (+7 more)

### Community 17 - "Plugin Manifest"
Cohesion: 0.15
Nodes (12): author, name, url, description, displayName, homepage, keywords, license (+4 more)

### Community 18 - "France and Italy Retail Reference"
Cohesion: 0.17
Nodes (13): Price comparators are pointers, not prices, Cybertek (own stock shown), Drako.it (authorised reseller, readable), ePrice.it (direct retailer, readable), France (retail and comparator sites), GrosBill (own stock shown), idealo (comparator, blocked on fetch), Italy (retail and comparator sites) (+5 more)

### Community 19 - "Japan Retail and Proxies"
Cohesion: 0.21
Nodes (12): Buyee (proxy-buying, fee conflicts), Dospara (direct, domestic only per page), Janpara (refurbisher, grades A to D), Japan (domestic delivery seen on pages, overseas not verified), Kakaku.com (comparator, readable), Mercari JP (private party, proxies used by buyers abroad), OneMall (proxy-buying, 3% claim), PC工房 (Pc-koubou, direct, 1-year warranty) (+4 more)

### Community 20 - "Connectors and Tool Categories"
Cohesion: 0.2
Nodes (10): Dated data rule, Optional data sources needing user key or approval, Read-only rule (connectors), Tilde category placeholders (~~category), D11: tools cited by ~~ category, Tool categories used by skills, README.md (PC Hardware Advisor overview), Documented limits (perishable prices, volatile tax rules) (+2 more)

### Community 21 - "Price Scout Agent"
Cohesion: 0.25
Nodes (11): agents/price-scout.md, 14-column price row output table, price-scout agent definition (Haiku, read-only page reader), Seller type taxonomy, Page text treated as data, not instructions, D15: mechanical check script instead of Haiku agent, Phases 2-4 skills and agent (two waves), hunt-prices skill (+3 more)

### Community 22 - "Project Conventions"
Cohesion: 0.22
Nodes (9): External memory vault location, CLAUDE.md (project instructions), French for pilot files, English for package, no em dash, No personal data in package rule, Test command (claude plugin eval), Validate command (claude plugin validate), No personal data rule (contributions), Validate and test commands before PR (+1 more)

### Community 23 - "Used Market Pricing"
Cohesion: 0.22
Nodes (10): Fair used price method (sold prices, dated, per region), Listing red flags, Memory cost surge 2025-2026 (TrendForce forecast), Negotiation levers, RTX 3090 DE/EU used price (800-950 EUR, dated 2026-03-14, stale), RTX 3090 US used price snapshot (avg 1,596 USD, basis unclear), Ryzen 7 5800X3D used price (US 359.99 Amazon, UK 249 to 279 GBP), 10-sold-items sample rule (unsourced inference) (+2 more)

### Community 24 - "Orchestration and Phases"
Cohesion: 0.31
Nodes (8): D6: Sonnet for technical research and tax rules, Model routing per phase (Opus, Sonnet, Haiku), Phase 1 shared references (three disjoint lots), Phase 6 tests (claude plugin eval), Phase R research (10 parallel sub-agents), WebFetch rate limit caused by parallelism, Ten shared references, Token and cost accounting by phase

### Community 25 - "Germany and Canada Retail"
Cohesion: 0.22
Nodes (9): Alternate.de (readable, partial), Amazon (marketplace, mixed sellers, per country), Amazon PA-API deprecated, Creators API gated, Canada (retail sites), Canada Computers & Electronics (direct, readable), Geizhals.de (comparator, HTTP 403), Germany (retail and comparator sites), Kleinanzeigen.de (classifieds, readable) (+1 more)

### Community 26 - "US Marketplaces and APIs"
Cohesion: 0.25
Nodes (9): AliExpress (marketplace, affiliate API gated, empty page bodies), Best Buy (Products API: 50,000 calls/day, cache max 72 h, no pricing analysis by third parties), eBay US (marketplace, HTTP 403), Marketplace listings typed per seller, Micro Center (HTTP 403), Newegg (marketplace, HTTP 403), Rue du Commerce (direct plus marketplace), United States (retail and marketplace sites) (+1 more)

### Community 27 - "License and Contributions"
Cohesion: 0.32
Nodes (6): Release v0.1.0 (2026-11-07), Never write open source or MIT rule, Required PR acceptance sentence, Contribution terms and rights assignment, Conventional Commits convention, PolyForm Noncommercial License 1.0.0

### Community 28 - "Classifieds and Spain Retail"
Cohesion: 0.25
Nodes (8): Classifieds used for used-market review only, LDLC (direct retailer plus marketplace; Spanish storefront), Leboncoin (components classifieds), PcComponentes (ES, IT; refurbished tiers), Spain (retail and comparator sites), Subito.it (classifieds, rate limited), 2dehands.be (classifieds, scrapers not to be used), Wallapop (classifieds, login unclear)

### Community 29 - "Content Check Script"
Cohesion: 0.43
Nodes (7): check_license_mentions(), check_paths(), check_reference(), check_skill(), fail(), frontmatter(), Mechanical checks of plugin content (validation gate items that a script can ver

### Community 30 - "Marketplace Manifest"
Cohesion: 0.29
Nodes (6): description, name, owner, name, url, plugins

### Community 31 - "EU Consumer Rights"
Cohesion: 0.29
Nodes (7): Directive 2011/83/EU (consumer rights), DSA Art. 30 trader traceability, Seller identification on shop pages, Shipping cost and delivery time visible before checkout, Total price incl. VAT before checkout, Trusted Shops Buyer Protection, 14-day withdrawal right

### Community 32 - "No-Circumvention Rule"
Cohesion: 0.4
Nodes (6): Never circumvent a block (agent rule), No-circumvention rule (connectors), Nothing that circumvents a site (contributions), D16: amd.com unreadable, AMD data from board makers, confidence lowered, Blocked sites never circumvented principle, Reliable and discarded sources

### Community 33 - "Packaging and Delivery"
Cohesion: 0.33
Nodes (6): Build command (scripts/build_plugin.py), D18: marketplace.json added so repo serves as marketplace, D19: repo set private, push allowed at end of mission, D2: no GitHub push while repo public (superseded by D19), Phase 7 packaging and delivery, Installation paths (marketplace, plugin-dir, .plugin file)

### Community 34 - "China Brand Stores"
Cohesion: 0.33
Nodes (6): Asgard (brand site, no e-commerce link), China official brand stores (for buyers abroad), JD Worldwide (cross-border marketplace, shipping countries unconfirmed), Lexar (brand site, FR locale), Montech (official shop is Swiss, montech.com/ch), Thermalright (brand site, 5-year warranty on some models)

### Community 35 - "UK Retail Reference"
Cohesion: 0.33
Nodes (6): eBay Browse API (gated production access), eBay UK (marketplace, private and pro sellers), Overclockers UK (direct retailer, readable), PCPartPicker (robots.txt disallows Claude user agents, do not fetch), Scan Computers (affiliate via Awin, HTTP 403), United Kingdom (retail and comparator sites)

### Community 36 - "Radeon Power Data"
Cohesion: 0.33
Nodes (6): AMD reference TBP and recommended PSU gap, AMD Radeon AI PRO R9700, AMD Radeon RX 7900 XTX, AMD Radeon RX 9070, AMD Radeon RX 9070 XT, Sapphire PULSE RX 9070 XT

### Community 37 - "Used Part Testing"
Cohesion: 0.4
Nodes (5): Used GPU test checklist, Used listing red flags, memtest_vulkan VRAM test, Used PSU risk, MemTest86 and TestMem5 RAM tests

### Community 38 - "GPU and RAM Test Limits"
Cohesion: 0.5
Nodes (4): GPU temperature throttle limits (AMD RDNA4 110 C edge/hotspot, memory 108 or 105 C), GPU test checklist, memtest_vulkan (VRAM test, at least 6 minutes), RAM test procedure (one stick at a time, any error fails)

### Community 39 - "AMD ROCm and Radeon AI"
Cohesion: 0.5
Nodes (4): AMD Instinct MI50 32 GB (ROCm unsupported), ROCm software stack and Radeon support, RX 7900 XTX (24 GB, 960 GB/s), RX 9070 XT (16 GB, 640 GB/s)

### Community 40 - "Market Context 2026"
Cohesion: 0.5
Nodes (4): DRAM and NAND price surge 2026, RTX 3090 used price, Section 301 tariff on Chinese electronics (10 Nov 2026), Sold versus asking price basis

### Community 41 - "Build Script"
Cohesion: 0.67
Nodes (3): build(), included(), Build dist/pc-hardware-advisor.plugin (a zip of the plugin) without dev-only fil

### Community 42 - "Review Manipulation"
Cohesion: 0.67
Nodes (3): Fake or purchased reviews, US FTC Consumer Review Rule (16 CFR 465), Trustpilot as reputation source

### Community 43 - "Price Reduction Rules"
Cohesion: 0.67
Nodes (3): CJEU C-330/23 Aldi Sud ruling (price reduction), Directive (EU) 2019/2161 (Omnibus, price reductions and marketplaces), 30-day lowest price rule for price reductions

## Ambiguous Edges - Review These
- `LGA1851 (Core Ultra 200S and 200S Plus, 800 series)` → `LGA1954 Nova Lake (leak only, not released)`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/references/sockets-chipsets.md · relation: conceptually_related_to
- `AMD B840 chipset (GPU slot generation in conflict)` → `B840 and B850 GPU slot generation conflict (Corsair vs HWCooling vs ASUS)`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/references/sockets-chipsets.md · relation: references
- `AMD B850 chipset (GPU slot generation in conflict)` → `B840 and B850 GPU slot generation conflict (Corsair vs HWCooling vs ASUS)`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/references/sockets-chipsets.md · relation: references
- `AliExpress (platform)` → `Peerless Assassin (Thermalright line)`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/research/r1-retailers-asia.md · relation: references
- `AliExpress (platform)` → `Kingbank`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/research/r1-retailers-asia.md · relation: references
- `Rakuten Ichiba Item Search` → `Plugin connector recommendation by category`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/research/r2-apis-feeds.md · relation: conceptually_related_to
- `US Section 301 exclusions on 8473.30 lines, deadline 2026-11-09 (status unconfirmed)` → `US HTS general rate Free for PC parts lines (8471.80, 8473.30, 8528.52, 8523.51)`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/research/r2-international-buying.md · relation: conceptually_related_to
- `Regulation (EU) 2019/518 card FX and DCC disclosure` → `Worked example (illustrative): USD 300 GPU, US to France, approx EUR 387.92 landed`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/research/r2-international-buying.md · relation: references
- `Regulation (EU) 2019/518 card FX and DCC disclosure` → `Worked example (illustrative): USD 60 cooler, China to UK, approx GBP 64.87 landed`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/research/r2-international-buying.md · relation: references
- `14-day withdrawal right` → `Trusted Shops Buyer Protection`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/research/r3-retailer-criteria.md · relation: conceptually_related_to
- `Relabelled older GPU scam` → `RTX 3090 (24 GB, 936 GB/s, NVLink 2-way)`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/research/r3-retailer-criteria.md · relation: conceptually_related_to
- `Decode speed bounded by bandwidth x MBU / bytes per token` → `DDR5-6000 sweet spot for Ryzen (press-relayed, not AMD primary)`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/research/r4-platforms-memory.md · relation: conceptually_related_to
- `AM4 chipset and Ryzen 5000 support matrix (partial)` → `AMD AM5 platform (DDR5 only)`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/research/r4-platforms-amd-addendum.md · relation: conceptually_related_to
- `PSU sizing from GPU and CPU power` → `PSU margin rule of thumb (not verified)`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/research/r4-power-form-factors.md · relation: rationale_for
- `PCIe and M.2 lane sharing` → `ATX motherboard form factor`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/research/r4-power-form-factors.md · relation: conceptually_related_to
- `AMD Radeon AI PRO R9700` → `AMD reference TBP and recommended PSU gap`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/research/r4-radeon-addendum.md · relation: references
- `hunt-prices skill` → `prices corrector (grading criterion)`  [AMBIGUOUS]
  E:/Claude code/Projects/pc-hardware-advisor/tests/results/run1.md · relation: conceptually_related_to

## Knowledge Gaps
- **210 isolated node(s):** `name`, `description`, `name`, `url`, `plugins` (+205 more)
  These have ≤1 connection - possible missing edges or undocumented components.
- **18 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **What is the exact relationship between `LGA1851 (Core Ultra 200S and 200S Plus, 800 series)` and `LGA1954 Nova Lake (leak only, not released)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `AMD B840 chipset (GPU slot generation in conflict)` and `B840 and B850 GPU slot generation conflict (Corsair vs HWCooling vs ASUS)`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `AMD B850 chipset (GPU slot generation in conflict)` and `B840 and B850 GPU slot generation conflict (Corsair vs HWCooling vs ASUS)`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `AliExpress (platform)` and `Peerless Assassin (Thermalright line)`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `AliExpress (platform)` and `Kingbank`?**
  _Edge tagged AMBIGUOUS (relation: references) - confidence is low._
- **What is the exact relationship between `Rakuten Ichiba Item Search` and `Plugin connector recommendation by category`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._
- **What is the exact relationship between `US Section 301 exclusions on 8473.30 lines, deadline 2026-11-09 (status unconfirmed)` and `US HTS general rate Free for PC parts lines (8471.80, 8473.30, 8528.52, 8523.51)`?**
  _Edge tagged AMBIGUOUS (relation: conceptually_related_to) - confidence is low._