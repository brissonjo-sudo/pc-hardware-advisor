# R3 Retailer criteria and sites to avoid
Collected: 2026-11-07 · Model: haiku

Legend: "fetched" = text read from the official page via WebFetch on 2026-11-07 (WebFetch answers are a small-model summary, quotes checked against the summary only). "search" = secondary source or snippet from WebSearch on 2026-11-07, not opened. Confidence: high = official text fetched and consistent; medium = secondary or partial; low = single or unverified source.

## Criteria

| Criterion | How to check on a page | Why | Legal anchor if any | Source | Confidence |
|---|---|---|---|---|---|
| Seller clearly identified (direct / marketplace / refurbisher / private) | Legal name, postal address, phone or email on the page or imprint. On a marketplace, "sold by" line and a trader or non-trader statement. | Buyer must know who holds warranty and withdrawal rights. | Dir. 2011/83/EU Art. 6(1)(b)-(c) (fetched). Marketplace must say whether the third-party seller is a trader, Art. 6a(1)(b) of Dir. 2011/83 as inserted by Dir. (EU) 2019/2161 (fetched via summary). | [1], [2] | high (Art. 6(1)(b)-(c)); medium (marketplace trader flag) |
| Total price incl. VAT shown before checkout | Price label states "incl. VAT" or "inclusive of taxes"; total visible before payment step. | Hidden fees and VAT are a common complaint. | Dir. 2011/83/EU Art. 6(1)(e): total price inclusive of taxes (fetched). | [2] | high |
| Shipping cost and delivery time visible before checkout | Shipping fee and delivery date/range on product or cart page, before the payment step. | Shipping surprises at checkout. | Dir. 2011/83/EU Art. 6(1)(e): additional freight/delivery charges must be disclosed, or stated as payable (fetched). Delivery-date rule not retrieved. | [2] | high (costs); low (delivery date, not verified) |
| Real stock shown, not a vague delay | Stock status per SKU ("in stock: N units" or "ships in X days"); no "available soon" without date. | Preorders and phantom stock are a known trap. | None verified. | Not verified | low |
| Price-reduction reference visible or deducible | Any strike-through or "-X %" must be backed by the lowest price in the previous 30 days. Look for a price history or a dated price change. | Stops inflated "list price" discounts. | Dir. 98/6/EC Art. 6a(1)-(2), inserted by Dir. (EU) 2019/2161 Art. 2(1): prior price = lowest price applied during a period of at least 30 days before the reduction (fetched). CJEU C-330/23 (Aldi Süd) applies this to percentage and promotional wording (search). | [1], [4], [5] | high (Art. 6a); medium (CJEU ruling) |
| Price update date visible or deducible | Date of last price change, or a price history graph. Not required by law: treat as best practice. | Needed to apply the 30-day rule. | Implied by Art. 6a (30-day lookback) but no explicit date duty found. | [1] | medium |
| Withdrawal right: 14 days, usable from buyer's country | Returns page states 14 days from receipt; check that return address and carrier are accessible from the buyer's country. | EU consumer right. Exceptions exist (Art. 16). | Dir. 2011/83/EU Art. 9(1)-(2): 14 days, running from possession of goods (fetched). | [2] | high |
| Legal guarantee 2 years usable from buyer's country | Warranty page states 2-year legal guarantee for EU buyers; check that the seller ships to that country. | Legal conformity guarantee applies regardless of seller policy. | Dir. (EU) 2019/771 Art. 10(1): seller liable for lack of conformity appearing within two years of delivery (fetched). Art. 11 summary from the fetch conflicts with Art. 10 on option periods; not resolved. | [3] | high (Art. 10(1)); low (Art. 11 detail) |
| Secure payment, no mandatory bank transfer | Card, PayPal or other platform payment offered; no "bank transfer only" and no payment outside the site. | Bank-transfer-only is a common fake-shop signal. | Not verified in law. Practice guidance from consumer checklists (search). | [6], [7] | medium |
| Verifiable history and reputation | Company register entry, VAT number, company age; independent reviews checked on more than one source. | Fake shops are often days old. | DSA Art. 30 requires marketplaces to trace traders (secondary). | [8], [9] | medium |
| No fake or purchased reviews | Review page explains how reviews are verified (purchase proof, dates). | Reviews can be bought or fabricated. | Dir. 2005/29/EC Art. 7(6) and Annex I entries on fake reviews (search). UK DMCC Act 2024 bans fake reviews from 6 April 2025 (search). US FTC 16 CFR Part 465 (search). | [10], [11], [12] | medium |
| Pages readable without circumvention | Page loads and shows terms without blocked captcha bypass, login wall or geo block that needs a workaround. | Plugin must not recommend bypassing bot protection. | Project rule, not a legal anchor. | n/a | high (as a project rule) |

## Official scam / fake-shop resources by country

| Country | Resource | What it offers | Date checked | Source | Confidence |
|---|---|---|---|---|---|
| Austria | Watchlist Internet (watchlist-internet.at) | Fake-shop list and reader reports. Homepage returned HTTP 403 on 2026-11-07, so the list was not read directly. | 2026-11-07 (blocked) | [7] (referenced) | medium (existence), low (content read) |
| Germany | Verbraucherzentrale fake-shop warnings | Consumer-centre fake-shop list and warnings. Fetch blocked by rate limit. | 2026-11-07 (blocked) | [13] (search) | low |
| Germany | Fakeshop-Finder (fakeshop-finder.de) | Third-party checker that lists shops flagged by Watchlist Internet and similar sources. Fetch blocked by rate limit. Not an official authority. | 2026-11-07 (blocked) | [14] (search) | low |
| France | SignalConso (signal.conso.gouv.fr), DGCCRF | Official reporting platform for suspicious commercial practices. Reported about 80 sites blocked since January 2025. Fetch blocked by rate limit. | 2026-11-07 (blocked) | [15], [16] (search) | medium |
| France | PHAROS (internet-signalement.gouv.fr) | Reporting of illegal online content and fraud. Named as the route for fraud or scam pages in a secondary source. Not opened. | 2026-11-07 | [16] (search) | low |
| UK | Action Fraud (actionfraud.police.uk) | Online shopping fraud guidance and reporting. Fetch blocked by rate limit. | 2026-11-07 (blocked) | Not retrieved | low |
| Australia | Scamwatch (scamwatch.gov.au) | Online shopping scam guidance. Fetch blocked by rate limit. | 2026-11-07 (blocked) | Not retrieved | low |
| US | FTC (ftc.gov) | Consumer alerts; Consumer Review Rule enforcement. Not fetched. | 2026-11-07 | [11], [12] (search) | medium |

## Hardware scam patterns

| Pattern | Red flags | Source | Confidence |
|---|---|---|---|
| Relabelled older GPUs (e.g. older NVIDIA chips sold as newer models) | Name in GPU-Z differs from the die or device ID; GPU-Z shows [FAKE] prefix in newer versions. Check the GPU-Z version first, since older versions may flag genuine cards. | [17], [18] | medium (2018 GPU-Z feature; current list not checked) |
| Used GPU with harvested or swapped VRAM, or tampered stickers | Memory type and size in GPU-Z differ from the spec database; screws or sticker missing or mismatched. | [18] | medium |
| Fake-capacity SSDs and flash drives | No source found in this run. Known pattern in tech press, not verified here. | Gap | low |
| Used GPU sold with unrelated GPU-Z screenshot | Screenshot not matching the listed serial, date or seller; ask for a live check. | Not verified in this run; pattern named in brief. | low |
| Mining cards sold as new or lightly used | No warranty or unusual wear claims; seller refuses inspection. | Not verified in this run. | low |
| "Too cheap" marketplace listings | Price far below market; new account; stock photo; no returns policy. | [6], [7] (checklists, search) | medium |
| Payment outside the platform | Request for bank transfer, WhatsApp or direct payment outside the marketplace. | [6], [7] (checklists, search) | medium |
| Drop-shipping storefronts with imitation brand names | Brand name slightly altered, imprint names a different company, very recent domain. | Trustpilot reviews of hardware-branded shops (unverified user reports), [19]. | low |
| Review manipulation | Many reviews in a short window; generic praise; reviews from non-buyers. | [10], [11], [12] | medium |

## Sites or seller types to avoid (only sourced cases)

No individual site is named. No consumer authority or major outlet page was retrieved in this run that names a PC component seller. Trustpilot and fakeshop-finder entries are user reports or third-party checks and are not treated as established.

Seller types to avoid, with source basis:
- Sellers with no imprint or company identity: basis checklists and Watchlist claims (not opened). Confidence medium.
- Shops that accept only bank transfer or payment outside the platform: basis checklists. Confidence medium.
- Shops with strike-through prices not backed by a 30-day lowest price: basis Art. 6a, Dir. 98/6/EC. Confidence high for the rule, medium for enforcement examples.
- Shops with mass fake or purchased reviews: basis UK DMCC and US FTC rules (secondary). Confidence medium.

## Reputation sources and limits

| Source | Limit | Source reference | Confidence |
|---|---|---|---|
| Trustpilot | Reviews can be bought. Trustpilot won a UK High Court case against review sellers (search). Trustpilot reports removing about 3.3 million fake reviews in 2023 (search, unverified figure). | [19], [20] | medium |
| Google reviews | Which? reported that Google and Facebook did not filter fake reviews well. Article undated in the search result. | [21] | low |
| Trusted Shops | Buyer Protection covers non-delivery and refund failure; warranty cases excluded. Sources conflict on the covered order value (EUR 100 vs EUR 2,500). Shop must answer 95% of inquiries within 5 days. | [22] | medium |
| Reddit | Not researched in this run. | n/a | low |
| Klicksafe checklist | Consumer checklist for fake shops; no date verified. | [6] | medium |

## Not verified / gaps

- Watchlist Internet list not read (HTTP 403).
- Verbraucherzentrale, SignalConso, Scamwatch, Action Fraud, Fakeshop-Finder not read (rate-limited). Their descriptions above are from search snippets only.
- EUR-Lex text of Dir. (EU) 2019/2161 Art. 7(6) and Annex I not read; marketplace trader flag and reviews rule taken from secondary summaries.
- EUR-Lex text of DSA Art. 30 not read; taken from secondary summaries.
- CJEU C-330/23 (Aldi Süd) not read from curia; taken from a law-firm summary and a search snippet. Verify case number and date.
- Dir. (EU) 2019/771 Art. 11 detail conflicts with Art. 10 in the fetch summary. Not resolved.
- FTC 16 CFR Part 465: the eCFR text was not fetched. Penalty amount (USD 53,088 per violation) comes from a single secondary source; low confidence.
- UK CMA investigations into five businesses (27 March 2026) come from a search snippet without a primary source. Low confidence.
- UK DMCC Act fake-review ban date (6 April 2025) from a secondary source. Medium confidence.
- No source found for fake-capacity SSD or flash scams, or for used-GPU screenshot fraud.
- Delivery-date obligation and payment-security rules (PSD2) not researched.
- Reddit not researched.

## Sources (numbered)

1. Dir. 98/6/EC as amended by Dir. (EU) 2019/2161, Art. 6a (fetched 2026-11-07): https://eur-lex.europa.eu/eli/dir/2019/2161/oj/eng
2. Dir. 2011/83/EU, Arts. 6, 9 (fetched 2026-11-07): https://eur-lex.europa.eu/eli/dir/2011/83/oj/eng
3. Dir. (EU) 2019/771, Arts. 10-11 (fetched 2026-11-07, partial): https://eur-lex.europa.eu/eli/dir/2019/771/oj/eng
4. CJEU press release on C-330/23, Aldi Süd (search, not opened, 2026-11-07): https://curia.europa.eu/jcms/upload/docs/application/pdf/2024-09/cp240152en.pdf
5. Baker McKenzie summary of CJEU 30-day ruling (search, 2026-11-07): https://globallitigationnews.bakermckenzie.com/2024/10/15/european-union-the-cjeu-confirms-that-a-price-reduction-must-be-calculated-based-on-the-lowest-price-in-the-last-30-days/
6. Klicksafe checklist, fake shops (search, 2026-11-07): https://www.klicksafe.de/fileadmin/cms/download/Material/Checklisten/checkliste_echt_oder_nicht_-_so_erkennst_du_fake-shops_im_internet_klicksafe.pdf
7. Watchlist Internet (referenced; homepage HTTP 403 on 2026-11-07): https://www.watchlist-internet.at/
8. Freshfields, DSA and online marketplaces (search, 2026-11-07): https://technologyquotient.freshfields.com/post/102lx12/dsa-decoded-9-the-dsa-and-online-marketplaces
9. CCPC, Digital Services Act (search, 2026-11-07): https://www.ccpc.ie/enforcement-and-regulation/digital/the-digital-services-act
10. Directive 2005/29/EC Art. 7(6) and Annex I, via legislation.gov.uk (search, 2026-11-07): https://www.legislation.gov.uk/eudr/2019/2161/article/3/data.html
11. FTC Consumer Review Rule, 16 CFR Part 465 (search, 2026-11-07): https://federal-regs.com/title/16/part-465/
12. Arnold & Porter, FTC warning letters over consumer review rule, Jan 2026 (search, 2026-11-07): https://www.arnoldporter.com/en/perspectives/blogs/consumer-products-and-retail-navigator/2026/01/ftc-warning-letters-over-consumer-review-rule
13. Verbraucherzentrale fake-shop warnings (search, 2026-11-07, not opened): https://www.techbook.de/shop-pay/shops-marktplaetze/verbraucherzentrale-warnt-vor-fake-shops
14. Fakeshop-Finder (search, 2026-11-07, not opened): https://warnung.fakeshop-finder.de/2026_02/stilhausfreiburg_com.html
15. SignalConso, DGCCRF (search, 2026-11-07, not opened): https://signal.conso.gouv.fr/
16. Journal de l'Economie, about 80 sites blocked in 2025 (search, 2026-11-07): https://www.journaldeleconomie.fr/arnaques-en-ligne-80-sites-deja-bloques-en-2025/
17. HotHardware, GPU-Z v2.12.0 fake NVIDIA detection (search, 2026-11-07; date unverified, around 2018): https://hothardware.com/news/gpu-z-v2120
18. SlashGear, counterfeit RTX GPU warning signs (search, 2026-11-07; date unknown): https://www.slashgear.com/1925790/check-if-high-end-nvidia-rtx-gpu-is-counterfeit-biggest-warning-signs
19. Trustpilot, hardware-branded shop reviews (user reports, unverified, search, 2026-11-07): https://de.trustpilot.com/review/pimlicohardware.com
20. Trustpilot press, court orders against review sellers (search title only, 2026-11-07): https://press.trustpilot.com/trustpilot-secures-first-court-orders-banning-businesses-soliciting-fake-reviews
21. Retail Systems, Which? on Facebook, Google and Trustpilot fake reviews (undated, search, 2026-11-07): https://www.retail-systems.com/rs/Facebook_Google_And_Trustpilot_Failing_To_Filter_Out_Fake_Reviews.php
22. Trusted Shops Buyer Protection help article (search, 2026-11-07): https://help.etrusted.com/hc/en-gb/articles/23970803902354-What-is-the-Buyer-Protection
