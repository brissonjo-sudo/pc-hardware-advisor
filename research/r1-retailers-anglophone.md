# R1 Retailers: UK, US, Canada, Australia
Collected: 2026-11-07 · Model: haiku · Method: WebFetch on homepages (403 and domain rate-limit recorded as blocked/untested, no retries or bypass); WebSearch for API, feed and affiliate facts (secondary, marked medium/low).

Legend: Type = direct retailer / marketplace / professional refurbisher / private classifieds / manufacturer store / price comparator. "Auto-readable" = result of WebFetch on this run. "Untested" = domain hit a tool-side rate limit, no page content seen.

## United Kingdom

| Name | URL | Type | Role | Auto-readable | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| PriceSpy UK | https://pricespy.co.uk/ | Price comparator | Comparator | Yes (homepage only; product pages not tested) | None mentioned on homepage (text truncated) | Names sellers (Amazon.co.uk, eBay, OnBuy, Very, ao.com). Marketplace listings mixed in ("Amazon Marketplace", eBay). Shows "from" price and "+N shops". No freshness stamp seen. Homepage shows consumer categories; PC-parts coverage not verified | medium | [4] |
| PCPartPicker UK | https://uk.pcpartpicker.com/ | Price comparator | Comparator | Blocked: HTTP 403 | No official API found (search only). Secondary source: founder's 2020 Reddit comment says an API would breach retailer agreements (old, unconfirmed today) | Retailer list, freshness and seller display not verified | low | [2], [28] |
| PCPartPicker (global) | https://pcpartpicker.com/ | Price comparator | Comparator | Blocked: HTTP 403 (also /api/ 403) | None official. Community scrapers and a third-party "API" (parse.bot) exist; not PCPartPicker-run; ToS risk noted by search | Do not build on unofficial scrapers without ToS review | low | [1], [3], [28], [29b] |
| Google Shopping | https://www.google.com/shopping | Aggregator | Comparator | Blocked: returned a browser-update notice, no shopping content | No feed found (not searched further) | Cannot confirm seller display or freshness | low | [6] |
| Scan Computers | https://www.scan.co.uk/ | Direct retailer (type from prior knowledge, not confirmed on page) | Direct retailer | Blocked: HTTP 403 | Affiliate programme via Awin (merchant 15473), base commission 1%. Product feed unconfirmed (listings conflict) | Need Awin dashboard or affiliates@scan.co.uk to confirm feed | medium (type), low (readability) | [9], [35] |
| Overclockers UK (OcUK) | https://www.overclockers.co.uk/ | Direct retailer | Direct retailer | Yes (homepage, first 100k of 224k chars) | No public API found. Affiliate via Awin (ID 28821); no feed seen in results | Navigation shows own categories (CPUs, GPUs, motherboards, RAM, PSUs, SSDs, cases); no marketplace structure visible | high (type), medium (feed) | [10], [36] |
| CCL Online | https://www.cclonline.com/ | Direct retailer (prior knowledge, not confirmed) | Direct retailer | Blocked: HTTP 403 | None found | Unverified | low | [11] |
| Ebuyer | https://www.ebuyer.com/ | Direct retailer (prior knowledge) | Direct retailer | Untested (rate-limited) | Unknown | Unverified | low | n/a |
| Amazon UK | https://www.amazon.co.uk/ | Marketplace (mixed 1P and 3P) | Marketplace | Untested (rate-limited) | Product Advertising API: sales-qualification rule applies (see cross-country) | Third-party sellers mixed in (prior knowledge, unverified in this run) | low | [33] |
| eBay UK | https://www.ebay.co.uk/ | Marketplace (mixed private and pro) | Private classifieds / marketplace | Untested (ebay.com returned 403) | Browse API (item_summary/search, application token) exists per official docs, see US row | Mixed private and pro sellers (prior knowledge) | medium (API), low (readability) | [30] |
| Gumtree UK | https://www.gumtree.com/ | Private classifieds | Private classifieds | Untested (rate-limited) | Unknown | Unverified | low | n/a |

## United States

| Name | URL | Type | Role | Auto-readable | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| Newegg | https://www.newegg.com/ | Marketplace (1P plus 3P sellers) | Marketplace / direct | Blocked: HTTP 403 | Seller-side feeds and API (Item Creation, Inventory, Order Shipping schemas; Elite Seller required). No buyer-facing product feed or affiliate feed found | Mixed marketplace, so seller must be checked per listing | medium | [12], [31] |
| Newegg Refreshed (refurb) | https://www.newegg.com/ (Newegg Refreshed program) | Professional refurbisher channel (Newegg + partners such as ABS, Likewize) | Refurbisher | Blocked (no page fetched); info from 2024 launch release | Unknown | Launch terms: 90-day refund or replacement guarantee. Terms dated 2024, must re-check | medium (existence), low (current terms) | [34] |
| Best Buy | https://www.bestbuy.com/ | Direct retailer (online and stores) | Direct retailer | Partial: country-selection landing only, no product content | Yes: Products API (REST, key from developer portal, JSON or XML; Categories, Recommendations, Buying Options, Commerce API invite-only). Documentation found by search, endpoints not verified live | PC-parts coverage and marketplace presence not verified on page | high (API existence), low (PC catalog) | [15], [29] |
| B&H Photo | https://www.bhphotovideo.com/ | Direct retailer | Direct retailer | Blocked: HTTP 403 | None found | Unverified | low | [13] |
| Micro Center | https://www.microcenter.com/ | Direct retailer (stores and online) | Direct retailer | Blocked: HTTP 403 | None found | Store-only inventory signals not verified | low | [14] |
| Amazon US | https://www.amazon.com/ | Marketplace (mixed) | Marketplace | Untested | Product Advertising API (sales-qualification rule, see cross-country) | Unverified | low | [33] |
| eBay US | https://www.ebay.com/ | Marketplace (mixed private and pro) | Private classifieds / marketplace | Blocked: HTTP 403 | Browse API: GET item_summary/search, one category ID per request, application token with api_scope. Official reference found by search | Confirmed API existence only from docs search, not from live site | medium (API), low (site) | [19], [30] |
| Back Market (US) | https://www.backmarket.com/en-us | Professional refurbisher marketplace (third-party refurbishers) | Refurbisher / marketplace | Untested (rate-limited) | None found | 12-month seller warranty per help center (search). Back Market Pro states it does not refurbish devices itself. PC-component coverage not verified | medium | [21], [37] |
| Dell Outlet | https://www.dell.com/en-us/shop/outlet | Manufacturer store (outlet) | Manufacturer outlet | Untested (rate-limited) | None found | Not verified | low | [22] |
| Reddit r/hardwareswap | https://www.reddit.com/r/hardwareswap/ | Private classifieds (forum) | Private classifieds | Untested (rate-limited) | Reddit API exists (not checked) | Not verified | low | [25] |
| Facebook Marketplace | https://www.facebook.com/marketplace/ | Private classifieds (mixed with businesses) | Private classifieds | Untested (rate-limited) | Not checked; likely unavailable to unauthenticated tools | Not verified | low | [26] |

## Canada

| Name | URL | Type | Role | Auto-readable | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| Canada Computers & Electronics | https://www.canadacomputers.com/ | Direct retailer (online and stores) | Direct retailer | Yes (homepage, first 100k of 164k chars) | None mentioned on homepage | Lists CPUs, motherboards, GPUs, laptops, monitors, networking. Member-only prices and PC Builder tool. No third-party marketplace mentioned | high (type), medium (readability) | [17] |
| Memory Express | https://www.memoryexpress.com/ | Direct retailer (Canada) | Direct retailer | Blocked: HTTP 403 | None found | Unverified | low | [16] |
| Newegg Canada | https://www.newegg.ca/ | Marketplace (mixed 1P and 3P) | Marketplace / direct | Untested | Seller API base URL for Newegg.ca exists in the Newegg developer schema (seller-side) | Unverified | low | [31] |
| Amazon.ca | https://www.amazon.ca/ | Marketplace (mixed) | Marketplace | Untested | PA-API: Canadian endpoint documentation exists (webservices.amazon.ca); sales-qualification applies | Unverified | low | [33] |
| Kijiji | https://www.kijiji.ca/ | Private classifieds (mixed with pro sellers) | Private classifieds | Untested (rate-limited) | Unknown | Unverified | low | [23] |

## Australia

| Name | URL | Type | Role | Auto-readable | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| StaticICE | https://www.staticice.com.au/ | Price comparator (computer hardware, cameras, electronics) | Comparator | Yes (homepage) | None mentioned on homepage | Tracks "199 Australian stores" but does not name them on the page. No freshness indicator seen. Sister sites for NZ, UK and US listed | medium | [5] |
| PC Case Gear | https://www.pccasegear.com/ | Direct retailer (prior knowledge) | Direct retailer | Blocked: HTTP 403 (after one rate-limited attempt) | None found | Unverified | low | [18] |
| Mwave | https://www.mwave.com.au/ | Direct retailer (prior knowledge) | Direct retailer | Untested (rate-limited) | Unknown | Unverified | low | n/a |
| Scorptec | https://www.scorptec.com.au/ | Direct retailer (prior knowledge) | Direct retailer | Untested (rate-limited) | Unknown | Unverified | low | n/a |
| Umart | https://www.umart.com.au/ | Direct retailer (prior knowledge) | Direct retailer | Untested (rate-limited) | Unknown | Unverified | low | n/a |
| Centre Com | https://www.centrecom.com.au/ | Direct retailer (prior knowledge) | Direct retailer | Untested (rate-limited) | Unknown | Unverified | low | n/a |
| Amazon AU | https://www.amazon.com.au/ | Marketplace (mixed) | Marketplace | Untested | PA-API sales rule applies (cross-country) | Unverified | low | [33] |
| Gumtree AU | https://www.gumtree.com.au/ | Private classifieds | Private classifieds | Untested | Unknown | Unverified | low | n/a |

## Cross-country (affects all four zones)

| Name | URL | Type | Role | Auto-readable | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| camelcamelcamel | https://camelcamelcamel.com/ | Amazon price tracker | Price history | Blocked: HTTP 403 | None found | Regions and API status unverified | low | [7] |
| Keepa | https://keepa.com/ | Amazon price-history service | Price history | Partial: returned title only | Paid API documented (keepa.com/api-docs). Token-bucket model per search: tokens regenerate per minute, unused tokens expire after 60 minutes. Token costs conflict across sources (one secondary source gives per-request figures that do not match the official model) | Regions covered not confirmed on page | medium (API existence), low (costs) | [8], [32] |
| Amazon Product Advertising API 5.0 | https://webservices.amazon.com/paapi5/documentation/register-for-pa-api.html | Official API (Amazon Associates) | Feed for Amazon listings | n/a (docs via search) | Access requires qualified referral sales. Threshold conflicts: 3 sales in 30 days (DEV Community) vs 10 (KeywordRush). Successor "Creators API" reported as replacing PA-API 5.0 (AffiliateX, secondary) | Do not assume access; check Associates Central | low | [33] |
| Google Shopping | (see UK) | Aggregator | Comparator | Blocked | None found | See UK row | low | [6] |

## Not verified / gaps

- **Blocked (HTTP 403, 12 domains):** pcpartpicker.com (and uk. subdomain, /api/), camelcamelcamel.com, scan.co.uk, cclonline.com, bhphotovideo.com, microcenter.com, newegg.com, memoryexpress.com, ebay.com, pccasegear.com.
- **Blocked (other):** google.com/shopping returned a browser-update notice, no content.
- **Untested (domain-level rate limit from the safety check, not a site block; not retried):** mwave.com.au, scorptec.com.au, umart.com.au, centrecom.com.au, amazon.co.uk, backmarket.com, dell.com, kijiji.ca, gumtree.com, reddit.com/r/hardwareswap, facebook.com/marketplace, ebuyer.com. Their rows rely on prior knowledge and must be re-tested later.
- **Partial:** keepa.com (title only), bestbuy.com (country landing only), overclockers.co.uk and canadacomputers.com (first 100k chars only).
- **Not searched:** PCPartPicker Canada and Australia subdomains, Newegg.ca and Amazon.ca readability, Micro Center store inventory API, eBay UK and AU Browse API coverage, Back Market UK seller pages.
- **Role/type column for direct retailers not confirmed by a fetched page** (Scan, CCL, B&H, Micro Center, Memory Express, PC Case Gear, etc.) comes from prior knowledge and is marked medium or low.
- **Freshness:** no comparator's update frequency was verified on a live page.
- **Sold by Scan/OcUK via Awin:** feed availability unconfirmed. Ask the retailer before any feed design.
- **Terms of service:** none of the readings above reviewed ToS for automated access. Robots/ToS check still required before any crawling.

## Sources

1. https://pcpartpicker.com/ (403, 2026-11-07)
2. https://uk.pcpartpicker.com/ (403, 2026-11-07)
3. https://pcpartpicker.com/api/ (403, 2026-11-07)
4. https://pricespy.co.uk/ (fetched, 2026-11-07)
5. https://www.staticice.com.au/ (fetched, 2026-11-07)
6. https://www.google.com/shopping (browser notice, 2026-11-07)
7. https://camelcamelcamel.com/ (403, 2026-11-07)
8. https://keepa.com/ (title only, 2026-11-07)
9. https://www.scan.co.uk/ (403, 2026-11-07)
10. https://www.overclockers.co.uk/ (fetched, 2026-11-07)
11. https://www.cclonline.com/ (403, 2026-11-07)
12. https://www.newegg.com/ (403, 2026-11-07)
13. https://www.bhphotovideo.com/ (403, 2026-11-07)
14. https://www.microcenter.com/ (403, 2026-11-07)
15. https://www.bestbuy.com/ (fetched, country page, 2026-11-07)
16. https://www.memoryexpress.com/ (403, 2026-11-07)
17. https://www.canadacomputers.com/ (fetched, 2026-11-07)
18. https://www.pccasegear.com/ (403, 2026-11-07)
19. https://www.ebay.com/ (403, 2026-11-07)
20. https://www.amazon.co.uk/ (rate-limited, untested, 2026-11-07)
21. https://www.backmarket.com/en-us (rate-limited, untested, 2026-11-07)
22. https://www.dell.com/en-us/shop/outlet (rate-limited, untested, 2026-11-07)
23. https://www.kijiji.ca/ (rate-limited, untested, 2026-11-07)
24. https://www.gumtree.com/ (rate-limited, untested, 2026-11-07)
25. https://www.reddit.com/r/hardwareswap/ (rate-limited, untested, 2026-11-07)
26. https://www.facebook.com/marketplace/ (rate-limited, untested, 2026-11-07)
27. https://www.ebuyer.com/ (rate-limited, untested, 2026-11-07)
28. https://github.com/cyruscuenca/PCPartPicker-API/blob/master/README.rst (search, 2026-11-07; unofficial)
29. https://developer.bestbuy.com/apis and https://bestbuyapis.github.io/api-documentation/#products-api (search, 2026-11-07)
29b. https://apify.com/parseforge/pcpartpicker-component-scraper (search, 2026-11-07; third-party scraper)
30. https://www.developer.ebay.com/api-docs/buy/browse/resources/item_summary/methods/search (search, 2026-11-07)
31. https://developer.newegg.com/?p=3794 and https://feedonomics.com/supported-channels/newegg-feed-specs/ (search, 2026-11-07)
32. https://keepa.com/api-docs/ (search, 2026-11-07)
33. https://webservices.amazon.com/paapi5/documentation/register-for-pa-api.html and https://affiliate-program.amazon.co.uk/help/node/topic/GVJ2BJP35457CLML (search, 2026-11-07); secondary: https://www.keywordrush.com/blog/amazon-pa-api-associatenoteligible-error-is-there-a-new-10-sales-rule
34. https://www.businesswire.com/news/home/20240125666246/en/Newegg-Debuts-Newegg-Refreshed-Program-to-Offer-Quality-Resale-Products-at-Low-Prices (search, 2026-11-07)
35. https://ui.awin.com/merchant-profile/15473 and https://www.scan.co.uk/affiliate-program (search, 2026-11-07)
36. https://www.overclockers.co.uk/affiliate-program and https://ui.awin.com/merchant-profile/28821 (search, 2026-11-07)
37. https://help.backmarket.com/hc/en-gb/articles/360021395800-Refurbished-in-the-UK-resold-in-the-UK and https://backmarket-business.gorgias.help/en-US/does-back-market-pro-refurbish-products-4642374 (search, 2026-11-07)
