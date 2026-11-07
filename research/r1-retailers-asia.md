# R1 Retailers: China (official stores) and Japan
Collected: 2026-11-07 · Model: haiku · Method: WebFetch on homepages/store pages (one retry on timeouts); WebSearch for store/API claims, marked as unverified unless fetched.

Legend: Auto-readable = yes / partial / blocked (with HTTP code or error). "Search only" = claim seen in a search snippet, page not fetched. Confidence: high / medium / low.

## China official stores

| Name | URL | Type | Ships to | Auto-readable | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| AliExpress (platform) | https://www.aliexpress.com/ | marketplace | not verified | partial (fetch returned empty body) | none found on fetch; affiliate API claims in search only | Platform, not a brand store. Choice program and IOSS status: see "Gaps". | low | [S1], [S35] |
| AliExpress Lian Li store | https://www.aliexpress.com/store/1101594887 | manufacturer store (linked from brand site) | not verified | partial (empty body) | none | Link to this store appears on lian-li.com Support menu, so the brand self-declares it. Badge not seen. | medium (brand link) / low (badge) | [S2], [S22] |
| Thermalright (brand site) | https://www.thermalright.com/ | manufacturer site | not stated on page | yes | none | Footer "Thermalright Inc."; lists 5-year warranty on some models; sales via "Find Distributors" and resellers; no AliExpress/Amazon/JD store links found. Newegg "Thermalright Authorized Store" seen in search only. | high (site is brand's) / low (no China store found) | [S18], [S30] |
| Peerless Assassin (Thermalright line) | n/a verified | manufacturer line | not verified | n/a | none | Search found only third-party sellers (e.g. "AliExpress-226247430" on Buywisely) and resellers. Official AliExpress store NOT confirmed. | low | [S30] |
| Lexar | https://www.lexar.com/ | manufacturer site (FR locale served) | not verified | yes | none | Served as lexar.com/fr (France). Store link is "Où acheter". No AliExpress/JD store link. Warranty page linked but not read. Lexar China store not fetched. | medium (brand) / low (China store) | [S19] |
| Kingbank | not fetched (search only) | manufacturer store claimed on AliExpress | not verified | not tested | none | Search: a review says purchase via "KingBank official AliExpress store"; a Newegg listing credits "KingBank Official Store". One rep post says AliExpress buyers had warranty problems (anecdotal). Store page not located. | low | [S29] |
| Asgard (阿斯加特) | https://www.asgard.com.cn/ | manufacturer site (Shenzhen) | not stated | yes | none | Sells DDR4/DDR5 RAM and SSDs. No e-commerce store link on site. Hotline and email listed; EN site asgardoc.com linked. Warranty and foreign-buyer terms not on page. | high (site) / low (store) | [S25] |
| Montech | https://www.montech.com/ | manufacturer site (Swiss AG) | not stated | yes | none | Official shop is montech.com/ch (Switzerland). Regional site /us/en. No marketplace links. Montech China store not verified. montechworld.com: DNS error. | medium | [S21], [S20] |
| Fanxiang | https://www.fanxiang.com/ | manufacturer site (claimed) | not verified | partial (page text minimal, nothing usable) | none | Official status not confirmed; no store links in content. | low | [S23] |
| SAMA | https://www.sama.com.cn/ | not verified | n/a | blocked (TLS certificate name mismatch) | none | Cannot verify. Not bypassed. | n/a | [S24] |
| MSI China store | https://www.msi.com/ | manufacturer site | not verified | blocked (HTTP 403) | none | msi.com.cn not tested. | n/a | [S26] |
| ASUS China store | https://www.asus.com.cn/ | manufacturer site | China only (per title) | partial (title only; body empty) | none | Page title says "华硕电脑官方直营平台" (official direct-sales platform). Domain and store links not confirmed from body. | low | [S27] |
| JD Worldwide (JD Global) | https://global.jd.com/ | marketplace (cross-border) | not stated | yes | none | Title "京东全球版". Footer shows mainland operator (Beijing filing). No official-store badge text found. Shipping countries not stated on homepage. | medium (platform identity) / low (shipping) | [S16] |
| Tmall Global | https://global.tmall.com/ | marketplace (cross-border) | not verified | blocked (HTTP 404) | none | Cannot verify. | n/a | [S17] |
| Montech / Asgard / Thermalright shipping to EU/US/UK | n/a | n/a | not verified | n/a | n/a | No brand site above states EU/US/UK shipping terms. Do not assume. | low | [S18], [S21], [S25] |

Seller type reminders for China:
- AliExpress "Choice" and IOSS (VAT at checkout for EU): see Gaps. Duty mechanics conflict across sources; treat as unverified.
- Official-store verification method used: brand site link to store (medium). Store badge check on the live store was NOT possible because store pages returned empty bodies.

## Japan

| Name | URL | Type | Ships to | Auto-readable | API/feed | Notes | Confidence | Source |
|---|---|---|---|---|---|---|---|---|
| Kakaku.com (価格.com) | https://kakaku.com/ | price comparator | n/a | yes (JP text garbled in fetch, structure readable) | RSS (news) only; official product API from 2006 ("価格.com Webサービス") historical, current status unknown | No merchant API found on site. Third-party scrapers exist (ToS not reviewed). Merchant shop listing page /shopentry/ exists. | high (site) / low (API status) | [S4], [S34] |
| Dospara (ドスパラ) | https://www.dospara.co.jp/ | direct retailer (also used-goods and buyback) | Domestic only per page evidence; overseas not mentioned | yes | none found | BTO PCs and parts; 中古販売 (used sales) and 中古買取 (buyback). Footnote: some models made abroad (manufacturing, not delivery). | high | [S6] |
| PC工房 (Pc-koubou) | https://www.pc-koubou.jp/ | direct retailer | Domestic; overseas not mentioned | yes | none found | Operated by Unitcom. 1-year standard warranty; 3/4-year optional. Okinawa logistics. | high | [S7] |
| Tsukumo | https://www.tsukumo.co.jp/ | direct retailer | not verified | blocked/unreachable (socket hang up, 2 attempts) | none found | Not read. Retry later. | n/a | [S5] |
| Ark (ark-pc) | https://www.ark-pc.co.jp/ | direct retailer | not verified | blocked (HTTP 403) | none found | Not bypassed. | n/a | [S8] |
| Yodobashi.com | https://www.yodobashi.com/ | direct retailer (mass) | not verified | blocked/unreachable (timeout, 2 attempts) | none found | Not read. | n/a | [S9] |
| Bic Camera | https://www.biccamera.com/ | direct retailer (mass) | not verified | blocked/unreachable (timeout, 2 attempts) | none found | Not read. | n/a | [S10] |
| Sofmap (ソフマップ) | https://www.sofmap.com/ | direct retailer + used (Recole) | Domestic; overseas not mentioned | yes | none found | PC parts category present; used goods (Recole) and trade-in. | high | [S11] |
| Janpara (ジャンク・パラダイス) | https://www.janpara.co.jp/ | used/refurbished pro shop | Not visible in read range | yes (partial: first 100k of 184k chars read) | none found | Used PC parts with condition grades A-D (中古). Shipping page linked, not read. | medium | [S15] |
| Amazon.co.jp | https://www.amazon.co.jp/ | marketplace (mixed 1P/3P) | not verified | blocked (HTTP 403, then 503) | Product Advertising API not checked (not searched) | Not bypassed. | n/a | [S12] |
| Mercari (メルカリ) | https://jp.mercari.com/ | private classifieds (C2C) + business sellers (Mercari Shops) | Not stated; "メルカリUS" link only | yes | none found (not searched) | Buyers commonly reach it via proxies (see below). | medium | [S13] |
| Yahoo! Auctions (ヤフオク!) | https://auctions.yahoo.co.jp/ | private classifieds (auction) | not stated | blocked (HTTP 403) | see Yahoo Shopping API below (different service) | Not read. | n/a | [S14] |
| PayPay Flea Market (Yahoo Flea) | not fetched | private classifieds | not stated | not tested | not searched | Listed in brief; not tested. | n/a | n/a |
| Yahoo! Shopping (API) | https://developer.yahoo.co.jp/webapi/shopping/v3/itemsearch.html | API (not a shop) | n/a | blocked for direct fetch (HTTP 403); content from search snippet | Item Search v3: keyword, JAN, genre, brand, store ID; JSON; approx 1 query/sec per snippet; appid required (per search snippet and third-party README) | Official Yahoo developer network. Use requires agreeing to Yahoo! Developer Network guidelines. Credit notice required in displayed data (third-party README). v1 discontinued 30 Jun 2020. | medium (existence, from search) / low (limits) | [S28], [S31] |
| Rakuten Ichiba (API) | Rakuten Web Service | API | n/a | not fetched (official docs not reached) | Ichiba Item Search; application_id required; access_key claimed required since Feb 2026 (third-party only) | Rate and result caps conflict across sources (1 req/s; 100 or 3,000 items). Affiliate ID optional. | low (search only) | [S32] |
| Proxy: Buyee | https://japanlanded.pages.dev/articles/buyee-vs-zenmarket/ | proxy-buying service | Yes (intl forwarding) | not fetched | none | Fees conflict: ¥500/order (one source, per-order from Apr 2026) vs ¥300-500 + 5-10% (another). Official Mercari partner per one blog. | low | [S36] |
| Proxy: ZenMarket | https://japanlanded.pages.dev/articles/buyee-vs-zenmarket/ | proxy-buying service | Yes | not fetched | none | ¥800/item on Mercari and Yahoo Auctions per one source. | low | [S36] |
| Proxy: OneMall | https://blog.onemall.jp/?p=2107 | proxy-buying service | Yes | not fetched | none | 3% of winning bid on Yahoo Auctions, min ¥200, max ¥300 (blog claim). | low | [S36] |

Seller type summary:
- Direct retailers (domestic-only per page evidence): Dospara, PC工房, Sofmap, (Tsukumo, Ark, Yodobashi, Bic Camera unverified).
- Marketplaces: Amazon.co.jp (blocked), JD Worldwide (China, see above).
- Professional refurbishers: Janpara, Dospara used, Sofmap Recole.
- Private classifieds: Mercari (readable), Yahoo! Auctions (blocked).
- Manufacturer stores: see China table.
- Proxy-buying services: Buyee, ZenMarket, OneMall (fees from blogs only; treat as separate seller type with extra fees).
- Price comparator: Kakaku.com.

## Not verified / gaps

1. AliExpress homepage and Lian Li store returned empty bodies. Official badge and shipping destinations not verified. AliExpress help center redirected to a maintenance page; not followed.
2. Choice program and IOSS: secondary sources only (S35). They disagree on who collects duty and on the 1 July 2026 change (€150 exemption removal, €3 per-item/per-code duty). Check EU Commission customs pages and AliExpress buyer help before use.
3. Warranty for foreign buyers: not confirmed for any China brand. Only Thermalright (5-year on some models, domestic-facing wording) and Lexar (France site) have warranty pages linked; not read.
4. Official status for Peerless Assassin, Kingbank, Fanxiang, Asgard AliExpress stores: not confirmed. No store badge checked live.
5. Blocked or unreachable (8): Ark (403), Tsukumo (socket hang up x2), Yodobashi (timeout x2), Bic Camera (timeout x2), Amazon.co.jp (403, 503), Yahoo! Auctions (403), Yahoo developer page (403), MSI (403). Plus errors: Tmall Global (404), montechworld.com (DNS), SAMA (TLS mismatch). Not bypassed.
6. Japan shipping-abroad policy: not stated on any Japanese retailer homepage read. Confirm on each 特定商取引法 page (not fetched).
7. Rakuten and AliExpress affiliate API terms, rate limits and approval: search snippets and third-party guides only. Conflicting figures. Official docs not reached.
8. Kakaku.com merchant or product API: no current official program found. 2006 service status unknown.
9. Mercari, PayPay Flea Market, Janpara shipping and API status: not searched or only partially read.
10. JD Worldwide shipping countries and official-store badges: not verified.
11. Proxy fees: contradictory blog figures. Not verified on provider sites.

## Sources (numbered URLs)

S1. https://www.aliexpress.com/ (fetched 2026-11-07, empty body)
S2. https://www.aliexpress.com/store/1101594887 (fetched 2026-11-07, empty body)
S3. https://www.aliexpress.com/help/help_center.html (fetched 2026-11-07, 302 to maintenance page, not followed)
S4. https://kakaku.com/ (fetched 2026-11-07, loaded)
S5. https://www.tsukumo.co.jp/ (fetched 2026-11-07, socket hang up x2)
S6. https://www.dospara.co.jp/ (fetched 2026-11-07, loaded)
S7. https://www.pc-koubou.jp/ (fetched 2026-11-07, loaded)
S8. https://www.ark-pc.co.jp/ (fetched 2026-11-07, HTTP 403)
S9. https://www.yodobashi.com/ (fetched 2026-11-07, timeout x2)
S10. https://www.biccamera.com/ (fetched 2026-11-07, timeout x2)
S11. https://www.sofmap.com/ (fetched 2026-11-07, loaded)
S12. https://www.amazon.co.jp/ (fetched 2026-11-07, HTTP 403 then 503)
S13. https://jp.mercari.com/ (fetched 2026-11-07, loaded)
S14. https://auctions.yahoo.co.jp/ (fetched 2026-11-07, HTTP 403)
S15. https://www.janpara.co.jp/ (fetched 2026-11-07, loaded, partial)
S16. https://global.jd.com/ (fetched 2026-11-07, loaded)
S17. https://global.tmall.com/ (fetched 2026-11-07, HTTP 404)
S18. https://www.thermalright.com/ (fetched 2026-11-07, loaded)
S19. https://www.lexar.com/ (fetched 2026-11-07, loaded, FR locale)
S20. https://www.montechworld.com/ (fetched 2026-11-07, DNS error)
S21. https://www.montech.com/ (fetched 2026-11-07, loaded)
S22. https://lian-li.com/ (fetched 2026-11-07, loaded)
S23. https://www.fanxiang.com/ (fetched 2026-11-07, loaded, minimal)
S24. https://www.sama.com.cn/ (fetched 2026-11-07, TLS mismatch)
S25. https://www.asgard.com.cn/ (fetched 2026-11-07, loaded)
S26. https://www.msi.com/ (fetched 2026-11-07, HTTP 403)
S27. https://www.asus.com.cn/ (fetched 2026-11-07, title only)
S28. https://developer.yahoo.co.jp/webapi/shopping/v3/itemsearch.html (fetch 2026-11-07, HTTP 403; content from search snippet)
S29. Search 2026-11-07: "Kingbank official store AliExpress" (snippets incl. https://www.newegg.com/kingbank-32gb-ddr5-6400-cas-latency-cl32-memory-white/p/0RN-012W-00028)
S30. Search 2026-11-07: "Peerless Assassin official store AliExpress Thermalright" (snippets incl. https://www.newegg.com/global/il-en/Seller-Store/Thermalright-Authorized-Store and https://buywisely.com.au/product/thermalright-peerless-assassin-120-se-cpu-air-cooler-6-heat-pipes-cpu-cooler-dual-120mm-tl-c12c-pwm-fan-aluminium-heatsink-cover-aghp-technology)
S31. Search 2026-11-07: "Yahoo! Shopping API developer" (snippet from https://developer.yahoo.co.jp/webapi/shopping/v3/)
S32. Search 2026-11-07: "Rakuten Web Service API ichiba" (https://www.rubydoc.info/gems/rakuten_web_service/1.4.0; https://apify.com/fruitful_quintessence/rakuten-japan-mcp - third-party)
S33. Search 2026-11-07: "AliExpress Affiliate API" (https://rapidevelopers.com/replit-integration/aliexpress-api - vendor guide, low weight)
S34. Search 2026-11-07: "kakaku.com API" (https://webtan.impress.co.jp/node/267; https://metacpan.org/pod/WebService::KakakuCom)
S35. Search 2026-11-07: "AliExpress Choice IOSS VAT EU 2026" (https://yakkyofy.com/aliexpress-import-tax-what-to-do/; https://easproject.com/ioss-registration-1-july-3-euro-duty/)
S36. Search 2026-11-07: "Japan proxy buying service fees" (https://japanlanded.pages.dev/articles/buyee-vs-zenmarket/; https://blog.onemall.jp/?p=2107)
