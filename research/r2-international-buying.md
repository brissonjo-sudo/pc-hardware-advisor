# R2 International buying: taxes, duties, fees, warranty
Collected: 2026-11-07 · Model: sonnet

Conventions: every row carries "checked 2026-11-07". Confidence = high / medium / low. "Blocked" = official page refused automated access (403, CAPTCHA or access-request page); no bypass attempted. "Sec." = secondary source (law firm, logistics blog, news), used only when no official page could be read. Numbers in [brackets] refer to the Sources list.

## Landed-price formula

```
CV      = goods_price + shipping + insurance          (customs value, CIF-type basis: EU, UK, JP, AU, CA, US-ish; US uses FOB, i.e. excludes international freight)
DUTY    = CV x duty_rate                               (+ extra tariffs on origin, + EU flat EUR 3/item category if parcel <= EUR 150)
FEES_G  = handling fee (EU Union handling fee EUR 2 if parcel in scope) 
VAT_imp = (CV + DUTY + FEES_G_if_in_base) x vat_rate   (import VAT base normally = CV + duty + other taxes/charges due on import)
CARRIER = brokerage / disbursement / postal handling fee (+ VAT on that fee in most countries)
FX      = card_fx_pct x amount_charged_in_foreign_currency   (0 if paid in buyer's currency; avoid DCC)
LANDED  = goods_price + shipping + DUTY + FEES_G + VAT_imp + CARRIER + FX
```

Branching by who collects the tax (decide first):
1. **Tax collected at checkout by seller or platform** (EU IOSS for parcels <= EUR 150; UK point-of-sale VAT for consignments <= GBP 135; AU/GST for goods <= AUD 1,000 sold by large overseas sellers; JP planned from 2028): VAT_imp = 0 at the door and CARRIER is usually low or zero.
2. **Tax collected at the border** (above the thresholds, or seller not registered): carrier or post advances duty and VAT, then bills the buyer with a fee.
3. **Intra-EU purchase**: no customs. Seller charges VAT (own country below the EUR 10,000 EU-wide distance-selling threshold, destination-country VAT above it or if the seller opts in via OSS). Landed = price incl. VAT + shipping.
4. **US destination**: no VAT. Add duty (HTS general rate, usually Free for PC parts) + any Section 301/232 or other tariffs + customs entry/broker fee + state use tax if the seller did not collect sales tax.

## Rules by destination zone

| Zone | Tax rate & collection | De minimis tax | De minimis duty | Duty on PC parts | Extra tariffs China-origin | Status date | Source | Confidence |
|---|---|---|---|---|---|---|---|---|
| EU, general (non-EU seller) | VAT of the destination member state. Collected at checkout via IOSS (consignments <= EUR 150 when the seller is IOSS-registered) or at the border by carrier/post (otherwise). | None for VAT (VAT-exempt EUR 22 abolished 2021; not re-fetched here). | **EUR 150 duty exemption abolished 2026-07-01**; replaced by temporary flat **EUR 3 per item (per tariff sub-heading category) on consignments <= EUR 150**, from 2026-07-01 until 2028-07-01 or until the EU Customs Data Hub makes normal duties applicable. Above EUR 150: normal duty. **Union handling fee EUR 2 per item from 2026-11-01** on small parcels (see Carrier section). | ITA principle: 8471, 8473.30, 8542, 8523, 8528.52 are 0% in the UK Global Tariff (verified, see UK row). EU TARIC itself NOT read this session (not fetched). Expect 0% in EU too but confirm in TARIC per code. | No general extra EU tariff on Chinese PCs/parts found. Anti-dumping/anti-subsidy measures are product-specific (not checked for PC parts). | 2026-11-07 | [1] [2] [3] | EUR 3 duty and end of EUR 150 exemption: high (Commission page). EUR 2 fee from 2026-11-01: medium (Commission page via summary + press; delegated-act number not confirmed). EU PC-part duty 0%: low (inferred). |
| EU, standard VAT FR / DE / ES / IT / BE / NL / LU | FR 20%, DE 19%, ES 21%, IT 22%, BE 21%, NL 21%, LU 17% (one secondary source says LU 16%; not confirmed). | n/a | n/a | n/a | n/a | 2026-11-07 | [4] (Commission page gives no table; points to TEDB) [5] sec. | medium (FR, DE, BE, LU majority of sec. sources; ES, IT, NL not confirmed on a labelled source; verify in TEDB) |
| EU, intra-EU purchase | Seller's VAT (own country) while the seller's EU-wide distance sales to consumers stay under **EUR 10,000/year**; above it, VAT of the buyer's country (OSS one-stop-shop reporting). | n/a | No customs between member states. | n/a | n/a | 2026-11-07 | [6] | high on EUR 10,000 and destination VAT above it; medium on OSS detail (page only says sellers can register in one EU country) |
| UK | Standard VAT 20% (rate not re-fetched this session). Consignments <= GBP 135 to Great Britain: seller charges UK VAT at point of sale. Above GBP 135: import VAT at the border. Northern Ireland: import VAT rules differ. GBP 15 import-VAT relief removed. | None (VAT always due). | **GBP 135 customs-duty relief still in force as of the pages read.** HMRC policy paper (published 2026-07-13, updated 2026-10-28) says it will be removed; the page gives no effective date. Sec. sources say deadline moved to 2028-10 (unconfirmed). | UK Global Tariff third-country duty **0.00%** for 8471.80.00.00 and 8473.30.20.00 (Trade Tariff API, checked 2026-11-07). 8504.40, 8523.51, 8528.52, 8542 not queried. | None found for PC parts (UK has no blanket China surcharge; trade-remedy measures not checked). | 2026-11-07 | [7] [8] [9] | VAT point-of-sale rule: high. Duty 0% on 8471.80 and 8473.30: high. Date of removal of GBP 135 relief: low. 20% rate: medium. |
| US | No federal VAT/GST. State sales/use tax (seller or buyer). | n/a | **De minimis ($800) suspended for all countries and all modes.** Non-postal: CBP interim final rule dated 2026-06-24 (effective 2026-06-24). Postal: separate concurrent rule, text not read. Statute (OBBBA) ends de minimis 2027-07-01. | HTS general rate **Free** for 8471.80.xx, 8473.30.xx, 8504.40.60/.95, 8528.52, 8523.51 (USITC REST search, checked 2026-11-07). Column 2 rates 35% (80% for 8523.51) apply only to Column 2 countries. 8542 not queried. | IEEPA tariffs were ruled unlawful (SCOTUS, 2026-02-20, Learning Resources v. Trump) and CBP stopped collecting them 2026-02-24. Section 122 10% surcharge ran 2026-02-24 to 2026-07-24 and expired. Sec. report: replaced 2026-07-24 by Section 301 "forced labor" tariffs, 10% or 12.5% by country (12.5% reported for China) (not confirmed on an official page). **Section 301 (2018 action) remains**: 25% on 8473.30 lines (GPUs, motherboards, cases) is reported as excluded (exclusion expires **2026-11-09 11:59 pm EDT** unless extended; whether 8473.30.1180 and .5100 are among the 178 exclusions is NOT confirmed). 50% Section 301 on Chinese semiconductors (8541/8542), reported unchanged to 2027-06. Section 232 chips: 25% on a narrow set of advanced AI accelerators (2026-01-14), consumer GPUs not confirmed in scope. | 2026-11-07 | [10] [11] [12] [13] [14] [15] | De minimis suspended and IEEPA end: high. HTS Free: high. Section 301 forced-labor 10/12.5%: low-medium (secondary only). GPU/motherboard exclusion status after 2026-11-09: low (no post-expiry notice found, decision is imminent). |
| Canada | GST 5% federal + PST or HST by province (rate not re-fetched; CBSA page confirms GST/HST/PST apply). Collected at the border by courier/Canada Post, or at checkout by some platforms. | Mailed items <= **CAD 20**: no duty or tax (CBSA). Gifts <= CAD 60 exempt (not applicable to retail purchases). | CAD 20 (post). Courier Low Value Shipment (CLVS) program covers goods <= **CAD 3,300**, but CBSA has a moratorium on new participants. | CBSA 2026 tariff chapter pages were located but rates for 8471/8473.30 were not reached. Canada is an ITA member (expected Free): NOT verified. | Canada surtaxes on China-origin goods found only for steel/aluminium (and EVs, reportedly repealed 2026-03-01). No surtax found on computers or components. | 2026-11-07 | [16] [17] [18] | CAD 20 rule: high. CLVS: medium-high. Duty on PC parts: low. China surtax scope: medium. |
| Australia | GST 10% (rate from secondary sources; ATO page blocked). Overseas sellers/platforms collect GST at checkout for goods <= AUD 1,000 (large sellers above AUD 75,000 turnover); above AUD 1,000 GST at border. | AUD 1,000 (GST at point of sale for low-value goods). | AUD 1,000 informal-clearance / duty-free notion (ABF page blocked; not confirmed). | 8471 reported Free (ITA, duty-free since 1998 per Australian government submission; third-party tariff sites). Official Working Tariff not read. | None found. | 2026-11-07 | [19] [20] | medium (GST point-of-sale model), low (duty) |
| Japan | Consumption tax 10% (not re-fetched). Collected at the border by Japan Post/couriers. | JPY 10,000 total customs value: exempt from duty and consumption tax (Japan Customs FAQ 1006; page undated; counted per declaration, per package, split parcels combined). **Planned: exemption removed from 2028-04-01** (sec., PwC/BDO/VATupdate; passage into law unconfirmed). | JPY 10,000 (same rule). | 8471 reported Free (third-party tariff listing; official schedule not read). Simplified duty-rate table for personal imports: NOT verified. | None found. | 2026-11-07 | [21] [22] | JPY 10,000 current rule: high. 2028 reform: low-medium. Duty: low. |

### Goods shipped FROM China, by destination (summary)

| Destination | China-origin specifics | Confidence |
|---|---|---|
| EU | Low-value (<= EUR 150): EUR 3 flat duty per item category + EUR 2 handling fee + VAT (IOSS at checkout if the platform is registered). Above EUR 150: normal duty (expected 0% on ITA lines), import VAT. | medium |
| UK | <= GBP 135: UK VAT at checkout, no duty (relief in force), no import clearance fee when VAT is prepaid. Above GBP 135: import VAT + duty, Royal Mail/Parcelforce/courier fees. | medium-high |
| US | No de minimis. Section 301 on China applies by HTS line (see US row). No IEEPA tariff since 2026-02-24. Post-IEEPA replacements (Section 301 forced-labor 12.5% reported; Section 232 narrow) must be re-checked per HTS line on CBP/USTR. | low-medium |
| Canada | No China-specific surtax found for PC parts. Standard CAD 20 postal exemption otherwise duty+GST. | low-medium |
| Australia | GST at checkout up to AUD 1,000; no China-specific tariff found. | low-medium |
| Japan | JPY 10,000 exemption until the planned 2028 change; otherwise duty (expected Free) + 10% consumption tax. | medium |

## Carrier and payment fees

| Item | Fee / rule | Source | Date checked | Confidence |
|---|---|---|---|---|
| EU Union handling fee | EUR 2 per item (per tariff-category) from 2026-11-01 on small parcels from outside the EU, in addition to the EUR 3 duty. | [2] [3] | 2026-11-07 | medium |
| DHL Express Germany | "Duty Tax Processing Service" = 2% of fiscal charges, minimum EUR 12.50 per shipment (not applied when charges are exempt). Document dated 2024-12-26; PDF text unreadable here, figure comes from search excerpt of the DHL document. | [23] | 2026-11-07 | low-medium (may be outdated) |
| DHL Express France | Reseller page reports EUR 14.60 or 2.55% of advanced amount, whichever is higher. Official DHL France tariff not found. | [24] sec. | 2026-11-07 | low |
| Royal Mail / Parcelforce (UK) | Customs handling fee GBP 8 (Royal Mail) / GBP 12 (Parcelforce) when duty or import VAT is due; GBP 25 for full declaration over GBP 900. Royal Mail page itself blocked (403); figures from search excerpt. | [25] | 2026-11-07 | medium |
| Canada Post | Handling fee charged on dutiable/taxable mail (CBSA confirms a fee exists); CAD 9.95 is a secondary figure. Courier brokerage CAD ~15-35 per sec. sources. | [17] [18] sec. | 2026-11-07 | low |
| FedEx | Customs-clearance surcharge PDF (APAC, July 2026) exists; not read. UPS/FedEx US/EU brokerage pages: UPS "Access Denied", FedEx US page blocked. | [26] | 2026-11-07 | blocked |
| France national small-parcel tax | A French national tax (in force 2026-03-01) was suspended in favour of the EU duty (sec., Lexisveille). | [27] sec. | 2026-11-07 | low |
| Card FX / DCC | EU Regulation 2019/518 requires disclosure of currency-conversion charges as a % mark-up over the ECB reference rate and DCC disclosure (card payments in another currency); no cap, no ban. Typical bank card FX fee 1.5-3%: NO official source found, treat as an assumption. Practical rule: always pay in the seller's/local currency chosen by your card issuer, decline "pay in your currency" (DCC). | [28] | 2026-11-07 | medium (regulation), low (typical fee level) |

## Warranty across borders

| Topic | Rule | Source | Date checked | Confidence |
|---|---|---|---|---|
| EU legal guarantee | Directive (EU) 2019/771: **seller** liable for non-conformity existing at delivery and appearing within **2 years** (Art. 10); presumed existing at delivery if appearing within **1 year** (Art. 11, member states may extend to 2 years); consumer chooses repair or replacement, then price reduction or termination (Art. 13). Applies to sales to consumers by sellers directed at the EU. Buying from a non-EU seller without an EU presence: enforcement against that seller is practically harder; the guarantee still binds an EU-based seller/marketplace seller. | [29] | 2026-11-07 | high (text); medium (non-EU seller enforcement, my inference) |
| UK | Consumer Rights Act 2015 s.9: goods must be of satisfactory quality (price, durability, freedom from minor defects). Remedies in s.19 (30-day short-term right to reject, 6-month presumption: not verified on the pages read). Seller liability, not the manufacturer. | [30] | 2026-11-07 | high (s.9), medium (s.19/22 details) |
| US | No federal 2-year guarantee. Implied warranty of merchantability under the UCC (state law); manufacturer warranty is express and often limited to the US/seller channel. Not verified on an official page this session. | none read | 2026-11-07 | low |
| ASUS | Graphics-card warranty pages say period "may differ regionally, check with your purchase site". ASUS International Warranty PDF covers products bought and serviced within a listed country/region set, but the document was not confirmed to cover graphics cards or motherboards (PDF link 404 when fetched). Forum reports: no international GPU warranty. | [31] | 2026-11-07 | low-medium (regional is likely) |
| MSI | MSI warranty document: terms may differ by region; cross-region purchases via online stores are subject to the warranty of the country where the retailer processes the sale. Official MSI page blocked (403); statement from search excerpt of MSI document. | [32] | 2026-11-07 | medium (quoted from excerpt) |
| Gigabyte / AORUS | Warranty term and period vary by product and region; inquire with the shop of original purchase or the local office. Official page blocked (403); statement from search excerpt. | [33] | 2026-11-07 | medium |
| Sapphire | Claims go through the place of purchase; warranty varies by country/region; separate RMA desks by market (USA, Canada). Current official policy page not found (forum-quoted older terms). | [34] sec. | 2026-11-07 | low |
| Corsair | Warranty page redirected to help.corsair.com and returned 403. Worldwide vs regional: **not confirmed**. | [35] | 2026-11-07 | blocked |

Practical reading: for GPUs and motherboards, assume **regional warranty tied to the country of purchase** unless the maker's page for your model says otherwise. In the EU, the seller's 2-year legal guarantee is the reliable recourse and usually only if the seller is in the EU.

## Worked examples (illustrative)

Assumptions (illustrative, not quotes): FX 1 USD = 0.90 EUR and 1 USD = 0.75 GBP; card FX fee 2% (assumption, no official source); carrier fees as in the table above, sourced as low/medium confidence. Re-run with live values.

### Example 1: 300 USD GPU, US seller to France (buyer in FR), carrier DHL

| Step | Calculation | Amount |
|---|---|---|
| Goods | 300 USD | 300.00 USD |
| Shipping + insurance (assumed) | | 40.00 USD |
| Customs value (CV) | 340 USD x 0.90 | EUR 306.00 |
| Is the parcel <= EUR 150? | No (306 > 150): EUR 3 duty and EUR 2 handling fee NOT applicable (scope per [2]; handling-fee scope above EUR 150 not confirmed) | 0 |
| Duty | 0% (ITA; EU TARIC not verified, UK rate used as proxy, low confidence) | EUR 0.00 |
| Import VAT 20% (FR) | 306.00 x 20% | EUR 61.20 |
| Carrier disbursement fee (DHL FR, low-confidence figure) | max(14.60, 2.55% x 61.20 = 1.56) | EUR 14.60 |
| Card FX fee | 2% x 306.00 | EUR 6.12 |
| **Landed price (approx.)** | 306.00 + 0 + 61.20 + 14.60 + 6.12 | **about EUR 387.92** |

Note: the US 300 USD GPU may carry US tariffs only on export if made in China; no tariff is levied by the EU. VAT may also apply on the carrier fee (not added). The French 2-year legal guarantee from a US seller is hard to enforce; manufacturer warranty may be US-only.

### Example 2: 60 USD cooler, China seller to UK (buyer in GB)

| Step | Calculation | Amount |
|---|---|---|
| Goods | 60 USD x 0.75 | GBP 45.00 |
| Shipping (assumed, paid at checkout) | | GBP 8.00 |
| Consignment value for the GBP 135 test | goods only (shipping excluded when separately shown) | GBP 45.00 (<= 135) |
| Customs duty | GBP 135 relief in force: 0 (HMRC removal announced, no effective date on the page) | GBP 0.00 |
| UK VAT 20%, charged by seller at checkout | (45.00 + 8.00) x 20% | GBP 10.60 |
| Border clearance fee | none if seller collected VAT (point-of-sale scheme) | GBP 0.00 |
| Card FX fee | 2% x (53.00 + 10.60 = 63.60) | GBP 1.27 |
| **Landed price (approx.)** | 53.00 + 10.60 + 1.27 | **about GBP 64.87** |

If the seller is not VAT-registered or the order exceeds GBP 135: add import VAT at the border and a Royal Mail GBP 8 or Parcelforce GBP 12 handling fee. UK duty on a cooler (probably HS 8414.59 or 8473.30) not verified; 8473.30 was verified at 0%.

## Recent changes and pending changes (2025-2026)

| Date | Change | Status | Source | Confidence |
|---|---|---|---|---|
| 2025-08 | US suspended $800 de minimis for all countries | In force; re-confirmed by EO 2026-02-20 and CBP rule 2026-06-24 | [11] [12] | high |
| 2026-02-20 | SCOTUS: IEEPA does not authorise the tariffs. EO ends IEEPA tariffs; CBP stops collection 2026-02-24. No automatic refund; guidance pending. | In force | [11] [12] | high |
| 2026-02-24 to 2026-07-24 | Section 122 10% surcharge | Expired 2026-07-24 | [13] | high |
| 2026-07-24 | Section 301 "forced labor" tariffs 10%/12.5% on 60 economies replace Section 122 (secondary) | Reported in force; excess-capacity investigation still open | search excerpts (Kroll, RVIA) | low-medium |
| 2026-06-24 | CBP interim final rule: de minimis suspended indefinitely for non-postal modes; comments closed 2026-07-24 | In force | [12] | high |
| 2026-01-14 | Section 232: 25% on a narrow set of advanced AI chips | In force, Phase 2 broader tariffs pending | search excerpts (Thomson Reuters, KPMG) | medium |
| 2026-11-09/10 | US Section 301 exclusion deadline (178 exclusions, 9903.88.69/.70); no extension found | **Pending, decision expected within days** | [14] | medium |
| 2026-07-01 | EU: EUR 150 duty exemption abolished; EUR 3/item flat duty until 2028-07-01 | In force | [2] | high |
| 2026-11-01 | EU: EUR 2 Union handling fee on small parcels | In force per Commission page; Council adopted customs reform 2026-09-03 (press) | [2] [3] | medium |
| 2026-07-13 | UK: HMRC policy paper to remove GBP 135 duty relief; date not stated on page (sec.: by 2028-10, earlier March 2029) | Pending | [8] | medium (change), low (date) |
| 2026-04 (planned 2028-04-01) | Japan: end of JPY 10,000 consumption-tax exemption on low-value imports | Pending / possibly enacted | [22] | low-medium |
| 2026-03-01 | Canada: 100% EV surtax on China-origin reportedly repealed; steel/aluminium surtax continues | secondary | sec. | low |

## Not verified / gaps

1. EU TARIC duty for 8471/8473.30/8542/8523/8504.40/8528.52 not read (UK Global Tariff used as a proxy for two codes only). UK codes 8504.40, 8523.51, 8528.52, 8542 not queried.
2. US: whether GPUs and motherboards (8473.30.1180/.5100) are inside the 178 Section 301 exclusions and what happens after 2026-11-09; 8542 rate; Section 301 forced-labor tariff text and rates; postal-route duty rules; the CSMS bulletin numbers. Federal Register site returned an access-request page (blocked); the same document was read on govinfo.gov. USTR and Kroll fetches were rate-limited.
3. VAT/GST rates for UK 20%, Canada 5%, Australia 10%, Japan 10%, ES/IT/NL (EU) not confirmed on a primary page this session. Commission VAT rates page gives no table.
4. Canada and Australia official duty rates, Australian ABF/ATO pages (403), Japan simplified duty-rate table.
5. Carrier fees: DHL France, UPS, FedEx official pages not obtained; Royal Mail page blocked (403); economie.gouv.fr page (dated 2026-11-02) blocked (403) so the handling-fee scope (per item or per category, parcels <= EUR 150 only?) is unconfirmed.
6. Whether the EUR 3 duty and EUR 2 fee apply to consignments above EUR 150 (my reading: no, EUR 3 applies <= EUR 150; fee scope unclear).
7. Card FX fee levels: no official figure; 2% is an assumption.
8. Manufacturer warranty: MSI, Gigabyte, Corsair official pages blocked; ASUS GPU-specific international coverage unconfirmed; Sapphire policy page not found. US implied warranty and CRA s.19/22 not read.
9. Intra-EU: the Your Europe page confirms EUR 10,000 but did not explain OSS in detail; EU "VAT in the Digital Age"/IOSS EUR 150 rule not read on an official page.

## Sources (numbered)

1. EU Commission, VAT e-commerce page — https://taxation-customs.ec.europa.eu/taxation/vat/vat-ecommerce_en — HTTP 404 on 2026-11-07 (not used).
2. EU Commission, customs reform (EUR 3 duty, end of EUR 150 exemption, Union handling fee) — https://taxation-customs.ec.europa.eu/customs/eu-customs-reform_en — checked 2026-11-07.
3. Press on EU handling fee / Council 2026-09-03 — https://www.eunews.it/en/2026/09/03/eu-council-gives-the-green-light-to-customs-reform-from-1-november-a-handling-fee-for-small-parcels/ ; https://www.taxually.com/blog/eu-handling-fee-3-euro-customs-duty (secondary) — 2026-11-07.
4. EU Commission, VAT rates framework — https://taxation-customs.ec.europa.eu/taxation/vat/vat-rates_en — checked 2026-11-07 (no table).
5. Secondary VAT tables: https://taxfoundation.org/data/all/eu/value-added-tax-vat-rates-europe/ ; https://www.taxenlight.com/en/eu-vat-rates/ — 2026-11-07.
6. Your Europe, cross-border VAT (EUR 10,000 threshold) — https://europa.eu/youreurope/business/taxation/vat/cross-border-vat/index_en.htm — 2026-11-07.
7. UK Trade Tariff API: https://www.trade-tariff.service.gov.uk/api/v2/commodities/8471800000 and .../8473302000 — 2026-11-07.
8. HMRC policy paper, Reforming customs rules for low value imports — https://www.gov.uk/government/publications/reforming-customs-rules-for-low-value-imports — published 2026-07-13, updated 2026-10-28; checked 2026-11-07.
9. GOV.UK, VAT and overseas goods sold directly to customers in the UK — https://www.gov.uk/guidance/vat-and-overseas-goods-sold-directly-to-customers-in-the-uk — 2026-11-07.
10. USITC HTS REST search: https://hts.usitc.gov/reststop/search?keyword=8471.80 (also 8473.30, 8504.40, 8528.52, 8523.51, 9903.88.03) — 2026-11-07.
11. GHY International summary of Section 122/IEEPA/de minimis (secondary, cites CBP) — https://www.ghy.com/?p=25869 — 2026-11-07.
12. CBP interim final rule CBP Dec. 26-12 (2026-06-24), on govinfo — https://www.govinfo.gov/content/pkg/FR-2026-06-24/html/2026-12670.htm — 2026-11-07. Federal Register original (federalregister.gov): blocked (access-request page).
13. STR Trade, Section 122 tariffs (expired) — https://www.strtrade.com/trade-news-resources/tariff-actions-resources/section-122-tariffs — search result only, 2026-11-07.
14. Federal Register 2025-12-01 (USTR Section 301 exclusions extension to 2026-11-09) — https://www.govinfo.gov/content/pkg/FR-2025-12-01/html/2025-21671.htm — 2026-11-07.
15. Section 232 AI chips (secondary): https://www.whitecase.com/insight-alert/president-trump-orders-narrowly-targeted-25-section-232-tariff-certain-advanced ; Kroll https://www.kroll.com/en/publications/a-tale-of-tariff-substitution (fetch rate-limited; search excerpt only) — 2026-11-07.
16. CBSA, mail/courier (CAD 20) — https://www.cbsa-asfc.gc.ca/import/courier/menu-eng.html — 2026-11-07.
17. CBSA, Courier Low Value Shipment program — https://www.cbsa-asfc.gc.ca/import/courier/lvs-efv/comm-eng.html — search result excerpt, 2026-11-07.
18. CBSA 2026 Customs Tariff index — https://www.cbsa-asfc.gc.ca/trade-commerce/tariff-tarif/2026/html/tblmod-1-eng.html — 2026-11-07 (rates not reached).
19. ATO, GST on low value imported goods — https://www.ato.gov.au/businesses-and-organisations/international-tax-for-business/gst-for-non-resident-businesses/gst-on-low-value-imported-goods — 403 blocked 2026-11-07 (listed in search, last updated 2025-09-11 per snippet).
20. ABF duty and GST page — https://www.abf.gov.au/importing-exporting-and-manufacturing/importing/how-to-import/duty-and-gst — 403 blocked.
21. Japan Customs FAQ 1006 (JPY 10,000) — https://www.customs.go.jp/english/c-answer_e/imtsukan/1006_e.htm — undated, checked 2026-11-07.
22. Japan 2026 tax reform (secondary): https://www.pwc.com/jp/en/taxnews/pdf/jtu-20260114-en.pdf ; https://www.vatupdate.com/2026/01/13/japan-2026-tax-reform-key-consumption-tax-changes-and-timeline-for-low-value-imports — 2026-11-07.
23. DHL Express Germany clearance terms (PDF dated 2024-12-26) — https://www.dhl.de/content/dam/images/Express/downloads/zollinformation/zollinformationen-und-dokumente/dhl-express-auftragsbedingungen-gebuehren-zollabfertigung-en.pdf — text unreadable; figure from search excerpt.
24. Reseller page quoting DHL France fee — https://parceldetect.com/faq/customs-disbursement-fees (secondary).
25. Royal Mail fee page — https://www.royalmail.com/receiving-mail/pay-a-fee — 403 blocked; amounts from search excerpt.
26. FedEx APAC customs-clearance surcharge PDF — https://www.fedex.com/content/dam/fedex/apac-asia-pacific/downloads/fedex-customs-clearance-surcharge-20july2026.pdf (not read); UPS import page returned "Access Denied".
27. Lexisveille on French small-parcel tax suspension (secondary) — https://lexisveille.fr/petits-colis-importes-entree-en-vigueur-au-1er-juillet-du-droit-de-douane-europeen-et-suspension-de ; official French page https://www.economie.gouv.fr/particuliers/mes-droits-conso/bien-consommer/taxes-sur-les-petits-colis-comment-ca-marche — 403 blocked.
28. Regulation (EU) 2019/518 — https://www.legislation.gov.uk/eur/2019/518/data.html (retained text, excerpts via search) — 2026-11-07.
29. Directive (EU) 2019/771 — https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:32019L0771 — checked 2026-11-07 (Arts. 10, 11, 13).
30. Consumer Rights Act 2015 s.9 — https://www.legislation.gov.uk/ukpga/2015/15/section/9 — 2026-11-07.
31. ASUS warranty pages (search): https://www.asus.com/au/support/article/1100/ ; https://asus.com/support/images/upload/file/20240607114753061_E23952_International_warranty_V2.pdf (404 on fetch) ; https://www.asus.com/support/warranty-policy/ (404).
32. MSI warranty — https://www.msi.com/page/warranty — 403 blocked; excerpt from https://www.qvc.com/footers/electronics/pdf/E325241_MSI_Warranty.pdf via search.
33. Gigabyte warranty — https://www.gigabyte.com/eu/Support/Warranty/Graphics-Card — 403 blocked; excerpt via search.
34. Sapphire warranty/contact (secondary excerpts) — https://www.sapphiretech.com/en/contact-us
35. Corsair warranty — https://help.corsair.com/hc/en-us/articles/360033067832 — 403 blocked.
