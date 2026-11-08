# Audit A6b: factual accuracy, retailers outside Europe, and retry of blocked official pages

- Axis: A (factual accuracy)
- Date: 2026-11-08
- Model: Haiku 5.5 (claude-haiku-5-5)
- Tool calls: 33 (28 WebFetch, 2 Read, 1 ToolSearch, 2 Grep)
- Files read: `research/audit/_brief.md`, `references/retailers-by-country.md` (sections United States, Canada, Australia, Japan, China official stores, Cross-border, When a site is blocked, Not verified, Sources). Grep only (not read in full): `references/form-factors-cases.md`, `references/international-buying.md`, `references/sockets-chipsets.md`, `references/memory.md`, `references/power-supplies-connectors.md`.
- Part 1: 18 fetches (cap 25). Part 2: 10 fetches (cap 12).
- No file in the repository was modified.

## Method notes

- Part 1 sample: first 3 rows of each country section (US, CA, AU, JP, CN), plus 7 direct retailers outside those rows (Dell Outlet, Sofmap, Scorptec, Umart, Centre Com, Janpara, Back Market US).
- Rows previously recorded as blocked on 2026-11-07 were not fetched again (brief rule 4: never retry a blocked site). They are `not-checked` below.
- Part 2 retries used a different official page from the failed one, as the brief asks. No cache, mirror, archive or alternate user agent was used.
- Part 2 notes: no retry returned a new value. No value was confirmed or changed in Part 2. A1, A2 and A4 should keep the existing values, marked as unverified where the table says so.
- Cross-border and blocked-site rules (retailers-by-country.md:230-259) were checked as text against the fetched pages. Japan and Cross-border statements were tested against Dospara, PC Koubou and Sofmap.

## Findings

| id | axis | severity | evidence | failure_case | minimal_fix | effort |
|---|---|---|---|---|---|---|
| royal-mail-fee-figure-from-excerpt-only | A | major | references/international-buying.md:87; references/international-buying.md:168; https://www.royalmail.com/receiving-mail (checked 2026-11-08, HTTP 403) | A UK buyer budgets the GBP 8 Royal Mail fee. The figure comes from a search excerpt. The fee may be GBP 12 (Parcelforce) or a different amount, so the landed cost is wrong. | Label the GBP 8 / GBP 12 figure in every answer as "search excerpt, official page not read". Do not present it as confirmed. | S |
| lian-li-a4h2o-fit-rule-unverified | A | major | references/form-factors-cases.md:73; https://lian-li.com/ (checked 2026-11-08, homepage readable, A4-H2O X4 not listed) | The rule "SFX / SFX-L only" rests on retailer data. If the manufacturer lists ATX or SFX-L support differently, the fit check rejects a valid build or accepts an invalid one, and the buyer purchases the wrong case or PSU. | Mark the fit verdict for this case as "retailer data only, check the case page" until a manufacturer page is read. | S |
| ato-abf-low-value-gst-rules-unverified | A | minor | references/international-buying.md:205; references/international-buying.md:206; https://www.ato.gov.au/businesses-and-organisations/international-tax-for-business/gst-for-non-resident-businesses (checked 2026-11-08, HTTP 403); https://www.abf.gov.au/importing-exporting-and-manufacturing/importing/how-to-import (checked 2026-11-08, HTTP 403) | An Australian buyer is told about GST on low-value goods from an unread source. | Keep the entries as "blocked" in the file and say so in any answer about Australian import tax. | S |
| ups-fedex-uk-france-brokerage-no-figure | A | minor | references/international-buying.md:89; references/international-buying.md:212; https://www.ups.com/gb/en/support/shipping-support.page (checked 2026-11-08, "Access Denied"); https://www.fedex.com/en-gb/shipping/customs.html (checked 2026-11-08, access denied) | No brokerage fee is known for UPS or FedEx to UK or France. A buyer may not expect one. The file already states "No figure", so no wrong number is given. | Keep "no figure" in the file. Tell the buyer to ask the carrier before ordering. | S |
| meshroom-s-spec-source-blocked | A | minor | references/form-factors-cases.md:74; https://ssupd.co/products/cases-meshroom-s-v1 (checked 2026-11-08, HTTP 429, Retry-After 60) | GPU or cooler clearance for the Meshroom S is wrong by a few millimetres because the version differences are not resolved. | Keep the "medium (version differences)" label and ask the user to confirm the GPU length and layout. | S |
| amd-9800x3d-ppt-unverified | A | minor | references/power-supplies-connectors.md:136; https://www.amd.com/en/products/processors/technologies/3d-v-cache.html (checked 2026-11-08, timeout after 60 s) | PSU headroom for a 9800X3D build uses a PPT of 162 W taken from reviews. If AMD's figure differs, the headroom is wrong. | Keep the label "medium (reviews; amd.com blocked)". Do not present 162 W as AMD's value. | S |
| amd-am5-2029-statement-unverified | A | minor | references/sockets-chipsets.md:163; https://www.amd.com/en/newsroom.html (checked 2026-11-08, HTTP 403) | A buyer is told AM5 support is guaranteed to 2029. The statement has no primary source read today. | Attribute the 2029 statement to a search summary, not to AMD, until the AMD page is read. | S |
| dell-outlet-link-resolves-to-sitemap | A | minor | references/retailers-by-country.md:154; https://www.dell.com/en-us/shop/outlet (checked 2026-11-08, returned "Dell Sitemap" page) | The row's link opens a sitemap page, not the outlet listing. A user following it cannot see outlet prices. | Replace the link with the outlet listing path after a live check, or record "outlet listing not read". | S |
| janpara-seller-type-mismatch | A | minor | references/retailers-by-country.md:195; https://www.janpara.co.jp/ (checked 2026-11-08, site describes 中古販売 used sales and 買取 buyback) | The row says "professional refurbisher" with grades A to D. A buyer expects graded refurbished parts, but the site describes used goods sales. | Change the type to "used-goods retailer (sales and buyback)" and remove the grade claim unless a grading page is read. | S |
| mwave-direct-label-with-supplier-stock | A | minor | references/retailers-by-country.md:174; https://www.mwave.com.au/ (checked 2026-11-08, "Shipped by: Mwave" and "Available at Supplier") | The row says direct retailer. Some offers are held by suppliers, so the stock and seller differ per offer. A buyer assumes Mwave holds the item. | Type Mwave as "direct retailer (mixed, some supplier-held offers)" and check the seller per offer. | S |
| staticice-readability-downgraded | A | info | references/retailers-by-country.md:172; https://www.staticice.com.au/ (checked 2026-11-08) | Row says "yes (homepage)". Today the homepage has no product or price text. | Update the readability column to "partial (no product or price text on homepage)". | S |
| kakaku-readability-downgraded | A | info | references/retailers-by-country.md:187; https://kakaku.com/ (checked 2026-11-08, title and most Japanese text garbled, some prices readable) | Row says "yes". Text is garbled, so a parser may read wrong names. | Update to "partial (encoding corrupted)". | S |
| sofmap-readability-garbled | A | info | references/retailers-by-country.md:194; https://www.sofmap.com/ (checked 2026-11-08, Shift-JIS decoded as another character set) | Row says "yes". Product names and seller wording are not readable, so "Overseas not mentioned" and "sells own products" cannot be checked. | Update to "partial (encoding corrupted)" and keep the claim as not verified. | S |
| aliexpress-pages-empty-body | A | info | references/retailers-by-country.md:209; references/retailers-by-country.md:210; https://www.aliexpress.com/ and https://www.aliexpress.com/store/1101594887 (checked 2026-11-08, empty body) | The platform and the Lian Li store show no content. A reader may take the empty body as a store with no products. | Keep "partial (empty body)" and do not infer store status from it. | S |
| newegg-canada-blocked-403 | A | info | references/retailers-by-country.md:164; https://www.newegg.ca/ (checked 2026-11-08, HTTP 403) | Row said "not tested". The site is now a confirmed block, so a Canadian buyer gets no Newegg prices. | Change to "blocked (HTTP 403, 2026-11-08)". | S |
| scorptec-blocked-403 | A | info | references/retailers-by-country.md:175; https://www.scorptec.com.au/ (checked 2026-11-08, HTTP 403) | Row said "not tested (rate limit)". The site is now a confirmed block. | Change to "blocked (HTTP 403, 2026-11-08)". | S |
| centre-com-blocked-405 | A | info | references/retailers-by-country.md:177; https://www.centrecom.com.au/ (checked 2026-11-08, HTTP 405 Method Not Allowed) | Row said "not tested (rate limit)". The site returns a method error, not content. | Change to "blocked (HTTP 405, 2026-11-08)". | S |
| bestbuy-landing-page-only | A | info | references/retailers-by-country.md:148; https://www.bestbuy.com/ (checked 2026-11-08, country chooser only) | Row cites "partial (country landing only)". The seller type "direct retailer" cannot be confirmed from the landing page, so PC-part prices are unverified. | Keep the row at "could-not-verify" for seller type until a product page is read. | S |
| pc-koubou-third-party-brands | A | info | references/retailers-by-country.md:189; https://www.pc-koubou.jp/ (checked 2026-11-08, operated by Unitcom, also sells other makers' PCs) | "Direct retailer" fits the store, but the store sells third-party maker products. A reader may take all listed products as own stock. | Add "also sells other makers' PCs" to the row note. | S |
| canada-computers-template-placeholders | A | info | references/retailers-by-country.md:162; https://www.canadacomputers.com/ (checked 2026-11-08, unrendered template placeholders such as "[[ preferedStore.distance ]]") | Page text shows template placeholders and "Loading..." in places. Prices are readable, but a scraper may misread the page. | Keep "yes (first 100k of 164k chars)" and add the placeholder note. | S |

Counts by severity: blocker 0, major 2, minor 8, info 10 (total 20).

## Claim table

| claim_id | file:line | stated_value | official_source_url | checked_on | result | note |
|---|---|---|---|---|---|---|
| A6b-01 | references/retailers-by-country.md:146 | Newegg, marketplace (mixed), blocked HTTP 403 | https://www.newegg.com/ | 2026-11-08 | not-checked | Prior 2026-11-07 HTTP 403. Not retried (brief rule 4). |
| A6b-02 | references/retailers-by-country.md:147 | Newegg Refreshed, refurbisher, 90-day refund (2024 launch) | https://www.newegg.com/ | 2026-11-08 | not-checked | Shares the Newegg domain. No page fetched. Not retried. |
| A6b-03 | references/retailers-by-country.md:148 | Best Buy, direct retailer | https://www.bestbuy.com/ | 2026-11-08 | could-not-verify | Landing page only (country chooser). No seller wording and no product text. |
| A6b-04 | references/retailers-by-country.md:148 | Best Buy Products API, free key, 50,000 calls/day | not fetched | 2026-11-08 | not-checked | Developer page not in this sample. |
| A6b-05 | references/retailers-by-country.md:149 | B&H Photo, direct retailer | https://www.bhphotovideo.com/ | 2026-11-08 | not-checked | Prior HTTP 403. Not retried. |
| A6b-06 | references/retailers-by-country.md:150 | Micro Center, direct retailer | https://www.microcenter.com/ | 2026-11-08 | not-checked | Prior HTTP 403. Not retried. |
| A6b-07 | references/retailers-by-country.md:151 | Amazon US, marketplace (mixed) | https://www.amazon.com/ | 2026-11-08 | not-checked | Not sampled. |
| A6b-08 | references/retailers-by-country.md:152 | eBay US, marketplace (third-party seller) | https://www.ebay.com/ | 2026-11-08 | not-checked | Prior HTTP 403. Not retried. |
| A6b-09 | references/retailers-by-country.md:153 | Back Market US, professional refurbisher marketplace | https://www.backmarket.com/en-us | 2026-11-08 | confirmed | Site calls itself "a global marketplace" with "250+ refurbishers". |
| A6b-10 | references/retailers-by-country.md:153 | 12-month seller warranty (help center) | https://www.backmarket.com/en-us | 2026-11-08 | confirmed | Homepage description says "1-year warranty, 30-day money back guarantee". Help article not read. |
| A6b-11 | references/retailers-by-country.md:154 | Dell Outlet, manufacturer store | https://www.dell.com/en-us/shop/outlet | 2026-11-08 | confirmed | Sitemap lists "Dell Outlet (Certified Refurbished)". Outlet listing not read. See finding dell-outlet-link-resolves-to-sitemap. |
| A6b-12 | references/retailers-by-country.md:155 | Reddit r/hardwareswap, private party | https://www.reddit.com/r/hardwareswap/ | 2026-11-08 | not-checked | Not sampled. |
| A6b-13 | references/retailers-by-country.md:156 | Facebook Marketplace, private party | https://www.facebook.com/marketplace/ | 2026-11-08 | not-checked | Not sampled. |
| A6b-14 | references/retailers-by-country.md:162 | Canada Computers & Electronics, direct retailer | https://www.canadacomputers.com/ | 2026-11-08 | confirmed | "Proudly Canadian-Owned". No marketplace or third-party wording in first 100k chars. |
| A6b-15 | references/retailers-by-country.md:163 | Memory Express, direct retailer | https://www.memoryexpress.com/ | 2026-11-08 | not-checked | Prior HTTP 403. Not retried. |
| A6b-16 | references/retailers-by-country.md:164 | Newegg Canada, marketplace (mixed) | https://www.newegg.ca/ | 2026-11-08 | blocked | HTTP 403 on this session's fetch. |
| A6b-17 | references/retailers-by-country.md:165 | Amazon.ca, marketplace (mixed) | https://www.amazon.ca/ | 2026-11-08 | not-checked | Not sampled. |
| A6b-18 | references/retailers-by-country.md:166 | Kijiji, private party (mixed) | https://www.kijiji.ca/ | 2026-11-08 | not-checked | Not sampled. |
| A6b-19 | references/retailers-by-country.md:172 | StaticICE, price comparator, "199 Australian stores" | https://www.staticice.com.au/ | 2026-11-08 | confirmed | Page text: "Finding you the best tech deals from 199 Australian stores". |
| A6b-20 | references/retailers-by-country.md:172 | StaticICE sister sites NZ, UK, US | https://www.staticice.com.au/ | 2026-11-08 | confirmed | Footer lists the three sister sites. |
| A6b-21 | references/retailers-by-country.md:172 | StaticICE readability "yes (homepage)" | https://www.staticice.com.au/ | 2026-11-08 | changed | New value: partial, no product or price text on homepage. |
| A6b-22 | references/retailers-by-country.md:173 | PC Case Gear, direct retailer | https://www.pccasegear.com/ | 2026-11-08 | not-checked | Prior HTTP 403. Not retried. |
| A6b-23 | references/retailers-by-country.md:174 | Mwave, direct retailer | https://www.mwave.com.au/ | 2026-11-08 | could-not-verify | "Shipped by: Mwave" and "Available at Supplier" on listings. Type mixed. |
| A6b-24 | references/retailers-by-country.md:175 | Scorptec, direct retailer | https://www.scorptec.com.au/ | 2026-11-08 | blocked | HTTP 403. |
| A6b-25 | references/retailers-by-country.md:176 | Umart, direct retailer | https://www.umart.com.au/ | 2026-11-08 | confirmed | Own-shop wording "Australia's No.1 Computer Store". No product prices in visible text (partial). |
| A6b-26 | references/retailers-by-country.md:177 | Centre Com, direct retailer | https://www.centrecom.com.au/ | 2026-11-08 | blocked | HTTP 405 Method Not Allowed. |
| A6b-27 | references/retailers-by-country.md:178 | Amazon AU, marketplace (mixed) | https://www.amazon.com.au/ | 2026-11-08 | not-checked | Not sampled. |
| A6b-28 | references/retailers-by-country.md:179 | Gumtree AU, private party | https://www.gumtree.com.au/ | 2026-11-08 | not-checked | Not sampled. |
| A6b-29 | references/retailers-by-country.md:187 | Kakaku.com, price comparator | https://kakaku.com/ | 2026-11-08 | confirmed | Comparator (prices and merchant listings). Text partly garbled; see finding kakaku-readability-downgraded. |
| A6b-30 | references/retailers-by-country.md:187 | Kakaku merchant API not found | https://kakaku.com/ | 2026-11-08 | not-checked | Not searched on this pass. |
| A6b-31 | references/retailers-by-country.md:188 | Dospara, direct retailer (own sales, used and buyback) | https://www.dospara.co.jp/ | 2026-11-08 | confirmed | "パソコン販売店" with own products ("当社製", "弊社販売デスクトップPC"). |
| A6b-32 | references/retailers-by-country.md:188 | Dospara domestic only per page evidence | https://www.dospara.co.jp/ | 2026-11-08 | confirmed | No overseas shipping statement. "海外生産" refers to manufacturing. |
| A6b-33 | references/retailers-by-country.md:189 | PC Koubou, direct retailer (Unitcom) | https://www.pc-koubou.jp/ | 2026-11-08 | confirmed | "株式会社ユニットコムが運営する" store. Also lists other makers' PCs. |
| A6b-34 | references/retailers-by-country.md:189 | PC Koubou 1-year standard warranty | https://www.pc-koubou.jp/ | 2026-11-08 | not-checked | Warranty terms not on homepage. |
| A6b-35 | references/retailers-by-country.md:190 | Tsukumo, direct retailer | https://www.tsukumo.co.jp/ | 2026-11-08 | not-checked | Prior socket hang up (2 attempts). Not retried. |
| A6b-36 | references/retailers-by-country.md:191 | Ark, direct retailer | https://www.ark-pc.co.jp/ | 2026-11-08 | not-checked | Prior HTTP 403. Not retried. |
| A6b-37 | references/retailers-by-country.md:192 | Yodobashi, direct retailer | https://www.yodobashi.com/ | 2026-11-08 | not-checked | Prior timeouts (2 attempts). Not retried. |
| A6b-38 | references/retailers-by-country.md:193 | Bic Camera, direct retailer | https://www.biccamera.com/ | 2026-11-08 | not-checked | Prior timeouts (2 attempts). Not retried. |
| A6b-39 | references/retailers-by-country.md:194 | Sofmap, direct retailer | https://www.sofmap.com/ | 2026-11-08 | could-not-verify | Encoding garbled. Own-product wording not readable. |
| A6b-40 | references/retailers-by-country.md:195 | Janpara, professional refurbisher, grades A to D | https://www.janpara.co.jp/ | 2026-11-08 | changed | New value: used-goods retailer (中古販売 sales, 買取 buyback). Grades A to D not seen on homepage. |
| A6b-41 | references/retailers-by-country.md:196 | Amazon.co.jp, marketplace (mixed) | https://www.amazon.co.jp/ | 2026-11-08 | not-checked | Prior HTTP 403 and 503. Not retried. |
| A6b-42 | references/retailers-by-country.md:197 | Mercari, private party | https://jp.mercari.com/ | 2026-11-08 | not-checked | Not sampled. |
| A6b-43 | references/retailers-by-country.md:198 | Yahoo! Auctions, private party | https://auctions.yahoo.co.jp/ | 2026-11-08 | not-checked | Prior HTTP 403. Not retried. |
| A6b-44 | references/retailers-by-country.md:200 | Yahoo! Shopping Item Search v3 (free client ID, about 1 query/s) | https://developer.yahoo.co.jp/webapi/shopping/v3/itemsearch.html | 2026-11-08 | not-checked | Prior HTTP 403. Not retried. |
| A6b-45 | references/retailers-by-country.md:209 | AliExpress platform, marketplace (third-party seller) | https://www.aliexpress.com/ | 2026-11-08 | could-not-verify | Empty body. No HTTP error reported. |
| A6b-46 | references/retailers-by-country.md:210 | AliExpress Lian Li store, linked from lian-li.com | https://www.aliexpress.com/store/1101594887 | 2026-11-08 | could-not-verify | Empty body. Link on lian-li.com not seen in homepage text. |
| A6b-47 | references/retailers-by-country.md:211 | Thermalright, manufacturer site, no AliExpress/Amazon/JD link | https://www.thermalright.com/ | 2026-11-08 | confirmed | Manufacturer footer (founded 2001). No AliExpress, Amazon or JD link in page text. |
| A6b-48 | references/retailers-by-country.md:211 | Thermalright sales via "Find Distributors" | https://www.thermalright.com/ | 2026-11-08 | confirmed | "Find Distributors" on each featured product. |
| A6b-49 | references/retailers-by-country.md:212-218 | China brand store rows (Peerless Assassin, Kingbank, Asgard, Montech, Fanxiang, SAMA, MSI, ASUS CN) | not fetched | 2026-11-08 | not-checked | Not sampled. |
| A6b-50 | references/retailers-by-country.md:213 | Lexar, "Où acheter" store link | https://www.lexar.com/ | 2026-11-08 | not-checked | Not sampled. |
| A6b-51 | references/retailers-by-country.md:221 | JD Worldwide, cross-border marketplace | https://global.jd.com/ | 2026-11-08 | not-checked | Not sampled. |
| A6b-52 | references/retailers-by-country.md:234 | Japan retailers: pages show domestic delivery or no overseas mention | https://www.dospara.co.jp/ ; https://www.pc-koubou.jp/ | 2026-11-08 | confirmed | Dospara and PC Koubou show no overseas shipping statement. Sofmap not readable. |
| A6b-53 | references/retailers-by-country.md:235 | StaticICE lists sister sites for NZ, UK and US | https://www.staticice.com.au/ | 2026-11-08 | confirmed | Same wording as A6b-20. |
| A6b-54 | references/retailers-by-country.md:183 | Japanese retailer pages show domestic delivery only or nothing on overseas shipping | https://www.dospara.co.jp/ ; https://www.pc-koubou.jp/ | 2026-11-08 | confirmed | Same result as A6b-52. |
| A6b-55 | references/power-supplies-connectors.md:136 | Ryzen 7 9800X3D: TDP 120 W, PPT 162 W | https://www.amd.com/en/products/processors/technologies/3d-v-cache.html | 2026-11-08 | blocked | Retry on a different AMD page (3D V-Cache technology page). Timeout after 60 s. No value confirmed or changed. |
| A6b-56 | not located in repo (grep for 9950X PPT/TDP found no stated value) | Ryzen 9 9950X: PPT / default TDP | https://www.amd.com/en/products/processors/desktops/ryzen/9000-series.html | 2026-11-08 | blocked | Retry on the 9000-series overview page. Timeout after 60 s. No value confirmed or changed. |
| A6b-57 | references/sockets-chipsets.md:163 | AMD statement: AM5 support through 2029 | https://www.amd.com/en/newsroom.html | 2026-11-08 | blocked | Retry on AMD newsroom. HTTP 403. No value confirmed or changed. |
| A6b-58 | references/international-buying.md:205 | ATO: GST on low-value imported goods | https://www.ato.gov.au/businesses-and-organisations/international-tax-for-business/gst-for-non-resident-businesses | 2026-11-08 | blocked | Retry on the parent ATO page (not the failed page). HTTP 403. |
| A6b-59 | references/international-buying.md:206 | ABF: duty and GST rule | https://www.abf.gov.au/importing-exporting-and-manufacturing/importing/how-to-import | 2026-11-08 | blocked | Retry on the parent ABF page. HTTP 403. |
| A6b-60 | references/international-buying.md:87 | Royal Mail GBP 8 / Parcelforce GBP 12 customs handling fee | https://www.royalmail.com/receiving-mail | 2026-11-08 | blocked | Retry on the parent Royal Mail page. HTTP 403. Figure still from excerpt. |
| A6b-61 | references/international-buying.md:89 | UPS brokerage fee (UK or FR) | https://www.ups.com/gb/en/support/shipping-support.page | 2026-11-08 | blocked | Retry on a UPS UK support page. "Access Denied". No figure confirmed. |
| A6b-62 | references/international-buying.md:89 | FedEx customs clearance fee (UK or FR) | https://www.fedex.com/en-gb/shipping/customs.html | 2026-11-08 | blocked | Retry on FedEx UK customs page. Access denied. No figure confirmed. |
| A6b-63 | references/form-factors-cases.md:73 | Lian Li A4-H2O X4: SFX / SFX-L only, 322 mm | https://lian-li.com/ | 2026-11-08 | blocked | Retry on lian-li.com homepage. Readable, but the A4-H2O is not listed. Spec not confirmed. |
| A6b-64 | references/form-factors-cases.md:74 | SSUPD Meshroom S dimensions and clearances | https://ssupd.co/products/cases-meshroom-s-v1 | 2026-11-08 | blocked | Retry on the V1 product page. HTTP 429 (Retry-After 60). |

## Counts per result (claim table, 64 rows)

- confirmed: 16
- changed: 2
- could-not-verify: 5
- blocked: 13
- not-checked: 28
- total: 64

## Part 2 outcome (retry on a different official page)

| Item | URL tried | Result |
|---|---|---|
| AMD Ryzen 7 9800X3D PPT / TDP | https://www.amd.com/en/products/processors/technologies/3d-v-cache.html | blocked (timeout) |
| AMD Ryzen 9 9950X PPT / TDP | https://www.amd.com/en/products/processors/desktops/ryzen/9000-series.html | blocked (timeout) |
| AMD "AM5 through 2029" | https://www.amd.com/en/newsroom.html | blocked (HTTP 403) |
| ATO low-value GST | https://www.ato.gov.au/businesses-and-organisations/international-tax-for-business/gst-for-non-resident-businesses | blocked (HTTP 403) |
| ABF duty and GST | https://www.abf.gov.au/importing-exporting-and-manufacturing/importing/how-to-import | blocked (HTTP 403) |
| Royal Mail handling fee | https://www.royalmail.com/receiving-mail | blocked (HTTP 403) |
| UPS brokerage (UK) | https://www.ups.com/gb/en/support/shipping-support.page | blocked (Access Denied) |
| FedEx clearance (UK) | https://www.fedex.com/en-gb/shipping/customs.html | blocked (access denied) |
| Lian Li A4-H2O X4 spec | https://lian-li.com/ | blocked (product not on homepage) |
| SSUPD Meshroom S spec | https://ssupd.co/products/cases-meshroom-s-v1 | blocked (HTTP 429) |

No value was confirmed or changed in Part 2. A1, A2 and A4 must not use any new value from this audit.

## Not checked

- **Prior blocked, not retried (brief rule 4):** Newegg (US), Memory Express, PC Case Gear, B&H Photo, Micro Center, eBay US, Tsukumo, Ark, Yodobashi, Bic Camera, Amazon.co.jp, Yahoo! Auctions, Yahoo! Shopping API docs. Their 2026-11-07 status stands. Rows: A6b-01, A6b-05, A6b-06, A6b-08, A6b-15, A6b-22, A6b-35 to A6b-38, A6b-41, A6b-43, A6b-44.
- **Newegg Refreshed (A6b-02):** shares the Newegg domain, no page fetched, not retried.
- **Not sampled:** Best Buy API, Amazon US, Amazon.ca, Kijiji, Reddit, Facebook Marketplace, Amazon AU, Gumtree AU, Kakaku merchant API, PC Koubou warranty, Mercari, China brand store rows (Peerless Assassin, Kingbank, Asgard, Montech, Fanxiang, SAMA, MSI, ASUS CN), Lexar, JD Worldwide.
- **Part 2 location:** no stated value for the 9950X PPT or TDP was found in the repository by grep, so A6b-56 has no file:line.
- **Cross-border:** Montech shipping not checked (no fetch).
- **Rate-limited rows from 2026-11-07 that were not reattempted:** none in this sample except those listed above.

## Confidence

- Solid: Canada Computers, Back Market (type and warranty wording), Dospara, PC Koubou, Thermalright (no marketplace links), StaticICE (199 stores).
- Plausible: Umart (own shop, no product prices read), Dell Outlet (listing not read).
- To verify: all Royal Mail, ATO, ABF, UPS, FedEx and AMD values. Each is still open because the official page was blocked on 2026-11-08.
