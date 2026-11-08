# International buying: landed price, tax, duty, fees, warranty

Last checked: 2026-11-07. Values change: verify online before concluding.

Use this file to turn a price shown abroad into a LANDED price in the buyer's country, and to judge whether the warranty is usable there. All rates below are research values dated 2026-11-07. Treat every row as a starting point, not a final answer. Confidence labels: high / medium / low. "Sec." = secondary source (law firm, logistics blog, press) used only because no official page could be read.

## Volatile items (re-check before concluding)

Before giving a final landed price, re-check each item below that touches the buyer's destination. Use web search or web fetch on the official page listed in "Where to look up rates". If you cannot re-check, say so and label the result "indicative".

| Item | Status on 2026-11-07 | Deadline / pending change | Confidence |
|---|---|---|---|
| US Section 301 exclusions (178 lines, HTS 9903.88.69/.70) | Extended through 11:59 p.m. eastern time on 2027-01-09, effective 2026-11-10, by a USTR notice listing dated 2026-11-06 (https://ustr.gov/trade-topics/enforcement/section-301-investigations/section-301-china-technology-transfer/china-section-301-tariff-actions-and-exclusion-process/reinstatement-certain-exclusions-previously-extended, read 2026-11-08). The previous operative date was 2026-11-09 11:59 p.m. EDT [13] (press wording: "November 10"). Federal Register citation of the new notice not obtained. | Re-check by: 2027-01-05. Whether 8473.30 GPU and motherboard lines (8473.30.1180, .5100) are in the exclusions: unverified. | medium (deadline), low (scope) |
| US de minimis ($800) | Suspended for merchandise arriving via all modes other than the international postal network (CBP rule dated 2026-06-24) [11]. The postal route is not covered by this rule. | Statute ends de minimis 2027-07-01. | high |
| US "forced labor" Section 301 tariffs (10% or 12.5% by country) | The 10% and 12.5% tiers are confirmed by a USTR fact sheet (https://ustr.gov/about/policy-offices/press-office/fact-sheets/2026/july/fact-sheet-ustr-section-301-action-response-failure-60-economies-ban-imports-produced-forced-labor, read 2026-11-08). China's tier, the effective date and the scope for PC parts remain unverified (secondary sources only [14]). | Excess-capacity investigation still open. | tiers: high; China tier, date, PC-part scope: low |
| UK GBP 135 customs-duty relief | Still in force on the pages read [7]. HMRC says it will be removed, no date on the page. | Sec. sources say 2028-10 (unconfirmed). | removal: medium; date: low |
| EU EUR 3 flat duty per item category (consignments up to EUR 150) | In force since 2026-07-01 [1]. | Until 2028-07-01 or until the EU Customs Data Hub makes normal duties applicable. | high |
| EU Union handling fee EUR 2 per item (small parcels) | Applies from 2026-11-01 [1][2]. Per item, irrespective of the item's value, for distance sales; part of the VAT taxable amount (Commission customs guidance 3.2 and 9.2, https://taxation-customs.ec.europa.eu/document/download/053e5b4e-f0be-4f20-9a23-3e3b659a6676_en?filename=Customs+Guidance+on+EUR+3+customs+duty.pdf, read 2026-11-08). | Delegated-act number not confirmed. | medium-high |
| Japan JPY 10,000 exemption | In force [20]. | Planned end 2028-04-01; passage into law unconfirmed [21]. | current: high; reform: low-medium |
| Carrier handling fees (DHL, Royal Mail, Canada Post) | Figures come from search excerpts or resellers. | May be outdated. | low-medium |
| Australia GST/duty, Canada duty on PC parts | Official pages blocked or not reached. | n/a | low |

## Landed-price formula

Decide first WHO collects the tax. Then compute in this order.

1. **Who collects?**
   - Seller or platform collects at checkout: EU IOSS (seller IOSS-registered, consignment up to EUR 150); UK point-of-sale VAT (consignment up to GBP 135); Australia GST at checkout (goods up to AUD 1,000 from large overseas sellers). Then import VAT at the door is 0 and the carrier fee is usually low or zero.
   - Border collects (seller not registered, or above the threshold): the carrier or post advances duty and VAT, then bills the buyer with a fee.
   - Intra-EU purchase: no customs. See "Intra-EU purchases".
   - US destination: no VAT. See the US row.
2. **Customs value (CV)** = goods price + shipping + insurance. This is a CIF-type basis (EU, UK, JP, AU, CA). The US uses an FOB-type basis, which excludes international freight.
3. **Duty** = CV x duty rate for the HS code. Add extra tariffs by origin (for example Section 301 on China-origin goods to the US). For EU consignments up to EUR 150, add the flat EUR 3 per item category.
4. **Handling fee**: EU Union handling fee EUR 2 per item, irrespective of value for distance sales; it is part of the VAT taxable amount (Commission guidance 3.2 and 9.2, read 2026-11-08).
5. **Import VAT** = (CV + duty + handling fee + other taxes or charges due on import) x destination VAT rate. VAT applies to the duty-inclusive value.
6. **Carrier / postal fee**: brokerage, disbursement or handling fee, charged only when the carrier or post clears the parcel. VAT on this fee applies in most countries (not added in the examples).
7. **Card FX fee** = card FX % x amount charged in foreign currency. Zero if the seller charges in the buyer's currency. Typical level is an assumption (see Carrier and payment fees).
8. **Landed** = goods + shipping + duty + handling fee + import VAT + carrier fee + FX fee. Convert at a dated mid-market rate and write the rate date.

Fallback: if a rate, threshold or fee cannot be confirmed, do not guess. Give the shown price plus shipping, write `excluding fees` in the Landed column, and list which items are missing. If you must estimate, label it "indicative" and state each assumption.

## Rules by destination zone

Status date for every row: 2026-11-07. Source numbers refer to "## Sources".

| Zone | Tax rate and collection | De minimis tax | De minimis duty | Duty on PC parts | Extra tariffs, China-origin | Source | Confidence |
|---|---|---|---|---|---|---|---|
| EU, general (non-EU seller) | Destination member-state VAT. Checkout via IOSS (consignments up to EUR 150, seller IOSS-registered) or at the border by carrier/post. | None for VAT. | EUR 150 duty exemption abolished 2026-07-01. Replaced by flat EUR 3 per item category on consignments up to EUR 150, until 2028-07-01 or until the EU Customs Data Hub makes normal duties applicable. Above EUR 150: normal duty. Union handling fee EUR 2 per item from 2026-11-01. | EU TARIC NOT read. ITA lines (8471, 8473.30, 8542, 8523, 8528.52) are 0% in the UK Global Tariff; expect 0% in the EU, unconfirmed. | No general EU tariff on Chinese PCs or parts found. Anti-dumping measures are product-specific, not checked for PC parts. | [1][2] | EUR 3 and end of exemption: high. EUR 2 fee: medium. EU PC-part duty 0%: low (inferred). |
| EU standard VAT: FR, DE, ES, IT, BE, NL, LU | FR 20%, DE 19%, ES 21%, IT 22%, BE 21%, NL 21%, LU 17% (one sec. source says LU 16%, not confirmed). | n/a | n/a | n/a | n/a | [3] (no table, points to TEDB), [4] sec. | medium. FR, DE, BE, LU: majority of sec. sources. ES, IT, NL: not confirmed on a labelled source. Verify in TEDB. |
| UK | VAT 20% (rate not re-fetched). Consignments up to GBP 135 to Great Britain: seller charges UK VAT at point of sale. Above GBP 135: import VAT at the border. Northern Ireland rules differ. GBP 15 import-VAT relief removed. | None. | GBP 135 customs-duty relief still in force; removal announced (HMRC paper published 2026-07-13, updated 2026-10-28) with no date on the page. | UK Global Tariff third-country duty 0.00% for 8471.80.00.00 and 8473.30.20.00 (checked 2026-11-07). 8504.40, 8523.51, 8528.52, 8542 not queried. | None found for PC parts. Trade-remedy measures not checked. | [6][7][8] | VAT point-of-sale rule: high. 0% on 8471.80 and 8473.30: high. 20% rate: medium. Removal date: low. |
| US | No federal VAT. State sales/use tax (seller or buyer). | n/a | De minimis ($800) suspended for merchandise arriving via all modes other than the international postal network (CBP rule 2026-06-24). The postal route is not covered by this rule. | HTS general rate Free for 8471.80.xx, 8473.30.xx, 8504.40.60/.95, 8528.52, 8523.51 (USITC, checked 2026-11-07). Column 2 rates (35%, 80% for 8523.51) apply only to Column 2 countries. 8542 not queried. | IEEPA tariffs ruled unlawful by SCOTUS 2026-02-20; CBP stopped collecting 2026-02-24. Section 122 10% surcharge ran 2026-02-24 to 2026-07-24 and expired. Section 301 (2018 action) remains: the 178 exclusions were extended through 2027-01-09 (USTR notice 2026-11-06, effective 2026-11-10; previous operative date 2026-11-09); whether 8473.30 GPU and motherboard lines are in scope: unverified. 50% Section 301 on Chinese semiconductors (8541/8542), reported unchanged to 2027-06. Section 232: 25% on a narrow set of advanced AI accelerators (2026-01-14); consumer GPUs not confirmed in scope. Forced-labor 10%/12.5%: tiers confirmed by USTR, China's tier unverified (see Volatile items). | [9][10][11][12][13][14] | De minimis and IEEPA end: high. HTS Free: high. Forced-labor tariffs: low-medium. GPU/motherboard exclusion scope: low. |
| Canada | GST 5% federal plus PST or HST by province (rates not re-fetched; CBSA confirms they apply). Collected at the border by courier or Canada Post, or at checkout by some platforms. | Mailed items up to CAD 20: no duty or tax. | CAD 20 (post). Courier Low Value Shipment program covers goods up to CAD 3,300; CBSA has a moratorium on new participants. | CBSA 2026 tariff rates for 8471/8473.30 not reached. Canada is an ITA member (expected Free): NOT verified. | Surtaxes on China-origin goods found only for steel and aluminium (EV surtax reportedly repealed 2026-03-01). None found on computers or components. | [15][16][17] | CAD 20 rule: high. CLVS: medium-high. Duty on PC parts: low. China surtax scope: medium. |
| Australia | GST 10% (secondary sources; ATO page blocked). Overseas sellers/platforms collect GST at checkout for goods up to AUD 1,000 (large sellers above AUD 75,000 turnover); above AUD 1,000, GST at the border. | AUD 1,000 (GST at point of sale). | AUD 1,000 informal-clearance notion; ABF page blocked, not confirmed. | 8471 reported Free (ITA; third-party sites). Official Working Tariff not read. | None found. | [18][19] | GST model: medium. Duty: low. |
| Japan | Consumption tax 10% (not re-fetched). Collected at the border by Japan Post or couriers. | JPY 10,000 total customs value exempt from duty and consumption tax (Customs FAQ 1006, undated; per declaration, split parcels combined). | JPY 10,000 (same rule). | 8471 reported Free (third-party listing). Official schedule and simplified rate table for personal imports NOT verified. | None found. | [20][21] | Current rule: high. 2028 reform: low-medium. Duty: low. |

### Goods shipped from China, by destination

| Destination | What to apply | Confidence |
|---|---|---|
| EU | Up to EUR 150: EUR 3 flat duty per item category + EUR 2 handling fee per item + VAT (at checkout if the platform is IOSS-registered). Above EUR 150 (distance sales): EUR 2 handling fee per item still applies; normal duty (expected 0% on ITA lines) + import VAT. | medium |
| UK | Up to GBP 135: UK VAT at checkout, no duty (relief in force), no clearance fee when VAT is prepaid. Above GBP 135: import VAT + duty + carrier fee. | medium-high |
| US | No de minimis. Section 301 by HTS line (see US row). Post-IEEPA replacements must be re-checked per HTS line on CBP/USTR. | low-medium |
| Canada | No China-specific surtax found for PC parts. CAD 20 postal exemption, otherwise duty + GST. | low-medium |
| Australia | GST at checkout up to AUD 1,000. No China-specific tariff found. | low-medium |
| Japan | JPY 10,000 exemption until the planned 2028 change; otherwise duty (expected Free) + 10% consumption tax. | medium |

### AliExpress, Choice and IOSS: source conflict

The retailer research (r1, secondary blog sources [48]) disagrees across sources on who collects duty for AliExpress Choice and on the 2026-07-01 EU change. The duty research (r2, built on the Commission page [1]) wins: the EUR 150 exemption is gone and EUR 3 per item category applies. Whether AliExpress or Choice is IOSS-registered is NOT verified. Check the checkout page: if it shows VAT collected at checkout, treat import VAT as prepaid; if not, add border VAT and carrier fee. Say which case you assumed.

## Intra-EU purchases

- No customs between member states. Landed = price incl. VAT + shipping.
- Distance-sales rule [5]: while the seller's EU-wide distance sales to consumers stay under EUR 10,000 per year, the seller charges its own country's VAT. Above that, the VAT of the buyer's country applies. Confidence: high on EUR 10,000 and the destination-VAT rule.
- OSS (one-stop-shop) detail: the page only says sellers can register in one EU country. Medium.
- A shown price excl. VAT must be converted: read the page for which VAT it shows; do not assume. If unclear, mark `unknown`.

## Carrier and payment fees

Use only these figures. Date checked 2026-11-07.

| Item | Fee / rule | Source | Confidence |
|---|---|---|---|
| EU Union handling fee | EUR 2 per item, irrespective of value for distance sales, from 2026-11-01; part of the VAT taxable amount (Commission guidance 3.2, 9.2, read 2026-11-08). Applied per declaration line irrespective of quantity. | [1][2] | medium-high |
| DHL Express Germany | "Duty Tax Processing Service": 2% of fiscal charges, minimum EUR 12.50 per shipment (not applied when charges are exempt). Document dated 2024-12-26; figure from a search excerpt, PDF unreadable. | [22] | low-medium |
| DHL Express France | Not verified on the official page (2026-11-08): read the carrier's fee page at purchase time. A reseller page gave EUR 14.60 or 2.55% of the advanced amount; the official DHL France page states no amount. | [23] sec. | low |
| Royal Mail / Parcelforce | Customs handling fee GBP 8 (Royal Mail) / GBP 12 (Parcelforce) when duty or import VAT is due; GBP 25 for a full declaration over GBP 900. Not verified on the official page (2026-11-08, HTTP 403): read the carrier's fee page at purchase time. Figures from a search excerpt. | [24] | low-medium |
| Canada Post / couriers | A handling fee exists on dutiable or taxable mail (CBSA confirms). CAD 9.95 is a secondary figure; courier brokerage about CAD 15-35 per sec. sources. | [15][16] sec. | low |
| FedEx, UPS | Official brokerage pages blocked or unread. No figure. | [25] | blocked |
| France national small-parcel tax | Reported in force 2026-03-01 then suspended in favour of the EU duty (sec.). Official page blocked. | [26] sec. | low |
| Card FX | EU Regulation 2019/518 requires disclosure of currency-conversion charges as a % mark-up over the ECB reference rate. No cap, no ban. A typical bank FX fee of 1.5-3% has NO official source: treat it as an assumption and write it as one. | [27] | regulation: medium; fee level: low |
| Dynamic currency conversion (DCC) | The regulation requires DCC disclosure. Practical rule: pay in the seller's or local currency and decline "pay in your currency". | [27] | medium |

## Where to look up rates

Cite the source and date you used. Do not hard-code rates from this file when a live lookup is possible.

| Category | Source | URL (data) | Access / notes |
|---|---|---|---|
| FX, euro | ECB euro reference rates [35] | https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html | No key. About 16:00 CET on working days. Informational only. |
| FX | Frankfurter [36] | https://frankfurter.dev/docs/ | No key. Daily. Not for live trading. |
| FX | open.er-api.com [37] | https://www.exchangerate-api.com/docs/free | No key. Once daily. Attribution required. |
| FX | Bank of Canada Valet [39], US Fed H.10 [40], Bank of England IADB [41] | https://www.bankofcanada.ca/valet-api-how-to/ ; https://www.federalreserve.gov/RELEASES/h10/about.htm ; https://www.bankofengland.co.uk/boeapps/database/help.asp | Daily, no key. BoE says its rates are not official reference rates. |
| FX | exchangerate.host [38] | https://exchangerate.host/ | Key required; terms unread. |
| FX | RBA, Bank of Japan | not retrieved (BoJ API launched 2026-02-18, low-medium) | Gap. |
| Tariff UK | UK Trade Tariff [42] | https://docs.trade-tariff.service.gov.uk/ | REST; docs mention OAuth credentials, anonymous access unclear. Data updated daily. |
| Tariff EU | TARIC [43] | https://taxation-customs.ec.europa.eu/customs/calculation-customs-duties/customs-tariff/eu-customs-tariff-taric_en | Web consultation, updated daily. No official REST API confirmed. |
| VAT EU | TEDB [44] | https://taxation-customs.ec.europa.eu/system/files/2021-06/soap_webservice_documentation.pdf | SOAP service. Not a legal reference. |
| Tariff US | USITC HTS [45][46] | https://hts.usitc.gov/ | REST at hts.usitc.gov/reststop. Parameter docs not read. |
| Tariff Canada | CBSA [47] | https://www.cbsa-asfc.gc.ca/trade-commerce/tariff-tarif/menu-eng.html | Downloadable files. No API found. |
| Tariff Australia | none found | n/a | Gap. |

Converted amounts are mid-market or reference rates. Card networks add their own rate and fees, so label converted prices "indicative" and write the rate date. These are tool categories (web fetch, official lookup); see `CONNECTORS.md`.

## Warranty across borders

Two layers: the legal guarantee (owed by the seller under consumer law) and the manufacturer warranty (owed by the brand, usually regional).

| Topic | Rule | Source | Confidence |
|---|---|---|---|
| EU legal guarantee | Directive (EU) 2019/771: the seller is liable for non-conformity existing at delivery and appearing within 2 years (Art. 10). Presumed existing at delivery if it appears within 1 year (Art. 11; member states may extend to 2). Consumer chooses repair or replacement, then price reduction or termination (Art. 13). Applies to sellers directing sales to the EU. Against a non-EU seller with no EU presence, enforcement is practically harder (my inference). | [28] | text: high; non-EU enforcement: medium |
| UK | Consumer Rights Act 2015 s.9: goods must be of satisfactory quality. Seller liability, not the manufacturer. Remedy details (s.19, s.22) not verified. | [29] | s.9: high; remedies: medium |
| US | No federal 2-year guarantee. Implied warranty of merchantability under state law (UCC); manufacturer warranty is express and often limited to the US or seller channel. Not verified on an official page. | none read | low |

| Brand | What research found | Status | Source | Confidence |
|---|---|---|---|---|
| ASUS | GPU pages say the period "may differ regionally, check with your purchase site". International warranty PDF (404 on fetch) not confirmed to cover graphics cards or motherboards. Forum reports: no international GPU warranty. | Unconfirmed, regional likely | [30] | low-medium |
| MSI | Terms may differ by region; cross-region online purchases follow the warranty of the country where the retailer processes the sale. Official page blocked (403); from a search excerpt of an MSI document. | Regional by retailer country | [31] | medium |
| Gigabyte / AORUS | Term and period vary by product and region; ask the shop of purchase or the local office. Official page blocked (403); search excerpt. | Regional | [32] | medium |
| Sapphire | Claims via the place of purchase; varies by country; separate RMA desks by market (USA, Canada). Current official page not found. | Regional, unconfirmed | [33] sec. | low |
| Corsair | Page redirected and returned 403. Worldwide vs regional not confirmed. | Blocked | [34] | blocked |

Reading rule: for GPUs and motherboards assume a regional warranty tied to the country of purchase unless the maker's page for the exact model says otherwise. In the EU, the seller's 2-year legal guarantee is the reliable recourse, and mostly when the seller is in the EU. When writing the "Warranty from buyer country" column, use `regional (unconfirmed)`, `seller-only (EU legal guarantee)` or `blocked page, ask user`. If a brand page is blocked, record it as blocked and ask the user for a screenshot or pasted text. Do not use mirrors or caches.

## Worked examples (illustrative)

Not current prices and not quotes. Assumptions: 1 USD = 0.90 EUR and 1 USD = 0.75 GBP; card FX fee 2% (assumption, no official source); carrier fees from the table above at their stated confidence. Re-run with live values.

### Example 1: 300 USD GPU, US seller to France, DHL

| Step | Calculation | Amount |
|---|---|---|
| Goods | | 300.00 USD |
| Shipping + insurance (assumed) | | 40.00 USD |
| Customs value | 340 USD x 0.90 | EUR 306.00 |
| EUR 3 duty | CV above EUR 150: not applicable (scope per [1]) | EUR 0.00 |
| EUR 2 Union handling fee | applies per item irrespective of value (distance sales), part of the VAT base | EUR 2.00 |
| Duty | 0% (ITA; TARIC not verified, UK rate used as proxy, low confidence) | EUR 0.00 |
| Import VAT, FR 20% [4] | (306.00 + 0.00 + 2.00) x 20% = 308.00 x 20% | EUR 61.60 |
| Carrier fee (DHL France) | not verified on the official page (2026-11-08): excluded | not included |
| Card FX fee (assumption) | 2% x 306.00 | EUR 6.12 |
| **Landed (approx., excluding carrier fee)** | 306.00 + 2.00 + 61.60 + 6.12 | **about EUR 375.72** |

The carrier fee, if charged, comes on top (read the carrier's fee page at purchase time); VAT on it is not added. Any US tariff is not levied by the EU. A French legal guarantee against a US seller is hard to enforce; the manufacturer warranty may be US-only.

### Example 2: 60 USD cooler, China seller to UK

| Step | Calculation | Amount |
|---|---|---|
| Goods | 60 USD x 0.75 | GBP 45.00 |
| Shipping (assumed, paid at checkout) | | GBP 8.00 |
| GBP 135 test | goods only | GBP 45.00 (below 135) |
| Duty | GBP 135 relief in force [7] | GBP 0.00 |
| UK VAT 20%, charged at checkout [8] | (45.00 + 8.00) x 20% | GBP 10.60 |
| Border clearance fee | none if VAT collected at point of sale | GBP 0.00 |
| Card FX fee (assumption) | 2% x 63.60 | GBP 1.27 |
| **Landed (approx.)** | 53.00 + 10.60 + 1.27 | **about GBP 64.87** |

If the seller is not VAT-registered or the order exceeds GBP 135: add import VAT at the border and a GBP 8 (Royal Mail) or GBP 12 (Parcelforce) handling fee [24]. UK duty on a cooler is not verified (8473.30 was verified at 0%).

## Not verified

1. EU TARIC duty for 8471, 8473.30, 8542, 8523, 8504.40, 8528.52 not read. UK Global Tariff used as a proxy for two codes only; UK codes 8504.40, 8523.51, 8528.52, 8542 not queried.
2. US Section 301: whether GPUs and motherboards (8473.30.1180, .5100) are inside the 178 exclusions, and what applies after 2027-01-09 (exclusions extended by USTR notice 2026-11-06; Federal Register citation not obtained). 8542 HTS rate, postal-route rules and CSMS bulletin numbers not obtained. The Federal Register site returned an access-request page; the same documents were read on govinfo.gov.
3. US forced-labor Section 301 tariffs: the 10% and 12.5% tiers are confirmed by a USTR fact sheet; China's tier, the effective date and the PC-part scope are unverified. Section 232 scope: secondary sources only.
4. Duty on PC parts for EU, Canada and Australia not confirmed on official pages (Canada and Australia official pages blocked or not reached). Japan simplified duty-rate table not read.
5. VAT/GST rates for UK 20%, Canada 5%, Australia 10%, Japan 10%, and ES/IT/NL (EU) not confirmed on a primary page. The Commission VAT page has no table. LU 16% vs 17% unresolved.
6. Carrier fees: DHL France, UPS, FedEx official pages not obtained; Royal Mail page blocked; DHL Germany figure from an excerpt; the economie.gouv.fr page (2026-11-02) blocked (handling-fee scope now taken from the Commission guidance, 2026-11-08).
7. EUR 3 duty applies up to EUR 150 (my reading); the EUR 2 fee applies irrespective of value for distance sales (Commission guidance 3.2).
8. Card FX fee level: no official figure; 2% is an assumption.
9. Manufacturer warranty: MSI, Gigabyte, Corsair pages blocked; ASUS GPU international coverage unconfirmed; Sapphire policy page not found. US implied warranty and CRA s.19/22 not read.
10. Intra-EU: OSS detail and the IOSS EUR 150 rule not read on an official page.
11. AliExpress Choice and IOSS: conflicting secondary claims (see source-conflict note); IOSS registration not verified.
12. Japan 2028 reform and UK GBP 135 removal date: not confirmed.
13. RBA and Australian tariff data access: not found.

## Sources

1. EU Commission, customs reform (EUR 3 duty, end of EUR 150 exemption, handling fee) — https://taxation-customs.ec.europa.eu/customs/eu-customs-reform_en — 2026-11-07.
2. Press on EU handling fee and Council 2026-09-03 (secondary) — https://www.eunews.it/en/2026/09/03/eu-council-gives-the-green-light-to-customs-reform-from-1-november-a-handling-fee-for-small-parcels/ ; https://www.taxually.com/blog/eu-handling-fee-3-euro-customs-duty
3. EU Commission, VAT rates framework — https://taxation-customs.ec.europa.eu/taxation/vat/vat-rates_en — no table.
4. Secondary VAT tables — https://taxfoundation.org/data/all/eu/value-added-tax-vat-rates-europe/ ; https://www.taxenlight.com/en/eu-vat-rates/
5. Your Europe, cross-border VAT (EUR 10,000) — https://europa.eu/youreurope/business/taxation/vat/cross-border-vat/index_en.htm
6. UK Trade Tariff API — https://www.trade-tariff.service.gov.uk/api/v2/commodities/8471800000 and .../8473302000
7. HMRC, Reforming customs rules for low value imports (published 2026-07-13, updated 2026-10-28) — https://www.gov.uk/government/publications/reforming-customs-rules-for-low-value-imports
8. GOV.UK, VAT and overseas goods sold directly to customers — https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk
9. USITC HTS REST search — https://hts.usitc.gov/reststop/search?keyword=8471.80 (also 8473.30, 8504.40, 8528.52, 8523.51, 9903.88.03)
10. GHY International summary of Section 122, IEEPA, de minimis (secondary, cites CBP) — https://www.ghy.com/?p=25869
11. CBP interim final rule CBP Dec. 26-12 (2026-06-24) — https://www.govinfo.gov/content/pkg/FR-2026-06-24/html/2026-12670.htm
12. STR Trade, Section 122 tariffs (search result only) — https://www.strtrade.com/trade-news-resources/tariff-actions-resources/section-122-tariffs
13. Federal Register 2025-12-01, USTR Section 301 exclusions extended to 2026-11-09 (superseded by the USTR notice of 2026-11-06, to 2027-01-09) — https://www.govinfo.gov/content/pkg/FR-2025-12-01/html/2025-21671.htm
14. Section 232 AI chips and forced-labor tariffs (secondary) — https://www.whitecase.com/insight-alert/president-trump-orders-narrowly-targeted-25-section-232-tariff-certain-advanced ; https://www.kroll.com/en/publications/a-tale-of-tariff-substitution (search excerpt only)
15. CBSA, mail and courier (CAD 20) — https://www.cbsa-asfc.gc.ca/import/courier/menu-eng.html
16. CBSA, Courier Low Value Shipment program (search excerpt) — https://www.cbsa-asfc.gc.ca/import/courier/lvs-efv/comm-eng.html
17. CBSA 2026 Customs Tariff index (rates not reached) — https://www.cbsa-asfc.gc.ca/trade-commerce/tariff-tarif/2026/html/tblmod-1-eng.html
18. ATO, GST on low value imported goods (403 blocked) — https://www.ato.gov.au/businesses-and-organisations/international-tax-for-business/gst-for-non-resident-businesses/gst-on-low-value-imported-goods
19. ABF, duty and GST (403 blocked) — https://www.abf.gov.au/importing-exporting-and-manufacturing/importing/how-to-import/duty-and-gst
20. Japan Customs FAQ 1006 (JPY 10,000, undated) — https://www.customs.go.jp/english/c-answer_e/imtsukan/1006_e.htm
21. Japan 2026 tax reform (secondary) — https://www.pwc.com/jp/en/taxnews/pdf/jtu-20260114-en.pdf ; https://www.vatupdate.com/2026/01/13/japan-2026-tax-reform-key-consumption-tax-changes-and-timeline-for-low-value-imports
22. DHL Express Germany clearance terms (PDF 2024-12-26, text unreadable, excerpt) — https://www.dhl.de/content/dam/images/Express/downloads/zollinformation/zollinformationen-und-dokumente/dhl-express-auftragsbedingungen-gebuehren-zollabfertigung-en.pdf
23. Reseller page quoting DHL France fee (secondary) — https://parceldetect.com/faq/customs-disbursement-fees
24. Royal Mail fee page (403 blocked, excerpt) — https://www.royalmail.com/receiving-mail/pay-a-fee
25. FedEx APAC surcharge PDF (not read) — https://www.fedex.com/content/dam/fedex/apac-asia-pacific/downloads/fedex-customs-clearance-surcharge-20july2026.pdf ; UPS import page returned "Access Denied".
26. Lexisveille (secondary) — https://lexisveille.fr/petits-colis-importes-entree-en-vigueur-au-1er-juillet-du-droit-de-douane-europeen-et-suspension-de ; official page blocked: https://www.economie.gouv.fr/particuliers/mes-droits-conso/bien-consommer/taxes-sur-les-petits-colis-comment-ca-marche
27. Regulation (EU) 2019/518 (retained text, excerpts) — https://www.legislation.gov.uk/eur/2019/518/data.html
28. Directive (EU) 2019/771 — https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L0771
29. Consumer Rights Act 2015 s.9 — https://www.legislation.gov.uk/ukpga/2015/15/section/9
30. ASUS warranty pages — https://www.asus.com/au/support/article/1100/ ; PDF 404 on fetch.
31. MSI warranty (403 blocked; excerpt from an MSI document) — https://www.msi.com/page/warranty
32. Gigabyte warranty (403 blocked; excerpt) — https://www.gigabyte.com/eu/Support/Warranty/Graphics-Card
33. Sapphire (secondary excerpts) — https://www.sapphiretech.com/en/contact-us
34. Corsair warranty (403 blocked) — https://help.corsair.com/hc/en-us/articles/360033067832
35. ECB euro reference rates — https://www.ecb.europa.eu/stats/policy_and_exchange_rates/euro_reference_exchange_rates/html/index.en.html
36. Frankfurter — https://frankfurter.dev/docs/
37. open.er-api.com docs — https://www.exchangerate-api.com/docs/free
38. exchangerate.host — https://exchangerate.host/
39. Bank of Canada Valet — https://www.bankofcanada.ca/valet-api-how-to/ (via search)
40. US Fed H.10 — https://www.federalreserve.gov/RELEASES/h10/about.htm (via search)
41. Bank of England IADB; Bank of Japan — https://www.bankofengland.co.uk/boeapps/database/help.asp ; https://www.boj.or.jp/en/statistics/outline/notice_2026/not260218a.htm (via search)
42. UK Trade Tariff API docs — https://docs.trade-tariff.service.gov.uk/
43. EU TARIC — https://taxation-customs.ec.europa.eu/customs/calculation-customs-duties/customs-tariff/eu-customs-tariff-taric_en (via search)
44. EU TEDB SOAP documentation — https://taxation-customs.ec.europa.eu/system/files/2021-06/soap_webservice_documentation.pdf (via search)
45. USITC HTS — https://hts.usitc.gov/
46. HTS REST API listing — https://catalog.data.gov/dataset/harmonized-tariff-schedule-of-the-united-states-2023 (via search)
47. CBSA tariff menu — https://www.cbsa-asfc.gc.ca/trade-commerce/tariff-tarif/menu-eng.html (via search)
48. AliExpress Choice and IOSS, secondary blogs from retailer research (conflicting) — https://yakkyofy.com/aliexpress-import-tax-what-to-do/ ; https://easproject.com/ioss-registration-1-july-3-euro-duty/
