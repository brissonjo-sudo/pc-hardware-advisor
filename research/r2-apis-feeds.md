# R2 APIs and data feeds

Collected: 2026-11-07 · Model: sonnet

Method: official pages fetched where possible; many were blocked or rate-limited by the fetch tool (marked "blocked" / "search-only"). Search-snippet facts are tagged as such and capped at medium or low confidence. All "checked" dates are 2026-11-07. Numbers in [brackets] refer to Sources.

Key point for the plugin: it cannot hold API keys. Where a key is needed, the end user must obtain and supply it through a connector they install themselves.

## Price and product APIs

| Service | Doc URL | Key / who can get one | Cost | Limits | Terms relevant | Usable by an end user | Confidence |
|---|---|---|---|---|---|---|---|
| eBay Browse API | [1] (page 403-blocked on direct fetch; facts from [2],[3]) | Yes, eBay developer account + OAuth; Buy APIs need extra license per eBay's rate-limit table | Free tier | 5,000 calls/day free tier [2]; Browse 5,000/day per [3] | API License Agreement; Compatible Application Growth Check; community quote says eBay content must not be co-mingled with non-eBay content in public display (unverified quote) [3] | Technically yes, but production Buy API access is gated; whether a private price-comparison use qualifies is unanswered officially | medium |
| eBay Marketplace Insights (sold data) | [4] | Limited release, select developers approved by eBay business units | n/a | 90-day sold history; categories whitelisted per partner [4] | Restricted API | No (not self-serve) | medium |
| Amazon PA-API 5.0 | [5] | Deprecated; calls return HTTP 403 AccessDeniedException | n/a | n/a | Replaced by Creators API | No (retired) | high |
| Amazon Creators API (successor) | [5],[6] | Must be enrolled in Amazon Associates for the marketplace; 10+ qualifying sales in a 30-day window [6] | Free | Not documented on fetched pages | Associates Operating Agreement / Program Policies (not read) | Only affiliates with sales history; not a casual user | medium |
| Keepa API | [7] | Yes, paid plan via Keepa API dashboard; no eligibility rules listed | Prepaid monthly; official page gives no price (third parties cite from ~49 EUR/month, unverified) [7],[8] | Token bucket, tokens/min by plan; 1 token per product, 10 per search [7] | Data-use terms not on docs page | Yes, if user pays and supplies own key | medium |
| Best Buy Developer API | [9] | Yes, free key from developer portal; license to apps/sites selling Best Buy products | Free | 50,000 calls/day, 5/s; over-limit returns 403 [9] | Cache max 72 h; may not use for third parties (e.g. other retailers) to analyse Best Buy pricing; must attribute and show logo [9] | Only for apps offering Best Buy products; US retailer; price-comparison across retailers is risky/likely outside terms | high (terms), medium (fit) |
| Newegg | [10] | Marketplace API is for registered sellers only | n/a | n/a | Seller-only | No public product API found | medium |
| PCPartPicker | [11],[12] | No official public API found | n/a | n/a | Terms (mirror) grant personal, non-commercial license excluding collection of listings/prices; founder said API would breach their agreements [12]; robots.txt blocks Claude-User and many AI agents site-wide [11] | No (do not fetch) | high |
| Idealo | [13] | Partner Web Service is merchant-side (maintain own offers), OAuth2 from idealo Business; needs merchant contract | n/a | n/a | Not a consumer price-read API | No | medium (search-only) |
| Geizhals / Skinflint / PriceSpy | [14] | No official public API found; affiliate/publisher access via approval; feeds go in, not out | n/a | n/a | Scrapers are third party and unverified | No | low-medium (search-only) |
| Kelkoo Shopping API | [15] | Publisher Center token (Reporting + Shopping API scopes) per third-party guide; eligibility unknown | Unknown | Unknown | Docs say written for KelkooGroup publishers; access terms not found | Unclear: publishers/affiliates only | low |
| Google Merchant API | [16] | Merchant Center account; manages the merchant's own products | Free | n/a | Content API for Shopping sunset 2026-08-18 per Google (via search snippet) [16] | No for competitor prices (merchant-side) | medium (search-only) |
| AliExpress affiliate API | [17] | Open Platform developer app + separate affiliate enrolment; signed calls | Free | New apps ~500 req/day per third-party guides | Platform agreement; portals/domains inconsistent across sources | Possible for affiliates; not casual | low (third-party only) |
| Rakuten Ichiba Item Search | [18] | Free application ID (Rakuten account); a 2026 migration may also require an access key (conflicting) | Free | 1 req/s, ~1,000/day claimed by third parties, unverified | Official site blocked by fetch tool | Yes (Japan market) | low-medium |
| Yahoo! Shopping Japan Item Search v3 | [19] | Free Client ID (needs Yahoo! JAPAN ID) | Free | Not verified | Official doc exists; terms not read | Yes (Japan market) | medium |

## Component specification data

| Source | Doc URL | Access | Terms | Usable | Confidence |
|---|---|---|---|---|---|
| TechPowerUp GPU/CPU DB | [20] | No API found; site returned 403 to fetch | robots.txt header: personal non-commercial use, automated scraping prohibited without written permission, explicitly names AI/LLM use; ClaudeBot and Claude-User/Claude-Web blocked [20] | No automated access; user may read it themselves and paste data | high |
| Intel ARK | [21] | No public API (Intel support); manual export to Excel/CSV via Product Specifications tool | ARK terms not found | Only user-driven manual export; unofficial ARK API repo archived [21] | medium |
| AMD spec pages | not found | No API found | not checked | Not documented | low |
| dbgpu / RightNow GPU database (GitHub) | [22] | Downloadable JSON/Python package | dbgpu MIT; RightNow Apache-2.0, but values derive from TechPowerUp, so upstream rights unclear | Avoid as a legal source; flag provenance | medium |
| Wikidata | [23] | Public API/SPARQL | Structured data CC0 [23]; coverage of PC parts patchy (not tested) | Yes, as a low-coverage fallback | high (license), low (coverage) |
| PCPartPicker compatibility | [11] | No API | See above | No | high |

## Exchange-rate sources

| Source | Doc URL | Key | Update | Terms / notes | Confidence |
|---|---|---|---|---|---|
| ECB euro reference rates | [24] | None | About 16:00 CET on working days (concertation ~14:10 CET); daily XML `/stats/eurofxref/eurofxref-daily.xml`, CSV zip, 90-day and full history XML [24] | Informational only, discouraged for transactions; reuse terms on separate copyright page (not read) | high |
| Frankfurter | [25] | None | Daily, time unspecified; v2 API at api.frankfurter.dev, JSON/CSV/NDJSON | Blends rates from central banks/official sources; no quotas, abuse rate limit; blended rates free for commercial use; not for live trading [25] | high |
| open.er-api.com | [26] | None (open endpoint) | Once daily | Attribution link required; cache allowed; no redistribution; 429 ban 20 min on abuse [26] | high |
| exchangerate.host | [27] | Key required (free plan 100 req/month) | n/a | Terms hosted on ideracorp.com, not read | medium |
| Bank of Canada Valet | [28] | None | Daily | Free, terms-of-use page applies; caching recommended | medium |
| US Fed H.10 | [29] | None | Daily release; weekly country data Mondays 16:15 | Noon buying rates NY; data.gov bulk | medium |
| Bank of England IADB | [30] | None (CSV endpoint) | Daily | BoE says rates are not official reference rates [30] | medium |
| Bank of Japan time-series API | [30] | None (per third-party package) | Launched 2026-02-18; credit display required | Read official manual before use | low-medium |
| RBA | not retrieved | n/a | n/a | gap | n/a |

Card networks and banks apply their own rates plus fees; all of the above are mid-market or reference rates, so the plugin must label converted prices as indicative.

## Tax and tariff data access

| Source | Doc URL | Access method | Notes | Confidence |
|---|---|---|---|---|
| UK Trade Tariff API | [31] | REST; docs say OAuth 2.0 client_credentials token via developer portal (managed credentials) | OGL v3.0; rate limiting planned from September 2026; cache 24 h; data updated daily | medium (docs page ambiguous on whether anonymous access still works) |
| EU TARIC | [32] | Web consultation (updated daily); Commission says raw data available as Excel | No official REST API confirmed | medium |
| EU TEDB (VAT rates) | [33] | SOAP web service with WSDL; documentation PDF | Commission says not a legal reference; limits undocumented | medium |
| US HTS (USITC) | [34] | REST API at hts.usitc.gov/reststop, JSON; USITC user guide PDF | Official parameter docs not read; endpoints seen via third party | medium |
| Canada CBSA | [35] | Downloadable tariff files by chapter/full, per year and amendment | No API found | medium |
| Australia | not found | n/a | gap | n/a |

## Automated-access constraints

- robots.txt is data about permitted bots. PCPartPicker [11] and TechPowerUp [20] both disallow Claude user agents; do not fetch them.
- PCPartPicker ToS (mirror) excludes collecting listings/prices; Best Buy forbids using its content to analyse pricing for other retailers; eBay requires separate display of its content; Amazon requires Associates status.
- Sites returning 403 to fetch (eBay docs, TechPowerUp) are recorded as blocked; no bypass attempted.
- The fetch tool itself was rate-limited on several domains (Google, Rakuten, Kelkoo), so some terms remain unread.
- Shipping scrapers (Apify actors for Geizhals, Idealo, etc.) is not recommended; their legality against site ToS is unverified.

## Recommendation for the plugin

Mention in CONNECTORS.md, by category:

1. **Exchange rates (built-in, no key):** ECB daily XML and Frankfurter. Both are free, keyless and documented. Show the date and "indicative, card fees extra".
2. **Tax/tariff (user-driven lookups):** UK Trade Tariff, EU TEDB, USITC HTS, CBSA files, TARIC web consultation. Tell the plugin to cite them rather than hard-code rates.
3. **Prices, optional connectors needing the user's own key:** eBay Browse (conditional on approval), Keepa (paid, Amazon price history), Yahoo! Shopping Japan and Rakuten (Japan). Best Buy only for Best Buy-specific lookups, with attribution and no cross-retailer analysis.
4. **Do not list:** PCPartPicker, TechPowerUp, Amazon PA-API (dead), Newegg, Idealo, Geizhals, Google Merchant, scraper actors.
5. **Specs:** Rely on manufacturer pages read by the user and Wikidata fallback; prices come from user-pasted data or web search for retailer pages that allow it.

## Not verified / gaps

- eBay Browse and Buy API requirements page (403) and the exact production-access path.
- Amazon Creators API rate limits and price-display terms.
- Kelkoo, Rakuten, Google Merchant and AliExpress official pages (fetch rate-limited or not reached).
- Keepa actual prices, Geizhals/PriceSpy partner programs, AMD spec access, Australian tariff and RBA rates, ECB reuse licence text, Intel ARK terms, TARIC official API, exact UK Tariff anonymous-access status.

## Sources

1. https://developer.ebay.com/api-docs/buy/browse/overview.html (403, blocked)
2. https://developer.ebay.com/api-docs/buy/marketplace-insights/overview.html (fetched 2026-11-07; free tier 5,000 calls/day)
3. https://developer.ebay.com/develop/apis/api-license-agreement (via search snippet, 2026-11-07)
4. https://edp.ebay.com/api-docs/buy/marketplace-insights/static/overview.html (via search snippet, 2026-11-07)
5. https://affiliate-program.amazon.com/creatorsapi/docs/en-us/paapiv5-deprecation (fetched 2026-11-07)
6. https://affiliate-program.amazon.com/creatorsapi/docs/en-us/introduction (fetched 2026-11-07)
7. https://keepa.com/api-docs/plans-tokens.html (fetched 2026-11-07)
8. https://revenuegeeks.com/software/keepa/api (third-party pricing, unverified)
9. https://developer.bestbuy.com/legal (fetched 2026-11-07)
10. https://developer.newegg.com/newegg_marketplace_api (via search, 2026-11-07)
11. https://pcpartpicker.com/robots.txt (fetched 2026-11-07)
12. https://be.pcpartpicker.com/tos (via search snippet, 2026-11-07)
13. https://idealo.github.io/partner-web-service/docs/v2 (via search snippet, 2026-11-07)
14. https://ce-docs.keywordrush.com/modules/affiliate/geizhalsde-module (third-party, 2026-11-07)
15. https://docs.kelkoogroup.com/for-publishers (fetched 2026-11-07)
16. https://developers.google.com/merchant/api/overview (blocked; sunset via https://www.pinmeto.com/news/google-content-api-shopping-sunset-2026/)
17. https://developers.aliexpress.com (via third-party guides, e.g. https://zuplo.com/learning-center/aliexpress-api-guide.md)
18. https://webservice.rakuten.co.jp/en/ (blocked; search-only)
19. https://developer.yahoo.co.jp/webapi/shopping/v3/itemsearch.html (via search snippet, 2026-11-07)
20. https://www.techpowerup.com/robots.txt (fetched 2026-11-07)
21. https://community.intel.com/t5/Mobile-and-Desktop-Processors/API-for-Processor-Details/m-p/1627050 and https://www.intel.com/content/www/us/en/support/articles/000007012.html (via search)
22. https://github.com/rightnow-ai/rightnow-gpu-database ; https://pypi.org/project/dbgpu/ (via search)
23. https://www.wikidata.org/wiki/Wikidata:Licensing (fetched 2026-11-07)
24. https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html (fetched 2026-11-07)
25. https://frankfurter.dev/docs/ (fetched 2026-11-07)
26. https://www.exchangerate-api.com/docs/free (fetched 2026-11-07)
27. https://exchangerate.host/ (fetched 2026-11-07)
28. https://www.bankofcanada.ca/valet-api-how-to/ (via search)
29. https://www.federalreserve.gov/RELEASES/h10/about.htm (via search)
30. https://www.bankofengland.co.uk/boeapps/database/help.asp ; https://www.boj.or.jp/en/statistics/outline/notice_2026/not260218a.htm (via search)
31. https://docs.trade-tariff.service.gov.uk/ (fetched 2026-11-07)
32. https://taxation-customs.ec.europa.eu/customs/calculation-customs-duties/customs-tariff/eu-customs-tariff-taric_en (via search)
33. https://taxation-customs.ec.europa.eu/system/files/2021-06/soap_webservice_documentation.pdf (via search)
34. https://catalog.data.gov/dataset/harmonized-tariff-schedule-of-the-united-states-2023 (HTS REST API listing, via search)
35. https://www.cbsa-asfc.gc.ca/trade-commerce/tariff-tarif/menu-eng.html (via search)
